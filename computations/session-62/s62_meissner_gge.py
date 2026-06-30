#!/usr/bin/env python3
"""
S62 MEISSNER-GGE-62: Superfluid Weight in the Post-Transit GGE State
=====================================================================

PHYSICS (Volovik superfluid universe perspective):
  In superfluid 3He-B, the superfluid density rho_s is determined by the
  condensate fraction and the quasiparticle occupation numbers. At T=0,
  rho_s = rho (full superfluid). At finite T, Landau's two-fluid model
  gives rho_s = rho - rho_n where rho_n comes from thermally excited
  quasiparticles.

  For the GGE state, we have NON-THERMAL quasiparticle occupations
  {n_k} determined by the Richardson-Gaudin conserved charges. The
  superfluid weight D_s(GGE) is computed from the current-current
  correlator evaluated with these GGE occupation numbers.

  The computation follows three routes:
    Route 1: BCS current-current correlator with GGE occupation numbers
      D_s = (diamagnetic) - (paramagnetic bubble)
      = n/m - (2/V) sum_{k,k'} |J_{kk'}|^2 * f_GGE(k) / (E_k + E_k')
    Route 2: Landau two-fluid depletion formula
      D_s(GGE) = D_s(T=0) * [1 - sum_k n_k * (partial rho_n / partial n_k)]
    Route 3: Direct Josephson stiffness with GGE-modified pair amplitude
      D_s(GGE) = 2 * E_J * S_+(GGE) where S_+(GGE) uses GGE correlator

  Gate: MEISSNER-GGE-62
    PASS if D_s(GGE) > 0.636 M_KK^2 (>10% of fold value)
    FAIL if D_s(GGE) < 0.01 M_KK^2 (Meissner destroyed)
    INFO if in [0.01, 0.636]

Inputs:
  - computations/session-61/s61_extremal_gge.npz (GGE occupation numbers)
  - computations/session-61/s61_superfluid_weight.npz (fold D_s computation)
  - computations/session-60/s60_pair_transfer_n4.npz (BCS Hamiltonian data)
  - canonical_constants.py

Author: volovik-superfluid-universe-theorist (Session 62, Wave 2)
Date: 2026-03-29
"""

import os
import sys
import time
import numpy as np
from scipy.linalg import eigh, expm

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

t0 = time.time()

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from canonical_constants import (
    PI, N_cells, tau_fold, omega_L1, omega_L2,
    J_C2, J_su2, J_u1, T_acoustic,
    E_cond, Delta_0_GL, Delta_B3,
    E_B1, E_B2_mean, E_B3_mean,
    rho_B2_per_mode, alpha_QM,
    c_Gold, N_dof_BCS, xi_GL, xi_BCS,
)

np.set_printoptions(precision=10, linewidth=140, suppress=True)

print("=" * 78)
print("MEISSNER-GGE-62: Superfluid Weight in the Post-Transit GGE State")
print("=" * 78)

# ===========================================================================
# STEP 1: Load all upstream data
# ===========================================================================
print("\n--- Step 1: Load upstream data ---")

# GGE occupation numbers (S61 extremal GGE)
gge_data = np.load(os.path.join(SCRIPT_DIR, 's61_extremal_gge.npz'), allow_pickle=True)
n_k_GGE = gge_data['n_k_crit']       # 8 occupation numbers
lambda_k_GGE = gge_data['lambda_k_crit']  # 8 Lagrange multipliers
E_GS_GGE = float(gge_data['E_GS_crit'])
gap_GGE = float(gge_data['gap_crit'])
evals_GGE = gge_data['evals_crit_20']

# Superfluid weight at fold (S61)
sw_data = np.load(os.path.join(SCRIPT_DIR, 's61_superfluid_weight.npz'), allow_pickle=True)
D_s_fold_JPT = float(sw_data['D_s_JPT'])   # = 6.356 M_KK^2
D_s_fold_QM = float(sw_data['D_s_QM'])     # = 1.72e-5 M_KK^2
E_J_fold = float(sw_data['E_J_fold'])       # = 3.397 M_KK
S_plus_1 = float(sw_data['S_plus_1'])       # = 0.9356
g_mean_tensor = sw_data['g_mean_tensor']
g_mean_scalar = float(sw_data['g_mean_scalar'])

# BCS Hamiltonian data (S60)
pt_data = np.load(os.path.join(SCRIPT_DIR, 's60_pair_transfer_n4.npz'), allow_pickle=True)
eps_fold = pt_data['eps_fold']   # 8 single-particle energies
V_fold = pt_data['V_fold']       # 8x8 pairing interaction matrix

print(f"  GGE occupation numbers (n_k):")
sector_labels = ['B2[0]', 'B2[1]', 'B2[2]', 'B2[3]', 'B1[0]', 'B3[0]', 'B3[1]', 'B3[2]']
for i in range(N_dof_BCS):
    print(f"    {sector_labels[i]}: n_k = {n_k_GGE[i]:.10f}, lambda_k = {lambda_k_GGE[i]:.6f}")
print(f"  Sum n_k = {np.sum(n_k_GGE):.10f}")
print(f"  GGE gap = {gap_GGE:.10f} M_KK")
print(f"  D_s(fold, JPT) = {D_s_fold_JPT:.6f} M_KK^2")
print(f"  E_J(fold) = {E_J_fold:.6f} M_KK")
print(f"  S_+(1) at fold = {S_plus_1:.6f}")
print(f"  Single-particle energies: {eps_fold}")

# ===========================================================================
# STEP 2: Build the BCS Hamiltonian in the mode-pair basis
# ===========================================================================
print("\n--- Step 2: BCS Hamiltonian and Bogoliubov transformation ---")

N = N_dof_BCS  # = 8 modes

# The BCS Hamiltonian in the pair basis:
#   H_BCS = sum_k 2*eps_k * n_k - sum_{k,k'} V_{kk'} * c^+_k c_{k'}
# where c^+_k creates a Cooper pair in mode k.

# Build the full many-body Hamiltonian in the N_pair = 0,1 Fock sector
# For the superfluid weight, we need the current operator and its
# expectation value in the GGE state.

# The current operator for a superconductor:
#   J_x = sum_k (d eps_k / dk_x) * n_k (paramagnetic)
#   + sum_k (d^2 eps_k / dk_x^2) * A_x (diamagnetic)
#
# In the BCS ground state:
#   D_s = (diamagnetic) - (paramagnetic) = n/m - Pi(0)
#
# For the INTER-CELL superfluid weight (Josephson stiffness):
#   D_s = 2 * E_J * <S_+> / V_cell
# where <S_+> is the pair transfer amplitude.

