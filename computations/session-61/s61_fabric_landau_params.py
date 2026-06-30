#!/usr/bin/env python3
"""
S61 — Fermi Liquid Parameters with Josephson Coupling (POMERAN-FABRIC-61)
=========================================================================

Physics:
  The single-cell BCS ground state at tau_fold has 8 modes (4B2+1B1+3B3).
  S58 verified Pomeranchuk stability for the isolated cell.
  Now we couple two cells via Josephson pair-hopping H_J and extract the
  Landau parameters F_l^{s,a} for the 2-cell fabric system.

Method:
  1. Construct H_full = H_BCS(1) x I(2) + I(1) x H_BCS(2) + H_J(1,2)
     in the 2-cell Fock space (dim = 256 x 256 = 65536).
  2. Diagonalize exactly.
  3. Extract quasiparticle energies from the low-lying spectrum.
  4. Compute Landau parameters from the interaction-induced shifts
     in quasiparticle energies (forward scattering amplitudes).
  5. Decompose into symmetric/antisymmetric (bonding/antibonding) channels.
  6. Check Pomeranchuk criterion: F_l > -(2l+1) for all l.

Symmetry:
  - Each cell: SU(2)_pair x [B2 x B1 x B3] irreps
  - 2-cell: Z_2 exchange symmetry (cell 1 <-> cell 2)
  - Josephson: locks relative phase, breaks U(1)_rel -> Z_2
  - Bonding/antibonding = symmetric/antisymmetric under Z_2

Gate: POMERAN-FABRIC-61
  PASS if all F_l satisfy Pomeranchuk criterion F_l > -(2l+1)
  FAIL if any violation
  INFO if marginal (within 10% of bound)

Author: Landau Condensed-Matter Theorist (S61)
"""

import numpy as np
import sys
import os
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    tau_fold, E_cond, E_cond_ED_8mode, N_dof_BCS,
    J_C2, J_su2, J_u1, T_acoustic,
    Delta_0_GL, Delta_0_OES, xi_BCS,
    a_GL, b_GL
)

# =============================================================================
# Section 1: Load single-cell data from S58 and S60
# =============================================================================

script_dir = os.path.dirname(os.path.abspath(__file__))

d58 = np.load(os.path.join(script_dir, 's58_pomeranchuk_gge.npz'), allow_pickle=True)
d60 = np.load(os.path.join(script_dir, 's60_rg_integrals.npz'), allow_pickle=True)

# Single-cell BCS data
V_bare = d58['V_bare']          # 8x8 interaction matrix (M_KK units)
E_k_single = d58['E_k']         # Single-particle energies (8 modes)
F_alpha_single = d58['F_alpha_all']  # S58 Landau parameters (single cell)
fk_gge = d58['fk_gge']          # GGE occupation numbers
N0_k = d58['N0_k']              # Density of states per mode

# 2-cell data from S60
eps_fold = d60['eps_fold']       # Mode energies at fold
V_fold = d60['V_fold']          # Interaction matrix at fold
E_J_fold = float(d60['E_J_fold'])  # Josephson coupling per bond

N_modes = 8  # 4B2 + 1B1 + 3B3 (local)
branch_labels = ['B2[0]', 'B2[1]', 'B2[2]', 'B2[3]', 'B1', 'B3[0]', 'B3[1]', 'B3[2]']

print("=" * 70)
print("S61: Fermi Liquid Parameters with Josephson Coupling")
print("=" * 70)
print(f"N_modes = {N_modes}")
print(f"Single-cell Hilbert space dim = 2^{N_modes} = {2**N_modes}")
print(f"2-cell Hilbert space dim = {2**N_modes}^2 = {(2**N_modes)**2}")
print(f"E_J_fold = {E_J_fold:.6f} M_KK")
print(f"E_cond (single cell) = {E_cond:.6f} M_KK")
print(f"J/|E_cond| = {E_J_fold / abs(E_cond):.2f}")
print()

# =============================================================================
# Section 2: Construct Single-Cell BCS Hamiltonian
# =============================================================================
# Fock space basis: |n_0 n_1 ... n_7> with n_k in {0, 1}
# State index = sum_k n_k * 2^k
# H_BCS = sum_k eps_k * n_k - sum_{k,k'} V_{kk'} * c^dag_k c^dag_{k'} c_{k'} c_k
# In the 0D reduced BCS model, the pairing interaction creates/destroys pairs
# in the occupation number basis.

dim_1 = 2**N_modes  # 256

def build_bcs_hamiltonian(eps, V_int, dim, n_modes):
    """
    Build single-cell BCS Hamiltonian in Fock space.

    The reduced BCS Hamiltonian is:
      H = sum_k eps_k * n_k - sum_{k != k'} V_{kk'} * P^+_k P^-_{k'}
    where P^+_k creates a pair in mode k (c^dag_k c^dag_{k_bar})
    and in the 0D model, pair creation/annihilation act on single
    occupation numbers (no momentum partner needed — each mode IS its own
    Cooper channel in the reduced model).

    For the 8-mode reduced BCS, each mode k represents a Cooper channel.
    P^+_k |...0_k...> = |...1_k...>, P^-_k |...1_k...> = |...0_k...>
    """
    H = np.zeros((dim, dim), dtype=np.float64)

    for state in range(dim):
        # Diagonal: kinetic energy
        E_diag = 0.0
        for k in range(n_modes):
            if state & (1 << k):
                E_diag += eps[k]
        H[state, state] = E_diag

        # Off-diagonal: pair scattering V_{kk'} P^+_k P^-_{k'}
        # This flips mode k' from occupied to empty AND mode k from empty to occupied
        for k in range(n_modes):
            for kp in range(n_modes):
                if k == kp:
                    continue
                # Need: mode kp occupied, mode k empty
                kp_occ = bool(state & (1 << kp))
                k_occ = bool(state & (1 << k))
                if kp_occ and not k_occ:
                    # Final state: flip k to 1, kp to 0
                    final = (state | (1 << k)) & ~(1 << kp)
                    H[final, state] -= V_int[k, kp]

    return H

