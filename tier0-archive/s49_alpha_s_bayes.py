#!/usr/bin/env python3
"""
ALPHA-S-BAYES-49: Bayesian Uncertainty Quantification for alpha_s = dn_s/d(ln k).

Physics:
  S48 ANISO-OZ-48 found alpha_s = -0.038 (lattice, angular avg) at the pivot scale
  K_pivot = 2*pi/L_eff on the 32-cell tessellation. Planck 2018: alpha_s = 0 +/- 0.008.
  This is a 4.9-sigma tension. But the prediction carries uncertainty from:

  (1) BCS gap uncertainty (Delta_B2 varies 0.041-0.122 across 4 configs -- 3x spread)
  (2) Tessellation geometry (J_C2/J_su2/J_u1 depend on rho_s eigenvalues)
  (3) V-matrix element spread (40% CV within B2 subblock)
  (4) K_pivot choice (geometric mean of finite lattice)
  (5) m* mass uncertainty (propagated from J uncertainties through n_s formula)

  The alpha_s formula from O-Z model:
    n_s(K) = 1 - 2/(1 + m^2/(J_eff * K^2))
    alpha_s = dn_s/d(ln K) = -4 m^2 J_eff K^2 / (J_eff K^2 + m^2)^2

  m* is fixed by requiring <n_s>_angular = 0.965, so m* = m*(J_ij, K_pivot).
  Perturbing J_ij changes m* and therefore alpha_s.

  METHOD (Paper 06, McDonnell et al. 2015):
    - Define prior distributions on the uncertain parameters (J_ij, K_pivot).
    - Sample from these priors via Monte Carlo.
    - For each sample, solve for m*(J_ij, K_pivot) then compute alpha_s.
    - The resulting distribution IS the Bayesian posterior P(alpha_s | model).
    - No GP emulator needed: the forward model is O(1) evaluations (analytic).

  ERROR MODEL for J_ij (3 independent sources):
    Source A: BCS model spread.
      Delta_B2 varies by factor 3x across 4 configs (B2-only, B2+B1, B2+B3, Full).
      This is a MODEL SELECTION uncertainty, not statistical. We assign a uniform
      prior on log(Delta_B2) spanning the 4 configs.
      J propto rho_s * Delta^2 / (Casimir), so delta_J/J ~ 2*delta_Delta/Delta.
      Conservative: sigma_J/J = 50% (from 2x the 35% gap spread, log-normal).

    Source B: Geometric mapping uncertainty.
      8 SU(3) directions -> 6 lattice bonds. Assignment is not unique.
      J_xy could be J_C2 (current) or some weighted average including J_su2.
      J_z could be J_su2 or J_u1. We sample over bond assignments.

    Source C: Pivot scale uncertainty.
      K_pivot = 2*pi/L_eff is the geometric mean. But CMB observations probe
      a RANGE of scales. We assign a log-uniform prior on K_pivot over the
      first Brillouin zone: K_pivot in [K_min, K_max] = [2*pi/N^{1/3}, pi].

Gate: ALPHA-S-BAYES-49
  PASS: 95% CI includes alpha_s = 0
  INFO: tension reduced but > 2 sigma
  FAIL: error band negligible, 4.9 sigma unchanged

Session: S49 W1-L
Author: nazarewicz-nuclear-structure-theorist
"""

import sys
import os
import time
import numpy as np
from scipy.optimize import brentq
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

t0 = time.time()

# --- Import canonical constants ---
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    E_cond, tau_fold, N_cells, M_KK, M_KK_gravity,
    Delta_0_GL, Delta_0_OES,
    PI
)

# --- Load upstream data ---
data_dir = os.path.dirname(os.path.abspath(__file__))
s48_oz = np.load(os.path.join(data_dir, 's48_aniso_oz.npz'), allow_pickle=True)
s48_hfb = np.load(os.path.join(data_dir, 's48_hfb_selfconsist.npz'), allow_pickle=True)
s47_tex = np.load(os.path.join(data_dir, 's47_texture_corr.npz'), allow_pickle=True)
s46_gp = np.load(os.path.join(data_dir, 's46_bayesian_gp.npz'), allow_pickle=True)

# Central values from S48
J_C2_central = float(s48_oz['J_C2'])
J_su2_central = float(s48_oz['J_su2'])
J_u1_central = float(s48_oz['J_u1'])
T_acoustic = float(s48_oz['T_acoustic'])
K_pivot_central = float(s48_oz['K_pivot_lattice'])
L_eff_central = float(s48_oz['L_eff'])
alpha_s_central = float(s48_oz['alpha_s_framework'])
m_star_central = float(s48_oz['m_star_angular'])
J_eff_avg_central = float(s48_oz['J_eff_avg'])

# HFB gap data
Delta_configs_B2 = np.array([
    float(s48_hfb['Delta_B2_only'][0]),          # 0.041: B2-only
    float(s48_hfb['Delta_B2_B1'][0]),             # 0.097: B2+B1
    float(s48_hfb['Delta_B2_B3'][0]),             # 0.080: B2+B3
    float(s48_hfb['Delta_Full_B2_B1_B3'][0]),     # 0.122: Full B2+B1+B3
])

# V-matrix elements
V_bare = s48_hfb['V_bare']
V_phys = s48_hfb['V_phys']

# Bayesian GP posterior on tau from S46
sigma_tau_gp = float(s46_gp['sigma_tau'])

# rho_s eigenvalues from S47
rho_s_eigs = s47_tex['rho_s_eigs']

# Lattice dimensions
nx, ny, nz = 4, 4, 2
N = nx * ny * nz

print("=" * 78)
print("ALPHA-S-BAYES-49: Bayesian Uncertainty Quantification for alpha_s")
print("         Propagating J_ij Coupling Errors via Monte Carlo")
print("=" * 78)

# ===========================================================================
# STEP 1: Characterize uncertainty sources
# ===========================================================================
print("\n--- Step 1: Uncertainty Source Characterization ---")

