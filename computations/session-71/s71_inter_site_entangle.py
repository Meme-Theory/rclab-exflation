#!/usr/bin/env python3
"""
S71 INTER-SITE-ENTANGLE-71: Josephson Junction Entanglement Entropy
====================================================================

PHYSICS:
  The A_s Route B from the S70 Hawking workshop requires inter-site
  entanglement entropy across the Josephson junction to contribute to
  the squeeze budget.  This computation measures the von Neumann entropy
  of the reduced density matrix obtained by tracing out one cell of a
  2-cell BCS+Josephson system on CG(24).

  The physical system: 8 BCS modes per cell (4 B2 + 1 B1 + 3 B3),
  connected by Josephson coupling J_C2 = 0.933 M_KK.  The total pair
  number N_pair = 2 (canonical at N=2 filling).

  For a squeezed state with squeeze parameter r, the von Neumann
  entropy of the half-chain reduced density matrix is:
    S_ent = 2*r^2/ln(2)    [in bits, Gaussian limit]  # (local)

  The target squeeze parameter is r_spatial = 0.551 (S70), giving:
    S_predicted = 2 * 0.551^2 / ln(2) = 0.876 bits

  The computation:
    1. Build the 2-cell BCS Hamiltonian at N_pair = 2 (dim = C(16,2) = 120)
    2. Diagonalize to obtain |GS>
    3. Construct the FULL reduced density matrix rho_A = Tr_B(|GS><GS|)
       by partial trace over cell 2 (subsystem B)
    4. Compute S_vN = -Tr(rho_A log_2(rho_A))
    5. Also compute Renyi-2 entropy S_2 = -log_2(Tr(rho_A^2))
    6. Compare S_vN to S_predicted

  Hilbert space structure:
    - 16 pair-mode slots: 8 for cell 1 (indices 0..7), 8 for cell 2 (indices 8..15)
    - N_pair = 2: exactly 2 slots occupied => dim = C(16,2) = 120
    - Cell 1 can have n1 = 0, 1, or 2 pairs
    - After partial trace, rho_A has dimension:
        n1=0: C(8,0)=1, n1=1: C(8,1)=8, n1=2: C(8,2)=28  => total = 37

Gate: INTER-SITE-ENTANGLE-71
  PASS if |S_ent - 2*r_spatial^2/ln(2)| / (2*r_spatial^2/ln(2)) < 0.20
  FAIL if ratio > 3.0 (entanglement and squeeze decoupled)
  INFO if ratio in [0.20, 3.0]

Inputs:
  - computations/_shared/canonical_constants.py
  - computations/session-70/s70_meissner_ed.npz (2-cell ED results, cross-check)
  - computations/session-56/s56_gge_fabric.npz (GGE occupations)
  - computations/session-63/s63_quantum_metric.npz (CG(24) structure)
  - computations/session-60/s60_pair_transfer_n4.npz (BCS Hamiltonian data)
  - computations/session-61/s61_extremal_gge.npz (GGE Lagrange multipliers)

Author: landau-condensed-matter-theorist (Session 71, Wave 1)
Date: 2026-04-09
"""

import os
import sys
import time
import numpy as np
from scipy.linalg import eigh
from itertools import combinations

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

t0 = time.time()

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from canonical_constants import (
    PI, N_cells, tau_fold, T_acoustic,
    E_cond, E_cond_ED_8mode, Delta_BCS, Delta_0_OES,
    J_C2, J_su2, J_u1,
    N_dof_BCS,
    E_B1, E_B2_mean, E_B3_mean,
)

np.set_printoptions(precision=10, linewidth=140, suppress=True)

print("=" * 78)
print("INTER-SITE-ENTANGLE-71: Josephson Junction Entanglement Entropy")
print("=" * 78)

# ============================================================================
# SECTION 1: LOAD UPSTREAM DATA
# ============================================================================
print("\n--- Section 1: Load upstream data ---")

# BCS Hamiltonian data (S60)
pt_data = np.load(os.path.join(SCRIPT_DIR, 's60_pair_transfer_n4.npz'), allow_pickle=True)
eps_fold = pt_data['eps_fold']      # 8 single-particle energies at fold
V_fold = pt_data['V_fold']          # 8x8 pairing interaction matrix
E_J_fold = float(pt_data['E_J_fold'])

# GGE Lagrange multipliers (S61)
gge_data = np.load(os.path.join(SCRIPT_DIR, 's61_extremal_gge.npz'), allow_pickle=True)
n_k_GGE = gge_data['n_k_crit']
lambda_k = gge_data['lambda_k_crit']

# Cross-check data (S70 Meissner)
s70_data = np.load(os.path.join(SCRIPT_DIR, 's70_meissner_ed.npz'), allow_pickle=True)
rho1_evals_GS_s70 = s70_data['rho1_evals_GS']    # pair density matrix eigenvalues
rho1_evals_GGE_s70 = s70_data['rho1_evals_GGE']

# S56 GGE fabric
fab_data = np.load(os.path.join(SCRIPT_DIR, 's56_gge_fabric.npz'), allow_pickle=True)
evals_fold_fab = fab_data['evals_fold']

N = N_dof_BCS  # = 8 modes
sector_labels = ['B2[0]', 'B2[1]', 'B2[2]', 'B2[3]', 'B1[0]', 'B3[0]', 'B3[1]', 'B3[2]']

# Squeeze parameter from S70 Hawking workshop
r_spatial = 0.551  # (local)
S_predicted = 2.0 * r_spatial**2 / np.log(2.0)

print(f"  N_modes = {N}")
print(f"  T_acoustic = {T_acoustic:.4f} M_KK")
print(f"  E_J_fold = {E_J_fold:.6f} M_KK")
print(f"  Delta_BCS = {Delta_BCS:.6f} M_KK")
print(f"  J_C2 = {J_C2:.3f} M_KK (canonical)")
print(f"  r_spatial = {r_spatial:.3f} (S70)")
print(f"  S_predicted = 2*r^2/ln(2) = {S_predicted:.6f} bits")
print(f"\n  Single-particle energies eps_fold:")
for i in range(N):
    print(f"    {sector_labels[i]}: eps = {eps_fold[i]:.10f} M_KK")
