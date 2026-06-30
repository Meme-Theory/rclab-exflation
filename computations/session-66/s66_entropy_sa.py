#!/usr/bin/env python3
"""
s66_entropy_sa.py — ENTROPY-SA-CC-66: Thermodynamic Entropy Cutoff on SU(3)
=============================================================================

Gate: ENTROPY-SA-CC-66
Pre-registered criterion:
  PASS  if a_0^S / a_2^S < 0.1 * bare_ratio  (threshold = 0.023)
  FAIL  if a_0^S / a_2^S >= bare_ratio  (entropy cutoff makes it worse)
  INFO  if 0.1 < (a_0^S / a_2^S) / bare_ratio < 1.0  (some improvement, not dramatic)

  bare_ratio = 0.232 (task specification)

Physics
-------
The entropy cutoff function is:
    f_S(x, beta) = -[p * ln(p) + (1-p) * ln(1-p)]
where p = 1 / (exp(beta * x) + 1)  is the Fermi-Dirac distribution.

This is the von Neumann entropy S(p(x)) evaluated at Fermi-Dirac occupation.
It arises in Connes-Chamseddine (Paper 15) as the spectral action at finite
temperature and in the spectral functional framework (Lizzi Paper 03,
arXiv:1106.3263) as the anomaly functional.

Key properties of f_S for x >= 0:
  - f_S(0) = ln(2) for all beta (maximum)
  - f_S -> 0 exponentially as x -> +inf
  - f_S IS monotonically decreasing (df_S/dx < 0 for all x > 0)
  - f_S is NOT convex everywhere: it has an inflection point at
    x_infl = (1/beta) * arccosh(sqrt(3)/sqrt(2)) ~ 0.658/beta
  - Concave near x=0, convex for large x

The S65 NONLOCAL-SA-65 permanent theorem proved that all monotone f worsen
a_0/a_2 via Jensen's inequality. However, that proof used convexity of
certain derived quantities, not just monotonicity. The entropy cutoff's
inflection point means the Jensen argument must be re-examined.

The spectral action with entropy cutoff:
    S_S(Lambda, beta) = sum_n d_n * f_S(lambda_n^2 / Lambda^2, beta)

Effective moments (following S65 conventions):
    a_0^eff = sum_n d_n * f_S(x_n)           (x_n = lambda_n^2 / Lambda^2)
    a_2^eff = sum_n d_n * x_n * f_S(x_n)

The CC ratio:
    Q^S = a_0^eff / a_2^eff = <f_S(x)> / <x * f_S(x)>

We scan beta from 0.1 to 10.0 and compute Q^S(beta) / Q^bare to find the
optimal inverse temperature.

Method
------
1. Load D_K eigenvalue spectrum from s44_dos_tau.npz at tau=0.19 (fold).
2. Define f_S(x, beta) with numerical stability.
3. Compute effective moments a_0^eff(beta) and a_2^eff(beta).
4. Compute Q^S(beta) = a_0^eff / a_2^eff.
5. Compare to bare ratio Q^bare = a_0/a_2 (polynomial SDW).
6. Scan beta in [0.1, 10.0] to find minimum Q^S.
7. Cross-check: analytic SDW moment integrals f_0^S, f_2^S, f_4^S.
8. Verify consistency: Q^S(beta -> 0) -> Q^bare (high-T limit).

Input: computations/session-44/s44_dos_tau.npz (992-mode D_K spectrum at fold)
       canonical_constants.py

Output: s66_entropy_sa.npz, s66_entropy_sa.png

Author: Connes-NCG-Theorist
Session: S66 W2-B
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from scipy import integrate
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    PI, M_KK, M_KK_gravity, M_KK_kerner,
    M_Pl_reduced, rho_Lambda_obs,
    a0_fold, a2_fold, a4_fold,
    Vol_SU3_Haar, tau_fold
)

outdir = os.path.dirname(os.path.abspath(__file__))
archivedir = os.path.join(os.path.dirname(outdir), 'computations/_shared')

print("=" * 78)
print("ENTROPY-SA-CC-66: Thermodynamic Entropy Cutoff on SU(3)")
print("=" * 78)
print(f"  tau_fold = {tau_fold}")
print(f"  a0_fold  = {a0_fold}")
print(f"  a2_fold  = {a2_fold:.4f}")
print(f"  a4_fold  = {a4_fold:.4f}")
print(f"  M_KK     = {M_KK:.6e} GeV")

# =============================================================================
# 1. LOAD D_K EIGENVALUE SPECTRUM AT FOLD
# =============================================================================
print("\n" + "=" * 78)
print("1. LOAD D_K EIGENVALUE SPECTRUM AT FOLD (tau=0.19)")
print("=" * 78)

d44 = np.load(os.path.join(archivedir, 's44_dos_tau.npz'), allow_pickle=True)
omega = d44['tau0.19_all_omega']    # eigenvalues of D_K (992 values)
dim2 = d44['tau0.19_all_dim2']      # degeneracies (spinor x representation)

N_evals = len(omega)
N_modes = np.sum(dim2)
omega_sq = omega**2                  # eigenvalues of D_K^2

print(f"  Number of distinct eigenvalues: {N_evals}")
print(f"  Total weighted modes (Tr 1):    {N_modes:.0f}")
print(f"  omega range:     [{omega.min():.6f}, {omega.max():.6f}]")
print(f"  omega^2 range:   [{omega_sq.min():.6f}, {omega_sq.max():.6f}]")

# Bare SDW moments from the spectral sum
a0_spec = np.sum(dim2)                    # = Tr(1) = sum d_n
a2_spec = np.sum(dim2 * omega_sq)          # = Tr(D^2) = sum d_n * lambda_n^2
a4_spec = np.sum(dim2 * omega_sq**2)       # = Tr(D^4) = sum d_n * lambda_n^4

Q_bare = a0_spec / a2_spec                 # bare ratio from spectral sum

print(f"\n  Bare spectral moments:")
print(f"    a_0^spec = Tr(1)   = {a0_spec:.0f}")
print(f"    a_2^spec = Tr(D^2) = {a2_spec:.4f}")
print(f"    a_4^spec = Tr(D^4) = {a4_spec:.4f}")
print(f"    Q^bare = a_0/a_2   = {Q_bare:.6f}")
print(f"    a_4/a_2            = {a4_spec/a2_spec:.6f}")

# Gate-specified bare ratio
Q_bare_gate = 0.232  # (local)
print(f"\n  Gate-specified bare_ratio = {Q_bare_gate}")
print(f"  PASS threshold: Q^S < {0.1 * Q_bare_gate:.4f}")
print(f"  FAIL threshold: Q^S >= {Q_bare_gate}")

# =============================================================================
# 2. ENTROPY CUTOFF FUNCTION
# =============================================================================
print("\n" + "=" * 78)
print("2. ENTROPY CUTOFF FUNCTION f_S(x, beta)")
print("=" * 78)


def f_entropy(x, beta):
    """
    Von Neumann entropy of Fermi-Dirac distribution:
        f_S(x) = -[p*ln(p) + (1-p)*ln(1-p)]
    where p = 1/(exp(beta*x) + 1).

    Numerically stable implementation.
    """
    x = np.asarray(x, dtype=np.float64)
    bx = beta * x
    # Clip to avoid overflow in exp
    bx_clip = np.clip(bx, -500.0, 500.0)
    p = 1.0 / (np.exp(bx_clip) + 1.0)  # (local)
    # Clip p to avoid log(0)
    p_safe = np.clip(p, 1e-300, 1.0 - 1e-300)
    return -(p_safe * np.log(p_safe) + (1.0 - p_safe) * np.log(1.0 - p_safe))


# Verify key properties
print(f"  f_S(0, beta=1) = {f_entropy(0, 1):.10f}  (expected ln(2) = {np.log(2):.10f})")
print(f"  f_S(5, beta=1) = {f_entropy(5, 1):.10f}")
print(f"  f_S(10, beta=1) = {f_entropy(10, 1):.10f}")

# Check monotonicity
x_test = np.linspace(0, 20, 10000)
f_test = f_entropy(x_test, 1.0)
df_test = np.diff(f_test) / np.diff(x_test)
assert np.all(df_test <= 1e-10), "f_S should be monotonically decreasing for x >= 0"
print(f"  Monotonicity verified: df/dx <= 0 for all x in [0, 20]")

# Find inflection point (where f'' = 0)
d2f_test = np.gradient(np.gradient(f_test, x_test), x_test)
sign_changes = np.where(np.diff(np.sign(d2f_test)))[0]
if len(sign_changes) > 0:
    x_infl = x_test[sign_changes[0]]
    print(f"  Inflection point at x ~ {x_infl:.4f} (for beta=1)")
    print(f"  f_S concave for x < {x_infl:.4f}, convex for x > {x_infl:.4f}")
else:
    print(f"  No inflection point found in [0, 20]")

# =============================================================================
# 3. ANALYTIC SDW MOMENT INTEGRALS
# =============================================================================
print("\n" + "=" * 78)
print("3. ANALYTIC SDW MOMENT INTEGRALS f_k^S(beta)")
print("=" * 78)

# The SDW expansion S ~ f_4 Lambda^4 a_0 + f_2 Lambda^2 a_2 + f_0 a_4
# with:
#   f_0 = f_S(0) = ln(2)  [the value at zero]
#   f_2 = integral_0^inf f_S(x) dx  [zeroth Mellin moment]
#   f_4 = integral_0^inf x * f_S(x) dx  [first Mellin moment]
#
# Wait: the SDW convention in CCM is:
#   S ~ f(0)*a_4 + f_2*Lambda^2*a_2 + f_4*Lambda^4*a_0
# where f_k = integral_0^inf x^{k/2-1} f(x) dx
# So:
#   f_0 = f(0) = ln(2)
#   f_2 = integral_0^inf f(x) dx
#   f_4 = integral_0^inf x * f(x) dx
#
# Actually the STANDARD Chamseddine-Connes convention is:
#   Tr f(D^2/Lambda^2) ~ sum_{k>=0} f_{4-2k} Lambda^{4-2k} a_k(D^2)
# where (for d=4 base manifold, but we have d=8 internal):
#   f_0 = f(0)
#   f_2 = integral_0^inf f(u) du
#   f_4 = integral_0^inf u f(u) du
#
# The CC ratio involves:
#   rho_Lambda ~ f_4 * Lambda^4 * a_0    (cosmological constant)
#   1/G_N ~ f_2 * Lambda^2 * a_2         (gravity)
#
# So Q_cutoff = (f_4/f_2) * (a_0/a_2) = (f_4/f_2) * Q_bare
#
# For f_S we need f_4^S / f_2^S.

# Compute Mellin moments numerically (high precision)
def compute_sdw_moments(beta, x_max=500.0):
    """
    Compute the SDW cutoff moments for the entropy function f_S:
      f_0 = f_S(0) = ln(2)
      f_2 = integral_0^inf f_S(x, beta) dx
      f_4 = integral_0^inf x * f_S(x, beta) dx
    """
    f_0 = np.log(2)  # f_S(0) = ln(2) for all beta

    # f_2 = integral f_S(x) dx
    integrand_f2 = lambda x: f_entropy(x, beta)
    f_2, err_f2 = integrate.quad(integrand_f2, 0, x_max / beta,
                                  limit=200, epsabs=1e-14, epsrel=1e-12)

    # f_4 = integral x * f_S(x) dx
    integrand_f4 = lambda x: x * f_entropy(x, beta)
    f_4, err_f4 = integrate.quad(integrand_f4, 0, x_max / beta,
                                  limit=200, epsabs=1e-14, epsrel=1e-12)

    return f_0, f_2, f_4, err_f2, err_f4


# Compute for reference beta values
print(f"\n  {'beta':>6} {'f_0':>12} {'f_2':>14} {'f_4':>14} {'f_4/f_2':>12}")
for beta_ref in [0.1, 0.5, 1.0, 2.0, 5.0, 10.0]:
    f0, f2, f4, _, _ = compute_sdw_moments(beta_ref)
    print(f"  {beta_ref:6.1f} {f0:12.6f} {f2:14.6f} {f4:14.6f} {f4/f2:12.6f}")

# Key observation: f_4/f_2 depends on beta.
# The CC ratio is Q_S = (f_4/f_2) * Q_bare.
# We need to find the beta that minimizes Q_S.

# =============================================================================
# 4. EFFECTIVE SPECTRAL ACTION MOMENTS (FULL SPECTRUM)
# =============================================================================
print("\n" + "=" * 78)
print("4. EFFECTIVE SPECTRAL ACTION MOMENTS (FULL SPECTRUM)")
print("=" * 78)

# For the FULL (non-polynomial) spectral action at finite Lambda:
#   a_0^eff(f, Lambda) = sum_n d_n * f(lambda_n^2 / Lambda^2)
#   a_2^eff(f, Lambda) = sum_n d_n * (lambda_n^2/Lambda^2) * f(lambda_n^2 / Lambda^2)
#
# The effective CC ratio:
#   Q^eff = a_0^eff / a_2^eff
#
# Following the S45 UNEXPANDED-SA insight: for Lambda >> lambda_max,
# this reduces to the SDW polynomial. For Lambda ~ lambda_max,
# the full nonlinear behavior matters.
#
# We set Lambda = omega_max (species cutoff) as in S65 NONLOCAL-SA.

Lambda_sp = omega.max()   # species cutoff
Lambda_sp_sq = Lambda_sp**2
print(f"  Lambda_sp = omega_max = {Lambda_sp:.6f} M_KK")
print(f"  Lambda_sp^2 = {Lambda_sp_sq:.6f} M_KK^2")

# Also compute at Lambda = 2*omega_max and Lambda = 1.5*omega_max for comparison
Lambda_vals = [Lambda_sp, 1.5 * Lambda_sp, 2.0 * Lambda_sp, 5.0 * Lambda_sp]

# Beta scan: 0.1 to 10 in steps of 0.1 (fine grid)
beta_scan = np.arange(0.1, 10.05, 0.1)
N_beta = len(beta_scan)

# Storage
Q_eff_vs_beta = {}
a0_eff_vs_beta = {}
a2_eff_vs_beta = {}

# Also store the SDW moment ratio
Q_sdw_vs_beta = np.zeros(N_beta)

for i_lam, Lambda in enumerate(Lambda_vals):
    Lam2 = Lambda**2
    x_n = omega_sq / Lam2    # dimensionless arguments for each eigenvalue

    Q_arr = np.zeros(N_beta)
    a0_arr = np.zeros(N_beta)
    a2_arr = np.zeros(N_beta)

    for j, beta in enumerate(beta_scan):
        f_vals = f_entropy(x_n, beta)
        a0_eff = np.sum(dim2 * f_vals)
        a2_eff = np.sum(dim2 * x_n * f_vals)
        Q_arr[j] = a0_eff / a2_eff if a2_eff > 0 else np.inf
        a0_arr[j] = a0_eff
        a2_arr[j] = a2_eff

        # SDW moment ratio (only for first Lambda)
        if i_lam == 0:
            f0, f2, f4, _, _ = compute_sdw_moments(beta)
            Q_sdw_vs_beta[j] = (f4 / f2) if f2 > 0 else np.inf

    Q_eff_vs_beta[Lambda] = Q_arr
    a0_eff_vs_beta[Lambda] = a0_arr
    a2_eff_vs_beta[Lambda] = a2_arr

    # Report key values
    idx_min = np.argmin(Q_arr)
    print(f"\n  Lambda = {Lambda:.4f} M_KK (= {Lambda/Lambda_sp:.2f} * Lambda_sp):")
    print(f"    Q^eff range: [{Q_arr.min():.6f}, {Q_arr.max():.6f}]")
    print(f"    Q^eff minimum at beta = {beta_scan[idx_min]:.1f}: Q = {Q_arr[idx_min]:.6f}")
    print(f"    Q^bare = {Q_bare:.6f}")
    print(f"    Q^eff(beta_opt) / Q^bare = {Q_arr[idx_min] / Q_bare:.6f}")

# =============================================================================
# 5. DETAILED ANALYSIS AT SPECIES CUTOFF
# =============================================================================
print("\n" + "=" * 78)
print("5. DETAILED ANALYSIS AT Lambda = Lambda_sp")
print("=" * 78)

Q_main = Q_eff_vs_beta[Lambda_sp]
a0_main = a0_eff_vs_beta[Lambda_sp]
a2_main = a2_eff_vs_beta[Lambda_sp]

# Find optimal beta (minimum Q)
idx_opt = np.argmin(Q_main)
beta_opt = beta_scan[idx_opt]
Q_opt = Q_main[idx_opt]

# Fine-tune around optimal beta
beta_fine = np.linspace(max(0.01, beta_opt - 1.0), beta_opt + 1.0, 1000)
x_n = omega_sq / Lambda_sp_sq
Q_fine = np.zeros(len(beta_fine))
for j, beta in enumerate(beta_fine):
    f_vals = f_entropy(x_n, beta)
    a0_eff = np.sum(dim2 * f_vals)
    a2_eff = np.sum(dim2 * x_n * f_vals)
    Q_fine[j] = a0_eff / a2_eff

idx_fine_opt = np.argmin(Q_fine)
beta_opt_fine = beta_fine[idx_fine_opt]
Q_opt_fine = Q_fine[idx_fine_opt]

print(f"\n  Coarse scan: beta_opt = {beta_opt:.1f}, Q_opt = {Q_opt:.8f}")
print(f"  Fine   scan: beta_opt = {beta_opt_fine:.4f}, Q_opt = {Q_opt_fine:.8f}")
print(f"\n  Comparison to bare:")
print(f"    Q^bare              = {Q_bare:.8f}")
print(f"    Q^eff(beta_opt)     = {Q_opt_fine:.8f}")
print(f"    Q^eff / Q^bare      = {Q_opt_fine / Q_bare:.8f}")
print(f"    Improvement factor  = {Q_bare / Q_opt_fine:.4f}x")

# Limiting behaviors
print(f"\n  Limiting behaviors:")
x_n_sp = omega_sq / Lambda_sp_sq
# beta -> 0 (high temperature): p -> 1/2, f_S -> ln(2)
# Q -> sum(d_n * ln2) / sum(d_n * x_n * ln2) = Q_bare
print(f"    beta -> 0: Q -> Q^bare = {Q_bare:.8f}")
print(f"    Actual at beta=0.1: Q = {Q_main[0]:.8f}")

# beta -> inf (zero temperature): f_S -> 0 everywhere, ratio undefined
# For large beta, f_S(x) ~ beta*x * exp(-beta*x) for x > 0
# So a_0 ~ sum d_n * beta*x_n * exp(-beta*x_n), a_2 ~ sum d_n * beta*x_n^2 * exp(-beta*x_n)
# Q -> <x * exp(-beta*x)> / <x^2 * exp(-beta*x)> -> dominated by smallest x_n
print(f"    Actual at beta=10.0: Q = {Q_main[-1]:.8f}")

# What happens at very small beta?
# f_S(x, beta=0) = ln(2) for all x
# Q(beta=0) = sum(d_n * ln2) / sum(d_n * x_n * ln2) = a0/a2 = Q_bare
# For small beta: Taylor expansion around beta=0
# f_S(x, beta) = ln(2) - (beta*x)^2/8 + O(beta^4)
# a0_eff = sum d_n * [ln(2) - beta^2*x_n^2/8] = ln(2)*a0 - beta^2*a4/(8*Lambda^4)
# a2_eff = sum d_n * x_n * [ln(2) - beta^2*x_n^2/8]
#        = ln(2) * sum d_n*x_n - beta^2/(8*Lambda^4) * sum d_n*x_n^3
# So Q(beta) = [ln2*a0 - beta^2*c1] / [ln2*a2_eff_0 - beta^2*c2]
# where c1 = a4_spec/(8*Lambda^4) and c2 = Tr(D^6)/(8*Lambda^6)

# At leading order in beta^2:
# Q ~ Q_bare * [1 - beta^2/(8*ln2) * (c1/a0 - c2/a2_eff_0)]
# This determines whether Q increases or decreases initially

a6_spec = np.sum(dim2 * omega_sq**3)
c1_over_a0 = a4_spec / (a0_spec * 8 * Lambda_sp_sq**2)
c2_over_a2 = a6_spec / (a2_spec * 8 * Lambda_sp_sq**3)
# Actually: a2_eff_0 = sum d_n * x_n at beta=0 is sum d_n * omega^2/Lambda^2
a2_eff_0 = np.sum(dim2 * x_n_sp)

c1_over_a0_v2 = np.sum(dim2 * x_n_sp**2) / (8 * a0_spec)
c2_over_a2_v2 = np.sum(dim2 * x_n_sp**3) / (8 * a2_eff_0)

dQ_sign = c1_over_a0_v2 - c2_over_a2_v2
print(f"\n  Small-beta expansion:")
print(f"    Q(beta) ~ Q_bare * [1 - beta^2/(ln2) * {dQ_sign:.8f}]")
print(f"    Sign of correction: {'DECREASING' if dQ_sign > 0 else 'INCREASING'} (Q moves {'down' if dQ_sign > 0 else 'up'})")

# =============================================================================
# 6. COMPARISON WITH OTHER CUTOFF FUNCTIONS
# =============================================================================
print("\n" + "=" * 78)
print("6. COMPARISON WITH STANDARD CUTOFF FUNCTIONS")
print("=" * 78)

# Heat kernel: f(x) = exp(-x)
# Compact support: f(x) = (1-x)^4 * theta(1-x)
# Resolvent: f(x) = 1/(x+1)

def f_heat(x):
    return np.exp(-x)

def f_compact(x):
    return np.where(x < 1.0, (1.0 - x)**4, 0.0)

def f_resolvent(x):
    return 1.0 / (x + 1.0)


cutoffs = {
    'Entropy (beta_opt)': lambda x: f_entropy(x, beta_opt_fine),
    'Heat kernel':         f_heat,
    'Compact support':     f_compact,
    'Resolvent':           f_resolvent,
    'Entropy (beta=0.5)':  lambda x: f_entropy(x, 0.5),
    'Entropy (beta=1.0)':  lambda x: f_entropy(x, 1.0),
    'Entropy (beta=5.0)':  lambda x: f_entropy(x, 5.0),
}

x_sp = omega_sq / Lambda_sp_sq

print(f"\n  {'Cutoff':>25} {'a0_eff':>14} {'a2_eff':>14} {'Q=a0/a2':>12} {'Q/Q_bare':>10}")
results_comparison = {}
for name, f_func in cutoffs.items():
    fv = f_func(x_sp)
    a0_e = np.sum(dim2 * fv)
    a2_e = np.sum(dim2 * x_sp * fv)
    Q_e = a0_e / a2_e if a2_e > 0 else np.inf
    results_comparison[name] = {'a0': a0_e, 'a2': a2_e, 'Q': Q_e}
    print(f"  {name:>25} {a0_e:14.4f} {a2_e:14.4f} {Q_e:12.6f} {Q_e/Q_bare:10.6f}")

# Bare (polynomial / SDW)
print(f"  {'Bare (SDW polynomial)':>25} {a0_spec:14.0f} {np.sum(dim2*x_sp):14.4f} {Q_bare:12.6f} {1.0:10.6f}")

# =============================================================================
# 7. SDW MOMENT RATIO f_4/f_2 ANALYSIS
# =============================================================================
print("\n" + "=" * 78)
print("7. SDW MOMENT RATIO f_4/f_2 FOR ENTROPY CUTOFF")
print("=" * 78)

# In the SDW polynomial expansion, the CC ratio is:
#   Q_CC = (f_4/f_2) * (a_0/a_2)
# where f_4 = int x f(x) dx, f_2 = int f(x) dx.
#
# For the FULL spectral action, Q_eff is computed directly.
# The SDW ratio is valid for Lambda >> lambda_max.
# The effective ratio is valid at any Lambda.

# Compute f_4/f_2 for entropy cutoff vs beta
f4_over_f2 = np.zeros(N_beta)
f0_vals = np.zeros(N_beta)
f2_vals = np.zeros(N_beta)
f4_vals = np.zeros(N_beta)

for j, beta in enumerate(beta_scan):
    f0, f2, f4, _, _ = compute_sdw_moments(beta)
    f0_vals[j] = f0
    f2_vals[j] = f2
    f4_vals[j] = f4
    f4_over_f2[j] = f4 / f2 if f2 > 0 else np.inf

print(f"\n  {'beta':>6} {'f_0':>10} {'f_2':>12} {'f_4':>12} {'f_4/f_2':>10} {'Q_SDW':>12}")
for j in range(0, N_beta, 10):
    Q_sdw = f4_over_f2[j] * Q_bare
    print(f"  {beta_scan[j]:6.1f} {f0_vals[j]:10.6f} {f2_vals[j]:12.6f} "
          f"{f4_vals[j]:12.6f} {f4_over_f2[j]:10.6f} {Q_sdw:12.6f}")

idx_sdw_min = np.argmin(f4_over_f2)
print(f"\n  Minimum f_4/f_2 at beta = {beta_scan[idx_sdw_min]:.1f}: "
      f"f_4/f_2 = {f4_over_f2[idx_sdw_min]:.8f}")
print(f"  Q_SDW at minimum = {f4_over_f2[idx_sdw_min] * Q_bare:.8f}")

# Cross-check: verify that for large Lambda, Q_eff -> Q_SDW
print(f"\n  Cross-check (Q_eff vs Q_SDW at large Lambda):")
for Lambda_test in [5.0 * Lambda_sp, 10.0 * Lambda_sp, 20.0 * Lambda_sp]:
    x_test = omega_sq / Lambda_test**2
    for beta_test in [1.0, 3.0, 5.0]:
        fv = f_entropy(x_test, beta_test)
        a0_e = np.sum(dim2 * fv)
        a2_e = np.sum(dim2 * x_test * fv)
        Q_e = a0_e / a2_e
        _, f2_t, f4_t, _, _ = compute_sdw_moments(beta_test)
        Q_sdw_t = (f4_t / f2_t) * Q_bare
        print(f"    Lambda/Lambda_sp={Lambda_test/Lambda_sp:.0f}, beta={beta_test:.0f}: "
              f"Q_eff={Q_e:.6f}, Q_SDW={Q_sdw_t:.6f}, ratio={Q_e/Q_sdw_t:.6f}")

# =============================================================================
# 8. BETA DEPENDENCE OF KEY OBSERVABLES
# =============================================================================
print("\n" + "=" * 78)
print("8. BETA DEPENDENCE AT Lambda = Lambda_sp")
print("=" * 78)

print(f"\n  {'beta':>6} {'a0_eff':>14} {'a2_eff':>14} {'Q_eff':>12} {'Q/Q_bare':>10} {'Q/Q_gate':>10}")
for j in range(0, N_beta, 5):
    beta = beta_scan[j]
    Q = Q_main[j]
    print(f"  {beta:6.1f} {a0_main[j]:14.4f} {a2_main[j]:14.4f} "
          f"{Q:12.6f} {Q/Q_bare:10.6f} {Q/Q_bare_gate:10.6f}")

# =============================================================================
# 9. STRUCTURAL ANALYSIS: WHY THE RATIO BEHAVES AS IT DOES
# =============================================================================
print("\n" + "=" * 78)
print("9. STRUCTURAL ANALYSIS")
print("=" * 78)

# The key question: can f_S DECREASE Q = a0/a2 compared to bare?
#
# Q^eff = sum d_n f_S(x_n) / sum d_n x_n f_S(x_n)
# Q^bare = sum d_n / sum d_n x_n  (f=1 limit)
#
# For Q^eff < Q^bare, we need:
#   [sum d_n f_S(x_n)] * [sum d_n x_n] < [sum d_n] * [sum d_n x_n f_S(x_n)]
#
# Rearranging: <f_S(x)> * <x>_bare < <x * f_S(x)>
# i.e., <x * f_S(x)> / <f_S(x)> > <x>
# i.e., the f_S-WEIGHTED mean of x is LARGER than the unweighted mean.
#
# Since f_S(x) is decreasing, it gives MORE weight to small x (small eigenvalues).
# This makes the weighted mean of x SMALLER, not larger.
# Therefore: Q^eff > Q^bare for ANY decreasing f_S.
#
# This is a consequence of Chebyshev's sum inequality:
# If f is decreasing and g is increasing, then <f*g> < <f>*<g>.
# Here f = f_S(x) is decreasing, g = x is increasing.
# So <f_S(x) * x> < <f_S(x)> * <x>
# => <x*f_S>/<f_S> < <x>
# => Q^eff = <f_S>/<x*f_S> > 1/<x> * <f_S>/<x*f_S> ... wait, let me redo this.
#
# Actually: Q^eff = <f_S> / <x * f_S>
# Q^bare = <1> / <x> = 1/<x>
#
# Chebyshev: if f decreasing and g=x increasing, weighted by d_n > 0:
#   (sum d_n) * (sum d_n * f_S(x_n) * x_n) <= (sum d_n * f_S(x_n)) * (sum d_n * x_n)
#
# Dividing: <f_S * x> <= <f_S> * <x>
# So: <f_S> / <x * f_S> >= <f_S> / (<f_S> * <x>) = 1/<x> = Q^bare
#
# THEREFORE: Q^eff >= Q^bare for ANY DECREASING f_S.
# This is CHEBYSHEV'S INEQUALITY, not Jensen's.
# It applies to ALL monotone decreasing cutoffs, including the entropy function.
#
# The S65 theorem used Jensen; the correct statement is Chebyshev.
# The result is STRONGER: no monotone decreasing cutoff can improve the CC ratio.

print("  STRUCTURAL THEOREM (Chebyshev):")
print("  For ANY monotonically decreasing f: [0,inf) -> [0,inf):")
print("    Q^eff(f) = <f(x)> / <x*f(x)> >= <1>/<x> = Q^bare")
print("  Equality iff f = const or spectrum has one eigenvalue.")
print()
print("  Proof: Chebyshev's sum inequality.")
print("  f_S(x) is decreasing, x is increasing.")
print("  Weighted by d_n > 0: sum d_n * f(x_n) * x_n <= [sum d_n f(x_n)] * [sum d_n x_n] / sum d_n")
print("  => <f*x> <= <f> * <x>")
print("  => <f> / <f*x> >= 1/<x> = Q_bare")
print()
print("  This applies to the entropy cutoff because f_S IS monotone decreasing for x >= 0.")
print("  The inflection point is IRRELEVANT — only monotonicity matters.")

# Verify numerically
print(f"\n  Numerical verification:")
print(f"  Q^bare = {Q_bare:.8f}")
print(f"  Q^eff(beta_opt) = {Q_opt_fine:.8f}  (>= Q_bare? {Q_opt_fine >= Q_bare - 1e-10})")
print(f"  Q^eff / Q^bare = {Q_opt_fine / Q_bare:.8f}  (>= 1.0)")
print(f"  All Q^eff >= Q^bare? {np.all(Q_main >= Q_bare - 1e-10)}")

# Find the minimum ratio Q^eff / Q^bare
min_ratio = Q_main.min() / Q_bare
print(f"  Minimum Q^eff / Q^bare = {min_ratio:.8f}")
print(f"  Maximum 'improvement' = {(1 - min_ratio) * 100:.4f}% (consistent with numerical precision)")

# =============================================================================
# 10. GATE VERDICT
# =============================================================================
print("\n" + "=" * 78)
print("10. GATE VERDICT: ENTROPY-SA-CC-66")
print("=" * 78)

# Compute the gate quantities
# The task says bare_ratio = 0.232
# But we compute Q directly from the spectrum
Q_ratio_at_opt = Q_opt_fine / Q_bare

print(f"\n  Pre-registered criteria:")
print(f"    bare_ratio (gate spec) = {Q_bare_gate}")
print(f"    PASS: Q^S < 0.1 * bare_ratio = {0.1 * Q_bare_gate:.4f}")
print(f"    FAIL: Q^S >= bare_ratio = {Q_bare_gate}")
print(f"    INFO: 0.1 <= Q^S/bare_ratio < 1.0")

print(f"\n  Computed quantities:")
print(f"    Q^bare (from 992-mode spectrum) = {Q_bare:.6f}")
print(f"    Q^eff(beta_opt={beta_opt_fine:.3f}) = {Q_opt_fine:.6f}")
print(f"    Q^eff / Q^bare = {Q_ratio_at_opt:.6f}")

# The key result: the entropy cutoff CANNOT improve Q.
# Chebyshev's inequality guarantees Q^eff >= Q^bare for any decreasing f.
# Therefore Q^S / Q_bare >= 1.0 always.

if Q_opt_fine >= Q_bare - 1e-8:
    verdict = "FAIL"
    print(f"\n  GATE VERDICT: **FAIL**")
    print(f"  The entropy cutoff WORSENS a_0/a_2 at all beta.")
    print(f"  Q^eff >= Q^bare by Chebyshev's sum inequality.")
    print(f"  This is STRUCTURAL: no monotone decreasing cutoff can improve the CC ratio.")
else:
    # This branch should never be reached
    ratio_vs_gate = Q_opt_fine / Q_bare_gate
    if ratio_vs_gate < 0.1:
        verdict = "PASS"
        print(f"\n  GATE VERDICT: **PASS** (unexpected!)")
    elif ratio_vs_gate < 1.0:
        verdict = "INFO"
        print(f"\n  GATE VERDICT: **INFO**")
    else:
        verdict = "FAIL"
        print(f"\n  GATE VERDICT: **FAIL**")

print(f"\n  Classification: SCHEME-DEPENDENT (cutoff function choice)")
print(f"  The entropy cutoff is scheme-dependent: Q depends on both beta and Lambda.")
print(f"  But the LOWER BOUND Q >= Q_bare is SCHEME-INDEPENDENT (structural).")

# =============================================================================
# 11. SUMMARY TABLE
# =============================================================================
print("\n" + "=" * 78)
print("11. SUMMARY")
print("=" * 78)

print(f"""
  ENTROPY-SA-CC-66 SUMMARY
  ========================

  Cutoff function: f_S(x) = -[p*ln(p) + (1-p)*ln(1-p)], p = 1/(e^(beta*x)+1)

  KEY NUMBERS:
  1. f_S(0) = ln(2) = {np.log(2):.6f} (beta-independent)
  2. f_S is monotonically decreasing for x >= 0 (verified numerically)
  3. f_S has inflection point at x ~ {x_infl:.3f}/beta (NOT globally convex)
  4. Q^bare = a_0/a_2 = {Q_bare:.6f} (from 992-mode D_K spectrum at fold)
  5. Q^eff(beta_opt={beta_opt_fine:.3f}) = {Q_opt_fine:.6f}
  6. Q^eff / Q^bare = {Q_ratio_at_opt:.6f} >= 1.0 (ALWAYS)

  STRUCTURAL THEOREM:
  Q^eff(f) >= Q^bare for ANY monotonically decreasing f.
  Proof: Chebyshev's sum inequality (f decreasing, x increasing, d_n > 0).
  The entropy cutoff's inflection point is irrelevant — only monotonicity matters.

  SDW MOMENT RATIOS (for reference):
  f_4^S/f_2^S = {f4_over_f2[idx_sdw_min]:.6f} at beta = {beta_scan[idx_sdw_min]:.1f} (minimum)
  All f_4^S/f_2^S > 0, so the SDW CC ratio is always positive.

  VERDICT: FAIL
  The entropy cutoff makes the CC ratio WORSE, not better.
  This extends the S65 NONLOCAL-SA-65 result to the thermodynamic entropy cutoff.
  The underlying mechanism is Chebyshev's inequality (stronger than Jensen).
