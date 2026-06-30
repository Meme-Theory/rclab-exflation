#!/usr/bin/env python3
"""
PCK-LARGE-N-PAIR-75: Richardson-Gaudin Integrability at Multiple Fillings
=========================================================================

Gate: S75-J2-PCK-LARGE-N
  PASS: <r> < 0.45 at filling = 0.15
  INFO: <r> < 0.45 at 0.10 but not 0.15
  FAIL: <r> > 0.45 at all fillings

Physics:
  The Richardson-Gaudin (RG) model with separable pairing V_{jj'} = G*f_j*f_{j'}
  is exactly integrable (Richardson 1963, Gaudin 1976; Paper 15). Its level
  statistics follow Poisson: <r>_Poisson = 2*ln(2) - 1 = 0.386.

  The FULL pairing interaction V_{kl} from D_K on Jensen-deformed SU(3) has
  rank > 1. The non-separable component V_perp breaks integrability, driving
  level statistics toward GOE: <r>_GOE = 0.5307.

  We test integrability at filling fractions nu = {0.10, 0.15, 0.20} on the
  fabric (CG(24) x 8 modes = 192 levels). Since full ED at these fillings is
  intractable (dim = C(192, N) >> 10^30), we use TWO complementary methods:

  METHOD 1: Reduced single-cell ED with effective filling.
    Map fabric filling to single-cell filling: for 8 modes, nu=0.10 -> N=1,
    nu=0.15 -> N=1 (lower), nu=0.20 -> N=2. Use CG(24) band structure to
    generate an ENSEMBLE of effective single-cell spectra by sampling Bloch
    eigenvalues, then compute <r> as an ensemble average.

  METHOD 2: R-G equations on larger subsystems (2-cell, 4-cell).
    For 2 cells x 8 modes = 16 levels, N_pair up to 3 is tractable by ED.
    For 4 cells x 8 modes = 32 levels, N_pair up to 5 is tractable.
    Build the tight-binding Hamiltonian on small CG(24) subgraphs, solve
    both the separable (RG) and full Hamiltonians, compute <r>.

  METHOD 3: Richardson equation purity.
    For the rank-1 separable model on the full 192-level fabric, solve the
    M-pair Richardson equations. The reduced density matrix of a single level
    has purity Tr(rho^2) computable from the R-G pair amplitudes. Average
    purity <P> below a threshold indicates entanglement beyond mean-field,
    which correlates with integrability breaking under the full V.

References:
  - Richardson (1963): Exact eigenstates of pairing Hamiltonian
  - Gaudin (1976): Bethe ansatz for reduced BCS
  - Paper 15 (Dukelsky, Pittel, Sierra 2004): R-G colloquium
  - Paper 17 (von Delft & Ralph 2001): Ultrasmall BCS grains
  - Paper 03 (Dobaczewski et al.): HFB pairing Hamiltonian

Session: S75 W3-J
Agent: nazarewicz-nuclear-structure-theorist
"""

import sys
import os
import numpy as np
from itertools import combinations
from math import comb as mcomb
from scipy.linalg import eigh
from scipy.optimize import brentq, fsolve
from scipy.stats import kstest
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (, r_GOE_canonical
    tau_fold, E_cond, N_dof_BCS, Delta_0_OES, Delta_BCS,
    E_B1, E_B2_mean, E_B3_mean, N_cells as N_CELLS_CANONICAL,
    J_C2, xi_BCS,
)

data_dir = os.path.dirname(os.path.abspath(__file__))

np.random.seed(42)

# =====================================================================
#  1. LOAD INPUT DATA
# =====================================================================

print("=" * 72)
print("PCK-LARGE-N-PAIR-75: R-G Integrability at Multiple Fillings")
print("=" * 72)

# Single-cell BCS data from S52 HFB
hfb_data = np.load(os.path.join(data_dir, 's52_hfb_full.npz'), allow_pickle=True)
eps_bare = hfb_data['E_sp_bare']       # 8 single-particle energies (M_KK)
V_bare = hfb_data['V_bare']            # 8x8 pairing interaction (M_KK)
labels = hfb_data['labels']            # mode labels
N_modes = len(eps_bare)

# CG(24) adjacency
cg24_data = np.load(os.path.join(data_dir, 's60_entangle_cg24.npz'), allow_pickle=True)
adj_cg24 = cg24_data['adj'].astype(float)
N_cells_CG24 = int(cg24_data['N_vertices'])  # = 24
degree_CG24 = int(cg24_data['degree'])        # = 6

# Rank-1 separable decomposition from S60
rg_data = np.load(os.path.join(data_dir, 's60_rg_integrals.npz'), allow_pickle=True)
g_eff = float(rg_data['g_eff'])               # 0.2758 M_KK
u_vec = rg_data['u_vec']                       # 8 mode amplitudes
rank1_frac = float(rg_data['svd_rank1_fraction'])  # 64.3%

# Fabric data from S56
fab_data = np.load(os.path.join(data_dir, 's56_gge_fabric.npz'), allow_pickle=True)
eps_fold = fab_data['eps_fold']                # 8 single-cell energies at fold
V_fold = fab_data['V_fold']                    # 8x8 pairing at fold
E_J_fold = float(fab_data['E_J_fold'])         # Josephson coupling

print(f"N_modes = {N_modes}, N_cells = {N_cells_CG24}, degree = {degree_CG24}")
print(f"eps_bare = {eps_bare}")
print(f"g_eff = {g_eff:.6f} M_KK (rank-1 SVD, {rank1_frac*100:.1f}% of V)")
print(f"E_J_fold = {E_J_fold:.6f} M_KK")
print(f"Delta_BCS = {Delta_BCS:.6f} M_KK")
print()

