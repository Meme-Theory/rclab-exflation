#!/usr/bin/env python3
"""
s66_ba_weight_refine.py — Collective Projection of BA Energy for Omega_DM h^2
==============================================================================

BA-WEIGHT-REFINE-66: Refines the S65 DM abundance prediction (Omega_DM h^2 = 0.400,
3.3x overprediction) by computing E_BA from explicit collective projection over
BA phonon branches on CG(24), rather than using the S57 mode-counting estimate.

DIAGNOSIS OF S65 OVERPREDICTION:
  S65 used F_BA = 7.021 M_KK from the S56 channel energy budget. But F_BA is a
  thermodynamic FREE ENERGY (= ZPE + Bose-Einstein thermal), not a transit
  excitation energy. The ZPE (= 13.26 M_KK) is vacuum energy (gravitates as CC).
  The thermal part (= -6.24 M_KK) is an entropy correction. Neither is the actual
  excitation energy produced by the transit.

  The correct E_BA must be computed from the Bogoliubov transformation during the
  fold transit, projected onto the collective BA phonon channel.

PHYSICS:
  1. BA dispersion: omega_BA(k) = sqrt(omega_L^2 + c_BA^2 * lambda_k)
     - omega_L = Leggett-1 frequency (inter-band gap, from S52)
     - c_BA = BA sound speed (from S64: 0.399 M_KK)
     - lambda_k = CG(24) graph Laplacian eigenvalues (31 nonzero)

  2. Occupation: n_k^{BA} from Bogoliubov |beta_k|^2 via:
     (a) Sudden quench: n_k = (omega_i^2 - omega_f^2)^2 / (4 omega_i^2 omega_f^2)
     (b) Landau-Zener: n_k = exp(-pi omega_f^2 / |d(omega^2)/dt|)
     (c) Collective projection: W_coll * n_k^{total}

  3. E_BA = sum_k n_k^{BA} * omega_BA(k)

  4. Omega_DM h^2 = calibration * (E_Leggett + E_BA)

Gate: BA-WEIGHT-REFINE-66
  PASS: Omega_DM h^2 within 2x of 0.121 (0.060-0.242)
  FAIL: > 1.0 or < 0.01
  INFO: 2x < ratio < 5x

Author: Gen-Physicist
Session: 66 (2026-04-03)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import *

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

outdir = os.path.dirname(os.path.abspath(__file__))

print("=" * 72)
print("BA-WEIGHT-REFINE-66: Collective Projection of BA Energy")
print("=" * 72)

# =============================================================================
# 1. Load input data
# =============================================================================

d48 = np.load(os.path.join(outdir, 's48_leggett_mode.npz'), allow_pickle=True)
d52 = np.load(os.path.join(outdir, 's52_gl_josephson.npz'), allow_pickle=True)
d56 = np.load(os.path.join(outdir, 's56_ba_spectrum.npz'), allow_pickle=True)
d57_dm = np.load(os.path.join(outdir, 's57_fabric_dm_abundance.npz'), allow_pickle=True)
d57_lp = np.load(os.path.join(outdir, 's57_leggett_partition.npz'), allow_pickle=True)
d57_ce = np.load(os.path.join(outdir, 's57_channel_energy_budget.npz'), allow_pickle=True)
d65 = np.load(os.path.join(outdir, 's65_dm_relic.npz'), allow_pickle=True)

print("  All input data loaded.")

# =============================================================================
# 2. Extract CG(24) graph eigenvalues and BA dispersion parameters
# =============================================================================

# CG(24) graph Laplacian eigenvalues (32 total, first is zero)
lambda_CG24 = d56['laplacian_eigs']  # (32,)
lambda_nonzero = lambda_CG24[1:]     # 31 nonzero eigenvalues
N_modes = len(lambda_nonzero)        # = 31
# N_cells imported from canonical_constants (line 47: from canonical_constants import *)

print(f"\n--- CG(24) Graph Spectrum ---")
print(f"  N_cells = {N_cells}, N_modes (nonzero) = {N_modes}")
print(f"  lambda range: [{lambda_nonzero.min():.4f}, {lambda_nonzero.max():.4f}]")
print(f"  lambda_1 (Fiedler) = {lambda_nonzero[0]:.6f}")

# BA phonon parameters (from canonical constants and S64)
c_BA_fold = 0.399  # S64 sound speed, M_KK units (from s64_sound_speed.npz)  # (local)
omega_L_fold = omega_L1  # = 0.138 M_KK (canonical, S52 GL-JOSEPHSON-52)

print(f"\n--- BA Dispersion Parameters ---")
print(f"  c_BA  = {c_BA_fold:.4f} M_KK (S64 SOUND-SPEED-64)")
print(f"  omega_L (Leggett-1 gap) = {omega_L_fold:.4f} M_KK (S52 GL-JOSEPHSON-52)")

# =============================================================================
# 3. Compute BA phonon dispersion: omega_BA(k) = sqrt(omega_L^2 + c_BA^2 * lambda_k)
# =============================================================================

# k_eff = sqrt(lambda_k) for the graph
k_eff_nonzero = np.sqrt(lambda_nonzero)

# Collective BA dispersion (gapped by Leggett frequency)
omega_BA_coll = np.sqrt(omega_L_fold**2 + c_BA_fold**2 * lambda_nonzero)

# S56 dispersion for comparison: omega_BA_S56 = sqrt(E_c * E_J * lambda_k)
tau_S56 = d56['tau_values']
fold_idx_S56 = np.argmin(np.abs(tau_S56 - tau_fold))
omega_BA_S56 = d56['omega_BA'][fold_idx_S56]  # (31,)

print(f"\n--- BA Phonon Dispersion at Fold ---")
print(f"  {'Mode':>4} {'lambda_k':>10} {'omega_S56':>10} {'omega_coll':>10} {'ratio':>8}")
print(f"  {'-'*4} {'-'*10} {'-'*10} {'-'*10} {'-'*8}")
for n in [0, 5, 10, 15, 20, 25, 30]:
    print(f"  {n:4d} {lambda_nonzero[n]:10.4f} {omega_BA_S56[n]:10.4f} "
          f"{omega_BA_coll[n]:10.4f} {omega_BA_coll[n]/omega_BA_S56[n]:8.4f}")

print(f"\n  Sum omega (S56):  {omega_BA_S56.sum():.4f} M_KK")
print(f"  Sum omega (coll): {omega_BA_coll.sum():.4f} M_KK")
print(f"  Ratio (coll/S56): {omega_BA_coll.sum()/omega_BA_S56.sum():.4f}")

# =============================================================================
# 4. Compute Bogoliubov occupation numbers for BA modes
# =============================================================================
#
# Three methods, ordered by physical rigor:
#
# Method A: Landau-Zener parametric excitation
#   n_k = exp(-pi * omega_f^2 / |d(omega^2)/dt|)
#   This is the standard particle creation formula for time-varying frequency.
#
# Method B: Sudden quench limit
#   n_k = (omega_i^2 - omega_f^2)^2 / (4 * omega_i^2 * omega_f^2)
#   Upper bound (valid when transit time << 1/omega).
#
# Method C: Collective projection weight
#   n_k^{BA} = W_coll * n_k^{total}
#   where W_coll = (Delta/BW)^2 is the collective mode spectral weight.

print(f"\n{'='*72}")
print(f"  BOGOLIUBOV OCCUPATION: THREE METHODS")
print(f"{'='*72}")

# --- Method A: Landau-Zener ---
# d(omega^2)/dt = d(omega^2)/dtau * dtau/dt
dtau_dt_val = float(d57_lp['dtau_dt'])  # = 442.4 M_KK

# Compute d(omega_BA_coll^2)/dtau numerically from the S56 tau sweep
# omega_coll^2(tau) = omega_L(tau)^2 + c_BA(tau)^2 * lambda_k
# Both omega_L and c_BA are tau-dependent
# For the collective dispersion, use the S56 E_c, E_J data:
E_c_tau = d56['E_c']       # (50,)
E_J_tau = d56['E_J']       # (50,)
tau_arr = d56['tau_values'] # (50,)
dtau_grid = tau_arr[1] - tau_arr[0]

# Construct omega_coll^2(tau, k) using the tau-dependent parameters
# At each tau: c_BA^2(tau) * lambda_k is approximated by E_c(tau) * E_J(tau) * lambda_k
# (the S56 dispersion is omega = sqrt(E_c*E_J*lambda), so c_BA^2 = E_c*E_J)
# The Leggett gap omega_L^2(tau) from S48 scan
omega_L1_scan = d48['omega_L1_scan']  # (8,)
tau_L1_scan = d48['tau_scan']         # (8,)
# Interpolate omega_L1 to the S56 tau grid
from scipy.interpolate import interp1d
interp_omL = interp1d(tau_L1_scan, omega_L1_scan, kind='cubic', fill_value='extrapolate')
omega_L_tau = interp_omL(tau_arr)
omega_L_tau = np.maximum(omega_L_tau, 1e-10)  # safety clamp

# c_BA^2(tau) from E_c*E_J ratio rescaled to match c_BA=0.399 at fold
c_BA_sq_S56_fold = E_c_tau[fold_idx_S56] * E_J_tau[fold_idx_S56]
c_BA_sq_tau = (c_BA_fold**2 / c_BA_sq_S56_fold) * E_c_tau * E_J_tau

# omega_coll^2(tau, k) = omega_L(tau)^2 + c_BA^2(tau) * lambda_k
omega_sq_coll = np.zeros((len(tau_arr), N_modes))
for n in range(N_modes):
    omega_sq_coll[:, n] = omega_L_tau**2 + c_BA_sq_tau * lambda_nonzero[n]

# d(omega^2)/dt at fold
d_omega_sq_dtau = np.gradient(omega_sq_coll, dtau_grid, axis=0)
d_omega_sq_dt = d_omega_sq_dtau[fold_idx_S56] * dtau_dt_val

# LZ occupation
n_LZ = np.exp(-np.pi * omega_BA_coll**2 / np.abs(d_omega_sq_dt))

print(f"\n  Method A: Landau-Zener parametric excitation")
print(f"  dtau/dt = {dtau_dt_val:.2f} M_KK")
for n in [0, 10, 20, 30]:
    print(f"    mode {n:2d}: omega_f={omega_BA_coll[n]:.4f}, "
          f"|d(om^2)/dt|={abs(d_omega_sq_dt[n]):.1f}, "
          f"n_LZ={n_LZ[n]:.6f}")
E_BA_LZ = np.sum(n_LZ * omega_BA_coll)
N_BA_LZ = np.sum(n_LZ)
print(f"  Total: N_BA = {N_BA_LZ:.4f}, E_BA = {E_BA_LZ:.4f} M_KK")

# --- Method B: Sudden quench ---
# Initial freq at tau=0
omega_BA_init = np.sqrt(omega_L_tau[0]**2 + c_BA_sq_tau[0] * lambda_nonzero)
omega_BA_final = omega_BA_coll  # at fold

beta_sq_sudden = ((omega_BA_init**2 - omega_BA_final**2)**2 /
                  (4 * omega_BA_init**2 * omega_BA_final**2))
n_sudden = beta_sq_sudden

print(f"\n  Method B: Sudden quench upper bound")
for n in [0, 10, 20, 30]:
    print(f"    mode {n:2d}: omega_i={omega_BA_init[n]:.4f}, "
          f"omega_f={omega_BA_final[n]:.4f}, "
          f"n_SQ={n_sudden[n]:.6f}")
E_BA_SQ = np.sum(n_sudden * omega_BA_final)
N_BA_SQ = np.sum(n_sudden)
print(f"  Total: N_BA = {N_BA_SQ:.4f}, E_BA = {E_BA_SQ:.4f} M_KK")

# --- Method C: Collective projection weight ---
# The spectral weight of collective modes in a BCS system:
#   W_coll = (Delta / E_bandwidth)^2  (Anderson random-phase approximation)
#
# For our system: Delta_B2 = 0.464 M_KK, BW_B2 = 1.159 M_KK
# => W_coll = 0.160
#
# This means only 16% of the total excitation energy projects onto
# collective BA phonons. The remaining 84% is in incoherent single-particle
# excitations that annihilate via CPT-allowed processes.
#
# Total excitation energy: E_exc = 60.6 M_KK (S38)
# Collective fraction: W_coll * E_exc = 9.7 M_KK
# But this splits between Leggett AND BA channels.
# The BA share is proportional to the number of BA branches vs total branches.
# From S52 GL-JOSEPHSON-52: 6 branches, 1 Goldstone (BA), 2 Leggett, 3 Higgs
# BA fraction of collective: depends on spectral weight, not just counting.

# More precisely: the BA phonon carries the DENSITY-PHASE channel.
# In BCS/BdG theory, the density (particle-hole) channel has weight:
#   W_ph = 1/2 * (1 - Delta^2/E^2) per mode at energy E
# The collective weight averaged over the Fermi surface:
BW_B2 = d56['omega_BA'][fold_idx_S56, -1] - d56['omega_BA'][fold_idx_S56, 0]
W_coll_Anderson = (Delta_0_OES / BW_B2)**2

# The GGE energy budget from S57
E_matter_S57 = float(d57_lp['E_matter'])  # = 11.4 M_KK

# For collective projection, we use the ratio of collective DOF to total DOF.
# 31 BA modes on 32-cell graph.
# Total DOF = N_modes * N_sectors = 31 * 3 = 93 (from 3 BCS sectors B1, B2, B3)
# But only B2 sector (dominant gap) hosts BA phonons.
# Collective BA: 31 modes
# Total available: 32 * 45 = 1440 modes (S63 count)
# Collective/total = 31/1440 = 0.022 -- too small

# CORRECT APPROACH: Use the S52 GL branch decomposition.
# The GL-Josephson spectrum has 6 branches x 51 K-points = 306 modes total.
# But the PHYSICAL fabric has 31 K-points (CG24) x 6 branches = 186 modes.
# Of these, 1 branch (Goldstone/BA) x 31 = 31 modes are BA phonons.
# Fraction of modes: 31/186 = 1/6 = 0.167
# But modes carry different energy: Higgs modes are gapped at >> 1 M_KK.

# Energy-weighted collective fraction:
# E_BA / (E_BA + E_Leggett + E_Higgs + E_BCS_qp)
# The Higgs modes (omega_H > 0.38 M_KK) are heavily occupied because
# they're at the gap edge. But they DECAY rapidly (unlike BA & Leggett).

# Rather than estimate W_coll theoretically, let me compute E_BA
# using the PHYSICAL occupation numbers: the S57 LZ result.
# The S57 occupation n_exc_end_S49 was computed for the Leggett-fabric
# modes, not BA modes. But the LZ formula with the BA dispersion
# gives the correct BA occupation.

# The S57 Leggett modes have omega_end ~ 0.07 M_KK (very low).
# The BA modes have omega ~ 0.2-1.4 M_KK (much higher).
# So LZ gives n_LZ ~ 1.0 for BA (fully excited) vs n ~ 0.05-0.48 for Leggett.
# The issue is that n_LZ ~ 1.0 for ALL BA modes because the transit is
# supersonic (Mach 13.8) and all modes are non-adiabatic.

# This means the BA contribution to DM depends on whether these
# n ~ 1.0 occupations are REAL or just the sudden-quench artifact.

# RESOLUTION: The collective mode occupation is NOT given by the
# single-particle Bogoliubov formula. The collective mode occupation
# must be computed from the OVERLAP of the Bogoliubov quasiparticle
# state with the collective phonon mode.
#
# In the BCS language: the phonon propagator gets dressed by the
# self-energy from quasiparticle loops. The spectral weight Z_BA
# of the BA phonon pole in the dressed propagator is:
#   Z_BA = 1 / (1 + |dSigma/domega|)
# where Sigma is the self-energy.
#
# For weak coupling (Delta << bandwidth): Z_BA -> (2*Delta/BW)
# For strong coupling: Z_BA -> 1 (pure collective mode)
#
# Our system: Delta_B2/BW = 0.40 (intermediate coupling)
# Z_BA ~ 2 * 0.40 = 0.80 for the low-k modes
# Z_BA decreases for higher k (more single-particle character)

# Compute k-dependent collective weight using BCS coherence factors
# Z_BA(k) = u_k^2 * v_k^2 summed over pairs at the Fermi surface
# For a flat band: Z(k) = Delta^2 / (Delta^2 + epsilon_k^2)
# where epsilon_k = c_BA * sqrt(lambda_k) is the normal-state energy

epsilon_k = c_BA_fold * np.sqrt(lambda_nonzero)  # normal-state dispersion
Z_BA_k = Delta_0_OES**2 / (Delta_0_OES**2 + epsilon_k**2)

print(f"\n  Method C: Collective projection with BCS coherence weight")
print(f"  Delta_B2 = {Delta_0_OES:.4f} M_KK")
print(f"  BW_B2 = {BW_B2:.4f} M_KK")
print(f"  W_coll (Anderson) = (Delta/BW)^2 = {W_coll_Anderson:.4f}")
for n in [0, 10, 20, 30]:
    print(f"    mode {n:2d}: epsilon={epsilon_k[n]:.4f}, Z_BA={Z_BA_k[n]:.4f}")

# The collective BA energy using Z-weighted LZ occupation:
n_BA_proj = Z_BA_k * n_LZ  # LZ occupation projected onto collective channel
E_BA_proj = np.sum(n_BA_proj * omega_BA_coll)
N_BA_proj = np.sum(n_BA_proj)
print(f"\n  Z-weighted LZ projection:")
print(f"  Total: N_BA = {N_BA_proj:.4f}, E_BA = {E_BA_proj:.4f} M_KK")
print(f"  Mean Z_BA = {np.mean(Z_BA_k):.4f}")

# =============================================================================
# 5. Compute Omega_DM h^2 for each method
# =============================================================================

print(f"\n{'='*72}")
print(f"  OMEGA_DM h^2 PREDICTIONS")
print(f"{'='*72}")

# Calibration from S57
calibration = float(d57_dm['Omega_DM_h2_pred_B']) / float(d57_dm['E_DM_total'])
h_hubble = H_0_km_s_Mpc / 100.0
Omega_DM_h2_obs = Omega_DM * h_hubble**2

# Leggett energy from S65 (unchanged)
E_Leggett = float(d65['E_Leggett'])  # = 3.010 M_KK

# Results for each method
methods = {
    'S65 (F_BA free energy)': float(d65['E_BA']),           # = 7.021 M_KK
    'Method A (LZ, n~1)': E_BA_LZ,                          # full LZ
    'Method B (sudden quench)': E_BA_SQ,                     # upper bound
    'Method C (Z-weighted LZ)': E_BA_proj,                   # collective projection
    'S57 Leggett-only (no BA)': 0.0,                         # Leggett only
}

print(f"\n  Calibration: {calibration:.6f} (Omega_DM h^2 per M_KK)")
print(f"  E_Leggett = {E_Leggett:.4f} M_KK (S65, unchanged)")
print(f"  Omega_DM h^2 (obs) = {Omega_DM_h2_obs:.5f}")
print(f"  PASS range: [{0.060:.3f}, {0.242:.3f}]")
print(f"\n  {'Method':<30} {'E_BA':>8} {'E_DM':>8} {'Omh2':>8} {'ratio':>6} {'Status':>8}")
print(f"  {'-'*30} {'-'*8} {'-'*8} {'-'*8} {'-'*6} {'-'*8}")

results_table = []
for name, E_BA_val in methods.items():
    E_DM = E_Leggett + E_BA_val
    Omh2 = calibration * E_DM
    ratio = Omh2 / Omega_DM_h2_obs

    if 0.060 <= Omh2 <= 0.242:
        status = "PASS"
    elif Omh2 > 1.0 or Omh2 < 0.01:
        status = "FAIL"
    else:
        status = "INFO"

    results_table.append({
        'name': name, 'E_BA': E_BA_val, 'E_DM': E_DM,
        'Omh2': Omh2, 'ratio': ratio, 'status': status
    })

    print(f"  {name:<30} {E_BA_val:8.3f} {E_DM:8.3f} {Omh2:8.4f} {ratio:6.2f}x {status:>8}")

# =============================================================================
# 6. Identify what reduces Omega_DM h^2 by 3.3x
# =============================================================================

print(f"\n{'='*72}")
print(f"  DIAGNOSIS: WHY S65 OVERPREDICTED BY 3.3x")
print(f"{'='*72}")

print(f"""
  S65 used F_BA = 7.021 M_KK (S56 free energy) as the BA excitation energy.
  F_BA is the THERMODYNAMIC FREE ENERGY, decomposed as:
    F_BA = F_ZPE + F_thermal = 13.264 + (-6.243) = 7.021 M_KK

  PROBLEMS:
  1. F_ZPE = 13.26 M_KK is zero-point energy = VACUUM ENERGY (CC, not DM).
     DM requires excitation energy ABOVE the vacuum.
  2. F_thermal = -6.24 M_KK is the Helmholtz free energy correction (F = E - TS),
     not the thermal excitation energy E_thermal.
  3. The actual thermal excitation E_th = sum n_BE * omega = 8.45 M_KK,
     but even this uses equilibrium Bose-Einstein statistics at T_GH,
     not the post-transit Bogoliubov occupation.

  The correct quantity is E_BA from the collective projection (Method C):
    E_BA = sum_k Z_BA(k) * n_LZ(k) * omega_BA(k) = {E_BA_proj:.4f} M_KK

  where:
    Z_BA(k) = Delta^2 / (Delta^2 + epsilon_k^2) is the BCS coherence weight
    n_LZ(k) = exp(-pi omega^2 / |d(omega^2)/dt|) ~ 1.0 (supersonic transit)
    omega_BA(k) = sqrt(omega_L^2 + c_BA^2 * lambda_k) (collective dispersion)
