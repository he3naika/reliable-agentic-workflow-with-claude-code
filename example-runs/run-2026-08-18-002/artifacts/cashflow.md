# Cashflow Analysis — Personal Finance Goal Planner

## Net Income

- **8,000 BYN/month** — confirmed by the user directly as **net (take-home)**
  income (see `artifacts/requirements.md`, Current Position).
- `income-tax-modeler` was skipped for this run (per confirmed requirements:
  the stated income was already net, no tax/contribution modeling needed on
  top of it). No `net-income.md` artifact exists for this run; the figure
  above is used as-is, unmodified.

## Expenses Breakdown

- **2,537 BYN/month** — stated by the user as a **combined fixed + variable**
  total (see `artifacts/requirements.md`, Current Position: "Monthly expenses
  (fixed + variable)").
- **No category-level breakdown was provided or requested** (e.g. no split
  between housing, utilities, food, transport, discretionary, etc.). This
  analysis does **not** invent a breakdown — the single combined figure above
  is the only expense input available, and it is used as-is.

| Category | Amount (BYN/month) | Source |
|---|---|---|
| Fixed + variable (combined, undifferentiated) | 2,537 | User-stated, `requirements.md` |
| **Total expenses** | **2,537** | |

## Disposable Surplus

```
Disposable surplus = Net income − Fixed expenses − Variable expenses
                    = 8,000 − 2,537  (combined figure; no fixed/variable split available)
                    = 5,463 BYN/month
```

**Disposable monthly surplus: 5,463 BYN/month.**

## Flags

- **No expense category breakdown available.** The user supplied only a
  single combined fixed+variable figure (2,537 BYN/month). This cashflow
  analysis has not fabricated a category split; if downstream agents need
  category-level detail (e.g. to identify cuttable discretionary spend), that
  gap should be surfaced back to the user rather than assumed.
- **Surplus likely insufficient relative to the stated goal — flagged
  explicitly, not softened.** The goal is to accumulate 40,000 USD by
  31 Dec 2026 (~4.5 months from today, 2026-08-18), starting from 0 existing
  savings, with no financing/loan component (per confirmed requirements).
  A precise BYN-denominated gap requires a currency-converted target via
  `finance-math-toolkit` (with a real, cited USD/BYN rate), which is outside
  this agent's scope — but as an order-of-magnitude sanity check: even at a
  generous historical USD/BYN rate, 40,000 USD converts to well over
  100,000 BYN, which against a ~4.5-month horizon implies a required monthly
  contribution far exceeding the 5,463 BYN/month disposable surplus computed
  here (likely by a factor of several times). This strongly suggests the
  stated goal, timeline, and cash-only/no-financing assumption together are
  **not achievable from disposable surplus alone** in the given window.
  This should be treated as a hard flag for `savings-goal-planner` and
  `feasibility-assessor` to confirm precisely (via proper currency conversion
  and required-capital calculation) rather than assumed away, and may need to
  be escalated back to the user (e.g. extend timeline, reduce target price,
  reconsider the no-financing assumption) if confirmed.
- Surplus figure (5,463 BYN/month) assumes the stated income and expenses are
  stable/recurring; no seasonality or one-off items were reported by the
  user.
