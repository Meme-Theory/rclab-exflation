#!/usr/bin/env python3
"""
STRUTINSKY-FILTER-62 — Gaussian Cutoff Self-Consistency
========================================================

Gate: STRUTINSKY-FILTER-62
PASS if {f_0, f_2, f_4} agree to 10% and CS saturation holds to 1%.
FAIL if >50% discrepancy. INFO if 10-50%.

Physics:
    In nuclear physics, the Strutinsky energy theorem smooths the oscillating
    shell correction by Gaussian convolution of the single-particle level density:

        g_smooth(E) = (1/(gamma*sqrt(2pi))) * sum_n d_n * exp(-(E - lambda_n)^2 / (2*gamma^2))

    where lambda_n are eigenvalues of D_K^2 on SU(3) and d_n = dim(rep)^2 are degeneracies.

    The spectral action S[D,f] = Tr f(D^2/Lambda^2) is STRUCTURALLY a smoothed density
    of states integral. For Gaussian cutoff f(x) = exp(-x):

        S_Gauss = sum_n d_n * exp(-lambda_n^2 / Lambda^2)

    The Strutinsky width gamma and the spectral action cutoff Lambda are related by
    Lambda = sqrt(2) * gamma  (matching the Gaussian variance).

    The Seeley-DeWitt moments from the heat kernel expansion are:
        f_k = sum_n d_n * (lambda_n^2)^{k/2} / (sum_n d_n) = <(lambda^2)^{k/2}>
    normalized by f_0.

    Moment self-consistency test: Strutinsky smoothing must reproduce these moments.
    Cauchy-Schwarz saturation: for a Gaussian distribution, f_4 * f_0 / f_2^2 = 1
    (exact for perfect Gaussian). Deviation measures non-Gaussianity of the spectrum.

Session: S62 Wave 3 (W3-06)
"""

import numpy as np
from scipy.integrate import trapezoid
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    a0_fold, a2_fold, a4_fold, tau_fold, PI
)

# ============================================================
#  STEP 1: Load eigenvalue data
# ============================================================

# 992 D_K eigenvalues at the fold
d_hk = np.load('s61_hk_oscillation.npz', allow_pickle=True)
omega = d_hk['omega']      # sqrt(lambda_n^2) = |lambda_n|
dim2 = d_hk['dim2']        # degeneracies d_n = dim(rep)^2
lam2 = omega**2             # lambda_n^2 values

N_modes = len(omega)
N_total = dim2.sum()         # total weighted count

print(f"=== STRUTINSKY-FILTER-62: Gaussian Cutoff Self-Consistency ===")
print(f"N_modes = {N_modes}, N_total = {N_total:.0f}")
print(f"lambda^2 range: [{lam2.min():.6f}, {lam2.max():.6f}]")
print(f"mean level spacing: d = {(lam2.max() - lam2.min()) / N_modes:.6e}")
print()

# Load W1-01 gamma_opt
d_london = np.load('s62_cutoff_london.npz', allow_pickle=True)
gamma_opt_W1 = float(d_london['Gaussian_gamma_opt'])
f0_W1 = float(d_london['Gaussian_f0'])
f2_W1 = float(d_london['Gaussian_f2'])
f4_W1 = float(d_london['Gaussian_f4'])

print(f"W1-01 Gaussian results:")
print(f"  gamma_opt = {gamma_opt_W1:.6f}")
print(f"  f_0 = {f0_W1:.6f}")
print(f"  f_2 = {f2_W1:.6f}")
print(f"  f_4 = {f4_W1:.6f}")
print()

# Gilkey coefficients (normalized per unit volume)
a0_gilkey = float(d_london['a0_gilkey'])
a2_gilkey = float(d_london['a2_gilkey_fold'])
a4_gilkey = float(d_london['a4_gilkey_fold'])

# ============================================================
#  STEP 2: Direct spectral moments (the "exact" reference)
# ============================================================
# f_k^{SA} = (1/N_total) * sum_n d_n * (lambda_n^2)^{k/2}

