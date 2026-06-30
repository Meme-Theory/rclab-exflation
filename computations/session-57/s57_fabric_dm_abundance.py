#!/usr/bin/env python3
"""
FABRIC-DM-ABUNDANCE-57 (W2-4)
=============================
Does Leggett-channel DM match Omega_DM h^2 = 0.120?

Method
------
1. Extract Leggett excitation energy from W1-2 (32-cell parametric calculation)
2. Extract BCS excitation from W1-1, scale to 32 cells using W1-3 gap collapse
3. Compute total DM energy density per Hubble volume
4. Convert to Omega_DM h^2 using M_KK = 7.43e16 GeV

The Leggett channel = relative-phase oscillations between cells.
These are harmonic oscillators parametrically excited during transit.
W1-2 already computed this for 31 Leggett modes on 32 cells.

The BCS channel = quasiparticle pair-breaking within cells.
W1-1 computed P_exc = 0.081 on 2 cells. W1-3 shows the many-body gap
collapses as Delta ~ N^{-1.84}. This ENHANCES BCS excitation at 32 cells.

Scale bridge: M_KK = 7.43e16 GeV (gravity route).
One KZ domain = 32 cells. The Hubble volume contains one domain
(L_domain >> c/H_0 at the fold, inflated to current Hubble volume).

Author: Nazarewicz agent (W2-4)
"""

import numpy as np
import sys
sys.path.insert(0, '.')
from canonical_constants import (
    M_KK, M_KK_gravity, M_KK_kerner,
    N_cells, H_0_GeV, rho_crit_GeV4,
    Omega_DM, Omega_m, Omega_b, Omega_Lambda,
    E_cond, E_exc, n_pairs, N_dof_BCS,
    Delta_0_GL, Delta_0_OES, Delta_B3,
    J_C2, J_su2, J_u1, T_acoustic,
    H_fold, dt_transit, omega_tau,
    E_B1, E_B2_mean, E_B3_mean,
    omega_L1, omega_L2,
    a0_fold, a2_fold, a4_fold,
    PI, rho_Lambda_obs,
    S_fold, xi_BCS, xi_GL,
)

# ============================================================================
#  STEP 0: Load W1 outputs
# ============================================================================

d_w11 = np.load('s57_finite_rate_transit.npz', allow_pickle=True)
d_w12 = np.load('s57_leggett_partition.npz', allow_pickle=True)
d_w13 = np.load('s57_gap_scaling.npz', allow_pickle=True)

print("=" * 72)
print("FABRIC-DM-ABUNDANCE-57 (W2-4)")
print("=" * 72)

# ============================================================================
#  STEP 1: Leggett channel energy (from W1-2, already at 32 cells)
# ============================================================================
# W1-2 computed parametric excitation of 31 Leggett modes during transit.
# Three models were used; we take the S49 model (primary).

E_L_end = float(d_w12['E_L_end_S49'])       # Leggett excitation energy [M_KK]
f_DM_L = float(d_w12['f_DM_end_S49'])       # f_DM from Leggett (= E_L / E_matter)
E_matter = float(d_w12['E_matter'])          # Total matter-sector energy [M_KK]

# Also extract model spread for uncertainty
E_L_GL = float(d_w12['E_L_end_GL'])
E_L_S49_2 = float(d_w12['E_L_end_S49_2'])
E_L_models = np.array([E_L_end, E_L_GL, E_L_S49_2])
E_L_mean = np.mean(E_L_models)
E_L_std = np.std(E_L_models, ddof=1)

print(f"\n--- Step 1: Leggett Channel (32-cell, from W1-2) ---")
print(f"E_L (S49 model)   = {E_L_end:.4f} M_KK")
print(f"E_L (GL model)    = {E_L_GL:.4f} M_KK")
print(f"E_L (S49_2 model) = {E_L_S49_2:.4f} M_KK")
print(f"E_L mean +/- std  = {E_L_mean:.4f} +/- {E_L_std:.4f} M_KK")
print(f"E_matter (fabric) = {E_matter:.4f} M_KK")
print(f"f_DM_Leggett      = {f_DM_L:.6f}")

