#!/usr/bin/env python3
"""
Session 33a Step 2: Lie Derivative Norm along Jensen Curve.

Implement the Lie derivative norm formula from Baptista Paper 15 eq 3.67/3.84
for the Jensen family g_s on SU(3). Three diagnostic comparisons:
  1. f'(tau_dump) =? 0  (boson-fermion correspondence)
  2. f''(tau_dump) vs 16.19  (RPA-32b bare curvature comparison)
  3. f'(tau) shape vs B2 group velocity (structural connection)

Mathematical background:
    For the Jensen deformation g_K(sigma) with:
        lambda_1(s) = e^{2s},  lambda_2(s) = e^{-2s},  lambda_3(s) = e^s
    (Baptista Paper 15 eq 3.68), the gauge boson mass-squared for the C^2
    gauge fields is proportional to (eq 3.84 / eq after 3.83):

        f(s) = [(e^s - e^{-2s})^2 + (1 - e^{-s})^2] / 5

    This vanishes at s=0 (bi-invariant metric = full SU(3) isometry).
    For u(2) generators, the Lie derivative norm is identically zero
    (Killing directions).

    In our codebase, s = tau (the Jensen deformation parameter).

Author: sim (phonon-exflation-sim)
Date: 2026-03-06
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ─────────────────────────────────────────────────────────────
# 1. Define the Lie derivative norm function
# ─────────────────────────────────────────────────────────────

def lie_derivative_norm(tau):
    """Lie derivative norm f(tau) for C^2 gauge bosons on Jensen-deformed SU(3).

    From Baptista Paper 15 eq 3.83-3.84:
        f(tau) = [(e^tau - e^{-2*tau})^2 + (1 - e^{-tau})^2] / 5

    Parameters
    ----------
    tau : float or ndarray
        Jensen deformation parameter (sigma in Paper 15).

    Returns
    -------
    f : float or ndarray
        Lie derivative norm (proportional to gauge boson mass-squared).
    """
    return ((np.exp(tau) - np.exp(-2 * tau))**2 + (1 - np.exp(-tau))**2) / 5.0


def lie_derivative_norm_deriv1(tau):
    """Analytical first derivative f'(tau).

    f'(tau) = [2(e^tau - e^{-2tau})(e^tau + 2e^{-2tau}) + 2(1-e^{-tau})*e^{-tau}] / 5
    """
    a = np.exp(tau) - np.exp(-2 * tau)
    da = np.exp(tau) + 2 * np.exp(-2 * tau)
    b = 1 - np.exp(-tau)
    db = np.exp(-tau)
    return (2 * a * da + 2 * b * db) / 5.0


def lie_derivative_norm_deriv2(tau):
    """Analytical second derivative f''(tau).

    Computed by differentiating f'(tau) analytically.
    Let A = e^tau - e^{-2tau}, dA = e^tau + 2*e^{-2tau}
    d2A = e^tau - 4*e^{-2tau}
    Let B = 1 - e^{-tau}, dB = e^{-tau}, d2B = -e^{-tau}

    f'(tau) = [2*A*dA + 2*B*dB] / 5
    f''(tau) = [2*(dA)^2 + 2*A*d2A + 2*(dB)^2 + 2*B*d2B] / 5
    """
    A = np.exp(tau) - np.exp(-2 * tau)
    dA = np.exp(tau) + 2 * np.exp(-2 * tau)
    d2A = np.exp(tau) - 4 * np.exp(-2 * tau)
    B = 1 - np.exp(-tau)
    dB = np.exp(-tau)
    d2B = -np.exp(-tau)
    return (2 * dA**2 + 2 * A * d2A + 2 * dB**2 + 2 * B * d2B) / 5.0


# ─────────────────────────────────────────────────────────────
# 2. Compute on fine grid
# ─────────────────────────────────────────────────────────────

tau_grid = np.arange(0.0, 0.505, 0.005)
f_vals = lie_derivative_norm(tau_grid)
f_prime = lie_derivative_norm_deriv1(tau_grid)
f_double_prime = lie_derivative_norm_deriv2(tau_grid)

# Also compute numerical derivatives for verification
h = 0.0001
f_prime_num = (lie_derivative_norm(tau_grid + h) - lie_derivative_norm(tau_grid - h)) / (2 * h)
f_dp_num = (lie_derivative_norm(tau_grid + h) - 2 * lie_derivative_norm(tau_grid)
            + lie_derivative_norm(tau_grid - h)) / h**2

# Verify analytical vs numerical
max_err_1 = np.max(np.abs(f_prime - f_prime_num))
max_err_2 = np.max(np.abs(f_double_prime - f_dp_num))
print(f"Analytical vs numerical derivative verification:")
print(f"  f'  max error: {max_err_1:.2e}")
print(f"  f'' max error: {max_err_2:.2e}")

# ─────────────────────────────────────────────────────────────
# 3. Evaluate at dump point
# ─────────────────────────────────────────────────────────────

tau_dump = 0.190
f_at_dump = lie_derivative_norm(tau_dump)
fp_at_dump = lie_derivative_norm_deriv1(tau_dump)
fpp_at_dump = lie_derivative_norm_deriv2(tau_dump)

print(f"\n{'=' * 70}")
print(f"LIE DERIVATIVE NORM AT DUMP POINT (tau = {tau_dump})")
print(f"{'=' * 70}")
print(f"  f(tau_dump)   = {f_at_dump:.8f}")
print(f"  f'(tau_dump)  = {fp_at_dump:.8f}")
print(f"  f''(tau_dump) = {fpp_at_dump:.8f}")

# Find where f'(tau) = 0 (critical points of the Lie derivative norm)
from scipy.optimize import brentq
# f'(tau) = 0 has a root at tau = 0 (by construction). Any other roots?
# Check sign of f' on grid
sign_changes = np.where(np.diff(np.sign(f_prime[1:])))[0]  # skip tau=0
print(f"\n  f'(tau) sign changes (excluding tau=0): {len(sign_changes)}")
for sc in sign_changes:
    idx = sc + 1  # offset from skipping tau=0
    tau_a, tau_b = tau_grid[idx], tau_grid[idx + 1]
    try:
        tau_zero = brentq(lie_derivative_norm_deriv1, tau_a, tau_b)
        print(f"    f'(tau) = 0 at tau = {tau_zero:.6f}")
    except:
        pass

# ─────────────────────────────────────────────────────────────
# 4. Diagnostic comparisons
# ─────────────────────────────────────────────────────────────

print(f"\n{'=' * 70}")
print(f"DIAGNOSTIC COMPARISONS")
print(f"{'=' * 70}")

# Comparison 1: f'(0.190) vs 0 (boson-fermion correspondence)
print(f"\n  [1] f'(tau_dump = 0.190) = {fp_at_dump:.8f}")
print(f"      Expected if B-F correspondence: 0")
print(f"      Mismatch: {fp_at_dump:.8f} (finite-N correction)")
if abs(fp_at_dump) < 0.01:
    print(f"      Assessment: SMALL (< 0.01)")
elif abs(fp_at_dump) < 0.1:
    print(f"      Assessment: MODERATE (0.01-0.1)")
else:
    print(f"      Assessment: LARGE (> 0.1)")

# Comparison 2: f''(0.190) vs 16.19 (RPA-32b bare curvature)
rpa_bare = 16.19
print(f"\n  [2] f''(tau_dump = 0.190) = {fpp_at_dump:.8f}")
print(f"      RPA-32b bare curvature:    {rpa_bare:.2f}")
print(f"      Ratio f''/bare = {fpp_at_dump / rpa_bare:.6f}")
print(f"      Mismatch: {abs(fpp_at_dump - rpa_bare):.4f}")
print(f"      Assessment: f'' is the Riemannian geometry curvature for a SINGLE")
print(f"        C^2 gauge boson mass^2. The RPA-32b bare curvature is")
print(f"        d^2(sum_k |lambda_k|)/dtau^2, summing over ALL Dirac eigenvalues.")
print(f"        These are DIFFERENT quantities -- f'' is O(1) while bare curvature")
print(f"        is O(N_eigenvalues). The comparison tests whether f'' scales with")
print(f"        the PER-MODE curvature: bare_curvature / N_modes_contributing.")

# Per-mode comparison
# RPA-32b: bare curvature 16.19 from sum over all modes
# How many modes contribute? At N_max=6, 11424 eigenvalues total
# But many are far from the fold and contribute little curvature
# The B2 contribution: a_2 = 1.1757 per mode * 4 modes = ~4.7
# So per-mode curvature for B2 is ~1.18
b2_per_mode = 1.1757
print(f"\n      B2 per-mode curvature (d^2 lambda_B2/dtau^2): {b2_per_mode:.4f}")
print(f"      f''(0.190): {fpp_at_dump:.4f}")
print(f"      Ratio f''/B2_per_mode: {fpp_at_dump / b2_per_mode:.4f}")

# Comparison 3: f'(tau) shape vs B2 group velocity
# Load B2 trajectory from LANDAU-SECTOR results
try:
    d_ls = np.load('tier0-computation/s33a_landau_sector.npz', allow_pickle=True)
    b2_traj = d_ls['b2_centroid_00']
    tau_ls = d_ls['tau_values']
    from scipy.interpolate import CubicSpline
    cs_b2 = CubicSpline(tau_ls, b2_traj)
    # B2 group velocity = d(lambda_B2)/d(tau)
    tau_comp = np.linspace(0.05, 0.45, 500)
    v_b2 = cs_b2(tau_comp, 1)
    # Normalize f' and v_B2 for shape comparison
    fp_comp = lie_derivative_norm_deriv1(tau_comp)
    # Correlation
    corr = np.corrcoef(fp_comp, v_b2)[0, 1]
    print(f"\n  [3] Shape comparison: f'(tau) vs d(lambda_B2)/dtau")
    print(f"      Pearson correlation (tau in [0.05, 0.45]): {corr:.6f}")
    if corr > 0.95:
        print(f"      Assessment: STRONG correspondence (corr > 0.95)")
    elif corr > 0.80:
        print(f"      Assessment: MODERATE correspondence (corr > 0.80)")
    else:
        print(f"      Assessment: WEAK correspondence (corr < 0.80)")

    # Zero crossings comparison
    # f' = 0 at tau = 0 only (monotonically increasing for tau > 0)
    # v_B2 = 0 at tau ~ 0.190
    print(f"      f' zero crossing: only at tau = 0 (monotone for tau > 0)")
    print(f"      v_B2 zero crossing: tau ~ 0.190 (B2 minimum)")
    print(f"      --> f'(tau) does NOT have a zero at tau = 0.190")
    print(f"      --> Boson-fermion correspondence FAILS for zero-crossing location")
    print(f"      --> f'(0.190) = {fp_at_dump:.6f} is positive and substantial")
except Exception as e:
    print(f"\n  [3] Could not load B2 trajectory: {e}")

# ─────────────────────────────────────────────────────────────
# 5. Additional analysis: where is f minimal rate of change?
# ─────────────────────────────────────────────────────────────

print(f"\n{'=' * 70}")
print(f"ADDITIONAL: f(tau) STRUCTURAL FEATURES")
print(f"{'=' * 70}")

# f(tau) is monotonically increasing for tau > 0 (no minimum except at tau=0)
print(f"  f(0) = {lie_derivative_norm(0.0):.10f} (exactly 0)")
print(f"  f'(0) = {lie_derivative_norm_deriv1(0.0):.10f} (exactly 0)")
print(f"  f''(0) = {lie_derivative_norm_deriv2(0.0):.10f}")
print(f"  f(tau) is monotonically increasing for tau > 0 (all f' > 0)")

# f''(tau) = 0 location (inflection point of f = maximum deceleration of mass growth)
fp_sign = np.sign(f_double_prime)
infl_changes = np.where(np.diff(fp_sign))[0]
print(f"\n  f''(tau) = 0 (inflection points):")
for ic in infl_changes:
    try:
        tau_infl = brentq(lie_derivative_norm_deriv2, tau_grid[ic], tau_grid[ic + 1])
        print(f"    tau = {tau_infl:.6f} (f = {lie_derivative_norm(tau_infl):.8f})")
    except:
        pass

# Table of key values
print(f"\n  Key values:")
for t in [0.0, 0.10, 0.15, 0.190, 0.20, 0.25, 0.30, 0.40, 0.50]:
    print(f"    tau={t:.3f}: f={lie_derivative_norm(t):.8f}, "
          f"f'={lie_derivative_norm_deriv1(t):.8f}, "
          f"f''={lie_derivative_norm_deriv2(t):.8f}")

# ─────────────────────────────────────────────────────────────
# 6. Plot
# ─────────────────────────────────────────────────────────────

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: f(tau)
ax = axes[0, 0]
ax.plot(tau_grid, f_vals, 'b-', linewidth=2)
ax.axvline(x=0.190, color='red', linestyle='--', alpha=0.7, label='tau=0.190')
ax.plot(0.190, lie_derivative_norm(0.190), 'r*', markersize=12)
ax.set_xlabel('tau')
ax.set_ylabel('f(tau)')
ax.set_title('Lie Derivative Norm ||L_e g_K||^2 / (2 g_K(e,e))')
ax.legend()
ax.grid(True, alpha=0.3)

# Panel 2: f'(tau) vs B2 group velocity
ax = axes[0, 1]
ax.plot(tau_grid, f_prime, 'b-', linewidth=2, label="f'(tau) [bosonic]")
try:
    # Rescale v_B2 to match f' range for visual comparison
    scale = np.max(np.abs(f_prime[10:])) / np.max(np.abs(v_b2))
    ax.plot(tau_comp, v_b2 * scale, 'g--', linewidth=2,
            label=f"v_B2 (scaled x{scale:.1f}) [fermionic]")
except:
    pass
ax.axhline(y=0, color='black', linewidth=0.5)
ax.axvline(x=0.190, color='red', linestyle='--', alpha=0.7, label='tau=0.190')
ax.set_xlabel('tau')
ax.set_ylabel("f'(tau)")
ax.set_title("First Derivative: Bosonic f' vs Fermionic v_B2")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 3: f''(tau)
ax = axes[1, 0]
ax.plot(tau_grid, f_double_prime, 'b-', linewidth=2)
ax.axvline(x=0.190, color='red', linestyle='--', alpha=0.7, label='tau=0.190')
ax.axhline(y=b2_per_mode, color='green', linestyle=':', alpha=0.7,
           label=f'B2 d2/dtau2 = {b2_per_mode:.3f}')
ax.plot(0.190, fpp_at_dump, 'r*', markersize=12)
ax.set_xlabel('tau')
ax.set_ylabel("f''(tau)")
ax.set_title("Second Derivative: Curvature Comparison")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 4: Ratio f''(tau) / B2 per-mode curvature (if B2 data available)
ax = axes[1, 1]
# Just plot f''(tau) and the B2 per-mode curvature
ax.plot(tau_grid, f_double_prime, 'b-', linewidth=2, label="f''(tau)")
ax.axhline(y=b2_per_mode, color='green', linestyle=':', alpha=0.7,
           label=f'B2 per-mode: {b2_per_mode:.3f}')
ax.axhline(y=rpa_bare, color='orange', linestyle=':', alpha=0.7,
           label=f'RPA bare total: {rpa_bare:.2f}')
ax.axvline(x=0.190, color='red', linestyle='--', alpha=0.7)
ax.set_xlabel('tau')
ax.set_ylabel("Curvature")
ax.set_title("f'' vs Spectral Curvatures")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

plt.suptitle('Session 33a: Lie Derivative Norm (Baptista Paper 15 eq 3.67/3.84)',
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('tier0-computation/s33a_lie_derivative_norm.png', dpi=150, bbox_inches='tight')
print("\nPlot saved: tier0-computation/s33a_lie_derivative_norm.png")

# ─────────────────────────────────────────────────────────────
# 7. Save
# ─────────────────────────────────────────────────────────────

np.savez('tier0-computation/s33a_lie_derivative_norm.npz',
         tau_grid=tau_grid,
         f_vals=f_vals,
         f_prime=f_prime,
         f_double_prime=f_double_prime,
         tau_dump=np.array([tau_dump]),
         f_at_dump=np.array([f_at_dump]),
         fp_at_dump=np.array([fp_at_dump]),
         fpp_at_dump=np.array([fpp_at_dump]),
         b2_per_mode=np.array([b2_per_mode]),
         rpa_bare_curvature=np.array([rpa_bare]),
         )
print("Data saved: tier0-computation/s33a_lie_derivative_norm.npz")

# ─────────────────────────────────────────────────────────────
# 8. Summary
# ─────────────────────────────────────────────────────────────

print(f"\n{'=' * 70}")
print(f"SUMMARY: Lie Derivative Norm Diagnostic")
print(f"{'=' * 70}")
print(f"  f(tau) = [(e^tau - e^{{-2tau}})^2 + (1 - e^{{-tau}})^2] / 5")
print(f"  f(0.190) = {f_at_dump:.8f}")
print(f"  f'(0.190) = {fp_at_dump:.8f} (NOT zero: no B-F correspondence at dump)")
print(f"  f''(0.190) = {fpp_at_dump:.8f}")
print(f"  B2 per-mode d^2 lambda/dtau^2 = {b2_per_mode:.4f}")
print(f"  Ratio f''/B2_per_mode = {fpp_at_dump / b2_per_mode:.4f}")
print(f"  RPA-32b bare curvature = {rpa_bare:.2f}")
print(f"  f(tau) is monotonically increasing for tau > 0 (all f' > 0)")
print(f"  The dump point is NOT a stationary point of f(tau)")
print(f"  Finite-N correction: f'(0.190) = {fp_at_dump:.6f}")
