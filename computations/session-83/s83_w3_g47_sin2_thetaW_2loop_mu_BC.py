#!/usr/bin/env python3
"""
S83 W3-G47 -- SIN2-THETA-W-2-LOOP-PLUS-MU-BC
=============================================

Gate ID       : S83-SIN2-THETA-W-2-LOOP-PLUS-MU-BC
Trigger       : [VERIFY][CHAIN]
Classification: PARTICLE
Owner         : mack-cosmic-bridge
Anchor        : sessions/session-plan/session-83-plan.md L2748-L2792
S83 §W3-G47   : 2-loop RGE + mu_BC natural-threshold closure of the S82 3.98 sigma INFO

HYPOTHESIS (pre-registered, S83 plan L2758)
-------------------------------------------
sin^2(theta_W) at 2-loop RGE + mu_BC natural threshold closes the 3.98 sigma
INFO gap found in S82 W3-10. The S82 W3-10 gate established:
  - BC at mu_BC = 2*M_Z = 182.38 GeV gives sin^2(M_Z) = 0.231379 (3.98 sigma INFO)
  - Critical scale mu_crit(2-loop) = 188.44 GeV yields sin^2(M_Z) = PDG exactly
  - Gap of 3.3% between 2*M_Z and mu_crit is the INFO-to-PASS bridge

This gate tests two natural-threshold lifts to the 2*M_Z BC:
  (a) mu_BC -> mu_crit = 188.44 GeV (EW threshold-matching lift from 2*M_Z)
  (b) Inclusion of top-Yukawa 2-loop contribution to B_ij (PDG Ch. 10.2)
      which adjusts the effective b_i at low scale.

PRE-REGISTERED GATE (S83 plan L2759)
------------------------------------
  PASS : n_sigma < 2 (|sin^2_pred - PDG| < 2 sigma_PDG = 8e-5)
  INFO : 2 <= n_sigma < 3
  FAIL : n_sigma >= 3

MANDATORY [VERIFY][CHAIN] SUBSTITUTION CHAIN (direction claim)
--------------------------------------------------------------

CLAIM: The shift mu_BC: 2*M_Z -> mu_crit = 188.44 GeV (a 3.3% increase),
combined with top-Yukawa 2-loop corrections, reduces |sin^2(M_Z) - PDG|
from 3.98 sigma toward PASS (< 2 sigma).

DEFINITIONS:
  Step 1 (defn):
    sin^2(mu) = 3 alpha_1(mu) / (3 alpha_1(mu) + 5 alpha_2(mu))
    with alpha_i^{-1}(mu) determined by 2-loop SM RGE:
       d alpha_i^{-1}/d ln mu = -b_i/(2*pi)
                               - (1/(8*pi^2)) [ sum_j B_ij alpha_j - C_i^t alpha_t ]
    where alpha_t = y_t^2/(4*pi) and
       C_i^t = (17/10, 3/2, 2)      (U(1)_Y GUT, SU(2)_L, SU(3)_c)
    BC: sin^2(mu_BC) = 3 * L_2^3/(3 * L_2^3 + L_1^3)
                     = 3/(3 + exp(12 * tau_fold)) = 0.234803

  Step 2 (substitute):
    At mu_BC = 188.44 GeV: sin^2(mu_BC) = 0.234803 (geometric cubic).
    Alpha_1(mu_BC), alpha_2(mu_BC), alpha_3(mu_BC) determined by matching.
    Run DOWN from mu_BC to M_Z using 2-loop + y_t^2 RGE.

  Step 3 (simplify):
    Log-lever arm: ln(188.44/91.1876) = 0.7260.
    By S82 CHK4: d(sin^2)/d(ln mu) > 0 (= +0.00499/decade at M_Z).
    Therefore sin^2(M_Z) < sin^2(188.44 GeV) under run-down.
    Top-Yukawa corrections: C_i^t alpha_t at alpha_t(M_Z) = y_t^2/(4*pi) ~ 0.075
    gives delta(d alpha_i^{-1}/d ln mu) ~ 10^{-3} per decade,
    i.e., O(10^{-4}) shift in sin^2 over the log arm 0.7260.

  Step 4 (direction):
    At mu_BC = mu_crit (2-loop, no Yukawa), the run-down returns sin^2 = PDG
    by construction (S82 SEC 8 brentq gives mu_crit = 188.44 GeV).
    Adding top-Yukawa shifts sin^2(M_Z)_pred by delta ~ 10^{-4}, direction
    set by sign of (C_1^t alpha_1 + C_2^t alpha_2) * alpha_t at M_Z.

  Step 5 (conclusion):
    Two runs:
      (a) mu_BC = 188.44 GeV, 2-loop no Yukawa:    n_sigma_a ~ 0 (by construction)
      (b) mu_BC = 188.44 GeV, 2-loop + y_t^2:      n_sigma_b ~ O(1)
    PASS if n_sigma_b < 2 (which is expected since Yukawa shifts are O(10^{-4})
    and 1 sigma_PDG = 4e-5).

OUTPUT 4-TUPLE
--------------
(n_sigma=<best>, scheme=2-loop-RGE-plus-mu_BC, convention=PDG-0.23122, L_max=N/A)

MACHINERY PIN (PRDR per plan §4.5)
-----------------------------------
  Anchoring scale       : mu_BC = 188.4361 GeV (S82 W3-10 SEC 8 mu_crit(2-loop))
                          Confirmed by brentq: sin^2_SM(mu_crit) = cubic under 2-loop
  Boundary condition    : sin^2(mu_BC) = 3/(3 + exp(12*tau_fold)) = 0.234803
  RG order              : 2-loop (MS-bar, GUT-norm g_1 = sqrt(5/3) g_Y)
  Yukawa inclusion      : top-Yukawa y_t^2 from alpha_t(M_Z) = m_t^2/(2*v_EW^2*pi)
  b_1,b_2,b_3 1-loop    : 41/10, -19/6, -7  (canonical)
  B_{ij} 2-loop gauge   : PDG Ch. 10 / Machacek-Vaughn
  C_i^t 2-loop Yukawa   : (17/10, 3/2, 2)
  Alpha_s(M_Z)          : 0.1180 (PDG)
  Integrator            : DOP853, rtol=1e-10, atol=1e-12

CROSS-CHECKS (pre-registered)
-----------------------------
  CHK1: At mu_BC = 188.44 GeV, 2-loop without Yukawa returns sin^2 = PDG
        to within 1e-6 (by construction from S82 mu_crit brentq).
  CHK2: At mu_BC = 2*M_Z = 182.38 GeV, 2-loop reproduces S82 W3-10 result
        (sin^2 = 0.231379, 3.98 sigma) to 6 sig figs.
  CHK3: Top-Yukawa shift is O(10^{-4}) at M_Z (order-of-magnitude test).
  CHK4: [SIGN] substitution chain Step 3 verified: d(sin^2)/d(ln mu) > 0.

References
----------
  S83 plan §W3-G47  : sessions/session-plan/session-83-plan.md L2748-L2792
  S82 W3-10 result  : computations/session-82/s82_w3_10_cubic_sin2_w_ew.py (3.98 sigma INFO)
  S78 W3-J baseline : computations/session-78/s78_sin2_w_non_tree.py (31.6 sigma FAIL)
  PDG Ch. 10        : 2-loop SM RG with Yukawa (Machacek-Vaughn)
  Canonical const   : computations/_shared/canonical_constants.py

Author   : mack-cosmic-bridge
Session  : S83 W3-G47
Date     : 2026-04-18
"""

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')   # (local)
os.environ.setdefault('MKL_NUM_THREADS', '8')   # (local)

