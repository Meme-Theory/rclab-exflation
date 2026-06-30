"""
_b1_trajectory_extract.py

B1 eigenvalue trajectory extraction along fiber-tau
(T4-4, S86 W-3 AUDIT-4).

Purpose
-------
Extract λ_B1(τ) — the lowest eigenvalue of D_K^2 restricted to the
B1 cluster — along τ ∈ [0, τ_fold]. Required input for:

  - T4-2 / S87 CF-3a δ_speed_substrate Mellin-Barnes residue
  - T4-3 / S87 CF-3c asymmetric-inheritance regime classification

Output
------
  - .npz with arrays:
      tau_grid             — τ samples in [0, τ_fold]
      lambda_B1            — lowest D_K^2 eigenvalue restricted to B1 at each τ
      cluster_membership   — boolean mask per τ identifying B1 cluster members
      lambda_pivot         — λ_B1 at the pivot k-mode for cross-check
  - verdict line appended to s87_gate_verdicts.txt

Substitution chain (D_K^2 restriction):

    Definition 1: D_K(τ) — Dirac operator on Jensen-deformed SU(3) at fiber-coord τ
    Definition 2: B1     — lowest eigenvalue cluster of D_K (rank-2 product detector
                            "regulator-axis-clean" sub-band per W-3 R2-B)
    Substitute:   λ_B1(τ) = min{ λ_i(τ) : eigenvector_i ∈ B1_subspace(τ) }
    Simplify:     restrict D_K^2 to B1 subspace via projection P_B1(τ);
                  diagonalize P_B1 D_K^2 P_B1; extract minimum eigenvalue
    Direction:    τ → τ_fold ⇒ B1 cluster narrows (van Hove fold);
                  λ_B1(τ) → 0+ at τ = τ_fold (substrate spectral collapse)

Source
------
S86 W-3 §R2-B Dissent #1 spec (line 2196).
S86 W-3 §Carry-Forward 3 inputs (line 3255).

Provenance
----------
S86 W0c-7 housekeeping queue Tier-4 row T4-4.
Promoted from S86 W-3 AUDIT-4 (gen-physicist, 2026-04-26).

Status
------
SCAFFOLD. Major dependencies marked TODO(S87):
  - D_K(τ) construction at L_max=10 along fiber-tau grid
  - B1 cluster identification (lowest eigenvalue band membership)
  - GPU torch.linalg.eigh on 155984×155984 matrix (VRAM check required)

Usage (post-S87 wire-up)
------------------------
    python _b1_trajectory_extract.py                    # default τ-grid, L_max=10
    python _b1_trajectory_extract.py --tau-grid 256 --L 10
    python _b1_trajectory_extract.py --json
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

# Default fiber-τ grid: dense near τ_fold for van-Hove resolution.
TAU_GRID_DEFAULT = 256                                    # (local)

# Default L_max for D_K spectrum.
L_MAX_DEFAULT = 10                                        # (local)

# B1 cluster definition: lowest-eigenvalue band of D_K^2 within
# `b1_band_relative_window` of the global minimum.
B1_BAND_RELATIVE_WINDOW = 0.05                            # (local) — 5% above min

# GPU memory feasibility cap (W-3 §G2(c) GPU-pin selectivity).
GPU_VRAM_CAP_BYTES = 17 * 1024**3                         # (local) — RX 9070 XT 17 GB
GPU_DENSE_FRACTION_CAP = 0.5                              # (local) — half of VRAM


# ---------------------------------------------------------------------------
# Core extraction logic
# ---------------------------------------------------------------------------

def gpu_vram_feasibility_check(matrix_dim: int,
                               dtype_bytes: int = 16) -> tuple[bool, str]:
    """Verify dense storage of D_K^2 fits in GPU VRAM cap.

    matrix_dim : side length of the square matrix
    dtype_bytes : 8 (float64), 16 (complex128)

    Returns (feasible, message).
    """
    bytes_required = (matrix_dim ** 2) * dtype_bytes      # (local)
    cap = GPU_DENSE_FRACTION_CAP * GPU_VRAM_CAP_BYTES     # (local)
    if bytes_required > cap:
        return False, (
            f"D_K^2 dense storage = {bytes_required / 1e9:.2f} GB exceeds "
            f"{GPU_DENSE_FRACTION_CAP*100:.0f}% of VRAM cap "
            f"({cap / 1e9:.2f} GB). Use sparse / iterative path."
        )
    return True, f"OK ({bytes_required / 1e9:.2f} GB)"


def construct_D_K_at_tau(tau: float, L_max: int) -> np.ndarray:
    """Construct D_K(τ) at fiber-coord τ, truncated at L_max.

    TODO(S87): import from `computations/_shared/_dk_jensen_construct.py`
    or analogous module. Must produce hermitian D_K matrix on
    Jensen-deformed SU(3) Hilbert space.
    """
    raise NotImplementedError(
        f"TODO(S87): construct_D_K_at_tau(tau={tau}, L_max={L_max}) "
        "requires D_K Jensen-deformation module restoration."
    )


def project_onto_B1_subspace(D_K_sq: np.ndarray) -> np.ndarray:
    """Project D_K^2 onto the B1 cluster subspace.

    TODO(S87): identify B1 via lowest-eigenvalue band membership
    using B1_BAND_RELATIVE_WINDOW. Construct projection
    P_B1 = Σ |b⟩⟨b| over b ∈ B1.
    """
    raise NotImplementedError(
        "TODO(S87): project_onto_B1_subspace requires B1 cluster "
        "identification per W-3 R2-B Dissent #1 spec line 2196."
    )


def lowest_eigenvalue_in_B1(tau: float, L_max: int) -> float:
    """Return λ_B1(τ) = min{ λ_i(τ) | i ∈ B1_subspace(τ) }."""
    D_K = construct_D_K_at_tau(tau, L_max)                # (local)
    D_K_sq = D_K @ D_K.conj().T                           # (local)
    P_D_P = project_onto_B1_subspace(D_K_sq)              # (local)
    # GPU eigh path (S85+ rule per math-scripts.md):
    #     import torch
    #     eigvals = torch.linalg.eigvalsh(torch.tensor(P_D_P, device='cuda'))
    eigvals = np.linalg.eigvalsh(P_D_P)                   # (local) — CPU stub
    return float(np.min(eigvals))                         # (local)


def extract_b1_trajectory(tau_grid: int = TAU_GRID_DEFAULT,
                          L_max: int = L_MAX_DEFAULT) -> dict:
    """Extract λ_B1(τ) along τ ∈ [0, τ_fold]."""
    try:
        tau_fold = float(tau_fold_pin)  # type: ignore[name-defined]   # (local)
    except NameError:
        try:
            tau_fold = float(tau_fold)  # type: ignore[name-defined]
        except NameError:
            raise NotImplementedError(
                "TODO(S87): pin tau_fold from canonical_constants.py."
            )

    taus = np.linspace(0.0, tau_fold, tau_grid)           # (local)
    lambdas = np.full(tau_grid, np.nan, dtype=np.float64) # (local)
    blocked_by = None                                      # (local)

    # Feasibility check for D_K dimension at L_max.
    # TODO(S87): pin matrix_dim from L_max via degree-counting formula.
    matrix_dim_estimate = 155984  # (local) — at L_max=10 per project framework
    feasible, msg = gpu_vram_feasibility_check(matrix_dim_estimate)

    for i, tau in enumerate(taus):
        try:
            lambdas[i] = lowest_eigenvalue_in_B1(float(tau), L_max)
        except NotImplementedError as e:
            blocked_by = str(e)
            break

    out_path = Path(__file__).parent / "_b1_trajectory_extract.npz"  # (local)
    if blocked_by is None:
        np.savez(out_path,
                 tau_grid=taus,
                 lambda_B1=lambdas,
                 tau_fold=tau_fold,
                 L_max=L_max)

    return {
        "verdict": "PASS" if blocked_by is None else "INFO_SCAFFOLD",
        "blocked_by": blocked_by,
        "tau_grid_size": tau_grid,
        "L_max": L_max,
        "tau_fold": tau_fold,
        "feasibility": {"feasible": feasible, "message": msg},
        "output_path": str(out_path) if blocked_by is None else None,
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="B1 eigenvalue trajectory extraction (T4-4 / S87-W2 prereq for CF-3)"
    )
    parser.add_argument("--tau-grid", type=int, default=TAU_GRID_DEFAULT,
                        help=f"τ sampling grid size (default: {TAU_GRID_DEFAULT})")
    parser.add_argument("--L", type=int, default=L_MAX_DEFAULT,
                        help=f"L_max truncation (default: {L_MAX_DEFAULT})")
    parser.add_argument("--json", action="store_true",
                        help="emit machine-readable JSON")
    args = parser.parse_args()

    result = extract_b1_trajectory(args.tau_grid, args.L) # (local)

    if args.json:
        print(json.dumps(result, indent=2, default=str))
    else:
        print("=== S86 W-3 / S87-W2 B1 Trajectory Extraction ===")
        print(f"Verdict: {result['verdict']}")
        for k, v in result.items():
            if k == "verdict":
                continue
            print(f"  {k}: {v}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
