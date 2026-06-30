#!/usr/bin/env python3
"""
GGE-FABRIC-56: Generalized Gibbs Ensemble on the 2-Cell Josephson-Coupled System
=================================================================================

Characterizes the GGE structure of the 2-cell system after sudden quench.

Physics:
  - The single-cell BCS system (8 modes, 1 pair) has 8 conserved quantities
    (free-particle occupation numbers), producing a non-thermal GGE relic
    with 3 distinct branch temperatures (T_B2=0.668, T_B1=0.435, T_B3=0.178).
  - The 2-cell Josephson-coupled system (16 modes, 2 pairs, dim=120) was
    shown in FABRIC-INTEG-56 to PRESERVE integrability (<r>=0.367, Poisson).
  - Question: What are the conserved quantities of the 2-cell system?
    How many GGE temperatures? Does P_vac change relative to 1-cell?

Method:
  1. Build 2-cell H at tau=0 (initial) and tau_fold (final)
  2. Diagonalize both. Get ground state |GS(tau=0)>.
  3. Project |GS(tau=0)> onto eigenstates of H(tau_fold).
  4. Form diagonal ensemble rho_DE = sum_n |c_n|^2 |n><n|.
  5. Search for conserved quantities by testing commutators of candidate
     operators with H_2cell.
  6. Construct GGE from the conserved quantities.
  7. Compare P_vac_DE and P_vac_GGE.

Gate: GGE-FABRIC-56 (INFO)
  - GGE structure and P_vac comparison.

Author: Volovik Superfluid Universe Theorist (S56)
"""

import numpy as np
from scipy.linalg import eigh
from itertools import combinations
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys
import os
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    tau_fold, E_cond, N_cells, Delta_0_OES, J_C2,
    rho_Lambda_obs, M_KK_gravity
)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
t0 = time.time()

print("=" * 78)
print("GGE-FABRIC-56: GGE on 2-Cell Josephson-Coupled System")
print("=" * 78)

# ============================================================================
# 1. Load data from S54
# ============================================================================
tb_data = np.load(os.path.join(SCRIPT_DIR, 's54_tb_hamiltonian.npz'), allow_pickle=True)
ed_data = np.load(os.path.join(SCRIPT_DIR, 's54_ed_sweep.npz'), allow_pickle=True)

tau_values_tb = tb_data['tau_values']
fold_idx = int(ed_data['fold_idx'])
E_sp_sweep = ed_data['E_sp_sweep']     # (50, 8)
V_bare = ed_data['V_bare_cont']         # (8, 8) pairing interaction

tau_fold_actual = tau_values_tb[fold_idx]
print(f"Fold index: {fold_idx}, tau_fold = {tau_fold_actual:.6f}")

# Single-particle energies
eps_fold = E_sp_sweep[fold_idx].copy()
eps_tau0 = E_sp_sweep[0].copy()
print(f"eps(tau=0): {eps_tau0}")
print(f"eps(fold):  {eps_fold}")

# Symmetrize V
V_fold = (V_bare + V_bare.T) / 2.0
print(f"V_bare max asymmetry: {np.max(np.abs(V_bare - V_bare.T)):.2e}")

# Josephson coupling
J_C2_values = tb_data['J_C2_tau']  # (50,)


def compute_E_J(eps, J_C2_val, Delta=Delta_0_OES):
    """Compute Josephson energy per bond."""
    E_qp = np.sqrt(eps**2 + Delta**2)
    F_anom = np.sum(Delta / (2.0 * E_qp**2))
    E_J = J_C2_val**2 * F_anom
    return E_J


E_J_fold = compute_E_J(eps_fold, J_C2_values[fold_idx])
E_J_tau0 = compute_E_J(eps_tau0, J_C2_values[0])
print(f"E_J(fold) = {E_J_fold:.4f} M_KK")
print(f"E_J(tau=0) = {E_J_tau0:.4f} M_KK")

# ============================================================================
# 2. Build 2-cell Hilbert space
# ============================================================================
N_modes = 8  # (local)
N_pair_total = 2  # (local)
n_modes_total = 2 * N_modes

basis = list(combinations(range(n_modes_total), N_pair_total))
dim = len(basis)
assert dim == 120, f"Expected 120, got {dim}"
basis_dict = {state: idx for idx, state in enumerate(basis)}

print(f"\nHilbert space: C({n_modes_total},{N_pair_total}) = {dim}")


def classify_state(state):
    """Return (n1, n2) pair counts in cell 1 and cell 2."""
    n1 = sum(1 for k in state if k < N_modes)
    n2 = sum(1 for k in state if k >= N_modes)
    return n1, n2


sector_02 = [i for i, s in enumerate(basis) if classify_state(s) == (0, 2)]
sector_11 = [i for i, s in enumerate(basis) if classify_state(s) == (1, 1)]
sector_20 = [i for i, s in enumerate(basis) if classify_state(s) == (2, 0)]
print(f"Sectors: (0,2)={len(sector_02)}, (1,1)={len(sector_11)}, (2,0)={len(sector_20)}")


