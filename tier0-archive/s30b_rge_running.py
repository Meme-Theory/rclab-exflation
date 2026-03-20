#!/usr/bin/env python3
"""
s30b_rge_running.py — RGE Running + NCG-KK Tension Analysis
============================================================

Session 30Bb Step 4: Take g1/g2 from the grid data at the SM Weinberg contour
(where sin^2_B ~ 0.231 under Formula B) and run SM one-loop beta functions.

RGE-A (zero parameters): Starting from g1/g2 at M_KK, does the ratio run to
  sin^2(theta_W) = 0.2312 at M_Z for SOME M_KK in [10^10, 10^18] GeV?

RGE-B (one parameter): If Part A passes, do individual g1(M_Z), g2(M_Z)
  match PDG values? PDG: alpha_1(M_Z) = 0.01699, alpha_2(M_Z) = 0.03376.

NCG-KK tension (XS-2): Run UPWARD from M_KK. Find Lambda_SA where
  alpha_1 = alpha_2. Report Lambda_SA / M_KK.

Beta function coefficients (SM one-loop):
  b1 = 41/10, b2 = -19/6, b3 = -7

RGE formula:
  1/alpha_i(mu) = 1/alpha_i(M) + b_i/(2*pi) * ln(M/mu)

At KK scale:
  g1/g2 = sqrt(L2/L1)  =>  alpha_1/alpha_2 = L2/L1 = (g1/g2)^2

Formula B (correct, Baptista Paper 14 eq 2.93):
  sin^2(theta_W) = 3*L2 / (L1 + 3*L2)

Author: einstein-theorist agent, Session 30Bb
Date: 2026-03-01
"""

import numpy as np
import os
import sys
import time

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = Path(SCRIPT_DIR)

# ─── Physical Constants ──────────────────────────────────────────────────────
M_Z = 91.1876  # GeV (PDG 2024)
ALPHA_1_MZ = 0.01699  # PDG: alpha_1(M_Z) = 5/3 * alpha_em / cos^2(theta_W)
ALPHA_2_MZ = 0.03376  # PDG: alpha_2(M_Z)
SIN2_TW_PDG = 0.23122  # PDG: sin^2(theta_W)(M_Z) MSbar

# SM one-loop beta coefficients
B1 = 41.0 / 10.0   # = 4.1
B2 = -19.0 / 6.0   # = -3.1667
B3 = -7.0

# ─── Output ──────────────────────────────────────────────────────────────────
OUT_NPZ = DATA_DIR / 's30b_rge_running.npz'
OUT_PNG = DATA_DIR / 's30b_rge_running.png'


# =============================================================================
# MODULE 1: Load grid data and recompute Formula B
# =============================================================================

def load_grid_data():
    """Load 30Ba grid data and recompute Weinberg angle under Formula B."""
    npz = np.load(DATA_DIR / 's30b_grid_bcs.npz')

    tau = npz['tau']
    eps = npz['eps']
    g1g2 = npz['g1g2']       # sqrt(L2/L1) at each grid point
    sin2_A = npz['sin2_tw']  # Formula A: L2/(L1+L2) -- WRONG

    # Recover L2/L1 from g1g2
    ratio_L2_L1 = g1g2**2   # L2/L1

    # Recompute under Formula B: sin^2 = 3*L2/(L1 + 3*L2) = 3*r/(1 + 3*r)
    # where r = L2/L1
    sin2_B = 3.0 * ratio_L2_L1 / (1.0 + 3.0 * ratio_L2_L1)

    # Also need absolute L1, L2 from parameterization
    # From s30b_grid_bcs.py:
    #   L1 = exp(2*tau - 11*eps/N_T2)
    #   L2 = exp(-2*tau - 7*eps/N_T2)
    # where N_T2 = sqrt(234)
    N_T2 = np.sqrt(234.0)
    TAU, EPS = np.meshgrid(tau, eps, indexing='ij')
    L1_grid = np.exp(2.0 * TAU - 11.0 * EPS / N_T2)
    L2_grid = np.exp(-2.0 * TAU - 7.0 * EPS / N_T2)

    # V_total for reference
    V_total = npz['V_total_1p20']

    print(f"Grid loaded: {len(tau)} x {len(eps)} = {len(tau)*len(eps)} points")
    print(f"sin^2_B range: [{sin2_B.min():.4f}, {sin2_B.max():.4f}]")
    print(f"g1/g2 range: [{g1g2.min():.4f}, {g1g2.max():.4f}]")

    return {
        'tau': tau, 'eps': eps,
        'g1g2': g1g2, 'sin2_B': sin2_B, 'sin2_A': sin2_A,
        'L1': L1_grid, 'L2': L2_grid,
        'V_total': V_total,
        'ratio_L2_L1': ratio_L2_L1,
    }


