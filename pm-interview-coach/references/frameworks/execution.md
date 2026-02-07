# Execution Frameworks

All frameworks synthesized from Dianna Yau video transcript knowledge base with citations.

---

## Subtype: Take-Home Assignments

### 8-Step Take-Home Framework
**Source:** `gAeuGjvF7bE` — Product Manager Interviews: Take Home Assignments in 8 Steps
**Use for:** PM take-home assignments (increasingly common — 50%+ of product roles)

#### Steps
1. **Understand the Goal** — Company business model + explicit goal + how they connect. Always ask: how does this goal drive revenue/growth?
2. **Analyze Data** — Three data types:
   - Raw data → pivot tables, charts
   - Tables/graphs → interpret and draw insights
   - User feedback → group into theme buckets
   - Pro tip: Ask specific questions AND observe broadly for unexpected patterns
3. **Prioritize Problems** — Identify 2-3 key problems, prioritize by impact on the stated goal
   - Fix retention before acquisition — "If people aren't satisfied, they won't come back. And when they don't come back, they don't recommend friends. You'll have a leaky bucket."
4. **Create Strategy** — 3-pronged plan of attack (show breadth of thinking, not a single approach)
5. **Measure Success** — Define metrics at two levels: big picture goal metrics + strategy-specific metrics
6. **Identify Pain Points** — Break down by user stakeholders (supply AND demand sides)
7. **Generate Solutions** — 2-3 solutions per strategy, prioritize by impact vs. effort
   - "Think of solutions you would want to test — MVP as minimal viable product — not holistic solutions that will take six months to build"
8. **Write-Up** — Produce the final deliverable (see 10-section structure below)

### 10-Section Write-Up Structure
**Source:** `gAeuGjvF7bE`

1. **Executive summary** — TLDR of your entire analysis and recommendation
2. **Business and goal** — Company overview and the specific objective
3. **Data insights** — Lead with interpreted statements, NOT raw graphs ("Do not just throw a graph in there, leaving the audience to interpret")
4. **Prioritized problems** — Ranked list with justification
5. **Strategy / plan of attack** — Your 3-pronged approach
6. **Success metrics** — How you'll know if it's working
7. **MVP solutions** — Testable solutions, not 6-month builds
8. **Prioritized solutions** — ROI-based ranking (effort to build vs. potential impact)
9. **Mocks / wireframes / user flows** — Optional but shows execution ability
10. **Roadmap** — Timeline with milestones and break-even considerations

### 4-Part Take-Home Framework (Alternative)
**Source:** `rOpYuEOrxPQ` — Product Take Home Assignment: Real Example + Framework
**Use for:** Lighter alternative structure, especially for strategy-heavy take-homes

#### Steps
1. **Understanding the Business**
   - Mission — Identify key themes to connect strategy to later
   - Goals — North Star metric + 3-5 supporting metrics
   - Users — Multi-sided ecosystem players
   - Business Model — How does the company make money?
   - Source: Public company earnings reports (best source for goals, business model, metrics)

2. **Data Gathering**
   - **User Research:**
     - Primary: User interviews (best — "nothing beats talking to customers")
     - Secondary: App store reviews, forums (Reddit, YouTube review videos)
   - **Market Research:**
     - Statistics (Statista, Pew Research, Google search)
     - Industry reports (VCs, McKinsey, BCG, Bain)
     - Raw data (public earnings reports)
   - Tip: "Don't dig past page 5 on Google — it's really mentally draining and diminishing returns"
   - Look for 3-5 recurring themes across sources

3. **Strategy Development**
   - Define strategy addressing prioritized themes
   - Connect strategy back to company mission
   - Develop 2-3 solutions per strategic pillar
   - Mix practical solutions with moonshot ideas
   - Prioritize using ROI analysis (effort vs. benefit)
   - Create wireframes showing key user flows
   - Turn strategy into month-by-month roadmap

4. **Execution Planning**
   - Success metrics — How do you know if you're winning?
   - Experiments — A/B tests for key hypotheses
   - Go-to-market strategy — Awareness, purchase drivers, brand positioning

