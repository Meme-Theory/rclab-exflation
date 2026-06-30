#!/usr/bin/env python3
"""
s70_non_pert_sa.py -- NON-PERT-SA-70: Non-Perturbative Spectral Action
=======================================================================

Gate: NON-PERT-SA-70
  PASS: |S_exact - S_HK| / S_HK < 0.10 at Lambda = 2.048
  FAIL: |S_exact - S_HK| / S_HK > 0.50
  INFO: deviation in [0.10, 0.50] (marginal)

Physics:
--------
The spectral action is computed perturbatively via the heat kernel expansion:
  S ~ sum_k a_{2k} Lambda^{8-2k}    (for 8-dimensional SU(3))

At Lambda ~ M_KK (Lambda/M_KK = 1) or at the fold where Lambda_eff = 2.048
(swampland value from SWAMP-69), the asymptotic expansion may break down.

This computation tests convergence by comparing:
  S_exact(Lambda) = sum_n d_n f(lambda_n^2 / Lambda^2)
  S_HK(Lambda)    = truncated heat kernel series

for two spectral functions:
  (A) f(x) = exp(-x)   [heat kernel; S_HK well-defined]
  (B) f(x) = sqrt(x)   [framework choice; Mellin moments diverge]

For (A): both exact and HK are computable; the gate comparison uses this.
For (B): S_exact = (1/Lambda) sum d_n |lambda_n|; no clean HK expansion exists.

The comparison quantifies where the asymptotic expansion breaks down.

FUNCTIONAL SENSITIVITY:
  This is a FUNCTIONAL-DEPENDENT computation. The deviation depends on which
  f(x) is used. The heat kernel coefficients a_{2k} are structural (functional-
  independent), but the *accuracy* of the truncated expansion at finite Lambda
  depends on the spectral function f.

Author: Lizzi Spectral Functional Theorist
Session: S70
"""

import numpy as np
import sys
import os
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
os.chdir(SCRIPT_DIR)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    tau_fold, a0_fold, a2_fold, a4_fold,
    S_fold, M_KK, M_KK_gravity, M_KK_kerner,
    Vol_SU3_Haar, PI, g0_diag,
)

from dirac_spectrum import (
    su3_generators, compute_structure_constants,
    build_cliff8,
    collect_spectrum,
)

from spectral_action import (
    dim_su3_irrep, peter_weyl_degeneracy,
    extract_seeley_dewitt,
)

# ===========================================================================
# CONFIGURATION
# ===========================================================================
print("=" * 78)
print("NON-PERT-SA-70: Non-Perturbative Spectral Action at Lambda = 2.048")
print("=" * 78)

TAU = tau_fold  # 0.19
MAX_PQ_SUM = 6  # L_max = 6, ~28 sectors, ~11,000 eigenvalues (local)

# Lambda values in M_KK units (all eigenvalues are in M_KK units)
LAMBDA_VALUES = np.array([0.5, 1.0, 1.5, 2.0, 2.048, 3.0, 5.0, 10.0])
LAMBDA_SWAMP = 2.048  # From SWAMP-69  # (local)

# Gate thresholds
GATE_PASS = 0.10  # (local)
GATE_FAIL = 0.50  # (local)

# Gilkey discrepancy threshold for a_4^eff check
RATIO_GILKEY = 0.149  # 14.9% from prior alpha_s tension  # (local)

print(f"""
  Configuration:
    tau_fold        = {TAU}
    max_pq_sum      = {MAX_PQ_SUM} (L_max = 6)
    Lambda values   = {LAMBDA_VALUES}
    Lambda_swamp    = {LAMBDA_SWAMP}
    Gate threshold  = PASS < {GATE_PASS}, FAIL > {GATE_FAIL}
""")

# ===========================================================================
# STEP 1: COMPUTE EIGENVALUE SPECTRUM
# ===========================================================================
print("=" * 78)
print("STEP 1: Eigenvalue Spectrum at tau = {:.3f}, max_pq_sum = {}".format(TAU, MAX_PQ_SUM))
print("=" * 78)

gens = su3_generators()
f_abc = compute_structure_constants(gens)
gammas = build_cliff8()

t_start = time.time()
_, eval_data = collect_spectrum(TAU, gens, f_abc, gammas,
                                max_pq_sum=MAX_PQ_SUM, verbose=True)
dt_spectrum = time.time() - t_start

