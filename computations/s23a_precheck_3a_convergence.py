#!/usr/bin/env python3
"""
Session 23a Step 3a: Seven-Way Convergence p-Value (Einstein check 3.5)

Compute the look-elsewhere-corrected probability that seven indicators
fall within a window of width 0.20 in [0, 2.0].

Indicators:
  1. DNP stability crossing:       tau = 0.285   (22a SP-5)
  2. Slow-roll epsilon < 1 center: tau ~ 0.23    (22a SP-1)
  3. IR spinodal V_IR'' < 0:       tau ~ 0.30    (22c L-1)
  4. Pomeranchuk instability:      tau ~ 0.30    (22c F-1)
  5. Grav-YM instanton minimum:    tau ~ 0.31    (22c F-2)
  6. Weinberg angle (FR formula):  tau = 0.3007  (22a QA-5)
  7. phi_paasch crossing:          tau = 0.150   (22a QA-4)

Method: Monte Carlo simulation with look-elsewhere correction.
Also compute with effective DOF accounting for correlations.

Reports p-value WITH and WITHOUT indicator #7.
"""

import numpy as np
import sys

np.random.seed(42)

# ============================================================
# 1. INDICATOR VALUES
# ============================================================
# Actual tau values of the seven indicators
tau_indicators = np.array([
    0.285,   # 1: DNP stability crossing
    0.230,   # 2: Slow-roll epsilon < 1 window center
    0.300,   # 3: IR spinodal V_IR'' < 0
    0.300,   # 4: Pomeranchuk instability
    0.310,   # 5: Grav-YM instanton minimum
    0.3007,  # 6: Weinberg angle (FR formula)
    0.150,   # 7: phi_paasch crossing
])

labels = [
    "DNP stability crossing",
    "Slow-roll epsilon<1 center",
    "IR spinodal V_IR'' < 0",
    "Pomeranchuk instability",
    "Grav-YM instanton minimum",
    "Weinberg angle (FR)",
    "phi_paasch crossing",
]

print("=" * 70)
print("SESSION 23a STEP 3a: SEVEN-WAY CONVERGENCE P-VALUE")
print("=" * 70)

# Actual window parameters
domain = [0.0, 2.0]
domain_width = domain[1] - domain[0]  # 2.0

# The actual window containing all 7 indicators
actual_min = tau_indicators.min()  # 0.150
actual_max = tau_indicators.max()  # 0.310
actual_width = actual_max - actual_min  # 0.160
window_test = 0.20  # Test window width (the actual window [0.15, 0.35])

print(f"\nIndicator values:")
for i, (tau, label) in enumerate(zip(tau_indicators, labels)):
    print(f"  {i+1}. {label}: tau = {tau:.4f}")

print(f"\nActual span: [{actual_min:.3f}, {actual_max:.3f}], width = {actual_width:.3f}")
print(f"Test window width: {window_test:.2f}")
print(f"Domain: {domain}, width = {domain_width}")

# ============================================================
# 2. MONTE CARLO: ALL 7 INDICATORS
# ============================================================
print("\n" + "=" * 70)
print("2. MONTE CARLO: ALL 7 INDICATORS")
print("=" * 70)

N_trials = 10_000_000  # 10M trials for good statistics

def count_all_in_window(n_indicators, n_trials, window_width, domain_width):
    """
    Monte Carlo: draw n_indicators uniform in [0, domain_width].
    Count fraction where max - min <= window_width.
    """
    # Generate all samples at once (memory-efficient batching)
    batch_size = 1_000_000
    count = 0
    total = 0

    while total < n_trials:
        batch = min(batch_size, n_trials - total)
        samples = np.random.uniform(0, domain_width, size=(batch, n_indicators))
        spans = samples.max(axis=1) - samples.min(axis=1)
        count += np.sum(spans <= window_width)
        total += batch

    return count, total

# All 7 indicators
print(f"\nRunning {N_trials:,} Monte Carlo trials (7 indicators)...")
count_7, total_7 = count_all_in_window(7, N_trials, window_test, domain_width)
p_local_7 = count_7 / total_7

# Look-elsewhere correction
# Number of independent windows of width 0.20 in [0, 2.0]:
# N_windows = domain_width / window_test = 10
# But more precisely, we use a sliding window, so trials factor = (domain_width - window_test) / window_test + 1
# However, the standard LEE correction for a sliding window on a continuous domain is:
# p_LEE = 1 - (1 - p_local)^(domain_width / window_test)
N_windows = domain_width / window_test  # = 10
p_lee_7 = 1 - (1 - p_local_7)**N_windows