# ============================================================================
#  STEP 2: BCS channel excitation scaled to 32 cells
# ============================================================================
# W1-1: 2-cell system, P_exc = 0.081, of which 14.1% is Leggett channel.
# The BCS (intra-cell pair-breaking) fraction = 1 - f_Leggett = 85.9%.
#
# W1-3: The many-body gap collapses as Delta_N ~ A * N^alpha with alpha = -1.84.
# At N=2: gap_A = 0.370 M_KK. At N=32: gap_A = 0.025 M_KK (15x smaller).
#
# For LZ transitions, P_LZ = exp(-pi * gamma) with gamma = Delta^2 / (2 * v * dE/dtau).
# Smaller gap -> smaller gamma -> larger P_exc.
#
# BUT: The W1-1 P_exc = 0.081 is from the OVERLAP DEFICIT, not pure LZ.
# It includes contributions from all avoided crossings along the transit path.
# The correct scaling uses the adiabaticity parameter.
#
# CRITICAL OBSERVATION from W1-3 data:
# P_exc_A is CONSTANT (0.01182) for all N from 1 to 32.
# P_exc_B is CONSTANT (~2.4e-5) for all N.
# This means the gap_scaling script computed P_exc from ground-state overlaps
# at FIXED tau points, NOT from dynamical transit. The P_exc there is a STATIC
# overlap measure, not the transit excitation probability.
#
# The DYNAMICAL P_exc must be recomputed using the LZ formula with the 32-cell gap.

P_exc_2cell = float(d_w11['P_exc_final'])       # 0.081 (2-cell, dynamical)
f_Leggett = float(d_w11['ch_f_Leggett'])        # 0.141 (Leggett fraction of 2-cell excitation)
E_exc_2cell = float(d_w11['ch_E_exc'])           # 0.160 M_KK (total excitation, 2-cell)

# BCS portion of 2-cell excitation
f_BCS_2cell = 1.0 - f_Leggett                    # 0.859
E_BCS_2cell = E_exc_2cell * f_BCS_2cell           # ~0.137 M_KK

# Gap values from W1-3
gap_2cell_A = float(d_w13['gap_A_N2'])            # 0.370 M_KK (Model A, at fold)
gap_32cell_A = float(d_w13['gap_A_N32'])          # 0.025 M_KK
gap_2cell_B = float(d_w13['gap_B_N2'])            # 2.352 M_KK (Model B enhanced by J)
gap_32cell_B = float(d_w13['gap_B_N32'])          # 0.085 M_KK
alpha_phys = float(d_w13['alpha_physical'])       # -1.84

# Transit velocity (from W1-1)
dtau_dt = float(d_w11['dtau_dt_phys'])            # 442.4 M_KK

# For LZ scaling, the adiabaticity parameter gamma ~ Delta^2 / (rate * coupling).
# At 2 cells, P_exc = 0.081.
# The BCS part is P_BCS_2cell = P_exc_2cell * f_BCS_2cell = 0.081 * 0.859 = 0.070.
#
# However, the 32-cell BCS excitation is a PER-CELL quantity: each cell independently
# undergoes pair-breaking. The number of cells increases from 2 to 32, but the
# per-cell pair-breaking probability depends on the INTRA-CELL gap, not the
# inter-cell many-body gap.
#
# The intra-cell BCS gap is the SINGLE-CELL gap = 0.370 M_KK (same for all N in Model A).
# The many-body gap that collapses is the Josephson BAND gap (Model A at large N),
# which governs COLLECTIVE excitations (Leggett modes), not single-cell pair-breaking.
#
# This is a critical distinction:
# - Leggett modes: governed by inter-cell Josephson coupling, gap collapses with N
# - BCS pair-breaking: governed by intra-cell pairing gap, does NOT collapse with N
#
# Therefore: BCS excitation per cell is UNCHANGED at 32 cells.
# Total BCS excitation = 32 cells * (per-cell BCS excitation)

# Per-cell BCS excitation energy
# W1-1 had 2 cells with 8 modes each (16 total), N_pair = 2 (1 per cell)
# E_BCS per cell at 2-cell calculation = E_BCS_2cell / 2
E_BCS_per_cell = E_BCS_2cell / 2.0

# Total BCS on 32-cell fabric
E_BCS_32 = N_cells * E_BCS_per_cell

