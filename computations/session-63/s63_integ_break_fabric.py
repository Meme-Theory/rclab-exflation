#!/usr/bin/env python3
"""
S63 INTEG-BREAK-FABRIC-63: Josephson Anisotropy and Integrability Breaking
on 32-cell CG(24) Fabric

Tests whether the anisotropic Josephson coupling from the CG(24) fabric
geometry breaks Richardson-Gaudin integrability.

Physics:
    - CG(24) has 93 edges with 3 bond types: C2 (50), su2 (24), u1 (19)
    - Each bond type has different hopping: J_C2=0.919, J_su2=0.060, J_u1=0.038
    - Per-edge E_J = J_type^2 * F_anom (anomalous density)
    - Isotropic B_1^dag B_2 preserves R-G integrability (S56 FABRIC-INTEG-56)
    - Anisotropic Josephson with mode-dependent J_{kl} breaks it
    - On the fabric, the INTER-CELL coupling is ALREADY anisotropic by bond type
    - The question: does the bond-type anisotropy translate to MODE-LEVEL
      anisotropy that breaks the intra-cell Richardson-Gaudin algebra?

Strategy:
    1. Compute per-edge E_J from J_type and anomalous density
    2. For a 2-cell pair connected by bond type t, the Josephson is
       H_J = -E_J(t)/2 * (B_1^dag B_2 + h.c.) -- STILL isotropic in mode space
    3. The fabric has cells with MULTIPLE neighbors of DIFFERENT types
    4. Effective single-cell Josephson from all neighbors:
       H_J_eff(cell i) = -sum_{j in nbr(i)} E_J(i,j)/2 * (B_i^dag B_j + h.c.)
    5. For integrability breaking: need MODE-DEPENDENT coupling within a cell
    6. Two sources: (a) quasiparticle tunneling (mode-dependent by E_k)
                    (b) virtual excitation corrections (second-order)

Gate: INTEG-BREAK-FABRIC-63
    INFO: anisotropy + Gamma computed
    Gamma > H_0: CC path opens (integrability breaking fast enough)
    Gamma < H_0: CC locked (integrability protected over cosmic time)

Author: Volovik Superfluid Universe Theorist (S63)
"""

import numpy as np
from scipy.linalg import eigh, eigvalsh
from itertools import combinations
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from canonical_constants import (
    tau_fold, E_cond, N_cells, Delta_0_OES, Delta_B3,
    J_C2 as J_C2_canon, J_su2 as J_su2_canon, J_u1 as J_u1_canon,
    H_0_GeV, M_KK, xi_BCS, xi_GL, omega_PV,
    E_B1, E_B2_mean, E_B3_mean, N_dof_BCS,
    hbar_GeV_s, t_universe_s, H_0_inv_s
)

# ============================================================
# 1. Load data
# ============================================================
data_dir = os.path.dirname(os.path.abspath(__file__))

tb_data = np.load(os.path.join(data_dir, 's54_tb_hamiltonian.npz'), allow_pickle=True)
ed_data = np.load(os.path.join(data_dir, 's54_ed_sweep.npz'), allow_pickle=True)
meissner_data = np.load(os.path.join(data_dir, 's62_meissner_gge.npz'), allow_pickle=True)
ba_data = np.load(os.path.join(data_dir, 's56_ba_spectrum.npz'), allow_pickle=True)

# Adjacency matrices by bond type
adj_C2 = tb_data['adj_C2'].astype(float)
adj_su2 = tb_data['adj_su2'].astype(float)
adj_u1 = tb_data['adj_u1'].astype(float)
adj_full = tb_data['adjacency'].astype(float)

# Hopping parameters at fold
fold_idx = int(ed_data['fold_idx'])  # = 19
J_C2_val = tb_data['J_C2_tau'][fold_idx]
J_su2_val = tb_data['J_su2_tau'][fold_idx]
J_u1_val = tb_data['J_u1_tau'][fold_idx]

# Single-particle energies at fold
E_sp = ed_data['E_sp_sweep']  # (50, 8)
eps_fold = E_sp[fold_idx].copy()

# Pairing interaction
V_bare = ed_data['V_bare_cont']  # (8, 8)

# GGE occupation numbers
n_k_GGE = meissner_data['n_k_GGE']

# E_J from s56 BA spectrum
E_J_full = ba_data['E_J'][fold_idx]  # 7.042 M_KK (full spectrum sum)

print("="*70)
print("INTEG-BREAK-FABRIC-63: Josephson Anisotropy on CG(24)")
print("="*70)
print(f"\nFold index: {fold_idx}, tau = {tau_fold}")
print(f"Single-particle energies at fold: {eps_fold}")
print(f"Hoppings: J_C2={J_C2_val:.6f}, J_su2={J_su2_val:.6f}, J_u1={J_u1_val:.6f} M_KK")
print(f"Hopping ratios: J_C2/J_su2={J_C2_val/J_su2_val:.1f}, J_C2/J_u1={J_C2_val/J_u1_val:.1f}")
print(f"E_J(fold, full) = {E_J_full:.4f} M_KK")
print(f"GGE occupations: {n_k_GGE}")

# ============================================================
# 2. Per-edge Josephson energy
# ============================================================
print("\n" + "="*70)
print("SECTION 2: Per-edge Josephson energies")
print("="*70)

# Anomalous density: F_anom = sum_k Delta / (2 * E_qp_k),
# where E_qp_k = sqrt(eps_k^2 + Delta^2)
Delta = Delta_0_OES

def compute_anomalous_density(eps, delta):
    """Compute anomalous density F = sum_k delta / (2 * E_k)."""
    E_qp = np.sqrt(eps**2 + delta**2)
    return np.sum(delta / (2.0 * E_qp))

F_anom = compute_anomalous_density(eps_fold, Delta)
print(f"Anomalous density F = {F_anom:.6f}")

# Per-edge E_J = J_type^2 * F_anom  (for identical cells)
E_J_C2 = J_C2_val**2 * F_anom
E_J_su2 = J_su2_val**2 * F_anom
E_J_u1 = J_u1_val**2 * F_anom

print(f"\nPer-bond-type Josephson energies:")
print(f"  E_J(C2)  = {J_C2_val:.6f}^2 * {F_anom:.6f} = {E_J_C2:.6f} M_KK")
print(f"  E_J(su2) = {J_su2_val:.6f}^2 * {F_anom:.6f} = {E_J_su2:.6f} M_KK")
print(f"  E_J(u1)  = {J_u1_val:.6f}^2 * {F_anom:.6f} = {E_J_u1:.6f} M_KK")

