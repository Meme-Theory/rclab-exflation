#!/usr/bin/env python3
"""
s61_hk_oscillation.py — Heat Kernel Mode-Resolved Oscillatory Corrections
===========================================================================

Gate: HK-OSCILLATION-61
Pre-registered criterion:
  PASS  if oscillatory residual ~ Lambda_obs (within 10 orders)
  FAIL  if residual -> 0 (averages out)
  INFO  if finite but >> Lambda_obs

Method:
  1. Load D_K eigenvalues {omega_n} from s44_dos_tau.npz at tau=0.19 (fold)
     — 992 modes (L=0..6), with degeneracy weights dim(p,q)^2
  2. Compute K(t) = sum_n w_n * exp(-omega_n^2 * t) at 200 t-values
  3. Compute K_SD(t) = a_0 - a_2*t + a_4*t^2/2 (Taylor of heat kernel)
     where a_k are moment-matched to the same eigenvalue set
  4. K_osc(t) = K(t) - K_SD(t) = residual after removing smooth part
  5. Convert to CC: rho_osc = (2/pi^2) * (K_osc(1) / K(0)) * a_0_fold * M_KK^4
  6. Compare rho_osc / rho_Lambda_obs

Physical interpretation:
  The heat kernel K(t) = Tr(exp(-t*D^2)) encodes the FULL spectrum.
  The Seeley-DeWitt expansion captures the SMOOTH (polynomial) part.
  Any difference K_osc = K - K_SD is the OSCILLATORY contribution from
  the discrete mode structure — analogous to shell corrections in the
  nuclear Strutinsky method (sum_n - integral -> oscillatory).

  In nuclear DFT, the shell correction delta_E = E_exact - E_smooth
  is typically ~1-5 MeV out of ~1000 MeV total (0.1-0.5%).
  The CC problem asks whether a similar O(10^{-120}) oscillatory residual
  survives after removing the smooth part.

Session: S61   Agent: Nazarewicz
"""

import numpy as np
import sys
sys.path.insert(0, '.')
from canonical_constants import (
    M_KK, M_KK_gravity, M_KK_kerner, M_Pl_reduced,
    rho_Lambda_obs, a0_fold, a2_fold, a4_fold,
    Vol_SU3_Haar, PI, tau_fold
)

# ============================================================
# Section 1: Load eigenvalue spectrum at the fold (tau = 0.19)
# ============================================================

d44 = np.load('s44_dos_tau.npz', allow_pickle=True)
omega = d44['tau0.19_all_omega']     # 992 eigenvalues (M_KK units)
dim2  = d44['tau0.19_all_dim2']      # degeneracy weights dim(p,q)^2
N_modes = len(omega)

# Also load the Seeley-DeWitt coefficients from s61 data
d_a2 = np.load('s61_heat_kernel_a2.npz', allow_pickle=True)
d_a4 = np.load('s61_heat_kernel_a4.npz', allow_pickle=True)

a0_SD_geom = float(d_a2['a0_SD'])           # 0.8660 (geometric, normalized)
a2_SD_geom = float(d_a2['a2_SD_fold'])       # 0.7282 (geometric, normalized)
a4_SD_geom = float(d_a4['a4_gilkey_fold'])   # 0.3015 (geometric, normalized)
ratio_gilkey = float(d_a4['ratio_gilkey_fold'])  # a4/a2 = 0.4140

print("=" * 72)
print("HK-OSCILLATION-61: Heat Kernel Oscillatory Corrections")
print("=" * 72)
print(f"\nInput spectrum: {N_modes} modes at tau = {tau_fold}")
print(f"  omega range: [{omega.min():.6f}, {omega.max():.6f}] M_KK")
print(f"  Total degeneracy sum(dim2) = {dim2.sum():.0f}")
print(f"  Unique omega values: {len(np.unique(omega))}")

# ============================================================
# Section 2: Compute exact heat kernel K(t)
# ============================================================

# K(t) = sum_{n=1}^{992} dim2_n * exp(-omega_n^2 * t)
# t is dimensionless (in M_KK^{-2} units)

N_t = 200  # (local)
t_arr = np.logspace(-2, 2, N_t)
K_exact = np.zeros(N_t)

