#!/usr/bin/env python3
"""
S75-L2-DC-PERMANENCE: DC Component Permanence Across Tessellation Sizes
========================================================================

Gate: S75-L2-DC-PERMANENCE
  PASS: DC fraction > 10% at both 8-cell and 12-cell
  INFO: DC fraction > 5% but < 10%
  FAIL: DC fraction < 5% at 12-cell (finite-size artifact)

Physics (substrate framing):
  A localized perturbation on one cell/mode of the BCS+Josephson tessellation
  evolves in time. The perturbation partially disperses across the ring via
  Josephson hopping and partially remains as a permanent DC offset — the
  component that lives on conserved charges of the integrable Josephson network.

  The DC fraction is defined (following S73B W4-A):
      DC_frac = |<delta_n(t)>_{t > t_max/2}| / |delta_n(0)|

  This computation tests the scaling of DC_frac from 1-cell (trivially 100%)
  through 4-cell, 8-cell, and 12-cell induced cycles in CG(24).

  Key structural fact: for an integrable system, the number of conserved
  charges grows with system size, but so does the phase space. The DC fraction
  is the ratio of conserved-charge weight to total weight in the localized
  perturbation's spectral decomposition.

Method:
  1. 1-cell: Analytical. No Josephson coupling => DC fraction = 1.0 exactly.
  2. 4-cell, 8-cell, 12-cell: Exact diagonalization of H_BCS + H_Josephson
     on C_L rings extracted as induced cycles from the CG(24) Cayley graph.
     N_pair=2 (matching S73B protocol). Dim = C(8*L, 2).  # (local)
  3. Localized perturbation: pin one pair at (cell=1, mode=B1) starting from
     ground state, then project out the pinned component and renormalize.
  4. Time evolution via spectral decomposition.
  5. DC extraction: late-time average |<delta_n>| / |delta_n(0)|.

Input files:
  computations/_shared/canonical_constants.py
  computations/session-56/s56_gge_fabric.npz   (eps_fold, V_fold, E_J_fold)
  computations/session-64/s64_local_entangle.npz  (CG(24) adjacency)

Output files:
  computations/session-75/s75_dc_permanence.npz
  computations/session-75/s75_dc_permanence.png

Session: S75 W3-N
Agent: quantum-acoustics-theorist
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
)

data_dir = os.path.dirname(os.path.abspath(__file__))
t_start = time.time()

print("=" * 72)
print("S75-L2-DC-PERMANENCE")
print("DC Component Permanence: 1-cell -> 4-cell -> 8-cell -> 12-cell")
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
N_vertices_cg24 = int(d64['N_vert'])  # (local)
assert adj_cg24.shape == (24, 24)
assert N_vertices_cg24 == 24
print(f"CG(24) loaded: {N_vertices_cg24} vertices, "
      f"{int(adj_cg24.sum())//2} edges, 6-regular, bipartite")

# BCS mode structure at the fold
d56 = np.load(os.path.join(data_dir, 's56_gge_fabric.npz'),
              allow_pickle=True)
eps_fold = np.asarray(d56['eps_fold'], dtype=float)
V_fold = np.asarray(d56['V_fold'], dtype=float)
E_J_fold = float(d56['E_J_fold'])
N_modes = len(eps_fold)  # (local) = 8
print(f"N_modes per cell = {N_modes}")
print(f"eps_fold = {np.round(eps_fold, 6)}")
print(f"E_J_fold = {E_J_fold:.6f} M_KK")
print()


# ============================================================
#  2. INDUCED CYCLE FINDER
# ============================================================

def find_induced_cycle(adj, N, L, start=0):
    """
    DFS for an induced cycle of length L in graph adj.
    Returns list of L vertex indices forming a cordless cycle, or None.
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
                continue
            chord = False  # (local)
            for idx_u, u in enumerate(path[:-1]):
                if adj[u, w] > 0.5:
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
    for i in range(L):
        for j in range(L):
            if i == j:
                continue
            if (j == (i + 1) % L) or (i == (j + 1) % L):
                continue
            assert adj[cycle[i], cycle[j]] < 0.5, (
                f"Chord {cycle[i]}-{cycle[j]} at positions {i}, {j}"
            )
    return True


