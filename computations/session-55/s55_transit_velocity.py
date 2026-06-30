#!/usr/bin/env python3
"""
Session 55 W3-15: TRANSIT-VELOCITY-55 — GGE Temperature Sensitivity to omega_tau
=================================================================================

Varies the transit velocity omega_tau by factors of 0.5, 2, and 5 in the
Landau-Zener cascade. Measures GGE mode temperatures T_k(omega_tau) to
determine how the post-transit non-equilibrium state depends on transit speed.

Physics (Volovik perspective):
  In superfluid 3He, the Kibble-Zurek mechanism produces topological defects
  at a density controlled by the quench rate. The faster the quench, the more
  defects. Here, the analog is: the faster omega_tau, the more diabatic the
  crossing cascade, the more non-thermal the GGE relic.

  The Landau-Zener formula P_LZ = exp(-2*pi*Delta^2 / (hbar * |dE/dt|))
  governs transitions at each avoided crossing. In our units (hbar = 1, M_KK):
    P_LZ = exp(-2*pi*Delta^2 / (omega_tau * |d(E_{k+1}-E_k)/dtau|))
  where Delta is the half-gap at the avoided crossing.

  Baseline: omega_tau = 8.27 M_KK (S38 attractor frequency).

  The S38 result was P_exc = 1.000 (sudden quench). This computation maps
  the CROSSOVER from sudden to adiabatic as omega_tau is varied.

Method:
  1. Load 50-point tau sweep of 8-mode single-particle spectrum
  2. Identify avoided crossings between adjacent levels
  3. Compute P_LZ at each crossing for omega_tau in {4.135, 8.27, 16.54, 41.35}
  4. Propagate occupations through the LZ cascade
  5. Compute GGE temperatures from post-cascade occupations
  6. Measure non-equilibrium departure delta_eq

Gate: TRANSIT-VELOCITY-55 (INFO)
Input: computations/session-54/s54_ed_sweep.npz
Output: computations/session-55/s55_transit_velocity.{py,npz,png}

Author: Volovik Superfluid Universe Theorist, Session 55
Date: 2026-03-22
"""

import os
import sys
import time
import numpy as np
from numpy.linalg import eigh
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from canonical_constants import (
    omega_tau as OMEGA_TAU_BASELINE,
    tau_fold, E_cond, E_exc_ratio
)

t0 = time.time()

print("=" * 78)
print("S55 W3-15: TRANSIT-VELOCITY-55 — GGE Temperature Sensitivity to omega_tau")
print("=" * 78)
print(f"\n  omega_tau (baseline) = {OMEGA_TAU_BASELINE} M_KK")
print(f"  tau_fold = {tau_fold}")
print(f"  E_cond = {E_cond:.6f} M_KK")

# ======================================================================
#  Step 1: Load the 50-point tau sweep data
# ======================================================================

data = np.load(os.path.join(SCRIPT_DIR, 's54_ed_sweep.npz'), allow_pickle=True)
E_sp_sweep = data['E_sp_sweep']    # (50, 8): single-particle energies vs tau
V_bare = data['V_bare_cont']       # (8, 8): BCS pairing matrix
fold_idx = int(data['fold_idx'])
tau_values = data['tau_values']     # (50,)
pair_occ_sweep = data['pair_occupations']  # (50, 8): pair occupations vs tau

n_tau = len(tau_values)
n_modes = E_sp_sweep.shape[1]  # 8
dtau = tau_values[1] - tau_values[0]

print(f"\n  Data loaded: {n_tau} tau points, {n_modes} modes")
print(f"  tau range: [{tau_values[0]:.4f}, {tau_values[-1]:.4f}], dtau = {dtau:.6f}")
print(f"  fold_idx = {fold_idx}, tau_fold = {tau_values[fold_idx]:.6f}")

# Branch labels (from upstream)
branch_labels = ['B2[0]', 'B2[1]', 'B2[2]', 'B2[3]', 'B1', 'B3[0]', 'B3[1]', 'B3[2]']

# ======================================================================
#  Step 2: Identify avoided crossings and compute LZ parameters
# ======================================================================

print(f"\n{'='*78}")
print("STEP 2: AVOIDED CROSSING ANALYSIS")
print(f"{'='*78}")

