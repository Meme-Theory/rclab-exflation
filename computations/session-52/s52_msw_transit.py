#!/usr/bin/env python3
"""
S52 MSW-TRANSIT-52: Internal MSW Effect During Modulus Transit
===============================================================

During the modulus transit from tau=0 to tau=0.19 (fold), the Dirac
eigenvalues of the three lightest sectors (B1, B2, B3) evolve.
A LEVEL CROSSING between B1 and B2 occurs near tau ~ 0.11.

This script applies the MSW (Mikheyev-Smirnov-Wolfenstein) formalism
to the transit quench to determine:

1. Whether the crossing is adiabatic or non-adiabatic
2. Whether MSW conversion modifies the mass hierarchy ratio R
3. What the effective PMNS-like overlap is post-transit

Key insight: In standard neutrino physics, MSW occurs when matter
potentials shift effective masses through a resonance. Here, the
GEOMETRY itself is the "matter" — the modulus tau acts as the density
parameter, and the eigenvalue evolution is the analog of the matter
potential. The transit velocity v_terminal = 26.545 M_KK sets the
sweep rate.

Gate: MSW-TRANSIT-52 (INFO)
  Reports: Does MSW modify R = Delta_m32^2/Delta_m21^2 at fold?
  Does the B1-B2 level crossing produce flavor conversion?

Author: Neutrino-Detection-Specialist (Session 52)
Date: 2026-03-20

Provenance:
  - s44_dos_tau.npz: eigenvalue spectrum at tau = 0, 0.05, 0.10, 0.15, 0.19
  - canonical_constants.py: transit parameters, sector energies
  - S52 OFFJENSEN-PMNS: B2 is isolated (block-diagonal), mixing is B1-B3 only
  - S35-37: NNI texture, Schur's lemma, V(B1,B3)=0 exactly
"""

import numpy as np
from scipy.interpolate import CubicSpline
import sys
import os
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    tau_fold, v_terminal, dt_transit, E_B1, E_B2_mean, E_B3_mean,
    M_KK, M_KK_gravity, hbar_eV_s, omega_att
)

t_start = time.time()

# ============================================================================
# SECTION 1: LOAD EIGENVALUE DATA
# ============================================================================

print("=" * 72)
print("S52 MSW-TRANSIT-52: Internal MSW During Modulus Transit")
print("=" * 72)
print()

data = np.load(os.path.join(os.path.dirname(os.path.abspath(__file__)),
               's44_dos_tau.npz'), allow_pickle=True)

tau_data = data['tau_values']  # [0, 0.05, 0.10, 0.15, 0.19]

# Sector minimum eigenvalues (mass proxies)
B1_min = data['omin_00_vs_tau']       # (0,0) singlet
B2_min = data['omin_10_01_vs_tau']    # (1,0)+(0,1) fundamental
B3_min = data['omin_11_vs_tau']       # (1,1) adjoint

# Sector maximum eigenvalues (bandwidth)
B1_max = data['omax_00_vs_tau']
B2_max = data['omax_10_01_vs_tau']
B3_max = data['omax_11_vs_tau']

print("SECTION 1: Sector eigenvalue data from s44_dos_tau.npz")
print("-" * 60)
print(f"tau points: {tau_data}")
print(f"B1 min:     {B1_min}")
print(f"B2 min:     {B2_min}")
print(f"B3 min:     {B3_min}")
print()

# ============================================================================
# SECTION 2: INTERPOLATE EIGENVALUES TO FINE TAU GRID
# ============================================================================

print("SECTION 2: Cubic spline interpolation to fine grid")
print("-" * 60)

# Fine tau grid covering full transit
N_tau = 2000  # (local)
tau_fine = np.linspace(0.0, tau_fold, N_tau)

# Cubic spline for each sector
cs_B1 = CubicSpline(tau_data, B1_min)
cs_B2 = CubicSpline(tau_data, B2_min)
cs_B3 = CubicSpline(tau_data, B3_min)

E_B1_fine = cs_B1(tau_fine)
E_B2_fine = cs_B2(tau_fine)
E_B3_fine = cs_B3(tau_fine)

# Derivatives (needed for adiabaticity parameter)
dE_B1 = cs_B1(tau_fine, 1)  # dE/dtau
dE_B2 = cs_B2(tau_fine, 1)
dE_B3 = cs_B3(tau_fine, 1)

print(f"Fine grid: {N_tau} points, dtau = {tau_fine[1]-tau_fine[0]:.6f}")
print(f"E_B1 range: [{E_B1_fine.min():.6f}, {E_B1_fine.max():.6f}]")
print(f"E_B2 range: [{E_B2_fine.min():.6f}, {E_B2_fine.max():.6f}]")
print(f"E_B3 range: [{E_B3_fine.min():.6f}, {E_B3_fine.max():.6f}]")
print()

# ============================================================================
# SECTION 3: IDENTIFY LEVEL CROSSINGS
# ============================================================================

print("SECTION 3: Level crossing detection")
print("-" * 60)

# B1-B2 gap
gap_12 = E_B1_fine - E_B2_fine
# B1-B3 gap
gap_13 = E_B1_fine - E_B3_fine
# B2-B3 gap
gap_23 = E_B2_fine - E_B3_fine

# Find zero crossings of gap_12 (B1 = B2)
crossings_12 = []
for i in range(len(gap_12) - 1):
    if gap_12[i] * gap_12[i+1] < 0:
        # Linear interpolation for crossing point
        tau_cross = tau_fine[i] - gap_12[i] * (tau_fine[i+1] - tau_fine[i]) / (gap_12[i+1] - gap_12[i])
        crossings_12.append(tau_cross)

