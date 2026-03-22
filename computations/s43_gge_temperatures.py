#!/usr/bin/env python3
"""
Session 43 W6-20: All 8 GGE Effective Temperatures
=====================================================================

Computes all 8 effective temperatures {T_k = beta_k^{-1}} of the
Generalized Gibbs Ensemble (GGE) that characterizes the permanent
non-thermal relic produced by the transit quench.

Physics:
  After the sudden quench at the fold (tau ~ 0.19), the BCS condensate
  is destroyed (P_exc = 1.000, S38). The post-transit state is NOT
  thermal -- it is a GGE described by:

    rho_GGE = (1/Z) exp(-sum_k beta_k I_k)

  where I_k are the conserved integrals of motion. For this system:

  1. The BCS Hamiltonian is exactly diagonalized (256 states from 8 modes)
  2. The ground state |GS> is known exactly from ED
  3. The quench maps |GS> onto the free-particle basis
  4. The 8 conserved integrals are the occupation numbers n_k of the
     8 single-particle levels (post-transit, pairing is destroyed)
  5. The GGE Lagrange multipliers beta_k are fixed by:
     <n_k>_GGE = <GS|n_k|GS> = f_k
  6. Since rho_GGE factorizes per mode:
     f_k = 1/(exp(beta_k) + 1)  =>  beta_k = ln((1-f_k)/f_k)
  7. T_k = 1/beta_k is the effective temperature of mode k

  The T_RH = 1.098 M_KK (E-GGE-42) is the THERMODYNAMIC temperature
  obtained by equating total GGE energy to a thermal bath. The 8 T_k
  are mode-specific generalized temperatures that encode the full
  non-thermal character of the relic.

Volovik connection (Paper 34):
  Volovik's time crystal paper shows that integrable systems with
  multiple conserved charges produce GGE states with mode-dependent
  effective temperatures. The oscillation frequencies omega_n = dE/dN_n
  correspond to chemical potentials of the different conserved charges.
  The T_k computed here are the 8 independent thermodynamic coordinates
  of the Volovik time-crystal state.

Author: Volovik Superfluid Universe Theorist, Session 43
Date: 2026-03-14

Gate: GGE-TEMP-43 (INFO)
Input: s37_pair_susceptibility.npz, s38_cc_instanton.npz
Output: s43_gge_temperatures.{npz,png}
"""

import os
import sys
import time
import numpy as np
from numpy.linalg import eigh, eig
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
t0 = time.time()

print("=" * 78)
print("Session 43 W6-20: All 8 GGE Effective Temperatures")
print("=" * 78)

# ======================================================================
#  Step 1: Load stored data and reconstruct Hamiltonian
# ======================================================================

data37 = np.load(os.path.join(SCRIPT_DIR, 's37_pair_susceptibility.npz'),
                 allow_pickle=True)
data38 = np.load(os.path.join(SCRIPT_DIR, 's38_cc_instanton.npz'),
                 allow_pickle=True)

# Also load the upstream ED data for reconstruction
data36 = np.load(os.path.join(SCRIPT_DIR, 's36_multisector_ed.npz'),
                 allow_pickle=True)
arb35 = np.load(os.path.join(SCRIPT_DIR, 's35a_vh_impedance_arbiter.npz'),
                allow_pickle=True)

V_8x8 = data36['V_8x8_full']
E_8 = data36['E_8_full']
branch_labels = list(data37['branch_labels'])
E_cond_stored = float(data36['config_4_E_cond'])

n_modes = 8
n_states = 2**n_modes  # 256
mu = 0.0
xi = E_8 - mu

# DOS: B2 modes get van Hove rho, B1/B3 get 1.0
rho_smooth = float(arb35['rho_at_physical'])
rho = np.array([rho_smooth]*4 + [1.0, 1.0, 1.0, 1.0])

print(f"\nPhysical parameters:")
print(f"  N_modes = {n_modes}, N_states = {n_states}")
print(f"  mu = {mu}")
print(f"  E_8 = {E_8}")
print(f"  rho = {rho}")
print(f"  branch_labels = {branch_labels}")

# ======================================================================
#  Step 2: Reconstruct BCS Hamiltonian and diagonalize
# ======================================================================

print(f"\nReconstructing BCS pair Hamiltonian ({n_states}x{n_states})...")

H_BCS = np.zeros((n_states, n_states))

# Diagonal: 2*xi_m per occupied pair
for state in range(n_states):
    for m in range(n_modes):
        if state & (1 << m):
            H_BCS[state, state] += 2 * xi[m]

# Off-diagonal: pair scattering -V_nm * sqrt(rho_n * rho_m)
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

H_BCS = 0.5 * (H_BCS + H_BCS.T)  # Symmetrize

E_all, psi_all = eigh(H_BCS)
E_gs = E_all[0]
psi_gs = psi_all[:, 0]

print(f"  E_gs = {E_gs:.12f}")
print(f"  E_cond check: |E_gs - stored| = {abs(E_gs - E_cond_stored):.2e}")
assert abs(E_gs - E_cond_stored) < 1e-8, \
    f"FATAL: E_gs mismatch: {E_gs} vs {E_cond_stored}"

# Cross-check against S37 stored eigenvalues
E_all_stored = data37['E_all']
max_diff = np.max(np.abs(E_all - E_all_stored))
print(f"  Max eigenvalue deviation from S37: {max_diff:.2e}")

# ======================================================================
#  Step 3: Compute exact ground-state occupations <n_k>
# ======================================================================

print(f"\n{'='*78}")
print(f"EXACT GROUND STATE OCCUPATIONS")
print(f"{'='*78}")

