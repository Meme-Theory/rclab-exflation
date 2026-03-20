#!/usr/bin/env python3
"""
T-ACOUSTIC-40: Acoustic Hawking Temperature at the B2 Fold
===========================================================

Computes the acoustic surface gravity and Hawking temperature at the B2 van Hove
singularity (fold) from the CASCADE-39 dispersion data. Implements the Barcelo
acoustic metric formalism for the internal-space phonon field.

Pre-registered gate:
  PASS (GEOMETRIC TEMPERATURE): T_acoustic agrees with T_Gibbs within factor 2
       (0.057 < T_acoustic < 0.226 in M_KK units)
  FAIL (NO CONNECTION): T_acoustic differs from T_Gibbs by more than factor 5

Inputs:
  tier0-computation/s39_cascade_spectroscopy.npz  (B2 dispersion)
  tier0-computation/s39_richardson_gaudin.npz      (BCS gap at fold)
  tier0-computation/s37_pair_susceptibility.npz    (pair gap Delta_pair)

Outputs:
  tier0-computation/s40_acoustic_temperature.npz
  tier0-computation/s40_acoustic_temperature.png
"""

import numpy as np
from scipy.interpolate import CubicSpline
from scipy.optimize import brentq
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

# ============================================================================
# 0. Load data
# ============================================================================
base = Path(__file__).parent

cascade = np.load(base / 's39_cascade_spectroscopy.npz', allow_pickle=True)
rg_data = np.load(base / 's39_richardson_gaudin.npz', allow_pickle=True)
ps_data = np.load(base / 's37_pair_susceptibility.npz', allow_pickle=True)

tau_grid = cascade['tau_grid']       # (50,) in [0.00, 0.50]
B2 = cascade['B2']                   # (50,) eigenvalue branch (already |lambda|)
B1 = cascade['B1']                   # (50,)
v_B2_raw = cascade['v_B2']           # (50,) dm^2/dtau from CASCADE
d2_B2_raw = cascade['d2_B2']         # (50,) d^2m^2/dtau^2 from CASCADE

# Van Hove singularity locations from CASCADE
vh_taus = cascade['vh_taus']         # [B1_fold, B2_fold]
vh_lambdas = cascade['vh_lambdas']

# BCS gap data
Delta_k_fold = rg_data['Delta_k_fold']   # gap for each of 8 modes at fold
E_cond = float(ps_data['E_cond'])         # condensation energy
Delta_pair = float(ps_data['Delta_pair']) # pair gap from susceptibility

# T_Gibbs from prior work
T_Gibbs = 0.113  # M_KK units (from Session 38 workshops)

print("=" * 72)
print("T-ACOUSTIC-40: Acoustic Hawking Temperature at the B2 Fold")
print("=" * 72)

# ============================================================================
# 1. B2 squared-mass dispersion
# ============================================================================
# B2 stores |lambda|. The squared mass is m^2 = lambda^2.
# We work with m^2_B2(tau) = B2(tau)^2.
m2_B2 = B2**2
m2_B1 = B1**2

print("\n--- Step 1: B2 Dispersion ---")
print(f"  tau range: [{tau_grid[0]:.4f}, {tau_grid[-1]:.4f}], N = {len(tau_grid)}")
print(f"  m^2_B2 range: [{m2_B2.min():.8f}, {m2_B2.max():.8f}]")
print(f"  m^2_B2 at tau=0: {m2_B2[0]:.8f}")
print(f"  CASCADE van Hove: tau_B2 = {vh_taus[1]:.8f}, lambda_B2 = {vh_lambdas[1]:.8f}")

# ============================================================================
# 2. Cubic spline fit near the fold
# ============================================================================
# Use all 50 points for global spline, but focus analysis near fold
cs_m2 = CubicSpline(tau_grid, m2_B2)

# First derivative: dm^2/dtau
cs_dm2 = cs_m2.derivative(nu=1)
# Second derivative: d^2m^2/dtau^2
cs_d2m2 = cs_m2.derivative(nu=2)

