#!/usr/bin/env python3
"""
S74 LEGGETT-JEANS-74: Leggett Jeans k_J in 4D Units
====================================================

Computes the Jeans wavenumber k_J for the Leggett (inter-band coherence) mode
in the phonon-exflation framework, converted to 4D observable units (Mpc^{-1}).

SUBSTRATE FRAMING:
The Leggett mode is the inter-band Leggett collective mode of the BCS sector.
It is NOT a hydrodynamic sound mode of a fluid embedded in a pre-existing space.
Rather, it is an eigen-mode of the fabric's D_K spectrum that governs the
minimum spatial scale over which inter-band phase coherence can be sustained
against self-gravity in the emergent 4D description. Space is emergent from
spectral weight redistribution, so "DM clumping length" translates to "smallest
k at which the Leggett coherence channel resists self-gravitational compaction."

JEANS THEORY (standard derivation, reported here for clarity):
For a massive scalar field / collective mode with sound speed c_s, the Jeans
wavenumber satisfies
   k_J^2 = 4 pi G rho / c_s^2
(Weinberg, Cosmology eq. 6.1.13; Gurevich & Zybin 1995 for DM variants).

For the Leggett mode:
  - c_L is the Leggett sound speed (inter-band group velocity, canonical 0.025 M_KK, S64)
  - rho_L is the Leggett energy density (inter-band coherence channel)
  - G is Newton's constant (emergent from a_2 spectral moment)

Modes with k < k_J are gravitationally UNSTABLE (clump).
Modes with k > k_J are gravitationally STABLE (oscillate).
k_J thus sets the smallest DM clump length lambda_J = 2*pi/k_J.

INPUT PROVENANCE:
  - c_L: S64 canonical value c_Leggett = 0.025 M_KK (mean of [0.019, 0.032] S56)
  - rho_L: from S60 LEGGETT-DM-ABUND relic abundance (matches observed Omega_DM)
  - G, M_KK, M_Pl from canonical_constants.py

PRE-REGISTERED GATE: LEGGETT-JEANS-74
  PASS: k_J computed in Mpc^{-1} AND in [1e-6, 1] Mpc^{-1}
  INFO: k_J computed but outside range
  FAIL: k_J undefined

Author: Quantum Acoustics Theorist Agent
Session: S74, W4-FF
"""

import sys
import os
import numpy as np

# Ensure canonical_constants is importable
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    M_KK, M_KK_gravity,
    M_Pl_reduced, M_Pl_unreduced,
    G_N,
    H_0_GeV, H_0_inv_s,
    T_CMB, T_CMB_GeV,
    rho_crit_GeV4, rho_Lambda_obs, Omega_DM,
    hbar_c_GeV_m, hbar_c_GeV_fm,
    GeV_inv_to_Mpc, Mpc_to_GeV_inv, Mpc_to_m,
    omega_L1, omega_L2,
    Delta_BCS, E_cond,
    J_C2, c_Gold, c_fabric,
    N_cells, PI,
)

print("=" * 72)
print("S74 LEGGETT-JEANS-74: Leggett Jeans Wavenumber in 4D Units")
print("=" * 72)

# ============================================================================
# 1. LEGGETT SOUND SPEED (S64 / S56 canonical)
# ============================================================================
#
# From S56 Leggett-fabric spectrum: c_L = [0.019, 0.032] M_KK (group velocity range)
# From S64 four-speed summary: c_Leggett = 0.025 (central value)
# We use central value AND compute the range for robustness.

c_L_MKK_central = 0.025            # central Leggett sound speed (M_KK units)  # (local)
c_L_MKK_lo = 0.019                 # lower bound (S56, GL gap)                  # (local)
c_L_MKK_hi = 0.032                 # upper bound (S56, S49_1 gap)               # (local)

print("\n--- Leggett Sound Speed (S56/S64 canonical) ---")
print(f"c_L (central) = {c_L_MKK_central:.4f} M_KK (dimensionless, c=1 units)")
print(f"c_L (range)   = [{c_L_MKK_lo:.4f}, {c_L_MKK_hi:.4f}] M_KK")
print(f"  [c_L is already dimensionless in natural units; it is a fraction of c]")

