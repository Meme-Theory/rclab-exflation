"""
S57 FABRIC-KZ-QUENCH-57: Kibble-Zurek Defect Density on 32-Cell Fabric
========================================================================

Applies the Kibble-Zurek (KZ) mechanism to the BCS phase transition on
the 32-cell Josephson fabric during the tau-transit.

Key physics:
  1. The BCS transition is NOT a standard second-order phase transition
     with a critical point where Delta -> 0. The gap Delta(tau) is
     NONZERO at every tau (BCS is a 1D theorem: any g>0 pairs).
  2. What actually happens: the JOSEPHSON BONDS fragment at tau = 0.105,
     isolating all 32 cells. This is a first-order percolation transition,
     not a continuous phase transition.
  3. The physical transit is at Mach 2700 relative to the Josephson sound
     speed. Phase correlations freeze at cos(phi) = 0.935 throughout.
  4. L/xi_GL = 0.031 for each cell: every cell is deep in the 0D limit
     where standard KZ does not apply.

The computation addresses: can KZ produce defects on the fabric, and if
so, what is the density? The answer will turn on whether we treat the
quench as (a) passage through a critical point (standard KZ) or (b) a
sudden quench of an already-fragmented set of 0D systems.

Gate: FABRIC-KZ-QUENCH-57 = INFO

Author: Kitaev-Quantum-Chaos-Theorist (Session 57, W3-7)
"""

import numpy as np
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from canonical_constants import (
    tau_fold,
    omega_tau,           # 8.27 M_KK — transit frequency
    omega_PV,            # 0.792 M_KK — pair vibration
    omega_att,           # 1.430 M_KK — attractor frequency
    Delta_0_GL,          # 0.770 M_KK — GL gap
    Delta_0_OES,         # 0.464 M_KK — OES gap
    S_inst,              # 0.069 — instanton action
    xi_BCS,              # 0.808 M_KK^{-1}
    xi_GL,               # 0.976 M_KK^{-1}
    L_over_xi,           # 0.031 — 0D limit
    H_fold,              # 586.5 M_KK — Hubble at fold
    dt_transit,          # 0.00113 M_KK^{-1}
    v_terminal,          # 26.54 M_KK
    P_exc_kz,            # 1.0 — single-cell sudden-quench P_exc
    N_cells,             # 32
    E_cond,              # -0.137 M_KK
    barrier_0d,          # 0.0047 M_KK
    Gamma_Langer_BCS,    # 0.250 M_KK
    J_C2, J_su2, J_u1,  # Josephson couplings
    T_acoustic,          # 0.112 M_KK
    N_dof_BCS,           # 8 modes
    c_fabric,            # 210.0 M_KK — fabric sound speed
)

# ============================================================================
# 0. Load fabric graph and BCS spectrum data
# ============================================================================
data_dir = os.path.dirname(__file__)

# Graph structure
d_tb = np.load(os.path.join(data_dir, 's54_tb_hamiltonian.npz'), allow_pickle=True)
adjacency = d_tb['adjacency']
tau_tb = d_tb['tau_values']
eigenvalues_tb = d_tb['eigenvalues']  # (50, 32) tight-binding spectrum
bandwidths = d_tb['bandwidths']
diameter = int(d_tb['diameter'])
J_C2_tau = d_tb['J_C2_tau']
J_su2_tau = d_tb['J_su2_tau']
J_u1_tau = d_tb['J_u1_tau']

# BCS spectrum
d_ed = np.load(os.path.join(data_dir, 's54_ed_sweep.npz'), allow_pickle=True)
tau_ed = d_ed['tau_values']
E_cond_A = d_ed['E_cond_A']
E_cond_B = d_ed['E_cond_B']
E_sp_sweep = d_ed['E_sp_sweep']  # (50, 8) single-particle energies
all_evals = d_ed['all_eigenvalues']  # (50, 256) many-body eigenvalues
fold_idx = int(d_ed['fold_idx'])

# Scale factor
d_sf = np.load(os.path.join(data_dir, 's54_scale_factor.npz'), allow_pickle=True)
tau_sf = d_sf['tau']
H_sf = d_sf['H']

print("=" * 72)
print("S57 FABRIC-KZ-QUENCH-57: KIBBLE-ZUREK ON 32-CELL FABRIC")
print("=" * 72)

