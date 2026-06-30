#!/usr/bin/env python3
"""
s58_gap_cg.py — Many-Body Gap Scaling on the Physical CG(24) Cayley Graph
===========================================================================
Session 58, W2-1: GAP-CG-58

S57 found Delta_N ~ N^{-1.84} on a LINEAR CHAIN (degree 2, uniform J_C2).
This script tests whether the same exponent transfers to the physical
Cayley graph CG(24) of SU(3), which has:
  - 32 cells (irreps up to p+q <= 6)
  - 93 bonds (50 C2, 24 su2, 19 u1) with bond-type-dependent J
  - Non-uniform degree distribution (2 to 8, mean 5.8)
  - Diameter 6

METHOD:
  For N = 2, 4, 8, 16, 32 cells, grow connected BFS subgraphs from
  the (0,0) singlet. Construct the N-cell BCS Hamiltonian:

    H_N = sum_i H_cell(i) + sum_{<i,j>} (-J_{type}) * J_inter(i,j)

  TWO models:
    A) Diagonal Josephson: J_inter = delta_{kl} (same mode on neighbor cells)
    B) Full Josephson: J_inter = F_kl (normalized anomalous propagator)

  In both models, J_{type} is the bond-type-specific coupling:
    J_C2 = 0.9186, J_su2 = 0.0604, J_u1 = 0.0377 at the fold.
  This is the key difference from S57, which used uniform J_C2 for all bonds.

  Diagonalize with scipy.linalg.eigh (exact, dim <= 256).
  Extract Delta_N = E_1 - E_0. Fit Delta_N ~ N^alpha.

SPECTRAL DIMENSION:
  Compute d_s from pair return probability P(t) ~ t^{-d_s/2} on the
  CG(24) weighted Laplacian. Extract z from alpha = -z/d_s.

Gate: GAP-CG-58
  PASS: alpha in [-2.21, -1.47] (within 20% of chain -1.84)
  FAIL: alpha > 0
  INFO: alpha in [-2.5, -1.47] or [-1.47, 0]

Author: gen-physicist, Session 58
Date: 2026-03-23
"""

import numpy as np
from scipy.linalg import eigh
from scipy.sparse.csgraph import breadth_first_order, connected_components
from pathlib import Path
import sys
import time

sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import (
    tau_fold, E_cond, J_C2, J_su2, J_u1, N_dof_BCS,
    E_cond_ED_8mode, Delta_0_GL, M_max_thouless,
)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

data_dir = Path(__file__).parent
t_start = time.time()

N_MODES = 8  # BCS modes per cell (local)

print("=" * 78)
print("GAP-CG-58: Many-Body Gap Scaling on the Physical CG(24) Graph")
print("=" * 78)

# ============================================================================
# Section 1: Load Data
# ============================================================================

print("\n--- Section 1: Loading Data ---")

d_tb = np.load(data_dir / 's54_tb_hamiltonian.npz', allow_pickle=True)
tau_values = d_tb['tau_values']
eigenvalues = d_tb['eigenvalues']
adj_full = d_tb['adjacency'].astype(np.float64)  # 32x32 unweighted
adj_C2 = d_tb['adj_C2'].astype(np.float64)
adj_su2 = d_tb['adj_su2'].astype(np.float64)
adj_u1 = d_tb['adj_u1'].astype(np.float64)
J_C2_tau = d_tb['J_C2_tau']
J_su2_tau = d_tb['J_su2_tau']
J_u1_tau = d_tb['J_u1_tau']
cell_labels = d_tb['cell_labels']
cell_dims = d_tb['cell_dims']

d_ed = np.load(data_dir / 's54_ed_sweep.npz', allow_pickle=True)
V_bare_cont = d_ed['V_bare_cont']    # (8, 8) continuum pairing
E_sp_sweep = d_ed['E_sp_sweep']      # (50, 8)
fold_idx = int(d_ed['fold_idx'])
tau_init_idx = 0

print(f"Loaded: {len(tau_values)} tau values, fold at idx={fold_idx} "
      f"(tau={tau_values[fold_idx]:.6f})")

# Load S57 chain results for comparison
d57 = np.load(data_dir / 's57_gap_scaling.npz', allow_pickle=True)
alpha_chain = float(d57['alpha_B_large'])
print(f"S57 chain alpha (Model B, N>=8): {alpha_chain:.4f}")

# Josephson couplings at fold
J_C2_fold = J_C2_tau[fold_idx]
J_su2_fold = J_su2_tau[fold_idx]
J_u1_fold = J_u1_tau[fold_idx]
print(f"J at fold: C2={J_C2_fold:.6f}, su2={J_su2_fold:.6f}, u1={J_u1_fold:.6f}")

# At tau=0
J_C2_init = J_C2_tau[tau_init_idx]
J_su2_init = J_su2_tau[tau_init_idx]
J_u1_init = J_u1_tau[tau_init_idx]
print(f"J at init: C2={J_C2_init:.6f}, su2={J_su2_init:.6f}, u1={J_u1_init:.6f}")

