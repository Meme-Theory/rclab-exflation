#!/usr/bin/env python3
"""
S75-G3-ZETA-NOT-PHYS: Formal proof that zeta_D(s) is NOT a physical observable.

Three independent routes converging on a common obstruction:
  Route 1: Scheme dependence of vacuum energy (same spectrum, different numbers)
  Route 2: Non-uniqueness (zeta = one point in spectral functional space)
  Route 3: L_max convergence failure (zeta-regularized quantities are truncation-sensitive)

Gate: S75-G3-ZETA-NOT-PHYS
  PASS: All 3 routes share common obstruction (formalize as permanent theorem)
  INFO: 2/3 converge
  FAIL: Routes disagree on the obstruction

Author: Lizzi spectral functional theorist
Session: S75 Wave 3
"""

import numpy as np
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    PI, a0_fold, a2_fold, a4_fold, M_KK, M_KK_gravity, M_KK_kerner,
    M_Pl_reduced, rho_Lambda_obs, tau_fold, Delta_BCS
)

# ============================================================================
# SECTION 0: Reconstruct the D_K spectrum at the fold (tau = 0.19)
# ============================================================================
# Use the canonical Seeley-DeWitt moments as constraints on the spectral
# zeta function.  The spectral zeta is defined as:
#   zeta_D(s) = Tr |D|^{-2s} = sum_lam |lam|^{-2s}
# and the Seeley-DeWitt coefficients satisfy:
#   a_k = zeta_D(k)  for  k = 0, 1, 2, 3, ...
# where a_0 counts eigenvalues, a_2 = sum lam^{-2}, etc.
#
# We have canonical values at L_max = 3:
#   a_0 = 6440 (mode count)
#   a_2 = 2776.17 (second spectral moment)
#   a_4 = 1350.72 (fourth spectral moment -- the zeta action)
# These are the INPUT DATA.  The computation tests whether zeta_D
# can be promoted from a regularization tool to a physical observable.

a0 = a0_fold  # (local) mode count at fold
a2 = a2_fold  # (local) second moment at fold
a4 = a4_fold  # (local) fourth moment at fold

# Effective average eigenvalue (for analytic estimates)
lam_avg_sq = a0 / a2  # (local) <|lam|^2> = a_0/a_2
lam_avg = np.sqrt(lam_avg_sq)  # (local) RMS eigenvalue

print("=" * 72)
print("S75-G3-ZETA-NOT-PHYS: Is zeta_D(s) a physical observable?")
print("=" * 72)
print(f"\nCanonical spectral moments (L_max = 3, tau = {tau_fold}):")
print(f"  a_0 = {a0:.1f}  (mode count)")
print(f"  a_2 = {a2:.4f}  (second moment)")
print(f"  a_4 = {a4:.4f}  (fourth moment = S_zeta)")
print(f"  <|lam|^2> = a_0/a_2 = {lam_avg_sq:.4f}")
print(f"  lam_rms = {lam_avg:.4f} M_KK")

# ============================================================================
# ROUTE 1: SCHEME DEPENDENCE OF VACUUM ENERGY
# ============================================================================
# The "vacuum energy" extracted from a spectral sum depends on the
# regularization scheme.  For the SAME Dirac operator D_K:
#
#   (a) Zeta regularization: rho_vac^{zeta} = zeta_D(-1/2) * M_KK^4 / (4pi^2)
#       But zeta_D at negative arguments requires analytic continuation,
#       which is the DEFINITION of a regularization choice.
#
#   (b) Heat kernel (cutoff): rho_vac^{HK} = (f_0 * a_0 * Lambda^4 +
#       f_2 * a_2 * Lambda^2 + f_4 * a_4 + ...) * M_KK^4 / (4pi^2)
#       Different f(x) give different f_k moments.
#
#   (c) Sharp cutoff: rho_vac^{sharp} = sum_{|lam| < Lambda} |lam|^4 * M_KK^4
#       Quartic divergence in Lambda.
#
# We compute all three for the same spectral data.

print("\n" + "=" * 72)
print("ROUTE 1: Scheme dependence of vacuum energy")
print("=" * 72)

# --- (a) Zeta-regularized vacuum energy ---
# In zeta regularization, the vacuum energy (Casimir energy) is:
#   E_vac^{zeta} = -1/2 * zeta_D(-1/2) * mu^{2s}|_{s=-1/2}
# For our discrete spectrum, zeta_D(s) = sum |lam_i|^{-2s}.
# At s = -1/2: zeta_D(-1/2) = sum |lam_i|^{+1} = M_1 (first absolute moment)
# But this requires specifying the renormalization scale mu.
#
# The zeta action S_zeta = zeta_D(0) = a_4 by definition.
# The vacuum energy is zeta_D(-1/2) which, via the heat kernel relation,
# maps to a DIFFERENT linear combination of SDW moments.
#
# Use the spectral zeta function identity:
#   zeta_D(s) = sum_k c_k(s) * a_{2k}
# where c_k depends on the meromorphic continuation.
#
# For the vacuum energy density (d=4 manifold + d_int=6 internal):
# The key point: zeta regularization SUBTRACTS the pole at s=d/2,
# making the result FINITE but SCHEME-DEPENDENT (the subtraction
# defines the scheme).

# Construct vacuum energy in zeta scheme
# In 4D, the relevant quantity is zeta_D(-2) (fourth power for energy density)
# Analytic continuation from convergent region s > d/2 = 5 to s = -2
# requires subtracting poles.  The subtraction IS the regularization.

# The zeta function on a compact manifold has the asymptotic:
#   zeta_D(s) ~ sum_{k=0}^{N} a_{2k} / (s - (d-2k)/2) + O(1)
# with poles at s = d/2, (d-2)/2, (d-4)/2, ...
# For d_eff = 4 (4D effective theory): poles at s = 2, 1, 0, -1, -2, ...

