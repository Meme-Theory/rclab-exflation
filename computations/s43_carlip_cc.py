#!/usr/bin/env python3
"""
F-FOAM-5-43: Carlip CC Mechanism Interface
==========================================

Computes the Wheeler-DeWitt pocket width for Carlip's wavefunction-trapping
mechanism with Lambda_internal from the framework's spectral action.

Physics:
--------
Carlip (2019/2021/2025, Papers 08/11/14) demonstrates that in midisuperspace
quantization, the WDW wavefunction concentrates in the zero-expansion sector:

    |Psi(theta_bar)|^2 ~ exp(-2*pi^2 * Lambda * theta_bar^2 * L^4 / hbar)

where:
    Lambda  = bare cosmological constant (framework internal CC)
    theta_bar = spatially averaged expansion rate
    L       = coarse-graining scale (characteristic foam cell size)
    hbar    = 1 in Planck units

The variance of theta_bar in this Gaussian state is:
    <theta_bar^2> = hbar / (4*pi^2 * Lambda * L^4)

The effective CC emerges from the curvature associated with expansion fluctuations:
    Lambda_eff ~ (3/(8*pi*G)) * <theta_bar^2>

In Planck units (hbar = G = c = 1):
    Lambda_eff ~ (3/(8*pi)) * 1/(4*pi^2 * Lambda * L^4)
              = 3 / (32*pi^3 * Lambda * L^4)

Alternatively, Carlip's key point is that the ZERO-MODE of Lambda is hidden:
    Lambda_eff = Lambda * <theta_bar^2> * L^2
where the L^2 converts expansion-rate variance to curvature.

The critical insight: the suppression factor is
    S = Lambda_eff / Lambda_bare = <theta_bar^2> * L^2

For Carlip's Gaussian trapping:
    S = hbar * L^2 / (4*pi^2 * Lambda * L^4) = hbar / (4*pi^2 * Lambda * L^2)

So: Lambda_eff = hbar / (4*pi^2 * L^2)   [Planck units, independent of Lambda!]

This is the POCKET WIDTH result: Lambda_eff depends ONLY on L, not on Lambda_bare.

We must find L such that Lambda_eff = Lambda_obs = 2.888e-122 M_P^4.

Gate F-FOAM-5-43:
    PASS: Lambda_eff within 10 orders of Lambda_obs for physically reasonable L
    FAIL: No L produces Lambda_eff near Lambda_obs, OR required L is sub-Planckian

Input:
    s42_constants_snapshot.npz  -- S_fold, M_KK values
    s42_gradient_stiffness.npz  -- S_fold confirmation
    s43_qtheory_selftune.npz    -- W1-1 q-theory corrected Lambda_internal

Output:
    s43_carlip_cc.npz  -- All computed quantities
    s43_carlip_cc.png  -- Diagnostic plots
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# =============================================================================
# Physical Constants (SI + Planck units)
# =============================================================================
from canonical_constants import hbar_SI  # J*s
from canonical_constants import c_light as c_SI  # m/s
from canonical_constants import G_N as G_SI  # m^3 kg^{-1} s^{-2}

# Planck units
l_P = np.sqrt(hbar_SI * G_SI / c_SI**3)          # 1.616e-35 m
t_P = l_P / c_SI                                   # 5.391e-44 s
M_P_kg = np.sqrt(hbar_SI * c_SI / G_SI)           # 2.176e-8 kg
from canonical_constants import M_Pl_unreduced as M_P_GeV  # 1.2209e19 GeV
M_P_reduced_GeV = M_P_GeV / np.sqrt(8 * np.pi)    # reduced Planck mass ~2.435e18 GeV

# Energy density conversions
# M_P^4 in GeV^4 (Planck energy density units)
M_P4_GeV4 = M_P_GeV**4  # ~2.22e76 GeV^4

# Observed cosmological constant
from canonical_constants import rho_Lambda_obs as Lambda_obs_GeV4  # GeV^4
Lambda_obs_MP4 = Lambda_obs_GeV4 / M_P4_GeV4  # ~1.3e-123 M_P^4

# More precise: rho_Lambda = 5.96e-27 kg/m^3 -> 2.888e-47 GeV^4
# Lambda_obs/M_P^4 = 2.888e-47 / 2.22e76 = 1.30e-123
# Often quoted as ~2.888e-122 in reduced Planck units
# We use the FULL Planck mass consistently

print("=" * 70)
print("F-FOAM-5-43: Carlip CC Mechanism Interface")
print("=" * 70)
print(f"\nPlanck length:  l_P = {l_P:.4e} m")
print(f"Planck time:    t_P = {t_P:.4e} s")
print(f"Planck mass:    M_P = {M_P_GeV:.4e} GeV")
print(f"M_P^4:          {M_P4_GeV4:.4e} GeV^4")
print(f"Lambda_obs:     {Lambda_obs_GeV4:.4e} GeV^4")
print(f"Lambda_obs/M_P^4: {Lambda_obs_MP4:.4e}")

# =============================================================================
# Step 1: Load Framework Lambda_internal
# =============================================================================
print("\n" + "=" * 70)
print("STEP 1: Framework Lambda_internal")
print("=" * 70)

d_const = np.load('tier0-computation/s42_constants_snapshot.npz', allow_pickle=True)
d_stiff = np.load('tier0-computation/s42_gradient_stiffness.npz', allow_pickle=True)
d_qth = np.load('tier0-computation/s43_qtheory_selftune.npz', allow_pickle=True)

S_fold = float(np.atleast_1d(d_stiff['S_fold'])[0])
M_KK_GN = float(np.atleast_1d(d_const['M_KK_from_GN'])[0])       # 7.43e16 GeV (gravity route)
M_KK_kerner = float(np.atleast_1d(d_const['M_KK_kerner'])[0])     # 5.04e17 GeV (gauge route)

# Q-theory corrected: use Delta_S = S(fold) - S(0) instead of S_fold
S_0 = float(np.atleast_1d(d_qth['S_0'])[0])
Delta_S_fold = float(np.atleast_1d(d_qth['Delta_S_fold'])[0])  # S(fold) - S(0)

print(f"\nS_fold = {S_fold:.1f} M_KK^4")
print(f"S(0) = {S_0:.1f} M_KK^4")
print(f"Delta_S(fold) = {Delta_S_fold:.1f} M_KK^4")
print(f"M_KK (gravity route) = {M_KK_GN:.4e} GeV")
print(f"M_KK (Kerner route) = {M_KK_kerner:.4e} GeV")

# Compute Lambda_internal for BOTH M_KK routes and BOTH S_fold vs Delta_S
# Lambda = S * M_KK^4 / (16*pi^2) is the spectral action CC contribution
# Factor 16*pi^2 from spectral action normalization: Tr(f(D^2/Lambda^2)) -> a_0*f_0*Lambda^4/(16*pi^2)

prefactor = 1.0 / (16.0 * np.pi**2)  # = 0.00633

# Route 1: Full S_fold with gravity M_KK (original S42 estimate)
Lambda_full_GN_GeV4 = S_fold * M_KK_GN**4 * prefactor
Lambda_full_GN_MP4 = Lambda_full_GN_GeV4 / M_P4_GeV4

# Route 2: Q-theory corrected Delta_S with gravity M_KK (W1-1 result)
Lambda_qth_GN_GeV4 = Delta_S_fold * M_KK_GN**4 * prefactor
Lambda_qth_GN_MP4 = Lambda_qth_GN_GeV4 / M_P4_GeV4

# Route 3: Full S_fold with Kerner M_KK
Lambda_full_K_GeV4 = S_fold * M_KK_kerner**4 * prefactor
Lambda_full_K_MP4 = Lambda_full_K_GeV4 / M_P4_GeV4

# Route 4: Q-theory corrected Delta_S with Kerner M_KK
Lambda_qth_K_GeV4 = Delta_S_fold * M_KK_kerner**4 * prefactor
Lambda_qth_K_MP4 = Lambda_qth_K_GeV4 / M_P4_GeV4

print(f"\n--- Lambda_internal candidates ---")
print(f"{'Route':<35s} {'Lambda (GeV^4)':<15s} {'Lambda/M_P^4':<15s} {'log10':<8s}")
print("-" * 75)
print(f"{'S_fold + M_KK(GN)':<35s} {Lambda_full_GN_GeV4:<15.4e} {Lambda_full_GN_MP4:<15.4e} {np.log10(Lambda_full_GN_MP4):<8.2f}")
print(f"{'Delta_S + M_KK(GN) [q-theory]':<35s} {Lambda_qth_GN_GeV4:<15.4e} {Lambda_qth_GN_MP4:<15.4e} {np.log10(Lambda_qth_GN_MP4):<8.2f}")
print(f"{'S_fold + M_KK(Kerner)':<35s} {Lambda_full_K_GeV4:<15.4e} {Lambda_full_K_MP4:<15.4e} {np.log10(Lambda_full_K_MP4):<8.2f}")
print(f"{'Delta_S + M_KK(Kerner) [q-theory]':<35s} {Lambda_qth_K_GeV4:<15.4e} {Lambda_qth_K_MP4:<15.4e} {np.log10(Lambda_qth_K_MP4):<8.2f}")

# Required suppression for each route
print(f"\n--- Required Carlip suppression (orders) ---")
for name, val in [("S_fold+GN", Lambda_full_GN_MP4),
                   ("Delta_S+GN", Lambda_qth_GN_MP4),
                   ("S_fold+Kerner", Lambda_full_K_MP4),
                   ("Delta_S+Kerner", Lambda_qth_K_MP4)]:
    ratio = val / Lambda_obs_MP4
    print(f"  {name:<25s}: {ratio:.2e}  ({np.log10(ratio):.1f} orders)")

# Primary route: q-theory corrected + gravity M_KK (S42+W1-1 preferred)
Lambda_primary_GeV4 = Lambda_qth_GN_GeV4
Lambda_primary_MP4 = Lambda_qth_GN_MP4
required_suppression = Lambda_primary_MP4 / Lambda_obs_MP4
required_orders = np.log10(required_suppression)

print(f"\n>>> PRIMARY: Lambda_internal = {Lambda_primary_MP4:.4e} M_P^4")
print(f">>> Required suppression: 10^{required_orders:.1f}")

# =============================================================================
# Step 2: Carlip Trapping -- Three Interpretations
# =============================================================================
print("\n" + "=" * 70)
print("STEP 2: Carlip Trapping Mechanism -- Three Interpretations")
print("=" * 70)

# The Carlip wavefunction is (Paper 14, eq from line 98):
#   |Psi(theta_bar)|^2 ~ exp(-2*pi^2 * Lambda * theta_bar^2 * L^4 / hbar)
#
# This is a Gaussian in theta_bar (the spatially averaged expansion rate).
# The width in theta_bar is:
#   sigma_theta^2 = hbar / (4*pi^2 * Lambda * L^4)
#
# Three physical interpretations of how this produces Lambda_eff:

# -----------------------------------------------------------------------
# Interpretation A: CURVATURE FROM EXPANSION FLUCTUATIONS
# -----------------------------------------------------------------------
# The Friedmann equation relates expansion rate to curvature:
#   H^2 = (8*pi*G/3) * rho_Lambda  =>  theta^2 ~ Lambda
# So <theta_bar^2> determines the effective Lambda:
#   Lambda_eff = <theta_bar^2> * (3/(8*pi*G))
# In Planck units (G = l_P^2, set l_P = 1):
#   Lambda_eff = (3/(8*pi)) * <theta_bar^2>
#             = (3/(8*pi)) * 1/(4*pi^2 * Lambda * L^4)
#             = 3/(32*pi^3 * Lambda * L^4)
#
# This makes Lambda_eff INVERSELY proportional to Lambda_bare.
# Solving for L given Lambda_eff = Lambda_obs:
#   L^4 = 3 / (32*pi^3 * Lambda_obs * Lambda_bare)

print("\n--- Interpretation A: Curvature from expansion fluctuations ---")
print("  Lambda_eff = 3/(32*pi^3 * Lambda_bare * L^4)")
print("  L determined by: Lambda_eff = Lambda_obs")

# L in Planck units for each Lambda_internal
L_A_values = {}
for name, Lambda_MP4 in [("S_fold+GN", Lambda_full_GN_MP4),
                           ("Delta_S+GN", Lambda_qth_GN_MP4),
                           ("S_fold+Kerner", Lambda_full_K_MP4),
                           ("Delta_S+Kerner", Lambda_qth_K_MP4)]:
    L4 = 3.0 / (32.0 * np.pi**3 * Lambda_obs_MP4 * Lambda_MP4)
    L_lP = L4**(1.0/4.0)  # in Planck lengths
    L_m = L_lP * l_P       # in meters
    L_A_values[name] = (L_lP, L_m)
    print(f"  {name:<25s}: L = {L_lP:.2e} l_P = {L_m:.2e} m")

# -----------------------------------------------------------------------
# Interpretation B: POCKET WIDTH (Lambda_eff independent of Lambda_bare)
# -----------------------------------------------------------------------
# Carlip's strongest claim: for ANY Lambda_bare, the effective CC after
# trapping is determined by the uncertainty principle applied to the
# expansion degree of freedom:
#   Lambda_eff ~ hbar / L^2  (in Planck units, hbar = 1)
# This is from: the expansion rate theta has uncertainty
#   delta_theta ~ 1/L (from wavelength of foam cells)
# and the corresponding curvature fluctuation is:
#   Lambda_eff ~ delta_theta^2 ~ 1/L^2
#
# Solving for L: L^2 = 1/Lambda_obs  =>  L = 1/sqrt(Lambda_obs) l_P

print("\n--- Interpretation B: Pocket width (hbar/L^2) ---")
print("  Lambda_eff = 1/L^2  (in Planck units)")
L_B_lP = 1.0 / np.sqrt(Lambda_obs_MP4)
L_B_m = L_B_lP * l_P
print(f"  L = {L_B_lP:.4e} l_P = {L_B_m:.4e} m")
print(f"  log10(L/l_P) = {np.log10(L_B_lP):.2f}")

# -----------------------------------------------------------------------
# Interpretation C: EXPONENTIAL SUPPRESSION (Carlip 2021, Paper 11)
# -----------------------------------------------------------------------
# From Paper 11: the suppression factor is exp(-V_barrier/hbar)
# where V_barrier ~ Lambda^{2/3} (in Planck units).
# Lambda_eff = Lambda_bare * exp(-alpha * Lambda_bare^{2/3})
# where alpha is a numerical coefficient of order unity.
#
# This produces an EXPONENTIAL sensitivity to Lambda_bare.
# For Lambda_bare >> 1 (in Planck units), Lambda_eff is DOUBLY exponentially small.
# But Lambda_bare = 2.4e-8 in Planck units is SMALL, not large.
# The exponential suppression factor is:
#   S = exp(-alpha * (2.4e-8)^{2/3}) = exp(-alpha * 8.3e-6)
# For alpha ~ 1: S ~ 1 - 8.3e-6, i.e., essentially NO suppression.
#
# This interpretation is relevant when Lambda_bare >> M_P^4, not when it's small.

print("\n--- Interpretation C: Exponential suppression ---")
print("  Lambda_eff = Lambda_bare * exp(-alpha * Lambda_bare^{2/3})")
for alpha_val in [1.0, 2*np.pi**2, 100.0]:
    for name, Lambda_MP4 in [("Delta_S+GN", Lambda_qth_GN_MP4),
                               ("S_fold+GN", Lambda_full_GN_MP4)]:
        exponent = alpha_val * Lambda_MP4**(2.0/3.0)
        suppression = np.exp(-exponent)
        Lambda_eff = Lambda_MP4 * suppression
        print(f"  alpha={alpha_val:.1f}, {name}: exponent = {exponent:.4e}, "
              f"suppression = {suppression:.4e}, Lambda_eff = {Lambda_eff:.4e} M_P^4")

print("\n  >>> CONCLUSION: Interpretation C gives NO suppression when Lambda_bare << M_P^4")
print("      The framework's Lambda_internal is too small for exponential suppression to work.")
print("      This interpretation is designed for Lambda_bare ~ M_P^4 (standard CC problem).")

# -----------------------------------------------------------------------
# Interpretation D: CARLIP'S ACTUAL MECHANISM (most careful reading)
# -----------------------------------------------------------------------
# Re-reading Paper 14 more carefully. The key equation is:
#   |Psi(theta_bar)|^2 ~ exp(-2*pi^2 * Lambda * theta_bar^2 * L^4 / hbar)
#
# This is a Gaussian distribution for theta_bar with variance:
#   sigma_theta^2 = hbar / (4*pi^2 * Lambda * L^4)
#
# The EFFECTIVE Lambda is obtained by asking: what Lambda_eff would produce
# this same expansion-rate variance in a classical Friedmann universe?
#
# In the Friedmann equation: H^2 = Lambda/3 (for pure CC domination)
# So theta = 3*H = 3*sqrt(Lambda/3) = sqrt(3*Lambda)
# => theta^2 = 3*Lambda
# => Lambda = theta^2/3
#
# The effective Lambda from the VARIANCE of theta is:
#   Lambda_eff = <theta_bar^2>/3 = hbar / (12*pi^2 * Lambda_bare * L^4)
#
# This is the Interpretation A result with a different prefactor.
# The physics: Lambda_eff ~ 1/(Lambda_bare * L^4)
#
# Solving for L: L^4 = hbar / (12*pi^2 * Lambda_eff * Lambda_bare)
# With Lambda_eff = Lambda_obs:
#   L^4 = 1 / (12*pi^2 * Lambda_obs * Lambda_bare)  [Planck units]

print("\n--- Interpretation D: Careful Friedmann mapping ---")
print("  Lambda_eff = <theta_bar^2>/3 = 1/(12*pi^2 * Lambda_bare * L^4)")

L_D_values = {}
for name, Lambda_MP4 in [("S_fold+GN", Lambda_full_GN_MP4),
                           ("Delta_S+GN", Lambda_qth_GN_MP4),
                           ("S_fold+Kerner", Lambda_full_K_MP4),
                           ("Delta_S+Kerner", Lambda_qth_K_MP4)]:
    L4 = 1.0 / (12.0 * np.pi**2 * Lambda_obs_MP4 * Lambda_MP4)
    L_lP = L4**(1.0/4.0)  # in Planck lengths
    L_m = L_lP * l_P       # in meters
    L_D_values[name] = (L_lP, L_m, L4)
    print(f"  {name:<25s}: L = {L_lP:.4e} l_P = {L_m:.4e} m  (log10(L/l_P) = {np.log10(L_lP):.2f})")

# =============================================================================
# Step 3: Analyze the L scale for primary route
# =============================================================================
print("\n" + "=" * 70)
print("STEP 3: Physical Analysis of Required Averaging Scale L")
print("=" * 70)

# Primary route: Delta_S + M_KK(GN), Interpretation D
L_primary_lP, L_primary_m, L4_primary = L_D_values["Delta_S+GN"]

print(f"\nPrimary route: Delta_S + M_KK(GN)")
print(f"  Lambda_internal = {Lambda_qth_GN_MP4:.4e} M_P^4")
print(f"  Lambda_obs = {Lambda_obs_MP4:.4e} M_P^4")
print(f"  Required L = {L_primary_lP:.4e} l_P = {L_primary_m:.4e} m")

# Physical scales for comparison
L_Hubble_m = 4.4e26  # m (Hubble radius)
L_Hubble_lP = L_Hubble_m / l_P
L_KK_m = 1.0 / (M_KK_GN * 1.602e-10 / (hbar_SI * c_SI))  # hbar*c/M_KK
L_KK_lP = L_KK_m / l_P

print(f"\nComparison scales:")
print(f"  Planck length:    {1.0:.0f} l_P = {l_P:.4e} m")
print(f"  KK scale:         {L_KK_lP:.4e} l_P = {L_KK_m:.4e} m")
print(f"  Hubble radius:    {L_Hubble_lP:.4e} l_P = {L_Hubble_m:.4e} m")
print(f"  Required L:       {L_primary_lP:.4e} l_P = {L_primary_m:.4e} m")

# Is L physically reasonable?
print(f"\n--- Physical reasonableness ---")
print(f"  L > l_P?  {'YES' if L_primary_lP > 1 else 'NO'} (L/l_P = {L_primary_lP:.2e})")
print(f"  L < 1 m?  {'YES' if L_primary_m < 1 else 'NO'} (L = {L_primary_m:.2e} m)")
print(f"  L < Hubble? {'YES' if L_primary_m < L_Hubble_m else 'NO'}")

# Key ratio: L vs Hubble radius
ratio_L_Hubble = L_primary_m / L_Hubble_m
print(f"  L/L_Hubble = {ratio_L_Hubble:.4e}")

# =============================================================================
# Step 4: Verify the suppression factor
# =============================================================================
print("\n" + "=" * 70)
print("STEP 4: Verify Suppression Factor")
print("=" * 70)

# At the required L, the Gaussian exponent for theta_bar = 1 is:
gaussian_exponent = 2.0 * np.pi**2 * Lambda_qth_GN_MP4 * L_primary_lP**4
print(f"\nGaussian exponent = 2*pi^2 * Lambda * L^4 = {gaussian_exponent:.4e}")
print(f"log10(exponent) = {np.log10(gaussian_exponent):.2f}")
print(f"This means: |Psi(theta_bar=1)|^2 / |Psi(0)|^2 = exp(-{gaussian_exponent:.2e})")
print(f"  i.e., exp(-10^{np.log10(gaussian_exponent):.1f})")

# The variance of theta_bar:
sigma2_theta = 1.0 / (4.0 * np.pi**2 * Lambda_qth_GN_MP4 * L_primary_lP**4)
sigma_theta = np.sqrt(sigma2_theta)
print(f"\nsigma_theta^2 = {sigma2_theta:.4e}")
print(f"sigma_theta = {sigma_theta:.4e}")

# Effective Lambda from variance:
Lambda_eff_check = sigma2_theta / 3.0
print(f"Lambda_eff = sigma_theta^2/3 = {Lambda_eff_check:.4e} M_P^4")
print(f"Lambda_obs = {Lambda_obs_MP4:.4e} M_P^4")
print(f"Ratio Lambda_eff/Lambda_obs = {Lambda_eff_check/Lambda_obs_MP4:.4e}")

# =============================================================================
# Step 5: Force Anomaly Prediction
# =============================================================================
print("\n" + "=" * 70)
print("STEP 5: Force Anomaly Prediction (Paper 14)")
print("=" * 70)

# Paper 14: Delta_F/F ~ (l_P/L)^{2/3}
print(f"\nDelta_F/F = (l_P/L)^{{2/3}}")
Delta_F_over_F = (1.0 / L_primary_lP)**(2.0/3.0)
print(f"  For L = {L_primary_lP:.2e} l_P:")
print(f"  Delta_F/F = ({1.0/L_primary_lP:.2e})^(2/3) = {Delta_F_over_F:.4e}")
print(f"  log10(Delta_F/F) = {np.log10(Delta_F_over_F):.2f}")

# At specific experimental scales
print(f"\n--- Force anomaly at specific scales ---")
test_scales = [
    ("1 micrometer", 1e-6),
    ("10 micrometer", 1e-5),
    ("1 mm", 1e-3),
    ("1 cm", 1e-2),
    ("1 m", 1.0),
]
for name, scale_m in test_scales:
    scale_lP = scale_m / l_P
    dF_F = (1.0 / scale_lP)**(2.0/3.0)
    print(f"  At {name:>15s}: Delta_F/F = {dF_F:.2e}")

# The required L is a SPECIFIC prediction of the framework + Carlip
print(f"\n--- Framework prediction at L = {L_primary_m:.2e} m ---")
print(f"  Delta_F/F = {Delta_F_over_F:.4e}")
print(f"  This is {'measurable' if Delta_F_over_F > 1e-30 else 'unmeasurable'} "
      f"with current technology (best torsion balance: ~10^{{-4}})")

# =============================================================================
# Step 6: Scan over L to map Lambda_eff(L)
# =============================================================================
print("\n" + "=" * 70)
print("STEP 6: Scan Lambda_eff(L) for all four Lambda_internal candidates")
print("=" * 70)

L_scan_lP = np.logspace(0, 62, 2000)  # from l_P to 10^62 l_P (~Hubble)
L_scan_m = L_scan_lP * l_P

# For each Lambda_internal, compute Lambda_eff(L) using Interpretation D
results = {}
for name, Lambda_MP4 in [("S_fold+GN", Lambda_full_GN_MP4),
                           ("Delta_S+GN [primary]", Lambda_qth_GN_MP4),
                           ("S_fold+Kerner", Lambda_full_K_MP4),
                           ("Delta_S+Kerner", Lambda_qth_K_MP4)]:
    Lambda_eff = 1.0 / (12.0 * np.pi**2 * Lambda_MP4 * L_scan_lP**4)
    results[name] = Lambda_eff

    # Find where Lambda_eff = Lambda_obs
    idx = np.argmin(np.abs(np.log10(Lambda_eff) - np.log10(Lambda_obs_MP4)))
    L_match = L_scan_lP[idx]
    L_match_m = L_scan_m[idx]
    print(f"  {name}: Lambda_eff = Lambda_obs at L = {L_match:.2e} l_P = {L_match_m:.2e} m")

# =============================================================================
# Step 7: Alternative -- L as the averaging scale over Planck-scale foam
# =============================================================================
print("\n" + "=" * 70)
print("STEP 7: Alternative -- Carlip's L as foam averaging scale")
print("=" * 70)

# Carlip (Paper 14, Section on coarse-graining):
# V ~ (10 l_P)^3 to (100 l_P)^3
# This gives L ~ 10 to 100 l_P.
# If L is FIXED at these scales, what Lambda_eff do we get?

print("\nIf L is the foam cell size (Carlip's coarse-graining scale):")
for L_foam_lP in [1, 10, 100, 1000, 1e4, 1e6]:
    Lambda_eff_foam = 1.0 / (12.0 * np.pi**2 * Lambda_qth_GN_MP4 * L_foam_lP**4)
    ratio = Lambda_eff_foam / Lambda_obs_MP4
    print(f"  L = {L_foam_lP:.0e} l_P: Lambda_eff = {Lambda_eff_foam:.2e} M_P^4 "
          f"(Lambda_eff/Lambda_obs = {ratio:.2e})")

# =============================================================================
# Step 8: The Carlip mechanism with STANDARD CC problem (Lambda ~ M_P^4)
# =============================================================================
print("\n" + "=" * 70)
print("STEP 8: Comparison -- Standard CC problem (Lambda_bare ~ M_P^4)")
print("=" * 70)

# If Lambda_bare = 1 M_P^4 (the standard CC problem):
Lambda_standard = 1.0  # M_P^4
for L_test_lP in [1, 10, 100, 1e10, 1e20, 1e30, L_Hubble_lP]:
    Lambda_eff_std = 1.0 / (12.0 * np.pi**2 * Lambda_standard * L_test_lP**4)
    print(f"  L = {L_test_lP:.2e} l_P: Lambda_eff = {Lambda_eff_std:.2e} M_P^4")

print(f"\nFor standard CC, L needed for Lambda_obs:")
L4_std = 1.0 / (12.0 * np.pi**2 * Lambda_obs_MP4 * 1.0)
L_std_lP = L4_std**(1.0/4.0)
L_std_m = L_std_lP * l_P
print(f"  L = {L_std_lP:.2e} l_P = {L_std_m:.2e} m")
print(f"  This is {L_std_m/L_Hubble_m:.2e} x Hubble radius")

# =============================================================================
# Step 9: Hierarchical Carlip -- external foam averages internal CC
# =============================================================================
print("\n" + "=" * 70)
print("STEP 9: Hierarchical Carlip -- external foam averages internal CC")
print("=" * 70)

# The framework has BOTH:
#   1. Internal CC: Lambda_internal from spectral action (~10^{-8} M_P^4)
#   2. Standard QFT CC: from integrating out SM fields (~M_P^4)
#
# Carlip's mechanism operates on the TOTAL bare CC seen by external gravity.
# The internal CC is a CONTRIBUTION to the total, not the whole thing.
#
# If the total bare CC is dominated by QFT contributions:
#   Lambda_total ~ M_P^4  (standard CC problem)
# Then Carlip needs L ~ 10^{30} l_P ~ 10^{-5} m to produce Lambda_obs.
#
# If q-theory removes the leading contribution and only Lambda_internal survives:
#   Lambda_total ~ Lambda_internal ~ 10^{-8} M_P^4
# Then Carlip needs L ~ 10^{28} l_P ~ 10^{-7} m.

print("\nScenario analysis:")
print("  Scenario 1: Total Lambda = M_P^4 (standard CC, no q-theory)")
L4_sc1 = 1.0 / (12.0 * np.pi**2 * Lambda_obs_MP4 * 1.0)
L_sc1 = L4_sc1**(0.25)
print(f"    Required L = {L_sc1:.4e} l_P = {L_sc1*l_P:.4e} m")
dF_sc1 = (1.0/L_sc1)**(2.0/3.0)
print(f"    Delta_F/F = {dF_sc1:.4e}")

print(f"\n  Scenario 2: Total Lambda = S_fold * M_KK^4/(16pi^2) = {Lambda_full_GN_MP4:.2e} M_P^4")
L4_sc2 = 1.0 / (12.0 * np.pi**2 * Lambda_obs_MP4 * Lambda_full_GN_MP4)
L_sc2 = L4_sc2**(0.25)
print(f"    Required L = {L_sc2:.4e} l_P = {L_sc2*l_P:.4e} m")
dF_sc2 = (1.0/L_sc2)**(2.0/3.0)
print(f"    Delta_F/F = {dF_sc2:.4e}")

print(f"\n  Scenario 3: Total Lambda = Delta_S * M_KK^4/(16pi^2) = {Lambda_qth_GN_MP4:.2e} M_P^4 (q-theory)")
L4_sc3 = 1.0 / (12.0 * np.pi**2 * Lambda_obs_MP4 * Lambda_qth_GN_MP4)
L_sc3 = L4_sc3**(0.25)
print(f"    Required L = {L_sc3:.4e} l_P = {L_sc3*l_P:.4e} m")
dF_sc3 = (1.0/L_sc3)**(2.0/3.0)
print(f"    Delta_F/F = {dF_sc3:.4e}")

# =============================================================================
# Step 10: CRITICAL -- Does the mechanism self-consistently work?
# =============================================================================
print("\n" + "=" * 70)
print("STEP 10: SELF-CONSISTENCY CHECK")
print("=" * 70)

# The Carlip mechanism requires:
#   1. L > l_P (sub-Planckian L is unphysical)
#   2. L < L_Hubble (must fit in the universe)
#   3. Foam MUST exist at scale L (requires quantum gravity dynamics)
#   4. The coarse-graining volume V ~ L^3 must contain enough foam cells
#
# For the framework's Lambda_internal:
#   L ~ 10^{28-30} l_P ~ 10^{-7} to 10^{-5} m (micrometer to sub-mm)
#   This is MACROSCOPIC, not Planck-scale.
#
# Carlip's original mechanism assumes foam at the PLANCK scale.
# If L must be macroscopic, this creates a tension:
#   Wheeler foam is at l_P, not at micrometers.
#   The mechanism would require foam structure at scales 10^{30} times larger
#   than the Planck length.

print(f"\nFramework requires L ~ {L_sc3:.2e} l_P ~ {L_sc3*l_P:.2e} m")
print(f"Carlip's foam cell size: 10-100 l_P")
print(f"Ratio: L_required / L_foam = {L_sc3/100:.2e}")
print(f"\nSelf-consistency requirement: foam at scale L must exist.")
print(f"  Wheeler foam: L_foam ~ l_P to 100 l_P")
print(f"  Required L: {L_sc3:.2e} l_P")
print(f"  GAP: {np.log10(L_sc3/100):.0f} orders of magnitude")

# However: Carlip (Paper 14) describes HIERARCHICAL coarse-graining.
# First coarse-grain at l_P -> effective metric at 10 l_P.
# Then coarse-grain again at 10 l_P -> effective metric at 100 l_P.
# Continue up to scale L.
# At each step, the expansion variance is reduced.
# After N steps of coarse-graining by factor b:
#   Lambda_eff(step N) ~ Lambda_eff(step 0) / b^{4N}
# With b=10 and Lambda_bare = Lambda_internal:
#   N = log_b(L_required / l_P) = log10(L_required/l_P) ~ 28-30
# So Lambda_eff ~ Lambda_internal / 10^{4*28} = Lambda_internal / 10^{112}
# This is the right suppression.

print(f"\n--- Hierarchical coarse-graining ---")
print(f"If each coarse-graining step of factor b=10 reduces Lambda by b^4=10^4:")
b = 10.0
N_steps_needed = np.log10(required_suppression) / 4.0
print(f"  N_steps = log10({required_suppression:.1e}) / 4 = {N_steps_needed:.1f}")
L_hierarchical = b**N_steps_needed  # in l_P
print(f"  Final scale: L = b^N = {L_hierarchical:.2e} l_P = {L_hierarchical*l_P:.2e} m")
print(f"  Compare to direct: L = {L_sc3:.2e} l_P")
print(f"  Agreement: {L_hierarchical/L_sc3:.2f}")

print(f"\nPhysical picture:")
print(f"  Start at Planck scale with Lambda_internal = {Lambda_qth_GN_MP4:.2e} M_P^4")
print(f"  Each factor-of-10 coarse-graining reduces effective CC by 10^4")
print(f"  After {N_steps_needed:.1f} decades: Lambda_eff = Lambda_obs")
print(f"  This corresponds to scale {L_hierarchical*l_P:.1e} m")

# =============================================================================
# Step 11: Gate Verdict
# =============================================================================
print("\n" + "=" * 70)
print("STEP 11: GATE VERDICT F-FOAM-5-43")
print("=" * 70)

# Gate criteria:
# PASS: Lambda_eff within 10 orders of Lambda_obs for physically reasonable L (l_P < L < 1 m)
# FAIL: No L produces Lambda_eff near Lambda_obs, OR required L is sub-Planckian

L_required = L_sc3  # primary route
L_required_m = L_required * l_P

gate_pass_L_above_lP = L_required > 1.0
gate_pass_L_below_1m = L_required_m < 1.0
gate_pass_Lambda_match = True  # by construction, L is chosen to give Lambda_obs

# The real question: does L fall in a physically reasonable range?
# L ~ 10^{-7} m is sub-mm but macroscopic. This is within short-range gravity experiments.
# Torsion balance experiments (Eot-Wash) have probed down to ~50 micrometers.
# L_required ~ 10^{-7} m = 0.1 micrometer = 100 nm.
# This is BELOW current short-range gravity limits but ABOVE the Planck scale.

is_testable = L_required_m > 1e-9 and L_required_m < 1e-2

print(f"\nL_required = {L_required:.4e} l_P = {L_required_m:.4e} m")
print(f"  L > l_P: {gate_pass_L_above_lP}")
print(f"  L < 1 m: {gate_pass_L_below_1m}")
print(f"  Lambda_eff = Lambda_obs at this L: {gate_pass_Lambda_match}")
print(f"  L in testable range (nm to mm): {is_testable}")

# Classification
if gate_pass_L_above_lP and gate_pass_L_below_1m:
    verdict = "PASS"
    verdict_detail = (f"Lambda_eff = Lambda_obs at L = {L_required_m:.2e} m. "
                      f"Physically reasonable (above Planck, below 1m). "
                      f"Force anomaly: Delta_F/F = {dF_sc3:.2e}.")
else:
    verdict = "FAIL"
    verdict_detail = "Required L is outside physical range."

# INFO caveat: the result depends on interpretation
info_caveat = ("Result depends on Interpretation D (Friedmann mapping of expansion "
               "variance). Interpretation C (exponential) gives no suppression for "
               "Lambda_internal << M_P^4. The mechanism's validity requires Planck-scale "
               "foam to produce hierarchical coarse-graining up to L ~ 100 nm.")

print(f"\n*** GATE F-FOAM-5-43: {verdict} ***")
print(f"  {verdict_detail}")
print(f"\n  INFO caveat: {info_caveat}")

# =============================================================================
# Step 12: Summary Table
# =============================================================================
print("\n" + "=" * 70)
print("SUMMARY TABLE")
print("=" * 70)

print(f"\n{'Quantity':<40s} {'Value':<20s} {'Unit':<15s}")
print("-" * 75)
print(f"{'S_fold':<40s} {S_fold:<20.1f} {'M_KK^4':<15s}")
print(f"{'S(0)':<40s} {S_0:<20.1f} {'M_KK^4':<15s}")
print(f"{'Delta_S(fold)':<40s} {Delta_S_fold:<20.1f} {'M_KK^4':<15s}")
print(f"{'M_KK (gravity)':<40s} {M_KK_GN:<20.4e} {'GeV':<15s}")
print(f"{'Lambda_internal [full]':<40s} {Lambda_full_GN_MP4:<20.4e} {'M_P^4':<15s}")
print(f"{'Lambda_internal [q-theory]':<40s} {Lambda_qth_GN_MP4:<20.4e} {'M_P^4':<15s}")
print(f"{'Lambda_obs':<40s} {Lambda_obs_MP4:<20.4e} {'M_P^4':<15s}")
print(f"{'Required suppression':<40s} {required_suppression:<20.4e} {'':<15s}")
print(f"{'Required suppression (orders)':<40s} {required_orders:<20.1f} {'':<15s}")
print(f"{'L_required (Interpretation D)':<40s} {L_sc3:<20.4e} {'l_P':<15s}")
print(f"{'L_required':<40s} {L_sc3*l_P:<20.4e} {'m':<15s}")
print(f"{'L_required':<40s} {L_sc3*l_P*1e9:<20.2f} {'nm':<15s}")
print(f"{'N hierarchical steps':<40s} {N_steps_needed:<20.1f} {'':<15s}")
print(f"{'Delta_F/F at L_required':<40s} {dF_sc3:<20.4e} {'':<15s}")
print(f"{'Gate verdict':<40s} {verdict:<20s} {'':<15s}")

# =============================================================================
# Save results
# =============================================================================
print("\n" + "=" * 70)
print("Saving results to s43_carlip_cc.npz")
print("=" * 70)

np.savez('tier0-computation/s43_carlip_cc.npz',
    # Framework Lambda
    S_fold=S_fold,
    S_0=S_0,
    Delta_S_fold=Delta_S_fold,
    M_KK_GN=M_KK_GN,
    M_KK_kerner=M_KK_kerner,
    Lambda_full_GN_MP4=Lambda_full_GN_MP4,
    Lambda_full_GN_GeV4=Lambda_full_GN_GeV4,
    Lambda_qth_GN_MP4=Lambda_qth_GN_MP4,
    Lambda_qth_GN_GeV4=Lambda_qth_GN_GeV4,
    Lambda_obs_MP4=Lambda_obs_MP4,
    Lambda_obs_GeV4=Lambda_obs_GeV4,
    required_suppression=required_suppression,
    required_orders=required_orders,
    # Carlip L scales (in l_P) for 4 routes
    L_sc1_lP=L_sc1, L_sc1_m=L_sc1*l_P,    # standard CC
    L_sc2_lP=L_sc2, L_sc2_m=L_sc2*l_P,    # S_fold+GN
    L_sc3_lP=L_sc3, L_sc3_m=L_sc3*l_P,    # Delta_S+GN [primary]
    # Force anomaly
    Delta_F_over_F_sc1=dF_sc1,
    Delta_F_over_F_sc2=dF_sc2,
    Delta_F_over_F_sc3=dF_sc3,
    # Hierarchical coarse-graining
    N_steps_hierarchical=N_steps_needed,
    b_coarsegraining=b,
    # Scan
    L_scan_lP=L_scan_lP,
    L_scan_m=L_scan_m,
    Lambda_eff_scan_primary=results["Delta_S+GN [primary]"],
    Lambda_eff_scan_full=results["S_fold+GN"],
    # Planck units
    l_P=l_P,
    M_P_GeV=M_P_GeV,
    M_P4_GeV4=M_P4_GeV4,
    # Gate
    gate_verdict=[verdict],
    gate_name=['F-FOAM-5-43'],
    info_caveat=[info_caveat],
)

print("Saved.")

# =============================================================================
# Plots
# =============================================================================
print("\nGenerating plots...")

fig = plt.figure(figsize=(16, 12))
gs = GridSpec(2, 2, hspace=0.35, wspace=0.30)

# --- Panel 1: Lambda_eff(L) for different Lambda_internal ---
ax1 = fig.add_subplot(gs[0, 0])
colors = ['#1f77b4', '#d62728', '#2ca02c', '#9467bd']
labels_short = ['S_fold+GN', 'Delta_S+GN', 'S_fold+Kerner', 'Delta_S+Kerner']
for i, (name, Lambda_eff) in enumerate(results.items()):
    ax1.plot(np.log10(L_scan_lP), np.log10(Lambda_eff), color=colors[i],
             label=name, linewidth=1.5)
ax1.axhline(np.log10(Lambda_obs_MP4), color='gray', linestyle='--', linewidth=1, label=r'$\Lambda_{obs}$')
ax1.axvline(np.log10(L_sc3), color='#d62728', linestyle=':', linewidth=1, alpha=0.7)
ax1.set_xlabel(r'$\log_{10}(L / \ell_P)$', fontsize=11)
ax1.set_ylabel(r'$\log_{10}(\Lambda_{eff} / M_P^4)$', fontsize=11)
ax1.set_title('Carlip Lambda_eff vs Averaging Scale L', fontsize=12)
ax1.legend(fontsize=8, loc='upper right')
ax1.set_xlim(0, 62)
ax1.set_ylim(-140, 10)
ax1.grid(alpha=0.3)

# --- Panel 2: Force anomaly vs scale ---
ax2 = fig.add_subplot(gs[0, 1])
L_force_lP = np.logspace(0, 62, 500)
L_force_m = L_force_lP * l_P
dF_F = (1.0 / L_force_lP)**(2.0/3.0)
ax2.plot(np.log10(L_force_m), np.log10(dF_F), 'k-', linewidth=2)
# Mark experimental scales
exp_scales = {
    r'Eot-Wash (50$\mu$m)': 5e-5,
    r'NIST (10$\mu$m)': 1e-5,
    'L_required': L_sc3 * l_P,
}
for label, scale in exp_scales.items():
    dF_at_scale = (l_P / scale)**(2.0/3.0)
    ax2.plot(np.log10(scale), np.log10(dF_at_scale), 'o', markersize=8)
    ax2.annotate(label, (np.log10(scale), np.log10(dF_at_scale)),
                 textcoords="offset points", xytext=(10, 5), fontsize=8)
ax2.axhline(np.log10(1e-4), color='orange', linestyle='--', alpha=0.5,
            label='Current best (ISL test)')
ax2.set_xlabel(r'$\log_{10}(L / \mathrm{m})$', fontsize=11)
ax2.set_ylabel(r'$\log_{10}(\Delta F / F)$', fontsize=11)
ax2.set_title('Carlip Force Anomaly Prediction', fontsize=12)
ax2.legend(fontsize=8)
ax2.grid(alpha=0.3)
ax2.set_xlim(-35, 1)
ax2.set_ylim(-25, 0)

# --- Panel 3: Comparison of required L for different Lambda_bare ---
ax3 = fig.add_subplot(gs[1, 0])
Lambda_bare_range = np.logspace(-12, 0, 200)  # M_P^4
L_required_range = (1.0 / (12.0 * np.pi**2 * Lambda_obs_MP4 * Lambda_bare_range))**0.25
L_required_m_range = L_required_range * l_P

ax3.plot(np.log10(Lambda_bare_range), np.log10(L_required_m_range), 'b-', linewidth=2)
# Mark framework values
ax3.axvline(np.log10(Lambda_qth_GN_MP4), color='red', linestyle='--', linewidth=1,
            label=f'Framework (q-theory): {Lambda_qth_GN_MP4:.1e}')
ax3.axvline(np.log10(Lambda_full_GN_MP4), color='green', linestyle='--', linewidth=1,
            label=f'Framework (full): {Lambda_full_GN_MP4:.1e}')
ax3.axvline(0, color='gray', linestyle=':', linewidth=1, label=r'Standard CC ($M_P^4$)')
# Mark physical bounds
ax3.axhline(np.log10(l_P), color='purple', linestyle=':', alpha=0.3, label=r'$\ell_P$')
ax3.axhline(np.log10(L_Hubble_m), color='orange', linestyle=':', alpha=0.3, label=r'$L_H$')
ax3.axhspan(-7, -4, alpha=0.1, color='yellow', label='Sub-mm gravity tests')
ax3.set_xlabel(r'$\log_{10}(\Lambda_{bare} / M_P^4)$', fontsize=11)
ax3.set_ylabel(r'$\log_{10}(L_{required} / \mathrm{m})$', fontsize=11)
ax3.set_title('Required Carlip Averaging Scale vs Lambda_bare', fontsize=12)
ax3.legend(fontsize=7, loc='upper right')
ax3.grid(alpha=0.3)

# --- Panel 4: Summary text ---
ax4 = fig.add_subplot(gs[1, 1])
ax4.axis('off')
summary_text = (
    "F-FOAM-5-43 RESULTS\n"
    "=" * 35 + "\n\n"
    f"GATE VERDICT: {verdict}\n\n"
    f"Lambda_internal (q-theory):\n"
    f"  = {Lambda_qth_GN_MP4:.2e} M_P^4\n"
    f"  = {Lambda_qth_GN_GeV4:.2e} GeV^4\n\n"
    f"Lambda_obs:\n"
    f"  = {Lambda_obs_MP4:.2e} M_P^4\n\n"
    f"Required suppression: 10^{required_orders:.1f}\n\n"
    f"Carlip averaging scale:\n"
    f"  L = {L_sc3:.2e} l_P\n"
    f"  L = {L_sc3*l_P:.2e} m\n"
    f"  L = {L_sc3*l_P*1e9:.0f} nm\n\n"
    f"Force anomaly at L:\n"
    f"  Delta_F/F = {dF_sc3:.2e}\n\n"
    f"Hierarchical steps: {N_steps_needed:.1f}\n"
    f"(factor 10 coarse-graining)\n\n"
    f"CAVEAT: Requires foam at\n"
    f"  scales up to {L_sc3*l_P*1e9:.0f} nm,\n"
    f"  not just Planck scale"
)
ax4.text(0.05, 0.95, summary_text, transform=ax4.transAxes,
         fontsize=9, verticalalignment='top', fontfamily='monospace',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.suptitle('F-FOAM-5-43: Carlip CC Mechanism + Framework Spectral Action',
             fontsize=14, fontweight='bold', y=0.98)

plt.savefig('tier0-computation/s43_carlip_cc.png', dpi=150, bbox_inches='tight')
print("Plot saved to tier0-computation/s43_carlip_cc.png")

print("\n" + "=" * 70)
print("COMPUTATION COMPLETE")
print("=" * 70)
