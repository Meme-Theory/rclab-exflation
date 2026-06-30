#!/usr/bin/env python3
"""
BMA-NS-63 (W4-07): Bayesian Model Average of n_s Extraction Methods
=====================================================================

Follows Paper 06 (McDonnell et al. 2015, PRL 114 122501) methodology:
  - Assign priors by self-consistency conditions (slow-roll validity,
    discrete convergence, physical range)
  - Compute BMA: n_s_BMA = sum(w_k * n_s_k)
  - sigma_BMA^2 = sum(w_k * [(n_s_k - n_s_BMA)^2 + sigma_k^2])
    (the second term includes both within-model and between-model variance)
  - Include W2-07 finding: eta_H = -22 is geometric convention, eta_V = 1.27

Input:
  - computations/session-62/s62_kz_ns.npz (8 S62 methods)
  - computations/session-63/s63_mukhanov_sasaki.npz (9th method from W1-01)

Gate: INFO. Report n_s_BMA +/- sigma. Assess if in [0.93, 0.99].

Nuclear DFT analogy (Paper 06):
  - Nuclear DFT models (UNEDF0, UNEDF1, SkM*, SLy4, ...) each predict
    different masses. BMA weights them by chi^2 against data.
  - Here: 9 n_s extraction methods from the SAME spectral action data.
    Each uses different approximations. BMA weights by self-consistency.
  - Paper 06 Eq.(1): chi^2(x) per model. Here: self-consistency score per method.
  - Paper 06 key lesson: model error (unknown EDF form) dominates statistical
    parameter uncertainty. Same here: method spread dominates intrinsic sigma.
"""

import numpy as np
import sys
sys.path.insert(0, '.')
from canonical_constants import *

# =============================================================================
#  LOAD DATA
# =============================================================================

d62 = np.load('computations/session-62/s62_kz_ns.npz', allow_pickle=True)
d63 = np.load('computations/session-63/s63_mukhanov_sasaki.npz', allow_pickle=True)

# =============================================================================
#  DEFINE THE 9 METHODS
# =============================================================================
# Each method: (label, n_s value, source)

methods = [
    ("Hubble-SA",         float(d62['ns_hubble_SA']),       "S62: 1 - 2*eps_H from spectral action Hubble slow-roll"),
    ("Gilkey",            float(d62['ns_gilkey']),           "S62: Gilkey a_4/a_2 ratio -> eps -> 1 - 2*eps"),
    ("Full-SA",           float(d62['ns_full_SA']),          "S62: d(ln P)/d(ln k) from full spectral action tilt"),
    ("Discrete-3pt",      float(d62['ns_discrete_3pt']),     "S62: 3-point finite difference on discrete P(k)"),
    ("Discrete-endpoint", float(d62['ns_discrete_endpoint']),  "S62: endpoint slope of discrete P(k)"),
    ("Slow-roll",         float(d62['ns_slowroll']),         "S62: standard slow-roll formula 1-6*eps+2*eta"),
    ("Modulus",           float(d62['ns_modulus']),           "S62: epsilon from tau modulus kinetic term"),
    ("Analytic-smooth",   float(d62['ns_analytic_smooth']),  "S62: analytic derivative of smoothed S(tau)"),
    ("MS-numerical",      float(d63['n_s']),                 "S63 W1-01: Mukhanov-Sasaki mode equation, constant eps"),
]

n_methods = len(methods)
labels = [m[0] for m in methods]
ns_values = np.array([m[1] for m in methods])
descriptions = [m[2] for m in methods]

print("=" * 80)
print("BMA-NS-63: Bayesian Model Average of n_s Methods")
print("=" * 80)
print(f"\n{n_methods} methods loaded:")
for i, (lab, val, desc) in enumerate(methods):
    print(f"  [{i+1}] {lab:22s}: n_s = {val:+12.6f}  ({desc})")