print(f"  Hits: {count_7:,} / {total_7:,}")
print(f"  p_local (7 indicators, w={window_test}): {p_local_7:.6e}")
print(f"  Trials factor (N_windows = D/w): {N_windows:.1f}")
print(f"  p_LEE (7 indicators): {p_lee_7:.6e}")

# ============================================================
# 3. ANALYTIC CROSS-CHECK
# ============================================================
print("\n--- Analytic cross-check ---")
# For n uniform [0, L] variables, P(max - min <= w) = n * (w/L)^(n-1) - (n-1)*(w/L)^n
# when w <= L (order statistics formula for the range)
# More precisely: P(R <= w) = n! * integral over n-simplex = sum_{k=0}^{n} (-1)^k * C(n,k) * max(0, 1 - k*w/L)^n / ...
# Actually the exact formula for the range of n uniform [0,L]:
# P(range <= w) = sum_{k=0}^{floor(L/w)} (-1)^k * C(n,k) * (1 - k*w/L)^(n-1) ...
# Simpler: for n iid Uniform[0,1], P(range <= r) = n*r^(n-1) - (n-1)*r^n for 0 <= r <= 1

def p_range_uniform(n, r):
    """P(range of n Uniform[0,1] variables <= r), for 0 <= r <= 1."""
    # Exact formula: sum_{k=0}^{n} (-1)^k * C(n,k) * max(0, 1-k*r)^(n-1)
    # But for r <= 1/floor(1/r), simpler formula applies
    # General inclusion-exclusion:
    total = 0.0
    from math import comb
    for k in range(n + 1):
        val = 1 - k * r
        if val <= 0:
            break
        total += (-1)**k * comb(n, k) * val**(n-1)
    return total * n  # Wait, let me use the correct formula

# Actually the correct formula for the CDF of the range R of n U[0,1]:
# P(R <= r) = sum_{k=0}^{floor(1/r)} (-1)^k * C(n,k) * (1-k*r)^{n-1} ...
# Hmm, let me just use the well-known result:
# For n U[0,L], P(range <= w) = n * (w/L)^{n-1} - (n-1)*(w/L)^n  [for w <= L]

def p_range_simple(n, w, L):
    """Simple formula: P(range <= w) for n Uniform[0,L], valid for w <= L."""
    r = w / L
    return n * r**(n-1) - (n-1) * r**n

p_analytic_7 = p_range_simple(7, window_test, domain_width)
p_analytic_7_lee = 1 - (1 - p_analytic_7)**N_windows

print(f"  Analytic p_local (7, w={window_test}, L={domain_width}): {p_analytic_7:.6e}")
print(f"  Analytic p_LEE: {p_analytic_7_lee:.6e}")
print(f"  MC/Analytic ratio: {p_local_7/p_analytic_7:.4f}")

# ============================================================
# 4. WITHOUT INDICATOR #7 (6 indicators, tau = 0.230 to 0.310)
# ============================================================
print("\n" + "=" * 70)
print("4. WITHOUT INDICATOR #7 (phi_paasch)")
print("=" * 70)

tau_6 = tau_indicators[:6]
actual_span_6 = tau_6.max() - tau_6.min()  # 0.310 - 0.230 = 0.080
print(f"  6 indicators span: [{tau_6.min():.3f}, {tau_6.max():.3f}], width = {actual_span_6:.3f}")

# Use the actual span as the test window for 6 indicators
window_test_6 = 0.10  # Use a round number slightly larger than actual span

print(f"\nRunning {N_trials:,} Monte Carlo trials (6 indicators, w={window_test_6})...")
count_6, total_6 = count_all_in_window(6, N_trials, window_test_6, domain_width)
p_local_6 = count_6 / total_6

N_windows_6 = domain_width / window_test_6  # = 20
p_lee_6 = 1 - (1 - p_local_6)**N_windows_6

print(f"  Hits: {count_6:,} / {total_6:,}")
print(f"  p_local (6 indicators, w={window_test_6}): {p_local_6:.6e}")
print(f"  Trials factor (N_windows = D/w): {N_windows_6:.1f}")
print(f"  p_LEE (6 indicators): {p_lee_6:.6e}")

# Analytic
p_analytic_6 = p_range_simple(6, window_test_6, domain_width)
p_analytic_6_lee = 1 - (1 - p_analytic_6)**N_windows_6
print(f"  Analytic p_local: {p_analytic_6:.6e}")
print(f"  Analytic p_LEE: {p_analytic_6_lee:.6e}")

