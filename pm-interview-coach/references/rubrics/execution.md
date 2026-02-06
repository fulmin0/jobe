# Execution Evaluation Rubric

## Dimensions

### 1. Goal Setting (Weight: 20%)

| Score | Description |
|-------|-------------|
| 1 | Cannot articulate clear goals for the product or feature |
| 2 | States goals but they are vague or misaligned with business objectives |
| 3 | Clear, measurable goals tied to product and business objectives |
| 4 | Goals with explicit timeframes, considers gaming risks and misalignment |
| 5 | Coherent goal hierarchy (north star -> team -> feature level), articulates why each matters |

### 2. Metrics Selection (Weight: 25%)

| Score | Description |
|-------|-------------|
| 1 | Cannot identify relevant metrics or picks vanity metrics |
| 2 | Lists metrics but no prioritization, unclear relationship between them |
| 3 | Primary metric + 2-3 supporting metrics with rationale for each |
| 4 | Metrics framework (input/output, leading/lagging), includes guardrail metrics |
| 5 | Metrics reveal deep understanding of user behavior and business model, anticipates trade-offs |

### 3. Debugging / Root Cause Analysis (Weight: 25%)

| Score | Description |
|-------|-------------|
| 1 | Guesses at a cause with no systematic approach |
| 2 | Considers 1-2 causes but does not explore systematically |
| 3 | Structured approach: segments by internal vs external, time-based, user-type-based |
| 4 | Comprehensive hypothesis tree, data-driven elimination, considers seasonality and confounds |
| 5 | Identifies non-obvious causes, proposes specific validation steps for each hypothesis |

### 4. Prioritization and Trade-offs (Weight: 20%)

| Score | Description |
|-------|-------------|
| 1 | Cannot make trade-off decisions or prioritize competing demands |
| 2 | Makes decisions but without clear criteria or framework |
| 3 | Uses a prioritization framework (RICE/ICE), articulates trade-offs clearly |
| 4 | Quantifies trade-offs where possible, considers stakeholder perspectives and dependencies |
| 5 | Nuanced trade-off analysis with second-order effects, reversibility considerations, and timing |

### 5. Communication Clarity (Weight: 10%)

| Score | Description |
|-------|-------------|
| 1 | Rambling, unclear, hard to follow the thread |
| 2 | Generally clear but disorganized, loses the listener |
| 3 | Clear structure, easy to follow, logical progression |
| 4 | Crisp and precise, uses data effectively, good signposting |
| 5 | Would be persuasive to executives, impeccable clarity and conciseness |

## Follow-up Probe Suggestions

- "This metric dropped 20% week-over-week. Walk me through your investigation."
- "You have to cut one of these three features. Which one and why?"
- "How would you communicate this trade-off to engineering leadership?"
- "What data would you need to validate your hypothesis?"
- "How would you set up an A/B test for this change?"
