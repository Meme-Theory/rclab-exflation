#!/usr/bin/env python3
"""
N11-DC-PERMANENCE-74: 20% DC Component on Larger Multi-Cell Systems
====================================================================

Gate: N11-DC-PERMANENCE-74
  PASS: DC fraction at 12-cell in [0.15, 0.25].
  INFO: DC fraction at 12-cell in [0.10, 0.30] (but outside PASS window).
  FAIL: DC fraction at 12-cell outside [0.10, 0.30].

Physics (substrate framing):
  The 4-cell computation (S73B VIRTUAL-PARTICLE W4-A) found that ~20% of a
  localized perturbation survives as a long-time DC component --- a
  non-propagating, permanent offset of the pair occupation at the perturbed
  cell/mode away from the GGE equilibrium value. This is the non-propagating
  part of the substrate's response: the fraction of the "virtual particle"
  amplitude that lives on conserved charges of the Josephson network and
  therefore cannot dephase away.

  The question is whether the ~20% value is a feature of the substrate's
  integrability structure (in which case it should be roughly size-independent
  --- a structural constant of the network topology) or a small-cluster
  artifact (in which case it should decay as N_cells increases).

  Method (identical to S73B W4-A, only the ring size changes):
    1. Find an induced cycle C_L of length L in CG(24) for L = 8, 12.
       CG(24) is 6-regular, bipartite, girth 4. Induced C_8 and C_12
       subgraphs exist by explicit DFS search.
    2. Build the BCS + Josephson Hamiltonian on the L-cell ring:
          H = sum_c [sum_k 2 eps_k n_{c,k} + sum_{k,l} V_{kl} b^dag_{c,k} b_{c,l}]
            + E_J sum_{<c,c'>} sum_k [b^dag_{c,k} b_{c',k} + h.c.]
       with eps_fold, V_fold, E_J_fold loaded from the same S56/S73B source.
    3. Fix N_pair = 2 (same as S73B, keeps dims tractable at 12-cell).
       Dim(Fock) = C(8*L, 2) ==>  4: 496, 8: 2016, 12: 4560.
    4. Prepare |psi_0> by pinning one pair on cell 1, mode B1 starting from
       the BCS ground state and re-normalizing (same protocol as S73B).
    5. Evolve under full H and compute <n_{cell=1, B1}(t)> - <n_{cell=1, B1}>_GGE.
    6. DC fraction = |<delta_n(t)>|_{t > t_max/2} / |delta_n(0)|  (identical
       definition to S73B).
    7. Gate check at L = 12.

  The 4-cell DC fraction from S73B (dc_fraction = 0.2037) is loaded directly
  --- not recomputed --- to ensure the cross-size comparison is apples to
  apples. Only the 8- and 12-cell values are computed here.

Input files:
  computations/_shared/canonical_constants.py
  computations/session-73/s73b_virtual_particle.npz  (S73B 4-cell DC fraction)
  computations/session-64/s64_local_entangle.npz     (CG(24) adjacency)
  computations/session-56/s56_gge_fabric.npz         (eps_fold, V_fold, E_J_fold)

Output files:
  computations/session-74/s74_dc_permanence.npz
  computations/session-74/s74_dc_permanence.png

Session: S74 W4-B
Agent: kitaev-quantum-chaos-theorist
"""

import os
import sys
import time
import numpy as np
from itertools import combinations
from math import comb as mcomb
from scipy.linalg import eigh
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# === Canonical constants ===
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    tau_fold, E_cond, N_dof_BCS, M_KK,
    Delta_BCS, Delta_0_OES,
    E_B1, E_B2_mean, E_B3_mean,
    J_C2, J_su2, J_u1, T_acoustic,
    c_fabric, c_Gold, omega_att, omega_L1,
    l_Planck, hbar_GeV_s,
)

data_dir = os.path.dirname(os.path.abspath(__file__))
t_start = time.time()

print("=" * 72)
print("N11-DC-PERMANENCE-74")
print("20% DC Component on Larger Multi-Cell Systems (C_L rings in CG(24))")
print("=" * 72)
print(f"Delta_BCS   = {Delta_BCS:.6f} M_KK")
print(f"J_C2        = {J_C2:.6f} M_KK  (Josephson coupling, dominant)")
print(f"T_acoustic  = {T_acoustic} M_KK")
print(f"M_KK        = {M_KK:.4e} GeV")
print()

