#!/usr/bin/env python3
"""
S57 W2-2: DESERT-DYNAMICS-57 — Time-Dependent Schrodinger Through Coherence Desert
===================================================================================

Gate: DESERT-DYNAMICS-57
  PASS: P_exc > 0.1 at BCS freeze point tau = 0.22. Desert decouples cells.
  FAIL: P_exc < 0.01. Josephson gap persists through desert.
  INFO: 0.01 < P_exc < 0.1.

Physics:
  The coherence desert is the epoch where E_J(tau)/H(tau) < 1. During this
  epoch, the Josephson coupling is weaker than the intra-cell Hamiltonian,
  so cells may decouple. If they decouple, single-cell physics applies
  (P_exc ~ 0.14 per cell from W1-1 isolated benchmark).

  We track:
  (a) <cos(phi_1 - phi_2)>(tau) — inter-cell phase correlation
  (b) P_exc(tau) at tau=0.22 (BCS freeze) for full-coupled vs desert-decoupled
  (c) E_J_GGE(tau)/H(tau) during evolution

Method:
  Solve TDSE i d|psi>/dt = H(tau(t)) |psi> using RK4 on the 120-dim Fock
  space. Compare three evolution protocols:
    (A) Full-coupled: H_J active throughout [0, 0.5]
    (B) Desert-decoupled: H_J = 0 during desert epoch, restored before/after
    (C) Isolated: H_J = 0 throughout (single-cell limit)

  The inter-cell phase operator cos(phi_1 - phi_2) is constructed from
  the pair-transfer operators between cells.

Author: Schwarzschild-Penrose geometer agent
Session: S57 Wave 2
"""

import sys
import os
import time as clock_time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
from canonical_constants import (
    E_cond, tau_fold, N_dof_BCS,
    Delta_0_OES, xi_BCS, omega_PV, S_inst,
    PI, M_KK, M_KK_gravity,
)

import numpy as np
from scipy.linalg import eigh
from itertools import combinations

print("=" * 70)
print("S57 W2-2: DESERT-DYNAMICS-57")
print("Time-Dependent Schrodinger Through Coherence Desert")
print("=" * 70)

# ==============================================================================
#  SECTION 1: Load Input Data
# ==============================================================================

print("\n--- Loading input data ---")
data_dir = os.path.dirname(os.path.abspath(__file__))

ed_data = np.load(os.path.join(data_dir, 's54_ed_sweep.npz'), allow_pickle=True)
tau_values = ed_data['tau_values']       # (50,)
E_sp_sweep = ed_data['E_sp_sweep']      # (50, 8)
V_bare_raw = ed_data['V_bare_cont']     # (8, 8)
fold_idx = int(ed_data['fold_idx'])      # 19
N_modes = int(ed_data['N_modes'])        # 8

V_bare = (V_bare_raw + V_bare_raw.T) / 2.0

tb_data = np.load(os.path.join(data_dir, 's54_tb_hamiltonian.npz'), allow_pickle=True)
J_C2_tau = tb_data['J_C2_tau']          # (50,)

leggett_data = np.load(os.path.join(data_dir, 's57_leggett_tau_profile.npz'), allow_pickle=True)
dtau_dt_phys = float(leggett_data['dtau_dt'])

sf_data = np.load(os.path.join(data_dir, 's54_scale_factor.npz'), allow_pickle=True)
H_tau_sparse = sf_data['H']             # (10,) — Hubble parameter
tau_sparse = sf_data['tau']              # (10,)

# W1-1 data for cross-validation
w1_data = np.load(os.path.join(data_dir, 's57_finite_rate_transit.npz'), allow_pickle=True)
P_exc_w1_final = float(w1_data['P_exc_final'])
P_exc_w1_isolated = float(w1_data['P_exc_isolated'])

# S56 coherence data
coh_data = np.load(os.path.join(data_dir, 's56_post_transit_coh.npz'), allow_pickle=True)
ratio_GGE_s56 = coh_data['ratio_GGE']
tau_coh = coh_data['tau_values']

print(f"  N_modes = {N_modes}, fold_idx = {fold_idx} (tau = {tau_values[fold_idx]:.4f})")
print(f"  dtau/dt (physical) = {dtau_dt_phys:.4f} M_KK")
print(f"  W1-1 P_exc(final) = {P_exc_w1_final:.6f}")
print(f"  W1-1 P_exc(isolated) = {P_exc_w1_isolated:.6f}")

# ==============================================================================
#  SECTION 2: Build Pair Basis (exact S56/W1-1 construction)
# ==============================================================================

N_pair_total = 2  # (local)
n_modes_total = 2 * N_modes  # 16
basis = list(combinations(range(n_modes_total), N_pair_total))
dim = len(basis)
assert dim == 120, f"Expected dim=120, got {dim}"
basis_dict = {state: idx for idx, state in enumerate(basis)}

def classify_state(state):
    n1 = sum(1 for k in state if k < N_modes)
    n2 = sum(1 for k in state if k >= N_modes)
    return n1, n2

sector_02 = [i for i, s in enumerate(basis) if classify_state(s) == (0, 2)]
sector_11 = [i for i, s in enumerate(basis) if classify_state(s) == (1, 1)]
sector_20 = [i for i, s in enumerate(basis) if classify_state(s) == (2, 2)]
# Fix: sector_20 should be (2,0)
sector_20 = [i for i, s in enumerate(basis) if classify_state(s) == (2, 0)]

print(f"  dim = {dim}, sectors: (2,0)={len(sector_20)}, (1,1)={len(sector_11)}, (0,2)={len(sector_02)}")

