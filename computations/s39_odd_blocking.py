#!/usr/bin/env python3
"""
s39_odd_blocking.py — Odd-Particle Blocking Computation (ODD-39)

Computes the quasiparticle spectrum for odd-particle (blocking) configurations.
In BCS theory, an odd-particle state has one unpaired fermion in mode k,
which blocks that mode from participating in pairing. The remaining N-1 modes
form a reduced BCS Hamiltonian.

The blocking energy delta_E(k) = E_gs(blocked, k) - E_gs(unblocked) gives the
energy cost of placing one unpaired particle in mode k. This is the odd-even
mass staggering, a direct analog of the nuclear odd-even mass difference.

Physics:
  - The pair Fock space is 2^N (N=8 modes, dim=256)
  - Blocking mode k reduces to 2^(N-1) = 128 states (7 active modes)
  - The blocked Hamiltonian removes mode k from both diagonal and off-diagonal
  - The unpaired electron in mode k contributes epsilon_k to the energy

Gate: ODD-39. INFO: Blocking spectrum computed for all 4 B2 modes.

Author: gen-physicist
Date: 2026-03-09
"""

import numpy as np
from scipy import linalg as la
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import time

print("=" * 70)
print("ODD-39: Odd-Particle Blocking Computation")
print("=" * 70)

# ============================================================
# 1. LOAD DATA
# ============================================================

d37 = np.load('tier0-computation/s37_pair_susceptibility.npz', allow_pickle=True)
d38 = np.load('tier0-computation/s38_otoc_bcs.npz', allow_pickle=True)
d39 = np.load('tier0-computation/s39_richardson_gaudin.npz', allow_pickle=True)

E_8 = d37['E_8']            # Single-particle energies
V_8x8 = d37['V_8x8']        # Bare pairing matrix
rho_8 = d37['rho']           # DOS weights
branch_labels = d37['branch_labels']
mu = float(d37['mu'])        # mu = 0
n_modes = int(d37['n_modes'])  # 8

# S38 unblocked ground state energy (from full 256-dim diagonalization)
E_gs_unblocked = float(d38['evals_BCS'][0])  # = -0.6684

# S39 Bogoliubov coefficients at fold
u_k = d39['u_k_fold']
v_k = d39['v_k_fold']
n_k = d39['n_k_fold']
Delta_k = d39['Delta_k_fold']

# S37 three-point mass formula
Delta_OES_s37 = float(d37['Delta_OES'])  # = 0.4643

# Reconstruct the physical pairing matrix used in S38
V_phys = V_8x8 * np.sqrt(np.outer(rho_8, rho_8))

# Single-particle energies relative to Fermi level
xi = E_8 - mu

print(f"\nParameters:")
print(f"  n_modes = {n_modes}")
print(f"  E_8 = {E_8}")
print(f"  mu = {mu}")
print(f"  rho = {rho_8}")
print(f"  branch_labels = {branch_labels}")
print(f"  E_gs(unblocked, S38) = {E_gs_unblocked:.10f}")
print(f"  Delta_OES(S37) = {Delta_OES_s37:.6f}")

# ============================================================
# 2. BUILD UNBLOCKED BCS HAMILTONIAN (verification)
# ============================================================

N = n_modes  # 8
dim_full = 2**N  # 256

def build_H_BCS(xi_arr, V_mat, mode_indices, dim):
    """
    Build BCS pair Hamiltonian in Fock space.

    H = sum_k (2*xi_k - V_kk) * n_k - sum_{k!=k'} V_{kk'} * P_k^dag P_k'

    mode_indices: list of mode indices that are active (not blocked)
    The Fock space basis uses bit positions 0..len(mode_indices)-1
    mapping to the physical modes in mode_indices.
    """
    n_active = len(mode_indices)
    H = np.zeros((dim, dim), dtype=np.float64)

    for alpha in range(dim):
        # Diagonal: kinetic + Hartree
        E_diag = 0.0
        for bit, k in enumerate(mode_indices):
            if alpha & (1 << bit):
                E_diag += 2 * xi_arr[k] - V_mat[k, k]
        H[alpha, alpha] = E_diag

        # Off-diagonal: pair scattering
        for bit_k, k in enumerate(mode_indices):
            for bit_kp, kp in enumerate(mode_indices):
                if k == kp:
                    continue
                if (alpha & (1 << bit_kp)) and not (alpha & (1 << bit_k)):
                    beta = (alpha ^ (1 << bit_kp)) | (1 << bit_k)
                    H[beta, alpha] -= V_mat[k, kp]

    return H

print("\n--- Verification: Unblocked Hamiltonian ---")
t0 = time.time()
H_full = build_H_BCS(xi, V_phys, list(range(N)), dim_full)
evals_full, evecs_full = la.eigh(H_full)
t1 = time.time()

herm_err = np.max(np.abs(H_full - H_full.T))
print(f"  Hermiticity error: {herm_err:.2e}")
print(f"  E_gs(full, this script) = {evals_full[0]:.10f}")
print(f"  E_gs(full, S38 data)    = {E_gs_unblocked:.10f}")
print(f"  Difference: {abs(evals_full[0] - E_gs_unblocked):.2e}")
print(f"  Build+diag time: {t1-t0:.3f}s")

assert abs(evals_full[0] - E_gs_unblocked) < 1e-8, \
    f"Unblocked E_gs mismatch: {evals_full[0]} vs {E_gs_unblocked}"