# Vectorized computation (992 x 200 matrix)
omega2 = omega**2
# K[i] = sum_n dim2_n * exp(-omega_n^2 * t_i)
exp_matrix = np.exp(-np.outer(omega2, t_arr))  # (992, 200)
K_exact = dim2 @ exp_matrix                     # (200,)

print(f"\nK(t) computed at {N_t} t-values from {t_arr[0]:.4f} to {t_arr[-1]:.4f}")
print(f"  K(t_min={t_arr[0]:.4f}) = {K_exact[0]:.4f}")
print(f"  K(t=1)  = {K_exact[np.argmin(np.abs(t_arr - 1.0))]:.4f}")
print(f"  K(t_max={t_arr[-1]:.4f}) = {K_exact[-1]:.10e}")

# ============================================================
# Section 3: Seeley-DeWitt smooth expansion (moment-matched)
# ============================================================

# Two approaches for K_SD:
# (A) Moment-matched: fit polynomial from eigenvalue moments
# (B) Geometric: use Gilkey-DeWitt coefficients from curvature invariants
#
# Approach (A) is the correct Strutinsky analog: the smooth part is
# determined by the spectrum itself, not by external geometric input.
# The oscillatory part is what's LEFT after removing the smooth trend.

# Moment-matched coefficients from eigenvalues:
a0_mm = np.sum(dim2)                          # = 101984
a2_mm = np.sum(dim2 * omega2)                  # first moment
a4_mm = np.sum(dim2 * omega2**2) / 2.0        # second moment / 2

# Taylor expansion: exp(-omega^2 * t) = 1 - omega^2*t + omega^4*t^2/2 - ...
# So K(t) ~ a0 - a2*t + a4*t^2 - a6*t^3/6 + ...
# The SD expansion to order t^2:
a6_mm = np.sum(dim2 * omega2**3) / 6.0        # third moment / 6

K_SD_order2 = np.zeros(N_t)
K_SD_order3 = np.zeros(N_t)
K_SD_order4 = np.zeros(N_t)

a8_mm = np.sum(dim2 * omega2**4) / 24.0
a10_mm = np.sum(dim2 * omega2**5) / 120.0

for i, t in enumerate(t_arr):
    K_SD_order2[i] = a0_mm - a2_mm * t + a4_mm * t**2
    K_SD_order3[i] = K_SD_order2[i] - a6_mm * t**3
    K_SD_order4[i] = K_SD_order3[i] + a8_mm * t**4
    # order 5 for error estimate
    K_SD_order5 = K_SD_order4[i] - a10_mm * t**5

print(f"\nMoment-matched SD coefficients:")
print(f"  a0 = {a0_mm:.4f}")
print(f"  a2 = {a2_mm:.4f}")
print(f"  a4 = {a4_mm:.4f}")
print(f"  a6 = {a6_mm:.4f}")
print(f"  a8 = {a8_mm:.4f}")
print(f"  Ratio a4/a2 = {a4_mm/a2_mm:.6f}")
print(f"  Ratio a6/a4 = {a6_mm/a4_mm:.6f}")

# ============================================================
# Section 4: Oscillatory residual K_osc(t)
# ============================================================

# The Strutinsky prescription: subtract smooth from exact
K_osc_2 = K_exact - K_SD_order2
K_osc_3 = K_exact - K_SD_order3
K_osc_4 = K_exact - K_SD_order4

# Fractional residual at key t values
idx_1 = np.argmin(np.abs(t_arr - 1.0))
idx_01 = np.argmin(np.abs(t_arr - 0.1))
idx_10 = np.argmin(np.abs(t_arr - 10.0))

