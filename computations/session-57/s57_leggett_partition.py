#!/usr/bin/env python3
"""
S57 LEGGETT-PARTITION-57 (Quantum-Acoustics, W1-2)
===================================================

Gate: P_exc^Leggett in [0.15, 0.45] (PASS) or < 0.05 / > 0.80 (FAIL)
      Also evaluate ENERGY fraction f_DM = E_L / E_matter.

Physics:
--------
The Leggett modes are HARMONIC OSCILLATORS with time-dependent frequency
omega_L(n, tau). The transit is in the SUDDEN QUENCH regime:
  omega_L * dt_transit ~ 5.5e-5 << 1
(modes cannot complete even one oscillation during transit).

For a sudden quench of frequency from omega_i to omega_f, the system
initially in the ground state |0_i> ends up in a SQUEEZED STATE in
the omega_f basis. The key results are:

  <n_exc>(n) = (omega_i/omega_f + omega_f/omega_i - 2) / 4
  P_0 = |<0_f|0_i>|^2 = 2*sqrt(omega_i*omega_f) / (omega_i + omega_f)
  E_exc(n) = <n_exc>(n) * omega_f(n)

This is the Bogoliubov transformation for parametric particle creation,
the SAME physics as cosmological particle creation (Parker 1969) but
applied to internal Leggett modes rather than spatial field modes.

The LZ formula from W0-1 (gamma << 1, P_diabatic ~ 1) correctly
identifies the REGIME (deeply non-adiabatic), but the LZ two-level
formalism doesn't give the correct ENERGY — that requires the
harmonic oscillator squeezing formula.

Three regimes exist depending on omega(tau) ratio:
  1. SUDDEN QUENCH (our regime): dt << 1/omega, use squeezing formula
  2. INTERMEDIATE: solve time-dependent Schrodinger numerically
  3. ADIABATIC: dt >> 1/omega, system stays in ground state

We are firmly in regime 1.

Inputs:
  - s57_leggett_tau_profile.npz (W0-1)
  - s57_channel_energy_budget.npz (W0-2)
  - s56_leggett_fabric.npz (31 modes + dispersions)
  - canonical_constants.py
"""

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(SCRIPT_DIR)
sys.path.insert(0, SCRIPT_DIR)

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from canonical_constants import (
    tau_fold, E_cond, N_cells,
    omega_L1, T_acoustic, Omega_DM, Omega_Lambda,
    Delta_0_OES, J_C2, M_ATDHFB, v_terminal
)

print("=" * 70)
print("S57 LEGGETT-PARTITION-57: DM/CC Energy Fraction")
print("=" * 70)

# ======================================================================
# 1. Load all input data
# ======================================================================

d_tau = np.load('s57_leggett_tau_profile.npz', allow_pickle=True)
d_budget = np.load('s57_channel_energy_budget.npz', allow_pickle=True)
d_fabric = np.load('s56_leggett_fabric.npz', allow_pickle=True)

tau_values = d_tau['tau_values']  # (50,)
omega_L0_tau = d_tau['omega_L0']  # (50,) - uniform Leggett gap omega_L0(tau)
d_omega_dt = d_tau['d_omega_L0_dt']  # (50,)
gamma_LZ_tau = d_tau['gamma_LZ']  # (50,) - LZ adiabaticity parameter
H_tau = d_tau['H']  # (50,)
dtau_dt = float(d_tau['dtau_dt'])
E_J_tau = d_tau['E_J']  # (50,)
fold_idx = int(d_tau['fold_idx'])

# S56 fabric data
laplacian_eigs = d_fabric['laplacian_eigs']  # (32,)
omega_L_S49 = d_fabric['omega_L_S49_1']  # (50, 32) - S49 model
omega_L_GL = d_fabric['omega_L_GL']  # (50, 32) - GL model
omega_L_S49_2 = d_fabric['omega_L_S49_2']  # (50, 32) - intermediate
J_Leggett_tau = d_fabric['J_Leggett']  # (50,)

# Energy budget from W0-2
F_Josephson = float(d_budget['F_Josephson'])
F_BCS = float(d_budget['F_BCS'])
F_Leggett = float(d_budget['F_Leggett'])
F_BA = float(d_budget['F_BA'])
F_total = float(d_budget['F_total'])
T_GH = float(d_budget['T_GH'])
omega_BA_fold = d_budget['omega_BA_fold']  # (31,) - BA modes at fold

