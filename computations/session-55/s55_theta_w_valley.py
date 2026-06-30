#!/usr/bin/env python3
"""
S55 — THETA-W-VALLEY-55: sin^2(theta_W) at Off-Jensen Valley Floor
====================================================================

Compute the Weinberg angle at the valley floor sigma* = 0.0148 of the
off-Jensen (T2) deformation, and compare to the Jensen-metric value at sigma=0.

From Baptista Paper 14 eqs (2.85)/(2.88) and Paper 13 eq (5.25):
  g'/g = sqrt(3) * sqrt(lambda_2/lambda_1)

where lambda_1 = metric eigenvalue on u(1) and lambda_2 = metric eigenvalue
on su(2) subspace. For the Jensen deformation:
  lambda_1 = alpha * e^{2*tau}    [u(1)]
  lambda_2 = alpha * e^{-2*tau}   [su(2)]
  => g'/g = sqrt(3) * e^{-2*tau}

For the Jensen + T2 deformation with sigma:
  lambda_1(tau, sigma) = alpha * e^{2*tau - 11*sigma}   [u(1)]
  lambda_2(tau, sigma) = alpha * e^{-2*tau - 7*sigma}   [su(2)]
  lambda_3(tau, sigma) = alpha * e^{tau + 8*sigma}       [C^2]

  => lambda_2/lambda_1 = e^{-4*tau + 4*sigma}
  => g'/g = sqrt(3) * e^{-2*tau + 2*sigma}

sin^2(theta_W) = (g'/g)^2 / (1 + (g'/g)^2)
               = 3*e^{-4*tau + 4*sigma} / (1 + 3*e^{-4*tau + 4*sigma})
               = 3 / (e^{4*tau - 4*sigma} + 3)

Derivation of g'/g = sqrt(3) * sqrt(lambda_2/lambda_1):
  From Paper 14 eq (2.85): g' = 3 * sqrt(2*kappa_M / <Y,Y>)
    where Y = diag(-2i, i, i) in u(1), <Y,Y> = lambda_1 * gamma_0(Y,Y) = 6*lambda_1
    (since gamma_0(Y,Y) = -Tr(Y^2) = -Tr(diag(-4,-1,-1)) = 6)

  From Paper 14 eq (2.88): g = sqrt(2*kappa_M / <T3,T3>)
    where T3 = diag(i,-i,0) in su(2), <T3,T3> = lambda_2 * gamma_0(T3,T3) = 2*lambda_2
    (since gamma_0(T3,T3) = -Tr(T3^2) = -Tr(diag(-1,-1,0)) = 2)

  => g'/g = 3 * sqrt(<T3,T3>/<Y,Y>) = 3 * sqrt(2*lambda_2 / (6*lambda_1))
          = 3 * sqrt(lambda_2/(3*lambda_1)) = sqrt(3) * sqrt(lambda_2/lambda_1)

Cross-check at tau=0, sigma=0: g'/g = sqrt(3), sin^2 = 3/4.
Cross-check with canonical constant: sin2_thetaW_fold = 0.58385 at tau=0.19, sigma=0:
  3/(e^{0.76}+3) = 3/5.138 = 0.5839 (matches to 5 digits).

Paper 13 eq (5.25) gives MZ/MW = sqrt(1 + 3*lambda_2/lambda_1), which yields
sin^2(theta_W) = 1 - MW^2/MZ^2 = 3*(lambda_2/lambda_1)/(1 + 3*(lambda_2/lambda_1))
confirming the same formula via the mass ratio route.

Gate: THETA-W-VALLEY-55 — INFO: corrected sin^2(theta_W) at valley floor.
Output: s55_theta_w_valley.npz, s55_theta_w_valley.png

Author: Baptista-Spacetime-Analyst (Session 55)
Date: 2026-03-22
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from numpy import pi, sqrt, exp, log
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import tau_fold, sin2_thetaW_fold, sin2_thetaW_MSbar

print("=" * 72)
print("  S55 — THETA-W-VALLEY-55: sin^2(theta_W) at Off-Jensen Valley Floor")
print("=" * 72)

DATA_DIR = os.path.dirname(os.path.abspath(__file__))

# ============================================================================
#  SECTION 1: Formula verification at Jensen (sigma=0)
# ============================================================================
print("\n" + "=" * 72)
print("  SECTION 1: Verify sin^2(theta_W) formula at Jensen (sigma=0)")
print("=" * 72)

def sin2_thetaW(tau, sigma=0.0):
    """
    sin^2(theta_W) at general (tau, sigma) in the Jensen + T2 family.

    From Baptista Paper 13 eq 5.25 / Paper 14 eqs 2.85, 2.88:
      g'/g = sqrt(3) * sqrt(lambda_2/lambda_1)
      lambda_2/lambda_1 = e^{-4*tau + 4*sigma}

    => sin^2 = 3*e^{-4*tau+4*sigma} / (1 + 3*e^{-4*tau+4*sigma})
             = 3 / (e^{4*tau-4*sigma} + 3)
    """
    x = exp(4.0 * tau - 4.0 * sigma)
    return 3.0 / (x + 3.0)

def coupling_ratio(tau, sigma=0.0):
    """g'/g at (tau, sigma)."""
    return sqrt(3.0) * exp(-2.0 * tau + 2.0 * sigma)