# ============================================================================
# 1. DIAGNOSTIC: Does the BCS gap vanish anywhere?
# ============================================================================
print("\n" + "=" * 72)
print("SECTION 1: BCS GAP PROFILE Delta(tau)")
print("=" * 72)

# The many-body gap: E_1 - E_0 at each tau
E0 = all_evals[:, 0]
E1 = all_evals[:, 1]
Delta_MB = E1 - E0  # Many-body gap

print(f"\n  Many-body gap Delta_MB = E_1 - E_0:")
print(f"    min over all tau: {np.min(Delta_MB):.6f} M_KK")
print(f"    max over all tau: {np.max(Delta_MB):.6f} M_KK")
print(f"    at fold (tau={tau_ed[fold_idx]:.3f}): {Delta_MB[fold_idx]:.6f} M_KK")

# Does Delta_MB ever vanish?
gap_zero = np.any(Delta_MB < 1e-10)
print(f"\n  Does the many-body gap vanish? {gap_zero}")
if not gap_zero:
    print(f"  -> NO CRITICAL POINT WHERE Delta -> 0.")
    print(f"     The BCS transition is always gapped.")
    print(f"     Standard KZ requires passage through a critical point.")
    print(f"     THE GAP NEVER CLOSES -> KZ INAPPLICABLE IN STANDARD FORM.")

# Condensation energy (the "order parameter" energy)
print(f"\n  Condensation energy E_cond(tau):")
print(f"    E_cond_A at fold: {E_cond_A[fold_idx]:.6f} M_KK")
print(f"    E_cond_B at fold: {E_cond_B[fold_idx]:.6f} M_KK")
print(f"    E_cond_A range: [{np.min(E_cond_A):.6f}, {np.max(E_cond_A):.6f}]")
print(f"    E_cond_B range: [{np.min(E_cond_B):.6f}, {np.max(E_cond_B):.6f}]")
print(f"    E_cond NEVER vanishes -> pairing persists at all tau.")

# ============================================================================
# 2. THE 0D LIMIT: Standard KZ does not apply to single cells
# ============================================================================
print("\n" + "=" * 72)
print("SECTION 2: ZERO-DIMENSIONAL LIMIT — KZ INAPPLICABLE PER CELL")
print("=" * 72)

L_sys = L_over_xi * xi_GL  # = 0.031 * 0.976 = 0.030 M_KK^{-1}
print(f"\n  Single-cell effective size:")
print(f"    L/xi_GL = {L_over_xi}")
print(f"    L_sys   = L_over_xi * xi_GL = {L_sys:.6f} M_KK^{{-1}}")
print(f"    xi_GL   = {xi_GL:.6f} M_KK^{{-1}}")
print(f"    xi_BCS  = {xi_BCS:.6f} M_KK^{{-1}}")

print(f"\n  CONCLUSION: L_sys / xi_BCS = {L_sys / xi_BCS:.4f}")
print(f"  The system is {1.0 / (L_sys / xi_BCS):.0f}x smaller than the coherence length.")
print(f"  In this regime:")
print(f"    - No spatial structure within a cell (homogeneous condensate)")
print(f"    - No domain walls or vortices can form WITHIN a cell")
print(f"    - KZ defects require spatial extent >> xi; here L << xi")
print(f"    - The cell is a single quantum DOF (pair vibrator), not a field theory")

# ============================================================================
# 3. KZ CRITICAL EXPONENTS (for completeness)
# ============================================================================
print("\n" + "=" * 72)
print("SECTION 3: KZ CRITICAL EXPONENTS (FORMAL)")
print("=" * 72)

# Mean-field BCS: z=2, nu=1/2 (Ginzburg-Landau universality)
z_mf = 2.0  # (local)
nu_mf = 0.5  # (local)
d_eff = 0  # Each cell is 0D

# For the FABRIC as a whole, the effective dimension is the spectral
# dimension d_s = 2.0 of the Cayley graph (from S54)
d_s = 2.0  # (local)

# KZ correlation length exponent: nu / (1 + z*nu)
kz_xi_exp_mf = nu_mf / (1 + z_mf * nu_mf)   # 0.5/2.0 = 0.25
kz_xi_exp_ball = nu_mf / (1 + 1.0 * nu_mf)   # 0.5/1.5 = 1/3