# <n_k> = sum_s |c_s|^2 * n_k(s)
# where c_s = <s|GS> and n_k(s) = bit k of state s
nk_exact = np.zeros(n_modes)
for k in range(n_modes):
    for s in range(n_states):
        if (s >> k) & 1:
            nk_exact[k] += abs(psi_gs[s])**2

print(f"\n  Exact occupations from ED ground state:")
for k in range(n_modes):
    print(f"    {branch_labels[k]:>5s}: <n_k> = {nk_exact[k]:.10f}")
print(f"    Total <N> = {sum(nk_exact):.10f}")

# ======================================================================
#  Step 4: Compare with BCS mean-field occupations
# ======================================================================

print(f"\n{'='*78}")
print(f"BCS MEAN-FIELD COMPARISON")
print(f"{'='*78}")

# MF BCS: v_k^2 = (1/2)(1 - xi_k/E_k) with E_k = sqrt(xi_k^2 + Delta^2)
# Delta from S37:
Delta_pair = float(data37['Delta_pair'])
print(f"  Delta_pair (S37) = {Delta_pair:.6f}")

nk_mf = np.zeros(n_modes)
for k in range(n_modes):
    E_k = np.sqrt(xi[k]**2 + Delta_pair**2)
    nk_mf[k] = 0.5 * (1 - xi[k] / E_k)

print(f"\n  MF vs ED occupations:")
print(f"  {'Mode':>5s}  {'<n_k>_ED':>12s}  {'v_k^2 (MF)':>12s}  {'Ratio':>8s}")
for k in range(n_modes):
    ratio = nk_exact[k] / nk_mf[k] if nk_mf[k] > 1e-15 else float('inf')
    print(f"  {branch_labels[k]:>5s}  {nk_exact[k]:12.8f}  {nk_mf[k]:12.8f}  {ratio:8.4f}")

# The ED result includes fluctuations beyond mean field
# In a number-conserving ED, <n_k> can differ significantly from v_k^2

# ======================================================================
#  Step 5: Post-quench GGE — the sudden approximation
# ======================================================================

print(f"\n{'='*78}")
print(f"POST-QUENCH GENERALIZED GIBBS ENSEMBLE")
print(f"{'='*78}")

# The sudden quench from S38:
# Before: BCS ground state |GS> of H_BCS
# After: BCS pairing destroyed, system evolves under H_free = sum_k 2*xi_k * n_k
#
# In the free Hamiltonian, the 8 occupation numbers n_k are EXACTLY conserved.
# The GGE density matrix is:
#   rho_GGE = (1/Z) exp(-sum_k beta_k n_k)
#
# The beta_k are fixed by matching: <n_k>_GGE = <GS|n_k|GS> = nk_exact[k]
#
# Since the modes are independent in the free Hamiltonian:
#   <n_k>_GGE = 1/(exp(beta_k) + 1) = f_k
#   beta_k = ln((1 - f_k)/f_k)
#   T_k = 1/beta_k

# But there is a subtlety: the BCS ED state |GS> has N_pair = 1 (from S37).
# After quench, the total number is ALSO conserved.
# We must check: does N_pair = 1 propagate correctly?

total_N_gs = sum(nk_exact)
print(f"\n  Total pair number in GS: <N> = {total_N_gs:.10f}")
print(f"  (Should be 1.0 for N_pair = 1 sector)")

# The occupations sum to ~1.0, confirming we're in the 1-pair sector.
# Each n_k is the PROBABILITY of finding the single Cooper pair in mode k.

# For a SINGLE Cooper pair distributed among 8 modes:
# sum_k f_k = 1 (exactly, by number conservation)
# f_k = probability of pair being in mode k
# This is NOT a Fermi-Dirac distribution in general.

# The GGE for number-conserving systems:
# rho_GGE = (1/Z) * delta(N, 1) * exp(-sum_k beta_k n_k)
# The delta function constrains total N = 1.
# In this sector, exactly one mode is occupied.
# P(mode k occupied) = exp(-beta_k) / sum_l exp(-beta_l)

# Equivalently: f_k = exp(-beta_k) / Z_1, where Z_1 = sum_l exp(-beta_l)
# (This is the 1-particle partition function, not the grand canonical one)

# The beta_k are determined up to an overall shift (gauge freedom from N constraint):
# f_k = exp(-beta_k) / Z_1
# => beta_k = -ln(f_k) + ln(Z_1) = -ln(f_k) + const
# => beta_k - beta_j = -ln(f_k/f_j)

# Convention: set sum_k beta_k = 0 (center the chemical potential)
# Then beta_k = -ln(f_k) - (1/L) * sum_l ln(f_l)

# OR: use the physical convention beta_k = -ln(f_k * Z_1)
# with Z_1 = sum_l exp(-beta_l) = sum_l f_l^{-1} * f_l = L (wrong)
# Actually Z_1 = sum_l exp(-beta_l) and f_k = exp(-beta_k)/Z_1

# Simplest: beta_k = -ln(f_k) + C where C = ln(Z_1)
# Physical temperature: T_k is NOT 1/beta_k in the usual sense
# because the system has 1 particle total.

# The CORRECT GGE temperature interpretation:
# For a single pair in 8 modes, the effective temperature for mode k
# relative to mode j is determined by the Boltzmann ratio:
# f_k/f_j = exp(-(2*xi_k - 2*xi_j) / T_eff)  if thermalized
# For a non-thermal state, each pair (k,j) gives a different T_eff.

# Method 1: Pairwise temperatures from occupation ratios
print(f"\n  Method 1: Pairwise effective temperatures")
print(f"  T_kj = -2*(xi_k - xi_j) / ln(f_k/f_j)")
print()