# Validate against known N=1 result
evals_N1_stored = d_ed['all_eigenvalues_N1'][fold_idx]
print(f"N=1 stored: E0={evals_N1_stored[0]:.6f}, "
      f"gap={evals_N1_stored[1]-evals_N1_stored[0]:.6f}")

# Anomalous propagator for Model B
V_max = np.max(np.abs(V_bare_cont))
F_inter = V_bare_cont / V_max
print(f"V_max = {V_max:.6f} M_KK")
print(f"F_inter norm: {np.linalg.norm(F_inter):.4f}")

# ============================================================================
# Section 2: CG(24) Subgraph Construction
# ============================================================================

print("\n--- Section 2: CG(24) Subgraph Construction ---")

# BFS from (0,0) singlet
singlet_idx = None
for i in range(32):
    if cell_labels[i][0] == 0 and cell_labels[i][1] == 0:
        singlet_idx = i
        break
assert singlet_idx is not None, "Singlet (0,0) not found"

bfs_order, _ = breadth_first_order(adj_full, singlet_idx, directed=False)
print(f"BFS from (0,0): order = {bfs_order}")


def get_subgraph(N):
    """Return N-cell connected subgraph of CG(24) via BFS from singlet.

    Returns:
        nodes: array of N cell indices
        adj_C2_sub: NxN C2 adjacency
        adj_su2_sub: NxN su2 adjacency
        adj_u1_sub: NxN u1 adjacency
    """
    nodes = bfs_order[:N]
    idx = np.ix_(nodes, nodes)
    return nodes, adj_C2[idx], adj_su2[idx], adj_u1[idx]


def weighted_adjacency(adj_c2, adj_s2, adj_u, J_c2, J_s2, J_u):
    """Bond-type-weighted adjacency matrix."""
    return J_c2 * adj_c2 + J_s2 * adj_s2 + J_u * adj_u


for N in [2, 4, 8, 16, 32]:
    nodes, ac2, as2, au1 = get_subgraph(N)
    n_C2 = int(ac2.sum()) // 2
    n_su2 = int(as2.sum()) // 2
    n_u1 = int(au1.sum()) // 2
    Aw = weighted_adjacency(ac2, as2, au1, J_C2_fold, J_su2_fold, J_u1_fold)
    degrees = Aw.sum(axis=1)
    node_labels = [f"({cell_labels[n][0]},{cell_labels[n][1]})" for n in nodes]
    print(f"  N={N:2d}: bonds C2={n_C2} su2={n_su2} u1={n_u1} total={n_C2+n_su2+n_u1}")
    print(f"         mean_degree(weighted)={degrees.mean():.3f}, "
          f"max={degrees.max():.3f}")
    if N <= 8:
        print(f"         cells: {node_labels}")

# ============================================================================
# Section 3: Hamiltonian Construction
# ============================================================================

print("\n--- Section 3: Hamiltonian Construction ---")


def build_single_cell_H(E_sp, V_intra):
    """Build single-cell pair Hamiltonian (N_MODES x N_MODES).

    H_cell[k,k] = 2*E_sp[k]  (pair energy = 2 x single-particle)
    H_cell[k,l] = -V_intra[k,l]  for k != l  (pairing interaction)
    """
    n = len(E_sp)
    H = np.diag(2.0 * E_sp)
    for k in range(n):
        for l in range(n):
            if k != l:
                H[k, l] = -V_intra[k, l]
    return H


def build_multicell_H_diagonal_CG(E_sp, V_intra, nodes, ac2, as2, au1,
                                    J_c2, J_s2, J_u):
    """
    Model A: Diagonal Josephson on CG(24) subgraph.
    H[(i,k), (i,l)] = H_cell[k,l]
    H[(i,k), (j,k)] -= J_{type(i,j)}  (same mode k, neighboring cells)

    Bond-type-weighted: each bond contributes its own J.
    """
    N_c = len(nodes)
    n = len(E_sp)
    dim = N_c * n
    H_cell = build_single_cell_H(E_sp, V_intra)
    H = np.zeros((dim, dim))

    # Intra-cell: block diagonal
    for c in range(N_c):
        s = c * n
        H[s:s+n, s:s+n] = H_cell

    # Inter-cell: diagonal Josephson with bond-type weighting
    Aw = weighted_adjacency(ac2, as2, au1, J_c2, J_s2, J_u)
    for c1 in range(N_c):
        for c2 in range(N_c):
            if Aw[c1, c2] > 0:
                for k in range(n):
                    H[c1*n+k, c2*n+k] -= Aw[c1, c2]
    return H