# Source A: BCS gap uncertainty
Delta_B2_mean = np.mean(Delta_configs_B2)
Delta_B2_std = np.std(Delta_configs_B2)
Delta_B2_logmean = np.exp(np.mean(np.log(Delta_configs_B2)))
Delta_B2_logstd = np.std(np.log(Delta_configs_B2))

print(f"  SOURCE A: BCS model selection uncertainty")
print(f"    Delta_B2 configs: {Delta_configs_B2}")
print(f"    Mean = {Delta_B2_mean:.4f}, Std = {Delta_B2_std:.4f} ({Delta_B2_std/Delta_B2_mean:.1%})")
print(f"    Log-mean = {Delta_B2_logmean:.4f}, Log-std = {Delta_B2_logstd:.4f}")
print(f"    Max/Min = {max(Delta_configs_B2)/min(Delta_configs_B2):.2f}")

# Source B: V-matrix element spread within B2 subblock
V_B2 = V_phys[:4, :4]
V_B2_mean = np.mean(V_B2)
V_B2_std = np.std(V_B2)
V_B2_cv = V_B2_std / V_B2_mean

print(f"\n  SOURCE B: V-matrix element spread (B2 subblock)")
print(f"    V_phys B2 mean = {V_B2_mean:.4f}, std = {V_B2_std:.4f}, CV = {V_B2_cv:.1%}")

# The Josephson coupling J_C2 is proportional to rho_s * V:
# J propto rho_s * <V_pair>. The rho_s eigenvalues within each group are
# degenerate to < 10^{-5}, so J uncertainty comes entirely from V uncertainty.
# Conservative: sigma_J/J = CV(V_B2) = 41% per element,
# but the effective J_eff_avg is an average, so its uncertainty is reduced
# by sqrt(number of contributing elements).
# For J_xy (from C^2 directions): 4 bonds, each from ~4 V-matrix elements
# Effective sigma_J/J = CV / sqrt(4) ~ 20% (internal averaging)
# But model selection (Delta configs) gives additional 35% from Source A.

# Combined: sigma_J/J from quadrature of model selection and V-element spread
sigma_J_model = 2 * Delta_B2_std / Delta_B2_mean  # 2x gap spread -> J spread (J ~ Delta^2)
sigma_J_V = V_B2_cv / 2  # effective coupling uncertainty from V spread (conservative sqrt(4))
sigma_J_total = np.sqrt(sigma_J_model**2 + sigma_J_V**2)

print(f"\n  COMBINED J_ij uncertainty:")
print(f"    From BCS model selection: sigma_J/J = {sigma_J_model:.1%}")
print(f"    From V-matrix spread:     sigma_J/J = {sigma_J_V:.1%}")
print(f"    Total (quadrature):       sigma_J/J = {sigma_J_total:.1%}")

# Source C: Geometric mapping (lattice assignment)
# S48 used: J_xy = J_C2, J_z = J_su2
# Alternative assignments:
# (i)   J_xy = (2*J_C2 + J_su2)/3, J_z = J_su2 (include one su2 in-plane)
# (ii)  J_xy = J_C2, J_z = J_u1 (use u1 as inter-plane)
# (iii) J_xy = J_C2, J_z = (J_su2 + J_u1)/2 (average soft directions)
# This is a discrete model selection uncertainty.
J_assignments = [
    (J_C2_central, J_su2_central, "S48 canonical"),
    ((2*J_C2_central + J_su2_central)/3, J_su2_central, "include su2 in-plane"),
    (J_C2_central, J_u1_central, "u1 as z-coupling"),
    (J_C2_central, (J_su2_central + J_u1_central)/2, "avg soft for z"),
    ((J_C2_central + J_su2_central)/2, J_su2_central, "avg C2+su2 for xy"),
]

print(f"\n  SOURCE C: Geometric mapping assignments:")
for jxy, jz, label in J_assignments:
    j_eff = (2*jxy + jz)/3
    print(f"    {label:30s}: J_xy={jxy:.4f}, J_z={jz:.4f}, J_eff={j_eff:.4f}")

# Source D: K_pivot range
K_min = 2*PI/N**(1.0/3.0)  # smallest lattice K
K_max = PI  # Nyquist
K_pivot_range = [K_min, K_max]
print(f"\n  SOURCE D: K_pivot range")
print(f"    K_min = 2*pi/N^(1/3) = {K_min:.4f}")
print(f"    K_pivot (S48) = {K_pivot_central:.4f}")
print(f"    K_max = pi = {K_max:.4f}")
print(f"    log range = {np.log(K_max/K_min):.2f} decades")

# ===========================================================================
# STEP 2: Forward model: alpha_s(J_xy, J_z, K_pivot)
# ===========================================================================
print("\n--- Step 2: Forward Model ---")

def compute_alpha_s(J_xy, J_z, K_pivot, ns_target=0.965, n_angle=50000):
    """
    Compute alpha_s = dn_s/d(ln K) at K_pivot for the anisotropic O-Z model.

    Steps:
    1. Generate uniform directions on S^2
    2. Compute J_eff(Omega) = J_xy*nx^2 + J_xy*ny^2 + J_z*nz^2
    3. Find m* such that <n_s>_angular = ns_target
    4. Compute alpha_s = -4*m^2*J_eff_avg*K^2 / (J_eff_avg*K^2 + m^2)^2

    Returns: (alpha_s, m_star, J_eff_avg, n_s_check)
    """
    # Fixed random directions (reproducible per-call with deterministic seed)
    rng = np.random.RandomState(42)
    theta = np.arccos(2*rng.random(n_angle) - 1)
    phi = 2*PI*rng.random(n_angle)
    nx_hat = np.sin(theta)*np.cos(phi)
    ny_hat = np.sin(theta)*np.sin(phi)
    nz_hat = np.cos(theta)

    J_eff_angular = J_xy*nx_hat**2 + J_xy*ny_hat**2 + J_z*nz_hat**2
    K2 = K_pivot**2

    def ns_avg_minus_target(m_val):
        ns_a = 1.0 - 2.0 / (1.0 + m_val**2 / (J_eff_angular * K2))
        return np.mean(ns_a) - ns_target

    # Find m*
    try:
        m_star = brentq(ns_avg_minus_target, 1e-8, 1000.0)
    except ValueError:
        return np.nan, np.nan, np.nan, np.nan

    # Compute alpha_s using the isotropic average formula
    # (the angular average of the running is well-approximated by the running
    # evaluated at J_eff_avg, because the running is smooth)
    J_eff_avg = (2*J_xy + J_z)/3.0
    x = J_eff_avg * K2
    alpha_s_val = -4.0 * m_star**2 * x / (x + m_star**2)**2

    # Also compute the full angular average of alpha_s
    # alpha_s(Omega) = -4 m^2 J(Omega) K^2 / (J(Omega) K^2 + m^2)^2
    alpha_s_angular = -4.0 * m_star**2 * J_eff_angular * K2 / (J_eff_angular * K2 + m_star**2)**2
    alpha_s_avg = np.mean(alpha_s_angular)

    ns_check = ns_avg_minus_target(m_star) + ns_target

    return alpha_s_avg, m_star, J_eff_avg, ns_check

