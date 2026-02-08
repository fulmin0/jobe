# PM Interview Prep Agent

An [Agent Skill](https://agentskills.io) that acts as a PM interview coach. Conducts mock interviews across 5 question types, evaluates answers against detailed rubrics, tracks your progress over time, and provides targeted practice on weak areas.

## Compatibility

| Tool | Support |
|------|---------|
| **Claude Code** | Full — slash commands, auto-discovery, progress tracking |
| **Cursor / VS Code + Claude** | Agent Skills supported, invoke skill manually |
| **Gemini CLI** | Agent Skills standard supported |
| **Other AI coding tools** | Partial — can read SKILL.md if prompted |

## Quick Start

```bash
# 1. Clone
git clone https://github.com/fulmin/jobe.git && cd jobe

# 2. Install Claude Code (if you don't have it)
npm install -g @anthropic-ai/claude-code

# 3. Initialize progress tracking
cp pm-interview-coach/assets/progress-template.md progress/summary.md
cat > progress/question-log.md << 'EOF'
# Question Log

| Date | Type | Question | Score | Weak Dimensions |
|------|------|----------|-------|-----------------|
EOF

# 4. Start Claude Code
claude

# 5. Run your first mock interview
/mock product-sense
```

## Commands

| Command | Description |
|---------|-------------|
| `/mock [type] [company]` | Full mock interview with scoring and session logging |
| `/drill [type]` | Quick 10-minute practice targeting weak areas |
| `/evaluate [type]` | Evaluate a specific answer against the rubric |
| `/progress [period]` | Comprehensive progress report with trends |
| `/study [topic]` | Socratic teaching session on a framework |
| `/weak-areas` | Targeted practice on your weakest dimensions |
| `/question-bank [type] [difficulty]` | Generate practice questions |
| `/review-session [latest\|filename]` | Review a past session |
| `/framework [name]` | Quick reference card (e.g., product-sense, market-entry, debugging, growth, monetization) |
| `/debrief` | Post-real-interview reflection and logging |

**Question types:** `product-sense`, `execution`, `strategy`, `estimation`, `behavioral`

## Project Structure

```
├── CLAUDE.md                        # Project config (references the skill)
├── pm-interview-coach/              # Agent Skill (portable)
│   ├── SKILL.md                     # Core skill definition
│   ├── references/
│   │   ├── rubrics/                 # Scoring rubrics (5 types + universal scale)
│   │   └── frameworks/              # PM frameworks (video-derived, with citations)
│   ├── assets/                      # Templates for progress files
│   └── scripts/                     # Transcript extraction (optional)
├── .claude/commands/                # Slash commands (10 workflows)
├── knowledge/transcripts/           # 24 processed video transcripts
│   ├── raw/                         # Whisper-extracted transcripts
│   ├── processed/                   # Summarized, tagged versions
│   └── index.md                     # Index by type, framework, difficulty
└── progress/                        # Personal data (gitignored)
    ├── sessions/                    # Per-session logs
    ├── summary.md                   # Running scores and trends
    └── question-log.md              # All questions with scores
```

## Knowledge Base

The repo includes 24 processed transcripts from [Dianna Yau's PM interview prep playlist](https://www.youtube.com/playlist?list=PLejl_r9a59gtDlXZ1Na95296rPI1uoyBu), covering product sense, strategy, execution, and mock interviews.

### Adding More Videos (Optional)

```bash
# Set up Python environment
python -m venv .venv && source .venv/bin/activate
pip install -r pm-interview-coach/scripts/requirements.txt

# Requires ffmpeg
brew install ffmpeg  # macOS

# Extract transcripts
python pm-interview-coach/scripts/extract_transcripts.py --playlist "PLAYLIST_URL"
python pm-interview-coach/scripts/extract_transcripts.py --video "VIDEO_URL"
```

## Rubric Dimensions

| Type | Dimensions (weights vary by subtype) |
|------|-----------|
| Product Sense | Structure & Framework (10-15%), Strategic Thinking/Why (15-25%), User Empathy (25-30%), Prioritization (15-20%), Solution Creativity (15%), Communication (10%) |
| Execution | Process Rigor (25%), Metrics Quality (15-35%), Data-Driven Thinking (20-30%), Prioritization & Trade-offs (20%), Communication Clarity (10-20%) |
| Strategy | Market Understanding (15-25%), Strategic Thinking (20-35%), Business Model Reasoning (20-35%), Risk Assessment (10-20%), Actionability (10-30%) |
| Estimation | Decomposition (30%), Assumptions Quality (25%), Math Execution (20%), Sanity Check (15%), Communication (10%) |
| Behavioral | Story Selection (20%), STAR Structure (20%), Personal Contribution (25%), Impact/Results (20%), Self-Awareness (15%) |

Scores use a 1-5 scale. 3.0+ generally passes. 4.0+ is exceptional.