# Build per-edge E_J matrix
E_J_matrix = np.zeros((32, 32))
for i in range(32):
    for j in range(i+1, 32):
        if adj_C2[i, j] > 0:
            E_J_matrix[i, j] = E_J_C2
            E_J_matrix[j, i] = E_J_C2
        elif adj_su2[i, j] > 0:
            E_J_matrix[i, j] = E_J_su2
            E_J_matrix[j, i] = E_J_su2
        elif adj_u1[i, j] > 0:
            E_J_matrix[i, j] = E_J_u1
            E_J_matrix[j, i] = E_J_u1

# Collect all nonzero edge values
edge_EJs = []
edge_types = []
for i in range(32):
    for j in range(i+1, 32):
        if adj_full[i, j] > 0:
            edge_EJs.append(E_J_matrix[i, j])
            if adj_C2[i, j] > 0:
                edge_types.append('C2')
            elif adj_su2[i, j] > 0:
                edge_types.append('su2')
            else:
                edge_types.append('u1')

edge_EJs = np.array(edge_EJs)
n_edges = len(edge_EJs)

print(f"\nTotal edges: {n_edges}")
print(f"  C2 bonds:  {edge_types.count('C2')} with E_J = {E_J_C2:.6f}")
print(f"  su2 bonds: {edge_types.count('su2')} with E_J = {E_J_su2:.6f}")
print(f"  u1 bonds:  {edge_types.count('u1')} with E_J = {E_J_u1:.6f}")

# Anisotropy measures
E_J_mean = np.mean(edge_EJs)
E_J_max = np.max(edge_EJs)
E_J_min = np.min(edge_EJs)
E_J_std = np.std(edge_EJs)

delta_J = (E_J_max - E_J_min) / E_J_mean
delta_J_std = E_J_std / E_J_mean

print(f"\nEdge E_J statistics:")
print(f"  Mean:  {E_J_mean:.6f} M_KK")
print(f"  Max:   {E_J_max:.6f} M_KK (C2)")
print(f"  Min:   {E_J_min:.6f} M_KK (u1)")
print(f"  Std:   {E_J_std:.6f} M_KK")
print(f"  Anisotropy delta_J = (max-min)/mean = {delta_J:.4f}")
print(f"  Relative std delta_J_std = std/mean = {delta_J_std:.4f}")

# ============================================================
# 3. Per-cell effective Josephson environment
# ============================================================
print("\n" + "="*70)
print("SECTION 3: Per-cell Josephson environment")
print("="*70)

# Each cell sees a total Josephson energy from all its neighbors
# E_J_total(i) = sum_j E_J(i,j)
# The composition of neighbors (fraction C2 vs su2 vs u1) varies by cell

E_J_total_per_cell = np.zeros(32)
n_C2_per_cell = np.zeros(32, dtype=int)
n_su2_per_cell = np.zeros(32, dtype=int)
n_u1_per_cell = np.zeros(32, dtype=int)

for i in range(32):
    for j in range(32):
        if adj_C2[i, j] > 0:
            n_C2_per_cell[i] += 1
            E_J_total_per_cell[i] += E_J_C2
        if adj_su2[i, j] > 0:
            n_su2_per_cell[i] += 1
            E_J_total_per_cell[i] += E_J_su2
        if adj_u1[i, j] > 0:
            n_u1_per_cell[i] += 1
            E_J_total_per_cell[i] += E_J_u1

degree = (adj_full.sum(axis=1)).astype(int)

print(f"Cell connectivity and E_J_total:")
print(f"{'Cell':>4} {'deg':>3} {'nC2':>3} {'nsu2':>4} {'nu1':>3} {'E_J_tot':>10} {'frac_C2':>8}")
for i in range(32):
    frac_C2 = n_C2_per_cell[i] / max(degree[i], 1)
    print(f"{i:4d} {degree[i]:3d} {n_C2_per_cell[i]:3d} {n_su2_per_cell[i]:4d} {n_u1_per_cell[i]:3d} "
          f"{E_J_total_per_cell[i]:10.4f} {frac_C2:8.3f}")

print(f"\nE_J_total per cell:")
print(f"  Mean: {E_J_total_per_cell.mean():.4f} M_KK")
print(f"  Std:  {E_J_total_per_cell.std():.4f} M_KK")
print(f"  Min:  {E_J_total_per_cell.min():.4f} M_KK (cell {E_J_total_per_cell.argmin()})")
print(f"  Max:  {E_J_total_per_cell.max():.4f} M_KK (cell {E_J_total_per_cell.argmax()})")

cell_aniso = (E_J_total_per_cell.max() - E_J_total_per_cell.min()) / E_J_total_per_cell.mean()
print(f"  Cell-level anisotropy: {cell_aniso:.4f}")

# ============================================================
# 4. Richardson-Gaudin commutator analysis
# ============================================================
print("\n" + "="*70)
print("SECTION 4: Richardson-Gaudin Commutator [H_J, R_k]")
print("="*70)

# The Richardson-Gaudin conserved charges for BCS with N_modes modes are:
#   R_k = s_k^z + 2*g * sum_{l!=k} [s_k^+ s_l^- + s_k^z s_l^z] / (eps_k - eps_l)
# where s_k^+ = b_k^dag (pair creation), s_k^- = b_k (pair annihilation),
# s_k^z = (n_k - 1/2).
#
# CRITICAL STRUCTURAL POINT:
# The Josephson coupling H_J = -E_J/2 * (B_i^dag B_j + h.c.) where B_i = sum_k b_k^(i)
# is ISOTROPIC in mode space within each cell. This means:
#   [H_J_iso, R_k^(i)] ~ sum_l [b_l^(j), R_k^(i)] = 0 (different cells)
# because R_k^(i) only involves operators from cell i.
#
# S56 proved: isotropic Josephson PRESERVES integrability.
#
# For integrability BREAKING, we need MODE-DEPENDENT inter-cell coupling.
# Two physical sources:
#
# Source A: Quasiparticle tunneling (Andreev channel)
#   H_QP = -sum_k t_k * (c_{k,sigma}^(1)dag c_{k,sigma}^(2) + h.c.)
#   where t_k depends on the mode energy through the BCS coherence factors:
#   t_k = J * (u_k^(1) u_k^(2) + v_k^(1) v_k^(2))
#   This is INTRINSICALLY mode-dependent -> breaks R-G
#
# Source B: Second-order virtual processes
#   A pair hops to neighbor, partner undergoes mode-changing scattering,
#   pair returns. Effective coupling: J_eff^{kl} ~ E_J^2 * f(eps_k, eps_l) / Delta
#   This is mode-dependent by construction -> breaks R-G

# Compute BCS coherence factors
u_k = np.sqrt(0.5 * (1.0 + eps_fold / np.sqrt(eps_fold**2 + Delta**2)))
v_k = np.sqrt(0.5 * (1.0 - eps_fold / np.sqrt(eps_fold**2 + Delta**2)))