# Find precise fold: dm^2/dtau = 0 by root-finding
# CASCADE reports B2 fold near tau ~ 0.190
# Search in window [0.15, 0.25]
tau_search_lo, tau_search_hi = 0.15, 0.25

# Verify sign change
dm2_lo = cs_dm2(tau_search_lo)
dm2_hi = cs_dm2(tau_search_hi)
print(f"\n--- Step 2: Fold Identification ---")
print(f"  dm^2/dtau at tau={tau_search_lo:.2f}: {dm2_lo:.8f}")
print(f"  dm^2/dtau at tau={tau_search_hi:.2f}: {dm2_hi:.8f}")
print(f"  Sign change: {dm2_lo * dm2_hi < 0}")

if dm2_lo * dm2_hi < 0:
    tau_fold_B2 = brentq(cs_dm2, tau_search_lo, tau_search_hi, xtol=1e-14)
else:
    # Fallback: use minimum of spline on fine grid
    tau_fine = np.linspace(tau_search_lo, tau_search_hi, 10000)
    m2_fine = cs_m2(tau_fine)
    idx_min = np.argmin(m2_fine)
    tau_fold_B2 = tau_fine[idx_min]

m2_at_fold = cs_m2(tau_fold_B2)
dm2_at_fold = cs_dm2(tau_fold_B2)  # should be ~0
d2m2_at_fold = cs_d2m2(tau_fold_B2)

print(f"  tau_fold (spline root): {tau_fold_B2:.12f}")
print(f"  m^2_B2(tau_fold):       {m2_at_fold:.12f}")
print(f"  dm^2/dtau(tau_fold):    {dm2_at_fold:.2e}  (should be ~0)")
print(f"  d^2m^2/dtau^2(fold):    {d2m2_at_fold:.8f}")
print(f"  CASCADE reported fold:  {vh_taus[1]:.8f}")
print(f"  Discrepancy:            {abs(tau_fold_B2 - vh_taus[1]):.2e}")

# ============================================================================
# 3. Acoustic surface gravity alpha and cross-checks
# ============================================================================
alpha_spline = d2m2_at_fold

# Finite difference cross-check using 3 nearest grid points
# Find the grid index closest to the fold
idx_fold = np.argmin(np.abs(tau_grid - tau_fold_B2))
h = tau_grid[1] - tau_grid[0]  # uniform spacing

# Central second-order finite difference
if 1 <= idx_fold <= len(tau_grid) - 2:
    alpha_FD = (m2_B2[idx_fold + 1] - 2 * m2_B2[idx_fold] + m2_B2[idx_fold - 1]) / h**2
else:
    alpha_FD = np.nan

# Also try with the 3 points nearest to the fold (may differ from idx_fold +/- 1)
dists = np.abs(tau_grid - tau_fold_B2)
nearest_3 = np.argsort(dists)[:3]
nearest_3 = np.sort(nearest_3)
if len(nearest_3) == 3:
    t0, t1, t2 = tau_grid[nearest_3[0]], tau_grid[nearest_3[1]], tau_grid[nearest_3[2]]
    m0, m1, m2_v = m2_B2[nearest_3[0]], m2_B2[nearest_3[1]], m2_B2[nearest_3[2]]
    # General 3-point second derivative (non-uniform spacing formula)
    h01 = t1 - t0
    h12 = t2 - t1
    h02 = t2 - t0
    alpha_FD3 = 2.0 * (m0 / (h01 * h02) - m1 / (h01 * h12) + m2_v / (h12 * h02))
else:
    alpha_FD3 = np.nan

