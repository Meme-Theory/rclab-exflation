#!/usr/bin/env python3
"""
Session 31A — K-1: Kapitza Effective Potential on U(2)-Invariant Surface

Computes V_Kapitza(tau; A) for the modulus tau, where epsilon oscillates
rapidly with amplitude A along the T2 direction. Uses arcsine-weighted
averaging (natural measure for sinusoidal oscillation).

V_Kapitza(tau; A) = (1/pi) * integral_{-A}^{A} V_total(tau, eps) / sqrt(A^2 - eps^2) deps
                  + (1/(4*omega_perp^2)) * (1/pi) * integral_{-A}^{A} (dV/deps)^2 / sqrt(A^2 - eps^2) deps

Gate K-1: PASS if V_Kapitza has interior minimum at tau_* in (0.05, 0.55)
          for ANY amplitude A with d^2 V_Kapitza / dtau^2 > 0.

Inputs:
  - s30b_grid_bcs.npz  (V_total on 21x21 grid)
  - s30b_5d_stability.npz  (T3/T4 eigenvalues for omega_perp)
  - s30b_sdw_grid.npz  (L1, L2 for Formula B sin^2 evaluation)

Outputs:
  - s31a_kapitza_gate.npz
  - s31a_kapitza_gate.png

Author: phonon-exflation-sim agent (Session 31A)
Date: 2026-03-02
"""

import numpy as np
from scipy.interpolate import RectBivariateSpline, interp1d
from scipy.integrate import quad
from scipy.signal import argrelmin
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
import sys

# ── Paths ────────────────────────────────────────────────────────────────
ROOT = r"C:\sandbox\Ainulindale Exflation"
T0 = os.path.join(ROOT, "tier0-computation")

# ── Load data ────────────────────────────────────────────────────────────
print("Loading prerequisite data...")
bcs = np.load(os.path.join(T0, "s30b_grid_bcs.npz"), allow_pickle=True)
stab = np.load(os.path.join(T0, "s30b_5d_stability.npz"), allow_pickle=True)
sdw = np.load(os.path.join(T0, "s30b_sdw_grid.npz"), allow_pickle=True)

tau_grid = bcs['tau']       # (21,) in [0, 0.60]
eps_grid = bcs['eps']       # (21,) in [-0.15, 0.15]
V_total_1p00 = bcs['V_total_1p00']  # (21, 21) V_total at mu/lmin=1.00
V_total_1p20 = bcs['V_total_1p20']  # (21, 21) V_total at mu/lmin=1.20
V_spec = bcs['V_spec']              # (21, 21) spectral action alone
sin2_tw = bcs['sin2_tw']            # (21, 21) Formula A sin^2(theta_W)
phi_30 = bcs['phi_30']              # (21, 21)
L1 = sdw['L1']                      # (21, 21)
L2 = sdw['L2']                      # (21, 21)

# T3/T4 transverse Hessian eigenvalues (at boundary point)
H_T3 = float(stab['H_T3'])   # +8.326
H_T4 = float(stab['H_T4'])   # -9.893

print(f"  tau: [{tau_grid[0]:.3f}, {tau_grid[-1]:.3f}], n={len(tau_grid)}")
print(f"  eps: [{eps_grid[0]:.3f}, {eps_grid[-1]:.3f}], n={len(eps_grid)}")
print(f"  V_total_1p00 range: [{V_total_1p00.min():.4f}, {V_total_1p00.max():.4f}]")
print(f"  H_T3 = {H_T3:.3f}, H_T4 = {H_T4:.3f}")

# ── Formula B correction for sin^2(theta_W) ─────────────────────────────
# sin^2_B = 3*L2 / (L1 + 3*L2)   [Paper 14 eq 2.85-2.93]
sin2_B = 3.0 * L2 / (L1 + 3.0 * L2)
print(f"  sin^2_B range: [{sin2_B.min():.4f}, {sin2_B.max():.4f}]")