print(f"\n  GGE occupation numbers:")
for i in range(N):
    print(f"    {sector_labels[i]}: n_k = {n_k_GGE[i]:.10e}")
print(f"\n  S70 pair density matrix eigenvalues (cross-check):")
print(f"    GS:  {rho1_evals_GS_s70}")
print(f"    GGE: {rho1_evals_GGE_s70}")

# ============================================================================
# SECTION 2: BUILD THE 2-CELL FOCK SPACE
# ============================================================================
print("\n--- Section 2: Build 2-cell Fock space ---")

# 16 pair-mode slots: 0..7 = cell 1, 8..15 = cell 2
# N_pair = 2: exactly 2 slots occupied
N_slots = 2 * N  # = 16
N_pair_sector = 2
basis_tuples = list(combinations(range(N_slots), N_pair_sector))
dim = len(basis_tuples)

basis = [np.zeros(N_slots, dtype=int) for _ in range(dim)]
for i, combo in enumerate(basis_tuples):
    for c in combo:
        basis[i][c] = 1
basis_lookup = {tuple(b): i for i, b in enumerate(basis)}

# Classify each basis state by pair count on cell 1
n1_of_state = np.array([sum(basis[i][:N]) for i in range(dim)])

print(f"  N_slots = {N_slots}")
print(f"  N_pair_sector = {N_pair_sector}")
print(f"  Hilbert space dimension = C({N_slots},{N_pair_sector}) = {dim}")
print(f"  States with n1=0: {np.sum(n1_of_state == 0)}")
print(f"  States with n1=1: {np.sum(n1_of_state == 1)}")
print(f"  States with n1=2: {np.sum(n1_of_state == 2)}")

# Build the cell-1 basis for the reduced density matrix
# This is the set of all pair occupations on cell 1 consistent with n1 = 0,1,2
# n1=0: 1 state (all empty)
# n1=1: C(8,1) = 8 states
# n1=2: C(8,2) = 28 states
# Total: 37

cell1_basis_0 = [tuple(np.zeros(N, dtype=int))]   # 1 state
cell1_basis_1 = []
for k in range(N):
    s = np.zeros(N, dtype=int)
    s[k] = 1
    cell1_basis_1.append(tuple(s))
cell1_basis_2 = []
for k1, k2 in combinations(range(N), 2):
    s = np.zeros(N, dtype=int)
    s[k1] = 1
    s[k2] = 1
    cell1_basis_2.append(tuple(s))

cell1_basis_all = cell1_basis_0 + cell1_basis_1 + cell1_basis_2
dim_A = len(cell1_basis_all)
cell1_lookup = {s: i for i, s in enumerate(cell1_basis_all)}

print(f"\n  Cell 1 reduced Hilbert space dimension = {dim_A}")
print(f"    n1=0: {len(cell1_basis_0)} states")
print(f"    n1=1: {len(cell1_basis_1)} states")
print(f"    n1=2: {len(cell1_basis_2)} states")

# ============================================================================
# SECTION 3: BUILD 2-CELL BCS HAMILTONIAN
# ============================================================================
print("\n--- Section 3: Build 2-cell BCS Hamiltonian ---")

def build_H_2cell(eps, V_pair_mat, E_J_val, n_modes, dim_H, basis_list, lookup):
    """
    Build 2-cell BCS Hamiltonian in N_pair=2 sector at phi=0.

    H = H_kinetic + H_pairing(cell1) + H_pairing(cell2) + H_Josephson

    Kinetic: sum_k 2*eps_k * n_k  (for each cell)
    Pairing: -V_{kk'} P^+_k P_{k'}  (within each cell)
    Josephson: -E_J * sum_k (P^+_{k,1} P_{k,2} + h.c.)

    At phi=0, the Hamiltonian is real symmetric.
    """
    H = np.zeros((dim_H, dim_H), dtype=np.float64)

    for idx in range(dim_H):
        state = tuple(basis_list[idx])

        # --- Diagonal: kinetic energy ---
        E_kin = 0.0  # (local)
        for k in range(n_modes):
            if state[k] == 1:           # cell 1
                E_kin += 2.0 * eps[k]
            if state[k + n_modes] == 1:  # cell 2
                E_kin += 2.0 * eps[k]
        H[idx, idx] += E_kin

        # --- Intra-cell pairing: -V_{kk'} P^+_k P_{k'} ---
        for cell in [0, 1]:
            offset = cell * n_modes
            for k in range(n_modes):
                for kp in range(n_modes):
                    if k == kp:
                        continue
                    if state[offset + kp] == 1 and state[offset + k] == 0:
                        ns = list(state)
                        ns[offset + kp] = 0
                        ns[offset + k] = 1
                        nst = tuple(ns)
                        if nst in lookup:
                            H[idx, lookup[nst]] += -V_pair_mat[k, kp]

        # --- Inter-cell Josephson: -E_J * P^+_{k,1} P_{k,2} + h.c. ---
        for k in range(n_modes):
            k1 = k
            k2 = k + n_modes
            # Transfer from cell 2 to cell 1
            if state[k2] == 1 and state[k1] == 0:
                ns = list(state)
                ns[k2] = 0
                ns[k1] = 1
                nst = tuple(ns)
                if nst in lookup:
                    H[idx, lookup[nst]] += -E_J_val
            # Transfer from cell 1 to cell 2 (h.c.)
            if state[k1] == 1 and state[k2] == 0:
                ns = list(state)
                ns[k1] = 0
                ns[k2] = 1
                nst = tuple(ns)
                if nst in lookup:
                    H[idx, lookup[nst]] += -E_J_val

    # Symmetrize (should already be symmetric, but enforce)
    H = 0.5 * (H + H.T)
    return H