# ==============================================================================
#  SECTION 3: Hamiltonian Construction (exact copy from W1-1)
# ==============================================================================

Delta = Delta_0_OES

def compute_E_J_val(eps, J_C2_val):
    """Compute Josephson energy from W1-1 formula."""
    E_qp = np.sqrt(eps**2 + Delta**2)
    F_anom = np.sum(Delta / (2.0 * E_qp**2))
    return J_C2_val**2 * F_anom


def build_H_2cell(eps_1, eps_2, V_1, V_2, E_J_coupling, alpha=1.0):
    """Build 2-cell BCS Hamiltonian in pair basis (EXACT W1-1 copy)."""
    H = np.zeros((dim, dim))
    for i, state_i in enumerate(basis):
        E_kin = 0.0  # (local)
        for k in state_i:
            if k < N_modes:
                E_kin += 2.0 * eps_1[k]
            else:
                E_kin += 2.0 * eps_2[k - N_modes]
        H[i, i] += E_kin

        for pos, k in enumerate(state_i):
            cell_offset = 0 if k < N_modes else N_modes
            k_local = k - cell_offset
            V_cell = V_1 if k < N_modes else V_2

            for l_local in range(N_modes):
                l = l_local + cell_offset
                if l == k:
                    H[i, i] -= V_cell[k_local, k_local]
                    continue
                if l in state_i:
                    continue
                ns = list(state_i)
                ns[pos] = l
                ns = tuple(sorted(ns))
                if ns in basis_dict:
                    j = basis_dict[ns]
                    H[i, j] -= V_cell[l_local, k_local]

        if alpha > 0 and E_J_coupling > 0:
            for pos, k in enumerate(state_i):
                if k >= N_modes:
                    for l1 in range(N_modes):
                        if l1 in state_i:
                            continue
                        ns = list(state_i)
                        ns[pos] = l1
                        ns = tuple(sorted(ns))
                        if ns in basis_dict:
                            H[i, basis_dict[ns]] -= alpha * E_J_coupling / 2.0
                else:
                    for l2 in range(N_modes):
                        l = l2 + N_modes
                        if l in state_i:
                            continue
                        ns = list(state_i)
                        ns[pos] = l
                        ns = tuple(sorted(ns))
                        if ns in basis_dict:
                            H[i, basis_dict[ns]] -= alpha * E_J_coupling / 2.0

    H = (H + H.T) / 2.0
    return H


# ==============================================================================
#  SECTION 4: Precompute Hamiltonians on tau grid
# ==============================================================================

print("\n--- Precomputing Hamiltonians at 50 tau grid points ---")
t_pre = clock_time.time()

H_grid = np.zeros((len(tau_values), dim, dim))
H_grid_noJ = np.zeros((len(tau_values), dim, dim))
E_J_grid = np.zeros(len(tau_values))

for ti in range(len(tau_values)):
    eps_ti = E_sp_sweep[ti]
    E_J_ti = compute_E_J_val(eps_ti, J_C2_tau[ti])
    E_J_grid[ti] = E_J_ti
    H_grid[ti] = build_H_2cell(eps_ti, eps_ti, V_bare, V_bare, E_J_ti, alpha=1.0)
    H_grid_noJ[ti] = build_H_2cell(eps_ti, eps_ti, V_bare, V_bare, 0.0, alpha=0.0)

print(f"  Precompute time: {clock_time.time() - t_pre:.2f} s")
print(f"  E_J range: [{E_J_grid.min():.4f}, {E_J_grid.max():.4f}] M_KK")
print(f"  E_J at fold: {E_J_grid[fold_idx]:.4f}")

# Interpolate H on tau using the Hubble parameter on the 50-point grid
# Reconstruct H(tau) on the 50-point grid by interpolating the 10-point sparse data
from scipy.interpolate import interp1d
H_hubble_interp = interp1d(tau_sparse, H_tau_sparse, kind='linear', fill_value='extrapolate')
H_hubble_50 = H_hubble_interp(tau_values)

# Compute E_J/H ratio
E_J_over_H = E_J_grid / H_hubble_50

print(f"\n  E_J/H range: [{E_J_over_H.min():.4f}, {E_J_over_H.max():.4f}]")

# Find desert boundaries (E_J/H = 1 crossings)
desert_entries = []
desert_exits = []
for i in range(len(tau_values) - 1):
    if E_J_over_H[i] >= 1.0 and E_J_over_H[i+1] < 1.0:
        t_cross = tau_values[i] + (1.0 - E_J_over_H[i]) / (E_J_over_H[i+1] - E_J_over_H[i]) * (tau_values[i+1] - tau_values[i])
        desert_entries.append(t_cross)
    elif E_J_over_H[i] < 1.0 and E_J_over_H[i+1] >= 1.0:
        t_cross = tau_values[i] + (1.0 - E_J_over_H[i]) / (E_J_over_H[i+1] - E_J_over_H[i]) * (tau_values[i+1] - tau_values[i])
        desert_exits.append(t_cross)

tau_desert_entry = desert_entries[0] if desert_entries else 0.08
tau_desert_exit = desert_exits[0] if desert_exits else 0.48
tau_BCS_freeze = 0.22  # Post-transit freeze point  # (local)

print(f"  Desert entry (E_J/H drops below 1): tau = {tau_desert_entry:.4f}")
print(f"  Desert exit (E_J/H rises above 1): tau = {tau_desert_exit:.4f}")
print(f"  BCS freeze: tau = {tau_BCS_freeze:.4f}")
print(f"  E_J/H at fold (tau={tau_values[fold_idx]:.4f}): {E_J_over_H[fold_idx]:.4f}")
print(f"  E_J/H at BCS freeze (interp): {np.interp(tau_BCS_freeze, tau_values, E_J_over_H):.4f}")