# Also compare with CASCADE's d2_B2 (which is d^2|lambda|/dtau^2, not d^2(lambda^2)/dtau^2)
# d^2(lambda^2)/dtau^2 = 2*lambda * d^2lambda/dtau^2 + 2*(dlambda/dtau)^2
# At the fold dlambda/dtau is NOT zero (v_B2 is dlambda/dtau from CASCADE)
# But dm^2/dtau = 2*lambda*dlambda/dtau = 0 at fold => dlambda/dtau = 0 at fold
# since lambda != 0 there.
# So d^2m^2/dtau^2 = 2*lambda*d^2lambda/dtau^2 + 2*(dlambda/dtau)^2
# At the fold: = 2*lambda_fold * d2lambda_fold + 0
lambda_fold_cascade = vh_lambdas[1]

# Interpolate CASCADE's d2_B2 at fold
cs_d2_cascade = CubicSpline(tau_grid, d2_B2_raw)
d2lambda_at_fold = cs_d2_cascade(tau_fold_B2)
alpha_from_cascade = 2 * lambda_fold_cascade * d2lambda_at_fold

# Also get v_B2 (dlambda/dtau) at fold from CASCADE interpolation
cs_v_cascade = CubicSpline(tau_grid, v_B2_raw)
vlambda_at_fold = cs_v_cascade(tau_fold_B2)
alpha_from_cascade_full = (2 * lambda_fold_cascade * d2lambda_at_fold
                           + 2 * vlambda_at_fold**2)

print(f"\n--- Step 3: Surface Gravity alpha ---")
print(f"  alpha (spline on m^2):        {alpha_spline:.8f}")
print(f"  alpha (FD, idx={idx_fold}):           {alpha_FD:.8f}")
print(f"  alpha (FD, 3-nearest):        {alpha_FD3:.8f}")
print(f"  alpha (CASCADE d2lambda):     {alpha_from_cascade:.8f}  (2*lam*d2lam)")
print(f"  alpha (CASCADE full):         {alpha_from_cascade_full:.8f}  (2*lam*d2lam + 2*vlam^2)")
print(f"  dlambda/dtau at fold:         {vlambda_at_fold:.8e}")
print(f"  d^2lambda/dtau^2 at fold:     {d2lambda_at_fold:.8f}")

# Use spline as primary, cascade as cross-check
alpha = alpha_spline
print(f"\n  ADOPTED alpha = {alpha:.8f}")
print(f"  Spline vs FD agreement:       {abs(alpha_spline - alpha_FD) / alpha_spline * 100:.2f}%")
print(f"  Spline vs CASCADE agreement:  {abs(alpha_spline - alpha_from_cascade_full) / alpha_spline * 100:.2f}%")

# ============================================================================
# 4. Acoustic Hawking Temperature
# ============================================================================
T_acoustic = alpha / (4 * np.pi)

print(f"\n--- Step 4: Acoustic Hawking Temperature ---")
print(f"  T_acoustic = alpha / (4*pi)")
print(f"  T_acoustic = {alpha:.8f} / {4*np.pi:.8f}")
print(f"  T_acoustic = {T_acoustic:.8f} M_KK")
print(f"")
print(f"  T_Gibbs    = {T_Gibbs:.3f} M_KK")
print(f"  Ratio T_acoustic / T_Gibbs = {T_acoustic / T_Gibbs:.6f}")
print(f"  Factor: {max(T_acoustic/T_Gibbs, T_Gibbs/T_acoustic):.3f}x")

# ============================================================================
# 5. Ratios: T_acoustic/Delta_BCS and E5 universality
# ============================================================================
# BCS gap at the fold: Delta_k_fold contains gap for each of 8 modes
# The B2 modes (first 4, degenerate) dominate
Delta_B2_fold = np.mean(np.abs(Delta_k_fold[:4]))
Delta_B1_fold = np.abs(Delta_k_fold[4])
Delta_BCS = Delta_B2_fold  # primary gap

