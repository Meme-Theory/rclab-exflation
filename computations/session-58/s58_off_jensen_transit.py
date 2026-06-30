#!/usr/bin/env python3
"""
s58_off_jensen_transit.py — OFF-JENSEN-TRANSIT-58
=================================================
Solve the 2D equations of motion for (tau(t), sigma(t)) in the off-Jensen
potential landscape E_J(tau, sigma).

Gate: OFF-JENSEN-TRANSIT-58 (INFO)
Criterion: sigma(tau_fold) > 0.01?

Method:
  1. Construct 2D potential V(tau, sigma) from E_J_B grid (s57_off_jensen_ej.npz)
  2. Build interpolated potential + gradient on (tau, sigma) grid
  3. Lagrangian: L = (1/2)*G_J*dtau^2 + (1/2)*G_T2*dsigma^2 - V(tau, sigma)
     with G_T2 = 26.2 * G_J (BAP master collab)
  4. Euler-Lagrange equations -> second-order ODEs
  5. Initial conditions from scale factor H(tau) = dtau/dt
  6. Three perturbation runs: sigma_0 = 1e-6, 1e-4, 1e-2
  7. RK45 adaptive integration

Author: Schwarzschild-Penrose-Geometer (S58)
"""

import numpy as np
from scipy.interpolate import RectBivariateSpline
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from canonical_constants import (
    tau_fold, M_ATDHFB, dt_transit, v_terminal,
    G_DeWitt, omega_tau
)

# ==============================================================================
# 1. Load data
# ==============================================================================

data_ej = np.load(os.path.join(os.path.dirname(__file__), 's57_off_jensen_ej.npz'),
                  allow_pickle=True)
data_sf = np.load(os.path.join(os.path.dirname(__file__), 's54_scale_factor.npz'),
                  allow_pickle=True)

tau_grid = data_ej['tau_range']   # (51,) from 0 to 0.4
sig_grid = data_ej['sig_range']   # (41,) from -0.015 to 0.015
E_J_B = data_ej['E_J_B']         # (51, 41) — E_J landscape

# Scale factor data
tau_sf = data_sf['tau']           # (10,) from 0 to 0.347
H_sf = data_sf['H']              # (10,) — H = dtau/dt in M_KK units

# Hessian data at saddle
H_ej_saddle = data_ej['EJ_B_Hessian_at_saddle']  # 2x2
H_ej_evals = data_ej['EJ_B_Hessian_evals']       # [-0.0856, +0.0841]

print("=" * 70)
print("OFF-JENSEN-TRANSIT-58: 2D Transit Dynamics")
print("=" * 70)

# ==============================================================================
# 2. Build interpolated potential and its derivatives
# ==============================================================================

# RectBivariateSpline expects (x, y, z) where z[i,j] = f(x[i], y[j])
# tau = x, sigma = y
# Use degree 3 (cubic) for smooth derivatives
V_interp = RectBivariateSpline(tau_grid, sig_grid, E_J_B, kx=3, ky=3)

def V_func(tau_val, sig_val):
    """Potential V(tau, sigma) from interpolated E_J_B."""
    return float(V_interp(tau_val, sig_val, grid=False))

def dV_dtau(tau_val, sig_val):
    """dV/dtau from spline derivative."""
    return float(V_interp(tau_val, sig_val, dx=1, grid=False))

def dV_dsig(tau_val, sig_val):
    """dV/dsigma from spline derivative."""
    return float(V_interp(tau_val, sig_val, dy=1, grid=False))

# Verify interpolation at grid points
V_test = V_interp(tau_grid[25], sig_grid[20], grid=False)
print(f"\nInterpolation check: V(0.2, 0) = {float(V_test):.10f}")
print(f"Grid value:          E_J_B[25,20] = {E_J_B[25, 20]:.10f}")
print(f"Difference: {abs(float(V_test) - E_J_B[25,20]):.2e}")

# ==============================================================================
# 3. Interpolate H(tau) = dtau/dt from scale factor
# ==============================================================================

from scipy.interpolate import interp1d

# H(tau) from s54 scale factor
H_interp = interp1d(tau_sf, H_sf, kind='cubic', fill_value='extrapolate')

