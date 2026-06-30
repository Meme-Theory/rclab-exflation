#!/usr/bin/env python3
"""
S80 — PRU Baseline Trendline Persistence
========================================

Gate: S80-PRU-TRENDLINE (infrastructure, NON-PHONONIC; no substitution-chain
trigger — pure logging.)

PURPOSE
-------
Append one snapshot of the three PRU baseline counts from the latest
`s80_pru_audit_report.json` to a JSONL ledger. The ledger is the
session-over-session trendline:

  baseline counts over time  =  did we drive unpinned gates to 0?

FORMAT
------
`computations/session-80/s80_pru_trendline.jsonl`

Each line is a JSON object:
{
  "timestamp_utc":   "<ISO-8601>",
  "session":         "<auto-detected tag, e.g., S81>",
  "git_head":        "<short sha>",
  "canon_sha":       "<sha256 of canonical_constants.py>",
  "a_unregistered":  <int>,    # unregistered constants >= threshold
  "b_untagged":      <int>,    # permanent-results rows without 4-tuple tag
  "c_unpinned":      <int>,    # verdict lines without sha256 pin
  "delta_since_prev": {"a": <int>, "b": <int>, "c": <int>},
  "note":            "<free-text context>"
}

DISCIPLINE
----------
- Reads `s80_pru_audit_report.json` — does not recompute.
- Does not modify the audit report or canonical_constants.
- Appends only; never rewrites prior lines.
- Auto-detects session from SESSION env var, falls back to latest
  `sessions/session-plan/s*-plan.md` filename, then "Sxx-unknown".
- 4-tuple: (value=<count>, scheme=STRUCTURAL-AUDIT, convention=PRU-CLASS-8, L_max=N/A)
"""
from __future__ import annotations

# Mandatory canonical import (this script does not consume values, but the
# audit flags scripts without the import line).
from canonical_constants import *  # noqa: F401,F403

import argparse
import hashlib
import json
import os
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===


PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
AUDIT_REPORT = resolve_output(80, 's80_pru_audit_report.json')
TRENDLINE_JSONL = resolve_script(80, 's80_pru_trendline.jsonl')
CANON_PY = resolve_script(None, 'canonical_constants.py')
SESSION_PLAN_DIR = PROJECT_ROOT / "sessions" / "session-plan"


def sha256_of_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def git_head_short() -> str:
    try:
        out = subprocess.check_output(
            ["git", "-C", str(PROJECT_ROOT), "rev-parse", "--short", "HEAD"],
            stderr=subprocess.DEVNULL,
            timeout=8,
        )
        return out.decode().strip()
    except (subprocess.SubprocessError, FileNotFoundError, OSError):
        return "unknown"


def detect_session() -> str:
    env = os.environ.get("SESSION")
    if env:
        return env.strip()
    # Prefer the highest-numbered active verdict file — that tag is the
    # session currently writing verdicts (more reliable than plan-doc names
    # which vary in naming convention).
    verdict_nums: list[int] = []
    for p in SCRIPT_DIR.glob("s*_gate_verdicts.txt"):
        m = re.match(r"s(\d+)_gate_verdicts\.txt$", p.name)
        if m:
            verdict_nums.append(int(m.group(1)))
    if verdict_nums:
        return f"S{max(verdict_nums)}"
    # Fall back to the latest session-plan filename.
    if SESSION_PLAN_DIR.is_dir():
        plan_nums: list[int] = []
        for p in SESSION_PLAN_DIR.glob("session-*.md"):
            m = re.match(r"session-(\d+)", p.name)
            if m:
                plan_nums.append(int(m.group(1)))
        if plan_nums:
            return f"S{max(plan_nums)}"
    return "Sxx-unknown"


def load_last_snapshot() -> dict | None:
    if not TRENDLINE_JSONL.exists():
        return None
    with TRENDLINE_JSONL.open("r", encoding="utf-8") as f:
        last = None
        for line in f:
            line = line.strip()
            if line:
                try:
                    last = json.loads(line)
                except json.JSONDecodeError:
                    continue
        return last


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Append one PRU baseline snapshot to the trendline JSONL.",
    )
    ap.add_argument(
        "--session",
        default=None,
        help="Session tag (default: SESSION env var or latest session-plan).",
    )
    ap.add_argument(
        "--note",
        default="",
        help="Free-text note (e.g. 'post S81 batch 2 rerun').",
    )
    ap.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the JSON line without appending.",
    )
    args = ap.parse_args()

    if not AUDIT_REPORT.exists():
        print(
            f"ERROR: audit report missing: {AUDIT_REPORT}\n"
            f"Run s80_pru_audit.py first.",
        )
        return 2
    report = json.loads(AUDIT_REPORT.read_text(encoding="utf-8"))
    baseline = report.get("baseline_counts") or {}
    a = int(baseline.get("a_unregistered_constants_ge_threshold", -1))
    b = int(baseline.get("b_untagged_theorem_entries", -1))
    c = int(baseline.get("c_gates_without_sha_pin", -1))

    prev = load_last_snapshot()
    delta = {"a": 0, "b": 0, "c": 0}
    if prev:
        delta = {
            "a": a - int(prev.get("a_unregistered", a)),
            "b": b - int(prev.get("b_untagged", b)),
            "c": c - int(prev.get("c_unpinned", c)),
        }

    snap = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "session": args.session or detect_session(),
        "git_head": git_head_short(),
        "canon_sha": sha256_of_file(CANON_PY) if CANON_PY.exists() else "missing",
        "a_unregistered": a,
        "b_untagged": b,
        "c_unpinned": c,
        "delta_since_prev": delta,
        "note": args.note,
    }

    line = json.dumps(snap, ensure_ascii=False)
    if args.dry_run:
        print(line)
        return 0

    with TRENDLINE_JSONL.open("a", encoding="utf-8") as f:
        f.write(line + "\n")

    total_lines = sum(
        1 for _ in TRENDLINE_JSONL.open("r", encoding="utf-8") if _.strip()
    )
    print(
        f"Appended snapshot #{total_lines}: "
        f"a={a}, b={b}, c={c}  "
        f"delta=(a{delta['a']:+d},b{delta['b']:+d},c{delta['c']:+d})  "
        f"session={snap['session']}  git={snap['git_head']}",
    )
    print(f"  -> {TRENDLINE_JSONL}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