# ── Build interpolating splines ─────────────────────────────────────────
# RectBivariateSpline expects (x, y, z) with z[i,j] = f(x[i], y[j])
# Our arrays: V_total[i_tau, j_eps], tau_grid[i_tau], eps_grid[j_eps]
# V_total uses mu/lmin = 1.20 (the physical BCS parameter from Session 29)
V_total = V_total_1p20  # Primary choice: mu/lmin=1.20

spl_V = RectBivariateSpline(tau_grid, eps_grid, V_total, kx=3, ky=3)
spl_sin2B = RectBivariateSpline(tau_grid, eps_grid, sin2_B, kx=3, ky=3)
spl_phi30 = RectBivariateSpline(tau_grid, eps_grid, phi_30, kx=3, ky=3)

# ── Kapitza computation ─────────────────────────────────────────────────
# Amplitudes to scan
A_values = np.array([0.02, 0.05, 0.08, 0.10, 0.12, 0.15])

# omega_perp values: use both T3 and T4 to bracket
# T4 is negative (unstable), so |T4| gives the instability frequency
# For Kapitza, omega^2 = eigenvalue of transverse Hessian
# T3 = +8.326 -> omega_T3 = sqrt(8.326) ~ 2.885
# T4 = -9.893 -> UNSTABLE. For the Kapitza formula, use |T4| as the
#   relevant frequency scale (the oscillation frequency in the unstable
#   direction is set by the curvature at the hilltop).
omega_sq_T3 = abs(H_T3)   # = 8.326
omega_sq_T4 = abs(H_T4)   # = 9.893

# Fine tau grid for output
n_tau_fine = 201
tau_fine = np.linspace(0.01, 0.59, n_tau_fine)

def compute_kapitza_potential(A, omega_sq, tau_arr):
    """
    Compute V_Kapitza(tau; A) = <V>_arcsine + (1/(4*omega^2)) * <(dV/deps)^2>_arcsine

    The arcsine average of f(eps) over [-A, A]:
      <f> = (1/pi) * integral_{-A}^{A} f(eps) / sqrt(A^2 - eps^2) deps

    We use Gauss-Chebyshev quadrature (native for arcsine weight):
      integral_{-1}^{1} g(x) / sqrt(1 - x^2) dx = (pi/N) * sum g(x_k)
    where x_k = cos((2k-1)*pi/(2N)), k=1,...,N.

    So <f> = (1/N) * sum f(A*x_k)

    Parameters
    ----------
    A : float
        Oscillation amplitude in epsilon
    omega_sq : float
        omega_perp^2 from transverse Hessian eigenvalue
    tau_arr : ndarray (M,)
        tau values to evaluate

    Returns
    -------
    V_kap : ndarray (M,)
        Kapitza effective potential
    V_avg : ndarray (M,)
        Time-averaged bare potential (first term only)
    V_corr : ndarray (M,)
        Kapitza correction (second term)
    """
    # Gauss-Chebyshev quadrature nodes (arcsine distribution)
    N_quad = 200  # Sufficient for smooth V_total
    k = np.arange(1, N_quad + 1)
    x_k = np.cos((2*k - 1) * np.pi / (2 * N_quad))  # nodes in [-1, 1]
    eps_k = A * x_k  # scale to [-A, A]

    M = len(tau_arr)
    V_avg = np.zeros(M)
    grad_sq_avg = np.zeros(M)

    for i, tau_val in enumerate(tau_arr):
        # Evaluate V_total at (tau_val, eps_k)
        V_vals = spl_V(tau_val, eps_k, grid=False)  # shape (N_quad,)
        V_avg[i] = np.mean(V_vals)

        # Evaluate dV/deps at (tau_val, eps_k) via spline derivative
        dV_deps = spl_V(tau_val, eps_k, dx=0, dy=1, grid=False)
        grad_sq_avg[i] = np.mean(dV_deps**2)

    V_corr = grad_sq_avg / (4.0 * omega_sq)
    V_kap = V_avg + V_corr

    return V_kap, V_avg, V_corr