# Verify against S48 central value
alpha_s_check, m_star_check, J_eff_check, ns_check = compute_alpha_s(
    J_C2_central, J_su2_central, K_pivot_central)
print(f"  Central value verification:")
print(f"    alpha_s = {alpha_s_check:.6f} (S48: {alpha_s_central:.6f})")
print(f"    m*      = {m_star_check:.6f} (S48: {m_star_central:.6f})")
print(f"    J_eff   = {J_eff_check:.6f} (S48: {J_eff_avg_central:.6f})")
print(f"    n_s     = {ns_check:.8f}")

# The alpha_s from the angular average is slightly different from the
# isotropic-J formula because <f(J)> != f(<J>). This is the Jensen
# inequality at work. Record the discrepancy.
alpha_s_iso = -4.0 * m_star_check**2 * J_eff_check * K_pivot_central**2 / \
              (J_eff_check * K_pivot_central**2 + m_star_check**2)**2
print(f"    alpha_s (iso J_eff) = {alpha_s_iso:.6f}")
print(f"    alpha_s (angular avg) = {alpha_s_check:.6f}")
print(f"    Jensen discrepancy = {abs(alpha_s_check - alpha_s_iso)/abs(alpha_s_check):.1%}")

# ===========================================================================
# STEP 3: Monte Carlo sampling
# ===========================================================================
print("\n--- Step 3: Monte Carlo Sampling (N=10000) ---")

N_MC = 10000
rng_mc = np.random.RandomState(2049)

# Priors:
# P1: J_xy ~ LogNormal(log(J_C2), sigma_J_total)
# P2: J_z ~ LogNormal(log(J_su2), sigma_J_total)
#     with 20% probability of J_z = J_u1 (geometric mapping uncertainty)
# P3: K_pivot ~ LogUniform(K_min_usable, K_max_usable)
#     where K_min_usable and K_max_usable bracket the physical pivot
# P4: T_acoustic stays fixed (cancels in the n_s formula; appears only in P(K), not in n_s)
#
# Note: T_acoustic DOES NOT appear in the n_s formula at all!
# n_s = 1 - 2/(1 + m^2/(J_eff*K^2)) depends only on J_eff and K_pivot
# (since m* is determined by the n_s=0.965 constraint).
# alpha_s depends on m*/sqrt(J_eff*K^2) which is fixed by the same constraint.
# So the ONLY parameters that matter are:
#   (a) The RATIO J_xy/J_z (determines anisotropy and angular average)
#   (b) K_pivot (enters through the lattice dispersion correction)
#   (c) The n_s target (observational, Planck)
#
# CRITICAL INSIGHT: In the CONTINUUM limit, alpha_s depends ONLY on n_s!
# alpha_s = (n_s - 1)^2 / 2 * (something from angular averaging)
# So the uncertainty comes from:
#   - Lattice discretization corrections (K_pivot-dependent)
#   - Anisotropy (J_xy/J_z ratio)
#   - The n_s target (Planck uncertainty: 0.9649 +/- 0.0042)

# FULL ERROR MODEL:
# We sample from 4 priors:
# P1: log(J_xy) ~ N(log(J_C2), sigma_J)  with sigma_J = 0.50 (50% spread)
# P2: log(J_z)  ~ N(log(J_su2), sigma_Jz) with sigma_Jz = 0.80 (larger for soft mode)
#     with 25% probability of geometric reassignment (J_z -> J_u1)
# P3: log(K_pivot) ~ N(log(K_pivot_central), sigma_K) with sigma_K = 0.30
# P4: n_s_target ~ N(0.9649, 0.0042)  (Planck 2018 measurement)

sigma_J_xy = 0.50  # 50% log-normal spread (from BCS + V-matrix combined)
sigma_J_z = 0.80   # larger for soft mode (less constrained)
sigma_K = 0.30      # K_pivot uncertainty from lattice assignment
p_reassign = 0.25   # probability of z-coupling reassignment

# Planck measurement
ns_planck_mean = 0.9649
ns_planck_sigma = 0.0042

print(f"  Prior distributions:")
print(f"    log(J_xy) ~ N(log({J_C2_central:.4f}), {sigma_J_xy})")
print(f"    log(J_z)  ~ N(log({J_su2_central:.4f}), {sigma_J_z})")
print(f"    P(reassign J_z -> J_u1) = {p_reassign}")
print(f"    log(K_pivot) ~ N(log({K_pivot_central:.4f}), {sigma_K})")
print(f"    n_s_target ~ N({ns_planck_mean}, {ns_planck_sigma})")
print(f"    N_MC = {N_MC}")

# Storage
alpha_s_samples = np.zeros(N_MC)
m_star_samples = np.zeros(N_MC)
J_eff_samples = np.zeros(N_MC)
J_xy_samples = np.zeros(N_MC)
J_z_samples = np.zeros(N_MC)
K_pivot_samples = np.zeros(N_MC)
ns_target_samples = np.zeros(N_MC)
valid_mask = np.ones(N_MC, dtype=bool)

