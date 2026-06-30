#!/usr/bin/env python3
"""
s54_ed_sweep.py — Richardson Ground State E_0(tau) via Exact Diagonalization
=============================================================================
Session 54, W1-1: ED-SWEEP-54

Computes the exact ground state energy E_0(tau) of the BCS Hamiltonian at
N_pair=1 via exact diagonalization in the 8-mode pair space, at 50 tau  # (local)
values across [0.00, 0.50], using the 32-cell lattice Hamiltonian spectrum.

TWO parallel approaches (Strutinsky philosophy):
  A) LATTICE-V: Project Kosmann pairing from cell basis onto lattice eigenmodes.
     Geometrically honest but pairing diluted by delocalization over 32 cells.
  B) HYBRID (Strutinsky): Lattice single-particle energies + continuum V_bare.
     Captures correct pairing strength. This is the standard nuclear DFT approach:
     shell structure from the lattice, pairing from fitted interaction.

Physics (Paper 02, Dobaczewski; Paper 03, Bogoliubov; Paper 08, pairing collapse):
For N_pair=1 in 8 modes: canonical subspace dim = C(8,1) = 8.
The full 256-state Fock space captures all N sectors simultaneously.

Gate: ED-SWEEP-54
  PASS: V_eff = V_KK + E_0 has a local minimum near the fold
  FAIL: V_eff monotone or only has maxima

Author: nazarewicz-nuclear-structure-theorist, Session 54
Date: 2026-03-21
"""

import numpy as np
from scipy.integrate import trapezoid
from pathlib import Path
import sys
import time

sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import (
    tau_fold, E_cond, E_cond_ED_8mode,
    E_B1, E_B2_mean, E_B3_mean,
    Delta_0_GL, M_max_thouless, N_dof_BCS,
    a0_fold, a2_fold, a4_fold,
    S_fold, d2S_fold, dS_fold,
    J_C2, J_su2, J_u1,
)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

data_dir = Path(__file__).parent
archive_dir = Path(__file__).parent.parent / 'computations/_shared'
t_start = time.time()

N_MODES = 8  # (local)
N_FOCK = 2**N_MODES  # 256
N_PAIR_TARGET = 1

THRESHOLD_CONTINUUM = 63.2  # |d2V_KK/dtau2| from S53 W3-7  # (local)

print("=" * 78)
print("ED-SWEEP-54: Richardson Ground State E_0(tau) on 32-Cell Lattice")
print("=" * 78)

# ============================================================================
# Section 1: Load Data
# ============================================================================

print("\n--- Section 1: Loading Data ---")

d_tb = np.load(data_dir / 's54_tb_hamiltonian.npz', allow_pickle=True)
tau_values = d_tb['tau_values']       # (50,)
eigenvalues = d_tb['eigenvalues']     # (50, 32)
eigenvectors = d_tb['eigenvectors']   # (50, 32, 32)
cell_labels = d_tb['cell_labels']     # (32, 2)
cell_casimirs = d_tb['cell_casimirs'] # (32,)
adj_C2 = d_tb['adj_C2']              # (32, 32)
adj_su2 = d_tb['adj_su2']
adj_u1 = d_tb['adj_u1']

N_tau = len(tau_values)
N_cells = eigenvalues.shape[1]
fold_idx = np.argmin(np.abs(tau_values - tau_fold))

# Load continuum V_bare from S48
d48 = np.load(archive_dir / 's48_hfb_selfconsist.npz', allow_pickle=True)
V_bare_cont = d48['V_bare'].copy()  # 8x8 continuum sector basis
E_sp_cont = d48['E_sp'].copy()

print(f"Loaded {N_tau} tau in [{tau_values[0]:.3f}, {tau_values[-1]:.3f}]")
print(f"Lattice: {N_cells} cells, fold at tau[{fold_idx}]={tau_values[fold_idx]:.4f}")
print(f"Continuum V_bare norm: {np.linalg.norm(V_bare_cont):.6f}")

# ============================================================================
# Section 2: Construct Pairing Interactions
# ============================================================================

print("\n--- Section 2: Pairing Interactions ---")

# Method A: Lattice-projected V from cell-basis Kosmann kernel
# The Kosmann kernel on the 32-cell lattice is:
# V^{cell}_{mn} = g_K * sum_a |<R_m|K_a|R_n>|^2
# This is nonzero only when R_m tensor R_n contains the adjoint.
# Equivalently: cells connected by C^2 bonds can scatter pairs.
# The adjacency matrix encodes this CG structure.

# Construct V_cell from adjacency with Kosmann normalization.
# Normalize so that V(B2,B2) matches the continuum at the fold.
# Continuum V(B2,B2) ~ 0.039 (sector-averaged off-diagonal).
# B2 cells: (1,0) and (0,1), which are cells 1 and 2.
# adj_C2[1,2] should be 1 (they're CG-connected via (1,0)x(0,1) -> (1,1)+(0,0)).

print(f"adj_C2 between B2 cells (1,0)-(0,1): {adj_C2[1,2]}")
print(f"adj_C2 between B1-B2 cells (0,0)-(1,0): {adj_C2[0,1]}")
print(f"adj_C2 between B1-B2 cells (0,0)-(0,1): {adj_C2[0,2]}")