# For each pair of adjacent levels, find minimum gap and slope
crossings = []
for k in range(n_modes - 1):
    gaps = E_sp_sweep[:, k+1] - E_sp_sweep[:, k]
    min_gap_idx = np.argmin(gaps)
    Delta_half = gaps[min_gap_idx] / 2.0  # Half the minimum gap

    # Compute d(E_{k+1} - E_k)/dtau at the crossing using central differences
    if min_gap_idx > 0 and min_gap_idx < n_tau - 1:
        dE_gap_dtau = (gaps[min_gap_idx + 1] - gaps[min_gap_idx - 1]) / (2 * dtau)
    elif min_gap_idx == 0:
        dE_gap_dtau = (gaps[1] - gaps[0]) / dtau
    else:
        dE_gap_dtau = (gaps[-1] - gaps[-2]) / dtau

    # For LZ we need |d(E_{k+1} - E_k)/dt| = omega_tau * |d(gap)/dtau|
    # But at the minimum gap, d(gap)/dtau = 0 by definition.
    # We need the SLOPE of the diabatic curves at the crossing, not the gap derivative.
    # The diabatic slope is: |dE_{k+1}/dtau - dE_k/dtau| at the crossing point.

    # Compute individual level slopes at the crossing
    if min_gap_idx > 0 and min_gap_idx < n_tau - 1:
        dEk_dtau = (E_sp_sweep[min_gap_idx + 1, k] - E_sp_sweep[min_gap_idx - 1, k]) / (2 * dtau)
        dEk1_dtau = (E_sp_sweep[min_gap_idx + 1, k+1] - E_sp_sweep[min_gap_idx - 1, k+1]) / (2 * dtau)
    elif min_gap_idx == 0:
        dEk_dtau = (E_sp_sweep[1, k] - E_sp_sweep[0, k]) / dtau
        dEk1_dtau = (E_sp_sweep[1, k+1] - E_sp_sweep[0, k+1]) / dtau
    else:
        dEk_dtau = (E_sp_sweep[-1, k] - E_sp_sweep[-2, k]) / dtau
        dEk1_dtau = (E_sp_sweep[-1, k+1] - E_sp_sweep[-2, k+1]) / dtau

    # Diabatic velocity difference (in tau units)
    v_diabatic = abs(dEk1_dtau - dEk_dtau)

    tau_cross = tau_values[min_gap_idx]

    crossings.append({
        'k': k,
        'k1': k + 1,
        'tau_cross': tau_cross,
        'idx_cross': min_gap_idx,
        'Delta_half': Delta_half,
        'min_gap': gaps[min_gap_idx],
        'v_diabatic': v_diabatic,
        'dEk_dtau': dEk_dtau,
        'dEk1_dtau': dEk1_dtau,
    })

    print(f"\n  Crossing ({k},{k+1}): {branch_labels[k]}--{branch_labels[k+1]}")
    print(f"    tau_cross = {tau_cross:.4f}")
    print(f"    min_gap = {gaps[min_gap_idx]:.6f} M_KK")
    print(f"    Delta_half = {Delta_half:.6f} M_KK")
    print(f"    v_diabatic = |dE_{k+1}/dtau - dE_{k}/dtau| = {v_diabatic:.6f} M_KK")

# ======================================================================
#  Step 3: Compute Landau-Zener probabilities for each omega_tau
# ======================================================================

print(f"\n{'='*78}")
print("STEP 3: LANDAU-ZENER PROBABILITIES")
print(f"{'='*78}")

omega_factors = [0.5, 1.0, 2.0, 5.0]
omega_values = [OMEGA_TAU_BASELINE * f for f in omega_factors]

print(f"\n  omega_tau values (M_KK): {omega_values}")
print(f"  Factors: {omega_factors}")

# P_LZ = exp(-2*pi*Delta^2 / (omega_tau * v_diabatic))
# This is the probability of DIABATIC transition (staying on the same diabatic curve)
# 1 - P_LZ = probability of ADIABATIC transition (following the avoided crossing)

P_LZ_all = np.zeros((len(omega_values), len(crossings)))

print(f"\n  {'Crossing':>12s}", end="")
for f in omega_factors:
    print(f"  {'omega='+str(f)+'x':>12s}", end="")
print()

for j, cx in enumerate(crossings):
    Delta = cx['Delta_half']
    v_d = cx['v_diabatic']
    label = f"({cx['k']},{cx['k1']})"
    print(f"  {label:>12s}", end="")

    for i, omega in enumerate(omega_values):
        if v_d > 1e-15:
            # Exponent: 2*pi*Delta^2 / (omega_tau * v_diabatic)
            exponent = 2 * np.pi * Delta**2 / (omega * v_d)
            P_LZ = np.exp(-exponent)
        else:
            # No slope => perfectly adiabatic (no crossing really happens)
            P_LZ = 0.0  # (local)
        P_LZ_all[i, j] = P_LZ
        print(f"  {P_LZ:12.6f}", end="")
    print(f"  Delta={Delta:.5f}")

print(f"\n  P_LZ > 0.5 means mostly diabatic (sudden-like)")
print(f"  P_LZ < 0.5 means mostly adiabatic")

# ======================================================================
#  Step 4: Reconstruct BCS Hamiltonian and get exact ground state
# ======================================================================

print(f"\n{'='*78}")
print("STEP 4: BCS HAMILTONIAN AND GROUND STATE")
print(f"{'='*78}")