# In the GGE state, the pair transfer amplitude is modified because
# the quasiparticle occupation changes the anomalous correlator.

# The BCS anomalous average (pair amplitude):
#   F_k = <c_{-k,down} c_{k,up}> = u_k * v_k * (1 - 2*n_k^{qp})
# where u_k, v_k are Bogoliubov amplitudes and n_k^{qp} is the
# quasiparticle occupation.

# For a BCS state: u_k^2 = (1 + xi_k/E_k)/2, v_k^2 = (1 - xi_k/E_k)/2
# E_k = sqrt(xi_k^2 + Delta^2)

# The GGE occupation numbers n_k_GGE are the PAIR occupation numbers
# in the original (non-Bogoliubov) basis. They are NOT the quasiparticle
# occupations directly. However, for the N_pair=1 system, the ground
# state has one pair distributed according to the BCS wavefunction,
# and the GGE state has modified weights.

# The pair amplitude in the GGE is:
#   <P_+>_GGE = sum_k sqrt(n_k_GGE * (1 - n_k_GGE)) * phase_k
# For the condensate: all pairs in the same mode -> coherent
# For the GGE: pairs spread across modes -> reduced coherence

print("\n  Computing pair amplitudes and coherence factors...")

# BCS coherence factors from the pairing interaction
# Solve the BCS gap equation: Delta_k = sum_k' V_{kk'} * Delta_{k'} / (2*E_{k'})
# For the single-pair ground state, Delta ~ V * psi_GS

# Ground state wavefunction from exact diagonalization
# H_BCS |psi> = E_GS |psi> in the N_pair=1 sector
# The N_pair=1 sector has dimension C(8,1) = 8
# |psi> = sum_k alpha_k |k> where |k> = c^+_k |0>

H_pair = np.diag(2.0 * eps_fold) - V_fold  # 8x8 pair Hamiltonian
E_pair, V_pair = eigh(H_pair)

print(f"  Pair Hamiltonian eigenvalues:")
for i in range(N):
    print(f"    E_{i} = {E_pair[i]:.10f} M_KK")

# Ground state wavefunction
psi_GS = V_pair[:, 0]
E_GS = E_pair[0]
print(f"\n  Ground state energy = {E_GS:.10f} M_KK")
print(f"  Ground state wavefunction (pair amplitudes):")
for i in range(N):
    print(f"    alpha_{i} ({sector_labels[i]}) = {psi_GS[i]:.10f}")

# Pair occupation in the ground state: n_k^GS = |alpha_k|^2
n_k_GS = np.abs(psi_GS)**2
print(f"\n  Ground state pair occupation:")
for i in range(N):
    print(f"    n_k^GS_{i} = {n_k_GS[i]:.10f}")
print(f"  Sum = {np.sum(n_k_GS):.10f}")

# ===========================================================================
# STEP 3: Route 1 — BCS current-current correlator with GGE occupations
# ===========================================================================
print("\n--- Step 3: Route 1 — Current-Current Correlator ---")
print("  D_s = n/m_eff - Pi(q=0, omega=0)")
print("  where Pi is the paramagnetic susceptibility (current-current bubble)")

# The diamagnetic term: D_dia = n / m_eff
# In the BCS pair picture, the diamagnetic contribution comes from
# the second derivative of the energy with respect to the vector potential.
#
# For the Josephson lattice, the diamagnetic term is:
#   D_dia = E_J * sum_{<ij>} cos(phi_i - phi_j) / V_cell
# In the ordered state (cos(phi_i-phi_j) ~ 1):
#   D_dia = z * E_J / V_cell where z = coordination number

# From S59: <cos(phi)> = 0.960 (Josephson-phase PASS-B)
cos_phi_mean = 0.960  # (local)
z_eff = 2.0 * 92 / 32  # 2*N_bonds/N_cells = effective coordination
print(f"  <cos(phi)> = {cos_phi_mean:.3f} (S59 JOSEPHSON-PHASE-59)")
print(f"  z_eff = 2*N_bonds/N_cells = {z_eff:.2f}")

D_dia = z_eff * E_J_fold * cos_phi_mean
print(f"  D_dia = z_eff * E_J * <cos(phi)> = {D_dia:.6f} M_KK^2")

# The paramagnetic term: current-current bubble
# Pi(q=0, omega=0) = (2/V) sum_{m,n} |<m|J|n>|^2 * [f(E_m) - f(E_n)] / (E_n - E_m)
#
# In the BCS pair basis, the current operator matrix element between
# pair states k and k' is proportional to V_{kk'} (the pair hopping).
# The current flows when pairs hop between modes.
#
# For the GGE state, the distribution function f(E) is replaced by
# the GGE occupation: f_GGE(k) = n_k_GGE

# Current operator in the pair basis:
# J_k = d(eps_k)/dk ~ velocity * pair operator
# For inter-cell current: J_{kk'} ~ V_{kk'} * (position operator)
# The relevant matrix element is V_{kk'} itself

# Paramagnetic susceptibility in the N_pair=1 sector:
# Using the eigenstates of H_pair

# For the GROUND STATE (thermal T=0):
# Pi_GS = 2 * sum_{n>0} |<0|J|n>|^2 / (E_n - E_0)
# where J = sum_k j_k * c^+_k c_k (current operator)

# For the GGE state with density matrix rho_GGE = sum_k n_k |k><k|
# (in the diagonal ensemble):
# Pi_GGE = sum_{m,n} |<m|J|n>|^2 * (rho_m - rho_n) / (E_n - E_m)

# Build the current operator in the pair basis
# The current is the derivative of H with respect to the vector potential
# In the tight-binding (Josephson) picture:
# H(A) = sum_k 2*eps_k n_k - sum_{kk'} V_{kk'} e^{i*A} c^+_k c_{k'}
# dH/dA = -i * sum_{kk'} V_{kk'} c^+_k c_{k'} (for k != k')
# So J = -i * V_fold (off-diagonal part)

J_op = -1j * (V_fold - np.diag(np.diag(V_fold)))  # off-diagonal V as current

# Transform to the energy eigenbasis of H_pair
J_eig = V_pair.T @ J_op @ V_pair  # J in the eigenbasis

print(f"\n  Current operator |J_{'{mn}'}|^2 (first 4x4 block):")
J2 = np.abs(J_eig)**2
for i in range(4):
    row = '  '.join([f'{J2[i,j]:.6f}' for j in range(4)])
    print(f"    {row}")

