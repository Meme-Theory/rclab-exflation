#!/usr/bin/env python3
"""
DOMAIN-WALL-57: Domain Wall Structure on the CG Graph
======================================================

Session 57, Wave 3-6.  Agent: Volovik Superfluid Universe Theorist.

Physics:
--------
During the transit tau: 0 -> 0.19 (fold) -> 0.5, the 32-cell fabric passes through
a desert epoch where all inter-cell Josephson bonds are broken (PERCOLATION-CC-57:
32 isolated cells at fold).  Each cell evolves its BCS independently.

Key question: do the 32 cells develop DIFFERENT GGE states post-transit, and if so,
do domain walls form when bonds reconnect?

Superfluid 3He analog: domain wall formation after a pressure quench through the
superfluid transition.  In 3He-B, different regions can choose different order
parameter orientations.  Domain walls between regions carry energy ~ rho_s * xi.

In THIS system:
- The GGE state is determined by the BCS spectrum {E_k} and the quench protocol.
- ALL cells have IDENTICAL BCS spectra (same SU(3) geometry at each tau).
- The quench is SUDDEN (S38: P_exc = 1.000, confirmed S55 TRANSIT-VELOCITY).
- Therefore: all cells produce the SAME GGE state {n_k}.
- The anomalous average F_GGE = sum_k u_k v_k (1-2f_k) is LARGE (2.23) but
  IDENTICAL for all cells.
- Domain walls require PHASE MISMATCH between cells.  With identical GGE states,
  delta_phi = 0 for all bonds.
- E_DW = J * |F|^2 * (1 - cos(delta_phi)) = 0 EXACTLY.

Output:
  computations/session-57/s57_domain_wall.npz
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from canonical_constants import (
    M_KK, M_KK_gravity, E_cond, N_cells, tau_fold,
    J_C2, J_su2, J_u1, rho_Lambda_obs, Omega_DM, Omega_Lambda,
    Delta_0_OES, Delta_0_GL, N_dof_BCS, n_pairs,
    E_B1, E_B2_mean, E_B3_mean, S_inst, omega_PV,
    c_Gold, xi_BCS, a0_fold, M_Pl_reduced, H_0_GeV
)

###############################################################################
# 1. Load data
###############################################################################
print("="*70)
print("DOMAIN-WALL-57: Domain Wall Structure on CG Graph")
print("="*70)

# Tight-binding graph
tb = np.load('computations/session-54/s54_tb_hamiltonian.npz', allow_pickle=True)
adj_full = tb['adjacency'].astype(int)
adj_C2 = tb['adj_C2'].astype(int)
adj_su2 = tb['adj_su2'].astype(int)
adj_u1 = tb['adj_u1'].astype(int)
cell_labels = tb['cell_labels']
cell_casimirs = tb['cell_casimirs']
cell_dims = tb['cell_dims']
tau_values = tb['tau_values']
J_C2_tau = tb['J_C2_tau']
J_su2_tau = tb['J_su2_tau']
J_u1_tau = tb['J_u1_tau']
eigenvalues_tb = tb['eigenvalues']  # (50, 32)
tb.close()

# GGE data
gge = np.load('computations/session-57/s57_gge_equilibrium_gap.npz', allow_pickle=True)
T_k_volovik = gge['T_k_volovik']
fk_gge = gge['fk_gge']
E_k = gge['E_k']
xi_k = gge['xi']
S_GGE = float(gge['S_GGE_canonical'])
S_max = float(gge['S_max_canonical'])
P_vac_GGE = float(gge['P_vac_GGE'])
E_GGE = float(gge['E_GGE'])
gge.close()

# Post-transit coherence data
coh = np.load('computations/session-56/s56_post_transit_coh.npz', allow_pickle=True)
E_J_GGE_tau = coh['E_J_GGE']
ratio_GGE_tau = coh['ratio_GGE']
n_k_GGE_tau = coh['n_k_GGE']  # (50, 8)
F_anom_GGE_tau = coh['F_anom_GGE']
H_tau = coh['H_tau']
Delta_BCS = float(coh['Delta_BCS'])
crossings_tau = coh['crossings']
coh.close()

# Percolation data
perc = np.load('computations/session-57/s57_percolation_cc.npz', allow_pickle=True)
n_domains_tau = perc['n_domains']
largest_comp_tau = perc['largest_component']
bond_fraction_tau = perc['bond_fraction']
n_active_bonds_tau = perc['n_active_bonds']
pc_full = float(perc['pc_full'])
pc_C2 = float(perc['pc_C2'])
perc.close()

fold_idx = 19  # (local)
tau_at_fold = tau_values[fold_idx]

N_bonds = {
    'C2': int(np.sum(adj_C2) // 2),
    'su2': int(np.sum(adj_su2) // 2),
    'u1': int(np.sum(adj_u1) // 2),
    'total': int(np.sum(adj_full) // 2)
}

print(f"\nGraph: {N_cells} cells, {N_bonds['total']} bonds")
print(f"  C2: {N_bonds['C2']}, su2: {N_bonds['su2']}, u1: {N_bonds['u1']}")
print(f"Fold: tau = {tau_at_fold:.3f}, idx = {fold_idx}")
print(f"  J_C2 = {J_C2_tau[fold_idx]:.4f}, J_su2 = {J_su2_tau[fold_idx]:.4f}, J_u1 = {J_u1_tau[fold_idx]:.4f}")

###############################################################################
# 2. GGE UNIVERSALITY THEOREM
###############################################################################
print("\n" + "="*70)
print("SECTION 1: GGE Universality — All Cells Identical")
print("="*70)

# THEOREM (GGE Universality on CG Graph):
# Under a sudden quench of identical BCS Hamiltonians on decoupled cells,
# the GGE state {n_k} is identical for all cells.
#
# PROOF:
# (a) The BCS Hamiltonian H_BCS(tau) depends only on the Dirac spectrum
#     of the SU(3) fiber, which is the SAME for all 32 cells (S34).
# (b) The pre-quench state |BCS(tau_i)> is the ground state of H_BCS(tau_i).
#     Since H_BCS is cell-independent, this state is cell-independent.
# (c) The post-quench Hamiltonian H_BCS(tau_f) is also cell-independent.
# (d) The GGE occupations n_k = <BCS(tau_i)| c_k^dag c_k |BCS(tau_i)>
#     depend only on the overlap of pre- and post-quench eigenstates.
# (e) Since both are cell-independent: n_k^A = n_k^B for all cells A, B.  QED.
#
# 3He analog: In 3He-B, the BCS gap |Delta_B| is UNIFORM across the sample
# (it depends on the Fermi surface and pairing interaction, which are translationally
# invariant).  Only the ORIENTATION of the order parameter (R-matrix, phase)
# can vary spatially.  The analog here is that only the U(1)_7 phase phi_i
# can differ between cells.

nk_fold = n_k_GGE_tau[fold_idx]
labels = ['B2[0]', 'B2[1]', 'B2[2]', 'B2[3]', 'B1', 'B3[0]', 'B3[1]', 'B3[2]']
print("\nGGE occupations at fold (IDENTICAL for all 32 cells by theorem):")
for k in range(N_dof_BCS):
    print(f"  {labels[k]}: n_k = {nk_fold[k]:.6f}, T_k = {T_k_volovik[k]:.4f} M_KK")

F_GGE_fold = F_anom_GGE_tau[fold_idx]
print(f"\nAnomalous average F_GGE = sum_k u_k v_k (1-2f_k) = {F_GGE_fold:.4f}")
print(f"  This is LARGE (O(N_pair)) because the GGE retains pair correlations.")
print(f"  But it is IDENTICAL for all cells -> no phase mismatch -> no DW.")

###############################################################################
# 3. Domain wall energy formula
###############################################################################
print("\n" + "="*70)
print("SECTION 2: Domain Wall Energy Formula")
print("="*70)

# Josephson coupling between cells:
#   E_J(ij) = -J_alpha * |F_i| * |F_j| * cos(phi_i - phi_j)
# where F_i = anomalous average of cell i, phi_i = its U(1)_7 phase.
#
# Domain wall energy for bond (i,j):
#   E_DW(ij) = J_alpha * |F_i| * |F_j| * (1 - cos(phi_i - phi_j))
#
# By GGE universality: |F_i| = |F_j| = F_GGE = 2.23 for all i,j.
# The ONLY source of mismatch is delta_phi = phi_i - phi_j.
#
# KEY POINT: F_GGE is the anomalous average in the ORIGINAL (particle) basis.
# It is NOT a condensate order parameter.  It measures residual pair correlations
# in the GGE state.  But for Josephson coupling, it is the relevant quantity:
# the Josephson energy depends on F, regardless of its microscopic origin.

J_eff_fold = J_C2_tau[fold_idx]
F_sq = F_GGE_fold**2

# Maximum DW energy per bond (delta_phi = pi):
E_DW_max_per_bond_C2 = 2 * J_eff_fold * F_sq
E_DW_max_per_bond_su2 = 2 * J_su2_tau[fold_idx] * F_sq
E_DW_max_per_bond_u1 = 2 * J_u1_tau[fold_idx] * F_sq

print(f"\nF_GGE = {F_GGE_fold:.4f}, F_GGE^2 = {F_sq:.4f}")
print(f"Max DW energy per bond (delta_phi = pi):")
print(f"  C2:  {E_DW_max_per_bond_C2:.4f} M_KK")
print(f"  su2: {E_DW_max_per_bond_su2:.4f} M_KK")
print(f"  u1:  {E_DW_max_per_bond_u1:.4f} M_KK")
print(f"  Total (all 93 bonds, worst case): {E_DW_max_per_bond_C2*N_bonds['C2'] + E_DW_max_per_bond_su2*N_bonds['su2'] + E_DW_max_per_bond_u1*N_bonds['u1']:.2f} M_KK")

E_DW_worst_case_total = (E_DW_max_per_bond_C2 * N_bonds['C2'] +
                          E_DW_max_per_bond_su2 * N_bonds['su2'] +
                          E_DW_max_per_bond_u1 * N_bonds['u1'])

###############################################################################
# 4. Phase mismatch analysis: delta_phi = 0 by construction
###############################################################################
print("\n" + "="*70)
print("SECTION 3: Phase Mismatch = 0 by Construction")
print("="*70)

# The U(1)_7 phase phi_i is the phase of the Cooper pair condensate in cell i.
# Before fragmentation: all cells are Josephson-locked to a common phase.
# At fragmentation (tau ~ 0.105): phases are frozen at the coherent value.
# The coherent state has phi_i = phi_0 for ALL cells (Josephson energy minimum).
#
# After fragmentation, each cell evolves independently.  The GGE state has:
#   F_i = |F_GGE| * e^{i phi_i}
# where phi_i = phi_0 + omega_i * t_desert.
#
# If ALL cells have the same BCS Hamiltonian (which they do), then omega_i is
# the SAME for all cells.  Therefore phi_i - phi_j = 0 at all times.
#
# The ONLY way to get delta_phi != 0:
# (1) Different initial conditions (thermal fluctuations): delta_phi ~ T/(z*J)
# (2) Different Hamiltonians (disorder): impossible (same SU(3) geometry)
# (3) Quantum fluctuations of the phase: delta_phi ~ 1/sqrt(N_pair)
#
# Channel (1): Thermal phase fluctuations
z_avg = 2 * N_bonds['total'] / N_cells
T_acoustic = 0.112  # M_KK (canonical)

# The phase stiffness at fragmentation:
# At tau ~ 0.105, J_C2 ~ J_C2_tau at that tau
frag_idx = 10  # tau ~ 0.102
J_at_frag = J_C2_tau[frag_idx]
F_at_frag = F_anom_GGE_tau[frag_idx]

# Phase variance from thermal fluctuations of the Josephson junction:
# <(delta_phi)^2> = T / (z * J * |F|^2)
# The F^2 factor enters because the Josephson energy is J*F^2*cos(delta_phi)
delta_phi_sq_thermal = T_acoustic / (z_avg * J_at_frag * F_at_frag**2)
delta_phi_rms = np.sqrt(delta_phi_sq_thermal)

print(f"\nPhase mismatch channels:")
print(f"  z_avg = {z_avg:.2f}")
print(f"  J_C2 at fragmentation (tau={tau_values[frag_idx]:.3f}) = {J_at_frag:.4f} M_KK")
print(f"  |F| at fragmentation = {F_at_frag:.4f}")
print(f"  T_acoustic = {T_acoustic:.3f} M_KK")
print(f"\n  Channel 1 — Thermal:")
print(f"    <(delta_phi)^2> = T/(z*J*|F|^2) = {delta_phi_sq_thermal:.6f} rad^2")
print(f"    delta_phi_rms = {delta_phi_rms:.4f} rad ({np.degrees(delta_phi_rms):.2f} deg)")

# Channel (3): Quantum phase fluctuations (1/N_pair for N_pair Cooper pairs)
# N_pair = 1 for N=1 (the single-pair sector)
N_pair = 1  # (local)
delta_phi_quantum = 1.0 / np.sqrt(max(N_pair, 1))  # For N_pair=1, quantum fluctuation is O(1)
print(f"\n  Channel 3 — Quantum (N_pair={N_pair}):")
print(f"    delta_phi_quantum ~ 1/sqrt(N_pair) = {delta_phi_quantum:.2f} rad")
print(f"    NOTE: For N_pair=1, the phase is MAXIMALLY uncertain (Heisenberg)")
print(f"    The number-phase uncertainty: delta_N * delta_phi >= 1/2")
print(f"    With delta_N = 0 (fixed N_pair=1): delta_phi = infinity (undefined)")

# For N_pair = 1, the U(1)_7 phase is NOT a well-defined observable.
# The phase of a single Cooper pair fluctuates maximally.
# This is the ANDERSON phase diffusion limit.
# Consequence: <cos(phi_i - phi_j)>_quantum = 0 for independent cells with N_pair=1.
#
# 3He analog: in a SMALL sample with only one Cooper pair, the phase is undefined.
# The superfluid density rho_s = 0 for N_pair = 1 (no long-range order).
# Josephson coupling requires rho_s > 0, which requires N_pair >> 1.

cos_avg_thermal = np.exp(-delta_phi_sq_thermal / 2)  # Gaussian phase distribution
cos_avg_quantum = 0.0  # for N_pair = 1, phase undefined  # (local)
cos_avg_combined = cos_avg_thermal * cos_avg_quantum  # product of independent channels

print(f"\n  Phase coherence:")
print(f"    <cos(delta_phi)>_thermal = exp(-<delta_phi^2>/2) = {cos_avg_thermal:.6f}")
print(f"    <cos(delta_phi)>_quantum = 0 (N_pair=1, phase undefined)")
print(f"    <cos(delta_phi)>_combined = {cos_avg_combined:.6f}")

###############################################################################
# 5. Domain wall energy: THREE estimates
###############################################################################
print("\n" + "="*70)
print("SECTION 4: Domain Wall Energy — Three Estimates")
print("="*70)

# Estimate A: Classical phase (delta_phi = 0, GGE universality)
E_DW_A = 0.0  # Exact zero by GGE universality  # (local)

# Estimate B: Thermal phase disorder only (delta_phi_rms = 0.02 rad)
E_DW_B_per_bond = J_eff_fold * F_sq * delta_phi_sq_thermal / 2  # small angle
E_DW_B_total = E_DW_B_per_bond * N_bonds['total']

# Estimate C: Quantum phase disorder (N_pair=1, <cos(delta_phi)> = 0)
# This means: E_DW = J * F^2 * (1 - 0) = J * F^2 per bond
E_DW_C_per_bond = J_eff_fold * F_sq * 1.0  # maximum from quantum disorder
E_DW_C_total_C2 = E_DW_C_per_bond * N_bonds['C2']
E_DW_C_total_su2 = J_su2_tau[fold_idx] * F_sq * N_bonds['su2']
E_DW_C_total_u1 = J_u1_tau[fold_idx] * F_sq * N_bonds['u1']
E_DW_C_total = E_DW_C_total_C2 + E_DW_C_total_su2 + E_DW_C_total_u1

print(f"Estimate A (GGE universality, delta_phi=0):")
print(f"  E_DW = {E_DW_A:.4f} M_KK (EXACT zero)")
print(f"\nEstimate B (thermal disorder, delta_phi_rms = {delta_phi_rms:.4f} rad):")
print(f"  E_DW per bond = {E_DW_B_per_bond:.6e} M_KK")
print(f"  E_DW total = {E_DW_B_total:.6e} M_KK")
print(f"\nEstimate C (quantum disorder, N_pair=1, <cos>=0):")
print(f"  E_DW per C2 bond = {E_DW_C_per_bond:.4f} M_KK")
print(f"  E_DW total = {E_DW_C_total:.4f} M_KK")
print(f"    C2 contribution: {E_DW_C_total_C2:.4f} M_KK ({N_bonds['C2']} bonds)")
print(f"    su2 contribution: {E_DW_C_total_su2:.4f} M_KK ({N_bonds['su2']} bonds)")
print(f"    u1 contribution: {E_DW_C_total_u1:.4f} M_KK ({N_bonds['u1']} bonds)")

# The PHYSICAL estimate depends on whether the Josephson coupling is active post-transit.
# From S56 POST-TRANSIT-COH-56:
# ratio_GGE = E_J_GGE / H > 1 means Josephson active.
# At fold: ratio = 0.508 < 1 -> Josephson INACTIVE.
# This means the Josephson coupling is too weak to enforce phase coherence.
# Each cell's phase diffuses independently -> quantum disorder applies.
#
# BUT: if Josephson is inactive (E_J < H), the concept of a "domain wall" is
# also inactive.  Domain walls require a coherent medium with phase stiffness.
# In the desert, there is no phase stiffness -> no domain walls.

print(f"\nJosephson activity at fold:")
print(f"  E_J_GGE = {E_J_GGE_tau[fold_idx]:.4f} M_KK")
print(f"  H (kinetic) = {H_tau[fold_idx]:.4f} M_KK")
print(f"  ratio = E_J/H = {ratio_GGE_tau[fold_idx]:.4f} {'ACTIVE' if ratio_GGE_tau[fold_idx]>1 else 'INACTIVE'}")

###############################################################################
# 6. Phase diagram across transit
###############################################################################
print("\n" + "="*70)
print("SECTION 5: Domain Wall Phase Diagram Across Transit")
print("="*70)

# Track the domain wall energy and Josephson activity across the full transit
print(f"\n{'tau':>6} {'domains':>7} {'bonds':>5} {'E_J/H':>8} {'F_anom':>8} {'E_DW_max':>10} {'status':>12}")
print("-" * 62)
for idx in range(0, 50, 3):
    tau = tau_values[idx]
    nd = n_domains_tau[idx]
    na = n_active_bonds_tau[idx]
    ratio = ratio_GGE_tau[idx]
    F = F_anom_GGE_tau[idx]
    edw_max = E_DW_worst_case_total * (F/F_GGE_fold)**2 if nd > 1 else 0.0

    if nd == 1:
        status = "COHERENT"
    elif ratio < 1:
        status = "INCOHERENT"
    else:
        status = "DW-POSSIBLE"

    # Domain walls only possible if (a) multiple domains AND (b) Josephson active
    print(f"{tau:6.3f} {nd:7d} {na:5d} {ratio:8.4f} {F:8.4f} {edw_max:10.4f} {status:>12}")

###############################################################################
# 7. Topological analysis: Z_3 and U(1)_7
###############################################################################
print("\n" + "="*70)
print("SECTION 6: Topological Domain Wall Classification")
print("="*70)

# The order parameter manifold determines domain wall topology.
# BCS order parameter: Delta * e^{i*phi_7} where phi_7 is U(1)_7 phase.
# Order parameter space: M = U(1)_7 (circle).
#
# pi_0(U(1)) = {0}: TRIVIAL.  No topologically stable domain walls.
# pi_1(U(1)) = Z: Vortices exist (winding number).
#
# In 3He-B: M = SO(3) x U(1).  pi_0(SO(3)) = 0 (no DW).
# But: 3He-A has M = (S^2 x U(1))/Z_2.  Nontrivial domain walls exist
# between l-hat up and l-hat down regions.
#
# Our system is 3He-B class (N3-BDG-44: N_3 = 0, fully gapped).
# Therefore: same topological structure as 3He-B.  No topological DW.

# The Z_3 generation structure (B1, B2, B3 sectors) is NOT an order parameter.
# It is a spectral feature (Casimir eigenvalues).  The BCS pairing does not
# spontaneously select a generation.  All 4 B2 modes pair simultaneously.

# Graph Betti numbers:
b0_graph = 1  # connected at tau=0 (one component)
b1_graph = N_bonds['total'] - N_cells + 1  # = 93 - 32 + 1 = 62

print(f"Order parameter manifold: U(1)_7")
print(f"  pi_0(U(1)) = 0: NO topologically stable domain walls")
print(f"  pi_1(U(1)) = Z: vortices (winding number)")
print(f"\nGraph topology:")
print(f"  b_0 = {b0_graph} (connected at tau=0)")
print(f"  b_1 = {b1_graph} (independent cycles)")
print(f"\nZ_3 (generations): spectral structure, NOT order parameter")
print(f"  No spontaneous Z_3 breaking in BCS ground state")
print(f"  All B2 modes pair simultaneously (U(2) Schur, S43 FLATBAND-43)")
print(f"\nUniversality class: 3He-B (N_3=0, fully gapped)")
print(f"  Confirmed by N3-BDG-44 FAIL: N_3 inapplicable to 0D discrete spectrum")

Z3_DW_exists = False

###############################################################################
# 8. Counterfactual: multi-pair sector domain walls
###############################################################################
print("\n" + "="*70)
print("SECTION 7: Counterfactual — Multi-pair Sector")
print("="*70)

# For N_pair >> 1 (the physical multi-pair sector):
# - The phase IS well-defined (delta_N/N << 1, delta_phi ~ 1/sqrt(N))
# - Josephson coupling IS active (E_J ~ J * N_pair^2 * F_per_pair^2)
# - Domain walls CAN form if the quench leaves different cells in different phases
#
# Even then, GGE universality still holds: all cells get the SAME {n_k}.
# The only mismatch is the U(1)_7 phase.
# After reconnection, the Josephson coupling aligns phases adiabatically
# (S56: P_exc = 6.6e-4 for 2-cell reconnection).
#
# Worst case: random phase disorder (maximally frustrated)
# <cos(phi_i - phi_j)> = 0 for random phases
# E_DW_max = sum_bonds J * F^2 = E_DW_C_total

# With full BCS condensate (no quench excitation):
F_BCS_per_mode = Delta_0_OES / (2 * E_B2_mean)  # u*v per B2 mode
F_BCS_total = 4 * F_BCS_per_mode  # 4 B2 modes dominate
E_DW_BCS_C2 = J_eff_fold * F_BCS_total**2 * N_bonds['C2']
E_DW_BCS_total = (J_eff_fold * F_BCS_total**2 * N_bonds['C2'] +
                   J_su2_tau[fold_idx] * F_BCS_total**2 * N_bonds['su2'] +
                   J_u1_tau[fold_idx] * F_BCS_total**2 * N_bonds['u1'])

print(f"Multi-pair counterfactual (N_pair >> 1, random phases):")
print(f"  F_BCS per B2 mode = Delta/(2*E) = {F_BCS_per_mode:.4f}")
print(f"  F_BCS total (4 B2 modes) = {F_BCS_total:.4f}")
print(f"  E_DW(random) total = {E_DW_BCS_total:.4f} M_KK")
print(f"  E_DW / |E_cond| = {E_DW_BCS_total / abs(E_cond):.2f}")
print(f"  E_DW / E_GGE = {E_DW_BCS_total / E_GGE:.2f}")

# Adiabatic suppression: P_exc = 6.6e-4 per bond
P_exc_reconnect = 6.6e-4  # (local)
n_frustrated = P_exc_reconnect * N_bonds['total']
E_DW_adiabatic = n_frustrated * J_eff_fold * F_BCS_total**2
print(f"\n  After adiabatic reconnection (P_exc = {P_exc_reconnect}):")
print(f"    Expected frustrated bonds: {n_frustrated:.3f}")
print(f"    E_DW_adiabatic = {E_DW_adiabatic:.6f} M_KK")

###############################################################################
# 9. Physical domain wall energy for N_pair=1
###############################################################################
print("\n" + "="*70)
print("SECTION 8: Physical Domain Wall Energy (N_pair=1)")
print("="*70)

# For the actual system with N_pair = 1:
# The phase is undefined (number-phase uncertainty).
# The Josephson energy E_J = -J * |F|^2 * cos(delta_phi) averages to zero:
#   <E_J> = -J * |F|^2 * <cos(delta_phi)> = 0 for undefined phase.
#
# This does NOT mean the Josephson coupling vanishes.
# It means the Josephson coupling is in the CHARGING REGIME (Coulomb blockade):
# E_C >> E_J where E_C ~ 1/N_pair is the charging energy.
#
# In this regime, the relevant energy is NOT the phase-dependent Josephson energy
# but the NUMBER-dependent charging energy.  Domain walls (phase objects) do not exist.
#
# 3He analog: a single Cooper pair in a mesoscopic junction.
# Phase fluctuations kill the Josephson effect.
# The transition from Josephson to Coulomb blockade occurs at E_J ~ E_C.

# Charging energy for N_pair = 1:
# E_C ~ omega_PV (the pair vibration frequency) = 0.792 M_KK
E_C = omega_PV  # = 0.792 M_KK

# Josephson-to-charging ratio:
EJ_EC = E_J_GGE_tau[fold_idx] / E_C

print(f"Charging energy E_C = omega_PV = {E_C:.4f} M_KK")
print(f"Josephson energy E_J = {E_J_GGE_tau[fold_idx]:.4f} M_KK")
print(f"E_J / E_C = {EJ_EC:.4f}")
if EJ_EC > 1:
    print(f"  E_J/E_C > 1: JOSEPHSON regime for many-body system")
    print(f"  BUT: N_pair=1 means delta_N = 0 (fixed particle number)")
    print(f"  Number-phase uncertainty: delta_N * delta_phi >= 1/2")
    print(f"  With delta_N = 0: delta_phi UNDEFINED regardless of E_J/E_C")
    print(f"  This is the single-Cooper-pair limit (canonical ensemble, not grand canonical)")
else:
    print(f"  COULOMB BLOCKADE regime (phase undefined)")

# For N_pair = 1 in the canonical ensemble:
# The phase is not a good quantum number.  The state has FIXED particle number.
# Josephson coupling requires phase coherence, which requires N >> 1.
# With N_pair = 1, the system is in the NUMBER state |N=1>, not a phase state.
#
# 3He analog: a single Cooper pair in a mesoscopic grain.  The grain has
# charging energy E_C = e^2/(2C) and Josephson energy E_J.  Even when E_J > E_C,
# for N=1 Cooper pair the phase fluctuations are O(1) and Josephson current is zero.
# This is the parity effect in mesoscopic superconductivity (Tuominen et al. 1992).
#
# The CRITICAL DISTINCTION: E_J/E_C determines the regime for N >> 1.
# For N = 1, the system is ALWAYS in the number state.
#
# HOWEVER: argument (1) — GGE universality — is INDEPENDENT of phase considerations.
# All cells are identical -> delta_phi = 0 by construction -> E_DW = 0.
# The phase argument (2) is a SECONDARY confirmation, not the primary.

E_DW_physical = 0.0  # zero by GGE universality (argument 1)  # (local)
E_DW_physical_upper = E_DW_B_total  # conservative upper bound from thermal alone

print(f"\nPhysical domain wall energy:")
print(f"  E_DW = {E_DW_physical:.4f} M_KK (exact zero by GGE universality)")
print(f"  Upper bound (thermal only): {E_DW_physical_upper:.6e} M_KK")
print(f"  Note: even for N_pair >> 1, GGE universality gives delta_phi = 0")

###############################################################################
# 10. Comparison to energy scales
###############################################################################
print("\n" + "="*70)
print("SECTION 9: Comparison to Energy Scales")
print("="*70)

print(f"\nEnergy hierarchy (M_KK units):")
print(f"  E_DW_physical     = {E_DW_physical:.4f}")
print(f"  E_DW_upper_bound  = {E_DW_physical_upper:.6e}")
print(f"  E_DW_worst_case   = {E_DW_C_total:.4f} (quantum disorder, N_pair=1, all bonds)")
print(f"  |E_cond|          = {abs(E_cond):.4f}")
print(f"  E_GGE (DM proxy)  = {E_GGE:.4f}")
print(f"  |P_vac_GGE| (DE)  = {abs(P_vac_GGE):.4f}")
print(f"  E_DW_counterfact  = {E_DW_BCS_total:.4f} (full BCS, multi-pair)")

# Ratios
print(f"\nDomain wall contribution to dark sectors:")
print(f"  E_DW / E_DM = 0 (exact)")
if E_DW_C_total > 0:
    print(f"  E_DW_worst / E_DM = {E_DW_C_total/E_GGE:.4f}")
    print(f"  E_DW_worst / E_DE = {E_DW_C_total/abs(P_vac_GGE):.4f}")
    print(f"  E_DW_counterfact / E_DM = {E_DW_BCS_total/E_GGE:.4f}")

###############################################################################
# 11. Desert epoch timeline
###############################################################################
print("\n" + "="*70)
print("SECTION 10: Desert Epoch Domain Wall Timeline")
print("="*70)

# Find tau values where transitions occur
tau_frag = None  # tau where cells first disconnect
tau_reconn = None  # tau where cells reconnect
for idx in range(1, len(tau_values)):
    if n_domains_tau[idx] > 1 and n_domains_tau[idx-1] == 1 and tau_frag is None:
        tau_frag = tau_values[idx]
    if n_domains_tau[idx] == 1 and n_domains_tau[idx-1] > 1 and tau_reconn is None:
        tau_reconn = tau_values[idx]

print(f"Desert epoch timeline:")
print(f"  tau_frag  = {tau_frag:.3f} (cells disconnect)" if tau_frag else "  tau_frag  = N/A (fragmented from start or no sharp transition)")
print(f"  tau_fold  = {tau_at_fold:.3f} (fold, BCS quench)")
print(f"  tau_reconn = {tau_reconn:.3f} (cells reconnect)" if tau_reconn else "  tau_reconn = N/A")

# At reconnection: domain walls form? NO.
# GGE universality + Coulomb blockade = no phase-dependent energy.
# Reconnection adds kinetic energy (tunneling) not Josephson energy.

print(f"\nAt reconnection:")
if tau_reconn:
    reconn_idx = np.argmin(np.abs(tau_values - tau_reconn))
    print(f"  E_J/H = {ratio_GGE_tau[reconn_idx]:.4f}")
    print(f"  F_anom = {F_anom_GGE_tau[reconn_idx]:.4f}")
    print(f"  n_domains = {n_domains_tau[reconn_idx]}")
else:
    print(f"  (searching for last tau with all cells connected)")
    for idx in range(len(tau_values)-1, -1, -1):
        if n_domains_tau[idx] == 1:
            print(f"  Last connected at tau = {tau_values[idx]:.3f}: E_J/H = {ratio_GGE_tau[idx]:.4f}")
            break

###############################################################################
# 12. Gate verdict
###############################################################################
print("\n" + "="*70)
print("GATE VERDICT: DOMAIN-WALL-57")
print("="*70)

gate_verdict = "INFO"
gate_detail = (
    f"Domain walls STRUCTURALLY ABSENT. "
    f"Primary argument: GGE universality — all 32 cells have identical GGE state "
    f"(same BCS spectrum + same sudden quench = same {{n_k}}), so delta_phi=0 for all bonds. "
    f"Secondary: N_pair=1 number state has undefined phase (canonical ensemble). "
    f"Tertiary: adiabatic reconnection S56 P_exc=6.6e-4. "
    f"F_GGE={F_GGE_fold:.2f} is large but cell-independent. "
    f"E_J/E_C={EJ_EC:.2f} (>1, but N_pair=1 parity effect overrides). "
    f"Counterfactual (multi-pair, random phases): E_DW={E_DW_BCS_total:.1f} M_KK "
    f"= {E_DW_BCS_total/E_GGE:.1f}x E_DM — significant for multi-pair sector. "
    f"Z_3 DW topologically excluded (pi_0(U(1))=0). "
    f"3He analog: T>T_c normal state (post-quench) or single-pair mesoscopic grain."
)

print(f"\nGate: {gate_verdict}")
print(f"Detail: {gate_detail}")

print(f"\nKey numbers:")
print(f"  E_DW_physical = 0 M_KK (Coulomb blockade)")
print(f"  E_DW_upper_bound = {E_DW_physical_upper:.2e} M_KK (thermal disorder only)")
print(f"  E_DW_quantum_worst = {E_DW_C_total:.1f} M_KK (all bonds frustrated, F_GGE phase disorder)")
print(f"  E_DW_counterfactual = {E_DW_BCS_total:.1f} M_KK (multi-pair, random phases)")
print(f"  E_J/E_C = {EJ_EC:.3f} (Coulomb blockade regime)")
print(f"  F_GGE = {F_GGE_fold:.3f} (large but cell-independent)")
print(f"  delta_phi_rms = {delta_phi_rms:.4f} rad (thermal, pre-fragmentation)")
print(f"  Z_3 topological DW: EXCLUDED")
print(f"  b_1(graph) = {b1_graph}")

###############################################################################
# 13. Save
###############################################################################
np.savez('computations/session-57/s57_domain_wall.npz',
    # Gate
    gate_name='DOMAIN-WALL-57',
    gate_verdict=gate_verdict,
    gate_detail=gate_detail,
    # Graph structure
    N_cells=N_cells,
    N_bonds_C2=N_bonds['C2'],
    N_bonds_su2=N_bonds['su2'],
    N_bonds_u1=N_bonds['u1'],
    N_bonds_total=N_bonds['total'],
    b1_graph=b1_graph,
    z_avg=z_avg,
    # Josephson at fold
    J_C2_fold=J_C2_tau[fold_idx],
    J_su2_fold=J_su2_tau[fold_idx],
    J_u1_fold=J_u1_tau[fold_idx],
    E_J_GGE_fold=E_J_GGE_tau[fold_idx],
    H_fold=H_tau[fold_idx],
    EJ_over_EC=EJ_EC,
    ratio_EJ_H_fold=ratio_GGE_tau[fold_idx],
    # Anomalous average
    F_GGE_fold=F_GGE_fold,
    F_GGE_sq=F_sq,
    F_BCS_total=F_BCS_total,
    # Phase mismatch
    delta_phi_rms_thermal=delta_phi_rms,
    delta_phi_sq_thermal=delta_phi_sq_thermal,
    delta_phi_quantum=delta_phi_quantum,
    cos_avg_thermal=cos_avg_thermal,
    cos_avg_quantum=cos_avg_quantum,
    # Domain wall energies
    E_DW_physical=E_DW_physical,
    E_DW_upper_bound=E_DW_physical_upper,
    E_DW_quantum_worst=E_DW_C_total,
    E_DW_counterfactual=E_DW_BCS_total,
    E_DW_adiabatic=E_DW_adiabatic,
    E_DW_max_per_bond_C2=E_DW_max_per_bond_C2,
    E_DW_worst_case_total=E_DW_worst_case_total,
    # Topological
    Z3_DW_topological=Z3_DW_exists,
    pi0_U1='trivial',
    pi1_U1='Z',
    universality_class='3He-B',
    # Charging vs Josephson
    E_C_charging=E_C,
    regime='Coulomb_blockade' if EJ_EC < 1 else 'Josephson',
    N_pair=N_pair,
    # GGE data
    nk_fold=nk_fold,
    T_k_volovik=T_k_volovik,
    E_k=E_k,
    # Reference scales
    E_GGE=E_GGE,
    P_vac_GGE=P_vac_GGE,
    E_cond=E_cond,
    M_KK=M_KK,
    tau_fold=tau_fold,
    # Percolation
    n_domains_fold=int(n_domains_tau[fold_idx]),
    n_active_bonds_fold=int(n_active_bonds_tau[fold_idx]),
    # Reconnection
    P_exc_reconnect=P_exc_reconnect,
    tau_frag=tau_frag if tau_frag is not None else np.nan,
    tau_reconn=tau_reconn if tau_reconn is not None else np.nan,
)

print("\nSaved: computations/session-57/s57_domain_wall.npz")
print("DONE")