# =============================================================================
# MODULE 2: SM one-loop RGE
# =============================================================================

def rge_run_down(alpha_1_KK, alpha_2_KK, M_KK, mu_low=M_Z):
    """
    Run SM one-loop RGE from M_KK down to mu_low.

    1/alpha_i(mu) = 1/alpha_i(M_KK) + b_i/(2*pi) * ln(M_KK/mu)

    Parameters
    ----------
    alpha_1_KK, alpha_2_KK : float
        Gauge couplings at KK scale.
    M_KK : float (GeV)
        Compactification scale.
    mu_low : float (GeV)
        Low-energy scale (default M_Z).

    Returns
    -------
    alpha_1_low, alpha_2_low : float
        Couplings at mu_low.
    sin2_tw_low : float
        sin^2(theta_W) at mu_low = alpha_1/(alpha_1 + alpha_2).
    """
    ln_ratio = np.log(M_KK / mu_low)

    inv_a1_low = 1.0 / alpha_1_KK + B1 / (2.0 * np.pi) * ln_ratio
    inv_a2_low = 1.0 / alpha_2_KK + B2 / (2.0 * np.pi) * ln_ratio

    # Check for Landau poles (negative inverse coupling)
    if np.any(inv_a1_low <= 0) or np.any(inv_a2_low <= 0):
        return np.nan, np.nan, np.nan

    alpha_1_low = 1.0 / inv_a1_low
    alpha_2_low = 1.0 / inv_a2_low

    # Physical Weinberg angle: sin^2 = alpha_Y / (alpha_Y + alpha_2)
    # where alpha_Y = (3/5) * alpha_1_GUT
    alpha_Y_low = (3.0 / 5.0) * alpha_1_low
    sin2_tw_low = alpha_Y_low / (alpha_Y_low + alpha_2_low)

    return alpha_1_low, alpha_2_low, sin2_tw_low


def rge_run_up(alpha_1_KK, alpha_2_KK, M_KK, mu_high):
    """
    Run SM one-loop RGE from M_KK upward to mu_high.

    1/alpha_i(mu_high) = 1/alpha_i(M_KK) - b_i/(2*pi) * ln(mu_high/M_KK)

    Returns alpha_1, alpha_2 at mu_high.
    """
    ln_ratio = np.log(mu_high / M_KK)

    inv_a1_high = 1.0 / alpha_1_KK - B1 / (2.0 * np.pi) * ln_ratio
    inv_a2_high = 1.0 / alpha_2_KK - B2 / (2.0 * np.pi) * ln_ratio

    if inv_a1_high <= 0 or inv_a2_high <= 0:
        return np.nan, np.nan

    return 1.0 / inv_a1_high, 1.0 / inv_a2_high


def find_unification_scale(alpha_1_KK, alpha_2_KK, M_KK):
    """
    Find Lambda_SA where alpha_1 = alpha_2 above M_KK.

    From 1/alpha_1 - b1/(2pi)*t = 1/alpha_2 - b2/(2pi)*t
    => (1/alpha_1 - 1/alpha_2) = (b1 - b2)/(2pi) * t
    => t = 2pi * (1/alpha_1 - 1/alpha_2) / (b1 - b2)
    where t = ln(Lambda_SA / M_KK)

    Returns Lambda_SA and Lambda_SA/M_KK.
    """
    delta_inv_alpha = 1.0 / alpha_1_KK - 1.0 / alpha_2_KK
    delta_b = B1 - B2  # 4.1 - (-3.1667) = 7.2667

    t = 2.0 * np.pi * delta_inv_alpha / delta_b

    Lambda_SA = M_KK * np.exp(t)
    ratio = Lambda_SA / M_KK

    return Lambda_SA, ratio, t


# =============================================================================
# MODULE 3: RGE-A scan over M_KK
# =============================================================================

