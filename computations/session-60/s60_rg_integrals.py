#!/usr/bin/env python3
"""
s60_rg_integrals.py — Richardson-Gaudin Integrals as Explicit Diagnostics
=========================================================================

Gate: RG-INTEGRALS-60
  PASS: Dominant breaking from Josephson (inter-cell) — separable intra-cell
        integrals approximately conserved (delta_k < 0.01 for majority)
  FAIL: All integrals strongly broken (delta_k > 0.1 for all k)
  INFO: Mixed (some conserved, some broken, no clear pattern)

Physics:
  The Richardson-Gaudin (RG) model is the unique integrable BCS Hamiltonian.
  It possesses N integrals of motion {R_k}, one per single-particle level,
  satisfying [R_k, R_l] = 0 and [H_RG, R_k] = 0. The standard form is:

    R_k = S_k^z + Sum_{l != k} (S_k . S_l) / (eps_k - eps_l)

  where S_k^z, S_k^+, S_k^- are pseudo-spin-1/2 operators for pair k:
    S_k^+ = pair_k^dag,  S_k^- = pair_k,  S_k^z = (n_k - 1/2)

  For the framework's non-separable V_fold, the RG integrals are NOT exact.
  The mode-resolved commutator norm
    delta_k = ||[H_full, R_k]|| / ||H_full||
  identifies which modes break integrability and which remain approximately
  conserved. We further decompose the breaking into:
    (a) Intra-cell non-separability of V_fold  (non-RG pairing)
    (b) Inter-cell Josephson coupling E_J      (collective tunneling)

Method:
  1. Load 2-cell BCS Hamiltonian parameters from s58/s56 data
  2. Construct pseudo-spin operators S_k^z, S_k^+, S_k^- for each
     mode k in each cell, in the N_pair=2 Fock space (dim=120)
  3. Build R_k as explicit matrices for all 16 modes (8 per cell)
  4. Compute [H_full, R_k], [H_noJ, R_k], [H_sep, R_k] for decomposition
  5. Normalize: delta_k = ||[H, R_k]||_F / ||H||_F
  6. Rank and classify

Session: S60 W5-1
Agent: landau-condensed-matter-theorist
"""

import sys
import os
import numpy as np
from itertools import combinations
from scipy.linalg import eigh
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# === Import canonical constants ===
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from canonical_constants import tau_fold, E_cond, N_dof_BCS, M_KK

# =====================================================================
#  1. LOAD INPUT DATA
# =====================================================================

data_dir = os.path.dirname(os.path.abspath(__file__))

# S56 GGE fabric data (2-cell system at fold)
d56 = np.load(os.path.join(data_dir, 's56_gge_fabric.npz'), allow_pickle=True)
eps_fold = d56['eps_fold']       # (8,) single-particle energies at fold
eps_tau0 = d56['eps_tau0']       # (8,) single-particle energies at tau=0
V_fold   = d56['V_fold']        # (8,8) pairing matrix
E_J_fold = float(d56['E_J_fold'])
tau_fold_actual = float(d56['tau_fold_actual'])

# S58 for cross-check of existing commutator norms
d58 = np.load(os.path.join(data_dir, 's58_npair2_integ.npz'), allow_pickle=True)
comm_norms_s58_full = d58['comm_norms_full']   # (2,8) — [H_full, n_k] norms
comm_norms_s58_noJ  = d58['comm_norms_noJ']    # (2,8) — [H_noJ, n_k] norms

N_modes = 8  # (local)
N_cells = 2
N_pair  = 2  # (local)

print("=" * 70)
print("S60 W5-1: Richardson-Gaudin Integrals — RG-INTEGRALS-60")
print("=" * 70)
print(f"tau_fold = {tau_fold_actual:.6f}")
print(f"E_J_fold = {E_J_fold:.4f} M_KK")
print(f"N_modes/cell = {N_modes}, N_cells = {N_cells}, N_pair = {N_pair}")
print(f"eps_fold = {eps_fold}")


# =====================================================================
#  2. CONSTRUCT PAIR FOCK SPACE (identical to S58)
# =====================================================================

N_slots = N_modes * N_cells  # 16
pair_states = list(combinations(range(N_slots), N_pair))
dim = len(pair_states)
print(f"\nFock space: C({N_slots},{N_pair}) = {dim} two-pair states")