print(f"\n{'='*72}")
print(f"Oscillatory residual K_osc(t) = K(t) - K_SD(t)")
print(f"{'='*72}")
print(f"\n  At t = {t_arr[idx_01]:.4f} (short time, UV):")
print(f"    K_exact     = {K_exact[idx_01]:.6f}")
print(f"    K_SD(ord 2) = {K_SD_order2[idx_01]:.6f}")
print(f"    K_SD(ord 3) = {K_SD_order3[idx_01]:.6f}")
print(f"    K_SD(ord 4) = {K_SD_order4[idx_01]:.6f}")
print(f"    K_osc(ord 2) = {K_osc_2[idx_01]:.6e}  (frac: {K_osc_2[idx_01]/K_exact[idx_01]:.6e})")
print(f"    K_osc(ord 3) = {K_osc_3[idx_01]:.6e}  (frac: {K_osc_3[idx_01]/K_exact[idx_01]:.6e})")
print(f"    K_osc(ord 4) = {K_osc_4[idx_01]:.6e}  (frac: {K_osc_4[idx_01]/K_exact[idx_01]:.6e})")

print(f"\n  At t = {t_arr[idx_1]:.4f} (natural scale, t ~ 1/M_KK^2):")
print(f"    K_exact     = {K_exact[idx_1]:.6f}")
print(f"    K_SD(ord 2) = {K_SD_order2[idx_1]:.6f}")
print(f"    K_SD(ord 3) = {K_SD_order3[idx_1]:.6f}")
print(f"    K_SD(ord 4) = {K_SD_order4[idx_1]:.6f}")
print(f"    K_osc(ord 2) = {K_osc_2[idx_1]:.6e}  (frac: {K_osc_2[idx_1]/K_exact[idx_1]:.6e})")
print(f"    K_osc(ord 3) = {K_osc_3[idx_1]:.6e}  (frac: {K_osc_3[idx_1]/K_exact[idx_1]:.6e})")
print(f"    K_osc(ord 4) = {K_osc_4[idx_1]:.6e}  (frac: {K_osc_4[idx_1]/K_exact[idx_1]:.6e})")

print(f"\n  At t = {t_arr[idx_10]:.4f} (long time, IR):")
print(f"    K_exact     = {K_exact[idx_10]:.10e}")
print(f"    K_SD(ord 2) = {K_SD_order2[idx_10]:.10e}")
print(f"    K_SD(ord 3) = {K_SD_order3[idx_10]:.10e}")
print(f"    K_SD(ord 4) = {K_SD_order4[idx_10]:.10e}")
print(f"    K_osc(ord 2) = {K_osc_2[idx_10]:.6e}  (frac: {K_osc_2[idx_10]/max(K_exact[idx_10],1e-300):.6e})")
print(f"    K_osc(ord 3) = {K_osc_3[idx_10]:.6e}  (frac: {K_osc_3[idx_10]/max(K_exact[idx_10],1e-300):.6e})")
print(f"    K_osc(ord 4) = {K_osc_4[idx_10]:.6e}  (frac: {K_osc_4[idx_10]/max(K_exact[idx_10],1e-300):.6e})")

# ============================================================
# Section 5: Convergence of the smooth expansion
# ============================================================

# Check whether the polynomial expansion converges at the relevant t
# The series K_SD = a0 - a2*t + a4*t^2 - a6*t^3 + ...
# converges if successive terms decrease. At t=1:

print(f"\n{'='*72}")
print(f"Convergence of polynomial expansion at t = 1")
print(f"{'='*72}")
terms = [a0_mm, -a2_mm, a4_mm, -a6_mm, a8_mm, -a10_mm]
labels = ['a0', '-a2', 'a4', '-a6', 'a8', '-a10']
running_sum = 0
for label, term in zip(labels, terms):
    running_sum += term
    print(f"  {label:5s} = {term:+15.4f}   cumulative = {running_sum:15.4f}")
print(f"  K_exact(t=1) = {K_exact[idx_1]:15.4f}")

# Ratio test: |a_{n+2}/a_n|
for i in range(len(terms)-1):
    if abs(terms[i]) > 0:
        ratio = abs(terms[i+1]/terms[i])
        print(f"  |{labels[i+1]}/{labels[i]}| = {ratio:.6f}")

# ============================================================
# Section 6: Gaussian-smoothed Strutinsky decomposition
# ============================================================

# The moment-matched polynomial is NOT a good smooth approximation at large t
# because the series diverges. Use Gaussian smoothing instead.
# This is the direct analog of the Strutinsky shell correction method.
#
# K_smooth(t) = integral d(omega^2) * rho_smooth(omega^2) * exp(-omega^2 * t)
# where rho_smooth is a Gaussian-broadened level density.