# =====================================================================
#  2. SVD DECOMPOSITION OF PAIRING INTERACTION
# =====================================================================

print("=" * 72)
print("V_BARE STRUCTURE")
print("=" * 72)

U_svd, S_svd, Vt_svd = np.linalg.svd(V_bare)
frac_rank1 = S_svd[0]**2 / np.sum(S_svd**2)  # (local)
frac_rank2 = np.sum(S_svd[:2]**2) / np.sum(S_svd**2)  # (local)

V_sep = S_svd[0] * np.outer(U_svd[:, 0], Vt_svd[0, :])  # (local)
V_perp = V_bare - V_sep  # (local)

print(f"Rank-1 fraction: {frac_rank1:.4f}")
print(f"Rank-2 fraction: {frac_rank2:.4f}")
print(f"||V_perp||/||V|| = {np.linalg.norm(V_perp, 'fro')/np.linalg.norm(V_bare, 'fro'):.6f}")
print()

# =====================================================================
#  3. CORE FUNCTIONS: Fock space, Hamiltonians, r-statistic
# =====================================================================

def build_pair_fock_states(n_levels, n_pair):
    """Build pair Fock states: all C(n_levels, n_pair) configurations."""
    return list(combinations(range(n_levels), n_pair))

def build_hamiltonian_RG(eps, g, states, n_levels):
    """Richardson-Gaudin Hamiltonian: H_RG = sum_k 2*eps_k n_k - g sum_{k,l} P_k^+ P_l"""
    dim = len(states)  # (local)
    H = np.zeros((dim, dim))  # (local)
    for i, si in enumerate(states):
        H[i, i] = 2.0 * sum(eps[k] for k in si) - g * len(si)
        for j in range(i + 1, dim):
            sj = states[j]
            si_set, sj_set = set(si), set(sj)
            diff_i = si_set - sj_set  # (local)
            diff_j = sj_set - si_set  # (local)
            if len(diff_i) == 1 and len(diff_j) == 1:
                H[i, j] = -g
                H[j, i] = -g
    return H

def build_hamiltonian_full(eps, V, states, n_levels):
    """Full pairing Hamiltonian with non-separable V_{kl}."""
    dim = len(states)  # (local)
    H = np.zeros((dim, dim))  # (local)
    for i, si in enumerate(states):
        H[i, i] = 2.0 * sum(eps[k] for k in si) - sum(V[k, k] for k in si)
        for j in range(i + 1, dim):
            sj = states[j]
            si_set, sj_set = set(si), set(sj)
            diff_i = si_set - sj_set
            diff_j = sj_set - si_set
            if len(diff_i) == 1 and len(diff_j) == 1:
                k = diff_i.pop()
                l = diff_j.pop()
                H[i, j] = -V[k, l]
                H[j, i] = -V[l, k]
    return H

def compute_r_statistic(eigenvalues, remove_degeneracies=True):
    """
    Mean ratio of consecutive spacings (Oganesyan-Huse).
    r_n = min(s_n, s_{n+1}) / max(s_n, s_{n+1})
    Poisson: <r> = 2*ln(2) - 1 = 0.386
    GOE:     <r> = 0.5307
    """
    E = np.sort(eigenvalues)
    spacings = np.diff(E)
    if remove_degeneracies and len(spacings) > 0:
        mean_s = np.mean(spacings)  # (local)
        if mean_s > 0:
            mask = spacings > 1e-12 * mean_s  # (local)
            spacings = spacings[mask]
    if len(spacings) < 2:
        return np.nan, np.array([]), spacings
    r_values = []  # (local)
    for n in range(len(spacings) - 1):
        s_n = spacings[n]  # (local)
        s_np1 = spacings[n + 1]  # (local)
        if max(s_n, s_np1) > 0:
            r_values.append(min(s_n, s_np1) / max(s_n, s_np1))
    r_values = np.array(r_values)
    return np.mean(r_values) if len(r_values) > 0 else np.nan, r_values, spacings

def bootstrap_r(r_values, n_boot=1000):
    """Bootstrap uncertainty on <r>."""
    if len(r_values) < 2:
        return np.nan
    means = [np.mean(r_values[np.random.choice(len(r_values), size=len(r_values), replace=True)])
             for _ in range(n_boot)]
    return np.std(means)

def solve_bcs_gap(eps, V_diag, N_target, Delta_init=0.3):
    """Solve BCS gap + number equations for uniform g."""
    Delta_target = Delta_BCS  # (local)
    def bcs_eqs(params):
        mu, g = params
        E_k = np.sqrt((eps - mu)**2 + Delta_target**2)  # (local)
        v2 = 0.5 * (1 - (eps - mu) / E_k)  # (local)
        number_eq = np.sum(v2) - N_target  # (local)
        gap_eq = 1.0 / g - 0.5 * np.sum(1.0 / E_k)  # (local)
        return [number_eq, gap_eq]
    mu0 = np.mean(eps)  # (local)
    g0 = 0.15  # (local)
    sol = fsolve(bcs_eqs, [mu0, g0], full_output=True)
    return sol[0][1], sol[0][0]  # g, mu

# =====================================================================
#  4. REFERENCE VALUES
# =====================================================================

r_Poisson = 2 * np.log(2) - 1  # 0.3863  (local)
r_GOE = r_GOE_canonical  # canonical alias (was: = 0.5307)
r_GUE = 0.6027  # (local)

fillings = [0.10, 0.15, 0.20]  # (local)
N_levels_fabric = N_cells_CG24 * N_modes  # = 192  (local)

