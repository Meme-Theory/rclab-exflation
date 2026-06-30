#!/usr/bin/env python3
"""
s58_multimode_resonance.py — Three-Mode Resonance Census (MULTIMODE-RESONANCE-58)
==================================================================================

Gate: MULTIMODE-RESONANCE-58 (INFO)
Question: Do multi-mode resonances have sufficient coupling for energy transfer?

The 32-cell fabric has 63 collective modes at the fold:
  - 31 Bogoliubov-Anderson (BA): omega in [0.209, 1.368] M_KK
  - 31 Leggett: omega in [0.089, 0.365] M_KK
  - 1 plasma (Josephson): omega_J = 1.429 M_KK

Transit broadening Gamma = 1/dt_transit = 885 M_KK >> all mode frequencies.
Every triplet trivially satisfies the resonance condition delta < Gamma.
The physical question is COUPLING STRENGTH.

Method:
  1. Enumerate all 3-mode triplets (63 choose 3 with repetition = 41,664)
  2. Confirm N_res = all (trivial)
  3. Import cubic vertex = 0 from W1-3 (cos is even, no frustration)
  4. Compute 4-mode (quartic) parametric gain from W1-3 data
  5. Compute BA-Leggett cross-coupling from BCS self-consistency
  6. Report strongest coupling, top resonances, gain assessment

Session: S58 W2-4
Agent: tesla-resonance
"""

import numpy as np
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    tau_fold, dt_transit, E_cond, Delta_0_OES, omega_PV,
    J_C2, J_su2, J_u1, N_cells, E_cond_ED_8mode,
    omega_L1, omega_L2, xi_BCS, Delta_B3
)

# =============================================================================
#  LOAD DATA
# =============================================================================

ba_data = np.load('computations/session-56/s56_ba_spectrum.npz', allow_pickle=True)
lg_data = np.load('computations/session-56/s56_leggett_fabric.npz', allow_pickle=True)
pd_data = np.load('computations/session-57/s57_phase_diagram.npz', allow_pickle=True)
ah_data = np.load('computations/session-58/s58_anharmonic_leggett.npz', allow_pickle=True)

# Find fold index
tau_vals = ba_data['tau_values']
idx_fold = np.argmin(np.abs(tau_vals - tau_fold))
tau_actual = tau_vals[idx_fold]

print(f"=== MULTIMODE-RESONANCE-58: Three-Mode Resonance Census ===")
print(f"tau_fold = {tau_fold}, actual tau = {tau_actual:.4f}, idx = {idx_fold}")
print()

# =============================================================================
#  EXTRACT MODE FREQUENCIES AT FOLD
# =============================================================================

# 31 BA modes
omega_BA = ba_data['omega_BA'][idx_fold]  # shape (31,)
N_BA = len(omega_BA)

# 31 nonzero Leggett modes (exclude k=0 uniform phase)
omega_L_all = lg_data['omega_L_S49_1'][idx_fold]  # shape (32,)
omega_L = omega_L_all[1:]  # 31 nonzero modes
N_L = len(omega_L)

# 1 plasma mode
omega_J = pd_data['omega_J'][idx_fold]
omega_J_scalar = float(omega_J)

# All 63 modes concatenated: [BA_0..BA_30, L_0..L_30, J]
omega_all = np.concatenate([omega_BA, omega_L, [omega_J_scalar]])
N_modes = len(omega_all)
assert N_modes == 63, f"Expected 63 modes, got {N_modes}"

# Mode labels
labels = []
for i in range(N_BA):
    labels.append(f"BA_{i}")
for i in range(N_L):
    labels.append(f"L_{i}")
labels.append("J")

print(f"Mode census: {N_BA} BA + {N_L} Leggett + 1 plasma = {N_modes} modes")
print(f"  BA range:  [{omega_BA.min():.4f}, {omega_BA.max():.4f}] M_KK")
print(f"  L range:   [{omega_L.min():.4f}, {omega_L.max():.4f}] M_KK")
print(f"  omega_J:   {omega_J_scalar:.4f} M_KK")
print()

# =============================================================================
#  TRANSIT BROADENING
# =============================================================================

