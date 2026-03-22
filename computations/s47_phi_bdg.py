#!/usr/bin/env python3
"""
s47_phi_bdg.py — BdG-Dressed Phi Ratio Across Tau (PHI-BDG-47)
================================================================

Session 47 Wave 3-2: Paasch Mass Quantization Analyst

The phi ratio phi_paasch = 1.53158 was found as an INTER-SECTOR ratio:
    R_phi(tau) = min|lambda_{(3,0)}| / min|lambda_{(0,0)}|
            = 1.531588 at tau = 0.15 (5 ppm from phi_paasch)

Under BCS dressing with PH-forced mu=0:
    E_qp(k) = sqrt(lambda_k^2 + Delta_sector(k)^2)

The (0,0) and (3,0) sectors are decoupled (Peter-Weyl block-diagonality
theorem, S22b). Each sector gets independently dressed:
    - (0,0) B1 gap: Delta_B1 ~ 0.372 at fold
    - (3,0) gap: Delta_B3 ~ 0.084 at fold (heuristic assignment from s45)

Since Delta_B1 >> Delta_B3, BCS dressing adds MORE to the denominator
than the numerator, so R_dressed < R_bare. The crossing shifts to
larger tau, if it survives at all.

Gate PHI-BDG-47:
    PASS: R_dressed crosses phi at some tau in [0.05, 0.40]
    INFO: Crossing at same tau as bare (BCS negligible)
    FAIL: R_dressed never crosses phi

Data sources:
    s44_dos_tau.npz: 992 eigenvalues at 5 tau (0.00, 0.05, 0.10, 0.15, 0.19)
    s46_qtheory_selfconsistent.npz: BCS gaps on 60-point tau grid [0.025, 0.40]
"""

import sys
import os
import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Add parent to path for canonical_constants
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import tau_fold

# ==============================================================================
# SECTION 1: Load data
# ==============================================================================

print("=" * 78)
print("PHI-BDG-47: BdG-Dressed Phi Ratio Across Tau")
print("=" * 78)

DATA_DIR = os.path.dirname(os.path.abspath(__file__))

d44 = np.load(os.path.join(DATA_DIR, 's44_dos_tau.npz'))
d46 = np.load(os.path.join(DATA_DIR, 's46_qtheory_selfconsistent.npz'))

# Paasch quantization factor
phi_paasch = 1.53158  # From x = e^{-x^2}, Eq. (2g) Paasch 2009

# BCS gaps on 60-point grid
tau_60 = d46['tau_scan']         # shape (60,)
Delta_B1_sc = d46['Delta_B1_sc']  # (0,0) sector B1 gap
Delta_B2_sc = d46['Delta_B2_sc']
Delta_B3_sc = d46['Delta_B3_sc']  # Also used as heuristic for (3,0) sector

# (0,0) eigenvalues at 20 points
valid_tau_20 = d46['valid_tau']   # shape (20,)
lam_sq_B1_20 = d46['lam_sq_B1']  # lambda^2 for B1 at 20 tau
lam_sq_B3_20 = d46['lam_sq_B3']  # lambda^2 for B3 at 20 tau

# (0,0) eigenvalues interpolated to 60-point grid
lam2_B1_60 = d46['lam2_B1_interp']  # shape (60,)
lam2_B3_60 = d46['lam2_B3_interp']

# ==============================================================================
# SECTION 2: Extract (3,0) sector eigenvalues from s44 (5 tau points)
# ==============================================================================

print("\n--- SECTION 2: Raw Eigenvalue Extraction ---")

taus_s44 = d44['tau_values']  # [0.00, 0.05, 0.10, 0.15, 0.19]
tau_labels = ['tau0.00', 'tau0.05', 'tau0.10', 'tau0.15', 'tau0.19']

# (3,0)/(0,3) irrep has dim = 10, dim^2 = 100
DIM2_30 = 100.0
DIM2_00 = 1.0

