---
name: plan-doc-theme-builder
description: Provides the canonical section skeleton for Personal Finance Goal Planner documents and deterministically renders an approved plan.md into styled HTML. Use when assembling plan.md (for the skeleton) and when rendering the final approved report (for the HTML).
---

# Plan Doc Theme Builder

Keeps every run's final document structurally identical and visually
consistent, and renders HTML with a script instead of asking the model to
hand-write markup — so the same markdown input always produces the same
layout.

## For `plan-builder`: assembling `plan.md`

Read `references/template.md` and follow its section skeleton exactly:
Executive Summary → Current Position → Paths Considered → Verdict →
Recommendation → Action Plan. Do not add extra top-level sections and do not
skip one — `financial-auditor`'s structural gate checks against this same
skeleton.

## For `report-builder`: rendering the final HTML

Once `plan.md` is approved, render it with the script — do not write HTML by
hand:
```
python scripts/render_html.py --input plan.md --output financial-goal-plan.html --title "Financial Goal Plan"
```
The script supports the markdown subset actually used in `plan.md`: `#`/`##`/`###`
headings, paragraphs, `- ` lists, GFM pipe tables, `**bold**`, `*italic*`,
`[text](url)` links, and `---` horizontal rules. It embeds a self-contained
light/dark theme — no external stylesheet or network request.

The approved `plan.md` itself is also copied/renamed to
`financial-goal-plan.md` as the Markdown deliverable — both formats come from
the same approved source, so they can never drift apart.
