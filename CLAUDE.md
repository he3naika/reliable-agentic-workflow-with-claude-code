# Personal Finance Goal Planner — Reliable Agentic Workflow

A Claude Code multi-agent workflow that takes a personal financial goal (buy an
apartment, buy a car, pay off a debt, build an emergency fund, reach a target
passive income), gathers the user's current financial situation, and produces
several concrete paths to the goal with an honest achievability verdict and a
step-by-step action plan.

Entry point: the `/plan-financial-goal` slash command
(`.claude/commands/plan-financial-goal.md`).

## Design principles

- **Coordinator does no financial reasoning.** All domain content is produced
  by subagents. The coordinator gathers requirements, decides which subagents
  to run, enforces quality gates and human approval, and persists/resumes
  state.
- **Files are the source of truth, not chat text.** Every subagent writes a
  markdown artifact to disk. A subagent's returned text is only a short status
  signal (`STATUS: success|failed`, artifact path, notes) — the coordinator
  always reads the actual artifact file when it needs the content.
- **No fabricated numbers.** Every external figure (tax rate, investment
  return, loan terms) must carry a real source and access date. This is
  enforced by a quality gate, not just requested in a prompt.
- **Deterministic math, not LLM arithmetic.** Compound growth, safe withdrawal
  capital, amortization, and currency conversion are computed by
  `finance-math-toolkit` scripts, not estimated in prose.

## Execution flow

```
requirements-formalizer
  → [income-tax-modeler, market-data-fetcher]   (parallel, run only if relevant to the goal)
  → cashflow-analyzer
  → goal-path-planner                            (exactly one of: savings-goal-planner,
                                                    debt-payoff-planner, retirement-income-planner)
  → feasibility-assessor
  → financial-auditor                            (quality gates; targeted retry, max 3 attempts)
  → plan-builder
  → human approval                               (revision loop on reject)
  → report-builder
```

`income-tax-modeler` and `market-data-fetcher` are skipped when the goal
doesn't need them (e.g. a pure debt-payoff goal with no investment
component). This is decided by the coordinator from the confirmed goal type.

## Subagents (11)

| Agent | Responsibility | Depends on |
|---|---|---|
| `requirements-formalizer` | Formalizes the goal + current situation via adaptive Q&A; confirms requirements back to the user before execution starts | — |
| `income-tax-modeler` | Computes net income after taxes/social contributions for the user's jurisdiction and contract type, via WebSearch | requirements-formalizer |
| `market-data-fetcher` | Historical returns for benchmark instruments via the Yahoo Finance MCP, WebSearch fallback on MCP failure | requirements-formalizer |
| `cashflow-analyzer` | Disposable monthly surplus (net income − expenses) | income-tax-modeler, market-data-fetcher |
| `savings-goal-planner` | Paths for "accumulate a target sum by a date" goals: apartment down payment, car purchase, emergency fund | cashflow-analyzer |
| `debt-payoff-planner` | Paths for paying off an existing debt; researches lender/product terms (rate, prepayment penalty) via WebSearch, escalates to the user only what research couldn't find | cashflow-analyzer |
| `retirement-income-planner` | Paths for a target passive income by a target age (safe withdrawal rate + compound growth) | cashflow-analyzer |
| `feasibility-assessor` | Quantitative achievable/not-achievable verdict per path, with supporting calculation | goal-path-planner |
| `financial-auditor` | Runs quality gates: structure/citation check + **independent recomputation** of every numeric claim + cross-artifact consistency | feasibility-assessor |
| `plan-builder` | Merges validated artifacts into the final structured plan (5 required output fields) | financial-auditor (pass) |
| `report-builder` | Renders the approved plan to `.md` + `.html` via `plan-doc-theme-builder` | human approval |

Exactly one of `savings-goal-planner` / `debt-payoff-planner` /
`retirement-income-planner` runs per invocation, selected by confirmed goal
type.

## Required output fields (enforced by gates)