# Find zero crossings of gap_13 (B1 = B3)
crossings_13 = []
for i in range(len(gap_13) - 1):
    if gap_13[i] * gap_13[i+1] < 0:
        tau_cross = tau_fine[i] - gap_13[i] * (tau_fine[i+1] - tau_fine[i]) / (gap_13[i+1] - gap_13[i])
        crossings_13.append(tau_cross)

# Find zero crossings of gap_23 (B2 = B3)
crossings_23 = []
for i in range(len(gap_23) - 1):
    if gap_23[i] * gap_23[i+1] < 0:
        tau_cross = tau_fine[i] - gap_23[i] * (tau_fine[i+1] - tau_fine[i]) / (gap_23[i+1] - gap_23[i])
        crossings_23.append(tau_cross)

print(f"B1-B2 crossings: {len(crossings_12)}")
for tc in crossings_12:
    E_at_cross = float(cs_B1(tc))
    print(f"  tau_cross = {tc:.6f}, E_cross = {E_at_cross:.6f}")
print(f"B1-B3 crossings: {len(crossings_13)}")
for tc in crossings_13:
    E_at_cross = float(cs_B1(tc))
    print(f"  tau_cross = {tc:.6f}, E_cross = {E_at_cross:.6f}")
print(f"B2-B3 crossings: {len(crossings_23)}")
for tc in crossings_23:
    E_at_cross = float(cs_B2(tc))
    print(f"  tau_cross = {tc:.6f}, E_cross = {E_at_cross:.6f}")
print()

# ============================================================================
# SECTION 4: ORDERING EVOLUTION
# ============================================================================

print("SECTION 4: Mass ordering evolution")
print("-" * 60)

ordering = []
for i in range(N_tau):
    vals = [('B1', E_B1_fine[i]), ('B2', E_B2_fine[i]), ('B3', E_B3_fine[i])]
    vals.sort(key=lambda x: x[1])
    ordering.append(f"{vals[0][0]}<{vals[1][0]}<{vals[2][0]}")

# Find where ordering changes
order_changes = []
for i in range(1, N_tau):
    if ordering[i] != ordering[i-1]:
        order_changes.append((tau_fine[i], ordering[i-1], ordering[i]))

print("Ordering transitions:")
for tc, old, new in order_changes:
    print(f"  tau = {tc:.6f}: {old}  -->  {new}")

# Initial and final ordering
print(f"\nInitial (tau=0):    {ordering[0]}")
print(f"Final (tau=0.19):   {ordering[-1]}")
print()

# ============================================================================
# SECTION 5: MSW ADIABATICITY PARAMETER
# ============================================================================

print("SECTION 5: MSW adiabaticity parameter")
print("-" * 60)

# MSW formalism adapted to the internal geometry:
#
# Standard MSW: gamma = delta_m^2 sin^2(2*theta) / (4*E * |dV/dr| * cos(2*theta))
# where V = sqrt(2) G_F N_e is the matter potential.
#
# Here the analog is:
#   - "mass eigenstates" = D_K eigenvalues in sectors B1, B2, B3
#   - "matter potential" = Jensen deformation tau (geometry plays role of matter)
#   - "propagation" = transit through tau from 0 to 0.19
#   - "sweep rate" = dtau/dt = v_terminal (terminal velocity from S38)
#
# The adiabaticity parameter for a 2-level crossing is:
#   gamma_MSW = (Delta E)^2 / (2 * |d(Delta E)/dtau| * dtau/dt)
#
# where Delta E = E_i - E_j is the gap at the minimum approach point,
# and dtau/dt is the transit velocity.
#
# If the levels truly cross (gap = 0 at some tau), then we need the
# "avoided crossing" gap from the off-diagonal coupling V_ij.
#
# From S34: V(B1,B3) = 0 EXACTLY (Schur/NNI). V(B1,B2) = 0.077.
# V(B2,B3) = 0.022. V(B1,B1) = 0 (Trap 1).

# Off-diagonal couplings (from S34, spinor V matrix elements in M_KK units)
V_12 = 0.077   # V(B1,B2) — Schur-allowed  # (local)
V_23 = 0.022   # V(B2,B3) — Schur-allowed  # (local)
V_13 = 0.000   # V(B1,B3) — EXACTLY ZERO (NNI texture, Trap 4)  # (local)

print("Off-diagonal couplings (S34 spinor V, M_KK units):")
print(f"  V(B1,B2) = {V_12:.4f}")
print(f"  V(B2,B3) = {V_23:.4f}")
print(f"  V(B1,B3) = {V_13:.4f} (EXACT ZERO, NNI)")
print()

# For B1-B2 crossing:
# The bare crossing happens, but V_12 != 0 creates an avoided crossing.
# Minimum gap at avoided crossing = 2*|V_12| = 0.154

# For each crossing, compute the 2x2 Landau-Zener problem
# P_LZ = exp(-pi * gamma / 2) where gamma = (2*V_12)^2 / (|d(E1-E2)/dtau| * v_terminal)

print("MSW / Landau-Zener analysis at each crossing:")
print()

# Transit velocity: dtau/dt = v_terminal (in M_KK units: tau is dimensionless, t in M_KK^-1)
# Actually v_terminal = dx/dt = 26.545 M_KK units, but tau transit duration is dt_transit
# dtau/dt = delta_tau / dt_transit = 0.19 / 0.00113 = 168.1 (M_KK units)
dtau_dt = tau_fold / dt_transit

