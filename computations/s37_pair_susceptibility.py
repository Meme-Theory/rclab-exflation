#!/usr/bin/env python3
"""
Session 37: F.2 Pair Susceptibility + F.3 Vacuum Polarization Energy
=====================================================================

Computes the dynamical pair susceptibility chi_pair(omega) via the Lehmann
representation using ALL 256 eigenstates from the 8-mode BCS exact
diagonalization (ED-CONV-36).

The pair susceptibility:
  chi_pair(omega) = Sum_n [ |<n|P^dag|0>|^2 / (omega - omega_n + i*eta)
                          - |<n|P|0>|^2    / (omega + omega_n + i*eta) ]

where omega_n = E_n - E_0 and P^dag = Sum_k b_k^dag (pair creation operator).

Physical content:
  - Im chi_pair(omega) = spectral density of pair fluctuations
  - Poles below 2*Delta = pair-vibrational (virtual) excitations
  - Continuum above 2*Delta = pair-breaking excitations
  - E_vac = -(1/2pi) * integral_0^{2Delta} Im chi(omega) * omega d(omega)

This is the nuclear-physics standard analysis: the pair-vibrational spectrum
reveals the structure of virtual pair fluctuations in the BCS vacuum.

Nuclear benchmarks:
  - Pole-to-continuum ratio: 0.3-0.7 (mid-shell), >0.9 (near closures)
  - |E_vac|/|E_cond|: 0.05-0.15

Author: Nazarewicz Nuclear Structure Theorist, Session 37
Date: 2026-03-08
"""

import os
import sys
import time
import numpy as np
from numpy.linalg import eigh
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
t0 = time.time()

print("=" * 78)
print("Session 37: F.2 Pair Susceptibility + F.3 Vacuum Polarization Energy")
print("=" * 78)

# ======================================================================
#  Step 1: Load stored data and reconstruct full Hamiltonian
# ======================================================================

data = np.load(os.path.join(SCRIPT_DIR, 's36_multisector_ed.npz'),
               allow_pickle=True)
vh_arbiter = np.load(os.path.join(SCRIPT_DIR, 's35a_vh_impedance_arbiter.npz'),
                     allow_pickle=True)

V_8x8 = data['V_8x8_full']        # 8x8 interaction matrix
E_8 = data['E_8_full']            # 8 single-particle energies
branch_labels = list(data['branch_labels'])
E_cond_stored = float(data['config_4_E_cond'])

# Physical parameters (matching ED-CONV-36 exactly)
n_modes = 8
n_states = 2**n_modes  # 256
mu = 0.0
xi = E_8 - mu  # xi_m = E_m - mu

# DOS: B2 modes get van Hove rho (exact value from arbiter), B1 and B3 get 1.0
rho_smooth = float(vh_arbiter['rho_at_physical'])  # 14.023250234055
rho = np.array([rho_smooth]*4 + [1.0, 1.0, 1.0, 1.0])

print(f"\nPhysical parameters:")
print(f"  N_modes = {n_modes}, N_states = {n_states}")
print(f"  mu = {mu}")
print(f"  E_8 = {E_8}")
print(f"  rho = {rho}")
print(f"  branch_labels = {branch_labels}")
print(f"  V_8x8 diagonal = {np.diag(V_8x8)}")
print(f"  E_cond (stored) = {E_cond_stored:.10f}")

# ======================================================================
#  Step 2: Reconstruct and diagonalize the pair Hamiltonian
# ======================================================================

print(f"\nReconstructing BCS pair Hamiltonian ({n_states}x{n_states})...")

H = np.zeros((n_states, n_states))

# Diagonal: kinetic energy 2*xi_m for each occupied pair
for state in range(n_states):
    for m in range(n_modes):
        if state & (1 << m):
            H[state, state] += 2 * xi[m]

# Off-diagonal: pair scattering -V_nm * sqrt(rho_n * rho_m) * b_n^dag b_m
for state in range(n_states):
    for n in range(n_modes):
        for m in range(n_modes):
            if n == m:
                continue
            if V_8x8[n, m] < 1e-15:
                continue
            # b_n^dag b_m: annihilate pair m, create pair n
            if (state & (1 << m)) and not (state & (1 << n)):
                new_state = state ^ (1 << m) ^ (1 << n)
                H[new_state, state] -= V_8x8[n, m] * np.sqrt(rho[n] * rho[m])

H = 0.5 * (H + H.T)  # Ensure Hermiticity

# Full diagonalization
E_all, psi_all = eigh(H)
E_gs = E_all[0]
psi_gs = psi_all[:, 0]

print(f"  E_gs = {E_gs:.10f}")
print(f"  E_cond check: |E_gs - stored| = {abs(E_gs - E_cond_stored):.2e}")
assert abs(E_gs - E_cond_stored) < 1e-10, \
    f"FATAL: E_gs mismatch: {E_gs} vs {E_cond_stored}"

# Excitation energies
omega_n = E_all - E_gs  # All non-negative
print(f"  omega_n range: [{omega_n[0]:.6f}, {omega_n[-1]:.6f}]")
print(f"  First 15 excitation energies:")
for i in range(min(15, len(omega_n))):
    print(f"    omega[{i:3d}] = {omega_n[i]:.10f}")

# ======================================================================
#  Step 3: Construct pair creation operator P^dag = Sum_k b_k^dag
# ======================================================================

print(f"\nConstructing pair creation operator P^dag = Sum_k b_k^dag...")

# P^dag|state> = Sum_k b_k^dag|state>
# b_k^dag|state> = |state with bit k set> if bit k is 0, else 0
# We need the matrix elements <n|P^dag|0> for all eigenstates |n>

# Method: construct P^dag as a matrix, then compute P^dag|GS>
# P^dag is (n_states x n_states) but very sparse

# More efficient: compute P^dag|psi_gs> directly in Fock space
Pdag_psi_gs = np.zeros(n_states)
for state in range(n_states):
    amp = psi_gs[state]
    if abs(amp) < 1e-16:
        continue
    for k in range(n_modes):
        if not (state & (1 << k)):  # bit k is 0, can create pair
            new_state = state | (1 << k)
            Pdag_psi_gs[new_state] += amp