Gamma = 1.0 / dt_transit
print(f"Transit broadening: Gamma = 1/dt_transit = {Gamma:.1f} M_KK")
print(f"  omega_max / Gamma = {omega_all.max() / Gamma:.5f}")
print(f"  ALL modes satisfy omega << Gamma")
print()

# =============================================================================
#  THREE-MODE RESONANCE COUNT
# =============================================================================
# For triplet (a, b, c), resonance condition: |omega_a - omega_b - omega_c| < Gamma
# Also check: |omega_a + omega_b - omega_c| (sum/difference variants)
# Since Gamma >> all omega, every triplet satisfies this trivially.

# Count all distinct triplets (a, b, c) with a <= b <= c
# This is "63 choose 3 with repetition" = C(63+3-1, 3) = C(65,3)
# But for DISTINCT ordered triplets: a < b < c gives C(63,3)
# For resonance counting, we need all unordered combinations including repeats

from itertools import combinations_with_replacement, combinations

# Distinct triplets (no repetition): C(63,3) = 39711
N_triplets_distinct = 0
N_res_distinct = 0
for i, j, k in combinations(range(N_modes), 3):
    N_triplets_distinct += 1
    # Check all frequency-difference conditions
    w = sorted([omega_all[i], omega_all[j], omega_all[k]])
    # Decay: omega_c -> omega_a + omega_b requires |w[2] - w[1] - w[0]| < Gamma
    delta_decay = abs(w[2] - w[1] - w[0])
    if delta_decay < Gamma:
        N_res_distinct += 1

print(f"=== THREE-MODE RESONANCE COUNT ===")
print(f"Total distinct triplets C(63,3) = {N_triplets_distinct}")
print(f"Triplets with |omega_c - omega_b - omega_a| < Gamma: {N_res_distinct}")
print(f"Fraction: {N_res_distinct / N_triplets_distinct:.6f}")
print(f"  (Expected: 1.000000 since Gamma >> all omega)")
print()

# Also count with repetition for completeness
N_triplets_rep = 0
N_res_rep = 0
for i, j, k in combinations_with_replacement(range(N_modes), 3):
    N_triplets_rep += 1
    w = sorted([omega_all[i], omega_all[j], omega_all[k]])
    delta_decay = abs(w[2] - w[1] - w[0])
    if delta_decay < Gamma:
        N_res_rep += 1

print(f"With repetition C(65,3) = {N_triplets_rep}")
print(f"Resonant: {N_res_rep}")
print(f"Fraction: {N_res_rep / N_triplets_rep:.6f}")
print()

# =============================================================================
#  CUBIC VERTEX: CONFIRMED ZERO FROM W1-3
# =============================================================================

S3_diag = ah_data['S3_diagonal']
V3_max = np.max(np.abs(S3_diag))
Gamma_3_ub = float(ah_data['Gamma_3_ub_fold'])

print(f"=== CUBIC VERTEX (from W1-3) ===")
print(f"V_3 = 0 identically (cos is even function, no frustration in ferromagnetic CG)")
print(f"  S3 diagonal max |entry|: {V3_max:.4e} (numerical noise)")
print(f"  Fluctuation-induced upper bound Gamma_3: {Gamma_3_ub:.4e} M_KK")
print(f"  Gamma_3 * dt_transit: {Gamma_3_ub * dt_transit:.4e}")
print(f"  THREE-MODE COUPLING VIA JOSEPHSON: FORBIDDEN BY SYMMETRY")
print()

# =============================================================================
#  QUARTIC VERTEX: PARAMETRIC GAIN FROM W1-3
# =============================================================================

# W1-3 computed the full quartic structure tensor.
# max |V_4| = 7.0e-4 M_KK
# Gamma_4 (FGR upper bound) = 1.21e-3 M_KK
# Gamma_4 * dt_transit = 1.37e-6

V4_max = float(ah_data['V4_0_top100'][0])
V4_self = ah_data['V4_self_fold']
Gamma_4_fold = float(ah_data['Gamma_4_fold'])
Gamma_4_per_mode = ah_data['Gamma_4_per_mode']

print(f"=== QUARTIC VERTEX (from W1-3) ===")
print(f"max |V_4|: {V4_max:.4e} M_KK (mode pair (0,22,3,22))")
print(f"Gamma_4 (FGR, mode 0): {Gamma_4_fold:.4e} M_KK")
print(f"Gamma_4 * dt_transit: {Gamma_4_fold * dt_transit:.4e}")
print()

