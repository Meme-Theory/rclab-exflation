"""
_verifier_rubric_audit.py

Verifier-rubric pre-registration audit
(T4-24, S86 W-12 AUDIT-W12-1; PRU Class-8.2 detection).

# NEEDS-ORCHESTRATOR-FOLLOWUP: NEEDS-DECISION readiness — orchestrator
# must decide whether this lands as (a) a NEW audit script
# (`_verifier_rubric_audit.py`, this file) OR (b) a feature extension
# to the existing `_pru_cardinality_audit.py`. RULE-W12-1 was the
# READY-TO-INSTALL rule-file diff; this audit is the implementation
# arm that was left as NEEDS-DECISION in the W-12 housekeeping queue.

Purpose
-------
Scans plan-block gate criteria in `sessions/session-plan/*.md` for
ambiguous-disjunction tokens that admit unintended logical readings
without explicit pre-registration. Flags Class-8.2 candidates.

PRU Class-8 taxonomy (per `.claude/rules/epistemic-discipline.md`):

  Class 8.0  : machinery-pin pre-registration failure (S78 origin;
               execution-time freedom from unpinned machinery)
  Class 8.1  : source-reconciliation drift (S85 origin; pinned-but-
               drift values)
  Class 8.2 (NEW)  : verifier-rubric pre-registration failure
                     (S86 W-12 origin; plan enumerated the verifier's
                     pattern-set but admitted an unintended logical
                     reading of "or similar" / "or equivalent" /
                     "any of [X, Y, ...]" tokens)
  Class 8.3 (potential): output-precision pre-registration failure
                         (S86 W1c-8 origin)

Detection rule:
  A gate criterion is a Class-8.2 candidate iff it contains a
  disjunction token from the AMBIGUOUS_TOKENS set BUT does NOT
  satisfy the four `Verifier-Rubric Pre-Registration` requirements:
    (1) pattern set enumeration
    (2) disjunction-vs-conjunction declaration
    (3) negative-marker set
    (4) calibration corpus pin

Calibration corpus (W-12 RULE-W12-1):
  S86 W-12 "Z_4 or similar" admitted Klein-four V_4 as "similar" via
  cardinality match despite structural distinction via element orders.

Source
------
S86 W-12 §AUDIT-W12-1 (lines 98-102).
S86 W-12 RULE-W12-1 PRU Class-8.2 (lines 33-50).
S86 W-12 EMERGENCE E-2 (R3-A) lines 1432-1449.
S86 W-12 CONVERGENCE C-5 (R3-B) lines 1577-1593.
`.claude/rules/epistemic-discipline.md` § "Verifier-Rubric
Pre-Registration".

Provenance
----------
S86 W0c-7 housekeeping queue Tier-4 row T4-24.
Promoted from S86 W-12 AUDIT-W12-1 (connes-ncg, 2026-04-26).

Status
------
SCAFFOLD with ACTIVE STAGE-1 GREP. Stage-2 rubric-completeness check
relies on plan-block schema; marked TODO(S87) once R3 schema lands.

Usage
-----
    python _verifier_rubric_audit.py
    python _verifier_rubric_audit.py --json
    python _verifier_rubric_audit.py --plan sessions/session-plan/session-87-plan.md
    python _verifier_rubric_audit.py --strict
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

# Project canonical constants (mandatory per .claude/rules/math-scripts.md S34+).
sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import *  # noqa: F401,F403


# ---------------------------------------------------------------------------
# Pinned audit parameters
# ---------------------------------------------------------------------------

# Disjunction tokens that admit ambiguous readings.
AMBIGUOUS_TOKENS = (                                       # (local)
    "or similar",
    "or equivalent",
    "any of",
    "or analogous",
    "or related",
    "etc.",
    "and so on",
    "or comparable",
    "or one of",
)

# Required Verifier-Rubric Pre-Registration markers.
RUBRIC_MARKERS = {                                         # (local)
    "pattern_set": (
        "pattern set:",
        "pattern_set:",
        "pre-registered set:",
    ),
    "disjunction_declaration": (
        "disjunction:",
        "conjunction:",
        "disjunction-vs-conjunction:",
    ),
    "negative_marker_set": (
        "negative-marker set:",
        "negative_markers:",
        "auto-fail patterns:",
    ),
    "calibration_corpus": (
        "calibration corpus:",
        "calibration_corpus:",
        "exemplar sha:",
    ),
}

# Default plan-file scan pattern.
DEFAULT_PLAN_GLOB = "sessions/session-plan/*.md"          # (local)
DEFAULT_PLAN_ARCHIVE_GLOB = "sessions/session-plan/archive/*.md"  # (local)


# ---------------------------------------------------------------------------
# Stage 1: ambiguous-token grep
# ---------------------------------------------------------------------------

def find_ambiguous_token_hits(text: str) -> list[dict]:
    """Find all ambiguous-token occurrences in plan text."""
    pattern = re.compile(
        "|".join(re.escape(t) for t in AMBIGUOUS_TOKENS),
        re.IGNORECASE,
    )
    hits = []                                              # (local)
    for i, line in enumerate(text.splitlines(), start=1):
        for m in pattern.finditer(line):
            hits.append({
                "line_no": i,
                "snippet": line.strip()[:200],
                "matched_token": m.group(0),
                "match_start": m.start(),
            })
    return hits


# ---------------------------------------------------------------------------
# Stage 2: rubric-completeness check around each hit
# ---------------------------------------------------------------------------

def check_rubric_markers_around(text_lines: list[str], hit_line_no: int,
                                window: int = 50) -> dict:
    """For each rubric marker, check whether ANY of its candidates
    appears within +/- window lines of hit_line_no.
    """
    lo = max(0, hit_line_no - 1 - window)                 # (local)
    hi = min(len(text_lines), hit_line_no - 1 + window + 1)
    context = "\n".join(text_lines[lo:hi]).lower()        # (local)
    out = {}                                               # (local)
    for marker_key, candidates in RUBRIC_MARKERS.items():
        out[marker_key] = any(c in context for c in candidates)
    return out


def class_8_2_classify(hit: dict, marker_check: dict) -> dict:
    """Classify a hit as Class-8.2 candidate or pre-registered."""
    n_present = sum(1 for v in marker_check.values() if v)
    is_class_8_2 = n_present < len(RUBRIC_MARKERS)
    return {
        **hit,
        "rubric_marker_check": marker_check,
        "n_markers_present": n_present,
        "n_markers_required": len(RUBRIC_MARKERS),
        "is_class_8_2_candidate": is_class_8_2,
    }


# ---------------------------------------------------------------------------
# Top-level audit
# ---------------------------------------------------------------------------

def _project_root() -> Path:
    p = Path(__file__).resolve().parent                   # (local)
    while p != p.parent:
        if (p / "CLAUDE.md").exists() and (p / "computations").exists():
            return p
        p = p.parent
    return Path(__file__).resolve().parent.parent


def audit_plan_file(path: Path) -> dict:
    """Audit a single plan file."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError as e:
        return {"path": str(path), "error": str(e), "hits": []}
    text_lines = text.splitlines()                         # (local)
    hits = find_ambiguous_token_hits(text)                # (local)
    classified = []                                        # (local)
    for h in hits:
        markers = check_rubric_markers_around(text_lines, h["line_no"])
        classified.append(class_8_2_classify(h, markers))
    n_class_8_2 = sum(1 for c in classified if c["is_class_8_2_candidate"])
    return {
        "path": str(path),
        "n_hits": len(hits),
        "n_class_8_2_candidates": n_class_8_2,
        "hits": classified,
    }


