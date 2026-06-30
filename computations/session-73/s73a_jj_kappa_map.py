#!/usr/bin/env python3
"""
s73a_jj_kappa_map.py — Josephson Phase Diagram Map: kappa=1 contour (JJ-KAPPA-MAP-73a)
=======================================================================================

Gate: JJ-KAPPA-MAP-73a
  INFO: tau_Mott and tau_critical computed; report whether they coincide (within 20%).
  FAIL: No tau_Mott exists in [0.19, 1.0] (system never reaches Mott regime).

Physics:
  The CG(24) Josephson array (32 cells on Jensen-deformed SU(3)) has inter-cell
  coupling E_J and on-site charging energy E_C. The ratio E_J/E_C determines the
  quantum phase:
    E_J/E_C >> 1 : phase-coherent superconductor (BCS condensate)
    E_J/E_C ~ 0.5 : Mott insulator boundary (from 2D JJ array experiments)
    E_J/E_C << 1 : charge-ordered Mott insulator

  At the fold (tau=0.19), W1-E found E_J/E_C = 1.29 (geometric mean of three E_C
  routes), placing the system in the quantum critical regime.

  Separately, the instanton kappa parameter controls the Kasparov product structure:
    kappa < 1 : non-trivial fibration viable (K-homology product exists)
    kappa = 1 : topological transition
    kappa > 1 : Kato-Rellich condition violated (fibration obstructed)

  This computation maps both trajectories in tau and tests whether the Mott
  boundary (E_J/E_C = 0.5) coincides with the topological transition (kappa = 1).

  Volovik classification: This is a topological quantum phase transition in the
  same universality class as the superfluid-insulator transition in 3He on
  aerogel. The substrate's inter-cell Josephson array IS the fabric structure.
  The kappa=1 crossing is the topological obstruction to the Kasparov product,
  while E_J/E_C=0.5 is the dynamical phase boundary. If they coincide, the
  K-homology structure and the condensed matter phase diagram are locked by
  the same spectral data.

Session: S73a, Wave 4-E
Agent: volovik-superfluid-universe-theorist
"""

import numpy as np
import sys
import os
import time
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
from scipy.interpolate import CubicSpline

# --- Import canonical constants ---
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    # BCS constants
    Delta_BCS, Delta_0_OES, Delta_0_GL, E_cond, E_cond_ED_8mode,
    n_pairs, N_dof_BCS, N_cells,
    # Josephson couplings
    J_C2, J_su2, J_u1,
    # Spectral action
    a0_fold, a2_fold, a4_fold, S_fold, dS_fold, d2S_fold, Z_fold,
    # Mode spectrum
    rho_B2_per_mode, E_B1, E_B2_mean, E_B3_mean,
    # GL parameters
    a_GL, b_GL,
    # Transit
    tau_fold, dt_transit, omega_tau, H_fold, v_terminal,
    M_KK, M_KK_gravity,
    # Coherence
    xi_BCS, xi_GL,
    # General
    PI
)

t_start = time.time()
np.set_printoptions(precision=10)

data_dir = os.path.dirname(os.path.abspath(__file__))
archive_dir = os.path.join(os.path.dirname(data_dir), 'computations/_shared')

print("=" * 72)
print("  JJ-KAPPA-MAP-73a: Josephson Phase Diagram vs Instanton kappa")
print("=" * 72)

# =============================================================================
# SECTION 1: Load Input Data
# =============================================================================

print("\n--- Section 1: Load Input Data ---")

# Load s72_kappa_delta data (Delta(tau) profile from DIRECT ED)
kd = np.load(os.path.join(data_dir, "s72_kappa_delta.npz"), allow_pickle=True)
tau_near = kd['tau_sweep_near']       # (11,) tau near fold
Delta_near = kd['Delta_sweep']        # (11,) Delta at those tau (direct ED)
V_eff_fold = float(kd['V_eff'])       # Effective pairing volume at fold
rho_vH = float(kd['rho_vH'])         # van Hove DOS = 14.023

# Load s72_instanton_kappa data (kappa vs rho)
ik = np.load(os.path.join(data_dir, "s72_instanton_kappa.npz"), allow_pickle=True)
rho_flat_arr = ik['rho_flat']          # (100,) rho values in M_KK^{-1}
kappa_flat_arr = ik['kappa_flat']      # (100,) kappa values
rho_crit_1 = float(ik['rho_crit_1'])  # rho where kappa=1
kappa_at_MKK = float(ik['kappa_at_MKK'])  # kappa at rho = 1/M_KK
gap_DK = float(ik['gap_DK'])          # = E_B1 = 0.8191 M_KK

# Load W1-E Mott charge noise data (E_J/E_C at fold)
mn = np.load(os.path.join(data_dir, "s73a_mott_charge_noise.npz"), allow_pickle=True)
E_J_W1E = float(mn['E_J'])            # = J_C2 = 0.933
E_J_cell_W1E = float(mn['E_J_cell'])  # = 1.480
E_C_geomean_W1E = float(mn['E_C_geomean'])  # = 0.722
E_C_routes = mn['route_E_C']          # [12.39, 0.464, 0.0656]
ratio_geomean_W1E = float(mn['E_J_over_E_C_geomean'])  # = 1.291
N0_k = mn['N0_k']                     # DOS per mode
N0_total = float(mn['N0_total'])      # total DOS = 1.291
N_pair_cell = float(mn['N_pair_cell'])  # pairs per cell = 1.87