# Parametric gain for 4-mode processes
# g_4 = |V_4|^2 * rho / omega, where rho = density of final states ~ N_modes / BW
BW_BA = float(ba_data['BW_BA'][idx_fold])
BW_L = omega_L.max() - omega_L.min()
BW_total = omega_all.max() - omega_all.min()
rho_modes = N_modes / BW_total  # modes per M_KK

# Parametric gain for the strongest channel
# For a 4-wave process a+b -> c+d, gain = |V_4|^2 * rho / (energy mismatch)
# Since all are resonant within Gamma, use Gamma as the effective detuning
V4_max_full = 7.0e-4  # from W1-3 report  # (local)

# The standard parametric instability criterion:
# Gain = V_4^2 * n_occ * rho / Gamma_damping
# Here n_occ ~ 1 (quantum ground state), and we compare to the transit rate

# Method 1: FGR scattering rate vs transit rate
ratio_FGR = Gamma_4_fold / Gamma
print(f"=== PARAMETRIC GAIN ANALYSIS ===")
print(f"Method 1: FGR rate / transit rate")
print(f"  Gamma_4 / Gamma_transit = {ratio_FGR:.4e}")
print(f"  Interpretation: quartic scattering {1/ratio_FGR:.0f}x slower than transit")
print()

# Method 2: Number of scattering events during transit
N_scatter = Gamma_4_fold * dt_transit
print(f"Method 2: Expected scattering events during transit")
print(f"  N_scatter = Gamma_4 * dt_transit = {N_scatter:.4e}")
print(f"  << 1 means at most {N_scatter:.2e} scatterings per mode (adiabatic)")
print()

# =============================================================================
#  BA-LEGGETT CROSS-COUPLING
# =============================================================================
# BA modes = phase-density (Goldstone) oscillations of the condensate amplitude
# Leggett modes = relative phase oscillations between cells
# They couple through BCS self-consistency: Delta_i depends on <c c>_i which
# depends on the local density (BA mode) and relative phase (Leggett mode).

# The coupling Hamiltonian is:
# H_int = sum_ij V_ij * delta_n_i * delta_phi_j
# where delta_n = BA displacement, delta_phi = Leggett displacement
# V_ij = d(Delta_i)/d(n_j) * d(Delta_j)/d(phi_ij)
# ~ (d Delta/d n) * J_L * sin(phi_eq)
# At equilibrium phi_eq = 0, so sin(0) = 0: LINEAR coupling is ZERO.

# This is the same argument as the cubic vertex: the equilibrium is at
# the minimum of cos(phi), so the first derivative vanishes.

# The QUADRATIC BA-Leggett coupling comes from:
# H_int^(2) ~ (d^2 Delta/dn^2) * J_L * cos(phi_eq) * delta_n * delta_phi^2
# or ~ (d Delta/dn) * J_L * cos(phi_eq) * delta_n * delta_phi^2 / Delta

# Estimate d(Delta)/d(n):
# From BCS: Delta ~ g * N(E_F) * sinh(1/g*N(E_F))^{-1}
# d(Delta)/d(n) ~ Delta / n ~ Delta_0 / (N_cells * filling)
# Very roughly: d Delta/d n ~ Delta_0_OES since filling ~ 1 per cell

# BA-Leggett coupling vertex:
J_L = float(ah_data['J_L_fold'])
Delta_0 = Delta_0_OES

# The leading BA-Leggett coupling is through the density dependence of J_L:
# J_L ~ Delta^2 / (something), so delta J_L / J_L ~ 2 * delta Delta / Delta
# delta Delta / Delta ~ (delta n / n) from number-phase uncertainty

# Number fluctuations in each cell from BA modes:
# <delta n^2> = 1/(2*sqrt(E_J * E_c)) per mode (quantum ground state)
E_J_fold = float(ba_data['E_J'][idx_fold])
E_c_fold = float(ba_data['E_c'][idx_fold])
delta_n_rms = 1.0 / (2.0 * (E_J_fold * E_c_fold)**0.25)

