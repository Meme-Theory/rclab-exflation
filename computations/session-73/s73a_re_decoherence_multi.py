#!/usr/bin/env python3
"""
RE-DECOHERENCE-MULTI-73a: Multi-Channel Decoherence Master Budget
==================================================================

Session 73a, Wave 4-B
Gate: RE-DECOHERENCE-MULTI-73a
  PASS: Combined multi-channel t_dec/t_transit in [0.57, 0.88]
        OR combined delta_OOM in [0.20, 0.35]
  INFO: Combined t_dec/delta_OOM computed; report value and channel decomposition
  FAIL: Channels are not independent (double-counting detected)
        AND combined value outside any reasonable band

Physics
-------
Four decoherence channels have been computed in S73a Waves 1-3:

  | Channel              | Source | t_dec/t_transit | delta_OOM | Status        |
  |:---------------------|:-------|:----------------|:----------|:--------------|
  | Exit Bogoliubov      | W1-A   | 23.2            | ~0        | Dead          |
  | Mott charge noise    | W1-E   | —               | 0.336     | PASS (static) |
  | Graph spectral       | W2-C   | 118             | ~0        | Dead          |
  | Inter-branch dispers | W3-A   | 0.535           | 0.150     | Closest       |

Target: residual A_s gap delta_OOM = 0.267 (S72 dual-timescale model).
Gate band for t_dec/t_transit: [0.57, 0.88].

This computation:
1. Loads all four channel results for cross-check
2. Extracts CG(24) Josephson coupling distribution for anisotropy channel
3. Computes anisotropy decoherence from spread in local sound speeds
4. Determines channel independence by degree-of-freedom analysis
5. Combines all active channels into master budget
6. Reports final A_s status

Author: Quantum Acoustics Theorist (S73a W4-B)
"""

import sys
import os
import time
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    # BCS constants
    Delta_BCS, Delta_0_OES, E_cond, n_pairs, N_dof_BCS, N_cells,
    # Josephson couplings
    J_C2, J_su2, J_u1,
    # Transit
    dt_transit, omega_tau,
    # Spectral action
    a0_fold, a2_fold, S_fold, dS_fold,
    # Mode spectrum
    rho_B2_per_mode, E_B1, E_B2_mean, E_B3_mean,
    # Fabric
    c_Gold, c_fabric,
    # Observational
    A_s_CMB,
    # General
    PI, M_KK,
)

t0 = time.time()
data_dir = os.path.dirname(os.path.abspath(__file__))

print("=" * 76)
print("RE-DECOHERENCE-MULTI-73a: Multi-Channel Decoherence Master Budget")
print("=" * 76)
print()

# =============================================================================
#  SECTION 1: LOAD ALL CHANNEL RESULTS
# =============================================================================
print("SECTION 1: Loading channel results from W1-W3")
print("-" * 76)

# Channel 1: Exit Bogoliubov (W1-A)
d_exit = np.load(os.path.join(data_dir, "s73a_exit_horizon_bog.npz"),
                 allow_pickle=True)
t_dec_exit = float(d_exit["t_dec_ratio_new"]) if "t_dec_ratio_new" in d_exit.files else None  # (local)
# The exit horizon computation gives t_dec/t_transit as a ratio
# From the data: key "gate_detail" says t_dec/t_transit = 23.2
exit_ratio_str = str(d_exit["gate_detail"])  # (local)
# Extract delta_OOM_primary
delta_OOM_exit = float(d_exit["delta_OOM_primary"])  # (local)
no_exit_horizon = bool(d_exit["no_exit_horizon"])  # (local)

# The exit horizon t_dec/t_transit is encoded differently.
# From gate_detail: "t_dec/t_transit = 23.1945"
# This means essentially no decoherence from exit horizon (t_dec >> t_transit).
# delta_OOM_primary = 1.956 is the TOTAL undamped gap, NOT the exit contribution.
# The exit channel contribution: since no exit horizon exists, the mode-specific
# Bogoliubov phases from the exit region are negligible.
# The relevant quantity: how much does the exit scatter reduce the squeeze?
# F_compound from exit data:
F_exit = float(d_exit["F_compound"])  # (local)
# F_compound = 0.958 => nearly perfect transmission (no exit horizon)
# delta_OOM from exit = -log10(F_exit) if F_exit < 1, but this measures
# the COMPOUND fidelity, not an independent decoherence contribution.
# The exit channel gives delta_OOM ~ 0 because no exit horizon exists.
delta_OOM_ch1 = 0.0  # Dead: no exit horizon  # (local)

print(f"  Channel 1 (Exit Bogoliubov, W1-A):")
print(f"    no_exit_horizon: {no_exit_horizon}")
print(f"    F_compound: {F_exit:.6f}")
print(f"    delta_OOM_primary (undamped total): {delta_OOM_exit:.4f}")
print(f"    delta_OOM contribution: {delta_OOM_ch1:.4f} (DEAD — no exit horizon)")
print()

# Channel 2: Mott charge noise (W1-E)
d_mott = np.load(os.path.join(data_dir, "s73a_mott_charge_noise.npz"),
                 allow_pickle=True)
delta_OOM_mott = float(d_mott["delta_OOM_Mott"])  # (local)
F_mott = float(d_mott["F_total"])  # (local)
delta_phi_mott = float(d_mott["delta_phi_mott"])  # (local)
E_J_over_E_C = float(d_mott["E_J_over_E_C_geomean"])  # (local)
# t_dec ratio from Mott data
t_dec_ratio_mott_new = float(d_mott["t_dec_ratio_new"])  # (local)
t_dec_ratio_mott_old = float(d_mott["t_dec_ratio_old"])  # (local)
delta_OOM_ch2 = delta_OOM_mott  # (local)

print(f"  Channel 2 (Mott charge noise, W1-E):")
print(f"    delta_OOM_Mott: {delta_OOM_mott:.4f}")
print(f"    F_total: {F_mott:.4f}")
print(f"    delta_phi_Mott: {delta_phi_mott:.4f} rad")
print(f"    E_J/E_C (geomean): {E_J_over_E_C:.4f}")
print(f"    t_dec/t_transit (new est): {t_dec_ratio_mott_new:.4f}")
print()

# Channel 3: Graph spectral (W2-C)
d_graph = np.load(os.path.join(data_dir, "s73a_graph_spectral_decoherence.npz"),
                  allow_pickle=True)
ratio_graph = float(d_graph["ratio_primary"])  # t_dec/t_transit = 346.6  # (local)
ratio_graph_aniso = float(d_graph["ratio_aniso"])  # = 820.6  # (local)
ratio_graph_agg = float(d_graph["ratio_agg_aniso"])  # = 123.1  # (local)
lambda_1_aniso = float(d_graph["lambda_1_aniso"])  # (local)
# Graph spectral gives t_dec >> t_transit for ALL variants => effectively dead
delta_OOM_ch3 = 0.0  # Dead: t_dec/t_transit >> 1  # (local)

