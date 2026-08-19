# Requirements — Personal Finance Goal Planner

## Goal Type

`savings_goal` — accumulate a target sum to purchase a new Mazda CX-5 by a
target date.

## Target Parameters

| Field | Value | Status |
|---|---|---|
| Asset | Mazda CX-5, new (not used) | Given by user |
| Target price/budget | **40,000 USD** (official dealer price for a new car) | Given by user |
| New vs. used | New | Given by user |
| Country/market | Belarus | Given by user |
| Target date / horizon | **31 December 2026** (today is 2026-08-18 → ~4.5 months) | Given by user |
| Parking vehicle during accumulation (cash only vs. willing to invest part) | **ASSUMPTION: cash-only, low-risk.** Horizon is only ~4.5 months, too short for meaningful investment risk-taking; a market drawdown close to the purchase date could jeopardize the goal. | ASSUMPTION — low materiality, reasonable default for a sub-6-month horizon; coordinator may confirm with user but not blocking |
| Financing/loan as part of the plan, or pure cash savings | ASSUMPTION: pure cash savings (no loan) — user said "save up for," not "finance" | ASSUMPTION — low materiality, ready to revisit if `savings-goal-planner`/`feasibility-assessor` finds pure cash savings infeasible in the time available |

Note on currency: the target price is fixed in **USD (40,000)**, but the user
plans/thinks in **BYN**. Both figures must be carried through explicitly;
`finance-math-toolkit`'s `convert-currency` function must perform the
USD→BYN conversion using a real, cited USD/BYN exchange rate with an access
date when `savings-goal-planner`/`feasibility-assessor` need a BYN-denominated
target amount. Do not hand-estimate this conversion.

## Current Position

| Field | Value | Status |
|---|---|---|
| Current age | Not provided | Not asked — low materiality for a savings_goal (target-amount/timeline math does not depend on age; only relevant for retirement-type goals). No blocking impact. |
| Current income | **8,000 BYN/month, confirmed NET (take-home)** by the user | Given by user |
| Contract type / citizenship | Not asked | Deliberately skipped — only needed for tax modeling, and income is already confirmed net, so `income-tax-modeler` is not required for this goal (see Constraints). |
| Country of residence | Belarus | Given by user |
| Monthly expenses (fixed + variable) | **2,537 BYN/month** (combined) | Given by user |
| Existing savings/investments (toward this goal) | **0 (none)** | Given by user |
| Existing debts | **None** | Given by user |
| Currency the user thinks in for this goal | **BYN** | Given by user |

## Constraints

- Income of 8,000 BYN/month was explicitly confirmed by the user as **net**
  (take-home) income, not gross. Because of this, **`income-tax-modeler`
  should be skipped for this run** — there is no tax/contribution modeling
  needed on top of an already-net figure. The coordinator should proceed
  directly to `cashflow-analyzer` (and `market-data-fetcher` only if/when a
  non-cash allocation is later introduced — currently not needed given the
  cash-only assumption above).
- Target price (40,000 USD) and planning currency (BYN) are different
  currencies. Any BYN-denominated target amount, monthly contribution
  requirement, or shortfall/surplus calculation must go through
  `finance-math-toolkit`'s currency conversion with a real, cited USD/BYN
  rate and access date — never hand-estimated or fabricated.
- No numeric target amount, income, or expense figures have been fabricated;
  all figures above were supplied directly by the user.
- Working assumptions carried forward (both low materiality, flagged, not
  blocking):
  - Cash-only / low-risk parking of savings during the ~4.5-month
    accumulation window (horizon too short for meaningful investment risk).
  - Pure cash savings, no financing/loan component.
- Age was not collected; this is treated as non-essential for a savings_goal
  (car purchase) since it does not feed into the required-capital, monthly
  contribution, or timeline calculations for this goal type.

## Confirmed

**Confirmed by user: 2026-08-18.** All essential fields for this
savings_goal are now known:

- Goal: save 40,000 USD (new Mazda CX-5, Belarus market) by 31 December 2026.
- Net income: 8,000 BYN/month; monthly expenses: 2,537 BYN/month.
- Existing savings toward goal: 0; existing debts: none.
- Planning currency: BYN (target price in USD, requires explicit conversion
  downstream).
- Parking assumption: cash-only/low-risk (low-materiality default given the
  short horizon).
- `income-tax-modeler` is not required for this run (income already net).

Ready to proceed to `cashflow-analyzer` → `savings-goal-planner`.
