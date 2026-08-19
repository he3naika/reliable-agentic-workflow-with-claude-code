# Requirements — Personal Finance Goal Planner

## Goal Type

`debt_payoff` — pay off an existing consumer/personal loan as fast as possible.

## Target Parameters

- **Remaining balance**: 8,000 USD — this is the **current outstanding
  balance as of today (2026-08-18)**, i.e. after ~4 years of amortization
  on the original loan, **not** the originally borrowed principal.
  The original principal amount is NOT stated by the user and is
  **not needed**: current balance + rate + remaining term are sufficient
  inputs for `finance-math-toolkit` to compute payoff schedules from today
  forward. Do not infer or back-calculate an original principal value.
- **Stated interest rate**: 14% annual (user-provided; compounding basis not
  stated — see Assumption A1)
- **Loan origination year**: **2022** (user-confirmed).
- **Original loan term**: **25 years** (user-confirmed).
- **Elapsed term as of 2026-08-18**: ~4 years.
- **Remaining term on original amortization schedule**: ~21 years
  (2022 + 25 = maturity ~2047; today is 2026, so ~21 years remain) —
  **derived from user-confirmed facts, to be precisely computed by
  `finance-math-toolkit`, not estimated in prose downstream**.
- **Lender / bank name**: **PKO Bank Polski (PKO BP), Poland** (user-confirmed).
  Country of residence (Poland) has now been explicitly confirmed by the user,
  which resolves the entity inference — "PKO" refers to PKO Bank Polski
  (PKO BP), a major Polish bank. `debt-payoff-planner` should research
  "PKO" / "PKO Bank Polski" / "PKO BP" loan products to identify the most
  likely product and terms.
- **Loan / product name**: still NOT PROVIDED (Assumption A2 — narrowed: only
  the product name remains unknown now that the lender and its country are
  known; `debt-payoff-planner` should attempt to research typical PKO BP
  personal/long-term installment loan terms and escalate only if it cannot
  narrow down rate structure/prepayment penalty from lender research alone).
  Given the 25-year original term, this is likely a mortgage-like or
  long-amortization secured/consumer loan product rather than a short-term
  personal loan — `debt-payoff-planner` should factor this into its
  research (e.g. narrow toward PKO BP mortgage/long-term installment loan
  products rather than short-tenor consumer credit).
- **Objective**: minimize time to full payoff (maximum feasible prepayment),
  not minimum-payment/cost-minimization

### MATERIAL FLAG for `debt-payoff-planner` and `feasibility-assessor`

The 25-year original term is a **material change** from the prior version
of this artifact (which had no term information at all, per Assumption A6).
Implications that MUST be handled downstream, not assumed:

1. The **contractual minimum required monthly payment** on the remaining
   ~21-year/8,000 USD balance at 14% annual is likely to be **small relative
   to the ~1,200 USD/month raw surplus** (income 3,000 − expenses 1,800),
   because the payment is amortized over a long remaining term. **This
   minimum payment amount still needs to be computed** via
   `finance-math-toolkit` (standard amortization calculation using: current
   balance 8,000 USD, rate 14% annual, ~21 years remaining) or confirmed
   directly from the loan documents/lender research — but see the
   **user-confirmed clarification below**, which changes what this
   computed figure is used for.
2. **USER-CONFIRMED CLARIFICATION (this update):** the stated 1,800 USD/month
   expenses figure **already INCLUDES the current/existing minimum monthly
   payment on this PKO loan**. This resolves the ambiguity previously
   flagged by `cashflow-analyzer` (it did not know whether the loan payment
   was inside or outside the 1,800 figure).
   **Downstream implication for `debt-payoff-planner` /
   `feasibility-assessor` / `finance-math-toolkit` usage:**
   - The **full ~1,200 USD/month raw surplus (income 3,000 − expenses
     1,800) is available ON TOP OF the already-continuing minimum loan
     payment.** The minimum payment does **not** need to be carved out of
     the 1,200 USD/month separately — it is already being paid for out of
     the 1,800 USD/month expense baseline.
   - `debt-payoff-planner` may treat the **entire 1,200 USD/month surplus as
     extra/accelerated principal-payment capacity** (subject to any buffer
     considerations under Assumption A5/A7 below), not as
     "surplus minus minimum payment."
   - The exact minimum payment figure is **still useful and should still be
     computed** via `finance-math-toolkit`, but now only for: (a) the
     baseline "no extra payment" comparison case (time-to-payoff and total
     interest if the user only ever pays the contractual minimum, i.e. does
     nothing extra), and (b) sanity-checking that the minimum payment is
     indeed ≤ the 1,800 USD/month expense figure (it must be, since it's
     already included in it). It is **no longer needed** to determine how
     much of the 1,200 USD/month surplus is "true extra" — all of it is.