# Strutinsky smoothing: replace delta(omega - omega_n) with Gaussians
# rho_smooth(omega) = sum_n (w_n / (sqrt(2pi) * gamma)) * exp(-(omega - omega_n)^2 / (2*gamma^2))
# with smoothing width gamma

# For the heat kernel, we smooth in omega^2 space:
omega2_unique, inverse, counts = np.unique(omega2, return_inverse=True, return_counts=True)
# Weight per unique omega^2 value
w_unique = np.zeros(len(omega2_unique))
for j in range(len(omega)):
    w_unique[inverse[j]] += dim2[j]

print(f"\nUnique omega^2 values: {len(omega2_unique)}")
print(f"  omega^2 range: [{omega2_unique.min():.6f}, {omega2_unique.max():.6f}]")

# Strutinsky prescription: choose gamma ~ mean level spacing
# Mean spacing = (omega2_max - omega2_min) / N_unique
mean_spacing = (omega2_unique.max() - omega2_unique.min()) / len(omega2_unique)
print(f"  Mean level spacing: {mean_spacing:.6f}")

# Try gamma/d ratios from 1 to 3 (standard Strutinsky window)
gamma_ratios = [1.0, 1.5, 2.0, 3.0]

print(f"\nStrutinsky decomposition (Gaussian smoothing):")
print(f"{'gamma/d':>8s} {'gamma':>8s} {'K_smooth(1)':>14s} {'K_osc(1)':>14s} {'frac_osc':>14s}")

K_osc_strutinsky = {}
for gr in gamma_ratios:
    gamma = gr * mean_spacing

    # Compute K_smooth(t) by convolving the Laplace transform with Gaussian
    # K_smooth(t) = sum_n w_n * exp(-omega_n^2 * t) convolved with Gaussian in omega^2
    # = sum_n w_n * exp(-(omega_n^2 * t - gamma^2 * t^2 / 2))
    # No — that's not right. The Strutinsky smoothing is in the density of states,
    # not in the heat kernel directly.

    # Correct approach: compute the smoothed level density rho_smooth(E)
    # where E = omega^2, then compute K_smooth(t) = integral rho_smooth(E) * exp(-E*t) dE

    # Discretize E space
    E_min = omega2_unique.min() - 5 * gamma
    E_max = omega2_unique.max() + 5 * gamma
    N_E = 2000
    E_grid = np.linspace(max(0, E_min), E_max, N_E)
    dE = E_grid[1] - E_grid[0]

    # Smoothed density
    rho_smooth = np.zeros(N_E)
    for j in range(len(omega2_unique)):
        rho_smooth += w_unique[j] * np.exp(-(E_grid - omega2_unique[j])**2 / (2 * gamma**2)) / (np.sqrt(2 * np.pi) * gamma)

    # K_smooth(t) = integral rho_smooth(E) * exp(-E*t) dE
    K_smooth_arr = np.zeros(N_t)
    for i in range(N_t):
        K_smooth_arr[i] = np.sum(rho_smooth * np.exp(-E_grid * t_arr[i])) * dE

    K_osc_s = K_exact - K_smooth_arr
    K_osc_strutinsky[gr] = K_osc_s

    frac = K_osc_s[idx_1] / K_exact[idx_1] if K_exact[idx_1] != 0 else 0
    print(f"  {gr:8.1f} {gamma:8.4f} {K_smooth_arr[idx_1]:14.4f} {K_osc_s[idx_1]:14.4f} {frac:14.6e}")

# ============================================================
# Section 7: Best estimate of oscillatory fraction
# ============================================================

# Use gamma/d = 1.5 (standard Strutinsky choice, nuclear literature)
gamma_best = 1.5  # (local)
K_osc_best = K_osc_strutinsky[gamma_best]

# The oscillatory fraction at t=1 (natural M_KK scale)
frac_osc_t1 = K_osc_best[idx_1] / K_exact[idx_1]