# KZ defect density exponent: d*nu / (1 + z*nu)
# For d=0: n_def exponent = 0. No KZ defects in 0D. Period.
kz_def_exp_0d = d_eff * nu_mf / (1 + z_mf * nu_mf)  # 0
kz_def_exp_2d = d_s * nu_mf / (1 + z_mf * nu_mf)    # 2*0.5/2 = 0.5

print(f"  Mean-field BCS: z = {z_mf}, nu = {nu_mf}")
print(f"  xi_KZ exponent (mf): nu/(1+z*nu) = {kz_xi_exp_mf:.4f}")
print(f"  xi_KZ exponent (ballistic z=1): nu/(1+z*nu) = {kz_xi_exp_ball:.4f}")
print(f"\n  Defect density exponent n_def ~ tau_Q^{{-d*nu/(1+z*nu)}}:")
print(f"    d=0 (single cell): exponent = {kz_def_exp_0d:.4f} -> NO DEFECTS")
print(f"    d_s=2 (fabric):    exponent = {kz_def_exp_2d:.4f}")

# ============================================================================
# 4. QUENCH PARAMETERS
# ============================================================================
print("\n" + "=" * 72)
print("SECTION 4: QUENCH PARAMETERS")
print("=" * 72)

# Quench rate: tau_Q is the timescale over which the control parameter
# changes by O(1). For the tau-transit:
# tau_Q = |tau_range| / |dtau/dt| where dtau/dt = omega_tau
tau_range = 0.5  # full transit from tau=0 to tau=0.5  # (local)
tau_Q = tau_range / omega_tau  # = 0.5/8.27 = 0.0605 M_KK^{-1}

# Microscopic relaxation time: 1/Delta
tau_0 = 1.0 / Delta_0_OES   # = 1/0.464 = 2.155 M_KK^{-1}
tau_0_GL = 1.0 / Delta_0_GL  # = 1/0.770 = 1.299 M_KK^{-1}

# Adiabaticity parameter
adiab_OES = tau_Q / tau_0
adiab_GL = tau_Q / tau_0_GL

print(f"  Transit rate: omega_tau = {omega_tau} M_KK")
print(f"  Transit duration: dt_transit = {dt_transit:.6e} M_KK^{{-1}}")
print(f"  Quench timescale: tau_Q = tau_range/omega_tau = {tau_Q:.6f} M_KK^{{-1}}")
print(f"\n  Microscopic times:")
print(f"    tau_0 (1/Delta_OES) = {tau_0:.6f} M_KK^{{-1}}")
print(f"    tau_0 (1/Delta_GL)  = {tau_0_GL:.6f} M_KK^{{-1}}")
print(f"    1/omega_PV          = {1.0/omega_PV:.6f} M_KK^{{-1}}")
print(f"\n  Adiabaticity:")
print(f"    tau_Q / tau_0 (OES) = {adiab_OES:.6f}")
print(f"    tau_Q / tau_0 (GL)  = {adiab_GL:.6f}")
print(f"\n  BOTH << 1 -> DEEPLY DIABATIC.")
print(f"  The transit is {1.0/adiab_OES:.0f}x faster than the gap relaxation time.")
print(f"  This means the system CANNOT follow the adiabatic ground state.")

# ============================================================================
# 5. FORMAL KZ LENGTH AND DEFECT DENSITY (IF KZ APPLIED)
# ============================================================================
print("\n" + "=" * 72)
print("SECTION 5: FORMAL KZ RESULTS (COUNTERFACTUAL)")
print("=" * 72)

print("\n  NOTE: These results assume KZ applies, which it does NOT because:")
print("    (a) The gap never vanishes — no critical point")
print("    (b) L/xi = 0.031 — 0D limit, no spatial defects")
print("    (c) Fragmentation at tau=0.105 is first-order, not continuous")
print("  Presented for comparison with S55 KZ-DOMAIN-55.\n")

# Formal KZ correlation length: xi_KZ = xi_0 * (tau_Q/tau_0)^{nu/(1+z*nu)}
# In diabatic regime (tau_Q < tau_0), xi_KZ < xi_0 -> saturates at xi_0
xi_KZ_mf = xi_BCS * adiab_OES**kz_xi_exp_mf
xi_KZ_ball = xi_BCS * adiab_OES**kz_xi_exp_ball
xi_KZ_mf_GL = xi_BCS * adiab_GL**kz_xi_exp_mf
xi_KZ_ball_GL = xi_BCS * adiab_GL**kz_xi_exp_ball