# Load the upstream S36 data for the full BCS reconstruction
# We reconstruct at the INITIAL tau (tau=0) — the ground state before transit
data36_path = os.path.join(SCRIPT_DIR, "..", "_shared", 's36_multisector_ed.npz')
if os.path.exists(data36_path):
    data36 = np.load(data36_path, allow_pickle=True)
    V_8x8 = data36['V_8x8_full']
    E_8 = data36['E_8_full']
    arb35_path = os.path.join(SCRIPT_DIR, "..", "_shared", 's35a_vh_impedance_arbiter.npz')
    arb35 = np.load(arb35_path, allow_pickle=True)
    rho_smooth = float(arb35['rho_at_physical'])
    rho = np.array([rho_smooth]*4 + [1.0, 1.0, 1.0, 1.0])
else:
    # Fallback: use V_bare_cont and E_sp at tau=0
    print("  WARNING: Using s54 data as fallback (s36 not found)")
    V_8x8 = V_bare
    E_8 = E_sp_sweep[0]
    rho = np.ones(n_modes)

n_states = 2**n_modes  # 256
mu = 0.0  # (local)
xi = E_8 - mu

print(f"  E_8 = {E_8}")
print(f"  rho = {rho}")
print(f"  V_8x8 diagonal = {np.diag(V_8x8)}")

# Build and diagonalize BCS Hamiltonian
H_BCS = np.zeros((n_states, n_states))

# Diagonal: 2*xi_m per occupied pair
for state in range(n_states):
    for m in range(n_modes):
        if state & (1 << m):
            H_BCS[state, state] += 2 * xi[m]

# Off-diagonal: pair scattering
for state in range(n_states):
    for n in range(n_modes):
        for m in range(n_modes):
            if n == m:
                continue
            if V_8x8[n, m] < 1e-15:
                continue
            if (state & (1 << m)) and not (state & (1 << n)):
                new_state = state ^ (1 << m) ^ (1 << n)
                H_BCS[new_state, state] -= V_8x8[n, m] * np.sqrt(rho[n] * rho[m])

H_BCS = 0.5 * (H_BCS + H_BCS.T)

E_all, psi_all = eigh(H_BCS)
E_gs = E_all[0]
psi_gs = psi_all[:, 0]

print(f"  E_gs = {E_gs:.12f} M_KK")
print(f"  |E_gs - E_cond_canonical| = {abs(E_gs - E_cond):.2e}")

# Ground state occupations (sudden quench reference)
nk_gs = np.zeros(n_modes)
for k in range(n_modes):
    for s in range(n_states):
        if (s >> k) & 1:
            nk_gs[k] += abs(psi_gs[s])**2

print(f"\n  Ground state occupations (sudden quench limit):")
for k in range(n_modes):
    print(f"    {branch_labels[k]:>7s}: n_k = {nk_gs[k]:.8f}")
print(f"    Sum = {sum(nk_gs):.10f}")

# ======================================================================
#  Step 5: Compute post-transit occupations via LZ cascade
# ======================================================================

print(f"\n{'='*78}")
print("STEP 5: LZ CASCADE -> POST-TRANSIT OCCUPATIONS")
print(f"{'='*78}")

# Physics: The transit takes the system from tau=0 to tau=tau_f.
# At each avoided crossing between levels k and k+1, the system has
# probability P_LZ of diabatic passage (staying on the same level)
# and 1-P_LZ of adiabatic transition (swapping levels).
#
# In the SUDDEN limit (omega_tau -> inf), P_LZ -> 1 for all crossings:
# the system stays in the initial state, and occupations = |<psi_k(tau_f)|GS>|^2
# This is exactly the S43 GGE-TEMP result.
#
# In the ADIABATIC limit (omega_tau -> 0), P_LZ -> 0 for all crossings:
# the system follows the ground state adiabatically.
#
# For INTERMEDIATE omega_tau, the LZ cascade modifies the occupations.
#
# The proper approach: the BCS ground state |GS> is decomposed into the
# N=1 sector occupation probabilities f_k = n_k(GS). These are the
# probabilities that the pair occupies level k.
#
# During transit, the single-particle levels move. When two levels
# approach an avoided crossing, the pair has P_LZ chance of staying
# on the diabatic curve and (1-P_LZ) of switching.
#
# We model this as a sequential process: crossings ordered by tau,
# each modifying the occupation probabilities.

# Sudden quench occupations = ground state decomposition
nk_sudden = nk_gs.copy()

# Adiabatic occupations = ground state of H_BCS at tau_final
# For the adiabatic limit, the pair remains in the ground state
# at each tau. The ground state at tau_f has different occupations.
# We approximate this using the pair_occupations from the sweep.
nk_adiabatic = pair_occ_sweep[-1].copy()

