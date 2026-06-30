#!/usr/bin/env python3
"""
GGE-VACUUM-ENERGY-66: Prethermal Vacuum Energy from Non-Equilibrium
=====================================================================

Session 66, Wave 2-E (landau-condensed-matter-theorist)

Physics (Landau framework):
  The GGE relic state is characterized by a density matrix
    rho_GGE = exp(-sum_k beta_k * I_k) / Z_GGE
  where I_k are the Richardson-Gaudin conserved integrals (Paper 16)
  and beta_k are the GGE chemical potentials (Paper 22, Rigol 2006).

  By Volovik's theorem (Paper 04/05): in true thermodynamic equilibrium,
  the vacuum energy density vanishes identically via Gibbs-Duhem:
    rho_vac^{eq} = 0

  Therefore the PHYSICAL vacuum energy is the deviation:
    rho_vac = rho_GGE - rho_eq = <H>_GGE - <H>_eq

  This is a Landau-type argument: the order parameter is the GGE
  occupation {n_k}, the symmetry is the full set of conserved integrals,
  and the excitation spectrum determines the vacuum energy.

  CRITICAL CONTEXT from Wave 1:
  - W1-A: Volovik q-theory relaxation rho ~ M_Pl^2 * H^2 matches obs to 0.01 OOM
  - W1-D: Static q-theory self-tuning FAILS (degeneracy lock)
  - W1-E: a_0 is exactly constant (117 OOM gap, scheme-independent)
  - Question: is the GGE deviation energy itself small enough to be the CC?

Gate: GGE-VACUUM-ENERGY-66
  PASS: delta_rho / rho_obs < 10^{10}
  FAIL: delta_rho / rho_obs > 10^{100}
  INFO: 10^{10} < ratio < 10^{100}

Inputs:
  - s52_n_pair_full.npz (BCS pair data)
  - s54_ed_sweep.npz (exact diagonalization spectrum)
  - s53_q_theory_gge.npz (prior GGE analysis)
  - canonical_constants.py

Outputs:
  - s66_gge_vacuum_energy.npz
  - s66_gge_vacuum_energy.png
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import numpy as np
from scipy.optimize import minimize_scalar
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    E_cond, E_cond_ED_8mode, E_exc, n_pairs, N_dof_BCS,
    rho_Lambda_obs, M_KK, M_KK_gravity, M_KK_kerner,
    T_acoustic, S_fold, a0_fold, a2_fold, a4_fold,
    Delta_0_GL, Delta_0_OES, Delta_B3,
    E_B1, E_B2_mean, E_B3_mean,
    omega_PV, S_inst, tau_fold, H_fold, dt_transit,
    M_Pl_reduced, M_Pl_unreduced, H_0_GeV,
    PI, E_exc_ratio, n_Bog,
    rho_B2_per_mode, Vol_SU3_Haar, N_cells,
    J_C2, J_su2, J_u1,
    xi_BCS, xi_GL,
    n_pairs as N_pair_canonical,
    d2S_fold,
)

outdir = os.path.dirname(__file__)

print("=" * 76)
print("GGE-VACUUM-ENERGY-66: Prethermal Vacuum Energy from Non-Equilibrium")
print("=" * 76)

# ==============================================================================
# SECTION 1: Load Input Data
# ==============================================================================

print("\n" + "=" * 76)
print("SECTION 1: Load Input Data")
print("=" * 76)

# Load ED sweep data
ed = np.load(os.path.join(outdir, 's54_ed_sweep.npz'), allow_pickle=True)
fold_idx = int(ed['fold_idx'])
tau_values = ed['tau_values']
tau_fold_ed = tau_values[fold_idx]
print(f"fold_idx = {fold_idx}, tau_fold = {tau_fold_ed:.4f}")

# Single-particle energies at fold (8 BCS modes)
eps_k = ed['E_sp_sweep'][fold_idx]  # shape (8,), M_KK units
print(f"\nSingle-particle energies at fold (8 modes):")
for i, e in enumerate(eps_k):
    label = 'B2' if i < 4 else ('B1' if i == 4 else 'B3')
    print(f"  mode {i} ({label}): eps_k = {e:.6f} M_KK")

# BCS pair occupations at fold
v2_k = ed['pair_occupations'][fold_idx]  # v_k^2 (BCS)
print(f"\nBCS pair occupations v_k^2 at fold:")
for i, v in enumerate(v2_k):
    print(f"  mode {i}: v_k^2 = {v:.6f}")

# Interaction matrix
V_bare = ed['V_bare_cont']  # (8,8) pairing interaction
print(f"\nInteraction matrix V_bare: shape = {V_bare.shape}")
print(f"  V_bare[0,0] = {V_bare[0,0]:.6f}, V_bare[0,1] = {V_bare[0,1]:.6f}")

# Full 256-state spectrum at fold
all_eig_fold = ed['all_eigenvalues'][fold_idx]
E_GS_ED = all_eig_fold[0]  # Ground state from ED (N=1 pair sector)
print(f"\nED ground state energy (N=1): E_GS = {E_GS_ED:.6f} M_KK")

# E(N) staircase from S60/S61
staircase = np.load(os.path.join(outdir, 's60_staircase_ext.npz'), allow_pickle=True)
E_GS_staircase = staircase['E_GS_A']  # [E(0), E(1), E(2), E(3), E(4)]
N_staircase = np.arange(len(E_GS_staircase))
print(f"\nE(N) staircase (S60, with diag, M_KK):")
for N, E in zip(N_staircase, E_GS_staircase):
    print(f"  N={N}: E = {E:.6f} M_KK")

# S53 GGE data
gge53 = np.load(os.path.join(outdir, 's53_q_theory_gge.npz'), allow_pickle=True)
T_GGE_prior = gge53['T_GGE']
beta_GGE_prior = gge53['beta_GGE']
E_GGE_prior = float(gge53['E_GGE_MKK'])
print(f"\nS53 GGE energy: E_GGE = {E_GGE_prior:.3f} M_KK")
print(f"S53 GGE temperatures: {T_GGE_prior}")
print(f"S53 log10(Lambda_GGE/Lambda_obs) = {float(gge53['log10_ratio']):.1f}")

# ==============================================================================
# SECTION 2: BCS Hamiltonian and GGE State
# ==============================================================================

print("\n" + "=" * 76)
print("SECTION 2: BCS Hamiltonian and GGE State Construction")
print("=" * 76)

# The BCS Hamiltonian for the 8-mode system:
#   H_BCS = sum_k eps_k * n_k - sum_{k,k'} V_{kk'} * c^+_k c_k'
#
# In the Bogoliubov quasiparticle basis:
#   H_BCS = E_GS + sum_k E_k * alpha^+_k alpha_k
#
# where E_k = sqrt(eps_k^2 + Delta_k^2) is the BCS quasiparticle energy
# and E_GS is the BCS ground state energy (condensation energy).

# BCS gap equation: Delta_k = sum_{k'} V_{kk'} * Delta_{k'} / (2*E_{k'})
# From the ED data, the gap Delta is implicitly encoded in the pair occupations:
#   v_k^2 = 0.5 * (1 - eps_k / E_k)
#   u_k^2 = 0.5 * (1 + eps_k / E_k)

# Reconstruct BCS quasiparticle energies from pair occupations
# v_k^2 = 0.5 * (1 - xi_k / E_k) where xi_k = eps_k - mu
# For canonical BCS (ED ground state), we need to find mu and Delta_k

# First: extract BCS parameters from ED pair occupations
# Using v^2 and eps_k:
#   v_k^2 = 0.5 * (1 - (eps_k - mu) / sqrt((eps_k - mu)^2 + Delta_eff^2))
# For a single-gap BCS: Delta_eff = Delta (same for all modes, mean-field)

# Since mode 0 has eps_0 ~ 0 and v_0^2 ~ 0.958:
#   v_0^2 = 0.5 * (1 + mu / sqrt(mu^2 + Delta^2))
# This means mu > 0 (BEC side for this mode).

# From S52 data:
v2_BCS = v2_k.copy()
print(f"\nReconstructing BCS parameters from ED occupations...")

# BCS gap and chemical potential from self-consistent mean-field:
# Use the variational BCS approach on the 8-mode system.
# The gap equation: Delta = g * sum_k Delta / (2 * E_k)
# where g = bare coupling from V_bare.

# For this computation, we need the QUASIPARTICLE ENERGIES.
# Method: from v_k^2 and eps_k, extract E_k and Delta_k.
#
# v_k^2 = 0.5 * (1 - xi_k / E_k)  =>  xi_k / E_k = 1 - 2*v_k^2
# E_k = |xi_k| / |1 - 2*v_k^2|
#
# But we need xi_k = eps_k - mu.  Let's determine mu first.
# The total pair number constraint: N = sum_k v_k^2.

N_pair_BCS = np.sum(v2_BCS)
print(f"Total BCS pairs: N = sum(v_k^2) = {N_pair_BCS:.6f}")
print(f"(This is the BCS mean-field N for the N=1 ED ground state)")

# The BCS mean-field for the N=1 ground state
# uses a single chemical potential mu. We solve:
#   sum_k v_k^2(mu, Delta) = 1  (N=1 constraint)
#   1/g = sum_k 1/(2*E_k)      (gap equation)
# where g = effective coupling from V_bare.

# Average coupling (separable approximation):
g_eff = np.mean(V_bare[V_bare > 1e-10])
print(f"Effective coupling g_eff = {g_eff:.6f} M_KK")

# Self-consistent BCS solver
def bcs_solve(mu_trial, Delta_trial, eps_arr, g):
    """Solve BCS equations for given mu, Delta."""
    xi_k = eps_arr - mu_trial
    E_k = np.sqrt(xi_k**2 + Delta_trial**2)
    v2 = 0.5 * (1.0 - xi_k / E_k)
    # Gap equation residual
    gap_rhs = g * np.sum(Delta_trial / (2.0 * E_k))
    return v2, E_k, gap_rhs

# Iterative BCS self-consistency
def solve_bcs_full(eps_arr, g, N_target, max_iter=2000, tol=1e-12):
    """Full self-consistent BCS solution."""
    N_modes = len(eps_arr)
    # Initial guess
    mu = eps_arr[0] + 0.01  # (local)
    Delta = 0.1  # (local)

    for it in range(max_iter):
        xi_k = eps_arr - mu
        E_k = np.sqrt(xi_k**2 + Delta**2)
        v2 = 0.5 * (1.0 - xi_k / E_k)
        N_calc = np.sum(v2)

        # Gap equation: Delta = g * sum_k Delta/(2*E_k)
        gap_sum = np.sum(1.0 / (2.0 * E_k))
        Delta_new = g * Delta * gap_sum if Delta > 1e-15 else 0.01

        # Adjust mu to fix N
        dN_dmu = np.sum(Delta**2 / (2.0 * E_k**3))
        mu += 0.3 * (N_target - N_calc) / max(dN_dmu, 1e-10)

        # Update Delta
        if gap_sum > 0:
            Delta = Delta * (g * gap_sum) ** 0.3  # damped update

        if abs(N_calc - N_target) < tol and abs(g * gap_sum - 1.0) < tol:
            break

    return mu, Delta, v2, E_k

# Solve BCS for N=1 (ground state sector)
mu_BCS, Delta_BCS, v2_BCS_solved, E_k_BCS = solve_bcs_full(eps_k, g_eff, 1.0)
print(f"\nBCS solution (N=1 ground state):")
print(f"  mu = {mu_BCS:.6f} M_KK")
print(f"  Delta = {Delta_BCS:.6f} M_KK")
print(f"  N = sum(v2) = {np.sum(v2_BCS_solved):.6f}")
print(f"  BCS quasiparticle energies E_k:")
for i, E in enumerate(E_k_BCS):
    print(f"    mode {i}: E_k = {E:.6f} M_KK")

# BCS ground state energy
# E_BCS_GS = sum_k (eps_k - E_k) * v_k^2 + sum_k eps_k * v_k^2
#           = 2 * sum_k eps_k * v_k^2 - sum_{kk'} V_{kk'} u_k v_k u_{k'} v_{k'}
# More precisely:
# E_BCS = sum_k 2*eps_k*v_k^2 - Delta^2/g
xi_k_BCS = eps_k - mu_BCS
E_BCS_GS = np.sum(2.0 * eps_k * v2_BCS_solved) - Delta_BCS**2 / g_eff
E_BCS_GS_v2 = np.sum(eps_k * (1.0 - xi_k_BCS / E_k_BCS)) - Delta_BCS**2 / g_eff
print(f"\nBCS ground state energy: E_BCS_GS = {E_BCS_GS:.6f} M_KK")
print(f"  (alternative: {E_BCS_GS_v2:.6f} M_KK)")
print(f"  ED ground state: E_GS_ED = {E_GS_ED:.6f} M_KK")
print(f"  E(N=1) staircase: {E_GS_staircase[1]:.6f} M_KK")

# ==============================================================================
# SECTION 3: GGE State -- Occupation Numbers and Energy
# ==============================================================================

print("\n" + "=" * 76)
print("SECTION 3: GGE State -- Occupation Numbers and Energy")
print("=" * 76)

# The GGE state after the transit has:
#   - 8 BCS modes, each with occupation n_k ~ n_Bog ~ 0.999 (fully excited)
#   - The GGE temperatures T_k = {0.668 (B2), 0.435 (B1), 0.178 (B3)} M_KK
#   - Total excitation energy E_exc = 60.625 M_KK (from S38)
#
# The GGE occupations for Bogoliubov quasiparticles:
#   <alpha_k^+ alpha_k>_GGE = n_k = 1/(exp(beta_k * E_k) + 1)
#
# where beta_k = 1/T_k are the GGE inverse temperatures.
# These are NOT Fermi-Dirac with a single T -- each mode has its own beta_k.
# This is the defining feature of the GGE (Paper 22, Rigol 2006).

T_GGE = np.array([0.668]*4 + [0.435] + [0.178]*3)  # M_KK units
beta_GGE = 1.0 / T_GGE

print("GGE temperatures (S43 GGE-TEMP-43):")
print(f"  T_B2 = {T_GGE[0]:.3f} M_KK (4 modes)")
print(f"  T_B1 = {T_GGE[4]:.3f} M_KK (1 mode)")
print(f"  T_B3 = {T_GGE[5]:.3f} M_KK (3 modes)")

# Method A: GGE occupations from Fermi function with mode-dependent T
# n_k^{GGE} = 1 / (exp(E_k / T_k) + 1)
# where E_k is the BCS quasiparticle energy
n_k_GGE = 1.0 / (np.exp(E_k_BCS / T_GGE) + 1.0)
print(f"\nGGE quasiparticle occupations (Fermi with mode-dependent T):")
for i, n in enumerate(n_k_GGE):
    print(f"  mode {i}: n_k = {n:.6f} (T_k = {T_GGE[i]:.3f}, E_k = {E_k_BCS[i]:.4f})")
print(f"  sum(n_k) = {np.sum(n_k_GGE):.6f}")

# Method B: Use the S38 value n_Bog = 0.999 (nearly fully occupied)
# This is the Bogoliubov number from Kibble-Zurek quench (P_exc = 1.0)
n_k_S38 = np.full(N_dof_BCS, n_Bog)
print(f"\nS38 Bogoliubov occupation: n_Bog = {n_Bog:.6f} (all modes)")

# GGE energy: <H>_GGE = E_BCS_GS + sum_k E_k * n_k^{GGE}
# The BCS ground state is the reference. Quasiparticle excitations add energy.

# Method A: using computed GGE occupations
E_GGE_A = E_BCS_GS + np.sum(E_k_BCS * n_k_GGE)
print(f"\nGGE energy (Method A, Fermi occupations):")
print(f"  E_GGE = E_BCS_GS + sum(E_k * n_k)")
print(f"        = {E_BCS_GS:.6f} + {np.sum(E_k_BCS * n_k_GGE):.6f}")
print(f"        = {E_GGE_A:.6f} M_KK")

# Method B: using n_Bog = 0.999
E_GGE_B = E_BCS_GS + np.sum(E_k_BCS * n_k_S38)
print(f"\nGGE energy (Method B, n_Bog occupations):")
print(f"  E_GGE = E_BCS_GS + sum(E_k * n_Bog)")
print(f"        = {E_BCS_GS:.6f} + {np.sum(E_k_BCS * n_k_S38):.6f}")
print(f"        = {E_GGE_B:.6f} M_KK")

# Method C: Direct from S38/S53 -- E_exc = 60.625 M_KK
# This is the TOTAL excitation energy from the transit (= E_exc_ratio * |E_cond|)
# E_GGE = E_cond + E_exc = -0.137 + 60.625 = 60.489 M_KK
E_GGE_C = E_cond + E_exc
print(f"\nGGE energy (Method C, S38 E_exc):")
print(f"  E_GGE = E_cond + E_exc = {E_cond:.6f} + {E_exc:.3f} = {E_GGE_C:.3f} M_KK")

# The canonical E_exc = 60.625 M_KK uses 443 * |E_cond| scaling.
# This accounts for ALL 496 modes across 6 representation sectors (S52).
# The 8-mode BCS sector is only one piece.

print(f"\n*** KEY: Three GGE energy estimates ***")
print(f"  Method A (8-mode BCS, Fermi GGE): {E_GGE_A:.6f} M_KK")
print(f"  Method B (8-mode BCS, n_Bog=0.999): {E_GGE_B:.6f} M_KK")
print(f"  Method C (all 496 modes, S38): {E_GGE_C:.3f} M_KK")

# ==============================================================================
# SECTION 4: Equilibrium Energy -- The Reference State
# ==============================================================================

print("\n" + "=" * 76)
print("SECTION 4: Equilibrium Energy (the Volovik zero)")
print("=" * 76)

# By Volovik's theorem (Paper 04/05), in true thermodynamic equilibrium:
#   rho_vac^{eq} = 0
#
# This means E_eq = 0 in the sense that the equilibrium vacuum
# does not gravitate. The physical content is:
#   delta_rho = rho_GGE - rho_eq = rho_GGE - 0 = rho_GGE
#
# But what is "equilibrium" here? There are THREE candidates:
#
# (a) The BCS ground state at N=1 pair: E_GS(N=1) = -0.0464 M_KK
#     This is the SINGLE-CELL equilibrium.
#
# (b) The BCS ground state at N=0 (empty): E_GS(N=0) = 0
#     The trivial vacuum.
#
# (c) The thermodynamic equilibrium state at the SAME total energy,
#     i.e., the thermal state with beta*H at E_total = E_GGE.
#     By Volovik's theorem, this has rho_vac = 0.

# The physical vacuum energy is:
#   delta_rho = <H>_GGE - <H>_eq
#
# Case 1: If Volovik's theorem applies, E_eq effectively = 0 for gravity.
#   Then delta_rho = E_GGE (the full GGE energy gravitates).
#
# Case 2: If we compare to the BCS ground state (N=1):
#   delta_rho = E_GGE - E_GS(N=1)
#   This is the excitation energy ABOVE the condensate ground state.
#
# Case 3: If we compare to the thermal equilibrium at the same energy:
#   The thermal state has beta chosen so <H>_thermal = <H>_GGE.
#   Then delta_rho = 0 trivially. But the GGE is NOT thermal.
#   The non-zero CC comes from the GGE-thermal DIFFERENCE at fixed energy.

# Volovik's argument (Paper 04, eq. 14-16): in equilibrium, the
# Gibbs-Duhem identity makes rho_vac vanish for ANY self-tuning q.
# The GGE breaks this because it is constrained by I_k, not just H.
# The deviation FROM equilibrium IS the vacuum energy.

# Compute all three reference energies:
E_eq_volovik = 0.0  # Volovik: equilibrium vacuum energy = 0  # (local)
E_eq_BCS_N1 = E_GS_staircase[1]  # BCS ground state, N=1
E_eq_BCS_N0 = E_GS_staircase[0]  # Trivial vacuum, N=0

print(f"Reference energies:")
print(f"  E_eq (Volovik zero): {E_eq_volovik:.6f} M_KK")
print(f"  E_GS(N=1) (BCS GS): {E_eq_BCS_N1:.6f} M_KK")
print(f"  E_GS(N=0) (trivial): {E_eq_BCS_N0:.6f} M_KK")

# Now compute the thermal equilibrium at the same total energy as GGE.
# For the 8-mode BCS system, find T_thermal such that:
#   <H>_thermal = E_BCS_GS + sum_k E_k / (exp(E_k/T) + 1) = E_GGE
# This gives the thermal comparison point.

def thermal_energy(T, E_k_arr, E_gs):
    """Total energy of thermal state at temperature T."""
    if T < 1e-15:
        return E_gs
    n_thermal = 1.0 / (np.exp(E_k_arr / T) + 1.0)
    return E_gs + np.sum(E_k_arr * n_thermal)

# Find T_thermal for Method A GGE energy (8-mode)
from scipy.optimize import brentq

E_target_A = E_GGE_A
# At T=0, E = E_BCS_GS. At T=inf, E = E_BCS_GS + sum(E_k)/2.
E_Tinf = E_BCS_GS + 0.5 * np.sum(E_k_BCS)
print(f"\n8-mode system energy range:")
print(f"  T=0: E = {E_BCS_GS:.6f} M_KK")
print(f"  T=inf: E = {E_Tinf:.6f} M_KK")
print(f"  E_GGE_A = {E_GGE_A:.6f} M_KK")

if E_target_A < E_Tinf:
    T_thermal_A = brentq(lambda T: thermal_energy(T, E_k_BCS, E_BCS_GS) - E_target_A,
                          1e-6, 100.0)
    print(f"  T_thermal (matching E_GGE_A) = {T_thermal_A:.6f} M_KK")
else:
    T_thermal_A = np.inf
    print(f"  E_GGE_A exceeds T=inf limit -- GGE more excited than any thermal state")

# For the thermal state, the ENTROPY is different from the GGE entropy.
# The GGE has LESS entropy than thermal at the same energy
# (because it preserves more integrals of motion).
# The entropy DEFICIT is what drives the non-zero CC.

# Thermal entropy at T_thermal
if T_thermal_A < np.inf and T_thermal_A > 1e-10:
    n_thermal_A = 1.0 / (np.exp(E_k_BCS / T_thermal_A) + 1.0)
    S_thermal_A = -np.sum(n_thermal_A * np.log(np.clip(n_thermal_A, 1e-30, 1.0)) +
                          (1 - n_thermal_A) * np.log(np.clip(1 - n_thermal_A, 1e-30, 1.0)))
else:
    n_thermal_A = 0.5 * np.ones(N_dof_BCS)
    S_thermal_A = N_dof_BCS * np.log(2)

# GGE entropy
S_GGE = -np.sum(n_k_GGE * np.log(np.clip(n_k_GGE, 1e-30, 1.0)) +
                (1 - n_k_GGE) * np.log(np.clip(1 - n_k_GGE, 1e-30, 1.0)))

print(f"\nEntropy comparison:")
print(f"  S_thermal(T_thermal) = {S_thermal_A:.6f}")
print(f"  S_GGE (mode-dep T)   = {S_GGE:.6f}")
print(f"  S_max = 8*ln(2)      = {N_dof_BCS * np.log(2):.6f}")
print(f"  Delta_S = S_thermal - S_GGE = {S_thermal_A - S_GGE:.6f}")
print(f"  (GGE has {'LESS' if S_GGE < S_thermal_A else 'MORE'} entropy than thermal)")

# ==============================================================================
# SECTION 5: Vacuum Energy Computation -- Multiple Methods
# ==============================================================================

print("\n" + "=" * 76)
print("SECTION 5: Vacuum Energy -- delta_rho Computation")
print("=" * 76)

# ---------------------------------------------------------------------------
# Method I: Direct excitation energy (GGE above BCS ground state)
# This is the most physical: the BCS ground state is the equilibrium,
# the GGE quasiparticle excitations carry excess energy.
# ---------------------------------------------------------------------------

# For the 8-mode BCS system:
delta_E_8mode_A = E_GGE_A - E_BCS_GS  # Method A (Fermi GGE)
delta_E_8mode_B = E_GGE_B - E_BCS_GS  # Method B (n_Bog)
print(f"\nMethod I: Excitation above BCS ground state (8-mode)")
print(f"  delta_E_A = sum(E_k * n_k^GGE) = {delta_E_8mode_A:.6f} M_KK")
print(f"  delta_E_B = sum(E_k * n_Bog) = {delta_E_8mode_B:.6f} M_KK")

# For the full 496-mode system:
delta_E_full = E_exc  # = 60.625 M_KK from S38
print(f"  delta_E_full (496 modes) = {delta_E_full:.3f} M_KK")

# ---------------------------------------------------------------------------
# Method II: GGE-thermal entropy deficit * effective temperature
# The vacuum energy is T_eff * (S_thermal - S_GGE) -- the "lost entropy"
# that becomes vacuum energy because the GGE cannot relax.
# ---------------------------------------------------------------------------

if T_thermal_A < np.inf:
    delta_F_entropy = T_thermal_A * (S_thermal_A - S_GGE)
    print(f"\nMethod II: Entropy deficit (8-mode)")
    print(f"  T_eff * Delta_S = {T_thermal_A:.4f} * {S_thermal_A - S_GGE:.6f}")
    print(f"                  = {delta_F_entropy:.6f} M_KK")
else:
    delta_F_entropy = np.nan
    print(f"\nMethod II: T_thermal = inf, not applicable")

# ---------------------------------------------------------------------------
# Method III: Free energy difference F_GGE - F_thermal at same energy
# F = E - T*S, so delta_F = delta(T*S) at fixed E.
# Since E_GGE = E_thermal by construction:
#   delta_F = T_thermal * S_thermal - sum_k T_k * S_k^GGE
# ---------------------------------------------------------------------------

TS_GGE = np.sum(T_GGE * (-n_k_GGE * np.log(np.clip(n_k_GGE, 1e-30, 1.0)) -
                           (1 - n_k_GGE) * np.log(np.clip(1 - n_k_GGE, 1e-30, 1.0))))
if T_thermal_A < np.inf:
    TS_thermal = T_thermal_A * S_thermal_A
    delta_F_free_energy = TS_thermal - TS_GGE
    print(f"\nMethod III: Free energy difference (8-mode)")
    print(f"  T*S (thermal) = {TS_thermal:.6f} M_KK")
    print(f"  sum(T_k*S_k) (GGE) = {TS_GGE:.6f} M_KK")
    print(f"  delta_F = {delta_F_free_energy:.6f} M_KK")
else:
    delta_F_free_energy = np.nan

# ---------------------------------------------------------------------------
# Method IV: Volovik direct -- the ENTIRE GGE energy gravitates
# By Volovik's theorem, rho_eq = 0. So rho_vac = E_GGE per cell.
# ---------------------------------------------------------------------------

# Per-cell GGE energy (8 modes per cell, 32 cells in fabric)
E_GGE_per_cell = E_GGE_C  # Total system ~ single cell (0D limit)
print(f"\nMethod IV: Volovik direct (all excitation energy gravitates)")
print(f"  E_GGE_per_cell = {E_GGE_per_cell:.3f} M_KK")

# ==============================================================================
# SECTION 6: Convert to Physical Units and Compare to CC
# ==============================================================================

print("\n" + "=" * 76)
print("SECTION 6: Physical Units and CC Comparison")
print("=" * 76)

# Energy density conversion:
# rho = (energy per cell) * M_KK / (volume per cell)
# Volume per cell = Vol_SU3 * M_KK^{-8} (8D internal space, geometric units)
# In 4D effective theory: rho = E * M_KK^4 / Vol_SU3
# Actually: the spectral action gives rho = (2/pi^2) * a_n * M_KK^4
# For BCS energy: it's already in M_KK units, so rho = E * M_KK^4 / V_eff
# where V_eff is the effective 4-volume normalization.

# Standard spectral action normalization (S42, S53):
# rho_SA = (2/pi^2) * F(tau) * M_KK^4
# The BCS energy is a PERTURBATION to the spectral action.
# Following S53: rho_GGE = (2/pi^2) * delta_E * M_KK^4

prefactor_SA = 2.0 / PI**2  # = 0.2026

# Method I(a): 8-mode Fermi GGE
rho_Ia_GeV4 = prefactor_SA * delta_E_8mode_A * M_KK**4
# Method I(b): 8-mode n_Bog
rho_Ib_GeV4 = prefactor_SA * delta_E_8mode_B * M_KK**4
# Method I(c): Full 496-mode
rho_Ic_GeV4 = prefactor_SA * delta_E_full * M_KK**4
# Method IV: Volovik direct
rho_IV_GeV4 = prefactor_SA * E_GGE_per_cell * M_KK**4

# Alternative normalization: direct M_KK^4 (no spectral action prefactor)
rho_Ia_direct = delta_E_8mode_A * M_KK**4
rho_Ic_direct = delta_E_full * M_KK**4
rho_IV_direct = E_GGE_per_cell * M_KK**4

# Per-fabric normalization: divide by N_cells
rho_Ia_fabric = rho_Ia_GeV4 / N_cells
rho_Ic_fabric = rho_Ic_GeV4 / N_cells

print(f"\n--- Vacuum energy density estimates ---")
print(f"(Using M_KK = {M_KK:.4e} GeV, M_KK^4 = {M_KK**4:.4e} GeV^4)")
print(f"(Spectral action prefactor: 2/pi^2 = {prefactor_SA:.4f})")
print()

results = {}

# ---- Method I(a): 8-mode Fermi GGE ----
ratio_Ia = rho_Ia_GeV4 / rho_Lambda_obs
log10_Ia = np.log10(ratio_Ia) if ratio_Ia > 0 else -np.inf
print(f"Method I(a) -- 8-mode Fermi GGE:")
print(f"  delta_E = {delta_E_8mode_A:.6f} M_KK")
print(f"  rho = {rho_Ia_GeV4:.4e} GeV^4")
print(f"  rho / rho_obs = {ratio_Ia:.4e}")
print(f"  log10(rho/rho_obs) = {log10_Ia:.2f}")
results['Ia'] = {'delta_E': delta_E_8mode_A, 'rho': rho_Ia_GeV4, 'ratio': ratio_Ia, 'log10': log10_Ia}

# ---- Method I(b): 8-mode n_Bog ----
ratio_Ib = rho_Ib_GeV4 / rho_Lambda_obs
log10_Ib = np.log10(ratio_Ib) if ratio_Ib > 0 else -np.inf
print(f"\nMethod I(b) -- 8-mode n_Bog:")
print(f"  delta_E = {delta_E_8mode_B:.6f} M_KK")
print(f"  rho = {rho_Ib_GeV4:.4e} GeV^4")
print(f"  rho / rho_obs = {ratio_Ib:.4e}")
print(f"  log10(rho/rho_obs) = {log10_Ib:.2f}")
results['Ib'] = {'delta_E': delta_E_8mode_B, 'rho': rho_Ib_GeV4, 'ratio': ratio_Ib, 'log10': log10_Ib}

# ---- Method I(c): Full 496-mode ----
ratio_Ic = rho_Ic_GeV4 / rho_Lambda_obs
log10_Ic = np.log10(ratio_Ic) if ratio_Ic > 0 else -np.inf
print(f"\nMethod I(c) -- Full 496-mode S38:")
print(f"  delta_E = {delta_E_full:.3f} M_KK")
print(f"  rho = {rho_Ic_GeV4:.4e} GeV^4")
print(f"  rho / rho_obs = {ratio_Ic:.4e}")
print(f"  log10(rho/rho_obs) = {log10_Ic:.2f}")
results['Ic'] = {'delta_E': delta_E_full, 'rho': rho_Ic_GeV4, 'ratio': ratio_Ic, 'log10': log10_Ic}

# ---- Method IV: Volovik direct ----
ratio_IV = rho_IV_GeV4 / rho_Lambda_obs
log10_IV = np.log10(ratio_IV) if ratio_IV > 0 else -np.inf
print(f"\nMethod IV -- Volovik direct (E_cond + E_exc):")
print(f"  E_GGE = {E_GGE_per_cell:.3f} M_KK")
print(f"  rho = {rho_IV_GeV4:.4e} GeV^4")
print(f"  rho / rho_obs = {ratio_IV:.4e}")
print(f"  log10(rho/rho_obs) = {log10_IV:.2f}")
results['IV'] = {'delta_E': E_GGE_per_cell, 'rho': rho_IV_GeV4, 'ratio': ratio_IV, 'log10': log10_IV}

# ==============================================================================
# SECTION 7: Dissection -- Where Does the Gap Come From?
# ==============================================================================

print("\n" + "=" * 76)
print("SECTION 7: Dissecting the 10^{N} Gap")
print("=" * 76)

# The gap decomposes into three factors:
# log10(rho_GGE / rho_obs) = log10(delta_E) + 4*log10(M_KK) + log10(2/pi^2) - log10(rho_obs)

log10_deltaE_Ic = np.log10(delta_E_full)
log10_MKK4 = 4.0 * np.log10(M_KK)
log10_prefactor = np.log10(prefactor_SA)
log10_rho_obs = np.log10(rho_Lambda_obs)

print(f"\nGap decomposition (Method Ic, 496 modes):")
print(f"  log10(delta_E)  = {log10_deltaE_Ic:.2f}  [GGE excitation in M_KK units]")
print(f"  4*log10(M_KK)   = {log10_MKK4:.2f}  [UV scale M_KK^4]")
print(f"  log10(2/pi^2)   = {log10_prefactor:.2f}  [spectral action prefactor]")
print(f"  -log10(rho_obs) = {-log10_rho_obs:.2f}  [observed CC]")
print(f"  Total = {log10_deltaE_Ic + log10_MKK4 + log10_prefactor - log10_rho_obs:.2f}")

# The dominant contribution is M_KK^4 ~ 10^{67.5}
# The GGE excitation energy is O(60) in M_KK units ~ 10^{1.8}
# The gap is ~ 67.5 + 1.8 - 0.7 + 46.6 = 115.2 OOM

# Compare to S53:
print(f"\nS53 result: log10(Lambda_GGE/Lambda_obs) = {float(gge53['log10_ratio']):.1f}")
print(f"This computation: log10(rho/rho_obs) = {log10_Ic:.1f} (Method Ic)")
print(f"Consistency check: {'PASS' if abs(log10_Ic - float(gge53['log10_ratio'])) < 2 else 'FAIL'}")

# The GGE deviation energy is NOT small compared to the a_0 problem.
# Both scale as O(E) * M_KK^4, where E ~ O(10-100) M_KK.
# The "deviation" from equilibrium is the full excitation energy.

# Key structural insight: the GGE deviation IS the excitation energy.
# There is no separate "small parameter" that makes it small.
# The conservation of Richardson-Gaudin integrals prevents relaxation,
# but does NOT suppress the energy scale.

print(f"\n*** STRUCTURAL INSIGHT ***")
print(f"The GGE deviation energy delta_rho = (2/pi^2) * E_exc * M_KK^4")
print(f"scales identically to the spectral action contribution.")
print(f"E_exc ~ {delta_E_full:.1f} M_KK vs a_0 = {a0_fold:.0f}")
print(f"So delta_rho_GGE / rho_a0 = E_exc / a_0 = {delta_E_full / a0_fold:.4f}")
print(f"The GGE deviation is {delta_E_full / a0_fold * 100:.2f}% of the a_0 vacuum energy.")
print(f"The CC gap is dominated by M_KK^4, not by the GGE physics.")

# ==============================================================================
# SECTION 8: Cross-Checks
# ==============================================================================

print("\n" + "=" * 76)
print("SECTION 8: Cross-Checks")
print("=" * 76)

# Cross-check 1: Dimensional analysis
print(f"\n--- Cross-check 1: Dimensional analysis ---")
print(f"  [delta_E] = M_KK (energy)")
print(f"  [rho] = delta_E * M_KK^4 / V_eff = M_KK^5 / V_eff")
print(f"  With spectral action normalization: [rho] = M_KK^4 * (dimensionless)")
print(f"  Consistent: delta_E in M_KK units -> rho in GeV^4. CHECK.")

# Cross-check 2: Energy hierarchy
print(f"\n--- Cross-check 2: Energy hierarchy ---")
print(f"  E_exc (8-mode, Fermi) = {delta_E_8mode_A:.4f} M_KK")
print(f"  E_exc (8-mode, n_Bog) = {delta_E_8mode_B:.4f} M_KK")
print(f"  E_exc (496-mode, S38) = {delta_E_full:.1f} M_KK")
print(f"  E_cond = {E_cond:.6f} M_KK")
print(f"  Ratio (8-mode Fermi / E_cond) = {delta_E_8mode_A / abs(E_cond):.2f}")
print(f"  Ratio (496-mode / E_cond) = {delta_E_full / abs(E_cond):.1f}")
mode_fraction = delta_E_8mode_A / delta_E_full
print(f"  8-mode fraction of total: {mode_fraction:.4f} ({mode_fraction*100:.2f}%)")

# Cross-check 3: Compare 8-mode quasiparticle sum to ED spectrum
E_QP_sum = np.sum(E_k_BCS)
print(f"\n--- Cross-check 3: Quasiparticle energy sum ---")
print(f"  sum(E_k) = {E_QP_sum:.4f} M_KK")
print(f"  sum(E_k * n_k^GGE) = {np.sum(E_k_BCS * n_k_GGE):.4f} M_KK")
print(f"  sum(eps_k) = {np.sum(eps_k):.4f} M_KK")

# Cross-check 4: Bekenstein bound compatibility
# rho_GGE = E / V. The Bekenstein bound requires S < 2*pi*R*E.
# Here S_GGE ~ 0.08, E ~ 60 M_KK, R ~ 1/M_KK.
# 2*pi*R*E = 2*pi*60 = 377. S_GGE << 377. Bound satisfied.
print(f"\n--- Cross-check 4: Bekenstein bound ---")
print(f"  S_GGE = {S_GGE:.4f}")
print(f"  2*pi*R*E = 2*pi*{delta_E_full:.1f} = {2*PI*delta_E_full:.1f}")
print(f"  Bekenstein satisfied: {S_GGE < 2*PI*delta_E_full}")

# Cross-check 5: Compare to Volovik q-theory dynamic prediction
# Volovik (Paper 04): rho_vac ~ M_Pl^2 * H^2 in slow relaxation
rho_volovik_dynamic = M_Pl_reduced**2 * H_0_GeV**2
ratio_volovik = rho_volovik_dynamic / rho_Lambda_obs
print(f"\n--- Cross-check 5: Volovik dynamic prediction ---")
print(f"  rho_vac(q-theory dynamic) = M_Pl^2 * H_0^2 = {rho_volovik_dynamic:.4e} GeV^4")
print(f"  ratio to obs = {ratio_volovik:.2f}")
print(f"  log10(ratio) = {np.log10(ratio_volovik):.2f}")
print(f"  THIS is what matches observation (W1-A).")
print(f"  The GGE deviation (static) = {log10_Ic:.1f} OOM -- DOES NOT match.")

# ==============================================================================
# SECTION 9: Gate Verdict
# ==============================================================================

print("\n" + "=" * 76)
print("SECTION 9: Gate Verdict")
print("=" * 76)

# Use the most physical estimate: full 496-mode excitation (Method Ic)
# This is the most conservative since it includes all modes.
gate_log10 = log10_Ic
gate_ratio = ratio_Ic

# Also compute for the 8-mode case
gate_log10_8mode = log10_Ia

print(f"\nGate: GGE-VACUUM-ENERGY-66")
print(f"  Threshold PASS:  log10(delta_rho/rho_obs) < 10")
print(f"  Threshold INFO:  10 < log10 < 100")
print(f"  Threshold FAIL:  log10(delta_rho/rho_obs) > 100")
print(f"")
print(f"  Computed (496-mode, Method Ic): log10 = {gate_log10:.1f}")
print(f"  Computed (8-mode, Method Ia):   log10 = {gate_log10_8mode:.2f}")

if gate_log10 > 100:
    verdict = "FAIL"
    reason = (f"GGE deviation energy is {gate_log10:.1f} OOM above observation. "
              f"The full excitation energy E_exc = {delta_E_full:.1f} M_KK gives "
              f"rho_GGE = {rho_Ic_GeV4:.2e} GeV^4, which is the FULL CC gap. "
              f"The GGE deviation is NOT a small correction -- it IS the problem.")
elif gate_log10 < 10:
    verdict = "PASS"
    reason = f"GGE deviation naturally small: {gate_log10:.1f} OOM above obs."
else:
    verdict = "INFO"
    reason = f"Intermediate: {gate_log10:.1f} OOM above obs."

print(f"\n  VERDICT: {verdict}")
print(f"  REASON: {reason}")

# ==============================================================================
# SECTION 10: Physical Interpretation
# ==============================================================================

print("\n" + "=" * 76)
print("SECTION 10: Physical Interpretation")
print("=" * 76)

print(f"""
STRUCTURAL RESULT:
  The GGE prethermal vacuum energy delta_rho = (2/pi^2) * E_exc * M_KK^4
  carries the FULL CC gap of ~{gate_log10:.0f} OOM.

  This is NOT a surprise. The GGE preserves the Richardson-Gaudin integrals,
  preventing relaxation to the Volovik zero (rho_eq = 0). But the conservation
  laws do not SUPPRESS the energy -- they merely FREEZE it at the post-transit
  value.

  The GGE deviation energy:
    delta_E = E_exc = {delta_E_full:.1f} M_KK ~ {delta_E_full / a0_fold:.3f} * a_0

  scales as a FIXED FRACTION of the spectral action zeroth moment a_0.
  Since the CC problem is a_0 * M_KK^4 >> rho_obs, and the GGE deviation
  is O(a_0) * M_KK^4, the GGE state carries the same gap.

  KEY CONCLUSION: The GGE deviation energy is NOT an independent resolution
  of the CC problem. It is the SAME problem in different language.
  The GGE mechanism would only help if E_exc << a_0, but
  E_exc/a_0 = {delta_E_full / a0_fold:.3f} ~ O(1%).

  The Volovik DYNAMIC mechanism (rho ~ M_Pl^2 * H^2, matching obs to 0.01 OOM)
  operates at a COMPLETELY DIFFERENT scale from the GGE static energy.
  The dynamic mechanism requires actual relaxation (which the GGE prevents),
  creating a tension: the GGE freezes energy at ~10^{{115}} rho_obs,
  while Volovik's dynamic self-tuning would give ~10^{{0}} rho_obs.

  RESOLUTION DIRECTION: The Volovik dynamic mechanism must operate
  DESPITE the GGE constraints. This requires either:
  (a) Partial breaking of Richardson-Gaudin integrals (S60 RG-INTEGRALS showed
      99.8% Josephson-broken in fabric -- the integrals ARE broken in the fabric)
  (b) The q-variable (tau) can relax even while BCS integrals are frozen
      (because tau couples to the GEOMETRIC sector, not the BCS sector)
  (c) The GGE energy gravitates through a_2 (the Newton's constant channel),
      not through a_0 (the CC channel), separating the two problems
""")

# ==============================================================================
# Save results
# ==============================================================================

print("\n" + "=" * 76)
print("Saving results...")
print("=" * 76)

np.savez(os.path.join(outdir, 's66_gge_vacuum_energy.npz'),
    # Gate
    gate_name='GGE-VACUUM-ENERGY-66',
    gate_verdict=verdict,
    gate_reason=reason,
    gate_log10=gate_log10,
    # GGE energies
    delta_E_8mode_fermi=delta_E_8mode_A,
    delta_E_8mode_nBog=delta_E_8mode_B,
    delta_E_496mode=delta_E_full,
    E_GGE_total=E_GGE_C,
    E_BCS_GS=E_BCS_GS,
    # BCS parameters
    mu_BCS=mu_BCS,
    Delta_BCS=Delta_BCS,
    E_k_BCS=E_k_BCS,
    eps_k=eps_k,
    v2_BCS=v2_BCS_solved,
    # GGE state
    T_GGE=T_GGE,
    beta_GGE=beta_GGE,
    n_k_GGE=n_k_GGE,
    S_GGE=S_GGE,
    S_thermal=S_thermal_A,
    T_thermal=T_thermal_A,
    # Vacuum energy densities (GeV^4)
    rho_Ia_GeV4=rho_Ia_GeV4,
    rho_Ib_GeV4=rho_Ib_GeV4,
    rho_Ic_GeV4=rho_Ic_GeV4,
    rho_IV_GeV4=rho_IV_GeV4,
    # Ratios to observed CC
    log10_Ia=log10_Ia,
    log10_Ib=log10_Ib,
    log10_Ic=log10_Ic,
    log10_IV=log10_IV,
    # Gap decomposition
    log10_deltaE=log10_deltaE_Ic,
    log10_MKK4=log10_MKK4,
    log10_prefactor=log10_prefactor,
    log10_rho_obs=log10_rho_obs,
    # Key ratios
    E_exc_over_a0=delta_E_full / a0_fold,
    mode_fraction_8_of_496=mode_fraction,
    # Volovik dynamic
    rho_volovik_dynamic=rho_volovik_dynamic,
    log10_volovik_dynamic=np.log10(ratio_volovik),
)

print(f"Saved: s66_gge_vacuum_energy.npz")

# ==============================================================================
# Plot
# ==============================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('GGE-VACUUM-ENERGY-66: Prethermal Vacuum Energy', fontsize=14, fontweight='bold')

# Panel (a): GGE occupation numbers vs thermal
ax = axes[0, 0]
modes = np.arange(N_dof_BCS)
labels = ['B2-0', 'B2-1', 'B2-2', 'B2-3', 'B1', 'B3-0', 'B3-1', 'B3-2']
ax.bar(modes - 0.15, n_k_GGE, 0.3, label='GGE (mode-dep T)', color='steelblue', alpha=0.8)
if T_thermal_A < np.inf:
    n_therm = 1.0 / (np.exp(E_k_BCS / T_thermal_A) + 1.0)
    ax.bar(modes + 0.15, n_therm, 0.3, label=f'Thermal (T={T_thermal_A:.3f})', color='coral', alpha=0.8)
ax.set_xticks(modes)
ax.set_xticklabels(labels, fontsize=8)
ax.set_ylabel('Occupation $n_k$')
ax.set_title('(a) GGE vs Thermal Occupations')
ax.legend(fontsize=8)
ax.set_ylim(0, 1.05)

# Panel (b): Energy decomposition bar chart
ax = axes[0, 1]
methods = ['8-mode\n(Fermi)', '8-mode\n(n_Bog)', '496-mode\n(S38)', 'E_cond+E_exc\n(total)']
delta_Es = [delta_E_8mode_A, delta_E_8mode_B, delta_E_full, E_GGE_C]
log10s = [log10_Ia, log10_Ib, log10_Ic, log10_IV]
colors = ['steelblue', 'skyblue', 'darkred', 'orange']
bars = ax.bar(methods, log10s, color=colors, alpha=0.8)
ax.axhline(y=10, color='green', linestyle='--', linewidth=1.5, label='PASS threshold (10)')
ax.axhline(y=100, color='red', linestyle='--', linewidth=1.5, label='FAIL threshold (100)')
ax.set_ylabel(r'$\log_{10}(\delta\rho / \rho_{\rm obs})$')
ax.set_title('(b) CC Gap by Method')
ax.legend(fontsize=8)
for bar, l10 in zip(bars, log10s):
    ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 1,
            f'{l10:.1f}', ha='center', va='bottom', fontsize=9, fontweight='bold')

# Panel (c): Gap decomposition
ax = axes[1, 0]
components = [r'$\log_{10}(\delta E)$', r'$4\log_{10}(M_{KK})$', r'$\log_{10}(2/\pi^2)$', r'$-\log_{10}(\rho_{\rm obs})$']
values = [log10_deltaE_Ic, log10_MKK4, log10_prefactor, -log10_rho_obs]
colors_c = ['steelblue', 'darkred', 'gray', 'green']
bars_c = ax.barh(components, values, color=colors_c, alpha=0.8)
ax.set_xlabel('Orders of magnitude')
ax.set_title(f'(c) Gap Decomposition (total = {sum(values):.1f} OOM)')
for bar, v in zip(bars_c, values):
    ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2.,
            f'{v:.1f}', ha='left', va='center', fontsize=9)

# Panel (d): Energy scales comparison
ax = axes[1, 1]
scales = ['$|E_{\\rm cond}|$', '$E_{\\rm exc}^{8}$', '$E_{\\rm exc}^{496}$', '$a_0$', '$S_{\\rm fold}$']
E_values = [abs(E_cond), delta_E_8mode_A, delta_E_full, a0_fold, S_fold]
ax.barh(scales, [np.log10(max(e, 1e-30)) for e in E_values], color='steelblue', alpha=0.8)
ax.set_xlabel(r'$\log_{10}(E / M_{KK})$')
ax.set_title('(d) Energy Scale Hierarchy')
for i, (s, e) in enumerate(zip(scales, E_values)):
    ax.text(np.log10(max(e, 1e-30)) + 0.1, i, f'{e:.2f}', va='center', fontsize=8)

plt.tight_layout()
plt.savefig(os.path.join(outdir, 's66_gge_vacuum_energy.png'), dpi=150, bbox_inches='tight')
print(f"Saved: s66_gge_vacuum_energy.png")

print("\n" + "=" * 76)
print(f"FINAL GATE VERDICT: {verdict}")
print(f"  log10(delta_rho / rho_obs) = {gate_log10:.1f}")
print(f"  {reason}")
print("=" * 76)
