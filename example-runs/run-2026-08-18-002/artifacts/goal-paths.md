# Goal Paths — Personal Finance Goal Planner

## Goal Summary

- **Goal type:** `savings_goal` — accumulate cash to buy a Mazda CX-5.
- **Primary target:** new Mazda CX-5, official dealer price **40,000 USD**
  (given directly by the user, not searched).
- **Target date:** 31 December 2026. Today is 2026-08-18, leaving **~4.4
  months** (135 days) — modeled as **4 full monthly contribution periods**
  (Sep, Oct, Nov, Dec 2026; the remaining ~13 days of August are not counted
  as a full contribution period, a conservative assumption).
- **Planning currency:** BYN. Target converted from USD using a real, cited
  exchange rate (see Assumptions & Sources).
- **Target in BYN:** 40,000 USD × 3.037988 BYN/USD = **121,519.52 BYN**
  (`finance-math-toolkit convert-currency`, not hand-estimated).
- **Net income:** 8,000 BYN/month (confirmed net by user). **Expenses:**
  2,537 BYN/month (combined). **Disposable surplus: 5,463 BYN/month**
  (`cashflow.md`).
- **Existing savings toward goal:** 0. **Existing debts:** none.
- **Parking vehicle:** cash-only / low-risk (savings account or similar),
  0% assumed return — horizon is short and/or the money must stay liquid
  for a near-term purchase, per confirmed requirements. No investment return
  is applied to any path below.
- **Financing:** explicitly out of scope — pure cash savings, no loan.

`cashflow-analyzer` flagged that the required contribution for the exact
target/date combination likely far exceeds the 5,463 BYN/month surplus. This
is confirmed precisely below with `finance-math-toolkit`, and honest
alternatives are presented rather than a bare "not possible."

## Candidate Paths

### Path 1 — Full target (40,000 USD), exact deadline (31 Dec 2026)

- **Target:** 121,519.52 BYN (40,000 USD)
- **Timeline:** 4 monthly contributions (2026-08-18 → 2026-12-31)
- **Required monthly contribution:** 121,519.52 ÷ 4 = **30,379.88 BYN/month**
  (verified via `future-value`: principal 0, contribution 30,379.88, annual
  rate 0, 4 months → future value 121,519.52 BYN, matches target exactly)
- **Where to allocate:** cash-only, e.g. a BYN savings/deposit account —
  no investment given the sub-6-month horizon.
- **Available disposable surplus:** 5,463 BYN/month
- **Gap:** 30,379.88 − 5,463 = **24,916.88 BYN/month short**, i.e. the
  required contribution is **~5.6× the available surplus**.
- **Reality check:** saving 100% of the current surplus for all 4 months
  accumulates only 21,852 BYN (`future-value`: contribution 5,463, 0%, 4
  months) ≈ 7,193 USD at the same rate — about **18% of the 40,000 USD
  target**.
- **Verdict:** **NOT achievable** from disposable surplus alone by 31 Dec
  2026. Closing the gap would require ~24,917 BYN/month of additional
  income, an asset sale, gifted funds, or financing — all currently out of
  scope per confirmed requirements.

### Path 2 — Full target (40,000 USD), realistic timeline at current surplus

- **Target:** 121,519.52 BYN (40,000 USD), unchanged.
- **Monthly contribution:** the full 5,463 BYN/month disposable surplus,
  saved consistently, cash-only (0% return).
- **Timeline:** `future-value` shows 22 months reaches 120,186.00 BYN
  (still short by 1,333.52 BYN) and 23 months reaches 125,649.00 BYN
  (exceeds target). **23 months** are needed to fully cover the target —
  i.e. around **late July 2028** (2026-08-18 + 23 months), roughly **19
  months past** the user's original 31 Dec 2026 date.
- **Where to allocate:** cash-only, BYN savings/deposit account.
- **Verdict:** **Achievable**, but only if the target date is moved from
  31 Dec 2026 to ~July 2028 and 100% of the current surplus is preserved
  for the entire period with no interruptions or competing expenses.

### Path 3 — Reduced target: used Mazda CX-5, faster (but still delayed) timeline