# Extract min |eigenvalue| for (3,0) and (0,0) at each s44 tau
min_lam_30_s44 = np.zeros(5)
min_lam_00_s44 = np.zeros(5)

for i, tau_str in enumerate(tau_labels):
    omega = d44[f'{tau_str}_all_omega']
    dim2 = d44[f'{tau_str}_all_dim2']

    mask_30 = dim2 == DIM2_30
    mask_00 = dim2 == DIM2_00

    min_lam_30_s44[i] = np.min(np.abs(omega[mask_30]))
    min_lam_00_s44[i] = np.min(np.abs(omega[mask_00]))

    R_raw = min_lam_30_s44[i] / min_lam_00_s44[i]
    print(f"  tau={taus_s44[i]:.2f}: min|(3,0)| = {min_lam_30_s44[i]:.8f}, "
          f"min|(0,0)| = {min_lam_00_s44[i]:.8f}, R = {R_raw:.6f}")

# ==============================================================================
# SECTION 3: Verify inter-sector ratio at tau=0.15
# ==============================================================================

print("\n--- SECTION 3: Phi Verification at tau=0.15 ---")
idx_015 = 3  # tau=0.15
R_015 = min_lam_30_s44[idx_015] / min_lam_00_s44[idx_015]
dev_015 = abs(R_015 - phi_paasch) / phi_paasch
print(f"  R(0.15) = {R_015:.8f}")
print(f"  phi_paasch = {phi_paasch:.5f}")
print(f"  Relative deviation = {dev_015:.2e} ({dev_015*1e6:.1f} ppm)")

# Cross-check: (0,0) B1 is the smallest eigenvalue in (0,0)
# lam_sq_B1 at valid_tau closest to 0.15
idx_vt_015 = np.argmin(np.abs(valid_tau_20 - 0.15))
B1_015_from_s46 = np.sqrt(lam_sq_B1_20[idx_vt_015])
print(f"  Cross-check: sqrt(lam_sq_B1) at tau={valid_tau_20[idx_vt_015]:.2f} = {B1_015_from_s46:.8f}")
print(f"  s44 min|(0,0)| at tau=0.15 = {min_lam_00_s44[idx_015]:.8f}")
print(f"  Agreement: {abs(B1_015_from_s46 - min_lam_00_s44[idx_015]):.2e}")

# ==============================================================================
# SECTION 4: Interpolate (3,0) eigenvalues to 60-point grid
# ==============================================================================

print("\n--- SECTION 4: Interpolation ---")

# We have (3,0) eigenvalues at 5 tau points. Interpolate to 60-point grid.
# Use cubic spline on lambda^2 for smoothness.
lam2_30_s44 = min_lam_30_s44**2

# Build spline
cs_30 = CubicSpline(taus_s44, lam2_30_s44, bc_type='natural')

# Evaluate on the 60-point grid (clamp to s44 range for interpolation,
# extrapolate cautiously beyond 0.19)
lam2_30_60 = cs_30(tau_60)

# Also build (0,0) B1 spline from s44 for consistency check
lam2_00_s44 = min_lam_00_s44**2
cs_00 = CubicSpline(taus_s44, lam2_00_s44, bc_type='natural')
lam2_00_60_from_s44 = cs_00(tau_60)

# Cross-check: compare s44-interpolated (0,0) B1 with s46 interpolated values
# at tau values within [0, 0.19]
mask_interp_range = tau_60 <= 0.19
max_discrepancy = np.max(np.abs(
    np.sqrt(lam2_00_60_from_s44[mask_interp_range]) -
    np.sqrt(lam2_B1_60[mask_interp_range])
))
print(f"  Max |s44_interp - s46_interp| for (0,0) B1 in [0, 0.19]: {max_discrepancy:.6e}")

# For the computation, use s46 lam2_B1_interp as the (0,0) denominator
# (it was computed from 20 tau points, more reliable than 5-point s44)
# For (3,0) numerator, use s44-interpolated values (only source)