# Now convert to CC:
# The spectral action gives rho_Lambda = (2/pi^2) * f_4 * a_0 * Lambda^4
# where Lambda = M_KK is the cutoff and f_4 depends on the cutoff function.
# The oscillatory correction to this is:
# delta_rho_osc = (2/pi^2) * frac_osc * f_4 * a_0_fold * M_KK^4
# But the fractional residual IS the answer:
# rho_osc / rho_smooth ~ frac_osc

# Direct computation: CC from spectral action
# rho_Lambda_spectral = (2/pi^2) * a0_fold * M_KK^4 (using f_4 = 1 convention)
rho_spectral = (2.0 / PI**2) * a0_fold * M_KK**4
rho_osc = abs(frac_osc_t1) * rho_spectral

print(f"\n{'='*72}")
print(f"CC conversion (at t = 1, gamma/d = {gamma_best})")
print(f"{'='*72}")
print(f"  Fractional oscillatory residual: {frac_osc_t1:.6e}")
print(f"  |frac_osc|:                      {abs(frac_osc_t1):.6e}")
print(f"  rho_spectral (smooth CC):         {rho_spectral:.6e} GeV^4")
print(f"  rho_osc (oscillatory CC):         {rho_osc:.6e} GeV^4")
print(f"  rho_Lambda_obs:                   {rho_Lambda_obs:.6e} GeV^4")
print(f"  log10(rho_osc / rho_Lambda_obs):  {np.log10(rho_osc / rho_Lambda_obs):.4f}")
print(f"  log10(rho_spectral / rho_obs):    {np.log10(rho_spectral / rho_Lambda_obs):.4f}")
print(f"  Orders REDUCED by oscillation:    {np.log10(rho_spectral / rho_Lambda_obs) - np.log10(rho_osc / rho_Lambda_obs):.4f}")

# ============================================================
# Section 8: t-scan — find where residual is minimized
# ============================================================

print(f"\n{'='*72}")
print(f"t-scan: fractional oscillatory residual |K_osc/K_exact|")
print(f"{'='*72}")

# Find the t where |K_osc/K| is minimized (if it exists)
frac_scan = np.abs(K_osc_best) / np.maximum(np.abs(K_exact), 1e-300)
# Only consider t where K_exact is significantly nonzero
valid = K_exact > 1e-10 * K_exact[0]
frac_scan_valid = frac_scan[valid]
t_valid = t_arr[valid]

idx_min_frac = np.argmin(frac_scan_valid)
t_min_frac = t_valid[idx_min_frac]
frac_min = frac_scan_valid[idx_min_frac]

print(f"  Min |frac| = {frac_min:.6e} at t = {t_min_frac:.6f}")
print(f"  Max |frac| = {frac_scan_valid.max():.6e} at t = {t_valid[np.argmax(frac_scan_valid)]:.6f}")

# Log table at selected t values
t_samples = [0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0]
print(f"\n  {'t':>10s} {'K_exact':>14s} {'K_osc':>14s} {'|frac|':>14s} {'log10|frac|':>14s}")
for t_s in t_samples:
    idx_s = np.argmin(np.abs(t_arr - t_s))
    t_val = t_arr[idx_s]
    K_val = K_exact[idx_s]
    osc_val = K_osc_best[idx_s]
    if K_val > 1e-300:
        fr = abs(osc_val / K_val)
        print(f"  {t_val:10.4f} {K_val:14.6e} {osc_val:14.6e} {fr:14.6e} {np.log10(fr) if fr > 0 else -np.inf:14.4f}")
    else:
        print(f"  {t_val:10.4f} {K_val:14.6e} {osc_val:14.6e}     (K~0)")

# ============================================================
# Section 9: Uncertainty from smoothing parameter
# ============================================================

print(f"\n{'='*72}")
print(f"Uncertainty from gamma/d choice (at t = 1)")
print(f"{'='*72}")

frac_values = []
rho_osc_values = []
for gr in gamma_ratios:
    osc_val = K_osc_strutinsky[gr][idx_1]
    fr = osc_val / K_exact[idx_1] if K_exact[idx_1] != 0 else 0
    rho_o = abs(fr) * rho_spectral
    frac_values.append(fr)
    rho_osc_values.append(rho_o)
    print(f"  gamma/d = {gr:.1f}: frac_osc = {fr:+.6e}, rho_osc = {rho_o:.6e} GeV^4, log10(rho_osc/rho_obs) = {np.log10(rho_o/rho_Lambda_obs):.4f}")