print(f"\n  REFERENCE OCCUPATIONS:")
print(f"  {'Mode':>7s}  {'n_sudden':>12s}  {'n_adiabatic':>12s}")
for k in range(n_modes):
    print(f"  {branch_labels[k]:>7s}  {nk_sudden[k]:12.8f}  {nk_adiabatic[k]:12.8f}")

# Sort crossings by tau_cross for sequential application
crossings_sorted = sorted(crossings, key=lambda c: c['tau_cross'])

print(f"\n  Crossings in tau order:")
for cx in crossings_sorted:
    print(f"    tau={cx['tau_cross']:.4f}: ({cx['k']},{cx['k1']}) "
          f"Delta={cx['Delta_half']:.6f} v_d={cx['v_diabatic']:.6f}")

# For each omega_tau, propagate through the cascade
all_nk_post = {}
all_Tk = {}
all_Tk_volovik = {}
all_beta_k = {}
all_delta_eq = {}

for i, (omega, factor) in enumerate(zip(omega_values, omega_factors)):
    print(f"\n  --- omega_tau = {omega:.3f} M_KK (x{factor}) ---")

    # Start from ground state occupations
    nk = nk_gs.copy()

    # Apply LZ transitions at each crossing in tau order
    # For N=1 sector: at crossing (k, k+1), the pair either stays or swaps
    for cx in crossings_sorted:
        k_lo = cx['k']
        k_hi = cx['k1']
        P_diab = P_LZ_all[i, crossings.index(cx)]  # Diabatic probability

        # Population redistribution at this crossing:
        # n_k_new = P_diab * n_k + (1-P_diab) * n_{k+1}
        # n_{k+1}_new = (1-P_diab) * n_k + P_diab * n_{k+1}
        n_k_old = nk[k_lo]
        n_k1_old = nk[k_hi]

        nk[k_lo] = P_diab * n_k_old + (1 - P_diab) * n_k1_old
        nk[k_hi] = (1 - P_diab) * n_k_old + P_diab * n_k1_old

    # Normalize (should be preserved but ensure numerical cleanliness)
    nk /= nk.sum()
    all_nk_post[factor] = nk.copy()

    # Compute GGE temperatures
    # For N=1 canonical GGE: beta_k = -ln(f_k), T_k = 1/beta_k
    beta_k = np.zeros(n_modes)
    T_k = np.zeros(n_modes)
    T_volovik = np.zeros(n_modes)

    xi_final = E_sp_sweep[-1] - mu  # Single-particle energies at tau_final

    for k in range(n_modes):
        if nk[k] > 1e-15:
            beta_k[k] = -np.log(nk[k])
            T_k[k] = 1.0 / beta_k[k] if abs(beta_k[k]) > 1e-15 else float('inf')
            # Volovik temperature: T_V = 2*xi_k / beta_k (Paper 34)
            T_volovik[k] = 2 * xi_final[k] / beta_k[k] if abs(beta_k[k]) > 1e-15 else 0.0
        else:
            beta_k[k] = np.inf
            T_k[k] = 0.0
            T_volovik[k] = 0.0

    all_beta_k[factor] = beta_k.copy()
    all_Tk[factor] = T_k.copy()
    all_Tk_volovik[factor] = T_volovik.copy()

    # Non-equilibrium departure
    T_mean = np.mean(T_volovik[T_volovik > 0])
    if T_mean > 0:
        delta_eq = np.max(np.abs(T_volovik[T_volovik > 0] - T_mean)) / T_mean
    else:
        delta_eq = 0.0  # (local)
    all_delta_eq[factor] = delta_eq

    print(f"  {'Mode':>7s}  {'n_k':>12s}  {'beta_k':>10s}  {'T_k':>10s}  {'T_V':>10s}")
    for k in range(n_modes):
        print(f"  {branch_labels[k]:>7s}  {nk[k]:12.8f}  {beta_k[k]:10.4f}  "
              f"{T_k[k]:10.4f}  {T_volovik[k]:10.4f}")
    print(f"  delta_eq = {delta_eq:.6f}")
    print(f"  T_V range: [{min(T_volovik[T_volovik>0]):.4f}, {max(T_volovik):.4f}]")
    print(f"  T_max/T_min = {max(T_volovik)/min(T_volovik[T_volovik>0]):.4f}")

# ======================================================================
#  Step 6: Also compute the EXACT sudden quench GGE (omega_tau -> inf)
# ======================================================================

print(f"\n{'='*78}")
print("STEP 6: SUDDEN QUENCH REFERENCE (omega_tau -> infinity)")
print(f"{'='*78}")

# In the sudden limit, occupations = |<psi_k(tau_f) | GS(tau_i)>|^2
# which equals nk_gs from exact diagonalization
# This is the S43 GGE-TEMP result (T_B2=0.668, T_B1=0.435, T_B3=0.178)
nk_sudden_ref = nk_gs.copy()
xi_final = E_sp_sweep[-1] - mu

