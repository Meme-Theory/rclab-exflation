"""
s87_delta_speed_mellin_barnes_residue.py

δ_speed_substrate Mellin-Barnes residue computation harness
(T4-2, S86 W-3 AUDIT-2).

Purpose
-------
Direct evaluation of

    delta_speed_substrate(k_pivot) = d ln c_sub / d ln k |_{k = k_pivot}

from the S78 W2-E upper-spread Mellin integrand evaluated on the B1
eigenvalue cluster trajectory along fiber-tau.

Compares result to the lab-inherited 25% pin (Vollhardt-Wölfle Ch. 7-8).

Output
------
    delta_speed_substrate                    (dimensionless slope)
  +/- regime tag in {LOCAL-slope-bounded, GLOBAL-trajectory-dominated}
    .npz with full integrand sample on the B1 trajectory
    verdict line appended to s87_gate_verdicts.txt

Source
------
S86 W-3 §R2-B Dissent #1 (lines 2132-2208) — Mellin-Barnes formulation.
S86 W-3 §Carry-Forward 3 sub-gate (3a) (line 3254).
S86 W-3 §Carry-Forward 4 (lines 3259-3264) — δ_speed_substrate spec.

Provenance
----------
S86 W0c-7 housekeeping queue Tier-4 row T4-2.
Promoted from S86 W-3 AUDIT-2 (gen-physicist, 2026-04-26).

Status
------
SCAFFOLD. Major data dependencies marked TODO(S87):
  - B1 eigenvalue trajectory along fiber-tau (T4-4 prerequisite, CF-3 sub-gate)
  - S78 W2-E upper-spread Mellin integrand restoration

Usage (post-S87 wire-up)
------------------------
    python s87_delta_speed_mellin_barnes_residue.py             # report
    python s87_delta_speed_mellin_barnes_residue.py --json
    python s87_delta_speed_mellin_barnes_residue.py --tau-grid 256
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

# Cap CPU threads for parallel-agent friendliness.
os.environ.setdefault("OMP_NUM_THREADS", "8")

import numpy as np                                         # noqa: E402

# Project canonical constants (mandatory per .claude/rules/math-scripts.md S34+).
sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import *  # noqa: E402, F401, F403


# ---------------------------------------------------------------------------
# Pinned parameters
# ---------------------------------------------------------------------------

# Lab-inherited 25% pin (Vollhardt-Wölfle Ch. 7-8) — tolerance band for
# δ_speed_substrate compared to expected slope.
DELTA_SPEED_LAB_PIN_FRAC = 0.25                           # (local)

# Pivot wavenumber (k_pivot from canonical constants).
K_PIVOT_DEFAULT = 0.05                                    # (local) — Mpc^{-1}, CMB pivot

# Mellin contour parameter c (Re(s) for Bromwich-Mellin contour).
MELLIN_CONTOUR_C = 0.5                                    # (local)

# Default integrand sampling grid sizes.
TAU_GRID_DEFAULT = 256                                    # (local)
S_CONTOUR_GRID_DEFAULT = 1024                             # (local)


# ---------------------------------------------------------------------------
# Data-loading hooks (TODO scaffolds)
# ---------------------------------------------------------------------------

def load_b1_trajectory(tau_grid: int = TAU_GRID_DEFAULT) -> dict:
    """Load B1 eigenvalue trajectory λ_B1(τ) along τ ∈ [0, τ_fold].

    Required for the Mellin integrand restriction. This is the
    output of T4-4 (`B1 eigenvalue trajectory extraction`).
    """
    raise NotImplementedError(
        "TODO(S87): load B1 trajectory from S87-W2 prerequisite. "
        "Source artifact: T4-4 output (`computations/_shared/_b1_trajectory_extract.py`)."
    )


def load_w2e_upper_spread_integrand() -> dict:
    """Load S78 W2-E upper-spread Mellin integrand spec.

    Returns a dict with the integrand callable + Mellin contour pin
    + integration-domain bounds. Required for δ_speed_substrate eval.
    """
    raise NotImplementedError(
        "TODO(S87): restore S78 W2-E upper-spread Mellin integrand "
        "from `computations/session-78/s78_w2e_*` outputs. May require "
        "re-derivation from spectral-functional working paper."
    )


# ---------------------------------------------------------------------------
# Core computation
# ---------------------------------------------------------------------------

def mellin_barnes_residue(k: float, b1_trajectory: dict,
                          integrand_spec: dict) -> complex:
    """Evaluate the Mellin-Barnes residue at wavenumber k.

    The c_sub conformal substitution coefficient as a function of k
    is given by a Mellin contour integral over the B1 trajectory.
    Residue extraction at the pole governing d ln c_sub / d ln k
    gives δ_speed_substrate.

    TODO(S87): implement using the S78 W2-E integrand spec on the
    B1 trajectory grid; use scipy.integrate.quad on the Bromwich
    contour at Re(s) = MELLIN_CONTOUR_C.
    """
    raise NotImplementedError(
        "TODO(S87): implement Mellin-Barnes residue extraction; "
        "depends on B1 trajectory + S78 W2-E integrand."
    )


def delta_speed_substrate(k_pivot: float = K_PIVOT_DEFAULT) -> dict:
    """Compute δ_speed_substrate(k_pivot) = d ln c_sub / d ln k |_pivot.

    Returns
    -------
    dict with fields:
        delta_speed             — float (dimensionless slope)
        regime                  — "LOCAL-slope-bounded" or "GLOBAL-trajectory-dominated"
        within_lab_pin          — bool, |delta - lab_expected| ≤ 0.25 * |lab_expected|
        cross_check_quad        — quadrature-method cross-check value
    """
    try:
        b1 = load_b1_trajectory()                         # (local)
        integ = load_w2e_upper_spread_integrand()         # (local)
    except NotImplementedError as e:
        return {
            "verdict": "INFO_SCAFFOLD",
            "blocked_by": str(e),
            "k_pivot": k_pivot,
        }

    res = mellin_barnes_residue(k_pivot, b1, integ)       # (local)
    delta = float(np.real(res))                           # (local)

    # Regime classification: LOCAL if |slope| < threshold AND pole
    # localizes within trajectory window; GLOBAL otherwise.
    # TODO(S87): pin regime threshold from §R2-B Dissent #1 detail.
    regime = "LOCAL-slope-bounded"  # (local) — placeholder pending S87 pin

    return {
        "verdict": "PASS",
        "k_pivot": k_pivot,
        "delta_speed_substrate": delta,
        "regime": regime,
        "lab_pin_frac": DELTA_SPEED_LAB_PIN_FRAC,
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="δ_speed_substrate Mellin-Barnes residue (T4-2 / S87 CF-3a)"
    )
    parser.add_argument("--k-pivot", type=float, default=K_PIVOT_DEFAULT,
                        help=f"pivot wavenumber (default: {K_PIVOT_DEFAULT} Mpc^-1)")
    parser.add_argument("--tau-grid", type=int, default=TAU_GRID_DEFAULT,
                        help=f"τ sampling grid size (default: {TAU_GRID_DEFAULT})")
    parser.add_argument("--json", action="store_true",
                        help="emit machine-readable JSON")
    args = parser.parse_args()

    result = delta_speed_substrate(args.k_pivot)          # (local)

    if args.json:
        print(json.dumps(result, indent=2, default=str))
    else:
        print(f"=== S86 W-3 / S87 CF-3a δ_speed_substrate ===")
        print(f"Verdict: {result['verdict']}")
        for k, v in result.items():
            if k == "verdict":
                continue
            print(f"  {k}: {v}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