print(f"BCS coherence factors:")
print(f"  u_k = {u_k}")
print(f"  v_k = {v_k}")

# Source A: Quasiparticle tunneling amplitude (mode-dependent)
# For Andreev tunneling between identical cells:
# t_k_Andreev = J_type * (u_k^2 - v_k^2) = J_type * eps_k / E_qp_k
# (normal reflection channel)
# t_k_pair = J_type * 2 * u_k * v_k = J_type * Delta / E_qp_k
# (Andreev reflection = pair transfer channel, this is the mode-dependent piece)

E_qp = np.sqrt(eps_fold**2 + Delta**2)

# Andreev reflection amplitude per mode (pair transfer)
t_k_pair_C2 = J_C2_val * Delta / E_qp
t_k_pair_su2 = J_su2_val * Delta / E_qp
t_k_pair_u1 = J_u1_val * Delta / E_qp

print(f"\nAndreev pair-transfer amplitude per mode (C2 bond):")
for k in range(8):
    print(f"  k={k}: t_pair = {t_k_pair_C2[k]:.6f}, E_qp = {E_qp[k]:.6f}")

# The mode-dependent deviation from isotropic:
# delta_t_k = t_k - <t> where <t> = (1/N_modes) * sum_k t_k
t_mean_C2 = np.mean(t_k_pair_C2)
delta_t_C2 = t_k_pair_C2 - t_mean_C2
mode_aniso_C2 = np.std(t_k_pair_C2) / t_mean_C2

print(f"\nMode-level anisotropy in pair transfer (C2):")
print(f"  <t_pair> = {t_mean_C2:.6f}")
print(f"  delta_t = {delta_t_C2}")
print(f"  mode anisotropy = std/mean = {mode_aniso_C2:.4f}")

# Normal tunneling amplitude per mode
t_k_normal_C2 = J_C2_val * eps_fold / E_qp
mode_aniso_normal = np.std(t_k_normal_C2) / (np.mean(np.abs(t_k_normal_C2)) + 1e-30)

print(f"\nNormal tunneling amplitude per mode (C2):")
for k in range(8):
    print(f"  k={k}: t_normal = {t_k_normal_C2[k]:.6f}")
print(f"  mode anisotropy (normal) = {mode_aniso_normal:.4f}")

# ============================================================
# 5. Integrability-breaking Hamiltonian
# ============================================================
print("\n" + "="*70)
print("SECTION 5: Integrability-Breaking Hamiltonian")
print("="*70)

# The integrability-breaking part of H_J is the MODE-DEPENDENT piece.
# Write H_J = H_J_iso + H_J_aniso where:
#   H_J_iso = -E_J/2 * B_i^dag B_j  (preserves R-G)
#   H_J_aniso = -sum_k (delta_J_k/2) * b_k^(i)dag b_k^(j)  (breaks R-G)
#
# For quasiparticle tunneling, the total inter-cell Hamiltonian is:
#   H_inter = sum_k [t_k^pair * b_k^(i)dag b_k^(j)] + [t_k^normal * ...]
#
# The pair transfer channel gives: J_{kl} = delta_{kl} * t_k^pair
# which is diagonal in mode index but MODE-DEPENDENT.
#
# Decompose: t_k^pair = <t^pair> + delta_t_k
# The <t^pair> part = isotropic Josephson (integrable)
# The delta_t_k part = integrability-breaking perturbation V_break

# Strength of integrability breaking per bond type
V_break_C2 = np.sum(delta_t_C2**2)  # ||delta_t||^2
V_break_su2_arr = J_su2_val * Delta / E_qp
delta_t_su2 = V_break_su2_arr - np.mean(V_break_su2_arr)
V_break_su2 = np.sum(delta_t_su2**2)

V_break_u1_arr = J_u1_val * Delta / E_qp
delta_t_u1 = V_break_u1_arr - np.mean(V_break_u1_arr)
V_break_u1 = np.sum(delta_t_u1**2)

print(f"Integrability-breaking strength ||delta_t||^2:")
print(f"  C2:  {V_break_C2:.6e}")
print(f"  su2: {V_break_su2:.6e}")
print(f"  u1:  {V_break_u1:.6e}")

# The TOTAL integrability breaking per cell sums over all neighbors
# V_break_total(i) = sum_{j in nbr(i)} ||delta_t(i,j)||^2
# But since delta_t is proportional to J_type, and the mode-dependence
# comes from 1/E_qp_k structure, all bond types have the SAME normalized
# mode anisotropy. The breaking strength scales as J_type^2.

# Total breaking Hamiltonian matrix element (rms)
# For a single bond of type t:
V_rms_C2 = np.sqrt(V_break_C2 / N_dof_BCS)
V_rms_su2 = np.sqrt(V_break_su2 / N_dof_BCS)
V_rms_u1 = np.sqrt(V_break_u1 / N_dof_BCS)

print(f"\nRMS breaking matrix element per mode:")
print(f"  V_rms(C2)  = {V_rms_C2:.6e} M_KK")
print(f"  V_rms(su2) = {V_rms_su2:.6e} M_KK")
print(f"  V_rms(u1)  = {V_rms_u1:.6e} M_KK")

# ============================================================
# 6. Second-order virtual process (Source B)
# ============================================================
print("\n" + "="*70)
print("SECTION 6: Second-Order Virtual Integrability Breaking")
print("="*70)

# A Cooper pair hops from cell 1 to cell 2, undergoes intra-cell scattering
# in cell 2 (mode k -> mode l), then hops back. This generates an effective
# mode-changing coupling:
#   J_eff^{kl} = E_J^2 * V_{kl} / (Delta_pair^2)
# where Delta_pair is the virtual intermediate state energy cost.
#
# For the intermediate state: pair is in cell 2 mode m, no pair in cell 1 mode k
# Energy cost ~ 2*Delta (creating a quasiparticle pair)
#
# This gives J_eff^{kl} ~ E_J^2 * V_{kl} / (4*Delta^2)

# Using the full pairing matrix V_bare
Delta_sq = Delta**2

J_eff_2nd = np.zeros((N_dof_BCS, N_dof_BCS))
for k in range(N_dof_BCS):
    for l in range(N_dof_BCS):
        if k != l:
            # Second-order virtual: pair hops out of k, scatters to l, hops back
            # Intermediate energy ~ E_qp[k] + E_qp[l]
            denom = E_qp[k] + E_qp[l]
            J_eff_2nd[k, l] = E_J_C2 * V_bare[k, l] * E_J_C2 / denom