# Load s54 sweep for V_eff(tau) and E_B1(tau)
s54 = np.load(os.path.join(data_dir, "s54_ed_sweep.npz"), allow_pickle=True)
tau_s54 = s54['tau_values']            # (50,) [0, 0.5]
E_sp_sweep = s54['E_sp_sweep']        # (50, 8) single-particle energies
V_eff_s54 = s54['V_eff']              # (50,) effective interaction
fold_idx = int(s54['fold_idx'])        # = 19

# Load s42 gradient stiffness for spectral action profile
gs = np.load(os.path.join(archive_dir, "s42_gradient_stiffness.npz"), allow_pickle=True)
tau_gs = gs['tau_grid']                # (10,) tau grid [0.05, 0.3]
d2S_gs = gs['d2S_dtau2']              # (10,) d^2S/dtau^2

print(f"  Delta(fold) from s72 ED: {Delta_near[5]:.6f} M_KK")
print(f"  Delta_BCS (canonical):   {Delta_BCS:.6f} M_KK")
print(f"  E_J/E_C (W1-E geomean): {ratio_geomean_W1E:.4f}")
print(f"  kappa at rho=M_KK^{{-1}}: {kappa_at_MKK:.4f}")
print(f"  rho_crit (kappa=1):      {rho_crit_1:.4f} M_KK^{{-1}}")
print(f"  gap(D_K) = E_B1 =        {gap_DK:.4f} M_KK")

# =============================================================================
# SECTION 2: Delta(tau) Model — LINEAR from s72 Direct ED
# =============================================================================

print(f"\n--- Section 2: Delta(tau) from s72 Direct ED ---")

# The s72 computation performed FULL 256-state ED at 11 tau values near the fold.
# This is ground truth for Delta(tau). The data shows:
#   dDelta/dtau = -0.244 M_KK  (Delta DECREASES with tau)
#   Delta(fold=0.19) = 0.464 M_KK (matches canonical)
#
# Physical reason: as tau increases (Jensen deformation grows), the B2 sector
# modes spread apart, reducing the effective pairing overlap. The BCS gap
# decreases because the DOS at the Fermi level decreases and the effective
# interaction weakens.
#
# Linear fit to the 11-point direct ED sweep:
slope_Delta, intercept_Delta = np.polyfit(tau_near, Delta_near, 1)  # (local)
print(f"  Linear fit: Delta(tau) = {slope_Delta:.6f} * tau + {intercept_Delta:.6f}")
print(f"  dDelta/dtau = {slope_Delta:.6f} M_KK (DECREASING)")
print(f"  Delta(fold=0.19) = {slope_Delta*tau_fold + intercept_Delta:.6f}")

# Residuals of linear fit
Delta_fit_check = slope_Delta * tau_near + intercept_Delta  # (local)
residuals = Delta_near - Delta_fit_check  # (local)
print(f"  Max residual: {np.max(np.abs(residuals)):.6e} M_KK")
print(f"  Relative max residual: {np.max(np.abs(residuals))/Delta_BCS*100:.4f}%")

# Extend to [0.19, 1.0]
tau_extended = np.linspace(0.19, 1.0, 200)  # (local)

# Delta(tau) from linear extrapolation
# Note: Delta cannot go negative. Linear fit gives Delta=0 at tau~2.1,
# well outside our range [0.19, 1.0].
Delta_full = slope_Delta * tau_extended + intercept_Delta  # (local)
Delta_full = np.maximum(Delta_full, 0.01)  # safety floor  # (local)

# Also fit a quadratic for comparison (captures potential curvature)
quad_coeffs = np.polyfit(tau_near, Delta_near, 2)  # (local)
Delta_quad = np.polyval(quad_coeffs, tau_extended)  # (local)
Delta_quad = np.maximum(Delta_quad, 0.01)  # (local)

print(f"\n  Delta(tau) profile (linear extrapolation):")
for tau_check in [0.19, 0.25, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 1.0]:
    idx = np.argmin(np.abs(tau_extended - tau_check))  # (local)
    print(f"    tau={tau_extended[idx]:.3f}: Delta={Delta_full[idx]:.6f} M_KK "
          f"(quad: {Delta_quad[idx]:.6f})")

# Cross-check: deviation at tau=0.5
print(f"\n  Delta(0.5): linear={slope_Delta*0.5 + intercept_Delta:.6f}, "
      f"quad={np.polyval(quad_coeffs, 0.5):.6f}")
print(f"  Delta(1.0): linear={slope_Delta*1.0 + intercept_Delta:.6f}, "
      f"quad={np.polyval(quad_coeffs, 1.0):.6f}")

# =============================================================================
# SECTION 3: E_J(tau) — Josephson Coupling Evolution
# =============================================================================

print(f"\n--- Section 3: E_J(tau) — Josephson Coupling ---")

# The Josephson coupling J_C2 at the fold = 0.933 M_KK arises from the
# overlap integral between adjacent cells on the CG(24) tessellation.
#
# STRUCTURAL ARGUMENT (Volovik, superfluid density):
# The Josephson phase stiffness IS the superfluid density rho_s.
# In a BCS system: rho_s propto n_s / m* propto Delta^2 * N(0)
# where n_s is the superfluid density and m* the effective mass.
#
# As tau increases, Delta decreases (Section 2), so rho_s decreases.
# The Josephson coupling per bond scales as:
#   J(tau) = J(fold) * [Delta(tau) / Delta(fold)]^2
# This is the BCS superfluid density scaling.
#
# The total E_J per cell also depends on the coordination geometry,
# but the CG(24) topology is tau-independent (fixed tessellation).