# ============================================================================
# 2. LEGGETT ENERGY DENSITY (from S60 LEGGETT-DM-ABUND canonical inheritance)
# ============================================================================
#
# The Leggett mode carries the DM-relevant energy density. From S60/S66,
# the Leggett channel saturates the DM relic budget: Omega_L h^2 = 0.120 (central).
# The present-day Leggett energy density is therefore
#   rho_L(today) = Omega_DM * rho_crit = 0.265 * 4.08e-47 GeV^4
#
# This is the 4D-projected energy density, accounting for all relevant dilution
# from the fold to today. We use Omega_DM = 0.265 (Planck 2018 central value).
#
# NOTE: This is NOT the "bare" Leggett mode density at production (which is
# M_KK^4-order). It is the expanded, redshifted, observationally-relevant
# density in the 4D emergent description. This is the correct input for a
# 4D Jeans scale computation.

Omega_DM_canonical = 0.265                 # Planck 2018 central             # (local)
rho_L_GeV4 = Omega_DM_canonical * rho_crit_GeV4  # Leggett energy density today (GeV^4)
rho_L_kg_m3 = rho_L_GeV4 / (hbar_c_GeV_m**3) * 1.78266192e-27  # convert GeV^4 -> kg/m^3  # (local)

# More careful conversion: GeV^4 to kg/m^3
# Energy density: 1 GeV = 1.78266e-27 kg*c^2, so rho[kg/m^3] = rho[GeV/m^3]/c^2
# 1 GeV^4 in SI:
#   rho[J/m^3] = rho[GeV^4] * (GeV in J) / (hbar*c in GeV*m)^3
#   GeV in J = 1.602176634e-10 J
#   hbar*c = 1.973269804e-16 GeV*m
GeV_to_J = 1.602176634e-10  # (local)
rho_L_J_m3 = rho_L_GeV4 * GeV_to_J / (hbar_c_GeV_m**3)  # energy density in J/m^3   # (local)
rho_L_kg_m3 = rho_L_J_m3 / (2.99792458e8)**2             # mass density in kg/m^3   # (local)

print("\n--- Leggett Energy Density (S60/S66 DM-saturated) ---")
print(f"Omega_DM (Planck)    = {Omega_DM_canonical:.3f}")
print(f"rho_crit             = {rho_crit_GeV4:.4e} GeV^4")
print(f"rho_L (GeV^4)        = {rho_L_GeV4:.4e}")
print(f"rho_L (J/m^3)        = {rho_L_J_m3:.4e}")
print(f"rho_L (kg/m^3)       = {rho_L_kg_m3:.4e}")

# ============================================================================
# 3. JEANS WAVENUMBER (natural units first)
# ============================================================================
#
# Jeans formula (massive collective mode, self-gravity):
#     k_J = sqrt(4 pi G rho) / c_s
#
# In natural units (c=1, hbar=1):
#   G_N = 1 / M_Pl_unreduced^2 (GeV^{-2})
#   rho in GeV^4
#   c_s dimensionless
#   k_J in GeV (inverse length in natural units)

G_natural_GeV_inv2 = 1.0 / M_Pl_unreduced**2  # Newton's constant in GeV^{-2}  # (local)
print(f"\n--- Newton's constant (natural units) ---")
print(f"G_N = 1/M_Pl^2 = {G_natural_GeV_inv2:.4e} GeV^{-2}")
print(f"M_Pl_unreduced = {M_Pl_unreduced:.4e} GeV")
print(f"M_Pl_reduced   = {M_Pl_reduced:.4e} GeV")

# k_J in natural (GeV) units, central Leggett speed
k_J_natural_central = np.sqrt(4.0 * PI * G_natural_GeV_inv2 * rho_L_GeV4) / c_L_MKK_central
k_J_natural_lo      = np.sqrt(4.0 * PI * G_natural_GeV_inv2 * rho_L_GeV4) / c_L_MKK_hi  # hi c_L -> lo k_J
k_J_natural_hi      = np.sqrt(4.0 * PI * G_natural_GeV_inv2 * rho_L_GeV4) / c_L_MKK_lo  # lo c_L -> hi k_J

print(f"\n--- Jeans wavenumber (natural GeV units) ---")
print(f"sqrt(4*pi*G*rho_L) = {np.sqrt(4.0 * PI * G_natural_GeV_inv2 * rho_L_GeV4):.4e} GeV")
print(f"k_J (central c_L)  = {k_J_natural_central:.4e} GeV")
print(f"k_J (range)        = [{k_J_natural_lo:.4e}, {k_J_natural_hi:.4e}] GeV")

# ============================================================================
# 4. CONVERT TO Mpc^{-1}
# ============================================================================
#
# 1 GeV (energy) <-> 1 GeV^{-1} (length, natural units) = hbar*c/GeV in meters
# hbar*c = 1.973e-16 GeV*m, so 1 GeV = (1/1.973e-16) m^{-1} = 5.068e15 m^{-1}
# 1 Mpc = 3.0857e22 m, so
#   k[Mpc^{-1}] = k[m^{-1}] * Mpc_to_m
#   k[GeV] * (1/hbar_c_GeV_m) m^{-1} = k[GeV] * Mpc_to_m / hbar_c_GeV_m Mpc^{-1}

