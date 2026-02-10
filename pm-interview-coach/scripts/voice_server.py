#!/usr/bin/env python3
"""
Voice Web UI server for PM interview practice.

Bridges Claude Code (sends questions, requests recordings) with a browser UI
(displays questions, records audio, detects silence, uploads for transcription).

Usage:
    python voice_server.py [--port 8420] [--model api|local] [--whisper-model base]
"""

import argparse
import json
import os
import queue
import tempfile
import threading
import time
import webbrowser

from flask import Flask, Response, jsonify, request, send_file

# Import transcription functions from voice_input.py (same directory)
import voice_input

app = Flask(__name__)

# Server state
event_queue = queue.Queue()
record_event = threading.Event()
record_result = {"data": None}
record_lock = threading.Lock()
transcription_model = "api"
whisper_model_name = "base"


@app.route("/")
def index():
    """Serve the voice UI HTML."""
    html_path = os.path.join(os.path.dirname(__file__), "voice_ui.html")
    return send_file(html_path, mimetype="text/html")


@app.route("/health")
def health():
    """Lightweight health check — returns instantly (unlike /events which blocks 30s)."""
    return jsonify({"status": "ok", "model": transcription_model})


@app.route("/reset", methods=["POST"])
def reset():
    """Clear stale state between sessions. Call at the start of each new session."""
    # Drain event queue
    while not event_queue.empty():
        try:
            event_queue.get_nowait()
        except queue.Empty:
            break
    # Clear record state
    with record_lock:
        record_event.clear()
        record_result["data"] = None
    return jsonify({"ok": True})


@app.route("/message", methods=["POST"])
def message():
    """Claude sends a message to display in the browser."""
    data = request.get_json(force=True)
    event_queue.put({
        "type": "message",
        "role": data.get("role", "interviewer"),
        "text": data.get("text", ""),
        "phase": data.get("phase", ""),
    })
    return jsonify({"ok": True})


@app.route("/events")
def events():
    """Browser long-polls for new events. Returns after an event or 30s timeout."""
    try:
        event = event_queue.get(timeout=30)
        return jsonify(event)
    except queue.Empty:
        return jsonify({"type": "heartbeat"})


@app.route("/record", methods=["POST"])
def record():
    """
    Claude requests a recording. Blocks until the browser records and uploads audio.
    Returns the same JSON shape as voice_input.py: {"text", "duration_seconds", "total_seconds"}
    """
    data = request.get_json(force=True)
    read_delay = data.get("read_delay", 0)
    silence_duration = data.get("silence_duration", 10)
    question_type = data.get("question_type", "")
    phase_number = data.get("phase_number", 0)

    with record_lock:
        # Reset state for this recording
        record_event.clear()
        record_result["data"] = None

    # Tell the browser to start recording
    event_queue.put({
        "type": "record_start",
        "read_delay": read_delay,
        "silence_duration": silence_duration,
        "question_type": question_type,
        "phase_number": phase_number,
    })

    # Block until browser submits audio or timeout (10 min)
    got_result = record_event.wait(timeout=600)

    with record_lock:
        if not got_result:
            return jsonify({"text": "", "duration_seconds": 0, "total_seconds": 0, "timeout": True})
        if record_result["data"] is None:
            return jsonify({"text": "", "duration_seconds": 0, "total_seconds": 0})
        return jsonify(record_result["data"])


@app.route("/text", methods=["POST"])
def text_input():
    """Browser submits text input (new answer). Unblocks pending /record call."""
    data = request.get_json(force=True)
    text = data.get("text", "").strip()

    result = {
        "text": text,
        "duration_seconds": 0,
        "total_seconds": 0,
    }

    with record_lock:
        record_result["data"] = result
        record_event.set()

    return jsonify({"ok": True})


@app.route("/correction", methods=["POST"])
def correction():
    """Browser submits an edit to a previous transcript. Fire-and-forget, does not unblock /record."""
    data = request.get_json(force=True)
    text = data.get("text", "").strip()
    # Log the correction for debugging; Claude will see it in the session log
    print(f"Transcript correction received: {text[:80]}...")
    return jsonify({"ok": True})