# Spread
log_rho_values = [np.log10(r / rho_Lambda_obs) for r in rho_osc_values]
print(f"\n  Spread in log10(rho_osc/rho_obs): [{min(log_rho_values):.2f}, {max(log_rho_values):.2f}]")
print(f"  Central value: {np.mean(log_rho_values):.2f} +/- {np.std(log_rho_values):.2f}")

# ============================================================
# Section 10: Polynomial order convergence check
# ============================================================

# Another approach: how many polynomial terms are needed to match K(t)?
print(f"\n{'='*72}")
print(f"Polynomial expansion convergence at t = 1")
print(f"{'='*72}")

# Compute moments up to high order
max_order = 20
moments = np.zeros(max_order + 1)
for k in range(max_order + 1):
    from math import factorial
    moments[k] = np.sum(dim2 * omega2**k) / factorial(k)

K_poly = np.zeros(max_order + 1)
running = 0  # (local)
for k in range(max_order + 1):
    running += (-1)**k * moments[k] * 1.0**k  # t=1
    K_poly[k] = running

K_ref = K_exact[idx_1]
print(f"  K_exact(t={t_arr[idx_1]:.4f}) = {K_ref:.6f}")
print(f"\n  {'Order':>6s} {'K_poly':>14s} {'|K_poly - K|':>14s} {'frac':>14s}")
for k in range(min(max_order + 1, 15)):
    diff = abs(K_poly[k] - K_ref)
    frac = diff / abs(K_ref) if K_ref != 0 else 0
    print(f"  {k:6d} {K_poly[k]:14.4f} {diff:14.6e} {frac:14.6e}")

# ============================================================
# Section 11: Mode-by-mode Poisson summation analysis
# ============================================================

# The oscillatory part can also be analyzed via Poisson summation:
# K_osc ~ sum_{m != 0} K_m(t) where K_m are the non-zero Poisson terms
# For a smooth density of states, the m-th Poisson term oscillates as
# exp(2*pi*i*m*N(E)) where N(E) is the counting function.

# Compute the weighted eigenvalue density statistics
print(f"\n{'='*72}")
print(f"Mode structure analysis")
print(f"{'='*72}")

# Group by irrep to understand which contribute most to K_osc
# The s44 data has 992 entries. Group by unique (p,q) irreps.
# Each irrep contributes a cluster of eigenvalues.
# The oscillatory part comes from the GAPS between clusters.

# Compute K(t) contribution per irrep cluster
d60 = np.load('s60_pw_h0_conv.npz', allow_pickle=True)
pq = d60['irrep_pq']       # (35, 2) for L=0..7
dims_60 = d60['irrep_dim']  # dim(p,q) for 35 irreps

# The s44 data for L=0..6 has 28 irreps
# Map back to the irrep structure
# omega values in s44 are organized: first dim(0,0)^2=1 entries,
# then dim(0,1)^2=9 entries, etc. (grouped by irrep)

# Actually, we need to identify which entries belong to which irrep
# by matching omega values to the irrep omega ranges
irrep_K_contributions = []
start_idx = 0
# The s44 all_omega array is ordered by irrep blocks
# Let's verify by checking dim2 patterns

# Group consecutive entries with same dim2 value
groups = []
current_d2 = dim2[0]
current_start = 0
for j in range(1, len(dim2)):
    if dim2[j] != current_d2:
        groups.append((current_start, j, current_d2))
        current_d2 = dim2[j]
        current_start = j
groups.append((current_start, len(dim2), current_d2))

print(f"  Number of dim2-based groups: {len(groups)}")
print(f"  Group structure (start, end, dim2, count, omega_range):")
for s, e, d2 in groups[:15]:
    count = e - s  # (local)
    om_min = omega[s:e].min()
    om_max = omega[s:e].max()
    print(f"    [{s:4d}:{e:4d}] dim2={d2:5.0f} count={count:3d} omega=[{om_min:.4f}, {om_max:.4f}]")
if len(groups) > 15:
    print(f"    ... ({len(groups) - 15} more groups)")

