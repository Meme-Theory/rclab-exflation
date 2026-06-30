#!/usr/bin/env python3
"""
s61_pair_cmb.py — PAIR-CMB-61: Pair Transfer CMB Propagation
=============================================================

Gate: PAIR-CMB-61
  PASS if delta_T/T has structure in [1e-6, 1e-4]
  FAIL if flat or outside [1e-8, 1e-2]
  INFO if below Planck sensitivity

Propagation chain (4 links):
  delta_N  -->  delta_Delta  -->  delta_J  -->  delta_T/T

Physics derivation (see full notes in output):
  The pair-transfer strength S_+(N) is measured in ED.  The quantum
  number fluctuation of the BCS-like ground state gives delta_N.
  This propagates through the gap equation sensitivity, the Josephson
  coupling dependence on the gap, and finally the Sachs-Wolfe relation
  connecting vacuum energy fluctuations to CMB temperature.

  CRITICAL: The OES (odd-even staggering) gap alternates in sign by
  construction.  The physical pairing gap is |Delta_OES|, and the
  sensitivity dDelta/dN is the derivative of the ENVELOPE |Delta_OES(N)|,
  not the oscillating quantity.  The alternation reflects the even-odd
  nature of pairing, not a physical instability.

  Furthermore, the gap-to-Josephson chain must account for the fact
  that E_J is set by the GEOMETRY of the inter-cell tunneling, not
  solely by the BCS gap.  The correct sensitivity is:
    delta_J/J = alpha_JD * delta_Delta/Delta
  where alpha_JD is the Josephson-gap elasticity (= 1 for weak coupling,
  = 2 for Ambegaokar-Baratoff).

Created: S61 (2026-03-28)
"""

import numpy as np
import matplotlib.pyplot as plt
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from canonical_constants import (
    E_cond, M_KK, tau_fold, Delta_0_OES, Delta_0_GL,
    A_s_CMB, T_CMB, rho_Lambda_obs, N_cells, J_C2, J_su2, J_u1,
    E_B1, E_B2_mean, E_B3_mean, a0_fold, rho_crit_GeV4,
    Omega_Lambda, Omega_m, S_fold, Delta_B3,
    E_cond_ED_8mode, N_dof_BCS
)

# --------------------------------------------------------------------------
# 0. Load data
# --------------------------------------------------------------------------
data_dir = os.path.dirname(__file__)

pt = np.load(os.path.join(data_dir, 's60_pair_transfer_n4.npz'), allow_pickle=True)
st = np.load(os.path.join(data_dir, 's60_staircase_ext.npz'), allow_pickle=True)
rg = np.load(os.path.join(data_dir, 's60_rg_integrals.npz'), allow_pickle=True)
hfb = np.load(os.path.join(data_dir, 's52_hfb_full.npz'), allow_pickle=True)

# Ground state energies from ED
N_max_pt = 5
E_GS = np.array([float(pt[f'E_GS_N{n}']) for n in range(N_max_pt + 1)])
S_plus = np.array([float(pt[f'S_plus_N{n}']) for n in range(N_max_pt)])

# Mode parameters
eps_fold = pt['eps_fold']
V_fold = pt['V_fold']
E_J_fold = float(pt['E_J_fold'])
N_modes = int(pt['N_modes'])
N_cells_data = int(pt['N_cells'])
N_slots = int(pt['N_slots'])  # 16 = 2 cells x 8 modes

print("=" * 72)
print("PAIR-CMB-61: Pair Transfer -> CMB Temperature Fluctuation Chain")
print("=" * 72)

# ==========================================================================
# STEP 1: Pair-number fluctuation delta_N
# ==========================================================================
print("\n--- STEP 1: Number fluctuation delta_N ---")
print("  Method: var(N) = Sum_k n_k(1-n_k) from ED occupations (Paper 03)")

# ED occupation numbers from HFB data
n_k_ed = {}
for N in range(1, 5):
    key = f'N{N}_n_k_ed'
    if key in hfb.files:
        n_k_ed[N] = hfb[key]

var_N = {}
delta_N = {}
for N in range(1, 5):
    nk = n_k_ed[N]
    var = np.sum(nk * (1.0 - nk))
    var_N[N] = var
    delta_N[N] = np.sqrt(var)

print(f"  {'N':>3}  {'var(N)':>10}  {'delta_N':>10}  {'var/N':>10}")
for N in range(1, 5):
    print(f"  {N:3d}  {var_N[N]:10.6f}  {delta_N[N]:10.6f}  {var_N[N]/N:10.6f}")

# Nuclear cross-check: var/N ~ 0.5 at half-filling (BCS limit)
# N=3: var/N=0.45, close to BCS; N=1: var/N=0.76, particle-like
print("  Nuclear benchmark: var/N -> 0.5 at half-filling (sd-shell)")