def build_multicell_H_full_CG(E_sp, V_intra, F_inter, nodes, ac2, as2, au1,
                                J_c2, J_s2, J_u):
    """
    Model B: Full Josephson on CG(24) subgraph (mode-mixing).
    H[(i,k), (j,l)] -= J_{type(i,j)} * F_inter[k,l]

    F_inter = V_bare / V_max is the normalized anomalous propagator.
    Bond-type-weighted adjacency.
    """
    N_c = len(nodes)
    n = len(E_sp)
    dim = N_c * n
    H_cell = build_single_cell_H(E_sp, V_intra)
    H = np.zeros((dim, dim))

    # Intra-cell
    for c in range(N_c):
        s = c * n
        H[s:s+n, s:s+n] = H_cell

    # Inter-cell: full mode-mixing with bond-type weighting
    Aw = weighted_adjacency(ac2, as2, au1, J_c2, J_s2, J_u)
    for c1 in range(N_c):
        for c2 in range(N_c):
            if Aw[c1, c2] > 0:
                for k in range(n):
                    for l in range(n):
                        H[c1*n+k, c2*n+l] -= Aw[c1, c2] * F_inter[k, l]
    return H


# Validate N=1
H_cell_fold = build_single_cell_H(E_sp_sweep[fold_idx], V_bare_cont)
evals_cell_fold = np.linalg.eigvalsh(H_cell_fold)
assert np.allclose(evals_cell_fold, evals_N1_stored, atol=1e-10), \
    "Single-cell validation FAILED"
print("N=1 validation: PASS")
print(f"Cell gap: {evals_cell_fold[1] - evals_cell_fold[0]:.6f} M_KK")

# ============================================================================
# Section 4: Gap Scaling on CG(24)
# ============================================================================

print("\n--- Section 4: Gap Scaling on CG(24) ---")

N_cells_list = [2, 4, 8, 16, 32]
# Include N=1 for reference (same as chain)
N_all = [1] + N_cells_list

results_A_CG = {}  # Model A on CG(24)
results_B_CG = {}  # Model B on CG(24)

# N=1: just the single cell (no graph)
evals_fold_N1 = evals_cell_fold
E_sp_init = E_sp_sweep[tau_init_idx]
H_cell_init = build_single_cell_H(E_sp_init, V_bare_cont)
evals_init_N1 = np.linalg.eigvalsh(H_cell_init)
_, evecs_fold_N1 = eigh(H_cell_fold)
_, evecs_init_N1 = eigh(H_cell_init)
overlap_N1 = abs(np.dot(evecs_fold_N1[:, 0], evecs_init_N1[:, 0]))**2

results_A_CG[1] = {
    'dim': N_MODES,
    'E0': evals_fold_N1[0],
    'E1': evals_fold_N1[1],
    'gap': evals_fold_N1[1] - evals_fold_N1[0],
    'gap_init': evals_init_N1[1] - evals_init_N1[0],
    'P_exc': 1.0 - overlap_N1,
    'evals': evals_fold_N1[:8].copy(),
}
results_B_CG[1] = dict(results_A_CG[1])
results_B_CG[1]['PR'] = 1.0
results_B_CG[1]['cell_probs'] = np.array([1.0])

print(f"  N=1 (dim=8): gap={results_A_CG[1]['gap']:.6f} M_KK")

for N_c in N_cells_list:
    dim = N_c * N_MODES
    nodes, ac2, as2, au1 = get_subgraph(N_c)

    E_sp_fold = E_sp_sweep[fold_idx]
    E_sp_init = E_sp_sweep[tau_init_idx]

    t0 = time.time()

    # --- Model A: Diagonal Josephson on CG(24) ---
    H_A_fold = build_multicell_H_diagonal_CG(
        E_sp_fold, V_bare_cont, nodes, ac2, as2, au1,
        J_C2_fold, J_su2_fold, J_u1_fold)
    evals_A_fold, evecs_A_fold = eigh(H_A_fold)

    H_A_init = build_multicell_H_diagonal_CG(
        E_sp_init, V_bare_cont, nodes, ac2, as2, au1,
        J_C2_init, J_su2_init, J_u1_init)
    evals_A_init, evecs_A_init = eigh(H_A_init)

    overlap_A = abs(np.dot(evecs_A_fold[:, 0], evecs_A_init[:, 0]))**2

    results_A_CG[N_c] = {
        'dim': dim,
        'E0': evals_A_fold[0],
        'E1': evals_A_fold[1],
        'gap': evals_A_fold[1] - evals_A_fold[0],
        'gap_init': evals_A_init[1] - evals_A_init[0],
        'P_exc': 1.0 - overlap_A,
        'evals': evals_A_fold[:min(20, dim)].copy(),
    }

    # --- Model B: Full Josephson on CG(24) ---
    H_B_fold = build_multicell_H_full_CG(
        E_sp_fold, V_bare_cont, F_inter, nodes, ac2, as2, au1,
        J_C2_fold, J_su2_fold, J_u1_fold)
    evals_B_fold, evecs_B_fold = eigh(H_B_fold)

    H_B_init = build_multicell_H_full_CG(
        E_sp_init, V_bare_cont, F_inter, nodes, ac2, as2, au1,
        J_C2_init, J_su2_init, J_u1_init)
    evals_B_init, evecs_B_init = eigh(H_B_init)

    overlap_B = abs(np.dot(evecs_B_fold[:, 0], evecs_B_init[:, 0]))**2

    # Ground state participation ratio
    gs_B = evecs_B_fold[:, 0]
    cell_probs = np.array([np.sum(gs_B[c*N_MODES:(c+1)*N_MODES]**2)
                           for c in range(N_c)])
    PR = 1.0 / np.sum(cell_probs**2)

    results_B_CG[N_c] = {
        'dim': dim,
        'E0': evals_B_fold[0],
        'E1': evals_B_fold[1],
        'gap': evals_B_fold[1] - evals_B_fold[0],
        'gap_init': evals_B_init[1] - evals_B_init[0],
        'P_exc': 1.0 - overlap_B,
        'evals': evals_B_fold[:min(20, dim)].copy(),
        'PR': PR,
        'cell_probs': cell_probs,
    }

    dt = time.time() - t0
    print(f"\n  N={N_c:2d} (dim={dim:3d}, {dt:.2f}s):")
    print(f"    Model A (diag J): gap={results_A_CG[N_c]['gap']:.8f}, "
          f"P_exc={results_A_CG[N_c]['P_exc']:.6f}")
    print(f"    Model B (full J): gap={results_B_CG[N_c]['gap']:.8f}, "
          f"P_exc={results_B_CG[N_c]['P_exc']:.6f}, PR={PR:.2f}/{N_c}")