for i in range(N_MC):
    # Sample J_xy (log-normal)
    J_xy_i = J_C2_central * np.exp(rng_mc.randn() * sigma_J_xy)

    # Sample J_z with reassignment
    if rng_mc.random() < p_reassign:
        J_z_base = J_u1_central  # reassign to u1
    else:
        J_z_base = J_su2_central
    J_z_i = J_z_base * np.exp(rng_mc.randn() * sigma_J_z)

    # Enforce J_xy > J_z (physical: coset directions are stiffer)
    # If violated, swap or clip
    if J_z_i > J_xy_i:
        J_z_i = J_xy_i * 0.5  # soft mode cannot exceed stiff mode

    # Sample K_pivot (log-normal around central)
    K_pivot_i = K_pivot_central * np.exp(rng_mc.randn() * sigma_K)
    K_pivot_i = np.clip(K_pivot_i, 0.5, PI)  # stay within BZ

    # Sample n_s target (Gaussian from Planck)
    ns_target_i = rng_mc.normal(ns_planck_mean, ns_planck_sigma)
    ns_target_i = np.clip(ns_target_i, 0.90, 0.99)  # physical bounds

    # Store
    J_xy_samples[i] = J_xy_i
    J_z_samples[i] = J_z_i
    K_pivot_samples[i] = K_pivot_i
    ns_target_samples[i] = ns_target_i

    # Compute alpha_s for this sample (use smaller n_angle for speed)
    alpha_s_i, m_star_i, J_eff_i, ns_check_i = compute_alpha_s(
        J_xy_i, J_z_i, K_pivot_i, ns_target=ns_target_i, n_angle=10000)

    if np.isnan(alpha_s_i):
        valid_mask[i] = False
        continue

    alpha_s_samples[i] = alpha_s_i
    m_star_samples[i] = m_star_i
    J_eff_samples[i] = J_eff_i

# Filter valid samples
n_valid = np.sum(valid_mask)
alpha_s_valid = alpha_s_samples[valid_mask]
m_star_valid = m_star_samples[valid_mask]
J_eff_valid = J_eff_samples[valid_mask]
J_xy_valid = J_xy_samples[valid_mask]
J_z_valid = J_z_samples[valid_mask]
K_pivot_valid = K_pivot_samples[valid_mask]
ns_target_valid = ns_target_samples[valid_mask]

print(f"\n  Sampling complete:")
print(f"    Valid samples: {n_valid}/{N_MC} ({100*n_valid/N_MC:.1f}%)")
print(f"    Invalid (brentq failure): {N_MC - n_valid}")

# ===========================================================================
# STEP 4: Posterior analysis
# ===========================================================================
print("\n--- Step 4: Posterior P(alpha_s) Analysis ---")

# Statistics
alpha_s_median = np.median(alpha_s_valid)
alpha_s_mean = np.mean(alpha_s_valid)
alpha_s_std = np.std(alpha_s_valid)

# Credible intervals
alpha_s_sorted = np.sort(alpha_s_valid)
ci_68_lo = np.percentile(alpha_s_valid, 16)
ci_68_hi = np.percentile(alpha_s_valid, 84)
ci_95_lo = np.percentile(alpha_s_valid, 2.5)
ci_95_hi = np.percentile(alpha_s_valid, 97.5)
ci_99_lo = np.percentile(alpha_s_valid, 0.5)
ci_99_hi = np.percentile(alpha_s_valid, 99.5)

print(f"  Posterior alpha_s:")
print(f"    Median  = {alpha_s_median:.6f}")
print(f"    Mean    = {alpha_s_mean:.6f}")
print(f"    Std     = {alpha_s_std:.6f}")
print(f"    68% CI  = [{ci_68_lo:.6f}, {ci_68_hi:.6f}]")
print(f"    95% CI  = [{ci_95_lo:.6f}, {ci_95_hi:.6f}]")
print(f"    99% CI  = [{ci_99_lo:.6f}, {ci_99_hi:.6f}]")

# Does 95% CI include alpha_s = 0?
includes_zero_95 = (ci_95_lo <= 0.0 <= ci_95_hi)
includes_zero_99 = (ci_99_lo <= 0.0 <= ci_99_hi)
print(f"\n  alpha_s = 0 in 95% CI? {includes_zero_95}")
print(f"  alpha_s = 0 in 99% CI? {includes_zero_99}")

# Fraction of samples with alpha_s > 0
frac_positive = np.mean(alpha_s_valid > 0)
print(f"  P(alpha_s > 0) = {frac_positive:.4f}")
print(f"  P(alpha_s < 0) = {1 - frac_positive:.4f}")

# Tension with Planck
# Planck: alpha_s = 0.0 +/- 0.008 (approximately)
# Framework: alpha_s = median +/- std
# Tension = |median - 0| / sqrt(std^2 + 0.008^2)
sigma_planck = 0.008
tension_planck = abs(alpha_s_median) / np.sqrt(alpha_s_std**2 + sigma_planck**2)
print(f"\n  Tension with Planck (alpha_s = 0 +/- {sigma_planck}):")
print(f"    |median| / sqrt(sigma_framework^2 + sigma_Planck^2) = {tension_planck:.2f} sigma")
print(f"    (Original S48 tension: 4.9 sigma with zero uncertainty)")

# More precise Planck value: -0.0045 +/- 0.0067
alpha_s_planck_central = -0.0045
alpha_s_planck_sigma = 0.0067
tension_planck_precise = abs(alpha_s_median - alpha_s_planck_central) / \
    np.sqrt(alpha_s_std**2 + alpha_s_planck_sigma**2)
print(f"\n  Tension with Planck (alpha_s = {alpha_s_planck_central} +/- {alpha_s_planck_sigma}):")
print(f"    = {tension_planck_precise:.2f} sigma")