# ============================================================================
# 3. Build Hamiltonian
# ============================================================================
def build_H_2cell(eps_1, eps_2, V_1, V_2, E_J_coupling, alpha=1.0):
    """
    Build 2-cell BCS Hamiltonian in pair basis.
    H = H_BCS(1) + H_BCS(2) + alpha * H_J
    H_BCS(i) = sum_k 2*eps_k^(i) n_k - sum_{kl} V_{kl} b_k^dag b_l
    H_J = -(E_J/2)(B_1^dag B_2 + h.c.)
    """
    H = np.zeros((dim, dim))

    for i, state_i in enumerate(basis):
        # Diagonal: kinetic + BCS diagonal
        E_kin = 0.0  # (local)
        for k in state_i:
            if k < N_modes:
                E_kin += 2.0 * eps_1[k]
            else:
                E_kin += 2.0 * eps_2[k - N_modes]
        H[i, i] += E_kin

        # BCS off-diagonal within each cell
        for pos, k in enumerate(state_i):
            if k < N_modes:
                cell_offset = 0
                k_local = k
                V_cell = V_1
            else:
                cell_offset = N_modes
                k_local = k - N_modes
                V_cell = V_2

            for l_local in range(N_modes):
                l = l_local + cell_offset
                if l == k:
                    # BCS diagonal: -V_{kk} for occupied k
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

        # Josephson coupling
        if alpha > 0 and E_J_coupling > 0:
            for pos, k in enumerate(state_i):
                if k >= N_modes:
                    # Cell 2 -> Cell 1 transfer
                    for l1 in range(N_modes):
                        if l1 in state_i:
                            continue
                        new_state = list(state_i)
                        new_state[pos] = l1
                        new_state = tuple(sorted(new_state))
                        if new_state in basis_dict:
                            j = basis_dict[new_state]
                            H[i, j] -= alpha * E_J_coupling / 2.0
                else:
                    # Cell 1 -> Cell 2 transfer
                    for l2 in range(N_modes):
                        l = l2 + N_modes
                        if l in state_i:
                            continue
                        new_state = list(state_i)
                        new_state[pos] = l
                        new_state = tuple(sorted(new_state))
                        if new_state in basis_dict:
                            j = basis_dict[new_state]
                            H[i, j] -= alpha * E_J_coupling / 2.0

    H = (H + H.T) / 2.0
    return H


# ============================================================================
# 4. Build number operators for each mode
# ============================================================================
def build_number_operator(mode_idx):
    """Build n_k = b_k^dag b_k in the pair basis (0 or 1)."""
    N_op = np.zeros((dim, dim))
    for i, state_i in enumerate(basis):
        if mode_idx in state_i:
            N_op[i, i] = 1.0
    return N_op


# All 16 mode number operators
n_ops = [build_number_operator(k) for k in range(n_modes_total)]

# Cell-1 and cell-2 total pair numbers
N1_op = sum(n_ops[k] for k in range(N_modes))
N2_op = sum(n_ops[k] for k in range(N_modes, n_modes_total))


# ============================================================================
# 5. Diagonalize at tau=0 and tau_fold
# ============================================================================
print("\n" + "=" * 60)
print("STEP 1: Build and diagonalize Hamiltonians")
print("=" * 60)

# H at tau=0 with Josephson coupling
H_tau0 = build_H_2cell(eps_tau0, eps_tau0, V_fold, V_fold, E_J_tau0, alpha=1.0)
evals_tau0, evecs_tau0 = eigh(H_tau0)
print(f"H(tau=0): E_min={evals_tau0[0]:.6f}, E_max={evals_tau0[-1]:.6f}")
print(f"  Ground state energy = {evals_tau0[0]:.6f} M_KK")

# H at fold with Josephson coupling
H_fold = build_H_2cell(eps_fold, eps_fold, V_fold, V_fold, E_J_fold, alpha=1.0)
evals_fold, evecs_fold = eigh(H_fold)
print(f"H(fold): E_min={evals_fold[0]:.6f}, E_max={evals_fold[-1]:.6f}")
print(f"  Ground state energy = {evals_fold[0]:.6f} M_KK")

# Also build H_fold without Josephson for comparison
H_fold_noJ = build_H_2cell(eps_fold, eps_fold, V_fold, V_fold, 0.0, alpha=0.0)
evals_fold_noJ, evecs_fold_noJ = eigh(H_fold_noJ)
print(f"H(fold, no J): E_min={evals_fold_noJ[0]:.6f}")

# Hermiticity checks
print(f"H(tau=0) hermiticity: {np.max(np.abs(H_tau0 - H_tau0.T)):.2e}")
print(f"H(fold) hermiticity: {np.max(np.abs(H_fold - H_fold.T)):.2e}")

# ============================================================================
# 6. Sudden quench: project GS(tau=0) onto eigenstates at fold
# ============================================================================
print("\n" + "=" * 60)
print("STEP 2: Sudden quench and diagonal ensemble")
print("=" * 60)

gs_tau0 = evecs_tau0[:, 0]  # ground state at tau=0

# Project onto fold eigenstates
c_n = evecs_fold.T @ gs_tau0  # overlap coefficients
p_n = np.abs(c_n)**2          # diagonal ensemble probabilities

# Verify normalization
print(f"Sum |c_n|^2 = {np.sum(p_n):.15f} (should be 1)")
print(f"Max |c_n|^2 = {np.max(p_n):.6f} at n={np.argmax(p_n)}")
print(f"IPR = 1/sum(p_n^2) = {1.0/np.sum(p_n**2):.2f} (effective # states)")

# Energy in the diagonal ensemble
E_DE = np.sum(p_n * evals_fold)
print(f"\nE_DE = {E_DE:.6f} M_KK (energy after quench)")
print(f"E_GS(fold) = {evals_fold[0]:.6f} M_KK (ground state at fold)")
print(f"E_exc = E_DE - E_GS(fold) = {E_DE - evals_fold[0]:.6f} M_KK")
print(f"E_exc/|E_cond_1cell| = {(E_DE - evals_fold[0])/abs(E_cond):.1f}")

# ============================================================================
# 7. Search for conserved quantities
# ============================================================================
print("\n" + "=" * 60)
print("STEP 3: Conserved quantity search")
print("=" * 60)

# For the 2-cell system with Josephson coupling, candidate conserved quantities:
# - Total pair number N_total = N_1 + N_2 (always conserved since H preserves total pair number)
# - Individual mode occupations n_k (these are conserved for free particles)
# - H itself is trivially conserved
# - Single-cell conserved quantities Q_k^(i): these may or may not commute with H_J

# Test [n_k, H_fold] for each mode
print("\nCommutator tests: [n_k, H_fold]")
comm_norms = []
for k in range(n_modes_total):
    comm = n_ops[k] @ H_fold - H_fold @ n_ops[k]
    norm = np.max(np.abs(comm))
    comm_norms.append(norm)

comm_norms = np.array(comm_norms)
print(f"  max|[n_k, H]| for k=0..15: {comm_norms}")
print(f"  All zero? (tol 1e-10): {np.all(comm_norms < 1e-10)}")

