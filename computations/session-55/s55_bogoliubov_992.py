"""
s55_bogoliubov_992.py — Continuum 992-mode Bogoliubov spectrum non-thermality
Gate: BOGOLIUBOV-992-55

Physics:
  The transit from tau=0 to tau=0.19 (van Hove fold) is Parker-type cosmological
  particle creation — NOT Hawking radiation. No horizon => no thermal Planck spectrum.

  Bogoliubov transformation: when the Hamiltonian changes from H(tau_i) to H(tau_f),
  the vacuum at tau_i contains particles as viewed from tau_f.

  Sudden approximation:
    tanh(2*theta_k) = (omega_f - omega_i) / (omega_f + omega_i)
    |beta_k|^2 = sinh^2(theta_k) = particle number in mode k
    |alpha_k|^2 = cosh^2(theta_k), |alpha|^2 - |beta|^2 = 1 (bosonic normalization)

  Thermal test: Hawking/Planck: |beta|^2 = 1/(exp(omega/T) - 1)
  Parker spectrum: mode-dependent, non-thermal, depends on quench profile.

Author: Hawking-Theorist agent
Session: S55
"""

import numpy as np
from scipy.optimize import curve_fit
from scipy.stats import spearmanr, kendalltau
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys
sys.path.insert(0, 'computations')

# ============================================================
# 1. Load continuum spectrum at tau=0 and tau=0.19
# ============================================================
d44 = np.load('computations/session-44/s44_dos_tau.npz', allow_pickle=True)

omega_i = d44['tau0.00_all_omega']   # (992,) eigenvalues at tau=0
omega_f = d44['tau0.19_all_omega']   # (992,) eigenvalues at tau=0.19
dim2_i = d44['tau0.00_all_dim2']     # (992,) degeneracy dim^2
dim2_f = d44['tau0.19_all_dim2']     # (992,) degeneracy dim^2

N_modes = len(omega_i)
N_phys = dim2_i.sum()
print(f"N_modes = {N_modes}, N_physical = {N_phys:.0f}")

# Sort both arrays by initial frequency for consistent pairing
sort_i = np.argsort(omega_i)
omega_i_sorted = omega_i[sort_i]
omega_f_sorted = omega_f[sort_i]
dim2_sorted = dim2_i[sort_i]

# ============================================================
# 2. Bogoliubov coefficients — sudden approximation
# ============================================================
# tanh(2*theta) = (omega_f - omega_i)/(omega_f + omega_i)
delta_omega = omega_f_sorted - omega_i_sorted
sum_omega = omega_f_sorted + omega_i_sorted

# Fractional frequency change
eta_k = delta_omega / sum_omega  # = tanh(2*theta_k)

# Bogoliubov angle
theta_k = 0.5 * np.arctanh(np.clip(eta_k, -0.9999, 0.9999))

# Particle number per mode
beta_sq = np.sinh(theta_k)**2    # |beta_k|^2
alpha_sq = np.cosh(theta_k)**2   # |alpha_k|^2

# Verify bosonic normalization
norm_check = alpha_sq - beta_sq
print(f"\nBosonic normalization |alpha|^2 - |beta|^2 = 1:")
print(f"  max deviation: {np.max(np.abs(norm_check - 1.0)):.2e}")

# Total particle number (weighted by degeneracy)
N_total_weighted = np.sum(beta_sq * dim2_sorted)
N_total_unweighted = np.sum(beta_sq)
print(f"\nTotal particle number:")
print(f"  Unweighted (992 modes): {N_total_unweighted:.4f}")
print(f"  Weighted (101,984 physical): {N_total_weighted:.1f}")
print(f"  Mean |beta|^2: {np.mean(beta_sq):.6f}")
print(f"  Max |beta|^2:  {np.max(beta_sq):.6f}")
print(f"  Min |beta|^2:  {np.min(beta_sq):.6f}")
print(f"  Std |beta|^2:  {np.std(beta_sq):.6f}")

# ============================================================
# 3. Thermal (Planck) fit
# ============================================================
# Hawking/Planck: n(omega) = 1/(exp(omega/T) - 1)
# We fit |beta_k|^2 vs omega_f_sorted

def planck_dist(omega, T):
    """Bose-Einstein/Planck distribution."""
    x = omega / T
    # Avoid overflow
    x = np.clip(x, 0, 500)
    return 1.0 / (np.expm1(x))