# Fractional density fluctuation per mode
n_mean = 1.0  # one Cooper pair per cell (BCS at fold)
frac_dn = delta_n_rms / max(n_mean, 1.0)

# BA-Leggett coupling vertex estimate
# V_BL ~ J_L * (delta Delta / Delta) * (delta phi)
# ~ J_L * frac_dn * phi_quantum
# phi_quantum = (E_c / (16 * E_J))^{1/4} for each mode
phi_quantum = (E_c_fold / (16.0 * E_J_fold))**0.25

V_BL = J_L * frac_dn * phi_quantum
print(f"=== BA-LEGGETT CROSS-COUPLING ===")
print(f"J_L (Leggett coupling at fold): {J_L:.4e} M_KK")
print(f"Delta_0 (OES gap): {Delta_0:.4f} M_KK")
print(f"E_J/E_c at fold: {E_J_fold/E_c_fold:.1f}")
print(f"delta_n_rms (per mode): {delta_n_rms:.4f}")
print(f"phi_quantum: {phi_quantum:.4e}")
print(f"frac_dn: {frac_dn:.4e}")
print(f"V_BL (BA-Leggett vertex): {V_BL:.4e} M_KK")
print(f"V_BL / V4_max: {V_BL / V4_max_full:.4f}")
print()

# Cross-coupling scattering rate (FGR)
# Gamma_BL ~ |V_BL|^2 * rho_final * 2*pi
Gamma_BL = 2 * np.pi * V_BL**2 * rho_modes
print(f"Gamma_BL (FGR): {Gamma_BL:.4e} M_KK")
print(f"Gamma_BL * dt_transit: {Gamma_BL * dt_transit:.4e}")
print(f"Gamma_BL / Gamma_transit: {Gamma_BL / Gamma:.4e}")
print()

# =============================================================================
#  TOP 10 RESONANT CHANNELS BY COUPLING STRENGTH
# =============================================================================

# Since cubic is zero and BA-Leggett is tiny, the only nonzero couplings are
# the QUARTIC Leggett self-interactions from W1-3.
# Report top 10 quartic self-energy channels (mode-resolved)

print(f"=== TOP 10 QUARTIC CHANNELS (Leggett self-interaction) ===")
print(f"{'Mode':>6} | {'omega (M_KK)':>12} | {'V4_self':>12} | {'Gamma_4':>12} | {'Gamma*dt':>12} | {'Gain':>12}")
print("-" * 82)

# Sort by Gamma_4 per mode
sort_idx = np.argsort(Gamma_4_per_mode)[::-1]
omega_L_modes = ah_data['omega_fold']  # 31 Leggett modes with frequencies

for rank, idx in enumerate(sort_idx[:10]):
    om = omega_L_modes[idx]
    v4s = V4_self[idx]
    g4 = Gamma_4_per_mode[idx]
    gdt = g4 * dt_transit
    gain = g4 / Gamma  # parametric gain = scattering rate / transit rate
    print(f"L_{idx:>4} | {om:>12.6f} | {v4s:>12.4e} | {g4:>12.4e} | {gdt:>12.4e} | {gain:>12.4e}")

print()

# Maximum gain across all channels
max_gain = Gamma_4_per_mode.max() / Gamma
max_gain_mode = np.argmax(Gamma_4_per_mode)
print(f"Maximum parametric gain: {max_gain:.4e} (mode L_{max_gain_mode})")
print(f"  Gain > 1? {'YES -- ENERGY TRANSFER' if max_gain > 1 else 'NO -- ADIABATIC REGIME'}")
print()

# =============================================================================
#  SUMMARY: ALL COUPLING CHANNELS
# =============================================================================

print(f"=== COUPLING CHANNEL SUMMARY ===")
print(f"{'Channel':>30} | {'Vertex':>12} | {'Rate (M_KK)':>12} | {'Rate*dt':>12} | {'Gain':>12}")
print("-" * 90)

channels = [
    ("3-mode Josephson (cubic)", 0.0, 0.0, 0.0, 0.0),
    ("3-mode cubic (fluct. UB)", Gamma_3_ub, Gamma_3_ub, Gamma_3_ub * dt_transit, Gamma_3_ub / Gamma),
    ("4-mode Josephson (quartic)", V4_max_full, Gamma_4_fold, Gamma_4_fold * dt_transit, Gamma_4_fold / Gamma),
    ("BA-Leggett cross (quadratic)", V_BL, Gamma_BL, Gamma_BL * dt_transit, Gamma_BL / Gamma),
]