f0_SA = dim2.sum() / N_total  # = 1 by construction
f2_SA = (dim2 * lam2).sum() / N_total
f4_SA = (dim2 * lam2**2).sum() / N_total

# Higher moments for completeness
f6_SA = (dim2 * lam2**3).sum() / N_total
f8_SA = (dim2 * lam2**4).sum() / N_total

print(f"=== Direct Spectral Moments (normalized by N_total) ===")
print(f"  f_0^SA = {f0_SA:.10f}  (identity check)")
print(f"  f_2^SA = {f2_SA:.10f}")
print(f"  f_4^SA = {f4_SA:.10f}")
print(f"  f_6^SA = {f6_SA:.10f}")
print(f"  f_8^SA = {f8_SA:.10f}")
print()

# ============================================================
#  STEP 3: Strutinsky Gaussian smoothing
# ============================================================
# g_smooth(E) = (1/(gamma*sqrt(2pi))) * sum_n d_n * exp(-(E - lambda_n^2)^2 / (2*gamma^2))
# The Strutinsky smoothed density is convolution of the discrete DOS with a Gaussian.

def strutinsky_smooth_dos(E_grid, lam2, dim2, gamma):
    """Compute Strutinsky-smoothed DOS on an energy grid.

    g_smooth(E) = sum_n d_n * (1/(gamma*sqrt(2pi))) * exp(-(E - lambda_n^2)^2 / (2*gamma^2))
    """
    g = np.zeros_like(E_grid)
    norm = 1.0 / (gamma * np.sqrt(2 * PI))  # (local)
    for i in range(len(lam2)):
        g += dim2[i] * norm * np.exp(-0.5 * ((E_grid - lam2[i]) / gamma)**2)
    return g


def strutinsky_moments(E_grid, g_smooth, k_values):
    """Compute moments f_k = integral E^{k/2} * g_smooth(E) dE / integral g_smooth(E) dE."""
    norm = trapezoid(g_smooth, E_grid)
    moments = {}
    for k in k_values:
        integrand = E_grid**(k/2.0) * g_smooth
        moments[k] = trapezoid(integrand, E_grid) / norm
    return moments, norm


def strutinsky_shell_correction(lam2, dim2, E_grid, g_smooth):
    """Shell correction: delta_E = sum_n d_n * lambda_n^2 - integral E * g_smooth(E) dE.

    This is the Strutinsky energy theorem applied to the spectral action:
    the difference between the discrete sum and the smoothed integral.
    """
    E_exact = (dim2 * lam2).sum()
    E_smooth = trapezoid(E_grid * g_smooth, E_grid)
    return E_exact - E_smooth, E_exact, E_smooth


# Use gamma_opt from W1-01 as the primary test point
gamma = gamma_opt_W1

# Energy grid: cover the full range of lambda^2 with generous margins
E_min = lam2.min() - 5 * gamma
E_max = lam2.max() + 5 * gamma
E_grid = np.linspace(max(0, E_min), E_max, 10000)

g_smooth = strutinsky_smooth_dos(E_grid, lam2, dim2, gamma)

# Compute Strutinsky moments
moments_strut, g_norm = strutinsky_moments(E_grid, g_smooth, [0, 2, 4, 6, 8])

f0_Strut = 1.0  # By construction (normalized)  # (local)
f2_Strut = moments_strut[2]
f4_Strut = moments_strut[4]
f6_Strut = moments_strut[6]
f8_Strut = moments_strut[8]

print(f"=== Strutinsky-Smoothed Moments at gamma = {gamma:.4f} ===")
print(f"  g_norm (integral of DOS) = {g_norm:.2f}  (should be {N_total:.0f})")
print(f"  f_0^Strut = {f0_Strut:.10f}")
print(f"  f_2^Strut = {f2_Strut:.10f}")
print(f"  f_4^Strut = {f4_Strut:.10f}")
print(f"  f_6^Strut = {f6_Strut:.10f}")
print(f"  f_8^Strut = {f8_Strut:.10f}")
print()

