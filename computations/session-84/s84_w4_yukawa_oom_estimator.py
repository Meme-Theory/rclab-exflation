"""
================================================================================
S84 §W4-45   : S84-YUKAWA-OOM-ESTIMATOR (mack-cosmic-bridge)
================================================================================

Purpose
-------
  Build a closed-form analytic OOM estimator for 2-loop + Yukawa-threshold
  shifts in sin^2(theta_W)(M_Z) when the geometric cubic boundary condition
  is imposed at mu_BC > M_Z, and verify it against the actual G47 numerical
  2-loop RGE result at mu_BC ∈ {188.185, 500, 2000} GeV.

Context
-------
  S83-G47 (SIN2-THETA-W-2-LOOP-PLUS-MU-BC) pre-registered the Yukawa shift
  as O(10^-4) but the actual 2-loop numerical integration returned
  O(10^-6) — a 2 OOM overestimate.  The gap traced to (a) log-arm length
  0.73 (not 1 decade) and (b) partial cancellation between C_i coefficients.
  This gate derives an analytic linearized estimator that captures the
  correct OOM and verifies it across 3 cases.

Estimator (linearized, leading-L, top-Yukawa dominant)
------------------------------------------------------

  Δ(sin^2θ_W)|_Yuk ≈ -[15/(3+5r)²] · (C_1 - r·C_2) · α_t · L / (8π² x_2)

  where:
    r    = x_1/x_2  with x_i = 1/α_i (GUT-normalized for i=1)
    L    = ln(μ_BC/M_Z)  (log-arm)
    α_t  = y_t²/(4π) with y_t = √2 m_t/v_EW (PDG central)
    C_1, C_2 = Mihaila-Salomon-Steinhauser 2012 / Arason et al. 1992
                2-loop top-Yukawa gauge-beta coefficients: (17/10, 3/2, 2)

  The Y_b² and Y_τ² contributions enter at O(Y_b²/Y_t²) ≈ 2.7e-4 relative
  to the top-Yukawa term (since Y_b(M_Z) ≈ 0.024, Y_τ ≈ 0.010, Y_t ≈ 0.993).
  They are retained for completeness via the modified kernel but their
  numerical contribution is < 1% even at μ_BC = 2 TeV.

  Full kernel:  K(Y_t, Y_b, Y_τ) = (C_1 - r C_2) Y_t²/(4π)²/(4π)·(4π)
    ... simplified by absorbing into α_t equivalents for each flavor.

Substitution chain [VERIFY]
---------------------------
  Step 1 (definitions):
    sin²θ_W = 3 α_1/(3 α_1 + 5 α_2) = 3/(3 + 5 r)     (dividing by α_1)
    where r = x_1/x_2 = α_2/α_1 (GUT-norm).
    At M_Z: x_1 ≈ 59.02, x_2 ≈ 29.59, r ≈ 1.995, denominator (3+5r) ≈ 12.97.

  Step 2 (differential):
    d sin² = -15/(3+5r)² · dr
    dr = (dx_1·x_2 - x_1·dx_2)/x_2² = (dx_1 - r·dx_2)/x_2

  Step 3 (substitution — Yukawa shift of x_i during downrun from μ_BC):
    Running DOWN from μ_BC to M_Z, the Yukawa contribution to x_i flips
    sign (integration bound flip):
      Δx_i|_Yuk = -C_i·α_t·L/(8π²)   (relative to gauge-only downrun)
    (top-Yukawa dominant; Y_b, Y_τ corrections additive)

  Step 4 (simplification):
    dr = [-C_1·α_t·L/(8π²) - r·(-C_2·α_t·L/(8π²))]/x_2
       = -α_t·L·(C_1 - r·C_2)/(8π² x_2)
    d(sin²) = -15/(3+5r)² · dr
            = +15·α_t·L·(C_1 - r·C_2)/(8π²·x_2·(3+5r)²)

  Step 5 (direction):
    At PDG r ≈ 1.995, C_1 = 1.7, r·C_2 = 2.99, (C_1 - r·C_2) ≈ -1.29 < 0
    ⇒ d(sin²)|_Yuk < 0  (Yukawa SUPPRESSES sin²(M_Z) relative to gauge-only
       downrun from the same cubic BC at μ_BC).

  This matches G47: yukawa_shift = sin²_mucrit_yuk - sin²_mucrit_gauge
                                 = 0.2312174 - 0.2312201 = -2.68e-6.

Method for "actual" values
--------------------------
  Case A (μ_BC = 188.185 GeV): compared to G47 yukawa_shift exactly
                                (-2.6811e-6; loaded from npz).
  Cases B, C (μ_BC = 500, 2000 GeV): full 2-loop SM RGE downrun — same
                                     machinery as G47 (SciPy DOP853, 2-loop
                                     gauge Machacek-Vaughn + top-Yukawa
                                     MSS2012 coefficient), taking the
                                     difference sin²_yuk - sin²_gauge both
                                     at M_Z with cubic BC imposed at μ_BC.

PASS/FAIL/INFO
--------------
  PASS:  max |Δ_est - Δ_actual|/|Δ_actual| ≤ 0.30 across 3 cases
  INFO:  max ∈ (0.30, 3.0)
  FAIL:  max > 3.0 → replace with full numerical 2-loop RGE for S84+ gates

Pass gives a reusable utility `_yukawa_oom_estimator.py` closing the class
of 2-loop threshold overestimates.

References
----------
  Mihaila, Salomon, Steinhauser, PRD 86 (2012) 096008 — 3-loop gauge β
      functions with Yukawa threshold corrections (MSS2012).
  Arason, Castano, Kesthelyi, Mimura, Pirard, Ramond, Wright,
      PRD 46 (1992) 3945 — 2-loop top-Yukawa gauge β contributions
      (C_1^t = 17/10, C_2^t = 3/2, C_3^t = 2) [original derivation].
  Chetyrkin, Zoller, JHEP 06 (2016) 175 — higher-order sin²θ_W thresholds.
  PDG Ch.10 (2024)  — 2-loop SM RG with Yukawa (Machacek-Vaughn conventions).
  S83 §W3-G47     — `computations/session-83/s83_w3_g47_sin2_thetaW_2loop_mu_BC.py`
  S82 W3-10       — `computations/session-82/s82_w3_10_cubic_sin2_w_ew.py`

Canonical const   : computations/_shared/canonical_constants.py

Author   : mack-cosmic-bridge
Session  : S84 W4-45
Date     : 2026-04-19
"""