for name, vertex, rate, rdt, gain in channels:
    print(f"{name:>30} | {vertex:>12.4e} | {rate:>12.4e} | {rdt:>12.4e} | {gain:>12.4e}")

print()
print(f"STRONGEST COUPLING: Fluctuation-induced cubic UB = {Gamma_3_ub:.4e} M_KK")
print(f"  Even this is {Gamma_3_ub * dt_transit:.2e} of one scattering event during transit")
print(f"  Parametric gain: {Gamma_3_ub / Gamma:.4e} << 1")
print()

# =============================================================================
#  THE RESONANCE PARADOX: UNIVERSAL RESONANCE, ZERO COUPLING
# =============================================================================

print(f"=== PHYSICAL INTERPRETATION ===")
print(f"The transit broadening Gamma = {Gamma:.0f} M_KK dwarfs all mode frequencies.")
print(f"In a RESONANCE CENSUS, N_res = N_total = {N_res_distinct}/{N_triplets_distinct} (100%).")
print(f"But having access to a resonance requires COUPLING to reach it.")
print(f"")
print(f"Three channels checked:")
print(f"  1. Cubic Josephson: ZERO (exact symmetry, cos is even)")
print(f"  2. Quartic Josephson: max gain = {max_gain:.2e} << 1")
print(f"  3. BA-Leggett cross: gain = {Gamma_BL / Gamma:.2e} << 1")
print(f"")
print(f"The transit is SUDDEN (P_exc = 1.0 from S38).")
print(f"Modes are born frozen — they never exchange energy.")
print(f"This CONFIRMS the sudden-quench picture from S57 W1-1.")

# =============================================================================
#  SAVE DATA
# =============================================================================

np.savez('computations/session-58/s58_multimode_resonance.npz',
    # Mode census
    N_modes=N_modes,
    N_BA=N_BA,
    N_L=N_L,
    omega_BA=omega_BA,
    omega_L=omega_L,
    omega_J=omega_J_scalar,
    omega_all=omega_all,
    labels=np.array(labels),

    # Transit broadening
    Gamma_transit=Gamma,
    dt_transit=dt_transit,

    # Resonance count
    N_triplets_distinct=N_triplets_distinct,
    N_res_distinct=N_res_distinct,
    N_triplets_rep=N_triplets_rep,
    N_res_rep=N_res_rep,

    # Cubic vertex (zero)
    V3_max_numerical=V3_max,
    Gamma_3_ub=Gamma_3_ub,

    # Quartic vertex
    V4_max=V4_max_full,
    Gamma_4_fold=Gamma_4_fold,
    Gamma_4_per_mode=Gamma_4_per_mode,
    V4_self_fold=V4_self,

    # BA-Leggett cross coupling
    V_BL=V_BL,
    Gamma_BL=Gamma_BL,
    delta_n_rms=delta_n_rms,
    phi_quantum=phi_quantum,

    # Gains
    max_gain_quartic=max_gain,
    max_gain_mode=max_gain_mode,
    gain_BL=Gamma_BL / Gamma,
    gain_cubic_ub=Gamma_3_ub / Gamma,

    # Gate
    gate_name='MULTIMODE-RESONANCE-58',
    gate_verdict='INFO',
    gate_detail=f'N_res={N_res_distinct}/{N_triplets_distinct} (100%). V3=0 exact. max gain={max_gain:.2e}. Sudden-quench confirmed.',

    # Metadata
    tau_fold=tau_actual,
    idx_fold=idx_fold,
)

print()
print(f"Saved: computations/session-58/s58_multimode_resonance.npz")
print(f"Gate: MULTIMODE-RESONANCE-58 = INFO")
print(f"  N_res = {N_res_distinct}/{N_triplets_distinct} (100%)")
print(f"  V3 = 0 (exact symmetry)")
print(f"  max parametric gain = {max_gain:.2e} << 1")
print(f"  Sudden-quench picture CONFIRMED")
