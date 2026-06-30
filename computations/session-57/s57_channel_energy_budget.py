#!/usr/bin/env python3
"""
CHANNEL-ENERGY-BUDGET-57 — Energy decomposition of the 32-cell fabric
=====================================================================

Gate: INFO — decompose total fabric energy into Josephson, BCS, and Leggett channels.
Question: does E_L/E_total << 0.01, which would make DM via Leggett energetically impossible?

Physics:
  The fabric free energy at the fold decomposes (Strutinsky-like) into:
    F_total = F_Josephson + F_BCS + F_Leggett + F_BA_phonon + F_residual

  where:
    F_Josephson  = -N_bonds_type * E_J_type * <cos(phi_i - phi_j)>  [phase coherence]
    F_BCS        = N_cells * E_cond                                  [intra-cell condensation]
    F_Leggett    = N_cells * E_Leggett_per_cell                     [relative B2-B1 phase]
    F_BA_phonon  = Sum_{k,n} [omega_n(k)/2 + T*ln(1-exp(-omega_n(k)/T))]  [BA fluctuations]

  The Josephson energy per bond E_J(tau) = J_C2(tau)^2 * F_anomalous(tau) from BCS coherence
  factors, evaluated on the FULL 32-eigenvalue TB spectrum (S56 Leggett/BA formulation).

  The Leggett energy per cell = (1/2) * epsilon * E_J * alpha_Leggett, where:
    epsilon = 0.00248 (dipolar coupling, S49 DIPOLAR-CATALOG-49)
    alpha_Leggett = <cos(phi_B2 - phi_B1)> captures the relative-phase coherence
    In the deep superfluid regime, alpha ~ 1 (locked phases)

  The BA phonon free energy = ZPE + thermal, from the 31 Bogoliubov-Anderson modes.

Method:
  1. Load bond counts from S54, Josephson couplings from S56
  2. Compute Josephson energy for each bond type (C2, su2, u1)
  3. Compute mean-field <cos(phi)> in the superfluid regime
  4. Decompose total energy and report fractions

Author: Quantum-Acoustics (S57 W0-2)
Date: 2026-03-22
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from canonical_constants import (
    tau_fold, E_cond, N_cells, Delta_0_OES, J_C2, J_su2, J_u1,
    omega_L1, omega_L2, T_acoustic, E_B1, E_B2_mean, E_B3_mean
)

# ============================================================================
# 1. Load all input data
# ============================================================================
print("=" * 72)
print("CHANNEL-ENERGY-BUDGET-57: Energy decomposition of the 32-cell fabric")
print("=" * 72)

# S54: bond structure
d54 = np.load('computations/session-54/s54_tb_hamiltonian.npz', allow_pickle=True)
n_bonds_C2 = int(d54['n_bonds_C2'])
n_bonds_su2 = int(d54['n_bonds_su2'])
n_bonds_u1 = int(d54['n_bonds_u1'])
n_bonds_total = int(d54['n_bonds_total'])

tau_arr_54 = d54['tau_values']
fold_idx_54 = np.argmin(np.abs(tau_arr_54 - tau_fold))
J_C2_fold = d54['J_C2_tau'][fold_idx_54]
J_su2_fold = d54['J_su2_tau'][fold_idx_54]
J_u1_fold = d54['J_u1_tau'][fold_idx_54]

print(f"\n--- Bond structure (S54 TB-HAMILTONIAN-54) ---")
print(f"  N_cells = {N_cells}")
print(f"  Bonds: {n_bonds_C2} C2 + {n_bonds_su2} su2 + {n_bonds_u1} u1 = {n_bonds_total} total")
print(f"  Mean coordination z = {2 * n_bonds_total / N_cells:.2f}")
print(f"  J_C2(fold) = {J_C2_fold:.6f} M_KK")
print(f"  J_su2(fold) = {J_su2_fold:.6f} M_KK")
print(f"  J_u1(fold) = {J_u1_fold:.6f} M_KK")

# S56: fabric data
d56_gge = np.load('computations/session-56/s56_gge_fabric.npz', allow_pickle=True)
d56_legg = np.load('computations/session-56/s56_leggett_fabric.npz', allow_pickle=True)
d56_ba = np.load('computations/session-56/s56_ba_spectrum.npz', allow_pickle=True)

tau_arr_L = d56_legg['tau_values']
fold_idx_L = np.argmin(np.abs(tau_arr_L - tau_fold))
E_J_fold_fabric = d56_legg['E_J'][fold_idx_L]  # = 7.042 M_KK (full TB spectrum)
E_c_fold = d56_legg['E_c'][fold_idx_L]
J_Leggett_fold = d56_legg['J_Leggett'][fold_idx_L]
epsilon_L = float(d56_legg['epsilon_Leggett'])

tau_arr_BA = d56_ba['tau_values']
fold_idx_BA = np.argmin(np.abs(tau_arr_BA - tau_fold))
F_BA_fold = d56_ba['F_BA'][fold_idx_BA]
F_ZPE_fold = d56_ba['F_ZPE'][fold_idx_BA]
F_thermal_fold = d56_ba['F_thermal'][fold_idx_BA]
omega_BA_fold = d56_ba['omega_BA'][fold_idx_BA]  # 31 modes
E_J_BA = d56_ba['E_J'][fold_idx_BA]  # cross-check: should match E_J_fold_fabric

print(f"\n--- Josephson energy (S56 LEGGETT-FABRIC-56 / BA-SPECTRUM-56) ---")
print(f"  E_J(fold, fabric) = {E_J_fold_fabric:.6f} M_KK (from full 32-level TB spectrum)")
print(f"  E_J(fold, 2-cell) = {float(d56_gge['E_J_fold']):.6f} M_KK (from 8-level intra-cell)")
print(f"  E_c(fold) = {E_c_fold:.6f} M_KK")
print(f"  E_J/E_c = {E_J_fold_fabric / E_c_fold:.1f} (deep superfluid)")
print(f"  E_J cross-check (BA): {E_J_BA:.6f} M_KK")

# ============================================================================
# 2. Josephson energy: F_Josephson = -Sum_bonds E_J_type * <cos(delta_phi)>
# ============================================================================
# In the superfluid regime (E_J/E_c >> 1), the XY order parameter is:
#   m = <cos(phi_i - phi_j)> = 1 - T/(2*J*z) for mean-field XY model
# More precisely (quantum rotor):
#   <cos(phi)> = 1 - 1/(2*sqrt(E_J/E_c)) in the zero-T quantum limit
# At finite T_GH:
#   <cos(phi)> ~ 1 - T/(2*E_J) - 1/(2*sqrt(E_J/E_c))

print(f"\n--- Order parameter <cos(phi)> ---")

# Quantum + thermal corrections to order parameter
# Quantum depletion for each bond type
def cos_phi_quantum(E_J_val, E_c_val):
    """Zero-temperature quantum depletion of XY order parameter."""
    return 1.0 - 1.0 / (2.0 * np.sqrt(E_J_val / E_c_val))

def cos_phi_thermal(E_J_val, T):
    """Thermal correction to order parameter."""
    if T <= 0 or E_J_val <= 0:
        return 0.0
    return -T / (2.0 * E_J_val)

# E_J per bond type: E_J_type = J_type^2 * F_anom
# The anomalous factor F_anom is the same for all bond types (same BCS state)
# From E_J_fold_fabric = J_C2_fold^2 * F_anom, extract F_anom
F_anom = E_J_fold_fabric / J_C2_fold**2
print(f"  F_anomalous = {F_anom:.6f}")

E_J_C2_bond = J_C2_fold**2 * F_anom
E_J_su2_bond = J_su2_fold**2 * F_anom
E_J_u1_bond = J_u1_fold**2 * F_anom

print(f"  E_J per bond:")
print(f"    C2:  {E_J_C2_bond:.6f} M_KK ({n_bonds_C2} bonds)")
print(f"    su2: {E_J_su2_bond:.6f} M_KK ({n_bonds_su2} bonds)")
print(f"    u1:  {E_J_u1_bond:.6f} M_KK ({n_bonds_u1} bonds)")

# Temperature: GGE acoustic temperature from S47/S56
T_GH = T_acoustic  # = 0.112 M_KK

# Order parameters per bond type
m_C2_q = cos_phi_quantum(E_J_C2_bond, E_c_fold)
m_su2_q = cos_phi_quantum(E_J_su2_bond, E_c_fold)
m_u1_q = cos_phi_quantum(E_J_u1_bond, E_c_fold)

m_C2_th = cos_phi_thermal(E_J_C2_bond, T_GH)
m_su2_th = cos_phi_thermal(E_J_su2_bond, T_GH)
m_u1_th = cos_phi_thermal(E_J_u1_bond, T_GH)

m_C2 = m_C2_q + m_C2_th
m_su2 = max(m_su2_q + m_su2_th, 0.0)  # can't go negative if superfluid
m_u1 = max(m_u1_q + m_u1_th, 0.0)

print(f"\n  <cos(phi)> per bond type (quantum + thermal at T_GH = {T_GH:.3f}):")
print(f"    C2:  {m_C2:.6f} (quantum: {m_C2_q:.6f}, thermal: {m_C2_th:.6f})")
print(f"    su2: {m_su2:.6f} (quantum: {m_su2_q:.6f}, thermal: {m_su2_th:.6f})")
print(f"    u1:  {m_u1:.6f} (quantum: {m_u1_q:.6f}, thermal: {m_u1_th:.6f})")

# Josephson free energy: F_J = -Sum_type N_type * E_J_type * m_type
F_J_C2 = -n_bonds_C2 * E_J_C2_bond * m_C2
F_J_su2 = -n_bonds_su2 * E_J_su2_bond * m_su2
F_J_u1 = -n_bonds_u1 * E_J_u1_bond * m_u1
F_Josephson = F_J_C2 + F_J_su2 + F_J_u1

print(f"\n--- Josephson energy ---")
print(f"  F_J(C2)  = {F_J_C2:.4f} M_KK ({n_bonds_C2} bonds)")
print(f"  F_J(su2) = {F_J_su2:.4f} M_KK ({n_bonds_su2} bonds)")
print(f"  F_J(u1)  = {F_J_u1:.4f} M_KK ({n_bonds_u1} bonds)")
print(f"  F_Josephson = {F_Josephson:.4f} M_KK")

# ============================================================================
# 3. BCS condensation energy: F_BCS = N_cells * E_cond
# ============================================================================
F_BCS = N_cells * E_cond
print(f"\n--- BCS condensation energy ---")
print(f"  E_cond = {E_cond:.6f} M_KK (per cell, 8-mode ED)")
print(f"  F_BCS = N_cells * E_cond = {N_cells} * {E_cond:.6f} = {F_BCS:.4f} M_KK")

# ============================================================================
# 4. Leggett relative-phase energy
# ============================================================================
# The Leggett mode involves oscillations of the relative phase phi_B2 - phi_B1
# between the two gap components within each cell.
#
# Energy per cell:
#   E_Leggett = (1/2) * epsilon * E_J * alpha_L
# where alpha_L = product of gap magnitudes / sum (geometric mean weighting)
#
# More precisely, the Leggett coupling energy is:
#   E_L_cell = epsilon * E_J * |Delta_B2| * |Delta_B1| / (|Delta_B2| + |Delta_B1|)
#            * <cos(theta_B2 - theta_B1)>
#
# The B2 and B1 gaps:
#   Delta_B2 ~ Delta_0_OES = 0.464 M_KK (4 modes, dominant)
#   Delta_B1 = subset of condensate. From S49: omega_L1 = 0.070, omega_L2 = 0.107
#
# In the deep superfluid regime, <cos(theta_B2 - theta_B1)> ~ 1 (locked by epsilon coupling).
# The Leggett energy per cell sets the SCALE of the relative-phase degree of freedom.

print(f"\n--- Leggett relative-phase energy ---")

# Gap magnitudes: B2 carries most of the pairing, B1 is the acoustic (softer) gap
# From the BCS state: Delta_B2 ~ Delta_0_OES (main gap), Delta_B1 ~ fraction
# Use the gap ratio from S49 Leggett analysis: omega_L propto sqrt(epsilon * Delta_B2 * Delta_B1)
# From S52: omega_L1 = 0.138 (GL), omega_L1_S49 = 0.070

# The Leggett coupling at the fold from S56:
# J_Leggett = epsilon * E_J = 0.00248 * 7.042 = 0.01746 M_KK per bond

# INTRA-cell Leggett: this is the energy cost of twisting the relative phase within ONE cell
# This is NOT the inter-cell hopping of the Leggett mode (that's J_Leggett * laplacian)
# The intra-cell Leggett energy is set by the Leggett mode gap:
#   E_L_cell = (1/2) * omega_L0 (zero-point energy of the relative-phase oscillator)
# At finite T_GH: F_L_cell = T * ln(2*sinh(omega_L0 / (2*T)))

# The Leggett POTENTIAL energy per cell (the well depth that confines the relative phase):
# V_Leggett = epsilon * E_J_intra * (Delta_B2 * Delta_B1) / (Delta_B2^2 + Delta_B1^2)
# From the Leggett original paper (1966): the coupling is between the two condensate components

# For our decomposition, the Leggett CHANNEL energy includes:
# (a) The static Leggett coupling (potential energy of relative phase)
# (b) The kinetic energy of relative-phase fluctuations
# (c) The inter-cell dispersive correction

# The omega_L0 already encodes (a) + (b) at the single-cell level.
# For the fabric, each cell contributes the Leggett mode, and they disperse via J_Leggett * laplacian.

# Method 1: Direct from Leggett gap
# The Leggett potential energy per cell (harmonic approximation):
# V_L0 = (1/2) * omega_L0^2 / chi_L, where chi_L is the Leggett susceptibility
# In the Leggett model: omega_L0 = sqrt(2 * epsilon * E_J / chi_L)
# So V_L0 = (1/2) * chi_L * omega_L0^2 = epsilon * E_J

# Using the Leggett coupling from the fabric data:
E_L_coupling_per_cell = epsilon_L * E_J_fold_fabric  # Leggett potential energy per cell

# The full Leggett channel energy per cell includes:
# - Zero-point energy of relative-phase oscillator: (1/2) * omega_L0
# - Thermal population (at T_GH)
omega_L0_values = [0.070, 0.107, 0.138]  # Three estimates from S49/S52
omega_L0_labels = ['S49-1 (dipolar)', 'S49-2 (sigma-pi)', 'GL (harmonic)']

print(f"  epsilon = {epsilon_L:.6f}")
print(f"  E_J(fold, fabric) = {E_J_fold_fabric:.6f} M_KK")
print(f"  Leggett coupling per cell: epsilon * E_J = {E_L_coupling_per_cell:.6f} M_KK")
print(f"  J_Leggett(fold) = {J_Leggett_fold:.6f} M_KK (inter-cell hopping)")

# Total Leggett channel energy for the fabric (all 32 cells):
# F_Leggett_fabric = N_cells * F_L_cell + dispersive corrections
# The dispersive correction from inter-cell hopping adds J_Leggett * Sum_n lambda_n * <a_n^dag a_n>
# At T_GH, the dispersive correction is second-order.

# The Leggett FREE ENERGY per cell at T_GH (quantum + thermal, harmonic):
def F_Leggett_cell(omega_L0, T):
    """Free energy of a single Leggett oscillator at temperature T."""
    if T <= 0:
        return 0.5 * omega_L0  # Just ZPE
    beta_omega = omega_L0 / T
    if beta_omega > 40:  # Very cold
        return 0.5 * omega_L0
    return T * np.log(2.0 * np.sinh(0.5 * beta_omega))

print(f"\n  Leggett free energy per cell at T_GH = {T_GH:.3f} M_KK:")
F_L_cells = {}
for i, (omega_L0, label) in enumerate(zip(omega_L0_values, omega_L0_labels)):
    F_L = F_Leggett_cell(omega_L0, T_GH)
    n_BE = 1.0 / (np.exp(omega_L0 / T_GH) - 1.0) if omega_L0 / T_GH < 40 else 0.0
    F_L_cells[label] = F_L
    print(f"    {label}: omega_L0 = {omega_L0:.3f}, F_L/cell = {F_L:.6f} M_KK, n_BE = {n_BE:.4f}")

# Use the S49-1 (dipolar) value as canonical (from DIPOLAR-CATALOG-49)
omega_L0_canonical = 0.070  # S49 dipolar value, intentionally != omega_L1 (0.138)  # (local)
F_L_per_cell = F_Leggett_cell(omega_L0_canonical, T_GH)
F_Leggett_total = N_cells * F_L_per_cell

# Add dispersive correction from inter-cell hopping
laplacian_eigs = d56_legg['laplacian_eigs']  # 32 eigenvalues
# The dispersive modes have omega_L(n) = sqrt(omega_L0^2 + J_Leggett * lambda_n)
# Their total free energy:
F_Leggett_dispersive = 0.0  # (local)
for n in range(len(laplacian_eigs)):
    omega_n = np.sqrt(omega_L0_canonical**2 + J_Leggett_fold * laplacian_eigs[n])
    F_Leggett_dispersive += F_Leggett_cell(omega_n, T_GH)

print(f"\n  Total Leggett free energy (fabric):")
print(f"    Uniform (N * F_L/cell): {F_Leggett_total:.6f} M_KK")
print(f"    Dispersive (sum modes): {F_Leggett_dispersive:.6f} M_KK")
print(f"    Dispersive correction:  {F_Leggett_dispersive - F_Leggett_total:.6f} M_KK")

# Use the dispersive value (it includes the k=0 mode + all nonzero-k)
F_Leggett = F_Leggett_dispersive

# ============================================================================
# 5. BA phonon free energy (already computed in S56)
# ============================================================================
# F_BA_fold = 7.021 M_KK (from BA-SPECTRUM-56, 31 modes on 32-cell graph)
print(f"\n--- BA phonon free energy (S56 BA-SPECTRUM-56) ---")
print(f"  F_BA(fold) = {F_BA_fold:.4f} M_KK (31 Bogoliubov-Anderson modes)")
print(f"  F_ZPE     = {F_ZPE_fold:.4f} M_KK")
print(f"  F_thermal = {F_thermal_fold:.4f} M_KK")
print(f"  (F_BA = F_ZPE + F_thermal = {F_ZPE_fold + F_thermal_fold:.4f} M_KK)")

# ============================================================================
# 6. Total energy and fractions
# ============================================================================
# The smooth + shell decomposition:
# F_smooth = F_Josephson (bulk phase stiffness, dominant, smooth in tau)
# delta_F  = F_BCS + F_Leggett + F_BA (fluctuation/shell corrections)

# Absolute values for the budget
print(f"\n{'=' * 72}")
print(f"ENERGY BUDGET at tau = {tau_fold} (fold)")
print(f"{'=' * 72}")

print(f"\n  F_Josephson  = {F_Josephson:+.4f} M_KK  (inter-cell phase coherence)")
print(f"  F_BCS        = {F_BCS:+.4f} M_KK  (intra-cell pairing)")
print(f"  F_Leggett    = {F_Leggett:+.4f} M_KK  (relative B2-B1 phase)")
print(f"  F_BA         = {F_BA_fold:+.4f} M_KK  (BA phonon fluctuations)")

F_total = F_Josephson + F_BCS + F_Leggett + F_BA_fold
print(f"  -------------------------------------------------------")
print(f"  F_total      = {F_total:+.4f} M_KK")

# Energy fractions (using absolute values for the budget)
abs_total = abs(F_Josephson) + abs(F_BCS) + abs(F_Leggett) + abs(F_BA_fold)
frac_J = abs(F_Josephson) / abs_total
frac_BCS = abs(F_BCS) / abs_total
frac_L = abs(F_Leggett) / abs_total
frac_BA = abs(F_BA_fold) / abs_total

print(f"\n  Energy fractions (|F_channel| / Sum |F|):")
print(f"    |F_J|/Sum|F|     = {frac_J:.6f} = {frac_J*100:.2f}%")
print(f"    |F_BCS|/Sum|F|   = {frac_BCS:.6f} = {frac_BCS*100:.2f}%")
print(f"    |F_L|/Sum|F|     = {frac_L:.6f} = {frac_L*100:.2f}%")
print(f"    |F_BA|/Sum|F|    = {frac_BA:.6f} = {frac_BA*100:.2f}%")

# The physically relevant question: what fraction of the total is in the Leggett channel?
# For the DM mechanism: DM is produced by Leggett excitations
# The Leggett channel must carry enough energy for Omega_DM/Omega_total ~ 0.27

print(f"\n  Ratios relevant for DM mechanism:")
print(f"    F_Leggett / |F_Josephson| = {F_Leggett / abs(F_Josephson):.6f} = {F_Leggett / abs(F_Josephson) * 100:.4f}%")
print(f"    F_Leggett / |F_BCS|       = {F_Leggett / abs(F_BCS):.6f} = {F_Leggett / abs(F_BCS) * 100:.2f}%")
print(f"    F_Leggett / |F_total|     = {F_Leggett / abs(F_total):.6f} = {F_Leggett / abs(F_total) * 100:.4f}%")

# ============================================================================
# 7. Strutinsky decomposition: smooth vs shell
# ============================================================================
print(f"\n{'=' * 72}")
print(f"STRUTINSKY DECOMPOSITION")
print(f"{'=' * 72}")

F_smooth = F_Josephson  # Smooth: Josephson phase stiffness (extensive, monotonic)
delta_F = F_BCS + F_Leggett + F_BA_fold  # Shell: quantum fluctuations on top

print(f"\n  F_smooth (Josephson) = {F_smooth:+.4f} M_KK")
print(f"  delta_F (BCS+L+BA)  = {delta_F:+.4f} M_KK")
print(f"  |delta_F/F_smooth|  = {abs(delta_F / F_smooth):.4f} = {abs(delta_F / F_smooth) * 100:.2f}%")

# Within the shell correction:
print(f"\n  Shell decomposition:")
print(f"    F_BCS / delta_F     = {F_BCS / delta_F:.4f}")
print(f"    F_Leggett / delta_F = {F_Leggett / delta_F:.4f}")
print(f"    F_BA / delta_F      = {F_BA_fold / delta_F:.4f}")

# ============================================================================
# 8. Sensitivity: what if Leggett modes are FULLY excited?
# ============================================================================
print(f"\n{'=' * 72}")
print(f"SENSITIVITY: Leggett modes at full excitation")
print(f"{'=' * 72}")

# If the Leggett channel is fully excited (P_exc^L ~ 1), the energy deposited is:
# E_L_excited = N_cells * omega_L0 (one quantum per cell)
# vs ground state: E_L_ground = N_cells * omega_L0 / 2 (zero-point)
# Energy DIFFERENCE: Delta_E_L = N_cells * omega_L0 / 2

Delta_E_L = N_cells * omega_L0_canonical / 2.0
print(f"  If all Leggett modes excited (P_exc = 1):")
print(f"    Energy deposited: N_cells * omega_L0 / 2 = {Delta_E_L:.4f} M_KK")
print(f"    Fraction of |F_total|: {Delta_E_L / abs(F_total):.6f} = {Delta_E_L / abs(F_total) * 100:.4f}%")
print(f"    Fraction of |F_Josephson|: {Delta_E_L / abs(F_Josephson):.6f}")

# Maximum possible: all 32 Leggett modes excited to n_BE >> 1
# E_L_max ~ N_cells * max(omega_L(k)) for one quantum each
omega_L_max = np.sqrt(omega_L0_canonical**2 + J_Leggett_fold * laplacian_eigs[-1])
E_L_max_1quantum = np.sum([np.sqrt(omega_L0_canonical**2 + J_Leggett_fold * lam)
                           for lam in laplacian_eigs])
print(f"\n  Maximum Leggett excitation energy (1 quantum per mode):")
print(f"    Sum omega_L(k) = {E_L_max_1quantum:.4f} M_KK")
print(f"    Fraction of |F_total|: {E_L_max_1quantum / abs(F_total):.6f}")

# ============================================================================
# 9. DM viability assessment
# ============================================================================
print(f"\n{'=' * 72}")
print(f"DM VIABILITY ASSESSMENT")
print(f"{'=' * 72}")

# Observed: Omega_DM / Omega_total ~ 0.266
# Required: E_DM / E_total ~ 0.27 (the DM fraction of the total energy budget)
# Available from Leggett: E_L_excited / |F_total|
Omega_DM_target = 0.266  # (local)

print(f"  Target: Omega_DM / Omega_total = {Omega_DM_target}")
print(f"  Leggett ground state energy:   {F_Leggett:.4f} M_KK ({F_Leggett / abs(F_total) * 100:.4f}% of |F_total|)")
print(f"  Leggett excitation energy:     {Delta_E_L:.4f} M_KK ({Delta_E_L / abs(F_total) * 100:.4f}% of |F_total|)")
print(f"  Max Leggett 1-quantum energy:  {E_L_max_1quantum:.4f} M_KK ({E_L_max_1quantum / abs(F_total) * 100:.4f}% of |F_total|)")

# The CRITICAL ratio:
ratio_L_to_DM_target = F_Leggett / (Omega_DM_target * abs(F_total))
shortfall = Omega_DM_target * abs(F_total) / max(E_L_max_1quantum, 1e-30)
print(f"\n  Leggett / (DM target * |F_total|) = {ratio_L_to_DM_target:.6f}")
print(f"  Shortfall factor (DM target / max Leggett): {shortfall:.1f}x")

energetically_viable = (E_L_max_1quantum / abs(F_total)) > 0.01
print(f"\n  E_L/E_total > 0.01? {'YES' if energetically_viable else 'NO'} ({E_L_max_1quantum / abs(F_total):.6f})")

# ============================================================================
# 10. Cross-checks
# ============================================================================
print(f"\n{'=' * 72}")
print(f"CROSS-CHECKS")
print(f"{'=' * 72}")

# Check 1: Compare our F_Josephson with S56 estimate
# S56: F_Josephson = -N_bonds * E_J * m ~ -347 at fold
# Our computation uses bond-type-resolved E_J and m
# S56 used N_bonds_C2 only (50 bonds * E_J * m)
F_J_S56_style = -n_bonds_C2 * E_J_fold_fabric * m_C2
print(f"  Cross-check 1: F_J using C2 bonds only (S56 style)")
print(f"    F_J(C2 only) = {F_J_S56_style:.4f} M_KK")
print(f"    Our F_J(all types) = {F_Josephson:.4f} M_KK")
print(f"    su2+u1 correction: {(F_Josephson - F_J_S56_style)/F_J_S56_style*100:.2f}%")

# Check 2: E_J hierarchy
print(f"\n  Cross-check 2: Josephson coupling hierarchy")
print(f"    E_J_C2 / E_J_su2 = {E_J_C2_bond / E_J_su2_bond:.1f}")
print(f"    E_J_C2 / E_J_u1  = {E_J_C2_bond / E_J_u1_bond:.1f}")
print(f"    E_J_su2 / E_J_u1 = {E_J_su2_bond / E_J_u1_bond:.1f}")

# Check 3: Josephson dominance theorem (S56)
print(f"\n  Cross-check 3: Josephson dominance theorem")
n_modes_BA = 31
omega_mean = np.mean(omega_BA_fold)
dominance_ratio = n_bonds_total * E_J_fold_fabric / (n_modes_BA * omega_mean)
print(f"    N_bonds * E_J / (N_BA * omega_mean) = {n_bonds_total} * {E_J_fold_fabric:.3f} / ({n_modes_BA} * {omega_mean:.3f})")
print(f"    = {dominance_ratio:.2f} (S56 predicted ~14)")

# Check 4: S56 Josephson gap vs our E_J
CC_gap_S56 = float(d56_gge['CC_gap'])
E_J_gap_2cell = float(d56_gge['E_J_fold'])
print(f"\n  Cross-check 4: 2-cell Josephson gap")
print(f"    2-cell E_J = {E_J_gap_2cell:.4f} M_KK")
print(f"    Fabric E_J = {E_J_fold_fabric:.4f} M_KK")
print(f"    Ratio (fabric/2-cell) = {E_J_fold_fabric / E_J_gap_2cell:.3f}")

# ============================================================================
# 11. Save results
# ============================================================================
outpath = 'computations/session-57/s57_channel_energy_budget.npz'
np.savez(outpath,
    # Constants
    tau_fold=tau_fold,
    N_cells=N_cells,
    n_bonds_C2=n_bonds_C2,
    n_bonds_su2=n_bonds_su2,
    n_bonds_u1=n_bonds_u1,
    n_bonds_total=n_bonds_total,
    epsilon_Leggett=epsilon_L,
    T_GH=T_GH,
    omega_L0_canonical=omega_L0_canonical,

    # Josephson
    E_J_C2_bond=E_J_C2_bond,
    E_J_su2_bond=E_J_su2_bond,
    E_J_u1_bond=E_J_u1_bond,
    F_anomalous=F_anom,
    m_C2=m_C2,
    m_su2=m_su2,
    m_u1=m_u1,
    F_Josephson=F_Josephson,
    F_J_C2=F_J_C2,
    F_J_su2=F_J_su2,
    F_J_u1=F_J_u1,

    # BCS
    E_cond_per_cell=E_cond,
    F_BCS=F_BCS,

    # Leggett
    F_Leggett_uniform=F_Leggett_total,
    F_Leggett_dispersive=F_Leggett_dispersive,
    F_Leggett=F_Leggett,
    J_Leggett_fold=J_Leggett_fold,
    E_L_coupling_per_cell=E_L_coupling_per_cell,
    Delta_E_L_excited=Delta_E_L,
    E_L_max_1quantum=E_L_max_1quantum,

    # BA phonon
    F_BA=F_BA_fold,
    F_ZPE=F_ZPE_fold,
    F_thermal=F_thermal_fold,
    omega_BA_fold=omega_BA_fold,

    # Totals
    F_total=F_total,
    F_smooth=F_smooth,
    delta_F=delta_F,

    # Fractions
    frac_Josephson=frac_J,
    frac_BCS=frac_BCS,
    frac_Leggett=frac_L,
    frac_BA=frac_BA,

    # DM viability
    ratio_L_to_Ftotal=F_Leggett / abs(F_total),
    ratio_DeltaEL_to_Ftotal=Delta_E_L / abs(F_total),
    ratio_ELmax_to_Ftotal=E_L_max_1quantum / abs(F_total),
    shortfall_factor=shortfall,
    energetically_viable=energetically_viable,

    # Gate
    gate_name='CHANNEL-ENERGY-BUDGET-57',
    gate_verdict='INFO',
)

print(f"\nSaved: {outpath}")
print(f"\nDONE")