# Test [N_1, H_fold] and [N_2, H_fold]
comm_N1 = N1_op @ H_fold - H_fold @ N1_op
comm_N2 = N2_op @ H_fold - H_fold @ N2_op
print(f"\n  |[N_1, H]| = {np.max(np.abs(comm_N1)):.6e}")
print(f"  |[N_2, H]| = {np.max(np.abs(comm_N2)):.6e}")

# Test N_total conservation
N_total_op = N1_op + N2_op
comm_Ntot = N_total_op @ H_fold - H_fold @ N_total_op
print(f"  |[N_total, H]| = {np.max(np.abs(comm_Ntot)):.6e}")

# For the integrable 2-cell system, the conserved quantities are the
# eigenstate projectors P_n = |n><n| -- trivially. But for a GGE,
# we need EXTENSIVE conserved quantities. Since the system is integrable
# (Poisson statistics confirmed), there should be a set.
#
# In Richardson-Gaudin integrable BCS, the conserved quantities are
# R_k = sum_l G_{kl} b_l^dag b_k type operators. But we showed in S43
# that this system is NOT R-G integrable -- the integrability is FREE-PARTICLE
# (the post-transit Hamiltonian is effectively non-interacting).
#
# Key insight from S43 GGE-TEMP-43: the conserved quantities ARE the
# free-particle occupation numbers of the post-transit Hamiltonian's
# eigenstates. For the 2-cell system, these are the eigenstates of
# H_fold at alpha=1. The GGE is therefore the diagonal ensemble itself.

# Build the projectors onto eigenstates of H_fold
# P_n = |n><n| all commute with H_fold by construction
# The GGE = diagonal ensemble when the conserved quantities are P_n

# But we can ask: are there FEWER than dim conserved quantities that are
# physically meaningful? Group by symmetry sectors.

# Test if the system factorizes into independent blocks
# by checking if n_k are good quantum numbers at alpha=1:
print("\nIndividual mode number conservation at alpha=1:")
for k in range(n_modes_total):
    cell = 1 if k < N_modes else 2
    k_local = k if k < N_modes else k - N_modes
    status = "CONSERVED" if comm_norms[k] < 1e-10 else f"BROKEN ({comm_norms[k]:.4f})"
    print(f"  n_{k:2d} (cell {cell}, mode {k_local}): {status}")

# Count conserved individual-mode numbers
n_conserved_modes = np.sum(comm_norms < 1e-10)
n_broken_modes = n_modes_total - n_conserved_modes
print(f"\nConserved mode numbers: {n_conserved_modes}/{n_modes_total}")
print(f"Broken by Josephson coupling: {n_broken_modes}")

# ============================================================================
# 8. Build single-cell BCS Hamiltonians and their eigenstates
# ============================================================================
# For a single cell, the BCS Hamiltonian in the N_pair=1 sector has dim=8
# (one pair in one of 8 modes). Build these.

print("\n" + "=" * 60)
print("STEP 4: Single-cell BCS for comparison")
print("=" * 60)


def build_H_1cell(eps, V):
    """Single-cell BCS Hamiltonian for N_pair=1 on N_modes modes. Dim = N_modes."""
    N = len(eps)
    H1 = np.zeros((N, N))
    for k in range(N):
        H1[k, k] = 2.0 * eps[k] - V[k, k]
        for l in range(N):
            if l != k:
                H1[k, l] = -V[l, k]
    return H1


H_1cell_fold = build_H_1cell(eps_fold, V_fold)
evals_1cell_fold, evecs_1cell_fold = eigh(H_1cell_fold)
print(f"1-cell at fold: E_min={evals_1cell_fold[0]:.6f}, E_max={evals_1cell_fold[-1]:.6f}")
print(f"  E_cond(1-cell) = {evals_1cell_fold[0] - 2*eps_fold[0]:.6f} M_KK")

H_1cell_tau0 = build_H_1cell(eps_tau0, V_fold)
evals_1cell_tau0, evecs_1cell_tau0 = eigh(H_1cell_tau0)
print(f"1-cell at tau=0: E_min={evals_1cell_tau0[0]:.6f}")

# Single-cell quench: GS(tau=0) -> eigenstates at fold
gs_1cell_tau0 = evecs_1cell_tau0[:, 0]
c_1cell = evecs_1cell_fold.T @ gs_1cell_tau0
p_1cell = np.abs(c_1cell)**2
E_DE_1cell = np.sum(p_1cell * evals_1cell_fold)
print(f"\n1-cell diagonal ensemble:")
print(f"  p_k = {p_1cell}")
print(f"  E_DE_1cell = {E_DE_1cell:.6f} M_KK")
print(f"  E_exc_1cell = {E_DE_1cell - evals_1cell_fold[0]:.6f} M_KK")

# ============================================================================
# 9. Construct the GGE for the 2-cell system
# ============================================================================
print("\n" + "=" * 60)
print("STEP 5: GGE construction for 2-cell system")
print("=" * 60)

# The conserved quantities for the 2-cell system:
# Since the Josephson coupling is ISOTROPIC (rank-1 in mode space, as shown
# in FABRIC-INTEG-56), the conserved quantities are combinations of the
# single-cell conserved quantities that commute with H_J.
#
# The Josephson term H_J ~ B_1^dag B_2 + h.c. mixes (n1, n2) sectors.
# Individual cell pair numbers N_1, N_2 are NOT conserved (as tested above).
# But N_total = N_1 + N_2 IS conserved.
#
# For a system where the full H commutes with certain operators, those
# operators' eigenvalues label the GGE. Since the system is integrable,
# the GGE = diagonal ensemble is exact.
#
# Approach: the 120 eigenstate projectors are the maximal set of conserved
# quantities. The GGE with 120 Lagrange multipliers reproduces the diagonal
# ensemble EXACTLY. We can ask whether fewer conserved quantities suffice.

# The diagonal ensemble expectation values
print("Diagonal ensemble properties:")

# <N_1> and <N_2> in the DE
N1_DE = np.sum(p_n * np.array([evecs_fold[:, n].T @ N1_op @ evecs_fold[:, n]
                                for n in range(dim)]))
N2_DE = np.sum(p_n * np.array([evecs_fold[:, n].T @ N2_op @ evecs_fold[:, n]
                                for n in range(dim)]))