import os
os.environ.setdefault('OMP_NUM_THREADS', '4')   # (local) analytic + small RGE — CPU-only
os.environ.setdefault('MKL_NUM_THREADS', '4')   # (local)

import sys
import hashlib
import time
import json
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp

SCRIPT_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPT_DIR))

from canonical_constants import (
    PI, M_Z, tau_fold,
    sin2_thetaW_MSbar, alpha_em_MZ_inv,
    b1_SM, b2_SM, b3_SM,
    v_ew, m_t_pole,
    alpha_s_MZ_obs,
)

# =============================================================================
# SECTION 0: Input SHA-256 pins (logged in first 20 lines of stdout)
# =============================================================================

def _sha256(path):
    with open(path, 'rb') as h:
        return hashlib.sha256(h.read()).hexdigest()


HERE = str(SCRIPT_DIR)                                                 # (local)
INPUT_FILES = [                                                        # (local)
    os.path.join(HERE, 'canonical_constants.py'),
    os.path.join(HERE, 's83_w3_g47_sin2_thetaW_2loop_mu_BC.py'),
    os.path.join(HERE, 's83_w3_g47_sin2_thetaW_2loop_mu_BC.npz'),
]

t_start = time.time()

print("=" * 78)
print("S84 W4-45 -- YUKAWA-OOM-ESTIMATOR (mack-cosmic-bridge)")
print("=" * 78)
print("Gate     : S84-YUKAWA-OOM-ESTIMATOR")
print("Trigger  : [VERIFY]")
print("Class    : PARTICLE")
print("Anchor   : session-84-plan-w4.md §W4-45")
print()
print("[SEC 0] Input SHA-256 pins")
INPUT_SHAS = {}                                                        # (local)
for _f in INPUT_FILES:
    if os.path.exists(_f):
        _h = _sha256(_f)                                               # (local)
        INPUT_SHAS[os.path.basename(_f)] = _h
        print(f"  {os.path.basename(_f):48s} sha256={_h[:16]}...{_h[-8:]}")
    else:
        INPUT_SHAS[os.path.basename(_f)] = None
        print(f"  {os.path.basename(_f):48s} MISSING")