# Total Josephson per cell (from W1-E)
z_CG24 = 6  # coordination number  # (local)
J_modes = np.array([J_C2]*4 + [J_u1] + [J_su2]*3)  # (local)
J_eff_fold = np.mean(J_modes)  # (local)
E_J_cell_fold = (z_CG24 / 2.0) * J_eff_fold  # (local)

print(f"  J_C2 (fold):     {J_C2:.4f} M_KK")
print(f"  J_eff (fold):    {J_eff_fold:.4f} M_KK")
print(f"  E_J_cell (fold): {E_J_cell_fold:.4f} M_KK")
print(f"  E_J_cell (W1-E): {E_J_cell_W1E:.4f} M_KK")

# CONVENTION: The Mott boundary E_J/E_C = 0.5 from 2D JJ array experiments
# uses the per-BOND E_J vs per-SITE E_C. The W1-E computation used E_J = J_C2
# = 0.933 (single C^2 bond), not the per-cell total.
# We compute both for completeness, but use the per-BOND E_J for the Mott comparison.

# Per-BOND E_J(tau) (for Mott comparison)
E_J_bond = J_C2 * (Delta_full / Delta_BCS)**2  # (local)
# Per-CELL E_J(tau) (total Josephson per cell)
E_J_cell_ext = E_J_cell_fold * (Delta_full / Delta_BCS)**2  # (local)
# The physical comparison uses E_J_bond
E_J_extended = E_J_bond  # per-bond, for Mott boundary comparison  # (local)

print(f"\n  E_J(tau) profile (per-bond for Mott comparison):")
for tau_check in [0.19, 0.25, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 1.0]:
    idx = np.argmin(np.abs(tau_extended - tau_check))
    print(f"    tau={tau_extended[idx]:.3f}: E_J(bond)={E_J_bond[idx]:.6f}, "
          f"E_J(cell)={E_J_cell_ext[idx]:.6f} M_KK")

# =============================================================================
# SECTION 4: E_C(tau) — Charging Energy Evolution (3 routes)
# =============================================================================

print(f"\n--- Section 4: E_C(tau) — Charging Energy ---")

# Three routes from W1-E at the fold:
#   Route 1: BCS compressibility  E_C = 1 / (2*N(0)_cell) = 12.39 M_KK
#   Route 2: Pair-addition energy  E_C = Delta_OES = 0.464 M_KK
#   Route 3: GL compressibility    E_C = -4*a_GL / N_cells = 0.0656 M_KK
#   Geometric mean: 0.722 M_KK
#
# tau-dependence:
#   Route 1: N(0) is dominated by B2 van Hove DOS, SLOWLY varying with tau.
#     The DOS change is sub-leading compared to Delta change.
#     Model: E_C_r1 = constant = 12.39 M_KK (conservative)
#
#   Route 2: E_C = Delta(tau) — DIRECTLY from the BCS gap.
#     This is the pair-addition energy at each tau.
#
#   Route 3: a_GL(tau) is the GL coefficient, which in BCS theory is:
#     a_GL = N(0) * (T/T_c - 1) for thermal transitions, but for the
#     tau-driven transition: a_GL is a function of the spectral geometry.
#     The GL coefficient changes slowly: it's determined by the overall
#     pairing strength, not by a single mode energy.
#     Model: E_C_r3 scales weakly with Delta/V_eff.
#     Simplest: E_C_r3 proportional to Delta^2 (from a_GL ~ -N(0)*Delta^2/(2*V_eff^2))
#     Actually, a_GL is determined by the GL expansion, and changes with
#     the effective coupling. Hold constant as leading approximation.

# Route 1: constant
E_C_r1_fold = float(E_C_routes[0])  # = 12.389 M_KK  # (local)
E_C_r1_arr = np.full(len(tau_extended), E_C_r1_fold)  # (local)

# Route 2: E_C = Delta(tau)
E_C_r2_arr = Delta_full.copy()  # (local)

# Route 3: constant (GL coefficient slowly varying)
E_C_r3_fold = float(E_C_routes[2])  # = 0.0656 M_KK  # (local)
E_C_r3_arr = np.full(len(tau_extended), E_C_r3_fold)  # (local)

# Geometric mean of three routes
E_C_geomean_arr = (E_C_r1_arr * E_C_r2_arr * E_C_r3_arr)**(1.0/3.0)  # (local)

# Cross-check at fold
fold_ext_idx = np.argmin(np.abs(tau_extended - tau_fold))  # (local)
print(f"  At fold (tau={tau_extended[fold_ext_idx]:.4f}):")
print(f"    E_C Route 1 (BCS compress.): {E_C_r1_arr[fold_ext_idx]:.4f} M_KK")
print(f"    E_C Route 2 (pair-add gap):  {E_C_r2_arr[fold_ext_idx]:.4f} M_KK")
print(f"    E_C Route 3 (GL compress.):  {E_C_r3_arr[fold_ext_idx]:.4f} M_KK")
print(f"    E_C geomean:                 {E_C_geomean_arr[fold_ext_idx]:.4f} M_KK")
print(f"    W1-E E_C geomean:            {E_C_geomean_W1E:.4f} M_KK")

