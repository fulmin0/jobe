"""
YouTube Playlist Transcript Extractor

Extracts transcripts from a YouTube playlist (or single video) and saves
them as markdown files for use as a PM interview prep knowledge base.

Strategy:
  1. Try pytubefix captions (fast, no download needed)
  2. Fall back to: download audio via pytubefix → transcribe with local Whisper model

Usage:
    python extract_transcripts.py --playlist "PLAYLIST_URL" [--output DIR] [--whisper-model base]
    python extract_transcripts.py --video "VIDEO_URL" [--output DIR]

Dependencies:
    pip install pytubefix openai-whisper
    Also requires ffmpeg: brew install ffmpeg
"""

from __future__ import annotations

import argparse
import re
import sys
import tempfile
from datetime import datetime
from pathlib import Path


def slugify(text: str, max_length: int = 80) -> str:
    """Convert text to a filesystem-safe slug."""
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    text = text.strip("-")
    return text[:max_length]


def get_playlist_videos(playlist_url: str) -> list[dict]:
    """Extract video metadata from a YouTube playlist using pytubefix."""
    from pytubefix import Playlist

    print("Fetching playlist metadata...")
    playlist = Playlist(playlist_url)

    videos = []
    for video in playlist.videos:
        duration_secs = video.length or 0
        mins = duration_secs // 60
        secs = duration_secs % 60
        duration_fmt = f"{mins}:{secs:02d}" if duration_secs else "unknown"

        videos.append({
            "id": video.video_id,
            "title": video.title,
            "duration": duration_fmt,
            "channel": video.author or "unknown",
        })

    print(f"Found {len(videos)} videos in playlist.")
    return videos


def get_single_video(video_url: str) -> dict:
    """Get metadata for a single video using pytubefix."""
    from pytubefix import YouTube

    yt = YouTube(video_url)
    duration_secs = yt.length or 0
    mins = duration_secs // 60
    secs = duration_secs % 60
    duration_fmt = f"{mins}:{secs:02d}" if duration_secs else "unknown"

    return {
        "id": yt.video_id,
        "title": yt.title,
        "duration": duration_fmt,
        "channel": yt.author or "unknown",
    }


def try_captions(video_id: str) -> str | None:
    """Try to get transcript via pytubefix captions (fast path)."""
    try:
        from pytubefix import YouTube

        yt = YouTube(f"https://www.youtube.com/watch?v={video_id}")
        captions = yt.captions

        # Prefer English captions
        caption = None
        for lang_code in ["en", "a.en", "en-US", "en-GB"]:
            if lang_code in captions:
                caption = captions[lang_code]
                break

        # Fall back to any available caption
        if caption is None and captions:
            caption = list(captions.values())[0]

        if caption is None:
            return None

        # Get SRT formatted captions and parse them
        srt_text = caption.generate_srt_captions()
        return _parse_srt(srt_text)

    except Exception as e:
        print(f"\n    Caption extraction failed: {e}", end="")
        return None


def _parse_srt(srt_text: str) -> str | None:
    """Parse SRT format into timestamped lines."""
    lines = []
    current_timestamp = None

    for line in srt_text.strip().split("\n"):
        line = line.strip()

        # Match SRT timestamp line (e.g., "00:01:23,456 --> 00:01:25,789")
        ts_match = re.match(r"(\d{2}):(\d{2}):(\d{2}),\d+\s+-->", line)
        if ts_match:
            hours = int(ts_match.group(1))
            mins = int(ts_match.group(2))
            secs = int(ts_match.group(3))
            total_mins = hours * 60 + mins
            current_timestamp = f"[{total_mins:02d}:{secs:02d}]"
            continue

        # Skip sequence numbers and blank lines
        if not line or line.isdigit():
            continue

        # This is a text line
        if current_timestamp and line:
            # Strip HTML tags that sometimes appear in captions
            clean = re.sub(r"<[^>]+>", "", line)
            if clean.strip():
                lines.append(f"{current_timestamp} {clean.strip()}")
                current_timestamp = None  # Only use timestamp for first line of segment

    return "\n".join(lines) if lines else None


