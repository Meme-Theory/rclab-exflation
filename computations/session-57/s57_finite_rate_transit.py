#!/usr/bin/env python3
"""
S57 W1-1: FINITE-RATE-TRANSIT-57 — Exact Time Evolution of 2-Cell Fabric
=========================================================================

Gate: FINITE-RATE-TRANSIT-57
  PASS: P_exc(tau_final) > 0.1 at physical transit rate
  FAIL: P_exc(tau_final) < 0.01
  INFO: 0.01 < P_exc < 0.1

Physics:
  2-cell Josephson array. 8 BCS pair levels per cell. N_pair_total = 2.
  Fock space dim = C(16, 2) = 120. Pair basis from S56.

  H(tau) = H_BCS(tau) + E_J(tau) * H_J_struct
  where H_BCS = sum of intra-cell single-particle + pairing terms,
  and H_J_struct is the tau-independent Josephson structure matrix.

Method:
  Precompute H at 50 tau grid points. Interpolate via cubic spline for
  intermediate tau. RK4 time evolution. This avoids rebuilding H from
  scratch at every time step.

Author: Nazarewicz nuclear structure theorist agent
Session: S57 Wave 1
"""

import sys
import os
import time as clock_time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
from canonical_constants import (
    E_cond, tau_fold, N_cells, N_dof_BCS, E_exc_ratio,
    Delta_0_OES, xi_BCS, omega_PV, S_inst, E_B1, E_B2_mean, E_B3_mean,
    PI, M_KK, M_KK_gravity, J_C2,
)

import numpy as np
from scipy.linalg import eigh
from scipy.interpolate import interp1d
from itertools import combinations

print("=" * 70)
print("S57 W1-1: FINITE-RATE-TRANSIT-57")
print("Exact Time Evolution of 2-Cell Josephson Fabric")
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
fold_idx = int(ed_data['fold_idx'])
N_modes = int(ed_data['N_modes'])        # 8

V_bare = (V_bare_raw + V_bare_raw.T) / 2.0

tb_data = np.load(os.path.join(data_dir, 's54_tb_hamiltonian.npz'), allow_pickle=True)
J_C2_tau = tb_data['J_C2_tau']          # (50,)

leggett_data = np.load(os.path.join(data_dir, 's57_leggett_tau_profile.npz'), allow_pickle=True)
E_J_from_leggett = leggett_data['E_J']  # (50,)
dtau_dt_phys = float(leggett_data['dtau_dt'])

sf_data = np.load(os.path.join(data_dir, 's54_scale_factor.npz'), allow_pickle=True)
H_tau_sparse = sf_data['H']
tau_sparse = sf_data['tau']

fabric_data = np.load(os.path.join(data_dir, 's56_gge_fabric.npz'), allow_pickle=True)

print(f"  N_modes = {N_modes}, fold_idx = {fold_idx} (tau = {tau_values[fold_idx]:.4f})")
print(f"  dtau/dt (physical) = {dtau_dt_phys:.4f} M_KK")

# ==============================================================================
#  SECTION 2: Build Pair Basis (exact S56 construction)
# ==============================================================================

N_pair_total = 2  # (local)
n_modes_total = 2 * N_modes  # 16
basis = list(combinations(range(n_modes_total), N_pair_total))
dim = len(basis)
assert dim == 120
basis_dict = {state: idx for idx, state in enumerate(basis)}

# Precompute sector membership
def classify_state(state):
    n1 = sum(1 for k in state if k < N_modes)
    n2 = sum(1 for k in state if k >= N_modes)
    return n1, n2

sector_02 = [i for i, s in enumerate(basis) if classify_state(s) == (0, 2)]
sector_11 = [i for i, s in enumerate(basis) if classify_state(s) == (1, 1)]
sector_20 = [i for i, s in enumerate(basis) if classify_state(s) == (2, 0)]
print(f"  dim = {dim}, sectors: (2,0)={len(sector_20)}, (1,1)={len(sector_11)}, (0,2)={len(sector_02)}")

# ==============================================================================
#  SECTION 3: Hamiltonian Construction
# ==============================================================================

def compute_E_J_val(eps, J_C2_val, Delta=Delta_0_OES):
    """Compute Josephson energy (S56 formula)."""
    E_qp = np.sqrt(eps**2 + Delta**2)
    F_anom = np.sum(Delta / (2.0 * E_qp**2))
    return J_C2_val**2 * F_anom


def build_H_2cell(eps_1, eps_2, V_1, V_2, E_J_coupling, alpha=1.0):
    """Build 2-cell BCS Hamiltonian in pair basis (EXACT S56 copy)."""
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
                new_state = tuple(sorted([state_i[1-pos], l] if pos == 0 else [state_i[0], l]))
                # Proper reconstruction
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
#  SECTION 4: Precompute H on tau grid + interpolation
# ==============================================================================