GeV_to_invMpc = Mpc_to_m / hbar_c_GeV_m  # 1 GeV -> Mpc^{-1}  # (local)
print(f"\n--- Unit conversion ---")
print(f"1 GeV = {GeV_to_invMpc:.4e} Mpc^{-1}")
print(f"  (check: 1/GeV_inv_to_Mpc = {1.0/GeV_inv_to_Mpc:.4e})")

k_J_invMpc_central = k_J_natural_central * GeV_to_invMpc
k_J_invMpc_lo = k_J_natural_lo * GeV_to_invMpc
k_J_invMpc_hi = k_J_natural_hi * GeV_to_invMpc

print(f"\n--- Jeans wavenumber in Mpc^{-1} ---")
print(f"k_J (central)      = {k_J_invMpc_central:.4e} Mpc^{-1}")
print(f"k_J (lo c_L=0.032) = {k_J_invMpc_lo:.4e} Mpc^{-1}")
print(f"k_J (hi c_L=0.019) = {k_J_invMpc_hi:.4e} Mpc^{-1}")

# ============================================================================
# 5. JEANS LENGTH AND MASS
# ============================================================================

lambda_J_Mpc_central = 2.0 * PI / k_J_invMpc_central  # comoving Jeans length
lambda_J_Mpc_lo = 2.0 * PI / k_J_invMpc_hi
lambda_J_Mpc_hi = 2.0 * PI / k_J_invMpc_lo

print(f"\n--- Jeans length (Mpc) ---")
print(f"lambda_J (central) = {lambda_J_Mpc_central:.4e} Mpc")
print(f"lambda_J (range)   = [{lambda_J_Mpc_lo:.4e}, {lambda_J_Mpc_hi:.4e}] Mpc")

# Jeans mass (standard): M_J = (4 pi / 3) * (lambda_J/2)^3 * rho
rho_L_Msun_Mpc3 = rho_L_kg_m3 * (Mpc_to_m)**3 / 1.989e30  # Msun/Mpc^3  # (local)
M_J_Msun_central = (4.0 * PI / 3.0) * (lambda_J_Mpc_central / 2.0)**3 * rho_L_Msun_Mpc3
print(f"\n--- Jeans mass (M_sun) ---")
print(f"rho_L (Msun/Mpc^3) = {rho_L_Msun_Mpc3:.4e}")
print(f"M_J (central)      = {M_J_Msun_central:.4e} M_sun")

# ============================================================================
# 6. DIMENSIONAL CROSS-CHECK
# ============================================================================
#
# [k_J]^2 = [G] * [rho] / [c_s^2]
#         = (length^3 / mass / time^2) * (mass / length^3) / (length^2 / time^2)
#         = 1 / time^2 * 1 / (length^2/time^2)
#         = 1 / length^2 = correct!
#
# Numerical cross-check via SI units
# k_J[SI] = sqrt(4 pi G rho[kg/m^3]) / c_s[m/s]
#         [m^-1] = sqrt([m^3/kg/s^2] * [kg/m^3]) / [m/s] = sqrt(1/s^2) / (m/s) = (1/s)/(m/s) = 1/m

c_light_SI = 2.99792458e8   # m/s  # (local)
c_L_SI_central = c_L_MKK_central * c_light_SI  # m/s (c_L is a fraction of c)  # (local)

k_J_SI_central = np.sqrt(4.0 * PI * G_N * rho_L_kg_m3) / c_L_SI_central  # m^-1
k_J_invMpc_SI  = k_J_SI_central * Mpc_to_m  # Mpc^-1

print(f"\n--- Dimensional cross-check (SI units) ---")
print(f"G_N (SI)           = {G_N:.4e} m^3 kg^-1 s^-2")
print(f"rho_L (kg/m^3)     = {rho_L_kg_m3:.4e}")
print(f"c_L (m/s)          = {c_L_SI_central:.4e}")
print(f"k_J (SI)           = {k_J_SI_central:.4e} m^-1")
print(f"k_J (SI -> Mpc^-1) = {k_J_invMpc_SI:.4e} Mpc^-1")
print(f"k_J (natural route)= {k_J_invMpc_central:.4e} Mpc^-1")

rel_err = abs(k_J_invMpc_SI - k_J_invMpc_central) / k_J_invMpc_central
print(f"Relative error (SI vs natural) = {rel_err:.4e}")
assert rel_err < 1e-3, f"Natural vs SI mismatch: {rel_err}"
print("PASS: natural and SI routes agree to better than 0.1%")