# ============================================================
#  1. LOAD INPUT DATA
# ============================================================

# CG(24) adjacency
d64 = np.load(os.path.join(data_dir, 's64_local_entangle.npz'),
              allow_pickle=True)
adj_cg24 = d64['adj_cg24'].astype(float)
N_vertices_cg24 = int(d64['N_vert'])
assert adj_cg24.shape == (24, 24)
assert N_vertices_cg24 == 24
print(f"CG(24) loaded: {N_vertices_cg24} vertices, "
      f"{int(adj_cg24.sum())//2} edges, "
      f"6-regular, bipartite")

# BCS mode structure at the fold (same source as S73B)
d56 = np.load(os.path.join(data_dir, 's56_gge_fabric.npz'),
              allow_pickle=True)
eps_fold = np.asarray(d56['eps_fold'], dtype=float)
V_fold = np.asarray(d56['V_fold'], dtype=float)
E_J_fold = float(d56['E_J_fold'])
N_modes = len(eps_fold)  # (local) = 8 (B1, B2[3], B3[2], ...)
print(f"N_modes per cell = {N_modes}")
print(f"eps_fold = {np.round(eps_fold, 6)}")
print(f"E_J_fold = {E_J_fold:.6f} M_KK")

# S73B 4-cell reference
d73b = np.load(os.path.join(data_dir, 's73b_virtual_particle.npz'),
               allow_pickle=True)
dc_fraction_4cell = float(d73b['dc_fraction'])
dc_signal_4cell = float(d73b['dc_signal'])
initial_excess_4cell = float(d73b['initial_excess'])
c4_vertices_ref = d73b['c4_vertices']
dim_4cell_ref = int(d73b['dim'])
N_pair_ref = int(d73b['N_pair'])
print()
print(f"S73B 4-cell reference (loaded):")
print(f"  C_4 vertices   = {c4_vertices_ref}")
print(f"  dim            = {dim_4cell_ref}")
print(f"  N_pair         = {N_pair_ref}")
print(f"  dc_signal      = {dc_signal_4cell:.6f}")
print(f"  initial_excess = {initial_excess_4cell:.6f}")
print(f"  dc_fraction    = {dc_fraction_4cell:.6f}")
assert N_pair_ref == 2, "S73B used N_pair=2; must match"
print()


# ============================================================
#  2. INDUCED CYCLE FINDER
# ============================================================

def find_induced_cycle(adj, N, L, start=0):
    """
    Depth-first search for an induced cycle of length L in graph adj.
    Returns a list of L vertex indices forming a cordless cycle, or None.

    An induced cycle C_L has exactly L edges (the cycle edges) and no
    chords: adj[path[i], path[j]] = 0 for all (i,j) with |i-j| != 1
    modulo L.
    """
    best = [None]  # (local)

    def dfs(path):
        if best[0] is not None:
            return
        depth = len(path)
        if depth == L:
            if adj[path[-1], path[0]] > 0.5:
                best[0] = list(path)
            return
        last = path[-1]
        for w in range(N):
            if adj[last, w] < 0.5:
                continue
            if w in path:
                continue
            if w < start:
                continue  # break symmetry
            # Chord check: w must not be adjacent to any earlier path vertex
            # except 'last'. Allowed closure (adj to path[0]) only when depth+1==L.
            chord = False  # (local)
            for idx_u, u in enumerate(path[:-1]):
                if adj[u, w] > 0.5:
                    # Allow connection to start only on the final step
                    if idx_u == 0 and depth + 1 == L:
                        continue
                    chord = True
                    break
            if chord:
                continue
            path.append(w)
            dfs(path)
            if best[0] is not None:
                return
            path.pop()

    dfs([start])
    return best[0]


def verify_induced_cycle(adj, cycle):
    """Assert that `cycle` is an induced (chord-free) cycle in adj."""
    L = len(cycle)
    for i in range(L):
        a, b = cycle[i], cycle[(i + 1) % L]
        assert adj[a, b] > 0.5, f"Missing edge {a}-{b}"
    # Chord check
    for i in range(L):
        for j in range(L):
            if i == j:
                continue
            # Skip cycle edges
            if (j == (i + 1) % L) or (i == (j + 1) % L):
                continue
            assert adj[cycle[i], cycle[j]] < 0.5, (
                f"Chord {cycle[i]}-{cycle[j]} at cycle positions {i}, {j}"
            )
    return True