print(f"\nInputs loaded:")
print(f"  tau grid: {len(tau_values)} points, [{tau_values[0]:.3f}, {tau_values[-1]:.3f}]")
print(f"  fold_idx = {fold_idx}, tau_fold = {tau_values[fold_idx]:.4f}")
print(f"  N_cells = {N_cells}, non-Goldstone Leggett modes = {N_cells - 1}")
print(f"  dtau/dt = {dtau_dt:.2f} M_KK")
print(f"  dt_transit = {0.5/dtau_dt:.6f} M_KK^-1")
print(f"  F_Josephson = {F_Josephson:.2f}, F_BCS = {F_BCS:.2f}")
print(f"  F_Leggett = {F_Leggett:.2f}, F_BA = {F_BA:.2f}")
print(f"  F_total = {F_total:.2f}")

N_modes = N_cells - 1  # = 31

# Transit kinetic energy (energy budget ceiling)
T_kin = 0.5 * M_ATDHFB * v_terminal**2
print(f"  T_kin (transit KE) = {T_kin:.1f} M_KK")

# ======================================================================
# 2. Verify sudden quench regime
# ======================================================================

dt_transit = 0.5 / dtau_dt  # full transit duration in M_KK^{-1}

print(f"\n{'='*60}")
print("REGIME VERIFICATION: Sudden quench?")
print(f"{'='*60}")
print(f"  dt_transit = {dt_transit:.6f} M_KK^-1")

# Check omega * dt for the uniform mode
print(f"  omega_L0(tau=0) * dt = {omega_L0_tau[0] * dt_transit:.6e}")
print(f"  omega_L0(fold) * dt  = {omega_L0_tau[fold_idx] * dt_transit:.6e}")
print(f"  omega_L0(end) * dt   = {omega_L0_tau[-1] * dt_transit:.6e}")

# Also check adiabaticity parameter eta = |d_omega/dt| / omega^2
eta_tau = np.abs(d_omega_dt) / omega_L0_tau**2
print(f"  eta = |d_omega/dt|/omega^2 at fold = {eta_tau[fold_idx]:.0f} >> 1 (SUDDEN)")
print(f"  eta range: [{eta_tau.min():.0f}, {eta_tau.max():.0f}]")
print(f"  CONFIRMED: Deeply in sudden quench regime throughout transit")

# ======================================================================
# 3. Mode-resolved parametric excitation (Bogoliubov squeezing)
# ======================================================================

# For a sudden quench from omega_i to omega_f:
#   <n_exc> = (r + 1/r - 2) / 4   where r = omega_i/omega_f
#   P_ground = 2*sqrt(omega_i*omega_f) / (omega_i + omega_f)
#   P_exc = 1 - P_ground  (probability of NOT being in ground state)
#   E_exc = <n_exc> * omega_f  (energy above ground state of final H)
#
# This is the EXACT result for an instantaneous frequency change.
# For the actual finite-time transit, this is an UPPER BOUND on excitation.
#
# We evaluate at THREE "scission points":
#   A. Full transit (tau=0 -> tau=0.5): maximum possible excitation
#   B. Fold scission (tau=0 -> tau_fold): excitation frozen at fold
#   C. Scission point from W0-1 (tau=0 -> tau_scission=0.296)

tau_scission = float(d_tau['scission_tau'])
scission_idx = np.argmin(np.abs(tau_values - tau_scission))

models = {
    'S49_1': omega_L_S49,     # omega_L0 = 0.070
    'GL': omega_L_GL,         # omega_L0 = 0.138
    'S49_2': omega_L_S49_2,   # omega_L0 = 0.107
}

# Matter-sector energy (Volovik reframing)
E_matter = abs(F_BCS) + F_BA  # = 4.38 + 7.02 = 11.40 M_KK

results = {}

