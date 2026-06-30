#!/usr/bin/env python3
"""
s63_nonlocal_cc_spectral.py — CC Beyond Seeley-DeWitt: Nonlocal Form Factor
=============================================================================

Gate: NONLOCAL-CC-SPECTRAL-63
Pre-registered criterion:
  PASS  if F(Box) is entire-function (IDG-type), evades Weinberg no-go
  FAIL  if F(Box) is polynomial (local), Weinberg no-go binds

Method:
  For the product geometry M^4 x F with D = D_M x 1 + gamma_5 x D_F,
  the spectral action Tr[f(D^2/Lambda^2)] generates an effective gravitational
  action. The second variation with respect to the 4D metric perturbation h_{mu nu}
  produces a form factor F(Box_4D / Lambda^2) in the graviton propagator.

  KEY DERIVATION:
  ===============
  D^2 = D_M^2 x 1 + 1 x D_F^2  (at zeroth order in fluctuations)

  The 4D Laplacian Box_4D acts on D_M^2. The internal eigenvalues {lambda_n^2}
  of D_F^2 (= D_K^2 for us) give the KK tower.

  The spectral action response to a 4D scalar curvature perturbation is:

  delta^2 S / delta R(x) delta R(y) = sum_n d_n * f''((Box_4D + lambda_n^2)/Lambda^2)
                                        * delta^4(x-y)   (in Fourier space ->)

  In momentum space (p = 4D Euclidean momentum):

  F(p^2) = sum_n d_n * f''((p^2 + lambda_n^2) / Lambda^2)

  This is the graviton propagator form factor. If f is smooth/entire,
  F(p^2) inherits the analyticity of f. If f is sharp cutoff, F(p^2) is
  distributional.

  For the CC problem, the key quantity is F(0) vs F(p^2) at large p^2:
  - If F(p^2) -> 0 faster than any power as p -> infinity (ENTIRE function),
    then the theory is "infinite derivative gravity" (IDG) type and
    Weinberg's no-go theorem does not apply (the no-go requires locality).
  - If F(p^2) is polynomial in p^2, the theory is local and the no-go binds.

  THEOREM (UNEXPANDED-SA-45, PERMANENT):
  For a FINITE spectrum {lambda_n, d_n} and smooth cutoff f, the spectral
  action S(Lambda) = sum_n d_n f(lambda_n^2/Lambda^2) is EXACTLY its Taylor
  series in 1/Lambda^2 for Lambda > lambda_max. This means S is polynomial.

  However, F(p^2) involves BOTH the cutoff Lambda AND the momentum p^2.
  The question is whether the p^2-dependence is polynomial or not.

  For f(x) = exp(-x) (heat kernel), f''(x) = exp(-x), and:
    F_HK(p^2) = sum_n d_n exp(-(p^2 + lambda_n^2)/Lambda^2)
              = exp(-p^2/Lambda^2) * sum_n d_n exp(-lambda_n^2/Lambda^2)
              = exp(-p^2/Lambda^2) * K(1/Lambda^2)

  This IS an entire function of p^2! The Gaussian decay is inherited
  from the heat kernel cutoff, regardless of the spectrum being finite.

  The question becomes: does this survive for general cutoff functions f?

  TEST: Compute F(p^2) for multiple cutoff functions and test:
  (a) Gaussian / heat kernel: f(x) = exp(-x)
  (b) Erfc cutoff: f(x) = erfc(sqrt(x))
  (c) Optimized cutoff (Chamseddine-Connes): f(x) = Theta(1-x) (sharp)
  (d) Polynomial-modified Gaussian: f(x) = (1 + x + x^2/2) exp(-x)

  For each, compute F(p^2) and fit to:
    log|F(p^2)| = -alpha * p^2 + beta * log(p^2) + gamma
  If alpha > 0, F is exponentially suppressed -> entire function -> PASS
  If alpha ~ 0, F is polynomial -> FAIL

Session: S63   Agent: Connes-NCG-Theorist
"""

import numpy as np
import sys
import os
sys.path.insert(0, '.')
from canonical_constants import (
    M_KK, M_KK_gravity, M_KK_kerner, M_Pl_reduced,
    rho_Lambda_obs, a0_fold, a2_fold, a4_fold,
    Vol_SU3_Haar, PI, tau_fold, Lambda_obs_MP4
)
from scipy.special import erfc
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

print("=" * 78)
print("NONLOCAL-CC-SPECTRAL-63: CC Beyond Seeley-DeWitt")
print("=" * 78)

# ============================================================
# Section 1: Load D_K eigenvalue spectrum at fold
# ============================================================

# Use the HK oscillation data (992 modes with degeneracies at fold)
d_hk = np.load('s61_hk_oscillation.npz', allow_pickle=True)
omega = d_hk['omega']      # |D_K| eigenvalues (M_KK units)
dim2 = d_hk['dim2']        # PW degeneracy weights
N_modes = len(omega)

# Also load the higher-resolution weyl law data for cross-check
d_weyl = np.load('s61_weyl_law.npz', allow_pickle=True)
omega_hr = d_weyl['omega_sorted']     # 18624 eigenvalues (L_max=7)
mult_hr = d_weyl['pw_mult_sorted']    # PW multiplicities

# D_K^2 eigenvalues
lambda_sq = omega**2                  # (992,)
lambda_sq_hr = omega_hr**2            # (18624,)

print(f"\nInput spectrum (L_max <= 6, 992 modes):")
print(f"  lambda^2 range: [{lambda_sq.min():.6f}, {lambda_sq.max():.6f}] M_KK^2")
print(f"  Total degeneracy: {dim2.sum():.0f}")
print(f"  Distinct lambda^2 values: {len(np.unique(np.round(lambda_sq, 6)))}")