print(f"Transit parameters:")
print(f"  tau range: 0 to {tau_fold}")
print(f"  dt_transit = {dt_transit:.6f} M_KK^{{-1}}")
print(f"  v_terminal = {v_terminal:.4f} M_KK")
print(f"  dtau/dt = {dtau_dt:.2f} M_KK (modulus velocity in tau)")
print()

# For the B1-B2 crossing:
results_crossings = []
for tc in crossings_12:
    tc_f = float(tc)
    # Derivative of gap at crossing
    dg_12 = float(cs_B1(tc_f, 1) - cs_B2(tc_f, 1))

    # Avoided crossing gap
    Delta_ac = 2 * V_12  # avoided crossing gap

    # Adiabaticity parameter (Landau-Zener)
    # gamma = pi * Delta_ac^2 / (2 * |dg/dtau| * dtau/dt)
    # Note: dtau/dt is the sweep rate of tau with respect to M_KK time
    gamma_LZ = np.pi * Delta_ac**2 / (2 * abs(dg_12) * dtau_dt)

    # Landau-Zener transition probability (diabatic jump)
    P_LZ = np.exp(-np.pi * gamma_LZ / 2)

    # Adiabatic survival probability
    P_adiab = 1 - P_LZ

    print(f"B1-B2 crossing at tau = {tc_f:.6f}:")
    print(f"  d(E_B1-E_B2)/dtau = {dg_12:.6f} M_KK")
    print(f"  Avoided crossing gap = 2*V_12 = {Delta_ac:.4f} M_KK")
    print(f"  gamma_LZ = {gamma_LZ:.6f}")
    print(f"  P_diabatic (level jump) = {P_LZ:.6e}")
    print(f"  P_adiabatic (follow level) = {P_adiab:.6f}")
    print(f"  VERDICT: {'ADIABATIC (follow curved level)' if gamma_LZ > 1 else 'NON-ADIABATIC (jump through)' if gamma_LZ < 0.01 else 'INTERMEDIATE'}")
    print()

    results_crossings.append({
        'type': 'B1-B2',
        'tau_cross': tc_f,
        'dg_dtau': dg_12,
        'Delta_ac': Delta_ac,
        'gamma_LZ': gamma_LZ,
        'P_LZ': P_LZ,
        'V_coupling': V_12,
    })

# For B1-B3 and B2-B3 crossings (if any)
for tc in crossings_13:
    tc_f = float(tc)
    dg_13 = float(cs_B1(tc_f, 1) - cs_B3(tc_f, 1))
    Delta_ac = 2 * V_13  # = 0 for B1-B3 (NNI)
    if abs(dg_13) > 1e-15:
        gamma_LZ = np.pi * Delta_ac**2 / (2 * abs(dg_13) * dtau_dt) if Delta_ac > 0 else 0.0
    else:
        gamma_LZ = float('inf') if Delta_ac > 0 else 0.0
    P_LZ = np.exp(-np.pi * gamma_LZ / 2)
    print(f"B1-B3 crossing at tau = {tc_f:.6f}:")
    print(f"  V(B1,B3) = 0 EXACTLY (NNI). TRUE crossing, no avoided crossing.")
    print(f"  d(E_B1-E_B3)/dtau = {dg_13:.6f} M_KK")
    print(f"  gamma_LZ = {gamma_LZ:.6f}")
    print(f"  P_diabatic = {P_LZ:.6e}")
    print(f"  VERDICT: NON-ADIABATIC (true crossing, V=0)")
    print()
    results_crossings.append({
        'type': 'B1-B3',
        'tau_cross': tc_f,
        'dg_dtau': dg_13,
        'Delta_ac': Delta_ac,
        'gamma_LZ': gamma_LZ,
        'P_LZ': P_LZ,
        'V_coupling': V_13,
    })

for tc in crossings_23:
    tc_f = float(tc)
    dg_23 = float(cs_B2(tc_f, 1) - cs_B3(tc_f, 1))
    Delta_ac = 2 * V_23
    gamma_LZ = np.pi * Delta_ac**2 / (2 * abs(dg_23) * dtau_dt) if abs(dg_23) > 1e-15 else float('inf')
    P_LZ = np.exp(-np.pi * gamma_LZ / 2)
    print(f"B2-B3 crossing at tau = {tc_f:.6f}:")
    print(f"  d(E_B2-E_B3)/dtau = {dg_23:.6f} M_KK")
    print(f"  Avoided crossing gap = 2*V_23 = {Delta_ac:.4f} M_KK")
    print(f"  gamma_LZ = {gamma_LZ:.6f}")
    print(f"  P_diabatic = {P_LZ:.6e}")
    print(f"  VERDICT: {'ADIABATIC' if gamma_LZ > 1 else 'NON-ADIABATIC' if gamma_LZ < 0.01 else 'INTERMEDIATE'}")
    print()
    results_crossings.append({
        'type': 'B2-B3',
        'tau_cross': tc_f,
        'dg_dtau': dg_23,
        'Delta_ac': Delta_ac,
        'gamma_LZ': gamma_LZ,
        'P_LZ': P_LZ,
        'V_coupling': V_23,
    })

# ============================================================================
# SECTION 6: MASS-SQUARED DIFFERENCES AND R RATIO
# ============================================================================

print("SECTION 6: Mass-squared differences and R ratio")
print("-" * 60)