# === GGE density matrix in the energy eigenbasis ===
# The GGE occupation numbers n_k_GGE are defined in the ORIGINAL mode basis.
# Transform to the energy eigenbasis:
# rho_GGE(E-basis) = V_pair^T * diag(n_k_GGE) * V_pair
rho_GGE_mode = np.diag(n_k_GGE)
rho_GGE_eig = V_pair.T @ rho_GGE_mode @ V_pair

print(f"\n  GGE density matrix diagonal (eigenbasis):")
rho_diag_GGE = np.diag(rho_GGE_eig)
for i in range(N):
    print(f"    rho_{i} = {rho_diag_GGE[i]:.10f}")

# Ground state density matrix for comparison
rho_GS_eig = np.zeros((N, N))
rho_GS_eig[0, 0] = 1.0  # pure ground state

# === Paramagnetic susceptibility ===
# Pi = sum_{m != n} |J_{mn}|^2 * (rho_m - rho_n) / (E_n - E_m)
# where rho_m = <m|rho_GGE|m> and E_m are the pair eigenvalues

def compute_Pi(rho_diag, E_vals, J2_matrix):
    """Compute paramagnetic susceptibility."""
    Pi = 0.0  # (local)
    Nn = len(E_vals)
    for m in range(Nn):
        for n in range(Nn):
            if m == n:
                continue
            dE = E_vals[n] - E_vals[m]
            if abs(dE) < 1e-12:
                continue
            Pi += J2_matrix[m, n] * (rho_diag[m] - rho_diag[n]) / dE
    return Pi

Pi_GS = compute_Pi(np.diag(rho_GS_eig), E_pair, J2)
Pi_GGE = compute_Pi(rho_diag_GGE, E_pair, J2)

print(f"\n  Pi(GS) = {Pi_GS:.10f}")
print(f"  Pi(GGE) = {Pi_GGE:.10f}")

# Superfluid weight from current-current correlator
# D_s = D_dia - Pi
# Note: Pi should be positive (paramagnetic response reduces D_s)
D_s_GS_cc = D_dia - Pi_GS
D_s_GGE_cc = D_dia - Pi_GGE

print(f"\n  Route 1 results:")
print(f"    D_s(GS, current-current) = {D_s_GS_cc:.6f} M_KK^2")
print(f"    D_s(GGE, current-current) = {D_s_GGE_cc:.6f} M_KK^2")
print(f"    Ratio D_s(GGE)/D_s(GS) = {D_s_GGE_cc/D_s_GS_cc:.6f}")

# ===========================================================================
# STEP 4: Route 2 — Two-fluid (Landau) depletion formula
# ===========================================================================
print("\n--- Step 4: Route 2 — Landau Two-Fluid Depletion ---")
print("  D_s(GGE) = D_s(T=0) * (1 - f_n)")
print("  where f_n = normal fraction from GGE quasiparticle occupations")

# In Volovik's two-fluid model (Paper 01, Ch.5):
# rho_s/rho = 1 - rho_n/rho
# rho_n/rho = sum_k n_k^{qp} * (d eps_k / dk)^2 / (rho * some normalization)
#
# For the pair model, the normal fraction comes from the GGE depleting
# the condensate. The condensate fraction is:
#   n_0 = |<psi_GS | rho_GGE | psi_GS>|
# which measures how much of the GGE state overlaps with the BCS ground state.

# Condensate fraction in the GGE state
# <psi_GS | rho_GGE | psi_GS> = sum_k |psi_GS(k)|^2 * n_k_GGE
n_0_GGE = np.sum(n_k_GS * n_k_GGE)

# For comparison, ground state condensate fraction
n_0_GS = np.sum(n_k_GS * n_k_GS)  # = sum |alpha_k|^4 (= 1 for pure state overlap with itself)

print(f"  Condensate overlap:")
print(f"    n_0(GS) = sum |alpha_k|^4 = {n_0_GS:.10f}")
print(f"    n_0(GGE) = sum |alpha_k|^2 * n_k^GGE = {n_0_GGE:.10f}")

# The normal fraction in the two-fluid picture:
# f_n = 1 - n_0(GGE) / n_0(GS)
# But this is the condensate depletion, not the full normal fraction.
# The full superfluid weight also includes the off-diagonal long-range
# order (ODLRO) contribution.

# ODLRO in the pair basis:
# The one-body density matrix rho_1(k, k') = <c^+_k c_{k'}>
# For the GGE state: rho_1(k, k') = sum_n psi_n(k) psi_n*(k') * n_k^GGE
# ODLRO means the largest eigenvalue of rho_1 is O(N).
# For the N_pair=1 sector, rho_1 is 8x8.

# Build the one-body density matrix in the GGE
rho_1_GGE = np.zeros((N, N))
for n in range(N):
    psi_n = V_pair[:, n]  # n-th eigenstate of H_pair
    # GGE weight for eigenstate n:
    # The GGE in the energy eigenbasis has off-diagonal terms because
    # n_k_GGE is defined in the mode basis, not the energy basis.
    # rho_1(k,k') = sum_n,n' rho_GGE(n,n') * psi_n(k) * psi_n'(k')
    for m in range(N):
        psi_m = V_pair[:, m]
        rho_1_GGE += rho_GGE_eig[n, m] * np.outer(psi_n, psi_m)

# Eigenvalues of rho_1_GGE (largest = condensate fraction)
evals_rho1, evecs_rho1 = eigh(rho_1_GGE)
evals_rho1_sorted = np.sort(evals_rho1)[::-1]

print(f"\n  One-body density matrix eigenvalues (GGE):")
for i in range(N):
    print(f"    lambda_{i} = {evals_rho1_sorted[i]:.10f}")

# The largest eigenvalue IS the condensate fraction for N_pair=1
n_condensate_GGE = evals_rho1_sorted[0]
print(f"\n  Condensate fraction (ODLRO):")
print(f"    n_condensate(GGE) = {n_condensate_GGE:.10f}")

# Verify: for the ground state, n_condensate should be 1.0
rho_1_GS = np.outer(psi_GS, psi_GS)
evals_rho1_GS = np.sort(np.linalg.eigvalsh(rho_1_GS))[::-1]
print(f"    n_condensate(GS) = {evals_rho1_GS[0]:.10f}")

# Two-fluid superfluid weight:
# D_s(GGE) / D_s(GS) = n_condensate(GGE) / n_condensate(GS)
# This is the Leggett-type formula: superfluid weight proportional to ODLRO
ratio_ODLRO = n_condensate_GGE / evals_rho1_GS[0]
D_s_GGE_2fluid = D_s_fold_JPT * ratio_ODLRO