def planck_with_mu(omega, T, mu):
    """Planck with chemical potential."""
    x = (omega - mu) / T
    x = np.clip(x, 0, 500)
    return 1.0 / (np.expm1(x))

# Use omega_f as the frequency for the "out" modes
omega_out = omega_f_sorted

# Filter to modes with nonzero particle production
mask = beta_sq > 1e-15
omega_fit = omega_out[mask]
beta_sq_fit = beta_sq[mask]

print(f"\n{'='*60}")
print("THERMAL FIT ANALYSIS")
print(f"{'='*60}")
print(f"Modes with |beta|^2 > 1e-15: {mask.sum()} / {N_modes}")

# Fit 1: Simple Planck (1 parameter: T)
try:
    popt_planck, pcov_planck = curve_fit(
        planck_dist, omega_fit, beta_sq_fit,
        p0=[0.5], bounds=(0.001, 100), maxfev=10000
    )
    T_fit = popt_planck[0]
    beta_sq_planck = planck_dist(omega_fit, T_fit)
    residuals_planck = beta_sq_fit - beta_sq_planck
    SS_res_planck = np.sum(residuals_planck**2)
    SS_tot = np.sum((beta_sq_fit - np.mean(beta_sq_fit))**2)
    R2_planck = 1 - SS_res_planck / SS_tot if SS_tot > 0 else float('nan')
    rms_planck = np.sqrt(np.mean(residuals_planck**2))
    print(f"\nPlanck fit (1 param):")
    print(f"  T_fit = {T_fit:.6f} M_KK")
    print(f"  R^2 = {R2_planck:.6f}")
    print(f"  RMS residual = {rms_planck:.6e}")
    print(f"  Max |residual| = {np.max(np.abs(residuals_planck)):.6e}")
    PLANCK_FIT_SUCCESS = True
except Exception as e:
    print(f"\nPlanck fit FAILED: {e}")
    T_fit = np.nan
    R2_planck = np.nan
    rms_planck = np.nan
    PLANCK_FIT_SUCCESS = False

# Fit 2: Planck with chemical potential (2 params: T, mu)
try:
    popt_mu, pcov_mu = curve_fit(
        planck_with_mu, omega_fit, beta_sq_fit,
        p0=[0.5, 0.5], bounds=([0.001, -5], [100, 5]), maxfev=10000
    )
    T_fit_mu = popt_mu[0]
    mu_fit = popt_mu[1]
    beta_sq_mu = planck_with_mu(omega_fit, T_fit_mu, mu_fit)
    residuals_mu = beta_sq_fit - beta_sq_mu
    SS_res_mu = np.sum(residuals_mu**2)
    R2_mu = 1 - SS_res_mu / SS_tot if SS_tot > 0 else float('nan')
    rms_mu = np.sqrt(np.mean(residuals_mu**2))
    print(f"\nPlanck+mu fit (2 params):")
    print(f"  T_fit = {T_fit_mu:.6f} M_KK")
    print(f"  mu_fit = {mu_fit:.6f} M_KK")
    print(f"  R^2 = {R2_mu:.6f}")
    print(f"  RMS residual = {rms_mu:.6e}")
    MU_FIT_SUCCESS = True
except Exception as e:
    print(f"\nPlanck+mu fit FAILED: {e}")
    T_fit_mu = np.nan
    mu_fit = np.nan
    R2_mu = np.nan
    rms_mu = np.nan
    MU_FIT_SUCCESS = False

# ============================================================
# 4. Spectral index n(omega) = d ln|beta|^2 / d ln omega
# ============================================================
# For thermal: n -> -1 at high omega (Wien tail: |beta|^2 ~ exp(-omega/T) ~ omega^{-1} * ...)
# Actually for Planck: at high omega, |beta|^2 ~ exp(-omega/T), so
# d ln|beta|^2 / d ln omega = omega * d(ln|beta|^2)/d(omega) = -omega/T (frequency-dependent, not -1)
# For Parker: depends on the quench profile

# Compute spectral index numerically
# Sort by omega_out for index computation
sort_out = np.argsort(omega_out)
omega_sorted_out = omega_out[sort_out]
beta_sq_sorted_out = beta_sq[sort_out]

# Only use modes with nonzero particle production
mask_out = beta_sq_sorted_out > 1e-15
omega_si_raw = omega_sorted_out[mask_out]
beta_si_raw = beta_sq_sorted_out[mask_out]

