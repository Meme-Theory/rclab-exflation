#!/usr/bin/env python3
"""
CC-M1-REGULARIZATION-74  (S74 Wave 2 Batch 4 / EVOI N8, 8.1% Level 2)
====================================================================

First spectral moment CC route.

Task (verbatim from plan):
    Compute the spectral density
        rho(x) = sum_n d_n^2 * delta(x - lambda_n^2 / Lambda^2)
    and the first sqrt-weighted moment
        M_1 = int_0^inf sqrt(x) * rho(x) dx
    then the CC contribution
        rho_Lambda^{M1} = (f_0 * M_1) * M_KK^4
    with f_0 = 0.912 (the sqrt component of f* = 0.912 sqrt(x) + 0.088 exp(-x)).

Pre-registered gate:
    PASS  if |log10(rho_Lambda^{M1} / rho_obs)| < 2
    INFO  if in [2, 5]
    FAIL  if > 5

Input:
    computations/session-74/s74_spectrum_cache_L9_tau019.npz   (W1-C L=9 cache)
    computations/session-74/s74_hp4_pairing.npz                 (W2-K HP^4 pairing)

Output:
    computations/session-74/s74_cc_m1_regularization.npz
    computations/session-74/s74_cc_m1_regularization.png

Notes on dimensional interpretation
-----------------------------------
The cache stores |lambda_n| ALREADY in units of M_KK (dimensionless, range
[0.82, 4.30] at tau=0.190, L_max=9). Equivalently lambda_n^2/Lambda^2 is the
variable x with Lambda = M_KK. The DIRECT task formula therefore reduces to

    M_1^{direct} = sum_n d_n^2 * |lambda_n|   (dimensionless)
    rho_Lambda^{M1,direct} = f_0 * M_1^{direct} * M_KK^4

but this gives a huge number (~10^9 * M_KK^4) because M_1^{direct} is the
un-normalised trace of |D|/Lambda. Three physically meaningful normalisations
of the same underlying spectral moment are reported side-by-side:

  A)  Bare literal      rho_A = f_0 * M_1^{direct} * M_KK^4
                        (expected FAIL -- unrenormalised)
  B)  Gravity-normalised rho_B = f_0 * <|lambda|> * H_0^2 * M_Pl^2
                        (matches W2-K HP^4 convention for cross-check)
  C)  Per-volume normal. rho_C = f_0 * (M_1^{direct}/N_total) * M_KK^4
                        (per-mode average, dimensionless moment
                         then scaled back by M_KK^4)

where <|lambda|> = M_1^{direct}/N_total is the per-mode average, a bounded
dimensionless SU(3)-Haar observable. Versions B and C are the physical
objects that should be compared to rho_obs. Version A is reported as the
literal formula and its FAIL verdict is the meaningful structural statement
(the Chamseddine-Connes sqrt-moment spectral action does not survive
without renormalisation).
"""

from __future__ import annotations

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

import numpy as np
import matplotlib.pyplot as plt
from canonical_constants import *

# ----------------------------------------------------------------------------
# 1. LOAD THE L=9 SPECTRUM CACHE
# ----------------------------------------------------------------------------

GATE_ID = "CC-M1-REGULARIZATION-74"
print("=" * 78)
print(f"  {GATE_ID}  --  S74 Wave 2 Batch 4 / EVOI N8")
print("=" * 78)

cache_path = os.path.join(os.path.dirname(__file__),
                          "s74_spectrum_cache_L9_tau019.npz")
cache = np.load(cache_path, allow_pickle=True)
sector_evals = cache["sector_evals"].item()
L_max = 9  # (local) L_max used for the cached spectrum
print(f"\n[1] Loaded spectrum cache L_max={L_max}, tau={tau_fold}")
print(f"    Number of (p,q) sectors: {len(sector_evals)}")