# At tau=0: dtau/dt = H(0) ~ 3.95
print(f"\nH(0) = dtau/dt at tau=0: {H_interp(0.0):.4f} M_KK")
print(f"H(fold) = dtau/dt at tau=0.19: {H_interp(0.19):.4f} M_KK")

# ==============================================================================
# 4. Set up equations of motion
# ==============================================================================

# Lagrangian: L = (1/2) G_J (dtau/dt)^2 + (1/2) G_T2 (dsigma/dt)^2 - V(tau, sigma)
#
# G_J = collective inertia for tau direction
# G_T2 = 26.2 * G_J for sigma direction (BAP master collab, transverse mass)
#
# From S42: G_DeWitt = 5.0, but the actual kinetic term uses M_ATDHFB = 1.695
# The gradient stiffness Z_fold = 74730.76
# For consistency with the scale factor data where H = dtau/dt,
# use the kinetic term (1/2)*M_eff*(dtau/dt)^2
#
# The key physics: M_ATDHFB = 1.695 is the tau-direction mass.
# The sigma-direction mass is 26.2 times larger.

G_J = M_ATDHFB                    # tau-direction mass = 1.695 M_KK
G_T2_ratio = 26.2                 # from BAP master collab  # (local)
G_sigma = G_T2_ratio * G_J        # sigma-direction mass = 44.409 M_KK

print(f"\nKinetic coefficients:")
print(f"  G_J (tau mass) = {G_J:.4f} M_KK")
print(f"  G_sigma (sigma mass) = {G_sigma:.4f} M_KK")
print(f"  G_sigma/G_J = {G_T2_ratio:.1f}")

# Euler-Lagrange equations:
#   G_J * d2tau/dt2 = -dV/dtau
#   G_sigma * d2sigma/dt2 = -dV/dsigma
#
# State vector: y = [tau, sigma, dtau/dt, dsigma/dt]

def eom(t, y):
    """Equations of motion for 2D modulus dynamics."""
    tau_val, sig_val, dtau_dt, dsig_dt = y

    # Clamp to grid bounds for interpolation safety
    tau_c = np.clip(tau_val, tau_grid[0] + 1e-10, tau_grid[-1] - 1e-10)
    sig_c = np.clip(sig_val, sig_grid[0] + 1e-10, sig_grid[-1] - 1e-10)

    # Forces from potential
    F_tau = -dV_dtau(tau_c, sig_c)
    F_sig = -dV_dsig(tau_c, sig_c)

    # Accelerations
    d2tau = F_tau / G_J
    d2sig = F_sig / G_sigma

    return [dtau_dt, dsig_dt, d2tau, d2sig]

# ==============================================================================
# 5. Initial conditions and integration
# ==============================================================================

# Initial dtau/dt from scale factor
dtau_dt_0 = float(H_interp(0.0))  # ~ 3.95 M_KK

# The E_J potential has a NEGATIVE d2V/dsig2 everywhere along Jensen.
# But the gradient dV/dsig at sigma=0 is tiny (~1e-3 to 1e-6).
# The initial dsigma/dt = 0 (no initial sigma velocity).

# Three sigma perturbation levels
sigma_perturbations = [1e-6, 1e-4, 1e-2]

# Integration time: from tau=0 to tau=fold
# Rough estimate: dt ~ 0.19 / 3.85 ~ 0.049 M_KK^{-1}
# But use the canonical dt_transit = 0.00113 from S38 for the fold crossing
# More precisely: integrate until tau reaches tau_fold or slightly beyond
t_max = 0.15  # generous upper bound in M_KK^{-1} units (local)

print(f"\nInitial conditions:")
print(f"  tau_0 = 0")
print(f"  dtau/dt_0 = {dtau_dt_0:.4f} M_KK")
print(f"  dsigma/dt_0 = 0")
print(f"  Target: tau_fold = {tau_fold}")
print(f"  t_max = {t_max} M_KK^{{-1}}")

# Event function: stop when tau reaches tau_fold
def event_fold(t, y):
    return y[0] - tau_fold
event_fold.terminal = True
event_fold.direction = 1

