"""
s87_w0_eps_h_hp1_lscan.py

HKR L-monotonic convergence diagnostic for ‖[ε_H]‖_{HP^1, r}
(T4-9, S86 W-5 AUDIT-2).

Purpose
-------
Computes ‖[ε_H]‖_{HP^1, r} at each L_max ∈ {5, 6, 7, 8, 9, 10}
(and optionally L_max ∈ {12, 15} per GPU-feasibility audit) under
all three regulators r ∈ {ζ, Zubarev, SDW}; fits residual to
L^{-α} power law.

Three-outcome distribution:
  Outcome A: α ≈ 3 (refines L^{-3} envelope; CANONICAL)
  Outcome B: α > 3 (faster convergence than canonical envelope)
  Outcome C: α < 3 OR non-monotonic (opens effective spectral
             dimension re-examination tied to S82 W2-5
             MP-Exclusion d=4 anchor)

Substitution chain (HP^1 L-convergence envelope):

    Definition 1: ‖[ε_H]‖_{HP^1, r}(L) — HP^1-norm of Heitsch
                   class at truncation L under regulator r
    Definition 2: ε_envelope(L, d) = L^{-3} at d=4 (S86 W-5
                   §R2-B DISSENT #1 Step 3; W-5 CANONICAL-6 pin
                   L_envelope_d4_Lmax10 = 0.001)
    Substitute:  residual(L, r) = ‖[ε_H]‖_{HP^1, r}(L) − ‖[ε_H]‖_∞^r
    Simplify:    log10(residual) = −α · log10(L) + const
    Direction:   α ↑ → faster convergence
                 α = 3 (Outcome A) ⇒ canonical d=4 spectral
                                       dimension confirmed
                 α < 3 (Outcome C) ⇒ non-canonical d_eff < 4
                                       (effective spectral
                                       dimension lower than 4;
                                       re-examines S82 W2-5)

Source
------
S86 W-5 §AUDIT-2 (lines 76-80).
S86 W-5 R2-A Q1' (workshop L1503).
S86 W-5 R2-B DISSENT #1 substitution chain (workshop L1646-1707).
S86 W-5 CANONICAL-6: L_envelope_d4_Lmax10 = 0.001.
S86 W-5 CANONICAL-1: eps_H_HP1_norm = 16.197719 at L_max=10.

Provenance
----------
S86 W0c-7 housekeeping queue Tier-4 row T4-9.
Promoted from S86 W-5 AUDIT-2 (volovik + connes, 2026-04-26).

Status
------
SCAFFOLD. Major dependencies marked TODO(S87):
  - HP^1 norm computation per (L, r) requires L_max scan of
    Heitsch cocycle representative + HC^2 pairing
  - eps_H spectral-triple representative at each L_max
  - GPU-feasibility audit before L_max ∈ {12, 15} extension

Usage (post-S87 wire-up)
------------------------
    python s87_w0_eps_h_hp1_lscan.py                 # default L_max=5..10
    python s87_w0_eps_h_hp1_lscan.py --extended      # adds L_max=12,15
    python s87_w0_eps_h_hp1_lscan.py --json
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

# L_max scan range.
L_MAX_DEFAULT_RANGE = (5, 6, 7, 8, 9, 10)                 # (local)
L_MAX_EXTENDED_RANGE = (5, 6, 7, 8, 9, 10, 12, 15)        # (local)

# Regulator roster (W-5 AUDIT-2 spec).
REGULATORS = ("zeta", "Zubarev", "SDW")                   # (local)

# Pre-pinned anchor: ‖[ε_H]‖_{HP^1} at L_max=10 (W-5 CANONICAL-1).
EPS_H_HP1_NORM_LMAX10 = 16.197719                         # (local)

# Canonical envelope value at d=4, L_max=10 (W-5 CANONICAL-6).
L_ENVELOPE_D4_LMAX10 = 0.001                              # (local)

# Three-outcome alpha bands.
ALPHA_OUTCOME_A_BAND = (2.7, 3.3)                         # (local)
ALPHA_OUTCOME_B_THRESHOLD = 3.3                           # (local)
ALPHA_OUTCOME_C_THRESHOLD = 2.7                           # (local)

# GPU VRAM cap (RX 9070 XT).
GPU_VRAM_CAP_BYTES = 17 * 1024**3                         # (local)
GPU_DENSE_FRACTION_CAP = 0.5                              # (local)


# ---------------------------------------------------------------------------
# Hooks (TODO scaffolds)
# ---------------------------------------------------------------------------

def compute_eps_h_hp1_norm(L_max: int, regulator: str) -> float:
    """Compute ‖[ε_H]‖_{HP^1, r}(L_max) under regulator r.

    TODO(S87): implement via:
      1. Construct ε_H spectral-triple representative at L_max
         (truncated A^{<=L_max}, H^{<=L_max}, D^{<=L_max}).
      2. Apply HKR map to map cyclic chains to differential forms.
      3. Compute HP^1 norm via cohomology-class projection under
         the regulator-r HC^2 pairing.
    Returns the (positive real) HP^1 norm.
    """
    raise NotImplementedError(
        f"TODO(S87): compute_eps_h_hp1_norm(L_max={L_max}, regulator={regulator}) "
        "requires HP^1 cohomology pairing infrastructure restoration."
    )


def gpu_feasibility_for_L(L_max: int) -> tuple[bool, str]:
    """Estimate D_K matrix dimension at L_max and check VRAM fit."""
    # TODO(S87): pin matrix-dim-vs-L_max formula from project framework.
    # Provisional: dim ≈ 155984 at L_max=10; scale ~ L_max^4 by Weyl law.
    base_dim = 155984                                      # (local) — at L_max=10
    base_L = 10                                            # (local)
    dim_estimate = int(base_dim * (L_max / base_L) ** 4)  # (local)
    bytes_required = dim_estimate ** 2 * 16                # (local) — complex128
    cap = GPU_DENSE_FRACTION_CAP * GPU_VRAM_CAP_BYTES     # (local)
    feasible = bytes_required <= cap                       # (local)
    msg = (
        f"L_max={L_max}: dim≈{dim_estimate}, bytes≈{bytes_required/1e9:.2f}GB, "
        f"cap={cap/1e9:.2f}GB"
    )
    return feasible, msg


# ---------------------------------------------------------------------------
# Core scan + fit
# ---------------------------------------------------------------------------

def fit_residual_power_law(L_arr: np.ndarray,
                           residuals: np.ndarray) -> dict:
    """Fit log(residual) = -alpha * log(L) + const.

    Substitution chain:
        Definition: residual(L) ~ L^{-alpha}
        Substitute: log10(residual(L)) = -alpha · log10(L) + log10(C)
        Simplify:   linear fit y = m·x + b with m = -alpha, b = log10(C)
        Direction:  steeper negative m ⇒ larger alpha ⇒ faster convergence
    """
    pos = residuals > 0                                    # (local) — log requires positive
    if pos.sum() < 2:
        return {"alpha": float("nan"), "const": float("nan"),
                "n_points_fit": int(pos.sum()),
                "note": "insufficient positive residuals for log-log fit"}
    x = np.log10(L_arr[pos])                              # (local)
    y = np.log10(residuals[pos])                          # (local)
    slope, intercept = np.polyfit(x, y, 1)                # (local)
    alpha = -slope                                         # (local)
    return {
        "alpha": float(alpha),
        "const": float(10 ** intercept),
        "n_points_fit": int(pos.sum()),
    }


def classify_outcome(alpha: float) -> str:
    """Three-outcome classifier per W-5 AUDIT-2 spec."""
    if np.isnan(alpha):
        return "INDETERMINATE"
    if ALPHA_OUTCOME_A_BAND[0] <= alpha <= ALPHA_OUTCOME_A_BAND[1]:
        return "A_canonical_alpha_3"
    if alpha > ALPHA_OUTCOME_B_THRESHOLD:
        return "B_faster_than_canonical"
    if alpha < ALPHA_OUTCOME_C_THRESHOLD:
        return "C_slower_or_non_monotonic"
    return "MARGINAL"


def run_lscan(L_max_range: tuple[int, ...] = L_MAX_DEFAULT_RANGE,
              extended: bool = False) -> dict:
    """Execute the L-scan diagnostic."""
    if extended:
        L_max_range = L_MAX_EXTENDED_RANGE

    # GPU-feasibility check for each L (W-5 AUDIT-2: extended range
    # gated on feasibility audit).
    feasibility = {}                                       # (local)
    for L in L_max_range:
        feasibility[L] = gpu_feasibility_for_L(L)

    norms_by_regulator = {r: {} for r in REGULATORS}      # (local)
    blockers = []                                          # (local)
    for L in L_max_range:
        for r in REGULATORS:
            try:
                norms_by_regulator[r][L] = compute_eps_h_hp1_norm(L, r)
            except NotImplementedError as e:
                blockers.append(f"L={L}, r={r}: {e}")

    if blockers:
        return {
            "audit_id": "S86-W5-EPS-H-HP1-LSCAN",
            "verdict": "INFO_SCAFFOLD",
            "L_max_range": list(L_max_range),
            "regulators": list(REGULATORS),
            "feasibility": feasibility,
            "blocked_by": blockers[:5],
            "blocker_count": len(blockers),
        }

    # Per-regulator power-law fit.
    fits = {}                                              # (local)
    outcomes = {}                                          # (local)
    for r in REGULATORS:
        L_arr = np.asarray(sorted(norms_by_regulator[r].keys()), dtype=np.float64)
        norms_arr = np.asarray([norms_by_regulator[r][int(L)] for L in L_arr])
        # Residual relative to canonical limit (CANONICAL-1 at L_max=10).
        residuals = np.abs(norms_arr - EPS_H_HP1_NORM_LMAX10)
        fit = fit_residual_power_law(L_arr, residuals)    # (local)
        outcome = classify_outcome(fit["alpha"])          # (local)
        fits[r] = fit
        outcomes[r] = outcome

    # Verdict: PASS iff at least one regulator yields Outcome A.
    a_count = sum(1 for o in outcomes.values() if o == "A_canonical_alpha_3")
    verdict = "PASS" if a_count >= 1 else "INFO"

    return {
        "audit_id": "S86-W5-EPS-H-HP1-LSCAN",
        "verdict": verdict,
        "L_max_range": list(L_max_range),
        "regulators": list(REGULATORS),
        "feasibility": feasibility,
        "norms_by_regulator": norms_by_regulator,
        "fits": fits,
        "outcomes": outcomes,
        "outcome_a_count": a_count,
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="HKR L-monotonic convergence diagnostic (T4-9 / S87 CF-1 sub-gate)"
    )
    parser.add_argument("--extended", action="store_true",
                        help="add L_max ∈ {12, 15} to scan (gated on GPU feasibility)")
    parser.add_argument("--json", action="store_true",
                        help="emit machine-readable JSON")
    args = parser.parse_args()

    result = run_lscan(extended=args.extended)            # (local)

    if args.json:
        print(json.dumps(result, indent=2, default=str))
    else:
        print("=== S86 W-5 / S87 CF-1 eps_H HP^1 L-Scan Diagnostic ===")
        print(f"Verdict: {result['verdict']}")
        print(f"L_max range: {result['L_max_range']}")
        print(f"Regulators : {result['regulators']}")
        print("\nGPU feasibility:")
        for L, (ok, msg) in result["feasibility"].items():
            mark = "OK" if ok else "OVER VRAM"
            print(f"  L={L}: [{mark}] {msg}")
        if result.get("blocked_by"):
            print(f"\nBlockers ({result['blocker_count']}, first 5):")
            for b in result["blocked_by"]:
                print(f"  - {b}")
        else:
            print("\nFits (per regulator):")
            for r, fit in result["fits"].items():
                print(f"  r={r}: alpha={fit['alpha']:.3f}, "
                      f"outcome={result['outcomes'][r]}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
