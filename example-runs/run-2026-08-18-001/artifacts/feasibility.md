# Feasibility Assessment — Debt Payoff

Run: `run-2026-08-18-001` | Goal type: `debt_payoff` | Assessor: `feasibility-assessor`

## Inputs Used (from upstream artifacts)

- Current loan balance: 8,000 USD (14% annual, fixed, standard annuity,
  reducing-balance monthly compounding) — `goal-paths.md`.
- Disposable monthly surplus: **1,200 USD/month** (income 3,000 USD −
  expenses 1,800 USD, expenses already include the loan's existing minimum
  payment) — `cashflow.md`, `requirements.md`.
- Zero existing savings/emergency buffer (Assumption A5) — `requirements.md`.
- Objective: pay off as fast as reasonably possible (Assumption A7), with
  the liquidity-buffer risk explicitly flagged for this assessor to weigh
  (`cashflow.md` Flag 3, `requirements.md` MATERIAL FLAG / A5).
- Prepayment penalty: none, per PKO BP's own published 0% early-repayment
  commission policy (`goal-paths.md` Assumptions & Sources item 2). Note:
  the previously-cited statutory-threshold argument for this conclusion has
  been withdrawn by `goal-paths.md` as unsound (invalid currency comparison)
  and is **not** relied on anywhere in this assessment either — the "no
  penalty" conclusion rests solely on PKO BP's own policy.

## Per-Path Verdict

### Path 1 — Minimum Payment Only (baseline)

- **Required monthly commitment**: 98.65 USD/month.
- **Verdict: ACHIEVABLE, but does not meet the stated objective.**
  98.65 USD/month is far below the 1,200 USD/month disposable surplus (and
  is already funded inside the 1,800 USD/month expense baseline per
  `requirements.md`), so there is no affordability problem. However, this
  path takes 252 months (21 years) and pays 16,840.75 USD in interest —
  more than double the original 8,000 USD balance — which directly
  contradicts the user's stated objective of paying off "as fast as
  possible." It exists only as the required comparison baseline, not as a
  recommended path.

### Path 2 — Balanced Payoff (698.65 USD/month = 98.65 minimum + 600 extra)

- **Required monthly commitment**: 698.65 USD/month total, i.e. 600 USD/month
  of the 1,200 USD/month surplus redirected to extra principal, with the
  remaining 600 USD/month building a cash buffer in parallel.
- **Verdict: ACHIEVABLE.** 600 USD/month extra-principal commitment is
  exactly half of the 1,200 USD/month surplus and well within it; no shortfall.
  Payoff in 13 months, total interest 638.23 USD. This path also directly
  addresses the zero-buffer risk flagged in `cashflow.md` (Flag 3) and
  `requirements.md` (A5): by month 13 it has built ≈7,800 USD (13 × 600 USD)
  of liquid savings alongside payoff, rather than leaving the user fully
  exposed with no buffer during the payoff window.

### Path 3 — Aggressive Full-Surplus Payoff (1,298.65 USD/month = 98.65 minimum + full 1,200 extra)

- **Required monthly commitment**: 1,298.65 USD/month total, i.e. the entire
  1,200 USD/month surplus redirected to extra principal.
- **Verdict: ACHIEVABLE on paper, but carries a real liquidity-risk
  cost the user should weigh.** The full 1,200 USD/month surplus exists and
  covers the required extra payment exactly (no shortfall against
  disposable surplus), and payoff completes in 7 months at only 352.22 USD
  total interest — the fastest and cheapest-in-interest path. But because
  existing savings are assumed to be zero (Assumption A5) and this path
  commits 100% of surplus to the loan with no parallel buffer, any income
  disruption or shock expense during the 7-month window would have to be
  absorbed with zero liquid cushion. The math is achievable; the risk
  profile is materially higher than Path 2's for a marginal gain (6 months
  saved, 286.01 USD less interest than Path 2).

## Supporting Calculation

All three paths were independently recomputed via `finance-math-toolkit`
using each path's own stated principal, rate, and monthly payment (not
copied from `goal-paths.md`):

```
python scripts/calc.py amortization --principal 8000 --annual-rate 0.14 --monthly-payment 98.65
→ {"months_to_payoff": 252, "total_interest_paid": 16840.75, ...}

python scripts/calc.py amortization --principal 8000 --annual-rate 0.14 --monthly-payment 698.65
→ {"months_to_payoff": 13, "total_interest_paid": 638.23, ...}

python scripts/calc.py amortization --principal 8000 --annual-rate 0.14 --monthly-payment 1298.65
→ {"months_to_payoff": 7, "total_interest_paid": 352.22, ...}
```

All three independently-recomputed figures (months to payoff and total
interest) match `goal-paths.md` exactly — no discrepancy found. These
payoff-time/interest figures were unaffected by the correction made to
`goal-paths.md`'s Assumptions & Sources section (which only withdrew a
currency-conversion/statutory-threshold argument used as secondary
supporting evidence for the "no prepayment penalty" conclusion); the
underlying loan balance, rate, and payment amounts were never in question.

**Surplus-vs-requirement check** (disposable surplus = 1,200 USD/month, per
`cashflow.md`):

| Path | Extra payment required | ≤ 1,200 USD/month surplus? | Headroom |
|---|---|---|---|
| 1 | 0 USD/month (minimum only, inside 1,800 baseline) | Yes | 1,200 USD/month unused for debt |
| 2 | 600 USD/month | Yes | 600 USD/month left over (built into buffer) |
| 3 | 1,200 USD/month | Yes, exactly | 0 USD/month — no buffer margin |

No path exceeds the disposable surplus, so all three are mathematically
affordable. The differentiator is not affordability but risk (liquidity
buffer) and speed-vs-buffer trade-off, per Assumption A5/A7 and `cashflow.md`
Flag 3.

## Ranking

1. **Path 2 — Balanced Payoff (recommended).** Fully affordable, pays off
   the loan in just over a year (13 months) at very low total interest
   (638.23 USD), and — critically given the user's confirmed zero existing
   savings (Assumption A5) — builds a ≈7,800 USD liquidity buffer in
   parallel rather than leaving the user fully exposed. Best match to the
   user's implicit risk profile: "as fast as possible" without ignoring the
   zero-buffer flag that `cashflow.md` and `requirements.md` both raise as
   high-materiality. Recommended primary path.
2. **Path 3 — Aggressive Full-Surplus Payoff.** Fastest (7 months) and
   cheapest in total interest (352.22 USD) if the user's dominant
   preference is truly "speed above all else" (per stated objective and
   Assumption A7) and they are willing to accept zero liquidity cushion for
   that ~7-month window. Acceptable as an alternate/aggressive option, but
   only if the user explicitly accepts the flagged risk of having no buffer
   for income disruption or shock expenses during payoff; otherwise Path 2
   is the better match to the user's overall situation.
3. **Path 1 — Minimum Payment Only.** Achievable as a "do nothing extra"
   baseline and useful only for comparison. Not recommended: it directly
   contradicts the user's stated "as fast as possible" objective, taking
   21 years and costing 16,840.75 USD in interest versus 638.23-352.22 USD
   for the other two paths.

**Overall verdict: achievable.** The user's disposable surplus (1,200
USD/month) comfortably covers every candidate path's required extra
payment, so the goal ("pay off the 8,000 USD PKO BP loan as fast as
reasonably possible") is achievable under all three paths; the meaningful
choice is between Path 2's balanced speed-with-buffer approach (recommended)
and Path 3's maximum-speed-zero-buffer approach, not between achievable and
unachievable.