# Find cycles
c4_verts = find_induced_cycle(adj_cg24, N_vertices_cg24, 4, start=0)
assert c4_verts is not None, "No induced C_4 found in CG(24)"
verify_induced_cycle(adj_cg24, c4_verts)
print(f"C_4 induced cycle:  {c4_verts}")

c8_verts = find_induced_cycle(adj_cg24, N_vertices_cg24, 8, start=0)
assert c8_verts is not None, "No induced C_8 found in CG(24)"
verify_induced_cycle(adj_cg24, c8_verts)
print(f"C_8 induced cycle:  {c8_verts}")

c12_verts = find_induced_cycle(adj_cg24, N_vertices_cg24, 12, start=0)
assert c12_verts is not None, "No induced C_12 found in CG(24)"
verify_induced_cycle(adj_cg24, c12_verts)
print(f"C_12 induced cycle: {c12_verts}")
print()


# ============================================================
#  3. CORE ROUTINE: DC FRACTION ON A RING
# ============================================================

def ring_adjacency(N_cells):
    """N_cells x N_cells adjacency for a ring C_{N_cells}."""
    A = np.zeros((N_cells, N_cells), dtype=float)  # (local)
    for i in range(N_cells):
        j = (i + 1) % N_cells
        A[i, j] = 1.0
        A[j, i] = 1.0
    return A


