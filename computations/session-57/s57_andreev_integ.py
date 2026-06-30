#!/usr/bin/env python3
"""
s57_andreev_integ.py -- ANDREEV-INTEG-57 (Kitaev, W1-4)
========================================================

Explicit Andreev Hamiltonian construction and integrability test.

The question: Does the mode-dependent Andreev tunneling channel break
Richardson-Gaudin integrability at the fabric level?

W0-4 computed the physical t_k = J_C2 * (u_k^2 - v_k^2) for all 8 modes.
The t_k are MONOTONICALLY INCREASING -- a smooth function of mode energy,
NOT random. W0-4 concluded this rank-1 diagonal perturbation cannot break
R-G integrability. This computation VERIFIES that conclusion by exact
diagonalization and level statistics.

Method:
  H_full = H_BCS^(1) + H_BCS^(2) + H_J(isotropic) + alpha * H_A
  on the 120-dim Fock space (2-cell, N_pair_total=2, 16 modes total).

  H_A = Sum_k t_k * gamma_k^(1)dag * gamma_k^(2) + h.c.
  implemented in pair basis as mode-dependent inter-cell tunneling.

Diagnostics:
  1. Level spacing ratio <r> at alpha = 0, 0.1, 0.5, 1.0, 2.0
  2. ||[H_A, Q_j]|| / ||Q_j|| for Richardson-Gaudin conserved quantities
  3. Spectral form factor K(t) at alpha = 1.0
  4. OTOC growth (if <r> > 0.45)

Gate: ANDREEV-INTEG-57
  PASS: <r> > 0.48 (integrability broken)
  FAIL: <r> < 0.40 (Poisson persists)
  INFO: 0.40 < <r> < 0.48

Author: Kitaev Quantum Chaos Theorist (S57 W1-4)
"""

import sys
import os
import numpy as np
from scipy.linalg import eigh, expm, norm
from itertools import combinations
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    tau_fold, J_C2, Delta_0_GL, Delta_0_OES,
    N_dof_BCS, E_cond, T_acoustic, gamma_RP,
)

data_dir = os.path.dirname(os.path.abspath(__file__))

# ============================================================
# 0. Load input data
# ============================================================

d54 = np.load(os.path.join(data_dir, 's54_ed_sweep.npz'), allow_pickle=True)
d56 = np.load(os.path.join(data_dir, 's56_fabric_integ.npz'), allow_pickle=True)
d57 = np.load(os.path.join(data_dir, 's57_andreev_anisotropy.npz'), allow_pickle=True)

fold_idx = int(d54['fold_idx'])  # = 19
E_sp = d54['E_sp_sweep']         # (50, 8)
V_bare = d54['V_bare_cont']      # (8, 8) pairing interaction
eps_fold = E_sp[fold_idx].copy()  # (8,) single-particle energies at fold

# Physical t_k from W0-4 (mean-field, appropriate for thermodynamic limit)
t_k_MF = d57['t_k_MF']           # (8,) Andreev transmission amplitudes
t_k_ED = d57['t_k_ED']           # (8,) ED version for cross-check
eps_A_MF = float(d57['eps_A_MF'])

# Josephson coupling from S56
E_J_fold = float(d56['E_J_fold'])

# Symmetrize V
V_fold = (V_bare + V_bare.T) / 2.0

N_modes = N_dof_BCS  # = 8
N_pair_total = 2     # 2 Cooper pairs across 2 cells

print("=" * 72)
print("ANDREEV-INTEG-57 (Kitaev, W1-4)")
print("=" * 72)
print(f"tau_fold = {tau_fold}")
print(f"N_modes = {N_modes}, N_pair_total = {N_pair_total}")
print(f"eps_fold = {eps_fold}")
print(f"t_k (MF) = {t_k_MF}")
print(f"t_k (ED) = {t_k_ED}")
print(f"eps_A (MF) = {eps_A_MF:.4f}")
print(f"E_J_fold = {E_J_fold:.4f} M_KK")
print(f"V_bare diagonal = {np.diag(V_fold)}")

# ============================================================
# 1. Build pair basis (identical to S56)
# ============================================================

n_modes_total = 2 * N_modes  # 16 modes (8 per cell)
basis = list(combinations(range(n_modes_total), N_pair_total))
dim = len(basis)
assert dim == 120, f"Expected dim=120, got {dim}"
basis_dict = {state: idx for idx, state in enumerate(basis)}

print(f"\nHilbert space: C({n_modes_total},{N_pair_total}) = {dim} states")


# ============================================================
# 2. Build Hamiltonians
# ============================================================

def build_H_BCS(eps_1, eps_2, V_1, V_2):
    """
    Build H_BCS^(1) + H_BCS^(2) in the pair basis.
    No inter-cell coupling. Returns (dim, dim) matrix.
    """
    H = np.zeros((dim, dim))
    for i, state_i in enumerate(basis):
        # Diagonal: kinetic energy
        E_kin = 0.0  # (local)
        for k in state_i:
            if k < N_modes:
                E_kin += 2.0 * eps_1[k]
            else:
                E_kin += 2.0 * eps_2[k - N_modes]
        H[i, i] += E_kin

        # BCS pairing within each cell
        for pos, k in enumerate(state_i):
            if k < N_modes:
                k_local = k
                V_cell = V_1
                offset = 0  # (local)
            else:
                k_local = k - N_modes
                V_cell = V_2
                offset = N_modes

            for l_local in range(N_modes):
                l = l_local + offset
                if l == k:
                    H[i, i] -= V_cell[k_local, k_local]
                    continue
                if l in state_i:
                    continue
                new_state = list(state_i)
                new_state[pos] = l
                new_state = tuple(sorted(new_state))
                if new_state in basis_dict:
                    j = basis_dict[new_state]
                    H[i, j] -= V_cell[l_local, k_local]

    return (H + H.T) / 2.0


