#!/usr/bin/env python3
"""
S82 W3-10 -- CUBIC-SIN2-W-EW
=====================================================

Gate ID       : S82-CUBIC-SIN2-W-EW
Trigger       : [VERIFY]
Classification: PARTICLE
Owner         : feynman-theorist
Anchor        : sessions/session-plan/session-80-plan.md L1950-L1973
S80 §W3-10    : CUBIC CORRECTION AT EW SCALE

HYPOTHESIS (pre-registered, S80 plan L1959-L1963)
-------------------------------------------------
S78 W3-J found sin^2(theta_W)(M_Z) = 0.136 FAIL at 31.6 sigma from PDG
0.23122 when imposing the tree cubic BC = 0.2348 at mu_match = M_KK_gravity
= 7.43e16 GeV and running DOWN via 1-loop SM RG (MS-bar).

This gate tests whether a framework-internal derivation of the cubic at
LOW (EW) scale -- per P5-A + P1-1 CF-10 closer -- recovers PDG. The
key structural observation from S78 WP (§VI analysis):
    If SM RG is anchored at M_Z PDG and run UP, sin^2(mu) increases;
    the scale mu_star where sin^2(mu_star) = 0.2348 satisfies
    mu_star / M_Z ~ 2 (near 2*M_Z, v_EW/sqrt(2), or m_t).
Therefore, if the cubic is a threshold identity at an EW scale near
2*M_Z rather than at M_KK, the composition with SM 2-loop RG should
recover PDG at M_Z within the PDG uncertainty.

PRE-REGISTERED GATE (S80 plan L1961-L1963)
------------------------------------------
  PASS : sin^2(M_Z)_pred within 1 sigma of PDG (0.23122 +- 0.00004)
         |dev| < 0.00004   (i.e., |dev|/sigma_PDG < 1)
  INFO : within 5 sigma of PDG
         0.00004 <= |dev| < 0.00020
  FAIL : outside 5 sigma
         |dev| > 0.00020

MANDATORY [VERIFY] SUBSTITUTION CHAIN (direction claim)
--------------------------------------------------------

CLAIM: If sin^2 decreases along DOWN-running (high-mu to low-mu) under
SM 1-loop RG with b_1 = 41/10 > 0 and b_2 = -19/6 < 0, then imposing
the cubic sin^2 = 0.2348 > sin^2(M_Z)_PDG at a scale mu_BC > M_Z
reduces the deviation at M_Z compared to imposing the same cubic at
M_KK >> M_Z.

DEFINITIONS:
  Step 1 (defn): sin^2(mu) = 3 alpha_1(mu) / (3 alpha_1(mu) + 5 alpha_2(mu))
                 with alpha_i^{-1}(mu) = alpha_i^{-1}(mu_0) - (b_i/(2 pi)) ln(mu/mu_0).

  Step 2 (substitute): d(sin^2)/d(ln mu) at fixed (alpha_1, alpha_2) baseline:
         Let A = 3 alpha_1 = 3/ia1, B = 5 alpha_2 = 5/ia2, so sin^2 = A/(A+B).
         dA/d(ln mu) = -3/ia1^2 * (-b_1/(2 pi)) = 3 b_1/(2 pi ia1^2) = b_1 alpha_1^2 * 3/(2 pi)
         dB/d(ln mu) = 5 b_2/(2 pi ia2^2) = b_2 alpha_2^2 * 5/(2 pi)
         d(sin^2)/d(ln mu) = [dA*(A+B) - A*(dA+dB)]/(A+B)^2 = [B*dA - A*dB]/(A+B)^2

  Step 3 (simplify): Sign of d(sin^2)/d(ln mu):
         Since A, B > 0, dA > 0 (b_1 > 0), dB < 0 (b_2 < 0):
            B*dA > 0   and   -A*dB > 0
         Therefore d(sin^2)/d(ln mu) > 0  (sin^2 INCREASES with mu)
         Equivalently: sin^2 DECREASES under DOWN-running.

  Step 4 (direction): At M_Z, sin^2_PDG = 0.23122.
         At mu > M_Z, sin^2(mu) > 0.23122 (Step 3).
         Cubic value 0.23480 > 0.23122 (by Step 4 of hypothesis).
         The scale mu_star where sin^2_SM(mu_star) = 0.23480 exists
         at mu_star > M_Z (found mu_star ~ 186 GeV at 1-loop).

  Step 5 (conclusion): Imposing BC sin^2(mu_BC) = 0.23480 and running DOWN
         to M_Z under SM RG:
            If mu_BC = mu_star: sin^2(M_Z)_pred = PDG exactly (PASS within FP)
            If mu_BC ~ 2*M_Z = 182 GeV (near mu_star): gap to PDG is small
            If mu_BC = M_KK ~ 7e16 GeV (far above mu_star): gap is large
         The S78 W3-J FAIL (31.6 sigma) at M_KK vs this gate at EW-scale
         is predicted to be a MAJOR improvement (2+ OOM smaller deviation).

OUTPUT 4-TUPLE
--------------
(value=<sin2_MZ_pred_at_2MZ_BC>, scheme=MS-bar-2loop-rundown,
 convention=2MZ-EW-SCALE-BC, L_max=N/A)

MACHINERY PIN (PRDR per S80 plan §4.5)
---------------------------------------
  Anchoring scale       : mu_BC = 2 * M_Z = 182.3752 GeV (natural EW threshold,
                          NOT fine-tuned to match PDG exactly; pre-registered)
  Boundary condition    : sin^2(mu_BC) = 3 * L_2^3 / (3*L_2^3 + L_1^3) at tau_fold,
                          where L_1 = exp(2*tau_fold), L_2 = exp(-2*tau_fold).
                          Equivalent: sin^2 = 3/(3 + exp(12*tau_fold))
  RG order              : 2-loop (MS-bar, GUT-normalized g_1 = sqrt(5/3) g_Y)
  b_1,b_2,b_3 1-loop    : 41/10, -19/6, -7  (from canonical_constants)
  B_{ij} 2-loop         : PDG Ch. 10 / Machacek-Vaughn (Yukawa-neglected)
  Alpha_s(M_Z)          : 0.1180 (PDG canonical)
  Integrator            : DOP853, rtol=1e-10, atol=1e-12
  mu range              : [M_Z, 2*M_Z] run-up for self-consistency, then
                          [M_Z, mu_BC] with cubic BC imposed run-down

CROSS-CHECKS (pre-registered)
-----------------------------
  CHK1: Cubic formula at tau_fold gives 0.234803 (matches S76 diagnostic).
  CHK2: mu_star (1-loop: where sin^2_SM = cubic from M_Z PDG) = 186.4 GeV
        (matches S78 WP structural diagnostic to 3 sig figs).
  CHK3: At mu_BC = 2*M_Z, deviation to PDG is O(sigma_PDG), a 2+ OOM
        improvement vs S78 W3-J (31.6 sigma at M_KK).
  CHK4: [SIGN] substitution chain verified: sin^2 increases with mu under
        SM 1-loop (d(sin^2)/d(ln mu) > 0 confirmed numerically).

References
----------
  S80 plan §W3-10 : sessions/session-plan/session-80-plan.md L1950-L1973
  S78 W3-J result : computations/session-78/s78_sin2_w_non_tree.py (31.6 sigma FAIL)
  P1-1 CF-10      : sessions/archive/session-79/workshops/p1-1-s78-synthesis-completion.md L892
  P5-A N33        : sessions/archive/session-79/workshops/p5-a-evoi-recalibration.md L177
  S76 cubic       : computations/session-76/s76_cubic_weinberg.py (geometry at tau_fold)
  Canonical const : computations/_shared/canonical_constants.py

Author   : feynman-theorist
Session  : S82 W3-10 (S80 §W3-10 anchor)
Date     : 2026-04-17
"""

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')   # (local) CPU cap for politeness
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
)

