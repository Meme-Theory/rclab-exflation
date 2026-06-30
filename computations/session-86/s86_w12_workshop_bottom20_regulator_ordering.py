"""
S86 Slot 2 Workshop W-12 (Bimodality + 4-Fold Cardinality Coincidence)
Connes Track A — C1+C2: Bottom-20 D_K eigenvalue ordering at tau_fold=0.190 under
the 5-regulator atlas A_5 = {zeta, Pauli-Villars, Mellin, lattice, cutoff_sqrt}.

Substitution chain (plain text in workshop §C1):
  - x_i := |lambda_i|^2 / Lambda^2,  Lambda = M_KK
  - bottom-20 cut: smallest 20 entries of |lambda| over the spectrum
  - apply regulator weight w_R(x_i); record the rank permutation vs zeta-baseline

Workshop output: ranking tables + ordering-permutation summary written to JSON.
Dual-SHA dispatched separately at workshop closure (this is a workshop-side
diagnostic computation, not a registry-grade gate).
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))

from canonical_constants import M_KK, tau_fold

# ---- 1. Load cached D_K spectrum at tau_fold (S84 cache, L_max=12) -----
CACHE = Path(__file__).resolve().parent / "s84_spectrum_cache_L12_tau019.npz"
d = np.load(CACHE, allow_pickle=True)
sec_dict = d["sector_evals"].item()  # {(p,q): {dim, level, abs_evals}}

# Aggregate ALL absolute eigenvalues, tagging each with sector label.
all_abs: list[tuple[float, tuple[int, int]]] = []  # (|lambda|, (p,q))  # (local)
for (p, q), payload in sec_dict.items():
    abs_evals = np.asarray(payload["abs_evals"], dtype=np.float64)
    for lam in abs_evals:
        all_abs.append((float(lam), (p, q)))

# Sort ascending by |lambda|.
all_abs.sort(key=lambda t: t[0])
N_total = len(all_abs)  # (local)

# ---- 2. Bottom-20 cut ----------------------------------------------------
N_BOT = 20  # (local)
bottom20 = all_abs[:N_BOT]  # (local)

# Eigenvalues in dimensionless form (x = |lambda|^2 / Lambda^2 with Lambda=1 here
# because the cache stores |lambda| in M_KK units; physical scale absorbed in M_KK).
abs_lams = np.array([t[0] for t in bottom20], dtype=np.float64)
sectors = [t[1] for t in bottom20]
x_vals = abs_lams ** 2  # (local) dimensionless x = |lambda|^2 (Lambda set to 1)

# ---- 3. Five regulator weight functions ---------------------------------
# Defined per regulator-pin-discipline.md atlas A_5; FORMULAS PER WORKSHOP PIN.
EPS = 1e-30  # (local) numerical floor

def w_zeta(x: np.ndarray) -> np.ndarray:
    # zeta-regularization: rank-equivalent to identity ordering on bare |lambda|.
    return x.copy()

def w_PV(x: np.ndarray, kappa_PV: float = 1.0) -> np.ndarray:
    # Pauli-Villars: w_PV(x) = x * (LambdaPV^2 / (x + LambdaPV^2))^2
    # kappa_PV pinned to 1.0 (workshop convention; canonical PV is order-1).
    L2 = kappa_PV ** 2
    return x * (L2 / (x + L2)) ** 2

def w_Mellin(x: np.ndarray, s_star: float = 3.0) -> np.ndarray:
    # Mellin moment x^{-s_star} (W2-C9 cone moment; rank-INVERTING).
    safe_x = np.maximum(x, EPS)
    return safe_x ** (-s_star)

def w_lattice(x: np.ndarray, a: float = 1.0 / 12.0) -> np.ndarray:
    # Lattice: w_L(x; a) = (4/a^2) sin^2(a |lambda|/2), with |lambda| = sqrt(x).
    abs_lam = np.sqrt(np.maximum(x, 0.0))
    return (4.0 / a ** 2) * np.sin(a * abs_lam / 2.0) ** 2

def w_cutoff_sqrt(x: np.ndarray, Lc2: float = 144.0) -> np.ndarray:
    # cutoff_sqrt with sharp cutoff Lambda_c^2 = 144 dimless (L_max=12).
    safe_x = np.maximum(x, 0.0)
    out = np.sqrt(safe_x)
    out[x > Lc2] = 0.0
    return out

REGULATORS = {
    "zeta": w_zeta,
    "Pauli-Villars": w_PV,
    "Mellin": w_Mellin,
    "lattice": w_lattice,
    "cutoff_sqrt": w_cutoff_sqrt,
}

# ---- 4. Ordering tables --------------------------------------------------
# For each regulator, sort bottom-20 by w_R(x) and record the rank permutation
# relative to zeta-baseline (which is identity-ordering on |lambda|).
order_tables: dict[str, dict] = {}
zeta_order_idx = list(range(N_BOT))  # bottom-20 already sorted by |lambda|.

for name, weight_fn in REGULATORS.items():
    w = weight_fn(x_vals)
    # Sort by w in DESCENDING magnitude (largest weight = "first" mode).
    sort_idx = np.argsort(w)[::-1].tolist()
    # Inverse: position-in-sorted-order for each original index.
    rank_of_orig = [0] * N_BOT
    for pos, orig in enumerate(sort_idx):
        rank_of_orig[orig] = pos
    order_tables[name] = {
        "weight_values": w.tolist(),
        "sort_idx": sort_idx,
        "rank_of_original": rank_of_orig,
    }

# ---- 5. Pairwise ordering-difference matrix -----------------------------
names = list(REGULATORS.keys())
n_R = len(names)
diff_matrix = np.zeros((n_R, n_R), dtype=int)
kendall_tau = np.zeros((n_R, n_R), dtype=np.float64)

def kendall(a: list[int], b: list[int]) -> float:
    """Kendall tau between two rank vectors a, b of equal length."""
    n = len(a)
    if n < 2:
        return 1.0
    concordant = 0  # (local)
    discordant = 0  # (local)
    for i in range(n):
        for j in range(i + 1, n):
            ai, aj = a[i], a[j]
            bi, bj = b[i], b[j]
            s_a = (ai - aj)
            s_b = (bi - bj)
            prod = s_a * s_b
            if prod > 0:
                concordant += 1
            elif prod < 0:
                discordant += 1
    denom = n * (n - 1) // 2
    return (concordant - discordant) / denom if denom else 1.0

for i, ni in enumerate(names):
    for j, nj in enumerate(names):
        if i == j:
            continue
        rank_i = order_tables[ni]["rank_of_original"]
        rank_j = order_tables[nj]["rank_of_original"]
        # Number of positions where rank differs.
        diff_matrix[i, j] = sum(1 for k in range(N_BOT) if rank_i[k] != rank_j[k])
        kendall_tau[i, j] = kendall(rank_i, rank_j)

# ---- 6. Identify level-crossing candidates ------------------------------
# Search for near-degenerate eigenvalues across full spectrum where regulator
# could split a degenerate level. Use gap < tol_gap as candidate crossing site.
TOL_GAP = 1e-4  # (local) numerical degeneracy tolerance
crossing_candidates: list[dict] = []

# Operate on all eigenvalues (across all sectors) sorted by |lambda|.
all_sorted = all_abs[:200]  # (local) inspect bottom-200 for crossing-density profile
for k in range(len(all_sorted) - 1):
    gap = all_sorted[k + 1][0] - all_sorted[k][0]
    if gap < TOL_GAP:
        crossing_candidates.append({
            "k": k,
            "lam_k": all_sorted[k][0],
            "lam_kplus1": all_sorted[k + 1][0],
            "gap": gap,
            "sector_k": all_sorted[k][1],
            "sector_kplus1": all_sorted[k + 1][1],
        })

# ---- 7. Output ----------------------------------------------------------
output = {
    "session": "S86",
    "workshop": "Slot 2 W-12 (Bimodality + 4-Fold Cardinality)",
    "track": "A (connes)",
    "tau_fold": float(tau_fold),
    "L_max": 12,
    "M_KK": float(M_KK),
    "N_total_eigenvalues": N_total,
    "N_bottom": N_BOT,
    "bottom20_abs_lambda": abs_lams.tolist(),
    "bottom20_sectors": [list(s) for s in sectors],
    "regulator_atlas_A5": names,
    "order_tables": order_tables,
    "diff_matrix": diff_matrix.tolist(),
    "kendall_tau_matrix": kendall_tau.tolist(),
    "row_col_legend": names,
    "crossing_candidates_bottom200": crossing_candidates,
    "crossing_count_bottom200": len(crossing_candidates),
    "tol_gap": TOL_GAP,
    "interpretation_substitution_chain": (
        "x_i = |lambda_i|^2 (Lambda=M_KK absorbed). "
        "w_zeta = x (monotone increasing); w_PV = x * (1/(x+1))^2 (monotone increasing in x for x small, "
        "non-monotone above the PV-pole; bottom-20 |lambda|<<1 so monotone here); "
        "w_Mellin = x^{-3} (monotone DECREASING in x => global rank inversion vs zeta); "
        "w_lattice = (4/a^2) sin^2(a sqrt(x)/2), a=1/12 (monotone in x for sqrt(x)*a < pi i.e. |lambda| < 12*pi); "
        "w_cutoff_sqrt = sqrt(x) * theta(144 - x) (monotone increasing for bottom-20 since x<<144). "
        "Therefore on bottom-20: 4 of 5 regulators (zeta, PV, lattice, cutoff_sqrt) produce IDENTICAL ranking; "
        "Mellin produces the GLOBAL REVERSAL of that ranking. "
        "BIMODALITY signature on bottom-20 reduces to MONOTONE-INCREASING vs MONOTONE-DECREASING dichotomy, "
        "i.e. a Z_2 ordering structure on bottom-20 — NOT a higher-order regulator-dependent splitting."
    ),
}

OUT = Path(__file__).resolve().parent / "s86_w12_workshop_bottom20_regulator_ordering.json"
OUT.write_text(json.dumps(output, indent=2))
print(f"Written: {OUT}")
print()
print(f"N_total eigenvalues at tau_fold=0.190 L_max=12: {N_total}")
print(f"Bottom-20 |lambda| range: [{abs_lams.min():.6f}, {abs_lams.max():.6f}]")
print()
print("Bottom-20 ranks under each regulator (rank_of_original):")
for name in names:
    rs = order_tables[name]["rank_of_original"]
    print(f"  {name:14s}: {rs}")
print()
print("Pairwise ordering-difference matrix (count of positions w/ different rank):")
print(f"  {'':14s}", " ".join(f"{n:>12s}" for n in names))
for i, ni in enumerate(names):
    print(f"  {ni:14s}", " ".join(f"{diff_matrix[i, j]:>12d}" for j in range(n_R)))
print()
print("Pairwise Kendall tau (rank correlation):")
for i, ni in enumerate(names):
    print(f"  {ni:14s}", " ".join(f"{kendall_tau[i, j]:+.4f}" for j in range(n_R)))
print()
print(f"Near-degenerate gaps (gap<{TOL_GAP}) in bottom-200: {len(crossing_candidates)}")
if crossing_candidates:
    for c in crossing_candidates[:10]:
        print(f"  k={c['k']:3d} |lam|={c['lam_k']:.6f} gap={c['gap']:.2e} sec1={c['sector_k']} sec2={c['sector_kplus1']}")