def compute_dc_fraction(N_cells, N_pair, eps_fold, V_fold, E_J_fold,
                        T_acoustic, J_C2, verbose=True):
    """
    Build H_BCS + H_Josephson on C_{N_cells} ring, prepare localized
    perturbation at (cell=1, B1), time-evolve, return DC fraction.

    DC fraction = |<delta_n_{cell=1,B1}(t)>_{t>t_max/2}| / |delta_n(0)|

    For N_cells=1 (isolated fiber), Josephson coupling is absent and
    the perturbation cannot decay: DC fraction = 1.0 exactly.
    """
    N_modes = len(eps_fold)  # (local)
    N_slots = N_modes * N_cells  # (local)
    dim = mcomb(N_slots, N_pair)  # (local)

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
    t_h = time.time()  # (local)
    H = np.zeros((dim, dim), dtype=float)  # (local)
    V_sym = (V_fold + V_fold.T) / 2.0  # (local) enforce symmetry

    for i, state_i in enumerate(basis):
        # Diagonal kinetic: sum_k 2*eps_k for occupied slots
        E_kin = 0.0  # (local)
        for slot in state_i:
            c, m = slot_to_cell_mode(slot)
            E_kin += 2.0 * eps_fold[m]
        H[i, i] += E_kin

        # Intra-cell pairing V_{kl}: pair hops within the same cell
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

        # Inter-cell Josephson hopping: same mode k, neighboring cells
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

    H = 0.5 * (H + H.T)  # enforce exact Hermiticity
    herm_err = np.max(np.abs(H - H.T))  # (local)
    if verbose:
        print(f"  H build: {time.time()-t_h:.2f} s, "
              f"Hermiticity err = {herm_err:.2e}")

    # --- Diagonalize ---
    t_d = time.time()  # (local)
    evals, evecs = eigh(H)
    if verbose:
        print(f"  Diagonalize: {time.time()-t_d:.2f} s, "
              f"E_min={evals[0]:.4f}, spread={evals[-1]-evals[0]:.4f}")

    # --- GGE reference (thermal at T_acoustic) ---
    beta_loc = 1.0 / T_acoustic  # (local) inverse GGE temperature
    w_unnorm = np.exp(-beta_loc * (evals - evals[0]))  # (local)
    Z_loc = np.sum(w_unnorm)  # (local)
    w_therm = w_unnorm / Z_loc  # (local) GGE weights

    # <n_slot>_GGE
    n_gge = np.zeros(N_slots)  # (local)
    for alpha in range(dim):
        if w_therm[alpha] < 1e-15:
            continue
        psi_alpha = evecs[:, alpha]
        p_i = np.abs(psi_alpha) ** 2  # (local)
        for i, state_i in enumerate(basis):
            if p_i[i] < 1e-20:
                continue
            for slot in state_i:
                n_gge[slot] += w_therm[alpha] * p_i[i]

    assert abs(np.sum(n_gge) - N_pair) < 1e-8, (
        f"GGE sum={np.sum(n_gge)} != N_pair={N_pair}"
    )

    # --- Perturbation: pin pair on (cell=1, mode=B1) ---
    # For 1-cell, cell index is 0 (only cell).
    # For multi-cell, perturb cell 1 to be consistent with S73B/S74.
    PERT_CELL = min(1, N_cells - 1)  # (local) cell 1 if available, else cell 0
    PERT_MODE = 0  # (local) B1 (eps_fold[0] ~ 0)
    PERT_SLOT = cell_mode_to_slot(PERT_CELL, PERT_MODE)  # (local)

    psi_gs = evecs[:, 0]  # (local) ground state
    psi_pert_raw = np.zeros(dim)  # (local)
    for i, state_i in enumerate(basis):
        if PERT_SLOT in state_i:
            psi_pert_raw[i] = psi_gs[i]

    norm_raw = np.linalg.norm(psi_pert_raw)  # (local)
    assert norm_raw > 1e-8, f"GS has zero weight on perturbed slot {PERT_SLOT}"
    psi_0 = psi_pert_raw / norm_raw  # (local)

    # --- Spectral decomposition of the perturbation ---
    c_alpha = evecs.T @ psi_0  # (local) overlap coefficients
    assert abs(np.sum(c_alpha ** 2) - 1.0) < 1e-10

    # --- Time grid (same as S73B/S74) ---
    tau_J_local = 1.0 / (2 * np.pi * J_C2)  # (local) Josephson time
    t_max = 40.0 * tau_J_local  # (local)
    n_t = 2000  # (local)
    t_grid = np.linspace(0.0, t_max, n_t)  # (local)

    # --- <n_{PERT_SLOT}(t)> via spectral sum ---
    diag_n = np.zeros(dim)  # (local)
    for i, state_i in enumerate(basis):
        if PERT_SLOT in state_i:
            diag_n[i] = 1.0

    M_eig = (evecs.T * diag_n) @ evecs  # (local) n_slot in eigenbasis

    # n(t) = sum_a c_a^2 M_aa + 2 sum_{a<b} c_a c_b M_ab cos((E_a-E_b)*t)
    stat_part = float(np.sum(c_alpha ** 2 * np.diag(M_eig)))  # (local)
    c_outer = np.outer(c_alpha, c_alpha)  # (local)
    AMP = c_outer * M_eig  # (local)

    iu = np.triu_indices(dim, k=1)  # (local)
    w_ab = 2.0 * AMP[iu]  # (local) off-diagonal spectral weights
    dE_ab = evals[iu[0]] - evals[iu[1]]  # (local) energy differences
    mask = np.abs(w_ab) > 1e-14  # (local)
    w_ab_k = w_ab[mask]  # (local) significant spectral pairs
    dE_ab_k = dE_ab[mask]  # (local)

    n_traces = np.full(n_t, stat_part, dtype=float)  # (local)
    batch = 200_000  # (local) rows per chunk for memory management
    n_pairs_kept = len(w_ab_k)  # (local)
    t_ev = time.time()  # (local)
    for b0 in range(0, n_pairs_kept, batch):
        b1 = min(b0 + batch, n_pairs_kept)
        phase = np.outer(dE_ab_k[b0:b1], t_grid)  # (local)
        n_traces += w_ab_k[b0:b1] @ np.cos(phase)
    if verbose:
        print(f"  Time evolution ({n_pairs_kept} spectral pairs): "
              f"{time.time()-t_ev:.2f} s")

    delta_n = n_traces - n_gge[PERT_SLOT]  # (local)

    # --- DC fraction (S73B protocol) ---
    half = n_t // 2  # (local)
    dc_signal = float(np.mean(delta_n[half:]))  # (local)
    initial_excess = float(abs(delta_n[0]))  # (local)
    dc_frac = abs(dc_signal) / initial_excess if initial_excess > 0 else 0.0  # (local)

    # --- Also compute the static spectral weight (analytical DC) ---
    # The static part is stat_part - n_gge[PERT_SLOT], which gives the
    # time-averaged DC component from the diagonal elements alone.
    dc_analytical = abs(stat_part - n_gge[PERT_SLOT])  # (local)
    dc_frac_analytical = dc_analytical / initial_excess if initial_excess > 0 else 0.0  # (local)

    if verbose:
        print(f"  delta_n(0)          = {delta_n[0]:.6f}")
        print(f"  <delta_n>_late      = {dc_signal:.6f}")
        print(f"  DC fraction (time)  = {dc_frac:.6f}")
        print(f"  DC fraction (spec)  = {dc_frac_analytical:.6f}")
        print(f"  PERT_CELL={PERT_CELL}, PERT_MODE={PERT_MODE}, "
              f"PERT_SLOT={PERT_SLOT}")

    return {
        'N_cells': N_cells,
        'N_slots': N_slots,
        'dim': dim,
        'dc_signal': dc_signal,
        'initial_excess': initial_excess,
        'dc_fraction': dc_frac,
        'dc_fraction_analytical': dc_frac_analytical,
        'n_gge_slot': float(n_gge[PERT_SLOT]),
        'stat_part': stat_part,
        'delta_n_trace': delta_n,
        't_grid': t_grid,
        'herm_err': float(herm_err),
        'E_min': float(evals[0]),
        'E_max': float(evals[-1]),
        'n_pairs_kept': n_pairs_kept,
        'pert_cell': PERT_CELL,
        'pert_mode': PERT_MODE,
    }