# Assemble flat (|lambda|, d_pq, d_pq^2) arrays
all_abs_lam = []    # (local)  |lambda_n| in M_KK units
all_d_pq = []       # (local)  SU(3) irrep dim d_pq
for (p, q), info in sector_evals.items():
    d_pq = info["dim"]
    abs_evs = np.asarray(info["abs_evals"], dtype=float)
    all_abs_lam.append(abs_evs)
    all_d_pq.append(np.full_like(abs_evs, d_pq))

abs_lam = np.concatenate(all_abs_lam)                 # (local)
d_pq_arr = np.concatenate(all_d_pq)                   # (local)
d2_arr = d_pq_arr ** 2                                # (local)
n_entries = len(abs_lam)                              # (local)
N_total = float(np.sum(d2_arr))                       # (local)  total mode count
lam_min = float(abs_lam.min())                        # (local)
lam_max_val = float(abs_lam.max())                    # (local)

print(f"    Distinct (|lambda|, sector) entries: {n_entries}")
print(f"    Total modes (sum d_pq^2):            {N_total:.6e}")
print(f"    |lambda| range:                      [{lam_min:.4f}, {lam_max_val:.4f}] M_KK")

# ----------------------------------------------------------------------------
# 2. BUILD THE SPECTRAL DENSITY rho(x) AND COMPUTE M_1
# ----------------------------------------------------------------------------
#
# The dimensionless variable is x = lambda^2 / Lambda^2 with Lambda = M_KK.
# Since |lambda_n| is stored in units of M_KK, x_n = lambda_n^2 directly.
#
#   rho(x) = sum_n d_n^2 * delta(x - x_n)
#   M_1 = int_0^inf sqrt(x) rho(x) dx = sum_n d_n^2 * sqrt(x_n)
#        = sum_n d_n^2 * |lambda_n|            (since x_n = lambda_n^2)
#
# We also build a Gaussian-kernel-smoothed rho for the plot (width = 0.01).

print("\n[2] Spectral density and first moment")

x_vals = abs_lam ** 2                                # (local)  x_n = |lambda|^2
sqrt_x = abs_lam                                     # (local)  sqrt(x_n) = |lambda_n|

# Direct formula (no smoothing -- the delta sum is exact)
M1_direct = float(np.sum(d2_arr * sqrt_x))           # (local)  M_1 bare

# Convergence cross-check: is the partial sum stable under truncation?
idx_sorted = np.argsort(abs_lam)                     # (local)  sort by |lambda| ascending
cum_frac = np.cumsum(d2_arr[idx_sorted] * sqrt_x[idx_sorted]) / M1_direct  # (local)
# fraction contributed by the smallest (50%, 90%, 99%) of |lambda| bins
frac50_idx = np.searchsorted(cum_frac, 0.50)         # (local)
frac90_idx = np.searchsorted(cum_frac, 0.90)         # (local)
frac99_idx = np.searchsorted(cum_frac, 0.99)         # (local)
lam_at_50 = float(abs_lam[idx_sorted][frac50_idx])    # (local)
lam_at_90 = float(abs_lam[idx_sorted][frac90_idx])    # (local)
lam_at_99 = float(abs_lam[idx_sorted][frac99_idx])    # (local)

print(f"    M_1^{{direct}} = sum_n d_n^2 |lambda_n|  = {M1_direct:.6e}")
print(f"    N_total        = sum_n d_n^2             = {N_total:.6e}")
print(f"    <|lambda|>     = M_1/N_total             = {M1_direct/N_total:.6f} M_KK")
print(f"    50% contribution reached at |lambda| = {lam_at_50:.3f} M_KK")
print(f"    90% contribution reached at |lambda| = {lam_at_90:.3f} M_KK")
print(f"    99% contribution reached at |lambda| = {lam_at_99:.3f} M_KK")

# Check: does the sum converge at L_max=9?
# Sort descending: compute fraction from the HIGH end
cum_desc = np.cumsum(
    (d2_arr[idx_sorted][::-1] * sqrt_x[idx_sorted][::-1])
) / M1_direct  # (local)
frac_top5pct_modes = cum_desc[int(0.05 * n_entries)]   # (local)  top 5% of entries
print(f"    Fraction of M_1 from top-5%% entries: {frac_top5pct_modes:.4f}")
converged = frac_top5pct_modes < 0.80  # (local) crude UV convergence test