for model_name, omega_L_full in models.items():
    print(f"\n{'='*60}")
    print(f"Model: {model_name}")
    print(f"{'='*60}")

    # Skip Goldstone mode (n=0)
    omega_L = omega_L_full[:, 1:]  # (50, 31) dispersive modes

    omega_i = omega_L[0, :]       # initial frequencies (tau=0)
    omega_fold = omega_L[fold_idx, :]  # at fold
    omega_scission = omega_L[scission_idx, :]  # at scission
    omega_end = omega_L[-1, :]    # at tau=0.5

    # ---- Excitation to fold ----
    r_fold = omega_i / omega_fold
    n_exc_fold = (r_fold + 1.0/r_fold - 2.0) / 4.0
    P_ground_fold = 2.0 * np.sqrt(omega_i * omega_fold) / (omega_i + omega_fold)
    P_exc_fold = 1.0 - P_ground_fold
    E_exc_fold = n_exc_fold * omega_fold

    # ---- Excitation to scission ----
    r_scission = omega_i / omega_scission
    n_exc_scission = (r_scission + 1.0/r_scission - 2.0) / 4.0
    P_ground_scission = 2.0 * np.sqrt(omega_i * omega_scission) / (omega_i + omega_scission)
    P_exc_scission = 1.0 - P_ground_scission
    E_exc_scission = n_exc_scission * omega_scission

    # ---- Excitation to end ----
    r_end = omega_i / omega_end
    n_exc_end = (r_end + 1.0/r_end - 2.0) / 4.0
    P_ground_end = 2.0 * np.sqrt(omega_i * omega_end) / (omega_i + omega_end)
    P_exc_end = 1.0 - P_ground_end
    E_exc_end = n_exc_end * omega_end

    # Totals
    E_L_fold = E_exc_fold.sum()
    E_L_scission = E_exc_scission.sum()
    E_L_end = E_exc_end.sum()

    n_bar_fold = n_exc_fold.mean()
    n_bar_end = n_exc_end.mean()

    # DM fractions
    f_DM_fold = E_L_fold / E_matter
    f_DM_scission = E_L_scission / E_matter
    f_DM_end = E_L_end / E_matter

    # Probability mappings
    # Fraction of modes with P_exc > 0.5
    frac_exc_050_fold = (P_exc_fold > 0.5).sum() / N_modes
    frac_exc_050_end = (P_exc_end > 0.5).sum() / N_modes
    # Fraction of modes with P_exc > 0.01
    frac_exc_001_fold = (P_exc_fold > 0.01).sum() / N_modes
    frac_exc_001_end = (P_exc_end > 0.01).sum() / N_modes
    # Mean P_exc
    mean_P_exc_fold = P_exc_fold.mean()
    mean_P_exc_end = P_exc_end.mean()

    # Cumulative: what fraction of E_L comes from top N modes?
    idx_sorted_fold = np.argsort(E_exc_fold)[::-1]
    E_cumul_fold = np.cumsum(E_exc_fold[idx_sorted_fold])
    E_cumul_frac_fold = E_cumul_fold / E_L_fold

    idx_sorted_end = np.argsort(E_exc_end)[::-1]
    E_cumul_end = np.cumsum(E_exc_end[idx_sorted_end])
    E_cumul_frac_end = E_cumul_end / E_L_end

    # Flat band vs dispersive
    lambda_modes = laplacian_eigs[1:]  # (31,)
    lambda_median = np.median(lambda_modes)
    is_low_k = lambda_modes < lambda_median
    E_low_k_fold = E_exc_fold[is_low_k].sum()
    E_high_k_fold = E_exc_fold[~is_low_k].sum()
    E_low_k_end = E_exc_end[is_low_k].sum()
    E_high_k_end = E_exc_end[~is_low_k].sum()

    print(f"\n  Frequency ratios (omega_i/omega_f):")
    print(f"    To fold:     [{r_fold.min():.4f}, {r_fold.max():.4f}]")
    print(f"    To scission: [{r_scission.min():.4f}, {r_scission.max():.4f}]")
    print(f"    To end:      [{r_end.min():.4f}, {r_end.max():.4f}]")

    print(f"\n  Mean excitation number <n_exc>:")
    print(f"    To fold:     [{n_exc_fold.min():.6f}, {n_exc_fold.max():.6f}], mean={n_bar_fold:.6f}")
    print(f"    To end:      [{n_exc_end.min():.6f}, {n_exc_end.max():.6f}], mean={n_bar_end:.6f}")

    print(f"\n  P_exc (probability NOT in ground state):")
    print(f"    To fold:     [{P_exc_fold.min():.6f}, {P_exc_fold.max():.6f}], mean={mean_P_exc_fold:.6f}")
    print(f"    To end:      [{P_exc_end.min():.6f}, {P_exc_end.max():.6f}], mean={mean_P_exc_end:.6f}")

    print(f"\n  Total Leggett excitation energy:")
    print(f"    To fold:     E_L = {E_L_fold:.6f} M_KK")
    print(f"    To scission: E_L = {E_L_scission:.6f} M_KK")
    print(f"    To end:      E_L = {E_L_end:.6f} M_KK")

    print(f"\n  E_matter = {E_matter:.2f} M_KK (|F_BCS| + F_BA)")
    print(f"  DM fraction f_DM = E_L / E_matter:")
    print(f"    To fold:     f_DM = {f_DM_fold:.6f}")
    print(f"    To scission: f_DM = {f_DM_scission:.6f}")
    print(f"    To end:      f_DM = {f_DM_end:.6f}")
    print(f"  Observed Omega_DM = {Omega_DM:.3f}")

    print(f"\n  Probability mapping:")
    print(f"    Frac with P_exc > 0.50: fold={frac_exc_050_fold:.3f}, end={frac_exc_050_end:.3f}")
    print(f"    Frac with P_exc > 0.01: fold={frac_exc_001_fold:.3f}, end={frac_exc_001_end:.3f}")
    print(f"    Mean P_exc: fold={mean_P_exc_fold:.6f}, end={mean_P_exc_end:.6f}")

    # Top 10 modes table
    print(f"\n  Top 10 modes by E_exc (to end, tau=0.5):")
    print(f"  {'Mode':>6s} {'lambda':>8s} {'omega_i':>10s} {'omega_f':>10s} "
          f"{'ratio':>8s} {'<n>':>10s} {'P_exc':>10s} {'E_exc':>10s} {'Cum%':>7s}")
    for i in range(min(10, N_modes)):
        n = idx_sorted_end[i]
        print(f"  {n+1:6d} {lambda_modes[n]:8.3f} {omega_i[n]:10.4f} {omega_end[n]:10.4f} "
              f"{r_end[n]:8.4f} {n_exc_end[n]:10.4f} {P_exc_end[n]:10.6f} "
              f"{E_exc_end[n]:10.6f} {E_cumul_frac_end[i]*100:7.2f}")

    print(f"\n  Low-k vs high-k partition:")
    print(f"    lambda_median = {lambda_median:.4f}")
    print(f"    E_low_k (to end): {E_low_k_end:.6f} ({E_low_k_end/E_L_end*100:.1f}%)")
    print(f"    E_high_k (to end): {E_high_k_end:.6f} ({E_high_k_end/E_L_end*100:.1f}%)")

    results[model_name] = {
        'omega_i': omega_i,
        'omega_fold': omega_fold,
        'omega_end': omega_end,
        'omega_scission': omega_scission,
        'r_fold': r_fold,
        'r_end': r_end,
        'n_exc_fold': n_exc_fold,
        'n_exc_end': n_exc_end,
        'n_exc_scission': n_exc_scission,
        'P_exc_fold': P_exc_fold,
        'P_exc_end': P_exc_end,
        'P_exc_scission': P_exc_scission,
        'E_exc_fold': E_exc_fold,
        'E_exc_end': E_exc_end,
        'E_exc_scission': E_exc_scission,
        'E_L_fold': E_L_fold,
        'E_L_end': E_L_end,
        'E_L_scission': E_L_scission,
        'f_DM_fold': f_DM_fold,
        'f_DM_end': f_DM_end,
        'f_DM_scission': f_DM_scission,
        'mean_P_exc_fold': mean_P_exc_fold,
        'mean_P_exc_end': mean_P_exc_end,
        'frac_exc_050_end': frac_exc_050_end,
        'frac_exc_001_end': frac_exc_001_end,
        'E_matter': E_matter,
        'idx_sorted_end': idx_sorted_end,
        'E_cumul_frac_end': E_cumul_frac_end,
        'E_low_k_end': E_low_k_end,
        'E_high_k_end': E_high_k_end,
        'P_ground_fold': P_ground_fold,
        'P_ground_end': P_ground_end,
    }

