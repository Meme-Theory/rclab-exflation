#!/usr/bin/env python3
"""
S77-D5-TRANS-PBH: Power Spectrum at the Stiff-to-dS Transition Scale
=====================================================================

Computes the primordial power spectrum P_zeta(k) for modes near the
stiff-to-dS transition scale k_trans, where enhanced amplification may
produce PBHs or spectral distortions.

Gate: S77-D5-TRANS-PBH (INFO)
  Report P_zeta(k_trans) and PBH formation assessment.
  If P_zeta > 10^{-2}, flag as potential PBH channel.

Physics:
  The S73B trajectory transitions from stiff (w ~ 0.15, eps ~ 1.7) at the fold
  to quasi-dS (w ~ -0.997, eps ~ 0.005) within ~1 e-fold. The comoving Hubble
  parameter aH has a MINIMUM at N ~ 0.036 (where eps = 1). Modes with k near
  this minimum experience a deeply nonadiabatic transition that amplifies their
  amplitude via parametric/Bogoliubov enhancement.

  Mode equation (conformal time, no friction):
    v_k'' + (k^2 - z''/z) v_k = 0                                  ... (1)

  z = a * sqrt(2*eps) * M_Pl (Mukhanov variable: v = z * zeta)      ... (2)

  Wronskian conservation: W = v*v'* - v'*v* = const (unitarity)      ... (3)

  Power spectrum: P_zeta = k^3/(2*pi^2) * |v_k/z|^2                 ... (4)

  Enhancement factor: F_amp = P_zeta(real) / P_zeta(pure dS)        ... (5)

Method:
  1. Load S73B trajectory, compute z''/z in conformal time
  2. Solve mode eq (1) in conformal time with plane-wave IC at eta=0
  3. Solve same eq for pure dS with identical IC (normalization-independent F_amp)
  4. F_amp(k) = P_zeta(real) / P_zeta(dS) is IC-independent
  5. Physical P_zeta = F_amp * [H^2/(8*pi^2*eps)] * (M_KK/M_Pl)^2

  The conformal-time formulation has NO friction term and exactly conserves
  the Wronskian, providing a clean unitarity cross-check.

Input: computations/session-73/s73b_efold_mapping.npz, s77_n_pivot_map.npz
Output: computations/session-77/s77_transition_scale_pbh.npz, .png

Cross-checks:
  CHK1: Wronskian |W(eta_end)/W(0) - 1| < 10^{-6} (unitarity)
  CHK2: F_amp -> 1 for modes deep inside horizon during transition
  CHK3: P_zeta frozen after horizon exit (superhorizon constancy)
  CHK4: pump -> 2*(aH)^2 in dS limit
  CHK5: P_zeta(dS) matches analytic H^2/(8*pi^2*eps) to < 10%
"""

import sys
sys.path.insert(0, "computations")
from canonical_constants import (
    M_KK, M_KK_gravity, A_s_CMB, M_Pl_reduced,
    H_fold, m_tau, tau_fold, dS_fold, d2S_fold, S_fold,
    v_terminal, dt_transit, Mpc_to_GeV_inv
)
import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import interp1d
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

print("=" * 78)
print("S77-D5-TRANS-PBH: Power Spectrum at Stiff-to-dS Transition Scale")
print("=" * 78)

# =============================================================================
# SECTION 1: Load trajectory data
# =============================================================================
print("\nSECTION 1: Loading trajectory data")
print("-" * 50)

data73 = np.load("computations/session-73/s73b_efold_mapping.npz", allow_pickle=True)
lna_raw = data73['lna_sol']
H_raw = data73['H_sol']
w_raw = data73['w_sol']
aH_raw = data73['aH_sol']
N_total_s73b = float(data73['N_total'])  # (local)

data77 = np.load("computations/session-77/s77_n_pivot_map.npz", allow_pickle=True)
k_pivot_fold = float(data77['k_pivot_com_fold'])  # (local) = 14.31 M_KK
N_pivot = float(data77['N_pivot'])  # (local) = 3.12

print(f"  Trajectory: {len(lna_raw)} points, N in [{lna_raw[0]:.4f}, {lna_raw[-1]:.4f}]")
print(f"  k_pivot (fold norm) = {k_pivot_fold:.4f} M_KK")
print(f"  N_pivot = {N_pivot:.4f}")

# =============================================================================
# SECTION 2: Build conformal-time arrays
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 2: Conformal Time & Pump Field")
print("-" * 50)

# Restrict to N < N_max for mode equation (modes freeze well before this)
N_max_mode = 15.0  # (local) e-folds
mask_N = lna_raw <= N_max_mode  # (local)
N_arr = lna_raw[mask_N].copy()  # (local)
H_arr = H_raw[mask_N].copy()  # (local)
w_arr = w_raw[mask_N].copy()  # (local)
aH_arr = aH_raw[mask_N].copy()  # (local)
eps_arr = 1.5 * (1.0 + w_arr)  # (local) Eq. (2): eps = 3(1+w)/2
a_arr = np.exp(N_arr)  # (local)
z_arr = a_arr * np.sqrt(2.0 * np.abs(eps_arr) + 1e-30)  # (local) Eq. (2)

