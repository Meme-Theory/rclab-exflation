"""
_cross_detector_r_protection_audit.py

Cross-detector R-protection scope test (T4-6, S86 W-4 AUDIT-2).

Purpose
-------
Audits detector measure choice (Mellin-natural ds vs alternatives)
across:
  - CMB-S4 polarization B-mode bispectrum
  - DESI / Euclid LSS pair-counting non-Gaussianity
  - post-SKA-1 21-cm experiments

Classifies which detectors lie INSIDE the Mellin-cone protected
class (ds-natural integration measure preserves R-invariance) vs
which exit it (alternative measure breaks Mellin-cone protection
and re-introduces measure-dependent f_NL spread).

For each (detector, measure) pair, audit returns:
    - Mellin-cone protection status: PROTECTED / BROKEN / UNCLASSIFIED
    - Measure type: Mellin-natural ds / volume / Euclidean / mixed
    - f_NL spread under measure perturbation (if computable)

Source
------
S86 W-4 §Open Question 5 (line 1596).
S86 W-4 R2-B Dissent #1 (lines 904-930) — 5.7% spread under non-Mellin measures.
S86 W-4 §AUDIT-2 (line 45 of housekeeping extract).

Provenance
----------
S86 W0c-7 housekeeping queue Tier-4 row T4-6.
Promoted from S86 W-4 AUDIT-2 (connes-ncg + lizzi, 2026-04-26).

Status
------
SCAFFOLD. Major dependencies marked TODO(S87):
  - Detector-specific bispectrum estimator measures
  - Mellin-cone protection classifier (S82 W3-A inheritance)

Usage (post-S87 wire-up)
------------------------
    python _cross_detector_r_protection_audit.py
    python _cross_detector_r_protection_audit.py --json
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

# Detector roster (S86 W-4 §AUDIT-2 spec).
DETECTORS = (                                              # (local)
    "CMB-S4_polarization_Bmode_bispectrum",
    "DESI_LSS_pair_counting_NG",
    "Euclid_LSS_pair_counting_NG",
    "SKA1_21cm_post_reion",
)

# Measure-class roster.
MEASURE_CLASSES = (                                        # (local)
    "Mellin_natural_ds",
    "volume_d3k",
    "Euclidean_d3k",
    "mixed",
)

# Spread threshold (S86 W-4 R2-B Dissent #1: 5.7% under non-Mellin).
NON_MELLIN_SPREAD_THRESHOLD = 0.057                       # (local)


# ---------------------------------------------------------------------------
# Detector-specific hooks (TODO scaffolds)
# ---------------------------------------------------------------------------

def detector_estimator_measure(detector: str) -> str:
    """Return the canonical estimator measure used by `detector`.

    TODO(S87): pin from each detector's published bispectrum estimator
    convention. Sources:
      - CMB-S4: Lewis-Challinor / CAMB convention
      - DESI / Euclid: Sefusatti-Crocce-Pueblas estimator
      - SKA1: Munoz-Watkins reionization 21-cm bispectrum
    """
    raise NotImplementedError(
        f"TODO(S87): pin estimator measure for {detector} "
        "from observational pipeline literature."
    )


def f_NL_spread_under_measure(detector: str, measure: str) -> float:
    """Compute f_NL spread (relative) under the given measure.

    TODO(S87): perturbation calculation requires:
      - S82 W3-A f_NL Mellin-natural baseline
      - Re-evaluation under non-Mellin measure (volume, Euclidean, mixed)
      - Spread = |f_NL_alt − f_NL_Mellin| / |f_NL_Mellin|
    """
    raise NotImplementedError(
        f"TODO(S87): f_NL_spread_under_measure({detector}, {measure}) "
        "requires S82 W3-A Mellin-natural baseline + alternative-measure rerun."
    )


# ---------------------------------------------------------------------------
# Core audit
# ---------------------------------------------------------------------------

def classify_detector_protection(detector: str) -> dict:
    """Classify a single detector's R-protection status.

    Substitution chain:
        Definition 1: PROTECTED iff estimator_measure ∈ Mellin-natural class
                       AND f_NL spread under canonical-measure perturbation
                       ≤ NON_MELLIN_SPREAD_THRESHOLD
        Definition 2: BROKEN iff estimator_measure ∉ Mellin-natural class
                       AND f_NL spread > NON_MELLIN_SPREAD_THRESHOLD
        Definition 3: UNCLASSIFIED iff insufficient data
    """
    try:
        measure = detector_estimator_measure(detector)    # (local)
    except NotImplementedError as e:
        return {
            "detector": detector,
            "measure": None,
            "status": "UNCLASSIFIED",
            "blocked_by": str(e),
        }

    is_mellin_natural = measure == "Mellin_natural_ds"    # (local)
    spreads = {}                                           # (local)
    for alt_measure in MEASURE_CLASSES:
        if alt_measure == measure:
            continue
        try:
            spread = f_NL_spread_under_measure(detector, alt_measure)  # (local)
            spreads[alt_measure] = spread
        except NotImplementedError as e:
            spreads[alt_measure] = {"error": str(e)}

    # Classify if at least one numeric spread available.
    numeric_spreads = [v for v in spreads.values() if isinstance(v, (int, float))]
    if numeric_spreads:
        max_spread = max(numeric_spreads)                  # (local)
        if is_mellin_natural and max_spread <= NON_MELLIN_SPREAD_THRESHOLD:
            status = "PROTECTED"
        elif (not is_mellin_natural) and max_spread > NON_MELLIN_SPREAD_THRESHOLD:
            status = "BROKEN"
        else:
            status = "MARGINAL"
    else:
        status = "UNCLASSIFIED"
        max_spread = None

    return {
        "detector": detector,
        "measure": measure,
        "is_mellin_natural": is_mellin_natural,
        "max_alt_measure_spread": max_spread,
        "spreads": spreads,
        "status": status,
    }


def run_audit() -> dict:
    """Run the full cross-detector R-protection audit."""
    rows = [classify_detector_protection(d) for d in DETECTORS]  # (local)
    counts = {                                              # (local)
        "PROTECTED": sum(1 for r in rows if r["status"] == "PROTECTED"),
        "BROKEN": sum(1 for r in rows if r["status"] == "BROKEN"),
        "MARGINAL": sum(1 for r in rows if r["status"] == "MARGINAL"),
        "UNCLASSIFIED": sum(1 for r in rows if r["status"] == "UNCLASSIFIED"),
    }
    blocked_by = [r["blocked_by"] for r in rows if "blocked_by" in r]  # (local)

    if blocked_by:
        verdict = "INFO_SCAFFOLD"
    elif counts["BROKEN"] > 0:
        verdict = "INFO"  # Mixed: some detectors confirmed unprotected
    else:
        verdict = "PASS"

    return {
        "audit_id": "S86-W4-CROSS-DETECTOR-R-PROTECTION",
        "verdict": verdict,
        "non_mellin_spread_threshold": NON_MELLIN_SPREAD_THRESHOLD,
        "counts": counts,
        "rows": rows,
        "scaffold_blockers": blocked_by,
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Cross-detector R-protection scope test (T4-6 / S87 OQ5)"
    )
    parser.add_argument("--json", action="store_true",
                        help="emit machine-readable JSON")
    args = parser.parse_args()

    result = run_audit()                                   # (local)

    if args.json:
        print(json.dumps(result, indent=2, default=str))
    else:
        print("=== S86 W-4 / OQ5 Cross-Detector R-Protection Audit ===")
        print(f"Verdict: {result['verdict']}")
        print(f"Threshold: {result['non_mellin_spread_threshold']*100:.1f}% spread")
        print(f"Counts: {result['counts']}")
        if result.get("scaffold_blockers"):
            print(f"Scaffold blockers: {len(result['scaffold_blockers'])}")
        for r in result["rows"]:
            print(f"  {r['detector']:50s} → {r['status']}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