# =============================================================================
# SECTION 1: Pre-registered parameters (PDG + MSS2012)
# =============================================================================
print()
print("-" * 78)
print("[SEC 1] Pre-registered parameters")
print("-" * 78)

# PASS/FAIL/INFO thresholds (pre-registered)
TOL_PASS = 0.30                          # (local) max rel_dev for PASS
TOL_INFO = 3.00                          # (local) max rel_dev for INFO

# PDG Yukawa at M_Z (central values)
Y_t_MZ = np.sqrt(2.0) * m_t_pole / v_ew  # (local) y_t = sqrt(2) m_t / v_EW
# Y_b(M_Z) and Y_tau(M_Z) from PDG running masses
m_b_MZ = 2.89                            # (local) GeV, MSbar bottom at M_Z (PDG)
m_tau_pole = 1.77686                     # (local) GeV, tau pole (PDG 2024)
Y_b_MZ = np.sqrt(2.0) * m_b_MZ / v_ew    # (local)
Y_tau_MZ = np.sqrt(2.0) * m_tau_pole / v_ew  # (local)

alpha_t_MZ = (Y_t_MZ**2) / (4.0 * PI)    # (local) alpha_t = y_t^2/(4 pi)
alpha_b_MZ = (Y_b_MZ**2) / (4.0 * PI)    # (local)
alpha_tau_MZ = (Y_tau_MZ**2) / (4.0 * PI)  # (local)

# MSS2012 / Arason 1992 2-loop top-Yukawa gauge-β coefficients
C_top = np.array([17.0/10.0, 3.0/2.0, 2.0])   # (local) [C_1^t, C_2^t, C_3^t]
# For bottom-Yukawa (down-type): same group-theory factors but for d-quark
# hypercharge — Arason 1992 Table I: C_b = (1/2, 3/2, 2)
C_bot = np.array([1.0/2.0, 3.0/2.0, 2.0])     # (local)
# For tau-Yukawa (charged lepton): C_tau = (3/2, 1/2, 0)
C_tau = np.array([3.0/2.0, 1.0/2.0, 0.0])     # (local)

# SM couplings at M_Z (PDG-derived, GUT-normalized α_1)
alpha_em_MZ = 1.0 / alpha_em_MZ_inv      # (local)
alpha2_MZ = alpha_em_MZ / sin2_thetaW_MSbar          # (local)
alpha_Y_MZ = alpha_em_MZ / (1.0 - sin2_thetaW_MSbar) # (local)
alpha1_MZ = (5.0/3.0) * alpha_Y_MZ        # (local) GUT-normalized
alpha3_MZ = alpha_s_MZ_obs                # (local)

x1_MZ = 1.0 / alpha1_MZ                   # (local)
x2_MZ = 1.0 / alpha2_MZ                   # (local)
x3_MZ = 1.0 / alpha3_MZ                   # (local)
r_MZ = x1_MZ / x2_MZ                      # (local) r = α_2/α_1

# Cubic BC at tau_fold
sin2_cubic_tau_fold = 3.0 / (3.0 + np.exp(12.0 * tau_fold))   # (local)

