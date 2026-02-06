# Execution Frameworks

## GAME Framework

**Use for:** Goal-setting and metrics questions

### Steps
1. **G**oals — What is the product/feature trying to achieve? Align with company mission and team objectives.
2. **A**ctions — What levers can the team pull? What features or initiatives drive the goals?
3. **M**etrics — How do you measure progress? Define primary metric, secondary metrics, and guardrails.
4. **E**valuate — How do you evaluate success? Set thresholds, define experiment design, plan iteration.

### When to Use
- "What metrics would you set for X?"
- "How would you measure success of Y?"
- "Define the goals for this product"

### Common Mistakes
- Choosing vanity metrics (page views, downloads) instead of engagement or retention metrics
- No guardrail metrics (e.g., measuring engagement without monitoring quality or user satisfaction)
- Metrics that are too lagging to be actionable
- Not distinguishing between input metrics (things you control) and output metrics (outcomes)

---

## RICE Prioritization Framework

**Use for:** Feature prioritization questions, roadmap decisions

### Dimensions
- **R**each — How many users will this impact in a given time period?
- **I**mpact — How much will this move the needle per user? (3=massive, 2=high, 1=medium, 0.5=low, 0.25=minimal)
- **C**onfidence — How sure are we about reach and impact estimates? (100%=high, 80%=medium, 50%=low)
- **E**ffort — How many person-months will this take?

**Score = (Reach x Impact x Confidence) / Effort**

### When to Use
- "How would you prioritize these features?"
- "You have limited engineering resources. What do you build first?"
- Any question requiring you to rank competing priorities

### Common Mistakes
- Using gut feel instead of attempting to quantify
- Ignoring confidence (overweighting uncertain high-impact ideas)
- Not considering effort or underestimating it
- Forgetting strategic alignment beyond just the score

---

## Metric Debugging Framework

**Use for:** "Why did metric X drop?" questions

### Step-by-Step Approach
1. **Clarify the metric**: What exactly is being measured? How is it calculated? What is the normal range?
2. **Scope the change**: When did it start? How significant is the drop? Is it sudden or gradual?
3. **Segment the data**:
   - By platform (iOS, Android, Web)
   - By geography
   - By user cohort (new vs returning, free vs paid)
   - By feature/entry point
4. **Check internal causes**:
   - Recent code deployments or feature launches
   - A/B tests running
   - Data pipeline issues (instrumentation bugs)
   - Server/infrastructure problems
5. **Check external causes**:
   - Seasonality or holidays
   - Competitor launches
   - App store changes
   - News/PR events
6. **Validate hypotheses**: For each possible cause, describe what data you would check to confirm or rule it out.
7. **Propose action plan**: Immediate actions (revert if needed) and longer-term investigation steps.

### Common Mistakes
- Jumping to a single root cause without exploring alternatives
- Not checking if it is a data/instrumentation issue first
- Forgetting about external factors
- Not segmenting the data to narrow down where the drop is happening

---

## ICE Framework

**Use for:** Quick prioritization alternative to RICE

### Dimensions
- **I**mpact — How much will this improve the target metric?
- **C**onfidence — How sure are you about the impact?
- **E**ase — How easy is it to implement?

Score each 1-10, average for final score.

### When to Use
- Quick prioritization discussions
- When you do not have data for Reach estimates
- Brainstorming sessions where speed matters