# Count pairs in ground state
gs_full = evecs_full[:, 0]
npair_gs = sum(np.abs(gs_full[alpha])**2 * bin(alpha).count('1')
               for alpha in range(dim_full))
print(f"  <N_pair> in GS: {npair_gs:.6f}")

# ============================================================
# 3. BLOCKED HAMILTONIANS: Fix one electron in mode k
# ============================================================
#
# Physics: An odd-particle state has one unpaired fermion occupying
# single-particle level k. This blocks mode k from participating in
# pairing. The total energy is:
#
#   E_odd(k) = epsilon_k + E_gs(H_blocked_k)
#
# where epsilon_k = xi_k is the single-particle energy of the unpaired
# electron, and H_blocked_k is the BCS Hamiltonian with mode k removed
# from the active pairing space.
#
# The blocking energy (odd-even staggering) is:
#   delta_E(k) = E_odd(k) - E_gs(unblocked)
#              = xi_k + E_gs(blocked, k) - E_gs(unblocked)
#
# This is positive: it costs energy to break a pair.

print("\n" + "=" * 70)
print("BLOCKING COMPUTATION: 8 modes, one blocked at a time")
print("=" * 70)

dim_blocked = 2**(N-1)  # 128

results = {}

for k_blocked in range(N):
    print(f"\n--- Blocking mode {k_blocked}: {branch_labels[k_blocked]} ---")

    # Active modes: all except k_blocked
    active_modes = [j for j in range(N) if j != k_blocked]

    # Build blocked Hamiltonian
    t0 = time.time()
    H_blocked = build_H_BCS(xi, V_phys, active_modes, dim_blocked)
    evals_blocked, evecs_blocked = la.eigh(H_blocked)
    t1 = time.time()

    # Hermiticity check
    herm_err_b = np.max(np.abs(H_blocked - H_blocked.T))

    # Ground state of blocked system
    E_gs_blocked = evals_blocked[0]

    # First excitation gap in blocked system
    gap_blocked = evals_blocked[1] - evals_blocked[0]

    # <N_pair> in blocked ground state
    gs_blocked = evecs_blocked[:, 0]
    npair_blocked = sum(np.abs(gs_blocked[alpha])**2 * bin(alpha).count('1')
                        for alpha in range(dim_blocked))

    # Total energy of odd-particle state: unpaired electron + blocked pairs
    E_odd = xi[k_blocked] + E_gs_blocked

    # Blocking energy (odd-even staggering)
    delta_E = E_odd - evals_full[0]

    # Quasiparticle energy from BCS theory (for comparison):
    # E_qp(k) = sqrt(xi_k^2 + Delta_k^2) in standard BCS
    # But here we have a finite system, so use the exact blocking result
    E_qp_bcs = np.sqrt(xi[k_blocked]**2 + Delta_k[k_blocked]**2)

    # Pair susceptibility of blocked system
    # Build pair creation/annihilation operators for active modes
    Delta_op_blocked = np.zeros((dim_blocked, dim_blocked))
    for alpha_b in range(dim_blocked):
        for bit, j in enumerate(active_modes):
            if alpha_b & (1 << bit):
                beta_b = alpha_b ^ (1 << bit)
                Delta_op_blocked[beta_b, alpha_b] += np.sqrt(rho_8[j])

    Delta_dag_blocked = Delta_op_blocked.T
    A_blocked = (Delta_op_blocked + Delta_dag_blocked) / np.sqrt(2)

    # Pair susceptibility: chi(omega) via Lehmann representation
    # chi(omega) = sum_n |<n|P^dag|0>|^2 / (omega - omega_n + i*eta)
    #            - sum_n |<n|P|0>|^2 / (omega + omega_n + i*eta)

    # Compute pair transition matrix elements
    gs_b = evecs_blocked[:, 0]
    Pdag_gs = Delta_dag_blocked @ gs_b
    P_gs = Delta_op_blocked @ gs_b

    # Project onto eigenstates
    Bplus_blocked = np.abs(evecs_blocked.T @ Pdag_gs)**2
    Bminus_blocked = np.abs(evecs_blocked.T @ P_gs)**2
    omega_blocked = evals_blocked - evals_blocked[0]

    # M_max for blocked system (pair-addition strength at first pole)
    # Find dominant pair-addition pole
    mask_plus = (Bplus_blocked > 1e-10) & (omega_blocked > 1e-10)
    if np.any(mask_plus):
        idx_first_pole = np.where(mask_plus)[0][0]
        omega_first = omega_blocked[idx_first_pole]
        B_first = Bplus_blocked[idx_first_pole]
        # Total pair-addition strength
        sum_Pdag_blocked = np.sum(Bplus_blocked)
        M_max_blocked = B_first / sum_Pdag_blocked if sum_Pdag_blocked > 0 else 0
    else:
        omega_first = 0.0
        B_first = 0.0
        M_max_blocked = 0.0
        sum_Pdag_blocked = 0.0

    print(f"  Active modes: {[str(branch_labels[j]) for j in active_modes]}")
    print(f"  Hermiticity error: {herm_err_b:.2e}")
    print(f"  E_gs(blocked) = {E_gs_blocked:.10f}")
    print(f"  xi_k (unpaired electron) = {xi[k_blocked]:.10f}")
    print(f"  E_odd = xi_k + E_gs(blocked) = {E_odd:.10f}")
    print(f"  delta_E = E_odd - E_gs(full) = {delta_E:.6f}")
    print(f"  E_qp(BCS) = sqrt(xi^2 + Delta^2) = {E_qp_bcs:.6f}")
    print(f"  Gap in blocked spectrum: {gap_blocked:.6f}")
    print(f"  <N_pair> in blocked GS: {npair_blocked:.6f}")
    print(f"  M_max(blocked): {M_max_blocked:.4f}")
    print(f"  omega(first pole): {omega_first:.6f}")
    print(f"  sum |<n|P^dag|0>|^2: {sum_Pdag_blocked:.6f}")
    print(f"  Diag time: {t1-t0:.3f}s")

    results[k_blocked] = {
        'label': str(branch_labels[k_blocked]),
        'E_gs_blocked': E_gs_blocked,
        'xi_k': xi[k_blocked],
        'E_odd': E_odd,
        'delta_E': delta_E,
        'E_qp_bcs': E_qp_bcs,
        'gap_blocked': gap_blocked,
        'npair_blocked': npair_blocked,
        'M_max_blocked': M_max_blocked,
        'omega_first': omega_first,
        'sum_Pdag': sum_Pdag_blocked,
        'evals_blocked': evals_blocked,
        'Bplus': Bplus_blocked,
        'omega_n': omega_blocked,
    }