# Use weighted adjacency as pairing kernel.
# V^{cell} = g_K * (w_C2 * adj_C2 + w_su2 * adj_su2 + w_u1 * adj_u1)
# Weights from the continuum V matrix:
# V(B2,B2) off-diag ~ 0.039 from C2 bonds
# V(B2,B1) ~ 0.080 from C2 bonds (B1=(0,0) connects to B2=(1,0),(0,1))
# V(B3,B3) ~ 0.050 from su2/C2 bonds

# Calibrate: use V(B2,B1)_continuum to set the scale.
# B2 cell (1,0) connects to B1 cell (0,0) via C2 bond.
# V^{cell}_{01} = g_K should equal V_B2B1_cont = 0.080.
idx_B2 = [0, 1, 2, 3]
idx_B1 = [4]
idx_B3 = [5, 6, 7]
V_B2B1_cont = np.mean(V_bare_cont[np.ix_(idx_B2, idx_B1)])

# Build full adjacency (any bond type)
adj_full = (np.abs(adj_C2) + np.abs(adj_su2) + np.abs(adj_u1)).astype(float)
adj_full = np.minimum(adj_full, 1.0)  # Binary: connected or not

# Coupling strength per bond type (from continuum V structure)
g_C2 = V_B2B1_cont   # = 0.080 (dominant pairing channel)
g_su2 = 0.02          # Weaker (from B3-B3 structure)  # (local)
g_u1 = 0.01           # Weakest  # (local)

V_cell = g_C2 * np.abs(adj_C2).astype(float) + g_su2 * np.abs(adj_su2).astype(float) + g_u1 * np.abs(adj_u1).astype(float)
# Make symmetric
V_cell = 0.5 * (V_cell + V_cell.T)

# Add diagonal self-pairing for B2-like and B3-like cells
# B2 cells: C2 ~ 1.33. B3 cells: C2 ~ 3.0
for i in range(N_cells):
    c2 = cell_casimirs[i]
    if 0.5 < c2 < 2.0:
        V_cell[i, i] = 0.039  # V(B2,B2)_continuum
    elif 2.0 <= c2 < 4.0:
        V_cell[i, i] = 0.050  # V(B3,B3)_continuum
    else:
        V_cell[i, i] = 0.0    # V(B1,B1) = 0 (Trap 1) and EXT weak

print(f"\nV_cell (32x32) constructed:")
print(f"  Frobenius norm: {np.linalg.norm(V_cell):.6f}")
print(f"  V_cell[B1,B2_10]: {V_cell[0, 2]:.6f} (target: {V_B2B1_cont:.6f})")
print(f"  V_cell[B2_10,B2_01]: {V_cell[1, 2]:.6f}")

# Method B: Continuum V_bare directly (8x8)
# Used as the "calibrated" pairing with correct strength.
print(f"\nContinuum V_bare (8x8):")
print(f"  V(B2,B2) mean: {np.mean(V_bare_cont[np.ix_(idx_B2, idx_B2)]):.6f}")
print(f"  V(B1,B1): {V_bare_cont[4,4]:.2e}")
print(f"  V(B2,B1) mean: {V_B2B1_cont:.6f}")

# ============================================================================
# Section 3: BCS Hamiltonian Routines
# ============================================================================


def build_fock_states(n_modes, n_pair):
    """All Fock states with exactly n_pair occupied modes."""
    return np.array([s for s in range(2**n_modes) if bin(s).count('1') == n_pair])


def build_canonical_H(E_sp, V, n_pair):
    """Build BCS Hamiltonian in the N-pair canonical subspace.

    H = sum_k 2*eps_k * n_k - sum_{kk'} V_{kk'} P+_k P_{k'}
    """
    states = build_fock_states(len(E_sp), n_pair)
    dim = len(states)
    state_idx = {int(s): i for i, s in enumerate(states)}
    H = np.zeros((dim, dim))

    for i, state in enumerate(states):
        state = int(state)
        for k in range(len(E_sp)):
            if state & (1 << k):
                H[i, i] += 2.0 * E_sp[k]

        for k in range(len(E_sp)):
            for kp in range(len(E_sp)):
                if k == kp or abs(V[k, kp]) < 1e-30:
                    continue
                if (state & (1 << kp)) and not (state & (1 << k)):
                    new_state = (state ^ (1 << kp)) | (1 << k)
                    j = state_idx.get(new_state)
                    if j is not None:
                        H[j, i] -= V[k, kp]

    return H, states


def build_full_fock_H(E_sp, V):
    """Build BCS Hamiltonian in the full 2^N Fock space."""
    n_modes = len(E_sp)
    dim = 2**n_modes
    H = np.zeros((dim, dim))

    for s in range(dim):
        for k in range(n_modes):
            if s & (1 << k):
                H[s, s] += 2.0 * E_sp[k]

        for k in range(n_modes):
            for kp in range(n_modes):
                if k == kp or abs(V[k, kp]) < 1e-30:
                    continue
                if (s & (1 << kp)) and not (s & (1 << k)):
                    sp = (s ^ (1 << kp)) | (1 << k)
                    H[sp, s] -= V[k, kp]

    return H


def extract_occupations(psi, states, n_modes):
    """Extract pair occupations from ground state."""
    n_k = np.zeros(n_modes)
    for i, s in enumerate(states):
        for k in range(n_modes):
            if int(s) & (1 << k):
                n_k[k] += psi[i]**2
    return n_k