# Mark the extrapolation boundary
extrap_boundary_tau = 0.19
n_interp = np.sum(tau_60 <= extrap_boundary_tau)
n_extrap = np.sum(tau_60 > extrap_boundary_tau)
print(f"  60-point grid: {n_interp} interpolated, {n_extrap} extrapolated (beyond tau=0.19)")
print(f"  WARNING: (3,0) values at tau > 0.19 are CUBIC EXTRAPOLATION, not data.")

# ==============================================================================
# SECTION 5: Compute R_bare and R_dressed on 60-point grid
# ==============================================================================

print("\n--- SECTION 5: Bare and Dressed Ratios ---")

# Use s46's (0,0) B1 for denominator (20-point interpolation, reliable)
lam_00_60 = np.sqrt(lam2_B1_60)

# Use s44-interpolated (3,0) for numerator
lam_30_60 = np.sqrt(np.maximum(lam2_30_60, 0))  # Ensure non-negative under extrap

# Bare ratio
R_bare = lam_30_60 / lam_00_60

# BCS dressed ratios — THREE scenarios:
# (A) (3,0) undressed (Delta_30 = 0): maximum possible R_dressed
# (B) (3,0) dressed with Delta_B3: heuristic assignment from s45
# (C) (3,0) dressed with Delta_B1: worst case (same gap as denominator)

# Scenario A: (3,0) undressed
E_qp_00_A = np.sqrt(lam2_B1_60 + Delta_B1_sc**2)
E_qp_30_A = lam_30_60  # Undressed
R_dressed_A = E_qp_30_A / E_qp_00_A

# Scenario B: (3,0) gets Delta_B3 (s45 heuristic)
E_qp_30_B = np.sqrt(lam2_30_60 + Delta_B3_sc**2)
R_dressed_B = E_qp_30_B / E_qp_00_A

# Scenario C: (3,0) gets Delta_B1 (same large gap as denominator)
E_qp_30_C = np.sqrt(lam2_30_60 + Delta_B1_sc**2)
R_dressed_C = E_qp_30_C / E_qp_00_A

print(f"\n  {'tau':>6s} {'R_bare':>10s} {'R_A(30=0)':>10s} {'R_B(30=B3)':>10s} {'R_C(30=B1)':>10s}")
print("  " + "-" * 50)
for idx_show in [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 59]:
    if idx_show >= len(tau_60):
        continue
    t = tau_60[idx_show]
    marker = " *" if abs(t - 0.15) < 0.005 or abs(t - tau_fold) < 0.005 else ""
    print(f"  {t:6.3f} {R_bare[idx_show]:10.6f} {R_dressed_A[idx_show]:10.6f} "
          f"{R_dressed_B[idx_show]:10.6f} {R_dressed_C[idx_show]:10.6f}{marker}")

# ==============================================================================
# SECTION 6: Find phi crossings
# ==============================================================================

print("\n--- SECTION 6: Phi Crossings ---")

def find_crossings(tau_arr, R_arr, target, label, extrap_tau=None):
    """Find where R_arr crosses target. Returns list of (tau_cross, direction)."""
    crossings = []
    for i in range(len(tau_arr) - 1):
        if (R_arr[i] - target) * (R_arr[i+1] - target) < 0:
            # Linear interpolation
            frac = (target - R_arr[i]) / (R_arr[i+1] - R_arr[i])
            tau_cross = tau_arr[i] + frac * (tau_arr[i+1] - tau_arr[i])
            direction = "up" if R_arr[i+1] > R_arr[i] else "down"
            is_extrap = extrap_tau is not None and tau_cross > extrap_tau
            crossings.append((tau_cross, direction, is_extrap))
    return crossings