print(f"  <N_1>_DE = {N1_DE:.6f}")
print(f"  <N_2>_DE = {N2_DE:.6f}")
print(f"  <N_total>_DE = {N1_DE + N2_DE:.6f} (should be 2)")

# Mode occupations in the DE
nk_DE = np.zeros(n_modes_total)
for k in range(n_modes_total):
    nk_DE[k] = np.sum(p_n * np.array([evecs_fold[:, n].T @ n_ops[k] @ evecs_fold[:, n]
                                       for n in range(dim)]))
print(f"\n  <n_k>_DE:")
for k in range(n_modes_total):
    cell = 1 if k < N_modes else 2
    k_local = k if k < N_modes else k - N_modes
    cons_label = "C" if comm_norms[k] < 1e-10 else "X"
    print(f"    k={k:2d} (cell {cell}, mode {k_local}) [{cons_label}]: {nk_DE[k]:.6f}")
print(f"  Sum <n_k> = {np.sum(nk_DE):.6f} (should be 2)")

# ============================================================================
# 10. GGE temperatures from the conserved quantities
# ============================================================================
print("\n" + "=" * 60)
print("STEP 6: GGE temperatures")
print("=" * 60)

# For modes where n_k IS conserved ([n_k, H] = 0), we can define
# individual GGE temperatures T_k via:
#   <n_k>_DE = 1 / (1 + exp(beta_k * E_k))
# where E_k is the eigenvalue associated with that mode.
#
# For modes where n_k is NOT conserved, the GGE temperature is defined
# through the diagonal ensemble itself.

# First, compute the single-mode energies in the 2-cell eigenbasis
# For each eigenstate |n>, the occupation <n|n_k|n> gives the
# mode-k occupation in that eigenstate.

nk_in_eigenstates = np.zeros((dim, n_modes_total))
for k in range(n_modes_total):
    for n in range(dim):
        nk_in_eigenstates[n, k] = evecs_fold[:, n].T @ n_ops[k] @ evecs_fold[:, n]

# For conserved modes, n_k is diagonal in the eigenbasis: check
print("Mode-eigenstate diagonality check (off-diagonal norm):")
for k in range(n_modes_total):
    # Check if n_k is diagonal in the eigenbasis
    nk_eig = evecs_fold.T @ n_ops[k] @ evecs_fold
    off_diag = np.max(np.abs(nk_eig - np.diag(np.diag(nk_eig))))
    cons = "DIAG" if off_diag < 1e-10 else f"off={off_diag:.4f}"
    print(f"  n_{k:2d}: {cons}")

# Group modes by conservation status
conserved_modes = [k for k in range(n_modes_total) if comm_norms[k] < 1e-10]
broken_modes = [k for k in range(n_modes_total) if comm_norms[k] >= 1e-10]

print(f"\nConserved modes: {conserved_modes}")
print(f"Broken modes: {broken_modes}")

# For conserved modes, define GGE temperature
# The GGE for conserved n_k: rho_GGE = exp(-sum_k beta_k n_k) / Z
# gives <n_k> = 1/(1 + exp(beta_k)) for single-mode
# But in the 2-pair system, the constraint sum n_k = 2 complicates this.

# Instead, work with the full diagonal ensemble.
# The GGE entropy is S_DE = -sum_n p_n ln(p_n)
p_nonzero = p_n[p_n > 1e-30]
S_DE = -np.sum(p_nonzero * np.log(p_nonzero))
S_max = np.log(dim)
print(f"\nDiagonal ensemble entropy:")
print(f"  S_DE = {S_DE:.6f} nats")
print(f"  S_max = ln({dim}) = {S_max:.6f} nats")
print(f"  S_DE/S_max = {S_DE/S_max:.6f}")

# Effective number of participating states
N_eff = np.exp(S_DE)
print(f"  N_eff = exp(S_DE) = {N_eff:.2f}")

# ============================================================================
# 11. Sector-resolved GGE
# ============================================================================
print("\n" + "=" * 60)
print("STEP 7: Sector-resolved GGE analysis")
print("=" * 60)

# Weight of each (n1, n2) sector in the diagonal ensemble
# Each eigenstate has some weight in each sector
sector_weight_in_eigenstates = np.zeros((dim, 3))  # (0,2), (1,1), (2,0)
for n in range(dim):
    v = evecs_fold[:, n]
    sector_weight_in_eigenstates[n, 0] = np.sum(v[sector_02]**2)
    sector_weight_in_eigenstates[n, 1] = np.sum(v[sector_11]**2)
    sector_weight_in_eigenstates[n, 2] = np.sum(v[sector_20]**2)

# DE sector weights
P_sector_DE = np.zeros(3)
for s in range(3):
    P_sector_DE[s] = np.sum(p_n * sector_weight_in_eigenstates[:, s])
print(f"Sector weights in DE: (0,2)={P_sector_DE[0]:.4f}, "
      f"(1,1)={P_sector_DE[1]:.4f}, (2,0)={P_sector_DE[2]:.4f}")
print(f"Sum = {np.sum(P_sector_DE):.6f}")

# Initial state sector weights
gs_sector = np.zeros(3)
gs_sector[0] = np.sum(gs_tau0[sector_02]**2)
gs_sector[1] = np.sum(gs_tau0[sector_11]**2)
gs_sector[2] = np.sum(gs_tau0[sector_20]**2)
print(f"GS(tau=0) sector weights: (0,2)={gs_sector[0]:.4f}, "
      f"(1,1)={gs_sector[1]:.4f}, (2,0)={gs_sector[2]:.4f}")

# ============================================================================
# 12. GGE temperatures from mode occupation inversion
# ============================================================================
print("\n" + "=" * 60)
print("STEP 8: Mode-level GGE temperatures (Fermi-Dirac inversion)")
print("=" * 60)

# For each mode k, the GGE temperature is defined by inverting
# <n_k> = 1/(1 + exp(epsilon_k / T_k))
# This is the standard definition used in S43 GGE-TEMP-43 for the 1-cell system.
# For the 2-cell system, identical modes in cells 1 and 2 should have
# the same T_k by symmetry.

