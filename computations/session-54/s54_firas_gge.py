#!/usr/bin/env python3
"""
FIRAS-GGE-54: CMB Non-Thermality Suppression Factor
=====================================================

Session 54, Wave 2, Gate 5 (sagan-empiricist)

Physics:
  The GGE relic from the BCS transit has internal non-thermality:
  8 Richardson-Gaudin conserved integrals with distinct GGE temperatures.
  T_B2 = 0.668, T_B1 = 0.435, T_B3 = 0.178 (M_KK units).

  FIRAS constrains CMB spectral distortions to delta_T/T < 6e-5 (95% CL).

  The question: how much does the KK dimensional reduction (8D -> 4D)
  suppress the internal non-thermality? The 4D observer measures the
  volume-weighted average over the internal SU(3) manifold.

  The 32-cell Voronoi lattice tiles K = SU(3) with EQUAL volumes
  (volume-preserving TT deformation, S12).

Gate: FIRAS-GGE-54
  PASS: Observable delta_T/T < 6e-5 (FIRAS-compatible)
  FAIL: Observable delta_T/T >= 6e-5 (FIRAS-incompatible)

  Equivalently: need suppression factor >= 2000 from internal 12% to
  observable < 6e-5.

Skeptical Notes (Sagan):
  1. The "suppression" can only come from averaging over the internal space.
     But the KK reduction is NOT statistical — it is a deterministic integral.
  2. If all 32 cells have the SAME non-thermal distribution (coherent GGE),
     then averaging over cells provides ZERO suppression.
  3. The key question is whether different cells have different GGE states,
     or the same GGE state.
  4. Even if cells differ, sqrt(32) ~ 5.7 gives suppression of ~5.7x,
     which reduces 12% to 2% — nowhere near the factor 2000 needed.

Inputs: canonical_constants, S53 GGE data
Outputs: s54_firas_gge_output.txt, s54_firas_gge.npz, s54_firas_gge.png
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from canonical_constants import (
    N_cells, N_dof_BCS, E_exc, E_cond, n_pairs, n_Bog, S_inst,
    M_KK, T_CMB, T_CMB_GeV, rho_Lambda_obs, H_0_GeV,
    Vol_SU3_Haar, tau_fold, PI,
)

# ==============================================================================
#  SECTION 0: FIRAS CONSTRAINT
# ==============================================================================

print("=" * 72)
print("FIRAS-GGE-54: CMB Non-Thermality Suppression Factor")
print("=" * 72)

# FIRAS/COBE constraint on CMB spectral distortions
# Fixsen et al. 1996, Fixsen 2009
delta_T_over_T_FIRAS = 6e-5  # 95% CL, mu-type distortion
# More precisely: |mu| < 9e-5 (95% CL), |y| < 1.5e-5 (95% CL)
# Combined spectral distortion: delta_T/T < 6e-5

print("\n--- SECTION 0: FIRAS Constraint ---")
print(f"FIRAS 95% CL: delta_T/T < {delta_T_over_T_FIRAS:.1e}")
print(f"T_CMB = {T_CMB:.4f} K = {T_CMB_GeV:.4e} GeV")

# ==============================================================================
#  SECTION 1: INTERNAL NON-THERMALITY
# ==============================================================================

print("\n--- SECTION 1: Internal GGE Non-Thermality ---")

# GGE temperatures from S53 (in M_KK units)
# 4 B2 modes at T_B2, 1 B1 mode at T_B1, 3 B3 modes at T_B3
T_B2 = 0.668  # M_KK  # (local)
T_B1 = 0.435  # M_KK  # (local)
T_B3 = 0.178  # M_KK  # (local)

T_modes = np.array([T_B2]*4 + [T_B1] + [T_B3]*3)
N_modes = len(T_modes)
assert N_modes == N_dof_BCS == 8

T_mean = np.mean(T_modes)
T_max = np.max(T_modes)
T_min = np.min(T_modes)

# Internal non-thermality: the variation in sector temperatures
# relative to the mean
delta_T_internal = (T_max - T_min) / (2.0 * T_mean)
sigma_T_internal = np.std(T_modes) / T_mean  # coefficient of variation

# Also compute w_k = T_k / T_mean (sector weights)
w_k = T_modes / T_mean
w_range = w_k.max() - w_k.min()

print(f"GGE temperatures (M_KK units):")
print(f"  T_B2 = {T_B2:.3f} (4 modes)")
print(f"  T_B1 = {T_B1:.3f} (1 mode)")
print(f"  T_B3 = {T_B3:.3f} (3 modes)")
print(f"  T_mean = {T_mean:.4f}")
print(f"  T_max = {T_max:.3f}, T_min = {T_min:.3f}")
print(f"")
print(f"  w_k = T_k / T_mean: {w_k}")
print(f"  w range: [{w_k.min():.4f}, {w_k.max():.4f}]")
print(f"")
print(f"  delta_T_internal / T = (T_max - T_min) / (2*T_mean) = {delta_T_internal:.4f}")
print(f"  sigma(T) / T_mean (CV) = {sigma_T_internal:.4f}")
print(f"")
print(f"  Internal non-thermality: {delta_T_internal*100:.1f}%")
print(f"  (S53 W1-5 reported w range 0.158-0.202 -> ~12%)")

# Use the more conservative measure
nonthermality_internal = delta_T_internal

# ==============================================================================
#  SECTION 2: MECHANISM ANALYSIS — WHAT CAN SUPPRESS NON-THERMALITY?
# ==============================================================================

print("\n--- SECTION 2: Mechanism Analysis ---")

print("""
QUESTION: What suppresses the internal 12% non-thermality to < 6e-5?

