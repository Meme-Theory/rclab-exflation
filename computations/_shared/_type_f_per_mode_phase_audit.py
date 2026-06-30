"""
_type_f_per_mode_phase_audit.py

Type-F per-mode phase audit script (T4-5, S86 W-4 AUDIT-1).

Purpose
-------
Compute canonical Bogoliubov-phase distribution {phi_a}_{a=1..32} on
post-tau_fold GGE state from S67 / S82 outputs. Report dispersion of
the scalar projection

    N_A = Sum_a w_a · Im[ alpha_a · (beta_a*)^2 ]

across 3 mode-distribution variations:

    (i)   canonical                     — w_a from canonical_constants
    (ii)  even-r                         — uniform weights w_a = 1/32
    (iii) random-uniform[0.5, 2.0]       — Monte Carlo bootstrap

and emit a per-mode phase histogram (32 bins).

The audit verifies the Level-1.5 prediction that f_NL = 0.0547
(Pathway A, Type-F state-functional) is invariant across the
mode-distribution variation set under the substrate-canonical
choice of {phi_a}.

Source
------
S86 W-4 §AUDIT-1 (lines 1633-1638).
S86 W-4 CF-2 `S87-TYPE-F-PER-MODE-PHASE-AUDIT` (Level 1.5).
S86 W-4 §VII.O.0 sub-entry text (lines 1458-1479).

Provenance
----------
S86 W0c-7 housekeeping queue Tier-4 row T4-5.
Promoted from S86 W-4 AUDIT-1 (connes-ncg + lizzi, 2026-04-26).

Status
------
SCAFFOLD. Major dependencies marked TODO(S87):
  - Bogoliubov coefficient (alpha_a, beta_a) extraction from S67 / S82 .npz outputs
  - Substrate-canonical w_a weights pin from canonical_constants
  - 32-mode pair-mode indexing (post-tau_fold GGE pair structure)

Usage (post-S87 wire-up)
------------------------
    python _type_f_per_mode_phase_audit.py
    python _type_f_per_mode_phase_audit.py --json
    python _type_f_per_mode_phase_audit.py --bootstrap-n 1000
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

# Number of post-tau_fold GGE pair-modes (canonical pair count from S42 era).
N_PAIR_MODES = 32                                          # (local)

# Expected scalar projection N_A (Pathway A f_NL = 0.0547).
EXPECTED_N_A = 0.0547                                      # (local) — W-4 R3-A

# Acceptance band for Level 1.5 PASS — 5% relative.
N_A_PASS_REL_TOL = 0.05                                    # (local)

# Random-uniform weight distribution support.
RANDOM_W_LOW = 0.5                                         # (local)
RANDOM_W_HIGH = 2.0                                        # (local)

# Bootstrap iterations for variation (iii).
BOOTSTRAP_N_DEFAULT = 1000                                 # (local)


# ---------------------------------------------------------------------------
# Data hooks (TODO scaffolds)
# ---------------------------------------------------------------------------

def load_post_fold_gge_bogoliubov() -> dict:
    """Load post-tau_fold GGE Bogoliubov coefficients (alpha_a, beta_a)
    from S67 / S82 outputs.

    TODO(S87): import from
        sessions/archive/session-67/.../s67_gge_bispectrum.npz
    or
        sessions/archive/session-82/.../s82_w3_4_gge_fnl.npz

    Returns dict with alpha (complex, 32), beta (complex, 32),
    phi (real phase = arg(alpha · beta*²) per mode).
    """
    raise NotImplementedError(
        "TODO(S87): load post-tau_fold GGE Bogoliubov coefficients "
        "from S67 / S82 outputs."
    )


def canonical_substrate_weights() -> np.ndarray:
    """Return substrate-canonical w_a (length 32).

    TODO(S87): pin from canonical_constants once W-4 closes the
    canonical weight choice. Provisional: uniform 1/32.
    """
    raise NotImplementedError(
        "TODO(S87): canonical w_a weights — pin from canonical_constants "
        "or W-4 §VII.O.0 sub-entry definition (lines 1458-1479)."
    )


# ---------------------------------------------------------------------------
# Core audit
# ---------------------------------------------------------------------------

def scalar_projection_N_A(weights: np.ndarray,
                          alpha: np.ndarray,
                          beta: np.ndarray) -> float:
    """N_A = Sum_a w_a · Im[ alpha_a · (beta_a*)^2 ]

    Substitution chain:
        Definition 1: alpha_a, beta_a — Bogoliubov coefficients per pair-mode
        Definition 2: (beta_a*)^2     — squared complex conjugate of beta_a
        Substitute:  N_A = Σ_a w_a · Im[ α_a · (β_a*)² ]
        Simplify:    Im[z] is linear over real weights; well-defined real scalar
        Direction:   weights w_a → uniform ⇒ N_A → ⟨Im[α(β*)²]⟩ (mean projection)
    """
    contributions = np.imag(alpha * np.conj(beta) ** 2)   # (local)
    return float(np.sum(weights * contributions))         # (local)


def run_audit(bootstrap_n: int = BOOTSTRAP_N_DEFAULT,
              rng_seed: int = 42) -> dict:
    """Run Type-F per-mode phase audit across 3 variations."""
    blockers = []                                          # (local)
    try:
        gge = load_post_fold_gge_bogoliubov()             # (local)
    except NotImplementedError as e:
        blockers.append(f"Bogoliubov loader: {e}")
        gge = None

    try:
        w_canon = canonical_substrate_weights()           # (local)
    except NotImplementedError as e:
        blockers.append(f"canonical weights: {e}")
        w_canon = None

    if blockers:
        return {
            "audit_id": "S86-W4-TYPE-F-PER-MODE-PHASE",
            "verdict": "INFO_SCAFFOLD",
            "blocked_by": blockers,
        }

    alpha = gge["alpha"]                                   # (local)
    beta = gge["beta"]                                     # (local)

    # Variation (i): canonical weights.
    n_a_canon = scalar_projection_N_A(w_canon, alpha, beta)  # (local)

    # Variation (ii): even-r (uniform 1/32).
    w_even = np.ones(N_PAIR_MODES) / N_PAIR_MODES          # (local)
    n_a_even = scalar_projection_N_A(w_even, alpha, beta)  # (local)

    # Variation (iii): random-uniform[0.5, 2.0] bootstrap.
    rng = np.random.default_rng(rng_seed)                  # (local)
    boot = []                                              # (local)
    for _ in range(bootstrap_n):
        w = rng.uniform(RANDOM_W_LOW, RANDOM_W_HIGH, N_PAIR_MODES)  # (local)
        w = w / np.sum(w)                                  # (local) — normalize
        boot.append(scalar_projection_N_A(w, alpha, beta))
    boot_arr = np.asarray(boot)                            # (local)

    # Per-mode phase histogram (Im[α(β*)²] per mode).
    phi_per_mode = np.imag(alpha * np.conj(beta) ** 2)    # (local)

    # PASS criterion: dispersion of N_A across variations within 5% rel.
    rel_disp_canon_vs_even = abs(n_a_canon - n_a_even) / abs(n_a_canon)  # (local)
    rel_disp_canon_vs_boot = abs(n_a_canon - float(np.mean(boot_arr))) / abs(n_a_canon)
    pass_canon_vs_expected = abs(n_a_canon - EXPECTED_N_A) / abs(EXPECTED_N_A) < N_A_PASS_REL_TOL

    verdict = "PASS" if (
        rel_disp_canon_vs_even < N_A_PASS_REL_TOL
        and rel_disp_canon_vs_boot < N_A_PASS_REL_TOL
        and pass_canon_vs_expected
    ) else "FAIL"

    return {
        "audit_id": "S86-W4-TYPE-F-PER-MODE-PHASE",
        "verdict": verdict,
        "N_A_canonical": n_a_canon,
        "N_A_even_r": n_a_even,
        "N_A_bootstrap_mean": float(np.mean(boot_arr)),
        "N_A_bootstrap_std": float(np.std(boot_arr)),
        "rel_disp_canon_vs_even": rel_disp_canon_vs_even,
        "rel_disp_canon_vs_boot": rel_disp_canon_vs_boot,
        "pass_canon_vs_expected_0_0547": pass_canon_vs_expected,
        "phi_per_mode_histogram_bins": list(np.histogram(phi_per_mode, bins=N_PAIR_MODES)[0].astype(int)),
        "expected_N_A": EXPECTED_N_A,
        "rel_tol": N_A_PASS_REL_TOL,
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Type-F per-mode phase audit (T4-5 / S87 CF-2)"
    )
    parser.add_argument("--bootstrap-n", type=int, default=BOOTSTRAP_N_DEFAULT,
                        help=f"random-uniform bootstrap iterations (default: {BOOTSTRAP_N_DEFAULT})")
    parser.add_argument("--seed", type=int, default=42,
                        help="RNG seed (default: 42)")
    parser.add_argument("--json", action="store_true",
                        help="emit machine-readable JSON")
    args = parser.parse_args()

    result = run_audit(args.bootstrap_n, args.seed)       # (local)

    if args.json:
        print(json.dumps(result, indent=2, default=str))
    else:
        print("=== S86 W-4 / S87 CF-2 Type-F Per-Mode Phase Audit ===")
        print(f"Verdict: {result['verdict']}")
        for k, v in result.items():
            if k in ("verdict", "audit_id"):
                continue
            print(f"  {k}: {v}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