print(f"\nHigh-res spectrum (L_max=7, 18624 modes):")
print(f"  lambda^2 range: [{lambda_sq_hr.min():.6f}, {lambda_sq_hr.max():.6f}] M_KK^2")
print(f"  Total PW multiplicity: {mult_hr.sum():.0f}")

# ============================================================
# Section 2: Define cutoff functions and their second derivatives
# ============================================================

def f_gaussian(x):
    """Heat kernel / Gaussian cutoff: f(x) = exp(-x)"""
    return np.exp(-x)

def f_gaussian_pp(x):
    """f''(x) for Gaussian"""
    return np.exp(-x)

def f_erfc(x):
    """Erfc cutoff: f(x) = erfc(sqrt(x)) for x > 0"""
    return erfc(np.sqrt(np.maximum(x, 0)))

def f_erfc_pp(x):
    """f''(x) for erfc(sqrt(x))"""
    # f'(x) = -1/(sqrt(pi*x)) * exp(-x) for x > 0
    # f''(x) = (1/(2*sqrt(pi)*x^{3/2}) - 1/(sqrt(pi*x))) * exp(-x)
    #        = exp(-x) / (sqrt(pi)) * (1/(2*x^{3/2}) - 1/sqrt(x))
    x_safe = np.maximum(x, 1e-30)
    return np.exp(-x_safe) / np.sqrt(PI) * (1.0/(2.0*x_safe**1.5) - 1.0/np.sqrt(x_safe))

def f_sharp(x):
    """Sharp cutoff: f(x) = Theta(1 - x)"""
    return np.where(x < 1.0, 1.0, 0.0)

def f_sharp_pp(x):
    """f''(x) for sharp cutoff = delta'(1-x) (distributional)
    Approximate with narrow Gaussian derivative"""
    eps = 0.01
    return (1.0/(eps*np.sqrt(2*PI))) * (x - 1.0)/eps**2 * np.exp(-0.5*((x-1.0)/eps)**2)

def f_poly_gauss(x):
    """Polynomial-modified Gaussian: f(x) = (1 + x + x^2/2) exp(-x)
    This preserves first 3 moments while keeping Gaussian UV decay."""
    return (1.0 + x + 0.5*x**2) * np.exp(-x)

def f_poly_gauss_pp(x):
    """f''(x) for (1+x+x^2/2)*exp(-x)"""
    # f(x) = sum_{k=0}^{2} x^k/k! * exp(-x)
    # f'(x) = (1 + x) exp(-x) + (1/2)(2x)exp(-x) - (1+x+x^2/2)exp(-x)
    #       = exp(-x) [(1+x+x) - (1+x+x^2/2)] = exp(-x)[x - x^2/2]
    # Actually let me compute this carefully
    # f(x) = P(x) e^{-x} where P(x) = 1 + x + x^2/2
    # f'(x) = (P'(x) - P(x)) e^{-x} = (1+x - 1 - x - x^2/2) e^{-x} = (-x^2/2) e^{-x}
    # f''(x) = (-x + x^2/2) e^{-x} = x(x/2 - 1) e^{-x}
    return x * (x/2.0 - 1.0) * np.exp(-x)

def f_bw(x):
    """Butterworth cutoff order 4: f(x) = 1/(1+x^4)
    Smooth but slower-than-exponential decay."""
    return 1.0 / (1.0 + x**4)

def f_bw_pp(x):
    """f''(x) for 1/(1+x^4)"""
    # f'(x) = -4x^3 / (1+x^4)^2
    # f''(x) = (-12x^2(1+x^4)^2 + 4x^3*2(1+x^4)*4x^3) / (1+x^4)^4
    #        = (-12x^2(1+x^4) + 32x^6) / (1+x^4)^3
    denom = (1.0 + x**4)**3
    numer = -12.0*x**2*(1.0 + x**4) + 32.0*x**6
    return numer / denom

cutoffs = {
    'Gaussian': (f_gaussian, f_gaussian_pp),
    'Erfc': (f_erfc, f_erfc_pp),
    'Sharp (reg.)': (f_sharp, f_sharp_pp),
    'Poly-Gauss': (f_poly_gauss, f_poly_gauss_pp),
    'Butterworth-4': (f_bw, f_bw_pp),
}

# ============================================================
# Section 3: Compute Form Factor F(p^2) for each cutoff
# ============================================================

# Momentum grid in M_KK units
# p^2 ranges from 0 to ~50 Lambda^2 (well into UV)
# Lambda is the NCG cutoff ~ O(1) in M_KK units (= lambda_max for sharp)
Lambda_sq = lambda_sq.max()  # = 4.246 (highest D_K^2 eigenvalue)
Lambda = np.sqrt(Lambda_sq)

print(f"\nLambda (= sqrt(max lambda_n^2)): {Lambda:.4f} M_KK")
print(f"Lambda^2: {Lambda_sq:.4f} M_KK^2")

# p^2 grid: log-spaced from 0.01 to 1000 Lambda^2
N_p = 500
p_sq = np.logspace(-2, 3, N_p) * Lambda_sq
p_sq_over_Lam2 = p_sq / Lambda_sq

print(f"\np^2 range: [{p_sq.min():.4f}, {p_sq.max():.2f}] M_KK^2")
print(f"p^2/Lambda^2 range: [{p_sq_over_Lam2.min():.4f}, {p_sq_over_Lam2.max():.2f}]")

