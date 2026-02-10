#!/usr/bin/env python3
"""
Voice input for PM interview practice.
Records audio via silence detection, transcribes via Whisper, outputs JSON.

Usage:
    python voice_input.py [--model api|local] [--whisper-model base]
                          [--silence-duration 3] [--max-duration 600]
                          [--read-delay 6]

Output (stdout): {"text": "...", "duration_seconds": 42.5, "total_seconds": 55.0}
Status messages go to stderr.

Requires:
    - sounddevice, scipy (recording)
    - openai (API mode) or whisper (local mode)
    - OPENAI_API_KEY env var for API mode
"""

import argparse
import json
import os
import platform
import subprocess
import sys
import tempfile
import time

import numpy as np


def beep():
    """Play a short beep sound to signal recording start/end."""
    try:
        if platform.system() == "Darwin":
            subprocess.Popen(
                ["afplay", "/System/Library/Sounds/Tink.aiff"],
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            )
        elif platform.system() == "Linux":
            subprocess.Popen(
                ["paplay", "/usr/share/sounds/freedesktop/stereo/bell.oga"],
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            )
    except Exception:
        pass  # Non-critical — skip silently


def print_status(msg):
    """Print status messages to stderr so stdout stays clean for JSON."""
    print(msg, file=sys.stderr, flush=True)


def check_microphone():
    """Verify microphone is accessible. Exit with help if not."""
    try:
        import sounddevice as sd
        devices = sd.query_devices()
        default_input = sd.query_devices(kind="input")
        if default_input is None:
            raise RuntimeError("No input device found")
        return True
    except Exception as e:
        print_status(f"Error: Could not access microphone — {e}")
        print_status("")
        print_status("Troubleshooting:")
        print_status("  macOS: System Settings → Privacy & Security → Microphone")
        print_status("         Make sure your terminal app has microphone access.")
        print_status("  Linux: Check that pulseaudio/pipewire is running and your mic is not muted.")
        print_status("  All:   pip install sounddevice scipy")
        sys.exit(1)


def record_with_silence_detection(silence_duration=3.0, max_duration=600,
                                  sample_rate=16000, threshold_factor=2.0):
    """
    Record audio from the default microphone.
    Stops after `silence_duration` seconds of silence once speech has been detected,
    or after `max_duration` seconds total.

    Returns (numpy array, duration in seconds).
    """
    import sounddevice as sd

    block_duration = 0.1  # 100ms blocks
    block_size = int(sample_rate * block_duration)
    frames = []
    speech_detected = False

    # Calibrate noise floor with a brief sample
    print_status("Calibrating... stay quiet for a moment.")
    calibration = sd.rec(int(sample_rate * 0.5), samplerate=sample_rate,
                         channels=1, dtype="float32")
    sd.wait()
    noise_floor = np.sqrt(np.mean(calibration ** 2))
    threshold = max(noise_floor * threshold_factor, 0.005)

    print_status("Recording... speak your answer. "
                 f"Will auto-stop after {silence_duration:.0f}s of silence.")

    recording = True
    start_time = time.time()
    silence_start = start_time  # Start counting silence immediately

    def callback(indata, frame_count, time_info, status):
        nonlocal speech_detected, silence_start, recording
        frames.append(indata.copy())

        rms = np.sqrt(np.mean(indata ** 2))

        if rms > threshold:
            speech_detected = True
            silence_start = None
        else:
            if silence_start is None:
                silence_start = time.time()
            elif time.time() - silence_start >= silence_duration:
                recording = False

    stream = sd.InputStream(samplerate=sample_rate, channels=1,
                            dtype="float32", blocksize=block_size,
                            callback=callback)

    with stream:
        while recording:
            sd.sleep(50)
            elapsed = time.time() - start_time
            if elapsed >= max_duration:
                print_status(f"Max duration ({max_duration}s) reached.")
                break

    audio = np.concatenate(frames, axis=0)
    duration = len(audio) / sample_rate

    # Trim trailing silence
    if speech_detected and silence_start is not None:
        trim_samples = int(silence_duration * sample_rate)
        if len(audio) > trim_samples:
            audio = audio[:-trim_samples]
            duration = len(audio) / sample_rate

    return audio, duration, speech_detected