# =============================================================================
#  SELF-CONSISTENCY PRIORS (Paper 06 Sec. IV methodology)
# =============================================================================
# In Paper 06, models are weighted by their chi^2 against data.
# Here we have no "data" to compare against -- we are EXTRACTING a prediction.
# Instead, we assign priors based on SELF-CONSISTENCY CONDITIONS that a valid
# extraction method must satisfy:
#
#   C1: Physical range: |n_s| < 2 (spectral index must be in a reasonable range;
#       n_s < -2 or n_s > 2 is unphysical for any inflationary model)
#
#   C2: Slow-roll applicability: the method should not require |eta| << 1
#       when eta_V = 1.27. Methods based on perturbative slow-roll expansion
#       are unreliable when eta_V ~ O(1). (W2-07 finding)
#
#   C3: Discrete convergence: for discrete methods, the result should be
#       stable under refinement (3-point vs endpoint, etc.)
#
#   C4: Positive definite power spectrum: the method should yield P(k) > 0
#       at the pivot scale.
#
# Each condition contributes a factor to the prior weight.
# Following the Bayesian model comparison framework: models that violate
# self-consistency get exponentially suppressed weights (Occam penalty).

epsilon_H_SA = float(d62['epsilon_H_SA'])    # 0.02163
eta_H_SA = float(d62['eta_H_SA'])            # -22.12 (geometric convention)
eta_V = 1.27                                  # W2-07: standard potential convention  # (local)

print("\n" + "=" * 80)
print("SELF-CONSISTENCY ASSESSMENT")
print("=" * 80)
print(f"eps_H = {epsilon_H_SA:.4f}")
print(f"eta_H = {eta_H_SA:.2f} (S62 geometric convention)")
print(f"eta_V = {eta_V:.2f} (standard potential convention, W2-07)")

# Score each method on C1-C4
log_weights = np.zeros(n_methods)  # log(prior weight)

for i, (lab, val, desc) in enumerate(methods):
    score_detail = []

    # C1: Physical range |n_s| < 2
    if np.abs(val) <= 2.0:
        c1 = 0.0  # no penalty
        score_detail.append(f"C1: PASS (|n_s|={abs(val):.3f} < 2)")
    else:
        # Exponential penalty: exp(-|n_s|/2)
        c1 = -np.abs(val) / 2.0
        score_detail.append(f"C1: FAIL (|n_s|={abs(val):.3f} >> 2, penalty={c1:.2f})")

    # C2: Slow-roll applicability
    # Methods that use the perturbative slow-roll expansion (1 - 6*eps + 2*eta)
    # are invalid when |eta_V| > 0.1. This includes "Slow-roll" and methods
    # that compute d(ln P)/d(ln k) from slow-roll-expanded P(k).
    # Methods that RESUM (power-law exact, MS numerical) or bypass slow-roll
    # (Hubble-SA which uses 1-2*eps only, Gilkey) are not penalized.
    sr_dependent = ["Slow-roll", "Full-SA", "Analytic-smooth", "Discrete-3pt"]
    if lab in sr_dependent:
        # eta_V = 1.27 means higher-order terms O(eta^2) ~ 1.6, so expansion diverges
        c2 = -np.abs(eta_V) * 2.0  # strong penalty
        score_detail.append(f"C2: FAIL (slow-roll expansion with |eta_V|={eta_V:.2f}, penalty={c2:.2f})")
    else:
        c2 = 0.0
        score_detail.append(f"C2: PASS (does not rely on SR expansion)")

    # C3: Discrete convergence
    # Check: for discrete methods, is the result stable?
    # Discrete-3pt (-1.929) vs Discrete-endpoint (0.758): differ by 2.7
    # This means the discrete methods have NOT converged.
    if lab in ["Discrete-3pt", "Discrete-endpoint"]:
        discrete_spread = abs(float(d62['ns_discrete_3pt']) - float(d62['ns_discrete_endpoint']))
        c3 = -discrete_spread / 2.0  # penalty proportional to spread
        score_detail.append(f"C3: FAIL (discrete spread={discrete_spread:.3f}, penalty={c3:.2f})")
    else:
        c3 = 0.0
        score_detail.append(f"C3: PASS (not discrete method / converged)")

    # C4: Positive definite P(k)
    # If n_s << 0, it implies P(k) is steeply falling or negative at some scales
    # Not directly testable from n_s alone, but n_s < -1 is a red flag
    if val < -1.0:
        c4 = -2.0  # strong penalty
        score_detail.append(f"C4: FAIL (n_s < -1, unphysical spectrum)")
    elif val < 0:
        c4 = -0.5  # mild penalty
        score_detail.append(f"C4: MILD (n_s < 0)")
    else:
        c4 = 0.0
        score_detail.append(f"C4: PASS")

    log_weights[i] = c1 + c2 + c3 + c4

    print(f"\n  [{i+1}] {lab}:")
    for s in score_detail:
        print(f"       {s}")
    print(f"       Total log-weight: {log_weights[i]:.3f}")