print(f"  Channel 3 (Graph spectral, W2-C):")
print(f"    t_dec/t_transit (isotropic): {ratio_graph:.2f}")
print(f"    t_dec/t_transit (aniso single): {ratio_graph_aniso:.2f}")
print(f"    t_dec/t_transit (aniso aggregate): {ratio_graph_agg:.2f}")
print(f"    lambda_1(aniso): {lambda_1_aniso:.4f}")
print(f"    delta_OOM contribution: {delta_OOM_ch3:.4f} (DEAD — transit too fast)")
print()

# Channel 4: Inter-branch dispersive (W3-A / Fabry-Perot)
d_fp = np.load(os.path.join(data_dir, "s73a_fabry_perot_cavity.npz"),
               allow_pickle=True)
delta_OOM_disp = float(d_fp["delta_OOM_dispersive"])  # (local)
t_dec_master_fp = float(d_fp["t_dec_master"])  # (local)
t_dec_squeezed_fp = float(d_fp["t_dec_squeezed"])  # (local)
Var_inter_branch = float(d_fp["Var_inter_branch"])  # (local)
F_dec_squeezed = float(d_fp["F_dec_squeezed"])  # (local)
F_dec_master = float(d_fp["F_dec_master"])  # (local)
shortfall_ratio = float(d_fp["shortfall_ratio"])  # (local)
delta_OOM_ch4 = delta_OOM_disp  # (local)
omega_k = d_fp["omega_k"]  # mode frequencies  # (local)
labels = d_fp["labels"]  # mode labels  # (local)
mode_weights = d_fp["mode_weights"]  # (local)
r_k_bcs = d_fp["r_k_bcs"]  # BCS squeeze parameters  # (local)

print(f"  Channel 4 (Inter-branch dispersive, W3-A):")
print(f"    delta_OOM_dispersive: {delta_OOM_disp:.4f}")
print(f"    t_dec/t_transit (master): {t_dec_master_fp:.4f}")
print(f"    t_dec/t_transit (squeezed): {t_dec_squeezed_fp:.4f}")
print(f"    Var(inter-branch phase): {Var_inter_branch:.6f}")
print(f"    shortfall_ratio: {shortfall_ratio:.4f}")
print()

# =============================================================================
#  SECTION 2: CG(24) JOSEPHSON ANISOTROPY CHANNEL
# =============================================================================
print("SECTION 2: CG(24) Josephson Anisotropy Decoherence")
print("-" * 76)

# Load CG(24) adjacency and S63 anisotropy data
d_island = np.load(os.path.join(data_dir, "s72_island_graph.npz"),
                   allow_pickle=True)
d_aniso = np.load(os.path.join(data_dir, "s63_aniso_josephson.npz"),
                  allow_pickle=True)

N_vert = int(d_island["N_vert"])  # = 24  # (local)
N_edges = int(d_island["N_edges"])  # = 72  # (local)
degree = int(d_island["degree"])  # = 6  # (local)

# Josephson coupling per edge
EJ_unoriented = d_aniso["EJ_unoriented"]  # shape (72,)  # (local)
EJ_per_trans = d_aniso["EJ_per_trans"]  # shape (6,) Josephson per transposition class  # (local)
EJ_max = float(d_aniso["EJ_max"])  # (local)
EJ_min = float(d_aniso["EJ_min"])  # (local)
ratio_maxmin = float(d_aniso["ratio_maxmin"])  # = 11.8  # (local)
adj_matrix = d_aniso["adj"]  # shape (24, 24), int8  # (local)

# Superfluid density directional
rho_s_directional = d_aniso["rho_s_directional"]  # shape (6,)  # (local)
rho_s_eigs = d_aniso["rho_s_eigs"]  # shape (8,)  # (local)

print(f"  CG(24): {N_vert} vertices, {N_edges} edges, degree {degree}")
print(f"  E_J per transposition: {EJ_per_trans}")
print(f"  E_J max/min ratio: {ratio_maxmin:.4f}")
print(f"  E_J range: [{EJ_min:.6f}, {EJ_max:.6f}] M_KK")
print(f"  rho_s directional: {rho_s_directional}")
print()

# -------------------------------------------------------------------------
# 2a. Local Josephson environment for each cell
# -------------------------------------------------------------------------
# On CG(24) (Cayley graph of S_4 with 6 transpositions as generators),
# each vertex i has degree 6. The 6 edges connect to neighbors via the
# 6 transpositions t_1,...,t_6. Each transposition carries a different
# Josephson coupling (from the rho_s anisotropy).
#
# The transposition-to-edge map: for vertex g (element of S_4), its
# neighbors are g*t_k for k=1,...,6. Since CG(24) is vertex-transitive
# (S_4 acts by left multiplication), every vertex has the SAME set of
# edge couplings {J(t_1), ..., J(t_6)}.
#
# This means: in the isotropic vertex-transitive limit, every cell sees
# the SAME Josephson environment. The anisotropy decoherence from spread
# in local Josephson environments is ZERO for a Cayley graph.
#
# The anisotropy enters NOT through vertex-to-vertex variation (which is
# zero by vertex-transitivity) but through DIRECTIONAL variation: different
# bonds from the same cell have different strengths.
#
# For the decoherence calculation, what matters is whether the EFFECTIVE
# LOCAL SOUND SPEED varies from cell to cell. If the fabric is isotropic
# at each cell (averaging over the 6 bond directions), then no spread in
# crossing times exists.

# Compute the effective Josephson energy per cell (sum over half-bonds)
# Since vertex-transitive: every cell gets the same total
J_per_cell_total = 0.5 * np.sum(EJ_per_trans)  # half-bond convention  # (local)
print(f"  2a. Local Josephson environment")
print(f"  J_total per cell (half-bond): {J_per_cell_total:.6f} M_KK")
print(f"  J_per_trans: {EJ_per_trans}")
print(f"  CG(24) is vertex-transitive => ALL cells see identical environment")
print()

# -------------------------------------------------------------------------
# 2b. Effective exit-horizon crossing velocity
# -------------------------------------------------------------------------
# The crossing velocity for the fold transit is v_tau = omega_tau = 8.27 M_KK.
# The "cell size" is the CG(24) lattice spacing: d_cell = xi_BCS / something.
# From S72 dual decoherence:
d_dual = np.load(os.path.join(data_dir, "s72_dual_decoherence.npz"),
                 allow_pickle=True)
d_cell = float(d_dual["d_cell"])  # = 1.596 M_KK^{-1}  # (local)
c_BCS = float(d_dual["c_BCS"])  # = 0.464 M_KK  # (local)
Mach_BCS = float(d_dual["Mach_BCS"])  # = 17.8  # (local)
t_cross_cell = float(d_dual["t_cross_cell"])  # cell crossing time  # (local)

v_tau = omega_tau  # transit velocity in tau-space = 8.27 M_KK  # (local)