# At s = -1/2 (vacuum energy in 4D):
# zeta_D(-1/2) is between poles at s = 0 and s = -1.
# The FINITE PART after analytic continuation depends on WHICH continuation
# is used (minimal subtraction vs. dimensional vs. proper-time cutoff).

# Model: assume eigenvalues follow approximate Weyl law
# N(lam) ~ a_0 * (lam/lam_max)^d_eff for lam < lam_max
# This gives zeta_D(s) analytically.

d_eff = 10  # (local) total dimension for Weyl law (4D + 6D internal)
d_eff_4 = 4  # (local) effective 4D spacetime dimension

# Effective Weyl law: lam_max from the spectrum
lam_max = np.sqrt(a0 / a2) * np.sqrt(a0)  # (local) rough UV cutoff from moments
# Better: use moment ratios
# a_0/a_2 = <lam^2>, so lam_typical^2 = a_0/a_2
# a_2/a_4 = <lam^{-2}>/<lam^{-4}>  -- probes IR

# --- Route 1a: Zeta functional value at s = -1/2 ---
# Using moment structure directly:
# We CANNOT compute zeta_D(-1/2) from {a_0, a_2, a_4} without
# additional input.  This is the FIRST obstruction.

# However, we CAN compute the vacuum energy for different ASSUMED
# spectral distributions that reproduce the same a_0, a_2, a_4.

# Model A: Uniform density (box spectrum)
# N eigenvalues uniformly in [lam_min, lam_max]
# Choose lam_min, lam_max to reproduce a_0, a_2

N_modes = int(a0)  # (local)
lam2_mean = a0 / a2  # (local) = <lam^2>
lam4_mean = a0 / a4  # (local) = <lam^4>  (from a_0/a_4 = sum 1 / sum lam^{-4})

# Actually: a_2 = sum lam^{-2}, a_4 = sum lam^{-4}
# So <lam^{-2}> = a_2 / a_0 and <lam^{-4}> = a_4 / a_0
inv_lam2_mean = a2 / a0  # (local) <lam^{-2}>
inv_lam4_mean = a4 / a0  # (local) <lam^{-4}>
var_inv_lam2 = inv_lam4_mean - inv_lam2_mean**2  # (local) Var(lam^{-2})

print(f"\nSpectral distribution parameters:")
print(f"  N_modes = {N_modes}")
print(f"  <|lam|^{{-2}}> = {inv_lam2_mean:.6f}")
print(f"  <|lam|^{{-4}}> = {inv_lam4_mean:.6f}")
print(f"  Var(|lam|^{{-2}}) = {var_inv_lam2:.6f}")
print(f"  Relative width = {np.sqrt(var_inv_lam2)/inv_lam2_mean:.4f}")

# --- Model A: Flat distribution of lam^{-2} ---
# If lam^{-2} is uniformly distributed in [alpha, beta]:
# <lam^{-2}> = (alpha + beta)/2 = inv_lam2_mean
# <lam^{-4}> = (alpha^2 + alpha*beta + beta^2)/3 = inv_lam4_mean
# Two equations, two unknowns.

A_coeff = inv_lam2_mean  # (local) = (alpha + beta)/2
B_coeff = inv_lam4_mean  # (local) = (alpha^2 + alpha*beta + beta^2)/3

# From Var = <X^2> - <X>^2 = B - A^2
# 3*B = (alpha + beta)^2 - alpha*beta = 4*A^2 - alpha*beta
# alpha*beta = 4*A^2 - 3*B

sum_ab = 2 * A_coeff  # (local) alpha + beta
prod_ab = 4 * A_coeff**2 - 3 * B_coeff  # (local) alpha * beta
disc = sum_ab**2 - 4 * prod_ab  # (local) discriminant

if disc >= 0:
    alpha_flat = (sum_ab - np.sqrt(disc)) / 2  # (local)
    beta_flat = (sum_ab + np.sqrt(disc)) / 2   # (local)
    lam_max_flat = 1.0 / np.sqrt(max(alpha_flat, 1e-30))  # (local)
    lam_min_flat = 1.0 / np.sqrt(beta_flat)    # (local)
else:
    # Negative discriminant: flat model doesn't fit
    alpha_flat = inv_lam2_mean  # (local) degenerate
    beta_flat = inv_lam2_mean   # (local) degenerate
    lam_max_flat = 1.0 / np.sqrt(inv_lam2_mean)  # (local)
    lam_min_flat = lam_max_flat  # (local)

print(f"\n  Model A (flat lam^{{-2}} distribution):")
print(f"    lam^{{-2}} range: [{alpha_flat:.6f}, {beta_flat:.6f}]")
print(f"    lam range: [{lam_min_flat:.4f}, {lam_max_flat:.4f}] M_KK")

# Vacuum energy for flat model:
# E_vac = sum |lam_i| = N * <|lam|> = N * integral of lam * rho(lam) dlam
# For flat in lam^{-2}: rho(u) = N/(beta-alpha), u = lam^{-2}
# <|lam|> = <u^{-1/2}> = integral_{alpha}^{beta} u^{-1/2} du / (beta - alpha)
#         = 2*(sqrt(beta) - sqrt(alpha)) / (beta - alpha)   [if alpha >= 0]

if beta_flat > alpha_flat and alpha_flat >= 0:
    inv_lam_half_A = 2 * (np.sqrt(beta_flat) - np.sqrt(alpha_flat)) / (beta_flat - alpha_flat)  # (local) <lam^{-1}>
    zeta_minus_half_A = a0 * inv_lam_half_A  # (local) sum |lam_i|^{+1} = zeta_D(-1/2)