print("\n--- Precomputing H at 50 tau grid points ---")
t_pre = clock_time.time()

H_grid = np.zeros((len(tau_values), dim, dim))
E_J_grid = np.zeros(len(tau_values))

for ti in range(len(tau_values)):
    eps_ti = E_sp_sweep[ti]
    E_J_ti = compute_E_J_val(eps_ti, J_C2_tau[ti])
    E_J_grid[ti] = E_J_ti
    H_grid[ti] = build_H_2cell(eps_ti, eps_ti, V_bare, V_bare, E_J_ti, alpha=1.0)

print(f"  Precompute time: {clock_time.time() - t_pre:.2f} s")
print(f"  E_J range: [{E_J_grid.min():.4f}, {E_J_grid.max():.4f}] M_KK")
print(f"  E_J at fold: {E_J_grid[fold_idx]:.4f}")

# Also precompute H without Josephson
H_grid_noJ = np.zeros((len(tau_values), dim, dim))
for ti in range(len(tau_values)):
    eps_ti = E_sp_sweep[ti]
    H_grid_noJ[ti] = build_H_2cell(eps_ti, eps_ti, V_bare, V_bare, 0.0, alpha=0.0)


def H_interp_matrix(tau_val):
    """Interpolate H(tau) from the precomputed grid."""
    tau_val = np.clip(tau_val, tau_values[0], tau_values[-1])
    # Find bracketing indices
    idx = np.searchsorted(tau_values, tau_val) - 1
    idx = np.clip(idx, 0, len(tau_values) - 2)
    t = (tau_val - tau_values[idx]) / (tau_values[idx + 1] - tau_values[idx])
    return (1 - t) * H_grid[idx] + t * H_grid[idx + 1]


def H_interp_noJ(tau_val):
    """Interpolate H_noJ(tau)."""
    tau_val = np.clip(tau_val, tau_values[0], tau_values[-1])
    idx = np.searchsorted(tau_values, tau_val) - 1
    idx = np.clip(idx, 0, len(tau_values) - 2)
    t = (tau_val - tau_values[idx]) / (tau_values[idx + 1] - tau_values[idx])
    return (1 - t) * H_grid_noJ[idx] + t * H_grid_noJ[idx + 1]


# ==============================================================================
#  SECTION 5: Validation Against S56
# ==============================================================================

print("\n--- Validating against S56 eigenvalues ---")

# At fold
evals_fold_comp = np.sort(np.linalg.eigvalsh(H_grid[fold_idx]))
evals_fold_s56 = np.sort(fabric_data['evals_fold'])
max_diff_J = np.max(np.abs(evals_fold_comp - evals_fold_s56))
print(f"  H(fold): max |diff| = {max_diff_J:.2e}")

# At fold no J
evals_noJ_comp = np.sort(np.linalg.eigvalsh(H_grid_noJ[fold_idx]))
evals_noJ_s56 = np.sort(fabric_data['evals_fold_noJ'])
max_diff_noJ = np.max(np.abs(evals_noJ_comp - evals_noJ_s56))
print(f"  H(fold, noJ): max |diff| = {max_diff_noJ:.2e}")

# At tau=0
evals_tau0_comp = np.sort(np.linalg.eigvalsh(H_grid[0]))
evals_tau0_s56 = np.sort(fabric_data['evals_tau0'])
max_diff_tau0 = np.max(np.abs(evals_tau0_comp - evals_tau0_s56))
print(f"  H(tau=0): max |diff| = {max_diff_tau0:.2e}")

validation_pass = max_diff_J < 1e-6 and max_diff_noJ < 1e-6 and max_diff_tau0 < 1e-6
print(f"  Validation: {'PASS' if validation_pass else 'FAIL'}")

if not validation_pass:
    print(f"  Max diffs: J={max_diff_J:.2e}, noJ={max_diff_noJ:.2e}, tau0={max_diff_tau0:.2e}")
    # Print first few eigenvalues for debugging
    print(f"  Computed fold evals[:5]: {evals_fold_comp[:5]}")
    print(f"  S56 fold evals[:5]: {evals_fold_s56[:5]}")
    print(f"  Computed noJ evals[:5]: {evals_noJ_comp[:5]}")
    print(f"  S56 noJ evals[:5]: {evals_noJ_s56[:5]}")
    print(f"  Computed tau0 evals[:5]: {evals_tau0_comp[:5]}")
    print(f"  S56 tau0 evals[:5]: {evals_tau0_s56[:5]}")

# ==============================================================================
#  SECTION 6: Helper Functions
# ==============================================================================

def get_ground_state(H):
    """Get ground state energy and vector from H."""
    evals, evecs = eigh(H)
    return evals[0], evecs[:, 0], evals, evecs


