#!/usr/bin/env python3
"""PreToolUse hook: blocks writing the final report before human approval.

Reads the PreToolUse JSON payload from stdin. Only acts on Write/Edit calls
whose target is the final report (financial-goal-plan.md / .html). Looks for
workflow-state.json in the same run directory and requires
approval.status == "approved" before allowing the write.
"""
import json
import re
import sys
from pathlib import Path

FINAL_REPORT_PATTERN = re.compile(r"financial-goal-plan\.(md|html)$")


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

    file_path = payload.get("tool_input", {}).get("file_path", "")
    if not FINAL_REPORT_PATTERN.search(file_path):
        allow()
        return

    run_dir = Path(file_path).resolve().parent
    state_path = run_dir / "workflow-state.json"
    if not state_path.exists():
        deny(f"No workflow-state.json found in {run_dir} — cannot verify human approval.")
        return

    try:
        state = json.loads(state_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        deny(f"workflow-state.json in {run_dir} is not valid JSON — cannot verify human approval.")
        return

    approval_status = state.get("approval", {}).get("status")
    if approval_status != "approved":
        deny(
            "Human approval required before writing the final report. "
            f"Current approval status: {approval_status!r}. "
            "Present the draft plan to the user and obtain explicit approval first."
        )
        return

    allow()


if __name__ == "__main__":
    main()