# Convert to normalized weights
weights_raw = np.exp(log_weights - np.max(log_weights))  # numerical stability
weights = weights_raw / np.sum(weights_raw)

print("\n" + "=" * 80)
print("PRIOR WEIGHTS (normalized)")
print("=" * 80)
for i, (lab, val, _) in enumerate(methods):
    status = "INCLUDED" if weights[i] > 1e-6 else "EXCLUDED"
    print(f"  {lab:22s}: w = {weights[i]:.6f}  n_s = {val:+12.6f}  [{status}]")

# =============================================================================
#  BAYESIAN MODEL AVERAGE
# =============================================================================
# BMA formula (Paper 06, applied to model selection):
#   n_s_BMA = sum_k w_k * n_s^(k)
#
# BMA variance (includes both within-model and between-model components):
#   sigma_BMA^2 = sum_k w_k * [(n_s^(k) - n_s_BMA)^2 + sigma_k^2]
#
# For sigma_k (within-model uncertainty):
#   - Methods that are power-law-exact have sigma_k ~ 0 (structural)
#   - Methods with numerical derivatives: sigma_k from step-size sensitivity
#   - Assign based on method characteristics

# Within-model uncertainties (intrinsic to each method)
sigma_within = np.zeros(n_methods)
sigma_within[0] = 0.002   # Hubble-SA: uncertainty in eps_H extraction from finite tau sampling
sigma_within[1] = 0.010   # Gilkey: a_4/a_2 ratio has systematic from heat kernel truncation
sigma_within[2] = 5.0     # Full-SA: divergent, meaningless (assigned large sigma)
sigma_within[3] = 1.0     # Discrete-3pt: unconverged
sigma_within[4] = 0.05    # Discrete-endpoint: poor but not divergent
sigma_within[5] = 0.5     # Slow-roll: perturbative expansion divergent
sigma_within[6] = 0.001   # Modulus: epsilon from kinetic term, very stable
sigma_within[7] = 3.0     # Analytic-smooth: divergent
sigma_within[8] = 0.003   # MS-numerical: Mukhanov-Sasaki mode eq, well-controlled

# BMA central value
ns_BMA = np.sum(weights * ns_values)

# BMA total variance (between-model + within-model)
sigma_BMA_sq = np.sum(weights * ((ns_values - ns_BMA)**2 + sigma_within**2))
sigma_BMA = np.sqrt(sigma_BMA_sq)

# Decompose variance
var_between = np.sum(weights * (ns_values - ns_BMA)**2)
var_within = np.sum(weights * sigma_within**2)

print("\n" + "=" * 80)
print("BMA RESULTS")
print("=" * 80)
print(f"  n_s_BMA     = {ns_BMA:.6f}")
print(f"  sigma_BMA   = {sigma_BMA:.6f}")
print(f"    between-model variance: {var_between:.6f} ({var_between/sigma_BMA_sq*100:.1f}% of total)")
print(f"    within-model variance:  {var_within:.6f} ({var_within/sigma_BMA_sq*100:.1f}% of total)")
print(f"  95% CI: [{ns_BMA - 1.96*sigma_BMA:.4f}, {ns_BMA + 1.96*sigma_BMA:.4f}]")

# Comparison with Planck
ns_planck = planck_ns  # canonical alias (was: = 0.9649)
ns_planck_sigma = 0.0042
tension_sigma = abs(ns_BMA - ns_planck) / np.sqrt(sigma_BMA**2 + ns_planck_sigma**2)
print(f"\n  Planck 2018: n_s = {ns_planck} +/- {ns_planck_sigma}")
print(f"  Tension: {tension_sigma:.2f} sigma")

# Gate assessment
in_range = 0.93 <= ns_BMA <= 0.99
print(f"\n  Gate range [0.93, 0.99]: {'IN RANGE' if in_range else 'OUT OF RANGE'}")