# ============================================================================
# Section 5: Scaling Fits
# ============================================================================

print("\n--- Section 5: Scaling Fits ---")

fit_results = {}

for label, results in [("A_CG (diagonal)", results_A_CG),
                        ("B_CG (full)", results_B_CG)]:
    key = 'A_CG' if 'A_CG' in label else 'B_CG'
    N_arr = np.array(N_all)
    gap_arr = np.array([results[N]['gap'] for N in N_arr])
    P_arr = np.array([results[N]['P_exc'] for N in N_arr])

    # Fit all N >= 2 (exclude N=1 which has no graph)
    mask_2plus = N_arr >= 2
    log_N_2 = np.log(N_arr[mask_2plus])
    log_gap_2 = np.log(gap_arr[mask_2plus])
    coeffs_2 = np.polyfit(log_N_2, log_gap_2, 1)
    alpha_2plus = coeffs_2[0]

    # Fit N >= 4 (robust regime where graph connectivity matters)
    mask_4plus = N_arr >= 4
    if np.sum(mask_4plus) >= 2:
        log_N_4 = np.log(N_arr[mask_4plus])
        log_gap_4 = np.log(gap_arr[mask_4plus])
        coeffs_4 = np.polyfit(log_N_4, log_gap_4, 1)
        alpha_4plus = coeffs_4[0]
    else:
        alpha_4plus = np.nan

    # Fit N >= 8 (large-N regime, matching S57 definition)
    mask_8plus = N_arr >= 8
    if np.sum(mask_8plus) >= 2:
        log_N_8 = np.log(N_arr[mask_8plus])
        log_gap_8 = np.log(gap_arr[mask_8plus])
        coeffs_8 = np.polyfit(log_N_8, log_gap_8, 1)
        alpha_8plus = coeffs_8[0]
        A_fit_8 = np.exp(coeffs_8[1])
    else:
        alpha_8plus = np.nan
        A_fit_8 = np.nan

    # All N fit (including N=1)
    log_N_all = np.log(N_arr)
    log_gap_all = np.log(gap_arr)
    coeffs_all = np.polyfit(log_N_all, log_gap_all, 1)
    alpha_all = coeffs_all[0]

    # R^2 for the N >= 2 fit
    if np.sum(mask_2plus) > 2:
        predicted = np.polyval(coeffs_2, log_N_2)
        ss_res = np.sum((log_gap_2 - predicted)**2)
        ss_tot = np.sum((log_gap_2 - np.mean(log_gap_2))**2)
        R2_2plus = 1.0 - ss_res / ss_tot if ss_tot > 0 else np.nan
    else:
        R2_2plus = np.nan

    # R^2 for the N >= 8 fit
    if np.sum(mask_8plus) > 2:
        predicted_8 = np.polyval(coeffs_8, log_N_8)
        ss_res_8 = np.sum((log_gap_8 - predicted_8)**2)
        ss_tot_8 = np.sum((log_gap_8 - np.mean(log_gap_8))**2)
        R2_8plus = 1.0 - ss_res_8 / ss_tot_8 if ss_tot_8 > 0 else np.nan
    else:
        R2_8plus = np.nan

    # Sigma for N>=2 fit
    if np.sum(mask_2plus) > 2:
        resid = log_gap_2 - np.polyval(coeffs_2, log_N_2)
        sigma_alpha = np.sqrt(np.sum(resid**2) / (np.sum(mask_2plus) - 2) /
                              np.sum((log_N_2 - np.mean(log_N_2))**2))
    else:
        sigma_alpha = np.nan

    fit_results[key] = {
        'alpha_all': alpha_all,
        'alpha_2plus': alpha_2plus,
        'alpha_4plus': alpha_4plus,
        'alpha_8plus': alpha_8plus,
        'A_fit_8': A_fit_8,
        'R2_2plus': R2_2plus,
        'R2_8plus': R2_8plus,
        'sigma_alpha': sigma_alpha,
        'gaps': gap_arr,
        'P_exc': P_arr,
    }

    print(f"\n  Model {label}:")
    print(f"    alpha (all N)  = {alpha_all:.4f}")
    print(f"    alpha (N>=2)   = {alpha_2plus:.4f} +/- {sigma_alpha:.4f}")
    print(f"    alpha (N>=4)   = {alpha_4plus:.4f}")
    print(f"    alpha (N>=8)   = {alpha_8plus:.4f}  <-- large-N regime")
    print(f"    R^2 (N>=2)     = {R2_2plus:.6f}")
    print(f"    R^2 (N>=8)     = {R2_8plus:.6f}")
    print(f"    Gaps: {', '.join(f'{g:.8f}' for g in gap_arr)}")
    print(f"    P_exc: {', '.join(f'{p:.6f}' for p in P_arr)}")

