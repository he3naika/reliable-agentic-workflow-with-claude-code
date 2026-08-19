# Audit Report — run-2026-08-19-001

Goal type: `retirement_income` (target passive income by target age). Debt-specific
gate (9) is not applicable to this run.

## Artifact-validator structural/citation pass

- `requirements.md`: PASS — all required sections present (Goal Type, Target
  Parameters, Current Position, Constraints, Confirmed); no external figures
  requiring citation (all user-stated).
- `net-income.md`: PASS — all required sections present (Gross Income,
  Jurisdiction & Contract Type, Taxes/Contributions, Net Income, Sources);
  every rate (ZUS components, health contribution, ryczałt 12%) carries a
  `(source: ..., accessed 2026-08-19)` citation.
- `market-data.md`: PASS — all required sections present (Benchmarks Used,
  Historical Return, Period, Source & Date Accessed); both headline figures
  (MSCI World 7.45%, AGG 3.15%) and the supplementary 12.73% figure are cited
  with source + access date; tier attempts (1/2/3) transparently logged.
- `cashflow.md`: PASS — all required sections present (Net Income, Expenses
  Breakdown, Disposable Surplus, Flags).
- `goal-paths.md`: PASS — all required sections present (Goal Summary, ≥2
  Candidate Paths each with target/contribution/instruments/timeline,
  Assumptions & Sources); 4 candidate paths, each fully specified.
- `feasibility.md`: PASS — all required sections present (Per-Path Verdict,
  Supporting Calculation, Ranking).

## Independent recomputation via `finance-math-toolkit` (financial-auditor's own run, not trusting goal-paths.md/feasibility.md prose)

All commands re-run independently against
`.claude/skills/finance-math-toolkit/scripts/calc.py` with the same inputs
the artifacts claim to use:

| Calculation | Artifact claim | Independent recomputation | Match |
|---|---|---|---|
| `required-capital --target-monthly-income 2000 --swr 0.04` | 600,000 EUR | 600,000.0 EUR | ✅ |
| `convert-currency --amount 2083.71 --rate 0.232153` | 483.74 EUR | 483.74 EUR | ✅ |
| `convert-currency --amount 50000 --rate 0.232153` | 11,607.65 EUR | 11,607.65 EUR | ✅ |
| `future-value` Path 1 (20y, 5.30%, principal 11,607.65, contrib 483.74) | 239,295.64 EUR | 239,295.64 EUR | ✅ |
| `future-value` Path 2 (34y, 5.30%, same principal/contrib) | 621,849.50 EUR | 621,849.5 EUR | ✅ |
| `future-value` Path 2 boundary (33y, 5.30%) | 584,176.85 EUR (insufficient) | 584,176.85 EUR | ✅ |
| `future-value` Path 3 (31y, 6.16%, same principal/contrib) | 616,762.90 EUR | 616,762.9 EUR | ✅ |
| `future-value` Path 3 boundary (30y, 6.16%) | 574,392.46 EUR (insufficient) | 574,392.46 EUR | ✅ |
| `required-capital --target-monthly-income 797 --swr 0.04` (Path 4) | 239,100 EUR | 239,100.0 EUR | ✅ |

Blended-rate arithmetic independently checked: 0.5×7.45 + 0.5×3.15 = 5.30
(Paths 1/2/4); 0.7×7.45 + 0.3×3.15 = 6.16 (Path 3). Both correct.

Net-income arithmetic independently re-derived from `net-income.md`'s own
stated inputs: ZUS total 1,103.27+452.16+138.47+94.39+138.47 = 1,926.76;
taxable base 12,000.00−1,926.76−415.29 = 9,657.95; tax 12%×9,657.95 =
1,158.95 (rounded); net = 12,000.00−1,926.76−830.58−1,158.95 = 8,083.71. All
reproduce exactly. `cashflow.md`'s disposable surplus 8,083.71−6,000.00 =
2,083.71 also reproduces exactly and matches `net-income.md`.

