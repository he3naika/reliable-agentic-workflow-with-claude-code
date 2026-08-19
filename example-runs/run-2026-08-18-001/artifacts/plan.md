# Financial Goal Plan — Pay Off PKO Bank Polski Loan (8,000 USD)

## Executive Summary

**Verdict: achievable.** Your 1,200 USD/month disposable surplus (3,000 USD
income − 1,800 USD expenses, which already includes your current loan
payment) comfortably covers every candidate payoff path for your 8,000 USD
PKO Bank Polski loan at 14% annual interest. The recommended path is the
**Balanced Payoff**: pay **698.65 USD/month** (98.65 USD minimum + 600 USD
extra) to clear the loan in **13 months**, while simultaneously building a
**~7,800 USD cash buffer** — because you currently have zero savings, and
committing 100% of your surplus to the fastest possible payoff would leave
you with no cushion at all during the payoff window. If you value raw speed
over having a buffer, a faster alternative (7 months, no buffer) is also
presented below for you to choose.

## Current Position

- **Income**: 3,000 USD/month, treated as usable/net take-home pay for this
  analysis (see Assumptions & Caveats — this has not been independently
  verified against Polish tax rules).
- **Net income**: 3,000 USD/month (no separate tax/social-contribution
  deduction modeled; `income-tax-modeler` was not run for this debt-payoff
  goal — see caveats).
- **Monthly expenses**: 1,800 USD/month (fixed + variable combined,
  user-stated; already includes the current minimum payment on the PKO BP
  loan).
- **Disposable surplus**: 1,200 USD/month (3,000 − 1,800).
- **Existing debts**: one loan with PKO Bank Polski (PKO BP), Poland —
  current remaining balance 8,000 USD, 14% annual fixed rate, standard
  annuity (equal-installment) amortization, originated 2022 on a 25-year
  term, ~21 years (252 months) remaining as of 2026-08-18. Computed
  contractual minimum payment: 98.65 USD/month. No prepayment penalty
  applies, per PKO Bank Polski's published 0% early-repayment commission
  policy for its cash-loan product family (source: TVN24 Biznes,
  "PKO BP zwróci koszty prowizji. Wcześniejsza spłata pożyczki lub kredytu",
  https://tvn24.pl/biznes/pieniadze/pko-bp-zwroci-koszty-prowizji-wczesniejsza-splata-pozyczki-lub-kredytu-st4618085,
  accessed 2026-08-18 — see Assumptions & Caveats for why this is a close
  match rather than a confirmed exact match to your specific loan product).
- **Existing savings/emergency buffer**: 0 (assumed; not stated by user).
- **Currency**: USD (as stated by the user).

## Paths Considered

### Path 1: Minimum Payment Only (baseline, not recommended)
- Target capital/amount: 8,000 USD current balance paid down to 0.
- Monthly contribution: 98.65 USD/month (contractual minimum only; no extra
  payment).
- Where to allocate: 98.65 USD/month to the PKO BP loan's standard
  installment; the remaining 1,200 USD/month surplus is not redirected to
  the loan in this path.
- Timeline: 252 months (21.0 years) to full payoff, on the loan's original
  schedule.
- Verdict: Achievable (well within surplus), but does **not** meet the
  stated objective of paying off "as fast as possible." Total interest paid:
  16,840.75 USD — more than double the current balance. Exists only as the
  required comparison baseline.

### Path 2: Balanced Payoff — RECOMMENDED
- Target capital/amount: 8,000 USD current balance paid down to 0, plus a
  parallel cash buffer.
- Monthly contribution: 698.65 USD/month total (98.65 USD minimum + 600
  USD/month extra principal payment).
- Where to allocate: 600 USD/month of the 1,200 USD/month surplus to extra
  principal payment on the PKO BP loan; the remaining 600 USD/month to a
  liquid cash emergency buffer (e.g. a standard Polish bank
  savings/oszczędnościowe account).
- Timeline: 13 months to full payoff. By month 13, this path has also
  accumulated ≈7,800 USD (13 × 600 USD) in a liquid buffer, and after payoff
  the full 698.65 USD/month is freed up for further savings or other goals.
- Verdict: Achievable. 600 USD/month extra-principal commitment is exactly
  half of the 1,200 USD/month surplus, well within it. Total interest paid:
  638.23 USD.

### Path 3: Aggressive Full-Surplus Payoff (fastest option, valid alternative)
- Target capital/amount: 8,000 USD current balance paid down to 0.
- Monthly contribution: 1,298.65 USD/month total (98.65 USD minimum + the
  full 1,200 USD/month surplus as extra principal payment).
- Where to allocate: the entire 1,200 USD/month surplus to extra principal
  payment on the PKO BP loan; no separate buffer is built during the payoff
  window.
- Timeline: 7 months to full payoff. From month 8 onward, the full 1,298.65
  USD/month is freed for emergency-fund building or other goals — reaching
  Path 2's ~7,800 USD buffer target in well under 6 months post-payoff.
- Verdict: Achievable on paper — the full 1,200 USD/month surplus exists and
  covers the required extra payment exactly, with payoff completing in 7
  months at only 352.22 USD total interest (the fastest and cheapest-in-
  interest path). However, this path commits 100% of surplus to the loan
  with **zero liquidity buffer** for its full 7-month duration; any income
  disruption or shock expense during that window would have no cash cushion
  behind it. Choose this path only if you are comfortable accepting that
  risk in exchange for the fastest payoff and the lowest total interest.

## Verdict