# ============================================================
#  4. 1-CELL (single fiber, analytical)
# ============================================================

print("=" * 72)
print("1-CELL (single isolated fiber)")
print("=" * 72)
print("  No inter-cell coupling => perturbation is a single-cell eigenstate.")
print("  Any localized perturbation is stationary. DC fraction = 1.0 exactly.")

# Verify by computation anyway for consistency
t1 = time.time()  # (local)
res_1 = compute_dc_fraction(
    N_cells=1,
    N_pair=2,  # (local)
    eps_fold=eps_fold,
    V_fold=V_fold,
    E_J_fold=E_J_fold,
    T_acoustic=T_acoustic,
    J_C2=J_C2,
    verbose=True,
)
print(f"  [1-cell elapsed: {time.time()-t1:.2f} s]")
print(f"  Computed DC fraction = {res_1['dc_fraction']:.6f} "
      f"(expected ~1.0 modulo intra-cell pairing)")
print()


# ============================================================
#  5. 4-CELL RING
# ============================================================

print("=" * 72)
print(f"4-CELL RING (induced C_4 from CG(24): {c4_verts})")
print("=" * 72)
t4 = time.time()  # (local)
res_4 = compute_dc_fraction(
    N_cells=4,
    N_pair=2,  # (local)
    eps_fold=eps_fold,
    V_fold=V_fold,
    E_J_fold=E_J_fold,
    T_acoustic=T_acoustic,
    J_C2=J_C2,
    verbose=True,
)
res_4['c_verts'] = np.asarray(c4_verts, dtype=int)
print(f"  [4-cell elapsed: {time.time()-t4:.2f} s]")
print()


# ============================================================
#  6. 8-CELL RING
# ============================================================

print("=" * 72)
print(f"8-CELL RING (induced C_8 from CG(24): {c8_verts})")
print("=" * 72)
t8 = time.time()  # (local)
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
#  7. 12-CELL RING
# ============================================================

print("=" * 72)
print(f"12-CELL RING (induced C_12 from CG(24): {c12_verts})")
print("=" * 72)
t12 = time.time()  # (local)
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
#  8. GATE CHECK
# ============================================================

print("=" * 72)
print("S75-L2-DC-PERMANENCE GATE")
print("=" * 72)

N_cell_array = np.array([1, 4, 8, 12])  # (local)
dc_array = np.array([
    res_1['dc_fraction'],
    res_4['dc_fraction'],
    res_8['dc_fraction'],
    res_12['dc_fraction'],
])  # (local)
dc_spec_array = np.array([
    res_1['dc_fraction_analytical'],
    res_4['dc_fraction_analytical'],
    res_8['dc_fraction_analytical'],
    res_12['dc_fraction_analytical'],
])  # (local)
dim_array = np.array([
    res_1['dim'], res_4['dim'], res_8['dim'], res_12['dim']
])  # (local)

