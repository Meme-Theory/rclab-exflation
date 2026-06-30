#!/usr/bin/env python3
"""
s68_beyond_mf_a4.py -- BEYOND-MF-A4-68
Gauge coupling implications of the 29.8% beyond-mean-field correction to a_4.

PHYSICAL CONTEXT
----------------
PROJECTED-MOMENTS-67 (s67_projected_moments.npz) found that the N=4 pair
projected moments give:
  delta_a2/a2 = 11.6%  (intermediate; intra-cell RG dominates)
  delta_a4/a4 = 29.8%  (large; inter-cell contributions significant)

FABRIC-PROJECTED-MOMENTS-67 showed the inter-cell coupling contributes
only 1.34% to a_2, so the 11.6% is purely intra-cell. However, the 29.8%
for a_4 may include both intra-cell and inter-cell.

The spectral action on M^4 x K yields:
  S = f_4*Lambda^4*a_0 + f_2*Lambda^2*a_2 + f_0*a_4 + ...

The a_4 coefficient determines:
  (1) Gauge couplings: 1/g_i^2 ~ f_0 * a_4^{sector_i}
  (2) Higgs quartic: lambda_h ~ a_4/a_2 (Gilkey ratio)
  (3) Weinberg angle at M_KK: sin^2(theta_W) = 3/(e^{4*tau} + 3) [metric, NOT a_4]

KEY SUBTLETY: The 29.8% correction modifies the TOTAL a_4 = sum_sectors a_4^{(p,q)}.
In the NCG spectral action, the gauge couplings at M_KK are:

  1/g_3^2(M_KK) = f_0/(2*pi^2) * a_4^{SU(3)}                     (1)
  1/g_2^2(M_KK) = f_0/(2*pi^2) * a_4^{SU(2)}                     (2)

The Weinberg angle sin^2(theta_W) depends on the METRIC (tau, sigma) via the
Killing form eigenvalues, NOT on a_4. So the 29.8% correction does NOT directly
shift sin^2(theta_W) at the fold. However, the running from M_KK to M_Z depends
on the coupling VALUES at M_KK, which ARE shifted by a_4. So the low-energy
sin^2(theta_W) receives an INDIRECT correction through RG running.

For the Higgs mass, the tree-level quartic coupling at M_KK is:
  lambda_CCM ~ f(n) * (a_4/a_2) * g^2

where f(n) = (n^2+3)/(n+3)^2 with n the neutrino Yukawa parameter.
The ratio a_4/a_2 shifts by:
  delta(a_4/a_2)/(a_4/a_2) = delta_a4/a4 - delta_a2/a2
                             = 0.298 - 0.116 = 0.182

This 18.2% increase in a_4/a_2 shifts the tree-level Higgs mass by sqrt(1.182).

METHOD
------
1. Load S67 projected-moment corrections and S66 KK threshold data.
2. Apply 29.8% a_4 correction to gauge couplings at M_KK.
3. Run one-loop SM RG from M_KK to M_Z.
4. Compare corrected vs uncorrected gauge couplings to observations.
5. Compute sin^2(theta_W) and m_H shifts.

Gate: BEYOND-MF-A4-68
  INFO: Report corrected gauge couplings, sin^2(theta_W), and m_H shift.

Author: gen-physicist
Session: S68 W3-C
"""

import sys
import os
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

from canonical_constants import (
    PI, M_KK, M_KK_gravity, M_KK_kerner,
    M_Pl_reduced, M_Z, M_W,
    alpha_em_MZ_inv, sin2_thetaW_MSbar, sin2_thetaW_fold,
    a0_fold, a2_fold, a4_fold,
    tau_fold, Vol_SU3_Haar,
    g_SU2_fold, g_U1_fold,
    alpha2_MKK_inv,
)

outdir = os.path.dirname(os.path.abspath(__file__))
t_start = time.time()

print("=" * 78)
print("BEYOND-MF-A4-68: Gauge Coupling Implications of 29.8% a_4 Correction")
print("gen-physicist | S68 W3-C")
print("=" * 78)

# =============================================================================
# 1. LOAD INPUT DATA
# =============================================================================
print("\n" + "=" * 78)
print("1. INPUT DATA")
print("=" * 78)

# S67 projected moments
d67 = np.load(os.path.join(outdir, 's67_projected_moments.npz'), allow_pickle=True)

# Extract the N=4 correction (fullest multi-pair result)
delta_a2_frac = float(d67['N4_delta_a2'])   # = 0.11588 ~ 11.6%
delta_a4_frac = float(d67['N4_delta_a4'])   # = 0.29760 ~ 29.8%
a2_bare = float(d67['a2_bare'])
a4_bare = float(d67['a4_bare'])
a2_bcs = float(d67['a2_bcs'])
a4_bcs = float(d67['a4_bcs'])

# S67 fabric projected moments
d67f = np.load(os.path.join(outdir, 's67_fabric_projected_moments.npz'), allow_pickle=True)
delta_a2_fabric = float(d67f['total_fabric_linear'])  # = 1.34%

# S66 KK threshold data
d66 = np.load(os.path.join(outdir, 's66_kk_threshold_l5.npz'), allow_pickle=True)
ratio_gilkey = float(d66['ratio_gilkey'])   # a_4/a_2 = 0.41396
mH_L6 = float(d66['mH_L6'])                # 131.8 GeV at L=6
mH_inf = float(d66['mH_inf'])              # 127.5 GeV (Aitken extrapolated)
g3_inv2_nominal = float(d66['g3_inv2_nominal'])  # 1/g_3^2 nominal at M_KK

print(f"\n  S67 Projected Moments (N=4 pairs):")
print(f"    delta_a2/a2 = {delta_a2_frac:.6f}  ({delta_a2_frac*100:.2f}%)")
print(f"    delta_a4/a4 = {delta_a4_frac:.6f}  ({delta_a4_frac*100:.2f}%)")
print(f"    a2_bare     = {a2_bare:.4f}")
print(f"    a4_bare     = {a4_bare:.4f}")
print(f"    a2_bcs      = {a2_bcs:.4f}")
print(f"    a4_bcs      = {a4_bcs:.4f}")

print(f"\n  S67 Fabric (inter-cell):")
print(f"    delta_a2_fabric = {delta_a2_fabric:.6f}  ({delta_a2_fabric*100:.4f}%)")

print(f"\n  Canonical Seeley-DeWitt at fold:")
print(f"    a_0 = {a0_fold:.1f}")
print(f"    a_2 = {a2_fold:.4f}")
print(f"    a_4 = {a4_fold:.4f}")
print(f"    a_4/a_2 (Gilkey ratio) = {ratio_gilkey:.6f}")