print("Building single-cell BCS Hamiltonian...")
t0 = time.time()
H_single = build_bcs_hamiltonian(eps_fold, V_fold, dim_1, N_modes)
t1 = time.time()
print(f"  Done in {t1-t0:.2f}s. Shape: {H_single.shape}")

# Verify: single-cell ground state energy
evals_single = np.linalg.eigvalsh(H_single)
E_gs_single = evals_single[0]
E_gs_check = E_cond_ED_8mode  # Should match canonical value
# The ground state energy in the BCS model includes the kinetic part
# E_cond is the CONDENSATION energy = E_gs - E_normal
# E_normal = sum of occupied eps_k for normal state
# In the half-filled normal state (4 modes occupied), pick lowest 4:
sorted_eps = np.sort(eps_fold)
E_normal = np.sum(sorted_eps[:4])  # 4 lowest modes occupied
E_cond_computed = E_gs_single - E_normal

print(f"\nSingle-cell verification:")
print(f"  E_gs = {E_gs_single:.10f} M_KK")
print(f"  E_normal = {E_normal:.10f} M_KK")
print(f"  E_cond (computed) = {E_cond_computed:.10f} M_KK")
print(f"  E_cond (canonical) = {E_cond_ED_8mode:.10f} M_KK")
print(f"  Agreement: {abs(E_cond_computed - E_cond_ED_8mode) < 0.01}")

# =============================================================================
# Section 3: Construct 2-Cell Hamiltonian with Josephson Coupling
# =============================================================================
# H_full = H_BCS(1) x I(2) + I(1) x H_BCS(2) + H_J(1,2)
#
# Josephson coupling: H_J = -E_J * sum_k (P^+_{1,k} P^-_{2,k} + h.c.)
# This transfers pairs between cells. E_J > 0 favors phase locking.
#
# The Josephson energy scale comes from canonical constants:
# E_J_fold = 3.397 M_KK (from s60_rg_integrals)
#
# However, the directional stiffness is given by J_C2, J_su2, J_u1.
# For a physical Josephson coupling, each mode k has its own tunneling
# amplitude determined by its sector:
#   B2 modes (k=0..3): J_C2 = 0.933 M_KK
#   B1 mode  (k=4):    J_u1 = 0.038 M_KK (softest direction)
#   B3 modes (k=5..7): J_su2 = 0.059 M_KK

# Build mode-resolved Josephson couplings
J_mode = np.zeros(N_modes)
J_mode[0:4] = J_C2    # B2 sector: C^2 coset
J_mode[4]   = J_u1    # B1 sector: u(1)
J_mode[5:8] = J_su2   # B3 sector: su(2)

print("\n" + "=" * 70)
print("Section 3: 2-Cell Hamiltonian Construction")
print("=" * 70)
print(f"Mode-resolved Josephson couplings (M_KK):")
for k in range(N_modes):
    print(f"  {branch_labels[k]}: J_k = {J_mode[k]:.4f}")
print(f"Sum J_mode = {np.sum(J_mode):.4f}")
print(f"E_J_fold (from S60) = {E_J_fold:.4f}")

# The full 2-cell Hilbert space is too large (65536 x 65536) for dense
# diagonalization. We use the BLOCK DIAGONAL structure.
#
# Key insight: The TOTAL occupation number N_total = N_1 + N_2 is conserved
# by both H_BCS and H_J (Josephson transfers pairs, not single particles,
# but in our reduced model it transfers single occupation quantum numbers).
# Actually, H_J as pair hopping conserves N_1 + N_2.
#
# We can also use the Z_2 exchange symmetry (cell 1 <-> cell 2) to
# block-diagonalize into symmetric (S) and antisymmetric (A) sectors.
#
# Strategy: Work in the (N_1, N_2) = (n, N_total - n) sectors.
# For each total N, the dimension is sum over n of C(8,n) * C(8, N-n).

print("\nBlock structure by total occupation N_total:")
from math import comb
dim_total = 0
block_dims = {}
for N_tot in range(2*N_modes + 1):
    d = 0  # (local)
    for n1 in range(max(0, N_tot - N_modes), min(N_modes, N_tot) + 1):
        n2 = N_tot - n1
        if 0 <= n2 <= N_modes:
            d += comb(N_modes, n1) * comb(N_modes, n2)
    block_dims[N_tot] = d
    dim_total += d
    if d > 0:
        print(f"  N_total = {N_tot:2d}: dim = {d:6d}")

print(f"  Total dim = {dim_total} (check: {(2**N_modes)**2})")

# =============================================================================
# Section 4: Exact Diagonalization in N_total Sectors
# =============================================================================
# We diagonalize each N_total sector separately.
# The ground state will be in the sector with optimal total filling.
# For Josephson coupling, the ground state typically has N_total = N_modes
# (half filling of each cell, delocalized).

print("\n" + "=" * 70)
print("Section 4: Exact Diagonalization")
print("=" * 70)

def get_states_with_n(n_modes, n_occ):
    """Return all Fock states with exactly n_occ occupied modes."""
    states = []
    for s in range(2**n_modes):
        if bin(s).count('1') == n_occ:
            states.append(s)
    return states