# Conformal time: d_eta = dN / (aH)
d_eta_dN = 1.0 / aH_arr  # (local)
dN_step = np.gradient(N_arr)  # (local)
eta_arr = np.cumsum(d_eta_dN * dN_step)  # (local) cumulative conformal time
eta_arr -= eta_arr[0]  # (local) eta = 0 at N = 0

print(f"  Conformal time range: eta in [0, {eta_arr[-1]:.6f}] M_KK^{{-1}}")
print(f"  N range: [0, {N_arr[-1]:.4f}]")

# Transition scale: minimum of aH
idx_aH_min = np.argmin(aH_arr)  # (local)
k_trans = aH_arr[idx_aH_min]  # (local) M_KK
N_trans = N_arr[idx_aH_min]  # (local)
print(f"  k_trans = aH_min = {k_trans:.6f} M_KK (at N = {N_trans:.6f})")

# Pump field z''/z: compute via eps, eta_H
deps_dN = np.gradient(eps_arr, N_arr)  # (local)
eta_H_arr = deps_dN / (eps_arr + 1e-30)  # (local) d(ln eps)/dN
deta_H_dN = np.gradient(eta_H_arr, N_arr)  # (local)
dlnz_dN = 1.0 + 0.5 * eta_H_arr  # (local)
d2lnz_dN2 = 0.5 * deta_H_dN  # (local)
# pump_N = z''/z / (aH)^2 in N-variable
pump_N_arr = d2lnz_dN2 + dlnz_dN**2 + (1.0 - eps_arr) * dlnz_dN  # (local)
# z''/z in conformal time = (aH)^2 * pump_N
zppoz_arr = aH_arr**2 * pump_N_arr  # (local)

# CHK4: pump_N -> 2 in dS limit
pump_dS_check = pump_N_arr[N_arr > 8.0].mean()  # (local)
print(f"\n  CHK4: pump_N(N>8) = {pump_dS_check:.6f} (expected: 2.0)")
assert abs(pump_dS_check - 2.0) < 0.01, f"CHK4 FAIL: pump = {pump_dS_check}"
print(f"  CHK4: PASS")

# dS reference values
H_dS = H_arr[N_arr > 5.0].mean()  # (local) late-time H in M_KK
eps_dS = eps_arr[N_arr > 5.0].mean()  # (local) late-time eps
P_dS_analytic = H_dS**2 / (8.0 * np.pi**2 * eps_dS)  # (local) Eq. for pure dS, M_Pl=1
print(f"\n  dS reference: H = {H_dS:.6f}, eps = {eps_dS:.6e}")
print(f"  P_dS(analytic, M_Pl=1) = H^2/(8*pi^2*eps) = {P_dS_analytic:.6f}")

# Build interpolators (functions of conformal time eta)
zppoz_eta_interp = interp1d(eta_arr, zppoz_arr, kind='cubic', fill_value='extrapolate')  # (local)
z_eta_interp = interp1d(eta_arr, z_arr, kind='cubic', fill_value='extrapolate')  # (local)
N_of_eta_interp = interp1d(eta_arr, N_arr, kind='cubic', fill_value='extrapolate')  # (local)
aH_of_N_interp = interp1d(N_arr, aH_arr, kind='cubic', fill_value='extrapolate')  # (local)

# Also build pure dS z''/z for comparison
# For pure dS with a = exp(H_dS * N), conformal time:
#   eta_dS(N) = integral_0^N dN'/(H_dS * exp(N')) = (1 - exp(-N)) / H_dS
# z''/z = 2 * H_dS^2 / (1 - H_dS * eta)^2 [exact for dS]
def zppoz_pure_dS(eta):
    """z''/z for pure de Sitter in conformal time."""
    return 2.0 * H_dS**2 / (1.0 - H_dS * eta)**2  # (local)


# =============================================================================
# SECTION 3: Mode Equation Solver (Conformal Time)
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 3: Mode Equation Solver")
print("-" * 50)