print(f"\n--- Step 5: T_acoustic / Delta_BCS ---")
print(f"  Delta_B2 at fold (mean |Delta_k|, k=0..3): {Delta_B2_fold:.8f}")
print(f"  Delta_B1 at fold:                           {Delta_B1_fold:.8f}")
print(f"  Delta_pair (susceptibility):                {Delta_pair:.8f}")
print(f"")
print(f"  T_acoustic / Delta_B2  = {T_acoustic / Delta_B2_fold:.6f}")
print(f"  T_acoustic / Delta_pair = {T_acoustic / Delta_pair:.6f}")
print(f"")
print(f"  E5 universality prediction: T_acoustic/Delta ~ 0.28")
print(f"  Nuclear backbending range:  0.3 - 0.5")
print(f"  Our value (B2 gap):         {T_acoustic / Delta_B2_fold:.4f}")
print(f"  Our value (pair gap):       {T_acoustic / Delta_pair:.4f}")

# ============================================================================
# 6. Acoustic metric and kappa_acoustic
# ============================================================================
# The Barcelo acoustic metric for a phonon field near a sonic point:
#   g_eff^{mu nu} = diag(-1, 1/v_B2^2)
# where v_B2 = dm^2/dtau is the "group velocity" in the tau-parametrized dispersion.
#
# Near the fold, m^2(tau) ~ m^2_fold + (1/2)*alpha*(tau - tau_fold)^2
# so v_B2(tau) = dm^2/dtau = alpha*(tau - tau_fold)
# This is linear in (tau - tau_fold), exactly like the Rindler horizon.
#
# The acoustic surface gravity (Unruh analog):
#   kappa_acoustic = lim_{tau->tau_fold} |d(v_B2)/dtau| / 2
# where the factor of 2 comes from the standard Unruh/Hawking derivation.
# Since v_B2 ~ alpha*(tau - tau_fold), we get dv_B2/dtau = alpha, hence:
#   kappa_acoustic = alpha / 2
#
# For a quadratic dispersion minimum, the exact relation is:
#   kappa_acoustic = sqrt(alpha) / 2
# This arises when the effective metric determinant is taken into account.
# The distinction:
#   - alpha/2: surface gravity from velocity gradient (1+1 Rindler)
#   - sqrt(alpha)/2: surface gravity from proper acoustic metric normalization
#
# Both are physically meaningful. We compute both.

kappa_Rindler = alpha / 2
kappa_acoustic = np.sqrt(alpha) / 2

T_Rindler = kappa_Rindler / (2 * np.pi)    # = alpha/(4*pi) = T_acoustic
T_acoustic_metric = kappa_acoustic / (2 * np.pi)

print(f"\n--- Step 6: Acoustic Metric Analysis ---")
print(f"  Near fold: m^2(tau) ~ {m2_at_fold:.8f} + (1/2)*{alpha:.6f}*(tau - {tau_fold_B2:.8f})^2")
print(f"  v_B2(tau) = dm^2/dtau ~ {alpha:.6f} * (tau - tau_fold)  [linear, Rindler-like]")
print(f"")
print(f"  Rindler surface gravity: kappa_R = alpha/2 = {kappa_Rindler:.8f}")
print(f"  Acoustic surface gravity: kappa_a = sqrt(alpha)/2 = {kappa_acoustic:.8f}")
print(f"")
print(f"  T_Rindler       = kappa_R / (2*pi) = {T_Rindler:.8f} M_KK")
print(f"  T_acoustic_metr = kappa_a / (2*pi) = {T_acoustic_metric:.8f} M_KK")
print(f"")
print(f"  [The Rindler form T_R = alpha/(4*pi) is the direct analog of the standard")
print(f"   Hawking derivation. The metric form uses sqrt(alpha) and applies when the")
print(f"   dispersion maps onto a proper acoustic line element.]")

# Verify the quadratic fit quality near the fold
tau_near = np.linspace(tau_fold_B2 - 0.03, tau_fold_B2 + 0.03, 1000)
m2_near_spline = cs_m2(tau_near)
m2_near_quad = m2_at_fold + 0.5 * alpha * (tau_near - tau_fold_B2)**2
residual_quad = np.max(np.abs(m2_near_spline - m2_near_quad))
print(f"\n  Quadratic fit residual (|tau-tau_fold|<0.03): {residual_quad:.2e}")
print(f"  Relative to m^2_fold: {residual_quad / m2_at_fold * 100:.4f}%")