# ============================================================
# 4. ODD-EVEN STAGGERING AND THREE-POINT FORMULA
# ============================================================

print("\n" + "=" * 70)
print("ODD-EVEN STAGGERING")
print("=" * 70)

# Three-point mass formula:
#   Delta_3(k) = (E(N+1) + E(N-1) - 2*E(N)) / 2
#
# In BCS pair language:
# - E(N) = E_gs(unblocked) with N_pair pairs (even particle number 2*N_pair)
# - E(N+1) = E_odd(k) = xi_k + E_gs(blocked, k) (odd: 2*N_pair + 1 particles)
# - E(N-1) = E_odd(k') but for particle removal
#
# The S37 Delta_OES = 0.4643 was computed from the pair susceptibility
# as Delta_OES = (omega_plus - omega_minus) / 2, which is the
# pair-addition/removal gap.
#
# For the blocking computation, the three-point formula per mode k is:
#   Delta_3(k) = delta_E(k) = E_odd(k) - E_gs(even)
# because removing a pair costs ~delta_E on the other side too.
# The symmetric three-point formula averages over addition and removal.
#
# More precisely, for the even-N ground state with N_pair pairs:
#   Delta_3 = [E_gs(N_pair, blocked_k) + xi_k + E_gs(N_pair-1, blocked_k) + xi_k
#              - 2*E_gs(N_pair, unblocked)] / 2
# where the first term is adding a particle (blocking k, N_pair pairs in remaining)
# and the second is removing a particle (blocking k, N_pair-1 pairs in remaining).

# For particle REMOVAL: block mode k, but now the remaining system has one
# fewer pair available. The "removed" electron energy is -xi_k (hole).
# E(N-1, k) = -xi_k + E_gs(blocked_k, searching for N_pair-1 ground state)
#
# Since the blocked Hamiltonian spans all pair numbers 0..N-1,
# we need the ground state in the (N_pair - 1) sector of the blocked system.

print(f"\n  E_gs(unblocked) = {evals_full[0]:.10f}")
print(f"  <N_pair> in unblocked GS = {npair_gs:.6f}")

# For each blocked mode, find the ground state in different pair-number sectors
for k_blocked in range(N):
    r = results[k_blocked]
    evals_b = r['evals_blocked']
    active_modes = [j for j in range(N) if j != k_blocked]
    n_active = len(active_modes)
    dim_b = 2**n_active

    # Pair number for each Fock state in blocked space
    npair_blocked_states = np.array([bin(alpha).count('1') for alpha in range(dim_b)])

    # Find ground state energy in each pair-number sector
    sector_E = {}
    for np_val in range(n_active + 1):
        mask = (npair_blocked_states == np_val)
        if not np.any(mask):
            continue
        indices = np.where(mask)[0]
        H_sector = np.zeros((len(indices), len(indices)))
        H_blocked_full = build_H_BCS(xi, V_phys, active_modes, dim_b)
        H_sector = H_blocked_full[np.ix_(indices, indices)]
        ev_sector = la.eigvalsh(H_sector)
        sector_E[np_val] = ev_sector[0]

    results[k_blocked]['sector_E'] = sector_E

# Three-point formula: symmetric version
# E(N+1, k) = xi_k + E_gs(blocked_k, N_pair sector)
# E(N-1, k) = -xi_k + E_gs(blocked_k, N_pair-1 sector)  [hole]
# Wait -- this isn't quite right. Let me think more carefully.
#
# The UNBLOCKED ground state has <N_pair> ~ 1.0 (from S38/RG-39).
# It is PURE N_pair = 1 (from W1-1).
# So the even-particle ground state has exactly 1 pair = 2 particles.
#
# Odd-particle state by ADDITION (3 particles):
#   Block mode k, put 1 unpaired electron in k.
#   The remaining 7 modes can still hold 1 pair (searching N_pair=1 sector).
#   E(3 particles, k) = xi_k + E_gs(blocked_k, N_pair=1)
#
# Odd-particle state by REMOVAL (1 particle):
#   Remove one electron from a pair. The unpaired electron stays in mode k.
#   Block mode k (occupied by one electron).
#   The remaining 7 modes now have 0 pairs.
#   E(1 particle, k) = xi_k + E_gs(blocked_k, N_pair=0)
#   But wait: E_gs(blocked_k, N_pair=0) = 0 (vacuum, no pairs).
#
# Three-point formula:
#   Delta_3(k) = [E(3,k) + E(1,k) - 2*E(2)] / 2
#              = [xi_k + E_gs(bl_k, Np=1) + xi_k + 0 - 2*E_gs(unbl, Np=1)] / 2
#              = xi_k + E_gs(bl_k, Np=1)/2 - E_gs(unbl)

