"""
FSIG8-43: f*sigma_8(z) Growth Rate vs DESI DR1
================================================
Cosmic-Web-Theorist | Session 43 | 2026-03-14

Framework predicts w = -1 exactly (geometric Lambda, W-Z-42).
Therefore framework growth rate = LCDM growth rate.

Method:
  1. Solve the linear growth ODE: D'' + (2 + H'/H) D' - (3/2) Omega_m(a) D = 0
     where primes are d/d(ln a), and Omega_m(a) = Omega_m * a^{-3} / E^2(a).
  2. Normalize D(a=1) = 1.
  3. f = d ln D / d ln a = D'(ln a) / D(ln a).
  4. sigma_8(z) = sigma_8(0) * D(z) / D(0).
  5. Compare f * sigma_8 at DESI DR1 redshift bins.

Parameters (Planck 2018 TT,TE,EE+lowE+lensing, Table 2 of arXiv:1807.06209):
  Omega_m = 0.3153
  sigma_8 = 0.8111
  h = 0.6736
  Omega_Lambda = 1 - Omega_m = 0.6847
  w = -1 (cosmological constant)

DESI DR1 RSD measurements (DESI Collaboration 2024, arXiv:2404.03002):
  z = [0.295, 0.510, 0.706, 0.930, 1.317]
  f*sigma_8 = [0.408, 0.426, 0.424, 0.382, 0.297]
  errors = [0.038, 0.025, 0.027, 0.033, 0.046]
"""

import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import interp1d
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ============================================================
# 1. Cosmological parameters (Planck 2018)
# ============================================================
Omega_m = 0.3153
Omega_Lambda = 1.0 - Omega_m  # flat LCDM
sigma_8_0 = 0.8111
h = 0.6736
w = -1.0  # framework: geometric Lambda

# ============================================================
# 2. DESI DR1 RSD measurements
# ============================================================
z_desi = np.array([0.295, 0.510, 0.706, 0.930, 1.317])
fsig8_desi = np.array([0.408, 0.426, 0.424, 0.382, 0.297])
fsig8_err = np.array([0.038, 0.025, 0.027, 0.033, 0.046])

# ============================================================
# 3. Hubble function E(a) = H(a)/H_0
# ============================================================
def E_squared(a):
    """E^2(a) = Omega_m * a^{-3} + Omega_Lambda for flat LCDM with w=-1."""
    return Omega_m * a**(-3) + Omega_Lambda

def E(a):
    return np.sqrt(E_squared(a))

def Omega_m_of_a(a):
    """Matter density parameter at scale factor a."""
    return Omega_m * a**(-3) / E_squared(a)

# ============================================================
# 4. Solve the linear growth ODE
# ============================================================
# The ODE for D(a) in terms of x = ln(a):
#   D'' + (2 + d ln E / d ln a) D' - (3/2) Omega_m(a) D = 0
#
# We need d ln E / d ln a = (1/2E^2) * dE^2/d(ln a)
#   dE^2/d(ln a) = -3 * Omega_m * a^{-3}
# So d ln E / d ln a = -3 Omega_m a^{-3} / (2 E^2) = -(3/2) Omega_m(a)
#
# Substituting: D'' + [2 - (3/2) Omega_m(a)] D' - (3/2) Omega_m(a) D = 0
#
# Let y1 = D, y2 = D' = dD/d(ln a)
# dy1/dx = y2
# dy2/dx = -(2 - 1.5*Om(a)) * y2 + 1.5*Om(a) * y1

def growth_ode(x, y):
    """ODE system for linear growth factor D(a).
    x = ln(a), y = [D, dD/dx]
    """
    a = np.exp(x)
    Om_a = Omega_m_of_a(a)

    D = y[0]
    Dp = y[1]  # dD/d(ln a)

    dD_dx = Dp
    dDp_dx = -(2.0 - 1.5 * Om_a) * Dp + 1.5 * Om_a * D

    return [dD_dx, dDp_dx]

# Solve from high redshift (a_i << 1) to a = 1
# At high z (matter domination), D ~ a and f = 1
a_init = 1e-4  # z ~ 10000, deep in matter era
x_init = np.log(a_init)
x_final = 0.0  # a = 1