# For each cutoff, compute F(p^2) = sum_n d_n * f''((p^2 + lambda_n^2) / Lambda^2)
results = {}

for name, (f_func, fpp_func) in cutoffs.items():
    # F(p^2) = sum_n d_n * f''((p^2 + lambda_n^2) / Lambda^2)
    # Shape: (N_p, N_modes) -> sum over modes -> (N_p,)
    arg = (p_sq[:, None] + lambda_sq[None, :]) / Lambda_sq  # (N_p, N_modes)
    fpp_vals = fpp_func(arg)  # (N_p, N_modes)
    F_p = np.sum(dim2[None, :] * fpp_vals, axis=1)  # (N_p,)

    # Normalize: F(0) sets the scale
    F_0 = F_p[0]

    results[name] = {
        'F_p': F_p,
        'F_0': F_0,
        'F_normalized': F_p / np.abs(F_0) if F_0 != 0 else F_p,
    }

    print(f"\n--- {name} ---")
    print(f"  F(0) = {F_0:.6e}")
    print(f"  F(Lambda^2) = {F_p[np.argmin(np.abs(p_sq - Lambda_sq))]:.6e}")
    print(f"  F(10*Lambda^2) = {F_p[np.argmin(np.abs(p_sq - 10*Lambda_sq))]:.6e}")
    print(f"  F(100*Lambda^2) = {F_p[np.argmin(np.abs(p_sq - 100*Lambda_sq))]:.6e}")

# ============================================================
# Section 4: Analyticity Classification
# ============================================================

print("\n" + "=" * 78)
print("ANALYTICITY CLASSIFICATION OF F(p^2)")
print("=" * 78)

# For each cutoff, fit log|F(p^2)| in the UV regime (p^2 >> Lambda^2)
# to discriminate:
#   Entire (IDG): log|F| ~ -alpha * p^2/Lambda^2  (alpha > 0)
#   Power-law:    log|F| ~ -n * log(p^2/Lambda^2)
#   Polynomial:   F = polynomial in p^2 (finite Taylor)

classification = {}

for name, res in results.items():
    F_p = res['F_p']
    F_abs = np.abs(F_p)

    # UV regime: p^2/Lambda^2 > 3 (well above internal modes)
    uv_mask = p_sq_over_Lam2 > 3.0
    if np.sum(uv_mask) < 20:
        print(f"\n{name}: insufficient UV data points")
        continue

    p2_uv = p_sq_over_Lam2[uv_mask]
    F_uv = F_abs[uv_mask]

    # Handle zeros/near-zeros
    nonzero = F_uv > 1e-300
    if np.sum(nonzero) < 10:
        print(f"\n{name}: F(p^2) -> 0 in UV (sharp cutoff behavior)")
        classification[name] = 'COMPACT_SUPPORT'
        continue

    log_F = np.log(F_uv[nonzero])
    p2_nz = p2_uv[nonzero]

    # Fit 1: Exponential decay  log|F| = -alpha * p^2/L^2 + const
    # Linear fit in p^2/L^2
    A_exp = np.vstack([p2_nz, np.ones_like(p2_nz)]).T
    coeffs_exp, residuals_exp, _, _ = np.linalg.lstsq(A_exp, log_F, rcond=None)
    alpha_exp = -coeffs_exp[0]
    resid_exp = np.sum((log_F - A_exp @ coeffs_exp)**2) / len(log_F)

    # Fit 2: Power-law decay  log|F| = -n * log(p^2/L^2) + const
    log_p2 = np.log(p2_nz)
    A_pow = np.vstack([log_p2, np.ones_like(log_p2)]).T
    coeffs_pow, residuals_pow, _, _ = np.linalg.lstsq(A_pow, log_F, rcond=None)
    n_pow = -coeffs_pow[0]
    resid_pow = np.sum((log_F - A_pow @ coeffs_pow)**2) / len(log_F)

    # Fit 3: Combined  log|F| = -alpha * p^2/L^2 - n * log(p^2/L^2) + const
    A_comb = np.vstack([p2_nz, log_p2, np.ones_like(p2_nz)]).T
    coeffs_comb, _, _, _ = np.linalg.lstsq(A_comb, log_F, rcond=None)
    alpha_comb = -coeffs_comb[0]
    n_comb = -coeffs_comb[1]
    resid_comb = np.sum((log_F - A_comb @ coeffs_comb)**2) / len(log_F)

    # Classification
    if alpha_exp > 0.01 and resid_exp < resid_pow * 2.0:
        cls = 'ENTIRE_FUNCTION'
    elif n_pow > 0.5 and resid_pow < resid_exp * 2.0:
        cls = 'POWER_LAW'
    else:
        cls = 'POLYNOMIAL'

    classification[name] = cls

    print(f"\n--- {name} ---")
    print(f"  Exponential fit: alpha = {alpha_exp:.6f}, MSE = {resid_exp:.6e}")
    print(f"  Power-law fit:   n = {n_pow:.4f}, MSE = {resid_pow:.6e}")
    print(f"  Combined fit:    alpha = {alpha_comb:.6f}, n = {n_comb:.4f}, MSE = {resid_comb:.6e}")
    print(f"  => Classification: {cls}")

    results[name]['alpha_exp'] = alpha_exp
    results[name]['n_pow'] = n_pow
    results[name]['alpha_comb'] = alpha_comb
    results[name]['n_comb'] = n_comb
    results[name]['resid_exp'] = resid_exp
    results[name]['resid_pow'] = resid_pow
    results[name]['resid_comb'] = resid_comb

# ============================================================
# Section 5: ANALYTICAL PROOF — Entire-Function Structure
# ============================================================