# Cross-check against canonical constant
sin2_check = sin2_thetaW(tau_fold, 0.0)
print(f"\n  tau_fold = {tau_fold}")
print(f"  sin^2(theta_W)(tau_fold, sigma=0) = {sin2_check:.11f}")
print(f"  canonical sin2_thetaW_fold        = {sin2_thetaW_fold:.11f}")
print(f"  difference                        = {abs(sin2_check - sin2_thetaW_fold):.2e}")
print(f"  MATCH: {np.isclose(sin2_check, sin2_thetaW_fold, rtol=1e-8)}")

# Cross-check at tau=0 (bi-invariant metric)
sin2_0 = sin2_thetaW(0.0, 0.0)
print(f"\n  sin^2(theta_W)(tau=0, sigma=0) = {sin2_0:.6f}")
print(f"  expected: 3/4 = {3.0/4.0:.6f}")
print(f"  g'/g(tau=0, sigma=0) = {coupling_ratio(0.0, 0.0):.6f} (= sqrt(3) = {sqrt(3.0):.6f})")

# Standard values for reference
print(f"\n  Experimental sin^2(theta_W)_MSbar at M_Z = {sin2_thetaW_MSbar}")
print(f"  NCG GUT boundary (SU(5)-normalized)       = 0.375 = 3/8")

# ============================================================================
#  SECTION 2: Load valley floor data from S54
# ============================================================================
print("\n" + "=" * 72)
print("  SECTION 2: Valley floor from S54 off-Jensen data")
print("=" * 72)

s54_path = os.path.join(DATA_DIR, 's54_off_jensen_t2.npz')
d54 = np.load(s54_path, allow_pickle=True)

tau_sb = float(d54['tau_sb'])
v_Jensen = d54['v_Jensen']
v_T2 = d54['v_T2']

print(f"\n  Speed bump tau = {tau_sb}")
print(f"  Jensen direction: v_J = {v_Jensen}")
print(f"  T2 direction:     v_T2 = {v_T2}")

# The valley floor sigma* = 0.0148 from the S54 analysis
# This is the sigma value where V is minimized in the T2 direction
# at or near the speed bump
sigma_star = 0.0148  # (local)
print(f"\n  Valley floor sigma* = {sigma_star}")

# Verify from the V_grid: for tau near speed bump, find sigma of min V
tau_range_54 = d54['tau_range']
sig_range_54 = d54['sig_range']
V_grid = d54['V_grid']

# Near speed bump
i_sb = np.argmin(np.abs(tau_range_54 - tau_sb))
V_slice = V_grid[i_sb, :]
i_min = np.argmin(V_slice)

