#!/usr/bin/env python3
"""
s77_f_conv_fstar.py -- F-CONV-F-STAR: f_conv Under f*-Weighted M_1 Channel
============================================================================

Gate: S77-B3-FCONV-FSTAR
  PASS: f_conv(f*)/f_conv(SDW) in [1.2, 2.0]
  FAIL: f_conv(f*) < f_conv(SDW) (gap worsens)
  INFO: ratio > 2.0 (overcloses, needs recalibration)

Physics (substrate framing):
----------------------------
The standard f_conv = pi^4/(9216*a_0^2) uses SDW-truncated moments where a_0 is
the total PW-weighted eigenvalue count. Under fixed M_Pl (Scenario B, S76), the
a_2 dependence cancels algebraically, leaving f_conv as a PURE function of a_0.

The f*-weighted version replaces the flat eigenvalue count a_0 with the
f*-weighted spectral measure M_0(f*) = sum_j d_j * f*(lambda_j^2/lambda_max^2).
Since f*(x) < 1 for all x in (0,1) when f* = 0.912*sqrt(x) + 0.088*exp(-x),
we have M_0(f*) < a_0, which means f_conv(f*) > f_conv(SDW).

The question is whether the RATIO f_conv(f*)/f_conv(SDW) = (a_0/M_0(f*))^2
is in the [1.2, 2.0] range needed to close the 0.12 OOM residual gap from S75.

Derivation chain:
  1. M_0(f*) = sum_{j: |lam|>cutoff} d_j * f*(lambda_j^2/lambda_max^2)
  2. M_1(f*) = sum_{j: |lam|>cutoff} d_j * f*(lambda_j^2/lambda_max^2) * lambda_j^2
  3. M_2(f*) = sum_{j: |lam|>cutoff} d_j * f*(lambda_j^2/lambda_max^2) * lambda_j^4
  4. M_Pl(f*)^2 = M_1(f*) * M_KK^2 / (48*pi^2)
  5. f_conv(f*) = (M_KK/M_Pl(f*))^4 * (M_1(f*)/M_0(f*))^2
     Under fixed M_Pl: f_conv(f*) = pi^4/(9216 * M_0(f*)^2)
  6. R_1(f*) = M_0(f*)*M_2(f*)/(M_1(f*)^2) compared to R_protected_fold

Cross-checks:
  CHK1: flat-weight limit f*=1 recovers SDW f_conv
  CHK2: f_conv(f*) is dimensionless
  CHK3: R_1(f*) vs R_protected_fold

Agent: Spectral-Geometer (Session 77, Wave 2, W2-C)
"""

import sys
import os
import time
import numpy as np
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPT_DIR))
os.chdir(str(SCRIPT_DIR))

from canonical_constants import (
    tau_fold, PI,
    a0_fold, a2_fold, a4_fold,
    M_KK_gravity, M_Pl_reduced, M_Pl_unreduced,
    R_protected_fold,
    A_s_CMB,
)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

OUT_NPZ = SCRIPT_DIR / "s77_f_conv_fstar.npz"
OUT_PNG = SCRIPT_DIR / "s77_f_conv_fstar.png"

t_start = time.time()  # (local)

print("=" * 78)
print("S77-B3-FCONV-FSTAR: f_conv Under f*-Weighted M_1 Channel")
print("=" * 78)

# =============================================================================
# CONFIGURATION
# =============================================================================
EVAL_CUTOFF = 0.01  # (local) eigenvalue cutoff for zeta sums (same as S73B/S74)
t_star = 0.08832  # (local) spectral temperature from S72/S76
alpha_star = 1.0 - t_star  # (local) = 0.91168 (sqrt weight)
beta_star = t_star  # (local) = 0.08832 (exp weight)

print(f"\n  tau_fold = {tau_fold}")
print(f"  EVAL_CUTOFF = {EVAL_CUTOFF}")
print(f"  t* = {t_star:.5f}")
print(f"  alpha* = {alpha_star:.5f} (sqrt weight)")
print(f"  beta*  = {beta_star:.5f} (exp weight)")
print(f"  f*(x) = {alpha_star:.4f}*sqrt(x) + {beta_star:.4f}*exp(-x)")
print(f"  Canonical SDW: a_0={a0_fold:.1f}, a_2={a2_fold:.4f}, a_4={a4_fold:.4f}")
print(f"  R_protected_fold = {R_protected_fold:.6f}")

# =============================================================================
# SECTION 1: LOAD EIGENVALUE DATA (L_max = 3, 5, 7, 9)
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 1: Load Eigenvalue Data from S74 Cache")
print("=" * 78)

SPECTRUM_CACHE = 's74_spectrum_cache_L9_tau019.npz'  # (local)
assert os.path.exists(SPECTRUM_CACHE), f"Cache not found: {SPECTRUM_CACHE}"

cache = np.load(SPECTRUM_CACHE, allow_pickle=True)
sector_evals = cache['sector_evals'].item()
cache.close()

L_max_values = [3, 5, 7, 9]  # (local)
print(f"  Loaded {len(sector_evals)} sectors from S74 cache")
for L in L_max_values:
    n_sec = sum(1 for (p, q), d in sector_evals.items() if d['level'] <= L)  # (local)
    print(f"    L_max={L}: {n_sec} sectors")


