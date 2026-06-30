#!/usr/bin/env python3
"""
s73b_m1_convergence.py -- M1-CC-73B
=====================================

Gate: M1-CC-73B
  PASS:           M_1 converges at Weyl rate (alpha < 0 with clear extrapolation)
                  AND the CC prediction from M_1 matches observed Lambda within
                  0.1 OOM via non-additive G-renormalization.
  INFO:           M_1 converges but the CC prediction shifts > 0.1 OOM.
  DIVERGENT-SCALE: M_1 diverges at Weyl rate but scales predictably
                   (absorbable into Lambda calibration).
  FAIL:           M_1 diverges OR the CC prediction shifts > 1 OOM without
                  absorbable scaling.

Physics:
--------
The f*-scheme spectral functional f* = 0.912*sqrt(x) + 0.088*exp(-x)
(SPECTRAL-FUNCTIONAL-FIT-72, PASS) is 91% sqrt-dominated. In the standard
heat-kernel expansion

    S ~ f_0 Lambda^4 a_0 + f_2 Lambda^2 a_2 + f_4 a_4 + ...

the moments of the functional are

    f_k = (1/(k-1)!) * integral_0^infty x^(k-1) f(x) dx  [k>0]
    f_0 = integral_0^infty f(x) dx

For f*, f_0 = alpha * integral sqrt(x) dx = infinity. The sqrt component has
NO SDW hierarchy. The zeroth moment of the spectral action is therefore
replaced by the finite absolute first moment

    M_1 = sum_n d_n^2 * |lambda_n|                                       (1)

on the d^2 weighting convention of the spectral action (Chamseddine-Connes),
or equivalently the d-weighted variant

    M_1^{(d)} = sum_n d_n * |lambda_n|                                   (2)

on the zeta-sum convention used for the canonical a_k in this project.
Both are FINITE at any finite L_max. The question is whether they CONVERGE
as L_max -> infinity at a Weyl-predictable rate.

Weyl asymptotics on a compact manifold of dimension d:
    sum |lambda_n|^p ~ L^{d + p}         (for p >= 0, divergent with L)
    sum |lambda_n|^{-s} ~ L^{d - s}      (converges for s > d)

For d=8 (SU(3) + Clifford-8 spinor):
    a_0 = mode count ~ L^8 ?            [but S73B W3-F measured L^? ]
    M_1 = sum |lambda| ~ L^{8+1} = L^9  ? (expected Weyl)
    a_2 = sum |lambda|^{-2} ~ L^{8-2}   (converges for s=2)

But this computation is intrinsically UV-finite because the SU(3) manifold
is compact and D_K is elliptic on it — eigenvalues grow but their NUMBER
also grows. The Peter-Weyl decomposition means that at L_max, one includes
sectors (p,q) with p+q <= L_max. The number of sectors grows quadratically
in L_max, but each sector has dim(p,q) ~ (p+q)^2 weighting.

For M_1 with d^2 weighting:
    M_1(L_max) ~ sum_{p+q<=L_max} dim(p,q)^2 * (16*dim(p,q)) * <|lambda|>
              ~ sum_{p+q<=L_max} dim(p,q)^3 * lambda_avg

With dim(p,q) ~ L^2 and the sum over sectors ~ L^2:
    M_1 ~ L^{2+6} = L^8    (approximate)

For d weighting:
    M_1^{(d)} ~ sum_{p+q<=L_max} dim(p,q) * (16*dim(p,q)) * <|lambda|>
             ~ sum_{p+q<=L_max} dim(p,q)^2 * lambda_avg ~ L^{2+4} = L^6

BOTH are expected to DIVERGE. The question is whether the divergence rate
is predictable (Weyl-like power law) and whether it is compatible with the
Volovik non-additive G-renormalization formula

    rho_vac = chi * H^2 * M_Pl^2                                         (3)

where chi is a dimensionless parameter DERIVED from the spectral structure.
Equation (3) is the KEY finding of S73A BBN-VOLOVIK: the additive tracking
vacuum rho_vac = alpha_track * rho_rad is EXCLUDED by BBN at 130x, so the
sole surviving CC mechanism is the non-additive Volovik-Klinkhamer q-theory
G-renormalization. In this mechanism rho_vac is tied to the dynamical
Hubble scale and does not gravitate as an independent component.

The key insight: in equation (3), rho_vac DOES NOT depend on the raw
M_1, only on the DIMENSIONLESS ratio chi. Any L_max divergence of M_1
can be ABSORBED into chi via the calibration

    chi = f(M_1/Lambda_ref, M_Pl/Lambda_ref)                             (4)

where Lambda_ref is a reference cutoff. If M_1 diverges as L^alpha and
Lambda_ref diverges as L^beta, the ratio M_1/Lambda_ref remains FINITE
when alpha = beta, yielding a FINITE chi and a FINITE CC prediction.

This is EXACTLY the Volovik vacuum-energy cancellation: the UV-divergent
bare vacuum energy is cancelled by the microscopic thermodynamic identity
(Gibbs-Duhem), leaving a DIMENSIONAL RESIDUAL chi * H^2 * M_Pl^2 that
is FINITE and IR-dominated.

Method:
-------
1. Compute D_K eigenvalues at L_max = 3, 4, 5, 6, 7 at tau_fold = 0.19.
2. For each L_max, compute:
     M_1^{(1)}   = sum_n d_pq * |lambda_n|          [d-weighted]
     M_1^{(2)}   = sum_n d_pq^2 * |lambda_n|        [d^2-weighted]
     M_1_avg^(1) = <|lambda|>_d-weighted
     M_1_avg^(2) = <|lambda|>_d^2-weighted
     lambda_max(L_max)
     n_modes(L_max)
3. Fit M_1(L_max) = A * L^alpha to determine the Weyl rate.
4. Compute the normalized quantity
     M_1_norm(L_max) = M_1(L_max) / lambda_max(L_max)^4
   which scales as L^(alpha-4*beta_lambda) where beta_lambda is the
   growth rate of the spectral radius. If this ratio is finite in the
   limit, it can serve as a dimensionless spectral-action invariant.
5. Compute chi in three candidate definitions:
     chi_1 = <|lambda|>^2 / M_KK^2           [dimensionless]
     chi_2 = M_1 / (n_modes * lambda_max)    [dimensionless, normalized]
     chi_3 = M_1 / (a_2 * Lambda_ref^2)      [dimensionless, SDW-consistent]
6. Compute the CC prediction via equation (3) and compare to
   rho_Lambda_obs = 2.7e-47 GeV^4.
7. Cross-check against S66 DILUTION-CC-66 (PASS at 0.01 OOM in f_0 scheme).
   Does the M_1-based prediction in the f* scheme give a DIFFERENT,
   COMPATIBLE, or BETTER CC?

Cross-checks:
-------------
(i)   M_1(L_max=3) matches a value derivable from the S73B W3-A existing
      L_max=3 data (for the d-weighted convention).  # (local)
(ii)  Convergence rate consistent with Weyl asymptotics for d=8.
(iii) f*-scheme sum matches S73A W1-D S(tau) direct sum at the fold when
      Lambda = lambda_max.
(iv)  Non-additive G-renormalization is compatible with S73A W1-C BBN
      constraints (alpha_track < 0.0038 for additive; the framework MUST
      use the non-additive form).

Agent: Volovik Superfluid-Universe Theorist (Session 73b, Wave 5-G)
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
from matplotlib.gridspec import GridSpec

from canonical_constants import (
    tau_fold, PI,
    a0_fold, a2_fold, a4_fold,
    S_fold, dS_fold, d2S_fold,
    M_KK_gravity, M_KK_kerner, M_KK, M_Pl_reduced, M_Pl_unreduced,
    rho_Lambda_obs, H_0_GeV, Omega_Lambda, rho_crit_GeV4,
    H_fold,
)

from dirac_spectrum import (
    su3_generators, compute_structure_constants,
    build_cliff8,
    collect_spectrum,
)

from spectral_action import dim_su3_irrep

# =============================================================================
# CONFIGURATION
# =============================================================================
print("=" * 78)
print("M1-CC-73B: Absolute First Moment Convergence for f*-Scheme CC")
print("=" * 78)

# f* parameters (from SPECTRAL-FUNCTIONAL-FIT-72)
alpha_star = 0.9116771171053042  # (local) weight of sqrt
beta_star = 0.08832288289469575  # (local) weight of exp

# L_max values for convergence sweep
Lmax_values = [3, 4, 5, 6, 7]  # (local)
n_Lmax = len(Lmax_values)  # (local)

# Only fold-tau computation (matches S66 CC context)
tau_target = tau_fold  # (local) 0.19

# Eigenvalue cutoff (exclude near-zero eigenvalues from inverse-power sums)
EVAL_CUTOFF = 0.01  # (local) same as S41/S73B-SDW

# Planck-mass convention for Volovik non-additive formula
M_Pl = M_Pl_reduced  # (local) reduced Planck mass, 2.435e18 GeV
M_Pl_sq_GeV2 = M_Pl**2  # (local)

# Hubble parameter at fold (from canonical_constants)
# H_fold is in M_KK units; H_fold_GeV = H_fold * M_KK
# but for the CC test we care about H_0 TODAY
H_obs_GeV = H_0_GeV  # (local) 1.438e-42 GeV

print(f"\n  f*(x) = {alpha_star:.4f}*sqrt(x) + {beta_star:.4f}*exp(-x)")
print(f"  L_max sweep: {Lmax_values}")
print(f"  tau = {tau_target} (fold)")
print(f"  Eigenvalue cutoff: {EVAL_CUTOFF}")
print(f"  M_KK (gravity route) = {M_KK_gravity:.4e} GeV")
print(f"  M_Pl (reduced)       = {M_Pl:.4e} GeV")
print(f"  H_0                  = {H_obs_GeV:.4e} GeV")
print(f"  rho_Lambda_obs       = {rho_Lambda_obs:.4e} GeV^4")

# Canonical spectral quantities at fold
print(f"\n  Canonical SDW at fold (tau=0.19):")
print(f"    a_0 = {a0_fold:.2f}  (mode count, L_max=7)")
print(f"    a_2 = {a2_fold:.4f}  (zeta_D(1), L_max=7)")
print(f"    a_4 = {a4_fold:.4f}  (zeta_D(2), L_max=7)")

# =============================================================================
# STEP 0: Build algebraic infrastructure
# =============================================================================
print("\n" + "=" * 78)
print("STEP 0: SU(3) Algebraic Infrastructure")
print("=" * 78)

gens = su3_generators()
f_abc = compute_structure_constants(gens)
gammas = build_cliff8()
print("  Done.")

# =============================================================================
# STEP 1: Compute eigenvalue spectrum for each L_max
# =============================================================================
print("\n" + "=" * 78)
print("STEP 1: D_K Eigenvalue Spectrum, L_max = 3, 4, 5, 6, 7")
print("=" * 78)

# spectra[Lmax] = list of (p, q, |evals|, dim(p,q))
spectra = {}

for Lmax in Lmax_values:
    t0 = time.time()  # (local)
    print(f"\n  L_max = {Lmax}...")
    _, eval_data = collect_spectrum(tau_target, gens, f_abc, gammas,
                                    max_pq_sum=Lmax, verbose=False)
    tau_spec = []  # (local)
    n_weighted = 0  # (local)
    n_raw = 0  # (local)
    for p, q, evals in eval_data:
        d_pq = dim_su3_irrep(p, q)  # (local)
        omega = np.abs(evals)  # (local)
        tau_spec.append((p, q, omega, d_pq))
        n_weighted += d_pq**2 * len(omega)
        n_raw += len(omega)
    spectra[Lmax] = tau_spec
    elapsed = time.time() - t0  # (local)
    print(f"    {n_raw} raw eigenvalues, {n_weighted} d^2-weighted, "
          f"{len(eval_data)} sectors, {elapsed:.1f}s")

# =============================================================================
# STEP 2: Compute M_1, M_1_d, and auxiliary spectral sums
# =============================================================================
print("\n" + "=" * 78)
print("STEP 2: Compute M_1, M_1_d, a_0_check, a_2_check at each L_max")
print("=" * 78)

# For each L_max, compute:
#   M_1_d2  = sum d^2 * |lambda|     [spectral-action convention]
#   M_1_d   = sum d * |lambda|       [canonical zeta-sum convention]
#   n_modes_d2 = sum d^2 * n_eigs    [total d^2-weighted mode count]
#   n_modes_d  = sum d * n_eigs_half [total d-weighted positive-mode count]
#   a_0 (d-weighted, positive-only) [should match a0_fold at L_max=7]
#   a_2 (d-weighted, positive-only) [should match a2_fold at L_max=7]
#   lambda_max, lambda_min
#   first_moment_avg = M_1 / n_modes [average |lambda| weighted]

def compute_moments(tau_spec, eval_cutoff=0.01):
    """Compute M_1 moments with both d and d^2 weightings."""
    M1_d2 = 0.0  # (local) sum d^2 |lambda|  (d^2 spectral-action convention)
    M1_d  = 0.0  # (local) sum d  |lambda|   (d zeta-sum convention, positive-only)
    n_d2 = 0      # (local) d^2-weighted mode count (all eigenvalues)
    n_d  = 0      # (local) d-weighted positive-only mode count
    a0_d = 0      # (local) = n_d  (same quantity as a0_fold computed earlier)
    a2_d = 0.0    # (local) sum d |lambda|^{-2} positive-only
    a4_d = 0.0    # (local) sum d |lambda|^{-4} positive-only
    lam_min = np.inf  # (local)
    lam_max = 0.0     # (local)

    for (p, q, omega, d_pq) in tau_spec:
        if len(omega) == 0:
            continue
        pos = omega[omega > eval_cutoff]  # (local)
        if len(pos) == 0:
            continue
        n_pos_total = len(pos)  # (local) includes + and - mirror
        n_pos_half = n_pos_total // 2  # (local) positive-only half
        half_factor = 0.5  # (local) for zeta-sum convention (half the spectrum)

        # d^2 spectral-action convention: sum over ALL eigenvalues in sector
        # weighted by dim(p,q)^2
        M1_d2 += d_pq**2 * np.sum(pos)
        n_d2 += d_pq**2 * n_pos_total

        # d-weighted, positive-only zeta-sum convention (matches a0_fold)
        M1_d += d_pq * half_factor * np.sum(pos)
        n_d  += d_pq * n_pos_half
        a0_d += d_pq * n_pos_half
        a2_d += d_pq * half_factor * np.sum(pos**(-2))
        a4_d += d_pq * half_factor * np.sum(pos**(-4))

        lam_min = min(lam_min, np.min(pos))
        lam_max = max(lam_max, np.max(pos))

    return {
        'M1_d2': M1_d2,
        'M1_d': M1_d,
        'n_d2': n_d2,
        'n_d': n_d,
        'a0_d': a0_d,
        'a2_d': a2_d,
        'a4_d': a4_d,
        'lam_min': lam_min,
        'lam_max': lam_max,
        'avg_d2': M1_d2 / n_d2 if n_d2 > 0 else 0.0,
        'avg_d':  M1_d / n_d if n_d > 0 else 0.0,
    }


moments = {}
print("\n  L_max | n_modes^(d2) | n_modes^(d) |    M_1^(d2)     |    M_1^(d)     "
      "| <|lam|>_d2 |  lam_max  |   a_0_d  |    a_2_d")
print("  " + "-" * 115)

for Lmax in Lmax_values:
    mom = compute_moments(spectra[Lmax], eval_cutoff=EVAL_CUTOFF)  # (local)
    moments[Lmax] = mom
    print(f"  {Lmax:5d} | {mom['n_d2']:11d}  | {mom['n_d']:10d}  "
          f"| {mom['M1_d2']:13.4e}  | {mom['M1_d']:13.4e}  "
          f"| {mom['avg_d2']:9.4f}  | {mom['lam_max']:8.4f}  "
          f"| {mom['a0_d']:7.0f}  | {mom['a2_d']:10.4f}")

# Cross-check: the canonical a_k in canonical_constants.py are the L_max=3 values
# (S42 constants_snapshot was frozen at max_pq_sum=3). S73B SDW-VALIDATION
# confirmed that a_0/a_2 ratio deviates 1.68x between L_max=3 and L_max=7,
# which is the SDW-VALIDATION-73B FAIL finding: canonical values ARE L_max=3.
L3_mom = moments[3]
print(f"\n  Cross-check at L_max=3 vs canonical_constants (canonical = L_max=3 snapshot):")
print(f"    a_0_d(L=3) = {L3_mom['a0_d']:.1f}  vs a0_fold = {a0_fold:.1f}  "
      f"dev = {abs(L3_mom['a0_d'] - a0_fold)/a0_fold:.2e}")
print(f"    a_2_d(L=3) = {L3_mom['a2_d']:.4f}  vs a2_fold = {a2_fold:.4f}  "
      f"dev = {abs(L3_mom['a2_d'] - a2_fold)/a2_fold:.2e}")
print(f"    a_4_d(L=3) = {L3_mom['a4_d']:.4f}  vs a4_fold = {a4_fold:.4f}  "
      f"dev = {abs(L3_mom['a4_d'] - a4_fold)/a4_fold:.2e}")

CROSSCHECK_A0 = abs(L3_mom['a0_d'] - a0_fold) / a0_fold < 1e-3  # (local)
CROSSCHECK_A2 = abs(L3_mom['a2_d'] - a2_fold) / a2_fold < 1e-3  # (local)
CROSSCHECK_A4 = abs(L3_mom['a4_d'] - a4_fold) / a4_fold < 1e-3  # (local)
print(f"    PASS a_0 crosscheck: {CROSSCHECK_A0}")
print(f"    PASS a_2 crosscheck: {CROSSCHECK_A2}")
print(f"    PASS a_4 crosscheck: {CROSSCHECK_A4}")

# Print how canonical constants evolve with L_max (significance for S66)
print(f"\n  NOTE: canonical_constants.a0_fold = {a0_fold} is the L_max=3 value.")
print(f"  At L_max=7: a_0_d = {moments[7]['a0_d']:.0f} (74x larger)")
print(f"  At L_max=7: a_2_d = {moments[7]['a2_d']:.4f} (27x larger)")
print(f"  S66 CC gap OOM used a_0_fold(L=3); Weyl-corrected a_0 at L=7 would shift S66 by log10(74)={np.log10(74):.2f} OOM")

# Cross-check M_1 at L_max=3 against SDW-validation stored M_1
M1_d_L3_stored = 10181.762467286375  # (local) from s73b_sdw_validation.npz zeta_Lmax3[1,4]
M1_d_L3_here = L3_mom['M1_d']  # (local)
print(f"\n  M_1^(d) cross-check at L_max=3:")
print(f"    Stored (SDW validation): {M1_d_L3_stored:.4f}")
print(f"    Computed here:           {M1_d_L3_here:.4f}")
print(f"    Deviation:               {abs(M1_d_L3_here - M1_d_L3_stored)/M1_d_L3_stored:.2e}")
CROSSCHECK_M1 = abs(M1_d_L3_here - M1_d_L3_stored)/M1_d_L3_stored < 1e-3  # (local)
print(f"    PASS M_1 crosscheck:     {CROSSCHECK_M1}")

# =============================================================================
# STEP 3: Fit Weyl scaling M_1(L_max) ~ A * L^alpha
# =============================================================================
print("\n" + "=" * 78)
print("STEP 3: Weyl Scaling Fit for M_1, n_modes, lam_max, a_0, a_2")
print("=" * 78)

L_arr = np.array(Lmax_values, dtype=float)  # (local)
log_L = np.log(L_arr)  # (local)

def fit_power_law(L_arr, y_arr):
    """Fit y = A * L^alpha in log-log; returns (alpha, log_A, y_fit, residuals)."""
    log_y = np.log(np.abs(y_arr))  # (local)
    log_L = np.log(L_arr)  # (local)
    # Least-squares linear fit in log-log
    A_mat = np.column_stack([log_L, np.ones_like(log_L)])  # (local)
    coef, res, rank, sv = np.linalg.lstsq(A_mat, log_y, rcond=None)  # (local)
    alpha = coef[0]  # (local)
    log_A = coef[1]  # (local)
    y_fit = np.exp(log_A + alpha * log_L)  # (local)
    rel_residuals = (y_arr - y_fit) / y_arr  # (local)
    return alpha, log_A, y_fit, rel_residuals

# Quantities to fit
quantities = {
    'M1_d2':   [moments[L]['M1_d2'] for L in Lmax_values],
    'M1_d':    [moments[L]['M1_d']  for L in Lmax_values],
    'n_d2':    [moments[L]['n_d2']  for L in Lmax_values],
    'n_d':     [moments[L]['n_d']   for L in Lmax_values],
    'lam_max': [moments[L]['lam_max'] for L in Lmax_values],
    'avg_d2':  [moments[L]['avg_d2']  for L in Lmax_values],
    'a0_d':    [moments[L]['a0_d']  for L in Lmax_values],
    'a2_d':    [moments[L]['a2_d']  for L in Lmax_values],
    'a4_d':    [moments[L]['a4_d']  for L in Lmax_values],
}

fit_results = {}
print("\n  Quantity  |    alpha    |   log10(A)   |  max |rel res|  |  converges?")
print("  " + "-" * 72)
for name, yvals in quantities.items():
    y_arr = np.array(yvals, dtype=float)  # (local)
    alpha, log_A, y_fit, rel_residuals = fit_power_law(L_arr, y_arr)
    max_res = np.max(np.abs(rel_residuals))  # (local)
    converges = alpha < 0  # (local)
    fit_results[name] = {
        'alpha': alpha,
        'log_A': log_A,
        'A': np.exp(log_A),
        'y_fit': y_fit,
        'y_obs': y_arr,
        'rel_residuals': rel_residuals,
        'max_residual': max_res,
        'converges': converges,
    }
    print(f"  {name:9s}  | {alpha:10.4f}  | {np.log10(np.exp(log_A)):10.4f}   "
          f"| {max_res:13.4e}  | {'YES' if converges else 'NO (diverges)'}")

# The KEY quantity: M_1 in both conventions
alpha_M1_d2 = fit_results['M1_d2']['alpha']
alpha_M1_d  = fit_results['M1_d']['alpha']
alpha_lam_max = fit_results['lam_max']['alpha']
alpha_a0 = fit_results['a0_d']['alpha']
alpha_a2 = fit_results['a2_d']['alpha']
alpha_a4 = fit_results['a4_d']['alpha']

print(f"\n  M_1 scaling summary:")
print(f"    M_1^(d2)  ~ L^{alpha_M1_d2:.3f}   {'CONVERGENT' if alpha_M1_d2<0 else 'DIVERGENT'}")
print(f"    M_1^(d)   ~ L^{alpha_M1_d:.3f}   {'CONVERGENT' if alpha_M1_d<0 else 'DIVERGENT'}")
print(f"    lam_max   ~ L^{alpha_lam_max:.3f}  {'CONVERGENT' if alpha_lam_max<0 else 'DIVERGENT'}")
print(f"    a_0_d     ~ L^{alpha_a0:.3f}  {'CONVERGENT' if alpha_a0<0 else 'DIVERGENT'}")
print(f"    a_2_d     ~ L^{alpha_a2:.3f}   {'CONVERGENT' if alpha_a2<0 else 'DIVERGENT'}")
print(f"    a_4_d     ~ L^{alpha_a4:.3f}   {'CONVERGENT' if alpha_a4<0 else 'DIVERGENT'}")

# Weyl expectation on d=8 compact manifold:
# The spectral counting function N(Lambda) = #{|lambda| < Lambda} scales as
# N(Lambda) ~ Vol_SU3 * Lambda^d / (4 pi)^(d/2) Gamma(d/2+1)
# At fixed Peter-Weyl cutoff L_max, lambda_max ~ L_max (linear)
# and n_modes ~ L_max^d (for d=8 this is L^8).
# Note: d here is NOT 8 literally, because PW uses sector index p+q,
# not lambda directly. Each sector has dim(p,q) ~ ((p+q)/2)^2 and the
# sum over sectors up to L_max is ~ L^4. With 16 * dim(p,q) eigenvalues
# per sector, total n_raw ~ L^6. With dim(p,q) multiplicity in the
# zeta sum (d-weighted): a_0_d ~ L^6. With dim(p,q)^2 weighting (d^2):
# n_d2 ~ L^8. These are the Weyl-like growth rates for PW truncation.
#
# Then M_1 ~ n_modes * <lambda> where <lambda> grows slowly (logarithmically
# or as small power). If lam_max ~ L and n_d2 ~ L^8, then M_1^(d2) ~ L^9
# for the raw sum (d^2 weighted). The fit should give alpha_M1_d2 ~ 9 - epsilon.
# Similarly for d weighting: a_0 ~ L^6, so M_1^(d) ~ L^7.

# =============================================================================
# STEP 4: Cross-check with S73A W1-D direct spectral sum at fold
# =============================================================================
print("\n" + "=" * 78)
print("STEP 4: Cross-check with S73A Direct Spectral Sum")
print("=" * 78)

# Load S73A spectral action profile data
try:
    s73a_data = np.load('s73a_spectral_action_profile.npz', allow_pickle=True)
    S_fold_73a = float(s73a_data['S_fold_recovered'])
    dS_fold_73a = float(s73a_data['dS_fold_recovered'])
    Lambda_73a = float(s73a_data['Lambda'])
    print(f"  S73A S_fold recovered  = {S_fold_73a:.2f}")
    print(f"  S73A dS_fold recovered = {dS_fold_73a:.2f}")
    print(f"  S73A Lambda            = {Lambda_73a:.4f} M_KK")
except Exception as e:
    print(f"  Could not load s73a data: {e}")
    S_fold_73a = float('nan')
    Lambda_73a = float('nan')

# The f*-scheme spectral action at fold is:
#   S_f* = sum d^2 * f*(lambda^2 / Lambda^2)
#        = alpha * sum d^2 * |lambda|/Lambda + beta * sum d^2 * exp(-lambda^2/Lambda^2)
#        = alpha * M_1^(d2) / Lambda + beta * K_d2(t=1/Lambda^2)
#
# So we can compute S_f* directly from M_1 at L_max=7:
Lambda_ref = Lambda_73a if not np.isnan(Lambda_73a) else 12.908  # (local)
S_fstar_M1 = alpha_star * moments[7]['M1_d2'] / Lambda_ref  # (local) sqrt component only
print(f"\n  alpha*M_1^(d2)/Lambda = {alpha_star:.4f} * {moments[7]['M1_d2']:.2e} / {Lambda_ref:.4f}")
print(f"                       = {S_fstar_M1:.4e}")
print(f"  (This is the sqrt component of S_f*; the exp component")
print(f"   adds beta * K(1/Lambda^2) which is much smaller at fold)")

# =============================================================================
# STEP 5: Compute CC prediction via Volovik non-additive G-renormalization
# =============================================================================
print("\n" + "=" * 78)
print("STEP 5: CC Prediction via Volovik Non-Additive G-Renormalization")
print("=" * 78)

# S73A W1-C BBN constraint: additive tracking vacuum EXCLUDED at 130x
# (alpha_crit_2sig = 0.0792, alpha_crit_3sig = 0.1212)
# So framework MUST use non-additive form:
#   rho_vac = chi * H^2 * M_Pl^2
# where chi is dimensionless, derived from spectral structure

# In Volovik's q-theory (Paper 13, 25):
#   chi = dimensionless susceptibility of the q-field
#   rho_vac(t) ~ M_Pl^2 * H^2(t) * chi
# Key: rho_vac depends on the CURRENT H, not the vacuum energy at the fold.
# This naturally gives rho_vac ~ rho_crit today, without CC hierarchy problem.

# Three candidate definitions of chi from M_1:
#
# Definition 1: chi_1 = <|lambda|>^2 / M_KK^2
#   Uses the average eigenvalue scale vs M_KK (naive dimensional)
#
# Definition 2: chi_2 = M_1^(d2) / (n_d2 * lambda_max)
#   Normalized first moment: average eigenvalue relative to max eigenvalue
#   (this is bounded by 1 and should converge)
#
# Definition 3: chi_3 = (M_1^(d) / a_2_d) / Lambda_ref^2
#   SDW-consistent: uses the ratio M_1/a_2 which combines positive and
#   negative-power moments. Dimensional analysis: M_1 has dim [length]^{-1},
#   a_2 has dim [length]^2, so M_1*a_2 has dim [length]^1 (not dimensionless!).
#   Fix: chi_3 = (M_1 * a_2) / n_d^2 gives dimensionless ratio.

# Define chi candidates for each L_max
chi_results = {}
for Lmax in Lmax_values:
    mom = moments[Lmax]  # (local)
    # chi_1: average eigenvalue scale squared (relative to M_KK=1 units)
    chi_1 = mom['avg_d2']**2  # (local)
    # chi_2: M_1 normalized by (n_modes * lambda_max)
    chi_2 = mom['M1_d2'] / (mom['n_d2'] * mom['lam_max']) if mom['n_d2'] > 0 else 0.0  # (local)
    # chi_3: SDW-consistent, M_1*a_2/n^2 (dimensionless)
    chi_3 = (mom['M1_d'] * mom['a2_d']) / mom['n_d']**2 if mom['n_d'] > 0 else 0.0  # (local)
    # chi_4: purely geometric: M_1 / lambda_max (= total spectral length in lam_max units)
    chi_4 = mom['M1_d2'] / (mom['lam_max'] * mom['n_d2']) if mom['n_d2'] > 0 else 0.0  # (local)
    chi_results[Lmax] = {
        'chi_1': chi_1,
        'chi_2': chi_2,
        'chi_3': chi_3,
        'chi_4': chi_4,
    }

print("\n  L_max |    chi_1    |    chi_2    |    chi_3    |    chi_4")
print("  " + "-" * 60)
for Lmax in Lmax_values:
    cr = chi_results[Lmax]
    print(f"  {Lmax:5d} | {cr['chi_1']:10.5f}  | {cr['chi_2']:10.5f}  "
          f"| {cr['chi_3']:10.5f}  | {cr['chi_4']:10.5f}")

# Fit chi convergence
chi_fits = {}
for chi_name in ['chi_1', 'chi_2', 'chi_3', 'chi_4']:
    chi_vals = np.array([chi_results[L][chi_name] for L in Lmax_values])  # (local)
    if np.all(chi_vals > 0):
        alpha_chi, log_A_chi, y_fit_chi, res_chi = fit_power_law(L_arr, chi_vals)
        chi_fits[chi_name] = {
            'alpha': alpha_chi,
            'A': np.exp(log_A_chi),
            'y_fit': y_fit_chi,
            'y_obs': chi_vals,
            'max_residual': np.max(np.abs(res_chi)),
            # Extrapolate to L -> infinity: if alpha < 0, limit exists
            'limit_inf': np.exp(log_A_chi) * 1e30 if alpha_chi < 0 else float('inf'),
            'L7_value': chi_vals[-1],
        }

print("\n  chi scaling fits (chi ~ L^alpha):")
print("  " + "-" * 72)
for name, fit in chi_fits.items():
    convergent = "CONVERGES" if fit['alpha'] < 0 else "DIVERGES"
    print(f"    {name}: alpha = {fit['alpha']:.4f}  L7_val = {fit['L7_value']:.5f}  "
          f"{convergent}")

# =============================================================================
# STEP 6: Compute CC prediction for each chi candidate
# =============================================================================
print("\n" + "=" * 78)
print("STEP 6: CC Prediction rho_vac = chi * H^2 * M_Pl^2")
print("=" * 78)

# Volovik non-additive form (S73A W1-C compliant):
# rho_vac = chi * H^2 * M_Pl^2
# Use H = H_0 for today's CC; M_Pl = reduced Planck mass
H_sq_MPl_sq = H_obs_GeV**2 * M_Pl**2  # (local) GeV^4
print(f"\n  H_0^2 * M_Pl^2 = ({H_obs_GeV:.3e})^2 * ({M_Pl:.3e})^2 = {H_sq_MPl_sq:.4e} GeV^4")
print(f"  For comparison: rho_crit = 3 * H_0^2 * M_Pl^2 = {3*H_sq_MPl_sq:.4e} GeV^4")
print(f"  Observed CC: rho_Lambda_obs = {rho_Lambda_obs:.4e} GeV^4")
print(f"  Omega_Lambda * rho_crit = {Omega_Lambda*3*H_sq_MPl_sq:.4e} GeV^4")

# For rho_vac = chi * H^2 * M_Pl^2 to match rho_Lambda_obs,
# we need chi ~ rho_Lambda_obs / (H_0^2 * M_Pl^2) ~ Omega_Lambda * 3 ~ 2.0
# (Note: using rho_crit = 3 * H^2 * M_Pl^2 in reduced Planck units)
chi_needed = rho_Lambda_obs / H_sq_MPl_sq  # (local) dimensionless chi for perfect match
print(f"\n  chi needed for rho_vac = rho_obs: {chi_needed:.4f}")
print(f"  chi = Omega_Lambda * 3 = {3*Omega_Lambda:.4f} would also work (uses rho_crit)")

# Compute rho_vac prediction for each chi at each L_max
cc_predictions = {}
print("\n  L_max |   chi_2_val   |   rho_vac_chi2   |   log10(gap_chi2)")
print("  " + "-" * 65)
for Lmax in Lmax_values:
    cr = chi_results[Lmax]  # (local)
    cc_predictions[Lmax] = {}
    for chi_name, chi_val in cr.items():
        rho_vac_pred = chi_val * H_sq_MPl_sq  # (local) GeV^4
        gap_log10 = np.log10(rho_vac_pred / rho_Lambda_obs)  # (local) OOM
        cc_predictions[Lmax][chi_name] = {
            'chi': chi_val,
            'rho_vac_GeV4': rho_vac_pred,
            'gap_log10': gap_log10,
        }
    print(f"  {Lmax:5d} | {cr['chi_2']:11.5f}   | {cc_predictions[Lmax]['chi_2']['rho_vac_GeV4']:.4e}  "
          f"| {cc_predictions[Lmax]['chi_2']['gap_log10']:+8.3f}")

# Extrapolate CC prediction to L_max -> infinity
print("\n  CC prediction extrapolation (L -> infinity):")
print("  " + "-" * 60)
for chi_name in ['chi_1', 'chi_2', 'chi_3', 'chi_4']:
    if chi_name not in chi_fits:
        continue
    fit = chi_fits[chi_name]  # (local)
    if fit['alpha'] < 0:
        # Convergent: the limit is the asymptote (as L->infty, L^alpha -> 0)
        # The fit is chi = A*L^alpha + ... but if the power law is clean
        # the limit is 0 (chi_inf = 0).
        # More accurately: if chi = chi_inf + A*L^alpha, we need chi_inf
        # from a 2-parameter fit; here we just use L=7 as best estimate.
        chi_inf_est = fit['L7_value']  # (local) best estimate
        descriptor = "CONVERGENT (using L=7 as best estimate)"
    else:
        # Divergent: chi * H^2 * M_Pl^2 also diverges
        chi_inf_est = float('inf')
        descriptor = "DIVERGENT"
    rho_inf = chi_inf_est * H_sq_MPl_sq  # (local)
    gap_inf = np.log10(rho_inf / rho_Lambda_obs) if rho_inf > 0 and np.isfinite(rho_inf) else float('inf')
    print(f"    {chi_name}: alpha={fit['alpha']:+.3f}, chi_inf ~ {chi_inf_est:.4e}, "
          f"gap_inf = {gap_inf:+.3f} OOM  [{descriptor}]")

# =============================================================================
# STEP 7: Comparison with S66 DILUTION-CC-66 result
# =============================================================================
print("\n" + "=" * 78)
print("STEP 7: Comparison with S66 DILUTION-CC-66 (0.01 OOM PASS)")
print("=" * 78)

# S66 used: rho_SA = (2/pi^2) * a_0 * M_KK^4  [f_0 = 1, pure exp scheme]
# At fold (with a0_fold = 6440 which is L_max=3 value):
rho_SA_a0_S66 = (2.0 / PI**2) * a0_fold * M_KK**4  # GeV^4
print(f"\n  S66 rho_SA (a_0 scheme) = (2/pi^2) * a_0 * M_KK^4")
print(f"                          = (2/pi^2) * {a0_fold:.0f} * ({M_KK:.3e})^4")
print(f"                          = {rho_SA_a0_S66:.4e} GeV^4")
print(f"  S66 gap (before dilution)  = {np.log10(rho_SA_a0_S66/rho_Lambda_obs):+.2f} OOM")
print(f"  S66 gap (after Volovik dilution, PASS at 0.01 OOM)")

# KEY FINDING: S66 used the L_max=3 canonical a_0_fold=6440, not the L_max=7 value.
# At L_max=7, a_0_d = 473760, which is 74x larger.
# If S66 had used the L_max=7 value, the fold CC would be 74x larger, or
# log10(74) ~ 1.87 OOM MORE to dilute. Volovik seesaw would then give
# 1.87 OOM gap instead of 0.01 OOM. Let's compute this.
rho_SA_a0_S66_L7 = (2.0 / PI**2) * moments[7]['a0_d'] * M_KK**4  # GeV^4
print(f"\n  [L_max=7 corrected]: S66 with a_0_d(L=7)={moments[7]['a0_d']:.0f}")
print(f"  rho_SA_L7 = (2/pi^2) * {moments[7]['a0_d']:.0f} * ({M_KK:.3e})^4")
print(f"            = {rho_SA_a0_S66_L7:.4e} GeV^4")
print(f"  Shift from L=3 to L=7: {np.log10(rho_SA_a0_S66_L7/rho_SA_a0_S66):.2f} OOM")
S66_L7_gap_fold = np.log10(rho_SA_a0_S66_L7/rho_Lambda_obs)  # (local)
print(f"  Fold gap at L=7: {S66_L7_gap_fold:+.2f} OOM")
# After Volovik seesaw:
rho_S66_L7_today_pre = rho_SA_a0_S66_L7 * (H_obs_GeV/M_KK)**2  # (local)
print(f"  After Volovik seesaw: rho_today = {rho_S66_L7_today_pre:.4e} GeV^4")
print(f"  Today gap at L=7: {np.log10(rho_S66_L7_today_pre/rho_Lambda_obs):+.2f} OOM")

# S66 found: after Volovik relaxation rho_vac(today) ~ rho_obs (0.01 OOM)
# via dilution factor (H_0/M_KK)^2 applied to the fold vacuum energy.
#
# In the f* scheme, the replacement is:
# rho_SA_fstar = (2/pi^2) * (alpha * M_1^(d2)/Lambda) * M_KK^4  [at fold]
# Note: M_1 replaces a_0 only when multiplied by the sqrt-moment factor.
# In the proper f* heat-kernel scheme, the CC contribution at the fold is
#   rho_vac_fstar(fold) = alpha * M_1 * M_KK^3
# (where M_1 has units [M_KK]^1 in natural units, so rho_vac ~ M_KK^4)

# Compute f*-scheme rho_vac at fold using M_1 at each L_max
print("\n  f*-scheme rho_vac at fold using M_1:")
print("  rho_fstar(fold) = alpha * M_1^(d2) * M_KK^3  [dim-matched]")
print("  " + "-" * 78)
print(f"  L_max |    M_1^(d2)     |   rho_fstar_fold (GeV^4)   | gap (OOM)")
print("  " + "-" * 78)
for Lmax in Lmax_values:
    M1 = moments[Lmax]['M1_d2']  # (local)
    # M_1 is in M_KK units (since eigenvalues are in M_KK units).
    # rho_fstar_fold = alpha * M_1 * M_KK^3 (M_KK^3 for 3 of the 4 dim factors;
    # M_1 provides the 4th)
    rho_fstar_fold = alpha_star * M1 * M_KK**3  # (local) GeV^4 (M_1 in M_KK units)
    gap_fold = np.log10(rho_fstar_fold / rho_Lambda_obs)  # (local)
    print(f"  {Lmax:5d} | {M1:14.4e}  | {rho_fstar_fold:.4e}          | {gap_fold:+8.2f}")

# Apply Volovik seesaw: rho_vac(today) = rho_vac(fold) * (H_0/M_KK)^2
seesaw_factor = (H_obs_GeV / M_KK)**2  # (local)
seesaw_OOM = np.log10(seesaw_factor)  # (local)
print(f"\n  Volovik seesaw factor = (H_0/M_KK)^2 = ({H_obs_GeV:.3e}/{M_KK:.3e})^2 = {seesaw_factor:.4e}")
print(f"  Seesaw reduction = {seesaw_OOM:.2f} OOM")

print("\n  f*-scheme rho_vac TODAY after Volovik dilution:")
print("  " + "-" * 78)
print(f"  L_max |   rho_today_GeV4    | gap_today (OOM) | compared to S66")
print("  " + "-" * 78)
cc_fstar_today = {}
for Lmax in Lmax_values:
    M1 = moments[Lmax]['M1_d2']  # (local)
    rho_fstar_fold = alpha_star * M1 * M_KK**3  # (local)
    rho_fstar_today = rho_fstar_fold * seesaw_factor  # (local) GeV^4
    gap_today = np.log10(rho_fstar_today / rho_Lambda_obs)  # (local)
    cc_fstar_today[Lmax] = {
        'rho_fold': rho_fstar_fold,
        'rho_today': rho_fstar_today,
        'gap_today': gap_today,
    }
    # Compare to S66 result (0.01 OOM = ~1%)
    if abs(gap_today) < 0.1:
        comparison = "WITHIN 0.1 OOM of S66 PASS"
    elif abs(gap_today) < 1.0:
        comparison = "within 1 OOM (INFO)"
    else:
        comparison = f"off by {abs(gap_today):.1f} OOM"
    print(f"  {Lmax:5d} | {rho_fstar_today:.4e}      | {gap_today:+8.3f}        | {comparison}")

# =============================================================================
# STEP 8: Final gate verdict
# =============================================================================
print("\n" + "=" * 78)
print("STEP 8: Gate Verdict M1-CC-73B")
print("=" * 78)

# Gate criteria:
# PASS: M_1 converges at Weyl rate (alpha < 0 with clear extrapolation) AND
#       CC prediction from M_1 matches observed Lambda within 0.1 OOM via
#       non-additive G-renormalization
# INFO: M_1 converges but CC prediction shifts > 0.1 OOM
# DIVERGENT-SCALE: M_1 diverges at Weyl rate but scales predictably
# FAIL: M_1 diverges or CC prediction shifts by > 1 OOM without absorbable scaling

# Analyze convergence
M1_d2_converges = alpha_M1_d2 < 0  # (local)
M1_d_converges = alpha_M1_d < 0  # (local)

# Check power-law fit quality for M1_d2
fit_M1_d2 = fit_results['M1_d2']
M1_d2_clean_powerlaw = fit_M1_d2['max_residual'] < 0.1  # (local) <10% residuals

# The key observation: at d=8, M_1 DIVERGES (expected Weyl rate).
# But the normalized quantities chi_2 and chi_4 are BOUNDED (bounded by 1
# because they're <|lam|>/lam_max ratios).

chi_2_converges = chi_fits['chi_2']['alpha'] < 0 if 'chi_2' in chi_fits else False  # (local)
chi_4_converges = chi_fits['chi_4']['alpha'] < 0 if 'chi_4' in chi_fits else False  # (local)

# Check the CC prediction: does f*-scheme rho_vac at L=7 (after Volovik seesaw)
# match rho_obs within 0.1 OOM?
L7_gap = cc_fstar_today[7]['gap_today']  # (local)
L7_gap_abs = abs(L7_gap)  # (local)

# Separately: does chi_2-based CC match?
chi2_L7 = chi_results[7]['chi_2']  # (local)
rho_chi2_L7 = chi2_L7 * H_sq_MPl_sq  # (local)
chi2_gap_L7 = np.log10(rho_chi2_L7 / rho_Lambda_obs)  # (local)

print(f"\n  M_1^(d2) converges? {M1_d2_converges}  (alpha = {alpha_M1_d2:+.3f})")
print(f"  M_1^(d)  converges? {M1_d_converges}   (alpha = {alpha_M1_d:+.3f})")
print(f"  chi_2 converges?   {chi_2_converges}  (alpha = {chi_fits['chi_2']['alpha']:+.3f})")
print(f"  chi_4 converges?   {chi_4_converges}  (alpha = {chi_fits['chi_4']['alpha']:+.3f})")
print(f"\n  Power-law fit cleanliness for M_1^(d2):")
print(f"    max |rel residual| = {fit_M1_d2['max_residual']:.3e}")
print(f"    clean Weyl scaling = {M1_d2_clean_powerlaw}")
print(f"\n  f*-scheme rho_vac TODAY (L_max=7):")
print(f"    rho_today     = {cc_fstar_today[7]['rho_today']:.4e} GeV^4")
print(f"    gap           = {L7_gap:+.3f} OOM")
print(f"\n  chi_2-based CC prediction (L_max=7):")
print(f"    chi_2 value   = {chi2_L7:.5f}")
print(f"    rho_vac pred  = {rho_chi2_L7:.4e} GeV^4")
print(f"    gap           = {chi2_gap_L7:+.3f} OOM")

# Determine verdict
verdict = None  # (local)
verdict_detail = ""  # (local)

if M1_d2_converges and L7_gap_abs < 0.1:
    verdict = "PASS"
    verdict_detail = f"M_1 converges (alpha={alpha_M1_d2:+.3f}) and rho_vac matches obs within 0.1 OOM"
elif M1_d2_converges and L7_gap_abs < 1.0:
    verdict = "INFO"
    verdict_detail = f"M_1 converges but CC shifts {L7_gap:+.2f} OOM"
elif (not M1_d2_converges) and M1_d2_clean_powerlaw:
    # M_1 diverges but at predictable Weyl rate
    # Check if the DIVERGENCE can be absorbed into Lambda calibration.
    # The f*-scheme Lambda_ref also diverges as lam_max ~ L
    # So M_1/Lambda_ref ~ L^(alpha_M1_d2 - 1).
    # If this is MORE CONVERGENT than alpha_M1_d2 alone, absorption works.
    abs_rate = alpha_M1_d2 - alpha_lam_max  # (local) reduced rate after Lambda normalization
    print(f"\n  M_1/Lambda_ref scaling: alpha = {abs_rate:+.3f}")
    # If chi_2 converges (bounded ratio), the absorption works
    if chi_2_converges or abs_rate < 0:
        verdict = "DIVERGENT-SCALE"
        verdict_detail = (f"M_1 diverges (alpha={alpha_M1_d2:+.3f}) "
                         f"but absorbs into Lambda calibration "
                         f"(chi_2 alpha={chi_fits['chi_2']['alpha']:+.3f})")
    else:
        verdict = "FAIL"
        verdict_detail = f"M_1 diverges at alpha={alpha_M1_d2:+.3f}, no absorbable scaling"
elif (not M1_d2_converges):
    verdict = "FAIL"
    verdict_detail = f"M_1 diverges at alpha={alpha_M1_d2:+.3f}, non-clean scaling"
else:
    verdict = "INFO"
    verdict_detail = "Intermediate case, requires further analysis"

print(f"\n  {'='*60}")
print(f"  GATE VERDICT: {verdict}")
print(f"  Detail: {verdict_detail}")
print(f"  {'='*60}")

# =============================================================================
# STEP 9: Plot
# =============================================================================
print("\n" + "=" * 78)
print("STEP 9: Plot M_1 convergence and CC predictions")
print("=" * 78)

fig = plt.figure(figsize=(14, 10))
gs = GridSpec(3, 2, figure=fig, hspace=0.38, wspace=0.28)

# Panel A: M_1 vs L_max in log-log
ax_a = fig.add_subplot(gs[0, 0])
L_fine = np.linspace(2.5, 8.0, 100)  # (local)

# M_1^(d2) fit
M1_d2_fit = fit_results['M1_d2']
ax_a.loglog(L_arr, M1_d2_fit['y_obs'], 'o', markersize=10, color='#CC3333', label='M_1^(d^2) data')
ax_a.loglog(L_fine, M1_d2_fit['A'] * L_fine**M1_d2_fit['alpha'], '--', color='#CC3333',
           label=f"fit: A*L^{M1_d2_fit['alpha']:+.2f}")

# M_1^(d) fit
M1_d_fit = fit_results['M1_d']
ax_a.loglog(L_arr, M1_d_fit['y_obs'], 's', markersize=10, color='#3333CC', label='M_1^(d) data')
ax_a.loglog(L_fine, M1_d_fit['A'] * L_fine**M1_d_fit['alpha'], '--', color='#3333CC',
           label=f"fit: A*L^{M1_d_fit['alpha']:+.2f}")

# n_modes fit (for reference)
n_d2_fit = fit_results['n_d2']
ax_a.loglog(L_arr, n_d2_fit['y_obs'], '^', markersize=8, color='#999999', alpha=0.6,
           label='n_modes^(d^2) (reference)')

ax_a.set_xlabel('L_max')
ax_a.set_ylabel('M_1, n_modes')
ax_a.set_title('(A) M_1 Weyl Scaling on d=8 Manifold')
ax_a.legend(fontsize=8, loc='upper left')
ax_a.grid(True, which='both', alpha=0.3)

# Panel B: chi candidates vs L_max
ax_b = fig.add_subplot(gs[0, 1])
colors_chi = {'chi_1': '#CC3333', 'chi_2': '#3333CC', 'chi_3': '#33CC33', 'chi_4': '#CC33CC'}
for chi_name, color in colors_chi.items():
    if chi_name in chi_fits:
        chi_vals = np.array([chi_results[L][chi_name] for L in Lmax_values])
        ax_b.plot(L_arr, chi_vals, 'o-', color=color, markersize=8,
                 label=f"{chi_name}: alpha={chi_fits[chi_name]['alpha']:+.2f}")
ax_b.axhline(chi_needed, color='k', linestyle=':', label=f'chi needed = {chi_needed:.3f}')
ax_b.axhline(3.0*Omega_Lambda, color='gray', linestyle=':', alpha=0.5,
            label=f'3*Omega_L = {3*Omega_Lambda:.3f}')
ax_b.set_yscale('log')
ax_b.set_xlabel('L_max')
ax_b.set_ylabel('chi (dimensionless)')
ax_b.set_title('(B) chi Candidates and CC Target')
ax_b.legend(fontsize=8, loc='best')
ax_b.grid(True, which='both', alpha=0.3)

# Panel C: CC prediction (rho_vac) vs L_max
ax_c = fig.add_subplot(gs[1, 0])
rho_today_arr = np.array([cc_fstar_today[L]['rho_today'] for L in Lmax_values])
ax_c.semilogy(L_arr, rho_today_arr, 'o-', color='#CC3333', markersize=10,
             label='rho_fstar(today, f* + Volovik seesaw)')
ax_c.axhline(rho_Lambda_obs, color='k', linestyle='-', linewidth=2,
            label=f'rho_obs = {rho_Lambda_obs:.2e}')
ax_c.axhline(rho_Lambda_obs * 10, color='k', linestyle=':', alpha=0.4,
            label='10x bound')
ax_c.axhline(rho_Lambda_obs / 10, color='k', linestyle=':', alpha=0.4)
ax_c.set_xlabel('L_max')
ax_c.set_ylabel('rho_vac (GeV^4)')
ax_c.set_title('(C) f*-Scheme CC Prediction vs L_max')
ax_c.legend(fontsize=8, loc='best')
ax_c.grid(True, which='both', alpha=0.3)

# Panel D: CC gap vs L_max
ax_d = fig.add_subplot(gs[1, 1])
gap_arr = np.array([cc_fstar_today[L]['gap_today'] for L in Lmax_values])
ax_d.plot(L_arr, gap_arr, 'o-', color='#CC3333', markersize=10, label='gap (L_max)')
ax_d.axhline(0, color='k', linestyle='-', linewidth=2, label='Match obs (0 OOM)')
ax_d.axhline(0.1, color='k', linestyle=':', alpha=0.4, label='+/-0.1 OOM')
ax_d.axhline(-0.1, color='k', linestyle=':', alpha=0.4)
ax_d.axhline(1.0, color='gray', linestyle=':', alpha=0.3, label='+/-1 OOM (INFO)')
ax_d.axhline(-1.0, color='gray', linestyle=':', alpha=0.3)
ax_d.set_xlabel('L_max')
ax_d.set_ylabel('log10(rho_vac / rho_obs)')
ax_d.set_title('(D) CC Gap vs L_max (f* scheme + Volovik seesaw)')
ax_d.legend(fontsize=8, loc='best')
ax_d.grid(True, which='both', alpha=0.3)

# Panel E: Convergence residuals
ax_e = fig.add_subplot(gs[2, 0])
for name, color in zip(['M1_d2', 'M1_d', 'n_d2', 'a0_d', 'a2_d', 'lam_max'],
                       ['#CC3333', '#3333CC', '#999999', '#33CC33', '#CC33CC', '#CC9933']):
    fit = fit_results[name]
    ax_e.semilogy(L_arr, np.abs(fit['rel_residuals']) + 1e-10, 'o-',
                 color=color, label=f'{name} (alpha={fit["alpha"]:+.2f})')
ax_e.set_xlabel('L_max')
ax_e.set_ylabel('|relative residual|')
ax_e.set_title('(E) Power-Law Fit Residuals')
ax_e.legend(fontsize=7, loc='best')
ax_e.grid(True, which='both', alpha=0.3)

# Panel F: Summary text
ax_f = fig.add_subplot(gs[2, 1])
ax_f.axis('off')
summary_text = (
    f"M1-CC-73B SUMMARY\n"
    f"=================\n\n"
    f"M_1^(d2) ~ L^{alpha_M1_d2:+.2f}\n"
    f"M_1^(d)  ~ L^{alpha_M1_d:+.2f}\n"
    f"lam_max  ~ L^{alpha_lam_max:+.2f}\n\n"
    f"chi_2 = M_1/(n*lam_max)\n"
    f"chi_2 ~ L^{chi_fits['chi_2']['alpha']:+.3f}\n"
    f"chi_2 at L=3: {chi_results[3]['chi_2']:.5f}\n"
    f"chi_2 at L=7: {chi_results[7]['chi_2']:.5f}\n"
    f"chi_2 needed: {chi_needed:.5f}\n\n"
    f"f* rho_today(L=7): {cc_fstar_today[7]['rho_today']:.2e}\n"
    f"chi_2 rho_today:   {chi_results[7]['chi_2']*H_sq_MPl_sq:.2e}\n"
    f"rho_Lambda_obs:    {rho_Lambda_obs:.2e}\n\n"
    f"Gap (f*):    {cc_fstar_today[7]['gap_today']:+.2f} OOM\n"
    f"Gap (chi_2): {np.log10(chi_results[7]['chi_2']*H_sq_MPl_sq/rho_Lambda_obs):+.2f} OOM\n\n"
    f"VERDICT: {verdict}\n\n"
    f"Cross-checks (L_max=3 canonical):\n"
    f"  a_0 L3:  {'PASS' if CROSSCHECK_A0 else 'FAIL'}\n"
    f"  a_2 L3:  {'PASS' if CROSSCHECK_A2 else 'FAIL'}\n"
    f"  a_4 L3:  {'PASS' if CROSSCHECK_A4 else 'FAIL'}\n"
    f"  M_1 L3:  {'PASS' if CROSSCHECK_M1 else 'FAIL'}"
)
ax_f.text(0.05, 0.95, summary_text, transform=ax_f.transAxes,
         fontfamily='monospace', fontsize=9, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

plt.suptitle(f'M1-CC-73B: Absolute First Moment Convergence (tau={tau_target}) — '
            f'Verdict: {verdict}',
            fontsize=13)
plt.savefig('s73b_m1_convergence.png', dpi=120, bbox_inches='tight')
plt.close()
print("  Saved plot: s73b_m1_convergence.png")

# =============================================================================
# STEP 10: Save data
# =============================================================================
print("\n" + "=" * 78)
print("STEP 10: Save results to s73b_m1_convergence.npz")
print("=" * 78)

# Flatten data for saving
M1_d2_arr = np.array([moments[L]['M1_d2'] for L in Lmax_values])
M1_d_arr = np.array([moments[L]['M1_d'] for L in Lmax_values])
n_d2_arr = np.array([moments[L]['n_d2'] for L in Lmax_values])
n_d_arr = np.array([moments[L]['n_d'] for L in Lmax_values])
lam_max_arr = np.array([moments[L]['lam_max'] for L in Lmax_values])
lam_min_arr = np.array([moments[L]['lam_min'] for L in Lmax_values])
a0_d_arr = np.array([moments[L]['a0_d'] for L in Lmax_values])
a2_d_arr = np.array([moments[L]['a2_d'] for L in Lmax_values])
a4_d_arr = np.array([moments[L]['a4_d'] for L in Lmax_values])
avg_d2_arr = np.array([moments[L]['avg_d2'] for L in Lmax_values])
avg_d_arr = np.array([moments[L]['avg_d'] for L in Lmax_values])

chi_1_arr = np.array([chi_results[L]['chi_1'] for L in Lmax_values])
chi_2_arr = np.array([chi_results[L]['chi_2'] for L in Lmax_values])
chi_3_arr = np.array([chi_results[L]['chi_3'] for L in Lmax_values])
chi_4_arr = np.array([chi_results[L]['chi_4'] for L in Lmax_values])

rho_fold_fstar = np.array([cc_fstar_today[L]['rho_fold'] for L in Lmax_values])
rho_today_fstar = np.array([cc_fstar_today[L]['rho_today'] for L in Lmax_values])
gap_today_fstar = np.array([cc_fstar_today[L]['gap_today'] for L in Lmax_values])

np.savez('s73b_m1_convergence.npz',
    # Gate metadata
    gate_name='M1-CC-73B',
    gate_verdict=verdict,
    gate_detail=verdict_detail,
    # Configuration
    Lmax_values=np.array(Lmax_values),
    tau_target=tau_target,
    alpha_star=alpha_star,
    beta_star=beta_star,
    EVAL_CUTOFF=EVAL_CUTOFF,  # (local)
    # Raw moments
    M1_d2=M1_d2_arr,
    M1_d=M1_d_arr,
    n_d2=n_d2_arr,
    n_d=n_d_arr,
    lam_max=lam_max_arr,
    lam_min=lam_min_arr,
    a0_d=a0_d_arr,
    a2_d=a2_d_arr,
    a4_d=a4_d_arr,
    avg_d2=avg_d2_arr,
    avg_d=avg_d_arr,
    # Power-law fits
    alpha_M1_d2=alpha_M1_d2,
    alpha_M1_d=alpha_M1_d,
    alpha_n_d2=fit_results['n_d2']['alpha'],
    alpha_n_d=fit_results['n_d']['alpha'],
    alpha_lam_max=alpha_lam_max,
    alpha_a0=alpha_a0,
    alpha_a2=alpha_a2,
    alpha_a4=alpha_a4,
    A_M1_d2=fit_results['M1_d2']['A'],
    A_M1_d=fit_results['M1_d']['A'],
    # Power-law fit quality
    residual_M1_d2_max=fit_results['M1_d2']['max_residual'],
    residual_M1_d_max=fit_results['M1_d']['max_residual'],
    M1_d2_clean_powerlaw=M1_d2_clean_powerlaw,
    # chi definitions
    chi_1=chi_1_arr,
    chi_2=chi_2_arr,
    chi_3=chi_3_arr,
    chi_4=chi_4_arr,
    chi_needed=chi_needed,
    alpha_chi_1=chi_fits['chi_1']['alpha'],
    alpha_chi_2=chi_fits['chi_2']['alpha'],
    alpha_chi_3=chi_fits['chi_3']['alpha'],
    alpha_chi_4=chi_fits['chi_4']['alpha'],
    # CC predictions
    H_sq_MPl_sq=H_sq_MPl_sq,
    rho_Lambda_obs=rho_Lambda_obs,
    seesaw_factor=seesaw_factor,
    rho_fold_fstar=rho_fold_fstar,
    rho_today_fstar=rho_today_fstar,
    gap_today_fstar=gap_today_fstar,
    # Comparison to S66
    rho_SA_a0_S66=rho_SA_a0_S66,
    rho_SA_a0_S66_L7=rho_SA_a0_S66_L7,
    S66_L7_gap_fold=S66_L7_gap_fold,
    S66_scheme='f_0=1, rho_SA=(2/pi^2)*a_0*M_KK^4',
    f_star_scheme='alpha*M_1*M_KK^3 (f*=alpha*sqrt+beta*exp)',
    S66_used_a0_Lmax3=True,  # canonical a0_fold = 6440 is L_max=3 value
    # Cross-checks
    crosscheck_a0=CROSSCHECK_A0,
    crosscheck_a2=CROSSCHECK_A2,
    crosscheck_a4=CROSSCHECK_A4,
    crosscheck_M1=CROSSCHECK_M1,
    M1_d_L3_stored=M1_d_L3_stored,
    # Pointers
    s73a_bbn_constraint='rho_vac MUST use non-additive G-renorm (alpha_track<0.0038)',
    s66_reference='DILUTION-CC-66 PASS at 0.01 OOM via rho_vac(fold)*(H_0/M_KK)^2',
)
print("  Saved data: s73b_m1_convergence.npz")

# =============================================================================
# FINAL REPORT
# =============================================================================
print("\n" + "=" * 78)
print("M1-CC-73B FINAL REPORT")
print("=" * 78)
print(f"\nVerdict: {verdict}")
print(f"Detail:  {verdict_detail}")
print(f"\nBidirectional finding:")
print(f"  (a) M_1 Weyl scaling: alpha_M1_d2 = {alpha_M1_d2:+.3f}")
if alpha_M1_d2 > 0:
    print(f"      M_1 DIVERGES at predictable Weyl rate.")
    print(f"      Power-law fit residuals: {fit_results['M1_d2']['max_residual']:.2e}")
    print(f"      Absorbable? chi_2 ~ L^{chi_fits['chi_2']['alpha']:+.3f} (bounded)")
else:
    print(f"      M_1 CONVERGES with L.")
print(f"\n  (b) f*-scheme CC prediction at L_max=7 (with Volovik seesaw):")
print(f"      rho_today = {cc_fstar_today[7]['rho_today']:.4e} GeV^4")
print(f"      gap       = {cc_fstar_today[7]['gap_today']:+.3f} OOM")
print(f"\n  (c) chi-based CC prediction at L_max=7:")
print(f"      chi_2     = {chi_results[7]['chi_2']:.5f} (L=7 value)")
print(f"      chi_2_needed = {chi_needed:.5f}")
print(f"      ratio     = {chi_results[7]['chi_2']/chi_needed:.4e}")
print(f"\n  (d) Comparison to S66 DILUTION-CC-66:")
print(f"      S66 scheme: f_0=1 -> rho_SA = (2/pi^2)*a_0*M_KK^4 = {rho_SA_a0_S66:.4e}")
print(f"      S66 verdict: PASS at 0.01 OOM after Volovik seesaw")
print(f"      f* scheme: alpha*M_1*M_KK^3 at L=7 = {cc_fstar_today[7]['rho_fold']:.4e}")
improvement = np.log10(rho_SA_a0_S66) - np.log10(cc_fstar_today[7]['rho_fold'])  # (local)
print(f"      Ratio (S66/f*): {improvement:+.3f} OOM")

print("\nAll outputs written.")
print("=" * 78)
