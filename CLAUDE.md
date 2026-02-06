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