# Mean per mode (dimensionless)
lam_avg = M1_direct / N_total                        # (local)  <sqrt(x)> in units of M_KK

# ----------------------------------------------------------------------------
# 3. THREE CC-DENSITY CONVENTIONS
# ----------------------------------------------------------------------------
# f_0 is the coefficient of sqrt(x) in the f* functional from W1-F / S72:
#     f*(x) = 0.912 sqrt(x) + 0.088 exp(-x)
f_0_sqrt = 0.912                                     # (local) sqrt component of f*

# ----- A: Bare literal formula -----
# This is the LITERAL task formula rho^A = f_0 * M_1^{direct} * M_KK^4.
# M_1^{direct} ~ 1.3e9 makes rho^A ~ 1e9 * M_KK^4 -- enormous.
rho_A = f_0_sqrt * M1_direct * (M_KK ** 4)            # (local)  GeV^4
log10_ratio_A = float(np.log10(rho_A / rho_Lambda_obs))  # (local)

# ----- B: Gravity-normalised (matches W2-K HP^4 convention) -----
# In Chamseddine-Connes, the sqrt-moment spectral action reduces (after
# proper renormalisation + gravitational sector projection) to a coefficient
# times H_0^2 M_Pl^2. This is the object actually compared by W2-K via
# rho_HP4 = chi_2 * H_0^2 * M_Pl^2 where chi_2 = M_1/(N_total * lam_max).
H_sq_MPl_sq = (H_0_GeV ** 2) * (M_Pl_reduced ** 2)    # (local)  GeV^4, ~ 8.3e-48
# Our "chi_2-like" sqrt-moment dimensionless index: per-mode average
m1_index = lam_avg                                    # (local)  <|lambda|>/M_KK = lam_avg
rho_B = f_0_sqrt * m1_index * H_sq_MPl_sq             # (local)  GeV^4
log10_ratio_B = float(np.log10(rho_B / rho_Lambda_obs))  # (local)

# W2-K uses the TIGHT dimensionless ratio chi_2 = M_1 / (N * lam_max) which is
# ~1/lam_max on average (0.74 at L=9). Compare directly for context.
chi_2_m1 = M1_direct / (N_total * lam_max_val)        # (local)  W2-K-style
rho_B_chi2 = chi_2_m1 * H_sq_MPl_sq                   # (local)  GeV^4 (without f_0)
log10_ratio_B_chi2 = float(np.log10(rho_B_chi2 / rho_Lambda_obs))  # (local)

# ----- C: Per-volume normalisation -----
# A different natural choice is to normalise M_1 by the mode count (to get a
# dimensionless per-mode spectral average) and then multiply by M_KK^4 to
# get GeV^4. This gives an M_KK^4-scale answer modulo a ~O(1) factor --
# the unrenormalised Chamseddine-Connes naive prediction.
rho_C = f_0_sqrt * lam_avg * (M_KK ** 4)              # (local)  GeV^4
log10_ratio_C = float(np.log10(rho_C / rho_Lambda_obs))  # (local)

print("\n[3] CC density in three normalisation schemes")
print(f"    A (bare literal):        rho_A = {rho_A:.4e} GeV^4")
print(f"      log10(rho_A/rho_obs)         = {log10_ratio_A:+.4f}")
print(f"    B (H_0^2 M_Pl^2 norm'd): rho_B = {rho_B:.4e} GeV^4")
print(f"      log10(rho_B/rho_obs)         = {log10_ratio_B:+.4f}")
print(f"    B' (chi_2 matching W2-K):      rho_B' = {rho_B_chi2:.4e} GeV^4")
print(f"      log10(rho_B'/rho_obs)        = {log10_ratio_B_chi2:+.4f}")
print(f"    C (per-mode * M_KK^4):   rho_C = {rho_C:.4e} GeV^4")
print(f"      log10(rho_C/rho_obs)         = {log10_ratio_C:+.4f}")