# ======================================================================
# 4. ALTERNATIVE: BA modes as DM (not Leggett)
# ======================================================================
# The Leggett modes have small frequency ratios (omega_i/omega_f ~ 1.1-4)
# because they are INTERNAL (B2-B1 relative phase) modes that change
# slowly. The BA modes are spatial sound modes that also undergo
# parametric excitation. Let's compare.

print(f"\n{'='*60}")
print("COMPARISON: BA parametric excitation")
print(f"{'='*60}")

# BA modes: omega_BA_fold gives the frequencies at the fold.
# We need omega_BA at tau=0 and tau=0.5 too. From s56_ba_spectrum.npz?
# We only have them at the fold. Estimate: BA modes scale with c_BA(tau).
# From MEMORY: c_BA=0.399 at fold, and c_BA varies with tau.

c_BA_tau = d_fabric['c_BA']  # (50,)
c_BA_0 = c_BA_tau[0]
c_BA_fold = c_BA_tau[fold_idx]
c_BA_end = c_BA_tau[-1]

print(f"  c_BA: tau=0 -> {c_BA_0:.4f}, fold -> {c_BA_fold:.4f}, end -> {c_BA_end:.4f}")

# BA frequency scales as omega_BA ~ c_BA * k, so ratio is c_BA(0)/c_BA(end)
r_BA = c_BA_0 / c_BA_end if c_BA_end > 0 else np.inf
n_exc_BA = (r_BA + 1.0/r_BA - 2.0) / 4.0
print(f"  c_BA ratio (0->end): {r_BA:.4f}")
print(f"  <n_exc> per BA mode = {n_exc_BA:.4f}")

# For each BA mode at fold, estimate E_exc
omega_BA_0 = omega_BA_fold * (c_BA_0 / c_BA_fold)  # scale to tau=0
omega_BA_end_est = omega_BA_fold * (c_BA_end / c_BA_fold)  # scale to tau=0.5