print("\n  Unblocked GS is PURE N_pair=1 (2 particles).")
print(f"  E_gs(unblocked, N_pair=1) = {evals_full[0]:.10f}")

print(f"\n  {'Mode':<8} {'E_gs(bl,Np=1)':>14} {'E_gs(bl,Np=0)':>14} "
      f"{'E(3p,k)':>10} {'E(1p,k)':>10} {'Delta_3':>10}")
print(f"  {'-'*8} {'-'*14} {'-'*14} {'-'*10} {'-'*10} {'-'*10}")

delta_3 = {}
for k in range(N):
    r = results[k]
    sE = r['sector_E']

    # E_gs of blocked system in N_pair=1 sector (1 pair in 7 remaining modes)
    E_bl_np1 = sE.get(1, np.nan)
    # E_gs of blocked system in N_pair=0 sector (vacuum: 0 pairs)
    E_bl_np0 = sE.get(0, 0.0)  # Should be 0 by construction

    # Odd-particle energies
    E_3p = xi[k] + E_bl_np1  # 3 particles: 1 unpaired + 1 pair
    E_1p = xi[k] + E_bl_np0  # 1 particle: just the unpaired electron

    # Three-point formula
    D3 = (E_3p + E_1p - 2 * evals_full[0]) / 2
    delta_3[k] = D3

    print(f"  {branch_labels[k]:<8} {E_bl_np1:>14.8f} {E_bl_np0:>14.8f} "
          f"{E_3p:>10.6f} {E_1p:>10.6f} {D3:>10.6f}")

    results[k]['E_3p'] = E_3p
    results[k]['E_1p'] = E_1p
    results[k]['Delta_3'] = D3

print(f"\n  S37 Delta_OES (from pair susceptibility): {Delta_OES_s37:.6f}")
avg_delta3_B2 = np.mean([delta_3[k] for k in range(4)])
print(f"  Average Delta_3 for B2 modes: {avg_delta3_B2:.6f}")
print(f"  Delta_3(B1): {delta_3[4]:.6f}")
avg_delta3_B3 = np.mean([delta_3[k] for k in range(5, 8)])
print(f"  Average Delta_3 for B3 modes: {avg_delta3_B3:.6f}")

# ============================================================
# 5. ODD-PARTICLE WEIGHTS IN THERMAL STATE
# ============================================================

print("\n" + "=" * 70)
print("ODD-PARTICLE WEIGHTS IN THERMAL STATE")
print("=" * 70)

# After transit, the system thermalizes (W2-2: t_therm ~ 6).
# The thermal state at inverse temperature beta_eff is a Gibbs ensemble.
# The probability of an odd number of particles depends on the
# individual mode occupations.
#
# In the pair Fock space, each state has a definite number of PAIRS.
# But we need single-particle occupations for blocking.
#
# In the BCS quasiparticle picture:
# - Each mode k has quasiparticle occupation n_k = v_k^2 (mean-field)
# - The probability that mode k is singly occupied (blocking) in the
#   exact many-body state requires going beyond mean field.
#
# For the THERMAL state at temperature T:
# In the grand canonical ensemble, each quasiparticle mode is independent.
# Probability of mode k being occupied: f_k = 1/(exp(beta*E_qp_k) + 1)
# where E_qp_k is the quasiparticle energy.
#
# But our system conserves pair number, so we work canonically.
# The exact thermal weights come from the full spectrum.

# From W2-2: system thermalizes. Use the full BCS spectrum.
# The Gibbs state is rho = exp(-beta * H) / Z.
# t_therm ~ 6, so beta_eff = 1/T_eff.
#
# What temperature? The conserved energy E = E_gs(unblocked) determines T.
# But actually the GGE has specific energy content.
# Let's compute the thermal weights as a function of temperature.

# First: occupation of each mode in the exact many-body eigenstates
# n_k(alpha) = 1 if bit k is set in state alpha, 0 otherwise
# <n_k>_thermal = sum_alpha p_alpha * n_k(alpha)

# Temperature from the GGE energy
# From W2-1: the GGE has specific lambda values. After thermalization,
# the energy is conserved. Let's find T from E(GGE) = <H>_Gibbs(T).

# Actually, let's compute the full thermal partition function and
# mode-resolved occupations as a function of beta.

beta_scan = np.array([0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 50.0])

print(f"\n  Thermal mode occupations vs temperature:")
print(f"  {'beta':>6} {'T':>6} {'<N_pair>':>10} " +
      " ".join(f"{'<n_'+str(branch_labels[k])+'>':>10}" for k in range(N)))
print(f"  {'-'*6} {'-'*6} {'-'*10} " + " ".join(['-'*10]*N))