def run_audit(plan_path: str | None = None) -> dict:
    """Top-level audit."""
    root = _project_root()                                # (local)
    plan_files = []                                        # (local)
    if plan_path:
        p = Path(plan_path)
        if not p.is_absolute():
            p = root / p
        if p.exists():
            plan_files.append(p)
    else:
        plan_files.extend((root).glob(DEFAULT_PLAN_GLOB))
        plan_files.extend((root).glob(DEFAULT_PLAN_ARCHIVE_GLOB))

    file_results = [audit_plan_file(p) for p in plan_files]
    total_hits = sum(r["n_hits"] for r in file_results)
    total_class_8_2 = sum(r["n_class_8_2_candidates"] for r in file_results)
    verdict = "PASS" if total_class_8_2 == 0 else "FAIL"

    return {
        "audit_id": "S86-W12-VERIFIER-RUBRIC",
        "verdict": verdict,
        "plan_files_audited": len(plan_files),
        "total_ambiguous_token_hits": total_hits,
        "total_class_8_2_candidates": total_class_8_2,
        "file_results": file_results,
        "ambiguous_tokens": list(AMBIGUOUS_TOKENS),
        "required_rubric_markers": list(RUBRIC_MARKERS.keys()),
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Verifier-rubric pre-registration audit (T4-24 / S86 W-12 AUDIT-W12-1)"
    )
    parser.add_argument("--plan", type=str, default=None,
                        help="path to a single plan file (default: scan plan/ + plan/archive/)")
    parser.add_argument("--json", action="store_true",
                        help="emit machine-readable JSON")
    parser.add_argument("--strict", action="store_true",
                        help="exit nonzero on FAIL")
    args = parser.parse_args()

    result = run_audit(args.plan)                         # (local)

    if args.json:
        print(json.dumps(result, indent=2, default=str))
    else:
        print("=== S86 W-12 / T4-24 Verifier-Rubric Pre-Registration Audit ===")
        print(f"Verdict: {result['verdict']}")
        print(f"Plan files audited      : {result['plan_files_audited']}")
        print(f"Ambiguous-token hits    : {result['total_ambiguous_token_hits']}")
        print(f"Class-8.2 candidates    : {result['total_class_8_2_candidates']}")
        if result["total_class_8_2_candidates"] > 0:
            print("\nClass-8.2 candidates (first 20):")
            shown = 0                                      # (local)
            for fr in result["file_results"]:
                if fr["n_class_8_2_candidates"] == 0:
                    continue
                for h in fr["hits"]:
                    if not h["is_class_8_2_candidate"]:
                        continue
                    if shown >= 20:
                        break
                    print(f"  {Path(fr['path']).name}:{h['line_no']}: "
                          f"[{h['matched_token']}] {h['snippet']}")
                    shown += 1
                if shown >= 20:
                    break

    if args.strict and result["verdict"] == "FAIL":
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