# Organize eigenvalue data
n_sectors = len(eval_data)
total_raw_evals = sum(len(evals) for _, _, evals in eval_data)
total_pw_weighted = sum(dim_su3_irrep(p, q) * len(evals) for p, q, evals in eval_data)

# Collect ALL |lambda| values with their PW degeneracies
all_abs_lambda = []
all_pw_deg = []
for p, q, evals in eval_data:
    d_pq = dim_su3_irrep(p, q)
    abs_lam = np.abs(evals)
    all_abs_lambda.append(abs_lam)
    all_pw_deg.append(np.full(len(abs_lam), d_pq))

all_abs_lambda = np.concatenate(all_abs_lambda)
all_pw_deg = np.concatenate(all_pw_deg)

# Basic spectrum statistics
lambda_min = all_abs_lambda.min()
lambda_max = all_abs_lambda.max()
lambda_mean = np.average(all_abs_lambda, weights=all_pw_deg)

print(f"\n  Spectrum Statistics:")
print(f"    Sectors:              {n_sectors}")
print(f"    Raw eigenvalues:      {total_raw_evals}")
print(f"    PW-weighted count:    {total_pw_weighted}")
print(f"    |lambda| range:       [{lambda_min:.6f}, {lambda_max:.6f}] M_KK")
print(f"    PW-weighted mean:     {lambda_mean:.6f} M_KK")
print(f"    Computation time:     {dt_spectrum:.1f}s")

# ===========================================================================
# STEP 2: EXACT SPECTRAL ACTION FOR f(x) = sqrt(x)
# ===========================================================================
print("\n" + "=" * 78)
print("STEP 2: Exact Spectral Action with f(x) = sqrt(x)")
print("    S_exact(Lambda) = (1/Lambda) * sum_n d_n * |lambda_n|")
print("=" * 78)

# For f(x) = sqrt(x): Tr(f(D^2/Lambda^2)) = Tr(|D|/Lambda) = (1/Lambda) sum d_n |lambda_n|
# This is INDEPENDENT of Lambda up to the overall 1/Lambda factor.
total_weighted_abs = np.sum(all_pw_deg * all_abs_lambda)

S_exact_sqrt = np.zeros(len(LAMBDA_VALUES))
for i, Lam in enumerate(LAMBDA_VALUES):
    S_exact_sqrt[i] = total_weighted_abs / Lam

print(f"\n  Total PW-weighted sum of |lambda|: {total_weighted_abs:.4f}")
print(f"\n  {'Lambda':>10}  {'S_exact(sqrt)':>16}")
print(f"  {'-'*10}  {'-'*16}")
for i, Lam in enumerate(LAMBDA_VALUES):
    print(f"  {Lam:>10.3f}  {S_exact_sqrt[i]:>16.4f}")

# ===========================================================================
# STEP 3: EXACT SPECTRAL ACTION FOR f(x) = exp(-x)
# ===========================================================================
print("\n" + "=" * 78)
print("STEP 3: Exact Spectral Action with f(x) = exp(-x)")
print("    S_exact(Lambda) = sum_n d_n * exp(-lambda_n^2 / Lambda^2)")
print("=" * 78)

S_exact_heat = np.zeros(len(LAMBDA_VALUES))
for i, Lam in enumerate(LAMBDA_VALUES):
    x = (all_abs_lambda / Lam) ** 2
    S_exact_heat[i] = np.sum(all_pw_deg * np.exp(-x))

print(f"\n  {'Lambda':>10}  {'S_exact(heat)':>16}")
print(f"  {'-'*10}  {'-'*16}")
for i, Lam in enumerate(LAMBDA_VALUES):
    print(f"  {Lam:>10.3f}  {S_exact_heat[i]:>16.4f}")

# ===========================================================================
# STEP 4: SEELEY-DEWITT COEFFICIENT EXTRACTION
# ===========================================================================
print("\n" + "=" * 78)
print("STEP 4: Seeley-DeWitt Coefficients from Heat Kernel")
print("=" * 78)

# Extract a_0 through a_8 using the tier1 infrastructure
# For dim=8 manifold: K(t) = a_0 t^{-4} + a_2 t^{-3} + a_4 t^{-2} + a_6 t^{-1} + a_8 + ...
# So t^4 K(t) = a_0 + a_2 t + a_4 t^2 + a_6 t^3 + a_8 t^4 + ...

# Extract from the L_max=6 spectrum
coeffs, fit_quality = extract_seeley_dewitt(
    eval_data, t_range=(0.001, 0.3), n_points=300, n_coeffs=5, verbose=True
)