Every final plan must contain, per recommended path:
1. **Target capital/amount** required
2. **Monthly contribution** needed
3. **Where to invest/allocate** — concrete instruments, not vague advice
4. **Timeline** — phased/step-by-step
5. **Verdict** — achievable or not, with reasoning

## Quality gates (`financial-auditor`)

1. All 5 required output fields are present.
2. Verdict is mathematically consistent — **independently recomputed** via `finance-math-toolkit`, not just read and trusted.
3. Net income accounts for every tax/contribution the user stated.
4. Every external figure has a real cited source + access date.
5. At least 2 candidate paths per goal.
6. No vague recommendations — concrete amounts/instruments/timelines only.
7. Currency consistency; conversions are explicit.
8. Every confirmed requirement/constraint is reflected in the output.
9. Loan terms (rate, type, prepayment penalty) are sourced via research or explicitly confirmed by the user — never assumed.

On failure: only the attributed agent is retried (max 3 attempts per artifact,
tracked in `workflow-state.json`). If the failing artifact's output changed,
any downstream artifact that already consumed the stale version is marked
`stale` and regenerated too. If a gate is still failing after 3 attempts, the
coordinator stops before `plan-builder`/`report-builder` and reports the exact
gate, artifact, and finding to the user instead of continuing with bad data.

## Skills (`.claude/skills/`)

- **`artifact-validator`** — structural + citation checklist per artifact
  type. Used by every producing agent (self-check) and by
  `financial-auditor` (cross-artifact check).
- **`finance-math-toolkit`** — deterministic calculations
  (`scripts/calc.py`: future value, required capital via safe withdrawal
  rate, amortization, currency conversion). Used by the goal-path-planner
  agents, `feasibility-assessor`, and `financial-auditor` (to recompute and
  verify, not just read).
- **`plan-doc-theme-builder`** — canonical section skeleton
  (`references/template.md`) and deterministic markdown→HTML rendering
  (`scripts/render_html.py`). Used by `plan-builder` (skeleton) and
  `report-builder` (final render).

## Hooks (`.claude/hooks/`, Python)

- **PreToolUse — `approval_gate_guard.py`**: blocks writing the final report
  (`financial-goal-plan.md` / `.html`) unless `workflow-state.json` in the
  same run directory has `approval.status == "approved"`.
- **PreToolUse — `no_leak_guard.py`**: blocks writing the final report if its
  content contains internal artifact filenames, internal agent names, or
  internal status markers (`STATUS:`, `SELF-CHECK:`).
- **PostToolUse — `post_write_state.py`**: after any artifact write, updates
  `workflow-state.json` for that run — stage status, artifact path,
  timestamp. This is what makes resume possible.

Both are wired in `.claude/settings.json`.

## MCP

Two community MCP servers, both configured in `.mcp.json`, both used by
`market-data-fetcher` for historical instrument returns:

- `yahoo-finance` (`Alex2Yang97/yahoo-finance-mcp`, wraps public `yfinance`
  data — no API key) — primary source.
- `tradingview` (`atilaahmettaner/tradingview-mcp`, public TradingView
  endpoints — no API key/account) — secondary source, genuinely independent
  of Yahoo Finance's data pipeline rather than another client for the same
  upstream API.

`market-data-fetcher` tries each source up to 3 times before moving to the
next: `yahoo-finance` (3 attempts) → `tradingview` (3 attempts) → WebSearch
for the same benchmark figures with a cited source. It never fabricates a
number, and records in `market-data.md` which of the three tiers actually
produced each figure.

## Run directory layout & state

Each invocation creates `runs/<run-id>/` (e.g. `runs/run-2026-08-18-001/`):
```
runs/<run-id>/
├── workflow-state.json
├── artifacts/
│   ├── requirements.md
│   ├── net-income.md              (if income-tax-modeler ran)
│   ├── market-data.md             (if market-data-fetcher ran)
│   ├── cashflow.md
│   ├── goal-paths.md
│   ├── feasibility.md
│   ├── audit-report.md
│   └── plan.md
├── financial-goal-plan.md          (written only after approval)
└── financial-goal-plan.html        (written only after approval)
```