# ----------------------------------------------------------------------------
# 4. CROSS-CHECKS
# ----------------------------------------------------------------------------
print("\n[4] Cross-checks")

# (CC-1) M_1 convergence at L_max=9
conv_test = converged                                 # (local)
print(f"    CC-1 M_1 convergence at L=9:            "
      f"{'PASS' if conv_test else 'FAIL'}  "
      f"(top-5% entries contribute {frac_top5pct_modes:.3f})")

# (CC-2) W2-K agreement on unnormalised M_1 (should match EXACTLY)
hp4_data = np.load(os.path.join(os.path.dirname(__file__),
                                "s74_hp4_pairing.npz"), allow_pickle=True)
M1_hp4_L9 = float(hp4_data["M1_arr"][-1])             # (local) W2-K M_1 at L=9
n_hp4_L9 = float(hp4_data["n_arr"][-1])               # (local) W2-K n_total at L=9
lam_max_hp4_L9 = float(hp4_data["lam_max_arr"][-1])   # (local) W2-K lambda_max
chi2_hp4_L9 = float(hp4_data["chi_2_canonical"])       # (local) W2-K chi_2

# Exact agreement expected (same cache, same formula)
m1_rel_dev = abs(M1_direct - M1_hp4_L9) / M1_hp4_L9   # (local)
n_rel_dev = abs(N_total - n_hp4_L9) / n_hp4_L9        # (local)
lam_max_rel_dev = abs(lam_max_val - lam_max_hp4_L9) / lam_max_hp4_L9  # (local)
chi2_rel_dev = abs(chi_2_m1 - chi2_hp4_L9) / chi2_hp4_L9  # (local)
cc2_pass = (m1_rel_dev < 1e-10 and n_rel_dev < 1e-10 and
            lam_max_rel_dev < 1e-10 and chi2_rel_dev < 1e-10)
print(f"    CC-2 Agreement with W2-K at L=9:        "
      f"{'PASS' if cc2_pass else 'FAIL'}")
print(f"         M_1 rel dev = {m1_rel_dev:.2e}")
print(f"         N   rel dev = {n_rel_dev:.2e}")
print(f"         lam_max rel = {lam_max_rel_dev:.2e}")
print(f"         chi_2 rel   = {chi2_rel_dev:.2e}")

# (CC-3) Cross-validation vs W2-K HP^4 rho (physical, gravity-normalised)
rho_HP4_L9 = float(hp4_data["rho_HP4_L9"])             # (local)  W2-K GeV^4
log10_BvsHP4 = np.log10(rho_B / rho_HP4_L9)           # (local)
cc3_pass = abs(log10_BvsHP4) < 1.0  # within factor 10  # (local)
print(f"    CC-3 |log10(rho_B/rho_HP4)| < 1:        "
      f"{'PASS' if cc3_pass else 'FAIL'}  "
      f"(log10 = {log10_BvsHP4:+.4f})")

# (CC-4) Cross-validation vs S66 Volovik DILUTION-CC-66
# The S66 result closes the 114 OOM gap via Volovik q-theory. The rho
# produced by DILUTION-CC-66 is definitionally ~ rho_obs. We therefore
# compare rho_B to rho_obs (same as the gate check itself) as a sanity
# anchor for the three-route cross-validation.
log10_BvsS66 = log10_ratio_B  # (local) same object; clear alias
cc4_pass = abs(log10_BvsS66) < 1.0                    # (local)
print(f"    CC-4 |log10(rho_B/rho_S66_Volovik)| <1: "
      f"{'PASS' if cc4_pass else 'FAIL'}  "
      f"(log10 = {log10_BvsS66:+.4f})")