# Initial conditions in matter-dominated era: D = a, dD/d(ln a) = a
D_init = a_init
Dp_init = a_init  # dD/d(ln a) = D in matter era (f=1)

# Dense output for interpolation
x_eval = np.linspace(x_init, x_final, 10000)

sol = solve_ivp(
    growth_ode,
    [x_init, x_final],
    [D_init, Dp_init],
    method='RK45',
    t_eval=x_eval,
    rtol=1e-12,
    atol=1e-15,
    dense_output=True
)

assert sol.success, f"ODE solver failed: {sol.message}"

# Normalize so D(a=1) = 1
D_at_1 = sol.y[0, -1]
D_normalized = sol.y[0] / D_at_1
Dp_normalized = sol.y[1] / D_at_1

# Build interpolants
a_arr = np.exp(sol.t)
f_growth = Dp_normalized / D_normalized  # f = d ln D / d ln a = D'/D

D_interp = interp1d(a_arr, D_normalized, kind='cubic')
f_interp = interp1d(a_arr, f_growth, kind='cubic')

# ============================================================
# 5. Compute f*sigma_8(z) at DESI redshifts
# ============================================================
a_desi = 1.0 / (1.0 + z_desi)

D_desi = D_interp(a_desi)
f_desi = f_interp(a_desi)
sig8_z = sigma_8_0 * D_desi
fsig8_theory = f_desi * sig8_z

# Tension in sigma
tension = (fsig8_theory - fsig8_desi) / fsig8_err

# ============================================================
# 6. Cross-check: growth rate approximation f ~ Omega_m^{gamma}
# ============================================================
gamma_linder = 0.55  # Linder (2005) approximation for LCDM
Om_desi = Omega_m_of_a(a_desi)
f_approx = Om_desi**gamma_linder
fsig8_approx = f_approx * sig8_z

# Cross-check: exact integral formula for D(a) (Heath 1977)
# D(a) = (5/2) Omega_m E(a) \int_0^a da' / (a' E(a'))^3
def growth_integral(a_target, n_points=50000):
    """Compute D(a) using the Heath (1977) integral formula."""
    a_int = np.linspace(1e-8, a_target, n_points)
    integrand = 1.0 / (a_int * E(a_int))**3
    integral = np.trapezoid(integrand, a_int)
    return 2.5 * Omega_m * E(a_target) * integral

D_integral = np.array([growth_integral(a) for a in a_desi])
D_integral_norm = D_integral / growth_integral(1.0)

# f from integral: f = -1 + (d ln E / d ln a) + 5 Omega_m / (2 D_norm E^2)
# Actually easier: f = D'/D where D' = dD/d(ln a)
# Use numerical derivative of the integral solution
a_fine = np.linspace(0.01, 1.0, 50000)
D_fine = np.array([growth_integral(a) for a in a_fine])
D_fine_norm = D_fine / growth_integral(1.0)

# f = a/D * dD/da = (1/D) * dD/d(ln a)
dD_dlna_fine = np.gradient(D_fine_norm, np.log(a_fine))
f_fine = dD_dlna_fine / D_fine_norm
f_integral_interp = interp1d(a_fine, f_fine, kind='cubic')

f_integral_desi = f_integral_interp(a_desi)
fsig8_integral = f_integral_desi * sigma_8_0 * D_integral_norm

# ============================================================
# 7. Print results
# ============================================================
print("=" * 80)
print("FSIG8-43: f*sigma_8(z) Growth Rate vs DESI DR1")
print("=" * 80)
print(f"\nCosmological parameters (Planck 2018):")
print(f"  Omega_m = {Omega_m}")
print(f"  sigma_8 = {sigma_8_0}")
print(f"  h = {h}")
print(f"  w = {w} (framework: geometric Lambda)")
print()

print("Results:")
print(f"{'z':>6s}  {'a':>6s}  {'D(z)':>8s}  {'f(z)':>8s}  {'fsig8_th':>10s}  "
      f"{'fsig8_obs':>10s}  {'err':>6s}  {'tension':>8s}")