# ============================================================================
# Section 6: Comparison to S57 Chain
# ============================================================================

print("\n--- Section 6: Comparison to S57 Chain ---")

# Load chain gaps from S57
chain_gaps = {}
for N in N_all:
    chain_gaps[N] = float(d57[f'gap_B_N{N}'])

print(f"\n  {'N':>4s}  {'Chain gap':>12s}  {'CG(24) A gap':>14s}  {'CG(24) B gap':>14s}  {'ratio B/chain':>14s}")
for N in N_all:
    gc = chain_gaps[N]
    ga = results_A_CG[N]['gap']
    gb = results_B_CG[N]['gap']
    ratio = gb / gc if gc > 0 else np.nan
    print(f"  {N:4d}  {gc:12.8f}  {ga:14.8f}  {gb:14.8f}  {ratio:14.4f}")

alpha_CG_B = fit_results['B_CG']['alpha_8plus']
print(f"\n  Chain alpha (N>=8):  {alpha_chain:.4f}")
print(f"  CG(24) alpha (N>=8): {alpha_CG_B:.4f}")
print(f"  Difference: {abs(alpha_CG_B - alpha_chain):.4f}")
print(f"  Ratio CG/chain: {alpha_CG_B / alpha_chain:.4f}")

# ============================================================================
# Section 7: Spectral Dimension of CG(24)
# ============================================================================

print("\n--- Section 7: Spectral Dimension ---")

# Spectral dimension from return probability P(t) ~ t^{-d_s/2}
# on the WEIGHTED graph Laplacian.
# L = D - A_weighted, where D = diag(sum of weighted degrees)
# P(t) = (1/N) * Tr(exp(-Lt)) = (1/N) * sum_i exp(-lambda_i * t)

# Full graph (N=32)
A_w_full = weighted_adjacency(adj_C2, adj_su2, adj_u1,
                               J_C2_fold, J_su2_fold, J_u1_fold)
D_full = np.diag(A_w_full.sum(axis=1))
L_full = D_full - A_w_full
evals_L, _ = eigh(L_full)
print(f"Laplacian eigenvalues (first 10): {evals_L[:10]}")
print(f"Spectral gap of Laplacian: {evals_L[1]:.6f}")

# Return probability P(t)
t_range = np.logspace(-2, 2, 500)
P_return = np.zeros_like(t_range)
for i, t in enumerate(t_range):
    P_return[i] = np.mean(np.exp(-evals_L * t))

# Fit d_s from log-log slope: log P = -(d_s/2) * log t + const
# Use intermediate time range where neither short-time (lattice) nor
# long-time (finite-size) effects dominate
# Short-time: P(t) ~ 1 (all eigenvalues contribute)
# Long-time: P(t) ~ (1/N) * exp(-lambda_1 * t) (dominated by smallest nonzero eigenvalue)
# Intermediate: P(t) ~ t^{-d_s/2}

# Find the power-law regime
log_t = np.log(t_range)
log_P = np.log(P_return)

# Local slope d(log P)/d(log t)
dlogP = np.gradient(log_P, log_t)
# d_s = -2 * slope
d_s_local = -2.0 * dlogP

# Find plateau in d_s_local (the spectral dimension)
# Look for the region where d_s_local is most stable
# Use the range t in [0.1, 10] as the intermediate regime
mask_inter = (t_range >= 0.1) & (t_range <= 10.0)
d_s_mean = np.mean(d_s_local[mask_inter])
d_s_std = np.std(d_s_local[mask_inter])
print(f"d_s (t in [0.1, 10]): {d_s_mean:.4f} +/- {d_s_std:.4f}")

# Also fit power law in the intermediate regime
mask_fit = (t_range >= 0.3) & (t_range <= 3.0)
coeffs_ds = np.polyfit(log_t[mask_fit], log_P[mask_fit], 1)
d_s_fit = -2.0 * coeffs_ds[0]
print(f"d_s (power-law fit, t in [0.3, 3]): {d_s_fit:.4f}")