# ===========================================================================
# STEP 5: Sensitivity analysis (which uncertainty dominates?)
# ===========================================================================
print("\n--- Step 5: Sensitivity Analysis ---")

# Compute partial correlations: what drives alpha_s variation?
from numpy.polynomial.polynomial import polyfit

# Correlation coefficients
corr_Jxy = np.corrcoef(np.log(J_xy_valid), alpha_s_valid)[0,1]
corr_Jz = np.corrcoef(np.log(J_z_valid), alpha_s_valid)[0,1]
corr_Kp = np.corrcoef(np.log(K_pivot_valid), alpha_s_valid)[0,1]
corr_ns = np.corrcoef(ns_target_valid, alpha_s_valid)[0,1]
corr_ratio = np.corrcoef(np.log(J_xy_valid/J_z_valid), alpha_s_valid)[0,1]

print(f"  Pearson correlations with alpha_s:")
print(f"    r(log J_xy, alpha_s)       = {corr_Jxy:+.4f}")
print(f"    r(log J_z, alpha_s)        = {corr_Jz:+.4f}")
print(f"    r(log K_pivot, alpha_s)    = {corr_Kp:+.4f}")
print(f"    r(n_s_target, alpha_s)     = {corr_ns:+.4f}")
print(f"    r(log(J_xy/J_z), alpha_s)  = {corr_ratio:+.4f}")

# Variance decomposition (approximate via conditional variances)
# Fix each parameter at its central value and resample the rest
# to estimate the variance contribution of each parameter.

# Method: compute var(alpha_s | J_xy fixed) etc.
# and compare to total variance. This is the Sobol-like decomposition.

# Actually, for a clearer picture: compute alpha_s with each parameter
# fixed at central and the rest varying. The reduction in variance
# tells us the importance of that parameter.

print(f"\n  Variance contribution analysis:")
print(f"    Total variance: {alpha_s_std**2:.8f}")

# Rather than resampling (expensive), we use the correlation-based estimate:
# Var_explained by X = r^2 * Var(alpha_s)
for label, r_val in [('log J_xy', corr_Jxy), ('log J_z', corr_Jz),
                       ('log K_pivot', corr_Kp), ('n_s_target', corr_ns),
                       ('log(J_xy/J_z)', corr_ratio)]:
    var_frac = r_val**2
    print(f"    {label:20s}: R^2 = {var_frac:.4f} ({100*var_frac:.1f}%)")

# ===========================================================================
# STEP 6: CMB-S4 forecast
# ===========================================================================
print("\n--- Step 6: CMB-S4 Forecast ---")

# CMB-S4 expected sigma(alpha_s) ~ 0.003
sigma_cmbs4 = 0.003

# If the framework median is the true value, what is the detection significance?
significance_cmbs4 = abs(alpha_s_median) / np.sqrt(alpha_s_std**2 + sigma_cmbs4**2)
print(f"  CMB-S4 sigma(alpha_s) ~ {sigma_cmbs4}")
print(f"  Framework median: {alpha_s_median:.4f}")
print(f"  Framework sigma: {alpha_s_std:.4f}")
print(f"  Detection significance if framework correct:")
print(f"    |median| / sqrt(sigma_fw^2 + sigma_S4^2) = {significance_cmbs4:.2f} sigma")
print(f"  (requires alpha_s < 0 at > 3sigma for meaningful test)")

# What precision in alpha_s would confirm/rule out the framework at 3sigma?
sigma_needed_3sigma = abs(alpha_s_median) / 3.0
sigma_needed_5sigma = abs(alpha_s_median) / 5.0
print(f"\n  Required precision for:")
print(f"    3-sigma detection: sigma(alpha_s) < {sigma_needed_3sigma:.4f}")
print(f"    5-sigma detection: sigma(alpha_s) < {sigma_needed_5sigma:.4f}")
print(f"    CMB-S4 expected:   sigma(alpha_s) ~ {sigma_cmbs4}")

# ===========================================================================
# STEP 7: Analytical cross-check
# ===========================================================================
print("\n--- Step 7: Analytical Cross-Check ---")

# In the CONTINUUM isotropic limit:
# n_s = 1 - 2/(1 + (m/sqrt(J)*K)^2) = 1 - 2*J*K^2/(J*K^2 + m^2)
# Defining xi = m^2/(J*K^2), then n_s = 1 - 2/(1+xi) => xi = (1-n_s)/(1+n_s) ... no
# More carefully: n_s - 1 = -2/(1+xi) => 1+xi = -2/(n_s-1) => xi = -(1+n_s)/(n_s-1)
# For n_s = 0.965: xi = -(1.965)/(-0.035) = 56.14
#
# alpha_s = dn_s/d(ln K) = d/d(ln K) [1 - 2/(1 + m^2/(J*K^2))]
# = -2 * d/d(ln K) [1/(1+xi)]  where xi = m^2/(J*K^2)
# = -2 * (-1/(1+xi)^2) * d(xi)/d(ln K)
# d(xi)/d(ln K) = m^2/(J) * d(K^{-2})/d(ln K) = m^2/(J) * (-2*K^{-2}) = -2*xi
# So: alpha_s = -2 * (-1/(1+xi)^2) * (-2*xi) = -4*xi/(1+xi)^2
#
# With xi = 56.14:
# alpha_s = -4*56.14/(57.14)^2 = -224.56/3265.0 = -0.06878
# This matches the S48 continuum value (-0.0688).
#
# The KEY INSIGHT: alpha_s depends ONLY on xi = m^2/(J K^2), and m is fixed
# by the n_s constraint. So xi is determined by n_s alone:
# xi = (1-n_s + 2)/(-(n_s-1)) = ... let me redo:
# n_s = 1 - 2/(1+xi), so 2/(1+xi) = 1-n_s, so 1+xi = 2/(1-n_s), so xi = (1+n_s)/(1-n_s)
# For n_s = 0.965: xi = 1.965/0.035 = 56.14. Check!
#
# alpha_s = -4*xi/(1+xi)^2 = -4 * [(1+n_s)/(1-n_s)] / [2/(1-n_s)]^2
# = -4*(1+n_s)/(1-n_s) * (1-n_s)^2/4
# = -(1+n_s)*(1-n_s)
# = -(1 - n_s^2)
# = n_s^2 - 1
#
# REMARKABLE: alpha_s = n_s^2 - 1 in the continuum isotropic limit!
# For n_s = 0.965: alpha_s = 0.965^2 - 1 = 0.931225 - 1 = -0.068775
# This exactly matches our numerical result!