print(f"\n--- Step 2: BCS Channel Scaling ---")
print(f"P_exc (2-cell, dynamical) = {P_exc_2cell:.6f}")
print(f"f_Leggett (2-cell)        = {f_Leggett:.4f}")
print(f"f_BCS (2-cell)            = {f_BCS_2cell:.4f}")
print(f"E_exc total (2-cell)      = {E_exc_2cell:.6f} M_KK")
print(f"E_BCS (2-cell)            = {E_BCS_2cell:.6f} M_KK")
print(f"E_BCS per cell            = {E_BCS_per_cell:.6f} M_KK")
print(f"E_BCS (32-cell)           = {E_BCS_32:.4f} M_KK")
print(f"Gap (single-cell, fold)   = {gap_2cell_A:.6f} M_KK (unchanged)")
print(f"Gap (32-cell, Model A)    = {gap_32cell_A:.6f} M_KK (Josephson band gap)")
print(f"Gap (32-cell, Model B)    = {gap_32cell_B:.6f} M_KK (full model)")

# ============================================================================
#  STEP 2b: Enhanced Leggett excitation from gap collapse
# ============================================================================
# The W1-2 Leggett calculation used specific mode frequencies.
# The gap collapse from W1-3 affects the Leggett mode spectrum.
# At 32 cells, the lowest Leggett mode has omega ~ Delta_32.
# If the gap collapses, modes become softer -> more excitation.
#
# W1-2 already computed with 31 Leggett modes on the 32-cell fabric,
# using the Josephson-derived frequencies. So it ALREADY includes the
# mode structure. No additional gap-collapse correction needed for Leggett.
# The gap_scaling in W1-3 measures the MANY-BODY gap (E_1-E_0), which
# for the Leggett system is the lowest Leggett mode frequency.
#
# Cross-check: omega_L1 = 0.138 M_KK (canonical, from S52).
# W1-2 omega_i_S49[0] should be comparable.
omega_L_lowest_w12 = float(d_w12['omega_i_S49'][0])
print(f"\nCross-check: omega_L1 (canonical) = {omega_L1:.4f} M_KK")
print(f"             omega_i_S49[0] (W1-2) = {omega_L_lowest_w12:.4f} M_KK")

# ============================================================================
#  STEP 3: Total DM energy per KZ domain
# ============================================================================
# One KZ domain = 32 cells (canonical from S42).
# DM = Leggett excitations + BCS quasiparticle excitations
# Both are "dark" because they are internal-space excitations invisible to
# 4D gauge interactions (they live in the SU(3) fiber, not on M4).

E_DM_Leggett = E_L_end        # 1.359 M_KK (from W1-2, 32-cell)
E_DM_BCS = E_BCS_32           # 32 * E_BCS_per_cell
E_DM_total = E_DM_Leggett + E_DM_BCS

# Also compute the total excitation energy (not just DM)
# W1-2's E_BCS_exc = 60.625 M_KK is the full BCS excitation from sudden quench
# Our E_BCS_32 = 2.19 M_KK is from the actual transit (P_exc = 0.081, f_BCS = 0.86)
# The ratio E_BCS_32/E_BCS_exc_w12 tells us the "realized" fraction

E_BCS_exc_sudden = float(d_w12['E_BCS_exc'])

print(f"\n--- Step 3: Total DM Energy per Domain ---")
print(f"E_DM (Leggett)     = {E_DM_Leggett:.4f} M_KK")
print(f"E_DM (BCS qp)      = {E_DM_BCS:.4f} M_KK")
print(f"E_DM (total)        = {E_DM_total:.4f} M_KK")
print(f"f_Leggett/total_DM  = {E_DM_Leggett/E_DM_total:.4f}")
print(f"f_BCS/total_DM      = {E_DM_BCS/E_DM_total:.4f}")
print(f"E_BCS_sudden (W1-2) = {E_BCS_exc_sudden:.2f} M_KK")
print(f"Realized fraction   = {E_BCS_32/E_BCS_exc_sudden:.4f}")

# ============================================================================
#  STEP 4: Scale bridge — energy density in physical units
# ============================================================================
# The framework's spectral action gives the effective Friedmann equation:
#   H^2 = (8*pi*G/3) * rho_total
# where rho_total includes contributions from:
#   - Spectral action (geometric, gives CC + kinetic + potential)
#   - BCS condensation (pairing energy)
#   - Transit excitations (DM + visible matter)
#
# The total energy per domain is E_matter = 11.40 M_KK (from W1-2).
# This is the MATTER-SECTOR energy (kinetic + Josephson + BCS + BA phonons).
#
# The DM FRACTION is:
#   f_DM = E_DM / E_matter
#
# The observed DM fraction of total matter is:
#   Omega_DM / Omega_m = 0.266 / 0.315 = 0.844
#
# If E_matter maps to Omega_m, then:
#   Omega_DM_pred = f_DM * Omega_m
#   Omega_DM_h2_pred = f_DM * Omega_m * h^2

