# Feasibility Assessment — run-2026-08-18-003

## Scope & Method

All figures below were **independently recomputed** with
`finance-math-toolkit` (`scripts/calc.py`), using each path's own stated
inputs (principal, monthly contribution, annual rate, years / SWR) as
written in `artifacts/goal-paths.md` — not copied from that artifact's
prose. Recomputation results are shown in "Supporting Calculation" below.

**Result of independent recomputation: every numeric figure in
`goal-paths.md` (currency conversions, both required-capital figures, and
all four future-value projections) matches the independently recomputed
value exactly (to the cent).** No arithmetic errors were found. The
findings below are therefore about the reasonableness/consistency of the
*assumptions* feeding those correct calculations, not about calculation
errors.

Disposable monthly surplus, per `artifacts/cashflow.md`: **25,000.00
PLN/month = 5,787.25 EUR/month** (full net income, no expenses deducted, by
explicit user instruction), plus an existing lump sum of **200,000.00
PLN = 46,298.00 EUR** (currently uninvested cash). Conversion rate used:
1 PLN = 0.23149 EUR ([Wise — PLN to EUR currency converter](https://wise.com/us/currency-converter/pln-to-eur-rate/history), accessed 2026-08-18) — independently reproduced below.

## Per-Path Verdict

### Path 1 — Full Commitment, AOM 40/60 Balanced (primary return 5.90%)
**Verdict: ACHIEVABLE, with substantial margin.**
- Required contribution (5,787.25 EUR/month) **equals** the actual
  disposable surplus (5,787.25 EUR/month) — no affordability gap.
- Projected capital at age 50 (1,026,681.71 EUR) exceeds the primary,
  horizon-adjusted required capital (685,714.29 EUR at 3.5% SWR) by
  +340,967.42 EUR (+49.7%), and exceeds even the classic 600,000.00 EUR
  (4% SWR) target by +426,681.71 EUR (+71.1%).
- Margin is large enough to comfortably absorb the un-modeled Belka
  (capital-gains) tax and some inflation erosion (see Caveats) without
  flipping the verdict.

### Path 2 — Downside Stress-Test, Lower Moderate Return (5.64%)
**Verdict: ACHIEVABLE.**
- Same contribution as Path 1 (fully affordable, no gap).
- Projected capital at age 50 (1,011,377.63 EUR) exceeds the primary
  required capital (685,714.29 EUR) by +325,663.34 EUR (+47.5%).
- Confirms Path 1's result is not fragile to the exact CAGR chosen within
  AOM's own reported 10Y/15Y range (5.90% vs. 5.64%) — a genuinely useful
  sensitivity check, correctly computed.

### Path 3 — Growth-Tilted Moderate, Custom 60/40 SPY/AGG Blend (9.96%)
**Verdict: ACHIEVABLE, largest nominal margin — but flagged as the least
reliable return assumption of the four paths.**
- Same contribution as Path 1 (fully affordable, no gap).
- Projected capital at age 50 (1,307,611.58 EUR) exceeds the primary
  required capital (685,714.29 EUR) by +621,897.29 EUR (+90.7%).
- Blend arithmetic re-verified: 0.60 × 15.58% + 0.40 × 1.52% = 9.348% +
  0.608% = **9.956% ≈ 9.96%** — correct. (SPY/AGG 10-year CAGR figures per
  [market-data.md](./market-data.md), sourced from financecharts.com, accessed
  2026-08-18.)
- **However, two assumption-quality issues make this path's margin less
  trustworthy than Path 1/2's, independent of the arithmetic being right:**
  1. **Return-assumption inconsistency across paths.** Paths 1/2 use
     AOM's own reported CAGR for an actual pre-blended 40/60 fund. Path 3
     instead hand-blends two *separate* funds' trailing CAGRs as a simple
     weighted average. A weighted average of two instruments' independent
     CAGRs is not the same figure as the CAGR of a portfolio that actually
     holds and rebalances both — it ignores rebalancing effects and
     (for a stock/bond mix) generally *overstates* the real blended return
     versus a true rebalanced-portfolio CAGR. This is a real methodological
     gap, not just a labeling nuance.
  2. **The 10-year SPY figure driving the blend (15.58%, per
     [market-data.md](./market-data.md)) reflects an unusually strong recent
     bull-market window**, well above SPY's own 15-year CAGR (14.15%, same
     source). Using the single most favorable trailing window as the
     forward assumption for a "moderate" risk path is optimistic, and the
     resulting 9.96% blended return should not be treated as equally
     credible as AOM's 5.90%/5.64% figures, which the market-data artifact
     itself recommends as the primary moderate-risk proxy.
  - Net effect: Path 3's achievability is not in doubt given the size of
    its margin (it would still clear the 685,714.29 EUR bar even at a
    meaningfully lower blended return — see sensitivity below), but its
    stated margin size should be treated as an upper bound, not the
    expected case, and it carries materially higher equity-concentration
    volatility than Path 1.
  - Sensitivity: solving backward, Path 3 only needs a blended CAGR high
    enough to clear 685,714.29 EUR; even AOM's own 5.90% (Path 1's rate)
    applied to the identical contribution schedule already clears the bar
    by +49.7%, so Path 3's extra margin over Path 1 is a genuine (if
    optimistic) upside case, not a load-bearing requirement for
    achievability.