# Find C_8 and C_12 induced cycles
c8_verts = find_induced_cycle(adj_cg24, N_vertices_cg24, 8, start=0)
assert c8_verts is not None, "No induced C_8 found in CG(24)"
verify_induced_cycle(adj_cg24, c8_verts)
print(f"C_8 induced cycle in CG(24):  {c8_verts}")

c12_verts = find_induced_cycle(adj_cg24, N_vertices_cg24, 12, start=0)
assert c12_verts is not None, "No induced C_12 found in CG(24)"
verify_induced_cycle(adj_cg24, c12_verts)
print(f"C_12 induced cycle in CG(24): {c12_verts}")
print()


# ============================================================
#  3. CORE ROUTINE: DC FRACTION FOR A GIVEN CELL COUNT
# ============================================================

def ring_adjacency(N_cells):
    """N_cells x N_cells adjacency for a C_{N_cells} ring (0-1-2-...-N_cells-1-0)."""
    A = np.zeros((N_cells, N_cells), dtype=float)
    for i in range(N_cells):
        j = (i + 1) % N_cells
        A[i, j] = 1.0
        A[j, i] = 1.0
    return A


def compute_dc_fraction(N_cells, N_pair, eps_fold, V_fold, E_J_fold,
                        T_acoustic, J_C2, verbose=True):
    """
    Build the BCS + Josephson Hamiltonian on a C_{N_cells} ring, prepare a
    localized perturbation at (cell=1, B1), time-evolve, and return the DC
    fraction using the exact definition of S73B W4-A:

        dc_fraction = |<delta_n_{cell=1, B1}(t)>_{t > t_max/2}| / |delta_n(0)|

    Parameters
    ----------
    N_cells : int
        Number of cells in the ring (cycle length).
    N_pair : int
        Total number of BCS pairs in the Fock space (fixed sector).
    eps_fold, V_fold : array
        Intra-cell BCS kinetic and pairing matrices at the fold.
    E_J_fold : float
        Josephson coupling.
    T_acoustic : float
        Temperature of the reference GGE (M_KK).
    J_C2 : float
        Josephson scale (M_KK) used for the time grid.
    """
    N_modes = len(eps_fold)
    N_slots = N_modes * N_cells
    dim = mcomb(N_slots, N_pair)

    if verbose:
        print(f"  N_cells={N_cells}, N_modes={N_modes}, N_slots={N_slots}, "
              f"dim=C({N_slots},{N_pair})={dim}")

    # --- Basis ---
    basis = list(combinations(range(N_slots), N_pair))
    basis_dict = {s: i for i, s in enumerate(basis)}

    def slot_to_cell_mode(slot):
        return slot // N_modes, slot % N_modes

    def cell_mode_to_slot(c, m):
        return c * N_modes + m

    # --- Ring adjacency ---
    adj_ring = ring_adjacency(N_cells)  # (local)

    # --- Hamiltonian ---
    t_h = time.time()
    H = np.zeros((dim, dim), dtype=float)
    V_sym = (V_fold + V_fold.T) / 2.0  # (local) enforce symmetry

    for i, state_i in enumerate(basis):
        # Diagonal kinetic
        E_kin = 0.0  # (local)
        for slot in state_i:
            c, m = slot_to_cell_mode(slot)
            E_kin += 2.0 * eps_fold[m]
        H[i, i] += E_kin

        # Intra-cell pairing V_{kl} (pair hop within the same cell)
        for slot_k in state_i:
            c_k, k = slot_to_cell_mode(slot_k)
            for l in range(N_modes):
                if l == k:
                    continue
                slot_l = cell_mode_to_slot(c_k, l)
                if slot_l in state_i:
                    continue
                new_state = tuple(sorted(
                    [s for s in state_i if s != slot_k] + [slot_l]
                ))
                j = basis_dict.get(new_state)
                if j is not None:
                    H[i, j] += V_sym[k, l]

        # Inter-cell Josephson hopping (same mode k, neighboring cells)
        for slot_from in state_i:
            c_from, k = slot_to_cell_mode(slot_from)
            for c_to in range(N_cells):
                if c_to == c_from:
                    continue
                if adj_ring[c_from, c_to] < 0.5:
                    continue
                slot_to = cell_mode_to_slot(c_to, k)
                if slot_to in state_i:
                    continue
                new_state = tuple(sorted(
                    [s for s in state_i if s != slot_from] + [slot_to]
                ))
                j = basis_dict.get(new_state)
                if j is not None:
                    H[i, j] += E_J_fold

    H = 0.5 * (H + H.T)
    herm_err = np.max(np.abs(H - H.T))  # (local)
    if verbose:
        print(f"  H build: {time.time()-t_h:.2f} s, "
              f"Hermiticity err = {herm_err:.2e}")

    # --- Diagonalize ---
    t_d = time.time()
    evals, evecs = eigh(H)
    if verbose:
        print(f"  Diagonalize: {time.time()-t_d:.2f} s, "
              f"E_min={evals[0]:.4f}, spread={evals[-1]-evals[0]:.4f}")

    # --- GGE reference state (thermal at T_acoustic) ---
    beta_loc = 1.0 / T_acoustic  # (local) inverse temperature
    w_unnorm = np.exp(-beta_loc * (evals - evals[0]))  # (local)
    Z_loc = np.sum(w_unnorm)  # (local)
    w_therm = w_unnorm / Z_loc  # (local)

    # <n_slot>_GGE
    n_gge = np.zeros(N_slots)  # (local)
    for alpha in range(dim):
        if w_therm[alpha] < 1e-15:
            continue
        psi_alpha = evecs[:, alpha]
        p_i = np.abs(psi_alpha) ** 2  # (local) weight on each basis state
        # Vectorize the slot loop by pre-indexing basis membership
        for i, state_i in enumerate(basis):
            if p_i[i] < 1e-20:
                continue
            for slot in state_i:
                n_gge[slot] += w_therm[alpha] * p_i[i]

    assert abs(np.sum(n_gge) - N_pair) < 1e-8, (
        f"GGE sum={np.sum(n_gge)} != N_pair={N_pair}"
    )

    # --- Perturbation: pin pair on (cell=1, B1) ---
    PERT_CELL = 1  # (local)
    PERT_MODE = 0  # (local) B1 (eps_fold[0] = 0)
    PERT_SLOT = cell_mode_to_slot(PERT_CELL, PERT_MODE)

    psi_gs = evecs[:, 0]  # (local) BCS ground state
    psi_pert_raw = np.zeros(dim)  # (local)
    for i, state_i in enumerate(basis):
        if PERT_SLOT in state_i:
            psi_pert_raw[i] = psi_gs[i]

    norm_raw = np.linalg.norm(psi_pert_raw)  # (local)
    assert norm_raw > 1e-8, "GS has zero weight on perturbed slot"
    psi_0 = psi_pert_raw / norm_raw  # (local)

    # Verify pinning
    n_slot_psi0 = 0.0  # (local)
    for i, state_i in enumerate(basis):
        if PERT_SLOT in state_i:
            n_slot_psi0 += np.abs(psi_0[i]) ** 2
    assert abs(n_slot_psi0 - 1.0) < 1e-10, (
        f"Pinning check: <n>={n_slot_psi0}"
    )

    # --- Spectral decomposition ---
    c_alpha = evecs.T @ psi_0  # (local)
    assert abs(np.sum(c_alpha ** 2) - 1.0) < 1e-10

    # --- Time grid (match S73B) ---
    tau_J_local = 1.0 / (2 * np.pi * J_C2)  # (local) single Josephson hop
    t_max = 40.0 * tau_J_local  # (local)
    n_t = 2000  # (local)
    t_grid = np.linspace(0.0, t_max, n_t)  # (local)

    # --- <n_{PERT_SLOT}(t)> via spectral sum ---
    diag_n = np.zeros(dim)  # (local)
    for i, state_i in enumerate(basis):
        if PERT_SLOT in state_i:
            diag_n[i] = 1.0

    M_eig = (evecs.T * diag_n) @ evecs  # (local) rotation of n_slot to eigenbasis

    # n(t) = sum_a c_a^2 M_aa + 2 sum_{a<b} c_a c_b M_ab cos((E_a-E_b) t)
    stat_part = float(np.sum(c_alpha ** 2 * np.diag(M_eig)))  # (local)
    c_outer = np.outer(c_alpha, c_alpha)  # (local)
    AMP = c_outer * M_eig  # (local)

    iu = np.triu_indices(dim, k=1)  # (local)
    w_ab = 2.0 * AMP[iu]  # (local)
    dE_ab = evals[iu[0]] - evals[iu[1]]  # (local)
    mask = np.abs(w_ab) > 1e-14  # (local)
    w_ab_k = w_ab[mask]  # (local)
    dE_ab_k = dE_ab[mask]  # (local)

    # Evaluate in reasonable-size batches to avoid blowing RAM for dim~4560
    n_traces = np.full(n_t, stat_part, dtype=float)  # (local)
    batch = 200_000  # (local) rows per chunk
    n_pairs_kept = len(w_ab_k)  # (local)
    t_ev = time.time()
    for b0 in range(0, n_pairs_kept, batch):
        b1 = min(b0 + batch, n_pairs_kept)
        phase = np.outer(dE_ab_k[b0:b1], t_grid)  # (local)
        n_traces += w_ab_k[b0:b1] @ np.cos(phase)
    if verbose:
        print(f"  Time evolution ({n_pairs_kept} spectral pairs): "
              f"{time.time()-t_ev:.2f} s")

    delta_n = n_traces - n_gge[PERT_SLOT]  # (local)

    # --- DC fraction (S73B definition, identical protocol) ---
    half = n_t // 2  # (local)
    dc_signal = float(np.mean(delta_n[half:]))  # (local)
    initial_excess = float(abs(delta_n[0]))  # (local)
    dc_frac = abs(dc_signal) / initial_excess if initial_excess > 0 else 0.0  # (local)

    if verbose:
        print(f"  delta_n(0) = {delta_n[0]:.6f}")
        print(f"  <delta_n(t)>_{{t>t_max/2}} = {dc_signal:.6f}")
        print(f"  DC fraction = {dc_frac:.6f}")

    return {
        'N_cells': N_cells,
        'N_slots': N_slots,
        'dim': dim,
        'dc_signal': dc_signal,
        'initial_excess': initial_excess,
        'dc_fraction': dc_frac,
        'n_gge_slot': float(n_gge[PERT_SLOT]),
        'delta_n_trace': delta_n,
        't_grid': t_grid,
        'herm_err': float(herm_err),
        'E_min': float(evals[0]),
        'E_max': float(evals[-1]),
    }