H_bcs = build_H_2cell(eps_fold, V_fold, E_J_fold, N, dim, basis, basis_lookup)

# Also build bare Hamiltonian (no pairing)
V_zero = np.zeros((N, N))
H_bare = build_H_2cell(eps_fold, V_zero, E_J_fold, N, dim, basis, basis_lookup)

# Verify Hermiticity
asym_bcs = np.max(np.abs(H_bcs - H_bcs.T))
asym_bare = np.max(np.abs(H_bare - H_bare.T))
print(f"  Hermiticity check: max|H - H^T| = {asym_bcs:.2e} (BCS), {asym_bare:.2e} (bare)")

# Diagonalize
evals_bcs, evecs_bcs = eigh(H_bcs)
evals_bare, evecs_bare = eigh(H_bare)

E_GS_bcs = evals_bcs[0]
E_GS_bare = evals_bare[0]
gap_bcs = evals_bcs[1] - evals_bcs[0]
gap_bare = evals_bare[1] - evals_bare[0]

print(f"\n  BCS ground state energy:   E_0 = {E_GS_bcs:.10f} M_KK")
print(f"  BCS first excited state:   E_1 = {evals_bcs[1]:.10f} M_KK")
print(f"  BCS spectral gap:          Delta = {gap_bcs:.10f} M_KK")
print(f"  Bare ground state energy:  E_0 = {E_GS_bare:.10f} M_KK")
print(f"  Bare spectral gap:         Delta = {gap_bare:.10f} M_KK")

# Cross-check against S70 data
E_GS_s70 = float(s70_data['evals_bcs'][0])
print(f"\n  Cross-check vs S70: E_GS(here) = {E_GS_bcs:.10f}, E_GS(S70) = {E_GS_s70:.10f}")
print(f"  Difference: {abs(E_GS_bcs - E_GS_s70):.2e} (should be machine epsilon)")

# ============================================================================
# SECTION 4: PARTIAL TRACE -- FULL REDUCED DENSITY MATRIX
# ============================================================================
print("\n--- Section 4: Full reduced density matrix by partial trace ---")

def partial_trace_cell2(psi, n_modes, basis_list, dim_H, cell1_basis_all_list, cell1_lu):
    """
    Compute rho_A = Tr_B(|psi><psi|) where A = cell 1, B = cell 2.

    For each pair of basis states |s> and |s'> that agree on cell 2
    but differ on cell 1, the matrix element is:
        rho_A[a, a'] = sum_{b} psi[s(a,b)]^* psi[s(a',b)]

    where s(a,b) is the full state with cell 1 config a and cell 2 config b.

    Parameters:
        psi: state vector in the 2-cell N_pair sector (length dim_H)
        n_modes: number of modes per cell (8)
        basis_list: list of basis state arrays
        dim_H: Hilbert space dimension
        cell1_basis_all_list: list of cell-1 basis state tuples
        cell1_lu: lookup dict mapping cell-1 tuple -> index in rho_A

    Returns:
        rho_A: reduced density matrix for cell 1 (dim_A x dim_A)
    """
    dim_A = len(cell1_basis_all_list)
    rho_A = np.zeros((dim_A, dim_A), dtype=np.float64)

    # Group full-space basis states by their cell-2 configuration
    # For each cell-2 config b, collect all (a_index, full_index) pairs
    cell2_groups = {}
    for idx_full in range(dim_H):
        state = basis_list[idx_full]
        cell1_config = tuple(state[:n_modes])
        cell2_config = tuple(state[n_modes:])

        if cell1_config not in cell1_lu:
            continue  # should not happen

        a_idx = cell1_lu[cell1_config]
        if cell2_config not in cell2_groups:
            cell2_groups[cell2_config] = []
        cell2_groups[cell2_config].append((a_idx, idx_full))

    # Partial trace: rho_A[a, a'] = sum_b psi[s(a,b)]^* psi[s(a',b)]
    for b_config, a_list in cell2_groups.items():
        for (a_idx, full_idx) in a_list:
            for (a_idx_p, full_idx_p) in a_list:
                rho_A[a_idx, a_idx_p] += psi[full_idx] * psi[full_idx_p]

    return rho_A


# --- BCS ground state ---
psi_GS = evecs_bcs[:, 0]

# Verify normalization
norm_GS = np.dot(psi_GS, psi_GS)
print(f"  Ground state normalization: <GS|GS> = {norm_GS:.15f}")

rho_A_GS = partial_trace_cell2(psi_GS, N, basis, dim, cell1_basis_all, cell1_lookup)

# Verify properties of rho_A
tr_rho = np.trace(rho_A_GS)
sym_check = np.max(np.abs(rho_A_GS - rho_A_GS.T))
print(f"  Tr(rho_A) = {tr_rho:.15f} (should be 1)")
print(f"  Symmetry: max|rho_A - rho_A^T| = {sym_check:.2e}")

# Eigenvalues of rho_A
evals_rhoA_GS = np.sort(np.linalg.eigvalsh(rho_A_GS))[::-1]
# Clean small negative eigenvalues (numerical noise)
evals_rhoA_GS_clean = np.maximum(evals_rhoA_GS, 0.0)
# Renormalize
evals_rhoA_GS_clean /= np.sum(evals_rhoA_GS_clean)

print(f"\n  rho_A eigenvalues (BCS GS), all {dim_A}:")
print(f"    Nonzero (>1e-15): {np.sum(evals_rhoA_GS_clean > 1e-15)}")
for i, ev in enumerate(evals_rhoA_GS_clean):
    if ev > 1e-15:
        print(f"    lambda_{i} = {ev:.12e}")

