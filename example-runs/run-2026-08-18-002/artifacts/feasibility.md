# Feasibility Assessment — Personal Finance Goal Planner

Source artifacts: `artifacts/requirements.md`, `artifacts/cashflow.md`,
`artifacts/goal-paths.md` (corrected version — Path 3 now anchored to a real
Belarus-market listing, with the US-market Edmunds figures retained only as a
labeled low/high sensitivity band). All figures below were **independently
recomputed** with `finance-math-toolkit` (`future-value`, `convert-currency`)
using each path's own stated inputs, not copied from `goal-paths.md`.

Confirmed disposable surplus (from `cashflow.md`): **5,463 BYN/month**
(8,000 BYN net income − 2,537 BYN combined expenses; both user-stated
figures, not externally sourced).

## Per-Path Verdict

### Path 1 — Full target (40,000 USD), exact deadline (31 Dec 2026)

**NOT achievable.**

The exact 4-month window to 31 Dec 2026 requires a monthly contribution of
30,379.88 BYN — **5.6× the actual 5,463 BYN/month disposable surplus**.
Saving 100% of the surplus for the full 4 months yields only 21,852 BYN
(≈7,193 USD), about 18% of the 40,000 USD target. There is no scenario
within the confirmed constraints (cash-only, no financing, 8,000 BYN net
income, 2,537 BYN expenses) under which this path closes. Closing the gap
would require ~24,917 BYN/month of additional income, an asset sale, gifted
funds, or financing — all explicitly out of scope per `requirements.md`.

### Path 2 — Full target (40,000 USD), extended timeline at current surplus

**Achievable, but only with the deadline moved from 31 Dec 2026 to ~late
July 2028 (23 months from today).**

Saving the full 5,463 BYN/month surplus with 0% return reaches 120,186.00
BYN at 22 months (still 1,333.52 BYN short of the 121,519.52 BYN target) and
125,649.00 BYN at 23 months (clears the target with 4,129.48 BYN to spare).
23 months is therefore the minimum timeline that fully covers the target —
roughly **19 months past** the user's original date. This path is the only
one of the three that preserves the user's original requirement exactly (new
car, full 40,000 USD budget); the only variable that has to change is the
date, and it is contingent on 100% of the current surplus being preserved,
uninterrupted, for the entire 23-month period.

### Path 3 — Reduced target: used Mazda CX-5, faster (but still delayed) timeline

**Achievable, and now adequately grounded** — this supersedes the prior
"conditionally achievable due to unbounded price" framing, which no longer
applies now that the primary target is a real, dated Belarus-market listing
rather than an unbounded foreign proxy.

Recomputed timelines at 5,463 BYN/month, 0% return, for all three stated
price points:

| Price point | Target (BYN) | Month before | Month that clears it |
|---|---|---|---|
| Low (Edmunds low, sensitivity only) | 77,969.96 | 14mo → 76,482.00 (short) | **15mo → 81,945.00** |
| **Most likely (av.by real anchor)** | **98,099.00** | 17mo → 92,871.00 (short) | **18mo → 98,334.00** |
| High (Edmunds high, sensitivity only) | 115,188.35 | 21mo → 114,723.00 (short) | **22mo → 120,186.00** |

All six values match `goal-paths.md` exactly on independent recomputation —
no discrepancy in the timeline math.