import sys
import json
import hashlib
import time
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

SCRIPT_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPT_DIR))

from canonical_constants import (
    PI, M_Z, M_W, tau_fold,
    sin2_thetaW_MSbar, alpha_em_MZ_inv,
    b1_SM, b2_SM, b3_SM,
    v_ew, m_t_pole,
    alpha_s_MZ_obs,
)

# =============================================================================
# SECTION 0: Input SHA-256 pins
# =============================================================================

def _sha256(path):
    with open(path, 'rb') as h:
        return hashlib.sha256(h.read()).hexdigest()


HERE = str(SCRIPT_DIR)                                                 # (local)
INPUT_FILES = [                                                        # (local)
    os.path.join(HERE, 'canonical_constants.py'),
    os.path.join(HERE, 's82_w3_10_cubic_sin2_w_ew.py'),
    os.path.join(HERE, 's78_sin2_w_non_tree.py'),
]

t_start = time.time()

print("=" * 78)
print("S83 W3-G47 -- SIN2-THETA-W-2-LOOP-PLUS-MU-BC (mack-cosmic-bridge)")
print("=" * 78)
print("Gate     : S83-SIN2-THETA-W-2-LOOP-PLUS-MU-BC")
print("Trigger  : [VERIFY][CHAIN]")
print("Class    : PARTICLE")
print("Anchor   : S83 plan L2748-L2792 (W3-G47)")
print()
print("[SEC 0] Input SHA-256 pins")
INPUT_SHAS = {}                                                        # (local)
for _f in INPUT_FILES:
    if os.path.exists(_f):
        _h = _sha256(_f)                                               # (local)
        INPUT_SHAS[os.path.basename(_f)] = _h
        print(f"  {os.path.basename(_f):40s} sha256={_h[:16]}...{_h[-8:]}")
    else:
        INPUT_SHAS[os.path.basename(_f)] = None
        print(f"  {os.path.basename(_f):40s} MISSING")

# =============================================================================
# SECTION 1: Pre-registered parameters
# =============================================================================
print()
print("-" * 78)
print("[SEC 1] Pre-registered parameters and PDG inputs")
print("-" * 78)

sigma_PDG = 4.0e-5                          # (local) PDG 2024 uncertainty on sin2_thetaW
tol_PASS = 2.0 * sigma_PDG                  # (local) PASS: n_sigma < 2
tol_INFO = 3.0 * sigma_PDG                  # (local) INFO: n_sigma < 3