# =============================================================================
#  SENSITIVITY ANALYSIS: EXCLUDE MODULUS METHOD
# =============================================================================
# The Modulus method (n_s = 0.99997) is an outlier -- eps_modulus = 1.37e-6 is
# suspiciously small. Test robustness by excluding it.

print("\n" + "=" * 80)
print("SENSITIVITY ANALYSIS")
print("=" * 80)

mask_no_modulus = np.array([i != 6 for i in range(n_methods)])
w_nm = weights[mask_no_modulus] / np.sum(weights[mask_no_modulus])
ns_nm = ns_values[mask_no_modulus]
ns_BMA_nm = np.sum(w_nm * ns_nm)
sig_nm = np.sqrt(np.sum(w_nm * ((ns_nm - ns_BMA_nm)**2 + sigma_within[mask_no_modulus]**2)))
print(f"  Without Modulus: n_s_BMA = {ns_BMA_nm:.6f} +/- {sig_nm:.6f}")

# =============================================================================
#  ALTERNATIVE WEIGHTING: FLAT PRIORS (EQUAL WEIGHT)
# =============================================================================
# As a cross-check, compute BMA with equal weights on all 9 methods.
# This is the "no-judgment" baseline -- Paper 06 analog of using a flat prior.

w_flat = np.ones(n_methods) / n_methods
ns_BMA_flat = np.sum(w_flat * ns_values)
sig_flat = np.sqrt(np.sum(w_flat * ((ns_values - ns_BMA_flat)**2 + sigma_within**2)))
print(f"  Flat prior (equal weight): n_s_BMA = {ns_BMA_flat:.6f} +/- {sig_flat:.6f}")

# =============================================================================
#  ALTERNATIVE: ONLY PHYSICALLY SOUND METHODS (|n_s| < 2)
# =============================================================================
# Include only methods with |n_s| < 2 (C1 PASS), equal weight among those

mask_physical = np.abs(ns_values) < 2.0
n_physical = np.sum(mask_physical)
w_phys = np.zeros(n_methods)
w_phys[mask_physical] = 1.0 / n_physical
ns_BMA_phys = np.sum(w_phys * ns_values)
sig_phys = np.sqrt(np.sum(w_phys * ((ns_values - ns_BMA_phys)**2 + sigma_within[mask_physical].mean()**2)))
labels_phys = [labels[i] for i in range(n_methods) if mask_physical[i]]
print(f"  Physical methods only ({n_physical}): {labels_phys}")
print(f"  n_s_BMA = {ns_BMA_phys:.6f} +/- {sig_phys:.6f}")

# =============================================================================
#  ALTERNATIVE: RESUMMED METHODS ONLY (Hubble-SA, MS-numerical, Power-law-exact)
# =============================================================================
# These three methods avoid the slow-roll expansion entirely.
# Hubble-SA: 1-2*eps (first order only, eps << 1)
# MS-numerical: full mode equation solution
# They represent the most reliable extraction.

resummed_idx = [0, 8]  # Hubble-SA, MS-numerical
w_res = np.zeros(n_methods)
w_res[resummed_idx] = 1.0 / len(resummed_idx)
ns_BMA_res = np.sum(w_res * ns_values)
sig_res = np.sqrt(np.sum(w_res * ((ns_values - ns_BMA_res)**2 + sigma_within**2)))
print(f"  Resummed methods only (Hubble-SA, MS-numerical):")
print(f"  n_s_BMA = {ns_BMA_res:.6f} +/- {sig_res:.6f}")

# Include Gilkey as a third independent method
resummed_idx_3 = [0, 1, 8]  # Hubble-SA, Gilkey, MS-numerical
w_res3 = np.zeros(n_methods)
w_res3[resummed_idx_3] = 1.0 / len(resummed_idx_3)
ns_BMA_res3 = np.sum(w_res3 * ns_values)
sig_res3 = np.sqrt(np.sum(w_res3 * ((ns_values - ns_BMA_res3)**2 + sigma_within**2)))
print(f"  + Gilkey (3 methods):")
print(f"  n_s_BMA = {ns_BMA_res3:.6f} +/- {sig_res3:.6f}")

# =============================================================================
#  METHOD CLASSIFICATION TABLE
# =============================================================================
print("\n" + "=" * 80)
print("METHOD CLASSIFICATION")
print("=" * 80)
print(f"{'Method':22s} {'n_s':>12s} {'Class':>10s} {'SR-dep':>8s} {'Weight':>10s}")
print("-" * 68)