def find_interior_minima(tau_arr, V_arr, tau_lo=0.05, tau_hi=0.55):
    """
    Find interior minima of V_arr(tau_arr) in (tau_lo, tau_hi).
    Returns list of (tau_min, V_min, d2V_dtau2) tuples.
    """
    results = []
    # Numerical second derivative for curvature check
    dtau = tau_arr[1] - tau_arr[0]
    dV = np.gradient(V_arr, tau_arr)
    d2V = np.gradient(dV, tau_arr)

    # Find local minima via sign change of first derivative
    mask_interior = (tau_arr > tau_lo) & (tau_arr < tau_hi)
    idx_int = np.where(mask_interior)[0]

    for i in range(len(idx_int) - 1):
        j = idx_int[i]
        j1 = idx_int[i+1]
        if dV[j] < 0 and dV[j1] > 0:  # sign change: decreasing then increasing
            # Interpolate zero crossing
            frac = -dV[j] / (dV[j1] - dV[j])
            tau_min = tau_arr[j] + frac * (tau_arr[j1] - tau_arr[j])
            V_min = V_arr[j] + frac * (V_arr[j1] - V_arr[j])
            d2V_min = d2V[j] + frac * (d2V[j1] - d2V[j])
            results.append((tau_min, V_min, d2V_min))

    return results


# ── Main computation ─────────────────────────────────────────────────────
print("\n" + "="*70)
print("K-1 KAPITZA EFFECTIVE POTENTIAL COMPUTATION")
print("="*70)

# Reference: V_total along Jensen (eps=0)
V_jensen = spl_V(tau_fine, 0.0, grid=False).ravel()

# Also compute V_spec along Jensen for comparison
spl_Vspec = RectBivariateSpline(tau_grid, eps_grid, V_spec, kx=3, ky=3)
V_spec_jensen = spl_Vspec(tau_fine, 0.0, grid=False).ravel()

results_all = {}

for omega_label, omega_sq in [("T3", omega_sq_T3), ("T4", omega_sq_T4)]:
    print(f"\n--- omega_perp^2 = {omega_sq:.3f} ({omega_label}, omega = {np.sqrt(omega_sq):.3f}) ---")

    for A in A_values:
        # Check amplitude is within grid
        if A > eps_grid[-1]:
            print(f"  A={A:.2f}: SKIPPED (exceeds grid bounds)")
            continue

        V_kap, V_avg, V_corr = compute_kapitza_potential(A, omega_sq, tau_fine)

        # Find interior minima
        minima = find_interior_minima(tau_fine, V_kap)

        key = f"{omega_label}_A{A:.2f}"
        results_all[key] = {
            'V_kap': V_kap,
            'V_avg': V_avg,
            'V_corr': V_corr,
            'minima': minima,
            'A': A,
            'omega_sq': omega_sq,
            'omega_label': omega_label,
        }

        corr_max = V_corr.max()
        corr_ratio = corr_max / abs(V_kap.max() - V_kap.min()) if abs(V_kap.max() - V_kap.min()) > 0 else 0

        if len(minima) > 0:
            for tm, vm, d2vm in minima:
                # Evaluate sin2_B and phi_30 at minimum
                s2b_at_min = float(spl_sin2B(tm, 0.0, grid=False))
                phi_at_min = float(spl_phi30(tm, 0.0, grid=False))
                print(f"  A={A:.2f}: MINIMUM at tau*={tm:.4f}, V_Kap={vm:.6f}, "
                      f"d2V/dtau2={d2vm:.4f}")
                print(f"           sin2_B={s2b_at_min:.4f}, phi_30={phi_at_min:.4f}, "
                      f"Kapitza_correction_max={corr_max:.6f}")
                results_all[key]['sin2_B_at_min'] = s2b_at_min
                results_all[key]['phi_at_min'] = phi_at_min
        else:
            print(f"  A={A:.2f}: NO interior minimum. Corr_max={corr_max:.6f}, "
                  f"V_range={V_kap.max()-V_kap.min():.6f}")


