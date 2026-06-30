#!/usr/bin/env python3
"""
29c-1: Gibbons-Hawking Temperature from Bogoliubov Spectrum (ACOUSTIC ANALOG)
============================================================================

Substrate framing:
    The "horizon" here is an ACOUSTIC analog (supersonic fold transit), NOT a
    geometric event horizon. The Gibbons-Hawking temperature T_GH in this
    internal-space context is derived from the surface-gravity analog of the
    Killing metric deformation under Jensen evolution, not from curvature
    in an embedding spacetime. Particle creation is fiber-eigenvalue
    reorganization, not QFT-in-curved-spacetime in a geometric container.

Physics:
    In de Sitter space, T_GH = H/(2*pi). For our internal space under
    volume-preserving TT deformation g(tau) = diag(e^{-4tau/3}, e^{-4tau/3},
    e^{8tau/3}), the characteristic frequency scale goes as e^{-2*tau}.
    Bogoliubov fit to Bose-Einstein yields T_eff at each tau; compare to
    T_GH^internal = e^{-2*tau}/pi.

    Substitution chain (direction of T_GH^internal):
        Step 1: T_GH^internal(tau) := omega_char(tau)/pi    [definition]
        Step 2: omega_char(tau) = exp(-2*tau)               [metric-det eigenvalue scaling]
        Step 3: T_GH^internal(tau) = exp(-2*tau)/pi
        Step 4: dT_GH/dtau = -2*exp(-2*tau)/pi              [differentiate]
        Step 5: exp(-2*tau) > 0 for all real tau            [exponential positivity]
        Conclusion: T_GH^internal DECREASES monotonically in tau.
"""

# --- Canonical constants (MANDATORY) ---
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import PI, tau_fold

import numpy as np
from scipy.optimize import curve_fit
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ==============================================================================
# Load data
# ==============================================================================

data_dir = os.path.dirname(os.path.abspath(__file__))  # (local)
bog = np.load(os.path.join(data_dir, 's28a_bogoliubov_coefficients.npz'), allow_pickle=True)  # (local)

tau_values = bog['tau_values']       # (local) (21,) tau in [0, 0.5]
omega = bog['omega_tracked']         # (local) (21, 11424) eigenfrequencies at each tau
B_k = bog['B_k']                     # (local) (21, 11424) |beta_k|^2 Bogoliubov coefficients
mult = bog['mult_ref']               # (local) (11424,) multiplicities

n_tau = len(tau_values)              # (local)

# ==============================================================================
# T_GH prediction: internal Gibbons-Hawking temperature (acoustic analog)
# ==============================================================================
# Under g(tau) = diag(e^{-4tau/3}, e^{-4tau/3}, e^{8tau/3}) (volume-preserving TT),
# the overall frequency scale goes as e^{-2tau} (metric-determinant contribution
# to Laplacian eigenvalues).
# T_GH^internal = exp(-2*tau) / PI  [natural units, omega_0 = 1 at tau=0].

T_GH_prediction = np.exp(-2.0 * tau_values) / PI  # (local)

# ==============================================================================
# Fit Bose-Einstein distribution at each tau
# ==============================================================================

def bose_einstein(omega, T):
    """Bose-Einstein occupation n(omega) = 1/(exp(omega/T) - 1)."""
    x = omega / T                    # (local)
    x = np.clip(x, 0, 500)           # (local)
    return 1.0 / (np.expm1(x) + 1e-300)

T_eff = np.full(n_tau, np.nan)                 # (local)
T_eff_err = np.full(n_tau, np.nan)             # (local)
R_squared = np.full(n_tau, np.nan)             # (local)
chi2_red = np.full(n_tau, np.nan)              # (local)
n_modes_used = np.zeros(n_tau, dtype=int)      # (local)