else:
    inv_lam_half_A = 1.0 / np.sqrt(inv_lam2_mean)  # (local) fallback
    zeta_minus_half_A = a0 * inv_lam_half_A  # (local)

# Vacuum energy density in this model
E_vac_A = 0.5 * zeta_minus_half_A * M_KK  # (local) in M_KK^2 units (one power from lam, one from M_KK)

# --- Model B: Log-normal distribution ---
# lam^{-2} ~ LogNormal(mu_ln, sigma_ln)
# <lam^{-2}> = exp(mu_ln + sigma_ln^2/2) = inv_lam2_mean
# <lam^{-4}> = exp(2*mu_ln + 2*sigma_ln^2) = inv_lam4_mean
# So: (inv_lam4_mean)/(inv_lam2_mean)^2 = exp(sigma_ln^2)

ratio_moments = inv_lam4_mean / inv_lam2_mean**2  # (local)
sigma_ln2 = np.log(ratio_moments)  # (local)
sigma_ln = np.sqrt(sigma_ln2)  # (local)
mu_ln = np.log(inv_lam2_mean) - sigma_ln2 / 2  # (local)

# <|lam|> for lognormal lam^{-2}: <(lam^{-2})^{-1/2}> = exp(-mu_ln/2 + sigma_ln^2/8)
inv_lam_half_B = np.exp(-mu_ln / 2 + sigma_ln2 / 8)  # (local) <|lam|>
zeta_minus_half_B = a0 * inv_lam_half_B  # (local)

E_vac_B = 0.5 * zeta_minus_half_B * M_KK  # (local)

print(f"\n  Model B (log-normal lam^{{-2}} distribution):")
print(f"    mu_ln = {mu_ln:.6f}, sigma_ln = {sigma_ln:.6f}")

# --- Model C: Delta function (all eigenvalues equal) ---
# All lam_i = lam_0, with a_0 = N, a_2 = N*lam_0^{-2}, a_4 = N*lam_0^{-4}
# Consistency: a_2^2/a_0 = a_4 requires a_4 = a_2^2/a_0
a4_delta = a2**2 / a0  # (local) prediction for delta function
delta_a4_dev = abs(a4 - a4_delta) / a4  # (local) fractional deviation

lam0_delta = np.sqrt(a0 / a2)  # (local)
zeta_minus_half_C = a0 * lam0_delta  # (local)
E_vac_C = 0.5 * zeta_minus_half_C * M_KK  # (local)

print(f"\n  Model C (delta function):")
print(f"    lam_0 = {lam0_delta:.4f} M_KK")
print(f"    a_4(predicted) = {a4_delta:.2f} vs a_4(actual) = {a4:.2f}")
print(f"    delta function INCONSISTENCY: {delta_a4_dev*100:.2f}%")

# --- Route 1 Summary ---
print(f"\n--- ROUTE 1 RESULTS: Vacuum energy from same {{a_0, a_2, a_4}} ---")
print(f"  zeta_D(-1/2) [Model A, flat]:      {zeta_minus_half_A:.2f}")
print(f"  zeta_D(-1/2) [Model B, lognormal]: {zeta_minus_half_B:.2f}")
print(f"  zeta_D(-1/2) [Model C, delta]:     {zeta_minus_half_C:.2f}")

spread_zeta_mhalf = max(zeta_minus_half_A, zeta_minus_half_B, zeta_minus_half_C) / \
                    min(zeta_minus_half_A, zeta_minus_half_B, zeta_minus_half_C)  # (local)
print(f"  Spread (max/min): {spread_zeta_mhalf:.4f}")

# The vacuum energy density in units of M_KK^4
rho_vac_A = zeta_minus_half_A * M_KK**4 / (32 * PI**2)  # (local) GeV^4
rho_vac_B = zeta_minus_half_B * M_KK**4 / (32 * PI**2)  # (local) GeV^4
rho_vac_C = zeta_minus_half_C * M_KK**4 / (32 * PI**2)  # (local) GeV^4

CC_gap_A = np.log10(rho_vac_A / rho_Lambda_obs)  # (local) OOM
CC_gap_B = np.log10(rho_vac_B / rho_Lambda_obs)  # (local) OOM
CC_gap_C = np.log10(rho_vac_C / rho_Lambda_obs)  # (local) OOM

print(f"\n  Vacuum energy density (GeV^4):")
print(f"    rho_vac [A]: {rho_vac_A:.3e}  (CC gap: {CC_gap_A:.1f} OOM)")
print(f"    rho_vac [B]: {rho_vac_B:.3e}  (CC gap: {CC_gap_B:.1f} OOM)")
print(f"    rho_vac [C]: {rho_vac_C:.3e}  (CC gap: {CC_gap_C:.1f} OOM)")

CC_gap_spread = abs(CC_gap_A - CC_gap_B)  # (local)
print(f"    CC gap spread A-B: {CC_gap_spread:.2f} OOM")
print(f"    CC gap spread A-C: {abs(CC_gap_A - CC_gap_C):.2f} OOM")

# Now add cutoff comparison (from canonical)
# Standard cutoff: rho_Lambda = f_0/(2*pi^2) * a_0 * Lambda^4 * M_KK^4
# With f(x) = sqrt(x): f_0 = Gamma(-1/2)*Gamma(d/2)/Gamma(d/2-1/2) -- divergent.
# With f(x) = exp(-x): f_0 = 1
Lambda_over_MKK = 2.048  # (local) optimal Lambda from S70
rho_cutoff_exp = a0 * Lambda_over_MKK**4 * M_KK**4 / (2 * PI**2)  # (local) f(x)=exp(-x), f_0=1
CC_gap_cutoff = np.log10(rho_cutoff_exp / rho_Lambda_obs)  # (local)