# Similarly, P|psi_gs> (pair annihilation)
P_psi_gs = np.zeros(n_states)
for state in range(n_states):
    amp = psi_gs[state]
    if abs(amp) < 1e-16:
        continue
    for k in range(n_modes):
        if state & (1 << k):  # bit k is 1, can annihilate pair
            new_state = state ^ (1 << k)
            P_psi_gs[new_state] += amp

# Matrix elements in the energy eigenbasis
# <n|P^dag|0> = psi_n^T . P^dag|psi_gs>
# <n|P|0> = psi_n^T . P|psi_gs>

mat_elem_Pdag = psi_all.T @ Pdag_psi_gs  # shape (256,)
mat_elem_P = psi_all.T @ P_psi_gs        # shape (256,)

# Spectral weights
B_n_plus = np.abs(mat_elem_Pdag)**2   # |<n|P^dag|0>|^2
B_n_minus = np.abs(mat_elem_P)**2     # |<n|P|0>|^2

# Sum rules
sum_Pdag = np.sum(B_n_plus)
sum_P = np.sum(B_n_minus)

# The sum rule: Sum_n |<n|P^dag|0>|^2 = <0|P P^dag|0>
# P P^dag = Sum_k b_k Sum_l b_l^dag = Sum_k (1 - n_k) for k=l, plus cross terms
# For different k,l: b_k b_l^dag = delta_{kl}(1-n_k) (hard-core bosons)
# Actually P P^dag = Sum_k Sum_l b_k b_l^dag. For k != l, b_k b_l^dag creates l, destroys k.
# For k = l, b_k b_k^dag = 1 - n_k.
# So <0|P P^dag|0> = Sum_k <0|(1-n_k)|0> + Sum_{k!=l} <0|b_k b_l^dag|0>

pair_occ = data['config_4_pair_occ']
expected_PP_dag = np.sum(1 - pair_occ)  # Diagonal part only, cross terms nonzero too

print(f"\nMatrix element analysis:")
print(f"  Sum |<n|P^dag|0>|^2 = {sum_Pdag:.10f}")
print(f"  Sum |<n|P|0>|^2    = {sum_P:.10f}")
print(f"  Sum (1 - <n_k>)    = {expected_PP_dag:.10f}")

# Identify dominant transitions
print(f"\nDominant P^dag transitions (|<n|P^dag|0>|^2 > 1e-4):")
print(f"  {'n':>5s}  {'omega_n':>12s}  {'|<n|P^dag|0>|^2':>16s}  {'cum_frac':>10s}")
cum = 0.0
n_dominant_Pdag = 0
dominant_Pdag_indices = []
for i in np.argsort(-B_n_plus):
    if B_n_plus[i] < 1e-6:
        break
    cum += B_n_plus[i]
    frac = cum / sum_Pdag
    n_dominant_Pdag += 1
    dominant_Pdag_indices.append(i)
    if n_dominant_Pdag <= 30:
        print(f"  {i:5d}  {omega_n[i]:12.6f}  {B_n_plus[i]:16.10f}  {frac:10.6f}")

print(f"  Total dominant transitions: {n_dominant_Pdag}")

print(f"\nDominant P transitions (|<n|P|0>|^2 > 1e-4):")
print(f"  {'n':>5s}  {'omega_n':>12s}  {'|<n|P|0>|^2':>16s}  {'cum_frac':>10s}")
cum = 0.0
n_dominant_P = 0
dominant_P_indices = []
for i in np.argsort(-B_n_minus):
    if B_n_minus[i] < 1e-6:
        break
    cum += B_n_minus[i]
    frac = cum / max(sum_P, 1e-30)
    n_dominant_P += 1
    dominant_P_indices.append(i)
    if n_dominant_P <= 30:
        print(f"  {i:5d}  {omega_n[i]:12.6f}  {B_n_minus[i]:16.10f}  {frac:10.6f}")

print(f"  Total dominant transitions: {n_dominant_P}")

# ======================================================================
#  Step 4: Also compute mode-resolved pair creation operators
# ======================================================================

print(f"\nMode-resolved pair creation matrix elements:")
print(f"  These show which modes contribute to each pole.")

# For each mode k, compute b_k^dag|psi_gs> and its matrix elements
mode_Bplus = np.zeros((n_modes, n_states))  # |<n|b_k^dag|0>|^2 for each k, n
for k in range(n_modes):
    bk_dag_psi = np.zeros(n_states)
    for state in range(n_states):
        amp = psi_gs[state]
        if abs(amp) < 1e-16:
            continue
        if not (state & (1 << k)):
            new_state = state | (1 << k)
            bk_dag_psi[new_state] += amp
    # Project onto eigenstates
    mode_Bplus[k, :] = np.abs(psi_all.T @ bk_dag_psi)**2

# Check: Sum_k mode_Bplus[k, n] should equal B_n_plus[n] (not exactly due to cross terms)
# Actually P^dag = Sum_k b_k^dag, so <n|P^dag|0> = Sum_k <n|b_k^dag|0>
# and |<n|P^dag|0>|^2 = |Sum_k <n|b_k^dag|0>|^2 != Sum_k |<n|b_k^dag|0>|^2 in general
# But we can decompose the strength into mode contributions

# Let me also compute the coherent vs incoherent decomposition
# <n|P^dag|0> = Sum_k <n|b_k^dag|0>, so the mode amplitudes are complex in general
mode_amp = np.zeros((n_modes, n_states))  # <n|b_k^dag|0> (real since H is real)
for k in range(n_modes):
    bk_dag_psi = np.zeros(n_states)
    for state in range(n_states):
        amp = psi_gs[state]
        if abs(amp) < 1e-16:
            continue
        if not (state & (1 << k)):
            new_state = state | (1 << k)
            bk_dag_psi[new_state] += amp
    mode_amp[k, :] = psi_all.T @ bk_dag_psi

# Coherent sum: |Sum_k A_k|^2 vs incoherent: Sum_k |A_k|^2
coherent = np.abs(np.sum(mode_amp, axis=0))**2  # = B_n_plus
incoherent = np.sum(np.abs(mode_amp)**2, axis=0)

# Check
print(f"  Coherent vs incoherent check:")
print(f"    max|coherent - B_n_plus| = {np.max(np.abs(coherent - B_n_plus)):.2e}")
print(f"    Total coherent   = {np.sum(coherent):.6f}")
print(f"    Total incoherent = {np.sum(incoherent):.6f}")
print(f"    Enhancement factor (coherent/incoherent) for dominant poles:")