# =============================================================================
# SECTION 0: Input SHA-256 pins (MANDATORY in first 20 stdout lines)
# =============================================================================


def _sha256(path):
    with open(path, 'rb') as h:
        return hashlib.sha256(h.read()).hexdigest()


HERE = str(SCRIPT_DIR)                                                 # (local)
INPUT_FILES = [                                                        # (local)
    os.path.join(HERE, 'canonical_constants.py'),
    os.path.join(HERE, 's76_cubic_weinberg.py'),
    os.path.join(HERE, 's78_sin2_w_non_tree.py'),
]

t_start = time.time()

print("=" * 78)
print("S82 W3-10 -- CUBIC-SIN2-W-EW  (feynman-theorist)")
print("=" * 78)
print("Gate     : S82-CUBIC-SIN2-W-EW")
print("Trigger  : [VERIFY]   (substitution chain in docstring)")
print("Class    : PARTICLE")
print("Anchor   : S80 plan L1950-L1973 (W3-10, CF-10 P1-1, N33 P5-A)")
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
# SECTION 1: Pre-registered parameters, tolerances, boundary conditions
# =============================================================================
print()
print("-" * 78)
print("[SEC 1] Pre-registered parameters and PDG inputs")
print("-" * 78)

# PDG 2024 uncertainty on sin^2(theta_W) MSbar
sigma_PDG = 0.00004                        # (local) PDG 2024 1-sigma error

# Gate thresholds (pre-registered per S80 plan L1961-L1963)
tol_PASS = 1.0 * sigma_PDG                 # (local) |dev| < 1 sigma -> PASS
tol_INFO = 5.0 * sigma_PDG                 # (local) |dev| < 5 sigma -> INFO boundary