- **Target basis:** the previous version of this path relied solely on a
  US-market Edmunds appraisal, flagged by `financial-auditor` as an
  unbounded proxy for Belarus pricing. This version adds a genuine
  Belarus-market reference found via WebSearch:
  - **Belarus-market anchor (primary):** a real listing on `cars.av.by`
    (Belarus's main used-car marketplace) — a 2023 Mazda CX-5, ~7,000 km,
    listed at **98,099 BYN** (≈ 32,291.54 USD-equivalent at the same
    3.037988 BYN/USD rate used throughout this document, per
    `convert-currency`) — [Mazda CX-5 listings, cars.av.by](https://cars.av.by/mazda/cx-5),
    accessed 2026-08-18. This is one concrete listing among 146 currently on
    the site (price varies by year/mileage/trim; the full distribution
    could not be extracted from search results), so it is used here as a
    real reference anchor, not a market average.
  - **US Edmunds appraisal (secondary, sensitivity band only):**
    25,665–37,916 USD (77,969.96–115,188.35 BYN, same conversion as before)
    — [2026 Mazda CX-5 Value | Edmunds](https://www.edmunds.com/mazda/cx-5/2026/appraisal-value/),
    accessed 2026-08-18. No longer used as the primary target; kept only as
    a bracketing sensitivity range around the Belarus anchor.
  - **Why the US figure is still a defensible bound here:** Belarus import
    rules (EAEU common customs tariff) impose steep duty+VAT on personally
    imported used vehicles under 3 years old (roughly 48–54% of customs
    value or a per-cc minimum, per multiple import-broker sources — see
    Assumptions & Sources), which would normally push a freshly-imported
    near-new car's landed Belarus cost well above the raw US price. The
    real av.by anchor above, however, already reflects an actual Belarus
    retail/resale price — any historical import cost on that specific,
    already-registered car is already baked into the seller's ask — and it
    lands squarely inside the Edmunds range (not above it). That is a real
    cross-check, not an assumption: it is why the Edmunds range is retained
    as a sensitivity band instead of being discarded outright.
- **Target range used for calculations:** **77,969.96 – 115,188.35 BYN**,
  with **98,099 BYN as the single most-likely point** (the real Belarus
  anchor).
- **Monthly contribution:** full 5,463 BYN/month surplus, cash-only (0%).
- **Timeline (`future-value`, independently computed at each price point,
  0% annual rate):**
  - Low end (77,969.96 BYN): 14mo → 76,482.00 BYN (short); **15mo → 81,945.00
    BYN (clears it)**.
  - **Most likely (98,099 BYN, av.by anchor): 17mo → 92,871.00 BYN (short);
    18mo → 98,334.00 BYN (clears it) → 18 months.**
  - High end (115,188.35 BYN): 21mo → 114,723.00 BYN (short); **22mo →
    120,186.00 BYN (clears it)**.
  - → Range of **15–22 months**, most likely **~18 months** (mid-February
    2028), depending on the specific used unit actually available/chosen —
    still **6.5–21.5 months past** the original 31 Dec 2026 date.
- **Where to allocate:** cash-only, BYN savings/deposit account.
- **Verdict:** **Achievable**, and faster than Path 2 across the whole
  range (15–22 months vs. Path 2's fixed 23), but the target date still has
  to move well past 31 Dec 2026, and it swaps the "new car" requirement for
  a used one. Because the real price depends materially on the exact
  year/mileage/trim, the user should get 2–3 concrete av.by or dealer
  quotes for a unit they'd actually accept before committing to a specific
  target date — the ~18-month figure is the best available estimate given
  current information, not a guarantee.

## Assumptions & Sources

- **USD/BYN exchange rate:** 1 USD = 3.037988 BYN, as of 2026-08-16 —
  [US Dollar (USD) To Belarusian Ruble (BYN) Exchange Rate History for 2026](https://www.exchange-rates.org/exchange-rate-history/usd-byn-2026),
  accessed 2026-08-18. Cross-checked for plausibility (recent daily range
  ~2.96–3.05 across multiple aggregators for the same week); official
  National Bank of the Republic of Belarus daily rate (nbrb.by) could not
  be pulled directly from search results but is the authoritative source
  if the user wants to re-verify.
- **Belarus used Mazda CX-5 market anchor (Path 3, primary):** a real
  listing on `cars.av.by`, 2023 model, ~7,000 km, **98,099 BYN** —
  [Mazda CX-5 listings, cars.av.by](https://cars.av.by/mazda/cx-5), accessed
  2026-08-18. One concrete real-market data point out of 146 current
  listings on the site; used as a reference anchor, not an average, because
  a full price distribution could not be extracted from search results.
- **Used Mazda CX-5 (2026 model) value range (Path 3, secondary sensitivity
  band only):** 25,665–37,916 USD (Clean condition, ~12,000 mi/yr) —
  [2026 Mazda CX-5 Value | Edmunds](https://www.edmunds.com/mazda/cx-5/2026/appraisal-value/),
  accessed 2026-08-18. US-market appraisal; retained only because the real
  Belarus anchor above falls inside this range, giving it some cross-checked
  relevance — it is not used as a stand-alone Belarus price estimate.
- **Belarus used-vehicle import duty/VAT context (used to sanity-check the
  above, Path 3):** EAEU common customs tariff imposes roughly 48–54%
  ad valorem duty+VAT (or a per-cc minimum) on personally imported vehicles
  under 3 years old, and €1.5–5.7/cc-based duty for vehicles over 5 years
  old, plus a 15% duty / 20% VAT baseline and a ~544.5 BYN recycling fee for
  vehicles over 3 years old for personal use — [Belarus Import Regulation &
  Taxes for Japan Used Cars, japanesecartrade.com](https://blog.japanesecartrade.com/1094-belarus-import-regulation-for-japan-used-cars/);
  [Belarus's Regulatory Framework for Importing Used Cars from China,
  autocango.com](https://www.autocango.com/blog-detail/belarus-import-regulations-used-cars-from-china);
  [Import duties, Ministry of Foreign Affairs of the Republic of
  Belarus](https://mfa.gov.by/en/export/tariffs/vvoz/) — all accessed
  2026-08-18. This context explains why a raw US price cannot be assumed
  to transfer directly to Belarus, and why the real av.by anchor (which
  already prices in any such costs for an already-registered car) is used
  as the primary reference instead.
- **All monthly-contribution/timeline figures were computed with
  `finance-math-toolkit`'s `future-value` and `convert-currency` commands**
  (0% annual rate throughout, consistent with the cash-only/no-investing
  assumption for this short-to-medium horizon) — none were estimated by
  hand, including all three price points (low/most-likely/high) in Path 3.
- Cash-only parking (0% return) is carried from `requirements.md`'s
  confirmed assumption; no investment return is applied to any path.
- No financing/loan component is modeled, per confirmed requirements
  ("pure cash savings, no financing").
- Disposable surplus (5,463 BYN/month) is taken as-is from `cashflow.md`;
  no expense-category breakdown was available to identify further cuttable
  spend, so no path assumes a higher contribution than the stated surplus.
- All paths assume the 5,463 BYN/month surplus is fully and consistently
  preserved toward this single goal for the entire stated timeline, with no
  competing priorities, emergencies, or income/expense changes — a
  significant real-world assumption the user should weigh, especially for
  the 15–23 month paths.
</content>