print(f"\n  S66 KK threshold results:")
print(f"    g_3^{{-2}} at M_KK = {g3_inv2_nominal:.6f}")
print(f"    m_H(L=6) = {mH_L6:.2f} GeV")
print(f"    m_H(inf)  = {mH_inf:.2f} GeV  (Aitken)")

# =============================================================================
# 2. CORRECTED SEELEY-DEWITT COEFFICIENTS
# =============================================================================
print("\n" + "=" * 78)
print("2. CORRECTED SEELEY-DEWITT COEFFICIENTS")
print("=" * 78)

# The BCS-dressed moments from N=4 exact diagonalization:
#   a_2^{dressed} = a_2^{bare} * (1 + delta_a2) = a_2_bare * 1.1159
#   a_4^{dressed} = a_4^{bare} * (1 + delta_a4) = a_4_bare * 1.2976
#
# But the CANONICAL a2_fold, a4_fold are the BARE (single-cell mean-field) values.
# The BCS corrections come from the many-body pairing, which shifts the
# spectral weight in the D_K eigenvalue distribution.

a2_corrected = a2_fold * (1.0 + delta_a2_frac)
a4_corrected = a4_fold * (1.0 + delta_a4_frac)
ratio_corrected = a4_corrected / a2_corrected

delta_ratio = (ratio_corrected - ratio_gilkey) / ratio_gilkey

print(f"\n  Bare (mean-field) values:")
print(f"    a_2 = {a2_fold:.4f}")
print(f"    a_4 = {a4_fold:.4f}")
print(f"    a_4/a_2 = {ratio_gilkey:.6f}")

print(f"\n  BCS-dressed values (N=4 projected moments):")
print(f"    a_2^{{dressed}} = {a2_corrected:.4f}  (x {1+delta_a2_frac:.4f})")
print(f"    a_4^{{dressed}} = {a4_corrected:.4f}  (x {1+delta_a4_frac:.4f})")
print(f"    (a_4/a_2)^{{dressed}} = {ratio_corrected:.6f}")
print(f"    delta(a_4/a_2)/(a_4/a_2) = {delta_ratio:.4f}  ({delta_ratio*100:.1f}%)")

# =============================================================================
# 3. GAUGE COUPLING SHIFT AT M_KK
# =============================================================================
print("\n" + "=" * 78)
print("3. GAUGE COUPLING SHIFT AT M_KK")
print("=" * 78)

# In the NCG spectral action, the gauge kinetic term is:
#
#   S_YM = (f_0 / (2*pi^2)) * integral_M (a_4^{gauge sector}) |F|^2 sqrt(g) d^4x
#
# Matching to (1/4g^2) integral |F|^2:
#   1/g_a^2 = (2*f_0 / pi^2) * a_4^{(a)}
#
# where a_4^{(a)} is the sector-a contribution to a_4.
#
# For SU(3)_c x SU(2)_L x U(1)_Y from the spectral triple M^4 x F x K:
# The gauge symmetry at the fold is SU(3)_color. The Weinberg angle determines
# the SU(2)_L x U(1)_Y decomposition at the fold via the metric.
#
# CRITICAL STRUCTURAL POINT:
# sin^2(theta_W) at M_KK = 3/(e^{4*tau} + 3) depends ONLY on the metric
# parameter tau, NOT on a_4. The BCS correction to a_4 does NOT change
# the metric — it changes the spectral weight while preserving the geometry.
#
# However, the ABSOLUTE values of g_1, g_2, g_3 at M_KK all scale with
# 1/sqrt(a_4). Since the correction is to the TOTAL a_4, all three gauge
# couplings receive the SAME fractional shift:
#
#   g_i^2 ~ 1/a_4  =>  delta(g_i^2)/g_i^2 = -delta(a_4)/a_4 = -0.298
#
# This is an OVERALL RESCALING. It does NOT change sin^2(theta_W) at M_KK.

# Current (bare) gauge couplings at M_KK
# From s55_theta_w_valley.py: sin^2(theta_W)(tau_fold) = 3/(e^{4*tau}+3)
sin2_W_fold = 3.0 / (np.exp(4.0 * tau_fold) + 3.0)

print(f"  sin^2(theta_W) at fold = {sin2_W_fold:.8f}")
print(f"  canonical value        = {sin2_thetaW_fold:.8f}")
print(f"  (This is metric-determined, INDEPENDENT of a_4)")

# Gauge couplings from canonical constants (Kerner route)
# g_SU2_fold = g_2^2 at fold = 2.0516
# g_U1_fold = g_1'^2 at fold = 4.387
# 1/alpha_2 = 47.856

g2_sq_bare = g_SU2_fold      # g_2^2 at M_KK (bare)
g1p_sq_bare = g_U1_fold      # g_1'^2 = (g'/sqrt(3/5))^2 at M_KK (bare)

# In GUT normalization: g_1 = sqrt(5/3) * g'
# sin^2(theta_W) = g'^2/(g'^2 + g_2^2) = g_1'^2/(g_1'^2 + g_2^2)
# at fold: 0.5839 = 4.387/(4.387 + 2.052)
sin2_check = g1p_sq_bare / (g1p_sq_bare + g2_sq_bare)
print(f"\n  sin^2(theta_W) from couplings = {sin2_check:.6f}")
print(f"  Consistency with metric formula: {np.isclose(sin2_check, sin2_W_fold, rtol=1e-3)}")

# The BCS correction rescales ALL couplings uniformly:
# 1/g_i^2 ~ a_4, so g_i^2 ~ 1/a_4
# If a_4 -> a_4*(1+0.298), then g_i^2 -> g_i^2 / (1+0.298)

rescale_factor = 1.0 / (1.0 + delta_a4_frac)  # = 1/1.298 = 0.770

g2_sq_dressed = g2_sq_bare * rescale_factor
g1p_sq_dressed = g1p_sq_bare * rescale_factor
g3_sq_dressed = (1.0 / g3_inv2_nominal) * rescale_factor

# alpha_i = g_i^2 / (4*pi)
alpha2_MKK_bare = g2_sq_bare / (4.0 * PI)
alpha2_MKK_dressed = g2_sq_dressed / (4.0 * PI)
alpha1_MKK_bare = g1p_sq_bare / (4.0 * PI)
alpha1_MKK_dressed = g1p_sq_dressed / (4.0 * PI)
alpha3_MKK_bare = (1.0 / g3_inv2_nominal) / (4.0 * PI)
alpha3_MKK_dressed = g3_sq_dressed / (4.0 * PI)