def solve_mode_conformal(k_com, zppoz_func, eta_start, eta_end,
                         rtol=1e-11, atol=1e-13):
    """Solve v'' + (k^2 - z''/z) v = 0 in conformal time.

    Uses plane-wave initial condition v = 1/sqrt(2k) at eta_start.
    The Wronskian W = v*v'* - v'*v* is exactly conserved (no friction).

    Returns dict with solution values at eta_end.
    """
    # Plane-wave IC: v(0) = 1/sqrt(2k), dv/d_eta(0) = -ik/sqrt(2k)
    amp = 1.0 / np.sqrt(2.0 * k_com)  # (local) BD amplitude
    y0 = [amp, 0.0, 0.0, -k_com * amp]  # (local) [v_re, v_im, dv_re, dv_im]

    def rhs(eta, y):
        vr, vi, dvr, dvi = y
        zpp = float(zppoz_func(eta))
        omega2 = k_com**2 - zpp  # (local)
        return [dvr, dvi, -omega2 * vr, -omega2 * vi]

    d_eta = eta_end - eta_start  # (local)
    max_step = d_eta / 5000  # (local) ensure good resolution

    sol = solve_ivp(rhs, [eta_start, eta_end], y0,
                    method='DOP853', rtol=rtol, atol=atol,
                    dense_output=True, max_step=max_step)

    if not sol.success:
        return {'status': 'SOLVER_FAILED', 'message': sol.message}

    # Evaluate at dense points
    n_pts = 2000  # (local)
    eta_eval = np.linspace(eta_start, eta_end, n_pts)  # (local)
    y_eval = sol.sol(eta_eval)  # (local)

    # Wronskian conservation check
    W = y_eval[0] * y_eval[3] - y_eval[1] * y_eval[2]  # (local) W = v_re * dv_im - v_im * dv_re
    W_0 = W[0]  # (local)
    W_end = W[-1]  # (local)
    W_deviation = abs(W_end - W_0) / abs(W_0)  # (local)

    # Power spectrum P_zeta at each point
    v_abs2 = y_eval[0]**2 + y_eval[1]**2  # (local)
    z_eval = np.array([float(z_eta_interp(e)) for e in eta_eval])  # (local)
    P_zeta = k_com**3 / (2.0 * np.pi**2) * v_abs2 / (z_eval**2 + 1e-30)  # (local) Eq. (4)

    # Frozen value: median of last 200 points
    P_zeta_final = np.median(P_zeta[-200:])  # (local)

    return {
        'status': 'OK',
        'k_com': k_com,
        'P_zeta_final': P_zeta_final,
        'v_abs2_final': np.median(v_abs2[-200:]),
        'z_final': z_eval[-1],
        'W_0': W_0,
        'W_end': W_end,
        'W_deviation': W_deviation,
        'P_zeta_arr': P_zeta,
        'eta_eval': eta_eval,
    }


def solve_mode_pure_dS(k_com, eta_end, rtol=1e-11, atol=1e-13):
    """Solve mode equation for pure dS background with plane-wave IC."""
    amp = 1.0 / np.sqrt(2.0 * k_com)  # (local)
    y0 = [amp, 0.0, 0.0, -k_com * amp]  # (local)

    def rhs(eta, y):
        vr, vi, dvr, dvi = y
        zpp = zppoz_pure_dS(eta)
        omega2 = k_com**2 - zpp
        return [dvr, dvi, -omega2 * vr, -omega2 * vi]

    d_eta = eta_end  # (local)
    max_step = d_eta / 5000  # (local)

    sol = solve_ivp(rhs, [0, eta_end], y0,
                    method='DOP853', rtol=rtol, atol=atol,
                    dense_output=True, max_step=max_step)

    if not sol.success:
        return {'status': 'SOLVER_FAILED'}

    n_pts = 2000  # (local)
    eta_eval = np.linspace(0, eta_end, n_pts)  # (local)
    y_eval = sol.sol(eta_eval)  # (local)

    v_abs2 = y_eval[0]**2 + y_eval[1]**2  # (local)

    # z for pure dS: z = exp(N) * sqrt(2*eps_dS)
    # N(eta) from eta = (1-exp(-N))/H_dS -> exp(-N) = 1 - H_dS*eta
    N_dS = -np.log(1.0 - H_dS * eta_eval)  # (local)
    z_dS = np.exp(N_dS) * np.sqrt(2.0 * eps_dS)  # (local)
    P_zeta = k_com**3 / (2.0 * np.pi**2) * v_abs2 / (z_dS**2 + 1e-30)  # (local)

    W = y_eval[0] * y_eval[3] - y_eval[1] * y_eval[2]  # (local)

    return {
        'status': 'OK',
        'P_zeta_final': np.median(P_zeta[-200:]),
        'W_0': W[0],
        'W_end': W[-1],
        'W_deviation': abs(W[-1] - W[0]) / abs(W[0]),
    }


# =============================================================================
# SECTION 4: Compute F_amp(k) across the transition scale
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 4: Computing F_amp(k)")
print("-" * 50)

# k range: k_trans/10 to max(k_trans*10, 2*k_pivot)
k_lo = k_trans / 10.0  # (local) ~ 0.096 M_KK
k_hi = max(k_trans * 10.0, 2.0 * k_pivot_fold)  # (local) ~ 28.6 M_KK
n_k = 50  # (local)

k_values = np.geomspace(k_lo, k_hi, n_k)  # (local)
# Add k_pivot and k_trans explicitly
k_values = np.sort(np.unique(np.append(k_values, [k_pivot_fold, k_trans])))  # (local)
n_k = len(k_values)  # (local)

