# Progress Data

This directory stores your personal interview practice data. These files are gitignored — initialize them locally after cloning.

## Setup

```bash
# Initialize progress summary from template
cp pm-interview-coach/assets/progress-template.md progress/summary.md

# Create question log
cat > progress/question-log.md << 'EOF'
# Question Log

| Date | Type | Question | Score | Weak Dimensions |
|------|------|----------|-------|-----------------|
EOF
```

Session logs will be created automatically in `progress/sessions/` during mock interviews.