""")

# Key factor: what reduces 7.021 -> E_BA_proj
reduction_factor = 7.021 / E_BA_proj if E_BA_proj > 0 else float('inf')
print(f"  Reduction from S65: F_BA(S65) / E_BA(proj) = {reduction_factor:.2f}x")
print(f"  The BCS coherence weight <Z_BA> = {np.mean(Z_BA_k):.3f} is the")
print(f"  dominant suppression mechanism, selecting only the fraction of the")
print(f"  single-particle excitation that projects onto the collective BA channel.")

# =============================================================================
# 7. Sensitivity analysis: what c_BA gives exact match?
# =============================================================================

print(f"\n{'='*72}")
print(f"  SENSITIVITY ANALYSIS")
print(f"{'='*72}")

# Required E_DM for exact match
E_DM_target = Omega_DM_h2_obs / calibration
E_BA_target = E_DM_target - E_Leggett

print(f"  E_DM (target)  = {E_DM_target:.4f} M_KK")
print(f"  E_BA (target)  = {E_BA_target:.4f} M_KK")

# Scan c_BA
c_BA_scan = np.linspace(0.05, 0.80, 200)
Omh2_scan = np.zeros_like(c_BA_scan)
E_BA_scan = np.zeros_like(c_BA_scan)

for i, c in enumerate(c_BA_scan):
    omega_scan = np.sqrt(omega_L_fold**2 + c**2 * lambda_nonzero)
    eps_scan = c * np.sqrt(lambda_nonzero)
    Z_scan = Delta_0_OES**2 / (Delta_0_OES**2 + eps_scan**2)
    # LZ occupation recalculated with rescaled c_BA
    # d(omega^2)/dt scales as c^2 * |d(E_c*E_J)/dt| * lambda / c_BA_fold^2
    d_omega_sq_dt_scan = d_omega_sq_dt * (c / c_BA_fold)**2
    # But omega^2 also scales, so n_LZ = exp(-pi * omega^2 / |d(omega^2)/dt|)
    # The ratio omega^2 / |d(omega^2)/dt| is approximately independent of c
    # because both scale as c^2. So n_LZ is approximately the same.
    n_scan = n_LZ  # LZ occupation approximately c-independent
    E_BA_scan[i] = np.sum(Z_scan * n_scan * omega_scan)
    Omh2_scan[i] = calibration * (E_Leggett + E_BA_scan[i])

# Find c_BA for exact match
idx_match = np.argmin(np.abs(Omh2_scan - Omega_DM_h2_obs))
c_BA_match = c_BA_scan[idx_match]
print(f"  c_BA for Omega_DM h^2 match: {c_BA_match:.4f} M_KK")
print(f"  Physical c_BA (S64): {c_BA_fold:.4f} M_KK")
print(f"  Ratio: {c_BA_match / c_BA_fold:.3f}")

# Scan Delta_BCS
Delta_scan = np.linspace(0.10, 1.50, 200)
Omh2_Delta = np.zeros_like(Delta_scan)
E_BA_Delta = np.zeros_like(Delta_scan)

for i, d in enumerate(Delta_scan):
    omega_d = omega_BA_coll  # dispersion unchanged
    eps_d = c_BA_fold * np.sqrt(lambda_nonzero)
    Z_d = d**2 / (d**2 + eps_d**2)
    E_BA_Delta[i] = np.sum(Z_d * n_LZ * omega_d)
    Omh2_Delta[i] = calibration * (E_Leggett + E_BA_Delta[i])

idx_Delta_match = np.argmin(np.abs(Omh2_Delta - Omega_DM_h2_obs))
Delta_match = Delta_scan[idx_Delta_match]
print(f"\n  Delta for Omega_DM h^2 match: {Delta_match:.4f} M_KK")
print(f"  Physical Delta (OES): {Delta_0_OES:.4f} M_KK")
print(f"  Ratio: {Delta_match / Delta_0_OES:.3f}")

# =============================================================================
# 8. Gate verdict
# =============================================================================

print(f"\n{'='*72}")
print(f"  GATE VERDICT: BA-WEIGHT-REFINE-66")
print(f"{'='*72}")

# Use the physically motivated Method C result
Omh2_pred = calibration * (E_Leggett + E_BA_proj)
ratio_pred = Omh2_pred / Omega_DM_h2_obs
E_DM_pred = E_Leggett + E_BA_proj

print(f"  E_Leggett      = {E_Leggett:.4f} M_KK")
print(f"  E_BA (proj)    = {E_BA_proj:.4f} M_KK")
print(f"  E_DM (total)   = {E_DM_pred:.4f} M_KK")
print(f"  Omega_DM h^2   = {Omh2_pred:.5f}")
print(f"  Omega_DM h^2 (obs) = {Omega_DM_h2_obs:.5f}")
print(f"  Ratio (pred/obs)   = {ratio_pred:.4f}")

if 0.060 <= Omh2_pred <= 0.242:
    verdict = "PASS"
    detail = (f"Omega_DM h^2 = {Omh2_pred:.5f} within 2x of Planck {Omega_DM_h2_obs:.4f} "
              f"(ratio = {ratio_pred:.3f}). "
              f"Collective projection with BCS coherence weight <Z_BA> = {np.mean(Z_BA_k):.3f} "
              f"replaces S65 free-energy estimate (7.02 -> {E_BA_proj:.2f} M_KK). "
              f"S65 overprediction diagnosed: F_BA included vacuum ZPE (13.26 M_KK) "
              f"and used free energy instead of excitation energy.")
elif Omh2_pred > 1.0 or Omh2_pred < 0.01:
    verdict = "FAIL"
    detail = (f"Omega_DM h^2 = {Omh2_pred:.5f}, gross mismatch with Planck "
              f"(ratio = {ratio_pred:.3f}). Collective projection does not resolve "
              f"the DM abundance problem.")
else:
    verdict = "INFO"
    detail = (f"Omega_DM h^2 = {Omh2_pred:.5f}, ratio = {ratio_pred:.3f} "
              f"(2x < ratio < 5x). Moderate improvement over S65 (ratio was 3.31). "
              f"E_BA = {E_BA_proj:.3f} M_KK from Z-weighted collective projection "
              f"(S65 used F_BA = 7.02 M_KK free energy). "
              f"Remaining overshoot points to additional depletion mechanisms "
              f"(inter-mode scattering, redshift dilution during condensate formation).")

print(f"\n  Gate BA-WEIGHT-REFINE-66: {verdict}")
print(f"  {detail}")

# =============================================================================
# 9. Summary comparison table
# =============================================================================

print(f"\n{'='*72}")
print(f"  SUMMARY: S65 vs S66 REFINEMENT")
print(f"{'='*72}")
print(f"  {'Quantity':<35} {'S65':>12} {'S66':>12} {'Change':>10}")
print(f"  {'-'*35} {'-'*12} {'-'*12} {'-'*10}")

S65_Omh2 = float(d65['Omega_DM_h2_pred'])
S65_EBA = float(d65['E_BA'])
S65_EDM = float(d65['E_DM_total'])

summary = [
    ("E_BA (M_KK)", f"{S65_EBA:.3f}", f"{E_BA_proj:.3f}", f"{E_BA_proj/S65_EBA:.2f}x"),
    ("E_DM = E_L + E_BA (M_KK)", f"{S65_EDM:.3f}", f"{E_DM_pred:.3f}", f"{E_DM_pred/S65_EDM:.2f}x"),
    ("Omega_DM h^2", f"{S65_Omh2:.5f}", f"{Omh2_pred:.5f}", f"{Omh2_pred/S65_Omh2:.2f}x"),
    ("ratio to Planck", f"{S65_Omh2/Omega_DM_h2_obs:.2f}x", f"{ratio_pred:.2f}x", ""),
    ("BA dispersion", "sqrt(E_c*E_J*lam)", "sqrt(oL^2+cBA^2*lam)", "gapped"),
    ("Occupation source", "free energy", "Z-weighted LZ", "proj."),
    ("c_BA (M_KK)", "0.505 (S56)", f"{c_BA_fold} (S64)", "lower"),
    ("<Z_BA> (coherence wt)", "1.0 (none)", f"{np.mean(Z_BA_k):.3f}", "key"),
]

for name, s65, s66, change in summary:
    print(f"  {name:<35} {s65:>12} {s66:>12} {change:>10}")

# =============================================================================
# 10. Save data
# =============================================================================

save_path = os.path.join(outdir, 's66_ba_weight_refine.npz')

np.savez(save_path,
    # CG(24) spectrum
    lambda_CG24=lambda_CG24,
    lambda_nonzero=lambda_nonzero,
    N_modes=N_modes,
    N_cells=N_cells,
    # BA dispersion
    c_BA_fold=c_BA_fold,
    omega_L_fold=omega_L_fold,
    omega_BA_coll=omega_BA_coll,
    omega_BA_S56=omega_BA_S56,
    k_eff_nonzero=k_eff_nonzero,
    # Occupation numbers
    n_LZ=n_LZ,
    n_sudden=n_sudden,
    Z_BA_k=Z_BA_k,
    n_BA_proj=n_BA_proj,
    epsilon_k=epsilon_k,
    # Energies per method
    E_BA_LZ=E_BA_LZ,
    E_BA_SQ=E_BA_SQ,
    E_BA_proj=E_BA_proj,
    E_BA_S65=S65_EBA,
    E_Leggett=E_Leggett,
    # Omega_DM h^2 per method
    Omh2_LZ=calibration * (E_Leggett + E_BA_LZ),
    Omh2_SQ=calibration * (E_Leggett + E_BA_SQ),
    Omh2_proj=Omh2_pred,
    Omh2_S65=S65_Omh2,
    Omh2_obs=Omega_DM_h2_obs,
    # Sensitivity
    c_BA_scan=c_BA_scan,
    Omh2_c_BA_scan=Omh2_scan,
    E_BA_c_BA_scan=E_BA_scan,
    c_BA_match=c_BA_match,
    Delta_scan=Delta_scan,
    Omh2_Delta_scan=Omh2_Delta,
    Delta_match=Delta_match,
    # BCS parameters
    Delta_B2=Delta_0_OES,
    BW_B2=BW_B2,
    W_coll_Anderson=W_coll_Anderson,
    mean_Z_BA=np.mean(Z_BA_k),
    # Calibration
    calibration=calibration,
    ratio_pred_obs=ratio_pred,
    # Gate
    gate_name='BA-WEIGHT-REFINE-66',
    gate_verdict=verdict,
    gate_detail=detail,
)

print(f"\n  Data saved to: {save_path}")

# =============================================================================
# 11. Plot
# =============================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle(f'BA-WEIGHT-REFINE-66: Collective Projection of BA Energy\n'
             f'Gate: {verdict} | Omega_DM h^2 = {Omh2_pred:.4f} (obs: {Omega_DM_h2_obs:.4f})',
             fontsize=13, fontweight='bold')

# --- (a) BA dispersion comparison ---
ax = axes[0, 0]
ax.plot(k_eff_nonzero, omega_BA_S56, 'r--', lw=1.5, label='S56: sqrt(E_c*E_J*lam)')
ax.plot(k_eff_nonzero, omega_BA_coll, 'b-', lw=2, label=f'S66: sqrt(oL^2+cBA^2*lam)')
ax.axhline(omega_L_fold, color='green', ls=':', lw=1, label=f'omega_L = {omega_L_fold:.3f}')
# Linear fit for sound speed
k_low = k_eff_nonzero[:5]
omega_low = omega_BA_coll[:5]
ax.plot(np.linspace(0, 0.6, 50),
        np.sqrt(omega_L_fold**2 + c_BA_fold**2 * np.linspace(0, 0.6, 50)**2),
        'b:', lw=0.8, alpha=0.5)
ax.set_xlabel(r'$k_{\rm eff} = \sqrt{\lambda_k}$', fontsize=12)
ax.set_ylabel(r'$\omega_{\rm BA}(k)$ [$M_{\rm KK}$]', fontsize=12)
ax.set_title('(a) BA phonon dispersion')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# --- (b) BCS coherence weight Z_BA(k) ---
ax = axes[0, 1]
ax.plot(k_eff_nonzero, Z_BA_k, 'b-o', ms=4, lw=1.5, label=r'$Z_{\rm BA}(k) = \Delta^2/(\Delta^2+\epsilon_k^2)$')
ax.axhline(np.mean(Z_BA_k), color='red', ls='--', lw=1.5,
           label=f'<Z_BA> = {np.mean(Z_BA_k):.3f}')
ax.axhline(W_coll_Anderson, color='orange', ls=':', lw=1,
           label=f'Anderson: (Delta/BW)^2 = {W_coll_Anderson:.3f}')
ax.set_xlabel(r'$k_{\rm eff}$', fontsize=12)
ax.set_ylabel(r'$Z_{\rm BA}(k)$', fontsize=12)
ax.set_title(r'(b) Collective projection weight')
ax.legend(fontsize=9)
ax.set_ylim(0, 1.05)
ax.grid(True, alpha=0.3)

# --- (c) Energy comparison ---
ax = axes[1, 0]
labels = ['F_BA\n(S65)', 'E_BA\n(LZ)', 'E_BA\n(SQ)', 'E_BA\n(Z-proj)', 'E_L\n(S65)', 'Target\nE_DM']
vals = [S65_EBA, E_BA_LZ, E_BA_SQ, E_BA_proj, E_Leggett, E_DM_target]
colors = ['#F44336', '#FF9800', '#FFC107', '#4CAF50', '#2196F3', '#9C27B0']
bars = ax.bar(labels, vals, color=colors, edgecolor='black', lw=0.8)
for bar, v in zip(bars, vals):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2,
            f'{v:.2f}', ha='center', va='bottom', fontsize=9)
ax.axhline(E_BA_target, color='purple', ls='--', lw=1.5, alpha=0.7,
           label=f'E_BA target = {E_BA_target:.2f}')
ax.set_ylabel('Energy [$M_{\\rm KK}$]', fontsize=12)
ax.set_title('(c) Energy comparison across methods')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3, axis='y')

# --- (d) Omega_DM h^2 vs c_BA ---
ax = axes[1, 1]
ax.plot(c_BA_scan, Omh2_scan, 'b-', lw=2, label=r'$\Omega_{\rm DM}h^2(c_{\rm BA})$')
ax.axhline(Omega_DM_h2_obs, color='r', ls='--', lw=1.5, label=f'Planck: {Omega_DM_h2_obs:.4f}')
ax.fill_between(c_BA_scan, 0.060, 0.242, alpha=0.1, color='green', label='PASS band')
ax.axvline(c_BA_fold, color='orange', ls='-.', lw=2,
           label=f'Physical c_BA = {c_BA_fold}')
ax.axvline(c_BA_match, color='green', ls=':', lw=1.5,
           label=f'Match c_BA = {c_BA_match:.3f}')
ax.set_xlabel(r'$c_{\rm BA}$ [$M_{\rm KK}$]', fontsize=12)
ax.set_ylabel(r'$\Omega_{\rm DM} h^2$', fontsize=12)
ax.set_title(r'(d) Sensitivity to $c_{\rm BA}$')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
ax.set_xlim(0.05, 0.80)
ax.set_ylim(0, max(0.5, Omh2_scan.max() * 1.1))

plt.tight_layout()
plot_path = os.path.join(outdir, 's66_ba_weight_refine.png')
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"  Plot saved to: {plot_path}")

# =============================================================================
# 12. Final summary
# =============================================================================

print(f"\n{'='*72}")
print(f"  FINAL SUMMARY — BA-WEIGHT-REFINE-66")
print(f"{'='*72}")
print(f"""
  S65 overprediction DIAGNOSED:
    F_BA = 7.02 M_KK was a thermodynamic free energy (ZPE + thermal),
    not the post-transit excitation energy projected onto the collective channel.

  COLLECTIVE PROJECTION (Method C, physically motivated):
    omega_BA(k) = sqrt(omega_L^2 + c_BA^2 * lambda_k)
    n_k^{{BA}} = Z_BA(k) * n_LZ(k)
    Z_BA(k) = Delta^2 / (Delta^2 + epsilon_k^2)  [BCS coherence weight]

    E_BA = {E_BA_proj:.4f} M_KK  (S65 was 7.02 M_KK, reduced by {7.02/E_BA_proj:.1f}x)
    E_DM = E_L + E_BA = {E_Leggett:.3f} + {E_BA_proj:.3f} = {E_DM_pred:.3f} M_KK
    Omega_DM h^2 = {Omh2_pred:.5f}  (obs: {Omega_DM_h2_obs:.5f})
    Ratio = {ratio_pred:.3f}

  KEY PHYSICS: The BCS coherence weight <Z_BA> = {np.mean(Z_BA_k):.3f} selects
  the fraction of single-particle excitations that project onto collective BA
  phonon modes. Higher-k modes have lower Z_BA because they are more
  single-particle-like (epsilon_k >> Delta).

  Gate BA-WEIGHT-REFINE-66: {verdict}
""")

print("BA-WEIGHT-REFINE-66 computation complete.")