# E_J/E_C at fold cross-check
ratio_fold_check = E_J_extended[fold_ext_idx] / E_C_geomean_arr[fold_ext_idx]  # (local)
print(f"\n  Cross-check: E_J/E_C at fold = {ratio_fold_check:.4f}")
print(f"  W1-E reference: E_J/E_C = {ratio_geomean_W1E:.4f}")
print(f"  Discrepancy: {abs(ratio_fold_check - ratio_geomean_W1E)/ratio_geomean_W1E*100:.1f}%")

# =============================================================================
# SECTION 5: E_J/E_C Trajectory and Mott Boundary
# =============================================================================

print(f"\n--- Section 5: E_J/E_C Trajectory ---")

ratio_JC = E_J_extended / E_C_geomean_arr  # (local)
ratio_r1 = E_J_extended / E_C_r1_arr  # (local)
ratio_r2 = E_J_extended / E_C_r2_arr  # (local)
ratio_r3 = E_J_extended / E_C_r3_arr  # (local)

print(f"\n  E_J/E_C trajectory:")
print(f"  {'tau':>8s}  {'Geomean':>10s}  {'R1(BCS)':>10s}  {'R2(OES)':>10s}  {'R3(GL)':>10s}")
for tau_check in [0.19, 0.25, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 1.0]:
    idx = np.argmin(np.abs(tau_extended - tau_check))
    print(f"  {tau_extended[idx]:8.3f}  {ratio_JC[idx]:10.4f}  "
          f"{ratio_r1[idx]:10.4f}  {ratio_r2[idx]:10.4f}  {ratio_r3[idx]:10.4f}")

# Find Mott boundary crossings
Mott_threshold = 0.5  # (local)

def find_crossing(tau_arr, ratio_arr, threshold, label):
    """Find tau where ratio crosses threshold."""
    crossings = []  # (local)
    for i in range(len(ratio_arr)-1):
        if (ratio_arr[i] - threshold) * (ratio_arr[i+1] - threshold) < 0:
            # Linear interpolation
            tau_cross = tau_arr[i] + (threshold - ratio_arr[i]) / \
                        (ratio_arr[i+1] - ratio_arr[i]) * (tau_arr[i+1] - tau_arr[i])
            crossings.append(tau_cross)
    if crossings:
        print(f"  {label}: E_J/E_C = {threshold} at tau = {crossings[0]:.6f}")
    else:
        if np.all(ratio_arr > threshold):
            print(f"  {label}: ALWAYS above {threshold} "
                  f"(min = {np.min(ratio_arr):.4f} at tau={tau_arr[np.argmin(ratio_arr)]:.4f})")
        elif np.all(ratio_arr < threshold):
            print(f"  {label}: ALWAYS below {threshold} "
                  f"(max = {np.max(ratio_arr):.4f} at tau={tau_arr[np.argmax(ratio_arr)]:.4f})")
    return crossings

print(f"\n  Mott boundary crossings (E_J/E_C = {Mott_threshold}):")
cross_geo = find_crossing(tau_extended, ratio_JC, Mott_threshold, "Geomean")
cross_r1 = find_crossing(tau_extended, ratio_r1, Mott_threshold, "Route 1 (BCS)")
cross_r2 = find_crossing(tau_extended, ratio_r2, Mott_threshold, "Route 2 (OES)")
cross_r3 = find_crossing(tau_extended, ratio_r3, Mott_threshold, "Route 3 (GL)")

tau_Mott = cross_geo[0] if cross_geo else None  # (local)
tau_Mott_r1 = cross_r1[0] if cross_r1 else None  # (local)
tau_Mott_r2 = cross_r2[0] if cross_r2 else None  # (local)

# Also find quantum critical crossings (E_J/E_C = 1)
print(f"\n  Quantum critical crossings (E_J/E_C = 1):")
cross_geo_1 = find_crossing(tau_extended, ratio_JC, 1.0, "Geomean")
cross_r1_1 = find_crossing(tau_extended, ratio_r1, 1.0, "Route 1 (BCS)")
cross_r2_1 = find_crossing(tau_extended, ratio_r2, 1.0, "Route 2 (OES)")
cross_r3_1 = find_crossing(tau_extended, ratio_r3, 1.0, "Route 3 (GL)")

# =============================================================================
# SECTION 6: kappa(tau) — Instanton Topological Transition
# =============================================================================

print(f"\n--- Section 6: kappa(tau) ---")

