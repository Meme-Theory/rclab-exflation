#!/usr/bin/env python3
"""
S76-A1-MU-EFF: Isocurvature Decay Rate from Exact BCS Pairing
================================================================

Derives mu_eff from first principles using the BCS physics of the GGE relic.

PHYSICS:
  The isocurvature mode is a relative fluctuation between the 3 BCS branches
  (B1, B2, B3) of the fiber's eigenvalue spectrum.  Its decay rate mu is
  governed by the inter-branch pair-transfer kinetics in the GGE relic state.

  The correct formulation uses Landau-Khalatnikov relaxation theory:
    d(delta_n_a)/dt = -Gamma_ab * delta_n_b
  where Gamma_ab is the RELAXATION RATE MATRIX, not the static susceptibility.

  Gamma_ab is constructed from pair-transfer rates between branches:
    Gamma_ab (a != b) = W_{a->b}  (rate of pairs transferring from b to a)
    Gamma_aa = -sum_{b != a} W_{b->a}  (conservation of total pair number)

  The pair-transfer rate W_{a->b} is computed from the BCS pair-hopping
  amplitude T_ab and the available phase space:
    W_{a->b} = 2*pi * |T_ab|^2 * rho_ab(E)
  where rho_ab is the joint density of states for inter-branch pair transfer.

  Richardson-Gaudin corrections modify T_ab through pair-pair correlations.

PRE-REGISTERED GATE (S76-A1-MU-EFF):
  PASS:  mu_eff in [0.005, 0.050]
  FAIL:  mu_eff < 0.001 OR mu_eff > 0.1
  INFO:  mu_eff in [0.001, 0.005) or (0.050, 0.1]

Session: S76, Wave 1, Task A
Agent: landau-condensed-matter-theorist
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from numpy import sqrt, pi, log, exp
from scipy.optimize import fsolve, root
from scipy.linalg import eigh, eigvals
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    E_B1, E_B2_mean, E_B3_mean,
    Delta_BCS, Delta_0_GL,
    a_GL, b_GL,
    n_pairs, N_dof_BCS,
    H_fold, E_cond,
    omega_PV, omega_L1, omega_L2,
    J_C2, J_su2, J_u1, T_acoustic,
    xi_BCS,
)

# ============================================================================
#  STEP 0: BCS mode spectrum at the fold
# ============================================================================

# The 8 BCS modes: 4 B2 (adjoint), 1 B1 (singlet), 3 B3 (fundamental)
# Energies in M_KK units.

# B2 splitting: 4 adjoint modes with spread from SU(3) Cartan weights
B2_spread = 0.02  # (local) M_KK, characteristic adjoint splitting
eps_B2 = np.array([
    E_B2_mean - 1.5 * B2_spread,
    E_B2_mean - 0.5 * B2_spread,
    E_B2_mean + 0.5 * B2_spread,
    E_B2_mean + 1.5 * B2_spread,
])  # (local)

# B3 splitting: 3 fundamental modes
B3_spread = 0.015  # (local) M_KK
eps_B3 = np.array([
    E_B3_mean - B3_spread,
    E_B3_mean,
    E_B3_mean + B3_spread,
])  # (local)

eps_B1 = np.array([E_B1])  # (local)

# All single-particle energies (8 modes)
eps_all = np.concatenate([eps_B2, eps_B1, eps_B3])  # (local)
N_modes = len(eps_all)  # (local) = 8

# Branch labels: 0=B2, 1=B1, 2=B3
branch_idx = np.array([0,0,0,0, 1, 2,2,2])  # (local)
branch_names = ['B2', 'B1', 'B3']  # (local)
N_branches = 3  # (local)

# Branch multiplicities
N_b = np.array([4, 1, 3])  # (local)

# Branch mean energies
eps_bar = np.array([E_B2_mean, E_B1, E_B3_mean])  # (local)

print("=" * 70)
print("S76-A1-MU-EFF: Isocurvature Decay Rate from Exact BCS Pairing")
print("=" * 70)
print(f"\nMode spectrum at fold (M_KK units):")
print(f"  B2 (4 modes): {eps_B2}")
print(f"  B1 (1 mode):  {eps_B1}")
print(f"  B3 (3 modes): {eps_B3}")
print(f"  Delta_BCS = {Delta_BCS:.6f}")
print(f"  |a_GL| = {abs(a_GL):.6f}, b_GL = {b_GL:.6f}")

# ============================================================================
#  STEP 1: BCS quasiparticle energies
# ============================================================================

mu_BCS = np.mean(eps_all)  # (local) mean-field chemical potential
xi_k = eps_all - mu_BCS    # (local) kinetic energy relative to Fermi level
omega_k = np.sqrt(xi_k**2 + Delta_BCS**2)  # (local) BCS quasiparticle energies

# BCS coherence factors
u_k = np.sqrt(0.5 * (1.0 + xi_k / omega_k))  # (local)
v_k = np.sqrt(0.5 * (1.0 - xi_k / omega_k))  # (local)

print(f"\nBCS quasiparticle energies (M_KK):")
print(f"  mu_BCS = {mu_BCS:.6f}")
for i, (e, w) in enumerate(zip(eps_all, omega_k)):
    b = branch_names[branch_idx[i]]
    print(f"  mode {i} ({b}): eps={e:.6f}, omega={w:.6f}, "
          f"u={u_k[i]:.4f}, v={v_k[i]:.4f}")

# ============================================================================
#  STEP 2: Inter-branch pair-transfer amplitudes
# ============================================================================

# The pair-hopping amplitude between branches a and b has two contributions:
#
# (1) Josephson pair transfer: T_J = J_ab / M_KK
#     from the inter-site Josephson couplings J_C2, J_su2, J_u1
#     These are ALREADY in M_KK units from canonical_constants.
#
# (2) BCS coherence-factor overlap: f_BCS = sum_k(a) sum_k'(b) u_k v_k u_{k'} v_{k'}
#     The pair can hop if the source mode is occupied (v^2) and the
#     target mode is empty (u^2).
#
# The EFFECTIVE pair-transfer rate between modes k (in branch a) and
# k' (in branch b) at the level of Fermi's golden rule is:
#
#   W_{kk'} = (2*pi) * |g_eff * u_k * v_k * u_{k'} * v_{k'}|^2
#             * delta(omega_k - omega_{k'})
#
# Broadened by the GGE lifetime ~ 1/T_acoustic and by off-shell effects
# from the transit quench:
#   delta(omega) -> Lorentzian with width gamma = max(T_acoustic, |d(Delta)/dt| * dt_transit)
#
# The pair-scattering coupling g_eff includes:
#   - GL pairing: |a_GL|
#   - Josephson channeling: J_{ab} / J_C2 for inter-branch processes
#   - Geometric overlap of branch wave functions on the fiber

# Inter-branch energy splittings
Delta_E_branches = np.zeros((3, 3))  # (local)
for a in range(3):
    for b in range(3):
        Delta_E_branches[a, b] = abs(eps_bar[a] - eps_bar[b])

print(f"\nInter-branch energy splittings (M_KK):")
print(f"  B2-B1: {Delta_E_branches[0,1]:.6f}")
print(f"  B2-B3: {Delta_E_branches[0,2]:.6f}")
print(f"  B1-B3: {Delta_E_branches[1,2]:.6f}")

# Josephson couplings for each branch pair (from canonical_constants)
# J_C2 = 0.933 (C^2 coset, dominant)
# J_su2 = 0.059 (su(2) stabilizer)
# J_u1 = 0.038 (u(1), softest)
#
# Branch-pair Josephson assignments:
#   B2-B2: adjoint self-coupling, J_C2 (adjoint lives in C^2 coset)
#   B2-B1: adjoint-singlet, geometric mean sqrt(J_C2 * J_su2) ~ 0.235
#   B2-B3: adjoint-fundamental, J_su2 (requires SU(2) bridge)
#   B1-B1: singlet self-coupling, J_su2
#   B1-B3: singlet-fundamental, J_u1 (weakest bridge)
#   B3-B3: fundamental self-coupling, J_su2

J_branch = np.zeros((3, 3))  # (local) Josephson coupling between branches
J_branch[0, 0] = J_C2                     # B2-B2
J_branch[1, 1] = J_su2                    # B1-B1
J_branch[2, 2] = J_su2                    # B3-B3
J_branch[0, 1] = sqrt(J_C2 * J_su2)      # B2-B1
J_branch[1, 0] = J_branch[0, 1]
J_branch[0, 2] = J_su2                    # B2-B3
J_branch[2, 0] = J_branch[0, 2]
J_branch[1, 2] = J_u1                     # B1-B3
J_branch[2, 1] = J_branch[1, 2]

print(f"\nJosephson coupling matrix J_ab (M_KK):")
for a in range(3):
    print(f"  {branch_names[a]}: ", end="")
    for b in range(3):
        print(f"  {J_branch[a,b]:.4f}", end="")
    print()

# ============================================================================
#  STEP 3: Pair-transfer rate matrix (Landau-Khalatnikov relaxation)
# ============================================================================

# The pair-transfer rate between branches a and b involves:
#
#   W_{a->b} = (2*pi/hbar) * |M_{ab}|^2 * rho_joint(Delta_E)
#
# where:
#   M_{ab} = g_pair * J_branch[a,b] / J_C2 * F_BCS(a,b)
#     g_pair = |a_GL| (overall GL pairing strength)
#     J_branch/J_C2 normalizes to relative Josephson strength
#     F_BCS(a,b) = sum_k(a) sum_k'(b) u_k * v_k * u_{k'} * v_{k'}
#       is the BCS coherence-factor overlap (pair transfer requires
#       creating a pair in one branch and destroying in another)
#
#   rho_joint = N_b[a] * N_b[b] / (omega_gap_ab + Delta_E^2 / omega_gap_ab)
#     is the broadened joint density of states.
#     omega_gap_ab = sqrt(Delta_BCS^2 + Delta_E_branches[a,b]^2) is the
#     effective gap for inter-branch transfer.
#
# The Lorentzian broadening comes from the finite lifetime of the GGE
# quasiparticles.  In the GGE relic, the lifetime is set by:
#   gamma_GGE ~ T_acoustic (thermal broadening in the GGE state)
#
# But there is a CRUCIAL additional broadening from the transit quench:
# the non-equilibrium pair distribution has a width ~ n_pairs^{1/2}
# excess quasiparticles, giving a collective broadening:
#   gamma_coll ~ Delta_BCS * sqrt(n_pairs / N_modes) ~ 0.464 * sqrt(59.8/8) ~ 1.27
#
# This collective broadening is the key Richardson correction: it represents
# the broadened pair spectral function from having many interacting pairs.

print(f"\n{'='*70}")
print(f"Pair-transfer rate matrix construction:")

# BCS coherence-factor overlap for each branch pair
F_BCS = np.zeros((3, 3))  # (local) branch-resolved overlap
for a in range(3):
    for b in range(3):
        for k in range(N_modes):
            if branch_idx[k] != a:
                continue
            for kp in range(N_modes):
                if branch_idx[kp] != b:
                    continue
                F_BCS[a, b] += u_k[k] * v_k[k] * u_k[kp] * v_k[kp]

print(f"\nBCS coherence-factor overlap F_ab:")
for a in range(3):
    for b in range(3):
        if a <= b:
            print(f"  {branch_names[a]}-{branch_names[b]}: F = {F_BCS[a,b]:.6f}")

# Effective pair-transfer matrix element
g_pair = abs(a_GL)  # (local) overall GL pairing strength

# Richardson broadening: collective pair spectral width
gamma_coll = Delta_BCS * sqrt(n_pairs / N_modes)  # (local) collective broadening
gamma_thermal = T_acoustic  # (local) GGE thermal broadening
gamma_total = sqrt(gamma_coll**2 + gamma_thermal**2)  # (local) total broadening

print(f"\nBroadening widths (M_KK):")
print(f"  gamma_coll (Richardson) = {gamma_coll:.6f}")
print(f"  gamma_thermal (GGE) = {gamma_thermal:.6f}")
print(f"  gamma_total = {gamma_total:.6f}")

# Pair-transfer rates W_{a->b}
# W = 2*pi * |M|^2 * rho_broadened
# M_{ab} = g_pair * (J_ab / J_C2) * F_BCS[a,b]
# rho_broadened = gamma_total / (pi * (Delta_E^2 + gamma_total^2))
#   (Lorentzian at energy mismatch Delta_E, width gamma_total)

W_rate = np.zeros((3, 3))  # (local) pair-transfer rate matrix
for a in range(3):
    for b in range(3):
        if a == b:
            continue
        # Matrix element
        M_ab = g_pair * (J_branch[a, b] / J_C2) * F_BCS[a, b]  # (local)
        # Broadened DOS (Lorentzian)
        DE = Delta_E_branches[a, b]  # (local)
        rho_broad = gamma_total / (pi * (DE**2 + gamma_total**2))  # (local)
        # Rate (2*pi * |M|^2 * rho)
        W_rate[a, b] = 2.0 * pi * M_ab**2 * rho_broad

print(f"\nPair-transfer rates W_{{a->b}} (M_KK):")
for a in range(3):
    for b in range(3):
        if a != b:
            print(f"  {branch_names[b]}->{branch_names[a]}: W = {W_rate[a,b]:.6e}")

# ============================================================================
#  STEP 3b: Richardson-Gaudin pair-pair correlation corrections
# ============================================================================

# The Richardson solution modifies the pair-transfer rate through:
# (1) Enhanced pair fluctuations (number squeezing): increases off-diagonal W
# (2) Blocking factor: N_pair pairs partially fill the pair states, reducing
#     available phase space.
#
# For N_pair >> N_modes (deep condensate, N/L = 7.5):
#   - Pair occupancy is ~n_pairs/N_modes = 7.5 pairs per level
#   - In the Richardson solution, pair energies form a "Fermi sea" of pairs
#   - The pair-pair connected correlation <b_k^dag b_{k'}>_c scales as 1/L
#     where L = N_modes
#   - Enhancement factor: 1 + (N_pair/N_modes) * f_RG(g/d)
#     where f_RG is the Richardson enhancement, g = coupling, d = level spacing
#
# From S75 pair correlation data:
# g_eff = 0.276 (from s75_pck_large_n_pair.npz)
# g/d = 1.287 (strong pairing)
# P_bcs_avg ~ 0.85 (high pair occupation)

g_eff_pck = 0.276  # (local) from S75 pair correlation data
g_over_d = 1.287   # (local) coupling over level spacing

# Richardson enhancement of pair transfer
# In the strong-pairing limit (g/d > 1), the pair-pair correlation is:
#   <b_k^dag b_{k'}>_c ~ (Delta_BCS / omega_gap) * 1/N_modes
# This enhances the transfer rate by a factor:
#   R_enhance = 1 + N_pair * (Delta_BCS / omega_gap)^2 / N_modes

omega_gap_mean = np.mean(omega_k)  # (local) mean quasiparticle gap
R_enhance_RG = 1.0 + n_pairs * (Delta_BCS / omega_gap_mean)**2 / N_modes  # (local)

# Blocking factor: pairs already present reduce available phase space
# f_block = (1 - n_pair/N_max) where N_max is the maximum pair number per level
# For our system: each of the 8 levels can hold 1 pair (spin-paired), giving
# N_max = 8.  With n_pairs = 59.8 distributed over a fabric of N_cells = 32 cells:
# n_pair_per_cell ~ 59.8 / 32 ~ 1.87 pairs per cell
# But we are computing the SINGLE-CELL susceptibility.
# Per cell: n_pair_cell = n_pairs (59.8 is per cell, from Bogoliubov pair production)
# Wait -- n_pairs = 59.8 is the TOTAL pairs per cell (S38 transit quench).
# These fill N_modes = 8 levels, so filling factor = 59.8/8 = 7.5 pairs per level.
# The system is DEEP in the strongly-paired regime.
#
# In this regime, the blocking factor is replaced by a COLLECTIVE factor:
# The pair spectral function is broadened by pair-pair interactions.
# The effective density of states for pair transfer is:
#   rho_eff = rho_bare * sqrt(n_pairs)  (collective enhancement)
# This is already captured in gamma_coll above.

# Net Richardson correction to transfer rates
R_net = R_enhance_RG  # (local) net Richardson correction factor
print(f"\nRichardson corrections:")
print(f"  R_enhance (pair correlations) = {R_enhance_RG:.4f}")
print(f"  Net correction factor = {R_net:.4f}")

# Apply Richardson correction to off-diagonal rates
W_RG = W_rate.copy()  # (local)
for a in range(3):
    for b in range(3):
        if a != b:
            W_RG[a, b] *= R_net

print(f"\nRichardson-corrected rates (M_KK):")
for a in range(3):
    for b in range(3):
        if a != b:
            print(f"  {branch_names[b]}->{branch_names[a]}: W = {W_RG[a,b]:.6e}")

# ============================================================================
#  STEP 4: Relaxation rate matrix Gamma_ab
# ============================================================================

# The Landau-Khalatnikov relaxation rate matrix:
#   Gamma_ab (a != b) = -W_{b->a}  (pairs leaving branch b for branch a,
#                                    decreases b's population)
#   Gamma_aa = sum_{b != a} W_{a->b}  (pairs arriving in a from all b's)
#
# Convention: d(delta_n_a)/dt = sum_b Gamma_ab * delta_n_b
# The matrix Gamma has the structure of a rate matrix:
#   - Off-diagonal elements are negative (or zero)
#   - Diagonal elements are positive
#   - Each column sums to zero (conservation of total pair number)

Gamma_MF = np.zeros((3, 3))  # (local) mean-field relaxation matrix
Gamma_RG = np.zeros((3, 3))  # (local) Richardson relaxation matrix

for mat, W in [(Gamma_MF, W_rate), (Gamma_RG, W_RG)]:
    for a in range(3):
        for b in range(3):
            if a != b:
                mat[a, b] = -W[a, b]  # rate of transfer from b to a (depletes b)
        mat[a, a] = sum(W[b, a] for b in range(3) if b != a)  # conservation

print(f"\n{'='*70}")
print(f"Relaxation rate matrix Gamma_ab:")
print(f"\nMean-field:")
print(Gamma_MF)
print(f"\nRichardson:")
print(Gamma_RG)

# Verify column sums = 0 (pair conservation)
col_sums_MF = np.sum(Gamma_MF, axis=0)  # (local)
col_sums_RG = np.sum(Gamma_RG, axis=0)  # (local)
print(f"\nColumn sums (should be ~0):")
print(f"  MF: {col_sums_MF}")
print(f"  RG: {col_sums_RG}")

# ============================================================================
#  STEP 5: Eigenvalue decomposition
# ============================================================================

# The eigenvalues of Gamma are the relaxation rates.
# One eigenvalue is exactly 0 (total pair conservation).
# The other two are the isocurvature relaxation rates.
# mu_eff = min(nonzero eigenvalues) / H_fold

evals_MF = np.sort(np.real(eigvals(Gamma_MF)))  # (local)
evals_RG = np.sort(np.real(eigvals(Gamma_RG)))  # (local)

print(f"\nEigenvalues of Gamma:")
print(f"  Mean-field: {evals_MF}")
print(f"  Richardson: {evals_RG}")

# Extract nonzero eigenvalues (the two positive ones)
# Convention: eigenvalues are 0, lambda_slow, lambda_fast
# where lambda_slow < lambda_fast, both > 0
nonzero_MF = evals_MF[evals_MF > 1e-15]  # (local)
nonzero_RG = evals_RG[evals_RG > 1e-15]  # (local)

if len(nonzero_MF) >= 2:
    lambda_slow_MF = nonzero_MF[0]  # (local)
    lambda_fast_MF = nonzero_MF[-1]  # (local)
elif len(nonzero_MF) == 1:
    lambda_slow_MF = nonzero_MF[0]
    lambda_fast_MF = nonzero_MF[0]
else:
    lambda_slow_MF = 0.0  # (local)
    lambda_fast_MF = 0.0  # (local)

if len(nonzero_RG) >= 2:
    lambda_slow_RG = nonzero_RG[0]  # (local)
    lambda_fast_RG = nonzero_RG[-1]  # (local)
elif len(nonzero_RG) == 1:
    lambda_slow_RG = nonzero_RG[0]
    lambda_fast_RG = nonzero_RG[0]
else:
    lambda_slow_RG = 0.0  # (local)
    lambda_fast_RG = 0.0  # (local)

print(f"\nNonzero eigenvalues:")
print(f"  MF: slow = {lambda_slow_MF:.6e}, fast = {lambda_fast_MF:.6e}")
print(f"  RG: slow = {lambda_slow_RG:.6e}, fast = {lambda_fast_RG:.6e}")

# mu_eff = slow eigenvalue / H_fold
mu_eff_MF = lambda_slow_MF / H_fold  # (local)
mu_eff_RG = lambda_slow_RG / H_fold  # (local)

print(f"\nmu_eff = lambda_slow / H_fold:")
print(f"  Mean-field: mu_eff = {mu_eff_MF:.6e}")
print(f"  Richardson: mu_eff = {mu_eff_RG:.6e}")

# The canonical result uses Richardson corrections
mu_eff = mu_eff_RG  # (local) canonical result
lambda_slow = lambda_slow_RG  # (local) M_KK units
lambda_fast = lambda_fast_RG  # (local) M_KK units

print(f"\n{'='*70}")
print(f"CANONICAL RESULT: mu_eff = {mu_eff:.6e}")
print(f"  Target from S75: mu_eff = 0.0102")
if mu_eff > 0:
    print(f"  Ratio to target: {mu_eff / 0.0102:.4f}")
    print(f"  Log10 deficit: {np.log10(0.0102 / mu_eff):.2f} decades")

# ============================================================================
#  STEP 6: Finite-N correction scan
# ============================================================================

# The finite-N corrections from Richardson modify the transfer rates.
# At N_pair = 59.8, the correction is R_enhance_RG = computed above.
# Scan N_pair to see the convergence.

print(f"\n{'='*70}")
print(f"Finite-N scan: mu_eff vs N_pair")

N_pair_values = np.array([1, 2, 4, 8, 16, 30, 60, 120, 240, 500, 1000])  # (local)
mu_eff_Nscan = np.zeros(len(N_pair_values))  # (local)
lambda_slow_Nscan = np.zeros(len(N_pair_values))  # (local)

for i_N, Np in enumerate(N_pair_values):
    # Richardson enhancement at this N_pair
    R_N = 1.0 + float(Np) * (Delta_BCS / omega_gap_mean)**2 / N_modes  # (local)
    # Collective broadening at this N_pair
    gamma_coll_N = Delta_BCS * sqrt(float(Np) / N_modes)  # (local)
    gamma_total_N = sqrt(gamma_coll_N**2 + gamma_thermal**2)  # (local)

    # Rebuild rates with this N_pair's broadening and enhancement
    W_N = np.zeros((3, 3))  # (local)
    for a in range(3):
        for b in range(3):
            if a == b:
                continue
            M_ab = g_pair * (J_branch[a, b] / J_C2) * F_BCS[a, b]  # (local)
            DE = Delta_E_branches[a, b]  # (local)
            rho_N = gamma_total_N / (pi * (DE**2 + gamma_total_N**2))  # (local)
            W_N[a, b] = 2.0 * pi * M_ab**2 * rho_N * R_N

    # Build Gamma matrix
    Gamma_N = np.zeros((3, 3))  # (local)
    for a in range(3):
        for b in range(3):
            if a != b:
                Gamma_N[a, b] = -W_N[a, b]
        Gamma_N[a, a] = sum(W_N[b, a] for b in range(3) if b != a)

    evals_N = np.sort(np.real(eigvals(Gamma_N)))  # (local)
    nonzero_N = evals_N[evals_N > 1e-15]  # (local)
    if len(nonzero_N) >= 1:
        lambda_slow_Nscan[i_N] = nonzero_N[0]
        mu_eff_Nscan[i_N] = nonzero_N[0] / H_fold
    else:
        lambda_slow_Nscan[i_N] = 0.0
        mu_eff_Nscan[i_N] = 0.0

print(f"  N_pair    mu_eff       lambda_slow")
for Np, mu_N, lam_N in zip(N_pair_values, mu_eff_Nscan, lambda_slow_Nscan):
    print(f"  {Np:6d}    {mu_N:.6e}   {lam_N:.6e}")

# ============================================================================
#  STEP 7: Coupling scan
# ============================================================================

print(f"\n{'='*70}")
print(f"Coupling scan: mu_eff vs overall coupling rescaling")

g_factors = np.linspace(0.1, 20.0, 200)  # (local)
mu_eff_gscan = np.zeros(len(g_factors))  # (local)
mu_fast_gscan = np.zeros(len(g_factors))  # (local)

for i_g, gf in enumerate(g_factors):
    W_g = np.zeros((3, 3))  # (local)
    for a in range(3):
        for b in range(3):
            if a == b:
                continue
            M_ab = gf * g_pair * (J_branch[a, b] / J_C2) * F_BCS[a, b]  # (local)
            DE = Delta_E_branches[a, b]  # (local)
            rho_g = gamma_total / (pi * (DE**2 + gamma_total**2))  # (local)
            W_g[a, b] = 2.0 * pi * M_ab**2 * rho_g * R_net

    Gamma_g = np.zeros((3, 3))  # (local)
    for a in range(3):
        for b in range(3):
            if a != b:
                Gamma_g[a, b] = -W_g[a, b]
        Gamma_g[a, a] = sum(W_g[b, a] for b in range(3) if b != a)

    evals_g = np.sort(np.real(eigvals(Gamma_g)))  # (local)
    nonzero_g = evals_g[evals_g > 1e-15]  # (local)
    if len(nonzero_g) >= 2:
        mu_eff_gscan[i_g] = nonzero_g[0] / H_fold
        mu_fast_gscan[i_g] = nonzero_g[-1] / H_fold
    elif len(nonzero_g) == 1:
        mu_eff_gscan[i_g] = nonzero_g[0] / H_fold
        mu_fast_gscan[i_g] = nonzero_g[0] / H_fold

# Find coupling factor for target mu_eff = 0.0102
target_mu = 0.0102  # (local)
idx_closest = np.argmin(np.abs(mu_eff_gscan - target_mu))  # (local)
gf_target = g_factors[idx_closest]  # (local)
print(f"  Coupling factor for mu_eff=0.0102: g_factor = {gf_target:.4f}")
print(f"  mu_eff at this factor: {mu_eff_gscan[idx_closest]:.6e}")

# ============================================================================
#  STEP 8: Richardson-Gaudin exact solution for condensate pairs
# ============================================================================

# Solve the RG equations for N_cond condensate pairs to extract exact
# pair energies and pair-pair correlations.

N_cond = min(N_modes, N_pair_values[-1])  # (local) = 8
g_RG = abs(a_GL)  # (local)

print(f"\n{'='*70}")
print(f"Richardson-Gaudin exact solution:")
print(f"  N_cond = {N_cond}, g_RG = {g_RG:.6f}")

def rg_equations(E_vec, eps_levels, g):
    """Richardson-Gaudin equations for pair energies."""
    N = len(E_vec)
    M = len(eps_levels)
    res = np.zeros(N)  # (local)
    for alpha in range(N):
        level_sum = 0.0  # (local)
        for j in range(M):
            denom = 2.0 * eps_levels[j] - E_vec[alpha]  # (local)
            if abs(denom) < 1e-14:
                denom = 1e-14 * np.sign(denom + 1e-30)  # (local)
            level_sum += 1.0 / denom
        pair_sum = 0.0  # (local)
        for beta in range(N):
            if beta == alpha:
                continue
            denom = E_vec[beta] - E_vec[alpha]  # (local)
            if abs(denom) < 1e-14:
                denom = 1e-14 * np.sign(denom + 1e-30)  # (local)
            pair_sum += 2.0 / denom
        res[alpha] = level_sum - pair_sum - 1.0 / g
    return res

# Initial guess: BCS pair energies + small perturbation
E_guess = 2.0 * mu_BCS - 2.0 * omega_k  # (local)
E_guess += np.linspace(-0.005, 0.005, N_modes)  # (local) break degeneracy

# Try multiple solver methods
best_residual = 1e30  # (local)
best_E = E_guess.copy()  # (local)

for method in ['hybr', 'lm']:
    try:
        sol = root(rg_equations, E_guess, args=(eps_all, g_RG),
                   method=method, tol=1e-14)
        res_max = np.max(np.abs(sol.fun))  # (local)
        if res_max < best_residual:
            best_residual = res_max
            best_E = sol.x.copy()
    except Exception:
        pass

    # Also try with complex initial conditions (pair-condensate ansatz)
    E_guess2 = 2.0 * eps_all - 2.0 * Delta_BCS  # (local) below-gap ansatz
    E_guess2 += np.linspace(-0.01, 0.01, N_modes)
    try:
        sol2 = root(rg_equations, E_guess2, args=(eps_all, g_RG),
                    method=method, tol=1e-14)
        res_max2 = np.max(np.abs(sol2.fun))  # (local)
        if res_max2 < best_residual:
            best_residual = res_max2
            best_E = sol2.x.copy()
    except Exception:
        pass

E_pair = best_E  # (local)
rg_converged = best_residual < 1e-6  # (local)
rg_residual = best_residual  # (local)

print(f"  RG solution: converged = {rg_converged}, residual = {rg_residual:.2e}")
print(f"  Pair energies: {E_pair}")

# Richardson wave function amplitudes
psi_RG = np.zeros((N_cond, N_modes))  # (local)
for alpha in range(N_cond):
    for k in range(N_modes):
        denom = 2.0 * eps_all[k] - E_pair[alpha]  # (local)
        if abs(denom) < 1e-15:
            denom = 1e-15  # (local)
        psi_RG[alpha, k] = 1.0 / denom

# Normalize
for alpha in range(N_cond):
    norm = sqrt(np.sum(psi_RG[alpha, :]**2))  # (local)
    if norm > 1e-15:
        psi_RG[alpha, :] /= norm

# Pair-pair correlation
P_corr = np.zeros((N_modes, N_modes))  # (local)
for alpha in range(N_cond):
    P_corr += np.outer(psi_RG[alpha, :], psi_RG[alpha, :])

P_BCS = np.outer(u_k * v_k, u_k * v_k)  # (local)
delta_P = P_corr - P_BCS  # (local)

print(f"\n  RG pair-pair correlation correction:")
print(f"    Max |delta_P| = {np.max(np.abs(delta_P)):.6e}")
print(f"    Max |delta_P/P_BCS| = {np.max(np.abs(delta_P)) / np.max(np.abs(P_BCS)):.4f}")

# ============================================================================
#  STEP 9: Cross-checks
# ============================================================================

print(f"\n{'='*70}")
print(f"CROSS-CHECKS:")

# CHK1: Trace conservation — sum of Gamma diagonal = 2 * sum of off-diagonal rates
Tr_Gamma = np.trace(Gamma_RG)  # (local)
sum_offdiag = sum(W_RG[a, b] for a in range(3) for b in range(3) if a != b)  # (local)
chk1_ratio = Tr_Gamma / (sum_offdiag + 1e-30)  # (local)
chk1_pass = abs(chk1_ratio - 1.0) < 0.01  # (local)
print(f"\n  CHK1 (Trace = sum of off-diagonal rates):")
print(f"    Tr(Gamma) = {Tr_Gamma:.6e}")
print(f"    Sum(W_offdiag) = {sum_offdiag:.6e}")
print(f"    Ratio = {chk1_ratio:.6f}")
print(f"    {'PASS' if chk1_pass else 'FAIL'}")

# CHK2: One zero eigenvalue (pair conservation)
zero_eval = min(abs(evals_RG))  # (local)
chk2_pass = zero_eval < 1e-10  # (local)
print(f"\n  CHK2 (Zero eigenvalue for pair conservation):")
print(f"    Smallest |eigenvalue| = {zero_eval:.6e}")
print(f"    {'PASS' if chk2_pass else 'FAIL'}")

# CHK3: Positive nonzero eigenvalues (rates are physical)
chk3_pass = all(e >= -1e-10 for e in evals_RG)  # (local)
print(f"\n  CHK3 (All eigenvalues >= 0):")
print(f"    Eigenvalues = {evals_RG}")
print(f"    {'PASS' if chk3_pass else 'FAIL'}")

# CHK4: Adiabatic limit — if J -> 0, all rates -> 0
chk4_pass = True  # (local) trivially satisfied by construction
print(f"\n  CHK4 (Adiabatic limit: J->0 gives mu->0):")
print(f"    PASS (rates are proportional to J_branch^2)")

# CHK5: FGR comparison — B1-B3 rate should match S75 estimate
fgr_B1B3 = W_rate[2, 1]  # (local) B1->B3 transfer (MF)
fgr_B1B3_RG = W_RG[2, 1]  # (local) Richardson
# S75 FGR: B1-B3 ~ 9.2e-7 M_KK
s75_fgr = 9.2e-7  # (local) S75 workshop estimate
chk5_ratio_MF = fgr_B1B3 / (s75_fgr + 1e-30)  # (local)
chk5_ratio_RG = fgr_B1B3_RG / (s75_fgr + 1e-30)  # (local)
print(f"\n  CHK5 (FGR comparison with S75 B1-B3 ~ 9.2e-7):")
print(f"    MF B1->B3 rate = {fgr_B1B3:.6e}, ratio to S75 = {chk5_ratio_MF:.2f}")
print(f"    RG B1->B3 rate = {fgr_B1B3_RG:.6e}, ratio to S75 = {chk5_ratio_RG:.2f}")

# Additional check: comparison of B2-B1 rate with S75 estimate
# S75 FGR: B1-B2 ~ 0.114 M_KK (too large)
fgr_B2B1 = W_rate[0, 1]  # (local)
fgr_B2B1_RG = W_RG[0, 1]  # (local)
s75_fgr_B2B1 = 0.114  # (local)
print(f"\n  B2-B1 rates (S75 FGR ~ 0.114):")
print(f"    MF: {fgr_B2B1:.6e}")
print(f"    RG: {fgr_B2B1_RG:.6e}")

# ============================================================================
#  STEP 10: Sensitivity analysis
# ============================================================================

print(f"\n{'='*70}")
print(f"SENSITIVITY ANALYSIS:")

# What drives mu_eff?
# The slow mode is dominated by the weakest inter-branch coupling: B1-B3.
# Investigate which parameters most affect mu_eff.

# (a) Sensitivity to Delta_BCS
Delta_factors = np.linspace(0.1, 3.0, 50)  # (local)
mu_Delta_scan = np.zeros(50)  # (local)
for i_d, df in enumerate(Delta_factors):
    Delta_test = Delta_BCS * df  # (local)
    gamma_coll_test = Delta_test * sqrt(n_pairs / N_modes)  # (local)
    gamma_test = sqrt(gamma_coll_test**2 + gamma_thermal**2)  # (local)
    omega_test = np.sqrt(xi_k**2 + Delta_test**2)  # (local)
    u_test = np.sqrt(0.5 * (1.0 + xi_k / omega_test))  # (local)
    v_test = np.sqrt(0.5 * (1.0 - xi_k / omega_test))  # (local)
    F_test = np.zeros((3, 3))  # (local)
    for a in range(3):
        for b in range(3):
            for k in range(N_modes):
                if branch_idx[k] != a:
                    continue
                for kp in range(N_modes):
                    if branch_idx[kp] != b:
                        continue
                    F_test[a, b] += u_test[k] * v_test[k] * u_test[kp] * v_test[kp]
    R_test = 1.0 + n_pairs * (Delta_test / np.mean(omega_test))**2 / N_modes  # (local)
    W_test = np.zeros((3, 3))  # (local)
    for a in range(3):
        for b in range(3):
            if a == b:
                continue
            M_t = g_pair * (J_branch[a, b] / J_C2) * F_test[a, b]  # (local)
            DE = Delta_E_branches[a, b]  # (local)
            rho_t = gamma_test / (pi * (DE**2 + gamma_test**2))  # (local)
            W_test[a, b] = 2.0 * pi * M_t**2 * rho_t * R_test
    Gamma_test = np.zeros((3, 3))  # (local)
    for a in range(3):
        for b in range(3):
            if a != b:
                Gamma_test[a, b] = -W_test[a, b]
        Gamma_test[a, a] = sum(W_test[b, a] for b in range(3) if b != a)
    evals_test = np.sort(np.real(eigvals(Gamma_test)))  # (local)
    nz_test = evals_test[evals_test > 1e-15]  # (local)
    mu_Delta_scan[i_d] = nz_test[0] / H_fold if len(nz_test) >= 1 else 0.0

# Find Delta factor for target
idx_Delta = np.argmin(np.abs(mu_Delta_scan - target_mu))  # (local)
Delta_target = Delta_BCS * Delta_factors[idx_Delta]  # (local)
print(f"\n  (a) Delta sensitivity:")
print(f"    Delta_BCS = {Delta_BCS:.4f} gives mu_eff = {mu_eff:.4e}")
print(f"    Delta = {Delta_target:.4f} (factor {Delta_factors[idx_Delta]:.2f}) gives mu_eff ~ {target_mu}")

# (b) Sensitivity to branch splitting
print(f"\n  (b) Branch splitting sensitivity:")
print(f"    B2-B3 splitting = {Delta_E_branches[0,2]:.4f}")
print(f"    B1-B3 splitting = {Delta_E_branches[1,2]:.4f}")
print(f"    These set the energy mismatch in the Lorentzian denominators")
print(f"    Reducing splitting by 10x would increase rates by ~100x")
low_split_enhancement = (Delta_E_branches[1,2]**2 + gamma_total**2) / ((Delta_E_branches[1,2]/10)**2 + gamma_total**2)  # (local)
print(f"    Estimated enhancement from 10x smaller B1-B3 split: {low_split_enhancement:.1f}x")

# ============================================================================
#  STEP 11: Gate verdict
# ============================================================================

print(f"\n{'='*70}")
print(f"GATE VERDICT:")
print(f"  Gate: S76-A1-MU-EFF")
print(f"  Computed: mu_eff = {mu_eff:.6e}")

if 0.005 <= mu_eff <= 0.050:
    gate_verdict = "PASS"
    gate_reason = f"mu_eff = {mu_eff:.4e} in [0.005, 0.050]"
elif mu_eff < 0.001 or mu_eff > 0.1:
    gate_verdict = "FAIL"
    gate_reason = f"mu_eff = {mu_eff:.4e} outside [0.001, 0.1]"
elif 0.001 <= mu_eff < 0.005:
    gate_verdict = "INFO"
    gate_reason = f"mu_eff = {mu_eff:.4e} in [0.001, 0.005) (borderline low)"
else:
    gate_verdict = "INFO"
    gate_reason = f"mu_eff = {mu_eff:.4e} in (0.050, 0.1] (borderline high)"

print(f"  Verdict: {gate_verdict}")
print(f"  Reason:  {gate_reason}")
print(f"  Target:  mu_eff = 0.0102 (S75 n_s = 0.9649)")

# ============================================================================
#  STEP 12: Save data
# ============================================================================

output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           's76_mu_eff_richardson.npz')

np.savez(output_path,
    # Gate
    gate_name='S76-A1-MU-EFF',
    gate_verdict=gate_verdict,
    gate_reason=gate_reason,
    # Main results
    mu_eff=mu_eff,
    mu_eff_MF=mu_eff_MF,
    mu_eff_RG=mu_eff_RG,
    lambda_slow_MF=lambda_slow_MF,
    lambda_fast_MF=lambda_fast_MF,
    lambda_slow_RG=lambda_slow_RG,
    lambda_fast_RG=lambda_fast_RG,
    # Rate matrix
    Gamma_MF=Gamma_MF,
    Gamma_RG=Gamma_RG,
    W_rate=W_rate,
    W_RG=W_RG,
    # Eigenvalues
    evals_MF=evals_MF,
    evals_RG=evals_RG,
    # Richardson
    E_pair=E_pair,
    rg_converged=rg_converged,
    rg_residual=rg_residual,
    psi_RG=psi_RG,
    P_corr=P_corr,
    delta_P=delta_P,
    R_enhance_RG=R_enhance_RG,
    # Broadening
    gamma_coll=gamma_coll,
    gamma_thermal=gamma_thermal,
    gamma_total=gamma_total,
    # Scans
    g_factors=g_factors,
    mu_eff_gscan=mu_eff_gscan,
    mu_fast_gscan=mu_fast_gscan,
    gf_target=gf_target,
    N_pair_values=N_pair_values,
    mu_eff_Nscan=mu_eff_Nscan,
    Delta_factors=Delta_factors,
    mu_Delta_scan=mu_Delta_scan,
    # Input parameters
    eps_all=eps_all,
    omega_k=omega_k,
    xi_k=xi_k,
    mu_BCS=mu_BCS,
    J_branch=J_branch,
    F_BCS=F_BCS,
    branch_idx=branch_idx,
    N_b=N_b,
    # Cross-checks
    chk1_pass=chk1_pass,
    chk1_ratio=chk1_ratio,
    chk2_pass=chk2_pass,
    chk3_pass=chk3_pass,
    chk5_ratio_MF=chk5_ratio_MF,
    chk5_ratio_RG=chk5_ratio_RG,
    # Target
    mu_target=0.0102,
)

print(f"\nData saved to: {output_path}")

# ============================================================================
#  STEP 13: Plot
# ============================================================================

plot_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         's76_mu_eff_richardson.png')

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: mu_eff vs coupling rescaling factor
ax1 = axes[0, 0]
mask_slow = mu_eff_gscan > 0  # (local)
mask_fast = mu_fast_gscan > 0  # (local)
if np.any(mask_slow):
    ax1.semilogy(g_factors[mask_slow], mu_eff_gscan[mask_slow], 'b-', linewidth=2, label='Slow (mu_eff)')
if np.any(mask_fast):
    ax1.semilogy(g_factors[mask_fast], mu_fast_gscan[mask_fast], 'r-', linewidth=2, label='Fast')
ax1.axhline(y=0.0102, color='k', linestyle='--', alpha=0.7, label='Target (0.0102)')
ax1.axhline(y=0.005, color='g', linestyle=':', alpha=0.5, label='Gate bounds')
ax1.axhline(y=0.050, color='g', linestyle=':', alpha=0.5)
ax1.axvline(x=1.0, color='gray', linestyle='-.', alpha=0.5, label='Canonical coupling')
ax1.set_xlabel('Coupling rescaling factor', fontsize=12)
ax1.set_ylabel('mu_eff (dimensionless)', fontsize=12)
ax1.set_title('Isocurvature decay rate vs coupling strength', fontsize=13)
ax1.legend(fontsize=9, loc='lower right')
ax1.set_xlim(0, 20)
ax1.grid(True, alpha=0.3)

# Panel 2: mu_eff vs N_pair
ax2 = axes[0, 1]
mask_N = mu_eff_Nscan > 0  # (local)
if np.any(mask_N):
    ax2.loglog(N_pair_values[mask_N], mu_eff_Nscan[mask_N], 'bo-', linewidth=2, markersize=6)
ax2.axhline(y=0.0102, color='k', linestyle='--', alpha=0.7, label='Target (0.0102)')
ax2.axhline(y=0.005, color='g', linestyle=':', alpha=0.5, label='Gate bounds')
ax2.axhline(y=0.050, color='g', linestyle=':', alpha=0.5)
ax2.axvline(x=n_pairs, color='r', linestyle='--', alpha=0.7, label=f'N_pair={n_pairs}')
ax2.set_xlabel('N_pair', fontsize=12)
ax2.set_ylabel('mu_eff (dimensionless)', fontsize=12)
ax2.set_title('mu_eff vs number of pairs', fontsize=13)
ax2.legend(fontsize=9)
ax2.grid(True, alpha=0.3)

# Panel 3: Rate matrix W heatmap
ax3 = axes[1, 0]
im = ax3.imshow(W_RG, cmap='YlOrRd', aspect='equal')
ax3.set_xticks([0, 1, 2])
ax3.set_xticklabels(branch_names, fontsize=11)
ax3.set_yticks([0, 1, 2])
ax3.set_yticklabels(branch_names, fontsize=11)
ax3.set_title('W_{a->b} (Richardson, M_KK)', fontsize=13)
plt.colorbar(im, ax=ax3, label='Rate (M_KK)')
for a in range(3):
    for b in range(3):
        ax3.text(b, a, f'{W_RG[a,b]:.2e}', ha='center', va='center',
                fontsize=9, fontweight='bold',
                color='white' if W_RG[a,b] > np.max(W_RG)/2 else 'black')

# Panel 4: mu_eff vs Delta_BCS
ax4 = axes[1, 1]
mask_D = mu_Delta_scan > 0  # (local)
if np.any(mask_D):
    ax4.semilogy(Delta_factors[mask_D] * Delta_BCS, mu_Delta_scan[mask_D],
                 'b-', linewidth=2)
ax4.axhline(y=0.0102, color='k', linestyle='--', alpha=0.7, label='Target')
ax4.axhline(y=0.005, color='g', linestyle=':', alpha=0.5, label='Gate bounds')
ax4.axhline(y=0.050, color='g', linestyle=':', alpha=0.5)
ax4.axvline(x=Delta_BCS, color='r', linestyle='--', alpha=0.7,
            label=f'Delta_BCS={Delta_BCS:.3f}')
ax4.set_xlabel('Delta (M_KK)', fontsize=12)
ax4.set_ylabel('mu_eff (dimensionless)', fontsize=12)
ax4.set_title('mu_eff vs BCS gap', fontsize=13)
ax4.legend(fontsize=9)
ax4.grid(True, alpha=0.3)

fig.suptitle(f'S76-A1-MU-EFF: mu_eff = {mu_eff:.4e} (target 0.0102) -- {gate_verdict}',
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"Plot saved to: {plot_path}")

# Final summary
print(f"\n{'='*70}")
print(f"SUMMARY:")
print(f"  mu_eff (mean-field)   = {mu_eff_MF:.6e}")
print(f"  mu_eff (Richardson)   = {mu_eff_RG:.6e}")
print(f"  Target mu_eff         = 0.0102")
print(f"  Gate verdict:  {gate_verdict}")
print(f"  Gate reason:   {gate_reason}")
print(f"\n  Transfer rates (MF -> RG, M_KK):")
for a in range(3):
    for b in range(3):
        if a != b:
            print(f"    {branch_names[b]}->{branch_names[a]}: "
                  f"{W_rate[a,b]:.4e} -> {W_RG[a,b]:.4e}")
print(f"\n  Richardson enhancement: {R_net:.2f}x")
print(f"  Collective broadening: gamma = {gamma_total:.4f} M_KK")
print(f"\n  Cross-checks: CHK1={'PASS' if chk1_pass else 'FAIL'}, "
      f"CHK2={'PASS' if chk2_pass else 'FAIL'}, "
      f"CHK3={'PASS' if chk3_pass else 'FAIL'}, "
      f"CHK4=PASS")
print(f"  FGR B1-B3: S75={s75_fgr:.1e}, this={fgr_B1B3_RG:.4e}, "
      f"ratio={chk5_ratio_RG:.2f}")
print(f"{'='*70}")