for i in dominant_Pdag_indices[:10]:
    if incoherent[i] > 1e-10:
        ratio = coherent[i] / incoherent[i]
        print(f"      n={i:3d}: omega={omega_n[i]:.6f}, "
              f"coh={coherent[i]:.6f}, incoh={incoherent[i]:.6f}, "
              f"ratio={ratio:.4f}")
        # Mode decomposition
        for k in range(n_modes):
            if mode_Bplus[k, i] > 1e-6:
                print(f"        mode {k} ({branch_labels[k]}): "
                      f"|<n|b_k^dag|0>|^2 = {mode_Bplus[k,i]:.6f}, "
                      f"<n|b_k^dag|0> = {mode_amp[k,i]:.6f}")

# ======================================================================
#  Step 5: Number-sector analysis of transitions
# ======================================================================

print(f"\nNumber-sector analysis:")
# Ground state is in N_pair=1 sector (from ED-CONV-36)
# P^dag adds one pair: N_pair=1 -> N_pair=2 transitions
# P removes one pair: N_pair=1 -> N_pair=0 transitions

# Count pair number for each eigenstate
n_pairs_of_state = np.zeros(n_states, dtype=int)
for state in range(n_states):
    n_pairs_of_state[state] = bin(state).count('1')

# For each eigenstate, determine its dominant number sector
eigenstate_npair = np.zeros(len(E_all), dtype=int)
for n_idx in range(len(E_all)):
    psi_n = psi_all[:, n_idx]
    sector_prob = np.zeros(n_modes + 1)
    for state in range(n_states):
        sector_prob[n_pairs_of_state[state]] += abs(psi_n[state])**2
    eigenstate_npair[n_idx] = np.argmax(sector_prob)

print(f"  Ground state dominant sector: N_pair = {eigenstate_npair[0]}")
print(f"  P^dag transitions go to N_pair = {eigenstate_npair[0]+1} sector")
print(f"  P transitions go to N_pair = {eigenstate_npair[0]-1} sector")

# Verify: all P^dag matrix elements should connect to N+1 sector
for i in dominant_Pdag_indices[:5]:
    print(f"    State {i}: N_pair = {eigenstate_npair[i]}, "
          f"omega = {omega_n[i]:.6f}, B+ = {B_n_plus[i]:.6f}")

for i in dominant_P_indices[:5]:
    print(f"    State {i} (P): N_pair = {eigenstate_npair[i]}, "
          f"omega = {omega_n[i]:.6f}, B- = {B_n_minus[i]:.6f}")

# ======================================================================
#  Step 6: Compute dynamical pair susceptibility chi_pair(omega)
# ======================================================================

print(f"\nComputing chi_pair(omega)...")

# Frequency grid
omega_max = 2.0
n_omega = 4000
omega_grid = np.linspace(0.001, omega_max, n_omega)

# Broadening parameter scan
eta_values = [0.001, 0.005, 0.01, 0.02, 0.05]
chi_results = {}

for eta in eta_values:
    chi_pair = np.zeros(n_omega, dtype=complex)
    for n_idx in range(len(E_all)):
        if omega_n[n_idx] < 1e-12 and B_n_plus[n_idx] < 1e-12:
            continue  # Skip ground state self-transition
        # Retarded part: B+/(omega - omega_n + i*eta)
        if B_n_plus[n_idx] > 1e-15:
            chi_pair += B_n_plus[n_idx] / (omega_grid - omega_n[n_idx] + 1j*eta)
        # Advanced part: -B-/(omega + omega_n + i*eta)
        if B_n_minus[n_idx] > 1e-15:
            chi_pair -= B_n_minus[n_idx] / (omega_grid + omega_n[n_idx] + 1j*eta)

    chi_results[eta] = chi_pair

# Use eta = 0.01 as primary
eta_primary = 0.01
chi_primary = chi_results[eta_primary]
Im_chi = np.imag(chi_primary)
Re_chi = np.real(chi_primary)

print(f"  eta = {eta_primary}")
print(f"  max |Im chi| = {np.max(np.abs(Im_chi)):.6f}")
print(f"  max |Re chi| = {np.max(np.abs(Re_chi)):.6f}")

# ======================================================================
#  Step 7: Identify discrete poles vs continuum
# ======================================================================

print(f"\nPole vs continuum decomposition:")

# The effective pairing gap Delta_eff from ED
# From config_4, Delta_eff is very small (number-conserving => <b_m> ~ 0)
# The PHYSICAL pair-breaking threshold is the minimum excitation energy
# to create a N+1 pair state minus the GS energy

# For pair-ADDITION channel (P^dag): threshold = min(omega_n) for states
# with nonzero B_n_plus

# Sort poles by weight
pole_data = []
for n_idx in range(len(E_all)):
    if B_n_plus[n_idx] > 1e-10:
        pole_data.append({
            'index': n_idx,
            'omega': omega_n[n_idx],
            'weight_plus': B_n_plus[n_idx],
            'weight_minus': B_n_minus[n_idx],
            'npair': eigenstate_npair[n_idx],
        })

pole_data.sort(key=lambda x: -x['weight_plus'])

print(f"\n  All significant poles (P^dag channel):")
print(f"  {'rank':>4s}  {'n':>5s}  {'omega_n':>10s}  {'B+':>12s}  {'N_pair':>6s}")
total_strength = sum(p['weight_plus'] for p in pole_data)
for rank, p in enumerate(pole_data[:30]):
    frac = p['weight_plus'] / total_strength
    print(f"  {rank:4d}  {p['index']:5d}  {p['omega']:10.6f}  "
          f"{p['weight_plus']:12.6f}  {p['npair']:6d}  ({frac*100:.2f}%)")

# Define "pole" vs "continuum" boundary
# In a finite system, everything is discrete. The relevant distinction is:
# - Collective poles: enhanced by coherent superposition (giant resonance analog)
# - Non-collective: single-pair excitations with small weight

# Method 1: Use a strength threshold
# A pole is "collective" if its weight exceeds 1/N_eff of the total
N_eff_modes = 8
threshold_collective = total_strength / (10 * N_eff_modes)  # 1/(10*N)

collective_strength = 0.0
non_collective_strength = 0.0
n_collective = 0
n_non_collective = 0