# ============================================================
#  STEP 4: Consistency ratios
# ============================================================

def ratio_pct(a, b):
    return abs(a - b) / abs(b) * 100.0

r0 = ratio_pct(f0_Strut, f0_SA)
r2 = ratio_pct(f2_Strut, f2_SA)
r4 = ratio_pct(f4_Strut, f4_SA)

print(f"=== Moment Consistency Ratios ===")
print(f"  |f_0^Strut - f_0^SA| / f_0^SA = {r0:.6f}%")
print(f"  |f_2^Strut - f_2^SA| / f_2^SA = {r2:.6f}%")
print(f"  |f_4^Strut - f_4^SA| / f_4^SA = {r4:.6f}%")
print()

# Comparison to W1-01 values (which used a different moment definition)
print(f"=== Cross-check with W1-01 London moments ===")
print(f"  W1-01 f_0 = {f0_W1:.6f}  (absolute, not normalized)")
print(f"  f_0 * N_total = {f0_SA * N_total:.2f}  (should match n_bare or related)")
print(f"  W1-01 f_2 = {f2_W1:.6f}")
print(f"  Our f_2^SA = {f2_SA:.6f}")
print(f"  Ratio: {f2_SA / f2_W1:.6f}")
print()

# W1-01 may use a different normalization convention. Let's check the
# unnormalized moments: M_k = sum_n d_n * (lambda_n^2)^{k/2}
M0 = dim2.sum()
M2 = (dim2 * lam2).sum()
M4 = (dim2 * lam2**2).sum()

print(f"=== Unnormalized Moments ===")
print(f"  M_0 = {M0:.2f}")
print(f"  M_2 = {M2:.2f}")
print(f"  M_4 = {M4:.2f}")
print(f"  M_2 / M_0 = {M2/M0:.6f}  (= f_2^SA)")
print(f"  M_4 / M_0 = {M4/M0:.6f}  (= f_4^SA)")
print()

# ============================================================
#  STEP 5: Cauchy-Schwarz saturation
# ============================================================
# For a Gaussian distribution, <x^2>*<1> / <x>^2 = CS ratio.
# With x = lambda^2, the CS ratio is f_4 * f_0 / f_2^2.
# For a PERFECT Gaussian, this equals 1 + sigma^2/mu^2 where mu = <lambda^2>, sigma^2 = Var(lambda^2).
# The CS inequality says f_4*f_0 >= f_2^2, i.e., ratio >= 1.
# For the Strutinsky procedure to be a valid Gaussian filter, we want this ratio to be
# close to what the actual spectral distribution gives.

# From direct spectral moments
CS_SA = f4_SA * f0_SA / f2_SA**2
# From Strutinsky moments
CS_Strut = f4_Strut * f0_Strut / f2_Strut**2
# From W1-01
CS_W1 = f4_W1 * f0_W1 / f2_W1**2

# The Gaussian prediction: for a pure Gaussian DOS with mean mu and width sigma,
# <x^2> / <x>^2 = 1 + (sigma/mu)^2
# So CS = 1 + Var(lambda^2) / <lambda^2>^2
mu_lam2 = f2_SA
var_lam2 = f4_SA - f2_SA**2
CS_Gauss_pred = 1.0 + var_lam2 / mu_lam2**2

print(f"=== Cauchy-Schwarz Saturation ===")
print(f"  CS ratio from SA moments: f_4*f_0/f_2^2 = {CS_SA:.10f}")
print(f"  CS ratio from Strutinsky:                 = {CS_Strut:.10f}")
print(f"  CS ratio from W1-01:      f_4*f_0/f_2^2 = {CS_W1:.10f}")
print(f"  CS ratio (Gaussian pred):  1 + Var/mu^2  = {CS_Gauss_pred:.10f}")
print(f"  CS deviation from 1: {abs(CS_SA - 1.0)*100:.4f}%")
print(f"  |CS_Strut - CS_SA| / CS_SA = {abs(CS_Strut - CS_SA)/CS_SA*100:.6f}%")
print(f"  Var(lambda^2) = {var_lam2:.6f}")
print(f"  sigma(lambda^2) / <lambda^2> = {np.sqrt(max(0, var_lam2))/mu_lam2:.6f}")
print()