alpha_s_analytic = ns_planck_mean**2 - 1
print(f"  ANALYTIC RESULT (continuum isotropic):")
print(f"    alpha_s = n_s^2 - 1 = {ns_planck_mean}^2 - 1 = {alpha_s_analytic:.6f}")
print(f"    S48 numerical: {alpha_s_central:.6f}")
print(f"    Error: {abs(alpha_s_analytic - alpha_s_central)/abs(alpha_s_central):.2e}")

# In this limit, the uncertainty on alpha_s propagates DIRECTLY from n_s:
# d(alpha_s)/d(n_s) = 2*n_s ~ 1.93
# sigma(alpha_s) = 2*n_s * sigma(n_s) = 1.93 * 0.0042 = 0.0081
sigma_alpha_from_ns = 2 * ns_planck_mean * ns_planck_sigma
print(f"\n  Analytic error propagation from n_s uncertainty ALONE:")
print(f"    d(alpha_s)/d(n_s) = 2*n_s = {2*ns_planck_mean:.4f}")
print(f"    sigma(alpha_s) from n_s = {sigma_alpha_from_ns:.4f}")
print(f"    This gives alpha_s = {alpha_s_analytic:.4f} +/- {sigma_alpha_from_ns:.4f}")
print(f"    95% CI = [{alpha_s_analytic - 2*sigma_alpha_from_ns:.4f}, "
      f"{alpha_s_analytic + 2*sigma_alpha_from_ns:.4f}]")
print(f"    Includes 0? {alpha_s_analytic + 2*sigma_alpha_from_ns > 0}")

# BUT: The lattice/anisotropy effects move alpha_s from -0.069 to -0.038.
# The anisotropy and lattice dispersion REDUCE |alpha_s| by 45%.
# This reduction itself is uncertain (depends on J_xy/J_z ratio, K_pivot).

# The correction factor:
correction = alpha_s_check / alpha_s_analytic
print(f"\n  Lattice+anisotropy correction factor:")
print(f"    alpha_s(lattice) / alpha_s(continuum) = {correction:.4f}")
print(f"    = {alpha_s_check:.4f} / {alpha_s_analytic:.4f}")

# ===========================================================================
# STEP 8: GATE VERDICT
# ===========================================================================
print("\n" + "=" * 78)
print("GATE VERDICT: ALPHA-S-BAYES-49")
print("=" * 78)

# Determine verdict
if includes_zero_95:
    verdict = "PASS"
    detail = f"95% CI [{ci_95_lo:.4f}, {ci_95_hi:.4f}] includes 0"
elif tension_planck < 2.0:
    verdict = "INFO"
    detail = f"Tension {tension_planck:.1f} sigma (reduced from 4.9), 95% CI excludes 0"
else:
    # Check if tension is significantly reduced
    if tension_planck < 3.0:
        verdict = "INFO"
        detail = f"Tension {tension_planck:.2f} sigma (reduced from 4.9)"
    else:
        verdict = "FAIL"
        detail = f"Tension {tension_planck:.2f} sigma, 95% CI excludes 0"

print(f"\n  VERDICT: {verdict}")
print(f"  Detail: {detail}")
print(f"")
print(f"  POSTERIOR SUMMARY:")
print(f"    alpha_s (median +/- sigma) = {alpha_s_median:.4f} +/- {alpha_s_std:.4f}")
print(f"    68% CI = [{ci_68_lo:.4f}, {ci_68_hi:.4f}]")
print(f"    95% CI = [{ci_95_lo:.4f}, {ci_95_hi:.4f}]")
print(f"    99% CI = [{ci_99_lo:.4f}, {ci_99_hi:.4f}]")
print(f"    P(alpha_s > 0) = {frac_positive:.4f}")
print(f"")
print(f"  TENSION ANALYSIS:")
print(f"    S48 (no UQ): alpha_s = -0.038, tension = 4.9 sigma")
print(f"    This work: alpha_s = {alpha_s_median:.4f} +/- {alpha_s_std:.4f}")
print(f"    vs Planck (0 +/- 0.008): {tension_planck:.2f} sigma")
print(f"    vs Planck (-0.0045 +/- 0.0067): {tension_planck_precise:.2f} sigma")
print(f"")
print(f"  STRUCTURAL INSIGHT:")
print(f"    alpha_s = n_s^2 - 1 in continuum isotropic limit (EXACT)")
print(f"    The O-Z mechanism predicts alpha_s < 0 STRUCTURALLY")
print(f"    (any n_s < 1 gives negative running)")
print(f"    The magnitude is set by n_s alone; J_ij affects only")
print(f"    the lattice correction (S48 value is 0.55x continuum)")
print(f"")
print(f"  DOMINANT UNCERTAINTIES:")
print(f"    r(log J_xy, alpha_s) = {corr_Jxy:+.4f}")
print(f"    r(log J_z, alpha_s)  = {corr_Jz:+.4f}")
print(f"    r(log K_pivot)       = {corr_Kp:+.4f}")
print(f"    r(n_s_target)        = {corr_ns:+.4f}")
print(f"    r(log J_xy/J_z)      = {corr_ratio:+.4f}")
print(f"")
print(f"  CMB-S4 FORECAST:")
print(f"    If framework correct, detection at {significance_cmbs4:.1f} sigma with S4")
print(f"    Need sigma(alpha_s) < {sigma_needed_3sigma:.4f} for 3-sigma test")