**No discrepancy beyond rounding found anywhere in `goal-paths.md` or
`feasibility.md`.**

## Gate Results

1. **All 5 required output fields derivable per path — PASS.** Each of the 4
   paths in `goal-paths.md`/`feasibility.md` states target capital, monthly
   contribution, allocation/instruments (SWDA/URTH + AGG or EUR-hedged
   equivalent), timeline, and verdict.
2. **Verdict mathematically consistent (independently recomputed) — PASS.**
   See recomputation table above; every figure in `goal-paths.md` and
   `feasibility.md` reproduces exactly via `finance-math-toolkit`, including
   the boundary-year checks (33y/30y) that confirm the stated minimum
   horizons.
3. **Net income accounts for every tax/contribution stated — PASS, with
   advisory note attributed to `income-tax-modeler`.** The user did not
   state a tax regime or ZUS-relief eligibility in `requirements.md`;
   `net-income.md` fills this gap with a sourced, statutory default (ryczałt
   12%, standard "duży ZUS") and explicitly flags both as unconfirmed
   assumptions with a caveats section, rather than fabricating or silently
   assuming them. This satisfies the no-fabrication rule but is a genuine
   open item — recommend `requirements-formalizer` ask the user to confirm
   tax regime election and business tenure on a future run/revision, since
   net income (and everything downstream) would change materially under
   podatek liniowy or skala podatkowa.
4. **Every external figure has a real cited source + access date — PASS.**
   Checked in the artifact-validator pass above across all 6 artifacts; spot
   ZUS/health/tax rates, SWR, MSCI World/AGG returns, and the NBP PLN/EUR
   rate are all cited with source + `accessed 2026-08-19`.
5. **At least 2 candidate paths — PASS.** 4 paths present in `goal-paths.md`.
6. **No vague recommendations — PASS.** Every path names concrete
   instruments (iShares Core MSCI World UCITS ETF SWDA/URTH, iShares Core
   U.S. Aggregate Bond ETF AGG or EUR-hedged equivalent), concrete
   allocations (50/50, 70/30), concrete amounts, and concrete timelines
   (years/target age).
7. **Currency consistency; conversions explicit — PASS.** PLN used
   consistently through `requirements.md`/`net-income.md`/`cashflow.md`;
   `cashflow.md` explicitly flags the PLN/EUR gap rather than silently
   converting; `goal-paths.md` then resolves it with a sourced NBP rate
   (1 EUR = 4.3075 PLN, cross-checked against Currency.Wiki) and shows the
   conversion command output. `feasibility.md` reuses the same rate
   consistently. No silent or inconsistent currency handling found.
8. **Every confirmed requirement/constraint reflected downstream — PASS.**
   Target income (2,000 EUR/month), target age (55)/horizon (20y), moderate
   risk tolerance, index-fund preference, and the PLN/EUR mixed-currency
   constraint are all addressed in `goal-paths.md`/`feasibility.md`; the
   moderate-risk constraint is specifically honored by treating Path 3
   (70/30) as conditional on explicit user confirmation rather than a
   default recommendation, consistent with `requirements.md`'s Constraints
   section. The unbroken-out expense figure is carried forward as a flagged
   (non-blocking) data-quality note, not silently dropped.
9. **Loan terms sourced or user-confirmed — N/A.** This is a
   `retirement_income` run, not `debt_payoff`; no loan terms are involved.

## Overall

All applicable gates PASS. One advisory (non-blocking) finding attributed to
`income-tax-modeler`/`requirements-formalizer`: the tax regime (ryczałt vs.
podatek liniowy vs. skala podatkowa) and ZUS start-up relief eligibility are
assumptions, not user-confirmed facts — already transparently flagged in
`net-income.md`, `cashflow.md`, and carried forward through `goal-paths.md`.
Does not block progression to `plan-builder`, but should be surfaced to the
user for confirmation before or alongside final approval.