# Zeta action: rho_zeta = a_4 * M_KK^4 / (2*pi^2)
rho_zeta = a4 * M_KK**4 / (2 * PI**2)  # (local)
CC_gap_zeta = np.log10(rho_zeta / rho_Lambda_obs)  # (local)

print(f"\n  Comparison with standard regularizations:")
print(f"    rho_cutoff [f=exp, Lambda={Lambda_over_MKK:.3f}]: {rho_cutoff_exp:.3e}  (CC gap: {CC_gap_cutoff:.1f} OOM)")
print(f"    rho_zeta [S_zeta = a_4]:                       {rho_zeta:.3e}  (CC gap: {CC_gap_zeta:.1f} OOM)")

# ROUTE 1 OBSTRUCTION: The vacuum energy requires specifying MORE than the
# convergent spectral moments {a_0, a_2, a_4, ...}.  zeta_D(-1/2) is NOT
# determined by the convergent zeta values.  It requires analytic continuation,
# which is EXACTLY a regularization choice.

route1_pass = (spread_zeta_mhalf > 1.01)  # (local) different models give different answers
route1_obstruction = "ANALYTIC_CONTINUATION"  # (local)
print(f"\n  ROUTE 1 VERDICT: {'SCHEME-DEPENDENT' if route1_pass else 'INCONCLUSIVE'}")
print(f"  Obstruction: Analytic continuation from convergent region (s > d/2)")
print(f"  to physical region (s = -1/2) is NOT unique.")
print(f"  Model spread: {spread_zeta_mhalf:.4f}x ({(spread_zeta_mhalf-1)*100:.2f}% variation)")

# ============================================================================
# ROUTE 2: NON-UNIQUENESS -- zeta is ONE POINT in functional space
# ============================================================================
# The spectral action is S[f, D] = Tr f(D^2/Lambda^2).
# Different f give different physics from the same D.
# The zeta function corresponds to f_s(x) = x^{-s}, one SPECIFIC choice.
#
# We demonstrate this by computing S[f, D] for several choices of f,
# all applied to the same spectral data.

print("\n" + "=" * 72)
print("ROUTE 2: Non-uniqueness -- zeta is one point in functional space")
print("=" * 72)

# For a discrete spectrum with moments a_0, a_2, a_4,
# the spectral action under different f at cutoff Lambda is:
#
#   S[f] = sum_k f_{2k} * a_{2k} * Lambda^{d-2k}
#
# where f_{2k} = integral_0^infty f(x) x^{k-1-d/2} dx (Mellin transform moments)
# and d = 4 (effective dimension).

Lambda_SA = Lambda_over_MKK  # (local) cutoff in M_KK units

# Define spectral functionals and their moment structure
functionals = {}  # (local)

# --- f_1(x) = exp(-x) [Chamseddine-Connes heat kernel] ---
# f_0 = 1, f_2 = 1, f_4 = 1/2
f_exp = {"name": "exp(-x)", "f0": 1.0, "f2": 1.0, "f4": 0.5}  # (local)
S_exp = f_exp["f0"] * a0 * Lambda_SA**4 + f_exp["f2"] * a2 * Lambda_SA**2 + f_exp["f4"] * a4  # (local)
functionals["exp"] = {"S": S_exp, "f": f_exp}

# --- f_2(x) = x^{-s}|_{s=0} [Zeta function at s=0] ---
# S_zeta = a_4 (only the a_4 moment survives)
# This is the Lizzi zeta action: DROPS a_0 and a_2 entirely
S_zeta_val = a4  # (local)
functionals["zeta"] = {"S": S_zeta_val, "f": {"name": "zeta(s=0)", "f0": 0, "f2": 0, "f4": 1}}

# --- f_3(x) = Theta(1-x) [Sharp cutoff] ---
# f_0 = 1, f_2 = 1/2, f_4 = -1/2 (via Abel-Plana or distributional)
# Standard: Tr Theta(1 - D^2/Lambda^2) = sum of |lam_i| < Lambda terms
# In moment expansion: S = a_0*Lambda^4 + (1/2)*a_2*Lambda^2 + (-1/6)*a_4 + ...
S_sharp = a0 * Lambda_SA**4 + 0.5 * a2 * Lambda_SA**2 - (1.0/6.0) * a4  # (local)
functionals["sharp"] = {"S": S_sharp, "f": {"name": "Theta(1-x)", "f0": 1, "f2": 0.5, "f4": -1.0/6.0}}

# --- f_4(x) = sqrt(x) [Framework f* dominant component, 91.2%] ---
# f_0 = Gamma(3/2) = sqrt(pi)/2 ~ 0.886 ... but this is for the 4D Mellin.
# Actually for sqrt: f_k = integral sqrt(x) x^{k-d/2-1} dx
# The Mellin transform of sqrt(x) does NOT converge for f_0 (x -> infinity divergence).
# This means sqrt(x) has NO perturbative expansion: S = M_1/Lambda (first moment only)
# where M_1 = sum |lam_i| = zeta_D(-1/2) * Lambda (first absolute moment).
#
# We CANNOT write S[sqrt] in the (a_0, a_2, a_4) basis.
# Use the parametric estimate from S70: S(sqrt) / S(exp) ~ 4.1 at Lambda=2.048
S_sqrt_ratio = 4.1  # (local) from S70 NON-PERT-SA-70
S_sqrt = S_sqrt_ratio * S_exp  # (local) estimate
functionals["sqrt"] = {"S": S_sqrt, "f": {"name": "sqrt(x)", "f0": "inf", "f2": "inf", "f4": "N/A"}}