print(f"Second-order effective mode-changing coupling (C2 bond):")
J_eff_max = np.max(np.abs(J_eff_2nd))
J_eff_rms = np.sqrt(np.mean(J_eff_2nd[J_eff_2nd != 0]**2))
print(f"  Max |J_eff^{{kl}}| = {J_eff_max:.6e} M_KK")
print(f"  RMS J_eff = {J_eff_rms:.6e} M_KK")
print(f"  Ratio to E_J(C2): {J_eff_max / E_J_C2:.6e}")

# The mode-dependent part of second-order:
J_eff_diag = np.array([np.sum(J_eff_2nd[k, :]) for k in range(N_dof_BCS)])
J_eff_diag_mean = np.mean(J_eff_diag)
delta_J_eff = J_eff_diag - J_eff_diag_mean
V_break_2nd = np.sum(delta_J_eff**2)

print(f"\n  Diagonal self-energy shift per mode:")
for k in range(N_dof_BCS):
    print(f"    k={k}: J_eff_diag = {J_eff_diag[k]:.6e}")
print(f"  Mean: {J_eff_diag_mean:.6e}")
print(f"  ||delta_J_eff||^2 = {V_break_2nd:.6e}")

# ============================================================
# 7. Exact 2-cell level statistics with anisotropic tunneling
# ============================================================
print("\n" + "="*70)
print("SECTION 7: Exact 2-Cell Level Statistics")
print("="*70)

# Build 2-cell Hilbert space (same as S56)
N_modes = 8  # (local)
N_pair_total = 2  # (local)
basis = list(combinations(range(2 * N_modes), N_pair_total))
dim = len(basis)
basis_dict = {state: idx for idx, state in enumerate(basis)}

def build_H_2cell_aniso(eps_1, eps_2, V_1, V_2, t_pair, alpha):
    """
    Build 2-cell BCS Hamiltonian with MODE-DEPENDENT Josephson.

    t_pair: (N_modes,) per-mode pair transfer amplitude.
    Instead of E_J * B_1^dag B_2 (isotropic), use sum_k t_pair[k] * b_k^(1)dag b_k^(2).
    """
    H = np.zeros((dim, dim))

    for i, state_i in enumerate(basis):
        # Diagonal: kinetic
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

            H[i, i] -= V_cell[k_local, k_local]

            for l_local in range(N_modes):
                l = l_local + offset
                if l == k or l in state_i:
                    continue
                new_state = list(state_i)
                new_state[pos] = l
                new_state = tuple(sorted(new_state))
                if new_state in basis_dict:
                    j = basis_dict[new_state]
                    H[i, j] -= V_cell[l_local, k_local]

        # Anisotropic Josephson: mode-dependent pair transfer
        if alpha > 0:
            for pos, k in enumerate(state_i):
                if k >= N_modes:
                    # Pair in cell 2, mode k_local -> transfer to cell 1
                    k_local = k - N_modes
                    for l_local_1 in range(N_modes):
                        l = l_local_1
                        if l in state_i:
                            continue
                        new_state = list(state_i)
                        new_state[pos] = l
                        new_state = tuple(sorted(new_state))
                        if new_state in basis_dict:
                            j = basis_dict[new_state]
                            # MODE-DEPENDENT: different amplitude for each k_local <-> l_local pair
                            # For pair transfer: b_l^(1)dag b_k^(2) with amplitude t_pair[k_local]
                            # (mode in the source cell determines tunneling rate)
                            H[i, j] -= alpha * t_pair[k_local] / 2.0

                elif k < N_modes:
                    # Pair in cell 1, mode k_local -> transfer to cell 2
                    k_local = k
                    for l_local_2 in range(N_modes):
                        l = l_local_2 + N_modes
                        if l in state_i:
                            continue
                        new_state = list(state_i)
                        new_state[pos] = l
                        new_state = tuple(sorted(new_state))
                        if new_state in basis_dict:
                            j = basis_dict[new_state]
                            H[i, j] -= alpha * t_pair[k_local] / 2.0

    H = (H + H.T) / 2.0
    return H


def compute_gap_ratio(eigenvalues):
    """Mean adjacent gap ratio <r>."""
    E = np.sort(eigenvalues)
    spacings = np.diff(E)
    mean_spacing = np.mean(spacings)
    mask = spacings > 1e-10 * mean_spacing
    spacings_clean = spacings[mask]
    if len(spacings_clean) < 10:
        return np.nan, 0
    n = len(spacings_clean)
    start = n // 10
    end = n - n // 10
    s = spacings_clean[start:end]
    r_vals = []
    for i in range(len(s) - 1):
        r = min(s[i], s[i+1]) / max(s[i], s[i+1])
        r_vals.append(r)
    return np.mean(r_vals), len(r_vals)


# Test 1: Isotropic Josephson (control, should reproduce S56)
t_pair_iso = np.ones(N_modes) * np.mean(t_k_pair_C2)
H_iso = build_H_2cell_aniso(eps_fold, eps_fold, V_bare, V_bare, t_pair_iso, alpha=1.0)
eigs_iso = eigvalsh(H_iso)
r_iso, n_iso = compute_gap_ratio(eigs_iso)
print(f"Control (isotropic): <r> = {r_iso:.4f} (n={n_iso}) [expect ~0.37 = Poisson]")

# Test 2: Physical mode-dependent tunneling (C2 bond)
H_aniso_C2 = build_H_2cell_aniso(eps_fold, eps_fold, V_bare, V_bare, t_k_pair_C2, alpha=1.0)
eigs_aniso_C2 = eigvalsh(H_aniso_C2)
r_aniso_C2, n_aniso_C2 = compute_gap_ratio(eigs_aniso_C2)
print(f"Aniso (C2 pair-transfer): <r> = {r_aniso_C2:.4f} (n={n_aniso_C2})")

# Test 3: Including normal tunneling as well
t_k_total_C2 = np.sqrt(t_k_pair_C2**2 + t_k_normal_C2**2)  # total tunneling amplitude
H_total_C2 = build_H_2cell_aniso(eps_fold, eps_fold, V_bare, V_bare, t_k_total_C2, alpha=1.0)
eigs_total_C2 = eigvalsh(H_total_C2)
r_total_C2, n_total_C2 = compute_gap_ratio(eigs_total_C2)
print(f"Total tunneling (C2): <r> = {r_total_C2:.4f} (n={n_total_C2})")

# Test 4: Random control (should give GOE)
np.random.seed(42)
t_random = np.random.uniform(0.1, 1.0, N_modes) * np.mean(t_k_pair_C2)
H_random = build_H_2cell_aniso(eps_fold, eps_fold, V_bare, V_bare, t_random, alpha=1.0)
eigs_random = eigvalsh(H_random)
r_random, n_random = compute_gap_ratio(eigs_random)
print(f"Random control: <r> = {r_random:.4f} (n={n_random}) [expect ~0.53 = GOE]")