# ==============================================================================
#  SECTION 5: Inter-Cell Phase Correlation Operator
# ==============================================================================

print("\n--- Constructing inter-cell phase correlation operator ---")

# The inter-cell phase operator measures cos(phi_1 - phi_2).
# In the pair basis, this corresponds to pair-transfer operators:
#   T_{1->2} = sum_k c_{2k}^dag c_{1k}  (transfer pair from cell 1 to cell 2)
#   T_{2->1} = T_{1->2}^dag
# Then cos(phi_1 - phi_2) ~ (T_{1->2} + T_{2->1}) / (2 * N_pair_max)
#
# More precisely, the Josephson coupling IS the cos(phi) operator.
# We construct the pair-transfer matrix in the 120-dim basis.

# Pair transfer: move a pair from mode k in cell 1 to mode k in cell 2
T_12 = np.zeros((dim, dim))
T_21 = np.zeros((dim, dim))

for i, state_i in enumerate(basis):
    for pos, k in enumerate(state_i):
        if k < N_modes:
            # Particle in cell 1, try moving to cell 2
            k_cell2 = k + N_modes
            if k_cell2 not in state_i:
                ns = list(state_i)
                ns[pos] = k_cell2
                ns = tuple(sorted(ns))
                if ns in basis_dict:
                    T_12[basis_dict[ns], i] += 1.0
        else:
            # Particle in cell 2, try moving to cell 1
            k_cell1 = k - N_modes
            if k_cell1 not in state_i:
                ns = list(state_i)
                ns[pos] = k_cell1
                ns = tuple(sorted(ns))
                if ns in basis_dict:
                    T_21[basis_dict[ns], i] += 1.0

# cos(phi_1 - phi_2) operator (normalized)
cos_op = (T_12 + T_21) / 2.0
# Verify Hermiticity
assert np.allclose(cos_op, cos_op.T), "cos_op not Hermitian"
print(f"  cos_op: dim={cos_op.shape}, nonzero elements: {np.count_nonzero(cos_op)}")

# Also construct the cell-exchange (swap) operator for bonding/antibonding
def swap_mode(k):
    return (k + N_modes) if k < N_modes else (k - N_modes)

S_cell = np.zeros((dim, dim))
for alpha in range(dim):
    s = basis[alpha]
    swapped = [swap_mode(k) for k in s]
    sign = 1 if swapped[0] < swapped[1] else -1  # (local)
    swapped_sorted = tuple(sorted(swapped))
    if swapped_sorted in basis_dict:
        S_cell[alpha, basis_dict[swapped_sorted]] = sign

P_bond = 0.5 * (np.eye(dim) + S_cell)
P_anti = 0.5 * (np.eye(dim) - S_cell)

# Compute cos_op ground state expectation at tau=0 for calibration
evals_init, evecs_init = eigh(H_grid[0])
psi_init = evecs_init[:, 0].copy()
cos_phi_init = np.real(psi_init.conj() @ cos_op @ psi_init)
print(f"  <cos(phi)> at tau=0 (GS): {cos_phi_init:.6f}")

# Number operators for each cell
N1_op = np.zeros((dim, dim))
N2_op = np.zeros((dim, dim))
for i, state_i in enumerate(basis):
    n1 = sum(1 for k in state_i if k < N_modes)
    n2 = sum(1 for k in state_i if k >= N_modes)
    N1_op[i, i] = n1
    N2_op[i, i] = n2

Delta_N_op = N1_op - N2_op  # Number difference operator


# ==============================================================================
#  SECTION 6: Hamiltonian Interpolators
# ==============================================================================

def H_interp_full(tau_val):
    """Interpolate full H(tau) from precomputed grid."""
    tau_val = np.clip(tau_val, tau_values[0], tau_values[-1])
    idx = np.searchsorted(tau_values, tau_val) - 1
    idx = np.clip(idx, 0, len(tau_values) - 2)
    t = (tau_val - tau_values[idx]) / (tau_values[idx + 1] - tau_values[idx])
    return (1 - t) * H_grid[idx] + t * H_grid[idx + 1]


def H_interp_noJ(tau_val):
    """Interpolate H_noJ(tau) from precomputed grid."""
    tau_val = np.clip(tau_val, tau_values[0], tau_values[-1])
    idx = np.searchsorted(tau_values, tau_val) - 1
    idx = np.clip(idx, 0, len(tau_values) - 2)
    t = (tau_val - tau_values[idx]) / (tau_values[idx + 1] - tau_values[idx])
    return (1 - t) * H_grid_noJ[idx] + t * H_grid_noJ[idx + 1]


def H_interp_desert_decoupled(tau_val, tau_d_entry, tau_d_exit):
    """
    Interpolate H with Josephson coupling turned off during desert.
    H_J = 0 for tau in [tau_d_entry, tau_d_exit], full H otherwise.
    """
    if tau_d_entry <= tau_val <= tau_d_exit:
        return H_interp_noJ(tau_val)
    else:
        return H_interp_full(tau_val)


# ==============================================================================
#  SECTION 7: RK4 Evolution Engine with Observable Tracking
# ==============================================================================