thermal_data = {}
for beta in beta_scan:
    boltz = np.exp(-beta * (evals_full - evals_full[0]))
    Z = np.sum(boltz)
    probs = boltz / Z

    # <N_pair>
    npair_thermal = 0.0
    for alpha in range(dim_full):
        npair_thermal += probs[0] * np.abs(evecs_full[:, 0])**2  # wrong, need full
    # Correct: for each eigenstate, compute <N_pair> contribution
    # <N_pair> = sum_n p_n * <n|N_pair|n>
    # In pair Fock space, N_pair for state alpha = number of set bits
    npair_per_eigenstate = np.zeros(dim_full)
    for n_idx in range(dim_full):
        psi_n = evecs_full[:, n_idx]
        npair_per_eigenstate[n_idx] = sum(
            np.abs(psi_n[alpha])**2 * bin(alpha).count('1')
            for alpha in range(dim_full)
        )
    npair_thermal = np.sum(probs * npair_per_eigenstate)

    # Mode-resolved occupations: <n_k> for each mode k
    # n_k|alpha> = (bit k of alpha)|alpha>
    mode_occ = np.zeros(N)
    for k in range(N):
        nk_per_eigenstate = np.zeros(dim_full)
        for n_idx in range(dim_full):
            psi_n = evecs_full[:, n_idx]
            for alpha in range(dim_full):
                if alpha & (1 << k):
                    nk_per_eigenstate[n_idx] += np.abs(psi_n[alpha])**2
        mode_occ[k] = np.sum(probs * nk_per_eigenstate)

    # Probability of odd vs even total pair number
    p_even = 0.0
    p_odd = 0.0
    for n_idx in range(dim_full):
        psi_n = evecs_full[:, n_idx]
        for alpha in range(dim_full):
            np_val = bin(alpha).count('1')
            if np_val % 2 == 0:
                p_even += probs[n_idx] * np.abs(psi_n[alpha])**2
            else:
                p_odd += probs[n_idx] * np.abs(psi_n[alpha])**2

    thermal_data[beta] = {
        'npair': npair_thermal,
        'mode_occ': mode_occ.copy(),
        'p_even': p_even,
        'p_odd': p_odd,
    }

    T_val = 1.0 / beta
    print(f"  {beta:>6.1f} {T_val:>6.3f} {npair_thermal:>10.4f} " +
          " ".join(f"{mode_occ[k]:>10.6f}" for k in range(N)))

print(f"\n  Odd/even pair-number probabilities:")
print(f"  {'beta':>6} {'P(even)':>10} {'P(odd)':>10}")
for beta in beta_scan:
    td = thermal_data[beta]
    print(f"  {beta:>6.1f} {td['p_even']:>10.6f} {td['p_odd']:>10.6f}")

# ============================================================
# 6. QUASIPARTICLE WEIGHT IN POST-TRANSIT STATE
# ============================================================

print("\n" + "=" * 70)
print("POST-TRANSIT QUASIPARTICLE OCCUPATIONS")
print("=" * 70)

# From S38: 59.8 quasiparticle pairs, P_exc = 1.000
# The Bogoliubov coefficients at the fold give:
# n_k = v_k^2 (coherence factors from BCS ground state)
# After sudden quench: each mode independently has occupation v_k^2
# in the OLD basis, which maps to quasiparticle excitations.

print(f"\n  Bogoliubov coefficients at fold (from S39 data):")
print(f"  {'Mode':<8} {'u_k':>10} {'v_k':>10} {'n_k=v_k^2':>12} {'Delta_k':>12}")
print(f"  {'-'*8} {'-'*10} {'-'*10} {'-'*12} {'-'*12}")
for k in range(N):
    print(f"  {branch_labels[k]:<8} {u_k[k]:>10.6f} {v_k[k]:>10.6f} "
          f"{n_k[k]:>12.8f} {Delta_k[k]:>12.6f}")

# The probability that exactly one quasiparticle is in mode k (blocking)
# In the independent quasiparticle picture (post-quench):
# P(n_k = 1) = n_k for a single mode in the BCS-to-normal quench
# But this is pair occupation, not single-particle.
#
# For the pair Fock space: n_k is the probability that a PAIR occupies mode k.
# "Blocking" in the single-particle sense requires an odd number of electrons.
# In the pair representation, all states have even particle number.
#
# The transition to odd-particle states happens through:
# 1. Pair-breaking: a pair (k↑, k↓) breaks into two unpaired electrons
# 2. This is a quasiparticle excitation in BCS theory
# 3. The quasiparticle creation operator: gamma_k^dag = u_k * c_k^dag - v_k * c_{-k}
#
# In the post-transit BCS-to-normal quench (S38):
# Each mode has P_exc ~ 1.0 (complete excitation).
# The quasiparticle occupation number is n_k(qp) = v_k^2 in the OLD basis.
# This gives the weight of the mode in odd-particle configurations.

# For 4D mass spectrum: the blocked (odd-particle) states contribute
# with weight proportional to the Boltzmann factor exp(-beta * E_odd(k))
# in the thermal state.

# Estimate effective temperature from the total excitation energy
E_exc_total = float(d39.get('de1_dtau_fold', 0.0))  # Not exactly right

# Use the GGE energy as total energy, find matching thermal beta
# E_GGE = sum_k lambda_k * <n_k>_GGE
# From W2-1: p_k = |psi_pair[k]|^2 are the GGE occupations
psi_pair = d39['psi_pair_s38']
p_k = psi_pair**2  # pair wavefunction amplitudes squared (probabilities)
print(f"\n  Pair wavefunction amplitudes squared (GGE occupations):")
for k in range(N):
    print(f"    {branch_labels[k]}: p_k = {p_k[k]:.8f}")