for p in pole_data:
    if p['weight_plus'] > threshold_collective:
        collective_strength += p['weight_plus']
        n_collective += 1
    else:
        non_collective_strength += p['weight_plus']
        n_non_collective += 1

print(f"\n  Collective vs non-collective decomposition (threshold = {threshold_collective:.6f}):")
print(f"    Collective poles:     {n_collective}, strength = {collective_strength:.6f}")
print(f"    Non-collective poles: {n_non_collective}, strength = {non_collective_strength:.6f}")
print(f"    Ratio (collective/total) = {collective_strength/total_strength:.6f}")

# Method 2: Energy-based decomposition
# The pair-breaking continuum threshold: minimum energy to scatter a pair
# from the ground state to an unpaired excited state
# For our N_pair=1 ground state:
#   - P^dag|0> goes to N_pair=2: threshold = 2*min(xi) for two pairs
#   - P|0> goes to N_pair=0: threshold = 0 (vacuum)

# Actually, the relevant physics: the spectral gap in Im chi
# Below some energy, there's a discrete pole (pair vibration)
# Above it, there's a quasi-continuum of pair-breaking excitations

# Find the first significant gap in the excitation spectrum
pole_omegas = sorted([p['omega'] for p in pole_data if p['weight_plus'] > 1e-6])
print(f"\n  Pole positions (sorted):")
for i, om in enumerate(pole_omegas[:20]):
    print(f"    omega[{i}] = {om:.6f}")

# Pair-vibrational vs pair-breaking: in nuclear physics, the pair vibration
# is the lowest 0+ excitation in the N+2 system. The pair-breaking continuum
# starts at 2*Delta.
# Here: the lowest P^dag excitation is the analog of the pair vibration.

# Since Delta_eff ~ 0 (number-conserving ED), use the actual spectral gap
# The relevant gap is the first excitation energy with significant P^dag weight
first_excitation = pole_omegas[0] if len(pole_omegas) > 0 else 0.0
print(f"\n  First P^dag excitation: omega_1 = {first_excitation:.6f}")

# For the pole/continuum split, use the ED spectrum structure:
# The "pole" is the lowest collective pair-vibrational mode
# Everything above the first dense cluster is "continuum"

# Define pair-breaking threshold from xi values
# 2*min(|xi|) = threshold for creating a pair excitation
xi_min = np.min(np.abs(xi))
pair_break_threshold = 2.0 * xi_min
print(f"  2*min(|xi|) = {pair_break_threshold:.6f} (pair-breaking threshold)")

# Alternative: the MF BCS gap Delta_MF
# From ED, the effective gap comes from the excitation spectrum
# The energy gap between GS and first excited state
gap_ED = omega_n[1]  # First excited state excitation energy
print(f"  ED spectral gap (E_1 - E_0) = {gap_ED:.6f}")

# Use the spectral gap as the threshold between "virtual" and "real"
# Below gap_ED: strictly virtual (zero spectral weight in Im chi at eta->0)
# The pair-vibrational pole at omega_1 has omega_1 > gap_ED

# Actually, for the Lehmann spectral function, ALL poles are discrete in
# finite ED. The "virtual" regime is below 2*Delta_BCS.
# With number conservation, Delta_BCS is not directly accessible.
# Use the condensation energy as a proxy: 2*Delta ~ 2*sqrt(|E_cond|*delta_xi)
# where delta_xi is the level spacing at the Fermi surface.

# From the B2 quartet: xi = 0.845 (degenerate), delta_xi ~ 0
# The pair-vibrational energy is better estimated from the spectrum directly.

# Key physics: in this N_pair=1 system, the pair vibration is the
# redistribution of the pair among modes (no pair creation/destruction
# of the condensate). P^dag creates a SECOND pair (N_pair=2 state).

# Define the boundary between "pole" (pair-vibrational, below-threshold)
# and "continuum" (pair-breaking, high-energy) based on spectral clustering

# ======================================================================
#  Step 8: Kramers-Kronig-consistent pair gap definition
# ======================================================================

# For the vacuum polarization energy, we need the spectral weight below
# the pair-breaking threshold. Since we're in a finite system, define:
#
# "Virtual" regime: below the first pair-breaking excitation
# In nuclear physics: omega < 2*Delta
#
# Here the relevant scale is:
# - The pairing gap from odd-even staggering: Delta_OES ~ |E_cond|/N_pair
# - Or from the pair-addition/removal spectrum

# The pair-addition spectrum (P^dag transitions from N=1 ground state):
# These go to N=2 states. The lowest N=2 state energy is E_2_min.
# The pair-removal spectrum (P transitions from N=1 ground state):
# These go to N=0 (vacuum). The vacuum energy is 0.
# So the pair-removal energy is omega = E_0 - E_vac = |E_gs| = 0.137

# For pair addition: omega = E(N=2) - E(N=1) = E(N=2) + 0.137

# The pair-breaking threshold in this language:
# If the pair-vibrational mode exhausts most of the strength below
# some energy omega_c, and the remaining strength is spread above,
# then omega_c separates "pole" from "continuum".

# Practical: use the spectral gap in the B_n_plus distribution

# ======================================================================
#  Step 9: Compute E_vac using different threshold definitions
# ======================================================================

print(f"\n{'='*78}")
print(f"VACUUM POLARIZATION ENERGY")
print(f"{'='*78}")

# Method A: Direct pole sum for the lowest pair-vibrational mode
# E_vac = -(1/2) * Sum_{n: omega_n < omega_c} B_n_plus * omega_n
# This is the discrete analog of the spectral integral

# First, let's understand the pole structure by computing cumulative
# strength as a function of energy

n_energy_bins = 200
energy_edges = np.linspace(0, omega_max, n_energy_bins + 1)
strength_hist = np.zeros(n_energy_bins)
for p in pole_data:
    idx = np.searchsorted(energy_edges, p['omega']) - 1
    if 0 <= idx < n_energy_bins:
        strength_hist[idx] += p['weight_plus']

cumulative_strength = np.cumsum(strength_hist)
energy_centers = 0.5 * (energy_edges[:-1] + energy_edges[1:])

# Find where 50%, 90% of strength is accumulated
for target_frac in [0.50, 0.75, 0.90, 0.95, 0.99]:
    idx = np.searchsorted(cumulative_strength, target_frac * total_strength)
    if idx < len(energy_centers):
        print(f"  {target_frac*100:.0f}% of P^dag strength below omega = {energy_centers[idx]:.4f}")