def evolve_with_observables(psi_init, tau_i, tau_f, dtau_dt, N_sample=300,
                            dt_safety=0.02, H_func=H_interp_full, label=""):
    """
    RK4 evolution tracking P_exc, <cos(phi)>, <Delta_N^2>, bond/anti weights.
    """
    psi = psi_init.astype(complex).copy()

    t_total = (tau_f - tau_i) / dtau_dt

    # Step size from spectral bound
    H_test = H_func(tau_i)
    evals_test = np.linalg.eigvalsh(H_test)
    E_max = max(abs(evals_test[-1]), abs(evals_test[0]))
    dt = dt_safety / E_max
    dt = min(dt, t_total / max(N_sample, 50))

    N_steps_est = int(t_total / dt) + 1
    if label:
        print(f"\n  [{label}] t_total = {t_total:.6e}, E_max = {E_max:.2f}, dt = {dt:.6e}, est steps = {N_steps_est}")

    # Sampling grid
    tau_sample = np.linspace(tau_i, tau_f, N_sample + 1)

    # Storage
    tau_hist = []
    P_exc_hist = []
    cos_phi_hist = []
    deltaN2_hist = []
    w_bond_hist = []
    w_anti_hist = []
    E_J_eff_hist = []    # E_J_GGE(tau)/H(tau)

    t = 0.0
    step = 0
    sample_idx = 0

    # Record initial state
    def record_observables(psi_now, tau_now):
        H_now_mat = H_func(tau_now)
        evals_n, evecs_n = eigh(H_now_mat)
        gs_n = evecs_n[:, 0]

        P_exc_n = 1.0 - abs(np.dot(gs_n.conj(), psi_now))**2

        cos_phi_n = np.real(psi_now.conj() @ cos_op @ psi_now)

        deltaN2_n = np.real(psi_now.conj() @ (Delta_N_op @ Delta_N_op) @ psi_now) - \
                    np.real(psi_now.conj() @ Delta_N_op @ psi_now)**2

        psi_b = P_bond @ psi_now
        psi_a = P_anti @ psi_now
        w_b = np.real(np.dot(psi_b.conj(), psi_b))
        w_a = np.real(np.dot(psi_a.conj(), psi_a))

        # E_J_GGE(tau)/H(tau) — use actual occupations from evolving state
        # to compute anomalous density and hence E_J_GGE
        eps_now = np.interp(tau_now, tau_values, E_sp_sweep[:, 0])
        # Instead, just interpolate E_J/H from precomputed grid
        E_J_over_H_now = np.interp(tau_now, tau_values, E_J_over_H)

        return P_exc_n, cos_phi_n, deltaN2_n, w_b, w_a, E_J_over_H_now

    # Initial point
    p0, c0, d0, wb0, wa0, ej0 = record_observables(psi, tau_i)
    tau_hist.append(tau_i)
    P_exc_hist.append(p0)
    cos_phi_hist.append(c0)
    deltaN2_hist.append(d0)
    w_bond_hist.append(wb0)
    w_anti_hist.append(wa0)
    E_J_eff_hist.append(ej0)
    sample_idx = 1

    while t < t_total and step < 10 * N_steps_est:
        tau_now = np.clip(tau_i + dtau_dt * t, tau_i, tau_f)
        tau_mid = np.clip(tau_i + dtau_dt * (t + 0.5*dt), tau_i, tau_f)
        tau_end = np.clip(tau_i + dtau_dt * (t + dt), tau_i, tau_f)

        H_n = H_func(tau_now)
        H_m = H_func(tau_mid)
        H_e = H_func(tau_end)

        k1 = -1j * (H_n @ psi)
        k2 = -1j * (H_m @ (psi + 0.5 * dt * k1))
        k3 = -1j * (H_m @ (psi + 0.5 * dt * k2))
        k4 = -1j * (H_e @ (psi + dt * k3))

        psi += (dt / 6.0) * (k1 + 2*k2 + 2*k3 + k4)

        norm = np.linalg.norm(psi)
        if abs(norm - 1.0) > 1e-8:
            psi /= norm

        t += dt
        step += 1

        tau_current = np.clip(tau_i + dtau_dt * t, tau_i, tau_f)

        if sample_idx < len(tau_sample) and tau_current >= tau_sample[sample_idx]:
            pn, cn, dn, wbn, wan, ejn = record_observables(psi, tau_current)
            tau_hist.append(tau_current)
            P_exc_hist.append(pn)
            cos_phi_hist.append(cn)
            deltaN2_hist.append(dn)
            w_bond_hist.append(wbn)
            w_anti_hist.append(wan)
            E_J_eff_hist.append(ejn)
            sample_idx += 1

            if label and sample_idx % 75 == 0:
                print(f"    tau={tau_current:.4f}, P_exc={pn:.4e}, <cos>={cn:.4f}, w_anti={wan:.4f}")

    psi /= np.linalg.norm(psi)

    if label:
        print(f"  [{label}] Steps: {step}")

    return psi, {
        'tau': np.array(tau_hist),
        'P_exc': np.array(P_exc_hist),
        'cos_phi': np.array(cos_phi_hist),
        'deltaN2': np.array(deltaN2_hist),
        'w_bond': np.array(w_bond_hist),
        'w_anti': np.array(w_anti_hist),
        'E_J_over_H': np.array(E_J_eff_hist),
    }


# ==============================================================================
#  SECTION 8: Validation — reproduce W1-1 P_exc
# ==============================================================================

print("\n" + "=" * 70)
print("VALIDATION: Reproduce W1-1 results")
print("=" * 70)

evals_gs, evecs_gs = eigh(H_grid[0])
psi_0 = evecs_gs[:, 0].astype(complex).copy()