a0_ext = coeffs['a_0']
a2_ext = coeffs['a_2']
a4_ext = coeffs['a_4']
a6_ext = coeffs.get('a_6', 0.0)
a8_ext = coeffs.get('a_8', 0.0)

# Cross-check against canonical values (which are at max_pq_sum=3)
print(f"\n  Cross-check vs canonical (max_pq_sum=3):")
print(f"    a_0: extracted={a0_ext:.2f} vs canonical={a0_fold:.2f} (ratio={a0_ext/a0_fold:.4f})")
print(f"    a_2: extracted={a2_ext:.4f} vs canonical={a2_fold:.4f} (ratio={a2_ext/a2_fold:.4f})")
print(f"    a_4: extracted={a4_ext:.4f} vs canonical={a4_fold:.4f} (ratio={a4_ext/a4_fold:.4f})")
print(f"  Note: L_max=6 includes more sectors than L_max=3; ratios > 1 are expected.")

# Also extract with broader range for systematic check
coeffs_broad, _ = extract_seeley_dewitt(
    eval_data, t_range=(0.005, 0.5), n_points=300, n_coeffs=5, verbose=False
)
coeffs_narrow, _ = extract_seeley_dewitt(
    eval_data, t_range=(0.0005, 0.15), n_points=300, n_coeffs=5, verbose=False
)

print(f"\n  Systematic check (3 t-ranges):")
print(f"  {'Coeff':>6}  {'narrow':>14}  {'default':>14}  {'broad':>14}  {'spread':>12}")
for name in ['a_0', 'a_2', 'a_4', 'a_6', 'a_8']:
    v1 = coeffs_narrow[name]
    v2 = coeffs[name]
    v3 = coeffs_broad[name]
    spread = max(v1, v2, v3) - min(v1, v2, v3)
    print(f"  {name:>6}  {v1:>14.4f}  {v2:>14.4f}  {v3:>14.4f}  {spread:>12.4f}")

# ===========================================================================
# STEP 5: HEAT KERNEL EXPANSION S_HK(Lambda)
# ===========================================================================
print("\n" + "=" * 78)
print("STEP 5: Heat Kernel Expansion S_HK(Lambda)")
print("    For f(x) = exp(-x): S_HK = a_0 L^8 + a_2 L^6 + a_4 L^4 + a_6 L^2 + a_8")
print("    where L = Lambda (cutoff in M_KK units)")
print("=" * 78)

# Heat kernel expansion for f(x) = exp(-x) on 8-dimensional manifold:
# S_HK(Lambda) = sum_k a_{2k} * Lambda^{8-2k}
# = a_0 * Lambda^8 + a_2 * Lambda^6 + a_4 * Lambda^4 + a_6 * Lambda^2 + a_8

def S_HK_heat(Lam, a0, a2, a4, a6, a8):
    """Heat kernel expansion truncated at 5 terms for dim=8."""
    return a0 * Lam**8 + a2 * Lam**6 + a4 * Lam**4 + a6 * Lam**2 + a8

# Compute S_HK at each Lambda value (using extracted coefficients)
S_hk_5term = np.array([S_HK_heat(L, a0_ext, a2_ext, a4_ext, a6_ext, a8_ext)
                        for L in LAMBDA_VALUES])
S_hk_3term = np.array([a0_ext * L**8 + a2_ext * L**6 + a4_ext * L**4
                        for L in LAMBDA_VALUES])

# Relative deviation
rel_dev_5term = np.abs(S_exact_heat - S_hk_5term) / np.abs(S_exact_heat)
rel_dev_3term = np.abs(S_exact_heat - S_hk_3term) / np.abs(S_exact_heat)

print(f"\n  Heat kernel comparison (5-term truncation):")
print(f"  {'Lambda':>8}  {'S_exact':>14}  {'S_HK(5)':>14}  {'S_HK(3)':>14}  {'|dev|(5)':>10}  {'|dev|(3)':>10}")
print(f"  {'-'*8}  {'-'*14}  {'-'*14}  {'-'*14}  {'-'*10}  {'-'*10}")
for i, Lam in enumerate(LAMBDA_VALUES):
    print(f"  {Lam:>8.3f}  {S_exact_heat[i]:>14.2f}  {S_hk_5term[i]:>14.2f}  "
          f"{S_hk_3term[i]:>14.2f}  {rel_dev_5term[i]:>10.6f}  {rel_dev_3term[i]:>10.6f}")