# Method B: Spectral integral of Im chi
# E_vac = -(1/2pi) * integral Im chi(omega) * omega d(omega) from 0 to omega_c

# For the full range (all virtual + real):
# This gives the energy-weighted sum rule:
# (1/pi) * int_0^inf Im chi(omega) * omega d(omega) = <0|[P, [H, P^dag]]|0>

# Double commutator sum rule
# [H, P^dag] = Sum_k [H, b_k^dag] = Sum_k 2*xi_k * b_k^dag - ...
# This is the energy-weighted sum rule m_1

# Compute m_1 from the poles directly
m1_poles = np.sum(B_n_plus * omega_n) - np.sum(B_n_minus * omega_n)
m0_poles = np.sum(B_n_plus) - np.sum(B_n_minus)  # Should relate to <N>

print(f"\n  Sum rules:")
print(f"    m_0 = Sum B+ - Sum B- = {m0_poles:.10f}")
print(f"    m_1 = Sum B+*omega - Sum B-*omega = {m1_poles:.10f}")

# E_vac computation with different cutoffs
# Nuclear standard: use 2*Delta as cutoff
# Here: use several physically-motivated cutoffs

# Define "pair gap" from the pair addition/removal asymmetry:
# omega_pair_vib = lowest P^dag pole with significant strength
omega_pair_vib = pole_omegas[0]
print(f"\n  Pair-vibrational energy: omega_PV = {omega_pair_vib:.6f}")

# Cutoff options:
cutoffs = {
    'PV_only': omega_pair_vib + 0.01,  # Just the pair vibration
    '2E_cond': 2 * abs(E_cond_stored),  # 2 * condensation energy
    'first_gap': gap_ED + 0.01,         # Below first ED gap
    'half_strength': None,              # Will find 50% point
}

# Find 50% strength energy
idx_50 = np.searchsorted(cumulative_strength, 0.5 * total_strength)
if idx_50 < len(energy_centers):
    cutoffs['half_strength'] = energy_centers[idx_50]

print(f"\n  Cutoff energies:")
for name, omega_c in cutoffs.items():
    if omega_c is not None:
        print(f"    {name}: omega_c = {omega_c:.6f}")

# Compute E_vac for each cutoff
# NORMALIZATION: From the Lehmann representation,
# Im chi(omega > 0) = -pi * Sum_n B_n_plus * delta(omega - omega_n)
# E_vac = -(1/(2*pi)) * integral_0^{omega_c} Im_chi(omega) * omega d(omega)
#       = -(1/(2*pi)) * Sum_{omega_n < omega_c} (-pi * B_n * omega_n)
#       = +(1/2) * Sum_{omega_n < omega_c} B_n_plus * omega_n
# The pi from the delta function cancels the 1/(2*pi) prefactor.
# E_vac is POSITIVE (energy of virtual pair fluctuations).

print(f"\n  Vacuum polarization energy:")
print(f"  Convention: E_vac = (1/2) * Sum B_n * omega_n [discrete, pi canceled]")
E_vac_results = {}
for name, omega_c in cutoffs.items():
    if omega_c is None:
        continue
    # Discrete pole sum: E_vac = (1/2) * Sum B_n * omega_n for omega_n < omega_c
    E_vac_discrete = 0.0
    n_poles_below = 0
    for p in pole_data:
        if p['omega'] < omega_c and p['omega'] > 1e-10:
            E_vac_discrete += 0.5 * p['weight_plus'] * p['omega']
            n_poles_below += 1

    # Also from Im chi integral (broadened):
    # -(1/(2*pi)) * integral Im_chi * omega d(omega)
    mask = (omega_grid < omega_c)
    E_vac_integral = -0.5 * np.trapezoid(Im_chi[mask] * omega_grid[mask],
                                       omega_grid[mask]) / np.pi

    E_vac_results[name] = {
        'omega_c': omega_c,
        'E_vac_discrete': E_vac_discrete,
        'E_vac_integral': E_vac_integral,
        'n_poles': n_poles_below,
    }

    ratio = abs(E_vac_discrete) / abs(E_cond_stored) if abs(E_cond_stored) > 0 else 0.0
    print(f"    {name}: E_vac = {E_vac_discrete:.6f}, |E_vac|/|E_cond| = {ratio:.6f}, "
          f"n_poles = {n_poles_below}, E_vac_integral = {E_vac_integral:.6f}")

# Full spectral integral (all poles)
E_vac_full_discrete = 0.5 * np.sum(B_n_plus * omega_n)
E_vac_full_integral = -0.5 * np.trapezoid(Im_chi * omega_grid, omega_grid) / np.pi
print(f"    FULL: E_vac_discrete = {E_vac_full_discrete:.6f}, "
      f"|E_vac|/|E_cond| = {abs(E_vac_full_discrete)/abs(E_cond_stored):.6f}")

# ======================================================================
#  Step 10: Physical BCS gap estimate from pair spectrum
# ======================================================================

print(f"\n{'='*78}")
print(f"BCS GAP ESTIMATES FROM PAIR SPECTRUM")
print(f"{'='*78}")

# Method 1: From pair addition/removal energies
# omega+(N+1) = E(N+1, lowest) - E(N, GS)
# omega-(N-1) = E(N, GS) - E(N-1, lowest)
# Delta = (omega+ + omega-) / 2

# P^dag: N=1 -> N=2. Lowest N=2 state energy:
N2_mask = (eigenstate_npair == 2)
N0_mask = (eigenstate_npair == 0)

if np.any(N2_mask):
    E_N2_min = np.min(E_all[N2_mask])
    omega_plus = E_N2_min - E_gs
    print(f"  omega+ (lowest N=2 excitation) = {omega_plus:.6f}")
else:
    omega_plus = None
    print(f"  No N=2 states found (unexpected)")

if np.any(N0_mask):
    E_N0_min = np.min(E_all[N0_mask])
    omega_minus = E_gs - E_N0_min  # This should be negative (vacuum is higher)
    # Actually: omega- = E(N=0, lowest) - E(N=1, GS) = 0 - E_gs = |E_gs|
    omega_minus_correct = E_N0_min - E_gs
    print(f"  omega- (lowest N=0 excitation) = {omega_minus_correct:.6f}")
    print(f"  E(N=0, lowest) = {E_N0_min:.6f}")