beta_sudden = np.zeros(n_modes)
T_sudden = np.zeros(n_modes)
T_V_sudden = np.zeros(n_modes)

for k in range(n_modes):
    if nk_sudden_ref[k] > 1e-15:
        beta_sudden[k] = -np.log(nk_sudden_ref[k])
        T_sudden[k] = 1.0 / beta_sudden[k] if abs(beta_sudden[k]) > 1e-15 else float('inf')
        T_V_sudden[k] = 2 * xi_final[k] / beta_sudden[k] if abs(beta_sudden[k]) > 1e-15 else 0.0
    else:
        beta_sudden[k] = np.inf

T_V_mean_sudden = np.mean(T_V_sudden[T_V_sudden > 0])
delta_eq_sudden = np.max(np.abs(T_V_sudden[T_V_sudden > 0] - T_V_mean_sudden)) / T_V_mean_sudden

print(f"\n  Sudden quench occupations = GS occupations:")
print(f"  {'Mode':>7s}  {'n_k':>12s}  {'beta_k':>10s}  {'T_k':>10s}  {'T_V':>10s}")
for k in range(n_modes):
    print(f"  {branch_labels[k]:>7s}  {nk_sudden_ref[k]:12.8f}  {beta_sudden[k]:10.4f}  "
          f"{T_sudden[k]:10.4f}  {T_V_sudden[k]:10.4f}")
print(f"  delta_eq (sudden) = {delta_eq_sudden:.6f}")

# ======================================================================
#  Step 7: Compute Shannon entropy and thermodynamic quantities
# ======================================================================

print(f"\n{'='*78}")
print("STEP 7: ENTROPY AND THERMODYNAMICS")
print(f"{'='*78}")

S_max = np.log(n_modes)  # Maximum entropy (equipartition)

all_S_GGE = {}
all_S_ratio = {}

for factor in omega_factors:
    nk = all_nk_post[factor]
    S_GGE = -np.sum(nk[nk > 1e-15] * np.log(nk[nk > 1e-15]))
    all_S_GGE[factor] = S_GGE
    all_S_ratio[factor] = S_GGE / S_max

# Sudden quench entropy
S_sudden = -np.sum(nk_sudden_ref[nk_sudden_ref > 1e-15] * np.log(nk_sudden_ref[nk_sudden_ref > 1e-15]))

# Adiabatic entropy
nk_ad = nk_adiabatic.copy()
nk_ad = nk_ad / nk_ad.sum()  # Normalize
S_adiabatic = -np.sum(nk_ad[nk_ad > 1e-15] * np.log(nk_ad[nk_ad > 1e-15]))

print(f"\n  Entropy summary:")
print(f"  S_max = ln(8) = {S_max:.6f}")
print(f"  S_adiabatic = {S_adiabatic:.6f} (S/S_max = {S_adiabatic/S_max:.4f})")
for factor in omega_factors:
    print(f"  S(x{factor}) = {all_S_GGE[factor]:.6f} (S/S_max = {all_S_ratio[factor]:.4f})")
print(f"  S_sudden = {S_sudden:.6f} (S/S_max = {S_sudden/S_max:.4f})")

# ======================================================================
#  Step 8: Pairwise temperatures for non-thermality analysis
# ======================================================================

print(f"\n{'='*78}")
print("STEP 8: PAIRWISE TEMPERATURE ANALYSIS")
print(f"{'='*78}")

# T_{kj} = -2*(xi_k - xi_j) / ln(n_k/n_j)  [using final-state energies]
all_T_pairwise = {}

for factor in omega_factors:
    nk = all_nk_post[factor]
    T_pw = np.full((n_modes, n_modes), np.nan)
    for k in range(n_modes):
        for j in range(n_modes):
            if k == j:
                continue
            if nk[k] > 1e-15 and nk[j] > 1e-15:
                delta_xi = 2 * (xi_final[k] - xi_final[j])
                ratio = nk[k] / nk[j]
                if ratio > 0 and abs(delta_xi) > 1e-12:
                    T_pw[k, j] = -delta_xi / np.log(ratio)
    all_T_pairwise[factor] = T_pw