# ── Also try V_spec only (without BCS, as a baseline) ───────────────────
print("\n--- V_spec only (no BCS contribution) ---")
spl_Vspec2 = RectBivariateSpline(tau_grid, eps_grid, V_spec, kx=3, ky=3)
for omega_label, omega_sq in [("T3", omega_sq_T3), ("T4", omega_sq_T4)]:
    for A in [0.10, 0.15]:
        N_quad = 200
        k = np.arange(1, N_quad + 1)
        x_k = np.cos((2*k - 1) * np.pi / (2 * N_quad))
        eps_k = A * x_k

        V_avg_spec = np.zeros(n_tau_fine)
        grad_sq_spec = np.zeros(n_tau_fine)
        for i, tv in enumerate(tau_fine):
            V_vals = spl_Vspec2(tv, eps_k, grid=False)
            V_avg_spec[i] = np.mean(V_vals)
            dV_deps = spl_Vspec2(tv, eps_k, dx=0, dy=1, grid=False)
            grad_sq_spec[i] = np.mean(dV_deps**2)

        V_corr_spec = grad_sq_spec / (4.0 * omega_sq)
        V_kap_spec = V_avg_spec + V_corr_spec
        minima_spec = find_interior_minima(tau_fine, V_kap_spec)

        if len(minima_spec) > 0:
            for tm, vm, d2vm in minima_spec:
                print(f"  {omega_label}, A={A:.2f}: V_spec-only MINIMUM at tau*={tm:.4f}, d2V={d2vm:.4f}")
        else:
            print(f"  {omega_label}, A={A:.2f}: V_spec-only NO minimum")


# ── Detailed analysis of the Kapitza correction structure ────────────────
print("\n" + "="*70)
print("KAPITZA CORRECTION STRUCTURE ANALYSIS")
print("="*70)

# The key diagnostic: how does the Kapitza correction vary with tau?
# If it increases faster than V_spec decreases, we get a minimum.
A_test = 0.15
for omega_label, omega_sq in [("T3", omega_sq_T3), ("T4", omega_sq_T4)]:
    V_kap, V_avg, V_corr = compute_kapitza_potential(A_test, omega_sq, tau_fine)

    dV_avg = np.gradient(V_avg, tau_fine)
    dV_corr = np.gradient(V_corr, tau_fine)

    # Where does dV_corr/dtau > -dV_avg/dtau? (correction slope exceeds bare slope)
    ratio_slopes = dV_corr / (-dV_avg + 1e-30)
    mask_positive = ratio_slopes > 0

    print(f"\n  {omega_label}, A={A_test:.2f}:")
    print(f"    V_avg slope range: [{dV_avg.min():.6f}, {dV_avg.max():.6f}]")
    print(f"    V_corr slope range: [{dV_corr.min():.6f}, {dV_corr.max():.6f}]")
    print(f"    V_corr max: {V_corr.max():.6f}")
    print(f"    V_avg range: {V_avg.max()-V_avg.min():.6f}")
    print(f"    Correction/range ratio: {V_corr.max()/(V_avg.max()-V_avg.min()):.6f}")

    # Check if slopes can ever balance
    idx_interior = (tau_fine > 0.05) & (tau_fine < 0.55)
    max_corr_slope = dV_corr[idx_interior].max()
    max_bare_descent = abs(dV_avg[idx_interior].min())
    print(f"    Max correction ascent: {max_corr_slope:.6f}")
    print(f"    Max bare descent: {max_bare_descent:.6f}")
    print(f"    Ratio (correction/descent): {max_corr_slope/max_bare_descent:.6f}")


# ── Extended analysis: scan omega_sq down to very soft modes ─────────────
print("\n" + "="*70)
print("EXTENDED SCAN: Soft-mode sweep (omega_sq from 0.1 to 100)")
print("="*70)