### Path 4 — Partial Commitment (60% of monthly surplus, 3,472.35 EUR/month)
**Verdict: NOT ACHIEVABLE under the primary SWR; marginal at best.**
- Contribution used (3,472.35 EUR/month) is **below** the actual
  disposable surplus (5,787.25 EUR/month) by design — this path is a
  stress test of under-investing, not a cashflow-affordability problem
  (the user can afford more; this path assumes they choose not to invest
  it).
- Projected capital at age 50 (649,369.18 EUR) is **below** the primary
  required capital (685,714.29 EUR at 3.5% SWR) by −36,345.11 EUR
  (−5.3%) → **shortfall, not achievable** under the SWR this plan treats
  as primary.
- Only clears the bar under the classic 4% SWR (600,000.00 EUR required),
  by +49,369.18 EUR (+8.2%) — and per the SWR discussion below, 4% is the
  less-appropriate rate for this user's actual horizon, not the more
  appropriate one.
- **Verdict stands as "not achievable" against the primary, more
  defensible SWR.** This path exists correctly to show that the comfort
  margin in Paths 1–3 depends on the user actually investing the full
  stated surplus.

## Supporting Calculation

All commands run via `finance-math-toolkit` (`scripts/calc.py`),
independently, with each path's own stated inputs:

| Check | Command | Recomputed result | Matches goal-paths.md? |
|---|---|---|---|
| PLN→EUR, monthly surplus | `convert-currency --amount 25000 --rate 0.23149` | 5,787.25 EUR | Yes |
| PLN→EUR, lump sum | `convert-currency --amount 200000 --rate 0.23149` | 46,298.00 EUR | Yes |
| PLN→EUR, Path 4 contribution | `convert-currency --amount 15000 --rate 0.23149` | 3,472.35 EUR | Yes |
| Required capital, 3.5% SWR (primary) | `required-capital --target-monthly-income 2000 --swr 0.035` | 685,714.29 EUR | Yes |
| Required capital, 4% SWR (reference) | `required-capital --target-monthly-income 2000 --swr 0.04` | 600,000.00 EUR | Yes |
| Path 1 FV | `future-value --principal 46298 --contribution 5787.25 --annual-rate 0.059 --years 10` | 1,026,681.71 EUR | Yes |
| Path 2 FV | `future-value --principal 46298 --contribution 5787.25 --annual-rate 0.0564 --years 10` | 1,011,377.63 EUR | Yes |
| Path 3 FV | `future-value --principal 46298 --contribution 5787.25 --annual-rate 0.0996 --years 10` | 1,307,611.58 EUR | Yes |
| Path 4 FV | `future-value --principal 46298 --contribution 3472.35 --annual-rate 0.059 --years 10` | 649,369.18 EUR | Yes |
| Path 3 blend weighting (manual, flagged for re-check) | 0.60 × 15.58% + 0.40 × 1.52% | 9.956% ≈ 9.96% | Yes |