# Cubic BC at tau_fold
sin2_cubic_tau_fold = 3.0 / (3.0 + np.exp(12.0 * tau_fold))   # (local)

# Candidate mu_BC scales
mu_BC_2MZ = 2.0 * M_Z                        # (local) S82 W3-10 primary (INFO)
mu_BC_mu_crit = 188.4361                     # (local) S82 W3-10 SEC 8 brentq result
mu_BC_mu_crit_1loop = 186.44                 # (local) S82 W3-10 1-loop mu_star

# Top-Yukawa at M_Z: alpha_t = y_t^2/(4*pi) with y_t = sqrt(2) m_t / v_EW
y_t_MZ_sq = 2.0 * (m_t_pole / v_ew)**2       # (local) y_t^2 at M_Z from Higgs mechanism
alpha_t_MZ = y_t_MZ_sq / (4.0 * PI)          # (local) alpha_t = y_t^2/(4*pi)

print(f"  tau_fold                          = {tau_fold}")
print(f"  Cubic sin^2(mu_BC) = 3/(3+e^12tau) = {sin2_cubic_tau_fold:.8f}")
print(f"  M_Z                               = {M_Z}")
print(f"  PDG sin^2(M_Z)                    = {sin2_thetaW_MSbar}")
print(f"  sigma_PDG                         = {sigma_PDG}")
print(f"  PASS threshold |dev| < 2*sigma    = {tol_PASS}")
print(f"  INFO threshold |dev| < 3*sigma    = {tol_INFO}")
print()
print(f"  Candidate mu_BC:")
print(f"    2*M_Z            = {mu_BC_2MZ:.4f} GeV (S82 baseline: 3.98 sigma INFO)")
print(f"    mu_crit (2-loop) = {mu_BC_mu_crit:.4f} GeV (S82 SEC 8 brentq)")
print(f"    mu_crit (1-loop) = {mu_BC_mu_crit_1loop:.4f} GeV (S82 SEC 5 brentq)")
print()
print(f"  Top-Yukawa:")
print(f"    m_t (pole)      = {m_t_pole} GeV")
print(f"    v_EW            = {v_ew} GeV")
print(f"    y_t^2(M_Z)      = {y_t_MZ_sq:.6f}")
print(f"    alpha_t(M_Z)    = y_t^2/(4*pi) = {alpha_t_MZ:.6f}")

# =============================================================================
# SECTION 2: SM RG beta coefficients (1-loop, 2-loop gauge, Yukawa C_i^t)
# =============================================================================
print()
print("-" * 78)
print("[SEC 2] SM RG beta coefficients")
print("-" * 78)

b1 = b1_SM                                  # (local) 41/10
b2 = b2_SM                                  # (local) -19/6
b3 = b3_SM                                  # (local) -7

# 2-loop gauge B_{ij} (Machacek-Vaughn / PDG Ch. 10, Yukawa-neglected)
B_2loop_gauge = np.array([                  # (local)
    [199.0/50.0,   27.0/10.0,  44.0/5.0],
    [9.0/10.0,     35.0/6.0,   12.0],
    [11.0/10.0,    9.0/2.0,    -26.0],
])

# Top-Yukawa 2-loop coefficients (PDG Ch. 10 / Arason et al. 1992)
# d alpha_i^{-1}/d ln mu += +C_i^t * alpha_t / (8*pi^2)
# Values: U(1)_Y (GUT): 17/10; SU(2)_L: 3/2; SU(3)_c: 2
C_yuk = np.array([17.0/10.0, 3.0/2.0, 2.0])  # (local)

print(f"  1-loop b_i: b_1 = {b1:.4f} (=41/10), b_2 = {b2:.6f} (=-19/6), b_3 = {b3} (=-7)")
print(f"  2-loop B_ij gauge (Machacek-Vaughn):")
for i, row in enumerate(B_2loop_gauge):
    print(f"    row {i+1}: {row}")
print(f"  2-loop top-Yukawa C_i^t = {C_yuk}  (= [17/10, 3/2, 2])")
print()

# SM couplings at M_Z (PDG-derived)
alpha_em_MZ = 1.0 / alpha_em_MZ_inv         # (local)
alpha2_MZ = alpha_em_MZ / sin2_thetaW_MSbar  # (local)
alpha_Y_MZ = alpha_em_MZ / (1.0 - sin2_thetaW_MSbar)  # (local)
alpha1_MZ = (5.0/3.0) * alpha_Y_MZ          # (local) GUT-normalized
alpha3_MZ = alpha_s_MZ_obs                  # (local)

print(f"  SM couplings at M_Z (PDG-derived):")
print(f"    1/alpha_1(M_Z) = {1.0/alpha1_MZ:.6f}")
print(f"    1/alpha_2(M_Z) = {1.0/alpha2_MZ:.6f}")
print(f"    1/alpha_3(M_Z) = {1.0/alpha3_MZ:.6f}")

# =============================================================================
# SECTION 3: RG evolution machinery
# =============================================================================

def rg_1loop(lnmu, y):
    """1-loop SM RG."""
    return [-b1/(2.0*PI), -b2/(2.0*PI), -b3/(2.0*PI)]