#### Tips
- "They don't care about the right answer as much as your process — if you build logical conclusions throughout, that shows you can execute if given the right data"
- "Strategy plain and simple means a plan of attack, a plan on how to win"
- Different companies value different solution types: Google looks for moonshots, Facebook/Meta looks for practical people problems
- Take-homes test your process and logical thinking more than getting the "right answer"

---

## Subtype: Success Metrics / KPIs

### 5-Step Success Metrics Framework
**Source:** `vpsUw1vP8w4` — Top 5 Product Manager Interview Questions: How to Answer
**Use for:** "What metrics would you set for [product]?" / "How would you measure success of X?"

#### Steps
1. **Understand the Product** — What it does, who uses it, what the core goal is
2. **Qualitative Goals** — What does success look like in words? (e.g., "users find what they need quickly," "hosts earn reliable income")
3. **Quantitative Metrics** — Translate each qualitative goal into measurable numbers. Make them specific to the product, not generic.
   - Bad: "DAU, MAU, time spent" (generic, shows memorization)
   - Good: Explain WHY each metric matters for THIS specific product
4. **North Star Metrics (2-3)** — The top metrics that best capture overall product health
5. **Counter-Metrics + Downstream Metrics** — What could go wrong if you optimize only for North Stars? What secondary effects should you monitor?

#### Tips
- "Make it specific to the product you're talking about, not just throwing out generic metrics that show memorization versus thinking"
- "This isn't high school — you're not going to impress them by memorizing things" (like AARRR pirates framework)
- Show thoughtful analysis over framework memorization

### Marketplace Metrics Selection
**Source:** `dz-hqOih9qY` — Product Sense Mock Interview for DoorDash
**Use for:** Metrics for marketplace / multi-sided platform products

#### Approach
1. Find a metric that captures value for ALL sides of the marketplace
2. Explicitly evaluate and reject ill-fitting metrics with reasoning:
   - Retention → May not work for infrequent-use products (can't distinguish bad experience from low usage frequency)
   - Rating → May not be representative (only extreme experiences get rated)
3. Show your reasoning process, not just the final choice

#### Example (Airbnb)
Selected: "Number of nights booked and stayed per day"
- Hosts: make money when nights are booked
- Guests: get value when they successfully stay
- Airbnb: earns revenue from each transaction
- Captures successful completion, not just booking intent

---

## Subtype: Root Cause / Debugging

### 6-Step Debugging Framework
**Source:** `vpsUw1vP8w4` — Top 5 Product Manager Interview Questions: How to Answer
**Use for:** "Metric X dropped by Y% — what happened and how would you fix it?"

#### Steps
1. **Clarify** — Ask about timespan, geography, scope, magnitude
   - When did the drop start? How significant is it? Sudden or gradual?
   - Is it isolated to a region, platform, or user segment?

2. **Understand the Product** — What does the product do? How is the metric calculated? What's the normal range?

3. **Map the User Flow** — Walk through the complete user journey step by step. Identify all points where the metric could be affected.

4. **Generate Hypotheses** — Systematically brainstorm possible causes:
   - **Internal:** Recent code deployments, feature launches, A/B tests, data pipeline issues, infrastructure problems
   - **External:** Seasonality/holidays, competitor launches, app store changes, news/PR events, regulatory changes

5. **Validation Approach** — For each hypothesis, describe what data you would check to confirm or rule it out. Segment the data:
   - By platform (iOS, Android, Web)
   - By geography
   - By user cohort (new vs. returning, free vs. paid)
   - By feature/entry point

6. **Propose Solutions** — For top hypotheses:
   - Immediate actions (revert if deployment-related)
   - Investigation steps (if root cause unclear)
   - Long-term fixes (if structural issue)

#### Tips
- Don't jump to a single root cause without exploring alternatives
- Always check if it's a data/instrumentation issue first
- Don't forget external factors (seasonality, competitors)
- Segment the data to narrow down where the drop is happening
- Think systematically through the framework rather than going through a memorized checklist