# ==========================================================================
# STEP 2: Gap sensitivity dDelta/dN
# ==========================================================================
print("\n--- STEP 2: Pairing gap and its N-sensitivity ---")

# --- 2a: OES gap (standard nuclear physics extraction, Paper 03) ---
# Delta_OES(N) = (-1)^N [E(N+1) - 2E(N) + E(N-1)] / 2
Delta_OES_raw = {}
for N in range(1, N_max_pt):
    sign = (-1)**N
    Delta_OES_raw[N] = sign * (E_GS[N+1] - 2*E_GS[N] + E_GS[N-1]) / 2.0

print("  OES gaps (raw, alternating sign):")
for N in sorted(Delta_OES_raw.keys()):
    print(f"    N={N}: Delta_OES_raw = {Delta_OES_raw[N]:+.6f} M_KK")

# --- 2b: Gap ENVELOPE ---
# The physical pairing gap is |Delta_OES|.  The alternation is the
# odd-even effect itself, not a physical instability.
# In nuclear physics, we ALWAYS take |Delta_OES|.
Delta_env = {N: abs(Delta_OES_raw[N]) for N in Delta_OES_raw}
print("\n  Gap envelope |Delta_OES|:")
for N in sorted(Delta_env.keys()):
    print(f"    N={N}: |Delta_OES| = {Delta_env[N]:.6f} M_KK")

# --- 2c: Derivative of envelope d|Delta|/dN ---
# CRITICAL: Use envelope derivative, not raw derivative.
# The raw dDelta/dN includes the sign flip (~2*Delta per step),
# which is an ARTIFACT of the OES convention, not a physical sensitivity.
Ns = sorted(Delta_env.keys())
d_env_dN = {}
for i, N in enumerate(Ns):
    if i == 0:
        d_env_dN[N] = Delta_env[Ns[i+1]] - Delta_env[N]
    elif i == len(Ns) - 1:
        d_env_dN[N] = Delta_env[N] - Delta_env[Ns[i-1]]
    else:
        d_env_dN[N] = (Delta_env[Ns[i+1]] - Delta_env[Ns[i-1]]) / 2.0

print("\n  Envelope derivative d|Delta|/dN:")
for N in sorted(d_env_dN.keys()):
    print(f"    N={N}: d|Delta|/dN = {d_env_dN[N]:+.6f} M_KK")

# --- 2d: Richardson gap (from RG integrals) ---
Delta_Rich = float(rg['mean_delta_full'])
Delta_Rich_noJ = float(rg['mean_delta_noJ'])
print(f"\n  Richardson gap (full):  {Delta_Rich:.6f} M_KK")
print(f"  Richardson gap (no J):  {Delta_Rich_noJ:.6f} M_KK")
print(f"  Canonical Delta_B3:     {Delta_B3:.6f} M_KK")

# --- 2e: Gap fluctuation delta_Delta = |d|Delta|/dN| * delta_N ---
delta_Delta = {}
for N in range(1, 5):
    if N in d_env_dN and N in delta_N:
        delta_Delta[N] = abs(d_env_dN[N]) * delta_N[N]

print("\n  Gap fluctuation delta_Delta = |d|Delta|/dN| * delta_N:")
for N in sorted(delta_Delta.keys()):
    print(f"    N={N}: delta_Delta = {delta_Delta[N]:.6f} M_KK")

# ==========================================================================
# STEP 3: Josephson coupling fluctuation delta_J/J
# ==========================================================================
print("\n--- STEP 3: Josephson coupling fluctuation ---")

# The Josephson coupling E_J between cells depends on the pair overlap
# integral across the inter-cell barrier.  Three models:
#
# Model A (weak-coupling): J ~ Delta (BCS tunneling)
#   dJ/dDelta = J/Delta  =>  delta_J/J = delta_Delta/Delta
#
# Model B (Ambegaokar-Baratoff): J ~ Delta^2/E_barrier
#   dJ/dDelta = 2J/Delta =>  delta_J/J = 2 * delta_Delta/Delta
#
# Model C (geometric): J set by SU(3) geometry, weak Delta-dependence
#   dJ/dDelta ~ alpha_geom * J/Delta, alpha_geom << 1
#   This is the case when E_J >> Delta (as here: E_J/Delta_env ~ 3.7)

# Reference gap for the denominator
Delta_ref_env = np.mean([Delta_env[N] for N in Delta_env])
print(f"  Mean envelope gap: {Delta_ref_env:.6f} M_KK")
print(f"  E_J_fold: {E_J_fold:.6f} M_KK")
print(f"  E_J/Delta_env = {E_J_fold/Delta_ref_env:.3f}")
print(f"  E_J/Delta_Rich = {E_J_fold/Delta_Rich:.3f}")