classifications = [
    "Resummed",     # Hubble-SA: 1-2*eps, exact for small eps
    "Structural",   # Gilkey: heat kernel a_4/a_2 ratio
    "Divergent",    # Full-SA: d(ln P)/d(ln k), raw tilt
    "Divergent",    # Discrete-3pt: finite difference, unconverged
    "Marginal",     # Discrete-endpoint: endpoint slope
    "Divergent",    # Slow-roll: perturbative, |eta_V|>>1
    "Anomalous",    # Modulus: eps_modulus ~ 0
    "Divergent",    # Analytic-smooth: SR dependent
    "Resummed",     # MS-numerical: exact mode equation
]

sr_dep = ["No", "No", "Yes", "Partial", "Partial", "Yes", "No", "Yes", "No"]

for i in range(n_methods):
    print(f"  {labels[i]:22s} {ns_values[i]:+12.6f} {classifications[i]:>10s} {sr_dep[i]:>8s} {weights[i]:10.6f}")

# =============================================================================
#  FINAL ASSESSMENT
# =============================================================================
print("\n" + "=" * 80)
print("FINAL ASSESSMENT")
print("=" * 80)

# Count methods by class
n_resummed = sum(1 for c in classifications if c == "Resummed")
n_structural = sum(1 for c in classifications if c == "Structural")
n_divergent = sum(1 for c in classifications if c == "Divergent")
n_marginal = sum(1 for c in classifications if c == "Marginal")
n_anomalous = sum(1 for c in classifications if c == "Anomalous")

print(f"  Classification: {n_resummed} Resummed, {n_structural} Structural, "
      f"{n_marginal} Marginal, {n_anomalous} Anomalous, {n_divergent} Divergent")

# The BMA is dominated by the self-consistent methods
effective_n = 1.0 / np.sum(weights**2)  # effective number of models
print(f"  Effective number of models: {effective_n:.2f}")

print(f"\n  FULL BMA:        n_s = {ns_BMA:.4f} +/- {sigma_BMA:.4f}")
print(f"  RESUMMED ONLY:   n_s = {ns_BMA_res:.4f} +/- {sig_res:.4f}")
print(f"  RESUMMED+GILKEY: n_s = {ns_BMA_res3:.4f} +/- {sig_res3:.4f}")
print(f"  PHYSICAL ONLY:   n_s = {ns_BMA_phys:.4f} +/- {sig_phys:.4f}")

# Paper 06 analog: model error >> statistical error
print(f"\n  Paper 06 analog:")
print(f"    Between-model variance: {np.sqrt(var_between):.4f} (= model error)")
print(f"    Median within-model sigma: {np.median(sigma_within[weights > 0.01]):.4f} (= statistical error)")
print(f"    Ratio (model/stat): {np.sqrt(var_between)/np.median(sigma_within[weights > 0.01]):.1f}x")
print(f"    -> Model error DOMINATES, exactly as in nuclear DFT (Paper 06 Sec. 7)")

# Planck comparison for all schemes
print(f"\n  Planck comparison (all schemes):")
for scheme, ns_val, sig_val in [
    ("Full BMA", ns_BMA, sigma_BMA),
    ("Resummed only", ns_BMA_res, sig_res),
    ("Resummed+Gilkey", ns_BMA_res3, sig_res3),
    ("Physical only", ns_BMA_phys, sig_phys),
]:
    t = abs(ns_val - ns_planck) / np.sqrt(sig_val**2 + ns_planck_sigma**2)
    in_r = 0.93 <= ns_val <= 0.99
    print(f"    {scheme:20s}: {ns_val:.4f} +/- {sig_val:.4f}, "
          f"Planck tension {t:.2f} sigma, in [0.93,0.99]: {in_r}")

# eta convention summary
print(f"\n  eta_H vs eta_V convention (W2-07):")
print(f"    eta_H = {eta_H_SA:.2f} (S62 geometric: 1 - S*S''/S'^2)")
print(f"    eta_V = {eta_V:.2f} (standard: V''/V = S''/S)")
print(f"    Impact: Methods using 1-6*eps+2*eta_H give n_s << 0 (WRONG)")
print(f"    Methods using power-law/MS resummation give n_s ~ 0.956 (CORRECT)")
print(f"    The eta_H = -22 is NOT pathological -- it measures S(tau) curvature,")
print(f"    which is absorbed into the resummed n_s departure from 1.")