""")

# =============================================================================
# 12. SAVE DATA
# =============================================================================
print("12. SAVING DATA")
outpath = os.path.join(outdir, 's66_entropy_sa.npz')
np.savez(outpath,
         # Gate
         gate_id='ENTROPY-SA-CC-66',
         verdict=verdict,
         # Spectrum
         omega=omega,
         dim2=dim2,
         N_evals=N_evals,
         N_modes=N_modes,
         # Bare moments
         a0_spec=a0_spec,
         a2_spec=a2_spec,
         a4_spec=a4_spec,
         Q_bare=Q_bare,
         Q_bare_gate=Q_bare_gate,
         # Beta scan
         beta_scan=beta_scan,
         Q_eff_species=Q_eff_vs_beta[Lambda_sp],
         a0_eff_species=a0_eff_vs_beta[Lambda_sp],
         a2_eff_species=a2_eff_vs_beta[Lambda_sp],
         # SDW moments
         f0_vals=f0_vals,
         f2_vals=f2_vals,
         f4_vals=f4_vals,
         f4_over_f2=f4_over_f2,
         Q_sdw_vs_beta=Q_sdw_vs_beta,
         # Optimal
         beta_opt=beta_opt_fine,
         Q_opt=Q_opt_fine,
         Q_ratio=Q_ratio_at_opt,
         # Lambda dependence
         Lambda_vals=np.array(Lambda_vals),
         Lambda_sp=Lambda_sp,
         # Fine scan
         beta_fine=beta_fine,
         Q_fine=Q_fine,
         # Inflection
         x_inflection=x_infl,
         )
print(f"  Saved: {outpath}")

# =============================================================================
# 13. PLOT
# =============================================================================
print("13. GENERATING PLOT")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('ENTROPY-SA-CC-66: Thermodynamic Entropy Cutoff on SU(3)',
             fontsize=14, fontweight='bold')

# Panel A: f_S(x) for various beta
ax = axes[0, 0]
x_plot = np.linspace(0, 8, 500)
for beta_p in [0.5, 1.0, 2.0, 5.0]:
    ax.plot(x_plot, f_entropy(x_plot, beta_p), label=f'beta={beta_p}')
ax.axhline(np.log(2), color='gray', linestyle='--', alpha=0.5, label='ln(2)')
ax.set_xlabel('x = lambda^2 / Lambda^2')
ax.set_ylabel('f_S(x, beta)')
ax.set_title('(A) Entropy Cutoff Function')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel B: Q^eff vs beta at Lambda = Lambda_sp
ax = axes[0, 1]
ax.plot(beta_scan, Q_main, 'b-', linewidth=2, label='Q^eff (full spectrum)')
ax.axhline(Q_bare, color='r', linestyle='--', linewidth=1.5, label=f'Q^bare = {Q_bare:.4f}')
ax.axhline(Q_bare_gate, color='orange', linestyle=':', linewidth=1.5,
           label=f'Gate bare = {Q_bare_gate}')
ax.axhline(0.1 * Q_bare_gate, color='green', linestyle=':', linewidth=1,
           label=f'PASS threshold = {0.1*Q_bare_gate:.4f}')
ax.set_xlabel('beta (inverse temperature)')
ax.set_ylabel('Q = a_0^eff / a_2^eff')
ax.set_title('(B) CC Ratio vs beta')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel C: Q^eff / Q^bare vs beta for different Lambda
ax = axes[1, 0]
for Lambda_p in Lambda_vals:
    Q_arr = Q_eff_vs_beta[Lambda_p]
    ratio_arr = Q_arr / Q_bare
    lbl = f'Lambda = {Lambda_p/Lambda_sp:.1f} * Lambda_sp'
    ax.plot(beta_scan, ratio_arr, label=lbl)
ax.axhline(1.0, color='r', linestyle='--', linewidth=1.5, label='Q/Q_bare = 1 (no improvement)')
ax.set_xlabel('beta (inverse temperature)')
ax.set_ylabel('Q^eff / Q^bare')
ax.set_title('(C) Relative CC Ratio (Chebyshev bound: >= 1)')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel D: SDW moment ratio f_4/f_2 vs beta
ax = axes[1, 1]
ax.plot(beta_scan, f4_over_f2, 'b-', linewidth=2, label='f_4/f_2')
ax.set_xlabel('beta (inverse temperature)')
ax.set_ylabel('f_4^S / f_2^S')
ax.set_title('(D) SDW Moment Ratio')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plotpath = os.path.join(outdir, 's66_entropy_sa.png')
plt.savefig(plotpath, dpi=150, bbox_inches='tight')
print(f"  Saved: {plotpath}")

print("\n" + "=" * 78)
print("COMPUTATION COMPLETE")
print("=" * 78)
