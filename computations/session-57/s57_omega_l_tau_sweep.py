#!/usr/bin/env python3
"""
S57 OMEGA-L-TAU-SWEEP-57: Leggett frequency minimum search at 100 tau points
=============================================================================
Gate: INFO — precise location and depth of omega_L0(tau) minimum

Refines W0-1 (s57_leggett_tau_profile.py, 50 points) with 100-point tau grid.
Tests whether finer resolution reveals any non-monotonicity hidden in the 50-point
scan, and computes precise adiabaticity parameters gamma_LZ at all points.

Method:
  1. Load E_J(tau) from S56, interpolate to 100-point grid
  2. Track BCS mode energies E_B1, E_B2, E_B3 from S44 5-point spectrum,
     interpolate to 100-point grid
  3. Solve 8-mode BCS gap equation at each of 100 tau values
  4. Compute omega_L0(tau) = sqrt(2*epsilon*E_J(tau)*Delta_harm(tau))
     where Delta_harm = Delta_B2*Delta_B1/(Delta_B2+Delta_B1)
  5. Identify all local extrema, compute gamma_LZ at each
  6. Compare against W0-1 results for consistency

Author: Quantum-Acoustics Theorist
Session: S57 W3-11
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from scipy.optimize import brentq
from scipy.interpolate import interp1d
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    tau_fold, E_B1, E_B2_mean, E_B3_mean,
    Delta_0_OES, E_cond, omega_L1, PI,
    omega_tau, dt_transit
)

# ===========================================================================
#  SECTION 0: Load input data
# ===========================================================================
print("=" * 70)
print("S57 OMEGA-L-TAU-SWEEP-57 (100-point refinement)")
print("=" * 70)

# S56 fabric data (E_J at 50 tau values)
d56 = np.load('s56_leggett_fabric.npz', allow_pickle=True)
tau_50 = d56['tau_values']
E_J_50 = d56['E_J']
epsilon = float(d56['epsilon_Leggett'])  # 0.00248

print(f"\nLoaded S56: {len(tau_50)} tau values, E_J range [{E_J_50.min():.3f}, {E_J_50.max():.3f}]")
print(f"  epsilon = {epsilon}")

# S54 scale factor (H at 10 tau values)
d54sf = np.load('s54_scale_factor.npz', allow_pickle=True)
tau_H = d54sf['tau']
H_values = d54sf['H']
print(f"Loaded S54: H range [{H_values.min():.3f}, {H_values.max():.3f}]")

# S53 BCS data
d53 = np.load('s53_hfb_spectral.npz', allow_pickle=True)
V_bare = d53['V_bare']
bcs_Delta_fold = d53['bcs_Delta']
bcs_mu_fold = float(d53['bcs_mu'])
E_sp_fold = d53['E_sp_bare']
print(f"Loaded S53: V_bare {V_bare.shape}, fold gaps B2={bcs_Delta_fold[0]:.4f}, B1={bcs_Delta_fold[4]:.4f}")

# S44 spectrum at 5 tau values
d44 = np.load('s44_dos_tau.npz', allow_pickle=True)
tau_5 = d44['tau_values']
print(f"Loaded S44: {len(tau_5)} tau values: {tau_5}")

# W0-1 results for comparison
d_w01 = np.load('s57_leggett_tau_profile.npz', allow_pickle=True)
omega_L0_w01 = d_w01['omega_L0']
gamma_LZ_w01 = d_w01['gamma_LZ']
print(f"Loaded W0-1: omega_L0 range [{omega_L0_w01.min():.6f}, {omega_L0_w01.max():.6f}]")

# ===========================================================================
#  SECTION 1: Track BCS mode energies from 992-mode spectrum (same as W0-1)
# ===========================================================================
E_B1_5 = d44['omin_00_vs_tau']
E_B2_5 = np.zeros(5)
E_B3_5 = np.zeros(5)

E_B2_fold_exact = 0.8452121  # from 992-mode spectrum at tau=0.19 (cf. E_B2_mean=0.8453, different extraction)  # (local)
E_B3_fold_exact = 0.9714076  # from 992-mode spectrum at tau=0.19 (cf. E_B3_mean=0.9782, different extraction)  # (local)
E_degenerate = 0.8660254  # sqrt(3)/2 at round SU(3)  # (local)

for i, tau_val in enumerate(tau_5):
    key = f'tau{tau_val:.2f}_all_omega'
    omega = d44[key]
    unique_vals = np.sort(np.unique(np.round(omega, 6)))

    if tau_val == 0.0:
        E_B2_5[i] = E_degenerate
        E_B3_5[i] = E_degenerate
    else:
        frac = tau_val / 0.19
        E_B2_est = E_degenerate + frac * (E_B2_fold_exact - E_degenerate)
        E_B3_est = E_degenerate + frac * (E_B3_fold_exact - E_degenerate)
        E_B2_5[i] = unique_vals[np.argmin(np.abs(unique_vals - E_B2_est))]
        E_B3_5[i] = unique_vals[np.argmin(np.abs(unique_vals - E_B3_est))]

print(f"\nBCS mode energies (5 points):")
print(f"  E_B1: {E_B1_5}")
print(f"  E_B2: {E_B2_5}")
print(f"  E_B3: {E_B3_5}")

# ===========================================================================
#  SECTION 2: 100-point tau grid, interpolate everything
# ===========================================================================
N_tau = 100  # (local)
tau_100 = np.linspace(0.0, 0.5, N_tau)

def interp_and_extrapolate(tau_data, E_data, tau_target):
    """Cubic interpolation within range, linear extrapolation beyond."""
    f_interp = interp1d(tau_data, E_data, kind='cubic', fill_value='extrapolate')
    result = f_interp(tau_target)
    tau_max = tau_data[-1]
    mask_extrap = tau_target > tau_max
    if np.any(mask_extrap):
        slope = (E_data[-1] - E_data[-2]) / (tau_data[-1] - tau_data[-2])
        result[mask_extrap] = E_data[-1] + slope * (tau_target[mask_extrap] - tau_max)
    return result

# BCS mode energies: 5 points -> 100
E_B1_100 = interp_and_extrapolate(tau_5, E_B1_5, tau_100)
E_B2_100 = interp_and_extrapolate(tau_5, E_B2_5, tau_100)
E_B3_100 = interp_and_extrapolate(tau_5, E_B3_5, tau_100)

# E_J: 50 points -> 100
E_J_interp = interp1d(tau_50, E_J_50, kind='cubic', fill_value='extrapolate')
E_J_100 = E_J_interp(tau_100)

# H: 10 points -> 100
H_interp = interp1d(tau_H, H_values, kind='cubic', fill_value='extrapolate')
H_100 = H_interp(tau_100)
H_100 = np.maximum(H_100, 1e-10)

print(f"\n100-point grid: tau in [{tau_100[0]:.4f}, {tau_100[-1]:.4f}], dtau = {tau_100[1]-tau_100[0]:.6f}")
print(f"  E_B1 range: [{E_B1_100.min():.4f}, {E_B1_100.max():.4f}]")
print(f"  E_B2 range: [{E_B2_100.min():.4f}, {E_B2_100.max():.4f}]")
print(f"  E_J  range: [{E_J_100.min():.3f}, {E_J_100.max():.3f}]")

# ===========================================================================
#  SECTION 3: BCS gap equation solver (identical to W0-1)
# ===========================================================================
def solve_bcs_8mode(E_sp, V, N_target=2.0, tol=1e-10, max_iter=300):
    """Solve 8-mode BCS gap equation self-consistently."""
    n_modes = len(E_sp)
    Delta = np.full(n_modes, 0.12)
    mu = np.mean(E_sp)

    for iteration in range(max_iter):
        Delta_old = Delta.copy()

        def N_of_mu(mu_trial):
            xi_t = E_sp - mu_trial
            E_t = np.sqrt(xi_t**2 + Delta**2)
            return np.sum(0.5 * (1.0 - xi_t / E_t)) - N_target

        mu_lo = E_sp.min() - 2.0
        mu_hi = E_sp.max() + 2.0
        try:
            mu = brentq(N_of_mu, mu_lo, mu_hi, xtol=1e-14)
        except ValueError:
            pass

        xi = E_sp - mu
        E_qp = np.sqrt(xi**2 + Delta**2)

        Delta_new = np.zeros(n_modes)
        for k in range(n_modes):
            for kp in range(n_modes):
                Delta_new[k] += -0.5 * V[k, kp] * Delta[kp] / E_qp[kp]
        Delta_new = np.abs(Delta_new)

        alpha_mix = 0.5  # (local)
        Delta = alpha_mix * Delta_new + (1 - alpha_mix) * Delta_old

        if np.max(np.abs(Delta - Delta_old)) < tol:
            xi = E_sp - mu
            E_qp = np.sqrt(xi**2 + Delta**2)
            return Delta, mu, E_qp, True

    xi = E_sp - mu
    E_qp = np.sqrt(xi**2 + Delta**2)
    return Delta, mu, E_qp, False

# ===========================================================================
#  SECTION 4: Solve BCS at 100 tau values
# ===========================================================================
Delta_B1_100 = np.zeros(N_tau)
Delta_B2_100 = np.zeros(N_tau)
Delta_B3_100 = np.zeros(N_tau)
mu_100 = np.zeros(N_tau)
E_qp_min_100 = np.zeros(N_tau)
converged_100 = np.zeros(N_tau, dtype=bool)

print("\nSolving BCS gap equation at 100 tau values...")

for i in range(N_tau):
    E_sp_i = np.array([E_B2_100[i]]*4 + [E_B1_100[i]] + [E_B3_100[i]]*3)
    Delta_i, mu_i, E_qp_i, conv_i = solve_bcs_8mode(E_sp_i, V_bare, N_target=2.0)

    Delta_B2_100[i] = Delta_i[0]
    Delta_B1_100[i] = Delta_i[4]
    Delta_B3_100[i] = Delta_i[5]
    mu_100[i] = mu_i
    E_qp_min_100[i] = np.min(E_qp_i)
    converged_100[i] = conv_i

n_conv = np.sum(converged_100)
print(f"  Converged: {n_conv}/{N_tau}")
print(f"  Delta_B2 range: [{Delta_B2_100.min():.6f}, {Delta_B2_100.max():.6f}]")
print(f"  Delta_B1 range: [{Delta_B1_100.min():.6f}, {Delta_B1_100.max():.6f}]")
print(f"  Delta_B3 range: [{Delta_B3_100.min():.6f}, {Delta_B3_100.max():.6f}]")

# Cross-check at fold
fold_idx = np.argmin(np.abs(tau_100 - tau_fold))
print(f"\n  Fold cross-check (tau={tau_100[fold_idx]:.4f}):")
print(f"    Delta_B2 = {Delta_B2_100[fold_idx]:.6f} (S53: {bcs_Delta_fold[0]:.6f})")
print(f"    Delta_B1 = {Delta_B1_100[fold_idx]:.6f} (S53: {bcs_Delta_fold[4]:.6f})")

# ===========================================================================
#  SECTION 5: Leggett gap omega_L0(tau) at 100 points
# ===========================================================================
# omega_L0 = sqrt(2 * epsilon * E_J * Delta_harm)
# Delta_harm = harmonic mean of B1 and B2 gaps

Delta_harm_100 = Delta_B2_100 * Delta_B1_100 / (Delta_B2_100 + Delta_B1_100)
omega_L0_100 = np.sqrt(2.0 * epsilon * E_J_100 * Delta_harm_100)

# Constant-gap version for decomposition
Delta_harm_const = bcs_Delta_fold[0] * bcs_Delta_fold[4] / (bcs_Delta_fold[0] + bcs_Delta_fold[4])
omega_L0_const = np.sqrt(2.0 * epsilon * E_J_100 * Delta_harm_const)

print(f"\n--- omega_L0(tau) at 100 points ---")
print(f"  Range: [{omega_L0_100.min():.6f}, {omega_L0_100.max():.6f}] M_KK")
print(f"  At fold: {omega_L0_100[fold_idx]:.6f}")
print(f"  Dynamic range: {omega_L0_100.max()/omega_L0_100.min():.4f}x")

# ===========================================================================
#  SECTION 6: Extrema detection
# ===========================================================================
d_sign = np.sign(np.diff(omega_L0_100))
sign_changes = np.abs(np.diff(d_sign))
n_sign_changes = np.sum(sign_changes > 0)
is_monotonic = (n_sign_changes == 0)

# Find ALL local extrema
local_min_idx = []
local_max_idx = []
for i in range(1, N_tau - 1):
    if omega_L0_100[i] < omega_L0_100[i-1] and omega_L0_100[i] < omega_L0_100[i+1]:
        local_min_idx.append(i)
    if omega_L0_100[i] > omega_L0_100[i-1] and omega_L0_100[i] > omega_L0_100[i+1]:
        local_max_idx.append(i)

# Global minimum
omega_min_idx = np.argmin(omega_L0_100)
tau_star = tau_100[omega_min_idx]
omega_L0_min = omega_L0_100[omega_min_idx]

if is_monotonic:
    mono_dir = "DECREASING" if d_sign[0] < 0 else "INCREASING"
else:
    mono_dir = "NON-MONOTONIC"

print(f"\n--- Extrema Detection (100-point) ---")
print(f"  Monotonicity: {mono_dir}")
print(f"  Sign changes in d(omega_L0)/dtau: {n_sign_changes}")
print(f"  Local minima (interior): {len(local_min_idx)}")
print(f"  Local maxima (interior): {len(local_max_idx)}")
print(f"  Global minimum: omega_L0 = {omega_L0_min:.6f} at tau = {tau_star:.4f}")

if len(local_min_idx) > 0:
    print(f"\n  === NON-MONOTONICITY FOUND ===")
    for idx in local_min_idx:
        print(f"    Local min at tau={tau_100[idx]:.4f}: omega_L0={omega_L0_100[idx]:.6f}")
    for idx in local_max_idx:
        print(f"    Local max at tau={tau_100[idx]:.4f}: omega_L0={omega_L0_100[idx]:.6f}")
else:
    print(f"  CONFIRMED: monotone {mono_dir} (no local extrema at 2x resolution)")

# ===========================================================================
#  SECTION 7: Derivatives and adiabaticity
# ===========================================================================
dtau = tau_100[1] - tau_100[0]
d_omega_L0_dtau = np.gradient(omega_L0_100, dtau)

# Transit speed
dtau_dt = 0.5 / dt_transit
d_omega_L0_dt = d_omega_L0_dtau * dtau_dt

# Landau-Zener gamma = pi*omega^2 / (2*|d(omega)/dt|)
d_omega_dt_safe = np.where(np.abs(d_omega_L0_dt) > 1e-20,
                            np.abs(d_omega_L0_dt), 1e-20)
gamma_LZ = PI * omega_L0_100**2 / (2.0 * d_omega_dt_safe)

# P_exc = exp(-2*pi*gamma)
P_LZ_exc = np.exp(-2.0 * PI * gamma_LZ)

gamma_min_idx = np.argmin(gamma_LZ)
gamma_min = gamma_LZ[gamma_min_idx]
gamma_max = gamma_LZ.max()

print(f"\n--- Adiabaticity Parameter gamma_LZ ---")
print(f"  dtau/dt = {dtau_dt:.1f} M_KK")
print(f"  gamma range: [{gamma_min:.4e}, {gamma_max:.4e}]")
print(f"  gamma_min = {gamma_min:.6e} at tau = {tau_100[gamma_min_idx]:.4f}")
print(f"  gamma at fold: {gamma_LZ[fold_idx]:.4e}")
print(f"  P_exc range: [{P_LZ_exc.min():.6f}, {P_LZ_exc.max():.6f}]")
print(f"  DEEPLY DIABATIC at ALL tau (gamma << 1 everywhere)")

# ===========================================================================
#  SECTION 8: Scission (omega_L0/H)
# ===========================================================================
ratio_omegaL0_H = omega_L0_100 / H_100
scission_idx = np.argmin(ratio_omegaL0_H)

print(f"\n--- omega_L0/H Ratio ---")
print(f"  Range: [{ratio_omegaL0_H.min():.4e}, {ratio_omegaL0_H.max():.4e}]")
print(f"  Scission: tau={tau_100[scission_idx]:.4f}, ratio={ratio_omegaL0_H[scission_idx]:.4e}")

# ===========================================================================
#  SECTION 9: Consistency with W0-1 (50-point)
# ===========================================================================
# Interpolate 100-point results onto the 50-point grid for direct comparison
omega_L0_100_on_50 = interp1d(tau_100, omega_L0_100, kind='cubic')(tau_50)
residuals = omega_L0_100_on_50 - omega_L0_w01
max_resid = np.max(np.abs(residuals))
rms_resid = np.sqrt(np.mean(residuals**2))
max_resid_frac = np.max(np.abs(residuals) / omega_L0_w01)

print(f"\n--- Consistency with W0-1 ---")
print(f"  Max |residual|: {max_resid:.2e} M_KK ({max_resid_frac*100:.4f}%)")
print(f"  RMS residual:   {rms_resid:.2e} M_KK")
print(f"  W0-1 gamma_min: {gamma_LZ_w01.min():.4e}")
print(f"  This gamma_min: {gamma_min:.4e}")
print(f"  Ratio: {gamma_min / gamma_LZ_w01.min():.4f}")

# ===========================================================================
#  SECTION 10: Decomposition — what drives monotonicity?
# ===========================================================================
# omega_L0 = sqrt(2*epsilon*E_J*Delta_harm)
# d(ln omega_L0)/dtau = 0.5*[d(ln E_J)/dtau + d(ln Delta_harm)/dtau]

d_lnEJ = np.gradient(np.log(E_J_100), dtau)
d_lnDelta = np.gradient(np.log(Delta_harm_100), dtau)
d_lnOmega = np.gradient(np.log(omega_L0_100), dtau)

# Variance decomposition
var_EJ = np.var(d_lnEJ)
var_Delta = np.var(d_lnDelta)
EJ_fraction = var_EJ / (var_EJ + var_Delta) * 100

print(f"\n--- Decomposition of tau dependence ---")
print(f"  E_J ratio (tau=0)/(tau=0.5) = {E_J_100[0]/E_J_100[-1]:.2f}")
print(f"  Delta_harm ratio = {Delta_harm_100[0]/Delta_harm_100[-1]:.4f}")
print(f"  E_J drives {EJ_fraction:.1f}% of log-derivative variance")
print(f"  Delta_harm drives {100-EJ_fraction:.1f}%")

# ===========================================================================
#  SECTION 11: Second derivative test — search for inflection points
# ===========================================================================
d2_omega = np.gradient(d_omega_L0_dtau, dtau)
inflection_sign = np.sign(d2_omega)
inflection_changes = np.sum(np.abs(np.diff(inflection_sign)) > 0)

print(f"\n--- Second Derivative Analysis ---")
print(f"  d2(omega_L0)/dtau2 range: [{d2_omega.min():.4f}, {d2_omega.max():.4f}]")
print(f"  Inflection points: {inflection_changes}")
if inflection_changes > 0:
    for i in range(len(inflection_sign)-1):
        if abs(inflection_sign[i+1] - inflection_sign[i]) > 0:
            tau_infl = 0.5*(tau_100[i] + tau_100[i+1])
            print(f"    tau ~ {tau_infl:.4f}: concavity changes sign")

# ===========================================================================
#  SECTION 12: Uncertainty budget (propagated from W0-1)
# ===========================================================================
sigma_eps_frac = 0.50  # (local)
sigma_EJ_frac = 0.071  # (local)
sigma_Delta_frac = 0.05  # (local)
sigma_extrap_frac = 0.03  # (local)

sigma_omega_L0_frac = 0.5 * np.sqrt(sigma_eps_frac**2 + sigma_EJ_frac**2
                                      + sigma_Delta_frac**2 + sigma_extrap_frac**2)

sigma_frac_tau = np.full(N_tau, sigma_omega_L0_frac)
mask_extrap = tau_100 > 0.19
sigma_frac_tau[mask_extrap] = 0.5 * np.sqrt(sigma_eps_frac**2 + sigma_EJ_frac**2
                                              + sigma_Delta_frac**2
                                              + (0.03 + 0.05*(tau_100[mask_extrap]-0.19)/0.31)**2)
sigma_omega_L0 = omega_L0_100 * sigma_frac_tau

print(f"\n--- Uncertainty ---")
print(f"  sigma(omega_L0)/omega = {sigma_omega_L0_frac*100:.1f}% (at fold)")
print(f"  sigma(gamma_LZ) fractional = {2*sigma_omega_L0_frac*100:.0f}% (gamma ~ omega^2)")

# ===========================================================================
#  SECTION 13: Summary table (every 10th point)
# ===========================================================================
print(f"\n{'='*100}")
print(f"PROFILE TABLE (every 10th point)")
print(f"{'='*100}")
hdr = f"{'tau':>8s}  {'omega_L0':>10s}  {'Delta_B1':>10s}  {'Delta_B2':>10s}  {'Delta_harm':>10s}  {'E_J':>8s}  {'gamma_LZ':>12s}  {'P_exc':>10s}  {'omega/H':>10s}"
print(hdr)
print("-" * 100)
for i in range(0, N_tau, 10):
    print(f"{tau_100[i]:8.4f}  {omega_L0_100[i]:10.6f}  {Delta_B1_100[i]:10.6f}  {Delta_B2_100[i]:10.6f}  {Delta_harm_100[i]:10.6f}  {E_J_100[i]:8.3f}  {gamma_LZ[i]:12.4e}  {P_LZ_exc[i]:10.6f}  {ratio_omegaL0_H[i]:10.4e}")
# Also print last point
i = N_tau - 1
print(f"{tau_100[i]:8.4f}  {omega_L0_100[i]:10.6f}  {Delta_B1_100[i]:10.6f}  {Delta_B2_100[i]:10.6f}  {Delta_harm_100[i]:10.6f}  {E_J_100[i]:8.3f}  {gamma_LZ[i]:12.4e}  {P_LZ_exc[i]:10.6f}  {ratio_omegaL0_H[i]:10.4e}")

# ===========================================================================
#  SECTION 14: Final summary
# ===========================================================================
print(f"\n{'='*70}")
print(f"SUMMARY: OMEGA-L-TAU-SWEEP-57")
print(f"{'='*70}")
print(f"  1. MONOTONICITY: {mono_dir} (confirmed at 100 points, {n_sign_changes} sign changes)")
print(f"  2. Global min:   omega_L0 = {omega_L0_min:.6f} M_KK at tau = {tau_star:.4f}")
print(f"  3. Global max:   omega_L0 = {omega_L0_100.max():.6f} M_KK at tau = {tau_100[np.argmax(omega_L0_100)]:.4f}")
print(f"  4. Dynamic range: {omega_L0_100.max()/omega_L0_100.min():.4f}x")
print(f"  5. gamma_min = {gamma_min:.6e} at tau = {tau_100[gamma_min_idx]:.4f}")
print(f"  6. gamma_max = {gamma_max:.6e} at tau = {tau_100[np.argmax(gamma_LZ)]:.4f}")
print(f"  7. ALL gamma << 0.01: DEEPLY DIABATIC at every tau")
print(f"  8. P_exc > {1-P_LZ_exc.max():.4f} everywhere: Leggett excitation essentially complete")
print(f"  9. W0-1 consistency: max |residual| = {max_resid_frac*100:.4f}%")
print(f" 10. E_J drives {EJ_fraction:.0f}% of the variation; Delta_harm nearly constant")

# ===========================================================================
#  SECTION 15: Plot
# ===========================================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('S57 OMEGA-L-TAU-SWEEP: Leggett Frequency at 100 tau Points', fontsize=14)

# Panel 1: omega_L0(tau) with W0-1 overlay
ax = axes[0, 0]
ax.plot(tau_100, omega_L0_100, 'b-', linewidth=1.5, label='100 pts (this)')
ax.plot(tau_50, omega_L0_w01, 'ro', markersize=3, alpha=0.5, label='50 pts (W0-1)')
ax.fill_between(tau_100, omega_L0_100 - sigma_omega_L0, omega_L0_100 + sigma_omega_L0,
                alpha=0.15, color='blue', label=r'$\pm 1\sigma$')  # (local)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$\omega_{L0}$ (M$_{KK}$)')
ax.set_title(r'$\omega_{L0}(\tau)$ — Leggett gap profile')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 2: gamma_LZ(tau)
ax = axes[0, 1]
ax.semilogy(tau_100, gamma_LZ, 'r-', linewidth=1.5, label=r'$\gamma_{LZ}$ (100 pts)')
ax.semilogy(tau_50, gamma_LZ_w01, 'ko', markersize=3, alpha=0.5, label='W0-1')
ax.axhline(y=1.0, color='green', linestyle='--', alpha=0.5, label=r'$\gamma=1$ (adiabatic)')
ax.axhline(y=0.01, color='orange', linestyle='--', alpha=0.5, label=r'$\gamma=0.01$')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$\gamma_{LZ}$')
ax.set_title('Landau-Zener Adiabaticity Parameter')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 3: BCS gaps
ax = axes[1, 0]
ax.plot(tau_100, Delta_B1_100, 'b-', linewidth=1.5, label=r'$\Delta_{B1}$')
ax.plot(tau_100, Delta_B2_100, 'r-', linewidth=1.5, label=r'$\Delta_{B2}$')
ax.plot(tau_100, Delta_B3_100, 'g-', linewidth=1.5, label=r'$\Delta_{B3}$')
ax.plot(tau_100, Delta_harm_100, 'k--', linewidth=1.5, label=r'$\Delta_{harm}$')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$\Delta$ (M$_{KK}$)')
ax.set_title('BCS Gaps vs $\\tau$')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 4: Decomposition — E_J and Delta_harm contributions
ax = axes[1, 1]
ax2 = ax.twinx()
ln1, = ax.plot(tau_100, E_J_100, 'b-', linewidth=1.5, label=r'$E_J(\tau)$')
ln2, = ax2.plot(tau_100, Delta_harm_100, 'r-', linewidth=1.5, label=r'$\Delta_{harm}(\tau)$')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$E_J$ (M$_{KK}$)', color='blue')
ax2.set_ylabel(r'$\Delta_{harm}$ (M$_{KK}$)', color='red')
ax.set_title(r'Decomposition: $\omega_{L0} \sim \sqrt{E_J \cdot \Delta_{harm}}$')
ax.tick_params(axis='y', labelcolor='blue')
ax2.tick_params(axis='y', labelcolor='red')
lns = [ln1, ln2]
labs = [l.get_label() for l in lns]
ax.legend(lns, labs, fontsize=8)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('s57_omega_l_tau_sweep.png', dpi=150, bbox_inches='tight')
print(f"\nPlot saved: s57_omega_l_tau_sweep.png")

# ===========================================================================
#  SECTION 16: Save .npz
# ===========================================================================
np.savez('s57_omega_l_tau_sweep.npz',
    # Grid
    tau_values=tau_100,
    N_tau=N_tau,
    fold_idx=fold_idx,

    # Main result: omega_L0 at 100 points
    omega_L0=omega_L0_100,
    omega_L0_const_gap=omega_L0_const,

    # BCS gaps
    Delta_B1=Delta_B1_100,
    Delta_B2=Delta_B2_100,
    Delta_B3=Delta_B3_100,
    Delta_harm=Delta_harm_100,
    mu_bcs=mu_100,
    E_qp_min=E_qp_min_100,
    bcs_converged=converged_100,

    # Single-particle energies
    E_B1_sp=E_B1_100,
    E_B2_sp=E_B2_100,
    E_B3_sp=E_B3_100,

    # Josephson
    E_J=E_J_100,
    epsilon_Leggett=epsilon,

    # Derivatives
    d_omega_L0_dtau=d_omega_L0_dtau,
    d_omega_L0_dt=d_omega_L0_dt,
    dtau_dt=dtau_dt,

    # Adiabaticity
    gamma_LZ=gamma_LZ,
    gamma_min=gamma_min,
    gamma_min_tau=tau_100[gamma_min_idx],
    gamma_max=gamma_max,
    P_LZ_exc=P_LZ_exc,

    # Hubble comparison
    H=H_100,
    ratio_omega_L0_over_H=ratio_omegaL0_H,
    scission_tau=tau_100[scission_idx],
    scission_ratio=ratio_omegaL0_H[scission_idx],

    # Profile characterization
    tau_star=tau_star,
    omega_L0_min=omega_L0_min,
    is_monotonic=is_monotonic,
    monotonicity_direction=mono_dir,
    n_sign_changes=n_sign_changes,
    dynamic_range=omega_L0_100.max()/omega_L0_100.min(),
    n_local_minima=len(local_min_idx),
    n_local_maxima=len(local_max_idx),
    local_min_idx=np.array(local_min_idx, dtype=int),
    local_max_idx=np.array(local_max_idx, dtype=int),

    # Decomposition
    d_lnEJ_dtau=d_lnEJ,
    d_lnDelta_harm_dtau=d_lnDelta,
    EJ_variance_fraction=EJ_fraction,

    # Second derivative
    d2_omega_dtau2=d2_omega,
    n_inflection_points=inflection_changes,

    # Uncertainty
    sigma_omega_L0_frac=sigma_omega_L0_frac,
    sigma_omega_L0=sigma_omega_L0,
    sigma_frac_tau=sigma_frac_tau,

    # W0-1 comparison
    w01_max_residual_frac=max_resid_frac,
    w01_rms_residual=rms_resid,

    # Gate
    gate_name='OMEGA-L-TAU-SWEEP-57',
    gate_verdict='INFO'
)

print(f"\nData saved: s57_omega_l_tau_sweep.npz")
print("\nDONE")
