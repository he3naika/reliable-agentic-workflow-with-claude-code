# Cashflow Analysis — Personal Finance Goal Planner

Run: `run-2026-08-18-001` | Goal type: `debt_payoff`

## Net Income

- **3,000 USD/month.**
- Source: `artifacts/requirements.md` (user-stated). `income-tax-modeler` was
  **skipped** for this run (per requirements, Assumption A4: pure debt-payoff
  goal, no investment/tax-optimization component) — the stated income is
  treated directly as usable/net take-home income. No separate
  `net-income.md` artifact exists for this run.
- No jurisdiction-specific tax/social-contribution deduction has been applied
  to this figure, despite the user's confirmed country of residence being
  Poland. See Flags below.

## Expenses Breakdown

- **1,800 USD/month total** — user-stated as a single combined figure
  ("fixed + variable combined; no breakdown provided").
- `requirements.md` explicitly notes no category-level breakdown was
  supplied by the user, and this run does not invent one. This figure is
  used as-is and assumed to already include all the user's fixed and
  variable living costs.
- No category split (housing / food / transport / utilities / discretionary
  etc.) is available and none is fabricated here.
- **Resolved (this update):** the user has confirmed that this 1,800
  USD/month figure **already includes** the current/existing minimum
  monthly payment on the existing 8,000 USD PKO Bank Polski loan. This was
  previously an open ambiguity (see prior version of this artifact); it is
  now a confirmed fact per `requirements.md` and is no longer flagged as
  unresolved.

## Disposable Surplus

- **Disposable surplus = Net income − Expenses = 3,000 − 1,800 = 1,200 USD/month.**
- This matches the "raw monthly surplus" figure already noted in
  `requirements.md`'s Derived section.
- **Resolved treatment (this update):** because the 1,800 USD/month expense
  figure already includes the loan's existing minimum monthly payment, this
  entire 1,200 USD/month is available **on top of** the already-continuing
  minimum payment — no carve-out for the minimum payment is needed from this
  1,200 USD/month. `debt-payoff-planner` may treat the full 1,200 USD/month
  as extra/accelerated principal-payment capacity, subject to any liquidity
  buffer considerations (see Flags below).
- The loan's exact contractual minimum monthly payment still needs to be
  computed via `finance-math-toolkit` (current balance 8,000 USD, 14%
  annual, ~21 years remaining), but only to establish the baseline
  "minimum-only" payoff timeline/total-interest comparison case for
  `feasibility-assessor` — it is **not** needed to determine how much of the
  1,200 USD/month is "true extra," since all of it is.

## Flags

1. **Income basis unverified (relates to Assumption A4 — High materiality).**
   The 3,000 USD/month figure is used directly as net/usable income because
   `income-tax-modeler` was skipped for this goal type. The user's country
   of residence is confirmed as Poland; if 3,000 USD/month is actually a
   gross figure and the user in fact owes Polish income tax/social
   contributions on it, the true disposable surplus is materially lower than
   the 1,200 USD/month computed here. This is not softened — if this
   assumption is wrong, every downstream payoff-speed calculation is
   overstated.
2. **No expense category breakdown provided.** The 1,800 USD/month figure is
   a single undifferentiated total (now known to include the loan's minimum
   payment, per the resolved fact above, but otherwise undifferentiated).
   This analysis cannot distinguish fixed from variable, or flag which
   remaining categories might be compressible to free up additional surplus
   for debt payoff (relevant given the user's stated objective of fastest
   possible payoff). This limits the precision of any "surplus available to
   redirect" reasoning downstream.
3. **Zero liquidity buffer (relates to Assumption A5 — High materiality).**
   `requirements.md` records existing savings/emergency fund as assumed
   zero. Redirecting the full 1,200 USD/month surplus toward accelerated
   debt payoff, as the user's "as fast as possible" objective implies
   (Assumption A7), would leave no cash buffer for income disruption or
   unexpected expenses. This is flagged for `feasibility-assessor` to weigh
   explicitly (e.g. a "keep small buffer" path vs. a "max speed" path), not
   resolved here.
4. **Surplus magnitude relative to goal.** At face value, 1,200 USD/month
   against an 8,000 USD current balance is not a low or impractical surplus
   (40% of stated income) — this analysis does **not** flag the goal as
   impractical on cashflow grounds. This verdict is provisional only insofar
   as it assumes Flag 1 (income basis) does not overstate net income; the
   prior ambiguity about the loan payment's treatment (Flag 3 in the
   previous version of this artifact) is now resolved per `requirements.md`
   and no longer qualifies this figure.