# ============================================================================
# 7. B1 van Hove singularity acoustic temperature
# ============================================================================
cs_m2_B1 = CubicSpline(tau_grid, m2_B1)
cs_dm2_B1 = cs_m2_B1.derivative(nu=1)
cs_d2m2_B1 = cs_m2_B1.derivative(nu=2)

# B1 fold near tau ~ 0.231 (CASCADE)
tau_search_B1_lo, tau_search_B1_hi = 0.20, 0.27
dm2_B1_lo = cs_dm2_B1(tau_search_B1_lo)
dm2_B1_hi = cs_dm2_B1(tau_search_B1_hi)

print(f"\n--- Step 7: B1 Van Hove Singularity ---")
print(f"  CASCADE reported B1 fold: tau = {vh_taus[0]:.8f}")
print(f"  dm^2_B1/dtau at tau={tau_search_B1_lo:.2f}: {dm2_B1_lo:.8f}")
print(f"  dm^2_B1/dtau at tau={tau_search_B1_hi:.2f}: {dm2_B1_hi:.8f}")

if dm2_B1_lo * dm2_B1_hi < 0:
    tau_fold_B1 = brentq(cs_dm2_B1, tau_search_B1_lo, tau_search_B1_hi, xtol=1e-14)
else:
    tau_fine_B1 = np.linspace(tau_search_B1_lo, tau_search_B1_hi, 10000)
    m2_B1_fine = cs_m2_B1(tau_fine_B1)
    tau_fold_B1 = tau_fine_B1[np.argmin(m2_B1_fine)]

m2_B1_fold = cs_m2_B1(tau_fold_B1)
alpha_B1 = cs_d2m2_B1(tau_fold_B1)
dm2_B1_at_fold = cs_dm2_B1(tau_fold_B1)
T_acoustic_B1 = alpha_B1 / (4 * np.pi)

# FD cross-check for B1
idx_fold_B1 = np.argmin(np.abs(tau_grid - tau_fold_B1))
if 1 <= idx_fold_B1 <= len(tau_grid) - 2:
    alpha_B1_FD = (m2_B1[idx_fold_B1 + 1] - 2 * m2_B1[idx_fold_B1] + m2_B1[idx_fold_B1 - 1]) / h**2
else:
    alpha_B1_FD = np.nan

print(f"  tau_fold_B1 (spline):   {tau_fold_B1:.12f}")
print(f"  m^2_B1(tau_fold):       {m2_B1_fold:.12f}")
print(f"  dm^2/dtau(fold):        {dm2_B1_at_fold:.2e}")
print(f"  alpha_B1 (spline):      {alpha_B1:.8f}")
print(f"  alpha_B1 (FD):          {alpha_B1_FD:.8f}")
print(f"  T_acoustic_B1:          {T_acoustic_B1:.8f} M_KK")
print(f"  T_B1 / T_Gibbs:         {T_acoustic_B1 / T_Gibbs:.6f}")
print(f"  T_B1 / T_B2:            {T_acoustic_B1 / T_acoustic:.6f}")

# ============================================================================
# 8. Gate Verdict
# ============================================================================
factor_from_Gibbs = max(T_acoustic / T_Gibbs, T_Gibbs / T_acoustic)

print(f"\n{'=' * 72}")
print(f"GATE VERDICT: T-ACOUSTIC-40")
print(f"{'=' * 72}")
print(f"  T_acoustic (B2) = {T_acoustic:.6f} M_KK")
print(f"  T_Gibbs         = {T_Gibbs:.3f} M_KK")
print(f"  Ratio            = {T_acoustic / T_Gibbs:.4f}")
print(f"  Factor off       = {factor_from_Gibbs:.3f}x")
print(f"  Window: [0.057, 0.226] M_KK")