def build_H_Josephson(E_J):
    """
    Build H_J = -(E_J/2) * (B_1^dag B_2 + B_2^dag B_1).
    Isotropic: all modes couple with equal strength.
    """
    H = np.zeros((dim, dim))
    for i, state_i in enumerate(basis):
        for pos, k in enumerate(state_i):
            if k >= N_modes:
                # Pair in cell 2 -> transfer to cell 1
                for l1 in range(N_modes):
                    if l1 in state_i:
                        continue
                    new_state = list(state_i)
                    new_state[pos] = l1
                    new_state = tuple(sorted(new_state))
                    if new_state in basis_dict:
                        j = basis_dict[new_state]
                        H[i, j] -= E_J / 2.0
            else:
                # Pair in cell 1 -> transfer to cell 2
                for l2_local in range(N_modes):
                    l2 = l2_local + N_modes
                    if l2 in state_i:
                        continue
                    new_state = list(state_i)
                    new_state[pos] = l2
                    new_state = tuple(sorted(new_state))
                    if new_state in basis_dict:
                        j = basis_dict[new_state]
                        H[i, j] -= E_J / 2.0

    return (H + H.T) / 2.0


def build_H_Andreev(t_k_vals):
    """
    Build H_A = Sum_k t_k * (b_k^(1)dag b_k^(2) + h.c.)

    Mode-dependent Andreev tunneling: pair in mode k of cell 2 tunnels
    to mode k of cell 1 with amplitude t_k. This is DIAGONAL in mode
    index -- pair transfers only within the same mode across cells.

    In the pair basis: if state has pair in mode k+N_modes (cell 2),
    replace with pair in mode k (cell 1), with amplitude -t_k/2.
    """
    H = np.zeros((dim, dim))
    for i, state_i in enumerate(basis):
        for pos, k_global in enumerate(state_i):
            if k_global >= N_modes:
                # Pair in cell 2, mode k_local = k_global - N_modes
                k_local = k_global - N_modes
                # Transfer to same mode in cell 1
                l = k_local  # cell 1 mode
                if l in state_i:
                    continue
                new_state = list(state_i)
                new_state[pos] = l
                new_state = tuple(sorted(new_state))
                if new_state in basis_dict:
                    j = basis_dict[new_state]
                    H[i, j] -= t_k_vals[k_local] / 2.0

            elif k_global < N_modes:
                # Pair in cell 1, mode k_local = k_global
                k_local = k_global
                # Transfer to same mode in cell 2
                l = k_local + N_modes
                if l in state_i:
                    continue
                new_state = list(state_i)
                new_state[pos] = l
                new_state = tuple(sorted(new_state))
                if new_state in basis_dict:
                    j = basis_dict[new_state]
                    H[i, j] -= t_k_vals[k_local] / 2.0

    return (H + H.T) / 2.0


def compute_gap_ratio(eigenvalues, trim_frac=0.1):
    """
    Compute mean adjacent gap ratio <r>.
    Uses central (1-2*trim_frac) of the spectrum.
    """
    E = np.sort(eigenvalues)
    spacings = np.diff(E)
    mean_sp = np.mean(np.abs(spacings))
    if mean_sp == 0:
        return np.nan, 0
    mask = spacings > 1e-10 * mean_sp
    spacings_clean = spacings[mask]
    if len(spacings_clean) < 10:
        return np.nan, 0

    n = len(spacings_clean)
    start = int(n * trim_frac)
    end = n - int(n * trim_frac)
    s = spacings_clean[start:end]

    r_vals = []
    for i in range(len(s) - 1):
        r = min(s[i], s[i+1]) / max(s[i], s[i+1])
        r_vals.append(r)

    return np.mean(r_vals), len(r_vals)


# ============================================================
# 3. Build Richardson-Gaudin conserved quantities Q_j
# ============================================================
#
# For the reduced BCS (pair) Hamiltonian with N_modes levels,
# the Richardson-Gaudin integrals of motion are:
#   Q_j = S_j^z + g * Sum_{k != j} (S_j^+ S_k^- + S_j^- S_k^+ + 2 S_j^z S_k^z) / (eps_j - eps_k)
#
# where S_j^+, S_j^-, S_j^z are the pair pseudospin operators for mode j:
#   S_j^+ = b_j^dag (pair creation), S_j^- = b_j (pair annihilation),
#   S_j^z = (n_j - 1/2) / 2 where n_j = 0,1 is pair occupation.
#
# For the 2-cell system, the R-G integrals for each cell are:
#   Q_j^(cell) (j = 0,...,7 for each cell)
#
# In the pair basis, we can represent these as matrices.

