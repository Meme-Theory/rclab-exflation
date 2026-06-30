"""
_eta_invariant_retarget_s_minus_1.py

Tier 4 eta-invariant re-target script at s = −1
(T4-20, S86 W-10 AUDIT-W10-3).

Purpose
-------
Compute Tier 4 of the ρ_∞ promotion schema (W-10 REG-W10-2):

    ρ_∞^{signed-residue, ζ}
        := Res_{s = −1} Tr( γ_9 · sign(D) · |D|^{−s} ) · (normalization)

This is an extension of:

    `computations/session-60/s60_eta_invariant.py`
    `computations/session-85/s85_w0_cc1_eta_invariant.py`

with the s-parameter re-targeted from s = 0 (canonical eta-invariant
density) to s = −1 (signed-residue analog at the fermionic
Mellin-cone pole below Sd_bos).

Required modifications versus the s = 0 base scripts:
  (a) re-target the zeta-regularization call from s = 0 to s = −1
  (b) verify Bernstein-Widder admissibility at s = −1 via separate
      analytic-continuation argument (channel-3c probe per T4-13)

Substitution chain (signed-residue at s = −1 vs eta-density at s = 0):

    Definition 1: η(D, s) := Tr(γ_9 · sign(D) · |D|^{−s})
                  (parametrized eta function)
    Definition 2: η-invariant := η(D, 0)
                  (canonical s = 0 evaluation per APS)
    Definition 3: signed residue at s = −1
                  := Res_{s = −1} η(D, s) · normalization
    Substitute:   |D|^{−s}|_{s = −1} = |D|^{+1}; integrand picks
                  up an extra factor of |D| relative to s = 0 case
    Simplify:     residue extraction via Mellin-Barnes contour
                  shift past the s = 0 pole to s = −1
    Direction:    s = 0 → −1 lowers convergence rate; admissibility
                  requires |λ|-cluster spectrum to support the
                  contour shift (W-10 R3-A CONVERGENCE #6a)

Source
------
S86 W-10 §AUDIT-W10-3 (lines 82-86).
S86 W-10 R3-A CONVERGENCE #6a + R3-B CONVERGENCE #6a.
S86 W-10 Carry-Forward 2 spec (lines 2275-2282).
S86 W-10 REG-W10-2 Tier 4 schema row.

Provenance
----------
S86 W0c-7 housekeeping queue Tier-4 row T4-20.
Promoted from S86 W-10 AUDIT-W10-3 (connes-ncg, 2026-04-26).

Status
------
SCAFFOLD. Major dependencies marked TODO(S87):
  - Re-targeted s = −1 zeta-regularization call (extension of
    existing s60 / s85_w0_cc1 modules)
  - Bernstein-Widder admissibility verification (analytic
    continuation past s = 0 pole)
  - Spectrum cache restoration (sign(D), |D| eigenvalue arrays)

LOW EFFORT per W-10 "INFRASTRUCTURE-READY-AT-S60-AND-S85" note.

Usage (post-S87 wire-up)
------------------------
    python _eta_invariant_retarget_s_minus_1.py
    python _eta_invariant_retarget_s_minus_1.py --json
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
# Pinned audit parameters
# ---------------------------------------------------------------------------

# Target s-value (W-10 AUDIT-W10-3 spec).
S_TARGET = -1.0                                            # (local)

# Default L_max (matching s60 / s85 anchor).
L_MAX_DEFAULT = 10                                         # (local)

# Source modules to extend (W-10 spec).
SOURCE_MODULES = (                                         # (local)
    "computations/session-60/s60_eta_invariant.py",
    "computations/session-85/s85_w0_cc1_eta_invariant.py",
)


# ---------------------------------------------------------------------------
# Hooks (TODO scaffolds)
# ---------------------------------------------------------------------------

def load_dirac_spectrum(L_max: int) -> dict:
    """Load D_K spectrum (eigenvalues + signs) from cached spectrum files.

    TODO(S87): import from
        sessions/archive/session-84/.../s84_spectrum_cache_L{L_max}_tau019.npz
    or analogous cache.
    """
    raise NotImplementedError(
        f"TODO(S87): load_dirac_spectrum(L_max={L_max}) requires "
        "spectrum-cache restoration."
    )


def load_chirality_operator(L_max: int) -> np.ndarray:
    """Load γ_9 chirality operator on the L_max truncated Hilbert space.

    TODO(S87): import from D_K construction module; γ_9 is the Z_2
    grading operator on the spectral triple's Hilbert space.
    """
    raise NotImplementedError(
        f"TODO(S87): load_chirality_operator(L_max={L_max})"
    )


def bernstein_widder_admissibility_at_s_minus_1(eigvals: np.ndarray) -> dict:
    """Verify Bernstein-Widder admissibility of the contour shift to s = −1.

    The contour shift requires the cumulative eigenvalue density to
    satisfy completely monotonic behavior (Bernstein-Widder theorem).

    TODO(S87): full BW check requires symbolic-mpmath analytic
    continuation argument per W-10 AUDIT-W10-3 spec (b).
    """
    raise NotImplementedError(
        "TODO(S87): Bernstein-Widder admissibility check at s = −1"
    )


# ---------------------------------------------------------------------------
# Core computation
# ---------------------------------------------------------------------------

def signed_residue_at_s_minus_1(L_max: int = L_MAX_DEFAULT) -> dict:
    """Compute Res_{s = −1} Tr(γ_9 · sign(D) · |D|^{−s})."""
    try:
        spec = load_dirac_spectrum(L_max)                 # (local)
        gamma_9 = load_chirality_operator(L_max)          # (local)
        bw = bernstein_widder_admissibility_at_s_minus_1(spec["eigvals"])
    except NotImplementedError as e:
        return {
            "verdict": "INFO_SCAFFOLD",
            "blocked_by": str(e),
            "L_max": L_max,
            "s_target": S_TARGET,
        }

    eigvals = spec["eigvals"]                              # (local)
    eigvecs = spec["eigvecs"]                              # (local)
    signs = np.sign(eigvals)                               # (local)
    abs_eig = np.abs(eigvals)                              # (local)

    # |D|^{−s} at s = −1 → |D|^{+1} = abs_eig.
    weights = signs * (abs_eig ** (-S_TARGET))            # (local) — note: (-(-1)) = +1

    # Tr(γ_9 · diag(weights)) in the eigenbasis.
    # γ_9 in eigenbasis has matrix elements (γ_9)_{ii} = ⟨e_i | γ_9 | e_i⟩.
    gamma_9_diag = np.real(np.einsum(
        "ij,ji->i", eigvecs.conj().T @ gamma_9, eigvecs
    ))                                                     # (local)
    trace_value = float(np.sum(gamma_9_diag * weights))   # (local)

    # Residue extraction (TODO: refine if pole is higher-order).
    residue = trace_value                                  # (local) — placeholder simple-pole

    return {
        "verdict": "PASS",
        "L_max": L_max,
        "s_target": S_TARGET,
        "trace_value": trace_value,
        "residue_at_s_minus_1": residue,
        "BW_admissibility": bw,
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Eta-invariant re-target at s = −1 (T4-20 / S86 W-10 AUDIT-W10-3)"
    )
    parser.add_argument("--L", type=int, default=L_MAX_DEFAULT,
                        help=f"L_max truncation (default: {L_MAX_DEFAULT})")
    parser.add_argument("--json", action="store_true",
                        help="emit machine-readable JSON")
    args = parser.parse_args()

    result = signed_residue_at_s_minus_1(args.L)          # (local)

    if args.json:
        print(json.dumps(result, indent=2, default=str))
    else:
        print("=== S86 W-10 / T4-20 Eta-Invariant Re-Target at s = −1 ===")
        print(f"Verdict: {result['verdict']}")
        for k, v in result.items():
            if k == "verdict":
                continue
            print(f"  {k}: {v}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