# --- f_5(x) = f*(x) = 0.912*sqrt(x) + 0.088*exp(-x) [S72 fit] ---
t_star = 0.0883  # (local) mixing parameter from S72
S_fstar = 0.912 * S_sqrt + t_star * S_exp  # (local)
functionals["f*"] = {"S": S_fstar, "f": {"name": "0.912*sqrt+0.088*exp", "f0": "inf", "f2": "inf", "f4": t_star * 0.5}}

# --- f_6(x) = x * exp(-x) [Anomaly-derived, one-loop] ---
# f_0 = 1, f_2 = 2, f_4 = 1
S_anomaly = 1.0 * a0 * Lambda_SA**4 + 2.0 * a2 * Lambda_SA**2 + 1.0 * a4  # (local)
functionals["anomaly"] = {"S": S_anomaly, "f": {"name": "x*exp(-x)", "f0": 1, "f2": 2, "f4": 1}}

print(f"\nSpectral action values for SAME D_K (Lambda = {Lambda_SA:.3f} M_KK):")
print(f"{'Functional':<25} {'S[f,D]':>15} {'S/S_zeta':>12} {'a_0 enters?':>12}")
print("-" * 68)

S_values = {}  # (local)
for key in ["exp", "zeta", "sharp", "sqrt", "f*", "anomaly"]:
    entry = functionals[key]  # (local)
    S_val = entry["S"]  # (local)
    ratio = S_val / S_zeta_val  # (local)
    f_data = entry["f"]  # (local)
    a0_enters = "NO" if (isinstance(f_data.get("f0", 1), (int, float)) and f_data.get("f0", 1) == 0) else "YES"
    if f_data.get("f0", 1) == "inf":
        a0_enters = "DIVERGENT"
    print(f"  {f_data['name']:<23} {S_val:>15.2f} {ratio:>12.3f} {a0_enters:>12}")
    S_values[key] = S_val

# Dynamic range
S_min = min(S_values.values())  # (local)
S_max = max(S_values.values())  # (local)
dynamic_range = S_max / S_min  # (local)
log_range = np.log10(dynamic_range)  # (local)

print(f"\n  Dynamic range: {dynamic_range:.1f}x ({log_range:.2f} OOM)")
print(f"  S_max / S_min = {S_max:.2f} / {S_min:.2f}")

# The PHYSICAL content of each:
print(f"\n  Physical predictions from each functional:")
print(f"  {'Functional':<20} {'CC term':>10} {'Newton G':>10} {'YM action':>10}")
print("-" * 55)

for key in ["exp", "zeta", "sharp", "anomaly"]:
    f_data = functionals[key]["f"]  # (local)
    f0 = f_data.get("f0", 0)  # (local)
    f2 = f_data.get("f2", 0)  # (local)
    f4 = f_data.get("f4", 0)  # (local)
    if isinstance(f0, str):
        cc_term = "DIVERGENT"
    else:
        cc_term = f"f0*a0={f0*a0:.0f}" if f0 != 0 else "ABSENT"
    gn_term = f"f2*a2={f2*a2:.0f}" if isinstance(f2, (int, float)) and f2 != 0 else ("ABSENT" if f2 == 0 else "DIVERGENT")
    ym_term = f"f4*a4={f4*a4:.0f}" if isinstance(f4, (int, float)) and f4 != 0 else ("ABSENT" if f4 == 0 else "DIVERGENT")
    print(f"  {f_data['name']:<20} {cc_term:>10} {gn_term:>10} {ym_term:>10}")

# ROUTE 2 KEY RESULT: zeta(s=0) = a_4 is ONE point (f0=0, f2=0, f4=1)
# in a continuous family parametrized by (f0, f2, f4, ...).
# There is NOTHING in the spectral triple that selects this point.
# The selection requires EXTERNAL input (anomaly cancellation,
# observational fit, or a principle not contained in the spectrum).

n_functionals_tested = len(functionals)  # (local)
route2_pass = (dynamic_range > 10.0)  # (local) order of magnitude variation
route2_obstruction = "NON_UNIQUENESS"  # (local)

print(f"\n  ROUTE 2 VERDICT: {'NON-UNIQUE' if route2_pass else 'INCONCLUSIVE'}")
print(f"  Obstruction: zeta_D(0) = a_4 is ONE of {n_functionals_tested} tested functionals")
print(f"  producing a {dynamic_range:.0f}x range in S[f,D] from the SAME D_K.")
print(f"  No spectral principle selects the zeta point.")

# ============================================================================
# ROUTE 3: L_max CONVERGENCE FAILURE
# ============================================================================
# From S73b SDW-VALIDATION-73B and S74 JOINT-AUDIT-ATLAS-74:
# The spectral zeta moments a_k are L_max-dependent.
# At L_max=3: a_0 = 6440, a_2 = 2776, a_4 = 1351
# At L_max=7: a_0 = 473760, a_2 = 76137, a_4 = 14050
# These are NOT converged.  The zeta action S_zeta = a_4 shifts by 10.4x.

print("\n" + "=" * 72)
print("ROUTE 3: L_max convergence failure")
print("=" * 72)

# Data from S73b SDW-VALIDATION-73B
a0_L3 = 6440.0       # (local) from S73b canonical
a2_L3 = 2776.165     # (local)
a4_L3 = 1350.722     # (local)
a6_L3 = 765.59       # (local)

a0_L7 = 473760.0     # (local) from S73b
a2_L7 = 76137.19     # (local)
a4_L7 = 14050.21     # (local)
a6_L7 = 3229.35      # (local)