# ===========================================================================
# SAVE
# ===========================================================================
print("\n--- Saving ---")
save_path = os.path.join(data_dir, 's49_alpha_s_bayes.npz')
np.savez(save_path,
    # Gate
    gate_name='ALPHA-S-BAYES-49',
    gate_verdict=verdict,
    gate_detail=detail,

    # Central values (from S48)
    alpha_s_central=alpha_s_central,
    m_star_central=m_star_central,
    J_C2_central=J_C2_central,
    J_su2_central=J_su2_central,
    J_u1_central=J_u1_central,
    J_eff_avg_central=J_eff_avg_central,
    K_pivot_central=K_pivot_central,

    # Posterior
    alpha_s_median=alpha_s_median,
    alpha_s_mean=alpha_s_mean,
    alpha_s_std=alpha_s_std,
    ci_68_lo=ci_68_lo,
    ci_68_hi=ci_68_hi,
    ci_95_lo=ci_95_lo,
    ci_95_hi=ci_95_hi,
    ci_99_lo=ci_99_lo,
    ci_99_hi=ci_99_hi,
    frac_positive=frac_positive,

    # Tension
    tension_planck_zero=tension_planck,
    tension_planck_precise=tension_planck_precise,

    # MC samples
    alpha_s_samples=alpha_s_valid,
    m_star_samples=m_star_valid,
    J_eff_samples=J_eff_valid,
    J_xy_samples=J_xy_valid,
    J_z_samples=J_z_valid,
    K_pivot_samples=K_pivot_valid,
    ns_target_samples=ns_target_valid,
    n_valid=n_valid,
    N_MC=N_MC,

    # Correlations
    corr_Jxy=corr_Jxy,
    corr_Jz=corr_Jz,
    corr_Kp=corr_Kp,
    corr_ns=corr_ns,
    corr_ratio=corr_ratio,

    # Priors
    sigma_J_xy=sigma_J_xy,
    sigma_J_z=sigma_J_z,
    sigma_K=sigma_K,
    p_reassign=p_reassign,

    # Analytic
    alpha_s_analytic=alpha_s_analytic,
    sigma_alpha_from_ns=sigma_alpha_from_ns,
    lattice_correction_factor=correction,

    # CMB-S4
    significance_cmbs4=significance_cmbs4,
    sigma_needed_3sigma=sigma_needed_3sigma,

    # Timing
    elapsed_s=time.time() - t0,
)
print(f"  Saved: {save_path}")

# ===========================================================================
# PLOT
# ===========================================================================
print("--- Generating plot ---")

fig = plt.figure(figsize=(18, 14))
gs = GridSpec(3, 3, figure=fig, hspace=0.35, wspace=0.35)
fig.suptitle('ALPHA-S-BAYES-49: Bayesian Uncertainty Quantification for $\\alpha_s$\n'
             r'$\alpha_s = dn_s/d(\ln k)$ Running of Spectral Index',
             fontsize=13, fontweight='bold')

# Panel 1: Posterior histogram
ax = fig.add_subplot(gs[0, 0])
bins = np.linspace(np.percentile(alpha_s_valid, 0.5), np.percentile(alpha_s_valid, 99.5), 60)
ax.hist(alpha_s_valid, bins=bins, density=True, alpha=0.7, color='C0',
        label=f'Posterior (N={n_valid})')
ax.axvline(alpha_s_median, color='C0', ls='-', lw=2, label=f'Median = {alpha_s_median:.4f}')
ax.axvline(0, color='red', ls='--', lw=2, label=r'$\alpha_s = 0$ (Planck)')
ax.axvline(alpha_s_central, color='k', ls=':', lw=1.5, label=f'S48 = {alpha_s_central:.3f}')
ax.axvspan(ci_95_lo, ci_95_hi, color='C0', alpha=0.15, label='95% CI')
ax.axvspan(-sigma_planck, sigma_planck, color='red', alpha=0.1, label=r'Planck $\pm 1\sigma$')
ax.set_xlabel(r'$\alpha_s$')
ax.set_ylabel('Posterior density')
ax.set_title(r'$P(\alpha_s | \mathrm{model})$')
ax.legend(fontsize=6.5, loc='upper left')
ax.grid(True, alpha=0.3)

# Panel 2: alpha_s vs J_xy/J_z
ax = fig.add_subplot(gs[0, 1])
scatter = ax.scatter(np.log10(J_xy_valid/J_z_valid), alpha_s_valid,
                     c=np.log10(K_pivot_valid), cmap='viridis',
                     s=2, alpha=0.3, rasterized=True)
ax.axhline(0, color='red', ls='--', lw=1.5)
ax.axhline(alpha_s_central, color='k', ls=':', lw=1)
ax.set_xlabel(r'$\log_{10}(J_{xy}/J_z)$')
ax.set_ylabel(r'$\alpha_s$')
ax.set_title(r'Sensitivity to Anisotropy Ratio')
plt.colorbar(scatter, ax=ax, label=r'$\log_{10}(K_{\rm pivot})$')
ax.grid(True, alpha=0.3)

# Panel 3: alpha_s vs K_pivot
ax = fig.add_subplot(gs[0, 2])
ax.scatter(K_pivot_valid, alpha_s_valid, c=np.log10(J_xy_valid/J_z_valid),
           cmap='coolwarm', s=2, alpha=0.3, rasterized=True)
ax.axhline(0, color='red', ls='--', lw=1.5)
ax.axvline(K_pivot_central, color='k', ls=':', lw=1)
ax.set_xlabel(r'$K_{\rm pivot}$ (cell$^{-1}$)')
ax.set_ylabel(r'$\alpha_s$')
ax.set_title(r'Sensitivity to Pivot Scale')
ax.grid(True, alpha=0.3)

# Panel 4: Correlation bar chart
ax = fig.add_subplot(gs[1, 0])
labels_corr = [r'$\ln J_{xy}$', r'$\ln J_z$', r'$\ln K_{\rm pivot}$',
               r'$n_s^{\rm target}$', r'$\ln(J_{xy}/J_z)$']