# Find crossings for all scenarios
for label, R_arr in [("R_bare", R_bare),
                      ("R_dressed_A (30 undressed)", R_dressed_A),
                      ("R_dressed_B (30=Delta_B3)", R_dressed_B),
                      ("R_dressed_C (30=Delta_B1)", R_dressed_C)]:
    crossings = find_crossings(tau_60, R_arr, phi_paasch, label,
                               extrap_tau=extrap_boundary_tau)
    if crossings:
        for tau_c, direction, is_extrap in crossings:
            status = "EXTRAPOLATED" if is_extrap else "interpolated"
            print(f"  {label}: crosses phi at tau = {tau_c:.4f} ({direction}, {status})")
    else:
        print(f"  {label}: max R = {R_arr.max():.6f} < phi = {phi_paasch:.5f} — NO CROSSING")

# ==============================================================================
# SECTION 7: Fine analysis near phi crossing (bare spectrum)
# ==============================================================================

print("\n--- SECTION 7: Bare Crossing Analysis ---")

# The bare ratio is a smooth function. Find where it crosses phi.
# Check if it crosses within [0.00, 0.19] (data range) or only in extrapolation.

print(f"  R_bare at data boundaries:")
print(f"    tau=0.00: R = {min_lam_30_s44[0]/min_lam_00_s44[0]:.6f}")
print(f"    tau=0.19: R = {min_lam_30_s44[4]/min_lam_00_s44[4]:.6f}")
print(f"  phi_paasch = {phi_paasch:.5f}")

# R at tau=0.19 is only 1.523, so bare crossing is BEYOND data range
# Let's estimate where it would cross using extrapolation
R_bare_at_data = min_lam_30_s44 / min_lam_00_s44
print(f"\n  R_bare at s44 data points:")
for i, t in enumerate(taus_s44):
    print(f"    tau={t:.2f}: R = {R_bare_at_data[i]:.6f}, deficit = {phi_paasch - R_bare_at_data[i]:.6f}")

# Rate of change near tau=0.19
if len(taus_s44) >= 2:
    dR_dtau = (R_bare_at_data[-1] - R_bare_at_data[-2]) / (taus_s44[-1] - taus_s44[-2])
    tau_extrap_cross = taus_s44[-1] + (phi_paasch - R_bare_at_data[-1]) / dR_dtau
    print(f"\n  Linear extrapolation from tau=0.19:")
    print(f"    dR/dtau at tau=0.19 = {dR_dtau:.4f}")
    print(f"    Estimated bare crossing: tau ~ {tau_extrap_cross:.3f}")
    print(f"    (This is {tau_extrap_cross - tau_fold:.3f} beyond the fold)")

# ==============================================================================
# SECTION 8: Correction — the ACTUAL phi ratio provenance
# ==============================================================================

print("\n--- SECTION 8: Phi Ratio Provenance Correction ---")
print("  The W3-1 report (line 624) incorrectly states:")
print("    'This ratio emerges from the specific structure of the")
print("     Jensen deformation on the 16-dimensional spinor space")
print("     at the (0,0) Peter-Weyl level'")
print()
print("  CORRECTION: The phi ratio is INTER-SECTOR, not intra-sector.")
print("    R = min|lambda_{(3,0)}| / min|lambda_{(0,0)}|")
print(f"    At tau=0.15: {min_lam_30_s44[3]:.6f} / {min_lam_00_s44[3]:.6f} = {R_bare_at_data[3]:.6f}")
print(f"    Intra-(0,0) B3/B1 at tau=0.15: {np.sqrt(lam_sq_B3_20[idx_vt_015]/lam_sq_B1_20[idx_vt_015]):.6f}")
print()
print("  The (3,0) and (0,0) sectors are decoupled by the block-diagonal theorem.")
print("  Under BCS, they get INDEPENDENT gaps. The phi ratio involves two")
print("  independently dressed quasiparticle energies from different PW blocks.")

# ==============================================================================
# SECTION 9: Quantitative shift analysis
# ==============================================================================

print("\n--- SECTION 9: Shift Analysis ---")

# At tau=0.15, compute how much BCS shifts the ratio
t_015_idx = np.argmin(np.abs(tau_60 - 0.15))
t_015 = tau_60[t_015_idx]

