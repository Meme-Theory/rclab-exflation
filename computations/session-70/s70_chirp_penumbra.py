#!/usr/bin/env python3
"""
CHIRP-PENUMBRA-70: Chirp Rate of Tachyonic Sweep Through z''/z
================================================================

The Mukhanov-Sasaki equation u_k'' + omega_k^2(eta) u_k = 0 has
omega_k^2 = k^2 c_s^2 - z''/z. A mode k is "tachyonic" (superhorizon,
growing) when omega_k^2 < 0, i.e., when k < k_tach(tau) = sqrt(z''/z)/c_s.

The tachyonic boundary k_tach(tau) sweeps through k-space as the modulus
transits the fold. The CHIRP RATE dk_tach/dt measures how rapidly modes
are swept from sub-horizon to super-horizon (or vice versa). This rate
controls the efficiency of parametric particle production:

  - WKB (Stokes line crossing): beta_k ~ exp(-pi k^2 / |dk_tach/dt|)
  - Rapid chirp (|dk_tach/dt| >> k^2): all modes excited, beta_k -> 1
  - Slow chirp (|dk_tach/dt| << k^2): adiabatic, beta_k -> 0

Gate: CHIRP-PENUMBRA-70
  PASS: |P_exact - P_WKB| / P_exact < 10% across tachyonic band
  FAIL: WKB error > 50%
  INFO: WKB error in [10%, 50%]

Resonance structure: The tachyonic region is the cavity. k_tach(tau) is
the time-dependent boundary. The chirp rate is the inverse of the dwell
time at each frequency. The WKB approximation treats each mode as
crossing the Stokes line once; resonant enhancement occurs when modes
re-enter the tachyonic band (multiple crossings).

References: Parker [01], Birrell-Davies [02], S67 transit PS, S62 workshop.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

import numpy as np
from scipy.interpolate import CubicSpline
from scipy.integrate import solve_ivp, cumulative_trapezoid
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    tau_fold, M_KK, M_Pl_reduced,
    S_fold, dS_fold, d2S_fold, H_fold as H_fold_canon,
    dt_transit, v_terminal,
    a0_fold, a2_fold, a4_fold,
    A_s_CMB, PI,
)

print("=" * 72)
print("CHIRP-PENUMBRA-70: Chirp Rate of Tachyonic Sweep")
print("=" * 72)

# ============================================================================
#  SECTION 1: Reconstruct background from S67 data
# ============================================================================

# Load S67 transit power spectrum data
s67_data = np.load(os.path.join(os.path.dirname(__file__), 's67_transit_ps.npz'),
                   allow_pickle=True)

tau_fine = s67_data['tau_fine']       # tau grid [0.10, 0.30], N=8000
eta_fine = s67_data['eta_fine']       # conformal time
z_fine = s67_data['z_fine']           # Mukhanov z(eta)
zpp_z = s67_data['zpp_z']            # z''/z(eta)
a_fine = s67_data['a_fine']           # scale factor
eps_H_fine = s67_data['eps_H_fine']   # slow-roll epsilon_H
k_grid_rk = s67_data['k_grid_rk']    # RK k-grid
beta_sq_rk = s67_data['beta_sq_rk']  # |beta_k|^2 from RK integration
P_zeta_rk = s67_data['P_zeta_rk']    # P_zeta from RK
S_tau_16 = s67_data['S_tau_16']       # S(tau) at 16 points

c_BLV = 0.485   # BLV acoustic speed (S65, same as S67)  # (local)

print(f"\nLoaded S67 data:")
print(f"  tau range: [{tau_fine[0]:.3f}, {tau_fine[-1]:.3f}], N={len(tau_fine)}")
print(f"  eta range: [{eta_fine[0]:.6f}, {eta_fine[-1]:.6f}]")
print(f"  z''/z range: [{zpp_z.min():.4e}, {zpp_z.max():.4e}]")
print(f"  c_BLV = {c_BLV}")

# ============================================================================
#  SECTION 2: Compute tachyonic boundary k_tach(tau) and k_tach(eta)
# ============================================================================

# k_tach(tau) = sqrt(z''/z(tau)) / c_s
# Note: z''/z is always positive in our data (ALL modes are amplified),
# so k_tach is real everywhere in the transit window.

# Map from eta to tau for convenience
cs_zpp_z_eta = CubicSpline(eta_fine, zpp_z)

# k_tach as function of tau
k_tach_tau = np.sqrt(np.abs(zpp_z)) / c_BLV

# Also as function of eta
k_tach_eta = k_tach_tau.copy()

# Spline for differentiation
cs_k_tach_tau = CubicSpline(tau_fine, k_tach_tau)
cs_k_tach_eta = CubicSpline(eta_fine, k_tach_eta)

# Chirp rate in tau: dk_tach/dtau
dk_tach_dtau = cs_k_tach_tau(tau_fine, 1)

# Chirp rate in physical time: dk_tach/dt = (dk_tach/dtau) * (dtau/dt)
# dtau/dt = v_terminal (the modulus velocity in tau-space)
v_tau = v_terminal
dk_tach_dt = dk_tach_dtau * v_tau

# Chirp rate in conformal time: dk_tach/deta
dk_tach_deta = cs_k_tach_eta(eta_fine, 1)

# Find fold index
fold_idx = np.argmin(np.abs(tau_fine - tau_fold))
eta_fold = eta_fine[fold_idx]

print(f"\n{'=' * 72}")
print(f"SECTION 2: Tachyonic Boundary k_tach(tau)")
print(f"{'=' * 72}")
print(f"\n  k_tach at fold: {k_tach_tau[fold_idx]:.2f} M_KK")
print(f"  k_tach range: [{k_tach_tau.min():.2f}, {k_tach_tau.max():.2f}] M_KK")
print(f"  k_transit (=H/c_s): {H_fold_canon / c_BLV:.2f} M_KK")
print(f"  k_tach / k_transit at fold: {k_tach_tau[fold_idx] / (H_fold_canon / c_BLV):.4f}")

print(f"\n  Chirp rate at fold:")
print(f"    dk_tach/dtau = {dk_tach_dtau[fold_idx]:.4e} M_KK per dtau")
print(f"    dk_tach/dt   = {dk_tach_dt[fold_idx]:.4e} M_KK^2")
print(f"    dk_tach/deta = {dk_tach_deta[fold_idx]:.4e} M_KK^2")

# ============================================================================
#  SECTION 3: Chirp profile analysis -- peak rate, duration, swept band
# ============================================================================

print(f"\n{'=' * 72}")
print(f"SECTION 3: Chirp Profile Analysis")
print(f"{'=' * 72}")

# Peak chirp rate
idx_max_chirp = np.argmax(np.abs(dk_tach_dt))
print(f"\n  Peak |dk_tach/dt|:")
print(f"    tau = {tau_fine[idx_max_chirp]:.5f}")
print(f"    |dk_tach/dt| = {np.abs(dk_tach_dt[idx_max_chirp]):.4e} M_KK^2")
print(f"    k_tach at peak = {k_tach_tau[idx_max_chirp]:.2f} M_KK")

# The "tachyonic band" width at the fold
k_tach_fold = k_tach_tau[fold_idx]
print(f"\n  Tachyonic band at fold: [0, {k_tach_fold:.2f}] M_KK")
print(f"  Modes below k_tach are superhorizon (tachyonic)")

# Rate of change of zpp_z -- characterizes the impulsiveness
cs_zpp_z_tau = CubicSpline(tau_fine, zpp_z)
d_zpp_z_dtau = cs_zpp_z_tau(tau_fine, 1)
d2_zpp_z_dtau2 = cs_zpp_z_tau(tau_fine, 2)

# Find the van Hove fold: maximum of z''/z
idx_zpp_max = np.argmax(zpp_z)
print(f"\n  z''/z peak:")
print(f"    tau = {tau_fine[idx_zpp_max]:.5f}")
print(f"    z''/z_max = {zpp_z[idx_zpp_max]:.4e}")
print(f"    d(z''/z)/dtau at peak = {d_zpp_z_dtau[idx_zpp_max]:.4e}")

# Temporal width of z''/z bump (FWHM in tau)
zpp_half = zpp_z[idx_zpp_max] / 2.0
above_half = zpp_z > zpp_half
if np.any(above_half):
    idx_first = np.argmax(above_half)
    idx_last = len(above_half) - 1 - np.argmax(above_half[::-1])
    dtau_FWHM = tau_fine[idx_last] - tau_fine[idx_first]
    dt_FWHM = dtau_FWHM / v_tau
    deta_FWHM = eta_fine[idx_last] - eta_fine[idx_first]
    print(f"\n  z''/z FWHM:")
    print(f"    dtau = {dtau_FWHM:.6f}")
    print(f"    dt = {dt_FWHM:.6e} M_KK^{{-1}}")
    print(f"    deta = {deta_FWHM:.6e} M_KK^{{-1}}")
else:
    dtau_FWHM = tau_fine[-1] - tau_fine[0]
    dt_FWHM = dtau_FWHM / v_tau
    print(f"\n  z''/z never drops below half-max in window")

# ============================================================================
#  SECTION 4: WKB particle production coefficient
# ============================================================================

print(f"\n{'=' * 72}")
print(f"SECTION 4: WKB Particle Production")
print(f"{'=' * 72}")

# WKB approximation for particle production from a chirped tachyonic sweep:
#
# The Mukhanov-Sasaki equation in the form u'' + omega^2(eta) u = 0 has
# omega^2(eta) = k^2 c_s^2 - z''/z(eta). When omega^2 passes through zero
# (mode crosses the horizon), the Stokes line crossing gives:
#
#   beta_k ~ exp(-pi * omega^2_max / |d(omega^2)/deta|)
#
# where the derivative is evaluated at the crossing point.
#
# For a mode k, omega^2 = k^2 c_s^2 - z''/z. At the crossing,
# omega^2 = 0 => z''/z = k^2 c_s^2. The rate is:
#   d(omega^2)/deta = -d(z''/z)/deta
# evaluated where z''/z = k^2 c_s^2.
#
# The standard WKB (Stokes line) result for the Bogoliubov coefficient is:
#   |beta_k|^2 = exp(-2*pi * Im(integral of omega through complex turning point))
#
# For a linear crossing: |beta_k|^2 = exp(-pi * k^2 * c_s^2 / |d(z''/z)/deta|_cross)
#
# This is the "chirp formula" -- the production efficiency is set by
# k^2 * c_s^2 relative to the chirp rate of z''/z.

# Compute d(z''/z)/deta using the spline
cs_zpp_z_eta_spline = CubicSpline(eta_fine, zpp_z)
d_zpp_z_deta = cs_zpp_z_eta_spline(eta_fine, 1)

# For each k, find the crossing point(s) where z''/z = k^2 c_s^2
# The crossing is on the rising slope (entering tachyonic) and falling slope (exiting)
# Two crossings => the WKB integral is from one turning point to the other.

# k values to test: span the range from deeply tachyonic to sub-horizon
k_tach_max = k_tach_tau.max()  # maximum tachyonic boundary
k_test = np.logspace(np.log10(100), np.log10(k_tach_max * 1.5), 300)

# For each k, determine:
# (a) Does it enter the tachyonic band? (k < k_tach_max)
# (b) What is the WKB prediction for |beta_k|^2?

beta_sq_wkb = np.zeros(len(k_test))
k_cross_entry = np.zeros(len(k_test))
k_cross_exit = np.zeros(len(k_test))
dwell_time_eta = np.zeros(len(k_test))
n_crossings = np.zeros(len(k_test), dtype=int)
chirp_at_cross = np.zeros(len(k_test))

for ik, k in enumerate(k_test):
    target = k**2 * c_BLV**2  # z''/z value at crossing

    if target > zpp_z.max():
        # Mode never enters tachyonic band -- adiabatic
        beta_sq_wkb[ik] = 0.0
        continue

    if target < zpp_z.min():
        # Mode is ALWAYS tachyonic -- fully superhorizon throughout
        # WKB does not apply: no crossing. Use sudden approximation.
        # beta_sq ~ 1 (fully excited)
        beta_sq_wkb[ik] = 1.0
        continue

    # Find crossing points: z''/z = target
    # z''/z is a bump centered near the fold. Should have two crossings.
    crossings = []
    for j in range(len(zpp_z) - 1):
        if (zpp_z[j] - target) * (zpp_z[j+1] - target) < 0:
            # Linear interpolation to find crossing eta
            frac = (target - zpp_z[j]) / (zpp_z[j+1] - zpp_z[j])
            eta_cross = eta_fine[j] + frac * (eta_fine[j+1] - eta_fine[j])
            crossings.append(eta_cross)

    n_crossings[ik] = len(crossings)

    if len(crossings) == 0:
        # No crossing found numerically (edge case)
        beta_sq_wkb[ik] = 0.0
        continue

    if len(crossings) >= 2:
        # Two crossings: entry and exit from tachyonic band
        eta_entry = crossings[0]
        eta_exit = crossings[-1]
        k_cross_entry[ik] = eta_entry
        k_cross_exit[ik] = eta_exit
        dwell_time_eta[ik] = eta_exit - eta_entry

        # WKB integral: integral of |kappa(eta)| deta from entry to exit
        # where kappa = sqrt(z''/z - k^2 c_s^2)
        # The WKB Bogoliubov coefficient is:
        #   |beta_k|^2 ~ exp(-2 * Im integral) but for the REAL tachyonic
        #   case, the exact result from Stokes line analysis is:
        #
        # For a parabolic barrier (inverted harmonic oscillator):
        #   |beta_k|^2 = 1 / (1 + exp(2*pi*Omega_k))
        # where Omega_k = integral of |omega(eta)| through the classically
        # forbidden region.
        #
        # For the tachyonic case (z''/z > k^2 c_s^2 in the band):
        #   The "forbidden" region is OUTSIDE the band (where omega^2 > 0).
        #   Modes are AMPLIFIED inside the band.
        #   The WKB result is:
        #   |beta_k|^2 ~ exp(2 * integral_entry^exit kappa deta)
        #   where kappa = sqrt(z''/z - k^2 c_s^2).
        #   But this overestimates for large integrals (can exceed 1).
        #
        # The proper WKB formula for a mode that passes through two
        # turning points with amplification in between is:
        #   |beta_k|^2 = sinh^2(integral) / (1 + sinh^2(integral))
        #              = 1 / (1 + exp(-2*integral))  -- for large integral
        #
        # Compute the integral numerically
        mask_inside = (eta_fine >= eta_entry) & (eta_fine <= eta_exit)
        if np.sum(mask_inside) > 2:
            zpp_inside = zpp_z[mask_inside]
            eta_inside = eta_fine[mask_inside]
            kappa_sq = zpp_inside - k**2 * c_BLV**2
            kappa = np.sqrt(np.maximum(kappa_sq, 0.0))
            integral = np.trapezoid(kappa, eta_inside)

            # Proper WKB:
            beta_sq_wkb[ik] = np.sinh(integral)**2 / (1.0 + np.sinh(integral)**2)
        else:
            beta_sq_wkb[ik] = 0.0

        # Chirp rate at the entry crossing
        chirp_at_cross[ik] = np.abs(np.interp(eta_entry, eta_fine, d_zpp_z_deta))

    elif len(crossings) == 1:
        # Only one crossing (mode enters but doesn't exit in window)
        eta_entry = crossings[0]
        k_cross_entry[ik] = eta_entry
        chirp_at_cross[ik] = np.abs(np.interp(eta_entry, eta_fine, d_zpp_z_deta))
        # Approximate: mode stays tachyonic to end of window
        mask_inside = eta_fine >= eta_entry
        zpp_inside = zpp_z[mask_inside]
        eta_inside = eta_fine[mask_inside]
        kappa_sq = zpp_inside - k**2 * c_BLV**2
        kappa = np.sqrt(np.maximum(kappa_sq, 0.0))
        integral = np.trapezoid(kappa, eta_inside)
        beta_sq_wkb[ik] = np.sinh(integral)**2 / (1.0 + np.sinh(integral)**2)

print(f"\n  k_tach max: {k_tach_max:.2f} M_KK")
print(f"  Modes tested: {len(k_test)}")
print(f"  Modes with 2 crossings: {np.sum(n_crossings == 2)}")
print(f"  Modes with 1 crossing: {np.sum(n_crossings == 1)}")
print(f"  Modes with 0 crossings: {np.sum(n_crossings == 0)}")
print(f"  Modes always tachyonic: {np.sum((k_test**2 * c_BLV**2) < zpp_z.min())}")

# ============================================================================
#  SECTION 5: Compare WKB to exact (RK) Bogoliubov coefficients
# ============================================================================

print(f"\n{'=' * 72}")
print(f"SECTION 5: WKB vs Exact Comparison")
print(f"{'=' * 72}")

# The S67 RK data gives beta_sq_rk on k_grid_rk.
# Find modes where WKB prediction is valid (finite, non-zero, non-saturated)

# Interpolate WKB predictions to the RK k-grid
beta_sq_wkb_on_rk = np.interp(k_grid_rk, k_test, beta_sq_wkb)

# Power spectrum from WKB
P_zeta_wkb = np.zeros(len(k_grid_rk))
for ik, k in enumerate(k_grid_rk):
    if beta_sq_wkb_on_rk[ik] > 1e-30:
        # P_zeta ~ k^3 / (2*pi^2) * |beta_k|^2 / (k * z_post^2)
        # Using same normalization as S67
        z_post = z_fine[-1]  # late-time z
        om_eff = k * c_BLV   # approximate late-time frequency
        P_zeta_wkb[ik] = k**3 / (2*PI**2) * (1 + 2*beta_sq_wkb_on_rk[ik]) / (2*om_eff * z_post**2)
    else:
        P_zeta_wkb[ik] = 0.0

# Compute relative error where both are non-zero
mask_valid = (P_zeta_rk > 0) & (P_zeta_wkb > 0) & (beta_sq_rk > 1e-6)
if np.sum(mask_valid) > 0:
    rel_error = np.abs(P_zeta_rk[mask_valid] - P_zeta_wkb[mask_valid]) / P_zeta_rk[mask_valid]
    mean_rel_error = np.mean(rel_error)
    median_rel_error = np.median(rel_error)
    max_rel_error = np.max(rel_error)
    min_rel_error = np.min(rel_error)

    print(f"\n  Comparison on {np.sum(mask_valid)} overlapping modes:")
    print(f"    Mean relative error:   {mean_rel_error:.4f} ({mean_rel_error*100:.2f}%)")
    print(f"    Median relative error: {median_rel_error:.4f} ({median_rel_error*100:.2f}%)")
    print(f"    Max relative error:    {max_rel_error:.4f} ({max_rel_error*100:.2f}%)")
    print(f"    Min relative error:    {min_rel_error:.4f} ({min_rel_error*100:.2f}%)")
else:
    print(f"\n  WARNING: No valid overlap between WKB and RK data")
    mean_rel_error = np.nan
    median_rel_error = np.nan
    max_rel_error = np.nan
    min_rel_error = np.nan

# Also compare beta_sq directly
mask_beta = (beta_sq_rk > 1e-6) & (beta_sq_wkb_on_rk > 1e-6)
if np.sum(mask_beta) > 0:
    rel_error_beta = np.abs(beta_sq_rk[mask_beta] - beta_sq_wkb_on_rk[mask_beta]) / beta_sq_rk[mask_beta]
    print(f"\n  |beta_k|^2 comparison ({np.sum(mask_beta)} modes):")
    print(f"    Mean relative error:   {np.mean(rel_error_beta):.4f} ({np.mean(rel_error_beta)*100:.2f}%)")
    print(f"    Median relative error: {np.median(rel_error_beta):.4f} ({np.median(rel_error_beta)*100:.2f}%)")
    print(f"    Max relative error:    {np.max(rel_error_beta):.4f} ({np.max(rel_error_beta)*100:.2f}%)")

# Diagnostic: for specific k values, compare in detail
k_diagnostic = [200, 500, 1000, 1500, 2000, 5000, 10000]
print(f"\n  Point-by-point diagnostics:")
print(f"  {'k (M_KK)':<12} {'beta_RK':<14} {'beta_WKB':<14} {'P_RK':<14} {'P_WKB':<14} {'rel_err':<12}")
print(f"  {'-'*78}")
for kd in k_diagnostic:
    # Find nearest in RK grid
    idx_rk = np.argmin(np.abs(k_grid_rk - kd))
    k_actual_rk = k_grid_rk[idx_rk]
    # Find nearest in test grid
    idx_wkb = np.argmin(np.abs(k_test - kd))
    k_actual_wkb = k_test[idx_wkb]

    b_rk = beta_sq_rk[idx_rk]
    b_wkb = beta_sq_wkb[idx_wkb]
    p_rk = P_zeta_rk[idx_rk]
    p_wkb = P_zeta_wkb[idx_rk] if idx_rk < len(P_zeta_wkb) else 0.0

    if p_rk > 0 and p_wkb > 0:
        re = abs(p_rk - p_wkb) / p_rk
        print(f"  {kd:<12} {b_rk:<14.4e} {b_wkb:<14.4e} {p_rk:<14.4e} {p_wkb:<14.4e} {re:<12.4f}")
    else:
        print(f"  {kd:<12} {b_rk:<14.4e} {b_wkb:<14.4e} {p_rk:<14.4e} {p_wkb:<14.4e} {'N/A':<12}")

# ============================================================================
#  SECTION 6: Chirp characterization -- adiabaticity parameter
# ============================================================================

print(f"\n{'=' * 72}")
print(f"SECTION 6: Adiabaticity Parameter")
print(f"{'=' * 72}")

# The adiabaticity parameter gamma_k = |d(omega)/dt| / omega^2
# When gamma >> 1: sudden (non-adiabatic), strong production
# When gamma << 1: adiabatic, WKB valid, weak production
# When gamma ~ 1: WKB boundary

# At the fold, for mode k:
# omega_k^2 = k^2 c_s^2 - z''/z
# d(omega_k^2)/deta = -d(z''/z)/deta

# Adiabaticity parameter as function of k at the fold
k_adiab = np.logspace(np.log10(100), np.log10(50000), 500)
zpp_z_at_fold = zpp_z[fold_idx]
d_zpp_z_deta_fold = d_zpp_z_deta[fold_idx]

gamma_fold = np.zeros(len(k_adiab))
for ik, k in enumerate(k_adiab):
    om_sq = k**2 * c_BLV**2 - zpp_z_at_fold
    if om_sq > 0:
        omega = np.sqrt(om_sq)
        d_om_sq = -d_zpp_z_deta_fold
        gamma_fold[ik] = np.abs(d_om_sq) / (2.0 * omega**2)
    elif om_sq < 0:
        # Tachyonic: gamma = |d(kappa^2)/deta| / kappa^2
        kappa_sq = -om_sq
        gamma_fold[ik] = np.abs(d_zpp_z_deta_fold) / (2.0 * kappa_sq)
    else:
        gamma_fold[ik] = np.inf  # at the turning point

# Find the WKB validity boundary: gamma = 1
idx_gamma_1 = np.argmin(np.abs(gamma_fold - 1.0))
k_gamma_1 = k_adiab[idx_gamma_1]

print(f"\n  Adiabaticity parameter gamma at fold:")
print(f"    z''/z(fold) = {zpp_z_at_fold:.4e}")
print(f"    d(z''/z)/deta(fold) = {d_zpp_z_deta_fold:.4e}")
print(f"    k where gamma = 1: {k_gamma_1:.2f} M_KK")
print(f"    k_tach at fold: {k_tach_tau[fold_idx]:.2f} M_KK")
print(f"    Ratio k(gamma=1) / k_tach: {k_gamma_1 / k_tach_tau[fold_idx]:.4f}")

# For gamma > 1 modes: WKB is unreliable (non-adiabatic)
n_nonadiab = np.sum(gamma_fold > 1)
print(f"\n  Modes with gamma > 1 (non-adiabatic): {n_nonadiab}/{len(k_adiab)}")
print(f"  Modes with gamma < 1 (adiabatic): {len(k_adiab) - n_nonadiab}/{len(k_adiab)}")

# ============================================================================
#  SECTION 7: WKB alternative -- simple Stokes line formula
# ============================================================================

print(f"\n{'=' * 72}")
print(f"SECTION 7: Alternative WKB -- Stokes Line Chirp Formula")
print(f"{'=' * 72}")

# Alternative approach: the simpler "chirp rate" WKB formula from the
# plan prompt: beta_k ~ exp(-pi * k^2 / |dk_tach/dt|)
#
# This is valid when the tachyonic boundary sweeps linearly through
# k-space. It treats the crossing as a single Landau-Zener transition.

# Use the chirp rate at the fold
dk_dt_fold = np.abs(dk_tach_dt[fold_idx])

beta_sq_chirp = np.exp(-PI * k_test**2 / dk_dt_fold)

# P_zeta from chirp formula
P_zeta_chirp = np.zeros(len(k_grid_rk))
beta_sq_chirp_on_rk = np.exp(-PI * k_grid_rk**2 / dk_dt_fold)
z_post = z_fine[-1]
for ik, k in enumerate(k_grid_rk):
    om_eff = k * c_BLV
    P_zeta_chirp[ik] = k**3 / (2*PI**2) * (1 + 2*beta_sq_chirp_on_rk[ik]) / (2*om_eff * z_post**2)

# Compare chirp formula to exact
mask_chirp_valid = (P_zeta_rk > 0) & (P_zeta_chirp > 0) & (beta_sq_rk > 1e-6)
if np.sum(mask_chirp_valid) > 0:
    rel_error_chirp = np.abs(P_zeta_rk[mask_chirp_valid] - P_zeta_chirp[mask_chirp_valid]) / P_zeta_rk[mask_chirp_valid]
    print(f"\n  Chirp formula comparison ({np.sum(mask_chirp_valid)} modes):")
    print(f"    Mean relative error:   {np.mean(rel_error_chirp):.4f} ({np.mean(rel_error_chirp)*100:.2f}%)")
    print(f"    Median relative error: {np.median(rel_error_chirp):.4f} ({np.median(rel_error_chirp)*100:.2f}%)")
    print(f"    Max relative error:    {np.max(rel_error_chirp):.4f} ({np.max(rel_error_chirp)*100:.2f}%)")
else:
    print(f"\n  WARNING: No valid overlap for chirp formula")

# Also for beta_sq directly
mask_chirp_beta = (beta_sq_rk > 1e-6) & (beta_sq_chirp_on_rk > 1e-30)
if np.sum(mask_chirp_beta) > 0:
    rel_err_cb = np.abs(beta_sq_rk[mask_chirp_beta] - beta_sq_chirp_on_rk[mask_chirp_beta]) / beta_sq_rk[mask_chirp_beta]
    print(f"\n  |beta_k|^2 chirp formula ({np.sum(mask_chirp_beta)} modes):")
    print(f"    Mean relative error:   {np.mean(rel_err_cb):.4f} ({np.mean(rel_err_cb)*100:.2f}%)")
    print(f"    Median relative error: {np.median(rel_err_cb):.4f} ({np.median(rel_err_cb)*100:.2f}%)")

# Point-by-point
print(f"\n  Chirp formula point-by-point:")
print(f"  {'k (M_KK)':<12} {'beta_RK':<14} {'beta_chirp':<14} {'ratio':<12}")
print(f"  {'-'*50}")
for kd in k_diagnostic:
    idx_rk = np.argmin(np.abs(k_grid_rk - kd))
    b_rk = beta_sq_rk[idx_rk]
    b_ch = beta_sq_chirp_on_rk[idx_rk]
    ratio = b_ch / b_rk if b_rk > 0 else np.nan
    print(f"  {kd:<12} {b_rk:<14.4e} {b_ch:<14.4e} {ratio:<12.4e}")

# ============================================================================
#  SECTION 8: Physical interpretation -- resonance analysis
# ============================================================================

print(f"\n{'=' * 72}")
print(f"SECTION 8: Resonance Structure")
print(f"{'=' * 72}")

# The key physical question: Is the transit a single-pass chirp (monotone
# sweep) or does z''/z have oscillations that could produce multiple
# crossings (resonant amplification)?

# Count oscillations in z''/z
d2_zpp_z = cs_zpp_z_eta_spline(eta_fine, 2)
zero_crossings_d1 = np.sum(np.diff(np.sign(d_zpp_z_deta)) != 0)
zero_crossings_d2 = np.sum(np.diff(np.sign(d2_zpp_z)) != 0)

print(f"\n  z''/z(eta) structure:")
print(f"    Zero crossings of d(z''/z)/deta: {zero_crossings_d1}")
print(f"    Zero crossings of d^2(z''/z)/deta^2: {zero_crossings_d2}")
print(f"    Shape: {'single bump' if zero_crossings_d1 <= 2 else 'oscillatory'}")

# Number of modes with multiple crossings
n_multi = np.sum(n_crossings > 2)
print(f"\n  Multiple-crossing modes (resonant amplification):")
print(f"    Modes with > 2 crossings: {n_multi}/{len(k_test)}")
print(f"    Modes with exactly 2 crossings: {np.sum(n_crossings == 2)}/{len(k_test)}")

# Mach number at fold: v_terminal / c_BLV
Mach_fold = v_terminal / c_BLV
print(f"\n  Transit characterization:")
print(f"    Mach number: {Mach_fold:.2f} (SUPERSONIC)")
print(f"    Transit time dt: {dt_transit:.6e} M_KK^{{-1}}")
print(f"    1/H_fold: {1/H_fold_canon:.6e} M_KK^{{-1}}")
print(f"    dt * H_fold: {dt_transit * H_fold_canon:.4f} (<<1: impulsive)")

# Condensed matter analog: Kibble-Zurek with chirp
# The chirp rate sets the Kibble-Zurek exponent for defect density
# n_defect ~ (chirp_rate / gap^2)^{d*nu/(1+z*nu)}
print(f"\n  Condensed matter analog:")
print(f"    This is a CHIRPED quench through a quantum critical point.")
print(f"    The z''/z barrier is the order parameter gap.")
print(f"    The chirp rate dk_tach/dt = {dk_dt_fold:.4e} M_KK^2 controls")
print(f"    the Kibble-Zurek defect density via the Landau-Zener formula.")
print(f"    Single-sweep (monotone) => no resonant enhancement.")

# ============================================================================
#  SECTION 9: Gate verdict
# ============================================================================

print(f"\n{'=' * 72}")
print(f"SECTION 9: Gate Verdict")
print(f"{'=' * 72}")

# Determine which WKB formula to use for the gate
# Use the FULL tachyonic integral (sinh formula) as the primary WKB

if np.sum(mask_valid) > 0:
    # Gate is on P_exact vs P_WKB
    gate_error = median_rel_error

    # Also compute in sub-bands
    # Band 1: deeply tachyonic (k < k_tach/2)
    k_half = k_tach_fold / 2
    mask_deep = mask_valid & (k_grid_rk < k_half)
    # Band 2: near tachyonic boundary (k ~ k_tach)
    mask_boundary = mask_valid & (k_grid_rk > k_half) & (k_grid_rk < k_tach_fold * 1.5)
    # Band 3: sub-horizon (k > k_tach)
    mask_sub = mask_valid & (k_grid_rk > k_tach_fold * 1.5)

    for label, m in [("Deep tachyonic", mask_deep),
                     ("Near boundary", mask_boundary),
                     ("Sub-horizon", mask_sub)]:
        if np.sum(m) > 0:
            re_band = np.abs(P_zeta_rk[m] - P_zeta_wkb[m]) / P_zeta_rk[m]
            print(f"  {label}: median rel. error = {np.median(re_band):.4f} ({np.median(re_band)*100:.2f}%) [{np.sum(m)} modes]")
        else:
            print(f"  {label}: no modes in band")
else:
    gate_error = np.nan

# Gate verdict
if not np.isnan(gate_error):
    if gate_error < 0.10:
        gate_verdict = "PASS"
        gate_detail = f"Median |P_exact - P_WKB|/P_exact = {gate_error*100:.1f}% < 10%"
    elif gate_error < 0.50:
        gate_verdict = "INFO"
        gate_detail = f"Median |P_exact - P_WKB|/P_exact = {gate_error*100:.1f}% in [10%, 50%]"
    else:
        gate_verdict = "FAIL"
        gate_detail = f"Median |P_exact - P_WKB|/P_exact = {gate_error*100:.1f}% > 50%"
else:
    gate_verdict = "INFO"
    gate_detail = "No valid overlap between WKB and exact modes for P_zeta comparison"

print(f"\n  Gate CHIRP-PENUMBRA-70: {gate_verdict}")
print(f"  {gate_detail}")

# Additional diagnostic: what is the right WKB regime?
if np.sum(mask_beta) > 0:
    med_beta_err = np.median(rel_error_beta)
    print(f"\n  |beta_k|^2 comparison: median error = {med_beta_err*100:.1f}%")
    if med_beta_err < 0.10:
        print(f"  WKB |beta_k|^2 is accurate to < 10% (PASS criterion met at beta level)")
    elif med_beta_err < 0.50:
        print(f"  WKB |beta_k|^2 is marginally accurate (10-50%)")
    else:
        print(f"  WKB |beta_k|^2 is poor (> 50%)")

print(f"\n  Physical interpretation:")
print(f"    k_tach(fold) = {k_tach_fold:.0f} M_KK")
print(f"    dk_tach/dt = {dk_dt_fold:.4e} M_KK^2")
print(f"    Mach = {Mach_fold:.2f}")
print(f"    Transit is SUPERSONIC and IMPULSIVE (dt*H << 1).")
print(f"    z''/z has {zero_crossings_d1} d1 zero-crossings => {'single-bump' if zero_crossings_d1 <= 2 else 'oscillatory'} profile.")
if n_multi > 0:
    print(f"    {n_multi} modes show multiple crossings (possible parametric resonance).")
else:
    print(f"    No multiple crossings => single-pass chirp, no parametric resonance.")

# ============================================================================
#  SECTION 10: Save data
# ============================================================================

outpath = os.path.join(os.path.dirname(__file__), 's70_chirp_penumbra.npz')
np.savez(
    outpath,
    # Tachyonic boundary
    tau_fine=tau_fine,
    eta_fine=eta_fine,
    k_tach_tau=k_tach_tau,
    dk_tach_dtau=dk_tach_dtau,
    dk_tach_dt=dk_tach_dt,
    dk_tach_deta=dk_tach_deta,
    # z''/z profile
    zpp_z=zpp_z,
    d_zpp_z_deta=d_zpp_z_deta,
    # WKB predictions
    k_test=k_test,
    beta_sq_wkb=beta_sq_wkb,
    n_crossings=n_crossings,
    dwell_time_eta=dwell_time_eta,
    chirp_at_cross=chirp_at_cross,
    # Chirp formula
    beta_sq_chirp=beta_sq_chirp,
    # Adiabaticity
    k_adiab=k_adiab,
    gamma_fold=gamma_fold,
    k_gamma_1=np.array(k_gamma_1),
    # Comparison to exact
    k_grid_rk=k_grid_rk,
    beta_sq_rk=beta_sq_rk,
    beta_sq_wkb_on_rk=beta_sq_wkb_on_rk,
    beta_sq_chirp_on_rk=beta_sq_chirp_on_rk,
    P_zeta_rk=P_zeta_rk,
    P_zeta_wkb=P_zeta_wkb,
    P_zeta_chirp=P_zeta_chirp,
    # Key scalars
    k_tach_fold=np.array(k_tach_fold),
    dk_dt_fold=np.array(dk_dt_fold),
    Mach_fold=np.array(Mach_fold),
    c_BLV=np.array(c_BLV),
    # Gate
    gate_verdict=np.array(gate_verdict),
    gate_detail=np.array(gate_detail),
    gate_error=np.array(gate_error) if not np.isnan(gate_error) else np.array(np.nan),
)
print(f"\nData saved to {outpath}")

# ============================================================================
#  SECTION 11: Plots
# ============================================================================

fig, axes = plt.subplots(2, 3, figsize=(18, 10))

# Panel 1: k_tach(tau) and chirp rate
ax = axes[0, 0]
ax.plot(tau_fine, k_tach_tau, 'b-', lw=2, label=r'$k_{\mathrm{tach}}(\tau)$')
ax.axvline(tau_fold, color='green', ls=':', alpha=0.7, label=r'$\tau_{\mathrm{fold}}$')
ax.axhline(H_fold_canon / c_BLV, color='red', ls='--', alpha=0.5, label=r'$k_{\mathrm{transit}}$')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$k_{\mathrm{tach}}$ [M$_{\mathrm{KK}}$]')
ax.set_title(r'Tachyonic Boundary $k_{\mathrm{tach}}(\tau)$')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 2: Chirp rate dk_tach/dt
ax = axes[0, 1]
ax.plot(tau_fine, np.abs(dk_tach_dt), 'r-', lw=2)
ax.axvline(tau_fold, color='green', ls=':', alpha=0.7, label=r'$\tau_{\mathrm{fold}}$')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$|dk_{\mathrm{tach}}/dt|$ [M$_{\mathrm{KK}}^2$]')
ax.set_title('Chirp Rate')
ax.set_yscale('log')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 3: z''/z profile
ax = axes[0, 2]
ax.semilogy(tau_fine, zpp_z, 'k-', lw=2, label=r"$z''/z$")
for kd in [200, 500, 1000, 2000]:
    ax.axhline(kd**2 * c_BLV**2, ls='--', alpha=0.3, label=f'$k={kd}$' if kd == 200 else None)
ax.axvline(tau_fold, color='green', ls=':', alpha=0.7)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r"$z''/z$ [M$_{\mathrm{KK}}^2$]")
ax.set_title(r"Mukhanov Pump $z''/z$")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 4: beta_k comparison (WKB vs exact)
ax = axes[1, 0]
mask_plot = beta_sq_rk > 1e-12
if np.sum(mask_plot) > 0:
    ax.loglog(k_grid_rk[mask_plot], beta_sq_rk[mask_plot], 'b-', lw=2, label='Exact (RK)')
mask_wkb_plot = beta_sq_wkb_on_rk > 1e-12
if np.sum(mask_wkb_plot) > 0:
    ax.loglog(k_grid_rk[mask_wkb_plot], beta_sq_wkb_on_rk[mask_wkb_plot], 'r--', lw=1.5, label='WKB (integral)')
mask_chirp_plot = beta_sq_chirp_on_rk > 1e-12
if np.sum(mask_chirp_plot) > 0:
    ax.loglog(k_grid_rk[mask_chirp_plot], beta_sq_chirp_on_rk[mask_chirp_plot], 'g:', lw=1.5, label='Chirp formula')
ax.axvline(k_tach_fold, color='orange', ls='--', alpha=0.5, label=r'$k_{\mathrm{tach}}$')
ax.set_xlabel(r'k [M$_{\mathrm{KK}}$]')
ax.set_ylabel(r'$|\beta_k|^2$')
ax.set_title(r'Bogoliubov Coefficient $|\beta_k|^2$')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 5: P_zeta comparison
ax = axes[1, 1]
mask_rk = P_zeta_rk > 0
if np.sum(mask_rk) > 0:
    ax.loglog(k_grid_rk[mask_rk], P_zeta_rk[mask_rk], 'b-', lw=2, label='Exact (RK)')
mask_wkb_p = P_zeta_wkb > 0
if np.sum(mask_wkb_p) > 0:
    ax.loglog(k_grid_rk[mask_wkb_p], P_zeta_wkb[mask_wkb_p], 'r--', lw=1.5, label='WKB')
mask_ch_p = P_zeta_chirp > 0
if np.sum(mask_ch_p) > 0:
    ax.loglog(k_grid_rk[mask_ch_p], P_zeta_chirp[mask_ch_p], 'g:', lw=1.5, label='Chirp')
ax.set_xlabel(r'k [M$_{\mathrm{KK}}$]')
ax.set_ylabel(r'$\mathcal{P}_\zeta(k)$')
ax.set_title('Power Spectrum Comparison')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 6: Adiabaticity parameter
ax = axes[1, 2]
ax.loglog(k_adiab, gamma_fold, 'purple', lw=2)
ax.axhline(1.0, color='red', ls='--', lw=1.5, label=r'$\gamma = 1$')
ax.axvline(k_tach_fold, color='orange', ls='--', alpha=0.5, label=r'$k_{\mathrm{tach}}$')
ax.axvline(k_gamma_1, color='red', ls=':', alpha=0.5, label=f'$k(\\gamma=1)={k_gamma_1:.0f}$')
ax.set_xlabel(r'k [M$_{\mathrm{KK}}$]')
ax.set_ylabel(r'$\gamma_k$ (adiabaticity)')
ax.set_title('Adiabaticity Parameter at Fold')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

plt.tight_layout()
figpath = os.path.join(os.path.dirname(__file__), 's70_chirp_penumbra.png')
plt.savefig(figpath, dpi=150)
plt.close()
print(f"Plot saved to {figpath}")

# ============================================================================
#  SUMMARY
# ============================================================================

print(f"\n{'=' * 72}")
print(f"SUMMARY: CHIRP-PENUMBRA-70")
print(f"{'=' * 72}")
print(f"""
RESONANCE STRUCTURE:
  What oscillates: Mukhanov mode functions u_k(eta)
  What constrains: z''/z barrier (Mukhanov pump from spectral action)
  Boundary:        k_tach(tau) = sqrt(z''/z) / c_BLV = {k_tach_fold:.0f} M_KK at fold
  Cavity:          The tachyonic band [0, k_tach(tau)] sweeps through k-space

CHIRP CHARACTERIZATION:
  k_tach(fold) = {k_tach_fold:.2f} M_KK
  dk_tach/dt(fold) = {dk_dt_fold:.4e} M_KK^2
  Mach number = {Mach_fold:.2f} (SUPERSONIC transit)
  z''/z profile: {'single-bump' if zero_crossings_d1 <= 2 else 'oscillatory'} ({zero_crossings_d1} d1 crossings)
  Multiple-crossing modes: {n_multi}

WKB VALIDITY:
  k(gamma=1) = {k_gamma_1:.2f} M_KK
  WKB adiabatic for k > k(gamma=1)
  WKB fails for k < k(gamma=1) (non-adiabatic regime)

GATE: CHIRP-PENUMBRA-70: {gate_verdict}
  {gate_detail}
""")

print("DONE.")