# Mass-squared differences (in M_KK^2 units)
dm2_21_fine = E_B2_fine**2 - E_B1_fine**2
dm2_31_fine = E_B3_fine**2 - E_B1_fine**2
dm2_32_fine = E_B3_fine**2 - E_B2_fine**2

# R ratio = |dm2_31| / |dm2_21| (avoiding division by zero near crossing)
R_fine = np.zeros_like(tau_fine)
for i in range(N_tau):
    if abs(dm2_21_fine[i]) > 1e-12:
        R_fine[i] = dm2_31_fine[i] / dm2_21_fine[i]
    else:
        R_fine[i] = np.nan

# R at fold (tau = 0.19)
R_fold = R_fine[-1]
# R at tau = 0.15
idx_15 = np.argmin(np.abs(tau_fine - 0.15))
R_15 = R_fine[idx_15]

print("R ratio = dm2_31 / dm2_21 evolution:")
for t_check in [0.00, 0.05, 0.10, 0.15, 0.19]:
    idx = np.argmin(np.abs(tau_fine - t_check))
    print(f"  tau={t_check:.2f}: dm2_21={dm2_21_fine[idx]:.6f}, dm2_31={dm2_31_fine[idx]:.6f}, dm2_32={dm2_32_fine[idx]:.6f}, R={R_fine[idx]:.4f}")

print()
print(f"R at fold (tau=0.19): {R_fold:.4f}")
print(f"  NuFit-6.0 target: 33.8 (= 2.507e-3 / 7.41e-5)")
print(f"  Shortfall: {33.8 / abs(R_fold):.1f}x")
print()

# ============================================================================
# SECTION 7: MSW MODIFICATION OF R
# ============================================================================

print("SECTION 7: MSW modification of R")
print("-" * 60)

# Key question: does the B1-B2 level crossing during transit modify R?
#
# Two regimes:
# (a) ADIABATIC crossing (gamma >> 1): states follow the curved levels.
#     The physical mass eigenstate that starts as B2 at tau=0 becomes
#     the B1 state at tau=0.19. Labels swap but eigenvalues don't change.
#     R is UNCHANGED because we measure eigenvalues, not labels.
#
# (b) NON-ADIABATIC crossing (gamma << 1): states jump through.
#     The physical state keeps its tau=0 identity. The B2 mode at tau=0
#     passes through the crossing and remains B2 at tau=0.19.
#     Again R measures the eigenvalue gaps at the fold, which are fixed.
#
# (c) INTERMEDIATE: partial conversion. The post-transit state is a
#     superposition. The mass eigenvalues at the fold are the SAME either
#     way — they are eigenvalues of D_K(tau_fold). What changes is which
#     physical excitation occupies which eigenstate.
#
# CRITICAL POINT: In the framework, neutrino masses ARE the eigenvalues
# of D_K at the frozen tau. The mass hierarchy ratio R = dm2_31/dm2_21
# is a property of the OPERATOR at fixed tau, not of which state is occupied.
# MSW-like conversion during transit would affect flavor composition of
# the post-transit state (which determines the PMNS matrix), NOT the masses.

print("Analysis:")
print()
print("The B1-B2 crossing occurs during transit. Two cases:")
print()

if len(crossings_12) > 0:
    gamma = results_crossings[0]['gamma_LZ']
    P_jump = results_crossings[0]['P_LZ']

    print(f"B1-B2 crossing at tau = {results_crossings[0]['tau_cross']:.6f}")
    print(f"  gamma_LZ = {gamma:.6f}")
    print(f"  V(B1,B2) = {V_12} M_KK (nonzero coupling)")
    print()

    if gamma > 10:
        print("  VERDICT: STRONGLY ADIABATIC (gamma >> 1)")
        print("  States follow the curved energy levels through the avoided crossing.")
        print("  Post-transit: what started as B2(tau=0) is now B1(tau=0.19)")
        print("  Mass eigenvalues at fold are UNCHANGED by the transit history.")
    elif gamma > 1:
        print("  VERDICT: ADIABATIC (gamma > 1)")
        print("  States predominantly follow the curved levels.")
        print(f"  Diabatic jump probability: {P_jump:.6e}")
    elif gamma > 0.01:
        print("  VERDICT: INTERMEDIATE (partially adiabatic)")
        print(f"  Diabatic jump probability: {P_jump:.4f}")
        print("  Post-transit state is a superposition of mass eigenstates.")
    else:
        print("  VERDICT: NON-ADIABATIC (gamma << 1)")
        print("  States jump diabatically through the crossing.")
        print("  Post-transit: B2(tau=0) remains effectively B2(tau=0.19)")

    print()
    print("KEY RESULT: R = dm2_31/dm2_21 is determined by the D_K eigenvalues")
    print("at the frozen tau_fold. The transit history does NOT modify R.")
    print("R is a property of the operator, not the occupation.")
    print()
    print("What MSW DOES affect: the FLAVOR COMPOSITION of the post-transit")
    print("state. If the B1-B2 crossing is adiabatic, the lightest mass")
    print("eigenstate at the fold contains the tau=0 'B2 flavor'. If")
    print("non-adiabatic, it retains the tau=0 'B1 flavor'. This is the")
    print("analog of the MSW solar neutrino solution.")
else:
    print("No B1-B2 crossing found in the data range. No MSW conversion.")

print()

# ============================================================================
# SECTION 8: EFFECTIVE MIXING FROM TRANSIT (Analogy to solar MSW)
# ============================================================================