# Also stop if sigma exits grid
def event_sigma_exit(t, y):
    return min(y[1] - sig_grid[0], sig_grid[-1] - y[1])
event_sigma_exit.terminal = True

# Also stop if tau exits grid
def event_tau_exit(t, y):
    return tau_grid[-1] - y[0]
event_tau_exit.terminal = True

results = {}

print("\n" + "=" * 70)
print("INTEGRATION RESULTS")
print("=" * 70)

for sig0 in sigma_perturbations:
    print(f"\n--- sigma_0 = {sig0:.1e} ---")

    y0 = [0.0, sig0, dtau_dt_0, 0.0]

    sol = solve_ivp(
        eom, [0, t_max], y0,
        method='RK45',
        rtol=1e-12, atol=1e-14,
        events=[event_fold, event_sigma_exit, event_tau_exit],
        dense_output=True,
        max_step=1e-4
    )

    tau_sol = sol.y[0]
    sig_sol = sol.y[1]
    dtau_sol = sol.y[2]
    dsig_sol = sol.y[3]
    t_sol = sol.t

    # Find sigma at tau_fold
    if sol.t_events[0].size > 0:
        t_fold = sol.t_events[0][0]
        y_fold = sol.sol(t_fold)
        sig_at_fold = y_fold[1]
        dsig_at_fold = y_fold[3]
        status = "reached fold"
    else:
        t_fold = sol.t[-1]
        y_fold = sol.y[:, -1]
        sig_at_fold = y_fold[1]
        dsig_at_fold = y_fold[3]
        status = f"terminated: {sol.message}"

    # Growth factor
    if sig0 > 0:
        growth = sig_at_fold / sig0
    else:
        growth = 0.0

    # Maximum sigma during transit
    sig_max = np.max(np.abs(sig_sol))

    # Sigma at various tau checkpoints
    tau_checks = [0.05, 0.10, 0.15, tau_fold]
    sig_at_checks = []
    for tc in tau_checks:
        # Find time when tau crosses tc
        idx = np.searchsorted(tau_sol, tc)
        if idx < len(tau_sol):
            sig_at_checks.append(sig_sol[idx])
        else:
            sig_at_checks.append(np.nan)

    print(f"  Status: {status}")
    print(f"  t_fold = {t_fold:.6e} M_KK^{{-1}}")
    print(f"  sigma(tau_fold) = {sig_at_fold:.6e}")
    print(f"  dsigma/dt(fold) = {dsig_at_fold:.6e}")
    print(f"  Growth factor sigma(fold)/sigma_0 = {growth:.6f}")
    print(f"  Max |sigma| during transit = {sig_max:.6e}")
    print(f"  Sigma at checkpoints:")
    for tc, sc in zip(tau_checks, sig_at_checks):
        print(f"    tau={tc:.3f}: sigma={sc:.6e}")

    results[sig0] = {
        't': t_sol,
        'tau': tau_sol,
        'sigma': sig_sol,
        'dtau': dtau_sol,
        'dsigma': dsig_sol,
        't_fold': t_fold,
        'sigma_at_fold': sig_at_fold,
        'dsig_at_fold': dsig_at_fold,
        'growth_factor': growth,
        'sigma_max': sig_max,
        'sig_at_checks': sig_at_checks,
        'sol': sol
    }

# ==============================================================================
# 6. Analytical estimates for comparison
# ==============================================================================

print("\n" + "=" * 70)
print("ANALYTICAL ESTIMATES")
print("=" * 70)

# The sigma equation is approximately:
#   G_sigma * d2sigma/dt2 = -dV/dsigma
# Near sigma=0: dV/dsigma ~ (d2V/dsig2) * sigma + (dV/dsig)|_{sig=0}
# d2V/dsig2 < 0 everywhere (unstable)
# So sigma satisfies: d2sigma/dt2 = omega_sigma^2 * sigma + f(tau)
# where omega_sigma^2 = |d2V/dsig2| / G_sigma