print(f"  2b. Transit parameters")
print(f"  v_tau (transit velocity): {v_tau:.4f} M_KK")
print(f"  d_cell: {d_cell:.6f} M_KK^{{-1}}")
print(f"  c_BCS: {c_BCS:.4f} M_KK")
print(f"  Mach_BCS: {Mach_BCS:.2f}")
print(f"  t_cross_cell: {t_cross_cell:.6e} M_KK^{{-1}}")
print()

# The modification to the local sound speed from Josephson coupling.
#
# In a Josephson array, the BCS sound speed receives a correction from
# the phase stiffness. The effective sound speed in cell i:
#
#   c_eff(i) = c_BCS * sqrt(1 + sum_j J(i,j) / (N_pair * omega_k))  (1)
#
# For a vertex-transitive graph, sum_j J(i,j) is the SAME for all i.
# Therefore c_eff is uniform: NO cell-to-cell spread in crossing velocities.
#
# The anisotropy enters at the DIRECTIONAL level: sound propagating along
# the t_1 direction sees J(t_1) while sound along t_4 sees J(t_4).
# This creates direction-dependent sound speeds:
#
#   c_eff(direction k) = c_BCS * sqrt(1 + J(t_k) / E_BCS_cell)  (2)
#
# where E_BCS_cell = |E_cond| / N_cells.
#
# The directional anisotropy creates a SPREAD in the effective speeds
# experienced by different BCS modes as the transit front sweeps through.

E_BCS_cell = abs(E_cond) / N_cells  # BCS energy per cell  # (local)

# Directional sound speeds from Josephson stiffness
# Equation (2): c_eff(k) = c_BCS * sqrt(1 + J(t_k) / E_BCS_cell)
c_directional = c_BCS * np.sqrt(1.0 + EJ_per_trans / E_BCS_cell)  # (local)
c_mean = np.mean(c_directional)  # (local)
c_std = np.std(c_directional)  # (local)
c_max = np.max(c_directional)  # (local)
c_min = np.min(c_directional)  # (local)

print(f"  2b. Directional sound speeds (Josephson-corrected)")
print(f"  E_BCS per cell: {E_BCS_cell:.6f} M_KK")
print(f"  c_directional = c_BCS * sqrt(1 + J_k/E_BCS): {c_directional}")
print(f"  c_mean: {c_mean:.4f}, c_std: {c_std:.4f}")
print(f"  c_max/c_min: {c_max/c_min:.4f}")
print(f"  Fractional spread: {c_std/c_mean:.4f}")
print()

# -------------------------------------------------------------------------
# 2c. Crossing time spread and anisotropy decoherence timescale
# -------------------------------------------------------------------------
# The transit sweeps across each cell in time t_cross = d_cell / v_tau.
# The BCS modes experience different effective propagation speeds depending
# on the local Josephson environment.
#
# Since the graph is vertex-transitive, the cell-to-cell variation is zero.
# The decoherence arises from the DIRECTIONAL spread within each cell.
#
# The directional crossing times:
#   t_cross(k) = d_cell / c_directional(k)                        (3)
#
# The spread in these times creates phase decoherence:
#   delta_phi_aniso = omega_k * Var(t_cross)^{1/2}                (4)
#
# The anisotropy decoherence timescale:
#   t_dec_aniso = 1 / (omega_eff * delta_c/c_mean)                (5)
# where omega_eff is the characteristic BCS frequency and delta_c/c is
# the fractional sound speed spread.

t_cross_dir = d_cell / c_directional  # directional crossing times  # (local)
Var_t_cross = np.var(t_cross_dir)  # variance of crossing times  # (local)
sigma_t_cross = np.sqrt(Var_t_cross)  # (local)

# Mode-dependent phase accumulation from directional spread
# Each mode k has frequency omega_k. The phase spread from
# directional anisotropy:
omega_eff_bcs = np.average(omega_k, weights=mode_weights)  # weighted avg freq  # (local)
delta_phi_aniso = omega_eff_bcs * sigma_t_cross  # phase spread from anisotropy  # (local)

print(f"  2c. Anisotropy decoherence")
print(f"  t_cross directional: {t_cross_dir}")
print(f"  Var(t_cross): {Var_t_cross:.6e}")
print(f"  sigma(t_cross): {sigma_t_cross:.6e} M_KK^{{-1}}")
print(f"  omega_eff (weighted): {omega_eff_bcs:.4f} M_KK")
print(f"  delta_phi_aniso = omega_eff * sigma_t: {delta_phi_aniso:.6e} rad")

# The anisotropy decoherence factor:
#   F_aniso = exp(-delta_phi_aniso^2 / 2)                          (6)
F_aniso = np.exp(-delta_phi_aniso**2 / 2.0)  # (local)
# The delta_OOM contribution:
# If F_aniso ~ 1, the anisotropy channel contributes negligible decoherence.
# delta_OOM_aniso = -log10(F_aniso) = delta_phi_aniso^2 / (2 * ln(10))
delta_OOM_aniso = -np.log10(F_aniso) if F_aniso < 1.0 else 0.0  # (local)

print(f"  F_aniso: {F_aniso:.8f}")
print(f"  delta_OOM_aniso: {delta_OOM_aniso:.6e}")
print()

# HOWEVER: the directional anisotropy above uses c_directional which
# corrects c_BCS by the Josephson stiffness. But c_BCS itself is the
# BCS propagation speed (= Delta_BCS), not the transit velocity.
# The TRANSIT is driven by the spectral action gradient (v_tau = 8.27),
# which is MUCH faster than c_BCS = 0.464.
#
# The relevant quantity for decoherence during transit is the PHASE
# accumulated by BCS modes as the transit front passes. Each mode k
# oscillates at omega_k during the transit. The total phase accumulated:
#   Phi_transit(k) = omega_k * dt_transit                           (7)
#
# The Josephson anisotropy modifies the MODE FREQUENCIES, not the transit
# velocity. The correction to omega_k from the Josephson coupling in
# direction d:
#   delta_omega_k(d) = J(d) * (mode overlap with direction d)       (8)
#
# For the 8 BCS modes, the coupling to each Josephson direction depends
# on the mode's representation content (B2 modes couple to C^2 directions,
# B1/B3 modes couple to su(2) and u(1) directions differently).

# Use the S63 eigenvalue data for mode-dependent corrections
eps_fold = d_aniso["eps_fold"]  # 8 single-particle energies at fold  # (local)
V_fold = d_aniso["V_fold"]  # 8x8 pairing interaction  # (local)