omega_sq_scan = np.array([0.1, 0.5, 1.0, 2.0, 5.0, 8.326, 9.893, 20.0, 50.0, 100.0])
A_scan = 0.15  # Maximum amplitude

found_any = False
soft_results = []

for omega_sq_val in omega_sq_scan:
    V_kap, V_avg, V_corr = compute_kapitza_potential(A_scan, omega_sq_val, tau_fine)
    minima = find_interior_minima(tau_fine, V_kap)

    corr_max = V_corr.max()
    V_range = V_kap.max() - V_kap.min()

    has_min = len(minima) > 0
    soft_results.append((omega_sq_val, corr_max, V_range, has_min, minima))

    if has_min:
        found_any = True
        for tm, vm, d2vm in minima:
            s2b = float(spl_sin2B(tm, 0.0, grid=False))
            phi = float(spl_phi30(tm, 0.0, grid=False))
            print(f"  omega^2={omega_sq_val:.1f}: MINIMUM at tau*={tm:.4f}, d2V={d2vm:.4f}, "
                  f"sin2_B={s2b:.4f}, phi_30={phi:.4f}, corr/range={corr_max/V_range:.4f}")
    else:
        print(f"  omega^2={omega_sq_val:.1f}: No minimum. corr_max={corr_max:.6f}, "
              f"corr/range={corr_max/V_range:.6f}")

if not found_any:
    print("\n  >>> NO interior minimum found for ANY omega^2 at A=0.15")
    print("  >>> Testing even softer modes...")

    # Push to extremely soft: omega^2 from 0.001 to 0.1
    omega_sq_ultra = np.array([0.001, 0.005, 0.01, 0.05])
    for omega_sq_val in omega_sq_ultra:
        V_kap, V_avg, V_corr = compute_kapitza_potential(A_scan, omega_sq_val, tau_fine)
        minima = find_interior_minima(tau_fine, V_kap)
        corr_max = V_corr.max()
        V_range = V_kap.max() - V_kap.min()

        if len(minima) > 0:
            found_any = True
            for tm, vm, d2vm in minima:
                s2b = float(spl_sin2B(tm, 0.0, grid=False))
                phi = float(spl_phi30(tm, 0.0, grid=False))
                print(f"  omega^2={omega_sq_val:.4f}: MINIMUM at tau*={tm:.4f}, d2V={d2vm:.4f}, "
                      f"sin2_B={s2b:.4f}, phi_30={phi:.4f}")
        else:
            print(f"  omega^2={omega_sq_val:.4f}: No minimum. corr_max={corr_max:.6f}, "
                  f"corr/range={corr_max/V_range:.6f}")


# ── Critical omega^2 threshold: solve for omega_crit ─────────────────────
print("\n" + "="*70)
print("CRITICAL OMEGA^2 THRESHOLD")
print("="*70)

# For the Kapitza correction to create a minimum, we need:
# d/dtau [V_corr(tau)] = d/dtau [<(dV/deps)^2> / (4*omega^2)]
# to exceed -d/dtau [V_avg(tau)] at SOME tau.
#
# Equivalently: omega_crit^2 = max_tau { d<(dV/deps)^2>/dtau / (4 * |dV_avg/dtau|) }

# Compute numerator: d<(dV/deps)^2>/dtau
N_quad = 200
k = np.arange(1, N_quad + 1)
x_k = np.cos((2*k - 1) * np.pi / (2 * N_quad))
eps_k = A_scan * x_k

grad_sq_profile = np.zeros(n_tau_fine)
for i, tv in enumerate(tau_fine):
    dV_deps = spl_V(tv, eps_k, dx=0, dy=1, grid=False)
    grad_sq_profile[i] = np.mean(dV_deps**2)

d_gradsq = np.gradient(grad_sq_profile, tau_fine)
V_avg_profile = np.zeros(n_tau_fine)
for i, tv in enumerate(tau_fine):
    V_vals = spl_V(tv, eps_k, grid=False)
    V_avg_profile[i] = np.mean(V_vals)