# Since E_J >> Delta, we are in the strong-Josephson limit where the
# coupling is set primarily by the geometry (barrier transparency),
# not by the gap amplitude.  The sensitivity is SUPPRESSED.
# In nuclear physics (Paper 18, pair transfer), the transfer integral
# depends on the overlap of Cooper-pair wave functions across the barrier.
# For a deep barrier, this goes as:
#   T ~ exp(-kappa * d) * (Delta/E_barrier)
# where kappa is the evanescent wavevector.
# The elasticity alpha_JD = d ln J / d ln Delta ~ 1 for this case.

# But there is a CRUCIAL suppression: the fluctuation at the CMB
# is not the local delta_J at one cell -- it is the SPATIAL AVERAGE
# over N_cells cells within a Hubble volume.  The central limit theorem
# gives a sqrt(N_cells) suppression.
N_hubble = N_cells  # 32 cells in fabric
sqrt_N_suppress = 1.0 / np.sqrt(N_hubble)
print(f"\n  Spatial averaging suppression: 1/sqrt(N_cells={N_hubble}) = {sqrt_N_suppress:.4f}")

delta_J_over_J = {}
for N in range(1, 5):
    if N in delta_Delta:
        Delta_N = Delta_env[N]
        if Delta_N < 1e-10:
            Delta_N = Delta_ref_env

        # Three J-Delta models
        djj_A = delta_Delta[N] / Delta_N                    # weak coupling
        djj_B = 2.0 * delta_Delta[N] / Delta_N              # Ambegaokar-Baratoff
        djj_C = delta_Delta[N] / Delta_N * (Delta_N / E_J_fold)  # geometric suppression

        # Apply spatial averaging
        djj_A *= sqrt_N_suppress
        djj_B *= sqrt_N_suppress
        djj_C *= sqrt_N_suppress

        # Geometric mean of A and B as central estimate
        djj_geom = np.sqrt(djj_A * djj_B)

        delta_J_over_J[N] = {
            'weak': djj_A,
            'AB': djj_B,
            'geometric': djj_C,
            'central': djj_geom,
        }
        print(f"  N={N}: delta_J/J = {djj_A:.4e} (weak), "
              f"{djj_B:.4e} (AB), {djj_C:.4e} (geom), {djj_geom:.4e} (central)")

# ==========================================================================
# STEP 4: CMB temperature fluctuation delta_T/T
# ==========================================================================
print("\n--- STEP 4: CMB temperature fluctuation delta_T/T ---")

# Three physical channels connect delta_J to delta_T/T:
#
# Channel 1: Primordial Sachs-Wolfe
#   delta_T/T = (1/3) * delta_Phi_N  (adiabatic, large scale)
#   delta_Phi_N = (delta_rho_vac / rho_total) at horizon crossing
#   rho_vac from BCS: E_cond * M_KK^4 ~ -0.137 * (7.4e16)^4 GeV^4
#   rho_total at transit: dominated by kinetic/geometric energy
#   The fraction: f_cond = |E_cond| / E_total(N)
#   where E_total(N) comes from the ED ground state energy
#
# Channel 2: Isocurvature (CC fluctuation at z=1100)
#   Omega_Lambda(z=1100) ~ 1.6e-9 -- negligible
#   delta_T/T_iso = Omega_Lambda(z_ls) * delta_J/J << 10^{-9}
#
# Channel 3: Late-time ISW
#   delta_T/T_ISW ~ 2 * f_ISW * Omega_Lambda_0 * delta_Lambda/Lambda
#   f_ISW ~ 0.10 from LCDM transfer function
#
# The DOMINANT channel is EITHER primordial (if the pair fluctuation
# is generated during transit and freezes in) OR ISW (if the fluctuation
# persists to late times).

# --- Channel 1: Primordial SW ---
print("\n  Channel 1: Primordial Sachs-Wolfe")
# E_total per cell at transit: include kinetic + BCS + Josephson
# From ED: E_GS(N) is the full 2-cell energy including E_J
# Per-cell energy: E_cell(N) ~ E_GS(N) / N_cells_data + E_J_fold
# The condensation energy fraction:
dTT_prim = {}
for N in range(1, 5):
    if N not in delta_J_over_J:
        continue
    E_gs_abs = abs(E_GS[N])
    # Condensation fraction: how much of the total energy is "vacuum"
    f_cond = abs(E_cond_ED_8mode) / (E_gs_abs / N_cells_data) if E_gs_abs > 0 else 0
    # But the CMB is sensitive to the FLUCTUATION of the vacuum component
    # delta_T/T = (1/3) * f_cond * delta_J/J
    djj = delta_J_over_J[N]['central']
    dtt = (1.0 / 3.0) * f_cond * djj
    dTT_prim[N] = dtt
    print(f"    N={N}: f_cond={f_cond:.4f}, delta_J/J={djj:.4e}, "
          f"delta_T/T = {dtt:.4e}")