print(f"\n  Route 2 results:")
print(f"    ODLRO ratio = {ratio_ODLRO:.10f}")
print(f"    D_s(GGE, two-fluid) = D_s(fold) * ODLRO_ratio")
print(f"    D_s(GGE, two-fluid) = {D_s_fold_JPT:.4f} * {ratio_ODLRO:.6f} = {D_s_GGE_2fluid:.6f} M_KK^2")

# ===========================================================================
# STEP 5: Route 3 — Josephson stiffness with GGE pair amplitude
# ===========================================================================
print("\n--- Step 5: Route 3 — Josephson Pair Stiffness ---")
print("  D_s(GGE) = 2 * E_J * S_+(GGE)")
print("  where S_+(GGE) = |<N+1| S_+ |N>|_GGE is the pair transfer amplitude")

# The pair transfer operator S_+ creates a pair in the other cell.
# In the GGE state, the pair transfer amplitude depends on the
# available Fock space for the transferred pair.
#
# S_+(GGE) = sum_k sqrt((1 - n_k^GGE)) * <k| S_+ |GGE>
#
# For the ground state (N_pair=1):
#   S_+(GS) = sqrt(N_pair * (N_modes - N_pair + 1) / N_modes) * overlap
# which gives S_+(1) = 0.9356 (from S60 pair transfer).
#
# For the GGE state, the pair transfer is SUPPRESSED because the
# quasiparticle modes are partially occupied, reducing the phase space
# for pair hopping.
#
# The key quantity is the ANOMALOUS correlator:
#   F(GGE) = sum_k u_k v_k * (1 - 2*f_k^{qp})
# For the pair model:
#   F(GGE) = sum_k psi_GS(k) * sqrt(n_k_GGE * (1 - n_k_GGE))
#
# But more precisely, S_+(GGE) comes from the GGE-averaged pair creation:
#   S_+(GGE) = Tr[rho_GGE * S_+]
# In the energy eigenbasis, this requires the off-diagonal elements of rho_GGE.

# Method 3a: Direct computation from GGE density matrix
# The pair transfer operator S_+ in the N_pair sector:
# S_+ |k> = |k, extra_pair> (creates pair in adjacent cell)
# For the stiffness, we need <S_+> in the N_pair=1 sector.
# S_+ ~ sum_k c^+_k (creation in adjacent cell)
# <S_+>_GGE = sum_k <c^+_k>_GGE = sum_k sqrt(n_k_GGE) * phase_k
#
# Actually, S_+(N_pair=1) connects N=1 to N=2 sectors.
# From the S60 pair transfer computation:
# S_+(N) = |<N+1,GS| sum_k c^+_{k,cell2} |N,GS,cell1>|
#
# For the GGE, the state is NOT |N,GS> but a mixed state.
# The pair transfer amplitude in the GGE is:
# S_+(GGE) = sum_n sqrt(p_n) * <N+1,GS| S_+ |N,n>
# where p_n are the GGE weights and |N,n> are the N-particle eigenstates.

# The pair transfer amplitude from N=1 GGE to N=2 ground state:
# <2,GS| S_+ |1,GGE> = sum_n sqrt(p_n) * <2,GS| S_+ |1,n>
# where p_n = overlap of GGE with eigenstate n.

# For a diagonal GGE in the mode basis:
# rho_GGE = diag(n_k_GGE) in the mode basis
# Transform to energy eigenbasis: rho_GGE_eig = V^T * rho_GGE * V

# The pair transfer matrix elements <2,GS|S_+|1,n> for each eigenstate n
# of the 1-pair sector involve the overlap of eigenstates with the
# 2-pair ground state. This requires the 2-pair sector.

# BUILD the 2-pair sector Hamiltonian
from itertools import combinations

def build_npair_hamiltonian(eps, V_mat, N_pair_target):
    """Build the BCS Hamiltonian in the N_pair sector."""
    N_modes = len(eps)
    # Basis: all ways to choose N_pair_target modes from N_modes
    basis = list(combinations(range(N_modes), N_pair_target))
    dim = len(basis)
    H = np.zeros((dim, dim))

    for a, state_a in enumerate(basis):
        # Diagonal: sum of 2*eps_k for occupied modes
        for k in state_a:
            H[a, a] += 2.0 * eps[k]
        # Off-diagonal: pair scattering V_{kk'} moves pair from k to k'
        for k in state_a:
            for kp in range(N_modes):
                if kp in state_a:
                    continue  # k' must be unoccupied
                # New state: replace k with k'
                new_state = tuple(sorted(set(state_a) - {k} | {kp}))
                if new_state in basis:
                    b = basis.index(new_state)
                    H[a, b] -= V_mat[kp, k]

    return H, basis

print("\n  Building 2-pair Hamiltonian...")
H_2pair, basis_2pair = build_npair_hamiltonian(eps_fold, V_fold, 2)
E_2pair, V_2pair = eigh(H_2pair)
psi_GS_2 = V_2pair[:, 0]  # Ground state of 2-pair sector
E_GS_2 = E_2pair[0]

print(f"  2-pair sector: dim = {len(basis_2pair)}")
print(f"  E_GS(N=2) = {E_GS_2:.10f} M_KK")

# Pair transfer operator: S_+ |1, state_a> -> |2, state_b>
# where state_b = state_a + {k'} for some k' not in state_a
# S_+ = sum_{k'} c^+_{k', cell2}  (creates pair in ANY unoccupied mode)

# For each 1-pair eigenstate |1,n>, compute <2,GS| S_+ |1,n>
S_plus_matrix = np.zeros(N)  # <2,GS| S_+ |1,n> for n = 0,...,7

basis_1pair = list(range(N))  # 1-pair basis = individual modes

for n in range(N):
    # Eigenstate |1,n> in mode basis
    psi_n = V_pair[:, n]

    # S_+ |1,n> = sum over modes k (occupied in |1,n>) and k' (unoccupied)
    # We create a pair in mode k' to get a 2-pair state
    overlap = 0.0  # (local)
    for a, k in enumerate(basis_1pair):
        coeff_a = psi_n[a]  # amplitude for mode k in eigenstate n
        # Creating a pair in any unoccupied mode k':
        for kp in range(N):
            if kp == k:
                continue  # k' must be different from k
            # New 2-pair state: (k, k') with k < k'
            new_state = tuple(sorted([k, kp]))
            if new_state in basis_2pair:
                b = basis_2pair.index(new_state)
                # Phase convention: + for k < k'
                overlap += coeff_a * psi_GS_2[b]

    S_plus_matrix[n] = abs(overlap)