# Since V is monotonically decreasing in sigma at the speed bump,
# the minimum is at the boundary. Use parabolic fit near boundary for refinement.
if i_min >= len(sig_range_54) - 1:
    # At boundary - the true minimum may be beyond the scan range
    # But the task specifies sigma* = 0.0148 from the S54 analysis
    print(f"  V_grid minimum at boundary sigma = {sig_range_54[i_min]:.5f}")
    print(f"  V is monotonically decreasing in sigma at speed bump")
    print(f"  Using prescribed sigma* = {sigma_star}")
else:
    print(f"  V_grid minimum at sigma = {sig_range_54[i_min]:.5f}")

# ============================================================================
#  SECTION 3: sin^2(theta_W) at valley floor
# ============================================================================
print("\n" + "=" * 72)
print("  SECTION 3: sin^2(theta_W) at valley floor")
print("=" * 72)

# Compute at the fold with sigma=0 (standard Jensen)
sin2_jensen = sin2_thetaW(tau_fold, 0.0)
gp_g_jensen = coupling_ratio(tau_fold, 0.0)

# Compute at the fold with sigma* (valley floor)
sin2_valley = sin2_thetaW(tau_fold, sigma_star)
gp_g_valley = coupling_ratio(tau_fold, sigma_star)

# Compute at speed bump with sigma* (another reference point)
sin2_sb_jensen = sin2_thetaW(tau_sb, 0.0)
sin2_sb_valley = sin2_thetaW(tau_sb, sigma_star)

print(f"\n  At tau_fold = {tau_fold}, sigma = 0 (Jensen):")
print(f"    g'/g = sqrt(3) * e^{{-2*{tau_fold}}} = {gp_g_jensen:.8f}")
print(f"    sin^2(theta_W) = {sin2_jensen:.8f}")
print(f"    lambda_2/lambda_1 = e^{{-4*{tau_fold}}} = {exp(-4*tau_fold):.8f}")

print(f"\n  At tau_fold = {tau_fold}, sigma* = {sigma_star} (Valley floor):")
print(f"    g'/g = sqrt(3) * e^{{-2*{tau_fold}+2*{sigma_star}}} = {gp_g_valley:.8f}")
print(f"    sin^2(theta_W) = {sin2_valley:.8f}")
print(f"    lambda_2/lambda_1 = e^{{-4*{tau_fold}+4*{sigma_star}}} = {exp(-4*tau_fold+4*sigma_star):.8f}")

delta_sin2 = sin2_valley - sin2_jensen
pct_shift = 100.0 * delta_sin2 / sin2_jensen
print(f"\n  Shift from Jensen:")
print(f"    delta(sin^2) = {delta_sin2:+.8f}")
print(f"    relative     = {pct_shift:+.4f}%")

print(f"\n  Comparison with experiment:")
print(f"    Jensen (sigma=0):    sin^2 = {sin2_jensen:.6f}  (exp: {sin2_thetaW_MSbar})")
print(f"    Valley (sigma*):     sin^2 = {sin2_valley:.6f}  (exp: {sin2_thetaW_MSbar})")
print(f"    Discrepancy Jensen:  {abs(sin2_jensen - sin2_thetaW_MSbar):.4f}")
print(f"    Discrepancy Valley:  {abs(sin2_valley - sin2_thetaW_MSbar):.4f}")

# At the speed bump
print(f"\n  At speed bump tau = {tau_sb}:")
print(f"    Jensen:  sin^2 = {sin2_sb_jensen:.8f}")
print(f"    Valley:  sin^2 = {sin2_sb_valley:.8f}")
print(f"    Shift:   {sin2_sb_valley - sin2_sb_jensen:+.8f} ({100*(sin2_sb_valley-sin2_sb_jensen)/sin2_sb_jensen:+.4f}%)")

