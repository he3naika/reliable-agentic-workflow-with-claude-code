# Market Data — run-2026-08-18-003

## MCP Attempt Log
`mcp__yahoo-finance__get_historical_stock_prices` was called for the first
benchmark ticker (SPY) and returned `Error: No such tool available:
mcp__yahoo-finance__get_historical_stock_prices` (the Yahoo Finance MCP was
not reachable/registered in this session). Per the retry policy, the call
was retried once with identical parameters and failed identically. No
fabricated figures were produced from this failed path — all figures below
were obtained via the WebSearch fallback with cited public sources.

**Source for every figure in this artifact: WebSearch fallback (MCP
unavailable after 1 retry).**

## Benchmarks Used

Selected for a 40-year-old, moderate-risk-tolerance investor with a 10-year
horizon (age 40 → 50), per `artifacts/requirements.md`:

1. **SPY** — SPDR S&P 500 ETF Trust. Broad US large-cap equity benchmark,
   representing the growth/equity sleeve of a moderate-risk portfolio.
2. **AGG** — iShares Core U.S. Aggregate Bond ETF. Broad US investment-grade
   bond benchmark, representing the fixed-income/defensive sleeve.
3. **AOM** — iShares Core 40/60 Moderate Allocation ETF. A pre-blended
   ~40% equity / 60% bond fund explicitly marketed as a "moderate
   allocation" portfolio — used as a direct, single-instrument proxy for a
   moderate-risk balanced benchmark rather than an assumed equity/bond split.

## Historical Return

All figures are compound annual growth rate (CAGR) of **total return**
(dividends/coupons reinvested), as reported by financecharts.com's total
return CAGR series, reflecting real historical price/distribution data
(not a forward-looking estimate).

| Benchmark | 10-Year CAGR | 15-Year CAGR |
|---|---|---|
| SPY (US equity) | 15.58% | 14.15% |
| AGG (US aggregate bonds) | 1.52% | 2.11% |
| AOM (moderate 40/60 allocation) | 5.90% | 5.64% |

Notes on interpretation for downstream agents:
- The 10-year AGG figure (1.52%) reflects the unusually weak bond
  performance of the 2016–2026 window (the rapid 2022–2023 rate-hiking
  cycle depressed bond prices); the 15-year figure (2.11%) and Bloomberg US
  Aggregate Bond Index's since-1976 long-run average of ~6.6% (cited in the
  Grokipedia summary of the Bloomberg US Aggregate Bond Index page, itself
  citing Bloomberg index data) are provided as additional context — do not
  treat 1.52% as a reliable 10-year-forward assumption without flagging this
  caveat.
- **AOM's 10-year CAGR (5.90%) is the single most direct "moderate risk,
  10-year horizon" figure in this table** and is recommended as the primary
  benchmark return for `retirement-income-planner`'s moderate-risk
  projections, since it already reflects a diversified 40/60 equity/bond mix
  rather than requiring the planner to assume a blend weighting itself.
- SPY and AGG are provided as the underlying equity/bond components in case
  the planner wants to model a custom allocation different from AOM's fixed
  40/60 split.

## Period

- SPY, AGG, AOM 10-Year CAGR: trailing 10 years to on/around July–August 2026
  (financecharts.com's rolling "10Y" total-return CAGR window).
- SPY, AGG, AOM 15-Year CAGR: trailing 15 years to on/around July–August 2026
  (financecharts.com's rolling "15Y" total-return CAGR window).
- Bloomberg US Aggregate Bond Index since-inception context figure: 1976
  through late 2023 (as reported in the cited secondary source).

Exact daily as-of dates are set by financecharts.com's data refresh cycle and
were not independently re-derived from raw price series in this run because
the MCP (which would have supplied raw start/end prices for a `cagr`
calc.py computation) was unavailable; see MCP Attempt Log above.

## Source & Date Accessed

All accessed via WebSearch on **2026-08-18**:

- SPY 10Y/15Y total-return CAGR: [SPDR S&P 500 ETF Trust (SPY) Total Return YTD, TTM, 3Y, 5Y, 10Y, 20Y Compound Annual Growth Rate (CAGR) — financecharts.com](https://www.financecharts.com/etfs/SPY/growth/total-return-cagr)
- AGG 10Y/15Y total-return CAGR: [iShares Core U.S. Aggregate Bond ETF (AGG) Total Return YTD, TTM, 3Y, 5Y, 10Y, 20Y Compound Annual Growth Rate (CAGR) — financecharts.com](https://www.financecharts.com/etfs/AGG/performance/total-return-cagr)
- AOM 10Y/15Y total-return CAGR: [iShares Core Moderate Allocation ETF (AOM) Total Return YTD, TTM, 3Y, 5Y, 10Y, 20Y — financecharts.com](https://www.financecharts.com/etfs/AOM/performance/total-return)
- AOM since-inception (Nov 4, 2008) average annual return (7.12%, supplementary context only, not used in the table above): [AOM: iShares Core 40/60 Moderate Allocation ETF — MutualFunds.com](https://www.mutualfunds.com/etfs/aom-ishares-core-moderate-allocation-etf/)
- Bloomberg US Aggregate Bond Index long-run (1976–late 2023) ~6.6% context figure: [Bloomberg US Aggregate Bond Index — Grokipedia](https://grokipedia.com/page/Bloomberg_US_Aggregate_Bond_Index)
- Official primary fact sheets identified but not directly parsed in this
  session (listed for the auditor/any follow-up verification):
  [AGG fact sheet, iShares, as of June 30, 2026](https://www.ishares.com/us/literature/fact-sheet/agg-ishares-core-u-s-aggregate-bond-etf-fund-fact-sheet-en-us.pdf),
  [AOM fact sheet, iShares, as of June 30, 2026](https://www.ishares.com/us/literature/fact-sheet/aom-ishares-core-40-60-moderate-allocation-etf-fund-fact-sheet-en-us.pdf)

## Fallback Disclosure

**Every figure in this artifact came from the WebSearch fallback, not the
Yahoo Finance MCP.** The MCP tool
(`mcp__yahoo-finance__get_historical_stock_prices`) was unavailable in this
session (tool not registered/reachable) on both the initial attempt and the
retry. No raw price series was obtained, so `finance-math-toolkit`'s `cagr`
command was not invoked in this run — the CAGR figures above are the
benchmark providers'/data aggregators' own already-computed and publicly
reported CAGR values, each with a direct citation and access date, per the
explicit fallback instructions for this agent.