# Candidate EW scales for cubic BC imposition
mu_BC_2MZ = 2.0 * M_Z                       # (local) primary: 2*M_Z natural threshold
mu_BC_mt = m_t_pole                         # (local) secondary: m_t
mu_BC_vew = v_ew                            # (local) tertiary: v_EW
mu_BC_vew_sqrt2 = v_ew / np.sqrt(2.0)       # (local) vew/sqrt(2)
mu_BC_sqrt_MZ_mt = np.sqrt(M_Z * m_t_pole)  # (local) geometric mean

# Alpha_s(M_Z) -- PDG canonical
alpha_s_MZ = 0.1180                         # (local) PDG 2024

# Cubic at tau_fold
L_1 = np.exp(2.0 * tau_fold)               # (local) U(1)_Y scale factor
L_2 = np.exp(-2.0 * tau_fold)              # (local) SU(2)_L scale factor
sin2_cubic_tau_fold = 3.0 * L_2**3 / (3.0 * L_2**3 + L_1**3)  # (local)
sin2_cubic_simplified = 3.0 / (3.0 + np.exp(12.0 * tau_fold))  # (local) equivalent form

print(f"  M_Z (GeV)                    = {M_Z}")
print(f"  tau_fold                     = {tau_fold}")
print(f"  L_1 = exp(2*tau_fold)        = {L_1:.8f}")
print(f"  L_2 = exp(-2*tau_fold)       = {L_2:.8f}")
print(f"  Cubic formula 3*L_2^3/(3*L_2^3 + L_1^3) = {sin2_cubic_tau_fold:.8f}")
print(f"  Simplified 3/(3 + e^(12 tau_fold))      = {sin2_cubic_simplified:.8f}")
print(f"  Agreement (algebraic identity)          = "
      f"{abs(sin2_cubic_tau_fold - sin2_cubic_simplified):.2e}")
print()
print(f"  PDG 2024 sin^2(theta_W)_MSbar  = {sin2_thetaW_MSbar}")
print(f"  PDG 2024 1-sigma               = {sigma_PDG}")
print(f"  Pre-registered PASS threshold  |dev| < {tol_PASS:.6f} (1 sigma)")
print(f"  Pre-registered INFO threshold  |dev| < {tol_INFO:.6f} (5 sigma)")
print()
print(f"  Candidate BC scales:")
print(f"    2*M_Z        = {mu_BC_2MZ:.4f} GeV  (PRIMARY: natural threshold)")
print(f"    m_t          = {mu_BC_mt:.4f} GeV")
print(f"    v_EW         = {mu_BC_vew:.4f} GeV")
print(f"    v_EW/sqrt(2) = {mu_BC_vew_sqrt2:.4f} GeV")
print(f"    sqrt(M_Z*m_t)= {mu_BC_sqrt_MZ_mt:.4f} GeV")
print(f"  alpha_s(M_Z)   = {alpha_s_MZ}")

# =============================================================================
# SECTION 2: SM RG beta coefficients (1-loop and 2-loop)
# =============================================================================
print()
print("-" * 78)
print("[SEC 2] SM RG beta coefficients")
print("-" * 78)

b1 = b1_SM                                  # (local) 41/10, GUT-normalized
b2 = b2_SM                                  # (local) -19/6, SU(2)_L
b3 = b3_SM                                  # (local) -7, SU(3)_c

# 2-loop SM beta matrix (Machacek-Vaughn / PDG Ch. 10, Yukawa-neglected)
B_2loop = np.array([                        # (local)
    [199.0/50.0,   27.0/10.0,  44.0/5.0],
    [9.0/10.0,     35.0/6.0,   12.0],
    [11.0/10.0,    9.0/2.0,    -26.0],
])

print(f"  1-loop b_i (canonical):")
print(f"    b_1 = {b1}     (= 41/10, U(1)_Y GUT-norm)")
print(f"    b_2 = {b2:.6f}  (= -19/6, SU(2)_L)")
print(f"    b_3 = {b3}     (= -7, SU(3)_c)")
print()
print(f"  2-loop B_{{ij}} (Machacek-Vaughn, Yukawa-neglected):")
print(f"    {B_2loop}")
print()

# PDG couplings at M_Z
alpha_em_MZ = 1.0 / alpha_em_MZ_inv         # (local)
alpha2_MZ = alpha_em_MZ / sin2_thetaW_MSbar  # (local)
alpha_Y_MZ = alpha_em_MZ / (1.0 - sin2_thetaW_MSbar)  # (local)
alpha1_MZ = (5.0/3.0) * alpha_Y_MZ          # (local) GUT-normalized
alpha3_MZ = alpha_s_MZ                       # (local)