# ============================================================
#  4. 4-CELL (reference, loaded from S73B --- NOT recomputed)
# ============================================================

print("=" * 72)
print("4-CELL RING  (reference, loaded from S73B W4-A)")
print("=" * 72)
print(f"  dim         = {dim_4cell_ref}")
print(f"  DC fraction = {dc_fraction_4cell:.6f}")
res_4 = {
    'N_cells': 4,
    'N_slots': 32,
    'dim': dim_4cell_ref,
    'dc_signal': dc_signal_4cell,
    'initial_excess': initial_excess_4cell,
    'dc_fraction': dc_fraction_4cell,
    'source': 'S73B_W4A',
}
print()

# ============================================================
#  5. 8-CELL RING
# ============================================================

print("=" * 72)
print(f"8-CELL RING  (induced C_8 from CG(24): {c8_verts})")
print("=" * 72)
t8 = time.time()
res_8 = compute_dc_fraction(
    N_cells=8,
    N_pair=2,  # (local)
    eps_fold=eps_fold,
    V_fold=V_fold,
    E_J_fold=E_J_fold,
    T_acoustic=T_acoustic,
    J_C2=J_C2,
    verbose=True,
)
res_8['c_verts'] = np.asarray(c8_verts, dtype=int)
print(f"  [8-cell elapsed: {time.time()-t8:.2f} s]")
print()

