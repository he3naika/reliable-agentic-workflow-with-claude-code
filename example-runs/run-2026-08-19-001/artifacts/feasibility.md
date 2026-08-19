# Feasibility Assessment — Target Passive Income

Goal: 2,000 EUR/month passive income by age 55 (20-year horizon, current age
35), moderate risk tolerance. Source artifacts: `requirements.md`,
`cashflow.md`, `market-data.md`, `goal-paths.md`.

All figures below were **independently recomputed** via
`finance-math-toolkit`'s `scripts/calc.py` (`required-capital`,
`future-value`, `convert-currency`), using each path's own stated inputs
(contribution, blended rate, timeline) rather than trusting the numbers as
written in `goal-paths.md`. Every recomputation matched `goal-paths.md`
exactly (see Supporting Calculation) — no discrepancies were found in this
run.

**External-figure sources used in the recomputation below** (restated from
`goal-paths.md`/`market-data.md` for traceability, not re-researched here):

- **Safe withdrawal rate = 4%** (source: William Bengen's 1994 SAFEMAX
  study; corroborated by Cooley, Hubbard & Walz, "Retirement Spending:
  Choosing a Sustainable Withdrawal Rate," AAII Journal, Feb 1998 — the
  "Trinity Study"; accessed via WebSearch 2026-08-19).
- **MSCI World Index (USD) equity return = 7.45%/yr** (source: MSCI World
  Index official factsheet,
  https://www.msci.com/documents/10199/255599/msci-world-index-usd-net.pdf,
  since-inception annualized 29 Dec 2000 – 31 Jul 2026, accessed
  2026-08-19).
- **iShares Core U.S. Aggregate Bond ETF (AGG) return = 3.15%/yr** (source:
  iShares AGG official fact sheet,
  https://www.ishares.com/us/literature/fact-sheet/agg-ishares-core-u-s-aggregate-bond-etf-fund-fact-sheet-en-us.pdf,
  since-inception NAV annualized 22 Sep 2003 – 30 Jun 2026, accessed
  2026-08-19).