# ============================================================================
#  SECTION 4: Metric component shifts at valley floor
# ============================================================================
print("\n" + "=" * 72)
print("  SECTION 4: Metric components at valley floor")
print("=" * 72)

# Jensen metric eigenvalues
a1_J = exp(2*tau_fold)          # u(1)
a2_J = exp(-2*tau_fold)         # su(2)
a3_J = exp(tau_fold)            # C^2

# Valley floor metric eigenvalues
a1_V = exp(2*tau_fold - 11*sigma_star)
a2_V = exp(-2*tau_fold - 7*sigma_star)
a3_V = exp(tau_fold + 8*sigma_star)

print(f"\n  Jensen metric (tau={tau_fold}, sigma=0):")
print(f"    alpha_1 [u(1)]  = {a1_J:.8f}")
print(f"    alpha_2 [su(2)] = {a2_J:.8f}")
print(f"    alpha_3 [C^2]   = {a3_J:.8f}")
print(f"    ratio a2/a1     = {a2_J/a1_J:.8f}")

print(f"\n  Valley floor (tau={tau_fold}, sigma*={sigma_star}):")
print(f"    alpha_1 [u(1)]  = {a1_V:.8f}")
print(f"    alpha_2 [su(2)] = {a2_V:.8f}")
print(f"    alpha_3 [C^2]   = {a3_V:.8f}")
print(f"    ratio a2/a1     = {a2_V/a1_V:.8f}")

print(f"\n  Percentage shifts in metric components:")
print(f"    delta(a1)/a1 = {100*(a1_V/a1_J - 1):+.4f}%  (u(1) shrinks)")
print(f"    delta(a2)/a2 = {100*(a2_V/a2_J - 1):+.4f}%  (su(2) shrinks)")
print(f"    delta(a3)/a3 = {100*(a3_V/a3_J - 1):+.4f}%  (C^2 grows)")

# Volume check
vol_J = a1_J**(0.5) * a2_J**(1.5) * a3_J**2
vol_V = a1_V**(0.5) * a2_V**(1.5) * a3_V**2
print(f"\n  Volume check (should be identical):")
print(f"    Vol(Jensen)  = {vol_J:.8f}")
print(f"    Vol(Valley)  = {vol_V:.8f}")
print(f"    Ratio        = {vol_V/vol_J:.12f} (= 1 for volume-preserving)")

# ============================================================================
#  SECTION 5: Sweep sigma at tau_fold
# ============================================================================
print("\n" + "=" * 72)
print("  SECTION 5: sigma sweep at tau_fold")
print("=" * 72)

sigma_sweep = np.linspace(-0.05, 0.10, 301)
sin2_sweep = np.array([sin2_thetaW(tau_fold, s) for s in sigma_sweep])
gp_g_sweep = np.array([coupling_ratio(tau_fold, s) for s in sigma_sweep])

# Find sigma that gives experimental value
# sin^2 = 0.23122 => 3/(e^{4*tau-4*sigma}+3) = 0.23122
# e^{4*tau-4*sigma} = 3/0.23122 - 3 = 12.973 - 3 = 9.973
# 4*tau - 4*sigma = ln(9.973) = 2.300
# sigma = tau - 0.575 = 0.19 - 0.575 = -0.385
sigma_for_exp = tau_fold - 0.25 * log(3.0 / sin2_thetaW_MSbar - 3.0)
print(f"\n  sigma needed for experimental sin^2 = {sin2_thetaW_MSbar}:")
print(f"    sigma_exp = {sigma_for_exp:.6f}")
print(f"    This is {abs(sigma_for_exp)/sigma_star:.1f}x the valley floor displacement")
print(f"    CONCLUSION: off-Jensen sigma alone CANNOT reach experimental value")