# h from H_0 = 67.4 km/s/Mpc
h_hubble = 0.674

# DM fraction of matter
f_DM_fabric = E_DM_total / E_matter

# Predicted Omega_DM h^2
Omega_DM_h2_pred = f_DM_fabric * Omega_m * h_hubble**2

# Observed
Omega_DM_h2_obs = Omega_DM * h_hubble**2

# Ratio
ratio = Omega_DM_h2_pred / Omega_DM_h2_obs

print(f"\n--- Step 4: Omega_DM h^2 (Ratio Method) ---")
print(f"E_DM / E_matter = f_DM = {f_DM_fabric:.6f}")
print(f"Omega_m = {Omega_m}")
print(f"h = {h_hubble}")
print(f"Omega_DM h^2 (predicted) = {Omega_DM_h2_pred:.6f}")
print(f"Omega_DM h^2 (observed)  = {Omega_DM_h2_obs:.6f}")
print(f"Ratio (pred/obs)         = {ratio:.4f}")

# ============================================================================
#  STEP 5: Absolute density calculation (independent cross-check)
# ============================================================================
# Convert to physical GeV^4 density using M_KK.
#
# The energy per domain in M_KK units must be converted to a density.
# E_domain [M_KK] * M_KK [GeV] gives E_domain [GeV].
# But density requires dividing by volume.
#
# Domain volume: Each cell has volume ~ (1/M_KK)^3 (KK size).
# 32 cells -> V_domain = 32 / M_KK^3.
# Energy density: rho = E_DM * M_KK / V_domain = E_DM * M_KK^4 / 32.
#
# But this is the density at the FOLD (tau_fold, z ~ 3.65).
# It must be diluted to today by (1+z)^3 for matter-like DM.
# Or: we use the fraction method, which is redshift-independent.
#
# The absolute method has additional systematic uncertainty from the
# volume normalization. The fraction method is more robust because
# both numerator and denominator are in M_KK units and the ratio
# is dimensionless.
#
# Nevertheless, let's compute the absolute density for completeness.

# Energy density at fold (in M_KK^4)
rho_DM_MKK4 = E_DM_total / 32.0   # per cell volume = 1/M_KK^3, so rho = E*M_KK/V = E*M_KK^4/N

# Convert to GeV^4
rho_DM_GeV4_fold = rho_DM_MKK4 * M_KK**4

# Dilute to today: factor of (1+z_fold)^3
# z_fold corresponds to tau_fold. From phi_paasch: z = 3.65 at tau = 0.15.
# tau_fold = 0.194. Extrapolating: z_fold ~ 2.8 (approximate).
# But the REAL dilution is from the fold to today, through the full expansion history.
# The ratio method avoids this entirely.

# Using a more careful estimate:
# The spectral action fold at tau_fold = 0.194 maps to some z_fold.
# From S12: m_{(3,0)}/m_{(0,0)} = 1.5316 at tau = 0.15 (z = 3.65).
# The transit happens around tau_fold, but the DM is produced during the transit
# and then dilutes like matter.
# For the absolute calculation, what matters is rho_DM(today).
# rho_DM(today) = rho_DM(fold) * (a_fold/a_0)^3 = rho_DM(fold) / (1+z_fold)^3.
#
# But z_fold is not well-constrained. This is the scale bridge uncertainty.
# The ratio method CANCELS this factor because both DM and baryonic matter
# dilute the same way (both are ~pressureless post-transit).

print(f"\n--- Step 5: Absolute Density (Cross-Check) ---")
print(f"rho_DM at fold = {rho_DM_MKK4:.6e} M_KK^4")
print(f"rho_DM at fold = {rho_DM_GeV4_fold:.4e} GeV^4")
print(f"rho_crit       = {rho_crit_GeV4:.4e} GeV^4")
print(f"NOTE: Absolute density is at the fold, not today.")
print(f"      Ratio method (Step 4) is the robust comparison.")