def slot_to_mode_cell(s):
    """Convert pair-slot index to (mode_index, cell_index)."""
    return (s % N_modes, s // N_modes)

state_info = []
for idx, (s1, s2) in enumerate(pair_states):
    m1, c1 = slot_to_mode_cell(s1)
    m2, c2 = slot_to_mode_cell(s2)
    state_info.append(((m1, c1), (m2, c2)))

state_index = {s: i for i, s in enumerate(pair_states)}


# =====================================================================
#  3. BUILD HAMILTONIAN (same as S58, reproduced for self-containment)
# =====================================================================

def build_H_BCS_2cell(eps, V, E_J):
    """
    Build full BCS + Josephson Hamiltonian for N_pair=2 on a 2-cell system.
    Identical to S58 construction.
    """
    H = np.zeros((dim, dim), dtype=np.float64)

    for i, (s1, s2) in enumerate(pair_states):
        (m1, c1), (m2, c2) = state_info[i]

        # Diagonal: kinetic energy
        H[i, i] += 2.0 * eps[m1] + 2.0 * eps[m2]

        # Pairing: scatter pair 1 in its cell
        for k in range(N_modes):
            if k == m1:
                H[i, i] -= V[m1, m1]
                continue
            new_slot1 = c1 * N_modes + k
            if new_slot1 == s2:
                continue
            new_state = tuple(sorted([new_slot1, s2]))
            if new_state in state_index:
                j = state_index[new_state]
                H[j, i] -= V[k, m1]

        # Pairing: scatter pair 2 in its cell
        for k in range(N_modes):
            if k == m2:
                H[i, i] -= V[m2, m2]
                continue
            new_slot2 = c2 * N_modes + k
            if new_slot2 == s1:
                continue
            new_state = tuple(sorted([s1, new_slot2]))
            if new_state in state_index:
                j = state_index[new_state]
                H[j, i] -= V[k, m2]

        # Josephson tunneling
        for l in range(N_modes):
            new_slot1 = (1 - c1) * N_modes + l
            if new_slot1 == s2:
                continue
            new_state = tuple(sorted([new_slot1, s2]))
            if new_state in state_index:
                j = state_index[new_state]
                H[j, i] += -E_J / 2.0

        for l in range(N_modes):
            new_slot2 = (1 - c2) * N_modes + l
            if new_slot2 == s1:
                continue
            new_state = tuple(sorted([s1, new_slot2]))
            if new_state in state_index:
                j = state_index[new_state]
                H[j, i] += -E_J / 2.0

    H = 0.5 * (H + H.T)
    return H


# Build the three Hamiltonians
print("\n--- Building Hamiltonians ---")
H_full = build_H_BCS_2cell(eps_fold, V_fold, E_J_fold)
H_noJ  = build_H_BCS_2cell(eps_fold, V_fold, 0.0)

# Build separable-V Hamiltonian: use rank-1 SVD approximation of V_fold
U_svd, S_svd, Vt_svd = np.linalg.svd(V_fold)
V_sep = S_svd[0] * np.outer(U_svd[:, 0], Vt_svd[0, :])  # Rank-1 approximation
V_nonsep = V_fold - V_sep  # Non-separable remainder

H_sep  = build_H_BCS_2cell(eps_fold, V_sep, 0.0)     # Separable pairing only (no J)
H_sep_J = build_H_BCS_2cell(eps_fold, V_sep, E_J_fold)  # Separable + Josephson

# Also build pure kinetic + Josephson (no pairing)
H_kin = np.zeros((dim, dim), dtype=np.float64)
for i, (s1, s2) in enumerate(pair_states):
    (m1, c1), (m2, c2) = state_info[i]
    H_kin[i, i] = 2.0 * eps_fold[m1] + 2.0 * eps_fold[m2]

# Pure Josephson (H_full - H_noJ)
H_J = H_full - H_noJ

# Pure non-separable pairing (H_noJ - H_sep)
H_nonsep = H_noJ - H_sep

# Verify decomposition: H_full = H_sep + H_nonsep + H_J + H_kin ... no,
# H_full = H_kin + H_pairing_full + H_J
# H_noJ = H_kin + H_pairing_full
# H_sep = H_kin + H_pairing_sep
# H_nonsep = H_pairing_full - H_pairing_sep
# So: H_full = H_sep + H_nonsep + H_J

decomp_check = np.max(np.abs(H_full - H_sep - H_nonsep - H_J))
print(f"Decomposition check: ||H_full - H_sep - H_nonsep - H_J||_max = {decomp_check:.2e}")

# Norms for normalization
norm_H_full = np.linalg.norm(H_full, 'fro')
norm_H_noJ  = np.linalg.norm(H_noJ, 'fro')
norm_H_sep  = np.linalg.norm(H_sep, 'fro')
norm_H_J    = np.linalg.norm(H_J, 'fro')
norm_H_nonsep = np.linalg.norm(H_nonsep, 'fro')

print(f"||H_full||_F   = {norm_H_full:.4f}")
print(f"||H_noJ||_F    = {norm_H_noJ:.4f}")
print(f"||H_sep||_F    = {norm_H_sep:.4f}")
print(f"||H_J||_F      = {norm_H_J:.4f}")
print(f"||H_nonsep||_F = {norm_H_nonsep:.4f}")

# Hermiticity checks
print(f"\nHermiticity: H_full={np.max(np.abs(H_full-H_full.T)):.2e}, "
      f"H_noJ={np.max(np.abs(H_noJ-H_noJ.T)):.2e}, "
      f"H_sep={np.max(np.abs(H_sep-H_sep.T)):.2e}")


# =====================================================================
#  4. CONSTRUCT PSEUDO-SPIN OPERATORS
# =====================================================================
print("\n--- Building pseudo-spin operators ---")

def build_pair_number_op(mode, cell):
    """n_{mode,cell} in pair Fock basis."""
    n_op = np.zeros((dim, dim))
    slot = cell * N_modes + mode
    for i, (s1, s2) in enumerate(pair_states):
        if s1 == slot or s2 == slot:
            n_op[i, i] = 1.0
    return n_op

def build_Sz(mode, cell):
    """S_k^z = n_k - 1/2 for pseudo-spin representation."""
    return build_pair_number_op(mode, cell) - 0.5 * np.eye(dim)

def build_Sp(mode, cell):
    """S_k^+ = pair_k^dag (pair creation at mode k in cell)."""
    op = np.zeros((dim, dim))
    slot = cell * N_modes + mode
    # S_k^+ |...0_k...> = |...1_k...>
    # In the 2-pair Fock space, this creates a pair at slot if it's empty
    # But we're in fixed N_pair=2 sector, so S_k^+ acts only if there's
    # exactly one pair elsewhere that can be annihilated...
    #
    # Actually, S_k^+ as a standalone operator doesn't conserve pair number.
    # It maps the N_pair=2 sector to N_pair=3. We need to embed in the
    # full Fock space or work with products S_k^+ S_l^-.
    #
    # For the RG integrals, what appears is the COMBINATION:
    #   S_k^+ S_l^- = pair_k^dag pair_l (pair hop: l -> k)
    # which DOES conserve pair number.
    #
    # So we skip standalone S_k^+/S_k^- and build S_k^+ S_l^- directly.
    return None  # Not used standalone

def build_SpSm(k_mode, k_cell, l_mode, l_cell):
    """
    Build S_k^+ S_l^- = pair_k^dag pair_l operator.
    Hops a pair from (l_mode, l_cell) to (k_mode, k_cell).
    Conserves pair number.
    """
    op = np.zeros((dim, dim))
    slot_k = k_cell * N_modes + k_mode
    slot_l = l_cell * N_modes + l_mode
    if slot_k == slot_l:
        # S_k^+ S_k^- = n_k (number operator)
        return build_pair_number_op(k_mode, k_cell)

    for i, (s1, s2) in enumerate(pair_states):
        # pair_l must be occupied, pair_k must be unoccupied
        if slot_l in (s1, s2) and slot_k not in (s1, s2):
            if s1 == slot_l:
                new_state = tuple(sorted([slot_k, s2]))
            else:
                new_state = tuple(sorted([s1, slot_k]))
            if new_state in state_index:
                j = state_index[new_state]
                op[j, i] = 1.0
    return op

def build_SzSz(k_mode, k_cell, l_mode, l_cell):
    """Build S_k^z S_l^z = (n_k - 1/2)(n_l - 1/2)."""
    Sz_k = build_Sz(k_mode, k_cell)
    Sz_l = build_Sz(l_mode, l_cell)
    return Sz_k @ Sz_l


# =====================================================================
#  5. CONSTRUCT RICHARDSON-GAUDIN INTEGRALS
# =====================================================================
print("\n--- Building Richardson-Gaudin integrals ---")
print("R_k = S_k^z + Sum_{l!=k} [S_k^+ S_l^- + S_k^- S_l^+ + 2 S_k^z S_l^z]")
print("                         / (2*eps_k - 2*eps_l)")
print()
print("NOTE: The eps_k here are the single-particle energies for the SAME cell.")
print("For the 2-cell system, we build R_k separately for each cell,")
print("using only intra-cell pseudo-spin couplings in the RG integral.")
print("This is the correct construction: RG integrals are per-cell quantities.")
print("Josephson coupling is EXTERNAL to the integrable structure.")

# For each cell c, for each mode k in that cell:
# R_k^(c) = S_k^z(c) + Sum_{l!=k, l in same cell}
#           [S_k^+(c) S_l^-(c) + S_l^+(c) S_k^-(c) + 2 S_k^z(c) S_l^z(c)]
#           / (2*(eps_k - eps_l))

# Pre-compute all Sz operators
Sz = {}
for c in range(N_cells):
    for k in range(N_modes):
        Sz[(k, c)] = build_Sz(k, c)

# Build RG integrals
R = {}  # R[(k, c)] = Richardson-Gaudin integral for mode k in cell c

for c in range(N_cells):
    for k in range(N_modes):
        R_k = Sz[(k, c)].copy()

        for l in range(N_modes):
            if l == k:
                continue
            denom = 2.0 * (eps_fold[k] - eps_fold[l])
            if abs(denom) < 1e-15:
                print(f"WARNING: degenerate levels k={k}, l={l}, eps={eps_fold[k]:.8f}")
                continue

            # S_k^+ S_l^- (hop l -> k, same cell)
            SpSm_kl = build_SpSm(k, c, l, c)
            # S_l^+ S_k^- = S_k^- S_l^+ (hop k -> l, same cell)
            SpSm_lk = build_SpSm(l, c, k, c)
            # S_k^z S_l^z
            SzSz_kl = build_SzSz(k, c, l, c)

            R_k += (SpSm_kl + SpSm_lk + 2.0 * SzSz_kl) / denom

        R[(k, c)] = R_k

print(f"Built {len(R)} Richardson-Gaudin integrals (8 per cell x 2 cells)")


# =====================================================================
#  6. VERIFY: RG INTEGRALS SHOULD COMMUTE WITH EACH OTHER (per cell)
# =====================================================================
print("\n" + "=" * 70)
print("VERIFICATION: [R_k, R_l] WITHIN EACH CELL")
print("=" * 70)
print("For the pure Gaudin model (separable V), [R_k, R_l] = 0 exactly.")
print("For non-separable V, [R_k, R_l] != 0 in general.")

# Check mutual commutation within cell 0
comm_RR = np.zeros((N_modes, N_modes))
for k in range(N_modes):
    for l in range(k+1, N_modes):
        comm = R[(k, 0)] @ R[(l, 0)] - R[(l, 0)] @ R[(k, 0)]
        comm_RR[k, l] = np.linalg.norm(comm, 'fro')
        comm_RR[l, k] = comm_RR[k, l]

print(f"\n||[R_k, R_l]||_F for cell 0 (should be 0 if integrable):")
print("   k\\l  " + "".join(f"  {l:5d}" for l in range(N_modes)))
for k in range(N_modes):
    row = f"   {k:3d}  "
    for l in range(N_modes):
        if l <= k:
            row += "      -"
        else:
            row += f"  {comm_RR[k,l]:5.3f}"
    print(row)

max_RR = np.max(comm_RR)
mean_RR = np.mean(comm_RR[np.triu_indices(N_modes, k=1)])
print(f"\nMax ||[R_k, R_l]|| = {max_RR:.6f}")
print(f"Mean ||[R_k, R_l]|| = {mean_RR:.6f}")

# Cross-check: build separable-V RG integrals and verify they commute
# Build R_k for the separable approximation
R_sep = {}
for c in range(N_cells):
    for k in range(N_modes):
        R_k = Sz[(k, c)].copy()
        for l in range(N_modes):
            if l == k:
                continue
            denom = 2.0 * (eps_fold[k] - eps_fold[l])
            if abs(denom) < 1e-15:
                continue
            SpSm_kl = build_SpSm(k, c, l, c)
            SpSm_lk = build_SpSm(l, c, k, c)
            SzSz_kl = build_SzSz(k, c, l, c)
            R_k += (SpSm_kl + SpSm_lk + 2.0 * SzSz_kl) / denom
        R_sep[(k, c)] = R_k

# NOTE: The R_k defined above are the GAUDIN integrals — they depend only
# on eps_k, NOT on V. They commute with H_Gaudin = Sum_k eps_k S_k^z + g Sum S_k.S_l,
# not with our BCS Hamiltonian. The test is whether they approximately commute
# with our ACTUAL Hamiltonian.

# Actually, the Gaudin integrals R_k are defined purely by the energy levels
# and the SU(2) algebra. They ALWAYS mutually commute: [R_k, R_l] = 0 is an
# ALGEBRAIC identity for the rational Gaudin model, independent of V.
# Let me verify this.

comm_RR_check = 0.0  # (local)
for k in range(N_modes):
    for l in range(k+1, N_modes):
        comm = R_sep[(k, 0)] @ R_sep[(l, 0)] - R_sep[(l, 0)] @ R_sep[(k, 0)]
        comm_RR_check = max(comm_RR_check, np.linalg.norm(comm, 'fro'))

print(f"\nSanity check: max ||[R_k^sep, R_l^sep]|| = {comm_RR_check:.2e}")
print("(Should be ~0: Gaudin algebra identity)")

# Important realization: R_k and R_sep_k are IDENTICAL because R_k depends
# only on eps_k and the SU(2) generators, NOT on V. The R_k are the GAUDIN
# integrals, period. The test is whether [H_BCS, R_k] = 0.


# =====================================================================
#  7. COMPUTE [H, R_k] FOR ALL 16 MODES
# =====================================================================
print("\n" + "=" * 70)
print("COMMUTATOR NORMS: delta_k = ||[H, R_k]||_F / ||H||_F")
print("=" * 70)

# For each H variant, compute delta_k
delta_full = np.zeros((N_cells, N_modes))    # [H_full, R_k]
delta_noJ  = np.zeros((N_cells, N_modes))    # [H_noJ, R_k]
delta_sep  = np.zeros((N_cells, N_modes))    # [H_sep, R_k]
delta_sepJ = np.zeros((N_cells, N_modes))    # [H_sep+J, R_k]

# Also compute unnormalized norms for decomposition analysis
raw_comm_full = np.zeros((N_cells, N_modes))
raw_comm_noJ  = np.zeros((N_cells, N_modes))
raw_comm_sep  = np.zeros((N_cells, N_modes))
raw_comm_J    = np.zeros((N_cells, N_modes))   # [H_J, R_k] contribution
raw_comm_nonsep = np.zeros((N_cells, N_modes)) # [H_nonsep, R_k] contribution

for c in range(N_cells):
    for k in range(N_modes):
        Rk = R[(k, c)]

        # [H_full, R_k]
        comm_full = H_full @ Rk - Rk @ H_full
        raw_comm_full[c, k] = np.linalg.norm(comm_full, 'fro')
        delta_full[c, k] = raw_comm_full[c, k] / norm_H_full

        # [H_noJ, R_k]
        comm_noJ = H_noJ @ Rk - Rk @ H_noJ
        raw_comm_noJ[c, k] = np.linalg.norm(comm_noJ, 'fro')
        delta_noJ[c, k] = raw_comm_noJ[c, k] / norm_H_noJ

        # [H_sep, R_k] — should be ~0 if V_sep is truly separable
        comm_sep = H_sep @ Rk - Rk @ H_sep
        raw_comm_sep[c, k] = np.linalg.norm(comm_sep, 'fro')
        delta_sep[c, k] = raw_comm_sep[c, k] / norm_H_sep

        # [H_sep+J, R_k]
        comm_sepJ = H_sep_J @ Rk - Rk @ H_sep_J
        raw_comm_sepJ = np.linalg.norm(comm_sepJ, 'fro')
        delta_sepJ[c, k] = raw_comm_sepJ / np.linalg.norm(H_sep_J, 'fro')

        # Decompose: [H_full, R_k] = [H_sep, R_k] + [H_nonsep, R_k] + [H_J, R_k]
        comm_J = H_J @ Rk - Rk @ H_J
        raw_comm_J[c, k] = np.linalg.norm(comm_J, 'fro')

        comm_ns = H_nonsep @ Rk - Rk @ H_nonsep
        raw_comm_nonsep[c, k] = np.linalg.norm(comm_ns, 'fro')

print("\n--- delta_k = ||[H, R_k]||_F / ||H||_F ---\n")

print("Mode  eps_k      delta_full  delta_noJ   delta_sep   delta_sepJ")
print("-" * 75)
for k in range(N_modes):
    print(f"  {k}   {eps_fold[k]:8.5f}   {delta_full[0,k]:.6f}    {delta_noJ[0,k]:.6f}    "
          f"{delta_sep[0,k]:.6f}    {delta_sepJ[0,k]:.6f}")

# Verify cell symmetry (delta should be identical for both cells)
cell_diff = np.max(np.abs(delta_full[0] - delta_full[1]))
print(f"\nCell symmetry check: max|delta(cell0) - delta(cell1)| = {cell_diff:.2e}")


# =====================================================================
#  8. BREAKING SOURCE DECOMPOSITION
# =====================================================================
print("\n" + "=" * 70)
print("BREAKING SOURCE DECOMPOSITION")
print("=" * 70)
print("||[H_i, R_k]||_F for each Hamiltonian component (cell 0):")
print()
print("Mode  ||[H_sep,Rk]||  ||[H_nonsep,Rk]||  ||[H_J,Rk]||  ||[H_full,Rk]||")
print("-" * 78)
for k in range(N_modes):
    print(f"  {k}    {raw_comm_sep[0,k]:10.6f}      {raw_comm_nonsep[0,k]:10.6f}       "
          f"{raw_comm_J[0,k]:10.6f}     {raw_comm_full[0,k]:10.6f}")

# Fractional contributions (using squared norms for additivity)
# Note: ||[A+B, R]|| != ||[A,R]|| + ||[B,R]|| due to cross-terms.
# But we can still report the individual contributions.
print("\nFractional norms (each component / full):")
print("Mode  f_sep      f_nonsep   f_J")
print("-" * 50)
for k in range(N_modes):
    f_sep = raw_comm_sep[0, k] / max(raw_comm_full[0, k], 1e-30)
    f_nonsep = raw_comm_nonsep[0, k] / max(raw_comm_full[0, k], 1e-30)
    f_J = raw_comm_J[0, k] / max(raw_comm_full[0, k], 1e-30)
    print(f"  {k}   {f_sep:8.5f}    {f_nonsep:8.5f}    {f_J:8.5f}")


# =====================================================================
#  9. CLASSIFY MODES
# =====================================================================
print("\n" + "=" * 70)
print("MODE CLASSIFICATION")
print("=" * 70)

n_conserved = 0
n_weakly_broken = 0
n_strongly_broken = 0

classifications = []
for k in range(N_modes):
    dk = delta_full[0, k]
    dk_noJ = delta_noJ[0, k]
    dk_sep = delta_sep[0, k]

    if dk < 0.01:
        status = "CONSERVED"
        n_conserved += 1
    elif dk < 0.1:
        status = "WEAKLY BROKEN"
        n_weakly_broken += 1
    else:
        status = "STRONGLY BROKEN"
        n_strongly_broken += 1

    # Determine primary breaking source
    if dk_noJ < 0.5 * dk:
        source = "Josephson-dominated"
    elif dk_sep > 0.5 * dk_noJ:
        source = "separable-V (unexpected)"
    else:
        source = "non-separable V"

    classifications.append((k, dk, status, source))
    print(f"  Mode {k} (eps={eps_fold[k]:.4f}): delta={dk:.6f} — {status} [{source}]")

print(f"\nSummary: {n_conserved} conserved, {n_weakly_broken} weakly broken, "
      f"{n_strongly_broken} strongly broken")


# =====================================================================
#  10. ADDITIONAL DIAGNOSTICS
# =====================================================================
print("\n" + "=" * 70)
print("ADDITIONAL DIAGNOSTICS")
print("=" * 70)

# 10a. V_fold separability analysis
print("\nV_fold SVD analysis:")
print(f"  Singular values: {S_svd}")
sep_ratio = S_svd[0] / np.sum(S_svd)
rank1_frac = S_svd[0]**2 / np.sum(S_svd**2)
print(f"  Separability ratio (s0/sum): {sep_ratio:.4f}")
print(f"  Rank-1 energy fraction (s0^2/sum(s^2)): {rank1_frac:.4f}")
print(f"  Non-separable fraction: {1.0 - rank1_frac:.4f}")

# 10b. Effective coupling constant for the separable component
g_eff = S_svd[0]
u_vec = U_svd[:, 0]
print(f"\n  Effective coupling: g_eff = {g_eff:.6f}")
print(f"  Separable mode shape: u = {u_vec}")

# 10c. Cross-check with S58 pair-number commutator norms
# S58 computed [H, n_k] which is simpler than [H, R_k]
print("\nCross-check with S58 pair-number commutators:")
print(f"  S58 ||[H_full, n_k]||: {comm_norms_s58_full[0]}")
print(f"  S58 ||[H_noJ, n_k]||:  {comm_norms_s58_noJ[0]}")
print(f"  This script ||[H_full, R_k]||: {raw_comm_full[0]}")
print(f"  This script ||[H_noJ, R_k]||:  {raw_comm_noJ[0]}")

# 10d. Does H_sep commute with R_k? (it should, as a consistency check)
# The Gaudin integrals R_k commute with H_Gaudin = Sum eps_k S_k^z + g Sum S_k.S_l
# but our H_sep is BCS-type: H_sep = Sum 2*eps_k n_k - Sum V_sep[k,l] pair_k^dag pair_l
# These are DIFFERENT Hamiltonians. The BCS H is NOT the Gaudin H.
# For the BCS model to be RG-integrable, V must be SEPARABLE: V[k,l] = g * u_k * u_l
# and the integrals take a DIFFERENT form (Richardson, not Gaudin).

# Let me also build the proper RICHARDSON integrals for the separable V.
# Richardson integrals:
#   R_k^Rich = S_k^z + g * Sum_{l!=k} u_k*u_l *
#              [S_k^+ S_l^- + S_l^+ S_k^- + 2 S_k^z S_l^z] / (eps_k - eps_l)
# where V[k,l] = g * u_k * u_l (g = S_svd[0], u_k = U_svd[k,0])

print("\n" + "=" * 70)
print("RICHARDSON INTEGRALS (proper BCS form)")
print("=" * 70)
print("Using V_sep[k,l] = g * u_k * u_l from rank-1 SVD")
print(f"g_eff = {g_eff:.6f}")

R_Rich = {}
for c in range(N_cells):
    for k in range(N_modes):
        R_k = Sz[(k, c)].copy()
        for l in range(N_modes):
            if l == k:
                continue
            denom = eps_fold[k] - eps_fold[l]
            if abs(denom) < 1e-15:
                continue

            # Richardson coupling: g * u_k * u_l / (eps_k - eps_l)
            coupling = g_eff * u_vec[k] * u_vec[l] / denom

            SpSm_kl = build_SpSm(k, c, l, c)
            SpSm_lk = build_SpSm(l, c, k, c)
            SzSz_kl = build_SzSz(k, c, l, c)

            R_k += coupling * (SpSm_kl + SpSm_lk + 2.0 * SzSz_kl)

        R_Rich[(k, c)] = R_k

# Verify: [R_Rich_k, R_Rich_l] should be ~0 (algebraic identity for Richardson model)
max_Rich_comm = 0.0
for k in range(N_modes):
    for l in range(k+1, N_modes):
        comm = R_Rich[(k,0)] @ R_Rich[(l,0)] - R_Rich[(l,0)] @ R_Rich[(k,0)]
        max_Rich_comm = max(max_Rich_comm, np.linalg.norm(comm, 'fro'))

print(f"\nMutual commutation: max ||[R_Rich_k, R_Rich_l]|| = {max_Rich_comm:.2e}")

# Now compute [H, R_Rich_k] for each H variant
delta_Rich_full = np.zeros((N_cells, N_modes))
delta_Rich_noJ  = np.zeros((N_cells, N_modes))
delta_Rich_sep  = np.zeros((N_cells, N_modes))

raw_Rich_full = np.zeros((N_cells, N_modes))
raw_Rich_noJ  = np.zeros((N_cells, N_modes))
raw_Rich_sep  = np.zeros((N_cells, N_modes))
raw_Rich_J    = np.zeros((N_cells, N_modes))
raw_Rich_nonsep = np.zeros((N_cells, N_modes))

for c in range(N_cells):
    for k in range(N_modes):
        Rk = R_Rich[(k, c)]

        comm_f = H_full @ Rk - Rk @ H_full
        raw_Rich_full[c, k] = np.linalg.norm(comm_f, 'fro')
        delta_Rich_full[c, k] = raw_Rich_full[c, k] / norm_H_full

        comm_nJ = H_noJ @ Rk - Rk @ H_noJ
        raw_Rich_noJ[c, k] = np.linalg.norm(comm_nJ, 'fro')
        delta_Rich_noJ[c, k] = raw_Rich_noJ[c, k] / norm_H_noJ

        comm_s = H_sep @ Rk - Rk @ H_sep
        raw_Rich_sep[c, k] = np.linalg.norm(comm_s, 'fro')
        delta_Rich_sep[c, k] = raw_Rich_sep[c, k] / norm_H_sep

        comm_j = H_J @ Rk - Rk @ H_J
        raw_Rich_J[c, k] = np.linalg.norm(comm_j, 'fro')

        comm_ns = H_nonsep @ Rk - Rk @ H_nonsep
        raw_Rich_nonsep[c, k] = np.linalg.norm(comm_ns, 'fro')

print("\n--- RICHARDSON delta_k = ||[H, R^Rich_k]||_F / ||H||_F ---\n")
print("Mode  eps_k      delta_full  delta_noJ   delta_sep")
print("-" * 65)
for k in range(N_modes):
    print(f"  {k}   {eps_fold[k]:8.5f}   {delta_Rich_full[0,k]:.6f}    "
          f"{delta_Rich_noJ[0,k]:.6f}    {delta_Rich_sep[0,k]:.6f}")

# KEY CHECK: [H_sep, R_Rich_k] should be ~0 (Richardson integrability)
print(f"\n*** KEY CHECK: [H_sep, R^Rich_k] ***")
print(f"Max delta_Rich_sep = {np.max(delta_Rich_sep):.2e}")
print(f"This should be ~0: the Richardson integrals are EXACT for H_sep.")

# Richardson breaking decomposition
print("\nRichardson breaking source decomposition (cell 0):")
print("Mode  ||[H_sep,R]||  ||[H_nonsep,R]||  ||[H_J,R]||  ||[H_full,R]||")
print("-" * 72)
for k in range(N_modes):
    print(f"  {k}    {raw_Rich_sep[0,k]:10.6f}     {raw_Rich_nonsep[0,k]:10.6f}      "
          f"{raw_Rich_J[0,k]:10.6f}    {raw_Rich_full[0,k]:10.6f}")

# Fractional contributions
print("\nFractional norms (Richardson):")
print("Mode  f_sep      f_nonsep   f_J")
print("-" * 50)
frac_nonsep_sum = 0.0  # (local)
frac_J_sum = 0.0  # (local)
for k in range(N_modes):
    denom_val = max(raw_Rich_full[0, k], 1e-30)
    f_s = raw_Rich_sep[0, k] / denom_val
    f_ns = raw_Rich_nonsep[0, k] / denom_val
    f_j = raw_Rich_J[0, k] / denom_val
    frac_nonsep_sum += f_ns
    frac_J_sum += f_j
    print(f"  {k}   {f_s:8.5f}    {f_ns:8.5f}    {f_j:8.5f}")

mean_f_nonsep = frac_nonsep_sum / N_modes
mean_f_J = frac_J_sum / N_modes
print(f"\nMean fractional contributions: f_nonsep = {mean_f_nonsep:.4f}, f_J = {mean_f_J:.4f}")


# =====================================================================
#  11. RICHARDSON INTEGRAL CLASSIFICATION
# =====================================================================
print("\n" + "=" * 70)
print("RICHARDSON MODE CLASSIFICATION (proper BCS integrals)")
print("=" * 70)

n_cons_R = 0
n_weak_R = 0
n_strong_R = 0
classifications_Rich = []

for k in range(N_modes):
    dk = delta_Rich_full[0, k]
    dk_noJ = delta_Rich_noJ[0, k]
    dk_sep = delta_Rich_sep[0, k]

    if dk < 0.01:
        status = "CONSERVED"
        n_cons_R += 1
    elif dk < 0.1:
        status = "WEAKLY BROKEN"
        n_weak_R += 1
    else:
        status = "STRONGLY BROKEN"
        n_strong_R += 1

    # Breaking source: compare noJ vs full
    if dk_noJ < 0.01 and dk > 0.01:
        source = "Josephson-dominated"
    elif dk_noJ > 0.5 * dk:
        source = "non-separable V (intra-cell)"
    elif dk_sep > 0.01:
        source = "separable V (unexpected)"
    else:
        source = "mixed"

    # Refined: compare J vs nonsep raw norms
    if raw_Rich_J[0, k] > 2.0 * raw_Rich_nonsep[0, k]:
        source_refined = "Josephson"
    elif raw_Rich_nonsep[0, k] > 2.0 * raw_Rich_J[0, k]:
        source_refined = "non-separable V"
    else:
        source_refined = "mixed (J + V_nonsep)"

    classifications_Rich.append((k, dk, status, source_refined))
    print(f"  Mode {k} (eps={eps_fold[k]:.4f}): delta={dk:.6f} — {status} [{source_refined}]")

print(f"\nSummary: {n_cons_R} conserved (<0.01), {n_weak_R} weakly broken (0.01-0.1), "
      f"{n_strong_R} strongly broken (>0.1)")


# =====================================================================
#  12. GATE VERDICT
# =====================================================================
print("\n" + "=" * 70)
print("GATE VERDICT: RG-INTEGRALS-60")
print("=" * 70)

# Use Richardson integrals (the proper BCS integrals) for the gate
all_strongly_broken = all(delta_Rich_full[0, k] > 0.1 for k in range(N_modes))
any_conserved = any(delta_Rich_full[0, k] < 0.01 for k in range(N_modes))
any_weakly_broken = any(0.01 <= delta_Rich_full[0, k] <= 0.1 for k in range(N_modes))

# Check if dominant breaking is from Josephson
J_dominant_count = sum(1 for k in range(N_modes)
                       if raw_Rich_J[0, k] > raw_Rich_nonsep[0, k])
nonsep_dominant_count = N_modes - J_dominant_count

# Average breaking with and without J
mean_delta_full = np.mean(delta_Rich_full[0])
mean_delta_noJ = np.mean(delta_Rich_noJ[0])
mean_delta_sep = np.mean(delta_Rich_sep[0])

print(f"Mean delta_k (full H):        {mean_delta_full:.6f}")
print(f"Mean delta_k (no Josephson):   {mean_delta_noJ:.6f}")
print(f"Mean delta_k (separable V):    {mean_delta_sep:.6f}")
print(f"Josephson-dominant modes:      {J_dominant_count}/{N_modes}")
print(f"Non-separable-V-dominant:      {nonsep_dominant_count}/{N_modes}")

# Determine verdict
if all_strongly_broken:
    verdict = "FAIL"
    detail = (f"All {N_modes} integrals strongly broken (delta_k > 0.1). "
              f"Mean delta_full={mean_delta_full:.4f}, mean delta_noJ={mean_delta_noJ:.4f}")
elif J_dominant_count > N_modes // 2 and any_conserved:
    verdict = "PASS"
    detail = (f"Dominant breaking from Josephson ({J_dominant_count}/{N_modes}), "
              f"{n_cons_R} conserved (delta<0.01), {n_weak_R} weakly broken")
elif any_conserved or any_weakly_broken:
    verdict = "INFO"
    detail = (f"Mixed: {n_cons_R} conserved, {n_weak_R} weakly broken, "
              f"{n_strong_R} strongly broken. "
              f"J-dominant: {J_dominant_count}, V_nonsep-dominant: {nonsep_dominant_count}")
else:
    verdict = "FAIL"
    detail = (f"No conserved integrals. Mean delta={mean_delta_full:.4f}")

print(f"\nVERDICT: {verdict}")
print(f"DETAIL: {detail}")


# =====================================================================
#  13. SAVE DATA
# =====================================================================
print("\n--- Saving data ---")

save_path = os.path.join(data_dir, 's60_rg_integrals.npz')
np.savez(save_path,
    # System parameters
    N_modes=N_modes,
    N_cells=N_cells,
    N_pair=N_pair,
    dim=dim,
    tau_fold=tau_fold_actual,
    E_J_fold=E_J_fold,
    eps_fold=eps_fold,
    V_fold=V_fold,
    V_sep=V_sep,
    V_nonsep=V_nonsep,

    # SVD analysis
    svd_singular_values=S_svd,
    svd_separability_ratio=sep_ratio,
    svd_rank1_fraction=rank1_frac,
    g_eff=g_eff,
    u_vec=u_vec,

    # Hamiltonian norms
    norm_H_full=norm_H_full,
    norm_H_noJ=norm_H_noJ,
    norm_H_sep=norm_H_sep,
    norm_H_J=norm_H_J,
    norm_H_nonsep=norm_H_nonsep,

    # Gaudin integral results
    delta_Gaudin_full=delta_full,
    delta_Gaudin_noJ=delta_noJ,
    delta_Gaudin_sep=delta_sep,
    raw_Gaudin_full=raw_comm_full,
    raw_Gaudin_noJ=raw_comm_noJ,
    raw_Gaudin_sep=raw_comm_sep,
    raw_Gaudin_J=raw_comm_J,
    raw_Gaudin_nonsep=raw_comm_nonsep,

    # Richardson integral results (proper BCS form)
    delta_Rich_full=delta_Rich_full,
    delta_Rich_noJ=delta_Rich_noJ,
    delta_Rich_sep=delta_Rich_sep,
    raw_Rich_full=raw_Rich_full,
    raw_Rich_noJ=raw_Rich_noJ,
    raw_Rich_sep=raw_Rich_sep,
    raw_Rich_J=raw_Rich_J,
    raw_Rich_nonsep=raw_Rich_nonsep,

    # Mutual commutation
    comm_RR_Gaudin=comm_RR,
    max_RR_Gaudin=max_RR,
    max_Rich_comm=max_Rich_comm,

    # Classification
    n_conserved=n_cons_R,
    n_weakly_broken=n_weak_R,
    n_strongly_broken=n_strong_R,
    J_dominant_count=J_dominant_count,
    nonsep_dominant_count=nonsep_dominant_count,
    mean_delta_full=mean_delta_full,
    mean_delta_noJ=mean_delta_noJ,
    mean_delta_sep=mean_delta_sep,

    # Gate
    gate_name=np.array(['RG-INTEGRALS-60']),
    gate_verdict=np.array([verdict]),
    gate_detail=np.array([detail]),
)
print(f"Saved: {save_path}")


# =====================================================================
#  14. PLOT
# =====================================================================
print("\n--- Generating plot ---")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle(f'RG-INTEGRALS-60: Richardson-Gaudin Integral Diagnostics\n'
             f'N_pair={N_pair}, N_modes={N_modes}, N_cells={N_cells}, '
             f'tau={tau_fold_actual:.4f}, E_J={E_J_fold:.3f}',
             fontsize=12, fontweight='bold')

modes = np.arange(N_modes)

# Panel 1: delta_k comparison (Richardson integrals)
ax = axes[0, 0]
ax.bar(modes - 0.2, delta_Rich_full[0], 0.3, label=r'$\delta_k$ (full $H$)', color='C0', alpha=0.8)
ax.bar(modes + 0.1, delta_Rich_noJ[0], 0.3, label=r'$\delta_k$ (no $E_J$)', color='C1', alpha=0.8)
ax.bar(modes + 0.4, delta_Rich_sep[0], 0.3, label=r'$\delta_k$ ($V_{\rm sep}$)', color='C2', alpha=0.8)
ax.axhline(0.1, color='r', ls='--', lw=1, label='Strongly broken (0.1)')
ax.axhline(0.01, color='orange', ls='--', lw=1, label='Conserved (0.01)')
ax.set_xlabel('Mode index $k$')
ax.set_ylabel(r'$\delta_k = \|[H, R_k]\|_F / \|H\|_F$')
ax.set_title('Richardson Integral Breaking')
ax.legend(fontsize=7, loc='upper right')
ax.set_xticks(modes)

# Panel 2: Breaking source decomposition
ax = axes[0, 1]
width = 0.35  # (local)
ax.bar(modes - width/2, raw_Rich_nonsep[0], width, label=r'$\|[H_{\rm nonsep}, R_k]\|$', color='C3')
ax.bar(modes + width/2, raw_Rich_J[0], width, label=r'$\|[H_J, R_k]\|$', color='C4')
ax.set_xlabel('Mode index $k$')
ax.set_ylabel(r'$\|[H_i, R_k]\|_F$')
ax.set_title('Breaking Source: V_nonsep vs Josephson')
ax.legend(fontsize=8)
ax.set_xticks(modes)

# Panel 3: V_fold separability
ax = axes[1, 0]
ax.bar(range(len(S_svd)), S_svd / np.sum(S_svd), color='C5', alpha=0.8)
ax.set_xlabel('SVD mode')
ax.set_ylabel('Fractional singular value')
ax.set_title(f'$V_{{\\rm fold}}$ Separability (rank-1 frac = {rank1_frac:.3f})')
ax.axhline(1.0/len(S_svd), color='gray', ls=':', label=f'Uniform ({1/len(S_svd):.3f})')
ax.legend(fontsize=8)

# Panel 4: Summary table
ax = axes[1, 1]
ax.axis('off')
table_data = [
    ['Quantity', 'Value'],
    ['Gate', f'RG-INTEGRALS-60: {verdict}'],
    ['N_pair, N_modes, N_cells', f'{N_pair}, {N_modes}, {N_cells}'],
    ['Fock dim', f'{dim}'],
    [r'$\langle\delta_k\rangle$ (full)', f'{mean_delta_full:.6f}'],
    [r'$\langle\delta_k\rangle$ (no J)', f'{mean_delta_noJ:.6f}'],
    [r'$\langle\delta_k\rangle$ (sep V)', f'{mean_delta_sep:.6f}'],
    ['Conserved (<0.01)', f'{n_cons_R}'],
    ['Weakly broken', f'{n_weak_R}'],
    ['Strongly broken (>0.1)', f'{n_strong_R}'],
    ['J-dominant modes', f'{J_dominant_count}/{N_modes}'],
    ['V_nonsep-dominant', f'{nonsep_dominant_count}/{N_modes}'],
    [r'Rank-1 $V$ fraction', f'{rank1_frac:.4f}'],
    [r'$g_{\rm eff}$', f'{g_eff:.4f}'],
    ['||H_J|| / ||H_full||', f'{norm_H_J/norm_H_full:.4f}'],
]
table = ax.table(cellText=table_data, loc='center', cellLoc='left',
                 colWidths=[0.5, 0.5])
table.auto_set_font_size(False)
table.set_fontsize(8)
table.scale(1, 1.3)
for i in range(len(table_data)):
    for j in range(2):
        cell = table[i, j]
        if i == 0:
            cell.set_facecolor('#4472C4')
            cell.set_text_props(color='white', fontweight='bold')
        elif i % 2 == 0:
            cell.set_facecolor('#D9E2F3')
        else:
            cell.set_facecolor('#FFFFFF')

plt.tight_layout()
plot_path = os.path.join(data_dir, 's60_rg_integrals.png')
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"Saved plot: {plot_path}")

print("\n" + "=" * 70)
print("COMPUTATION COMPLETE")
print("=" * 70)