print(f"\n  Pair transfer amplitudes |<2,GS|S_+|1,n>|:")
for n in range(N):
    print(f"    n={n}: |S_+(n)| = {S_plus_matrix[n]:.10f}")

# S_+(GGE) = Tr[rho_GGE * S_+]
# In the energy eigenbasis: S_+(GGE) = sum_n rho_nn * S_+(n)
# But we need the MATRIX ELEMENT, not the expectation value.
# The pair transfer AMPLITUDE from the GGE mixed state:
# |S_+(GGE)|^2 = sum_{n,m} rho_GGE(n,m) * S_+(n) * S_+(m)*
# For a diagonal GGE: |S_+(GGE)|^2 = sum_n rho_nn * |S_+(n)|^2

# GGE weights in the energy eigenbasis
rho_diag_GGE_renorm = rho_diag_GGE / np.sum(rho_diag_GGE)  # normalize

# Incoherent average (diagonal GGE):
S_plus_sq_GGE_incoh = np.sum(rho_diag_GGE_renorm * S_plus_matrix**2)
S_plus_GGE_incoh = np.sqrt(S_plus_sq_GGE_incoh)

# Coherent average (off-diagonal GGE contributions):
# S_+(GGE) = |sum_n sqrt(rho_nn) * S_+(n) * e^{i*phi_n}|
# For the GGE with real density matrix, phases are 0 or pi.
# Most conservative: full coherence
S_plus_GGE_coh = 0.0  # (local)
for n in range(N):
    for m in range(N):
        S_plus_GGE_coh += rho_GGE_eig[n, m] * S_plus_matrix[n] * S_plus_matrix[m]
S_plus_GGE_coh = np.sqrt(abs(S_plus_GGE_coh))

print(f"\n  S_+(GGE) estimates:")
print(f"    Incoherent: sqrt(sum rho_nn * |S_+_n|^2) = {S_plus_GGE_incoh:.10f}")
print(f"    Coherent: sqrt(|sum rho_nm * S_+_n * S_+_m|) = {S_plus_GGE_coh:.10f}")
print(f"    S_+(GS) = {S_plus_matrix[0]:.10f}")
print(f"    S_+(fold, canonical) = {S_plus_1:.10f}")

# D_s(GGE) from Josephson stiffness
D_s_GGE_J_incoh = 2.0 * E_J_fold * S_plus_GGE_incoh
D_s_GGE_J_coh = 2.0 * E_J_fold * S_plus_GGE_coh

print(f"\n  Route 3 results:")
print(f"    D_s(GGE, J-incoh) = 2 * {E_J_fold:.4f} * {S_plus_GGE_incoh:.6f} = {D_s_GGE_J_incoh:.6f} M_KK^2")
print(f"    D_s(GGE, J-coh) = 2 * {E_J_fold:.4f} * {S_plus_GGE_coh:.6f} = {D_s_GGE_J_coh:.6f} M_KK^2")

# ===========================================================================
# STEP 6: Thermal reference and comparison
# ===========================================================================
print("\n--- Step 6: Thermal Reference and Cross-Check ---")

# For a thermal BCS superconductor, the Yosida function gives:
# D_s(T) / D_s(0) = 1 - Y(T/T_c)
# where Y(t) = (2/T_c) * integral_0^inf cosh^{-2}(E/(2T)) * N(E) dE
#
# For the framework, the effective GGE temperature structure:
# T_B2 = 0.668, T_B1 = 0.435, T_B3 = 0.178 (from S43 GGE-TEMP-43)
# These are mode-specific temperatures, not a single temperature.

T_B2 = 0.668  # (local)
T_B1 = 0.435  # (local)
T_B3 = 0.178  # (local)

# Yosida function for thermal comparison
def yosida_D_s(T, Delta, E_modes, V_mat):
    """Compute D_s(T)/D_s(0) from Yosida formula."""
    if T < 1e-10:
        return 1.0
    # BCS quasiparticle energies
    E_qp = np.sqrt(E_modes**2 + Delta**2)
    # Fermi-Dirac at temperature T
    f_k = 1.0 / (1.0 + np.exp(E_qp / T))
    # Normal fraction from quasiparticle excitations
    # rho_n/rho = sum_k f_k * (1 - f_k) * (E_qp_k / E_k)^2 / normalization
    # Simplified: rho_n/rho ~ sum_k 2*f_k / N_modes
    f_n = 2.0 * np.sum(f_k) / len(E_modes)
    return max(0.0, 1.0 - f_n)

# Thermal D_s curve
T_arr = np.linspace(0, 2.0, 200)
D_s_thermal = np.zeros(len(T_arr))
for i, T in enumerate(T_arr):
    D_s_thermal[i] = D_s_fold_JPT * yosida_D_s(T, Delta_0_GL, eps_fold, V_fold)

# Effective GGE temperature (geometric mean of sector temperatures)
T_GGE_eff = (T_B2**4 * T_B1 * T_B3**3) ** (1.0/8)
print(f"  Effective GGE temperature = {T_GGE_eff:.4f} M_KK")
D_s_thermal_at_TGGE = D_s_fold_JPT * yosida_D_s(T_GGE_eff, Delta_0_GL, eps_fold, V_fold)
print(f"  D_s(thermal, T_GGE) = {D_s_thermal_at_TGGE:.6f} M_KK^2")

# ===========================================================================
# STEP 7: Cross-check via BCS anomalous correlator
# ===========================================================================
print("\n--- Step 7: Cross-Check via Anomalous Correlator ---")

# The BCS anomalous average F_k = u_k * v_k * (1 - 2*f_k)
# encodes the pair correlation. The superfluid weight is:
# D_s ~ |sum_k F_k|^2 (integrated anomalous correlator squared)

# For the ground state:
# F_k^GS = u_k * v_k = psi_GS(k) (for N_pair=1, this IS the wavefunction)

# For the GGE state:
# F_k^GGE = u_k * v_k * (1 - 2*f_k^{qp})
# The quasiparticle occupation f_k^{qp} is related to the pair occupation
# via the Bogoliubov transformation.
#
# For the N_pair=1 Richardson-Gaudin model:
# f_k^{qp} = 1 - n_k^{pair} for the occupied mode (k=0 dominant)
#           = n_k^{pair} for unoccupied modes (k>0)
#
# More precisely, the anomalous correlator in the GGE is:
# F_k = sqrt(n_k_GGE * (1 - n_k_GGE))
# This comes from: <c_{-k} c_k> = sqrt(n_k * (1 - n_k)) for a state
# that is a superposition of 0 and 1 pair in mode k.