# Average over degenerate frequencies to avoid 0/0 in log derivative
if len(omega_si_raw) > 10:
    # Group by unique omega and average |beta|^2
    uq_omega_si, inv_si = np.unique(omega_si_raw, return_inverse=True)
    beta_si_avg = np.zeros(len(uq_omega_si))
    for j in range(len(uq_omega_si)):
        beta_si_avg[j] = np.mean(beta_si_raw[inv_si == j])

    omega_si = uq_omega_si
    beta_si = beta_si_avg

    log_omega = np.log(omega_si)
    log_beta = np.log(np.maximum(beta_si, 1e-20))

    # Numerical derivative using finite differences (on unique values => no 0/0)
    n_spectral = np.gradient(log_beta, log_omega)

    # Global power-law index (linear regression in log-log)
    coeffs = np.polyfit(log_omega, log_beta, 1)
    n_global = coeffs[0]

    # Filter NaN/inf from spectral index for statistics
    n_finite = n_spectral[np.isfinite(n_spectral)]

    print(f"\n{'='*60}")
    print("SPECTRAL INDEX ANALYSIS")
    print(f"{'='*60}")
    print(f"Unique frequencies for index: {len(omega_si)}")
    print(f"Global power-law index (linear fit in log-log): n = {n_global:.4f}")
    if len(n_finite) > 0:
        print(f"Local spectral index statistics:")
        print(f"  Mean n(omega): {np.mean(n_finite):.4f}")
        print(f"  Std n(omega):  {np.std(n_finite):.4f}")
        print(f"  Min n(omega):  {np.min(n_finite):.4f}")
        print(f"  Max n(omega):  {np.max(n_finite):.4f}")
        n_variation = np.std(n_finite) / np.abs(np.mean(n_finite)) if np.abs(np.mean(n_finite)) > 1e-10 else float('inf')
    else:
        n_variation = float('inf')

    print(f"  Coefficient of variation: {n_variation:.4f}")
    print(f"  (CV >> 1 => strongly non-thermal)")
else:
    n_spectral = np.array([])
    omega_si = np.array([])
    n_global = np.nan
    n_variation = np.nan
    print("\nInsufficient modes for spectral index computation")

# ============================================================
# 5. Correlation analysis: is |beta|^2 monotone in omega?
# ============================================================
# For Planck: |beta|^2 is monotonically DECREASING in omega
# For Parker: depends on geometry

rho_spearman, p_spearman = spearmanr(omega_out[mask], beta_sq[mask])
tau_kendall, p_kendall = kendalltau(omega_out[mask], beta_sq[mask])

print(f"\n{'='*60}")
print("MONOTONICITY / CORRELATION ANALYSIS")
print(f"{'='*60}")
print(f"Spearman rank correlation (omega vs |beta|^2):")
print(f"  rho = {rho_spearman:.6f}, p = {p_spearman:.2e}")
print(f"Kendall tau correlation:")
print(f"  tau = {tau_kendall:.6f}, p = {p_kendall:.2e}")
print(f"\nFor thermal: rho should be ~ -1 (|beta|^2 decreasing with omega)")
print(f"Measured: rho = {rho_spearman:.6f}")

# Anti-thermal test: count modes where higher omega => higher |beta|^2
if mask.sum() > 1:
    n_anti = 0
    n_thermal = 0
    omega_m = omega_out[mask]
    beta_m = beta_sq[mask]
    sort_idx = np.argsort(omega_m)
    omega_m_s = omega_m[sort_idx]
    beta_m_s = beta_m[sort_idx]
    for i in range(len(omega_m_s)-1):
        if omega_m_s[i+1] > omega_m_s[i]:
            if beta_m_s[i+1] > beta_m_s[i]:
                n_anti += 1
            else:
                n_thermal += 1
    total_pairs = n_anti + n_thermal
    anti_frac = n_anti / total_pairs if total_pairs > 0 else 0
    print(f"\nAnti-thermal pairs (higher omega => higher |beta|^2): {n_anti}/{total_pairs} ({anti_frac:.1%})")

# ============================================================
# 6. Per-sector analysis
# ============================================================
print(f"\n{'='*60}")
print("PER-SECTOR BOGOLIUBOV ANALYSIS")
print(f"{'='*60}")

# At tau=0, the eigenvalues cluster at 16 discrete frequencies (highly degenerate)
# At tau=0.19, degeneracies are partially lifted (120 unique values)
# The sectors are labeled by SU(3) representations (p,q)