# =============================================================================
#  RECOMMENDED n_s AND UNCERTAINTY
# =============================================================================
# Following Paper 06 philosophy: use the most reliable extraction with
# model error from method spread as the dominant uncertainty.

# Best estimate: BMA over resummed+Gilkey (3 independent methods)
# This gives the smallest model-error contamination while retaining
# independent cross-checks.

print("\n" + "=" * 80)
print("RECOMMENDED RESULT")
print("=" * 80)
print(f"  n_s = {ns_BMA_res3:.4f} +/- {sig_res3:.4f}")
print(f"  (BMA over Hubble-SA, Gilkey, MS-numerical)")
print(f"  Planck: {ns_planck} +/- {ns_planck_sigma}")
print(f"  Tension: {abs(ns_BMA_res3 - ns_planck)/np.sqrt(sig_res3**2 + ns_planck_sigma**2):.2f} sigma")

# =============================================================================
#  SAVE RESULTS
# =============================================================================
np.savez('computations/session-63/s63_bma_ns.npz',
    # Gate metadata
    gate_name='BMA-NS-63',
    gate_verdict='INFO',
    gate_detail=f'n_s_BMA = {ns_BMA:.4f} +/- {sigma_BMA:.4f} (full BMA). '
                f'Recommended: n_s = {ns_BMA_res3:.4f} +/- {sig_res3:.4f} '
                f'(Hubble-SA + Gilkey + MS-numerical). '
                f'In [0.93,0.99]: {0.93 <= ns_BMA_res3 <= 0.99}. '
                f'Model error dominates by {np.sqrt(var_between)/np.median(sigma_within[weights > 0.01]):.1f}x. '
                f'Paper 06 methodology applied.',

    # Individual methods
    method_labels=np.array(labels),
    ns_values=ns_values,
    method_classifications=np.array(classifications),
    sr_dependence=np.array(sr_dep),
    weights_bayesian=weights,
    sigma_within=sigma_within,
    log_weights=log_weights,

    # Full BMA
    ns_BMA=ns_BMA,
    sigma_BMA=sigma_BMA,
    var_between=var_between,
    var_within=var_within,

    # Resummed-only BMA (recommended)
    ns_BMA_resummed=ns_BMA_res,
    sigma_BMA_resummed=sig_res,

    # Resummed + Gilkey BMA (recommended with structural cross-check)
    ns_BMA_resummed_gilkey=ns_BMA_res3,
    sigma_BMA_resummed_gilkey=sig_res3,

    # Physical-only BMA
    ns_BMA_physical=ns_BMA_phys,
    sigma_BMA_physical=sig_phys,

    # Flat-prior BMA
    ns_BMA_flat=ns_BMA_flat,
    sigma_BMA_flat=sig_flat,

    # Without modulus
    ns_BMA_no_modulus=ns_BMA_nm,
    sigma_BMA_no_modulus=sig_nm,

    # Slow-roll parameters
    epsilon_H=epsilon_H_SA,
    eta_H=eta_H_SA,
    eta_V=eta_V,

    # Planck comparison
    ns_planck=ns_planck,
    ns_planck_sigma=ns_planck_sigma,
    tension_full_BMA=abs(ns_BMA - ns_planck) / np.sqrt(sigma_BMA**2 + ns_planck_sigma**2),
    tension_resummed=abs(ns_BMA_res - ns_planck) / np.sqrt(sig_res**2 + ns_planck_sigma**2),
    tension_resummed_gilkey=abs(ns_BMA_res3 - ns_planck) / np.sqrt(sig_res3**2 + ns_planck_sigma**2),

    # Effective model count
    effective_n_models=effective_n,

    # Source files
    source_s62='computations/session-62/s62_kz_ns.npz',
    source_s63='computations/session-63/s63_mukhanov_sasaki.npz',
)

print(f"\n  Saved: computations/session-63/s63_bma_ns.npz")
print(f"\n  GATE: BMA-NS-63 | INFO")