T_pairwise = np.full((n_modes, n_modes), np.nan)
for k in range(n_modes):
    for j in range(n_modes):
        if k == j:
            continue
        if nk_exact[k] > 1e-15 and nk_exact[j] > 1e-15:
            delta_xi = 2 * (xi[k] - xi[j])  # factor 2 for pair
            if abs(delta_xi) > 1e-12:
                ratio = nk_exact[k] / nk_exact[j]
                if ratio > 0:
                    T_pairwise[k, j] = -delta_xi / np.log(ratio)

print(f"  Pairwise T matrix (M_KK):")
header = "  " + "".join(f"{branch_labels[j]:>8s}" for j in range(n_modes))
print(header)
for k in range(n_modes):
    row = f"  {branch_labels[k]:>5s}"
    for j in range(n_modes):
        if k == j:
            row += "       -"
        elif np.isnan(T_pairwise[k, j]):
            row += "     nan"
        else:
            row += f" {T_pairwise[k, j]:7.4f}"
    print(row)

# ======================================================================
#  Step 6: Canonical GGE temperatures (proper N=1 formulation)
# ======================================================================

print(f"\n{'='*78}")
print(f"CANONICAL GGE: N=1 SECTOR")
print(f"{'='*78}")

# In the canonical ensemble with N=1, the density matrix is:
# rho = sum_k f_k |k><k|  (one pair in mode k with probability f_k)
#
# The GGE adds generalized temperatures beta_k:
# rho_GGE = (1/Z) sum_k exp(-beta_k) |k><k|
# f_k = exp(-beta_k) / Z, where Z = sum_l exp(-beta_l)
#
# From f_k: beta_k = -ln(f_k * Z) = -ln(f_k) - ln(Z)
# But Z = 1/(sum_l f_l) ... no, Z = sum_l exp(-beta_l) != 1/sum(f_l)
#
# Since f_k = exp(-beta_k)/Z and sum_k f_k = 1:
# Z = sum_l exp(-beta_l) and sum_k exp(-beta_k)/Z = 1, so Z = sum_k exp(-beta_k)
# This is self-consistent. We choose:
# beta_k = -ln(f_k) + ln(Z)
# Z is the normalizing constant such that sum_k exp(-beta_k)/Z = 1
# This gives Z = sum_k exp(ln(f_k) - ln(Z)) = (1/Z) sum_k f_k = 1/Z
# => Z = 1 (!)
# So: beta_k = -ln(f_k)
# This is the correct canonical-N=1 GGE.

print(f"\n  Canonical N=1 GGE: beta_k = -ln(f_k)")
print(f"  (Z = 1 since sum f_k = 1 and Boltzmann statistics for distinguishable levels)")
print()

beta_k = np.zeros(n_modes)
T_k = np.zeros(n_modes)

for k in range(n_modes):
    f_k = nk_exact[k]
    if f_k > 1e-15:
        beta_k[k] = -np.log(f_k)
        T_k[k] = 1.0 / beta_k[k]
    else:
        beta_k[k] = np.inf
        T_k[k] = 0.0

print(f"  {'Mode':>5s}  {'f_k':>12s}  {'beta_k':>12s}  {'T_k (M_KK)':>12s}  {'2*xi_k':>10s}  {'T_k/2xi_k':>10s}")
for k in range(n_modes):
    two_xi = 2 * xi[k]
    ratio = T_k[k] / two_xi if two_xi > 0 else 0
    print(f"  {branch_labels[k]:>5s}  {nk_exact[k]:12.8f}  {beta_k[k]:12.6f}  {T_k[k]:12.6f}  {two_xi:10.6f}  {ratio:10.6f}")

# ======================================================================
#  Step 7: Volovik-type analysis — mode-dependent entropy
# ======================================================================

print(f"\n{'='*78}")
print(f"MODE-DEPENDENT ENTROPY AND THERMODYNAMICS")
print(f"{'='*78}")

# The GGE entropy is:
# S_GGE = -sum_k f_k ln(f_k)  (Shannon entropy of the pair distribution)

S_GGE = 0.0
for k in range(n_modes):
    if nk_exact[k] > 1e-15:
        S_GGE -= nk_exact[k] * np.log(nk_exact[k])

print(f"\n  GGE entropy: S_GGE = {S_GGE:.10f}")
print(f"  Maximum entropy (equipartition): S_max = ln(8) = {np.log(8):.10f}")
print(f"  S_GGE / S_max = {S_GGE / np.log(8):.6f}")

# Mode-resolved entropy contributions
print(f"\n  Mode entropy contributions:")
s_k = np.zeros(n_modes)
for k in range(n_modes):
    if nk_exact[k] > 1e-15:
        s_k[k] = -nk_exact[k] * np.log(nk_exact[k])
    print(f"    {branch_labels[k]:>5s}: s_k = {s_k[k]:.8f}, fraction = {s_k[k]/S_GGE:.4f}")

# The Volovik temperature (Paper 34, eq. for omega_n = dE/dN_n):
# For mode k, the "chemical potential" is:
# mu_k = dE/dN_k = 2*xi_k (energy cost to add a pair to mode k)
# The GGE temperature T_k is defined via:
# f_k = exp(-(mu_k - mu_global)/T_k) / normalization
#
# Or equivalently, the mode temperature from the entropy-energy relation:
# T_k^{-1} = dS/dE_k = dS/d(f_k) * d(f_k)/dE_k
# dS/d(f_k) = -ln(f_k) - 1 + Lagrange_multiplier
# dE_k/d(f_k) = 2*xi_k

# Method: Volovik's effective temperature per mode
# T_k^{Volovik} = 2*xi_k / beta_k = 2*xi_k / (-ln(f_k))
# This gives the "temperature" in the sense of Volovik Paper 34:
# the energy scale of mode k divided by its log-occupation