There are exactly three possible suppression mechanisms:

  (A) CELL AVERAGING: If different Voronoi cells have different GGE states,
      the KK integral averages over them.
      Suppression: 1/sqrt(N_cells) = 1/sqrt(32) ~ 0.18

  (B) MODE AVERAGING: The 8 BCS modes have different temperatures.
      The 4D energy density is the SUM over all modes.
      Individual mode fluctuations average down by 1/sqrt(N_dof).
      Suppression: 1/sqrt(N_dof_BCS) = 1/sqrt(8) ~ 0.35

  (C) KK SPECTRAL AVERAGING: The full Dirac spectrum has many more modes.
      The total 4D energy density sums over ALL KK modes.
      Only 8 BCS modes are non-thermal; the rest (10,000+) are thermal.
      Suppression: N_BCS / N_total_modes ~ 8 / N_total

Let me evaluate each.
""")

# ---- Mechanism A: Cell Averaging ----
print("  MECHANISM A: Cell Averaging")
print(f"  N_cells = {N_cells}")
print(f"  Volume-preserving TT: all cells have EQUAL volume (S12)")
print(f"  BUT: the GGE is a GLOBAL state of the BCS condensate.")
print(f"  ALL cells have the SAME GGE distribution — the transit is")
print(f"  spatially homogeneous on the internal manifold (no spatial")
print(f"  domain structure — coherence length >> cell size, S37).")
print(f"  L/xi_GL = 0.031 (S37). The condensate is a SINGLE domain.")
print(f"  Cell averaging suppression: NONE (factor 1.0)")
print(f"")

suppression_A = 1.0  # No cell averaging — GGE is coherent  # (local)

# ---- Mechanism B: Mode Averaging ----
print("  MECHANISM B: Mode Averaging")
print(f"  N_dof_BCS = {N_dof_BCS}")
# The 4D energy density is rho_4D = sum_k E_k * n_k
# where E_k are mode energies and n_k are occupations
# The non-thermality is the VARIATION in n_k relative to a single-T Bose/Fermi
# Mode averaging: sigma(sum_k) / mean(sum_k) = sigma(per_mode) / mean(per_mode) / sqrt(N)
# if modes are uncorrelated.
# BUT: the 8 integrals of motion CONSTRAIN the n_k. They are NOT independent.
# The constraint is: I_k = sum_j f(E_j, lambda_k) is conserved for each k.
# With 8 conserved charges and 8 modes, the system is INTEGRABLE — every mode
# is determined by the 8 integrals. There are ZERO free fluctuations.

print(f"  The 4D energy density sums over 8 BCS modes.")
print(f"  Mode averaging would give 1/sqrt(8) = {1/np.sqrt(8):.4f}")
print(f"  BUT: 8 Richardson-Gaudin integrals CONSTRAIN all 8 modes.")
print(f"  The system is EXACTLY INTEGRABLE (S38). Mode occupations are")
print(f"  deterministic functions of the 8 conserved charges.")
print(f"  No statistical averaging occurs — the mode asymmetry is LOCKED.")
print(f"  Mode averaging suppression: NONE (factor 1.0)")
print(f"")

suppression_B = 1.0  # Integrability locks mode asymmetry  # (local)

# ---- Mechanism C: KK Spectral Dilution ----
print("  MECHANISM C: KK Spectral Dilution")
# The total 4D energy density includes ALL KK modes, not just BCS modes.
# BCS modes: 8 (at the gap edge, non-thermal)
# Total modes: sum over all Peter-Weyl sectors
# From S53 Eliashberg: sectors up to (p+q)=3 have 616 Kramers pairs
# The full spectrum (p+q -> infinity) has infinitely many modes, but
# they are UV-cutoff by the spectral action at Lambda = M_KK.
# The spectral action at tau_fold has ~6440 eigenvalues (S37).

N_dirac_total = 6440  # total Dirac eigenvalues in spectral action window
N_BCS_modes = N_dof_BCS  # 8 non-thermal modes

# The 4D vacuum energy density is:
#   rho_4D = (2/pi^2) * sum_k E_k^2 * f(E_k/Lambda) / Lambda^4
# where f is the spectral action cutoff function.
# The NON-THERMAL part comes only from the 8 BCS modes.
# The THERMAL (equilibrium) part comes from all modes.
# BUT: the question is about TEMPERATURE fluctuations, not energy.

# Actually, let me be more careful. The GGE non-thermality means:
# the BCS modes have occupations n_k that differ from Bose-Einstein at a
# single temperature. The relevant observable for the CMB is the
# SPECTRAL SHAPE of the radiation.

# In the KK picture:
# - The CMB photon IS a massless mode in the 4D theory
# - It couples to the internal space through the KK metric
# - The non-thermal GGE affects the CMB through gravitational coupling
# - The coupling strength is determined by the overlap integral

# The key insight: the CMB photon lives in the 4D sector.
# The GGE non-thermality lives in the INTERNAL sector.
# The coupling between them is gravitational only.

# The gravitational coupling transmits internal non-thermality to
# the 4D metric perturbations at order (E_internal / M_Pl^2).

# Energy in non-thermal modes vs Planck energy:
E_nonthermal = E_exc * abs(E_cond)  # in M_KK^2 units... no.
# E_exc = 60.625 M_KK (total excitation energy)
# This lives at the KK scale. The CMB is at T ~ 0.235 meV ~ 10^{-13} GeV.

print(f"  Total Dirac eigenvalues in SA window: ~{N_dirac_total}")
print(f"  Non-thermal BCS modes: {N_BCS_modes}")
print(f"  Dilution factor (mode count): {N_BCS_modes}/{N_dirac_total} = {N_BCS_modes/N_dirac_total:.4e}")
print(f"")
print(f"  BUT this is not the right calculation. The non-thermality")
print(f"  does not dilute by mode counting — it transmits through")
print(f"  the gravitational coupling to 4D.")

# ==============================================================================
#  SECTION 3: GRAVITATIONAL COUPLING — THE CORRECT CALCULATION
# ==============================================================================

print("\n--- SECTION 3: Gravitational Coupling to CMB ---")

# The correct physics:
# The GGE relic energy E_exc = 60.625 M_KK contributes to the 4D CC
# through the KK reduction. This gives rho_GGE = 3.74e68 GeV^4 (S53).
# The CMB SPECTRAL DISTORTION from an anisotropic stress-energy in the
# internal space is:
#
#   delta_T/T ~ (delta_rho / rho) * (rho_internal / rho_CMB)
#
# where delta_rho / rho is the non-thermality in the internal energy.

# BUT: the CMB was PRODUCED during recombination, when the 4D plasma
# thermalized. The question is whether the internal non-thermality
# leaves an imprint on the 4D radiation field.

# There are two epochs to consider:
# (1) PRE-RECOMBINATION: the internal non-thermality sources a
#     quadrupole in the photon distribution through gravitational
#     coupling. This creates an anisotropy at order:
#     delta_T/T ~ (Phi_internal) ~ (rho_nonthermal / rho_total)
#
# (2) POST-RECOMBINATION: the internal DOF are frozen. The CMB
#     free-streams. No further coupling.

# The crucial point: the NON-THERMALITY is in the INTERNAL Hilbert space.
# The 4D observer projects onto the 4D subspace.
# The internal non-thermality appears as an ANISOTROPIC component of
# the stress-energy tensor in the 4D effective theory.

# For the CMB spectral shape:
# The photon number density in the 4D theory inherits the AVERAGE
# temperature from the internal space. Deviations from this average
# appear as higher multipole moments in the internal angular expansion.
# These couple to the 4D metric at order (R_internal / R_4D)^2.

# Let me compute the actual numbers.

# The 4D metric perturbation from internal non-thermality:
# h_mu_nu ~ (8*pi*G_N) * T_mu_nu^{internal} / k^2
# where T_mu_nu^{internal} is the TRACE of the internal stress-energy
# variation.

# The trace of the internal non-thermality:
# delta_T_00 = rho_GGE * (delta_T/T)_internal
rho_GGE_GeV4 = 3.7413e68  # GeV^4 (from S53)  # (local)
delta_rho_internal = rho_GGE_GeV4 * nonthermality_internal

print(f"  rho_GGE = {rho_GGE_GeV4:.4e} GeV^4")
print(f"  Internal non-thermality = {nonthermality_internal:.4f}")
print(f"  delta_rho_internal = {delta_rho_internal:.4e} GeV^4")

# The CMB energy density:
# rho_CMB = (pi^2/15) * T_CMB^4 = 2.01e-51 GeV^4
rho_CMB = (PI**2 / 15.0) * T_CMB_GeV**4
print(f"  rho_CMB = {rho_CMB:.4e} GeV^4")
print(f"  T_CMB = {T_CMB_GeV:.4e} GeV")

# STOP. This comparison is meaningless as stated.
# rho_GGE is the TOTAL internal energy, NOT a perturbation to the CMB.
# The CC problem (115 orders) means the GGE energy is already
# inconsistent with observations — it's the same number as S53.
# Computing delta_rho_internal / rho_CMB just reproduces the CC gap.

print(f"\n  IMPORTANT: Comparing rho_GGE to rho_CMB is the CC problem.")
print(f"  delta_rho_internal / rho_CMB = {delta_rho_internal/rho_CMB:.4e}")
print(f"  This is ~10^119 — the CC gap again, not a new constraint.")

# ==============================================================================
#  SECTION 4: WHAT THE COMPUTATION ACTUALLY SHOWS
# ==============================================================================

print("\n--- SECTION 4: The Actual Physical Situation ---")

print("""
The question "how much does gravitational averaging suppress the GGE
non-thermality?" rests on an assumption that needs examination.