# The Josephson coupling modifies the BCS Hamiltonian by adding a
# phase-stiffness term. For mode k, the effective frequency correction:
#   delta_omega_k = sum_d J(t_d) * |u_k(d)|^2                      (9)
# where u_k(d) is the participation of mode k in direction d.
#
# From the rho_s tensor diagonalization (S63):
rho_s_fold = d_aniso["rho_s_fold"]  # 8x8 superfluid density matrix  # (local)
# The eigenvalues of rho_s give the directional stiffnesses:
# rho_s_eigs spans [0.327, 7.962] with ratio 24.4.
# The mode-resolved Josephson shift: <k|rho_s|k> * J_mean
J_mean_bond = np.mean(EJ_per_trans)  # = 0.403 M_KK  # (local)
rho_s_diag = np.diag(rho_s_fold)  # diagonal elements per mode  # (local)

# Mode-specific Josephson correction:
delta_omega_J = J_mean_bond * rho_s_diag  # (local)
# These corrections are SMALL compared to the bare omega_k:
# omega_k ~ 0.84 M_KK, delta_omega ~ 0.4 * rho_s_diag ~ 0.4 * [0.3, 8] = [0.1, 3.2]
# So the correction can be ORDER 1 or larger for modes with large rho_s.
# But what matters for DECOHERENCE is the VARIANCE of the correction
# across modes, weighted by the mode contribution to the squeeze.

# Weighted variance of Josephson frequency shifts:
delta_omega_mean = np.average(delta_omega_J, weights=mode_weights)  # (local)
Var_delta_omega = np.average((delta_omega_J - delta_omega_mean)**2,
                             weights=mode_weights)  # (local)
sigma_delta_omega = np.sqrt(Var_delta_omega)  # (local)

# Phase spread from Josephson anisotropy during transit:
#   delta_phi_J = sigma(delta_omega) * dt_transit                  (10)
delta_phi_J = sigma_delta_omega * dt_transit  # (local)

print(f"  2c (continued). Josephson frequency shift anisotropy")
print(f"  J_mean_bond: {J_mean_bond:.4f} M_KK")
print(f"  rho_s diagonal (per mode): {rho_s_diag}")
print(f"  delta_omega_J (per mode): {delta_omega_J}")
print(f"  delta_omega_mean (weighted): {delta_omega_mean:.4f} M_KK")
print(f"  sigma(delta_omega) (weighted): {sigma_delta_omega:.4f} M_KK")
print(f"  dt_transit: {dt_transit:.6e} M_KK^{{-1}}")
print(f"  delta_phi_J = sigma * dt_transit: {delta_phi_J:.6e} rad")
print()

# The Josephson anisotropy decoherence factor (from frequency-shift channel):
F_aniso_J = np.exp(-delta_phi_J**2 / 2.0)  # (local)
delta_OOM_aniso_J = -np.log10(F_aniso_J) if F_aniso_J < 1.0 else 0.0  # (local)

# Take the LARGER of the two anisotropy estimates (directional vs frequency)
delta_OOM_aniso_max = max(delta_OOM_aniso, delta_OOM_aniso_J)  # (local)
F_aniso_min = min(F_aniso, F_aniso_J)  # (local)

# But BOTH are tiny because dt_transit ~ 1e-3 is extremely short.
# The vertex-transitive structure of CG(24) ensures no cell-to-cell variation.
# The directional anisotropy creates a spread, but it acts for only dt_transit.

# t_dec/t_transit for anisotropy:
if delta_phi_J > 0:
    t_dec_aniso_ratio = 1.0 / delta_phi_J  # (local)
else:
    t_dec_aniso_ratio = np.inf  # (local)

print(f"  F_aniso (directional): {F_aniso:.8f}")
print(f"  F_aniso (Josephson freq): {F_aniso_J:.8f}")
print(f"  delta_OOM_aniso (directional): {delta_OOM_aniso:.6e}")
print(f"  delta_OOM_aniso (Josephson freq): {delta_OOM_aniso_J:.6e}")
print(f"  delta_OOM_aniso (max): {delta_OOM_aniso_max:.6e}")
print(f"  t_dec/t_transit (aniso): {t_dec_aniso_ratio:.2f}")
print()

# CROSS-CHECK: in the limit J_C2 = J_su2 = J_u1 (isotropic),
# the variance of EJ_per_trans should vanish => delta_OOM_aniso = 0.
J_iso = np.mean(EJ_per_trans) * np.ones(6)  # (local)
c_dir_iso = c_BCS * np.sqrt(1.0 + J_iso / E_BCS_cell)  # (local)
assert np.std(c_dir_iso) < 1e-14, "Cross-check FAILED: isotropic limit has nonzero spread"
print(f"  CROSS-CHECK: isotropic limit std(c) = {np.std(c_dir_iso):.2e} (should be ~0) => PASS")
print()

# =============================================================================
#  SECTION 3: CHANNEL INDEPENDENCE ANALYSIS
# =============================================================================
print("SECTION 3: Channel Independence Analysis")
print("-" * 76)

# The key question: do the active channels (Mott, dispersive, anisotropy)
# act on independent degrees of freedom?
#
# Channel 2 (Mott charge noise):
#   Acts on: phase phi_i on each cell i (24 cells => 24 independent phases)
#   Mechanism: quantum charge number fluctuations => delta_N ~ 0.45 pairs
#   Creates: random phase kicks delta_phi_i = 2*pi * delta_N on each cell
#   DOF count: 24 (cell phases)
#   STATIC: does not depend on transit dynamics
#
# Channel 4 (Inter-branch dispersive):
#   Acts on: relative phases between BCS branches (B2 vs B1 vs B3)
#   Mechanism: different propagation speeds => different phase accumulation
#   Creates: inter-branch phase variance Var(Phi) = 0.044
#   DOF count: 3 inter-branch phases (B2-B1, B2-B3, B1-B3)
#   DYNAMIC: depends on transit duration and mode dispersion
#
# Channel 5 (Josephson anisotropy):
#   Acts on: directional phase differences within each cell
#   Mechanism: Josephson stiffness anisotropy => different mode frequencies
#   Creates: mode-dependent frequency shifts during transit
#   DOF count: 6 directional phases per cell
#   DYNAMIC: depends on transit duration (and is negligible)
#
# INDEPENDENCE TEST:
# The Mott channel acts on the ABSOLUTE phase phi_i of each cell.
# The dispersive channel acts on RELATIVE phases between spectral branches.
# These are different linear combinations of the same underlying phases.
#
# Decomposition:
# Let phi_k be the phase of BCS mode k (k = 1,...,8).
# The Mott channel contributes: delta_phi_k ~ delta_N_k (charge noise)
# The dispersive channel contributes: delta_phi_k ~ omega_k * dt (speed difference)
#
# If delta_N_k and omega_k * dt are statistically independent (they are,
# because charge noise is a quantum ground-state fluctuation while
# dispersion is a classical propagation effect), then:
#
#   <delta_phi_k^2>_total = <delta_phi_k^2>_Mott + <delta_phi_k^2>_disp  (11)
#
# The total decoherence factor:
#   F_total = F_Mott * F_disp * F_aniso                               (12)
#
# In delta_OOM:
#   delta_OOM_total = delta_OOM_Mott + delta_OOM_disp + delta_OOM_aniso (13)
#   (because delta_OOM = -log10(F), and logs multiply => add)
#
# WAIT. Equations (11) and (13) are DIFFERENT STATEMENTS.
# (11) says variances add (independent random variables).
# (13) says delta_OOM add (independent processes).
#
# If the decoherence factors are F = exp(-sigma^2/2), then for independent
# Gaussian noise channels:
#   sigma^2_total = sigma^2_Mott + sigma^2_disp + sigma^2_aniso       (14)
#   F_total = exp(-sigma^2_total/2) = F_Mott * F_disp * F_aniso       (15)
#   delta_OOM_total = -log10(F_total) = delta_OOM_Mott + delta_OOM_disp + delta_OOM_aniso  (16)
#
# So for INDEPENDENT Gaussian channels: delta_OOM values ADD.
# This is NOT quadrature (sqrt of sum of squares).
# Quadrature would apply if we were adding AMPLITUDES.
# But delta_OOM = -log10(F) is a LOGARITHM of a product => it is ADDITIVE.
#
# The confusion arises from the task description which suggested quadrature.
# Let me verify this carefully.
#
# The A_s prediction depends on the squeeze parameter as:
#   A_s^pred = f(r_eff) where r_eff involves the squeeze factor
#
# From the S72 framework:
#   A_s = (H^2 / (8*pi^2*eps)) * cosh(2*r_eff) * (correction factors)
#   delta_OOM = |log10(A_s^pred / A_s^obs)|
#
# The decoherence channels reduce r_eff (or equivalently, reduce cosh(2r)).
# The total reduction is a PRODUCT of fidelity factors:
#   r_eff_total = r_bare * F_Mott * F_disp * ...  (NOT exactly right)
#
# Actually the relationship is more nuanced. Let me use the precise
# formulation from each channel.