Grounding assessment: the primary target (98,099 BYN) is now a real, sourced,
dated listing — 2023 Mazda CX-5, ~7,000 km — [Mazda CX-5 listings,
cars.av.by](https://cars.av.by/mazda/cx-5), accessed 2026-08-18 — rather than
a US-market appraisal transplanted onto a different market. The previous
Edmunds range (77,969.96–115,188.35 BYN, from [2026 Mazda CX-5 Value |
Edmunds](https://www.edmunds.com/mazda/cx-5/2026/appraisal-value/), accessed
2026-08-18) is retained only as a labeled bracket around that anchor, and the
anchor falls inside it — a real cross-check, not just a relabeling. This is a
materially stronger basis than the prior version of this path: the range is
now bounded by one real comparable plus a plausibility band, not an unbounded
single foreign figure. Residual uncertainty is real but now bounded and
disclosed: exact price still depends on year/mileage/trim, so the 15–22
month range (most likely ~18 months, mid-February 2028) should be treated as
a well-supported estimate, confirmed with 2–3 concrete av.by/dealer quotes
before locking a date — not as a guaranteed single figure.

This path is faster than Path 2 across its entire range (15–22 months vs.
Path 2's fixed 23 months) but requires accepting a used car instead of the
originally stated new car, and — like Path 2 — still requires moving the
date well past 31 Dec 2026.

## Supporting Calculation

All figures recomputed independently via `finance-math-toolkit`
(`future-value`, `convert-currency`); inputs below are as stated in the
corrected `goal-paths.md`. USD/BYN rate used throughout: **1 USD = 3.037988
BYN**, as of 2026-08-16 — [US Dollar (USD) To Belarusian Ruble (BYN) Exchange
Rate History for 2026](https://www.exchange-rates.org/exchange-rate-history/usd-byn-2026),
accessed 2026-08-18 (same source cited in `goal-paths.md`, re-verified here).

- **Target conversion:** `convert-currency --amount 40000 --rate 3.037988`
  → 121,519.52 BYN. Matches `goal-paths.md`.
- **Path 1 required contribution:** `future-value --principal 0
  --contribution 30379.88 --annual-rate 0 --years 0.3333333333333333`
  (4 months) → 121,519.52 BYN, exactly matching the target. Confirms
  30,379.88 BYN/month is the correct required contribution.
- **Path 1 reality check:** `future-value --principal 0 --contribution 5463
  --annual-rate 0 --years 0.3333333333333333` → 21,852.00 BYN (≈7,193 USD at
  the same rate, ≈18% of 40,000 USD target). Matches `goal-paths.md`.
- **Path 2:** `future-value` at 22 months → 120,186.00 BYN (short by
  1,333.52 BYN); at 23 months → 125,649.00 BYN (exceeds target by 4,129.48
  BYN). Both match `goal-paths.md` exactly.
- **Path 3 low end (77,969.96 BYN, Edmunds sensitivity bound — [2026 Mazda
  CX-5 Value | Edmunds](https://www.edmunds.com/mazda/cx-5/2026/appraisal-value/),
  accessed 2026-08-18):** 14mo → 76,482.00 (short); 15mo → 81,945.00
  (clears). Matches.
- **Path 3 most-likely (98,099.00 BYN, av.by real anchor — [Mazda CX-5
  listings, cars.av.by](https://cars.av.by/mazda/cx-5), accessed
  2026-08-18):** 17mo → 92,871.00 (short); 18mo → 98,334.00 (clears).
  Matches.
- **Path 3 high end (115,188.35 BYN, Edmunds sensitivity bound, same source
  as low end above):** 21mo → 114,723.00 (short); 22mo → 120,186.00
  (clears). Matches.
- **Edmunds USD→BYN conversion check:** `convert-currency --amount 25665
  --rate 3.037988` → 77,969.96 BYN; `convert-currency --amount 37916 --rate
  3.037988` → 115,188.35 BYN (Edmunds USD figures per source above). Both
  match `goal-paths.md` exactly.
- **Minor discrepancy found (immaterial to any verdict):** `goal-paths.md`
  states the av.by anchor (98,099 BYN) is "≈32,291.54 USD-equivalent" at the
  3.037988 BYN/USD rate. Independent recomputation (98,099 ÷ 3.037988) gives
  **32,290.78 USD**, a ~0.76 USD (≈0.002%) rounding difference — likely from
  an inverse-rate rounding step in the original artifact rather than a
  different rate being used. This does not affect the BYN-denominated target,
  any timeline, or any verdict in this document, since all Path 3 accumulation
  math is done in BYN throughout; it is flagged here per the instruction not
  to silently pick one version without noting a disagreement.
- **Feasibility gap (Path 1):** 30,379.88 − 5,463 = 24,916.88 BYN/month
  short, i.e. required contribution is ~5.6× the 5,463 BYN/month disposable
  surplus confirmed in `cashflow.md`. Matches `goal-paths.md`.

## Ranking

1. **Path 2 (full target, extended ~23-month timeline)** — most recommended.
   It is the only path that preserves the user's originally stated
   requirement without modification (new car, full 40,000 USD / 121,519.52
   BYN budget, cash-only, no financing) — the sole change needed is the
   target date, from 31 Dec 2026 to ~late July 2028. The calculation is
   single-valued and fully verified (22 vs. 23 months bracketing the exact
   target), with no price-estimation uncertainty. Recommended as the primary
   path if the user is willing to move the date and is not willing to
   compromise on "new car."

2. **Path 3 (used car, ~15–22 months, ~18 most likely)** — recommended
   alternative if the user is open to a used car. It reaches a car
   significantly sooner than Path 2 (as much as 8 months sooner at the
   most-likely price point, and even the high-sensitivity case ties Path 2's
   22nd-month position while Path 2 needs a full 23rd month). Its grounding
   is now solid — a real, dated, sourced Belarus marketplace listing as the
   primary anchor, with a bounded, cross-checked sensitivity band rather than
   an unbounded foreign estimate — but it still changes a stated requirement
   (new → used) and carries residual price uncertainty that should be
   resolved with 2–3 concrete quotes before the user commits to a date.

3. **Path 1 (exact target, exact 31 Dec 2026 deadline)** — not achievable
   and not recommended. Retained in this assessment only to make explicit,
   with numbers, why the user's original stated timeline cannot be met from
   disposable surplus alone under the confirmed cash-only/no-financing
   constraints.

**Overall:** the user's exact original goal (new Mazda CX-5, 40,000 USD, by
31 Dec 2026, cash-only) is **not achievable**. A path to the goal exists in
two forms — extend the timeline and keep the full target (Path 2), or accept
a used car for a materially faster (though still delayed) timeline (Path 3)
— so the outcome is best characterized as **achievable with changes** to
either the deadline or the "new vs. used" requirement, not as a flat "not
achievable."