print("\n" + "=" * 78)
print("ANALYTICAL PROOF: ENTIRE-FUNCTION STRUCTURE")
print("=" * 78)

# THEOREM: For any cutoff f(x) that is an entire function of x
# (or at least analytic on x > 0), the form factor
#   F(p^2) = sum_n d_n f''((p^2 + lambda_n^2) / Lambda^2)
# is an entire function of p^2 if and only if f'' is entire.
#
# PROOF:
# F(z) = sum_n d_n f''((z + lambda_n^2)/Lambda^2)  for z = p^2 in C
# Each term d_n f''((z + lambda_n^2)/Lambda^2) is entire in z if f'' is entire.
# Finite sum of entire functions is entire.
# QED for Gaussian (f'' = exp(-x), entire in C).
#
# For the sharp cutoff, f''(x) = delta'(1-x) (distributional),
# so F(p^2) = sum_n d_n delta'(1 - (p^2+lambda_n^2)/Lambda^2)
# = sum of delta functions at p^2 = Lambda^2 - lambda_n^2.
# This is NOT a function, it's a distribution -> not entire.
#
# CRITICAL OBSERVATION:
# The spectrum {lambda_n^2} is FINITE (finite truncation of SU(3)).
# For Gaussian cutoff, F(z) = exp(-z/Lambda^2) * C where
# C = sum_n d_n exp(-lambda_n^2/Lambda^2) is a NUMBER.
# So F(z) = C * exp(-z/Lambda^2) — EXACTLY Gaussian decay.
#
# For more general entire cutoffs f, the form factor is a finite sum
# of translates of f'', hence entire.
#
# KEY STRUCTURAL RESULT:
# The nonlocality of F(p^2) is INHERITED from the cutoff function f,
# not from the spectrum. A finite spectrum cannot generate nonlocality.
# This is consistent with UNEXPANDED-SA-45: for finite spectra,
# the spectral action is polynomial in 1/Lambda^2 at fixed p.
# But at fixed Lambda, F(p^2) can be nonlocal if f is.

print("""
THEOREM (NONLOCAL FORM FACTOR):
  Let {lambda_n, d_n}_{n=1}^N be a finite spectrum (the D_K eigenvalues
  of the internal space F = SU(3) with PW truncation at L_max).
  Let f: R -> R be the cutoff function.
  Define the gravitational form factor:
    F(p^2) = sum_{n=1}^N d_n * f''((p^2 + lambda_n^2) / Lambda^2)

  Then:
  (i)   If f is entire (e.g., Gaussian, erfc), then F(p^2) is entire in p^2.
  (ii)  If f has compact support (sharp cutoff), F(p^2) is distributional.
  (iii) If f is rational (Butterworth), F(p^2) has poles at
        p^2 = -lambda_n^2 + Lambda^2 * z_k  where z_k are poles of f''.

  PROOF: Finite sum of translates of f''(z/Lambda^2) evaluated at
         z + const. Translation preserves analyticity class. QED.

  COROLLARY: The analyticity of the form factor is CUTOFF-DEPENDENT.
  It is NOT an intrinsic property of the spectral triple.
  The spectral triple (A, H, D) determines the SPECTRUM, not the cutoff f.
  The choice of f is additional physical input.
""")

# ============================================================
# Section 6: Quantitative Analysis — Gaussian Case
# ============================================================

print("=" * 78)
print("QUANTITATIVE ANALYSIS: GAUSSIAN CUTOFF (f = exp(-x))")
print("=" * 78)

# For Gaussian: F(p^2) = exp(-p^2/Lambda^2) * sum_n d_n exp(-lambda_n^2/Lambda^2)
# This is EXACT (not approximate)

K_at_1 = np.sum(dim2 * np.exp(-lambda_sq / Lambda_sq))
print(f"\nK(1/Lambda^2) = sum_n d_n exp(-lambda_n^2/Lambda^2) = {K_at_1:.6e}")

# Verify against direct computation
F_gauss = results['Gaussian']['F_p']
F_gauss_analytic = K_at_1 * np.exp(-p_sq / Lambda_sq)

# Check factorization (only where both are above underflow)
valid_check = (np.abs(F_gauss) > 1e-250) & (np.abs(F_gauss_analytic) > 1e-250)
ratio = np.ones_like(F_gauss)
ratio[valid_check] = F_gauss[valid_check] / F_gauss_analytic[valid_check]
err_check = np.max(np.abs(ratio[valid_check] - 1))
print(f"Factorization check: max|F_direct/F_analytic - 1| = {err_check:.2e} (over {valid_check.sum()} valid pts)")

# The Gaussian form factor decays as exp(-p^2/Lambda^2)
# At p^2 = Lambda^2: F/F(0) = exp(-1) = 0.368
# At p^2 = 10 Lambda^2: F/F(0) = exp(-10) = 4.54e-5
# At p^2 = 100 Lambda^2: F/F(0) = exp(-100) = 3.72e-44

# In physical units:
# Lambda ~ sqrt(lambda_max^2) M_KK ~ 2.06 M_KK
# M_KK ~ 7.4e16 GeV (gravity route)
# Lambda_phys ~ 1.53e17 GeV
Lambda_phys = Lambda * M_KK
print(f"\nPhysical cutoff: Lambda_phys = {Lambda:.4f} * {M_KK:.3e} = {Lambda_phys:.3e} GeV")

# The CC involves F(0) (zero momentum):
# delta_Lambda = F(0) * (geometric prefactors)
# This is the UV contribution to the CC. The nonlocal part only matters
# if we want to MODIFY the UV behavior.