def build_2cell_block(eps, V_int, J_k, n_modes, N_total):
    """
    Build the 2-cell Hamiltonian in the N_total sector.
    Basis: |s1, s2> where popcount(s1) + popcount(s2) = N_total.
    """
    # Enumerate basis states
    basis = []
    for n1 in range(max(0, N_total - n_modes), min(n_modes, N_total) + 1):
        n2 = N_total - n1
        if 0 <= n2 <= n_modes:
            states1 = get_states_with_n(n_modes, n1)
            states2 = get_states_with_n(n_modes, n2)
            for s1 in states1:
                for s2 in states2:
                    basis.append((s1, s2))

    dim = len(basis)
    if dim == 0:
        return np.array([]), [], np.array([])

    # Build index map for fast lookup
    idx_map = {}
    for i, (s1, s2) in enumerate(basis):
        idx_map[(s1, s2)] = i

    H = np.zeros((dim, dim), dtype=np.float64)

    for i, (s1, s2) in enumerate(basis):
        # Diagonal: eps(1) + eps(2)
        E_diag = 0.0
        for k in range(n_modes):
            if s1 & (1 << k):
                E_diag += eps[k]
            if s2 & (1 << k):
                E_diag += eps[k]
        H[i, i] = E_diag

        # Intra-cell pairing: cell 1
        for k in range(n_modes):
            for kp in range(n_modes):
                if k == kp:
                    continue
                kp_occ = bool(s1 & (1 << kp))
                k_occ = bool(s1 & (1 << k))
                if kp_occ and not k_occ:
                    s1_new = (s1 | (1 << k)) & ~(1 << kp)
                    key = (s1_new, s2)
                    if key in idx_map:
                        j = idx_map[key]
                        H[j, i] -= V_int[k, kp]

        # Intra-cell pairing: cell 2
        for k in range(n_modes):
            for kp in range(n_modes):
                if k == kp:
                    continue
                kp_occ = bool(s2 & (1 << kp))
                k_occ = bool(s2 & (1 << k))
                if kp_occ and not k_occ:
                    s2_new = (s2 | (1 << k)) & ~(1 << kp)
                    key = (s1, s2_new)
                    if key in idx_map:
                        j = idx_map[key]
                        H[j, i] -= V_int[k, kp]

        # Josephson: -J_k * (P^+_{1,k} P^-_{2,k} + h.c.)
        # Transfer mode k from cell 2 to cell 1: need k occupied in 2, empty in 1
        for k in range(n_modes):
            # Forward: cell2 -> cell1
            k_occ_1 = bool(s1 & (1 << k))
            k_occ_2 = bool(s2 & (1 << k))
            if k_occ_2 and not k_occ_1:
                s1_new = s1 | (1 << k)
                s2_new = s2 & ~(1 << k)
                key = (s1_new, s2_new)
                if key in idx_map:
                    j = idx_map[key]
                    H[j, i] -= J_k[k]
            # Backward: cell1 -> cell2
            if k_occ_1 and not k_occ_2:
                s1_new = s1 & ~(1 << k)
                s2_new = s2 | (1 << k)
                key = (s1_new, s2_new)
                if key in idx_map:
                    j = idx_map[key]
                    H[j, i] -= J_k[k]

    return H, basis, idx_map

# Diagonalize the most relevant sectors
# Ground state is expected near N_total = 8 (half filling)
# We need sectors N=6,7,8,9,10 for quasiparticle excitations (add/remove)

sectors_to_solve = list(range(0, 2*N_modes + 1))
sector_results = {}

t_start = time.time()
for N_tot in sectors_to_solve:
    d = block_dims[N_tot]
    if d == 0:
        continue
    if d > 10000:
        # For very large sectors, use sparse methods
        print(f"  N_total={N_tot}: dim={d} — using Lanczos (top 50 states)...")
        from scipy.sparse.linalg import eigsh
        from scipy.sparse import csr_matrix
        H_block, basis, idx_map = build_2cell_block(eps_fold, V_fold, J_mode, N_modes, N_tot)
        H_sp = csr_matrix(H_block)
        n_eig = min(50, d - 2)
        evals, evecs = eigsh(H_sp, k=n_eig, which='SA')
        sort_idx = np.argsort(evals)
        evals = evals[sort_idx]
        evecs = evecs[:, sort_idx]
        sector_results[N_tot] = {
            'evals': evals,
            'evecs': evecs,
            'basis': basis,
            'dim': d,
            'n_computed': n_eig
        }
    else:
        H_block, basis, idx_map = build_2cell_block(eps_fold, V_fold, J_mode, N_modes, N_tot)
        if H_block.size == 0:
            continue
        evals, evecs = np.linalg.eigh(H_block)
        sector_results[N_tot] = {
            'evals': evals,
            'evecs': evecs,
            'basis': basis,
            'dim': d,
            'n_computed': d
        }
    print(f"  N_total={N_tot}: dim={d:6d}, E_gs={sector_results[N_tot]['evals'][0]:.8f}")

t_end = time.time()
print(f"\nTotal diagonalization time: {t_end - t_start:.1f}s")

# =============================================================================
# Section 5: Ground State Analysis
# =============================================================================

print("\n" + "=" * 70)
print("Section 5: Ground State Analysis")
print("=" * 70)

# Find absolute ground state across all sectors
E_gs_all = {N: res['evals'][0] for N, res in sector_results.items()}
N_gs = min(E_gs_all, key=E_gs_all.get)
E_gs_2cell = E_gs_all[N_gs]