print(f"  PDG Yukawa at M_Z:")
print(f"    Y_t(M_Z)   = {Y_t_MZ:.6f}  (from y_t = sqrt(2) m_t / v_EW)")
print(f"    Y_b(M_Z)   = {Y_b_MZ:.6f}")
print(f"    Y_tau(M_Z) = {Y_tau_MZ:.6f}")
print(f"    Y_b/Y_t    = {Y_b_MZ/Y_t_MZ:.4e}  → (Y_b/Y_t)² = {(Y_b_MZ/Y_t_MZ)**2:.4e}")
print()
print(f"  α_t(M_Z) = y_t²/(4π) = {alpha_t_MZ:.6f}")
print(f"  α_b(M_Z)              = {alpha_b_MZ:.6e}")
print(f"  α_τ(M_Z)              = {alpha_tau_MZ:.6e}")
print()
print(f"  MSS2012 2-loop gauge-β coefficients:")
print(f"    C_top = {list(C_top)}  (17/10, 3/2, 2)")
print(f"    C_bot = {list(C_bot)}  (1/2, 3/2, 2)")
print(f"    C_tau = {list(C_tau)}  (3/2, 1/2, 0)")
print()
print(f"  SM inverse couplings at M_Z (GUT-norm):")
print(f"    x_1(M_Z) = 1/α_1 = {x1_MZ:.4f}")
print(f"    x_2(M_Z) = 1/α_2 = {x2_MZ:.4f}")
print(f"    x_3(M_Z) = 1/α_3 = {x3_MZ:.4f}")
print(f"    r = x_1/x_2      = {r_MZ:.6f}")
print()
print(f"  Cubic BC sin²(μ_BC) = 3/(3+e^12τ) = {sin2_cubic_tau_fold:.8f}")
print()
print(f"  PASS threshold: max rel_dev ≤ {TOL_PASS}")
print(f"  INFO threshold: max rel_dev ≤ {TOL_INFO}")

# =============================================================================
# SECTION 2: Linearized analytic estimator
# =============================================================================
print()
print("-" * 78)
print("[SEC 2] Analytic estimator (MSS2012 linearized 2-loop Yukawa shift)")
print("-" * 78)


def estimator_sin2_shift(mu_BC, x1, x2, alpha_t, alpha_b, alpha_tau,
                         C_t=C_top, C_b=C_bot, C_tau_=C_tau):
    """Analytic linearized 2-loop Yukawa threshold shift in sin²θ_W(M_Z).

    Δ(sin²)|_Yuk ≈ +15/(3+5r)² · (α_t + β_b α_b + β_τ α_τ) · L / (8π²·x_2)
                    · [(C_1 - r·C_2)]

    where β_b, β_τ account for the down-type and lepton-flavor kernels;
    sign chosen so that top-Yukawa dominant term is NEGATIVE (suppression).

    Derivation: Step 4 substitution chain above.
    """
    if mu_BC <= M_Z:
        return 0.0
    L = np.log(mu_BC / M_Z)                      # (local)
    r = x1 / x2                                  # (local)
    denom = (3.0 + 5.0 * r)**2                   # (local)
    pref = 15.0 / denom                          # (local)

    # Kernel for each Yukawa flavor: (C_i - r C_j) with i,j = (1,2) entries of C
    K_top = C_t[0] - r * C_t[1]                  # (local)
    K_bot = C_b[0] - r * C_b[1]                  # (local)
    K_tau = C_tau_[0] - r * C_tau_[1]            # (local)

    # Combined contribution (sign = +pref·K·α·L/(8π²·x_2), K<0 for top gives d sin²<0)
    contrib = (K_top * alpha_t + K_bot * alpha_b + K_tau * alpha_tau) * L / (8.0 * PI**2 * x2)
    return pref * contrib