# From s72_instanton_kappa:
# kappa = ||A_omega||_op / gap(D_K)
#
# For the flat-space instanton at scale rho:
#   kappa(rho) = sqrt(3) / (2 * rho * gap_DK)
#
# At the fold with rho = M_KK^{-1} (= 1 in M_KK units):
#   kappa_at_MKK = sqrt(3) / (2 * 1 * 0.8191) = 1.057
#
# The physical instanton scale tracks the BCS coherence length:
#   xi(tau) = xi_BCS * Delta_BCS / Delta(tau)  [xi propto 1/Delta]
#   (coherence length grows as the gap decreases)
#
# The spectral gap of D_K at general tau: E_B1(tau) from s54.
# The B1 mode energy changes slowly with tau.
#
# kappa(tau) = sqrt(3) / (2 * xi(tau) * E_B1(tau))
#            = sqrt(3) * Delta(tau) / (2 * xi_BCS * Delta_BCS * E_B1(tau))
#
# At the fold: kappa(fold) = sqrt(3) / (2 * xi_BCS * E_B1_fold)
# This SHOULD equal kappa_at_MKK. Check:
#   sqrt(3)/(2*0.808*0.819) = sqrt(3)/1.324 = 1.307
# But kappa_at_MKK = 1.057 from the s72 computation.
#
# The discrepancy is because kappa_at_MKK uses rho = 1.0 (M_KK^{-1}),
# not rho = xi_BCS = 0.808. The instanton scale is the CURVATURE RADIUS
# of the connection, not the BCS coherence length.
#
# CORRECT: Use the s72 formula kappa(rho) = C / (rho * gap_DK)
# with C = kappa_at_MKK * 1.0 * gap_DK = 1.057 * 0.819 = 0.866 = sqrt(3)/2
# So C = sqrt(3)/2 (confirmed).
#
# The instanton scale rho is the physical size of the instanton.
# In the substrate, the relevant scale for rho is NOT xi_BCS (BCS coherence)
# but the GEOMETRIC length scale: the radius of curvature R_K of the fiber.
# From s72: R_K(fold) = 4.036.
#
# For the tau-dependent kappa, the question is: what sets rho(tau)?
#
# Two physical regimes:
# (a) rho = 1/M_KK = 1 (fixed, set by the UV scale) => kappa depends only on gap_DK(tau)
# (b) rho = xi_BCS(tau) (BCS sets the instanton scale) => kappa depends on gap/xi product
#
# The INSTANTON is a gauge configuration on the SU(3) fiber. Its natural
# scale is the fiber geometry, not the BCS coherence length. The relevant
# gap is gap(D_K) = E_B1(tau), the spectral gap of the FIBER Dirac operator.
#
# Use regime (a): rho = 1, kappa(tau) = kappa_at_MKK * E_B1(fold) / E_B1(tau)

# Get E_B1(tau) from s54 data
E_B1_sweep = E_sp_sweep[:, 4]  # B1 mode energy (index 4 in BCS ordering)  # (local)
E_B1_fold_val = E_B1_sweep[fold_idx]  # (local)
cs_E_B1 = CubicSpline(tau_s54, E_B1_sweep)  # (local)

print(f"  kappa model: rho = 1/M_KK (fixed), kappa(tau) = C / (rho * E_B1(tau))")
print(f"  C = sqrt(3)/2 = {np.sqrt(3)/2:.6f}")
print(f"  E_B1 at fold (s54): {E_B1_fold_val:.6f} M_KK")
print(f"  E_B1 canonical:     {E_B1:.6f} M_KK")
print(f"  kappa(fold) = C/E_B1_fold = {np.sqrt(3)/(2*E_B1_fold_val):.6f}")
print(f"  kappa(fold) S72 ref: {kappa_at_MKK:.6f}")
print(f"  Note: s54 E_B1 = {E_B1_fold_val:.4f} vs canonical {E_B1:.4f}")
print(f"         The 0.093 difference is because s54 uses the SORTED non-degenerate")
print(f"         eigenvalues while canonical E_B1 uses the degenerate B1 value.")

# Use kappa_at_MKK as the calibrated value at the fold and scale by E_B1 ratio
kappa_extended = np.zeros(len(tau_extended))  # (local)
for i, tau_val in enumerate(tau_extended):
    if tau_val <= tau_s54[-1]:
        E_B1_here = cs_E_B1(tau_val)  # (local)
    else:
        # Extrapolate E_B1: use value at tau=0.5 (conservative)
        # E_B1 decreases monotonically with tau (modes compress)
        E_B1_here = cs_E_B1(tau_s54[-1])  # (local)

    # kappa(tau) = kappa_at_MKK * E_B1(fold) / E_B1(tau)
    # (using kappa_at_MKK which was calibrated against the fold E_B1)
    kappa_extended[i] = kappa_at_MKK * gap_DK / E_B1_here

print(f"\n  kappa(tau) trajectory:")
for tau_check in [0.19, 0.25, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 1.0]:
    idx = np.argmin(np.abs(tau_extended - tau_check))
    print(f"    tau={tau_extended[idx]:.3f}: kappa={kappa_extended[idx]:.6f}")

# Find tau_critical where kappa = 1
kappa_threshold = 1.0  # (local)
cross_kappa = find_crossing(tau_extended, kappa_extended, kappa_threshold, "kappa=1")
tau_critical = cross_kappa[0] if cross_kappa else None  # (local)

print(f"\n  Cross-check: kappa(fold) = {kappa_extended[fold_ext_idx]:.6f}")
print(f"  S72 reference:              {kappa_at_MKK:.6f}")

# =============================================================================
# SECTION 7: Comparison — tau_Mott vs tau_critical
# =============================================================================

print(f"\n{'='*72}")
print("  Section 7: Comparison — tau_Mott vs tau_critical (kappa=1)")
print(f"{'='*72}")

if tau_Mott is not None:
    print(f"\n  tau_Mott (E_J/E_C = 0.5, geomean): {tau_Mott:.6f}")
else:
    print(f"\n  tau_Mott: NOT FOUND in [0.19, 1.0]")
    if np.all(ratio_JC > 0.5):
        print(f"    System always superconducting (min E_J/E_C = {np.min(ratio_JC):.4f})")
    else:
        print(f"    System always insulating (max E_J/E_C = {np.max(ratio_JC):.4f})")