# Test 5: Asymmetric cells (different eps) -- physical on fabric
# Cells with different local environments have shifted eps
eps_shifted = eps_fold * 1.05  # 5% perturbation as proxy for cell asymmetry
H_asym = build_H_2cell_aniso(eps_fold, eps_shifted, V_bare, V_bare, t_k_pair_C2, alpha=1.0)
eigs_asym = eigvalsh(H_asym)
r_asym, n_asym = compute_gap_ratio(eigs_asym)
print(f"Asym cells + aniso J (C2): <r> = {r_asym:.4f} (n={n_asym})")

# Test 6: Sweep anisotropy strength
# Interpolate between isotropic and physical anisotropic
print(f"\nAnisotropy sweep (C2 bond):")
lambdas = np.linspace(0, 1, 11)
r_sweep = []
for lam in lambdas:
    t_interp = (1 - lam) * t_pair_iso + lam * t_k_pair_C2
    H_lam = build_H_2cell_aniso(eps_fold, eps_fold, V_bare, V_bare, t_interp, alpha=1.0)
    eigs_lam = eigvalsh(H_lam)
    r_lam, _ = compute_gap_ratio(eigs_lam)
    r_sweep.append(r_lam)
    print(f"  lambda={lam:.1f}: <r> = {r_lam:.4f}")
r_sweep = np.array(r_sweep)

# ============================================================
# 8. Commutator norm ||[H_J_aniso, R_k]||
# ============================================================
print("\n" + "="*70)
print("SECTION 8: Commutator Norm")
print("="*70)

# The commutator [H_J_aniso, R_k] measures how strongly the integrability-breaking
# perturbation V_break fails to commute with the conserved charges.
#
# For the Richardson-Gaudin algebra, the conserved charges are:
#   R_k = tau_k^z + g * sum_{l!=k} (tau_k . tau_l) / (eps_k - eps_l)
# where tau_k are the SU(2) pseudo-spin operators for pair k.
#
# In the pair basis, we can construct these matrices directly.
# For N=1 pair system (single cell), the R_k are 8x8 matrices.

def build_rg_charges(eps, g_coupling):
    """
    Build Richardson-Gaudin conserved charges for N_modes with N_pair=1.

    R_k = s_k^z + 2*g * sum_{l!=k} (s_k^+ s_l^- + s_k^z s_l^z) / (eps_k - eps_l)

    In the 1-pair sector, basis is |k> (pair in mode k), dim = N_modes.
    s_k^z |l> = (delta_{kl} - 1/2) |l>   [but for 1-pair: +1/2 if occupied, -1/2 if empty]
    Actually for 1 pair in N modes:
        s_k^z |l> = +1/2 |l> if k=l, -1/2 |l> if k!=l
        s_k^+ s_l^- |m> = delta_{lm} |k> (transfer pair from l to k)
        s_k^z s_l^z |m> = (+/-1/2)*(+/-1/2) |m>
    """
    N = len(eps)
    charges = []

    for k in range(N):
        R = np.zeros((N, N))

        # s_k^z part
        for m in range(N):
            if m == k:
                R[m, m] += 0.5
            else:
                R[m, m] -= 0.5

        # Interaction part: 2*g * sum_{l!=k}
        for l in range(N):
            if l == k:
                continue
            denom = eps[k] - eps[l]
            if abs(denom) < 1e-15:
                continue

            # s_k^+ s_l^- term: creates pair in k, destroys in l
            # <k| s_k^+ s_l^- |l> = 1, <m| s_k^+ s_l^- |l> = 0 for m!=k
            R[k, l] += 2.0 * g_coupling / denom

            # s_k^z s_l^z term:
            # <m| s_k^z s_l^z |m>
            for m in range(N):
                sz_k = 0.5 if m == k else -0.5
                sz_l = 0.5 if m == l else -0.5
                R[m, m] += 2.0 * g_coupling * sz_k * sz_l / denom

        charges.append(R)

    return charges

# BCS coupling constant g from the pairing matrix
# In R-G model: H_BCS = sum_k 2*eps_k s_k^z - g * sum_{kl} b_k^dag b_l
# g = -V_bare[0,1] (typical off-diagonal)
g_coupling = -V_bare[0, 1]  # use representative coupling
print(f"R-G coupling constant g = {g_coupling:.6f}")

# Build R-G charges for single cell (N_pair=1, N_modes=8)
rg_charges = build_rg_charges(eps_fold, g_coupling)

# Check: charges should commute with H_BCS
# H_BCS in 1-pair sector: H_{kl} = 2*eps_k delta_{kl} - V_{kl}
H_BCS_1pair = np.diag(2 * eps_fold) - V_bare
print(f"\nVerification: [H_BCS, R_k] norms:")
for k in range(N_dof_BCS):
    comm = H_BCS_1pair @ rg_charges[k] - rg_charges[k] @ H_BCS_1pair
    norm = np.linalg.norm(comm)
    print(f"  ||[H_BCS, R_{k}]|| = {norm:.2e}")

# Now build the integrability-breaking perturbation in 1-pair sector
# V_break in mode space: transfer pair from l to k with amplitude delta_t[l]
# <k| V_break |l> = delta_t[l] for k != l (pair transfer with mode-dependent weight)
V_break_matrix = np.zeros((N_dof_BCS, N_dof_BCS))
for k in range(N_dof_BCS):
    for l in range(N_dof_BCS):
        if k != l:
            V_break_matrix[k, l] = delta_t_C2[l]  # mode-dependent Josephson deviation

print(f"\nIntegrability-breaking commutator norms:")
comm_norms = []
for k in range(N_dof_BCS):
    comm = V_break_matrix @ rg_charges[k] - rg_charges[k] @ V_break_matrix
    norm = np.linalg.norm(comm)
    comm_norms.append(norm)
    print(f"  ||[V_break, R_{k}]|| = {norm:.6e}")

mean_comm_norm = np.mean(comm_norms)
max_comm_norm = np.max(comm_norms)
print(f"\n  Mean: {mean_comm_norm:.6e}")
print(f"  Max:  {max_comm_norm:.6e}")

# Ratio to mean level spacing
mean_level_spacing = np.mean(np.diff(np.sort(eigvalsh(H_BCS_1pair))))
ratio_comm = max_comm_norm / mean_level_spacing
print(f"  Mean level spacing: {mean_level_spacing:.6e}")
print(f"  Max ||[V,R]|| / mean_spacing = {ratio_comm:.4f}")

# ============================================================
# 9. Fermi Golden Rule decay rate
# ============================================================
print("\n" + "="*70)
print("SECTION 9: Fermi Golden Rule Decay Rate")
print("="*70)