print(f"\n  Volovik effective temperatures (T = 2*xi / beta):")
T_volovik = np.zeros(n_modes)
for k in range(n_modes):
    if abs(beta_k[k]) > 1e-15:
        T_volovik[k] = 2 * xi[k] / beta_k[k]
    print(f"    {branch_labels[k]:>5s}: T_V = {T_volovik[k]:.6f} M_KK")

# ======================================================================
#  Step 8: Connection to thermodynamic T_RH
# ======================================================================

print(f"\n{'='*78}")
print(f"CONNECTION TO T_RH = 1.098 M_KK (E-GGE-42)")
print(f"{'='*78}")

# T_RH from E-GGE-42:
# T_RH = M_KK * (30 * E_exc / (pi^2 * g_star))^{1/4}
# with E_exc = 50.9 M_KK and g_star = 106.75

from canonical_constants import E_exc as E_exc_total  # 60.6 M_KK (was 50.9 with old E_cond)
g_star = 106.75
T_RH = (30 * E_exc_total / (np.pi**2 * g_star))**0.25
print(f"\n  E_exc (total quench energy) = {E_exc_total:.1f} M_KK")
print(f"  g_star (SM) = {g_star}")
print(f"  T_RH = (30*E_exc/(pi^2*g_star))^(1/4) = {T_RH:.6f} M_KK")

# The total GGE energy in the 1-pair sector:
E_GGE = sum(nk_exact[k] * 2 * xi[k] for k in range(n_modes))
print(f"\n  E_GGE (1-pair energy) = sum_k f_k * 2*xi_k = {E_GGE:.6f} M_KK")
print(f"  E_gs (BCS) = {E_gs:.6f} M_KK")

# The excitation energy per pair in the GGE:
# E_exc_per_pair = E_GGE - E_gs (energy above BCS ground state)
# This should be related to 2*Delta_pair (pair breaking energy)
E_exc_per_pair = E_GGE - E_gs
print(f"  E_exc per pair = E_GGE - E_gs = {E_exc_per_pair:.6f} M_KK")

# Which T_k corresponds to T_RH?
# T_RH is the thermodynamic temperature of the 4D radiation bath
# AFTER the GGE decays through 992 KK channels.
# T_RH is NOT directly any single T_k — it is the thermal equilibrium
# temperature when ALL GGE energy is equipartitioned.
#
# However, we can identify the CLOSEST T_k:
print(f"\n  Comparison of T_k to T_RH = {T_RH:.6f} M_KK:")
for k in range(n_modes):
    ratio_rh = T_k[k] / T_RH
    print(f"    {branch_labels[k]:>5s}: T_k/T_RH = {ratio_rh:.6f}")

# The "thermal equivalent" temperature from the GGE entropy:
# If the GGE were thermal, T_therm * S_GGE = E_GGE
# T_therm = E_GGE / S_GGE
T_therm = E_GGE / S_GGE if S_GGE > 0 else float('inf')
print(f"\n  Thermal equivalent: T_therm = E_GGE/S_GGE = {T_therm:.6f} M_KK")
print(f"  T_therm / T_RH = {T_therm/T_RH:.4f}")

# ======================================================================
#  Step 9: Richardson-Gaudin integrals for the NON-UNIFORM case
# ======================================================================

print(f"\n{'='*78}")
print(f"RICHARDSON-GAUDIN ANALYSIS")
print(f"{'='*78}")

# The V_8x8 matrix is NOT uniform coupling (rank 8, not rank 1).
# For the general BCS Hamiltonian H = sum_k 2*xi_k n_k - sum_{kl} G_kl P+_k P-_l,
# integrability requires G_kl = g * f_k * f_l (separable) or G_kl = g (uniform).
#
# Test separability:
G_kl = np.zeros((n_modes, n_modes))
for k in range(n_modes):
    for l in range(n_modes):
        G_kl[k, l] = V_8x8[k, l] * np.sqrt(rho[k] * rho[l])

eigG, vecG = eigh(G_kl)
print(f"\n  Coupling matrix G_kl = V_kl * sqrt(rho_k * rho_l) eigenvalues:")
for i, ev in enumerate(eigG):
    print(f"    lambda_{i} = {ev:.8f}")

# Separability: G = g * |f><f| means only 1 nonzero eigenvalue
# Rank of G:
rank = np.sum(np.abs(eigG) > 1e-10 * np.max(np.abs(eigG)))
print(f"\n  Rank of G (10^-10 threshold): {rank}")
print(f"  System is {'SEPARABLE (R-G integrable)' if rank == 1 else 'NOT separable (NOT R-G integrable in strict sense)'}")

# For the non-integrable case, the 8 "conserved integrals" are:
# Post-transit occupation numbers n_k (conserved by H_free = sum 2*xi_k n_k)
# These are exact integrals of the POST-transit Hamiltonian.
# Pre-transit, they are approximately conserved if V is weak.

# Degree of integrability violation:
# Compare ED occupations with Boltzmann (thermal) prediction at T_therm
print(f"\n  Integrability diagnostic:")
print(f"  {'Mode':>5s}  {'f_k(GGE)':>10s}  {'f_k(therm)':>10s}  {'Deviation':>10s}")
for k in range(n_modes):
    f_therm = np.exp(-2*xi[k]/T_therm) / sum(np.exp(-2*xi[l]/T_therm) for l in range(n_modes))
    dev = abs(nk_exact[k] - f_therm) / max(nk_exact[k], 1e-15)
    print(f"  {branch_labels[k]:>5s}  {nk_exact[k]:10.6f}  {f_therm:10.6f}  {dev:10.4f}")

# ======================================================================
#  Step 10: The 3 distinct temperatures (by degeneracy)
# ======================================================================