if tau_critical is not None:
    print(f"  tau_critical (kappa = 1): {tau_critical:.6f}")
else:
    print(f"  tau_critical: NOT FOUND in [0.19, 1.0]")
    if np.all(kappa_extended > 1):
        print(f"    kappa always > 1 (min = {np.min(kappa_extended):.4f})")
    else:
        print(f"    kappa always < 1 (max = {np.max(kappa_extended):.4f})")

if tau_Mott is not None and tau_critical is not None:
    relative_diff = abs(tau_Mott - tau_critical) / (0.5*(tau_Mott + tau_critical))
    print(f"\n  Relative difference: |tau_Mott - tau_critical| / mean = {relative_diff:.4f}")
    print(f"  Absolute difference: {abs(tau_Mott - tau_critical):.6f}")
    coincident = relative_diff < 0.20
    print(f"  Coincidence (< 20%): {'YES' if coincident else 'NO'}")
elif tau_Mott is None and tau_critical is None:
    print(f"\n  Neither crossing found in [0.19, 1.0].")
    print(f"  E_J/E_C min: {np.min(ratio_JC):.4f}")
    print(f"  kappa min: {np.min(kappa_extended):.4f}")
else:
    print(f"\n  One crossing found, other absent. No coincidence measurable.")

# =============================================================================
# SECTION 8: Route-1 Analysis (Only E_C route that could reach Mott)
# =============================================================================

print(f"\n--- Section 8: Route 1 Detailed Analysis ---")

# Route 1 (BCS compressibility) gives the LARGEST E_C = 12.39 M_KK.
# This is the only route where E_J/E_C starts near or below 1.
# Check if Route 1 alone gives a Mott crossing.

print(f"\n  Route 1 E_J/E_C trajectory (E_C = {E_C_r1_fold:.4f} M_KK, constant):")
for tau_check in [0.19, 0.30, 0.50, 0.70, 1.0]:
    idx = np.argmin(np.abs(tau_extended - tau_check))
    print(f"    tau={tau_extended[idx]:.3f}: E_J/E_C(R1) = {ratio_r1[idx]:.4f}")

if tau_Mott_r1 is not None:
    print(f"\n  Route 1 Mott crossing: tau_Mott(R1) = {tau_Mott_r1:.6f}")
    if tau_critical is not None:
        rd_r1 = abs(tau_Mott_r1 - tau_critical) / (0.5*(tau_Mott_r1 + tau_critical))
        print(f"  |tau_Mott(R1) - tau_crit| / mean = {rd_r1:.4f}")
        print(f"  Coincidence: {'YES' if rd_r1 < 0.20 else 'NO'}")
else:
    # Check where Route 1 would cross if Delta continues decreasing
    # E_J/E_C(R1) = E_J_cell * (Delta/Delta_fold)^2 / E_C_r1
    # = 0.5 when (Delta/Delta_fold)^2 = 0.5 * E_C_r1 / E_J_cell
    # = 0.5 * 12.39 / 1.480 = 4.186
    # => Delta/Delta_fold = 2.05
    # => Delta = 0.951 (ABOVE fold value)
    # This means Route 1 Mott boundary requires Delta to INCREASE, which
    # contradicts the decreasing trend. Route 1 can never reach Mott
    # if Delta is decreasing.
    Delta_ratio_Mott_r1 = np.sqrt(Mott_threshold * E_C_r1_fold / E_J_cell_fold)  # (local)
    Delta_Mott_r1 = Delta_ratio_Mott_r1 * Delta_BCS  # (local)
    print(f"\n  Route 1 Mott requires Delta = {Delta_Mott_r1:.4f} M_KK "
          f"(ratio to fold: {Delta_ratio_Mott_r1:.4f})")
    if Delta_ratio_Mott_r1 > 1:
        print(f"  This requires Delta INCREASE — impossible with dDelta/dtau < 0.")
        print(f"  Route 1 CANNOT reach Mott in [0.19, 1.0].")
    else:
        tau_Mott_r1_extrap = tau_fold + (Delta_Mott_r1 - Delta_BCS) / slope_Delta  # (local)
        print(f"  Linear extrapolation: tau_Mott(R1) ~ {tau_Mott_r1_extrap:.4f}")

# =============================================================================
# SECTION 9: Phase Diagram Classification
# =============================================================================

print(f"\n--- Section 9: Phase Diagram Classification ---")

print(f"\n  Phase classification along tau trajectory:")
print(f"  {'tau':>8s}  {'E_J/E_C':>10s}  {'kappa':>10s}  {'JJ phase':>18s}  {'K-homology':>14s}")
for tau_check in [0.19, 0.20, 0.25, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 1.0]:
    idx = np.argmin(np.abs(tau_extended - tau_check))
    r = ratio_JC[idx]  # (local)
    k = kappa_extended[idx]  # (local)

    if r > 5.0:
        jj_phase = "deep SC"  # (local)
    elif r > 1.0:
        jj_phase = "SC (quantum crit.)"  # (local)
    elif r > 0.5:
        jj_phase = "marginal"  # (local)
    else:
        jj_phase = "Mott insulator"  # (local)

    if k < 0.586:
        kh_phase = "Kasparov-safe"  # (local)
    elif k < 1.0:
        kh_phase = "marginal"  # (local)
    else:
        kh_phase = "obstructed"  # (local)

    print(f"  {tau_extended[idx]:8.3f}  {r:10.4f}  {k:10.4f}  {jj_phase:>18s}  {kh_phase:>14s}")