def project_V_to_eigenbasis(V_cell, evecs, n_modes):
    """Project cell-basis V into lattice eigenbasis (lowest n_modes)."""
    U = evecs[:, :n_modes]  # (N_cells, n_modes)
    return U.T @ V_cell @ U  # (n_modes, n_modes)


# ============================================================================
# Section 4: ED Sweep — Both Approaches
# ============================================================================

print("\n--- Section 4: ED Sweep ---")
print("Running two parallel approaches:")
print("  A) Lattice-projected V (geometrically honest)")
print("  B) Hybrid (lattice E_sp + continuum V, Strutinsky philosophy)")

# Storage arrays
E0_lattV = np.zeros(N_tau)       # Approach A: lattice V
E0_hybrid = np.zeros(N_tau)      # Approach B: hybrid
E0_full_lattV = np.zeros(N_tau)  # Full Fock, lattice V
E0_full_hybrid = np.zeros(N_tau) # Full Fock, hybrid
E_sp_sweep = np.zeros((N_tau, N_MODES))
V_eig_norms = np.zeros(N_tau)

evals_N1_lattV = np.zeros((N_tau, N_MODES))
evals_N1_hybrid = np.zeros((N_tau, N_MODES))
evals_full_lattV = np.zeros((N_tau, N_FOCK))
evals_full_hybrid = np.zeros((N_tau, N_FOCK))
gs_vec_lattV = np.zeros((N_tau, N_MODES))
gs_vec_hybrid = np.zeros((N_tau, N_MODES))
occ_lattV = np.zeros((N_tau, N_MODES))
occ_hybrid = np.zeros((N_tau, N_MODES))

for t in range(N_tau):
    tau = tau_values[t]

    # Single-particle energies: lowest 8 lattice eigenvalues
    E_sp = eigenvalues[t, :N_MODES].copy()
    E_sp_sweep[t] = E_sp

    # === Approach A: Lattice-projected V ===
    V_eig = project_V_to_eigenbasis(V_cell, eigenvectors[t], N_MODES)
    V_eig_norms[t] = np.linalg.norm(V_eig)

    H_A, states_A = build_canonical_H(E_sp, V_eig, N_PAIR_TARGET)
    ev_A = np.linalg.eigh(H_A)
    E0_lattV[t] = ev_A[0][0]
    evals_N1_lattV[t] = ev_A[0]
    gs_vec_lattV[t] = ev_A[1][:, 0]
    occ_lattV[t] = extract_occupations(ev_A[1][:, 0], states_A, N_MODES)

    H_full_A = build_full_fock_H(E_sp, V_eig)
    E0_full_lattV[t] = np.linalg.eigh(H_full_A)[0][0]
    evals_full_lattV[t] = np.linalg.eigh(H_full_A)[0]

    # === Approach B: Hybrid (continuum V) ===
    # Use full continuum V_bare in the 8-mode basis
    H_B, states_B = build_canonical_H(E_sp, V_bare_cont, N_PAIR_TARGET)
    ev_B = np.linalg.eigh(H_B)
    E0_hybrid[t] = ev_B[0][0]
    evals_N1_hybrid[t] = ev_B[0]
    gs_vec_hybrid[t] = ev_B[1][:, 0]
    occ_hybrid[t] = extract_occupations(ev_B[1][:, 0], states_B, N_MODES)

    H_full_B = build_full_fock_H(E_sp, V_bare_cont)
    ev_full_B = np.linalg.eigh(H_full_B)[0]
    E0_full_hybrid[t] = ev_full_B[0]
    evals_full_hybrid[t] = ev_full_B

    if t % 10 == 0 or t == fold_idx:
        tag = " <-- FOLD" if t == fold_idx else ""
        print(f"  tau={tau:.4f}: E0_A={E0_lattV[t]:.6f}, E0_B={E0_hybrid[t]:.6f}, "
              f"gap_A={ev_A[0][1]-ev_A[0][0]:.4f}, gap_B={ev_B[0][1]-ev_B[0][0]:.4f}{tag}")

print(f"\nED sweep complete in {time.time()-t_start:.1f}s")

# ============================================================================
# Section 5: V_eff and Stabilization
# ============================================================================

print("\n--- Section 5: V_eff and Stabilization ---")

# Lattice geometric potential
V_KK_latt = np.sum(eigenvalues, axis=1)

# V_eff for both approaches
V_eff_A = V_KK_latt + E0_lattV
V_eff_B = V_KK_latt + E0_hybrid

# Numerical derivatives
dtau = tau_values[1] - tau_values[0]


def smooth_deriv(y, dt, order=1):
    """Compute smoothed numerical derivatives using Savitzky-Golay-like approach."""
    d = np.gradient(y, dt)
    if order >= 2:
        d = np.gradient(d, dt)
    return d


dE0_A = np.gradient(E0_lattV, dtau)
d2E0_A = np.gradient(dE0_A, dtau)
dE0_B = np.gradient(E0_hybrid, dtau)
d2E0_B = np.gradient(dE0_B, dtau)
dV_KK = np.gradient(V_KK_latt, dtau)
d2V_KK = np.gradient(dV_KK, dtau)
dV_eff_A = np.gradient(V_eff_A, dtau)
d2V_eff_A = np.gradient(dV_eff_A, dtau)
dV_eff_B = np.gradient(V_eff_B, dtau)
d2V_eff_B = np.gradient(dV_eff_B, dtau)