# --- Channel 2: Isocurvature ---
z_ls = 1100.0  # (local)
E_z_ls = np.sqrt(Omega_m * (1 + z_ls)**3 + Omega_Lambda)
Omega_Lam_ls = Omega_Lambda / E_z_ls**2
print(f"\n  Channel 2: Isocurvature at z={z_ls:.0f}")
print(f"    Omega_Lambda(z=1100) = {Omega_Lam_ls:.3e}")
dTT_iso = {}
for N in range(1, 5):
    if N in delta_J_over_J:
        dtt = Omega_Lam_ls * delta_J_over_J[N]['central']
        dTT_iso[N] = dtt

# --- Channel 3: ISW ---
f_ISW = 0.10  # (local)
print(f"\n  Channel 3: Integrated Sachs-Wolfe (f_ISW={f_ISW})")
dTT_ISW = {}
for N in range(1, 5):
    if N in delta_J_over_J:
        djj = delta_J_over_J[N]['central']
        dtt = 2 * Omega_Lambda * djj * f_ISW
        dTT_ISW[N] = dtt
        print(f"    N={N}: delta_T/T_ISW = {dtt:.4e}")

# ==========================================================================
# STEP 5: Combined results
# ==========================================================================
print("\n" + "=" * 72)
print("COMBINED RESULTS (all channels)")
print("=" * 72)

N_arr = np.array([1, 2, 3, 4])
delta_N_arr = np.array([delta_N[N] for N in N_arr])
Delta_env_arr = np.array([Delta_env[N] for N in N_arr])
d_env_dN_arr = np.array([d_env_dN[N] for N in N_arr])
delta_Delta_arr = np.array([delta_Delta[N] for N in N_arr])

djj_weak_arr = np.array([delta_J_over_J[N]['weak'] for N in N_arr])
djj_AB_arr = np.array([delta_J_over_J[N]['AB'] for N in N_arr])
djj_geom_arr = np.array([delta_J_over_J[N]['geometric'] for N in N_arr])
djj_central_arr = np.array([delta_J_over_J[N]['central'] for N in N_arr])

dTT_prim_arr = np.array([dTT_prim[N] for N in N_arr])
dTT_ISW_arr = np.array([dTT_ISW[N] for N in N_arr])
dTT_iso_arr = np.array([dTT_iso[N] for N in N_arr])

# Total: sum of channels
dTT_total = dTT_prim_arr + dTT_ISW_arr + dTT_iso_arr

# Uncertainty band: weak vs AB J-Delta model
E_gs_arr = np.array([abs(E_GS[N]) for N in N_arr])
f_cond_arr = np.array([abs(E_cond_ED_8mode) / (abs(E_GS[N]) / N_cells_data)
                        for N in N_arr])
dTT_lo = (1.0/3.0) * f_cond_arr * djj_weak_arr + dTT_ISW_arr * (djj_weak_arr / djj_central_arr) + dTT_iso_arr
dTT_hi = (1.0/3.0) * f_cond_arr * djj_AB_arr + dTT_ISW_arr * (djj_AB_arr / djj_central_arr) + dTT_iso_arr

# Also compute with geometric-suppression model (most conservative)
dTT_geom_model = (1.0/3.0) * f_cond_arr * djj_geom_arr

header = (f"{'N':>3}  {'delta_N':>9}  {'|Delta|':>9}  {'d|D|/dN':>9}  "
          f"{'dDelta':>9}  {'dJ/J':>10}  {'dT/T_SW':>10}  "
          f"{'dT/T_ISW':>10}  {'dT/T_tot':>10}")
print(f"\n{header}")
print("-" * len(header))
for i, N in enumerate(N_arr):
    print(f"{N:3d}  {delta_N_arr[i]:9.5f}  {Delta_env_arr[i]:9.5f}  "
          f"{d_env_dN_arr[i]:+9.5f}  {delta_Delta_arr[i]:9.5f}  "
          f"{djj_central_arr[i]:10.4e}  {dTT_prim_arr[i]:10.4e}  "
          f"{dTT_ISW_arr[i]:10.4e}  {dTT_total[i]:10.4e}")

# Structure assessment
dTT_abs = np.abs(dTT_total)
dTT_range = np.max(dTT_abs) / np.min(dTT_abs) if np.min(dTT_abs) > 0 else np.inf
dTT_cv = np.std(dTT_abs) / np.mean(dTT_abs)