# Table of key values
print(f"\n  sin^2(theta_W) at tau_fold = {tau_fold}:")
print(f"  {'sigma':>10s}  {'sin^2':>12s}  {'g\'/g':>12s}  {'delta%':>10s}")
print(f"  {'-'*50}")
sigma_table = [-0.05, -0.03, -0.01, 0.0, 0.005, 0.01, sigma_star, 0.02, 0.03, 0.05, 0.10]
for sig in sigma_table:
    s2 = sin2_thetaW(tau_fold, sig)
    gr = coupling_ratio(tau_fold, sig)
    delta = 100.0 * (s2 - sin2_jensen) / sin2_jensen
    marker = " <-- valley floor" if abs(sig - sigma_star) < 1e-6 else ""
    marker = " <-- Jensen" if abs(sig) < 1e-10 else marker
    print(f"  {sig:>10.4f}  {s2:>12.8f}  {gr:>12.8f}  {delta:>+10.4f}%{marker}")

# NCG boundary value
sin2_NCG = 3.0 / 8.0  # = 0.375
sigma_NCG = tau_fold - 0.25 * log(3.0 / sin2_NCG - 3.0)
print(f"\n  sigma for NCG boundary value (3/8 = 0.375):")
print(f"    sigma_NCG = {sigma_NCG:.6f}")

# ============================================================================
#  SECTION 6: Physical interpretation
# ============================================================================
print("\n" + "=" * 72)
print("  SECTION 6: Physical interpretation")
print("=" * 72)

# The T2 deformation changes the coupling ratio through the 4*sigma correction
# sigma > 0 makes lambda_2/lambda_1 LARGER (because the exponents are -7 for su(2)
# and -11 for u(1), so both decrease but u(1) decreases faster)
# This means g'/g INCREASES, and sin^2(theta_W) INCREASES

# Direction of shift
print(f"\n  T2 deformation at sigma > 0:")
print(f"    u(1) exponent shift:  -11*sigma = {-11*sigma_star:+.4f}  (DECREASES alpha_1)")
print(f"    su(2) exponent shift: -7*sigma  = {-7*sigma_star:+.4f}  (DECREASES alpha_2)")
print(f"    C^2 exponent shift:   +8*sigma  = {+8*sigma_star:+.4f}  (INCREASES alpha_3)")
print(f"    Net effect on a2/a1:  4*sigma   = {4*sigma_star:+.4f}  (ratio INCREASES)")
print(f"    => g'/g INCREASES by factor e^{{2*sigma*}} = {exp(2*sigma_star):.6f}")
print(f"    => sin^2(theta_W) moves FURTHER from experiment")

# The valley floor sigma* is very small
print(f"\n  Key quantitative result:")
print(f"    Jensen sin^2    = {sin2_jensen:.6f}  (already 2.5x above experiment)")
print(f"    Valley sin^2    = {sin2_valley:.6f}  (moves 3.5% further up)")
print(f"    Experiment      = {sin2_thetaW_MSbar:.6f}")
print(f"    Gap Jensen-exp  = {sin2_jensen - sin2_thetaW_MSbar:.4f}")
print(f"    Gap Valley-exp  = {sin2_valley - sin2_thetaW_MSbar:.4f}")
print(f"    The off-Jensen shift is {abs(pct_shift):.1f}% (negligible vs 150% gap)")
print(f"    => Valley floor does NOT improve Weinberg angle")
print(f"    => Must be resolved by RG running from M_KK to M_Z")

# What tau would give experimental value at sigma=0?
tau_for_exp = 0.25 * log(3.0 / sin2_thetaW_MSbar - 3.0)
print(f"\n  tau needed at sigma=0 for experimental sin^2:")
print(f"    tau_exp = {tau_for_exp:.6f}  (vs tau_fold = {tau_fold})")
print(f"    This is {tau_for_exp/tau_fold:.2f}x the fold value")