def compute_P_exc_from_H(psi, H):
    """Compute P_exc = 1 - |<GS|psi>|^2 using given H."""
    _, gs, _, _ = get_ground_state(H)
    return 1.0 - abs(np.dot(gs.conj(), psi))**2


def compute_nk(psi):
    """Compute pair-level occupations."""
    p = np.abs(psi)**2
    nk = np.zeros(n_modes_total)
    for alpha in range(dim):
        for k in basis[alpha]:
            nk[k] += p[alpha]
    return nk


def compute_S_DE_from_H(psi, H):
    """Compute diagonal entropy."""
    _, _, evals, evecs = get_ground_state(H)
    c_n = np.abs(evecs.T.conj() @ psi)**2
    c_n_pos = c_n[c_n > 1e-30]
    return -np.sum(c_n_pos * np.log(c_n_pos))


# ==============================================================================
#  SECTION 7: Pre-Registered Benchmarks
# ==============================================================================

print("\n" + "=" * 70)
print("BENCHMARKS")
print("=" * 70)

# --- Benchmark 1: Adiabatic limit (dtau/dt -> 0) ---
print("\n--- Benchmark 1: Adiabatic limit ---")

dtau_dt_slow = 0.1  # Slow but not impossibly slow  # (local)
E0_init, psi_init, evals_init, _ = get_ground_state(H_grid[0])

# Estimate time step from spectral gap
gap_init = evals_init[1] - evals_init[0]
E_max_init = max(abs(evals_init[-1]), abs(evals_init[0]))
t_total_slow = 0.5 / dtau_dt_slow  # = 5.0 M_KK^-1
dt_slow = min(0.02 / E_max_init, t_total_slow / 2000)
N_steps_slow = int(t_total_slow / dt_slow) + 1

print(f"  dtau/dt = {dtau_dt_slow}, t_total = {t_total_slow:.2f}, N_steps ~ {N_steps_slow}")
print(f"  Gap = {gap_init:.6f}, E_max = {E_max_init:.4f}, dt = {dt_slow:.6e}")

psi_slow = psi_init.astype(complex).copy()
t_s = 0.0  # (local)
for step in range(N_steps_slow):
    tau_now = min(dtau_dt_slow * t_s, 0.5)
    tau_mid = min(dtau_dt_slow * (t_s + 0.5 * dt_slow), 0.5)
    tau_end = min(dtau_dt_slow * (t_s + dt_slow), 0.5)

    H_now = H_interp_matrix(tau_now)
    H_mid = H_interp_matrix(tau_mid)
    H_end = H_interp_matrix(tau_end)

    k1 = -1j * (H_now @ psi_slow)
    k2 = -1j * (H_mid @ (psi_slow + 0.5 * dt_slow * k1))
    k3 = -1j * (H_mid @ (psi_slow + 0.5 * dt_slow * k2))
    k4 = -1j * (H_end @ (psi_slow + dt_slow * k3))
    psi_slow += (dt_slow / 6.0) * (k1 + 2*k2 + 2*k3 + k4)

    if step % 500 == 0:
        psi_slow /= np.linalg.norm(psi_slow)
    t_s += dt_slow

psi_slow /= np.linalg.norm(psi_slow)
H_final = H_interp_matrix(0.5)
P_exc_adiabatic = compute_P_exc_from_H(psi_slow, H_final)
print(f"  P_exc(adiabatic) = {P_exc_adiabatic:.6e}")
bench1_pass = P_exc_adiabatic < 0.05
print(f"  {'PASS' if bench1_pass else 'MARGINAL — P_exc should -> 0 for slower rates'}")

# --- Benchmark 2: Sudden quench ---
print("\n--- Benchmark 2: Sudden quench ---")

_, _, evals_fold_full, evecs_fold_full = get_ground_state(H_grid[fold_idx])
c_n_fold = evecs_fold_full.T.conj() @ psi_init
p_n_fold = np.abs(c_n_fold)**2
P_exc_quench_fold = 1.0 - p_n_fold[0]

P_exc_s56 = 1.0 - float(fabric_data['p_n'][0])

print(f"  P_exc(quench tau=0 -> fold) = {P_exc_quench_fold:.6e}")
print(f"  S56 P_exc (from p_n): {P_exc_s56:.6e}")
print(f"  Match ratio: {P_exc_quench_fold / P_exc_s56:.4f}")
bench2_pass = abs(P_exc_quench_fold - P_exc_s56) / max(P_exc_s56, 1e-10) < 0.1
print(f"  {'PASS' if bench2_pass else 'FAIL'}")

# Also quench to tau=0.5
_, _, evals_tauf, evecs_tauf = get_ground_state(H_grid[-1])
c_n_tauf = evecs_tauf.T.conj() @ psi_init
P_exc_quench_tauf = 1.0 - np.abs(c_n_tauf[0])**2
print(f"  P_exc(quench tau=0 -> 0.5) = {P_exc_quench_tauf:.6e}")