# ===========================================================================
# STEP 6: GATE EVALUATION at Lambda = 2.048
# ===========================================================================
print("\n" + "=" * 78)
print("STEP 6: GATE NON-PERT-SA-70 at Lambda = 2.048")
print("=" * 78)

idx_swamp = np.argmin(np.abs(LAMBDA_VALUES - LAMBDA_SWAMP))
dev_at_swamp_5 = rel_dev_5term[idx_swamp]
dev_at_swamp_3 = rel_dev_3term[idx_swamp]

print(f"\n  Lambda = {LAMBDA_VALUES[idx_swamp]:.3f} M_KK")
print(f"  S_exact(heat)  = {S_exact_heat[idx_swamp]:.6f}")
print(f"  S_HK(5-term)   = {S_hk_5term[idx_swamp]:.6f}")
print(f"  S_HK(3-term)   = {S_hk_3term[idx_swamp]:.6f}")
print(f"  Deviation (5-term): {dev_at_swamp_5:.6f} = {100*dev_at_swamp_5:.4f}%")
print(f"  Deviation (3-term): {dev_at_swamp_3:.6f} = {100*dev_at_swamp_3:.4f}%")

# Gate verdict (use 5-term as the primary comparison)
if dev_at_swamp_5 < GATE_PASS:
    gate_verdict = "PASS"
    gate_detail = (f"5-term HK deviation = {100*dev_at_swamp_5:.4f}% < {100*GATE_PASS:.0f}% "
                   f"at Lambda = {LAMBDA_SWAMP}. Heat kernel expansion converged.")
elif dev_at_swamp_5 > GATE_FAIL:
    gate_verdict = "FAIL"
    gate_detail = (f"5-term HK deviation = {100*dev_at_swamp_5:.4f}% > {100*GATE_FAIL:.0f}% "
                   f"at Lambda = {LAMBDA_SWAMP}. Heat kernel expansion badly broken.")
else:
    gate_verdict = "INFO"
    gate_detail = (f"5-term HK deviation = {100*dev_at_swamp_5:.4f}% in [{100*GATE_PASS:.0f}%, "
                   f"{100*GATE_FAIL:.0f}%] at Lambda = {LAMBDA_SWAMP}. Marginal; higher-order "
                   f"a_n may be needed.")

print(f"\n  Gate NON-PERT-SA-70: {gate_verdict}")
print(f"    Threshold: PASS < {100*GATE_PASS:.0f}%, FAIL > {100*GATE_FAIL:.0f}%")
print(f"    Computed:  {100*dev_at_swamp_5:.4f}%")
print(f"    Verdict:   {gate_detail}")

# ===========================================================================
# STEP 7: EFFECTIVE a_4 (alpha_s-relevant quantity)
# ===========================================================================
print("\n" + "=" * 78)
print("STEP 7: Effective a_4 from Non-Perturbative Action")
print("=" * 78)

# For the heat kernel action at scale Lambda:
#   S(Lambda) = a_0 L^8 + a_2 L^6 + a_4 L^4 + ...
# Define the "volume term" as the leading term:
#   S_0(Lambda) = a_0 L^8
# Then the effective a_4:
#   a_4^eff = [S_exact(L) - a_0 L^8 - a_2 L^6] / L^4
# This captures all non-perturbative corrections folded into a_4.

a4_eff = np.zeros(len(LAMBDA_VALUES))
for i, Lam in enumerate(LAMBDA_VALUES):
    S_residual = S_exact_heat[i] - a0_ext * Lam**8 - a2_ext * Lam**6
    if Lam > 0:
        a4_eff[i] = S_residual / Lam**4

delta_a4_frac = (a4_eff - a4_ext) / np.abs(a4_ext) if np.abs(a4_ext) > 1e-10 else np.zeros_like(a4_eff)

print(f"\n  a_4(HK) = {a4_ext:.6f}")
print(f"\n  {'Lambda':>8}  {'a_4^eff':>14}  {'delta/a_4':>12}  {'|delta|/a_4':>12}  {'> Gilkey?':>10}")
print(f"  {'-'*8}  {'-'*14}  {'-'*12}  {'-'*12}  {'-'*10}")
for i, Lam in enumerate(LAMBDA_VALUES):
    exceeds = "|delta|/a_4 > 14.9%" if np.abs(delta_a4_frac[i]) > RATIO_GILKEY else ""
    print(f"  {Lam:>8.3f}  {a4_eff[i]:>14.6f}  {delta_a4_frac[i]:>12.6f}  "
          f"{np.abs(delta_a4_frac[i]):>12.6f}  {exceeds}")