# Mode energies in the 2-cell eigenbasis
# Use the single-particle energies directly
eps_2cell = np.zeros(n_modes_total)
eps_2cell[:N_modes] = eps_fold
eps_2cell[N_modes:] = eps_fold

print(f"\nMode occupations and GGE temperatures:")
print(f"{'Mode':>6} {'Cell':>4} {'k_loc':>5} {'eps_k':>10} {'<n_k>':>10} "
      f"{'T_k':>10} {'beta_k':>10} {'Branch':>8}")

T_k_2cell = np.zeros(n_modes_total)
beta_k_2cell = np.zeros(n_modes_total)

# The single-particle energy for the GGE temperature computation
# is E_k = 2*eps_k - V_kk (the BCS mean-field single-particle energy)
# But actually, in the S43 computation, the GGE temperatures are defined
# differently: T_k = E_k / ln((1-f_k)/f_k) where f_k is the occupation
# and E_k is the quasiparticle energy from the BCS Hamiltonian eigenvalues.
#
# For the 2-cell system, the equivalent is:
# The eigenvalues of H_fold define the energy scale. The mode occupations
# in the DE define the occupation fractions. The GGE temperature per mode
# is then T_k = E_k^eff / ln((1-f_k)/f_k) where E_k^eff is a suitable
# energy scale.
#
# However, the correct approach is: for each conserved n_k, the GGE
# temperature is determined by the MARGINAL distribution.
#
# Since the single-cell BCS 1-pair problem on 8 modes has exactly the
# structure f_k = occupation of mode k, and the Lagrange multiplier
# beta_k satisfies <n_k> = (from GGE partition function), the inversion
# for a single-particle system gives:
#   f_k = 1/(1+exp(beta_k * e_k)) where e_k = 2*eps_k - V_kk
# => beta_k = ln((1-f_k)/f_k) / e_k

# For the 2-cell system with N_total=2, the constraint complicates the
# inversion. Use the approach: compute the reduced density matrix for
# each mode k, and extract T_k from the Boltzmann ratio.

# Alternative: use the pair of cell-1/cell-2 occupation numbers.
# Since the cells are identical, <n_k(cell 1)> = <n_k(cell 2)> by symmetry.
# Each f_k = <n_k> (per mode) should be N_pair/N_modes = 2/16 = 0.125 for
# a thermal state, but the GGE distributes differently.

# The mode-level effective single-particle energies:
# In the 1-cell BCS, the eigenvalues of H_1cell give the energies.
# For the 2-cell system, we use the single-mode energies from the
# diagonal of H in the pair basis.

# Branch labels for the 2-cell modes
branch_labels_2cell = ['B2', 'B2', 'B2', 'B2', 'B1', 'B3', 'B3', 'B3'] * 2

for k in range(n_modes_total):
    cell = 1 if k < N_modes else 2
    k_loc = k if k < N_modes else k - N_modes
    f_k = nk_DE[k]
    e_k = 2.0 * eps_2cell[k] - V_fold[k_loc, k_loc]

    if f_k > 1e-12 and f_k < 1 - 1e-12 and abs(e_k) > 1e-12:
        beta_k = np.log((1.0 - f_k) / f_k) / e_k
        T_k = 1.0 / beta_k if abs(beta_k) > 1e-12 else np.inf
    else:
        beta_k = np.nan
        T_k = np.nan

    T_k_2cell[k] = T_k
    beta_k_2cell[k] = beta_k
    branch = branch_labels_2cell[k]
    print(f"  {k:4d}   {cell:3d}   {k_loc:4d}   {e_k:10.6f}   {f_k:10.6f}   "
          f"{T_k:10.6f}   {beta_k:10.6f}   {branch}")

# Group by branch
T_B2_2cell = np.mean(T_k_2cell[np.array([0,1,2,3,8,9,10,11])])
T_B1_2cell = np.mean(T_k_2cell[np.array([4, 12])])
T_B3_2cell = np.mean(T_k_2cell[np.array([5,6,7,13,14,15])])

print(f"\nBranch-averaged GGE temperatures:")
print(f"  T_B2 (2-cell) = {T_B2_2cell:.6f} M_KK  (1-cell: 0.6675)")
print(f"  T_B1 (2-cell) = {T_B1_2cell:.6f} M_KK  (1-cell: 0.4345)")
print(f"  T_B3 (2-cell) = {T_B3_2cell:.6f} M_KK  (1-cell: 0.1778)")

# ============================================================================
# 13. Vacuum pressure and equation of state
# ============================================================================
print("\n" + "=" * 60)
print("STEP 9: Vacuum pressure and equation of state")
print("=" * 60)

# P_vac = N_pair - E_GGE (Volovik identity, S55)
# For the 2-cell system:
P_vac_2cell = N_pair_total - E_DE
rho_vac_2cell = E_DE  # energy density
w_2cell = P_vac_2cell / rho_vac_2cell if abs(rho_vac_2cell) > 1e-15 else np.nan

print(f"2-cell system:")
print(f"  N_pair = {N_pair_total}")
print(f"  E_DE = {E_DE:.6f} M_KK")
print(f"  P_vac = N_pair - E_DE = {P_vac_2cell:.6f} M_KK")
print(f"  w = P/rho = {w_2cell:.6f}")
print(f"  rho + 3P = {rho_vac_2cell + 3*P_vac_2cell:.6f} M_KK")

# Comparison with 2 isolated cells:
# 2 copies of 1-cell GGE: P_vac = 2 * (1 - E_DE_1cell)
P_vac_2isolated = 2 * (1 - E_DE_1cell)
print(f"\n2 isolated cells:")
print(f"  E_DE(1-cell) = {E_DE_1cell:.6f} M_KK")
print(f"  2 * E_DE(1-cell) = {2*E_DE_1cell:.6f} M_KK")
print(f"  P_vac(2 isolated) = 2*(1 - E_DE_1cell) = {P_vac_2isolated:.6f} M_KK")

# Josephson contribution to P_vac
Delta_P = P_vac_2cell - P_vac_2isolated
print(f"\nJosephson shift:")
print(f"  Delta_P = P_vac(coupled) - P_vac(isolated) = {Delta_P:.6f} M_KK")
print(f"  Delta_P / |P_vac_isolated| = {Delta_P/abs(P_vac_2isolated):.6f}")