# Compute omega_sigma^2 along Jensen
dsig = sig_grid[1] - sig_grid[0]
idx_s0 = 20
d2V_dsig2_Jensen = np.zeros(len(tau_grid))
dV_dsig_Jensen = np.zeros(len(tau_grid))
for i in range(len(tau_grid)):
    d2V_dsig2_Jensen[i] = (E_J_B[i, idx_s0+1] - 2*E_J_B[i, idx_s0] + E_J_B[i, idx_s0-1]) / dsig**2
    dV_dsig_Jensen[i] = (E_J_B[i, idx_s0+1] - E_J_B[i, idx_s0-1]) / (2*dsig)

omega_sig_sq = np.abs(d2V_dsig2_Jensen) / G_sigma
omega_sig = np.sqrt(omega_sig_sq)

print(f"\nSigma instability rate omega_sigma(tau):")
for i in range(0, len(tau_grid), 5):
    print(f"  tau={tau_grid[i]:.3f}: omega_sigma={omega_sig[i]:.6f} M_KK, "
          f"d2V/dsig2={d2V_dsig2_Jensen[i]:.6f}, dV/dsig(sig=0)={dV_dsig_Jensen[i]:.4e}")

# Transit time estimate
dt_transit_est = tau_fold / dtau_dt_0
print(f"\nTransit time estimate: dt ~ {dt_transit_est:.4f} M_KK^{{-1}}")
print(f"Canonical dt_transit: {dt_transit:.6f} M_KK^{{-1}}")

# Growth factor from linear analysis:
# sigma(t) ~ sigma_0 * cosh(omega_sigma * t)
# Average omega_sigma over transit
omega_avg = np.mean(omega_sig[:25])  # average over tau in [0, 0.2]
growth_linear = np.cosh(omega_avg * dt_transit_est)
growth_exp = np.exp(omega_avg * dt_transit_est)

print(f"\nAverage omega_sigma over transit: {omega_avg:.6f} M_KK")
print(f"omega_sigma * dt_transit: {omega_avg * dt_transit_est:.6f}")
print(f"Linear growth estimate cosh(omega*dt): {growth_linear:.8f}")
print(f"Exponential growth estimate exp(omega*dt): {growth_exp:.8f}")

# Workshop V4/V8 comparison
omega_V4 = np.sqrt(0.0856 / G_sigma)  # from Hessian eigenvalue at saddle
t_grow_V4 = 1.0 / omega_V4
print(f"\nWorkshop V4/V8 comparison:")
print(f"  omega_sigma at saddle = {omega_V4:.6f} M_KK")
print(f"  Growth time 1/omega = {t_grow_V4:.4f} M_KK^{{-1}}")
print(f"  Transit time = {dt_transit_est:.4f} M_KK^{{-1}}")
print(f"  Ratio t_grow/t_transit = {t_grow_V4/dt_transit_est:.2f}")
print(f"  Growth factor exp(dt/t_grow) = {np.exp(dt_transit_est/t_grow_V4):.8f}")

# ==============================================================================
# 7. Compute Lyapunov-like exponent from numerical solutions
# ==============================================================================

print("\n" + "=" * 70)
print("GROWTH CHARACTERIZATION")
print("=" * 70)

for sig0 in sigma_perturbations:
    r = results[sig0]

    # Check if sigma grows, oscillates, or decays
    sig = r['sigma']
    tau = r['tau']

    # Compute local growth rate: d(ln|sigma|)/dtau
    idx_valid = np.where(np.abs(sig) > 1e-30)[0]
    if len(idx_valid) > 10:
        ln_sig = np.log(np.abs(sig[idx_valid]))
        tau_v = tau[idx_valid]
        # Fit linear growth in ln|sigma| vs tau
        if len(tau_v) > 2:
            coeffs = np.polyfit(tau_v, ln_sig, 1)
            growth_rate = coeffs[0]  # d(ln|sigma|)/dtau
            print(f"\nsigma_0 = {sig0:.1e}:")
            print(f"  d(ln|sigma|)/dtau = {growth_rate:.6f}")
            print(f"  sigma(fold)/sigma_0 = {r['growth_factor']:.8f}")
            if r['growth_factor'] > 1:
                print(f"  Classification: GROWING (rate {growth_rate:.4f}/tau)")
            elif r['growth_factor'] < 1:
                print(f"  Classification: DECAYING (rate {growth_rate:.4f}/tau)")
            else:
                print(f"  Classification: FROZEN")