# Check at Lambda = 2.048
a4_eff_swamp = a4_eff[idx_swamp]
delta_swamp = delta_a4_frac[idx_swamp]
print(f"\n  At Lambda = 2.048:")
print(f"    a_4^eff = {a4_eff_swamp:.6f}")
print(f"    delta(a_4)/a_4 = {delta_swamp:.6f} = {100*delta_swamp:.4f}%")
print(f"    |delta|/a_4 {'>' if abs(delta_swamp) > RATIO_GILKEY else '<'} {100*RATIO_GILKEY:.1f}% "
      f"(Gilkey discrepancy threshold)")
if np.abs(delta_swamp) > RATIO_GILKEY:
    print(f"    ==> Non-perturbative correction may resolve alpha_s tension!")
else:
    print(f"    ==> Non-perturbative correction too small to resolve alpha_s tension.")

# ===========================================================================
# STEP 8: CONVERGENCE ANALYSIS -- dense Lambda scan
# ===========================================================================
print("\n" + "=" * 78)
print("STEP 8: Dense Lambda Scan for Convergence Profile")
print("=" * 78)

Lambda_dense = np.linspace(0.3, 15.0, 500)
S_exact_dense = np.zeros(len(Lambda_dense))
S_hk5_dense = np.zeros(len(Lambda_dense))
S_hk3_dense = np.zeros(len(Lambda_dense))

for i, Lam in enumerate(Lambda_dense):
    x = (all_abs_lambda / Lam) ** 2
    S_exact_dense[i] = np.sum(all_pw_deg * np.exp(-x))
    S_hk5_dense[i] = S_HK_heat(Lam, a0_ext, a2_ext, a4_ext, a6_ext, a8_ext)
    S_hk3_dense[i] = a0_ext * Lam**8 + a2_ext * Lam**6 + a4_ext * Lam**4

dev_dense_5 = np.abs(S_exact_dense - S_hk5_dense) / np.abs(S_exact_dense)
dev_dense_3 = np.abs(S_exact_dense - S_hk3_dense) / np.abs(S_exact_dense)

# Find Lambda where deviation crosses 10%
mask_5 = dev_dense_5 > GATE_PASS
if np.any(mask_5):
    Lambda_breakdown_5 = Lambda_dense[np.where(mask_5)[0][-1]] if Lambda_dense[mask_5].max() > LAMBDA_SWAMP else Lambda_dense[mask_5].max()
    # Find the highest Lambda where deviation > 10%
    idx_cross = np.where(mask_5)[0]
    Lambda_breakdown_5 = Lambda_dense[idx_cross[-1]] if len(idx_cross) > 0 else np.nan
else:
    Lambda_breakdown_5 = np.nan

mask_3 = dev_dense_3 > GATE_PASS
if np.any(mask_3):
    idx_cross_3 = np.where(mask_3)[0]
    Lambda_breakdown_3 = Lambda_dense[idx_cross_3[-1]] if len(idx_cross_3) > 0 else np.nan
else:
    Lambda_breakdown_3 = np.nan

print(f"\n  Convergence thresholds (where |S_exact - S_HK| / S_exact > 10%):")
print(f"    5-term HK: deviation > 10% for Lambda < {Lambda_breakdown_5:.3f} M_KK"
      if not np.isnan(Lambda_breakdown_5) else "    5-term HK: deviation always < 10%")
print(f"    3-term HK: deviation > 10% for Lambda < {Lambda_breakdown_3:.3f} M_KK"
      if not np.isnan(Lambda_breakdown_3) else "    3-term HK: deviation always < 10%")

# ===========================================================================
# STEP 9: ZETA SPECTRAL ACTION COMPARISON
# ===========================================================================
print("\n" + "=" * 78)
print("STEP 9: Zeta Spectral Action S_zeta = a_4(D^2)")
print("    FUNCTIONAL COMPARISON: cutoff vs zeta vs heat kernel")
print("=" * 78)

# The zeta spectral action S_zeta = zeta_D(0) = a_4(D^2_full).
# For the internal space, this is just a_4. The full product gives:
#   S_zeta = a_0(M4)*a_4(K) + a_2(M4)*a_2(K) + a_4(M4)*a_0(K)
# Key point: NO a_0(K)*Lambda^4 term (the CC term is absent in the zeta action).

# Compute spectral zeta sums directly
a0_zeta = 0.0  # (local)
a2_zeta = 0.0  # (local)
a4_zeta = 0.0  # (local)
a6_zeta = 0.0  # (local)