# Per-pair quantities for comparison with 1-cell results
E_DE_per_pair = E_DE / N_pair_total
P_vac_per_pair = P_vac_2cell / N_pair_total
w_per_pair = P_vac_per_pair / E_DE_per_pair if abs(E_DE_per_pair) > 1e-15 else np.nan

print(f"\nPer-pair quantities:")
print(f"  E_DE / N_pair = {E_DE_per_pair:.6f} M_KK  (1-cell: 1.688)")
print(f"  P_vac / N_pair = {P_vac_per_pair:.6f} M_KK  (1-cell: -0.688)")
print(f"  w (per pair) = {w_per_pair:.6f}  (1-cell: -0.408)")

# ============================================================================
# 14. GGE entropy and departure from equilibrium
# ============================================================================
print("\n" + "=" * 60)
print("STEP 10: GGE entropy and equilibrium departure")
print("=" * 60)

# Mode-level entropy
S_modes = np.zeros(n_modes_total)
for k in range(n_modes_total):
    f = nk_DE[k]
    if f > 1e-15 and f < 1 - 1e-15:
        S_modes[k] = -f * np.log(f) - (1-f) * np.log(1-f)
    else:
        S_modes[k] = 0.0

S_GGE_2cell = np.sum(S_modes)
S_max_modes = n_modes_total * np.log(2)  # max if all f=0.5

print(f"Mode-level GGE entropy: S_GGE = {S_GGE_2cell:.6f} nats")
print(f"Max mode entropy: S_max = {S_max_modes:.6f} nats")
print(f"S_GGE/S_max = {S_GGE_2cell/S_max_modes:.6f}")
print(f"Diagonal ensemble entropy: S_DE = {S_DE:.6f} nats")

# Euler identity check: sum T_k S_k = ?
Euler_sum = 0.0  # (local)
for k in range(n_modes_total):
    if np.isfinite(T_k_2cell[k]) and np.isfinite(S_modes[k]):
        Euler_sum += T_k_2cell[k] * S_modes[k]
print(f"\nEuler identity check: sum(T_k * S_k) = {Euler_sum:.6f} (should = N_pair = {N_pair_total})")

# Volovik departure
T_mean = np.nanmean(T_k_2cell)
T_valid = T_k_2cell[np.isfinite(T_k_2cell)]
delta_eq = np.max(np.abs(T_valid - T_mean)) / T_mean if abs(T_mean) > 1e-15 else np.nan
print(f"\nVolovik departure delta_eq = {delta_eq:.6f}")
print(f"T_mean = {T_mean:.6f} M_KK")
print(f"T_max/T_min = {np.max(T_valid)/np.min(T_valid):.4f}")

# Non-thermality index
sigma_T = np.std(T_valid)
NT_index = sigma_T / T_mean if abs(T_mean) > 1e-15 else np.nan
print(f"Non-thermality sigma_T/T_mean = {NT_index:.6f}")

# ============================================================================
# 15. Compare with the ground state of H_fold (BCS condensate)
# ============================================================================
print("\n" + "=" * 60)
print("STEP 11: Ground state (BCS condensate) at fold")
print("=" * 60)

# Ground state of 2-cell at fold
gs_fold = evecs_fold[:, 0]
nk_GS = np.zeros(n_modes_total)
for k in range(n_modes_total):
    nk_GS[k] = gs_fold.T @ n_ops[k] @ gs_fold

print(f"Ground state mode occupations:")
for k in range(n_modes_total):
    cell = 1 if k < N_modes else 2
    k_loc = k if k < N_modes else k - N_modes
    print(f"  n_{k:2d} (cell {cell}, mode {k_loc}): GS={nk_GS[k]:.6f}, DE={nk_DE[k]:.6f}")

# GS sector weights
gs_fold_sector = np.zeros(3)
gs_fold_sector[0] = np.sum(gs_fold[sector_02]**2)
gs_fold_sector[1] = np.sum(gs_fold[sector_11]**2)
gs_fold_sector[2] = np.sum(gs_fold[sector_20]**2)
print(f"\nGS(fold) sector: (0,2)={gs_fold_sector[0]:.4f}, "
      f"(1,1)={gs_fold_sector[1]:.4f}, (2,0)={gs_fold_sector[2]:.4f}")

# Condensation energy of 2-cell system
# Compare with 2 isolated cells
E_cond_2cell = evals_fold[0] - evals_fold_noJ[0]
print(f"\nCondensation energies:")
print(f"  E_GS(2-cell, J) = {evals_fold[0]:.6f} M_KK")
print(f"  E_GS(2-cell, no J) = {evals_fold_noJ[0]:.6f} M_KK")
print(f"  Josephson binding = {E_cond_2cell:.6f} M_KK")
print(f"  |E_cond|/|E_cond_1cell| = {abs(E_cond_2cell)/abs(E_cond):.4f}")

# ============================================================================
# 16. Comparison: same quench without Josephson coupling
# ============================================================================
print("\n" + "=" * 60)
print("STEP 12: Quench comparison (with vs without Josephson)")
print("=" * 60)

# Build H(tau=0, no J) ground state
H_tau0_noJ = build_H_2cell(eps_tau0, eps_tau0, V_fold, V_fold, 0.0, alpha=0.0)
evals_tau0_noJ, evecs_tau0_noJ = eigh(H_tau0_noJ)
gs_tau0_noJ = evecs_tau0_noJ[:, 0]

# Project onto H(fold, no J) eigenstates
c_noJ = evecs_fold_noJ.T @ gs_tau0_noJ
p_noJ = np.abs(c_noJ)**2
E_DE_noJ = np.sum(p_noJ * evals_fold_noJ)

P_vac_noJ = N_pair_total - E_DE_noJ
w_noJ = P_vac_noJ / E_DE_noJ

S_DE_noJ = -np.sum(p_noJ[p_noJ > 1e-30] * np.log(p_noJ[p_noJ > 1e-30]))