# --- Bare (no pairing) ground state ---
psi_bare = evecs_bare[:, 0]
rho_A_bare = partial_trace_cell2(psi_bare, N, basis, dim, cell1_basis_all, cell1_lookup)
evals_rhoA_bare = np.sort(np.linalg.eigvalsh(rho_A_bare))[::-1]
evals_rhoA_bare_clean = np.maximum(evals_rhoA_bare, 0.0)
evals_rhoA_bare_clean /= np.sum(evals_rhoA_bare_clean)

print(f"\n  rho_A eigenvalues (bare GS):")
print(f"    Nonzero (>1e-15): {np.sum(evals_rhoA_bare_clean > 1e-15)}")
for i, ev in enumerate(evals_rhoA_bare_clean):
    if ev > 1e-15:
        print(f"    lambda_{i} = {ev:.12e}")

# ============================================================================
# SECTION 5: VON NEUMANN AND RENYI ENTROPIES
# ============================================================================
print("\n--- Section 5: Von Neumann and Renyi entropies ---")

def von_neumann_entropy_bits(evals):
    """S_vN = -sum_i lambda_i * log2(lambda_i) for lambda_i > 0."""
    mask = evals > 1e-30
    return -np.sum(evals[mask] * np.log2(evals[mask]))

def von_neumann_entropy_nats(evals):
    """S_vN = -sum_i lambda_i * ln(lambda_i) for lambda_i > 0."""
    mask = evals > 1e-30
    return -np.sum(evals[mask] * np.log(evals[mask]))

def renyi_2_entropy_bits(evals):
    """S_2 = -log2(sum_i lambda_i^2) = -log2(Tr(rho^2))."""
    purity = np.sum(evals**2)
    return -np.log2(purity) if purity > 0 else np.inf

# BCS ground state entanglement
S_vN_GS_bits = von_neumann_entropy_bits(evals_rhoA_GS_clean)
S_vN_GS_nats = von_neumann_entropy_nats(evals_rhoA_GS_clean)
S_2_GS_bits = renyi_2_entropy_bits(evals_rhoA_GS_clean)
purity_GS = np.sum(evals_rhoA_GS_clean**2)

# Bare ground state entanglement
S_vN_bare_bits = von_neumann_entropy_bits(evals_rhoA_bare_clean)
S_vN_bare_nats = von_neumann_entropy_nats(evals_rhoA_bare_clean)
S_2_bare_bits = renyi_2_entropy_bits(evals_rhoA_bare_clean)
purity_bare = np.sum(evals_rhoA_bare_clean**2)

print(f"  BCS Ground State:")
print(f"    S_vN = {S_vN_GS_bits:.6f} bits = {S_vN_GS_nats:.6f} nats")
print(f"    S_2 (Renyi-2) = {S_2_GS_bits:.6f} bits")
print(f"    Purity Tr(rho^2) = {purity_GS:.10f}")
print(f"    Effective dimension = 1/Tr(rho^2) = {1.0/purity_GS:.4f}")

print(f"\n  Bare (no pairing) Ground State:")
print(f"    S_vN = {S_vN_bare_bits:.6f} bits = {S_vN_bare_nats:.6f} nats")
print(f"    S_2 (Renyi-2) = {S_2_bare_bits:.6f} bits")
print(f"    Purity Tr(rho^2) = {purity_bare:.10f}")
print(f"    Effective dimension = 1/Tr(rho^2) = {1.0/purity_bare:.4f}")

# ============================================================================
# SECTION 6: GGE-WEIGHTED ENTANGLEMENT
# ============================================================================
print("\n--- Section 6: GGE-weighted entanglement entropy ---")

# The GGE density matrix is rho_GGE = sum_n w_n |n><n| where
# w_n = exp(-sum_k lambda_k n_k) / Z
# For the 2-cell system with Josephson coupling, we use the Gibbs
# ensemble rho_GGE = exp(-sum_k lambda_k N_k) / Z where N_k counts
# pairs in mode k (both cells).

# Build rho_GGE in the N_pair=2 sector
# First compute weights for each eigenstate
beta_eff_GGE = lambda_k  # GGE Lagrange multipliers for each mode

# For the 2-cell system, the number operator for mode k is
# N_k = n_{k,cell1} + n_{k,cell2}
def compute_N_k_eigenstate(evec, n_modes, basis_list, dim_H):
    """Compute <psi|N_k|psi> for each mode k (summing both cells)."""
    N_k = np.zeros(n_modes)
    for idx in range(dim_H):
        prob = evec[idx]**2
        state = basis_list[idx]
        for k in range(n_modes):
            N_k[k] += prob * (state[k] + state[k + n_modes])
    return N_k

# Build GGE density operator as thermal mixture of eigenstates
# w_n = exp(-sum_k lambda_k <n|N_k|n>_diag) -- BUT this is wrong
# The GGE is diagonal in the QUASIPARTICLE basis of H, not in the
# occupation number basis. For exact diag, we use:
# rho_GGE = Z^{-1} * exp(-sum_k lambda_k * N_k)  (operator exponential)

# Build sum_k lambda_k * N_k operator in the Fock basis
H_GGE = np.zeros((dim, dim), dtype=np.float64)
for idx in range(dim):
    state = basis[idx]
    energy_GGE = 0.0  # (local)
    for k in range(N):
        energy_GGE += lambda_k[k] * (state[k] + state[k + N])
    H_GGE[idx, idx] = energy_GGE

# NOTE: The GGE conserves INDIVIDUAL mode occupations only for the
# integrable system. With Josephson coupling, the conserved charges
# are the eigenvalues of the FULL Hamiltonian. For the 2-cell system
# with Josephson, the GGE is:
#   rho_GGE = Z^{-1} exp(-beta_GGE * H)
# where beta_GGE = T_acoustic^{-1} if we use the microcanonical temperature.
#
# However, the Richardson-Gaudin integrable GGE for the BCS system uses
# the Gaudin charges. For this computation, I follow the S70 approach:
# thermal state at T_acoustic in the eigenbasis of H_bcs.