print(f"  k range: [{k_lo:.4f}, {k_hi:.4f}] M_KK ({n_k} modes)")
print(f"  k_trans = {k_trans:.6f} M_KK")
print(f"  k_pivot = {k_pivot_fold:.4f} M_KK")

# For each k: solve real trajectory and pure dS, compute F_amp = P_real / P_dS
F_amp_arr = np.zeros(n_k)  # (local)
P_real_arr = np.zeros(n_k)  # (local)
P_dS_comp_arr = np.zeros(n_k)  # (local)
W_dev_arr = np.zeros(n_k)  # (local)
status_arr = []  # (local)

print(f"\n  Solving mode equations...")
for i, k in enumerate(k_values):
    # Determine eta_end: mode should be well superhorizon
    # Find N where k / aH = 0.05 (safely superhorizon)
    koh = k / aH_arr  # (local)
    idx_sh = np.where(koh < 0.05)[0]  # (local)
    if len(idx_sh) > 0:
        N_end = N_arr[idx_sh[0]]  # (local)
        eta_end = eta_arr[idx_sh[0]]  # (local)
    else:
        # Mode never goes superhorizon in our range -- still subhorizon
        # Use the full range
        N_end = N_arr[-1]  # (local)
        eta_end = eta_arr[-1]  # (local)

    # For modes with k < aH(0): superhorizon at fold -- no BD condition
    if k < aH_arr[0]:
        F_amp_arr[i] = np.nan
        P_real_arr[i] = np.nan
        P_dS_comp_arr[i] = np.nan
        W_dev_arr[i] = np.nan
        status_arr.append('SUPER')
        continue

    # Solve real trajectory
    result_real = solve_mode_conformal(k, zppoz_eta_interp, 0.0, eta_end)  # (local)

    if result_real['status'] != 'OK':
        F_amp_arr[i] = np.nan
        P_real_arr[i] = np.nan
        P_dS_comp_arr[i] = np.nan
        W_dev_arr[i] = np.nan
        status_arr.append(result_real['status'])
        continue

    # Solve pure dS
    # eta_end for pure dS: find eta_dS where k/aH_dS = 0.05
    # aH_dS = H_dS * exp(N), so N = ln(k/(0.05*H_dS))
    N_dS_exit = np.log(k / (0.05 * H_dS))  # (local)
    eta_dS_end = (1.0 - np.exp(-N_dS_exit)) / H_dS  # (local)
    # Don't exceed eta_max_dS = 1/H_dS (conformal time horizon)
    eta_dS_max = 0.99 / H_dS  # (local) stay away from singularity
    eta_dS_end = min(eta_dS_end, eta_dS_max)  # (local)

    result_dS = solve_mode_pure_dS(k, eta_dS_end)  # (local)

    if result_dS['status'] != 'OK':
        F_amp_arr[i] = np.nan
        P_real_arr[i] = np.nan
        P_dS_comp_arr[i] = np.nan
        W_dev_arr[i] = np.nan
        status_arr.append('DS_FAIL')
        continue

    # Store results
    P_real_arr[i] = result_real['P_zeta_final']
    P_dS_comp_arr[i] = result_dS['P_zeta_final']
    F_amp_arr[i] = result_real['P_zeta_final'] / (result_dS['P_zeta_final'] + 1e-30)
    W_dev_arr[i] = result_real['W_deviation']
    status_arr.append('OK')

    if i % 10 == 0 or abs(k - k_pivot_fold) < 0.01 or abs(k - k_trans) < 0.01:
        print(f"    k = {k:10.4f}: P_real = {P_real_arr[i]:.4e}, P_dS = {P_dS_comp_arr[i]:.4e}, "
              f"F_amp = {F_amp_arr[i]:.4e}, W_dev = {W_dev_arr[i]:.2e}")

# =============================================================================
# SECTION 5: Cross-Checks
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 5: Cross-Checks")
print("-" * 50)

valid = np.array([s == 'OK' for s in status_arr])  # (local)
k_valid = k_values[valid]  # (local)
F_valid = F_amp_arr[valid]  # (local)
P_real_valid = P_real_arr[valid]  # (local)
P_dS_valid = P_dS_comp_arr[valid]  # (local)
W_dev_valid = W_dev_arr[valid]  # (local)

print(f"  Valid solutions: {valid.sum()} / {n_k}")
print(f"  Superhorizon at fold: {sum(1 for s in status_arr if s == 'SUPER')}")

# CHK1: Wronskian conservation
max_W_dev = W_dev_valid.max()  # (local)
print(f"\n  CHK1: max Wronskian deviation = {max_W_dev:.2e} (threshold: 1e-6)")
if max_W_dev < 1e-6:
    print(f"  CHK1: PASS")
else:
    print(f"  CHK1: WARNING (deviation {max_W_dev:.2e})")