print(f"No-Josephson quench:")
print(f"  E_DE(no J) = {E_DE_noJ:.6f} M_KK")
print(f"  P_vac(no J) = {P_vac_noJ:.6f} M_KK")
print(f"  w(no J) = {w_noJ:.6f}")
print(f"  S_DE(no J) = {S_DE_noJ:.6f} nats")

print(f"\nWith-Josephson quench:")
print(f"  E_DE(J) = {E_DE:.6f} M_KK")
print(f"  P_vac(J) = {P_vac_2cell:.6f} M_KK")
print(f"  w(J) = {w_2cell:.6f}")
print(f"  S_DE(J) = {S_DE:.6f} nats")

print(f"\nJosephson effect on GGE:")
print(f"  Delta E_DE = {E_DE - E_DE_noJ:.6f} M_KK")
print(f"  Delta P_vac = {P_vac_2cell - P_vac_noJ:.6f} M_KK")
print(f"  Delta w = {w_2cell - w_noJ:.6f}")
print(f"  Delta S_DE = {S_DE - S_DE_noJ:.6f} nats")

# ============================================================================
# 17. CC gap in physical units
# ============================================================================
print("\n" + "=" * 60)
print("STEP 13: CC gap")
print("=" * 60)

M_KK_val = M_KK_gravity  # 7.43e16 GeV
Lambda_2cell = abs(P_vac_2cell) * M_KK_val**4  # GeV^4
CC_gap = Lambda_2cell / rho_Lambda_obs
print(f"  |P_vac(2-cell)| = {abs(P_vac_2cell):.6f} M_KK")
print(f"  M_KK = {M_KK_val:.2e} GeV")
print(f"  Lambda_2cell = {Lambda_2cell:.4e} GeV^4")
print(f"  Lambda_obs = {rho_Lambda_obs:.2e} GeV^4")
print(f"  Lambda/Lambda_obs = {CC_gap:.4e}")
print(f"  log10(gap) = {np.log10(CC_gap):.1f} orders")

# Per-pair: compare with 1-cell
Lambda_1cell = 0.688 * M_KK_val**4
CC_gap_1cell = Lambda_1cell / rho_Lambda_obs
print(f"\n  1-cell: Lambda/Lambda_obs = {CC_gap_1cell:.4e} ({np.log10(CC_gap_1cell):.1f} orders)")

# ============================================================================
# 18. Summary
# ============================================================================
print("\n" + "=" * 78)
print("SUMMARY: GGE-FABRIC-56")
print("=" * 78)

print(f"""
2-cell Josephson-coupled system (dim={dim}, N_pair={N_pair_total}):
  - E_J(fold) = {E_J_fold:.4f} M_KK
  - <r> = 0.367 (Poisson, integrable) [from FABRIC-INTEG-56]

Diagonal Ensemble:
  - E_DE = {E_DE:.6f} M_KK
  - S_DE = {S_DE:.6f} nats (S_DE/ln(120) = {S_DE/np.log(120):.4f})
  - IPR = {1.0/np.sum(p_n**2):.2f} effective states

Vacuum Pressure:
  - P_vac(2-cell) = {P_vac_2cell:.6f} M_KK
  - P_vac(2 isolated) = {P_vac_2isolated:.6f} M_KK
  - Josephson shift = {Delta_P:.6f} M_KK ({100*Delta_P/abs(P_vac_2isolated):.2f}% of isolated)
  - w(2-cell) = {w_2cell:.6f}
  - CC gap: {np.log10(CC_gap):.1f} orders

Conserved Quantities:
  - N_total conserved: YES
  - Individual n_k: {n_conserved_modes}/{n_modes_total} conserved
  - N_1, N_2 individually: {'YES' if np.max(np.abs(comm_N1)) < 1e-10 else 'NO'}

GGE Temperatures (per pair):
  - T_B2 = {T_B2_2cell:.6f} M_KK (1-cell: 0.6675)
  - T_B1 = {T_B1_2cell:.6f} M_KK (1-cell: 0.4345)
  - T_B3 = {T_B3_2cell:.6f} M_KK (1-cell: 0.1778)
  - delta_eq = {delta_eq:.6f} (1-cell: 0.667)
  - Non-thermality = {NT_index:.6f}

Sector Distribution:
  - GS(tau=0): (0,2)={gs_sector[0]:.4f}, (1,1)={gs_sector[1]:.4f}, (2,0)={gs_sector[2]:.4f}
  - DE: (0,2)={P_sector_DE[0]:.4f}, (1,1)={P_sector_DE[1]:.4f}, (2,0)={P_sector_DE[2]:.4f}

Gate Verdict: INFO
  GGE structure computed. Josephson coupling shifts P_vac by {100*Delta_P/abs(P_vac_2isolated):.2f}%.
  CC gap remains at ~{np.log10(CC_gap):.0f} orders.
""")

elapsed = time.time() - t0
print(f"Elapsed: {elapsed:.1f}s")

# ============================================================================
# 19. Save data
# ============================================================================
save_path = os.path.join(SCRIPT_DIR, 's56_gge_fabric.npz')
np.savez(save_path,
    # Hamiltonians
    E_J_fold=E_J_fold,
    E_J_tau0=E_J_tau0,
    eps_fold=eps_fold,
    eps_tau0=eps_tau0,
    V_fold=V_fold,
    dim=dim,
    fold_idx=fold_idx,
    tau_fold_actual=tau_fold_actual,
    # Eigenvalues
    evals_tau0=evals_tau0,
    evals_fold=evals_fold,
    evals_fold_noJ=evals_fold_noJ,
    # Diagonal ensemble
    c_n=c_n,
    p_n=p_n,
    E_DE=E_DE,
    S_DE=S_DE,
    # Mode occupations
    nk_DE=nk_DE,
    nk_GS=nk_GS,
    comm_norms=comm_norms,
    # GGE temperatures
    T_k_2cell=T_k_2cell,
    beta_k_2cell=beta_k_2cell,
    T_B2_2cell=T_B2_2cell,
    T_B1_2cell=T_B1_2cell,
    T_B3_2cell=T_B3_2cell,
    # Vacuum pressure
    P_vac_2cell=P_vac_2cell,
    P_vac_2isolated=P_vac_2isolated,
    Delta_P=Delta_P,
    w_2cell=w_2cell,
    # Sector analysis
    sector_weights_DE=P_sector_DE,
    sector_weights_GS_tau0=gs_sector,
    sector_weights_GS_fold=gs_fold_sector,
    # Without Josephson
    E_DE_noJ=E_DE_noJ,
    P_vac_noJ=P_vac_noJ,
    w_noJ=w_noJ,
    S_DE_noJ=S_DE_noJ,
    # CC gap
    CC_gap=CC_gap,
    # Mode entropies
    S_modes=S_modes,
    S_GGE_2cell=S_GGE_2cell,
    # Single-cell reference
    E_DE_1cell=E_DE_1cell,
    p_1cell=p_1cell,
    # Volovik departure
    delta_eq=delta_eq,
    NT_index=NT_index,
    Euler_sum=Euler_sum,
    # Gate
    gate_verdict='INFO',
    gate_name='GGE-FABRIC-56',
)
print(f"Data saved to {save_path}")