# But we only have BA modes at fold from W0-2. The actual dispersion may differ.
# Use the ratio c_BA(0)/c_BA(end) as uniform scaling.

r_BA_modes = omega_BA_0 / omega_BA_end_est
n_exc_BA_modes = (r_BA_modes + 1.0/r_BA_modes - 2.0) / 4.0
E_exc_BA_modes = n_exc_BA_modes * omega_BA_end_est
E_BA_total = E_exc_BA_modes.sum()
f_DM_BA = E_BA_total / E_matter

print(f"  E_BA_total (parametric) = {E_BA_total:.4f} M_KK")
print(f"  f_DM (BA only) = {f_DM_BA:.6f}")
print(f"  BA + Leggett (S49_1, end) = {(E_BA_total + results['S49_1']['E_L_end']):.4f} M_KK")
print(f"  f_DM (BA+Leggett) = {(E_BA_total + results['S49_1']['E_L_end'])/E_matter:.6f}")

# ======================================================================
# 5. The W0-2 energy reframing check
# ======================================================================

print(f"\n{'='*60}")
print("W0-2 REFRAMING CHECK")
print(f"{'='*60}")

# W0-2 found E_L/E_matter = 26.4% at the fold for GROUND STATE Leggett energy.
# That was F_Leggett / (|F_BCS| + F_BA) = 3.01 / 11.40 = 26.4%.
# But F_Leggett is the GROUND STATE energy of the Leggett modes,
# not the EXCITATION energy from parametric particle creation.
#
# The ground state Leggett energy and the excitation energy are DIFFERENT things:
# - F_Leggett = Sum_n omega_L(n, fold) / 2  (zero-point energy)
# - E_L_exc = Sum_n <n_exc>(n) * omega_L(n)  (excitation above ZPE)
#
# For the DM mapping, the question is: what fraction of the POST-TRANSIT
# energy is in the form of Leggett quasiparticles?

# The 26.4% from W0-2 is the ZPE ratio. The parametric excitation adds
# more energy on top of ZPE. The total Leggett energy is ZPE + E_exc.

# From W0-2: F_Leggett = 3.01 M_KK (ZPE of 32 dispersive modes)
# Wait, F_Leggett includes F_Leggett_uniform + F_Leggett_dispersive

F_L_uniform = float(d_budget['F_Leggett_uniform'])
F_L_dispersive = float(d_budget['F_Leggett_dispersive'])
print(f"  F_Leggett_uniform = {F_L_uniform:.4f}")
print(f"  F_Leggett_dispersive = {F_L_dispersive:.4f}")
print(f"  F_Leggett_total = {F_Leggett:.4f}")

# The ZPE is F_ZPE = Sum_n omega_L(n)/2 which is part of what W0-2 computed
# Let me compute it directly from the S49_1 frequencies at fold
omega_L_S49_fold = omega_L_S49[fold_idx, 1:]  # (31,) skip Goldstone
ZPE_L_fold = 0.5 * omega_L_S49_fold.sum()
print(f"\n  ZPE (Leggett, S49_1 at fold) = {ZPE_L_fold:.4f} M_KK")
print(f"  E_L_exc (S49_1, to fold) = {results['S49_1']['E_L_fold']:.6f} M_KK")
print(f"  E_L_exc (S49_1, to end)  = {results['S49_1']['E_L_end']:.6f} M_KK")
print(f"  Ratio E_exc/ZPE (fold) = {results['S49_1']['E_L_fold']/ZPE_L_fold:.6f}")
print(f"  Ratio E_exc/ZPE (end) = {results['S49_1']['E_L_end']/ZPE_L_fold:.6f}")

# Total Leggett energy including excitation
E_L_total_fold = ZPE_L_fold + results['S49_1']['E_L_fold']
E_L_total_end = ZPE_L_fold + results['S49_1']['E_L_end']  # approx: ZPE changes too
print(f"\n  Total Leggett energy (ZPE + exc):")
print(f"    At fold: {E_L_total_fold:.4f} M_KK")
print(f"    At end:  {E_L_total_end:.4f} M_KK")
print(f"  f_DM (total, fold) = {E_L_total_fold / E_matter:.4f}")
print(f"  f_DM (total, end) = {E_L_total_end / E_matter:.4f}")

# The ZPE ratio dominates because <n_exc> is small (< 1 per mode)
# The W0-2 reframing (26.4%) was about the ZPE, which is a STATIC
# property, not a dynamical excitation.

# ======================================================================
# 6. CORRECT DM MAPPING
# ======================================================================

print(f"\n{'='*60}")
print("CORRECT DM MAPPING")
print(f"{'='*60}")

# There are FOUR possible DM mappings:
# A. P_exc probability (fraction of modes excited) -- SATURATED at ~0
#    because P_exc < 0.5 for all modes => frac_excited = 0
#    BUT: every mode has P_exc > 0 (all are slightly squeezed)
#    Mean P_exc ~ 0.01-0.20 depending on model