beta_acoustic = 1.0 / T_acoustic
boltz_weights = np.exp(-beta_acoustic * (evals_bcs - evals_bcs[0]))
Z_thermal = np.sum(boltz_weights)
probs_thermal = boltz_weights / Z_thermal

print(f"  T_acoustic = {T_acoustic:.4f} M_KK")
print(f"  beta_acoustic = {beta_acoustic:.4f} M_KK^{{-1}}")
print(f"  Z_thermal = {Z_thermal:.6f}")
print(f"  Ground state weight: p_0 = {probs_thermal[0]:.10f}")
print(f"  Sum of weights = {np.sum(probs_thermal):.15f}")

# Entanglement entropy of thermal mixed state
# S_ent(rho_thermal) = S_vN(Tr_B(rho_thermal))
# rho_thermal = sum_n p_n |n><n|
# Tr_B(rho_thermal) = sum_n p_n Tr_B(|n><n|)

rho_A_thermal = np.zeros((dim_A, dim_A), dtype=np.float64)
for n_state in range(dim):
    if probs_thermal[n_state] < 1e-30:
        continue
    psi_n = evecs_bcs[:, n_state]
    rho_A_n = partial_trace_cell2(psi_n, N, basis, dim, cell1_basis_all, cell1_lookup)
    rho_A_thermal += probs_thermal[n_state] * rho_A_n

evals_rhoA_thermal = np.sort(np.linalg.eigvalsh(rho_A_thermal))[::-1]
evals_rhoA_thermal_clean = np.maximum(evals_rhoA_thermal, 0.0)
evals_rhoA_thermal_clean /= np.sum(evals_rhoA_thermal_clean)

S_vN_thermal_bits = von_neumann_entropy_bits(evals_rhoA_thermal_clean)
S_vN_thermal_nats = von_neumann_entropy_nats(evals_rhoA_thermal_clean)
S_2_thermal_bits = renyi_2_entropy_bits(evals_rhoA_thermal_clean)
purity_thermal = np.sum(evals_rhoA_thermal_clean**2)

print(f"\n  Thermal state at T_acoustic:")
print(f"    S_vN = {S_vN_thermal_bits:.6f} bits = {S_vN_thermal_nats:.6f} nats")
print(f"    S_2 (Renyi-2) = {S_2_thermal_bits:.6f} bits")
print(f"    Purity = {purity_thermal:.10f}")

# Entanglement entropy of first excited state (for comparison)
psi_1st = evecs_bcs[:, 1]
rho_A_1st = partial_trace_cell2(psi_1st, N, basis, dim, cell1_basis_all, cell1_lookup)
evals_rhoA_1st = np.sort(np.linalg.eigvalsh(rho_A_1st))[::-1]
evals_rhoA_1st_clean = np.maximum(evals_rhoA_1st, 0.0)
evals_rhoA_1st_clean /= np.sum(evals_rhoA_1st_clean)
S_vN_1st_bits = von_neumann_entropy_bits(evals_rhoA_1st_clean)

print(f"\n  First excited state:")
print(f"    S_vN = {S_vN_1st_bits:.6f} bits")

# ============================================================================
# SECTION 7: COMPARISON WITH SQUEEZE PREDICTION
# ============================================================================
print("\n--- Section 7: Comparison with squeeze prediction ---")

print(f"  Squeeze parameter r_spatial = {r_spatial:.3f}")
print(f"  Predicted S_ent = 2*r^2/ln(2) = {S_predicted:.6f} bits")
print(f"  Computed  S_ent(GS) = {S_vN_GS_bits:.6f} bits")
print(f"  Computed  S_ent(thermal) = {S_vN_thermal_bits:.6f} bits")

# Gate evaluation
deviation_GS = abs(S_vN_GS_bits - S_predicted) / S_predicted
deviation_thermal = abs(S_vN_thermal_bits - S_predicted) / S_predicted

print(f"\n  Deviation (GS): |S_ent - S_pred|/S_pred = {deviation_GS:.4f}")
print(f"  Deviation (thermal): |S_ent - S_pred|/S_pred = {deviation_thermal:.4f}")

# Use GS as the primary measurement (thermal is secondary)
if deviation_GS < 0.20:
    gate_verdict = "PASS"
    gate_detail = (f"PASS: |S_ent - S_pred|/S_pred = {deviation_GS:.4f} < 0.20. "
                   f"S_ent(GS) = {S_vN_GS_bits:.4f} bits vs S_pred = {S_predicted:.4f} bits.")
elif deviation_GS > 3.0:
    gate_verdict = "FAIL"
    gate_detail = (f"FAIL: |S_ent - S_pred|/S_pred = {deviation_GS:.4f} > 3.0. "
                   f"Entanglement and squeeze decoupled.")
else:
    gate_verdict = "INFO"
    gate_detail = (f"INFO: |S_ent - S_pred|/S_pred = {deviation_GS:.4f} in [0.20, 3.0]. "
                   f"S_ent(GS) = {S_vN_GS_bits:.4f} bits vs S_pred = {S_predicted:.4f} bits.")

print(f"\n  Gate INTER-SITE-ENTANGLE-71: {gate_verdict}")
print(f"  {gate_detail}")

# ============================================================================
# SECTION 8: ENTANGLEMENT SPECTRUM AND STRUCTURE
# ============================================================================
print("\n--- Section 8: Entanglement spectrum analysis ---")

# The entanglement spectrum {-ln(lambda_i)} gives the "entanglement Hamiltonian"
# H_ent such that rho_A = exp(-H_ent)
ent_spectrum_GS = []
for ev in evals_rhoA_GS_clean:
    if ev > 1e-30:
        ent_spectrum_GS.append(-np.log(ev))

print(f"  Entanglement spectrum (BCS GS, -ln(lambda_i)):")
for i, xi in enumerate(sorted(ent_spectrum_GS)):
    print(f"    xi_{i} = {xi:.6f}")

