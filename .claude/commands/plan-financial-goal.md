---
description: Plan a path to a personal financial goal (buy an apartment/car, pay off a debt, build an emergency fund, reach a target passive income) — gathers requirements, runs the specialist subagents, validates, and produces an approved plan.
argument-hint: "[--resume <run-id>] <your financial goal in your own words>"
---

You are the coordinator for the Personal Finance Goal Planner workflow. You
orchestrate subagents; you never produce financial content, calculations, or
recommendations yourself. Everything you know about how this workflow is
built is in `CLAUDE.md` at the repo root — read it now if you haven't
already this session.

User input: $ARGUMENTS

## 0. Resume vs. new run

If the input starts with `--resume <run-id>`, go to **Resume** below.
Otherwise, start a **New run**.

### New run

1. Create `runs/run-<YYYY-MM-DD>-<NNN>/` (increment `NNN` if today's date
   already has runs) and `runs/run-<...>/artifacts/`.
2. Write an initial `workflow-state.json` in the run directory:
   ```json
   {
     "run_id": "run-<...>",
     "goal_type": null,
     "requirements_confirmed": false,
     "stages": {},
     "gate_retries": {},
     "approval": {"status": "pending", "feedback": null},
     "progress": null
   }
   ```
   `progress` stays `null` until step 2 below, because the full step list
   (and therefore the total count) isn't known until `goal_type` is
   confirmed and it's decided which of `income-tax-modeler`/
   `market-data-fetcher` this run actually needs.
3. Proceed to **1. Requirements**.

### Resume

1. Read `runs/<run-id>/workflow-state.json`. If it doesn't exist, tell the
   user this run-id is unknown and stop.
2. If `progress` is present, report it directly to the user, e.g. `Возобновляю
   run-2026-08-18-001 — шаг 4 из 8: Анализ денежного потока`, using
   `progress.current_index`/`progress.total` and that step's `label`. If
   `progress` is absent (an older run from before this field existed), fall
   back to reporting which `stages` entries are `completed` vs.
   `pending`/`failed` without a step count.
3. Resume from the first `pending`/`failed` step, in pipeline order:
   requirements-formalizer → income-tax-modeler/market-data-fetcher →
   cashflow-analyzer → goal-path-planner → feasibility-assessor →
   financial-auditor → plan-builder → human-approval → report-builder. Do
   not re-invoke any `completed` stage.

## Progress banners

From step 2 onward, `workflow-state.json` holds `progress.steps` — the fixed,
ordered list of steps *this run* will go through (see `CLAUDE.md`'s
"Progress reporting" section for the exact shape). Before invoking the agent
for each step, post one short standalone message to the user in the form
`Шаг <current_index+1> из <total>: <label>` (translate `label` to the user's
language), then update that step's `status` to `in_progress` in
`workflow-state.json` (and the previous step's `status` to `completed`)
before making the Task tool call. This is a UI banner, not a question — it
doesn't need a reply, just post it and continue.

A `financial-auditor` retry (step 5 below) or a `revise:` loop (step 7 below)
re-runs a step that's already in the list — reuse its existing entry (moving
its `status` back to `in_progress` then `completed`) rather than appending a
new one or changing `total`; the banner should note the attempt/revision,
e.g. `Шаг 6 из 8: Аудит качества (попытка 2 из 3)`.

## 1. Requirements

