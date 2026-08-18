#!/usr/bin/env python3
"""PreToolUse hook: blocks internal artifact/agent names leaking into the final report.

Only acts on Write/Edit calls whose target is the final report
(financial-goal-plan.md / .html). Scans the content about to be written for
internal agent names, internal artifact filenames, and internal status
markers used in agent handoff text — none of that belongs in user-facing
output.
"""
import json
import re
import sys

FINAL_REPORT_PATTERN = re.compile(r"financial-goal-plan\.(md|html)$")

INTERNAL_AGENT_NAMES = [
    "requirements-formalizer", "income-tax-modeler", "market-data-fetcher",
    "cashflow-analyzer", "savings-goal-planner", "debt-payoff-planner",
    "retirement-income-planner", "feasibility-assessor", "financial-auditor",
    "plan-builder", "report-builder",
]
INTERNAL_ARTIFACT_NAMES = [
    "requirements.md", "net-income.md", "market-data.md", "cashflow.md",
    "goal-paths.md", "feasibility.md", "audit-report.md", "plan.md",
    "workflow-state.json",
]
INTERNAL_MARKERS = ["STATUS:", "SELF-CHECK:", "ARTIFACT:", "NEEDS:"]

LEAK_PATTERNS = [
    re.compile(re.escape(token), re.IGNORECASE)
    for token in INTERNAL_AGENT_NAMES + INTERNAL_ARTIFACT_NAMES + INTERNAL_MARKERS
]


def deny(reason: str) -> None:
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        }
    }))
    sys.exit(0)


def allow() -> None:
    sys.exit(0)


def main() -> None:
    payload = json.load(sys.stdin)
    if payload.get("tool_name") not in ("Write", "Edit"):
        allow()
        return

    tool_input = payload.get("tool_input", {})
    file_path = tool_input.get("file_path", "")
    if not FINAL_REPORT_PATTERN.search(file_path):
        allow()
        return

    content = tool_input.get("content") or tool_input.get("new_string") or ""
    hits = sorted({pattern.pattern for pattern in LEAK_PATTERNS if pattern.search(content)})
    if hits:
        deny(
            "Internal artifact name(s)/marker(s) found in final report content: "
            f"{', '.join(hits)}. Rewrite using the plan-doc-theme-builder template only — "
            "no internal agent or artifact names in user-facing output."
        )
        return

    allow()


if __name__ == "__main__":
    main()