d_Vavg = np.gradient(V_avg_profile, tau_fine)

# Where V_avg is decreasing (d_Vavg < 0) and grad_sq is increasing (d_gradsq > 0)
mask = (d_Vavg < 0) & (d_gradsq > 0) & (tau_fine > 0.05) & (tau_fine < 0.55)
if mask.any():
    omega_crit_sq = d_gradsq[mask] / (4.0 * abs(d_Vavg[mask]))
    omega_crit_min = omega_crit_sq.min()
    idx_best = np.where(mask)[0][np.argmin(omega_crit_sq)]
    print(f"  Critical omega^2 (minimum needed for correction to match bare slope):")
    print(f"    omega_crit^2 = {omega_crit_min:.6f} at tau = {tau_fine[idx_best]:.4f}")
    print(f"    omega_crit = {np.sqrt(omega_crit_min):.6f}")
    print(f"  Compare: T3 omega^2 = {omega_sq_T3:.3f}, T4 |omega^2| = {omega_sq_T4:.3f}")
    print(f"  Ratio T3/crit = {omega_sq_T3/omega_crit_min:.3f}")

    if omega_crit_min < omega_sq_T3:
        print("  >>> T3 frequency EXCEEDS critical threshold -- Kapitza correction too weak")
    else:
        print("  >>> T3 frequency BELOW critical threshold -- Kapitza correction can dominate")
else:
    # Correction slope never positive where bare is negative
    mask2 = (d_Vavg < 0) & (tau_fine > 0.05) & (tau_fine < 0.55)
    if mask2.any():
        print("  Correction gradient never positive where bare gradient is negative!")
        print("  Kapitza correction DECREASES with tau (same direction as V_avg)")
        print("  >>> STRUCTURAL IMPOSSIBILITY: correction reinforces monotonicity")
    else:
        print("  V_avg not decreasing in interior -- unexpected.")


# ── Gate Verdict ─────────────────────────────────────────────────────────
print("\n" + "="*70)
print("GATE K-1 VERDICT")
print("="*70)

any_minimum = False
best_minimum = None
for key, res in results_all.items():
    if len(res['minima']) > 0:
        any_minimum = True
        for tm, vm, d2vm in res['minima']:
            if best_minimum is None or d2vm > best_minimum[2]:
                best_minimum = (tm, vm, d2vm, key, res)

if any_minimum:
    tm, vm, d2vm, key, res = best_minimum
    print(f"  K-1 PASS: Interior minimum at tau* = {tm:.4f}")
    print(f"    Amplitude A = {res['A']:.2f}, omega_label = {res['omega_label']}")
    print(f"    V_Kapitza(tau*) = {vm:.6f}")
    print(f"    d2V/dtau2 = {d2vm:.4f}")
    if 'sin2_B_at_min' in res:
        print(f"    sin2_B(tau*) = {res['sin2_B_at_min']:.4f}")
        print(f"    phi_30(tau*) = {res['phi_at_min']:.4f}")
    gate_verdict = "PASS"
else:
    print("  K-1 DOES NOT FIRE: No interior minimum found.")
    print("  Kapitza correction is structurally too weak to overcome V_spec monotonicity.")
    print(f"  Maximum correction at A=0.15: {max(r['V_corr'].max() for r in results_all.values()):.6f}")
    print(f"  V_total range: {V_jensen.max()-V_jensen.min():.6f}")
    gate_verdict = "DOES NOT FIRE"


# ── Save results ─────────────────────────────────────────────────────────
save_dict = {
    'tau_fine': tau_fine,
    'V_jensen': V_jensen,
    'A_values': A_values,
    'omega_sq_T3': np.array(omega_sq_T3),
    'omega_sq_T4': np.array(omega_sq_T4),
    'gate_verdict': np.array(gate_verdict, dtype='U20'),
}