# --- Benchmark 3: Isolated cells (E_J = 0) ---
print("\n--- Benchmark 3: Isolated cells (E_J=0) ---")

E0_noJ, psi_noJ_init, _, _ = get_ground_state(H_grid_noJ[0])
P_exc_isolated = compute_P_exc_from_H(psi_noJ_init, H_grid_noJ[-1])
print(f"  P_exc(noJ quench tau=0 -> 0.5) = {P_exc_isolated:.6e}")
print(f"  Expected: ~S38 single-cell value")

# --- Benchmark 4: Leggett gap -> 0 ---
print("\n--- Benchmark 4: Leggett gap -> 0 ---")
print(f"  Covered by Benchmark 3: P_exc = {P_exc_isolated:.6e}")

# ==============================================================================
#  SECTION 8: RK4 Evolution Engine (Fast)
# ==============================================================================

def evolve_rk4_fast(psi_init, tau_i, tau_f, dtau_dt, N_sample=200,
                     dt_safety=0.02, H_func=H_interp_matrix, verbose=True):
    """
    Fast RK4 evolution using precomputed interpolated H.
    """
    psi = psi_init.astype(complex).copy()

    t_total = (tau_f - tau_i) / dtau_dt

    # Step size from spectral bound
    H_test = H_func(tau_i)
    evals_test = np.linalg.eigvalsh(H_test)
    E_max = max(abs(evals_test[-1]), abs(evals_test[0]))
    dt = dt_safety / E_max
    dt = min(dt, t_total / max(N_sample, 10))

    N_steps_est = int(t_total / dt) + 1
    if verbose:
        print(f"  t_total = {t_total:.6e}, E_max = {E_max:.2f}, dt = {dt:.6e}, est steps = {N_steps_est}")

    # Sampling
    tau_sample = np.linspace(tau_i, tau_f, N_sample + 1)[1:]  # skip tau_i
    sample_idx = 0

    tau_hist = [tau_i]
    P_exc_hist = [0.0]
    E_exc_hist = [0.0]
    S_DE_hist = [0.0]
    nk_hist = [compute_nk(psi)]

    t = 0.0
    step = 0
    renorm_count = 0

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
            renorm_count += 1

        t += dt
        step += 1

        tau_current = np.clip(tau_i + dtau_dt * t, tau_i, tau_f)

        if sample_idx < N_sample and tau_current >= tau_sample[sample_idx]:
            H_cur = H_func(tau_current)
            E0_cur, gs_cur, evals_cur, evecs_cur = get_ground_state(H_cur)

            P_exc_now = 1.0 - abs(np.dot(gs_cur.conj(), psi))**2
            E_now = np.real(psi.conj() @ H_cur @ psi)
            E_exc_now = E_now - E0_cur

            c_n_cur = np.abs(evecs_cur.T.conj() @ psi)**2
            c_pos = c_n_cur[c_n_cur > 1e-30]
            S_DE_now = -np.sum(c_pos * np.log(c_pos))

            tau_hist.append(tau_current)
            P_exc_hist.append(P_exc_now)
            E_exc_hist.append(E_exc_now)
            S_DE_hist.append(S_DE_now)
            nk_hist.append(compute_nk(psi))

            sample_idx += 1

            if verbose and sample_idx % 50 == 0:
                print(f"    tau={tau_current:.4f}, P_exc={P_exc_now:.4e}, E_exc={E_exc_now:.4e}")

    if verbose:
        print(f"  Steps: {step}, renorms: {renorm_count}")

    return psi, {
        'tau': np.array(tau_hist), 'P_exc': np.array(P_exc_hist),
        'E_exc': np.array(E_exc_hist), 'S_DE': np.array(S_DE_hist),
        'nk': np.array(nk_hist),
    }


# ==============================================================================
#  SECTION 9: Physical Transit
# ==============================================================================

print("\n" + "=" * 70)
print("PHYSICAL TRANSIT (dtau/dt = {:.1f} M_KK)".format(dtau_dt_phys))
print("=" * 70)

print(f"  E_GS(tau=0) = {E0_init:.6f} M_KK")
print(f"  Gap(tau=0) = {gap_init:.6f} M_KK")

t_wall0 = clock_time.time()
psi_phys, obs_phys = evolve_rk4_fast(
    psi_init, 0.0, 0.5, dtau_dt_phys, N_sample=200, dt_safety=0.02
)
t_wall_phys = clock_time.time() - t_wall0

tau_phys = obs_phys['tau']
P_exc_phys = obs_phys['P_exc']
E_exc_phys = obs_phys['E_exc']
S_DE_phys = obs_phys['S_DE']
nk_phys = obs_phys['nk']