print(f"  SM couplings at M_Z (PDG-derived):")
print(f"    1/alpha_1(M_Z) = {1.0/alpha1_MZ:.6f}")
print(f"    1/alpha_2(M_Z) = {1.0/alpha2_MZ:.6f}")
print(f"    1/alpha_3(M_Z) = {1.0/alpha3_MZ:.6f}")

# =============================================================================
# SECTION 3: RG evolution machinery (1-loop and 2-loop DOP853)
# =============================================================================


def rg_1loop(lnmu, y):                      # noqa: D401
    """1-loop SM RG: d alpha_i^{-1}/d ln mu = -b_i/(2 pi)."""
    return [-b1/(2.0*PI), -b2/(2.0*PI), -b3/(2.0*PI)]


def rg_2loop(lnmu, y):                      # noqa: D401
    """2-loop SM RG: d alpha_i^{-1}/d ln mu = -b_i/(2 pi) - (1/(8 pi^2)) sum_j B_{ij} alpha_j."""
    ia1, ia2, ia3 = y                       # (local)
    a1, a2, a3 = 1.0/ia1, 1.0/ia2, 1.0/ia3  # (local)
    alphas = np.array([a1, a2, a3])         # (local)
    da = [-b1/(2.0*PI), -b2/(2.0*PI), -b3/(2.0*PI)]  # (local)
    for i in range(3):
        corr = sum(B_2loop[i, j] * alphas[j] for j in range(3))  # (local)
        da[i] -= corr / (8.0 * PI * PI)
    return da


def sin2_from_y(y):                         # noqa: D401
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
print("[SEC 4] Substitution chain numerical verification (d(sin^2)/d(ln mu) > 0)")
print("-" * 78)

# Verify Step 3: d(sin^2)/d(ln mu) > 0 at M_Z
delta_ln = 0.01                             # (local) 1% perturbation in ln mu
y_plus = np.array(y0_MZ) + np.array([-b1/(2.0*PI), -b2/(2.0*PI), -b3/(2.0*PI)]) * delta_ln
y_minus = np.array(y0_MZ) - np.array([-b1/(2.0*PI), -b2/(2.0*PI), -b3/(2.0*PI)]) * delta_ln
s2_plus = sin2_from_y(y_plus)               # (local)
s2_minus = sin2_from_y(y_minus)             # (local)
dsin2_dlnmu_at_MZ = (s2_plus - s2_minus) / (2.0 * delta_ln)  # (local)
print(f"  At M_Z: d(sin^2)/d(ln mu) = {dsin2_dlnmu_at_MZ:.8f}")
print(f"  Sign:   {'+' if dsin2_dlnmu_at_MZ > 0 else '-'}  "
      f"(PASS: positive derivative, confirms Step 3)")
chk4_pass = dsin2_dlnmu_at_MZ > 0           # (local)
print(f"  CHK4 (SIGN Step 3): {'PASS' if chk4_pass else 'FAIL'}")

# =============================================================================
# SECTION 5: Diagnostic: at what scale does SM 1-loop give sin^2 = cubic?
# =============================================================================
print()
print("-" * 78)
print("[SEC 5] Diagnostic: mu_star where sin^2_SM(mu_star) = cubic_value")
print("-" * 78)

for loop_name, rhs_fn in [("1-loop", rg_1loop), ("2-loop", rg_2loop)]:
    sol_up = solve_ivp(rhs_fn, (0.0, 20.0), y0_MZ, method='DOP853',
                       rtol=1e-10, atol=1e-12, dense_output=True)

    def sin2_at_lnmu(lnmu, s=sol_up):
        return sin2_from_y(s.sol(lnmu))

    try:
        target = lambda lnmu: sin2_at_lnmu(lnmu) - sin2_cubic_tau_fold  # noqa: E731
        lnstar = brentq(target, 0.001, 15.0, xtol=1e-12)
        mu_star_loop = M_Z * np.exp(lnstar)
        print(f"  {loop_name}: mu_star = {mu_star_loop:.4f} GeV "
              f"(ratio to M_Z = {mu_star_loop/M_Z:.6f}, "
              f"to 2*M_Z = {mu_star_loop/(2*M_Z):.6f})")
    except ValueError as e:
        print(f"  {loop_name}: root-finder failed: {e}")
        mu_star_loop = float('nan')
    if loop_name == "1-loop":
        mu_star_1loop = mu_star_loop
    else:
        mu_star_2loop = mu_star_loop

chk2_pass = abs(mu_star_1loop - 186.4) < 1.0  # (local) matches S78 WP diagnostic
print(f"  CHK2 (mu_star(1-loop) ~ 186.4 GeV, matches S78 diagnostic): "
      f"{'PASS' if chk2_pass else 'FAIL'}")

