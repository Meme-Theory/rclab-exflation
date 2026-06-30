#!/usr/bin/env python3
"""
PENROSE-SUPERRAD-60: Superradiance Analogy — B2 Mode Energy Extraction from B3 Ergosphere
===========================================================================================
Gate: PENROSE-SUPERRAD-60
  PASS: total extraction * t_universe > Lambda_eff
  FAIL: total extraction * t_universe << Lambda_eff (negligible)
  INFO: non-negligible but insufficient alone

Physics:
  The Penrose process in rotating black holes extracts energy via negative-energy
  orbits inside the ergosphere. The analog here: the RG Hessian at alpha_total > alpha_crit
  develops a negative eigenvalue (lambda_alpha = -15.60), creating a B3 "ergosphere" where
  effective quasiparticle energies can be negative.

  Superradiance condition (Zel'dovich 1971, my Paper 05 / Starobinsky amplification):
    omega < m * Omega_H  =>  E_eff(k) = E_k - q_7(k) * Phi_7 < 0
  where Phi_7 plays the role of the angular velocity Omega_H of the horizon, and
  q_7(k) is the U(1)_7 charge of mode k. The [iK_7, D_K] = 0 theorem means K_7
  is an exact quantum number (Session 34 permanent result).

  Cooper pairs carry K_7 = +/- 1/2. The chemical potential for K_7 charge in the
  ergosphere is Phi_7 = |lambda_alpha| / (8*pi*M_eff), the analog of the BH horizon
  angular velocity kappa/(8*pi*M) appearing in the first law dM = (kappa/8pi)dA + Omega_H dJ.

  Extraction rate per mode (Bogoliubov coefficient |beta_k|^2 for superradiant scattering):
    Gamma_SR(k) = |lambda_alpha| * |<k|V_B2B3|k'>|^2 * Theta(-E_eff(k))
  where V_B2B3 is the B2-B3 coupling from V_bare_cont, and Theta is the Heaviside function.

  Total CC reduction rate: dLambda/dt = sum_k Gamma_SR(k) * |E_eff(k)|

Inputs:
  - computations/session-59/s59_penrose_access.npz
  - computations/session-54/s54_ed_sweep.npz
  - canonical_constants.py

Session: S60, Gate: PENROSE-SUPERRAD-60
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
import sys

# Change to project root
os.chdir("C:/sandbox/Ainulindale Exflation")
sys.path.insert(0, "computations")
from canonical_constants import *

# ==============================================================================
# STEP 0: Load input data
# ==============================================================================

log_lines = []
def log(msg):
    log_lines.append(msg)
    print(msg)

log("=" * 78)
log("PENROSE-SUPERRAD-60: Superradiance Analogy for CC Extraction")
log("=" * 78)

# Load S59 Penrose access results
pa = np.load("computations/session-59/s59_penrose_access.npz", allow_pickle=True)
ed = np.load("computations/session-54/s54_ed_sweep.npz", allow_pickle=True)

alpha_total = float(pa['alpha_total'])
alpha_crit_val = float(pa['alpha_crit'])
lambda_alpha_val = float(pa['lambda_alpha'])   # = -15.595
lambda_0_val = float(pa['lambda_0'])           # = +2.835 (at alpha=0)
lambda_1_val = float(pa['lambda_1'])           # = -30.39 (at alpha=1)
Gamma_Penrose_s59 = float(pa['Gamma_Penrose']) # = 0.355 (S59 rate)
overlap_factor = float(pa['overlap_factor'])

N_modes = int(ed['N_modes'])       # = 8
fold_idx = int(ed['fold_idx'])     # = 19
tau_fold_val = float(ed['tau_values'][fold_idx])

# Single-particle spectrum at the fold
E_sp_fold = ed['E_sp_sweep'][fold_idx]  # shape (8,)
pair_occ_fold = ed['pair_occupations'][fold_idx]  # shape (8,)
V_bare = ed['V_bare_cont']  # shape (8, 8)

# Ground state energy at fold
E0_fold = float(ed['E0'][fold_idx])

log(f"\n--- Input Summary ---")
log(f"alpha_total = {alpha_total:.6f} (PASS threshold: {alpha_crit_val:.4f})")
log(f"lambda_alpha = {lambda_alpha_val:.4f} (negative => ergosphere open)")
log(f"N_modes = {N_modes}, tau_fold = {tau_fold_val:.4f}")
log(f"E_sp at fold: {E_sp_fold}")
log(f"pair_occ at fold: {pair_occ_fold}")
log(f"E0 (ground) = {E0_fold:.6f} M_KK")
log(f"V_bare shape = {V_bare.shape}")

# ==============================================================================
# STEP 1: Mode classification (B1, B2, B3) and K_7 charge assignment
# ==============================================================================

log("\n" + "=" * 78)
log("STEP 1: Mode classification and K_7 charge assignment")
log("=" * 78)

# From framework established results:
# 8 modes = 4 B2 + 1 B1 + 3 B3
# B2: modes 0-3 (lowest energy, near-degenerate at fold — van Hove)
# B1: mode 4 (E ~ 0.819 M_KK)
# B3: modes 5-7 (E ~ 0.98 M_KK)
#
# K_7 charge: [iK_7, D_K] = 0 theorem (Session 34)
# Cooper pairs carry K_7 = +/- 1/2
# B2 modes: q_7 = 0 (self-conjugate, (1,1) rep has weight with q_7=0)
# B1 mode: q_7 = +/- 1 (transforms under U(1)_7)
# B3 modes: q_7 = +/- 1 (transforms under U(1)_7)
#
# More precisely, from the Gell-Mann matrix lambda_7 eigenvalues on each sector:
# B2 (adjoint (1,1)): q_7 values include 0
# B1 (fundamental (1,0)): q_7 = ±1/2, ±1 depending on weight
# B3 (fundamental (0,1)): q_7 = ±1/2, ±1

# For the 8-mode BCS space, the pairing is between time-reversed pairs.
# The K_7 charge per mode comes from the Dirac spectrum structure.
# From S34 [iK_7, D_K]=0 and the Jensen deformation:

# Assign charges based on sector structure
# B2 sector: 4 modes, all have q_7 = 0 (K_7 commutes with D_K, B2 is self-conjugate)
# B1 sector: 1 mode, q_7 = 1 (from (1,0) weight structure)
# B3 sector: 3 modes, q_7 = -1, 0, +1 (from (0,1) = conjugate of (1,0))

mode_labels = ['B2_0', 'B2_1', 'B2_2', 'B2_3', 'B1', 'B3_0', 'B3_1', 'B3_2']
sector_ids = ['B2', 'B2', 'B2', 'B2', 'B1', 'B3', 'B3', 'B3']

# K_7 charges from the established SU(3) representation theory
# B2 (adjoint, (1,1)): all weights have q_7 from {-1, -1/2, 0, +1/2, +1}
# But the 4 B2 modes used in BCS pairing are the gap-edge modes near the van Hove singularity
# These are the q_7=0 doublet and q_7=±1/2 pair.
# For the BCS pairing: Cooper pairs (k, -k) have total q_7=0.
# Individual quasiparticle excitations carry the bare q_7.

# From the eigenstate structure at the fold, the q_7 values are:
q_7 = np.array([0.0, 0.5, -0.5, 0.0,   # B2: two with q_7=0, two with q_7=±1/2
                 1.0,                      # B1: q_7=1
                 -1.0, 0.0, 1.0])         # B3: q_7 = -1, 0, +1

for i in range(N_modes):
    log(f"  Mode {i} ({mode_labels[i]}): E_sp = {E_sp_fold[i]:.6f}, "
        f"q_7 = {q_7[i]:+.1f}, n_pair = {pair_occ_fold[i]:.6f}")

# ==============================================================================
# STEP 2: Compute E_eff(k) = E_k - q_7(k) * Phi_7 for each mode
# ==============================================================================

log("\n" + "=" * 78)
log("STEP 2: Effective energy with ergosphere chemical potential Phi_7")
log("=" * 78)

# The Penrose process analog: the ergosphere has a chemical potential Phi_7
# for K_7 charge, analogous to Omega_H for angular momentum in Kerr BHs.
#
# From the first law of BH mechanics (my Paper 04):
#   dM = (kappa/8pi) dA + Omega_H dJ + Phi_H dQ
#
# The analog first law for the BCS ergosphere (S43 FIRSTLAW-43 PASS):
#   dE_spec = T_eff dS_spec + Phi_7 dQ_7 + X_tau dtau
#
# S43 established Phi_7 = 0 for the equilibrium GGE. But inside the ergosphere
# (lambda_alpha < 0), there IS a chemical potential for K_7 because the Hessian
# negative eigenvalue direction involves B2->B3 transfer, and B3 modes carry q_7 != 0.
#
# The ergosphere Phi_7 is determined by the Hessian eigenstructure:
# lambda_alpha = -15.595 is the curvature of the free energy along the
# B2->B3 transfer direction. The chemical potential driving this transfer is:
#
#   Phi_7 = |lambda_alpha| * delta_n / delta_Q_7
#
# where delta_n is the occupation change and delta_Q_7 is the charge change
# per unit transfer. For B2(q_7=0) -> B3(q_7=±1): delta_Q_7/delta_n = ±1.
#
# So Phi_7 = |lambda_alpha| * v_transfer, where v_transfer is the
# "velocity" in occupation space — the Hessian eigenvector component.
#
# From the Hessian structure, the critical eigenvector has components:
# primarily along n_B3 direction, with amplitude ~ overlap_factor = 0.70
# Phi_7_ergo = |lambda_alpha| * overlap_factor * (Delta_B3 / E_B3_mean)

Phi_7_ergo = abs(lambda_alpha_val) * overlap_factor * (Delta_B3 / E_B3_mean)
log(f"  |lambda_alpha| = {abs(lambda_alpha_val):.4f}")
log(f"  overlap_factor = {overlap_factor:.4f}")
log(f"  Delta_B3 = {Delta_B3:.4f} M_KK")
log(f"  E_B3_mean = {E_B3_mean:.6f} M_KK")
log(f"  Phi_7 (ergosphere) = {Phi_7_ergo:.6f} M_KK")

# Effective energy: E_eff(k) = E_sp(k) - q_7(k) * Phi_7
E_eff = E_sp_fold - q_7 * Phi_7_ergo

log(f"\n  Mode-by-mode effective energies:")
log(f"  {'Mode':<8} {'E_sp':>10} {'q_7':>6} {'q_7*Phi_7':>12} {'E_eff':>12} {'SR?':>5}")
log(f"  {'-'*8} {'-'*10} {'-'*6} {'-'*12} {'-'*12} {'-'*5}")

n_superradiant = 0
superradiant_modes = []

# CRITICAL: Mode 0 (B2_0) is the condensate mode with E_sp ~ 0.
# Its E_eff ~ 0 from q_7=0 and E_sp~0 is NOT superradiance — it is the
# vacuum state itself. The Bose factor 1/(1-exp(E/T)) diverges at E->0,
# which is the infrared catastrophe of the condensate, not a physical
# extraction rate. We must regularize: exclude modes with |E_eff| < E_IR_cutoff,
# where E_IR_cutoff is set by the BCS gap (the minimum excitation energy).
E_IR_cutoff = abs(E_cond)  # = 0.137 M_KK (BCS gap protects the vacuum)

for i in range(N_modes):
    shift = q_7[i] * Phi_7_ergo
    is_condensate = (abs(E_sp_fold[i]) < 1e-6 and abs(q_7[i]) < 1e-6)
    is_ir_protected = abs(E_eff[i]) < E_IR_cutoff
    is_sr = E_eff[i] < -E_IR_cutoff  # must exceed IR cutoff to be superradiant
    status = "COND" if is_condensate else ("SR" if is_sr else "no")
    log(f"  {mode_labels[i]:<8} {E_sp_fold[i]:>10.6f} {q_7[i]:>+6.1f} {shift:>+12.6f} "
        f"{E_eff[i]:>+12.6f} {status:>5}")
    if is_sr and not is_condensate:
        n_superradiant += 1
        superradiant_modes.append(i)

log(f"\n  Superradiant modes: {n_superradiant} out of {N_modes}")
log(f"  Superradiant mode indices: {superradiant_modes}")

# ==============================================================================
# STEP 3: Compute superradiance extraction rate Gamma_SR per mode
# ==============================================================================

log("\n" + "=" * 78)
log("STEP 3: Superradiance extraction rate per mode")
log("=" * 78)

# The superradiance amplification factor for a BH (my Paper 05, Starobinsky):
#   Gamma_SR = |beta_omega|^2 = (exp(2*pi*omega/kappa) - 1)^{-1} for omega < m*Omega_H
# which is ENHANCED (>0) for superradiant modes.
#
# In the analog: the extraction rate per mode is governed by:
# 1. The depth of the negative energy: |E_eff(k)| when E_eff < 0
# 2. The coupling between B2 and B3 sectors: V_B2B3 from V_bare_cont
# 3. The Boltzmann/Bose factor for the mode
#
# Gamma_SR(k) = 2*pi * |<k|V|k'>|^2 * rho(E_eff) * n_BE(E_eff)
#
# For negative E_eff (superradiant regime):
# The Bose-Einstein factor n_BE(E_eff) = 1/(exp(E_eff/T) - 1) diverges as E_eff -> 0-
# This is the superradiant enhancement: modes with E_eff just below zero
# have an O(T/|E_eff|) amplification.
#
# Fermi's golden rule rate:
# Gamma_SR(k) = 2*pi * |V_kk'|^2 * rho_k * f(E_eff)
# where f = 1 for classical, Bose enhancement for quantum
#
# For B2->B3 transfer: V_kk' = V_bare_cont[k_B2, k_B3]

# Extract B2-B3 coupling matrix elements
# V_bare is 8x8. B2 modes: 0-3, B3 modes: 5-7
V_B2_B3 = V_bare[0:4, 5:8]  # (4, 3) matrix of B2-B3 couplings
log(f"  V_B2_B3 coupling matrix (B2 rows, B3 cols):")
for i in range(4):
    row_str = " ".join(f"{V_B2_B3[i,j]:>10.6f}" for j in range(3))
    log(f"    B2_{i}: [{row_str}]")

# Acoustic temperature from GGE (canonical)
T_eff = T_acoustic  # = 0.112 M_KK

# Density of states at fold for B2 modes
rho_fold = rho_B2_per_mode  # = 14.02 per mode

# Compute Gamma_SR for each superradiant mode
Gamma_SR = np.zeros(N_modes)
E_extracted = np.zeros(N_modes)

log(f"\n  T_eff = {T_eff:.4f} M_KK (GGE acoustic temperature)")
log(f"  rho_fold = {rho_fold:.4f} per mode (B2 DOS at fold)")

for k in range(N_modes):
    if k not in superradiant_modes:
        continue  # not a genuine superradiant mode (respects IR cutoff + condensate exclusion)

    # Sum over all B3 final states for this mode
    if sector_ids[k] == 'B2':
        # B2 mode scattering into B3: use V_B2_B3[k, :]
        V_sq_sum = np.sum(V_B2_B3[k, :]**2)
    elif sector_ids[k] == 'B1':
        # B1 mode: use V_bare[4, 5:8]
        V_sq_sum = np.sum(V_bare[4, 5:8]**2)
    elif sector_ids[k] == 'B3':
        # B3 mode (already negative energy — direct extraction)
        # Use self-coupling V_bare[k, k] and B2 couplings V_bare[0:4, k]
        V_sq_sum = np.sum(V_bare[0:4, k]**2)
    else:
        V_sq_sum = 0.0  # (local)

    # Fermi golden rule: Gamma = 2*pi * |V|^2 * rho
    # For superradiant modes, the Bose enhancement factor:
    # n_BE = 1/(exp(E_eff/T) - 1) ~ -T/E_eff for |E_eff| << T (superradiant regime)
    # Note: E_eff < 0, so exp(E_eff/T) < 1, giving n_BE < 0 —
    # this is the Zel'dovich superradiant instability.
    # The physical rate involves |n_BE + 1| = 1/(1 - exp(E_eff/T))
    # For |E_eff| >> T: bose_factor ~ 1 (classical regime)
    # For |E_eff| << T: bose_factor ~ T/|E_eff| (superradiant enhancement)

    bose_factor = 1.0 / (1.0 - np.exp(E_eff[k] / T_eff))

    # Gamma_SR(k) in M_KK units
    Gamma_SR[k] = 2 * np.pi * V_sq_sum * rho_fold * bose_factor

    # Energy extracted per unit time: |E_eff(k)| * Gamma_SR(k)
    E_extracted[k] = abs(E_eff[k]) * Gamma_SR[k]

log(f"\n  Superradiance rates:")
log(f"  {'Mode':<8} {'E_eff':>12} {'|V|^2_sum':>12} {'Bose':>10} {'Gamma_SR':>14} {'dE/dt':>14}")
log(f"  {'-'*8} {'-'*12} {'-'*12} {'-'*10} {'-'*14} {'-'*14}")

for k in range(N_modes):
    if Gamma_SR[k] > 0 or E_eff[k] < 0:
        if sector_ids[k] == 'B2':
            V_sq_sum = np.sum(V_B2_B3[k, :]**2)
        elif sector_ids[k] == 'B1':
            V_sq_sum = np.sum(V_bare[4, 5:8]**2)
        elif sector_ids[k] == 'B3':
            V_sq_sum = np.sum(V_bare[0:4, k]**2)
        else:
            V_sq_sum = 0.0  # (local)
        bose_f = 1.0 / (1.0 - np.exp(E_eff[k] / T_eff)) if E_eff[k] < 0 else 0.0
        log(f"  {mode_labels[k]:<8} {E_eff[k]:>+12.6f} {V_sq_sum:>12.6e} "
            f"{bose_f:>10.4f} {Gamma_SR[k]:>14.6e} {E_extracted[k]:>14.6e}")

# ==============================================================================
# STEP 4: Total CC reduction rate and timescale
# ==============================================================================

log("\n" + "=" * 78)
log("STEP 4: Total CC reduction rate and cosmic timescale comparison")
log("=" * 78)

# Total extraction rate: sum over all superradiant modes
dLambda_dt_MKK = np.sum(E_extracted)  # in M_KK^2 per M_KK^{-1} = M_KK^3

log(f"  Total dLambda/dt = sum Gamma_SR(k)*|E_eff(k)| = {dLambda_dt_MKK:.6e} M_KK^3")

# Convert to physical units:
# M_KK = 7.43e16 GeV, so M_KK^3 = (7.43e16)^3 GeV^3
# Rate in GeV^4/s: dLambda/dt [GeV^4/s] = dLambda/dt [M_KK^3] * M_KK^4 * GeV_to_inv_s / M_KK
# Actually: rate in natural units is M_KK^3 * M_KK = M_KK^4 per M_KK^{-1} time
# Convert: dLambda/dt [GeV^4/s] = dLambda_dt_MKK * M_KK^4 * (M_KK * GeV_to_inv_s)

# More carefully: dLambda/dt has dimensions of [energy density] / [time]
# In framework units: dLambda/dt = [M_KK^4] / [M_KK^{-1}] = M_KK^5
# Wait — E_extracted[k] = |E_eff(k)| * Gamma_SR(k)
# |E_eff| is in M_KK, Gamma_SR is in M_KK (rate), so E_extracted is in M_KK^2
# This is energy per unit time per mode (in M_KK units where hbar=1)

# Total energy extracted per M_KK^{-1} time: dE/dt = sum(E_extracted) in M_KK^2
# To get CC reduction: Lambda = E_vacuum / Vol_3
# The CC is rho_vac = Lambda_eff * M_KK^4 = 0.046 * M_KK^4 (from S59)
# Extraction acts on the 8-mode Fock space energy, so:
# dLambda_eff/dt = dE/dt / Vol_internal = dE/dt (since we work in M_KK units on S^3(SU(3)))

# But the CC is Lambda = a_0 * M_KK^4 / Vol (spectral action), so the
# dimensionless CC parameter is Lambda_eff = 0.046 (S59 Mack-Landau workshop)
Lambda_eff = 0.046  # S59 dimensionless CC residual  # (local)

# Time to fully extract Lambda_eff:
if dLambda_dt_MKK > 0:
    t_extract_MKK = Lambda_eff / dLambda_dt_MKK  # in M_KK^{-1}
else:
    t_extract_MKK = np.inf

# Convert to seconds
# M_KK^{-1} = 1/(M_KK * GeV_to_inv_s) seconds
MKK_inv_to_s = 1.0 / (M_KK * GeV_to_inv_s)
t_extract_s = t_extract_MKK * MKK_inv_to_s

log(f"\n  Lambda_eff (dimensionless CC) = {Lambda_eff:.4f}")
log(f"  dLambda/dt = {dLambda_dt_MKK:.6e} M_KK^2 / M_KK^{{-1}}")
log(f"  t_extract = Lambda_eff / (dLambda/dt) = {t_extract_MKK:.6e} M_KK^{{-1}}")
log(f"  MKK^{{-1}} = {MKK_inv_to_s:.4e} s")
log(f"  t_extract = {t_extract_s:.4e} s")
log(f"  t_universe = {t_universe_s:.4e} s")

if t_extract_s > 0 and np.isfinite(t_extract_s):
    ratio = t_extract_s / t_universe_s
    log(f"  t_extract / t_universe = {ratio:.4e}")
    total_extracted = dLambda_dt_MKK * (t_universe_s / MKK_inv_to_s)
    extraction_fraction = total_extracted / Lambda_eff
    log(f"  Total extracted in t_universe: {total_extracted:.6e}")
    log(f"  Fraction of Lambda_eff extracted: {extraction_fraction:.6e}")
else:
    ratio = np.inf
    total_extracted = 0.0  # (local)
    extraction_fraction = 0.0  # (local)
    log(f"  No extraction (t_extract = inf)")

# ==============================================================================
# STEP 5: Comparison with Hawking evaporation analog
# ==============================================================================

log("\n" + "=" * 78)
log("STEP 5: Hawking evaporation analogy — comparison of timescales")
log("=" * 78)

# For a Kerr BH with mass M and spin a:
#   T_H = kappa / (2*pi) where kappa = (r+ - r-) / (2*(r+^2 + a^2))
#   Superradiance rate: Gamma_BH ~ (omega - m*Omega_H) * |A_lm|^2
#   Total evaporation time: t_evap ~ M^3 / M_Pl^4 (Hawking, my Paper 05)
#
# The analog here:
#   T_eff = 0.112 M_KK (acoustic temperature — much larger than BH temperatures)
#   This is the WARM ERGOSPHERE regime: T >> |E_eff| for the superradiant modes
#
# In contrast to a BH where T_H ~ 1/M is tiny and superradiance is slow,
# here the high temperature ENHANCES the Bose factor dramatically.
# But the CC gap is 112 orders — even with enhancement, the question is
# whether the rate * time exceeds the gap.

log(f"  Analog Hawking temperature: T_eff = {T_eff:.4f} M_KK")
log(f"  For comparison: BH Hawking temp T_H = 1/(8*pi*M)")
log(f"  At M = M_Pl: T_H ~ 1/(8*pi) = {1/(8*np.pi):.4f} M_Pl")
log(f"  The framework ergosphere is WARM: T/E_gap ~ {T_eff/Delta_B3:.2f}")
log(f"  BH superradiance is COLD: T_H/omega ~ tiny for astrophysical BHs")

# Key difference from BH superradiance:
# BH: energy is radiated to infinity. The horizon area decreases. Second law
#     requires S_gen = S_BH + S_rad >= 0 (GSL, my Paper 07).
# Analog: energy is redistributed between B2 and B3 sectors within the same
#     Fock space. There is no "radiation to infinity." The GSL analog
#     (GSL-QTHEORY-46 PASS) involves the spectral entropy + condensate entropy.

log(f"\n  KEY DIFFERENCE: No radiation to infinity in the analog.")
log(f"  BH superradiance: S_BH decreases, S_rad increases, S_gen >= 0")
log(f"  Analog: occupation redistributes within 8-mode Fock space")
log(f"  GSL-QTHEORY-46 (PASS): dS_gen/dt >= 0, 35,983x gravitational dominance")
log(f"  => Redistribution is ENTROPY-INCREASING but confined to internal space")

# ==============================================================================
# STEP 6: CC reduction comparison — the 112-order gap
# ==============================================================================

log("\n" + "=" * 78)
log("STEP 6: CC gap analysis — can superradiance bridge 112 orders?")
log("=" * 78)

CC_gap_OOM = 112.0  # from S58/S59 (Lambda_spectral / Lambda_obs)  # (local)

# The CC in the framework: Lambda = S_spectral * M_KK^4 / (16*pi^2)
# S_spectral = 250,360 at fold. Lambda_eff = 0.046 (dimensionless residual after
# q-theory subtraction — the remnant that q-theory cannot cancel).
#
# The superradiance extraction rate dLambda/dt reduces the BCS contribution
# to Lambda by transferring occupation out of the condensate into B3 modes.
#
# But: the 112-order gap is between Lambda_spectral and Lambda_obs.
# The 0.046 residual is already 112 orders above observation.
# Superradiance would need to reduce 0.046 to 2.7e-47 / M_KK^4 = 2.7e-47 / (7.43e16)^4
# = 2.7e-47 / 3.05e67 = 8.85e-115 in dimensionless units.

Lambda_obs_dimless = rho_Lambda_obs / (M_KK**4)
log(f"  Lambda_eff (spectral residual) = {Lambda_eff:.4e}")
log(f"  Lambda_obs (dimensionless) = {Lambda_obs_dimless:.4e}")
log(f"  Gap: Lambda_eff / Lambda_obs_dimless = {Lambda_eff/Lambda_obs_dimless:.4e}")
log(f"  = 10^{np.log10(Lambda_eff/Lambda_obs_dimless):.1f}")

# The superradiance extraction over cosmic time
if dLambda_dt_MKK > 0 and np.isfinite(dLambda_dt_MKK):
    t_universe_MKK = t_universe_s / MKK_inv_to_s
    total_extracted_dimless = dLambda_dt_MKK * t_universe_MKK
    log(f"\n  t_universe in M_KK^{{-1}} = {t_universe_MKK:.4e}")
    log(f"  Total CC extracted = {total_extracted_dimless:.4e}")
    log(f"  CC reduction / Lambda_eff = {total_extracted_dimless/Lambda_eff:.4e}")
    log(f"  CC reduction / Lambda_obs = {total_extracted_dimless/Lambda_obs_dimless:.4e}")

    orders_bridged = np.log10(total_extracted_dimless / Lambda_obs_dimless) if total_extracted_dimless > 0 else -np.inf
    log(f"  Orders bridged toward observation: {orders_bridged:.1f} of {CC_gap_OOM:.0f}")
else:
    t_universe_MKK = t_universe_s / MKK_inv_to_s
    total_extracted_dimless = 0.0  # (local)
    orders_bridged = -np.inf
    log(f"  No extraction available.")

# ==============================================================================
# STEP 7: Back-reaction and self-consistency check
# ==============================================================================

log("\n" + "=" * 78)
log("STEP 7: Back-reaction and self-consistency")
log("=" * 78)

# The superradiance extraction depletes B2 occupation and fills B3.
# This changes alpha: the integrability-breaking parameter depends on
# the occupation distribution. As B3 fills, the system moves TOWARD
# the integrable GGE minimum (Hessian eigenvalue becomes less negative).
# This is the analog of BH spin-down via superradiance.
#
# Self-consistency: Gamma_SR decreases as extraction proceeds.
# The system approaches the alpha_crit boundary and the ergosphere closes.
# This is EXACTLY the BH superradiance saturation (Brito, Cardoso, Pani 2015).
#
# Maximum extractable energy: from alpha_total to alpha_crit
# delta_alpha = alpha_total - alpha_crit

delta_alpha = alpha_total - alpha_crit_val
alpha_range_frac = delta_alpha / alpha_total  # fraction of alpha "spent"

# The free energy change associated with alpha_total -> alpha_crit:
# delta_F = integral of lambda(alpha) * delta_alpha from alpha_total to alpha_crit
# With linear lambda: lambda(alpha) = lambda_0 + (lambda_1 - lambda_0) * alpha
# delta_F = integral from alpha_crit to alpha_total of |lambda(alpha)| dalpha

alpha_arr = np.linspace(alpha_crit_val, alpha_total, 1000)
lambda_arr = lambda_0_val + (lambda_1_val - lambda_0_val) * alpha_arr
_mask = lambda_arr < 0
if np.any(_mask):
    delta_F_ergo = np.trapezoid(np.abs(lambda_arr[_mask]), alpha_arr[_mask])
else:
    delta_F_ergo = 0.0  # (local)

log(f"  alpha_total - alpha_crit = {delta_alpha:.6f}")
log(f"  alpha range fraction = {alpha_range_frac:.4f} ({alpha_range_frac*100:.1f}%)")
log(f"  Integrated free energy from ergosphere: delta_F = {delta_F_ergo:.6e} M_KK")
log(f"  delta_F / Lambda_eff = {delta_F_ergo / Lambda_eff:.6e}")
log(f"  delta_F / Lambda_obs_dimless = {delta_F_ergo / Lambda_obs_dimless:.4e}")

# BH analog: spin-down timescale
# t_spindown ~ M^2 / (m * Omega_H * alpha_BH) for massive bosons
# Here: t_spindown ~ 1/Gamma_SR * (delta_alpha / alpha_total)
if np.max(Gamma_SR) > 0:
    t_spindown_MKK = delta_alpha / (np.max(Gamma_SR) * alpha_total)
    t_spindown_s = t_spindown_MKK * MKK_inv_to_s
    log(f"  Analog spin-down time: {t_spindown_MKK:.4e} M_KK^{{-1}} = {t_spindown_s:.4e} s")
else:
    t_spindown_MKK = np.inf
    t_spindown_s = np.inf
    log(f"  No spin-down (no superradiant modes)")

# ==============================================================================
# GATE VERDICT
# ==============================================================================

log("\n" + "=" * 78)
log("GATE VERDICT: PENROSE-SUPERRAD-60")
log("=" * 78)

# Gate criteria (BACK-REACTION CORRECTED):
# The naive linear extrapolation (rate * t_universe) is physically wrong because
# back-reaction closes the ergosphere on timescale t_spindown << t_universe.
# The CORRECT comparison is: total extractable free energy (delta_F_ergo)
# vs the CC gap (Lambda_eff vs Lambda_obs).
#
# PASS: delta_F_ergo > Lambda_eff AND resulting Lambda < Lambda_obs
#       (Penrose process can reduce CC to observed value)
# FAIL: delta_F_ergo << Lambda_obs_dimless (total extraction negligible vs CC gap)
# INFO: non-negligible but cannot bridge 112-order gap

# Back-reaction corrected analysis:
# delta_F_ergo = 0.482 M_KK: the ergosphere CAN dump more than Lambda_eff (0.046).
# But both are O(1) in M_KK units, while Lambda_obs ~ 10^{-115} in M_KK units.
# The Penrose process reduces Lambda from 0.046 to some O(0.01) value,
# but cannot reach 10^{-115}. The 112-order gap remains unbridged.
# The spindown saturates at alpha_crit in ~ 5e-42 s (instant on cosmological scales).

CC_gap_after_extraction = delta_F_ergo / Lambda_obs_dimless
orders_after = np.log10(CC_gap_after_extraction) if delta_F_ergo > 0 else np.inf

if n_superradiant == 0:
    verdict = "FAIL"
    verdict_detail = "No superradiant modes found — all E_eff >= 0"
elif delta_F_ergo > Lambda_eff and Lambda_obs_dimless > 0 and delta_F_ergo / Lambda_obs_dimless < 10:
    verdict = "PASS"
    verdict_detail = (f"delta_F_ergo = {delta_F_ergo:.4e} extracts to within "
                     f"factor {delta_F_ergo/Lambda_obs_dimless:.1f} of Lambda_obs")
elif delta_F_ergo > 0.01 * Lambda_eff:
    verdict = "INFO"
    verdict_detail = (f"Superradiance is REAL ({n_superradiant} modes, rate ~{np.max(Gamma_SR):.3f} M_KK) "
                     f"but back-reaction limits total extraction to delta_F = {delta_F_ergo:.3f} M_KK "
                     f"(O(1) in M_KK units, still {orders_after:.0f} orders above Lambda_obs). "
                     f"Spindown t ~ {t_spindown_s:.1e} s << t_universe.")
else:
    verdict = "FAIL"
    verdict_detail = f"Negligible extraction: delta_F = {delta_F_ergo:.4e} M_KK"

log(f"  N_superradiant modes: {n_superradiant}")
log(f"  Instantaneous dLambda/dt = {dLambda_dt_MKK:.6e} M_KK^2/M_KK^{{-1}}")
log(f"  Back-reaction limited: delta_F_ergo = {delta_F_ergo:.6f} M_KK")
log(f"  Lambda_eff = {Lambda_eff:.6e}")
log(f"  Lambda_obs_dimless = {Lambda_obs_dimless:.6e}")
log(f"  delta_F / Lambda_obs = {delta_F_ergo/Lambda_obs_dimless:.4e} (= 10^{orders_after:.1f})")
log(f"  Spindown timescale: {t_spindown_s:.4e} s ({t_spindown_s/t_universe_s:.2e} * t_universe)")
log(f"  VERDICT: {verdict}")
log(f"  Detail: {verdict_detail}")

# Physical interpretation
log(f"\n  PHYSICAL INTERPRETATION (Hawking perspective):")
if n_superradiant > 0:
    log(f"  The B3 ergosphere IS open (lambda_alpha = {lambda_alpha_val:.2f} < 0).")
    log(f"  {n_superradiant} modes satisfy the superradiance condition E_eff < 0.")
    log(f"  This is the precise analog of omega < m*Omega_H for Kerr BH superradiance")
    log(f"  (my Paper 05, Starobinsky amplification, Zel'dovich 1971).")
    log(f"")
    log(f"  CRITICAL: Back-reaction (analog of BH spin-down) is FAST.")
    log(f"  t_spindown = {t_spindown_s:.2e} s << t_universe = {t_universe_s:.2e} s.")
    log(f"  The ergosphere closes after extracting delta_F = {delta_F_ergo:.4f} M_KK,")
    log(f"  which is O(1) in framework units — not O(10^{{-115}}).")
    log(f"  This is the analog of a Kerr BH spinning down to Schwarzschild:")
    log(f"  superradiance is a transient that saturates at J=0, not a CC-tuning mechanism.")
    log(f"")
    log(f"  The CC gap of 112 orders requires a mechanism that can")
    log(f"  suppress Lambda by e^{{-260}}. Penrose extraction suppresses")
    log(f"  by a factor of ~ {delta_F_ergo/Lambda_eff:.1f}. Shortfall: {orders_after:.0f} orders.")
    log(f"")
    log(f"  CONCLUSION: Penrose superradiance is KINEMATICALLY REAL but")
    log(f"  DYNAMICALLY SELF-LIMITING. It joins the 27+ closed CC mechanisms.")
    log(f"  The CC = q-theory self-tuning (Q-THEORY-BCS-45 PASS) remains unique.")
else:
    log(f"  Despite lambda_alpha < 0, all modes have E_eff >= 0 after IR regularization.")
    log(f"  The ergosphere exists geometrically but is kinematically inaccessible.")
    log(f"  This is the analog of a slowly rotating BH where Omega_H is too small")
    log(f"  for any mode to satisfy the superradiance condition.")

# ==============================================================================
# SAVE RESULTS
# ==============================================================================

log("\n" + "=" * 78)
log("Saving results...")

results = {
    # Gate
    'gate_name': np.array('PENROSE-SUPERRAD-60'),
    'gate_verdict': np.array(verdict),
    'gate_detail': np.array(verdict_detail),

    # Input parameters
    'alpha_total': np.float64(alpha_total),
    'alpha_crit': np.float64(alpha_crit_val),
    'lambda_alpha': np.float64(lambda_alpha_val),
    'Phi_7_ergo': np.float64(Phi_7_ergo),
    'T_eff': np.float64(T_eff),
    'Lambda_eff': np.float64(Lambda_eff),
    'Lambda_obs_dimless': np.float64(Lambda_obs_dimless),

    # Mode data
    'E_sp_fold': E_sp_fold,
    'q_7': q_7,
    'E_eff': E_eff,
    'Gamma_SR': Gamma_SR,
    'E_extracted': E_extracted,
    'mode_labels': np.array(mode_labels),
    'sector_ids': np.array(sector_ids),
    'n_superradiant': np.int64(n_superradiant),
    'superradiant_modes': np.array(superradiant_modes, dtype=np.int64),

    # Totals
    'dLambda_dt_MKK': np.float64(dLambda_dt_MKK),
    'total_extracted_dimless': np.float64(total_extracted_dimless),
    'extraction_fraction': np.float64(extraction_fraction),
    't_extract_s': np.float64(t_extract_s),
    't_extract_MKK': np.float64(t_extract_MKK),

    # Back-reaction (DECISIVE quantities)
    'delta_alpha': np.float64(delta_alpha),
    'delta_F_ergo': np.float64(delta_F_ergo),
    't_spindown_s': np.float64(t_spindown_s),
    't_spindown_MKK': np.float64(t_spindown_MKK),

    # CC gap
    'CC_gap_OOM': np.float64(CC_gap_OOM),
    'orders_after_extraction': np.float64(orders_after if np.isfinite(orders_after) else -999.0),
    'orders_bridged': np.float64(orders_bridged if np.isfinite(orders_bridged) else -999.0),
}

np.savez("computations/session-60/s60_penrose_superrad.npz", **results)
log("  Saved s60_penrose_superrad.npz")

# ==============================================================================
# PLOTS
# ==============================================================================

fig, axes = plt.subplots(2, 2, figsize=(16, 14))

# --- Panel 1: Mode effective energies ---
ax1 = axes[0, 0]
colors_mode = ['#2196F3' if s == 'B2' else '#FF9800' if s == 'B1' else '#F44336'
               for s in sector_ids]
bars = ax1.bar(range(N_modes), E_eff, color=colors_mode, alpha=0.8,
               edgecolor='black', linewidth=1.0)
ax1.axhline(y=0, color='black', linestyle='-', linewidth=1.5)
ax1.set_xticks(range(N_modes))
ax1.set_xticklabels(mode_labels, rotation=45, ha='right', fontsize=10)
ax1.set_ylabel(r'$E_{\rm eff}(k) = E_k - q_7 \Phi_7$ [$M_{KK}$]', fontsize=12)
ax1.set_title(r'Effective Energies — Superradiance Condition: $E_{\rm eff} < 0$', fontsize=13)

# Highlight superradiant modes
for k in superradiant_modes:
    ax1.annotate('SR', xy=(k, E_eff[k]), xytext=(k, E_eff[k] - 0.15),
                fontsize=11, fontweight='bold', color='red', ha='center')

# Add bare energies for comparison
ax1.bar(range(N_modes), E_sp_fold, alpha=0.2, color='gray', edgecolor='gray',
        linewidth=0.5, label=r'$E_k$ (bare)')
ax1.legend(fontsize=11)
ax1.set_ylim(min(np.min(E_eff) - 0.3, -0.5), max(np.max(E_sp_fold) + 0.3, 1.5))

# --- Panel 2: Extraction rates ---
ax2 = axes[0, 1]
if n_superradiant > 0:
    sr_modes_plot = [mode_labels[k] for k in superradiant_modes]
    sr_rates = [Gamma_SR[k] for k in superradiant_modes]
    sr_extracted = [E_extracted[k] for k in superradiant_modes]

    x_pos = range(len(sr_modes_plot))
    width = 0.35  # (local)
    bars1 = ax2.bar([x - width/2 for x in x_pos], sr_rates, width,
                    label=r'$\Gamma_{SR}$ [M$_{KK}$]', color='#E91E63', alpha=0.8)
    bars2 = ax2.bar([x + width/2 for x in x_pos], sr_extracted, width,
                    label=r'$\dot{E}$ = $|E_{eff}| \Gamma_{SR}$', color='#9C27B0', alpha=0.8)
    ax2.set_xticks(x_pos)
    ax2.set_xticklabels(sr_modes_plot, fontsize=11)
    ax2.legend(fontsize=11)
    ax2.set_ylabel('Rate [$M_{KK}$ units]', fontsize=12)
else:
    ax2.text(0.5, 0.5, 'No superradiant modes\n(all $E_{eff} \\geq 0$)',
            transform=ax2.transAxes, ha='center', va='center', fontsize=14,
            style='italic', color='gray')
ax2.set_title('Superradiance Extraction Rates', fontsize=13)

# --- Panel 3: Hessian eigenvalue with superradiance regime ---
ax3 = axes[1, 0]
alpha_range = np.linspace(0, 0.8, 400)
lambda_range = lambda_0_val + (lambda_1_val - lambda_0_val) * alpha_range
ax3.plot(alpha_range, lambda_range, 'b-', linewidth=2.5)
ax3.axhline(y=0, color='black', linewidth=1)
ax3.axvline(x=alpha_crit_val, color='red', linestyle='--', linewidth=2,
           label=f'$\\alpha_{{crit}}$ = {alpha_crit_val:.3f}')
ax3.axvline(x=alpha_total, color='green', linestyle=':', linewidth=2.5,
           label=f'$\\alpha_{{total}}$ = {alpha_total:.3f}')
ax3.fill_between(alpha_range, lambda_range, 0,
                 where=(lambda_range < 0) & (alpha_range <= alpha_total),
                 alpha=0.25, color='red', label='Ergosphere (accessible)')  # (local)
ax3.fill_between(alpha_range, lambda_range, 0,
                 where=(lambda_range < 0) & (alpha_range > alpha_total),
                 alpha=0.08, color='red', label='Ergosphere (beyond reach)')  # (local)
ax3.scatter([alpha_total], [lambda_alpha_val], color='green', s=120, zorder=5,
           marker='*', label=f'$\\lambda_{{\\alpha}}$ = {lambda_alpha_val:.1f}')
ax3.set_xlabel(r'$\alpha$ (integrability breaking)', fontsize=12)
ax3.set_ylabel(r'Min Hessian eigenvalue $\lambda_{min}$', fontsize=12)
ax3.set_title('Ergosphere Structure', fontsize=13)
ax3.legend(fontsize=9, loc='upper right')

# --- Panel 4: CC gap visualization ---
ax4 = axes[1, 1]
# Log scale bar chart showing the CC gap
categories = ['$\\Lambda_{eff}$\n(residual)',
              '$\\delta\\Lambda_{SR}$\n(extracted/Hubble)',
              '$\\Lambda_{obs}$\n(observed)']
if total_extracted_dimless > 0:
    values = [Lambda_eff, total_extracted_dimless, Lambda_obs_dimless]
else:
    values = [Lambda_eff, 1e-200, Lambda_obs_dimless]  # placeholder

# Use log bars
log_values = [np.log10(max(v, 1e-300)) for v in values]
colors_cc = ['#FF5722', '#4CAF50', '#2196F3']
bars_cc = ax4.barh(range(len(categories)), log_values, color=colors_cc, alpha=0.8,
                   edgecolor='black', linewidth=1)
ax4.set_yticks(range(len(categories)))
ax4.set_yticklabels(categories, fontsize=12)
ax4.set_xlabel(r'$\log_{10}(\Lambda / M_{KK}^4)$', fontsize=12)
ax4.set_title(f'CC Gap: {CC_gap_OOM:.0f} Orders', fontsize=13)

# Annotate the gap
for i, (val, logv) in enumerate(zip(values, log_values)):
    ax4.text(logv + 1, i, f'$10^{{{logv:.0f}}}$', va='center', fontsize=11,
            fontweight='bold')

plt.tight_layout()
plt.savefig("computations/session-60/s60_penrose_superrad.png", dpi=150, bbox_inches='tight')
log("  Saved s60_penrose_superrad.png")

# Write log
log_text = "\n".join(log_lines)
with open("computations/session-60/s60_penrose_superrad_log.txt", "w") as fout:
    fout.write(log_text)
log("  Saved s60_penrose_superrad_log.txt")

log("\n" + "=" * 78)
log(f"PENROSE-SUPERRAD-60 COMPLETE. Verdict: {verdict}")
log(f"  {verdict_detail}")
log("=" * 78)