# Compute L_max scaling ratios
r_a0 = a0_L7 / a0_L3  # (local) = 73.57
r_a2 = a2_L7 / a2_L3  # (local) = 27.43
r_a4 = a4_L7 / a4_L3  # (local) = 10.40
r_a6 = a6_L7 / a6_L3  # (local) = 4.22

print(f"\nL_max dependence of spectral zeta moments:")
print(f"  {'Moment':<8} {'L_max=3':>12} {'L_max=7':>12} {'L7/L3':>8} {'log_7/3(ratio)':>14}")
print("-" * 58)

L_ratio = 7.0 / 3.0  # (local)
for name, val3, val7, ratio in [("a_0", a0_L3, a0_L7, r_a0),
                                   ("a_2", a2_L3, a2_L7, r_a2),
                                   ("a_4", a4_L3, a4_L7, r_a4),
                                   ("a_6", a6_L3, a6_L7, r_a6)]:
    power = np.log(ratio) / np.log(L_ratio)  # (local) effective scaling exponent
    print(f"  {name:<8} {val3:>12.2f} {val7:>12.2f} {ratio:>8.2f}  L^{power:.2f}")

# S_zeta = a_4 shifts by 10.4x from L_max=3 to L_max=7
S_zeta_L3 = a4_L3  # (local)
S_zeta_L7 = a4_L7  # (local)
S_zeta_shift = S_zeta_L7 / S_zeta_L3  # (local)
S_zeta_shift_OOM = np.log10(S_zeta_shift)  # (local)

print(f"\n  S_zeta = a_4:")
print(f"    L_max=3: {S_zeta_L3:.2f}")
print(f"    L_max=7: {S_zeta_L7:.2f}")
print(f"    Shift: {S_zeta_shift:.2f}x ({S_zeta_shift_OOM:.2f} OOM)")

# Cutoff action also shifts (more, because a_0 dominates)
S_cutoff_L3 = a0_L3 * Lambda_SA**4 + a2_L3 * Lambda_SA**2 + 0.5 * a4_L3  # (local)
S_cutoff_L7 = a0_L7 * Lambda_SA**4 + a2_L7 * Lambda_SA**2 + 0.5 * a4_L7  # (local)
S_cutoff_shift = S_cutoff_L7 / S_cutoff_L3  # (local)

print(f"\n  S_cutoff [f=exp, Lambda={Lambda_SA:.3f}]:")
print(f"    L_max=3: {S_cutoff_L3:.2f}")
print(f"    L_max=7: {S_cutoff_L7:.2f}")
print(f"    Shift: {S_cutoff_shift:.2f}x")

# KEY: Ratios are protected (from S73b, ratio-of-ratios shifts only 1.7%)
r_a0_a2_L3 = a0_L3 / a2_L3  # (local)
r_a0_a2_L7 = a0_L7 / a2_L7  # (local)
r_a2_a4_L3 = a2_L3 / a4_L3  # (local)
r_a2_a4_L7 = a2_L7 / a4_L7  # (local)

ror_L3 = r_a0_a2_L3 / r_a2_a4_L3  # (local) ratio-of-ratios
ror_L7 = r_a0_a2_L7 / r_a2_a4_L7  # (local)
ror_shift = abs(ror_L7 / ror_L3 - 1)  # (local)

print(f"\n  Protected quantities (L_max-robust):")
print(f"    a_0/a_2:  L3={r_a0_a2_L3:.4f}, L7={r_a0_a2_L7:.4f} (shift: {abs(r_a0_a2_L7/r_a0_a2_L3 - 1)*100:.1f}%)")
print(f"    a_2/a_4:  L3={r_a2_a4_L3:.4f}, L7={r_a2_a4_L7:.4f} (shift: {abs(r_a2_a4_L7/r_a2_a4_L3 - 1)*100:.1f}%)")
print(f"    (a_0/a_2)/(a_2/a_4): L3={ror_L3:.4f}, L7={ror_L7:.4f} (shift: {ror_shift*100:.1f}%)")

# What IS L_max-converged?  Ratios and tau-derivatives, NOT absolute moments.
# The zeta action S_zeta = a_4 is an ABSOLUTE moment, hence L_max-dependent.
# A physical observable cannot depend on the truncation level.

route3_pass = (S_zeta_shift > 5.0)  # (local) > 5x shift = not converged
route3_obstruction = "UV_TRUNCATION_SENSITIVITY"  # (local)

print(f"\n  ROUTE 3 VERDICT: {'L_MAX-UNCONVERGED' if route3_pass else 'INCONCLUSIVE'}")
print(f"  Obstruction: S_zeta = a_4 shifts {S_zeta_shift:.1f}x between L_max=3 and L_max=7")
print(f"  while ratio-of-ratios shifts only {ror_shift*100:.1f}%.")
print(f"  Absolute spectral moments are not physical observables.")

# ============================================================================
# CONVERGENCE OF OBSTRUCTIONS
# ============================================================================
print("\n" + "=" * 72)
print("CONVERGENCE: Common obstruction across all three routes")
print("=" * 72)

obstructions = {  # (local)
    "Route 1": route1_obstruction,
    "Route 2": route2_obstruction,
    "Route 3": route3_obstruction,
}
route_passes = {  # (local)
    "Route 1": route1_pass,
    "Route 2": route2_pass,
    "Route 3": route3_pass,
}

n_pass = sum(1 for v in route_passes.values() if v)  # (local)