# The integrability-breaking perturbation V_break causes transitions between
# R-G eigenstates, with rate given by Fermi's golden rule:
#
# Gamma_k = (2*pi/hbar) * |<f|V_break|i>|^2 * rho(E)
#
# where rho(E) is the density of final states at the transition energy.
#
# For a single cell with 8 modes and 1 pair:
# Mean level spacing: delta_E ~ BW/N_modes where BW is total bandwidth
# rho(E) ~ 1/delta_E = N_modes/BW

# Bandwidth of single-cell spectrum
E_BCS_1pair = eigvalsh(H_BCS_1pair)
BW_1pair = E_BCS_1pair[-1] - E_BCS_1pair[0]
delta_E = BW_1pair / N_dof_BCS
rho_E = 1.0 / delta_E

print(f"Single-cell BCS (1-pair sector):")
print(f"  Eigenvalues: {E_BCS_1pair}")
print(f"  Bandwidth: {BW_1pair:.6f} M_KK")
print(f"  Mean spacing: {delta_E:.6f} M_KK")
print(f"  DOS: {rho_E:.4f} M_KK^{{-1}}")

# Matrix elements of V_break between BCS eigenstates
eigvecs_BCS = eigh(H_BCS_1pair)[1]
V_break_eigen = eigvecs_BCS.T @ V_break_matrix @ eigvecs_BCS
V_break_offdiag = V_break_eigen.copy()
np.fill_diagonal(V_break_offdiag, 0)

V2_mean = np.mean(V_break_offdiag**2)
V2_max = np.max(V_break_offdiag**2)

print(f"\nV_break in BCS eigenbasis:")
print(f"  <|V_ij|^2> = {V2_mean:.6e}")
print(f"  max |V_ij|^2 = {V2_max:.6e}")

# FGR rate (in M_KK units, hbar=1 in natural units)
Gamma_FGR = 2 * np.pi * V2_mean * rho_E
Gamma_FGR_max = 2 * np.pi * V2_max * rho_E

print(f"\nFermi golden rule rate:")
print(f"  Gamma_FGR (mean) = {Gamma_FGR:.6e} M_KK")
print(f"  Gamma_FGR (max)  = {Gamma_FGR_max:.6e} M_KK")

# Convert to physical units
# M_KK = 7.43e16 GeV
Gamma_FGR_GeV = Gamma_FGR * M_KK  # GeV
Gamma_FGR_inv_s = Gamma_FGR_GeV / hbar_GeV_s  # s^{-1}

print(f"\nIn physical units:")
print(f"  Gamma = {Gamma_FGR_GeV:.4e} GeV")
print(f"  Gamma = {Gamma_FGR_inv_s:.4e} s^{{-1}}")
print(f"  H_0 = {H_0_inv_s:.4e} s^{{-1}}")
print(f"  Gamma / H_0 = {Gamma_FGR_inv_s / H_0_inv_s:.4e}")

# Timescale comparison
t_integ = 1.0 / Gamma_FGR_inv_s if Gamma_FGR_inv_s > 0 else np.inf
print(f"\n  t_integ = {t_integ:.4e} s")
print(f"  t_universe = {t_universe_s:.4e} s")
print(f"  t_integ / t_universe = {t_integ / t_universe_s:.4e}")

# ============================================================
# 10. Multi-cell enhancement on CG(24)
# ============================================================
print("\n" + "="*70)
print("SECTION 10: Multi-Cell Enhancement on CG(24)")
print("="*70)

# On the full 32-cell fabric, each cell has z_i neighbors.
# The total integrability-breaking rate is enhanced by:
# 1. Number of neighbors (each contributes independently)
# 2. The variance of E_J across neighbors (mixed bond types)
# 3. Correlated many-body effects

# Enhancement factor 1: Coordination sum
# Gamma_fabric(i) = sum_{j in nbr(i)} Gamma_FGR(type(i,j))
Gamma_per_type = {
    'C2': 2 * np.pi * np.mean((eigvecs_BCS.T @ np.zeros_like(V_break_matrix) @ eigvecs_BCS)**2) * rho_E,
    'su2': 0.0,
    'u1': 0.0
}

# Recompute for each bond type
for bond_type, J_val in [('C2', J_C2_val), ('su2', J_su2_val), ('u1', J_u1_val)]:
    t_pair_type = J_val * Delta / E_qp
    t_mean_type = np.mean(t_pair_type)
    delta_t_type = t_pair_type - t_mean_type

    V_type = np.zeros((N_dof_BCS, N_dof_BCS))
    for k in range(N_dof_BCS):
        for l in range(N_dof_BCS):
            if k != l:
                V_type[k, l] = delta_t_type[l]

    V_type_eigen = eigvecs_BCS.T @ V_type @ eigvecs_BCS
    V_type_offdiag = V_type_eigen.copy()
    np.fill_diagonal(V_type_offdiag, 0)
    V2_type = np.mean(V_type_offdiag**2)
    Gamma_per_type[bond_type] = 2 * np.pi * V2_type * rho_E

print(f"Gamma per bond type:")
for bt, g in Gamma_per_type.items():
    print(f"  Gamma({bt}) = {g:.6e} M_KK")

# Total per cell
Gamma_per_cell = np.zeros(32)
for i in range(32):
    for j in range(32):
        if adj_C2[i, j] > 0:
            Gamma_per_cell[i] += Gamma_per_type['C2']
        if adj_su2[i, j] > 0:
            Gamma_per_cell[i] += Gamma_per_type['su2']
        if adj_u1[i, j] > 0:
            Gamma_per_cell[i] += Gamma_per_type['u1']

print(f"\nGamma per cell (M_KK):")
print(f"  Mean: {Gamma_per_cell.mean():.6e}")
print(f"  Min:  {Gamma_per_cell.min():.6e} (cell {Gamma_per_cell.argmin()})")
print(f"  Max:  {Gamma_per_cell.max():.6e} (cell {Gamma_per_cell.argmax()})")

# Enhancement from multi-neighbor effects
# Additional: the VARIANCE in E_J across neighbors of a single cell
# creates effective disorder that further breaks integrability
for i in [0, 3, 6, 21]:  # sample cells with different coordination
    nbr_EJs = []
    for j in range(32):
        if adj_full[i, j] > 0:
            nbr_EJs.append(E_J_matrix[i, j])
    nbr_EJs = np.array(nbr_EJs)
    if len(nbr_EJs) > 1:
        cv = np.std(nbr_EJs) / np.mean(nbr_EJs)
    else:
        cv = 0
    print(f"  Cell {i} (deg={degree[i]}): E_J neighbors = {nbr_EJs}, CV = {cv:.3f}")