print("SECTION 8: Effective mixing angles from transit dynamics")
print("-" * 60)

# The transit through the crossing generates an effective mixing angle
# between mass eigenstates, analogous to how MSW generates the solar
# neutrino mixing angle.
#
# At the B1-B2 crossing, the 2x2 "matter" Hamiltonian is:
# H = ((E_B1(tau) - E_B2(tau))/2    V_12      )
#     (     V_12             -(E_B1(tau) - E_B2(tau))/2 )
#
# The mixing angle in matter (at each tau) is:
# tan(2*theta_m) = 2*V_12 / (E_B1 - E_B2)
#
# At the crossing (E_B1 = E_B2), theta_m = pi/4 (maximal mixing).
# Far from crossing, theta_m -> 0 (no mixing).

print("Effective mixing angle theta_m(tau) at selected points:")
print()

theta_m_fine = np.zeros(N_tau)
for i in range(N_tau):
    gap = E_B1_fine[i] - E_B2_fine[i]
    if abs(gap) < 1e-15:
        theta_m_fine[i] = np.pi / 4
    else:
        theta_m_fine[i] = 0.5 * np.arctan2(2 * V_12, gap)

sin2_2theta_m = np.sin(2 * theta_m_fine)**2

for t_check in [0.00, 0.05, 0.10, 0.12, 0.15, 0.19]:
    idx = np.argmin(np.abs(tau_fine - t_check))
    print(f"  tau={t_check:.2f}: theta_m = {np.degrees(theta_m_fine[idx]):.2f} deg, sin^2(2*theta_m) = {sin2_2theta_m[idx]:.6f}")

print()

# At the fold, the mixing angle
idx_fold = -1  # (local)
theta_m_fold = theta_m_fine[idx_fold]
gap_fold = E_B1_fine[idx_fold] - E_B2_fine[idx_fold]
print(f"At fold (tau=0.19):")
print(f"  E_B1 - E_B2 = {gap_fold:.6f}")
print(f"  theta_m = {np.degrees(theta_m_fold):.4f} deg")
print(f"  sin^2(theta_m) = {np.sin(theta_m_fold)**2:.6f}")
print(f"  sin^2(2*theta_m) = {sin2_2theta_m[idx_fold]:.6f}")
print()

# Effective survival probability (solar MSW analog)
# P_ee = 1/2 + (1/2 - P_LZ) * cos(2*theta_m_0) * cos(2*theta_m_fold)
# where theta_m_0 = mixing at production (tau=0), theta_m_fold = at detection (tau=0.19)

if len(crossings_12) > 0:
    P_LZ_12 = results_crossings[0]['P_LZ']
    theta_0 = theta_m_fine[0]
    theta_f = theta_m_fine[-1]
    P_surv = 0.5 + (0.5 - P_LZ_12) * np.cos(2*theta_0) * np.cos(2*theta_f)

    print(f"MSW survival probability (B1->B1):")
    print(f"  P_LZ = {P_LZ_12:.6e}")
    print(f"  cos(2*theta_0) = {np.cos(2*theta_0):.6f}")
    print(f"  cos(2*theta_f) = {np.cos(2*theta_f):.6f}")
    print(f"  P_surv = {P_surv:.6f}")
    print()

# ============================================================================
# SECTION 9: B1-B3 ANALYSIS (TRUE CROSSING, V=0)
# ============================================================================

print("SECTION 9: B1-B3 analysis (NNI constraint)")
print("-" * 60)

# B1 and B3 start degenerate at tau=0 (0.866025 both).
# They split immediately: B1 drops, B3 rises.
# V(B1,B3) = 0 EXACTLY (NNI texture, Trap 4, Schur).
# This is a TRUE crossing (not avoided), so it is always non-adiabatic.

if len(crossings_13) > 0:
    print(f"B1-B3 crossing at tau={crossings_13[0]:.6f}")
    print("  V(B1,B3) = 0 EXACTLY. TRUE crossing (no avoided crossing).")
    print("  Landau-Zener: P_diabatic = 1.000 (complete non-adiabatic jump)")
    print("  Physical: no mixing generated between B1 and B3 sectors")
else:
    print("B1 and B3 are DEGENERATE at tau=0 (both 0.866025)")
    print("They split immediately: B1 drops below, B3 rises above")
    print("V(B1,B3) = 0 EXACTLY (NNI). No coupling at ANY tau.")
    print("Even at the degenerate point, no avoided crossing exists.")
    print("This is the analog of two neutrino states that never mix.")
print()

# ============================================================================
# SECTION 10: NEAR-DEGENERACY ANALYSIS (B2-G1 from workshop)
# ============================================================================

print("SECTION 10: B2 near-degeneracy with higher sectors")
print("-" * 60)

# Check for B2-B3 near-degeneracy
min_gap_23 = np.min(np.abs(E_B2_fine - E_B3_fine))
idx_min_23 = np.argmin(np.abs(E_B2_fine - E_B3_fine))
print(f"Minimum |E_B2 - E_B3| = {min_gap_23:.6f} at tau = {tau_fine[idx_min_23]:.6f}")

# From workshop: B2-G1 near-degeneracy at tau~0.18-0.24
# G1 = (2,0)+(0,2) sector. Load its minimum eigenvalue.
G1_min = data['omin_20_02_vs_tau']
cs_G1 = CubicSpline(tau_data, G1_min)
E_G1_fine = cs_G1(tau_fine)