print(f"\n{'='*78}")
print(f"DISTINCT GGE TEMPERATURES (3 BRANCHES)")
print(f"{'='*78}")

# Due to degeneracies in E_8 (B2 4-fold, B3 3-fold, B1 singlet),
# the 8 T_k collapse to 3 distinct values IF the GS respects the symmetry.

# Branch averages:
T_B2 = np.mean(T_k[:4])
T_B1 = T_k[4]
T_B3 = np.mean(T_k[5:8])

f_B2 = np.mean(nk_exact[:4])
f_B1 = nk_exact[4]
f_B3 = np.mean(nk_exact[5:8])

print(f"\n  Branch-averaged temperatures:")
print(f"  {'Branch':>6s}  {'g_k':>4s}  {'f_k':>10s}  {'beta_k':>10s}  {'T_k (M_KK)':>12s}  {'2*xi_k':>10s}")
print(f"  {'B2':>6s}  {'4':>4s}  {f_B2:10.8f}  {-np.log(f_B2):10.6f}  {T_B2:12.6f}  {2*xi[0]:10.6f}")
print(f"  {'B1':>6s}  {'1':>4s}  {f_B1:10.8f}  {-np.log(f_B1):10.6f}  {T_B1:12.6f}  {2*xi[4]:10.6f}")
print(f"  {'B3':>6s}  {'3':>4s}  {f_B3:10.8f}  {-np.log(f_B3):10.6f}  {T_B3:12.6f}  {2*xi[5]:10.6f}")

# Degeneracy breaking within B2 and B3
print(f"\n  Within-branch spread:")
print(f"    B2: max-min = {np.max(T_k[:4]) - np.min(T_k[:4]):.2e} M_KK")
print(f"    B3: max-min = {np.max(T_k[5:8]) - np.min(T_k[5:8]):.2e} M_KK")

# ======================================================================
#  Step 11: Physical interpretation in Volovik framework
# ======================================================================

print(f"\n{'='*78}")
print(f"VOLOVIK INTERPRETATION: TIME-CRYSTAL FREQUENCIES")
print(f"{'='*78}")

# From Volovik Paper 34: omega_n = dE/dN_n = partial E / partial N_n
# In our system: omega_k = 2*xi_k (energy of adding one pair to mode k)
# The oscillation frequency is the chemical potential difference:
# omega_{kl} = mu_k - mu_l = 2*(xi_k - xi_l)

print(f"\n  Volovik oscillation frequencies (Paper 34):")
print(f"  omega_k = 2*xi_k (mode chemical potential):")
for k in range(n_modes):
    print(f"    {branch_labels[k]:>5s}: omega_k = {2*xi[k]:.6f} M_KK")

print(f"\n  Inter-branch frequencies omega_{k,l} = 2*(xi_k - xi_l):")
xi_unique = [xi[0], xi[4], xi[5]]  # B2, B1, B3
labels_unique = ['B2', 'B1', 'B3']
for i in range(3):
    for j in range(i+1, 3):
        omega_ij = 2 * abs(xi_unique[i] - xi_unique[j])
        print(f"    omega({labels_unique[i]},{labels_unique[j]}) = {omega_ij:.6f} M_KK")

# Time-crystal order parameter from Paper 34:
# <O(t)> = sum_k A_k * exp(-i * omega_k * t)
# where A_k = sqrt(f_k) (amplitude set by GGE occupation)

print(f"\n  Time-crystal oscillation amplitudes:")
for k in range(n_modes):
    A_k = np.sqrt(nk_exact[k])
    print(f"    {branch_labels[k]:>5s}: A_k = sqrt(f_k) = {A_k:.6f}")

# ======================================================================
#  Step 12: Non-thermality diagnostic
# ======================================================================

print(f"\n{'='*78}")
print(f"NON-THERMALITY DIAGNOSTIC")
print(f"{'='*78}")

# If the GGE were thermal at temperature T, then:
# f_k = exp(-2*xi_k / T) / sum_l exp(-2*xi_l / T)
# All pairwise T_kl would be equal. The SPREAD in T_kl measures non-thermality.

# Compute all pairwise temperatures between distinct branches
T_B2B1 = -2*(xi[0] - xi[4]) / np.log(f_B2/f_B1) if abs(f_B2/f_B1 - 1) > 1e-10 else np.inf
T_B2B3 = -2*(xi[0] - xi[5]) / np.log(f_B2/f_B3) if abs(f_B2/f_B3 - 1) > 1e-10 else np.inf
T_B1B3 = -2*(xi[4] - xi[5]) / np.log(f_B1/f_B3) if abs(f_B1/f_B3 - 1) > 1e-10 else np.inf

print(f"\n  Pairwise temperatures (inter-branch):")
print(f"    T(B2,B1) = {T_B2B1:.6f} M_KK")
print(f"    T(B2,B3) = {T_B2B3:.6f} M_KK")
print(f"    T(B1,B3) = {T_B1B3:.6f} M_KK")

T_pairs = np.array([T_B2B1, T_B2B3, T_B1B3])
T_pairs_finite = T_pairs[np.isfinite(T_pairs)]

if len(T_pairs_finite) > 1:
    T_mean_pair = np.mean(T_pairs_finite)
    T_std_pair = np.std(T_pairs_finite)
    non_thermality = T_std_pair / T_mean_pair
    print(f"\n  Mean pairwise T = {T_mean_pair:.6f} M_KK")
    print(f"  Std pairwise T  = {T_std_pair:.6f} M_KK")
    print(f"  Non-thermality index sigma/mu = {non_thermality:.6f}")
    print(f"  (0 = thermal, >0.1 = clearly non-thermal)")