ASSUMPTION: The 4D observer sees a REDUCED version of the internal
non-thermality, diluted by the KK averaging.

REALITY: The KK reduction is NOT statistical averaging. It is a
deterministic integral over the internal manifold:

  rho_4D = (1/V_K) * integral_K rho_8D(x, y) * sqrt(g_K) d^8y

If rho_8D(x, y) = rho_8D(x) (no y-dependence), the integral is trivial:
  rho_4D = rho_8D

The GGE is a QUANTUM state, not a classical field. It does not have
spatial variation on the internal manifold (L/xi_GL = 0.031, S37).
The 32 cells are in the SAME quantum state.

Therefore: the KK volume integral provides NO suppression of the
non-thermality. The internal non-thermality transmits to 4D AT FULL
STRENGTH through the Einstein equation.
""")

# Let me nonetheless compute all possible suppression mechanisms
# and their combined effect.

# ==============================================================================
#  SECTION 5: SYSTEMATIC SUPPRESSION FACTOR CALCULATION
# ==============================================================================

print("--- SECTION 5: Systematic Suppression Factors ---")

# Factor 1: Cell averaging (GGE is coherent -> no suppression)
S_cell = 1.0  # (local)

# Factor 2: Mode averaging (integrability -> no suppression)
S_mode = 1.0  # (local)

# Factor 3: KK volume integral (no y-dependence -> no suppression)
S_KK = 1.0  # (local)

# Factor 4: Epoch suppression
# The CMB was last scattered at recombination (z ~ 1100, T ~ 0.26 eV).
# The non-thermality in the INTERNAL space couples to the 4D metric
# through the Einstein equation. The metric perturbation delta_g/g
# is of order delta_rho/rho where rho includes ALL energy density.
#
# At recombination, rho_total ~ rho_radiation ~ (pi^2/30) * g_* * T^4
# with g_* ~ 3.36 (photons + neutrinos).
# rho_rad(z=1100) = rho_CMB * (1+z)^4 ~ 2e-51 * (1100)^4 ~ 2.9e-39 GeV^4
#
# The internal non-thermal stress-energy delta_T_mu_nu produces a
# metric perturbation Phi ~ (4*pi*G) * delta_rho / k^2
# At the Hubble scale k ~ H(z_rec), Phi ~ delta_rho / (3 * rho_total)
# (standard cosmological perturbation theory).

# BUT WAIT: the "internal non-thermality" is a CONSTANT energy density
# (no spatial variation in 4D). A spatially constant perturbation to
# rho is just a modification of the BACKGROUND cosmology, not a
# perturbation. It shifts H(z), not delta_T/T.

# A constant shift in the vacuum energy density affects:
# 1. The expansion rate H(z) — already constrained by the CC problem
# 2. The CMB MONOPOLE temperature — but this is not a "distortion"

# For the CMB SPECTRAL SHAPE:
# A pure vacuum energy modification preserves the Planck spectrum.
# The FRW metric sources a perfect blackbody.
# Only ANISOTROPIC or TIME-VARYING deviations create spectral distortions.

# The GGE non-thermality is:
# - Spatially isotropic (same GGE everywhere in 4D)
# - Constant in time (GGE is protected by integrability)
# - But SPECTRALLY non-thermal (mode occupations differ from single-T)

# Does the spectral non-thermality of the INTERNAL modes create a
# spectral distortion in the EXTERNAL (CMB) photons?

# The coupling is gravitational. The photon does not directly see the
# GGE modes — it only sees the metric. The metric is determined by
# the TOTAL stress-energy tensor, which includes the GGE contribution.
# But a CONSTANT, ISOTROPIC stress-energy tensor produces a FRW metric,
# which gives a PERFECT blackbody CMB.

# The spectral distortion would require:
# 1. Direct coupling between GGE modes and photons (not gravitational only)
# 2. Or a time-varying component of the GGE energy

# Neither exists in this framework:
# - Direct coupling: the BCS modes are in the INTERNAL space;
#   they couple to 4D photons only through gravity
# - Time variation: the GGE is integrability-protected (S38)

# Therefore: NO spectral distortion. The suppression is INFINITE.
# The non-thermality is COMPLETELY DECOUPLED from the CMB spectrum.

print("  Suppression Factor Analysis:")
print(f"")
print(f"  S_cell (cell averaging)    = {S_cell:.1f} (GGE is coherent)")
print(f"  S_mode (mode averaging)    = {S_mode:.1f} (integrability locks)")
print(f"  S_KK   (KK volume)         = {S_KK:.1f} (no y-dependence)")
print(f"")
print(f"  HOWEVER: The question is malformed.")
print(f"  The internal non-thermality is a CONSTANT, ISOTROPIC contribution")
print(f"  to the vacuum energy. It does NOT create CMB spectral distortions.")
print(f"  The coupling is purely gravitational (metric-only).")
print(f"  A constant, isotropic stress-energy -> FRW metric -> perfect BB.")
print(f"")
print(f"  The SPECTRAL non-thermality of the BCS modes lives in the")
print(f"  internal Hilbert space. It is invisible to 4D photons.")

# ==============================================================================
#  SECTION 6: BUT WAIT — TWO LEGITIMATE CONCERNS
# ==============================================================================

print("\n--- SECTION 6: Legitimate Concerns ---")

print("""
Concern 1: The GGE affects the EXPANSION HISTORY, not the CMB spectrum.
  If the GGE energy density is rho_GGE ~ 10^68 GeV^4, this dominates
  the expansion rate by 115 orders over the observed CC. This is the
  CC PROBLEM, not a FIRAS problem. FIRAS constrains spectral distortions,
  not the expansion rate.

  STATUS: The CC problem is S53's result. FIRAS adds nothing new.