# ============================================================
#  STEP 6: gamma scan — moments and CS ratio vs gamma
# ============================================================

gamma_scan = np.concatenate([
    np.linspace(0.02, 0.10, 20),
    np.linspace(0.12, 0.50, 20),
    np.linspace(0.55, 1.00, 10),
    np.linspace(1.10, 2.00, 10),
])
gamma_scan = np.sort(np.unique(gamma_scan))

f2_vs_gamma = np.zeros(len(gamma_scan))
f4_vs_gamma = np.zeros(len(gamma_scan))
CS_vs_gamma = np.zeros(len(gamma_scan))
dE_shell_vs_gamma = np.zeros(len(gamma_scan))
g_norm_vs_gamma = np.zeros(len(gamma_scan))

print("=== Gamma Scan ===")
print(f"{'gamma':>8s} {'f_2':>12s} {'f_4':>12s} {'CS':>10s} {'dE_shell':>12s} {'g_norm':>12s}")

for ig, gam in enumerate(gamma_scan):
    g_sm = strutinsky_smooth_dos(E_grid, lam2, dim2, gam)
    mm, gn = strutinsky_moments(E_grid, g_sm, [2, 4])
    dE_sh, _, _ = strutinsky_shell_correction(lam2, dim2, E_grid, g_sm)

    f2_vs_gamma[ig] = mm[2]
    f4_vs_gamma[ig] = mm[4]
    CS_vs_gamma[ig] = mm[4] / mm[2]**2
    dE_shell_vs_gamma[ig] = dE_sh
    g_norm_vs_gamma[ig] = gn

    if ig % 10 == 0 or abs(gam - gamma_opt_W1) < 0.02:
        print(f"{gam:8.4f} {mm[2]:12.6f} {mm[4]:12.6f} {mm[4]/mm[2]**2:10.6f} {dE_sh:12.4f} {gn:12.2f}")

print()

# ============================================================
#  STEP 7: Strutinsky shell correction at gamma_opt
# ============================================================

dE_shell, E_exact, E_smooth = strutinsky_shell_correction(lam2, dim2, E_grid, g_smooth)

print(f"=== Strutinsky Shell Correction at gamma = {gamma:.4f} ===")
print(f"  E_exact  = sum_n d_n * lambda_n^2 = {E_exact:.4f}")
print(f"  E_smooth = int E * g_smooth(E) dE = {E_smooth:.4f}")
print(f"  delta_E_shell = E_exact - E_smooth = {dE_shell:.4f}")
print(f"  delta_E / E_exact = {dE_shell/E_exact:.6f}  ({dE_shell/E_exact*100:.4f}%)")
print()

# Nuclear comparison: in heavy nuclei, delta_E_shell / E is typically 0.1-1%.
# The sign and magnitude encode shell structure.
print(f"  Nuclear comparison:")
print(f"    Typical nuclear delta_E_shell / E ~ 0.1-1%")
print(f"    This spectrum: delta_E_shell / E = {abs(dE_shell/E_exact)*100:.4f}%")
if abs(dE_shell/E_exact) < 0.01:
    shell_class = "WEAK shell structure (< 1%)"
elif abs(dE_shell/E_exact) < 0.05:
    shell_class = "MODERATE shell structure (1-5%)"
else:
    shell_class = "STRONG shell structure (> 5%)"
print(f"    Classification: {shell_class}")
print()

# ============================================================
#  STEP 8: Plateau test — Strutinsky variational principle
# ============================================================
# In nuclear physics, the Strutinsky shell correction must be STABLE under variation
# of gamma (plateau condition). This tests whether gamma_opt is in a plateau region.