for p, q, evals in eval_data:
    d_pq = dim_su3_irrep(p, q)

    # Positive eigenvalues only (Dirac eigenvalues come in +/- pairs)
    pos_mask = np.ones(len(evals), dtype=bool)
    for j, e in enumerate(evals):
        if np.abs(np.imag(e)) > 1e-10:
            pos_mask[j] = (np.imag(e) > 0)
        elif np.abs(np.real(e)) > 1e-10:
            pos_mask[j] = (np.real(e) > 0)
        else:
            pos_mask[j] = False

    pos_evals = np.abs(evals[pos_mask])
    n_pos = len(pos_evals)

    a0_zeta += d_pq * n_pos
    if n_pos > 0:
        a2_zeta += d_pq * np.sum(pos_evals**(-2))
        a4_zeta += d_pq * np.sum(pos_evals**(-4))
        a6_zeta += d_pq * np.sum(pos_evals**(-6))

print(f"\n  Spectral zeta moments (direct eigenvalue sums, L_max=6):")
print(f"    a_0(zeta) = {a0_zeta:.2f}  (mode count)")
print(f"    a_2(zeta) = {a2_zeta:.6f}  (gravity coupling)")
print(f"    a_4(zeta) = {a4_zeta:.6f}  (gauge coupling)")
print(f"    a_6(zeta) = {a6_zeta:.6f}  (Higgs coupling)")

print(f"\n  Cross-check: a_4(zeta) vs a_4(heat kernel fit):")
print(f"    a_4(zeta)  = {a4_zeta:.6f}")
print(f"    a_4(HK)    = {a4_ext:.6f}")
frac_diff_a4 = abs(a4_zeta - a4_ext) / abs(a4_zeta)
print(f"    |diff|/a_4 = {frac_diff_a4:.6f} = {100*frac_diff_a4:.4f}%")
print(f"    (These should agree at large Lambda; disagreement signals HK fit error)")

print(f"\n  FUNCTIONAL SENSITIVITY ANALYSIS at Lambda = 2.048:")
print(f"    Cutoff S(sqrt): S = (1/L) sum d_n |lam| = {S_exact_sqrt[idx_swamp]:.4f}")
print(f"    Heat kernel S:  S = sum d_n exp(-lam^2/L^2) = {S_exact_heat[idx_swamp]:.4f}")
print(f"    Zeta S:         S = a_4 = {a4_zeta:.6f}  (Lambda-independent!)")
print(f"  The zeta action is Lambda-INDEPENDENT for the internal space.")
print(f"  This is maximal scheme dependence: S_zeta does not scale with Lambda at all.")

# ===========================================================================
# STEP 10: PLOTS
# ===========================================================================
print("\n" + "=" * 78)
print("STEP 10: Generating Plots")
print("=" * 78)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('NON-PERT-SA-70: Non-Perturbative vs Heat Kernel Spectral Action',
             fontsize=13, fontweight='bold')

# Panel (a): S_exact vs S_HK for heat kernel
ax = axes[0, 0]
ax.semilogy(Lambda_dense, S_exact_dense, 'b-', linewidth=2, label='$S_{\\rm exact}$ (heat)')
ax.semilogy(Lambda_dense, S_hk5_dense, 'r--', linewidth=1.5, label='$S_{\\rm HK}$ (5-term)')
ax.semilogy(Lambda_dense, S_hk3_dense, 'g:', linewidth=1.5, label='$S_{\\rm HK}$ (3-term)')
ax.axvline(LAMBDA_SWAMP, color='orange', linestyle='-.', alpha=0.7, label=f'$\\Lambda = {LAMBDA_SWAMP}$')
ax.set_xlabel('$\\Lambda$ [$M_{KK}$]')
ax.set_ylabel('Spectral Action $S(\\Lambda)$')
ax.set_title('(a) $f(x) = e^{-x}$: Exact vs HK')
ax.legend(fontsize=8)
ax.set_xlim(0.3, 10)
ax.grid(True, alpha=0.3)