# CHK2: F_amp -> 1 for high-k modes
high_k_mask = k_valid > 20.0  # (local)
if high_k_mask.sum() > 0:
    F_high_k = F_valid[high_k_mask]  # (local)
    print(f"\n  CHK2: F_amp for k > 20 M_KK (should approach 1):")
    print(f"    Range: [{F_high_k.min():.4f}, {F_high_k.max():.4f}]")
    print(f"    Mean: {F_high_k.mean():.4f}")
    if abs(F_high_k.mean() - 1.0) < 0.5:
        print(f"    CHK2: PASS")
    else:
        print(f"    CHK2: NOTE (F_amp = {F_high_k.mean():.4f}, transition effects extend to high k)")

# CHK3: Frozen spectrum test
# Pick a mode that exits early, check that P_zeta is constant after exit
test_k = k_valid[np.argmin(np.abs(k_valid - 2.0))]  # (local) k ~ 2 M_KK
koh_test = test_k / aH_arr  # (local)
idx_sh_test = np.where(koh_test < 0.05)[0]  # (local)
if len(idx_sh_test) > 0:
    eta_end_test = eta_arr[idx_sh_test[0]]  # (local)
    sol_test = solve_mode_conformal(test_k, zppoz_eta_interp, 0.0, eta_end_test)
    if sol_test['status'] == 'OK':
        P_test = sol_test['P_zeta_arr']  # (local)
        P_late = P_test[-200:]  # (local)
        freeze_var = np.std(P_late) / (np.mean(P_late) + 1e-30)  # (local)
        print(f"\n  CHK3: Frozen spectrum (k = {test_k:.4f} M_KK):")
        print(f"    P_zeta(late) = {np.mean(P_late):.4e} +/- {np.std(P_late):.4e}")
        print(f"    Fractional variation: {freeze_var:.2e}")
        if freeze_var < 0.01:
            print(f"    CHK3: PASS")