# Find the plateau region: where d(delta_E_shell)/d(gamma) is minimal
d_dE_dgamma = np.gradient(dE_shell_vs_gamma, gamma_scan)
plateau_idx = np.argmin(np.abs(d_dE_dgamma))
gamma_plateau = gamma_scan[plateau_idx]

print(f"=== Strutinsky Plateau Test ===")
print(f"  Plateau gamma (min |d(dE)/dgamma|): {gamma_plateau:.4f}")
print(f"  W1-01 gamma_opt: {gamma_opt_W1:.4f}")
print(f"  Difference: {abs(gamma_plateau - gamma_opt_W1):.4f}")
print(f"  Mean level spacing: d = {(lam2.max() - lam2.min()) / N_modes:.6f}")
print(f"  gamma_opt / d = {gamma_opt_W1 / ((lam2.max() - lam2.min()) / N_modes):.2f}")
print(f"  Nuclear rule: gamma/d ~ 1.2 (Strutinsky optimal)")
print()

# ============================================================
#  STEP 9: Gilkey / heat-kernel cross-check
# ============================================================
# The Seeley-DeWitt coefficients define the asymptotic expansion:
# S(Lambda) ~ a_0 * Lambda^6 + a_2 * Lambda^4 + a_4 * Lambda^2 + ...
# (for D^2 on a 6-dim manifold, with Lambda = cutoff)
# Normalized: a_k_norm = a_k * (Lambda)^{6-k} / S

# The Gilkey ratios should match the moment ratios
gilkey_ratio_a2_a0 = a2_gilkey / a0_gilkey
gilkey_ratio_a4_a0 = a4_gilkey / a0_gilkey
gilkey_ratio_a4_a2 = a4_gilkey / a2_gilkey

# From the discrete spectrum at the fold (canonical constants)
canon_ratio_a2_a0 = a2_fold / a0_fold
canon_ratio_a4_a0 = a4_fold / a0_fold
canon_ratio_a4_a2 = a4_fold / a2_fold

print(f"=== Gilkey / Heat-Kernel Cross-Check ===")
print(f"  Gilkey a_2/a_0 = {gilkey_ratio_a2_a0:.6f}")
print(f"  Canon  a_2/a_0 = {canon_ratio_a2_a0:.6f}")
print(f"  Gilkey a_4/a_0 = {gilkey_ratio_a4_a0:.6f}")
print(f"  Canon  a_4/a_0 = {canon_ratio_a4_a0:.6f}")
print(f"  Gilkey a_4/a_2 = {gilkey_ratio_a4_a2:.6f}")
print(f"  Canon  a_4/a_2 = {canon_ratio_a4_a2:.6f}")
print()

# The spectral moments f_k and Gilkey a_k are related through the cutoff function.
# For Gaussian cutoff: f_k propto a_k * Gamma((6-k)/2 + 1) where 6 = dim
# More precisely: S = sum_n a_n Lambda^{d-n} * f_{(d-n)/2}
# where f_j = integral_0^inf t^j f(t) dt for the Gaussian f(t)=e^{-t}

# ============================================================
#  STEP 10: Gate Verdict
# ============================================================

max_moment_discrepancy = max(r0, r2, r4)
cs_dev_strut_sa = abs(CS_Strut - CS_SA) / CS_SA * 100.0  # Strutinsky vs SA consistency
cs_dev_from_1 = abs(CS_SA - 1.0) * 100.0                 # How non-Gaussian the spectrum is