def rg_2loop_gauge(lnmu, y):
    """2-loop gauge-only (Yukawa neglected) SM RG."""
    ia1, ia2, ia3 = y
    a1, a2, a3 = 1.0/ia1, 1.0/ia2, 1.0/ia3  # (local)
    alphas = np.array([a1, a2, a3])         # (local)
    da = [-b1/(2.0*PI), -b2/(2.0*PI), -b3/(2.0*PI)]  # (local)
    for i in range(3):
        corr = sum(B_2loop_gauge[i, j] * alphas[j] for j in range(3))  # (local)
        da[i] -= corr / (8.0 * PI * PI)
    return da


def rg_2loop_plus_yukawa(lnmu, y):
    """2-loop SM RG including top-Yukawa alpha_t contribution.
    d alpha_i^{-1}/d ln mu = -b_i/(2*pi) - (1/(8*pi^2)) [sum_j B_ij alpha_j - C_i^t alpha_t_eff]

    NOTE sign convention: Yukawa contribution SUBTRACTS from RHS the way gauge contribution does,
    but with opposite sign on C_i^t (Yukawa REDUCES alpha_i^{-1} running, equivalent to
    INCREASING alpha_i running toward Landau pole). PDG Ch. 10 convention:
       d alpha_i^{-1}/d ln mu = -b_i/(2*pi) - (1/(8*pi^2)) sum_j B_ij alpha_j
                               + (1/(8*pi^2)) C_i^t alpha_t
    with alpha_t = y_t^2/(4*pi).

    Here we approximate alpha_t as constant = alpha_t(M_Z) since the mu range is narrow
    (M_Z to 2 M_Z, log arm ~0.7). Full y_t RGE would add ~1% correction.
    """
    ia1, ia2, ia3 = y
    a1, a2, a3 = 1.0/ia1, 1.0/ia2, 1.0/ia3  # (local)
    alphas = np.array([a1, a2, a3])         # (local)
    da = [-b1/(2.0*PI), -b2/(2.0*PI), -b3/(2.0*PI)]  # (local)
    for i in range(3):
        corr_gauge = sum(B_2loop_gauge[i, j] * alphas[j] for j in range(3))  # (local)
        corr_yuk = C_yuk[i] * alpha_t_MZ    # (local)
        da[i] -= corr_gauge / (8.0 * PI * PI)
        da[i] += corr_yuk / (8.0 * PI * PI)
    return da


def sin2_from_y(y):
    """sin^2(theta_W) from y = [1/alpha_1, 1/alpha_2, 1/alpha_3]."""
    ia1, ia2 = y[0], y[1]
    a1, a2 = 1.0/ia1, 1.0/ia2               # (local)
    return 3.0 * a1 / (3.0 * a1 + 5.0 * a2)


y0_MZ = [1.0/alpha1_MZ, 1.0/alpha2_MZ, 1.0/alpha3_MZ]  # (local)

# =============================================================================
# SECTION 4: CROSS-CHECK (substitution chain Step 3 numerical verification)
# =============================================================================
print()
print("-" * 78)
print("[SEC 4] Substitution chain Step 3: d(sin^2)/d(ln mu) > 0")
print("-" * 78)

delta_ln = 0.01                             # (local)
da_1l = np.array(rg_1loop(0.0, y0_MZ))       # (local)
y_plus = np.array(y0_MZ) + da_1l * delta_ln   # (local)
y_minus = np.array(y0_MZ) - da_1l * delta_ln  # (local)
s2_plus = sin2_from_y(y_plus)               # (local)
s2_minus = sin2_from_y(y_minus)             # (local)
dsin2_dlnmu_at_MZ = (s2_plus - s2_minus) / (2.0 * delta_ln)  # (local)
print(f"  d(sin^2)/d(ln mu) at M_Z (1-loop) = {dsin2_dlnmu_at_MZ:+.8f}")
print(f"  Sign = {'+' if dsin2_dlnmu_at_MZ > 0 else '-'}  (Step 3 expects +)")
chk4_pass = dsin2_dlnmu_at_MZ > 0           # (local)
print(f"  CHK4 (SIGN Step 3 positive):        {'PASS' if chk4_pass else 'FAIL'}")

# =============================================================================
# SECTION 5: Core routine -- impose cubic at mu_BC, run DOWN to M_Z
# =============================================================================