3. This minimum payment (once computed) is required as the **baseline "no
   extra payment" comparison case** against which accelerated-payoff paths
   are measured for the feasibility verdict.
4. **Amortization schedule type is still unknown**: whether the loan uses
   standard equal-installment/annuity amortization (constant total payment,
   declining interest portion) vs. declining-balance/reducing (constant
   principal portion, declining total payment) changes both the minimum
   payment figure and the payoff-acceleration math. This is an **open item**
   for `debt-payoff-planner`'s lender/product research first; if research
   and the user cannot clarify it, **default to standard annuity/equal-
   installment amortization** (the overwhelmingly common structure for
   long-term Polish bank installment/mortgage-like products) and **flag this
   as an explicit assumption** in the resulting goal-paths artifact so
   `financial-auditor` can see it was assumed, not confirmed.

## Current Position

- **Current age**: **40** (user-confirmed; date of birth 15 June 1986,
  consistent with today's date 2026-08-18). This replaces the prior
  Assumption A3 (age assumed 30), which is now resolved and removed from
  the open-assumptions table.
- **Income**: 3,000 USD/month. **Country of residence: Poland (user-confirmed)**.
  Contract type and citizenship were not provided. For this goal
  `income-tax-modeler` is not required (pure debt payoff, no
  investment/tax-optimization component per workflow design), so the
  3,000 USD/month figure is treated as the usable take-home amount
  (Assumption A4 — **material**, see below).
- **Monthly expenses**: 1,800 USD/month (fixed + variable combined).
  **User-confirmed (this update): this 1,800 USD/month figure already
  INCLUDES the current/existing minimum monthly payment on the PKO loan
  described above.** No other breakdown was provided; the remainder of the
  figure (i.e. everything other than the loan's minimum payment) is assumed
  already comprehensive as stated.
- **Existing savings/investments**: not provided — assumed 0 / no emergency
  fund currently held (Assumption A5 — **material**)
- **Existing debts**: only the loan described above (current balance
  8,000 USD, originated 2022, 25-year original term); no other debts
  mentioned, assumed none
- **Currency user thinks in**: USD (explicit)

### Derived (for context only — not a calculation, coordinator/planner to
verify with `finance-math-toolkit`)
- Raw monthly surplus: 3,000 − 1,800 = 1,200 USD/month.
- **Since the 1,800 USD/month expense figure already includes the loan's
  minimum payment (user-confirmed this update), the full 1,200 USD/month is
  available as extra/accelerated principal-payment capacity ON TOP OF the
  minimum payment that continues to be paid within the 1,800 baseline.**
  `debt-payoff-planner` does not need to subtract a minimum-payment
  carve-out from this 1,200 USD/month figure. The exact minimum payment
  should still be computed via `finance-math-toolkit` (current balance
  8,000 USD, 14% annual, ~21 years remaining) solely to establish the
  baseline "minimum-only" payoff timeline for comparison purposes (see
  MATERIAL FLAG above).

## Constraints

- **Risk tolerance / aggressiveness**: user explicitly wants payoff "as fast
  as possible" — interpreted as willingness to redirect the large majority of
  monthly surplus toward extra principal payments (Assumption A7). Not
  explicitly asked whether user wants to retain any minimum liquidity buffer
  while doing so — flagged for feasibility-assessor to weigh given
  Assumption A5 (zero existing savings).
- Goal does not include an investment component; `market-data-fetcher` is not
  required.
- `income-tax-modeler` is not required given Assumption A4.

## Assumptions Requiring Confirmation (flagged for coordinator to surface)

| ID | Assumption | Why it matters | Materiality |
|---|---|---|---|
| A1 | Interest compounding is standard monthly amortizing (reducing-balance), 14% nominal annual rate | Changes exact time-to-payoff and total interest calculation | High |
| A2 | Lender confirmed as PKO Bank Polski (Poland); exact loan/product name still unknown; likely a long-amortization (25yr) product given confirmed term | `debt-payoff-planner` will research PKO BP long-term installment/mortgage-like loan products for likely rate structure/prepayment penalty; if research can't pin down a specific product, only the remaining unresolved fields (e.g. exact rate, prepayment penalty) should be re-asked | Medium — narrowed now that lender, country, and original term are all known |
| A4 | 3,000 USD/month income is already net/usable (no separate tax deduction modeled) | If this is actually gross income and the user owes significant tax/social contributions, real disposable surplus is lower than assumed, directly changing the payoff timeline | High |
| A5 | 0 existing savings/emergency fund | Redirecting nearly all surplus to debt with zero buffer increases risk of missed payments on shocks; feasibility-assessor should weigh a "keep small buffer" path vs. "max speed" path | High |
| A6 | Loan's contractual minimum monthly payment still needs computation (inputs now known: 8,000 USD balance, 14% annual, ~21 years remaining) | **Narrowed this update**: no longer needed to determine how much of the 1,200 USD/month surplus is "extra" (user confirmed the full 1,200 is extra, on top of the minimum already paid within the 1,800 expense baseline). Still needed to establish the baseline "minimum-only" payoff timeline/total-interest comparison case; MUST be computed via `finance-math-toolkit`, not estimated | Medium — narrowed from "blocks surplus determination" to "needed for baseline comparison only" |
| A7 | User wants maximum surplus redirected to extra payments ("as fast as possible") rather than a balanced approach | Determines which candidate path is framed as primary recommendation | Medium |
| A8 | Amortization schedule type (equal-installment/annuity vs. declining-balance) not confirmed; default to standard annuity if research/user can't clarify | Changes minimum payment figure and acceleration math; must be flagged as an explicit assumption in goal-paths artifact if defaulted | Medium |

Resolved this update: **expense/loan-payment overlap** — user has explicitly
confirmed that the 1,800 USD/month expenses figure already includes the
current minimum payment on the PKO loan. This resolves the ambiguity
previously flagged by `cashflow-analyzer` (whether the loan payment was
inside or outside the 1,800 figure) and removes the corresponding open item.
Net effect: the full 1,200 USD/month raw surplus is confirmed available as
extra/accelerated payment capacity, with no minimum-payment carve-out
required from it. A6 is narrowed accordingly (see table above) but not fully
closed, since the exact minimum-payment figure is still needed for the
baseline comparison case.

Previously resolved: **A3 (age)** — previously assumed 30, now
user-confirmed as 40 (DOB 1986-06-15); removed from the open assumptions
table. **Loan term** — previously fully unknown (part of old A6), now
user-confirmed: originated 2022, 25-year original term, ~21 years remaining
as of 2026-08-18. **A3b (country of residence)** — an inference from "PKO",
now a user-confirmed fact (Poland); folded into the Lender/bank name and
Income lines above.

These are **not** blocking further pipeline execution (per adaptive,
non-interactive handling for this run), but A1, A4, A5, A6, and A8 should be
surfaced to the user by the coordinator for awareness. A2 is now further
narrowed (lender, country, and original term all known) —
`debt-payoff-planner` should attempt research first and only escalate back
to the user for the specific fields (e.g. exact product, rate, prepayment
penalty, amortization type) it cannot determine, per the standard
escalation path.

## Confirmed

- Lender/bank name: **PKO Bank Polski (PKO BP)** — user-confirmed.
- Country of residence: **Poland** — user-confirmed.
- Age: **40** (DOB 1986-06-15) — user-confirmed, replaces prior
  age-30 assumption.
- Loan origination year: **2022**; original term: **25 years**; remaining
  term as of 2026-08-18: **~21 years** — user-confirmed.
- **Expense/loan-payment overlap: the 1,800 USD/month expenses figure
  already includes the current minimum payment on the PKO loan —
  user-confirmed (this update).** Full 1,200 USD/month raw surplus is
  therefore confirmed available as extra/accelerated payment capacity on
  top of the continuing minimum payment, with no carve-out needed.
- Current remaining balance (8,000 USD, as of today, not original
  principal), rate (14% annual, as stated), income (3,000 USD/month),
  expenses (1,800 USD/month), currency (USD), objective (fastest payoff),
  and the absence of other debts are unchanged from the prior version of
  this artifact and remain user-stated facts.

The user has reviewed this update and raised no further corrections.
Remaining items (A1, A2, A4, A5, A6, A7, A8, and the loan/product name)
remain open assumptions/unknowns to be handled downstream (research first
via `debt-payoff-planner`, escalate only what research cannot resolve)
rather than blockers to proceeding.

**Requirements confirmed: 2026-08-18.** This version is ready for the
coordinator to proceed with, pending the coordinator's own confirmation step.