# Physical: floor at xi_0 (cannot be smaller than coherence length)
xi_KZ_mf_phys = max(xi_BCS, xi_KZ_mf)
xi_KZ_ball_phys = max(xi_BCS, xi_KZ_ball)

print(f"  Formal xi_KZ (z=2, tau_0=1/Delta_OES): {xi_KZ_mf:.6f} M_KK^{{-1}}")
print(f"  Formal xi_KZ (z=1, tau_0=1/Delta_OES): {xi_KZ_ball:.6f} M_KK^{{-1}}")
print(f"  Physical xi_KZ (floored at xi_BCS): {xi_KZ_mf_phys:.6f} M_KK^{{-1}}")
print(f"  Physical xi_KZ (floored at xi_BCS): {xi_KZ_ball_phys:.6f} M_KK^{{-1}}")

print(f"\n  Comparison to system sizes:")
print(f"    xi_KZ_phys / L_sys (single cell) = {xi_KZ_mf_phys / L_sys:.1f}")
print(f"    -> xi_KZ >> L_cell: entire cell is ONE DOMAIN. No intra-cell defects.")

# Graph diameter in M_KK^{-1} units
# Use bandwidth to estimate lattice spacing: a ~ 1/W
bw_fold_idx = np.argmin(np.abs(tau_tb - tau_fold))
bw_fold = bandwidths[bw_fold_idx]
a_graph = 1.0 / bw_fold  # lattice spacing (M_KK^{-1})
L_graph_phys = diameter * a_graph

print(f"\n  Graph lattice spacing: a = 1/W_fold = 1/{bw_fold:.4f} = {a_graph:.6f} M_KK^{{-1}}")
print(f"  Graph diameter: {diameter} hops = {L_graph_phys:.4f} M_KK^{{-1}}")
print(f"  xi_KZ_phys / L_graph = {xi_KZ_mf_phys / L_graph_phys:.4f}")

if xi_KZ_mf_phys > L_graph_phys:
    print(f"  -> xi_KZ > L_graph: entire fabric is ONE DOMAIN even in formal KZ.")
    N_domains = 1
else:
    N_domains = (L_graph_phys / xi_KZ_mf_phys)**d_s
    print(f"  -> N_domains = (L_graph/xi_KZ)^d_s = {N_domains:.1f}")

# Formal defect density
# n_def ~ (tau_Q/tau_0)^{-d_s*nu/(1+z*nu)}
n_def_formal_2d = adiab_OES**(-kz_def_exp_2d)
print(f"\n  Formal n_defect (d_s=2, z=2): ~ tau_Q^{{-0.5}} = {n_def_formal_2d:.4f}")
print(f"  (per unit area in lattice units)")

# ============================================================================
# 6. THE ACTUAL PHYSICS: FRAGMENTATION + SUDDEN QUENCH
# ============================================================================
print("\n" + "=" * 72)
print("SECTION 6: ACTUAL PHYSICS — FRAGMENTATION + SUDDEN QUENCH")
print("=" * 72)

# From W3-2 (PERCOLATION-CC-57):
# C2 bonds fragment at tau = 0.105 (all-or-nothing, first-order)
# Fold at tau = 0.19 is deep in fragmentation window [0.105, 0.478]
# All 32 cells are ISOLATED at the fold

tau_frag = 0.105  # C2 fragmentation (from W3-2)  # (local)
tau_BCS = 0.22    # BCS freeze  # (local)
tau_recon = 0.487  # su2 reconnection (inaccessible)  # (local)

print(f"\n  Percolation structure (W3-2):")
print(f"    C2 fragmentation:  tau = {tau_frag}")
print(f"    Fold:              tau = {tau_fold}")
print(f"    BCS freeze:        tau = {tau_BCS}")
print(f"    su2 reconnection:  tau = {tau_recon} (INACCESSIBLE)")
print(f"\n  At the fold: ALL 32 cells are isolated.")
print(f"  The fabric IS 32 independent 0D systems.")

# From W2-2 (DESERT-DYNAMICS-57):
# Phase correlation cos(phi) = 0.935 FROZEN throughout transit
# Transit speed: Mach 2700 relative to Josephson sound speed
Mach = omega_tau * a_graph / J_C2  # rough Mach number
print(f"\n  Desert dynamics (W2-2):")
print(f"    <cos(phi_1-phi_2)> = 0.935 (frozen)")
print(f"    Transit speed / Josephson speed: {omega_tau / J_C2:.0f}")
print(f"    Phase correlations FROZEN at initial values")