print(f"Reference: <r>_Poisson = {r_Poisson:.4f}, <r>_GOE = {r_GOE:.4f}")
print(f"Fabric: {N_levels_fabric} levels ({N_cells_CG24} cells x {N_modes} modes)")
print(f"Fillings: {fillings}")
for nu in fillings:
    N_pair = int(round(nu * N_levels_fabric))  # (local)
    print(f"  nu = {nu:.2f}: N_pair = {N_pair}, dim(ED) = C({N_levels_fabric},{N_pair})")
print()

# =====================================================================
#  5. METHOD 1: Multi-cell ED at variable filling
# =====================================================================
#
# Strategy: use N_cell-site clusters (2, 4, 8 cells) with the tight-binding
# Hamiltonian H_k = eps_k I + E_J * adj for each mode k. For n_cell cells,
# n_levels = n_cell * 8. We vary N_pair to hit the target filling fractions.
#
# This is the nuclear structure approach: finite-size scaling of the
# integrability breaking parameter <r> vs filling at fixed interaction.

print("=" * 72)
print("METHOD 1: Multi-cell ED at variable filling")
print("=" * 72)

def build_multi_cell_spectrum(n_cells_sub, eps_intra, E_J, adj_full):
    """
    Build single-particle spectrum for an n_cells_sub-site subcluster.
    Uses the first n_cells_sub eigenvalues of the CG(24) adjacency
    (representative of the Bloch band structure).

    Returns: eps_fabric (n_cells_sub * N_modes), mode_labels (int array)
    """
    # Diagonalize full CG(24) adjacency for the band structure
    evals_adj = np.sort(eigh(adj_full, eigvals_only=True))
    # Sample n_cells_sub eigenvalues uniformly from the CG(24) spectrum
    # to represent a typical subcluster
    indices = np.linspace(0, len(evals_adj) - 1, n_cells_sub, dtype=int)  # (local)
    lambda_n = evals_adj[indices]  # (local)

    n_levels = n_cells_sub * N_modes  # (local)
    eps_fab = np.zeros(n_levels)  # (local)
    mode_lab = np.zeros(n_levels, dtype=int)  # (local)

    for k in range(N_modes):
        for n in range(n_cells_sub):
            idx = k * n_cells_sub + n  # (local)
            eps_fab[idx] = eps_intra[k] + E_J * lambda_n[n]
            mode_lab[idx] = k
    return eps_fab, mode_lab

def build_multi_cell_V(n_cells_sub, V_intra, N_modes_per_cell):
    """
    Build pairing interaction matrix for a multi-cell cluster.
    Pairing is LOCAL (same cell): V_{(k,n),(k',n)} = V_intra[k,k'].
    Cross-cell pairing vanishes: V_{(k,n),(k',m)} = 0 for n != m.
    In the Bloch basis, same-cell pairing spreads over all Bloch states:
      V_{(k,n),(k',n')} = (1/N_cells) * V_intra[k,k'] for all n,n'
    (uniform pairing in Bloch basis).
    """
    n_levels = n_cells_sub * N_modes_per_cell  # (local)
    V_fab = np.zeros((n_levels, n_levels))  # (local)
    for k in range(N_modes_per_cell):
        for kp in range(N_modes_per_cell):
            for n in range(n_cells_sub):
                for np_ in range(n_cells_sub):
                    idx_kn = k * n_cells_sub + n  # (local)
                    idx_kpnp = kp * n_cells_sub + np_  # (local)
                    # Bloch basis: pairing amplitude = V_kk' / N_cells
                    V_fab[idx_kn, idx_kpnp] = V_intra[k, kp] / n_cells_sub
    return V_fab

# Run ED for subclusters of size 2, 4, 8 cells
cluster_sizes = [2, 4, 8]  # (local)
results_method1 = {}  # (local)

for n_cells_sub in cluster_sizes:
    n_levels = n_cells_sub * N_modes  # (local)
    eps_sub, mode_sub = build_multi_cell_spectrum(n_cells_sub, eps_bare, E_J_fold, adj_cg24)

    # Build full V in Bloch basis
    V_sub = build_multi_cell_V(n_cells_sub, V_bare, N_modes)  # (local)

    # SVD for separable decomposition of V_sub
    U_s, S_s, Vt_s = np.linalg.svd(V_sub)
    g_sub = S_s[0]  # (local) rank-1 strength on this cluster

    print(f"\n--- {n_cells_sub}-cell cluster: {n_levels} levels ---")
    print(f"  eps range: [{eps_sub.min():.4f}, {eps_sub.max():.4f}] M_KK")
    print(f"  V_sub rank-1 fraction: {S_s[0]**2/np.sum(S_s**2):.4f}")

    for nu in fillings:
        N_pair = max(1, int(round(nu * n_levels)))  # (local)
        dim = mcomb(n_levels, N_pair)  # (local)

        # Skip if dimension is too large for ED
        MAX_DIM = 50000  # (local) practical ED limit
        if dim > MAX_DIM:
            print(f"  nu={nu:.2f}: N_pair={N_pair}, dim={dim} > {MAX_DIM} -- SKIPPED")
            results_method1[(n_cells_sub, nu)] = {
                'N_pair': N_pair, 'dim': dim, 'r_RG': np.nan, 'r_full': np.nan,
                'r_err_RG': np.nan, 'r_err_full': np.nan, 'skipped': True
            }
            continue

        print(f"  nu={nu:.2f}: N_pair={N_pair}, dim={dim}")

        states = build_pair_fock_states(n_levels, N_pair)

        # Solve BCS gap equation for this cluster's g
        try:
            g_bcs, mu_bcs = solve_bcs_gap(np.sort(eps_sub), None, N_pair)
        except Exception:
            g_bcs = g_eff  # (local) fallback
            mu_bcs = np.mean(eps_sub)  # (local)

        eps_sorted_sub = np.sort(eps_sub)  # (local)

        # Build Hamiltonians
        H_RG = build_hamiltonian_RG(eps_sorted_sub, abs(g_bcs), states, n_levels)
        H_full = build_hamiltonian_full(eps_sorted_sub, V_sub, states, n_levels)

        # Diagonalize
        evals_RG = np.sort(eigh(H_RG, eigvals_only=True))  # (local)
        evals_full = np.sort(eigh(H_full, eigvals_only=True))  # (local)

        # Compute <r>
        r_RG, rv_RG, sp_RG = compute_r_statistic(evals_RG)
        r_full, rv_full, sp_full = compute_r_statistic(evals_full)
        err_RG = bootstrap_r(rv_RG)  # (local)
        err_full = bootstrap_r(rv_full)  # (local)

        print(f"    <r>_RG   = {r_RG:.4f} +/- {err_RG:.4f} (N_spacings={len(sp_RG)})")
        print(f"    <r>_full = {r_full:.4f} +/- {err_full:.4f} (N_spacings={len(sp_full)})")
        print(f"    E_gs_RG = {evals_RG[0]:.6f}, E_gs_full = {evals_full[0]:.6f}")

        results_method1[(n_cells_sub, nu)] = {
            'N_pair': N_pair, 'dim': dim,
            'g_bcs': g_bcs, 'mu_bcs': mu_bcs,
            'r_RG': r_RG, 'r_err_RG': err_RG,
            'r_full': r_full, 'r_err_full': err_full,
            'E_gs_RG': evals_RG[0], 'E_gs_full': evals_full[0],
            'n_spacings_RG': len(sp_RG), 'n_spacings_full': len(sp_full),
            'skipped': False
        }