@app.route("/end", methods=["POST"])
def end():
    """Claude signals session end. Pushes session_end event to the browser."""
    data = request.get_json(force=True)
    event_queue.put({
        "type": "session_end",
        "message": data.get("message", "Session complete."),
    })
    return jsonify({"ok": True})


@app.route("/audio", methods=["POST"])
def audio():
    """Browser uploads recorded audio blob for transcription."""
    wall_start = time.time()

    audio_file = request.files.get("audio")
    duration = float(request.form.get("duration", 0))

    if audio_file is None:
        with record_lock:
            record_result["data"] = {"text": "", "duration_seconds": 0, "total_seconds": 0}
            record_event.set()
        event_queue.put({"type": "transcript", "text": "", "duration_seconds": 0, "total_seconds": 0})
        return jsonify({"ok": True})

    # Save uploaded audio to a temp file
    suffix = ".webm"
    content_type = audio_file.content_type or ""
    if "mp4" in content_type:
        suffix = ".mp4"

    tmp = tempfile.NamedTemporaryFile(suffix=suffix, delete=False)
    audio_file.save(tmp.name)
    tmp.close()

    # Convert to WAV for transcription (Whisper API accepts webm, but local needs wav)
    wav_path = None
    transcode_path = tmp.name
    try:
        if transcription_model == "local":
            wav_path = _convert_to_wav(tmp.name)
            if wav_path:
                transcode_path = wav_path
            else:
                print("Warning: ffmpeg not found, transcribing raw audio (quality may be reduced)")

        # Transcribe
        event_queue.put({"type": "transcribing"})
        if transcription_model == "api":
            text = voice_input.transcribe_api(transcode_path)
        else:
            text = voice_input.transcribe_local(transcode_path, whisper_model_name)
    except SystemExit as e:
        text = ""
        print(f"Transcription error (SystemExit): {e}")
    except Exception as e:
        text = ""
        print(f"Transcription error: {e}")
    finally:
        os.unlink(tmp.name)
        if wav_path and os.path.exists(wav_path):
            os.unlink(wav_path)

    total_seconds = round(time.time() - wall_start + duration, 1)
    result = {
        "text": text or "",
        "duration_seconds": round(duration, 1),
        "total_seconds": total_seconds,
    }

    with record_lock:
        record_result["data"] = result
        record_event.set()
    event_queue.put({
        "type": "transcript",
        "text": result["text"],
        "duration_seconds": result["duration_seconds"],
        "total_seconds": result["total_seconds"],
    })
    return jsonify({"ok": True})


def _convert_to_wav(input_path):
    """Convert audio file to WAV using ffmpeg."""
    import subprocess
    wav_path = input_path + ".wav"
    try:
        subprocess.run(
            ["ffmpeg", "-y", "-i", input_path, "-ar", "16000", "-ac", "1", wav_path],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True,
        )
        return wav_path
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def main():
    parser = argparse.ArgumentParser(description="Voice Web UI server for PM interviews")
    parser.add_argument("--port", type=int, default=8420, help="Port to listen on (default: 8420)")
    parser.add_argument("--model", choices=["api", "local"], default="local",
                        help="Transcription backend (default: local)")
    parser.add_argument("--whisper-model", default="base",
                        help="Local whisper model size (default: base)")
    parser.add_argument("--no-browser", action="store_true",
                        help="Don't auto-open browser on startup")
    args = parser.parse_args()

    global transcription_model, whisper_model_name
    transcription_model = args.model
    whisper_model_name = args.whisper_model

    print(f"Voice UI server starting on http://localhost:{args.port}")
    print(f"Transcription: {args.model}" + (f" ({args.whisper_model})" if args.model == "local" else ""))

    if not args.no_browser:
        threading.Timer(1.0, webbrowser.open, args=[f"http://localhost:{args.port}"]).start()

    app.run(host="127.0.0.1", port=args.port, debug=False, threaded=True)


if __name__ == "__main__":
    main()
