# Market Data

## Benchmarks Used

Goal is `retirement_income`, moderate risk tolerance, 20-year horizon, willing
to invest in index funds. Two benchmarks were chosen to represent a moderate
(roughly balanced growth/defensive) index-fund allocation:

1. **Global developed-market equity** — MSCI World Index (USD), the index
   tracked by widely available UCITS/US index funds (e.g. iShares Core MSCI
   World UCITS ETF, ticker SWDA/URTH).
2. **Aggregate bond / fixed income** — iShares Core U.S. Aggregate Bond ETF
   (ticker `AGG`), a standard broad investment-grade bond benchmark.

## Data-source tier attempts (per CLAUDE.md three-tier contract)

### Tier 1 — Yahoo Finance MCP (primary)

`mcp__yahoo-finance__get_historical_stock_prices` is **not exposed as a
callable tool in this session** (no such function is present in the
available tool list). This was treated as the tool being unavailable for
this run, so tier 1 could not be attempted at all — moved directly to tier 2
as instructed.

### Tier 2 — TradingView MCP (secondary)

Genuinely attempted `mcp__tradingview__stock_prices` (the only TradingView
tool exposed in this session) for `AMEX:URTH, AMEX:AGG`, 3 attempts as
required:

1. Attempt 1: timed out after ~1800s — "sent no response or progress;
   aborting."
2. Attempt 2: `UPSTREAM_ERROR` — `SSLCertVerificationError: [SSL:
   CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local
   issuer certificate` when the server tried to reach
   `scanner.tradingview.com`.
3. Attempt 3: same `UPSTREAM_ERROR` / SSL certificate verification failure.

All 3 attempts failed (transport/timeout + TLS trust-chain error on the
server side, not a data problem I can work around). Note also that even had
it succeeded, `mcp__tradingview__stock_prices` only returns a current
price/daily % change snapshot, not the historical start/end price series
needed for a CAGR calculation over 10-20 years — so this tier is exhausted
per the retry policy and moved to tier 3.

### Tier 3 — WebSearch (last resort)

Used WebSearch to find each benchmark's own publicly reported long-run
annualized return (not raw prices — no toolkit `cagr` computation was
needed/possible since the sources already report annualized figures
directly). Both figures below are `websearch-fallback`.

## Historical Return

- **MSCI World Index (USD): 7.45% / year** annualized, "since inception"
  (29 Dec 2000 – 31 Jul 2026) (source: MSCI World Index official factsheet,
  https://www.msci.com/documents/10199/255599/msci-world-index-usd-net.pdf,
  accessed 2026-08-19 via WebSearch). Tier: `websearch-fallback`.
- **iShares Core U.S. Aggregate Bond ETF (AGG): 3.15% / year** annualized,
  "since inception" NAV return (22 Sep 2003 – 30 Jun 2026) (source: iShares
  AGG official fact sheet,
  https://www.ishares.com/us/literature/fact-sheet/agg-ishares-core-u-s-aggregate-bond-etf-fund-fact-sheet-en-us.pdf,
  accessed 2026-08-19 via WebSearch). Tier: `websearch-fallback`.

Supplementary data point found but not used as the headline figure: MSCI
World Index 10-year annualized total return of **12.73% / year** (period
ending 31 Jul 2026) (source: MSCI World Index official factsheet,
https://www.msci.com/documents/10199/255599/msci-world-index-usd-net.pdf,
accessed 2026-08-19 via WebSearch; tier: `websearch-fallback`) — kept here
for context only; the since-inception figure above is preferred because it
spans a period closer to the user's 20-year horizon and includes both the
dot-com bust and the 2008 crisis, giving a more conservative, cycle-inclusive
long-run figure.

| Benchmark | Annualized return | Period | Tier |
|---|---|---|---|
| MSCI World Index (USD) | 7.45% / year | 29 Dec 2000 – 31 Jul 2026 (~25.6 years, "since inception" figure on the official factsheet, the longest period the factsheet reports) | `websearch-fallback` |
| iShares Core U.S. Aggregate Bond ETF (AGG) | 3.15% / year | 22 Sep 2003 (fund inception) – 30 Jun 2026 (~22.75 years, "since inception" NAV annualized return) | `websearch-fallback` |

## Period

- Equity benchmark period: 29 Dec 2000 – 31 Jul 2026 (~25.6 years).
- Bond benchmark period: 22 Sep 2003 – 30 Jun 2026 (~22.75 years).

Both exceed the requested 10-20 year window; both are the longest
"since-inception" periods the respective official factsheets report, so nothing
shorter was available to select instead.

## Source & Date Accessed

- MSCI World Index (USD) official factsheet, msci.com
  (`https://www.msci.com/documents/10199/255599/msci-world-index-usd-net.pdf`
  and related MSCI World Index factsheet page) — accessed via WebSearch
  2026-08-19. Tier: `websearch-fallback`.
- iShares Core U.S. Aggregate Bond ETF (AGG) official fact sheet, ishares.com
  (`https://www.ishares.com/us/literature/fact-sheet/agg-ishares-core-u-s-aggregate-bond-etf-fund-fact-sheet-en-us.pdf`,
  as of 30 Jun 2026) — accessed via WebSearch 2026-08-19. Tier:
  `websearch-fallback`.

## Notes for downstream agents

- Both figures are nominal (not inflation-adjusted) USD-denominated
  annualized total/NAV returns. The user's goal is stated in EUR and current
  finances are in PLN — `cashflow-analyzer` / `retirement-income-planner`
  must handle currency conversion explicitly, not assume these returns apply
  1:1 in EUR/PLN terms.
- For a moderate-risk 20-year allocation, a reasonable blended assumption
  (e.g. weighting equity/bond roughly 60/40 or 50/50 per the
  `retirement-income-planner`'s own allocation decision) should combine
  these two figures — that weighting decision belongs to
  `retirement-income-planner`, not to this artifact.
- Tier 1 (Yahoo Finance MCP) was unavailable (tool not exposed in this
  session) and tier 2 (TradingView MCP) failed after 3 genuine attempts
  (1 timeout + 2 SSL certificate verification errors reaching
  `scanner.tradingview.com`). If a future run has a working Yahoo Finance or
  TradingView MCP connection, these WebSearch figures should be re-verified
  against actual price-series CAGR computations via `finance-math-toolkit`.