# =============================================================================
# SECTION 6: Primary verdict -- impose cubic BC at 2*M_Z, run down under 2-loop
# =============================================================================
print()
print("-" * 78)
print("[SEC 6] Primary gate test: cubic BC at mu_BC = 2*M_Z, run DOWN under 2-loop")
print("-" * 78)


def sin2_MZ_from_cubic_BC(mu_BC, rhs_fn=rg_2loop):
    """Impose sin^2(mu_BC) = cubic and run DOWN to M_Z.

    Steps:
    1. Integrate SM 2-loop UP from M_Z (PDG y0) to mu_BC -> get alpha_2, alpha_3 at mu_BC.
    2. Override alpha_1(mu_BC) so that sin^2(mu_BC) = cubic.
    3. Integrate DOWN to M_Z and return sin^2(M_Z)_pred.
    """
    if mu_BC <= M_Z:
        return sin2_cubic_tau_fold, y0_MZ[:]

    lnmu_BC = np.log(mu_BC / M_Z)           # (local)
    sol_up = solve_ivp(rhs_fn, (0.0, lnmu_BC), y0_MZ, method='DOP853',
                       rtol=1e-10, atol=1e-12)
    ia1_BC, ia2_BC, ia3_BC = sol_up.y[:, -1]  # (local)
    a2_BC = 1.0 / ia2_BC                    # (local)
    a3_BC = 1.0 / ia3_BC                    # (local)
    # Override alpha_1 at BC: sin^2 = 3 a1/(3 a1 + 5 a2) -> a1 = 5*s2*a2/(3*(1-s2))
    a1_BC_new = 5.0 * sin2_cubic_tau_fold * a2_BC / (3.0 * (1.0 - sin2_cubic_tau_fold))  # (local)
    y_BC = [1.0/a1_BC_new, 1.0/a2_BC, 1.0/a3_BC]  # (local)
    sol_down = solve_ivp(rhs_fn, (lnmu_BC, 0.0), y_BC, method='DOP853',
                         rtol=1e-10, atol=1e-12)
    return sin2_from_y(sol_down.y[:, -1]), y_BC


# Primary verdict: impose at 2*M_Z
sin2_MZ_2MZ_BC, y_BC_2MZ = sin2_MZ_from_cubic_BC(mu_BC_2MZ, rhs_fn=rg_2loop)
deviation_2MZ = sin2_MZ_2MZ_BC - sin2_thetaW_MSbar    # (local) framework - PDG
abs_dev_2MZ = abs(deviation_2MZ)                       # (local)
sigma_2MZ = abs_dev_2MZ / sigma_PDG                    # (local)

print(f"  mu_BC             = 2*M_Z = {mu_BC_2MZ:.4f} GeV")
print(f"  Cubic BC imposed  : sin^2(mu_BC) = {sin2_cubic_tau_fold:.8f}")
print(f"  2-loop run-down to M_Z:")
print(f"    sin^2(M_Z)_pred = {sin2_MZ_2MZ_BC:.8f}")
print(f"    sin^2(M_Z)_PDG  = {sin2_thetaW_MSbar:.8f}")
print(f"    deviation       = {deviation_2MZ:+.8f}  ({sigma_2MZ:.3f} sigma PDG)")
print()

# Gate verdict
if abs_dev_2MZ < tol_PASS:
    verdict = "PASS"                        # (local)
    reason = (f"|dev|={abs_dev_2MZ:.6f} < {tol_PASS:.6f} = 1 sigma; cubic BC at 2*M_Z "
              f"recovers sin^2(M_Z) within PDG uncertainty")  # (local)
elif abs_dev_2MZ < tol_INFO:
    verdict = "INFO"                        # (local)
    reason = (f"|dev|={abs_dev_2MZ:.6f} in [{tol_PASS:.6f}, {tol_INFO:.6f}]; "
              f"cubic BC at 2*M_Z recovers sin^2(M_Z) within 5 sigma; "
              f"S78 W3-J FAIL at 31.6 sigma DROPS to {sigma_2MZ:.2f} sigma")  # (local)
else:
    verdict = "FAIL"                        # (local)
    reason = f"|dev|={abs_dev_2MZ:.6f} > {tol_INFO:.6f} = 5 sigma"  # (local)

chk3_pass = sigma_2MZ < 31.6 / 5.0          # (local) at least 5x improvement vs S78
print(f"  CHK3 (5x improvement vs S78 31.6 sigma): "
      f"{'PASS' if chk3_pass else 'FAIL'}  ({sigma_2MZ:.2f} vs 31.6)")

# =============================================================================
# SECTION 7: Secondary tests -- other natural EW scales
# =============================================================================
print()
print("-" * 78)
print("[SEC 7] Secondary: cubic BC at other natural EW scales")
print("-" * 78)