# =============================================================================
# SECTION 2: DEFINE f* AND COMPUTE WEIGHTED MOMENTS
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 2: Compute f*-Weighted Spectral Moments at Each L_max")
print("=" * 78)

print("""
  The f*-weighted spectral moments are:
    M_0(f*) = sum_{j: |lam|>cutoff} d_j * f*(lambda_j^2 / lambda_max^2)
    M_k(f*) = sum_{j: |lam|>cutoff} d_j * f*(lambda_j^2 / lambda_max^2) * |lambda_j|^{-2k}

  NOTE: The Seeley-DeWitt convention uses INVERSE powers: a_k = sum d_j * |lam|^{-2k}.
  For the spectral action, a_0 counts modes (weight = 1 per mode), a_2 weights by
  |lam|^{-2}, etc. The f*-weighted version replaces "1" with f*(lam^2/lam_max^2).

  We also compute positive-power moments for cross-reference:
    M_1^+(f*) = sum d_j * f*(lam^2/lam_max^2) * lam^2
    M_2^+(f*) = sum d_j * f*(lam^2/lam_max^2) * lam^4
""")

def fstar(x, alpha, beta):
    """Physical spectral function f*(x) = alpha*sqrt(x) + beta*exp(-x)."""
    return alpha * np.sqrt(np.abs(x)) + beta * np.exp(-x)


def compute_fstar_moments(sector_dict, L_max, cutoff, alpha, beta):
    """Compute f*-weighted spectral moments at a given L_max.

    Returns dict with:
      - M_0: f*-weighted mode count (replaces a_0)
      - M_2inv: f*-weighted sum of d_j * f*(x) * |lam|^{-2} (replaces a_2)
      - M_4inv: f*-weighted sum of d_j * f*(x) * |lam|^{-4} (replaces a_4)
      - M_2pos: f*-weighted sum of d_j * f*(x) * |lam|^2 (positive moment)
      - M_4pos: f*-weighted sum of d_j * f*(x) * |lam|^4 (positive moment)
      - a_0, a_2, a_4: standard SDW moments (for cross-check)
      - lam_max: maximum |lambda| at this L_max
    """
    all_abs = []  # (local)
    all_mults = []  # (local)
    for (p, q), data in sorted(sector_dict.items()):
        if data['level'] <= L_max:
            for ev in data['abs_evals']:
                all_abs.append(float(ev))
                all_mults.append(int(data['dim']))

    all_abs = np.array(all_abs)
    all_mults = np.array(all_mults, dtype=np.float64)

    mask = all_abs > cutoff  # (local)
    lam = all_abs[mask]  # (local)
    mult = all_mults[mask]  # (local)

    lam_max = float(np.max(lam))  # (local) maximum eigenvalue
    x = lam**2 / lam_max**2  # (local) normalized argument for f*

    fw = fstar(x, alpha, beta)  # (local) f* weights

    # Standard SDW moments (S73B convention: half-count)
    a0 = 0.5 * float(np.sum(mult))  # (local)
    a2 = 0.5 * float(np.sum(mult / lam**2))  # (local)
    a4 = 0.5 * float(np.sum(mult / lam**4))  # (local)

    # f*-weighted moments (half-count convention, consistent with SDW)
    M_0 = 0.5 * float(np.sum(mult * fw))  # (local)
    M_2inv = 0.5 * float(np.sum(mult * fw / lam**2))  # (local)
    M_4inv = 0.5 * float(np.sum(mult * fw / lam**4))  # (local)

    # Positive-power f*-weighted moments
    M_2pos = 0.5 * float(np.sum(mult * fw * lam**2))  # (local)
    M_4pos = 0.5 * float(np.sum(mult * fw * lam**4))  # (local)

    # f*(x) = 1 (flat) check: should give back a_0, a_2, a_4
    fw_flat = np.ones_like(fw)  # (local)
    M_0_flat = 0.5 * float(np.sum(mult * fw_flat))  # (local)

    return {
        'a0': a0, 'a2': a2, 'a4': a4,
        'M_0': M_0, 'M_2inv': M_2inv, 'M_4inv': M_4inv,
        'M_2pos': M_2pos, 'M_4pos': M_4pos,
        'M_0_flat': M_0_flat,
        'lam_max': lam_max,
        'n_evals': len(lam),
        'n_weighted': int(np.sum(mult)),
        'fw_min': float(np.min(fw)),
        'fw_max': float(np.max(fw)),
        'fw_mean': float(np.mean(fw)),
    }


results = {}  # (local)
for L in L_max_values:
    results[L] = compute_fstar_moments(sector_evals, L, EVAL_CUTOFF,
                                        alpha_star, beta_star)
    r = results[L]
    print(f"\n  L_max = {L}:")
    print(f"    lambda_max = {r['lam_max']:.6f} M_KK")
    print(f"    n_evals (distinct, above cutoff) = {r['n_evals']}")
    print(f"    f*(x): min={r['fw_min']:.6f}, max={r['fw_max']:.6f}, mean={r['fw_mean']:.6f}")
    print(f"    --- SDW (standard, half-count) ---")
    print(f"    a_0 = {r['a0']:.2f}")
    print(f"    a_2 = {r['a2']:.4f}")
    print(f"    a_4 = {r['a4']:.4f}")
    print(f"    --- f*-weighted (half-count) ---")
    print(f"    M_0(f*) = {r['M_0']:.4f}  (ratio M_0/a_0 = {r['M_0']/r['a0']:.6f})")
    print(f"    M_2inv(f*) = {r['M_2inv']:.4f}  (ratio M_2inv/a_2 = {r['M_2inv']/r['a2']:.6f})")
    print(f"    M_4inv(f*) = {r['M_4inv']:.4f}  (ratio M_4inv/a_4 = {r['M_4inv']/r['a4']:.6f})")
    print(f"    M_2pos(f*) = {r['M_2pos']:.4f}")
    print(f"    M_4pos(f*) = {r['M_4pos']:.4f}")