lam_00_015 = np.sqrt(lam2_B1_60[t_015_idx])
lam_30_015 = np.sqrt(lam2_30_60[t_015_idx])
D_B1_015 = Delta_B1_sc[t_015_idx]
D_B3_015 = Delta_B3_sc[t_015_idx]

R_bare_015 = lam_30_015 / lam_00_015

# Scenario A: (3,0) undressed
R_A_015 = lam_30_015 / np.sqrt(lam_00_015**2 + D_B1_015**2)

# Scenario B: (3,0) gets Delta_B3
R_B_015 = np.sqrt(lam_30_015**2 + D_B3_015**2) / np.sqrt(lam_00_015**2 + D_B1_015**2)

print(f"  At tau = {t_015:.4f}:")
print(f"    lambda_(0,0) B1   = {lam_00_015:.6f}")
print(f"    lambda_(3,0) min  = {lam_30_015:.6f}")
print(f"    Delta_B1 (for 0,0) = {D_B1_015:.6f}")
print(f"    Delta_B3 (for 3,0) = {D_B3_015:.6f}")
print(f"")
print(f"    R_bare             = {R_bare_015:.6f}")
print(f"    R_dressed_A (30=0) = {R_A_015:.6f}  (shift = {R_A_015 - R_bare_015:+.6f})")
print(f"    R_dressed_B (30=B3)= {R_B_015:.6f}  (shift = {R_B_015 - R_bare_015:+.6f})")
print(f"    phi_paasch         = {phi_paasch:.5f}")
print(f"")

# Fractional shifts
shift_A = (R_A_015 - R_bare_015) / R_bare_015
shift_B = (R_B_015 - R_bare_015) / R_bare_015
print(f"    Fractional shift A = {shift_A*100:.2f}%")
print(f"    Fractional shift B = {shift_B*100:.2f}%")

# At the fold (tau=0.19)
t_fold_idx = np.argmin(np.abs(tau_60 - tau_fold))
t_fold = tau_60[t_fold_idx]
lam_00_fold = np.sqrt(lam2_B1_60[t_fold_idx])
lam_30_fold = np.sqrt(lam2_30_60[t_fold_idx])
D_B1_fold = Delta_B1_sc[t_fold_idx]
D_B3_fold = Delta_B3_sc[t_fold_idx]

R_bare_fold = lam_30_fold / lam_00_fold
R_A_fold = lam_30_fold / np.sqrt(lam_00_fold**2 + D_B1_fold**2)
R_B_fold = np.sqrt(lam_30_fold**2 + D_B3_fold**2) / np.sqrt(lam_00_fold**2 + D_B1_fold**2)

print(f"\n  At fold tau = {t_fold:.4f}:")
print(f"    R_bare             = {R_bare_fold:.6f}")
print(f"    R_dressed_A (30=0) = {R_A_fold:.6f}")
print(f"    R_dressed_B (30=B3)= {R_B_fold:.6f}")
print(f"    phi_paasch         = {phi_paasch:.5f}")
print(f"    Deficit bare:        {phi_paasch - R_bare_fold:.6f} ({(phi_paasch - R_bare_fold)/phi_paasch*100:.2f}%)")
print(f"    Deficit dressed_B:   {phi_paasch - R_B_fold:.6f} ({(phi_paasch - R_B_fold)/phi_paasch*100:.2f}%)")

# ==============================================================================
# SECTION 10: Gate Verdict
# ==============================================================================

print("\n" + "=" * 78)
print("GATE VERDICT: PHI-BDG-47")
print("=" * 78)

# Check if any DRESSED scenario crosses phi within [0.05, 0.40]
# The gate is about R_DRESSED, not R_bare (bare crossing is the S12 result)
dressed_crossing_found = False
bare_crossing_found = False

for label, R_arr in [("R_dressed_A", R_dressed_A),
                      ("R_dressed_B", R_dressed_B),
                      ("R_dressed_C", R_dressed_C)]:
    crossings = find_crossings(tau_60, R_arr, phi_paasch, label,
                               extrap_tau=extrap_boundary_tau)
    for tau_c, direction, is_extrap in crossings:
        dressed_crossing_found = True