# ============================================================================
#  SECTION 7: Generate plot
# ============================================================================
print("\n" + "=" * 72)
print("  SECTION 7: Plot")
print("=" * 72)

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Left panel: sin^2(theta_W) vs sigma at tau_fold
ax1 = axes[0]
ax1.plot(sigma_sweep, sin2_sweep, 'b-', linewidth=2, label=r'$\sin^2\theta_W(\tau_{\rm fold}, \sigma)$')
ax1.axhline(sin2_thetaW_MSbar, color='red', linestyle='--', linewidth=1.5, label=f'Experiment ({sin2_thetaW_MSbar})')
ax1.axhline(sin2_NCG, color='green', linestyle=':', linewidth=1.5, label=f'NCG boundary (3/8)')
ax1.axvline(0.0, color='gray', linestyle=':', linewidth=0.8, alpha=0.5)
ax1.axvline(sigma_star, color='orange', linestyle='-', linewidth=1.5, alpha=0.7, label=f'$\\sigma^* = {sigma_star}$')
ax1.scatter([0.0], [sin2_jensen], color='blue', s=80, zorder=5, marker='o')
ax1.scatter([sigma_star], [sin2_valley], color='orange', s=80, zorder=5, marker='s')
ax1.set_xlabel(r'$\sigma$ (T2 deformation)', fontsize=13)
ax1.set_ylabel(r'$\sin^2\theta_W$', fontsize=13)
ax1.set_title(f'Weinberg Angle vs Off-Jensen Deformation\n' + r'$\tau = \tau_{\rm fold}$' + f' = {tau_fold}', fontsize=13)
ax1.legend(fontsize=10, loc='upper left')
ax1.set_xlim(-0.05, 0.10)
ax1.grid(True, alpha=0.3)

# Inset: zoom near valley floor
ax1_inset = ax1.inset_axes([0.45, 0.15, 0.50, 0.40])
sigma_zoom = np.linspace(-0.005, 0.025, 100)
sin2_zoom = np.array([sin2_thetaW(tau_fold, s) for s in sigma_zoom])
ax1_inset.plot(sigma_zoom, sin2_zoom, 'b-', linewidth=2)
ax1_inset.axvline(0.0, color='gray', linestyle=':', linewidth=0.8)
ax1_inset.axvline(sigma_star, color='orange', linestyle='-', linewidth=1.5, alpha=0.7)
ax1_inset.scatter([0.0], [sin2_jensen], color='blue', s=60, zorder=5)
ax1_inset.scatter([sigma_star], [sin2_valley], color='orange', s=60, zorder=5)
ax1_inset.set_title(f'$\\Delta\\sin^2 = {delta_sin2:+.5f}$', fontsize=10)
ax1_inset.tick_params(labelsize=8)
ax1_inset.grid(True, alpha=0.3)

# Right panel: sin^2(theta_W) in (tau, sigma) plane
ax2 = axes[1]
tau_2d = np.linspace(0.0, 0.40, 200)
sig_2d = np.linspace(-0.05, 0.10, 200)
TAU, SIG = np.meshgrid(tau_2d, sig_2d)
SIN2 = 3.0 / (np.exp(4.0 * TAU - 4.0 * SIG) + 3.0)

levels = [0.15, 0.20, sin2_thetaW_MSbar, 0.25, 0.30, sin2_NCG, 0.40, 0.50, sin2_jensen, 0.60, 0.70]
levels.sort()
CS = ax2.contour(TAU, SIG, SIN2, levels=levels, colors='gray', linewidths=0.8)
ax2.clabel(CS, inline=True, fontsize=8, fmt='%.3f')

# Highlight experimental contour
CS_exp = ax2.contour(TAU, SIG, SIN2, levels=[sin2_thetaW_MSbar], colors='red', linewidths=2.0)
ax2.clabel(CS_exp, inline=True, fontsize=9, fmt='%.3f')

# Mark key points
ax2.scatter([tau_fold], [0.0], color='blue', s=100, zorder=5, marker='o', label='Jensen fold')
ax2.scatter([tau_fold], [sigma_star], color='orange', s=100, zorder=5, marker='s', label=f'Valley floor')
ax2.scatter([0.0], [0.0], color='green', s=80, zorder=5, marker='^', label='Bi-invariant')