# Schmidt number (effective number of entangled states)
schmidt_number = 1.0 / purity_GS
print(f"\n  Schmidt number K = 1/Tr(rho^2) = {schmidt_number:.4f}")
print(f"  (K=1: product state, K>1: entangled, K={dim_A}: maximally entangled)")

# Effective squeeze parameter r_eff extracted from entanglement
# For a two-mode squeezed state with parameter r:
#   lambda_n = (1 - tanh^2(r)) * tanh^{2n}(r)
#   S_vN = cosh^2(r) * log_2(cosh^2(r)) - sinh^2(r) * log_2(sinh^2(r))
# In the Gaussian limit (large r or small r):
#   S_vN ~ 2*r^2/ln(2) for small r
#   S_vN ~ 2*r/ln(2) - log_2(e)/2 for large r

# Invert S_vN = cosh^2(r) * log2(cosh^2(r)) - sinh^2(r) * log2(sinh^2(r))
# to find r from S_vN. Use numerical search.
from scipy.optimize import brentq

def S_vN_squeezed(r_val):
    """Von Neumann entropy (bits) of a two-mode squeezed state with parameter r."""
    if r_val < 1e-10:
        return 0.0
    c2 = np.cosh(r_val)**2
    s2 = np.sinh(r_val)**2
    # Avoid log(0) for r->0
    if s2 < 1e-30:
        return c2 * np.log2(c2)
    return c2 * np.log2(c2) - s2 * np.log2(s2)

# Find r_eff such that S_vN_squeezed(r_eff) = S_vN_GS_bits
try:
    r_eff = brentq(lambda r: S_vN_squeezed(r) - S_vN_GS_bits, 0.01, 5.0)
    print(f"\n  Effective squeeze parameter (from S_vN inversion):")
    print(f"    r_eff = {r_eff:.6f}")
    print(f"    r_spatial (S70) = {r_spatial:.6f}")
    print(f"    ratio r_eff / r_spatial = {r_eff / r_spatial:.4f}")
except Exception as e:
    r_eff = np.nan
    print(f"\n  Could not invert S_vN for r_eff: {e}")

# Also check the Gaussian approximation quality
S_gaussian_from_r_eff = 2.0 * r_eff**2 / np.log(2.0) if not np.isnan(r_eff) else np.nan
print(f"\n  Gaussian approximation quality:")
print(f"    S_exact(r_eff) = {S_vN_squeezed(r_eff):.6f} bits" if not np.isnan(r_eff) else "    N/A")
print(f"    S_gaussian(r_eff) = {S_gaussian_from_r_eff:.6f} bits" if not np.isnan(r_eff) else "    N/A")
print(f"    Gaussian error = {abs(S_gaussian_from_r_eff - S_vN_squeezed(r_eff)):.6f} bits" if not np.isnan(r_eff) else "    N/A")

# ============================================================================
# SECTION 9: CROSS-CHECKS
# ============================================================================
print("\n--- Section 9: Cross-checks ---")

# Cross-check 1: S70 pair density matrix eigenvalues
# The pair density matrix rho_1(k,k') = <P^+_k P_k'> is the 8x8 one-body
# reduced density matrix for PAIRS. Its eigenvalues give the ODLRO.
# This is DIFFERENT from the full reduced density matrix.
# But they must be consistent: the largest eigenvalue of rho_1 should equal
# the largest eigenvalue of rho_A restricted to the n1=1 sector.

# Extract n1=1 block of rho_A
idx_n1_1 = list(range(1, 9))  # indices 1..8 in cell1_basis_all correspond to n1=1
rho_A_n1_1_block = rho_A_GS[np.ix_(idx_n1_1, idx_n1_1)]
evals_n1_1 = np.sort(np.linalg.eigvalsh(rho_A_n1_1_block))[::-1]

print(f"  Cross-check 1: Pair density matrix vs full rho_A")
print(f"    S70 pair density matrix eigenvalues (largest 5):")
for i in range(min(5, len(rho1_evals_GS_s70))):
    print(f"      {rho1_evals_GS_s70[i]:.12e}")
print(f"    n1=1 block of full rho_A (largest 5):")
for i in range(min(5, len(evals_n1_1))):
    print(f"      {evals_n1_1[i]:.12e}")
print(f"    n1=0 block (vacuum): rho_A[0,0] = {rho_A_GS[0,0]:.12e}")
print(f"    n1=2 block trace = {np.trace(rho_A_GS[9:,9:]):.12e}")
print(f"    Sum check: {rho_A_GS[0,0]:.6e} + {np.sum(evals_n1_1):.6e} + {np.trace(rho_A_GS[9:,9:]):.6e} = {rho_A_GS[0,0] + np.sum(evals_n1_1) + np.trace(rho_A_GS[9:,9:]):.10f}")

# Cross-check 2: Entanglement entropy of product state should be zero
# A product state |psi> = |a>|b> has S_ent = 0
# Test with state = both pairs in the same cell (cell 1, modes 0 and 1)
test_psi = np.zeros(dim)
test_state = np.zeros(N_slots, dtype=int)
test_state[0] = 1
test_state[1] = 1
test_idx = basis_lookup.get(tuple(test_state))
if test_idx is not None:
    test_psi[test_idx] = 1.0
    rho_A_test = partial_trace_cell2(test_psi, N, basis, dim, cell1_basis_all, cell1_lookup)
    evals_test = np.sort(np.linalg.eigvalsh(rho_A_test))[::-1]
    S_test = von_neumann_entropy_bits(np.maximum(evals_test, 0))
    print(f"\n  Cross-check 2: Product state entanglement")
    print(f"    State: both pairs in cell 1, modes 0,1")
    print(f"    S_vN = {S_test:.2e} bits (should be 0)")