# Evaluate Case A (sanity: reproduce prior-agent 4.46%)
mu_BC_A = 188.185                                # (local) Case A (S83 G47 reference)
delta_est_A = estimator_sin2_shift(mu_BC_A, x1_MZ, x2_MZ,
                                   alpha_t_MZ, alpha_b_MZ, alpha_tau_MZ)
print(f"  Case A: μ_BC = {mu_BC_A} GeV")
print(f"    ln(μ_BC/M_Z)                   = {np.log(mu_BC_A/M_Z):.6f}")
print(f"    (α/4π)²                        = {(alpha_em_MZ/(4*PI))**2:.6e}")
print(f"    Y_t²                           = {Y_t_MZ**2:.6f}")
print(f"    15/(3+5r)²                     = {15.0/(3+5*r_MZ)**2:.6f}")
print(f"    (C_1 - r·C_2) top              = {C_top[0] - r_MZ*C_top[1]:.6f}")
print(f"    Δ_estimator                    = {delta_est_A:.6e}")

# =============================================================================
# SECTION 3: Load G47 actual (Case A reference)
# =============================================================================
print()
print("-" * 78)
print("[SEC 3] Case A: compare to G47 actual (loaded from npz)")
print("-" * 78)

g47_npz = INPUT_FILES[2]                         # (local)
g47_data = np.load(g47_npz, allow_pickle=True)

# G47 yukawa_shift = sin2_mucrit_yuk - sin2_mucrit_gauge (at M_Z, from cubic BC at μ_BC)
actual_A = float(g47_data['yukawa_shift'])       # (local)
mu_BC_G47 = float(g47_data['mu_crit_yuk'])       # (local) actual μ_BC used in G47

# Re-evaluate estimator at G47's exact μ_BC for consistency
delta_est_A_exact = estimator_sin2_shift(mu_BC_G47, x1_MZ, x2_MZ,
                                         alpha_t_MZ, alpha_b_MZ, alpha_tau_MZ)
rel_dev_A = abs(delta_est_A_exact - actual_A) / abs(actual_A)  # (local)

print(f"  G47 μ_BC (μ_crit_yuk)   = {mu_BC_G47:.6f} GeV")
print(f"  G47 yukawa_shift        = {actual_A:.6e}")
print(f"  Estimator (at G47 μ_BC) = {delta_est_A_exact:.6e}")
print(f"  Rel dev (Case A)        = {rel_dev_A*100:.4f}%")

# =============================================================================
# SECTION 4: Full 2-loop numerical RGE for Cases B and C
# =============================================================================
print()
print("-" * 78)
print("[SEC 4] Full 2-loop numerical RGE for Cases B, C (actual reference)")
print("-" * 78)

# 2-loop SM gauge-β matrix (Machacek-Vaughn; GUT-normalized α_1)
B_2loop_gauge = np.array([                       # (local)
    [199.0/50.0, 27.0/10.0,  44.0/5.0],
    [9.0/10.0,   35.0/6.0,   12.0],
    [11.0/10.0,  9.0/2.0,   -26.0],
])


def rg_2loop_gauge(lnmu, y):
    """2-loop gauge-only SM RG (inverse couplings, d x_i / d ln μ)."""
    ia1, ia2, ia3 = y
    a1, a2, a3 = 1.0/ia1, 1.0/ia2, 1.0/ia3       # (local)
    alphas = np.array([a1, a2, a3])              # (local)
    da = [-b1_SM/(2.0*PI), -b2_SM/(2.0*PI), -b3_SM/(2.0*PI)]  # (local)
    for i in range(3):
        corr = sum(B_2loop_gauge[i, j] * alphas[j] for j in range(3))  # (local)
        da[i] -= corr / (8.0 * PI * PI)
    return da