print(f"\n  Mean |delta_T/T|:  {np.mean(dTT_abs):.4e}")
print(f"  Range (max/min):   {dTT_range:.3f}")
print(f"  CV:                {dTT_cv:.4f}")

# ==========================================================================
# STEP 6: N-dependence analysis (STRUCTURE test)
# ==========================================================================
print("\n--- STEP 6: N-dependence structure ---")

# The key question: does delta_T/T have STRUCTURE in N, or is it flat?
# Structure means: the pair-number dependence of the gap creates a
# non-trivial N-mode spectrum in the CMB.
# Flat means: all N sectors contribute equally.

# Test: fit delta_T/T(N) to a constant and measure chi^2
dTT_mean_val = np.mean(dTT_total)
chi2_flat = np.sum((dTT_total - dTT_mean_val)**2) / dTT_mean_val**2
print(f"  chi^2(flat model, 3 dof): {chi2_flat:.4f}")

# Test: correlation of delta_T/T with N
corr_N = np.corrcoef(N_arr, dTT_total)[0, 1]
print(f"  Pearson correlation (delta_T/T vs N): {corr_N:.4f}")

# Per-mode analysis from pair-transfer profiles
print("\n  Per-mode pair-transfer weights:")
P_plus_N1 = pt['P_plus_N1']
P_plus_N2 = pt['P_plus_N2']
w_k_N1 = np.abs(P_plus_N1) / S_plus[1]
w_k_N2 = np.abs(P_plus_N2) / S_plus[2]
unif_N1 = np.max(w_k_N1) / np.min(w_k_N1)
unif_N2 = np.max(w_k_N2) / np.min(w_k_N2)
print(f"    N=1 uniformity (max/min): {unif_N1:.4f}")
print(f"    N=2 uniformity (max/min): {unif_N2:.4f}")
print(f"    (Near 1.0 = uniform; >> 1 = Fermi-surface concentrated)")

# ==========================================================================
# STEP 7: Suppression factor analysis
# ==========================================================================
print("\n--- STEP 7: Suppression hierarchy ---")

# Track each suppression factor in the chain:
# 1. Envelope smoothing: |d|Delta|/dN| << |dDelta_raw/dN|
# 2. Gap-to-J suppression: Delta/E_J << 1
# 3. Spatial averaging: 1/sqrt(N_cells)
# 4. Condensation fraction: |E_cond| / E_total

# Reference: unsuppressed estimate
# delta_T/T_raw ~ delta_N * (1/E_J) * 1/3
delta_T_raw = np.mean(delta_N_arr) / 3.0
print(f"  Raw (no suppression): delta_T/T ~ delta_N/3 = {delta_T_raw:.4f}")

# Factor 1: envelope smoothing
f1 = np.mean(np.abs(d_env_dN_arr)) / np.mean(Delta_env_arr)
print(f"  F1 (envelope smoothing): d|D|/dN / |D| = {f1:.4e}")

# Factor 2: gap/Josephson
f2 = Delta_ref_env / E_J_fold
print(f"  F2 (gap/Josephson):      Delta/E_J = {f2:.4e}")

# Factor 3: spatial averaging
f3 = sqrt_N_suppress
print(f"  F3 (spatial avg):        1/sqrt(N) = {f3:.4e}")

# Factor 4: condensation fraction
f4 = np.mean(f_cond_arr)
print(f"  F4 (condensation frac):  |E_cond|/E = {f4:.4e}")

# Combined
f_total = f1 * f3 * f4  # F2 is already in the geometric model
delta_T_suppressed = delta_T_raw * f1 * f3 * f4
print(f"\n  Combined suppression: {f1*f3*f4:.4e}")
print(f"  Suppressed estimate: delta_T/T ~ {delta_T_suppressed:.4e}")

# ==========================================================================
# STEP 8: Bayesian uncertainty (3 J-Delta models)
# ==========================================================================
print("\n--- STEP 8: Uncertainty quantification ---")

# Three models for the J-Delta relation:
# Model A: J ~ Delta            (weak coupling)
# Model B: J ~ Delta^2          (Ambegaokar-Baratoff)
# Model C: J ~ Delta * T_geom   (geometric, T_geom = Delta/E_J)
# Assign equal prior weight to each

dTT_models = np.zeros((3, len(N_arr)))
model_names = ['Weak (J~D)', 'AB (J~D^2)', 'Geom (J~D^2/E_J)']