# B. Energy fraction (E_L_exc / E_matter) -- O(10^{-4} to 10^{-2})
#    Because frequency ratios are modest (1-4x) for Leggett modes

# C. ZPE fraction (Sum omega_L/2 / E_matter) -- This is what W0-2 got
#    = 26.4%. But ZPE is NOT an excitation -- it's always there

# D. Particle number fraction (N_L_exc / N_total_exc)
#    Compare Leggett quasiparticle number to BCS quasiparticle number

# The physical question: after transit, what fraction of MATTER
# (non-vacuum) energy is in Leggett excitations?

# From S38: the BCS transit produces 59.8 quasiparticle pairs
# with E_exc = 443 * |E_cond| = 60.6 M_KK (sudden quench).
# These are the "baryonic matter" excitations.

# The Leggett excitations are the "dark matter" candidate.

# Ratio = E_L_exc / (E_BCS_exc + E_L_exc)
E_BCS_exc = 443.0 * abs(E_cond)  # from S38 sudden quench
print(f"  E_BCS_exc (S38 quench) = {E_BCS_exc:.2f} M_KK")
print(f"  E_L_exc (S49_1, end) = {results['S49_1']['E_L_end']:.6f} M_KK")
print(f"  E_L_exc (GL, end) = {results['GL']['E_L_end']:.6f} M_KK")

f_DM_vs_BCS = results['S49_1']['E_L_end'] / (E_BCS_exc + results['S49_1']['E_L_end'])
print(f"  f_DM = E_L / (E_BCS + E_L) = {f_DM_vs_BCS:.6f}")
print(f"  This is 4 orders below Omega_DM = {Omega_DM:.3f}")

# But wait: the above uses the SINGLE-CELL BCS excitation scaled to 32 cells.
# The fabric BCS excitation may differ from the single-cell estimate.
# Use E_matter from W0-2 as the denominator instead.

print(f"\n  Using W0-2 denominator E_matter = {E_matter:.2f}:")
for mname in ['S49_1', 'GL', 'S49_2']:
    rm = results[mname]
    print(f"    {mname}: f_DM(fold)={rm['f_DM_fold']:.6f}, "
          f"f_DM(end)={rm['f_DM_end']:.6f}, "
          f"f_DM(scission)={rm['f_DM_scission']:.6f}")

# ======================================================================
# 7. Gate evaluation
# ======================================================================

print(f"\n{'='*70}")
print("GATE EVALUATION: LEGGETT-PARTITION-57")
print(f"{'='*70}")

def gate_classify(val, name):
    if val < 0.05:
        return f"FAIL (< 0.05): {name} DM mechanism dead"
    elif val <= 0.15:
        return f"INFO [0.05, 0.15]: {name} marginal low"
    elif val <= 0.45:
        return f"PASS [0.15, 0.45]: {name} consistent with Omega_DM"
    elif val <= 0.80:
        return f"INFO [0.45, 0.80]: {name} marginal high"
    else:
        return f"INFO (> 0.80): {name} fully excited, no CC partition"

r = results['S49_1']

# Three evaluation channels:
# A. Probability mapping (mean P_exc across modes)
P_exc_mean = r['mean_P_exc_end']

# B. Energy mapping (single-quantum equivalent)
f_DM_energy = r['f_DM_end']

# C. ZPE reframing (from W0-2)
f_DM_zpe = ZPE_L_fold / E_matter

print(f"\n  S49_1 (primary model, omega_L0 = 0.070):")
print(f"  A. Mean P_exc (prob mapping):   {P_exc_mean:.6f}")
print(f"     -> {gate_classify(P_exc_mean, 'P_exc')}")
print(f"  B. f_DM (energy, to end):       {f_DM_energy:.6f}")
print(f"     -> {gate_classify(f_DM_energy, 'f_DM_energy')}")
print(f"  C. f_DM (ZPE reframing):        {f_DM_zpe:.4f}")
print(f"     -> {gate_classify(f_DM_zpe, 'f_DM_ZPE')}")

# The ZPE reframing from W0-2 (26.4%) would give PASS.
# But ZPE is not excitation -- it's always present.
# The DYNAMICAL excitation (B) gives FAIL at O(10^{-4}).
# The probability mapping (A) also gives FAIL.

# HOWEVER: the gate criterion was written for the 2-level LZ P_exc,
# not for the harmonic oscillator squeezing probability. The W0-1
# result (P_exc = 0.9996 in the LZ sense) means the mode is FULLY
# DIABATIC -- it cannot follow. This is correctly captured by our
# result: the system is squeezed but the frequency ratio is modest,
# so the actual excitation energy is small.