def rg_2loop_plus_yukawa(lnmu, y):
    """2-loop SM RG with top-Yukawa threshold (MSS2012 / Arason 1992).
    d x_i/d ln μ = -b_i/(2π) - (1/(8π²))[Σ_j B_ij α_j - C_i^t α_t]
    """
    ia1, ia2, ia3 = y
    a1, a2, a3 = 1.0/ia1, 1.0/ia2, 1.0/ia3       # (local)
    alphas = np.array([a1, a2, a3])              # (local)
    da = [-b1_SM/(2.0*PI), -b2_SM/(2.0*PI), -b3_SM/(2.0*PI)]  # (local)
    for i in range(3):
        corr_gauge = sum(B_2loop_gauge[i, j] * alphas[j] for j in range(3))  # (local)
        corr_yuk = C_top[i] * alpha_t_MZ         # (local) top-dominant; const α_t
        da[i] -= corr_gauge / (8.0 * PI * PI)
        da[i] += corr_yuk / (8.0 * PI * PI)
    return da


def sin2_from_y(y):
    """sin²θ_W from y = [x_1, x_2, x_3]."""
    a1, a2 = 1.0/y[0], 1.0/y[1]                  # (local)
    return 3.0 * a1 / (3.0 * a1 + 5.0 * a2)


def sin2_MZ_from_cubic_BC(mu_BC, rhs_fn):
    """Impose sin²(μ_BC) = cubic at μ_BC, run DOWN to M_Z, return sin²(M_Z).
    Matches G47 `sin2_MZ_from_cubic_BC` exactly (same DOP853 ivp).
    """
    if mu_BC <= M_Z:
        return sin2_thetaW_MSbar
    lnmu_BC = np.log(mu_BC / M_Z)                # (local)
    y0 = [x1_MZ, x2_MZ, x3_MZ]                   # (local)
    # Step 1: integrate gauge-only UP from M_Z to μ_BC to get α_2, α_3 at μ_BC
    sol_up = solve_ivp(rg_2loop_gauge, (0.0, lnmu_BC), y0,
                       method='DOP853', rtol=1e-12, atol=1e-14, dense_output=False)
    if not sol_up.success:
        raise RuntimeError(f"UP integration failed at μ_BC={mu_BC}")
    y_BC = sol_up.y[:, -1].copy()
    # Step 2: override x_1(μ_BC) to impose cubic BC
    a2_BC = 1.0 / y_BC[1]                        # (local)
    a1_BC = 5.0 * a2_BC * sin2_cubic_tau_fold / (3.0 * (1 - sin2_cubic_tau_fold))  # (local)
    y_BC[0] = 1.0 / a1_BC
    # Step 3: run DOWN from μ_BC to M_Z under chosen RHS
    sol_down = solve_ivp(rhs_fn, (lnmu_BC, 0.0), y_BC,
                         method='DOP853', rtol=1e-12, atol=1e-14, dense_output=False)
    if not sol_down.success:
        raise RuntimeError(f"DOWN integration failed at μ_BC={mu_BC}")
    return sin2_from_y(sol_down.y[:, -1])


# Evaluate Cases B and C
mu_BC_B = 500.0                                  # (local)
mu_BC_C = 2000.0                                 # (local)

# Case B
sin2_B_gauge = sin2_MZ_from_cubic_BC(mu_BC_B, rg_2loop_gauge)  # (local)
sin2_B_yuk = sin2_MZ_from_cubic_BC(mu_BC_B, rg_2loop_plus_yukawa)  # (local)
actual_B = sin2_B_yuk - sin2_B_gauge             # (local)
delta_est_B = estimator_sin2_shift(mu_BC_B, x1_MZ, x2_MZ,
                                   alpha_t_MZ, alpha_b_MZ, alpha_tau_MZ)
rel_dev_B = abs(delta_est_B - actual_B) / abs(actual_B)  # (local)

# Case C
sin2_C_gauge = sin2_MZ_from_cubic_BC(mu_BC_C, rg_2loop_gauge)  # (local)
sin2_C_yuk = sin2_MZ_from_cubic_BC(mu_BC_C, rg_2loop_plus_yukawa)  # (local)
actual_C = sin2_C_yuk - sin2_C_gauge             # (local)
delta_est_C = estimator_sin2_shift(mu_BC_C, x1_MZ, x2_MZ,
                                   alpha_t_MZ, alpha_b_MZ, alpha_tau_MZ)
