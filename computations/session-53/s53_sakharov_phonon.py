#!/usr/bin/env python3
"""
SAKHAROV-PHONON-53 — Emergent G_N from GL 6-Branch Phonon Spectrum
=================================================================

Sakharov (1967) induced gravity: G_N^{-1} from one-loop polarization of
quantum fields on curved spacetime. Volovik (1994, 2003) showed this is
realized in superfluid 3He-A: 1/G_eff ~ N(E_F) x p_F^2.

This computation:
1. Loads the 6-branch GL phonon spectrum from S52 (GL-JOSEPHSON-52 PASS)
2. Computes the Sakharov integral for each branch
3. Includes the 32-cell tessellation factor (192 total modes)
4. Compares to observed G_N and to the S44/S45 Dirac-tower Sakharov result

Gate: SAKHAROV-PHONON-53 (INFO)

Author: volovik-superfluid-universe-theorist
Session: S53
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from canonical_constants import (
    M_KK, M_KK_gravity, M_Pl_reduced, M_Pl_unreduced,
    G_N, c_light, hbar_SI,
    Vol_SU3_Haar, N_cells,
    c_Gold, omega_L1, omega_L2, omega_H1, omega_H2, omega_H3,
    a0_fold, a2_fold, a4_fold,
    PI
)

# =============================================================================
# STEP 0: Load GL-Josephson data
# =============================================================================
data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         "s52_gl_josephson.npz")
d = np.load(data_path, allow_pickle=True)

K_array = d['K_array']         # shape (51,), in M_KK^{-1} units
K_BZ = float(d['K_BZ'])        # Brillouin zone boundary
omega_branches = d['omega_branches']  # shape (51, 6), omega in M_KK units
branch_labels = d['branch_labels']    # ['Goldstone', 'Leggett-1', ...]
c_eff_arr = d['c_eff']               # effective speeds (6,)
Delta_0 = d['Delta_0']               # gap parameters (3,)

N_K = len(K_array)
N_branches = omega_branches.shape[1]

print("=" * 72)
print("SAKHAROV-PHONON-53: Emergent G_N from GL 6-Branch Phonon Spectrum")
print("=" * 72)
print()

# =============================================================================
# STEP 1: Branch dispersion summary
# =============================================================================
print("--- STEP 1: GL Phonon Branch Summary ---")
print(f"  K_BZ = {K_BZ:.6f} M_KK^{{-1}}")
print(f"  N_K points = {N_K}")
print(f"  N_cells = {N_cells}")
print(f"  Total modes = {N_cells} x {N_branches} = {N_cells * N_branches}")
print()

# Masses (gaps at K=0) and speeds
masses_K0 = omega_branches[0, :]  # omega(K=0) for each branch
print(f"  {'Branch':<12} {'omega(K=0) [M_KK]':>18} {'c_eff [M_KK]':>14} {'Type':>10}")
print(f"  {'-'*12} {'-'*18} {'-'*14} {'-'*10}")
for i in range(N_branches):
    btype = "Goldstone" if masses_K0[i] < 1e-4 else "Gapped"
    print(f"  {branch_labels[i]:<12} {masses_K0[i]:>18.6f} {c_eff_arr[i]:>14.6f} {btype:>10}")
print()

# =============================================================================
# STEP 2: Sakharov integral per branch
# =============================================================================
# Sakharov formula (Volovik 2003, Ch. 10; Sakharov 1967):
#
#   1/(16*pi*G_N) = (1/48*pi^2) * sum_i integral_0^Lambda dk k^2 / omega_i(k)
#
# Equivalently:
#   G_N^{-1} = (16*pi) / (48*pi^2) * sum_i integral = (1/(3*pi)) * sum_i I_i
#
# For a gapped branch with omega = sqrt(m^2 + c^2 k^2):
#   I_i = integral_0^Lambda dk k^2 / sqrt(m_i^2 + c_i^2 k^2)
#       = (1/c_i^3) * integral_0^{c_i*Lambda} dx x^2 / sqrt((m_i/c_i)^2 + x^2)  [x = c_i*k]
#
# For Goldstone (m=0, omega = c*k):
#   I_Gold = integral_0^Lambda dk k^2 / (c*k) = Lambda^2 / (2*c)
#
# For gapped branch (general):
#   I_gap = (1/(2c^2)) * [Lambda*sqrt(Lambda^2 + (m/c)^2) - (m/c)^2 * arcsinh(c*Lambda/m)]
#
# All in M_KK units. Lambda = K_BZ for phonon modes.

print("--- STEP 2: Sakharov Integral Per Branch ---")
print()

# Use Lambda = K_BZ (phonon Brillouin zone cutoff)
Lambda_phonon = K_BZ

def sakharov_integral_goldstone(c, Lambda):
    """Integral_0^Lambda dk k^2 / (c*k) = Lambda^2 / (2*c)"""
    return Lambda**2 / (2.0 * c)

def sakharov_integral_gapped(m, c, Lambda):
    """Integral_0^Lambda dk k^2 / sqrt(m^2 + c^2*k^2)

    Analytic: (1/(2c^2)) * [Lambda*sqrt(c^2*Lambda^2 + m^2)
              - (m^2/c) * arcsinh(c*Lambda/m)]
    """
    cL = c * Lambda
    if m < 1e-10:
        return sakharov_integral_goldstone(c, Lambda)
    arg = cL / m
    term1 = Lambda * np.sqrt(cL**2 + m**2)
    term2 = (m**2 / c) * np.arcsinh(arg)
    return (1.0 / (2.0 * c**2)) * (term1 - term2)

def sakharov_integral_numerical(K_arr, omega_arr):
    """Numerical integral using trapezoidal rule on actual dispersion data."""
    integrand = K_arr**2 / omega_arr
    # Handle K=0 for Goldstone (0/0 -> 0 by L'Hopital: k/c -> 0)
    integrand = np.where(np.isfinite(integrand), integrand, 0.0)
    return np.trapezoid(integrand, K_arr)

# Compute both analytic and numerical for each branch
I_analytic = np.zeros(N_branches)
I_numerical = np.zeros(N_branches)

for i in range(N_branches):
    m_i = masses_K0[i]
    c_i = c_eff_arr[i]

    # Analytic
    if m_i < 1e-4:  # Goldstone
        I_analytic[i] = sakharov_integral_goldstone(c_i, Lambda_phonon)
    else:
        I_analytic[i] = sakharov_integral_gapped(m_i, c_i, Lambda_phonon)

    # Numerical from actual dispersion
    I_numerical[i] = sakharov_integral_numerical(K_array, omega_branches[:, i])

print(f"  Lambda_phonon = K_BZ = {Lambda_phonon:.6f} M_KK^{{-1}}")
print()
print(f"  {'Branch':<12} {'I_analytic':>14} {'I_numerical':>14} {'Ratio':>10}")
print(f"  {'-'*12} {'-'*14} {'-'*14} {'-'*10}")
for i in range(N_branches):
    ratio = I_analytic[i] / I_numerical[i] if I_numerical[i] > 0 else float('inf')
    print(f"  {branch_labels[i]:<12} {I_analytic[i]:>14.6f} {I_numerical[i]:>14.6f} {ratio:>10.4f}")

I_total_1cell_analytic = np.sum(I_analytic)
I_total_1cell_numerical = np.sum(I_numerical)
print()
print(f"  Sum (1 cell, analytic):  {I_total_1cell_analytic:.6f}")
print(f"  Sum (1 cell, numerical): {I_total_1cell_numerical:.6f}")
print()

# =============================================================================
# STEP 3: G_N from Sakharov with tessellation
# =============================================================================
# Standard Sakharov:
#   1/(16*pi*G) = (1/(48*pi^2)) * N_cells * sum_i I_i
#
# Therefore:
#   G_Sak = 48*pi^2 / (16*pi * N_cells * sum_i I_i)
#         = 3*pi / (N_cells * sum_i I_i)
#
# All in M_KK units: G_Sak has units M_KK^{-2}

print("--- STEP 3: Sakharov G_N from Phonon Modes ---")
print()

N_modes_total = N_cells * N_branches
I_total_analytic = N_cells * I_total_1cell_analytic
I_total_numerical = N_cells * I_total_1cell_numerical

# 1/(16*pi*G) in M_KK^2
inv_16piG_analytic = I_total_analytic / (48 * PI**2)
inv_16piG_numerical = I_total_numerical / (48 * PI**2)

# G_Sak in M_KK^{-2}
G_Sak_analytic = 1.0 / (16 * PI * inv_16piG_analytic)
G_Sak_numerical = 1.0 / (16 * PI * inv_16piG_numerical)

# Convert to M_Pl^{-2} for comparison
# G_N = 1/(8*pi*M_Pl_reduced^2) in natural units
# G_obs in M_KK^{-2}: G_obs = 1/(8*pi*M_Pl_reduced^2) * M_KK^2 ...
# More directly: M_Pl_eff from Sakharov
# 1/(16*pi*G) = M_Pl_eff^2 / 2  (reduced Planck mass convention)
# So M_Pl_eff = sqrt(2 * inv_16piG) in M_KK units

M_Pl_eff_analytic = np.sqrt(2 * inv_16piG_analytic)  # in M_KK
M_Pl_eff_numerical = np.sqrt(2 * inv_16piG_numerical)

# In GeV
M_Pl_eff_GeV_analytic = M_Pl_eff_analytic * M_KK  # GeV
M_Pl_eff_GeV_numerical = M_Pl_eff_numerical * M_KK

# Observed M_Pl_reduced
M_Pl_obs = M_Pl_reduced  # 2.435e18 GeV

# Ratio
ratio_MPl_analytic = M_Pl_eff_GeV_analytic / M_Pl_obs
ratio_MPl_numerical = M_Pl_eff_GeV_numerical / M_Pl_obs

# G_Sak / G_obs
# G ~ 1/M_Pl^2, so G_Sak/G_obs = (M_Pl_obs/M_Pl_eff)^2
ratio_G_analytic = (M_Pl_obs / M_Pl_eff_GeV_analytic)**2
ratio_G_numerical = (M_Pl_obs / M_Pl_eff_GeV_numerical)**2

print(f"  N_cells = {N_cells}")
print(f"  N_modes_total = {N_modes_total}")
print(f"  Lambda_phonon = K_BZ = {Lambda_phonon:.6f} M_KK^{{-1}}")
print()
print(f"  ANALYTIC dispersions:")
print(f"    1/(16*pi*G_Sak) = {inv_16piG_analytic:.6e} M_KK^2")
print(f"    M_Pl_eff = {M_Pl_eff_analytic:.6e} M_KK = {M_Pl_eff_GeV_analytic:.4e} GeV")
print(f"    M_Pl_eff / M_Pl_obs = {ratio_MPl_analytic:.6e}")
print(f"    G_Sak / G_obs = {ratio_G_analytic:.6e}")
print(f"    |log10(G_Sak/G_obs)| = {abs(np.log10(ratio_G_analytic)):.4f}")
print()
print(f"  NUMERICAL dispersions:")
print(f"    1/(16*pi*G_Sak) = {inv_16piG_numerical:.6e} M_KK^2")
print(f"    M_Pl_eff = {M_Pl_eff_numerical:.6e} M_KK = {M_Pl_eff_GeV_numerical:.4e} GeV")
print(f"    M_Pl_eff / M_Pl_obs = {ratio_MPl_numerical:.6e}")
print(f"    G_Sak / G_obs = {ratio_G_numerical:.6e}")
print(f"    |log10(G_Sak/G_obs)| = {abs(np.log10(ratio_G_numerical)):.4f}")
print()

# =============================================================================
# STEP 4: Volovik quick estimate comparison
# =============================================================================
# Volovik (2003) Ch 10: G_N^{-1} ~ N_species * Lambda^2 / (48*pi)
# With N = 192, Lambda = K_BZ:
#   1/(16*pi*G) = N * Lambda^2 / (48*pi^2)
# (note: need to be careful with 16*pi vs normalization)

print("--- STEP 4: Volovik Quick Estimate ---")
print()

# Quick estimate: 1/(16*pi*G) = N_modes * Lambda^2 / (48*pi^2)
# This assumes all modes are massless (Goldstone-like) with c=1
inv_16piG_volovik = N_modes_total * Lambda_phonon**2 / (48 * PI**2)
M_Pl_eff_volovik = np.sqrt(2 * inv_16piG_volovik)
M_Pl_eff_volovik_GeV = M_Pl_eff_volovik * M_KK
ratio_G_volovik = (M_Pl_obs / M_Pl_eff_volovik_GeV)**2

print(f"  Volovik estimate: G_N^{{-1}} ~ N * Lambda^2 / (48*pi)")
print(f"  N_species = {N_modes_total}")
print(f"  Lambda = K_BZ = {Lambda_phonon:.6f} M_KK^{{-1}}")
print(f"  1/(16*pi*G) = {inv_16piG_volovik:.6e} M_KK^2")
print(f"  M_Pl_eff = {M_Pl_eff_volovik_GeV:.4e} GeV")
print(f"  G_Sak/G_obs = {ratio_G_volovik:.6e}")
print(f"  |log10| = {abs(np.log10(ratio_G_volovik)):.4f}")
print()

# Now with the Volovik formula as stated in task:
# G_N^{-1} ~ 192 * M_KK^2 / (48*pi) = 4*M_KK^2 / pi
# This uses Lambda = M_KK (not K_BZ)
print(f"  Volovik estimate with Lambda = M_KK (not K_BZ):")
inv_16piG_volovik_mkk = N_modes_total * 1.0**2 / (48 * PI**2)  # Lambda=1 in M_KK units
M_Pl_eff_volovik_mkk = np.sqrt(2 * inv_16piG_volovik_mkk)
M_Pl_eff_volovik_mkk_GeV = M_Pl_eff_volovik_mkk * M_KK
ratio_G_volovik_mkk = (M_Pl_obs / M_Pl_eff_volovik_mkk_GeV)**2
ratio_MPl_volovik_mkk = M_Pl_eff_volovik_mkk_GeV / M_Pl_obs

print(f"  1/(16*pi*G) = {inv_16piG_volovik_mkk:.6e} M_KK^2")
print(f"  M_Pl_eff = {M_Pl_eff_volovik_mkk_GeV:.4e} GeV")
print(f"  M_Pl_eff / M_Pl_obs = {ratio_MPl_volovik_mkk:.6e}")
print(f"  G_Sak/G_obs = {ratio_G_volovik_mkk:.6e}")
print(f"  |log10| = {abs(np.log10(ratio_G_volovik_mkk)):.4f}")
print()

# Also compute 4*M_KK^2/pi explicitly as in task
inv_G_task = 4.0 * M_KK**2 / PI  # GeV^2
G_task = 1.0 / inv_G_task  # GeV^{-2}
# G_obs in natural units: G_N = 1/M_Pl_unreduced^2 = 6.71e-39 GeV^{-2}
from canonical_constants import M_Pl_unreduced
G_obs_natural = 1.0 / M_Pl_unreduced**2  # GeV^{-2}
ratio_G_task = G_task / G_obs_natural

print(f"  Task formula: G^{{-1}} = 4*M_KK^2/pi")
print(f"  1/G = {inv_G_task:.4e} GeV^2")
print(f"  G = {G_task:.4e} GeV^{{-2}}")
print(f"  G_obs = 1/M_Pl^2 = {G_obs_natural:.4e} GeV^{{-2}}")
print(f"  G_task / G_obs = {ratio_G_task:.6e}")
print(f"  |log10| = {abs(np.log10(ratio_G_task)):.4f}")
print()

# =============================================================================
# STEP 5: Compare to S24b/S44/S45 Dirac-tower Sakharov
# =============================================================================
print("--- STEP 5: Comparison with Prior Sakharov Computations ---")
print()

# S44 SAKHAROV-GN-44 (CORRECTED): Dirac tower, a_0=6440 PW modes
# M_Pl_eff = 99 GeV (wrong formula), corrected: G_Sak/G_obs = 0.436 at Lambda=10*M_KK
# S45 RUNNING-GN-45 confirmed to 0.19%
# Convention: G_obs/G_Sak = 2.29 (Sakharov predicts 2.29x STRONGER gravity)

# S44 values
N_PW_modes = a0_fold  # 6440
G_ratio_S44 = 0.436   # G_Sak/G_obs at Lambda=10*M_KK  # (local)
M_Pl_eff_S44_GeV = 99.0  # GeV (from formula error, but ratio is correct)  # (local)

# S24b: spectral action route
# 1/(16*pi*G) = f_2 * a_2 * M_KK^2 / (2*pi)  (Chamseddine-Connes formula)
# At f_2 = 1 (natural cutoff):
inv_16piG_SA = a2_fold * M_KK**2 / (2 * PI)  # GeV^2
M_Pl_eff_SA = np.sqrt(2 * inv_16piG_SA)  # GeV
ratio_G_SA = (M_Pl_obs / M_Pl_eff_SA)**2

print(f"  METHOD 1: This computation (phonon Sakharov)")
print(f"    N_modes = {N_modes_total} (= {N_cells} cells x {N_branches} branches)")
print(f"    Lambda = K_BZ = {Lambda_phonon:.4f} M_KK^{{-1}}")
print(f"    M_Pl_eff = {M_Pl_eff_GeV_analytic:.4e} GeV")
print(f"    G_Sak/G_obs = {ratio_G_analytic:.4e}")
print(f"    |log10| = {abs(np.log10(ratio_G_analytic)):.2f} OOM")
print()

print(f"  METHOD 2: S44/S45 Dirac-tower Sakharov (Lambda=10*M_KK)")
print(f"    N_modes = {int(N_PW_modes)} (PW-weighted Dirac eigenmodes)")
print(f"    Lambda = 10 * M_KK = {10*M_KK:.4e} GeV")
print(f"    G_Sak/G_obs = {G_ratio_S44}")
print(f"    |log10| = {abs(np.log10(G_ratio_S44)):.2f} OOM")
print()

print(f"  METHOD 3: Spectral action (S24b, f_2 = 1)")
print(f"    a_2 = {a2_fold:.2f}")
print(f"    1/(16*pi*G) = a_2 * M_KK^2 / (2*pi) = {inv_16piG_SA:.4e} GeV^2")
print(f"    M_Pl_eff = {M_Pl_eff_SA:.4e} GeV")
print(f"    G_SA/G_obs = {ratio_G_SA:.4e}")
print(f"    |log10| = {abs(np.log10(ratio_G_SA)):.2f} OOM")
print()

# Species ratio
print(f"  SPECIES COMPARISON:")
print(f"    Dirac tower: {int(N_PW_modes)} modes at Lambda = 10*M_KK")
print(f"    Phonon:      {N_modes_total} modes at Lambda = K_BZ = {Lambda_phonon:.4f} M_KK^{{-1}}")
print(f"    Mode ratio:  {N_PW_modes / N_modes_total:.1f}x")
print(f"    (Lambda ratio)^2: {(10.0 / Lambda_phonon)**2:.1f}x")
print(f"    Combined:    {N_PW_modes * (10.0)**2 / (N_modes_total * Lambda_phonon**2):.1f}x")
print()

# =============================================================================
# STEP 6: Decomposition by branch
# =============================================================================
print("--- STEP 6: Branch-by-Branch Contribution ---")
print()

# Fractional contribution from each branch (analytic, 1 cell)
frac = I_analytic / I_total_1cell_analytic
print(f"  {'Branch':<12} {'I_i':>14} {'Fraction':>10} {'cum %':>8}")
print(f"  {'-'*12} {'-'*14} {'-'*10} {'-'*8}")
cum = 0.0
for i in range(N_branches):
    cum += frac[i]
    print(f"  {branch_labels[i]:<12} {I_analytic[i]:>14.6f} {frac[i]:>10.4f} {cum*100:>7.1f}%")
print()

# =============================================================================
# STEP 7: Why the phonon route gives tiny G_N
# =============================================================================
print("--- STEP 7: Physical Interpretation ---")
print()

# The fundamental issue: Lambda_phonon = K_BZ << M_KK
# Sakharov integral scales as Lambda^2 (leading term)
# K_BZ / M_KK ~ 0.716 (less than 1 in M_KK units)
# But the REAL suppression: K_BZ is in M_KK^{-1}, so Lambda ~ 0.716 M_KK
# (Actually K_BZ IS in M_KK units since we work dimensionlessly)

# Let me be precise about units
print(f"  K_BZ = {K_BZ:.6f} [M_KK^{{-1}} units = dimensionless]")
print(f"  In M_KK units, Lambda_phonon = {K_BZ:.4f} M_KK")
print(f"  For Dirac tower, Lambda = 10 M_KK (S44 calibration)")
print()
print(f"  Leading-order scaling: G ~ 1/(N * Lambda^2)")
print(f"  N_phonon * Lambda_phonon^2 = {N_modes_total} * {K_BZ**2:.4f} = {N_modes_total * K_BZ**2:.2f}")
print(f"  N_Dirac  * Lambda_Dirac^2  = {int(N_PW_modes)} * {10.0**2:.0f} = {N_PW_modes * 100:.0f}")
print(f"  Ratio: {N_PW_modes * 100 / (N_modes_total * K_BZ**2):.1f}x")
print()

# The physical point from Volovik (2003):
# In 3He-A, G_eff^{-1} ~ p_F^2 * N_F, where p_F is the Fermi momentum
# (the UV cutoff) and N_F is the density of states at the Fermi surface.
#
# Phonon modes have their UV cutoff at K_BZ << k_F (the Fermi momentum).
# They are LOW-ENERGY collective modes, not the fundamental fermions.
# The Sakharov mechanism counts FERMIONIC loops, not bosonic ones.
# Phonons contribute to gravity through different channels (Volovik Paper 07,
# Section IV: "phonon contribution to G is subleading by (T/Delta)^2").

print("  VOLOVIK DIAGNOSTIC:")
print("  In 3He-A (Paper 07, Section IV), G_eff^{-1} ~ p_F^2 * N(E_F)")
print("  Phonon contribution to 1/G is SUBLEADING by (T/Delta)^2 << 1")
print("  The dominant contribution comes from FERMIONIC quasiparticles")
print("  near the Fermi surface, not from collective bosonic modes.")
print()
print("  Framework parallel:")
print("  - Dirac tower (S44): N=6440 fermionic modes, Lambda=10*M_KK -> 0.36 OOM")
print("  - GL phonons (this): N=192 bosonic modes, Lambda=K_BZ -> large deficit")
print("  - Phonons are emergent from the condensate — they do NOT replace the")
print("    Dirac-tower Sakharov mechanism; they ADD a subleading correction.")
print()

# =============================================================================
# STEP 8: Correction to Dirac-tower Sakharov from phonon dressing
# =============================================================================
print("--- STEP 8: Phonon Correction to Dirac-Tower G_N ---")
print()

# S44/S45 established: 1/(16*pi*G_Sak) from Dirac tower = a_0 * Lambda^2 / (48*pi^2)
# with a_0 = 6440, Lambda = 10*M_KK
#
# The phonon modes add a SEPARATE contribution:
# delta(1/(16*pi*G)) = phonon_integral / (48*pi^2)
#
# Relative correction:
delta_inv_G_phonon = I_total_analytic / (48 * PI**2)  # M_KK^2

# S44 Dirac contribution: a_0 * (10)^2 / (48*pi^2) in M_KK^2
inv_16piG_Dirac = a0_fold * (10.0)**2 / (48 * PI**2)

fractional_correction = delta_inv_G_phonon / inv_16piG_Dirac

print(f"  Dirac-tower: 1/(16*pi*G) = {inv_16piG_Dirac:.4e} M_KK^2")
print(f"  Phonon add:  delta[1/(16*pi*G)] = {delta_inv_G_phonon:.4e} M_KK^2")
print(f"  Fractional correction: {fractional_correction:.4e} = {fractional_correction*100:.4f}%")
print()
print(f"  Phonon correction to G_N: {-fractional_correction*100:.4f}%")
print(f"  (negative = G_N slightly DECREASED = gravity slightly STRONGER)")
print()

# =============================================================================
# STEP 9: What Lambda would phonons need to match G_obs?
# =============================================================================
print("--- STEP 9: Required Lambda for Phonon G_N Match ---")
print()

# To match G_obs with 192 modes:
# 1/(16*pi*G_obs) = M_Pl_reduced^2 / 2 = (2.435e18)^2 / 2 GeV^2
inv_16piG_obs = M_Pl_reduced**2 / 2  # GeV^2
inv_16piG_obs_MKK = inv_16piG_obs / M_KK**2  # M_KK^2

# For N massless modes: 1/(16*pi*G) = N * Lambda^2 / (48*pi^2)
# Lambda_needed^2 = 48*pi^2 * inv_16piG_obs_MKK / N_modes_total
Lambda_needed_sq = 48 * PI**2 * inv_16piG_obs_MKK / N_modes_total
Lambda_needed = np.sqrt(Lambda_needed_sq)

print(f"  1/(16*pi*G_obs) = {inv_16piG_obs:.4e} GeV^2 = {inv_16piG_obs_MKK:.4e} M_KK^2")
print(f"  Required Lambda = {Lambda_needed:.4e} M_KK^{{-1}}")
print(f"  Actual K_BZ = {K_BZ:.4e} M_KK^{{-1}}")
print(f"  Ratio Lambda_needed/K_BZ = {Lambda_needed/K_BZ:.4e}")
print()
print(f"  Lambda_needed in GeV = {Lambda_needed * M_KK:.4e} GeV")
print(f"  This is {Lambda_needed:.2f} M_KK -- ABOVE the KK scale.")
print(f"  At Lambda > M_KK, the phonon description breaks down.")
print(f"  This confirms phonon Sakharov CANNOT reproduce G_N alone.")
print()

# =============================================================================
# SUMMARY
# =============================================================================
print("=" * 72)
print("SUMMARY: SAKHAROV-PHONON-53")
print("=" * 72)
print()
print(f"  G_Sak(phonon) / G_obs = {ratio_G_analytic:.4e}")
print(f"  |log10| = {abs(np.log10(ratio_G_analytic)):.2f} OOM")
print()
print(f"  M_Pl_eff(phonon) = {M_Pl_eff_GeV_analytic:.4e} GeV")
print(f"  M_Pl_obs         = {M_Pl_obs:.4e} GeV")
print()
print(f"  Volovik quick estimate (Lambda=M_KK): G/G_obs = {ratio_G_volovik_mkk:.4e}")
print(f"  Task formula (4*M_KK^2/pi):           G/G_obs = {ratio_G_task:.4e}")
print()
print(f"  Comparison with S44/S45 Dirac-tower Sakharov:")
print(f"    Dirac: G_Sak/G_obs = 0.436 (0.36 OOM) [PASS]")
print(f"    Phonon: G_Sak/G_obs = {ratio_G_analytic:.4e} ({abs(np.log10(ratio_G_analytic)):.2f} OOM)")
print(f"    Phonon correction to Dirac G_N: {fractional_correction*100:.4f}%")
print()
print(f"  Comparison with S24b spectral action:")
print(f"    SA (f_2=1): G_SA/G_obs = {ratio_G_SA:.4e} ({abs(np.log10(ratio_G_SA)):.2f} OOM)")
print()
print(f"  PHYSICAL CONCLUSION:")
print(f"    Phonon modes contribute a {fractional_correction*100:.4f}% correction to 1/G_N.")
print(f"    The dominant Sakharov mechanism is the Dirac tower (S44, 6440 modes).")
print(f"    Phonon Sakharov alone gives {abs(np.log10(ratio_G_analytic)):.1f} OOM deficit --")
print(f"    confirming Volovik (1994, 2003): phonons are SUBLEADING to fermionic")
print(f"    quasiparticle loops in gravitational induction.")
print()
print(f"  GATE VERDICT: SAKHAROV-PHONON-53 = INFO")
print(f"    G_N^{{Sakharov}} from phonon spectrum reported and compared.")
print(f"    Phonon contribution is perturbative correction to Dirac-tower result.")
print()

# =============================================================================
# Save results
# =============================================================================
outfile = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "s53_sakharov_phonon_output.txt")
# Redirect stdout to file
import io
import contextlib

# Re-run with output capture
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    print("=" * 72)
    print("SAKHAROV-PHONON-53: Emergent G_N from GL 6-Branch Phonon Spectrum")
    print("=" * 72)
    print()
    print(f"M_KK = {M_KK:.4e} GeV")
    print(f"M_Pl_reduced = {M_Pl_obs:.4e} GeV")
    print(f"K_BZ = {K_BZ:.6f} M_KK^{{-1}}")
    print(f"N_cells = {N_cells}, N_branches = {N_branches}, N_total = {N_modes_total}")
    print()
    print("Branch dispersions (K=0):")
    for i in range(N_branches):
        print(f"  {branch_labels[i]:<12}: omega_0 = {masses_K0[i]:.6f}, c_eff = {c_eff_arr[i]:.6f}")
    print()
    print("Sakharov integrals (per cell, analytic):")
    for i in range(N_branches):
        print(f"  {branch_labels[i]:<12}: I = {I_analytic[i]:.6f} ({frac[i]*100:.1f}%)")
    print(f"  Total (1 cell): {I_total_1cell_analytic:.6f}")
    print(f"  Total ({N_cells} cells): {I_total_analytic:.6f}")
    print()
    print(f"Phonon Sakharov G_N:")
    print(f"  1/(16*pi*G) = {inv_16piG_analytic:.6e} M_KK^2")
    print(f"  M_Pl_eff = {M_Pl_eff_GeV_analytic:.4e} GeV")
    print(f"  G_Sak(phonon)/G_obs = {ratio_G_analytic:.4e}")
    print(f"  |log10| = {abs(np.log10(ratio_G_analytic)):.2f} OOM")
    print()
    print(f"Volovik quick estimate (N=192, Lambda=M_KK):")
    print(f"  G/G_obs = {ratio_G_volovik_mkk:.4e}")
    print(f"  |log10| = {abs(np.log10(ratio_G_volovik_mkk)):.2f} OOM")
    print()
    print(f"Task formula (4*M_KK^2/pi):")
    print(f"  G/G_obs = {ratio_G_task:.4e}")
    print(f"  |log10| = {abs(np.log10(ratio_G_task)):.2f} OOM")
    print()
    print(f"Dirac-tower Sakharov (S44/S45):")
    print(f"  G_Sak/G_obs = 0.436 (0.36 OOM)")
    print(f"  N_modes = 6440, Lambda = 10*M_KK")
    print()
    print(f"Spectral action (S24b, f_2=1):")
    print(f"  G_SA/G_obs = {ratio_G_SA:.4e}")
    print(f"  |log10| = {abs(np.log10(ratio_G_SA)):.2f} OOM")
    print()
    print(f"Phonon correction to Dirac-tower G_N: {fractional_correction*100:.4f}%")
    print()
    print(f"Required Lambda for phonon-only G_N match: {Lambda_needed:.2f} M_KK")
    print(f"  (vs actual K_BZ = {K_BZ:.4f} M_KK)")
    print()
    print("GATE: SAKHAROV-PHONON-53 = INFO")

with open(outfile, 'w') as f:
    f.write(buf.getvalue())

print(f"\nOutput saved to: {outfile}")

# Save .npz
npz_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         "s53_sakharov_phonon.npz")
np.savez(npz_path,
         # Inputs
         K_array=K_array,
         K_BZ=K_BZ,
         branch_labels=branch_labels,
         omega_branches=omega_branches,
         masses_K0=masses_K0,
         c_eff=c_eff_arr,
         N_cells=N_cells,
         N_branches=N_branches,
         N_modes_total=N_modes_total,
         Lambda_phonon=Lambda_phonon,
         # Sakharov integrals
         I_analytic=I_analytic,
         I_numerical=I_numerical,
         I_total_1cell_analytic=I_total_1cell_analytic,
         I_total_analytic=I_total_analytic,
         # G_N results
         inv_16piG_analytic=inv_16piG_analytic,
         M_Pl_eff_GeV=M_Pl_eff_GeV_analytic,
         ratio_G_phonon=ratio_G_analytic,
         log10_ratio=abs(np.log10(ratio_G_analytic)),
         # Volovik estimates
         ratio_G_volovik_KBZ=ratio_G_volovik,
         ratio_G_volovik_MKK=ratio_G_volovik_mkk,
         ratio_G_task=ratio_G_task,
         # Comparisons
         ratio_G_SA=ratio_G_SA,
         fractional_correction=fractional_correction,
         Lambda_needed=Lambda_needed,
         # Gate
         gate_name=np.array(["SAKHAROV-PHONON-53"]),
         gate_verdict=np.array(["INFO"]),
         gate_detail=np.array([f"G_phonon/G_obs={ratio_G_analytic:.4e} ({abs(np.log10(ratio_G_analytic)):.2f} OOM). "
                               f"Phonon correction to Dirac G_N: {fractional_correction*100:.4f}%. "
                               f"Dirac tower dominates (S44: 0.36 OOM)."])
         )
print(f"Data saved to: {npz_path}")