print(f"\n  Wall time: {t_wall_phys:.2f} s")
print(f"  Final P_exc = {P_exc_phys[-1]:.6e}")
print(f"  Final E_exc = {E_exc_phys[-1]:.6e} M_KK")
print(f"  Final S_DE = {S_DE_phys[-1]:.6e}")

# P_exc at fold
fold_sample = np.argmin(np.abs(tau_phys - tau_values[fold_idx]))
print(f"  P_exc at fold = {P_exc_phys[fold_sample]:.6e}")

# ==============================================================================
#  SECTION 10: Channel Decomposition
# ==============================================================================

print("\n" + "=" * 70)
print("CHANNEL DECOMPOSITION")
print("=" * 70)

p_final = np.abs(psi_phys)**2
P_cell0 = sum(p_final[i] for i in sector_20)
P_cell1 = sum(p_final[i] for i in sector_02)
P_cross = sum(p_final[i] for i in sector_11)

# Cell-exchange operator
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

P_plus = 0.5 * (np.eye(dim) + S_cell)
P_minus = 0.5 * (np.eye(dim) - S_cell)

psi_bond = P_plus @ psi_phys
psi_anti = P_minus @ psi_phys
w_bond = np.real(np.dot(psi_bond.conj(), psi_bond))
w_anti = np.real(np.dot(psi_anti.conj(), psi_anti))

# Ground state at tau_f
H_f = H_interp_matrix(0.5)
E0_f, gs_f, _, _ = get_ground_state(H_f)
gs_f_bond = P_plus @ gs_f
gs_f_anti = P_minus @ gs_f
w_bond_gs = np.real(np.dot(gs_f_bond.conj(), gs_f_bond))
w_anti_gs = np.real(np.dot(gs_f_anti.conj(), gs_f_anti))
delta_w_anti = w_anti - w_anti_gs

E_total_f = np.real(psi_phys.conj() @ H_f @ psi_phys)
E_exc_f = E_total_f - E0_f

print(f"  P_cell0 (2,0) = {P_cell0:.6f}")
print(f"  P_cell1 (0,2) = {P_cell1:.6f}")
print(f"  P_cross (1,1) = {P_cross:.6f}")
print(f"  w_bonding = {w_bond:.6f}")
print(f"  w_antibonding = {w_anti:.6f}")
print(f"  w_bonding(GS) = {w_bond_gs:.6f}")
print(f"  w_antibonding(GS) = {w_anti_gs:.6f}")
print(f"  delta_w_anti (Leggett) = {delta_w_anti:.6e}")
print(f"  E_total = {E_total_f:.6f}, E_GS = {E0_f:.6f}")
print(f"  E_exc = {E_exc_f:.6e} M_KK")

# Leggett channel: project E_exc onto bonding and antibonding
E_bond = np.real(psi_bond.conj() @ H_f @ psi_bond)
E_anti = np.real(psi_anti.conj() @ H_f @ psi_anti)
E_bond_gs = np.real(gs_f_bond.conj() @ H_f @ gs_f_bond)
E_anti_gs = np.real(gs_f_anti.conj() @ H_f @ gs_f_anti)
E_exc_bond = E_bond - E_bond_gs
E_exc_anti = E_anti - E_anti_gs

# Fractions
f_Leggett = abs(delta_w_anti) / max(abs(P_exc_phys[-1]), 1e-20) if P_exc_phys[-1] > 0 else 0
print(f"\n  Leggett fraction: |delta_w_anti|/P_exc = {f_Leggett:.4f}")

# ==============================================================================
#  SECTION 11: Landau-Zener Comparison
# ==============================================================================

print("\n" + "=" * 70)
print("LANDAU-ZENER COMPARISON")
print("=" * 70)

gamma_LZ = leggett_data['gamma_LZ']
P_LZ_exc = leggett_data['P_LZ_exc']
P_LZ_total = 1.0 - np.prod(1.0 - P_LZ_exc)

print(f"  gamma_LZ range: [{gamma_LZ.min():.2e}, {gamma_LZ.max():.2e}]")
print(f"  P_LZ range: [{P_LZ_exc.min():.6f}, {P_LZ_exc.max():.6f}]")
print(f"  P_LZ_total = {P_LZ_total:.6f}")
print(f"  Full TD P_exc = {P_exc_phys[-1]:.6e}")

# The LZ formula applies to a 2-level crossing. Our 120-dim system has
# many levels, so direct comparison is qualitative.
# Key: LZ predicts nearly complete excitation (P~1) at each crossing.
# The TD result gives the actual multi-level dynamics.

# ==============================================================================
#  SECTION 12: Rate Scan
# ==============================================================================

print("\n" + "=" * 70)
print("RATE SCAN")
print("=" * 70)