# From W1-1 (FINITE-RATE-TRANSIT-57):
# P_exc = 0.081 at end of transit (2-cell), 6.7e-4 at fold
# This is the SUDDEN-QUENCH CEILING: tau_Q << tau_0
P_exc_fold = 6.7e-4     # from W1-1  # (local)
P_exc_final = 0.081     # from W1-1 (2-cell; per-cell)  # (local)
P_exc_sudden = P_exc_kz  # 1.0 (single-cell S38 result)

print(f"\n  Excitation probabilities (W1-1):")
print(f"    P_exc at fold (2-cell):   {P_exc_fold:.4e}")
print(f"    P_exc at tau=0.5 (2-cell): {P_exc_final:.4f}")
print(f"    P_exc sudden (1-cell S38): {P_exc_sudden}")

# ============================================================================
# 7. THE THREE REASONS KZ FAILS ON THIS SYSTEM
# ============================================================================
print("\n" + "=" * 72)
print("SECTION 7: WHY KZ IS STRUCTURALLY INAPPLICABLE")
print("=" * 72)

# Reason 1: No critical point
print(f"\n  REASON 1: NO CRITICAL POINT")
print(f"  KZ requires passage through a second-order phase transition where")
print(f"  the order parameter vanishes (Delta -> 0). Here:")
print(f"    Delta_MB(tau=0)    = {Delta_MB[0]:.6f} M_KK")
print(f"    Delta_MB(fold)     = {Delta_MB[fold_idx]:.6f} M_KK")
print(f"    Delta_MB(tau=0.5)  = {Delta_MB[-1]:.6f} M_KK")
print(f"    min(Delta_MB)      = {np.min(Delta_MB):.6f} M_KK")
print(f"  The gap is ALWAYS open. BCS is a 1D theorem: any g>0 pairs.")
print(f"  No symmetry breaking -> no critical point -> no KZ.")

# Reason 2: Zero spatial dimension per cell
print(f"\n  REASON 2: ZERO-DIMENSIONAL CELLS")
print(f"  L/xi = {L_over_xi}. KZ defect density ~ tau_Q^{{-d*nu/(1+z*nu)}}.")
print(f"  For d=0: n_defect = tau_Q^0 = 1 (trivial).")
print(f"  No spatial extent -> no domain walls, no vortices, no topological defects.")

# Reason 3: First-order fragmentation, not continuous transition
print(f"\n  REASON 3: FIRST-ORDER FRAGMENTATION, NOT CONTINUOUS TRANSITION")
print(f"  At tau = {tau_frag}, ALL C2 bonds break simultaneously.")
print(f"  This is a first-order percolation transition (W3-2).")
print(f"  KZ applies to continuous (second-order) phase transitions with")
print(f"  diverging correlation length. First-order transitions have FINITE")
print(f"  correlation lengths and nucleation dynamics, not KZ scaling.")

# ============================================================================
# 8. WHAT ACTUALLY HAPPENS: DEFECT CLASSIFICATION
# ============================================================================
print("\n" + "=" * 72)
print("SECTION 8: ACTUAL DEFECT STRUCTURE")
print("=" * 72)

# The "defects" are not KZ defects. They are:
# 1. Bogoliubov quasiparticles from the sudden quench (S38: 59.8 pairs)
# 2. Phase mismatches between cells frozen by Mach 2700 transit
# 3. Occupation number differences between cells (GGE relic)

print(f"\n  The physical defects are NOT topological (no vortices, no domain walls).")
print(f"  They are OCCUPATION-NUMBER DEFECTS in the GGE:")
print(f"\n  1. BOGOLIUBOV QUASIPARTICLES (sudden quench, S38):")
print(f"     n_qp = {59.8} pairs (from 8-mode Fock space, single cell)")
print(f"     P_exc = {P_exc_sudden} (complete excitation in sudden limit)")
print(f"     These are NOT KZ defects; they are sudden-quench excitations.")
print(f"\n  2. FROZEN PHASE MISMATCHES (Mach 2700 transit, W2-2):")
print(f"     <cos(phi_1-phi_2)> = 0.935 (initial ground state value)")
print(f"     Phase is frozen, not randomized. No disorder generation.")
print(f"\n  3. GGE RELIC (integrability-protected, S38):")
print(f"     8 Richardson-Gaudin conserved quantities per cell")
print(f"     -> 8*32 = 256 conserved quantities total on the fabric")
print(f"     The post-transit state is a GGE, not thermal.")
print(f"     KZ assumes thermalization; this system NEVER thermalizes.")