F_k_GGE = np.sqrt(n_k_GGE * (1.0 - n_k_GGE))
F_k_GS = np.sqrt(n_k_GS * (1.0 - n_k_GS))

# The total anomalous correlator (order parameter)
F_total_GGE = np.sum(F_k_GGE)
F_total_GS = np.sum(F_k_GS)

# Ratio of anomalous correlators
ratio_F = F_total_GGE / F_total_GS

print(f"  Anomalous correlator F_k:")
print(f"  {'Mode':<8} {'F_k(GS)':<14} {'F_k(GGE)':<14} {'Ratio':<10}")
for i in range(N):
    r = F_k_GGE[i] / max(F_k_GS[i], 1e-15) if F_k_GS[i] > 1e-15 else 0.0
    print(f"  {sector_labels[i]:<8} {F_k_GS[i]:<14.10f} {F_k_GGE[i]:<14.10f} {r:<10.6f}")

print(f"\n  Total anomalous correlator:")
print(f"    F(GS) = {F_total_GS:.10f}")
print(f"    F(GGE) = {F_total_GGE:.10f}")
print(f"    Ratio F(GGE)/F(GS) = {ratio_F:.10f}")

# D_s ~ F^2, so
D_s_GGE_F = D_s_fold_JPT * (ratio_F)**2
print(f"    D_s(GGE, anomalous) = D_s(fold) * (F_ratio)^2 = {D_s_GGE_F:.6f} M_KK^2")

# ===========================================================================
# STEP 8: Synthesize all routes and compute derived quantities
# ===========================================================================
print("\n" + "=" * 78)
print("SYNTHESIS: Superfluid Weight in GGE State")
print("=" * 78)

# Collect all D_s(GGE) estimates
D_s_estimates = {
    'Route 1 (current-current)': D_s_GGE_cc,
    'Route 2 (ODLRO two-fluid)': D_s_GGE_2fluid,
    'Route 3a (Josephson incoh)': D_s_GGE_J_incoh,
    'Route 3b (Josephson coh)': D_s_GGE_J_coh,
    'Route 4 (anomalous F)': D_s_GGE_F,
}

print(f"\n  All D_s(GGE) estimates:")
for name, val in D_s_estimates.items():
    ratio = val / D_s_fold_JPT
    status = "PASS" if val > 0.636 else ("FAIL" if val < 0.01 else "INFO")
    print(f"    {name:<30s}: D_s = {val:.6f} M_KK^2  ({ratio:.4f} of fold)  [{status}]")

# The PHYSICAL D_s(GGE) is the ODLRO result (Route 2).
# Reason: in the BCS pair model with N_pair=1, the condensate fraction
# (largest eigenvalue of the one-body density matrix) is the most
# fundamental measure of superfluidity. It directly gives the fraction
# of the system that participates in superflow.
#
# The current-current correlator (Route 1) overcounts because it
# includes the diamagnetic contribution from ALL particles, not just
# the condensate. The Josephson routes (3a,3b) depend on whether the
# GGE preserves coherence.
#
# Route 2 is the Volovik answer: the superfluid density is determined
# by the condensate fraction, period.

D_s_GGE = D_s_GGE_2fluid  # ODLRO route = physical result
print(f"\n  >>> PHYSICAL D_s(GGE) = {D_s_GGE:.6f} M_KK^2 (ODLRO route) <<<")
print(f"  >>> Ratio to fold: {D_s_GGE / D_s_fold_JPT:.6f} <<<")

# London penetration depth
lambda_L_GGE = 1.0 / np.sqrt(max(D_s_GGE, 1e-30))
lambda_L_fold = 1.0 / np.sqrt(D_s_fold_JPT)

print(f"\n  London penetration depth:")
print(f"    lambda_L(fold) = {lambda_L_fold:.6f} M_KK^{{-1}}")
print(f"    lambda_L(GGE) = {lambda_L_GGE:.6f} M_KK^{{-1}}")
print(f"    Ratio lambda_L(GGE)/lambda_L(fold) = {lambda_L_GGE/lambda_L_fold:.6f}")

# GL coherence length
xi_GL_GGE = xi_GL  # Unchanged by GGE (set by pairing interaction, not occupation)

# Ginzburg-Landau parameter kappa
kappa_fold = lambda_L_fold / xi_GL
kappa_GGE = lambda_L_GGE / xi_GL_GGE

print(f"\n  Ginzburg-Landau parameter kappa:")
print(f"    kappa(fold) = {kappa_fold:.6f}")
print(f"    kappa(GGE) = {kappa_GGE:.6f}")
print(f"    Type-I boundary: kappa < 1/sqrt(2) = {1/np.sqrt(2):.6f}")
print(f"    kappa(fold) {'<' if kappa_fold < 1/np.sqrt(2) else '>'} 1/sqrt(2) => {'Type-I' if kappa_fold < 1/np.sqrt(2) else 'Type-II'}")
print(f"    kappa(GGE) {'<' if kappa_GGE < 1/np.sqrt(2) else '>'} 1/sqrt(2) => {'Type-I' if kappa_GGE < 1/np.sqrt(2) else 'Type-II'}")

# Meissner mass
m_M_GGE = np.sqrt(D_s_GGE)
m_M_fold = np.sqrt(D_s_fold_JPT)
print(f"\n  Meissner mass (= photon mass in superconductor):")
print(f"    m_M(fold) = {m_M_fold:.6f} M_KK")
print(f"    m_M(GGE) = {m_M_GGE:.6f} M_KK")

# DM-SM interaction cross-section constraint
# sigma_DM-SM ~ alpha^2 / (m_M^4) for gauge-boson exchange
# In the superconducting phase, the Meissner mass provides a natural
# UV cutoff for gauge interactions. A larger m_M means shorter range
# and smaller cross-section.
# sigma(GGE) / sigma(fold) ~ (m_M(fold) / m_M(GGE))^4
ratio_sigma = (m_M_fold / m_M_GGE)**4
print(f"\n  DM-SM interaction constraint:")
print(f"    sigma(GGE) / sigma(fold) = (m_fold/m_GGE)^4 = {ratio_sigma:.6f}")
if D_s_GGE > 0.636:
    print(f"    Meissner screening PERSISTS => DM-SM decoupled")
else:
    print(f"    Meissner screening WEAKENED => DM-SM partially coupled")

# Superfluid fraction
rho_s_fraction = D_s_GGE / D_s_fold_JPT
print(f"\n  Superfluid fraction: rho_s(GGE)/rho = {rho_s_fraction:.6f}")
print(f"  Normal fraction: rho_n(GGE)/rho = {1 - rho_s_fraction:.6f}")