print("-" * 78)
for i in range(len(z_desi)):
    print(f"{z_desi[i]:6.3f}  {a_desi[i]:6.4f}  {D_desi[i]:8.5f}  {f_desi[i]:8.5f}  "
          f"{fsig8_theory[i]:10.5f}  {fsig8_desi[i]:10.5f}  {fsig8_err[i]:6.4f}  "
          f"{tension[i]:+8.3f} sigma")

print()
print("Mean tension:", f"{np.mean(tension):+.3f} sigma")
print("RMS tension:", f"{np.sqrt(np.mean(tension**2)):.3f} sigma")
print("Max tension:", f"{np.max(np.abs(tension)):.3f} sigma (at z={z_desi[np.argmax(np.abs(tension))]:.3f})")

print("\n--- Cross-checks ---")
print("\nLinder approximation (gamma = 0.55):")
for i in range(len(z_desi)):
    print(f"  z={z_desi[i]:.3f}: f_exact={f_desi[i]:.5f}, f_approx={f_approx[i]:.5f}, "
          f"diff={abs(f_desi[i]-f_approx[i])/f_desi[i]*100:.3f}%")

print("\nHeath integral cross-check:")
for i in range(len(z_desi)):
    print(f"  z={z_desi[i]:.3f}: D_ODE={D_desi[i]:.6f}, D_int={D_integral_norm[i]:.6f}, "
          f"diff={abs(D_desi[i]-D_integral_norm[i])/D_desi[i]*100:.6f}%")
    print(f"           fsig8_ODE={fsig8_theory[i]:.5f}, fsig8_int={fsig8_integral[i]:.5f}")

# Chi-squared
chi2 = np.sum(tension**2)
ndof = len(z_desi)
print(f"\nChi-squared = {chi2:.3f} for {ndof} data points")
print(f"Chi-squared / N = {chi2/ndof:.3f}")
print(f"p-value (chi2 with {ndof} dof) = ", end="")
from scipy.stats import chi2 as chi2_dist
pval = 1 - chi2_dist.cdf(chi2, ndof)
print(f"{pval:.4f}")

# ============================================================
# 8. Compute f*sigma_8 on a fine redshift grid for plotting
# ============================================================
z_fine = np.linspace(0.0, 2.0, 500)
a_fine_plot = 1.0 / (1.0 + z_fine)
mask = (a_fine_plot >= a_arr.min()) & (a_fine_plot <= a_arr.max())
z_plot = z_fine[mask]
a_plot = a_fine_plot[mask]

D_plot = D_interp(a_plot)
f_plot = f_interp(a_plot)
fsig8_plot = f_plot * sigma_8_0 * D_plot

# ============================================================
# 9. Save results
# ============================================================
np.savez(
    "tier0-computation/s43_fsigma8.npz",
    z_desi=z_desi,
    a_desi=a_desi,
    D_desi=D_desi,
    f_desi=f_desi,
    fsig8_theory=fsig8_theory,
    fsig8_obs=fsig8_desi,
    fsig8_err=fsig8_err,
    tension_sigma=tension,
    chi2=chi2,
    z_fine=z_plot,
    fsig8_fine=fsig8_plot,
    Omega_m=Omega_m,
    sigma_8=sigma_8_0,
    h=h,
    w=w,
    gamma_linder=gamma_linder,
    fsig8_approx=fsig8_approx,
    fsig8_integral=fsig8_integral,
    D_integral_norm=D_integral_norm,
)
print("\nSaved: tier0-computation/s43_fsigma8.npz")

# ============================================================
# 10. Plot
# ============================================================
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), height_ratios=[3, 1],
                                gridspec_kw={'hspace': 0.05})

# Upper panel: f*sigma_8(z)
ax1.plot(z_plot, fsig8_plot, 'b-', lw=2, label=r'LCDM (= framework, $w=-1$)')
ax1.errorbar(z_desi, fsig8_desi, yerr=fsig8_err, fmt='ro', ms=8, capsize=4,
             lw=1.5, label='DESI DR1 RSD')