# Panel (b): Relative deviation
ax = axes[0, 1]
ax.semilogy(Lambda_dense, dev_dense_5, 'r-', linewidth=1.5, label='5-term HK')
ax.semilogy(Lambda_dense, dev_dense_3, 'g-', linewidth=1.5, label='3-term HK')
ax.axhline(GATE_PASS, color='blue', linestyle='--', alpha=0.5, label=f'{100*GATE_PASS:.0f}% threshold')
ax.axhline(GATE_FAIL, color='red', linestyle='--', alpha=0.5, label=f'{100*GATE_FAIL:.0f}% threshold')
ax.axvline(LAMBDA_SWAMP, color='orange', linestyle='-.', alpha=0.7, label=f'$\\Lambda = {LAMBDA_SWAMP}$')
# Mark gate evaluation point
ax.plot(LAMBDA_VALUES[idx_swamp], dev_at_swamp_5, 'ro', markersize=10, zorder=5,
        label=f'Gate: {100*dev_at_swamp_5:.2f}%')
ax.set_xlabel('$\\Lambda$ [$M_{KK}$]')
ax.set_ylabel('$|S_{\\rm exact} - S_{\\rm HK}| / S_{\\rm exact}$')
ax.set_title('(b) Relative Deviation: Exact vs HK')
ax.legend(fontsize=7, loc='upper right')
ax.set_xlim(0.3, 10)
ax.set_ylim(1e-12, 1.0)
ax.grid(True, alpha=0.3)

# Panel (c): f(x) = sqrt(x) spectral action
ax = axes[1, 0]
ax.plot(LAMBDA_VALUES, S_exact_sqrt, 'bs-', markersize=8, linewidth=2, label='$S_{\\rm exact}(\\sqrt{x})$')
ax.axvline(LAMBDA_SWAMP, color='orange', linestyle='-.', alpha=0.7, label=f'$\\Lambda = {LAMBDA_SWAMP}$')
ax.set_xlabel('$\\Lambda$ [$M_{KK}$]')
ax.set_ylabel('$S(\\Lambda) = (1/\\Lambda) \\sum d_n |\\lambda_n|$')
ax.set_title('(c) $f(x) = \\sqrt{x}$: Framework Spectral Action')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel (d): Effective a_4
ax = axes[1, 1]
ax.plot(LAMBDA_VALUES, a4_eff, 'ko-', markersize=8, linewidth=2, label='$a_4^{\\rm eff}(\\Lambda)$')
ax.axhline(a4_ext, color='blue', linestyle='--', alpha=0.7, label=f'$a_4$ (HK) = {a4_ext:.2f}')
ax.axhline(a4_zeta, color='red', linestyle=':', alpha=0.7, label=f'$a_4$ (zeta) = {a4_zeta:.2f}')
ax.axvline(LAMBDA_SWAMP, color='orange', linestyle='-.', alpha=0.7, label=f'$\\Lambda = {LAMBDA_SWAMP}$')
# Shade Gilkey band
a4_lo = a4_ext * (1 - RATIO_GILKEY)
a4_hi = a4_ext * (1 + RATIO_GILKEY)
ax.axhspan(a4_lo, a4_hi, color='gray', alpha=0.15, label=f'Gilkey band ({100*RATIO_GILKEY:.1f}%)')
ax.set_xlabel('$\\Lambda$ [$M_{KK}$]')
ax.set_ylabel('$a_4^{\\rm eff}(\\Lambda)$')
ax.set_title('(d) Effective $a_4$ (non-perturbative)')
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('s70_non_pert_sa.png', dpi=150, bbox_inches='tight')
print("  Saved: s70_non_pert_sa.png")

# ===========================================================================
# STEP 11: SAVE DATA
# ===========================================================================
print("\n" + "=" * 78)
print("STEP 11: Saving Results")
print("=" * 78)