# ============================================================================
# 9. QUANTITATIVE COMPARISON: KZ vs ACTUAL
# ============================================================================
print("\n" + "=" * 72)
print("SECTION 9: QUANTITATIVE KZ vs ACTUAL COMPARISON")
print("=" * 72)

# If we FORCE KZ on the 2D fabric (ignoring all three objections):
# xi_KZ = xi_BCS * (tau_Q/tau_0)^{1/4} for z=2
# n_defect ~ (tau_Q/tau_0)^{-1/2}

print(f"\n  COUNTERFACTUAL: If KZ applied to d_s=2 fabric (z=2, nu=1/2):")
print(f"    tau_Q / tau_0 = {adiab_OES:.6f}")
print(f"    xi_KZ = xi_BCS * ({adiab_OES:.4f})^0.25 = {xi_KZ_mf:.6f} M_KK^{{-1}}")
print(f"    n_defect ~ ({adiab_OES:.4f})^{{-0.5}} = {n_def_formal_2d:.2f} per lattice area")
print(f"    N_defects_total = n_defect * N_cells = {n_def_formal_2d * N_cells:.0f}")

# ACTUAL: no KZ defects. P_exc from overlap.
print(f"\n  ACTUAL: No KZ mechanism. Defects from sudden quench:")
print(f"    P_exc (single cell, S38) = {P_exc_sudden}")
print(f"    P_exc (2-cell, W1-1)     = {P_exc_final}")
print(f"    P_exc (N=32 estimate)    = dominated by gap scaling Delta_N ~ N^{{-1.84}}")

# From W1-3: Delta_32 ~ 0.025-0.085 M_KK
# P_exc for sudden quench: 1 - |<GS(0)|GS(final)>|^2
# For weak coupling: P_exc ~ (Delta_0/omega_tau)^2 * N_modes
# But this is already computed by W1-1 at finite rate
Delta_32_A = 0.025  # Model A from W1-3  # (local)
Delta_32_B = 0.085  # Model B from W1-3  # (local)
P_exc_A_est = 1.0 - np.exp(-2 * np.pi * Delta_32_A**2 / (4 * omega_tau))
P_exc_B_est = 1.0 - np.exp(-2 * np.pi * Delta_32_B**2 / (4 * omega_tau))

print(f"\n  Estimated P_exc from gap scaling (LZ formula):")
print(f"    Delta_32 (Model A) = {Delta_32_A} M_KK")
print(f"    Delta_32 (Model B) = {Delta_32_B} M_KK")
print(f"    P_exc_LZ (A) ~ 1 - exp(-pi*Delta^2/(2*omega)) = {P_exc_A_est:.6f}")
print(f"    P_exc_LZ (B) ~ 1 - exp(-pi*Delta^2/(2*omega)) = {P_exc_B_est:.6f}")

# ============================================================================
# 10. MSS BOUND CHECK ON DEFECT DYNAMICS
# ============================================================================
print("\n" + "=" * 72)
print("SECTION 10: MSS BOUND ON DEFECT FORMATION RATE")
print("=" * 72)

# The Maldacena-Shenker-Stanford bound: lambda_L <= 2*pi*T/hbar
# Using T_acoustic as the effective temperature
T_eff = T_acoustic  # 0.112 M_KK
lambda_L_max = 2 * np.pi * T_eff  # MSS bound
lambda_L_actual = 0.0  # From S38 CHAOS-2: no Lyapunov regime  # (local)

print(f"  MSS bound at T_acoustic = {T_eff:.4f} M_KK:")
print(f"    lambda_L_max = 2*pi*T = {lambda_L_max:.4f} M_KK")
print(f"    lambda_L_actual (S38) = {lambda_L_actual} (no exponential OTOC growth)")
print(f"    lambda_L / lambda_L_max = {lambda_L_actual / lambda_L_max:.4f}")
print(f"  The system is maximally NON-chaotic (lambda_L = 0).")
print(f"  Defect production is NOT driven by scrambling.")
print(f"  Defect production is driven by SUDDEN QUENCH (unitary, non-thermal).")