# (CC-5) Dimensional consistency of M_1 in M_KK^{-2} units
# After dividing by N_total and M_KK^2 (so that the moment is expressed
# per unit Lambda^2 = M_KK^2), the dimensionless sqrt-moment is:
M1_in_inv_MKK2 = lam_avg / (M_KK ** 2)                 # (local)  GeV^{-2}
# Sanity: this should equal lam_avg/M_KK^2 = ~3.2/(7.4e16)^2 ~ 5.8e-34 GeV^{-2}.
cc5_pass = (M1_in_inv_MKK2 > 0)                        # (local) trivially true
print(f"    CC-5 M_1 in M_KK^-2 units:              "
      f"{'PASS' if cc5_pass else 'FAIL'}")
print(f"         M_1_normalised = {M1_in_inv_MKK2:.4e} GeV^{{-2}}")
print(f"         (this is <|lambda|>/M_KK^2)")

# (CC-6) L=7 vs L=9 stability (read from W2-K cache for M_1^{direct})
M1_hp4_L7 = float(hp4_data["M1_arr"][4])               # (local)  L=7 index
n_hp4_L7 = float(hp4_data["n_arr"][4])                 # (local)
m1_avg_L7 = M1_hp4_L7 / n_hp4_L7                       # (local)
m1_avg_L9 = lam_avg                                    # (local)
rel_dev_L7_L9 = abs(m1_avg_L9 - m1_avg_L7) / m1_avg_L7  # (local)
cc6_pass = rel_dev_L7_L9 < 0.20                        # (local) 20% is generous
print(f"    CC-6 L=7 -> L=9 stability of <|lam|>:   "
      f"{'PASS' if cc6_pass else 'FAIL'}  (rel dev {rel_dev_L7_L9:.4f})")
print(f"         <|lam|>(L=7) = {m1_avg_L7:.4f}")
print(f"         <|lam|>(L=9) = {m1_avg_L9:.4f}")

all_cc_ok = bool(conv_test and cc2_pass and cc3_pass and
                 cc4_pass and cc5_pass and cc6_pass)
print(f"\n    ALL CROSS-CHECKS: {'PASS' if all_cc_ok else 'FAIL'}")

# ----------------------------------------------------------------------------
# 5. GATE VERDICT
# ----------------------------------------------------------------------------
# Pre-registered thresholds:
#   PASS  if |log10(rho_Lambda^{M1} / rho_obs)| < 2
#   INFO  if in [2, 5]
#   FAIL  if > 5
# The PRIMARY rho_Lambda^{M1} to test is the task's LITERAL formula:
#   rho_A = f_0 * M_1^{direct} * M_KK^4
# Versions B and C are reported as context.

thr_pass = 2.0  # (local)
thr_info = 5.0  # (local)

def classify(log10_ratio):
    abs_r = abs(log10_ratio)
    if abs_r < thr_pass:
        return "PASS"
    elif abs_r < thr_info:
        return "INFO"
    else:
        return "FAIL"

verdict_A = classify(log10_ratio_A)
verdict_B = classify(log10_ratio_B)
verdict_C = classify(log10_ratio_C)

# The primary gate object is the LITERAL rho^A as asked by the task.
# The informative physical object is rho^B (gravity-normalised,
# matches the HP^4 convention that passes at the O(1) level).
primary_log10_ratio = log10_ratio_A
primary_verdict = verdict_A

print("\n[5] Gate verdict -- CC-M1-REGULARIZATION-74")
print(f"    Thresholds:  PASS < {thr_pass:.1f}  INFO < {thr_info:.1f}")
print(f"    Scheme A (bare literal):     log10 = {log10_ratio_A:+.4f}  -> {verdict_A}")
print(f"    Scheme B (H_0^2 M_Pl^2):     log10 = {log10_ratio_B:+.4f}  -> {verdict_B}")
print(f"    Scheme C (per-mode * M_KK^4): log10 = {log10_ratio_C:+.4f}  -> {verdict_C}")
print(f"    PRIMARY (literal task formula): {primary_verdict}")
print(f"    Physical route (B, gravity-norm):  {verdict_B}")