# =====================================================================
#  6. METHOD 2: Richardson equation on 192-level fabric (rank-1 model)
# =====================================================================
#
# For the separable model V_{jj'} = G * f_j * f_{j'}, the M-pair Richardson
# equations read (Paper 15, Eq. 9):
#
#   1 + G * sum_j f_j^2 / (2*eps_j - E_alpha)
#     - 2*G * sum_{beta != alpha} 1/(E_beta - E_alpha) = 0    (alpha = 1..M)
#
# For M=1, the second term vanishes (no pair-pair interaction).
# For M > 1, the equations are coupled.
#
# We solve iteratively starting from the non-interacting limit (G=0).
# The purity of the reduced density matrix for level j is:
#   P_j = n_j^2 + (1 - n_j)^2
# where n_j = <n_j> is the occupation of level j in the RG ground state.
# Average purity: <P> = (1/L) sum_j P_j
# For a product state (BCS), <P> close to 1.
# For a strongly correlated state, <P> -> 0.5 (maximally mixed 1-level RDM).

print("\n" + "=" * 72)
print("METHOD 2: Richardson Equations on Full 192-Level Fabric")
print("=" * 72)

# Build full fabric spectrum
evals_adj_full = np.sort(eigh(adj_cg24, eigvals_only=True))  # (local)
eps_fabric_full = np.zeros(N_levels_fabric)  # (local)
u_fabric_full = np.zeros(N_levels_fabric)  # (local)
mode_fabric = np.zeros(N_levels_fabric, dtype=int)  # (local)

for k in range(N_modes):
    for n in range(N_cells_CG24):
        idx = k * N_cells_CG24 + n  # (local)
        eps_fabric_full[idx] = eps_bare[k] + E_J_fold * evals_adj_full[n]
        u_fabric_full[idx] = u_vec[k]
        mode_fabric[idx] = k

# Sort by energy
sort_idx_fab = np.argsort(eps_fabric_full)  # (local)
eps_fab_sorted = eps_fabric_full[sort_idx_fab]  # (local)
u_fab_sorted = u_fabric_full[sort_idx_fab]  # (local)
f_sq_fab = u_fab_sorted**2  # (local)

print(f"Fabric spectrum: {N_levels_fabric} levels")
print(f"  E_min = {eps_fab_sorted[0]:.6f}, E_max = {eps_fab_sorted[-1]:.6f}")
print(f"  Mean level spacing = {(eps_fab_sorted[-1] - eps_fab_sorted[0])/(N_levels_fabric-1):.6f}")
print(f"  Bandwidth = {eps_fab_sorted[-1] - eps_fab_sorted[0]:.4f} M_KK")

def solve_richardson_M1(eps, f_sq, G):
    """
    Solve Richardson equation for M=1 pair:
      R(E) = 1 + G * sum_j f_j^2 / (2*eps_j - E) = 0
    Returns the lowest root (ground state pair energy).
    """
    L = len(eps)  # (local)
    poles = 2.0 * eps  # (local)
    margin = 1e-12  # (local)

    def R_func(E):
        return 1.0 + G * np.sum(f_sq / (2.0 * eps - E))

    # Search below all poles (bound state)
    E_low = poles[0] - 100.0  # (local)
    roots = []  # (local)
    try:
        if R_func(E_low) * R_func(poles[0] - margin) < 0:
            root = brentq(R_func, E_low, poles[0] - margin, xtol=1e-14)
            roots.append(root)
    except Exception:
        pass

    # Between consecutive poles
    for j in range(L - 1):
        try:
            if R_func(poles[j] + margin) * R_func(poles[j + 1] - margin) < 0:
                root = brentq(R_func, poles[j] + margin, poles[j + 1] - margin, xtol=1e-14)
                roots.append(root)
        except Exception:
            pass

    return np.array(sorted(roots))