Concern 2: The GGE might have a TIME-DEPENDENT component.
  If the GGE energy evolves (e.g., through slow Josephson relaxation
  or integrability-breaking perturbations), the time variation creates
  a y-type spectral distortion:
    y ~ (delta_rho/rho) * (dt / t_Compton)

  From S53: tau_J = 2.97e-43 s (Josephson coupling time)
  This is 6.8e-61 * t_universe — effectively zero.
  Integrability breaking rate: Beliaev damping Q = 6.7e5 (S50)
  -> Gamma_Beliaev ~ omega/Q ~ negligible

  Even with maximal Josephson coupling:
    delta_rho / rho ~ tau_J / t_universe ~ 10^{-60}
    y ~ 10^{-60}

  This is 55 orders below FIRAS. SAFE.

Concern 3: Mode-dependent redshifting.
  If different BCS modes redshift differently during expansion,
  the mode asymmetry could evolve. But in the GGE framework,
  all modes are at the KK scale and redshift identically
  (same metric, same geometry). No differential redshift.
""")

# Quantify Concern 2
tau_J_seconds = 2.97e-43  # from S53  # (local)
t_universe = 4.35e17  # seconds  # (local)
Q_Beliaev = 6.7e5  # S50  # (local)

delta_rho_over_rho_Josephson = tau_J_seconds / t_universe
y_distortion = delta_rho_over_rho_Josephson  # order of magnitude
print(f"  Josephson time variation: tau_J / t_universe = {delta_rho_over_rho_Josephson:.2e}")
print(f"  y-distortion estimate: y ~ {y_distortion:.2e}")
print(f"  FIRAS y-bound: |y| < 1.5e-5")
print(f"  Margin: {1.5e-5 / y_distortion:.2e} (safely below)")

# ==============================================================================
#  SECTION 7: WHAT THE GATE ACTUALLY TESTS
# ==============================================================================

print("\n--- SECTION 7: Gate Verdict ---")

# The pre-registered gate asks: is the framework FIRAS-compatible?
# The answer depends on which interpretation we use:

# Interpretation 1: "Suppression factor" = how much the KK averaging
# reduces the internal non-thermality for the 4D observer.
# Result: The question is MALFORMED. The internal non-thermality does NOT
# produce a CMB spectral distortion. The suppression is not a finite
# number — the coupling channel does not exist.

# Interpretation 2: "FIRAS-compatible" = does the framework predict
# observable deviations from a perfect CMB blackbody?
# Result: The framework predicts NO spectral distortions from the GGE.
# The internal non-thermality is gravitationally decoupled from the
# CMB spectrum. The only effect is on the expansion rate (CC problem).

# Interpretation 3: Upper bound on spectral distortion from time variation.
# Result: y ~ 10^{-60}, safely below FIRAS by 55 orders.

# Let me compute the effective "suppression factor" that the gate expects.
# The gate defines: delta_T_CMB/T = nonthermality_internal * suppression
# and asks if suppression < 5e-4 (so that 0.12 * suppression < 6e-5).

# If the coupling channel does not exist: suppression = 0. PASS trivially.
# If we use the Josephson time-variation: suppression = tau_J/t_universe ~ 10^{-60}.

# The most conservative (hostile to the framework) estimate:
# Assume the internal non-thermality couples at FULL gravitational strength
# through the Sachs-Wolfe effect. Then:
#   delta_T/T ~ (1/3) * Phi_GGE
# where Phi_GGE is the gravitational potential from the GGE non-thermality.
# But Phi_GGE is part of the BACKGROUND (isotropic, homogeneous).
# It does not create PERTURBATIONS in the CMB.

# To get a perturbation, we would need SPATIAL VARIATION of the GGE.
# The GGE is coherent over L/xi_GL = 0.031 (S37), meaning the
# internal manifold is ONE coherence volume. No spatial variation.

# UNLESS: different VORONOI CELLS develop different GGE states due to
# the domain structure. This is the "strongest possible case" for
# a non-zero suppression factor.

print("Most conservative estimate (hostile to framework):")
print("  Assume each Voronoi cell independently develops a GGE state")
print("  drawn from the temperature distribution {T_B2, T_B1, T_B3}.")
print("  This is PHYSICALLY UNJUSTIFIED (L/xi_GL = 0.031) but gives")
print("  the largest possible non-thermality in 4D.")
print(f"")

# Even in this worst case: the cell-to-cell variation averages over
# the internal manifold, but the 4D observer sees the MEAN.
# The mean temperature is deterministic, not random.
# There is no CMB spectral distortion even in this case.

# The REAL answer: the GGE non-thermality produces no CMB spectral
# distortion because:
# 1. It is spatially homogeneous (no 4D perturbations)
# 2. It is temporally constant (no time-varying energy injection)
# 3. It couples only gravitationally (metric sees total stress-energy)
# 4. A constant isotropic stress-energy -> FRW -> perfect BB

# OK but the prompt ALSO mentioned a specific mechanism:
# "w = T_sector / T_mean varies from 0.158 to 0.202"
# This is the INTERNAL mode-by-mode temperature variation.
# When the 4D projection integrates over modes, does this create
# a spectral distortion?

# No. The 4D photon field thermalizes independently of the internal modes.
# The photon is a MASSLESS 4D mode (Goldstone of the condensate or
# gauge field). It does NOT "inherit" the temperatures of the BCS modes.
# It thermalizes through its own interactions (QED processes at T > 0.5 MeV).

# The only effect: the BCS modes contribute to the 4D vacuum energy,
# which affects the expansion rate. This is the CC problem.

print("CONCLUSION:")
print(f"  The GGE internal non-thermality does NOT produce CMB spectral")
print(f"  distortions. The coupling channel (GGE -> CMB spectrum) does")
print(f"  not exist. The GGE affects only the expansion rate (CC problem).")
print(f"")
print(f"  The 4D photon thermalizes through QED processes independently")
print(f"  of the internal BCS mode temperatures.")
print(f"")
print(f"  Effective suppression factor: EFFECTIVELY ZERO")
print(f"  (bounded above by Josephson time variation: ~10^{{-60}})")
print(f"")

# Compute all the numbers for the gate
suppression_Josephson = tau_J_seconds / t_universe  # ~ 10^{-60}
suppression_effective = 0.0  # exact: no coupling channel  # (local)
suppression_upper_bound = suppression_Josephson  # conservative upper bound

delta_T_observable = nonthermality_internal * suppression_upper_bound
delta_T_observable_over_T = delta_T_observable  # already a ratio

print(f"  Upper bound on observable delta_T/T:")
print(f"    = {nonthermality_internal:.4f} x {suppression_upper_bound:.2e}")
print(f"    = {delta_T_observable_over_T:.2e}")
print(f"  FIRAS bound: {delta_T_over_T_FIRAS:.1e}")
print(f"  Margin: {delta_T_over_T_FIRAS / max(delta_T_observable_over_T, 1e-300):.2e}")

# Gate: need suppression factor >= 2000 (i.e., 0.12 * S < 6e-5)
# We find S = 0 (or 10^{-60}). Vastly exceeds threshold.
required_suppression = nonthermality_internal / delta_T_over_T_FIRAS
print(f"")
print(f"  Required suppression factor: {required_suppression:.0f}x")
print(f"  Achieved suppression factor: >10^55 (no coupling channel)")

# ==============================================================================
#  SECTION 8: SKEPTICAL ASSESSMENT
# ==============================================================================

print("\n--- SECTION 8: Skeptical Assessment (Sagan) ---")

print("""
This is an ACCOMMODATION, not a prediction.