print(f"\n  Gauge couplings at M_KK:")
print(f"  {'':>15s} {'bare':>12s} {'dressed':>12s} {'shift':>10s}")
print(f"  {'g_2^2':>15s} {g2_sq_bare:12.6f} {g2_sq_dressed:12.6f} {(g2_sq_dressed/g2_sq_bare-1)*100:+9.2f}%")
print(f"  {'g_1^2':>15s} {g1p_sq_bare:12.6f} {g1p_sq_dressed:12.6f} {(g1p_sq_dressed/g1p_sq_bare-1)*100:+9.2f}%")
print(f"  {'g_3^2':>15s} {1.0/g3_inv2_nominal:12.6f} {g3_sq_dressed:12.6f} {(g3_sq_dressed*g3_inv2_nominal-1)*100:+9.2f}%")
print(f"  {'1/alpha_2':>15s} {1.0/alpha2_MKK_bare:12.4f} {1.0/alpha2_MKK_dressed:12.4f}")
print(f"  {'1/alpha_3':>15s} {1.0/alpha3_MKK_bare:12.4f} {1.0/alpha3_MKK_dressed:12.4f}")

# sin^2(theta_W) at M_KK: UNCHANGED by uniform rescaling
sin2_fold_dressed = g1p_sq_dressed / (g1p_sq_dressed + g2_sq_dressed)
print(f"\n  sin^2(theta_W) at M_KK:")
print(f"    bare    = {sin2_check:.8f}")
print(f"    dressed = {sin2_fold_dressed:.8f}")
print(f"    shift   = {(sin2_fold_dressed - sin2_check):.2e}  (zero by construction)")

# =============================================================================
# 4. RG RUNNING FROM M_KK TO M_Z
# =============================================================================
print("\n" + "=" * 78)
print("4. RG RUNNING FROM M_KK TO M_Z")
print("=" * 78)

# Standard one-loop SM RG equations
def sm_rge(t, y):
    """One-loop SM RGEs. t = log(mu/M_Z), y = (g1, g2, g3, yt, lam).
    g1 is in GUT normalization: g1 = sqrt(5/3) * g'.
    """
    g1, g2, g3, yt, lam = y
    b = 16.0 * PI**2

    dg1 = (41.0 / 10.0) * g1**3 / b
    dg2 = -(19.0 / 6.0) * g2**3 / b
    dg3 = -7.0 * g3**3 / b

    dyt = yt * (9.0/2.0 * yt**2 - 17.0/12.0 * g1**2
                - 9.0/4.0 * g2**2 - 8.0 * g3**2) / b

    dlam = (24.0*lam**2
            - (9.0/5.0*g1**2 + 9.0*g2**2)*lam
            + 9.0/200.0*(3.0*g1**4 + 2.0*g1**2*g2**2 + g2**4)
            + 12.0*yt**2*lam - 12.0*yt**4) / b

    return [dg1, dg2, dg3, dyt, dlam]

# Observed values at M_Z
# v_ew = 246.0       # GeV  # S72: now imported from canonical_constants
# m_H_obs = 125.1    # GeV  # S72: now imported from canonical_constants
# m_t_obs = 172.69   # GeV (PDG 2024)  # S72: now imported as m_t_pole from canonical_constants
m_t_obs = m_t_pole  # S72: alias for downstream use
# alpha_s_MZ = 0.1180  # S72: now imported as alpha_s_MZ_obs from canonical_constants
alpha_s_MZ = alpha_s_MZ_obs  # S72: alias for downstream use
alpha_em = 1.0 / alpha_em_MZ_inv

# Observed couplings at M_Z
g3_MZ_obs = np.sqrt(4 * PI * alpha_s_MZ)    # = 1.2177
g2_MZ_obs = np.sqrt(4 * PI * alpha_em / sin2_thetaW_MSbar)  # = 0.6519
g1_MZ_obs = np.sqrt(5.0/3.0) * np.sqrt(4 * PI * alpha_em / (1.0 - sin2_thetaW_MSbar))  # = 0.4614 (GUT norm)
yt_MZ_obs = np.sqrt(2) * m_t_obs / v_ew     # = 0.993
lambda_MZ_obs = m_H_obs**2 / (2.0 * v_ew**2)  # = 0.1293

alpha_1_MZ_obs = g1_MZ_obs**2 / (4.0 * PI)
alpha_2_MZ_obs = g2_MZ_obs**2 / (4.0 * PI)
alpha_3_MZ_obs = alpha_s_MZ

print(f"\n  Observed at M_Z (PDG 2024):")
print(f"    alpha_1(M_Z) = {alpha_1_MZ_obs:.6f}  [1/alpha_1 = {1.0/alpha_1_MZ_obs:.2f}]")
print(f"    alpha_2(M_Z) = {alpha_2_MZ_obs:.6f}  [1/alpha_2 = {1.0/alpha_2_MZ_obs:.2f}]")
print(f"    alpha_3(M_Z) = {alpha_3_MZ_obs:.6f}  [1/alpha_3 = {1.0/alpha_3_MZ_obs:.2f}]")
print(f"    sin^2(theta_W) = {sin2_thetaW_MSbar}")

# Strategy: Run FROM M_Z UPWARD to M_KK using observed initial conditions.
# Then compare the SM RG-evolved couplings at M_KK to our framework predictions.
# This avoids the numerical instability of downward running.

t_MKK = np.log(M_KK_gravity / M_Z)  # = ln(7.43e16/91.19) = 34.33
t_eval = np.linspace(0, t_MKK, 5000)

y0_MZ = [g1_MZ_obs, g2_MZ_obs, g3_MZ_obs, yt_MZ_obs, lambda_MZ_obs]

sol_up = solve_ivp(sm_rge, [0, t_MKK], y0_MZ,
                    t_eval=t_eval,
                    method='RK45', rtol=1e-10, atol=1e-12)

print(f"\n  RG running: M_Z -> M_KK")
print(f"    t_MKK = ln(M_KK/M_Z) = {t_MKK:.4f}")
print(f"    M_KK (gravity) = {M_KK_gravity:.4e} GeV")

# Extract SM-running couplings at M_KK
g1_SM_at_MKK = sol_up.y[0, -1]
g2_SM_at_MKK = sol_up.y[1, -1]
g3_SM_at_MKK = sol_up.y[2, -1]
yt_SM_at_MKK = sol_up.y[3, -1]
lam_SM_at_MKK = sol_up.y[4, -1]

alpha1_SM_MKK = g1_SM_at_MKK**2 / (4.0 * PI)
alpha2_SM_MKK = g2_SM_at_MKK**2 / (4.0 * PI)
alpha3_SM_MKK = g3_SM_at_MKK**2 / (4.0 * PI)