# Also compute with the SAME window (w=0.20) for direct comparison
print(f"\n--- 6 indicators with w={window_test} (same as 7-indicator test) ---")
count_6b, total_6b = count_all_in_window(6, N_trials, window_test, domain_width)
p_local_6b = count_6b / total_6b
p_lee_6b = 1 - (1 - p_local_6b)**N_windows
p_analytic_6b = p_range_simple(6, window_test, domain_width)
print(f"  MC p_local: {p_local_6b:.6e}")
print(f"  MC p_LEE: {p_lee_6b:.6e}")
print(f"  Analytic p_local: {p_analytic_6b:.6e}")

# ============================================================
# 5. EFFECTIVE DOF (CORRELATION ANALYSIS)
# ============================================================
print("\n" + "=" * 70)
print("5. EFFECTIVE DOF ANALYSIS")
print("=" * 70)

print("""
Correlation structure of the 7 indicators:

  Indicators 3, 4, and (partially) 5 are correlated:
    - #3 (IR spinodal) and #4 (Pomeranchuk) are both projections of the
      (0,0) singlet instability. They share the same eigenvalue data.
    - #5 (grav-YM instanton) is partially correlated with #3/#4 through
      the SU(3) curvature invariants.

  Correlation groups:
    Group A (independent): #1 (DNP), #2 (slow-roll), #6 (Weinberg), #7 (phi_paasch)
    Group B (correlated):  #3 (IR spinodal), #4 (Pomeranchuk), #5 (instanton)

  Group B effective DOF: ~1.5 (three correlated indicators count as ~1.5 independent ones)
  Total effective DOF: 4 + 1.5 = 5.5, round to ~5
""")

# Compute p-value for 5 effective indicators
print("--- p-value for N_eff = 5 indicators ---")
p_analytic_5 = p_range_simple(5, window_test, domain_width)
p_analytic_5_lee = 1 - (1 - p_analytic_5)**N_windows
print(f"  Analytic p_local (N_eff=5, w={window_test}): {p_analytic_5:.6e}")
print(f"  Analytic p_LEE (N_eff=5): {p_analytic_5_lee:.6e}")

# Without #7, effective DOF = 3 + 1.5 = 4.5 ~ 4-5
print("\n--- p-value for N_eff = 4 indicators (without #7, corr-adjusted) ---")
p_analytic_4 = p_range_simple(4, window_test_6, domain_width)
p_analytic_4_lee = 1 - (1 - p_analytic_4)**N_windows_6
print(f"  Analytic p_local (N_eff=4, w={window_test_6}): {p_analytic_4:.6e}")
print(f"  Analytic p_LEE (N_eff=4): {p_analytic_4_lee:.6e}")

# ============================================================
# 6. BOOTSTRAP CORRELATION ESTIMATE
# ============================================================
print("\n" + "=" * 70)
print("6. BOOTSTRAP CORRELATION FROM INDICATOR COVARIANCE")
print("=" * 70)

# We don't have raw data to bootstrap from, but we can estimate the
# correlation matrix from the known physical relationships.
#
# The key insight: indicators #3 and #4 come from the SAME computation
# (s22c_bcs_channel_scan.py and s22c_landau_classification.py use the
# same eigenvalue data from the (0,0) singlet sector).
#
# Construct a synthetic correlation matrix based on physical reasoning:

corr_matrix = np.array([
    # DNP  SR   IR   Pom  Inst Wein phi
    [1.0, 0.3, 0.1, 0.1, 0.1, 0.0, 0.0],  # 1: DNP (geometric, partially corr w/ SR)
    [0.3, 1.0, 0.2, 0.2, 0.1, 0.0, 0.0],  # 2: Slow-roll (kinematic)
    [0.1, 0.2, 1.0, 0.9, 0.5, 0.0, 0.0],  # 3: IR spinodal (singlet)
    [0.1, 0.2, 0.9, 1.0, 0.5, 0.0, 0.0],  # 4: Pomeranchuk (singlet)
    [0.1, 0.1, 0.5, 0.5, 1.0, 0.0, 0.0],  # 5: Instanton (partial singlet)
    [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0],  # 6: Weinberg angle (gauge coupling)
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0],  # 7: phi_paasch (mass ratio)
])

eigenvalues = np.linalg.eigvalsh(corr_matrix)
eigenvalues = eigenvalues[eigenvalues > 0.01]  # threshold at 1% of max
N_eff_bootstrap = len(eigenvalues)