# E_cond relative to uncorrelated single-pair
E_cond_A = E0_lattV - 2 * E_sp_sweep[:, 0]
E_cond_B = E0_hybrid - 2 * E_sp_sweep[:, 0]

print(f"\nAt fold (tau={tau_values[fold_idx]:.4f}):")
print(f"  APPROACH A (lattice V):")
print(f"    E_0 = {E0_lattV[fold_idx]:.6f}, E_cond = {E_cond_A[fold_idx]:.6f}")
print(f"    dE_0/dtau = {dE0_A[fold_idx]:.6f}, d2E_0/dtau2 = {d2E0_A[fold_idx]:.6f}")
print(f"  APPROACH B (hybrid):")
print(f"    E_0 = {E0_hybrid[fold_idx]:.6f}, E_cond = {E_cond_B[fold_idx]:.6f}")
print(f"    dE_0/dtau = {dE0_B[fold_idx]:.6f}, d2E_0/dtau2 = {d2E0_B[fold_idx]:.6f}")
print(f"  V_KK:")
print(f"    V_KK = {V_KK_latt[fold_idx]:.4f}")
print(f"    dV_KK/dtau = {dV_KK[fold_idx]:.4f}, d2V_KK/dtau2 = {d2V_KK[fold_idx]:.4f}")

# Search for critical points in V_eff for BOTH approaches
def find_critical_points(tau_arr, dV_arr, d2V_arr, V_arr):
    """Find minima and maxima from sign changes in dV."""
    dt = tau_arr[1] - tau_arr[0]
    mins, maxs = [], []
    for i in range(2, len(tau_arr) - 2):
        if dV_arr[i-1] < 0 and dV_arr[i] >= 0:
            tc = tau_arr[i-1] + (-dV_arr[i-1]) * dt / (dV_arr[i] - dV_arr[i-1] + 1e-30)
            Vc = np.interp(tc, tau_arr, V_arr)
            d2Vc = np.interp(tc, tau_arr, d2V_arr)
            mins.append((tc, Vc, d2Vc))
        elif dV_arr[i-1] > 0 and dV_arr[i] <= 0:
            tc = tau_arr[i-1] + dV_arr[i-1] * dt / (dV_arr[i-1] - dV_arr[i] + 1e-30)
            Vc = np.interp(tc, tau_arr, V_arr)
            d2Vc = np.interp(tc, tau_arr, d2V_arr)
            maxs.append((tc, Vc, d2Vc))
    return mins, maxs


mins_A, maxs_A = find_critical_points(tau_values, dV_eff_A, d2V_eff_A, V_eff_A)
mins_B, maxs_B = find_critical_points(tau_values, dV_eff_B, d2V_eff_B, V_eff_B)

# Also search for critical points in E_0 alone
mins_E0_A, maxs_E0_A = find_critical_points(tau_values, dE0_A, d2E0_A, E0_lattV)
mins_E0_B, maxs_E0_B = find_critical_points(tau_values, dE0_B, d2E0_B, E0_hybrid)

# Also search for critical points in E_cond
dEc_A = np.gradient(E_cond_A, dtau)
dEc_B = np.gradient(E_cond_B, dtau)
d2Ec_A = np.gradient(dEc_A, dtau)
d2Ec_B = np.gradient(dEc_B, dtau)
mins_Ec_A, maxs_Ec_A = find_critical_points(tau_values, dEc_A, d2Ec_A, E_cond_A)
mins_Ec_B, maxs_Ec_B = find_critical_points(tau_values, dEc_B, d2Ec_B, E_cond_B)

print(f"\n--- Critical Points ---")
for label, ms, mx in [("V_eff_A", mins_A, maxs_A), ("V_eff_B", mins_B, maxs_B),
                        ("E_0_A", mins_E0_A, maxs_E0_A), ("E_0_B", mins_E0_B, maxs_E0_B),
                        ("E_cond_A", mins_Ec_A, maxs_Ec_A), ("E_cond_B", mins_Ec_B, maxs_Ec_B)]:
    print(f"  {label}: {len(ms)} min, {len(mx)} max")
    for tc, vc, d2vc in ms:
        print(f"    MIN at tau={tc:.4f}, value={vc:.6f}, d2={d2vc:.4f}")
    for tc, vc, d2vc in mx:
        print(f"    MAX at tau={tc:.4f}, value={vc:.6f}, d2={d2vc:.4f}")

# ============================================================================
# Section 6: Gate Test
# ============================================================================

print("\n--- Section 6: Gate Test ---")

# The PHYSICAL gate: can E_0(tau) + V_KK(tau) form a minimum?
# On the lattice, V_KK is convex and decreasing. E_0 must rise with tau
# fast enough to balance the V_KK slope. The minimum requires:
# 1. dV_KK + dE_0 = 0 somewhere
# 2. d2V_KK + d2E_0 > 0 there (d2V_KK > 0 helps!)

# Gradient balance check
grad_ratio_A = np.abs(dE0_A[fold_idx]) / (np.abs(dV_KK[fold_idx]) + 1e-30)
grad_ratio_B = np.abs(dE0_B[fold_idx]) / (np.abs(dV_KK[fold_idx]) + 1e-30)

print(f"\nGradient analysis:")
print(f"  |dV_KK/dtau| at fold: {np.abs(dV_KK[fold_idx]):.4f}")
print(f"  |dE_0_A/dtau| at fold: {np.abs(dE0_A[fold_idx]):.6f} (ratio: {grad_ratio_A:.6f})")
print(f"  |dE_0_B/dtau| at fold: {np.abs(dE0_B[fold_idx]):.6f} (ratio: {grad_ratio_B:.6f})")
print(f"  Need ratio ~ 1.0 for gradient balance")