# Get unique initial frequencies and their mode counts
uq_i, inv_i, cnt_i = np.unique(omega_i_sorted, return_inverse=True, return_counts=True)
print(f"\nDistinct initial frequencies: {len(uq_i)}")

# Group modes by initial frequency band
# At tau=0, there are 16 exact eigenvalues corresponding to sectors
sector_boundaries = [0.83, 0.85, 0.87, 1.00, 1.05, 1.12, 1.15, 1.20, 1.28, 1.35,
                     1.40, 1.45, 1.50, 1.55, 1.60, 1.65, 1.75, 1.85]

# Simpler: group by initial omega bands
uq_omega_i = np.unique(np.round(omega_i_sorted, 4))
print(f"Distinct initial frequencies (rounded 4dp): {len(uq_omega_i)}")

sector_labels = ['B1:(0,0)', 'B2:(1,0)/(0,1)', 'B3:(1,1)',
                 'B4:(2,0)/(0,2)', 'B5:(3,0)/(0,3)', 'B6:(2,1)']

# Get rough sector boundaries from the distinct eigenvalue bands at tau=0
# At tau=0 exact: 0.833, 0.866, 1.014, 1.118, 1.167, 1.302, 1.323, 1.424, 1.443, 1.481, 1.500, 1.590, 1.607, 1.641, 1.740, 1.803
boundaries = [0, 0.85, 0.95, 1.07, 1.14, 1.25, 1.31, 1.37, 1.435, 1.46, 1.49, 1.55, 1.595, 1.625, 1.70, 1.77, 2.1]
band_names = ['B1-low', 'B2-singlet', 'B2-high', 'B4-low', 'B1/B2-mid', 'B5-low', 'B3-low',
              'B6-low', 'B3-mid', 'B4-mid', 'B5-mid', 'B6-mid', 'B5/B4-hi', 'B6-hi', 'B3-hi', 'B5-top']

# Actually, let's just report per-distinct-frequency statistics
uq_vals = np.unique(np.round(omega_i_sorted, 3))
print(f"\nPer-band Bogoliubov statistics:")
print(f"{'omega_i':>10} {'N_modes':>8} {'<|beta|^2>':>12} {'max|beta|^2':>12} {'<Delta_omega>':>14}")

band_data = []
for val in uq_vals:
    mask_band = np.abs(omega_i_sorted - val) < 0.005
    n_band = mask_band.sum()
    beta_band = beta_sq[mask_band]
    dw_band = delta_omega[mask_band]
    band_data.append({
        'omega_i': val,
        'n_modes': n_band,
        'mean_beta2': np.mean(beta_band),
        'max_beta2': np.max(beta_band),
        'mean_dw': np.mean(dw_band),
    })
    if n_band >= 5:  # only print bands with enough modes
        print(f"{val:10.4f} {n_band:8d} {np.mean(beta_band):12.6f} {np.max(beta_band):12.6f} {np.mean(dw_band):14.6f}")

# ============================================================
# 7. Compare with s52 lattice 8-mode Bogoliubov
# ============================================================
print(f"\n{'='*60}")
print("COMPARISON WITH S52 LATTICE (8-mode)")
print(f"{'='*60}")

d52 = np.load('computations/session-52/s52_bogoliubov_amp.npz', allow_pickle=True)
u_k_52 = d52['u_k']       # (8,) Bogoliubov u
v_k_52 = d52['v_k']       # (8,) Bogoliubov v
beta_sq_52 = v_k_52**2    # |beta|^2 = |v_k|^2
E_8 = d52['E_8']           # (8,) single-particle energies
labels_52 = d52['branch_labels']

print(f"S52 lattice (8 modes):")
print(f"  {'Label':>8} {'E_k':>10} {'|beta|^2':>12}")
for i in range(8):
    print(f"  {labels_52[i]:>8} {E_8[i]:10.6f} {beta_sq_52[i]:12.6f}")

print(f"\n  Total particles (8-mode): {np.sum(beta_sq_52):.4f}")
print(f"  Mean |beta|^2 (8-mode):   {np.mean(beta_sq_52):.6f}")

# The 8 modes of s52 correspond to the N_pair=1 sector (B2x4 + B1 + B3x3)
# Their energies at tau=0.20 should match approximately
# E_8 = [0.845, 0.845, 0.845, 0.845, 0.819, 0.978, 0.978, 0.978]
# These are the B2 (singlet) and B3 modes