# Decay scale in momentum space
p_half = Lambda_sq * np.log(2)  # p^2 where F drops to F(0)/2
print(f"\nHalf-power p^2: {p_half:.4f} M_KK^2 = {np.sqrt(p_half):.4f} M_KK")
print(f"  = {np.sqrt(p_half) * M_KK:.3e} GeV")

# ============================================================
# Section 7: Nonlocal CC Suppression Analysis
# ============================================================

print("\n" + "=" * 78)
print("NONLOCAL CC SUPPRESSION ANALYSIS")
print("=" * 78)

# In IDG (Infinite Derivative Gravity), the modification to the
# Newtonian potential is V(r) ~ (1/r) * erf(M_s * r / 2)
# where M_s is the nonlocality scale. This smooths the graviton
# propagator at high momenta, potentially resolving the CC problem.
#
# Capozziello et al. showed that if F(Box) = exp(-Box/M_s^2),
# then the CC contribution from vacuum loops is modified:
#   Lambda_eff = int d^4p / (2pi)^4 * p^2 * F(p^2/M_s^2) / (p^2 + m^2)
# The exponential suppression cuts off the integral at p ~ M_s,
# giving Lambda_eff ~ M_s^4 instead of Lambda^4.
#
# For our spectral action:
# The nonlocality scale IS Lambda (the spectral action cutoff).
# F(p^2) = exp(-p^2/Lambda^2) * K(1/Lambda^2)  (Gaussian case)
# This means the CC gets Lambda_eff ~ Lambda^4, same as Seeley-DeWitt.
# The IDG mechanism does NOT help because the nonlocality scale
# equals the cutoff scale.
#
# For IDG to solve the CC, one needs M_s << Lambda (nonlocality at
# a scale much below the UV cutoff). In our case, M_s = Lambda.

# Compute effective CC for each cutoff
print("\nCC from form factor at p=0 for each cutoff:")
print("-" * 60)

for name, res in results.items():
    F_0 = res['F_0']
    # CC contribution ~ (1/16pi^2) * integral_0^infty dp^2 p^2 F(p^2)
    # For Gaussian F = C exp(-p^2/L^2):
    #   integral = C * L^4 * Gamma(2) = C * L^4
    if name == 'Gaussian':
        CC_integral = K_at_1 * Lambda_sq**2  # = F(0) * Lambda^4
    else:
        # Numerical integration
        dp2 = np.diff(p_sq)
        integrand = p_sq[:-1] * np.abs(res['F_p'][:-1])
        CC_integral = np.sum(integrand * dp2) / (16.0 * PI**2)

    print(f"  {name:20s}: F(0) = {F_0:+.4e}, CC_integral = {CC_integral:.4e}")

# ============================================================
# Section 8: High-Resolution Cross-Check
# ============================================================

print("\n" + "=" * 78)
print("HIGH-RESOLUTION CROSS-CHECK (L_max=7, 18624 modes)")
print("=" * 78)

# Repeat Gaussian analysis with full high-res spectrum
lambda_sq_max_hr = lambda_sq_hr.max()
Lambda_hr = np.sqrt(lambda_sq_max_hr)

K_hr = np.sum(mult_hr * np.exp(-lambda_sq_hr / lambda_sq_max_hr))

print(f"Lambda_hr = {Lambda_hr:.4f} M_KK (vs {Lambda:.4f} at L<=6)")
print(f"K_hr(1/Lambda^2) = {K_hr:.6e} (vs {K_at_1:.6e} at L<=6)")

# Form factor at high-res
F_gauss_hr = K_hr * np.exp(-p_sq / lambda_sq_max_hr)
F_gauss_lr = K_at_1 * np.exp(-p_sq / Lambda_sq)

# The decay rate is 1/Lambda^2, which changes with truncation
ratio_decay = lambda_sq_max_hr / Lambda_sq
print(f"Lambda^2 ratio (hr/lr): {ratio_decay:.4f}")
print(f"This means F_hr decays {ratio_decay:.1f}x SLOWER than F_lr")
print(f"  (larger Lambda => broader form factor)")

# In the continuum limit (L_max -> infinity), Lambda -> infinity
# and F(p^2) = K * exp(-p^2/Lambda^2) -> K * 1 = K (constant!)
# The entire-function structure DISSOLVES in the continuum limit.
# This is the key tension: nonlocality requires finite truncation.

print(f"\n*** CONTINUUM LIMIT ANALYSIS ***")
print(f"As L_max -> infinity:")
print(f"  Lambda^2 -> infinity")
print(f"  exp(-p^2/Lambda^2) -> 1 for all finite p^2")
print(f"  F(p^2) -> sum_n d_n f''((0 + lambda_n^2)/Lambda^2) = F(0)")
print(f"  => F becomes CONSTANT (maximally local) in the continuum")
print(f"  The Gaussian suppression scale goes to infinity with the cutoff.")

# ============================================================
# Section 9: Comparison with IDG Requirements
# ============================================================

print("\n" + "=" * 78)
print("IDG COMPARISON: CAPOZZIELLO REQUIREMENTS")
print("=" * 78)

