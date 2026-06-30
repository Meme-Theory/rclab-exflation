#!/usr/bin/env python3
"""
s60_pair_transfer_n4.py — Pair Transfer Matrix Elements S_+(N) for N=1,2,3,4
=============================================================================

Gate: PAIR-TRANSFER-N4-60
  PASS: 2-cell S_+(1) within factor 2 of 1-cell (1.013)
  FAIL: 2-cell S_+(1) < 0.01
  INFO: 2-cell S_+(1) > 2

Physics:
  The pair-transfer spectroscopic amplitude measures the ease with which
  the system changes its Cooper pair number. In nuclear physics (Paper 18,
  pair transfer spectroscopy), this is the (p,t) or (t,p) reaction cross
  section between adjacent isotopes. The amplitude is:

    P_k(N -> N+1) = <N+1, GS| S_k^+ |N, GS>

  where S_k^+ creates a Cooper pair in mode k of cell 0. The total
  pair-addition strength is:

    S_+(N) = sum_k |P_k(N -> N+1)|^2

  This quantity determines:
  - CC stability: If S_+(1) ~ O(1), N_pair can fluctuate; if << 1, pinned.
  - DM lifetime: Pair-transfer rate ~ S_+ * |V_transfer|^2 * rho_final.
  - Screening: N_pair dynamics as potential backreaction channel.

  The S59 Mack-Landau workshop computed single-cell S_+(1) = 1.013. This
  script extends to the full 2-cell system with Josephson coupling and
  computes S_+(N) and S_-(N) for all accessible N transitions.

Method:
  1. Build H for N_pair = 0,1,2,3,4 in the 2-cell pair Fock space
  2. Exact diagonalization for ground state of each sector
  3. Construct pair-addition operator S_k^+ (cell 0, mode k)
  4. Compute overlap <N+1,GS|S_k^+|N,GS> for each k
  5. Sum: S_+(N), S_-(N)
  6. Compare 2-cell S_+(1) to workshop 1-cell result (1.013)
  7. Nuclear pair-transfer sum rule cross-check

Session: S60
Agent: nazarewicz-nuclear-structure-theorist
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
from canonical_constants import (
    tau_fold, E_cond, N_dof_BCS, t_Planck, t_universe_s,
    hbar_GeV_s, M_KK
)

# =====================================================================
#  1. LOAD INPUT DATA
# =====================================================================

data_dir = os.path.dirname(os.path.abspath(__file__))

# S56 GGE fabric data (2-cell system at fold)
d56 = np.load(os.path.join(data_dir, 's56_gge_fabric.npz'), allow_pickle=True)
eps_fold = d56['eps_fold']       # 8 single-particle energies at fold
V_fold   = d56['V_fold']        # 8x8 pairing matrix
E_J_fold = float(d56['E_J_fold'])  # Josephson coupling at fold
tau_fold_actual = float(d56['tau_fold_actual'])

N_modes = 8  # modes per cell (local)
N_cells = 2   # cells
N_slots = N_modes * N_cells  # 16 pair-slots total

print("=" * 70)
print("S60: Pair Transfer Matrix Elements — PAIR-TRANSFER-N4-60")
print("=" * 70)
print(f"tau_fold = {tau_fold_actual:.6f}")
print(f"E_J_fold = {E_J_fold:.4f} M_KK")
print(f"N_modes/cell = {N_modes}, N_cells = {N_cells}")
print(f"eps_fold = {eps_fold}")
print(f"V_fold diagonal = {np.diag(V_fold)}")


# =====================================================================
#  2. FOCK SPACE CONSTRUCTION FOR ARBITRARY N_pair
# =====================================================================

def slot_to_mode_cell(s):
    """Convert pair-slot index to (mode_index, cell_index).
    Slot 0..7 = cell 0, modes 0..7.
    Slot 8..15 = cell 1, modes 0..7."""
    return (s % N_modes, s // N_modes)


def build_fock_space(n_pair):
    """Build pair Fock space for n_pair pairs in N_slots=16 slots.
    Returns (pair_states, state_index, dim)."""
    if n_pair == 0:
        # Single vacuum state
        return [()], {(): 0}, 1
    states = list(combinations(range(N_slots), n_pair))
    index = {s: i for i, s in enumerate(states)}
    return states, index, len(states)


def build_hamiltonian(n_pair, eps, V, E_J):
    """Build the BCS + Josephson Hamiltonian for n_pair pairs on 2 cells.

    H = H_kinetic + H_pairing + H_Josephson

    H_kinetic: 2*eps[mode] per occupied pair-slot
    H_pairing: -V[k,l] scatters pair from mode l to mode k within same cell
    H_Josephson: -(E_J/2)(B_0^dag B_1 + h.c.), collective tunneling

    Returns H as (dim, dim) array, or scalar 0.0 for N=0.
    """
    if n_pair == 0:
        return np.array([[0.0]])

    pair_states, state_index, dim = build_fock_space(n_pair)
    H = np.zeros((dim, dim), dtype=np.float64)

    for i, slots_i in enumerate(pair_states):
        slots_set = set(slots_i)
        infos = [slot_to_mode_cell(s) for s in slots_i]

        # --- Diagonal: kinetic energy ---
        for (mk, ck) in infos:
            H[i, i] += 2.0 * eps[mk]

        # --- Pairing interaction (within each cell) ---
        for p_idx in range(n_pair):
            m_p, c_p = infos[p_idx]
            old_slot = c_p * N_modes + m_p

            for k in range(N_modes):
                new_slot = c_p * N_modes + k
                if k == m_p:
                    # Diagonal pairing
                    H[i, i] -= V[m_p, m_p]
                    continue
                if new_slot in slots_set:
                    continue  # Pauli blocked
                new_slots = list(slots_i)
                new_slots[new_slots.index(old_slot)] = new_slot
                new_state = tuple(sorted(new_slots))
                if new_state in state_index:
                    j = state_index[new_state]
                    H[j, i] -= V[k, m_p]

        # --- Josephson tunneling ---
        for p_idx in range(n_pair):
            m_p, c_p = infos[p_idx]
            old_slot = c_p * N_modes + m_p
            target_cell = 1 - c_p

            for l in range(N_modes):
                new_slot = target_cell * N_modes + l
                if new_slot in slots_set:
                    continue  # Pauli blocked
                new_slots = list(slots_i)
                new_slots[new_slots.index(old_slot)] = new_slot
                new_state = tuple(sorted(new_slots))
                if new_state in state_index:
                    j = state_index[new_state]
                    H[j, i] += -E_J / 2.0

    # Symmetrize
    H = 0.5 * (H + H.T)
    return H


# =====================================================================
#  3. DIAGONALIZE ALL N-SECTORS
# =====================================================================

print("\n" + "=" * 70)
print("  DIAGONALIZING N-PAIR SECTORS 0 through 5")
print("=" * 70)

max_N = 5  # Go to N=5 so we can compute S_+(4)
gs_energies = {}
gs_vectors = {}
fock_spaces = {}
dimensions = {}

for N in range(max_N + 1):
    pair_states_N, state_index_N, dim_N = build_fock_space(N)
    fock_spaces[N] = (pair_states_N, state_index_N, dim_N)
    dimensions[N] = dim_N

    print(f"\nN_pair = {N}: dim = {dim_N}")

    if dim_N == 0:
        print(f"  Empty sector, skipping")
        continue

    H = build_hamiltonian(N, eps_fold, V_fold, E_J_fold)

    if dim_N == 1:
        gs_energies[N] = H[0, 0]
        gs_vectors[N] = np.array([1.0])
        print(f"  E_GS = {H[0,0]:.6f} M_KK")
    else:
        # Diagonalize — only need lowest few eigenvalues
        n_eig = min(10, dim_N)
        evals, evecs = eigh(H, subset_by_index=[0, n_eig - 1])
        gs_energies[N] = evals[0]
        gs_vectors[N] = evecs[:, 0]
        gap = evals[1] - evals[0] if n_eig > 1 else float('inf')
        print(f"  E_GS = {evals[0]:.6f} M_KK, gap = {gap:.6f} M_KK")
        print(f"  First 5 evals: {evals[:5]}")

    # Verify hermiticity
    if dim_N > 1:
        herm_err = np.max(np.abs(H - H.T))
        print(f"  Hermiticity check: max|H-H^T| = {herm_err:.2e}")


# =====================================================================
#  4. CONSTRUCT PAIR-TRANSFER OPERATORS AND COMPUTE MATRIX ELEMENTS
# =====================================================================

print("\n" + "=" * 70)
print("  PAIR TRANSFER MATRIX ELEMENTS")
print("=" * 70)


def compute_pair_addition(N, cell=0):
    """Compute pair-addition matrix elements S_k^+:
    P_k = <N+1, GS| S_k^+(cell) |N, GS>

    S_k^+(cell) adds a Cooper pair in mode k of the specified cell.
    This maps an N-pair state to an (N+1)-pair state.

    Returns:
      P_k: array of shape (N_modes,) — transfer amplitudes per mode
      S_plus: total strength sum_k |P_k|^2
    """
    pair_states_N, state_index_N, dim_N = fock_spaces[N]
    pair_states_Np1, state_index_Np1, dim_Np1 = fock_spaces[N + 1]

    psi_N = gs_vectors[N]      # dim_N vector
    psi_Np1 = gs_vectors[N + 1]  # dim_Np1 vector

    P_k = np.zeros(N_modes, dtype=np.float64)

    for k in range(N_modes):
        # S_k^+(cell) adds a pair in slot (cell * N_modes + k)
        new_slot = cell * N_modes + k

        # Build the action of S_k^+ on each basis state |alpha> in N-sector
        # S_k^+ |alpha> = |alpha with new_slot added> if new_slot not in alpha
        #               = 0 if new_slot already in alpha (Pauli blocked)

        # The overlap is: <N+1,GS| S_k^+ |N,GS>
        #   = sum_alpha psi_N[alpha] * sum_beta delta(S_k^+ |alpha> = |beta>) * psi_Np1[beta]
        #   = sum_alpha psi_N[alpha] * psi_Np1[index of |alpha + new_slot>]

        amplitude = 0.0
        for i_alpha, slots_alpha in enumerate(pair_states_N):
            if new_slot in set(slots_alpha):
                continue  # Pauli blocked: pair already in this mode

            # New state: insert new_slot into the occupation list
            new_state = tuple(sorted(list(slots_alpha) + [new_slot]))

            if new_state in state_index_Np1:
                j_beta = state_index_Np1[new_state]

                # Sign from pair ordering: pairs are bosonic composites,
                # no fermionic sign. The pair creation operator has no
                # additional phase (all pairs are spin-singlet, K_7-neutral).
                amplitude += psi_N[i_alpha] * psi_Np1[j_beta]

        P_k[k] = amplitude

    S_plus = np.sum(P_k**2)
    return P_k, S_plus


def compute_pair_removal(N, cell=0):
    """Compute pair-removal matrix elements S_k^-:
    P_k = <N-1, GS| S_k^-(cell) |N, GS>

    S_k^-(cell) removes a Cooper pair from mode k of the specified cell.

    Returns:
      P_k: array of shape (N_modes,) — removal amplitudes per mode
      S_minus: total strength sum_k |P_k|^2
    """
    if N == 0:
        return np.zeros(N_modes), 0.0

    pair_states_N, state_index_N, dim_N = fock_spaces[N]
    pair_states_Nm1, state_index_Nm1, dim_Nm1 = fock_spaces[N - 1]

    psi_N = gs_vectors[N]        # dim_N vector
    psi_Nm1 = gs_vectors[N - 1]  # dim_Nm1 vector

    P_k = np.zeros(N_modes, dtype=np.float64)

    for k in range(N_modes):
        # S_k^-(cell) removes a pair from slot (cell * N_modes + k)
        rm_slot = cell * N_modes + k

        amplitude = 0.0
        for i_alpha, slots_alpha in enumerate(pair_states_N):
            if rm_slot not in set(slots_alpha):
                continue  # Nothing to remove

            # New state: remove rm_slot from the occupation list
            new_slots = list(slots_alpha)
            new_slots.remove(rm_slot)
            new_state = tuple(sorted(new_slots))

            if new_state in state_index_Nm1:
                j_beta = state_index_Nm1[new_state]
                amplitude += psi_N[i_alpha] * psi_Nm1[j_beta]

        P_k[k] = amplitude

    S_minus = np.sum(P_k**2)
    return P_k, S_minus


# =====================================================================
#  5. COMPUTE S_+(N) AND S_-(N) FOR ALL N
# =====================================================================

print("\n--- Pair-Addition Strengths S_+(N) [cell 0] ---")
S_plus_results = {}
P_plus_results = {}

for N in range(max_N):
    if N not in gs_vectors or (N + 1) not in gs_vectors:
        print(f"  N={N} -> N+1={N+1}: missing eigenvector, skipping")
        continue

    P_k, S_plus = compute_pair_addition(N, cell=0)
    S_plus_results[N] = S_plus
    P_plus_results[N] = P_k

    print(f"\n  S_+(N={N}): {N} -> {N+1}")
    print(f"    Mode-resolved |P_k|^2:")
    sector_labels = ['B2', 'B2', 'B2', 'B2', 'B1', 'B3', 'B3', 'B3']
    for k in range(N_modes):
        print(f"      k={k} ({sector_labels[k]}): P_k = {P_k[k]:+.6f}, |P_k|^2 = {P_k[k]**2:.6f}")
    print(f"    S_+(N={N}) = sum_k |P_k|^2 = {S_plus:.6f}")

# Also compute for cell 1 at N=1 as consistency check
P_k_c1, S_plus_c1 = compute_pair_addition(1, cell=1)
print(f"\n  Cell symmetry check: S_+(1, cell=0) = {S_plus_results[1]:.6f}")
print(f"                       S_+(1, cell=1) = {S_plus_c1:.6f}")
print(f"                       Ratio = {S_plus_results[1]/S_plus_c1:.6f} (should be 1.0)")


print("\n--- Pair-Removal Strengths S_-(N) [cell 0] ---")
S_minus_results = {}
P_minus_results = {}

for N in range(1, max_N + 1):
    if N not in gs_vectors or (N - 1) not in gs_vectors:
        print(f"  N={N} -> N-1={N-1}: missing eigenvector, skipping")
        continue

    P_k, S_minus = compute_pair_removal(N, cell=0)
    S_minus_results[N] = S_minus
    P_minus_results[N] = P_k

    print(f"\n  S_-(N={N}): {N} -> {N-1}")
    print(f"    Mode-resolved |P_k|^2:")
    for k in range(N_modes):
        print(f"      k={k} ({sector_labels[k]}): P_k = {P_k[k]:+.6f}, |P_k|^2 = {P_k[k]**2:.6f}")
    print(f"    S_-(N={N}) = sum_k |P_k|^2 = {S_minus:.6f}")


# =====================================================================
#  6. COMPARISON: 1-CELL vs 2-CELL
# =====================================================================

print("\n" + "=" * 70)
print("  1-CELL vs 2-CELL COMPARISON")
print("=" * 70)

S_plus_1cell_workshop = 1.013  # From S59 Mack-Landau workshop (Landau R2)  # (local)
S_plus_2cell = S_plus_results.get(1, float('nan'))

print(f"  1-cell S_+(1) [workshop]: {S_plus_1cell_workshop:.4f}")
print(f"  2-cell S_+(1) [this]:     {S_plus_2cell:.6f}")
ratio = S_plus_2cell / S_plus_1cell_workshop
print(f"  Ratio (2-cell / 1-cell):  {ratio:.4f}")
print(f"  Factor-2 window: [{S_plus_1cell_workshop/2:.4f}, {S_plus_1cell_workshop*2:.4f}]")

if S_plus_2cell < 0.01:
    gate_verdict = "FAIL"
    gate_detail = f"2-cell S_+(1) = {S_plus_2cell:.6f} < 0.01: pair transfer strongly suppressed"
elif S_plus_2cell > 2 * S_plus_1cell_workshop:
    gate_verdict = "INFO"
    gate_detail = f"2-cell S_+(1) = {S_plus_2cell:.6f} > 2x workshop value: Josephson enhancement"
elif S_plus_2cell > S_plus_1cell_workshop / 2:
    gate_verdict = "PASS"
    gate_detail = f"2-cell S_+(1) = {S_plus_2cell:.6f}, ratio = {ratio:.4f}: within factor 2 of 1-cell"
else:
    gate_verdict = "FAIL"
    gate_detail = f"2-cell S_+(1) = {S_plus_2cell:.6f}: below factor-2 window"

print(f"\n  GATE VERDICT: {gate_verdict}")
print(f"  DETAIL: {gate_detail}")


# =====================================================================
#  7. NUCLEAR PAIR-TRANSFER SUM RULE CHECK
# =====================================================================

print("\n" + "=" * 70)
print("  NUCLEAR PAIR-TRANSFER SUM RULE CHECK")
print("=" * 70)

# In nuclear physics (Yoshida 1962, Paper 18), the pair-transfer sum rule
# relates S_+(N) + S_-(N) to occupation number fluctuations:
#
#   S_+(N) + S_-(N) = sum_k (n_k(1-n_k) + ...) [approximate]
#
# For a BCS state: S_+(N) + S_-(N) = sum_k u_k^2 v_k^2 = (1/4) sum_k sin^2(2*theta_k)
# This is a measure of pairing correlations.
#
# More precisely, for the pair creation operator S_k^+ on cell 0:
#   S_k^+ S_k^- + S_k^- S_k^+ = n_k(cell0)(1 - n_k(cell0)) [not exact for interacting]
# The sum rule: sum_k {S_+(k) + S_-(k)} = sum_k n_k(1-n_k) holds for single-Slater states.
# For correlated ground states it is approximate.

for N in range(1, max_N):
    if N in S_plus_results and N in S_minus_results:
        total = S_plus_results[N] + S_minus_results[N]
        print(f"  N={N}: S_+(N) + S_-(N) = {S_plus_results[N]:.6f} + {S_minus_results[N]:.6f} = {total:.6f}")


# =====================================================================
#  8. ENERGY STAIRCASE
# =====================================================================

print("\n" + "=" * 70)
print("  ENERGY STAIRCASE E_GS(N)")
print("=" * 70)

for N in sorted(gs_energies.keys()):
    E = gs_energies[N]
    print(f"  N={N}: E_GS = {E:.6f} M_KK, dim = {dimensions[N]}")

print("\n  Two-neutron separation energies S_2n(N) = E(N-1) - E(N):")
S2n = {}
for N in range(1, max_N + 1):
    if N in gs_energies and (N - 1) in gs_energies:
        s2n = gs_energies[N - 1] - gs_energies[N]
        S2n[N] = s2n
        print(f"  S_2n(N={N}) = E({N-1}) - E({N}) = {s2n:.6f} M_KK")

print("\n  Odd-even staggering delta_3(N) = (-1)^N * [E(N+1) - 2*E(N) + E(N-1)] / 2:")
for N in range(1, max_N):
    if (N - 1) in gs_energies and N in gs_energies and (N + 1) in gs_energies:
        d3 = ((-1)**N) * (gs_energies[N + 1] - 2*gs_energies[N] + gs_energies[N - 1]) / 2.0
        print(f"  delta_3(N={N}) = {d3:.6f} M_KK")


# =====================================================================
#  9. PAIR TRANSFER vs OCCUPATION — BCS COHERENCE FACTORS
# =====================================================================

print("\n" + "=" * 70)
print("  PAIR TRANSFER vs BCS COHERENCE FACTORS")
print("=" * 70)

# For BCS ground state: P_k(N->N+1) = u_k(N+1) * v_k(N) approximately.
# We can extract effective u_k, v_k from occupations:
#   v_k^2(N) ~ n_k(N) = <N,GS| hat{n}_k |N,GS> / N (averaged per cell)

# Get occupations from data files
d58 = np.load(os.path.join(data_dir, 's58_npair2_integ.npz'), allow_pickle=True)
d59_3 = np.load(os.path.join(data_dir, 's59_npair3_integ.npz'), allow_pickle=True)
d59_4 = np.load(os.path.join(data_dir, 's59_therm_order.npz'), allow_pickle=True)

# N=2 occupations (cell 0)
nk_N2 = d58['nk_GS_2pair'][0]  # 8 modes, cell 0
nk_N3 = d59_3['nk_GS_3pair'][0]
nk_N4 = d59_4['nk_GS_4pair'][0]

print("\n  Occupations per mode (cell 0):")
print(f"  {'Mode':>4} {'Sector':>6} {'n_k(N=2)':>10} {'n_k(N=3)':>10} {'n_k(N=4)':>10}")
for k in range(N_modes):
    print(f"  {k:>4} {sector_labels[k]:>6} {nk_N2[k]:10.6f} {nk_N3[k]:10.6f} {nk_N4[k]:10.6f}")

# BCS prediction for S_+(N): if v_k^2 ~ n_k/N, u_k^2 ~ 1 - n_k/N,
# then |P_k(N->N+1)|^2 ~ u_k(N+1)^2 * v_k(N)^2 = (1-n_k(N+1)/(N+1)) * n_k(N)/N
# This is approximate because it assumes BCS coherence factors, which
# the ED may deviate from (especially at small N where BCS breaks down).

if 1 in P_plus_results and 2 in S_plus_results:
    print("\n  BCS approximation for S_+(1):")
    # We need n_k(N=1). From the S56 data: nk_GS is 16 elements, cell 0 = first 8
    nk_N1 = d56['nk_GS'][:N_modes]
    print(f"  n_k(N=1, cell 0) = {nk_N1}")
    for k in range(N_modes):
        v2_1 = nk_N1[k]
        u2_2 = 1.0 - nk_N2[k]
        bcs_pred = np.sqrt(u2_2 * v2_1)
        print(f"    k={k}: |P_k|_ED = {abs(P_plus_results[1][k]):.6f}, "
              f"|P_k|_BCS ~ sqrt(u_k^2(2)*v_k^2(1)) = {bcs_pred:.6f}")


# =====================================================================
#  10. PLOTTING
# =====================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 11))

# Panel (a): S_+(N) and S_-(N) vs N
ax = axes[0, 0]
Ns_plus = sorted(S_plus_results.keys())
Ns_minus = sorted(S_minus_results.keys())
ax.bar([N - 0.15 for N in Ns_plus], [S_plus_results[N] for N in Ns_plus],
       width=0.3, label=r'$S_+(N)$ (addition)', color='steelblue', alpha=0.8)  # (local)
ax.bar([N + 0.15 for N in Ns_minus], [S_minus_results[N] for N in Ns_minus],
       width=0.3, label=r'$S_-(N)$ (removal)', color='indianred', alpha=0.8)  # (local)
ax.axhline(y=S_plus_1cell_workshop, color='gray', linestyle='--', linewidth=1,
           label=f'1-cell $S_+(1)$ = {S_plus_1cell_workshop:.3f}')
ax.set_xlabel(r'$N_{\rm pair}$', fontsize=12)
ax.set_ylabel(r'$S_\pm(N)$', fontsize=12)
ax.set_title('(a) Pair Transfer Strength Functions', fontsize=12)
ax.legend(fontsize=9)
ax.set_xticks(range(max_N + 1))

# Panel (b): Mode-resolved |P_k|^2 for S_+(1)
ax = axes[0, 1]
if 1 in P_plus_results:
    Pk = P_plus_results[1]
    colors = ['#1f77b4', '#1f77b4', '#1f77b4', '#1f77b4',
              '#2ca02c', '#d62728', '#d62728', '#d62728']
    ax.bar(range(N_modes), Pk**2, color=colors, alpha=0.8, edgecolor='black', linewidth=0.5)
    ax.set_xlabel('Mode index k', fontsize=12)
    ax.set_ylabel(r'$|P_k(1 \to 2)|^2$', fontsize=12)
    ax.set_title(r'(b) Mode-Resolved $S_+(1)$: $N=1 \to 2$', fontsize=12)
    ax.set_xticks(range(N_modes))
    ax.set_xticklabels([f'{k}\n({sector_labels[k]})' for k in range(N_modes)], fontsize=9)

# Panel (c): Energy staircase
ax = axes[1, 0]
Ns_E = sorted(gs_energies.keys())
Es = [gs_energies[N] for N in Ns_E]
ax.plot(Ns_E, Es, 'ko-', markersize=8, linewidth=2)
for N, E in zip(Ns_E, Es):
    ax.annotate(f'{E:.3f}', (N, E), textcoords="offset points",
                xytext=(8, 5), fontsize=8)
ax.set_xlabel(r'$N_{\rm pair}$', fontsize=12)
ax.set_ylabel(r'$E_{\rm GS}(N)$ [M$_{\rm KK}$]', fontsize=12)
ax.set_title('(c) Ground State Energy Staircase', fontsize=12)
ax.set_xticks(range(max_N + 1))
ax.grid(True, alpha=0.3)

# Panel (d): Comparison of S_+(N) for addition at all N
ax = axes[1, 1]
# Mode-resolved for multiple N
mode_offsets = np.arange(N_modes)
width = 0.18  # (local)
for i, N in enumerate(sorted(P_plus_results.keys())):
    if N > 3:
        continue  # Too crowded
    Pk = P_plus_results[N]
    ax.bar(mode_offsets + i * width, Pk**2, width=width,
           label=f'$N={N} \\to {N+1}$', alpha=0.8)
ax.set_xlabel('Mode index k', fontsize=12)
ax.set_ylabel(r'$|P_k(N \to N+1)|^2$', fontsize=12)
ax.set_title(r'(d) Mode-Resolved $S_+$ at Multiple $N$', fontsize=12)
ax.set_xticks(mode_offsets + width)
ax.set_xticklabels([f'{k}\n({sector_labels[k]})' for k in range(N_modes)], fontsize=9)
ax.legend(fontsize=9)

plt.suptitle(f'PAIR-TRANSFER-N4-60: 2-Cell Pair Transfer Spectroscopy\n'
             f'$\\tau_{{\\rm fold}}$ = {tau_fold_actual:.4f}, $E_J$ = {E_J_fold:.3f} M$_{{\\rm KK}}$',
             fontsize=13, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.94])
plt.savefig(os.path.join(data_dir, 's60_pair_transfer_n4.png'), dpi=150, bbox_inches='tight')
print(f"\nPlot saved: s60_pair_transfer_n4.png")


# =====================================================================
#  11. SAVE DATA
# =====================================================================

save_path = os.path.join(data_dir, 's60_pair_transfer_n4.npz')

save_dict = {
    'N_modes': N_modes,
    'N_cells': N_cells,
    'N_slots': N_slots,
    'tau_fold': tau_fold_actual,
    'E_J_fold': E_J_fold,
    'eps_fold': eps_fold,
    'V_fold': V_fold,
    'S_plus_1cell_workshop': S_plus_1cell_workshop,
}

# Ground state energies and dimensions
for N in sorted(gs_energies.keys()):
    save_dict[f'E_GS_N{N}'] = gs_energies[N]
    save_dict[f'dim_N{N}'] = dimensions[N]

# Pair-addition results
for N in sorted(S_plus_results.keys()):
    save_dict[f'S_plus_N{N}'] = S_plus_results[N]
    save_dict[f'P_plus_N{N}'] = P_plus_results[N]

# Pair-removal results
for N in sorted(S_minus_results.keys()):
    save_dict[f'S_minus_N{N}'] = S_minus_results[N]
    save_dict[f'P_minus_N{N}'] = P_minus_results[N]

# Gate
save_dict['gate_name'] = np.array(['PAIR-TRANSFER-N4-60'])
save_dict['gate_verdict'] = np.array([gate_verdict])
save_dict['gate_detail'] = np.array([gate_detail])

np.savez(save_path, **save_dict)
print(f"Data saved: {save_path}")


# =====================================================================
#  12. SUMMARY
# =====================================================================

print("\n" + "=" * 70)
print("  SUMMARY — PAIR-TRANSFER-N4-60")
print("=" * 70)

print(f"\n  Gate: PAIR-TRANSFER-N4-60")
print(f"  Verdict: {gate_verdict}")
print(f"  Detail: {gate_detail}")

print(f"\n  Energy staircase:")
for N in sorted(gs_energies.keys()):
    E = gs_energies[N]
    label = " <-- GS minimum" if N == min(gs_energies, key=gs_energies.get) else ""
    print(f"    E_GS(N={N}) = {E:+.6f} M_KK  (dim={dimensions[N]}){label}")

print(f"\n  Pair-addition strengths:")
for N in sorted(S_plus_results.keys()):
    extra = ""
    if N == 1:
        extra = f"  [1-cell: {S_plus_1cell_workshop:.3f}, ratio: {S_plus_results[N]/S_plus_1cell_workshop:.3f}]"
    print(f"    S_+(N={N}) = {S_plus_results[N]:.6f}{extra}")

print(f"\n  Pair-removal strengths:")
for N in sorted(S_minus_results.keys()):
    print(f"    S_-(N={N}) = {S_minus_results[N]:.6f}")

print(f"\n  Nuclear analogy: S_+(N) is the (t,p) cross section measuring")
print(f"  pairing correlations between adjacent N-sectors. A large S_+")
print(f"  indicates strong pairing coherence (coherent superposition of")
print(f"  particle-hole excitations across the Fermi surface).")
print(f"  S_+(1) = O(1) means N_pair is NOT topologically locked.")
print(f"  Pinning is thermodynamic (energy minimum), not selection-rule.")

print("\n" + "=" * 70)
print("  COMPUTATION COMPLETE")
print("=" * 70)