def compute_rg_occupations_M1(eps, f_sq, u_sorted, E_alpha):
    """
    Compute level occupations from M=1 Richardson wavefunction.
    psi_j = u_j / (2*eps_j - E_alpha), normalized.
    n_j = |psi_j|^2 = probability of pair in level j.
    """
    psi_raw = u_sorted / (2.0 * eps - E_alpha)  # (local)
    psi_norm = psi_raw / np.sqrt(np.sum(psi_raw**2))  # (local)
    return psi_norm**2

def compute_rdm_purity(n_j):
    """
    Compute average purity of single-level reduced density matrix.
    For a system with pairing, each level j has a 2x2 RDM:
      rho_j = diag(n_j, 1 - n_j) + off-diagonal from anomalous density
    The diagonal purity is:
      P_j = n_j^2 + (1 - n_j)^2
    Average: <P> = (1/L) sum_j P_j
    For uncorrelated: n_j = 0 or 1, <P> = 1
    For maximally mixed: n_j = 0.5, <P> = 0.5
    """
    P_j = n_j**2 + (1 - n_j)**2  # (local)
    return np.mean(P_j)

results_method2 = {}  # (local)

for nu in fillings:
    N_pair = max(1, int(round(nu * N_levels_fabric)))  # (local)
    print(f"\n--- nu = {nu:.2f}: N_pair = {N_pair} ---")

    if N_pair == 1:
        # Exact M=1 solution
        roots = solve_richardson_M1(eps_fab_sorted, f_sq_fab, g_eff)  # (local)
        if len(roots) > 0:
            E_alpha = roots[0]  # (local)
            n_j = compute_rg_occupations_M1(eps_fab_sorted, f_sq_fab, u_fab_sorted, E_alpha)
            P_avg = compute_rdm_purity(n_j)  # (local)
            PR = 1.0 / np.sum(n_j**2)  # (local) participation ratio
            print(f"  M=1 Richardson: E_alpha = {E_alpha:.10f}")
            print(f"  Participation ratio PR = {PR:.2f}")
            print(f"  <P>_RDM = {P_avg:.6f}")
            print(f"  n_j: min={n_j.min():.6e}, max={n_j.max():.6e}, sum={n_j.sum():.6f}")
            results_method2[nu] = {
                'N_pair': N_pair, 'E_gs': E_alpha, 'PR': PR,
                'P_avg': P_avg, 'n_j_min': n_j.min(), 'n_j_max': n_j.max(),
                'method': 'Richardson M=1 exact'
            }
        else:
            print("  WARNING: No Richardson root found!")
            results_method2[nu] = {'N_pair': N_pair, 'P_avg': np.nan, 'method': 'FAILED'}
    else:
        # For M > 1: use BCS mean-field as proxy, then compute purity from v_k^2
        # BCS gap equation on fabric: 1 = G * sum_j f_j^2 / (2*E_qp_j)
        # where E_qp_j = sqrt((eps_j - mu)^2 + (Delta * |u_j|)^2)
        #
        # The BCS occupations v_j^2 give the mean-field purity estimate.
        # For a BCS state, the exact purity is:
        #   P_j = (u_j^4 + v_j^4) where u_j^2 + v_j^2 = 1 (Bogoliubov amplitudes)
        # which equals (1 - 2*v_j^2*(1-v_j^2)).
        #
        # Correction for pair correlations beyond BCS:
        # The Richardson solution has LESS purity than BCS (more entanglement),
        # approximately by factor (1 - 2/N_pair) for large N_pair (Paper 17).

        # Find chemical potential for N_pair
        def number_eq(mu_trial, Delta_trial=0.3):
            E_qp = np.sqrt((eps_fab_sorted - mu_trial)**2 + (Delta_trial * np.abs(u_fab_sorted))**2)  # (local)
            v2 = 0.5 * (1 - (eps_fab_sorted - mu_trial) / E_qp)  # (local)
            return np.sum(v2) - N_pair

        # Scan for mu
        mu_lo = eps_fab_sorted[0] - 1.0  # (local)
        mu_hi = eps_fab_sorted[-1] + 1.0  # (local)
        try:
            mu_sol = brentq(number_eq, mu_lo, mu_hi)  # (local)
        except Exception:
            mu_sol = eps_fab_sorted[N_pair]  # (local) fallback

        # Solve BCS gap equation at this mu
        def gap_eq(Delta_trial):
            if Delta_trial <= 0:
                return 1e10
            E_qp = np.sqrt((eps_fab_sorted - mu_sol)**2 + (Delta_trial * np.abs(u_fab_sorted))**2)  # (local)
            return 1.0 - g_eff * np.sum(f_sq_fab / (2.0 * E_qp))

        # Scan for Delta
        Delta_vals = np.logspace(-4, 1, 200)  # (local)
        gap_vals = [gap_eq(d) for d in Delta_vals]  # (local)
        sign_changes = np.where(np.diff(np.sign(gap_vals)))[0]  # (local)
        Delta_sol = 0.0  # (local) default: no pairing

        if len(sign_changes) > 0:
            Delta_sol = brentq(gap_eq, Delta_vals[sign_changes[0]], Delta_vals[sign_changes[0] + 1])

        # Re-solve mu at the found Delta
        def number_eq_full(mu_trial):
            E_qp = np.sqrt((eps_fab_sorted - mu_trial)**2 + (Delta_sol * np.abs(u_fab_sorted))**2)
            v2 = 0.5 * (1 - (eps_fab_sorted - mu_trial) / E_qp)
            return np.sum(v2) - N_pair

        try:
            mu_sol = brentq(number_eq_full, mu_lo, mu_hi)
        except Exception:
            pass

        # Compute BCS occupations
        E_qp = np.sqrt((eps_fab_sorted - mu_sol)**2 + (Delta_sol * np.abs(u_fab_sorted))**2)  # (local)
        v2_bcs = 0.5 * (1 - (eps_fab_sorted - mu_sol) / E_qp)  # (local)
        u2_bcs = 1.0 - v2_bcs  # (local)

        # BCS purity: P_j = u_j^4 + v_j^4 = (1 - 2*v_j^2*(1-v_j^2))
        P_bcs_j = u2_bcs**2 + v2_bcs**2  # (local)
        P_bcs_avg = np.mean(P_bcs_j)  # (local)

        # Richardson correction: the EXACT purity is LOWER than BCS.
        # For the ultrasmall grain (Paper 17), the pair correlation function
        # deviates from BCS by O(1/N_pair). The correction factor is
        # approximately (1 - delta/N_pair) where delta ~ 0.5-2.0 depends
        # on the coupling strength g/d (g = coupling, d = mean level spacing).
        d_mean = (eps_fab_sorted[-1] - eps_fab_sorted[0]) / (N_levels_fabric - 1)  # (local)
        g_over_d = g_eff / d_mean  # (local) dimensionless coupling
        # From Paper 17 Fig. 5: delta(g/d) ~ 1.0 for g/d ~ 1, smaller for weaker coupling
        delta_correction = min(2.0, g_over_d)  # (local)
        P_RG_est = P_bcs_avg * (1 - delta_correction / N_pair)  # (local)

        # Number of levels near Fermi surface (within Delta of mu)
        near_fermi = np.sum(np.abs(eps_fab_sorted - mu_sol) < max(Delta_sol, 0.1))  # (local)

        print(f"  BCS solution: mu = {mu_sol:.6f}, Delta = {Delta_sol:.6f}")
        print(f"  g/d = {g_over_d:.4f}")
        print(f"  sum(v^2) = {np.sum(v2_bcs):.4f} (target {N_pair})")
        print(f"  <P>_BCS = {P_bcs_avg:.6f}")
        print(f"  <P>_RG_est = {P_RG_est:.6f} (with 1/N correction, delta={delta_correction:.3f})")
        print(f"  Levels near Fermi surface: {near_fermi}")

        results_method2[nu] = {
            'N_pair': N_pair, 'mu': mu_sol, 'Delta': Delta_sol,
            'g_over_d': g_over_d, 'P_bcs_avg': P_bcs_avg,
            'P_RG_est': P_RG_est, 'delta_correction': delta_correction,
            'near_fermi': near_fermi,
            'method': 'BCS + Richardson 1/N correction'
        }