for i, N in enumerate(N_arr):
    # Model A
    dTT_models[0, i] = (1/3) * f_cond_arr[i] * djj_weak_arr[i] + dTT_ISW_arr[i]
    # Model B
    dTT_models[1, i] = (1/3) * f_cond_arr[i] * djj_AB_arr[i] + dTT_ISW_arr[i] * (djj_AB_arr[i]/djj_central_arr[i])
    # Model C
    dTT_models[2, i] = (1/3) * f_cond_arr[i] * djj_geom_arr[i] + dTT_ISW_arr[i] * (djj_geom_arr[i]/djj_central_arr[i])

print(f"  {'Model':<20}  {'N=1':>10}  {'N=2':>10}  {'N=3':>10}  {'N=4':>10}")
for m in range(3):
    vals = '  '.join(f'{dTT_models[m, i]:10.4e}' for i in range(4))
    print(f"  {model_names[m]:<20}  {vals}")

# Bayesian equal-weight average
dTT_bayesian = np.mean(dTT_models, axis=0)
dTT_bayesian_std = np.std(dTT_models, axis=0)
print(f"\n  {'Bayesian mean':<20}  " +
      '  '.join(f'{dTT_bayesian[i]:10.4e}' for i in range(4)))
print(f"  {'Bayesian std':<20}  " +
      '  '.join(f'{dTT_bayesian_std[i]:10.4e}' for i in range(4)))
print(f"  {'Frac. uncertainty':<20}  " +
      '  '.join(f'{dTT_bayesian_std[i]/abs(dTT_bayesian[i]):10.2%}' if abs(dTT_bayesian[i]) > 0 else f'{"N/A":>10}' for i in range(4)))

# ==========================================================================
# STEP 9: Gate assessment
# ==========================================================================
print("\n" + "=" * 72)
print("GATE ASSESSMENT: PAIR-CMB-61")
print("=" * 72)

# Use Bayesian mean as the primary result
dTT_gate = np.mean(np.abs(dTT_bayesian))
dTT_max = np.max(np.abs(dTT_bayesian))
dTT_min = np.min(np.abs(dTT_bayesian))
dTT_range_gate = dTT_max / dTT_min if dTT_min > 0 else np.inf

print(f"\n  Bayesian mean |delta_T/T|: {dTT_gate:.4e}")
print(f"  Range [{dTT_min:.3e}, {dTT_max:.3e}]")
print(f"  Max/min ratio: {dTT_range_gate:.2f}")
print(f"  log10(mean): {np.log10(dTT_gate):.2f}")

# Also report the most conservative model (geometric suppression)
dTT_conservative = np.mean(np.abs(dTT_models[2]))
print(f"\n  Most conservative (geometric): {dTT_conservative:.4e}")
print(f"  log10(conservative): {np.log10(dTT_conservative) if dTT_conservative > 0 else 'N/A':.2f}")

# Gate logic
has_structure = dTT_range_gate > 1.2

if 1e-6 <= dTT_gate <= 1e-4 and has_structure:
    gate_verdict = "PASS"
    gate_detail = (f"Bayesian mean delta_T/T = {dTT_gate:.2e} in [1e-6,1e-4], "
                   f"structured (max/min={dTT_range_gate:.1f})")
elif dTT_gate > 1e-2:
    gate_verdict = "FAIL"
    gate_detail = (f"Bayesian mean delta_T/T = {dTT_gate:.2e} > 1e-2 (too large). "
                   f"Conservative model: {dTT_conservative:.2e}")
elif dTT_gate < 1e-8:
    gate_verdict = "FAIL"
    gate_detail = (f"Bayesian mean delta_T/T = {dTT_gate:.2e} < 1e-8 (undetectable)")
elif dTT_gate < 1e-6:
    gate_verdict = "INFO"
    gate_detail = (f"Bayesian mean delta_T/T = {dTT_gate:.2e} below Planck 1e-6. "
                   f"Conservative: {dTT_conservative:.2e}")
elif 1e-6 <= dTT_gate <= 1e-4 and not has_structure:
    gate_verdict = "INFO"
    gate_detail = (f"delta_T/T = {dTT_gate:.2e} in range but flat "
                   f"(max/min={dTT_range_gate:.2f})")
elif dTT_gate > 1e-4:
    # Between 1e-4 and 1e-2: marginally too large
    gate_verdict = "FAIL"
    gate_detail = (f"Bayesian mean delta_T/T = {dTT_gate:.2e} in (1e-4,1e-2). "
                   f"Requires additional suppression. Conservative: {dTT_conservative:.2e}")
else:
    # 1e-8 to 1e-6
    gate_verdict = "INFO"
    gate_detail = (f"delta_T/T = {dTT_gate:.2e} in [1e-8,1e-6] sub-Planck range")

print(f"\n  >>> VERDICT: {gate_verdict}")
print(f"  >>> DETAIL:  {gate_detail}")