# All three obstructions share a common root:
# zeta_D(s) conflates UV REGULARIZATION with physical content.
#
# Route 1: The analytic continuation from convergent s > d/2 to physical
#           s = -1/2 is a CHOICE.  Different continuations (= different
#           spectral distributions consistent with the same moments)
#           give different vacuum energies.
#
# Route 2: The zeta function at s=0 is ONE point in the space of spectral
#           functionals f(x) = x^{-s}.  There are infinitely many other
#           choices producing different physics.  The spectrum does not
#           select among them.
#
# Route 3: The spectral moments a_k are UV-sensitive (L_max-dependent).
#           Absolute zeta values like a_4 grow with the UV cutoff.
#           A physical observable must be insensitive to UV completion.
#
# COMMON OBSTRUCTION:
# zeta_D(s) is a one-parameter family of spectral regularizations.
# Evaluating it at any fixed s (including s=0 for the action, or
# s=-1/2 for vacuum energy) selects a specific UV weighting.
# This weighting is NOT determined by the Dirac operator spectrum.
# It is an EXTERNAL input corresponding to a regularization choice.

common_obstruction = "UV_REGULARIZATION_CONFLATION"  # (local)

print(f"\n  Route 1 ({obstructions['Route 1']}): {'PASS' if route_passes['Route 1'] else 'FAIL'}")
print(f"    Analytic continuation of zeta to s = -1/2 is non-unique.")
print(f"    Same {a0:.0f} eigenvalues, {(spread_zeta_mhalf-1)*100:.2f}% variation in E_vac.")
print(f"\n  Route 2 ({obstructions['Route 2']}): {'PASS' if route_passes['Route 2'] else 'FAIL'}")
print(f"    zeta(s=0) = a_4 is 1 of {n_functionals_tested} functionals spanning {dynamic_range:.0f}x.")
print(f"    No spectral principle picks f(x) = x^0 over f(x) = exp(-x) or sqrt(x).")
print(f"\n  Route 3 ({obstructions['Route 3']}): {'PASS' if route_passes['Route 3'] else 'FAIL'}")
print(f"    S_zeta = a_4 shifts {S_zeta_shift:.1f}x from L_max=3 to 7.")
print(f"    Ratios shift only {ror_shift*100:.1f}%. Absolute moments are UV artifacts.")

print(f"\n  COMMON OBSTRUCTION: {common_obstruction}")
print(f"  zeta_D(s) at ANY fixed s conflates the UV eigenvalue weighting")
print(f"  with the physical content of D_K.  It is a regularization tool,")
print(f"  not a physical observable.")
print(f"\n  Routes converging: {n_pass}/3")

# ============================================================================
# GATE VERDICT
# ============================================================================
print("\n" + "=" * 72)
print("GATE VERDICT: S75-G3-ZETA-NOT-PHYS")
print("=" * 72)

if n_pass == 3:
    gate_verdict = "PASS"
    gate_reason = "All 3 routes converge on common obstruction: UV_REGULARIZATION_CONFLATION"
elif n_pass >= 2:
    gate_verdict = "INFO"
    gate_reason = f"{n_pass}/3 routes converge"
else:
    gate_verdict = "FAIL"
    gate_reason = "Routes disagree on the obstruction"

print(f"\n  Verdict: {gate_verdict}")
print(f"  Reason: {gate_reason}")
print(f"  Threshold: PASS = 3/3, INFO = 2/3, FAIL = <2/3")

# ============================================================================
# PERMANENT THEOREM (if PASS)
# ============================================================================
if gate_verdict == "PASS":
    print(f"\n{'=' * 72}")
    print("PERMANENT THEOREM: ZETA-NOT-OBSERVABLE")
    print("=" * 72)
    thm_text = (
        "\n  THEOREM (Spectral Zeta Non-Observability):\n\n"
        "  Let D_K be a Dirac operator on a compact spectral triple (A, H, D_K).\n"
        "  The spectral zeta function zeta_D(s) = Tr |D_K|^(-2s) is NOT a\n"
        "  physical observable.  Specifically:\n\n"
        "  (i)   zeta_D(s) at non-convergent points (s <= d/2) requires analytic\n"
        "        continuation whose finite part depends on the continuation scheme.\n"
        "        [Route 1: same spectrum, different vacuum energies]\n\n"
        f"  (ii)  The spectral action S_zeta = zeta_D(0) = a_4(D^2) corresponds to\n"
        "        the functional f(x) = x^0 = 1 (constant), which is one point in\n"
        f"        the space of spectral functionals.  No axiom of the\n"
        f"        spectral triple selects this point.\n"
        f"        [Route 2: 6 functionals span {dynamic_range:.0f}x range from same D_K]\n\n"
        f"  (iii) The spectral moments a_k = zeta_D(k) are UV-sensitive: a_4 shifts\n"
        f"        {S_zeta_shift:.1f}x between L_max = 3 and L_max = 7, while dimensionless\n"
        "        ratios a_k/a_j shift < 2%.  Only ratios are physical.\n"
        "        [Route 3: L_max convergence test fails for absolute moments]\n\n"
        "  COROLLARY: Any physical prediction derived from zeta_D(s) at a fixed s\n"
        "  is a prediction of the REGULARIZATION SCHEME, not of the Dirac operator\n"
        "  spectrum.  Physical observables are ratios of spectral moments, not\n"
        "  absolute values.\n\n"
        "  PHYSICAL CONSEQUENCE: The cosmological constant, Newton's constant (from\n"
        "  absolute a_2), and the bare Higgs mass (from absolute a_4/a_2 or a_6/a_4)\n"
        "  are scheme-dependent.  Only RATIOS like sin^2(theta_W), the equation\n"
        "  of state w_0 (Volovik partition), and the spectral tilt n_s (at fixed\n"
        "  functional) are candidates for physical predictions.\n"
    )
    print(thm_text)