# Cross-check 3: Maximally entangled state
# Equal superposition of all basis states = maximally mixed rho_A
test_psi_max = np.ones(dim) / np.sqrt(dim)
rho_A_max = partial_trace_cell2(test_psi_max, N, basis, dim, cell1_basis_all, cell1_lookup)
evals_max = np.sort(np.linalg.eigvalsh(rho_A_max))[::-1]
evals_max_clean = np.maximum(evals_max, 0)
evals_max_clean /= np.sum(evals_max_clean)
S_max = von_neumann_entropy_bits(evals_max_clean)
print(f"\n  Cross-check 3: Equal superposition entanglement")
print(f"    S_vN = {S_max:.6f} bits")
print(f"    Maximum possible = log2({dim_A}) = {np.log2(dim_A):.6f} bits")

# Cross-check 4: Dimensional consistency
# S_vN should be bounded: 0 <= S_vN <= log2(dim_A)
S_max_bound = np.log2(dim_A)
print(f"\n  Cross-check 4: Entropy bounds")
print(f"    0 <= S_vN(GS) = {S_vN_GS_bits:.6f} <= log2({dim_A}) = {S_max_bound:.6f} bits")
print(f"    Bound satisfied: {0 <= S_vN_GS_bits <= S_max_bound}")

# Cross-check 5: Parity symmetry
# The 2-cell system with identical cells has Z_2 swap symmetry.
# The ground state should be Z_2-symmetric (even parity).
# This means rho_A = rho_B (cell 1 and cell 2 have identical rho).
# Verify: rho_A(GS) should have identical eigenvalues when computed from cell 2.

# Build cell 2 basis
cell2_basis_0 = [tuple(np.zeros(N, dtype=int))]
cell2_basis_1 = []
for k in range(N):
    s = np.zeros(N, dtype=int)
    s[k] = 1
    cell2_basis_1.append(tuple(s))
cell2_basis_2 = []
for k1, k2 in combinations(range(N), 2):
    s = np.zeros(N, dtype=int)
    s[k1] = 1
    s[k2] = 1
    cell2_basis_2.append(tuple(s))

cell2_basis_all = cell2_basis_0 + cell2_basis_1 + cell2_basis_2
cell2_lookup = {s: i for i, s in enumerate(cell2_basis_all)}

# Partial trace over cell 1
rho_B_GS = np.zeros((dim_A, dim_A), dtype=np.float64)
cell1_groups = {}
for idx_full in range(dim):
    state = basis[idx_full]
    cell1_config = tuple(state[:N])
    cell2_config = tuple(state[N:])
    if cell2_config not in cell2_lookup:
        continue
    b_idx = cell2_lookup[cell2_config]
    if cell1_config not in cell1_groups:
        cell1_groups[cell1_config] = []
    cell1_groups[cell1_config].append((b_idx, idx_full))

for a_config, b_list in cell1_groups.items():
    for (b_idx, full_idx) in b_list:
        for (b_idx_p, full_idx_p) in b_list:
            rho_B_GS[b_idx, b_idx_p] += psi_GS[full_idx] * psi_GS[full_idx_p]

evals_rhoB_GS = np.sort(np.linalg.eigvalsh(rho_B_GS))[::-1]
evals_rhoB_GS_clean = np.maximum(evals_rhoB_GS, 0.0)
evals_rhoB_GS_clean /= np.sum(evals_rhoB_GS_clean)
S_vN_B_bits = von_neumann_entropy_bits(evals_rhoB_GS_clean)

print(f"\n  Cross-check 5: Z_2 parity symmetry")
print(f"    S_vN(cell 1) = {S_vN_GS_bits:.10f} bits")
print(f"    S_vN(cell 2) = {S_vN_B_bits:.10f} bits")
print(f"    Difference = {abs(S_vN_GS_bits - S_vN_B_bits):.2e} (should be ~machine epsilon)")

# ============================================================================
# SECTION 10: ENTANGLEMENT vs J_C2 DEPENDENCE
# ============================================================================
print("\n--- Section 10: Entanglement vs Josephson coupling ---")

# Sweep E_J from 0 to 2*E_J_fold
N_EJ_sweep = 21
EJ_ratios = np.linspace(0.0, 2.0, N_EJ_sweep)
S_vN_sweep = np.zeros(N_EJ_sweep)
S_2_sweep = np.zeros(N_EJ_sweep)

for i_ej, ej_ratio in enumerate(EJ_ratios):
    EJ_val = ej_ratio * E_J_fold
    H_sweep = build_H_2cell(eps_fold, V_fold, EJ_val, N, dim, basis, basis_lookup)
    evals_sw, evecs_sw = eigh(H_sweep)
    psi_sw = evecs_sw[:, 0]
    rho_sw = partial_trace_cell2(psi_sw, N, basis, dim, cell1_basis_all, cell1_lookup)
    ev_sw = np.sort(np.linalg.eigvalsh(rho_sw))[::-1]
    ev_sw = np.maximum(ev_sw, 0.0)
    ev_sw /= np.sum(ev_sw)
    S_vN_sweep[i_ej] = von_neumann_entropy_bits(ev_sw)
    S_2_sweep[i_ej] = renyi_2_entropy_bits(ev_sw)
    if i_ej % 5 == 0 or abs(ej_ratio - 1.0) < 0.05:
        print(f"  E_J/E_J_fold = {ej_ratio:.2f}: S_vN = {S_vN_sweep[i_ej]:.6f} bits")

# ============================================================================
# SECTION 11: PLOT
# ============================================================================
print("\n--- Section 11: Generate plot ---")

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Panel 1: Entanglement spectrum
ax1 = axes[0]
nonzero_GS = evals_rhoA_GS_clean[evals_rhoA_GS_clean > 1e-15]
ax1.bar(range(len(nonzero_GS)), nonzero_GS, color='steelblue', alpha=0.8)
ax1.set_xlabel('Eigenvalue index')
ax1.set_ylabel(r'$\lambda_i$')
ax1.set_title('Entanglement spectrum (BCS GS)')
ax1.set_yscale('log')
ax1.set_ylim(1e-8, 1.0)