# Physical diagnosis
print("\n  === Diagnostic summary ===")
print(f"  Chain: delta_N={np.mean(delta_N_arr):.3f} "
      f"--> delta_Delta={np.mean(delta_Delta_arr):.4e} "
      f"--> delta_J/J={np.mean(djj_central_arr):.4e} "
      f"--> delta_T/T={dTT_gate:.4e}")
print(f"  Dominant suppression: envelope smoothing (d|Delta|/dN / |Delta| = {f1:.4e})")
print(f"  Secondary: spatial averaging (1/sqrt(32) = {f3:.4f})")
print(f"  Tertiary: condensation fraction ({np.mean(f_cond_arr):.4f})")

if dTT_gate > 1e-4:
    print("\n  PHYSICS NOTE: delta_T/T too large by factor "
          f"{dTT_gate/1e-5:.1f} relative to CMB observed 10^{-5}.")
    print("  The pair-number fluctuation propagates TOO EFFICIENTLY")
    print("  through the Josephson channel.  This means either:")
    print("    (a) The J-Delta coupling is weaker than ANY model tested, or")
    print("    (b) An additional suppression mechanism exists (e.g., phase")
    print("        averaging, decoherence during transit, or number projection), or")
    print("    (c) The pair-transfer signal is an isocurvature mode that is")
    print("        diluted by the dominant adiabatic perturbations.")

# ==========================================================================
# STEP 10: Save data
# ==========================================================================
save_path = os.path.join(data_dir, 's61_pair_cmb.npz')
np.savez(save_path,
    # Input parameters
    N_arr=N_arr,
    E_GS=E_GS,
    S_plus=S_plus,
    eps_fold=eps_fold,
    E_J_fold=E_J_fold,
    N_modes=N_modes,
    N_cells=N_cells_data,
    N_slots=N_slots,
    # Step 1: number fluctuation
    delta_N=delta_N_arr,
    var_N=np.array([var_N[N] for N in N_arr]),
    # Step 2: gap
    Delta_OES_raw=np.array([Delta_OES_raw[N] for N in N_arr]),
    Delta_env=Delta_env_arr,
    d_env_dN=d_env_dN_arr,
    delta_Delta=delta_Delta_arr,
    Delta_ref_env=Delta_ref_env,
    Delta_Rich=Delta_Rich,
    # Step 3: Josephson
    djj_weak=djj_weak_arr,
    djj_AB=djj_AB_arr,
    djj_geometric=djj_geom_arr,
    djj_central=djj_central_arr,
    sqrt_N_suppress=sqrt_N_suppress,
    # Step 4-5: delta_T/T
    dTT_primordial=dTT_prim_arr,
    dTT_ISW=dTT_ISW_arr,
    dTT_isocurvature=dTT_iso_arr,
    dTT_total=dTT_total,
    dTT_models=dTT_models,
    dTT_bayesian_mean=dTT_bayesian,
    dTT_bayesian_std=dTT_bayesian_std,
    model_names=np.array(model_names),
    # Structure
    dTT_range=dTT_range_gate,
    dTT_cv=dTT_cv,
    f_cond=f_cond_arr,
    # Suppression
    f_envelope=f1,
    f_spatial_avg=f3,
    f_cond_mean=f4,
    # Per-mode
    P_plus_N1=P_plus_N1,
    P_plus_N2=P_plus_N2,
    w_k_N1=w_k_N1,
    w_k_N2=w_k_N2,
    # Gate
    gate_name=np.array(['PAIR-CMB-61']),
    gate_verdict=np.array([gate_verdict]),
    gate_detail=np.array([gate_detail]),
)
print(f"\n  Data saved: {save_path}")

# ==========================================================================
# STEP 11: Plot
# ==========================================================================
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle('PAIR-CMB-61: Pair Transfer $\\rightarrow$ CMB Propagation Chain',
             fontsize=14, fontweight='bold')

# Panel (a): delta_N vs N
ax = axes[0, 0]
ax.plot(N_arr, delta_N_arr, 'bo-', linewidth=2, markersize=8)
ax.set_xlabel('N (pair number)', fontsize=12)
ax.set_ylabel(r'$\delta N$', fontsize=12)
ax.set_title('(a) Number fluctuation', fontsize=12)
ax.grid(True, alpha=0.3)
ax.set_xticks(N_arr)

# Panel (b): Gap envelope vs N
ax = axes[0, 1]
ax.plot(N_arr, Delta_env_arr, 'rs-', linewidth=2, markersize=8)
ax.fill_between(N_arr, Delta_env_arr - delta_Delta_arr,
                Delta_env_arr + delta_Delta_arr, alpha=0.2, color='red')