# ===========================================================================
# STEP 9: Current-current correlator as function of q
# ===========================================================================
print("\n--- Step 9: Meissner kernel K(q) ---")

# The Meissner kernel K(q) = D_dia - Pi(q)
# For the 32-cell lattice, momentum takes discrete values
# q = 2*pi*n / L where L = 32^{1/3} ~ 3.17 in 1D equivalent

N_q = 50
q_arr = np.linspace(0, PI, N_q)

# Model the q-dependence of the paramagnetic bubble
# Pi(q) = Pi(0) * cos^2(q * xi_BCS)  (BCS coherence length cutoff)
# This is the standard BCS result: the paramagnetic response is suppressed
# at q > 1/xi_BCS because the Cooper pair wavefunction extends over xi_BCS.

K_q_GGE = np.zeros(N_q)
K_q_GS = np.zeros(N_q)
K_q_thermal = np.zeros(N_q)

# Effective Pi values
Pi_GGE_eff = D_dia - D_s_GGE  # from our Route 2 result
Pi_GS_eff = D_dia - D_s_fold_JPT

for i, q in enumerate(q_arr):
    form_factor = np.exp(-0.5 * (q * xi_BCS)**2)  # Gaussian envelope from BCS coherence
    K_q_GGE[i] = D_dia - Pi_GGE_eff * form_factor
    K_q_GS[i] = D_dia - Pi_GS_eff * form_factor
    K_q_thermal[i] = D_dia - (D_dia - D_s_thermal_at_TGGE) * form_factor

# ===========================================================================
# STEP 10: Lambda_xx correlator for GGE vs thermal
# ===========================================================================
print("\n--- Step 10: Lambda_xx(q) for GGE vs Thermal ---")

# Lambda_xx(q, omega=0) = D_dia - Pi(q, 0)
# At q=0: Lambda_xx = D_s (superfluid weight)
# At large q: Lambda_xx -> D_dia (diamagnetic contribution only)

Lambda_xx_GGE = K_q_GGE  # same as Meissner kernel
Lambda_xx_GS = K_q_GS
Lambda_xx_thermal = K_q_thermal

print(f"  Lambda_xx(q=0, GGE) = {Lambda_xx_GGE[0]:.6f} M_KK^2")
print(f"  Lambda_xx(q=0, GS) = {Lambda_xx_GS[0]:.6f} M_KK^2")
print(f"  Lambda_xx(q=inf, all) -> D_dia = {D_dia:.6f} M_KK^2")

# ===========================================================================
# GATE VERDICT
# ===========================================================================
print("\n" + "=" * 78)
print("GATE VERDICT: MEISSNER-GGE-62")
print("=" * 78)

threshold_PASS = 0.636  # 10% of fold
threshold_FAIL = 0.01

if D_s_GGE > threshold_PASS:
    verdict = "PASS"
    verdict_detail = (
        f"D_s(GGE) = {D_s_GGE:.4f} M_KK^2 > {threshold_PASS} (threshold). "
        f"Ratio to fold = {D_s_GGE/D_s_fold_JPT:.4f}. "
        f"Meissner effect SURVIVES transit. "
        f"lambda_L(GGE) = {lambda_L_GGE:.4f} M_KK^{{-1}}. "
        f"kappa(GGE) = {kappa_GGE:.4f} ({'Type-I' if kappa_GGE < 1/np.sqrt(2) else 'Type-II'}). "
        f"ODLRO condensate fraction = {n_condensate_GGE:.4f}."
    )
elif D_s_GGE < threshold_FAIL:
    verdict = "FAIL"
    verdict_detail = (
        f"D_s(GGE) = {D_s_GGE:.6f} M_KK^2 < {threshold_FAIL} (threshold). "
        f"Meissner effect DESTROYED by transit. "
        f"ODLRO condensate fraction = {n_condensate_GGE:.6f}."
    )
else:
    verdict = "INFO"
    verdict_detail = (
        f"D_s(GGE) = {D_s_GGE:.4f} M_KK^2 in [{threshold_FAIL}, {threshold_PASS}]. "
        f"Meissner effect PARTIALLY SURVIVES. "
        f"Ratio to fold = {D_s_GGE/D_s_fold_JPT:.4f}. "
        f"lambda_L(GGE) = {lambda_L_GGE:.4f} M_KK^{{-1}}. "
        f"kappa(GGE) = {kappa_GGE:.4f} ({'Type-I' if kappa_GGE < 1/np.sqrt(2) else 'Type-II'}). "
        f"ODLRO condensate fraction = {n_condensate_GGE:.4f}."
    )

print(f"\n  Gate: MEISSNER-GGE-62")
print(f"  Verdict: {verdict}")
print(f"  Detail: {verdict_detail}")

# ===========================================================================
# STEP 11: Save data
# ===========================================================================
print("\n--- Step 11: Save results ---")

outpath = os.path.join(SCRIPT_DIR, 's62_meissner_gge.npz')
np.savez(outpath,
    # Gate
    gate_name='MEISSNER-GGE-62',
    gate_verdict=verdict,
    gate_detail=verdict_detail,
    # Primary result
    D_s_GGE=D_s_GGE,
    D_s_fold=D_s_fold_JPT,
    ratio_Ds=D_s_GGE / D_s_fold_JPT,
    # All routes
    D_s_GGE_cc=D_s_GGE_cc,
    D_s_GGE_2fluid=D_s_GGE_2fluid,
    D_s_GGE_J_incoh=D_s_GGE_J_incoh,
    D_s_GGE_J_coh=D_s_GGE_J_coh,
    D_s_GGE_F=D_s_GGE_F,
    # Condensate fraction
    n_condensate_GGE=n_condensate_GGE,
    n_condensate_GS=evals_rho1_GS[0],
    rho_1_evals_GGE=evals_rho1_sorted,
    # Derived quantities
    lambda_L_GGE=lambda_L_GGE,
    lambda_L_fold=lambda_L_fold,
    kappa_GGE=kappa_GGE,
    kappa_fold=kappa_fold,
    m_M_GGE=m_M_GGE,
    m_M_fold=m_M_fold,
    xi_GL_GGE=xi_GL_GGE,
    # Cross-section ratio
    ratio_sigma=ratio_sigma,
    # q-dependent quantities
    q_arr=q_arr,
    K_q_GGE=K_q_GGE,
    K_q_GS=K_q_GS,
    K_q_thermal=K_q_thermal,
    Lambda_xx_GGE=Lambda_xx_GGE,
    Lambda_xx_GS=Lambda_xx_GS,
    Lambda_xx_thermal=Lambda_xx_thermal,
    # GGE data echoed
    n_k_GGE=n_k_GGE,
    n_k_GS=n_k_GS,
    F_k_GGE=F_k_GGE,
    F_k_GS=F_k_GS,
    # Pair transfer
    S_plus_GGE_incoh=S_plus_GGE_incoh,
    S_plus_GGE_coh=S_plus_GGE_coh,
    S_plus_matrix=S_plus_matrix,
    # Thermal reference
    T_arr=T_arr,
    D_s_thermal=D_s_thermal,
    T_GGE_eff=T_GGE_eff,
    # Paramagnetic
    Pi_GS=Pi_GS,
    Pi_GGE=Pi_GGE,
    D_dia=D_dia,
)
print(f"  Saved to {outpath}")

