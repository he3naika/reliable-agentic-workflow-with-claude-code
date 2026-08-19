# Requirements — run-2026-08-18-003

## Goal Type
retirement_income

## Target Parameters
- Target monthly passive income: 2,000 EUR/month
- Target age: 50 (current age 40 → 10-year horizon)
- Risk tolerance: moderate

## Current Position
- Current age: 40
- Current income: 25,000 PLN/month, explicitly confirmed by user as NET
  (take-home). This figure is now **doubly confirmed**: originally stated as
  net by the user, then re-examined after `income-tax-modeler` flagged an
  initial ambiguity around B2B "net" claims in Poland (since B2B net income
  can be less clean than employment net income). The user has since
  clarified and reconfirmed: 25,000 PLN/month is the amount that remains
  **after paying all taxes, including ZUS** — i.e., it is the true net
  take-home income, with no further mandatory deductions outstanding.
- Contract type: B2B (self-employed/business contract)
- B2B tax form: **ryczałt (lump-sum tax)**, confirmed by user — not podatek
  liniowy (flat tax). This resolves the ambiguity `income-tax-modeler` had
  flagged; `income-tax-modeler` should model net income using the ryczałt
  regime specifically, not the flat-tax (liniowy) regime.
- Country of residence: Poland
- Citizenship: Republic of Poland
- Monthly expenses: user confirmed expenses exist but are covered from a separate
  budget, NOT deducted from and NOT part of the stated 25,000 PLN figure. The
  user is willing to invest the FULL 25,000 PLN/month toward this goal.
  **Downstream note for cashflow-analyzer: treat the full 25,000 PLN/month as
  investable surplus as stated by the user; do not subtract, infer, or invent
  any expense figure — none was given and none should be assumed.**
- Existing savings/investments: 200,000 PLN, held in a PKO Bank Polski savings
  account (cash, not invested)
- Existing debts: none

## Constraints
- Currency to plan in: EUR (the 2,000 EUR/month target is already stated in
  EUR). Income (25,000 PLN/month) and existing savings (200,000 PLN) are in
  PLN and require explicit PLN → EUR conversion downstream via
  `finance-math-toolkit`, using a real, cited exchange rate with access date
  — no assumed/rounded rate.
- Both `income-tax-modeler` and `market-data-fetcher` must run for this
  retirement_income goal (per CLAUDE.md, retirement_income always requires
  both, regardless of income being stated as net).
  - `income-tax-modeler`: the B2B tax form is now confirmed as **ryczałt**
    (lump-sum tax), not podatek liniowy. The user has explicitly confirmed
    that 25,000 PLN/month is the amount remaining after paying all taxes
    (under the ryczałt regime) and all ZUS (social insurance) contributions
    — i.e., it is the true, final net take-home figure. `income-tax-modeler`
    should treat this as confirmed net income and does not need to
    independently re-derive it from gross, but should still cite the
    applicable ryczałt rate/rules for this activity type and confirm no
    other mandatory statutory deduction (e.g. health contribution under
    "Polski Ład" rules for ryczałt payers) is outstanding beyond what the
    user has already accounted for, with cited sources.
  - `market-data-fetcher`: source real historical return data for
    moderate-risk benchmark instruments appropriate to a 10-year horizon
    (e.g. a balanced equity/bond portfolio, diversified index funds/ETFs),
    each with a cited source and access date.

## Confirmed
Confirmed by user on 2026-08-18 (all base + goal-specific questions answered
across two Q&A rounds). No disputes raised on the summary presented.

Addendum confirmed by user on 2026-08-18: B2B tax form is ryczałt (lump-sum
tax), and the 25,000 PLN/month net take-home figure is reconfirmed as the
amount remaining after all taxes and ZUS contributions — resolving the
ambiguity `income-tax-modeler` had flagged. No other changes.