print(f"  Sum p_k = {np.sum(p_k):.10f}")

# GGE energy
E_GGE = evals_full[0]  # Ground state energy (the GGE starts from ground state of H)
# Actually the GGE state has <H> = E_gs since it IS the ground state evolved
# After transit, energy is conserved if H doesn't change.
# But the transit changes tau, hence H changes.
# The post-transit energy is determined by the quench.

# From S38: E_exc = 443 * |E_cond|
E_cond = evals_full[0]  # condensation energy
E_exc_s38 = 443 * abs(E_cond)  # from S38 sudden quench
print(f"\n  E_cond = {E_cond:.6f}")
print(f"  E_exc (S38, 443x) = {E_exc_s38:.4f}")

# Find beta_eff such that <H>_Gibbs(beta) = E_gs + E_exc
E_target = E_exc_s38
print(f"\n  Searching for beta_eff matching E_target = {E_target:.4f}...")

from scipy.optimize import brentq

def E_thermal(beta_val):
    """Thermal energy <H> at inverse temperature beta."""
    if beta_val <= 0:
        return np.mean(evals_full)
    boltz = np.exp(-beta_val * (evals_full - evals_full[0]))
    Z = np.sum(boltz)
    return np.sum((boltz / Z) * evals_full)

# Scan to find bracket
E_hot = E_thermal(0.01)
E_cold = E_thermal(100.0)
print(f"  E(beta=0.01) = {E_hot:.4f}")
print(f"  E(beta=100) = {E_cold:.4f}")

if E_target > E_hot:
    print(f"  E_target > E(hot limit). Using beta_eff = 0.01 (essentially infinite T)")
    beta_eff = 0.01
elif E_target < E_cold:
    print(f"  E_target < E(cold limit). Using beta_eff = 100.0 (essentially T=0)")
    beta_eff = 100.0
else:
    beta_eff = brentq(lambda b: E_thermal(b) - E_target, 0.01, 100.0)

T_eff = 1.0 / beta_eff
print(f"  beta_eff = {beta_eff:.4f}, T_eff = {T_eff:.4f}")

# Compute thermal weights at beta_eff
boltz_eff = np.exp(-beta_eff * (evals_full - evals_full[0]))
Z_eff = np.sum(boltz_eff)
probs_eff = boltz_eff / Z_eff

# Thermal weight of odd-particle states at beta_eff
# Weight of blocking mode k: proportional to exp(-beta * delta_E(k))
# relative to the even-particle ground state
print(f"\n  Thermal (Gibbs) weights for odd-particle states at T_eff={T_eff:.4f}:")
print(f"  {'Mode':<8} {'delta_E':>10} {'exp(-b*dE)':>12} {'weight':>10}")
print(f"  {'-'*8} {'-'*10} {'-'*12} {'-'*10}")

boltz_odd = np.zeros(N)
for k in range(N):
    dE = results[k]['delta_E']
    boltz_odd[k] = np.exp(-beta_eff * dE)

Z_odd = np.sum(boltz_odd)
Z_total = 1.0 + Z_odd  # even (ground) + all odd configurations

for k in range(N):
    dE = results[k]['delta_E']
    w = boltz_odd[k] / Z_total
    print(f"  {branch_labels[k]:<8} {dE:>10.6f} {boltz_odd[k]:>12.6e} {w:>10.6f}")
    results[k]['thermal_weight'] = w

w_even = 1.0 / Z_total
print(f"\n  P(even particle number) = {w_even:.6f}")
print(f"  P(odd particle number)  = {1 - w_even:.6f}")

# ============================================================
# 7. 4D MASS SPECTRUM WITH BLOCKING
# ============================================================

print("\n" + "=" * 70)
print("4D MASS SPECTRUM INCLUDING BLOCKED STATES")
print("=" * 70)

# KK mass scale: M_KK = 1 / R_KK (internal radius)
# All energies are in units of M_KK.
# The mass spectrum: M/M_KK = sqrt(energy differences)
# For even states: mass set by pair excitation energies
# For odd states: mass set by quasiparticle (blocking) energies

print(f"\n  Configuration     | E_gs      | delta_E   | M/M_KK    | Weight (thermal)")
print(f"  {'-'*18}|{'-'*11}|{'-'*11}|{'-'*11}|{'-'*18}")

# Even ground state
print(f"  {'Even GS (N=2)':<18}| {evals_full[0]:>9.6f} | {0.0:>9.6f} | {0.0:>9.6f} | {w_even:>9.6f}")

# Even excited states (from pair susceptibility, S37)
# First pair excitation
omega_plus_s37 = float(d37['omega_plus'])  # pair addition energy
omega_minus_s37 = float(d37['omega_minus'])  # pair removal energy
print(f"  {'Pair add (N=4)':<18}| {evals_full[0]+omega_plus_s37:>9.6f} | {omega_plus_s37:>9.6f} "
      f"| {omega_plus_s37:>9.6f} | {'(thermal)':>9}")
print(f"  {'Pair rem (N=0)':<18}| {evals_full[0]+omega_minus_s37:>9.6f} | {omega_minus_s37:>9.6f} "
      f"| {omega_minus_s37:>9.6f} | {'(thermal)':>9}")