# ==============================================================================
# 8. Check the driving force: dV/dsig at sigma=0
# ==============================================================================

print("\n" + "=" * 70)
print("DRIVING FORCE ANALYSIS")
print("=" * 70)

# The asymmetric gradient dV/dsig at sigma=0 acts as a constant force
# This is NOT from the perturbation but from the potential asymmetry
print("\ndV/dsigma along Jensen (sigma=0):")
for i in range(0, len(tau_grid), 5):
    # Force on sigma
    F_sig = -dV_dsig_Jensen[i]
    # Acceleration
    a_sig = F_sig / G_sigma
    print(f"  tau={tau_grid[i]:.3f}: dV/dsig={dV_dsig_Jensen[i]:.4e}, "
          f"F_sig={F_sig:.4e}, accel={a_sig:.4e}")

# Sigma displacement from asymmetric force alone (sigma_0=0 case):
# d2sigma/dt2 = -dV/dsig / G_sigma ~ const
# sigma(t) ~ (1/2) * a * t^2
a_avg = np.mean(np.abs(dV_dsig_Jensen[:25])) / G_sigma
sig_force = 0.5 * a_avg * dt_transit_est**2
print(f"\nAsymmetric force sigma displacement: ~{sig_force:.4e}")
print(f"(From constant-acceleration estimate over transit)")

# ==============================================================================
# 9. Gate assessment
# ==============================================================================

print("\n" + "=" * 70)
print("GATE VERDICT: OFF-JENSEN-TRANSIT-58")
print("=" * 70)

# Collect sigma(fold) values
sig_folds = {sig0: results[sig0]['sigma_at_fold'] for sig0 in sigma_perturbations}
sig_max_all = max(abs(r['sigma_at_fold']) for r in results.values())

print(f"\nCriterion: sigma(tau_fold) > 0.01?")
for sig0, sf in sig_folds.items():
    exceeds = "YES" if abs(sf) > 0.01 else "NO"
    print(f"  sigma_0={sig0:.1e}: sigma(fold) = {sf:.6e}  Exceeds 0.01? {exceeds}")

gate_pass = sig_max_all > 0.01
print(f"\nMaximum |sigma(fold)| across all runs: {sig_max_all:.6e}")
print(f"Gate INFO result: sigma(fold) > 0.01 = {gate_pass}")

if not gate_pass:
    print("\nSigma stays FROZEN during transit.")
    print("The off-Jensen direction is NOT dynamically accessed.")
    print("Kinematic suppression confirmed: transit too fast for sigma instability.")
else:
    print("\nSigma GROWS during transit — off-Jensen direction accessed.")

# ==============================================================================
# 10. Save results
# ==============================================================================

# Prepare arrays for each perturbation
save_dict = {
    'sigma_perturbations': np.array(sigma_perturbations),
    'tau_fold': np.float64(tau_fold),
    'G_J': np.float64(G_J),
    'G_sigma': np.float64(G_sigma),
    'G_T2_ratio': np.float64(G_T2_ratio),
    'dtau_dt_0': np.float64(dtau_dt_0),
    'd2V_dsig2_Jensen': d2V_dsig2_Jensen,
    'dV_dsig_Jensen': dV_dsig_Jensen,
    'omega_sig': omega_sig,
    'tau_grid_omega': tau_grid,
    'omega_avg': np.float64(omega_avg),
    'dt_transit_est': np.float64(dt_transit_est),
    'growth_linear_est': np.float64(growth_linear),
    'gate_name': np.array(['OFF-JENSEN-TRANSIT-58']),
    'gate_result': np.array(['INFO']),
}

for i, sig0 in enumerate(sigma_perturbations):
    r = results[sig0]
    save_dict[f'run{i}_sigma0'] = np.float64(sig0)
    save_dict[f'run{i}_sigma_at_fold'] = np.float64(r['sigma_at_fold'])
    save_dict[f'run{i}_growth_factor'] = np.float64(r['growth_factor'])
    save_dict[f'run{i}_sigma_max'] = np.float64(r['sigma_max'])
    save_dict[f'run{i}_t_fold'] = np.float64(r['t_fold'])
    save_dict[f'run{i}_tau'] = r['tau']
    save_dict[f'run{i}_sigma'] = r['sigma']
    save_dict[f'run{i}_t'] = r['t']