# For subgraphs
print("\nSpectral dimension by subgraph size:")
d_s_values = {}
for N_c in N_cells_list:
    nodes, ac2, as2, au1 = get_subgraph(N_c)
    Aw = weighted_adjacency(ac2, as2, au1, J_C2_fold, J_su2_fold, J_u1_fold)
    Dw = np.diag(Aw.sum(axis=1))
    Lw = Dw - Aw
    ev_L = np.linalg.eigvalsh(Lw)

    # Return probability
    P_ret = np.zeros_like(t_range)
    for i, t in enumerate(t_range):
        P_ret[i] = np.mean(np.exp(-ev_L * t))

    log_P_sub = np.log(P_ret)
    dlogP_sub = np.gradient(log_P_sub, log_t)
    d_s_sub_local = -2.0 * dlogP_sub

    # Fit in available range (shorter for small graphs)
    t_max_fit = min(3.0, 1.0 / ev_L[1]) if ev_L[1] > 0 else 3.0
    mask_sub = (t_range >= 0.1) & (t_range <= t_max_fit)
    if np.sum(mask_sub) > 5:
        d_s_sub = np.mean(d_s_sub_local[mask_sub])
    else:
        d_s_sub = np.nan

    d_s_values[N_c] = d_s_sub
    print(f"  N={N_c:2d}: d_s = {d_s_sub:.4f}, spectral_gap = {ev_L[1]:.6f}")

d_s_values[32] = d_s_fit  # Use the fitted value for full graph

# Dynamical exponent z from alpha = -z/d_s
# alpha_CG = -z / d_s => z = -alpha_CG * d_s
alpha_CG_physical = fit_results['B_CG']['alpha_8plus']
d_s_physical = d_s_fit
z_CG = -alpha_CG_physical * d_s_physical
print(f"\nDynamical exponent z = -alpha * d_s = {z_CG:.4f}")
print(f"  (alpha = {alpha_CG_physical:.4f}, d_s = {d_s_physical:.4f})")

# S57 chain: d_s=1 (by definition), z = -alpha_chain * 1 = 1.84
z_chain = -alpha_chain
print(f"  Chain: z = {z_chain:.4f} (d_s = 1)")

# ============================================================================
# Section 8: Uniform-J Control (CG(24) with J_C2 only)
# ============================================================================

print("\n--- Section 8: Uniform-J Control ---")

# Run the CG(24) computation with uniform J = J_C2 for ALL bond types
# This isolates the effect of graph topology from bond-type weighting
results_B_uniform = {}

for N_c in N_all:
    if N_c == 1:
        results_B_uniform[1] = results_B_CG[1].copy()
        continue

    nodes, ac2, as2, au1 = get_subgraph(N_c)
    # Uniform: treat all bonds as having J_C2
    adj_uniform = (ac2 + as2 + au1)
    adj_uniform[adj_uniform > 0] = 1.0  # unweighted

    H_B = build_multicell_H_full_CG(
        E_sp_sweep[fold_idx], V_bare_cont, F_inter,
        nodes,
        adj_uniform, np.zeros_like(adj_uniform), np.zeros_like(adj_uniform),
        J_C2_fold, 0.0, 0.0)
    evals_B, evecs_B = eigh(H_B)

    gs_B = evecs_B[:, 0]
    cell_probs = np.array([np.sum(gs_B[c*N_MODES:(c+1)*N_MODES]**2)
                           for c in range(N_c)])
    PR = 1.0 / np.sum(cell_probs**2)

    results_B_uniform[N_c] = {
        'gap': evals_B[1] - evals_B[0],
        'E0': evals_B[0],
        'PR': PR,
    }

    print(f"  N={N_c:2d}: gap(uniform J_C2) = {results_B_uniform[N_c]['gap']:.8f}, "
          f"gap(weighted) = {results_B_CG[N_c]['gap']:.8f}")

# Fit uniform-J gaps
N_arr_fit = np.array([N for N in N_all if N >= 8])
gap_uniform = np.array([results_B_uniform[N]['gap'] for N in N_arr_fit])
if len(N_arr_fit) >= 2:
    coeffs_uni = np.polyfit(np.log(N_arr_fit), np.log(gap_uniform), 1)
    alpha_uniform_8 = coeffs_uni[0]
    print(f"\n  Uniform J_C2 alpha (N>=8): {alpha_uniform_8:.4f}")
    print(f"  Weighted alpha (N>=8):     {alpha_CG_physical:.4f}")
    print(f"  Chain alpha (N>=8):        {alpha_chain:.4f}")

# ============================================================================
# Section 9: Gate Verdict
# ============================================================================

print("\n" + "=" * 78)
print("--- Section 9: Gate Verdict: GAP-CG-58 ---")
print("=" * 78)

# Physical result: Model B with weighted bonds on CG(24), N>=8 regime
alpha_gate = fit_results['B_CG']['alpha_8plus']
R2_gate = fit_results['B_CG']['R2_8plus']

print(f"\n  RESULT: alpha_CG = {alpha_gate:.4f}")
print(f"  R^2 (N>=8) = {R2_gate:.6f}")
print(f"  Chain reference: alpha_chain = {alpha_chain:.4f}")
print(f"  Difference: |alpha_CG - alpha_chain| = {abs(alpha_gate - alpha_chain):.4f}")
print(f"  Fractional difference: {abs(alpha_gate - alpha_chain)/abs(alpha_chain)*100:.1f}%")

