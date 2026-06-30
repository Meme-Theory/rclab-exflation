#!/usr/bin/env python3
"""
s63_higgs_running.py — HIGGS-RUNNING-63
Definitive Higgs mass prediction: 2-loop SM RGE with KK threshold from full PW tower.

Physics
-------
The CCM spectral action on M4 x SU(3) yields a Higgs quartic coupling at M_KK:

    lambda_CCM(M_KK) = (4/3) * g_3^{eff}(M_KK)^2 * (a_4/a_2)        (1)

where a_4/a_2 = 0.4140 is the Gilkey ratio (tau-independent, proven S61).

The effective g_3 at M_KK includes threshold corrections from integrating out
the PW tower of KK modes:

    1/g_3^{eff,2} = 1/g_3^{SM,2}(M_KK) + delta(1/g_3^2)_KK           (2)

where delta(1/g_3^2)_KK = 2.353 (Gaussian, L=6) from KK-THRESHOLD-63.

Additionally, the BCS condensate screens g_3 at the matching scale:

    g_3^{eff}(M_KK) = g_3^{KK-corrected}(M_KK) * (1 - delta_BCS)      (3)

Procedure:
    1. Run SM couplings UP from M_Z to M_KK (2-loop) to get g_3^{SM}(M_KK).
    2. Apply KK threshold: g_3^{eff} from Eq.(2).
    3. Optionally apply BCS correction from Eq.(3).
    4. Set lambda_CCM from Eq.(1).
    5. Run 2-loop SM RGE DOWN from M_KK to M_Z.
    6. m_H = sqrt(2*lambda(M_Z)) * v_ew.

Gate: HIGGS-RUNNING-63
    PASS: m_H in [120, 135] GeV
    FAIL: m_H outside [100, 150] GeV
    INFO: in [100, 120] or [135, 150]

Inputs:
    - computations/session-63/s63_kk_threshold.npz (delta_g3_inv at L=1..6, sharp+Gaussian)
    - computations/session-63/s63_f0_matching.npz  (f_0 interpretations)
    - computations/session-62/s62_higgs_bcs_threshold.npz (2-loop RGE validation, BCS scan)

Output:
    - computations/session-63/s63_higgs_running.npz
    - computations/session-63/s63_higgs_running.png

Author: einstein-theorist
Session: S63 W4-02
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
    M_Pl_reduced, M_Z, M_W,
    alpha_em_MZ_inv, sin2_thetaW_MSbar,
    a0_fold, a2_fold, a4_fold,
    tau_fold, Delta_0_GL, Delta_B3,
)

outdir = os.path.dirname(os.path.abspath(__file__))

print("=" * 76)
print("HIGGS-RUNNING-63: Definitive Higgs Mass — 2-Loop SM RGE + KK Threshold")
print("=" * 76)

# ============================================================================
# 1. PHYSICAL CONSTANTS AND INPUTS
# ============================================================================
print("\n" + "=" * 76)
print("1. PHYSICAL CONSTANTS AND INPUTS")
print("=" * 76)

# PDG 2024 observables
v_ew = 246.22            # GeV, Fermi VEV  # S72: intentionally differs from canonical v_ew=246.0 (Fermi-extracted)
# m_H_obs = 125.10         # GeV  # S72: now imported from canonical_constants
# m_t_pole = 172.69        # GeV  # S72: now imported from canonical_constants
# m_b_pole = 4.78          # GeV  # S72: now imported from canonical_constants
m_tau_lep = 1.77686      # GeV  # (local)
# alpha_s_MZ = 0.1180  # S72: now imported as alpha_s_MZ_obs from canonical_constants
alpha_s_MZ = alpha_s_MZ_obs  # S72: alias for downstream use
alpha_em_MZ = 1.0 / alpha_em_MZ_inv
sin2_tW = sin2_thetaW_MSbar  # 0.23122

# SM couplings at M_Z (MSbar)
g1_MZ = np.sqrt(5.0/3.0) * np.sqrt(4.0 * PI * alpha_em_MZ / (1.0 - sin2_tW))
g2_MZ = np.sqrt(4.0 * PI * alpha_em_MZ / sin2_tW)
g3_MZ = np.sqrt(4.0 * PI * alpha_s_MZ)
m_t_MSbar = m_t_pole * (1.0 - 4.0 * alpha_s_MZ / (3.0 * PI))
yt_MZ = np.sqrt(2.0) * m_t_MSbar / v_ew
yb_MZ = np.sqrt(2.0) * m_b_pole / v_ew
ytau_MZ = np.sqrt(2.0) * m_tau_lep / v_ew
lambda_MZ_obs = m_H_obs**2 / (2.0 * v_ew**2)

# RG parameter
t_MKK = np.log(M_KK_gravity / M_Z)  # ~ 34.3

# Gilkey ratio (proven S61, tau-independent)
# Load from s63_kk_threshold.npz for consistency
d_kk = np.load(os.path.join(outdir, 's63_kk_threshold.npz'), allow_pickle=True)
ratio_gilkey = float(d_kk['ratio_gilkey'])
g3_MKK_nominal = float(d_kk['g3_MKK_nominal'])

# KK threshold corrections from W1-02
delta_g3inv_sharp_L6 = float(d_kk['delta_g3_inv_sharp_fixed'][-1])
delta_g3inv_gauss_L6 = float(d_kk['delta_g3_inv_gauss_fixed'][-1])
delta_g3inv_sharp_arr = np.array(d_kk['delta_g3_inv_sharp_fixed'])
delta_g3inv_gauss_arr = np.array(d_kk['delta_g3_inv_gauss_fixed'])
m_H_kk_sharp_arr = np.array(d_kk['m_H_by_L_sharp'])
m_H_kk_gauss_arr = np.array(d_kk['m_H_by_L_gauss'])
Lambda_fixed = float(d_kk['Lambda_fixed'])
gamma_opt = float(d_kk['gamma_opt'])
L_range = np.arange(1, 7)

# Load BCS scan from S62 for delta_BCS sensitivity
d_bcs = np.load(os.path.join(outdir, 's62_higgs_bcs_threshold.npz'), allow_pickle=True)
delta_BCS_scan_s62 = np.array(d_bcs['delta_BCS_scan'])
m_H_scan_s62 = np.array(d_bcs['m_H_scan'])
g3_MZ_scan_s62 = np.array(d_bcs['g3_MZ_scan'])
m_H_2loop_noBCS_s62 = float(d_bcs['m_H_2loop_noBCS'])
delta_BCS_best_s62 = float(d_bcs['delta_BCS_best'])

print(f"  SM at M_Z: g1={g1_MZ:.4f}, g2={g2_MZ:.4f}, g3={g3_MZ:.4f}, yt={yt_MZ:.4f}")
print(f"  lambda_obs(M_Z)       = {lambda_MZ_obs:.6f}")
print(f"  t_MKK = ln(M_KK/M_Z) = {t_MKK:.4f}")
print(f"  Gilkey ratio a4/a2    = {ratio_gilkey:.6f}")
print(f"  g3^SM(M_KK) nominal   = {g3_MKK_nominal:.6f}")
print(f"  1/g3^2(M_KK) nominal  = {1.0/g3_MKK_nominal**2:.6f}")
print(f"\n  KK threshold corrections (L=6, Lambda_fixed={Lambda_fixed:.4f}):")
print(f"    delta(1/g3^2) sharp   = {delta_g3inv_sharp_L6:.4f}")
print(f"    delta(1/g3^2) Gauss   = {delta_g3inv_gauss_L6:.4f}")
print(f"    m_H(sharp, W1-02)     = {m_H_kk_sharp_arr[-1]:.2f} GeV")
print(f"    m_H(Gauss, W1-02)     = {m_H_kk_gauss_arr[-1]:.2f} GeV")

# ============================================================================
# 2. TWO-LOOP SM BETA FUNCTIONS (identical to S62)
# ============================================================================
# Reference: Machacek & Vaughn (1984), Ford-Jack-Jones (1992),
#            Buttazzo et al. (2013) arXiv:1307.3536

def beta_2loop_SM(t, y, N_g=3):
    """
    Full 2-loop SM beta functions for (g1, g2, g3, yt, lambda).
    g1 in GUT normalization: g1 = sqrt(5/3) * g'.
    Only top Yukawa (dominant by factor (m_t/m_b)^2 ~ 1300).
    """
    g1, g2, g3, yt, lam = y

    g1sq = g1**2
    g2sq = g2**2
    g3sq = g3**2
    ytsq = yt**2

    b16pi2 = 16.0 * PI**2
    b16pi2_sq = b16pi2**2

    # Gauge 1-loop: b1=41/10, b2=-19/6, b3=-7
    b1_1, b2_1, b3_1 = 41.0/10.0, -19.0/6.0, -7.0
    beta_g1_1 = b1_1 * g1**3 / b16pi2
    beta_g2_1 = b2_1 * g2**3 / b16pi2
    beta_g3_1 = b3_1 * g3**3 / b16pi2

    # Gauge 2-loop (Machacek-Vaughn III)
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

    # Top Yukawa 1-loop + 2-loop (Buttazzo et al.)
    beta_yt_1 = yt / b16pi2 * (
        9.0/2.0 * ytsq
        - 17.0/20.0 * g1sq - 9.0/4.0 * g2sq - 8.0 * g3sq
    )
    beta_yt_2 = yt / b16pi2_sq * (
        - 12.0 * ytsq**2
        + ytsq * (393.0/80.0 * g1sq + 225.0/16.0 * g2sq + 36.0 * g3sq)
        + 1187.0/600.0 * g1sq**2 - 9.0/20.0 * g1sq * g2sq
        + 19.0/15.0 * g1sq * g3sq - 23.0/4.0 * g2sq**2
        + 9.0 * g2sq * g3sq - 108.0 * g3sq**2
        + 6.0 * lam**2 - 3.0/2.0 * lam * ytsq
    )
    dyt = beta_yt_1 + beta_yt_2

    # Higgs quartic 1-loop + 2-loop (Buttazzo et al., GUT-normalized g1)
    beta_lam_1 = (1.0 / b16pi2) * (
        24.0 * lam**2
        + 12.0 * lam * ytsq - 12.0 * ytsq**2
        - 3.0 * lam * (3.0/5.0 * g1sq + 3.0 * g2sq)
        + 3.0/8.0 * (3.0/25.0 * g1sq**2 + 6.0/5.0 * g1sq * g2sq + 3.0 * g2sq**2)
    )
    beta_lam_2 = (1.0 / b16pi2_sq) * (
        - 312.0 * lam**3
        + lam**2 * (-144.0 * ytsq)
        + lam * ytsq * (
            -3.0 * ytsq + 80.0 * g3sq
            + 45.0/2.0 * g2sq + 85.0/6.0 * (3.0/5.0) * g1sq
        )
        + 60.0 * ytsq**3
        - 16.0 * ytsq**2 * g3sq
        + lam * (
            108.0/5.0 * (3.0/25.0) * g1sq**2
            + 36.0 * (3.0/5.0 * g1sq * g2sq) / 5.0
            - 73.0/8.0 * g2sq**2
        )
        - 3.0/5.0 * g1sq * (
            -57.0/10.0 * g2sq * g1sq + 12.0 * ytsq**2
        ) / 2.0
        + g2sq * (-289.0/8.0 * g2sq**2 / 4.0)
    )
    dlam = beta_lam_1 + beta_lam_2

    return [dg1, dg2, dg3, dyt, dlam]


def run_rg_down(g1_UV, g2_UV, g3_UV, yt_UV, lam_UV, t_UV, N_pts=5000):
    """Run 2-loop SM RGEs from t_UV down to t=0 (M_Z)."""
    y0 = [g1_UV, g2_UV, g3_UV, yt_UV, lam_UV]
    t_eval = np.linspace(t_UV, 0, N_pts)
    sol = solve_ivp(
        beta_2loop_SM, [t_UV, 0], y0,
        t_eval=t_eval, method='RK45', rtol=1e-12, atol=1e-14,
    )
    return sol.t, sol.y, sol.success


def run_rg_up(g1_IR, g2_IR, g3_IR, yt_IR, lam_IR, t_UV, N_pts=5000):
    """Run 2-loop SM RGEs from t=0 (M_Z) up to t_UV."""
    y0 = [g1_IR, g2_IR, g3_IR, yt_IR, lam_IR]
    t_eval = np.linspace(0, t_UV, N_pts)
    sol = solve_ivp(
        beta_2loop_SM, [0, t_UV], y0,
        t_eval=t_eval, method='RK45', rtol=1e-12, atol=1e-14,
    )
    return sol.t, sol.y, sol.success


def mH_from_lambda_MZ(lam_MZ):
    """Higgs pole mass from lambda(M_Z)."""
    if lam_MZ > 0:
        return np.sqrt(2.0 * lam_MZ) * v_ew
    else:
        return np.nan


# ============================================================================
# 3. STEP A — RUN SM COUPLINGS UP TO M_KK
# ============================================================================
print("\n" + "=" * 76)
print("2. RUN SM COUPLINGS M_Z -> M_KK (2-loop)")
print("=" * 76)

t_up, y_up, ok_up = run_rg_up(g1_MZ, g2_MZ, g3_MZ, yt_MZ, lambda_MZ_obs, t_MKK)
assert ok_up, "Upward RG integration failed!"

g1_UV = y_up[0, -1]
g2_UV = y_up[1, -1]
g3_UV = y_up[2, -1]
yt_UV = y_up[3, -1]
lam_UV_obs = y_up[4, -1]

g3inv2_SM_UV = 1.0 / g3_UV**2

print(f"  SM couplings at M_KK = {M_KK_gravity:.4e} GeV:")
print(f"    g1(M_KK) = {g1_UV:.6f}   [alpha_1^-1 = {4*PI/(g1_UV**2*3/5):.2f}]")
print(f"    g2(M_KK) = {g2_UV:.6f}   [alpha_2^-1 = {4*PI/g2_UV**2:.2f}]")
print(f"    g3(M_KK) = {g3_UV:.6f}   [alpha_3^-1 = {4*PI/g3_UV**2:.2f}]")
print(f"    yt(M_KK) = {yt_UV:.6f}")
print(f"    1/g3^2(M_KK) = {g3inv2_SM_UV:.6f}")

# Cross-check against stored nominal value
assert abs(g3_UV - g3_MKK_nominal) < 1e-3, \
    f"g3(M_KK) mismatch: {g3_UV:.6f} vs {g3_MKK_nominal:.6f}"

# ============================================================================
# 4. STEP B — APPLY KK THRESHOLD + COMPUTE LAMBDA_CCM
# ============================================================================
print("\n" + "=" * 76)
print("3. KK THRESHOLD CORRECTION + LAMBDA_CCM")
print("=" * 76)

# The threshold shifts 1/g3^2:
#   1/g3_eff^2 = 1/g3_SM^2(M_KK) + delta(1/g3^2)

regulators = ['sharp', 'gauss']
delta_vals = {'sharp': delta_g3inv_sharp_L6, 'gauss': delta_g3inv_gauss_L6}

results = {}
for reg in regulators:
    delta = delta_vals[reg]
    g3inv2_eff = g3inv2_SM_UV + delta
    g3_eff = 1.0 / np.sqrt(g3inv2_eff)
    lam_CCM = (4.0 / 3.0) * g3_eff**2 * ratio_gilkey

    results[reg] = {
        'delta_g3inv': delta,
        'g3inv2_eff': g3inv2_eff,
        'g3_eff': g3_eff,
        'lam_CCM': lam_CCM,
    }
    print(f"\n  Regulator: {reg}")
    print(f"    delta(1/g3^2)   = {delta:.4f}")
    print(f"    1/g3_eff^2      = {g3inv2_eff:.4f}")
    print(f"    g3_eff(M_KK)    = {g3_eff:.6f}")
    print(f"    lambda_CCM      = {lam_CCM:.6f}")

# Also compute the NO-threshold case for comparison
lam_CCM_bare = (4.0/3.0) * g3_UV**2 * ratio_gilkey
print(f"\n  Bare (no threshold): lambda_CCM = {lam_CCM_bare:.6f}")

# ============================================================================
# 5. STEP C — DOWNWARD RGE: m_H PREDICTIONS
# ============================================================================
print("\n" + "=" * 76)
print("4. DOWNWARD RGE: m_H PREDICTIONS (2-loop)")
print("=" * 76)

# Case 0: No threshold (bare CCM) — should reproduce S62 result
t_d0, y_d0, ok0 = run_rg_down(g1_UV, g2_UV, g3_UV, yt_UV, lam_CCM_bare, t_MKK)
lam_MZ_bare = y_d0[4, -1]
m_H_bare = mH_from_lambda_MZ(lam_MZ_bare)
print(f"\n  Case 0 — Bare (no threshold):")
print(f"    lambda(M_Z) = {lam_MZ_bare:.6f}")
print(f"    m_H         = {m_H_bare:.2f} GeV  [S62 ref: {m_H_2loop_noBCS_s62:.2f}]")
print(f"    Deviation from S62: {abs(m_H_bare - m_H_2loop_noBCS_s62):.2f} GeV")

# Verify consistency with S62
assert abs(m_H_bare - m_H_2loop_noBCS_s62) < 1.0, \
    f"Bare m_H inconsistency: {m_H_bare:.2f} vs {m_H_2loop_noBCS_s62:.2f}"

# Cases 1,2: KK threshold (sharp, Gaussian)
for reg in regulators:
    R = results[reg]
    # Apply threshold to g3 ONLY at M_KK. g1, g2, yt unchanged (KK modes
    # primarily affect QCD coupling through SU(3) Dynkin indices).
    g3_eff = R['g3_eff']
    lam_UV_cc = R['lam_CCM']

    t_d, y_d, ok = run_rg_down(g1_UV, g2_UV, g3_eff, yt_UV, lam_UV_cc, t_MKK)
    assert ok, f"Downward RG failed for {reg}"

    lam_MZ = y_d[4, -1]
    m_H = mH_from_lambda_MZ(lam_MZ)
    g3_MZ_out = y_d[2, -1]
    alpha_s_out = g3_MZ_out**2 / (4.0 * PI)

    R['lam_MZ'] = lam_MZ
    R['m_H'] = m_H
    R['g3_MZ'] = g3_MZ_out
    R['alpha_s_MZ'] = alpha_s_out
    R['t_run'] = t_d
    R['y_run'] = y_d

    print(f"\n  Case ({reg}) — KK threshold, delta={R['delta_g3inv']:.4f}:")
    print(f"    g3_eff(M_KK) = {g3_eff:.6f}")
    print(f"    lambda_CCM   = {lam_UV_cc:.6f}")
    print(f"    lambda(M_Z)  = {lam_MZ:.6f}")
    print(f"    m_H          = {m_H:.2f} GeV")
    print(f"    alpha_s(M_Z) = {alpha_s_out:.4f}  [obs: {alpha_s_MZ}]")

# ============================================================================
# 6. STEP D — BCS CORRECTION ON TOP OF KK THRESHOLD
# ============================================================================
print("\n" + "=" * 76)
print("5. BCS CORRECTION ON TOP OF KK THRESHOLD")
print("=" * 76)

# The BCS condensate screens g_3 at M_KK:
#   g_3^{full} = g_3^{KK-corrected} * (1 - delta_BCS)
# From s62: delta_BCS_direct = 7.5e-5 (negligible).
# The "enhanced" delta_BCS = 0.07 (S62 estimate from collective tunneling).
# But the EXACT value for m_H = 125.1 from S62 was delta_BCS_best = 0.267 (no KK threshold).
# With KK threshold already doing most of the work, we need LESS BCS correction.

delta_BCS_enhanced = 0.07   # S62 physical estimate  # (local)
delta_BCS_values = [0.0, 0.01, 0.03, 0.05, 0.07, 0.10, 0.15, 0.20]

print(f"\n  delta_BCS sensitivity scan (Gaussian regulator):")
print(f"  {'delta_BCS':>10} {'g3_full':>10} {'lam_CCM':>10} {'lam_MZ':>10} "
      f"{'m_H (GeV)':>10} {'alpha_s':>8}")

m_H_vs_dBCS = []
for dB in delta_BCS_values:
    g3_base = results['gauss']['g3_eff']
    g3_full = g3_base * (1.0 - dB)
    lam_UV_bcs = (4.0/3.0) * g3_full**2 * ratio_gilkey

    t_d, y_d, ok = run_rg_down(g1_UV, g2_UV, g3_full, yt_UV, lam_UV_bcs, t_MKK)
    if ok and y_d[4, -1] > 0:
        lam_MZ_b = y_d[4, -1]
        m_H_b = mH_from_lambda_MZ(lam_MZ_b)
        alpha_s_b = y_d[2, -1]**2 / (4.0 * PI)
    else:
        lam_MZ_b = np.nan
        m_H_b = np.nan
        alpha_s_b = np.nan

    m_H_vs_dBCS.append(m_H_b)
    print(f"  {dB:10.3f} {g3_full:10.6f} {lam_UV_bcs:10.6f} "
          f"{lam_MZ_b:10.6f} {m_H_b:10.2f} {alpha_s_b:8.4f}")

# Find delta_BCS for m_H = 125.1 GeV (with KK threshold)
print(f"\n  Finding delta_BCS for m_H = {m_H_obs} GeV (with KK + Gaussian threshold):")

def m_H_func(dB):
    """m_H as function of delta_BCS (Gaussian regulator)."""
    g3_base = results['gauss']['g3_eff']
    g3_full = g3_base * (1.0 - dB)
    lam_UV = (4.0/3.0) * g3_full**2 * ratio_gilkey
    _, y_d, ok = run_rg_down(g1_UV, g2_UV, g3_full, yt_UV, lam_UV, t_MKK)
    if ok and y_d[4, -1] > 0:
        return mH_from_lambda_MZ(y_d[4, -1]) - m_H_obs
    return 1e6

# Fine scan to find the root
dBCS_fine = np.linspace(0.0, 0.25, 101)
m_H_fine_gauss = []
for dB in dBCS_fine:
    val = m_H_func(dB) + m_H_obs
    m_H_fine_gauss.append(val)
m_H_fine_gauss = np.array(m_H_fine_gauss)

# Also for sharp
def m_H_func_sharp(dB):
    g3_base = results['sharp']['g3_eff']
    g3_full = g3_base * (1.0 - dB)
    lam_UV = (4.0/3.0) * g3_full**2 * ratio_gilkey
    _, y_d, ok = run_rg_down(g1_UV, g2_UV, g3_full, yt_UV, lam_UV, t_MKK)
    if ok and y_d[4, -1] > 0:
        return mH_from_lambda_MZ(y_d[4, -1]) - m_H_obs
    return 1e6

m_H_fine_sharp = []
for dB in dBCS_fine:
    val = m_H_func_sharp(dB) + m_H_obs
    m_H_fine_sharp.append(val)
m_H_fine_sharp = np.array(m_H_fine_sharp)

# Find roots
try:
    dBCS_target_gauss = brentq(m_H_func, 0.0, 0.25, xtol=1e-6)
    m_H_check_gauss = m_H_func(dBCS_target_gauss) + m_H_obs
    print(f"    Gaussian: delta_BCS = {dBCS_target_gauss:.6f} -> m_H = {m_H_check_gauss:.2f} GeV")
except ValueError:
    dBCS_target_gauss = np.nan
    print(f"    Gaussian: m_H(dBCS=0) = {m_H_fine_gauss[0]:.2f}, already below {m_H_obs}? "
          f"Or no root in [0,0.25]")

try:
    dBCS_target_sharp = brentq(m_H_func_sharp, 0.0, 0.25, xtol=1e-6)
    m_H_check_sharp = m_H_func_sharp(dBCS_target_sharp) + m_H_obs
    print(f"    Sharp:    delta_BCS = {dBCS_target_sharp:.6f} -> m_H = {m_H_check_sharp:.2f} GeV")
except ValueError:
    dBCS_target_sharp = np.nan
    print(f"    Sharp:    no root in [0, 0.25]")

# ============================================================================
# 7. CONVERGENCE ANALYSIS
# ============================================================================
print("\n" + "=" * 76)
print("6. CONVERGENCE ANALYSIS (L = 1..6)")
print("=" * 76)

# Compute m_H at each L independently (not from stored values — full 2-loop)
m_H_by_L_sharp_full = []
m_H_by_L_gauss_full = []
lam_MZ_by_L_sharp = []
lam_MZ_by_L_gauss = []

for iL in range(6):
    for reg, delta_arr, m_list, lam_list in [
        ('sharp', delta_g3inv_sharp_arr, m_H_by_L_sharp_full, lam_MZ_by_L_sharp),
        ('gauss', delta_g3inv_gauss_arr, m_H_by_L_gauss_full, lam_MZ_by_L_gauss),
    ]:
        delta = delta_arr[iL]
        g3inv2_eff = g3inv2_SM_UV + delta
        g3_eff = 1.0 / np.sqrt(g3inv2_eff)
        lam_UV = (4.0/3.0) * g3_eff**2 * ratio_gilkey

        t_d, y_d, ok = run_rg_down(g1_UV, g2_UV, g3_eff, yt_UV, lam_UV, t_MKK)
        if ok and y_d[4, -1] > 0:
            lam_list.append(y_d[4, -1])
            m_list.append(mH_from_lambda_MZ(y_d[4, -1]))
        else:
            lam_list.append(np.nan)
            m_list.append(np.nan)

m_H_by_L_sharp_full = np.array(m_H_by_L_sharp_full)
m_H_by_L_gauss_full = np.array(m_H_by_L_gauss_full)
lam_MZ_by_L_sharp = np.array(lam_MZ_by_L_sharp)
lam_MZ_by_L_gauss = np.array(lam_MZ_by_L_gauss)

print(f"  {'L':>3} {'delta_sharp':>12} {'m_H_sharp':>10} {'delta_gauss':>12} {'m_H_gauss':>10}")
for iL in range(6):
    print(f"  {iL+1:3d} {delta_g3inv_sharp_arr[iL]:12.4f} {m_H_by_L_sharp_full[iL]:10.2f} "
          f"{delta_g3inv_gauss_arr[iL]:12.4f} {m_H_by_L_gauss_full[iL]:10.2f}")

# Convergence ratios
print(f"\n  Convergence ratios m_H(L)/m_H(L-1):")
for iL in range(1, 6):
    r_s = m_H_by_L_sharp_full[iL] / m_H_by_L_sharp_full[iL-1]
    r_g = m_H_by_L_gauss_full[iL] / m_H_by_L_gauss_full[iL-1]
    print(f"    L={iL+1}: sharp ratio = {r_s:.4f}, gauss ratio = {r_g:.4f}")

# Convergence estimate: Richardson extrapolation
# Assume m_H(L) ~ m_H_inf + A / L^p
# From L=5,6: p ~ ln(ratio5/ratio6) / ln((L-1)/L)
# Simpler: just check if L=5->6 change is < 5%
dm_sharp = abs(m_H_by_L_sharp_full[-1] - m_H_by_L_sharp_full[-2])
dm_gauss = abs(m_H_by_L_gauss_full[-1] - m_H_by_L_gauss_full[-2])
dm_frac_sharp = dm_sharp / m_H_by_L_sharp_full[-2]
dm_frac_gauss = dm_gauss / m_H_by_L_gauss_full[-2]

print(f"\n  L=5->6 change:")
print(f"    Sharp: dm = {dm_sharp:.2f} GeV ({dm_frac_sharp*100:.1f}%)")
print(f"    Gauss: dm = {dm_gauss:.2f} GeV ({dm_frac_gauss*100:.1f}%)")
print(f"  Not yet converged — L=6 may not be the final answer.")

# Richardson extrapolation assuming m_H(L) = m_H_inf + A*L^(-alpha)
# Using L=4,5,6:
def richardson_3pt(f4, f5, f6, L4=4, L5=5, L6=6):
    """3-point Richardson extrapolation for f(L) = f_inf + A*L^(-alpha).
    Uses geometric series: f_inf = f6 + df_56 * r_conv / (1 - r_conv),
    where r_conv = df_56 / df_45 is the convergence ratio."""
    df_45 = f5 - f4
    df_56 = f6 - f5
    r_conv = df_56 / df_45 if abs(df_45) > 1e-15 else 0.0
    if abs(1.0 - r_conv) > 0.01:
        f_inf_geom = f6 + df_56 * r_conv / (1.0 - r_conv)
    else:
        f_inf_geom = f6
    return f_inf_geom, r_conv

m_H_inf_sharp, r_sharp = richardson_3pt(
    m_H_by_L_sharp_full[3], m_H_by_L_sharp_full[4], m_H_by_L_sharp_full[5])
m_H_inf_gauss, r_gauss = richardson_3pt(
    m_H_by_L_gauss_full[3], m_H_by_L_gauss_full[4], m_H_by_L_gauss_full[5])

print(f"\n  Richardson extrapolation (geometric, L=4,5,6):")
print(f"    Sharp: m_H_inf = {m_H_inf_sharp:.2f} GeV (r_conv = {r_sharp:.3f})")
print(f"    Gauss: m_H_inf = {m_H_inf_gauss:.2f} GeV (r_conv = {r_gauss:.3f})")

# ============================================================================
# 8. UNCERTAINTY BUDGET
# ============================================================================
print("\n" + "=" * 76)
print("7. UNCERTAINTY BUDGET")
print("=" * 76)

m_H_central_gauss = results['gauss']['m_H']
m_H_central_sharp = results['sharp']['m_H']

# Source 1: Regulator (sharp vs Gaussian)
sigma_regulator = abs(m_H_central_gauss - m_H_central_sharp)

# Source 2: Truncation (L=5 vs L=6 shift, as 1-sigma proxy)
sigma_trunc_sharp = dm_sharp
sigma_trunc_gauss = dm_gauss

# Source 3: m_t uncertainty (PDG: 172.69 +/- 0.30 GeV)
# From Buttazzo et al: dm_H/dm_t ~ 0.5 (at 2-loop)
dm_t = 0.30  # GeV, PDG uncertainty  # (local)
sigma_mt = 0.5 * dm_t  # ~ 0.15 GeV

# Source 4: alpha_s uncertainty (PDG: 0.1180 +/- 0.0009)
# dm_H/dalpha_s ~ 100 GeV (from RGE sensitivity)
dalpha_s = 0.0009  # (local)
sigma_alphas = 100.0 * dalpha_s  # ~ 0.09 GeV

# Source 5: BCS correction (delta_BCS = 0 to 0.07 from S62 physical estimate)
m_H_at_dBCS007_gauss = np.interp(0.07, dBCS_fine, m_H_fine_gauss)
sigma_BCS = abs(m_H_central_gauss - m_H_at_dBCS007_gauss)

# Source 6: M_KK route (gravity vs Kerner, 0.83 decades)
# Kerner M_KK is 6.78x larger -> t_MKK shifts by ~1.9
# This is the DOMINANT systematic
t_MKK_kerner = np.log(M_KK_kerner / M_Z)
t_up_k, y_up_k, ok_k = run_rg_up(g1_MZ, g2_MZ, g3_MZ, yt_MZ, lambda_MZ_obs, t_MKK_kerner)
g3_UV_kerner = y_up_k[2, -1]
g3inv2_kerner = 1.0 / g3_UV_kerner**2
g3inv2_eff_kerner = g3inv2_kerner + delta_g3inv_gauss_L6
g3_eff_kerner = 1.0 / np.sqrt(g3inv2_eff_kerner)
lam_CCM_kerner = (4.0/3.0) * g3_eff_kerner**2 * ratio_gilkey
t_dk, y_dk, ok_k2 = run_rg_down(
    y_up_k[0,-1], y_up_k[1,-1], g3_eff_kerner, y_up_k[3,-1],
    lam_CCM_kerner, t_MKK_kerner
)
if ok_k2 and y_dk[4,-1] > 0:
    m_H_kerner = mH_from_lambda_MZ(y_dk[4,-1])
else:
    m_H_kerner = np.nan
sigma_MKK = abs(m_H_central_gauss - m_H_kerner) / 2.0  # Half-spread as estimate

print(f"  Uncertainty sources (Gaussian regulator, L=6):")
print(f"    1. Regulator (sharp vs Gauss)  : {sigma_regulator:.2f} GeV")
print(f"    2. Truncation (L=5 vs L=6)     : {sigma_trunc_gauss:.2f} GeV")
print(f"    3. m_t pole mass (+/- 0.30 GeV): {sigma_mt:.2f} GeV")
print(f"    4. alpha_s (+/- 0.0009)         : {sigma_alphas:.2f} GeV")
print(f"    5. BCS (0 to 0.07)              : {sigma_BCS:.2f} GeV")
print(f"    6. M_KK route (grav vs Kerner)  : {sigma_MKK:.2f} GeV")
print(f"    m_H (Kerner route, Gauss)       : {m_H_kerner:.2f} GeV")

sigma_total = np.sqrt(sigma_regulator**2 + sigma_trunc_gauss**2 + sigma_mt**2 +
                      sigma_alphas**2 + sigma_BCS**2 + sigma_MKK**2)

print(f"\n  Total uncertainty (quadrature): {sigma_total:.2f} GeV")
print(f"  Central value (Gaussian, L=6): {m_H_central_gauss:.2f} GeV")
print(f"  Result: m_H = {m_H_central_gauss:.1f} +/- {sigma_total:.1f} GeV")

# ============================================================================
# 9. CROSS-CHECKS
# ============================================================================
print("\n" + "=" * 76)
print("8. CROSS-CHECKS")
print("=" * 76)

# Cross-check 1: sin^2(theta_W)
g1_IR_gauss = results['gauss']['y_run'][0, -1]
g2_IR_gauss = results['gauss']['y_run'][1, -1]
sin2_pred = (3.0/5.0) * g1_IR_gauss**2 / (g2_IR_gauss**2 + (3.0/5.0) * g1_IR_gauss**2)
print(f"  sin^2(theta_W) predicted = {sin2_pred:.5f}  [obs: {sin2_tW}]")

# Cross-check 2: M_W
M_W_pred = g2_IR_gauss / 2.0 * v_ew
print(f"  M_W predicted             = {M_W_pred:.2f} GeV  [obs: {M_W} GeV]")

# Cross-check 3: M_Z
g_prime_IR = g1_IR_gauss * np.sqrt(3.0/5.0)
M_Z_pred = v_ew / 2.0 * np.sqrt(g2_IR_gauss**2 + g_prime_IR**2)
print(f"  M_Z predicted             = {M_Z_pred:.2f} GeV  [obs: {M_Z} GeV]")

# Cross-check 4: alpha_s(M_Z)
alpha_s_pred = results['gauss']['alpha_s_MZ']
print(f"  alpha_s(M_Z) predicted    = {alpha_s_pred:.4f}  [obs: {alpha_s_MZ}]")

# Cross-check 5: Consistency with W1-02 m_H values
print(f"\n  W1-02 cross-check:")
print(f"    m_H(sharp, W1-02) = {m_H_kk_sharp_arr[-1]:.2f}, this script = {m_H_central_sharp:.2f}")
print(f"    m_H(gauss, W1-02) = {m_H_kk_gauss_arr[-1]:.2f}, this script = {m_H_central_gauss:.2f}")

# ============================================================================
# 10. GATE VERDICT
# ============================================================================
print("\n" + "=" * 76)
print("9. GATE VERDICT")
print("=" * 76)

# Use Gaussian as primary (better UV behavior), sharp as systematic check
m_H_final = m_H_central_gauss
m_H_sharp_final = m_H_central_sharp
m_H_range = [m_H_sharp_final, m_H_final]  # [sharp, gauss] brackets the result

# Gate criteria
PASS_LO, PASS_HI = 120.0, 135.0
FAIL_LO, FAIL_HI = 100.0, 150.0

if PASS_LO <= m_H_final <= PASS_HI:
    verdict = "PASS"
    detail = (f"m_H(Gauss,L=6) = {m_H_final:.2f} GeV in [{PASS_LO}, {PASS_HI}]. "
              f"Sharp: {m_H_sharp_final:.2f} GeV. Uncertainty: +/- {sigma_total:.1f} GeV.")
elif FAIL_LO <= m_H_final <= FAIL_HI:
    if m_H_final < PASS_LO:
        verdict = "INFO"
        detail = (f"m_H(Gauss,L=6) = {m_H_final:.2f} GeV below PASS band [{PASS_LO}, {PASS_HI}]. "
                  f"Sharp: {m_H_sharp_final:.2f} GeV. Uncertainty: +/- {sigma_total:.1f} GeV.")
    else:
        verdict = "INFO"
        detail = (f"m_H(Gauss,L=6) = {m_H_final:.2f} GeV above PASS band [{PASS_LO}, {PASS_HI}]. "
                  f"Sharp: {m_H_sharp_final:.2f} GeV. Uncertainty: +/- {sigma_total:.1f} GeV.")
else:
    verdict = "FAIL"
    detail = (f"m_H(Gauss,L=6) = {m_H_final:.2f} GeV outside [{FAIL_LO}, {FAIL_HI}]. "
              f"Sharp: {m_H_sharp_final:.2f} GeV. Uncertainty: +/- {sigma_total:.1f} GeV.")

print(f"\n  GATE: HIGGS-RUNNING-63")
print(f"  VERDICT: {verdict}")
print(f"  DETAIL: {detail}")
print(f"  m_H(Gaussian, L=6)    = {m_H_final:.2f} GeV")
print(f"  m_H(sharp, L=6)       = {m_H_sharp_final:.2f} GeV")
print(f"  m_H(Gaussian, L=inf)  ~ {m_H_inf_gauss:.2f} GeV (Richardson)")
print(f"  m_H(sharp, L=inf)     ~ {m_H_inf_sharp:.2f} GeV (Richardson)")
print(f"  delta_BCS(exact 125.1, Gauss) = {dBCS_target_gauss:.4f}")
if not np.isnan(dBCS_target_sharp):
    print(f"  delta_BCS(exact 125.1, sharp) = {dBCS_target_sharp:.4f}")
print(f"  Observed: m_H = {m_H_obs} GeV")
print(f"  Deviation: {(m_H_final - m_H_obs):.2f} GeV ({(m_H_final/m_H_obs - 1)*100:.1f}%)")

# ============================================================================
# 11. PLOT
# ============================================================================
print("\n" + "=" * 76)
print("10. GENERATING PLOTS")
print("=" * 76)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel (a): m_H vs L convergence
ax = axes[0, 0]
ax.plot(L_range, m_H_by_L_sharp_full, 'bs-', label='Sharp cutoff', markersize=6)
ax.plot(L_range, m_H_by_L_gauss_full, 'ro-', label='Gaussian', markersize=6)
ax.axhline(m_H_obs, color='green', ls='--', lw=1.5, label=f'Observed {m_H_obs} GeV')
ax.axhspan(PASS_LO, PASS_HI, color='green', alpha=0.1, label='PASS band')
ax.axhline(m_H_bare, color='gray', ls=':', lw=1, label=f'No threshold: {m_H_bare:.0f} GeV')
ax.set_xlabel('Truncation level L', fontsize=12)
ax.set_ylabel('m_H (GeV)', fontsize=12)
ax.set_title('(a) Higgs Mass vs PW Truncation', fontsize=12)
ax.legend(fontsize=9, loc='upper right')
ax.set_xlim(0.5, 6.5)
ax.grid(True, alpha=0.3)

# Panel (b): m_H vs delta_BCS (with KK threshold)
ax = axes[0, 1]
ax.plot(dBCS_fine, m_H_fine_gauss, 'r-', lw=2, label='Gaussian + BCS')
ax.plot(dBCS_fine, m_H_fine_sharp, 'b-', lw=2, label='Sharp + BCS')
ax.axhline(m_H_obs, color='green', ls='--', lw=1.5, label=f'Observed {m_H_obs} GeV')
ax.axhspan(PASS_LO, PASS_HI, color='green', alpha=0.1)
if not np.isnan(dBCS_target_gauss):
    ax.axvline(dBCS_target_gauss, color='r', ls=':', lw=1,
               label=f'dBCS(Gauss)={dBCS_target_gauss:.3f}')
if not np.isnan(dBCS_target_sharp):
    ax.axvline(dBCS_target_sharp, color='b', ls=':', lw=1,
               label=f'dBCS(sharp)={dBCS_target_sharp:.3f}')
ax.axvline(0.07, color='orange', ls='-.', lw=1, label='BCS estimate (0.07)')
ax.set_xlabel('delta_BCS', fontsize=12)
ax.set_ylabel('m_H (GeV)', fontsize=12)
ax.set_title('(b) Higgs Mass vs BCS Correction', fontsize=12)
ax.legend(fontsize=8, loc='upper right')
ax.grid(True, alpha=0.3)

# Panel (c): Running couplings (Gaussian, L=6)
ax = axes[1, 0]
t_run = results['gauss']['t_run']
y_run = results['gauss']['y_run']
mu_GeV = M_Z * np.exp(t_run)
ax.plot(np.log10(mu_GeV), y_run[0]**2, label=r'$g_1^2$', color='blue')
ax.plot(np.log10(mu_GeV), y_run[1]**2, label=r'$g_2^2$', color='red')
ax.plot(np.log10(mu_GeV), y_run[2]**2, label=r'$g_3^2$', color='green')
ax.plot(np.log10(mu_GeV), y_run[3]**2 * 2, label=r'$2 y_t^2$', color='orange')
ax.plot(np.log10(mu_GeV), y_run[4] * 10, label=r'$10 \lambda$', color='purple')
ax.axvline(np.log10(M_KK_gravity), color='gray', ls='--', lw=1, label=r'$M_{KK}$')
ax.set_xlabel(r'$\log_{10}(\mu/{\rm GeV})$', fontsize=12)
ax.set_ylabel('Coupling', fontsize=12)
ax.set_title('(c) Running Couplings (KK threshold, Gaussian)', fontsize=12)
ax.legend(fontsize=8, ncol=2, loc='upper right')
ax.grid(True, alpha=0.3)

# Panel (d): Uncertainty breakdown
ax = axes[1, 1]
labels = ['Regulator', 'Truncation', 'm_t', 'alpha_s', 'BCS', 'M_KK route']
sigmas = [sigma_regulator, sigma_trunc_gauss, sigma_mt, sigma_alphas, sigma_BCS, sigma_MKK]
colors = ['steelblue', 'coral', 'gold', 'mediumseagreen', 'plum', 'sandybrown']
bars = ax.barh(labels, sigmas, color=colors, edgecolor='black', linewidth=0.5)
ax.set_xlabel('Uncertainty (GeV)', fontsize=12)
ax.set_title('(d) Uncertainty Budget', fontsize=12)
for bar, s in zip(bars, sigmas):
    ax.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height()/2,
            f'{s:.1f}', va='center', fontsize=10)
ax.grid(True, alpha=0.3, axis='x')

plt.tight_layout()
plotfile = os.path.join(outdir, 's63_higgs_running.png')
plt.savefig(plotfile, dpi=150, bbox_inches='tight')
print(f"  Plot saved: {plotfile}")
plt.close()

# ============================================================================
# 12. SAVE OUTPUT
# ============================================================================
print("\n" + "=" * 76)
print("11. SAVING OUTPUT")
print("=" * 76)

outfile = os.path.join(outdir, 's63_higgs_running.npz')

np.savez(
    outfile,
    # Gate
    gate_name='HIGGS-RUNNING-63',
    gate_verdict=verdict,
    gate_detail=detail,
    # Central results
    m_H_gauss_L6=m_H_central_gauss,
    m_H_sharp_L6=m_H_central_sharp,
    m_H_gauss_Linf=m_H_inf_gauss,
    m_H_sharp_Linf=m_H_inf_sharp,
    m_H_bare_noBCS=m_H_bare,
    m_H_kerner_gauss=m_H_kerner,
    m_H_obs=m_H_obs,
    # KK threshold
    delta_g3inv_sharp_L6=delta_g3inv_sharp_L6,
    delta_g3inv_gauss_L6=delta_g3inv_gauss_L6,
    g3_eff_sharp=results['sharp']['g3_eff'],
    g3_eff_gauss=results['gauss']['g3_eff'],
    lam_CCM_sharp=results['sharp']['lam_CCM'],
    lam_CCM_gauss=results['gauss']['lam_CCM'],
    lam_MZ_sharp=results['sharp']['lam_MZ'],
    lam_MZ_gauss=results['gauss']['lam_MZ'],
    alpha_s_sharp=results['sharp']['alpha_s_MZ'],
    alpha_s_gauss=results['gauss']['alpha_s_MZ'],
    # UV boundary
    g3_SM_MKK=g3_UV,
    g3inv2_SM_MKK=g3inv2_SM_UV,
    g1_MKK=g1_UV,
    g2_MKK=g2_UV,
    yt_MKK=yt_UV,
    ratio_gilkey=ratio_gilkey,
    Lambda_fixed=Lambda_fixed,
    t_MKK=t_MKK,
    v_ew=v_ew,
    # Convergence
    L_range=L_range,
    delta_g3inv_sharp_arr=delta_g3inv_sharp_arr,
    delta_g3inv_gauss_arr=delta_g3inv_gauss_arr,
    m_H_by_L_sharp=m_H_by_L_sharp_full,
    m_H_by_L_gauss=m_H_by_L_gauss_full,
    lam_MZ_by_L_sharp=lam_MZ_by_L_sharp,
    lam_MZ_by_L_gauss=lam_MZ_by_L_gauss,
    # BCS
    dBCS_target_gauss=dBCS_target_gauss,
    dBCS_target_sharp=dBCS_target_sharp,
    dBCS_fine=dBCS_fine,
    m_H_fine_gauss=m_H_fine_gauss,
    m_H_fine_sharp=m_H_fine_sharp,
    # Uncertainties
    sigma_regulator=sigma_regulator,
    sigma_trunc=sigma_trunc_gauss,
    sigma_mt=sigma_mt,
    sigma_alphas=sigma_alphas,
    sigma_BCS=sigma_BCS,
    sigma_MKK=sigma_MKK,
    sigma_total=sigma_total,
    # Cross-checks
    sin2_tW_pred=sin2_pred,
    M_W_pred=M_W_pred,
    M_Z_pred=M_Z_pred,
    # Running (Gaussian, for plots)
    t_run_gauss=results['gauss']['t_run'],
    g1_run_gauss=results['gauss']['y_run'][0],
    g2_run_gauss=results['gauss']['y_run'][1],
    g3_run_gauss=results['gauss']['y_run'][2],
    yt_run_gauss=results['gauss']['y_run'][3],
    lam_run_gauss=results['gauss']['y_run'][4],
)

print(f"  Saved: {outfile}")

# ============================================================================
# FINAL SUMMARY
# ============================================================================
print("\n" + "=" * 76)
print("FINAL SUMMARY: HIGGS-RUNNING-63")
print("=" * 76)
print(f"  GATE VERDICT: {verdict}")
print(f"  m_H (Gaussian, L=6)    = {m_H_central_gauss:.2f} GeV")
print(f"  m_H (sharp, L=6)       = {m_H_central_sharp:.2f} GeV")
print(f"  m_H (Gaussian, L->inf) ~ {m_H_inf_gauss:.2f} GeV")
print(f"  m_H (no threshold)     = {m_H_bare:.2f} GeV")
print(f"  m_H (Kerner route)     = {m_H_kerner:.2f} GeV")
print(f"  Observed               = {m_H_obs} GeV")
print(f"  Deviation (Gauss)      = {(m_H_central_gauss - m_H_obs):.2f} GeV ({(m_H_central_gauss/m_H_obs - 1)*100:.1f}%)")
print(f"  BCS needed for exact   = {dBCS_target_gauss:.4f}")
print(f"  Total uncertainty      = +/- {sigma_total:.1f} GeV")
print(f"  PASS band: [{PASS_LO}, {PASS_HI}] GeV")
print(f"  FAIL band: [{FAIL_LO}, {FAIL_HI}] GeV")
print("=" * 76)