def build_RG_conserved(eps, V, cell_offset, g_eff):
    """
    Build the 8 Richardson-Gaudin conserved quantities for one cell.

    Q_j = S_j^z + g_eff * Sum_{k!=j} [S_j^+ S_k^- + S_j^- S_k^+ + 2 S_j^z S_k^z]
                                       / (eps_j - eps_k)

    Parameters:
        eps: (N_modes,) single-particle energies
        V: (N_modes, N_modes) pairing matrix (not used directly -- g_eff encodes coupling)
        cell_offset: 0 for cell 1, N_modes for cell 2
        g_eff: effective coupling strength (from mean V)

    Returns: list of (dim, dim) matrices Q_0, ..., Q_{N_modes-1}
    """
    Q_list = []
    for j in range(N_modes):
        Q = np.zeros((dim, dim))

        for i_state, state in enumerate(basis):
            j_global = j + cell_offset

            # S_j^z: (n_j - 1/2) / 2
            #   n_j = 1 if j_global in state, else 0
            n_j = 1 if j_global in state else 0
            Q[i_state, i_state] += (n_j - 0.5) / 2.0

            # Sum over k != j (same cell)
            for k in range(N_modes):
                if k == j:
                    continue
                k_global = k + cell_offset

                # Denominator
                denom = eps[j] - eps[k]
                if abs(denom) < 1e-14:
                    continue  # Skip degenerate levels

                # S_j^+ S_k^-: annihilate pair in k, create in j (same cell)
                # state must have k_global, must not have j_global
                if k_global in state and j_global not in state:
                    new_state = list(state)
                    new_state[new_state.index(k_global)] = j_global
                    new_state = tuple(sorted(new_state))
                    if new_state in basis_dict:
                        j_idx = basis_dict[new_state]
                        Q[i_state, j_idx] += g_eff / denom

                # S_j^- S_k^+: annihilate pair in j, create in k
                if j_global in state and k_global not in state:
                    new_state = list(state)
                    new_state[new_state.index(j_global)] = k_global
                    new_state = tuple(sorted(new_state))
                    if new_state in basis_dict:
                        j_idx = basis_dict[new_state]
                        Q[i_state, j_idx] += g_eff / denom

                # 2 S_j^z S_k^z
                n_k = 1 if k_global in state else 0
                Q[i_state, i_state] += 2.0 * g_eff * (n_j - 0.5) * (n_k - 0.5) / (4.0 * denom)

        Q = (Q + Q.T) / 2.0
        Q_list.append(Q)

    return Q_list


# Effective coupling strength from pairing matrix
g_eff = np.mean(np.abs(V_fold))
print(f"\ng_eff (mean |V_kl|) = {g_eff:.6f}")

# Build R-G conserved quantities for both cells
print("Building Richardson-Gaudin conserved quantities...")
Q_cell1 = build_RG_conserved(eps_fold, V_fold, 0, g_eff)
Q_cell2 = build_RG_conserved(eps_fold, V_fold, N_modes, g_eff)
Q_all = Q_cell1 + Q_cell2  # 16 conserved quantities total

# Verify R-G commute with H_BCS at alpha=0
H_BCS = build_H_BCS(eps_fold, eps_fold, V_fold, V_fold)
print(f"H_BCS built. Hermiticity: {np.max(np.abs(H_BCS - H_BCS.T)):.2e}")

print("\nR-G commutator check [Q_j, H_BCS]:")
for j, Q in enumerate(Q_all):
    comm = Q @ H_BCS - H_BCS @ Q
    cell_label = f"cell{1 + j // N_modes}"
    mode_label = j % N_modes
    comm_norm = norm(comm, 'fro')
    Q_norm = norm(Q, 'fro')
    rel = comm_norm / Q_norm if Q_norm > 0 else 0
    if j < 4 or j >= 12:  # print a subset
        print(f"  Q_{mode_label}^({cell_label}): ||[Q,H_BCS]|| = {comm_norm:.4e}, "
              f"||Q|| = {Q_norm:.4e}, ratio = {rel:.4e}")


# ============================================================
# 4. Build component Hamiltonians
# ============================================================

print("\n" + "=" * 72)
print("BUILDING COMPONENT HAMILTONIANS")
print("=" * 72)

H_J_iso = build_H_Josephson(E_J_fold)
H_A_MF = build_H_Andreev(t_k_MF)
H_A_ED = build_H_Andreev(t_k_ED)

print(f"H_J (isotropic) built. ||H_J|| = {norm(H_J_iso, 'fro'):.4f}")
print(f"H_A (MF t_k) built. ||H_A|| = {norm(H_A_MF, 'fro'):.4f}")
print(f"H_A (ED t_k) built. ||H_A|| = {norm(H_A_ED, 'fro'):.4f}")

# Verify symmetry
print(f"H_J Hermiticity: {np.max(np.abs(H_J_iso - H_J_iso.T)):.2e}")
print(f"H_A_MF Hermiticity: {np.max(np.abs(H_A_MF - H_A_MF.T)):.2e}")
print(f"H_A_ED Hermiticity: {np.max(np.abs(H_A_ED - H_A_ED.T)):.2e}")

# Compare H_A vs H_J
print(f"\n||H_A_MF|| / ||H_J|| = {norm(H_A_MF, 'fro') / norm(H_J_iso, 'fro'):.4f}")
print(f"||H_A_ED|| / ||H_J|| = {norm(H_A_ED, 'fro') / norm(H_J_iso, 'fro'):.4f}")


# ============================================================
# 5. R-G commutator with H_A
# ============================================================

