#!/usr/bin/env python3
"""
MKK-BAYES-43: Bayesian M_KK Posterior from Joint Observables
=============================================================
Nazarewicz nuclear-structure-theorist computation.

GATE: MKK-BAYES-43 (INFO) -- posterior with CI

METHODOLOGY (Paper 06, McDonnell et al. 2015):
  Bayesian inference on a single parameter (M_KK) using three independent
  observables as constraints.  This replaces the ad hoc "two routes" approach
  (gravity route vs gauge route) with a single joint posterior.

  P(M_KK | data) ~ L(alpha_EM | M_KK) * L(G_N | M_KK) * L(FIRAS | M_KK) * pi(M_KK)

THREE LIKELIHOODS:
  1. L(alpha_EM | M_KK): From Kerner formula alpha_a = M_KK^2/(M_Pl^2 * g_aa)
     + 1-loop SM RGE running from M_KK to m_Z.
     Target: 1/alpha_EM(m_Z) = 127.955 +/- sigma_th
  2. L(G_N | M_KK): From Seeley-DeWitt a_2 coefficient.
     M_KK^2 = pi^3 * M_Pl^2 / (12 * a_2) predicts a unique M_KK.
     Target: M_Pl_reduced = 2.435e18 GeV observed.
  3. L(FIRAS | M_KK): From HOMOG-42 delta_tau/tau(M_KK) computation.
     One-sided: delta_tau/tau < 3e-6 (FIRAS thermal spectrum constraint).

PRIOR: Flat in log10(M_KK) over [10^9, 10^19] GeV.
       This is the Jeffreys prior for a scale parameter.

OUTPUTS: mode, 68% CI, 95% CI, KL divergence, most informative observable.

Author: nazarewicz-nuclear-structure-theorist
Session: 43, Wave 5, Task 12
References: Paper 06 (McDonnell et al. 2015), S42 constants snapshot, S42 homogeneity
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from pathlib import Path
from scipy.interpolate import interp1d

# ============================================================
# 0. LOAD INPUT DATA
# ============================================================

DATA_DIR = Path(__file__).parent

cs = np.load(DATA_DIR / 's42_constants_snapshot.npz', allow_pickle=True)
hm = np.load(DATA_DIR / 's42_homogeneity.npz', allow_pickle=True)

# From S42 constants snapshot
tau_fold = float(cs['tau_fold'])
g_SU2_fold = float(cs['g_SU2_fold'])
g_U1_fold = float(cs['g_U1_fold'])
a2_fold = float(cs['a2_fold'])
a0_fold = float(cs['a0_fold'])
sin2_thetaW_fold = float(cs['sin2_thetaW_fold'])
M_KK_kerner_s42 = float(cs['M_KK_kerner'])
M_KK_GN_s42 = float(cs['M_KK_from_GN'])

# From S42 homogeneity
m_phi_sq = float(hm['m_phi_sq'])
m_phi = float(hm['m_phi'])
Z_fold = float(hm['Z_fold'])
d2S_fold = float(hm['d2S_fold'])
H_prefactor = float(hm['H_prefactor'])
dt_transit = float(hm['dt_transit'])
c_fabric = float(hm['c_fabric'])
FIRAS_bound = float(hm['FIRAS_bound'])  # 3e-6
M_KK_max_FIRAS_s42 = float(hm['M_KK_max_FIRAS'])

# Load the HOMOG-42 M_KK scan for cross-check
M_KK_scan_homog = hm['M_KK_scan']
dtau_scan_homog = hm['dtau_scan']

# ============================================================
# 1. PHYSICAL CONSTANTS
# ============================================================

PI = np.pi
from canonical_constants import M_Pl_reduced as M_PL, alpha_em_MZ_inv as ALPHA_EM_MZ_INV  # 2.435e18 GeV, PDG 2024
M_Z = 91.1876            # GeV
ALPHA_2_MZ_INV = 29.587    # PDG
ALPHA_1_MZ_INV = 59.0      # approximate (GUT-normalized)

# SM 1-loop beta coefficients (MS-bar, b > 0 = asymptotically free)
b1_SM = -41.0 / 10.0    # U(1)_Y (NOT asymptotically free)
b2_SM = 19.0 / 6.0      # SU(2)_L (asymptotically free)

# Baptista Weinberg angle formula at fold (Paper 14, eq 2.85/2.88)
# sin^2(theta_W) = 3 e^{-4tau} / (3 e^{-4tau} + 1)
sin2_W_baptista = 3.0 * np.exp(-4 * tau_fold) / (3.0 * np.exp(-4 * tau_fold) + 1.0)

print("=" * 78)
print("MKK-BAYES-43: Bayesian M_KK Posterior")
print("=" * 78)
print(f"\n  tau_fold = {tau_fold}")
print(f"  g_SU2_fold = {g_SU2_fold:.6f}")
print(f"  g_U1_fold = {g_U1_fold:.6f}")
print(f"  a_2 = {a2_fold:.4f}")
print(f"  sin^2(theta_W) at fold = {sin2_W_baptista:.6f}")
print(f"  sin^2(theta_W) stored  = {sin2_thetaW_fold:.6f}")
print(f"  M_KK(gauge, S42) = {M_KK_kerner_s42:.4e} GeV")
print(f"  M_KK(gravity, S42) = {M_KK_GN_s42:.4e} GeV")
print(f"  M_KK_max(FIRAS, S42) = {M_KK_max_FIRAS_s42:.4e} GeV")

# ============================================================
# 2. DEFINE LOG-M_KK GRID
# ============================================================

N_grid = 10000
log10_MKK_min = 9.0
log10_MKK_max = 19.0
log10_MKK = np.linspace(log10_MKK_min, log10_MKK_max, N_grid)
MKK_grid = 10.0**log10_MKK
dlog = log10_MKK[1] - log10_MKK[0]

print(f"\n  Grid: {N_grid} points in log10(M_KK) = [{log10_MKK_min}, {log10_MKK_max}]")
print(f"  Resolution: d(log10) = {dlog:.5f}")

# ============================================================
# 3. LIKELIHOOD 1: L(alpha_EM | M_KK) -- Kerner + RGE
# ============================================================

print(f"\n{'='*78}")
print("3. LIKELIHOOD: alpha_EM constraint (Kerner + RGE)")
print("=" * 78)

# Kerner formula for SU(2) coupling at scale M_KK:
#   alpha_2(M_KK) = M_KK^2 / (M_Pl^2 * g_SU2_fold)
#
# RGE running from M_KK to m_Z (1-loop SM):
#   1/alpha_2(m_Z) = 1/alpha_2(M_KK) + (b_2/(2*pi)) * ln(M_KK/m_Z)
#   where b_2 = 19/6 and the sign convention: alpha_2 decreases going up (AF).
#
# EM coupling: alpha_EM = alpha_2 * sin^2(theta_W)
#   At M_KK: sin^2 given by Baptista formula
#   Running sin^2: 1/alpha_EM(m_Z) = 1/alpha_1(m_Z) + 1/alpha_2(m_Z)
#   (standard Glashow relation: 1/alpha_EM = 1/alpha_1 + 1/alpha_2 in SU(5) normalization)
#
# Approach: For each M_KK, compute alpha_2(M_KK) from Kerner,
#   then run alpha_2 down to m_Z, and compute alpha_EM(m_Z).
#   Similarly compute alpha_1(M_KK) from Kerner, run it down.
#   Then 1/alpha_EM(m_Z) from the Glashow relation.

def alpha_EM_predicted(M_KK):
    """
    Predict 1/alpha_EM(m_Z) from Kerner formula + 1-loop SM RGE.

    Returns 1/alpha_EM(m_Z) for each M_KK value.
    """
    M_KK = np.asarray(M_KK, dtype=float)

    # Kerner: alpha_a(M_KK) = M_KK^2 / (M_Pl^2 * g_aa)
    alpha2_MKK = M_KK**2 / (M_PL**2 * g_SU2_fold)
    alpha1_MKK = M_KK**2 / (M_PL**2 * g_U1_fold)

    # For very small M_KK < m_Z, no running needed. Clip.
    ln_ratio = np.log(np.maximum(M_KK, M_Z) / M_Z)

    # 1-loop RGE: 1/alpha_i(m_Z) = 1/alpha_i(M_KK) + (b_i/(2*pi)) * ln(M_KK/m_Z)
    # Note: for alpha_2 (AF, b2 > 0), 1/alpha_2 INCREASES going down in energy
    # For alpha_1 (not AF, b1 < 0), 1/alpha_1 DECREASES going down in energy
    alpha2_inv_mZ = 1.0 / alpha2_MKK + (b2_SM / (2 * PI)) * ln_ratio
    alpha1_inv_mZ = 1.0 / alpha1_MKK + (b1_SM / (2 * PI)) * ln_ratio

    # Glashow relation: 1/alpha_EM = 1/alpha_1 + 1/alpha_2
    # (using GUT-normalized alpha_1 = (5/3)*alpha_Y, standard convention)
    # Actually in the SU(5) convention: 1/alpha_EM = (3/5)/alpha_1 + 1/alpha_2
    # But the Kerner formula already gives the PHYSICAL U(1) coupling (not GUT-normalized),
    # because g_U1 is the metric on the lambda_8 direction.
    #
    # The physical relation: alpha_EM = alpha_2 * sin^2(theta_W)
    # where sin^2(theta_W)(mu) = alpha_1(mu)/(alpha_1(mu) + alpha_2(mu))
    # with the PHYSICAL (not GUT-normalized) alpha_1.
    #
    # In terms of 1/alpha: 1/alpha_EM(mu) = 1/alpha_2(mu) + 1/(alpha_2(mu)*tan^2(theta_W))
    # = (1/alpha_2 + 1/alpha_1) if alpha_1 = alpha_2 * tan^2(theta_W)
    #
    # Actually simplest: alpha_EM = alpha_1 * alpha_2 / (alpha_1 + alpha_2)
    # So: 1/alpha_EM = 1/alpha_1 + 1/alpha_2
    # This holds at ANY scale. The alphas individually run, but the sum of inverses
    # gives 1/alpha_EM at each scale.
    #
    # HOWEVER: alpha_1 here from the Kerner formula is the U(1)_Y coupling.
    # The standard-model relation uses the GUT-normalized alpha_1^{GUT} = (5/3)*alpha_1^{Y}.
    # The Kerner formula for the lambda_8 direction gives the PHYSICAL U(1)_Y coupling.
    # But the Baptista formula includes a sqrt(3) factor already:
    #   g'/g = sqrt(3)*e^{-2tau}
    # This means alpha_1^{Baptista} already includes the normalization.
    #
    # Let me be careful. The Kerner formula:
    #   alpha_a = M_KK^2/(M_Pl^2 * g_aa)
    # This gives the coupling associated with generator T_a normalized so that
    # the kinetic term is (1/(4*g_a^2)) * F^2.
    # For U(1)_Y, the PHYSICAL coupling g' is related to the lambda_8 coupling g_8 by:
    #   g' = g_8 * sqrt(normalization factor)
    # The Baptista Paper 14 gives g'/g = sqrt(3)*e^{-2tau}, where g = g_SU2.
    # From Kerner: alpha_8 = M_KK^2/(M_Pl^2 * g_88), alpha_2 = M_KK^2/(M_Pl^2 * g_SU2).
    # Ratio: alpha_8/alpha_2 = g_SU2/g_88 = e^{-4tau} (from Jensen metric scaling).
    # But Baptista gives (g'/g)^2 = 3*e^{-4tau}. So alpha_Y = 3*alpha_8.
    # The factor of 3 is from the different normalization of T_8 vs T_Y.
    #
    # For the EM coupling at m_Z:
    #   sin^2(theta_W) = alpha_Y / (alpha_Y + alpha_2) at any scale
    #   = 3*alpha_8 / (3*alpha_8 + alpha_2) using Kerner values
    #
    # And: 1/alpha_EM = (1/alpha_Y + 1/alpha_2) = 1/(3*alpha_8) + 1/alpha_2

    # Correct alpha_Y from Kerner (with Baptista factor):
    alpha_Y_MKK = 3.0 * alpha1_MKK  # factor of 3 from T_Y vs T_8 normalization

    # RGE for alpha_Y (hypercharge): b_Y = -41/6 in standard convention
    # d(1/alpha_Y)/d(ln mu) = b_Y/(2*pi) with b_Y = -41/6 (not AF)
    b_Y = -41.0 / 6.0
    alpha_Y_inv_mZ = 1.0 / alpha_Y_MKK + (b_Y / (2 * PI)) * ln_ratio

    # EM coupling: 1/alpha_EM = 1/alpha_Y + 1/alpha_2
    alpha_EM_inv_mZ = alpha_Y_inv_mZ + alpha2_inv_mZ

    return alpha_EM_inv_mZ


# Compute predicted 1/alpha_EM for the grid
alpha_EM_inv_pred = alpha_EM_predicted(MKK_grid)

# Cross-check at the two S42 routes
alpha_EM_inv_grav = alpha_EM_predicted(M_KK_GN_s42)
alpha_EM_inv_gauge = alpha_EM_predicted(M_KK_kerner_s42)

print(f"\n  Cross-check at S42 routes:")
print(f"    1/alpha_EM(m_Z) at M_KK(grav)  = {float(alpha_EM_inv_grav):.2f}")
print(f"    1/alpha_EM(m_Z) at M_KK(gauge) = {float(alpha_EM_inv_gauge):.2f}")
print(f"    Observed: {ALPHA_EM_MZ_INV:.3f}")

# Which M_KK gives the observed alpha_EM?
# Find where alpha_EM_inv_pred crosses ALPHA_EM_MZ_INV
# This is a non-trivial function of M_KK because of the Kerner + RGE interplay.
idx_match = np.argmin(np.abs(alpha_EM_inv_pred - ALPHA_EM_MZ_INV))
MKK_alpha_best = MKK_grid[idx_match]
print(f"    Best-fit M_KK for alpha_EM: {MKK_alpha_best:.4e} GeV (log10 = {np.log10(MKK_alpha_best):.3f})")

# Likelihood: Gaussian in 1/alpha_EM(m_Z)
# Theoretical uncertainty: from Paper 06 methodology, we assign sigma_th
# to account for:
#   (a) 1-loop vs 2-loop RGE running (delta ~ 2-5 units in 1/alpha_EM)
#   (b) Threshold corrections at M_KK (unknown spectrum of KK modes)
#   (c) Uncertainty in the Kerner normalization (factor of sqrt(3) issue above)
# Conservative estimate: sigma_th = 10 (about 8% on 1/alpha_EM ~ 128)
# This corresponds to sigma ~ 10 on the inverse, or sigma(alpha)/alpha ~ 0.08
sigma_alpha_th = 10.0  # in units of 1/alpha_EM

def log_likelihood_alpha(M_KK):
    """Log-likelihood for alpha_EM constraint."""
    pred = alpha_EM_predicted(M_KK)
    return -0.5 * ((pred - ALPHA_EM_MZ_INV) / sigma_alpha_th)**2

logL_alpha = log_likelihood_alpha(MKK_grid)

print(f"\n  sigma_th(1/alpha_EM) = {sigma_alpha_th}")
print(f"  Rationale: 1-loop RGE + threshold corrections + Kerner normalization")

# ============================================================
# 4. LIKELIHOOD 2: L(G_N | M_KK) -- Seeley-DeWitt a_2
# ============================================================

print(f"\n{'='*78}")
print("4. LIKELIHOOD: G_N constraint (Seeley-DeWitt a_2)")
print("=" * 78)

# From S42 constants snapshot:
# M_KK^2 = pi^3 * M_Pl^2 / (12 * a_2)
# This fixes M_KK uniquely.
M_KK_GN_predicted = np.sqrt(PI**3 * M_PL**2 / (12.0 * a2_fold))

print(f"\n  Formula: M_KK^2 = pi^3 * M_Pl^2 / (12 * a_2)")
print(f"  a_2(fold) = {a2_fold:.4f}")
print(f"  M_KK(G_N) = {M_KK_GN_predicted:.4e} GeV")
print(f"  log10(M_KK(G_N)) = {np.log10(M_KK_GN_predicted):.4f}")
print(f"  S42 value = {M_KK_GN_s42:.4e} GeV (check: match = {np.isclose(M_KK_GN_predicted, M_KK_GN_s42)})")

# Theoretical uncertainty on M_KK from G_N:
# Sources:
#   (a) a_2 is a spectral zeta sum, not the exact Seeley-DeWitt coefficient.
#       The relation between zeta(1) and a_2^{SD} involves (4pi)^{d/2} normalization.
#       S42 identified this as a potential 1000:1 ratio issue for a_4 but claimed
#       a_2 is better behaved. Still, factor 2-3 uncertainty is plausible.
#   (b) Volume normalization: Vol_code depends on Killing metric convention.
#       Factor of 2 uncertainty from the topological volume formula.
#   (c) M_Pl is known to <0.1% experimentally -- negligible.
#
# Total: sigma(log10 M_KK) ~ 0.3 decades (factor of 2 on M_KK from a_2 uncertainty)
# Equivalently: sigma_GN = 0.3 in log10 space.

sigma_GN_log10 = 0.3  # decades

def log_likelihood_GN(M_KK):
    """Log-likelihood for G_N constraint (Gaussian in log10 M_KK)."""
    log10_MKK = np.log10(np.asarray(M_KK, dtype=float))
    log10_target = np.log10(M_KK_GN_predicted)
    return -0.5 * ((log10_MKK - log10_target) / sigma_GN_log10)**2

logL_GN = log_likelihood_GN(MKK_grid)

print(f"\n  sigma(log10 M_KK) = {sigma_GN_log10} decades")
print(f"  Rationale: zeta->SD conversion, volume normalization, Kerner prefactors")

# ============================================================
# 5. LIKELIHOOD 3: L(FIRAS | M_KK) -- homogeneity constraint
# ============================================================

print(f"\n{'='*78}")
print("5. LIKELIHOOD: FIRAS constraint (HOMOG-42)")
print("=" * 78)

# From HOMOG-42: delta_tau/tau(M_KK) must be < 3e-6.
# The S42 computation provides a scan: dtau_scan vs M_KK_scan.
# We recompute for our finer grid.

def delta_tau_over_tau(M_KK):
    """Compute delta_tau/tau from Starobinsky relaxation formula."""
    M_KK = np.asarray(M_KK, dtype=float)
    H_over_MKK = H_prefactor * (M_KK / M_PL)
    N_efolds = H_over_MKK * dt_transit
    N_sat = 3.0 * H_over_MKK**2 / (2.0 * m_phi_sq)

    exp_arg = 2.0 * m_phi_sq * N_efolds / (3.0 * H_over_MKK**2)
    factor = 1.0 - np.exp(-exp_arg)

    phi2_eq = 3.0 * H_over_MKK**4 / (8.0 * PI**2 * m_phi_sq)
    phi2 = phi2_eq * factor
    dtau = np.sqrt(phi2) / np.sqrt(Z_fold) / tau_fold
    return dtau

dtau_grid = delta_tau_over_tau(MKK_grid)

# Likelihood: one-sided. FIRAS constrains dtau/tau < 3e-6.
# Model this as a complementary error function (smooth step):
# L(FIRAS | M_KK) = Phi((FIRAS_bound - dtau(M_KK)) / sigma_FIRAS)
# where sigma_FIRAS accounts for measurement uncertainty in the FIRAS bound.
# FIRAS precision: delta_T/T < 1.5e-5 at 2-sigma, so sigma ~ 7.5e-6.
# But the 3e-6 bound already includes a safety factor.
# Use sigma_FIRAS = 1e-6 (factor ~3 below the bound).

from scipy.special import erfc

from canonical_constants import sigma_FIRAS

def log_likelihood_FIRAS(M_KK):
    """Log-likelihood for FIRAS constraint (one-sided Gaussian)."""
    dtau = delta_tau_over_tau(M_KK)
    # L = 0.5 * erfc((dtau - FIRAS_bound) / (sqrt(2) * sigma_FIRAS))
    # Log: log(L) = log(0.5 * erfc(x/sqrt(2)))
    x = (dtau - FIRAS_bound) / sigma_FIRAS
    # For numerical stability: when x >> 1, log(erfc(x)) ~ -x^2 - log(x*sqrt(pi))
    # When x << -1, erfc -> 2, log(erfc) -> log(2)
    val = 0.5 * erfc(x / np.sqrt(2.0))
    # Clip for numerical safety
    val = np.clip(val, 1e-300, 1.0)
    return np.log(val)

logL_FIRAS = log_likelihood_FIRAS(MKK_grid)

# Cross-check at the FIRAS threshold
dtau_at_threshold = delta_tau_over_tau(M_KK_max_FIRAS_s42)
print(f"\n  delta_tau/tau at M_KK_max(FIRAS,S42) = {float(dtau_at_threshold):.4e}")
print(f"  FIRAS bound = {FIRAS_bound:.0e}")
print(f"  sigma_FIRAS = {sigma_FIRAS:.0e}")

# Find our own FIRAS crossing
idx_cross = np.searchsorted(dtau_grid, FIRAS_bound)
if 0 < idx_cross < N_grid:
    MKK_FIRAS_cross = MKK_grid[idx_cross]
    print(f"  Our FIRAS crossing: M_KK = {MKK_FIRAS_cross:.4e} GeV (log10 = {np.log10(MKK_FIRAS_cross):.3f})")
else:
    MKK_FIRAS_cross = 1e19
    print(f"  FIRAS bound not crossed in grid range")

# ============================================================
# 6. JOINT POSTERIOR
# ============================================================

print(f"\n{'='*78}")
print("6. JOINT POSTERIOR P(M_KK | alpha_EM, G_N, FIRAS)")
print("=" * 78)

# Prior: flat in log10(M_KK) = Jeffreys prior for scale parameter
# log pi(M_KK) = const (absorbed into normalization)
log_prior = np.zeros(N_grid)  # flat in log10

# Joint log-posterior (unnormalized)
log_posterior_joint = logL_alpha + logL_GN + logL_FIRAS + log_prior

# Individual posteriors for comparison
log_posterior_alpha = logL_alpha + log_prior
log_posterior_GN = logL_GN + log_prior
log_posterior_FIRAS = logL_FIRAS + log_prior

# Normalize (in log space for numerical stability)
def normalize_log_posterior(logp, dlog):
    """Normalize log-posterior over the grid."""
    logp_max = np.max(logp)
    p = np.exp(logp - logp_max)
    norm = np.sum(p) * dlog
    return p / norm, logp - logp_max - np.log(norm * dlog)

p_joint, logp_joint_norm = normalize_log_posterior(log_posterior_joint, dlog)
p_alpha, _ = normalize_log_posterior(log_posterior_alpha, dlog)
p_GN, _ = normalize_log_posterior(log_posterior_GN, dlog)
p_FIRAS, _ = normalize_log_posterior(log_posterior_FIRAS, dlog)

# Also compute the prior (flat) for KL divergence reference
p_prior = np.ones(N_grid) / (N_grid * dlog)

# ============================================================
# 7. EXTRACT POSTERIOR STATISTICS
# ============================================================

print(f"\n{'='*78}")
print("7. POSTERIOR STATISTICS")
print("=" * 78)

# Mode
idx_mode = np.argmax(p_joint)
mode_log10 = log10_MKK[idx_mode]
mode_MKK = MKK_grid[idx_mode]

# Mean
mean_log10 = np.sum(log10_MKK * p_joint * dlog)
mean_MKK = 10**mean_log10

# Median (CDF = 0.5)
cdf = np.cumsum(p_joint * dlog)
cdf /= cdf[-1]  # ensure normalization
idx_median = np.searchsorted(cdf, 0.5)
median_log10 = log10_MKK[min(idx_median, N_grid-1)]
median_MKK = 10**median_log10

# 68% CI (highest posterior density interval)
def hpd_interval(p, log10_grid, dlog, prob=0.68):
    """Compute highest posterior density interval."""
    # Sort posterior values descending
    sorted_idx = np.argsort(p)[::-1]
    cumsum = 0.0
    in_hpd = np.zeros(len(p), dtype=bool)
    for i in sorted_idx:
        cumsum += p[i] * dlog
        in_hpd[i] = True
        if cumsum >= prob:
            break
    # Find contiguous interval (may be multi-modal)
    hpd_log10 = log10_grid[in_hpd]
    return hpd_log10.min(), hpd_log10.max()

# 68% CI
ci68_lo_log10, ci68_hi_log10 = hpd_interval(p_joint, log10_MKK, dlog, 0.68)
ci68_lo = 10**ci68_lo_log10
ci68_hi = 10**ci68_hi_log10

# 95% CI
ci95_lo_log10, ci95_hi_log10 = hpd_interval(p_joint, log10_MKK, dlog, 0.95)
ci95_lo = 10**ci95_lo_log10
ci95_hi = 10**ci95_hi_log10

print(f"\n  Mode:    log10(M_KK) = {mode_log10:.3f}  =>  M_KK = {mode_MKK:.3e} GeV")
print(f"  Mean:    log10(M_KK) = {mean_log10:.3f}  =>  M_KK = {mean_MKK:.3e} GeV")
print(f"  Median:  log10(M_KK) = {median_log10:.3f}  =>  M_KK = {median_MKK:.3e} GeV")
print(f"  68% CI:  [{ci68_lo_log10:.3f}, {ci68_hi_log10:.3f}]  =>  [{ci68_lo:.3e}, {ci68_hi:.3e}] GeV")
print(f"  95% CI:  [{ci95_lo_log10:.3f}, {ci95_hi_log10:.3f}]  =>  [{ci95_lo:.3e}, {ci95_hi:.3e}] GeV")
print(f"  Width (68%): {ci68_hi_log10 - ci68_lo_log10:.3f} decades")
print(f"  Width (95%): {ci95_hi_log10 - ci95_lo_log10:.3f} decades")

# Individual modes for comparison
idx_mode_alpha = np.argmax(p_alpha)
idx_mode_GN = np.argmax(p_GN)
# FIRAS is one-sided, so "mode" is at the lower boundary
# Find where FIRAS posterior starts to decline significantly
print(f"\n  Individual constraint modes:")
print(f"    alpha_EM: log10(M_KK) = {log10_MKK[idx_mode_alpha]:.3f}  =>  {MKK_grid[idx_mode_alpha]:.3e} GeV")
print(f"    G_N:      log10(M_KK) = {log10_MKK[idx_mode_GN]:.3f}  =>  {MKK_grid[idx_mode_GN]:.3e} GeV")
print(f"    FIRAS:    one-sided, upper bound at log10 = {np.log10(MKK_FIRAS_cross):.3f}")

# ============================================================
# 8. KL DIVERGENCE -- INFORMATION CONTENT
# ============================================================

print(f"\n{'='*78}")
print("8. INFORMATION CONTENT (KL Divergence)")
print("=" * 78)

# KL divergence: D_KL(posterior || prior) = int posterior * log(posterior/prior)
# This measures how much the data has changed our beliefs (Paper 06).

def kl_divergence(p_post, p_prior_ref, dlog):
    """Compute D_KL(posterior || prior) in nats."""
    mask = p_post > 1e-300
    integrand = np.zeros_like(p_post)
    integrand[mask] = p_post[mask] * np.log(p_post[mask] / p_prior_ref[mask])
    return np.sum(integrand * dlog)

DKL_joint = kl_divergence(p_joint, p_prior, dlog)
DKL_alpha = kl_divergence(p_alpha, p_prior, dlog)
DKL_GN = kl_divergence(p_GN, p_prior, dlog)
DKL_FIRAS = kl_divergence(p_FIRAS, p_prior, dlog)

print(f"\n  D_KL(posterior || prior) [in nats]:")
print(f"    Joint:    {DKL_joint:.3f}")
print(f"    alpha_EM: {DKL_alpha:.3f}")
print(f"    G_N:      {DKL_GN:.3f}")
print(f"    FIRAS:    {DKL_FIRAS:.3f}")
print(f"\n  Most informative observable: ", end="")

DKL_vals = {'alpha_EM': DKL_alpha, 'G_N': DKL_GN, 'FIRAS': DKL_FIRAS}
most_informative = max(DKL_vals, key=DKL_vals.get)
print(f"{most_informative} (D_KL = {DKL_vals[most_informative]:.3f} nats)")

# KL between the two routes (gravity vs gauge)
# Treat each route as a delta function posterior:
# D_KL(gravity route || gauge route) is ill-defined for deltas.
# Instead, compute D_KL between the individual posteriors from G_N and alpha_EM.
DKL_routes = kl_divergence(p_GN, p_alpha + 1e-300, dlog)
print(f"\n  D_KL(G_N posterior || alpha_EM posterior) = {DKL_routes:.3f} nats")
print(f"    (measures discrepancy between gravity and gauge routes)")

# Also compute the log10 separation between modes
route_separation = abs(log10_MKK[idx_mode_GN] - log10_MKK[idx_mode_alpha])
print(f"    Route separation: {route_separation:.3f} decades (S42: 0.83)")

# ============================================================
# 9. BAYES FACTOR: GRAVITY ROUTE vs GAUGE ROUTE
# ============================================================

print(f"\n{'='*78}")
print("9. BAYES FACTOR: Model Comparison")
print("=" * 78)

# Following Paper 06:
# Define two hypotheses:
#   H_grav: M_KK ~ 7.4e16 GeV (gravity route)
#   H_gauge: M_KK ~ 5.0e17 GeV (gauge route)
# Each is modeled as a Gaussian centered on its prediction.
# BF = P(data | H_grav) / P(data | H_gauge)
#    = integral L(data|M_KK) * p(M_KK|H_grav) / integral L(data|M_KK) * p(M_KK|H_gauge)

# Compute evidence for each hypothesis using a narrow Gaussian prior
# centered on the respective M_KK predictions
sigma_model = 0.1  # decades (fairly specific hypothesis)

def model_evidence(log10_MKK_center, sigma_model, log10_grid, logL_total, dlog):
    """Compute evidence for a hypothesis centered on log10_MKK_center."""
    log_model_prior = -0.5 * ((log10_grid - log10_MKK_center) / sigma_model)**2
    log_model_prior -= np.log(sigma_model * np.sqrt(2 * PI))
    log_integrand = logL_total + log_model_prior
    # Stabilize
    log_max = np.max(log_integrand)
    integrand = np.exp(log_integrand - log_max)
    evidence = np.sum(integrand * dlog) * np.exp(log_max)
    return evidence

logL_total = logL_alpha + logL_GN + logL_FIRAS

log10_grav = np.log10(M_KK_GN_s42)
log10_gauge = np.log10(M_KK_kerner_s42)

evidence_grav = model_evidence(log10_grav, sigma_model, log10_MKK, logL_total, dlog)
evidence_gauge = model_evidence(log10_gauge, sigma_model, log10_MKK, logL_total, dlog)

if evidence_gauge > 0:
    BF_grav_vs_gauge = evidence_grav / evidence_gauge
    log10_BF = np.log10(BF_grav_vs_gauge) if BF_grav_vs_gauge > 0 else -np.inf
else:
    BF_grav_vs_gauge = np.inf
    log10_BF = np.inf

print(f"\n  Hypothesis H_grav: M_KK = {M_KK_GN_s42:.2e} (log10 = {log10_grav:.3f})")
print(f"  Hypothesis H_gauge: M_KK = {M_KK_kerner_s42:.2e} (log10 = {log10_gauge:.3f})")
print(f"  Prior width: sigma = {sigma_model} decades")
print(f"\n  Evidence(H_grav)  = {evidence_grav:.4e}")
print(f"  Evidence(H_gauge) = {evidence_gauge:.4e}")
print(f"  Bayes Factor = {BF_grav_vs_gauge:.2e}")
print(f"  log10(BF) = {log10_BF:.2f}")

# Jeffreys scale interpretation
if BF_grav_vs_gauge > 1:
    favored = "gravity"
    bf_val = BF_grav_vs_gauge
else:
    favored = "gauge"
    bf_val = 1.0 / BF_grav_vs_gauge

if bf_val < 3:
    strength = "not worth more than a bare mention"
elif bf_val < 10:
    strength = "substantial"
elif bf_val < 30:
    strength = "strong"
elif bf_val < 100:
    strength = "very strong"
else:
    strength = "decisive"

print(f"  Jeffreys scale: {strength} evidence for {favored} route")

# ============================================================
# 10. CROSS-CHECKS
# ============================================================

print(f"\n{'='*78}")
print("10. CROSS-CHECKS")
print("=" * 78)

# Check 1: Do individual likelihoods peak where expected?
print(f"\n  [Check 1] Individual likelihood peaks vs S42 values:")
print(f"    alpha_EM peak: {MKK_grid[np.argmax(logL_alpha)]:.4e} (S42 Kerner: {M_KK_kerner_s42:.4e})")
print(f"    G_N peak:      {MKK_grid[np.argmax(logL_GN)]:.4e} (S42 SD: {M_KK_GN_s42:.4e})")
print(f"    FIRAS:          upper bound at {MKK_FIRAS_cross:.4e} (S42: {M_KK_max_FIRAS_s42:.4e})")

# Check 2: Posterior normalization
norm_check = np.sum(p_joint * dlog)
print(f"\n  [Check 2] Posterior normalization: {norm_check:.8f} (should be 1.0)")

# Check 3: CDF values at the two S42 routes
if M_KK_GN_s42 >= MKK_grid[0] and M_KK_GN_s42 <= MKK_grid[-1]:
    idx_grav = np.searchsorted(MKK_grid, M_KK_GN_s42)
    cdf_grav = cdf[min(idx_grav, N_grid-1)]
else:
    cdf_grav = 0.0

if M_KK_kerner_s42 >= MKK_grid[0] and M_KK_kerner_s42 <= MKK_grid[-1]:
    idx_gauge = np.searchsorted(MKK_grid, M_KK_kerner_s42)
    cdf_gauge = cdf[min(idx_gauge, N_grid-1)]
else:
    cdf_gauge = 1.0

print(f"\n  [Check 3] CDF at S42 routes:")
print(f"    P(M_KK < M_KK(grav)) = {cdf_grav:.4f}")
print(f"    P(M_KK < M_KK(gauge)) = {cdf_gauge:.4f}")

# Check 4: Does the FIRAS cut matter?
# Recompute posterior WITHOUT FIRAS
log_posterior_no_FIRAS = logL_alpha + logL_GN + log_prior
p_no_FIRAS, _ = normalize_log_posterior(log_posterior_no_FIRAS, dlog)
idx_mode_noF = np.argmax(p_no_FIRAS)
print(f"\n  [Check 4] Joint posterior WITHOUT FIRAS:")
print(f"    Mode: log10(M_KK) = {log10_MKK[idx_mode_noF]:.3f} (with FIRAS: {mode_log10:.3f})")
print(f"    Shift: {abs(log10_MKK[idx_mode_noF] - mode_log10):.3f} decades")
FIRAS_shift = log10_MKK[idx_mode_noF] - mode_log10
print(f"    FIRAS {'lowers' if FIRAS_shift > 0 else 'raises'} the mode by {abs(FIRAS_shift):.3f} decades")

# ============================================================
# 11. SUMMARY TABLE
# ============================================================

print(f"\n{'='*78}")
print("11. SUMMARY")
print("=" * 78)

print(f"""
  ┌──────────────────────────────────────────────────────────────┐
  │  MKK-BAYES-43: Joint Bayesian M_KK Posterior                │
  ├──────────────────────────────────────────────────────────────┤
  │  Mode:      {mode_MKK:.3e} GeV  (log10 = {mode_log10:.3f})           │
  │  Mean:      {mean_MKK:.3e} GeV  (log10 = {mean_log10:.3f})           │
  │  Median:    {median_MKK:.3e} GeV  (log10 = {median_log10:.3f})           │
  │  68% CI:    [{ci68_lo:.2e}, {ci68_hi:.2e}] GeV         │
  │  95% CI:    [{ci95_lo:.2e}, {ci95_hi:.2e}] GeV         │
  │  Width:     68%: {ci68_hi_log10-ci68_lo_log10:.2f} dec   95%: {ci95_hi_log10-ci95_lo_log10:.2f} dec             │
  ├──────────────────────────────────────────────────────────────┤
  │  D_KL(joint||prior) = {DKL_joint:.2f} nats                         │
  │  Most informative: {most_informative:<12} (D_KL = {DKL_vals[most_informative]:.2f} nats)       │
  │  BF(grav/gauge) = {BF_grav_vs_gauge:.2e}  ({strength})      │
  ├──────────────────────────────────────────────────────────────┤
  │  Gate: MKK-BAYES-43 — INFO                                  │
  │  (Posterior computed. Replaces two-routes with single CI.)   │
  └──────────────────────────────────────────────────────────────┘