# ============================================================
#  6. 12-CELL RING
# ============================================================

print("=" * 72)
print(f"12-CELL RING  (induced C_12 from CG(24): {c12_verts})")
print("=" * 72)
t12 = time.time()
res_12 = compute_dc_fraction(
    N_cells=12,
    N_pair=2,  # (local)
    eps_fold=eps_fold,
    V_fold=V_fold,
    E_J_fold=E_J_fold,
    T_acoustic=T_acoustic,
    J_C2=J_C2,
    verbose=True,
)
res_12['c_verts'] = np.asarray(c12_verts, dtype=int)
print(f"  [12-cell elapsed: {time.time()-t12:.2f} s]")
print()

# ============================================================
#  7. GATE CHECK
# ============================================================

print("=" * 72)
print("N11-DC-PERMANENCE-74 GATE")
print("=" * 72)
N_cell_array = np.array([4, 8, 12])  # (local)
dc_array = np.array([
    res_4['dc_fraction'],
    res_8['dc_fraction'],
    res_12['dc_fraction'],
])  # (local)
dim_array = np.array([res_4['dim'], res_8['dim'], res_12['dim']])  # (local)

print("\n DC fraction vs cell count:")
print(" N_cells   dim     DC fraction")
for Nc, di, dcf in zip(N_cell_array, dim_array, dc_array):
    print(f"  {Nc:5d}  {di:5d}    {dcf:.6f}")