# Curvature analysis
fold_mask = (tau_values >= 0.10) & (tau_values <= 0.30)

d2E0_A_max = np.max(np.abs(d2E0_A[fold_mask]))
d2E0_B_max = np.max(np.abs(d2E0_B[fold_mask]))

print(f"\nCurvature analysis:")
print(f"  d2E_0_A/dtau2 at fold: {d2E0_A[fold_idx]:.6f}")
print(f"  d2E_0_B/dtau2 at fold: {d2E0_B[fold_idx]:.6f}")
print(f"  max|d2E_0_A| in [0.10, 0.30]: {d2E0_A_max:.6f}")
print(f"  max|d2E_0_B| in [0.10, 0.30]: {d2E0_B_max:.6f}")
print(f"  d2V_KK at fold (lattice): {d2V_KK[fold_idx]:.4f}")
print(f"  Continuum threshold: {THRESHOLD_CONTINUUM}")

# GATE 1: Continuum threshold test
gate1_A = d2E0_A_max > THRESHOLD_CONTINUUM
gate1_B = d2E0_B_max > THRESHOLD_CONTINUUM
print(f"\n  GATE 1 (|d2E_0| > 63.2, continuum threshold):")
print(f"    Approach A: {'PASS' if gate1_A else 'FAIL'} ({d2E0_A_max:.4f} vs {THRESHOLD_CONTINUUM})")
print(f"    Approach B: {'PASS' if gate1_B else 'FAIL'} ({d2E0_B_max:.4f} vs {THRESHOLD_CONTINUUM})")

# GATE 2: V_eff minimum exists
gate2_A = len(mins_A) > 0
gate2_B = len(mins_B) > 0
print(f"\n  GATE 2 (V_eff minimum exists):")
print(f"    Approach A: {'PASS' if gate2_A else 'FAIL'} ({len(mins_A)} minima)")
print(f"    Approach B: {'PASS' if gate2_B else 'FAIL'} ({len(mins_B)} minima)")

# GATE 3: Gradient ratio sufficient for balance
gate3_A = grad_ratio_A > 0.01
gate3_B = grad_ratio_B > 0.01
print(f"\n  GATE 3 (gradient ratio > 1%, necessary for balance):")
print(f"    Approach A: {'PASS' if gate3_A else 'FAIL'} ({grad_ratio_A:.6f})")
print(f"    Approach B: {'PASS' if gate3_B else 'FAIL'} ({grad_ratio_B:.6f})")

# GATE 4: E_cond has non-trivial structure (minimum or maximum)
gate4_A = len(mins_Ec_A) + len(maxs_Ec_A) > 0
gate4_B = len(mins_Ec_B) + len(maxs_Ec_B) > 0
print(f"\n  GATE 4 (E_cond has critical points = shell structure):")
print(f"    Approach A: {'PASS' if gate4_A else 'FAIL'} ({len(mins_Ec_A)} min, {len(maxs_Ec_A)} max)")
print(f"    Approach B: {'PASS' if gate4_B else 'FAIL'} ({len(mins_Ec_B)} min, {len(maxs_Ec_B)} max)")

# Overall verdict: PASS requires V_eff minimum in EITHER approach
gate_pass = gate2_A or gate2_B
gate_verdict = "PASS" if gate_pass else "FAIL"

# If FAIL: assess HOW FAR from passing
if not gate_pass:
    # Need gradient balance: what coupling enhancement g* would create a minimum?
    # dV_KK + g*dE_0 = 0 at the fold => g = |dV_KK|/|dE_0|
    g_needed_A = np.abs(dV_KK[fold_idx]) / (np.abs(dE0_A[fold_idx]) + 1e-30)
    g_needed_B = np.abs(dV_KK[fold_idx]) / (np.abs(dE0_B[fold_idx]) + 1e-30)
    print(f"\n  Required coupling enhancement for gradient balance:")
    print(f"    Approach A: g* = {g_needed_A:.1f}x")
    print(f"    Approach B: g* = {g_needed_B:.1f}x")

print(f"\n  === ED-SWEEP-54 GATE VERDICT: {gate_verdict} ===")

# ============================================================================
# Section 7: Strutinsky Shell Correction
# ============================================================================

print("\n--- Section 7: Strutinsky Shell Correction ---")