print(f"\n  SM RG at M_KK (from observed M_Z values):")
print(f"    g_1 = {g1_SM_at_MKK:.6f}   [1/alpha_1 = {1.0/alpha1_SM_MKK:.2f}]")
print(f"    g_2 = {g2_SM_at_MKK:.6f}   [1/alpha_2 = {1.0/alpha2_SM_MKK:.2f}]")
print(f"    g_3 = {g3_SM_at_MKK:.6f}   [1/alpha_3 = {1.0/alpha3_SM_MKK:.2f}]")
print(f"    sin^2(theta_W)_SM = {g1_SM_at_MKK**2 * 3.0/5.0 / (g1_SM_at_MKK**2 * 3.0/5.0 + g2_SM_at_MKK**2):.6f}")

# =============================================================================
# 5. GAUGE COUPLING PROPAGATION: M_KK -> M_Z
# =============================================================================
print("\n" + "=" * 78)
print("5. GAUGE COUPLING PROPAGATION: STRUCTURAL ANALYSIS")
print("=" * 78)

# CRITICAL STRUCTURAL POINT:
# The framework's gauge couplings at M_KK (Kerner route, g_3^{-2}=3.755)
# differ from the SM RG extrapolation (1/alpha_3^{SM}(M_KK) ~ 47) by a
# factor ~12. This gap is bridged by KK threshold corrections from the
# Peter-Weyl tower (S64/S66 computations).
#
# The BCS correction modifies the D_K spectral weight, which affects BOTH:
#   (a) The leading-order gauge couplings (g_i^2 ~ 1/a_4)
#   (b) The KK threshold corrections (which depend on the eigenvalue spectrum)
#
# Computing the full dressed threshold program requires rerunning the
# entire S64/S66 computation with dressed occupation numbers. This is
# beyond the scope of this single-gate computation.
#
# WHAT WE CAN COMPUTE:
# 1. The fractional shift at M_KK (uniform -22.9%)
# 2. The propagation assuming the threshold corrections are unchanged
#    (first-order approximation: BCS shifts the boundary, thresholds are
#    computed from the bare spectrum which is not substantially modified)
# 3. The Higgs mass, which depends only on a_4/a_2 (no threshold issue)

b_1 = 41.0 / 10.0
b_2 = -19.0 / 6.0
b_3 = -7.0  # (local)

ln_ratio = np.log(M_KK_gravity / M_Z)  # = 34.33

# SM RG contribution (the logarithmic piece)
rg_contrib_1 = b_1 / (2.0 * PI) * ln_ratio
rg_contrib_2 = b_2 / (2.0 * PI) * ln_ratio
rg_contrib_3 = b_3 / (2.0 * PI) * ln_ratio

print(f"\n  One-loop beta coefficients & RG logarithms:")
print(f"    b_1 = {b_1:.4f},  delta(1/alpha_1) = {rg_contrib_1:+.2f}")
print(f"    b_2 = {b_2:.4f},  delta(1/alpha_2) = {rg_contrib_2:+.2f}")
print(f"    b_3 = {b_3:.4f},  delta(1/alpha_3) = {rg_contrib_3:+.2f}")
print(f"    ln(M_KK/M_Z) = {ln_ratio:.4f}")

# Use the FRAMEWORK coupling at M_KK (Kerner route) as the UV boundary
alpha_1_MZ_obs = g1_MZ_obs**2 / (4.0 * PI)
alpha_2_MZ_obs = g2_MZ_obs**2 / (4.0 * PI)
alpha_3_MZ_obs = alpha_s_MZ

# Framework's bare 1/alpha_i at M_KK (from spectral action Kerner normalization)
inv_a3_MKK_fw = g3_inv2_nominal  # = 3.755 (from S66)
inv_a2_MKK_fw = 1.0 / alpha2_MKK_bare  # from Section 3 (~ 6.13)
inv_a1_MKK_fw = 1.0 / alpha1_MKK_bare  # from Section 3 (~ 1.72)

# BCS shift at M_KK: delta(1/alpha_i) = delta_a4 * (1/alpha_i)_{bare}
delta_inv_a1_MKK = delta_a4_frac * inv_a1_MKK_fw
delta_inv_a2_MKK = delta_a4_frac * inv_a2_MKK_fw
delta_inv_a3_MKK = delta_a4_frac * inv_a3_MKK_fw

print(f"\n  Framework couplings at M_KK (Kerner route):")
print(f"    1/alpha_1 = {inv_a1_MKK_fw:.4f} (bare)  ->  {inv_a1_MKK_fw + delta_inv_a1_MKK:.4f} (dressed)")
print(f"    1/alpha_2 = {inv_a2_MKK_fw:.4f} (bare)  ->  {inv_a2_MKK_fw + delta_inv_a2_MKK:.4f} (dressed)")
print(f"    1/alpha_3 = {inv_a3_MKK_fw:.4f} (bare)  ->  {inv_a3_MKK_fw + delta_inv_a3_MKK:.4f} (dressed)")
print(f"    BCS shift delta(1/alpha_3) = {delta_inv_a3_MKK:+.4f}")

# Running to M_Z (FRAMEWORK route = Kerner coupling + SM running below M_KK)
# This does NOT include KK threshold corrections (which are separate)
inv_a1_MZ_fw_bare = inv_a1_MKK_fw + rg_contrib_1
inv_a2_MZ_fw_bare = inv_a2_MKK_fw + rg_contrib_2
inv_a3_MZ_fw_bare = inv_a3_MKK_fw + rg_contrib_3

inv_a1_MZ_fw_dressed = inv_a1_MZ_fw_bare + delta_inv_a1_MKK
inv_a2_MZ_fw_dressed = inv_a2_MZ_fw_bare + delta_inv_a2_MKK
inv_a3_MZ_fw_dressed = inv_a3_MZ_fw_bare + delta_inv_a3_MKK

# Note: these are WITHOUT KK thresholds. The actual predictions differ.
print(f"\n  Running to M_Z (no KK thresholds -- for SHIFT analysis only):")
print(f"  {'':>15s} {'bare':>10s} {'dressed':>10s} {'shift':>10s} {'observed':>10s}")
print(f"  {'1/alpha_1':>15s} {inv_a1_MZ_fw_bare:10.2f} {inv_a1_MZ_fw_dressed:10.2f} {delta_inv_a1_MKK:+10.4f} {1.0/alpha_1_MZ_obs:10.2f}")
print(f"  {'1/alpha_2':>15s} {inv_a2_MZ_fw_bare:10.2f} {inv_a2_MZ_fw_dressed:10.2f} {delta_inv_a2_MKK:+10.4f} {1.0/alpha_2_MZ_obs:10.2f}")
print(f"  {'1/alpha_3':>15s} {inv_a3_MZ_fw_bare:10.2f} {inv_a3_MZ_fw_dressed:10.2f} {delta_inv_a3_MKK:+10.4f} {1.0/alpha_3_MZ_obs:10.2f}")

