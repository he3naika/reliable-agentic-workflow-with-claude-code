# Requirements

## Goal Type

`retirement_income` — target passive income by a target age.

## Target Parameters

- Target monthly passive income: **2,000 EUR/month**
- Target age: **55** (current age 35 → 20-year horizon)
- Risk tolerance: **moderate**
- Currency the user thinks in for this goal: **EUR** (target stated in EUR; note that current income/expenses/savings are in PLN — see Constraints)

## Current Position

- Current age: **35**
- Country of residence: **Poland**
- Citizenship: **Polish** (tax resident in Poland, same as country of residence)
- Employment: **freelance IT contractor, B2B contract, no employer** (self-employed/B2B in Poland)
- Current gross income: **12,000 PLN/month gross, before any deductions**
- Monthly expenses: **6,000 PLN/month** (fixed + variable not broken out; taken as a single combined figure)
- Existing savings/investments: **50,000 PLN in a bank savings account; no investments yet**
- Existing debts: **none**

## Constraints

- Willing to invest in index funds during accumulation (not cash-only).
- Mixed currency inputs: income/expenses/savings stated in PLN, goal target stated in EUR — conversion will need to be explicit and sourced (handled downstream by `finance-math-toolkit` / `cashflow-analyzer`, not assumed here).
- Expense figure (6,000 PLN/month) is given as a single combined number, not split into fixed vs. variable; treated as reasonable at this stage, not a materially blocking gap.
- Risk tolerance is moderate — asset allocation recommendations from `retirement-income-planner` should reflect this (not full-equity aggressive, not cash-only conservative).

## Confirmed

Confirmed with user 2026-08-19. All base and goal-specific requirements for a `retirement_income` goal are now complete.
