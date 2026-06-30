"""
_layer1_layer2_conflation_audit.py

LAYER 1 / LAYER 2 retroactive sweep audit (T4-10, S86 W-7 AU-1).

Purpose
-------
4-stage protocol (with optional Stage-2.5) for retroactive
LAYER 1 / LAYER 2 conflation detection across sessions S78-onward.

LAYER 1 = combinatorial (mechanical numerical assembly)
LAYER 2 = admissibility (axiomatic / structural eligibility)
LAYER-1-with-LAYER-2-disclaimer = combinatorial output flagged as
                                  contingent on LAYER 2 eligibility

Stage-2.5 sub-tag (optional):
  LAYER-2-axiomatic — eligibility derives from a registered axiom
  LAYER-2-numerical — eligibility derives from a numerical calibration

Stages:
  Stage 1: Statement enumeration via trigger-vocabulary grep
           (~250 cites estimated per lizzi L4 line 448).
  Stage 2: LAYER tag assignment.
  Stage 2.5 (optional): LAYER-2 axiomatic-vs-numerical sub-tag.
  Stage 3: Cross-tag conflation detection — same-subject +
           inference-direction + implication-theorem tests.
  Stage 4: Remediation tagging:
              REPAIR-IN-SESSION
              REPAIR-AT-REGISTRY
              CARRY-FORWARD-COMPUTE
              NO-ACTION

Trigger-vocabulary candidates (Stage-1 grep set; lizzi L4 spec):
  "combinatorial"
  "axiomatic"
  "admissible"
  "permitted by"
  "structurally allowed"
  "satisfies the layer"
  "layer 1"
  "layer 2"
  "L1-axiomatic"
  "L1-combinatorial"
  "L2-numerical"
  "L2-axiomatic"

Verdict thresholds (W-7 AU-3 calibration):
  PASS  iff ≤ 5% conflation-flag rate
  INFO  iff 5% – 25%
  FAIL  iff > 25%

Source
------
S86 W-7 §AU-1 (lines 76-86).
S86 W-7 lizzi L4 audit method spec (workshop lines 357-513).
S86 W-7 connes Re:L4 scaffolding (lines 824-895).
S86 W-7 connes C3 17-row inventory (lines 1199-1452).
S86 W-7 EM-LZ-2 transitive composition (lines 2685-2745).
S86 W-7 RU-3 nomenclature canonical (workshop §What Changed line 3464).
Outline target: `sessions/framework/registry/layer1-layer2-retroactive-audit.md`.

Provenance
----------
S86 W0c-7 housekeeping queue Tier-4 row T4-10.
Promoted from S86 W-7 AU-1 (lizzi-spectral, 2026-04-26).

Status
------
SCAFFOLD with ACTIVE STAGE-1 GREP. Stages 2-4 marked TODO(S87) for
manual semantic review (mechanical regex inference is over-broad).

Usage
-----
    python _layer1_layer2_conflation_audit.py
    python _layer1_layer2_conflation_audit.py --json
    python _layer1_layer2_conflation_audit.py --include-paths sessions/archive/session-78
    python _layer1_layer2_conflation_audit.py --strict
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

# Trigger-vocabulary set (Stage 1).
TRIGGER_VOCAB = (                                          # (local)
    "combinatorial",
    "axiomatic",
    "admissibl",       # catches admissible / admissibility
    "permitted by",
    "structurally allowed",
    "satisfies the layer",
    "layer 1",
    "layer 2",
    "l1-axiomatic",
    "l1-combinatorial",
    "l2-numerical",
    "l2-axiomatic",
    "layer-1-with-layer-2-disclaimer",
)

# Default scan roots: S78-onward.
DEFAULT_SCAN_ROOTS = (                                     # (local)
    "sessions/archive/session-78",
    "sessions/archive/session-79",
    "sessions/archive/session-80",
    "sessions/archive/session-81",
    "sessions/archive/session-82",
    "sessions/archive/session-83",
    "sessions/archive/session-84",
    "sessions/archive/session-85",
    "sessions/archive/session-86",
    "computations",
)

SCAN_EXTENSIONS = (".md", ".py", ".txt")                  # (local)

# Conflation-flag rate thresholds (W-7 AU-3 calibration).
PASS_RATE_MAX = 0.05                                       # (local)
INFO_RATE_MAX = 0.25                                       # (local)


# ---------------------------------------------------------------------------
# Stage 1: enumeration
# ---------------------------------------------------------------------------

def stage1_enumerate(scan_roots: tuple[str, ...],
                     project_root: Path) -> list[dict]:
    """Stage 1: walk scan roots, grep for trigger vocabulary."""
    pattern = re.compile(
        "|".join(re.escape(t) for t in TRIGGER_VOCAB),
        re.IGNORECASE,
    )
    cites = []                                             # (local)
    for root_str in scan_roots:
        root = project_root / root_str                    # (local)
        if not root.exists():
            continue
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = [d for d in dirnames
                           if d not in ("__pycache__", ".git", "node_modules")]
            for fn in filenames:
                if not fn.endswith(SCAN_EXTENSIONS):
                    continue
                p = Path(dirpath) / fn                    # (local)
                try:
                    text = p.read_text(encoding="utf-8", errors="replace")
                except OSError:
                    continue
                for i, line in enumerate(text.splitlines(), start=1):
                    if pattern.search(line):
                        cites.append({
                            "path": p.relative_to(project_root).as_posix(),
                            "line_no": i,
                            "snippet": line.strip()[:200],
                        })
    return cites


# ---------------------------------------------------------------------------
# Stage 2: LAYER tag assignment (TODO scaffold)
# ---------------------------------------------------------------------------

def stage2_assign_layer_tags(cites: list[dict]) -> list[dict]:
    """Stage 2: classify each cite as LAYER 1, LAYER 2, or
    LAYER-1-with-LAYER-2-disclaimer.

    TODO(S87): mechanical regex inference is over-broad — many
    matches are false positives (string literals, generic English
    use, lattice "layer", etc.). Manual semantic review required.
    """
    for cite in cites:
        cite["layer_tag"] = "UNCLASSIFIED_TODO_S87"
    return cites


# ---------------------------------------------------------------------------
# Stage 2.5: optional axiomatic-vs-numerical sub-tag
# ---------------------------------------------------------------------------

def stage2_5_subtag_layer2(cites: list[dict]) -> list[dict]:
    """Stage 2.5 (optional): for LAYER 2 cites, sub-tag as
    LAYER-2-axiomatic vs LAYER-2-numerical.

    TODO(S87): manual review per AU-1 spec; mechanical inference unsafe.
    """
    for cite in cites:
        if cite.get("layer_tag") == "LAYER 2":
            cite["layer2_subtag"] = "UNCLASSIFIED_TODO_S87"
    return cites


# ---------------------------------------------------------------------------
# Stage 3: conflation detection
# ---------------------------------------------------------------------------

def stage3_detect_conflations(cites: list[dict]) -> list[dict]:
    """Stage 3: cross-tag conflation tests:
        - same-subject test (two cites referring to the same observable
          but with conflicting layer tags)
        - inference-direction test (combinatorial → axiomatic without
          warrant)
        - implication-theorem test (axiomatic claim derived from
          combinatorial assembly)

    TODO(S87): requires Stage 2 outputs to be valid. Stage 3 returns
    NOT_RUN until Stage 2 is manually reviewed.
    """
    return [{"flag": "NOT_RUN_TODO_S87",
             "reason": "Stage 2 layer tags pending manual review"}]


# ---------------------------------------------------------------------------
# Stage 4: remediation tagging
# ---------------------------------------------------------------------------

REMEDIATION_CLASSES = (                                    # (local)
    "REPAIR-IN-SESSION",
    "REPAIR-AT-REGISTRY",
    "CARRY-FORWARD-COMPUTE",
    "NO-ACTION",
)


def stage4_remediation_tag(conflations: list[dict]) -> list[dict]:
    """Stage 4: assign remediation class to each Stage-3 conflation flag."""
    out = []                                               # (local)
    for c in conflations:
        out.append({**c, "remediation_class": "TODO_S87"})
    return out


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


def run_audit(scan_roots: tuple[str, ...] = DEFAULT_SCAN_ROOTS) -> dict:
    """Run all 4 stages."""
    root = _project_root()                                # (local)
    cites = stage1_enumerate(scan_roots, root)            # (local)
    tagged = stage2_assign_layer_tags(cites)              # (local)
    subtagged = stage2_5_subtag_layer2(tagged)            # (local)
    conflations = stage3_detect_conflations(subtagged)    # (local)
    remediated = stage4_remediation_tag(conflations)      # (local)

    cite_count = len(cites)                               # (local)
    flag_count = sum(1 for c in conflations
                     if c.get("flag") not in (None, "NOT_RUN_TODO_S87"))
    rate = flag_count / cite_count if cite_count else 0.0  # (local)

    if cite_count == 0:
        verdict = "INFO_NO_CITES"
    elif "TODO_S87" in str(conflations[0]):
        verdict = "INFO_SCAFFOLD"
    elif rate <= PASS_RATE_MAX:
        verdict = "PASS"
    elif rate <= INFO_RATE_MAX:
        verdict = "INFO"
    else:
        verdict = "FAIL"

    return {
        "audit_id": "S86-W7-LAYER1-LAYER2-RETROACTIVE",
        "verdict": verdict,
        "scan_roots": list(scan_roots),
        "stage1_cite_count": cite_count,
        "stage3_conflation_flag_count": flag_count,
        "conflation_rate": rate,
        "thresholds": {
            "pass_max": PASS_RATE_MAX,
            "info_max": INFO_RATE_MAX,
        },
        "stage1_cites_first_50": cites[:50],
        "stage3_conflations": conflations,
        "stage4_remediated_first_50": remediated[:50],
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="LAYER 1 / LAYER 2 retroactive sweep audit (T4-10 / S86 W-7 AU-1)"
    )
    parser.add_argument("--include-paths", nargs="+",
                        help="override scan roots (project-relative paths)")
    parser.add_argument("--json", action="store_true",
                        help="emit machine-readable JSON")
    parser.add_argument("--strict", action="store_true",
                        help="exit nonzero on FAIL")
    args = parser.parse_args()

    scan_roots = tuple(args.include_paths) if args.include_paths else DEFAULT_SCAN_ROOTS
    result = run_audit(scan_roots)                        # (local)

    if args.json:
        print(json.dumps(result, indent=2, default=str))
    else:
        print("=== S86 W-7 / T4-10 LAYER 1/2 Retroactive Sweep Audit ===")
        print(f"Verdict: {result['verdict']}")
        print(f"Stage 1 cite count: {result['stage1_cite_count']}")
        print(f"Stage 3 conflation flag count: {result['stage3_conflation_flag_count']}")
        print(f"Conflation rate: {result['conflation_rate']*100:.2f}%")
        print(f"Thresholds: PASS ≤ {PASS_RATE_MAX*100:.0f}%, INFO ≤ {INFO_RATE_MAX*100:.0f}%")

    if args.strict and result["verdict"] == "FAIL":
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