# The RG-diluted fractional shift at M_Z
# delta(alpha_i(M_Z))/alpha_i(M_Z) = delta(1/alpha_i) / (1/alpha_i(M_Z))
# Using the OBSERVED 1/alpha_i(M_Z) as the denominator:
frac_shift_a1_MZ = delta_inv_a1_MKK / (1.0/alpha_1_MZ_obs)
frac_shift_a2_MZ = delta_inv_a2_MKK / (1.0/alpha_2_MZ_obs)
frac_shift_a3_MZ = delta_inv_a3_MKK / (1.0/alpha_3_MZ_obs)

print(f"\n  RG-diluted fractional shifts at M_Z (relative to observed):")
print(f"    delta(1/alpha_1)/obs = {frac_shift_a1_MZ*100:+.2f}%  ({delta_inv_a1_MKK:+.3f} out of {1.0/alpha_1_MZ_obs:.1f})")
print(f"    delta(1/alpha_2)/obs = {frac_shift_a2_MZ*100:+.2f}%  ({delta_inv_a2_MKK:+.3f} out of {1.0/alpha_2_MZ_obs:.1f})")
print(f"    delta(1/alpha_3)/obs = {frac_shift_a3_MZ*100:+.2f}%  ({delta_inv_a3_MKK:+.3f} out of {1.0/alpha_3_MZ_obs:.1f})")

# sin^2(theta_W) shift at M_Z from the BCS correction
# Use the observed values + perturbative shift
inv_a1_MZ_perturbed = 1.0/alpha_1_MZ_obs + delta_inv_a1_MKK
inv_a2_MZ_perturbed = 1.0/alpha_2_MZ_obs + delta_inv_a2_MKK
alpha1_perturbed = 1.0 / inv_a1_MZ_perturbed
alpha2_perturbed = 1.0 / inv_a2_MZ_perturbed

sin2_fw_MZ_bare = sin2_thetaW_MSbar
sin2_fw_MZ_dressed = ((3.0/5.0)*alpha1_perturbed /
                      ((3.0/5.0)*alpha1_perturbed + alpha2_perturbed))
delta_sin2 = sin2_fw_MZ_dressed - sin2_fw_MZ_bare

alpha3_fw_MZ_dressed = 1.0 / (1.0/alpha_3_MZ_obs + delta_inv_a3_MKK)

# Variables for the plot (BCS shift at M_Z, using OBSERVED as baseline)
delta_inv_a1_MZ = delta_inv_a1_MKK
delta_inv_a2_MZ = delta_inv_a2_MKK
delta_inv_a3_MZ = delta_inv_a3_MKK

print(f"\n  sin^2(theta_W) at M_Z:")
print(f"    bare (observed):  {sin2_thetaW_MSbar:.6f}")
print(f"    + BCS correction: {sin2_fw_MZ_dressed:.6f}")
print(f"    shift:            {delta_sin2:+.6f}  ({delta_sin2/sin2_thetaW_MSbar*100:+.3f}%)")
print(f"\n  alpha_s(M_Z):")
print(f"    bare (observed):  {alpha_s_MZ:.6f}")
print(f"    + BCS correction: {alpha3_fw_MZ_dressed:.6f}")
print(f"    shift:            {(alpha3_fw_MZ_dressed - alpha_s_MZ):+.6f}")
print(f"\n  NOTE: The framework coupling at M_KK (g_3^{{-2}} = {g3_inv2_nominal:.2f})")
print(f"  is ~12x smaller than SM extrapolation (1/alpha_3^SM = {1.0/alpha3_SM_MKK:.1f}).")
print(f"  The gap is filled by KK threshold corrections (S66).")
print(f"  The BCS shift delta(1/alpha_3) = {delta_inv_a3_MKK:.3f} is therefore a")
print(f"  {delta_inv_a3_MKK/inv_a3_MKK_fw*100:.0f}% correction TO the UV boundary condition,")
print(f"  propagating to a {frac_shift_a3_MZ*100:.1f}% fractional shift at M_Z.")
print(f"  This is MODEST because the RG running from M_KK to M_Z ({abs(rg_contrib_3):.1f})")
print(f"  dominates over the UV boundary condition ({inv_a3_MKK_fw:.2f}).")

# =============================================================================
# 6. HIGGS MASS SHIFT
# =============================================================================
print("\n" + "=" * 78)
print("6. HIGGS MASS SHIFT FROM a_4/a_2 CORRECTION")
print("=" * 78)

# The tree-level Higgs quartic at M_KK from CCM spectral action:
#   lambda_h(M_KK) = f(n) * (a_4/a_2) * g^2 * (normalization)
#
# The Higgs mass scales as:
#   m_H^2 ~ lambda * v^2 ~ (a_4/a_2)
#
# So:
#   delta(m_H)/m_H = (1/2) * delta(a_4/a_2)/(a_4/a_2)
#
# TWO RATIOS IN PLAY:
#   PW spectral sum ratio: a4_fold/a2_fold = 0.487 (S42 canonical constants)
#   Gilkey geometric ratio: 0.414 (S61 heat kernel computation)
#
# The S66 Higgs mass computation uses the Gilkey ratio. The S67 BCS correction
# is a FRACTIONAL shift of the PW spectral weight. By A4-TRACE-60 (N_factor
# is the same for a_2 and a_4, ~16), the fractional shift in a_4/a_2 is the
# same for both the PW and Gilkey measures:
#
#   delta(a_4/a_2)/(a_4/a_2) = delta_a4/a4 - delta_a2/a2  (to leading order)
#                             = 0.298 - 0.116 = 0.182
#
# More precisely (ratio of (1+delta)):
frac_shift_ratio = (1.0 + delta_a4_frac) / (1.0 + delta_a2_frac) - 1.0

# Report both PW and Gilkey
ratio_PW_bare = a4_fold / a2_fold
ratio_PW_dressed = ratio_PW_bare * (1.0 + frac_shift_ratio)
ratio_gilkey_dressed = ratio_gilkey * (1.0 + frac_shift_ratio)

# m_H scales as sqrt(ratio):
frac_shift_mH = np.sqrt(1.0 + frac_shift_ratio) - 1.0

