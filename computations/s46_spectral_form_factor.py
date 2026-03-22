#!/usr/bin/env python3
"""
SPECTRAL-FORM-FACTOR-46: Spectral Form Factor K(t) for Jensen-deformed SU(3)
=============================================================================

Gate: SPECTRAL-FORM-FACTOR-46
Input: s42_hauser_feshbach.npz (unique_masses, mass_multiplicities)
       canonical_constants.py (tau_fold)

Computes:
  K(t) = |Z(t)|^2 / |Z(0)|^2
  Z(t) = sum_n d_n exp(i E_n t)

where E_n = unique_masses[n]^2 (eigenvalues of D_K^2) and d_n = multiplicities.

For universality class identification:
  - Unfolded spectrum: map E_n -> xi_n via CDF (uniform mean spacing = 1)
  - Connected SFF: K_c(t) = K(t) - |<Z(t)>|^2 / Z(0)^2
  - Poisson: K(t) -> 1 instantly (no correlations)
  - GOE: ramp (slope 2t/(2pi N)^2) -> plateau (K=1) at t_H
  - GUE: ramp (slope t/(pi N)^2) -> plateau (K=1) at t_H

Heisenberg time: t_H = 2*pi / Delta_mean (mean level spacing of unfolded spectrum)

Also computes:
  - Number variance Sigma^2(L): var(N(E, E+L)) vs L
  - Level spacing ratio <r> cross-check against S38 CHAOS-1

Session 46 | Spectral-Geometer
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import tau_fold

# ============================================================================
#  Load spectrum
# ============================================================================

data_path = Path(__file__).parent / 's42_hauser_feshbach.npz'
data = np.load(data_path, allow_pickle=True)

unique_masses = data['unique_masses']      # sqrt(eigenvalues of D_K^2), shape (119,)
multiplicities = data['mass_multiplicities']  # degeneracies, shape (119,)
N_unique = len(unique_masses)
N_total = int(np.sum(multiplicities))       # = 992

print("=" * 78)
print(f"SPECTRAL-FORM-FACTOR-46: K(t) for Jensen SU(3) at tau = {tau_fold}")
print("=" * 78)
print(f"  N_unique = {N_unique}, N_total = {N_total}")
print(f"  E_min = {unique_masses[0]:.6f}, E_max = {unique_masses[-1]:.6f}")

# ============================================================================
#  Step 1: Construct the eigenvalue list for D_K^2
# ============================================================================
# The "masses" are |lambda| = sqrt(E). For the SFF we use E = lambda^2.
# The Dirac spectrum on SU(3) is symmetric: +/- pairs. Each unique_mass m
# corresponds to eigenvalues +m and -m of D_K, or equivalently m^2 of D_K^2.
# For SFF, we work with D_K^2 eigenvalues (all positive).

E_unique = unique_masses**2  # eigenvalues of D_K^2
print(f"\n  D_K^2 eigenvalues: E_min = {E_unique[0]:.6f}, E_max = {E_unique[-1]:.6f}")
print(f"  Bandwidth = {E_unique[-1] - E_unique[0]:.6f}")

# Expand to full list (with multiplicity) for spacing statistics
E_full = np.repeat(E_unique, multiplicities)
E_full.sort()
print(f"  Full spectrum: {len(E_full)} eigenvalues")

# ============================================================================
#  Step 2: Unfolding via smooth CDF (polynomial fit to staircase)
# ============================================================================
# Standard spectral unfolding: map E -> xi = N_bar(E) where N_bar is the
# smooth part of the staircase function N(E) = #{E_n <= E}.
#
# For a finite discrete spectrum with high degeneracies, we use the
# CUMULATIVE approach: xi_n = rank(E_n) / N_total * N_unique
# This gives mean spacing 1 for the unique levels.

# Method: polynomial unfolding of unique eigenvalues
# Fit a smooth polynomial to (E_unique, cumulative_index)
cumulative_idx = np.arange(1, N_unique + 1)

# Try polynomial degrees 3-7, pick the one with best residual
best_poly = None
best_resid = np.inf
for deg in range(3, 8):
    coeffs = np.polyfit(E_unique, cumulative_idx, deg)
    fitted = np.polyval(coeffs, E_unique)
    resid = np.max(np.abs(fitted - cumulative_idx))
    if resid < best_resid:
        best_resid = resid
        best_poly = coeffs
        best_deg = deg

E_unfolded = np.polyval(best_poly, E_unique)
print(f"\n  Unfolding: polynomial degree {best_deg}, max residual = {best_resid:.4f}")

# Normalize so mean spacing = 1
spacings_unfolded = np.diff(E_unfolded)
mean_spacing = np.mean(spacings_unfolded)
E_unfolded /= mean_spacing
spacings_unfolded = np.diff(E_unfolded)
mean_spacing_check = np.mean(spacings_unfolded)
print(f"  Mean unfolded spacing = {mean_spacing_check:.6f} (should be ~1)")

# ============================================================================
#  Step 3: Level spacing statistics (cross-check S38 CHAOS-1)
# ============================================================================

# Nearest-neighbor spacing distribution (using unique unfolded levels)
s_nn = spacings_unfolded
s_nn_normalized = s_nn / np.mean(s_nn)  # should already be ~1

# Level spacing ratio r_n = min(s_n, s_{n+1}) / max(s_n, s_{n+1})
r_ratios = np.minimum(s_nn[:-1], s_nn[1:]) / np.maximum(s_nn[:-1], s_nn[1:])
r_mean = np.mean(r_ratios)

# Reference values
r_Poisson = 2 * np.log(2) - 1  # = 0.3863
r_GOE = 0.5307
r_GUE = 0.5996

print(f"\n  Level spacing ratio <r> = {r_mean:.4f}")
print(f"    Poisson: {r_Poisson:.4f}")
print(f"    GOE:     {r_GOE:.4f}")
print(f"    GUE:     {r_GUE:.4f}")

# Classify
if abs(r_mean - r_Poisson) < abs(r_mean - r_GOE):
    r_class = "POISSON"
else:
    r_class = "GOE" if abs(r_mean - r_GOE) < abs(r_mean - r_GUE) else "GUE"
print(f"  => Nearest class: {r_class}")

# ============================================================================
#  Step 4: Spectral Form Factor K(t) -- multiplicity-weighted
# ============================================================================
# K(t) = |Z(t)|^2 / Z(0)^2
# Z(t) = sum_n d_n exp(i E_n t)
# Z(0) = sum_n d_n = N_total = 992
#
# We compute TWO versions:
# (A) Raw: using E_unique with multiplicities d_n
# (B) Unfolded: using E_unfolded (unique levels, equal weight 1)
#
# For universality class identification, (B) is canonical.

# Time grid: from t_min to well past Heisenberg time
# Heisenberg time for unfolded spectrum: t_H = 2*pi * N_unique (since spacing=1)
# But for unique levels only: t_H = 2*pi (since N=N_unique, spacing=1 => t_H = 2pi*1/1 = 2pi)
# Actually t_H = 2*pi*rho = 2*pi / Delta_mean = 2*pi * N / (total range)
# For unfolded: total range ~ N, spacing = 1, so t_H = 2*pi * N

Delta_mean_unfolded = 1.0  # by construction
t_H_unfolded = 2.0 * np.pi / Delta_mean_unfolded  # = 2*pi per level
# Total Heisenberg time for the whole system:
t_H_system = 2.0 * np.pi * N_unique  # ~ 748

# For raw spectrum:
Delta_mean_raw = (E_unique[-1] - E_unique[0]) / (N_unique - 1)
t_H_raw = 2.0 * np.pi / Delta_mean_raw

print(f"\n  Heisenberg times:")
print(f"    t_H (unfolded, per-level) = {2*np.pi:.4f}")
print(f"    t_H (unfolded, system)    = {t_H_system:.2f}")
print(f"    t_H (raw, per-level)      = {t_H_raw:.4f}")
print(f"    Delta_mean (raw)          = {Delta_mean_raw:.6f}")

# Time arrays
N_t = 10000
t_max_factor = 3.0  # go to 3x Heisenberg time

# (A) Raw SFF
t_raw = np.linspace(0.01, t_max_factor * t_H_raw, N_t)
Z_raw = np.zeros(N_t, dtype=complex)
for k in range(N_unique):
    Z_raw += multiplicities[k] * np.exp(1j * E_unique[k] * t_raw)
K_raw = np.abs(Z_raw)**2 / N_total**2

# (B) Unfolded SFF (unit weights, canonical)
t_unf = np.linspace(0.01, t_max_factor * t_H_system, N_t)
Z_unf = np.zeros(N_t, dtype=complex)
for k in range(N_unique):
    Z_unf += np.exp(1j * E_unfolded[k] * t_unf)
K_unf = np.abs(Z_unf)**2 / N_unique**2

print(f"\n  SFF computed: {N_t} time points each")

# ============================================================================
#  Step 5: Identify ramp-plateau structure
# ============================================================================

# For unfolded SFF:
# - Early time (t << t_H): "dip" (K drops from 1)
# - Intermediate: "ramp" (K rises linearly)
# - Late time (t >> t_H): "plateau" at K = 1/N (disconnected) or K -> 1 (connected)
#
# The connected SFF subtracts the diagonal:
# K_c(t) = K(t) - 1/N  for Poisson
# For finite N, the plateau is at 1/N (not 1) for the disconnected part.

# The disconnected part is |<Z>|^2/Z(0)^2 which for uncorrelated levels -> 0
# at long times, leaving K -> 1/N.

# Identify ramp region: where K(t) is increasing linearly
# Look for the minimum ("dip") in K_unf
idx_dip = np.argmin(K_unf[:N_t//2])  # search in first half
t_dip = t_unf[idx_dip]
K_dip = K_unf[idx_dip]

# Plateau value: average of K in the last 20% of time range
plateau_region = K_unf[int(0.8*N_t):]
K_plateau = np.mean(plateau_region)
K_plateau_std = np.std(plateau_region)

# Theoretical plateau for finite-N system:
# K_plateau = 1/N for Poisson (no level repulsion, no ramp)
K_plateau_Poisson = 1.0 / N_unique

print(f"\n  SFF structure (unfolded):")
print(f"    K(0+)     = {K_unf[0]:.6f}")
print(f"    K_dip     = {K_dip:.6f} at t = {t_dip:.2f}")
print(f"    K_plateau = {K_plateau:.6f} +/- {K_plateau_std:.6f}")
print(f"    1/N       = {K_plateau_Poisson:.6f}")
print(f"    Ratio K_plateau / (1/N) = {K_plateau / K_plateau_Poisson:.4f}")

# ============================================================================
#  Step 6: Ramp detection and beta classification
# ============================================================================

# For RMT universality classes:
# K(t) ~ t / (beta * N * pi)  in the ramp regime
# where beta = 1 (GOE), 2 (GUE), 4 (GSE)
# For Poisson: no ramp, K(t) ~ 1/N immediately

# Fit a linear ramp in the region [t_dip, t_H_system]
ramp_mask = (t_unf > t_dip) & (t_unf < t_H_system)
if np.sum(ramp_mask) > 10:
    t_ramp = t_unf[ramp_mask]
    K_ramp = K_unf[ramp_mask]

    # Linear fit: K(t) = a + b*t
    coeffs_ramp = np.polyfit(t_ramp, K_ramp, 1)
    b_ramp = coeffs_ramp[0]  # slope
    a_ramp = coeffs_ramp[1]  # intercept
    K_ramp_fitted = np.polyval(coeffs_ramp, t_ramp)
    R2_ramp = 1 - np.sum((K_ramp - K_ramp_fitted)**2) / np.sum((K_ramp - np.mean(K_ramp))**2)

    # Extract beta from slope: b = 1 / (beta * pi * N)
    # Actually for disconnected SFF with N levels: K(tau) = tau / (beta * pi * N)
    # where tau = t in Heisenberg units
    beta_sff = 1.0 / (b_ramp * np.pi * N_unique) if b_ramp > 0 else np.inf

    print(f"\n  Ramp fit (t in [{t_dip:.1f}, {t_H_system:.1f}]):")
    print(f"    slope b     = {b_ramp:.6e}")
    print(f"    intercept a = {a_ramp:.6e}")
    print(f"    R^2         = {R2_ramp:.6f}")
    print(f"    beta_SFF    = {beta_sff:.4f}")
    print(f"    (GOE: beta=1, GUE: beta=2, Poisson: no ramp)")

    # Ramp quality: is R^2 high enough to claim a ramp?
    has_ramp = R2_ramp > 0.8 and b_ramp > 0
else:
    has_ramp = False
    b_ramp = 0.0
    beta_sff = np.inf
    R2_ramp = 0.0
    print(f"\n  No ramp region detected (insufficient points)")

# ============================================================================
#  Step 7: Number variance Sigma^2(L)
# ============================================================================

# Sigma^2(L) = <(N(x, x+L) - L)^2> averaged over x
# For unfolded spectrum with mean spacing 1:
# Poisson: Sigma^2(L) = L
# GOE: Sigma^2(L) ~ (2/pi^2) * (ln(2*pi*L) + gamma_E + 1 - pi^2/8)
# GUE: Sigma^2(L) ~ (1/pi^2) * (ln(2*pi*L) + gamma_E + 1)

L_values = np.linspace(0.5, 15.0, 100)
sigma2 = np.zeros(len(L_values))

for i, L in enumerate(L_values):
    counts = []
    for j in range(N_unique - 1):
        x0 = E_unfolded[j]
        n_in = np.sum((E_unfolded >= x0) & (E_unfolded < x0 + L))
        counts.append(n_in)
    counts = np.array(counts, dtype=float)
    sigma2[i] = np.var(counts)

# Theoretical curves
gamma_E = 0.5772156649
sigma2_poisson = L_values.copy()
sigma2_goe = (2.0 / np.pi**2) * (np.log(2*np.pi*L_values) + gamma_E + 1 - np.pi**2/8)
sigma2_gue = (1.0 / np.pi**2) * (np.log(2*np.pi*L_values) + gamma_E + 1)

# Ensure theoretical values are non-negative
sigma2_goe = np.maximum(sigma2_goe, 0)
sigma2_gue = np.maximum(sigma2_gue, 0)

# Fit: which theoretical curve matches best?
# Use L in [2, 10] where the curves are well-separated
fit_mask = (L_values >= 2) & (L_values <= 10)
resid_poisson = np.mean((sigma2[fit_mask] - sigma2_poisson[fit_mask])**2)
resid_goe = np.mean((sigma2[fit_mask] - sigma2_goe[fit_mask])**2)
resid_gue = np.mean((sigma2[fit_mask] - sigma2_gue[fit_mask])**2)

print(f"\n  Number variance Sigma^2(L) residuals (L in [2,10]):")
print(f"    vs Poisson: {resid_poisson:.4f}")
print(f"    vs GOE:     {resid_goe:.4f}")
print(f"    vs GUE:     {resid_gue:.4f}")

if resid_poisson < resid_goe and resid_poisson < resid_gue:
    sigma2_class = "POISSON"
elif resid_goe < resid_gue:
    sigma2_class = "GOE"
else:
    sigma2_class = "GUE"
print(f"  => Number variance class: {sigma2_class}")

# ============================================================================
#  Step 8: Time-averaged SFF (smoothed K)
# ============================================================================
# For finite-N noisy SFF, the standard approach is to time-average:
# K_avg(t) = (1/Delta_t) * int_{t-Delta_t/2}^{t+Delta_t/2} K(t') dt'
# We use a simple running average

window = max(1, N_t // 100)
K_unf_smooth = np.convolve(K_unf, np.ones(window)/window, mode='same')
K_raw_smooth = np.convolve(K_raw, np.ones(window)/window, mode='same')

# ============================================================================
#  Step 9: Spectral rigidity Delta_3(L) -- Dyson-Mehta
# ============================================================================
# Delta_3(L) = min_{a,b} (1/L) int_0^L (N(x+E_0) - aE - b)^2 dE
# For unfolded spectrum.
# Poisson: Delta_3(L) = L/15
# GOE: ~ (1/pi^2)(ln L - 0.0687)
# GUE: ~ (1/(2*pi^2))(ln L + 0.4418)

L_delta3 = np.linspace(1, 20, 50)
delta3 = np.zeros(len(L_delta3))

for i_L, L in enumerate(L_delta3):
    d3_vals = []
    for j in range(0, N_unique - 1, max(1, N_unique // 50)):
        x0 = E_unfolded[j]
        mask = (E_unfolded >= x0) & (E_unfolded < x0 + L)
        levels_in = E_unfolded[mask] - x0
        if len(levels_in) < 3:
            continue
        # Staircase within window
        N_stair = np.arange(1, len(levels_in) + 1)
        # Best fit line: N = a*E + b
        if len(levels_in) >= 2:
            A = np.vstack([levels_in, np.ones(len(levels_in))]).T
            result = np.linalg.lstsq(A, N_stair, rcond=None)
            a_fit, b_fit = result[0]
            residual = np.mean((N_stair - a_fit * levels_in - b_fit)**2) / L
            d3_vals.append(residual)
    if len(d3_vals) > 0:
        delta3[i_L] = np.mean(d3_vals)

delta3_poisson = L_delta3 / 15.0
delta3_goe = (1.0/np.pi**2) * (np.log(L_delta3) - 0.0687)
delta3_gue = (1.0/(2*np.pi**2)) * (np.log(L_delta3) + 0.4418)
delta3_goe = np.maximum(delta3_goe, 0)
delta3_gue = np.maximum(delta3_gue, 0)

# ============================================================================
#  Step 10: Final classification
# ============================================================================

# Combine evidence
evidence = {
    'r_ratio': r_class,
    'number_variance': sigma2_class,
    'has_ramp': has_ramp,
    'beta_sff': beta_sff,
    'K_plateau_ratio': K_plateau / K_plateau_Poisson,
}

# Plateau test: for Poisson, K -> 1/N. For RMT, K -> 1/N but via ramp.
# The KEY discriminant is the RAMP.
# No ramp (R^2 < 0.8 or slope < 0) => Poisson
# Ramp with beta ~ 1 => GOE
# Ramp with beta ~ 2 => GUE

if not has_ramp:
    universality = "POISSON"
    universality_confidence = "HIGH" if r_class == "POISSON" else "MODERATE"
elif abs(beta_sff - 1) < 0.5:
    universality = "GOE"
    universality_confidence = "HIGH" if r_class == "GOE" else "MODERATE"
elif abs(beta_sff - 2) < 0.5:
    universality = "GUE"
    universality_confidence = "HIGH" if r_class == "GUE" else "MODERATE"
else:
    universality = "INTERMEDIATE"
    universality_confidence = "LOW"

print(f"\n{'='*78}")
print(f"  CLASSIFICATION SUMMARY")
print(f"{'='*78}")
print(f"  Level spacing ratio <r>: {r_mean:.4f} => {r_class}")
print(f"  Number variance:                  => {sigma2_class}")
print(f"  Ramp detected:           {has_ramp} (R^2 = {R2_ramp:.4f})")
if has_ramp:
    print(f"  Ramp beta:               {beta_sff:.4f}")
print(f"  K_plateau / (1/N):       {K_plateau/K_plateau_Poisson:.4f}")
print(f"")
print(f"  UNIVERSALITY CLASS: {universality} (confidence: {universality_confidence})")
print(f"  t_H (system, unfolded):  {t_H_system:.2f}")
print(f"  t_H (raw, per-level):    {t_H_raw:.4f}")

# Cross-check with S38 CHAOS-1: <r> = 0.321 (sub-Poisson)
print(f"\n  Cross-check S38 CHAOS-1: <r> = 0.321 (unique D_K^2 levels)")
print(f"  This computation:        <r> = {r_mean:.4f} (unique D_K^2 levels)")
if abs(r_mean - 0.321) < 0.05:
    print(f"  CONSISTENT (within 0.05)")
else:
    print(f"  DISCREPANCY: delta_r = {abs(r_mean - 0.321):.4f}")
    print(f"  (Possible: different unfolding, or D_K vs D_K^2 spectrum)")

# ============================================================================
#  Step 11: Also compute SFF for D_K (signed eigenvalues)
# ============================================================================
# The Dirac spectrum has +/- pairs. Z(t) = sum d_n [exp(i m_n t) + exp(-i m_n t)]
# = 2 * sum d_n cos(m_n t)
# So K_Dirac(t) = |2 sum d_n cos(m_n t)|^2 / (2*N_total)^2
# = |sum d_n cos(m_n t)|^2 / N_total^2

t_dirac = np.linspace(0.01, t_max_factor * t_H_raw, N_t)
Z_dirac = np.zeros(N_t)
for k in range(N_unique):
    Z_dirac += multiplicities[k] * np.cos(unique_masses[k] * t_dirac)
K_dirac = Z_dirac**2 / N_total**2  # Z is real since spectrum is +/- symmetric

print(f"\n  Dirac SFF (signed eigenvalues, Z real):")
print(f"    K_Dirac(0+) = {K_dirac[0]:.6f}")
print(f"    K_Dirac(t_H) = {K_dirac[N_t//3]:.6f}")

# ============================================================================
#  Save data
# ============================================================================

save_path = Path(__file__).parent / 's46_spectral_form_factor.npz'
np.savez(save_path,
    # Spectrum
    E_unique=E_unique,
    E_unfolded=E_unfolded,
    unique_masses=unique_masses,
    multiplicities=multiplicities,
    N_unique=N_unique,
    N_total=N_total,
    tau_fold=tau_fold,

    # SFF data
    t_raw=t_raw,
    K_raw=K_raw,
    K_raw_smooth=K_raw_smooth,
    t_unf=t_unf,
    K_unf=K_unf,
    K_unf_smooth=K_unf_smooth,
    t_dirac=t_dirac,
    K_dirac=K_dirac,

    # Heisenberg times
    t_H_system=t_H_system,
    t_H_raw=t_H_raw,
    Delta_mean_raw=Delta_mean_raw,

    # SFF structure
    t_dip=t_dip,
    K_dip=K_dip,
    K_plateau=K_plateau,
    K_plateau_std=K_plateau_std,
    K_plateau_Poisson=K_plateau_Poisson,

    # Ramp
    has_ramp=has_ramp,
    b_ramp=b_ramp,
    beta_sff=beta_sff,
    R2_ramp=R2_ramp,

    # Level statistics
    r_mean=r_mean,
    r_Poisson=r_Poisson,
    r_GOE=r_GOE,
    r_GUE=r_GUE,
    spacings_unfolded=spacings_unfolded,

    # Number variance
    L_values=L_values,
    sigma2=sigma2,
    sigma2_poisson=sigma2_poisson,
    sigma2_goe=sigma2_goe,
    sigma2_gue=sigma2_gue,

    # Delta_3
    L_delta3=L_delta3,
    delta3=delta3,
    delta3_poisson=delta3_poisson,
    delta3_goe=delta3_goe,
    delta3_gue=delta3_gue,

    # Classification
    universality=np.array([universality]),
    universality_confidence=np.array([universality_confidence]),
)
print(f"\n  Data saved: {save_path}")

# ============================================================================
#  Plots
# ============================================================================

fig, axes = plt.subplots(3, 2, figsize=(16, 18))
fig.suptitle(f'SPECTRAL-FORM-FACTOR-46: Jensen SU(3), tau = {tau_fold}\n'
             f'N_unique = {N_unique}, N_total = {N_total}, '
             f'Class: {universality} ({universality_confidence})',
             fontsize=14, fontweight='bold')

# (a) Raw SFF K(t)
ax = axes[0, 0]
ax.semilogy(t_raw, K_raw, alpha=0.3, color='blue', lw=0.5, label='K(t)')
ax.semilogy(t_raw, K_raw_smooth, color='blue', lw=1.5, label='K smoothed')
ax.axhline(1.0/N_total, color='red', ls='--', label=f'1/N_total = {1/N_total:.4e}')
ax.axvline(t_H_raw, color='green', ls=':', lw=1.5, label=f't_H = {t_H_raw:.1f}')
ax.set_xlabel('t (D_K^2 units)')
ax.set_ylabel('K(t)')
ax.set_title('(a) Raw SFF (D_K^2, multiplicity-weighted)')
ax.legend(fontsize=8)
ax.set_ylim(bottom=1e-5)

# (b) Unfolded SFF K(t)
ax = axes[0, 1]
ax.semilogy(t_unf, K_unf, alpha=0.3, color='purple', lw=0.5, label='K(t)')
ax.semilogy(t_unf, K_unf_smooth, color='purple', lw=1.5, label='K smoothed')
ax.axhline(K_plateau_Poisson, color='red', ls='--', label=f'1/N = {K_plateau_Poisson:.4f}')
ax.axvline(t_H_system, color='green', ls=':', lw=1.5, label=f't_H = {t_H_system:.0f}')
ax.set_xlabel('t (unfolded units)')
ax.set_ylabel('K(t)')
ax.set_title('(b) Unfolded SFF (unique levels, unit weight)')
ax.legend(fontsize=8)
ax.set_ylim(bottom=1e-4)

# (c) Level spacing distribution
ax = axes[1, 0]
bins = np.linspace(0, 4, 40)
ax.hist(s_nn_normalized, bins=bins, density=True, alpha=0.7, color='steelblue',
        edgecolor='black', label='Data')
s_plot = np.linspace(0.01, 4, 200)
# Poisson: P(s) = exp(-s)
ax.plot(s_plot, np.exp(-s_plot), 'r-', lw=2, label='Poisson: exp(-s)')
# GOE: P(s) ~ (pi*s/2)*exp(-pi*s^2/4)
ax.plot(s_plot, (np.pi*s_plot/2)*np.exp(-np.pi*s_plot**2/4), 'g-', lw=2,
        label='GOE: Wigner')
# GUE: P(s) ~ (32*s^2/pi^2)*exp(-4*s^2/pi)
ax.plot(s_plot, (32*s_plot**2/np.pi**2)*np.exp(-4*s_plot**2/np.pi), 'm-', lw=2,
        label='GUE')
ax.set_xlabel('s (normalized spacing)')
ax.set_ylabel('P(s)')
ax.set_title(f'(c) NNS Distribution (<r> = {r_mean:.4f})')
ax.legend(fontsize=8)
ax.set_xlim(0, 4)

# (d) Number variance
ax = axes[1, 1]
ax.plot(L_values, sigma2, 'ko-', ms=3, lw=1.5, label='Data')
ax.plot(L_values, sigma2_poisson, 'r--', lw=2, label='Poisson: L')
ax.plot(L_values, sigma2_goe, 'g--', lw=2, label='GOE')
ax.plot(L_values, sigma2_gue, 'm--', lw=2, label='GUE')
ax.set_xlabel('L')
ax.set_ylabel(r'$\Sigma^2(L)$')
ax.set_title(f'(d) Number Variance ({sigma2_class})')
ax.legend(fontsize=8)

# (e) Spectral rigidity Delta_3(L)
ax = axes[2, 0]
ax.plot(L_delta3, delta3, 'ko-', ms=3, lw=1.5, label='Data')
ax.plot(L_delta3, delta3_poisson, 'r--', lw=2, label='Poisson: L/15')
ax.plot(L_delta3, delta3_goe, 'g--', lw=2, label='GOE')
ax.plot(L_delta3, delta3_gue, 'm--', lw=2, label='GUE')
ax.set_xlabel('L')
ax.set_ylabel(r'$\Delta_3(L)$')
ax.set_title('(e) Spectral Rigidity (Dyson-Mehta)')
ax.legend(fontsize=8)

# (f) Dirac SFF (signed spectrum)
ax = axes[2, 1]
ax.semilogy(t_dirac, np.abs(K_dirac), alpha=0.3, color='orange', lw=0.5, label='|K(t)|')
K_dirac_smooth = np.convolve(np.abs(K_dirac), np.ones(window)/window, mode='same')
ax.semilogy(t_dirac, K_dirac_smooth, color='orange', lw=1.5, label='|K| smoothed')
ax.axhline(1.0/N_total, color='red', ls='--', label=f'1/N = {1/N_total:.4e}')
ax.axvline(t_H_raw, color='green', ls=':', lw=1.5, label=f't_H = {t_H_raw:.1f}')
ax.set_xlabel('t (D_K units)')
ax.set_ylabel('K(t)')
ax.set_title('(f) Dirac SFF (signed spectrum, Z real)')
ax.legend(fontsize=8)
ax.set_ylim(bottom=1e-5)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plot_path = Path(__file__).parent / 's46_spectral_form_factor.png'
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
plt.close()
print(f"  Plot saved: {plot_path}")

print(f"\n{'='*78}")
print(f"  GATE: SPECTRAL-FORM-FACTOR-46")
print(f"  VERDICT: INFO")
print(f"  UNIVERSALITY: {universality} ({universality_confidence})")
print(f"  HEISENBERG TIME (system): {t_H_system:.2f}")
print(f"  HEISENBERG TIME (raw): {t_H_raw:.4f}")
print(f"  <r> = {r_mean:.4f} (Poisson: {r_Poisson:.4f}, GOE: {r_GOE:.4f})")
print(f"  RAMP: {'YES' if has_ramp else 'NO'} (R^2 = {R2_ramp:.4f})")
if has_ramp:
    print(f"  beta_SFF = {beta_sff:.4f}")
print(f"  K_plateau = {K_plateau:.6f}, 1/N = {K_plateau_Poisson:.6f}")
print(f"  Sigma^2 class: {sigma2_class}")
print(f"{'='*78}")