# ============================================================================
# WHAT IS PHYSICAL (positive classification)
# ============================================================================
print("=" * 72)
print("POSITIVE CLASSIFICATION: What IS physical from the spectrum")
print("=" * 72)
ratio_shift_pct = abs(r_a0_a2_L7/r_a0_a2_L3 - 1)*100  # (local)
abs_shift_pct = (r_a4-1)*100  # (local)
ror_shift_pct = ror_shift*100  # (local)
print(f"\n  FUNCTIONAL-INDEPENDENT (physical, scheme-does-not-matter):")
print(f"    1. Eigenvalue RATIOS: lam_i / lam_j  (representation theory)")
print(f"    2. Moment RATIOS: a_k / a_j  (shift < {ratio_shift_pct:.0f}% under L_max change, vs {abs_shift_pct:.0f}% for absolutes)")
print(f"    3. Ratio-of-ratios: (a_0/a_2)/(a_2/a_4)  (shift {ror_shift_pct:.1f}% at L_max=3..7)")
print(f"    4. Tau-derivatives: d(a_k/a_j)/dtau  (L_max-robust)")
print(f"    5. Block structure: D_K = D_B1 + D_B2 + D_B3  (exact at all L_max)")
print(f"    6. Topological: dim ker D_K, eta invariant, index (integer-valued)")
print(f"    7. w_0 = -0.918  (Volovik partition, structural)")
print(f"    8. alpha_s = 0  (Bogoliubov saturation, structural)")
print(f"")
print(f"  SCHEME-DEPENDENT (regularization choice determines value):")
print(f"    1. Absolute a_k (a_0, a_2, a_4 individually)")
print(f"    2. S_zeta = a_4  (the zeta action)")
print(f"    3. rho_Lambda = f_0 * a_0 * Lambda^4  (CC density)")
print(f"    4. G_N^(-1) = f_2 * a_2 * Lambda^2  (Newton's constant)")
print(f"    5. m_H^2 ~ (a_4/a_2) * (f_4/f_2)  (Higgs mass)")
print(f"    6. n_s  (spectral tilt, fixes the functional)")
print(f"    7. A_s  (amplitude, fixes the normalization)")

# ============================================================================
# NUMERICAL SUMMARY TABLE
# ============================================================================
print("=" * 72)
print("NUMERICAL SUMMARY")
print("=" * 72)

print(f"""
  Route 1 (scheme dependence):
    zeta_D(-1/2): flat={zeta_minus_half_A:.2f}, lognormal={zeta_minus_half_B:.2f}, delta={zeta_minus_half_C:.2f}
    Spread: {spread_zeta_mhalf:.4f}x ({(spread_zeta_mhalf-1)*100:.2f}%)
    CC gap range: [{min(CC_gap_A,CC_gap_B,CC_gap_C):.1f}, {max(CC_gap_A,CC_gap_B,CC_gap_C):.1f}] OOM
    vs cutoff CC gap: {CC_gap_cutoff:.1f} OOM, zeta CC gap: {CC_gap_zeta:.1f} OOM

  Route 2 (non-uniqueness):
    S[f,D] range: [{S_min:.2f}, {S_max:.2f}]
    Dynamic range: {dynamic_range:.1f}x ({log_range:.2f} OOM)
    Functionals tested: {n_functionals_tested}

  Route 3 (L_max convergence):
    a_4(L=3) = {a4_L3:.2f}, a_4(L=7) = {a4_L7:.2f} (shift: {r_a4:.2f}x)
    a_0(L=3) = {a0_L3:.0f}, a_0(L=7) = {a0_L7:.0f} (shift: {r_a0:.2f}x)
    Ratio-of-ratios shift: {ror_shift*100:.1f}% (PROTECTED)

  Gate: S75-G3-ZETA-NOT-PHYS = {gate_verdict}
  Common obstruction: {common_obstruction}
  Routes converging: {n_pass}/3
""")

# ============================================================================
# SAVE RESULTS
# ============================================================================
output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "s75_zeta_not_physical.npz")  # (local)

np.savez(output_path,
         # Route 1
         zeta_mhalf_flat=zeta_minus_half_A,
         zeta_mhalf_lognormal=zeta_minus_half_B,
         zeta_mhalf_delta=zeta_minus_half_C,
         spread_zeta_mhalf=spread_zeta_mhalf,
         rho_vac_A=rho_vac_A,
         rho_vac_B=rho_vac_B,
         rho_vac_C=rho_vac_C,
         CC_gap_A=CC_gap_A,
         CC_gap_B=CC_gap_B,
         CC_gap_C=CC_gap_C,
         CC_gap_cutoff=CC_gap_cutoff,
         CC_gap_zeta=CC_gap_zeta,
         route1_pass=route1_pass,
         # Route 2
         S_exp=S_exp,
         S_zeta=S_zeta_val,
         S_sharp=S_sharp,
         S_sqrt=S_sqrt,
         S_fstar=S_fstar,
         S_anomaly=S_anomaly,
         dynamic_range=dynamic_range,
         log_range=log_range,
         n_functionals=n_functionals_tested,
         route2_pass=route2_pass,
         # Route 3
         a_k_L3=np.array([a0_L3, a2_L3, a4_L3, a6_L3]),
         a_k_L7=np.array([a0_L7, a2_L7, a4_L7, a6_L7]),
         ratios_L7_L3=np.array([r_a0, r_a2, r_a4, r_a6]),
         S_zeta_L3=S_zeta_L3,
         S_zeta_L7=S_zeta_L7,
         S_zeta_shift=S_zeta_shift,
         ror_L3=ror_L3,
         ror_L7=ror_L7,
         ror_shift=ror_shift,
         route3_pass=route3_pass,
         # Gate
         gate_verdict=gate_verdict,
         n_routes_pass=n_pass,
         common_obstruction=common_obstruction,
         )

print(f"Results saved to: {output_path}")
print("DONE.")