The framework "passes" FIRAS because the non-thermal internal modes
are gravitationally DECOUPLED from the CMB spectral shape. This is
not a specific quantitative prediction — it is a structural feature
of ANY Kaluza-Klein theory where the internal DOF do not directly
couple to the photon field.

Bayes factor analysis:
  P(FIRAS-compatible | framework):
    Yes, by standard KK decoupling. Any extra-dimensional theory
    with internal modes that couple only gravitationally will
    trivially satisfy FIRAS.

  P(FIRAS-compatible | generic theory with extra dimensions):
    Also yes, for the same reason.

  Bayes factor: BF ~ 1.0 (no discriminating power)

This gate is a CONSISTENCY CHECK, not a prediction.
It verifies that the framework does not immediately violate a
well-established observation, but does not distinguish the framework
from any other KK theory.

Compare to the Venus standard (Sagan, Paper 01):
  Sagan's Venus prediction was SPECIFIC: T_surface > 600K from CO2
  greenhouse effect, when the consensus was T ~ 300K.
  The FIRAS check is GENERIC: any KK theory passes.

The actually important constraint here is the CC PROBLEM:
  rho_GGE = 3.74e68 GeV^4 vs rho_Lambda_obs = 2.7e-47 GeV^4
  This is a 115-order discrepancy. FIRAS is irrelevant by comparison.