else:
    omega_minus_correct = None

if omega_plus is not None and omega_minus_correct is not None:
    Delta_pair = (omega_plus + omega_minus_correct) / 2.0
    print(f"  Delta_pair = (omega+ + omega-)/2 = {Delta_pair:.6f}")
    two_Delta = omega_plus + omega_minus_correct
    print(f"  2*Delta_pair = {two_Delta:.6f}")

    # Also the odd-even mass difference formula
    # Delta_OES = (-1)^N * [E(N+1) + E(N-1) - 2*E(N)] / 2
    # For N=1: Delta_OES = [E(2) + E(0) - 2*E(1)] / 2
    Delta_OES = (E_N2_min + E_N0_min - 2*E_gs) / 2.0
    print(f"  Delta_OES = [E(N=2) + E(N=0) - 2*E(N=1)] / 2 = {Delta_OES:.6f}")
else:
    Delta_pair = None
    Delta_OES = None

# ======================================================================
#  Step 11: Pole/continuum ratio (F.2 gate)
# ======================================================================

print(f"\n{'='*78}")
print(f"F.2 GATE: POLE/CONTINUUM RATIO")
print(f"{'='*78}")

# In nuclear physics, the pole/continuum decomposition of the pair
# vibrational strength uses the pair-breaking threshold 2*Delta.
# Below 2*Delta: collective pair vibration (pole)
# Above 2*Delta: pair-breaking continuum

# For this system with N_pair=1, the relevant decomposition:
# - The LOWEST P^dag pole is the pair vibration (adds a second pair)
# - Higher poles are pair-breaking (the added pair excites internal modes)

# Define "pole" as the lowest cluster, "continuum" as everything else
# Natural separation: the gap in the excitation spectrum

# Find the largest gap in the pole positions
if len(pole_omegas) > 1:
    gaps = np.diff(pole_omegas)
    max_gap_idx = np.argmax(gaps)
    omega_split = 0.5 * (pole_omegas[max_gap_idx] + pole_omegas[max_gap_idx + 1])
    print(f"  Largest spectral gap at omega ~ {omega_split:.4f}")
    print(f"    Between poles at {pole_omegas[max_gap_idx]:.4f} and "
          f"{pole_omegas[max_gap_idx+1]:.4f}")
    print(f"    Gap width = {gaps[max_gap_idx]:.4f}")

# Pole strength: lowest 1 or 2 transitions
pole_strength = 0.0
continuum_strength = 0.0

# Use energy cutoff: below the first gap in the spectrum
# The first excitation is omega[1] = 0.137 (gap between GS and vacuum)
# But for P^dag channel, the relevant poles are at their own energies

# Simple decomposition: first pole vs rest
if len(pole_data) > 0:
    first_pole_strength = pole_data[0]['weight_plus']
    rest_strength = sum(p['weight_plus'] for p in pole_data[1:])

    ratio_first_vs_rest = first_pole_strength / (first_pole_strength + rest_strength)
    print(f"\n  First-pole / total ratio = {ratio_first_vs_rest:.6f}")
    print(f"    First pole: omega = {pole_data[0]['omega']:.6f}, "
          f"B+ = {first_pole_strength:.6f}")

# Also: lowest 2 poles vs rest
if len(pole_data) > 1:
    low2_strength = pole_data[0]['weight_plus'] + pole_data[1]['weight_plus']
    rest2_strength = sum(p['weight_plus'] for p in pole_data[2:])
    ratio_low2_vs_total = low2_strength / (low2_strength + rest2_strength)
    print(f"  (Lowest 2) / total ratio = {ratio_low2_vs_total:.6f}")

# Use the natural energy threshold from the spectral gap
if omega_split is not None:
    pole_below = sum(p['weight_plus'] for p in pole_data if p['omega'] < omega_split)
    cont_above = sum(p['weight_plus'] for p in pole_data if p['omega'] >= omega_split)
    if (pole_below + cont_above) > 0:
        ratio_gap_split = pole_below / (pole_below + cont_above)
    else:
        ratio_gap_split = 0.0
    print(f"\n  Gap-based split (omega_c = {omega_split:.4f}):")
    print(f"    Pole strength (below) = {pole_below:.6f}")
    print(f"    Continuum strength (above) = {cont_above:.6f}")
    print(f"    Pole / total = {ratio_gap_split:.6f}")

# The DEFINITIVE pole/continuum ratio:
# Use Delta_OES-based threshold if available
if Delta_OES is not None:
    two_Delta_OES = 2 * Delta_OES
    pole_below_OES = sum(p['weight_plus'] for p in pole_data
                         if p['omega'] < two_Delta_OES)
    cont_above_OES = sum(p['weight_plus'] for p in pole_data
                         if p['omega'] >= two_Delta_OES)
    if (pole_below_OES + cont_above_OES) > 0:
        ratio_OES = pole_below_OES / (pole_below_OES + cont_above_OES)
    else:
        ratio_OES = 0.0
    print(f"\n  OES-based split (2*Delta_OES = {two_Delta_OES:.4f}):")
    print(f"    Pole strength (below) = {pole_below_OES:.6f}")
    print(f"    Continuum strength (above) = {cont_above_OES:.6f}")
    print(f"    Pole / total = {ratio_OES:.6f}")

# Report the primary ratio
# Use the gap-based split as the canonical answer
primary_ratio = ratio_gap_split if omega_split is not None else ratio_first_vs_rest
print(f"\n  *** F.2 PRIMARY RATIO (pole/total) = {primary_ratio:.6f} ***")
print(f"  Nuclear benchmark: 0.3-0.7 (mid-shell), >0.9 (near closures)")
if primary_ratio > 0.9:
    print(f"  --> NEAR CLOSURE REGIME (concentrated in few poles)")
elif 0.3 <= primary_ratio <= 0.7:
    print(f"  --> MID-SHELL REGIME (distributed between pole and continuum)")
elif primary_ratio < 0.3:
    print(f"  --> HIGHLY FRAGMENTED (collective pole carries < 30% of strength)")

# ======================================================================
#  Step 12: F.3 Gate: |E_vac|/|E_cond| ratio
# ======================================================================

print(f"\n{'='*78}")
print(f"F.3 GATE: |E_vac|/|E_cond| RATIO")
print(f"{'='*78}")