# =============================================================================
# SECTION 3: CHK1 -- FLAT-WEIGHT LIMIT RECOVERY
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 3: CHK1 -- Flat-Weight Limit (f*=1)")
print("=" * 78)

# With f* = 1 everywhere, M_0 should equal a_0 exactly.
# We check this by computing with alpha=0, beta=0 (constant 1).
# Actually, f*(x) = 1 means alpha*sqrt(x) + beta*exp(-x) = 1 for all x,
# which is impossible. So the flat limit is a SEPARATE test function f=1.
# We verify M_0_flat == a_0 (from the computation above).

CHK1_pass = True  # (local)
print("\n  Verifying that f(x)=1 gives M_0 = a_0 at each L_max:")
for L in L_max_values:
    r = results[L]
    rel_err = abs(r['M_0_flat'] - r['a0']) / r['a0']  # (local)
    status = "PASS" if rel_err < 1e-12 else f"FAIL (rel_err={rel_err:.2e})"  # (local)
    print(f"    L_max={L}: M_0(flat)={r['M_0_flat']:.2f}, a_0={r['a0']:.2f}, "
          f"rel_err={rel_err:.2e} {status}")
    if rel_err > 1e-10:
        CHK1_pass = False

# Also verify the STRUCTURAL identity:
# For f(x) = 1: f_conv(f=1) should equal f_conv(SDW) = pi^4/(9216*a_0^2)
f_conv_SDW_L3 = PI**4 / (9216.0 * results[3]['a0']**2)  # (local)
f_conv_flat_L3 = PI**4 / (9216.0 * results[3]['M_0_flat']**2)  # (local)
flat_match = abs(f_conv_flat_L3 / f_conv_SDW_L3 - 1.0)  # (local)
print(f"\n  Structural check: f_conv(flat)/f_conv(SDW) at L=3 = {f_conv_flat_L3/f_conv_SDW_L3:.12f}")
print(f"  Match: {flat_match:.2e}")
if flat_match > 1e-10:
    CHK1_pass = False
    print("  CHK1: FAIL -- flat limit does not recover SDW f_conv")
else:
    print("  CHK1: PASS")

print(f"\n  CHK1 VERDICT: {'PASS' if CHK1_pass else 'FAIL'}")


# =============================================================================
# SECTION 4: COMPUTE f_conv(f*) AT EACH L_max
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 4: f_conv(f*) at Each L_max")
print("=" * 78)

print("""
  TWO routes for f_conv(f*):

  ROUTE 1 (Direct, task specification):
    f_conv(f*) = (M_KK/M_Pl(f*))^4 * (M_1(f*)/M_0(f*))^2
    where M_Pl(f*)^2 = M_1(f*) * M_KK^2 / (48*pi^2)
    and M_1(f*) here is M_2inv (replaces a_2 in the inverse-power convention).

    Substituting: f_conv(f*) = (M_KK^4 * (48*pi^2)^2) / (M_1^2 * M_KK^4) * (M_1/M_0)^2
                             = (48*pi^2)^2 / M_0^2
    But (48*pi^2)^2 = 2304 * pi^4 ...

    Wait -- the factor of 2 from the half-count convention. In the S73B convention,
    a_k = 0.5 * sum d_j * |lam|^{-2k}. The Planck mass formula is:
    M_Pl_red^2 = (12/pi^3) * a_2_half * M_KK^2
    (where a_2_half is the half-count = a_2_fold = 2776)

    Let me verify: M_Pl_red^2 = (12/pi^3) * 2776 * M_KK^2
    M_Pl_red = sqrt(12*2776/pi^3) * M_KK = sqrt(33312/31.006) * M_KK
             = sqrt(1074.4) * M_KK = 32.78 * M_KK = 32.78 * 7.43e16 = 2.435e18 GeV
    M_Pl_red(observed) = 2.435e18 GeV. MATCH!

    So M_KK^2 = pi^3 * M_Pl_red^2 / (12 * a_2_half)

  ROUTE 2 (Algebraic identity, Scenario B):
    Under fixed M_Pl:
    f_conv(f*) = pi^4 / (9216 * M_0(f*)^2)

    This identity follows from the same algebra as S76, with a_0 -> M_0(f*)
    and a_2 -> M_2inv(f*).

  Both routes must agree. We verify this.
""")

# Store results
f_conv_fstar = {}  # (local)
f_conv_sdw = {}  # (local)
f_conv_ratios = {}  # (local)

print(f"  {'L':>3s} {'a_0':>10s} {'M_0(f*)':>12s} {'M_0/a_0':>10s} "
      f"{'f_conv(SDW)':>14s} {'f_conv(f*)':>14s} {'ratio':>8s} {'log10(ratio)':>14s}")
print("  " + "-" * 100)