# ============================================================================
# 7. COMPARISON TO OBSERVATIONAL SCALES
# ============================================================================

k_BAO = 0.066   # Mpc^-1, BAO peak (approximate)  # (local)
k_nl = 0.2      # Mpc^-1, non-linear scale  # (local)
k_galaxy = 1.0  # Mpc^-1, galaxy scale  # (local)
k_MW_halo = 0.015  # Mpc^-1, Milky Way halo scale  # (local)

print(f"\n--- Comparison to observational scales ---")
print(f"k_J (central)        = {k_J_invMpc_central:.4e} Mpc^-1  <-- LEGGETT JEANS")
print(f"k_BAO ~ 0.066 Mpc^-1    (BAO)")
print(f"k_nl ~ 0.2   Mpc^-1    (non-linear)")
print(f"k_MW halo ~ 0.015      (Milky Way halo)")
print(f"k_galaxy ~ 1           (galaxy scale)")
print(f"k_Planck range (valid)= [{1e-6:.0e}, {1.0:.0e}] Mpc^-1")

# ============================================================================
# 8. GATE VERDICT
# ============================================================================

print("\n" + "=" * 72)
print("GATE VERDICT: LEGGETT-JEANS-74")
print("=" * 72)

gate_lo = 1e-6  # (local)
gate_hi = 1.0  # (local)

if np.isfinite(k_J_invMpc_central) and k_J_invMpc_central > 0:
    if gate_lo <= k_J_invMpc_central <= gate_hi:
        verdict = "PASS"
        verdict_text = (
            f"k_J = {k_J_invMpc_central:.4e} Mpc^-1 is well-defined and lies "
            f"within the observationally-relevant range [{gate_lo:.0e}, {gate_hi:.0e}] Mpc^-1"
        )
    else:
        verdict = "INFO"
        verdict_text = (
            f"k_J = {k_J_invMpc_central:.4e} Mpc^-1 is well-defined but outside "
            f"[{gate_lo:.0e}, {gate_hi:.0e}] Mpc^-1"
        )
else:
    verdict = "FAIL"
    verdict_text = f"k_J computation undefined or non-positive: {k_J_invMpc_central}"

print(f"Verdict: {verdict}")
print(f"  {verdict_text}")

# ============================================================================
# 9. SAVE DATA
# ============================================================================

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 's74_leggett_jeans.npz')
np.savez(
    out_path,
    # PRIMARY RESULTS
    k_J_invMpc_central=k_J_invMpc_central,
    k_J_invMpc_lo=k_J_invMpc_lo,
    k_J_invMpc_hi=k_J_invMpc_hi,
    k_J_natural_central=k_J_natural_central,
    k_J_SI_central=k_J_SI_central,
    # INPUTS
    rho_L_GeV4=rho_L_GeV4,
    rho_L_J_m3=rho_L_J_m3,
    rho_L_kg_m3=rho_L_kg_m3,
    c_L_MKK_central=c_L_MKK_central,
    c_L_MKK_lo=c_L_MKK_lo,
    c_L_MKK_hi=c_L_MKK_hi,
    c_L_SI_central=c_L_SI_central,
    Omega_DM_used=Omega_DM_canonical,
    # DERIVED
    lambda_J_Mpc_central=lambda_J_Mpc_central,
    lambda_J_Mpc_lo=lambda_J_Mpc_lo,
    lambda_J_Mpc_hi=lambda_J_Mpc_hi,
    M_J_Msun_central=M_J_Msun_central,
    rho_L_Msun_Mpc3=rho_L_Msun_Mpc3,
    # CROSS-CHECK
    rel_err_SI_vs_natural=rel_err,
    # META
    verdict=verdict,
    gate_lo=gate_lo,
    gate_hi=gate_hi,
)
print(f"\nSaved: {out_path}")

print("\n" + "=" * 72)
print("SUMMARY")
print("=" * 72)
print(f"  k_J (central)    = {k_J_invMpc_central:.4e} Mpc^-1")
print(f"  k_J (range)      = [{k_J_invMpc_lo:.4e}, {k_J_invMpc_hi:.4e}] Mpc^-1")
print(f"  lambda_J         = {lambda_J_Mpc_central:.4e} Mpc")
print(f"  M_J              = {M_J_Msun_central:.4e} M_sun")
print(f"  rho_L (GeV^4)    = {rho_L_GeV4:.4e}")
print(f"  c_L (central)    = {c_L_MKK_central:.4f} (c=1 units)")
print(f"  GATE: {verdict}")