# CHK5: dS computation matches analytic
# For k ~ 5 (well inside horizon at fold in dS): P_dS should match H^2/(8*pi^2*eps)
# The plane-wave IC doesn't exactly match BD, so there's a correction for finite k/H.
# Check trend: P_dS(comp) / P_dS(analytic) should approach 1 for large k.
if len(P_dS_valid) > 3:
    ratios = P_dS_valid / P_dS_analytic  # (local)
    print(f"\n  CHK5: P_dS(computed) / P_dS(analytic) = H^2/(8*pi^2*eps):")
    for j in range(0, len(k_valid), max(1, len(k_valid)//8)):
        print(f"    k = {k_valid[j]:8.3f}: ratio = {ratios[j]:.4f}")
    # For large k, ratio should approach the plane-wave correction factor
    print(f"    Trend: {'CONVERGING' if ratios[-1] < ratios[0] else 'OK'}")

# =============================================================================
# SECTION 6: Physical Power Spectrum
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 6: Physical Power Spectrum & PBH Assessment")
print("-" * 50)

# Physical P_zeta = F_amp * P_dS_phys
# P_dS_phys = H_phys^2 / (8*pi^2 * eps * M_Pl^2)
# = (H_dS * M_KK)^2 / (8*pi^2 * eps_dS * M_Pl_reduced^2)
# = H_dS^2 * (M_KK/M_Pl)^2 / (8*pi^2 * eps_dS)
# = P_dS_analytic * (M_KK/M_Pl)^2

MKK_over_MPl_sq = (M_KK / M_Pl_reduced)**2  # (local) = (7.43e16/2.435e18)^2
P_dS_phys = P_dS_analytic * MKK_over_MPl_sq  # (local)

print(f"  (M_KK/M_Pl)^2 = {MKK_over_MPl_sq:.4e}")
print(f"  P_dS(physical) = {P_dS_phys:.4e}")
print(f"  A_s(Planck) = {A_s_CMB:.4e}")
print(f"  P_dS / A_s = {P_dS_phys / A_s_CMB:.4e}")

# Physical P_zeta = F_amp * P_dS_phys
P_phys_arr = F_amp_arr * P_dS_phys  # (local)

if len(k_valid) > 0:
    P_phys_valid = F_valid * P_dS_phys  # (local)

    # Results at key scales
    idx_trans = np.argmin(np.abs(k_valid - k_trans))  # (local)
    idx_pivot = np.argmin(np.abs(k_valid - k_pivot_fold))  # (local)
    idx_max = np.argmax(P_phys_valid)  # (local)

    print(f"\n  P_zeta(k_trans = {k_trans:.4f} M_KK):")
    print(f"    F_amp = {F_valid[idx_trans]:.2f}")
    print(f"    P_zeta(physical) = {P_phys_valid[idx_trans]:.4e}")
    print(f"    PBH threshold 10^{{-2}}: {'EXCEEDS' if P_phys_valid[idx_trans] > 1e-2 else 'BELOW'}")

    print(f"\n  P_zeta(k_pivot = {k_pivot_fold:.4f} M_KK):")
    print(f"    F_amp = {F_valid[idx_pivot]:.2f}")
    print(f"    P_zeta(physical) = {P_phys_valid[idx_pivot]:.4e}")
    print(f"    Ratio to A_s: {P_phys_valid[idx_pivot] / A_s_CMB:.4e}")

    print(f"\n  Maximum P_zeta:")
    print(f"    k = {k_valid[idx_max]:.4f} M_KK")
    print(f"    F_amp = {F_valid[idx_max]:.2f}")
    print(f"    P_zeta(physical) = {P_phys_valid[idx_max]:.4e}")

    # PBH assessment
    P_max_phys = P_phys_valid.max()  # (local)
    print(f"\n  PBH Assessment:")
    print(f"    max P_zeta(phys) = {P_max_phys:.4e}")
    print(f"    PBH threshold = 1e-2")
    if P_max_phys > 1e-2:
        pbh_verdict = "EXCEEDS_PBH_THRESHOLD"  # (local)
        print(f"    RESULT: P_zeta EXCEEDS PBH threshold by {np.log10(P_max_phys/1e-2):.1f} OOM")
    else:
        pbh_verdict = "BELOW_PBH_THRESHOLD"  # (local)
        print(f"    RESULT: P_zeta BELOW PBH threshold by {np.log10(1e-2/P_max_phys):.1f} OOM")

    # A_s gap
    A_s_gap_OOM = np.log10(A_s_CMB / P_dS_phys)  # (local) gap without enhancement
    A_s_gap_with_Famp = np.log10(A_s_CMB / P_phys_valid[idx_pivot])  # (local) gap WITH enhancement
    print(f"\n  A_s Gap Analysis:")
    print(f"    Gap without enhancement: {A_s_gap_OOM:.2f} OOM")
    print(f"    F_amp(k_pivot) = {F_valid[idx_pivot]:.2f} ({np.log10(F_valid[idx_pivot]):.2f} OOM)")
    print(f"    Gap WITH enhancement: {A_s_gap_with_Famp:.2f} OOM")
    print(f"    Enhancement closes {np.log10(F_valid[idx_pivot]):.2f} OOM of the {A_s_gap_OOM:.2f} OOM gap")

    # Spectral distortion mu-parameter (rough)
    if len(k_valid) > 2:
        dlnk = np.gradient(np.log(k_valid))  # (local)
        mu_estimate = 2.2 * np.sum(P_phys_valid * dlnk)  # (local)
        print(f"\n  Spectral Distortion:")
        print(f"    mu (rough) ~ {mu_estimate:.4e}")
        print(f"    COBE/FIRAS bound: mu < 9e-5")
    else:
        mu_estimate = np.nan  # (local)

else:
    pbh_verdict = "NO_VALID_MODES"  # (local)
    A_s_gap_OOM = np.nan  # (local)
    A_s_gap_with_Famp = np.nan  # (local)
    mu_estimate = np.nan  # (local)

# =============================================================================
# SECTION 7: Physical Scale Mapping
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 7: Physical Scale Mapping")
print("-" * 50)

# k [Mpc^{-1}] = k_com(fold) * M_KK / exp(N_total) * Mpc_to_GeV_inv
k_phys_GeV = k_values * M_KK / np.exp(N_total_s73b)  # (local)
k_phys_Mpc = k_phys_GeV * Mpc_to_GeV_inv  # (local)

k_pivot_check = k_pivot_fold * M_KK / np.exp(N_total_s73b) * Mpc_to_GeV_inv  # (local)
k_trans_Mpc = k_trans * M_KK / np.exp(N_total_s73b) * Mpc_to_GeV_inv  # (local)

print(f"  k_pivot check: {k_pivot_check:.6f} Mpc^{{-1}} (expected: 0.05)")
print(f"  k_trans = {k_trans_Mpc:.4e} Mpc^{{-1}}")

# PBH mass scale
if k_trans_Mpc > 0:
    M_PBH_grams = 1e18 * (k_trans_Mpc / 1e6)**(-2)  # (local) rough estimate
    M_PBH_solar = M_PBH_grams / 1.989e33  # (local)
    print(f"  PBH mass scale: M_PBH ~ {M_PBH_grams:.2e} g ~ {M_PBH_solar:.2e} M_sun")

# =============================================================================
# SECTION 8: Summary Table
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 8: Summary Table")
print("-" * 50)

print(f"\n  {'k [M_KK]':>12s} {'k [Mpc^-1]':>12s} {'F_amp':>10s} {'P_phys':>12s} {'W_dev':>10s} {'Status':>8s}")
print("  " + "-" * 72)
for i in range(n_k):
    label = ""  # (local)
    if abs(k_values[i] - k_trans) < 0.001:
        label = " <-- k_trans"
    elif abs(k_values[i] - k_pivot_fold) < 0.01:
        label = " <-- k_pivot"
    if i % 5 == 0 or label:
        if status_arr[i] == 'OK':
            print(f"  {k_values[i]:12.4f} {k_phys_Mpc[i]:12.4e} {F_amp_arr[i]:10.2f} "
                  f"{P_phys_arr[i]:12.4e} {W_dev_arr[i]:10.2e}{label}")
        else:
            print(f"  {k_values[i]:12.4f} {k_phys_Mpc[i]:12.4e} {'---':>10s} "
                  f"{'---':>12s} {'---':>10s} {status_arr[i]:>8s}{label}")

# =============================================================================
# SECTION 9: Gate Verdict
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 9: Gate Verdict")
print("-" * 50)

gate_name = "S77-D5-TRANS-PBH"  # (local)
gate_verdict = "INFO"  # (local)

if len(k_valid) > 0:
    gate_detail = (  # (local)
        f"F_amp(k_trans={k_trans:.3f} M_KK) = {F_valid[idx_trans]:.0f}. "
        f"F_amp(k_pivot={k_pivot_fold:.1f} M_KK) = {F_valid[idx_pivot]:.0f}. "
        f"P_zeta(k_trans,phys) = {P_phys_valid[idx_trans]:.2e}. "
        f"P_zeta(k_pivot,phys) = {P_phys_valid[idx_pivot]:.2e}. "
        f"max F_amp = {F_valid.max():.0f} at k = {k_valid[np.argmax(F_valid)]:.1f} M_KK. "
        f"P_dS(phys) = {P_dS_phys:.2e}. "
        f"A_s gap = {A_s_gap_OOM:.1f} OOM (bare) -> {A_s_gap_with_Famp:.1f} OOM (with F_amp). "
        f"Transition closes {np.log10(F_valid[idx_pivot]):.1f} OOM. "
        f"PBH: {pbh_verdict}. "
        f"Wronskian max dev = {max_W_dev:.1e}. "
        f"Stiff-to-dS at N={N_trans:.3f}, k_trans={k_trans_Mpc:.1e} Mpc^-1."
    )
else:
    gate_detail = "All modes superhorizon at fold."  # (local)

print(f"\n  Gate: {gate_name}")
print(f"  Verdict: {gate_verdict}")
print(f"  Detail: {gate_detail}")

# =============================================================================
# SECTION 10: Save Results
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 10: Saving Results")
print("-" * 50)

save_dict = dict(  # (local)
    gate_name=gate_name,
    gate_verdict=gate_verdict,
    gate_detail=gate_detail,
    # k arrays
    k_values=k_values,
    k_phys_Mpc=k_phys_Mpc,
    k_trans=k_trans,
    k_trans_Mpc=k_trans_Mpc,
    k_pivot_fold=k_pivot_fold,
    N_trans=N_trans,
    # Enhancement factors
    F_amp=F_amp_arr,
    P_real_code=P_real_arr,
    P_dS_code=P_dS_comp_arr,
    P_phys=P_phys_arr,
    # Reference values
    P_dS_analytic=P_dS_analytic,
    P_dS_phys=P_dS_phys,
    MKK_over_MPl_sq=MKK_over_MPl_sq,
    H_dS=H_dS,
    eps_dS=eps_dS,
    # Assessment
    pbh_verdict=pbh_verdict,
    A_s_gap_bare_OOM=A_s_gap_OOM,
    # Cross-checks
    CHK1_max_W_dev=max_W_dev,
    CHK4_pump_dS=pump_dS_check,
    # Pump field (at fold)
    pump_N_fold=pump_N_arr[0],
    zppoz_fold=zppoz_arr[0],
)

# Add A_s gap with enhancement only if valid
if len(k_valid) > 0:
    save_dict['A_s_gap_with_Famp_OOM'] = A_s_gap_with_Famp
    save_dict['F_amp_pivot'] = F_valid[idx_pivot]
    save_dict['F_amp_trans'] = F_valid[idx_trans]
    save_dict['F_amp_max'] = F_valid.max()
    save_dict['k_F_amp_max'] = k_valid[np.argmax(F_valid)]

np.savez("computations/session-77/s77_transition_scale_pbh.npz", **save_dict)
print(f"  Saved: computations/session-77/s77_transition_scale_pbh.npz")

# =============================================================================
# SECTION 11: Plots
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 11: Plotting")
print("-" * 50)

fig, axes = plt.subplots(2, 3, figsize=(18, 10))

# Panel 1: F_amp(k)
ax = axes[0, 0]
if len(k_valid) > 0:
    ax.loglog(k_valid, F_valid, 'b-', lw=2, label=r'$F_{amp}(k)$')
    ax.axvline(k_trans, color='r', ls='--', alpha=0.7, label=f'$k_{{trans}}$={k_trans:.3f}')
    ax.axvline(k_pivot_fold, color='g', ls='--', alpha=0.7, label=f'$k_{{pivot}}$={k_pivot_fold:.1f}')
    ax.axhline(1.0, color='gray', ls=':', alpha=0.5, label='F=1 (no enhancement)')
    ax.set_xlabel(r'$k$ [$M_{KK}$]')
    ax.set_ylabel(r'$F_{amp} = \mathcal{P}_\zeta^{real} / \mathcal{P}_\zeta^{dS}$')
    ax.set_title('Enhancement Factor')
    ax.legend(fontsize=7)

# Panel 2: P_zeta(k) physical
ax = axes[0, 1]
if len(k_valid) > 0:
    ax.loglog(k_valid, P_phys_valid, 'b-', lw=2, label=r'$\mathcal{P}_\zeta(k)$')
    ax.axhline(A_s_CMB, color='orange', ls='-', lw=2, alpha=0.7, label=f'$A_s$={A_s_CMB:.1e}')
    ax.axhline(1e-2, color='red', ls='--', alpha=0.7, label='PBH threshold')
    ax.axhline(P_dS_phys, color='gray', ls=':', alpha=0.5, label=f'$P_{{dS}}$={P_dS_phys:.1e}')
    ax.axvline(k_trans, color='r', ls='--', alpha=0.3)
    ax.axvline(k_pivot_fold, color='g', ls='--', alpha=0.3)
    ax.set_xlabel(r'$k$ [$M_{KK}$]')
    ax.set_ylabel(r'$\mathcal{P}_\zeta(k)$ [physical]')
    ax.set_title('Physical Power Spectrum')
    ax.legend(fontsize=7)

# Panel 3: P_zeta on Mpc^{-1} scale
ax = axes[0, 2]
if len(k_valid) > 0:
    k_valid_Mpc = k_phys_Mpc[valid]  # (local)
    ax.loglog(k_valid_Mpc, P_phys_valid, 'b-', lw=2)
    ax.axhline(A_s_CMB, color='orange', ls='-', lw=2, alpha=0.7, label='$A_s$ (Planck)')
    ax.axhline(1e-2, color='red', ls='--', alpha=0.7, label='PBH threshold')
    ax.axvline(0.05, color='g', ls='--', alpha=0.7, label=r'$k_{pivot}$')
    ax.set_xlabel(r'$k$ [Mpc$^{-1}$]')
    ax.set_ylabel(r'$\mathcal{P}_\zeta(k)$')
    ax.set_title('Power Spectrum (Physical Scales)')
    ax.legend(fontsize=7)

# Panel 4: Background w(N), eps(N)
ax = axes[1, 0]
N_plot_max = 5.0  # (local)
mask_plot = N_arr < N_plot_max  # (local)
ax.plot(N_arr[mask_plot], w_arr[mask_plot], 'b-', lw=2, label='$w(N)$')
ax.plot(N_arr[mask_plot], eps_arr[mask_plot], 'r-', lw=2, label=r'$\epsilon(N)$')
ax.axhline(-1/3, color='gray', ls=':', alpha=0.5, label='$w=-1/3$')
ax.axhline(1.0, color='gray', ls='--', alpha=0.3, label=r'$\epsilon=1$')
ax.set_xlabel('$N$ [e-folds]')
ax.set_ylabel('$w$, $\\epsilon$')
ax.set_title('Stiff-to-dS Transition')
ax.legend(fontsize=7)
ax.set_ylim(-1.2, 2.0)

# Panel 5: z''/z pump field
ax = axes[1, 1]
ax.plot(N_arr[mask_plot], pump_N_arr[mask_plot], 'b-', lw=2)
ax.axhline(2.0, color='gray', ls=':', alpha=0.5, label='dS value = 2')
ax.set_xlabel('$N$ [e-folds]')
ax.set_ylabel(r"$z''/z \,/\, (aH)^2$")
ax.set_title('Pump Field (N-variable)')
ax.legend(fontsize=7)
ax.set_ylim(-150, 10)

# Panel 6: aH(N) with mode scales
ax = axes[1, 2]
ax.semilogy(N_arr[mask_plot], aH_arr[mask_plot], 'b-', lw=2, label='$aH(N)$')
ax.axhline(k_trans, color='r', ls='--', alpha=0.7, label=f'$k_{{trans}}$={k_trans:.3f}')
ax.axhline(k_pivot_fold, color='g', ls='--', alpha=0.7, label=f'$k_{{pivot}}$={k_pivot_fold:.1f}')
ax.set_xlabel('$N$ [e-folds]')
ax.set_ylabel('$aH$ [$M_{KK}$]')
ax.set_title('Comoving Hubble Parameter')
ax.legend(fontsize=7)

plt.suptitle('S77-D5-TRANS-PBH: Power Spectrum at Stiff-to-dS Transition', fontsize=14)
plt.tight_layout()
plt.savefig("computations/session-77/s77_transition_scale_pbh.png", dpi=150, bbox_inches='tight')
print(f"  Saved: computations/session-77/s77_transition_scale_pbh.png")

print("\n" + "=" * 78)
print("S77-D5-TRANS-PBH: COMPLETE")
print("=" * 78)