# Find corresponding modes in the 992 spectrum
# B2 modes at tau=0: omega ~ 0.866 (singlet rep (0,0) has dim^2=1, 3 of them from spinor)
# At tau=0.19: these should be near the B2 mass 0.845

# Match s52 modes to continuum
print(f"\nMatching s52 modes to continuum:")
for i in range(8):
    E = E_8[i]  # (local)
    # Find closest continuum mode at tau=0.19
    # s52 is at tau=0.20, continuum at tau=0.19 - slight mismatch expected
    idx_close = np.argmin(np.abs(omega_f_sorted - E))
    print(f"  {labels_52[i]:>8}: s52 E={E:.6f}, closest continuum omega_f={omega_f_sorted[idx_close]:.6f}, "
          f"continuum |beta|^2={beta_sq[idx_close]:.6f}, s52 |beta|^2={beta_sq_52[i]:.6f}")

# ============================================================
# 8. Kolmogorov-Smirnov test against thermal
# ============================================================
print(f"\n{'='*60}")
print("KOLMOGOROV-SMIRNOV TEST vs THERMAL")
print(f"{'='*60}")

if PLANCK_FIT_SUCCESS and mask.sum() > 5:
    from scipy.stats import ks_2samp
    # Generate thermal sample with fitted T
    beta_sq_thermal_pred = planck_dist(omega_fit, T_fit)
    # KS test: are the two distributions drawn from the same parent?
    ks_stat, ks_p = ks_2samp(beta_sq_fit, beta_sq_thermal_pred)
    print(f"KS statistic: {ks_stat:.6f}")
    print(f"KS p-value:   {ks_p:.2e}")
    print(f"(p < 0.05 => reject thermal hypothesis)")
else:
    ks_stat = np.nan
    ks_p = np.nan
    print("Skipped (Planck fit failed or too few modes)")

# ============================================================
# 9. Chi-squared test against thermal
# ============================================================
print(f"\n{'='*60}")
print("CHI-SQUARED GOODNESS OF FIT")
print(f"{'='*60}")