# Use the physically-motivated cutoff: 2*Delta_OES
if Delta_OES is not None:
    omega_c_vac = 2 * Delta_OES
    label_vac = f"2*Delta_OES = {omega_c_vac:.4f}"
else:
    omega_c_vac = omega_split if omega_split else omega_pair_vib + 0.01
    label_vac = f"gap-based = {omega_c_vac:.4f}"

# E_vac = (1/2) * Sum B_n_plus * omega_n for poles below cutoff
# (pi from delta function cancels the 1/(2*pi) prefactor)
E_vac_final = 0.0
for p in pole_data:
    if p['omega'] < omega_c_vac and p['omega'] > 1e-10:
        E_vac_final += 0.5 * p['weight_plus'] * p['omega']

ratio_vac = abs(E_vac_final) / abs(E_cond_stored)

print(f"  Cutoff: {label_vac}")
print(f"  E_vac = {E_vac_final:.10f}")
print(f"  E_cond = {E_cond_stored:.10f}")
print(f"  |E_vac| / |E_cond| = {ratio_vac:.6f}")
print(f"  Nuclear benchmark: 0.05-0.15")
if ratio_vac > 0.1:
    print(f"  --> SIGNIFICANT virtual pair contribution")
elif 0.05 <= ratio_vac <= 0.1:
    print(f"  --> MODERATE virtual pair contribution (within nuclear range)")
elif ratio_vac < 0.05:
    print(f"  --> WEAK virtual pair contribution (below nuclear benchmark)")

# Also compute E_vac with other cutoffs for comparison
print(f"\n  E_vac sensitivity to cutoff:")
for omega_c_test in [0.5, 1.0, 1.5, 2.0, 3.0, 5.0]:
    E_vac_test = 0.0
    for p in pole_data:
        if p['omega'] < omega_c_test and p['omega'] > 1e-10:
            E_vac_test += 0.5 * p['weight_plus'] * p['omega']
    r_test = abs(E_vac_test) / abs(E_cond_stored)
    print(f"    omega_c = {omega_c_test:.1f}: E_vac = {E_vac_test:.6f}, "
          f"|E_vac|/|E_cond| = {r_test:.6f}")

# ======================================================================
#  Step 13: Cumulative E_vac(omega) for plotting
# ======================================================================

# Compute cumulative E_vac as a function of cutoff energy
# E_vac(omega_c) = (1/2) * Sum_{omega_n < omega_c} B_n * omega_n
n_cum = 500
omega_cum = np.linspace(0, omega_max, n_cum)
E_vac_cumulative = np.zeros(n_cum)

for i, om_c in enumerate(omega_cum):
    for p in pole_data:
        if p['omega'] < om_c and p['omega'] > 1e-10:
            E_vac_cumulative[i] += 0.5 * p['weight_plus'] * p['omega']

# Also compute from Im chi integral
E_vac_integral_cum = np.zeros(n_omega)
for i in range(1, n_omega):
    E_vac_integral_cum[i] = E_vac_integral_cum[i-1] + \
        (-0.5 / np.pi) * Im_chi[i] * omega_grid[i] * (omega_grid[1] - omega_grid[0])

# ======================================================================
#  Step 14: SAVE
# ======================================================================

print(f"\n{'='*78}")
print(f"SAVING RESULTS")
print(f"{'='*78}")

save_dict = {
    # Raw data
    'V_8x8': V_8x8,
    'E_8': E_8,
    'rho': rho,
    'mu': mu,
    'n_modes': n_modes,
    'n_states': n_states,
    'branch_labels': np.array(branch_labels),

    # Full spectrum
    'E_all': E_all,
    'E_gs': E_gs,
    'E_cond': E_cond_stored,
    'omega_n': omega_n,

    # Matrix elements
    'B_n_plus': B_n_plus,
    'B_n_minus': B_n_minus,
    'sum_Pdag': sum_Pdag,
    'sum_P': sum_P,

    # Mode-resolved
    'mode_Bplus': mode_Bplus,
    'mode_amp': mode_amp,
    'coherent': coherent,
    'incoherent': incoherent,

    # Number-sector
    'eigenstate_npair': eigenstate_npair,

    # Chi pair
    'omega_grid': omega_grid,
    'Im_chi': Im_chi,
    'Re_chi': Re_chi,
    'eta_primary': eta_primary,

    # Chi at multiple eta
    'eta_values': np.array(eta_values),
    'Im_chi_multi_eta': np.array([np.imag(chi_results[e]) for e in eta_values]),

    # Pair gap estimates
    'omega_plus': omega_plus if omega_plus is not None else np.nan,
    'omega_minus': omega_minus_correct if omega_minus_correct is not None else np.nan,
    'Delta_pair': Delta_pair if Delta_pair is not None else np.nan,
    'Delta_OES': Delta_OES if Delta_OES is not None else np.nan,

    # F.2 gate: pole/continuum
    'primary_ratio_pole_continuum': primary_ratio,
    'ratio_first_pole': ratio_first_vs_rest,
    'omega_split': omega_split if omega_split is not None else np.nan,

    # F.3 gate: E_vac
    'E_vac_final': E_vac_final,
    'ratio_Evac_Econd': ratio_vac,
    'E_vac_cutoff': omega_c_vac,
    'E_vac_full': E_vac_full_discrete,

    # Cumulative
    'omega_cum': omega_cum,
    'E_vac_cumulative': E_vac_cumulative,

    # Sum rules
    'm0_poles': m0_poles,
    'm1_poles': m1_poles,
}

out_npz = os.path.join(SCRIPT_DIR, 's37_pair_susceptibility.npz')
np.savez_compressed(out_npz, **save_dict)
print(f"Saved: {out_npz}")
print(f"  Size: {os.path.getsize(out_npz) / 1024:.1f} KB")

# ======================================================================
#  Step 15: PLOT
# ======================================================================

print(f"\nGenerating plots...")

fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Panel (a): Im chi_pair(omega)
ax = axes[0, 0]
for eta_val in [0.005, 0.01, 0.02, 0.05]:
    Im_chi_eta = np.imag(chi_results[eta_val])
    ax.plot(omega_grid, Im_chi_eta, lw=1.5, alpha=0.7,
            label=f'eta={eta_val}')