# =====================================================================
#  7. METHOD 3: Ensemble-averaged <r> from effective single-cell model
# =====================================================================
#
# Nuclear structure insight (Paper 17, Paper 15):
# The level spacing ratio <r> for the FULL interaction can be estimated
# by an ensemble average over random matrix realizations with the same
# rank structure. The idea: sample effective single-particle spectra
# from the CG(24) band structure, compute <r> for each realization,
# and average.
#
# This gives the FABRIC-averaged <r> at each filling without requiring
# the impossible C(192, N_pair) diagonalization.

print("\n" + "=" * 72)
print("METHOD 3: Ensemble-Averaged <r> from Band-Sampled Spectra")
print("=" * 72)

N_ensemble = 100  # (local)
N_levels_eff = 16  # (local) effective 2-cell system (tractable ED)

def sample_effective_spectrum(eps_intra, evals_adj, E_J, n_cells_sample):
    """Sample an effective spectrum by randomly selecting Bloch eigenvalues."""
    n_sel = n_cells_sample  # (local)
    idx = np.random.choice(len(evals_adj), size=n_sel, replace=False)  # (local)
    lambda_sel = evals_adj[idx]  # (local)
    n_levels = n_sel * len(eps_intra)  # (local)
    eps = np.zeros(n_levels)  # (local)
    for k in range(len(eps_intra)):
        for n in range(n_sel):
            eps[k * n_sel + n] = eps_intra[k] + E_J * lambda_sel[n]
    return np.sort(eps)

# Build effective V_full for 2-cell cluster
V_eff = build_multi_cell_V(2, V_bare, N_modes)  # (local) 16x16

results_method3 = {}  # (local)