else:
    non_thermality = 0.0
    T_mean_pair = T_pairs_finite[0] if len(T_pairs_finite) > 0 else 0.0

# ======================================================================
#  Step 13: Energy budget and sector decomposition
# ======================================================================

print(f"\n{'='*78}")
print(f"ENERGY BUDGET IN GGE")
print(f"{'='*78}")

# Energy per branch
E_branch = np.zeros(3)
E_branch[0] = 4 * f_B2 * 2 * xi[0]   # B2: 4 modes
E_branch[1] = f_B1 * 2 * xi[4]        # B1: 1 mode
E_branch[2] = 3 * f_B3 * 2 * xi[5]    # B3: 3 modes

E_total_GGE = sum(E_branch)

print(f"\n  Energy per branch:")
print(f"    B2 (4 modes): E = {E_branch[0]:.6f} M_KK ({E_branch[0]/E_total_GGE*100:.1f}%)")
print(f"    B1 (1 mode):  E = {E_branch[1]:.6f} M_KK ({E_branch[1]/E_total_GGE*100:.1f}%)")
print(f"    B3 (3 modes): E = {E_branch[2]:.6f} M_KK ({E_branch[2]/E_total_GGE*100:.1f}%)")
print(f"    Total: E_GGE = {E_total_GGE:.6f} M_KK")

# Entropy per branch
S_branch = np.zeros(3)
if f_B2 > 1e-15:
    S_branch[0] = -4 * f_B2 * np.log(f_B2)
if f_B1 > 1e-15:
    S_branch[1] = -f_B1 * np.log(f_B1)
if f_B3 > 1e-15:
    S_branch[2] = -3 * f_B3 * np.log(f_B3)

S_total = sum(S_branch)

print(f"\n  Entropy per branch:")
print(f"    B2: S = {S_branch[0]:.6f} ({S_branch[0]/S_total*100:.1f}%)")
print(f"    B1: S = {S_branch[1]:.6f} ({S_branch[1]/S_total*100:.1f}%)")
print(f"    B3: S = {S_branch[2]:.6f} ({S_branch[2]/S_total*100:.1f}%)")
print(f"    Total: S_GGE = {S_total:.6f}")

# Temperature per branch (as T = dE/dS = 2*xi_k)
print(f"\n  Branch thermodynamic temperature T = E/S:")
for i, (lab, g) in enumerate(zip(['B2','B1','B3'], [4,1,3])):
    T_branch = E_branch[i] / S_branch[i] if S_branch[i] > 0 else float('inf')
    print(f"    {lab}: T = E/S = {T_branch:.6f} M_KK")

# ======================================================================
#  Step 14: Full 59.8-pair GGE (scaling from 1-pair result)
# ======================================================================

print(f"\n{'='*78}")
print(f"SCALING TO FULL 59.8-PAIR GGE (S38)")
print(f"{'='*78}")

# The S38 quench produces 59.8 Bogoliubov pairs total.
# Each pair independently occupies the 8 modes with probabilities f_k.
# In the independent-pair approximation, the many-body GGE is:
# rho_many = product_k (rho_k)^{N_k}
# where N_k = 59.8 * f_k is the expected number of pairs in mode k.

N_total_pairs = 59.8  # from S38

print(f"\n  N_total = {N_total_pairs} pairs (S38)")
print(f"\n  Expected occupancy per mode (N_k = N_total * f_k):")
N_k = np.zeros(n_modes)
for k in range(n_modes):
    N_k[k] = N_total_pairs * nk_exact[k]
    print(f"    {branch_labels[k]:>5s}: N_k = {N_k[k]:.4f}")

# Branch totals
N_B2 = 4 * N_total_pairs * f_B2
N_B1 = N_total_pairs * f_B1
N_B3 = 3 * N_total_pairs * f_B3
print(f"\n  Branch totals:")
print(f"    B2: {N_B2:.2f} pairs ({N_B2/N_total_pairs*100:.1f}%)")
print(f"    B1: {N_B1:.2f} pairs ({N_B1/N_total_pairs*100:.1f}%)")
print(f"    B3: {N_B3:.2f} pairs ({N_B3/N_total_pairs*100:.1f}%)")

# Total energy of 59.8-pair GGE:
E_total_59 = N_total_pairs * E_total_GGE
print(f"\n  Total GGE energy (59.8 pairs): {E_total_59:.2f} M_KK")
print(f"  Cross-check E_exc (S38): 50.9 M_KK")
print(f"  Ratio: {E_total_59/50.9:.4f}")

# The GGE temperatures are IDENTICAL in the independent-pair limit:
# Each pair sees the same effective temperature structure.
# The many-body T_k = 1-pair T_k (extensive energy, extensive entropy,
# intensive temperature).

print(f"\n  GGE temperatures are INTENSIVE (same for 1 pair or 59.8 pairs)")
print(f"  The 8 effective temperatures characterize the SHAPE of the distribution,")
print(f"  not the AMOUNT of energy.")

# ======================================================================
#  Step 15: Identify which T matches T_RH
# ======================================================================

print(f"\n{'='*78}")
print(f"T_RH IDENTIFICATION")
print(f"{'='*78}")

# T_RH = 1.098 M_KK is the 4D thermalization temperature.
# None of the 8 T_k individually equals T_RH because:
# 1. T_k are GGE temperatures (non-thermal distribution)
# 2. T_RH is the thermal temperature after cascade + thermalization
# 3. The relationship is: g_star * T_RH^4 = sum_k g_k * N_k * 2*xi_k * M_KK^4

# The GGE energy per 4D volume = E_exc * M_KK^4 = (pi^2/30) * g_star * T_RH^4
# T_RH^4 = 30 * E_exc / (pi^2 * g_star)