print(f"Ground state sector: N_total = {N_gs}")
print(f"Ground state energy: E_gs = {E_gs_2cell:.10f} M_KK")
print(f"2 x E_gs(single cell) = {2 * evals_single[0]:.10f} M_KK")
print(f"Josephson binding energy: Delta_E_J = {E_gs_2cell - 2*evals_single[0]:.10f} M_KK")
print(f"  = {abs(E_gs_2cell - 2*evals_single[0]) / abs(E_cond):.4f} |E_cond|")

# Z_2 exchange symmetry analysis
# The ground state eigenvector tells us about the cell-cell correlations
gs_vec = sector_results[N_gs]['evecs'][:, 0]
gs_basis = sector_results[N_gs]['basis']

# Compute <n_k(1)>, <n_k(2)> in the ground state
n1_avg = np.zeros(N_modes)
n2_avg = np.zeros(N_modes)
n1n2_corr = np.zeros((N_modes, N_modes))

for i, (s1, s2) in enumerate(gs_basis):
    prob = gs_vec[i]**2
    for k in range(N_modes):
        if s1 & (1 << k):
            n1_avg[k] += prob
        if s2 & (1 << k):
            n2_avg[k] += prob
        for kp in range(N_modes):
            occ1 = 1 if (s1 & (1 << k)) else 0
            occ2 = 1 if (s2 & (1 << kp)) else 0
            n1n2_corr[k, kp] += prob * occ1 * occ2

print(f"\nOccupation numbers in ground state:")
print(f"  {'Mode':8s} {'<n_1>':>10s} {'<n_2>':>10s} {'<n_1>+<n_2>':>12s}")
for k in range(N_modes):
    print(f"  {branch_labels[k]:8s} {n1_avg[k]:10.6f} {n2_avg[k]:10.6f} {n1_avg[k]+n2_avg[k]:12.6f}")
print(f"  {'Total':8s} {np.sum(n1_avg):10.6f} {np.sum(n2_avg):10.6f} {np.sum(n1_avg)+np.sum(n2_avg):12.6f}")

# Inter-cell correlation: C_{kk'} = <n_1k n_2k'> - <n_1k><n_2k'>
C_inter = n1n2_corr - np.outer(n1_avg, n2_avg)
print(f"\nInter-cell pair correlation (diagonal = same-mode Josephson coherence):")
print(f"  {'Mode':8s} {'C_kk':>12s}")
for k in range(N_modes):
    print(f"  {branch_labels[k]:8s} {C_inter[k,k]:12.8f}")

# =============================================================================
# Section 6: Quasiparticle Spectrum and Landau Parameters
# =============================================================================
#
# The Landau parameters are extracted from the quasiparticle interaction.
# In the 2-cell system, the quasiparticle energies split into bonding (+)
# and antibonding (-) channels under Z_2 exchange.
#
# For mode k, the quasiparticle energy is:
#   E_qp(k, +) = E(N_gs + 1, symmetric) - E(N_gs)   [bonding]
#   E_qp(k, -) = E(N_gs + 1, antisymmetric) - E(N_gs) [antibonding]
#
# The Landau parameter in channel alpha is:
#   F_alpha = N_0 * f_alpha
# where f_alpha is the forward scattering amplitude and N_0 is the DOS.
#
# For the 2-cell system, the bonding/antibonding splitting gives:
#   F_l^s = (F_+ + F_-) / 2   (symmetric Landau parameter)
#   F_l^a = (F_+ - F_-) / 2   (antisymmetric Landau parameter)
#
# The interaction matrix in the quasiparticle basis is:
#   f_{kk'} = d^2 E_gs / (dn_k dn_{k'}) = V_eff_{kk'}
# which we extract from the Hessian of the ground state energy
# with respect to occupation number variations.

print("\n" + "=" * 70)
print("Section 6: Landau Parameters from Quasiparticle Interaction")
print("=" * 70)

# Method A: Direct energy differences (quasiparticle addition/removal)
# E_qp(k) = E(N+1, k excited) - E(N)
# For the 2-cell system, excitations come in bonding/antibonding pairs

# The quasiparticle energies are the gaps to the first excited states
# in sectors N_gs +/- 1
E_add = {}  # Addition energies E(N+1) - E(N_gs)
E_rem = {}  # Removal energies E(N_gs) - E(N-1)

for dN in [-1, +1]:
    N_exc = N_gs + dN
    if N_exc in sector_results:
        evals_exc = sector_results[N_exc]['evals']
        n_exc_states = min(16, len(evals_exc))
        if dN == +1:
            for i in range(n_exc_states):
                E_add[i] = evals_exc[i] - E_gs_2cell
        else:
            for i in range(n_exc_states):
                E_rem[i] = E_gs_2cell - evals_exc[i]

print("Addition spectrum (E(N+1) - E_gs):")
for i in sorted(E_add.keys())[:8]:
    print(f"  level {i}: {E_add[i]:.8f} M_KK")

print("\nRemoval spectrum (E_gs - E(N-1)):")
for i in sorted(E_rem.keys())[:8]:
    print(f"  level {i}: {E_rem[i]:.8f} M_KK")

# Method B: Hessian of ground state energy
# The effective interaction between quasiparticles is the second derivative
# of E_gs with respect to an external potential coupled to mode k.
#
# We compute this by adding small perturbations delta_mu_k to each mode
# and measuring the response of the ground state energy.
#
# f_{kk'} = d^2 E_gs / (d mu_k d mu_{k'})
# F_{kk'} = N_0(k) * f_{kk'} * N_0(k')

print("\n--- Method B: Hessian extraction of Landau parameters ---")

