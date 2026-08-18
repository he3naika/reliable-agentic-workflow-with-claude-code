---
name: artifact-validator
description: Checks a workflow markdown artifact against the required section structure and citation rules for its type. Use before handing any Personal Finance Goal Planner artifact to the next stage, and to cross-check a whole batch of artifacts together.
---

# Artifact Validator

Checks one or more markdown artifacts from the Personal Finance Goal Planner
workflow against two things: **structure** (required sections present) and
**citation** (every external numeric claim has a real source).

## How to use this skill

1. Read the artifact file(s) you were asked to check.
2. Look up the artifact's type in the table below and get its required
   sections.
3. Check structure: every required section heading must be present and
   non-empty.
4. Check citations: every number that represents an external fact (a tax
   rate, an investment return, a loan interest rate/penalty, an inflation
   rate, a safe-withdrawal-rate assumption) must be immediately followed by
   `(source: <name/URL>, accessed <date>)` or a markdown link plus an access
   date. Numbers that are directly restated from what the user told the
   workflow (their own income, their own expenses, their own debt balance)
   do **not** need a citation — only externally-sourced facts do.
5. Report `PASS` or `FAIL`. On `FAIL`, list every finding as a short,
   specific bullet — name the missing section or the exact uncited claim, not
   a vague "structure looks incomplete."

## Required sections by artifact type

| Artifact filename | Required sections |
|---|---|
| `requirements.md` | Goal Type, Target Parameters, Current Position, Constraints, Confirmed |
| `net-income.md` | Gross Income, Jurisdiction & Contract Type, Taxes/Contributions, Net Income, Sources |
| `market-data.md` | Benchmarks Used, Historical Return, Period, Source & Date Accessed |
| `cashflow.md` | Net Income, Expenses Breakdown, Disposable Surplus, Flags |
| `goal-paths.md` | Goal Summary, Candidate Paths (≥2, each with target/contribution/instruments/timeline), Assumptions & Sources |
| `feasibility.md` | Per-Path Verdict, Supporting Calculation, Ranking |
| `audit-report.md` | Gate Results (one line per gate: PASS/FAIL + finding + attributed agent) |
| `plan.md` / final report | Executive Summary, Current Position, Paths & Verdicts, Recommendation, Action Plan |

If an artifact type isn't in this table, ask the caller which sections are
required instead of guessing.

## Output format

```
PASS
```
or
```
FAIL
1. missing section: Sources
2. uncited claim: "MSCI World ETF, CAGR 15y ≈ 7.2%" has no source
3. uncited claim: "average money-market yield ≈ 3.8%" has no source
```

Keep findings short and mechanically checkable — a coordinator will map each
finding back to the agent that produced it, so vague findings ("looks off")
are not useful.