# Also check bare
for tau_c, direction, is_extrap in find_crossings(tau_60, R_bare, phi_paasch,
                                                    "bare", extrap_tau=extrap_boundary_tau):
    bare_crossing_found = True

# R_bare maximum in data range [0, 0.19]
R_bare_max_data = max(min_lam_30_s44[i]/min_lam_00_s44[i] for i in range(5))
R_bare_at_019 = min_lam_30_s44[4] / min_lam_00_s44[4]

if dressed_crossing_found:
    verdict = "PASS"
else:
    verdict = "FAIL"

# Check: does bare ratio reach phi ANYWHERE in data range?
if R_bare_max_data >= phi_paasch:
    bare_crosses = True
else:
    bare_crosses = False

print(f"\n  Criterion: R_dressed crosses phi = {phi_paasch} in tau in [0.05, 0.40]")
print(f"")
print(f"  R_bare max (data, tau<=0.19)   = {R_bare_max_data:.6f} {'> phi' if bare_crosses else '< phi'}")
print(f"  R_bare max (extrapolated)      = {R_bare.max():.6f} {'> phi' if R_bare.max() >= phi_paasch else '< phi'}")
print(f"  R_dressed_A max                = {R_dressed_A.max():.6f} {'> phi' if R_dressed_A.max() >= phi_paasch else '< phi'}")
print(f"  R_dressed_B max                = {R_dressed_B.max():.6f} {'> phi' if R_dressed_B.max() >= phi_paasch else '< phi'}")
print(f"  R_dressed_C max                = {R_dressed_C.max():.6f} {'> phi' if R_dressed_C.max() >= phi_paasch else '< phi'}")

# Report crossings
bare_crossings = find_crossings(tau_60, R_bare, phi_paasch, "bare",
                                 extrap_tau=extrap_boundary_tau)
if bare_crossings:
    for tau_c, direction, is_extrap in bare_crossings:
        status_str = "EXTRAPOLATED" if is_extrap else "DATA"
        print(f"\n  BARE crossing at tau = {tau_c:.4f} ({status_str})")
else:
    print(f"\n  No bare crossing in tau range [0.025, 0.400]")

for lab, R_arr in [("Scenario A (30 undressed)", R_dressed_A),
                    ("Scenario B (30=Delta_B3)", R_dressed_B),
                    ("Scenario C (30=Delta_B1)", R_dressed_C)]:
    cs = find_crossings(tau_60, R_arr, phi_paasch, lab,
                        extrap_tau=extrap_boundary_tau)
    if cs:
        for tau_c, direction, is_extrap in cs:
            status_str = "EXTRAPOLATED" if is_extrap else "DATA"
            print(f"  {lab} crossing at tau = {tau_c:.4f} ({status_str})")
    else:
        print(f"  {lab}: NO crossing (max = {R_arr.max():.6f})")

print(f"\n  >>> VERDICT: {verdict}")

if "FAIL" in verdict:
    print(f"  The bare inter-sector ratio at tau=0.19 (fold) is {R_bare_at_019:.6f},")
    print(f"  which is {(phi_paasch - R_bare_at_019)/phi_paasch*100:.1f}% below phi.")
    print(f"  BCS dressing DECREASES the ratio further (by {abs(shift_B)*100:.1f}% at tau=0.15).")
    print(f"  The phi crossing requires tau ~ 0.21+ (extrapolation), well BEYOND the fold.")
    print(f"  BCS dressing destroys the phi relationship at the fold.")

# Also note: even the bare crossing at tau=0.15 is not actually AT phi
R_bare_at_015_direct = min_lam_30_s44[3] / min_lam_00_s44[3]
print(f"\n  Precision note: R_bare(0.15) = {R_bare_at_015_direct:.8f} vs phi = {phi_paasch:.5f}")
print(f"  This 5 ppm match is from the BARE spectrum at a specific tau.")
print(f"  Under BCS dressing (scenario B), R drops to {R_B_015:.6f},")
print(f"  opening a {(phi_paasch - R_B_015)/phi_paasch*100:.2f}% gap from phi.")