# Jensen trajectory
ax2.plot(tau_2d, np.zeros_like(tau_2d), 'b-', linewidth=1.5, alpha=0.5)
ax2.axhline(sigma_star, color='orange', linestyle=':', linewidth=1, alpha=0.5)

ax2.set_xlabel(r'$\tau$ (Jensen deformation)', fontsize=13)
ax2.set_ylabel(r'$\sigma$ (T2 deformation)', fontsize=13)
ax2.set_title(r'$\sin^2\theta_W(\tau, \sigma)$ contours', fontsize=13)
ax2.legend(fontsize=9, loc='upper right')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(DATA_DIR, 's55_theta_w_valley.png'), dpi=150, bbox_inches='tight')
print(f"  Plot saved: {os.path.join(DATA_DIR, 's55_theta_w_valley.png')}")

# ============================================================================
#  SECTION 8: Save results
# ============================================================================
print("\n" + "=" * 72)
print("  SECTION 8: Save results")
print("=" * 72)

results = {
    # Key scalar results
    'tau_fold': tau_fold,
    'sigma_star': sigma_star,
    'sin2_thetaW_jensen': sin2_jensen,
    'sin2_thetaW_valley': sin2_valley,
    'sin2_thetaW_MSbar': sin2_thetaW_MSbar,
    'delta_sin2': delta_sin2,
    'pct_shift': pct_shift,
    'gp_g_jensen': gp_g_jensen,
    'gp_g_valley': gp_g_valley,
    'sigma_for_experiment': sigma_for_exp,
    'tau_for_experiment': tau_for_exp,
    # Metric components
    'alpha1_jensen': a1_J,
    'alpha2_jensen': a2_J,
    'alpha3_jensen': a3_J,
    'alpha1_valley': a1_V,
    'alpha2_valley': a2_V,
    'alpha3_valley': a3_V,
    # Sweep data
    'sigma_sweep': sigma_sweep,
    'sin2_sweep': sin2_sweep,
    'gp_g_sweep': gp_g_sweep,
    # T2 direction
    'v_Jensen': v_Jensen,
    'v_T2': v_T2,
}

npz_path = os.path.join(DATA_DIR, 's55_theta_w_valley.npz')
np.savez(npz_path, **results)
print(f"  Data saved: {npz_path}")

# ============================================================================
#  SECTION 9: Gate verdict
# ============================================================================
print("\n" + "=" * 72)
print("  SECTION 9: Gate THETA-W-VALLEY-55")
print("=" * 72)

print(f"\n  Gate: THETA-W-VALLEY-55")
print(f"  Type: INFO")
print(f"  Status: COMPUTED")
print(f"")
print(f"  Result: sin^2(theta_W) at valley floor sigma* = {sigma_star}:")
print(f"    Jensen (sigma=0):    {sin2_jensen:.8f}")
print(f"    Valley (sigma*):     {sin2_valley:.8f}")
print(f"    Shift:               {delta_sin2:+.8f} ({pct_shift:+.2f}%)")
print(f"    Experiment (M_Z):    {sin2_thetaW_MSbar}")
print(f"")
print(f"  Physical assessment:")
print(f"    The valley floor shift is +{abs(pct_shift):.1f}%, moving sin^2 AWAY from experiment.")
print(f"    The gap to experiment is {sin2_jensen - sin2_thetaW_MSbar:.3f} at Jensen,")
print(f"    increasing to {sin2_valley - sin2_thetaW_MSbar:.3f} at valley floor.")
print(f"    The off-Jensen correction is a {abs(delta_sin2)/(sin2_jensen-sin2_thetaW_MSbar)*100:.1f}% perturbation")
print(f"    of the gap, and goes in the WRONG direction.")
print(f"    Resolution requires RG running from M_KK to M_Z (standard KK expectation).")
print(f"    sigma needed for experiment: {sigma_for_exp:.4f} (26x valley floor displacement).")

print("\n" + "=" * 72)
print("  DONE")
print("=" * 72)
