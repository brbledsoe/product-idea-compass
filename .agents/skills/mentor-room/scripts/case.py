"""Initialize and structurally check durable mentor-room cases (stdlib only)."""
import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1]


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def library(name):
    return read(SKILL / "references" / name)


def initialize(directory, title):
    if directory.exists():
        raise ValueError("Case directory already exists; resume it or choose a new ID")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", directory.name):
        raise ValueError("Use a lowercase hyphenated case directory ID")
    core = library("core.json")
    catalog = library("catalog.json")
    record = {
        "schema_version": 1,
        "id": directory.name,
        "title": title,
        "created": datetime.now(timezone.utc).isoformat(),
        "core_version": core["version"],
        "lifecycle": "active",
        "scope": {"revision": 1, "audience": None, "context": None,
                  "ambition": None, "success_criteria": [],
                  "next_investment": None, "constraints": []},
        "hypotheses": [], "evidence": [], "experiments": [], "artifacts": [],
        "core": [{"id": a["id"], "state": "unassessed", "artifact_ids": [],
                  "check": "", "adaptation": "", "reviewer": "", "date": ""}
                 for a in core["activities"]],
        "resources": [{"id": r["id"], "state": "unassessed", "reason": "",
                       "references": []} for r in catalog["resources"]],
        "components": [], "decisions": [], "sessions": [],
        "next_action": {"owner": "facilitator", "action": "Establish the idea scope",
                        "inputs": "User's rough idea and existing work",
                        "deliverable": "Provisional scope and next session",
                        "completion_check": "User intent and unknowns are recorded",
                        "resume_trigger": "User describes the idea"},
    }
    directory.mkdir(parents=True)
    (directory / "artifacts").mkdir()
    (directory / "sessions").mkdir()
    (directory / "case.json").write_text(
        json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (directory / "core-baseline.json").write_text(
        json.dumps(core, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return {"created": str(directory / "case.json"), "core_version": core["version"]}


def check(directory, decision=False):
    case = read(directory / "case.json")
    snapshot = directory / "core-baseline.json"
    baseline = read(snapshot) if snapshot.is_file() else library("core.json")
    catalog = library("catalog.json")
    errors = []

    def require(condition, message):
        if not condition:
            errors.append(message)

    def items(field):
        value = case.get(field, [])
        require(isinstance(value, list), f"{field} must be a list")
        return value if isinstance(value, list) else []

    def indexed(field):
        result = {}
        for row in items(field):
            if not isinstance(row, dict) or not row.get("id"):
                errors.append(f"{field} entry lacks an ID")
                continue
            key = row["id"]
            require(key not in result, f"Duplicate {field} ID: {key}")
            result[key] = row
        return result

    def local_file(relative, label):
        if not isinstance(relative, str) or not relative:
            errors.append(f"{label} needs a relative file path")
            return
        path = Path(relative)
        target = (directory / path).resolve()
        require(not path.is_absolute() and target.is_relative_to(directory.resolve()),
                f"{label} path must stay within its case")
        require(target.is_file(), f"{label} file missing: {relative}")

    require(case.get("schema_version") == 1, "Unsupported case schema")
    require(case.get("core_version") == baseline["version"],
            "Pinned baseline differs from its snapshot (or current baseline for a legacy case); review migration explicitly")
    require(case.get("lifecycle") in {"active", "paused", "stopped", "reviewed"},
            "Invalid lifecycle")
    artifacts = indexed("artifacts")
    evidence = indexed("evidence")
    hypotheses = indexed("hypotheses")
    experiments = indexed("experiments")
    components = indexed("components")
    for aid, artifact in artifacts.items():
        local_file(artifact.get("path"), f"Artifact {aid}")
    for eid, row in evidence.items():
        for key in ("kind", "source", "observation", "audience", "context", "date"):
            require(bool(row.get(key)), f"Evidence {eid} lacks {key}")
        for hid in row.get("claim_ids", []):
            require(hid in hypotheses, f"Evidence {eid} refers to missing hypothesis {hid}")
    for field, rows in (("Hypothesis", hypotheses), ("Experiment", experiments),
                        ("Component", components)):
        for rid, row in rows.items():
            for eid in row.get("evidence_ids", []):
                require(eid in evidence, f"{field} {rid} refers to missing evidence {eid}")
    for xid, row in experiments.items():
        require(row.get("claim_id") in hypotheses, f"Experiment {xid} needs an existing claim_id")
        require(row.get("stage") in {"backlog", "setup", "run", "learn"},
                f"Experiment {xid} has invalid stage")
        if row.get("stage") in {"run", "learn"}:
            for key in ("metric", "criteria", "audience", "context", "owner"):
                require(bool(row.get(key)), f"Experiment {xid} lacks {key}")
        if row.get("stage") == "learn":
            require(bool(row.get("evidence_ids")), f"Experiment {xid} has no evidence to learn from")
    activities = {a["id"]: a for a in baseline["activities"]}
    coverage = indexed("core")
    require(set(coverage) == set(activities), "Core activity IDs must exactly match pinned baseline")
    complete = set()
    adapted = []
    for cid, row in coverage.items():
        row_error_count = len(errors)
        state = row.get("state")
        require(state in {"unassessed", "pending", "done", "credited", "adapted", "considered"},
                f"Invalid state for {cid}")
        if state in {"done", "credited", "adapted", "considered"}:
            require(bool(row.get("check")), f"{cid} needs a substantive completion/applicability check")
            require(bool(row.get("reviewer")) and bool(row.get("date")), f"{cid} needs reviewer/date")
            if state == "considered":
                require(activities.get(cid, {}).get("conditional") is True,
                        f"Mandatory activity {cid} cannot be merely considered")
            else:
                require(bool(row.get("artifact_ids")), f"{cid} needs inspected artifact IDs")
            for prerequisite in activities.get(cid, {}).get("requires", []):
                require(coverage.get(prerequisite, {}).get("state") in {"done", "credited", "adapted"},
                        f"{cid} requires completed {prerequisite}; an initial plan is not a post-study result")
            if state == "adapted":
                require(bool(row.get("adaptation")), f"{cid} needs adaptation and inference limits")
                adapted.append(cid)
            if len(errors) == row_error_count:
                complete.add(cid)
        for aid in row.get("artifact_ids", []):
            require(aid in artifacts, f"{cid} refers to missing artifact {aid}")
    resources = indexed("resources")
    require(set(resources) == {r["id"] for r in catalog["resources"]},
            "Resource IDs must account for all 49 catalog rows exactly once")
    unassessed = []
    for rid, row in resources.items():
        state = row.get("state")
        require(state in {"unassessed", "selected", "deferred", "omitted", "covered"},
                f"Invalid resource state: {rid}")
        if state == "unassessed":
            unassessed.append(rid)
        else:
            require(bool(row.get("reason")), f"Resource {rid} needs a case-specific reason")
        if state == "covered":
            require(bool(row.get("references")), f"Covered resource {rid} needs references")
    for session in items("sessions"):
        local_file(session.get("path") if isinstance(session, dict) else session, "Session")
    for row in items("decisions"):
        require(row.get("recommendation") in {"pursue", "revise", "pause", "stop", "insufficient-evidence"},
                "Invalid decision recommendation")
        for eid in row.get("evidence_ids", []):
            require(eid in evidence, f"Decision refers to missing evidence {eid}")
    pending = sorted(set(activities) - complete)
    status = "incomplete" if pending else ("complete-adapted" if adapted else "complete")
    if case.get("lifecycle") == "stopped" and pending:
        status = "stopped—core incomplete"
    if decision:
        require(not unassessed, "Decision review needs a disposition for all catalog entries")
        require(bool(case.get("decisions")), "Decision review needs a saved decision")
        scope = case.get("scope", {})
        require(bool(scope.get("success_criteria")), "Decision review needs idea-specific success criteria")
        require(bool(scope.get("next_investment")), "Decision review needs the investment being considered")
        action = case.get("next_action", {})
        for key in ("owner", "action", "inputs", "deliverable", "completion_check", "resume_trigger"):
            require(bool(action.get(key)), f"Next action lacks {key}")
    return {"valid": not errors, "core_status": status, "core_done": len(complete),
            "core_total": len(activities), "pending_core": pending,
            "adapted_core": adapted, "unassessed_resources": unassessed,
            "errors": errors,
            "limit": "Structural checks only; inspect artifacts and actual evidence before credit or conclusions."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    new = sub.add_parser("new")
    new.add_argument("directory", type=Path)
    new.add_argument("--title", required=True)
    validate = sub.add_parser("check")
    validate.add_argument("directory", type=Path)
    validate.add_argument("--decision", action="store_true")
    args = parser.parse_args()
    try:
        result = initialize(args.directory, args.title) if args.command == "new" else check(args.directory, args.decision)
    except (ValueError, OSError, KeyError, TypeError) as exc:
        result = {"valid": False, "errors": [str(exc)]}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result.get("valid", True) else 1)


if __name__ == "__main__":
    main()