def strutinsky_smooth(E_sp_arr, gamma, n_pair=1):
    """Strutinsky-smoothed single-particle energy sum.

    Using the Strutinsky prescription (Paper 08):
    1. Compute smoothed level density rho_tilde(E) by convolving with Gaussian
    2. Find smoothed Fermi energy lambda_tilde for N particles
    3. Compute E_smooth = integral E * rho_tilde(E) dE up to lambda_tilde

    For N_pair=1 (1 occupied pair = 1 mode), each "level" holds 1 pair.
    E_smooth = 2 * E_F_smooth (where E_F_smooth is the smoothed lowest level).
    """
    N_tau_loc = E_sp_arr.shape[0]
    n_modes = E_sp_arr.shape[1]  # (local)
    E_smooth = np.zeros(N_tau_loc)

    for t in range(N_tau_loc):
        E_k = E_sp_arr[t]
        E_min_val = np.min(E_k) - 4 * gamma
        E_max_val = np.max(E_k) + 4 * gamma
        E_grid = np.linspace(E_min_val, E_max_val, 1000)
        dE = E_grid[1] - E_grid[0]

        # Smoothed level density
        rho = np.zeros_like(E_grid)
        for ek in E_k:
            rho += np.exp(-(E_grid - ek)**2 / (2 * gamma**2)) / (gamma * np.sqrt(2 * np.pi))

        # Cumulative particle count
        N_cumul = np.cumsum(rho) * dE

        # Find smoothed Fermi energy for n_pair pairs
        idx_F = np.searchsorted(N_cumul, n_pair)
        idx_F = min(idx_F, len(E_grid) - 1)

        # Smoothed energy sum (factor 2 for Kramers pair)
        if idx_F > 0:
            integrand = 2.0 * E_grid[:idx_F+1] * rho[:idx_F+1]
            E_smooth[t] = trapezoid(integrand, E_grid[:idx_F+1])
        else:
            E_smooth[t] = 2.0 * E_grid[0]

    return E_smooth


# Apply Strutinsky smoothing to the lattice single-particle energies
gammas = [0.2, 0.3, 0.4, 0.5, 0.6, 0.8]
strutinsky_results = {}

for gamma in gammas:
    E_sm = strutinsky_smooth(E_sp_sweep, gamma, N_PAIR_TARGET)
    # Shell correction: defined as E_0 - E_smooth
    # For approach A:
    delta_A = E0_lattV - E_sm
    # For approach B:
    delta_B = E0_hybrid - E_sm
    # Pure shell correction (no pairing): 2*E_sp[0] - E_smooth
    delta_SP = 2.0 * E_sp_sweep[:, 0] - E_sm

    strutinsky_results[gamma] = {
        'E_smooth': E_sm,
        'delta_A': delta_A,
        'delta_B': delta_B,
        'delta_SP': delta_SP,
    }
    print(f"  gamma={gamma:.2f}: delta_SP_fold={delta_SP[fold_idx]:.6f}, "
          f"delta_B_fold={delta_B[fold_idx]:.6f}, "
          f"range_SP=[{np.min(delta_SP):.4f}, {np.max(delta_SP):.4f}]")

gamma_primary = 0.4  # (local)
delta_shell_primary = strutinsky_results[gamma_primary]['delta_SP']
delta_full_primary = strutinsky_results[gamma_primary]['delta_B']
E_smooth_primary = strutinsky_results[gamma_primary]['E_smooth']

# Plateau check
gamma_test = [0.3, 0.4, 0.5, 0.6]
delta_plateau = np.array([strutinsky_results[g]['delta_SP'][fold_idx] for g in gamma_test])
spread = np.max(delta_plateau) - np.min(delta_plateau)
mean_val = np.mean(delta_plateau)
rel_spread = spread / (abs(mean_val) + 1e-10)
print(f"\nPlateau check (gamma={gamma_test}):")
print(f"  delta_SP at fold: {delta_plateau}")
print(f"  Spread: {spread:.6f}, relative: {rel_spread:.4f}")
print(f"  Status: {'GOOD' if rel_spread < 0.3 else 'MARGINAL' if rel_spread < 1.0 else 'POOR'}")

# Strutinsky shell correction second derivative
d_delta_SP = np.gradient(delta_shell_primary, dtau)
d2_delta_SP = np.gradient(d_delta_SP, dtau)
print(f"\nShell correction curvature at fold:")
print(f"  d2(delta_E_shell)/dtau2 = {d2_delta_SP[fold_idx]:.6f}")
print(f"  max|d2(delta_E_shell)| in [0.10,0.30] = {np.max(np.abs(d2_delta_SP[fold_mask])):.6f}")

# ============================================================================
# Section 8: Detailed Diagnostic Table
# ============================================================================

print("\n" + "=" * 78)
print("SUMMARY TABLE")
print("=" * 78)

key_taus = [0, 5, 10, 15, fold_idx, fold_idx+1, 25, 30, 35, 40, 45, 49]
print(f"\n{'tau':>7s} {'E0_A':>10s} {'E0_B':>10s} {'Ec_A':>10s} {'Ec_B':>10s} {'V_KK':>8s}")
for i in key_taus:
    if i < N_tau:
        tag = " *" if i == fold_idx else ""
        print(f"{tau_values[i]:7.4f} {E0_lattV[i]:10.6f} {E0_hybrid[i]:10.6f} "
              f"{E_cond_A[i]:10.6f} {E_cond_B[i]:10.6f} {V_KK_latt[i]:8.2f}{tag}")

# Pair occupation evolution
print(f"\nPair occupations (Approach B, hybrid) at key tau:")
print(f"{'tau':>7s}  ", end="")
for k in range(N_MODES):
    print(f"{'n_'+str(k):>8s}", end="")
print()
for i in [0, fold_idx, N_tau-1]:
    print(f"{tau_values[i]:7.4f}  ", end="")
    for k in range(N_MODES):
        print(f"{occ_hybrid[i, k]:8.4f}", end="")
    print()

# E_cond comparison to continuum
print(f"\nE_cond comparison:")
print(f"  Continuum (S36 ED-CONV-36): {E_cond_ED_8mode:.6f}")
print(f"  Approach A at fold: {E_cond_A[fold_idx]:.6f} (ratio: {E_cond_A[fold_idx]/E_cond_ED_8mode:.4f})")
print(f"  Approach B at fold: {E_cond_B[fold_idx]:.6f} (ratio: {E_cond_B[fold_idx]/E_cond_ED_8mode:.4f})")