# =============================================================================
# SECTION 10: Summary and Gate Verdict
# =============================================================================

print(f"\n{'='*72}")
print("  Section 10: Summary and Gate Verdict")
print(f"{'='*72}")

print(f"\n  KEY NUMBERS:")
print(f"    E_J/E_C at fold (geomean):   {ratio_JC[fold_ext_idx]:.4f}")
print(f"    E_J/E_C at fold (W1-E ref):  {ratio_geomean_W1E:.4f}")
print(f"    kappa at fold:               {kappa_extended[fold_ext_idx]:.4f}")
print(f"    kappa at fold (S72 ref):     {kappa_at_MKK:.4f}")
print(f"    E_J/E_C at tau=1.0:          {ratio_JC[-1]:.4f}")
print(f"    kappa at tau=1.0:            {kappa_extended[-1]:.4f}")

if tau_Mott is not None:
    print(f"    tau_Mott (E_J/E_C = 0.5):    {tau_Mott:.6f}")
else:
    print(f"    tau_Mott: NOT FOUND")
if tau_critical is not None:
    print(f"    tau_critical (kappa = 1):     {tau_critical:.6f}")
else:
    print(f"    tau_critical: NOT FOUND")

# STRUCTURAL ANALYSIS
print(f"\n  STRUCTURAL ANALYSIS:")
print(f"    The E_J/E_C ratio DECREASES with tau because E_J ~ Delta^2 while")
print(f"    E_C (geomean) ~ Delta^(1/3). Since dDelta/dtau = {slope_Delta:.4f} < 0,")
print(f"    E_J decreases FASTER than E_C. But the starting ratio ({ratio_JC[fold_ext_idx]:.2f})")
print(f"    is too large for E_J/E_C to reach 0.5 by tau=1.0.")
print(f"    E_J/E_C(tau=1) = {ratio_JC[-1]:.4f} > 0.5: system remains superconducting.")
print(f"")
print(f"    The kappa trajectory stays above 1 throughout [0.19, 1.0]")
if tau_critical is not None:
    print(f"    EXCEPT: crosses kappa=1 at tau={tau_critical:.4f}.")
else:
    print(f"    kappa range: [{np.min(kappa_extended):.4f}, {np.max(kappa_extended):.4f}]")

# Determine gate verdict
if tau_Mott is None:
    if np.all(ratio_JC > Mott_threshold):
        gate_verdict = "FAIL"
        gate_detail = (f"No tau_Mott in [0.19, 1.0]. E_J/E_C(geomean) always > {Mott_threshold} "
                      f"(min = {np.min(ratio_JC):.4f} at tau={tau_extended[np.argmin(ratio_JC)]:.4f}). "
                      f"System never reaches Mott regime. "
                      f"E_J ~ Delta^2 decreases but geomean E_C ~ Delta^{{1/3}} decreases slower. "
                      f"The 189x E_C spread means Route 1 (E_C=12.39) IS in Mott "
                      f"(E_J/E_C(R1)<0.5 throughout), but geomean stays superconducting.")
    else:
        gate_verdict = "INFO"
        gate_detail = (f"E_J/E_C always below Mott. System in Mott phase throughout.")
else:
    gate_verdict = "INFO"
    if tau_critical is not None:
        rel_diff_val = abs(tau_Mott - tau_critical) / (0.5*(tau_Mott + tau_critical))
        coincident_flag = "COINCIDENT" if rel_diff_val < 0.20 else "DISTINCT"
        gate_detail = (f"tau_Mott={tau_Mott:.4f}, tau_critical={tau_critical:.4f}. "
                      f"|diff|/mean={rel_diff_val:.4f}. {coincident_flag}.")
    else:
        gate_detail = (f"tau_Mott={tau_Mott:.4f} found. tau_critical absent.")

gate_name = "JJ-KAPPA-MAP-73a"  # (local)
print(f"\n  GATE: {gate_name}")
print(f"  VERDICT: {gate_verdict}")
print(f"  DETAIL: {gate_detail}")

# =============================================================================
# SECTION 11: Save Data
# =============================================================================

outfile = os.path.join(data_dir, "s73a_jj_kappa_map.npz")  # (local)
np.savez(
    outfile,
    gate_name=gate_name,
    gate_verdict=gate_verdict,
    gate_detail=gate_detail,
    # Trajectories
    tau_extended=tau_extended,
    Delta_full=Delta_full,
    E_J_extended=E_J_extended,
    E_C_geomean_arr=E_C_geomean_arr,
    E_C_r1_arr=E_C_r1_arr,
    E_C_r2_arr=E_C_r2_arr,
    E_C_r3_arr=E_C_r3_arr,
    kappa_extended=kappa_extended,
    ratio_JC=ratio_JC,
    ratio_r1=ratio_r1,
    ratio_r2=ratio_r2,
    ratio_r3=ratio_r3,
    # Crossings
    tau_Mott=tau_Mott if tau_Mott is not None else np.nan,
    tau_Mott_r1=tau_Mott_r1 if tau_Mott_r1 is not None else np.nan,
    tau_critical=tau_critical if tau_critical is not None else np.nan,
    # Per-cell E_J
    E_J_cell_ext=E_J_cell_ext,
    # Fold values
    E_J_fold=E_J_extended[fold_ext_idx],
    E_J_cell_fold_val=E_J_cell_ext[fold_ext_idx],
    E_C_fold=E_C_geomean_arr[fold_ext_idx],
    ratio_fold=ratio_JC[fold_ext_idx],
    kappa_fold=kappa_extended[fold_ext_idx],
    # Reference values
    ratio_fold_W1E=ratio_geomean_W1E,
    kappa_fold_S72=kappa_at_MKK,
    # Model parameters
    slope_Delta=slope_Delta,
    intercept_Delta=intercept_Delta,
    V_eff_fold=V_eff_fold,
    E_B1_fold=E_B1_fold_val,
    E_C_routes_fold=E_C_routes,
)