# Relative change
dc_rel_8 = (res_8['dc_fraction'] - res_4['dc_fraction']) / res_4['dc_fraction']  # (local)
dc_rel_12 = (res_12['dc_fraction'] - res_4['dc_fraction']) / res_4['dc_fraction']  # (local)
print(f"\n Relative change from 4-cell:")
print(f"  8-cell:  {dc_rel_8:+.2%}")
print(f"  12-cell: {dc_rel_12:+.2%}")

dc_12 = float(res_12['dc_fraction'])  # (local) gate value
PASS_LO, PASS_HI = 0.15, 0.25  # (local)
INFO_LO, INFO_HI = 0.10, 0.30  # (local)

print(f"\n Gate thresholds:")
print(f"  PASS: [{PASS_LO}, {PASS_HI}]")
print(f"  INFO: [{INFO_LO}, {INFO_HI}]")
print(f"\n 12-cell DC fraction = {dc_12:.6f}")

if PASS_LO <= dc_12 <= PASS_HI:
    gate_verdict = 'PASS'
    gate_reason = (
        f"dc_fraction(12-cell) = {dc_12:.4f} in PASS window [{PASS_LO}, {PASS_HI}]"
    )
elif INFO_LO <= dc_12 <= INFO_HI:
    gate_verdict = 'INFO'
    gate_reason = (
        f"dc_fraction(12-cell) = {dc_12:.4f} in INFO window [{INFO_LO}, {INFO_HI}] "
        f"but outside PASS [{PASS_LO}, {PASS_HI}]"
    )
else:
    gate_verdict = 'FAIL'
    gate_reason = (
        f"dc_fraction(12-cell) = {dc_12:.4f} outside INFO window [{INFO_LO}, {INFO_HI}]"
    )

print(f"\n GATE VERDICT: {gate_verdict}")
print(f"  Reason: {gate_reason}")

# ============================================================
#  8. SAVE DATA
# ============================================================