# ============================================================================
#  STEP 6: Uncertainty budget
# ============================================================================
# Sources of uncertainty:
# 1. Leggett model spread: 3 models give E_L = 1.02-1.36 M_KK
# 2. BCS per-cell scaling: assumes independent cells (no inter-cell correlation)
# 3. M_KK scale: 0.83-decade tension between gravity and Kerner routes
# 4. E_matter normalization: from fabric free energy, depends on E_J and BCS
# 5. Leggett fraction f_L: W1-1 gives 14.1% on 2-cell; may differ at 32 cells
# 6. Transit rate: physical rate vs critical rate (4400x above, W1-1)

# Error from Leggett model spread
E_DM_min = min(E_L_models) + E_BCS_32
E_DM_max = max(E_L_models) + E_BCS_32
f_DM_min = E_DM_min / E_matter
f_DM_max = E_DM_max / E_matter
Omega_DM_h2_min = f_DM_min * Omega_m * h_hubble**2
Omega_DM_h2_max = f_DM_max * Omega_m * h_hubble**2
ratio_min = Omega_DM_h2_min / Omega_DM_h2_obs
ratio_max = Omega_DM_h2_max / Omega_DM_h2_obs

# Error from M_KK (affects absolute density, not ratio)
ratio_MKK = M_KK_kerner / M_KK_gravity  # 6.79x

# Error from including ZPE (upper bound)
E_DM_ZPE = float(d_w12['ZPE_L_fold']) + E_BCS_32
f_DM_ZPE = E_DM_ZPE / E_matter
Omega_DM_h2_ZPE = f_DM_ZPE * Omega_m * h_hubble**2
ratio_ZPE = Omega_DM_h2_ZPE / Omega_DM_h2_obs

# BA parametric (upper bound from Bogoliubov-Anderson phonon channel)
E_DM_BA = float(d_w12['E_BA_parametric']) + E_DM_BCS
f_DM_BA = E_DM_BA / E_matter
Omega_DM_h2_BA = f_DM_BA * Omega_m * h_hubble**2
ratio_BA = Omega_DM_h2_BA / Omega_DM_h2_obs

print(f"\n--- Step 6: Uncertainty Budget ---")
print(f"{'Source':<30s} {'f_DM':>8s} {'Omega_DM h^2':>14s} {'Ratio':>8s}")
print("-" * 66)
print(f"{'Leggett (S49, central)':<30s} {f_DM_fabric:>8.4f} {Omega_DM_h2_pred:>14.6f} {ratio:>8.4f}")
print(f"{'Leggett (GL, lower)':<30s} {f_DM_min:>8.4f} {Omega_DM_h2_min:>14.6f} {ratio_min:>8.4f}")
print(f"{'Leggett (S49, upper)':<30s} {f_DM_max:>8.4f} {Omega_DM_h2_max:>14.6f} {ratio_max:>8.4f}")
print(f"{'ZPE-inclusive Leggett':<30s} {f_DM_ZPE:>8.4f} {Omega_DM_h2_ZPE:>14.6f} {ratio_ZPE:>8.4f}")
print(f"{'BA parametric (upper)':<30s} {f_DM_BA:>8.4f} {Omega_DM_h2_BA:>14.6f} {ratio_BA:>8.4f}")
print(f"{'Observed':<30s} {'---':>8s} {Omega_DM_h2_obs:>14.6f} {'1.0000':>8s}")

# ============================================================================
#  STEP 7: Gate classification
# ============================================================================
# PASS: within factor 3 of 0.120
# FAIL: off by > 10x
# INFO: depends on unresolved scale bridge

# Check factor-of-3 criterion
obs_val = 0.120  # (local)
factor = Omega_DM_h2_pred / obs_val
in_factor_3 = (1.0/3.0 <= factor <= 3.0)
off_by_10x = (factor < 0.1) or (factor > 10.0)

# The ratio method gives the FRACTIONAL prediction.
# But the absolute Omega_DM h^2 depends on whether E_matter maps to Omega_m.
# This mapping is the SCALE BRIDGE assumption.
# The assumption is that the matter-sector energy (kinetic + Josephson + BCS + BA)
# IS the total matter density, and DM is the non-baryonic fraction of that.
#
# This is a STRUCTURAL assumption, not a parameter. It either holds or it doesn't.
# If it holds, the prediction is Omega_DM h^2 = f_DM * Omega_m * h^2.
# If it doesn't, the prediction is undefined.
#
# Under this assumption:
# - Central value: ratio = f_DM = 0.338 -> Omega_DM h^2 = 0.048 -> ratio 0.40
# - With model spread: 0.36 - 0.46
# - Observation: 0.120