def rge_a_scan(g1g2_KK, M_KK_range):
    """
    RGE-A: For a given g1/g2 (= sqrt(L2/L1)) at the KK scale, scan M_KK
    to find where sin^2(theta_W)(M_Z) = 0.2312.

    NORMALIZATION (critical):
    The code stores g1g2 = sqrt(L2/L1), the bare metric ratio.
    Formula B: sin^2 = 3*L2/(L1 + 3*L2). This implies:
      g_Y^2 / g_2^2 = 3 * L2/L1 = 3 * g1g2^2
    where g_Y is the SM hypercharge coupling (no GUT normalization).

    The SM RGE beta coefficients b_1 = 41/10 use GUT-normalized g_1:
      g_1 = sqrt(5/3) * g_Y
      alpha_1_GUT = (5/3) * alpha_Y
      alpha_1_GUT / alpha_2 = (5/3) * (g_Y/g_2)^2 = (5/3) * 3 * g1g2^2
                             = 5 * g1g2^2 = 5 * L2/L1

    Physical sin^2(theta_W) = alpha_Y / (alpha_Y + alpha_2)
                             = (3/5)*alpha_1_GUT / ((3/5)*alpha_1_GUT + alpha_2)

    Method: Fix alpha_2(M_KK) by running PDG alpha_2(M_Z) upward.
            Set alpha_1_GUT(M_KK) = 5 * g1g2^2 * alpha_2(M_KK).
            Run both down via SM one-loop RGE.
            Compute sin^2 = (3/5)*alpha_1 / ((3/5)*alpha_1 + alpha_2) at M_Z.
    """
    # GUT-normalized coupling ratio at KK scale
    r_KK = 5.0 * g1g2_KK**2  # alpha_1_GUT / alpha_2 at M_KK

    sin2_at_MZ = np.zeros_like(M_KK_range)
    alpha1_at_MZ = np.zeros_like(M_KK_range)
    alpha2_at_MZ = np.zeros_like(M_KK_range)

    for k, M_KK in enumerate(M_KK_range):
        # Step 1: Determine alpha_2 at M_KK by running PDG alpha_2(M_Z) upward
        ln_up = np.log(M_KK / M_Z)
        inv_a2_KK = 1.0 / ALPHA_2_MZ - B2 / (2.0 * np.pi) * ln_up
        if inv_a2_KK <= 0:
            sin2_at_MZ[k] = np.nan
            continue
        alpha_2_KK = 1.0 / inv_a2_KK

        # Step 2: alpha_1 at M_KK from ratio
        alpha_1_KK = r_KK * alpha_2_KK

        # Step 3: Run BOTH down to M_Z
        a1_low, a2_low, sin2_low = rge_run_down(alpha_1_KK, alpha_2_KK, M_KK)
        sin2_at_MZ[k] = sin2_low
        alpha1_at_MZ[k] = a1_low
        alpha2_at_MZ[k] = a2_low

    return sin2_at_MZ, alpha1_at_MZ, alpha2_at_MZ


# =============================================================================
# MODULE 4: Main analysis
# =============================================================================