for i in range(n_tau):
    tau = tau_values[i]              # (local)
    om = omega[i]                    # (local) (11424,)
    bk = B_k[i]                      # (local) (11424,)

    # Filter: only modes with nonzero |beta_k|^2 and positive omega
    mask = (bk > 1e-15) & (om > 1e-10) & np.isfinite(bk) & np.isfinite(om)  # (local)

    if mask.sum() < 5:
        continue

    om_fit = om[mask]                # (local)
    bk_fit = bk[mask]                # (local)
    n_modes_used[i] = mask.sum()

    # Linearized fit: ln(1 + 1/|beta_k|^2) = omega_k / T_eff
    y = np.log1p(1.0 / bk_fit)       # (local)

    # Weighted linear fit: y = (1/T) * omega, no intercept
    w = mult[mask].astype(float)     # (local)

    num = np.sum(w * om_fit**2)      # (local)
    den = np.sum(w * om_fit * y)     # (local)

    if den > 0:
        T_fit = num / den                             # (local)
        T_eff[i] = T_fit

        y_pred = om_fit / T_fit                       # (local)
        ss_res = np.sum(w * (y - y_pred)**2)          # (local)
        ss_tot = np.sum(w * (y - np.mean(y))**2)      # (local)
        if ss_tot > 0:
            R_squared[i] = 1.0 - ss_res / ss_tot

        resid = y - y_pred                            # (local)
        if n_modes_used[i] > 1:
            sigma_est = np.sqrt(np.sum(w * resid**2) / (np.sum(w) - 1))   # (local)
            chi2_red[i] = np.sum(w * resid**2 / (sigma_est**2 + 1e-300)) / (n_modes_used[i] - 1)

        try:
            popt, pcov = curve_fit(
                bose_einstein, om_fit, bk_fit,
                p0=[T_fit], bounds=(1e-10, np.inf),
                sigma=1.0/np.sqrt(w + 1e-300), absolute_sigma=False,
                maxfev=5000
            )
            T_eff[i] = popt[0]
            T_eff_err[i] = np.sqrt(pcov[0, 0]) if pcov[0, 0] > 0 else 0.0

            bk_pred = bose_einstein(om_fit, popt[0])      # (local)
            ss_res_nl = np.sum(w * (bk_fit - bk_pred)**2) # (local)
            ss_tot_nl = np.sum(w * (bk_fit - np.average(bk_fit, weights=w))**2)  # (local)
            if ss_tot_nl > 0:
                R_squared[i] = 1.0 - ss_res_nl / ss_tot_nl
        except Exception:
            T_eff_err[i] = 0.0

# ==============================================================================
# Compare T_eff to T_GH
# ==============================================================================

T_ratio = T_eff / T_GH_prediction                           # (local)
T_ratio_mean = np.nanmean(T_ratio[1:])                      # (local)
T_ratio_std = np.nanstd(T_ratio[1:])                        # (local)

# ==============================================================================
# Gate verdict
# ==============================================================================
# PASS if T_eff tracks T_GH within factor of 3 for >50% of tau values
# AND if mean R^2 > 0.3 (acoustic-analog thermal fit quality).

valid = np.isfinite(T_ratio) & (tau_values > 0.01)          # (local)
if valid.sum() > 0:
    fraction_within_3x = np.mean((T_ratio[valid] > 1.0/3.0) & (T_ratio[valid] < 3.0))  # (local)
    mean_R2 = np.nanmean(R_squared[valid])                  # (local)

    if fraction_within_3x > 0.5 and mean_R2 > 0.3:
        verdict = "PASS"
    elif fraction_within_3x > 0.3 or mean_R2 > 0.2:
        verdict = "MODERATE"
    else:
        verdict = "FAIL"
else:
    fraction_within_3x = 0.0                                # (local)
    mean_R2 = 0.0                                           # (local)
    verdict = "FAIL"                                        # (local)

# ==============================================================================
# Print results
# ==============================================================================

print("=" * 70)
print("29c-1: GIBBONS-HAWKING TEMPERATURE FROM BOGOLIUBOV SPECTRUM (ACOUSTIC)")
print("=" * 70)
print()
print(f"tau_fold (canonical) = {tau_fold}")
print()
print(f"{'tau':>6s}  {'T_GH_pred':>10s}  {'T_eff':>10s}  {'T_eff/T_GH':>10s}  {'R^2':>8s}  {'n_modes':>7s}")
print("-" * 65)
for i in range(n_tau):
    tau = tau_values[i]              # (local)
    tgh = T_GH_prediction[i]         # (local)
    te = T_eff[i]                    # (local)
    tr = T_ratio[i]                  # (local)
    r2 = R_squared[i]                # (local)
    nm = n_modes_used[i]             # (local)
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
    tau_fold=tau_fold,
)
print(f"\nSaved: s29c_gibbons_hawking_temperature.npz")