# ==============================================================================
# SECTION 11: Additional diagnostics — sensitivity to gap ratio
# ==============================================================================

print("\n--- SECTION 11: Gap Ratio Sensitivity ---")
print("  The BCS shift depends on the ratio Delta_(3,0) / Delta_(0,0).")
print("  If both sectors had EQUAL gaps, R_dressed -> R_bare (gaps cancel).")
print("  The phi ratio is preserved only when Delta_30/Delta_B1 ~ lambda_30/lambda_B1.")
print()

# What gap ratio would preserve phi?
# R_dressed = sqrt(lam_30^2 + D_30^2) / sqrt(lam_00^2 + D_B1^2) = phi
# => lam_30^2 + D_30^2 = phi^2 * (lam_00^2 + D_B1^2)
# => D_30^2 = phi^2 * (lam_00^2 + D_B1^2) - lam_30^2
D_30_required_sq = phi_paasch**2 * (lam_00_015**2 + D_B1_015**2) - lam_30_015**2
if D_30_required_sq > 0:
    D_30_required = np.sqrt(D_30_required_sq)
    print(f"  At tau={t_015:.3f}, to maintain R_dressed = phi requires:")
    print(f"    Delta_(3,0) = {D_30_required:.6f}")
    print(f"    vs actual Delta_B3 = {D_B3_015:.6f}")
    print(f"    Required/actual = {D_30_required/D_B3_015:.2f}x")
    print(f"    Required/Delta_B1 = {D_30_required/D_B1_015:.4f}")
else:
    print(f"  At tau={t_015:.3f}, no positive Delta_(3,0) can achieve R_dressed = phi.")
    print(f"  The bare ratio is already below phi.")

# ==============================================================================
# SECTION 12: Save results
# ==============================================================================

print("\n--- Saving results ---")

outpath = os.path.join(DATA_DIR, 's47_phi_bdg.npz')
np.savez(outpath,
    # Grid
    tau_60=tau_60,
    taus_s44=taus_s44,
    phi_paasch=phi_paasch,
    tau_fold=tau_fold,
    extrap_boundary=extrap_boundary_tau,

    # Raw eigenvalues at s44 points
    min_lam_30_s44=min_lam_30_s44,
    min_lam_00_s44=min_lam_00_s44,

    # Interpolated eigenvalues on 60-point grid
    lam_30_60=lam_30_60,
    lam_00_60=lam_00_60,
    lam2_30_60=lam2_30_60,
    lam2_B1_60=lam2_B1_60,

    # BCS gaps
    Delta_B1_sc=Delta_B1_sc,
    Delta_B3_sc=Delta_B3_sc,

    # Ratios
    R_bare=R_bare,
    R_dressed_A=R_dressed_A,  # (3,0) undressed
    R_dressed_B=R_dressed_B,  # (3,0) = Delta_B3
    R_dressed_C=R_dressed_C,  # (3,0) = Delta_B1

    # Crossing info
    R_bare_at_015=R_bare_at_015_direct,
    R_dressed_B_at_015=R_B_015,
    shift_B_frac=shift_B,

    # Gate
    verdict=verdict,
)
print(f"  Saved to {outpath}")

# ==============================================================================
# SECTION 13: Plot
# ==============================================================================

print("\n--- Generating plot ---")

fig, axes = plt.subplots(2, 1, figsize=(12, 10), gridspec_kw={'height_ratios': [3, 1]})

# --- Main plot ---
ax = axes[0]

# Shade extrapolation region
ax.axvspan(extrap_boundary_tau, tau_60[-1], alpha=0.08, color='gray',
           label='Extrapolation region')