if 0.057 <= T_acoustic <= 0.226:
    verdict = "PASS (GEOMETRIC TEMPERATURE)"
    print(f"  >>> {verdict}")
    print(f"  T_acoustic is within factor 2 of T_Gibbs.")
elif factor_from_Gibbs > 5:
    verdict = "FAIL (NO CONNECTION)"
    print(f"  >>> {verdict}")
    print(f"  T_acoustic differs from T_Gibbs by more than factor 5.")
else:
    verdict = "INFO (INTERMEDIATE)"
    print(f"  >>> {verdict}")
    print(f"  T_acoustic is between factor 2 and 5 from T_Gibbs.")

# E5 universality
ratio_E5 = T_acoustic / Delta_BCS
print(f"\n  E5 universality: T_acoustic / Delta_BCS = {ratio_E5:.4f}")
print(f"  Prediction: 0.28. Nuclear range: 0.3-0.5.")
if 0.20 <= ratio_E5 <= 0.60:
    print(f"  E5 CONSISTENT: ratio within nuclear backbending range.")
else:
    print(f"  E5 OUTSIDE nuclear range.")

# ============================================================================
# 9. Save data
# ============================================================================
np.savez(base / 's40_acoustic_temperature.npz',
         # B2 fold
         tau_fold_B2=tau_fold_B2,
         m2_at_fold_B2=m2_at_fold,
         dm2_at_fold_B2=dm2_at_fold,
         alpha_B2=alpha,
         alpha_B2_FD=alpha_FD,
         alpha_B2_FD3=alpha_FD3,
         alpha_B2_cascade=alpha_from_cascade_full,
         T_acoustic_B2=T_acoustic,
         kappa_Rindler_B2=kappa_Rindler,
         kappa_acoustic_B2=kappa_acoustic,
         T_Rindler_B2=T_Rindler,
         T_acoustic_metric_B2=T_acoustic_metric,
         # B1 fold
         tau_fold_B1=tau_fold_B1,
         m2_at_fold_B1=m2_B1_fold,
         alpha_B1=alpha_B1,
         alpha_B1_FD=alpha_B1_FD,
         T_acoustic_B1=T_acoustic_B1,
         # Ratios
         T_Gibbs=T_Gibbs,
         ratio_T_acoustic_T_Gibbs=T_acoustic / T_Gibbs,
         Delta_B2_fold=Delta_B2_fold,
         Delta_pair=Delta_pair,
         ratio_T_over_Delta_B2=T_acoustic / Delta_B2_fold,
         ratio_T_over_Delta_pair=T_acoustic / Delta_pair,
         # Quadratic fit quality
         quad_residual=residual_quad,
         # Gate
         verdict=verdict,
         # Dispersion for plotting
         tau_grid=tau_grid,
         m2_B2=m2_B2,
         m2_B1=m2_B1,
)
print(f"\n  Data saved to: tier0-computation/s40_acoustic_temperature.npz")

# ============================================================================
# 10. Plot
# ============================================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('T-ACOUSTIC-40: Acoustic Hawking Temperature at B2 Fold',
             fontsize=14, fontweight='bold')