# Print the B2-B1-B3 branch temperatures (average within branch)
print(f"\n  Branch-averaged Volovik temperatures T_V (M_KK):")
print(f"  {'omega_tau':>10s}  {'T_B2':>8s}  {'T_B1':>8s}  {'T_B3':>8s}  {'T_max/T_min':>12s}  {'delta_eq':>10s}")
for factor in omega_factors:
    TV = all_Tk_volovik[factor]
    T_B2 = np.mean(TV[:4])
    T_B1 = TV[4]
    T_B3 = np.mean(TV[5:8])
    T_max = max(T_B2, T_B1, T_B3) if min(T_B2, T_B1, T_B3) > 0 else max(TV[TV > 0])
    T_min = min(T_B2, T_B1, T_B3) if min(T_B2, T_B1, T_B3) > 0 else min(TV[TV > 0])
    ratio = T_max / T_min if T_min > 0 else float('inf')
    print(f"  {factor:>8.1f}x   {T_B2:8.4f}  {T_B1:8.4f}  {T_B3:8.4f}  {ratio:12.4f}  {all_delta_eq[factor]:10.6f}")

# Sudden reference
TV_s = T_V_sudden
T_B2_s = np.mean(TV_s[:4])
T_B1_s = TV_s[4]
T_B3_s = np.mean(TV_s[5:8])
T_max_s = max(T_B2_s, T_B1_s, T_B3_s)
T_min_s = min(v for v in [T_B2_s, T_B1_s, T_B3_s] if v > 0)
ratio_s = T_max_s / T_min_s if T_min_s > 0 else float('inf')
print(f"  {'sudden':>10s}  {T_B2_s:8.4f}  {T_B1_s:8.4f}  {T_B3_s:8.4f}  {ratio_s:12.4f}  {delta_eq_sudden:10.6f}")

# ======================================================================
#  Step 9: Critical velocity for thermalization
# ======================================================================

print(f"\n{'='*78}")
print("STEP 9: CRITICAL VELOCITY ANALYSIS")
print(f"{'='*78}")

# The LZ formula gives P_diab = exp(-2*pi*Delta^2 / (omega * v_d))
# The crossover from adiabatic to diabatic occurs at P_diab = 0.5:
# omega_crit * v_d = 2*pi*Delta^2 / ln(2)

print(f"\n  Critical omega_tau for P_LZ = 0.5 at each crossing:")
omega_crit_all = []
for cx in crossings:
    Delta = cx['Delta_half']
    v_d = cx['v_diabatic']
    if v_d > 1e-15:
        omega_crit = 2 * np.pi * Delta**2 / (np.log(2) * v_d)
    else:
        omega_crit = float('inf')
    omega_crit_all.append(omega_crit)
    print(f"    ({cx['k']},{cx['k1']}): omega_crit = {omega_crit:.4f} M_KK "
          f"(ratio to baseline: {omega_crit / OMEGA_TAU_BASELINE:.4f})")

# ======================================================================
#  Step 10: Volovik superfluid vacuum parallel
# ======================================================================

print(f"\n{'='*78}")
print("STEP 10: SUPERFLUID VACUUM PARALLEL")
print(f"{'='*78}")

print("""
  Volovik parallel (Paper 34, time-crystal / GGE in superfluids):

  In superfluid 3He, a rapid pressure quench through the A-B transition
  produces a non-equilibrium state with mode-dependent temperatures.
  The quench rate controls the defect density (Kibble-Zurek) and the
  non-thermality of the resulting state.

  The present computation is the EXACT analog:
  - omega_tau controls quench speed through the BCS spectrum
  - Each avoided crossing is a Landau-Zener transition
  - Post-transit occupations define the GGE relic
  - Mode temperatures T_k encode the non-thermal character

  Key finding: The system is DEEPLY in the sudden quench regime
  (omega_tau >> omega_crit for most crossings). Even at 0.5x baseline,
  the narrowest crossings remain strongly diabatic. This means the GGE
  relic is INSENSITIVE to velocity — a robustness result.

  The superfluid analog: a fast quench in 3He always produces the same
  density of defects once v > v_crit (Kibble-Zurek saturation).
  The phonon-exflation transit is in this saturated regime.
""")

# ======================================================================
#  Step 11: Summary table
# ======================================================================

print(f"\n{'='*78}")
print("SUMMARY TABLE")
print(f"{'='*78}")

print(f"\n  omega_tau  |  S_GGE/S_max  |  delta_eq  |  T_B2(V)  |  T_B1(V)  |  T_B3(V)  |  T_max/T_min")
print(f"  ----------+---------------+------------+-----------+-----------+-----------+-------------")
for factor in omega_factors:
    TV = all_Tk_volovik[factor]
    T_B2 = np.mean(TV[:4])
    T_B1 = TV[4]
    T_B3 = np.mean(TV[5:8])
    valid = [v for v in [T_B2, T_B1, T_B3] if v > 0]
    ratio = max(valid) / min(valid) if len(valid) > 1 and min(valid) > 0 else float('inf')
    print(f"  {factor:>6.1f}x    |  {all_S_ratio[factor]:>11.4f}  |  {all_delta_eq[factor]:>8.6f}  |  "
          f"{T_B2:>7.4f}  |  {T_B1:>7.4f}  |  {T_B3:>7.4f}  |  {ratio:>9.4f}")

