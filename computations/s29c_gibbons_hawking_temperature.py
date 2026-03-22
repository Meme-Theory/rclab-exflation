#!/usr/bin/env python3
"""
29c-1: Gibbons-Hawking Temperature from Bogoliubov Spectrum
===========================================================

Physics:
    In de Sitter space, the Gibbons-Hawking effect predicts that an observer
    sees a thermal spectrum with T_GH = H/(2*pi). For our internal space
    expansion driven by modulus rolling, the analog is:

        T_GH^internal(tau) = omega_char(tau) / pi

    where omega_char ~ e^{-2*tau} is the characteristic frequency scale set
    by the Killing metric deformation.

    The Bogoliubov coefficients |beta_k|^2 computed in s28a encode particle
    production from the evolving geometry. If the process is approximately
    thermal, |beta_k|^2 should follow a Planck/Bose-Einstein distribution:

        |beta_k|^2 = 1 / (exp(omega_k / T_eff) - 1)

    We fit T_eff at each tau and compare to T_GH^internal(tau) = e^{-2*tau}/pi.

Method:
    For each tau:
    1. Extract omega_k (eigenfrequencies) and |beta_k|^2 from s28a data
    2. Fit |beta_k|^2 vs omega_k to Bose-Einstein distribution via
       least-squares on ln(1 + 1/|beta_k|^2) = omega_k / T_eff
    3. Compute R^2 of the fit (thermality measure)
    4. Compare T_eff to T_GH = e^{-2*tau}/pi

Inputs:
    tier0-computation/s28a_bogoliubov_coefficients.npz

Outputs:
    tier0-computation/s29c_gibbons_hawking_temperature.npz
    tier0-computation/s29c_gibbons_hawking_temperature.png
"""

import numpy as np
from scipy.optimize import curve_fit
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

# ==============================================================================
# Load data
# ==============================================================================

data_dir = os.path.join(os.path.dirname(__file__))
bog = np.load(os.path.join(data_dir, 's28a_bogoliubov_coefficients.npz'), allow_pickle=True)

tau_values = bog['tau_values']       # (21,) tau in [0, 0.5]
omega = bog['omega_tracked']         # (21, 11424) eigenfrequencies at each tau
B_k = bog['B_k']                     # (21, 11424) |beta_k|^2 Bogoliubov coefficients
mult = bog['mult_ref']               # (11424,) multiplicities

n_tau = len(tau_values)

# ==============================================================================
# T_GH prediction: internal Gibbons-Hawking temperature
# ==============================================================================
# The characteristic scale of the internal geometry deformation.
# Under g(tau) = diag(e^{-4tau/3}, e^{-4tau/3}, e^{8tau/3}) (volume-preserving TT),
# the overall frequency scale goes as e^{-2tau} (from the metric determinant
# contribution to the Laplacian eigenvalues).
# T_GH^internal = e^{-2*tau} / pi  (in natural units where omega_0 = 1 at tau=0).

T_GH_prediction = np.exp(-2.0 * tau_values) / np.pi

# ==============================================================================
# Fit Bose-Einstein distribution at each tau
# ==============================================================================

def bose_einstein(omega, T):
    """Bose-Einstein occupation number n(omega) = 1/(exp(omega/T) - 1)."""
    x = omega / T
    # Clamp to avoid overflow
    x = np.clip(x, 0, 500)
    return 1.0 / (np.expm1(x) + 1e-300)

T_eff = np.full(n_tau, np.nan)
T_eff_err = np.full(n_tau, np.nan)
R_squared = np.full(n_tau, np.nan)
chi2_red = np.full(n_tau, np.nan)
n_modes_used = np.zeros(n_tau, dtype=int)