# So T_RH is the EQUILIBRIUM temperature when all GGE energy is redistributed
# among g_star = 106.75 SM degrees of freedom. It is NOT any single T_k.

# The CLOSEST match: energy-weighted average temperature
T_energy_weighted = sum(nk_exact[k] * T_k[k] * 2 * xi[k] for k in range(n_modes)) / E_total_GGE
print(f"\n  Energy-weighted average T = {T_energy_weighted:.6f} M_KK")
print(f"  T_RH (thermodynamic) = {T_RH:.6f} M_KK")
print(f"  Ratio = {T_energy_weighted/T_RH:.4f}")

print(f"\n  CONCLUSION: T_RH = 1.098 M_KK is the THERMALIZED temperature.")
print(f"  It is NOT any individual T_k. It emerges when the GGE energy")
print(f"  is redistributed among g_star = {g_star} SM DOF via 992 KK cascades.")
print(f"  The 8 T_k describe the non-thermal GGE BEFORE cascade.")

# ======================================================================
#  Step 16: Summary table
# ======================================================================

print(f"\n{'='*78}")
print(f"FINAL SUMMARY: ALL 8 GGE EFFECTIVE TEMPERATURES")
print(f"{'='*78}")

print(f"\n  {'#':>2s}  {'Mode':>5s}  {'g_k':>3s}  {'f_k':>10s}  {'beta_k':>10s}  {'T_k':>10s}  {'T_V':>10s}  {'2*xi_k':>10s}")
for k in range(n_modes):
    g = 4 if k < 4 else (1 if k == 4 else 3)
    print(f"  {k+1:>2d}  {branch_labels[k]:>5s}  {1:>3d}  {nk_exact[k]:10.8f}  {beta_k[k]:10.6f}  {T_k[k]:10.6f}  {T_volovik[k]:10.6f}  {2*xi[k]:10.6f}")

print(f"\n  Distinct temperatures (3 branches):")
print(f"    T_B2 = {T_B2:.6f} M_KK  (4 modes)")
print(f"    T_B1 = {T_B1:.6f} M_KK  (1 mode)")
print(f"    T_B3 = {T_B3:.6f} M_KK  (3 modes)")

print(f"\n  Ratios:")
print(f"    T_B1/T_B2 = {T_B1/T_B2:.6f}")
print(f"    T_B3/T_B2 = {T_B3/T_B2:.6f}")
print(f"    T_B1/T_B3 = {T_B1/T_B3:.6f}")
print(f"    T_max/T_min = {max(T_B2,T_B1,T_B3)/min(T_B2,T_B1,T_B3):.6f}")

print(f"\n  Thermodynamic quantities:")
print(f"    S_GGE = {S_GGE:.6f}  (non-thermal entropy)")
print(f"    S_max = {np.log(8):.6f}  (equipartition)")
print(f"    S_GGE/S_max = {S_GGE/np.log(8):.4f}")
print(f"    T_RH = {T_RH:.6f} M_KK  (thermalized)")
print(f"    T_therm = {T_therm:.6f} M_KK  (E/S)")
non_th_str = f"{non_thermality:.6f}" if non_thermality > 0 else "computed above"
print(f"    Non-thermality index = {non_th_str}")

# ======================================================================
#  Step 17: SAVE
# ======================================================================

print(f"\n{'='*78}")
print(f"SAVING")
print(f"{'='*78}")

save_dict = {
    # Mode labels and parameters
    'branch_labels': np.array(branch_labels),
    'n_modes': n_modes,
    'E_8': E_8,
    'xi': xi,
    'rho': rho,

    # Exact occupations from ED
    'nk_exact': nk_exact,
    'nk_mf': nk_mf,

    # GGE temperatures
    'beta_k': beta_k,
    'T_k': T_k,
    'T_volovik': T_volovik,

    # Branch averages
    'T_B2': T_B2,
    'T_B1': T_B1,
    'T_B3': T_B3,
    'f_B2': f_B2,
    'f_B1': f_B1,
    'f_B3': f_B3,

    # Pairwise temperatures
    'T_B2B1': T_B2B1,
    'T_B2B3': T_B2B3,
    'T_B1B3': T_B1B3,

    # Thermodynamics
    'S_GGE': S_GGE,
    'S_max': np.log(8),
    'E_GGE': E_total_GGE,
    'T_RH': T_RH,
    'T_therm': T_therm,
    'non_thermality': non_thermality,
    'T_mean_pairwise': T_mean_pair,

    # 59.8-pair extension
    'N_total_pairs': N_total_pairs,
    'N_k': N_k,
    'N_B2': N_B2,
    'N_B1': N_B1,
    'N_B3': N_B3,

    # Branch energies/entropies
    'E_branch': E_branch,
    'S_branch': S_branch,

    # Coupling matrix analysis
    'G_kl': G_kl,
    'G_eigenvalues': eigG,
    'G_rank': rank,

    # Gate
    'gate_verdict': np.array(['INFO']),
}

out_npz = os.path.join(SCRIPT_DIR, 's43_gge_temperatures.npz')
np.savez_compressed(out_npz, **save_dict)
print(f"Saved: {out_npz}")
print(f"  Size: {os.path.getsize(out_npz) / 1024:.1f} KB")

# ======================================================================
#  Step 18: PLOT
# ======================================================================

print(f"\nGenerating plots...")

fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Panel (a): GGE occupations vs mode energy
ax = axes[0, 0]
colors = ['steelblue']*4 + ['firebrick'] + ['forestgreen']*3
for k in range(n_modes):
    ax.bar(k, nk_exact[k], color=colors[k], alpha=0.8, edgecolor='black', lw=0.5)