print(f"\n  Gilkey ratio (a_4/a_2) [used for Higgs mass]:")
print(f"    bare    = {ratio_gilkey:.6f}")
print(f"    dressed = {ratio_gilkey_dressed:.6f}")
print(f"    shift   = {frac_shift_ratio*100:+.2f}%")
print(f"\n  PW spectral ratio (a_4/a_2) [for reference]:")
print(f"    bare    = {ratio_PW_bare:.6f}")
print(f"    dressed = {ratio_PW_dressed:.6f}")
print(f"    shift   = {frac_shift_ratio*100:+.2f}%  (same fractional shift)")

print(f"\n  Higgs mass prediction:")
print(f"    m_H ~ sqrt(a_4/a_2) => delta(m_H)/m_H = {frac_shift_mH*100:+.2f}%")

# Apply to the S66 KK-threshold corrected Higgs masses
# The S66 values already use the Gilkey ratio. The BCS dressing
# multiplies the effective ratio by (1 + frac_shift_ratio).
mH_L6_dressed = mH_L6 * np.sqrt(1.0 + frac_shift_ratio)
mH_inf_dressed = mH_inf * np.sqrt(1.0 + frac_shift_ratio)

print(f"\n  S66 Higgs mass predictions:")
print(f"  {'':>20s} {'bare':>10s} {'dressed':>10s} {'shift':>10s} {'obs':>10s}")
print(f"  {'m_H (L=6)':>20s} {mH_L6:10.2f} {mH_L6_dressed:10.2f} {mH_L6_dressed-mH_L6:+10.2f} {m_H_obs:10.2f}")
print(f"  {'m_H (Aitken)':>20s} {mH_inf:10.2f} {mH_inf_dressed:10.2f} {mH_inf_dressed-mH_inf:+10.2f} {m_H_obs:10.2f}")

# Deviation from observed
dev_L6_bare = (mH_L6 - m_H_obs) / m_H_obs * 100
dev_L6_dressed = (mH_L6_dressed - m_H_obs) / m_H_obs * 100
dev_inf_bare = (mH_inf - m_H_obs) / m_H_obs * 100
dev_inf_dressed = (mH_inf_dressed - m_H_obs) / m_H_obs * 100

print(f"\n  Deviation from observed m_H = {m_H_obs} GeV:")
print(f"    m_H(L=6) bare:    {dev_L6_bare:+.1f}%")
print(f"    m_H(L=6) dressed: {dev_L6_dressed:+.1f}%")
print(f"    m_H(inf) bare:    {dev_inf_bare:+.1f}%")
print(f"    m_H(inf) dressed: {dev_inf_dressed:+.1f}%")

# =============================================================================
# 7. SENSITIVITY ANALYSIS: NON-UNIFORM CORRECTION
# =============================================================================
print("\n" + "=" * 78)
print("7. SENSITIVITY: NON-UNIFORM SECTOR CORRECTION")
print("=" * 78)

# The above assumes the 29.8% correction applies UNIFORMLY to all PW sectors
# of a_4. In reality, different sectors (p,q) may receive different corrections
# depending on their BCS occupation numbers. The N=4 projected moment correction
# comes from the full 8-mode BCS Fock space, which is dominated by B2 modes.
#
# If the correction is concentrated in specific sectors:
#   - SU(3)_c sector: (p,q) != (0,0) -- most of a_4 comes from higher reps
#   - Singlet sector (0,0): contributes ~1/16 of total (trace factor 16)
#
# The A4-TRACE-60 result showed N_factor_a4 ~ N_factor_a2 ~ 16, confirming
# uniform scaling. So the uniform correction is structurally supported.
#
# Nevertheless, parametrize non-uniformity via epsilon:
#   delta(1/alpha_2) at M_KK gets extra +epsilon
#   delta(1/alpha_1) at M_KK gets extra -epsilon (compensating)
#   so the total weighted average stays at 0.298

epsilons = np.linspace(-0.15, 0.15, 31)
sin2_MZ_vs_eps = []

for eps_nu in epsilons:
    # Non-uniform: SU(2) sector gets extra +epsilon, U(1) gets -epsilon
    # Applied to the framework couplings at M_KK, then propagated to M_Z
    delta_1 = (delta_a4_frac - eps_nu) * inv_a1_MKK_fw  # U(1) gets less
    delta_2 = (delta_a4_frac + eps_nu) * inv_a2_MKK_fw  # SU(2) gets more

    inv_a1_MZ_nu = 1.0/alpha_1_MZ_obs + delta_1
    inv_a2_MZ_nu = 1.0/alpha_2_MZ_obs + delta_2

    alpha1_MZ_nu = 1.0 / inv_a1_MZ_nu
    alpha2_MZ_nu = 1.0 / inv_a2_MZ_nu

    sin2_nu = (3.0/5.0)*alpha1_MZ_nu / ((3.0/5.0)*alpha1_MZ_nu + alpha2_MZ_nu)
    sin2_MZ_vs_eps.append(sin2_nu)

sin2_MZ_vs_eps = np.array(sin2_MZ_vs_eps)

# Find epsilon that gives best match to observed sin^2
idx_best = np.argmin(np.abs(sin2_MZ_vs_eps - sin2_thetaW_MSbar))
eps_best = epsilons[idx_best]
sin2_best = sin2_MZ_vs_eps[idx_best]

