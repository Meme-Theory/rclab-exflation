#!/usr/bin/env python3
"""
s70_f0_alpha_s.py — F0-ALPHA-S-70
Spectral function normalization scan for alpha_s.

Physics
-------
The framework extracts alpha_s(M_Z) = 0.022 from the spectral action, a factor
5.4x below the observed 0.1180. The extraction uses:

    alpha_3(M_KK) = 2 * pi^2 * f_0 / a_4

where a_4 = 1350.72 is the fourth Seeley-DeWitt coefficient of D_K on Jensen-
deformed SU(3) at the fold. Then alpha_3(M_KK) is RG-run from M_KK to M_Z
using 2-loop QCD beta functions with quark mass thresholds at m_t, m_b, m_c.

The KK threshold correction shifts the effective coupling at M_KK:
    1/g_3^2(M_KK) = 1/g_3^2(tree, f_0) + S_inf
where S_inf = 2.895 is the Aitken-extrapolated Gaussian-regulated threshold sum
(from S66/S69 computations).

The question: does a value of f_0 in [0.5, 5.0] simultaneously give
alpha_s(M_Z) in [0.10, 0.13] AND m_H in [120, 135] GeV?

Method
------
1. Tree-level SA: alpha_3(tree) = 2*pi^2*f_0/a_4
   Equivalently: 1/g_3^2(tree) = a_4/(8*pi^3*f_0)

2. KK threshold: 1/g_3^2(M_KK) = 1/g_3^2(tree) + S_inf

3. CCM Higgs quartic: lambda_CCM(M_KK) = (4/3)*g_3^2(M_KK)*(a_4/a_2)
   This depends on f_0 through g_3^2.

4. 2-loop RG: run (g1, g2, g3, yt, lambda) from M_KK to M_Z.
   g1, g2, yt at M_KK are fixed from SM upward running (f_0-independent).
   g3 and lambda at M_KK come from the SA/CCM matching (f_0-dependent).

5. Extract alpha_s(M_Z) and m_H = sqrt(2*lambda(M_Z))*v_ew.

Gate: F0-ALPHA-S-70
  PASS: Consistent f_0 exists in [0.5, 5.0] with alpha_s in [0.10, 0.13]
        AND m_H in [120, 135] GeV
  FAIL: No such f_0 exists (alpha_s tension is structural, not normalization)
  INFO: f_0 exists but outside [0.5, 5.0] or requires fine-tuning > 10%

Author: baptista-spacetime-analyst
Session: S70 W1-B
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
    tau_fold,
)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

print("=" * 80)
print("F0-ALPHA-S-70: Spectral Function Normalization Scan for alpha_s")
print("=" * 80)

# =============================================================================
# 1. PHYSICAL CONSTANTS AND UPSTREAM DATA
# =============================================================================
print("\n" + "=" * 80)
print("1. PHYSICAL CONSTANTS AND UPSTREAM DATA")
print("=" * 80)

# PDG / observational
# m_H_obs = 125.10        # GeV  # S72: now imported from canonical_constants
v_ew = 246.22            # GeV  # S72: intentionally differs from canonical v_ew=246.0 (Fermi-extracted)
# alpha_s_MZ_obs = 0.1180  # S72: now imported from canonical_constants
alpha_em_MZ = 1.0 / alpha_em_MZ_inv
sin2_tW = sin2_thetaW_MSbar
# m_t_pole = 172.69        # GeV  # S72: now imported from canonical_constants
# m_b_pole = 4.18          # GeV (1S mass)  # S72: this is actually m_b_1S, not m_b_pole (canonical: m_b_pole=4.78, m_b_1S=4.18)
m_b_pole = m_b_1S  # S72: script uses 1S mass but calls it m_b_pole — preserving downstream name
m_c_pole = 1.27          # GeV  # (local)

# SM couplings at M_Z
g1_MZ = np.sqrt(5.0 / 3.0) * np.sqrt(4 * PI * alpha_em_MZ / (1.0 - sin2_tW))
g2_MZ = np.sqrt(4 * PI * alpha_em_MZ / sin2_tW)
g3_MZ = np.sqrt(4 * PI * alpha_s_MZ_obs)
m_t_MSbar = m_t_pole * (1.0 - 4.0 * alpha_s_MZ_obs / (3.0 * PI))
yt_MZ = np.sqrt(2) * m_t_MSbar / v_ew
lambda_MZ_obs = m_H_obs**2 / (2.0 * v_ew**2)

# Scales
t_MKK_gravity = np.log(M_KK_gravity / M_Z)
t_MKK_kerner = np.log(M_KK_kerner / M_Z)

# Load upstream: KK threshold Aitken sum
d_kk = np.load(os.path.join(SCRIPT_DIR, 's64_kk_threshold.npz'), allow_pickle=True)
S_inf_gauss = float(d_kk['delta_primary'])         # 2.353 at L=6
g3_inv2_nominal_SM = float(d_kk['g3_inv2_nominal'])  # 3.755
Lambda_fixed = float(d_kk['Lambda_fixed'])          # 2.048

# Load S69 for Aitken-extrapolated S_inf
d_s69 = np.load(os.path.join(SCRIPT_DIR, 's69_kk_higgs.npz'), allow_pickle=True)
S_inf_bare = float(d_s69['S_inf_bare'])             # 2.895 (Aitken extrapolation)
S_inf_sector = float(d_s69['S_inf_sector'])         # 2.887 (sector-resolved BCS)
ratio_gilkey = float(d_s69['ratio_gilkey'])         # 0.4140

# Spectral constants
a_4 = a4_fold  # 1350.72
a_2 = a2_fold  # 2776.17
a_0 = a0_fold  # 6440.0

print(f"  M_KK (gravity)  = {M_KK_gravity:.6e} GeV")
print(f"  M_KK (Kerner)   = {M_KK_kerner:.6e} GeV")
print(f"  t_MKK (gravity) = ln(M_KK/M_Z) = {t_MKK_gravity:.4f}")
print(f"  a_0 = {a_0:.2f}, a_2 = {a_2:.2f}, a_4 = {a_4:.4f}")
print(f"  ratio_gilkey (a_4/a_2) = {ratio_gilkey:.6f}")
print(f"  S_inf (L=6 Gauss)  = {S_inf_gauss:.6f}")
print(f"  S_inf (Aitken bare) = {S_inf_bare:.6f}")
print(f"  g3_inv2_nominal (SM running) = {g3_inv2_nominal_SM:.6f}")
print(f"  Observed: alpha_s(M_Z) = {alpha_s_MZ_obs}, m_H = {m_H_obs} GeV")

# =============================================================================
# 2. TREE-LEVEL SPECTRAL ACTION COUPLING
# =============================================================================
print("\n" + "=" * 80)
print("2. TREE-LEVEL SPECTRAL ACTION: alpha_3(M_KK) vs f_0")
print("=" * 80)

# The spectral action on M4 x SU(3)_Jensen gives:
#
#   S_YM = (f_0 / (2*pi^2)) * integral |F_mu_nu|^2 * sqrt(g) d^4x
#
# (factor 1/(2*pi^2) from 4D heat kernel normalization)
# Matching to S_YM = (1/(4*g^2)) * integral |F|^2:
#   1/(4*g^2) = f_0/(2*pi^2)
#   => 1/g^2 = 2*f_0/pi^2
#
# BUT: this is the FULL a_4 normalization. In the Baptista framework,
# a_4 includes the KK multiplicity of modes. The correct normalization
# for the SU(3)_color gauge coupling is:
#
#   alpha_3(tree) = 2*pi^2 * f_0 / a_4    [as specified in the prompt]
#
# This gives: g_3^2(tree) = 4*pi*alpha_3 = 8*pi^3*f_0/a_4
#             1/g_3^2(tree) = a_4/(8*pi^3*f_0)
#
# Cross-check at f_0 = 1:
#   alpha_3 = 2*pi^2/1350.72 = 0.01461
#   g_3 = 0.429, 1/g_3^2 = 5.445
#   After threshold: 1/g_3^2(eff) = 5.445 + 2.895 = 8.340
#   alpha_3(eff) = 1/(4*pi*8.340) = 0.00955
#   1-loop: 1/alpha_s(M_Z) = 4*pi*8.340 - 38.3 = 66.5
#   alpha_s(M_Z) ~ 0.015 (rough estimate, matches S69's 0.022 order)

# Reference: at the standard normalization f_0 = 1.0:
alpha_3_tree_ref = 2 * PI**2 * 1.0 / a_4
g3_tree_ref = np.sqrt(4 * PI * alpha_3_tree_ref)

print(f"  SA tree-level formula: alpha_3(tree) = 2*pi^2*f_0 / a_4")
print(f"  At f_0 = 1.0:")
print(f"    alpha_3(tree) = {alpha_3_tree_ref:.6f}")
print(f"    g_3(tree)     = {g3_tree_ref:.6f}")
print(f"    1/g_3^2(tree) = {1/g3_tree_ref**2:.4f}")

# What f_0 reproduces the SM-running g3 at M_KK (without threshold)?
f0_SM_match = g3_inv2_nominal_SM * 8 * PI**3 / a_4
alpha_3_SM = 1.0 / (4 * PI * g3_inv2_nominal_SM)
print(f"\n  SM g_3 at M_KK: 1/g^2 = {g3_inv2_nominal_SM:.4f}, alpha_3 = {alpha_3_SM:.6f}")
print(f"  f_0 to match SM tree = {f0_SM_match:.4f}")

# =============================================================================
# 3. TWO-LOOP SM BETA FUNCTIONS
# =============================================================================
# (Copied from S69/S64 for consistency)


def beta_2loop_SM(t, y, N_g=3):
    """Full 2-loop SM beta functions for (g1, g2, g3, yt, lambda).
    Conventions: GUT-normalized g1 = sqrt(5/3)*g', t = ln(mu/M_Z).
    From Arason et al. (1992), Machacek & Vaughn (1983-84)."""
    g1, g2, g3, yt, lam = y
    g1sq, g2sq, g3sq = g1**2, g2**2, g3**2
    ytsq = yt**2
    b16 = 16.0 * PI**2
    b16sq = b16**2

    # Gauge couplings: 1-loop + 2-loop
    dg1 = g1**3 / b16 * (41.0 / 10.0) + g1**3 / b16sq * (
        199.0 / 50.0 * g1sq + 27.0 / 10.0 * g2sq + 44.0 / 5.0 * g3sq
        - 17.0 / 10.0 * ytsq)
    dg2 = g2**3 / b16 * (-19.0 / 6.0) + g2**3 / b16sq * (
        9.0 / 10.0 * g1sq + 35.0 / 6.0 * g2sq + 12.0 * g3sq
        - 3.0 / 2.0 * ytsq)
    dg3 = g3**3 / b16 * (-7.0) + g3**3 / b16sq * (
        11.0 / 10.0 * g1sq + 9.0 / 2.0 * g2sq - 26.0 * g3sq
        - 2.0 * ytsq)

    # Top Yukawa
    dyt = yt / b16 * (9.0 / 2.0 * ytsq - 17.0 / 20.0 * g1sq
                       - 9.0 / 4.0 * g2sq - 8.0 * g3sq)
    dyt += yt / b16sq * (
        -12.0 * ytsq**2
        + ytsq * (393.0 / 80.0 * g1sq + 225.0 / 16.0 * g2sq + 36.0 * g3sq)
        + 1187.0 / 600.0 * g1sq**2 - 9.0 / 20.0 * g1sq * g2sq
        + 19.0 / 15.0 * g1sq * g3sq - 23.0 / 4.0 * g2sq**2
        + 9.0 * g2sq * g3sq - 108.0 * g3sq**2
        + 6.0 * lam**2 - 3.0 / 2.0 * lam * ytsq)

    # Higgs quartic
    dlam = (1.0 / b16) * (
        24.0 * lam**2
        + 12.0 * lam * ytsq - 12.0 * ytsq**2
        - 3.0 * lam * (3.0 / 5.0 * g1sq + 3.0 * g2sq)
        + 3.0 / 8.0 * (3.0 / 25.0 * g1sq**2 + 6.0 / 5.0 * g1sq * g2sq
                        + 3.0 * g2sq**2))
    dlam += (1.0 / b16sq) * (
        -312.0 * lam**3
        - 144.0 * lam**2 * ytsq
        + lam * ytsq * (-3.0 * ytsq + 80.0 * g3sq + 45.0 / 2.0 * g2sq
                         + 85.0 / 6.0 * 3.0 / 5.0 * g1sq)
        + 60.0 * ytsq**3 - 16.0 * ytsq**2 * g3sq
        + lam * (108.0 / 5.0 * 3.0 / 25.0 * g1sq**2
                 + 36.0 * 3.0 / 5.0 * g1sq * g2sq / 5.0
                 - 73.0 / 8.0 * g2sq**2)
        - 3.0 / 5.0 * g1sq * (-57.0 / 10.0 * g2sq * g1sq
                                + 12.0 * ytsq**2) / 2.0
        + g2sq * (-289.0 / 8.0 * g2sq**2 / 4.0))

    return [dg1, dg2, dg3, dyt, dlam]


# =============================================================================
# 4. REFERENCE SM COUPLINGS AT M_KK (from upward running)
# =============================================================================
print("\n" + "=" * 80)
print("4. SM COUPLINGS AT M_KK (2-loop upward from M_Z)")
print("=" * 80)

# Run SM from M_Z up to M_KK (gravity route)
y0_up = [g1_MZ, g2_MZ, g3_MZ, yt_MZ, lambda_MZ_obs]
sol_up = solve_ivp(
    beta_2loop_SM, [0, t_MKK_gravity], y0_up,
    t_eval=np.linspace(0, t_MKK_gravity, 5000),
    method='RK45', rtol=1e-12, atol=1e-14
)
assert sol_up.success, f"Upward RG failed: {sol_up.message}"

g1_MKK = sol_up.y[0, -1]
g2_MKK = sol_up.y[1, -1]
g3_MKK_sm = sol_up.y[2, -1]
yt_MKK = sol_up.y[3, -1]
lam_MKK_sm = sol_up.y[4, -1]

print(f"  g_1(M_KK) = {g1_MKK:.6f}")
print(f"  g_2(M_KK) = {g2_MKK:.6f}")
print(f"  g_3(M_KK, SM) = {g3_MKK_sm:.6f}, 1/g_3^2 = {1/g3_MKK_sm**2:.4f}")
print(f"  y_t(M_KK) = {yt_MKK:.6f}")
print(f"  lambda(M_KK, SM) = {lam_MKK_sm:.8f}")
print(f"  alpha_3(M_KK, SM) = {g3_MKK_sm**2/(4*PI):.6f}")

# Cross-check: upward running of g3 gives 1/g3^2 = 3.755 (S69 result)
print(f"\n  Cross-check: 1/g3^2(SM) = {1/g3_MKK_sm**2:.4f} vs S69 nominal = {g3_inv2_nominal_SM:.4f}")

# =============================================================================
# 5. DOWNWARD RG FUNCTION
# =============================================================================


def run_rg_down(g3_eff, lam_UV, M_KK_val=M_KK_gravity):
    """Run 2-loop SM from M_KK to M_Z with given g3_eff and lambda_UV.

    Returns: (g3_MZ, lam_MZ, m_H, alpha_s_MZ)
    """
    t_MKK = np.log(M_KK_val / M_Z)
    y0 = [g1_MKK, g2_MKK, g3_eff, yt_MKK, lam_UV]
    sol = solve_ivp(
        beta_2loop_SM, [t_MKK, 0], y0,
        t_eval=np.linspace(t_MKK, 0, 5000),
        method='RK45', rtol=1e-12, atol=1e-14
    )
    if not sol.success:
        return np.nan, np.nan, np.nan, np.nan

    g3_low = sol.y[2, -1]
    lam_low = sol.y[4, -1]
    alpha_s = g3_low**2 / (4.0 * PI)
    m_H = np.sqrt(2.0 * lam_low) * v_ew if lam_low > 0 else 0.0

    return g3_low, lam_low, m_H, alpha_s


# =============================================================================
# 6. MAIN f_0 SCAN (GRAVITY ROUTE)
# =============================================================================
print("\n" + "=" * 80)
print("6. f_0 SCAN: GRAVITY ROUTE (M_KK = 7.43e16 GeV)")
print("=" * 80)

# Scan parameters
f0_arr = np.linspace(0.1, 10.0, 200)
S_inf = S_inf_bare  # 2.895 (Aitken-extrapolated)

# Results arrays
alpha_s_arr = np.zeros(len(f0_arr))
mH_arr = np.zeros(len(f0_arr))
alpha_3_tree_arr = np.zeros(len(f0_arr))
alpha_3_eff_arr = np.zeros(len(f0_arr))
g3_eff_arr = np.zeros(len(f0_arr))
lam_UV_arr = np.zeros(len(f0_arr))
lam_IR_arr = np.zeros(len(f0_arr))

print(f"\n  Scanning f_0 in [{f0_arr[0]:.1f}, {f0_arr[-1]:.1f}] with {len(f0_arr)} points")
print(f"  S_inf = {S_inf:.6f} (Aitken bare)")
print(f"  Ratio gilkey = {ratio_gilkey:.6f}")

for i, f0 in enumerate(f0_arr):
    # Step 1: Tree-level spectral action coupling
    alpha_3_tree = 2 * PI**2 * f0 / a_4
    g3sq_tree = 4 * PI * alpha_3_tree
    g3inv2_tree = 1.0 / g3sq_tree

    # Step 2: KK threshold correction
    g3inv2_eff = g3inv2_tree + S_inf
    g3sq_eff = 1.0 / g3inv2_eff
    g3_eff = np.sqrt(g3sq_eff)

    # Step 3: CCM Higgs quartic matching
    lam_CCM = (4.0 / 3.0) * g3sq_eff * ratio_gilkey

    # Step 4: 2-loop RG running from M_KK to M_Z
    _, lam_low, mH, alpha_s = run_rg_down(g3_eff, lam_CCM)

    # Store results
    alpha_3_tree_arr[i] = alpha_3_tree
    alpha_3_eff_arr[i] = g3sq_eff / (4 * PI)
    g3_eff_arr[i] = g3_eff
    lam_UV_arr[i] = lam_CCM
    lam_IR_arr[i] = lam_low
    alpha_s_arr[i] = alpha_s
    mH_arr[i] = mH

    if i % 40 == 0 or i == len(f0_arr) - 1:
        print(f"  f_0={f0:6.3f}: alpha_3(tree)={alpha_3_tree:.6f}, "
              f"g3_eff={g3_eff:.4f}, lam_UV={lam_CCM:.6f}, "
              f"alpha_s(M_Z)={alpha_s:.6f}, m_H={mH:.2f} GeV")

# =============================================================================
# 7. IDENTIFY VIABLE WINDOW
# =============================================================================
print("\n" + "=" * 80)
print("7. VIABLE WINDOW ANALYSIS")
print("=" * 80)

# Target bands
alpha_s_lo, alpha_s_hi = 0.10, 0.13
mH_lo, mH_hi = 120.0, 135.0
f0_phys_lo, f0_phys_hi = 0.5, 5.0

# Mask for each constraint
mask_alpha = (alpha_s_arr >= alpha_s_lo) & (alpha_s_arr <= alpha_s_hi)
mask_mH = (mH_arr >= mH_lo) & (mH_arr <= mH_hi)
mask_phys = (f0_arr >= f0_phys_lo) & (f0_arr <= f0_phys_hi)
mask_both = mask_alpha & mask_mH
mask_all = mask_both & mask_phys

n_alpha = np.sum(mask_alpha)
n_mH = np.sum(mask_mH)
n_both = np.sum(mask_both)
n_all = np.sum(mask_all)

print(f"  alpha_s in [{alpha_s_lo}, {alpha_s_hi}]: {n_alpha}/{len(f0_arr)} points")
print(f"  m_H in [{mH_lo}, {mH_hi}] GeV: {n_mH}/{len(f0_arr)} points")
print(f"  Both constraints: {n_both}/{len(f0_arr)} points")
print(f"  Both + f_0 in [{f0_phys_lo}, {f0_phys_hi}]: {n_all}/{len(f0_arr)} points")

if n_alpha > 0:
    f0_alpha_range = f0_arr[mask_alpha]
    print(f"\n  alpha_s constraint satisfied for f_0 in [{f0_alpha_range[0]:.3f}, {f0_alpha_range[-1]:.3f}]")
else:
    print(f"\n  alpha_s constraint NOT satisfied for any f_0 in scan range!")
    # Check what alpha_s values are achieved
    print(f"  alpha_s range achieved: [{alpha_s_arr.min():.6f}, {alpha_s_arr.max():.6f}]")
    print(f"  Best alpha_s = {alpha_s_arr.max():.6f} at f_0 = {f0_arr[alpha_s_arr.argmax()]:.3f}")

if n_mH > 0:
    f0_mH_range = f0_arr[mask_mH]
    print(f"  m_H constraint satisfied for f_0 in [{f0_mH_range[0]:.3f}, {f0_mH_range[-1]:.3f}]")
else:
    print(f"  m_H constraint NOT satisfied for any f_0 in scan range!")
    print(f"  m_H range achieved: [{mH_arr.min():.2f}, {mH_arr.max():.2f}] GeV")
    valid = mH_arr > 0
    if np.any(valid):
        print(f"  Valid m_H range: [{mH_arr[valid].min():.2f}, {mH_arr[valid].max():.2f}] GeV")

if n_both > 0:
    f0_both = f0_arr[mask_both]
    print(f"\n  JOINT viable window: f_0 in [{f0_both[0]:.4f}, {f0_both[-1]:.4f}]")
    # Find optimal f_0 closest to observed values
    merit = np.abs(alpha_s_arr - alpha_s_MZ_obs) / alpha_s_MZ_obs + np.abs(mH_arr - m_H_obs) / m_H_obs
    merit[~mask_both] = np.inf
    idx_opt = np.argmin(merit)
    f0_opt = f0_arr[idx_opt]
    print(f"  Optimal f_0 = {f0_opt:.4f}: alpha_s = {alpha_s_arr[idx_opt]:.6f}, m_H = {mH_arr[idx_opt]:.2f} GeV")

# =============================================================================
# 8. STRUCTURAL ANALYSIS: WHY alpha_s IS LOW
# =============================================================================
print("\n" + "=" * 80)
print("8. STRUCTURAL ANALYSIS")
print("=" * 80)

# 1-loop analytical estimate for maximum alpha_s(M_Z)
# Running from M_KK to m_t with n_f=6: b_0 = (33-12)/3 = 7
# Running from m_t to M_Z with n_f=5: b_0 = (33-10)/3 = 23/3
b0_6 = 7.0  # (local)
b0_5 = 23.0 / 3.0

delta_1loop_up = b0_6 / (2 * PI) * np.log(M_KK_gravity / m_t_pole)
delta_1loop_dn = b0_5 / (2 * PI) * np.log(m_t_pole / M_Z)
total_1loop_shift = delta_1loop_up + delta_1loop_dn

print(f"  1-loop QCD running analysis:")
print(f"    b_0(n_f=6) = {b0_6:.1f}, b_0(n_f=5) = {b0_5:.4f}")
print(f"    M_KK -> m_t: delta(1/alpha) = {delta_1loop_up:.4f}")
print(f"    m_t -> M_Z:  delta(1/alpha) = {delta_1loop_dn:.4f}")
print(f"    Total:       delta(1/alpha) = {total_1loop_shift:.4f}")
print(f"    Max alpha_s(M_Z) = 1/delta = {1.0/total_1loop_shift:.6f}")
print(f"    (This is the alpha_s(M_Z) if alpha_3(M_KK) = infinity)")
print()

# f_0 needed for observed alpha_s (1-loop estimate, no threshold)
# 1/alpha_s(M_Z) = 1/alpha_3(tree) + delta
# 1/alpha_3(tree) = 1/0.118 - delta = 8.47 - 38.32 = -29.8 ... NEGATIVE!
# This means even without threshold, f_0 = infinity is needed.

# With threshold:
# 1/alpha_s(M_Z) = 1/alpha_3(tree) + 4*pi*S_inf + delta_1loop
# Need: 8.47 = 1/alpha_3(tree) + 4*PI*S_inf + delta_1loop
# 1/alpha_3(tree) = 8.47 - 4*PI*S_inf - delta_1loop
inv_alpha_tree_needed_1loop = 1.0/alpha_s_MZ_obs - 4*PI*S_inf - total_1loop_shift

print(f"  1-loop estimate for matching observed alpha_s:")
print(f"    1/alpha_s(M_Z) = {1/alpha_s_MZ_obs:.2f}")
print(f"    4*pi*S_inf = {4*PI*S_inf:.2f}")
print(f"    1-loop shift = {total_1loop_shift:.2f}")
print(f"    Needed 1/alpha_3(tree) = {inv_alpha_tree_needed_1loop:.2f}")

if inv_alpha_tree_needed_1loop > 0:
    alpha_tree_needed = 1.0 / inv_alpha_tree_needed_1loop
    f0_needed = alpha_tree_needed * a_4 / (2 * PI**2)
    print(f"    alpha_3(tree) needed = {alpha_tree_needed:.6f}")
    print(f"    f_0 needed = {f0_needed:.4f}")
else:
    print(f"    IMPOSSIBLE at 1-loop: needed 1/alpha_3(tree) < 0")
    print(f"    The QCD running + threshold is too strong for ANY finite coupling")
    print(f"    Maximum: alpha_s(M_Z) = 1/(4*pi*S_inf + delta) = {1.0/(4*PI*S_inf + total_1loop_shift):.6f}")

# The maximum alpha_s(M_Z) FROM THE SA (infinite tree-level coupling):
alpha_s_max_with_thresh = 1.0 / (4 * PI * S_inf + total_1loop_shift)
alpha_s_max_no_thresh = 1.0 / total_1loop_shift

print(f"\n  Absolute maximum alpha_s(M_Z) (f_0 -> infinity):")
print(f"    Without threshold: {alpha_s_max_no_thresh:.6f}")
print(f"    With threshold:    {alpha_s_max_with_thresh:.6f}")
print(f"    Observed:          {alpha_s_MZ_obs:.4f}")
print(f"    Ratio obs/max:     {alpha_s_MZ_obs/alpha_s_max_with_thresh:.2f}")

# =============================================================================
# 9. KERNER ROUTE CROSS-CHECK
# =============================================================================
print("\n" + "=" * 80)
print("9. KERNER ROUTE CROSS-CHECK (M_KK = 5.04e17 GeV)")
print("=" * 80)

# Run SM from M_Z up to M_KK (Kerner route)
sol_up_K = solve_ivp(
    beta_2loop_SM, [0, t_MKK_kerner], y0_up,
    t_eval=np.linspace(0, t_MKK_kerner, 5000),
    method='RK45', rtol=1e-12, atol=1e-14
)
assert sol_up_K.success, f"Kerner upward RG failed: {sol_up_K.message}"

g1_MKK_K = sol_up_K.y[0, -1]
g2_MKK_K = sol_up_K.y[1, -1]
g3_MKK_K_sm = sol_up_K.y[2, -1]
yt_MKK_K = sol_up_K.y[3, -1]

print(f"  g_3(M_KK_Kerner, SM) = {g3_MKK_K_sm:.6f}, 1/g_3^2 = {1/g3_MKK_K_sm**2:.4f}")

# Scan f_0 for Kerner route
alpha_s_K_arr = np.zeros(len(f0_arr))
mH_K_arr = np.zeros(len(f0_arr))

for i, f0 in enumerate(f0_arr):
    # Tree level
    alpha_3_tree = 2 * PI**2 * f0 / a_4
    g3sq_tree = 4 * PI * alpha_3_tree
    g3inv2_tree = 1.0 / g3sq_tree

    # Threshold + effective coupling
    g3inv2_eff = g3inv2_tree + S_inf
    g3sq_eff = 1.0 / g3inv2_eff
    g3_eff = np.sqrt(g3sq_eff)

    # CCM lambda
    lam_CCM = (4.0 / 3.0) * g3sq_eff * ratio_gilkey

    # RG run with Kerner M_KK
    y0_K = [g1_MKK_K, g2_MKK_K, g3_eff, yt_MKK_K, lam_CCM]
    sol_K = solve_ivp(
        beta_2loop_SM, [t_MKK_kerner, 0], y0_K,
        t_eval=np.linspace(t_MKK_kerner, 0, 5000),
        method='RK45', rtol=1e-12, atol=1e-14
    )
    if sol_K.success:
        g3K_low = sol_K.y[2, -1]
        lamK_low = sol_K.y[4, -1]
        alpha_s_K_arr[i] = g3K_low**2 / (4 * PI)
        mH_K_arr[i] = np.sqrt(2.0 * lamK_low) * v_ew if lamK_low > 0 else 0.0
    else:
        alpha_s_K_arr[i] = np.nan
        mH_K_arr[i] = np.nan

# Best alpha_s for Kerner
idx_best_K = np.nanargmax(alpha_s_K_arr)
print(f"\n  Kerner route results:")
print(f"  Max alpha_s(M_Z) = {alpha_s_K_arr[idx_best_K]:.6f} at f_0 = {f0_arr[idx_best_K]:.3f}")
print(f"  m_H at max alpha_s = {mH_K_arr[idx_best_K]:.2f} GeV")

# Kerner 1-loop analysis
delta_K_up = b0_6 / (2 * PI) * np.log(M_KK_kerner / m_t_pole)
delta_K_dn = b0_5 / (2 * PI) * np.log(m_t_pole / M_Z)
total_K = delta_K_up + delta_K_dn
alpha_s_K_max = 1.0 / (4 * PI * S_inf + total_K)
print(f"  1-loop shift (Kerner): {total_K:.4f}")
print(f"  Absolute max alpha_s(M_Z): {alpha_s_K_max:.6f}")

# =============================================================================
# 10. WITHOUT THRESHOLD: f_0 SCAN (UPPER BOUND)
# =============================================================================
print("\n" + "=" * 80)
print("10. UPPER BOUND: f_0 SCAN WITHOUT KK THRESHOLD")
print("=" * 80)

# What if the threshold correction is wrong or absent?
# This gives the MAXIMUM possible alpha_s for each f_0.
alpha_s_nothr_arr = np.zeros(len(f0_arr))
mH_nothr_arr = np.zeros(len(f0_arr))

for i, f0 in enumerate(f0_arr):
    alpha_3_tree = 2 * PI**2 * f0 / a_4
    g3sq_tree = 4 * PI * alpha_3_tree
    g3_tree = np.sqrt(g3sq_tree)

    # CCM lambda without threshold
    lam_CCM = (4.0 / 3.0) * g3sq_tree * ratio_gilkey

    _, lam_low, mH, alpha_s = run_rg_down(g3_tree, lam_CCM)
    alpha_s_nothr_arr[i] = alpha_s
    mH_nothr_arr[i] = mH

# Check viable window without threshold
mask_alpha_nt = (alpha_s_nothr_arr >= alpha_s_lo) & (alpha_s_nothr_arr <= alpha_s_hi)
mask_mH_nt = (mH_nothr_arr >= mH_lo) & (mH_nothr_arr <= mH_hi)
mask_both_nt = mask_alpha_nt & mask_mH_nt
mask_all_nt = mask_both_nt & mask_phys

print(f"  WITHOUT threshold:")
print(f"  Max alpha_s = {np.nanmax(alpha_s_nothr_arr):.6f} at f_0 = {f0_arr[np.nanargmax(alpha_s_nothr_arr)]:.3f}")
if np.any(mask_alpha_nt):
    f0_nt = f0_arr[mask_alpha_nt]
    print(f"  alpha_s in [0.10, 0.13] for f_0 in [{f0_nt[0]:.3f}, {f0_nt[-1]:.3f}]")
else:
    print(f"  alpha_s NEVER reaches [0.10, 0.13]. Max = {np.nanmax(alpha_s_nothr_arr):.6f}")

if np.any(mask_both_nt):
    f0_bnt = f0_arr[mask_both_nt]
    print(f"  JOINT viable (no threshold): f_0 in [{f0_bnt[0]:.3f}, {f0_bnt[-1]:.3f}]")
    # Check if in physical range
    if np.any(mask_all_nt):
        f0_ant = f0_arr[mask_all_nt]
        print(f"  ...and in [0.5, 5.0]: f_0 in [{f0_ant[0]:.3f}, {f0_ant[-1]:.3f}]")
    else:
        print(f"  ...but NONE in physical range [0.5, 5.0]")
else:
    print(f"  No joint viable window even without threshold")

# =============================================================================
# 11. SWAMPLAND CHECK
# =============================================================================
print("\n" + "=" * 80)
print("11. SWAMPLAND CONSTRAINT CHECK")
print("=" * 80)

# SWAMP-69 PASS: c(fold) = 3.52 >> 1. The swampland gradient conjecture
# requires c > 1 in Planck units.
# The swampland parameter c = |nabla V|/V * M_Pl does NOT depend on f_0
# because it's a ratio of spectral action derivatives (f_0 cancels).

try:
    d_sw = np.load(os.path.join(SCRIPT_DIR, 's69_swampland.npz'), allow_pickle=True)
    c_bare = float(d_sw['c_bare'][d_sw['fold_idx']])
    print(f"  c(fold) = {c_bare:.4f} [from SWAMP-69]")
    print(f"  Swampland conjecture: c > 1 required")
    print(f"  c is a RATIO of SA derivatives: f_0-INDEPENDENT")
    print(f"  Verdict: f_0 scan does NOT violate swampland constraint")
except Exception as e:
    print(f"  Could not load swampland data: {e}")
    print(f"  Swampland check: SKIPPED")

# =============================================================================
# 12. SENSITIVITY ANALYSIS
# =============================================================================
print("\n" + "=" * 80)
print("12. SENSITIVITY ANALYSIS")
print("=" * 80)

# Numerical derivative d(alpha_s)/d(f_0)
dalpha_df0 = np.gradient(alpha_s_arr, f0_arr)
# Elasticity: (d alpha_s / alpha_s) / (d f_0 / f_0)
# Find reference point at f_0 = 1
idx_ref = np.argmin(np.abs(f0_arr - 1.0))
elasticity = dalpha_df0[idx_ref] * f0_arr[idx_ref] / alpha_s_arr[idx_ref]

print(f"  At f_0 = 1.0:")
print(f"    alpha_s(M_Z) = {alpha_s_arr[idx_ref]:.6f}")
print(f"    d(alpha_s)/d(f_0) = {dalpha_df0[idx_ref]:.6e}")
print(f"    Elasticity = {elasticity:.4f}")
print(f"    (10% change in f_0 => {abs(elasticity)*10:.2f}% change in alpha_s)")

# f_0 needed for alpha_s = 0.118 (extrapolation)
if np.max(alpha_s_arr) > alpha_s_lo:
    # Find the f_0 where alpha_s crosses 0.118
    try:
        from scipy.interpolate import interp1d
        interp_alpha = interp1d(alpha_s_arr, f0_arr, kind='linear',
                                fill_value='extrapolate')
        f0_target = interp_alpha(alpha_s_MZ_obs)
        print(f"\n  Extrapolation: f_0 for alpha_s = 0.118: {f0_target:.2f}")
    except Exception:
        pass

# =============================================================================
# 13. SUMMARY TABLE
# =============================================================================
print("\n" + "=" * 80)
print("13. SUMMARY TABLE")
print("=" * 80)

print(f"\n  {'f_0':>8} | {'alpha_3(tree)':>14} | {'g3_eff':>8} | {'lam_UV':>10} | {'alpha_s(MZ)':>12} | {'m_H(GeV)':>10}")
print(f"  {'-'*8} | {'-'*14} | {'-'*8} | {'-'*10} | {'-'*12} | {'-'*10}")

for f0_val in [0.1, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]:
    idx = np.argmin(np.abs(f0_arr - f0_val))
    print(f"  {f0_arr[idx]:8.3f} | {alpha_3_tree_arr[idx]:14.6f} | {g3_eff_arr[idx]:8.4f} | "
          f"{lam_UV_arr[idx]:10.6f} | {alpha_s_arr[idx]:12.6f} | {mH_arr[idx]:10.2f}")

# =============================================================================
# 14. GATE VERDICT
# =============================================================================
print("\n" + "=" * 80)
print("14. GATE VERDICT: F0-ALPHA-S-70")
print("=" * 80)

# Determine verdict
if n_all > 0:
    verdict = "PASS"
    detail = (f"Consistent f_0 exists in [{f0_arr[mask_all][0]:.3f}, {f0_arr[mask_all][-1]:.3f}] "
              f"(physical range [0.5, 5.0]). "
              f"alpha_s in [{alpha_s_arr[mask_all].min():.4f}, {alpha_s_arr[mask_all].max():.4f}], "
              f"m_H in [{mH_arr[mask_all].min():.1f}, {mH_arr[mask_all].max():.1f}] GeV.")
elif n_both > 0:
    verdict = "INFO"
    f0_both_min = f0_arr[mask_both].min()
    f0_both_max = f0_arr[mask_both].max()
    detail = (f"f_0 in [{f0_both_min:.3f}, {f0_both_max:.3f}] satisfies both constraints, "
              f"but outside physical range [0.5, 5.0]. Requires f_0 > 5.")
else:
    # Check if alpha_s constraint is the binding one
    max_alpha_s = np.max(alpha_s_arr)
    max_alpha_s_nt = np.max(alpha_s_nothr_arr) if np.any(np.isfinite(alpha_s_nothr_arr)) else 0
    if max_alpha_s < alpha_s_lo:
        verdict = "FAIL"
        detail = (f"No f_0 in [{f0_arr[0]:.1f}, {f0_arr[-1]:.1f}] reaches alpha_s >= {alpha_s_lo}. "
                  f"Max alpha_s(M_Z) = {max_alpha_s:.6f} at f_0 = {f0_arr[np.argmax(alpha_s_arr)]:.3f}. "
                  f"Structural limit: 34 decades of QCD running (n_f=6 above m_t) + "
                  f"KK threshold S_inf={S_inf:.3f} cap alpha_s(M_Z) at {alpha_s_max_with_thresh:.4f}. "
                  f"Without threshold: max = {max_alpha_s_nt:.6f}. "
                  f"alpha_s tension is STRUCTURAL, not normalization.")
    else:
        verdict = "FAIL"
        detail = f"alpha_s reachable but m_H incompatible. Max alpha_s = {max_alpha_s:.6f}."

print(f"\n  Gate: F0-ALPHA-S-70")
print(f"  Verdict: {verdict}")
print(f"  Detail: {detail}")

print(f"\n  Structural ceiling (1-loop):")
print(f"    Without threshold: max alpha_s(M_Z) = {alpha_s_max_no_thresh:.6f}")
print(f"    With threshold:    max alpha_s(M_Z) = {alpha_s_max_with_thresh:.6f}")
print(f"    Observed:          alpha_s(M_Z) = {alpha_s_MZ_obs:.4f}")
print(f"    Factor:            {alpha_s_MZ_obs / alpha_s_max_with_thresh:.1f}x above ceiling")

# =============================================================================
# 15. SAVE DATA
# =============================================================================
print("\n" + "=" * 80)
print("15. SAVING DATA")
print("=" * 80)

out_path = os.path.join(SCRIPT_DIR, 's70_f0_alpha_s.npz')
np.savez(
    out_path,
    # Gate
    gate_name=np.array('F0-ALPHA-S-70'),
    gate_verdict=np.array(verdict),
    gate_detail=np.array(detail),
    # Scan arrays
    f0_arr=f0_arr,
    alpha_s_arr=alpha_s_arr,
    mH_arr=mH_arr,
    alpha_3_tree_arr=alpha_3_tree_arr,
    alpha_3_eff_arr=alpha_3_eff_arr,
    g3_eff_arr=g3_eff_arr,
    lam_UV_arr=lam_UV_arr,
    lam_IR_arr=lam_IR_arr,
    # Kerner route
    alpha_s_K_arr=alpha_s_K_arr,
    mH_K_arr=mH_K_arr,
    # No threshold
    alpha_s_nothr_arr=alpha_s_nothr_arr,
    mH_nothr_arr=mH_nothr_arr,
    # Constants used
    S_inf=np.array(S_inf),
    ratio_gilkey=np.array(ratio_gilkey),
    a4_fold=np.array(a_4),
    a2_fold=np.array(a_2),
    M_KK_gravity=np.array(M_KK_gravity),
    M_KK_kerner=np.array(M_KK_kerner),
    # Structural limits
    alpha_s_max_no_thresh=np.array(alpha_s_max_no_thresh),
    alpha_s_max_with_thresh=np.array(alpha_s_max_with_thresh),
    total_1loop_shift=np.array(total_1loop_shift),
    # Target bands
    alpha_s_lo=np.array(alpha_s_lo),
    alpha_s_hi=np.array(alpha_s_hi),
    mH_lo=np.array(mH_lo),
    mH_hi=np.array(mH_hi),
    # Counts
    n_alpha=np.array(n_alpha),
    n_mH=np.array(n_mH),
    n_both=np.array(n_both),
    n_all=np.array(n_all),
)
print(f"  Saved: {out_path}")

# =============================================================================
# 16. PLOT
# =============================================================================
print("\n" + "=" * 80)
print("16. PLOTTING")
print("=" * 80)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10), sharex=True)

# Upper panel: alpha_s(M_Z) vs f_0
ax1.plot(f0_arr, alpha_s_arr, 'b-', lw=2, label='Gravity route (with threshold)')
ax1.plot(f0_arr, alpha_s_K_arr, 'g--', lw=1.5, label='Kerner route (with threshold)')
ax1.plot(f0_arr, alpha_s_nothr_arr, 'r:', lw=1.5, label='No threshold (upper bound)')
ax1.axhline(alpha_s_MZ_obs, color='k', ls='--', lw=1, label=f'PDG: {alpha_s_MZ_obs}')
ax1.axhspan(alpha_s_lo, alpha_s_hi, alpha=0.15, color='green', label=f'Target [{alpha_s_lo}, {alpha_s_hi}]')
ax1.axhline(alpha_s_max_with_thresh, color='gray', ls=':', lw=0.8,
            label=f'Structural ceiling: {alpha_s_max_with_thresh:.4f}')
ax1.set_ylabel(r'$\alpha_s(M_Z)$', fontsize=14)
ax1.set_ylim(0, 0.15)
ax1.legend(loc='upper left', fontsize=9)
ax1.set_title('F0-ALPHA-S-70: Spectral Function Normalization Scan', fontsize=14)
ax1.grid(True, alpha=0.3)

# Lower panel: m_H vs f_0
ax2.plot(f0_arr, mH_arr, 'b-', lw=2, label='Gravity route (with threshold)')
ax2.plot(f0_arr, mH_K_arr, 'g--', lw=1.5, label='Kerner route (with threshold)')
ax2.plot(f0_arr, mH_nothr_arr, 'r:', lw=1.5, label='No threshold')
ax2.axhline(m_H_obs, color='k', ls='--', lw=1, label=f'Observed: {m_H_obs} GeV')
ax2.axhspan(mH_lo, mH_hi, alpha=0.15, color='green', label=f'Target [{mH_lo}, {mH_hi}] GeV')
ax2.set_xlabel(r'$f_0$ (spectral function normalization)', fontsize=14)
ax2.set_ylabel(r'$m_H$ (GeV)', fontsize=14)
ax2.set_ylim(0, 250)
ax2.legend(loc='upper right', fontsize=9)
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plot_path = os.path.join(SCRIPT_DIR, 's70_f0_alpha_s.png')
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"  Saved: {plot_path}")

print("\n" + "=" * 80)
print("COMPUTATION COMPLETE")
print("=" * 80)