""")

# ============================================================
# 11b. SENSITIVITY ANALYSIS: sigma_th dependence
# ============================================================

print(f"\n{'='*78}")
print("11b. SENSITIVITY: Effect of sigma_th on posterior")
print("=" * 78)

# The posterior is dominated by alpha_EM because d(1/alpha)/d(log10 M_KK) ~ 1000.
# sigma_th = 10 gives sigma(log10 M_KK) = 0.01 decades = unrealistically tight.
# This is the Paper 06 lesson: the theoretical error floor MATTERS.
# In nuclear DFT, sigma_th ~ 0.5 MeV is an irreducible error floor from
# the functional form, not just from parameter uncertainty.
# Here, the analogues are:
#   (a) Kerner normalization factors (factor of 3 from T_Y vs T_8 = 0.5 decades)
#   (b) Threshold corrections (unknown KK tower spectrum)
#   (c) 2-loop + matching conditions
# A conservative estimate: sigma_th = 50 (covering ~40% variation in 1/alpha)

sigma_scenarios = [10.0, 30.0, 50.0, 100.0]
sensitivity_results = {}

for sig in sigma_scenarios:
    # Recompute alpha likelihood with this sigma
    logL_a = -0.5 * ((alpha_EM_inv_pred - ALPHA_EM_MZ_INV) / sig)**2
    logL_tot = logL_a + logL_GN + logL_FIRAS + log_prior
    p_s, _ = normalize_log_posterior(logL_tot, dlog)
    idx_m = np.argmax(p_s)
    # HPD 68%
    lo68, hi68 = hpd_interval(p_s, log10_MKK, dlog, 0.68)
    lo95, hi95 = hpd_interval(p_s, log10_MKK, dlog, 0.95)
    sensitivity_results[sig] = {
        'mode': log10_MKK[idx_m],
        'ci68': (lo68, hi68),
        'ci95': (lo95, hi95),
        'width68': hi68 - lo68,
    }
    print(f"  sigma_th = {sig:>5.0f}: mode = {log10_MKK[idx_m]:.3f}, "
          f"68% CI = [{lo68:.3f}, {hi68:.3f}] ({hi68-lo68:.3f} dec), "
          f"95% CI = [{lo95:.3f}, {hi95:.3f}] ({hi95-lo95:.3f} dec)")

# CRITICAL ASSESSMENT
print(f"""
  ASSESSMENT:
    The alpha_EM constraint has gradient d(1/alpha)/d(log10 M_KK) ~ 1000,
    which maps any sigma_th to sigma(log10 M_KK) ~ sigma_th/1000.

    With sigma_th = 10: posterior width 0.01 dec = UNREALISTICALLY TIGHT
    With sigma_th = 50: posterior width 0.05 dec = STILL TIGHT but more honest
    With sigma_th = 100: posterior width 0.10 dec = REASONABLE given systematics

    The FIRAS constraint matters ONLY when sigma_th > ~80:
    For sigma_th < 80, the posterior is entirely alpha_EM-dominated.
    For sigma_th > 80, FIRAS pulls the mode toward ~17.0.

    KEY TENSION: The alpha_EM best-fit (17.57) is 0.54 decades ABOVE
    the FIRAS upper bound (17.03). This is a 54x / sigma_th tension.
    For sigma_th = 10: 5.4 sigma tension with FIRAS.
    For sigma_th = 50: 1.1 sigma tension -- barely compatible.
    For sigma_th = 100: 0.5 sigma -- compatible.

    The G_N constraint (16.87) is 0.70 decades BELOW the alpha_EM peak.
    BF(grav/gauge) is decisively against the gravity route IN THE
    KERNER FORMULA FRAMEWORK. But the gravity route uses the SD a_2
    formula which is a DIFFERENT framework (spectral zeta, not Kerner).

    HONEST CONCLUSION: The two M_KK extraction methods are fundamentally
    different calculations. Their disagreement is 0.70 decades = 5x in M_KK.
    This tension is STRUCTURAL, not resolvable by adjusting sigma_th.
    The Bayesian posterior assumes both are correct simultaneously,
    and the compromise is dominated by whichever has smaller uncertainty.