# HOWEVER: the KEY question is whether Omega_DM / Omega_m or
# Omega_DM / Omega_total is the right comparison.
# Omega_DM h^2 = 0.120 is measured from CMB.
# If our f_DM = E_DM / E_matter, and E_matter -> total energy density rho_total
# (not just Omega_m), then:
# Omega_DM = f_DM, and Omega_DM h^2 = f_DM * h^2

# Let's also try the DIRECT interpretation: E_DM / E_total_domain = Omega_DM
# where E_total_domain includes everything (matter, radiation, Lambda).
# At the fold, the total energy is dominated by:
# T_kin (kinetic) = 597 M_KK >> everything else.
# F_Josephson = -337 M_KK (negative, potential energy).
# The total is complex; the matter energy is a DERIVED quantity.

# Most conservative: use fraction of matter-sector energy.
# f_DM = E_DM / E_matter = 0.34 (central).
# Then Omega_DM h^2_pred depends on interpretation:

# Interpretation A: Omega_DM h^2 = f_DM * Omega_m * h^2 = 0.049
# (DM is a fraction of total matter, observed Omega_m sets the scale)
Omega_DM_h2_A = f_DM_fabric * Omega_m * h_hubble**2
ratio_A = Omega_DM_h2_A / obs_val

# Interpretation B: Omega_DM = f_DM directly (DM fraction of TOTAL density)
# Omega_DM h^2 = f_DM * h^2
Omega_DM_h2_B = f_DM_fabric * h_hubble**2
ratio_B = Omega_DM_h2_B / obs_val

# Interpretation C: f_DM is Omega_DM / Omega_total = Omega_DM
# This gives Omega_DM h^2 = f_DM * h^2 = same as B
# But here, f_DM = E_DM / E_total (E_total = all energy in domain)

# The W1-2 definition: f_DM = E_L / E_matter where E_matter = 11.40 M_KK
# includes Josephson + BCS + BA + kinetic contributions.
# This is closer to "total matter" than "total energy" because it excludes
# the spectral action vacuum energy (which -> Lambda).

print(f"\n--- Step 7: Gate Assessment ---")
print(f"\nInterpretation A (f_DM * Omega_m * h^2):")
print(f"  Omega_DM h^2 = {Omega_DM_h2_A:.6f}")
print(f"  Ratio to obs  = {ratio_A:.4f}")
print(f"  Within x3?    = {1/3 <= ratio_A <= 3}")

print(f"\nInterpretation B (f_DM * h^2, DM = fraction of total):")
print(f"  Omega_DM h^2 = {Omega_DM_h2_B:.6f}")
print(f"  Ratio to obs  = {ratio_B:.4f}")
print(f"  Within x3?    = {1/3 <= ratio_B <= 3}")

# The physical picture:
# E_matter = 11.40 M_KK per domain. Of this:
# E_DM = 3.56 M_KK is dark (Leggett + BCS qp, does not couple to photons)
# E_visible = E_matter - E_DM = 7.84 M_KK is visible (couples to gauge fields)
#
# The ratio E_DM / E_visible = Omega_DM / Omega_b:
E_visible = E_matter - E_DM_total
DM_to_visible = E_DM_total / E_visible
DM_to_visible_obs = Omega_DM / Omega_b  # 0.266 / 0.0493 = 5.40

# Actually, E_visible includes EVERYTHING that isn't DM in the matter sector.
# Not all of it is baryonic. In the framework:
# - BCS condensate energy -> vacuum (Lambda-like)
# - Josephson energy -> vacuum (Lambda-like)
# - BA phonons -> radiation or matter depending on mass
# - Transit quasiparticles (non-DM) -> visible matter (baryons)
#
# The baryon sector is the non-DM, non-vacuum excitation.
# This is highly model-dependent. Let's not go there.

# Final gate: use Interpretation A (most conservative).
# ratio_A = 0.40 -> within factor 3 of observation. PASS.

if 1.0/3.0 <= ratio_A <= 3.0:
    gate_verdict = "PASS"
    gate_detail = f"Omega_DM h^2 = {Omega_DM_h2_A:.4f}, ratio = {ratio_A:.2f} (within 3x of 0.120)"
elif ratio_A < 0.1 or ratio_A > 10.0:
    gate_verdict = "FAIL"
    gate_detail = f"Omega_DM h^2 = {Omega_DM_h2_A:.4f}, ratio = {ratio_A:.2f} (> 10x from 0.120)"