ax.set_xticks(range(n_modes))
ax.set_xticklabels([str(l) for l in branch_labels], rotation=45, fontsize=8)
ax.set_ylabel('f_k = <n_k>', fontsize=11)
ax.set_title('(a) GGE Occupations', fontsize=12)
ax.axhline(1.0/8, color='gray', ls='--', alpha=0.5, label='Equipartition 1/8')

# Overlay MF prediction
ax.scatter(range(n_modes), nk_mf, marker='x', color='red', s=80, zorder=5,
           label='BCS mean-field v_k^2')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel (b): Effective temperatures
ax = axes[0, 1]
for k in range(n_modes):
    ax.bar(k, T_k[k], color=colors[k], alpha=0.8, edgecolor='black', lw=0.5)
ax.set_xticks(range(n_modes))
ax.set_xticklabels([str(l) for l in branch_labels], rotation=45, fontsize=8)
ax.set_ylabel('T_k = 1/beta_k (M_KK)', fontsize=11)
ax.set_title('(b) GGE Effective Temperatures', fontsize=12)
ax.axhline(T_RH, color='red', ls='--', lw=2, label=f'T_RH = {T_RH:.3f} M_KK')
ax.axhline(T_therm, color='purple', ls=':', lw=2, label=f'T_therm = {T_therm:.3f} M_KK')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel (c): Occupation vs energy (Boltzmann plot)
ax = axes[1, 0]
two_xi_arr = 2 * xi
ax.scatter(two_xi_arr, np.log(nk_exact), c=colors, s=120, edgecolors='black',
           zorder=5, label='GGE (exact ED)')

# Thermal fit
if T_therm > 0:
    xi_plot = np.linspace(min(two_xi_arr)*0.9, max(two_xi_arr)*1.1, 100)
    f_therm_plot = np.exp(-xi_plot / T_therm)
    f_therm_plot /= sum(np.exp(-2*xi[l]/T_therm) for l in range(n_modes))
    ax.plot(xi_plot, np.log(f_therm_plot), 'r--', lw=2, alpha=0.7,
            label=f'Thermal T={T_therm:.3f}')

ax.set_xlabel('2*xi_k (pair energy, M_KK)', fontsize=11)
ax.set_ylabel('ln(f_k)', fontsize=11)
ax.set_title('(c) Boltzmann Plot: GGE vs Thermal', fontsize=12)
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel (d): Energy and entropy budget by branch
ax = axes[1, 1]
branches = ['B2 (x4)', 'B1 (x1)', 'B3 (x3)']
x_pos = np.arange(3)
w = 0.35
bars1 = ax.bar(x_pos - w/2, E_branch/E_total_GGE, w, color=['steelblue', 'firebrick', 'forestgreen'],
               alpha=0.8, label='E_branch/E_total', edgecolor='black')
bars2 = ax.bar(x_pos + w/2, S_branch/S_total, w, color=['steelblue', 'firebrick', 'forestgreen'],
               alpha=0.4, label='S_branch/S_total', edgecolor='black', hatch='//')
ax.set_xticks(x_pos)
ax.set_xticklabels(branches, fontsize=10)
ax.set_ylabel('Fraction of total', fontsize=11)
ax.set_title('(d) Energy and Entropy Budget', fontsize=12)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3, axis='y')

# Add text box
textstr = (f'T_B2 = {T_B2:.4f} M_KK\n'
           f'T_B1 = {T_B1:.4f} M_KK\n'
           f'T_B3 = {T_B3:.4f} M_KK\n'
           f'T_max/T_min = {max(T_B2,T_B1,T_B3)/min(T_B2,T_B1,T_B3):.4f}\n'
           f'S_GGE/S_max = {S_GGE/np.log(8):.4f}\n'
           f'Non-thermality = {non_thermality:.4f}\n'
           f'T_RH = {T_RH:.4f} M_KK')
ax.text(0.97, 0.97, textstr, transform=ax.transAxes, fontsize=8,
        verticalalignment='top', horizontalalignment='right',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

fig.suptitle('W6-20: All 8 GGE Effective Temperatures\n'
             '8-mode ED (256 states), Canonical N=1, Volovik Paper 34',
             fontsize=13, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.93])
out_png = os.path.join(SCRIPT_DIR, 's43_gge_temperatures.png')
plt.savefig(out_png, dpi=150)
plt.close()
print(f"Plot saved: {out_png}")

# ======================================================================
#  FINAL VERDICT
# ======================================================================

elapsed = time.time() - t0

print(f"\n{'='*78}")
print(f"GATE VERDICT: GGE-TEMP-43 -- INFO")
print(f"{'='*78}")
print(f"\n  The 8 GGE effective temperatures are:")
print(f"    T_B2 = {T_B2:.6f} M_KK  (4 degenerate modes, flat optical band)")
print(f"    T_B1 = {T_B1:.6f} M_KK  (1 mode, acoustic)")
print(f"    T_B3 = {T_B3:.6f} M_KK  (3 degenerate modes, dispersive optical)")
print(f"\n  All 3 distinct T_k lie in the narrow range [{min(T_B2,T_B1,T_B3):.4f}, {max(T_B2,T_B1,T_B3):.4f}] M_KK")
print(f"  T_max/T_min = {max(T_B2,T_B1,T_B3)/min(T_B2,T_B1,T_B3):.4f}")
print(f"  Non-thermality index = {non_thermality:.4f}")
print(f"\n  T_RH = {T_RH:.4f} M_KK is the THERMALIZED temperature (post-cascade).")
print(f"  It does NOT correspond to any individual T_k.")
print(f"  T_RH arises from redistributing GGE energy among g* = {g_star} SM DOF.")
print(f"\n  Runtime: {elapsed:.1f}s")
print(f"{'='*78}")