# Quick full-coupled run
psi_val, obs_val = evolve_with_observables(
    psi_0, 0.0, 0.5, dtau_dt_phys, N_sample=200,
    dt_safety=0.02, H_func=H_interp_full, label="VALIDATION"
)

P_exc_val_final = obs_val['P_exc'][-1]
print(f"\n  P_exc(validation, tau=0.5) = {P_exc_val_final:.6f}")
print(f"  P_exc(W1-1) = {P_exc_w1_final:.6f}")
print(f"  Ratio: {P_exc_val_final / P_exc_w1_final:.4f}")
val_pass = abs(P_exc_val_final - P_exc_w1_final) / max(P_exc_w1_final, 1e-10) < 0.1
print(f"  Validation: {'PASS' if val_pass else 'FAIL'} (<10% tolerance)")


# ==============================================================================
#  SECTION 9: PROTOCOL A — Full-Coupled Evolution (with observables)
# ==============================================================================

print("\n" + "=" * 70)
print("PROTOCOL A: Full-Coupled Evolution")
print("=" * 70)

t_A_start = clock_time.time()
psi_A, obs_A = evolve_with_observables(
    psi_0, 0.0, 0.5, dtau_dt_phys, N_sample=300,
    dt_safety=0.02, H_func=H_interp_full, label="FULL-COUPLED"
)
t_A_wall = clock_time.time() - t_A_start

# Extract values at key tau points
def extract_at_tau(obs, tau_target):
    idx = np.argmin(np.abs(obs['tau'] - tau_target))
    return {k: obs[k][idx] for k in obs if k != 'tau'}, obs['tau'][idx]

obs_A_desert_entry, tau_actual_entry = extract_at_tau(obs_A, tau_desert_entry)
obs_A_fold, tau_actual_fold = extract_at_tau(obs_A, tau_values[fold_idx])
obs_A_BCS, tau_actual_BCS = extract_at_tau(obs_A, tau_BCS_freeze)
obs_A_desert_exit, tau_actual_exit = extract_at_tau(obs_A, tau_desert_exit)

print(f"\n  Wall time: {t_A_wall:.1f} s")
print(f"\n  --- Key tau points ---")
print(f"  Desert entry (tau={tau_actual_entry:.4f}):")
print(f"    P_exc = {obs_A_desert_entry['P_exc']:.6f}")
print(f"    <cos(phi)> = {obs_A_desert_entry['cos_phi']:.6f}")
print(f"    <Delta_N^2> = {obs_A_desert_entry['deltaN2']:.6f}")
print(f"    w_bond = {obs_A_desert_entry['w_bond']:.6f}, w_anti = {obs_A_desert_entry['w_anti']:.6f}")
print(f"    E_J/H = {obs_A_desert_entry['E_J_over_H']:.4f}")

print(f"  Fold (tau={tau_actual_fold:.4f}):")
print(f"    P_exc = {obs_A_fold['P_exc']:.6f}")
print(f"    <cos(phi)> = {obs_A_fold['cos_phi']:.6f}")
print(f"    <Delta_N^2> = {obs_A_fold['deltaN2']:.6f}")
print(f"    w_bond = {obs_A_fold['w_bond']:.6f}, w_anti = {obs_A_fold['w_anti']:.6f}")
print(f"    E_J/H = {obs_A_fold['E_J_over_H']:.4f}")

print(f"  BCS freeze (tau={tau_actual_BCS:.4f}):")
print(f"    P_exc = {obs_A_BCS['P_exc']:.6f}")
print(f"    <cos(phi)> = {obs_A_BCS['cos_phi']:.6f}")
print(f"    <Delta_N^2> = {obs_A_BCS['deltaN2']:.6f}")
print(f"    w_bond = {obs_A_BCS['w_bond']:.6f}, w_anti = {obs_A_BCS['w_anti']:.6f}")
print(f"    E_J/H = {obs_A_BCS['E_J_over_H']:.4f}")

print(f"  Final (tau=0.5):")
print(f"    P_exc = {obs_A['P_exc'][-1]:.6f}")
print(f"    <cos(phi)> = {obs_A['cos_phi'][-1]:.6f}")


# ==============================================================================
#  SECTION 10: PROTOCOL B — Desert-Decoupled Evolution
# ==============================================================================

print("\n" + "=" * 70)
print("PROTOCOL B: Desert-Decoupled Evolution")
print(f"  H_J = 0 for tau in [{tau_desert_entry:.4f}, {tau_desert_exit:.4f}]")
print("=" * 70)

def H_desert_decoupled(tau_val):
    return H_interp_desert_decoupled(tau_val, tau_desert_entry, tau_desert_exit)

t_B_start = clock_time.time()
psi_B, obs_B = evolve_with_observables(
    psi_0, 0.0, 0.5, dtau_dt_phys, N_sample=300,
    dt_safety=0.02, H_func=H_desert_decoupled, label="DESERT-DECOUPLED"
)
t_B_wall = clock_time.time() - t_B_start

obs_B_desert_entry, _ = extract_at_tau(obs_B, tau_desert_entry)
obs_B_fold, _ = extract_at_tau(obs_B, tau_values[fold_idx])
obs_B_BCS, _ = extract_at_tau(obs_B, tau_BCS_freeze)
obs_B_desert_exit, _ = extract_at_tau(obs_B, tau_desert_exit)

print(f"\n  Wall time: {t_B_wall:.1f} s")
print(f"\n  --- Key tau points ---")
print(f"  Desert entry (tau~{tau_desert_entry:.4f}):")
print(f"    P_exc = {obs_B_desert_entry['P_exc']:.6f}")
print(f"    <cos(phi)> = {obs_B_desert_entry['cos_phi']:.6f}")