# ============================================================================
# 20. Plot
# ============================================================================
fig, axes = plt.subplots(2, 3, figsize=(18, 11))
fig.suptitle('GGE-FABRIC-56: GGE on 2-Cell Josephson-Coupled System', fontsize=14)

# Panel 1: Diagonal ensemble weights
ax = axes[0, 0]
ax.semilogy(np.arange(dim), np.sort(p_n)[::-1], 'b-', lw=1.5)
ax.axhline(y=1.0/dim, color='r', ls='--', label=f'1/{dim}')
ax.set_xlabel('State index (sorted)', fontsize=11)
ax.set_ylabel('$p_n$', fontsize=11)
ax.set_title('Diagonal Ensemble Weights', fontsize=12)
ax.legend()
ax.grid(True, alpha=0.3)

# Panel 2: Mode occupations
ax = axes[0, 1]
x_pos = np.arange(n_modes_total)
ax.bar(x_pos - 0.15, nk_GS, width=0.3, color='green', alpha=0.7, label='GS(fold)')
ax.bar(x_pos + 0.15, nk_DE, width=0.3, color='blue', alpha=0.7, label='DE')
ax.axhline(y=N_pair_total/n_modes_total, color='r', ls='--',
           label=f'Thermal (f={N_pair_total/n_modes_total:.3f})')
ax.set_xlabel('Mode index', fontsize=11)
ax.set_ylabel('$\\langle n_k \\rangle$', fontsize=11)
ax.set_title('Mode Occupations: GS vs DE', fontsize=12)
ax.legend(fontsize=9)
ax.set_xticks(x_pos)
labels = [f'C1:{k}' for k in range(8)] + [f'C2:{k}' for k in range(8)]
ax.set_xticklabels(labels, rotation=45, fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 3: GGE temperatures
ax = axes[0, 2]
T_valid_plot = T_k_2cell.copy()
T_valid_plot[~np.isfinite(T_valid_plot)] = 0
# 1-cell temperatures for comparison
T_1cell_ref = np.array([0.758, 0.741, 0.610, 0.560, 0.435, 0.175, 0.179, 0.180] * 2)
ax.bar(x_pos - 0.15, T_valid_plot, width=0.3, color='blue', alpha=0.7, label='2-cell')
ax.bar(x_pos + 0.15, T_1cell_ref, width=0.3, color='red', alpha=0.5, label='1-cell ref')
ax.set_xlabel('Mode index', fontsize=11)
ax.set_ylabel('$T_k$ (M_KK)', fontsize=11)
ax.set_title('GGE Temperatures', fontsize=12)
ax.legend(fontsize=9)
ax.set_xticks(x_pos)
ax.set_xticklabels(labels, rotation=45, fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 4: Sector weights
ax = axes[1, 0]
sectors = ['(0,2)', '(1,1)', '(2,0)']
x_sec = np.arange(3)
ax.bar(x_sec - 0.15, gs_sector, width=0.3, color='green', alpha=0.7, label='GS(tau=0)')
ax.bar(x_sec + 0.15, P_sector_DE, width=0.3, color='blue', alpha=0.7, label='DE')
ax.set_xlabel('Sector', fontsize=11)
ax.set_ylabel('Weight', fontsize=11)
ax.set_title('Sector Weights', fontsize=12)
ax.set_xticks(x_sec)
ax.set_xticklabels(sectors)
ax.legend()
ax.grid(True, alpha=0.3)

# Panel 5: P_vac comparison
ax = axes[1, 1]
labels_p = ['1-cell\n(ref)', '2 isolated', '2-cell\n(Josephson)', '2-cell\n(no J quench)']
values_p = [-0.688, P_vac_2isolated, P_vac_2cell, P_vac_noJ]
colors_p = ['gray', 'orange', 'blue', 'red']
ax.bar(np.arange(len(labels_p)), values_p, color=colors_p, alpha=0.7)
ax.set_xticks(np.arange(len(labels_p)))
ax.set_xticklabels(labels_p, fontsize=9)
ax.set_ylabel('$P_{vac}$ (M_KK)', fontsize=11)
ax.set_title('Vacuum Pressure Comparison', fontsize=12)
ax.axhline(y=0, color='k', ls='-', lw=0.5)
ax.grid(True, alpha=0.3)

# Panel 6: Energy spectrum comparison
ax = axes[1, 2]
ax.hist(evals_fold, bins=25, alpha=0.5, color='blue', label='H(fold, J)', density=True)
ax.hist(evals_fold_noJ, bins=25, alpha=0.5, color='red', label='H(fold, no J)', density=True)
ax.axvline(x=E_DE, color='blue', ls='--', lw=2, label=f'E_DE(J)={E_DE:.3f}')
ax.axvline(x=E_DE_noJ, color='red', ls='--', lw=2, label=f'E_DE(no J)={E_DE_noJ:.3f}')
ax.set_xlabel('Energy (M_KK)', fontsize=11)
ax.set_ylabel('Density', fontsize=11)
ax.set_title('Energy Spectrum and DE Energy', fontsize=12)
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plot_path = os.path.join(SCRIPT_DIR, 's56_gge_fabric.png')
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"Plot saved to {plot_path}")
print(f"\nTotal time: {time.time()-t0:.1f}s")