print("\n DC fraction vs cell count:")
print(" N_cells   dim      DC_time    DC_spec")
for Nc, di, dcf, dcs in zip(N_cell_array, dim_array, dc_array, dc_spec_array):
    print(f"  {Nc:5d}  {di:6d}    {dcf:.6f}  {dcs:.6f}")

# Relative change from 4-cell
dc_rel_8 = (res_8['dc_fraction'] - res_4['dc_fraction']) / res_4['dc_fraction']  # (local)
dc_rel_12 = (res_12['dc_fraction'] - res_4['dc_fraction']) / res_4['dc_fraction']  # (local)
print(f"\n Relative change from 4-cell:")
print(f"  8-cell:  {dc_rel_8:+.2%}")
print(f"  12-cell: {dc_rel_12:+.2%}")

# Power-law fit: DC_frac ~ N^alpha
# Fit to the multi-cell data (4, 8, 12), excluding trivial 1-cell
log_N = np.log(N_cell_array[1:])  # (local) log(4), log(8), log(12)
log_DC = np.log(dc_array[1:])  # (local)
if np.all(dc_array[1:] > 0):
    coeffs = np.polyfit(log_N, log_DC, 1)  # (local)
    alpha_decay = coeffs[0]  # (local) power-law exponent
    print(f"\n Power-law fit DC ~ N^alpha (4,8,12-cell):")
    print(f"  alpha = {alpha_decay:.4f}")
    # Extrapolate to N=32 (physical tessellation)
    dc_extrap_32 = np.exp(np.polyval(coeffs, np.log(32)))  # (local)
    print(f"  Extrapolated DC(N=32) = {dc_extrap_32:.6f}")
else:
    alpha_decay = np.nan  # (local)
    dc_extrap_32 = np.nan  # (local)

# Gate evaluation
dc_8 = float(res_8['dc_fraction'])  # (local)
dc_12 = float(res_12['dc_fraction'])  # (local)
PASS_THRESH = 0.10  # (local) 10%
INFO_THRESH = 0.05  # (local) 5%

print(f"\n Gate thresholds:")
print(f"  PASS: DC > {PASS_THRESH:.0%} at BOTH 8-cell and 12-cell")
print(f"  INFO: DC > {INFO_THRESH:.0%} but < {PASS_THRESH:.0%}")
print(f"  FAIL: DC < {INFO_THRESH:.0%} at 12-cell")
print(f"\n  DC(8-cell)  = {dc_8:.6f}")
print(f"  DC(12-cell) = {dc_12:.6f}")

if dc_8 > PASS_THRESH and dc_12 > PASS_THRESH:
    gate_verdict = 'PASS'
    gate_reason = (
        f"DC(8)={dc_8:.4f} > 0.10 AND DC(12)={dc_12:.4f} > 0.10"
    )
elif dc_12 > INFO_THRESH:
    gate_verdict = 'INFO'
    gate_reason = (
        f"DC(12)={dc_12:.4f} > 0.05 but "
        + (f"DC(8)={dc_8:.4f} < 0.10" if dc_8 < PASS_THRESH
           else f"DC(12)={dc_12:.4f} < 0.10")
    )
else:
    gate_verdict = 'FAIL'
    gate_reason = (
        f"DC(12)={dc_12:.4f} < 0.05 threshold (finite-size artifact)"
    )

print(f"\n GATE VERDICT: {gate_verdict}")
print(f"  Reason: {gate_reason}")


# ============================================================
#  9. STRUCTURAL ANALYSIS
# ============================================================

print("\n" + "=" * 72)
print("STRUCTURAL ANALYSIS")
print("=" * 72)

# The DC fraction has a spectral interpretation:
# DC_frac = |sum_a |c_a|^2 M_aa - n_gge| / |delta_n(0)|
# This is the diagonal-ensemble average of the perturbation minus GGE.
# It measures how much the perturbation's spectral decomposition differs
# from the GGE on the observable n_slot.

print("\nSpectral decomposition of DC component:")
for label, res in [('1-cell', res_1), ('4-cell', res_4),
                   ('8-cell', res_8), ('12-cell', res_12)]:
    print(f"  {label}: stat_part={res['stat_part']:.6f}, "
          f"n_gge={res['n_gge_slot']:.6f}, "
          f"diff={abs(res['stat_part']-res['n_gge_slot']):.6f}, "
          f"initial={res['initial_excess']:.6f}")