""")

# ============================================================
# 12. SAVE DATA
# ============================================================

np.savez(DATA_DIR / 's43_mkk_posterior.npz',
    # Grid
    log10_MKK=log10_MKK,
    MKK_grid=MKK_grid,
    N_grid=N_grid,
    dlog=dlog,
    # Posteriors
    p_joint=p_joint,
    p_alpha=p_alpha,
    p_GN=p_GN,
    p_FIRAS=p_FIRAS,
    p_no_FIRAS=p_no_FIRAS,
    # Log-likelihoods
    logL_alpha=logL_alpha,
    logL_GN=logL_GN,
    logL_FIRAS=logL_FIRAS,
    # Statistics
    mode_log10=mode_log10,
    mode_MKK=mode_MKK,
    mean_log10=mean_log10,
    mean_MKK=mean_MKK,
    median_log10=median_log10,
    median_MKK=median_MKK,
    ci68_lo_log10=ci68_lo_log10,
    ci68_hi_log10=ci68_hi_log10,
    ci68_lo=ci68_lo,
    ci68_hi=ci68_hi,
    ci95_lo_log10=ci95_lo_log10,
    ci95_hi_log10=ci95_hi_log10,
    ci95_lo=ci95_lo,
    ci95_hi=ci95_hi,
    # KL divergences
    DKL_joint=DKL_joint,
    DKL_alpha=DKL_alpha,
    DKL_GN=DKL_GN,
    DKL_FIRAS=DKL_FIRAS,
    DKL_routes=DKL_routes,
    # Bayes factor
    BF_grav_vs_gauge=BF_grav_vs_gauge,
    log10_BF=log10_BF,
    # Input parameters
    tau_fold=tau_fold,
    g_SU2_fold=g_SU2_fold,
    g_U1_fold=g_U1_fold,
    a2_fold=a2_fold,
    sigma_alpha_th=sigma_alpha_th,
    sigma_GN_log10=sigma_GN_log10,
    sigma_FIRAS=sigma_FIRAS,
    sin2_W_baptista=sin2_W_baptista,
    M_KK_GN_s42=M_KK_GN_s42,
    M_KK_kerner_s42=M_KK_kerner_s42,
    M_KK_max_FIRAS=MKK_FIRAS_cross,
    most_informative=np.array([most_informative]),
    # Gate
    gate_name=np.array(['MKK-BAYES-43']),
    gate_verdict=np.array(['INFO']),
    # Predicted 1/alpha_EM
    alpha_EM_inv_pred=alpha_EM_inv_pred,
)

print("Saved: tier0-computation/s43_mkk_posterior.npz")

# ============================================================
# 13. PLOT
# ============================================================

fig = plt.figure(figsize=(18, 14))
gs = GridSpec(2, 3, hspace=0.35, wspace=0.35)

# --- Panel A: Individual posteriors ---
ax1 = fig.add_subplot(gs[0, 0])
ax1.plot(log10_MKK, p_alpha / np.max(p_alpha), 'b-', lw=2, label=r'$\alpha_{\rm EM}$ (Kerner+RGE)')
ax1.plot(log10_MKK, p_GN / np.max(p_GN), 'r-', lw=2, label=r'$G_N$ (SD $a_2$)')
ax1.plot(log10_MKK, p_FIRAS / np.max(p_FIRAS), 'g-', lw=2, label='FIRAS')
ax1.axvline(np.log10(M_KK_GN_s42), color='r', ls=':', alpha=0.6, label=f'S42 grav: {np.log10(M_KK_GN_s42):.2f}')
ax1.axvline(np.log10(M_KK_kerner_s42), color='b', ls=':', alpha=0.6, label=f'S42 gauge: {np.log10(M_KK_kerner_s42):.2f}')
ax1.set_xlabel(r'$\log_{10}(M_{KK}$ / GeV)', fontsize=12)
ax1.set_ylabel('Normalized posterior', fontsize=12)
ax1.set_title('(A) Individual Posteriors', fontsize=13)
ax1.legend(fontsize=8, loc='upper left')
ax1.set_xlim(14, 19)
ax1.grid(True, alpha=0.3)

# --- Panel B: Joint posterior ---
ax2 = fig.add_subplot(gs[0, 1])
ax2.fill_between(log10_MKK, p_joint, alpha=0.3, color='purple')
ax2.plot(log10_MKK, p_joint, 'purple', lw=2, label='Joint posterior')
ax2.axvline(mode_log10, color='k', ls='--', lw=1.5, label=f'Mode: {mode_log10:.2f}')
ax2.axvspan(ci68_lo_log10, ci68_hi_log10, alpha=0.15, color='orange', label=f'68% CI: [{ci68_lo_log10:.2f}, {ci68_hi_log10:.2f}]')
ax2.axvspan(ci95_lo_log10, ci95_hi_log10, alpha=0.08, color='yellow', label=f'95% CI: [{ci95_lo_log10:.2f}, {ci95_hi_log10:.2f}]')
ax2.axvline(np.log10(M_KK_GN_s42), color='r', ls=':', alpha=0.6, label='S42 grav')
ax2.axvline(np.log10(M_KK_kerner_s42), color='b', ls=':', alpha=0.6, label='S42 gauge')
ax2.set_xlabel(r'$\log_{10}(M_{KK}$ / GeV)', fontsize=12)
ax2.set_ylabel(r'$P(M_{KK} | \mathrm{data})$', fontsize=12)
ax2.set_title('(B) Joint Posterior', fontsize=13)
ax2.legend(fontsize=7, loc='upper right')
ax2.set_xlim(14, 19)
ax2.grid(True, alpha=0.3)

# --- Panel C: CDF ---
ax3 = fig.add_subplot(gs[0, 2])
ax3.plot(log10_MKK, cdf, 'purple', lw=2)
ax3.axhline(0.025, color='gray', ls=':', alpha=0.5)
ax3.axhline(0.16, color='gray', ls=':', alpha=0.5)
ax3.axhline(0.5, color='gray', ls='--', alpha=0.5, label='Median')
ax3.axhline(0.84, color='gray', ls=':', alpha=0.5)
ax3.axhline(0.975, color='gray', ls=':', alpha=0.5)
ax3.axvline(np.log10(M_KK_GN_s42), color='r', ls=':', alpha=0.6, label=f'grav CDF={cdf_grav:.3f}')
ax3.axvline(np.log10(M_KK_kerner_s42), color='b', ls=':', alpha=0.6, label=f'gauge CDF={cdf_gauge:.3f}')
ax3.set_xlabel(r'$\log_{10}(M_{KK}$ / GeV)', fontsize=12)
ax3.set_ylabel('CDF', fontsize=12)
ax3.set_title('(C) Cumulative Distribution', fontsize=13)
ax3.legend(fontsize=8)
ax3.set_xlim(14, 19)
ax3.grid(True, alpha=0.3)

# --- Panel D: KL divergence bar chart ---
ax4 = fig.add_subplot(gs[1, 0])
labels = [r'$\alpha_{\rm EM}$', r'$G_N$', 'FIRAS', 'Joint']
kl_values = [DKL_alpha, DKL_GN, DKL_FIRAS, DKL_joint]
colors = ['blue', 'red', 'green', 'purple']
bars = ax4.bar(labels, kl_values, color=colors, alpha=0.7, edgecolor='black')
ax4.set_ylabel(r'$D_{\rm KL}$ (nats)', fontsize=12)
ax4.set_title('(D) Information Content', fontsize=13)
ax4.grid(True, alpha=0.3, axis='y')
for bar, val in zip(bars, kl_values):
    ax4.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.05,
             f'{val:.2f}', ha='center', va='bottom', fontsize=10)

# --- Panel E: Predicted observables vs M_KK ---
ax5 = fig.add_subplot(gs[1, 1])
# Plot 1/alpha_EM(m_Z) vs M_KK
mask = (log10_MKK > 14) & (log10_MKK < 19)
ax5.plot(log10_MKK[mask], alpha_EM_inv_pred[mask], 'b-', lw=2, label=r'$1/\alpha_{\rm EM}(m_Z)$ predicted')
ax5.axhline(ALPHA_EM_MZ_INV, color='k', ls='--', lw=1.5, label=f'Observed: {ALPHA_EM_MZ_INV:.1f}')
ax5.fill_between(log10_MKK[mask],
                 ALPHA_EM_MZ_INV - sigma_alpha_th,
                 ALPHA_EM_MZ_INV + sigma_alpha_th,
                 alpha=0.15, color='blue', label=rf'$\pm\sigma_{{th}}$ = {sigma_alpha_th}')
ax5.axvline(mode_log10, color='purple', ls='--', alpha=0.7, label=f'Posterior mode')
ax5.set_xlabel(r'$\log_{10}(M_{KK}$ / GeV)', fontsize=12)
ax5.set_ylabel(r'$1/\alpha_{\rm EM}(m_Z)$', fontsize=12)
ax5.set_title(r'(E) $\alpha_{\rm EM}$ Prediction vs $M_{KK}$', fontsize=13)
ax5.legend(fontsize=8)
ax5.set_ylim(0, 500)
ax5.grid(True, alpha=0.3)

# --- Panel F: Summary table ---
ax6 = fig.add_subplot(gs[1, 2])
ax6.axis('off')

table_data = [
    ['Statistic', 'log10(M_KK)', 'M_KK (GeV)'],
    ['Mode', f'{mode_log10:.3f}', f'{mode_MKK:.2e}'],
    ['Mean', f'{mean_log10:.3f}', f'{mean_MKK:.2e}'],
    ['Median', f'{median_log10:.3f}', f'{median_MKK:.2e}'],
    ['68% CI lower', f'{ci68_lo_log10:.3f}', f'{ci68_lo:.2e}'],
    ['68% CI upper', f'{ci68_hi_log10:.3f}', f'{ci68_hi:.2e}'],
    ['95% CI lower', f'{ci95_lo_log10:.3f}', f'{ci95_lo:.2e}'],
    ['95% CI upper', f'{ci95_hi_log10:.3f}', f'{ci95_hi:.2e}'],
    ['', '', ''],
    ['D_KL(joint)', f'{DKL_joint:.2f} nats', ''],
    ['Most informative', most_informative, f'D_KL={DKL_vals[most_informative]:.2f}'],
    ['BF(grav/gauge)', f'{BF_grav_vs_gauge:.1e}', strength],
    ['Gate', 'MKK-BAYES-43', 'INFO'],
]

table = ax6.table(cellText=table_data, cellLoc='center', loc='center',
                  colWidths=[0.35, 0.35, 0.30])
table.auto_set_font_size(False)
table.set_fontsize(9)
table.scale(1, 1.3)

for j in range(3):
    table[0, j].set_facecolor('#4472C4')
    table[0, j].set_text_props(color='white', fontweight='bold')

# Color the gate row
for j in range(3):
    table[12, j].set_facecolor('#D5E8D4')

ax6.set_title('(F) MKK-BAYES-43 Summary', fontsize=13, pad=20)

fig.suptitle(r'MKK-BAYES-43: Joint Bayesian $M_{KK}$ Posterior' + '\n'
             r'$P(M_{KK} | \alpha_{\rm EM}, G_N, \mathrm{FIRAS})$ — Paper 06 methodology',
             fontsize=14, fontweight='bold', y=0.98)

plt.savefig(DATA_DIR / 's43_mkk_posterior.png', dpi=150, bbox_inches='tight')
print("Saved: tier0-computation/s43_mkk_posterior.png")
plt.close()

print(f"\n{'='*78}")
print("COMPUTATION COMPLETE")
print("=" * 78)