# Gate criteria:
# PASS: alpha in [-2.21, -1.47] (within 20% of -1.84)
# FAIL: alpha > 0
# INFO: alpha in [-2.5, -1.47] or [-1.47, 0]

if alpha_gate > 0:
    gate_verdict = "FAIL"
    gate_detail = (f"alpha_CG = {alpha_gate:.4f} > 0. "
                   f"Gap grows with N on CG(24). DM prediction collapses.")
elif -2.21 <= alpha_gate <= -1.47:
    gate_verdict = "PASS"
    gate_detail = (f"alpha_CG = {alpha_gate:.4f} within 20% of chain "
                   f"alpha = {alpha_chain:.4f}. "
                   f"Gap scaling transfers from chain to physical CG(24) graph. "
                   f"R^2 = {R2_gate:.4f}. "
                   f"d_s = {d_s_physical:.3f}, z = {z_CG:.3f}.")
elif alpha_gate < -2.5:
    gate_verdict = "INFO"
    gate_detail = (f"alpha_CG = {alpha_gate:.4f} < -2.5. "
                   f"Gap closes faster on CG(24) than on chain. "
                   f"Steeper than expected but gap still decreasing.")
elif -2.5 <= alpha_gate < -2.21:
    gate_verdict = "INFO"
    gate_detail = (f"alpha_CG = {alpha_gate:.4f} in [-2.5, -2.21]. "
                   f"Steeper than chain by more than 20% but negative. "
                   f"Higher connectivity accelerates gap closure.")
elif -1.47 < alpha_gate <= 0:
    gate_verdict = "INFO"
    gate_detail = (f"alpha_CG = {alpha_gate:.4f} in [-1.47, 0]. "
                   f"Gap closes but shallower than chain by >20%. "
                   f"DM mass prediction may need revision.")
else:
    gate_verdict = "INFO"
    gate_detail = f"alpha_CG = {alpha_gate:.4f}. Unexpected range."

print(f"\n  GATE: GAP-CG-58 = {gate_verdict}")
print(f"  {gate_detail}")

# ============================================================================
# Section 10: Save Data
# ============================================================================

print("\n--- Section 10: Saving Data ---")

save_dict = {
    'N_cells_list': np.array(N_all),
    'tau_fold': tau_values[fold_idx],
    'tau_init': tau_values[tau_init_idx],
    'fold_idx': fold_idx,
    'J_C2_fold': J_C2_fold,
    'J_su2_fold': J_su2_fold,
    'J_u1_fold': J_u1_fold,
    'V_max': V_max,
    'F_inter': F_inter,
    'bfs_order': bfs_order,
}

# Save per-N results
for N in N_all:
    for key in ['E0', 'E1', 'gap', 'gap_init', 'P_exc']:
        save_dict[f'{key}_A_CG_N{N}'] = results_A_CG[N][key]
        save_dict[f'{key}_B_CG_N{N}'] = results_B_CG[N][key]
    save_dict[f'evals_A_CG_N{N}'] = results_A_CG[N]['evals']
    save_dict[f'evals_B_CG_N{N}'] = results_B_CG[N]['evals']
    if 'PR' in results_B_CG[N]:
        save_dict[f'PR_B_CG_N{N}'] = results_B_CG[N]['PR']
    if N in results_B_uniform:
        save_dict[f'gap_B_uniform_N{N}'] = results_B_uniform[N]['gap']

# Fit results
for model_key in ['A_CG', 'B_CG']:
    fr = fit_results[model_key]
    for fit_key in ['alpha_all', 'alpha_2plus', 'alpha_4plus', 'alpha_8plus',
                     'R2_2plus', 'R2_8plus', 'sigma_alpha']:
        save_dict[f'{fit_key}_{model_key}'] = fr[fit_key]

# Spectral dimension
save_dict['d_s_fit'] = d_s_fit
save_dict['d_s_mean'] = d_s_mean
save_dict['d_s_std'] = d_s_std
save_dict['z_CG'] = z_CG
save_dict['z_chain'] = z_chain
save_dict['alpha_chain_S57'] = alpha_chain
if 'alpha_uniform_8' in dir():
    save_dict['alpha_uniform_8'] = alpha_uniform_8

# Gate
save_dict['gate_name'] = np.array(['GAP-CG-58'])
save_dict['gate_verdict'] = np.array([gate_verdict])
save_dict['gate_detail'] = np.array([gate_detail])

out_path = data_dir / 's58_gap_cg.npz'
np.savez(out_path, **save_dict)
print(f"Saved: {out_path}")

# ============================================================================
# Section 11: Plot
# ============================================================================

print("\n--- Section 11: Plotting ---")

fig, axes = plt.subplots(2, 2, figsize=(14, 11))

# --- Panel (a): Gap vs N, log-log ---
ax = axes[0, 0]
N_arr = np.array(N_all)

