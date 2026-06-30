"""
_cross_level_lambda_collision_extractor.py

Cross-level |λ|-collision spectrum-cache extractor (utility)
(T4-21, S86 W-10 AUDIT-W10-4).

Purpose
-------
Generic substrate-spectrum order-N pole structural test. Extracts:

    CL_count    := #{ λ_value : λ_value appears in ≥ 2 distinct
                                 sectors with disjoint level indices }
    N_distinct  := #{ distinct rounded |λ| values to 6 decimals }

Then tests CL_count / N_distinct against the calibrated significance
threshold

    ε_pole_significance = 0.05

Already exercised in W-10 §C2 (reference outcome at L=12, τ_fold=0.190):
    CL count: 2
    N distinct: 6995
    ratio: 2 / 6995 ≈ 2.86e-4

Substitution chain (cross-level collision rate):

    Definition 1: spectrum cache C := {(sector, level_index, λ_value)}
                  loaded from `s84_spectrum_cache_L{L}_tau019.npz`
    Definition 2: round_lambda(λ) := round(|λ|, 6) — 6-decimal
                  fingerprint
    Definition 3: CL_count := count of round_lambda values that
                  appear in 2+ distinct sectors with disjoint
                  level indices (cross-level collision)
    Definition 4: N_distinct := count of unique round_lambda values
    Substitute:  collision_ratio = CL_count / N_distinct
    Simplify:    collision_ratio numeric (e.g. 2/6995 ≈ 2.86e-4)
    Direction:   ratio < 0.05 ⇒ NO significant cross-level pole structure
                                  (random-coincidence regime; substrate
                                   spectra are sector-disjoint at the
                                   |λ|-fingerprint resolution)
                 ratio ≥ 0.05 ⇒ significant pole structure detected
                                  (additional sector-degeneracy
                                   evidence; downstream gate trigger)

Source
------
S86 W-10 §AUDIT-W10-4 (lines 88-92).
S86 W-10 §L2 Step 4 + Re:L2 + C2 (workshop lines 191-204, 503-558,
786-869).
Existing exemplar: §C2 result CL_count = 2 / N_distinct = 6995 at
L = 12, τ_fold = 0.190.

Provenance
----------
S86 W0c-7 housekeeping queue Tier-4 row T4-21.
Promoted from S86 W-10 AUDIT-W10-4 (connes + lizzi, 2026-04-26).

Status
------
SCAFFOLD with ACTIVE COLLISION-COUNTING UTILITY. Spectrum-cache
loader marked TODO(S87) for the canonical-cache path resolution.

Usage
-----
    python _cross_level_lambda_collision_extractor.py --L 12
    python _cross_level_lambda_collision_extractor.py --json
    python _cross_level_lambda_collision_extractor.py --cache-path s84_spectrum_cache_L12_tau019.npz
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from collections import defaultdict
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

# ε_pole_significance threshold (W-10 AUDIT-W10-4 calibration).
EPS_POLE_SIGNIFICANCE = 0.05                               # (local)

# Fingerprint rounding precision (6 decimals per W-10 spec).
LAMBDA_ROUND_DECIMALS = 6                                  # (local)

# Default τ value (W-10 §C2 anchor).
TAU_FOLD_DEFAULT = 0.190                                   # (local)

# Default L_max (W-10 §C2 anchor).
L_MAX_DEFAULT = 12                                         # (local)

# Default spectrum cache path (W-10 spec name).
DEFAULT_CACHE_NAME_TEMPLATE = "s84_spectrum_cache_L{L}_tau{tau_str}.npz"  # (local)


# ---------------------------------------------------------------------------
# Hooks (TODO scaffold)
# ---------------------------------------------------------------------------

def _format_tau(tau: float) -> str:
    """Format τ value as cache filename suffix (e.g., 0.190 → '019')."""
    return f"{int(round(tau * 1000)):03d}"


def load_spectrum_cache(L_max: int = L_MAX_DEFAULT,
                        tau_fold: float = TAU_FOLD_DEFAULT,
                        cache_path: str | None = None) -> dict:
    """Load spectrum cache .npz file.

    Expected to contain arrays:
      - sector_ids   (int)           — sector tag per eigenvalue
      - level_indices (int)          — level index within sector
      - lambda_values (float)        — eigenvalue (signed)

    TODO(S87): pin the canonical cache location once W-10 reference
    cache `s84_spectrum_cache_L12_tau019.npz` is restored to a
    discoverable path under `computations/_shared/` or `sessions/archive/session-84/`.
    """
    if cache_path is None:
        cache_path = DEFAULT_CACHE_NAME_TEMPLATE.format(
            L=L_max, tau_str=_format_tau(tau_fold)
        )
    p = Path(cache_path)
    if not p.exists():
        # Search likely roots.
        roots = [
            Path(__file__).resolve().parent,
            Path(__file__).resolve().parent.parent / "computation archive",
            Path(__file__).resolve().parent.parent / "sessions",
        ]
        for root in roots:
            for found in root.rglob(p.name):
                p = found
                break
            if p.exists():
                break
    if not p.exists():
        raise FileNotFoundError(
            f"TODO(S87): spectrum cache {cache_path} not found in standard "
            f"roots; pin canonical path per W-10 AUDIT-W10-4 spec."
        )
    data = np.load(p, allow_pickle=True)                  # (local)
    return {
        "path": str(p),
        "sector_ids": np.asarray(data["sector_ids"]),
        "level_indices": np.asarray(data["level_indices"]),
        "lambda_values": np.asarray(data["lambda_values"]),
    }


# ---------------------------------------------------------------------------
# Core extraction logic
# ---------------------------------------------------------------------------

def cross_level_collision_count(sector_ids: np.ndarray,
                                level_indices: np.ndarray,
                                lambda_values: np.ndarray,
                                round_decimals: int = LAMBDA_ROUND_DECIMALS,
                                ) -> dict:
    """Compute CL_count and N_distinct from a spectrum cache."""
    abs_lambda = np.abs(lambda_values)                     # (local)
    fingerprints = np.round(abs_lambda, round_decimals)   # (local)

    # Group level indices by (fingerprint, sector_id).
    sectors_by_fp = defaultdict(set)                       # (local)
    levels_by_fp_sector = defaultdict(set)                 # (local)

    for i, fp in enumerate(fingerprints):
        sec = int(sector_ids[i])                          # (local)
        lvl = int(level_indices[i])                       # (local)
        sectors_by_fp[float(fp)].add(sec)
        levels_by_fp_sector[(float(fp), sec)].add(lvl)

    # CL_count: fingerprints that appear in ≥ 2 distinct sectors AND
    # those sector-occurrences have disjoint level index sets
    # (i.e., not the same level shared across sector relabels).
    cl_count = 0                                           # (local)
    cl_examples = []                                       # (local)
    for fp, secs in sectors_by_fp.items():
        if len(secs) < 2:
            continue
        # Check level-index disjointness across sectors.
        all_level_sets = [levels_by_fp_sector[(fp, s)] for s in secs]
        union = set().union(*all_level_sets)
        sum_lengths = sum(len(s) for s in all_level_sets)
        disjoint = (sum_lengths == len(union))
        if disjoint:
            cl_count += 1
            if len(cl_examples) < 5:
                cl_examples.append({
                    "fingerprint": fp,
                    "n_sectors": len(secs),
                    "sectors": sorted(secs),
                })

    n_distinct = len(sectors_by_fp)                       # (local)
    ratio = cl_count / n_distinct if n_distinct else 0.0  # (local)

    return {
        "CL_count": cl_count,
        "N_distinct": n_distinct,
        "collision_ratio": ratio,
        "round_decimals": round_decimals,
        "examples_first_5": cl_examples,
    }


def run_audit(L_max: int = L_MAX_DEFAULT,
              tau_fold: float = TAU_FOLD_DEFAULT,
              cache_path: str | None = None) -> dict:
    """Top-level extractor."""
    try:
        cache = load_spectrum_cache(L_max, tau_fold, cache_path)
    except (FileNotFoundError, NotImplementedError) as e:
        return {
            "audit_id": "S86-W10-CROSS-LEVEL-LAMBDA-COLLISION",
            "verdict": "INFO_SCAFFOLD",
            "blocked_by": str(e),
            "L_max": L_max,
            "tau_fold": tau_fold,
        }

    summary = cross_level_collision_count(
        cache["sector_ids"], cache["level_indices"], cache["lambda_values"]
    )                                                      # (local)
    significant = summary["collision_ratio"] >= EPS_POLE_SIGNIFICANCE  # (local)

    return {
        "audit_id": "S86-W10-CROSS-LEVEL-LAMBDA-COLLISION",
        "verdict": "INFO" if significant else "PASS",
        "L_max": L_max,
        "tau_fold": tau_fold,
        "spectrum_cache_path": cache["path"],
        "epsilon_pole_significance": EPS_POLE_SIGNIFICANCE,
        "significant_pole_structure_detected": significant,
        **summary,
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Cross-level |λ|-collision spectrum-cache extractor (T4-21 / S86 W-10)"
    )
    parser.add_argument("--L", type=int, default=L_MAX_DEFAULT,
                        help=f"L_max (default: {L_MAX_DEFAULT})")
    parser.add_argument("--tau-fold", type=float, default=TAU_FOLD_DEFAULT,
                        help=f"τ_fold (default: {TAU_FOLD_DEFAULT})")
    parser.add_argument("--cache-path", type=str, default=None,
                        help="explicit spectrum cache .npz path")
    parser.add_argument("--json", action="store_true",
                        help="emit machine-readable JSON")
    args = parser.parse_args()

    result = run_audit(args.L, args.tau_fold, args.cache_path)  # (local)

    if args.json:
        print(json.dumps(result, indent=2, default=str))
    else:
        print("=== S86 W-10 / T4-21 Cross-Level |λ|-Collision Extractor ===")
        print(f"Verdict: {result['verdict']}")
        for k, v in result.items():
            if k in ("verdict", "audit_id", "examples_first_5"):
                continue
            print(f"  {k}: {v}")
        if "examples_first_5" in result:
            print("  Examples (first 5):")
            for ex in result["examples_first_5"]:
                print(f"    fingerprint={ex['fingerprint']}, "
                      f"n_sectors={ex['n_sectors']}, sectors={ex['sectors']}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