for nu in fillings:
    N_pair_eff = max(1, int(round(nu * N_levels_eff)))  # (local)
    dim_eff = mcomb(N_levels_eff, N_pair_eff)  # (local)

    if dim_eff > 50000:
        print(f"  nu={nu:.2f}: dim={dim_eff} too large, skipping")
        results_method3[nu] = {'r_full_mean': np.nan, 'r_full_std': np.nan,
                               'r_RG_mean': np.nan, 'r_RG_std': np.nan,
                               'N_pair': N_pair_eff, 'dim': dim_eff, 'skipped': True}
        continue

    print(f"\n--- nu = {nu:.2f}: N_pair = {N_pair_eff}, dim = {dim_eff}, {N_ensemble} samples ---")

    r_full_samples = []  # (local)
    r_RG_samples = []  # (local)

    for isamp in range(N_ensemble):
        eps_samp = sample_effective_spectrum(eps_bare, evals_adj_full, E_J_fold, 2)

        states = build_pair_fock_states(N_levels_eff, N_pair_eff)

        # Solve for g
        try:
            g_samp, mu_samp = solve_bcs_gap(eps_samp, None, N_pair_eff)
            g_samp = abs(g_samp)  # (local)
        except Exception:
            g_samp = g_eff  # (local) fallback

        H_RG = build_hamiltonian_RG(eps_samp, g_samp, states, N_levels_eff)
        H_full = build_hamiltonian_full(eps_samp, V_eff, states, N_levels_eff)

        evals_RG = np.sort(eigh(H_RG, eigvals_only=True))
        evals_full = np.sort(eigh(H_full, eigvals_only=True))

        r_RG_val, _, _ = compute_r_statistic(evals_RG)
        r_full_val, _, _ = compute_r_statistic(evals_full)

        if not np.isnan(r_RG_val):
            r_RG_samples.append(r_RG_val)
        if not np.isnan(r_full_val):
            r_full_samples.append(r_full_val)

    r_RG_arr = np.array(r_RG_samples)  # (local)
    r_full_arr = np.array(r_full_samples)  # (local)

    r_RG_mean = np.mean(r_RG_arr)  # (local)
    r_RG_std = np.std(r_RG_arr) / np.sqrt(len(r_RG_arr))  # (local) SEM
    r_full_mean = np.mean(r_full_arr)  # (local)
    r_full_std = np.std(r_full_arr) / np.sqrt(len(r_full_arr))  # (local) SEM

    print(f"  <r>_RG   = {r_RG_mean:.4f} +/- {r_RG_std:.4f} ({len(r_RG_arr)} valid)")
    print(f"  <r>_full = {r_full_mean:.4f} +/- {r_full_std:.4f} ({len(r_full_arr)} valid)")
    print(f"  Poisson: {r_Poisson:.4f}, GOE: {r_GOE:.4f}")

    results_method3[nu] = {
        'r_full_mean': r_full_mean, 'r_full_std': r_full_std,
        'r_RG_mean': r_RG_mean, 'r_RG_std': r_RG_std,
        'N_pair': N_pair_eff, 'dim': dim_eff,
        'n_valid_full': len(r_full_arr), 'n_valid_RG': len(r_RG_arr),
        'skipped': False
    }

# =====================================================================
#  8. SYNTHESIS AND GATE VERDICT
# =====================================================================

print("\n" + "=" * 72)
print("SYNTHESIS: <r> vs FILLING FRACTION")
print("=" * 72)

print("\n--- Method 1: Multi-cell ED ---")
print(f"{'Cells':>5} {'nu':>5} {'N_pair':>7} {'dim':>8} {'<r>_RG':>10} {'<r>_full':>10} {'err_full':>10}")
for key in sorted(results_method1.keys()):
    nc, nu = key
    r = results_method1[key]
    if r.get('skipped', False):
        print(f"{nc:5d} {nu:5.2f} {r['N_pair']:7d} {r['dim']:8d}     SKIPPED")
    else:
        print(f"{nc:5d} {nu:5.2f} {r['N_pair']:7d} {r['dim']:8d} {r['r_RG']:10.4f} {r['r_full']:10.4f} {r['r_err_full']:10.4f}")

print("\n--- Method 2: Richardson/BCS on 192-level fabric ---")
for nu in fillings:
    r = results_method2[nu]
    print(f"  nu = {nu:.2f}: {r['method']}")
    if 'P_avg' in r:
        print(f"    <P>_RDM = {r['P_avg']:.6f}")
    if 'P_bcs_avg' in r:
        print(f"    <P>_BCS = {r['P_bcs_avg']:.6f}, <P>_RG_est = {r['P_RG_est']:.6f}")

print("\n--- Method 3: Ensemble-averaged <r> (2-cell, 100 samples) ---")
print(f"{'nu':>5} {'N_pair':>7} {'<r>_RG':>10} {'<r>_full':>10} {'err_full':>10}")
for nu in fillings:
    r = results_method3[nu]
    if r.get('skipped', False):
        print(f"{nu:5.2f} {r['N_pair']:7d}     SKIPPED")
    else:
        print(f"{nu:5.2f} {r['N_pair']:7d} {r['r_RG_mean']:10.4f} {r['r_full_mean']:10.4f} {r['r_full_std']:10.4f}")

# Gate verdict for S75-J2-PCK-LARGE-N
# The gate criterion is <r> < 0.45 at filling = 0.15
# We use Method 3 (ensemble-averaged <r>_full at nu=0.15) as the primary diagnostic
r015 = results_method3.get(0.15, {})  # (local)
r010 = results_method3.get(0.10, {})  # (local)
r020 = results_method3.get(0.20, {})  # (local)

r_at_015 = r015.get('r_full_mean', np.nan)  # (local)
r_at_010 = r010.get('r_full_mean', np.nan)  # (local)
r_at_020 = r020.get('r_full_mean', np.nan)  # (local)

print("\n" + "=" * 72)
print("GATE VERDICT: S75-J2-PCK-LARGE-N")
print("=" * 72)

if not np.isnan(r_at_015) and r_at_015 < 0.45:
    gate_verdict = "PASS"
    gate_detail = f"<r>_full = {r_at_015:.4f} < 0.45 at nu=0.15"
elif not np.isnan(r_at_010) and r_at_010 < 0.45 and (np.isnan(r_at_015) or r_at_015 >= 0.45):
    gate_verdict = "INFO"
    gate_detail = f"<r>_full = {r_at_010:.4f} < 0.45 at nu=0.10, but {r_at_015:.4f} at nu=0.15"
else:
    gate_verdict = "FAIL"
    gate_detail = f"<r>_full = {r_at_010:.4f} (0.10), {r_at_015:.4f} (0.15), {r_at_020:.4f} (0.20)"

print(f"Verdict: {gate_verdict}")
print(f"Detail: {gate_detail}")
print(f"Threshold: <r> < 0.45 at nu=0.15")
print(f"Computed: <r>_full(0.10) = {r_at_010:.4f}, <r>_full(0.15) = {r_at_015:.4f}, <r>_full(0.20) = {r_at_020:.4f}")

