"""
_hankel_psd_channel_3e_audit.py

Hankel-PSD audit for channel-3e classification
(T4-12, S86 W-8 AUDIT-1).

Purpose
-------
Hankel matrices

    H_n = (M_{i+j})_{i, j = 0..n}

PSD test on the M_{2k} sequence for k = 0..5. Required for the
anomaly Pauli-Villars classification per channel-3e definition
(W-8 lines 1782-1798).

The Stieltjes-Hamburger moment problem (Akhiezer 1965, Ch. 1)
identifies a moment sequence {M_n} as having a positive measure
representation iff the associated Hankel matrices are PSD for all n.

Substitution chain (Hankel-PSD ⇒ moment-problem solvability):

    Definition 1: M_k     — k-th moment of regulator residue at f_6 = 0.1
    Definition 2: H_n     — Hankel matrix (M_{i+j})_{i,j=0..n}
    Definition 3: PSD(H)  — H is positive semi-definite iff all
                            eigenvalues of (H + H^*)/2 are ≥ −eig_tol
    Substitute:   channel-3e classification:
                    PSD for all n ≤ 5 ⇒ valid moment sequence ⇒
                                          channel-3e PASS (Pauli-Villars
                                          anomaly is well-defined)
                    PSD violated      ⇒ channel-3e FAIL (no positive
                                          measure representation)
    Direction:    smallest eigenvalue ↑ → PSD margin grows
                  smallest eigenvalue < −eig_tol → PSD violated

Source
------
S86 W-8 §AUDIT-1 (lines 37-39).
S86 W-8 channel-3e definition (workshop lines 1782-1798).
S86 W-8 CF-4 `S87-HBW-AUDIT-ATLAS-A_4` (lines 2106-2128).
Akhiezer, N. I. (1965). "The Classical Moment Problem", Ch. 1.

Provenance
----------
S86 W0c-7 housekeeping queue Tier-4 row T4-12.
Promoted from S86 W-8 AUDIT-1 (connes-ncg + lizzi, 2026-04-26).

Status
------
SCAFFOLD. Major dependencies marked TODO(S87):
  - M_{2k} sequence for the candidate regulator (anomaly /
    Pauli-Villars / others) must be supplied by an upstream Sage MCP
    closed-form computation.

Usage (post-S87 wire-up)
------------------------
    python _hankel_psd_channel_3e_audit.py --regulator anomaly
    python _hankel_psd_channel_3e_audit.py --moments 1.0 0.5 0.333 ...
    python _hankel_psd_channel_3e_audit.py --json
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

# Maximum k for the M_{2k} sequence (W-8 AUDIT-1 spec: k = 0..5).
K_MAX_DEFAULT = 5                                          # (local)

# Eigenvalue tolerance for PSD declaration (small negative values
# accepted as numerical noise).
EIG_TOL_DEFAULT = 1e-12                                    # (local)

# Channel-3e classification labels.
CH3E_PASS = "channel-3e_PASS"                              # (local)
CH3E_FAIL = "channel-3e_FAIL"                              # (local)
CH3E_MARGINAL = "channel-3e_MARGINAL"                      # (local)


# ---------------------------------------------------------------------------
# Moment-loading hook (TODO scaffold)
# ---------------------------------------------------------------------------

def load_moments_for_regulator(regulator: str, k_max: int = K_MAX_DEFAULT) -> list[float]:
    """Load M_{2k} moment sequence for k = 0..k_max for a regulator.

    TODO(S87): integrate with Sage MCP closed-form M_{2k} computation
    per W-8 CF-4 spec. Sources: anomaly regulator → M_6 via Sage
    (W-8 line 142 — "M_6 via Sage MCP closed form").
    """
    raise NotImplementedError(
        f"TODO(S87): load_moments_for_regulator({regulator}, k_max={k_max}) "
        "requires Sage MCP closed-form moment computation per W-8 CF-4."
    )


# ---------------------------------------------------------------------------
# Core audit
# ---------------------------------------------------------------------------

def hankel_matrix(moments: list[float], n: int) -> np.ndarray:
    """Build the (n+1) × (n+1) Hankel matrix H_n = (M_{i+j})_{i, j = 0..n}.

    Requires the moment sequence to have at least 2n + 1 entries.
    """
    if len(moments) < 2 * n + 1:
        raise ValueError(
            f"Need at least {2*n+1} moments for Hankel order n={n}; "
            f"got {len(moments)}"
        )
    H = np.zeros((n + 1, n + 1), dtype=np.float64)         # (local)
    for i in range(n + 1):
        for j in range(n + 1):
            H[i, j] = moments[i + j]
    return H


def is_psd(H: np.ndarray, eig_tol: float = EIG_TOL_DEFAULT) -> tuple[bool, float]:
    """Check whether H is positive semi-definite.

    Returns (is_psd, smallest_eigenvalue). PSD iff smallest_eig ≥ -eig_tol.
    """
    H_sym = 0.5 * (H + H.conj().T)                         # (local)
    eigs = np.linalg.eigvalsh(H_sym)                       # (local)
    smallest = float(np.min(eigs))                         # (local)
    return smallest >= -eig_tol, smallest


def channel_3e_classify(moments: list[float],
                        k_max: int = K_MAX_DEFAULT,
                        eig_tol: float = EIG_TOL_DEFAULT) -> dict:
    """Classify channel-3e via Hankel-PSD test on M_{2k} for k = 0..k_max."""
    rows = []                                              # (local)
    all_psd = True                                         # (local)
    for n in range(k_max + 1):
        try:
            H_n = hankel_matrix(moments, n)               # (local)
            psd, smallest = is_psd(H_n, eig_tol)          # (local)
            rows.append({
                "n": n,
                "matrix_dim": n + 1,
                "is_psd": psd,
                "smallest_eig": smallest,
            })
            if not psd:
                all_psd = False
        except ValueError as e:
            rows.append({"n": n, "error": str(e)})
            all_psd = False
            break

    if all_psd:
        classification = CH3E_PASS
    else:
        # Marginal if at least one Hankel PASSes but not all.
        any_psd = any(r.get("is_psd", False) for r in rows)
        classification = CH3E_MARGINAL if any_psd else CH3E_FAIL

    return {
        "k_max": k_max,
        "moments_count": len(moments),
        "eig_tol": eig_tol,
        "classification": classification,
        "all_psd": all_psd,
        "hankel_tests": rows,
    }


def run_audit(regulator: str | None = None,
              moments: list[float] | None = None,
              k_max: int = K_MAX_DEFAULT) -> dict:
    """Top-level audit dispatch."""
    if moments is None:
        if regulator is None:
            return {
                "audit_id": "S86-W8-HANKEL-PSD-CHANNEL-3E",
                "verdict": "INFO_SCAFFOLD",
                "blocked_by": "Either --regulator or --moments must be supplied",
            }
        try:
            moments = load_moments_for_regulator(regulator, k_max)  # (local)
        except NotImplementedError as e:
            return {
                "audit_id": "S86-W8-HANKEL-PSD-CHANNEL-3E",
                "verdict": "INFO_SCAFFOLD",
                "blocked_by": str(e),
                "regulator": regulator,
            }

    result = channel_3e_classify(moments, k_max)          # (local)
    verdict = "PASS" if result["classification"] == CH3E_PASS else (
        "INFO" if result["classification"] == CH3E_MARGINAL else "FAIL"
    )

    return {
        "audit_id": "S86-W8-HANKEL-PSD-CHANNEL-3E",
        "verdict": verdict,
        "regulator": regulator,
        **result,
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Hankel-PSD audit for channel-3e classification (T4-12 / S86 W-8 AUDIT-1)"
    )
    parser.add_argument("--regulator", type=str, default=None,
                        help="regulator name (loaded via Sage MCP closed-form)")
    parser.add_argument("--moments", type=float, nargs="+", default=None,
                        help="explicit M_{2k} sequence (k=0..k_max)")
    parser.add_argument("--k-max", type=int, default=K_MAX_DEFAULT,
                        help=f"max k for M_{{2k}} (default: {K_MAX_DEFAULT})")
    parser.add_argument("--json", action="store_true",
                        help="emit machine-readable JSON")
    args = parser.parse_args()

    result = run_audit(args.regulator, args.moments, args.k_max)  # (local)

    if args.json:
        print(json.dumps(result, indent=2, default=str))
    else:
        print("=== S86 W-8 Hankel-PSD channel-3e Audit (T4-12) ===")
        print(f"Verdict: {result['verdict']}")
        print(f"Regulator: {result.get('regulator', '<explicit moments>')}")
        if "blocked_by" in result:
            print(f"Blocked by: {result['blocked_by']}")
        else:
            print(f"k_max: {result['k_max']}")
            print(f"All PSD: {result.get('all_psd')}")
            print(f"Classification: {result.get('classification')}")
            for r in result.get("hankel_tests", []):
                if "error" in r:
                    print(f"  n={r['n']}: ERROR — {r['error']}")
                else:
                    flag = "PSD" if r["is_psd"] else "NOT-PSD"
                    print(f"  n={r['n']} dim={r['matrix_dim']}: "
                          f"smallest_eig={r['smallest_eig']:+.3e}  [{flag}]")

    return 0


if __name__ == "__main__":
    sys.exit(main())