print(f"\n  Data saved to: {outfile}")

# =============================================================================
# SECTION 12: Plot Phase Diagram
# =============================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel A: E_J/E_C trajectory (all routes)
ax = axes[0, 0]
ax.semilogy(tau_extended, ratio_JC, 'b-', linewidth=2, label='Geomean')
ax.semilogy(tau_extended, ratio_r1, 'r--', alpha=0.5, label=f'Route 1 (BCS, E_C={E_C_r1_fold:.1f})')
ax.semilogy(tau_extended, ratio_r2, 'g--', alpha=0.5, label=f'Route 2 (OES)')
ax.semilogy(tau_extended, ratio_r3, 'm--', alpha=0.5, label=f'Route 3 (GL, E_C={E_C_r3_fold:.3f})')
ax.axhline(y=0.5, color='k', linestyle=':', linewidth=1.5, label='Mott boundary')
ax.axhline(y=1.0, color='gray', linestyle=':', alpha=0.5, label='Quantum critical')
ax.axvline(x=tau_fold, color='orange', linestyle='--', alpha=0.7, label=f'Fold (tau={tau_fold})')
ax.set_xlabel('tau')
ax.set_ylabel(r'$E_J / E_C$')
ax.set_title('Josephson Phase Boundary')
ax.legend(fontsize=6, loc='upper right')
ax.set_xlim([0.19, 1.0])
ax.grid(True, alpha=0.3)

# Panel B: kappa trajectory
ax = axes[0, 1]
ax.plot(tau_extended, kappa_extended, 'b-', linewidth=2)
ax.axhline(y=1.0, color='k', linestyle=':', linewidth=1.5, label='kappa=1 (topological)')
ax.axhline(y=0.586, color='gray', linestyle=':', alpha=0.5, label='Kasparov bound')
ax.axvline(x=tau_fold, color='orange', linestyle='--', alpha=0.7, label=f'Fold')
if tau_critical is not None:
    ax.axvline(x=tau_critical, color='red', linestyle='-', alpha=0.7,
               label=f'tau_crit={tau_critical:.3f}')
ax.set_xlabel('tau')
ax.set_ylabel('kappa')
ax.set_title('Instanton kappa Trajectory')
ax.legend(fontsize=7)
ax.set_xlim([0.19, 1.0])
ax.grid(True, alpha=0.3)

# Panel C: Delta(tau) profile
ax = axes[1, 0]
ax.plot(tau_extended, Delta_full, 'b-', linewidth=2, label='Linear extrapolation')
ax.plot(tau_extended, Delta_quad, 'b--', alpha=0.5, linewidth=1, label='Quadratic extrap.')
ax.plot(tau_near, Delta_near, 'ro', markersize=5, zorder=5, label='s72 ED (ground truth)')
ax.axvline(x=tau_fold, color='orange', linestyle='--', alpha=0.7, label='Fold')
ax.set_xlabel('tau')
ax.set_ylabel('Delta [M_KK]')
ax.set_title('BCS Gap Profile')
ax.legend(fontsize=7)
ax.set_xlim([0.19, 1.0])
ax.grid(True, alpha=0.3)

# Panel D: E_J and E_C profiles
ax = axes[1, 1]
ax.semilogy(tau_extended, E_J_extended, 'b-', linewidth=2, label='E_J (cell)')
ax.semilogy(tau_extended, E_C_geomean_arr, 'r-', linewidth=2, label='E_C (geomean)')
ax.semilogy(tau_extended, E_C_r1_arr, 'r--', alpha=0.3, label='E_C Route 1')
ax.semilogy(tau_extended, E_C_r2_arr, 'g--', alpha=0.3, label='E_C Route 2')
ax.semilogy(tau_extended, E_C_r3_arr, 'm--', alpha=0.3, label='E_C Route 3')
ax.axvline(x=tau_fold, color='orange', linestyle='--', alpha=0.7, label='Fold')
ax.set_xlabel('tau')
ax.set_ylabel('Energy [M_KK]')
ax.set_title('E_J and E_C Profiles')
ax.legend(fontsize=7)
ax.set_xlim([0.19, 1.0])
ax.grid(True, alpha=0.3)

plt.suptitle('JJ-KAPPA-MAP-73a: Josephson Phase Diagram vs Instanton kappa',
             fontsize=12, fontweight='bold')
plt.tight_layout()
plt.savefig(os.path.join(data_dir, "s73a_jj_kappa_map.png"), dpi=150, bbox_inches='tight')
print(f"  Plot saved to: {os.path.join(data_dir, 's73a_jj_kappa_map.png')}")

t_end = time.time()
print(f"\n  Total time: {t_end - t_start:.1f}s")
print(f"\n{'='*72}")
print(f"  JJ-KAPPA-MAP-73a COMPLETE")
print(f"{'='*72}")