# Excitation gap (N=1 sector)
gap_A_fold = evals_N1_lattV[fold_idx, 1] - evals_N1_lattV[fold_idx, 0]
gap_B_fold = evals_N1_hybrid[fold_idx, 1] - evals_N1_hybrid[fold_idx, 0]
print(f"\nExcitation gaps at fold:")
print(f"  Approach A: {gap_A_fold:.6f}")
print(f"  Approach B: {gap_B_fold:.6f}")

# ============================================================================
# Section 9: Save Data
# ============================================================================

print("\n--- Section 9: Saving Data ---")

save_dict = {
    # Core
    'tau_values': tau_values,
    'E0': E0_hybrid,                   # Primary result (approach B)
    'E0_lattV': E0_lattV,              # Approach A
    'E0_full': E0_full_hybrid,         # Full Fock, approach B
    'E0_full_lattV': E0_full_lattV,    # Full Fock, approach A
    'V_KK_latt': V_KK_latt,
    'V_eff': V_KK_latt + E0_hybrid,   # Primary V_eff
    'V_eff_lattV': V_eff_A,

    # Condensation energy
    'E_cond_A': E_cond_A,
    'E_cond_B': E_cond_B,

    # Derivatives
    'dE0': dE0_B,
    'd2E0': d2E0_B,
    'E0_second_deriv': d2E0_B,
    'dE0_lattV': dE0_A,
    'd2E0_lattV': d2E0_A,
    'dV_KK': dV_KK,
    'd2V_KK': d2V_KK,
    'dV_eff': dV_eff_B,
    'd2V_eff': d2V_eff_B,

    # Spectra
    'all_eigenvalues': evals_full_hybrid,
    'all_eigenvalues_N1': evals_N1_hybrid,
    'all_eigenvalues_N1_lattV': evals_N1_lattV,
    'eigenstates': gs_vec_hybrid,
    'eigenstates_lattV': gs_vec_lattV,
    'pair_occupations': occ_hybrid,
    'pair_occupations_lattV': occ_lattV,
    'E_sp_sweep': E_sp_sweep,

    # Strutinsky
    'strutinsky_shell': delta_shell_primary,
    'strutinsky_full': delta_full_primary,
    'strutinsky_smooth': E_smooth_primary,
    'strutinsky_gamma': np.float64(gamma_primary),

    # Pairing
    'V_cell': V_cell,
    'V_eig_norms': V_eig_norms,
    'V_bare_cont': V_bare_cont,

    # Gate
    'gate_name': np.array(['ED-SWEEP-54']),
    'gate_verdict': np.array([gate_verdict]),
    'gate_detail': np.array([
        f"V_eff_mins_A={len(mins_A)},V_eff_mins_B={len(mins_B)},"
        f"d2E0_B_fold={d2E0_B[fold_idx]:.6f},d2V_KK_fold={d2V_KK[fold_idx]:.2f},"
        f"grad_ratio_B={grad_ratio_B:.6f},"
        f"continuum_threshold={THRESHOLD_CONTINUUM}"
    ]),

    # Metadata
    'N_modes': np.int64(N_MODES),
    'N_pair': np.int64(N_PAIR_TARGET),
    'fold_idx': np.int64(fold_idx),
}

if mins_A:
    save_dict['minima_A'] = np.array(mins_A)
if maxs_A:
    save_dict['maxima_A'] = np.array(maxs_A)
if mins_B:
    save_dict['minima_B'] = np.array(mins_B)
if maxs_B:
    save_dict['maxima_B'] = np.array(maxs_B)

np.savez(data_dir / 's54_ed_sweep.npz', **save_dict)
print(f"Saved: computations/session-54/s54_ed_sweep.npz")

# ============================================================================
# Section 10: Plot
# ============================================================================

print("\n--- Section 10: Plotting ---")

fig, axes = plt.subplots(3, 2, figsize=(14, 16))
fig.suptitle('ED-SWEEP-54: Richardson Ground State E_0(τ) on 32-Cell Lattice\n'
             f'Gate: {gate_verdict}', fontsize=14, fontweight='bold')

# Panel 1: E_0 and E_cond vs tau
ax = axes[0, 0]
ax.plot(tau_values, E0_hybrid, 'b-', linewidth=2, label='E_0 hybrid')
ax.plot(tau_values, E0_lattV, 'b--', linewidth=1, label='E_0 lattice V')
ax.plot(tau_values, E_cond_B, 'r-', linewidth=2, label='E_cond hybrid')
ax.plot(tau_values, E_cond_A, 'r--', linewidth=1, label='E_cond lattice V')
ax.axvline(tau_fold, color='gray', linestyle=':', alpha=0.5)
ax.set_xlabel('τ')
ax.set_ylabel('Energy (M_KK)')
ax.set_title('BCS Ground State Energy')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 2: V_eff zoom near fold
ax = axes[0, 1]
zoom = (tau_values >= 0.05) & (tau_values <= 0.40)
ax.plot(tau_values[zoom], V_eff_B[zoom] - V_eff_B[fold_idx], 'r-', linewidth=2, label='V_eff(B) - V_eff(fold)')
ax.plot(tau_values[zoom], V_KK_latt[zoom] - V_KK_latt[fold_idx], 'k--', linewidth=1, label='V_KK - V_KK(fold)')
for tc, vc, _ in mins_B:
    ax.plot(tc, vc - V_eff_B[fold_idx], 'go', ms=10, label=f'min@{tc:.3f}')