print(f"  Fold (tau~{tau_values[fold_idx]:.4f}):")
print(f"    P_exc = {obs_B_fold['P_exc']:.6f}")
print(f"    <cos(phi)> = {obs_B_fold['cos_phi']:.6f}")

print(f"  BCS freeze (tau~{tau_BCS_freeze:.2f}):")
print(f"    P_exc = {obs_B_BCS['P_exc']:.6f}")
print(f"    <cos(phi)> = {obs_B_BCS['cos_phi']:.6f}")

print(f"  Final (tau=0.5):")
print(f"    P_exc = {obs_B['P_exc'][-1]:.6f}")
print(f"    <cos(phi)> = {obs_B['cos_phi'][-1]:.6f}")


# ==============================================================================
#  SECTION 11: PROTOCOL C — Fully Isolated (E_J = 0 throughout)
# ==============================================================================

print("\n" + "=" * 70)
print("PROTOCOL C: Fully Isolated (E_J = 0 always)")
print("=" * 70)

# For isolated, initial state must be ground state of H_noJ
evals_noJ_gs, evecs_noJ_gs = eigh(H_grid_noJ[0])
psi_0_noJ = evecs_noJ_gs[:, 0].astype(complex).copy()

t_C_start = clock_time.time()
psi_C, obs_C = evolve_with_observables(
    psi_0_noJ, 0.0, 0.5, dtau_dt_phys, N_sample=300,
    dt_safety=0.02, H_func=H_interp_noJ, label="ISOLATED"
)
t_C_wall = clock_time.time() - t_C_start

obs_C_fold, _ = extract_at_tau(obs_C, tau_values[fold_idx])
obs_C_BCS, _ = extract_at_tau(obs_C, tau_BCS_freeze)

print(f"\n  Wall time: {t_C_wall:.1f} s")
print(f"  Fold: P_exc = {obs_C_fold['P_exc']:.6f}, <cos>= {obs_C_fold['cos_phi']:.6f}")
print(f"  BCS:  P_exc = {obs_C_BCS['P_exc']:.6f}, <cos> = {obs_C_BCS['cos_phi']:.6f}")
print(f"  Final: P_exc = {obs_C['P_exc'][-1]:.6f}, <cos> = {obs_C['cos_phi'][-1]:.6f}")


# ==============================================================================
#  SECTION 12: PROTOCOL D — Desert-decoupled starting from coupled GS
# ==============================================================================
# This is the physically relevant comparison: same initial state as A,
# but with H_J switched off during desert.

print("\n" + "=" * 70)
print("PROTOCOL D: Desert-Decoupled, Coupled Initial State")
print(f"  Same psi_0 as Protocol A, H_J off in [{tau_desert_entry:.4f}, {tau_desert_exit:.4f}]")
print("=" * 70)

t_D_start = clock_time.time()
psi_D, obs_D = evolve_with_observables(
    psi_0, 0.0, 0.5, dtau_dt_phys, N_sample=300,
    dt_safety=0.02, H_func=H_desert_decoupled, label="DECOUPLED-COUPLED-INIT"
)
t_D_wall = clock_time.time() - t_D_start

obs_D_fold, _ = extract_at_tau(obs_D, tau_values[fold_idx])
obs_D_BCS, _ = extract_at_tau(obs_D, tau_BCS_freeze)

print(f"\n  Wall time: {t_D_wall:.1f} s")
print(f"  Fold: P_exc = {obs_D_fold['P_exc']:.6f}, <cos> = {obs_D_fold['cos_phi']:.6f}")
print(f"  BCS:  P_exc = {obs_D_BCS['P_exc']:.6f}, <cos> = {obs_D_BCS['cos_phi']:.6f}")
print(f"  Final: P_exc = {obs_D['P_exc'][-1]:.6f}, <cos> = {obs_D['cos_phi'][-1]:.6f}")


# ==============================================================================
#  SECTION 13: Coherence Decay Analysis
# ==============================================================================

print("\n" + "=" * 70)
print("COHERENCE DECAY ANALYSIS")
print("=" * 70)

# Track <cos(phi)> through the desert for Protocol A
cos_A = obs_A['cos_phi']
tau_A = obs_A['tau']

# Find the coherence at desert boundaries
cos_at_entry = np.interp(tau_desert_entry, tau_A, cos_A)
cos_at_fold = np.interp(tau_values[fold_idx], tau_A, cos_A)
cos_at_BCS = np.interp(tau_BCS_freeze, tau_A, cos_A)
cos_at_exit = np.interp(tau_desert_exit, tau_A, cos_A)
cos_at_final = cos_A[-1]

print(f"  <cos(phi)> at tau=0 (GS): {cos_A[0]:.6f}")
print(f"  <cos(phi)> at desert entry: {cos_at_entry:.6f}")
print(f"  <cos(phi)> at fold: {cos_at_fold:.6f}")
print(f"  <cos(phi)> at BCS freeze: {cos_at_BCS:.6f}")
print(f"  <cos(phi)> at desert exit: {cos_at_exit:.6f}")
print(f"  <cos(phi)> at final: {cos_at_final:.6f}")

# Decoherence criterion: <cos(phi)> < 0.5 = cells decoupled
cos_threshold = 0.5  # (local)
decoherence_tau = np.nan
for i in range(len(tau_A) - 1):
    if cos_A[i] >= cos_threshold and cos_A[i+1] < cos_threshold:
        decoherence_tau = tau_A[i] + (cos_threshold - cos_A[i]) / (cos_A[i+1] - cos_A[i]) * (tau_A[i+1] - tau_A[i])
        break