# Save all V_Kapitza profiles
for key, res in results_all.items():
    safe_key = key.replace('.', 'p')
    save_dict[f'V_kap_{safe_key}'] = res['V_kap']
    save_dict[f'V_avg_{safe_key}'] = res['V_avg']
    save_dict[f'V_corr_{safe_key}'] = res['V_corr']

outfile = os.path.join(T0, "s31a_kapitza_gate.npz")
np.savez_compressed(outfile, **save_dict)
print(f"\nSaved: {outfile}")


# ── Plotting ─────────────────────────────────────────────────────────────
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("K-1: Kapitza Effective Potential on U(2)-Invariant Surface", fontsize=14)

# Panel 1: V_Kapitza for all A at T3 frequency
ax = axes[0, 0]
ax.plot(tau_fine, V_jensen - V_jensen[0], 'k-', linewidth=2, label='V_total (eps=0)')
for A in A_values:
    key = f"T3_A{A:.2f}"
    if key in results_all:
        V_kap = results_all[key]['V_kap']
        ax.plot(tau_fine, V_kap - V_kap[0], '--', label=f'V_Kap A={A:.2f}')
        for tm, vm, d2vm in results_all[key]['minima']:
            ax.plot(tm, vm - V_kap[0], 'ro', markersize=8)
ax.set_xlabel('tau')
ax.set_ylabel('V - V(tau=0.01)')
ax.set_title(f'omega^2 = T3 = {omega_sq_T3:.2f}')
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)

# Panel 2: V_Kapitza for all A at T4 frequency
ax = axes[0, 1]
ax.plot(tau_fine, V_jensen - V_jensen[0], 'k-', linewidth=2, label='V_total (eps=0)')
for A in A_values:
    key = f"T4_A{A:.2f}"
    if key in results_all:
        V_kap = results_all[key]['V_kap']
        ax.plot(tau_fine, V_kap - V_kap[0], '--', label=f'V_Kap A={A:.2f}')
        for tm, vm, d2vm in results_all[key]['minima']:
            ax.plot(tm, vm - V_kap[0], 'ro', markersize=8)
ax.set_xlabel('tau')
ax.set_ylabel('V - V(tau=0.01)')
ax.set_title(f'omega^2 = |T4| = {omega_sq_T4:.2f}')
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)

# Panel 3: Kapitza correction magnitude
ax = axes[1, 0]
for omega_label, omega_sq in [("T3", omega_sq_T3), ("T4", omega_sq_T4)]:
    for A in [0.05, 0.10, 0.15]:
        key = f"{omega_label}_A{A:.2f}"
        if key in results_all:
            ax.plot(tau_fine, results_all[key]['V_corr'],
                   label=f'{omega_label} A={A:.2f}')
ax.set_xlabel('tau')
ax.set_ylabel('Kapitza correction')
ax.set_title('Correction term: <(dV/deps)^2> / (4*omega^2)')
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)

# Panel 4: Gradient comparison
ax = axes[1, 1]
dV_jensen = np.gradient(V_jensen, tau_fine)
ax.plot(tau_fine, dV_jensen, 'k-', linewidth=2, label='dV_total/dtau')
for omega_label, omega_sq in [("T3", omega_sq_T3), ("T4", omega_sq_T4)]:
    key = f"{omega_label}_A0.15"
    if key in results_all:
        dV_kap = np.gradient(results_all[key]['V_kap'], tau_fine)
        ax.plot(tau_fine, dV_kap, '--', label=f'dV_Kap/dtau ({omega_label}, A=0.15)')
ax.axhline(y=0, color='r', linewidth=0.5)
ax.set_xlabel('tau')
ax.set_ylabel('dV/dtau')
ax.set_title('Gradient comparison (zero crossing = minimum)')
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plotfile = os.path.join(T0, "s31a_kapitza_gate.png")
plt.savefig(plotfile, dpi=150, bbox_inches='tight')
print(f"Saved: {plotfile}")
plt.close()

print("\nK-1 computation complete.")