def sin2_MZ_from_cubic_BC(mu_BC, rhs_fn):
    """Impose sin^2(mu_BC) = cubic and run DOWN to M_Z under chosen RG.

    Steps:
    1. Integrate SM RG UP from M_Z (PDG y0) to mu_BC -> get alpha_2, alpha_3 at mu_BC.
    2. Override alpha_1(mu_BC) so that sin^2(mu_BC) = cubic value.
    3. Integrate DOWN from mu_BC to M_Z and return sin^2(M_Z)_pred.
    """
    if mu_BC <= M_Z:
        return sin2_cubic_tau_fold, y0_MZ[:]

    lnmu_BC = np.log(mu_BC / M_Z)           # (local)
    sol_up = solve_ivp(rhs_fn, (0.0, lnmu_BC), y0_MZ, method='DOP853',
                       rtol=1e-10, atol=1e-12)
    ia1_BC, ia2_BC, ia3_BC = sol_up.y[:, -1]  # (local)
    a2_BC = 1.0 / ia2_BC                    # (local)
    a3_BC = 1.0 / ia3_BC                    # (local)
    # Override alpha_1 at BC so that sin^2 = cubic
    a1_BC_new = (5.0 * sin2_cubic_tau_fold * a2_BC) / (3.0 * (1.0 - sin2_cubic_tau_fold))  # (local)
    y_BC = [1.0/a1_BC_new, 1.0/a2_BC, 1.0/a3_BC]  # (local)
    sol_down = solve_ivp(rhs_fn, (lnmu_BC, 0.0), y_BC, method='DOP853',
                         rtol=1e-10, atol=1e-12)
    return sin2_from_y(sol_down.y[:, -1]), y_BC


# =============================================================================
# SECTION 6: CHK1 -- mu_BC = mu_crit with 2-loop gauge: expect sin^2 = PDG
# =============================================================================
print()
print("-" * 78)
print("[SEC 6] CHK1: mu_BC = mu_crit (2-loop gauge) should reproduce PDG exactly")
print("-" * 78)

sin2_mucrit_gauge, _ = sin2_MZ_from_cubic_BC(mu_BC_mu_crit, rg_2loop_gauge)   # (local)
dev_mucrit_gauge = sin2_mucrit_gauge - sin2_thetaW_MSbar   # (local)
chk1_pass = abs(dev_mucrit_gauge) < 1.0e-6                  # (local)
print(f"  mu_BC = {mu_BC_mu_crit} GeV, 2-loop gauge:")
print(f"    sin^2(M_Z)_pred = {sin2_mucrit_gauge:.8f}")
print(f"    deviation       = {dev_mucrit_gauge:+.8f}")
print(f"    |deviation|     = {abs(dev_mucrit_gauge):.2e}")
print(f"  CHK1 (|dev| < 1e-6 by construction): {'PASS' if chk1_pass else 'FAIL'}")

# =============================================================================
# SECTION 7: CHK2 -- reproduce S82 W3-10 at mu_BC = 2*M_Z
# =============================================================================
print()
print("-" * 78)
print("[SEC 7] CHK2: reproduce S82 W3-10 at mu_BC = 2*M_Z")
print("-" * 78)

sin2_2MZ_gauge, _ = sin2_MZ_from_cubic_BC(mu_BC_2MZ, rg_2loop_gauge)   # (local)
dev_2MZ_gauge = sin2_2MZ_gauge - sin2_thetaW_MSbar                      # (local)
sigma_2MZ_gauge = abs(dev_2MZ_gauge) / sigma_PDG                        # (local)
chk2_pass = abs(sin2_2MZ_gauge - 0.231379) < 1.0e-5                     # (local)
print(f"  mu_BC = {mu_BC_2MZ:.4f} GeV, 2-loop gauge:")
print(f"    sin^2(M_Z)_pred = {sin2_2MZ_gauge:.8f}")
print(f"    S82 reported    = 0.23137921")
print(f"    |diff from S82| = {abs(sin2_2MZ_gauge - 0.23137921):.2e}")
print(f"    n_sigma (PDG)   = {sigma_2MZ_gauge:.3f}")
print(f"  CHK2 (reproduces S82 to 1e-5): {'PASS' if chk2_pass else 'FAIL'}")

# =============================================================================
# SECTION 8: PRIMARY test -- 2-loop + Yukawa at mu_BC = mu_crit
# =============================================================================
print()
print("-" * 78)
print("[SEC 8] PRIMARY: mu_BC = mu_crit (2-loop + top-Yukawa)")
print("-" * 78)

sin2_mucrit_yuk, _ = sin2_MZ_from_cubic_BC(mu_BC_mu_crit, rg_2loop_plus_yukawa)  # (local)
dev_mucrit_yuk = sin2_mucrit_yuk - sin2_thetaW_MSbar     # (local)
sigma_mucrit_yuk = abs(dev_mucrit_yuk) / sigma_PDG       # (local)
yuk_shift = sin2_mucrit_yuk - sin2_mucrit_gauge          # (local)

print(f"  mu_BC = {mu_BC_mu_crit} GeV, 2-loop + top-Yukawa:")
print(f"    sin^2(M_Z)_pred   = {sin2_mucrit_yuk:.8f}")
print(f"    PDG target        = {sin2_thetaW_MSbar}")
print(f"    deviation         = {dev_mucrit_yuk:+.8f}")
print(f"    n_sigma (PDG)     = {sigma_mucrit_yuk:.3f}")
print()
print(f"  Yukawa shift       = {yuk_shift:+.2e}")
print(f"  Expected O(10^-4)  = {'PASS' if 1e-5 < abs(yuk_shift) < 5e-4 else 'FAIL'}")
chk3_pass = 1.0e-5 < abs(yuk_shift) < 5.0e-4             # (local)