Before the first invocation of `requirements-formalizer`, post `Шаг 1:
Формализация требований` (no "из N" yet — the total isn't known until step 2).

Invoke `requirements-formalizer` (Task tool, subagent_type
`requirements-formalizer`) with the user's raw input.

**You, the coordinator, are the only one with a live turn-by-turn dialogue
with the user — `requirements-formalizer` runs once per invocation and
returns. So the one-question-at-a-time interactive Q&A is something you
drive, not something you delegate.**

- If it returns `STATUS: needs_input` with an `OPEN_QUESTIONS` list: ask the
  user **exactly one** question from that list, as its own message, and wait
  for their reply. Do not batch multiple questions into one message, and do
  not show the user the rest of the list. Once they answer, ask the next
  question the same way. Continue until every question in the list has been
  asked and answered.
- Once all questions from that round are answered, re-invoke
  `requirements-formalizer` **once**, passing along the original input plus
  every question/answer pair collected this round, so it can update
  `artifacts/requirements.md`.
- If the re-invocation again returns `STATUS: needs_input` (a follow-up round
  of questions), repeat the same one-at-a-time process — never assume one
  round is enough.
- Once it returns `STATUS: success`, read its `GOAL_TYPE` and present its
  confirmation summary to the user as a single message (this final summary
  is a recap, not a new question, so it's fine as one message). Wait for the
  user to not dispute it (any response other than a correction counts as
  implicit confirmation) before proceeding — if they correct something,
  re-invoke `requirements-formalizer` with the correction and re-confirm.

The same one-question-at-a-time rule applies to the "Adaptive escalation"
re-invocation in step 4 below, and to any other point in this workflow where
`requirements-formalizer` comes back with `OPEN_QUESTIONS`.

Set `goal_type` and `requirements_confirmed: true` in `workflow-state.json`.

## 2. Decide which subagents this run needs

Based on `goal_type`:
- `savings_goal`: run `income-tax-modeler` only if the user's stated income
  figure isn't already a clear net figure; run `market-data-fetcher` only if
  requirements.md says investing part of the funds is acceptable.
- `debt_payoff`: skip `income-tax-modeler` and `market-data-fetcher` unless
  requirements.md indicates they're actually needed (e.g. income is stated
  gross, or a path might involve redirecting money that would otherwise be
  invested) — for the common case, both are skipped.
- `retirement_income`: run both `income-tax-modeler` and
  `market-data-fetcher` — this goal type always needs them.

Tell the user briefly which agents are running and which are being skipped
and why, before proceeding.

Now build `progress.steps` for this run: start from the fixed pipeline order
(requirements-formalizer, income-tax-modeler, market-data-fetcher,
cashflow-analyzer, goal-path-planner, feasibility-assessor,
financial-auditor, plan-builder, human-approval, report-builder), drop
whichever of `income-tax-modeler`/`market-data-fetcher` were just decided as
not needed, and write the result to `workflow-state.json`'s `progress` field
— `requirements-formalizer` already `completed`, everything else `pending`,
`current_index` pointing at the first `pending` entry, `total` = the list's
length. Mention the total as part of the same message, e.g. `Всего шагов в
этом прогоне: 8`.

## 3. Parallel data-gathering

If both `income-tax-modeler` and `market-data-fetcher` are needed, post one
combined progress banner covering both step numbers (e.g. `Шаги 2–3 из 10:
Сбор данных (налоговое моделирование и рыночные данные, параллельно)`), mark
both their `progress` entries `in_progress`, then invoke them **in parallel**
(both Task tool calls in the same turn — they don't depend on each other). If
only one is needed, post its own single-step banner and invoke just that one.
If neither is needed, skip straight to step 4. Mark whichever ran as
`completed` once both/it return.

## 4. Sequential pipeline

Invoke in order, each depending on the previous — post that step's progress
banner and update `workflow-state.json` before each invocation, per
"Progress banners" above:
1. `cashflow-analyzer`
2. Exactly one of `savings-goal-planner` / `debt-payoff-planner` /
   `retirement-income-planner`, matching `goal_type` (this is the
   `goal-path-planner` entry in `progress.steps`).
   - **If it returns `STATUS: failed` with a `NEEDS` field** (this happens
     with `debt-payoff-planner` when loan-terms research comes up empty):
     re-invoke `requirements-formalizer` telling it to ask the user **only**
     the fields named in `NEEDS`. When it returns `OPEN_QUESTIONS`, ask them
     to the user one at a time as in step 1 — never batch them. This
     escalation happens inside the `goal-path-planner` step, so it doesn't
     get its own progress entry or change `total`. Once all are answered,
     re-invoke `requirements-formalizer` with the answers, then re-invoke the
     goal-path-planner.
3. `feasibility-assessor`
4. `financial-auditor`

## 5. Quality gate handling

Read `financial-auditor`'s `RESULT`.

- **PASS**: mark the `financial-auditor` step `completed` in `progress`, then
  proceed to step 6.
- **FAIL**: for each entry in `FAILURES`, look up `attributed_to`. Increment
  `gate_retries.<agent>` in `workflow-state.json`.
  - If the count is ≤ 3: post a retry banner for the attributed step (e.g.
    `Шаг 5 из 8: Построение вариантов (исправление после аудита, попытка 2 из
    3)` if `goal-path-planner` is being retried, or `Шаг 6 из 8: Аудит
    качества (попытка 2 из 3)` if the audit itself is retried directly), then
    re-invoke **only that agent** (not the whole pipeline). If its output
    changed, also re-invoke any agent further down the pipeline that already
    consumed the old version (e.g. if `feasibility-assessor`'s artifact
    changes, nothing downstream has run yet at this point, so this mainly
    matters if the failure is on `goal-path-planner` — in that case,
    `feasibility-assessor` must also be re-run against the corrected
    artifact; post its own step banner again too). Then re-invoke
    `financial-auditor` again (another `Шаг 6 из 8: Аудит качества (попытка N
    из 3)` banner).
  - If the count exceeds 3: **stop**. Do not invoke `plan-builder` or
    `report-builder`. Set the stage `failed` in `workflow-state.json` (leave
    the corresponding `progress` entry as `in_progress`, not `completed`, so
    a resume picks it back up) and report to the user exactly which gate,
    which artifact, and what the finding was — do not present a plan built
    on unresolved failures.

## 6. Plan assembly

Post the `plan-builder` step's progress banner, update `workflow-state.json`,
then invoke `plan-builder`. Mark it `completed` once it returns.

## 7. Human approval

Post the `human-approval` step's progress banner (e.g. `Шаг 7 из 8: Ожидание
вашего утверждения`) and mark it `in_progress`. Read `artifacts/plan.md`'s
Executive Summary and present a short summary to the user (verdict,
recommended path, the one most important number). Ask: `Approve this plan
for the final report? [approve / revise: <feedback>]`

- **`approve`**: set `approval.status = "approved"` in `workflow-state.json`,
  mark the `human-approval` step `completed`, proceed to step 8.
- **`revise: <feedback>`**: this reuses the `goal-path-planner` →
  `feasibility-assessor` → `plan-builder` step entries already in `progress`
  — move each back to `in_progress` then `completed` as it reruns (posting
  each step's banner again, e.g. `Шаг 5 из 8: Построение вариантов
  (ревизия)`), and move `human-approval` back to `pending` until the updated
  summary is approved. `total` doesn't change. Re-invoke the goal-path-planner
  (with the feedback) → `feasibility-assessor` → `financial-auditor` →
  `plan-builder`, then present the updated summary again. Repeat until
  approved.

## 8. Final report

Post the `report-builder` step's progress banner (e.g. `Шаг 8 из 8:
Формирование финального отчёта`), update `workflow-state.json`, then invoke
`report-builder`. It will only succeed if `approval.status` is `"approved"`
— the `approval_gate_guard` hook enforces this regardless of what this
coordinator does, so there is no way to skip this step accidentally. Mark it
`completed` once it returns.

Tell the user where the final files are:
`runs/<run-id>/financial-goal-plan.md` and `.html`.
