#!/usr/bin/env python3
"""
s59_therm_order.py — THERM-ORDER-59: N_pair=4 and Crossover Fit
================================================================

Gate: THERM-ORDER-59
  PASS: N_c < 5 (crossover to GOE within small N_pair)
  FAIL: N_c > 10 (Poisson regime persists to large N_pair)
  INFO: N_c in [5, 10]

Physics:
  W0-2 returned FAIL: <r>_even(N=3) = 0.412, DECREASING from 0.442 at N=2.
  The Volovik crossover prediction (N_c ~ N_modes/2 = 4) is contradicted
  by the downward trend. This computation extends to N_pair = 4 to determine
  whether the trend continues (convergence to Poisson) or reverses.

  N_pair = 4 constructs C(16,4) = 1820 basis states. The 1820x1820  # (local)
  Hamiltonian is dense but diagonalizable in seconds on a modern CPU.

  The crossover fit uses:
    <r>(N) = r_GOE - (r_GOE - r_Poisson) * exp(-N/N_c)

  If <r>(N=4) < <r>(N=3) = 0.412, the trend is monotonically toward Poisson
  and N_c is effectively infinite (no crossover in this system). If <r>(N=4)
  reverses and increases, we fit N_c from the non-monotonic data.

Method:
  1. Load 2-cell Hamiltonian data from S56 (eps_fold, V_fold, E_J_fold)
  2. Load N=2 and N=3 results from S58/S59 npz files
  3. Construct 4-pair Fock space: C(16,4) = 1820 states
  4. Build H = H_BCS(cell_0) + H_BCS(cell_1) + H_Josephson
  5. Z_2 cell-exchange decomposition; diag each sector
  6. Compute <r>_even, <r>_odd with polynomial unfolding
  7. Fit crossover model to {N=2,3,4} data
  8. Report gate verdict

Session: S59 W4G-1
Agent: landau-condensed-matter-theorist
"""

import sys
import os
import time
import numpy as np
from itertools import combinations
from scipy.linalg import eigh
from scipy.optimize import curve_fit
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# === Import canonical constants ===
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
from canonical_constants import *

t_start = time.time()

# =====================================================================
#  1. LOAD INPUT DATA
# =====================================================================

data_dir = os.path.dirname(os.path.abspath(__file__))

# S56 GGE fabric data (2-cell system at fold)
d56 = np.load(os.path.join(data_dir, 's56_gge_fabric.npz'), allow_pickle=True)
eps_fold = d56['eps_fold']       # 8 single-particle energies at fold
eps_tau0 = d56['eps_tau0']       # 8 single-particle energies at tau=0
V_fold   = d56['V_fold']        # 8x8 pairing matrix
E_J_fold = float(d56['E_J_fold'])
E_J_tau0 = float(d56['E_J_tau0'])
tau_fold_actual = float(d56['tau_fold_actual'])

# N_pair=3 data from S59
d3 = np.load(os.path.join(data_dir, 's59_npair3_integ.npz'), allow_pickle=True)
r_even_np3 = float(d3['r_even'])
r_odd_np3  = float(d3['r_odd'])
r_combined_np3 = float(d3['r_combined'])
r_stderr_even_np3 = float(d3['r_stderr_even'])
delta_n_np3 = float(d3['delta_n_norm_np3'])
delta_n_np2_from3 = float(d3['delta_n_norm_np2'])
delta_n_np1_from3 = float(d3['delta_n_norm_np1'])

# N_pair=2 data from S58
d2 = np.load(os.path.join(data_dir, 's58_npair2_integ.npz'), allow_pickle=True)
r_even_np2 = float(d2['r_even'])
r_odd_np2  = float(d2['r_odd'])
r_combined_np2 = float(d2['r_combined'])
# S58 may not have r_stderr_even — compute from r_dist_even if absent
if 'r_stderr_even' in d2.files:
    r_stderr_even_np2 = float(d2['r_stderr_even'])
else:
    _r_dist = d2['r_dist_even']
    r_stderr_even_np2 = float(np.std(_r_dist) / np.sqrt(len(_r_dist)))
delta_n_np2 = float(d2['delta_n_norm'])

N_modes = 8  # modes per cell (local)
N_cells = 2   # cells
N_pair  = 4  # Cooper pairs for this run (local)

log_lines = []
def log(msg):
    log_lines.append(msg)

log("=" * 70)
log("S59 W4G-1: N_pair = 4 Exact Diagonalization — THERM-ORDER-59")
log("=" * 70)
log(f"tau_fold = {tau_fold_actual:.6f}")
log(f"E_J_fold = {E_J_fold:.4f} M_KK")
log(f"N_modes/cell = {N_modes}, N_cells = {N_cells}, N_pair = {N_pair}")
log(f"eps_fold = {eps_fold}")
log(f"Prior data: <r>_even(N=2) = {r_even_np2:.6f}, <r>_even(N=3) = {r_even_np3:.6f}")


# =====================================================================
#  2. CONSTRUCT PAIR FOCK SPACE (N_pair=4)
# =====================================================================