ax.set_xlabel('N', fontsize=12)
ax.set_ylabel(r'$|\Delta_{OES}|$ (M$_{KK}$)', fontsize=12)
ax.set_title('(b) OES gap envelope', fontsize=12)
ax.grid(True, alpha=0.3)
ax.set_xticks(N_arr)

# Panel (c): d|Delta|/dN
ax = axes[0, 2]
ax.bar(N_arr, d_env_dN_arr, color='seagreen', alpha=0.8, edgecolor='black')
ax.axhline(0, color='gray', linestyle='--', alpha=0.5)
ax.set_xlabel('N', fontsize=12)
ax.set_ylabel(r'd$|\Delta|$/dN (M$_{KK}$)', fontsize=12)
ax.set_title('(c) Gap envelope derivative', fontsize=12)
ax.grid(True, alpha=0.3, axis='y')
ax.set_xticks(N_arr)

# Panel (d): delta_J/J (three models)
ax = axes[1, 0]
ax.semilogy(N_arr, np.abs(djj_weak_arr), 'b--o', label=r'J $\sim \Delta$', markersize=6)
ax.semilogy(N_arr, np.abs(djj_AB_arr), 'r--s', label=r'J $\sim \Delta^2$', markersize=6)
ax.semilogy(N_arr, np.abs(djj_geom_arr), 'g--^', label=r'J $\sim \Delta^2/E_J$', markersize=6)
ax.semilogy(N_arr, np.abs(djj_central_arr), 'k-D', label='Central', linewidth=2, markersize=8)
ax.set_xlabel('N', fontsize=12)
ax.set_ylabel(r'$|\delta J/J|$', fontsize=12)
ax.set_title(r'(d) Josephson fluctuation ($\times 1/\sqrt{32}$)', fontsize=12)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
ax.set_xticks(N_arr)

# Panel (e): delta_T/T (all channels + Planck band)
ax = axes[1, 1]
ax.semilogy(N_arr, np.abs(dTT_prim_arr), 'ro-', label='Primordial SW',
            linewidth=2, markersize=8)
ax.semilogy(N_arr, np.abs(dTT_ISW_arr), 'bs-', label='ISW',
            linewidth=2, markersize=8)
ax.semilogy(N_arr, np.abs(dTT_bayesian), 'k-D', label='Bayesian mean',
            linewidth=2.5, markersize=10)
# Error bars from model spread
for i in range(len(N_arr)):
    lo = abs(dTT_bayesian[i]) - dTT_bayesian_std[i]
    hi = abs(dTT_bayesian[i]) + dTT_bayesian_std[i]
    if lo < 1e-15:
        lo = 1e-15
    ax.plot([N_arr[i], N_arr[i]], [lo, hi], 'k-', linewidth=1.5)
# Planck sensitivity
ax.axhspan(1e-6, 1e-4, alpha=0.1, color='gold', label='Planck range')
ax.axhline(1e-5, color='orange', linestyle=':', alpha=0.5, label=r'CMB $\delta T/T$')
ax.set_xlabel('N', fontsize=12)
ax.set_ylabel(r'$|\delta T/T|$', fontsize=12)
ax.set_title('(e) CMB temperature fluctuation', fontsize=12)
ax.legend(fontsize=8, loc='best')
ax.grid(True, alpha=0.3)
ax.set_xticks(N_arr)
ax.set_ylim(1e-10, 1e1)

# Panel (f): Model comparison bar chart (N=2)
ax = axes[1, 2]
model_vals_N2 = [abs(dTT_models[m, 1]) for m in range(3)]
colors = ['steelblue', 'indianred', 'seagreen']
bars = ax.bar(range(3), model_vals_N2, color=colors, alpha=0.8, edgecolor='black')
ax.set_yscale('log')
ax.set_xticks(range(3))
ax.set_xticklabels(['J~$\\Delta$', 'J~$\\Delta^2$', 'J~$\\Delta^2/E_J$'],
                    fontsize=10)
ax.axhline(1e-5, color='orange', linestyle=':', alpha=0.7, label=r'CMB $\delta T/T$')
ax.axhspan(1e-6, 1e-4, alpha=0.1, color='gold', label='Planck range')
ax.set_ylabel(r'$|\delta T/T|$ at N=2', fontsize=12)
ax.set_title('(f) Model comparison (N=2)', fontsize=12)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plot_path = os.path.join(data_dir, 's61_pair_cmb.png')
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"  Plot saved: {plot_path}")

print("\n" + "=" * 72)
print(f"FINAL GATE VERDICT: PAIR-CMB-61 = {gate_verdict}")
print(f"  {gate_detail}")
print("=" * 72)
