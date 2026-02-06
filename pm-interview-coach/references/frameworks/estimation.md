# Estimation Frameworks

## Fermi Estimation Approach

**Use for:** Market sizing, back-of-envelope calculations, "how many X are there?" questions

### Step-by-Step Method
1. **Clarify what you're estimating**: Restate the question. Define scope (geography, time period, specific product).
2. **Choose your decomposition**: Break the problem into 3-5 multiplicative or additive components.
3. **State and justify assumptions**: For each component, state your assumption and briefly explain why.
4. **Calculate step by step**: Show your work. Round at each step for mental math.
5. **Sanity check**: Compare your answer to something known. Does it pass the smell test?
6. **Give a range**: Express confidence as a range (e.g., "I estimate 5-15 million, with 10 million as my point estimate").

### Decomposition Strategies

**Population-based** (good for consumer products):
```
Total population
x % in target demographic
x % who have the need
x % who would use this type of product
x average usage/purchase per person
```

**Supply-based** (good for counting things):
```
Number of locations/units
x capacity per unit
x utilization rate
x time period
```

**Revenue-based** (good for market sizing):
```
Number of potential customers
x % who would pay
x average price point
x purchase frequency per year
```

### When to Use
- "How many piano tuners are in Chicago?"
- "What is the market size for X?"
- "How many Y are sold per year?"

### Common Mistakes
- Not clarifying scope before starting (geography? time period? segment?)
- Making assumptions without stating them
- Compounding errors by having too many variables
- Not sanity-checking the final answer
- Over-precision (saying "4,237,192" when you should say "about 4 million")

---

## Top-Down vs Bottom-Up

### Top-Down
Start from the big picture and narrow down.

**When to use**: When macro data is available (industry reports, population data, GDP).

**Example**: "Revenue of coffee shops in Manhattan"
- US coffee industry: ~$80B/year
- NYC share: ~3% of US population but ~5% of spending = ~$4B
- Manhattan share of NYC: ~30% = ~$1.2B

### Bottom-Up
Start from individual units and scale up.

**When to use**: When you can estimate individual behavior or unit economics.

**Example**: "Revenue of coffee shops in Manhattan"
- Estimated 3,000 coffee shops in Manhattan
- Average revenue per shop: ~$500K/year (based on $1,500/day average)
- Total: 3,000 x $500K = $1.5B

### Cross-Validation
Use both approaches and compare. If they are within 2x of each other, you likely have a reasonable estimate. If they diverge wildly, investigate which assumptions are off.

---

## Useful Reference Numbers

Keep these anchors in mind for US-focused estimates:

| Fact | Number |
|------|--------|
| US population | ~330 million |
| US households | ~130 million |
| US smartphone users | ~300 million |
| US GDP | ~$27 trillion |
| Average US household income | ~$75,000 |
| US life expectancy | ~78 years |
| Hours in a year | ~8,760 |
| Seconds in a day | ~86,400 |
| World population | ~8 billion |

---

## Estimation Principles

1. **Round aggressively**: Use 300M instead of 331M for US population. Precision is false comfort.
2. **Identify the swing variable**: Which assumption matters most? Spend extra time justifying that one.
3. **Use base rates**: When unsure, start from known rates (e.g., smartphone penetration is ~85% in US).
4. **Think in orders of magnitude**: Is the answer millions, tens of millions, or hundreds of millions? Getting the order right matters more than the exact number.
5. **Communicate your uncertainty**: "This could be off by 2-3x, but the order of magnitude should be right."
