# Audit Report — run-2026-08-18-003 (re-audit)

Re-audit performed after `feasibility.md`'s "Other consistency notes" section
was corrected to remove the previously-flagged uncited "~19% haircut" Belka
capital-gains-tax figure. Full re-pass over all 9 CLAUDE.md gates across all
six upstream artifacts (`requirements.md`, `net-income.md`, `market-data.md`,
`cashflow.md`, `goal-paths.md`, `feasibility.md`), including independent
recomputation of every numeric claim via `finance-math-toolkit` (redone from
scratch, not trusting the prior audit-report.md's figures).

## Independent Recomputation Log (finance-math-toolkit)

| Check | Command | Toolkit result | Artifact-stated result | Match? |
|---|---|---|---|---|
| PLN→EUR, monthly surplus | `convert-currency --amount 25000 --rate 0.23149` | 5,787.25 EUR | 5,787.25 EUR | Yes |
| PLN→EUR, lump sum | `convert-currency --amount 200000 --rate 0.23149` | 46,298.00 EUR | 46,298.00 EUR | Yes |
| PLN→EUR, Path 4 contribution | `convert-currency --amount 15000 --rate 0.23149` | 3,472.35 EUR | 3,472.35 EUR | Yes |
| Required capital, 3.5% SWR | `required-capital --target-monthly-income 2000 --swr 0.035` | 685,714.29 EUR | 685,714.29 EUR | Yes |
| Required capital, 4.0% SWR | `required-capital --target-monthly-income 2000 --swr 0.04` | 600,000.00 EUR | 600,000.00 EUR | Yes |
| Path 1 FV | `future-value --principal 46298 --contribution 5787.25 --annual-rate 0.059 --years 10` | 1,026,681.71 EUR | 1,026,681.71 EUR | Yes |
| Path 2 FV | `future-value --principal 46298 --contribution 5787.25 --annual-rate 0.0564 --years 10` | 1,011,377.63 EUR | 1,011,377.63 EUR | Yes |
| Path 3 FV | `future-value --principal 46298 --contribution 5787.25 --annual-rate 0.0996 --years 10` | 1,307,611.58 EUR | 1,307,611.58 EUR | Yes |
| Path 4 FV | `future-value --principal 46298 --contribution 3472.35 --annual-rate 0.059 --years 10` | 649,369.18 EUR | 649,369.18 EUR | Yes |
| Path 3 blend weighting (manual) | 0.60 × 15.58% + 0.40 × 1.52% | 9.956% ≈ 9.96% | 9.96% | Yes |
| Path 1 margin vs 3.5% SWR | 1,026,681.71 − 685,714.29 | +340,967.42 (+49.7%) | +340,967.42 (+49.7%) | Yes |
| Path 2 margin vs 3.5% SWR | 1,011,377.63 − 685,714.29 | +325,663.34 (+47.5%) | +325,663.34 (+47.5%) | Yes |
| Path 3 margin vs 3.5% SWR | 1,307,611.58 − 685,714.29 | +621,897.29 (+90.7%) | +621,897.29 (+90.7%) | Yes |
| Path 4 shortfall vs 3.5% SWR | 649,369.18 − 685,714.29 | −36,345.11 (−5.3%) | −36,345.11 (−5.3%) | Yes |
| Path 1 margin vs 4.0% SWR (ref) | 1,026,681.71 − 600,000.00 | +426,681.71 (+71.1%) | +426,681.71 (+71.1%) | Yes |
| Path 4 margin vs 4.0% SWR (ref) | 649,369.18 − 600,000.00 | +49,369.18 (+8.2%) | +49,369.18 (+8.2%) | Yes |

No mismatch found beyond exact-match precision. All numeric claims in
`goal-paths.md` and `feasibility.md` recompute identically.

## Gate Results

1. **All 5 required output fields present for every path — PASS.** Each of
   the 4 candidate paths in `goal-paths.md`/`feasibility.md` states target
   capital (685,714.29 EUR primary / 600,000.00 EUR reference), monthly
   contribution (5,787.25 EUR for Paths 1-3, 3,472.35 EUR for Path 4),
   concrete instruments (AOM 40/60 balanced fund; SPY/AGG for Path 3's
   blend), a 10-year timeline, and a reasoned verdict.
2. **Verdict mathematically consistent, independently recomputed — PASS.**
   See recomputation log above — every currency conversion, required-capital
   figure, future-value projection, margin/shortfall figure, and the Path 3
   blend weighting reproduce exactly against `finance-math-toolkit`.
3. **Net income accounts for every tax/contribution stated — PASS.**
   `net-income.md` documents ZUS (1,926.76 PLN/month, cited), the
   ryczałt-specific health-contribution bracket (1,495.04 PLN/month for
   >300,000 PLN/year revenue, cited), and the ryczałt PIT mechanism (rate
   depends on PKWiU classification, appropriately caveated as unconfirmed
   but not needed since the user directly confirmed the net figure already
   nets out all of these). `cashflow.md` correctly carries this net figure
   forward unchanged.
4. **Every external figure has a real cited source + access date — PASS
   (previously FAIL, now fixed).** Re-verified: `feasibility.md`'s "Other
   consistency notes" section no longer asserts a specific Belka-tax
   percentage. It now explicitly states no rate is asserted because no
   cited source is available, describes the qualitative direction of the
   effect (a real haircut, absorbed by Paths 1-3's 47-91% margins under
   "any plausible rate"), and defers a precise figure to future research —
   this is a correct, honest treatment, not a fabricated number. Checked
   all other external figures across all six artifacts: ryczałt rate
   schedule, ZUS amount, health-contribution brackets (net-income.md);
   SPY/AGG/AOM CAGRs, Bloomberg Agg long-run figure (market-data.md);
   PLN→EUR rate, SWR figures 3.5%/4.0% (goal-paths.md) — all carry a real
   source link/name and an access date (2026-08-18).
5. **At least 2 candidate paths — PASS.** 4 paths present in `goal-paths.md`.
6. **No vague recommendations — PASS.** Every path specifies concrete
   amounts (EUR figures to the cent), concrete instruments (AOM; SPY/AGG
   blend), and a concrete 10-year timeline; no generic "invest wisely"
   language found.
7. **Currency consistency; conversions explicit — PASS.** PLN is used
   consistently upstream (`requirements.md`, `net-income.md`, `cashflow.md`);
   `goal-paths.md` performs an explicit, cited PLN→EUR conversion via
   `finance-math-toolkit` before any EUR figure is used, and `feasibility.md`
   reproduces the same rate and figures without re-deriving a new one.
8. **Every confirmed requirement/constraint reflected downstream — PASS.**
   Target monthly income (2,000 EUR), target age (50), risk tolerance
   (moderate → AOM 40/60 primary, Path 3 explicitly flagged as
   growth-tilted/outside the core moderate proxy), existing 200,000 PLN lump
   sum, the "full 25,000 PLN/month available, expenses separate" basis, the
   ryczałt tax-form correction, and the required PLN→EUR conversion are all
   traceable through `net-income.md` → `cashflow.md` → `goal-paths.md` →
   `feasibility.md`. `income-tax-modeler` and `market-data-fetcher` both ran
   as required by `requirements.md`'s constraint for retirement_income goals.
9. **Loan terms sourced or user-confirmed — N/A.** This is a
   `retirement_income` run, not `debt_payoff`; no loan-terms gate applies.

## Overall Result

**PASS** — all 9 applicable gates pass (gate 9 not applicable to this goal
type). The prior gate-4 failure (uncited Belka-tax haircut, attributed to
`feasibility-assessor`) is confirmed resolved: the artifact now correctly
withholds an unsourced number rather than presenting a fabricated one.