# The key insight: as N_cells grows, the perturbation's spectral weight
# becomes more uniformly distributed across eigenstates (dilution),
# and the diagonal-ensemble average converges toward the GGE.
# If the system were ergodic (ETH), DC -> 0 as 1/sqrt(dim).
# If integrable, DC -> const * f(conserved charges).

print(f"\nETH prediction (1/sqrt(dim)) for comparison:")
for Nc, di, dcf in zip(N_cell_array, dim_array, dc_array):
    eth_pred = 1.0 / np.sqrt(di)  # (local) ETH decay rate
    print(f"  N={Nc:2d}: DC={dcf:.4f}, 1/sqrt(dim)={eth_pred:.4f}, "
          f"ratio={dcf/eth_pred:.2f}" if eth_pred > 0 else "")


# ============================================================
#  10. SAVE DATA
# ============================================================

out_npz = os.path.join(data_dir, 's75_dc_permanence.npz')
np.savez(
    out_npz,
    gate_name='S75-L2-DC-PERMANENCE',
    gate_verdict=gate_verdict,
    gate_reason=gate_reason,
    pass_thresh=PASS_THRESH,
    info_thresh=INFO_THRESH,
    # Arrays
    N_cell_array=N_cell_array,
    dim_array=dim_array,
    dc_array=dc_array,
    dc_spec_array=dc_spec_array,
    alpha_decay=alpha_decay,
    dc_extrap_32=dc_extrap_32,
    dc_rel_8=dc_rel_8,
    dc_rel_12=dc_rel_12,
    # 1-cell
    dc_fraction_1=res_1['dc_fraction'],
    dc_fraction_analytical_1=res_1['dc_fraction_analytical'],
    dc_signal_1=res_1['dc_signal'],
    initial_excess_1=res_1['initial_excess'],
    dim_1=res_1['dim'],
    stat_part_1=res_1['stat_part'],
    n_gge_slot_1=res_1['n_gge_slot'],
    # 4-cell
    c4_verts=np.asarray(c4_verts, dtype=int),
    dc_fraction_4=res_4['dc_fraction'],
    dc_fraction_analytical_4=res_4['dc_fraction_analytical'],
    dc_signal_4=res_4['dc_signal'],
    initial_excess_4=res_4['initial_excess'],
    dim_4=res_4['dim'],
    stat_part_4=res_4['stat_part'],
    n_gge_slot_4=res_4['n_gge_slot'],
    delta_n_trace_4=res_4['delta_n_trace'],
    t_grid_4=res_4['t_grid'],
    # 8-cell
    c8_verts=np.asarray(c8_verts, dtype=int),
    dc_fraction_8=res_8['dc_fraction'],
    dc_fraction_analytical_8=res_8['dc_fraction_analytical'],
    dc_signal_8=res_8['dc_signal'],
    initial_excess_8=res_8['initial_excess'],
    dim_8=res_8['dim'],
    stat_part_8=res_8['stat_part'],
    n_gge_slot_8=res_8['n_gge_slot'],
    delta_n_trace_8=res_8['delta_n_trace'],
    t_grid_8=res_8['t_grid'],
    herm_err_8=res_8['herm_err'],
    E_min_8=res_8['E_min'],
    E_max_8=res_8['E_max'],
    # 12-cell
    c12_verts=np.asarray(c12_verts, dtype=int),
    dc_fraction_12=res_12['dc_fraction'],
    dc_fraction_analytical_12=res_12['dc_fraction_analytical'],
    dc_signal_12=res_12['dc_signal'],
    initial_excess_12=res_12['initial_excess'],
    dim_12=res_12['dim'],
    stat_part_12=res_12['stat_part'],
    n_gge_slot_12=res_12['n_gge_slot'],
    delta_n_trace_12=res_12['delta_n_trace'],
    t_grid_12=res_12['t_grid'],
    herm_err_12=res_12['herm_err'],
    E_min_12=res_12['E_min'],
    E_max_12=res_12['E_max'],
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
#  11. PLOT
# ============================================================

out_png = os.path.join(data_dir, 's75_dc_permanence.png')
fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))

# (a) DC fraction vs cell count
ax = axes[0]
ax.plot(N_cell_array, dc_array, 'o-', color='C0', markersize=9, lw=2,
        label='DC fraction (time)')