else:
    gate_verdict = "INFO"
    gate_detail = f"Omega_DM h^2 = {Omega_DM_h2_A:.4f}, ratio = {ratio_A:.2f} (between 3x and 10x)"

print(f"\n{'='*72}")
print(f"GATE VERDICT: {gate_verdict}")
print(f"  {gate_detail}")
print(f"{'='*72}")

# ============================================================================
#  STEP 8: Nuclear analog assessment
# ============================================================================
# In nuclear physics, the equivalent problem is:
# Given a compound nucleus with excitation energy E*, what fraction goes
# into specific decay channels?
#
# The Leggett channel is analogous to collective vibrations (GDR, GQR).
# The BCS channel is analogous to quasiparticle (evaporative) excitation.
# In nuclear reactions at E* ~ 10 MeV/nucleon:
# - Collective modes carry 10-20% of the energy (EWSR fraction)
# - Quasiparticle emission carries 60-80%
# - Pre-equilibrium carries 10-20%
#
# Our f_Leggett/f_total ~ 38% is HIGHER than typical nuclear collective
# fractions, but consistent with a system near a phase transition where
# collective modes soften.

print(f"\n--- Step 8: Nuclear Analog ---")
print(f"f_Leggett/f_DM_total = {E_DM_Leggett/E_DM_total:.3f}")
print(f"Nuclear analog: collective/total ~ 0.10-0.20 (at moderate E*)")
print(f"Framework value is 2x nuclear, consistent with phase-transition softening")
print(f"BCS analog: evaporative fraction = {E_DM_BCS/E_DM_total:.3f}")
print(f"Nuclear analog: evaporative/total ~ 0.60-0.80")
print(f"Framework BCS fraction LOWER than nuclear (fewer available qp modes)")

# ============================================================================
#  SAVE
# ============================================================================

results = {
    # Inputs
    'E_L_end_S49': E_L_end,
    'E_L_end_GL': E_L_GL,
    'E_L_end_S49_2': E_L_S49_2,
    'E_L_mean': E_L_mean,
    'E_L_std': E_L_std,
    'E_BCS_per_cell': E_BCS_per_cell,
    'E_BCS_32': E_BCS_32,
    'E_matter': E_matter,
    'P_exc_2cell': P_exc_2cell,
    'f_Leggett_2cell': f_Leggett,

    # Gap scaling
    'gap_2cell_A': gap_2cell_A,
    'gap_32cell_A': gap_32cell_A,
    'gap_32cell_B': gap_32cell_B,
    'alpha_physical': alpha_phys,

    # DM energies
    'E_DM_Leggett': E_DM_Leggett,
    'E_DM_BCS': E_DM_BCS,
    'E_DM_total': E_DM_total,
    'f_DM_fabric': f_DM_fabric,
    'f_Leggett_of_DM': E_DM_Leggett / E_DM_total,
    'f_BCS_of_DM': E_DM_BCS / E_DM_total,

    # Cosmological observables
    'Omega_DM_h2_pred_A': Omega_DM_h2_A,  # f_DM * Omega_m * h^2
    'Omega_DM_h2_pred_B': Omega_DM_h2_B,  # f_DM * h^2
    'Omega_DM_h2_obs': Omega_DM_h2_obs,
    'ratio_A': ratio_A,
    'ratio_B': ratio_B,
    'h_hubble': h_hubble,

    # Uncertainty envelope
    'Omega_DM_h2_min': Omega_DM_h2_min,
    'Omega_DM_h2_max': Omega_DM_h2_max,
    'ratio_min': ratio_min,
    'ratio_max': ratio_max,
    'Omega_DM_h2_ZPE': Omega_DM_h2_ZPE,
    'ratio_ZPE': ratio_ZPE,
    'Omega_DM_h2_BA': Omega_DM_h2_BA,
    'ratio_BA': ratio_BA,

    # Absolute density
    'rho_DM_MKK4': rho_DM_MKK4,
    'rho_DM_GeV4_fold': rho_DM_GeV4_fold,

    # Gate
    'gate_name': 'FABRIC-DM-ABUNDANCE-57',
    'gate_verdict': gate_verdict,
    'gate_detail': gate_detail,
}

np.savez('s57_fabric_dm_abundance.npz', **results)
print(f"\nSaved: s57_fabric_dm_abundance.npz")
print("DONE")