min_gap_2G1 = np.min(np.abs(E_B2_fine - E_G1_fine))
idx_min_2G1 = np.argmin(np.abs(E_B2_fine - E_G1_fine))
print(f"Minimum |E_B2 - E_G1| = {min_gap_2G1:.6f} at tau = {tau_fine[idx_min_2G1]:.6f}")
print(f"  E_B2 at min gap: {E_B2_fine[idx_min_2G1]:.6f}")
print(f"  E_G1 at min gap: {E_G1_fine[idx_min_2G1]:.6f}")
print()

# ============================================================================
# SECTION 11: PHYSICAL MASS PREDICTIONS AT FOLD
# ============================================================================

print("SECTION 11: Physical mass predictions at fold")
print("-" * 60)

# At tau = 0.19 (fold):
E1 = E_B1_fine[-1]
E2 = E_B2_fine[-1]
E3 = E_B3_fine[-1]

print(f"Eigenvalues at fold (M_KK units):")
print(f"  E_B1 = {E1:.8f}")
print(f"  E_B2 = {E2:.8f}")
print(f"  E_B3 = {E3:.8f}")
print()

# Mass-squared differences (M_KK^2 units)
dm2_21 = E2**2 - E1**2
dm2_31 = E3**2 - E1**2
dm2_32 = E3**2 - E2**2

print(f"Mass-squared differences (M_KK^2 units):")
print(f"  dm2_21 = E_B2^2 - E_B1^2 = {dm2_21:.8f}")
print(f"  dm2_31 = E_B3^2 - E_B1^2 = {dm2_31:.8f}")
print(f"  dm2_32 = E_B3^2 - E_B2^2 = {dm2_32:.8f}")
print()

R = dm2_31 / dm2_21
R_alt = dm2_32 / dm2_21
print(f"R = dm2_31/dm2_21 = {R:.4f}")
print(f"R' = dm2_32/dm2_21 = {R_alt:.4f}")
print(f"Target R (NuFit-6.0): {2.507e-3/7.41e-5:.1f}")
print()

# Mass ordering
print("Mass ordering:")
if E1 < E2 < E3:
    print(f"  B1 < B2 < B3: NORMAL ORDERING")
elif E1 < E3 < E2:
    print(f"  B1 < B3 < B2: INVERTED")
else:
    print(f"  Order: {E1:.6f}, {E2:.6f}, {E3:.6f}")
print()

# Absolute mass scale (using M_KK gravity route)
# m_i = E_i * M_KK (in GeV)
print(f"Absolute mass scale (using M_KK_gravity = {M_KK_gravity:.3e} GeV):")
m1_GeV = E1 * M_KK_gravity
m2_GeV = E2 * M_KK_gravity
m3_GeV = E3 * M_KK_gravity
print(f"  m_1 = {m1_GeV:.3e} GeV = {m1_GeV*1e9:.3e} eV")
print(f"  m_2 = {m2_GeV:.3e} GeV = {m2_GeV*1e9:.3e} eV")
print(f"  m_3 = {m3_GeV:.3e} GeV = {m3_GeV*1e9:.3e} eV")
print(f"  Sum = {(m1_GeV+m2_GeV+m3_GeV)*1e9:.3e} eV")
print()
print(f"  Measured: m_nu < 0.45 eV (KATRIN 90% CL)")
print(f"  Cosmological: Sum < 0.064 eV (Planck+DESI DR2, LCDM)")
print(f"  Framework predicts m_i ~ O(10^7) eV. SCALE BRIDGE UNRESOLVED.")
print(f"  (Eigenvalues are O(1) * M_KK; need scale suppression mechanism)")
print()

# ============================================================================
# SECTION 12: COMPARISON WITH STANDARD MSW PARAMETERS
# ============================================================================

print("SECTION 12: Comparison with standard MSW parameters")
print("-" * 60)

# Standard MSW resonance condition:
# Delta_m^2 cos(2*theta) = 2*E*V
# where V = sqrt(2)*G_F*N_e
#
# Solar MSW:
# Delta_m^2_21 = 7.41e-5 eV^2, theta_12 = 33.4 deg
# E ~ 1-10 MeV, rho ~ 100 g/cm^3 (solar core)
# gamma_solar ~ 100 (strongly adiabatic)
#
# Earth MSW (atmospheric):
# |Delta_m^2_32| = 2.507e-3 eV^2, theta_23 ~ 47 deg
# E ~ 1-100 GeV, rho ~ 5.5 g/cm^3 (Earth)
# Parametric resonance in core-mantle structure
#
# Framework analog:
# "V" = coupling V_12 = 0.077 M_KK (fixed, not density-dependent)
# "Delta_E" sweeps from +0.033 to -0.016 during transit
# gamma depends on sweep rate (dtau/dt)

print("Standard MSW parameters (for reference):")
print(f"  Solar: dm2_21 = 7.41e-5 eV^2, theta_12 = 33.4 deg, gamma ~ 100")
print(f"  Atmospheric: |dm2_32| = 2.507e-3 eV^2, theta_23 ~ 47 deg")
print()
print("Framework analog:")
print(f"  V(B1,B2) = {V_12} M_KK (geometric coupling, not matter)")
print(f"  Gap sweep: {gap_12[0]:.6f} to {gap_12[-1]:.6f} M_KK")
print(f"  Sweep rate: dtau/dt = {dtau_dt:.2f} M_KK")
if len(crossings_12) > 0:
    print(f"  gamma_LZ = {results_crossings[0]['gamma_LZ']:.6f}")
print()