# IDG requires F(Box) = exp(Box / M_s^2) with M_s << M_Pl
# (note: F acts on Box = -nabla^2, so exp(+Box/M_s^2) in position space
# = exp(-p^2/M_s^2) in momentum space, i.e., UV suppression)
#
# For the CC, Weinberg's no-go says:
# In any local QFT with a finite number of fields,
# the CC receives radiative corrections ~ Lambda^4.
# Renormalization can absorb these, but fine-tuning is required.
#
# IDG evades the no-go by making gravity nonlocal:
# The propagator 1/p^2 -> exp(-p^2/M_s^2) / p^2
# This exponential suppression makes all loop integrals UV-finite.
#
# Our spectral action form factor IS of IDG type (Gaussian),
# but with M_s = Lambda (the cutoff). This means:
# 1. Loop integrals ARE UV-finite (the spectral action is a trace, no renormalization needed)
# 2. But the CC STILL scales as Lambda^4 (the Seeley-DeWitt a_0 term)
# 3. The nonlocality does not SUPPRESS the CC below Lambda^4
#
# For IDG to solve the CC, one needs M_s ~ Lambda_CC^{1/2} ~ 10^{-3} eV
# Our M_s = Lambda ~ M_KK ~ 10^{17} GeV. Off by 20+ orders.

M_s_ours = Lambda * M_KK  # GeV
M_s_IDG = np.sqrt(rho_Lambda_obs)  # ~5e-24 GeV (naive IDG target)
print(f"\nOur nonlocality scale M_s: {M_s_ours:.3e} GeV")
print(f"IDG target M_s (CC scale): {M_s_IDG:.3e} GeV")
print(f"Gap: {np.log10(M_s_ours / M_s_IDG):.1f} orders of magnitude")
print(f"=> Spectral action nonlocality scale is {M_s_ours/M_s_IDG:.1e}x too high")

# ============================================================
# Section 10: The UNEXPANDED-SA-45 Connection
# ============================================================

print("\n" + "=" * 78)
print("CONNECTION TO UNEXPANDED-SA-45 (Taylor Exactness)")
print("=" * 78)

# UNEXPANDED-SA-45 proved: for finite spectrum, S(Lambda) is EXACTLY
# its Taylor series in 1/Lambda^2 for Lambda > lambda_max.
#
# This seems to contradict the entire-function nature of F(p^2).
# Resolution: there are TWO different expansions:
#
# (A) S(Lambda) at FIXED p=0 as a function of Lambda:
#     S(Lambda) = sum_n d_n f(lambda_n^2/Lambda^2)
#     For Gaussian: S = sum_n d_n exp(-lambda_n^2/Lambda^2)
#     This IS polynomial in u = 1/Lambda^2 because it's a finite sum
#     of exponentials in u. For u < 1/lambda_max^2, the Taylor series
#     converges and equals the function exactly.
#     => POLYNOMIAL in 1/Lambda^2 (UNEXPANDED-SA-45)
#
# (B) F(p^2) at FIXED Lambda as a function of p^2:
#     F(p^2) = sum_n d_n f''((p^2+lambda_n^2)/Lambda^2)
#     For Gaussian: F = exp(-p^2/Lambda^2) * K
#     This is ENTIRE in p^2 (not polynomial).
#
# There is no contradiction: different functions of different variables.
# S(Lambda) is polynomial in 1/Lambda^2.
# F(p^2) is entire in p^2 for smooth f.
#
# But physically: the CC is S(Lambda) at p=0, not F(p^2).
# The CC problem lives in expansion (A), not (B).
# The nonlocal form factor F(p^2) controls the GRAVITON PROPAGATOR,
# not the vacuum energy.

print("""
RESOLUTION OF APPARENT CONTRADICTION:
  UNEXPANDED-SA-45: S(Lambda) = polynomial in 1/Lambda^2 at fixed p=0
  THIS COMPUTATION: F(p^2) = entire in p^2 at fixed Lambda

  These are DIFFERENT functions of DIFFERENT variables.
  S(Lambda) controls the CC (vacuum energy at zero momentum).
  F(p^2) controls the graviton propagator (dynamics at finite momentum).

  The CC problem is in S(Lambda), which IS polynomial.
  The graviton propagator is controlled by F(p^2), which CAN BE entire.
  But the entire-function structure of F does not help with the CC
  because M_s = Lambda (too high).
""")

# ============================================================
# Section 11: Numerical Verification of Key Claims
# ============================================================

print("=" * 78)
print("NUMERICAL VERIFICATION")
print("=" * 78)

# Verify 1: F_Gaussian is exactly factorized
# Only compare where both are above machine precision
valid = (np.abs(F_gauss) > 1e-250) & (np.abs(F_gauss_analytic) > 1e-250)
err_factor = np.max(np.abs(F_gauss[valid] / F_gauss_analytic[valid] - 1.0))
print(f"\n1. Gaussian factorization: F = K * exp(-p^2/L^2)")
print(f"   max|direct/analytic - 1| = {err_factor:.2e}  [machine epsilon: ~2.2e-16]")

# Verify 2: F(p^2) for erfc is also entire (slower decay than Gaussian)
F_erfc = results['Erfc']['F_p']
# erfc(sqrt(x))'' ~ exp(-x) / x^{3/2} for large x
# So F_erfc should decay like exp(-p^2/Lambda^2) / (p^2/Lambda^2)^{3/2}
# Still entire, but with polynomial prefactor
alpha_erfc = results['Erfc'].get('alpha_exp', 0)
n_erfc = results['Erfc'].get('n_pow', 0)
print(f"\n2. Erfc form factor: alpha_exp = {alpha_erfc:.4f}, n_pow = {n_erfc:.4f}")
print(f"   Classification: {classification.get('Erfc', 'N/A')}")

# Verify 3: Butterworth is NOT entire (rational function has poles)
alpha_bw = results['Butterworth-4'].get('alpha_exp', 0)
n_bw = results['Butterworth-4'].get('n_pow', 0)
print(f"\n3. Butterworth-4 form factor: alpha_exp = {alpha_bw:.6f}, n_pow = {n_bw:.4f}")
print(f"   Classification: {classification.get('Butterworth-4', 'N/A')}")