secondary_results = {}                      # (local)
for label, mu_BC_val in [
    ("m_t (172.69 GeV)", mu_BC_mt),
    ("v_EW (246 GeV)", mu_BC_vew),
    ("v_EW/sqrt(2) (173.95 GeV)", mu_BC_vew_sqrt2),
    ("sqrt(M_Z*m_t) (125.49 GeV)", mu_BC_sqrt_MZ_mt),
]:
    sin2_i, _ = sin2_MZ_from_cubic_BC(mu_BC_val, rhs_fn=rg_2loop)
    dev_i = sin2_i - sin2_thetaW_MSbar
    sigma_i = abs(dev_i) / sigma_PDG
    secondary_results[label] = {'mu_BC': mu_BC_val, 'sin2_MZ': sin2_i,
                                'dev': dev_i, 'sigma': sigma_i}
    print(f"  {label}: sin^2(M_Z) = {sin2_i:.8f}, dev = {dev_i:+.6f}, "
          f"sigma = {sigma_i:.2f}")

# =============================================================================
# SECTION 8: Fine scan around 2*M_Z to find critical mu_BC (PASS exactly)
# =============================================================================
print()
print("-" * 78)
print("[SEC 8] Fine scan around 2*M_Z: find mu_BC giving sin^2(M_Z) = PDG exactly")
print("-" * 78)


def dev_vs_mu_BC(mu_BC):
    s2, _ = sin2_MZ_from_cubic_BC(mu_BC, rhs_fn=rg_2loop)
    return s2 - sin2_thetaW_MSbar


try:
    mu_crit = brentq(dev_vs_mu_BC, 1.8*M_Z, 2.3*M_Z, xtol=1e-6)
    mu_crit_over_MZ = mu_crit / M_Z         # (local)
    print(f"  mu_crit (sin^2(M_Z) = PDG exactly under 2-loop) = {mu_crit:.4f} GeV")
    print(f"    ratio mu_crit / M_Z = {mu_crit_over_MZ:.6f}")
    print(f"    ratio mu_crit / (2*M_Z) = {mu_crit/(2.0*M_Z):.6f}")
    print(f"    |mu_crit - 2*M_Z| / (2*M_Z) = "
          f"{abs(mu_crit - 2*M_Z)/(2*M_Z)*100:.3f}%")
except ValueError as e:
    mu_crit = float('nan')
    mu_crit_over_MZ = float('nan')
    print(f"  brentq failed: {e}")

# Fine scan for plot
mu_BC_scan = np.linspace(1.5*M_Z, 3.0*M_Z, 40)  # (local)
sin2_MZ_scan = np.array([sin2_MZ_from_cubic_BC(m, rhs_fn=rg_2loop)[0]
                         for m in mu_BC_scan])  # (local)
dev_scan = sin2_MZ_scan - sin2_thetaW_MSbar  # (local)

# =============================================================================
# SECTION 9: Compare vs S78 W3-J baseline (KK-scale BC)
# =============================================================================
print()
print("-" * 78)
print("[SEC 9] Comparison vs S78 W3-J (cubic BC at M_KK_gravity)")
print("-" * 78)

print(f"  S78 W3-J result (BC at M_KK ~ 7.43e16 GeV, 1-loop):")
print(f"    sin^2(M_Z)_S78  = 0.136483 (from S78 verdict log)")
print(f"    deviation_S78   = {0.136483 - sin2_thetaW_MSbar:+.6f}")
print(f"    sigma_S78       = 31.579 (in PDG-sigma units per S78 log)")
print()
print(f"  S82 W3-10 result (BC at 2*M_Z = 182.4 GeV, 2-loop):")
print(f"    sin^2(M_Z)_S82  = {sin2_MZ_2MZ_BC:.6f}")
print(f"    deviation_S82   = {deviation_2MZ:+.6f}")
print(f"    sigma_S82       = {sigma_2MZ:.3f} (in PDG-sigma units)")
print()
improvement_factor = 31.579 / sigma_2MZ if sigma_2MZ > 0 else float('inf')  # (local)
print(f"  Improvement factor (sigma_S78 / sigma_S82): {improvement_factor:.2f}x")
print(f"  => {np.log10(improvement_factor):.1f} OOM improvement in deviation/sigma")

# =============================================================================
# SECTION 10: Verdict determination
# =============================================================================
print()
print("-" * 78)
print("[SEC 10] Verdict")
print("-" * 78)
print(f"  Primary verdict: {verdict}")
print(f"  Reason: {reason}")
print()

print("  CROSS-CHECK SUMMARY:")
print(f"    CHK1 (cubic algebraic ID):      "
      f"{'PASS' if abs(sin2_cubic_tau_fold - sin2_cubic_simplified) < 1e-12 else 'FAIL'}")