delta_mu = 0.001  # Small perturbation for numerical derivatives  # (local)

def compute_E_gs_shifted(eps_shift, V_int, J_k, n_modes, N_target):
    """Compute ground state energy with shifted single-particle energies."""
    d_block = block_dims[N_target]
    if d_block == 0:
        return np.inf
    H_block, _, _ = build_2cell_block(eps_shift, V_int, J_k, n_modes, N_target)
    if H_block.size == 0:
        return np.inf
    if d_block > 5000:
        from scipy.sparse.linalg import eigsh
        from scipy.sparse import csr_matrix
        evals = eigsh(csr_matrix(H_block), k=1, which='SA', return_eigenvectors=False)
        return evals[0]
    else:
        return np.linalg.eigvalsh(H_block)[0]

# Compute unshifted ground state in the optimal sector
E0 = E_gs_2cell

# Single shifts: dE/d(mu_k)
dE_dmu = np.zeros(N_modes)
for k in range(N_modes):
    eps_p = eps_fold.copy()
    eps_p[k] += delta_mu
    eps_m = eps_fold.copy()
    eps_m[k] -= delta_mu
    E_p = compute_E_gs_shifted(eps_p, V_fold, J_mode, N_modes, N_gs)
    E_m = compute_E_gs_shifted(eps_m, V_fold, J_mode, N_modes, N_gs)
    dE_dmu[k] = (E_p - E_m) / (2 * delta_mu)

print(f"\nLinear response dE/d(mu_k) = <n_k(1) + n_k(2)>:")
for k in range(N_modes):
    print(f"  {branch_labels[k]}: {dE_dmu[k]:.6f} (check: {n1_avg[k]+n2_avg[k]:.6f})")

# Second derivatives: d^2 E / (d mu_k d mu_{k'})
# This is the quasiparticle interaction vertex
f_matrix = np.zeros((N_modes, N_modes))

t_hess_start = time.time()
for k in range(N_modes):
    for kp in range(k, N_modes):
        eps_pp = eps_fold.copy()
        eps_pp[k] += delta_mu
        eps_pp[kp] += delta_mu

        eps_pm = eps_fold.copy()
        eps_pm[k] += delta_mu
        eps_pm[kp] -= delta_mu

        eps_mp = eps_fold.copy()
        eps_mp[k] -= delta_mu
        eps_mp[kp] += delta_mu

        eps_mm = eps_fold.copy()
        eps_mm[k] -= delta_mu
        eps_mm[kp] -= delta_mu

        E_pp = compute_E_gs_shifted(eps_pp, V_fold, J_mode, N_modes, N_gs)
        E_pm = compute_E_gs_shifted(eps_pm, V_fold, J_mode, N_modes, N_gs)
        E_mp = compute_E_gs_shifted(eps_mp, V_fold, J_mode, N_modes, N_gs)
        E_mm = compute_E_gs_shifted(eps_mm, V_fold, J_mode, N_modes, N_gs)

        f_matrix[k, kp] = (E_pp - E_pm - E_mp + E_mm) / (4 * delta_mu**2)
        f_matrix[kp, k] = f_matrix[k, kp]

t_hess_end = time.time()
print(f"\nHessian computation time: {t_hess_end - t_hess_start:.1f}s")

# The Hessian d^2E/dmu_k dmu_{k'} represents the compressibility matrix.
# In Landau theory: d^2E/dmu_k dmu_{k'} = chi_{kk'} = N_0(k) [delta_{kk'} + F_{kk'}/N_0(k')]
# So the Landau interaction matrix is:
#   F_{kk'} = chi_{kk'} - N_0(k) delta_{kk'}
#
# But we need to be careful: the Hessian of E_gs w.r.t. mu_k
# gives the SUSCEPTIBILITY chi = -dN/dmu, and the Landau parameter
# enters as: chi^{-1} = N_0^{-1} (1 + F)
#
# Actually, the STATIC susceptibility is:
#   chi_{kk'} = -d^2 E / (d mu_k d mu_{k'})  [note the sign]
# and
#   chi_{kk'}^{-1} = delta_{kk'}/N_0(k) + f_{kk'}
# So:
#   f_{kk'} = chi^{-1}_{kk'} - delta_{kk'}/N_0(k)

# The Hessian as computed IS the susceptibility (negative of it, since
# d^2E/dmu^2 = -dN/dmu for stability)
# chi_{kk'} = -f_matrix[k,k'] (the negative Hessian)

chi_matrix = -f_matrix  # Static susceptibility

print(f"\nSusceptibility matrix chi_{'{kk}'}:")
print(f"  Diagonal entries (compressibility per mode):")
for k in range(N_modes):
    print(f"  {branch_labels[k]}: chi_kk = {chi_matrix[k,k]:.8f}")

# =============================================================================
# Section 7: Landau Parameters Extraction
# =============================================================================

print("\n" + "=" * 70)
print("Section 7: Landau Parameter Extraction")
print("=" * 70)

# The 2-cell density of states at the Fermi surface
# For the coupled system, N_0 is modified by Josephson coupling.
# We extract it from the single-particle Green's function:
#   N_0(k) = -Im[G(k, omega -> 0+)] / pi
# In practice, for discrete systems, N_0(k) is related to the occupation
# number susceptibility.
#
# Use the S58 density of states as the baseline,
# then correct for Josephson-induced bandwidth changes.

# For the 2-cell system, each mode k splits into bonding/antibonding:
#   eps_+(k) = eps(k) - J_k  (bonding)
#   eps_-(k) = eps(k) + J_k  (antibonding)
# The DOS doubles (two bands) but each band has half the spectral weight.
# Net effect on N_0: unchanged to leading order in J/bandwidth.