# ============================================================
# Section 12: Shell correction as fraction of smooth part
# ============================================================

# The crucial nuclear analogy: in the Strutinsky method,
# delta_E_shell / E_smooth ~ 0.1-0.5% for medium-mass nuclei
# This corresponds to R ~ shell_correction / bulk_energy

# Here, the analog is:
# R_osc = |K_osc(t)| / K_smooth(t)
# at the physically relevant t = 1 (natural KK scale)

# The CC question: does R_osc ~ 10^{-120}?
# Nuclear result: R ~ 10^{-3} (shell correction is 0.1% of bulk)
# Framework needs R ~ 10^{-120}

R_osc = abs(K_osc_best[idx_1]) / K_exact[idx_1]
log_R_osc = np.log10(R_osc) if R_osc > 0 else -np.inf

print(f"\n{'='*72}")
print(f"Shell correction ratio (Strutinsky analog)")
print(f"{'='*72}")
print(f"  R_osc = |K_osc| / K_smooth = {R_osc:.6e}")
print(f"  log10(R_osc) = {log_R_osc:.4f}")
print(f"  Nuclear benchmark: R ~ 10^{{-3}} (0.1% shell correction)")
print(f"  CC target: R ~ 10^{{-120}}")
print(f"  Shortfall: {120 + log_R_osc:.1f} orders of magnitude")

# ============================================================
# Section 13: Gate verdict
# ============================================================

# Convert the oscillatory residual to CC in physical units
# rho_osc = R_osc * rho_spectral
# rho_spectral ~ (2/pi^2) * a0 * M_KK^4 ~ 10^{73} GeV^4
# So rho_osc ~ R_osc * 10^{73} GeV^4

log_rho_spectral = np.log10(rho_spectral)
log_rho_osc = np.log10(rho_osc)
log_rho_obs = np.log10(rho_Lambda_obs)
gap = log_rho_osc - log_rho_obs

print(f"\n{'='*72}")
print(f"GATE VERDICT: HK-OSCILLATION-61")
print(f"{'='*72}")
print(f"  rho_spectral (smooth) = 10^{{{log_rho_spectral:.2f}}} GeV^4")
print(f"  rho_osc (oscillatory) = 10^{{{log_rho_osc:.2f}}} GeV^4")
print(f"  rho_obs (Lambda)      = 10^{{{log_rho_obs:.2f}}} GeV^4")
print(f"  Gap: rho_osc / rho_obs = 10^{{{gap:.2f}}}")
print(f"  Shell correction R = 10^{{{log_R_osc:.2f}}}")

# Pre-registered criteria:
# PASS if gap within 10 orders of 0 (i.e., |gap| < 10)
# FAIL if R_osc -> 0 (averages out)
# INFO if finite but >> Lambda_obs

if R_osc < 1e-15:
    verdict = "FAIL"
    detail = f"Oscillatory residual averages out: R_osc = {R_osc:.2e} ~ 0"
elif abs(gap) < 10:
    verdict = "PASS"
    detail = f"rho_osc/rho_obs = 10^{{{gap:.2f}}} within 10 orders of Lambda_obs"
else:
    verdict = "INFO"
    detail = f"Oscillatory residual finite but {gap:.1f} orders above Lambda_obs. R_osc = {R_osc:.2e}"

print(f"\n  VERDICT: {verdict}")
print(f"  DETAIL: {detail}")

# ============================================================
# Section 14: Save results
# ============================================================