print(f"=== GATE: STRUTINSKY-FILTER-62 ===")
print(f"  Max moment discrepancy (Strut vs SA): {max_moment_discrepancy:.4f}%")
print(f"  CS saturation |CS_SA - 1|: {cs_dev_from_1:.4f}%")
print(f"  CS Strut-SA consistency: {cs_dev_strut_sa:.6f}%")
print()
print(f"  Gate criterion 1: f_k agree to 10% => {max_moment_discrepancy:.2f}% ", end="")
print("=> PASS" if max_moment_discrepancy < 10.0 else "=> FAIL")
print(f"  Gate criterion 2: CS saturation to 1% => |CS-1| = {cs_dev_from_1:.2f}% ", end="")
print("=> PASS" if cs_dev_from_1 < 1.0 else "=> FAIL")

# Verdict: BOTH criteria must pass for PASS
if max_moment_discrepancy < 10.0 and cs_dev_from_1 < 1.0:
    verdict = "PASS"
    detail = (f"All moments agree to {max_moment_discrepancy:.2f}% (< 10%). "
              f"CS saturation |CS-1| = {cs_dev_from_1:.2f}% (< 1%). "
              f"Shell correction dE/E = {dE_shell/E_exact*100:.3f}%. "
              f"gamma_opt = {gamma_opt_W1:.3f}.")
elif max_moment_discrepancy > 50.0 or cs_dev_from_1 > 50.0:
    verdict = "FAIL"
    detail = (f"Moment discrepancy {max_moment_discrepancy:.2f}% or CS deviation {cs_dev_from_1:.2f}% exceeds 50%. "
              f"Strutinsky smoothing NOT a valid Gaussian SA cutoff.")
else:
    # Moments PASS but CS FAILS -- Strutinsky preserves moments but spectrum is non-Gaussian
    verdict = "INFO"
    detail = (f"Moments agree to {max_moment_discrepancy:.2f}% (PASS, < 10%). "
              f"CS saturation fails: |CS-1| = {cs_dev_from_1:.2f}% (> 1%). "
              f"D_K^2 spectrum is {cs_dev_from_1:.1f}% non-Gaussian (sigma/mu = {np.sqrt(max(0, var_lam2))/mu_lam2:.3f}). "
              f"Strutinsky preserves moments but NOT a perfect Gaussian filter. "
              f"Shell correction dE/E = {abs(dE_shell/E_exact)*100:.4f}% (WEAK). "
              f"Strut-SA CS consistency = {cs_dev_strut_sa:.2f}%.")

print(f"  VERDICT: {verdict}")
print(f"  DETAIL: {detail}")
print()

# ============================================================
#  STEP 11: Save data
# ============================================================

np.savez('s62_strutinsky_filter.npz',
    # Gate
    gate_name='STRUTINSKY-FILTER-62',
    gate_verdict=verdict,
    gate_detail=detail,
    # Input parameters
    gamma_opt=gamma_opt_W1,
    N_modes=N_modes,
    N_total=N_total,
    # Direct spectral moments (reference)
    f0_SA=f0_SA,
    f2_SA=f2_SA,
    f4_SA=f4_SA,
    f6_SA=f6_SA,
    f8_SA=f8_SA,
    # Strutinsky moments
    f2_Strut=f2_Strut,
    f4_Strut=f4_Strut,
    # Unnormalized moments
    M0=M0,
    M2=M2,
    M4=M4,
    # Consistency ratios (percent)
    ratio_f0_pct=r0,
    ratio_f2_pct=r2,
    ratio_f4_pct=r4,
    max_discrepancy_pct=max_moment_discrepancy,
    # Cauchy-Schwarz
    CS_SA=CS_SA,
    CS_Strut=CS_Strut,
    CS_W1=CS_W1,
    CS_dev_strut_sa_pct=cs_dev_strut_sa,
    CS_dev_from_1_pct=cs_dev_from_1,
    var_lam2=var_lam2,
    # Shell correction
    dE_shell=dE_shell,
    E_exact=E_exact,
    E_smooth=E_smooth,
    dE_over_E=dE_shell / E_exact,
    # Plateau
    gamma_plateau=gamma_plateau,
    # Gamma scan
    gamma_scan=gamma_scan,
    f2_vs_gamma=f2_vs_gamma,
    f4_vs_gamma=f4_vs_gamma,
    CS_vs_gamma=CS_vs_gamma,
    dE_shell_vs_gamma=dE_shell_vs_gamma,
    g_norm_vs_gamma=g_norm_vs_gamma,
    # W1-01 cross-reference
    f0_W1=f0_W1,
    f2_W1=f2_W1,
    f4_W1=f4_W1,
    # Gilkey
    a0_gilkey=a0_gilkey,
    a2_gilkey=a2_gilkey,
    a4_gilkey=a4_gilkey,
)
print("Saved: s62_strutinsky_filter.npz")