# Fabric-averaged rate
Gamma_fabric = Gamma_per_cell.mean()
Gamma_fabric_GeV = Gamma_fabric * M_KK
Gamma_fabric_inv_s = Gamma_fabric_GeV / hbar_GeV_s

print(f"\nFabric-averaged integrability-breaking rate:")
print(f"  Gamma_fabric = {Gamma_fabric:.6e} M_KK")
print(f"  Gamma_fabric = {Gamma_fabric_GeV:.4e} GeV")
print(f"  Gamma_fabric = {Gamma_fabric_inv_s:.4e} s^{{-1}}")
print(f"  Gamma_fabric / H_0 = {Gamma_fabric_inv_s / H_0_inv_s:.4e}")

# ============================================================
# 11. Including second-order processes in Gamma
# ============================================================
print("\n" + "="*70)
print("SECTION 11: Combined Rate (First + Second Order)")
print("="*70)

# Second-order V_break matrix elements in eigenbasis
J_eff_eigen = eigvecs_BCS.T @ J_eff_2nd @ eigvecs_BCS
J_eff_offdiag = J_eff_eigen.copy()
np.fill_diagonal(J_eff_offdiag, 0)
V2_2nd = np.mean(J_eff_offdiag**2)

Gamma_2nd = 2 * np.pi * V2_2nd * rho_E
print(f"Second-order FGR rate:")
print(f"  <|V_2nd|^2> = {V2_2nd:.6e}")
print(f"  Gamma_2nd = {Gamma_2nd:.6e} M_KK")

# Combined (incoherent sum)
Gamma_total_per_bond = Gamma_FGR + Gamma_2nd
print(f"\nCombined per-bond rate (C2):")
print(f"  Gamma_total = {Gamma_total_per_bond:.6e} M_KK")
print(f"  Ratio 2nd/1st = {Gamma_2nd / (Gamma_FGR + 1e-30):.4f}")

# Fabric total with both processes
Gamma_fabric_total = Gamma_fabric + 32 * np.mean([Gamma_2nd]) * np.mean(degree) / 32
Gamma_fabric_total_GeV = Gamma_fabric_total * M_KK
Gamma_fabric_total_inv_s = Gamma_fabric_total_GeV / hbar_GeV_s

print(f"\nFabric total (all processes):")
print(f"  Gamma = {Gamma_fabric_total:.6e} M_KK")
print(f"  Gamma = {Gamma_fabric_total_inv_s:.4e} s^{{-1}}")
print(f"  Gamma / H_0 = {Gamma_fabric_total_inv_s / H_0_inv_s:.4e}")

# ============================================================
# 12. Key diagnostic: WHY the mode-level anisotropy is weak
# ============================================================
print("\n" + "="*70)
print("SECTION 12: Structural Analysis of Mode-Level Anisotropy")
print("="*70)

# The critical insight from the superfluid 3He analog:
# In a superfluid Josephson junction, the pair transfer operator B_1^dag B_2
# is the SUM over all modes. Its mode-dependence comes only from the
# BCS coherence factors u_k, v_k.
#
# For the BCS ground state (all pairs in condensate mode):
#   u_k ~ 1 for eps_k >> Delta (empty modes)
#   v_k ~ 1 for eps_k << Delta (occupied modes)
#   u_k ~ v_k ~ 1/sqrt(2) for eps_k ~ Delta
#
# The pair transfer amplitude t_k = Delta / E_qp_k varies SMOOTHLY with k.
# The variation is bounded: t_k in [Delta/E_max, 1] where E_max is the
# largest quasiparticle energy.

print(f"Mode-resolved pair transfer (C2 bond):")
print(f"{'k':>3} {'eps_k':>10} {'E_qp_k':>10} {'t_pair':>10} {'delta_t':>10} {'delta_t/t':>10}")
for k in range(N_dof_BCS):
    print(f"{k:3d} {eps_fold[k]:10.6f} {E_qp[k]:10.6f} {t_k_pair_C2[k]:10.6f} "
          f"{delta_t_C2[k]:10.6f} {delta_t_C2[k]/t_k_pair_C2[k]:10.4f}")

# The anisotropy is bounded by the ratio E_qp_max / E_qp_min
E_qp_ratio = E_qp[-1] / E_qp[0]
t_ratio = t_k_pair_C2[0] / t_k_pair_C2[-1]  # max/min since 1/E_qp
print(f"\nE_qp_max / E_qp_min = {E_qp_ratio:.4f}")
print(f"t_max / t_min = {t_ratio:.4f}")
print(f"Bound on mode anisotropy: {(t_ratio - 1) / (t_ratio + 1):.4f}")

# STRUCTURAL RESULT: The mode anisotropy is O(1) because the BCS coherence
# factors ARE mode-dependent. But it is a SMOOTH function of eps_k, not random.
# The question is whether this smooth mode-dependence breaks integrability
# as effectively as random mode-dependence.

# Compare: random mode-dependence strength needed for GOE
# From S56: random J gave <r> = 0.446. What strength?
print(f"\nLevel statistics summary:")
print(f"  Isotropic Josephson:    <r> = {r_iso:.4f} (Poisson: 0.386)")
print(f"  Physical aniso (C2):    <r> = {r_aniso_C2:.4f}")
print(f"  Total tunneling (C2):   <r> = {r_total_C2:.4f}")
print(f"  Asym cells + aniso:     <r> = {r_asym:.4f}")
print(f"  Random control:         <r> = {r_random:.4f} (GOE: 0.531)")
print(f"  GOE threshold:          <r> > 0.48")
print(f"  Poisson threshold:      <r> < 0.40")

# ============================================================
# 13. Gate verdict
# ============================================================
print("\n" + "="*70)
print("SECTION 13: Gate Verdict")
print("="*70)

gate_verdict = "INFO"
# Decisive criterion: Gamma vs H_0
if Gamma_fabric_total_inv_s > H_0_inv_s:
    cc_path = "OPEN"
    detail = f"Gamma = {Gamma_fabric_total_inv_s:.2e} s^-1 > H_0 = {H_0_inv_s:.2e} s^-1"
else:
    cc_path = "LOCKED"
    detail = f"Gamma = {Gamma_fabric_total_inv_s:.2e} s^-1 < H_0 = {H_0_inv_s:.2e} s^-1"

# Key discriminant: is <r> in GOE regime?
if r_aniso_C2 > 0.48:
    integ_status = "BROKEN (GOE)"
elif r_aniso_C2 > 0.40:
    integ_status = "TRANSITION"
else:
    integ_status = "PRESERVED (Poisson)"

