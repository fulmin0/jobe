# Estimation Evaluation Rubric

## Dimensions

### 1. Problem Decomposition (Weight: 30%)

| Score | Description |
|-------|-------------|
| 1 | No breakdown, guesses a final number directly |
| 2 | Attempts breakdown but misses key components or uses wrong splits |
| 3 | Logical breakdown into 3-5 components with reasonable structure |
| 4 | Elegant decomposition that captures all key variables, clearly explains each step |
| 5 | Multiple decomposition approaches considered, picks the best one and cross-validates |

### 2. Assumptions Quality (Weight: 25%)

| Score | Description |
|-------|-------------|
| 1 | Unstated or wildly inaccurate assumptions |
| 2 | States assumptions but they are unreasonable or unjustified |
| 3 | Reasonable assumptions, stated explicitly, within an order of magnitude |
| 4 | Well-calibrated assumptions with reasoning for each, uses anchor data points |
| 5 | Sensitivity analysis on key assumptions, identifies which ones matter most to the answer |

### 3. Mathematical Execution (Weight: 20%)

| Score | Description |
|-------|-------------|
| 1 | Arithmetic errors, gets lost in calculations |
| 2 | Correct math but unnecessarily complex or hard to follow |
| 3 | Clean calculations, easy to follow, arrives at a reasonable answer |
| 4 | Efficient calculation with clear intermediate results, uses rounding well |
| 5 | Elegant math, shows work clearly, rounds appropriately at each step |

### 4. Sanity Check (Weight: 15%)

| Score | Description |
|-------|-------------|
| 1 | No validation of the final answer |
| 2 | Says "seems reasonable" without actually checking |
| 3 | Compares to at least one known reference point or related fact |
| 4 | Multiple sanity checks from different angles, adjusts if something seems off |
| 5 | Cross-validates using an alternative estimation approach to confirm the range |

### 5. Communication (Weight: 10%)

| Score | Description |
|-------|-------------|
| 1 | Hard to follow the reasoning, jumps between steps |
| 2 | Understandable but disorganized, hard to audit |
| 3 | Clear narration of approach, listener can follow along |
| 4 | Engaging walkthrough, checks in with interviewer, explains trade-offs |
| 5 | Would be compelling in a board presentation, perfect pacing and clarity |

## Follow-up Probe Suggestions

- "Your estimate is X. How confident are you? What range would you give?"
- "What if [key assumption] was off by 2x? How would that change your answer?"
- "Can you verify this using a completely different approach?"
- "How would this number change in [different market/country]?"
- "What additional data would most improve the accuracy of this estimate?"