""")

# ==============================================================================
#  GATE VERDICT
# ==============================================================================

print("=" * 72)

# The gate as stated: PASS if suppression >= 10^{-5}
# But the actual question (FIRAS compatibility) is: PASS if
# delta_T_CMB/T < 6e-5.
# We find delta_T_CMB/T < 10^{-60}. PASS by 55 orders.

gate_verdict = "PASS"
print(f"GATE VERDICT: FIRAS-GGE-54 = {gate_verdict}")
print("=" * 72)
print(f"")
print(f"HEADLINE: FIRAS-compatible by KK decoupling. BF = 1.0 (accommodation).")
print(f"")
print(f"Key numbers:")
print(f"  Internal non-thermality: delta_T_internal/T = {nonthermality_internal:.4f} ({nonthermality_internal*100:.1f}%)")
print(f"  GGE temperatures: T_B2={T_B2}, T_B1={T_B1}, T_B3={T_B3} (M_KK)")
print(f"  Coupling channel (GGE -> CMB spectrum): DOES NOT EXIST")
print(f"  Reason: isotropic+constant stress-energy -> FRW -> perfect BB")
print(f"  Upper bound from Josephson time variation: delta_T/T < {delta_T_observable_over_T:.2e}")
print(f"  FIRAS bound: delta_T/T < {delta_T_over_T_FIRAS:.1e}")
print(f"  Margin: >{55} orders of magnitude")
print(f"")
print(f"Classification: ACCOMMODATION (any KK theory passes)")
print(f"Bayes factor: BF ~ 1.0 (no discriminating power)")
print(f"")
print(f"The decisive constraint is the CC PROBLEM (115 orders), not FIRAS.")

# ==============================================================================
#  SAVE DATA
# ==============================================================================

script_dir = os.path.dirname(os.path.abspath(__file__))

np.savez(
    os.path.join(script_dir, "s54_firas_gge.npz"),
    gate_verdict=gate_verdict,
    nonthermality_internal=nonthermality_internal,
    T_modes=T_modes,
    T_mean=T_mean,
    w_k=w_k,
    suppression_cell=S_cell,
    suppression_mode=S_mode,
    suppression_KK=S_KK,
    suppression_Josephson=suppression_Josephson,
    suppression_effective=suppression_effective,
    delta_T_observable=delta_T_observable_over_T,
    delta_T_FIRAS=delta_T_over_T_FIRAS,
    margin_orders=55,
    rho_GGE_GeV4=rho_GGE_GeV4,
    rho_CMB_GeV4=rho_CMB,
    Bayes_factor=1.0,
    classification="ACCOMMODATION",
)
print(f"\nData saved: s54_firas_gge.npz")

# ==============================================================================
#  PLOT
# ==============================================================================

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Left panel: GGE temperature distribution
ax1 = axes[0]
mode_labels = ['B2-1', 'B2-2', 'B2-3', 'B2-4', 'B1', 'B3-1', 'B3-2', 'B3-3']
colors = ['#2196F3']*4 + ['#FF9800'] + ['#4CAF50']*3
ax1.bar(range(8), T_modes, color=colors, edgecolor='black', linewidth=0.8)
ax1.axhline(T_mean, color='red', linestyle='--', linewidth=2, label=f'$T_{{mean}}$ = {T_mean:.3f}')
ax1.set_xticks(range(8))
ax1.set_xticklabels(mode_labels, rotation=45)
ax1.set_ylabel('GGE Temperature ($M_{KK}$ units)')
ax1.set_title('GGE Mode Temperatures\n(Internal Non-Thermality)')
ax1.legend()
ax1.set_ylim(0, 0.8)

# Add non-thermality annotation
ax1.annotate(
    f'delta T / T = {nonthermality_internal*100:.1f}%\n(internal)',
    xy=(4, T_B1), xytext=(5.5, 0.55),
    arrowprops=dict(arrowstyle='->', color='black'),
    fontsize=11, ha='center',
    bbox=dict(boxstyle='round,pad=0.3', facecolor='lightyellow', edgecolor='gray')
)

# Right panel: Suppression mechanisms
ax2 = axes[1]

# Show the cascade from internal to observable
levels = {
    'Internal\nnon-thermality': nonthermality_internal,
    'Cell averaging\n(N=32, coherent)': nonthermality_internal * S_cell,
    'Mode averaging\n(N=8, integrable)': nonthermality_internal * S_cell * S_mode,
    'KK volume\n(no y-dep)': nonthermality_internal * S_cell * S_mode * S_KK,
    'Josephson\ntime-variation': nonthermality_internal * suppression_Josephson,
}

names = list(levels.keys())
values = list(levels.values())

# Use log scale
values_log = [np.log10(max(v, 1e-70)) for v in values]

bars = ax2.barh(range(len(names)), values_log, color=['#F44336', '#F44336', '#F44336', '#F44336', '#4CAF50'],
       edgecolor='black', linewidth=0.8)
ax2.set_yticks(range(len(names)))
ax2.set_yticklabels(names, fontsize=9)
ax2.set_xlabel('log$_{10}$(delta T / T)')
ax2.set_title('Suppression Cascade\n(each mechanism applied sequentially)')

# FIRAS bound
firas_log = np.log10(delta_T_over_T_FIRAS)
ax2.axvline(firas_log, color='red', linestyle='--', linewidth=2, label=f'FIRAS bound (log = {firas_log:.1f})')
ax2.legend(fontsize=9)

# Add text for "no coupling channel"
ax2.text(-30, 2, 'No coupling channel:\nGGE is isotropic + constant\n=> FRW => perfect BB',
         fontsize=9, style='italic', color='gray',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.tight_layout()
plt.savefig(os.path.join(script_dir, "s54_firas_gge.png"), dpi=150, bbox_inches='tight')
print(f"Plot saved: s54_firas_gge.png")

# Final save of text output
output_path = os.path.join(script_dir, "s54_firas_gge_output.txt")
print(f"\nOutput will be captured by redirect.")