rel_dev_C = abs(delta_est_C - actual_C) / abs(actual_C)  # (local)

print(f"  Case B: μ_BC = {mu_BC_B} GeV")
print(f"    sin²_gauge(M_Z) = {sin2_B_gauge:.10f}")
print(f"    sin²_yuk(M_Z)   = {sin2_B_yuk:.10f}")
print(f"    actual shift    = {actual_B:.6e}")
print(f"    estimator       = {delta_est_B:.6e}")
print(f"    rel_dev         = {rel_dev_B*100:.4f}%")
print()
print(f"  Case C: μ_BC = {mu_BC_C} GeV")
print(f"    sin²_gauge(M_Z) = {sin2_C_gauge:.10f}")
print(f"    sin²_yuk(M_Z)   = {sin2_C_yuk:.10f}")
print(f"    actual shift    = {actual_C:.6e}")
print(f"    estimator       = {delta_est_C:.6e}")
print(f"    rel_dev         = {rel_dev_C*100:.4f}%")

# =============================================================================
# SECTION 5: Verdict
# =============================================================================
print()
print("-" * 78)
print("[SEC 5] Verdict")
print("-" * 78)

mu_BC_arr = np.array([mu_BC_G47, mu_BC_B, mu_BC_C])               # (local)
delta_est_arr = np.array([delta_est_A_exact, delta_est_B, delta_est_C])  # (local)
delta_actual_arr = np.array([actual_A, actual_B, actual_C])       # (local)
rel_dev_arr = np.array([rel_dev_A, rel_dev_B, rel_dev_C])         # (local)

max_rel_dev = float(np.max(rel_dev_arr))         # (local)

print(f"  3-case table:")
print(f"    {'μ_BC (GeV)':>12s}  {'actual':>14s}  {'estimator':>14s}  {'rel_dev':>10s}")
for mu, act, est, rel in zip(mu_BC_arr, delta_actual_arr, delta_est_arr, rel_dev_arr):
    print(f"    {mu:>12.4f}  {act:>14.6e}  {est:>14.6e}  {rel*100:>9.4f}%")
print()
print(f"  max rel_dev = {max_rel_dev*100:.4f}%")
print(f"  PASS threshold = {TOL_PASS*100:.1f}%")

if max_rel_dev <= TOL_PASS:
    verdict = "PASS"
    reason = f"max rel_dev = {max_rel_dev*100:.2f}% ≤ {TOL_PASS*100:.0f}% across 3 cases"
elif max_rel_dev <= TOL_INFO:
    verdict = "INFO"
    reason = f"max rel_dev = {max_rel_dev*100:.2f}% ∈ ({TOL_PASS*100:.0f}%, {TOL_INFO*100:.0f}%)"
else:
    verdict = "FAIL"
    reason = f"max rel_dev = {max_rel_dev*100:.2f}% > {TOL_INFO*100:.0f}% — replace with full numerical RGE"

print(f"  VERDICT: {verdict}")
print(f"  REASON : {reason}")

# =============================================================================
# SECTION 6: Closure SHA and 4-tuple
# =============================================================================
print()
print("-" * 78)
print("[SEC 6] Closure SHA and 4-tuple")
print("-" * 78)

# Ordered input-pin map (S81+ canonical form)
closure_inputs = {                               # (local)
    'gate_id': 'S84-YUKAWA-OOM-ESTIMATOR',
    'session': 'S84',
    'mu_BC_cases': [mu_BC_G47, mu_BC_B, mu_BC_C],
    'delta_actual': delta_actual_arr.tolist(),
    'delta_estimator': delta_est_arr.tolist(),
    'rel_dev': rel_dev_arr.tolist(),
    'max_rel_dev': max_rel_dev,
    'verdict': verdict,
    'scheme': '2-loop-Yukawa-estimator-MSS2012',
    'convention': 'PDG Yukawa at M_Z',
    'L_max': 'N/A',
    'input_shas': INPUT_SHAS,
}

