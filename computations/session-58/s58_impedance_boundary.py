#!/usr/bin/env python3
"""
S58 IMPEDANCE-BOUNDARY-58: Acoustic impedance at domain boundaries.

Computes acoustic impedance Z = rho * c_BA for isolated cells and C2-connected
bonds, then derives reflection R and transmission T at domain boundaries.

The resonance question: Does the 32-cell fabric trap phonons or transmit them?
In any acoustic system, the answer lives in the impedance mismatch.

Gate: IMPEDANCE-BOUNDARY-58 (INFO)
  Criterion: T > 0.5 (transparent) or T < 0.5 (trapped)?

Input:
  - s56_ba_spectrum.npz: BA sound speeds c_BA(tau), E_J(tau), E_c(tau)
  - s54_tb_hamiltonian.npz: graph structure, adjacency, cell properties
  - s57_percolation_cc.npz: per-bond Josephson energies, percolation data

Output:
  - s58_impedance_boundary.npz
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from canonical_constants import (
    tau_fold, N_cells, Delta_0_OES, omega_att
)

# ============================================================================
#  Load input data
# ============================================================================

ba = np.load('computations/session-56/s56_ba_spectrum.npz', allow_pickle=True)
tb = np.load('computations/session-54/s54_tb_hamiltonian.npz', allow_pickle=True)
perc = np.load('computations/session-57/s57_percolation_cc.npz', allow_pickle=True)

tau_values = ba['tau_values']   # (50,)
N_tau = len(tau_values)
c_BA = ba['c_BA']               # (50,) sound speed per tau
E_J_total = ba['E_J']           # (50,) total Josephson energy
E_c = ba['E_c']                 # (50,) charging energy
omega_BA = ba['omega_BA']       # (50, 31) BA mode spectrum

adj_C2 = tb['adj_C2']           # (32, 32) C2 adjacency
cell_dims = tb['cell_dims']     # (32,) dimension of each SU(3) irrep
cell_casimirs = tb['cell_casimirs']  # (32,) Casimir of each cell
eigenvalues = tb['eigenvalues']  # (50, 32) TB eigenvalues
J_C2_tau = tb['J_C2_tau']       # (50,) C2 hopping amplitude

E_J_C2 = perc['E_J_C2']         # (50,) Josephson energy per C2 bond
E_J_su2 = perc['E_J_su2']       # (50,) per su2 bond
n_active_C2 = perc['n_active_C2']  # (50,) active C2 bonds
n_domains = perc['n_domains']    # (50,) domain count

# ============================================================================
#  Cell impedance: Z_cell = rho_cell * c_cell
# ============================================================================
#
# The "density" (inertia) of a cell in the tight-binding language is the
# number of internal DOF: dim(p,q). This is the condensed-matter analog of
# mass density -- how much "stuff" resists acceleration by the sound wave.
#
# The sound speed c_BA is defined as the group velocity of the acoustic branch
# at k -> 0. In the BA model, this is a collective property depending on the
# full Josephson network, so c_BA(tau) is a scalar (single acoustic branch).
#
# For per-cell impedance, we use each cell's LOCAL sound speed contribution.
# On a lattice, the local sound speed at cell i is related to the nearest-
# neighbor hopping: c_i ~ sqrt(E_J_eff / m_i) where m_i ~ dim_i.
# But we also have the collective c_BA from the BA model.
#
# Strategy: compute TWO impedance measures.
#
# (A) Homogeneous: All cells share the BA sound speed (collective).
#     Z_cell(tau) = dim_i * c_BA(tau). Impedance mismatch from DOF only.
#
# (B) Local: Each cell has effective speed c_i = sqrt(sum_j J_ij / dim_i).
#     Z_cell_i(tau) = dim_i * c_i(tau). Full heterogeneity.

# --- Method A: Homogeneous sound speed ---
# Z_cell_i(tau) = dim_i * c_BA(tau)
Z_cell_hom = np.outer(cell_dims, c_BA)  # (32, 50)

# --- Method B: Local sound speed ---
# For cell i, effective spring constant K_i = sum_j adj_C2[i,j] * J_C2(tau)
#   (only C2 bonds are coherent in the relevant tau range)
# c_i = sqrt(K_i / dim_i)
# Z_i = dim_i * c_i = dim_i * sqrt(K_i / dim_i) = sqrt(dim_i * K_i)

n_C2_neighbors = np.sum(adj_C2, axis=1)  # (32,) number of C2 neighbors per cell
# K_i(tau) = n_neighbors_C2[i] * J_C2(tau)
K_local = np.outer(n_C2_neighbors, J_C2_tau)  # (32, 50)
c_local = np.sqrt(K_local / cell_dims[:, None])  # (32, 50)
Z_cell_local = cell_dims[:, None] * c_local  # (32, 50)

# ============================================================================
#  Bond impedance: Z_bond = rho_bond * c_bond
# ============================================================================
#
# A bond between cells i and j has an effective impedance. The standard
# acoustic impedance matching formula at a junction uses the geometric
# mean of the cell impedances for the "bond" impedance:
#
#   Z_bond_ij = sqrt(Z_i * Z_j)  (series combination / geometric mean)
#
# But the physical impedance of the tunneling link itself is set by the
# Josephson coupling: the bond transmits phonons with amplitude J_C2(tau)
# and its effective inertia is the reduced DOF: mu_ij = dim_i*dim_j/(dim_i+dim_j).
#
# Z_bond_ij(tau) = mu_ij * sqrt(J_C2(tau) / mu_ij) = sqrt(mu_ij * J_C2(tau))

# Find all C2 bond pairs
bond_pairs = []
for i in range(N_cells):
    for j in range(i+1, N_cells):
        if adj_C2[i, j]:
            bond_pairs.append((i, j))
bond_pairs = np.array(bond_pairs)  # (n_bonds, 2)
n_bonds = len(bond_pairs)
print(f"N_cells = {N_cells}, n_C2_bonds = {n_bonds}")

# Reduced mass for each bond
dim_i = cell_dims[bond_pairs[:, 0]]  # (n_bonds,)
dim_j = cell_dims[bond_pairs[:, 1]]  # (n_bonds,)
mu_bond = (dim_i * dim_j) / (dim_i + dim_j)  # (n_bonds,)

# Z_bond(tau) = sqrt(mu_ij * J_C2(tau))
Z_bond = np.sqrt(mu_bond[:, None] * J_C2_tau[None, :])  # (n_bonds, 50)

# ============================================================================
#  Reflection and Transmission at each bond
# ============================================================================
#
# For each bond (i,j), the mismatch is between the larger-impedance cell
# (source) and the bond (channel):
#
#   R_ij = (Z_max - Z_bond) / (Z_max + Z_bond)
#   T_ij = 1 - R_ij^2
#
# We also compute the cell-cell reflection using Method B (local impedance):
#   R_cell_ij = (Z_i - Z_j) / (Z_i + Z_j)
#   T_cell_ij = 1 - R_cell_ij^2

# Method A: Cell vs Bond
Z_i_hom = Z_cell_hom[bond_pairs[:, 0], :].T  # (50, n_bonds)
Z_j_hom = Z_cell_hom[bond_pairs[:, 1], :].T  # (50, n_bonds)
Z_max_hom = np.maximum(Z_i_hom, Z_j_hom)     # (50, n_bonds)
Z_min_hom = np.minimum(Z_i_hom, Z_j_hom)     # (50, n_bonds)

# Cell-cell reflection (homogeneous c_BA)
R_cell_hom = (Z_max_hom - Z_min_hom) / (Z_max_hom + Z_min_hom + 1e-30)  # (50, n_bonds)
T_cell_hom = 1.0 - R_cell_hom**2  # (50, n_bonds)

# Method B: Local impedance
Z_i_loc = Z_cell_local[bond_pairs[:, 0], :].T  # (50, n_bonds)
Z_j_loc = Z_cell_local[bond_pairs[:, 1], :].T  # (50, n_bonds)

R_cell_loc = np.abs(Z_i_loc - Z_j_loc) / (Z_i_loc + Z_j_loc + 1e-30)  # (50, n_bonds)
T_cell_loc = 1.0 - R_cell_loc**2  # (50, n_bonds)

# Cell vs Bond (Method A)
Z_bond_T = Z_bond.T  # (50, n_bonds)
Z_cell_mean_hom = 0.5 * (Z_i_hom + Z_j_hom)  # (50, n_bonds)
R_bond_hom = np.abs(Z_cell_mean_hom - Z_bond_T) / (Z_cell_mean_hom + Z_bond_T + 1e-30)
T_bond_hom = 1.0 - R_bond_hom**2

# ============================================================================
#  Statistics over bonds at each tau
# ============================================================================

# Cell-cell (Method A: homogeneous c)
R_cc_mean = np.mean(R_cell_hom, axis=1)   # (50,)
R_cc_std = np.std(R_cell_hom, axis=1)
T_cc_mean = np.mean(T_cell_hom, axis=1)
T_cc_std = np.std(T_cell_hom, axis=1)
T_cc_min = np.min(T_cell_hom, axis=1)
T_cc_max = np.max(T_cell_hom, axis=1)

# Cell-cell (Method B: local c)
R_loc_mean = np.mean(R_cell_loc, axis=1)
R_loc_std = np.std(R_cell_loc, axis=1)
T_loc_mean = np.mean(T_cell_loc, axis=1)
T_loc_std = np.std(T_cell_loc, axis=1)
T_loc_min = np.min(T_cell_loc, axis=1)
T_loc_max = np.max(T_cell_loc, axis=1)

# Cell-bond (Method A)
R_cb_mean = np.mean(R_bond_hom, axis=1)
R_cb_std = np.std(R_bond_hom, axis=1)
T_cb_mean = np.mean(T_bond_hom, axis=1)
T_cb_std = np.std(T_bond_hom, axis=1)

# ============================================================================
#  Select 20 tau values spanning reconnection for reporting
# ============================================================================

# Reconnection happens around tau ~ 0.1-0.5 (percolation threshold).
# Select 20 evenly-spaced indices from the 50 available.
idx_20 = np.linspace(0, N_tau - 1, 20, dtype=int)
tau_20 = tau_values[idx_20]

# ============================================================================
#  Gate verdict
# ============================================================================

fold_idx = np.argmin(np.abs(tau_values - tau_fold))

# Method A: homogeneous -- impedance mismatch from DOF asymmetry alone
T_fold_cc = T_cc_mean[fold_idx]
T_fold_min_cc = T_cc_min[fold_idx]

# Method B: local -- full heterogeneity
T_fold_loc = T_loc_mean[fold_idx]
T_fold_min_loc = T_loc_min[fold_idx]

# Method A: cell-bond
T_fold_cb = T_cb_mean[fold_idx]

# Report the dominant physical quantity: T_cell_cell (local) at fold
T_gate = T_fold_loc
verdict = "TRANSPARENT" if T_gate > 0.5 else "TRAPPED"
gate_status = "INFO"

print(f"\n{'='*70}")
print(f"IMPEDANCE-BOUNDARY-58 GATE")
print(f"{'='*70}")
print(f"Method A (homogeneous c_BA):")
print(f"  <R_cell-cell> at fold = {R_cc_mean[fold_idx]:.4f} +/- {R_cc_std[fold_idx]:.4f}")
print(f"  <T_cell-cell> at fold = {T_fold_cc:.4f} (min={T_fold_min_cc:.4f}, max={T_cc_max[fold_idx]:.4f})")
print(f"  <T_cell-bond> at fold = {T_fold_cb:.4f}")
print(f"")
print(f"Method B (local c_i):")
print(f"  <R_cell-cell> at fold = {R_loc_mean[fold_idx]:.4f} +/- {R_loc_std[fold_idx]:.4f}")
print(f"  <T_cell-cell> at fold = {T_fold_loc:.4f} (min={T_fold_min_loc:.4f}, max={T_loc_max[fold_idx]:.4f})")
print(f"")
print(f"Gate verdict: {verdict} (T_local = {T_gate:.4f}, threshold 0.5)")
print(f"{'='*70}")

# Print table at 20 tau points
print(f"\n{'tau':>6s} | {'<T_hom>':>8s} | {'T_hom_min':>9s} | {'<T_loc>':>8s} | {'T_loc_min':>9s} | {'<R_loc>':>8s} | {'domains':>7s}")
print("-" * 72)
for k in idx_20:
    print(f"{tau_values[k]:6.3f} | {T_cc_mean[k]:8.4f} | {T_cc_min[k]:9.4f} | {T_loc_mean[k]:8.4f} | {T_loc_min[k]:9.4f} | {R_loc_mean[k]:8.4f} | {n_domains[k]:7d}")

# ============================================================================
#  Impedance ratio analysis: what drives the mismatch?
# ============================================================================

# For cell-cell (local), the mismatch is dominated by the DOF ratio.
# Z_i/Z_j = sqrt(dim_i * K_i) / sqrt(dim_j * K_j).
# If all cells have same n_C2_neighbors, then Z_i/Z_j = sqrt(dim_i/dim_j).
# Max DOF ratio: 81/1 = 81, so max Z ratio ~ 9.

dim_ratio_max = cell_dims.max() / cell_dims.min()
Z_ratio_max_dof = np.sqrt(dim_ratio_max)
print(f"\nDOF ratio max: {dim_ratio_max:.0f} (cells {cell_dims.max()}/{cell_dims.min()})")
print(f"Z ratio from DOF alone: {Z_ratio_max_dof:.2f}")

# Actual Z ratios at fold
Z_ratios_fold = Z_i_loc[fold_idx, :] / (Z_j_loc[fold_idx, :] + 1e-30)
Z_ratios_fold = np.where(Z_ratios_fold > 1, Z_ratios_fold, 1.0/Z_ratios_fold)
print(f"Actual Z ratio range at fold: [{Z_ratios_fold.min():.3f}, {Z_ratios_fold.max():.3f}]")
print(f"Actual Z ratio mean at fold: {Z_ratios_fold.mean():.3f}")

# The key question: does the impedance mismatch change during reconnection?
# At low tau (C2 coherent, one domain): all bonds active, impedance set by DOF
# At fold (fragmented): bonds still exist but cells are isolated
# At high tau (su2 reconnection): new topology

# ============================================================================
#  Frequency-dependent transmission
# ============================================================================
#
# The above is the low-frequency (long-wavelength) limit.
# At finite frequency omega, the transmission through a barrier of width d is:
#   T(omega) = 1 / (1 + (R/(1-R^2))^2 * sin^2(omega*d/c_bond))
#
# The characteristic frequency is c_BA / lattice_spacing.
# On the graph, lattice_spacing ~ 1 (in graph units).
# So T varies on scale omega ~ c_BA.

omega_char = c_BA  # characteristic frequency scale
print(f"\nCharacteristic frequency (c_BA) at fold: {c_BA[fold_idx]:.4f}")
print(f"omega_BA range at fold: [{omega_BA[fold_idx,0]:.4f}, {omega_BA[fold_idx,-1]:.4f}]")
print(f"Most BA modes are at omega > c_BA: frequency-dependent effects moderate")

# ============================================================================
#  Save data
# ============================================================================

np.savez('computations/session-58/s58_impedance_boundary.npz',
    tau_values=tau_values,
    tau_20=tau_20,
    idx_20=idx_20,

    # Cell impedances
    Z_cell_hom=Z_cell_hom,       # (32, 50)
    Z_cell_local=Z_cell_local,   # (32, 50)
    c_local=c_local,             # (32, 50) per-cell sound speed

    # Bond impedances
    Z_bond=Z_bond,               # (n_bonds, 50)
    bond_pairs=bond_pairs,       # (n_bonds, 2)
    mu_bond=mu_bond,             # (n_bonds,)

    # Reflection/Transmission statistics
    R_cc_mean=R_cc_mean, R_cc_std=R_cc_std,
    T_cc_mean=T_cc_mean, T_cc_std=T_cc_std,
    T_cc_min=T_cc_min, T_cc_max=T_cc_max,

    R_loc_mean=R_loc_mean, R_loc_std=R_loc_std,
    T_loc_mean=T_loc_mean, T_loc_std=T_loc_std,
    T_loc_min=T_loc_min, T_loc_max=T_loc_max,

    R_cb_mean=R_cb_mean, R_cb_std=R_cb_std,
    T_cb_mean=T_cb_mean, T_cb_std=T_cb_std,

    # Gate
    gate_name='IMPEDANCE-BOUNDARY-58',
    gate_verdict=gate_status,
    gate_detail=f'T_loc(fold)={T_gate:.4f}, {verdict}. DOF ratio max={dim_ratio_max:.0f}. '
                f'T range at fold: [{T_fold_min_loc:.4f}, {T_loc_max[fold_idx]:.4f}]. '
                f'50 C2 bonds on 32-cell graph.',
    n_bonds_C2=n_bonds,
    n_domains=n_domains,
    fold_idx=fold_idx,
)

print(f"\nSaved: computations/session-58/s58_impedance_boundary.npz")

# ============================================================================
#  Plot
# ============================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('IMPEDANCE-BOUNDARY-58: Acoustic Impedance at Domain Boundaries', fontsize=13)

# Panel 1: Transmission vs tau (all methods)
ax = axes[0, 0]
ax.fill_between(tau_values, T_cc_min, T_cc_max, alpha=0.15, color='C0')
ax.plot(tau_values, T_cc_mean, 'C0-', lw=2, label='$\\langle T \\rangle$ hom (cell-cell)')
ax.fill_between(tau_values, T_loc_min, T_loc_max, alpha=0.15, color='C1')
ax.plot(tau_values, T_loc_mean, 'C1-', lw=2, label='$\\langle T \\rangle$ local (cell-cell)')
ax.plot(tau_values, T_cb_mean, 'C2--', lw=1.5, label='$\\langle T \\rangle$ cell-bond')
ax.axhline(0.5, color='k', ls=':', lw=1, alpha=0.5, label='T = 0.5 threshold')
ax.axvline(tau_fold, color='gray', ls='--', lw=1, alpha=0.7, label=f'fold ($\\tau$={tau_fold})')
ax.set_xlabel('$\\tau$')
ax.set_ylabel('Transmission $T$')
ax.set_title('Transmission across C2 bonds')
ax.legend(fontsize=8, loc='lower left')
ax.set_ylim(-0.05, 1.05)
ax.grid(True, alpha=0.3)

# Panel 2: Reflection vs tau
ax = axes[0, 1]
ax.plot(tau_values, R_cc_mean, 'C0-', lw=2, label='$\\langle R \\rangle$ hom')
ax.fill_between(tau_values, R_cc_mean - R_cc_std, R_cc_mean + R_cc_std, alpha=0.2, color='C0')
ax.plot(tau_values, R_loc_mean, 'C1-', lw=2, label='$\\langle R \\rangle$ local')
ax.fill_between(tau_values, R_loc_mean - R_loc_std, R_loc_mean + R_loc_std, alpha=0.2, color='C1')
ax.axvline(tau_fold, color='gray', ls='--', lw=1, alpha=0.7)
ax.set_xlabel('$\\tau$')
ax.set_ylabel('Reflection $R$')
ax.set_title('Reflection coefficient')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel 3: Impedance Z for selected cells vs tau
ax = axes[1, 0]
selected_cells = [0, 1, 5, 10, 20, 30, 31]  # range of DOF
for ic in selected_cells:
    ax.plot(tau_values, Z_cell_local[ic, :], lw=1.5,
            label=f'Cell {ic} (dim={cell_dims[ic]})')
ax.axvline(tau_fold, color='gray', ls='--', lw=1, alpha=0.7)
ax.set_xlabel('$\\tau$')
ax.set_ylabel('$Z_{cell}$ (local)')
ax.set_title('Cell impedance by DOF')
ax.legend(fontsize=7, ncol=2)
ax.grid(True, alpha=0.3)

# Panel 4: Domains + transmission
ax = axes[1, 1]
ax2 = ax.twinx()
ax.plot(tau_values, n_domains, 'C3-', lw=2, label='Domains')
ax.set_ylabel('Number of domains', color='C3')
ax.tick_params(axis='y', labelcolor='C3')
ax2.plot(tau_values, T_loc_mean, 'C1-', lw=2, label='$\\langle T \\rangle$ local')
ax2.set_ylabel('$\\langle T \\rangle$ local', color='C1')
ax2.tick_params(axis='y', labelcolor='C1')
ax.axvline(tau_fold, color='gray', ls='--', lw=1, alpha=0.7, label=f'fold')
ax.set_xlabel('$\\tau$')
ax.set_title('Domains vs Transmission')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('computations/session-58/s58_impedance_boundary.png', dpi=150)
plt.close()
print("Saved: computations/session-58/s58_impedance_boundary.png")
print("\nDone.")