def save_wav(audio, sample_rate=16000):
    """Save audio to a temporary WAV file. Returns the file path."""
    from scipy.io import wavfile

    # Convert float32 [-1, 1] to int16
    audio_int16 = (audio * 32767).astype(np.int16)
    if audio_int16.ndim > 1:
        audio_int16 = audio_int16[:, 0]

    tmp = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    wavfile.write(tmp.name, sample_rate, audio_int16)
    tmp.close()
    return tmp.name


def transcribe_api(wav_path):
    """Transcribe using OpenAI Whisper API."""
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print_status("Error: OPENAI_API_KEY environment variable not set.")
        print_status("  Set it:  export OPENAI_API_KEY='sk-...'")
        print_status("  Or use:  --model local  (slower, no API key needed)")
        sys.exit(1)

    try:
        from openai import OpenAI
        client = OpenAI(api_key=api_key)
        with open(wav_path, "rb") as f:
            result = client.audio.transcriptions.create(
                model="whisper-1",
                file=f,
                response_format="text",
            )
        return result.strip()
    except ImportError:
        print_status("Error: openai package not installed.")
        print_status("  pip install openai")
        sys.exit(1)
    except Exception as e:
        print_status(f"Error: Transcription API call failed — {e}")
        print_status("  Check your OPENAI_API_KEY and network connection.")
        print_status("  Or try:  --model local")
        sys.exit(1)


def transcribe_local(wav_path, model_name="base"):
    """Transcribe using local Whisper model."""
    try:
        import whisper
    except ImportError:
        print_status("Error: whisper package not installed.")
        print_status("  pip install openai-whisper")
        sys.exit(1)

    print_status(f"Loading local Whisper model '{model_name}'...")
    model = whisper.load_model(model_name)
    result = model.transcribe(wav_path)
    return result["text"].strip()


def main():
    parser = argparse.ArgumentParser(
        description="Record voice input and transcribe for PM interview practice."
    )
    parser.add_argument("--model", choices=["api", "local"], default="api",
                        help="Transcription backend (default: api)")
    parser.add_argument("--whisper-model", default="base",
                        help="Local whisper model size (default: base)")
    parser.add_argument("--silence-duration", type=float, default=3.0,
                        help="Seconds of silence before auto-stop (default: 3)")
    parser.add_argument("--max-duration", type=float, default=600,
                        help="Max recording duration in seconds (default: 600)")
    parser.add_argument("--read-delay", type=float, default=0,
                        help="Seconds to wait before recording starts (default: 0)")
    args = parser.parse_args()

    wall_start = time.time()

    check_microphone()

    # Reading delay — give the user time to read the question
    if args.read_delay > 0:
        print_status(f"Read the question... recording starts in {args.read_delay:.0f}s")
        time.sleep(args.read_delay)

    beep()  # Signal: recording starts

    audio, duration, speech_detected = record_with_silence_detection(
        silence_duration=args.silence_duration,
        max_duration=args.max_duration,
    )

    beep()  # Signal: recording ends

    total_seconds = round(time.time() - wall_start, 1)

    if not speech_detected:
        print_status("No speech detected.")
        result = {"text": "", "duration_seconds": 0, "total_seconds": total_seconds}
        print(json.dumps(result))
        return

    print_status(f"Recorded {duration:.1f}s of audio.")

    wav_path = save_wav(audio)
    try:
        print_status("Transcribing...")
        if args.model == "api":
            text = transcribe_api(wav_path)
        else:
            text = transcribe_local(wav_path, args.whisper_model)
    finally:
        os.unlink(wav_path)

    if not text:
        print_status("Transcription returned empty.")
        text = ""

    result = {
        "text": text,
        "duration_seconds": round(duration, 1),
        "total_seconds": total_seconds,
    }
    print(json.dumps(result))


if __name__ == "__main__":
    main()
