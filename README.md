# Personal Finance Goal Planner

A Claude Code agentic workflow: tell it a financial goal (buy an apartment,
buy a car, pay off a debt, build an emergency fund, reach a target passive
income), it gathers your current financial situation, researches real
external data (taxes, loan terms, historical investment returns), and
produces several concrete paths with an honest achievability verdict and a
step-by-step action plan — as `financial-goal-plan.md` / `.html`.

See [CLAUDE.md](./CLAUDE.md) for the full architecture (coordinator,
subagents, quality gates, skills, hooks, MCP integration, retry/resume
rules).

## Prerequisites

- [Claude Code](https://docs.claude.com/en/docs/claude-code) CLI, logged in
- **Python 3.11+** on `PATH` as `python` (used by the hooks, the
  `finance-math-toolkit`/`plan-doc-theme-builder` scripts, and required by
  the Yahoo Finance MCP server)
- [`uv`](https://docs.astral.sh/uv/getting-started/installation/) — used via
  `uvx` to run the Yahoo Finance MCP server without a manual install step
- `git`

No API keys or accounts are required — the MCP server this repo uses wraps
publicly available Yahoo Finance data.

## Setup

```
git clone https://github.com/he3naika/reliable-agentic-workflow-with-claude-code.git
cd reliable-agentic-workflow-with-claude-code
claude
```

On first run, Claude Code will pick up `.mcp.json` and may ask you to approve
starting the `yahoo-finance` MCP server — approve it. It will also load
`.claude/settings.json` (hooks), `.claude/agents/`, `.claude/skills/`,
`.claude/commands/`, and `CLAUDE.md` automatically — nothing else to
configure.

## Running

Inside the Claude Code session:

```
/plan-financial-goal I want to pay off a $8000 credit card debt at 14% APR as fast as possible. Income $3000/mo, expenses $1800/mo.
```

The coordinator will:
1. Ask any missing questions and confirm what it understood before doing
   anything else.
2. Run only the subagents relevant to your goal (e.g. it skips tax/investment
   research entirely for a simple debt payoff).
3. Show you a draft plan and ask for approval — reply `approve` or
   `revise: <what to change>`.
4. Write the final report only after you approve.

Each run creates its own directory under `runs/run-<date>-<n>/` with every
intermediate artifact, `workflow-state.json`, and the final
`financial-goal-plan.md` / `.html`. `runs/` is gitignored (it's your own
financial data, not repo content) — nothing is checked in, but after a few
runs you'll accumulate examples of different goal types locally, including
ones that hit a gate retry or a market-data MCP fallback to WebSearch.

## Resuming an interrupted run

If a run is interrupted (closed terminal, crash) before it finishes:

```
/plan-financial-goal --resume run-2026-08-18-001
```

The coordinator reads that run's `workflow-state.json` and continues from the
first stage that isn't `completed` — nothing already done gets recomputed.

## Secrets

None are required for this repo as shipped. `.gitignore` already excludes
`.env`/`.env.*` for if a future MCP integration needs a key — should that
happen, document the required variable name here and load it from `.env`,
never commit the value itself.

## Repository/branching conventions

`main` is protected — no direct commits, changes go through a pull request
from a `feature/*`-named branch (enforced by
`.github/workflows/branch-name-check.yml`).