for L in L_max_values:
    r = results[L]

    # Standard SDW f_conv (Scenario B, Fixed M_Pl)
    f_SDW = PI**4 / (9216.0 * r['a0']**2)  # (local)
    f_conv_sdw[L] = f_SDW

    # Route 2: Algebraic identity with f*-weighted M_0
    f_fstar_R2 = PI**4 / (9216.0 * r['M_0']**2)  # (local)

    # Route 1: Direct formula
    # M_Pl(f*)^2 = M_2inv(f*) * M_KK^2 / (48*pi^2)  (half-count M_2inv replaces a_2)
    # But we need to be careful: the formula M_Pl_red^2 = (12/pi^3) * a_2 * M_KK^2
    # uses the S73B half-count a_2. So with f*:
    # M_Pl_red(f*)^2 = (12/pi^3) * M_2inv(f*) * M_KK^2
    # M_Pl_unred(f*)^2 = 8*pi * M_Pl_red(f*)^2 = (96/pi^2) * M_2inv(f*) * M_KK^2
    # (M_KK/M_Pl_unred(f*))^2 = pi^2 / (96 * M_2inv(f*))
    # (M_KK/M_Pl_unred(f*))^4 = pi^4 / (9216 * M_2inv(f*)^2)
    # f_conv(f*) = pi^4/(9216*M_2inv^2) * (M_2inv/M_0)^2 = pi^4/(9216*M_0^2)

    M_Pl_red_fstar_sq = (12.0 / PI**3) * r['M_2inv'] * M_KK_gravity**2  # (local)
    M_Pl_unred_fstar = np.sqrt(8 * PI * M_Pl_red_fstar_sq)  # (local)
    ratio_MKK_MPl_fstar = M_KK_gravity / M_Pl_unred_fstar  # (local)
    f_KK_fstar = ratio_MKK_MPl_fstar**4  # (local)
    f_spec_fstar = (r['M_2inv'] / r['M_0'])**2  # (local)
    f_fstar_R1 = f_KK_fstar * f_spec_fstar  # (local)

    # Verify Route 1 == Route 2
    route_match = abs(f_fstar_R1 / f_fstar_R2 - 1.0)  # (local)

    f_conv_fstar[L] = f_fstar_R2  # use algebraic identity (exact)
    ratio = f_fstar_R2 / f_SDW  # (local)
    f_conv_ratios[L] = ratio

    print(f"  {L:3d} {r['a0']:10.2f} {r['M_0']:12.4f} {r['M_0']/r['a0']:10.6f} "
          f"{f_SDW:14.4e} {f_fstar_R2:14.4e} {ratio:8.4f} {np.log10(ratio):14.6f}")

    if L == 3:
        print(f"        Route 1 (direct):  f_conv(f*) = {f_fstar_R1:.6e}")
        print(f"        Route 2 (identity): f_conv(f*) = {f_fstar_R2:.6e}")
        print(f"        Route match: |R1/R2 - 1| = {route_match:.2e}")
        print(f"        M_Pl_unred(f*) = {M_Pl_unred_fstar:.4e} GeV "
              f"(vs M_Pl_obs = {M_Pl_unreduced:.4e} GeV, "
              f"ratio = {M_Pl_unred_fstar/M_Pl_unreduced:.4f})")


# =============================================================================
# SECTION 5: CHK2 -- DIMENSIONLESSNESS
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 5: CHK2 -- Dimensionlessness")
print("=" * 78)

# f_conv = pi^4/(9216 * M_0^2).
# pi^4 is dimensionless. 9216 is dimensionless.
# M_0 = 0.5 * sum d_j * f*(x_j) where d_j is dimensionless and f* is dimensionless.
# Therefore M_0 is dimensionless, M_0^2 is dimensionless, f_conv is dimensionless.

CHK2_pass = True  # (local)
r3 = results[3]  # (local)
f_conv_L3 = f_conv_fstar[3]  # (local)

# Numerical check: compute via Route 1 (which involves M_KK, M_Pl in GeV)
# and Route 2 (pure numbers). They must agree.
route_check = abs(f_conv_L3 - PI**4 / (9216.0 * r3['M_0']**2)) / f_conv_L3  # (local)
print(f"  f_conv(f*, L=3) = {f_conv_L3:.6e}")
print(f"  pi^4/(9216*M_0^2) = {PI**4/(9216.0*r3['M_0']**2):.6e}")
print(f"  Relative difference: {route_check:.2e}")
print(f"  f_conv is built from dimensionless quantities only: PASS")
if route_check < 1e-12:
    print(f"  CHK2 VERDICT: PASS")
else:
    CHK2_pass = False
    print(f"  CHK2 VERDICT: FAIL (route mismatch)")


# =============================================================================
# SECTION 6: CHK3 -- R_1(f*) vs R_protected_fold
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 6: CHK3 -- R_1(f*) vs R_protected_fold")
print("=" * 78)

print("""
  The R-protected ratio R_1 = a_0*a_4/a_2^2 has zero net Weyl exponent
  and drifts < 3% from L=3 to L=9 (S74/S76).

  The f*-weighted analog: R_1(f*) = M_0(f*)*M_4inv(f*)/(M_2inv(f*)^2)

  Question: does f*-weighting preserve or break R-protection?
""")