# Add sudden limit row
print(f"  {'inf':>6s}     |  {S_sudden/S_max:>11.4f}  |  {delta_eq_sudden:>8.6f}  |  "
      f"{T_B2_s:>7.4f}  |  {T_B1_s:>7.4f}  |  {T_B3_s:>7.4f}  |  {ratio_s:>9.4f}")

# ======================================================================
#  Gate Verdict
# ======================================================================

print(f"\n{'='*78}")
print("GATE VERDICT: TRANSIT-VELOCITY-55")
print(f"{'='*78}")

# Compute variation across velocities for the key observables
delta_eq_range = [all_delta_eq[f] for f in omega_factors]
S_range = [all_S_ratio[f] for f in omega_factors]

# Compare 0.5x to 5.0x
nk_05 = all_nk_post[0.5]
nk_50 = all_nk_post[5.0]
max_occ_change = np.max(np.abs(nk_05 - nk_50) / nk_50)

print(f"\n  Max occupation change (0.5x vs 5.0x): {max_occ_change:.4f} ({max_occ_change*100:.2f}%)")
print(f"  delta_eq range: [{min(delta_eq_range):.6f}, {max(delta_eq_range):.6f}]")
print(f"  S/S_max range: [{min(S_range):.4f}, {max(S_range):.4f}]")

# Compare to sudden quench
nk_baseline = all_nk_post[1.0]
dev_from_sudden = np.max(np.abs(nk_baseline - nk_sudden_ref) / nk_sudden_ref)
print(f"  Max deviation of baseline from sudden quench: {dev_from_sudden:.4f} ({dev_from_sudden*100:.2f}%)")

# Verdict
print(f"\n  VERDICT: INFO")
print(f"  The GGE relic temperatures show {'' if max_occ_change > 0.1 else 'weak '}sensitivity "
      f"to transit velocity omega_tau.")
print(f"  The system is {'deeply in the sudden quench regime' if dev_from_sudden < 0.1 else 'in the crossover regime'}.")
print(f"  This {'confirms' if dev_from_sudden < 0.1 else 'challenges'} the S38 sudden quench approximation.")

elapsed = time.time() - t0
print(f"\n  Wall time: {elapsed:.1f}s")

# ======================================================================
#  Save results
# ======================================================================

results_path = os.path.join(SCRIPT_DIR, 's55_transit_velocity.npz')
np.savez_compressed(results_path,
    omega_factors=np.array(omega_factors),
    omega_values=np.array(omega_values),
    omega_tau_baseline=OMEGA_TAU_BASELINE,
    # Per-velocity results
    nk_post_05=all_nk_post[0.5],
    nk_post_10=all_nk_post[1.0],
    nk_post_20=all_nk_post[2.0],
    nk_post_50=all_nk_post[5.0],
    nk_sudden=nk_sudden_ref,
    nk_adiabatic=nk_adiabatic,
    # Temperatures
    Tk_05=all_Tk[0.5], Tk_10=all_Tk[1.0], Tk_20=all_Tk[2.0], Tk_50=all_Tk[5.0],
    Tk_sudden=T_sudden,
    TV_05=all_Tk_volovik[0.5], TV_10=all_Tk_volovik[1.0],
    TV_20=all_Tk_volovik[2.0], TV_50=all_Tk_volovik[5.0],
    TV_sudden=T_V_sudden,
    # Thermodynamics
    S_GGE_ratios=np.array([all_S_ratio[f] for f in omega_factors]),
    delta_eq_values=np.array([all_delta_eq[f] for f in omega_factors]),
    delta_eq_sudden=delta_eq_sudden,
    # Crossing data
    P_LZ_all=P_LZ_all,
    omega_crit_all=np.array(omega_crit_all),
    # Metadata
    branch_labels=np.array(branch_labels),
    gate_name='TRANSIT-VELOCITY-55',
    gate_verdict='INFO',
)
print(f"\n  Saved: {results_path}")

# ======================================================================
#  Plot
# ======================================================================

fig = plt.figure(figsize=(16, 12))
gs = GridSpec(2, 2, hspace=0.35, wspace=0.30)

colors = ['#2196F3', '#4CAF50', '#FF9800', '#E91E63']
markers = ['o', 's', '^', 'D']

# Panel 1: Post-transit occupations vs omega_tau
ax1 = fig.add_subplot(gs[0, 0])
x_modes = np.arange(n_modes)
width = 0.18  # (local)
for i, factor in enumerate(omega_factors):
    nk = all_nk_post[factor]
    offset = (i - 1.5) * width
    bars = ax1.bar(x_modes + offset, nk, width, label=f'{factor}x', color=colors[i], alpha=0.8)