np.savez('s70_non_pert_sa.npz',
    # Gate
    gate_name=np.array('NON-PERT-SA-70'),
    gate_verdict=np.array(gate_verdict),
    gate_detail=np.array(gate_detail),

    # Configuration
    tau=np.float64(TAU),
    max_pq_sum=np.int64(MAX_PQ_SUM),
    n_sectors=np.int64(n_sectors),
    total_raw_evals=np.int64(total_raw_evals),
    total_pw_weighted=np.int64(total_pw_weighted),
    lambda_min=np.float64(lambda_min),
    lambda_max=np.float64(lambda_max),

    # Lambda values
    Lambda_values=LAMBDA_VALUES,
    Lambda_swamp=np.float64(LAMBDA_SWAMP),

    # Exact spectral actions
    S_exact_sqrt=S_exact_sqrt,
    S_exact_heat=S_exact_heat,
    total_weighted_abs=np.float64(total_weighted_abs),

    # Heat kernel expansion
    S_HK_5term=S_hk_5term,
    S_HK_3term=S_hk_3term,

    # Seeley-DeWitt coefficients (HK extraction at L_max=6)
    a0_HK=np.float64(a0_ext),
    a2_HK=np.float64(a2_ext),
    a4_HK=np.float64(a4_ext),
    a6_HK=np.float64(a6_ext),
    a8_HK=np.float64(a8_ext),

    # Spectral zeta coefficients (direct eigenvalue sums)
    a0_zeta=np.float64(a0_zeta),
    a2_zeta=np.float64(a2_zeta),
    a4_zeta=np.float64(a4_zeta),
    a6_zeta=np.float64(a6_zeta),

    # Deviations
    rel_dev_5term=rel_dev_5term,
    rel_dev_3term=rel_dev_3term,
    dev_at_swamp_5=np.float64(dev_at_swamp_5),
    dev_at_swamp_3=np.float64(dev_at_swamp_3),

    # Effective a_4
    a4_eff=a4_eff,
    a4_eff_swamp=np.float64(a4_eff_swamp),
    delta_a4_frac=delta_a4_frac,
    delta_a4_swamp=np.float64(delta_swamp),

    # Dense scan
    Lambda_dense=Lambda_dense,
    dev_dense_5=dev_dense_5,
    dev_dense_3=dev_dense_3,
    Lambda_breakdown_5=np.float64(Lambda_breakdown_5),
    Lambda_breakdown_3=np.float64(Lambda_breakdown_3),

    # Fit quality
    HK_fit_residual=np.float64(fit_quality['residual']),
    HK_fit_condition=np.float64(fit_quality['condition_number']),
)

print("  Saved: s70_non_pert_sa.npz")

# ===========================================================================
# SUMMARY
# ===========================================================================
print("\n" + "=" * 78)
print("NON-PERT-SA-70: SUMMARY")
print("=" * 78)

print(f"""
  SPECTRAL FUNCTION COMPARISON AT Lambda = {LAMBDA_SWAMP} M_KK
  =============================================================

  Spectrum: {n_sectors} sectors, {total_raw_evals} eigenvalues, {total_pw_weighted} PW-weighted
  |lambda| range: [{lambda_min:.4f}, {lambda_max:.4f}] M_KK

  HEAT KERNEL (f(x) = exp(-x)):
    S_exact        = {S_exact_heat[idx_swamp]:.6f}
    S_HK (5-term)  = {S_hk_5term[idx_swamp]:.6f}
    S_HK (3-term)  = {S_hk_3term[idx_swamp]:.6f}
    Deviation (5t) = {100*dev_at_swamp_5:.6f}%
    Deviation (3t) = {100*dev_at_swamp_3:.6f}%

  FRAMEWORK f(x) = sqrt(x):
    S_exact(sqrt)  = {S_exact_sqrt[idx_swamp]:.4f}
    (No HK expansion available -- Mellin moments diverge)

  ZETA ACTION:
    S_zeta = a_4   = {a4_zeta:.6f}
    (Lambda-independent, NO cosmological constant term)

  EFFECTIVE a_4:
    a_4(HK)        = {a4_ext:.6f}
    a_4(zeta)      = {a4_zeta:.6f}
    a_4^eff(2.048) = {a4_eff_swamp:.6f}
    delta(a_4)/a_4 = {100*delta_swamp:.4f}%
    Gilkey threshold: {100*RATIO_GILKEY:.1f}%
    {'Exceeds Gilkey -> may resolve alpha_s' if abs(delta_swamp) > RATIO_GILKEY else 'Below Gilkey -> does not resolve alpha_s'}

  CONVERGENCE:
    5-term HK breakdown: Lambda < {Lambda_breakdown_5:.3f} M_KK  (> 10% deviation)
    3-term HK breakdown: Lambda < {Lambda_breakdown_3:.3f} M_KK  (> 10% deviation)

  GATE NON-PERT-SA-70: {gate_verdict}
    {gate_detail}

  FUNCTIONAL INDEPENDENCE CLASSIFICATION:
    a_0, a_2, a_4, a_6: FUNCTIONAL-INDEPENDENT (Seeley-DeWitt coefficients)
    S_exact(Lambda):     SCHEME-DEPENDENT (depends on f(x) choice)
    HK convergence rate: SCHEME-DEPENDENT (depends on Lambda and f(x))
    a_4^eff(Lambda):     SCHEME-DEPENDENT (mixes non-perturbative corrections)
    Gate verdict:        SCHEME-DEPENDENT (evaluated for f(x) = exp(-x) only)
""")

print("DONE.")