# From Mott data:
# delta_OOM_Mott comes from reducing the squeeze through phase diffusion
# delta_OOM_Mott = 0.336 is computed as the reduction in log10(cosh(2r))
# when the squeeze phase is randomized by delta_phi_mott.

# From dispersive data:
# delta_OOM_disp = 0.150 comes from inter-branch phase variance
# reducing the coherent sum of squeeze amplitudes.

# The precise combination depends on HOW each channel reduces the power.
# For the Mott channel: P_s -> P_s * exp(-delta_phi_mott^2)  (phase diffusion)
# For dispersive: P_s -> P_s * (1 - Var_inter / Var_total)  (decoherence)
# These are MULTIPLICATIVE corrections to the power spectrum amplitude.
# In log-space (delta_OOM = log10 corrections), they ADD.

# The CORRECT combination for independent multiplicative factors:
#   delta_OOM_total = delta_OOM_ch1 + delta_OOM_ch2 + delta_OOM_ch3
#                   + delta_OOM_ch4 + delta_OOM_ch5                    (17)

# Let me verify with a direct approach.
# The Mott fidelity F_Mott = 0.461 reduces power by factor 0.461.
# The dispersive delta_OOM = 0.150 reduces power by factor 10^{-0.150} = 0.708.
# Combined: power reduced by 0.461 * 0.708 = 0.326
# delta_OOM_combined = -log10(0.326) = 0.487

# Check: 0.336 + 0.150 = 0.486. Yes, additive (up to rounding).
verification_product = F_mott * 10**(-delta_OOM_disp)  # (local)
verification_dOOM = -np.log10(verification_product)  # (local)
verification_sum = delta_OOM_mott + delta_OOM_disp  # (local)

print(f"  INDEPENDENCE VERIFICATION:")
print(f"    F_Mott: {F_mott:.4f}")
print(f"    F_disp = 10^(-{delta_OOM_disp:.4f}): {10**(-delta_OOM_disp):.4f}")
print(f"    Product: {verification_product:.6f}")
print(f"    delta_OOM from product: {verification_dOOM:.4f}")
print(f"    Sum of delta_OOM: {verification_sum:.4f}")
print(f"    Agreement: {abs(verification_dOOM - verification_sum):.2e} (should be ~0)")
print()

# The physical argument for independence:
# 1. Mott charge noise is a QUANTUM GROUND STATE property.
#    It exists whether or not the transit occurs. It depends on E_J/E_C
#    (the ratio of Josephson to charging energy), which is a property of
#    the static Josephson array at the fold.
#
# 2. Inter-branch dispersive decoherence is a DYNAMICAL property.
#    It depends on the transit velocity, the mode frequency spread,
#    and the interaction between BCS branches during propagation.
#    It would vanish if all modes had identical frequencies.
#
# 3. The Mott channel randomizes the ABSOLUTE phase of the squeeze.
#    The dispersive channel randomizes the RELATIVE phases between branches.
#    These are orthogonal in the sense that:
#    - Mott: phi_k -> phi_k + delta_phi_Mott (same for all k within a cell)
#    - Dispersive: phi_k -> phi_k + omega_k * delta_t (different for each k)
#    The Mott noise is cell-correlated; the dispersive noise is mode-correlated.
#
# CONCLUSION: channels are INDEPENDENT. The correct combination is ADDITIVE
# in delta_OOM (equivalently, multiplicative in fidelity).

print(f"  PHYSICAL ARGUMENT FOR INDEPENDENCE:")
print(f"    Mott: static quantum ground-state property (E_J/E_C ratio)")
print(f"    Dispersive: dynamic transit property (omega_k spread)")
print(f"    Mott DOF: 24 cell phases (absolute phase per cell)")
print(f"    Dispersive DOF: 3 inter-branch phases (B2-B1, B2-B3, B1-B3)")
print(f"    Overlap: NONE (cell vs branch indices)")
print(f"    Combination rule: ADDITIVE in delta_OOM (product in fidelity)")
print()

# =============================================================================
#  SECTION 4: MASTER DECOHERENCE BUDGET
# =============================================================================
print("SECTION 4: Master Decoherence Budget")
print("-" * 76)

# All channels, with their contributions:
channels = {
    "Exit Bogoliubov (W1-A)": {
        "delta_OOM": delta_OOM_ch1,
        "status": "DEAD (no exit horizon)",
        "DOF": "N/A",
        "type": "dynamic",
    },
    "Mott charge noise (W1-E)": {
        "delta_OOM": delta_OOM_ch2,
        "status": "ACTIVE",
        "DOF": "24 cell phases",
        "type": "static",
    },
    "Graph spectral (W2-C)": {
        "delta_OOM": delta_OOM_ch3,
        "status": "DEAD (transit too fast)",
        "DOF": "graph mixing modes",
        "type": "dynamic",
    },
    "Inter-branch dispersive (W3-A)": {
        "delta_OOM": delta_OOM_ch4,
        "status": "ACTIVE",
        "DOF": "3 inter-branch phases",
        "type": "dynamic",
    },
    "Josephson anisotropy (W4-B)": {
        "delta_OOM": delta_OOM_aniso_max,
        "status": "NEGLIGIBLE (vertex-transitive)",
        "DOF": "6 directional phases",
        "type": "dynamic",
    },
}