# We use the S58 N0_k values as the density of states per mode
N0_2cell = N0_k.copy()  # Per mode, both cells combined

# The Landau interaction function in the mode basis:
# From the Hessian, the INVERSE susceptibility is:
#   chi^{-1}_{kk'} = delta_{kk'}/N0(k) + f_{kk'}
# So:
#   f_{kk'} = chi^{-1}_{kk'} - delta_{kk'}/N0(k)

# Compute chi^{-1}
# chi_matrix should be positive definite for a stable system
chi_evals = np.linalg.eigvalsh(chi_matrix)
print(f"Susceptibility eigenvalues: {chi_evals}")
print(f"Min eigenvalue: {np.min(chi_evals):.8e}")

if np.min(chi_evals) > 0:
    chi_inv = np.linalg.inv(chi_matrix)
    print("Susceptibility matrix is positive definite — system is compressible.")
else:
    print("WARNING: Susceptibility has non-positive eigenvalues!")
    print("Adding regularization...")
    reg = abs(np.min(chi_evals)) + 1e-8
    chi_reg = chi_matrix + reg * np.eye(N_modes)
    chi_inv = np.linalg.inv(chi_reg)

# Landau interaction in mode basis (dimensionless)
# F_{kk'} = N_0(k)^{1/2} * f_{kk'} * N_0(k')^{1/2}
# where f is the irreducible vertex function
# From chi^{-1} = N_0^{-1} + f:
#   f_{kk'} = chi^{-1}_{kk'} - delta_{kk'}/N_0(k)

f_vertex = np.zeros((N_modes, N_modes))
for k in range(N_modes):
    for kp in range(N_modes):
        f_vertex[k, kp] = chi_inv[k, kp]
        if k == kp:
            f_vertex[k, kp] -= 1.0 / N0_2cell[k]

# Dimensionless Landau parameters: F_{kk'} = sqrt(N0_k) * f_{kk'} * sqrt(N0_{k'})
F_Landau = np.zeros((N_modes, N_modes))
for k in range(N_modes):
    for kp in range(N_modes):
        F_Landau[k, kp] = np.sqrt(N0_2cell[k]) * f_vertex[k, kp] * np.sqrt(N0_2cell[kp])

print(f"\nLandau interaction matrix F_{{kk'}} (dimensionless):")
header = "        " + "".join(f"{branch_labels[k]:>10s}" for k in range(N_modes))
print(header)
for k in range(N_modes):
    row = f"{branch_labels[k]:8s}" + "".join(f"{F_Landau[k,kp]:10.6f}" for kp in range(N_modes))
    print(row)

# =============================================================================
# Section 8: Angular Momentum Decomposition
# =============================================================================
#
# In the reduced 0D BCS model, there is no continuous angular momentum.
# The "angular harmonics" are the irreps of the discrete symmetry group.
#
# For the 8-mode system with sectors B2(4) + B1(1) + B3(3):
# - l=0: Trace of F (monopole, compressibility)
# - l=1: B2-B1 and B2-B3 cross-sector (dipole, effective mass)
# - l=2: Intra-B2 quadrupole
# Higher l: intra-sector fine structure
#
# The Pomeranchuk condition is checked for each eigenvalue of F:
#   All eigenvalues of (1 + F) must be positive, i.e., F_alpha > -1 for l=0

print("\n" + "=" * 70)
print("Section 8: Pomeranchuk Stability Analysis")
print("=" * 70)

# Eigenvalues of the Landau interaction matrix
F_evals = np.linalg.eigvalsh(F_Landau)
print(f"\nEigenvalues of Landau matrix F (sorted):")
for i, ev in enumerate(F_evals):
    bound = -(2*0 + 1)  # For l=0, bound is -1. For general l, -(2l+1)
    # In the discrete case, the Pomeranchuk condition is simply
    # all eigenvalues of (1 + F_l/(2l+1)) > 0
    # For l=0: F_0 > -1
    # The most conservative: all eigenvalues of F must be > -1
    margin = (ev - (-1)) / 1.0  # fractional distance from bound
    status = "STABLE" if ev > -1 else "UNSTABLE"
    if ev > -1 and margin < 0.1:
        status = "MARGINAL"
    print(f"  F_{i} = {ev:12.8f}  (1+F_{i} = {1+ev:12.8f})  {status}")

# The stability matrix S = I + F
stability_matrix = np.eye(N_modes) + F_Landau
stability_evals = np.linalg.eigvalsh(stability_matrix)
print(f"\nStability matrix eigenvalues (must all be > 0):")
for i, ev in enumerate(stability_evals):
    status = "STABLE" if ev > 0 else "UNSTABLE"
    if ev > 0 and ev < 0.1:
        status = "MARGINAL"
    print(f"  lambda_{i} = {ev:12.8f}  {status}")

min_stability = np.min(stability_evals)
print(f"\nMinimum stability eigenvalue: {min_stability:.8e}")

# Sector-resolved Landau parameters
# F_0 (compressibility): average of F matrix = Tr(F)/N_modes
F_0_fabric = np.trace(F_Landau) / N_modes
print(f"\nSector-resolved Landau parameters:")
print(f"  F_0 (full, compressibility) = {F_0_fabric:.8f}")
print(f"  F_0 (S58, single cell)      = {float(d58['F_0_full']):.8f}")
print(f"  Shift due to Josephson       = {F_0_fabric - float(d58['F_0_full']):.8f}")