outpath = os.path.join(os.path.dirname(__file__), 's58_off_jensen_transit.npz')
np.savez(outpath, **save_dict)
print(f"\nSaved: {outpath}")

# ==============================================================================
# 11. Plot
# ==============================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('OFF-JENSEN-TRANSIT-58: 2D Transit Dynamics', fontsize=14, fontweight='bold')

# Panel 1: sigma(tau) trajectories
ax = axes[0, 0]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
for i, sig0 in enumerate(sigma_perturbations):
    r = results[sig0]
    ax.plot(r['tau'], r['sigma'], color=colors[i], linewidth=1.5,
            label=f'$\\sigma_0 = {sig0:.0e}$')
ax.axvline(tau_fold, color='red', linestyle='--', alpha=0.5, label=f'$\\tau_{{fold}}={tau_fold}$')
ax.axhline(0.01, color='gray', linestyle=':', alpha=0.5, label='threshold 0.01')
ax.axhline(-0.01, color='gray', linestyle=':', alpha=0.5)
ax.set_xlabel('$\\tau$')
ax.set_ylabel('$\\sigma(\\tau)$')
ax.set_title('$\\sigma(\\tau)$ trajectories')
ax.legend(fontsize=8)
ax.set_xlim(0, 0.25)

# Panel 2: Growth factor sigma/sigma_0
ax = axes[0, 1]
for i, sig0 in enumerate(sigma_perturbations):
    r = results[sig0]
    ratio = r['sigma'] / sig0
    ax.plot(r['tau'], ratio, color=colors[i], linewidth=1.5,
            label=f'$\\sigma_0 = {sig0:.0e}$')
ax.axvline(tau_fold, color='red', linestyle='--', alpha=0.5)
ax.axhline(1.0, color='gray', linestyle=':', alpha=0.5)
ax.set_xlabel('$\\tau$')
ax.set_ylabel('$\\sigma(\\tau) / \\sigma_0$')
ax.set_title('Growth factor')
ax.legend(fontsize=8)
ax.set_xlim(0, 0.25)

# Panel 3: Instability rate omega_sigma(tau)
ax = axes[1, 0]
ax.plot(tau_grid, omega_sig, 'k-', linewidth=2)
ax.axvline(tau_fold, color='red', linestyle='--', alpha=0.5, label=f'$\\tau_{{fold}}$')
ax.set_xlabel('$\\tau$')
ax.set_ylabel('$\\omega_\\sigma$ (M$_{KK}$)')
ax.set_title('$\\sigma$-instability rate $\\omega_\\sigma(\\tau) = \\sqrt{|\\partial^2 V/\\partial\\sigma^2|/G_\\sigma}$')
ax.legend(fontsize=8)

# Panel 4: d2V/dsig2 and dV/dsig along Jensen
ax = axes[1, 1]
ax.plot(tau_grid, d2V_dsig2_Jensen, 'b-', linewidth=2, label='$\\partial^2 V/\\partial\\sigma^2$')
ax2 = ax.twinx()
ax2.plot(tau_grid, dV_dsig_Jensen, 'r-', linewidth=1.5, alpha=0.7, label='$\\partial V/\\partial\\sigma|_{\\sigma=0}$')
ax.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5)
ax.axhline(0, color='gray', linestyle=':', alpha=0.3)
ax.set_xlabel('$\\tau$')
ax.set_ylabel('$\\partial^2 V/\\partial\\sigma^2$', color='blue')
ax2.set_ylabel('$\\partial V/\\partial\\sigma|_{\\sigma=0}$', color='red')
ax.set_title('Potential curvature and tilt along Jensen')
ax.legend(loc='upper right', fontsize=8)
ax2.legend(loc='center right', fontsize=8)

plt.tight_layout()
plotpath = os.path.join(os.path.dirname(__file__), 's58_off_jensen_transit.png')
plt.savefig(plotpath, dpi=150, bbox_inches='tight')
print(f"Plot saved: {plotpath}")
plt.close()

print("\nDone.")