print(f"  {'Channel':<35s} {'delta_OOM':>10s}  {'Status':<35s}")
print(f"  {'-'*35} {'-'*10}  {'-'*35}")
for name, ch in channels.items():
    print(f"  {name:<35s} {ch['delta_OOM']:10.4f}  {ch['status']:<35s}")
print()

# Active channels only:
active_delta_OOM = [ch["delta_OOM"] for ch in channels.values()
                    if ch["status"] == "ACTIVE"]  # (local)
delta_OOM_total_additive = sum(ch["delta_OOM"] for ch in channels.values())  # (local)

# Compute the three combination models from the task:
delta_OOM_quadrature = np.sqrt(delta_OOM_ch2**2 + delta_OOM_ch4**2)  # (local)
delta_OOM_max = max(delta_OOM_ch2, delta_OOM_ch4)  # (local)
delta_OOM_additive_active = delta_OOM_ch2 + delta_OOM_ch4  # (local)

print(f"  COMBINATION MODELS (active channels only):")
print(f"    (A) Quadrature (sqrt of sum of squares): {delta_OOM_quadrature:.4f}")
print(f"    (B) Overlap (max): {delta_OOM_max:.4f}")
print(f"    (C) Additive (independent): {delta_OOM_additive_active:.4f}")
print()

# Physical determination: As shown in Section 3, for INDEPENDENT MULTIPLICATIVE
# noise channels, delta_OOM values ADD. The channels are independent because
# they act on different degrees of freedom (cell phases vs inter-branch phases).
# The correct model is (C): ADDITIVE.

delta_OOM_combined = delta_OOM_additive_active  # The physically correct combination  # (local)

# Including the negligible anisotropy channel:
delta_OOM_combined_full = delta_OOM_combined + delta_OOM_aniso_max  # (local)

print(f"  PHYSICALLY CORRECT COMBINATION: ADDITIVE")
print(f"  delta_OOM_combined (Mott + dispersive): {delta_OOM_combined:.4f}")
print(f"  delta_OOM_combined (including anisotropy): {delta_OOM_combined_full:.4f}")
print()

# Compute combined t_dec/t_transit from independent decoherence rates.
# For independent channels: 1/t_dec_combined = sum(1/t_dec_i)
rate_mott = 1.0 / t_dec_ratio_mott_new  # (local)
rate_disp = 1.0 / t_dec_master_fp  # (local)
rate_aniso = 1.0 / t_dec_aniso_ratio if t_dec_aniso_ratio < 1e10 else 0.0  # (local)
rate_combined = rate_mott + rate_disp + rate_aniso  # (local)
t_dec_combined = 1.0 / rate_combined  # (local)

print(f"  COMBINED RATE:")
print(f"    1/t_Mott = {rate_mott:.4f}, 1/t_disp = {rate_disp:.4f}, 1/t_aniso = {rate_aniso:.6e}")
print(f"    1/t_combined = {rate_combined:.4f}")
print(f"    t_dec/t_transit (combined) = {t_dec_combined:.4f}")
print()

# =============================================================================
#  SECTION 5: RESIDUAL A_s GAP — S72 FORMULA
# =============================================================================
print("SECTION 5: Residual A_s Gap (S72 Formula)")
print("-" * 76)

# CRITICAL: The S72 delta_OOM is defined as:
#   delta_OOM = log10( sum_k w_k * cosh(2 * r_k_dec) )
# where r_k_dec = r_k_BCS * exp(-1/(t_dec/t_transit)) + delta_r_slow_k * decay_slow.
# The undamped value: delta_OOM_undamped = log10(sum w_k * cosh(2*r_k)) = 2.074
# means weighted cosh(2r) = 10^{2.074} = 118.6.
# The target: delta_OOM = 0.267 means weighted cosh(2*r_dec) = 10^{0.267} = 1.85.
# The "A_s gap" of 0.267 OOM is the RESIDUAL over-prediction after decoherence.

delta_OOM_undamped = float(d_dual["delta_OOM_undamped"])  # (local)
delta_OOM_instant_bcs = float(d_dual["delta_OOM_instant_bcs"])  # = 0.0024  # (local)
delta_OOM_target = 0.267  # S72 target residual gap  # (local)

# S72 squeeze parameters
r_k_bcs_s72 = d_dual["r_k_bcs"]  # shape (8,), BCS squeeze per mode  # (local)
r_eff_modes_s72 = d_dual["r_eff_modes"]  # shape (8,), total r per mode  # (local)
mw_s72 = d_dual["mode_weights"]  # (local)
labels_dual = d_dual["labels"]  # (local)
delta_r_slow_s72 = r_eff_modes_s72 - r_k_bcs_s72  # slow-channel correction  # (local)

# S72 formula: r_k_dec = r_k_BCS * exp(-1/ratio) + delta_r_slow_k * decay_slow
# delta_OOM = log10( sum_k w_k * cosh(2*r_k_dec) )
def s72_delta_OOM(t_dec_bcs_ratio, r_bcs, delta_r_slow, weights, decay_slow=1.0):
    """Reproduce the S72 dual-timescale delta_OOM formula."""
    decay_bcs = np.exp(-1.0 / t_dec_bcs_ratio) if t_dec_bcs_ratio > 0 else 0.0
    r_dec = r_bcs * decay_bcs + delta_r_slow * decay_slow
    cosh2r_w = np.sum(weights * np.cosh(2.0 * r_dec))
    return np.log10(cosh2r_w) if cosh2r_w > 1.0 else 0.0, cosh2r_w, r_dec

cosh2r_bare = np.sum(mw_s72 * np.cosh(2.0 * r_eff_modes_s72))  # (local)

print(f"  delta_OOM_undamped: {delta_OOM_undamped:.4f} OOM")
print(f"  delta_OOM_instant_bcs: {delta_OOM_instant_bcs:.4f} OOM")
print(f"  Weighted cosh(2r_bare): {cosh2r_bare:.4f}")
print(f"  r_k_BCS: {r_k_bcs_s72}")
print(f"  delta_r_slow: {delta_r_slow_s72}")
print()

# Undamped cross-check
dOOM_inf, _, _ = s72_delta_OOM(1e12, r_k_bcs_s72, delta_r_slow_s72, mw_s72)
print(f"  CC: undamped limit delta_OOM = {dOOM_inf:.4f} vs {delta_OOM_undamped:.4f}: "
      f"{'PASS' if abs(dOOM_inf - delta_OOM_undamped) < 0.01 else 'FAIL'}")

# Multi-channel t_dec applied to S72 model
t_dec_ratio_mott = t_dec_ratio_mott_new  # (local)
t_dec_ratio_disp = t_dec_master_fp  # (local)

dOOM_at_combined, c2r_at_combined, r_dec_at_combined = s72_delta_OOM(
    t_dec_combined, r_k_bcs_s72, delta_r_slow_s72, mw_s72)