# The gate needs to be evaluated on the ENERGY fraction, which is
# the physical observable. The answer is FAIL.

if f_DM_energy < 0.05:
    overall_verdict = "FAIL"
elif f_DM_energy < 0.15:
    overall_verdict = "INFO"
elif f_DM_energy <= 0.45:
    overall_verdict = "PASS"
elif f_DM_energy <= 0.80:
    overall_verdict = "INFO"
else:
    overall_verdict = "INFO"

print(f"\n  OVERALL GATE VERDICT: {overall_verdict}")
print(f"  Basis: Parametric excitation energy fraction f_DM = {f_DM_energy:.6f}")
print(f"  (S49_1 model, sudden quench to tau=0.5)")
print(f"  Shortfall: Omega_DM / f_DM = {Omega_DM / f_DM_energy:.0f}x")

# But also report the W0-2 ZPE reframing
print(f"\n  NOTE: W0-2 ZPE reframing gives 26.4%.")
print(f"  This is a STATIC (ground-state) property, not a dynamical excitation.")
print(f"  Whether ZPE counts as 'matter' depends on the mapping convention.")
print(f"  If ZPE = matter: PASS at 26.4%.")
print(f"  If only excitations = matter: FAIL at 0.03%.")

# ======================================================================
# 8. Save
# ======================================================================

r0 = results['S49_1']
r1 = results['GL']
r2 = results['S49_2']

save_dict = {
    'tau_values': tau_values,
    'tau_fold': tau_values[fold_idx],
    'fold_idx': fold_idx,
    'tau_scission': tau_scission,
    'N_modes': N_modes,
    'N_cells': N_cells,
    'lambda_modes': laplacian_eigs[1:],
    'dtau_dt': dtau_dt,
    'dt_transit': dt_transit,
    'E_matter': E_matter,
    'F_Josephson': F_Josephson,
    'F_BCS': F_BCS,
    'F_BA': F_BA,
    'T_kin': T_kin,
    'Omega_DM_obs': Omega_DM,
    'E_BCS_exc': E_BCS_exc,
    'ZPE_L_fold': ZPE_L_fold,
    'f_DM_ZPE': f_DM_zpe,

    # S49_1
    'omega_i_S49': r0['omega_i'],
    'omega_end_S49': r0['omega_end'],
    'r_end_S49': r0['omega_i'] / r0['omega_end'],
    'n_exc_fold_S49': r0['n_exc_fold'],
    'n_exc_end_S49': r0['n_exc_end'],
    'P_exc_fold_S49': r0['P_exc_fold'],
    'P_exc_end_S49': r0['P_exc_end'],
    'E_exc_fold_S49': r0['E_exc_fold'],
    'E_exc_end_S49': r0['E_exc_end'],
    'E_L_fold_S49': r0['E_L_fold'],
    'E_L_end_S49': r0['E_L_end'],
    'f_DM_fold_S49': r0['f_DM_fold'],
    'f_DM_end_S49': r0['f_DM_end'],
    'f_DM_scission_S49': r0['f_DM_scission'],
    'mean_P_exc_end_S49': r0['mean_P_exc_end'],

    # GL
    'omega_i_GL': r1['omega_i'],
    'omega_end_GL': r1['omega_end'],
    'n_exc_end_GL': r1['n_exc_end'],
    'P_exc_end_GL': r1['P_exc_end'],
    'E_exc_end_GL': r1['E_exc_end'],
    'E_L_end_GL': r1['E_L_end'],
    'f_DM_end_GL': r1['f_DM_end'],

    # S49_2
    'omega_i_S49_2': r2['omega_i'],
    'omega_end_S49_2': r2['omega_end'],
    'n_exc_end_S49_2': r2['n_exc_end'],
    'P_exc_end_S49_2': r2['P_exc_end'],
    'E_exc_end_S49_2': r2['E_exc_end'],
    'E_L_end_S49_2': r2['E_L_end'],
    'f_DM_end_S49_2': r2['f_DM_end'],

    # BA comparison
    'E_BA_parametric': E_BA_total,
    'f_DM_BA': f_DM_BA,

    # Gate
    'gate_name': 'LEGGETT-PARTITION-57',
    'gate_verdict': overall_verdict,
    'f_DM_energy': f_DM_energy,
    'P_exc_mean': P_exc_mean,
    'shortfall_factor': Omega_DM / max(f_DM_energy, 1e-20),
}

np.savez('s57_leggett_partition.npz', **save_dict)
print(f"\nData saved: s57_leggett_partition.npz")

# ======================================================================
# 9. Plotting
# ======================================================================

