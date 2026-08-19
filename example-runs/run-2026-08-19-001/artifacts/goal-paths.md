# Goal Paths — Target Passive Income

## Goal Summary

- **Goal type:** `retirement_income` — target passive income by a target age.
- **Target passive income:** 2,000 EUR/month.
- **Target age:** 55 (current age 35 → 20-year horizon).
- **Risk tolerance:** moderate.
- **Existing savings:** 50,000 PLN → converted to EUR below.
- **Disposable monthly surplus:** 2,083.71 PLN/month (per `cashflow.md`) → converted to EUR below.

### Required capital (Stage 1)

Computed via `finance-math-toolkit`'s `required-capital` command:

```
python scripts/calc.py required-capital --target-monthly-income 2000 --swr 0.04
→ {"required_capital": 600000.0, "target_annual_income": 24000.0, "safe_withdrawal_rate": 0.04}
```

**Required capital: 600,000 EUR**, using a **4% safe withdrawal rate (SWR)**.

**SWR source (source: Bengen 1994 SAFEMAX study; Cooley, Hubbard & Walz,
"Retirement Spending: Choosing a Sustainable Withdrawal Rate," AAII
Journal, Feb 1998 — the "Trinity Study"; accessed via WebSearch 2026-08-19):**
the "4% rule" originates from William Bengen's 1994 SAFEMAX study and was
corroborated by the Trinity Study, which found a 4% inflation-adjusted
withdrawal rate achieved a 95% historical success rate over 30-year
retirement horizons with a 50/50 stock/bond portfolio (98% with 75%
stocks). This is the standard, widely-cited baseline SWR assumption in the
retirement-planning literature; a more conservative planner could use
3.5–3.7% (recent Morningstar downgrade) or a more optimistic one 4.7%
(Bengen's own 2024/2025 revision), but 4% is used here as the standard,
citable middle assumption.

### Currency conversion (resolving the PLN/EUR gap flagged by `cashflow.md`)

`cashflow.md` correctly flagged that no artifact upstream provided a sourced
PLN/EUR rate. Resolved here via WebSearch (a live spot/reference rate, not
domain-specific research requiring escalation):

- **Source:** Narodowy Bank Polski (NBP), official reference table No.
  158/A/NBP/2026 (17 Aug 2026): **1 EUR = 4.3075 PLN**
  (source: https://nbp.pl/statystyka-i-sprawozdawczosc/kursy/tabela-a/,
  accessed 2026-08-19). Cross-checked against Currency.Wiki's 18 Aug 2026
  quote of 1 PLN ≈ 0.2318 EUR (source: https://currency.wiki/pln-eur,
  accessed 2026-08-19), which is consistent with the NBP figure (reciprocal
  ≈ 0.23215).
- **Rate used:** 1 PLN = 1 / 4.3075 = **0.232153 EUR** (source: NBP table
  158/A/NBP/2026, accessed 2026-08-19).

Conversions via `finance-math-toolkit`'s `convert-currency` command:

```
python scripts/calc.py convert-currency --amount 2083.71 --rate 0.232153
→ {"converted_amount": 483.74}

python scripts/calc.py convert-currency --amount 50000 --rate 0.232153
→ {"converted_amount": 11607.65}
```

- **Disposable monthly surplus: 483.74 EUR/month** (from 2,083.71 PLN/month).
- **Existing savings: 11,607.65 EUR** (from 50,000 PLN).

**Caveat:** this is a single point-in-time spot rate. Over a 20–34 year
horizon, PLN/EUR will move (Poland is not in the Eurozone; no fixed peg
exists), so all EUR figures below carry FX risk not modeled by the toolkit.
Flagged for `feasibility-assessor` / `financial-auditor`.

## Candidate Paths (Stage 2 — projection of surplus vs. required capital)

All paths project the same 483.74 EUR/month contribution and 11,607.65 EUR
starting principal (existing savings) via `finance-math-toolkit`'s
`future-value` command, at a blended return derived from `market-data.md`:
**MSCI World Index (USD) equity, 7.45%/yr** (source: MSCI World Index
official factsheet,
https://www.msci.com/documents/10199/255599/msci-world-index-usd-net.pdf,
since-inception annualized 29 Dec 2000 – 31 Jul 2026, `websearch-fallback`
tier, accessed 2026-08-19) and **iShares Core U.S. Aggregate Bond ETF (AGG),
3.15%/yr** (source: iShares AGG official fact sheet,
https://www.ishares.com/us/literature/fact-sheet/agg-ishares-core-u-s-aggregate-bond-etf-fund-fact-sheet-en-us.pdf,
since-inception NAV annualized 22 Sep 2003 – 30 Jun 2026,
`websearch-fallback` tier, accessed 2026-08-19). Both nominal (not
inflation-adjusted). Concrete instruments for implementation: a UCITS
global-equity index tracker fund such as the iShares Core MSCI World UCITS
ETF (ticker SWDA/URTH) for the equity sleeve, and a broad investment-grade
bond index fund such as the iShares Core U.S. Aggregate Bond ETF (AGG) or a
EUR-hedged aggregate-bond UCITS equivalent for the bond sleeve.

### Path 1 — Baseline: moderate 50/50 allocation, target age 55 (NOT achievable)

- **Asset allocation:** 50% global equity (e.g. iShares Core MSCI World
  UCITS ETF, SWDA/URTH) / 50% aggregate bonds (e.g. iShares Core U.S.
  Aggregate Bond ETF, AGG, or a EUR-hedged equivalent) → blended nominal
  return = 0.5×7.45% + 0.5×3.15% = **5.30%/yr** (source: MSCI World and
  iShares AGG factsheets, both accessed 2026-08-19, as cited above).
- **Monthly contribution:** 483.74 EUR (full surplus).
- **Timeline:** 20 years (age 35 → 55, as requested).
- **Projected capital** (`future-value --principal 11607.65 --contribution
  483.74 --annual-rate 0.053 --years 20`): **239,295.64 EUR**.
- **Required capital:** 600,000 EUR.
- **Verdict: NOT achievable.** Shortfall of 360,704.36 EUR — the baseline
  path reaches only ~39.9% of the required capital.

### Path 2 — Longer horizon, same moderate allocation (achievable)

- **Asset allocation:** same 50/50 equity/bond index funds as Path 1,
  5.30%/yr blended.
- **Monthly contribution:** 483.74 EUR (unchanged).
- **Timeline:** 34 years (age 35 → **69**) — 14 years later than the
  requested age 55.
- **Projected capital** (`future-value --principal 11607.65 --contribution
  483.74 --annual-rate 0.053 --years 34`): **621,849.50 EUR** ≥ 600,000 EUR
  required. (33 years is insufficient: 584,176.85 EUR.)
- **Verdict: Achievable**, at the cost of a substantially delayed target
  retirement age (69 instead of 55).

### Path 3 — Growth-tilted allocation, shorter delay (achievable, needs risk-tolerance confirmation)

- **Asset allocation:** 70% equity (same MSCI World tracker) / 30% bonds
  (same AGG/aggregate-bond tracker) → blended nominal return =
  0.7×7.45% + 0.3×3.15% = **6.16%/yr** (source: same MSCI World / iShares
  AGG factsheets cited above). This is more equity-heavy than the strict
  50/50 split used as the "moderate" baseline in Path 1/2/4 — flagged
  explicitly as stretching beyond the user's stated moderate risk tolerance,
  and should be confirmed with the user before being presented as a
  recommendation, not just a moderate-family default.
- **Monthly contribution:** 483.74 EUR (unchanged).
- **Timeline:** 31 years (age 35 → **66**) — 11 years later than requested,
  3 years less delay than Path 2.
- **Projected capital** (`future-value --principal 11607.65 --contribution
  483.74 --annual-rate 0.0616 --years 31`): **616,762.90 EUR** ≥ 600,000 EUR
  required. (30 years is insufficient: 574,392.46 EUR.)
- **Verdict: Achievable**, with a shorter delay than Path 2, in exchange for
  a higher-equity, higher-volatility allocation than a strict moderate
  50/50 split.

### Path 4 — Reduced target income, original age 55 (achievable)

- **Asset allocation:** same 50/50 moderate index-fund allocation as Path 1,
  5.30%/yr blended.
- **Monthly contribution:** 483.74 EUR (unchanged).
- **Timeline:** 20 years (age 35 → 55, as originally requested — unchanged).
- **Reduced target monthly passive income:** 797 EUR/month (≈40% of the
  original 2,000 EUR/month goal), instead of extending the horizon or
  changing risk profile.
- **Required capital recomputed** for the reduced target
  (`required-capital --target-monthly-income 797 --swr 0.04`):
  **239,100 EUR**.
- **Projected capital:** 239,295.64 EUR (same Path-1 projection) ≥ 239,100
  EUR required (margin of +195.64 EUR).
- **Verdict: Achievable** at the originally requested target age, but only
  for a passive income of ~797 EUR/month rather than the requested 2,000
  EUR/month.

### Lever not modeled: higher contribution via income increase

The "higher contribution" lever (e.g. a raise, a new client, converting to a
higher-paying contract) is **not** modeled as a candidate path here, because
`requirements.md` states no concrete income-increase possibility — inventing
one (an amount and a date) would violate the no-fabricated-numbers rule. If
the user can identify a specific, real additional contribution capacity
(e.g. "I could add another client for +X PLN/month starting in year Y"),
this should be added as a new path and recomputed via the toolkit, not
estimated in prose.

## Assumptions & Sources

1. **SWR = 4%** — Bengen (1994) SAFEMAX study; Trinity Study (Cooley,
   Hubbard & Walz, AAII Journal, Feb 1998), 95% historical success rate over
   30-year horizons with a 50/50 portfolio (source: WebSearch summary of
   the above literature, accessed 2026-08-19).
2. **PLN/EUR rate = 0.232153** (1 EUR = 4.3075 PLN) — NBP official reference
   table No. 158/A/NBP/2026, 17 Aug 2026 (source:
   https://nbp.pl/statystyka-i-sprawozdawczosc/kursy/tabela-a/, accessed
   2026-08-19). Cross-checked against Currency.Wiki, 18 Aug 2026 (source:
   https://currency.wiki/pln-eur, accessed 2026-08-19). This is a
   point-in-time spot rate, not hedged or projected forward over the
   20–34 year horizons used below — a real FX-risk caveat, not resolved by
   this artifact.
3. **Market returns** — from `market-data.md` (this run): MSCI World Index
   (USD) 7.45%/yr since-inception annualized (29 Dec 2000 – 31 Jul 2026,
   source: MSCI World Index official factsheet,
   https://www.msci.com/documents/10199/255599/msci-world-index-usd-net.pdf,
   `websearch-fallback` tier, accessed 2026-08-19), iShares Core U.S.
   Aggregate Bond ETF (AGG) 3.15%/yr since-inception annualized (22 Sep
   2003 – 30 Jun 2026, source: iShares AGG official fact sheet,
   https://www.ishares.com/us/literature/fact-sheet/agg-ishares-core-u-s-aggregate-bond-etf-fund-fact-sheet-en-us.pdf,
   `websearch-fallback` tier, accessed 2026-08-19). Both nominal (not
   inflation-adjusted), USD-denominated; applied here to EUR-denominated
   projections as a proxy for globally-diversified index-fund returns, per
   `market-data.md`'s own notes to downstream agents.
4. **Moderate allocation baseline = 50% equity / 50% bonds** for Paths 1, 2,
   4 (blended 5.30%/yr). Path 3 uses a **70/30 growth-tilted** alternative
   (blended 6.16%/yr), explicitly flagged as more aggressive than a strict
   "moderate" split.
5. **Concrete instruments:** iShares Core MSCI World UCITS ETF (ticker
   SWDA/URTH) for the equity sleeve; iShares Core U.S. Aggregate Bond ETF
   (ticker AGG) or a EUR-hedged aggregate-bond UCITS equivalent for the
   bond sleeve — per `market-data.md`'s choice of benchmarks.
6. **All contributions/projections** use the full disposable surplus
   (483.74 EUR/month) and full existing savings (11,607.65 EUR) as the
   starting principal — per `cashflow.md` and `requirements.md`.
7. **Net income and surplus figures** carry the caveats already flagged in
   `net-income.md` and `cashflow.md` (tax regime and ZUS relief eligibility
   not confirmed by the user; expense figure not broken out) — not
   re-derived here, carried forward for `financial-auditor`.
8. All numeric projections were computed via `finance-math-toolkit`
   (`scripts/calc.py`), not estimated in prose; exact commands and outputs
   are shown inline above for independent recomputation by
   `financial-auditor`.