# Scan from 0.1 to 100000 M_KK (avoid extremely slow rates that take forever)
rate_values = np.logspace(-1, 5, 30)
rate_values = np.sort(np.unique(np.append(rate_values, [dtau_dt_phys, 1.0, 10.0, 100.0, 1000.0])))

P_exc_scan = []
t_wall_scan = clock_time.time()

print(f"  Scanning {len(rate_values)} rates...")

for i_r, rate in enumerate(rate_values):
    psi_r = psi_init.astype(complex).copy()
    t_total_r = 0.5 / rate

    # Step sizing
    dt_r = 0.02 / E_max_init
    dt_r = min(dt_r, t_total_r / 10)

    t_r = 0.0  # (local)
    step_r = 0
    max_steps = min(int(t_total_r / dt_r) + 100, 500000)

    while t_r < t_total_r and step_r < max_steps:
        tau_n = np.clip(rate * t_r, 0, 0.5)
        tau_m = np.clip(rate * (t_r + 0.5*dt_r), 0, 0.5)
        tau_e = np.clip(rate * (t_r + dt_r), 0, 0.5)

        H_n = H_interp_matrix(tau_n)
        H_m = H_interp_matrix(tau_m)
        H_e = H_interp_matrix(tau_e)

        k1 = -1j * (H_n @ psi_r)
        k2 = -1j * (H_m @ (psi_r + 0.5*dt_r*k1))
        k3 = -1j * (H_m @ (psi_r + 0.5*dt_r*k2))
        k4 = -1j * (H_e @ (psi_r + dt_r*k3))
        psi_r += (dt_r / 6.0) * (k1 + 2*k2 + 2*k3 + k4)

        norm = np.linalg.norm(psi_r)
        if abs(norm - 1.0) > 1e-8:
            psi_r /= norm

        t_r += dt_r
        step_r += 1

    psi_r /= np.linalg.norm(psi_r)
    tau_fin = np.clip(rate * t_r, 0, 0.5)
    H_fin = H_interp_matrix(tau_fin)
    P_exc_r = compute_P_exc_from_H(psi_r, H_fin)
    P_exc_scan.append(P_exc_r)

    if i_r % 6 == 0 or abs(rate - dtau_dt_phys) < 1:
        tag = " <-- PHYSICAL" if abs(rate - dtau_dt_phys) < 1 else ""
        print(f"    rate={rate:10.2f}, P_exc={P_exc_r:.6e}, steps={step_r}{tag}")

P_exc_scan = np.array(P_exc_scan)
t_scan_wall = clock_time.time() - t_wall_scan
print(f"  Rate scan time: {t_scan_wall:.1f} s")

# Find critical rates
def find_crossing_rate(rates_arr, pexc_arr, threshold):
    for i in range(len(pexc_arr) - 1):
        if (pexc_arr[i] < threshold <= pexc_arr[i+1]) or (pexc_arr[i] >= threshold > pexc_arr[i+1]):
            f = (threshold - pexc_arr[i]) / (pexc_arr[i+1] - pexc_arr[i])
            return rates_arr[i] + f * (rates_arr[i+1] - rates_arr[i])
    return np.nan

rate_crit_001 = find_crossing_rate(rate_values, P_exc_scan, 0.01)
rate_crit_01 = find_crossing_rate(rate_values, P_exc_scan, 0.1)

print(f"\n  P_exc at slowest ({rate_values[0]:.2f}): {P_exc_scan[0]:.6e}")
print(f"  P_exc at fastest ({rate_values[-1]:.0f}): {P_exc_scan[-1]:.6e}")
print(f"  P_exc at physical ({dtau_dt_phys:.0f}): {P_exc_scan[np.argmin(np.abs(rate_values-dtau_dt_phys))]:.6e}")

if not np.isnan(rate_crit_001):
    print(f"  Critical rate (P=0.01): {rate_crit_001:.2f} M_KK")
else:
    print(f"  P_exc never crosses 0.01 in scan range")
if not np.isnan(rate_crit_01):
    print(f"  Critical rate (P=0.1): {rate_crit_01:.2f} M_KK")
else:
    print(f"  P_exc never crosses 0.1 in scan range")

# ==============================================================================
#  SECTION 13: Strutinsky Decomposition
# ==============================================================================

print("\n" + "=" * 70)
print("STRUTINSKY DECOMPOSITION")
print("=" * 70)

# Decompose E_GS(tau) into smooth + shell on the 2-cell system
E_GS_grid = np.array([get_ground_state(H_grid[ti])[0] for ti in range(len(tau_values))])

from numpy.polynomial import polynomial as P_poly
coeffs_strut = P_poly.polyfit(tau_values, E_GS_grid, deg=4)
E_smooth_2cell = P_poly.polyval(tau_values, coeffs_strut)
delta_E_shell_2cell = E_GS_grid - E_smooth_2cell