corr_vals = [corr_Jxy, corr_Jz, corr_Kp, corr_ns, corr_ratio]
colors_corr = ['C0' if c > 0 else 'C3' for c in corr_vals]
bars = ax.barh(labels_corr, [abs(c) for c in corr_vals], color=colors_corr, alpha=0.7)
for bar, c in zip(bars, corr_vals):
    ax.text(abs(c) + 0.02, bar.get_y() + bar.get_height()/2,
            f'{c:+.3f}', va='center', fontsize=8)
ax.set_xlabel(r'$|r|$ (Pearson correlation with $\alpha_s$)')
ax.set_title('Sensitivity Analysis')
ax.set_xlim([0, 1.0])
ax.grid(True, alpha=0.3, axis='x')

# Panel 5: CDF of alpha_s
ax = fig.add_subplot(gs[1, 1])
alpha_s_sorted_plot = np.sort(alpha_s_valid)
cdf = np.arange(1, len(alpha_s_sorted_plot)+1) / len(alpha_s_sorted_plot)
ax.plot(alpha_s_sorted_plot, cdf, 'C0-', lw=2)
ax.axvline(0, color='red', ls='--', lw=1.5, label=r'$\alpha_s = 0$')
ax.axhline(0.025, color='gray', ls=':', lw=1, alpha=0.5)
ax.axhline(0.975, color='gray', ls=':', lw=1, alpha=0.5)
ax.axhline(frac_positive, color='C3', ls=':', lw=1.5,
           label=f'P(>0) = {frac_positive:.3f}')
ax.set_xlabel(r'$\alpha_s$')
ax.set_ylabel('CDF')
ax.set_title('Cumulative Distribution')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 6: Prior vs posterior for J_xy
ax = fig.add_subplot(gs[1, 2])
ax.hist(np.log10(J_xy_valid), bins=50, density=True, alpha=0.5, color='C0',
        label=r'Sampled $\log J_{xy}$')
ax.hist(np.log10(J_z_valid), bins=50, density=True, alpha=0.5, color='C2',
        label=r'Sampled $\log J_z$')
ax.axvline(np.log10(J_C2_central), color='C0', ls='--', lw=2, label=f'J_C2 = {J_C2_central:.3f}')
ax.axvline(np.log10(J_su2_central), color='C2', ls='--', lw=2, label=f'J_su2 = {J_su2_central:.3f}')
ax.set_xlabel(r'$\log_{10}(J)$')
ax.set_ylabel('Density')
ax.set_title('Prior Distributions on Couplings')
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)

# Panel 7: alpha_s vs n_s_target
ax = fig.add_subplot(gs[2, 0])
ax.scatter(ns_target_valid, alpha_s_valid, s=2, alpha=0.2, color='C0', rasterized=True)
# Analytic curve
ns_range = np.linspace(0.93, 0.99, 100)
alpha_s_analytic_curve = ns_range**2 - 1  # continuum isotropic
ax.plot(ns_range, alpha_s_analytic_curve, 'r-', lw=2,
        label=r'$\alpha_s = n_s^2 - 1$ (continuum)')
ax.plot(ns_range, alpha_s_analytic_curve * correction, 'k--', lw=1.5,
        label=f'Lattice correction ({correction:.2f}x)')
ax.axvline(ns_planck_mean, color='red', ls=':', lw=1)
ax.set_xlabel(r'$n_s^{\rm target}$')
ax.set_ylabel(r'$\alpha_s$')
ax.set_title(r'$\alpha_s$ vs $n_s$ (Structural Relation)')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 8: m_star distribution
ax = fig.add_subplot(gs[2, 1])
ax.hist(m_star_valid, bins=50, density=True, alpha=0.7, color='C4')
ax.axvline(m_star_central, color='k', ls='--', lw=2,
           label=f'S48 = {m_star_central:.3f}')
ax.axvline(np.median(m_star_valid), color='C4', ls='-', lw=2,
           label=f'Median = {np.median(m_star_valid):.3f}')
ax.set_xlabel(r'$m^*$ ($M_{KK}$)')
ax.set_ylabel('Density')
ax.set_title(r'Posterior on Goldstone Mass $m^*$')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 9: Summary text
ax = fig.add_subplot(gs[2, 2])
ax.axis('off')
summary_text = (
    f"ALPHA-S-BAYES-49: {verdict}\n\n"
    f"POSTERIOR:\n"
    f"  alpha_s = {alpha_s_median:.4f} +/- {alpha_s_std:.4f}\n"
    f"  68% CI = [{ci_68_lo:.4f}, {ci_68_hi:.4f}]\n"
    f"  95% CI = [{ci_95_lo:.4f}, {ci_95_hi:.4f}]\n"
    f"  P(alpha_s > 0) = {frac_positive:.3f}\n\n"
    f"TENSION:\n"
    f"  vs Planck (0 +/- 0.008): {tension_planck:.1f} sigma\n"
    f"  vs Planck (-0.005 +/- 0.007): {tension_planck_precise:.1f} sigma\n"
    f"  S48 (no UQ): 4.9 sigma\n\n"
    f"STRUCTURAL:\n"
    f"  alpha_s = n_s^2 - 1 (continuum)\n"
    f"  = {alpha_s_analytic:.4f} (exact isotropic)\n"
    f"  Lattice correction: x{correction:.2f}\n\n"
    f"CMB-S4:\n"
    f"  Detection: {significance_cmbs4:.1f} sigma\n"
    f"  sigma needed: < {sigma_needed_3sigma:.4f}\n\n"
    f"DOMINANT SOURCE:\n"
    f"  J_xy/J_z ratio (r={corr_ratio:+.3f})"
)
ax.text(0.05, 0.95, summary_text, transform=ax.transAxes,
        fontsize=8, va='top', fontfamily='monospace',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plot_path = os.path.join(data_dir, 's49_alpha_s_bayes.png')
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
plt.close()
print(f"  Saved: {plot_path}")

elapsed = time.time() - t0
print(f"\nTotal elapsed: {elapsed:.2f} s")
print("Done.")