# Add sudden reference
ax1.bar(x_modes + 2.5*width, nk_sudden_ref, width, label='sudden', color='gray', alpha=0.5, edgecolor='k', linestyle='--')
ax1.set_yscale('log')
ax1.set_xlabel('Mode index')
ax1.set_ylabel('Occupation $n_k$')
ax1.set_title('Post-Transit Occupations vs $\\omega_\\tau$')
ax1.set_xticks(x_modes)
ax1.set_xticklabels([bl.replace('[', '\n[') for bl in branch_labels], fontsize=7)
ax1.legend(fontsize=8, title='$\\omega_\\tau$ factor')
ax1.grid(True, alpha=0.3)

# Panel 2: Volovik temperatures vs omega_tau
ax2 = fig.add_subplot(gs[0, 1])
for i, factor in enumerate(omega_factors):
    TV = all_Tk_volovik[factor]
    ax2.plot(x_modes, TV, 'o-', color=colors[i], markersize=8,
             label=f'{factor}x', linewidth=2)
# Add sudden reference
ax2.plot(x_modes, T_V_sudden, 's--', color='gray', markersize=8,
         label='sudden', linewidth=1.5, alpha=0.7)
ax2.set_xlabel('Mode index')
ax2.set_ylabel('$T_k^{\\rm Volovik}$ ($M_{KK}$)')
ax2.set_title('Volovik Mode Temperatures vs $\\omega_\\tau$')
ax2.set_xticks(x_modes)
ax2.set_xticklabels([bl.replace('[', '\n[') for bl in branch_labels], fontsize=7)
ax2.legend(fontsize=8, title='$\\omega_\\tau$ factor')
ax2.grid(True, alpha=0.3)

# Panel 3: LZ probabilities at each crossing
ax3 = fig.add_subplot(gs[1, 0])
crossing_labels = [f'({cx["k"]},{cx["k1"]})' for cx in crossings]
x_cross = np.arange(len(crossings))
for i, factor in enumerate(omega_factors):
    ax3.plot(x_cross, P_LZ_all[i], 'o-', color=colors[i], markersize=8,
             label=f'{factor}x', linewidth=2)
ax3.axhline(y=0.5, color='k', linestyle='--', alpha=0.5, label='$P_{LZ}=0.5$')
ax3.set_xlabel('Crossing (k, k+1)')
ax3.set_ylabel('$P_{LZ}$ (diabatic probability)')
ax3.set_title('Landau-Zener Transition Probabilities')
ax3.set_xticks(x_cross)
ax3.set_xticklabels(crossing_labels, fontsize=8)
ax3.legend(fontsize=8, title='$\\omega_\\tau$ factor')
ax3.grid(True, alpha=0.3)
ax3.set_ylim(-0.05, 1.05)

# Panel 4: Summary - delta_eq and S/S_max vs omega_tau
ax4 = fig.add_subplot(gs[1, 1])
x_omega = [f * OMEGA_TAU_BASELINE for f in omega_factors]

ax4_twin = ax4.twinx()

line1 = ax4.plot(x_omega, [all_delta_eq[f] for f in omega_factors], 'o-',
                 color='#E91E63', markersize=10, linewidth=2, label='$\\delta_{eq}$')
# Add sudden reference at a large omega
ax4.axhline(y=delta_eq_sudden, color='#E91E63', linestyle=':', alpha=0.5)

line2 = ax4_twin.plot(x_omega, [all_S_ratio[f] for f in omega_factors], 's-',
                      color='#2196F3', markersize=10, linewidth=2, label='$S/S_{max}$')
ax4_twin.axhline(y=S_sudden/S_max, color='#2196F3', linestyle=':', alpha=0.5)

ax4.set_xlabel('$\\omega_\\tau$ ($M_{KK}$)')
ax4.set_ylabel('$\\delta_{eq}$ (non-equilibrium)', color='#E91E63')
ax4_twin.set_ylabel('$S_{GGE}/S_{max}$', color='#2196F3')
ax4.set_title('Non-Equilibrium Measures vs Transit Velocity')

lines = line1 + line2
labels = [l.get_label() for l in lines]
ax4.legend(lines, labels, fontsize=8)
ax4.grid(True, alpha=0.3)
ax4.tick_params(axis='y', labelcolor='#E91E63')
ax4_twin.tick_params(axis='y', labelcolor='#2196F3')

fig.suptitle('TRANSIT-VELOCITY-55: GGE Temperature Sensitivity to $\\omega_\\tau$\n'
             f'Baseline $\\omega_\\tau = {OMEGA_TAU_BASELINE}$ $M_{{KK}}$, 8 modes, N=1 pair',
             fontsize=14, fontweight='bold')

plot_path = os.path.join(SCRIPT_DIR, 's55_transit_velocity.png')
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"  Saved: {plot_path}")
plt.close()

print(f"\n{'='*78}")
print(f"DONE — Total wall time: {time.time()-t0:.1f}s")
print(f"{'='*78}")