def transcribe_with_whisper(video_id: str, model_name: str = "base") -> str | None:
    """Download audio with pytubefix and transcribe with local Whisper."""
    import whisper
    from pytubefix import YouTube

    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)

        try:
            yt = YouTube(f"https://www.youtube.com/watch?v={video_id}")

            # Try audio-only stream first, fall back to lowest resolution video
            stream = yt.streams.filter(only_audio=True).order_by("abr").first()
            if stream is None:
                stream = yt.streams.filter(progressive=True).order_by("resolution").first()

            if stream is None:
                print("\n    No suitable stream found", end="")
                return None

            # Download to temp directory
            audio_file = stream.download(output_path=str(tmp_path), filename="audio")
            audio_path = Path(audio_file)

        except Exception as e:
            print(f"\n    Audio download failed: {e}", end="")
            return None

        # Transcribe with Whisper
        model = _get_whisper_model(model_name)
        result = model.transcribe(str(audio_path), language="en")

        # Format with timestamps
        lines = []
        for segment in result.get("segments", []):
            start = segment["start"]
            minutes = int(start // 60)
            seconds = int(start % 60)
            timestamp = f"[{minutes:02d}:{seconds:02d}]"
            text = segment["text"].strip()
            if text:
                lines.append(f"{timestamp} {text}")

        return "\n".join(lines) if lines else None


# Cache the Whisper model so it's loaded only once
_whisper_model = None
_whisper_model_name = None


def _get_whisper_model(model_name: str):
    global _whisper_model, _whisper_model_name
    if _whisper_model is None or _whisper_model_name != model_name:
        import whisper
        print(f"\n    Loading Whisper '{model_name}' model (first time only)...", end="")
        _whisper_model = whisper.load_model(model_name)
        _whisper_model_name = model_name
    return _whisper_model


def save_transcript(video: dict, transcript: str, method: str, output_dir: Path) -> Path:
    """Save transcript as a markdown file."""
    slug = slugify(video["title"])
    filename = f"{video['id']}-{slug}.md"
    filepath = output_dir / filename

    content = f"""# {video['title']}

- **Video ID:** {video['id']}
- **Channel:** {video['channel']}
- **URL:** https://www.youtube.com/watch?v={video['id']}
- **Duration:** {video['duration']}
- **Extracted:** {datetime.now().strftime('%Y-%m-%d')}
- **Method:** {method}

## Transcript

{transcript}
"""

    filepath.write_text(content)
    return filepath


def main():
    parser = argparse.ArgumentParser(
        description="Extract YouTube transcripts for PM interview prep"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--playlist", help="YouTube playlist URL")
    group.add_argument("--video", help="Single YouTube video URL")
    parser.add_argument(
        "--output",
        default=None,
        help="Output directory (default: knowledge/transcripts/raw/ relative to project root)",
    )
    parser.add_argument(
        "--whisper-model",
        default="base",
        choices=["tiny", "base", "small", "medium", "large"],
        help="Whisper model size for audio transcription fallback (default: base)",
    )

    args = parser.parse_args()

    # Default output directory: project_root/knowledge/transcripts/raw/
    if args.output:
        output_dir = Path(args.output)
    else:
        script_dir = Path(__file__).resolve().parent
        project_root = script_dir.parent.parent
        output_dir = project_root / "knowledge" / "transcripts" / "raw"

    output_dir.mkdir(parents=True, exist_ok=True)

    # Get video list
    if args.playlist:
        videos = get_playlist_videos(args.playlist)
    else:
        video = get_single_video(args.video)
        videos = [video]

    # Extract transcripts
    success = 0
    skipped = 0
    failed = []
    methods = {"captions": 0, "whisper": 0}

    for i, video in enumerate(videos, 1):
        # Skip if already extracted
        slug = slugify(video["title"])
        existing = output_dir / f"{video['id']}-{slug}.md"
        if existing.exists():
            print(f"[{i}/{len(videos)}] {video['title']}... SKIPPED (already exists)")
            skipped += 1
            success += 1
            continue

        print(f"[{i}/{len(videos)}] {video['title']}...", end=" ", flush=True)

        # Strategy 1: Try pytubefix captions
        transcript = try_captions(video["id"])
        if transcript:
            method = "pytubefix-captions"
            methods["captions"] += 1
        else:
            # Strategy 2: Download audio + Whisper
            print("no captions, using Whisper...", end=" ", flush=True)
            transcript = transcribe_with_whisper(video["id"], args.whisper_model)
            method = f"whisper-{args.whisper_model}"
            if transcript:
                methods["whisper"] += 1

        if transcript:
            filepath = save_transcript(video, transcript, method, output_dir)
            print(f"OK [{method}]")
            success += 1
        else:
            print("FAILED")
            failed.append(video["title"])

    # Summary
    print(f"\n{'='*60}")
    print(f"Done: {success} total ({skipped} skipped), {len(failed)} failed out of {len(videos)} videos")
    print(f"  - Via captions: {methods['captions']}")
    print(f"  - Via Whisper:  {methods['whisper']}")
    print(f"Output directory: {output_dir}")

    if failed:
        print(f"\nFailed videos:")
        for title in failed:
            print(f"  - {title}")


if __name__ == "__main__":
    main()