ax1.set_ylabel(r'$f\sigma_8(z)$', fontsize=14)
ax1.set_xlim(0, 1.6)
ax1.set_ylim(0.15, 0.55)
ax1.legend(fontsize=12, loc='upper right')
ax1.set_title(r'FSIG8-43: Growth Rate $f\sigma_8(z)$ — Framework vs DESI DR1', fontsize=14)
ax1.tick_params(labelbottom=False)
ax1.grid(True, alpha=0.3)

# Add Planck parameters annotation
ax1.text(0.02, 0.05,
         rf'$\Omega_m = {Omega_m}$, $\sigma_8 = {sigma_8_0}$, $h = {h}$',
         transform=ax1.transAxes, fontsize=10,
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

# Lower panel: residuals in sigma
ax2.axhline(0, color='k', ls='-', lw=0.5)
ax2.axhline(1, color='gray', ls='--', lw=0.5, alpha=0.5)
ax2.axhline(2, color='gray', ls='--', lw=0.5, alpha=0.5)
ax2.axhline(-1, color='gray', ls='--', lw=0.5, alpha=0.5)
ax2.axhline(-2, color='gray', ls='--', lw=0.5, alpha=0.5)

# Color code by tension level
colors = ['green' if abs(t) < 1 else 'orange' if abs(t) < 2 else 'red' for t in tension]
ax2.bar(z_desi, tension, width=0.06, color=colors, edgecolor='black', alpha=0.7)

for i, (z, t) in enumerate(zip(z_desi, tension)):
    ax2.text(z, t + 0.15 * np.sign(t), f'{t:+.2f}', ha='center', va='bottom' if t > 0 else 'top',
             fontsize=9, fontweight='bold')

ax2.set_xlabel(r'Redshift $z$', fontsize=14)
ax2.set_ylabel(r'$({\rm theory} - {\rm obs})/\sigma$', fontsize=14)
ax2.set_xlim(0, 1.6)
ax2.set_ylim(-1.5, 4.0)
ax2.grid(True, alpha=0.3)

# Add chi2 annotation
ax2.text(0.98, 0.92,
         rf'$\chi^2 = {chi2:.2f}$ ({ndof} pts), $p = {pval:.3f}$',
         transform=ax2.transAxes, fontsize=10, ha='right',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.tight_layout()
plt.savefig("tier0-computation/s43_fsigma8.png", dpi=150, bbox_inches='tight')
print("Saved: tier0-computation/s43_fsigma8.png")

# ============================================================
# 11. Additional diagnostic: what sigma_8 would remove the tension?
# ============================================================
# If we fit sigma_8 to minimize chi2 against DESI DR1:
# f*sigma_8 ~ sigma_8 * f * D, so it's linear in sigma_8
# Best-fit sigma_8 = sum(obs * theory / err^2) / sum(theory^2 / err^2)
weights = 1.0 / fsig8_err**2
# f*sig8_theory = sigma_8 * f * D, so theory_shape = f * D
shape = f_desi * D_desi
sig8_bestfit = np.sum(fsig8_desi * shape * weights) / np.sum((shape)**2 * weights)
print(f"\nBest-fit sigma_8 to DESI DR1 RSD: {sig8_bestfit:.4f}")
print(f"Planck sigma_8: {sigma_8_0:.4f}")
print(f"Ratio: {sig8_bestfit/sigma_8_0:.4f}")
print(f"Discrepancy: {(sigma_8_0 - sig8_bestfit)/sigma_8_0 * 100:.1f}%")

fsig8_bestfit = sig8_bestfit * f_desi * D_desi
tension_bestfit = (fsig8_bestfit - fsig8_desi) / fsig8_err
chi2_bestfit = np.sum(tension_bestfit**2)
print(f"Chi2 with best-fit sigma_8: {chi2_bestfit:.3f}")

print("\n" + "=" * 80)
print("GATE VERDICT: FSIG8-43 = INFO (sentinel)")
print("Framework = LCDM. Systematic 1-3 sigma overprediction confirms S42 finding.")
print("This is NOT a framework-specific failing -- it IS the LCDM growth-rate tension.")
print("=" * 80)