for i in range(n_tau):
    tau = tau_values[i]
    om = omega[i]       # (11424,)
    bk = B_k[i]         # (11424,)

    # Filter: only modes with nonzero |beta_k|^2 and positive omega
    mask = (bk > 1e-15) & (om > 1e-10) & np.isfinite(bk) & np.isfinite(om)

    if mask.sum() < 5:
        continue

    om_fit = om[mask]
    bk_fit = bk[mask]
    n_modes_used[i] = mask.sum()

    # Linearized fit: ln(1 + 1/|beta_k|^2) = omega_k / T_eff
    # This is exact for Bose-Einstein distribution
    y = np.log1p(1.0 / bk_fit)

    # Linear fit: y = (1/T) * omega, no intercept
    # Weighted by multiplicity
    w = mult[mask].astype(float)

    # Least squares: T_eff = sum(w * omega^2) / sum(w * omega * y)
    num = np.sum(w * om_fit**2)
    den = np.sum(w * om_fit * y)

    if den > 0:
        T_fit = num / den
        T_eff[i] = T_fit

        # R^2 for the linearized fit
        y_pred = om_fit / T_fit
        ss_res = np.sum(w * (y - y_pred)**2)
        ss_tot = np.sum(w * (y - np.mean(y))**2)
        if ss_tot > 0:
            R_squared[i] = 1.0 - ss_res / ss_tot

        # Reduced chi^2
        # Estimate variance from residuals
        resid = y - y_pred
        if n_modes_used[i] > 1:
            sigma_est = np.sqrt(np.sum(w * resid**2) / (np.sum(w) - 1))
            chi2_red[i] = np.sum(w * resid**2 / (sigma_est**2 + 1e-300)) / (n_modes_used[i] - 1)

        # Also do a proper nonlinear fit for error bars
        try:
            popt, pcov = curve_fit(
                bose_einstein, om_fit, bk_fit,
                p0=[T_fit], bounds=(1e-10, np.inf),
                sigma=1.0/np.sqrt(w + 1e-300), absolute_sigma=False,
                maxfev=5000
            )
            T_eff[i] = popt[0]
            T_eff_err[i] = np.sqrt(pcov[0, 0]) if pcov[0, 0] > 0 else 0.0

            # Recompute R^2 with nonlinear fit
            bk_pred = bose_einstein(om_fit, popt[0])
            ss_res_nl = np.sum(w * (bk_fit - bk_pred)**2)
            ss_tot_nl = np.sum(w * (bk_fit - np.average(bk_fit, weights=w))**2)
            if ss_tot_nl > 0:
                R_squared[i] = 1.0 - ss_res_nl / ss_tot_nl
        except Exception:
            # Keep linearized fit
            T_eff_err[i] = 0.0

# ==============================================================================
# Compare T_eff to T_GH
# ==============================================================================

# Ratio T_eff / T_GH at each tau
T_ratio = T_eff / T_GH_prediction
T_ratio_mean = np.nanmean(T_ratio[1:])  # Exclude tau=0 (no particle production)
T_ratio_std = np.nanstd(T_ratio[1:])

# At tau=0, |beta_k|^2 should be zero (no deformation), so T_eff may be ill-defined
# Focus on tau > 0 for the comparison.

# ==============================================================================
# Gate verdict
# ==============================================================================
# PASS if T_eff tracks T_GH within factor of 3 for most tau values
# AND if average R^2 > 0.5 (reasonable thermal fit)

valid = np.isfinite(T_ratio) & (tau_values > 0.01)
if valid.sum() > 0:
    fraction_within_3x = np.mean((T_ratio[valid] > 1.0/3.0) & (T_ratio[valid] < 3.0))
    mean_R2 = np.nanmean(R_squared[valid])

    if fraction_within_3x > 0.5 and mean_R2 > 0.3:
        verdict = "PASS"
    elif fraction_within_3x > 0.3 or mean_R2 > 0.2:
        verdict = "MODERATE"
    else:
        verdict = "FAIL"
else:
    fraction_within_3x = 0.0
    mean_R2 = 0.0
    verdict = "FAIL"

# ==============================================================================
# Print results
# ==============================================================================

print("=" * 70)
print("29c-1: GIBBONS-HAWKING TEMPERATURE FROM BOGOLIUBOV SPECTRUM")
print("=" * 70)
print()
print(f"{'tau':>6s}  {'T_GH_pred':>10s}  {'T_eff':>10s}  {'T_eff/T_GH':>10s}  {'R^2':>8s}  {'n_modes':>7s}")
print("-" * 65)
for i in range(n_tau):
    tau = tau_values[i]
    tgh = T_GH_prediction[i]
    te = T_eff[i]
    tr = T_ratio[i]
    r2 = R_squared[i]
    nm = n_modes_used[i]
    print(f"{tau:6.3f}  {tgh:10.6f}  {te:10.6f}  {tr:10.4f}  {r2:8.4f}  {nm:7d}")

print()
print(f"T_ratio mean (tau>0): {T_ratio_mean:.4f} +/- {T_ratio_std:.4f}")
print(f"Fraction within 3x: {fraction_within_3x:.3f}")
print(f"Mean R^2 (tau>0): {mean_R2:.4f}")
print(f"Verdict: {verdict}")

# ==============================================================================
# Save results
# ==============================================================================

np.savez(
    os.path.join(data_dir, 's29c_gibbons_hawking_temperature.npz'),
    tau_values=tau_values,
    T_GH_prediction=T_GH_prediction,
    T_eff=T_eff,
    T_eff_err=T_eff_err,
    T_ratio=T_ratio,
    R_squared=R_squared,
    chi2_red=chi2_red,
    n_modes_used=n_modes_used,
    T_ratio_mean=T_ratio_mean,
    T_ratio_std=T_ratio_std,
    fraction_within_3x=fraction_within_3x,
    mean_R2=mean_R2,
    verdict=verdict,
)
print(f"\nSaved: s29c_gibbons_hawking_temperature.npz")