# CG(24) Model B
gap_B_CG = np.array([results_B_CG[N]['gap'] for N in N_arr])
ax.loglog(N_arr, gap_B_CG, 'o-', color='C0', lw=2, ms=8,
          label=f'CG(24) Model B: α={fit_results["B_CG"]["alpha_8plus"]:.2f}')

# CG(24) Model A
gap_A_CG = np.array([results_A_CG[N]['gap'] for N in N_arr])
ax.loglog(N_arr, gap_A_CG, 's--', color='C1', lw=1.5, ms=6,
          label=f'CG(24) Model A: α={fit_results["A_CG"]["alpha_8plus"]:.2f}')

# Chain Model B (from S57)
gap_chain = np.array([chain_gaps[N] for N in N_arr])
ax.loglog(N_arr, gap_chain, 'D:', color='C2', lw=1.5, ms=6,
          label=f'Chain Model B (S57): α={alpha_chain:.2f}')

# Uniform-J control
gap_uni = np.array([results_B_uniform[N]['gap'] for N in N_arr])
ax.loglog(N_arr, gap_uni, '^--', color='C3', lw=1, ms=5, alpha=0.7,
          label='CG(24) uniform J_C2')

# Power-law fit lines
N_fit = np.linspace(4, 40, 100)
if not np.isnan(fit_results['B_CG']['alpha_8plus']):
    # Fit from N>=8 data
    alpha_B = fit_results['B_CG']['alpha_8plus']
    # Use N=8 as anchor
    gap_8 = results_B_CG[8]['gap']
    ax.loglog(N_fit, gap_8 * (N_fit / 8)**alpha_B,
              '-', color='C0', alpha=0.3, lw=3)

ax.set_xlabel('N (cells)', fontsize=12)
ax.set_ylabel('Δ_N (M_KK)', fontsize=12)
ax.set_title('(a) Many-Body Gap vs Cell Count', fontsize=12)
ax.legend(fontsize=9, loc='lower left')
ax.grid(True, alpha=0.3, which='both')
ax.set_xlim(0.8, 50)

# --- Panel (b): Spectral dimension ---
ax = axes[0, 1]
ax.semilogx(t_range, d_s_local, 'k-', lw=0.8, alpha=0.5)
ax.axhline(d_s_fit, color='C0', lw=2, ls='--',
           label=f'd_s = {d_s_fit:.2f} (fit)')
ax.axhline(1.0, color='C2', lw=1, ls=':', label='d_s = 1 (chain)')
ax.fill_between(t_range, d_s_fit - d_s_std, d_s_fit + d_s_std,
                alpha=0.15, color='C0')  # (local)
ax.axvspan(0.3, 3.0, alpha=0.08, color='green', label='fit window')
ax.set_xlabel('t', fontsize=12)
ax.set_ylabel('d_s(t) = -2 d(log P)/d(log t)', fontsize=12)
ax.set_title('(b) Spectral Dimension of CG(24)', fontsize=12)
ax.legend(fontsize=9)
ax.set_ylim(-1, 8)
ax.grid(True, alpha=0.3)

# --- Panel (c): Return probability ---
ax = axes[1, 0]
ax.loglog(t_range, P_return, 'k-', lw=1.5, label='P(t) on CG(24)')
# Fit line
t_fit = t_range[(t_range >= 0.3) & (t_range <= 3.0)]
P_fit_line = np.exp(coeffs_ds[1]) * t_fit**coeffs_ds[0]
ax.loglog(t_fit, P_fit_line, 'r--', lw=2,
          label=f'P ~ t^{{{coeffs_ds[0]:.2f}}} (d_s/2 = {-coeffs_ds[0]:.2f})')
ax.set_xlabel('t', fontsize=12)
ax.set_ylabel('P(t) = Tr(e^{-Lt})/N', fontsize=12)
ax.set_title('(c) Return Probability', fontsize=12)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3, which='both')

# --- Panel (d): Ground state participation ratio ---
ax = axes[1, 1]
PR_arr = [results_B_CG[N].get('PR', 1.0) for N in N_arr]
ax.plot(N_arr, PR_arr, 'o-', color='C0', lw=2, ms=8, label='PR (CG24 Model B)')
ax.plot(N_arr, N_arr, 'k--', lw=1, alpha=0.5, label='PR = N (fully delocalized)')
ax.set_xlabel('N (cells)', fontsize=12)
ax.set_ylabel('Participation Ratio', fontsize=12)
ax.set_title('(d) Ground State Delocalization', fontsize=12)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

fig.suptitle(f'GAP-CG-58: Gap Scaling on Physical CG(24) — '
             f'α = {alpha_gate:.3f} ({gate_verdict})',
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(data_dir / 's58_gap_cg.png', dpi=150, bbox_inches='tight')
print(f"Saved: {data_dir / 's58_gap_cg.png'}")

t_total = time.time() - t_start
print(f"\nTotal runtime: {t_total:.1f}s")
print(f"\n{'='*78}")
print(f"GAP-CG-58: {gate_verdict}")
print(f"{'='*78}")