for tc, vc, _ in maxs_B:
    ax.plot(tc, vc - V_eff_B[fold_idx], 'rs', ms=8, label=f'max@{tc:.3f}')
ax.axvline(tau_fold, color='gray', linestyle=':', alpha=0.5)
ax.axhline(0, color='gray', linestyle='-', alpha=0.3)
ax.set_xlabel('τ')
ax.set_ylabel('ΔE (M_KK, relative to fold)')
ax.set_title('V_eff Near Fold')
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)

# Panel 3: Gradients
ax = axes[1, 0]
ax.plot(tau_values, dE0_B, 'b-', linewidth=2, label='dE_0/dτ (hybrid)')
ax.plot(tau_values, dV_KK / 100, 'k--', linewidth=1, label='dV_KK/dτ / 100')
ax.plot(tau_values, dV_eff_B, 'r-', linewidth=2, label='dV_eff/dτ (hybrid)')
ax.axhline(0, color='gray', linestyle='-', alpha=0.3)
ax.axvline(tau_fold, color='gray', linestyle=':', alpha=0.5)
ax.set_xlabel('τ')
ax.set_ylabel('Gradient (M_KK)')
ax.set_title('Gradients (note: dV_KK scaled by 1/100)')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 4: Second derivatives (curvature)
ax = axes[1, 1]
ax.plot(tau_values, d2E0_B, 'b-', linewidth=2, label='d²E_0/dτ² (hybrid)')
ax.plot(tau_values, d2E0_A, 'b--', linewidth=1, label='d²E_0/dτ² (lattV)')
ax.axhline(0, color='gray', linestyle='-', alpha=0.3)
ax.axhline(THRESHOLD_CONTINUUM, color='green', linestyle=':', label=f'Threshold={THRESHOLD_CONTINUUM}')
ax.axvline(tau_fold, color='gray', linestyle=':', alpha=0.5)
ax.set_xlabel('τ')
ax.set_ylabel('d²/dτ² (M_KK)')
ax.set_title('E_0 Curvature (Gate Test)')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 5: Strutinsky shell correction
ax = axes[2, 0]
for gamma in [0.3, 0.4, 0.5, 0.6]:
    ls = '-' if gamma == 0.4 else '--'
    lw = 2 if gamma == 0.4 else 1  # (local)
    ax.plot(tau_values, strutinsky_results[gamma]['delta_SP'], ls, linewidth=lw,
            label=f'δE_shell (γ={gamma:.1f})')
ax.axhline(0, color='gray', linestyle='-', alpha=0.3)
ax.axvline(tau_fold, color='gray', linestyle=':', alpha=0.5)
ax.set_xlabel('τ')
ax.set_ylabel('δE_shell (M_KK)')
ax.set_title('Strutinsky Shell Correction (single-particle)')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 6: Pair occupations
ax = axes[2, 1]
for k in range(N_MODES):
    marker = 'o' if k < 4 else ('s' if k == 4 else '^')
    ax.plot(tau_values, occ_hybrid[:, k], '-'+marker, ms=2, label=f'k={k}')
ax.axvline(tau_fold, color='gray', linestyle=':', alpha=0.5)
ax.set_xlabel('τ')
ax.set_ylabel('n_k')
ax.set_title('Pair Occupations (Hybrid)')
ax.legend(fontsize=7, ncol=2)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(data_dir / 's54_ed_sweep.png', dpi=150, bbox_inches='tight')
print(f"Saved: computations/session-54/s54_ed_sweep.png")

# ============================================================================
# Final Summary
# ============================================================================

elapsed = time.time() - t_start
print(f"\n{'='*78}")
print(f"ED-SWEEP-54 COMPLETE in {elapsed:.1f}s")
print(f"{'='*78}")
print(f"\nGATE: ED-SWEEP-54 = {gate_verdict}")
print(f"  Approach A (lattice V):")
print(f"    E_0 at fold: {E0_lattV[fold_idx]:.6f}, E_cond: {E_cond_A[fold_idx]:.6f}")
print(f"    d2E_0 at fold: {d2E0_A[fold_idx]:.6f}, grad ratio: {grad_ratio_A:.6f}")
print(f"    V_eff minima: {len(mins_A)}, maxima: {len(maxs_A)}")
print(f"  Approach B (hybrid, Strutinsky):")
print(f"    E_0 at fold: {E0_hybrid[fold_idx]:.6f}, E_cond: {E_cond_B[fold_idx]:.6f}")
print(f"    d2E_0 at fold: {d2E0_B[fold_idx]:.6f}, grad ratio: {grad_ratio_B:.6f}")
print(f"    V_eff minima: {len(mins_B)}, maxima: {len(maxs_B)}")
print(f"  Strutinsky delta_E_shell at fold: {delta_shell_primary[fold_idx]:.6f}")
print(f"  Lattice d2V_KK at fold: {d2V_KK[fold_idx]:.2f}")
print(f"  Continuum threshold: {THRESHOLD_CONTINUUM}")
print(f"\nData: computations/session-54/s54_ed_sweep.npz")
print(f"Plot: computations/session-54/s54_ed_sweep.png")