# =====================================================================
#  9. SAVE RESULTS
# =====================================================================

# Flatten results for saving
save_dict = {
    'fillings': np.array(fillings),
    'N_levels_fabric': N_levels_fabric,
    'g_eff': g_eff,
    'rank1_frac': rank1_frac,
    'E_J_fold': E_J_fold,
    'r_Poisson': r_Poisson,
    'r_GOE': r_GOE,
    'gate_verdict': np.array([gate_verdict]),
    'gate_detail': np.array([gate_detail]),
    'gate_name': np.array(['S75-J2-PCK-LARGE-N']),
}

# Method 1 results
for key in results_method1:
    nc, nu = key
    r = results_method1[key]
    prefix = f'm1_c{nc}_nu{int(nu*100):03d}'  # (local)
    for k2, v2 in r.items():
        if isinstance(v2, (int, float, np.floating)):
            save_dict[f'{prefix}_{k2}'] = v2

# Method 2 results
for nu in fillings:
    r = results_method2[nu]
    prefix = f'm2_nu{int(nu*100):03d}'  # (local)
    for k2, v2 in r.items():
        if isinstance(v2, (int, float, np.floating)):
            save_dict[f'{prefix}_{k2}'] = v2

# Method 3 results
for nu in fillings:
    r = results_method3[nu]
    prefix = f'm3_nu{int(nu*100):03d}'  # (local)
    for k2, v2 in r.items():
        if isinstance(v2, (int, float, np.floating)):
            save_dict[f'{prefix}_{k2}'] = v2

out_path = os.path.join(data_dir, 's75_pck_large_n_pair.npz')
np.savez(out_path, **save_dict)
print(f"\nSaved: {out_path}")

# =====================================================================
#  10. FIGURE
# =====================================================================

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Panel (a): Method 1 — <r>_full vs filling for different cluster sizes
ax = axes[0]
for nc in cluster_sizes:
    nus_plot = []  # (local)
    rs_plot = []  # (local)
    errs_plot = []  # (local)
    for nu in fillings:
        r = results_method1.get((nc, nu), {})
        if not r.get('skipped', True):
            nus_plot.append(nu)
            rs_plot.append(r['r_full'])
            errs_plot.append(r['r_err_full'])
    if nus_plot:
        ax.errorbar(nus_plot, rs_plot, yerr=errs_plot, marker='o', label=f'{nc}-cell', capsize=3)
ax.axhline(r_Poisson, color='b', ls='--', alpha=0.5, label='Poisson')
ax.axhline(r_GOE, color='r', ls='--', alpha=0.5, label='GOE')
ax.axhline(0.45, color='k', ls=':', alpha=0.5, label='Gate threshold')
ax.set_xlabel('Filling fraction nu')
ax.set_ylabel('<r>')
ax.set_title('Method 1: Multi-cell ED')
ax.legend(fontsize=8)

# Panel (b): Method 2 — RDM purity vs filling
ax = axes[1]
nus_p = []  # (local)
P_bcs = []  # (local)
P_rg = []  # (local)
for nu in fillings:
    r = results_method2[nu]
    nus_p.append(nu)
    if 'P_avg' in r:
        P_bcs.append(r['P_avg'])
        P_rg.append(r['P_avg'])
    elif 'P_bcs_avg' in r:
        P_bcs.append(r['P_bcs_avg'])
        P_rg.append(r['P_RG_est'])
ax.plot(nus_p, P_bcs, 'o-', label='BCS purity')
ax.plot(nus_p, P_rg, 's--', label='RG-corrected purity')
ax.axhline(0.5, color='k', ls=':', alpha=0.5, label='Max mixing')
ax.set_xlabel('Filling fraction nu')
ax.set_ylabel('<P> = Tr(rho_j^2)')
ax.set_title('Method 2: RDM Purity (192 levels)')
ax.legend(fontsize=8)

# Panel (c): Method 3 — Ensemble <r>_full vs filling
ax = axes[2]
nus_e = []  # (local)
r_full_e = []  # (local)
r_rg_e = []  # (local)
err_full_e = []  # (local)
err_rg_e = []  # (local)
for nu in fillings:
    r = results_method3[nu]
    if not r.get('skipped', True):
        nus_e.append(nu)
        r_full_e.append(r['r_full_mean'])
        r_rg_e.append(r['r_RG_mean'])
        err_full_e.append(r['r_full_std'])
        err_rg_e.append(r['r_RG_std'])
if nus_e:
    ax.errorbar(nus_e, r_full_e, yerr=err_full_e, marker='o', label='<r>_full', capsize=3)
    ax.errorbar(nus_e, r_rg_e, yerr=err_rg_e, marker='s', label='<r>_RG', capsize=3)
ax.axhline(r_Poisson, color='b', ls='--', alpha=0.5, label='Poisson')
ax.axhline(r_GOE, color='r', ls='--', alpha=0.5, label='GOE')
ax.axhline(0.45, color='k', ls=':', alpha=0.5, label='Gate threshold')
ax.set_xlabel('Filling fraction nu')
ax.set_ylabel('<r>')
ax.set_title('Method 3: Ensemble (2-cell, 100 samples)')
ax.legend(fontsize=8)

plt.tight_layout()
fig_path = os.path.join(data_dir, 's75_pck_large_n_pair.png')
plt.savefig(fig_path, dpi=150)
plt.close()
print(f"Figure saved: {fig_path}")

print("\n" + "=" * 72)
print("DONE: PCK-LARGE-N-PAIR-75")
print("=" * 72)