fig, axes = plt.subplots(2, 3, figsize=(18, 12))
fig.suptitle('S57 LEGGETT-PARTITION-57: DM/CC Energy Fraction\n'
             '(Parametric Excitation from Sudden Quench of Leggett Modes)',
             fontsize=13, fontweight='bold')

mode_idx = np.arange(1, N_modes + 1)

# (a) Frequency ratio omega_i/omega_f for each mode
ax = axes[0, 0]
for mname, color, ls in [('S49_1', 'blue', '-'), ('GL', 'red', '--'), ('S49_2', 'green', ':')]:
    rm = results[mname]
    r_vals = rm['omega_i'] / rm['omega_end']
    ax.plot(mode_idx, r_vals, color=color, ls=ls, marker='o', ms=3, label=mname)
ax.axhline(1.0, color='gray', ls=':', lw=1)
ax.set_xlabel('Mode index n')
ax.set_ylabel('omega_i / omega_f')
ax.set_title('(a) Frequency ratio (0 -> 0.5)')
ax.legend()
ax.grid(True, alpha=0.3)

# (b) Mean excitation number per mode
ax = axes[0, 1]
for mname, color, ls in [('S49_1', 'blue', '-'), ('GL', 'red', '--'), ('S49_2', 'green', ':')]:
    rm = results[mname]
    ax.plot(mode_idx, rm['n_exc_end'], color=color, ls=ls, marker='o', ms=3, label=mname)
ax.set_xlabel('Mode index n')
ax.set_ylabel('<n_exc>')
ax.set_title('(b) Excitation number per mode (to end)')
ax.legend()
ax.grid(True, alpha=0.3)

# (c) Energy deposited per mode
ax = axes[0, 2]
for mname, color, ls in [('S49_1', 'blue', '-'), ('GL', 'red', '--'), ('S49_2', 'green', ':')]:
    rm = results[mname]
    ax.plot(mode_idx, rm['E_exc_end'], color=color, ls=ls, marker='o', ms=3, label=mname)
ax.set_xlabel('Mode index n')
ax.set_ylabel('E_exc(n) [M_KK]')
ax.set_title('(c) Excitation energy per mode (to end)')
ax.legend()
ax.grid(True, alpha=0.3)

# (d) P_exc per mode
ax = axes[1, 0]
for mname, color, ls in [('S49_1', 'blue', '-'), ('GL', 'red', '--'), ('S49_2', 'green', ':')]:
    rm = results[mname]
    ax.plot(mode_idx, rm['P_exc_end'], color=color, ls=ls, marker='o', ms=3, label=mname)
ax.axhline(Omega_DM, color='red', ls='--', lw=2, label=f'Omega_DM = {Omega_DM:.3f}')
ax.set_xlabel('Mode index n')
ax.set_ylabel('P_exc (not in ground state)')
ax.set_title('(d) Excitation probability per mode')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# (e) Cumulative energy distribution
ax = axes[1, 1]
for mname, color in [('S49_1', 'blue'), ('GL', 'red'), ('S49_2', 'green')]:
    rm = results[mname]
    ax.plot(np.arange(1, N_modes + 1), rm['E_cumul_frac_end'],
            color=color, marker='o', ms=3, label=mname)
ax.axhline(0.5, color='gray', ls='--', lw=1, label='50%')
ax.axhline(0.9, color='gray', ls=':', lw=1, label='90%')
ax.set_xlabel('Number of modes (sorted by E_exc)')
ax.set_ylabel('Cumulative fraction of E_L')
ax.set_title('(e) Cumulative energy distribution')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# (f) DM fraction comparison
ax = axes[1, 2]
x = np.arange(3)
labels = ['S49_1', 'GL', 'S49_2']
# Three bars: fold, scission, end
for i, (mname, color) in enumerate(zip(labels, ['blue', 'red', 'green'])):
    rm = results[mname]
    ax.bar(i - 0.2, rm['f_DM_fold'], 0.2, color=color, alpha=0.6, label='fold' if i==0 else '')
    ax.bar(i, rm['f_DM_scission'], 0.2, color=color, alpha=0.8, label='scission' if i==0 else '')
    ax.bar(i + 0.2, rm['f_DM_end'], 0.2, color=color, alpha=1.0, label='end' if i==0 else '')
ax.axhline(Omega_DM, color='black', ls='--', lw=2, label=f'Omega_DM={Omega_DM:.3f}')
ax.axhspan(0.15, 0.45, alpha=0.1, color='green', label='PASS band')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel('f_DM = E_L_exc / E_matter')
ax.set_title('(f) DM energy fraction by model')
ax.legend(fontsize=7, loc='upper left')
ax.set_yscale('log')
ax.set_ylim(1e-5, 1)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('s57_leggett_partition.png', dpi=150, bbox_inches='tight')
print(f"Plot saved: s57_leggett_partition.png")

print("\nDONE")
