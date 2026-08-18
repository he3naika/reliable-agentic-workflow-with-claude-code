---
name: finance-math-toolkit
description: Deterministic financial calculations (compound growth, required capital via safe withdrawal rate, loan amortization/payoff time, currency conversion). Use this instead of computing these by hand — required whenever a goal-path-planner, feasibility-assessor, or financial-auditor needs a numeric projection or verdict.
---

# Finance Math Toolkit

Never estimate compound growth, the capital needed for a target passive
income, a loan's payoff time, or a currency conversion in prose. Call
`scripts/calc.py` and use its exact output. This is what makes the workflow's
achievability verdicts reproducible between runs and independently
verifiable by `financial-auditor`.

## Commands

Run with `python scripts/calc.py <command> [args]` via Bash. Every command
prints one JSON object to stdout.

### `future-value`
Compound growth of a lump sum plus monthly contributions.
```
python scripts/calc.py future-value --principal 0 --contribution 400 --annual-rate 0.072 --years 13
```
→ `{"future_value": 102842.71, ...}`

### `required-capital`
Capital needed to sustain a target monthly passive income at a given safe
withdrawal rate (e.g. 0.04 for the "4% rule" — always ask the calling agent to
cite where its SWR assumption comes from, this script does not invent one).
```
python scripts/calc.py required-capital --target-monthly-income 2000 --swr 0.04
```
→ `{"required_capital": 600000.0, ...}`

### `amortization`
Months to pay off a debt at a fixed monthly payment, and total interest paid.
Returns an `error` field instead of a payoff time if the payment doesn't even
cover the first month's interest (balance would never decrease).
```
python scripts/calc.py amortization --principal 8000 --annual-rate 0.14 --monthly-payment 1200
```
→ `{"months_to_payoff": 7, "total_interest_paid": 376.87, ...}`

### `convert-currency`
Simple conversion using a rate the calling agent already sourced (this script
has no network access and does not fetch rates itself).
```
python scripts/calc.py convert-currency --amount 1000 --rate 0.23
```
→ `{"converted_amount": 230.0, ...}`

### `cagr`
Compound annual growth rate between two prices over N years — use this to
turn a historical price series from the Yahoo Finance MCP into a return
figure instead of eyeballing it.
```
python scripts/calc.py cagr --start-price 100 --end-price 270 --years 15
```
→ `{"cagr": 0.0685, ...}`

## Who uses this and how

- **`market-data-fetcher`** calls `cagr` to turn historical prices from the
  Yahoo Finance MCP into a return figure.
- **`savings-goal-planner` / `debt-payoff-planner` / `retirement-income-planner`**
  call `future-value`/`amortization` while building candidate paths, to get
  real numbers for each path instead of guessing.
- **`feasibility-assessor`** calls it to produce the verdict's supporting
  calculation.
- **`financial-auditor`** calls it **independently**, with the same inputs
  the artifact claims to use, and compares its own result against what the
  artifact states. A mismatch beyond rounding is a gate failure attributed to
  whichever agent produced the artifact — this is what makes the "verdict is
  mathematically consistent" gate a real check instead of an LLM eyeballing
  the numbers.
