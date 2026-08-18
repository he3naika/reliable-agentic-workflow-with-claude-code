#!/usr/bin/env python3
"""PostToolUse hook: updates workflow-state.json after any artifact/report write.

Only acts on Write/Edit calls whose target is a known workflow artifact
(under a run's artifacts/ directory) or the final report. Marks the
corresponding stage as completed with its artifact path and a timestamp,
merging into whatever workflow-state.json already contains (goal_type,
approval, gate_retries, etc. are left untouched). This is what makes
--resume possible: the coordinator reads this file and skips completed
stages.
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ARTIFACT_TO_STAGE = {
    "requirements.md": "requirements-formalizer",
    "net-income.md": "income-tax-modeler",
    "market-data.md": "market-data-fetcher",
    "cashflow.md": "cashflow-analyzer",
    "goal-paths.md": "goal-path-planner",
    "feasibility.md": "feasibility-assessor",
    "audit-report.md": "financial-auditor",
    "plan.md": "plan-builder",
    "financial-goal-plan.md": "report-builder",
    "financial-goal-plan.html": "report-builder",
}


def find_run_dir(path: Path):
    if path.name in ("financial-goal-plan.md", "financial-goal-plan.html"):
        return path.parent
    if path.parent.name == "artifacts":
        return path.parent.parent
    return None


def main() -> None:
    payload = json.load(sys.stdin)
    if payload.get("tool_name") not in ("Write", "Edit"):
        sys.exit(0)

    tool_input = payload.get("tool_input", {})
    file_path_str = tool_input.get("file_path", "")
    if not file_path_str:
        sys.exit(0)

    file_path = Path(file_path_str)
    stage = ARTIFACT_TO_STAGE.get(file_path.name)
    if stage is None:
        sys.exit(0)

    run_dir = find_run_dir(file_path)
    if run_dir is None:
        sys.exit(0)

    state_path = run_dir / "workflow-state.json"
    state = {}
    if state_path.exists():
        try:
            state = json.loads(state_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            state = {}

    try:
        artifact_rel = str(file_path.relative_to(run_dir))
    except ValueError:
        artifact_rel = str(file_path)

    state.setdefault("stages", {})
    state["stages"][stage] = {
        "status": "completed",
        "artifact": artifact_rel,
        "updated_at": datetime.now(timezone.utc).isoformat(),
    }

    state_path.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")
    sys.exit(0)


if __name__ == "__main__":
    main()
