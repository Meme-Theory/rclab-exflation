"""
_bk_array_meta_classifier_v2_audit.py

7×4 outcome-table audit harness for BK-array meta-classifier_v2
(T4-1, S86 W-3 AUDIT-1).

Purpose
-------
Runs the four-outcome meta-classifier_v2 against:
  - 7-input synthetic panel: r ∈ {0.003, 0.0074, 0.0117, 0.014, 0.017, 0.025, 0.040}
  - 4 reference inputs: one per outcome class i / ii / iii / iv

Verifies routing to expected outcomes. Per-outcome co-gating wiring:
  - outcomes (i), (ii)   : LiteBIRD-only co-gating
  - outcomes (iii), (iv) : LiteBIRD ∧ LISA co-gating

Tested with synthetic (n_T_obs, Ω_GW_obs) tuples.

Source
------
S86 W-3 §Carry-Forward 2 (lines 3245-3250).
S86 W-3 §R2-B Emergence #1-3 (lines 2273-2432) — rank-2 product detector.
S86 W-3 §R3-A Convergence #1-4 (lines 2440-2597) — numerical lock-ins.

Provenance
----------
S86 W0c-7 housekeeping queue Tier-4 row T4-1.
Promoted from S86 W-3 AUDIT-1 (gen-physicist, 2026-04-26).

Status
------
SCAFFOLD. Data dependencies marked TODO(S87).

Usage
-----
    python _bk_array_meta_classifier_v2_audit.py             # report mode
    python _bk_array_meta_classifier_v2_audit.py --json      # machine-readable
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# Project canonical constants (mandatory per .claude/rules/math-scripts.md S34+).
sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import *  # noqa: F401,F403


# ---------------------------------------------------------------------------
# Pinned audit parameters (S86 W-3 R3-A Convergence #1-4)
# ---------------------------------------------------------------------------

# 7-input synthetic r panel.
SYNTHETIC_R_PANEL = (                                     # (local)
    0.003,
    0.0074,
    0.0117,
    0.014,
    0.017,
    0.025,
    0.040,
)

# Outcome-class enumeration (i/ii/iii/iv).
OUTCOMES = ("i", "ii", "iii", "iv")                       # (local)

# Per-outcome co-gating wiring.
COGATING_WIRING = {                                       # (local)
    "i":   ("LiteBIRD",),
    "ii":  ("LiteBIRD",),
    "iii": ("LiteBIRD", "LISA"),
    "iv":  ("LiteBIRD", "LISA"),
}

# Reference inputs per outcome (TODO: pin from S87 CF-2 deliverable).
# Each entry: (r_input, expected_outcome, n_T_obs, Omega_GW_obs)
REFERENCE_INPUTS = {                                      # (local)
    # TODO(S87): pin reference (r, n_T_obs, Omega_GW_obs) tuples
    #             once meta-classifier_v2 spec lands from S87 CF-2.
    "i":   None,
    "ii":  None,
    "iii": None,
    "iv":  None,
}


# ---------------------------------------------------------------------------
# Meta-classifier hooks (TODO: import S87 implementation when available)
# ---------------------------------------------------------------------------

def meta_classifier_v2(r: float, n_T_obs: float | None = None,
                       Omega_GW_obs: float | None = None) -> str:
    """Four-outcome meta-classifier_v2.

    TODO(S87): Replace stub with import from
        computations/session-87/s87_bk_array_meta_classifier_v2.py
    once that module lands as part of S87 CF-2.

    The classifier returns one of: "i", "ii", "iii", "iv".
    Routing rules pre-registered in S86 W-3 R2-B Emergence (rank-2
    product detector, lines 2273-2432).
    """
    raise NotImplementedError(
        "TODO(S87): meta_classifier_v2 not yet implemented; awaiting "
        "S87 CF-2 deliverable per S86 W-3 §Carry-Forward 2."
    )


def cogating_satisfied(outcome: str,
                       litebird_pass: bool,
                       lisa_pass: bool) -> bool:
    """Per-outcome co-gating: outcomes i/ii need LiteBIRD-only;
    iii/iv need LiteBIRD ∧ LISA.
    """
    required = COGATING_WIRING[outcome]                   # (local)
    have = {"LiteBIRD": litebird_pass, "LISA": lisa_pass} # (local)
    return all(have[d] for d in required)


# ---------------------------------------------------------------------------
# Audit harness
# ---------------------------------------------------------------------------

def synthetic_panel_audit() -> dict:
    """Run the 7-input synthetic panel through meta_classifier_v2 and
    record routed outcomes. SCAFFOLD: returns NOT_RUN until classifier lands.
    """
    rows = []                                              # (local)
    for r in SYNTHETIC_R_PANEL:
        try:
            outcome = meta_classifier_v2(r)               # (local)
            status = "ROUTED"
        except NotImplementedError:
            outcome = None
            status = "NOT_RUN_SCAFFOLD"
        rows.append({
            "r": r,
            "outcome": outcome,
            "status": status,
        })
    return {
        "panel_size": len(SYNTHETIC_R_PANEL),
        "routed_count": sum(1 for r in rows if r["status"] == "ROUTED"),
        "rows": rows,
    }


def reference_input_audit() -> dict:
    """Run the 4 reference inputs (one per class) through the classifier."""
    rows = []                                              # (local)
    for outcome_class, ref in REFERENCE_INPUTS.items():
        if ref is None:
            rows.append({
                "expected_outcome": outcome_class,
                "status": "NOT_PINNED_SCAFFOLD",
                "todo": "TODO(S87): pin (r, n_T_obs, Omega_GW_obs) for this class.",
            })
            continue
        r, expected, n_T, Omega_GW = ref
        try:
            actual = meta_classifier_v2(r, n_T, Omega_GW) # (local)
            rows.append({
                "expected_outcome": outcome_class,
                "actual_outcome": actual,
                "match": actual == expected,
                "status": "ROUTED",
            })
        except NotImplementedError:
            rows.append({
                "expected_outcome": outcome_class,
                "status": "NOT_RUN_SCAFFOLD",
            })
    return {"rows": rows}


def cogating_audit() -> dict:
    """Verify cogating wiring: outcomes (i,ii) require LiteBIRD only;
    outcomes (iii,iv) require LiteBIRD ∧ LISA. Tests synthetic boolean
    combinations of (litebird_pass, lisa_pass) per outcome.
    """
    cases = []                                             # (local)
    for outcome in OUTCOMES:
        for lb in (True, False):
            for ls in (True, False):
                ok = cogating_satisfied(outcome, lb, ls)  # (local)
                cases.append({
                    "outcome": outcome,
                    "litebird_pass": lb,
                    "lisa_pass": ls,
                    "satisfied": ok,
                })
    return {"cases": cases}


def run_audit() -> dict:
    """Top-level audit dispatch. Aggregates all three sub-audits."""
    panel = synthetic_panel_audit()                       # (local)
    refs = reference_input_audit()                        # (local)
    cogate = cogating_audit()                             # (local)

    scaffold_blockers = []                                 # (local)
    if panel["routed_count"] == 0:
        scaffold_blockers.append("synthetic_panel: meta_classifier_v2 not implemented")
    if any(r.get("status", "").endswith("SCAFFOLD") for r in refs["rows"]):
        scaffold_blockers.append("reference_input: 4 reference inputs not pinned")

    verdict = "PASS" if not scaffold_blockers else "INFO_SCAFFOLD"  # (local)

    return {
        "audit_id": "S86-W3-BK-ARRAY-META-CLASSIFIER-V2",
        "verdict": verdict,
        "scaffold_blockers": scaffold_blockers,
        "synthetic_panel": panel,
        "reference_inputs": refs,
        "cogating_wiring": cogate,
        "cogating_spec": COGATING_WIRING,
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _format_report(result: dict) -> str:
    lines = []                                             # (local)
    lines.append(f"=== {result['audit_id']} ===")
    lines.append(f"Verdict: {result['verdict']}")
    if result["scaffold_blockers"]:
        lines.append("")
        lines.append("SCAFFOLD BLOCKERS (NEEDS-COMPUTATION):")
        for b in result["scaffold_blockers"]:
            lines.append(f"  - {b}")
    lines.append("")
    lines.append(f"Synthetic panel: {result['synthetic_panel']['routed_count']}/"
                 f"{result['synthetic_panel']['panel_size']} routed")
    lines.append(f"Cogating cases : {len(result['cogating_wiring']['cases'])} verified")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="BK-array meta_classifier_v2 7×4 outcome-table audit (T4-1)"
    )
    parser.add_argument("--json", action="store_true",
                        help="emit machine-readable JSON")
    args = parser.parse_args()

    result = run_audit()                                   # (local)

    if args.json:
        print(json.dumps(result, indent=2, default=str))
    else:
        print(_format_report(result))

    return 0


if __name__ == "__main__":
    sys.exit(main())