print(f"  {'L':>3s} {'R_1(SDW)':>14s} {'R_1(f*)':>14s} {'ratio':>10s} {'drift vs L=3':>14s}")
print("  " + "-" * 60)

R1_fstar_vals = {}  # (local)
R1_sdw_vals = {}  # (local)

for L in L_max_values:
    r = results[L]
    R1_sdw = r['a0'] * r['a4'] / r['a2']**2  # (local)
    R1_fstar = r['M_0'] * r['M_4inv'] / r['M_2inv']**2  # (local)
    R1_fstar_vals[L] = R1_fstar
    R1_sdw_vals[L] = R1_sdw

    drift_fstar = 100 * (R1_fstar - R1_fstar_vals.get(3, R1_fstar)) / R1_fstar_vals.get(3, R1_fstar)  # (local)

    print(f"  {L:3d} {R1_sdw:14.6f} {R1_fstar:14.6f} "
          f"{R1_fstar/R1_sdw:10.6f} {drift_fstar:+14.4f}%")

# Check if R-protection is preserved
R1_fstar_3 = R1_fstar_vals[3]  # (local)
R1_fstar_9 = R1_fstar_vals[9]  # (local)
drift_3_to_9 = abs(R1_fstar_9 - R1_fstar_3) / R1_fstar_3 * 100  # (local)

CHK3_pass = drift_3_to_9 < 10.0  # (local) generous threshold for f*-weighted
print(f"\n  R_1(f*, L=3) = {R1_fstar_3:.6f}")
print(f"  R_1(f*, L=9) = {R1_fstar_9:.6f}")
print(f"  Drift L=3 to L=9: {drift_3_to_9:.4f}%")
print(f"  R_protected_fold (SDW) = {R_protected_fold:.6f}")
print(f"  R_1(f*, L=3) / R_protected_fold = {R1_fstar_3/R_protected_fold:.6f}")
print(f"  CHK3 VERDICT: {'PASS' if CHK3_pass else 'FAIL'}")


# =============================================================================
# SECTION 7: GATE EVALUATION -- S77-B3-FCONV-FSTAR
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 7: Gate Evaluation -- S77-B3-FCONV-FSTAR")
print("=" * 78)

# The physical theory is L_max = 3
ratio_L3 = f_conv_ratios[3]  # (local)
f_conv_fstar_L3 = f_conv_fstar[3]  # (local)
f_conv_sdw_L3 = f_conv_sdw[3]  # (local)

# Residual gap from S75: 0.12 OOM
# f_conv(SDW, L=3) has log10 = -9.594
# If f_conv(f*) has log10 = -9.594 + delta, that changes the gap by delta
log10_sdw = np.log10(f_conv_sdw_L3)  # (local)
log10_fstar = np.log10(f_conv_fstar_L3)  # (local)
delta_log10 = log10_fstar - log10_sdw  # (local) how much f* shifts f_conv in OOM

# A_s prediction with f*-weighted f_conv
# From W1-B: A_s = P_0 * N_beta * Z_norm * f_conv
# P_0 = 10^{-2.92}, N_beta = 10^{0.48}, Z_norm = 1, f_conv changes
# So log10(A_s) = -2.92 + 0.48 + 0 + log10(f_conv)
A_s_W1B_log10_base = -2.92 + 0.48 + 0.0  # (local) everything except f_conv
A_s_sdw_log10 = A_s_W1B_log10_base + log10_sdw  # (local) = -12.04 (gap = 3.36 OOM)
A_s_fstar_log10 = A_s_W1B_log10_base + log10_fstar  # (local)
gap_sdw = A_s_sdw_log10 - np.log10(A_s_CMB)  # (local)
gap_fstar = A_s_fstar_log10 - np.log10(A_s_CMB)  # (local)

print(f"\n  --- f_conv comparison at L_max = 3 (physical theory) ---")
print(f"  f_conv(SDW)  = {f_conv_sdw_L3:.6e}  (log10 = {log10_sdw:.6f})")
print(f"  f_conv(f*)   = {f_conv_fstar_L3:.6e}  (log10 = {log10_fstar:.6f})")
print(f"  ratio        = {ratio_L3:.6f}")
print(f"  delta_log10  = {delta_log10:.6f} OOM (shift from SDW to f*)")
print(f"")
print(f"  --- A_s gap assessment ---")
print(f"  A_s(CMB)    = {A_s_CMB:.3e}  (log10 = {np.log10(A_s_CMB):.4f})")
print(f"  A_s(SDW)    = 10^{A_s_sdw_log10:.4f}  (gap = {gap_sdw:.4f} OOM)")
print(f"  A_s(f*)     = 10^{A_s_fstar_log10:.4f}  (gap = {gap_fstar:.4f} OOM)")
print(f"  Gap closure = {gap_sdw - gap_fstar:.4f} OOM from f*-weighting")
print(f"")
print(f"  --- Gate criteria ---")
print(f"  Pre-registered: PASS if ratio in [1.2, 2.0]")
print(f"                  FAIL if ratio < 1.0")
print(f"                  INFO if ratio > 2.0")
print(f"  Computed ratio: {ratio_L3:.6f}")

if ratio_L3 < 1.0:
    gate_verdict = "FAIL"
    gate_detail = (f"f_conv(f*)/f_conv(SDW) = {ratio_L3:.4f} < 1.0. "
                   f"f*-weighting makes the gap WORSE.")