**Overall verdict: achievable.** All three paths are mathematically
affordable — no path's required extra payment exceeds the 1,200 USD/month
disposable surplus:

| Path | Extra payment required | ≤ 1,200 USD/month surplus? | Headroom | Months to payoff | Total interest |
|---|---|---|---|---|---|
| 1 — Minimum only | 0 USD/month | Yes | 1,200 USD/month unused for debt | 252 | 16,840.75 USD |
| 2 — Balanced (recommended) | 600 USD/month | Yes | 600 USD/month (built into buffer) | 13 | 638.23 USD |
| 3 — Aggressive | 1,200 USD/month | Yes, exactly | 0 USD/month — no buffer margin | 7 | 352.22 USD |

All payoff-time and total-interest figures are direct, independently
recomputed outputs of `finance-math-toolkit`'s amortization calculation
(principal 8,000 USD, 14% annual rate, standard annuity), cross-checked by
`financial-auditor` against `goal-paths.md` with no discrepancy found. The
choice between paths is not a question of affordability but of speed versus
liquidity risk, given your confirmed zero existing savings.

## Recommendation

**Recommended path: Path 2 — Balanced Payoff (698.65 USD/month, 13 months,
~7,800 USD buffer built in parallel).**

This is recommended over Path 3 (the mathematically fastest option, 7
months) because you currently have **zero existing savings**. Committing
100% of your surplus to the loan under Path 3 would clear the debt 6 months
sooner and save 286.01 USD in additional interest, but it would leave you
completely exposed to any income disruption or unexpected expense for that
entire 7-month window, with no cash cushion at all. Path 2 reaches full
payoff in just over a year (13 months) at very low total interest (638.23
USD) while simultaneously building a meaningful ~7,800 USD liquidity buffer
— directly addressing the zero-buffer risk. The trade-off is a modest one:
6 extra months and 286.01 USD more interest than Path 3, in exchange for
financial resilience during the payoff period.

**Path 3 remains a valid alternative** if speed and minimizing total
interest are your dominant priorities and you are explicitly willing to
accept having no cash buffer for those 7 months. Path 1 (minimum payment
only) is not recommended under either preference — it satisfies neither the
speed objective nor materially improves your risk position, and costs far
more in total interest (16,840.75 USD).

## Action Plan

- **This month (Month 1)**: Confirm your exact PKO BP loan product and
  payment details directly with the bank (see Assumptions & Caveats below —
  the terms used here are researched from PKO BP's closest comparable
  product, not confirmed against your exact loan). Set up an automatic
  monthly payment of 698.65 USD to the loan (98.65 USD contractual minimum +
  600 USD extra principal), and open/designate a separate savings account
  for the parallel buffer if you don't already have one.
- **Months 1–13**: Pay 698.65 USD/month toward the PKO BP loan (with the 600
  USD/month extra explicitly applied to principal, not just as a larger
  regular installment — confirm with PKO BP how to designate extra payments
  as principal-reduction to avoid it being misapplied). In parallel, direct
  the other 600 USD/month of your surplus into the liquid emergency buffer
  account.
- **Month 13**: Loan should reach full payoff (8,000 USD balance cleared),
  with total interest paid of approximately 638.23 USD. Your buffer account
  should hold approximately 7,800 USD at this point.
- **Month 14 onward**: With the loan paid off, the full former loan payment
  capacity (698.65 USD/month) is freed up. Redirect it toward continuing to
  grow your emergency buffer beyond 7,800 USD (a common target is 3–6
  months of expenses, i.e. roughly 5,400–10,800 USD based on your 1,800
  USD/month expense figure) and/or toward your next financial goal.
- **Ongoing / if you prefer speed over buffer**: If at any point you decide
  you'd rather prioritize speed and are comfortable with zero buffer, you
  can switch to Path 3 (1,298.65 USD/month, full surplus to the loan) —
  this would complete payoff in fewer total months from whenever you switch,
  at a small additional interest savings, but leaves no cash cushion until
  the loan is cleared.

## Assumptions & Caveats

These caveats were carried forward from `financial-auditor`'s review and
should be weighed alongside the numbers above:

1. **Income basis not independently verified.** The 3,000 USD/month income
   figure is treated as net/usable take-home income for all calculations in
   this plan. `income-tax-modeler` was not run for this goal (pure
   debt-payoff goals with no investment component skip this step by design).
   Your confirmed country of residence is Poland; if 3,000 USD/month is
   actually a gross figure and you owe Polish income tax/social
   contributions on it, your true disposable surplus is lower than the 1,200
   USD/month used throughout this plan, and every payoff timeline above
   would be correspondingly slower. If you're unsure whether this figure is
   gross or net, this is worth confirming before committing to a payment
   plan.
2. **Loan-term research is a close match, not a confirmed exact match.**
   PKO Bank Polski's researched loan terms used in this plan (0%
   early-repayment commission with no penalty, standard annuity
   amortization; source: TVN24 Biznes, accessed 2026-08-18, cited above)
   come from PKO BP's published cash-loan ("pożyczka gotówkowa") product
   family, whose maximum published tenor is 96 months (8 years) — shorter
   than your stated 25-year original loan term. This product was used as
   the closest comparable match because it independently confirmed the
   amortization structure and the absence of a prepayment penalty, but it
   does not exactly match your loan's longer tenor. Your actual loan may be
   a different PKO product (e.g. a secured or mortgage-adjacent installment
   loan) with different exact terms. It is worth confirming directly with
   PKO BP that no early-repayment penalty applies to your specific loan
   before making large extra payments.