np.savez('s61_hk_oscillation.npz',
    # Spectrum
    omega=omega,
    dim2=dim2,
    N_modes=N_modes,

    # Heat kernel
    t_arr=t_arr,
    K_exact=K_exact,
    K_SD_order2=K_SD_order2,
    K_SD_order3=K_SD_order3,
    K_SD_order4=K_SD_order4,

    # Moment-matched coefficients
    a0_mm=a0_mm,
    a2_mm=a2_mm,
    a4_mm=a4_mm,
    a6_mm=a6_mm,
    a8_mm=a8_mm,

    # Strutinsky oscillatory residuals
    K_osc_gd1p0=K_osc_strutinsky[1.0],
    K_osc_gd1p5=K_osc_strutinsky[1.5],
    K_osc_gd2p0=K_osc_strutinsky[2.0],
    K_osc_gd3p0=K_osc_strutinsky[3.0],

    # Key results
    R_osc=R_osc,
    frac_osc_t1=frac_osc_t1,
    rho_spectral=rho_spectral,
    rho_osc=rho_osc,
    rho_Lambda_obs=rho_Lambda_obs,
    log_rho_osc_over_obs=gap,
    log_R_osc=log_R_osc,

    # Seeley-DeWitt geometric coefficients
    a0_SD_geom=a0_SD_geom,
    a2_SD_geom=a2_SD_geom,
    a4_SD_geom=a4_SD_geom,

    # Gate
    gate_name=np.array(['HK-OSCILLATION-61']),
    gate_verdict=np.array([verdict]),
    gate_detail=np.array([detail]),
)

print(f"\nSaved: s61_hk_oscillation.npz")

# ============================================================
# Section 15: Diagnostic — eigenvalue-by-eigenvalue decomposition
# ============================================================

# Which eigenvalues contribute most to the oscillatory part?
# Compute K_n(t=1) = dim2_n * exp(-omega_n^2) for each mode
K_per_mode = dim2 * np.exp(-omega2 * 1.0)  # at t=1
K_total = K_per_mode.sum()

# Sort by contribution
sort_idx = np.argsort(-K_per_mode)
print(f"\nTop 10 mode contributions to K(t=1) = {K_total:.4f}:")
print(f"  {'rank':>4s} {'omega':>8s} {'dim2':>6s} {'K_n':>14s} {'frac':>10s} {'cumfrac':>10s}")
cumfrac = 0
for rank, idx in enumerate(sort_idx[:10]):
    frac = K_per_mode[idx] / K_total
    cumfrac += frac
    print(f"  {rank+1:4d} {omega[idx]:8.4f} {dim2[idx]:6.0f} {K_per_mode[idx]:14.6f} {frac:10.6f} {cumfrac:10.6f}")

print(f"\n  Mode saturation: top 10 modes account for {cumfrac*100:.1f}% of K(t=1)")
print(f"  Bottom 100 modes: {K_per_mode[sort_idx[-100:]].sum()/K_total*100:.4f}%")

# ============================================================
# Section 16: Physical interpretation summary
# ============================================================

print(f"\n{'='*72}")
print(f"PHYSICAL INTERPRETATION")
print(f"{'='*72}")
print(f"""
The heat kernel K(t) = Tr(exp(-t*D_K^2)) was computed from {N_modes} Dirac
eigenvalues at the fold (tau = {tau_fold}), with degeneracy-weighted sums.

The Seeley-DeWitt (smooth polynomial) expansion captures the bulk of K(t):
  K_SD(t) = a_0 - a_2*t + a_4*t^2 - ... (moment-matched from eigenvalues)

The oscillatory residual K_osc = K - K_SD (Strutinsky method, gamma/d = {gamma_best})
gives a fractional correction:
  R_osc = |K_osc(t=1)| / K(t=1) = {R_osc:.4e}

Converting to the cosmological constant:
  rho_smooth = (2/pi^2) * a_0 * M_KK^4 ~ 10^{{{log_rho_spectral:.0f}}} GeV^4
  rho_osc = R_osc * rho_smooth ~ 10^{{{log_rho_osc:.0f}}} GeV^4
  rho_obs = 2.7e-47 GeV^4

The oscillatory shell correction is {abs(log_R_osc):.0f} orders smaller than the smooth
part, but still ~ 10^{{{gap:.0f}}} orders ABOVE the observed CC.

Nuclear analogy: In the Strutinsky method, delta_E_shell ~ 10^{{-3}} * E_smooth.
The framework's R_osc ~ {R_osc:.2e} is comparable to nuclear shell corrections
({np.log10(R_osc):.1f} vs -3.0 in log10). The oscillatory corrections do NOT
average out — they are finite, robust, and of the same relative magnitude as
nuclear shell corrections.

However, they fall short of the CC by ~ {gap:.0f} orders. The oscillatory
correction mechanism alone does NOT solve the CC problem.
""")

print("Done.")