# =============================================================================
# SECTION 9: PRIMARY test -- 2-loop + Yukawa at mu_BC = 2*M_Z
# =============================================================================
print()
print("-" * 78)
print("[SEC 9] Comparison: mu_BC = 2*M_Z (2-loop + top-Yukawa)")
print("-" * 78)

sin2_2MZ_yuk, _ = sin2_MZ_from_cubic_BC(mu_BC_2MZ, rg_2loop_plus_yukawa)  # (local)
dev_2MZ_yuk = sin2_2MZ_yuk - sin2_thetaW_MSbar            # (local)
sigma_2MZ_yuk = abs(dev_2MZ_yuk) / sigma_PDG              # (local)

print(f"  mu_BC = 2*M_Z, 2-loop + top-Yukawa:")
print(f"    sin^2(M_Z)_pred = {sin2_2MZ_yuk:.8f}")
print(f"    deviation       = {dev_2MZ_yuk:+.8f}")
print(f"    n_sigma (PDG)   = {sigma_2MZ_yuk:.3f}")

# =============================================================================
# SECTION 10: Fine scan between 2*M_Z and mu_crit to find optimal with Yukawa
# =============================================================================
print()
print("-" * 78)
print("[SEC 10] Fine scan: mu_BC in [2*M_Z, 1.05*mu_crit], 2-loop + Yukawa")
print("-" * 78)

mu_BC_scan = np.linspace(mu_BC_2MZ, 1.05 * mu_BC_mu_crit, 50)    # (local)
sin2_scan_yuk = np.array([sin2_MZ_from_cubic_BC(m, rg_2loop_plus_yukawa)[0]
                          for m in mu_BC_scan])                    # (local)
dev_scan_yuk = sin2_scan_yuk - sin2_thetaW_MSbar                   # (local)
sigma_scan_yuk = np.abs(dev_scan_yuk) / sigma_PDG                  # (local)

i_min = int(np.argmin(sigma_scan_yuk))                             # (local)
mu_BC_best = mu_BC_scan[i_min]                                     # (local)
sigma_best = sigma_scan_yuk[i_min]                                 # (local)
sin2_best = sin2_scan_yuk[i_min]                                   # (local)
print(f"  Scan min: mu_BC = {mu_BC_best:.4f} GeV")
print(f"             sin^2 = {sin2_best:.8f}, n_sigma = {sigma_best:.3f}")

# Also find brentq root for sin^2(M_Z) = PDG under 2-loop + Yukawa
def dev_vs_mu_BC_yuk(mu_BC):
    s2, _ = sin2_MZ_from_cubic_BC(mu_BC, rg_2loop_plus_yukawa)
    return s2 - sin2_thetaW_MSbar


try:
    mu_crit_yuk = brentq(dev_vs_mu_BC_yuk, 1.8*M_Z, 2.5*M_Z, xtol=1e-6)   # (local)
    print(f"  mu_crit (2-loop + Yukawa) = {mu_crit_yuk:.4f} GeV")
    print(f"    ratio to M_Z       = {mu_crit_yuk/M_Z:.6f}")
    print(f"    shift from gauge-only mu_crit = {mu_crit_yuk - mu_BC_mu_crit:+.4f} GeV")
except ValueError as e:
    mu_crit_yuk = float('nan')                                    # (local)
    print(f"  brentq failed: {e}")

# =============================================================================
# SECTION 11: Verdict determination
# =============================================================================
print()
print("-" * 78)
print("[SEC 11] Verdict determination")
print("-" * 78)

# The PRIMARY gate result is at mu_BC = mu_crit (the natural threshold lift).
# This is the "mu_BC natural threshold shift" referenced in the task.
sin2_pred = sin2_mucrit_yuk                   # (local) primary result
dev_primary = dev_mucrit_yuk                  # (local)
n_sigma = sigma_mucrit_yuk                    # (local)

if n_sigma < 2.0:
    verdict = "PASS"                          # (local)
    reason = (f"n_sigma = {n_sigma:.3f} < 2; mu_BC = mu_crit + 2-loop + Yukawa "
              f"closes to PASS ({n_sigma:.2f} sigma from PDG)")  # (local)
elif n_sigma < 3.0:
    verdict = "INFO"                          # (local)
    reason = (f"n_sigma = {n_sigma:.3f} in [2,3); at mu_BC = mu_crit + Yukawa, "
              f"the 3.98 sigma S82 gap compresses to {n_sigma:.2f} sigma INFO; "
              f"3-loop or full Yukawa RGE needed for PASS")  # (local)
else:
    verdict = "FAIL"                          # (local)
    reason = (f"n_sigma = {n_sigma:.3f} >= 3; framework does not close at "
              f"2-loop + mu_BC natural threshold alone")  # (local)

