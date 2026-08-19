# Cashflow Analysis

## Net Income

- **Net monthly income: 8,083.71 PLN/month** (per `net-income.md`).
- Basis: 12,000.00 PLN/month gross, B2B self-employed (ryczałt ewidencjonowany
  12%), less ZUS social contributions (1,926.76 PLN), health insurance
  contribution (830.58 PLN), and ryczałt income tax (1,158.95 PLN).
- Carries the caveats already flagged in `net-income.md` (tax regime and ZUS
  relief eligibility not confirmed by the user) — those affect the net income
  figure itself, not the arithmetic below, and are not re-litigated here.

## Expenses Breakdown

- **Total monthly expenses: 6,000.00 PLN/month** (per `requirements.md`).
- `requirements.md` states this as a **single combined figure**, explicitly
  not broken out into fixed vs. variable components ("Monthly expenses:
  6,000 PLN/month (fixed + variable not broken out; taken as a single
  combined figure)"). No further categorization (housing, utilities,
  food, discretionary, etc.) is available from any upstream artifact, so
  none is fabricated here — this is a genuine data gap, noted as a flag
  below rather than assumed away.

| Category | Amount (PLN/month) | Source |
|---|---|---|
| Fixed + variable (combined, not split) | 6,000.00 | `requirements.md` |
| **Total expenses** | **6,000.00** | |

## Disposable Surplus

| Line | Amount (PLN/month) |
|---|---|
| Net income | 8,083.71 |
| − Total expenses | −6,000.00 |
| **= Disposable monthly surplus** | **2,083.71** |

**Disposable surplus ≈ 2,083.71 PLN/month** (≈ 25.8% of net income). The
surplus is positive and not trivially small in PLN terms.

## Flags

1. **Currency mismatch — PLN surplus vs. EUR-denominated goal target
   (explicit, unresolved).** The disposable surplus above is calculated
   entirely in PLN, because income, expenses, and existing savings are all
   stated in PLN in `requirements.md`. The goal itself — 2,000 EUR/month
   passive income by age 55 — is stated in EUR. No artifact in this run
   (`requirements.md`, `net-income.md`, `market-data.md`) provides a sourced,
   cited PLN/EUR exchange rate: `market-data-fetcher` only fetched equity/bond
   benchmark returns (MSCI World, AGG), not an FX rate, and explicitly notes
   in its own file that currency conversion is left to downstream agents.
   Per the no-fabricated-numbers rule, **this artifact does not invent or
   assume a PLN/EUR rate** to translate the 2,083.71 PLN/month surplus (or
   the 50,000 PLN existing savings) into EUR terms, even for illustration.
   **This is a genuine open item that must be resolved with a real, cited
   PLN/EUR exchange rate (via WebSearch or a `finance-math-toolkit` currency
   conversion call) before `retirement-income-planner` and
   `feasibility-assessor` can judge whether this PLN-denominated surplus is
   adequate to reach a EUR-denominated target.** Flagging explicitly rather
   than silently assuming a rate, as instructed.
2. **Surplus adequacy vs. the goal cannot be assessed here.** Because of flag
   #1, this artifact can confirm the surplus is *positive* (2,083.71
   PLN/month) but cannot judge whether it is *adequate* relative to the
   2,000 EUR/month × 20-year passive income target — that comparison
   requires both the missing exchange rate and the compound-growth/safe-
   withdrawal-rate math that belongs to `retirement-income-planner` and
   `feasibility-assessor`, not to `cashflow-analyzer`. Flagged here so it is
   not silently skipped downstream.
3. **Expense figure is unbroken-out (data gap, not blocking).** The 6,000
   PLN/month expense figure is a single combined number with no fixed/
   variable split, as already noted in `requirements.md` and carried forward
   here. This is treated as a data-quality limitation rather than a blocking
   gap, consistent with `requirements.md`'s own characterization, but is
   flagged so `financial-auditor` can decide if it warrants a follow-up
   question to the user.
4. **Net income carries upstream caveats.** `net-income.md` flags that the
   tax regime (ryczałt vs. podatek liniowy vs. skala podatkowa) and ZUS
   relief eligibility (start-up relief windows) were not confirmed by the
   user. If either assumption is wrong, net income — and therefore this
   surplus — would change. Not re-derived here; noted for
   `financial-auditor`'s cross-artifact consistency check.
