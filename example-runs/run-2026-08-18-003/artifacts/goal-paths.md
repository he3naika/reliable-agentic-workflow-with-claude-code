# Goal Paths — run-2026-08-18-003

## Goal Summary

- **Goal type:** retirement_income (target passive income by target age)
- **Current age:** 40 → **Target age:** 50 (10-year accumulation horizon)
- **Target passive income:** 2,000 EUR/month (24,000 EUR/year)
- **Risk tolerance:** moderate
- **Monthly contribution capacity (confirmed):** 25,000 PLN/month, fully
  disposable (per `cashflow.md`) → **5,787.25 EUR/month** at the sourced
  conversion rate below.
- **Existing lump sum:** 200,000 PLN, currently uninvested cash in a PKO
  Bank Polski savings account → **46,298.00 EUR** at the sourced conversion
  rate below.

### Currency conversion

- Rate used: **1 PLN = 0.23149 EUR** (equivalently ≈4.3162 PLN/EUR), mid-market
  rate as of **2026-08-18**.
- Source: [Wise — PLN to EUR currency converter](https://wise.com/us/currency-converter/pln-to-eur-rate/history) (accessed 2026-08-18).
- Computed via `finance-math-toolkit convert-currency`:
  - `convert-currency --amount 25000 --rate 0.23149` → `{"converted_amount": 5787.25}`
  - `convert-currency --amount 200000 --rate 0.23149` → `{"converted_amount": 46298.0}`

### Safe withdrawal rate (SWR) — sourced and justified

Retiring at age 50 implies a **very long decumulation horizon** (likely
35–45+ years, to age 85–95+), which is materially longer than the ~30-year
horizon the classic "4% rule" (Bengen 1994; Trinity Study, Cooley/Hubbard/Walz
1998) was validated against. Updated Trinity Study analyses explicitly flag
that longer/early-retirement horizons need a lower withdrawal rate to keep
failure risk low:

> "For early retirement with 35-50+ year horizons, aim for 3.0–3.5% ... With
> 50 years of retirement, you have a 90% chance of success with a 4%
> withdrawal rate at most. A withdrawal rate of around 3.5% would be safer
> for most people."
— [The Poor Swiss — Updated Trinity Study For 2026](https://thepoorswiss.com/updated-trinity-study/), [Retirement Researcher — Safe Withdrawal Rates for Retirement and the Trinity Study](https://retirementresearcher.com/safe-withdrawal-rates-for-retirement-and-the-trinity-study/) (both accessed 2026-08-18)

Given the age-50 retirement start, this plan uses **3.5% as the primary
(conservative) SWR** and reports the classic **4% SWR** alongside it for
reference/comparison — not as the primary planning figure, since 4% was
validated for ~30-year, not 40+-year, horizons.

| SWR | Required capital for 2,000 EUR/month | Toolkit call |
|---|---|---|
| **3.5% (primary, early-retirement-adjusted)** | **685,714.29 EUR** | `required-capital --target-monthly-income 2000 --swr 0.035` |
| 4.0% (classic reference) | 600,000.00 EUR | `required-capital --target-monthly-income 2000 --swr 0.04` |

All verdicts below are judged primarily against the **685,714.29 EUR**
figure, with the 600,000.00 EUR figure noted for context.

### Moderate-risk return assumption

Per `market-data.md`, **AOM (iShares Core 40/60 Moderate Allocation ETF)**
10-year total-return CAGR of **5.90%** is the recommended single-instrument
proxy for a moderate-risk, 10-year-horizon portfolio (it already reflects a
diversified 40% equity / 60% bond blend, rather than requiring an assumed
split). This is the primary return assumption used below. A downside
stress-test using AOM's 15-year CAGR (5.64%) and a growth-tilted custom
60% SPY / 40% AGG blend (9.96%) are also modeled as alternatives within
"moderate" risk tolerance, per market-data.md's SPY/AGG figures.

## Candidate Paths

### Path 1 — Recommended: Full Commitment, Moderate Balanced Allocation (AOM 40/60)

- **Asset allocation:** 100% into a moderate 40/60 equity/bond balanced
  allocation (proxied by AOM or an equivalent low-cost 40/60 balanced
  fund), consistent with the user's stated moderate risk tolerance.
- **Capital deployed:** full 200,000 PLN lump sum (46,298.00 EUR) redeployed
  from cash into the balanced allocation, plus the full 25,000 PLN/month
  (5,787.25 EUR/month) surplus invested monthly.
- **Return assumption:** 5.90% CAGR (AOM 10-year total return CAGR).
- **Timeline:** 10 years (age 40 → 50).
- **Toolkit call:** `future-value --principal 46298 --contribution 5787.25 --annual-rate 0.059 --years 10`
- **Projected capital at age 50:** **1,026,681.71 EUR**
- **Required capital (3.5% SWR):** 685,714.29 EUR → **surplus of +340,967.42 EUR (+49.7%)**
- **Required capital (4% SWR, reference):** 600,000.00 EUR → surplus of +426,681.71 EUR (+71.1%)
- **Verdict: Achievable, with substantial margin**, even judged against the
  more conservative 3.5% SWR appropriate for a 40+-year decumulation
  horizon starting at age 50.

### Path 2 — Downside Stress-Test: Same Commitment, Lower Moderate Return

- **Asset allocation:** identical to Path 1 (100% moderate 40/60 balanced
  allocation, full lump sum + full monthly surplus).
- **Return assumption:** **5.64%** CAGR (AOM's own **15-year** total-return
  CAGR, used here as a lower/older-cycle stress case on the same
  instrument, per `market-data.md`).
- **Timeline:** 10 years.
- **Toolkit call:** `future-value --principal 46298 --contribution 5787.25 --annual-rate 0.0564 --years 10`
- **Projected capital at age 50:** **1,011,377.63 EUR**
- **Required capital (3.5% SWR):** 685,714.29 EUR → **surplus of +325,663.34 EUR (+47.5%)**
- **Verdict: Achievable.** The outcome is not materially sensitive to the
  exact CAGR chosen within the AOM 10Y/15Y range — this path confirms
  Path 1 isn't a fragile, single-assumption result.

### Path 3 — Growth-Tilted Moderate: Custom 60/40 Equity/Bond Blend

- **Asset allocation:** a custom 60% equity (SPY-proxy) / 40% bond
  (AGG-proxy) blend — more equity-heavy than the AOM 40/60 fund, still
  within a "moderate" (not aggressive 100%-equity) risk profile, offered as
  an alternative for a user comfortable tilting toward growth given the
  10-year horizon.
- **Blended return:** 0.60 × 15.58% (SPY 10Y CAGR) + 0.40 × 1.52% (AGG 10Y
  CAGR) = **9.96%** (computed by hand from `market-data.md` figures; the
  blend weighting itself, not the underlying CAGRs, is the assumption to
  flag for the auditor).
- **Capital deployed:** full lump sum + full monthly surplus, same as Path 1.
- **Timeline:** 10 years.
- **Toolkit call:** `future-value --principal 46298 --contribution 5787.25 --annual-rate 0.0996 --years 10`
- **Projected capital at age 50:** **1,307,611.58 EUR**
- **Required capital (3.5% SWR):** 685,714.29 EUR → **surplus of +621,897.29 EUR (+90.7%)**
- **Verdict: Achievable, with the largest margin of all paths** — but carries
  materially higher equity-concentration volatility than Path 1's
  pre-blended 40/60 fund, and the 60/40 split here is an assumed weighting
  rather than a single diversified instrument's reported return. Suitable
  only if the user's "moderate" tolerance leans toward the growth end.

### Path 4 — Sensitivity Check: Partial Commitment (60% of Monthly Surplus)

Included to test how fragile the comfortable Path 1 margin is if the user's
stated "full 25,000 PLN/month available" turns out to be optimistic in
practice (e.g. future expense creep against the "separate budget").

- **Asset allocation:** same moderate 40/60 balanced allocation as Path 1.
- **Capital deployed:** full 200,000 PLN lump sum (46,298.00 EUR), but only
  **60% of the monthly surplus** — 15,000 PLN/month (3,472.35 EUR/month) —
  invested, with the remaining 40% held back as a buffer.
- **Return assumption:** 5.90% CAGR (AOM 10-year), same as Path 1.
- **Timeline:** 10 years.
- **Toolkit call:** `future-value --principal 46298 --contribution 3472.35 --annual-rate 0.059 --years 10`
- **Projected capital at age 50:** **649,369.18 EUR**
- **Required capital (3.5% SWR):** 685,714.29 EUR → **shortfall of −36,345.11 EUR (−5.3%) — NOT achievable** under the primary, conservative SWR.
- **Required capital (4% SWR, reference):** 600,000.00 EUR → surplus of
  +49,369.18 EUR (+8.2%) — achievable only under the less conservative
  classic 4% rule.
- **Verdict: Marginal / not robustly achievable.** At 60% of the stated
  contribution capacity, the goal's achievability flips depending on which
  SWR is trusted. This is the honest boundary case: the comfortable margin
  in Path 1 depends on the user actually investing the *full* stated
  surplus, not a partial amount — the plan should not be presented as
  "achievable no matter what."

## Assumptions & Sources

1. **Currency conversion rate:** 1 PLN = 0.23149 EUR, mid-market, accessed
   2026-08-18 — [Wise PLN→EUR converter](https://wise.com/us/currency-converter/pln-to-eur-rate/history).
2. **Safe withdrawal rate:** 3.5% (primary, early-retirement-adjusted),
   4.0% (classic reference) — [The Poor Swiss, Updated Trinity Study For 2026](https://thepoorswiss.com/updated-trinity-study/); [Retirement Researcher, Safe Withdrawal Rates for Retirement and the Trinity Study](https://retirementresearcher.com/safe-withdrawal-rates-for-retirement-and-the-trinity-study/) (both accessed 2026-08-18). Rationale: retiring at 50 implies a 35–45+ year decumulation horizon, materially longer than the ~30-year horizon the 4% rule was validated for.
3. **Moderate-risk return assumptions:** AOM (iShares Core 40/60 Moderate
   Allocation ETF) 10-year CAGR 5.90% (primary) and 15-year CAGR 5.64%
   (stress-test); SPY 10-year CAGR 15.58% and AGG 10-year CAGR 1.52% (used
   only for the custom 60/40 blend in Path 3) — all from
   `artifacts/market-data.md`, sourced via WebSearch fallback (Yahoo
   Finance MCP unavailable this run), financecharts.com, accessed
   2026-08-18. Returns are historical total-return CAGRs, not
   forward-looking guarantees; inflation is not separately modeled (the
   2,000 EUR/month target and required-capital figure are treated as
   already expressed in today's terms).
4. **Net income / contribution capacity:** 25,000 PLN/month is the user's
   confirmed, fully net (post-tax, post-ZUS/health, ryczałt regime) monthly
   income, per `artifacts/net-income.md` and `artifacts/cashflow.md`, with
   the full amount confirmed by the user as available for investing (no
   expenses deducted from it, by explicit user statement, since expenses
   are funded from a separate budget).
5. **Existing savings:** 200,000 PLN currently held as uninvested cash
   (PKO Bank Polski savings account), per `artifacts/requirements.md`,
   treated as a redeployable starting principal in Paths 1–3 (and Path 4).
6. All future-value and required-capital figures above were computed via
   `finance-math-toolkit`'s `scripts/calc.py` (`future-value`,
   `required-capital`, `convert-currency` commands) — no manual arithmetic
   was used for these figures, only for the Path 3 blended-CAGR weighting
   (0.60 × 15.58% + 0.40 × 1.52% = 9.96%), which is flagged above for
   `financial-auditor` to independently re-verify.
7. No tax on investment gains/withdrawals in Poland (e.g. "Belka tax" on
   capital gains) is modeled in this artifact — this is a gap to flag for
   `feasibility-assessor`/`financial-auditor`, since it would reduce the
   real sustainable withdrawal somewhat below the pre-tax figures above.