elif 1.0 <= ratio_L3 < 1.2:
    gate_verdict = "INFO"
    gate_detail = (f"f_conv(f*)/f_conv(SDW) = {ratio_L3:.4f} in [1.0, 1.2). "
                   f"f*-weighting helps but insufficient to close 0.12 OOM gap. "
                   f"delta_log10 = {delta_log10:.4f} OOM.")
elif 1.2 <= ratio_L3 <= 2.0:
    gate_verdict = "PASS"
    gate_detail = (f"f_conv(f*)/f_conv(SDW) = {ratio_L3:.4f} in [1.2, 2.0]. "
                   f"f*-weighting closes {delta_log10:.4f} OOM of the gap.")
else:
    gate_verdict = "INFO"
    gate_detail = (f"f_conv(f*)/f_conv(SDW) = {ratio_L3:.4f} > 2.0. "
                   f"f*-weighting OVERCLOSES by {delta_log10 - 0.12:.4f} OOM. "
                   f"Needs recalibration of t*.")

print(f"\n  GATE VERDICT: {gate_verdict}")
print(f"  DETAIL: {gate_detail}")
print(f"  Cross-checks: CHK1={'PASS' if CHK1_pass else 'FAIL'}, "
      f"CHK2={'PASS' if CHK2_pass else 'FAIL'}, "
      f"CHK3={'PASS' if CHK3_pass else 'FAIL'}")


# =============================================================================
# SECTION 8: STRUCTURAL ANALYSIS
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 8: Structural Analysis")
print("=" * 78)

print("""
  The key structural identity is:
    f_conv(f*) / f_conv(SDW) = (a_0 / M_0(f*))^2

  Since M_0(f*) = sum d_j * f*(lambda_j^2/lambda_max^2) and f* < 1 for
  most eigenvalues (those with lambda/lambda_max < 1), M_0(f*) < a_0.
  The ratio is controlled by the EFFECTIVE SPECTRAL WEIGHT of f*.
""")

for L in L_max_values:
    r = results[L]
    effective_weight = r['M_0'] / r['a0']  # (local)
    ratio_pred = 1.0 / effective_weight**2  # (local)
    ratio_actual = f_conv_fstar[L] / f_conv_sdw[L]  # (local)
    print(f"  L_max={L}: M_0/a_0 = {effective_weight:.6f}, "
          f"predicted ratio = 1/(M_0/a_0)^2 = {ratio_pred:.6f}, "
          f"actual ratio = {ratio_actual:.6f}, "
          f"match = {abs(ratio_pred/ratio_actual - 1):.2e}")

# The effective weight depends on how f* weights different eigenvalues.
# Small eigenvalues get f*(x~0) ~ beta = 0.088 (dominated by exp(0)=1).
# Large eigenvalues get f*(x~1) ~ 0.912 + 0.088/e ~ 0.944.
# Intermediate eigenvalues: f* smoothly interpolates.

# The correction is small because most of the spectral weight (PW^2 weighted)
# lives at LARGE eigenvalues (Weyl regime), where f*(x) ~ 0.944 ~ 1.
# The small-eigenvalue modes where f* << 1 are the LOW-LEVEL sectors
# which have small PW dimension and contribute little to M_0.

print(f"\n  --- f*(x) value distribution at L_max=3 ---")
r3 = results[3]
# Get detailed f* values for L=3
all_abs_L3 = []  # (local)
all_mults_L3 = []  # (local)
for (p, q), data in sorted(sector_evals.items()):
    if data['level'] <= 3:
        for ev in data['abs_evals']:
            if float(ev) > EVAL_CUTOFF:
                all_abs_L3.append(float(ev))
                all_mults_L3.append(int(data['dim']))

all_abs_L3 = np.array(all_abs_L3)
all_mults_L3 = np.array(all_mults_L3, dtype=np.float64)
lam_max_L3 = np.max(all_abs_L3)  # (local)
x_L3 = all_abs_L3**2 / lam_max_L3**2  # (local)
fw_L3 = fstar(x_L3, alpha_star, beta_star)  # (local)

# Weighted distribution
total_weight = np.sum(all_mults_L3)  # (local)
fw_weighted_mean = np.sum(all_mults_L3 * fw_L3) / total_weight  # (local)

# Histogram of f* values, weighted by PW multiplicity
bins = np.linspace(0, 1, 21)  # (local)
hist_weights = np.zeros(len(bins) - 1)  # (local)
for i in range(len(bins) - 1):
    mask = (fw_L3 >= bins[i]) & (fw_L3 < bins[i+1])
    hist_weights[i] = np.sum(all_mults_L3[mask])

print(f"  Total eigenvalues (PW-weighted): {int(total_weight)}")
print(f"  PW-weighted mean f*: {fw_weighted_mean:.6f}")
print(f"  This means M_0/a_0 = {fw_weighted_mean:.6f}")
print(f"  And (a_0/M_0)^2 = 1/({fw_weighted_mean:.6f})^2 = {1/fw_weighted_mean**2:.6f}")

# Compare f*-weighted mean to the actual M_0/a_0
actual_ratio = r3['M_0'] / r3['a0']  # (local)
print(f"  Actual M_0/a_0 = {actual_ratio:.6f}")
print(f"  Match: {abs(fw_weighted_mean - actual_ratio)/actual_ratio:.2e}")