# Odd states (blocked)
for k in range(N):
    r = results[k]
    label = f"Odd {r['label']}"
    print(f"  {label:<18}| {r['E_odd']:>9.6f} | {r['delta_E']:>9.6f} "
          f"| {r['delta_E']:>9.6f} | {r['thermal_weight']:>9.6f}")

# ============================================================
# 8. CROSS-CHECKS
# ============================================================

print("\n" + "=" * 70)
print("CROSS-CHECKS")
print("=" * 70)

# Check 1: B2 modes should be nearly degenerate (SU(3) quartet)
delta_E_B2 = [results[k]['delta_E'] for k in range(4)]
spread_B2 = max(delta_E_B2) - min(delta_E_B2)
print(f"\n  1. B2 degeneracy:")
print(f"     delta_E(B2) = {delta_E_B2}")
print(f"     Spread: {spread_B2:.2e} (should be ~0 if SU(3) exact)")

# Check 2: B3 modes should be nearly degenerate (SU(3) triplet)
delta_E_B3 = [results[k]['delta_E'] for k in range(5, 8)]
spread_B3 = max(delta_E_B3) - min(delta_E_B3)
print(f"\n  2. B3 degeneracy:")
print(f"     delta_E(B3) = {delta_E_B3}")
print(f"     Spread: {spread_B3:.2e}")

# Check 3: delta_E vs BCS quasiparticle energy
print(f"\n  3. Blocking vs BCS quasiparticle energies:")
print(f"     {'Mode':<8} {'delta_E(exact)':>15} {'E_qp(BCS)':>12} {'Ratio':>8}")
for k in range(N):
    r = results[k]
    ratio = r['delta_E'] / r['E_qp_bcs'] if r['E_qp_bcs'] > 0 else np.nan
    print(f"     {r['label']:<8} {r['delta_E']:>15.8f} {r['E_qp_bcs']:>12.8f} {ratio:>8.4f}")

# Check 4: Sum rule -- sum of blocking energies related to condensation energy
sum_delta = sum(results[k]['delta_E'] for k in range(N))
print(f"\n  4. Sum of blocking energies: {sum_delta:.6f}")
print(f"     E_cond (= E_gs): {evals_full[0]:.6f}")
print(f"     Ratio sum_delta / |E_cond|: {sum_delta / abs(evals_full[0]):.4f}")

# Check 5: Verify pair-number conservation in blocked systems
print(f"\n  5. Pair number in blocked ground states:")
for k in range(N):
    r = results[k]
    print(f"     {r['label']}: <N_pair> = {r['npair_blocked']:.6f}")

# ============================================================
# 9. SAVE DATA
# ============================================================

print("\n" + "=" * 70)
print("SAVING DATA")
print("=" * 70)

save_dict = {
    # Input parameters
    'E_8': E_8,
    'V_phys': V_phys,
    'rho_8': rho_8,
    'mu': np.array(mu),
    'n_modes': np.array(N),
    'branch_labels': branch_labels,

    # Unblocked reference
    'E_gs_unblocked': np.array(evals_full[0]),
    'npair_gs_unblocked': np.array(npair_gs),
    'evals_unblocked': evals_full,

    # Blocking results per mode
    'delta_E': np.array([results[k]['delta_E'] for k in range(N)]),
    'E_gs_blocked': np.array([results[k]['E_gs_blocked'] for k in range(N)]),
    'E_odd': np.array([results[k]['E_odd'] for k in range(N)]),
    'E_qp_bcs': np.array([results[k]['E_qp_bcs'] for k in range(N)]),
    'gap_blocked': np.array([results[k]['gap_blocked'] for k in range(N)]),
    'npair_blocked': np.array([results[k]['npair_blocked'] for k in range(N)]),
    'M_max_blocked': np.array([results[k]['M_max_blocked'] for k in range(N)]),
    'E_3p': np.array([results[k]['E_3p'] for k in range(N)]),
    'E_1p': np.array([results[k]['E_1p'] for k in range(N)]),
    'Delta_3': np.array([delta_3[k] for k in range(N)]),
    'thermal_weight': np.array([results[k]['thermal_weight'] for k in range(N)]),

    # Three-point formula
    'Delta_OES_s37': np.array(Delta_OES_s37),
    'avg_Delta3_B2': np.array(avg_delta3_B2),

    # Thermal state data
    'beta_eff': np.array(beta_eff),
    'T_eff': np.array(T_eff),
    'P_even': np.array(w_even),
    'P_odd': np.array(1.0 - w_even),

    # Bogoliubov coefficients
    'u_k_fold': u_k,
    'v_k_fold': v_k,
    'n_k_fold': n_k,

    # Blocked spectra (first 20 eigenvalues per mode)
    **{f'evals_blocked_{k}': results[k]['evals_blocked'][:20] for k in range(N)},

    # Gate
    'gate_verdict': np.array(['INFO']),
}

np.savez('tier0-computation/s39_odd_blocking.npz', **save_dict)
print("  Saved: tier0-computation/s39_odd_blocking.npz")

# ============================================================
# 10. PLOT
# ============================================================

print("\nGenerating plots...")

fig, axes = plt.subplots(2, 2, figsize=(14, 11))