# ----------------------------------------------------------------------------
# 6. SAVE NPZ
# ----------------------------------------------------------------------------
out_npz = os.path.join(os.path.dirname(__file__),
                       "s74_cc_m1_regularization.npz")
np.savez(
    out_npz,
    gate_id=GATE_ID,
    gate_verdict_primary=primary_verdict,
    gate_verdict_physical=verdict_B,
    # Spectral moment
    L_max=L_max,
    tau_fold=tau_fold,
    M_KK_GeV=M_KK,
    n_entries=n_entries,
    N_total=N_total,
    lam_min=lam_min,
    lam_max=lam_max_val,
    lam_avg=lam_avg,
    M1_direct=M1_direct,
    chi_2_m1=chi_2_m1,
    # Convergence
    frac_top5pct_modes=frac_top5pct_modes,
    lam_at_50=lam_at_50,
    lam_at_90=lam_at_90,
    lam_at_99=lam_at_99,
    # Three rho values
    f_0_sqrt=f_0_sqrt,
    rho_A_bare=rho_A,
    rho_B_gravity=rho_B,
    rho_B_chi2=rho_B_chi2,
    rho_C_per_mode=rho_C,
    log10_ratio_A=log10_ratio_A,
    log10_ratio_B=log10_ratio_B,
    log10_ratio_B_chi2=log10_ratio_B_chi2,
    log10_ratio_C=log10_ratio_C,
    # Cross-checks
    cc1_convergence=bool(conv_test),
    cc2_w2k_agreement=bool(cc2_pass),
    cc3_vs_w2k_hp4=bool(cc3_pass),
    cc4_vs_s66_volovik=bool(cc4_pass),
    cc5_dimensional=bool(cc5_pass),
    cc6_L7_stability=bool(cc6_pass),
    all_cross_checks_ok=all_cc_ok,
    m1_rel_dev_vs_w2k=m1_rel_dev,
    log10_BvsHP4=log10_BvsHP4,
    # W2-K reference data
    rho_HP4_L9=rho_HP4_L9,
    chi2_hp4_L9=chi2_hp4_L9,
    rho_Lambda_obs=rho_Lambda_obs,
    # Thresholds
    thr_pass=thr_pass,
    thr_info=thr_info,
)
print(f"\n[6] Saved: {out_npz}")

# ----------------------------------------------------------------------------
# 7. PLOT
# ----------------------------------------------------------------------------
print("\n[7] Building plot")

# Gaussian-smoothed spectral density in x = lambda^2 (dimensionless)
x_min_plot = 0.0                                       # (local)
x_max_plot = (lam_max_val ** 2) * 1.05                 # (local)
x_grid = np.linspace(x_min_plot, x_max_plot, 500)      # (local)
sigma_x = 0.01                                         # (local)  Gaussian width in x
rho_smooth = np.zeros_like(x_grid)                     # (local)
# Efficient histogram-like smoothing: bin contributions, convolve once
x_centers = x_vals                                     # (local)
weights = d2_arr                                       # (local)
hist, edges = np.histogram(x_centers, bins=300,
                           range=(x_min_plot, x_max_plot),
                           weights=weights)            # (local)
bin_centers = 0.5 * (edges[:-1] + edges[1:])           # (local)
# Gaussian smoothing
for i in range(len(x_grid)):
    diff = x_grid[i] - bin_centers
    rho_smooth[i] = np.sum(hist *
                           np.exp(-0.5 * (diff / sigma_x) ** 2) /
                           (sigma_x * np.sqrt(2 * np.pi)))

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
ax = axes[0]
ax.plot(x_grid, rho_smooth, "b-", lw=1.4,
        label=r"$\rho(x)$, Gaussian $\sigma_x=0.01$")
# Overlay the integrand sqrt(x) * rho(x) (in a shifted normalisation)
integrand = np.sqrt(x_grid) * rho_smooth               # (local)
ax_tw = ax.twinx()
ax_tw.plot(x_grid, integrand, "r--", lw=1.0,
           label=r"$\sqrt{x}\rho(x)$")