# Mark pole positions
for p in pole_data[:10]:
    ax.axvline(p['omega'], color='gray', ls=':', alpha=0.3, lw=0.5)

# Mark thresholds
if Delta_OES is not None:
    ax.axvline(2*Delta_OES, color='red', ls='--', lw=1.5,
               label=f'2*Delta_OES={2*Delta_OES:.3f}')
if omega_split is not None:
    ax.axvline(omega_split, color='green', ls='-.', lw=1.5,
               label=f'Spectral gap={omega_split:.3f}')

ax.set_xlabel('omega')
ax.set_ylabel('Im chi_pair(omega)')
ax.set_title('(a) Pair Spectral Function')
ax.legend(fontsize=7, loc='upper right')
ax.grid(True, alpha=0.3)
ax.set_xlim(0, omega_max)

# Panel (b): Re chi_pair(omega)
ax = axes[0, 1]
ax.plot(omega_grid, Re_chi, 'b-', lw=1.5, label=f'eta={eta_primary}')
ax.axhline(0, color='black', ls='-', lw=0.5)

if Delta_OES is not None:
    ax.axvline(2*Delta_OES, color='red', ls='--', lw=1.5,
               label=f'2*Delta_OES={2*Delta_OES:.3f}')

ax.set_xlabel('omega')
ax.set_ylabel('Re chi_pair(omega)')
ax.set_title('(b) Real Part of Pair Susceptibility')
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)
ax.set_xlim(0, omega_max)

# Panel (c): Pole decomposition (discrete spectrum)
ax = axes[1, 0]
# Bar plot of B_n_plus vs omega_n
for p in pole_data:
    color = 'steelblue' if p['omega'] < (omega_split if omega_split else 1e10) else 'coral'
    ax.bar(p['omega'], p['weight_plus'], width=0.015, color=color,
           alpha=0.7, edgecolor='black', linewidth=0.3)

if omega_split is not None:
    ax.axvline(omega_split, color='green', ls='-.', lw=2,
               label=f'Pole/cont. split = {omega_split:.3f}')
    ax.fill_betweenx([0, ax.get_ylim()[1] if ax.get_ylim()[1] > 0 else 1],
                     0, omega_split, color='lightblue', alpha=0.2,
                     label=f'Pole region ({primary_ratio*100:.1f}%)')

ax.set_xlabel('omega_n')
ax.set_ylabel('|<n|P^dag|0>|^2')
ax.set_title(f'(c) Pole Decomposition (pole/total = {primary_ratio:.3f})')
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)
ax.set_xlim(0, omega_max)

# Panel (d): Cumulative E_vac(omega)
ax = axes[1, 1]
ax.plot(omega_cum, E_vac_cumulative, 'b-', lw=2, label='E_vac(omega_c)')
ax.axhline(E_vac_final, color='red', ls='--', lw=1.5,
           label=f'E_vac = {E_vac_final:.4f}')
ax.axhline(abs(E_cond_stored), color='purple', ls=':', lw=1.5,
           label=f'|E_cond| = {abs(E_cond_stored):.4f}')

if Delta_OES is not None:
    ax.axvline(2*Delta_OES, color='red', ls='--', lw=1, alpha=0.5)

ax.set_xlabel('omega_c (cutoff energy)')
ax.set_ylabel('E_vac (cumulative)')
ax.set_title(f'(d) Vacuum Polarization Energy (|E_vac|/|E_cond| = {ratio_vac:.4f})')
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)

# Add text box with key results
textstr = (f'F.2: Pole/total = {primary_ratio:.4f}\n'
           f'F.3: |E_vac|/|E_cond| = {ratio_vac:.4f}\n'
           f'Delta_OES = {Delta_OES:.4f}\n'
           f'E_cond = {E_cond_stored:.4f}')
ax.text(0.98, 0.02, textstr, transform=ax.transAxes, fontsize=8,
        verticalalignment='bottom', horizontalalignment='right',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

fig.suptitle('F.2 + F.3: Pair Susceptibility and Vacuum Polarization\n'
             f'8-mode ED (256 states), eta={eta_primary}',
             fontsize=13, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.94])
out_png = os.path.join(SCRIPT_DIR, 's37_pair_susceptibility.png')
plt.savefig(out_png, dpi=150)
plt.close()
print(f"Plot saved: {out_png}")

# ======================================================================
#  FINAL SUMMARY
# ======================================================================

elapsed = time.time() - t0
print(f"\n{'='*78}")
print(f"FINAL SUMMARY: F.2 + F.3")
print(f"{'='*78}")
print(f"\n  Physical regime: N_pair = 1 (single Cooper pair)")
print(f"  Pair-vibrational energy: omega_PV = {omega_pair_vib:.6f}")
print(f"  OES gap: Delta_OES = {Delta_OES:.6f}")
print(f"  Pair-breaking threshold: 2*Delta_OES = {2*Delta_OES:.6f}")
print(f"\n  F.2: Pair susceptibility pole structure")
print(f"    Total P^dag strength = {total_strength:.6f}")
print(f"    Number of significant poles = {len(pole_data)}")
print(f"    Pole/total ratio = {primary_ratio:.6f}")
print(f"    First pole strength = {pole_data[0]['weight_plus']:.6f} "
      f"({pole_data[0]['weight_plus']/total_strength*100:.1f}%)")
print(f"\n  F.3: Vacuum polarization energy")
print(f"    E_vac = {E_vac_final:.10f}")
print(f"    |E_vac|/|E_cond| = {ratio_vac:.6f}")
print(f"    Nuclear benchmark: 0.05-0.15")
print(f"\n  Sum rules:")
print(f"    m_0 = {m0_poles:.6f}")
print(f"    m_1 = {m1_poles:.6f}")
print(f"\n  Mode coherence (first pole):")
coh_ratio = coherent[pole_data[0]['index']] / max(incoherent[pole_data[0]['index']], 1e-30)
print(f"    Coherent/incoherent = {coh_ratio:.4f}")
if coh_ratio > 1.5:
    print(f"    --> CONSTRUCTIVE COHERENCE (giant resonance analog)")
elif coh_ratio < 0.5:
    print(f"    --> DESTRUCTIVE INTERFERENCE")
else:
    print(f"    --> NEAR-INCOHERENT SUPERPOSITION")
print(f"\n  Runtime: {elapsed:.1f}s")
print(f"{'='*78}")