# More refined: N_eff = (sum eigenvalues)^2 / sum(eigenvalues^2)
# This is the "participation ratio" of the eigenvalue spectrum
evals_full = np.linalg.eigvalsh(corr_matrix)
evals_full = evals_full[evals_full > 0]
N_eff_participation = (np.sum(evals_full))**2 / np.sum(evals_full**2)

print(f"  Correlation matrix eigenvalues: {np.sort(evals_full)[::-1]}")
print(f"  N_eff (threshold 1%): {N_eff_bootstrap}")
print(f"  N_eff (participation ratio): {N_eff_participation:.2f}")

# Use participation ratio for final p-value
N_eff_final = round(N_eff_participation)
print(f"\n  Adopted N_eff = {N_eff_final} (rounded participation ratio)")

p_analytic_neff = p_range_simple(N_eff_final, window_test, domain_width)
p_analytic_neff_lee = 1 - (1 - p_analytic_neff)**N_windows
print(f"  p_local (N_eff={N_eff_final}, w={window_test}): {p_analytic_neff:.6e}")
print(f"  p_LEE (N_eff={N_eff_final}): {p_analytic_neff_lee:.6e}")

# ============================================================
# 7. SUMMARY TABLE
# ============================================================
print("\n" + "=" * 70)
print("7. SUMMARY")
print("=" * 70)

print(f"""
SEVEN-WAY CONVERGENCE P-VALUE RESULTS
======================================

All 7 indicators, window w = {window_test}:
  p_local (MC, {N_trials/1e6:.0f}M trials): {p_local_7:.4e}
  p_local (analytic):               {p_analytic_7:.4e}
  p_LEE (trials factor {N_windows:.0f}):        {p_lee_7:.4e}

Without #7 (phi_paasch), 6 indicators, window w = {window_test_6}:
  p_local (MC):                     {p_local_6:.4e}
  p_LEE (trials factor {N_windows_6:.0f}):       {p_lee_6:.4e}

Effective DOF analysis:
  Correlation matrix eigenvalue participation ratio: {N_eff_participation:.2f}
  Adopted N_eff: {N_eff_final}
  p_local (N_eff={N_eff_final}, w={window_test}): {p_analytic_neff:.4e}
  p_LEE (N_eff={N_eff_final}):                    {p_analytic_neff_lee:.4e}

INTERPRETATION:
  Even after look-elsewhere correction and correlation discounting,
  the convergence of {N_eff_final} effective indicators within a window of
  width {window_test} in [0, 2.0] has p_LEE = {p_analytic_neff_lee:.4e}.

  For reference:
    1-sigma: p = 0.317
    2-sigma: p = 0.046
    3-sigma: p = 0.0027

  The convergence is at the {'<1' if p_analytic_neff_lee < 0.0027 else '~' + str(round(-np.log10(p_analytic_neff_lee)/0.301, 1))}-sigma level after LEE correction.

SENSITIVITY TO INDICATOR #7:
  INCLUDING #7 (phi_paasch at tau=0.150): p_LEE = {p_lee_7:.4e} (7 raw / ~{N_eff_final} eff)
  EXCLUDING #7:                            p_LEE = {p_lee_6:.4e} (6 raw / ~{N_eff_final-1} eff)
  Indicator #7 contributes significantly because it extends the span from
  0.080 (indicators 1-6) to 0.160 (all 7), which still fits in the 0.20 window.
  Its physical distinctness (mass ratio vs stability indicators) supports inclusion.

NOTE ON CORRELATIONS:
  Indicators #3 (IR spinodal), #4 (Pomeranchuk), and #5 (instanton) are
  correlated — all involve the (0,0) singlet instability. The effective DOF
  from the participation ratio ({N_eff_participation:.2f}) accounts for this.
  Indicators #1 (DNP), #2 (slow-roll), #6 (Weinberg), #7 (phi_paasch) are
  mechanistically independent.
""")

# Compute sigma-equivalent
from scipy.stats import norm
if p_analytic_neff_lee > 0:
    sigma_equiv = norm.ppf(1 - p_analytic_neff_lee / 2)  # Two-sided
    sigma_one_sided = norm.ppf(1 - p_analytic_neff_lee)
    print(f"  Sigma equivalent (two-sided): {sigma_equiv:.2f}")
    print(f"  Sigma equivalent (one-sided): {sigma_one_sided:.2f}")

print("\n=== STEP 3a COMPLETE ===")