# ===========================================================================
# STEP 12: Plot
# ===========================================================================
print("\n--- Step 12: Generate plots ---")

fig, axes = plt.subplots(2, 2, figsize=(14, 11))

# --- Panel (a): D_s vs T (thermal) with GGE horizontal line ---
ax = axes[0, 0]
ax.plot(T_arr, D_s_thermal, 'b-', linewidth=2, label=r'$D_s(T)$ thermal BCS')
ax.axhline(y=D_s_GGE, color='r', linewidth=2, linestyle='--', label=f'$D_s$(GGE) = {D_s_GGE:.3f}')
ax.axhline(y=threshold_PASS, color='orange', linewidth=1, linestyle=':', label=f'PASS threshold = {threshold_PASS}')
ax.axhline(y=threshold_FAIL, color='gray', linewidth=1, linestyle=':', label=f'FAIL threshold = {threshold_FAIL}')
ax.axvline(x=T_GGE_eff, color='green', linewidth=1, linestyle='--', alpha=0.6, label=f'$T_{{GGE}}^{{eff}}$ = {T_GGE_eff:.3f}')
ax.set_xlabel(r'$T / M_{KK}$', fontsize=12)
ax.set_ylabel(r'$D_s$ [$M_{KK}^2$]', fontsize=12)
ax.set_title('(a) Superfluid Weight: Thermal vs GGE', fontsize=13)
ax.legend(fontsize=9, loc='upper right')
ax.set_xlim(0, 2.0)
ax.set_ylim(-0.5, D_s_fold_JPT * 1.1)
ax.grid(True, alpha=0.3)

# --- Panel (b): Lambda_xx(q) ---
ax = axes[0, 1]
ax.plot(q_arr, Lambda_xx_GS, 'b-', linewidth=2, label=r'$\Lambda_{xx}(q)$ ground state')
ax.plot(q_arr, Lambda_xx_GGE, 'r--', linewidth=2, label=r'$\Lambda_{xx}(q)$ GGE')
ax.plot(q_arr, Lambda_xx_thermal, 'g-.', linewidth=1.5, label=r'$\Lambda_{xx}(q)$ thermal ($T_{GGE}$)')
ax.axhline(y=D_dia, color='gray', linewidth=1, linestyle=':', alpha=0.5, label=f'$D_{{dia}}$ = {D_dia:.1f}')
ax.set_xlabel(r'$q$ [lattice units]', fontsize=12)
ax.set_ylabel(r'$\Lambda_{xx}(q)$ [$M_{KK}^2$]', fontsize=12)
ax.set_title(r'(b) Current-Current Correlator $\Lambda_{xx}(q)$', fontsize=13)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# --- Panel (c): Meissner kernel K(q) ---
ax = axes[1, 0]
ax.plot(q_arr, K_q_GS, 'b-', linewidth=2, label='$K(q)$ ground state')
ax.plot(q_arr, K_q_GGE, 'r--', linewidth=2, label='$K(q)$ GGE')
ax.plot(q_arr, K_q_thermal, 'g-.', linewidth=1.5, label='$K(q)$ thermal')
ax.axhline(y=threshold_PASS, color='orange', linewidth=1, linestyle=':', label='PASS threshold')
ax.set_xlabel(r'$q$ [lattice units]', fontsize=12)
ax.set_ylabel(r'$K(q)$ [$M_{KK}^2$]', fontsize=12)
ax.set_title('(c) Meissner Kernel $K(q)$', fontsize=13)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# --- Panel (d): GGE occupation + condensate fraction ---
ax = axes[1, 1]
x_modes = np.arange(N)
width = 0.35  # (local)
bars1 = ax.bar(x_modes - width/2, n_k_GS, width, color='blue', alpha=0.7, label='$n_k$ (ground state)')
bars2 = ax.bar(x_modes + width/2, n_k_GGE, width, color='red', alpha=0.7, label='$n_k$ (GGE)')
ax.set_xticks(x_modes)
ax.set_xticklabels(sector_labels, rotation=45, ha='right', fontsize=9)
ax.set_ylabel('Occupation $n_k$', fontsize=12)
ax.set_title(f'(d) Mode Occupations: GS vs GGE', fontsize=13)
ax.set_yscale('log')
ax.set_ylim(1e-6, 2)

# Add condensate fraction text
ax.text(0.02, 0.95, f'$n_{{cond}}$(GGE) = {n_condensate_GGE:.4f}\n'
        f'$D_s$(GGE)/$D_s$(fold) = {D_s_GGE/D_s_fold_JPT:.4f}\n'
        f'Verdict: {verdict}',
        transform=ax.transAxes, fontsize=10, verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plotpath = os.path.join(SCRIPT_DIR, 's62_meissner_gge.png')
plt.savefig(plotpath, dpi=150, bbox_inches='tight')
print(f"  Saved plot to {plotpath}")

# ===========================================================================
# FINAL SUMMARY
# ===========================================================================
elapsed = time.time() - t0
print(f"\n{'=' * 78}")
print(f"MEISSNER-GGE-62 COMPLETE")
print(f"{'=' * 78}")
print(f"  D_s(GGE) = {D_s_GGE:.6f} M_KK^2")
print(f"  D_s(fold) = {D_s_fold_JPT:.6f} M_KK^2")
print(f"  Ratio = {D_s_GGE/D_s_fold_JPT:.6f}")
print(f"  n_condensate(GGE) = {n_condensate_GGE:.6f}")
print(f"  lambda_L(GGE) = {lambda_L_GGE:.6f} M_KK^{{-1}}")
print(f"  kappa(GGE) = {kappa_GGE:.6f} ({'Type-I' if kappa_GGE < 1/np.sqrt(2) else 'Type-II'})")
print(f"  Verdict: {verdict}")
print(f"  Elapsed: {elapsed:.1f} s")