# Verify 4: Polynomial F at each Lambda (Taylor exactness)
# At fixed Lambda, expand F(p^2) = sum_{k=0}^N c_k (p^2)^k
# For finite spectrum with N distinct eigenvalues, F is a finite
# sum of translates of f'', which for smooth f is NOT polynomial
# in p^2 (it's entire). For sharp f, it's distributional.
print(f"\n4. Taylor expansion test (Gaussian, p^2/Lambda^2 < 1):")
p2_small = np.linspace(0, 0.5*Lambda_sq, 100)
F_exact = K_at_1 * np.exp(-p2_small / Lambda_sq)
# Taylor: F(p^2) = K * (1 - p^2/L^2 + (p^2/L^2)^2/2 - ...)
u = p2_small / Lambda_sq
F_taylor_2 = K_at_1 * (1 - u + u**2/2)
F_taylor_4 = K_at_1 * (1 - u + u**2/2 - u**3/6 + u**4/24)
err_2 = np.max(np.abs(F_exact - F_taylor_2) / np.abs(F_exact))
err_4 = np.max(np.abs(F_exact - F_taylor_4) / np.abs(F_exact))
print(f"   Order-2 Taylor max error: {err_2:.4e}")
print(f"   Order-4 Taylor max error: {err_4:.4e}")
print(f"   => Taylor series CONVERGES but is INFINITE ORDER (not polynomial)")

# ============================================================
# Section 12: Summary and Gate Verdict
# ============================================================

print("\n" + "=" * 78)
print("GATE VERDICT: NONLOCAL-CC-SPECTRAL-63")
print("=" * 78)

# Count entire-function cutoffs
n_entire = sum(1 for c in classification.values() if c == 'ENTIRE_FUNCTION')
n_total = len(classification)
n_power = sum(1 for c in classification.values() if c == 'POWER_LAW')
n_compact = sum(1 for c in classification.values() if c == 'COMPACT_SUPPORT')

print(f"\nClassification summary:")
for name, cls in classification.items():
    print(f"  {name:20s}: {cls}")

print(f"\nEntire-function cutoffs: {n_entire}/{n_total}")
print(f"Power-law cutoffs:      {n_power}/{n_total}")
print(f"Compact support:        {n_compact}/{n_total}")

# VERDICT:
# The form factor F(p^2) IS entire-function for entire cutoffs (Gaussian, erfc, poly-Gauss).
# But this is TRIVIALLY inherited from f — it tells us nothing about the geometry.
# The spectral triple's contribution is the COEFFICIENTS (through the spectrum),
# not the analyticity (which comes from f).
#
# Moreover, the nonlocality scale M_s = Lambda ~ M_KK, far too high for CC suppression.
# And the CC itself is S(Lambda) at p=0, which is polynomial (UNEXPANDED-SA-45).
#
# So: F(Box) CAN be entire, but this does NOT evade Weinberg's no-go for the CC.
# The no-go is evaded for the GRAVITON PROPAGATOR (dynamical gravity),
# but NOT for the VACUUM ENERGY (CC).

gate_verdict = "INFO"
gate_detail = (
    f"F(p^2) entire for entire cutoffs (alpha={results['Gaussian'].get('alpha_exp',0):.4f}), "
    f"but M_s=Lambda~M_KK ({Lambda_phys:.1e} GeV), "
    f"not M_s~Lambda_CC ({M_s_IDG:.1e} GeV). "
    f"CC is S(Lambda) at p=0 = polynomial (UNEXPANDED-SA-45). "
    f"Weinberg no-go NOT evaded for CC. "
    f"Graviton propagator IS nonlocal for smooth f."
)

print(f"\nVERDICT: {gate_verdict}")
print(f"DETAIL: {gate_detail}")

print("""
STRUCTURAL ASSESSMENT:
  The gate question — is F(Box) entire-function? — has a CONDITIONAL answer:
  YES, if and only if the cutoff function f is entire.
  The spectral triple does not determine the analyticity class of F.

  This is NOT a property of the geometry (A, H, D).
  It is a property of the CUTOFF FUNCTION f.

  The distinction matters:
  - Spectral triple data (eigenvalues, degeneracies) = GEOMETRIC
  - Cutoff function f = ADDITIONAL PHYSICAL INPUT
  - Analyticity of F(p^2) = INHERITED FROM f, NOT FROM GEOMETRY

  For the CC specifically: UNEXPANDED-SA-45 proves S(Lambda) is polynomial
  for finite spectra. This IS a geometric statement. The CC problem
  requires solving S(Lambda), not F(p^2).

  The form factor F(p^2) controls the graviton propagator at finite
  momentum, which IS nonlocal for smooth f. This could be relevant
  for gravitational wave propagation or black hole physics, but
  NOT for the cosmological constant.

  CLASSIFICATION: NON-PHONONIC (form factor structure is cutoff-dependent,
  not a property of the internal geometry SU(3) or its phononic excitations).
""")

# ============================================================
# Section 13: Save Data
# ============================================================

print("=" * 78)
print("SAVING DATA")
print("=" * 78)

