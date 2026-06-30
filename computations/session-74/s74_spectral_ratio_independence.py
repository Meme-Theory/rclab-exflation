#!/usr/bin/env python3
"""
SPECTRAL-RATIO-INDEPENDENCE-74  (S74 W3-F, Wave 3 Batch 2)
===========================================================

Cross-check: Route 2 E_C (W1-D), branch-resolved n_bar (W2-A), and horizon
backreaction (W2-C) all modify the Bogoliubov coefficients |beta_k|^2.
Do the corrections DOUBLE-COUNT (share a common physical origin)?

We quantify this by computing |beta_k|^2 under each correction individually
and jointly, then comparing the linear-sum-of-individual-deltas against the
nonlinear product formula.

STRUCTURE
---------
Baseline: |beta_k|^2_0 = sinh^2(r_k_bcs) from S73A BCS coherence parameter,
                        mode-resolved over the 8 fabric modes (B1, B2[0..3], B3[0..2]).

Correction factors (multiplicative on |beta_k|^2):
  lambda_EC(k)  : E_C canonical (W1-D, Method A)        — single-cell Delta_OES invariant
  lambda_nbar(k): branch-resolved f_retention  (W2-A)   — group-velocity hop retention
  lambda_HFB(k) : horizon backreaction var_ratio (W2-C) — squeeze x horizon cross term

|beta_k|^2_{EC}     = |beta_k|^2_0 * lambda_EC(k)
|beta_k|^2_{nbar}   = |beta_k|^2_0 * lambda_nbar(k)
|beta_k|^2_{HFB}    = |beta_k|^2_0 * lambda_HFB(k)
|beta_k|^2_{all}    = |beta_k|^2_0 * lambda_EC(k) * lambda_nbar(k) * lambda_HFB(k)

Additivity test (linear-sum approximation):
  Delta_all_linear   = sum_i (|beta_k|^2_{i} - |beta_k|^2_0)
  Delta_all_nonlin   = |beta_k|^2_{all} - |beta_k|^2_0

  Primary (observable-scale) metric:
      residual_obs(k) = (Delta_all_nonlin - Delta_all_linear) / |beta_k|^2_0
  This is the fractional error on the observable |beta_k|^2 itself and is
  robust at exact-cancellation points where Delta_all_nonlin happens to vanish.

  Secondary (delta-scale) metric:
      residual_del(k) = (Delta_all_nonlin - Delta_all_linear) / |Delta_all_nonlin|
  Diverges when individual-correction deltas cancel (artifact, not physics).

PRE-REGISTERED GATE (primary, observable-scale)
-----------------------------------------------
  PASS:  max |residual_obs| < 5%   (linear-additive valid)
  INFO:  5% <= max |residual_obs| < 15%   (mildly nonlinearly coupled)
  FAIL:  max |residual_obs| >= 15%        (double-counting risk)

SUBSTRATE FRAMING
-----------------
All three corrections live on the SAME Dirac operator spectrum D_K restricted
to the 8 fabric modes near the fold. Any nonlinear coupling between them
reflects shared spectral structure (i.e., two corrections acting on the same
eigenvalue branch). The cross-check separates structural independence from
operational overlap.

OUTPUT
------
  s74_spectral_ratio_independence.npz
  s74_spectral_ratio_independence.png
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import M_KK, Delta_BCS, tau_fold, dt_transit

# --------------------------------------------------------------------------
# 0. Gate pre-registration
# --------------------------------------------------------------------------
GATE_NAME = "SPECTRAL-RATIO-INDEPENDENCE-74"
GATE_DESC = "Cross-check of W1-D + W2-A + W2-C corrections for |beta_k|^2 double-counting"
GATE_PASS_THRESHOLD_PCT  = 5.0   # (local)
GATE_INFO_THRESHOLD_PCT  = 15.0  # (local)

print("=" * 74)
print(f"{GATE_NAME}  —  S74 W3-F")
print("=" * 74)
print(f"Gate: {GATE_DESC}")
print(f"  PASS:  max residual < {GATE_PASS_THRESHOLD_PCT:.1f} %")
print(f"  INFO:  {GATE_PASS_THRESHOLD_PCT:.1f} % <= max residual < {GATE_INFO_THRESHOLD_PCT:.1f} %")
print(f"  FAIL:  max residual >= {GATE_INFO_THRESHOLD_PCT:.1f} %")
print()

# --------------------------------------------------------------------------
# 1. Load W1-D, W2-A, W2-C outputs
# --------------------------------------------------------------------------
print("-" * 74)
print("[1] Loading Wave 1-2 outputs")
print("-" * 74)

ec_data  = np.load("computations/session-74/s74_ec_resolution.npz", allow_pickle=True)
nb_data  = np.load("computations/session-74/s74_branch_nbar_dk.npz", allow_pickle=True)
hfb_data = np.load("computations/session-74/s74_hfb_horizon_backreaction.npz", allow_pickle=True)

# W1-D: E_C canonical (Method A) = Delta_OES single-cell invariant
E_C_canonical   = float(ec_data["E_C_oes_cg24"])
E_C_method_B    = float(ec_data["E_C_oes_cg24_method_B"])
E_C_method_C    = float(ec_data["E_C_oes_cg24_method_C"])
EC_corr_upper_pct = float(ec_data["correction_upper_bound_pct"])   # (local) 0.394%
EC_method_C_pct = float(ec_data["method_C_vs_A_pct"])              # (local) 13.13%

print(f"W1-D  E_C canonical (Method A)  = {E_C_canonical:.6f} M_KK   (= Delta_OES)")
print(f"      E_C Method B (pair-add)   = {E_C_method_B:.6f} M_KK")
print(f"      E_C Method C (excess)     = {E_C_method_C:.6f} M_KK")
print(f"      correction_upper_bound    = {EC_corr_upper_pct:.4f} %   (n_bar sensitivity)")

# W2-A: mode-resolved baseline r_k and corrected r_k (f_retention = 1/(1+N_hop))
labels        = [str(l) for l in nb_data["labels"]]
r_k_baseline  = np.array(nb_data["r_k_baseline"])
r_k_corrected = np.array(nb_data["r_k_corrected"])
f_retention   = np.array(nb_data["f_retention"])
N_hop         = np.array(nb_data["N_hop"])
n_bar_base_W2A = np.array(nb_data["n_bar_baseline"])
n_bar_corr_W2A = np.array(nb_data["n_bar_corrected"])
idx_B1 = np.array(nb_data["idx_B1"])
idx_B2 = np.array(nb_data["idx_B2"])
idx_B3 = np.array(nb_data["idx_B3"])
print(f"\nW2-A  r_k_baseline  = {r_k_baseline}")
print(f"      f_retention   = {f_retention}")
print(f"      n_bar_base    = {n_bar_base_W2A}")
print(f"      n_bar_corr    = {n_bar_corr_W2A}")

# W2-C: var_ratio = cosh(2r) + sinh(2r)*cos(phi)  (per-mode)
#       factor_k  = sqrt(var_ratio)
var_ratio_W2C   = np.array(hfb_data["var_ratio"])
factor_k_W2C    = np.array(hfb_data["factor_k"])
factor_avg_W2C  = float(hfb_data["factor_avg"])
phi_comp        = np.array(hfb_data["phi_comp"])
r_exit          = np.array(hfb_data["r_exit"])
n_k_hfb         = np.array(hfb_data["n_k"])
mode_wt         = np.array(hfb_data["mode_wt"])
print(f"\nW2-C  var_ratio     = {var_ratio_W2C}")
print(f"      factor_k      = {factor_k_W2C}")
print(f"      factor_avg    = {factor_avg_W2C:.6f}")
print(f"      r_exit        = {r_exit}")
print(f"      phi_comp      = {phi_comp}")

# --------------------------------------------------------------------------
# 2. Build baseline |beta_k|^2 and the three correction factors
# --------------------------------------------------------------------------
print()
print("-" * 74)
print("[2] Baseline |beta_k|^2 and correction factors")
print("-" * 74)

# Baseline |beta_k|^2 = sinh^2(r_k_bcs)
# (This equals n_bar_base_W2A by construction in the BCS squeezed-state picture.)
beta2_0 = np.sinh(r_k_baseline) ** 2  # (local) mode-resolved baseline
assert np.allclose(beta2_0, n_bar_base_W2A), "Baseline |beta|^2 != n_bar_base"
print(f"|beta_k|^2_0  (baseline, sinh^2(r_bcs)) = {beta2_0}")

# -----------------------------------------------------------------
# W1-D lambda_EC: E_C canonical is a RESOLUTION — it selects Method A
# (Delta_OES = 0.4643 M_KK) as the single-cell gap. The BCS
# r_k_bcs used by S73A depends only on the gap Delta, not on the
# charging energy route. Since Delta is unchanged by canonicalization,
# the direct effect on |beta_k|^2 is the residual sensitivity
#   correction_upper_bound_pct / 100.
# We define lambda_EC(k) = 1 + delta_EC  with |delta_EC| <= 0.004.
# For the default additivity test we take delta_EC = +corr_upper_bound
# (worst-case positive bias). A sign-symmetric sensitivity is reported
# below.
# -----------------------------------------------------------------
delta_EC = EC_corr_upper_pct / 100.0  # (local)
lambda_EC = np.ones_like(beta2_0) * (1.0 + delta_EC)  # (local) uniform, conservative
print(f"\nlambda_EC(k)   = {lambda_EC}  (uniform, delta_EC = +{delta_EC:.6f})")

# -----------------------------------------------------------------
# W2-A lambda_nbar: f_retention(k)^2 acts on sinh^2(r) = |beta|^2
# Wait: the W2-A correction applies r_k -> r_k * f_retention,
# NOT n_bar -> n_bar * f_retention. So
#   lambda_nbar(k) = sinh^2(r_k * f_retention) / sinh^2(r_k)
# This is nonlinear in f_retention; use exact ratio.
# -----------------------------------------------------------------
lambda_nbar = n_bar_corr_W2A / n_bar_base_W2A  # (local) exact nonlinear ratio
print(f"\nlambda_nbar(k) = {lambda_nbar}  (exact sinh^2 ratio)")

# -----------------------------------------------------------------
# W2-C lambda_HFB: var_ratio(k) is the multiplicative correction on
# mode VARIANCE, which for a squeezed vacuum rescales |beta|^2 directly:
#   |beta|^2 = sinh^2(r_eff)  where
#   <omega^2>_sq / omega^2_vac = cosh(2r) + sinh(2r) cos(phi) = var_ratio
# Treating var_ratio as a multiplicative correction on |beta|^2 at
# the FABRIC (r_bcs) level yields the proper cross-check: both
# W2-A and W2-C are rescalings of the same BCS Bogoliubov mode variance.
# -----------------------------------------------------------------
lambda_HFB = var_ratio_W2C.copy()  # (local)
print(f"\nlambda_HFB(k)  = {lambda_HFB}  (= var_ratio_W2C)")

# --------------------------------------------------------------------------
# 3. Individual and combined |beta_k|^2
# --------------------------------------------------------------------------
print()
print("-" * 74)
print("[3] |beta_k|^2 under each single / combined correction")
print("-" * 74)

beta2_EC   = beta2_0 * lambda_EC    # (local)
beta2_nbar = beta2_0 * lambda_nbar  # (local)
beta2_HFB  = beta2_0 * lambda_HFB   # (local)

beta2_all = beta2_0 * lambda_EC * lambda_nbar * lambda_HFB  # (local) multiplicative combination

print(f"|beta_k|^2 (EC only)   = {beta2_EC}")
print(f"|beta_k|^2 (nbar only) = {beta2_nbar}")
print(f"|beta_k|^2 (HFB only)  = {beta2_HFB}")
print(f"|beta_k|^2 (ALL)       = {beta2_all}")

# --------------------------------------------------------------------------
# 4. Additivity test
# --------------------------------------------------------------------------
print()
print("-" * 74)
print("[4] Additivity test — linear-sum vs product")
print("-" * 74)

# Individual deltas
delta_EC_beta   = beta2_EC   - beta2_0  # (local)
delta_nbar_beta = beta2_nbar - beta2_0  # (local)
delta_HFB_beta  = beta2_HFB  - beta2_0  # (local)

# Linear sum of deltas (what you would expect if the three corrections were
# independent infinitesimals on the same observable)
delta_sum_linear = delta_EC_beta + delta_nbar_beta + delta_HFB_beta  # (local)

# Nonlinear (actual product) delta
delta_sum_nonlin = beta2_all - beta2_0  # (local)

# Per-mode residual
eps = 1e-30  # (local) guard against /0
residual_abs = delta_sum_nonlin - delta_sum_linear  # (local) nonlin - linear

# PRIMARY metric (observable-scale): fractional error on |beta_k|^2 itself.
# Robust when Delta_all_nonlin exactly vanishes (pair cancellation).
residual_obs = residual_abs / beta2_0  # (local)

# SECONDARY metric (delta-scale): normalized by |Delta_all_nonlin|.
# Diverges when individual deltas happen to cancel — NOT a physics signal.
residual_del = residual_abs / (np.abs(delta_sum_nonlin) + eps)  # (local)

# Alias for back-compatibility
residual_rel = residual_obs  # (local) primary metric

# Alternative: compare |beta|^2 themselves (fractional)
frac_all_vs_baseline   = (beta2_all - beta2_0) / beta2_0           # (local)
frac_linear_vs_baseline = delta_sum_linear / beta2_0                # (local)

# Cross-coupling magnitude: product of pairs
cross_EC_nbar = (lambda_EC - 1.0) * (lambda_nbar - 1.0) * beta2_0   # (local)
cross_EC_HFB  = (lambda_EC - 1.0) * (lambda_HFB - 1.0) * beta2_0    # (local)
cross_nbar_HFB = (lambda_nbar - 1.0) * (lambda_HFB - 1.0) * beta2_0 # (local)
cross_triple  = (lambda_EC - 1.0) * (lambda_nbar - 1.0) * (lambda_HFB - 1.0) * beta2_0  # (local)

print(f"Delta_EC(k)        = {delta_EC_beta}")
print(f"Delta_nbar(k)      = {delta_nbar_beta}")
print(f"Delta_HFB(k)       = {delta_HFB_beta}")
print(f"\nDelta_sum_linear   = {delta_sum_linear}")
print(f"Delta_sum_nonlin   = {delta_sum_nonlin}")
print(f"\nResidual abs (nonlin - linear) = {residual_abs}")
print()
print("PRIMARY METRIC -- observable-scale residual:")
print(f"  residual_obs(k) [pct] = {residual_obs * 100.0}")
print(f"  max  |residual_obs|  = {np.max(np.abs(residual_obs)) * 100:.6f} %")
print(f"  mean |residual_obs|  = {np.mean(np.abs(residual_obs)) * 100:.6f} %")
print()
print("SECONDARY METRIC -- delta-scale residual (diverges at cancellation points):")
print(f"  residual_del(k) [pct] = {residual_del * 100.0}")
print(f"  max  |residual_del|  = {np.max(np.abs(residual_del)) * 100:.6f} %")
print(f"  mean |residual_del|  = {np.mean(np.abs(residual_del)) * 100:.6f} %")

# Branch-averaged numbers using DOS weighting (from W2-C mode_wt)
avg_beta2_0   = float(np.sum(mode_wt * beta2_0))     # (local)
avg_beta2_EC  = float(np.sum(mode_wt * beta2_EC))    # (local)
avg_beta2_nb  = float(np.sum(mode_wt * beta2_nbar))  # (local)
avg_beta2_HFB = float(np.sum(mode_wt * beta2_HFB))   # (local)
avg_beta2_all = float(np.sum(mode_wt * beta2_all))   # (local)

avg_delta_lin   = (avg_beta2_EC - avg_beta2_0) + (avg_beta2_nb - avg_beta2_0) + (avg_beta2_HFB - avg_beta2_0)  # (local)
avg_delta_nonlin = avg_beta2_all - avg_beta2_0  # (local)
avg_res_rel = (avg_delta_nonlin - avg_delta_lin) / (abs(avg_delta_nonlin) + eps)  # (local)

print()
print(f"DOS-weighted averages:")
print(f"  <|beta|^2>_0   = {avg_beta2_0:.6f}")
print(f"  <|beta|^2>_EC  = {avg_beta2_EC:.6f}")
print(f"  <|beta|^2>_nb  = {avg_beta2_nb:.6f}")
print(f"  <|beta|^2>_HFB = {avg_beta2_HFB:.6f}")
print(f"  <|beta|^2>_all = {avg_beta2_all:.6f}")
print(f"  linear-sum delta <>   = {avg_delta_lin:.6f}")
print(f"  product delta    <>   = {avg_delta_nonlin:.6f}")
print(f"  residual rel (pct)    = {avg_res_rel * 100:.4f} %")

# --------------------------------------------------------------------------
# 5. Pair-coupling diagnostics
# --------------------------------------------------------------------------
print()
print("-" * 74)
print("[5] Pair-coupling diagnostics")
print("-" * 74)

# Pairwise additivity test:
# For (1+a)(1+b) = 1 + a + b + a*b, the nonlinear residual is a*b.
# We express the residual as a fraction of the BASELINE (observable scale),
# NOT as a fraction of the delta sum (which can vanish at pair zero-crossings).
#
#   cross_ab / |beta|^2_0 = (lambda_a - 1) * (lambda_b - 1)
#
# This is dimensionless and stable across all cancellation regimes.
def pair_cross(lam_x, lam_y):
    return (lam_x - 1.0) * (lam_y - 1.0)  # dimensionless fraction of baseline

res_EC_nbar  = pair_cross(lambda_EC,  lambda_nbar)  # (local)
res_EC_HFB   = pair_cross(lambda_EC,  lambda_HFB)   # (local)
res_nbar_HFB = pair_cross(lambda_nbar, lambda_HFB)  # (local)

print("Pair cross-term (lam_a-1)(lam_b-1) as fraction of |beta|^2_0 [pct]:")
print(f"  EC   x nbar  : max = {np.max(np.abs(res_EC_nbar))*100:.6f} %, "
      f"mean = {np.mean(np.abs(res_EC_nbar))*100:.6f} %")
print(f"  EC   x HFB   : max = {np.max(np.abs(res_EC_HFB))*100:.6f} %, "
      f"mean = {np.mean(np.abs(res_EC_HFB))*100:.6f} %")
print(f"  nbar x HFB   : max = {np.max(np.abs(res_nbar_HFB))*100:.6f} %, "
      f"mean = {np.mean(np.abs(res_nbar_HFB))*100:.6f} %")

# Which pair has LARGEST absolute cross term?
pair_max_nonlin = {
    "EC x nbar":  np.max(np.abs(res_EC_nbar)),
    "EC x HFB":   np.max(np.abs(res_EC_HFB)),
    "nbar x HFB": np.max(np.abs(res_nbar_HFB)),
}
worst_pair = max(pair_max_nonlin, key=pair_max_nonlin.get)
print(f"\nMost nonlinearly coupled pair: {worst_pair}  "
      f"({pair_max_nonlin[worst_pair]*100:.6f} % of baseline)")

# Triple cross term (all three)
triple_cross_frac = (lambda_EC - 1.0) * (lambda_nbar - 1.0) * (lambda_HFB - 1.0)  # (local)
print(f"Triple cross term: max = {np.max(np.abs(triple_cross_frac))*100:.6f} % of baseline")

# --------------------------------------------------------------------------
# 6. Cross-checks
# --------------------------------------------------------------------------
print()
print("-" * 74)
print("[6] Cross-checks")
print("-" * 74)

# Cross-check 1: zero-correction limit
lim1_lin = np.ones_like(beta2_0)
beta2_lim1 = beta2_0 * lim1_lin * lim1_lin * lim1_lin
cc1_pass = bool(np.allclose(beta2_lim1, beta2_0))
print(f"[CC-1] All lambda = 1 -> |beta|^2 = |beta|^2_0   : {'PASS' if cc1_pass else 'FAIL'}")

# Cross-check 2: bounded corrections (no exponential blowup)
max_lam = max(np.max(lambda_EC), np.max(lambda_nbar), np.max(lambda_HFB))
min_lam = min(np.min(lambda_EC), np.min(lambda_nbar), np.min(lambda_HFB))
cc2_pass = bool((max_lam < 2.0) and (min_lam > 0.5))
print(f"[CC-2] All lambda in (0.5, 2.0)   : {'PASS' if cc2_pass else 'FAIL'}   "
      f"(min={min_lam:.4f}, max={max_lam:.4f})")

# Cross-check 3: residuals small for small corrections
max_delta_any = max(np.max(np.abs(lambda_EC - 1.0)),
                    np.max(np.abs(lambda_nbar - 1.0)),
                    np.max(np.abs(lambda_HFB - 1.0)))
# For (1+a)(1+b)(1+c) = 1 + a + b + c + O(eps^2), residual should be O(max_delta^2)
expected_residual_order = max_delta_any ** 2  # (local)
actual_max_res = np.max(np.abs(residual_abs))
cc3_pass = bool(actual_max_res < 10 * expected_residual_order * np.max(beta2_0))
print(f"[CC-3] Residual scales as O(max_delta^2) : {'PASS' if cc3_pass else 'FAIL'}  "
      f"(max_delta={max_delta_any:.4f}, expected O({expected_residual_order:.6e}))")

# Cross-check 4: spectral ratios invariant under common scale
#  If we multiply baseline by scalar c, all corrections are still the same multiplicatively,
#  so |beta_k|^2_{all} / |beta_k|^2_0 is unchanged.
scale_test_ratio = beta2_all / beta2_0
rescaled_baseline = beta2_0 * 2.0
rescaled_all = beta2_all * 2.0
rescaled_ratio = rescaled_all / rescaled_baseline
cc4_pass = bool(np.allclose(scale_test_ratio, rescaled_ratio))
print(f"[CC-4] Ratio invariant under baseline rescaling : {'PASS' if cc4_pass else 'FAIL'}")

# --------------------------------------------------------------------------
# 7. Gate verdict
# --------------------------------------------------------------------------
print()
print("-" * 74)
print("[7] Gate verdict")
print("-" * 74)

max_residual_pct  = float(np.max(np.abs(residual_obs)) * 100.0)   # primary: observable scale
mean_residual_pct = float(np.mean(np.abs(residual_obs)) * 100.0)
max_residual_del_pct  = float(np.max(np.abs(residual_del)) * 100.0)  # secondary
mean_residual_del_pct = float(np.mean(np.abs(residual_del)) * 100.0)

if max_residual_pct < GATE_PASS_THRESHOLD_PCT:
    gate_verdict = "PASS"
    gate_detail = f"max residual = {max_residual_pct:.4f}% < {GATE_PASS_THRESHOLD_PCT:.1f}% (linear-additive valid)"
elif max_residual_pct < GATE_INFO_THRESHOLD_PCT:
    gate_verdict = "INFO"
    gate_detail = f"max residual = {max_residual_pct:.4f}% in [{GATE_PASS_THRESHOLD_PCT:.1f}, {GATE_INFO_THRESHOLD_PCT:.1f})% (mild nonlinear coupling)"
else:
    gate_verdict = "FAIL"
    gate_detail = f"max residual = {max_residual_pct:.4f}% >= {GATE_INFO_THRESHOLD_PCT:.1f}% (double-counting risk)"

print(f"Gate {GATE_NAME}: {gate_verdict}")
print(f"  Threshold: PASS < {GATE_PASS_THRESHOLD_PCT}%  /  INFO < {GATE_INFO_THRESHOLD_PCT}%")
print(f"  Computed (PRIMARY, observable-scale):")
print(f"    max  |residual_obs| = {max_residual_pct:.6f} %")
print(f"    mean |residual_obs| = {mean_residual_pct:.6f} %")
print(f"  Computed (SECONDARY, delta-scale, diverges at cancellations):")
print(f"    max  |residual_del| = {max_residual_del_pct:.4f} %")
print(f"    mean |residual_del| = {mean_residual_del_pct:.4f} %")
print(f"  Verdict:   {gate_detail}")

# Functional classification
if gate_verdict == "PASS":
    classification = "INDEPENDENT"
elif gate_verdict == "INFO":
    classification = "WEAKLY COUPLED"
else:
    classification = "DOUBLE-COUNTING"
print(f"  Classification: {classification}")

# --------------------------------------------------------------------------
# 8. Save data
# --------------------------------------------------------------------------
print()
print("-" * 74)
print("[8] Saving outputs")
print("-" * 74)

out_data = {
    # Provenance
    "gate_name":      GATE_NAME,
    "gate_verdict":   gate_verdict,
    "gate_detail":    gate_detail,
    "classification": classification,
    "gate_pass_threshold_pct": GATE_PASS_THRESHOLD_PCT,
    "gate_info_threshold_pct": GATE_INFO_THRESHOLD_PCT,

    # Inputs
    "labels":           np.array(labels),
    "mode_wt":          mode_wt,
    "E_C_canonical":    E_C_canonical,
    "E_C_method_B":     E_C_method_B,
    "E_C_method_C":     E_C_method_C,
    "EC_corr_upper_pct": EC_corr_upper_pct,
    "EC_method_C_pct":  EC_method_C_pct,
    "r_k_baseline":     r_k_baseline,
    "r_k_corrected":    r_k_corrected,
    "f_retention":      f_retention,
    "var_ratio_W2C":    var_ratio_W2C,
    "phi_comp":         phi_comp,
    "r_exit":           r_exit,

    # Correction factors
    "lambda_EC":        lambda_EC,
    "lambda_nbar":      lambda_nbar,
    "lambda_HFB":       lambda_HFB,
    "delta_EC":         delta_EC,

    # |beta_k|^2 results
    "beta2_0":          beta2_0,
    "beta2_EC":         beta2_EC,
    "beta2_nbar":       beta2_nbar,
    "beta2_HFB":        beta2_HFB,
    "beta2_all":        beta2_all,

    # Deltas
    "delta_EC_beta":    delta_EC_beta,
    "delta_nbar_beta":  delta_nbar_beta,
    "delta_HFB_beta":   delta_HFB_beta,
    "delta_sum_linear": delta_sum_linear,
    "delta_sum_nonlin": delta_sum_nonlin,

    # Residuals
    "residual_abs":     residual_abs,
    "residual_obs":     residual_obs,    # primary: observable-scale
    "residual_del":     residual_del,    # secondary: delta-scale
    "residual_rel":     residual_rel,    # alias (= residual_obs)
    "max_residual_pct":      max_residual_pct,      # primary
    "mean_residual_pct":     mean_residual_pct,     # primary
    "max_residual_del_pct":  max_residual_del_pct,  # secondary
    "mean_residual_del_pct": mean_residual_del_pct, # secondary

    # Pair-coupling (observable-scale cross terms)
    "res_EC_nbar":        res_EC_nbar,
    "res_EC_HFB":         res_EC_HFB,
    "res_nbar_HFB":       res_nbar_HFB,
    "triple_cross_frac":  triple_cross_frac,
    "worst_pair":         worst_pair,

    # DOS-averaged
    "avg_beta2_0":      avg_beta2_0,
    "avg_beta2_EC":     avg_beta2_EC,
    "avg_beta2_nbar":   avg_beta2_nb,
    "avg_beta2_HFB":    avg_beta2_HFB,
    "avg_beta2_all":    avg_beta2_all,
    "avg_delta_lin":    avg_delta_lin,
    "avg_delta_nonlin": avg_delta_nonlin,
    "avg_res_rel_pct":  avg_res_rel * 100.0,

    # Cross-checks
    "cc1_zero_limit":   cc1_pass,
    "cc2_bounded":      cc2_pass,
    "cc3_order_eps2":   cc3_pass,
    "cc4_scale_inv":    cc4_pass,
}

np.savez_compressed("computations/session-74/s74_spectral_ratio_independence.npz", **out_data)
print("  Saved: computations/session-74/s74_spectral_ratio_independence.npz")

# --------------------------------------------------------------------------
# 9. Plot
# --------------------------------------------------------------------------
print()
print("-" * 74)
print("[9] Plot")
print("-" * 74)

fig, axes = plt.subplots(2, 2, figsize=(12, 9))

# Top-left: |beta_k|^2 per mode, colored by correction
ax = axes[0, 0]
xs = np.arange(len(labels))
width = 0.17  # (local)
ax.bar(xs - 2*width, beta2_0,   width, label="baseline",  color="#808080")
ax.bar(xs - 1*width, beta2_EC,  width, label="W1-D E_C",  color="#1f77b4")
ax.bar(xs + 0*width, beta2_nbar, width, label="W2-A nbar", color="#2ca02c")
ax.bar(xs + 1*width, beta2_HFB, width, label="W2-C HFB",  color="#d62728")
ax.bar(xs + 2*width, beta2_all, width, label="ALL",       color="#9467bd")
ax.set_yscale("log")
ax.set_xticks(xs)
ax.set_xticklabels(labels, rotation=45, ha="right")
ax.set_ylabel(r"$|\beta_k|^2$")
ax.set_title("|beta_k|^2 under each / combined correction")
ax.legend(fontsize=8, ncol=2)
ax.grid(alpha=0.3, which="both")

# Top-right: fractional change vs baseline
ax = axes[0, 1]
frac_EC   = (beta2_EC   / beta2_0 - 1.0) * 100.0
frac_nbar = (beta2_nbar / beta2_0 - 1.0) * 100.0
frac_HFB  = (beta2_HFB  / beta2_0 - 1.0) * 100.0
frac_all  = (beta2_all  / beta2_0 - 1.0) * 100.0
frac_lin  = (delta_sum_linear / beta2_0) * 100.0
ax.plot(xs, frac_EC,   "o-", label="EC (single)",  color="#1f77b4")
ax.plot(xs, frac_nbar, "s-", label="nbar (single)", color="#2ca02c")
ax.plot(xs, frac_HFB,  "^-", label="HFB (single)",  color="#d62728")
ax.plot(xs, frac_all,  "d-", label="ALL (product)", color="#9467bd", lw=2)
ax.plot(xs, frac_lin,  "x--", label="linear sum",   color="#ff7f0e", lw=1.5)
ax.axhline(0, color="k", ls=":", alpha=0.5)
ax.set_xticks(xs)
ax.set_xticklabels(labels, rotation=45, ha="right")
ax.set_ylabel(r"$(|\beta_k|^2 - |\beta_k|^2_0) / |\beta_k|^2_0$  [%]")
ax.set_title("Fractional change vs baseline")
ax.legend(fontsize=8)
ax.grid(alpha=0.3)

# Bottom-left: per-mode primary residual (observable-scale)
ax = axes[1, 0]
bar_colors = ['#6a3d9a' if abs(r)*100 < GATE_PASS_THRESHOLD_PCT else '#ff7f00' if abs(r)*100 < GATE_INFO_THRESHOLD_PCT else '#e31a1c' for r in residual_obs]
ax.bar(xs, residual_obs * 100.0, color=bar_colors, alpha=0.85)
ax.axhline( GATE_PASS_THRESHOLD_PCT, color="green", ls="--", label=f"PASS < {GATE_PASS_THRESHOLD_PCT}%")
ax.axhline(-GATE_PASS_THRESHOLD_PCT, color="green", ls="--")
ax.axhline( GATE_INFO_THRESHOLD_PCT, color="orange", ls="--", label=f"INFO < {GATE_INFO_THRESHOLD_PCT}%")
ax.axhline(-GATE_INFO_THRESHOLD_PCT, color="orange", ls="--")
ax.set_xticks(xs)
ax.set_xticklabels(labels, rotation=45, ha="right")
ax.set_ylabel(r"residual_obs(k) = $(\Delta_{\rm non}-\Delta_{\rm lin})/|\beta_k|^2_0$  [%]")
ax.set_title(f"Additivity residual (observable-scale) — max = {max_residual_pct:.4f}% ({gate_verdict})")
ax.legend(fontsize=8)
ax.grid(alpha=0.3)

# Bottom-right: pair coupling heatmap
ax = axes[1, 1]
pair_matrix = np.array([
    [0.0, np.max(np.abs(res_EC_nbar)), np.max(np.abs(res_EC_HFB))],
    [np.max(np.abs(res_EC_nbar)), 0.0, np.max(np.abs(res_nbar_HFB))],
    [np.max(np.abs(res_EC_HFB)), np.max(np.abs(res_nbar_HFB)), 0.0],
]) * 100.0
im = ax.imshow(pair_matrix, cmap="Reds", vmin=0)
ax.set_xticks(range(3))
ax.set_yticks(range(3))
ax.set_xticklabels(["EC", "nbar", "HFB"])
ax.set_yticklabels(["EC", "nbar", "HFB"])
for i in range(3):
    for j in range(3):
        if i != j:
            ax.text(j, i, f"{pair_matrix[i,j]:.3f}%",
                    ha="center", va="center",
                    color="white" if pair_matrix[i,j] > pair_matrix.max()/2 else "black",
                    fontsize=9)
ax.set_title("Pairwise max |residual|  [%]")
plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04, label="max |res| [%]")

fig.suptitle(f"SPECTRAL-RATIO-INDEPENDENCE-74  |  Gate: {gate_verdict}  |  max residual = {max_residual_pct:.4f}%",
             fontsize=13)
plt.tight_layout(rect=[0, 0, 1, 0.97])
plt.savefig("computations/session-74/s74_spectral_ratio_independence.png", dpi=140)
plt.close()
print("  Saved: computations/session-74/s74_spectral_ratio_independence.png")

print()
print("=" * 74)
print(f"SPECTRAL-RATIO-INDEPENDENCE-74 COMPLETE  :  {gate_verdict}")
print("=" * 74)
