import argparse
import json
from pathlib import Path
from datetime import datetime

from src.engine import (
    load_json,
    validate_state,
    migrate_state,
    compute_ratings,
    detect_bottlenecks,
    build_dependency_graph,
    generate_plan,
    compare_paths,
    risk_score,
)

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
STATE_PATH = DATA_DIR / "state.json"


def save_log(message):
    log_dir = ROOT / "logs"
    log_dir.mkdir(exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_path = log_dir / f"run_{stamp}.log"
    log_path.write_text(message, encoding="utf-8")


def cmd_status(state):
    account = state.get("account", {})
    skills = state.get("skills", {})
    print("Status")
    print(f"- Name: {account.get('name', 'Unknown')}")
    print(f"- Mode: {account.get('mode', 'main')}")
    print(f"- Avg skill: {sum(skills.values())/max(1, len(skills)) if skills else 0:.1f}")


def cmd_ratings(state):
    ratings, reasons = compute_ratings(state)
    print("Ratings")
    for k, v in ratings.items():
        print(f"- {k.replace('_', ' ').title()}: {v}/100")
        for r in reasons.get(k, [])[:3]:
            print(f"  reason: {r}")


def cmd_plan(state):
    plan = generate_plan(state)
    print("Plan")
    for horizon in ["short", "mid", "long"]:
        print(f"{horizon.title()} horizon:")
        for idx, item in enumerate(plan.get(horizon, []), start=1):
            prereqs = ", ".join(item.get("prereqs", [])) or "none"
            print(f" {idx}) {item.get('task')} ({item.get('time')})")
            print(f"    why: {item.get('why')}; prereqs: {prereqs}")
    print("Alternate paths:")
    for opt in compare_paths(state):
        print(f"- {opt['path']}: {opt['tradeoff']} ({opt['notes']})")


def cmd_dependencies(state):
    graph = build_dependency_graph(state)
    print("Dependencies")
    for node, reqs in graph.items():
        if reqs:
            print(f"- {node}: {', '.join(reqs)}")


def cmd_risk(state):
    print(f"Risk score: {risk_score(state)}/100")
    print(f"Bottlenecks: {', '.join(detect_bottlenecks(state))}")


def main():
    parser = argparse.ArgumentParser(description="<project_name> CLI")
    parser.add_argument("command", nargs="?", default="status")
    parser.add_argument("--state", default=str(STATE_PATH))
    args = parser.parse_args()

    state_path = Path(args.state)
    state = load_json(state_path, {})
    if not state:
        print("State file missing or empty. Edit data/state.json first.")
        return
    state = migrate_state(state)
    errors = validate_state(state)
    if errors:
        print("State validation errors:")
        for e in errors:
            print(f"- {e}")
        return

    cmd = args.command.lower()
    if cmd == "status":
        cmd_status(state)
    elif cmd == "ratings":
        cmd_ratings(state)
    elif cmd == "plan":
        cmd_plan(state)
    elif cmd == "deps":
        cmd_dependencies(state)
    elif cmd == "risk":
        cmd_risk(state)
    else:
        print("Unknown command. Try: status, ratings, plan, deps, risk")

    save_log(f"Command: {cmd}\n")


if __name__ == "__main__":
    main()