N_slots = N_modes * N_cells  # 16
pair_states = list(combinations(range(N_slots), N_pair))
dim = len(pair_states)
log(f"\nFock space: C({N_slots},{N_pair}) = {dim} four-pair states")
assert dim == 1820, f"Expected 1820, got {dim}"

# Map pair-slot to (mode, cell)
def slot_to_mode_cell(s):
    return (s % N_modes, s // N_modes)

# Pre-compute state info
state_info = []
for idx, slots in enumerate(pair_states):
    info = [slot_to_mode_cell(s) for s in slots]
    state_info.append(info)

# Index lookup
state_index = {s: i for i, s in enumerate(pair_states)}


# =====================================================================
#  3. CONSTRUCT HAMILTONIAN
# =====================================================================

def build_H_BCS_2cell(eps, V, E_J, n_pair, pair_st, st_info, st_idx, d):
    """
    Build the full BCS + Josephson Hamiltonian for N_pair on a 2-cell system.

    H = H_kinetic + H_pairing + H_Josephson
    """
    H = np.zeros((d, d), dtype=np.float64)

    for i, slots_i in enumerate(pair_st):
        slots_set = set(slots_i)
        infos = st_info[i]

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
                    H[i, i] -= V[m_p, m_p]
                    continue
                if new_slot in slots_set:
                    continue  # Pauli blocked
                new_slots = list(slots_i)
                new_slots[new_slots.index(old_slot)] = new_slot
                new_state = tuple(sorted(new_slots))
                if new_state in st_idx:
                    j = st_idx[new_state]
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
                if new_state in st_idx:
                    j = st_idx[new_state]
                    H[j, i] += -E_J / 2.0

    # Symmetrize
    H = 0.5 * (H + H.T)
    return H


log("\n--- Building Hamiltonian (1820x1820) ---")
t_build = time.time()
H_fold_full = build_H_BCS_2cell(eps_fold, V_fold, E_J_fold, N_pair,
                                 pair_states, state_info, state_index, dim)
t_build_done = time.time()
herm_check = np.max(np.abs(H_fold_full - H_fold_full.T))
log(f"H_fold_full: {H_fold_full.shape}, Hermiticity = {herm_check:.2e}, build time = {t_build_done - t_build:.2f}s")

# Also build no-J version for control
H_fold_noJ = build_H_BCS_2cell(eps_fold, V_fold, 0.0, N_pair,
                                pair_states, state_info, state_index, dim)
log(f"H_fold_noJ:  {H_fold_noJ.shape}, Hermiticity = {np.max(np.abs(H_fold_noJ - H_fold_noJ.T)):.2e}")

# tau=0 Hamiltonian for quench analysis
H_tau0_full = build_H_BCS_2cell(eps_tau0, V_fold, E_J_tau0, N_pair,
                                 pair_states, state_info, state_index, dim)

log("\n--- Diagonalizing (1820x1820) ---")
t_diag = time.time()
evals_fold_full, evecs_fold_full = eigh(H_fold_full)
evals_fold_noJ, evecs_fold_noJ  = eigh(H_fold_noJ)
evals_tau0_full, evecs_tau0_full = eigh(H_tau0_full)
t_diag_done = time.time()

log(f"Diagonalization time = {t_diag_done - t_diag:.2f}s")
log(f"E_GS(fold, full J) = {evals_fold_full[0]:.8f} M_KK")
log(f"E_GS(fold, no J)   = {evals_fold_noJ[0]:.8f} M_KK")
log(f"E_GS(tau=0, full J) = {evals_tau0_full[0]:.8f} M_KK")
log(f"Spectrum range (fold): [{evals_fold_full[0]:.4f}, {evals_fold_full[-1]:.4f}]")


# =====================================================================
#  4. LEVEL SPACING STATISTICS
# =====================================================================

def level_spacing_ratio(eigenvalues, unfold=True, deg=5):
    """
    Compute the mean adjacent gap ratio <r> for a spectrum.

    <r> = <min(s_n, s_{n+1}) / max(s_n, s_{n+1})>

    Poisson (integrable): <r> ~ 0.386
    GOE (chaotic):        <r> ~ 0.530
    """
    E = np.sort(eigenvalues)

    if unfold:
        N = np.arange(1, len(E) + 1)
        poly = np.polyfit(E, N, deg=min(deg, len(E) - 1))
        N_smooth = np.polyval(poly, E)
        E_unf = N_smooth
    else:
        E_unf = E

    s = np.diff(E_unf)
    s = s[s > 1e-12]  # remove degeneracies

    if len(s) < 3:
        return 0.0, np.array([])

    r_n = np.minimum(s[:-1], s[1:]) / np.maximum(s[:-1], s[1:])
    return np.mean(r_n), r_n


# =====================================================================
#  5. Z_2 SYMMETRY DECOMPOSITION
# =====================================================================

log("\n" + "=" * 70)
log("Z_2 CELL-EXCHANGE SYMMETRY DECOMPOSITION")
log("=" * 70)

def swap_slot(s):
    """Swap cell index of a pair-slot."""
    mode = s % N_modes
    cell = s // N_modes
    return (1 - cell) * N_modes + mode

# Build permutation matrix
P_mat = np.zeros((dim, dim), dtype=np.float64)
for i, slots in enumerate(pair_states):
    new_slots = tuple(sorted([swap_slot(s) for s in slots]))
    j = state_index[new_slots]
    P_mat[j, i] = 1.0

# Verify P^2 = I and [H, P] = 0
P2_check = np.max(np.abs(P_mat @ P_mat - np.eye(dim)))
commHP = H_fold_full @ P_mat - P_mat @ H_fold_full
comm_norm = np.max(np.abs(commHP))
log(f"P^2 = I check: max|P^2 - I| = {P2_check:.2e}")
log(f"[H_fold, P] = 0 check: max|[H,P]| = {comm_norm:.2e}")

# Project onto Z_2 sectors
P_evals, P_evecs = eigh(P_mat)
even_mask = P_evals > 0.5
odd_mask  = P_evals < -0.5
n_even = np.sum(even_mask)
n_odd  = np.sum(odd_mask)
log(f"Z_2 sectors: even = {n_even}, odd = {n_odd}, total = {n_even + n_odd}")

# Diagonalize H in each sector
Q_even = P_evecs[:, even_mask]
H_even = Q_even.T @ H_fold_full @ Q_even
evals_even, evecs_even_proj = eigh(H_even)

Q_odd = P_evecs[:, odd_mask]
H_odd = Q_odd.T @ H_fold_full @ Q_odd
evals_odd, evecs_odd_proj = eigh(H_odd)

# <r> in each sector
r_even_np4, r_dist_even = level_spacing_ratio(evals_even)
r_odd_np4, r_dist_odd   = level_spacing_ratio(evals_odd)
r_even_raw, _ = level_spacing_ratio(evals_even, unfold=False)
r_odd_raw, _  = level_spacing_ratio(evals_odd, unfold=False)

n_gaps_even = len(r_dist_even)
n_gaps_odd  = len(r_dist_odd)
r_combined_np4 = (n_gaps_even * r_even_np4 + n_gaps_odd * r_odd_np4) / max(1, n_gaps_even + n_gaps_odd)

r_stderr_even_np4 = np.std(r_dist_even) / np.sqrt(n_gaps_even) if n_gaps_even > 0 else 0
r_stderr_odd_np4  = np.std(r_dist_odd) / np.sqrt(n_gaps_odd) if n_gaps_odd > 0 else 0
r_stderr_combined = np.sqrt((n_gaps_even * r_stderr_even_np4)**2 + (n_gaps_odd * r_stderr_odd_np4)**2) / max(1, n_gaps_even + n_gaps_odd)

log(f"\n<r>_even (N=4, {n_even} levels, {n_gaps_even} gaps): {r_even_np4:.6f} +/- {r_stderr_even_np4:.4f}")
log(f"<r>_odd  (N=4, {n_odd} levels, {n_gaps_odd} gaps):  {r_odd_np4:.6f} +/- {r_stderr_odd_np4:.4f}")
log(f"<r>_combined: {r_combined_np4:.6f} +/- {r_stderr_combined:.4f}")
log(f"Raw (no unfolding): even={r_even_raw:.6f}, odd={r_odd_raw:.6f}")

# Unfolding robustness
log("\n--- Unfolding robustness check ---")
for deg in [3, 5, 7, 9]:
    r_e, _ = level_spacing_ratio(evals_even, deg=deg)
    r_o, _ = level_spacing_ratio(evals_odd, deg=deg)
    wt = n_gaps_even * r_e + n_gaps_odd * r_o
    r_c = wt / max(1, n_gaps_even + n_gaps_odd)
    log(f"  poly deg {deg}: <r>_even = {r_e:.4f}, <r>_odd = {r_o:.4f}, combined = {r_c:.4f}")

# Control: no-J
H_even_noJ = Q_even.T @ H_fold_noJ @ Q_even
H_odd_noJ  = Q_odd.T  @ H_fold_noJ @ Q_odd
evals_even_noJ, _ = eigh(H_even_noJ)
evals_odd_noJ, _  = eigh(H_odd_noJ)
r_even_noJ, r_dist_even_noJ = level_spacing_ratio(evals_even_noJ)
r_odd_noJ, r_dist_odd_noJ   = level_spacing_ratio(evals_odd_noJ)
n_gaps_even_noJ = len(r_dist_even_noJ)
n_gaps_odd_noJ = len(r_dist_odd_noJ)
r_combined_noJ = (n_gaps_even_noJ * r_even_noJ + n_gaps_odd_noJ * r_odd_noJ) / max(1, n_gaps_even_noJ + n_gaps_odd_noJ)
log(f"\nControl (E_J = 0): <r>_even = {r_even_noJ:.6f}, <r>_odd = {r_odd_noJ:.6f}, combined = {r_combined_noJ:.6f}")


# =====================================================================
#  6. QUENCH DYNAMICS AND GGE OCCUPATION NUMBERS
# =====================================================================

log("\n" + "=" * 70)
log("QUENCH DYNAMICS: tau=0 -> tau_fold")
log("=" * 70)

psi0 = evecs_tau0_full[:, 0]
c_n = evecs_fold_full.T @ psi0
p_n = c_n**2
E_DE = np.sum(p_n * evals_fold_full)
P_exc = 1.0 - p_n[0]
p_nz = p_n[p_n > 1e-30]
S_DE = -np.sum(p_nz * np.log(p_nz))

log(f"Sum |c_n|^2 = {np.sum(p_n):.10f}")
log(f"E_DE = {E_DE:.6f}, E_GS = {evals_fold_full[0]:.6f}")
log(f"E_exc = {E_DE - evals_fold_full[0]:.6f}")
log(f"P_exc = {P_exc:.8f}")
log(f"S_DE = {S_DE:.6f}, S_max = {np.log(dim):.6f}, S_DE/S_max = {S_DE/np.log(dim):.6f}")

# Build pair number operators
def build_pair_number_op(mode, cell, n_pair, pair_st, d):
    n_op = np.zeros((d, d))
    slot = cell * N_modes + mode
    for i, slots in enumerate(pair_st):
        if slot in slots:
            n_op[i, i] = 1.0
    return n_op

nk_DE_4pair = np.zeros((N_cells, N_modes))
nk_GS_4pair = np.zeros((N_cells, N_modes))
psi_GS = evecs_fold_full[:, 0]

for c in range(N_cells):
    for k in range(N_modes):
        n_k = build_pair_number_op(k, c, N_pair, pair_states, dim)
        nk_DE_4pair[c, k] = np.sum(p_n * np.diag(evecs_fold_full.T @ n_k @ evecs_fold_full))
        nk_GS_4pair[c, k] = psi_GS @ n_k @ psi_GS

delta_n_4pair = nk_DE_4pair - nk_GS_4pair
delta_n_np4 = np.linalg.norm(delta_n_4pair)

log(f"\nGGE occupations: Sum = {np.sum(nk_DE_4pair):.6f} (should be {N_pair})")
log(f"GS occupations:  Sum = {np.sum(nk_GS_4pair):.6f}")
log(f"||delta_n|| = {delta_n_np4:.8f}")


# =====================================================================
#  7. OCCUPATION NUMBER SCALING
# =====================================================================

log("\n" + "-" * 70)
log("OCCUPATION NUMBER SCALING: ||delta_n|| vs N_pair")
log("-" * 70)

ns_scaling = np.array([1, 2, 3, 4], dtype=float)
dns_scaling = np.array([delta_n_np1_from3, delta_n_np2_from3, delta_n_np3, delta_n_np4])
log(f"||delta_n||: N=1: {dns_scaling[0]:.8f}, N=2: {dns_scaling[1]:.8f}, N=3: {dns_scaling[2]:.8f}, N=4: {dns_scaling[3]:.8f}")

mask_nz = dns_scaling > 0
if np.sum(mask_nz) >= 2:
    coeffs = np.polyfit(np.log(ns_scaling[mask_nz]), np.log(dns_scaling[mask_nz]), 1)
    alpha_scaling = coeffs[0]
    log(f"Power law exponent: alpha = {alpha_scaling:.4f}")


# =====================================================================
#  8. ENTANGLEMENT ENTROPY
# =====================================================================

log("\n" + "=" * 70)
log("ENTANGLEMENT ENTROPY")
log("=" * 70)

def get_cell_content(state_idx, st_info_local):
    infos = st_info_local[state_idx]
    cell0 = tuple(sorted([m for m, c in infos if c == 0]))
    cell1 = tuple(sorted([m for m, c in infos if c == 1]))
    return cell0, cell1

cell0_states = set()
cell1_states = set()
for i in range(dim):
    c0, c1 = get_cell_content(i, state_info)
    cell0_states.add(c0)
    cell1_states.add(c1)

cell0_list = sorted(cell0_states)
cell1_list = sorted(cell1_states)
cell0_idx = {s: i for i, s in enumerate(cell0_list)}
cell1_idx = {s: i for i, s in enumerate(cell1_list)}
d0 = len(cell0_list)
d1 = len(cell1_list)
log(f"Cell-0 sub-basis: {d0}, Cell-1 sub-basis: {d1}")

def entanglement_entropy(psi, d0_local, d1_local, cell0_idx_local, cell1_idx_local, dim_local, st_info_local):
    C = np.zeros((d0_local, d1_local))
    for i in range(dim_local):
        c0, c1 = get_cell_content(i, st_info_local)
        a = cell0_idx_local[c0]
        b = cell1_idx_local[c1]
        C[a, b] += psi[i]
    _, sigma, _ = np.linalg.svd(C, full_matrices=False)
    sigma2 = sigma**2
    sigma2 = sigma2[sigma2 > 1e-30]
    return -np.sum(sigma2 * np.log(sigma2))

S_ent_GS = entanglement_entropy(evecs_fold_full[:, 0], d0, d1, cell0_idx, cell1_idx, dim, state_info)
S_ent_DE = np.sum([p_n[n] * entanglement_entropy(evecs_fold_full[:, n], d0, d1, cell0_idx, cell1_idx, dim, state_info) for n in range(dim)])
S_ent_quench = entanglement_entropy(psi0, d0, d1, cell0_idx, cell1_idx, dim, state_info)

log(f"S_ent(GS, fold) = {S_ent_GS:.6f}")
log(f"S_ent(DE avg)   = {S_ent_DE:.6f}")
log(f"S_ent(initial)  = {S_ent_quench:.6f}")
log(f"S_max = log(min({d0},{d1})) = {np.log(min(d0, d1)):.6f}")


# =====================================================================
#  9. PARTICIPATION RATIOS
# =====================================================================

log("\n" + "=" * 70)
log("PARTICIPATION RATIOS")
log("=" * 70)

PR_fold = np.zeros(dim)
for n in range(dim):
    psi = evecs_fold_full[:, n]
    ipr = np.sum(psi**4)
    PR_fold[n] = 1.0 / ipr if ipr > 0 else 0.0

PR_noJ = np.zeros(dim)
for n in range(dim):
    psi = evecs_fold_noJ[:, n]
    ipr = np.sum(psi**4)
    PR_noJ[n] = 1.0 / ipr if ipr > 0 else 0.0

log(f"Mean PR (full J): {np.mean(PR_fold):.2f} / {dim}")
log(f"Mean PR (no J):   {np.mean(PR_noJ):.2f} / {dim}")
log(f"PR ratio: {np.mean(PR_fold)/max(np.mean(PR_noJ), 1e-10):.3f}")


# =====================================================================
#  10. COMMUTATOR ANALYSIS
# =====================================================================

log("\n" + "=" * 70)
log("COMMUTATOR ANALYSIS")
log("=" * 70)

H_norm = np.linalg.norm(H_fold_full, 'fro')
comm_norms_full = np.zeros((N_cells, N_modes))
for c in range(N_cells):
    for k in range(N_modes):
        n_k = build_pair_number_op(k, c, N_pair, pair_states, dim)
        comm = H_fold_full @ n_k - n_k @ H_fold_full
        comm_norms_full[c, k] = np.linalg.norm(comm, 'fro')

log(f"[H, n_k] / ||H|| (cell 0): {comm_norms_full[0] / H_norm}")
log(f"[H, n_k] / ||H|| (cell 1): {comm_norms_full[1] / H_norm}")
log(f"Max commutator / ||H||: {np.max(comm_norms_full / H_norm):.6f}")

threshold_integ = 0.01  # (local)
n_surviving = np.sum(comm_norms_full / H_norm < threshold_integ)
log(f"Surviving integrals (||[H,n_k]||/||H|| < {threshold_integ}): {n_surviving} / {N_cells * N_modes}")


# =====================================================================
#  11. CROSSOVER FIT
# =====================================================================

log("\n" + "=" * 70)
log("CROSSOVER FIT: <r>(N) = r_GOE - (r_GOE - r_Poi) * exp(-N/N_c)")
log("=" * 70)

r_Poisson = 0.3863  # (local)
r_GOE = r_GOE_canonical  # canonical alias (was: = 0.5307)

# Collected data points
N_data = np.array([2, 3, 4], dtype=float)
r_data = np.array([r_even_np2, r_even_np3, r_even_np4])
r_err  = np.array([r_stderr_even_np2, r_stderr_even_np3, r_stderr_even_np4])

log(f"\nData points:")
log(f"  N=2: <r>_even = {r_even_np2:.6f} +/- {r_stderr_even_np2:.4f}")
log(f"  N=3: <r>_even = {r_even_np3:.6f} +/- {r_stderr_even_np3:.4f}")
log(f"  N=4: <r>_even = {r_even_np4:.6f} +/- {r_stderr_even_np4:.4f}")

# Check monotonicity
is_decreasing_23 = r_even_np3 < r_even_np2
is_decreasing_34 = r_even_np4 < r_even_np3
monotone_down = is_decreasing_23 and is_decreasing_34

log(f"\nTrend: N=2->3: {'DECREASE' if is_decreasing_23 else 'INCREASE'} ({r_even_np3 - r_even_np2:+.4f})")
log(f"Trend: N=3->4: {'DECREASE' if is_decreasing_34 else 'INCREASE'} ({r_even_np4 - r_even_np3:+.4f})")

# Attempt crossover fit
def crossover_model(N, N_c):
    return r_GOE - (r_GOE - r_Poisson) * np.exp(-N / N_c)

# Also try a more general model allowing for non-GOE asymptote
def crossover_general(N, N_c, r_inf):
    return r_inf - (r_inf - r_Poisson) * np.exp(-N / N_c)

N_c_fit = np.nan
N_c_err = np.nan
r_inf_fit = np.nan
fit_success = False

try:
    # Standard GOE crossover
    popt, pcov = curve_fit(crossover_model, N_data, r_data,
                           p0=[5.0], bounds=(0.1, 100.0),
                           sigma=r_err if np.all(r_err > 0) else None)
    N_c_fit = popt[0]
    N_c_err = np.sqrt(pcov[0, 0]) if pcov[0, 0] > 0 else np.nan
    fit_success = True
    log(f"\nStandard crossover fit: N_c = {N_c_fit:.2f} +/- {N_c_err:.2f}")

    # Residuals
    r_fit = crossover_model(N_data, N_c_fit)
    chi2 = np.sum(((r_data - r_fit) / r_err)**2) if np.all(r_err > 0) else np.sum((r_data - r_fit)**2)
    log(f"  chi^2 = {chi2:.4f} (dof = {len(N_data) - 1})")
except Exception as e:
    log(f"\nStandard crossover fit FAILED: {e}")

# General fit with free asymptote
try:
    popt2, pcov2 = curve_fit(crossover_general, N_data, r_data,
                              p0=[5.0, 0.53], bounds=([0.1, 0.386], [200.0, 0.65]),
                              sigma=r_err if np.all(r_err > 0) else None)
    N_c_gen = popt2[0]
    r_inf_gen = popt2[1]
    log(f"General crossover fit: N_c = {N_c_gen:.2f}, r_inf = {r_inf_gen:.4f}")
except Exception as e:
    N_c_gen = np.nan
    r_inf_gen = np.nan
    log(f"General crossover fit FAILED: {e}")

# If trend is monotonically decreasing, the crossover model may not apply
if monotone_down:
    # Fit a linear model instead
    slope = np.polyfit(N_data, r_data, 1)
    N_poisson = (r_Poisson - slope[1]) / slope[0] if abs(slope[0]) > 1e-10 else np.inf
    log(f"\nMonotonically DECREASING: linear fit slope = {slope[0]:.4f}/pair")
    log(f"Extrapolated Poisson crossing at N ~ {N_poisson:.1f}")
    log(f"System converges TOWARD Poisson (integrability), NOT toward GOE")

# Whether or not data is all below Poisson
all_below_poisson = np.all(r_data < r_Poisson)
if all_below_poisson:
    log(f"\nALL data points below Poisson ({r_Poisson:.4f}). Sub-Poisson statistics.")
    log(f"This indicates clustering/attraction of levels, not regular spacing.")


# =====================================================================
#  12. V_FOLD SEPARABILITY
# =====================================================================

log("\n" + "=" * 70)
log("V_FOLD SEPARABILITY ANALYSIS")
log("=" * 70)

U_V, S_V, Vt_V = np.linalg.svd(V_fold)
rank1_frac = S_V[0] / np.sum(S_V)
log(f"V_fold SVD values: {S_V}")
log(f"Rank-1 fraction: {rank1_frac:.4f}")

# Build pairing-only Hamiltonian
H_pair_only = np.zeros((dim, dim), dtype=np.float64)
for i, slots_i in enumerate(pair_states):
    slots_set = set(slots_i)
    infos = state_info[i]
    for p_idx in range(N_pair):
        m_p, c_p = infos[p_idx]
        old_slot = c_p * N_modes + m_p
        for k in range(N_modes):
            new_slot = c_p * N_modes + k
            if k == m_p:
                H_pair_only[i, i] -= V_fold[m_p, m_p]
                continue
            if new_slot in slots_set:
                continue
            new_slots = list(slots_i)
            new_slots[new_slots.index(old_slot)] = new_slot
            new_state = tuple(sorted(new_slots))
            if new_state in state_index:
                j = state_index[new_state]
                H_pair_only[j, i] -= V_fold[k, m_p]
H_pair_only = 0.5 * (H_pair_only + H_pair_only.T)

# Rank-1 approximation
V_rank1 = S_V[0] * np.outer(U_V[:, 0], Vt_V[0, :])
V_rank1 = 0.5 * (V_rank1 + V_rank1.T)

H_pair_rank1 = np.zeros((dim, dim), dtype=np.float64)
for i, slots_i in enumerate(pair_states):
    slots_set = set(slots_i)
    infos = state_info[i]
    for p_idx in range(N_pair):
        m_p, c_p = infos[p_idx]
        old_slot = c_p * N_modes + m_p
        for k in range(N_modes):
            new_slot = c_p * N_modes + k
            if k == m_p:
                H_pair_rank1[i, i] -= V_rank1[m_p, m_p]
                continue
            if new_slot in slots_set:
                continue
            new_slots = list(slots_i)
            new_slots[new_slots.index(old_slot)] = new_slot
            new_state = tuple(sorted(new_slots))
            if new_state in state_index:
                j = state_index[new_state]
                H_pair_rank1[j, i] -= V_rank1[k, m_p]
H_pair_rank1 = 0.5 * (H_pair_rank1 + H_pair_rank1.T)

norm_full = np.linalg.norm(H_pair_only, 'fro')
norm_rank1 = np.linalg.norm(H_pair_rank1, 'fro')
norm_resid = np.linalg.norm(H_pair_only - H_pair_rank1, 'fro')
sep_frac_4pair = 1.0 - (norm_resid / norm_full) if norm_full > 0 else 0

log(f"||H_pair|| = {norm_full:.6f}")
log(f"||H_pair_rk1|| = {norm_rank1:.6f}")
log(f"||residual|| = {norm_resid:.6f}")
log(f"Separability fraction (N=4): {sep_frac_4pair:.4f}")


# =====================================================================
#  13. GATE VERDICT
# =====================================================================

log("\n" + "=" * 70)
log("GATE VERDICT: THERM-ORDER-59")
log("=" * 70)

log(f"\n--- Crossover data ---")
log(f"  N=2: <r>_even = {r_even_np2:.4f} +/- {r_stderr_even_np2:.4f}")
log(f"  N=3: <r>_even = {r_even_np3:.4f} +/- {r_stderr_even_np3:.4f}")
log(f"  N=4: <r>_even = {r_even_np4:.4f} +/- {r_stderr_even_np4:.4f}")
log(f"  Trend 2->3: {r_even_np3 - r_even_np2:+.4f}")
log(f"  Trend 3->4: {r_even_np4 - r_even_np3:+.4f}")

if fit_success:
    log(f"\n  Crossover scale N_c = {N_c_fit:.2f} +/- {N_c_err:.2f}")

log(f"\n  Poisson = {r_Poisson:.4f}, GOE = {r_GOE:.4f}")

# Verdict logic:
# If N_c < 5: PASS
# If N_c > 10: FAIL
# If N_c in [5,10]: INFO
# If fit fails (monotonic decrease): FAIL (no crossover)

if fit_success and N_c_fit < 5:
    verdict = "PASS"
    detail = f"N_c = {N_c_fit:.2f} < 5. Crossover to GOE occurs within small N_pair"
elif fit_success and N_c_fit > 10:
    verdict = "FAIL"
    detail = f"N_c = {N_c_fit:.2f} > 10. Poisson regime persists to large N_pair"
elif fit_success:
    verdict = "INFO"
    detail = f"N_c = {N_c_fit:.2f} in [5, 10]. Intermediate crossover scale"
elif monotone_down:
    verdict = "FAIL"
    detail = f"<r>_even monotonically decreasing: {r_even_np2:.4f} -> {r_even_np3:.4f} -> {r_even_np4:.4f}. No GOE crossover; system converges to Poisson"
else:
    # Non-monotonic but fit failed
    verdict = "INFO"
    detail = f"Non-monotonic trend but crossover fit failed. <r>_even: {r_even_np2:.4f}, {r_even_np3:.4f}, {r_even_np4:.4f}"

log(f"\n>>> VERDICT: {verdict}")
log(f">>> {detail}")

t_total = time.time() - t_start
log(f"\nTotal runtime: {t_total:.1f}s")


# =====================================================================
#  14. SAVE DATA
# =====================================================================

save_path = os.path.join(data_dir, 's59_therm_order.npz')
np.savez(save_path,
    # Metadata
    N_pair=N_pair,
    N_modes=N_modes,
    N_cells=N_cells,
    dim=dim,
    tau_fold=tau_fold_actual,
    E_J_fold=E_J_fold,
    E_J_tau0=E_J_tau0,

    # Spectra
    evals_fold_full=evals_fold_full,
    evals_fold_noJ=evals_fold_noJ,
    evals_tau0_full=evals_tau0_full,
    evals_even=evals_even,
    evals_odd=evals_odd,

    # Level statistics — N=4
    r_even=r_even_np4,
    r_odd=r_odd_np4,
    r_combined=r_combined_np4,
    r_combined_noJ=r_combined_noJ,
    r_dist_even=r_dist_even,
    r_dist_odd=r_dist_odd,
    r_stderr_even=r_stderr_even_np4,
    r_stderr_odd=r_stderr_odd_np4,
    r_even_raw=r_even_raw,
    r_odd_raw=r_odd_raw,

    # All N_pair data
    N_data=N_data,
    r_even_data=r_data,
    r_even_err=r_err,
    r_even_np2=r_even_np2,
    r_even_np3=r_even_np3,
    r_even_np4=r_even_np4,

    # Crossover fit
    N_c_fit=N_c_fit,
    N_c_err=N_c_err,
    fit_success=fit_success,
    monotone_down=monotone_down,

    # Quench dynamics
    c_n_quench=c_n,
    p_n_quench=p_n,
    E_DE=E_DE,
    S_DE=S_DE,
    P_exc=P_exc,
    nk_DE_4pair=nk_DE_4pair,
    nk_GS_4pair=nk_GS_4pair,
    delta_n_norm=delta_n_np4,

    # Entanglement
    S_ent_GS=S_ent_GS,
    S_ent_DE=S_ent_DE,
    S_ent_quench=S_ent_quench,

    # Integrability
    comm_norms_full=comm_norms_full,
    n_surviving_integrals=n_surviving,

    # Participation ratios
    PR_fold_mean=np.mean(PR_fold),
    PR_noJ_mean=np.mean(PR_noJ),

    # Separability
    V_svd_values=S_V,
    rank1_frac=rank1_frac,
    sep_frac_4pair=sep_frac_4pair,

    # Scaling
    delta_n_scaling=dns_scaling,

    # Gate
    gate_name=np.array(['THERM-ORDER-59']),
    gate_verdict=np.array([verdict]),
    gate_detail=np.array([detail]),
)
log(f"Data saved to {save_path}")

# Write log
log_path = os.path.join(data_dir, 's59_therm_order_log.txt')
with open(log_path, 'w') as f:
    f.write('\n'.join(log_lines))


# =====================================================================
#  15. PLOTS
# =====================================================================

fig, axes = plt.subplots(2, 3, figsize=(18, 11))
fig.suptitle(f'S59 W4G-1: THERM-ORDER-59 — N_pair=4 Crossover Analysis — {verdict}',
             fontsize=14, fontweight='bold')

# (a) <r> vs N_pair — the key plot
ax = axes[0, 0]
N_all = np.array([2, 3, 4])
r_all = np.array([r_even_np2, r_even_np3, r_even_np4])
r_err_all = np.array([r_stderr_even_np2, r_stderr_even_np3, r_stderr_even_np4])

ax.errorbar(N_all, r_all, yerr=r_err_all, fmt='o-', color='blue',
            markersize=8, capsize=5, label=r'$\langle r \rangle_{\mathrm{even}}$')
ax.axhline(y=r_Poisson, color='green', linestyle='--', label=f'Poisson ({r_Poisson:.3f})')
ax.axhline(y=r_GOE, color='red', linestyle='--', label=f'GOE ({r_GOE:.3f})')

# Plot fit if successful
if fit_success:
    N_fine = np.linspace(1, 8, 100)
    r_fit_fine = crossover_model(N_fine, N_c_fit)
    ax.plot(N_fine, r_fit_fine, 'k--', alpha=0.5, label=f'Fit: $N_c={N_c_fit:.1f}$')

ax.set_xlabel('$N_{\\mathrm{pair}}$', fontsize=12)
ax.set_ylabel(r'$\langle r \rangle_{\mathrm{even}}$', fontsize=12)
ax.set_title(r'Level Statistics Crossover')
ax.set_xlim(0.5, 5.5)
ax.set_ylim(0.3, 0.6)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# (b) Spectrum comparison (full vs noJ)
ax = axes[0, 1]
ax.plot(evals_fold_full, np.arange(dim), 'b-', label='Full (with $E_J$)', linewidth=0.5)
ax.plot(evals_fold_noJ, np.arange(dim), 'r-', label='No $E_J$', linewidth=0.5, alpha=0.5)
ax.set_xlabel('$E$ ($M_{KK}$)', fontsize=12)
ax.set_ylabel('Cumulative count', fontsize=12)
ax.set_title(f'Spectrum ($N_{{pair}}=4$, dim={dim})')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# (c) Level spacing distribution (even sector)
ax = axes[0, 2]
if len(r_dist_even) > 10:
    ax.hist(r_dist_even, bins=30, density=True, alpha=0.7, color='blue', label='Even sector')
    r_grid = np.linspace(0, 1, 200)
    # Poisson: P(r) = 2/(1+r)^2
    ax.plot(r_grid, 2.0 / (1 + r_grid)**2, 'g-', linewidth=2, label='Poisson')
    # GOE: P(r) = (27/4)(r+r^2)/(1+r+r^2)^{5/2}
    ax.plot(r_grid, (27.0/4.0) * (r_grid + r_grid**2) / (1 + r_grid + r_grid**2)**2.5,
            'r-', linewidth=2, label='GOE')
    ax.axvline(x=r_even_np4, color='blue', linestyle=':', linewidth=2, label=f'$\\langle r \\rangle = {r_even_np4:.3f}$')
ax.set_xlabel('$r$', fontsize=12)
ax.set_ylabel('$P(r)$', fontsize=12)
ax.set_title(f'Gap Ratio Distribution (even, N=4)')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# (d) Occupation number comparison
ax = axes[1, 0]
modes = np.arange(N_modes)
width = 0.35  # (local)
ax.bar(modes - width/2, nk_GS_4pair[0], width, label='GS cell 0', alpha=0.7, color='blue')
ax.bar(modes + width/2, nk_DE_4pair[0], width, label='DE cell 0', alpha=0.7, color='red')
ax.set_xlabel('Mode index', fontsize=12)
ax.set_ylabel('Pair occupation', fontsize=12)
ax.set_title('Pair Occupations ($N_{pair}=4$, cell 0)')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# (e) Scaling: ||delta_n|| vs N
ax = axes[1, 1]
ax.plot([1, 2, 3, 4], dns_scaling, 'bo-', markersize=8, label=r'$||\delta n||$')
if np.sum(mask_nz) >= 2:
    N_fine = np.linspace(1, 5, 50)
    ax.plot(N_fine, np.exp(coeffs[1]) * N_fine**alpha_scaling, 'r--',
            label=f'$N^{{{alpha_scaling:.2f}}}$')
ax.set_xlabel('$N_{\\mathrm{pair}}$', fontsize=12)
ax.set_ylabel('$||\\delta n||$', fontsize=12)
ax.set_title('Occupation Deviation Scaling')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# (f) Participation ratio histogram
ax = axes[1, 2]
ax.hist(PR_fold, bins=40, alpha=0.7, color='blue', label=f'Full $E_J$ (mean={np.mean(PR_fold):.1f})')
ax.hist(PR_noJ, bins=40, alpha=0.5, color='red', label=f'No $E_J$ (mean={np.mean(PR_noJ):.1f})')
ax.set_xlabel('Participation Ratio', fontsize=12)
ax.set_ylabel('Count', fontsize=12)
ax.set_title('Eigenstate Delocalization')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plot_path = os.path.join(data_dir, 's59_therm_order.png')
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
log(f"Plot saved to {plot_path}")

# Also write final log update
with open(log_path, 'w') as f:
    f.write('\n'.join(log_lines))

print("SCRIPT COMPLETE")
print(f"Verdict: {verdict}")
print(f"N_c = {N_c_fit if fit_success else 'N/A'}")