closure_payload = json.dumps(closure_inputs, sort_keys=True).encode('utf-8')  # (local)
content_sha = hashlib.sha256(closure_payload).hexdigest()        # (local)

# audit SHA: hash of the script file itself + verdict string + max_rel_dev (6-digit)
audit_payload = (                                # (local)
    _sha256(__file__)
    + f"|verdict={verdict}"
    + f"|max_rel_dev={max_rel_dev:.6e}"
).encode('utf-8')
audit_sha = hashlib.sha256(audit_payload).hexdigest()            # (local)

four_tuple = (                                   # (local)
    f"(value={max_rel_dev:.6f}, "
    f"scheme=2-loop-Yukawa-estimator-MSS2012, "
    f"convention=PDG Yukawa at M_Z, L_max=N/A)"
)

print(f"  content_sha256 = {content_sha}")
print(f"  audit_sha256   = {audit_sha}")
print(f"  4-tuple        = {four_tuple}")

# =============================================================================
# SECTION 7: Save .npz
# =============================================================================
print()
print("-" * 78)
print("[SEC 7] Save outputs")
print("-" * 78)

out_npz = SCRIPT_DIR / "s84_w4_yukawa_oom_estimator.npz"   # (local)
np.savez(
    out_npz,
    mu_bc_GeV=mu_BC_arr,
    delta_estimator=delta_est_arr,
    delta_actual=delta_actual_arr,
    rel_dev=rel_dev_arr,
    max_rel_dev=max_rel_dev,
    verdict=np.array([verdict]),
    reason=np.array([reason]),
    closure_sha=np.array([content_sha]),
    audit_sha=np.array([audit_sha]),
    four_tuple=np.array([four_tuple]),
    input_shas=np.array([f"{k}={v}" for k, v in INPUT_SHAS.items()]),
    # Estimator ingredients (for reproduction)
    x1_MZ=x1_MZ, x2_MZ=x2_MZ, r_MZ=r_MZ,
    Y_t_MZ=Y_t_MZ, Y_b_MZ=Y_b_MZ, Y_tau_MZ=Y_tau_MZ,
    alpha_t_MZ=alpha_t_MZ, alpha_b_MZ=alpha_b_MZ, alpha_tau_MZ=alpha_tau_MZ,
    C_top=C_top, C_bot=C_bot, C_tau=C_tau,
    sin2_cubic_tau_fold=sin2_cubic_tau_fold,
)
print(f"  wrote {out_npz}")

# =============================================================================
# SECTION 8: Verdict line (append, S84+ DUAL-SHA canonical form)
# =============================================================================
print()
print("-" * 78)
print("[SEC 8] Append verdict line to s84_gate_verdicts.txt")
print("-" * 78)

verdict_line = (
    f"S84-YUKAWA-OOM-ESTIMATOR: {verdict} -- "
    f"value={max_rel_dev:.6f} "
    f"scheme=2-loop-Yukawa-estimator-MSS2012 "
    f"convention=PDG-Yukawa-at-MZ "
    f"L_max=N/A "
    f"audit_sha256={audit_sha} "
    f"content_sha256={content_sha}"
)
print(f"  line: {verdict_line}")

verdict_file = SCRIPT_DIR / "s84_gate_verdicts.txt"   # (local)
with open(verdict_file, 'a', encoding='utf-8') as fh:
    fh.write(verdict_line + "\n")
print(f"  appended to {verdict_file}")

elapsed = time.time() - t_start                  # (local)
print()
print("=" * 78)
print(f"DONE ({elapsed:.2f} s)")
print("=" * 78)
# 4-tuple output (printed as final non-verdict line per gate-verdicts.md §2):
print(four_tuple)