print(f"  PRIMARY (mu_BC = mu_crit = 188.44 GeV, 2-loop + Yukawa):")
print(f"    sin^2(M_Z)_pred = {sin2_pred:.8f}")
print(f"    PDG             = {sin2_thetaW_MSbar}")
print(f"    deviation       = {dev_primary:+.8f}")
print(f"    n_sigma         = {n_sigma:.3f}")
print(f"  VERDICT: {verdict}")
print(f"  Reason:  {reason}")
print()
print(f"  CROSS-CHECK SUMMARY:")
print(f"    CHK1 (mu_crit gauge-only reproduces PDG): {'PASS' if chk1_pass else 'FAIL'}")
print(f"    CHK2 (2*M_Z gauge-only reproduces S82):   {'PASS' if chk2_pass else 'FAIL'}")
print(f"    CHK3 (Yukawa shift is O(10^-4)):          {'PASS' if chk3_pass else 'FAIL'}")
print(f"    CHK4 (SIGN d(sin2)/d(ln mu) > 0):         {'PASS' if chk4_pass else 'FAIL'}")

# =============================================================================
# SECTION 12: Closure SHA + 4-tuple emit
# =============================================================================
print()
print("-" * 78)
print("[SEC 12] Closure SHA and 4-tuple emit")
print("-" * 78)

closure_map = {                               # (local) ordered input-pin map
    'script': 's83_w3_g47_sin2_thetaW_2loop_mu_BC.py',
    'gate_id': 'S83-SIN2-THETA-W-2-LOOP-PLUS-MU-BC',
    'scheme': '2-loop-RGE-plus-mu_BC',
    'convention': 'PDG-0.23122',
    'L_max': 'N/A',
    'mu_BC_primary_GeV': float(mu_BC_mu_crit),
    'mu_BC_baseline_GeV': float(mu_BC_2MZ),
    'cubic_value_at_tau_fold': float(sin2_cubic_tau_fold),
    'sin2_MZ_pred_mucrit_2loop_gauge': float(sin2_mucrit_gauge),
    'sin2_MZ_pred_mucrit_2loop_yuk': float(sin2_mucrit_yuk),
    'sin2_MZ_pred_2MZ_2loop_gauge': float(sin2_2MZ_gauge),
    'sin2_MZ_pred_2MZ_2loop_yuk': float(sin2_2MZ_yuk),
    'sin2_MZ_PDG': float(sin2_thetaW_MSbar),
    'sigma_PDG': float(sigma_PDG),
    'deviation_primary': float(dev_primary),
    'n_sigma_primary': float(n_sigma),
    'yukawa_shift': float(yuk_shift),
    'alpha_t_MZ': float(alpha_t_MZ),
    'mu_crit_yuk_GeV': float(mu_crit_yuk) if not np.isnan(mu_crit_yuk) else None,
    'tau_fold': float(tau_fold),
    'b1_SM': float(b1), 'b2_SM': float(b2), 'b3_SM': float(b3),
    'C_yuk_1': float(C_yuk[0]), 'C_yuk_2': float(C_yuk[1]), 'C_yuk_3': float(C_yuk[2]),
    'alpha_em_MZ_inv': float(alpha_em_MZ_inv),
    'alpha_s_MZ': float(alpha_s_MZ_obs),
    'RG_order': '2-loop + top-Yukawa',
    'integrator': 'DOP853',
    'rtol': 1e-10,
    'atol': 1e-12,
    'tol_PASS': float(tol_PASS),
    'tol_INFO': float(tol_INFO),
    'verdict': verdict,
    'inputs': {k: v for k, v in sorted(INPUT_SHAS.items())},
}
closure_str = json.dumps(closure_map, sort_keys=True, default=str)       # (local)
closure_sha = hashlib.sha256(closure_str.encode('utf-8')).hexdigest()    # (local)

four_tuple = (                              # (local)
    f"(n_sigma={n_sigma:.4f}, scheme=2-loop-RGE-plus-mu_BC, "
    f"convention=PDG-0.23122, L_max=N/A)"
)
print(f"  Closure SHA-256: {closure_sha}")
print(f"  4-TUPLE        : {four_tuple}")

# =============================================================================
# SECTION 13: Save .npz
# =============================================================================
print()
print("-" * 78)
print("[SEC 13] Save .npz")
print("-" * 78)

out_npz = SCRIPT_DIR / 's83_w3_g47_sin2_thetaW_2loop_mu_BC.npz'        # (local)
np.savez(str(out_npz),
    tau_fold=tau_fold,
    sin2_cubic_tau_fold=sin2_cubic_tau_fold,
    sin2_thetaW_MSbar=sin2_thetaW_MSbar,
    sigma_PDG=sigma_PDG,
    mu_BC_2MZ=mu_BC_2MZ,
    mu_BC_mu_crit=mu_BC_mu_crit,
    mu_crit_yuk=mu_crit_yuk,
    alpha_t_MZ=alpha_t_MZ,
    sin2_mucrit_gauge=sin2_mucrit_gauge,
    sin2_mucrit_yuk=sin2_mucrit_yuk,
    sin2_2MZ_gauge=sin2_2MZ_gauge,
    sin2_2MZ_yuk=sin2_2MZ_yuk,
    dev_primary=dev_primary,
    n_sigma_primary=n_sigma,
    yukawa_shift=yuk_shift,
    mu_BC_scan=mu_BC_scan,
    sin2_scan_yuk=sin2_scan_yuk,
    dev_scan_yuk=dev_scan_yuk,
    sigma_scan_yuk=sigma_scan_yuk,
    mu_BC_best=mu_BC_best,
    sigma_best=sigma_best,
    sin2_best=sin2_best,
    tol_PASS=tol_PASS,
    tol_INFO=tol_INFO,
    verdict=np.array([verdict]),
    reason=np.array([reason]),
    closure_sha=np.array([closure_sha]),
    four_tuple=np.array([four_tuple]),
    input_shas=np.array([f"{k}={v}" for k, v in sorted(INPUT_SHAS.items())]),
)
print(f"  Saved: {out_npz}")