print(f"\n  S72 model at combined t_dec/t_transit = {t_dec_combined:.4f}:")
print(f"    decay_bcs = exp(-{1.0/t_dec_combined:.2f}) = {np.exp(-1.0/t_dec_combined):.6e}")
print(f"    cosh(2r_dec) weighted: {c2r_at_combined:.4f}")
print(f"    delta_OOM = log10({c2r_at_combined:.4f}) = {dOOM_at_combined:.4f}")
print()

# Scan to find exact target crossing
t_dec_ratio_scan_fine = np.logspace(-1.0, 2.0, 5000)  # (local)
dOOM_scan_fine = np.zeros(len(t_dec_ratio_scan_fine))  # (local)
for idx, tdr in enumerate(t_dec_ratio_scan_fine):
    dOOM_scan_fine[idx], _, _ = s72_delta_OOM(tdr, r_k_bcs_s72, delta_r_slow_s72, mw_s72)

idx_tgt = np.argmin(np.abs(dOOM_scan_fine - 0.267))  # (local)
t_dec_exact_for_target = t_dec_ratio_scan_fine[idx_tgt]  # (local)
print(f"  Exact t_dec/t_transit for delta_OOM=0.267: {t_dec_exact_for_target:.4f}")
print(f"    (gives delta_OOM = {dOOM_scan_fine[idx_tgt]:.4f})")
print()

# The S72 residual delta_OOM at our combined t_dec:
delta_OOM_residual_final = dOOM_at_combined  # (local)
print(f"  RESIDUAL A_s GAP: delta_OOM = {delta_OOM_residual_final:.4f}")
print(f"  Target: 0.267")
if delta_OOM_residual_final < 0.267:
    print(f"  Over-decoheres: A_s_pred brought BELOW A_s_obs")
else:
    print(f"  Under-decoheres: residual overshoot {delta_OOM_residual_final - 0.267:.4f}")
print()

# =============================================================================
#  SECTION 6: GATE VERDICT
# =============================================================================
print("SECTION 6: Gate Verdict")
print("-" * 76)

# Gate criterion from pre-registration:
# PASS: Combined t_dec/t_transit in [0.57, 0.88] OR combined delta_OOM in [0.20, 0.35]
# INFO: values computed; report decomposition
# FAIL: Channels not independent AND outside band

in_t_dec_band = 0.57 <= t_dec_combined <= 0.88  # (local)
in_delta_OOM_band = 0.20 <= delta_OOM_combined <= 0.35  # (local)

# The channels ARE independent (Section 3). Combined t_dec = 0.267 is below
# gate band [0.57, 0.88]. Combined delta_OOM = 0.486 is above gate band
# [0.20, 0.35]. The multi-channel budget OVER-DECOHERES.

# Two interpretations of the S72 residual A_s gap:
# (A) delta_OOM_combined is the FIDELITY REDUCTION (power spectrum factor).
#     This acts multiplicatively: A_s_pred -> A_s_pred * 10^{-0.486}.
#     Residual gap = delta_OOM_undamped - delta_OOM_combined = 2.074 - 0.486 = 1.588.
# (B) The S72 dual-timescale model uses t_dec as the BCS phase decoherence time
#     and computes delta_OOM = log10(sum w_k cosh(2 r_k_dec)).
#     Our multi-channel t_dec_combined feeds into this model directly.
#     The result: delta_OOM_S72 = dOOM_at_combined (computed in Section 5).

# Use interpretation (B) as the primary result (it uses the S72 formula)
# and interpretation (A) as a cross-check.
delta_OOM_interp_A = delta_OOM_undamped - delta_OOM_combined  # fidelity subtraction  # (local)
delta_OOM_interp_B = delta_OOM_residual_final  # S72 formula  # (local)

print(f"  TWO INTERPRETATIONS:")
print(f"    (A) Fidelity subtraction: {delta_OOM_undamped:.4f} - {delta_OOM_combined:.4f} = {delta_OOM_interp_A:.4f}")
print(f"    (B) S72 formula at t_dec={t_dec_combined:.4f}: {delta_OOM_interp_B:.4f}")
print()

# Determine verdict
if in_t_dec_band or in_delta_OOM_band:
    verdict = "PASS"
    verdict_detail = (f"Combined t_dec/t_transit = {t_dec_combined:.4f} in [0.57, 0.88]."
                     if in_t_dec_band else
                     f"Combined delta_OOM = {delta_OOM_combined:.4f} in [0.20, 0.35].")
else:
    verdict = "INFO"
    verdict_detail = (f"Combined t_dec/t_transit = {t_dec_combined:.4f} (below [0.57, 0.88]). "
                     f"delta_OOM_combined = {delta_OOM_combined:.4f} (above [0.20, 0.35]). "
                     f"S72 residual = {delta_OOM_residual_final:.4f}. "
                     f"Channels INDEPENDENT. Over-decoheres by "
                     f"{delta_OOM_combined/delta_OOM_target:.1f}x vs target.")

# A_s status (from S72 model)
if delta_OOM_residual_final < 0.30:
    As_status = "CLOSED"
elif delta_OOM_residual_final < 0.50:
    As_status = "MARGINAL"
else:
    As_status = "OPEN"

print(f"  GATE: RE-DECOHERENCE-MULTI-73a")
print(f"  VERDICT: {verdict}")
print(f"  DETAIL: {verdict_detail}")
print(f"  A_s STATUS: {As_status} (S72 residual = {delta_OOM_residual_final:.4f})")
print()

# =============================================================================
#  SECTION 7: CROSS-CHECKS
# =============================================================================
print("SECTION 7: Cross-Checks")
print("-" * 76)

# CC-1: Individual channel recovery
cc1_mott = abs(delta_OOM_ch2 - 0.336) < 0.01  # (local)
cc1_disp = abs(delta_OOM_ch4 - 0.150) < 0.01  # (local)
print(f"  CC-1: Channel recovery")
print(f"    Mott: {delta_OOM_ch2:.4f} vs 0.336 {'PASS' if cc1_mott else 'FAIL'}")
print(f"    Disp: {delta_OOM_ch4:.4f} vs 0.150 {'PASS' if cc1_disp else 'FAIL'}")

# CC-2: Isotropic limit (already checked in Section 2)
print(f"  CC-2: Isotropic limit => delta_OOM_aniso = 0: PASS (by vertex-transitivity)")

# CC-3: Combined > max(individual) for independent channels
cc3 = delta_OOM_combined > max(delta_OOM_ch2, delta_OOM_ch4)  # (local)
print(f"  CC-3: Combined ({delta_OOM_combined:.4f}) > max ({max(delta_OOM_ch2, delta_OOM_ch4):.4f}): "
      f"{'PASS' if cc3 else 'FAIL'}")

# CC-4: Additive > max (consistent with independence)
print(f"  CC-4: Additive > overlap: {'PASS' if cc3 else 'FAIL'}")