- **PLN/EUR rate = 0.232153 EUR per PLN** (1 EUR = 4.3075 PLN) (source:
  Narodowy Bank Polski (NBP) official reference table 158/A/NBP/2026, 17 Aug
  2026, https://nbp.pl/statystyka-i-sprawozdawczosc/kursy/tabela-a/, accessed
  2026-08-19; cross-checked against Currency.Wiki, 18 Aug 2026,
  https://currency.wiki/pln-eur, accessed 2026-08-19).

## Affordability check (applies to all 4 paths)

- **Actual disposable surplus (per `cashflow.md`):** 2,083.71 PLN/month =
  **483.74 EUR/month** (converted at the NBP-sourced PLN/EUR rate above).
- **Required monthly contribution in every one of the 4 candidate paths:
  483.74 EUR/month** — i.e. **100% of the disposable surplus**, no more and
  no less.
- Because required contribution == actual surplus exactly, every path is
  affordable *today*, but with **zero margin**: no buffer for a bad month,
  an expense shock, or the unconfirmed tax/ZUS assumptions in `net-income.md`
  turning out less favorable. This is a cross-cutting risk, not a reason by
  itself to call any path "not achievable," but it should be disclosed to
  the user rather than silently assumed away.
- FX caveat carried forward from `goal-paths.md`/`cashflow.md`: the PLN/EUR
  rate is a single spot quote; Poland is not in the Eurozone, so all EUR
  figures over a 20-34 year horizon carry unmodeled FX risk.

## Per-Path Verdict

### Path 1 — Baseline 50/50, target age 55 → **NOT achievable**

Projected capital (239,295.64 EUR) covers only ~39.9% of the 600,000 EUR
required to sustain 2,000 EUR/month at a 4% SWR (source above). Shortfall:
360,704.36 EUR. The monthly contribution itself is affordable (equals full
surplus), but the combination of return (5.30%/yr blended, per the MSCI
World/AGG sources above), horizon (20 years), and contribution is
mathematically insufficient to reach the stated target by age 55.
**Verdict confirmed: not achievable as stated.**

### Path 2 — Same allocation, extended horizon to age 69 → **Achievable**

Extending the horizon from 20 to 34 years (same 483.74 EUR/month
contribution, same 5.30%/yr blended 50/50 return) reaches 621,849.50 EUR,
which clears the 600,000 EUR target. 33 years is not enough (584,176.85
EUR), confirming 34 years is the correct minimum at this contribution/rate.
**Verdict confirmed: achievable, but only by retiring 14 years later than
the requested age 55 (at age 69 instead)** — this is a real trade-off
against the user's stated target age, not a cost-free fix.

### Path 3 — Growth-tilted 70/30, horizon to age 66 → **Achievable, but exceeds stated risk tolerance**

Shifting to 70% equity / 30% bonds (6.16%/yr blended, per the same
MSCI World/AGG sources above) over 31 years reaches 616,762.90 EUR ≥
600,000 EUR required; 30 years falls short (574,392.46 EUR), confirming 31
years is the minimum at this allocation. Mathematically achievable with 11
fewer years of delay than Path 2. However, `requirements.md` states risk
tolerance as **moderate** and explicitly scopes recommendations away from
"full-equity aggressive." A 70/30 split is not full-equity, but it is more
aggressive than the 50/50 split used elsewhere as the moderate baseline, so
this path should not be presented as a drop-in moderate recommendation
without the user explicitly confirming they accept the higher equity
weighting — consistent with how `goal-paths.md` already flagged it.

### Path 4 — Reduced target income, original age 55 → **Achievable (different goal)**

Keeping the original 20-year horizon and the moderate 50/50 allocation
(same 239,295.64 EUR projected capital as Path 1), but lowering the target
passive income to 797 EUR/month (≈40% of the requested 2,000 EUR/month)
drops the required capital to 239,100 EUR (at the same 4% SWR) — just under
the projected 239,295.64 EUR (margin: +195.64 EUR). **Verdict confirmed:
achievable at the originally requested age and risk profile, but this
satisfies a materially smaller goal** (797 EUR/month, not 2,000 EUR/month)
— it resolves the timeline/risk constraints by changing the target itself,
which is a genuine lever but changes what "success" means relative to the
original ask.

## Supporting Calculation

All commands run against `.claude/skills/finance-math-toolkit/scripts/calc.py`
independently of `goal-paths.md`'s narrative; outputs are the actual script
output, not transcribed by hand. Rate/SWR inputs are the sourced figures
listed above.

```
$ python calc.py required-capital --target-monthly-income 2000 --swr 0.04
{"required_capital": 600000.0, "target_monthly_income": 2000.0,
 "target_annual_income": 24000.0, "safe_withdrawal_rate": 0.04}
→ matches goal-paths.md (600,000 EUR). CONFIRMED.

$ python calc.py convert-currency --amount 2083.71 --rate 0.232153
{"converted_amount": 483.74, "amount": 2083.71, "rate": 0.232153}
→ matches goal-paths.md (483.74 EUR/month surplus). CONFIRMED.

$ python calc.py convert-currency --amount 50000 --rate 0.232153
{"converted_amount": 11607.65, "amount": 50000.0, "rate": 0.232153}
→ matches goal-paths.md (11,607.65 EUR existing savings). CONFIRMED.

# Path 1: 20 years, 5.30% blended (50% x 7.45% MSCI World + 50% x 3.15% AGG,
# sources above)
$ python calc.py future-value --principal 11607.65 --contribution 483.74 \
    --annual-rate 0.053 --years 20
{"future_value": 239295.64, ...}
→ matches goal-paths.md (239,295.64 EUR). Shortfall vs 600,000 EUR required
  = 360,704.36 EUR (39.9% of target). CONFIRMED NOT achievable.

# Path 2: 34 years, same 5.30% blended rate
$ python calc.py future-value --principal 11607.65 --contribution 483.74 \
    --annual-rate 0.053 --years 34
{"future_value": 621849.50, ...}
→ matches goal-paths.md; ≥ 600,000 EUR required. CONFIRMED achievable.

$ python calc.py future-value --principal 11607.65 --contribution 483.74 \
    --annual-rate 0.053 --years 33
{"future_value": 584176.85, ...}
→ matches goal-paths.md's claim that 33 years is insufficient. CONFIRMED
  34 years is the correct minimum horizon at this rate/contribution.

# Path 3: 31 years, 6.16% blended (70% x 7.45% + 30% x 3.15%, sources above)
$ python calc.py future-value --principal 11607.65 --contribution 483.74 \
    --annual-rate 0.0616 --years 31
{"future_value": 616762.90, ...}
→ matches goal-paths.md; ≥ 600,000 EUR required. CONFIRMED achievable.

$ python calc.py future-value --principal 11607.65 --contribution 483.74 \
    --annual-rate 0.0616 --years 30
{"future_value": 574392.46, ...}
→ matches goal-paths.md's claim that 30 years is insufficient. CONFIRMED
  31 years is the correct minimum horizon at this allocation.

# Path 4: required capital for a reduced 797 EUR/month target, same 4% SWR
$ python calc.py required-capital --target-monthly-income 797 --swr 0.04
{"required_capital": 239100.0, "target_annual_income": 9564.0,
 "safe_withdrawal_rate": 0.04}
→ matches goal-paths.md (239,100 EUR). Path-1 projection (239,295.64 EUR)
  clears this by 195.64 EUR. CONFIRMED achievable.
```

**Result of independent recomputation: no discrepancies found.** Every
numeric claim in `goal-paths.md` (required capital, currency conversions,
and all four future-value projections, including the boundary-year checks)
reproduces exactly under `finance-math-toolkit`. Blended-rate arithmetic
(0.5×7.45%+0.5×3.15%=5.30%; 0.7×7.45%+0.3×3.15%=6.16%) also checks out.

## Ranking

Ranked most to least recommended, weighing (a) how closely each path
matches the user's stated constraints — target age 55, target income 2,000
EUR/month, moderate risk tolerance — against (b) mathematical feasibility:

1. **Path 3 (growth-tilted 70/30, age 66)** — achievable, and the smallest
   deviation from the user's stated preferences among the paths that keep
   the full 2,000 EUR/month target: only 11 years later than requested,
   versus 14 for Path 2. Recommended **conditional on the user explicitly
   confirming** they accept a 70/30 allocation, since it is more
   equity-heavy than the 50/50 "moderate" baseline used elsewhere — this
   should be surfaced as a question, not assumed.
2. **Path 2 (moderate 50/50, age 69)** — achievable and stays strictly
   within the user's stated moderate risk tolerance, but delays retirement
   by 14 years, the largest deviation from the stated target age of any
   achievable path. Recommended as the "no risk-profile change" fallback if
   the user declines Path 3's higher equity weighting.
3. **Path 4 (reduced target, age 55)** — achievable and matches both the
   original target age and the moderate risk tolerance exactly, but only by
   accepting a materially smaller passive income (≈797 EUR/month, ~40% of
   the original 2,000 EUR/month ask). Useful if the user's target age is
   the least negotiable constraint, but changes the goal itself rather than
   the path to it.
4. **Path 1 (baseline 50/50, age 55, full 2,000 EUR/month target)** — **not
   achievable** under any combination of the stated contribution, moderate
   allocation, and 20-year horizon; included only as the baseline showing
   why a lever (horizon, allocation, or target) must change. Not
   recommendable as-is.

All rankings assume the 483.74 EUR/month contribution (100% of current
disposable surplus) is sustained without interruption for the full
projection horizon of the chosen path, and that the single-point-in-time
PLN/EUR rate and unconfirmed net-income assumptions (flagged in
`cashflow.md`/`net-income.md`) do not materially change. The "higher
contribution via income increase" lever remains unmodeled, as
`goal-paths.md` notes, because no concrete income-increase figure was
provided by the user.