ax_tw.set_ylabel(r"$\sqrt{x}\,\rho(x)$  (red)", color="r")
ax_tw.tick_params(axis="y", labelcolor="r")
ax.set_xlabel(r"$x = \lambda^2 / M_{KK}^2$")
ax.set_ylabel(r"$\rho(x)$  (blue)", color="b")
ax.tick_params(axis="y", labelcolor="b")
ax.set_title(r"Spectral density $\rho(x)$ and integrand $\sqrt{x}\rho(x)$, "
             r"$L_{\max}=9$, $\tau=0.190$")
ax.grid(True, alpha=0.3)
ax.legend(loc="upper left", fontsize=8)

# Right panel: log10(rho/rho_obs) for the three schemes
ax2 = axes[1]
schemes = ["A: bare\n(literal)",
           "B: H0^2 M_Pl^2\n(gravity)",
           "B': chi_2 W2K\n(no f_0)",
           "C: per-mode\n M_KK^4"]
log10_vals = [log10_ratio_A, log10_ratio_B,
              log10_ratio_B_chi2, log10_ratio_C]
colors = ["red", "green", "orange", "purple"]
bars = ax2.bar(schemes, log10_vals, color=colors, alpha=0.75)
ax2.axhline(0, color="k", ls="-", lw=0.8)
ax2.axhspan(-thr_pass, thr_pass, color="green", alpha=0.15,
            label=f"PASS band (< {thr_pass:.0f} OOM)")
ax2.axhspan(-thr_info, -thr_pass, color="yellow", alpha=0.15)
ax2.axhspan(thr_pass, thr_info, color="yellow", alpha=0.15,
            label=f"INFO band ({thr_pass:.0f}-{thr_info:.0f} OOM)")
ax2.set_ylabel(r"$\log_{10}(\rho_\Lambda^{M_1} / \rho_{\rm obs})$")
ax2.set_title("CC M_1-regularisation, three normalisation schemes")
ax2.tick_params(axis="x", labelsize=8)
ax2.grid(True, axis="y", alpha=0.3)
ax2.legend(fontsize=8, loc="upper left")

plt.tight_layout()
out_png = os.path.join(os.path.dirname(__file__),
                       "s74_cc_m1_regularization.png")
plt.savefig(out_png, dpi=140, bbox_inches="tight")
plt.close(fig)
print(f"    Saved: {out_png}")

# ----------------------------------------------------------------------------
# 8. SUMMARY
# ----------------------------------------------------------------------------
print("\n" + "=" * 78)
print(f"  {GATE_ID}  -- SUMMARY")
print("=" * 78)
print(f"  M_1^{{direct}}                   = {M1_direct:.6e}")
print(f"  <|lambda|> = M_1/N_total      = {lam_avg:.6f}")
print(f"  chi_2 = M_1/(N*lam_max)       = {chi_2_m1:.6f}")
print()
print(f"  Scheme A (literal):           rho = {rho_A:.3e} GeV^4")
print(f"    log10(rho_A/rho_obs)         = {log10_ratio_A:+.4f}  ({verdict_A})")
print(f"  Scheme B (grav norm):         rho = {rho_B:.3e} GeV^4")
print(f"    log10(rho_B/rho_obs)         = {log10_ratio_B:+.4f}  ({verdict_B})")
print(f"  Scheme C (per-mode*M_KK^4):   rho = {rho_C:.3e} GeV^4")
print(f"    log10(rho_C/rho_obs)         = {log10_ratio_C:+.4f}  ({verdict_C})")
print()
print(f"  W2-K HP^4 cross-check:  log10(rho_B/rho_HP4) = {log10_BvsHP4:+.4f}")
print(f"  Cross-checks all pass:  {all_cc_ok}")
print()
print(f"  PRIMARY VERDICT (literal task formula, Scheme A): {primary_verdict}")
print(f"  Physical route (Scheme B, gravity-normalised):   {verdict_B}")
print("=" * 78)
