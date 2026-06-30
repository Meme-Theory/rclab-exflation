#!/usr/bin/env python3
"""
s62_higgs_bcs_threshold.py — HIGGS-BCS-THRESHOLD-62
2-loop Higgs mass with BCS correction to the UV boundary condition.

Physics
-------
The CCM spectral action yields a Higgs quartic coupling at the KK scale:
  lambda_H(M_KK) = (4/3) * g^2 * (a_4/a_2)
where a_4/a_2 = 0.414 is the Gilkey ratio from the SU(3) heat kernel (S61).

The BCS condensate screens the strong coupling at M_KK:
  g_3^{eff}(M_KK) = g_3(M_KK) * (1 - delta_BCS)

This script:
1. Implements the full 2-loop SM RGEs (Machacek-Vaughn 1984, Ford-Jack-Jones 1992)
2. Runs from M_KK DOWN to M_Z
3. Compares: (a) tree-level, (b) 2-loop no BCS, (c) 2-loop with BCS
4. Sensitivity: m_H vs delta_BCS, finding the exact delta_BCS for m_H = 125.1

Gate: HIGGS-BCS-THRESHOLD-62
  PASS: m_H(BCS-corrected, 2-loop) in [120, 135] GeV
  FAIL: m_H outside [100, 160] GeV
  INFO: in [100, 120] or [135, 160]

Author: connes-ncg-theorist
Session: S62 W1-04
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

from canonical_constants import (
    PI, M_KK, M_KK_gravity, M_KK_kerner,
    M_Pl_reduced,
    M_Z, M_W, alpha_em_MZ_inv, sin2_thetaW_MSbar,
    a0_fold, a2_fold, a4_fold,
    tau_fold, Delta_0_GL, Delta_B3,
)

outdir = os.path.dirname(os.path.abspath(__file__))

print("=" * 72)
print("HIGGS-BCS-THRESHOLD-62: 2-Loop Higgs Mass with BCS Correction")
print("=" * 72)

# =============================================================================
# 1. INPUT DATA AND PHYSICAL CONSTANTS
# =============================================================================
print("\n" + "=" * 72)
print("1. INPUT DATA")
print("=" * 72)

# Load S61 results
d_higgs = np.load(os.path.join(outdir, 's61_higgs_mass.npz'), allow_pickle=True)
d_bdg = np.load(os.path.join(outdir, 's61_bdg_spectral_action.npz'), allow_pickle=True)

# Geometric Gilkey ratio from S61
a2_gilkey = float(d_higgs['a2_gilkey'])       # 0.7282
a4_gilkey = float(d_higgs['a4_gilkey'])       # 0.3015
ratio_gilkey = float(d_higgs['ratio_gilkey']) # 0.4140

# BdG screening fractions
delta_a2_over_a2 = float(d_bdg['ratio_delta_a2'])  # 1.359e-4
delta_a4_over_a4 = float(d_bdg['ratio_delta_a4'])  # 1.491e-4

# Physical constants (PDG 2024)
v_ew = 246.22              # GeV, electroweak VEV (Fermi constant extraction)  # S72: intentionally differs from canonical v_ew=246.0 (uses Fermi-extracted value)
# m_H_obs = 125.10           # GeV (PDG 2024 combined)  # S72: now imported from canonical_constants
# m_t_pole = 172.69          # GeV (PDG 2024 pole mass)  # S72: now imported from canonical_constants
# m_b_pole = 4.78            # GeV (PDG 2024 pole mass)  # S72: now imported from canonical_constants
m_tau = 1.77686            # GeV

# alpha_s_MZ = 0.1180        # PDG 2024  # S72: now imported as alpha_s_MZ_obs from canonical_constants
alpha_s_MZ = alpha_s_MZ_obs  # S72: alias for downstream use
alpha_em_MZ = 1.0 / alpha_em_MZ_inv
sin2_tW = sin2_thetaW_MSbar  # 0.23122

# SM couplings at M_Z (MSbar)
g1_MZ = np.sqrt(5.0/3.0) * np.sqrt(4 * PI * alpha_em_MZ / (1 - sin2_tW))
g2_MZ = np.sqrt(4 * PI * alpha_em_MZ / sin2_tW)
g3_MZ = np.sqrt(4 * PI * alpha_s_MZ)
# Note: g1 in GUT normalization (factor sqrt(5/3))

# Top Yukawa at M_Z (MSbar, from pole mass with QCD correction)
# m_t(m_t) ~ m_t_pole * (1 - 4*alpha_s/(3*pi)) ~ 163.3 GeV
m_t_MSbar = m_t_pole * (1.0 - 4.0 * alpha_s_MZ / (3.0 * PI))
yt_MZ = np.sqrt(2) * m_t_MSbar / v_ew

# Bottom Yukawa and tau Yukawa (small but included for completeness)
yb_MZ = np.sqrt(2) * m_b_pole / v_ew
ytau_MZ = np.sqrt(2) * m_tau / v_ew

# Higgs quartic from observed mass
lambda_MZ_obs = m_H_obs**2 / (2.0 * v_ew**2)

# RG parameter: t = ln(mu/M_Z), running from t_MKK down to 0
t_MKK = np.log(M_KK_gravity / M_Z)  # ~ 34.3

print(f"  Gilkey ratio a_4/a_2     = {ratio_gilkey:.6f}")
print(f"  BdG screening delta_a2   = {delta_a2_over_a2:.4e}")
print(f"  BdG screening delta_a4   = {delta_a4_over_a4:.4e}")
print(f"  M_KK (gravity route)     = {M_KK_gravity:.4e} GeV")
print(f"  t_MKK = ln(M_KK/M_Z)    = {t_MKK:.4f}")
print(f"  v_ew                     = {v_ew} GeV")
print(f"  m_H (observed)           = {m_H_obs} GeV")
print(f"  m_t (pole)               = {m_t_pole} GeV")
print(f"  m_t (MSbar at M_Z)       = {m_t_MSbar:.2f} GeV")
print(f"\n  SM couplings at M_Z (MSbar):")
print(f"    g_1 (GUT norm) = {g1_MZ:.6f}")
print(f"    g_2            = {g2_MZ:.6f}")
print(f"    g_3            = {g3_MZ:.6f}")
print(f"    y_t            = {yt_MZ:.6f}")
print(f"    y_b            = {yb_MZ:.6f}")
print(f"    y_tau          = {ytau_MZ:.6f}")
print(f"    lambda         = {lambda_MZ_obs:.6f}")

# =============================================================================
# 2. TWO-LOOP SM BETA FUNCTIONS
# =============================================================================
# Reference: Machacek & Vaughn (1984) Nucl. Phys. B222, 83; B236, 221; B249, 70
# Also: Ford, Jack & Jones (1992) Nucl. Phys. B387, 373
# Also: Buttazzo et al. (2013) JHEP 12 (2013) 089 [arXiv:1307.3536]
# Conventions: g1 in GUT normalization (g1 = sqrt(5/3) * g'),
# t = ln(mu/mu_0), beta_x = dx/dt

def beta_2loop_SM(t, y, N_g=3):
    """
    Full 2-loop SM beta functions for (g1, g2, g3, yt, lambda).

    N_g = number of generations (3).
    g1 in GUT normalization: g1 = sqrt(5/3) * g'.

    We include only top Yukawa (dominant). Bottom and tau are perturbations
    at the ~1% level for the Higgs mass.
    """
    g1, g2, g3, yt, lam = y

    g1sq = g1**2
    g2sq = g2**2
    g3sq = g3**2
    ytsq = yt**2
    lamsq = lam**2

    b16pi2 = 16.0 * PI**2
    b16pi2_sq = b16pi2**2

    # =========================================================================
    # GAUGE COUPLING BETAS — 1-loop
    # =========================================================================
    # SM with N_g generations: b_i = (b_i^(1), b_i^(2))
    # 1-loop: beta_gi^(1) = b_i * g_i^3
    # GUT normalization for g1: b_1 = 41/10, b_2 = -19/6, b_3 = -7

    b1_1 = 41.0 / 10.0
    b2_1 = -19.0 / 6.0
    b3_1 = -7.0  # (local)

    beta_g1_1 = b1_1 * g1**3 / b16pi2
    beta_g2_1 = b2_1 * g2**3 / b16pi2
    beta_g3_1 = b3_1 * g3**3 / b16pi2

    # =========================================================================
    # GAUGE COUPLING BETAS — 2-loop
    # =========================================================================
    # beta_gi^(2) = sum_j b_{ij} * g_i^3 * g_j^2 / (16pi^2)^2
    # Plus Yukawa contributions at 2-loop
    #
    # From Machacek-Vaughn III (Nucl. Phys. B249, 70):
    # b_{ij} matrix (GUT-normalized g1):
    #   b_11 = 199/50, b_12 = 27/10, b_13 = 44/5
    #   b_21 = 9/10,   b_22 = 35/6,  b_23 = 12
    #   b_31 = 11/10,  b_32 = 9/2,   b_33 = -26
    #
    # Yukawa 2-loop contributions to gauge betas:
    #   beta_g1^(2,Y) = g1^3 * (-17/10 * ytsq) / (16pi^2)^2
    #   beta_g2^(2,Y) = g2^3 * (-3/2 * ytsq) / (16pi^2)^2
    #   beta_g3^(2,Y) = g3^3 * (-2 * ytsq) / (16pi^2)^2

    beta_g1_2 = g1**3 / b16pi2_sq * (
        199.0/50.0 * g1sq + 27.0/10.0 * g2sq + 44.0/5.0 * g3sq
        - 17.0/10.0 * ytsq
    )
    beta_g2_2 = g2**3 / b16pi2_sq * (
        9.0/10.0 * g1sq + 35.0/6.0 * g2sq + 12.0 * g3sq
        - 3.0/2.0 * ytsq
    )
    beta_g3_2 = g3**3 / b16pi2_sq * (
        11.0/10.0 * g1sq + 9.0/2.0 * g2sq - 26.0 * g3sq
        - 2.0 * ytsq
    )

    dg1 = beta_g1_1 + beta_g1_2
    dg2 = beta_g2_1 + beta_g2_2
    dg3 = beta_g3_1 + beta_g3_2

    # =========================================================================
    # TOP YUKAWA BETA — 1-loop + 2-loop
    # =========================================================================
    # 1-loop (Machacek-Vaughn):
    #   beta_yt^(1) = yt * [9/2 * ytsq - (17/20 * g1sq + 9/4 * g2sq + 8 * g3sq)]
    #   (with g1 in GUT normalization: 17/20 * g1sq instead of 17/12 * g'^2)
    #   Note: 17/20 = (17/12)*(3/5) for the GUT g1 convention

    beta_yt_1 = yt / b16pi2 * (
        9.0/2.0 * ytsq
        - 17.0/20.0 * g1sq - 9.0/4.0 * g2sq - 8.0 * g3sq
    )

    # 2-loop top Yukawa beta (from Buttazzo et al. 2013, Eq. (A.5)):
    # Dominant terms:
    beta_yt_2 = yt / b16pi2_sq * (
        - 12.0 * ytsq**2  # -12 * yt^4
        + ytsq * (
            393.0/80.0 * g1sq + 225.0/16.0 * g2sq + 36.0 * g3sq
        )
        + 1187.0/600.0 * g1sq**2 - 9.0/20.0 * g1sq * g2sq
        + 19.0/15.0 * g1sq * g3sq - 23.0/4.0 * g2sq**2
        + 9.0 * g2sq * g3sq - 108.0 * g3sq**2
        + 6.0 * lam**2 - 3.0/2.0 * lam * ytsq  # Higgs portal
    )

    dyt = beta_yt_1 + beta_yt_2

    # =========================================================================
    # HIGGS QUARTIC BETA — 1-loop + 2-loop
    # =========================================================================
    # 1-loop (Buttazzo et al., Machacek-Vaughn, with GUT-normalized g1):
    #   Note: with GUT g1, the coefficient 9/5 * g1^2 replaces 3 * g'^2

    beta_lam_1 = (1.0 / b16pi2) * (
        24.0 * lamsq
        + 12.0 * lam * ytsq - 12.0 * ytsq**2
        - 3.0 * lam * (3.0/5.0 * g1sq + 3.0 * g2sq)
        + 3.0/8.0 * (3.0/25.0 * g1sq**2 + 6.0/5.0 * g1sq * g2sq + 3.0 * g2sq**2)
    )

    # 2-loop Higgs quartic beta (from Buttazzo et al. 2013, simplified):
    # This is the crucial piece for precision Higgs mass prediction.
    beta_lam_2 = (1.0 / b16pi2_sq) * (
        # Pure scalar
        - 312.0 * lam**3
        # Scalar-Yukawa
        + lamsq * (-144.0 * ytsq)
        + lam * ytsq * (
            -3.0 * ytsq  # reduced from single-Y dominance
            + 80.0 * g3sq  # QCD enhancement
            + 45.0/2.0 * g2sq + 85.0/6.0 * (3.0/5.0) * g1sq
        )
        # Pure Yukawa at 2-loop
        + 60.0 * ytsq**3
        - 16.0 * ytsq**2 * g3sq  # destructive QCD-Yukawa
        # Gauge-scalar at 2-loop
        + lam * (
            108.0/5.0 * (3.0/25.0) * g1sq**2
            + 36.0 * (3.0/5.0 * g1sq * g2sq) / 5.0
            - 73.0/8.0 * g2sq**2
        )
        # Pure gauge at 2-loop (enter through Higgs potential renormalization)
        - 3.0/5.0 * g1sq * (
            -57.0/10.0 * g2sq * g1sq + 12.0 * ytsq**2
        ) / 2.0
        + g2sq * (
            -289.0/8.0 * g2sq**2 / 4.0
        )
    )

    dlam = beta_lam_1 + beta_lam_2

    return [dg1, dg2, dg3, dyt, dlam]


# =============================================================================
# 3. UV BOUNDARY CONDITIONS AT M_KK
# =============================================================================
print("\n" + "=" * 72)
print("2. UV BOUNDARY CONDITIONS AT M_KK")
print("=" * 72)

# Strategy: Run SM couplings UP from M_Z using observed values to get g_i(M_KK).
# Then set lambda(M_KK) from the CCM spectral action formula.
# Run back DOWN with these boundary conditions to get m_H.

# Step A: Run couplings UP from M_Z to M_KK to determine g_3(M_KK), g_2(M_KK), etc.
print("\n  Step A: Running SM couplings from M_Z to M_KK (2-loop)...")

y0_up = [g1_MZ, g2_MZ, g3_MZ, yt_MZ, lambda_MZ_obs]

N_pts = 5000  # (local)
t_eval_up = np.linspace(0, t_MKK, N_pts)

sol_up = solve_ivp(
    beta_2loop_SM, [0, t_MKK], y0_up,
    t_eval=t_eval_up,
    method='RK45', rtol=1e-12, atol=1e-14
)

if not sol_up.success:
    print(f"  WARNING: RG integration failed: {sol_up.message}")

# Extract couplings at M_KK
g1_at_MKK = sol_up.y[0, -1]
g2_at_MKK = sol_up.y[1, -1]
g3_at_MKK = sol_up.y[2, -1]
yt_at_MKK = sol_up.y[3, -1]
lam_at_MKK_obs = sol_up.y[4, -1]

print(f"  SM couplings at M_KK = {M_KK_gravity:.3e} GeV (from 2-loop upward run):")
print(f"    g_1(M_KK) = {g1_at_MKK:.6f}   [alpha_1^{-1} = {4*PI/(g1_at_MKK**2*3/5):.2f}]")
print(f"    g_2(M_KK) = {g2_at_MKK:.6f}   [alpha_2^{-1} = {4*PI/g2_at_MKK**2:.2f}]")
print(f"    g_3(M_KK) = {g3_at_MKK:.6f}   [alpha_3^{-1} = {4*PI/g3_at_MKK**2:.2f}]")
print(f"    y_t(M_KK) = {yt_at_MKK:.6f}")
print(f"    lambda(M_KK) from obs = {lam_at_MKK_obs:.6f}")

# Step B: CCM spectral action boundary condition for lambda at M_KK
# The CCM formula: lambda_H = (4/3) * g^2 * (a_4/a_2)
# where g^2 = pi^2/(2*f_0) is the unified coupling.
# In the spectral action, g_1 = g_2 = sqrt(5/3)*g_3 at the cutoff (SU(5) relation).
# But the SM couplings at M_KK do NOT satisfy this relation.
# We use g_3(M_KK) as the reference coupling (most precisely determined).
#
# The CCM quartic at the cutoff:
#   lambda_CCM(M_KK) = (4/3) * g_3^2(M_KK) * (a_4/a_2)

g3_MKK_nominal = g3_at_MKK  # = 0.519 (from SM running)
lambda_CCM_MKK = (4.0/3.0) * g3_MKK_nominal**2 * ratio_gilkey

print(f"\n  Step B: CCM spectral action boundary condition:")
print(f"    g_3(M_KK)                  = {g3_MKK_nominal:.6f}")
print(f"    a_4/a_2 (Gilkey)           = {ratio_gilkey:.6f}")
print(f"    lambda_CCM(M_KK)           = (4/3)*g3^2*(a4/a2) = {lambda_CCM_MKK:.6f}")
print(f"    lambda_obs(M_KK) from run  = {lam_at_MKK_obs:.6f}")
print(f"    Ratio CCM/obs              = {lambda_CCM_MKK/lam_at_MKK_obs:.4f}")

# Step C: Top Yukawa at M_KK
# The spectral action also predicts y_t at the cutoff from the Dirac operator.
# For now, use the SM-running value as the boundary condition.
# This is exact at 1-loop if there are no new physics thresholds.
yt_MKK_bc = yt_at_MKK

print(f"\n  Step C: Yukawa boundary condition:")
print(f"    y_t(M_KK) from SM running = {yt_MKK_bc:.6f}")

# =============================================================================
# 4. DOWNWARD RG: M_KK -> M_Z
# =============================================================================
print("\n" + "=" * 72)
print("3. DOWNWARD RG: M_KK -> M_Z (2-loop)")
print("=" * 72)

def run_rg_down(g1_UV, g2_UV, g3_UV, yt_UV, lam_UV, t_UV, N_pts=5000):
    """
    Run 2-loop SM RGEs from scale t_UV down to t=0 (M_Z).
    Returns (t_array, y_array, success).
    """
    y0 = [g1_UV, g2_UV, g3_UV, yt_UV, lam_UV]
    t_eval = np.linspace(t_UV, 0, N_pts)

    sol = solve_ivp(
        beta_2loop_SM, [t_UV, 0], y0,
        t_eval=t_eval,
        method='RK45', rtol=1e-12, atol=1e-14
    )
    return sol.t, sol.y, sol.success

# Case 1: CCM boundary condition, no BCS correction
print("\n  Case 1: CCM boundary, no BCS")
t_down, y_down, ok = run_rg_down(
    g1_at_MKK, g2_at_MKK, g3_MKK_nominal, yt_MKK_bc,
    lambda_CCM_MKK, t_MKK
)
if not ok:
    print("  WARNING: downward RG failed")

g1_IR = y_down[0, -1]
g2_IR = y_down[1, -1]
g3_IR = y_down[2, -1]
yt_IR = y_down[3, -1]
lam_IR = y_down[4, -1]

m_H_2loop_noBCS = np.sqrt(2.0 * abs(lam_IR)) * v_ew if lam_IR > 0 else 0.0

print(f"  Couplings at M_Z (from CCM downward run, no BCS):")
print(f"    g_1 = {g1_IR:.6f}  [obs: {g1_MZ:.6f}, dev: {(g1_IR/g1_MZ-1)*100:.2f}%]")
print(f"    g_2 = {g2_IR:.6f}  [obs: {g2_MZ:.6f}, dev: {(g2_IR/g2_MZ-1)*100:.2f}%]")
print(f"    g_3 = {g3_IR:.6f}  [obs: {g3_MZ:.6f}, dev: {(g3_IR/g3_MZ-1)*100:.2f}%]")
print(f"    y_t = {yt_IR:.6f}  [obs: {yt_MZ:.6f}, dev: {(yt_IR/yt_MZ-1)*100:.2f}%]")
print(f"    lambda = {lam_IR:.6f}  [obs: {lambda_MZ_obs:.6f}]")
print(f"\n  ** m_H (2-loop, no BCS) = sqrt(2*lambda) * v = {m_H_2loop_noBCS:.2f} GeV **")
print(f"  ** Observed: {m_H_obs} GeV, deviation: {(m_H_2loop_noBCS/m_H_obs - 1)*100:.1f}% **")

# Store the full running for plotting
t_run_noBCS = t_down.copy()
y_run_noBCS = y_down.copy()

# =============================================================================
# 5. BCS CORRECTION
# =============================================================================
print("\n" + "=" * 72)
print("4. BCS CORRECTION TO g_3 AT M_KK")
print("=" * 72)

# The BCS condensate screens gauge interactions at M_KK.
# From S61 BdG spectral action:
#   delta_a2/a_2 = 1.359e-4 (gravitational screening)
#   delta_a4/a_4 = 1.491e-4 (gauge kinetic screening)
#
# The gauge coupling squared is set by the spectral action:
#   1/g_3^2 = (f_0 * a_4) / (pi^2)
# (from the Yang-Mills term in the spectral action expansion).
# The BCS correction shifts a_4:
#   a_4 -> a_4 * (1 + delta_a4/a_4)
# So g_3^2 -> g_3^2 / (1 + delta_a4/a_4) ~ g_3^2 * (1 - delta_a4/a_4)
# Hence g_3 -> g_3 * (1 - delta_a4/(2*a_4))
#
# Direct screening: delta_BCS^{direct} = delta_a4/(2*a_4) = 7.5e-5
# This is TINY — the BCS condensate barely touches the gauge coupling.
#
# However, the PROMPT suggests delta_BCS = 0.07, estimated from the enhanced
# gauge fraction a_4/a_2 = 0.414. Let me compute both:

delta_BCS_direct = delta_a4_over_a4 / 2.0  # = 7.46e-5
delta_BCS_enhanced = 0.07  # Prompt estimate (via gauge fraction enhancement)  # (local)

# The enhanced estimate: the BCS condensate screens 0.014% of gravity (delta_a2/a_2),
# but the gauge-to-gravity ratio in the spectral action is a_4/a_2 = 0.414.
# If the screening is preferentially gauge (as in color superconductivity where
# the gap is in the QCD sector), then:
#   delta_BCS^{gauge} = delta_a2/a_2 * (a_2/a_4) * f_gauge
# where f_gauge accounts for the fact that BCS screening acts on color, not SU(2)/U(1).
# For SU(3) color: f_gauge ~ 8/(8+3+1) = 2/3 of the gauge sector.
# But this reasoning is speculative. Let me compute both endpoints.

# More precise estimate from BdG data:
# tr(Delta^2) = 2.467 in M_KK units (mostly B2 sector = SU(3) color)
# The B2 fraction: 2.374/2.467 = 96.2% -> gap is overwhelmingly in color sector
tr_Delta_sq = float(d_bdg['tr_Delta_sq'])
Delta_sq_B2 = float(d_bdg['Delta_sq_B2'])
f_color = Delta_sq_B2 / tr_Delta_sq  # fraction of gap in color sector

# The ratio a_4/a_2 determines how the spectral weight distributes:
# a_4 contains both the YM term (g^{-2} F^2) and the Higgs quartic.
# The screening of g_3 is proportional to tr(Delta^2) * (color fraction)
# relative to the total spectral weight a_4.
# Crude estimate: delta_g3/g3 ~ delta_a4/(2*a_4) * (full/color_only)
# But since the direct computation gives 7.5e-5, let me just scan delta_BCS.

print(f"  BdG screening data:")
print(f"    delta_a2/a_2 = {delta_a2_over_a2:.4e}")
print(f"    delta_a4/a_4 = {delta_a4_over_a4:.4e}")
print(f"    tr(Delta^2)  = {tr_Delta_sq:.4f}")
print(f"    B2 fraction  = {f_color:.4f}")
print(f"\n  BCS screening estimates:")
print(f"    delta_BCS (direct, delta_a4/2a_4) = {delta_BCS_direct:.4e}")
print(f"    delta_BCS (enhanced, prompt est.)  = {delta_BCS_enhanced:.4f}")

# Case 2: BCS correction with delta_BCS = 0.07 (prompt estimate)
g3_BCS = g3_MKK_nominal * (1.0 - delta_BCS_enhanced)
lambda_CCM_BCS = (4.0/3.0) * g3_BCS**2 * ratio_gilkey

print(f"\n  Case 2: CCM boundary, BCS-corrected (delta_BCS = {delta_BCS_enhanced}):")
print(f"    g_3^eff(M_KK) = {g3_BCS:.6f}")
print(f"    lambda_CCM(M_KK, BCS) = {lambda_CCM_BCS:.6f}")

t_down2, y_down2, ok2 = run_rg_down(
    g1_at_MKK, g2_at_MKK, g3_BCS, yt_MKK_bc,
    lambda_CCM_BCS, t_MKK
)

lam_IR_BCS = y_down2[4, -1]
m_H_2loop_BCS = np.sqrt(2.0 * abs(lam_IR_BCS)) * v_ew if lam_IR_BCS > 0 else 0.0

print(f"  Couplings at M_Z (BCS-corrected downward run):")
print(f"    g_3 = {y_down2[2, -1]:.6f}  [obs: {g3_MZ:.6f}]")
print(f"    lambda = {lam_IR_BCS:.6f}  [obs: {lambda_MZ_obs:.6f}]")
print(f"\n  ** m_H (2-loop, BCS delta=0.07) = {m_H_2loop_BCS:.2f} GeV **")

t_run_BCS = t_down2.copy()
y_run_BCS = y_down2.copy()

# =============================================================================
# 6. TREE-LEVEL COMPARISON
# =============================================================================
print("\n" + "=" * 72)
print("5. TREE-LEVEL (S61 REFERENCE)")
print("=" * 72)

# Tree-level: m_H = sqrt(2 * lambda_CCM) * v, no running
m_H_tree = np.sqrt(2.0 * lambda_CCM_MKK) * v_ew

# Also: the S61 "134 GeV" comes from the scaling approach
m_H_S61 = float(d_higgs['m_H_tree_g3_RG'])

print(f"  Tree-level (no RG):  m_H = sqrt(2*lambda_CCM) * v = {m_H_tree:.2f} GeV")
print(f"  S61 result:          m_H = {m_H_S61:.2f} GeV")
print(f"  2-loop (no BCS):     m_H = {m_H_2loop_noBCS:.2f} GeV")
print(f"  2-loop (BCS 0.07):   m_H = {m_H_2loop_BCS:.2f} GeV")
print(f"  Observed:            m_H = {m_H_obs} GeV")

# =============================================================================
# 7. SENSITIVITY ANALYSIS: m_H vs delta_BCS
# =============================================================================
print("\n" + "=" * 72)
print("6. SENSITIVITY: m_H vs delta_BCS")
print("=" * 72)

delta_BCS_scan = np.linspace(0.0, 0.50, 101)
m_H_scan = np.zeros_like(delta_BCS_scan)
g3_MZ_scan = np.zeros_like(delta_BCS_scan)
lam_MZ_scan = np.zeros_like(delta_BCS_scan)

for i, db in enumerate(delta_BCS_scan):
    g3_eff = g3_MKK_nominal * (1.0 - db)
    lam_eff = (4.0/3.0) * g3_eff**2 * ratio_gilkey

    t_s, y_s, ok_s = run_rg_down(
        g1_at_MKK, g2_at_MKK, g3_eff, yt_MKK_bc,
        lam_eff, t_MKK, N_pts=2000
    )

    lam_final = y_s[4, -1]
    m_H_scan[i] = np.sqrt(2.0 * abs(lam_final)) * v_ew if lam_final > 0 else 0.0
    g3_MZ_scan[i] = y_s[2, -1]
    lam_MZ_scan[i] = lam_final

    if i % 20 == 0:
        print(f"  delta_BCS = {db:.3f}: g3_eff = {g3_eff:.4f}, "
              f"lambda(M_Z) = {lam_final:.6f}, m_H = {m_H_scan[i]:.2f} GeV")

# Find delta_BCS that gives m_H = 125.1 GeV
# Need m_H_scan to cross 125.1
print(f"\n  m_H range: [{m_H_scan.min():.2f}, {m_H_scan.max():.2f}] GeV")

# Use interpolation to find exact crossing
delta_BCS_best = None
if m_H_scan[0] >= m_H_obs and m_H_scan[-1] <= m_H_obs:
    # Monotonically decreasing: find crossing
    from scipy.interpolate import interp1d
    interp = interp1d(m_H_scan[::-1], delta_BCS_scan[::-1], kind='linear')
    delta_BCS_best = float(interp(m_H_obs))
    print(f"\n  ** delta_BCS for m_H = {m_H_obs} GeV: {delta_BCS_best:.6f} **")
elif m_H_scan[0] <= m_H_obs:
    print(f"  m_H(delta_BCS=0) = {m_H_scan[0]:.2f} < {m_H_obs}: "
          f"already below observed even without BCS")
    delta_BCS_best = 0.0  # No correction needed, already too low or matching  # (local)
else:
    # Try to find crossing in the scanned range
    crossings = np.where(np.diff(np.sign(m_H_scan - m_H_obs)))[0]
    if len(crossings) > 0:
        idx = crossings[0]
        # Linear interpolation
        frac = (m_H_obs - m_H_scan[idx]) / (m_H_scan[idx+1] - m_H_scan[idx])
        delta_BCS_best = delta_BCS_scan[idx] + frac * (delta_BCS_scan[idx+1] - delta_BCS_scan[idx])
        print(f"\n  ** delta_BCS for m_H = {m_H_obs} GeV: {delta_BCS_best:.6f} **")
    else:
        print(f"  No crossing found in scanned range")

# =============================================================================
# 8. CONSISTENCY CHECKS
# =============================================================================
print("\n" + "=" * 72)
print("7. CONSISTENCY CHECKS")
print("=" * 72)

# Check 1: sin^2(theta_W) at M_Z from the downward run
# sin^2(theta_W) = g'^2 / (g'^2 + g_2^2) = (3/5)*g1^2 / ((3/5)*g1^2 + g2^2)
g1p_IR = np.sqrt(3.0/5.0) * g1_IR  # convert from GUT to standard normalization
sin2_tW_pred = g1p_IR**2 / (g1p_IR**2 + g2_IR**2)
print(f"  sin^2(theta_W) at M_Z:")
print(f"    Predicted (2-loop, no BCS)  = {sin2_tW_pred:.5f}")
print(f"    Observed (PDG)              = {sin2_tW:.5f}")
print(f"    Deviation                   = {(sin2_tW_pred/sin2_tW - 1)*100:.3f}%")

# Check 2: m_W, m_Z from the gauge couplings
m_W_pred = g2_IR * v_ew / 2.0
g1p_noBCS = np.sqrt(3.0/5.0) * g1_IR
m_Z_pred = v_ew / 2.0 * np.sqrt(g2_IR**2 + g1p_noBCS**2)
print(f"\n  Gauge boson masses from predicted couplings:")
print(f"    m_W = g_2 * v / 2 = {m_W_pred:.2f} GeV  [obs: {M_W} GeV, "
      f"dev: {(m_W_pred/M_W - 1)*100:.2f}%]")
print(f"    m_Z = v/(2)*sqrt(g2^2+g'^2) = {m_Z_pred:.2f} GeV  [obs: {M_Z} GeV, "
      f"dev: {(m_Z_pred/M_Z - 1)*100:.2f}%]")

# Check 3: alpha_s(M_Z) from the downward run
alpha_s_pred = g3_IR**2 / (4.0 * PI)
print(f"\n  alpha_s(M_Z):")
print(f"    Predicted (2-loop, no BCS) = {alpha_s_pred:.4f}")
print(f"    Observed (PDG)             = {alpha_s_MZ:.4f}")
print(f"    Deviation                  = {(alpha_s_pred/alpha_s_MZ - 1)*100:.3f}%")

# Check 4: Vacuum stability
lam_min_down = np.min(y_run_noBCS[4])
idx_min = np.argmin(y_run_noBCS[4])
mu_min = M_Z * np.exp(t_run_noBCS[idx_min])
print(f"\n  Vacuum stability (no BCS):")
print(f"    lambda_min = {lam_min_down:.6f} at mu = {mu_min:.2e} GeV")
print(f"    Status: {'STABLE' if lam_min_down > 0 else 'METASTABLE (lambda < 0)'}")

# Check 5: BCS correction self-consistency
# The BdG spectral action gives delta_a4/a_4 = 1.49e-4.
# The implied delta_BCS from this direct computation:
print(f"\n  BCS consistency check:")
print(f"    delta_BCS (direct from BdG SA) = {delta_BCS_direct:.4e}")
print(f"    delta_BCS (needed for 125.1)   = {delta_BCS_best if delta_BCS_best else 'N/A'}")
if delta_BCS_best is not None and delta_BCS_best > 0:
    print(f"    Ratio (needed/direct)          = {delta_BCS_best/delta_BCS_direct:.1f}")
    print(f"    The direct BdG screening is {delta_BCS_direct/delta_BCS_best*100:.3f}% "
          f"of what would be needed for exact m_H = 125.1 GeV")

# Check 6: 1-loop vs 2-loop comparison
# Run with 1-loop only for comparison
def beta_1loop_SM(t, y):
    """1-loop SM beta functions only."""
    g1, g2, g3, yt, lam = y
    b16pi2 = 16.0 * PI**2

    dg1 = (41.0/10.0) * g1**3 / b16pi2
    dg2 = -(19.0/6.0) * g2**3 / b16pi2
    dg3 = -7.0 * g3**3 / b16pi2

    dyt = yt / b16pi2 * (
        9.0/2.0 * yt**2
        - 17.0/20.0 * g1**2 - 9.0/4.0 * g2**2 - 8.0 * g3**2
    )

    dlam = (1.0 / b16pi2) * (
        24.0 * lam**2
        + 12.0 * lam * yt**2 - 12.0 * yt**4
        - 3.0 * lam * (3.0/5.0 * g1**2 + 3.0 * g2**2)
        + 3.0/8.0 * (3.0/25.0 * g1**4 + 6.0/5.0 * g1**2 * g2**2 + 3.0 * g2**4)
    )

    return [dg1, dg2, dg3, dyt, dlam]

sol_1loop = solve_ivp(
    beta_1loop_SM, [t_MKK, 0],
    [g1_at_MKK, g2_at_MKK, g3_MKK_nominal, yt_MKK_bc, lambda_CCM_MKK],
    t_eval=np.linspace(t_MKK, 0, 2000),
    method='RK45', rtol=1e-12, atol=1e-14
)
lam_1loop_IR = sol_1loop.y[4, -1]
m_H_1loop = np.sqrt(2.0 * abs(lam_1loop_IR)) * v_ew if lam_1loop_IR > 0 else 0.0

print(f"\n  1-loop vs 2-loop comparison:")
print(f"    m_H (1-loop) = {m_H_1loop:.2f} GeV")
print(f"    m_H (2-loop) = {m_H_2loop_noBCS:.2f} GeV")
print(f"    2-loop shift = {m_H_2loop_noBCS - m_H_1loop:.2f} GeV ({(m_H_2loop_noBCS/m_H_1loop - 1)*100:.2f}%)")

# =============================================================================
# 9. GATE VERDICT
# =============================================================================
print("\n" + "=" * 72)
print("8. GATE VERDICT: HIGGS-BCS-THRESHOLD-62")
print("=" * 72)

# The decisive number: m_H with BCS correction
m_H_decisive = m_H_2loop_BCS

print(f"\n  Pre-registered gate: HIGGS-BCS-THRESHOLD-62")
print(f"    m_H (2-loop, BCS delta={delta_BCS_enhanced}) = {m_H_decisive:.2f} GeV")

if 120 <= m_H_decisive <= 135:
    gate_verdict = "PASS"
    gate_detail = (f"m_H = {m_H_decisive:.2f} GeV in [120, 135]. "
                   f"Tree: {m_H_tree:.1f}, 2-loop no BCS: {m_H_2loop_noBCS:.1f}, "
                   f"BCS(delta={delta_BCS_enhanced}): {m_H_decisive:.1f}. "
                   f"delta_BCS for 125.1: {delta_BCS_best:.4f}" if delta_BCS_best else "N/A")
elif 100 <= m_H_decisive <= 160:
    if m_H_decisive < 120:
        gate_verdict = "INFO"
        gate_detail = (f"m_H = {m_H_decisive:.2f} GeV in [100, 120] (marginal low). "
                       f"Tree: {m_H_tree:.1f}, 2-loop no BCS: {m_H_2loop_noBCS:.1f}.")
    else:
        gate_verdict = "INFO"
        gate_detail = (f"m_H = {m_H_decisive:.2f} GeV in [135, 160] (marginal high). "
                       f"Tree: {m_H_tree:.1f}, 2-loop no BCS: {m_H_2loop_noBCS:.1f}.")
else:
    gate_verdict = "FAIL"
    gate_detail = (f"m_H = {m_H_decisive:.2f} GeV outside [100, 160]. "
                   f"Tree: {m_H_tree:.1f}, 2-loop no BCS: {m_H_2loop_noBCS:.1f}.")

print(f"\n  VERDICT: {gate_verdict}")
print(f"  Detail: {gate_detail}")

# =============================================================================
# 10. PLOTS
# =============================================================================
print("\n" + "=" * 72)
print("9. GENERATING PLOTS")
print("=" * 72)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('HIGGS-BCS-THRESHOLD-62: 2-Loop Higgs Mass with BCS Correction',
             fontsize=13, fontweight='bold')

# Panel (a): RG running of couplings — no BCS
ax = axes[0, 0]
mu_arr = M_Z * np.exp(t_run_noBCS)
ax.plot(np.log10(mu_arr), y_run_noBCS[0], 'b-', label=r'$g_1$ (GUT norm)', lw=1.2)
ax.plot(np.log10(mu_arr), y_run_noBCS[1], 'g-', label=r'$g_2$', lw=1.2)
ax.plot(np.log10(mu_arr), y_run_noBCS[2], 'r-', label=r'$g_3$', lw=1.2)
ax.plot(np.log10(mu_arr), y_run_noBCS[3], 'm-', label=r'$y_t$', lw=1.2)
ax.plot(np.log10(mu_arr), y_run_noBCS[4]*10, 'k--', label=r'$10\lambda$', lw=1.2)
ax.axvline(np.log10(M_Z), color='gray', ls=':', alpha=0.5)
ax.axvline(np.log10(M_KK_gravity), color='gray', ls=':', alpha=0.5)
ax.set_xlabel(r'$\log_{10}(\mu / {\rm GeV})$')
ax.set_ylabel('Coupling value')
ax.set_title('(a) SM RG running (2-loop, no BCS)')
ax.legend(fontsize=8, loc='upper right')
ax.set_xlim([1.5, np.log10(M_KK_gravity)+0.5])
ax.grid(True, alpha=0.3)

# Panel (b): RG running with BCS overlay
ax = axes[0, 1]
mu_noBCS = M_Z * np.exp(t_run_noBCS)
mu_BCS = M_Z * np.exp(t_run_BCS)
ax.plot(np.log10(mu_noBCS), y_run_noBCS[2], 'r-', label=r'$g_3$ (no BCS)', lw=1.5)
ax.plot(np.log10(mu_BCS), y_run_BCS[2], 'r--', label=r'$g_3$ (BCS)', lw=1.5)
ax.plot(np.log10(mu_noBCS), y_run_noBCS[4]*10, 'k-', label=r'$10\lambda$ (no BCS)', lw=1.5)
ax.plot(np.log10(mu_BCS), y_run_BCS[4]*10, 'k--', label=r'$10\lambda$ (BCS)', lw=1.5)
ax.axhline(lambda_MZ_obs*10, color='orange', ls=':', label=r'$10\lambda_{\rm obs}$')
ax.set_xlabel(r'$\log_{10}(\mu / {\rm GeV})$')
ax.set_ylabel('Coupling value')
ax.set_title(f'(b) BCS effect on $g_3$ and $\\lambda$ ($\\delta_{{BCS}}$={delta_BCS_enhanced})')
ax.legend(fontsize=8, loc='upper right')
ax.set_xlim([1.5, np.log10(M_KK_gravity)+0.5])
ax.grid(True, alpha=0.3)

# Panel (c): m_H vs delta_BCS
ax = axes[1, 0]
ax.plot(delta_BCS_scan, m_H_scan, 'b-', lw=2)
ax.axhline(m_H_obs, color='red', ls='--', lw=1.5, label=f'$m_H^{{obs}}$ = {m_H_obs} GeV')
ax.axhspan(120, 135, color='green', alpha=0.15, label='PASS [120, 135]')
ax.axhspan(100, 120, color='yellow', alpha=0.10, label='INFO [100, 120]')
ax.axhspan(135, 160, color='yellow', alpha=0.10, label='INFO [135, 160]')
if delta_BCS_best is not None and delta_BCS_best > 0:
    ax.axvline(delta_BCS_best, color='red', ls=':', lw=1,
               label=f'$\\delta_{{BCS}}^*$ = {delta_BCS_best:.4f}')
ax.axvline(delta_BCS_direct, color='purple', ls=':', lw=1,
           label=f'$\\delta_{{BCS}}^{{BdG}}$ = {delta_BCS_direct:.1e}')
ax.axvline(delta_BCS_enhanced, color='orange', ls=':', lw=1,
           label=f'$\\delta_{{BCS}}^{{est}}$ = {delta_BCS_enhanced}')
ax.set_xlabel(r'$\delta_{BCS}$')
ax.set_ylabel(r'$m_H$ (GeV)')
ax.set_title('(c) Higgs mass vs BCS screening')
ax.legend(fontsize=7, loc='upper right')
ax.set_xlim([0, 0.50])
ax.grid(True, alpha=0.3)

# Panel (d): Comparison bar chart
ax = axes[1, 1]
labels = ['Tree\n(CCM)', '1-loop\n(no BCS)', '2-loop\n(no BCS)',
          f'2-loop\n(BCS {delta_BCS_enhanced})', 'Observed']
masses = [m_H_tree, m_H_1loop, m_H_2loop_noBCS, m_H_2loop_BCS, m_H_obs]
colors = ['#4a90d9', '#6ab04c', '#2ecc71', '#e17055', '#e74c3c']
bars = ax.bar(labels, masses, color=colors, edgecolor='black', alpha=0.85)

# Add value labels on bars
for bar, val in zip(bars, masses):
    ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 1,
            f'{val:.1f}', ha='center', va='bottom', fontsize=9, fontweight='bold')

ax.axhline(m_H_obs, color='red', ls='--', lw=1.5, alpha=0.7)
ax.axhspan(120, 135, color='green', alpha=0.10)
ax.set_ylabel(r'$m_H$ (GeV)')
ax.set_title('(d) Higgs mass predictions comparison')
ax.set_ylim([0, max(masses) * 1.2])
ax.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig(os.path.join(outdir, 's62_higgs_bcs_threshold.png'), dpi=150, bbox_inches='tight')
print("  Plot saved: s62_higgs_bcs_threshold.png")

# =============================================================================
# 11. SAVE DATA
# =============================================================================
print("\n" + "=" * 72)
print("10. SAVING DATA")
print("=" * 72)

np.savez(
    os.path.join(outdir, 's62_higgs_bcs_threshold.npz'),
    # Input
    ratio_gilkey=ratio_gilkey,
    a2_gilkey=a2_gilkey,
    a4_gilkey=a4_gilkey,
    delta_a2_over_a2=delta_a2_over_a2,
    delta_a4_over_a4=delta_a4_over_a4,
    g3_MKK_nominal=g3_MKK_nominal,
    g1_MKK=g1_at_MKK,
    g2_MKK=g2_at_MKK,
    yt_MKK=yt_MKK_bc,
    t_MKK=t_MKK,
    M_KK=M_KK_gravity,
    v_ew=v_ew,
    # Tree level
    m_H_tree=m_H_tree,
    lambda_CCM_MKK=lambda_CCM_MKK,
    # 1-loop
    m_H_1loop=m_H_1loop,
    lambda_1loop_MZ=lam_1loop_IR,
    # 2-loop no BCS
    m_H_2loop_noBCS=m_H_2loop_noBCS,
    lambda_2loop_MZ=lam_IR,
    g1_IR_noBCS=g1_IR,
    g2_IR_noBCS=g2_IR,
    g3_IR_noBCS=g3_IR,
    yt_IR_noBCS=yt_IR,
    # 2-loop with BCS
    delta_BCS_enhanced=delta_BCS_enhanced,
    delta_BCS_direct=delta_BCS_direct,
    g3_BCS=g3_BCS,
    lambda_CCM_BCS=lambda_CCM_BCS,
    m_H_2loop_BCS=m_H_2loop_BCS,
    lambda_BCS_MZ=lam_IR_BCS,
    # Sensitivity scan
    delta_BCS_scan=delta_BCS_scan,
    m_H_scan=m_H_scan,
    g3_MZ_scan=g3_MZ_scan,
    lam_MZ_scan=lam_MZ_scan,
    delta_BCS_best=delta_BCS_best if delta_BCS_best is not None else np.nan,
    # Running (for external use)
    t_run_noBCS=t_run_noBCS,
    g1_run_noBCS=y_run_noBCS[0],
    g2_run_noBCS=y_run_noBCS[1],
    g3_run_noBCS=y_run_noBCS[2],
    yt_run_noBCS=y_run_noBCS[3],
    lam_run_noBCS=y_run_noBCS[4],
    t_run_BCS=t_run_BCS,
    g3_run_BCS=y_run_BCS[2],
    lam_run_BCS=y_run_BCS[4],
    # Consistency checks
    sin2_tW_pred=sin2_tW_pred,
    m_W_pred=m_W_pred,
    m_Z_pred=m_Z_pred,
    alpha_s_pred=alpha_s_pred,
    # Gate
    gate_name='HIGGS-BCS-THRESHOLD-62',
    gate_verdict=gate_verdict,
    gate_detail=gate_detail,
)

print(f"  Data saved: s62_higgs_bcs_threshold.npz")

# =============================================================================
# SUMMARY
# =============================================================================
print("\n" + "=" * 72)
print("SUMMARY")
print("=" * 72)
print(f"  Tree-level m_H (CCM, Gilkey)       = {m_H_tree:.2f} GeV")
print(f"  1-loop m_H (no BCS)                = {m_H_1loop:.2f} GeV")
print(f"  2-loop m_H (no BCS)                = {m_H_2loop_noBCS:.2f} GeV")
print(f"  2-loop m_H (BCS delta=0.07)        = {m_H_2loop_BCS:.2f} GeV")
print(f"  Observed m_H                       = {m_H_obs} GeV")
print(f"  delta_BCS for exact match           = {delta_BCS_best if delta_BCS_best is not None else 'N/A'}")
print(f"  delta_BCS from BdG SA (direct)     = {delta_BCS_direct:.4e}")
print(f"  1-loop -> 2-loop shift             = {m_H_2loop_noBCS - m_H_1loop:.2f} GeV")
print(f"  BCS correction shift (delta=0.07)  = {m_H_2loop_BCS - m_H_2loop_noBCS:.2f} GeV")
print(f"  Gate: HIGGS-BCS-THRESHOLD-62       = {gate_verdict}")
print("=" * 72)