# ==============================================================================
# Plot
# ==============================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))                  # (local)

ax = axes[0, 0]                                                    # (local)
valid_mask = np.isfinite(T_eff) & (tau_values > 0.001)             # (local)
ax.semilogy(tau_values, T_GH_prediction, 'k--', lw=2, label=r'$T_{GH}^{int} = e^{-2\tau}/\pi$')
ax.semilogy(tau_values[valid_mask], T_eff[valid_mask], 'ro-', ms=5, lw=1.5, label=r'$T_{eff}$ (Bogoliubov fit)')
if np.any(np.isfinite(T_eff_err[valid_mask])):
    ax.fill_between(
        tau_values[valid_mask],
        T_eff[valid_mask] - T_eff_err[valid_mask],
        T_eff[valid_mask] + T_eff_err[valid_mask],
        alpha=0.2, color='red'  # (local)
    )
ax.axvline(tau_fold, color='purple', ls=':', lw=1.5, label=f'tau_fold={tau_fold}')
ax.set_xlabel(r'$\tau$', fontsize=12)
ax.set_ylabel(r'Temperature [natural units]', fontsize=12)
ax.set_title('GH Temperature (acoustic analog): Prediction vs Fit', fontsize=13)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

ax = axes[0, 1]
ax.axhline(1.0, color='k', ls='--', lw=1, alpha=0.5, label='Exact match')
ax.axhspan(1.0/3.0, 3.0, alpha=0.1, color='green', label='Within 3x')
ax.plot(tau_values[valid_mask], T_ratio[valid_mask], 'bo-', ms=5, lw=1.5)
ax.axvline(tau_fold, color='purple', ls=':', lw=1.5)
ax.set_xlabel(r'$\tau$', fontsize=12)
ax.set_ylabel(r'$T_{eff} / T_{GH}$', fontsize=12)
ax.set_title(f'Temperature Ratio (mean={T_ratio_mean:.2f})', fontsize=13)
ax.set_ylim(0, max(5, np.nanmax(T_ratio[valid_mask]) * 1.2) if valid_mask.sum() > 0 else 5)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

ax = axes[1, 0]
ax.plot(tau_values[valid_mask], R_squared[valid_mask], 'gs-', ms=5, lw=1.5)
ax.axhline(0.5, color='r', ls='--', lw=1, alpha=0.5, label=r'$R^2 = 0.5$ threshold')
ax.axvline(tau_fold, color='purple', ls=':', lw=1.5)
ax.set_xlabel(r'$\tau$', fontsize=12)
ax.set_ylabel(r'$R^2$ (thermal fit quality)', fontsize=12)
ax.set_title(f'Thermality of Bogoliubov Spectrum (mean $R^2$={mean_R2:.3f})', fontsize=13)
ax.set_ylim(-0.1, 1.1)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

idx_repr = np.argmin(np.abs(tau_values - 0.25))    # (local)
ax = axes[1, 1]
om_r = omega[idx_repr]                              # (local)
bk_r = B_k[idx_repr]                                # (local)
mask_r = (bk_r > 1e-15) & (om_r > 1e-10) & np.isfinite(bk_r) & np.isfinite(om_r)  # (local)

if mask_r.sum() > 0 and np.isfinite(T_eff[idx_repr]):
    om_sorted_idx = np.argsort(om_r[mask_r])         # (local)
    om_plot = om_r[mask_r][om_sorted_idx]            # (local)
    bk_plot = bk_r[mask_r][om_sorted_idx]            # (local)

    if len(om_plot) > 500:
        step = len(om_plot) // 500                   # (local)
        om_plot = om_plot[::step]
        bk_plot = bk_plot[::step]

    ax.semilogy(om_plot, bk_plot, 'b.', ms=2, alpha=0.3, label=r'$|\beta_k|^2$ data')

    om_smooth = np.linspace(om_plot.min(), om_plot.max(), 200)    # (local)
    bk_fit_smooth = bose_einstein(om_smooth, T_eff[idx_repr])      # (local)
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