gate_detail = (
    f"INTEG-BREAK-FABRIC-63: {gate_verdict}\n"
    f"  delta_J (edge aniso) = {delta_J:.4f}\n"
    f"  Mode anisotropy = {mode_aniso_C2:.4f}\n"
    f"  <r>(iso) = {r_iso:.4f}, <r>(aniso C2) = {r_aniso_C2:.4f}\n"
    f"  Integrability: {integ_status}\n"
    f"  Gamma_fabric = {Gamma_fabric_total_inv_s:.2e} s^-1\n"
    f"  H_0 = {H_0_inv_s:.2e} s^-1\n"
    f"  Gamma/H_0 = {Gamma_fabric_total_inv_s / H_0_inv_s:.2e}\n"
    f"  CC path: {cc_path}\n"
    f"  {detail}"
)

print(gate_detail)
print(f"\n  GATE VERDICT: {gate_verdict}")
print(f"  CC PATH: {cc_path}")

# ============================================================
# 14. Save data
# ============================================================
print("\n" + "="*70)
print("Saving data...")
print("="*70)

np.savez(os.path.join(data_dir, 's63_integ_break_fabric.npz'),
    # Gate
    gate_name='INTEG-BREAK-FABRIC-63',
    gate_verdict=gate_verdict,
    gate_detail=gate_detail,
    cc_path=cc_path,

    # Edge anisotropy
    edge_EJs=edge_EJs,
    edge_types=np.array(edge_types),
    E_J_C2=E_J_C2,
    E_J_su2=E_J_su2,
    E_J_u1=E_J_u1,
    E_J_mean=E_J_mean,
    delta_J=delta_J,
    delta_J_std=delta_J_std,

    # Cell anisotropy
    E_J_total_per_cell=E_J_total_per_cell,
    cell_aniso=cell_aniso,
    n_C2_per_cell=n_C2_per_cell,
    n_su2_per_cell=n_su2_per_cell,
    n_u1_per_cell=n_u1_per_cell,

    # Mode-level anisotropy
    mode_aniso_C2=mode_aniso_C2,
    t_k_pair_C2=t_k_pair_C2,
    delta_t_C2=delta_t_C2,
    u_k=u_k,
    v_k=v_k,
    E_qp=E_qp,

    # Level statistics
    r_iso=r_iso,
    r_aniso_C2=r_aniso_C2,
    r_total_C2=r_total_C2,
    r_asym=r_asym,
    r_random=r_random,
    r_sweep=r_sweep,
    lambdas=lambdas,

    # Commutator norms
    comm_norms=np.array(comm_norms),
    mean_comm_norm=mean_comm_norm,
    max_comm_norm=max_comm_norm,

    # FGR rates
    Gamma_FGR=Gamma_FGR,
    Gamma_FGR_max=Gamma_FGR_max,
    Gamma_2nd=Gamma_2nd,
    Gamma_per_type_C2=Gamma_per_type['C2'],
    Gamma_per_type_su2=Gamma_per_type['su2'],
    Gamma_per_type_u1=Gamma_per_type['u1'],
    Gamma_per_cell=Gamma_per_cell,
    Gamma_fabric_total=Gamma_fabric_total,
    Gamma_fabric_total_inv_s=Gamma_fabric_total_inv_s,
    Gamma_over_H0=Gamma_fabric_total_inv_s / H_0_inv_s,

    # Second-order
    J_eff_2nd=J_eff_2nd,
    V_break_2nd=V_break_2nd,

    # Reference values
    F_anom=F_anom,
    E_J_full=E_J_full,
    Delta=Delta,
    eps_fold=eps_fold,
)

print("Saved: s63_integ_break_fabric.npz")

# ============================================================
# 15. Plot
# ============================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: Edge E_J distribution
ax = axes[0, 0]
bins_C2 = [E_J_C2 - 0.01, E_J_C2 + 0.01]
bins_su2 = [E_J_su2 - 0.001, E_J_su2 + 0.001]
bins_u1 = [E_J_u1 - 0.001, E_J_u1 + 0.001]
ax.bar(['C2\n(50 bonds)', 'su2\n(24 bonds)', 'u1\n(19 bonds)'],
       [E_J_C2, E_J_su2, E_J_u1],
       color=['steelblue', 'coral', 'forestgreen'], alpha=0.8)
ax.set_ylabel('E_J per bond (M_KK)')
ax.set_title(f'Per-Bond-Type Josephson Energy\ndelta_J = {delta_J:.3f}')
ax.axhline(E_J_mean, color='k', ls='--', label=f'mean = {E_J_mean:.4f}')
ax.legend()

# Panel 2: Anisotropy sweep
ax = axes[0, 1]
ax.plot(lambdas, r_sweep, 'o-', color='steelblue', markersize=6)
ax.axhline(0.386, color='green', ls='--', label='Poisson (0.386)')
ax.axhline(0.531, color='red', ls='--', label='GOE (0.531)')
ax.axhline(0.40, color='orange', ls=':', label='FAIL threshold')
ax.axhline(0.48, color='purple', ls=':', label='PASS threshold')
ax.set_xlabel('Anisotropy parameter lambda')
ax.set_ylabel('<r> (gap ratio)')
ax.set_title('Level Statistics vs Mode Anisotropy')
ax.legend(fontsize=8)

# Panel 3: Mode-resolved pair transfer
ax = axes[1, 0]
k_indices = np.arange(N_dof_BCS)
ax.bar(k_indices - 0.15, t_k_pair_C2, width=0.3, label='t_pair(C2)', color='steelblue', alpha=0.8)
ax.bar(k_indices + 0.15, np.abs(t_k_normal_C2), width=0.3, label='|t_normal(C2)|', color='coral', alpha=0.8)
ax.axhline(t_mean_C2, color='k', ls='--', label=f'<t_pair> = {t_mean_C2:.4f}')
ax.set_xlabel('Mode index k')
ax.set_ylabel('Tunneling amplitude (M_KK)')
ax.set_title(f'Mode-Resolved Tunneling\naniso = {mode_aniso_C2:.3f}')
ax.legend(fontsize=8)

# Panel 4: Commutator norms
ax = axes[1, 1]
ax.bar(k_indices, comm_norms, color='steelblue', alpha=0.8)
ax.set_xlabel('R-G charge index k')
ax.set_ylabel('||[V_break, R_k]||')
ax.set_title(f'Integrability-Breaking Commutators\nmax = {max_comm_norm:.2e}')

plt.suptitle(f'INTEG-BREAK-FABRIC-63: {gate_verdict} | CC {cc_path}',
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(os.path.join(data_dir, 's63_integ_break_fabric.png'), dpi=150, bbox_inches='tight')
print("Saved: s63_integ_break_fabric.png")

print("\n" + "="*70)
print("COMPUTATION COMPLETE")
print("="*70)