`workflow-state.json` shape:
```json
{
  "run_id": "run-2026-08-18-001",
  "goal_type": "passive_income",
  "requirements_confirmed": true,
  "stages": {
    "requirements-formalizer": {"status": "completed", "artifact": "artifacts/requirements.md", "updated_at": "..."}
  },
  "gate_retries": {"feasibility-assessor": 1},
  "approval": {"status": "pending", "feedback": null},
  "progress": {
    "steps": [
      {"key": "requirements-formalizer", "label": "Formalize requirements", "status": "completed"},
      {"key": "income-tax-modeler", "label": "Model net income", "status": "completed"},
      {"key": "market-data-fetcher", "label": "Fetch market data", "status": "completed"},
      {"key": "cashflow-analyzer", "label": "Analyze cashflow", "status": "in_progress"},
      {"key": "goal-path-planner", "label": "Build candidate paths", "status": "pending"},
      {"key": "feasibility-assessor", "label": "Assess feasibility", "status": "pending"},
      {"key": "financial-auditor", "label": "Run quality audit", "status": "pending"},
      {"key": "plan-builder", "label": "Assemble plan", "status": "pending"},
      {"key": "human-approval", "label": "Wait for your approval", "status": "pending"},
      {"key": "report-builder", "label": "Generate final report", "status": "pending"}
    ],
    "current_index": 3,
    "total": 10
  }
}
```

## Progress reporting

`progress.steps` is the fixed, ordered list of steps **this specific run**
will go through — decided once, right after step 2 of the coordinator
(deciding which of `income-tax-modeler`/`market-data-fetcher` are needed),
and written to `workflow-state.json` before the pipeline starts. Steps for
agents that were skipped (e.g. a debt-payoff run skipping
`income-tax-modeler`) are simply not included, so `total` reflects only what
this run will actually do.

Before invoking the agent/step for each entry, the coordinator posts a short
one-line progress banner to the user, e.g. `Step 4 of 8: Analyzing cashflow`,
and updates that step's `status` (`pending` → `in_progress` → `completed`) in
`workflow-state.json`. A `financial-auditor` retry loop does not consume
additional steps — it stays on the same `financial-auditor` step entry, with
the banner noting the attempt number (e.g. `Step 6 of 8: Running quality
audit (attempt 2 of 3)`). A `revise:` loop at the human-approval step
similarly re-runs earlier step entries in place (their `status` moves back to
`in_progress` then `completed` again) rather than adding new steps or
changing `total`.

On `--resume`, the coordinator reads `progress` and reports `current_index`/
`total` directly instead of recomputing it, so the user immediately sees
where the run stands.

## Resume

`/plan-financial-goal --resume <run-id>` reads `runs/<run-id>/workflow-state.json`
and skips every stage already `completed`, continuing from the first
`pending`/`failed` stage. Nothing already-done is recomputed.

## Human approval

The coordinator presents a short summary drawn from `artifacts/plan.md` and
waits for `approve` or `revise: <feedback>`. On `revise`, only the affected
upstream agents are re-run (typically `goal-path-planner` →
`feasibility-assessor` → `plan-builder`), not the whole pipeline. The final
report can only be written once `approval.status` is `approved` —
enforced by `approval_gate_guard.py`, not by convention.

## Tech stack

- Agents, coordinator, skills: Claude Code native primitives (markdown +
  frontmatter). Not a programming language.
- Hooks and `finance-math-toolkit`/`plan-doc-theme-builder` scripts: Python
  (stdlib only, no extra dependencies for hooks).

## Git workflow for this repository

- `main` is protected: no direct commits, changes only via pull request.
- Every change lives on a `feature/*` branch; a CI check
  (`.github/workflows/branch-name-check.yml`) fails any PR whose source
  branch doesn't match `feature/*`.
