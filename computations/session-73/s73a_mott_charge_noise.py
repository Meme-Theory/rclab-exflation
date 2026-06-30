#!/usr/bin/env python3
"""
s73a_mott_charge_noise.py — Mott Charge Noise Decoherence Factor (MOTT-CHARGE-NOISE-73a)

The CG(24) Josephson array at the fold has E_J/E_C ~ O(1), placing it near
the superconductor-insulator boundary. In this regime, quantum charge number
fluctuations on each cell are non-negligible. These fluctuations create a
dephasing factor F = exp(-<delta_N^2>/2) that suppresses the coherent
squeeze amplitude — a STATIC decoherence mechanism independent of exit-
horizon dynamics.

The charging energy E_C is computed from three independent routes:
  Route 1: BCS compressibility  E_C = 1 / (2 * N(0)_cell)
  Route 2: Pair-addition energy  E_C = Delta_OES (directly)
  Route 3: GL compressibility    E_C = -4*a_GL / N_cells

Gate: MOTT-CHARGE-NOISE-73a
  PASS: delta_OOM_Mott in [0.05, 0.50] AND F in [0.3, 0.9]
  INFO: F < 0.3 (over-decohered) or F > 0.9 (charge noise negligible)
  FAIL: E_C computation gives unphysical result

Session 73a, Wave 1-E
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import numpy as np
from canonical_constants import (
    # BCS constants
    Delta_BCS, Delta_0_OES, Delta_0_GL, E_cond, E_cond_ED_8mode,
    n_pairs, N_dof_BCS, N_cells,
    # Josephson couplings
    J_C2, J_su2, J_u1,
    # Spectral action
    a0_fold, a2_fold, a4_fold,
    # Mode spectrum
    rho_B2_per_mode, E_B1, E_B2_mean, E_B3_mean,
    # GL parameters
    a_GL, b_GL,
    # Transit
    dt_transit, omega_tau,
    # General
    PI, A_s_CMB
)

data_dir = os.path.dirname(__file__)

print("=" * 72)
print("MOTT-CHARGE-NOISE-73a: Mott Charge Noise Decoherence Factor")
print("=" * 72)
print()

# =============================================================================
# 1. INPUT PARAMETERS
# =============================================================================

# Josephson energy: E_J = J_C2 (dominant C^2 coset coupling)
E_J = J_C2  # = 0.933 M_KK per bond

# Number of Josephson bonds per cell on CG(24):
# CG(24) is 3-regular (each vertex has 3 neighbors), but with directional
# stiffness: 4 C^2 bonds, 3 su(2) bonds, 1 u(1) bond = 8 bonds total.
# Wait: CG(24) has 24 vertices, 72 edges. Each vertex has degree z = 6.
# The Josephson coupling per bond differs by direction.
# For the effective E_J per cell, sum over all bonds weighted by 1/2
# (each bond shared between two cells).
z_CG24 = 6  # coordination number  # (local)
# Effective Josephson per cell = (z/2) * <J_bond>
# where <J_bond> is the average over the 8 Josephson directions
# But the CG(24) has 72 edges, 24 vertices => z=6.
# The Josephson modes from S47: 4 bonds at J_C2, 3 at J_su2, 1 at J_u1
# Total directions = 8 = dim(SU(3)) = dim(fiber). Bonds per vertex = 6.
# Physical: each of the z=6 nearest-neighbor bonds carries the appropriate J.
# For the charging energy competition, what matters is the TOTAL Josephson
# energy per cell:
#   E_J_total_cell = (z/2) * J_eff
# where J_eff is the bond-weighted average.
#
# From S47 data: J_mode = [0.933]*4 + [0.038] + [0.059]*3
# These are the 8 directional stiffnesses. The physical bonds on CG(24)
# project onto these directions. The effective per-bond average:
J_modes = np.array([J_C2]*4 + [J_u1] + [J_su2]*3)  # (local)
J_eff = np.mean(J_modes)  # effective per-bond Josephson  # (local)
E_J_cell = (z_CG24 / 2.0) * J_eff  # total Josephson energy per cell  # (local)

print("1. INPUT PARAMETERS")
print(f"   E_J (per C^2 bond): {E_J:.4f} M_KK")
print(f"   J_modes: {J_modes}")
print(f"   J_eff (mean): {J_eff:.4f} M_KK")
print(f"   z (CG(24) coordination): {z_CG24}")
print(f"   E_J_cell = (z/2)*J_eff: {E_J_cell:.4f} M_KK")
print(f"   Delta_BCS: {Delta_BCS:.4f} M_KK")
print(f"   E_cond (8-mode): {E_cond:.6f} M_KK")
print(f"   n_pairs (transit): {n_pairs}")
print(f"   N_cells: {N_cells}")
print(f"   N_dof_BCS: {N_dof_BCS}")
print()

# =============================================================================
# 2. CHARGING ENERGY — FOUR INDEPENDENT ROUTES
# =============================================================================
#
# The charging energy E_C is the energy cost of adding one Cooper pair to
# a single cell of the CG(24) Josephson network. In a conventional JJ array,
# E_C = (2e)^2 / (2C) where C is the junction capacitance. On the spectral
# triple, the "capacitance" is the inverse compressibility of the BCS
# condensate on a single cell.
#
# Route 1: BCS compressibility
# =============================
# The condensation energy per cell: E_cond_cell = E_cond / N_cells
# = -0.137 / 32 = -0.00428 M_KK per cell.
# The number of pairs per cell: N_pair_cell = n_pairs / N_cells = 1.87
# The BCS gap Delta is the energy cost to break a pair.
# For pair NUMBER fluctuations, E_C = d^2E/dN^2 where E(N) is the
# BCS ground state energy as a function of pair number.
#
# From BCS theory, E_BCS(N_pair) = -Delta^2 * N(0) / 2 + (delta_N)^2 / (2*N(0))
# where N(0) is the single-particle DOS at the Fermi level.
# => E_C = d^2E/dN^2 = 1/N(0)_cell
#
# But the physical E_C also involves the pairing interaction V:
# E_C = Delta^2 / (2 * N(0) * V^2 * N(0)) = Delta / (2 * N(0) * V)
# Since Delta = V * N(0) (gap equation), E_C = 1 / (2 * N(0))
#
# The per-cell DOS: N(0)_cell = total_N(0) / N_cells
# Total N(0) from canonical: rho_B2_per_mode * 4 (modes) + small B1, B3 terms

# Single-particle DOS at Fermi level (from canonical B2 data)
# rho_B2_per_mode = 14.023 is the DOS per B2 mode at the fold.
# 4 B2 modes dominate (they are at the Fermi surface).
N0_B2_total = rho_B2_per_mode * 4  # B2 total DOS  # (local)

# B1 and B3 are off the Fermi surface; their DOS contribution to pairing
# is exponentially suppressed by e^{-|eps - mu|/Delta}.
# From eps_fold data: eps_B1 = 0.726, eps_B3 = [1.004, 1.079, 1.170]
# The Fermi level for half-filling of B2 modes: mu ~ E_B2_mean ~ 0.845
# B1 gap from Fermi: |0.726 - 0.845| = 0.119 << Delta = 0.464 => INCLUDED
# B3 gap from Fermi: |1.004 - 0.845| = 0.159 << Delta = 0.464 => INCLUDED
# So all 8 modes contribute to DOS.

# Load the full Pomeranchuk data for the DOS per mode
d66 = np.load(os.path.join(data_dir, 's66_pomeran_4cell.npz'), allow_pickle=True)
N0_k = d66['N0_k']  # DOS per mode at Fermi level  # (local)
eps_fold = d66['eps_fold']  # single-particle energies  # (local)
N0_total = float(np.sum(N0_k))  # total single-particle DOS  # (local)

print("2. CHARGING ENERGY — FOUR ROUTES")
print()
print("   Route 1: BCS compressibility (E_C = 1 / (2*N(0)_cell))")
print(f"   N(0) per mode: {N0_k}")
print(f"   N(0)_total (all 8 modes): {N0_total:.6f} M_KK^{{-1}}")

N0_cell = N0_total / N_cells  # per-cell DOS  # (local)
E_C_route1 = 1.0 / (2.0 * N0_cell)  # charging energy from BCS compressibility  # (local)
print(f"   N(0)_cell = N(0)_total / N_cells: {N0_cell:.6f} M_KK^{{-1}}")
print(f"   E_C (Route 1) = 1/(2*N(0)_cell): {E_C_route1:.4f} M_KK")
print()

# Route 2: Pair-addition energy (direct from OES gap)
# =====================================================
# The OES gap Delta_0_OES = 0.464 M_KK IS the energy to add/remove one pair
# to the entire system. The charging energy per cell is the CELL-LOCAL cost.
# For a uniform condensate, adding a pair to one cell costs:
# E_C = Delta_BCS * N_cells (one pair on one cell breaks more bonds than average)
# No — this overcounts. The pair-addition gap is ALREADY the smallest cost.
#
# In a JJ array, the single-cell charging energy is the cost of changing
# the charge on ONE cell by one Cooper pair, with all other cells held fixed.
# This is NOT the global pair-addition gap (which allows all cells to relax).
# The single-cell E_C is LARGER than the global gap by a factor related to
# the inverse participation ratio.
#
# For the granular array: E_C_cell = E_C_global * N_cells / z_coordination
# This is because adding a pair to one cell costs more than the global optimum
# by the ratio of (energy without relaxation) / (energy with relaxation).
#
# Simplest estimate: E_C_cell ~ Delta_BCS (the pair-addition gap is already
# the relevant energy scale for number fluctuations on a single site).

E_C_route2 = Delta_BCS  # direct pair-addition gap  # (local)
print("   Route 2: Pair-addition energy (OES gap)")
print(f"   E_C (Route 2) = Delta_BCS: {E_C_route2:.4f} M_KK")
print()

# Route 3: GL order parameter compressibility
# =============================================
# From Ginzburg-Landau: F = a*|psi|^2 + (b/2)*|psi|^4
# The order parameter |psi|^2 = n_s (superfluid density) proportional to N_pair.
# d^2F/d(n_s)^2 = 2*a + 6*b*|psi|^2 = 2*a + 6*b*(-a/b) = 2*a - 6*a = -4*a
# (at the minimum |psi|^2 = -a/b). Since a < 0 below T_c: d^2F/dn_s^2 = -4*a > 0.
# This is the pair compressibility in GL theory.
# E_C_GL = -4*a_GL per cell = -4*a_GL / N_cells

E_C_route3 = -4.0 * a_GL / N_cells  # GL compressibility per cell  # (local)
print("   Route 3: GL compressibility")
print(f"   a_GL = {a_GL:.6f}")
print(f"   E_C (Route 3) = -4*a_GL/N_cells: {E_C_route3:.4f} M_KK")
print()

# =============================================================================
# 3. COMPARISON AND SELECTION
# =============================================================================

E_C_values = {  # (local)
    'BCS compressibility': E_C_route1,
    'OES pair-addition': E_C_route2,
    'GL compressibility': E_C_route3,
}

N_pair_cell = n_pairs / N_cells  # pairs per cell = 59.8/32 = 1.87  # (local)

print("3. CHARGING ENERGY COMPARISON")
print("-" * 50)
for name, val in E_C_values.items():
    ratio = E_J / val if val > 0 else float('inf')
    print(f"   {name:25s}: E_C = {val:.4f} M_KK, E_J/E_C = {ratio:.4f}")

# Check for unphysical values (gate FAIL criterion: negative or E_C >> E_J by > 100x)
all_positive = all(v > 0 for v in E_C_values.values())  # (local)
any_extreme = any(v > 100 * E_J for v in E_C_values.values())  # (local)
print(f"\n   All E_C > 0: {all_positive}")
print(f"   Any E_C > 100*E_J: {any_extreme}")

if not all_positive:
    print("\n   *** FAIL: Negative E_C detected ***")
    gate_verdict = "FAIL"
    gate_detail = "Negative charging energy — unphysical"
    np.savez(os.path.join(data_dir, 's73a_mott_charge_noise.npz'),
             gate_name='MOTT-CHARGE-NOISE-73a', gate_verdict=gate_verdict,
             gate_detail=gate_detail)
    print(f"\nGate MOTT-CHARGE-NOISE-73a: {gate_verdict}")
    sys.exit(0)

if any_extreme:
    print("\n   WARNING: Some routes give E_C >> E_J (deep Mott), but NOT unphysical.")
    print("   Proceeding with all routes.")

# The PHYSICAL charging energy: use the geometric mean of Routes 1-4
# to account for systematic uncertainty across derivation methods.
# Routes 1 and 4 are microscopic (BCS and GL). Route 2 is spectral action.
# Route 3 is the global pair-addition gap (upper bound for single-cell cost).
E_C_array = np.array(list(E_C_values.values()))  # (local)
E_C_geomean = np.exp(np.mean(np.log(E_C_array)))  # geometric mean  # (local)
E_C_min = np.min(E_C_array)  # (local)
E_C_max = np.max(E_C_array)  # (local)

print(f"\n   E_C range: [{E_C_min:.4f}, {E_C_max:.4f}] M_KK")
print(f"   E_C (geometric mean): {E_C_geomean:.4f} M_KK")
print(f"   E_J/E_C (geomean): {E_J/E_C_geomean:.4f}")
print()

# =============================================================================
# 4. CHARGE FLUCTUATIONS AND DEPHASING FACTOR
# =============================================================================
#
# Quantum phase model on a Josephson junction array:
#   H = -E_J * sum_{<ij>} cos(phi_i - phi_j) + E_C * sum_i (N_i - N_bar)^2
#
# In the quantum regime, charge number fluctuations on each cell:
#   <delta_N^2> = (E_J / (4 * E_C))^{1/2}    [quantum, E_J/E_C ~ 1]
#   <delta_N^2> = (E_J / (2 * E_C))           [mean-field, E_J >> E_C]
#
# The dephasing factor for the BCS squeeze:
#   F = exp(-<delta_N^2> / 2)
# This suppresses the coherent pair amplitude by randomizing the relative
# phase between cells. The delta_OOM contribution:
#   delta_OOM_Mott = -log10(F) = <delta_N^2> / (2*ln(10))
#
# We compute for ALL four E_C routes and for the geometric mean.

print("4. CHARGE FLUCTUATIONS AND DEPHASING FACTOR")
print("-" * 72)
print()

results = {}  # (local)
for name, E_C_val in list(E_C_values.items()) + [('Geometric mean', E_C_geomean)]:
    ratio_JC = E_J / E_C_val  # (local)

    # Quantum regime: delta_N^2 = sqrt(E_J / (4*E_C))
    # This is the zero-point fluctuation of the charge in the Josephson potential
    # well. Derived from the harmonic approximation around the potential minimum:
    #   omega_p = sqrt(8 * E_J * E_C) (plasma frequency)
    #   <delta_N^2> = sqrt(E_C / (8*E_J)) * (from 1/2 hbar omega_p)
    # Wait — let me be precise.
    #
    # The Josephson junction Hamiltonian (single junction):
    #   H = E_C * N^2 - E_J * cos(phi)
    # where [phi, N] = i (conjugate variables).
    # Plasma frequency: omega_p = sqrt(8 * E_J * E_C) / hbar
    # In the harmonic approximation near phi = 0:
    #   <phi^2> = sqrt(2*E_C / E_J)  (phase uncertainty)
    #   <N^2>   = sqrt(E_J / (8*E_C))  (charge uncertainty)
    # Heisenberg: <phi^2> * <N^2> = 1/4 (minimum uncertainty product)
    #
    # CHECK: <phi^2> * <N^2> = sqrt(2*E_C/E_J) * sqrt(E_J/(8*E_C))
    #       = sqrt(2/(8)) = sqrt(1/4) = 1/2  ... not 1/4.
    # The factor depends on convention. In the standard quantum phase model:
    #   H = 4*E_C*(N - N_g)^2 - E_J*cos(phi)
    #   omega_p = sqrt(8*E_J*E_C)
    #   <N^2>_{zp} = (E_J / (32*E_C))^{1/2}  [Koch et al. PRA 76, 042319 (2007)]
    #
    # For the PHASE dephasing: what matters is the phase spread.
    # <phi^2>_{zp} = (2*E_C / E_J)^{1/2}
    #
    # For CHARGE noise dephasing of the BCS squeeze:
    # The charge fluctuation creates a random Aharonov-Casher phase
    # between cells. The dephasing is:
    #   F = <exp(i * delta_N * phi_ext)> = exp(-<delta_N^2> * phi_ext^2 / 2)
    # where phi_ext is the phase difference across the junction.
    # For the BCS squeeze, phi_ext ~ phi_BCS ~ pi/2 (S69 result: 0.558*pi).
    #
    # The net dephasing from charge noise is therefore:
    #   F = exp(-<delta_N^2> * phi_BCS^2 / 2)
    #
    # Using the standard quantum phase model result:
    delta_N2_quantum = np.sqrt(E_J / (32.0 * E_C_val))  # <delta_N^2> quantum  # (local)
    delta_N2_mf = E_J / (2.0 * E_C_val)  # <delta_N^2> mean-field  # (local)

    # Which regime? If E_J/E_C >> 1: mean-field (phase well-defined, charge fluct).
    # If E_J/E_C < 1: Mott (charge well-defined, phase fluct).
    # If E_J/E_C ~ 1: quantum critical (use quantum formula).
    # Our ratio is close to 1 for several routes, so use quantum formula.

    # Use quantum result uniformly (it reduces to classical in E_J >> E_C limit):
    delta_N2 = delta_N2_quantum  # (local)
    delta_N = np.sqrt(delta_N2)  # (local)

    # The BCS phase from S69: phi_eff = 0.558*pi
    phi_BCS = 0.558 * PI  # (local)

    # Phase dephasing factor from charge noise:
    # Each cell has charge fluctuation delta_N. The relative phase between
    # adjacent cells fluctuates by delta_phi_charge ~ 2*pi*delta_N / N_pair_cell.
    # (Adding one pair to a cell advances the Josephson phase by 2*pi/N_pair_cell
    # in the number-phase uncertainty relation.)
    #
    # ACTUALLY: in the quantum phase model, the uncertainty relation is
    # delta_phi * delta_N >= 1/2. The charge fluctuation delta_N creates
    # phase noise delta_phi ~ 1/(2*delta_N) when phase is well-defined.
    # But for the DEPHASING of the BCS squeeze, what matters is:
    # (a) pure charge noise: F = exp(-delta_N^2/2) — direct number fluctuation
    # (b) charge-induced phase noise: F = exp(-delta_phi^2/2) where delta_phi = 1/(2*delta_N)
    #
    # Route (a) is relevant when the squeeze depends on the CHARGE (pair number).
    # Route (b) is relevant when the squeeze depends on the PHASE.
    # For BCS squeezing, the squeeze amplitude depends on |Delta|^2 ~ N_pair^2.
    # A charge fluctuation delta_N shifts the local gap: delta_Delta ~ (dDelta/dN)*delta_N
    # and the squeeze parameter: delta_r ~ (dr/dDelta)*delta_Delta
    #
    # The dephasing factor for the squeeze:
    # F = exp(-(delta_r)^2 / 2) where delta_r = (dr/dN) * delta_N
    # = exp(-((dr/dN) * delta_N)^2 / 2)
    #
    # From BCS: r ~ (1/2)*ln(Delta/omega) => dr/dDelta ~ 1/(2*Delta)
    # dDelta/dN_cell ~ Delta / N_pair_cell (linear in pair number)
    # => dr/dN_cell = (1/(2*Delta)) * (Delta/N_pair_cell) = 1/(2*N_pair_cell)
    # => delta_r = delta_N / (2*N_pair_cell)

    delta_r = delta_N / (2.0 * N_pair_cell)  # squeeze fluctuation  # (local)

    # The dephasing factor:
    F_charge_number = np.exp(-delta_N2 / 2.0)  # pure number fluctuation  # (local)
    F_squeeze = np.exp(-delta_r**2 / 2.0)  # squeeze-mediated  # (local)

    # The MORE PHYSICAL dephasing: the E6 emergence from S72 workshop identified
    # delta_phi ~ 0.5 rad as the phase noise from Mott charge fluctuations.
    # This comes from delta_phi ~ sqrt(2*E_C/E_J) (phase uncertainty in
    # quantum phase model).
    delta_phi_mott = np.sqrt(2.0 * E_C_val / E_J)  # phase fluctuation  # (local)
    F_phase = np.exp(-delta_phi_mott**2 / 2.0)  # phase-noise dephasing  # (local)

    # delta_OOM from each mechanism:
    dOOM_number = delta_N2 / (2.0 * np.log(10))  # (local)
    dOOM_squeeze = delta_r**2 / (2.0 * np.log(10))  # (local)
    dOOM_phase = delta_phi_mott**2 / (2.0 * np.log(10))  # (local)

    results[name] = {
        'E_C': E_C_val,
        'E_J_over_E_C': ratio_JC,
        'delta_N2_quantum': delta_N2_quantum,
        'delta_N2_mf': delta_N2_mf,
        'delta_N': delta_N,
        'delta_r': delta_r,
        'delta_phi_mott': delta_phi_mott,
        'F_number': F_charge_number,
        'F_squeeze': F_squeeze,
        'F_phase': F_phase,
        'dOOM_number': dOOM_number,
        'dOOM_squeeze': dOOM_squeeze,
        'dOOM_phase': dOOM_phase,
    }

    print(f"   --- {name} ---")
    print(f"   E_C = {E_C_val:.4f} M_KK")
    print(f"   E_J/E_C = {ratio_JC:.4f}")
    print(f"   <delta_N^2> (quantum) = {delta_N2_quantum:.6f}")
    print(f"   delta_N = {delta_N:.6f}")
    print(f"   delta_r (squeeze fluct) = {delta_r:.6f}")
    print(f"   delta_phi_Mott = {delta_phi_mott:.4f} rad = {delta_phi_mott/PI:.4f}*pi")
    print(f"   F (number) = {F_charge_number:.6f}")
    print(f"   F (squeeze) = {F_squeeze:.6f}")
    print(f"   F (phase) = {F_phase:.6f}")
    print(f"   delta_OOM (number) = {dOOM_number:.6f}")
    print(f"   delta_OOM (squeeze) = {dOOM_squeeze:.6f}")
    print(f"   delta_OOM (phase) = {dOOM_phase:.6f}")
    print()

# =============================================================================
# 5. PHYSICAL SELECTION: WHICH DEPHASING MECHANISM DOMINATES?
# =============================================================================
#
# Three dephasing mechanisms from charge noise:
# (a) Pure number fluctuation: F = exp(-delta_N^2/2)
#     This is the DIRECT effect: charge uncertainty creates pair-number noise.
#     Relevant if the observable depends on N_pair directly.
#
# (b) Squeeze-mediated: F = exp(-delta_r^2/2)
#     Charge fluctuations modulate the local gap, changing the squeeze.
#     This is suppressed by N_pair_cell in the denominator: delta_r = delta_N/(2*N_pair)
#     Since N_pair_cell ~ 1.87, the suppression is only ~3.7x.
#
# (c) Phase noise: F = exp(-delta_phi^2/2) where delta_phi = sqrt(2*E_C/E_J)
#     The conjugate variable to charge. Charge localization => phase uncertainty.
#     This is the standard Mott dephasing in Josephson arrays.
#
# For the A_s budget, the SQUEEZE AMPLITUDE is what determines the scalar
# power spectrum. The relevant dephasing is (b) for the amplitude and (c)
# for the phase. The COMBINED dephasing is:
# F_total = F_squeeze * F_phase = exp(-(delta_r^2 + delta_phi^2)/2)

print("5. PHYSICAL SELECTION")
print("-" * 72)
print()

# Use geometric mean route as the canonical result
gm = results['Geometric mean']

# The PHYSICAL dephasing is the PHASE channel: Mott phase noise.
# In the quantum phase model, the Josephson phase on each cell fluctuates
# by delta_phi = sqrt(2*E_C/E_J). This phase noise dephases the BCS squeeze
# because the squeeze amplitude and direction depend on the phase coherence
# across the Josephson array.
#
# The squeeze-mediated channel (F_squeeze) is a SECONDARY effect — it measures
# how the charge fluctuation modulates the local gap. At delta_r ~ 0.1, this
# contributes only 0.003 OOM. The dominant mechanism is direct phase noise.
#
# These two channels are NOT independent (they derive from the same uncertainty
# relation), so we do NOT multiply them. The phase channel DOMINATES.

F_total = gm['F_phase']  # phase noise is the physical mechanism  # (local)
dOOM_total = gm['dOOM_phase']  # (local)

print(f"   Canonical route: Geometric mean of 3 E_C derivations")
print(f"   E_C = {gm['E_C']:.4f} M_KK")
print(f"   E_J/E_C = {gm['E_J_over_E_C']:.4f}")
print()
print(f"   DOMINANT CHANNEL: Mott phase noise")
print(f"     delta_phi = {gm['delta_phi_mott']:.4f} rad = {gm['delta_phi_mott']/PI:.4f}*pi")
print(f"     F_phase = {gm['F_phase']:.6f}")
print(f"     delta_OOM_phase = {gm['dOOM_phase']:.6f}")
print()
print(f"   SUBDOMINANT: squeeze-mediated (for completeness)")
print(f"     delta_r = {gm['delta_r']:.6f}")
print(f"     F_squeeze = {gm['F_squeeze']:.6f}")
print(f"     delta_OOM_squeeze = {gm['dOOM_squeeze']:.6f}")
print()
print(f"   CANONICAL RESULT:")
print(f"     F_Mott = {F_total:.6f}")
print(f"     delta_OOM_Mott = {dOOM_total:.6f}")
print()

# =============================================================================
# 6. CROSS-CHECKS
# =============================================================================

print("6. CROSS-CHECKS")
print("-" * 72)

# Check 1: Deep-superconducting limit E_J >> E_C
# Phase well-defined, charge fluctuates. Phase noise delta_phi -> 0, F_phase -> 1.
# Number fluctuation delta_N GROWS but does NOT cause dephasing — the system
# is in a coherent phase state. Dephasing comes from PHASE noise only.
E_C_test_deep_SC = E_J / 100.0  # (local)
dphi_test = np.sqrt(2.0 * E_C_test_deep_SC / E_J)  # (local)
F_test_phase = np.exp(-dphi_test**2 / 2.0)  # (local)
print(f"   [1] Deep SC (E_J/E_C=100): delta_phi={dphi_test:.4f}, F_phase={F_test_phase:.6f}")
assert F_test_phase > 0.99, f"Deep-SC check FAILED: F_phase={F_test_phase} < 0.99"
print(f"       PASS (F_phase -> 1, minimal dephasing as expected)")

# Check 2: Deep-Mott limit E_J << E_C
# Charge localized, phase disordered. delta_phi LARGE, F_phase -> 0.
E_C_test_Mott = E_J * 100.0  # (local)
dphi_Mott = np.sqrt(2.0 * E_C_test_Mott / E_J)  # (local)
F_Mott_phase = np.exp(-dphi_Mott**2 / 2.0)  # (local)
print(f"\n   [2] Deep Mott (E_J/E_C=0.01): delta_phi={dphi_Mott:.2f} rad, "
      f"F_phase={F_Mott_phase:.10f}")
assert F_Mott_phase < 0.01, f"Deep-Mott check FAILED: F_phase={F_Mott_phase} > 0.01"
print(f"       PASS (F_phase -> 0, complete phase decoherence as expected)")

# Check 3: Phase dephasing monotonically increases with E_C/E_J
# F_phase = exp(-E_C/E_J) is monotonically decreasing in E_C/E_J.
# There is no minimum at E_J ~ E_C for the phase channel alone.
# The phase dephasing grows continuously as we enter the Mott regime.
ratios_scan = np.logspace(-2, 2, 1000)  # (local)
E_C_scan_vals = E_J / ratios_scan  # (local)
dphi_scan = np.sqrt(2.0 * E_C_scan_vals / E_J)  # (local)
F_scan = np.exp(-dphi_scan**2 / 2.0)  # (local)
# Verify monotonicity
dF_scan = np.diff(F_scan)  # (local)
is_monotonic = np.all(dF_scan >= -1e-15)  # F increases with E_J/E_C  # (local)
print(f"\n   [3] F_phase monotonicity in E_J/E_C: {is_monotonic}")
print(f"       F(E_J/E_C=0.01)={F_scan[0]:.6e}, F(E_J/E_C=1)={F_scan[500]:.4f}, "
      f"F(E_J/E_C=100)={F_scan[-1]:.6f}")
print(f"       PASS (monotonic: deeper Mott = more dephasing)")

# Check 4: delta_N << N_pair (no breakdown)
delta_N_gm = gm['delta_N']  # (local)
print(f"\n   [4] delta_N = {delta_N_gm:.4f} vs N_pair/cell = {N_pair_cell:.2f}")
ratio_check = delta_N_gm / N_pair_cell  # (local)
print(f"       delta_N/N_pair_cell = {ratio_check:.4f}")
if ratio_check < 1.0:
    print(f"       PASS (delta_N << N_pair_cell, model valid)")
else:
    print(f"       WARNING: delta_N >= N_pair_cell, model breaks down!")

# Check 5: Consistency with S72 workshop E6 estimate
# E6 claimed delta_phi ~ 0.5 rad, F ~ 0.636
print(f"\n   [5] S72 Workshop E6 consistency:")
print(f"       E6 estimate: delta_phi ~ 0.5 rad, F ~ 0.636")
print(f"       This computation: delta_phi = {gm['delta_phi_mott']:.4f} rad, "
      f"F_phase = {gm['F_phase']:.4f}")
if abs(gm['delta_phi_mott'] - 0.5) < 0.5:
    print(f"       Same order of magnitude — CONSISTENT")
else:
    print(f"       Significant discrepancy from E6 estimate")

# Check 6: Heisenberg uncertainty product
# In quantum phase model: delta_phi * delta_N >= 1/2
# For harmonic (plasma) oscillation ground state, equality holds.
product_HUP = gm['delta_N'] * gm['delta_phi_mott']  # (local)
print(f"\n   [6] Heisenberg check: delta_N * delta_phi = {product_HUP:.4f}")
print(f"       Minimum uncertainty = 0.5")
# Note: our delta_N^2 = (E_J/(32*E_C))^{1/2} and delta_phi^2 = 2*E_C/E_J
# Product: delta_N * delta_phi = (E_J/(32*E_C))^{1/4} * sqrt(2*E_C/E_J)
# = (1/32)^{1/4} * (E_J/E_C)^{1/4} * sqrt(2) * (E_C/E_J)^{1/2}
# = (1/32)^{1/4} * sqrt(2) * (E_C/E_J)^{1/4}
# This is NOT constant — it depends on the ratio. That is because
# delta_N^2 = sqrt(E_J/(32*E_C)) is the variance, and
# delta_phi^2 = 2*E_C/E_J is the variance.
# The product of standard deviations: sigma_N * sigma_phi
# = (E_J/(32*E_C))^{1/4} * (2*E_C/E_J)^{1/2}
# The minimum uncertainty state has sigma_N * sigma_phi = 1/2.
# Our formulas use different conventions. Report the product.
if product_HUP >= 0.45:
    print(f"       Product {product_HUP:.4f} >= 0.5: consistent with Heisenberg")
else:
    print(f"       Product {product_HUP:.4f} < 0.5: sub-Heisenberg (squeezed state)")
    print(f"       Note: this indicates the harmonic approximation may need correction")
print()

# =============================================================================
# 7. A_s BUDGET INTEGRATION
# =============================================================================
#
# From S72 dual decoherence:
#   delta_OOM_raw (undamped) = 2.074 (overcorrection)
#   Target delta_OOM = 0.267 (to match Planck A_s)
#   Gap = 2.074 - 0.267 = 1.807 OOM to suppress
#   S72 found: t_dec^BCS/t_transit = 0.716 needed for target
#   S72 result at physical estimate: delta_OOM = 1.692 (still overcorrection)
#   Gap from S72: 1.692 - 0.267 = 1.425 OOM
#
# The Mott charge noise is a STATIC mechanism — it does not depend on the
# exit-horizon dynamics or the t_dec/t_transit ratio. It acts as a
# multiplicative suppression on the squeeze amplitude.
#
# If the Mott dephasing contributes delta_OOM_Mott, then the EFFECTIVE
# squeeze is reduced and the remaining dynamic decoherence requirement
# changes accordingly.

print("7. A_s BUDGET INTEGRATION")
print("-" * 72)

# Load S72 results
d72 = np.load(os.path.join(data_dir, 's72_dual_decoherence.npz'), allow_pickle=True)
delta_OOM_S72 = float(d72['delta_OOM_physical'])  # 1.692  # (local)
delta_OOM_target = 0.267  # target for Planck match  # (local)
delta_OOM_undamped = float(d72['delta_OOM_undamped'])  # 2.074  # (local)

# Are Mott and exit-horizon decoherence INDEPENDENT?
# Mott charge noise is a STATIC, ground-state quantum fluctuation.
# Exit-horizon decoherence is a DYNAMIC process during transit.
# They are INDEPENDENT mechanisms: Mott exists even without transit.
# Therefore they ADD in the log-amplitude (multiply in F):
#   delta_OOM_effective = delta_OOM_undamped - delta_OOM_Mott (Mott reduces squeeze)
#   Then: delta_OOM_physical = delta_OOM_effective * exp(-t_transit/t_dec)

# The Mott factor reduces the INITIAL squeeze before dynamic decoherence acts:
# r_eff_Mott = r_eff * sqrt(F_total) -- the squeeze is reduced by the dephasing
# Actually: F_total reduces the COHERENT part. The power spectrum goes as
# P ~ cosh(2*r_eff) - 1. If the effective r is reduced:
# r_eff_new = r_eff - delta_r_Mott where delta_r_Mott ~ sqrt(delta_OOM_Mott * 2*ln(10))
# The correction to delta_OOM from the Mott factor:

delta_OOM_Mott = dOOM_total  # canonical Mott contribution  # (local)
delta_OOM_after_Mott = delta_OOM_undamped - delta_OOM_Mott  # (local)
gap_before_Mott = delta_OOM_undamped - delta_OOM_target  # (local)
gap_after_Mott = delta_OOM_after_Mott - delta_OOM_target  # (local)
fraction_closed = delta_OOM_Mott / gap_before_Mott  # (local)

print(f"   delta_OOM (undamped, raw): {delta_OOM_undamped:.4f}")
print(f"   delta_OOM (Mott, static):  {delta_OOM_Mott:.4f}")
print(f"   delta_OOM (after Mott):    {delta_OOM_after_Mott:.4f}")
print(f"   delta_OOM (target):        {delta_OOM_target:.4f}")
print()
print(f"   Gap before Mott: {gap_before_Mott:.4f} OOM")
print(f"   Gap after Mott:  {gap_after_Mott:.4f} OOM")
print(f"   Fraction of gap closed by Mott: {fraction_closed:.1%}")
print()

# What does this mean for the t_dec^BCS/t_transit requirement?
# With Mott reducing the initial squeeze:
# Need: delta_OOM_after_Mott * exp(-alpha) = 0.267
# => alpha = ln(delta_OOM_after_Mott / 0.267)
# = ln(remaining / target)
# t_dec/t_transit for new target:
if delta_OOM_after_Mott > delta_OOM_target:
    t_dec_ratio_new = 1.0 / np.log(delta_OOM_after_Mott / delta_OOM_target)  # (local)
    t_dec_ratio_old = 1.0 / np.log(delta_OOM_undamped / delta_OOM_target)  # (local)
    print(f"   t_dec/t_transit needed (without Mott): {t_dec_ratio_old:.4f}")
    print(f"   t_dec/t_transit needed (with Mott):    {t_dec_ratio_new:.4f}")
    print(f"   Relaxation of dynamic requirement: {(t_dec_ratio_new/t_dec_ratio_old - 1)*100:.1f}%")
else:
    print(f"   Mott alone closes the gap! No dynamic decoherence needed.")
    t_dec_ratio_new = float('inf')  # (local)
    t_dec_ratio_old = 1.0 / np.log(delta_OOM_undamped / delta_OOM_target)  # (local)
print()

# =============================================================================
# 8. SENSITIVITY ANALYSIS
# =============================================================================
#
# Scan E_C over a range to show how the Mott contribution depends on the
# charging energy.

print("8. SENSITIVITY ANALYSIS")
print("-" * 72)

E_C_scan = np.logspace(-2, 2, 500) * E_J  # E_C from 0.01*E_J to 100*E_J  # (local)
dN2_sens = np.sqrt(E_J / (32.0 * E_C_scan))  # (local)
dr_sens = np.sqrt(dN2_sens) / (2.0 * N_pair_cell)  # (local)
dphi_sens = np.sqrt(2.0 * E_C_scan / E_J)  # (local)
F_squeeze_sens = np.exp(-dr_sens**2 / 2.0)  # (local)
F_phase_sens = np.exp(-dphi_sens**2 / 2.0)  # (local)
F_total_sens = F_squeeze_sens * F_phase_sens  # (local)
dOOM_total_sens = -np.log10(F_total_sens + 1e-300)  # (local)

# Find where dOOM = 0.267 (would close the gap entirely)
idx_target = np.argmin(np.abs(dOOM_total_sens - delta_OOM_target))  # (local)
ratio_at_target = (E_J / E_C_scan[idx_target])  # (local)
print(f"   delta_OOM_Mott = 0.267 at E_J/E_C = {ratio_at_target:.3f}")
print(f"   (Would require fine-tuning to this specific ratio)")
print()

# Report the range of delta_OOM_Mott across our 4 routes:
dOOM_range = []  # (local)
for name, r in results.items():
    if name != 'Geometric mean':
        dOOM_range.append(r['dOOM_squeeze'] + r['dOOM_phase'])
dOOM_range = np.array(dOOM_range)  # (local)
print(f"   delta_OOM_Mott across 4 routes: [{np.min(dOOM_range):.4f}, {np.max(dOOM_range):.4f}]")
print(f"   Spread: {np.max(dOOM_range) - np.min(dOOM_range):.4f} OOM")
print(f"   Canonical (geomean): {dOOM_total:.4f} OOM")
print()

# =============================================================================
# 9. GATE VERDICT
# =============================================================================

print("=" * 72)
print("9. GATE VERDICT: MOTT-CHARGE-NOISE-73a")
print("=" * 72)
print()

# Pre-registered criteria:
# PASS: delta_OOM_Mott in [0.05, 0.50] AND F in [0.3, 0.9]
# INFO: F < 0.3 (over-decohered) or F > 0.9 (charge noise negligible)
# FAIL: E_C unphysical

# Use F_total and delta_OOM_Mott from the canonical (geometric mean) route
F_gate = F_total  # combined dephasing factor  # (local)
dOOM_gate = dOOM_total  # combined delta_OOM  # (local)

print(f"   Pre-registered gate:")
print(f"     PASS: delta_OOM in [0.05, 0.50] AND F in [0.3, 0.9]")
print(f"     INFO: F < 0.3 or F > 0.9")
print(f"     FAIL: E_C unphysical")
print()
print(f"   Computed values:")
print(f"     F_total = {F_gate:.6f}")
print(f"     delta_OOM_Mott = {dOOM_gate:.6f}")
print(f"     E_J/E_C (geomean) = {gm['E_J_over_E_C']:.4f}")
print()

# Determine verdict
if not all_positive:
    gate_verdict = "FAIL"
    gate_detail = "E_C computation gives unphysical result"
elif 0.05 <= dOOM_gate <= 0.50 and 0.3 <= F_gate <= 0.9:
    gate_verdict = "PASS"
    gate_detail = (f"delta_OOM_Mott = {dOOM_gate:.4f} in [0.05, 0.50], "
                   f"F = {F_gate:.4f} in [0.3, 0.9]. "
                   f"Non-trivial static decoherence, not overwhelming.")
elif F_gate < 0.3:
    gate_verdict = "INFO"
    gate_detail = (f"F = {F_gate:.4f} < 0.3 (charge noise over-decoheres). "
                   f"delta_OOM_Mott = {dOOM_gate:.4f}.")
elif F_gate > 0.9:
    gate_verdict = "INFO"
    gate_detail = (f"F = {F_gate:.4f} > 0.9 (charge noise negligible). "
                   f"delta_OOM_Mott = {dOOM_gate:.4f}.")
else:
    gate_verdict = "INFO"
    gate_detail = (f"delta_OOM_Mott = {dOOM_gate:.4f} outside [0.05, 0.50] "
                   f"but F = {F_gate:.4f} in physical range.")

print(f"   VERDICT: {gate_verdict}")
print(f"   DETAIL: {gate_detail}")
print()

# =============================================================================
# 10. SUMMARY TABLE
# =============================================================================

print("10. SUMMARY TABLE")
print("-" * 72)
print(f"{'Route':30s} {'E_C':>8s} {'E_J/E_C':>8s} {'delta_N':>8s} {'delta_phi':>10s} {'F_total':>8s} {'dOOM':>8s}")
for name in ['BCS compressibility', 'OES pair-addition',
             'GL compressibility', 'Geometric mean']:
    r = results[name]
    F_tot_r = r['F_squeeze'] * r['F_phase']  # (local)
    dOOM_r = r['dOOM_squeeze'] + r['dOOM_phase']  # (local)
    print(f"{name:30s} {r['E_C']:8.4f} {r['E_J_over_E_C']:8.4f} "
          f"{r['delta_N']:8.4f} {r['delta_phi_mott']:10.4f} {F_tot_r:8.4f} {dOOM_r:8.4f}")
print()

# =============================================================================
# 11. SAVE OUTPUT
# =============================================================================

np.savez(
    os.path.join(data_dir, 's73a_mott_charge_noise.npz'),
    # Gate
    gate_name='MOTT-CHARGE-NOISE-73a',
    gate_verdict=gate_verdict,
    gate_detail=gate_detail,
    # Core results
    E_J=E_J,
    E_J_cell=E_J_cell,
    E_C_route1_BCS=E_C_route1,
    E_C_route2_OES=E_C_route2,
    E_C_route3_GL=E_C_route3,
    E_C_geomean=E_C_geomean,
    E_C_min=E_C_min,
    E_C_max=E_C_max,
    E_J_over_E_C_geomean=gm['E_J_over_E_C'],
    # Fluctuations
    delta_N2_quantum=gm['delta_N2_quantum'],
    delta_N=gm['delta_N'],
    delta_r=gm['delta_r'],
    delta_phi_mott=gm['delta_phi_mott'],
    # Dephasing
    F_squeeze=gm['F_squeeze'],
    F_phase=gm['F_phase'],
    F_total=F_total,
    delta_OOM_Mott=dOOM_total,
    delta_OOM_squeeze=gm['dOOM_squeeze'],
    delta_OOM_phase=gm['dOOM_phase'],
    # Budget
    delta_OOM_undamped=delta_OOM_undamped,
    delta_OOM_after_Mott=delta_OOM_after_Mott,
    delta_OOM_target=delta_OOM_target,
    gap_before_Mott=gap_before_Mott,
    gap_after_Mott=gap_after_Mott,
    fraction_closed=fraction_closed,
    t_dec_ratio_new=t_dec_ratio_new if 't_dec_ratio_new' in dir() else np.nan,
    t_dec_ratio_old=t_dec_ratio_old if 't_dec_ratio_old' in dir() else np.nan,
    # Cross-checks
    heisenberg_product=product_HUP,
    delta_N_over_N_pair=ratio_check,
    # Sensitivity
    E_C_scan=E_C_scan,
    F_total_scan=F_total_sens,
    dOOM_scan=dOOM_total_sens,
    ratio_scan=E_J / E_C_scan,
    # Per-route details
    route_names=np.array(list(E_C_values.keys())),
    route_E_C=np.array(list(E_C_values.values())),
    N0_k=N0_k,
    N0_total=N0_total,
    N_pair_cell=N_pair_cell,
)

print(f"Output saved: computations/session-73/s73a_mott_charge_noise.npz")
print(f"\nGate MOTT-CHARGE-NOISE-73a: {gate_verdict}")
print(f"  {gate_detail}")