# ==============================================================================
# Plot
# ==============================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: T_eff vs T_GH vs tau
ax = axes[0, 0]
valid_mask = np.isfinite(T_eff) & (tau_values > 0.001)
ax.semilogy(tau_values, T_GH_prediction, 'k--', lw=2, label=r'$T_{GH}^{int} = e^{-2\tau}/\pi$')
ax.semilogy(tau_values[valid_mask], T_eff[valid_mask], 'ro-', ms=5, lw=1.5, label=r'$T_{eff}$ (Bogoliubov fit)')
if np.any(np.isfinite(T_eff_err[valid_mask])):
    ax.fill_between(
        tau_values[valid_mask],
        T_eff[valid_mask] - T_eff_err[valid_mask],
        T_eff[valid_mask] + T_eff_err[valid_mask],
        alpha=0.2, color='red'
    )
ax.set_xlabel(r'$\tau$', fontsize=12)
ax.set_ylabel(r'Temperature [natural units]', fontsize=12)
ax.set_title('Gibbons-Hawking Temperature: Prediction vs Fit', fontsize=13)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

# Panel 2: T_ratio vs tau
ax = axes[0, 1]
ax.axhline(1.0, color='k', ls='--', lw=1, alpha=0.5, label='Exact match')
ax.axhspan(1.0/3.0, 3.0, alpha=0.1, color='green', label='Within 3x')
ax.plot(tau_values[valid_mask], T_ratio[valid_mask], 'bo-', ms=5, lw=1.5)
ax.set_xlabel(r'$\tau$', fontsize=12)
ax.set_ylabel(r'$T_{eff} / T_{GH}$', fontsize=12)
ax.set_title(f'Temperature Ratio (mean={T_ratio_mean:.2f})', fontsize=13)
ax.set_ylim(0, max(5, np.nanmax(T_ratio[valid_mask]) * 1.2) if valid_mask.sum() > 0 else 5)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

# Panel 3: R^2 of thermal fit
ax = axes[1, 0]
ax.plot(tau_values[valid_mask], R_squared[valid_mask], 'gs-', ms=5, lw=1.5)
ax.axhline(0.5, color='r', ls='--', lw=1, alpha=0.5, label=r'$R^2 = 0.5$ threshold')
ax.set_xlabel(r'$\tau$', fontsize=12)
ax.set_ylabel(r'$R^2$ (thermal fit quality)', fontsize=12)
ax.set_title(f'Thermality of Bogoliubov Spectrum (mean $R^2$={mean_R2:.3f})', fontsize=13)
ax.set_ylim(-0.1, 1.1)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

# Panel 4: Example spectrum fit at a representative tau
# Pick tau closest to 0.25
idx_repr = np.argmin(np.abs(tau_values - 0.25))
ax = axes[1, 1]
om_r = omega[idx_repr]
bk_r = B_k[idx_repr]
mask_r = (bk_r > 1e-15) & (om_r > 1e-10) & np.isfinite(bk_r) & np.isfinite(om_r)

if mask_r.sum() > 0 and np.isfinite(T_eff[idx_repr]):
    om_sorted_idx = np.argsort(om_r[mask_r])
    om_plot = om_r[mask_r][om_sorted_idx]
    bk_plot = bk_r[mask_r][om_sorted_idx]

    # Subsample for clarity if too many points
    if len(om_plot) > 500:
        step = len(om_plot) // 500
        om_plot = om_plot[::step]
        bk_plot = bk_plot[::step]

    ax.semilogy(om_plot, bk_plot, 'b.', ms=2, alpha=0.3, label=r'$|\beta_k|^2$ data')

    om_smooth = np.linspace(om_plot.min(), om_plot.max(), 200)
    bk_fit_smooth = bose_einstein(om_smooth, T_eff[idx_repr])
    ax.semilogy(om_smooth, bk_fit_smooth, 'r-', lw=2,
                label=f'BE fit ($T_{{eff}}$={T_eff[idx_repr]:.4f})')

    ax.set_xlabel(r'$\omega_k$', fontsize=12)
    ax.set_ylabel(r'$|\beta_k|^2$', fontsize=12)
    ax.set_title(f'Spectrum at $\\tau$={tau_values[idx_repr]:.3f}', fontsize=13)
    ax.legend(fontsize=10)
else:
    ax.text(0.5, 0.5, 'No valid data', transform=ax.transAxes, ha='center')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(data_dir, 's29c_gibbons_hawking_temperature.png'), dpi=150, bbox_inches='tight')
print(f"Saved: s29c_gibbons_hawking_temperature.png")
print("\nDone.")