print("\n" + "=" * 72)
print("RICHARDSON-GAUDIN COMMUTATOR WITH H_ANDREEV")
print("=" * 72)

comm_norms_MF = np.zeros(len(Q_all))
comm_norms_ED = np.zeros(len(Q_all))
Q_norms = np.zeros(len(Q_all))

for j, Q in enumerate(Q_all):
    Q_norms[j] = norm(Q, 'fro')

    comm_MF = Q @ H_A_MF - H_A_MF @ Q
    comm_norms_MF[j] = norm(comm_MF, 'fro')

    comm_ED = Q @ H_A_ED - H_A_ED @ Q
    comm_norms_ED[j] = norm(comm_ED, 'fro')

    cell_label = f"cell{1 + j // N_modes}"
    mode_label = j % N_modes
    ratio_MF = comm_norms_MF[j] / Q_norms[j] if Q_norms[j] > 0 else 0
    ratio_ED = comm_norms_ED[j] / Q_norms[j] if Q_norms[j] > 0 else 0
    print(f"  Q_{mode_label}^({cell_label}): "
          f"||[Q,H_A_MF]||/||Q|| = {ratio_MF:.4f}, "
          f"||[Q,H_A_ED]||/||Q|| = {ratio_ED:.4f}")

max_ratio_MF = np.max(comm_norms_MF / np.maximum(Q_norms, 1e-15))
max_ratio_ED = np.max(comm_norms_ED / np.maximum(Q_norms, 1e-15))
mean_ratio_MF = np.mean(comm_norms_MF / np.maximum(Q_norms, 1e-15))
mean_ratio_ED = np.mean(comm_norms_ED / np.maximum(Q_norms, 1e-15))

print(f"\nMax ||[Q,H_A]||/||Q|| (MF): {max_ratio_MF:.4f}")
print(f"Max ||[Q,H_A]||/||Q|| (ED): {max_ratio_ED:.4f}")
print(f"Mean ||[Q,H_A]||/||Q|| (MF): {mean_ratio_MF:.4f}")
print(f"Mean ||[Q,H_A]||/||Q|| (ED): {mean_ratio_ED:.4f}")

# Also check [H_A, H_J]
comm_AJ = H_A_MF @ H_J_iso - H_J_iso @ H_A_MF
print(f"\n||[H_A_MF, H_J]|| = {norm(comm_AJ, 'fro'):.4f}")
print(f"||[H_A_MF, H_J]|| / ||H_J|| = {norm(comm_AJ, 'fro') / norm(H_J_iso, 'fro'):.4f}")


# ============================================================
# 6. Alpha sweep: H_full = H_BCS + H_J + alpha * H_A
# ============================================================

print("\n" + "=" * 72)
print("ALPHA SWEEP: Level Spacing Ratio <r>")
print("=" * 72)

# Baseline: H_BCS + H_J (S56 result at alpha_J=1)
H_base = H_BCS + H_J_iso

alpha_values = np.array([0.0, 0.05, 0.1, 0.2, 0.3, 0.5, 0.7, 1.0, 1.5, 2.0, 3.0, 5.0])
n_alpha = len(alpha_values)

r_means_MF = np.zeros(n_alpha)
r_means_ED = np.zeros(n_alpha)
n_ratios_MF = np.zeros(n_alpha, dtype=int)
n_ratios_ED = np.zeros(n_alpha, dtype=int)
eigenvalue_sets_MF = []
eigenvalue_sets_ED = []

# Also break cell exchange symmetry for a cleaner diagnostic
# Use eps_fold for cell 1, eps_fold * 1.05 for cell 2 (same as S56)
eps_fold_2 = eps_fold * 1.05
H_BCS_asym = build_H_BCS(eps_fold, eps_fold_2, V_fold, V_fold)
H_base_asym = H_BCS_asym + H_J_iso

r_means_asym_MF = np.zeros(n_alpha)
r_means_asym_ED = np.zeros(n_alpha)
n_ratios_asym_MF = np.zeros(n_alpha, dtype=int)
n_ratios_asym_ED = np.zeros(n_alpha, dtype=int)

for i_a, alpha in enumerate(alpha_values):
    # Symmetric cells
    H_full_MF = H_base + alpha * H_A_MF
    H_full_ED = H_base + alpha * H_A_ED

    evals_MF = eigh(H_full_MF, eigvals_only=True)
    evals_ED = eigh(H_full_ED, eigvals_only=True)
    eigenvalue_sets_MF.append(evals_MF)
    eigenvalue_sets_ED.append(evals_ED)

    r_MF, nr_MF = compute_gap_ratio(evals_MF)
    r_ED, nr_ED = compute_gap_ratio(evals_ED)
    r_means_MF[i_a] = r_MF
    r_means_ED[i_a] = r_ED
    n_ratios_MF[i_a] = nr_MF
    n_ratios_ED[i_a] = nr_ED

    # Asymmetric cells
    H_asym_MF = H_base_asym + alpha * H_A_MF
    H_asym_ED = H_base_asym + alpha * H_A_ED

    evals_asym_MF = eigh(H_asym_MF, eigvals_only=True)
    evals_asym_ED = eigh(H_asym_ED, eigvals_only=True)

    r_a_MF, nr_a_MF = compute_gap_ratio(evals_asym_MF)
    r_a_ED, nr_a_ED = compute_gap_ratio(evals_asym_ED)
    r_means_asym_MF[i_a] = r_a_MF
    r_means_asym_ED[i_a] = r_a_ED
    n_ratios_asym_MF[i_a] = nr_a_MF
    n_ratios_asym_ED[i_a] = nr_a_ED

    print(f"  alpha={alpha:5.2f}: <r>_sym(MF)={r_MF:.4f} (n={nr_MF:3d}), "
          f"<r>_sym(ED)={r_ED:.4f} (n={nr_ED:3d}), "
          f"<r>_asym(MF)={r_a_MF:.4f}, <r>_asym(ED)={r_a_ED:.4f}")