out_npz = os.path.join(data_dir, 's74_dc_permanence.npz')
np.savez(
    out_npz,
    gate_name='N11-DC-PERMANENCE-74',
    gate_verdict=gate_verdict,
    gate_reason=gate_reason,
    pass_lo=PASS_LO, pass_hi=PASS_HI,
    info_lo=INFO_LO, info_hi=INFO_HI,
    N_cell_array=N_cell_array,
    dim_array=dim_array,
    dc_array=dc_array,
    dc_rel_8=dc_rel_8,
    dc_rel_12=dc_rel_12,
    # 4-cell (S73B loaded)
    dc_fraction_4=res_4['dc_fraction'],
    dc_signal_4=res_4['dc_signal'],
    initial_excess_4=res_4['initial_excess'],
    dim_4=res_4['dim'],
    # 8-cell
    c8_verts=np.asarray(c8_verts, dtype=int),
    dc_fraction_8=res_8['dc_fraction'],
    dc_signal_8=res_8['dc_signal'],
    initial_excess_8=res_8['initial_excess'],
    dim_8=res_8['dim'],
    n_gge_slot_8=res_8['n_gge_slot'],
    E_min_8=res_8['E_min'],
    E_max_8=res_8['E_max'],
    herm_err_8=res_8['herm_err'],
    delta_n_trace_8=res_8['delta_n_trace'],
    t_grid_8=res_8['t_grid'],
    # 12-cell
    c12_verts=np.asarray(c12_verts, dtype=int),
    dc_fraction_12=res_12['dc_fraction'],
    dc_signal_12=res_12['dc_signal'],
    initial_excess_12=res_12['initial_excess'],
    dim_12=res_12['dim'],
    n_gge_slot_12=res_12['n_gge_slot'],
    E_min_12=res_12['E_min'],
    E_max_12=res_12['E_max'],
    herm_err_12=res_12['herm_err'],
    delta_n_trace_12=res_12['delta_n_trace'],
    t_grid_12=res_12['t_grid'],
    # Framework constants used
    tau_fold=tau_fold,
    Delta_BCS=Delta_BCS,
    J_C2=J_C2,
    T_acoustic=T_acoustic,
    E_J_fold=E_J_fold,
    N_pair=2,  # (local)
    elapsed_s=time.time() - t_start,
)
print(f"\nData saved: {out_npz}")

# ============================================================
#  9. PLOT
# ============================================================

out_png = os.path.join(data_dir, 's74_dc_permanence.png')
fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.5))

# (a) DC fraction vs cell count
ax = axes[0]
ax.plot(N_cell_array, dc_array, 'o-', color='C0', markersize=9, lw=2,
        label='computed')
ax.axhspan(PASS_LO, PASS_HI, color='tab:green', alpha=0.18,
           label=f'PASS [{PASS_LO},{PASS_HI}]')
ax.axhspan(INFO_LO, PASS_LO, color='tab:olive', alpha=0.15)
ax.axhspan(PASS_HI, INFO_HI, color='tab:olive', alpha=0.15,
           label=f'INFO [{INFO_LO},{INFO_HI}]')
ax.axhline(dc_fraction_4cell, color='C3', ls=':', lw=1.0,
           label=f'S73B 4-cell = {dc_fraction_4cell:.3f}')
ax.set_xlabel('N_cells (ring length L)')
ax.set_ylabel('DC fraction  |<delta_n>_t| / |delta_n(0)|')
ax.set_title(f'N11-DC-PERMANENCE-74  [{gate_verdict}]')
ax.set_xticks(N_cell_array)
ax.set_ylim(0, max(0.35, dc_array.max() * 1.15))
ax.grid(True, alpha=0.35)
ax.legend(loc='best', fontsize=8)

# (b) delta_n(t) traces at 8 and 12 cells
ax = axes[1]
ax.plot(res_8['t_grid'], res_8['delta_n_trace'], color='C1',
        label=f'8-cell  DC={res_8["dc_fraction"]:.3f}', alpha=0.85)
ax.plot(res_12['t_grid'], res_12['delta_n_trace'], color='C2',
        label=f'12-cell DC={res_12["dc_fraction"]:.3f}', alpha=0.85)
ax.axhline(0.0, color='k', lw=0.6)
ax.axvline(res_8['t_grid'][len(res_8['t_grid']) // 2],
           color='k', ls='--', lw=0.6, label='t_max/2')
ax.set_xlabel('t  (M_KK^{-1})')
ax.set_ylabel('delta_n_{cell=1, B1}(t)')
ax.set_title('Perturbed-cell occupation vs GGE')
ax.grid(True, alpha=0.35)
ax.legend(loc='best', fontsize=8)

fig.tight_layout()
fig.savefig(out_png, dpi=150)
plt.close(fig)
print(f"Plot saved: {out_png}")

print()
print("=" * 72)
print(f"N11-DC-PERMANENCE-74 complete in {time.time()-t_start:.2f} s")
print(f"VERDICT: {gate_verdict}  |  "
      f"DC(4)={res_4['dc_fraction']:.4f}  "
      f"DC(8)={res_8['dc_fraction']:.4f}  "
      f"DC(12)={res_12['dc_fraction']:.4f}")
print("=" * 72)