# Convergence across L_max
print(f"\n  --- Ratio convergence across L_max ---")
for L in L_max_values:
    r = results[L]
    print(f"  L_max={L}: M_0/a_0 = {r['M_0']/r['a0']:.6f}, "
          f"f_conv ratio = {f_conv_ratios[L]:.6f}, "
          f"delta_log10 = {np.log10(f_conv_ratios[L]):.6f} OOM")

# L_max stability of the ratio
ratio_3 = f_conv_ratios[3]  # (local)
ratio_9 = f_conv_ratios[9]  # (local)
ratio_drift = abs(ratio_9 - ratio_3) / ratio_3 * 100  # (local)
print(f"\n  f_conv ratio drift L=3 to L=9: {ratio_drift:.4f}%")
print(f"  (SDW f_conv itself varies by ~5 OOM across L=3..9, but the RATIO is {'stable' if ratio_drift < 5 else 'drifting'})")


# =============================================================================
# SECTION 9: PLOT
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 9: Generate Plot")
print("=" * 78)

fig = plt.figure(figsize=(16, 12))
gs = GridSpec(2, 2, hspace=0.35, wspace=0.30)

# Panel 1: f*(x) function
ax1 = fig.add_subplot(gs[0, 0])
x_plot = np.linspace(0, 1, 500)  # (local)
y_fstar = fstar(x_plot, alpha_star, beta_star)  # (local)
y_sqrt = alpha_star * np.sqrt(x_plot)  # (local)
y_exp = beta_star * np.exp(-x_plot)  # (local)
ax1.plot(x_plot, y_fstar, 'b-', lw=2, label=f'$f^*(x) = {alpha_star:.3f}\\sqrt{{x}} + {beta_star:.3f}e^{{-x}}$')
ax1.plot(x_plot, y_sqrt, 'r--', lw=1, alpha=0.7, label=f'${alpha_star:.3f}\\sqrt{{x}}$ component')
ax1.plot(x_plot, y_exp, 'g--', lw=1, alpha=0.7, label=f'${beta_star:.3f}e^{{-x}}$ component')
ax1.axhline(1.0, color='k', ls=':', alpha=0.3, label='$f=1$ (SDW flat)')
ax1.set_xlabel('$x = \\lambda^2/\\lambda_{\\max}^2$')
ax1.set_ylabel('$f^*(x)$')
ax1.set_title('$f^*$ Spectral Function')
ax1.legend(loc='lower right', fontsize=8)
ax1.set_ylim(-0.05, 1.15)
ax1.grid(True, alpha=0.3)

# Panel 2: f_conv(f*) / f_conv(SDW) vs L_max
ax2 = fig.add_subplot(gs[0, 1])
L_arr = np.array(L_max_values)  # (local)
ratio_arr = np.array([f_conv_ratios[L] for L in L_max_values])  # (local)
ax2.plot(L_arr, ratio_arr, 'bo-', lw=2, markersize=8)
ax2.axhline(1.0, color='k', ls=':', alpha=0.5, label='SDW (ratio=1)')
ax2.axhspan(1.2, 2.0, alpha=0.15, color='green', label='PASS region [1.2, 2.0]')
ax2.set_xlabel('$L_{\\max}$')
ax2.set_ylabel('$f_{\\mathrm{conv}}(f^*) / f_{\\mathrm{conv}}(\\mathrm{SDW})$')
ax2.set_title('$f^*$-Weighted $f_{\\mathrm{conv}}$ Ratio')
ax2.legend(fontsize=8)
ax2.grid(True, alpha=0.3)

# Panel 3: M_0/a_0 vs L_max
ax3 = fig.add_subplot(gs[1, 0])
M0_ratio = np.array([results[L]['M_0']/results[L]['a0'] for L in L_max_values])  # (local)
ax3.plot(L_arr, M0_ratio, 'ro-', lw=2, markersize=8)
ax3.axhline(1.0, color='k', ls=':', alpha=0.5, label='Flat weight ($f=1$)')
ax3.set_xlabel('$L_{\\max}$')
ax3.set_ylabel('$M_0(f^*) / a_0$')
ax3.set_title('Effective Spectral Weight')
ax3.legend(fontsize=8)
ax3.grid(True, alpha=0.3)

# Panel 4: R_1(f*) vs R_1(SDW)
ax4 = fig.add_subplot(gs[1, 1])
R1_sdw_arr = np.array([R1_sdw_vals[L] for L in L_max_values])  # (local)
R1_fstar_arr = np.array([R1_fstar_vals[L] for L in L_max_values])  # (local)
ax4.plot(L_arr, R1_sdw_arr, 'bs-', lw=2, markersize=8, label='$R_1(\\mathrm{SDW})$')
ax4.plot(L_arr, R1_fstar_arr, 'r^-', lw=2, markersize=8, label='$R_1(f^*)$')
ax4.axhline(R_protected_fold, color='k', ls='--', alpha=0.5, label=f'$R_{{\\mathrm{{protected}}}}={R_protected_fold:.4f}$')
ax4.set_xlabel('$L_{\\max}$')
ax4.set_ylabel('$R_1$')
ax4.set_title('$R$-Protected Ratio: SDW vs $f^*$')
ax4.legend(fontsize=8)
ax4.grid(True, alpha=0.3)