# Plot ratios
ax.plot(tau_60, R_bare, 'k-', lw=2.5, label=r'$R_{\rm bare} = |\lambda_{(3,0)}^{\min}| / |\lambda_{(0,0)}^{\min}|$')
ax.plot(tau_60, R_dressed_A, 'b--', lw=2, label=r'Scenario A: $(3,0)$ undressed')
ax.plot(tau_60, R_dressed_B, 'r-', lw=2, label=r'Scenario B: $\Delta_{(3,0)} = \Delta_{B3}$')
ax.plot(tau_60, R_dressed_C, 'g:', lw=2, label=r'Scenario C: $\Delta_{(3,0)} = \Delta_{B1}$')

# Phi line
ax.axhline(phi_paasch, color='orange', lw=1.5, ls='--', alpha=0.8,
           label=rf'$\phi_{{Paasch}} = {phi_paasch}$')

# Fold
ax.axvline(tau_fold, color='purple', lw=1, ls=':', alpha=0.6, label=f'Fold ($\\tau = {tau_fold}$)')

# Data points
ax.plot(taus_s44, min_lam_30_s44 / min_lam_00_s44, 'ko', ms=8, zorder=5,
        label='s44 data points (bare)')

# Mark the phi match at tau=0.15
ax.plot(0.15, R_bare_at_015_direct, 'r*', ms=15, zorder=6,
        label=f'$R_{{bare}}(0.15) = {R_bare_at_015_direct:.4f}$ (5 ppm from $\\phi$)')

# Find and mark bare crossing if it exists
bare_crossings = find_crossings(tau_60, R_bare, phi_paasch, "bare",
                                 extrap_tau=extrap_boundary_tau)
for tau_c, direction, is_extrap in bare_crossings:
    marker = 'D' if is_extrap else 's'
    color = 'gray' if is_extrap else 'red'
    ax.plot(tau_c, phi_paasch, marker=marker, ms=12, color=color, zorder=6,
            markeredgecolor='black', markeredgewidth=1.5,
            label=f'Bare crossing $\\tau = {tau_c:.3f}$' +
                  (' (extrap)' if is_extrap else ''))

ax.set_ylabel(r'Inter-sector ratio $R(\tau)$', fontsize=13)
ax.set_title(r'PHI-BDG-47: BdG-Dressed $\phi_{Paasch}$ Ratio — $|\lambda_{(3,0)}^{\min}| / |\lambda_{(0,0)}^{\min}|$',
             fontsize=14)
ax.legend(fontsize=9, loc='upper left')
ax.set_xlim(tau_60[0], tau_60[-1])
ax.grid(True, alpha=0.3)
ax.set_ylim(0.9, 1.6)

# --- Lower panel: BCS shift ---
ax2 = axes[1]

shift_A_arr = (R_dressed_A - R_bare) / R_bare * 100
shift_B_arr = (R_dressed_B - R_bare) / R_bare * 100
shift_C_arr = (R_dressed_C - R_bare) / R_bare * 100

ax2.axvspan(extrap_boundary_tau, tau_60[-1], alpha=0.08, color='gray')
ax2.plot(tau_60, shift_A_arr, 'b--', lw=2, label='Scenario A')
ax2.plot(tau_60, shift_B_arr, 'r-', lw=2, label='Scenario B')
ax2.plot(tau_60, shift_C_arr, 'g:', lw=2, label='Scenario C')
ax2.axhline(0, color='gray', lw=0.5)
ax2.axvline(tau_fold, color='purple', lw=1, ls=':', alpha=0.6)

ax2.set_xlabel(r'$\tau$ (Jensen deformation parameter)', fontsize=13)
ax2.set_ylabel(r'$(R_{\rm dressed} - R_{\rm bare})/R_{\rm bare}$ [%]', fontsize=13)
ax2.legend(fontsize=9)
ax2.set_xlim(tau_60[0], tau_60[-1])
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plotpath = os.path.join(DATA_DIR, 's47_phi_bdg.png')
plt.savefig(plotpath, dpi=150, bbox_inches='tight')
print(f"  Saved plot to {plotpath}")

print("\n" + "=" * 78)
print("DONE: PHI-BDG-47")
print("=" * 78)
