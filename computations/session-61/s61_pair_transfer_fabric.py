#!/usr/bin/env python3
"""
s61_pair_transfer_fabric.py — Pair-Transfer Scaling on Multi-Cell Fabrics
=========================================================================

Gate: PAIR-FABRIC-61
  PASS: bosonic scaling S_+(N) = (N+1)(1 - N/(2*N_slots))/2 holds < 10% at 8 cells
  FAIL: S_+(N) suppressed below (N+1)/2 at 8 cells
  INFO: intermediate (> (N+1)/2 but > 10% deviation from bosonic)

Physics:
  Tests whether single-cell BCS pair-transfer coherence survives on a
  multi-cell Josephson-coupled fabric. In nuclear physics (Paper 18),
  pair transfer between even-even neighbors follows:
    S_+(N) = sqrt(N_pair * (Omega - N_pair + 1))
  where Omega = pair degeneracy / 2. The bosonic limit (large Omega) gives:
    S_+(N) ~ (N+1)/2 * (1 - N/(2*Omega))
  which is the Pauli-corrected bosonic scaling found in S60.

  The Josephson coupling E_J = 3.397 M_KK >> V_pair ~ 0.08 M_KK, so
  pairs delocalize across cells. The question is: does this delocalization
  PRESERVE the bosonic scaling (as in a superfluid), or DESTROY it
  (as in a Mott insulator where pairs localize)?

Method:
  1. Effective 2-mode model per cell: modes extracted from B2(k=0) and B1(k=4)
  2. BCS pairing within each cell, Josephson hopping between adjacent cells
  3. Chain topology with open boundary conditions
  4. ED in N_pair sectors for N_cell = 1, 2, 4, 8
  5. Pair-transfer S_+(N) = sum_{k,c} |<N+1,GS| c†_{k,c,up} c†_{k,c,dn} |N,GS>|^2
  6. Mode uniformity: how does the pair spread across cells?

Session: S61
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
import time

# === Import canonical constants ===
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from canonical_constants import tau_fold, E_cond, M_KK

# =====================================================================
#  1. LOAD INPUT DATA AND CONSTRUCT 2-MODE EFFECTIVE MODEL
# =====================================================================

data_dir = os.path.dirname(os.path.abspath(__file__))

# Load S60 data for the full 8-mode V and eps
d60 = np.load(os.path.join(data_dir, 's60_pair_transfer_n4.npz'), allow_pickle=True)
eps_full = d60['eps_fold']       # 8 single-particle energies
V_full   = d60['V_fold']         # 8x8 pairing matrix
E_J_fold = float(d60['E_J_fold'])

# Extract 2-mode effective model: B2(k=0) and B1(k=4)
# These are the two modes closest to the Fermi surface (S53: B1 is Fermi-surface mode)
# B2(k=0): eps ~ 0, V[0,0] = 0.0255
# B1(k=4): eps = 0.726, V[4,4] = 0.0 (no diagonal pairing for B1)
# Cross-pairing: V[0,4] = V[4,0] = 0.0799 (dominant off-diagonal)
N_MODES = 2  # modes per cell (local)
eps_2mode = np.array([eps_full[0], eps_full[4]])
V_2mode = np.array([[V_full[0, 0], V_full[0, 4]],
                     [V_full[4, 0], V_full[4, 4]]])

print("=" * 72)
print("S61: Pair-Transfer Scaling on Multi-Cell Fabrics — PAIR-FABRIC-61")
print("=" * 72)
print(f"E_J_fold = {E_J_fold:.4f} M_KK")
print(f"2-mode effective model:")
print(f"  eps = [{eps_2mode[0]:.6f}, {eps_2mode[1]:.6f}] M_KK")
print(f"  V   = [[{V_2mode[0,0]:.6f}, {V_2mode[0,1]:.6f}],")
print(f"         [{V_2mode[1,0]:.6f}, {V_2mode[1,1]:.6f}]]")
print(f"  E_J / V_max = {E_J_fold / max(abs(V_2mode).max(), 1e-30):.1f} (Josephson dominates)")
print()

# =====================================================================
#  2. FOCK SPACE AND HAMILTONIAN FOR MULTI-CELL FABRIC
# =====================================================================

def build_fock_space(n_pair, n_slots):
    """Build pair Fock space: choose n_pair pair-slots from n_slots total.
    Returns (states_list, state_index_dict, dimension)."""
    if n_pair == 0:
        return [()], {(): 0}, 1
    if n_pair > n_slots:
        return [], {}, 0
    states = list(combinations(range(n_slots), n_pair))
    index = {s: i for i, s in enumerate(states)}
    return states, index, len(states)


def slot_to_mode_cell(s, n_modes):
    """Pair-slot s -> (mode_index, cell_index).
    Slots 0..n_modes-1 = cell 0, n_modes..2*n_modes-1 = cell 1, etc."""
    return (s % n_modes, s // n_modes)


def build_hamiltonian(n_pair, n_cells, eps, V, E_J, n_modes=N_MODES):
    """Build H = H_kinetic + H_pairing + H_Josephson for n_pair pairs
    on n_cells cells with n_modes modes per cell, chain topology.

    H_kinetic: 2*eps[mode] per occupied pair-slot
    H_pairing: -V[k,l] scatters pair from mode l to k WITHIN same cell
    H_Josephson: -(E_J/2) hops a pair between adjacent cells (any mode to any mode)
    """
    n_slots = n_modes * n_cells

    if n_pair == 0:
        return np.array([[0.0]]), [()], {(): 0}, 1

    pair_states, state_index, dim = build_fock_space(n_pair, n_slots)
    if dim == 0:
        return np.zeros((0, 0)), [], {}, 0

    H = np.zeros((dim, dim), dtype=np.float64)

    for i, slots_i in enumerate(pair_states):
        slots_set = set(slots_i)
        infos = [slot_to_mode_cell(s, n_modes) for s in slots_i]

        # --- Diagonal: kinetic energy ---
        for (mk, ck) in infos:
            H[i, i] += 2.0 * eps[mk]

        # --- Pairing interaction (within each cell) ---
        for p_idx in range(n_pair):
            m_p, c_p = infos[p_idx]
            old_slot = c_p * n_modes + m_p

            for k in range(n_modes):
                new_slot = c_p * n_modes + k
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

        # --- Josephson tunneling (between adjacent cells, chain topology) ---
        for p_idx in range(n_pair):
            m_p, c_p = infos[p_idx]
            old_slot = c_p * n_modes + m_p

            # Hop to adjacent cells (open boundary chain)
            for dc in [-1, +1]:
                c_target = c_p + dc
                if c_target < 0 or c_target >= n_cells:
                    continue  # boundary

                for l in range(n_modes):
                    new_slot = c_target * n_modes + l
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
    return H, pair_states, state_index, dim


def compute_pair_addition_all_cells(N, n_cells, fock_data, gs_vecs, n_modes=N_MODES):
    """Compute pair-addition S_+(N) summed over ALL modes and ALL cells.

    S_+(N) = sum_{k,c} |<N+1,GS| S_k^+(c) |N,GS>|^2

    Also returns per-cell and per-mode resolved amplitudes.
    """
    pair_states_N, state_index_N, dim_N = fock_data[N]
    pair_states_Np1, state_index_Np1, dim_Np1 = fock_data[N + 1]

    psi_N = gs_vecs[N]
    psi_Np1 = gs_vecs[N + 1]

    P_kc = np.zeros((n_modes, n_cells), dtype=np.float64)

    for c in range(n_cells):
        for k in range(n_modes):
            new_slot = c * n_modes + k
            amplitude = 0.0

            for i_alpha, slots_alpha in enumerate(pair_states_N):
                if new_slot in set(slots_alpha):
                    continue  # Pauli blocked

                new_state = tuple(sorted(list(slots_alpha) + [new_slot]))
                if new_state in state_index_Np1:
                    j_beta = state_index_Np1[new_state]
                    amplitude += psi_N[i_alpha] * psi_Np1[j_beta]

            P_kc[k, c] = amplitude

    # Total S_+
    S_plus = np.sum(P_kc**2)

    # Per-cell: sum over modes
    S_per_cell = np.sum(P_kc**2, axis=0)  # shape (n_cells,)

    # Per-mode: sum over cells
    S_per_mode = np.sum(P_kc**2, axis=1)  # shape (n_modes,)

    return P_kc, S_plus, S_per_cell, S_per_mode


# =====================================================================
#  3. MAIN COMPUTATION: SWEEP OVER N_CELLS = 1, 2, 4, 8
# =====================================================================

cell_configs = [1, 2, 4, 8]
max_N_pair = 4  # compute S_+(N) for N=0,1,2,3,4

# Storage
results = {}

for n_cells in cell_configs:
    n_slots = N_MODES * n_cells
    max_N_here = min(max_N_pair + 1, n_slots)  # need N+1 sector

    print("=" * 72)
    print(f"  N_cells = {n_cells}, N_modes/cell = {N_MODES}, N_slots = {n_slots}")
    print("=" * 72)

    t0 = time.time()

    # Diagonalize all N-sectors needed
    fock_data = {}
    gs_energies = {}
    gs_vectors = {}
    dimensions = {}

    for N in range(max_N_here + 1):
        if N > n_slots:
            break
        H, pair_states, state_index, dim = build_hamiltonian(
            N, n_cells, eps_2mode, V_2mode, E_J_fold, N_MODES
        )
        fock_data[N] = (pair_states, state_index, dim)
        dimensions[N] = dim

        if dim == 0:
            print(f"  N_pair={N}: empty sector")
            continue
        elif dim == 1:
            gs_energies[N] = H[0, 0]
            gs_vectors[N] = np.array([1.0])
            print(f"  N_pair={N}: dim={dim}, E_GS={H[0,0]:.6f} M_KK")
        else:
            n_eig = min(10, dim)
            evals, evecs = eigh(H, subset_by_index=[0, n_eig - 1])
            gs_energies[N] = evals[0]
            gs_vectors[N] = evecs[:, 0]
            gap = evals[1] - evals[0] if n_eig > 1 else float('inf')
            print(f"  N_pair={N}: dim={dim}, E_GS={evals[0]:.6f}, gap={gap:.6f} M_KK")

            # Hermiticity check
            herm_err = np.max(np.abs(H - H.T))
            if herm_err > 1e-12:
                print(f"    WARNING: Hermiticity error {herm_err:.2e}")

    # Compute S_+(N) for accessible N
    print(f"\n  --- Pair-Addition S_+(N) ---")
    S_plus_vals = {}
    S_per_cell_vals = {}
    S_per_mode_vals = {}
    P_kc_vals = {}

    for N in range(min(max_N_pair, n_slots)):
        if N not in gs_vectors or (N + 1) not in gs_vectors:
            continue

        P_kc, S_plus, S_per_cell, S_per_mode = compute_pair_addition_all_cells(
            N, n_cells, fock_data, gs_vectors, N_MODES
        )
        S_plus_vals[N] = S_plus
        S_per_cell_vals[N] = S_per_cell
        S_per_mode_vals[N] = S_per_mode
        P_kc_vals[N] = P_kc

        # Bosonic prediction
        S_bos = (N + 1) * (1.0 - N / (2.0 * n_slots)) / 2.0
        dev = abs(S_plus - S_bos) / S_bos * 100 if S_bos > 0 else 0

        # Nuclear formula: sqrt((N+1)*(Omega - N)) where Omega = n_slots
        S_nuc = np.sqrt((N + 1) * (n_slots - N))

        # Cell uniformity
        if n_cells > 1:
            cell_max = np.max(S_per_cell)
            cell_min = np.min(S_per_cell)
            uniformity = cell_max / cell_min if cell_min > 1e-15 else float('inf')
        else:
            uniformity = 1.0

        print(f"\n    N={N} -> N+1={N+1}:")
        print(f"      S_+(N={N}) = {S_plus:.6f}")
        print(f"      Bosonic pred = {S_bos:.6f}, deviation = {dev:.2f}%")
        print(f"      Nuclear sqrt  = {S_nuc:.6f}")
        print(f"      (N+1)/2 floor = {(N+1)/2:.6f}")
        if n_cells > 1:
            print(f"      Cell uniformity (max/min) = {uniformity:.4f}")
            print(f"      S per cell = {S_per_cell}")
        print(f"      S per mode = {S_per_mode}")

    elapsed = time.time() - t0
    print(f"\n  Elapsed: {elapsed:.2f} s")

    # Store results
    results[n_cells] = {
        'gs_energies': gs_energies,
        'dimensions': dimensions,
        'S_plus': S_plus_vals,
        'S_per_cell': S_per_cell_vals,
        'S_per_mode': S_per_mode_vals,
        'P_kc': P_kc_vals,
        'elapsed': elapsed,
    }


# =====================================================================
#  4. SCALING ANALYSIS
# =====================================================================

print("\n" + "=" * 72)
print("  SCALING ANALYSIS: S_+(N) vs BOSONIC PREDICTION")
print("=" * 72)

# Bosonic formula: S_+(N) = (N+1)(1 - N/(2*N_slots))/2
print(f"\n{'N_cells':>7} {'N_slots':>7} {'N_pair':>6} {'S_+(N)':>10} {'S_bos':>10} {'dev%':>8} {'(N+1)/2':>8} {'ratio':>8}")
print("-" * 72)

deviations_8cell = []  # for gate

for n_cells in cell_configs:
    n_slots = N_MODES * n_cells
    S_data = results[n_cells]['S_plus']
    for N in sorted(S_data.keys()):
        S_val = S_data[N]
        S_bos = (N + 1) * (1.0 - N / (2.0 * n_slots)) / 2.0
        dev = (S_val - S_bos) / S_bos * 100 if S_bos > 0 else 0
        floor = (N + 1) / 2.0
        ratio = S_val / floor if floor > 0 else float('inf')
        print(f"{n_cells:>7} {n_slots:>7} {N:>6} {S_val:>10.6f} {S_bos:>10.6f} {dev:>7.2f}% {floor:>8.4f} {ratio:>8.4f}")
        if n_cells == 8:
            deviations_8cell.append(abs(dev))


# =====================================================================
#  5. CELL UNIFORMITY ANALYSIS
# =====================================================================

print("\n" + "=" * 72)
print("  CELL UNIFORMITY: pair spread across fabric")
print("=" * 72)

for n_cells in cell_configs:
    if n_cells == 1:
        continue
    S_cell_data = results[n_cells]['S_per_cell']
    print(f"\n  N_cells = {n_cells}:")
    for N in sorted(S_cell_data.keys()):
        S_per_cell = S_cell_data[N]
        uniformity = np.max(S_per_cell) / np.min(S_per_cell) if np.min(S_per_cell) > 1e-15 else float('inf')
        # Entropy of distribution
        p = S_per_cell / np.sum(S_per_cell)
        entropy = -np.sum(p * np.log(p + 1e-30)) / np.log(n_cells)  # normalized to [0,1]
        print(f"    N={N}: max/min={uniformity:.4f}, entropy={entropy:.4f}, S_per_cell={S_per_cell}")


# =====================================================================
#  6. NUCLEAR COMPARISON: seniority model
# =====================================================================

print("\n" + "=" * 72)
print("  NUCLEAR COMPARISON: Seniority Model")
print("=" * 72)
print("  In the nuclear seniority model (Paper 18, pair transfer spectroscopy):")
print("  S_+(N) = sqrt((N+1)(Omega - N)) where Omega = total pair degeneracy")
print("  For large Omega, this approaches (N+1)/2 (bosonic limit)")
print()

for n_cells in cell_configs:
    n_slots = N_MODES * n_cells
    Omega = n_slots
    S_data = results[n_cells]['S_plus']
    print(f"  N_cells={n_cells}, Omega={Omega}:")
    for N in sorted(S_data.keys()):
        S_val = S_data[N]
        S_sen = np.sqrt((N + 1) * (Omega - N))
        dev_sen = (S_val - S_sen) / S_sen * 100 if S_sen > 0 else 0
        print(f"    N={N}: S_+(ED)={S_val:.6f}, S_+(seniority)={S_sen:.6f}, dev={dev_sen:.2f}%")


# =====================================================================
#  7. CONVERGENCE WITH N_CELLS: approach to thermodynamic limit
# =====================================================================

print("\n" + "=" * 72)
print("  CONVERGENCE: S_+(1) vs N_cells")
print("=" * 72)

S_plus_1_vs_Nc = []
for n_cells in cell_configs:
    S_data = results[n_cells]['S_plus']
    if 1 in S_data:
        S_val = S_data[1]
        n_slots = N_MODES * n_cells
        S_bos = 2 * (1 - 1 / (2 * n_slots)) / 2.0  # = 1 - 1/(2*n_slots)
        S_plus_1_vs_Nc.append((n_cells, S_val, S_bos))
        print(f"  N_cells={n_cells}: S_+(1)={S_val:.6f}, bosonic={S_bos:.6f}")

# S60 reference (8-mode 2-cell): S_+(1) = 0.9356
print(f"\n  S60 reference (8-mode, 2-cell): S_+(1) = 0.935600")
print(f"  S60 workshop (8-mode, 1-cell): S_+(1) = 1.013")


# =====================================================================
#  8. GATE VERDICT
# =====================================================================

print("\n" + "=" * 72)
print("  GATE VERDICT: PAIR-FABRIC-61")
print("=" * 72)

max_dev_8cell = max(deviations_8cell) if deviations_8cell else float('inf')
mean_dev_8cell = np.mean(deviations_8cell) if deviations_8cell else float('inf')

# Check the (N+1)/2 floor condition
S_data_8 = results[8]['S_plus']
below_floor = False
for N in sorted(S_data_8.keys()):
    floor = (N + 1) / 2.0
    if S_data_8[N] < floor:
        below_floor = True
        print(f"  S_+(N={N}) = {S_data_8[N]:.6f} < (N+1)/2 = {floor:.4f} -- BELOW FLOOR")

if below_floor:
    verdict = "FAIL"
    detail = f"S_+(N) falls below (N+1)/2 at 8 cells"
elif max_dev_8cell < 10.0:
    verdict = "PASS"
    detail = f"Bosonic scaling holds at 8 cells: max deviation {max_dev_8cell:.2f}% < 10%"
else:
    verdict = "INFO"
    detail = f"Intermediate: above (N+1)/2 floor but max deviation {max_dev_8cell:.2f}% > 10%"

print(f"\n  Max deviation at 8-cell: {max_dev_8cell:.2f}%")
print(f"  Mean deviation at 8-cell: {mean_dev_8cell:.2f}%")
print(f"  Gate: PAIR-FABRIC-61 = {verdict}")
print(f"  Detail: {detail}")


# =====================================================================
#  9. SAVE DATA
# =====================================================================

save_dict = {
    'N_modes_per_cell': N_MODES,
    'cell_configs': np.array(cell_configs),
    'max_N_pair': max_N_pair,
    'eps_2mode': eps_2mode,
    'V_2mode': V_2mode,
    'E_J_fold': E_J_fold,
    'tau_fold': tau_fold,
}

# Store per-config results
for n_cells in cell_configs:
    res = results[n_cells]
    prefix = f'Nc{n_cells}'
    for N, val in res['S_plus'].items():
        save_dict[f'{prefix}_S_plus_N{N}'] = val
    for N, val in res['S_per_cell'].items():
        save_dict[f'{prefix}_S_per_cell_N{N}'] = val
    for N, val in res['S_per_mode'].items():
        save_dict[f'{prefix}_S_per_mode_N{N}'] = val
    for N, val in res['gs_energies'].items():
        save_dict[f'{prefix}_E_GS_N{N}'] = val
    save_dict[f'{prefix}_elapsed'] = res['elapsed']

# Gate
save_dict['gate_name'] = np.array(['PAIR-FABRIC-61'])
save_dict['gate_verdict'] = np.array([verdict])
save_dict['gate_detail'] = np.array([detail])
save_dict['max_dev_8cell'] = max_dev_8cell
save_dict['mean_dev_8cell'] = mean_dev_8cell

out_path = os.path.join(data_dir, 's61_pair_transfer_fabric.npz')
np.savez(out_path, **save_dict)
print(f"\n  Data saved: {out_path}")


# =====================================================================
#  10. PLOT
# =====================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('PAIR-FABRIC-61: Pair-Transfer Scaling on Multi-Cell Fabrics',
             fontsize=13, fontweight='bold')

# Panel (a): S_+(N) vs N for each N_cells
ax = axes[0, 0]
colors = {1: 'C0', 2: 'C1', 4: 'C2', 8: 'C3'}
for n_cells in cell_configs:
    S_data = results[n_cells]['S_plus']
    Ns = sorted(S_data.keys())
    Svals = [S_data[N] for N in Ns]
    ax.plot(Ns, Svals, 'o-', color=colors[n_cells], label=f'{n_cells}-cell ED', markersize=7)

    # Bosonic prediction
    n_slots = N_MODES * n_cells
    N_arr = np.array(Ns)
    S_bos = (N_arr + 1) * (1 - N_arr / (2 * n_slots)) / 2.0
    ax.plot(Ns, S_bos, '--', color=colors[n_cells], alpha=0.5, linewidth=1)

# (N+1)/2 floor
N_plot = np.arange(0, max_N_pair + 0.1, 0.1)
ax.plot(N_plot, (N_plot + 1) / 2, 'k:', alpha=0.4, label='$(N+1)/2$ floor')
ax.set_xlabel('$N_{\\rm pair}$')
ax.set_ylabel('$S_+(N)$')
ax.set_title('(a) Pair-transfer strength vs $N_{\\rm pair}$')
ax.legend(fontsize=8, ncol=2)
ax.grid(True, alpha=0.3)

# Panel (b): deviation from bosonic scaling
ax = axes[0, 1]
for n_cells in cell_configs:
    S_data = results[n_cells]['S_plus']
    n_slots = N_MODES * n_cells
    Ns = sorted(S_data.keys())
    devs = []
    for N in Ns:
        S_bos = (N + 1) * (1 - N / (2 * n_slots)) / 2.0
        dev = (S_data[N] - S_bos) / S_bos * 100
        devs.append(dev)
    ax.plot(Ns, devs, 'o-', color=colors[n_cells], label=f'{n_cells}-cell', markersize=7)

ax.axhline(0, color='k', linewidth=0.5)
ax.axhspan(-10, 10, alpha=0.1, color='green', label='PASS band (<10%)')
ax.set_xlabel('$N_{\\rm pair}$')
ax.set_ylabel('Deviation from bosonic (%)')
ax.set_title('(b) Bosonic scaling deviation')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel (c): S_+(1) convergence with N_cells
ax = axes[1, 0]
Nc_arr = np.array([r[0] for r in S_plus_1_vs_Nc])
S1_arr = np.array([r[1] for r in S_plus_1_vs_Nc])
S1_bos = np.array([r[2] for r in S_plus_1_vs_Nc])
ax.plot(Nc_arr, S1_arr, 'ko-', markersize=8, label='$S_+(1)$ ED')
ax.plot(Nc_arr, S1_bos, 'r--', label='Bosonic prediction')
ax.axhline(1.0, color='gray', linestyle=':', alpha=0.5, label='$N \\to \\infty$ limit')
ax.set_xlabel('$N_{\\rm cells}$')
ax.set_ylabel('$S_+(1)$')
ax.set_title('(c) $S_+(1)$ convergence with fabric size')
ax.set_xscale('log', base=2)
ax.set_xticks(Nc_arr)
ax.set_xticklabels([str(int(n)) for n in Nc_arr])
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel (d): Cell uniformity for 8-cell
ax = axes[1, 1]
S_cell_data_8 = results[8]['S_per_cell']
Ns_8 = sorted(S_cell_data_8.keys())
cell_indices = np.arange(8)
for N in Ns_8:
    S_per_cell = S_cell_data_8[N]
    ax.plot(cell_indices, S_per_cell, 'o-', label=f'$N_{{\\rm pair}}={N}$', markersize=5)
ax.set_xlabel('Cell index')
ax.set_ylabel('$S_+$ per cell')
ax.set_title('(d) Cell-resolved pair transfer (8-cell chain)')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plot_path = os.path.join(data_dir, 's61_pair_transfer_fabric.png')
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"  Plot saved: {plot_path}")

print("\n" + "=" * 72)
print("  COMPUTATION COMPLETE")
print("=" * 72)