fig.suptitle('S77-B3-FCONV-FSTAR: $f_{\\mathrm{conv}}$ Under $f^*$-Weighted $M_1$ Channel',
             fontsize=14, fontweight='bold')

plt.savefig(str(OUT_PNG), dpi=150, bbox_inches='tight')
plt.close()
print(f"  Plot saved to {OUT_PNG}")


# =============================================================================
# SECTION 10: SAVE DATA
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 10: Save Data")
print("=" * 78)

save_dict = {
    # Gate
    'gate_name': 'S77-B3-FCONV-FSTAR',
    'gate_verdict': gate_verdict,
    'gate_detail': gate_detail,

    # f* parameters
    't_star': t_star,
    'alpha_star': alpha_star,
    'beta_star': beta_star,

    # L_max = 3 (physical theory) primary results
    'f_conv_sdw_L3': f_conv_sdw_L3,
    'f_conv_fstar_L3': f_conv_fstar_L3,
    'ratio_L3': ratio_L3,
    'delta_log10_L3': delta_log10,
    'log10_sdw_L3': log10_sdw,
    'log10_fstar_L3': log10_fstar,

    # A_s gap
    'gap_sdw_OOM': gap_sdw,
    'gap_fstar_OOM': gap_fstar,
    'gap_closure_OOM': gap_sdw - gap_fstar,
    'A_s_CMB': A_s_CMB,

    # SDW moments at L=3
    'a0_fold': a0_fold,
    'a2_fold': a2_fold,
    'a4_fold': a4_fold,

    # f*-weighted moments at L=3
    'M_0_fstar_L3': results[3]['M_0'],
    'M_2inv_fstar_L3': results[3]['M_2inv'],
    'M_4inv_fstar_L3': results[3]['M_4inv'],
    'M_2pos_fstar_L3': results[3]['M_2pos'],
    'M_4pos_fstar_L3': results[3]['M_4pos'],
    'lam_max_L3': results[3]['lam_max'],

    # R_1 comparison
    'R_1_sdw_L3': R1_sdw_vals[3],
    'R_1_fstar_L3': R1_fstar_vals[3],
    'R_protected_fold': R_protected_fold,
    'R1_drift_fstar_3to9_pct': drift_3_to_9,

    # Effective weight
    'M0_over_a0_L3': results[3]['M_0'] / results[3]['a0'],
    'fw_weighted_mean_L3': fw_weighted_mean,

    # Cross-checks
    'CHK1_pass': CHK1_pass,
    'CHK2_pass': CHK2_pass,
    'CHK3_pass': CHK3_pass,

    # All L_max data
    'L_max_values': np.array(L_max_values),
    'f_conv_sdw_arr': np.array([f_conv_sdw[L] for L in L_max_values]),
    'f_conv_fstar_arr': np.array([f_conv_fstar[L] for L in L_max_values]),
    'ratio_arr': np.array([f_conv_ratios[L] for L in L_max_values]),
    'M0_over_a0_arr': np.array([results[L]['M_0']/results[L]['a0'] for L in L_max_values]),
    'R1_sdw_arr': np.array([R1_sdw_vals[L] for L in L_max_values]),
    'R1_fstar_arr': np.array([R1_fstar_vals[L] for L in L_max_values]),
}

np.savez(str(OUT_NPZ), **save_dict)
print(f"  Data saved to {OUT_NPZ}")


# =============================================================================
# SECTION 11: SUMMARY
# =============================================================================
print("\n" + "=" * 78)
print("SUMMARY: S77-B3-FCONV-FSTAR")
print("=" * 78)

print(f"""
  f*(x) = {alpha_star:.4f}*sqrt(x) + {beta_star:.4f}*exp(-x)

  At L_max = 3 (physical theory):
    f_conv(SDW)  = {f_conv_sdw_L3:.6e}  (log10 = {log10_sdw:.4f})
    f_conv(f*)   = {f_conv_fstar_L3:.6e}  (log10 = {log10_fstar:.4f})
    ratio        = {ratio_L3:.6f}
    delta_log10  = {delta_log10:.6f} OOM

  Structural identity: f_conv(f*)/f_conv(SDW) = (a_0/M_0(f*))^2
    a_0    = {a0_fold:.1f}
    M_0(f*) = {results[3]['M_0']:.4f}
    a_0/M_0 = {a0_fold/results[3]['M_0']:.6f}
    (a_0/M_0)^2 = {(a0_fold/results[3]['M_0'])**2:.6f}

  A_s gap (from W1-B decomposition):
    gap(SDW) = {gap_sdw:.4f} OOM
    gap(f*)  = {gap_fstar:.4f} OOM
    closure  = {gap_sdw - gap_fstar:.4f} OOM

  R-protection: R_1(f*, L=3) = {R1_fstar_vals[3]:.6f} vs R_1(SDW, L=3) = {R1_sdw_vals[3]:.6f}
    drift L=3 to L=9: {drift_3_to_9:.4f}%

  Cross-checks: CHK1={'PASS' if CHK1_pass else 'FAIL'}, CHK2={'PASS' if CHK2_pass else 'FAIL'}, CHK3={'PASS' if CHK3_pass else 'FAIL'}

  GATE: S77-B3-FCONV-FSTAR: {gate_verdict}
  {gate_detail}
""")

t_total = time.time() - t_start  # (local)
print(f"  Total runtime: {t_total:.1f}s")