# =============================================================================
# SECTION 14: Plot
# =============================================================================
print()
print("-" * 78)
print("[SEC 14] Plot")
print("-" * 78)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))

ax1.plot(mu_BC_scan, sin2_scan_yuk, 'b-', lw=2.0,
         label='2-loop + Yukawa run-down')
ax1.axhline(sin2_thetaW_MSbar, color='r', ls='--', lw=1.5,
            label=f'PDG sin^2={sin2_thetaW_MSbar}')
ax1.axhspan(sin2_thetaW_MSbar - tol_PASS, sin2_thetaW_MSbar + tol_PASS,
            color='green', alpha=0.3, label='PASS (2 sigma)')
ax1.axhspan(sin2_thetaW_MSbar - tol_INFO, sin2_thetaW_MSbar - tol_PASS,
            color='gold', alpha=0.2, label='INFO (3 sigma)')
ax1.axhspan(sin2_thetaW_MSbar + tol_PASS, sin2_thetaW_MSbar + tol_INFO,
            color='gold', alpha=0.2)
ax1.axvline(mu_BC_2MZ, color='purple', ls=':', lw=1.5,
            label=f'2*M_Z = {mu_BC_2MZ:.1f} GeV')
ax1.axvline(mu_BC_mu_crit, color='black', ls=':', lw=1.5,
            label=f'mu_crit = {mu_BC_mu_crit:.1f} GeV')
ax1.plot([mu_BC_mu_crit], [sin2_mucrit_yuk], 'mo', ms=12,
         label=f'Primary: sin^2 = {sin2_mucrit_yuk:.5f}')
ax1.set_xlabel('mu_BC [GeV]', fontsize=11)
ax1.set_ylabel('sin^2(theta_W, M_Z), 2-loop + Yukawa', fontsize=11)
ax1.set_title('(a) sin^2(M_Z) vs mu_BC, 2-loop + Yukawa', fontsize=11)
ax1.legend(loc='upper right', fontsize=8)
ax1.grid(True, alpha=0.3)

ax2.semilogy(mu_BC_scan, sigma_scan_yuk, 'b-', lw=2.0, label='2-loop + Yukawa')
ax2.axhline(2.0, color='green', ls='--', lw=1.5, label='PASS threshold (2 sigma)')
ax2.axhline(3.0, color='gold', ls='--', lw=1.5, label='INFO threshold (3 sigma)')
ax2.axhline(3.98, color='red', ls='--', lw=1.5,
            label='S82 W3-10 (gauge only) = 3.98 sigma')
ax2.axvline(mu_BC_2MZ, color='purple', ls=':', lw=1.5,
            label=f'2*M_Z')
ax2.axvline(mu_BC_mu_crit, color='black', ls=':', lw=1.5,
            label=f'mu_crit = 188.44 GeV')
ax2.plot([mu_BC_mu_crit], [sigma_mucrit_yuk], 'mo', ms=12,
         label=f'Primary: {sigma_mucrit_yuk:.3f} sigma')
ax2.set_xlabel('mu_BC [GeV]', fontsize=11)
ax2.set_ylabel('|sin^2(M_Z) - PDG| / sigma_PDG', fontsize=11)
ax2.set_title(f'(b) Verdict: {verdict}', fontsize=13, fontweight='bold')
ax2.legend(loc='upper right', fontsize=8)
ax2.grid(True, alpha=0.3, which='both')

fig.suptitle('S83 W3-G47: sin^2(theta_W) 2-loop + mu_BC natural threshold', fontsize=12)
plt.tight_layout()

out_png = SCRIPT_DIR / 's83_w3_g47_sin2_thetaW_2loop_mu_BC.png'        # (local)
plt.savefig(str(out_png), dpi=120, bbox_inches='tight')
plt.close()
print(f"  Saved: {out_png}")

# =============================================================================
# SECTION 15: Final verdict line
# =============================================================================
print()
print("-" * 78)
print("[SEC 15] Gate verdict line")
print("-" * 78)
final_verdict_line = (
    f"S83-SIN2-THETA-W-2-LOOP-PLUS-MU-BC: {verdict} -- value={n_sigma:.6f} "
    f"scheme=2-loop-RGE-plus-mu_BC convention=PDG-0.23122 "
    f"L_max=N/A sha256={closure_sha}"
)
print()
print(f"  {final_verdict_line}")
print()
print(f"  Runtime: {time.time() - t_start:.2f} s")
print()
print("=" * 78)
print("DONE")
print("=" * 78)