print(f"\nPOISSON reference: <r> = 0.3863")
print(f"GOE reference:     <r> = 0.5307")
print(f"Gate threshold: PASS > 0.48, FAIL < 0.40")

# Physical alpha = 1.0
idx_phys = np.argmin(np.abs(alpha_values - 1.0))
r_physical_MF = r_means_asym_MF[idx_phys]
r_physical_ED = r_means_asym_ED[idx_phys]
print(f"\nPhysical (alpha=1.0, asymmetric cells):")
print(f"  <r> (MF) = {r_physical_MF:.4f}")
print(f"  <r> (ED) = {r_physical_ED:.4f}")


# ============================================================
# 7. Spectral Form Factor at alpha = 1.0
# ============================================================

print("\n" + "=" * 72)
print("SPECTRAL FORM FACTOR (SFF)")
print("=" * 72)

# Use the asymmetric cell spectrum at alpha=1.0 (cleaner)
evals_sff = eigh(H_base_asym + 1.0 * H_A_MF, eigvals_only=True)

# Unfold: subtract mean and normalize by local mean spacing
E_sort = np.sort(evals_sff)
n_evals = len(E_sort)

# Simple unfolding: cumulative staircase -> normalized
# Polynomial fit to the staircase
x = np.arange(n_evals) / n_evals  # uniform on [0,1]
# Mean spacing
mean_sp_sff = np.mean(np.diff(E_sort))
E_unfolded = (E_sort - E_sort[0]) / mean_sp_sff

# SFF: K(t) = |Sum_n exp(i * E_n_unfolded * t)|^2 / N^2
t_max = 200.0  # (local)
n_t = 2000  # (local)
t_sff = np.linspace(0.01, t_max, n_t)
K_sff = np.zeros(n_t)

for it, t in enumerate(t_sff):
    phases = np.exp(1j * E_unfolded * t)
    Z = np.sum(phases)
    K_sff[it] = np.abs(Z)**2 / n_evals**2

# Connected SFF: subtract disconnected part
K_conn = K_sff - 1.0  # K_disc = 1 for unfolded spectrum
# For Poisson: K_conn(t) = 0 (no correlations)
# For GUE: K_conn(t) = t/(2*pi*N) for t < t_H, then plateau at 1