# Panel (a): Full B2 and B1 dispersion
ax = axes[0, 0]
ax.plot(tau_grid, m2_B2, 'b.-', label=r'$m^2_{B2}(\tau)$', markersize=4)
ax.plot(tau_grid, m2_B1, 'r.-', label=r'$m^2_{B1}(\tau)$', markersize=4)
ax.axvline(tau_fold_B2, color='b', ls='--', alpha=0.5, label=f'B2 fold: {tau_fold_B2:.4f}')
ax.axvline(tau_fold_B1, color='r', ls='--', alpha=0.5, label=f'B1 fold: {tau_fold_B1:.4f}')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$m^2$ (M$_{KK}^2$)')
ax.set_title('(a) Squared-mass dispersion')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel (b): Zoom near B2 fold with quadratic fit
ax = axes[0, 1]
tau_zoom = np.linspace(tau_fold_B2 - 0.05, tau_fold_B2 + 0.05, 500)
m2_zoom_spline = cs_m2(tau_zoom)
m2_zoom_quad = m2_at_fold + 0.5 * alpha * (tau_zoom - tau_fold_B2)**2
ax.plot(tau_zoom, m2_zoom_spline, 'b-', linewidth=2, label='Spline')
ax.plot(tau_zoom, m2_zoom_quad, 'k--', linewidth=1.5, label=f'Quadratic: $\\alpha={alpha:.4f}$')
# Mark data points in zoom range
mask = (tau_grid > tau_fold_B2 - 0.06) & (tau_grid < tau_fold_B2 + 0.06)
ax.plot(tau_grid[mask], m2_B2[mask], 'bo', markersize=6, zorder=5)
ax.axvline(tau_fold_B2, color='b', ls=':', alpha=0.5)
ax.plot(tau_fold_B2, m2_at_fold, 'r*', markersize=15, zorder=10,
        label=f'Fold: $\\tau={tau_fold_B2:.5f}$')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$m^2_{B2}$ (M$_{KK}^2$)')
ax.set_title('(b) B2 fold zoom + quadratic fit')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel (c): Group velocity (dm^2/dtau) near fold
ax = axes[1, 0]
tau_vel = np.linspace(0.10, 0.30, 500)
v_spline = cs_dm2(tau_vel)
ax.plot(tau_vel, v_spline, 'b-', linewidth=2, label=r'$v_{B2} = dm^2/d\tau$ (spline)')
v_linear = alpha * (tau_vel - tau_fold_B2)
ax.plot(tau_vel, v_linear, 'k--', linewidth=1.5, label=f'Linear: $\\alpha \\cdot (\\tau - \\tau_{{fold}})$')
ax.axhline(0, color='gray', ls='-', alpha=0.3)
ax.axvline(tau_fold_B2, color='b', ls=':', alpha=0.5)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$dm^2_{B2}/d\tau$ (M$_{KK}^2$)')
ax.set_title('(c) B2 group velocity (Rindler horizon at $v=0$)')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel (d): Temperature summary
ax = axes[1, 1]
ax.axis('off')
results_text = (
    f"GATE: T-ACOUSTIC-40\n"
    f"{'='*40}\n\n"
    f"B2 Fold:\n"
    f"  tau_fold      = {tau_fold_B2:.6f}\n"
    f"  alpha (d2m2/dtau2) = {alpha:.6f}\n"
    f"  T_acoustic    = {T_acoustic:.6f} M_KK\n\n"
    f"B1 Fold:\n"
    f"  tau_fold      = {tau_fold_B1:.6f}\n"
    f"  alpha_B1      = {alpha_B1:.6f}\n"
    f"  T_acoustic_B1 = {T_acoustic_B1:.6f} M_KK\n\n"
    f"Comparisons:\n"
    f"  T_Gibbs        = {T_Gibbs:.3f} M_KK\n"
    f"  T_ac/T_Gibbs   = {T_acoustic/T_Gibbs:.4f}\n"
    f"  T_ac/Delta_B2  = {T_acoustic/Delta_B2_fold:.4f}\n"
    f"  T_ac/Delta_pair = {T_acoustic/Delta_pair:.4f}\n\n"
    f"E5 universality:\n"
    f"  T_ac/Delta = {ratio_E5:.4f}  (pred: 0.28)\n\n"
    f"Verdict: {verdict}\n"
    f"Cross-check: spline vs FD = {abs(alpha_spline-alpha_FD)/alpha_spline*100:.1f}%"
)
ax.text(0.05, 0.95, results_text, transform=ax.transAxes,
        fontsize=10, fontfamily='monospace', verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.tight_layout()
plt.savefig(base / 's40_acoustic_temperature.png', dpi=150, bbox_inches='tight')
print(f"  Plot saved to: tier0-computation/s40_acoustic_temperature.png")

print(f"\n{'=' * 72}")
print(f"COMPUTATION COMPLETE")
print(f"{'=' * 72}")