print(f"  Non-uniform correction sensitivity (epsilon shifts SU(2) vs U(1)):")
print(f"  {'epsilon':>10s} {'sin^2(M_Z)':>12s} {'dev from obs':>14s}")
for i in [0, len(epsilons)//4, len(epsilons)//2, 3*len(epsilons)//4, -1]:
    dev = (sin2_MZ_vs_eps[i] - sin2_thetaW_MSbar) / sin2_thetaW_MSbar * 100
    print(f"  {epsilons[i]:+10.4f} {sin2_MZ_vs_eps[i]:12.6f} {dev:+13.2f}%")

print(f"\n  Best-fit epsilon = {eps_best:+.4f}")
print(f"  sin^2(theta_W)_best = {sin2_best:.6f} (obs: {sin2_thetaW_MSbar})")
print(f"  Deviation: {(sin2_best - sin2_thetaW_MSbar)/sin2_thetaW_MSbar*100:+.3f}%")
print(f"\n  STRUCTURAL CONCLUSION: Non-uniform corrections at the 15% level")
print(f"  shift sin^2(theta_W) by O({abs(sin2_MZ_vs_eps[0] - sin2_MZ_vs_eps[-1]):.4f}).")

# =============================================================================
# 8. ALPHA_S SHIFT AND STRONG COUPLING CHECK
# =============================================================================
print("\n" + "=" * 78)
print("8. STRONG COUPLING alpha_s(M_Z) CHECK")
print("=" * 78)

# The strong coupling is the most precisely constrained gauge coupling.
# alpha_s(M_Z) = 0.1180 +/- 0.0009
#
# In the relative-shift method, the dressed alpha_s at M_Z is:

sigma_alpha_s = 0.0009  # (local)

delta_alpha_s = alpha3_fw_MZ_dressed - alpha_3_MZ_obs
pull = delta_alpha_s / sigma_alpha_s
print(f"  alpha_s(M_Z) shift from BCS dressing:")
print(f"    bare (=observed): {alpha_3_MZ_obs:.6f}")
print(f"    dressed:          {alpha3_fw_MZ_dressed:.6f}")
print(f"    shift:            {delta_alpha_s:+.6f}")
print(f"    observed:         {alpha_s_MZ:.4f} +/- {sigma_alpha_s}")
print(f"    Pull: {pull:+.2f} sigma")
print(f"\n  The BCS correction increases 1/alpha_3 at M_KK by {delta_inv_a3_MKK:+.3f}")
print(f"  (a {frac_shift_a3_MZ*100:+.1f}% shift relative to 1/alpha_3(M_Z) = {1.0/alpha_3_MZ_obs:.2f}).")
print(f"  |delta alpha_s| = {abs(delta_alpha_s):.4f}, a {abs(pull):.1f}-sigma effect.")

# =============================================================================
# 9. SUMMARY TABLE AND GATE VERDICT
# =============================================================================
print("\n" + "=" * 78)
print("9. SUMMARY AND GATE VERDICT")
print("=" * 78)

print(f"\n  SUMMARY TABLE:")
print(f"  ┌───────────────────────────────────────────────────────────────────────┐")
print(f"  │  BEYOND-MF-A4-68: Impact of 29.8% BCS Correction to a_4             │")
print(f"  ├───────────────────────────────────────────────────────────────────────┤")
print(f"  │  Input: delta_a4/a4 = {delta_a4_frac*100:.1f}%,  delta_a2/a2 = {delta_a2_frac*100:.1f}%               │")
print(f"  │                                                                       │")
print(f"  │  1. sin^2(theta_W) at fold: {sin2_W_fold:.6f} (metric, UNCHANGED)          │")
print(f"  │     (BCS does not deform the Jensen metric)                           │")
print(f"  │                                                                       │")
print(f"  │  2. g_i^2 at M_KK: all shift by {(rescale_factor-1)*100:+.1f}% (uniform)               │")
print(f"  │                                                                       │")
print(f"  │  3. sin^2(theta_W) at M_Z: {sin2_fw_MZ_dressed:.6f}                             │")
print(f"  │     shift from BCS: {delta_sin2:+.6f} ({delta_sin2/sin2_thetaW_MSbar*100:+.4f}%)                    │")
print(f"  │                                                                       │")
print(f"  │  4. Gilkey ratio: {ratio_gilkey:.6f} -> {ratio_gilkey_dressed:.6f} (+{frac_shift_ratio*100:.1f}%)              │")
print(f"  │     m_H(L=6): {mH_L6:.1f} -> {mH_L6_dressed:.1f} GeV  (obs: {m_H_obs} GeV)              │")
print(f"  │     m_H(Aitken): {mH_inf:.1f} -> {mH_inf_dressed:.1f} GeV  ({mH_inf_dressed-mH_inf:+.1f} GeV)              │")
print(f"  │                                                                       │")
print(f"  │  5. alpha_s(M_Z): {alpha3_fw_MZ_dressed:.6f}  (obs: {alpha_s_MZ})                     │")
print(f"  └───────────────────────────────────────────────────────────────────────┘")

print(f"\n  Gate BEYOND-MF-A4-68: INFO")
print(f"    The 29.8% BCS correction to a_4 produces a UNIFORM {abs(rescale_factor-1)*100:.0f}% decrease")
print(f"    in all g_i^2 at M_KK. Via relative-shift analysis at M_Z:")
print(f"    - sin^2(theta_W) shift: {delta_sin2:+.6f} ({delta_sin2/sin2_thetaW_MSbar*100:+.4f}%)")
print(f"    - Higgs mass shift: {frac_shift_mH*100:+.1f}% ({mH_inf_dressed-mH_inf:+.1f} GeV at Aitken level)")
print(f"    - BCS dressing pushes m_H AWAY from observation (larger, not closer)")
print(f"    - The a_4/a_2 correction is only +{frac_shift_ratio*100:.1f}% (partial cancellation")
print(f"      from the 11.6% a_2 correction). The Higgs mass is protected by")
print(f"      the ratio structure of the spectral action.")

# =============================================================================
# 10. SAVE DATA
# =============================================================================
print("\n" + "=" * 78)
print("10. SAVING OUTPUT")
print("=" * 78)

out_path = os.path.join(outdir, 's68_beyond_mf_a4.npz')
np.savez(out_path,
    # Input
    delta_a2_frac=delta_a2_frac,
    delta_a4_frac=delta_a4_frac,
    delta_a2_fabric=delta_a2_fabric,
    a2_fold=a2_fold,
    a4_fold=a4_fold,
    ratio_gilkey=ratio_gilkey,
    # Corrected coefficients
    a2_corrected=a2_corrected,
    a4_corrected=a4_corrected,
    ratio_gilkey_dressed=ratio_gilkey_dressed,
    ratio_PW_dressed=ratio_PW_dressed,
    frac_shift_ratio=frac_shift_ratio,
    # Gauge couplings at M_KK
    g2_sq_bare=g2_sq_bare,
    g2_sq_dressed=g2_sq_dressed,
    g1p_sq_bare=g1p_sq_bare,
    g1p_sq_dressed=g1p_sq_dressed,
    g3_sq_dressed=g3_sq_dressed,
    rescale_factor=rescale_factor,
    # Framework couplings at M_KK (Kerner route)
    inv_a1_MKK_fw=inv_a1_MKK_fw,
    inv_a2_MKK_fw=inv_a2_MKK_fw,
    inv_a3_MKK_fw=inv_a3_MKK_fw,
    delta_inv_a1_MKK=delta_inv_a1_MKK,
    delta_inv_a2_MKK=delta_inv_a2_MKK,
    delta_inv_a3_MKK=delta_inv_a3_MKK,
    # RG-diluted shifts at M_Z
    frac_shift_a1_MZ=frac_shift_a1_MZ,
    frac_shift_a2_MZ=frac_shift_a2_MZ,
    frac_shift_a3_MZ=frac_shift_a3_MZ,
    alpha3_dressed_MZ=alpha3_fw_MZ_dressed,
    delta_alpha_s=delta_alpha_s,
    # sin^2(theta_W)
    sin2_fold=sin2_W_fold,
    sin2_fw_MZ_bare=sin2_fw_MZ_bare,
    sin2_fw_MZ_dressed=sin2_fw_MZ_dressed,
    delta_sin2=delta_sin2,
    # Higgs mass
    mH_L6_bare=mH_L6,
    mH_L6_dressed=mH_L6_dressed,
    mH_inf_bare=mH_inf,
    mH_inf_dressed=mH_inf_dressed,
    frac_shift_mH=frac_shift_mH,
    # Sensitivity
    epsilons=epsilons,
    sin2_MZ_vs_eps=sin2_MZ_vs_eps,
    eps_best=eps_best,
    # Gate
    gate_name=np.array('BEYOND-MF-A4-68'),
    gate_verdict=np.array('INFO'),
    gate_detail=np.array(
        f'29.8% BCS correction to a_4: uniform {(rescale_factor-1)*100:.0f}% shift in g_i^2 at M_KK. '
        f'sin^2(theta_W)(M_Z) shifts {delta_sin2:+.6f}. '
        f'm_H(Aitken) {mH_inf:.1f} -> {mH_inf_dressed:.1f} GeV ({frac_shift_mH*100:+.1f}%). '
        f'Net a_4/a_2 shift only +{frac_shift_ratio*100:.1f}% due to partial a_2 cancellation.'
    ),
)

print(f"  Saved: {out_path}")

# =============================================================================
# 11. PLOT: RG RUNNING COMPARISON
# =============================================================================
print("\n" + "=" * 78)
print("11. GENERATING PLOTS")
print("=" * 78)

fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Panel 1: SM running from observed M_Z + BCS shift band
mu_vals = M_Z * np.exp(sol_up.t)
log_mu = np.log10(mu_vals)

inv_a1_SM = 1.0 / ((5.0/3.0) * sol_up.y[0]**2 / (4.0 * PI))
inv_a2_SM = 1.0 / (sol_up.y[1]**2 / (4.0 * PI))
inv_a3_SM = 1.0 / (sol_up.y[2]**2 / (4.0 * PI))

# Dressed: constant shift in 1/alpha propagated from M_KK
inv_a1_dressed_line = inv_a1_SM + delta_inv_a1_MZ
inv_a2_dressed_line = inv_a2_SM + delta_inv_a2_MZ
inv_a3_dressed_line = inv_a3_SM + delta_inv_a3_MZ

ax = axes[0]
ax.plot(log_mu, inv_a1_SM, 'b-', lw=1.5, label=r'$1/\alpha_1$ (SM)')
ax.plot(log_mu, inv_a2_SM, 'r-', lw=1.5, label=r'$1/\alpha_2$ (SM)')
ax.plot(log_mu, inv_a3_SM, 'g-', lw=1.5, label=r'$1/\alpha_3$ (SM)')
ax.plot(log_mu, inv_a1_dressed_line, 'b:', lw=2, alpha=0.7, label='BCS dressed')
ax.plot(log_mu, inv_a2_dressed_line, 'r:', lw=2, alpha=0.7)
ax.plot(log_mu, inv_a3_dressed_line, 'g:', lw=2, alpha=0.7)
ax.axvline(np.log10(M_KK_gravity), color='gray', ls='-.', alpha=0.5, label=r'$M_{KK}$')
ax.set_xlabel(r'$\log_{10}(\mu/\mathrm{GeV})$')
ax.set_ylabel(r'$1/\alpha_i$')
ax.set_title('Gauge Coupling Running (SM + BCS shift)')
ax.legend(fontsize=7, loc='upper left')
ax.set_ylim(0, 75)
ax.grid(alpha=0.3)

# Panel 2: sin^2(theta_W) sensitivity to non-uniform correction
ax = axes[1]
ax.plot(epsilons, sin2_MZ_vs_eps, 'k-', lw=2)
ax.axhline(sin2_thetaW_MSbar, color='red', ls='--', lw=1.5, label=f'Observed: {sin2_thetaW_MSbar}')
ax.axhline(sin2_fw_MZ_dressed, color='blue', ls=':', lw=1.5, label=f'Dressed (uniform): {sin2_fw_MZ_dressed:.5f}')
ax.axvline(0, color='gray', ls=':', alpha=0.5)
ax.fill_between(epsilons, sin2_thetaW_MSbar - 0.0005, sin2_thetaW_MSbar + 0.0005,
                alpha=0.2, color='red', label=r'$\pm 0.0005$')  # (local)
ax.set_xlabel(r'$\epsilon$ (non-uniformity parameter)')
ax.set_ylabel(r'$\sin^2(\theta_W)$ at $M_Z$')
ax.set_title(r'$\sin^2(\theta_W)$ Sensitivity')
ax.legend(fontsize=7)
ax.grid(alpha=0.3)

# Panel 3: Higgs mass bar chart
ax = axes[2]
labels_bar = ['L=6\nbare', 'L=6\ndressed', 'Aitken\nbare', 'Aitken\ndressed', 'Observed']
values_bar = [mH_L6, mH_L6_dressed, mH_inf, mH_inf_dressed, m_H_obs]
colors_bar = ['steelblue', 'navy', 'steelblue', 'navy', 'red']
alphas_bar = [0.6, 0.9, 0.6, 0.9, 0.7]

for i, (lbl, val, col, alp) in enumerate(zip(labels_bar, values_bar, colors_bar, alphas_bar)):
    ax.bar(i, val, color=col, edgecolor='black', alpha=alp)
ax.set_xticks(range(len(labels_bar)))
ax.set_xticklabels(labels_bar)
ax.axhline(m_H_obs, color='red', ls='--', lw=1.5, alpha=0.7)
ax.set_ylabel(r'$m_H$ (GeV)')
ax.set_title('Higgs Mass Shift')
ax.set_ylim(110, 155)
ax.grid(axis='y', alpha=0.3)

# Annotate shifts
for i, (v, l) in enumerate(zip(values_bar, labels_bar)):
    ax.text(i, v + 0.5, f'{v:.1f}', ha='center', va='bottom', fontsize=9)

plt.suptitle('BEYOND-MF-A4-68: Impact of 29.8% BCS Correction to $a_4$',
             fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()

plot_path = os.path.join(outdir, 's68_beyond_mf_a4.png')
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"  Saved: {plot_path}")

t_end = time.time()
print(f"\n  Total runtime: {t_end - t_start:.2f}s")
print("=" * 78)
print("DONE: BEYOND-MF-A4-68")
print("=" * 78)