fold_strut = fold_idx
print(f"  E_GS(fold) = {E_GS_grid[fold_strut]:.6f} M_KK")
print(f"  E_smooth(fold) = {E_smooth_2cell[fold_strut]:.6f} M_KK")
print(f"  delta_E_shell(fold) = {delta_E_shell_2cell[fold_strut]:.6e} M_KK")
print(f"  |shell/smooth| at fold = {abs(delta_E_shell_2cell[fold_strut] / E_smooth_2cell[fold_strut]):.4e}")

# Single-cell Strutinsky for comparison
strut_shell_1cell = ed_data['strutinsky_shell']
print(f"  Single-cell shell correction at fold: {strut_shell_1cell[fold_idx]:.6f} M_KK")

# ==============================================================================
#  SECTION 14: CC Contribution
# ==============================================================================

print("\n" + "=" * 70)
print("CC CONTRIBUTION (delta_P_vac)")
print("=" * 70)

delta_P_vac = E_exc_f
P_vac_2cell_s56 = float(fabric_data['P_vac_2cell'])

print(f"  E_exc(final) = {delta_P_vac:.6e} M_KK")
print(f"  P_vac_2cell (S56) = {P_vac_2cell_s56:.6f} M_KK")
print(f"  delta_P_vac / P_vac = {delta_P_vac / P_vac_2cell_s56:.6e}")

# ==============================================================================
#  SECTION 15: Gate Verdict
# ==============================================================================

print("\n" + "=" * 70)
print("GATE VERDICT: FINITE-RATE-TRANSIT-57")
print("=" * 70)

P_exc_final = P_exc_phys[-1]

if P_exc_final > 0.1:
    verdict = "PASS"
elif P_exc_final < 0.01:
    verdict = "FAIL"
else:
    verdict = "INFO"

print(f"\n  P_exc(final, physical rate) = {P_exc_final:.6e}")
print(f"  Gate: {verdict}")
print(f"  Criterion: PASS > 0.1, FAIL < 0.01, INFO between")

print(f"\n  --- Benchmark Summary ---")
print(f"  B1 (adiabatic, rate=0.1): P_exc = {P_exc_adiabatic:.6e} {'OK' if bench1_pass else 'MARGINAL'}")
print(f"  B2 (sudden quench to fold): P_exc = {P_exc_quench_fold:.6e} vs S56 {P_exc_s56:.6e} (ratio {P_exc_quench_fold/P_exc_s56:.3f}) {'PASS' if bench2_pass else 'FAIL'}")
print(f"  B3 (isolated cells): P_exc = {P_exc_isolated:.6e}")
print(f"  B4 (Leggett gap->0): = B3")

# ==============================================================================
#  SECTION 16: Save Results
# ==============================================================================

print("\n--- Saving results ---")
save_path = os.path.join(data_dir, 's57_finite_rate_transit.npz')

np.savez(save_path,
    gate_name='FINITE-RATE-TRANSIT-57',
    gate_verdict=verdict,

    tau_phys=tau_phys,
    P_exc_phys=P_exc_phys,
    E_exc_phys=E_exc_phys,
    S_DE_phys=S_DE_phys,
    nk_phys=nk_phys,
    dtau_dt_phys=dtau_dt_phys,
    P_exc_final=P_exc_final,

    P_exc_adiabatic=P_exc_adiabatic,
    P_exc_quench_fold=P_exc_quench_fold,
    P_exc_quench_tauf=P_exc_quench_tauf,
    P_exc_isolated=P_exc_isolated,
    P_exc_s56_ref=P_exc_s56,
    P_exc_s56_recomputed=P_exc_quench_fold,

    ch_P_cell0=P_cell0,
    ch_P_cell1=P_cell1,
    ch_P_cross=P_cross,
    ch_w_bond=w_bond,
    ch_w_anti=w_anti,
    ch_w_bond_gs=w_bond_gs,
    ch_w_anti_gs=w_anti_gs,
    ch_delta_w_anti=delta_w_anti,
    ch_E_exc=E_exc_f,
    ch_f_Leggett=f_Leggett,
    ch_E_exc_bond=E_exc_bond,
    ch_E_exc_anti=E_exc_anti,

    gamma_LZ=gamma_LZ,
    P_LZ_exc=P_LZ_exc,
    P_LZ_total=P_LZ_total,

    rate_values=rate_values,
    P_exc_scan=P_exc_scan,
    rate_crit_001=rate_crit_001,
    rate_crit_01=rate_crit_01,

    E_GS_grid=E_GS_grid,
    E_smooth_2cell=E_smooth_2cell,
    delta_E_shell_2cell=delta_E_shell_2cell,

    delta_P_vac=delta_P_vac,
    P_vac_2cell_s56=P_vac_2cell_s56,

    max_diff_evals_J=max_diff_J,
    max_diff_evals_noJ=max_diff_noJ,
    max_diff_evals_tau0=max_diff_tau0,
    validation_pass=validation_pass,

    dim=dim, N_modes=N_modes, N_pair_total=N_pair_total,
    n_modes_total=n_modes_total,
    tau_fold_actual=tau_values[fold_idx], fold_idx=fold_idx,
)
print(f"  Saved: {save_path}")