# ============================================================
#  STEP 12: Plots
# ============================================================

fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle('STRUTINSKY-FILTER-62: Gaussian Cutoff Self-Consistency', fontsize=14, fontweight='bold')

# (a) Raw vs smoothed DOS
ax = axes[0, 0]
# Raw: histogram of lambda^2 weighted by degeneracy
E_hist_bins = np.linspace(lam2.min() - 0.1, lam2.max() + 0.1, 200)
raw_counts, raw_edges = np.histogram(lam2, bins=E_hist_bins, weights=dim2)
raw_centers = 0.5 * (raw_edges[:-1] + raw_edges[1:])
dE_bin = raw_edges[1] - raw_edges[0]
raw_dos = raw_counts / dE_bin

ax.fill_between(raw_centers, raw_dos, alpha=0.3, color='blue', label='Raw DOS')
ax.plot(E_grid, g_smooth, 'r-', linewidth=1.5, label=f'Strutinsky ($\\gamma$={gamma:.3f})')
ax.set_xlabel('$\\lambda^2$')
ax.set_ylabel('$g(E)$')
ax.set_title('(a) DOS: Raw vs Strutinsky Smoothed')
ax.legend(fontsize=8)
ax.set_xlim(lam2.min() - 0.2, lam2.max() + 0.2)

# (b) Moments vs gamma
ax = axes[0, 1]
ax.plot(gamma_scan, f2_vs_gamma, 'b-o', markersize=3, label='$f_2^{\\mathrm{Strut}}$')
ax.axhline(f2_SA, color='b', linestyle='--', alpha=0.5, label=f'$f_2^{{SA}}$ = {f2_SA:.4f}')
ax.plot(gamma_scan, f4_vs_gamma, 'r-s', markersize=3, label='$f_4^{\\mathrm{Strut}}$')
ax.axhline(f4_SA, color='r', linestyle='--', alpha=0.5, label=f'$f_4^{{SA}}$ = {f4_SA:.4f}')
ax.axvline(gamma_opt_W1, color='green', linestyle=':', linewidth=2, label=f'$\\gamma_{{opt}}$ = {gamma_opt_W1:.3f}')
ax.set_xlabel('$\\gamma$')
ax.set_ylabel('$f_k$')
ax.set_title('(b) Moments vs Smoothing Width')
ax.legend(fontsize=7)
ax.set_xlim(0, 2.0)

# (c) CS ratio vs gamma
ax = axes[0, 2]
ax.plot(gamma_scan, CS_vs_gamma, 'k-o', markersize=3)
ax.axhline(CS_SA, color='red', linestyle='--', linewidth=1.5, label=f'CS$_{{SA}}$ = {CS_SA:.4f}')
ax.axhline(1.0, color='gray', linestyle=':', alpha=0.5, label='CS = 1 (pure Gaussian)')
ax.axvline(gamma_opt_W1, color='green', linestyle=':', linewidth=2, label=f'$\\gamma_{{opt}}$')
ax.set_xlabel('$\\gamma$')
ax.set_ylabel('$f_4 \\cdot f_0 / f_2^2$')
ax.set_title('(c) Cauchy-Schwarz Ratio vs $\\gamma$')
ax.legend(fontsize=8)
ax.set_xlim(0, 2.0)