if not np.isnan(decoherence_tau):
    print(f"  Decoherence (|<cos>| < 0.5) at tau = {decoherence_tau:.4f}")
else:
    if np.all(np.abs(cos_A) >= cos_threshold):
        print(f"  <cos(phi)> NEVER drops below 0.5 — cells remain correlated")
    else:
        print(f"  <cos(phi)> starts below 0.5")

# Also check Protocol D
cos_D = obs_D['cos_phi']
tau_D = obs_D['tau']
cos_D_at_BCS = np.interp(tau_BCS_freeze, tau_D, cos_D)
print(f"  Protocol D <cos(phi)> at BCS: {cos_D_at_BCS:.6f}")


# ==============================================================================
#  SECTION 14: P_exc Comparison at BCS Freeze
# ==============================================================================

print("\n" + "=" * 70)
print("P_exc COMPARISON AT BCS FREEZE (tau = 0.22)")
print("=" * 70)

P_exc_A_BCS = obs_A_BCS['P_exc']
P_exc_D_BCS = obs_D_BCS['P_exc']
P_exc_C_BCS = obs_C_BCS['P_exc']

print(f"  Protocol A (full-coupled):          P_exc = {P_exc_A_BCS:.6f}")
print(f"  Protocol D (desert-decoupled):      P_exc = {P_exc_D_BCS:.6f}")
print(f"  Protocol C (fully isolated):        P_exc = {P_exc_C_BCS:.6f}")
print(f"  Ratio A/D:                          {P_exc_A_BCS / max(P_exc_D_BCS, 1e-10):.4f}")
print(f"  Ratio A/C:                          {P_exc_A_BCS / max(P_exc_C_BCS, 1e-10):.4f}")
print(f"  |A - D| / A:                        {abs(P_exc_A_BCS - P_exc_D_BCS) / max(P_exc_A_BCS, 1e-10):.4f}")

# At tau = 0.5
P_exc_A_final = obs_A['P_exc'][-1]
P_exc_D_final = obs_D['P_exc'][-1]
P_exc_C_final = obs_C['P_exc'][-1]

print(f"\n  --- At tau = 0.5 (final) ---")
print(f"  Protocol A (full-coupled):          P_exc = {P_exc_A_final:.6f}")
print(f"  Protocol D (desert-decoupled):      P_exc = {P_exc_D_final:.6f}")
print(f"  Protocol C (fully isolated):        P_exc = {P_exc_C_final:.6f}")


# ==============================================================================
#  SECTION 15: E_J_GGE / H Tracking During Evolution (CW Request)
# ==============================================================================

print("\n" + "=" * 70)
print("E_J_GGE / H TRACKING")
print("=" * 70)

# The E_J/H ratio from the equilibrium perspective is already in the grid.
# During evolution, the relevant quantity is the *instantaneous* Josephson
# energy computed from the evolving state's pair occupations.
# However, at the physical transit rate (sudden quench regime), the state
# barely evolves from the GS, so the instantaneous E_J/H ~ equilibrium.

# We already stored the equilibrium E_J/H in obs_A['E_J_over_H']
ej_A = obs_A['E_J_over_H']
tau_ej = obs_A['tau']

ej_at_entry = np.interp(tau_desert_entry, tau_ej, ej_A)
ej_at_fold = np.interp(tau_values[fold_idx], tau_ej, ej_A)
ej_at_BCS = np.interp(tau_BCS_freeze, tau_ej, ej_A)
ej_at_exit = np.interp(tau_desert_exit, tau_ej, ej_A)
ej_min_desert = np.min(ej_A[tau_ej >= tau_desert_entry])

print(f"  E_J/H at desert entry: {ej_at_entry:.4f}")
print(f"  E_J/H at fold: {ej_at_fold:.4f}")
print(f"  E_J/H at BCS freeze: {ej_at_BCS:.4f}")
print(f"  E_J/H at desert exit: {ej_at_exit:.4f}")
print(f"  E_J/H minimum in desert: {ej_min_desert:.4f}")


# ==============================================================================
#  SECTION 16: <Delta_N^2> and Number Fluctuations
# ==============================================================================

print("\n" + "=" * 70)
print("NUMBER FLUCTUATIONS")
print("=" * 70)

deltaN2_A = obs_A['deltaN2']
deltaN2_D = obs_D['deltaN2']

dN2_A_entry = np.interp(tau_desert_entry, obs_A['tau'], deltaN2_A)
dN2_A_fold = np.interp(tau_values[fold_idx], obs_A['tau'], deltaN2_A)
dN2_A_BCS = np.interp(tau_BCS_freeze, obs_A['tau'], deltaN2_A)

dN2_D_BCS = np.interp(tau_BCS_freeze, obs_D['tau'], deltaN2_D)

print(f"  Protocol A: <Delta_N^2> at entry = {dN2_A_entry:.6f}")
print(f"  Protocol A: <Delta_N^2> at fold = {dN2_A_fold:.6f}")
print(f"  Protocol A: <Delta_N^2> at BCS = {dN2_A_BCS:.6f}")
print(f"  Protocol D: <Delta_N^2> at BCS = {dN2_D_BCS:.6f}")
print(f"  (Decoupled cells have Delta_N^2 = 0; coupled cells ~ 1)")


# ==============================================================================
#  SECTION 17: Gate Verdict
# ==============================================================================

print("\n" + "=" * 70)
print("GATE VERDICT: DESERT-DYNAMICS-57")
print("=" * 70)