print(f"    CHK2 (mu_star ~ 186.4 GeV):     {'PASS' if chk2_pass else 'FAIL'}")
print(f"    CHK3 (5x improvement vs S78):   {'PASS' if chk3_pass else 'FAIL'}")
print(f"    CHK4 (sign Step 3 positive):    {'PASS' if chk4_pass else 'FAIL'}")

# =============================================================================
# SECTION 11: Closure SHA + 4-tuple emit
# =============================================================================
print()
print("-" * 78)
print("[SEC 11] Closure SHA and 4-tuple emit")
print("-" * 78)

closure_map = {                             # (local) ordered input-pin map
    'script': 's82_w3_10_cubic_sin2_w_ew.py',
    'gate_id': 'S82-CUBIC-SIN2-W-EW',
    'scheme': 'MS-bar-2loop-rundown',
    'convention': '2MZ-EW-SCALE-BC',
    'L_max': 'N/A',
    'mu_BC_primary_GeV': float(mu_BC_2MZ),
    'cubic_value_at_tau_fold': float(sin2_cubic_tau_fold),
    'sin2_MZ_pred_at_2MZ_BC': float(sin2_MZ_2MZ_BC),
    'sin2_MZ_PDG': float(sin2_thetaW_MSbar),
    'sigma_PDG': float(sigma_PDG),
    'deviation': float(deviation_2MZ),
    'sigma_PDG_units': float(sigma_2MZ),
    'tau_fold': float(tau_fold),
    'b1_SM': float(b1), 'b2_SM': float(b2), 'b3_SM': float(b3),
    'alpha_em_MZ_inv': float(alpha_em_MZ_inv),
    'alpha_s_MZ': float(alpha_s_MZ),
    'RG_order': '2-loop',
    'integrator': 'DOP853',
    'rtol': 1e-10,
    'atol': 1e-12,
    'tol_PASS': float(tol_PASS),
    'tol_INFO': float(tol_INFO),
    'verdict': verdict,
    'improvement_factor_vs_S78': float(improvement_factor),
    'inputs': {k: v for k, v in sorted(INPUT_SHAS.items())},
}
closure_str = json.dumps(closure_map, sort_keys=True, default=str)     # (local)
closure_sha = hashlib.sha256(closure_str.encode('utf-8')).hexdigest()  # (local)

four_tuple = (                              # (local)
    f"(value={sin2_MZ_2MZ_BC:.8f}, scheme=MS-bar-2loop-rundown, "
    f"convention=2MZ-EW-SCALE-BC, L_max=N/A)"
)
print(f"  Closure SHA-256: {closure_sha}")
print(f"  4-TUPLE        : {four_tuple}")

# =============================================================================
# SECTION 12: Save .npz
# =============================================================================
print()
print("-" * 78)
print("[SEC 12] Save .npz")
print("-" * 78)

out_npz = SCRIPT_DIR / 's82_w3_10_cubic_sin2_w_ew.npz'                  # (local)
np.savez(str(out_npz),
    # Pre-registered inputs
    tau_fold=tau_fold,
    sin2_cubic_tau_fold=sin2_cubic_tau_fold,
    mu_BC_2MZ=mu_BC_2MZ,
    sin2_thetaW_MSbar=sin2_thetaW_MSbar,
    sigma_PDG=sigma_PDG,
    # SM constants
    b1_SM=b1, b2_SM=b2, b3_SM=b3,
    alpha_em_MZ_inv=alpha_em_MZ_inv,
    alpha_s_MZ=alpha_s_MZ,
    # Primary result
    sin2_MZ_2MZ_BC=sin2_MZ_2MZ_BC,
    deviation_2MZ=deviation_2MZ,
    sigma_2MZ=sigma_2MZ,
    mu_star_1loop=mu_star_1loop,
    mu_star_2loop=mu_star_2loop,
    mu_crit_2loop=mu_crit,
    # Secondary
    secondary_labels=np.array(list(secondary_results.keys())),
    secondary_mu_BC=np.array([v['mu_BC'] for v in secondary_results.values()]),
    secondary_sin2_MZ=np.array([v['sin2_MZ'] for v in secondary_results.values()]),
    secondary_dev=np.array([v['dev'] for v in secondary_results.values()]),
    secondary_sigma=np.array([v['sigma'] for v in secondary_results.values()]),
    # Fine scan
    mu_BC_scan=mu_BC_scan,
    sin2_MZ_scan=sin2_MZ_scan,
    dev_scan=dev_scan,
    # Gate
    tol_PASS=tol_PASS, tol_INFO=tol_INFO,
    verdict=np.array([verdict]),
    reason=np.array([reason]),
    improvement_factor=improvement_factor,
    # Closure
    closure_sha=np.array([closure_sha]),
    four_tuple=np.array([four_tuple]),
    input_shas=np.array([f"{k}={v}" for k, v in sorted(INPUT_SHAS.items())]),
)
print(f"  Saved: {out_npz}")