# Panel 1: Blocking energies for all 8 modes
ax = axes[0, 0]
modes_x = np.arange(N)
delta_E_all = [results[k]['delta_E'] for k in range(N)]
E_qp_all = [results[k]['E_qp_bcs'] for k in range(N)]
colors = ['#1f77b4']*4 + ['#ff7f0e'] + ['#2ca02c']*3
ax.bar(modes_x - 0.15, delta_E_all, width=0.3, color=colors, alpha=0.8, label='Exact blocking')
ax.bar(modes_x + 0.15, E_qp_all, width=0.3, color=colors, alpha=0.4,
       edgecolor='black', linewidth=0.5, label='BCS E_qp')
ax.set_xticks(modes_x)
ax.set_xticklabels([str(bl) for bl in branch_labels], fontsize=8)
ax.set_ylabel(r'$\delta E$ (units of $M_{KK}$)')
ax.set_title('Blocking Energy (Odd-Even Staggering)')
ax.legend(fontsize=8)
ax.axhline(y=Delta_OES_s37, color='red', linestyle='--', alpha=0.5, label=f'S37 OES={Delta_OES_s37:.3f}')
ax.legend(fontsize=7)

# Panel 2: Three-point mass formula
ax = axes[0, 1]
delta3_all = [delta_3[k] for k in range(N)]
ax.bar(modes_x, delta3_all, color=colors, alpha=0.8)
ax.axhline(y=Delta_OES_s37, color='red', linestyle='--', linewidth=2,
           label=f'S37 Delta_OES = {Delta_OES_s37:.4f}')
ax.set_xticks(modes_x)
ax.set_xticklabels([str(bl) for bl in branch_labels], fontsize=8)
ax.set_ylabel(r'$\Delta_3(k)$')
ax.set_title('Three-Point Mass Formula')
ax.legend(fontsize=8)

# Panel 3: Mass spectrum with blocking
ax = axes[1, 0]
# Even states
ax.axhline(y=0, color='black', linewidth=2, label='Even GS')
ax.axhline(y=omega_plus_s37, color='blue', linewidth=1.5, linestyle='--',
           alpha=0.6, label=f'Pair add: {omega_plus_s37:.3f}')
# Odd states
for k in range(N):
    dE = results[k]['delta_E']
    ax.axhline(y=dE, color=colors[k], linewidth=1.0, alpha=0.7)
    ax.text(0.02, dE + 0.01, f"{branch_labels[k]}", fontsize=7,
            color=colors[k], transform=ax.get_yaxis_transform())

ax.set_xlim(-0.5, 1.5)
ax.set_ylabel(r'$M / M_{KK}$')
ax.set_title('Mass Spectrum: Even + Odd States')
ax.legend(fontsize=7, loc='upper right')
ax.set_xticks([0, 1])
ax.set_xticklabels(['Even', 'Odd'])

# Panel 4: Thermal weights
ax = axes[1, 1]
w_all = [results[k]['thermal_weight'] for k in range(N)]
ax.bar(modes_x, w_all, color=colors, alpha=0.8)
ax.set_xticks(modes_x)
ax.set_xticklabels([str(bl) for bl in branch_labels], fontsize=8)
ax.set_ylabel('Thermal weight')
ax.set_title(f'Odd-particle weights at T_eff = {T_eff:.3f}')
ax.text(0.95, 0.95, f'P(even) = {w_even:.4f}\nP(odd) = {1-w_even:.4f}',
        transform=ax.transAxes, ha='right', va='top', fontsize=9,
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

fig.suptitle(f'ODD-39: Odd-Particle Blocking Computation (8 modes, {N} blocked configs)',
             fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig('tier0-computation/s39_odd_blocking.png', dpi=150, bbox_inches='tight')
print("  Saved: tier0-computation/s39_odd_blocking.png")

# ============================================================
# 11. SUMMARY TABLE
# ============================================================

print("\n" + "=" * 70)
print("SUMMARY TABLE")
print("=" * 70)

print(f"\n  {'Config':<18} {'E_gs':>10} {'delta_E':>10} {'M/M_KK':>10} {'Thermal wt':>12}")
print(f"  {'-'*18} {'-'*10} {'-'*10} {'-'*10} {'-'*12}")
print(f"  {'Even GS (Np=1)':<18} {evals_full[0]:>10.6f} {0.0:>10.6f} {0.0:>10.6f} {w_even:>12.6f}")
for k in range(N):
    r = results[k]
    print(f"  {'Odd '+r['label']:<18} {r['E_odd']:>10.6f} {r['delta_E']:>10.6f} "
          f"{r['delta_E']:>10.6f} {r['thermal_weight']:>12.6f}")
print(f"  {'Pair add':<18} {evals_full[0]+omega_plus_s37:>10.6f} {omega_plus_s37:>10.6f} "
      f"{omega_plus_s37:>10.6f} {'(Gibbs)':>12}")

print(f"\n  Three-point mass formula Delta_3:")
print(f"    B2 average: {avg_delta3_B2:.6f}")
print(f"    B1:         {delta_3[4]:.6f}")
print(f"    B3 average: {avg_delta3_B3:.6f}")
print(f"    S37 Delta_OES: {Delta_OES_s37:.6f}")

print(f"\n  Cross-checks:")
print(f"    B2 degeneracy spread: {spread_B2:.2e}")
print(f"    B3 degeneracy spread: {spread_B3:.2e}")
print(f"    beta_eff = {beta_eff:.4f}, T_eff = {T_eff:.4f}")

print(f"\n  Gate ODD-39: INFO (blocking spectrum computed for all 8 modes)")
print("\nDone.")