# ============================================================================
# SECTION 13: PLOT
# ============================================================================

print("SECTION 13: Generating plots")
print("-" * 60)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle('S52 MSW-TRANSIT-52: Internal MSW During Modulus Transit', fontsize=14, fontweight='bold')

# Panel 1: Eigenvalue evolution
ax = axes[0, 0]
ax.plot(tau_fine, E_B1_fine, 'b-', linewidth=2, label='B1 (singlet)')
ax.plot(tau_fine, E_B2_fine, 'r-', linewidth=2, label='B2 (fundamental)')
ax.plot(tau_fine, E_B3_fine, 'g-', linewidth=2, label='B3 (adjoint)')
ax.plot(tau_fine, E_G1_fine, 'purple', linewidth=1, linestyle='--', label='G1 (2,0)+(0,2)')
# Mark crossings
for tc in crossings_12:
    ax.axvline(float(tc), color='orange', linestyle=':', alpha=0.7)
    ax.annotate(f'B1=B2\n$\\tau$={float(tc):.3f}', xy=(float(tc), float(cs_B1(float(tc)))),
                fontsize=8, ha='center', va='bottom', color='orange')
# Mark fold
ax.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$E_i(\tau)$ [$M_{KK}$]')
ax.set_title('Sector eigenvalue evolution')
ax.legend(fontsize=8)
ax.set_xlim(0, 0.20)
ax.set_ylim(0.80, 0.98)

# Panel 2: Gap evolution
ax = axes[0, 1]
ax.plot(tau_fine, gap_12, 'b-', linewidth=2, label='$E_{B1} - E_{B2}$')
ax.plot(tau_fine, gap_23, 'g-', linewidth=2, label='$E_{B2} - E_{B3}$')
ax.axhline(0, color='k', linestyle='-', linewidth=0.5)
ax.axhline(2*V_12, color='orange', linestyle='--', alpha=0.5, label=f'$2V_{{12}}$ = {2*V_12:.3f}')
ax.axhline(-2*V_12, color='orange', linestyle='--', alpha=0.5)
for tc in crossings_12:
    ax.axvline(float(tc), color='orange', linestyle=':', alpha=0.7)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$\Delta E$ [$M_{KK}$]')
ax.set_title('Eigenvalue gaps')
ax.legend(fontsize=8)
ax.set_xlim(0, 0.20)

# Panel 3: Effective mixing angle
ax = axes[0, 2]
ax.plot(tau_fine, np.degrees(theta_m_fine), 'r-', linewidth=2)
ax.axhline(45, color='gray', linestyle='--', alpha=0.5, label=r'$\theta_m = 45°$ (maximal)')
for tc in crossings_12:
    ax.axvline(float(tc), color='orange', linestyle=':', alpha=0.7)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$\theta_m(\tau)$ [degrees]')
ax.set_title('Effective B1-B2 mixing angle')
ax.legend(fontsize=8)
ax.set_xlim(0, 0.20)
ax.set_ylim(-90, 90)

# Panel 4: sin^2(2*theta_m)
ax = axes[1, 0]
ax.plot(tau_fine, sin2_2theta_m, 'm-', linewidth=2)
ax.axhline(1.0, color='gray', linestyle='--', alpha=0.5, label='Maximal mixing')
for tc in crossings_12:
    ax.axvline(float(tc), color='orange', linestyle=':', alpha=0.7)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$\sin^2(2\theta_m)$')
ax.set_title(r'$\sin^2(2\theta_m)$ evolution')
ax.legend(fontsize=8)
ax.set_xlim(0, 0.20)
ax.set_ylim(0, 1.05)

# Panel 5: R ratio evolution
ax = axes[1, 1]
R_clipped = np.where(np.isnan(R_fine) | (np.abs(R_fine) > 200), np.nan, R_fine)
ax.plot(tau_fine, R_clipped, 'k-', linewidth=2)
ax.axhline(33.8, color='red', linestyle='--', label=r'NuFit target $R = 33.8$')
ax.axhline(0, color='gray', linestyle='-', linewidth=0.5)
for tc in crossings_12:
    ax.axvline(float(tc), color='orange', linestyle=':', alpha=0.7, label=f'B1-B2 crossing')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$R = \Delta m^2_{31}/\Delta m^2_{21}$')
ax.set_title(r'Mass hierarchy ratio $R(\tau)$')
ax.legend(fontsize=8)
ax.set_xlim(0, 0.20)
ax.set_ylim(-50, 50)

# Panel 6: Mass ordering diagram
ax = axes[1, 2]
# Show the 3 eigenvalues as shaded bands
ax.fill_between(tau_fine, E_B1_fine, E_B2_fine, alpha=0.3, color='blue', label=r'$\Delta_{12}$')
ax.fill_between(tau_fine, E_B2_fine, E_B3_fine, alpha=0.3, color='green', label=r'$\Delta_{23}$')
ax.plot(tau_fine, E_B1_fine, 'b-', linewidth=2)
ax.plot(tau_fine, E_B2_fine, 'r-', linewidth=2)
ax.plot(tau_fine, E_B3_fine, 'g-', linewidth=2)
for tc in crossings_12:
    ax.axvline(float(tc), color='orange', linewidth=2, linestyle='-', alpha=0.8, label='B1-B2 crossing')
ax.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5, label=r'$\tau_{fold}$')
ax.annotate('INVERTED\n(B2 < B1)', xy=(0.03, 0.86), fontsize=10, color='red',
            fontweight='bold', ha='center')