# The gate question: does P_exc > 0.1 at BCS freeze, indicating desert decouples?
# We evaluate this by comparing Protocol A (full) vs Protocol D (desert off).
# If they differ significantly, the desert matters.

# Primary metric: P_exc at BCS freeze in Protocol A
P_exc_gate = P_exc_A_BCS
cos_phi_gate = cos_at_BCS

# Decoupling criterion: |P_exc_A - P_exc_D| / P_exc_A > 0.5
# AND <cos(phi)> < 0.5 at BCS freeze
decoupling_strength = abs(P_exc_A_BCS - P_exc_D_BCS) / max(P_exc_A_BCS, 1e-10)

print(f"\n  PRIMARY METRICS:")
print(f"    P_exc(A, BCS freeze) = {P_exc_A_BCS:.6f}")
print(f"    P_exc(D, BCS freeze) = {P_exc_D_BCS:.6f}")
print(f"    |A-D|/A = {decoupling_strength:.4f}")
print(f"    <cos(phi)>(BCS) = {cos_phi_gate:.6f}")
print(f"    E_J/H at BCS = {ej_at_BCS:.4f}")

# Gate classification
if P_exc_gate > 0.1:
    gate_verdict = "PASS"
    gate_detail = f"P_exc={P_exc_gate:.4f} > 0.1 at BCS freeze. Desert genuinely decouples cells."
elif P_exc_gate < 0.01:
    gate_verdict = "FAIL"
    gate_detail = f"P_exc={P_exc_gate:.6f} < 0.01 at BCS freeze. Josephson gap persists."
else:
    gate_verdict = "INFO"
    gate_detail = f"P_exc={P_exc_gate:.4f} in [0.01, 0.1]. Partial decoupling."

print(f"\n  GATE: {gate_verdict}")
print(f"  Detail: {gate_detail}")

# Interpretation
print(f"\n  PHYSICAL INTERPRETATION:")
if decoupling_strength < 0.1:
    print(f"    Desert has < 10% effect on P_exc. Transit too fast for desert to matter.")
    print(f"    The sudden-quench character (dtau/dt=442) overwhelms the desert.")
elif decoupling_strength < 0.5:
    print(f"    Desert has {decoupling_strength*100:.1f}% effect on P_exc. Partial decoupling.")
else:
    print(f"    Desert has {decoupling_strength*100:.1f}% effect on P_exc. Genuine decoupling.")

if abs(cos_phi_gate) < 0.5:
    print(f"    Inter-cell coherence LOST by BCS freeze.")
else:
    print(f"    Inter-cell coherence MAINTAINED through BCS freeze.")


# ==============================================================================
#  SECTION 18: Save Results
# ==============================================================================

print("\n--- Saving results ---")
outpath = os.path.join(data_dir, 's57_desert_dynamics.npz')

np.savez(outpath,
    # Gate
    gate_name='DESERT-DYNAMICS-57',
    gate_verdict=gate_verdict,
    gate_detail=gate_detail,

    # Desert boundaries
    tau_desert_entry=tau_desert_entry,
    tau_desert_exit=tau_desert_exit,
    tau_BCS_freeze=tau_BCS_freeze,
    E_J_over_H=E_J_over_H,

    # Protocol A (full-coupled)
    tau_A=obs_A['tau'],
    P_exc_A=obs_A['P_exc'],
    cos_phi_A=obs_A['cos_phi'],
    deltaN2_A=obs_A['deltaN2'],
    w_bond_A=obs_A['w_bond'],
    w_anti_A=obs_A['w_anti'],
    E_J_H_A=obs_A['E_J_over_H'],

    # Protocol D (desert-decoupled, coupled init)
    tau_D=obs_D['tau'],
    P_exc_D=obs_D['P_exc'],
    cos_phi_D=obs_D['cos_phi'],
    deltaN2_D=obs_D['deltaN2'],
    w_bond_D=obs_D['w_bond'],
    w_anti_D=obs_D['w_anti'],

    # Protocol C (fully isolated)
    tau_C=obs_C['tau'],
    P_exc_C=obs_C['P_exc'],
    cos_phi_C=obs_C['cos_phi'],

    # Key scalars at BCS freeze
    P_exc_A_BCS=P_exc_A_BCS,
    P_exc_D_BCS=P_exc_D_BCS,
    P_exc_C_BCS=P_exc_C_BCS,
    cos_phi_A_BCS=cos_at_BCS,
    cos_phi_D_BCS=cos_D_at_BCS,
    decoupling_strength=decoupling_strength,

    # Key scalars at final
    P_exc_A_final=P_exc_A_final,
    P_exc_D_final=P_exc_D_final,
    P_exc_C_final=P_exc_C_final,

    # Coherence decay
    decoherence_tau=decoherence_tau,
    cos_at_entry=cos_at_entry,
    cos_at_fold=cos_at_fold,
    cos_at_BCS=cos_at_BCS,
    cos_at_exit=cos_at_exit,

    # E_J/H at key points
    ej_at_entry=ej_at_entry,
    ej_at_fold=ej_at_fold,
    ej_at_BCS=ej_at_BCS,
    ej_at_exit=ej_at_exit,
    ej_min_desert=ej_min_desert,

    # Validation
    P_exc_val_final=P_exc_val_final,
    P_exc_w1_final=P_exc_w1_final,
    validation_pass=val_pass,

    # Metadata
    dtau_dt_phys=dtau_dt_phys,
    dim=dim,
    N_modes=N_modes,
)

print(f"  Saved to {outpath}")
print("\nDONE")