def main():
    t0 = time.time()
    print("=" * 70)
    print("Session 30Bb Step 4: RGE Running + NCG-KK Tension")
    print("=" * 70)

    # ─── Load grid data ──────────────────────────────────────────────────
    data = load_grid_data()
    sin2_B = data['sin2_B']
    g1g2 = data['g1g2']
    tau = data['tau']
    eps = data['eps']
    V_total = data['V_total']
    L1 = data['L1']
    L2 = data['L2']

    # ─── Identify SM Weinberg contour under Formula B ────────────────────
    # Find grid points closest to sin^2_B = 0.231
    target = SIN2_TW_PDG
    tol = 0.010  # points within 0.01 of target

    mask = np.abs(sin2_B - target) < tol
    n_contour = np.sum(mask)
    print(f"\nFormula B Weinberg contour (|sin^2_B - 0.231| < {tol}):")
    print(f"  {n_contour} grid points on contour")

    if n_contour == 0:
        print("  ERROR: No grid points near SM Weinberg angle under Formula B!")
        return

    # Extract contour points
    TAU_grid, EPS_grid = np.meshgrid(tau, eps, indexing='ij')
    contour_tau = TAU_grid[mask]
    contour_eps = EPS_grid[mask]
    contour_g1g2 = g1g2[mask]
    contour_sin2B = sin2_B[mask]
    contour_V = V_total[mask]
    contour_L1 = L1[mask]
    contour_L2 = L2[mask]

    # Sort by V_total (ascending) to find lowest-energy contour point
    sort_idx = np.argsort(contour_V)
    print(f"\n  Contour points sorted by V_total:")
    print(f"  {'tau':>6s} {'eps':>7s} {'sin2_B':>8s} {'g1/g2':>7s} {'V_total':>12s} {'L1':>8s} {'L2':>8s}")
    for k in range(min(10, len(sort_idx))):
        idx = sort_idx[k]
        print(f"  {contour_tau[idx]:6.3f} {contour_eps[idx]:7.4f} "
              f"{contour_sin2B[idx]:8.5f} {contour_g1g2[idx]:7.4f} "
              f"{contour_V[idx]:12.4f} {contour_L1[idx]:8.4f} {contour_L2[idx]:8.4f}")

    # Best candidate: lowest V_total on Weinberg contour
    best_idx = sort_idx[0]
    tau_best = contour_tau[best_idx]
    eps_best = contour_eps[best_idx]
    g1g2_best = contour_g1g2[best_idx]
    sin2B_best = contour_sin2B[best_idx]
    V_best = contour_V[best_idx]
    L1_best = contour_L1[best_idx]
    L2_best = contour_L2[best_idx]

    print(f"\n  BEST contour point (lowest V_total on Weinberg contour):")
    print(f"    tau = {tau_best:.4f}")
    print(f"    eps = {eps_best:.4f}")
    print(f"    sin^2_B = {sin2B_best:.5f}")
    print(f"    g1/g2 = {g1g2_best:.6f}")
    print(f"    V_total = {V_best:.4f}")
    print(f"    L1 = {L1_best:.6f}, L2 = {L2_best:.6f}")
    print(f"    L2/L1 = {(L2_best/L1_best):.6f}")

    # ─── RGE-A: Scan M_KK ───────────────────────────────────────────────
    print(f"\n{'=' * 70}")
    print("RGE-A: Zero-parameter ratio test")
    print(f"{'=' * 70}")
    print(f"  Input: g1g2_code = sqrt(L2/L1) = {g1g2_best:.6f} at KK scale")
    print(f"  L2/L1 = {g1g2_best**2:.6f}")
    print(f"  alpha_1_GUT/alpha_2 = 5 * L2/L1 = {5.0*g1g2_best**2:.6f}  (GUT-normalized)")
    print(f"  alpha_Y/alpha_2 = 3 * L2/L1 = {3.0*g1g2_best**2:.6f}  (SM hypercharge)")
    print(f"  sin^2(theta_W)_KK = 3r/(1+3r) = {3*g1g2_best**2/(1+3*g1g2_best**2):.6f}  (Formula B)")
    print(f"  Target: sin^2(theta_W)(M_Z) = {SIN2_TW_PDG}")

    # Scan M_KK from 10^4 to 10^19 GeV (broader range for exploration)
    log_M_range = np.linspace(4, 19, 3001)
    M_KK_range = 10.0**log_M_range

    sin2_scan, a1_scan, a2_scan = rge_a_scan(g1g2_best, M_KK_range)

    # Find where sin^2(M_Z) crosses 0.2312
    valid = ~np.isnan(sin2_scan)
    print(f"\n  sin^2(theta_W)(M_Z) range over M_KK scan:")
    print(f"    M_KK range: [10^{log_M_range[valid][0]:.1f}, 10^{log_M_range[valid][-1]:.1f}] GeV")
    print(f"    sin^2 range: [{sin2_scan[valid].min():.6f}, {sin2_scan[valid].max():.6f}]")

    # Check if target is in range
    sin2_min = sin2_scan[valid].min()
    sin2_max = sin2_scan[valid].max()
    target_in_range = sin2_min <= SIN2_TW_PDG <= sin2_max

    print(f"\n  SM target {SIN2_TW_PDG} in range: {target_in_range}")

    M_KK_match = None
    if target_in_range:
        # Find crossing by linear interpolation
        for k in range(len(sin2_scan) - 1):
            if np.isnan(sin2_scan[k]) or np.isnan(sin2_scan[k+1]):
                continue
            if (sin2_scan[k] - SIN2_TW_PDG) * (sin2_scan[k+1] - SIN2_TW_PDG) < 0:
                # Linear interpolation
                frac = (SIN2_TW_PDG - sin2_scan[k]) / (sin2_scan[k+1] - sin2_scan[k])
                log_M_match = log_M_range[k] + frac * (log_M_range[k+1] - log_M_range[k])
                M_KK_match = 10.0**log_M_match
                print(f"\n  CROSSING FOUND:")
                print(f"    M_KK = 10^{log_M_match:.4f} GeV = {M_KK_match:.3e} GeV")

                # Verify: run at this M_KK
                _, _, sin2_check = rge_a_scan(g1g2_best, np.array([M_KK_match]))
                print(f"    sin^2(theta_W)(M_Z) = {sin2_check[0]:.6f} (target: {SIN2_TW_PDG})")
                break
    else:
        print(f"\n  NO CROSSING: sin^2(M_Z) never reaches {SIN2_TW_PDG}")
        print(f"  Closest approach: {sin2_scan[valid][np.argmin(np.abs(sin2_scan[valid] - SIN2_TW_PDG))]:.6f}")
        closest_idx = np.argmin(np.abs(sin2_scan[valid] - SIN2_TW_PDG))
        log_M_closest = log_M_range[valid][closest_idx]
        print(f"  at M_KK = 10^{log_M_closest:.2f} GeV")

    # ─── Also scan across several g1/g2 values on the contour ────────────
    print(f"\n  Scanning g1/g2 values on Weinberg contour:")
    print(f"  {'g1/g2':>8s} {'(g1/g2)^2':>10s} {'M_KK_match':>14s} {'sin2(M_Z)@10^16':>16s}")

    # Pick representative g1/g2 values
    unique_g1g2 = np.unique(np.round(contour_g1g2, 4))
    for g_val in unique_g1g2[:15]:  # limit output
        sin2_test, _, _ = rge_a_scan(g_val, np.array([1e16]))
        # Find crossing
        sin2_full, _, _ = rge_a_scan(g_val, M_KK_range)
        valid_f = ~np.isnan(sin2_full)
        crossing_str = "none"
        for k in range(len(sin2_full) - 1):
            if np.isnan(sin2_full[k]) or np.isnan(sin2_full[k+1]):
                continue
            if (sin2_full[k] - SIN2_TW_PDG) * (sin2_full[k+1] - SIN2_TW_PDG) < 0:
                frac = (SIN2_TW_PDG - sin2_full[k]) / (sin2_full[k+1] - sin2_full[k])
                log_cross = log_M_range[k] + frac * (log_M_range[k+1] - log_M_range[k])
                crossing_str = f"10^{log_cross:.2f}"
                break
        print(f"  {g_val:8.4f} {g_val**2:10.6f} {crossing_str:>14s} "
              f"{sin2_test[0]:16.6f}" if not np.isnan(sin2_test[0]) else
              f"  {g_val:8.4f} {g_val**2:10.6f} {crossing_str:>14s} {'NaN':>16s}")

    # ─── RGE-B: Individual coupling test ─────────────────────────────────
    print(f"\n{'=' * 70}")
    print("RGE-B: Individual coupling test")
    print(f"{'=' * 70}")

    if M_KK_match is not None:
        # Run at matched M_KK
        r_KK = 5.0 * g1g2_best**2  # GUT-normalized ratio
        ln_up = np.log(M_KK_match / M_Z)
        inv_a2_KK = 1.0 / ALPHA_2_MZ - B2 / (2.0 * np.pi) * ln_up
        alpha_2_KK = 1.0 / inv_a2_KK
        alpha_1_KK = r_KK * alpha_2_KK

        a1_low, a2_low, sin2_low = rge_run_down(alpha_1_KK, alpha_2_KK, M_KK_match)

        print(f"  At M_KK = {M_KK_match:.3e} GeV:")
        print(f"    alpha_1(M_KK) = {alpha_1_KK:.6f}")
        print(f"    alpha_2(M_KK) = {alpha_2_KK:.6f}")
        print(f"    alpha_1/alpha_2 = {alpha_1_KK/alpha_2_KK:.6f}")
        print(f"\n  Evolved to M_Z = {M_Z} GeV:")
        print(f"    alpha_1(M_Z) = {a1_low:.6f}  (PDG: {ALPHA_1_MZ})")
        print(f"    alpha_2(M_Z) = {a2_low:.6f}  (PDG: {ALPHA_2_MZ})")
        print(f"    sin^2(theta_W) = {sin2_low:.6f}  (PDG: {SIN2_TW_PDG})")
        print(f"\n  Deviations:")
        print(f"    delta alpha_1 / alpha_1 = {(a1_low - ALPHA_1_MZ)/ALPHA_1_MZ:.4f} ({(a1_low - ALPHA_1_MZ)/ALPHA_1_MZ*100:.2f}%)")
        print(f"    delta alpha_2 / alpha_2 = {(a2_low - ALPHA_2_MZ)/ALPHA_2_MZ:.4f} ({(a2_low - ALPHA_2_MZ)/ALPHA_2_MZ*100:.2f}%)")

        # RGE-B verdict: by construction, alpha_2 matches (we fixed it).
        # alpha_1 match is the test.
        a1_dev = abs(a1_low - ALPHA_1_MZ) / ALPHA_1_MZ
        rge_b_pass = a1_dev < 0.05  # 5% tolerance
        print(f"\n  RGE-B verdict: {'PASS' if rge_b_pass else 'FAIL'} "
              f"(alpha_1 deviation {a1_dev*100:.2f}%, threshold 5%)")
    else:
        print("  SKIPPED: No M_KK crossing found in RGE-A.")
        rge_b_pass = False

    # ─── Alternative approach: Fix alpha_1 normalization ─────────────────
    print(f"\n{'=' * 70}")
    print("RGE-A ALTERNATIVE: Fix normalization via alpha_1_GUT instead of alpha_2")
    print(f"{'=' * 70}")

    r_KK = 5.0 * g1g2_best**2  # GUT-normalized ratio
    sin2_alt = np.zeros_like(M_KK_range)
    for k, M_KK in enumerate(M_KK_range):
        ln_up = np.log(M_KK / M_Z)
        # Fix alpha_1_GUT(M_KK) by running PDG alpha_1_GUT(M_Z) upward
        inv_a1_KK = 1.0 / ALPHA_1_MZ - B1 / (2.0 * np.pi) * ln_up
        if inv_a1_KK <= 0:
            sin2_alt[k] = np.nan
            continue
        alpha_1_KK = 1.0 / inv_a1_KK
        # alpha_2 from ratio
        alpha_2_KK = alpha_1_KK / r_KK
        # Run both down
        a1_l, a2_l, s2_l = rge_run_down(alpha_1_KK, alpha_2_KK, M_KK)
        sin2_alt[k] = s2_l

    valid_alt = ~np.isnan(sin2_alt)
    print(f"  sin^2 range (alpha_1-fixed): [{sin2_alt[valid_alt].min():.6f}, {sin2_alt[valid_alt].max():.6f}]")

    # ─── NCG-KK Tension (XS-2) ──────────────────────────────────────────
    print(f"\n{'=' * 70}")
    print("NCG-KK TENSION ANALYSIS (XS-2)")
    print(f"{'=' * 70}")

    # At each contour point, find where alpha_1 = alpha_2 above M_KK
    # Use a reference M_KK (from RGE-A match if available, else 10^16)
    M_KK_ref = M_KK_match if M_KK_match is not None else 1e16
    print(f"\n  Reference M_KK = {M_KK_ref:.3e} GeV")

    # Determine alpha_1_GUT, alpha_2 at M_KK_ref
    r_KK = 5.0 * g1g2_best**2  # GUT-normalized ratio
    ln_up = np.log(M_KK_ref / M_Z)
    inv_a2_KK = 1.0 / ALPHA_2_MZ - B2 / (2.0 * np.pi) * ln_up
    alpha_2_KK = 1.0 / inv_a2_KK
    alpha_1_KK = r_KK * alpha_2_KK

    print(f"  alpha_1_GUT(M_KK) = {alpha_1_KK:.6f}")
    print(f"  alpha_2(M_KK) = {alpha_2_KK:.6f}")
    print(f"  alpha_1_GUT/alpha_2 = {alpha_1_KK/alpha_2_KK:.6f}")
    print(f"  sin^2(theta_W)_KK = {3*g1g2_best**2/(1+3*g1g2_best**2):.6f}  (Formula B)")

    Lambda_SA, ratio_SA, t_SA = find_unification_scale(alpha_1_KK, alpha_2_KK, M_KK_ref)

    print(f"\n  Unification scale Lambda_SA:")
    if np.isfinite(Lambda_SA) and Lambda_SA > 0:
        print(f"    Lambda_SA = {Lambda_SA:.3e} GeV = 10^{np.log10(Lambda_SA):.2f} GeV")
        print(f"    Lambda_SA / M_KK = {ratio_SA:.4e}")
        print(f"    ln(Lambda_SA / M_KK) = {t_SA:.4f}")

        # Gate classification
        if 1e-3 <= ratio_SA <= 1e3:
            nck_status = "MILD (within [10^-3, 10^3])"
            nck_fires = False
        else:
            nck_status = "B-30nck FIRES (outside [10^-3, 10^3])"
            nck_fires = True
        print(f"\n  B-30nck: {nck_status}")
    else:
        print(f"    Lambda_SA cannot be computed (alpha_1 > alpha_2 requires upward running)")
        print(f"    t = {t_SA:.4f} => {'already unified (t<0)' if t_SA < 0 else 'Landau pole before unification'}")
        nck_fires = None

    # Scan: how does tension depend on tau along contour?
    print(f"\n  NCG-KK tension scan across Weinberg contour:")
    print(f"  {'tau':>6s} {'eps':>7s} {'g1/g2':>7s} {'a1/a2':>7s} "
          f"{'Lambda_SA':>12s} {'Ratio':>12s} {'Status':>8s}")
    for k in range(min(15, len(sort_idx))):
        idx = sort_idx[k]
        g_val = contour_g1g2[idx]
        r_val = 5.0 * g_val**2  # GUT-normalized ratio
        a2_kk = alpha_2_KK  # same for all (set by M_KK_ref)
        a1_kk = r_val * a2_kk

        lam, rat, t_val = find_unification_scale(a1_kk, a2_kk, M_KK_ref)
        status = "OK" if 1e-3 <= rat <= 1e3 else "FIRE"
        print(f"  {contour_tau[idx]:6.3f} {contour_eps[idx]:7.4f} "
              f"{g_val:7.4f} {r_val:7.4f} "
              f"10^{np.log10(lam):5.2f} {rat:12.4e} {status:>8s}")

    # ─── B-30rge gate ────────────────────────────────────────────────────
    print(f"\n{'=' * 70}")
    print("GATE VERDICTS")
    print(f"{'=' * 70}")

    # B-30rge: sin^2(theta_W)(M_Z) < 0.15 or > 0.30 for ALL M_KK in [10^10, 10^18]
    mask_gate = (log_M_range >= 10) & (log_M_range <= 18) & valid
    if np.any(mask_gate):
        sin2_gate_range = sin2_scan[mask_gate]
        sin2_gate_min = sin2_gate_range.min()
        sin2_gate_max = sin2_gate_range.max()
        print(f"\n  B-30rge: sin^2(theta_W)(M_Z) for M_KK in [10^10, 10^18] GeV:")
        print(f"    Range: [{sin2_gate_min:.6f}, {sin2_gate_max:.6f}]")
        b30rge_fires = (sin2_gate_max < 0.15) or (sin2_gate_min > 0.30)
        print(f"    B-30rge FIRES: {b30rge_fires}")
        if not b30rge_fires:
            print(f"    (sin^2 covers part of [0.15, 0.30] => gate does NOT fire)")
    else:
        print(f"\n  B-30rge: No valid data in [10^10, 10^18] range")
        b30rge_fires = None

    # RGE-A gate
    rge_a_pass = M_KK_match is not None and 1e10 <= M_KK_match <= 1e18
    print(f"\n  RGE-A: g1/g2 runs to tan(theta_W) = 0.553 at M_Z for some M_KK?")
    print(f"    tan(theta_W) = sqrt(sin^2/(1-sin^2)) at target = {np.sqrt(SIN2_TW_PDG/(1-SIN2_TW_PDG)):.4f}")
    if M_KK_match is not None:
        print(f"    M_KK match = {M_KK_match:.3e} GeV = 10^{np.log10(M_KK_match):.2f} GeV")
        print(f"    In [10^10, 10^18]: {rge_a_pass}")
    else:
        print(f"    No crossing found. RGE-A: FAIL")
    print(f"    RGE-A verdict: {'PASS' if rge_a_pass else 'FAIL'}")

    # ─── Summary ─────────────────────────────────────────────────────────
    print(f"\n{'=' * 70}")
    print("SUMMARY")
    print(f"{'=' * 70}")
    print(f"\n  Input:")
    print(f"    g1g2_code = sqrt(L2/L1) = {g1g2_best:.6f} (at best Weinberg contour point)")
    print(f"    tau = {tau_best:.4f}, eps = {eps_best:.4f}")
    print(f"    sin^2_B (KK-scale) = {sin2B_best:.5f}")
    print(f"    alpha_1_GUT/alpha_2 = 5*L2/L1 = {5.0*g1g2_best**2:.6f}  (GUT-normalized)")
    print(f"    alpha_Y/alpha_2 = 3*L2/L1 = {3.0*g1g2_best**2:.6f}  (SM hypercharge)")

    print(f"\n  RGE-A: {'PASS' if rge_a_pass else 'FAIL'}")
    if M_KK_match is not None:
        print(f"    M_KK = 10^{np.log10(M_KK_match):.2f} GeV")
    print(f"  RGE-B: {'PASS' if rge_b_pass else 'FAIL (or SKIPPED)'}")
    print(f"  B-30rge: {'FIRES' if b30rge_fires else 'DOES NOT FIRE'}")
    print(f"  B-30nck: {'FIRES' if nck_fires else 'DOES NOT FIRE' if nck_fires is not None else 'INDETERMINATE'}")

    t_total = time.time() - t0
    print(f"\n  Total runtime: {t_total:.1f}s")

    # ─── Save results ────────────────────────────────────────────────────
    save_dict = {
        # Input
        'g1g2_best': g1g2_best,
        'tau_best': tau_best,
        'eps_best': eps_best,
        'sin2B_best': sin2B_best,
        'V_best': V_best,
        'L1_best': L1_best,
        'L2_best': L2_best,
        # Contour data
        'contour_tau': contour_tau,
        'contour_eps': contour_eps,
        'contour_g1g2': contour_g1g2,
        'contour_sin2B': contour_sin2B,
        'contour_V': contour_V,
        # RGE scan
        'log_M_range': log_M_range,
        'sin2_scan': sin2_scan,
        'alpha1_scan': a1_scan,
        'alpha2_scan': a2_scan,
        'sin2_alt': sin2_alt,
        # Full grid Formula B
        'sin2_B_grid': sin2_B,
        # Gate verdicts
        'rge_a_pass': rge_a_pass,
        'rge_b_pass': rge_b_pass,
        'b30rge_fires': b30rge_fires if b30rge_fires is not None else False,
    }
    if M_KK_match is not None:
        save_dict['M_KK_match'] = M_KK_match
    if Lambda_SA is not None and np.isfinite(Lambda_SA):
        save_dict['Lambda_SA'] = Lambda_SA
        save_dict['Lambda_SA_ratio'] = ratio_SA

    np.savez_compressed(OUT_NPZ, **save_dict)
    print(f"\n  Saved: {OUT_NPZ}")

    # ─── Plot ────────────────────────────────────────────────────────────
    fig, axes = plt.subplots(2, 2, figsize=(14, 11))

    # Panel 1: sin^2(theta_W)(M_Z) vs log10(M_KK)
    ax = axes[0, 0]
    valid_mask = ~np.isnan(sin2_scan)
    ax.plot(log_M_range[valid_mask], sin2_scan[valid_mask], 'b-', linewidth=2,
            label=f'g1/g2={g1g2_best:.4f} (alpha_2-fixed)')
    valid_alt_mask = ~np.isnan(sin2_alt)
    ax.plot(log_M_range[valid_alt_mask], sin2_alt[valid_alt_mask], 'r--', linewidth=1.5,
            label=f'g1/g2={g1g2_best:.4f} (alpha_1-fixed)')
    ax.axhline(SIN2_TW_PDG, color='green', linestyle=':', linewidth=2, label=f'SM: {SIN2_TW_PDG}')
    ax.axhspan(0.15, 0.30, alpha=0.1, color='green', label='[0.15, 0.30]')
    ax.axvspan(10, 18, alpha=0.1, color='blue', label='Gate range')
    if M_KK_match is not None:
        ax.axvline(np.log10(M_KK_match), color='red', linestyle='-', linewidth=1.5,
                   label=f'Match: 10^{np.log10(M_KK_match):.1f}')
    ax.set_xlabel('log10(M_KK / GeV)', fontsize=11)
    ax.set_ylabel('sin^2(theta_W)(M_Z)', fontsize=11)
    ax.set_title('RGE-A: Weinberg Angle at M_Z', fontsize=12)
    ax.legend(fontsize=8, loc='best')
    ax.set_xlim(4, 19)
    ax.grid(True, alpha=0.3)

    # Panel 2: Formula B contour on grid
    ax = axes[0, 1]
    TAU_g, EPS_g = np.meshgrid(tau, eps, indexing='ij')
    c = ax.contourf(TAU_g, EPS_g, sin2_B, levels=30, cmap='viridis')
    plt.colorbar(c, ax=ax, label='sin^2_B')
    cs = ax.contour(TAU_g, EPS_g, sin2_B, levels=[0.20, 0.231, 0.25],
                    colors=['white', 'red', 'white'], linewidths=[1, 2.5, 1])
    ax.clabel(cs, inline=True, fontsize=9, fmt='%.3f')
    # Mark best contour point
    ax.plot(tau_best, eps_best, 'r*', markersize=15, markeredgecolor='white')
    ax.set_xlabel('tau')
    ax.set_ylabel('epsilon')
    ax.set_title('Formula B: sin^2(theta_W) on grid')

    # Panel 3: g1/g2 on grid with Weinberg contour
    ax = axes[1, 0]
    c = ax.contourf(TAU_g, EPS_g, g1g2, levels=30, cmap='plasma')
    plt.colorbar(c, ax=ax, label='g1/g2')
    cs = ax.contour(TAU_g, EPS_g, sin2_B, levels=[0.231],
                    colors=['lime'], linewidths=[2.5])
    ax.clabel(cs, inline=True, fontsize=9, fmt='%.3f')
    ax.plot(tau_best, eps_best, 'r*', markersize=15, markeredgecolor='white')
    ax.set_xlabel('tau')
    ax.set_ylabel('epsilon')
    ax.set_title('g1/g2 with Weinberg contour (sin^2_B=0.231)')

    # Panel 4: Individual couplings at M_Z vs M_KK
    ax = axes[1, 1]
    valid_a1 = ~np.isnan(a1_scan)
    valid_a2 = ~np.isnan(a2_scan)
    ax.plot(log_M_range[valid_a1], a1_scan[valid_a1], 'b-', linewidth=2, label='alpha_1(M_Z)')
    ax.plot(log_M_range[valid_a2], a2_scan[valid_a2], 'r-', linewidth=2, label='alpha_2(M_Z)')
    ax.axhline(ALPHA_1_MZ, color='blue', linestyle=':', label=f'PDG alpha_1 = {ALPHA_1_MZ}')
    ax.axhline(ALPHA_2_MZ, color='red', linestyle=':', label=f'PDG alpha_2 = {ALPHA_2_MZ}')
    if M_KK_match is not None:
        ax.axvline(np.log10(M_KK_match), color='green', linestyle='--', linewidth=1.5)
    ax.set_xlabel('log10(M_KK / GeV)', fontsize=11)
    ax.set_ylabel('alpha_i(M_Z)', fontsize=11)
    ax.set_title('RGE-B: Individual Couplings at M_Z', fontsize=12)
    ax.legend(fontsize=8, loc='best')
    ax.set_xlim(4, 19)
    ax.grid(True, alpha=0.3)

    plt.suptitle(f'Session 30Bb: RGE Running | g1/g2 = {g1g2_best:.4f} at tau={tau_best:.3f}',
                 fontsize=13)
    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=150, bbox_inches='tight')
    print(f"  Saved: {OUT_PNG}")

    return save_dict


if __name__ == '__main__':
    results = main()
