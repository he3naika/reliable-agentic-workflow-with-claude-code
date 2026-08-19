# Cashflow Analysis — run-2026-08-18-003

## Net Income

- **Confirmed net income: 25,000.00 PLN/month** (300,000.00 PLN/year).
- Source: `artifacts/net-income.md` (§ "Net Income"), which in turn is based
  on the user's explicit, doubly-confirmed statement that 25,000 PLN/month is
  the amount remaining after all taxes (ryczałt ewidencjonowany) and all ZUS
  (social insurance) and health contributions — i.e. a fully net,
  post-deduction take-home figure. `income-tax-modeler` independently
  sanity-checked this figure against ryczałt/ZUS mechanics for a B2B IT
  contractor and found it plausible; it did not need to re-derive it from
  gross since the net figure was directly confirmed by the user.
- Currency: PLN. The plan currency is EUR (per `requirements.md` §
  Constraints); PLN → EUR conversion of this figure must be performed
  downstream via `finance-math-toolkit` using a real, cited exchange rate
  with access date — no conversion is applied in this artifact.

## Expenses Breakdown

- **No expense figures are deducted in this analysis.**
- Per `requirements.md` (§ Current Position and § Constraints /
  downstream note to `cashflow-analyzer`): the user explicitly confirmed
  that their monthly living expenses exist but are covered from a **separate
  budget outside the stated 25,000 PLN/month figure**. Expenses are
  therefore NOT netted against income here, by explicit user instruction —
  this is not a missing/skipped step.
- No fixed-expense or variable-expense figures were collected or estimated
  for this run, and none should be inferred or fabricated. This is
  intentional and specific to this run's stated basis, not the normal
  process (which would otherwise subtract fixed + variable expenses from net
  income).
- Fixed expenses considered: none applicable (excluded from this budget by
  user statement).
- Variable expenses considered: none applicable (excluded from this budget
  by user statement).

## Disposable Surplus

- **Disposable monthly surplus = full confirmed net income = 25,000.00
  PLN/month**, because no expense deduction applies (see Expenses Breakdown
  above and Flags below).
- Calculation: 25,000.00 PLN/month (net income) − 0 (fixed expenses,
  excluded by user statement) − 0 (variable expenses, excluded by user
  statement) = **25,000.00 PLN/month**.
- This is the PLN figure available before any downstream PLN → EUR
  conversion, which `goal-path-planner` (here: `retirement-income-planner`)
  must perform via `finance-math-toolkit` with a cited exchange rate.
- Existing savings of 200,000 PLN (PKO Bank Polski savings account, cash,
  uninvested) are a separate stock/balance-sheet figure, not part of the
  monthly disposable surplus flow computed here. They should be treated as
  a starting lump sum available for allocation by the goal-path-planner,
  not double-counted as additional monthly surplus.

## Flags

1. **Unusual basis — expenses intentionally excluded from this calculation,
   not omitted by error.** Normally this agent computes disposable surplus
   as net income minus fixed and variable expenses. For this run, the user
   explicitly and repeatedly confirmed (see `requirements.md` § Current
   Position: "Monthly expenses: user confirmed expenses exist but are
   covered from a separate budget, NOT deducted from and NOT part of the
   stated 25,000 PLN figure") that their real-world living expenses are
   funded entirely outside the stated 25,000 PLN/month figure, and that the
   full 25,000 PLN/month is intended to be available toward the retirement
   income goal. Accordingly, the full net income figure is carried forward
   unchanged as the disposable surplus. Downstream agents
   (`retirement-income-planner`, `feasibility-assessor`,
   `financial-auditor`) should treat this 25,000 PLN/month as the genuine
   monthly contribution capacity, not as an unvetted or partial figure — the
   absence of an expense line item here is deliberate and sourced, not a gap.
2. **No plausibility concern on surplus size relative to goal.** The stated
   target is 2,000 EUR/month passive income by age 50 (10-year horizon), with
   a 25,000 PLN/month (~300,000 PLN/year) contribution capacity plus a
   200,000 PLN existing lump sum. This surplus is large relative to typical
   goals of this shape; nothing here suggests impracticality on cashflow
   grounds. (Feasibility given actual required capital and market
   assumptions is `feasibility-assessor`'s responsibility, not this
   artifact's.)
3. **Currency conversion outstanding.** All monetary figures in this
   artifact are stated in PLN. The plan is denominated in EUR. PLN → EUR
   conversion has not been performed here and must be done downstream via
   `finance-math-toolkit` with a real, cited exchange rate and access date —
   per `requirements.md` § Constraints.
4. **Residual caveats from `net-income.md` carry forward.** The exact
   ryczałt PIT rate and exact gross revenue underlying the confirmed
   25,000 PLN/month net figure remain unconfirmed (PKWiU classification not
   provided) but are not needed downstream since the net figure was used
   directly, per `income-tax-modeler`'s explicit note. This does not affect
   the disposable-surplus figure computed here, which depends only on the
   confirmed net income and the user's expense-exclusion statement, not on
   the gross-to-net derivation.