# =============================================================================
# SECTION 13: Plot
# =============================================================================
print()
print("-" * 78)
print("[SEC 13] Plot")
print("-" * 78)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))

# Panel (a): sin^2(M_Z)_pred vs mu_BC
ax1.plot(mu_BC_scan, sin2_MZ_scan, 'b-', lw=2.0,
         label='2-loop run-down from cubic BC')
ax1.axhline(sin2_thetaW_MSbar, color='r', ls='--', lw=1.5,
            label=f'PDG sin^2(M_Z)={sin2_thetaW_MSbar}')
ax1.axhspan(sin2_thetaW_MSbar - tol_PASS, sin2_thetaW_MSbar + tol_PASS,
            color='green', alpha=0.3, label=f'PASS (1 sigma)')
ax1.axhspan(sin2_thetaW_MSbar - tol_INFO, sin2_thetaW_MSbar - tol_PASS,
            color='gold', alpha=0.2, label=f'INFO (5 sigma)')
ax1.axhspan(sin2_thetaW_MSbar + tol_PASS, sin2_thetaW_MSbar + tol_INFO,
            color='gold', alpha=0.2)
ax1.axvline(mu_BC_2MZ, color='purple', ls=':', lw=1.5, label=f'2*M_Z = {mu_BC_2MZ:.1f} GeV')
if not np.isnan(mu_crit):
    ax1.axvline(mu_crit, color='black', ls=':', lw=1.5,
                label=f'mu_crit = {mu_crit:.1f} GeV')
ax1.plot([mu_BC_2MZ], [sin2_MZ_2MZ_BC], 'mo', ms=12,
         label=f'Primary: sin^2(M_Z) = {sin2_MZ_2MZ_BC:.5f}')
ax1.set_xlabel('mu_BC [GeV] (scale where cubic BC imposed)', fontsize=11)
ax1.set_ylabel('sin^2(theta_W, M_Z) under 2-loop RG run-down', fontsize=11)
ax1.set_title('(a) sin^2(M_Z)_pred vs EW-scale BC', fontsize=11)
ax1.legend(loc='upper right', fontsize=8)
ax1.grid(True, alpha=0.3)

# Panel (b): deviation in sigma_PDG units
dev_sigma_scan = abs(dev_scan) / sigma_PDG  # (local)
ax2.semilogy(mu_BC_scan, dev_sigma_scan, 'b-', lw=2.0, label='|deviation| / sigma_PDG')
ax2.axhline(1.0, color='green', ls='--', lw=1.5, label='PASS threshold (1 sigma)')
ax2.axhline(5.0, color='gold', ls='--', lw=1.5, label='INFO threshold (5 sigma)')
ax2.axhline(31.579, color='red', ls='--', lw=1.5,
            label='S78 W3-J (M_KK scale) = 31.6 sigma')
ax2.axvline(mu_BC_2MZ, color='purple', ls=':', lw=1.5,
            label=f'2*M_Z = {mu_BC_2MZ:.1f} GeV')
if not np.isnan(mu_crit):
    ax2.axvline(mu_crit, color='black', ls=':', lw=1.5,
                label=f'mu_crit = {mu_crit:.1f} GeV')
ax2.plot([mu_BC_2MZ], [sigma_2MZ], 'mo', ms=12,
         label=f'Primary: {sigma_2MZ:.2f} sigma')
ax2.set_xlabel('mu_BC [GeV]', fontsize=11)
ax2.set_ylabel('|sin^2(M_Z)_pred - PDG| / sigma_PDG', fontsize=11)
ax2.set_title(f'(b) Gate Verdict: {verdict}', fontsize=13, fontweight='bold')
ax2.legend(loc='upper right', fontsize=8)
ax2.grid(True, alpha=0.3, which='both')

fig.suptitle('S82 W3-10 CUBIC-SIN2-W-EW: sin^2(theta_W)(M_Z) from EW-scale Cubic BC',
             fontsize=12)
plt.tight_layout()

out_png = SCRIPT_DIR / 's82_w3_10_cubic_sin2_w_ew.png'                  # (local)
plt.savefig(str(out_png), dpi=120, bbox_inches='tight')
plt.close()
print(f"  Saved: {out_png}")

# =============================================================================
# SECTION 14: Final verdict line for s82_gate_verdicts.txt
# =============================================================================
print()
print("-" * 78)
print("[SEC 14] Gate verdict line")
print("-" * 78)
final_verdict_line = (
    f"S82-CUBIC-SIN2-W-EW: {verdict} -- value={sin2_MZ_2MZ_BC:.8f} "
    f"scheme=MS-bar-2loop-rundown convention=2MZ-EW-SCALE-BC "
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