**Margin/shortfall arithmetic (surplus or shortfall = projected capital −
required capital at 3.5% SWR of 685,714.29 EUR):**
- Path 1: 1,026,681.71 − 685,714.29 = **+340,967.42** (+49.7%)
- Path 2: 1,011,377.63 − 685,714.29 = **+325,663.34** (+47.5%)
- Path 3: 1,307,611.58 − 685,714.29 = **+621,897.29** (+90.7%)
- Path 4: 649,369.18 − 685,714.29 = **−36,345.11** (−5.3%, shortfall)

All four margin/shortfall figures independently recompute to the same
values stated in `goal-paths.md`.

### Cashflow feasibility (affordability of the *contribution itself*)

- Paths 1–3 require 5,787.25 EUR/month, which is **exactly** the
  confirmed disposable surplus per `cashflow.md` — fully affordable, with
  zero slack. There is no cushion in the monthly contribution itself if
  the "separate expense budget" the user described turns out not to be
  fully separate in practice.
- Path 4 requires only 3,472.35 EUR/month — well within capacity — so it
  is trivially affordable; its problem is projected-outcome shortfall
  against the goal, not affordability.

### SWR choice — reasonableness given the accumulation-vs-decumulation horizon mismatch

`goal-paths.md` correctly identifies that retiring at age 50 implies a
long decumulation horizon (roughly 35–45+ years to age 85–95) and, on that
basis, adopts **3.5%** as the primary SWR rather than the classic **4%**,
citing early/long-retirement-adjusted guidance
([The Poor Swiss — Updated Trinity Study For 2026](https://thepoorswiss.com/updated-trinity-study/);
[Retirement Researcher — Safe Withdrawal Rates for Retirement and the
Trinity Study](https://retirementresearcher.com/safe-withdrawal-rates-for-retirement-and-the-trinity-study/),
both accessed 2026-08-18). This reasoning is sound as far as it goes, but
two things should be flagged explicitly for the record:

1. **The decumulation horizon (35–45+ years) is an assumption, not a
   user-confirmed input.** `requirements.md` states the accumulation
   horizon (age 40 → 50) but nowhere records the user's expected
   retirement duration, life expectancy assumption, or whether the
   2,000 EUR/month target is meant to run for a fixed period or
   indefinitely. Using ~35–45 years is a reasonable default but is an
   assumption manufactured downstream, not something the user confirmed —
   `financial-auditor`/`plan-builder` should either get this confirmed or
   carry it forward explicitly as an assumption in the final plan.
2. **The classic 4%-rule research (Bengen 1994; Trinity Study, both cited
   above) is itself calibrated to a ~30-year retirement horizon, and the
   3.5% figure used here comes from secondary commentary extrapolating
   that research to longer horizons, not from an independently-run
   40+-year Monte Carlo/historical simulation.** This is the right
   directional adjustment (lower SWR for a longer horizon) and is properly
   sourced with citations and access dates, but the underlying data
   backing a "safe" rate for a 45-year horizon specifically is thinner
   than the 30-year case (fewer non-overlapping historical periods exist
   to test against). This does not invalidate 3.5% as a reasonable,
   appropriately conservative planning figure — if anything it argues for
   *not* leaning on the less-conservative 4% figure to rescue Path 4's
   verdict, which is exactly how the assessment above treats it.

Neither issue changes any of the four verdicts above; they are recorded so
`financial-auditor`/`plan-builder` do not present the 3.5%/685,714.29 EUR
figure as more precisely validated than it actually is.

### Other consistency notes (do not change verdicts, but relevant to overall confidence)

- **Belka tax / capital-gains tax on withdrawals is not modeled** (flagged
  already in `goal-paths.md`, § Assumptions & Sources, item 7). No specific
  rate is asserted here since this artifact set does not carry a cited
  source + access date for it (raising one would require research beyond
  this artifact's scope) — but any nonzero capital-gains tax would reduce
  the real sustainable withdrawal somewhat below the pre-tax required-capital
  figures used throughout. Paths 1–3's margins (47–91%) are large enough to
  comfortably absorb a realistic capital-gains tax haircut on gains under
  any plausible rate; Path 4, already short before this adjustment, would
  only fall further behind. If the final plan needs a precise post-tax
  figure, the actual Belka tax rate (and any IKE/IKZE tax-advantaged-account
  exemption the user may be eligible for) should be researched and cited
  before that number is presented to the user.
- **Inflation is not modeled on either side of the ledger** (also flagged
  in `goal-paths.md`, § Assumptions & Sources, item 3) — the 2,000
  EUR/month target is treated as already expressed in "today's terms"
  while the projected accumulation is a nominal (not inflation-adjusted)
  future-value figure. If the user's intent is 2,000 EUR/month of
  *today's* purchasing power at age 50 (i.e., a real, inflation-adjusted
  target), the comparison implicitly assumes ~0% inflation over the
  horizon, which is optimistic. This does not flip any verdict here given
  the size of the margins in Paths 1–3, but should be disclosed in the
  final plan rather than silently assumed.
- **Return-assumption consistency across paths**: Paths 1, 2, and 4 all
  correctly reuse AOM's own reported CAGR figures (per `market-data.md`)
  for a real pre-blended fund. Path 3's hand-built 60/40 blend from two
  separate instruments' CAGRs is the one internally inconsistent
  methodology in the set (see Path 3 verdict above) — it is
  mathematically executed correctly but rests on a less defensible return
  assumption than the other three paths.

## Ranking

1. **Path 1 — Full Commitment, AOM 40/60 Balanced (5.90%).** Most
   recommended. Achievable with a large (+49.7%) margin against the
   conservative, horizon-appropriate SWR; uses a real, single
   diversified moderate-allocation instrument (no synthetic blend); the
   contribution required matches the user's actual full stated surplus
   exactly, so it directly reflects the user's stated willingness to
   invest the full amount. Best balance of feasibility, methodological
   soundness, and fit to the user's "moderate" risk tolerance.
2. **Path 2 — Downside Stress-Test (5.64%).** Second — not a distinct
   allocation choice but a robustness check on Path 1 using the same
   instrument's own lower historical CAGR. Still comfortably achievable
   (+47.5%), and its main value is confirming Path 1 isn't a fragile,
   single-assumption result. Recommended to present alongside Path 1
   as evidence of the plan's robustness, not as a separate path to choose.
3. **Path 3 — Growth-Tilted 60/40 Blend (9.96%).** Third — achievable
   with the largest nominal margin, but ranked below Paths 1/2 because
   (a) its return assumption is the least methodologically sound (a
   hand-averaged blend of two funds' CAGRs, one of which reflects an
   unusually strong recent equity bull run, rather than one real
   instrument's own reported blended return), and (b) it carries more
   equity-concentration volatility than the user's stated moderate
   tolerance implies, per `market-data.md`/`goal-paths.md`'s own framing.
   Worth offering only if the user, after seeing this caveat, explicitly
   confirms comfort tilting toward the growth end of "moderate."
4. **Path 4 — Partial Commitment (60% of surplus).** Least recommended,
   and not achievable against the primary SWR (−5.3% shortfall). Its
   purpose is diagnostic (showing how much slack exists in Paths 1–3),
   not a recommendation to actually under-invest — if presented to the
   user at all, it should be framed strictly as "here is the downside if
   you don't invest the full stated surplus," not as a viable path to the
   stated goal.

**Overall:** the goal (2,000 EUR/month passive income by age 50) is
**achievable**, provided the user invests the full stated 25,000 PLN/month
surplus (Paths 1–3 all clear the conservative 685,714.29 EUR bar with
40–90% margin). It is **not achievable** on the primary SWR if the user
only invests 60% of that surplus (Path 4). Recommended path: Path 1.