# Scrambling time for comparison
if lambda_L_actual > 0:
    t_scr = (1.0 / lambda_L_actual) * np.log(N_dof_BCS)
else:
    t_scr = np.inf
t_transit = dt_transit

print(f"\n  Scrambling time: t_scr = {'infinity' if t_scr == np.inf else f'{t_scr:.2f}'} M_KK^{{-1}}")
print(f"  Transit time:    t_transit = {t_transit:.6e} M_KK^{{-1}}")
print(f"  Ratio t_scr/t_transit = {'infinity' if t_scr == np.inf else f'{t_scr/t_transit:.0f}'}")
print(f"  The system cannot scramble during transit. Defects are non-thermal.")

# ============================================================================
# 11. SUMMARY TABLE
# ============================================================================
print("\n" + "=" * 72)
print("SUMMARY: FABRIC-KZ-QUENCH-57")
print("=" * 72)

print(f"""
  Gate: FABRIC-KZ-QUENCH-57 = INFO

  STANDARD KZ IS STRUCTURALLY INAPPLICABLE because:
    1. No critical point (Delta never vanishes, min = {np.min(Delta_MB):.4f} M_KK)
    2. d = 0 per cell (L/xi = {L_over_xi}, 32x smaller than coherence length)
    3. First-order fragmentation at tau = {tau_frag} (not continuous)
    4. lambda_L = 0 (no chaos, no scrambling, no thermalization)

  If forced (counterfactual, d_s=2 fabric):
    xi_KZ = {xi_KZ_mf:.4f} M_KK^{{-1}} (< xi_BCS, saturates at floor)
    n_defect ~ {n_def_formal_2d:.2f} per lattice area (diabatic, meaningless)

  Actual defect mechanism: SUDDEN QUENCH (non-KZ)
    P_exc = {P_exc_final} (2-cell, W1-1)
    Defects = Bogoliubov quasiparticle pairs (non-thermal GGE relic)
    Phase correlations frozen at 0.935 (Mach 2700 transit, W2-2)
    8 conserved quantities per cell -> no thermalization

  KEY NUMBER: n_KZ_defect = 0 (KZ inapplicable)
  Actual excitation: P_exc = 0.081 (sudden quench, non-KZ, W1-1)
""")

# ============================================================================
# 12. SAVE RESULTS
# ============================================================================
out_path = os.path.join(data_dir, 's57_fabric_kz_quench.npz')

np.savez(out_path,
    # BCS gap profile
    tau_ed=tau_ed,
    Delta_MB=Delta_MB,
    E_cond_A=E_cond_A,
    E_cond_B=E_cond_B,

    # KZ parameters
    z_mf=z_mf,
    nu_mf=nu_mf,
    d_s=d_s,
    kz_xi_exp_mf=kz_xi_exp_mf,
    kz_def_exp_2d=kz_def_exp_2d,

    # Quench parameters
    tau_Q=tau_Q,
    tau_0_OES=tau_0,
    tau_0_GL=tau_0_GL,
    adiab_OES=adiab_OES,
    adiab_GL=adiab_GL,

    # KZ lengths (formal, counterfactual)
    xi_KZ_mf=xi_KZ_mf,
    xi_KZ_ball=xi_KZ_ball,
    xi_KZ_mf_phys=xi_KZ_mf_phys,
    n_def_formal_2d=n_def_formal_2d,

    # System sizes
    L_sys=L_sys,
    L_graph_phys=L_graph_phys,
    a_graph=a_graph,
    diameter=diameter,

    # MSS bound
    lambda_L_max=lambda_L_max,
    lambda_L_actual=lambda_L_actual,

    # Key results
    gap_vanishes=gap_zero,
    N_domains=N_domains,
    tau_frag=tau_frag,
    P_exc_fold=P_exc_fold,
    P_exc_final=P_exc_final,

    # Gate
    gate_name=np.array(['FABRIC-KZ-QUENCH-57']),
    gate_verdict=np.array(['INFO']),
    gate_detail=np.array([
        f'KZ inapplicable: no critical point (min Delta_MB={np.min(Delta_MB):.4f}), '
        f'd=0 per cell (L/xi={L_over_xi}), first-order fragmentation. '
        f'Actual: sudden quench P_exc=0.081 (non-KZ, non-thermal GGE relic).'
    ]),
)

print(f"  Data saved to: {out_path}")
print("DONE")