if PLANCK_FIT_SUCCESS:
    # Bin the data
    n_bins = min(30, mask.sum() // 5)
    if n_bins >= 3:
        omega_bins = np.linspace(omega_fit.min(), omega_fit.max(), n_bins + 1)
        observed_counts = np.zeros(n_bins)
        expected_counts = np.zeros(n_bins)
        for b in range(n_bins):
            in_bin = (omega_fit >= omega_bins[b]) & (omega_fit < omega_bins[b+1])
            if b == n_bins - 1:
                in_bin = (omega_fit >= omega_bins[b]) & (omega_fit <= omega_bins[b+1])
            observed_counts[b] = np.sum(beta_sq_fit[in_bin])
            expected_counts[b] = np.sum(beta_sq_thermal_pred[in_bin]) if PLANCK_FIT_SUCCESS else 0

        # Chi-squared
        mask_nonzero = expected_counts > 0
        if mask_nonzero.sum() > 1:
            chi2 = np.sum((observed_counts[mask_nonzero] - expected_counts[mask_nonzero])**2 /
                          expected_counts[mask_nonzero])
            dof = mask_nonzero.sum() - 1  # -1 for T parameter
            chi2_red = chi2 / dof if dof > 0 else float('inf')
            print(f"chi^2 = {chi2:.4f}, dof = {dof}, chi^2/dof = {chi2_red:.4f}")
            print(f"(chi^2/dof >> 1 => non-thermal)")
    else:
        chi2_red = np.nan
        print("Too few bins for chi-squared test")
else:
    chi2_red = np.nan

# ============================================================
# 10. Classification verdict
# ============================================================
print(f"\n{'='*60}")
print("CLASSIFICATION VERDICT")
print(f"{'='*60}")

# Criteria for non-thermality:
# 1. R^2 of Planck fit < 0.9
# 2. Spectral index varies strongly (CV > 0.5)
# 3. Spearman rho > -0.9 (not monotonically decreasing)
# 4. Anti-thermal fraction > 20%

criteria = []
if PLANCK_FIT_SUCCESS:
    is_poor_fit = R2_planck < 0.9
    criteria.append(('Planck R^2 < 0.9', is_poor_fit, f'R^2 = {R2_planck:.4f}'))

if not np.isnan(n_variation):
    is_variable_index = n_variation > 0.5
    criteria.append(('Spectral index CV > 0.5', is_variable_index, f'CV = {n_variation:.4f}'))

criteria.append(('Spearman rho > -0.9', rho_spearman > -0.9, f'rho = {rho_spearman:.4f}'))
criteria.append(('Anti-thermal frac > 20%', anti_frac > 0.2, f'frac = {anti_frac:.1%}'))

n_nonthermal = sum(1 for _, v, _ in criteria if v)
n_total_criteria = len(criteria)

print(f"\nNon-thermality criteria ({n_nonthermal}/{n_total_criteria} met):")
for name, met, detail in criteria:
    status = "PASS (non-thermal)" if met else "FAIL (thermal-like)"
    print(f"  [{status}] {name}: {detail}")

if n_nonthermal >= 2:
    verdict = "NON-THERMAL (Parker-type)"
    print(f"\nVERDICT: {verdict}")
    print("The Bogoliubov spectrum is non-thermal. No Hawking radiation.")
    print("Consistent with Parker-type particle creation (no horizon).")
else:
    verdict = "THERMAL-LIKE"
    print(f"\nVERDICT: {verdict}")
    print("WARNING: spectrum appears thermal-like despite absence of horizon.")

# ============================================================
# 11. Save data
# ============================================================
save_dict = {
    'omega_i': omega_i_sorted,
    'omega_f': omega_f_sorted,
    'dim2': dim2_sorted,
    'beta_sq': beta_sq,
    'alpha_sq': alpha_sq,
    'theta_k': theta_k,
    'delta_omega': delta_omega,
    'eta_k': eta_k,
    'N_modes': N_modes,
    'N_total_unweighted': N_total_unweighted,
    'N_total_weighted': N_total_weighted,
    'T_fit_planck': T_fit if PLANCK_FIT_SUCCESS else np.nan,
    'R2_planck': R2_planck if PLANCK_FIT_SUCCESS else np.nan,
    'rms_planck': rms_planck if PLANCK_FIT_SUCCESS else np.nan,
    'T_fit_mu': T_fit_mu if MU_FIT_SUCCESS else np.nan,
    'mu_fit': mu_fit if MU_FIT_SUCCESS else np.nan,
    'R2_mu': R2_mu if MU_FIT_SUCCESS else np.nan,
    'n_global': n_global,
    'n_variation': n_variation,
    'rho_spearman': rho_spearman,
    'tau_kendall': tau_kendall,
    'anti_thermal_frac': anti_frac,
    'ks_stat': ks_stat if not np.isnan(ks_stat) else np.nan,
    'ks_pvalue': ks_p if not np.isnan(ks_p) else np.nan,
    'verdict': verdict,
    'gate': 'BOGOLIUBOV-992-55',
}

np.savez('computations/session-55/s55_bogoliubov_992.npz', **save_dict)
print(f"\nData saved to computations/session-55/s55_bogoliubov_992.npz")

# ============================================================
# 12. Plot
# ============================================================
fig, axes = plt.subplots(2, 3, figsize=(18, 11))
fig.suptitle(f'BOGOLIUBOV-992-55: Continuum Bogoliubov Spectrum\n'
             f'992 modes, tau: 0 -> 0.19 (fold). Verdict: {verdict}',
             fontsize=14, fontweight='bold')

# Panel 1: |beta|^2 vs omega_f
ax = axes[0, 0]
sc = ax.scatter(omega_f_sorted, beta_sq, c=omega_i_sorted, cmap='viridis',
                s=3, alpha=0.6, edgecolors='none')
if PLANCK_FIT_SUCCESS:
    omega_plot = np.linspace(omega_fit.min(), omega_fit.max(), 200)
    ax.plot(omega_plot, planck_dist(omega_plot, T_fit), 'r-', lw=2,
            label=f'Planck T={T_fit:.4f}, R²={R2_planck:.3f}')
    ax.legend(fontsize=8)
plt.colorbar(sc, ax=ax, label='omega_i')
ax.set_xlabel('omega_f (final frequency)')
ax.set_ylabel('|beta_k|^2 (particle number)')
ax.set_title('Bogoliubov particle spectrum')
ax.set_yscale('log')
ax.set_ylim(bottom=max(1e-8, beta_sq[beta_sq > 0].min() * 0.1))

# Panel 2: |beta|^2 vs omega_f (linear scale)
ax = axes[0, 1]
ax.scatter(omega_f_sorted, beta_sq, c='steelblue', s=3, alpha=0.6, edgecolors='none')
if PLANCK_FIT_SUCCESS:
    ax.plot(omega_plot, planck_dist(omega_plot, T_fit), 'r-', lw=2,
            label=f'Planck fit')
    ax.legend(fontsize=8)
ax.set_xlabel('omega_f')
ax.set_ylabel('|beta_k|^2')
ax.set_title('Particle spectrum (linear)')

# Panel 3: Spectral index
ax = axes[0, 2]
if len(n_spectral) > 0:
    ax.scatter(omega_si, n_spectral, c='darkgreen', s=3, alpha=0.6)
    ax.axhline(y=n_global, color='red', ls='--', lw=1.5,
               label=f'global index = {n_global:.3f}')
    ax.axhline(y=0, color='gray', ls=':', lw=1)
    ax.legend(fontsize=8)
ax.set_xlabel('omega_f')
ax.set_ylabel('n(omega) = d ln|beta|^2 / d ln omega')
ax.set_title(f'Spectral index (CV={n_variation:.3f})')

# Panel 4: Delta_omega vs omega_i (frequency shift)
ax = axes[1, 0]
ax.scatter(omega_i_sorted, delta_omega, c='coral', s=3, alpha=0.6)
ax.axhline(y=0, color='gray', ls=':', lw=1)
ax.set_xlabel('omega_i (initial frequency)')
ax.set_ylabel('Delta omega = omega_f - omega_i')
ax.set_title('Frequency shift per mode')

# Panel 5: Residuals from Planck fit
ax = axes[1, 1]
if PLANCK_FIT_SUCCESS:
    ax.scatter(omega_fit, residuals_planck, c='purple', s=3, alpha=0.6)
    ax.axhline(y=0, color='red', ls='--', lw=1)
    ax.set_xlabel('omega_f')
    ax.set_ylabel('Residual (data - Planck)')
    ax.set_title(f'Planck fit residuals (RMS={rms_planck:.2e})')
else:
    ax.text(0.5, 0.5, 'Planck fit failed', ha='center', va='center',
            transform=ax.transAxes, fontsize=14)

# Panel 6: Comparison with s52 lattice
ax = axes[1, 2]
# Plot continuum
ax.scatter(omega_f_sorted, beta_sq, c='steelblue', s=3, alpha=0.3, label='992-mode continuum')
# Plot s52
ax.scatter(E_8, beta_sq_52, c='red', s=80, marker='*', zorder=5, edgecolors='black',
           label='S52 lattice (8-mode)')
for i in range(8):
    ax.annotate(str(labels_52[i]), (E_8[i], beta_sq_52[i]),
                fontsize=6, ha='left', va='bottom')
ax.set_xlabel('omega')
ax.set_ylabel('|beta|^2')
ax.set_title('Continuum vs Lattice Bogoliubov')
ax.legend(fontsize=8)

plt.tight_layout()
plt.savefig('computations/session-55/s55_bogoliubov_992.png', dpi=150)
print(f"Plot saved to computations/session-55/s55_bogoliubov_992.png")

# ============================================================
# Summary
# ============================================================
print(f"\n{'='*60}")
print("SUMMARY")
print(f"{'='*60}")
print(f"Gate: BOGOLIUBOV-992-55")
print(f"Verdict: {verdict}")
print(f"  992 modes, tau: 0.00 -> 0.19 (van Hove fold)")
print(f"  Total particles (unweighted): {N_total_unweighted:.4f}")
print(f"  Total particles (weighted):   {N_total_weighted:.1f}")
print(f"  Planck fit R^2:    {R2_planck:.4f}" if PLANCK_FIT_SUCCESS else "  Planck fit: FAILED")
print(f"  Planck fit T:      {T_fit:.4f} M_KK" if PLANCK_FIT_SUCCESS else "")
print(f"  Spectral index:    n = {n_global:.4f} (CV = {n_variation:.4f})")
print(f"  Spearman rho:      {rho_spearman:.4f}")
print(f"  Anti-thermal frac: {anti_frac:.1%}")
print(f"  KS statistic:     {ks_stat:.4f} (p = {ks_p:.2e})" if not np.isnan(ks_stat) else "")
print(f"\nPhysics: Parker-type particle creation from time-dependent geometry.")
print(f"No horizon, no thermal spectrum, no information paradox.")