# ==============================================================================
#  SECTION 17: Plot
# ==============================================================================

print("\n--- Generating plot ---")

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 3, figsize=(18, 10))

# Panel 1: P_exc vs tau
ax = axes[0, 0]
mask = P_exc_phys > 0
if np.any(mask):
    ax.semilogy(tau_phys[mask], P_exc_phys[mask], 'b-', lw=1.5)
ax.axvline(tau_values[fold_idx], color='r', ls='--', alpha=0.5, label='fold')
ax.set_xlabel('tau')
ax.set_ylabel('P_exc')
ax.set_title(f'P_exc vs tau\nP_exc(final) = {P_exc_final:.2e}')
ax.legend()
ax.grid(True, alpha=0.3)

# Panel 2: E_exc vs tau
ax = axes[0, 1]
ax.plot(tau_phys, E_exc_phys, 'r-', lw=1.5)
ax.axvline(tau_values[fold_idx], color='r', ls='--', alpha=0.5)
ax.set_xlabel('tau')
ax.set_ylabel('E_exc (M_KK)')
ax.set_title('Excitation energy')
ax.grid(True, alpha=0.3)

# Panel 3: S_DE vs tau
ax = axes[0, 2]
ax.plot(tau_phys, S_DE_phys, 'g-', lw=1.5)
ax.axvline(tau_values[fold_idx], color='r', ls='--', alpha=0.5)
ax.set_xlabel('tau')
ax.set_ylabel('S_DE')
ax.set_title('Diagonal entropy')
ax.grid(True, alpha=0.3)

# Panel 4: Rate scan
ax = axes[1, 0]
ax.loglog(rate_values, np.maximum(P_exc_scan, 1e-20), 'ko-', ms=3)
ax.axvline(dtau_dt_phys, color='r', ls='--', lw=2, label=f'physical ({dtau_dt_phys:.0f})')
ax.axhline(0.1, color='g', ls=':', alpha=0.5, label='PASS')
ax.axhline(0.01, color='orange', ls=':', alpha=0.5, label='FAIL')
ax.set_xlabel('dtau/dt (M_KK)')
ax.set_ylabel('P_exc(final)')
ax.set_title('Rate scan')
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)

# Panel 5: Channel decomposition
ax = axes[1, 1]
labels = ['Bond', 'Anti', '(2,0)', '(0,2)', '(1,1)']
vals = [w_bond, w_anti, P_cell0, P_cell1, P_cross]
gs_v = [w_bond_gs, w_anti_gs, 0, 0, 0]
x = np.arange(len(labels))
w = 0.35  # (local)
ax.bar(x - w/2, vals, w, label='Final', color='steelblue')
ax.bar(x[:2] + w/2, gs_v[:2], w, label='GS', color='salmon')
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=15)
ax.set_ylabel('Weight')
ax.set_title('Channel decomposition')
ax.legend()
ax.grid(True, alpha=0.3)

# Panel 6: Strutinsky
ax = axes[1, 2]
ax.plot(tau_values, E_GS_grid, 'b-', lw=1.5, label='E_GS')
ax.plot(tau_values, E_smooth_2cell, 'r--', lw=1, label='E_smooth')
ax2 = ax.twinx()
ax2.plot(tau_values, delta_E_shell_2cell, 'g-', lw=1, alpha=0.7, label='delta_E_shell')
ax2.set_ylabel('delta_E_shell (M_KK)', color='g')
ax.axvline(tau_values[fold_idx], color='gray', ls='--', alpha=0.5)
ax.set_xlabel('tau')
ax.set_ylabel('E (M_KK)')
ax.set_title('Strutinsky decomposition (2-cell)')
ax.legend(loc='upper right', fontsize=8)
ax2.legend(loc='lower right', fontsize=8)
ax.grid(True, alpha=0.3)

plt.suptitle(f'FINITE-RATE-TRANSIT-57: Gate = {verdict}\n'
             f'P_exc = {P_exc_final:.4e} at dtau/dt = {dtau_dt_phys:.1f}',
             fontsize=14, fontweight='bold')
plt.tight_layout()

plot_path = os.path.join(data_dir, 's57_finite_rate_transit.png')
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"  Saved: {plot_path}")

print("\n" + "=" * 70)
print(f"DONE — Gate: {verdict}, P_exc = {P_exc_final:.6e}")
print("=" * 70)