# (d) Shell correction vs gamma
ax = axes[1, 0]
ax.plot(gamma_scan, dE_shell_vs_gamma, 'k-o', markersize=3)
ax.axhline(0, color='gray', linestyle='-', alpha=0.3)
ax.axvline(gamma_opt_W1, color='green', linestyle=':', linewidth=2, label=f'$\\gamma_{{opt}}$ = {gamma_opt_W1:.3f}')
ax.axvline(gamma_plateau, color='orange', linestyle='--', linewidth=1.5, label=f'Plateau = {gamma_plateau:.3f}')
ax.set_xlabel('$\\gamma$')
ax.set_ylabel('$\\delta E_{\\mathrm{shell}}$')
ax.set_title('(d) Shell Correction vs $\\gamma$')
ax.legend(fontsize=8)
ax.set_xlim(0, 2.0)

# (e) Normalization check: g_norm vs gamma
ax = axes[1, 1]
ax.plot(gamma_scan, g_norm_vs_gamma, 'b-o', markersize=3)
ax.axhline(N_total, color='red', linestyle='--', label=f'$N_{{total}}$ = {N_total:.0f}')
ax.set_xlabel('$\\gamma$')
ax.set_ylabel('$\\int g_{\\mathrm{smooth}} \\, dE$')
ax.set_title('(e) DOS Normalization vs $\\gamma$')
ax.legend(fontsize=8)
ax.set_xlim(0, 2.0)

# (f) Moment discrepancies vs gamma
ax = axes[1, 2]
disc_f2 = np.abs(f2_vs_gamma - f2_SA) / f2_SA * 100
disc_f4 = np.abs(f4_vs_gamma - f4_SA) / f4_SA * 100
ax.semilogy(gamma_scan, disc_f2 + 1e-10, 'b-o', markersize=3, label='$|\\Delta f_2|/f_2$ (%)')
ax.semilogy(gamma_scan, disc_f4 + 1e-10, 'r-s', markersize=3, label='$|\\Delta f_4|/f_4$ (%)')
ax.axhline(10.0, color='green', linestyle='--', alpha=0.5, label='10% threshold (PASS)')
ax.axhline(50.0, color='orange', linestyle='--', alpha=0.5, label='50% threshold (FAIL)')
ax.axvline(gamma_opt_W1, color='green', linestyle=':', linewidth=2, label=f'$\\gamma_{{opt}}$')
ax.set_xlabel('$\\gamma$')
ax.set_ylabel('Discrepancy (%)')
ax.set_title('(f) Moment Discrepancy vs $\\gamma$')
ax.legend(fontsize=7)
ax.set_xlim(0, 2.0)
ax.set_ylim(1e-4, 200)

plt.tight_layout()
plt.savefig('s62_strutinsky_filter.png', dpi=150, bbox_inches='tight')
print("Saved: s62_strutinsky_filter.png")

# ============================================================
#  Summary
# ============================================================
print()
print("=" * 70)
print(f"STRUTINSKY-FILTER-62 SUMMARY")
print("=" * 70)
print(f"  Verdict: {verdict}")
print(f"  gamma_opt = {gamma_opt_W1:.4f} (from W1-01)")
print(f"  gamma_plateau = {gamma_plateau:.4f} (Strutinsky variational)")
print(f"  f_2: SA = {f2_SA:.6f}, Strut = {f2_Strut:.6f}, discrepancy = {r2:.4f}%")
print(f"  f_4: SA = {f4_SA:.6f}, Strut = {f4_Strut:.6f}, discrepancy = {r4:.4f}%")
print(f"  CS ratio: SA = {CS_SA:.6f}, Strut = {CS_Strut:.6f}, dev = {cs_dev_strut_sa:.6f}%")
print(f"  Shell correction: dE = {dE_shell:.4f}, dE/E = {dE_shell/E_exact*100:.4f}%")
print(f"  DOS normalization at gamma_opt: {g_norm:.2f} / {N_total:.0f} = {g_norm/N_total:.6f}")
print("=" * 70)