ax.plot(N_cell_array, dc_spec_array, 's--', color='C4', markersize=7, lw=1.5,
        label='DC fraction (spectral)', alpha=0.7)
ax.axhspan(PASS_THRESH, 1.0, color='tab:green', alpha=0.08,
           label=f'PASS (>{PASS_THRESH:.0%})')
ax.axhspan(INFO_THRESH, PASS_THRESH, color='tab:olive', alpha=0.12,
           label=f'INFO ({INFO_THRESH:.0%}-{PASS_THRESH:.0%})')
ax.axhspan(0, INFO_THRESH, color='tab:red', alpha=0.08,
           label=f'FAIL (<{INFO_THRESH:.0%})')
# Power-law fit overlay
if not np.isnan(alpha_decay):
    N_fit = np.linspace(3, 14, 50)  # (local)
    dc_fit = np.exp(np.polyval(coeffs, np.log(N_fit)))  # (local)
    ax.plot(N_fit, dc_fit, ':', color='gray', lw=1.5,
            label=f'fit: N^{{{alpha_decay:.2f}}}')
ax.set_xlabel('N_cells (ring size)')
ax.set_ylabel('DC fraction')
ax.set_title(f'S75-L2-DC-PERMANENCE [{gate_verdict}]')
ax.set_xticks(N_cell_array)
ax.set_ylim(-0.02, 1.05)
ax.grid(True, alpha=0.35)
ax.legend(loc='upper right', fontsize=7)

# (b) delta_n(t) traces at 4, 8, 12 cells
ax = axes[1]
for label, res, col in [('4-cell', res_4, 'C0'),
                         ('8-cell', res_8, 'C1'),
                         ('12-cell', res_12, 'C2')]:
    ax.plot(res['t_grid'], res['delta_n_trace'], color=col,
            label=f'{label} DC={res["dc_fraction"]:.3f}', alpha=0.85)
ax.axhline(0.0, color='k', lw=0.6)
half_t = res_8['t_grid'][len(res_8['t_grid']) // 2]  # (local)
ax.axvline(half_t, color='k', ls='--', lw=0.6, label='t_max/2')
ax.set_xlabel('t (M_KK^{-1})')
ax.set_ylabel('delta_n_{cell=1, B1}(t)')
ax.set_title('Perturbation evolution')
ax.grid(True, alpha=0.35)
ax.legend(loc='best', fontsize=7)

# (c) DC fraction vs 1/sqrt(dim) (ETH comparison)
ax = axes[2]
inv_sqrt_dim = 1.0 / np.sqrt(dim_array.astype(float))  # (local)
ax.plot(inv_sqrt_dim[1:], dc_array[1:], 'o-', color='C0', markersize=9, lw=2,
        label='computed DC')
# ETH line
x_eth = np.linspace(0, inv_sqrt_dim[1] * 1.2, 50)  # (local)
ax.plot(x_eth, x_eth * dc_array[1] / inv_sqrt_dim[1], '--', color='gray',
        lw=1, label='ETH: DC ~ 1/sqrt(dim)')  # (local)
ax.set_xlabel('1/sqrt(dim)')
ax.set_ylabel('DC fraction')
ax.set_title('ETH scaling comparison')
ax.grid(True, alpha=0.35)
ax.legend(loc='best', fontsize=7)

fig.tight_layout()
fig.savefig(out_png, dpi=150)
plt.close(fig)
print(f"Plot saved: {out_png}")

print()
print("=" * 72)
elapsed_total = time.time() - t_start  # (local)
print(f"S75-L2-DC-PERMANENCE complete in {elapsed_total:.2f} s")
print(f"VERDICT: {gate_verdict}")
print(f"  DC(1)={res_1['dc_fraction']:.4f}  "
      f"DC(4)={res_4['dc_fraction']:.4f}  "
      f"DC(8)={res_8['dc_fraction']:.4f}  "
      f"DC(12)={res_12['dc_fraction']:.4f}")
if not np.isnan(alpha_decay):
    print(f"  Power-law: DC ~ N^{alpha_decay:.3f}")
    print(f"  Extrapolated DC(32) = {dc_extrap_32:.4f}")
print("=" * 72)