# Panel 2: S_vN vs E_J
ax2 = axes[1]
ax2.plot(EJ_ratios * E_J_fold, S_vN_sweep, 'b-o', label=r'$S_{\mathrm{vN}}$', markersize=3)
ax2.plot(EJ_ratios * E_J_fold, S_2_sweep, 'r--s', label=r'$S_2$ (R\'{e}nyi)', markersize=3)
ax2.axhline(S_predicted, color='green', linestyle=':', label=f'$2r^2/\\ln 2 = {S_predicted:.3f}$')
ax2.axvline(E_J_fold, color='gray', linestyle='--', alpha=0.5, label=f'$E_J = {E_J_fold:.2f}$')
ax2.set_xlabel(r'$E_J$ (M$_{\rm KK}$)')
ax2.set_ylabel('Entropy (bits)')
ax2.set_title(r'$S_{\mathrm{ent}}$ vs Josephson coupling')
ax2.legend(fontsize=8)

# Panel 3: Comparison table
ax3 = axes[2]
ax3.axis('off')
table_data = [
    [r'$S_{\mathrm{vN}}$ (GS)', f'{S_vN_GS_bits:.4f} bits'],
    [r'$S_{\mathrm{vN}}$ (thermal)', f'{S_vN_thermal_bits:.4f} bits'],
    [r'$S_{\mathrm{predicted}}$', f'{S_predicted:.4f} bits'],
    [r'$|S - S_{\mathrm{pred}}|/S_{\mathrm{pred}}$', f'{deviation_GS:.4f}'],
    [r'$r_{\mathrm{eff}}$', f'{r_eff:.4f}' if not np.isnan(r_eff) else 'N/A'],
    [r'$r_{\mathrm{spatial}}$', f'{r_spatial:.4f}'],
    [r'$S_2$ (R\'{e}nyi-2)', f'{S_2_GS_bits:.4f} bits'],
    ['Schmidt number', f'{schmidt_number:.4f}'],
    ['Gate', gate_verdict],
]
table = ax3.table(cellText=table_data, colLabels=['Quantity', 'Value'],
                  cellLoc='center', loc='center')
table.auto_set_font_size(False)
table.set_fontsize(9)
table.scale(1.2, 1.5)
ax3.set_title('INTER-SITE-ENTANGLE-71 Summary')

plt.tight_layout()
plt.savefig(os.path.join(SCRIPT_DIR, 's71_inter_site_entangle.png'), dpi=150, bbox_inches='tight')
print(f"  Plot saved to: s71_inter_site_entangle.png")

# ============================================================================
# SECTION 12: SAVE DATA
# ============================================================================
print("\n--- Section 12: Save data ---")

outpath = os.path.join(SCRIPT_DIR, 's71_inter_site_entangle.npz')
np.savez(outpath,
    # Gate
    gate_name=np.array('INTER-SITE-ENTANGLE-71'),
    gate_verdict=np.array(gate_verdict),
    gate_detail=np.array(gate_detail),
    # Primary results
    S_vN_GS_bits=S_vN_GS_bits,
    S_vN_GS_nats=S_vN_GS_nats,
    S_2_GS_bits=S_2_GS_bits,
    S_predicted=S_predicted,
    deviation_GS=deviation_GS,
    r_spatial=r_spatial,
    r_eff=r_eff,
    purity_GS=purity_GS,
    schmidt_number=schmidt_number,
    # rho_A eigenvalues
    evals_rhoA_GS=evals_rhoA_GS_clean,
    evals_rhoA_bare=evals_rhoA_bare_clean,
    evals_rhoA_thermal=evals_rhoA_thermal_clean,
    # Entanglement spectrum
    ent_spectrum_GS=np.array(sorted(ent_spectrum_GS)),
    # Bare and thermal
    S_vN_bare_bits=S_vN_bare_bits,
    S_vN_thermal_bits=S_vN_thermal_bits,
    S_2_bare_bits=S_2_bare_bits,
    S_2_thermal_bits=S_2_thermal_bits,
    # Sweep
    EJ_ratios=EJ_ratios,
    S_vN_sweep=S_vN_sweep,
    S_2_sweep=S_2_sweep,
    # Hamiltonian parameters
    E_J_fold=E_J_fold,
    E_GS_bcs=E_GS_bcs,
    gap_bcs=gap_bcs,
    dim_Hilbert=dim,
    dim_A=dim_A,
    N_modes=N,
)
print(f"  Data saved to: {outpath}")

# ============================================================================
# FINAL SUMMARY
# ============================================================================
elapsed = time.time() - t0
print("\n" + "=" * 78)
print("FINAL SUMMARY: INTER-SITE-ENTANGLE-71")
print("=" * 78)
print(f"  Gate: {gate_verdict}")
print(f"  {gate_detail}")
print(f"")
print(f"  S_vN(GS)       = {S_vN_GS_bits:.6f} bits = {S_vN_GS_nats:.6f} nats")
print(f"  S_predicted     = {S_predicted:.6f} bits (2*r_spatial^2/ln(2), r={r_spatial})")
print(f"  Deviation       = {deviation_GS:.4f}")
print(f"  S_2(Renyi-2)    = {S_2_GS_bits:.6f} bits")
print(f"  r_eff           = {r_eff:.6f}" if not np.isnan(r_eff) else f"  r_eff           = N/A")
print(f"  Schmidt number  = {schmidt_number:.4f}")
print(f"  Purity          = {purity_GS:.10f}")
print(f"  S_vN(bare)      = {S_vN_bare_bits:.6f} bits")
print(f"  S_vN(thermal)   = {S_vN_thermal_bits:.6f} bits")
print(f"  Elapsed time    = {elapsed:.2f} s")
print("=" * 78)