# B2 sector (l=2 analog)
F_B2 = F_Landau[0:4, 0:4]
F_B2_evals = np.linalg.eigvalsh(F_B2)
print(f"\n  B2 sector eigenvalues: {F_B2_evals}")
print(f"  B2 F_0 = {np.trace(F_B2)/4:.8f}")

# B3 sector
F_B3 = F_Landau[5:8, 5:8]
F_B3_evals = np.linalg.eigvalsh(F_B3)
print(f"\n  B3 sector eigenvalues: {F_B3_evals}")
print(f"  B3 F_0 = {np.trace(F_B3)/3:.8f}")

# B1 sector (single mode)
F_B1 = F_Landau[4, 4]
print(f"\n  B1 (single mode): F = {F_B1:.8f}")

# Cross-sector couplings induced by Josephson
F_B2_B1 = np.mean(np.abs(F_Landau[0:4, 4]))
F_B2_B3 = np.mean(np.abs(F_Landau[0:4, 5:8]))
F_B1_B3 = np.mean(np.abs(F_Landau[4, 5:8]))
print(f"\n  Cross-sector coupling magnitudes:")
print(f"    |F_B2-B1| (mean) = {F_B2_B1:.8f}")
print(f"    |F_B2-B3| (mean) = {F_B2_B3:.8f}")
print(f"    |F_B1-B3| (mean) = {F_B1_B3:.8f}")

# =============================================================================
# Section 9: Symmetric (s) and Antisymmetric (a) Channel Decomposition
# =============================================================================
#
# For the 2-cell system with Z_2 exchange symmetry:
# Bonding (symmetric): both cells in phase -> collective compressibility
# Antibonding (antisymmetric): cells out of phase -> relative compressibility
#
# In the 2-cell problem, the bonding/antibonding splitting of quasiparticle
# energies directly gives F^s and F^a:
#   F^s_k = (F_k,bonding + F_k,antibonding) / 2
#   F^a_k = (F_k,bonding - F_k,antibonding) / 2
#
# We extract this from the spectrum in the N_gs and N_gs+/-1 sectors
# by resolving the Z_2 parity of each excited state.

print("\n" + "=" * 70)
print("Section 9: Symmetric/Antisymmetric Channel Decomposition")
print("=" * 70)

# For each state in sector N_gs, compute the Z_2 parity
# Z_2 acts as (s1, s2) -> (s2, s1)
gs_basis_N = sector_results[N_gs]['basis']
gs_evecs = sector_results[N_gs]['evecs']
gs_evals = sector_results[N_gs]['evals']

def compute_z2_parity(evec, basis, n_modes):
    """Compute <P_12> where P_12 swaps cells 1 and 2."""
    # Build the swap map
    parity = 0.0
    idx_map_local = {b: i for i, b in enumerate(basis)}
    for i, (s1, s2) in enumerate(basis):
        swapped = (s2, s1)
        if swapped in idx_map_local:
            j = idx_map_local[swapped]
            parity += evec[i] * evec[j]
    return parity

# Compute parity of ground state and first few excited states
n_check = min(20, len(gs_evals))
print(f"Z_2 parity of low-lying states in N_total={N_gs} sector:")
parities_gs_sector = []
for i in range(n_check):
    p = compute_z2_parity(gs_evecs[:, i], gs_basis_N, N_modes)
    parities_gs_sector.append(p)
    parity_label = "+" if p > 0 else "-"
    print(f"  E_{i} = {gs_evals[i]:.8f}, P_12 = {p:+.6f} ({parity_label})")

# Same for N_gs+1 sector (quasiparticle addition)
if N_gs + 1 in sector_results:
    add_basis = sector_results[N_gs+1]['basis']
    add_evecs = sector_results[N_gs+1]['evecs']
    add_evals = sector_results[N_gs+1]['evals']
    n_add = min(16, len(add_evals))
    print(f"\nZ_2 parity of addition excitations (N={N_gs+1}):")
    parities_add = []
    E_add_sym = []
    E_add_anti = []
    for i in range(n_add):
        p = compute_z2_parity(add_evecs[:, i], add_basis, N_modes)
        parities_add.append(p)
        parity_label = "+" if p > 0 else "-"
        print(f"  E_{i} = {add_evals[i]:.8f}, dE = {add_evals[i]-E_gs_2cell:.8f}, P_12 = {p:+.6f} ({parity_label})")
        if p > 0.5:
            E_add_sym.append(add_evals[i] - E_gs_2cell)
        elif p < -0.5:
            E_add_anti.append(add_evals[i] - E_gs_2cell)

    print(f"\n  Symmetric (bonding) addition energies: {E_add_sym[:4]}")
    print(f"  Antisymmetric (antibonding) addition energies: {E_add_anti[:4]}")

    if len(E_add_sym) > 0 and len(E_add_anti) > 0:
        # The bonding-antibonding splitting is the Josephson signature
        # For paired modes, we should see pairs split by ~2*J_k
        print(f"\n  Bonding-antibonding splittings:")
        n_pairs_to_show = min(len(E_add_sym), len(E_add_anti))
        for i in range(n_pairs_to_show):
            splitting = E_add_anti[i] - E_add_sym[i]
            print(f"    pair {i}: delta = {splitting:.8f} M_KK")

# =============================================================================
# Section 10: Comparison with S58 Single-Cell Results
# =============================================================================

print("\n" + "=" * 70)
print("Section 10: Comparison with S58 Single-Cell Pomeranchuk")
print("=" * 70)

F_alpha_fabric = F_evals  # Eigenvalues of F for the fabric
F_alpha_single_sorted = np.sort(F_alpha_single)

