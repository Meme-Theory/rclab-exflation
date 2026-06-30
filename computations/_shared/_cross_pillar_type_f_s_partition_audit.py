"""
_cross_pillar_type_f_s_partition_audit.py

Cross-pillar Type-F / Type-S partition audit
(T4-7, S86 W-4 AUDIT-3).

Purpose
-------
Re-classify framework observables under the Type-F / Type-S
state-functional / state-coordinate partition (W-4 §VII.O):

  Pillar II  (LEGGETT-MOMENT-70):  a_0, a_2, a_4, a_6
  Pillar III (BCS pair-fluctuation):
                s67_bcs_4pt_wilson.py outputs
  Pillar VI  (A_s / n_s; f_conv * P_zeta = 1.72e-9):
                S77 r_AB pattern

Output: §VII.P "Type-F / Type-S Cross-Pillar Atlas" registry table.

Type-F / Type-S definitions (S86 W-4 §VII.O.0 + §R3-A EMERGENCE #1):

  Type-F  state-functional, per-mode-resolved
          (substrate-canonical observable; example: per-mode {phi_a}
           on D_K's eigenmode pairs at tau_fold)

  Type-S  state-coordinate, scalar function of aggregate
          (detector-canonical observable; example: f_NL,
           N_pair_eff = 59.8)

Source
------
S86 W-4 §AUDIT-3 (lines 1651-1655).
S86 W-4 §R3-B EMERGENCE #2 (lines 1508-1531).
S86 W-4 CF-5 `S87-TYPE-F-TYPE-S-CROSS-PILLAR-AUDIT` (Tier 4).
S86 W-4 §VII.O / §VII.P entry candidates (lines 991-995, 1531).

Provenance
----------
S86 W0c-7 housekeeping queue Tier-4 row T4-7.
Promoted from S86 W-4 AUDIT-3 (connes-ncg + lizzi, 2026-04-26).

Status
------
SCAFFOLD. Major dependencies marked TODO(S87):
  - LEGGETT-MOMENT entries (a_0, a_2, a_4, a_6) per-mode/aggregate decomposition
  - BCS pair-fluctuation observable parentage classification
  - S77 r_AB pattern Type-F/Type-S projection

Usage (post-S87 wire-up)
------------------------
    python _cross_pillar_type_f_s_partition_audit.py
    python _cross_pillar_type_f_s_partition_audit.py --json
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
# Pinned parameters
# ---------------------------------------------------------------------------

# Pillar roster.
PILLARS = (                                                # (local)
    "II_LEGGETT_MOMENT_70",
    "III_BCS_pair_fluctuation",
    "VI_A_s_n_s",
)

# Per-pillar observable rosters.
LEGGETT_MOMENT_OBSERVABLES = ("a_0", "a_2", "a_4", "a_6")  # (local)

BCS_PAIR_FLUCTUATION_OBSERVABLES = (                       # (local)
    "wilson_4pt_function",
    "pair_fluctuation_amplitude",
    "BdG_spectral_det",
)

PILLAR_VI_OBSERVABLES = (                                  # (local)
    "A_s",
    "n_s",
    "f_conv_times_P_zeta",
    "S77_r_AB_pattern",
)

# Type-F / Type-S enumeration.
TYPE_F = "F_state_functional_per_mode"                     # (local)
TYPE_S = "S_state_coordinate_aggregate_scalar"             # (local)
TYPE_OTHER = "OTHER_non_F_non_S"                           # (local)


# ---------------------------------------------------------------------------
# Per-observable classifier hooks (TODO scaffolds)
# ---------------------------------------------------------------------------

def classify_observable(pillar: str, observable: str) -> dict:
    """Classify an observable as Type-F, Type-S, or OTHER.

    Substitution chain (per W-4 §VII.O.0 / §R3-B EMERGENCE #1):
        Definition: Type-F  iff observable is per-mode-resolved (state-functional)
                    Type-S  iff observable is scalar of aggregate (state-coordinate)
                    OTHER   iff neither (e.g., partial mode resolution
                            or non-state-functional non-state-coordinate)

    TODO(S87): pin classification per (pillar, observable) by reading
    the observable's canonical-source script header and operator-parentage tag.
    """
    raise NotImplementedError(
        f"TODO(S87): classify_observable({pillar}, {observable}) requires "
        "operator-parentage tag from canonical-source script."
    )


def detector_invisibility_status(pillar: str, observable: str,
                                 typ: str) -> str:
    """Per R3-B EMERGENCE #4: Type-F observables flagged with
    detector-invisibility-on-current-horizon status.

    Returns one of: "INVISIBLE", "VISIBLE", "MARGINAL", "UNKNOWN".
    """
    if typ != TYPE_F:
        return "VISIBLE"  # Type-S aggregates are detector-coupled by construction.
    raise NotImplementedError(
        f"TODO(S87): detector_invisibility_status({pillar}, {observable}) for Type-F "
        "requires per-detector resolution scoping."
    )


# ---------------------------------------------------------------------------
# Per-pillar audit
# ---------------------------------------------------------------------------

def audit_pillar(pillar: str, observables: tuple[str, ...]) -> dict:
    """Run audit on a single pillar."""
    rows = []                                              # (local)
    for obs in observables:
        try:
            cls = classify_observable(pillar, obs)        # (local)
            try:
                visibility = detector_invisibility_status(
                    pillar, obs, cls.get("type"))         # (local)
            except NotImplementedError as e:
                visibility = f"NOT_RESOLVED: {e}"
            rows.append({
                "pillar": pillar,
                "observable": obs,
                "type": cls.get("type"),
                "rationale": cls.get("rationale"),
                "detector_visibility": visibility,
            })
        except NotImplementedError as e:
            rows.append({
                "pillar": pillar,
                "observable": obs,
                "type": None,
                "status": "NOT_CLASSIFIED_SCAFFOLD",
                "blocked_by": str(e),
            })

    counts = {                                              # (local)
        "F": sum(1 for r in rows if r.get("type") == TYPE_F),
        "S": sum(1 for r in rows if r.get("type") == TYPE_S),
        "OTHER": sum(1 for r in rows if r.get("type") == TYPE_OTHER),
        "UNCLASSIFIED": sum(1 for r in rows if r.get("type") is None),
    }
    return {
        "pillar": pillar,
        "rows": rows,
        "counts": counts,
    }


def run_audit() -> dict:
    """Run cross-pillar Type-F/Type-S partition audit."""
    pillar_results = []                                    # (local)
    pillar_results.append(audit_pillar("II_LEGGETT_MOMENT_70",
                                       LEGGETT_MOMENT_OBSERVABLES))
    pillar_results.append(audit_pillar("III_BCS_pair_fluctuation",
                                       BCS_PAIR_FLUCTUATION_OBSERVABLES))
    pillar_results.append(audit_pillar("VI_A_s_n_s",
                                       PILLAR_VI_OBSERVABLES))

    # PASS criterion (S87 CF-5 gate):
    #  (a) per-pillar partition table built with ≥3 pillars covered
    #  (b) Type-F observables flagged with visibility status
    #  (c) §VII.P entry registered (post-Level-1)
    pillars_covered = sum(1 for p in pillar_results
                          if p["counts"]["UNCLASSIFIED"] < len(p["rows"]))
    blockers_present = any(
        any("blocked_by" in r for r in p["rows"]) for p in pillar_results
    )

    if blockers_present:
        verdict = "INFO_SCAFFOLD"
    elif pillars_covered >= 3:
        verdict = "PASS"
    else:
        verdict = "INFO"

    return {
        "audit_id": "S86-W4-CROSS-PILLAR-TYPE-F-S",
        "verdict": verdict,
        "pillars_covered": pillars_covered,
        "results": pillar_results,
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Cross-pillar Type-F/Type-S partition audit (T4-7 / S87 CF-5)"
    )
    parser.add_argument("--json", action="store_true",
                        help="emit machine-readable JSON")
    args = parser.parse_args()

    result = run_audit()                                   # (local)

    if args.json:
        print(json.dumps(result, indent=2, default=str))
    else:
        print("=== S86 W-4 / S87 CF-5 Cross-Pillar Type-F/Type-S Audit ===")
        print(f"Verdict: {result['verdict']}")
        print(f"Pillars covered: {result['pillars_covered']}")
        for p in result["results"]:
            print(f"\n  Pillar: {p['pillar']}")
            print(f"    Counts: {p['counts']}")
            for r in p["rows"]:
                marker = r.get("type") or r.get("status", "?")
                print(f"    - {r['observable']:30s} → {marker}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