save_dict = {
    # Input
    'N_modes': N_modes,
    'lambda_sq': lambda_sq,
    'dim2': dim2,
    'Lambda': Lambda,
    'Lambda_sq': Lambda_sq,
    'Lambda_phys_GeV': Lambda_phys,
    'tau_fold': tau_fold,

    # Momentum grid
    'p_sq': p_sq,
    'p_sq_over_Lam2': p_sq_over_Lam2,

    # Form factors
    'F_gaussian': results['Gaussian']['F_p'],
    'F_erfc': results['Erfc']['F_p'],
    'F_sharp': results['Sharp (reg.)']['F_p'],
    'F_poly_gauss': results['Poly-Gauss']['F_p'],
    'F_butterworth': results['Butterworth-4']['F_p'],

    # Gaussian analytics
    'K_at_1': K_at_1,
    'factorization_error': err_factor,

    # Classification
    'alpha_gaussian': results['Gaussian'].get('alpha_exp', 0),
    'alpha_erfc': results['Erfc'].get('alpha_exp', 0),
    'alpha_butterworth': results['Butterworth-4'].get('alpha_exp', 0),
    'n_pow_gaussian': results['Gaussian'].get('n_pow', 0),
    'n_pow_erfc': results['Erfc'].get('n_pow', 0),
    'n_pow_butterworth': results['Butterworth-4'].get('n_pow', 0),

    # Scales
    'M_s_ours_GeV': M_s_ours,
    'M_s_IDG_GeV': M_s_IDG,
    'M_s_gap_orders': np.log10(M_s_ours / M_s_IDG),

    # High-res
    'Lambda_hr': Lambda_hr,
    'K_hr': K_hr,

    # Gate
    'gate_name': 'NONLOCAL-CC-SPECTRAL-63',
    'gate_verdict': gate_verdict,
    'gate_detail': gate_detail,
}

np.savez('s63_nonlocal_cc_spectral.npz', **save_dict)
print("Saved: s63_nonlocal_cc_spectral.npz")

# ============================================================
# Section 14: Plot
# ============================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: Form factors |F(p^2)| vs p^2/Lambda^2
ax = axes[0, 0]
for name, res in results.items():
    F_norm = np.abs(res['F_p']) / np.abs(res['F_0']) if res['F_0'] != 0 else np.abs(res['F_p'])
    ax.semilogy(p_sq_over_Lam2, F_norm, label=name, linewidth=1.5)
ax.set_xlabel(r'$p^2 / \Lambda^2$')
ax.set_ylabel(r'$|F(p^2)| / |F(0)|$')
ax.set_title('Form Factor F(p²) — All Cutoffs')
ax.legend(fontsize=8)
ax.set_xlim(0, 20)
ax.set_ylim(1e-10, 10)
ax.axhline(1, color='gray', ls=':', alpha=0.5)

# Panel 2: log|F| vs p^2/Lambda^2 (exponential decay test)
ax = axes[0, 1]
for name, res in results.items():
    F_abs = np.abs(res['F_p'])
    F_abs = np.where(F_abs > 0, F_abs, 1e-300)
    ax.plot(p_sq_over_Lam2, np.log10(F_abs), label=name, linewidth=1.5)
ax.set_xlabel(r'$p^2 / \Lambda^2$')
ax.set_ylabel(r'$\log_{10} |F(p^2)|$')
ax.set_title('Logarithmic Decay — Entire vs Polynomial')
ax.legend(fontsize=8)
ax.set_xlim(0, 50)

# Panel 3: Gaussian factorization check
ax = axes[1, 0]
F_direct = results['Gaussian']['F_p']
F_factor = K_at_1 * np.exp(-p_sq / Lambda_sq)
valid_plot = (np.abs(F_factor) > 1e-250) & (np.abs(F_direct) > 1e-250)
ratio_plot = np.ones_like(F_direct)
ratio_plot[valid_plot] = F_direct[valid_plot] / F_factor[valid_plot]
ax.plot(p_sq_over_Lam2[valid_plot], ratio_plot[valid_plot], 'b-', linewidth=1.5)
ax.axhline(1.0, color='r', ls='--', alpha=0.7)
ax.set_xlabel(r'$p^2 / \Lambda^2$')
ax.set_ylabel(r'$F_{\rm direct} / (K \cdot e^{-p^2/\Lambda^2})$')
ax.set_title(f'Gaussian Factorization (max err = {err_factor:.1e})')
ax.set_xlim(0, 100)
ax.set_ylim(0.999, 1.001)

# Panel 4: Truncation dependence
ax = axes[1, 1]
Lambda_vals = [Lambda, Lambda_hr]
labels = [f'L≤6 (Λ={Lambda:.2f})', f'L≤7 (Λ={Lambda_hr:.2f})']
for L_val, lbl in zip(Lambda_vals, labels):
    F_plot = np.exp(-p_sq / L_val**2)
    ax.semilogy(p_sq_over_Lam2, F_plot, label=lbl, linewidth=1.5)
# Show continuum limit
ax.axhline(1.0, color='gray', ls=':', label=r'Continuum ($\Lambda \to \infty$)')
ax.set_xlabel(r'$p^2 / \Lambda_6^2$')
ax.set_ylabel(r'$e^{-p^2/\Lambda^2}$')
ax.set_title('Truncation Dependence (Nonlocality Dissolves)')
ax.legend(fontsize=8)
ax.set_xlim(0, 20)
ax.set_ylim(1e-10, 10)

plt.suptitle('NONLOCAL-CC-SPECTRAL-63: Form Factor Analysis\n'
             r'$F(p^2) = \sum_n d_n f^{\prime\prime}((p^2 + \lambda_n^2)/\Lambda^2)$',
             fontsize=12, y=1.02)
plt.tight_layout()
plt.savefig('s63_nonlocal_cc_spectral.png', dpi=150, bbox_inches='tight')
print("Saved: s63_nonlocal_cc_spectral.png")

print("\n" + "=" * 78)
print("COMPUTATION COMPLETE")
print("=" * 78)