# Identify ramp/plateau
# Heisenberg time: t_H = 2*pi*N / <spacing> = 2*pi*N for unfolded
t_H = 2 * np.pi * n_evals
K_plateau = np.mean(K_sff[-n_t//4:])

print(f"Heisenberg time t_H = {t_H:.1f}")
print(f"SFF plateau value (last 25%): K = {K_plateau:.4f}")
print(f"GUE plateau: K = 1.0 (unfolded)")
print(f"SFF mean (all t): K = {np.mean(K_sff):.4f}")

# Check for ramp: linear increase region
# For GUE, K(t) ~ t/(2*pi*N) at early times
# For Poisson, K(t) ~ 1 + delta(t=0)
# Check slope in early region
early_mask = (t_sff > 1) & (t_sff < 50)
if np.sum(early_mask) > 5:
    slope = np.polyfit(t_sff[early_mask], K_sff[early_mask], 1)[0]
    gue_slope = 1.0 / (2 * np.pi * n_evals)
    print(f"SFF early slope: {slope:.6f} (GUE prediction: {gue_slope:.6f})")
    print(f"Slope / GUE = {slope / gue_slope:.3f}")


# ============================================================
# 8. OTOC at alpha = 1.0 (conditional on <r> > 0.45)
# ============================================================

print("\n" + "=" * 72)
print("OTOC GROWTH ANALYSIS")
print("=" * 72)

# Compute OTOC regardless of <r>, for completeness
# C(t) = -<[W(t), V(0)]^2>_beta
# Use infinite temperature (beta=0, trace average)
# W = pair number on mode 0 of cell 1: n_0^(1)
# V = pair number on mode 0 of cell 2: n_0^(2)

# Build n_0^(1) and n_0^(2) in pair basis
def build_pair_number(mode_global):
    """Build pair number operator n_k (0 or 1) in the pair basis."""
    n_op = np.zeros((dim, dim))
    for i, state in enumerate(basis):
        if mode_global in state:
            n_op[i, i] = 1.0
    return n_op

W_op = build_pair_number(0)            # mode 0, cell 1
V_op = build_pair_number(N_modes)      # mode 0, cell 2

# Full Hamiltonian at alpha = 1.0 (asymmetric cells)
H_otoc = H_base_asym + 1.0 * H_A_MF
evals_otoc, evecs_otoc = eigh(H_otoc)

# OTOC: C(t) = Tr([W(t), V]^2) / dim  (infinite temperature)
# W(t) = exp(iHt) W exp(-iHt)
# [W(t), V] = W(t)V - VW(t)

n_t_otoc = 500
t_max_otoc = 50.0  # (local)
t_otoc = np.linspace(0.0, t_max_otoc, n_t_otoc)
C_otoc = np.zeros(n_t_otoc)

# Diagonalize: H = U diag(E) U^T
# W(t) = U diag(e^{iEt}) U^T W U diag(e^{-iEt}) U^T
W_eig = evecs_otoc.T @ W_op @ evecs_otoc  # W in energy basis
V_eig = evecs_otoc.T @ V_op @ evecs_otoc

for it, t in enumerate(t_otoc):
    # Phase factors
    phases = np.exp(1j * evals_otoc * t)
    phases_dag = np.exp(-1j * evals_otoc * t)

    # W(t) in energy basis: W(t)_{ij} = phases[i] * W_eig[i,j] * phases_dag[j]
    W_t_eig = W_eig * phases[:, None] * phases_dag[None, :]

    # Commutator in energy basis
    comm = W_t_eig @ V_eig - V_eig @ W_t_eig

    # C(t) = -Tr(comm^2) / dim = Tr(comm @ comm^dag) / dim (comm is anti-Hermitian)
    C_otoc[it] = np.real(np.trace(comm @ comm.conj().T)) / dim

# Normalize by C(0) if nonzero
C_0_val = C_otoc[0]
print(f"C(0) = {C_0_val:.6e}")

# Look for exponential growth in early time
# C(t) ~ C_0 + A * exp(lambda_L * t) at early times
# Actually C(0) = 0 for commuting operators at equal time
# C(t) ~ a * t^2 for generic early time (from BCH expansion)

# Find the max of C(t)
C_max = np.max(C_otoc)
t_max_C = t_otoc[np.argmax(C_otoc)]
print(f"C_max = {C_max:.6e} at t = {t_max_C:.2f}")

# Try to fit exponential growth in early time
# Only fit where C > 0.01 * C_max and C < 0.5 * C_max
if C_max > 1e-10:
    growth_mask = (C_otoc > 0.01 * C_max) & (C_otoc < 0.5 * C_max) & (t_otoc > 0)
    if np.sum(growth_mask) > 5:
        t_fit = t_otoc[growth_mask]
        logC_fit = np.log(C_otoc[growth_mask])
        # Linear fit to log(C) vs t
        coeffs = np.polyfit(t_fit, logC_fit, 1)
        lambda_L_fit = coeffs[0]
        # Also fit power law: log(C) = beta * log(t) + const
        log_t_fit = np.log(t_fit)
        coeffs_power = np.polyfit(log_t_fit, logC_fit, 1)
        beta_power = coeffs_power[0]

        # R^2 for both fits
        logC_pred_exp = np.polyval(coeffs, t_fit)
        logC_pred_pow = np.polyval(coeffs_power, log_t_fit)
        ss_res_exp = np.sum((logC_fit - logC_pred_exp)**2)
        ss_res_pow = np.sum((logC_fit - logC_pred_pow)**2)
        ss_tot = np.sum((logC_fit - np.mean(logC_fit))**2)
        R2_exp = 1 - ss_res_exp / ss_tot if ss_tot > 0 else 0
        R2_pow = 1 - ss_res_pow / ss_tot if ss_tot > 0 else 0

        print(f"\nExponential fit: lambda_L = {lambda_L_fit:.4f} M_KK (R^2 = {R2_exp:.4f})")
        print(f"Power law fit: beta = {beta_power:.2f} (R^2 = {R2_pow:.4f})")

        # MSS bound
        lambda_MSS = 2 * np.pi * T_acoustic
        print(f"MSS bound: lambda_L_max = 2*pi*T = {lambda_MSS:.4f} M_KK")
        if lambda_L_fit > 0:
            print(f"lambda_L / lambda_MSS = {lambda_L_fit / lambda_MSS:.4f}")
        print(f"Growth type: {'EXPONENTIAL' if R2_exp > R2_pow + 0.05 else 'POWER LAW' if R2_pow > R2_exp + 0.05 else 'AMBIGUOUS'}")
    else:
        lambda_L_fit = 0.0  # (local)
        beta_power = 0.0  # (local)
        R2_exp = 0.0  # (local)
        R2_pow = 0.0  # (local)
        print("Insufficient growth region for fitting")
else:
    lambda_L_fit = 0.0  # (local)
    beta_power = 0.0  # (local)
    R2_exp = 0.0  # (local)
    R2_pow = 0.0  # (local)
    print("C_max too small for analysis")


# ============================================================
# 9. Tau sweep at alpha = 1.0 (Kitaev K2 criterion)
# ============================================================

print("\n" + "=" * 72)
print("TAU SWEEP (Kitaev K2 criterion: any tau in [0.08, 0.22]?)")
print("=" * 72)

# Re-use the S54 data for tau sweep
tau_values = d54['tau_values']
tau_indices_K2 = np.where((tau_values >= 0.08) & (tau_values <= 0.22))[0]
print(f"Tau values in [0.08, 0.22]: {tau_values[tau_indices_K2]}")

# Compute t_k at each tau using mean-field formula
# t_k = J_C2(tau) * xi_k(tau) / E_k(tau)
# where E_k = sqrt(xi_k^2 + Delta^2)

J_C2_tau = d54.get('J_C2_tau', None)
if J_C2_tau is None:
    # Load from TB data
    tb_data = np.load(os.path.join(data_dir, 's54_tb_hamiltonian.npz'), allow_pickle=True)
    J_C2_tau = tb_data['J_C2_tau']

r_tau_sweep = np.zeros(len(tau_indices_K2))
tau_sweep_vals = np.zeros(len(tau_indices_K2))

for it, ti in enumerate(tau_indices_K2):
    eps_tau = E_sp[ti].copy()
    tau_val = tau_values[ti]
    tau_sweep_vals[it] = tau_val

    # Compute MF t_k at this tau
    Delta = Delta_0_GL  # Approximate: use GL gap (tau-independent in 0D limit)
    E_qp = np.sqrt(eps_tau**2 + Delta**2)
    xi_over_E = eps_tau / E_qp
    t_k_tau = J_C2 * xi_over_E  # Use constant J_C2 for simplicity

    # Build Hamiltonians at this tau
    H_BCS_tau = build_H_BCS(eps_tau, eps_tau * 1.05, V_fold, V_fold)
    H_J_tau = build_H_Josephson(E_J_fold)  # approximate E_J
    H_A_tau = build_H_Andreev(t_k_tau)
    H_full_tau = H_BCS_tau + H_J_tau + H_A_tau

    evals_tau = eigh(H_full_tau, eigvals_only=True)
    r_tau, nr_tau = compute_gap_ratio(evals_tau)
    r_tau_sweep[it] = r_tau

    print(f"  tau={tau_val:.4f}: <r>={r_tau:.4f} (n={nr_tau})")

max_r_K2 = np.max(r_tau_sweep)
print(f"\nMax <r> in [0.08, 0.22]: {max_r_K2:.4f}")
print(f"K2 criterion (<r> > 0.48): {'PASS' if max_r_K2 > 0.48 else 'FAIL'}")


# ============================================================
# 10. RANDOM ANISOTROPY CONTROL
# ============================================================

print("\n" + "=" * 72)
print("CONTROL: Random anisotropy Andreev")
print("=" * 72)

# If the physical t_k give Poisson, does RANDOM t_k give GOE?
# This validates the diagnostic can detect chaos when present.
np.random.seed(42)
n_random_trials = 50
r_random = np.zeros(n_random_trials)

t_k_scale = np.std(np.abs(t_k_MF)) * 3  # scale ~ physical but random

for trial in range(n_random_trials):
    t_k_rand = np.random.uniform(-t_k_scale, t_k_scale, N_modes)
    H_A_rand = build_H_Andreev(t_k_rand)
    H_rand = H_base_asym + H_A_rand
    evals_rand = eigh(H_rand, eigvals_only=True)
    r_rand, _ = compute_gap_ratio(evals_rand)
    r_random[trial] = r_rand

print(f"Random t_k control (50 trials):")
print(f"  <r> mean = {np.mean(r_random):.4f}")
print(f"  <r> std  = {np.std(r_random):.4f}")
print(f"  <r> min  = {np.min(r_random):.4f}")
print(f"  <r> max  = {np.max(r_random):.4f}")
print(f"  Fraction with <r> > 0.48: {np.mean(r_random > 0.48):.2f}")


# ============================================================
# 11. Gate Verdict
# ============================================================

print("\n" + "=" * 72)
print("GATE VERDICT: ANDREEV-INTEG-57")
print("=" * 72)

# Use the asymmetric MF result at alpha=1.0 as canonical
r_canonical = r_physical_MF
if r_canonical < 0.40:
    verdict = "FAIL"
    detail = f"<r>={r_canonical:.4f} < 0.40 (Poisson persists, integrability preserved)"
elif r_canonical > 0.48:
    verdict = "PASS"
    detail = f"<r>={r_canonical:.4f} > 0.48 (integrability broken by Andreev channel)"
else:
    verdict = "INFO"
    detail = f"<r>={r_canonical:.4f} in [0.40, 0.48] (intermediate)"

print(f"Verdict: {verdict}")
print(f"Detail: {detail}")
print(f"Criterion: PASS >0.48, FAIL <0.40, INFO [0.40,0.48]")


# ============================================================
# 12. Save data
# ============================================================

print("\n" + "=" * 72)
print("SAVING DATA")
print("=" * 72)

save_path = os.path.join(data_dir, 's57_andreev_integ.npz')
np.savez(save_path,
    # Gate
    gate_name='ANDREEV-INTEG-57',
    gate_verdict=verdict,
    gate_detail=detail,
    r_canonical=r_canonical,

    # Alpha sweep
    alpha_values=alpha_values,
    r_means_sym_MF=r_means_MF,
    r_means_sym_ED=r_means_ED,
    r_means_asym_MF=r_means_asym_MF,
    r_means_asym_ED=r_means_asym_ED,
    n_ratios_MF=n_ratios_MF,
    n_ratios_ED=n_ratios_ED,

    # R-G commutators
    comm_norms_MF=comm_norms_MF,
    comm_norms_ED=comm_norms_ED,
    Q_norms=Q_norms,
    max_ratio_MF=max_ratio_MF,
    max_ratio_ED=max_ratio_ED,
    mean_ratio_MF=mean_ratio_MF,
    mean_ratio_ED=mean_ratio_ED,

    # SFF
    t_sff=t_sff,
    K_sff=K_sff,
    K_plateau=K_plateau,

    # OTOC
    t_otoc=t_otoc,
    C_otoc=C_otoc,
    lambda_L_fit=lambda_L_fit,
    beta_power=beta_power,
    R2_exp=R2_exp,
    R2_pow=R2_pow,
    C_max=C_max,

    # Tau sweep
    tau_sweep_vals=tau_sweep_vals,
    r_tau_sweep=r_tau_sweep,
    max_r_K2=max_r_K2,

    # Random control
    r_random_mean=np.mean(r_random),
    r_random_std=np.std(r_random),
    r_random_all=r_random,

    # Input echoes
    t_k_MF=t_k_MF,
    t_k_ED=t_k_ED,
    eps_fold=eps_fold,
    E_J_fold=E_J_fold,
    dim=dim,
)

print(f"Saved: {save_path}")


# ============================================================
# 13. Plot
# ============================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('ANDREEV-INTEG-57: Andreev Channel Integrability Test', fontsize=14, fontweight='bold')

# Panel 1: <r> vs alpha
ax = axes[0, 0]
ax.plot(alpha_values, r_means_asym_MF, 'b-o', label='Asym MF $t_k$', markersize=4)
ax.plot(alpha_values, r_means_asym_ED, 'r-s', label='Asym ED $t_k$', markersize=4)
ax.plot(alpha_values, r_means_MF, 'b--^', label='Sym MF $t_k$', markersize=3, alpha=0.5)
ax.axhline(y=0.3863, color='green', linestyle=':', linewidth=2, label='Poisson (0.386)')
ax.axhline(y=0.5307, color='red', linestyle=':', linewidth=2, label='GOE (0.531)')
ax.axhline(y=0.48, color='orange', linestyle='--', linewidth=1, label='PASS threshold')
ax.axhline(y=0.40, color='purple', linestyle='--', linewidth=1, label='FAIL threshold')
ax.set_xlabel(r'$\alpha$ (Andreev coupling)')
ax.set_ylabel(r'$\langle r \rangle$')
ax.set_title(r'Level spacing ratio vs Andreev strength')
ax.legend(fontsize=7, loc='upper right')
ax.set_ylim(0.1, 0.65)
ax.grid(True, alpha=0.3)

# Panel 2: SFF
ax = axes[0, 1]
ax.semilogy(t_sff, K_sff, 'b-', linewidth=0.5, alpha=0.7)
# Smooth with running average
window = 50  # (local)
if len(K_sff) > window:
    K_smooth = np.convolve(K_sff, np.ones(window)/window, mode='valid')
    t_smooth = np.convolve(t_sff, np.ones(window)/window, mode='valid')
    ax.semilogy(t_smooth, K_smooth, 'r-', linewidth=2, label='Smoothed')
ax.axhline(y=1.0, color='green', linestyle=':', label='Plateau (=1)')
ax.set_xlabel('$t$')
ax.set_ylabel('$K(t)$ (SFF)')
ax.set_title(f'Spectral Form Factor ($\\alpha=1.0$)')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 3: OTOC
ax = axes[1, 0]
ax.plot(t_otoc, C_otoc, 'b-', linewidth=1)
ax.set_xlabel('$t$ ($M_{KK}^{-1}$)')
ax.set_ylabel('$C(t)$')
ax.set_title(f'OTOC ($\\alpha=1.0$, asym cells)')
ax.grid(True, alpha=0.3)
# Inset with log scale if C grows
if C_max > 1e-10:
    # Add log-scale inset
    from mpl_toolkits.axes_grid1.inset_locator import inset_axes
    ax_in = inset_axes(ax, width="40%", height="40%", loc='upper right')
    pos_mask = C_otoc > 1e-12
    if np.sum(pos_mask) > 2:
        ax_in.semilogy(t_otoc[pos_mask], C_otoc[pos_mask], 'b-', linewidth=0.5)
        ax_in.set_xlabel('$t$', fontsize=7)
        ax_in.set_ylabel('$C(t)$', fontsize=7)
        ax_in.tick_params(labelsize=6)

# Panel 4: R-G commutator norms
ax = axes[1, 1]
ratio_MF_arr = comm_norms_MF / np.maximum(Q_norms, 1e-15)
ratio_ED_arr = comm_norms_ED / np.maximum(Q_norms, 1e-15)
x_modes = np.arange(len(Q_all))
labels = [f"Q{j%8}^c{1+j//8}" for j in range(len(Q_all))]
ax.bar(x_modes - 0.2, ratio_MF_arr, 0.4, label='MF $t_k$', color='blue', alpha=0.7)
ax.bar(x_modes + 0.2, ratio_ED_arr, 0.4, label='ED $t_k$', color='red', alpha=0.7)
ax.axhline(y=0.1, color='orange', linestyle='--', label='Breaking threshold (0.1)')
ax.set_xlabel('Conserved quantity index')
ax.set_ylabel(r'$\|[Q_j, H_A]\| / \|Q_j\|$')
ax.set_title('R-G Commutator Norms')
ax.legend(fontsize=8)
ax.set_xticks(x_modes[::2])
ax.set_xticklabels([labels[i] for i in range(0, len(labels), 2)], fontsize=6, rotation=45)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plot_path = os.path.join(data_dir, 's57_andreev_integ.png')
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"Saved plot: {plot_path}")

print("\nDONE")
