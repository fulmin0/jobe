# PM Interview Prep - Project Configuration

This project is a PM interview preparation workspace powered by the `pm-interview-coach` Agent Skill.

## Skill
The core interview coaching capability lives in `pm-interview-coach/SKILL.md`. Activate it for any PM interview practice, evaluation, study, or progress review task.

## Data Directories
- `knowledge/transcripts/` — YouTube video transcripts (raw and processed) used as knowledge base
- `progress/` — Session logs, running scores, and question history
- `progress/summary.md` — Read this at the start of any interview session

## Slash Commands
Use `/mock`, `/drill`, `/evaluate`, `/progress`, `/study`, `/weak-areas`, `/question-bank`, `/review-session`, `/framework`, or `/debrief` to activate specific workflows. See `.claude/commands/` for details.

## Transcript Extraction
To populate the knowledge base, run:
```
python pm-interview-coach/scripts/extract_transcripts.py --playlist "<URL>"
```

## Voice Web UI
Voice mode is the default for `/mock` and `/drill` — the server starts automatically and opens the browser.
Use `--text` flag to run in text-only mode. Local Whisper is the default transcription model (no API key needed).
To start the server manually: `python pm-interview-coach/scripts/voice_server.py` (use `--model api` for OpenAI API transcription).