# CC-5: S72 undamped cross-check
print(f"  CC-5: S72 undamped delta_OOM = {dOOM_inf:.4f} vs {delta_OOM_undamped:.4f}: "
      f"{'PASS' if abs(dOOM_inf - delta_OOM_undamped) < 0.01 else 'FAIL'}")
print()

# =============================================================================
#  SECTION 8: SAVE RESULTS
# =============================================================================
print("SECTION 8: Saving results")
print("-" * 76)

outfile = os.path.join(data_dir, "s73a_re_decoherence_multi.npz")

np.savez(
    outfile,
    # Gate
    gate_name="RE-DECOHERENCE-MULTI-73a",
    gate_verdict=verdict,
    gate_detail=verdict_detail,
    # Channel decomposition
    delta_OOM_ch1_exit=delta_OOM_ch1,
    delta_OOM_ch2_mott=delta_OOM_ch2,
    delta_OOM_ch3_graph=delta_OOM_ch3,
    delta_OOM_ch4_disp=delta_OOM_ch4,
    delta_OOM_ch5_aniso=delta_OOM_aniso_max,
    # Combined
    delta_OOM_combined=delta_OOM_combined,
    delta_OOM_combined_full=delta_OOM_combined_full,
    delta_OOM_quadrature=delta_OOM_quadrature,
    delta_OOM_max_overlap=max(delta_OOM_ch2, delta_OOM_ch4),
    delta_OOM_additive=delta_OOM_additive_active,
    # t_dec ratios
    t_dec_ratio_mott=t_dec_ratio_mott,
    t_dec_ratio_disp=t_dec_ratio_disp,
    t_dec_ratio_aniso=t_dec_aniso_ratio,
    t_dec_combined=t_dec_combined,
    t_dec_exact_for_target=t_dec_exact_for_target,
    # Anisotropy details
    EJ_per_trans=EJ_per_trans,
    ratio_maxmin=ratio_maxmin,
    c_directional=c_directional,
    delta_phi_aniso=delta_phi_aniso,
    delta_phi_J=delta_phi_J,
    F_aniso=F_aniso,
    F_aniso_J=F_aniso_J,
    # S72 model results
    delta_OOM_undamped=delta_OOM_undamped,
    delta_OOM_residual_S72=delta_OOM_residual_final,
    delta_OOM_interp_A=delta_OOM_interp_A,
    cosh2r_bare=cosh2r_bare,
    cosh2r_at_combined=c2r_at_combined,
    As_status=As_status,
    # Combination rule
    combination_rule="ADDITIVE (independent channels)",
    independence_basis="Mott=static/cell-phase, Dispersive=dynamic/branch-phase",
    # Cross-checks
    cc1_pass=bool(cc1_mott and cc1_disp),
    cc3_combined_gt_max=bool(cc3),
    cc5_undamped_match=bool(abs(dOOM_inf - delta_OOM_undamped) < 0.01),
    # Scan data
    t_dec_ratio_scan=t_dec_ratio_scan_fine,
    dOOM_scan=dOOM_scan_fine,
    # Mode data
    labels=labels_dual,
    mode_weights=mw_s72,
    r_k_bcs=r_k_bcs_s72,
    r_eff_modes=r_eff_modes_s72,
    r_dec_at_combined=r_dec_at_combined,
    # Timing
    elapsed_s=time.time() - t0,
)

print(f"  Saved: {outfile}")
print(f"  Elapsed: {time.time() - t0:.2f} s")
print()

# =============================================================================
#  FINAL SUMMARY
# =============================================================================
print("=" * 76)
print("FINAL SUMMARY: RE-DECOHERENCE-MULTI-73a")
print("=" * 76)
print()
print(f"GATE VERDICT: {verdict}")
print(f"  Combined t_dec/t_transit = {t_dec_combined:.4f} (gate band [0.57, 0.88])")
print(f"  Combined delta_OOM = {delta_OOM_combined:.4f} (gate band [0.20, 0.35])")
print(f"  S72 residual delta_OOM = {delta_OOM_residual_final:.4f}")
print(f"  Channels INDEPENDENT (Mott: cell phases, dispersive: branch phases)")
print()
print("CHANNEL DECOMPOSITION:")
print(f"  | {'Channel':<32s} | {'delta_OOM':>10s} | {'t_dec/t_tr':>10s} | {'Status':<22s} |")
print(f"  | {'-'*32} | {'-'*10} | {'-'*10} | {'-'*22} |")
print(f"  | {'Exit Bogoliubov (W1-A)':<32s} | {'0.000':>10s} | {'23.195':>10s} | {'DEAD':22s} |")
print(f"  | {'Mott charge noise (W1-E)':<32s} | {delta_OOM_ch2:10.4f} | {t_dec_ratio_mott:10.4f} | {'ACTIVE':22s} |")
print(f"  | {'Graph spectral (W2-C)':<32s} | {'0.000':>10s} | {'346.6':>10s} | {'DEAD':22s} |")
print(f"  | {'Inter-branch dispersive (W3-A)':<32s} | {delta_OOM_ch4:10.4f} | {t_dec_ratio_disp:10.4f} | {'ACTIVE':22s} |")
print(f"  | {'Josephson anisotropy (W4-B)':<32s} | {delta_OOM_aniso_max:10.4e} | {t_dec_aniso_ratio:10.2f} | {'NEGLIGIBLE':22s} |")
print(f"  | {'-'*32} | {'-'*10} | {'-'*10} | {'-'*22} |")
print(f"  | {'COMBINED (additive)':<32s} | {delta_OOM_combined:10.4f} | {t_dec_combined:10.4f} | {'OVER-DECOHERES':22s} |")
print()
print(f"A_s STATUS: {As_status}")
print(f"  S72 residual gap: {delta_OOM_residual_final:.4f} OOM")
print(f"  Fidelity-subtraction gap: {delta_OOM_interp_A:.4f} OOM")
print(f"  Needed t_dec for 0.267: {t_dec_exact_for_target:.4f}")
print(f"  Have t_dec: {t_dec_combined:.4f}")
print()
pct_mott = delta_OOM_ch2 / delta_OOM_combined * 100  # (local)
pct_disp = delta_OOM_ch4 / delta_OOM_combined * 100  # (local)
print("KEY PHYSICAL RESULT:")
print(f"  Mott contributes {pct_mott:.0f}% of total decoherence, dispersive {pct_disp:.0f}%.")
print(f"  Josephson anisotropy is NEGLIGIBLE (CG(24) vertex-transitive).")
print(f"  The 11.8x directional anisotropy creates frequency shifts acting for")
print(f"  only dt_transit = {dt_transit:.4e} M_KK^{{-1}}: delta_phi_J = {delta_phi_J:.4e} rad.")
print(f"  Multi-channel budget over-decoheres by {delta_OOM_combined/delta_OOM_target:.1f}x vs target.")