ax.annotate('NORMAL\n(B1 < B2)', xy=(0.16, 0.82), fontsize=10, color='blue',
            fontweight='bold', ha='center')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$E_i(\tau)$ [$M_{KK}$]')
ax.set_title('Mass ordering transition during transit')
ax.legend(fontsize=7, loc='upper right')
ax.set_xlim(0, 0.20)
ax.set_ylim(0.81, 0.90)

plt.tight_layout()
outpng = os.path.join(os.path.dirname(os.path.abspath(__file__)), 's52_msw_transit.png')
plt.savefig(outpng, dpi=150, bbox_inches='tight')
print(f"Saved: {outpng}")
print()

# ============================================================================
# SECTION 14: SAVE DATA
# ============================================================================

print("SECTION 14: Saving results")
print("-" * 60)

outnpz = os.path.join(os.path.dirname(os.path.abspath(__file__)), 's52_msw_transit.npz')
np.savez(outnpz,
    # Grid
    tau_fine=tau_fine,
    N_tau=N_tau,

    # Eigenvalue evolution
    E_B1_fine=E_B1_fine,
    E_B2_fine=E_B2_fine,
    E_B3_fine=E_B3_fine,
    E_G1_fine=E_G1_fine,

    # Gaps
    gap_12=gap_12,
    gap_23=gap_23,
    gap_13=gap_13,

    # Mass-squared differences
    dm2_21=dm2_21_fine,
    dm2_31=dm2_31_fine,
    dm2_32=dm2_32_fine,
    R_fine=R_fine,

    # Mixing angles
    theta_m=theta_m_fine,
    sin2_2theta_m=sin2_2theta_m,

    # Crossings
    crossings_12=np.array(crossings_12),
    crossings_13=np.array(crossings_13),
    crossings_23=np.array(crossings_23),

    # LZ parameters
    V_12=V_12,
    V_23=V_23,
    V_13=V_13,
    dtau_dt=dtau_dt,

    # Values at fold
    R_fold=R_fold,
    E1_fold=E1,
    E2_fold=E2,
    E3_fold=E3,
    dm2_21_fold=dm2_21,
    dm2_31_fold=dm2_31,
    dm2_32_fold=dm2_32,
    theta_m_fold=theta_m_fold,
)
print(f"Saved: {outnpz}")
print()

# ============================================================================
# SECTION 15: SUMMARY
# ============================================================================

elapsed = time.time() - t_start

print("=" * 72)
print("MSW-TRANSIT-52: SUMMARY")
print("=" * 72)
print()
print("1. LEVEL CROSSING DETECTED")
print(f"   B1-B2 crossing at tau = {crossings_12[0]:.6f}" if crossings_12 else "   No B1-B2 crossing")
print(f"   At tau=0: B2 < B1 (inverted ordering)")
print(f"   At tau=0.19: B1 < B2 < B3 (normal ordering)")
print(f"   Transit CREATES the normal mass hierarchy")
print()
print("2. LANDAU-ZENER ADIABATICITY")
if results_crossings:
    rc = results_crossings[0]
    print(f"   gamma_LZ = {rc['gamma_LZ']:.6f}")
    print(f"   V(B1,B2) = {V_12} M_KK (avoided crossing gap = {2*V_12:.4f})")
    print(f"   Sweep rate dtau/dt = {dtau_dt:.1f} M_KK")
    if rc['gamma_LZ'] > 1:
        print(f"   VERDICT: ADIABATIC — states follow curved levels")
    elif rc['gamma_LZ'] < 0.01:
        print(f"   VERDICT: NON-ADIABATIC — states jump through")
    else:
        print(f"   VERDICT: INTERMEDIATE — partial conversion")
print()
print("3. MASS HIERARCHY RATIO R")
print(f"   R at fold = {R_fold:.4f}")
print(f"   NuFit-6.0 target: 33.8")
print(f"   MSW transit does NOT modify R (eigenvalues are properties of D_K)")
print()
print("4. MIXING ANGLES")
print(f"   theta_m at fold = {np.degrees(theta_m_fold):.2f} deg")
print(f"   sin^2(theta_m) at fold = {np.sin(theta_m_fold)**2:.6f}")
print(f"   V(B1,B3) = 0 EXACTLY: B1-B3 mixing impossible (NNI)")
print(f"   B2 isolated (block-diagonal, S52 OFFJENSEN): no B2 mixing")
print()
print("5. STRUCTURAL RESULTS")
print(f"   (a) Normal ordering is a DYNAMICAL consequence of the transit")
print(f"       It is NOT the initial condition — it is created by the B1-B2 crossing")
print(f"   (b) The B1-B2 crossing at tau~{crossings_12[0]:.3f} is the geometric analog" if crossings_12 else "")
print(f"       of the MSW resonance in solar neutrinos")
print(f"   (c) R is unaffected by transit dynamics (operator property, not state)")
print(f"   (d) The transit generates an effective B1-B2 mixing from the Landau-Zener")
print(f"       transition, but V(B1,B3)=0 prevents full 3x3 PMNS")
print()
print("6. GATE VERDICT: MSW-TRANSIT-52 = INFO")
print(f"   MSW does NOT modify R = {R_fold:.4f}")
print(f"   Transit dynamics do not fix the R shortfall vs target 33.8")
print(f"   Normal ordering is structurally robust (created during transit)")
print(f"   New finding: ordering INVERTS at early tau, then flips to normal")
print()
print(f"Elapsed: {elapsed:.2f} s")