print(f"\n{'Channel':>10s} {'F(single)':>12s} {'F(fabric)':>12s} {'Shift':>12s} {'Status':>10s}")
print("-" * 60)
for i in range(N_modes):
    f_s = F_alpha_single_sorted[i] if i < len(F_alpha_single_sorted) else 0.0
    f_f = F_alpha_fabric[i]
    shift = f_f - f_s
    dist = f_f - (-1)
    status = "STABLE"
    if dist < 0:
        status = "UNSTABLE"
    elif dist / 1.0 < 0.1:
        status = "MARGINAL"
    print(f"  alpha={i:2d}  {f_s:12.8f}  {f_f:12.8f}  {shift:+12.8f}  {status:>10s}")

# Pomeranchuk distances (distance to instability boundary)
distances = F_alpha_fabric - (-1)
closest_channel = np.argmin(distances)
min_distance = distances[closest_channel]

print(f"\nClosest to instability: channel {closest_channel}")
print(f"  F_{closest_channel} = {F_alpha_fabric[closest_channel]:.8f}")
print(f"  Distance to bound = {min_distance:.8f}")
print(f"  Relative margin = {min_distance:.4f} (10% threshold = 0.1)")

# S58 comparison
dist_s58 = float(d58['min_distance'])
print(f"\n  S58 min distance = {dist_s58:.8f}")
print(f"  S61 min distance = {min_distance:.8f}")
print(f"  Change = {min_distance - dist_s58:+.8f}")
if min_distance < dist_s58:
    print(f"  -> Josephson coupling DECREASED stability margin by {abs(min_distance - dist_s58):.6f}")
else:
    print(f"  -> Josephson coupling INCREASED stability margin by {abs(min_distance - dist_s58):.6f}")

# =============================================================================
# Section 11: Gate Verdict
# =============================================================================

print("\n" + "=" * 70)
print("Section 11: POMERAN-FABRIC-61 Gate Verdict")
print("=" * 70)

all_stable = np.all(F_alpha_fabric > -1)
any_marginal = np.any((F_alpha_fabric > -1) & (F_alpha_fabric + 1 < 0.1))
any_unstable = np.any(F_alpha_fabric <= -1)

if any_unstable:
    verdict = "FAIL"
    detail = f"Pomeranchuk violation in channel {np.argmin(F_alpha_fabric)}: F = {np.min(F_alpha_fabric):.8f} < -1"
elif any_marginal:
    verdict = "INFO"
    detail = f"Marginal stability. Min F = {np.min(F_alpha_fabric):.8f}, distance to bound = {min_distance:.8f}"
else:
    verdict = "PASS"
    detail = f"All channels stable. Min F = {np.min(F_alpha_fabric):.8f}, distance to bound = {min_distance:.8f}"

print(f"\n  Gate: POMERAN-FABRIC-61")
print(f"  Criterion: F_l > -(2l+1) for all l")
print(f"  Verdict: {verdict}")
print(f"  Detail: {detail}")
print(f"  Min stability eigenvalue: {min_stability:.8e}")
print(f"  All F_alpha > -1: {all_stable}")
print(f"  Josephson binding energy: {E_gs_2cell - 2*evals_single[0]:.8f} M_KK")

# =============================================================================
# Section 12: Save Results
# =============================================================================

print("\n" + "=" * 70)
print("Section 12: Saving Results")
print("=" * 70)

output = os.path.join(script_dir, 's61_fabric_landau_params.npz')

np.savez(output,
    # Gate
    gate_name='POMERAN-FABRIC-61',
    gate_verdict=verdict,
    gate_criterion='F_l > -(2l+1) for all l',
    gate_detail=detail,

    # 2-cell ground state
    E_gs_2cell=E_gs_2cell,
    E_gs_single=evals_single[0],
    E_binding_J=E_gs_2cell - 2*evals_single[0],
    N_gs=N_gs,

    # Landau parameters (eigenvalues)
    F_alpha_fabric=F_alpha_fabric,
    F_alpha_single=F_alpha_single_sorted,
    F_shift=F_alpha_fabric - F_alpha_single_sorted[:len(F_alpha_fabric)],

    # Landau interaction matrix
    F_Landau_matrix=F_Landau,
    f_vertex_matrix=f_vertex,
    chi_matrix=chi_matrix,

    # Sector-resolved
    F_0_fabric=F_0_fabric,
    F_0_single=float(d58['F_0_full']),
    F_B2_evals=F_B2_evals,
    F_B3_evals=F_B3_evals,
    F_B1=F_B1,

    # Stability
    stability_evals=stability_evals,
    min_stability_eval=min_stability,
    distances_to_instability=distances,
    closest_channel=closest_channel,
    min_distance=min_distance,

    # Occupation numbers
    n1_avg=n1_avg,
    n2_avg=n2_avg,
    C_inter=C_inter,

    # Josephson couplings used
    J_mode=J_mode,
    E_J_fold=E_J_fold,

    # Metadata
    N_modes=N_modes,
    branch_labels=branch_labels,
    eps_fold=eps_fold,
    V_fold=V_fold,
    tau_fold=tau_fold,
    delta_mu_hessian=delta_mu,

    # S58 comparison
    pomeranchuk_stable_single=bool(d58['pomeranchuk_stable']),
    min_distance_single=dist_s58,
)

print(f"  Saved to: {output}")
print(f"  Keys: {sorted(np.load(output, allow_pickle=True).files)}")

print("\n" + "=" * 70)
print(f"FINAL VERDICT: POMERAN-FABRIC-61 = {verdict}")
print("=" * 70)
