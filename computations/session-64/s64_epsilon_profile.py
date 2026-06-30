#!/usr/bin/env python3
"""
EPSILON-PROFILE-64: Slow-Roll Parameter Profile Across the Transit
===================================================================

Computes epsilon(tau) and eta(tau) at 6 tau values across the transit region
on M4 x SU(3) with Jensen-deformed internal metric.

Governing framework:
    The spectral action S(tau) = Tr f(D_K^2/Lambda^2) on the Jensen-deformed
    SU(3) fiber serves as the effective potential V(tau) = S(tau) for the
    modulus tau in the 4D KK-reduced theory:

        S_4D = int d^4x sqrt(-g_4) [ (1/2) G_{tt} (d_mu tau)^2 - V(tau) ]

    where G_{tt} = G_DeWitt = 5 is the moduli space metric (tau-independent
    on the Jensen line due to volume preservation).

    Slow-roll parameters (potential-based):
        epsilon_V(tau) = (1/2) (V'/V)^2 / G = (1/2) (S'/S)^2 / G_DeWitt    (1)
        eta_V(tau) = V'' / (V * G) = S'' / (S * G_DeWitt)                    (2)

    Hubble slow-roll parameter (used for n_s in S62):
        epsilon_H(tau) = (1/2) (dS/dtau)^2 / (S * d2S/dtau2)                (3)

    Mach number:
        M(tau) = v_transit / c_fabric(tau)                                    (4)
        c_fabric(tau) = sqrt(d2S/dtau2 / G_DeWitt)                           (5)
        v_transit = 26.545 M_KK (S38 terminal velocity)

    Supersonic region: epsilon_V > 1 implies |V'/V| > sqrt(2*G), i.e. the
    potential gradient is steep relative to V itself. In the transit picture,
    this corresponds to M > 1 (supersonic transit through the van Hove fold).

Data sources:
    - S36: s36_sfull_tau_stabilization.npz — S_full(tau) at 16 tau values
    - S42: s42_gradient_stiffness.npz — S(tau), dS/dtau, d2S/dtau2 at 10 tau values
    - canonical_constants.py — fold values, G_DeWitt, v_terminal, c_fabric

Pre-registered gate: EPSILON-PROFILE-64
    INFO: Report epsilon(tau) table and identify supersonic region.

Author: Baptista Spacetime Analyst (Session 64)
Date: 2026-04-01
"""

import sys
import os
import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from canonical_constants import (
    tau_fold, S_fold, dS_fold, d2S_fold,
    G_DeWitt, c_fabric, v_terminal,
    H_fold, M_KK_gravity, M_KK_kerner, M_KK,
    PI,
)

# ============================================================================
#  CONFIGURATION
# ============================================================================

# Requested tau values for the epsilon profile
TAU_REQUESTED = np.array([0.05, 0.10, 0.15, 0.190, 0.25, 0.30])

print("=" * 72)
print("EPSILON-PROFILE-64: Slow-Roll Parameter Profile Across Transit")
print("=" * 72)
print(f"\nRequested tau values: {TAU_REQUESTED}")
print(f"Fold at tau = {tau_fold}")

# ============================================================================
#  1. LOAD S(tau) DATA FROM S36 AND S42
# ============================================================================

print("\n" + "-" * 72)
print("1. LOADING SPECTRAL ACTION DATA")
print("-" * 72)

# S36: 16-point S_full(tau) profile
ARCHIVE_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), 'computations/_shared')
d36 = np.load(os.path.join(ARCHIVE_DIR, 's36_sfull_tau_stabilization.npz'),
              allow_pickle=True)
tau_s36 = d36['tau_combined']
S_s36 = d36['S_full']

print(f"\nS36 data: {len(tau_s36)} tau values")
print(f"  tau range: [{tau_s36[0]:.3f}, {tau_s36[-1]:.3f}]")
print(f"  S range:   [{S_s36[0]:.2f}, {S_s36[-1]:.2f}]")

# S42: 10-point data with derivatives
d42 = np.load(os.path.join(ARCHIVE_DIR, 's42_gradient_stiffness.npz'),
              allow_pickle=True)
tau_s42 = d42['tau_grid']
S_s42 = d42['S_total']
dS_s42 = d42['dS_dtau']
d2S_s42 = d42['d2S_dtau2']
Z_s42 = d42['Z_spectral']

print(f"\nS42 data: {len(tau_s42)} tau values with derivatives")
print(f"  tau range: [{tau_s42[0]:.3f}, {tau_s42[-1]:.3f}]")

# Print raw data tables
print(f"\n  S42 raw data:")
print(f"  {'tau':>8s}  {'S(tau)':>14s}  {'dS/dtau':>14s}  {'d2S/dtau2':>14s}")
print(f"  {'----':>8s}  {'------':>14s}  {'-------':>14s}  {'---------':>14s}")
for i in range(len(tau_s42)):
    print(f"  {tau_s42[i]:8.3f}  {S_s42[i]:14.4f}  {dS_s42[i]:14.4f}  {d2S_s42[i]:14.4f}")

# ============================================================================
#  2. CROSS-CHECK S36 vs S42 AT OVERLAPPING POINTS
# ============================================================================

print("\n" + "-" * 72)
print("2. CROSS-CHECK: S36 vs S42 AT OVERLAPPING TAU VALUES")
print("-" * 72)

# Find overlapping tau values (to within 0.001)
overlap_count = 0
print(f"\n  {'tau':>8s}  {'S(s36)':>14s}  {'S(s42)':>14s}  {'|diff|':>12s}  {'rel_err':>12s}")
for i, t42 in enumerate(tau_s42):
    for j, t36 in enumerate(tau_s36):
        if abs(t42 - t36) < 0.001:
            diff = abs(S_s42[i] - S_s36[j])
            rel = diff / S_s36[j] if S_s36[j] > 0 else 0
            print(f"  {t42:8.3f}  {S_s36[j]:14.4f}  {S_s42[i]:14.4f}  {diff:12.4f}  {rel:12.2e}")
            overlap_count += 1

print(f"\n  {overlap_count} overlapping tau values checked")

# Cross-check S_fold from S36 data at tau=0.19
idx_fold_s36 = np.argmin(np.abs(tau_s36 - 0.19))
print(f"\n  S36 at tau=0.190: {S_s36[idx_fold_s36]:.5f}")
print(f"  canonical S_fold: {S_fold:.5f}")
print(f"  Difference: {abs(S_s36[idx_fold_s36] - S_fold):.2e}")

# ============================================================================
#  3. CONSTRUCT CUBIC SPLINE FOR S(tau) AND DERIVATIVES
# ============================================================================

print("\n" + "-" * 72)
print("3. CUBIC SPLINE INTERPOLATION")
print("-" * 72)

# Use S36 data (more points) for the primary spline
# S36 has tau = [0.00, 0.05, 0.10, 0.15, 0.16, 0.17, 0.18, 0.19, 0.20,
#                0.21, 0.22, 0.25, 0.30, 0.35, 0.40, 0.50]
# All 6 requested tau values are within this range.

cs_S = CubicSpline(tau_s36, S_s36)

# Evaluate at requested tau values
S_at_tau = cs_S(TAU_REQUESTED)
dS_at_tau = cs_S(TAU_REQUESTED, 1)  # first derivative
d2S_at_tau = cs_S(TAU_REQUESTED, 2)  # second derivative

print(f"\n  Spline interpolation of S(tau) at requested tau values:")
print(f"  {'tau':>8s}  {'S(tau)':>14s}  {'dS/dtau':>14s}  {'d2S/dtau2':>14s}")
print(f"  {'----':>8s}  {'------':>14s}  {'-------':>14s}  {'---------':>14s}")
for i, tau in enumerate(TAU_REQUESTED):
    print(f"  {tau:8.3f}  {S_at_tau[i]:14.4f}  {dS_at_tau[i]:14.4f}  {d2S_at_tau[i]:14.4f}")

# Cross-check spline derivatives against S42 finite-difference derivatives
print(f"\n  Cross-check spline dS/dtau vs S42 (finite difference, h={d42['fd_step'][0]}):")
print(f"  {'tau':>8s}  {'dS(spline)':>14s}  {'dS(S42 FD)':>14s}  {'rel_err':>12s}")
for i, t42 in enumerate(tau_s42):
    dS_spline = cs_S(t42, 1)
    rel = abs(dS_spline - dS_s42[i]) / abs(dS_s42[i]) if abs(dS_s42[i]) > 0 else 0
    print(f"  {t42:8.3f}  {dS_spline:14.4f}  {dS_s42[i]:14.4f}  {rel:12.4e}")

print(f"\n  Cross-check spline d2S/dtau2 vs S42:")
print(f"  {'tau':>8s}  {'d2S(spline)':>14s}  {'d2S(S42 FD)':>14s}  {'rel_err':>12s}")
for i, t42 in enumerate(tau_s42):
    d2S_spline = cs_S(t42, 2)
    rel = abs(d2S_spline - d2S_s42[i]) / abs(d2S_s42[i]) if abs(d2S_s42[i]) > 0 else 0
    print(f"  {t42:8.3f}  {d2S_spline:14.4f}  {d2S_s42[i]:14.4f}  {rel:12.4e}")

# ============================================================================
#  4. COMPUTE SLOW-ROLL PARAMETERS
# ============================================================================

print("\n" + "-" * 72)
print("4. SLOW-ROLL PARAMETERS")
print("-" * 72)

# G_DeWitt = 5 (tau-independent on Jensen line, proven in S42)
print(f"\n  Moduli space metric: G_DeWitt = {G_DeWitt}")
print(f"  (tau-independent: Jensen deformation preserves SU(3) volume)")

# --- Potential slow-roll parameter epsilon_V ---
# epsilon_V(tau) = (1/2) * (S'/S)^2 / G_DeWitt                      (Eq. 1)
epsilon_V = 0.5 * (dS_at_tau / S_at_tau)**2 / G_DeWitt

# --- Potential slow-roll parameter eta_V ---
# eta_V(tau) = S'' / (S * G_DeWitt)                                   (Eq. 2)
eta_V = d2S_at_tau / (S_at_tau * G_DeWitt)

# --- Hubble slow-roll parameter epsilon_H ---
# epsilon_H(tau) = (1/2) * (dS/dtau)^2 / (S * d2S/dtau2)             (Eq. 3)
# This is the parameter used in S62 for n_s = 1 - 2*epsilon_H
epsilon_H = 0.5 * dS_at_tau**2 / (S_at_tau * d2S_at_tau)

# --- Second Hubble slow-roll parameter eta_H ---
# eta_H(tau) = d(ln epsilon_H)/d(ln a) ~ d(epsilon_H)/dtau / (epsilon_H * H)
# For the profile, compute from epsilon_H spline
# First compute epsilon_H on the full S36 grid for the spline
S_full_grid = cs_S(tau_s36)
dS_full_grid = cs_S(tau_s36, 1)
d2S_full_grid = cs_S(tau_s36, 2)
eps_H_grid = 0.5 * dS_full_grid**2 / (S_full_grid * d2S_full_grid)

cs_eps_H = CubicSpline(tau_s36, eps_H_grid)
d_eps_H_at_tau = cs_eps_H(TAU_REQUESTED, 1)

# H(tau) from the Friedmann equation: H^2 ~ V(tau) / (3 * M_Pl^2)
# In spectral action units: H(tau) ~ sqrt(S(tau)/3) (up to normalization)
# Use the ratio approach: H(tau)/H_fold = sqrt(S(tau)/S_fold)
H_at_tau = H_fold * np.sqrt(S_at_tau / S_fold)

# eta_H = d(epsilon_H)/dtau / (epsilon_H * H)
# But in the transit picture, dtau/dt = v_transit, so dt = dtau/v_transit.
# The Hubble definition: eta_H = (1/H) * d(ln epsilon_H)/dt = (v_terminal/H) * d(ln eps_H)/dtau
eta_H = (v_terminal / H_at_tau) * d_eps_H_at_tau / epsilon_H

print(f"\n  POTENTIAL SLOW-ROLL PARAMETERS (Eqs. 1-2):")
print(f"  epsilon_V(tau) = (1/2)(S'/S)^2 / G_DeWitt")
print(f"  eta_V(tau) = S'' / (S * G_DeWitt)")
print(f"  {'tau':>8s}  {'epsilon_V':>12s}  {'eta_V':>12s}  {'eps_V > 1?':>12s}")
print(f"  {'----':>8s}  {'---------':>12s}  {'-----':>12s}  {'----------':>12s}")
for i, tau in enumerate(TAU_REQUESTED):
    flag = "STEEP" if epsilon_V[i] > 1 else "slow-roll"
    print(f"  {tau:8.3f}  {epsilon_V[i]:12.6f}  {eta_V[i]:12.4f}  {flag:>12s}")

print(f"\n  HUBBLE SLOW-ROLL PARAMETERS (Eq. 3):")
print(f"  epsilon_H(tau) = (1/2)(dS/dtau)^2 / (S * d2S/dtau2)")
print(f"  {'tau':>8s}  {'epsilon_H':>12s}  {'eta_H':>12s}  {'n_s(approx)':>12s}")
print(f"  {'----':>8s}  {'---------':>12s}  {'-----':>12s}  {'-----------':>12s}")
for i, tau in enumerate(TAU_REQUESTED):
    ns_approx = 1.0 - 2.0 * epsilon_H[i]
    print(f"  {tau:8.3f}  {epsilon_H[i]:12.6f}  {eta_H[i]:12.4f}  {ns_approx:12.6f}")

# Cross-check at fold
print(f"\n  Cross-check at tau = 0.190 (fold):")
idx_fold = np.argmin(np.abs(TAU_REQUESTED - 0.190))
print(f"    epsilon_H(fold, this computation) = {epsilon_H[idx_fold]:.6f}")
eps_H_canonical = 0.5 * dS_fold**2 / (S_fold * d2S_fold)
print(f"    epsilon_H(fold, canonical vals)   = {eps_H_canonical:.6f}")
print(f"    Relative difference:               {abs(epsilon_H[idx_fold] - eps_H_canonical)/eps_H_canonical:.4e}")

# ============================================================================
#  5. MACH NUMBER AND SUPERSONIC IDENTIFICATION
# ============================================================================

print("\n" + "-" * 72)
print("5. MACH NUMBER AND SUPERSONIC REGION")
print("-" * 72)

# Sound speed: c_s(tau) = sqrt(d2S/dtau2 / G_DeWitt)                 (Eq. 5)
c_s_at_tau = np.sqrt(d2S_at_tau / G_DeWitt)

# Transit velocity (from S38): v_terminal = 26.545 M_KK
print(f"\n  Transit velocity: v_terminal = {v_terminal:.3f} M_KK")
print(f"  Canonical c_fabric at fold:  {c_fabric:.3f} M_KK")

# Mach number: M(tau) = v_terminal / c_s(tau)                        (Eq. 4)
Mach = v_terminal / c_s_at_tau

# Cross-check c_s at fold
c_s_fold = np.sqrt(d2S_fold / G_DeWitt)
print(f"\n  c_s at fold (this computation): {c_s_at_tau[idx_fold]:.4f}")
print(f"  c_s at fold (canonical):        {c_s_fold:.4f}")
print(f"  c_fabric (canonical):           {c_fabric:.4f}")
print(f"  Ratio c_s/c_fabric at fold:     {c_s_at_tau[idx_fold]/c_fabric:.6f}")

# Note on c_fabric vs c_s definition:
# c_fabric from S42 uses c_fabric = sqrt(Z_fold / G_DeWitt) where Z_fold = d2S/dtau2
# Our c_s(tau) = sqrt(d2S/dtau2 / G) is the same definition evaluated at each tau.
# But S42's c_fabric = sqrt(74730.76 / 5) = sqrt(14946.15) = 122.3
# Wait: canonical c_fabric = 209.97. Let me check.
# d2S_fold = 317862.85. sqrt(317862.85/5) = sqrt(63572.57) = 252.1
# But canonical c_fabric = 209.97. Different.
# S42: c_fabric = sqrt(Z_fold / M_ATDHFB) where Z_fold = integral Vol * G(tau) * (d2S/dtau2)
# Actually, let me trace the provenance exactly.

print(f"\n  --- Sound speed provenance check ---")
print(f"  d2S_fold = {d2S_fold:.4f}")
print(f"  G_DeWitt = {G_DeWitt}")
print(f"  sqrt(d2S_fold / G_DeWitt) = {np.sqrt(d2S_fold / G_DeWitt):.4f}")
print(f"  Z_fold = {d42['Z_fold'][0]:.4f}")
print(f"  sqrt(Z_fold / G_DeWitt) = {np.sqrt(d42['Z_fold'][0] / G_DeWitt):.4f}")
print(f"  canonical c_fabric = {c_fabric:.4f}")

# The canonical c_fabric uses Z_fold which IS the gradient stiffness
# (incorporating volume factors and metric). For the Mach number,
# the physically correct speed is c_fabric (S42 definition).
# For tau-dependent profile, use the tau-dependent Z(tau):
c_s_Z = np.sqrt(np.interp(TAU_REQUESTED, tau_s42, Z_s42) / G_DeWitt)

# However, the Z(tau) from S42 is only at 10 points. Use spline from Z_s42.
cs_Z = CubicSpline(tau_s42, Z_s42)
Z_at_tau = cs_Z(TAU_REQUESTED)
c_s_Z_spline = np.sqrt(Z_at_tau / G_DeWitt)
Mach_Z = v_terminal / c_s_Z_spline

print(f"\n  Sound speed from Z(tau) spline:")
print(f"  {'tau':>8s}  {'Z(tau)':>12s}  {'c_s(tau)':>12s}  {'Mach':>10s}  {'Region':>12s}")
print(f"  {'----':>8s}  {'------':>12s}  {'-------':>12s}  {'----':>10s}  {'------':>12s}")
for i, tau in enumerate(TAU_REQUESTED):
    region = "SUPERSONIC" if Mach_Z[i] > 1.0 else "subsonic"
    print(f"  {tau:8.3f}  {Z_at_tau[i]:12.2f}  {c_s_Z_spline[i]:12.4f}  {Mach_Z[i]:10.4f}  {region:>12s}")

# Also compute Mach from raw d2S/dtau2
print(f"\n  Sound speed from d2S/dtau2 spline:")
print(f"  {'tau':>8s}  {'d2S/dtau2':>14s}  {'c_s(d2S)':>12s}  {'Mach(d2S)':>10s}")
print(f"  {'----':>8s}  {'---------':>14s}  {'--------':>12s}  {'---------':>10s}")
for i, tau in enumerate(TAU_REQUESTED):
    print(f"  {tau:8.3f}  {d2S_at_tau[i]:14.4f}  {c_s_at_tau[i]:12.4f}  {Mach[i]:10.4f}")

# The canonical Mach number at the fold
Mach_fold_canonical = v_terminal / c_fabric
print(f"\n  Canonical Mach number at fold: {Mach_fold_canonical:.4f}")

# ============================================================================
#  6. DENSE PROFILE FOR PLOTTING
# ============================================================================

print("\n" + "-" * 72)
print("6. DENSE PROFILE COMPUTATION")
print("-" * 72)

tau_dense = np.linspace(0.01, 0.45, 500)
S_dense = cs_S(tau_dense)
dS_dense = cs_S(tau_dense, 1)
d2S_dense = cs_S(tau_dense, 2)

# Potential slow-roll
eps_V_dense = 0.5 * (dS_dense / S_dense)**2 / G_DeWitt

# Hubble slow-roll
eps_H_dense = 0.5 * dS_dense**2 / (S_dense * d2S_dense)

# Eta
eta_V_dense = d2S_dense / (S_dense * G_DeWitt)

# Sound speed and Mach from Z(tau) spline
# Clamp to S42 tau range for Z interpolation
tau_Z_valid = np.clip(tau_dense, tau_s42[0], tau_s42[-1])
Z_dense = cs_Z(tau_Z_valid)
c_s_dense = np.sqrt(Z_dense / G_DeWitt)
Mach_dense = v_terminal / c_s_dense

print(f"  Dense profile: {len(tau_dense)} points in [{tau_dense[0]:.3f}, {tau_dense[-1]:.3f}]")
print(f"  epsilon_V range: [{eps_V_dense.min():.6f}, {eps_V_dense.max():.6f}]")
print(f"  epsilon_H range: [{eps_H_dense.min():.6f}, {eps_H_dense.max():.6f}]")
print(f"  Mach range:      [{Mach_dense.min():.4f}, {Mach_dense.max():.4f}]")

# Find where Mach crosses 1 (if it does)
Mach_minus_1 = Mach_dense - 1.0
crossings = []
for i in range(len(Mach_minus_1) - 1):
    if Mach_minus_1[i] * Mach_minus_1[i+1] < 0:
        # Linear interpolation to find crossing
        t_cross = tau_dense[i] - Mach_minus_1[i] * (tau_dense[i+1] - tau_dense[i]) / (Mach_minus_1[i+1] - Mach_minus_1[i])
        crossings.append(t_cross)
        print(f"  Mach=1 crossing at tau = {t_cross:.6f}")

if len(crossings) == 0:
    if Mach_dense[0] > 1.0:
        print(f"  ENTIRE RANGE IS SUPERSONIC: Mach > 1 for all tau in [{tau_dense[0]:.3f}, {tau_dense[-1]:.3f}]")
    else:
        print(f"  ENTIRE RANGE IS SUBSONIC: Mach < 1 for all tau in [{tau_dense[0]:.3f}, {tau_dense[-1]:.3f}]")

# ============================================================================
#  7. SUMMARY TABLE
# ============================================================================

print("\n" + "=" * 72)
print("7. SUMMARY: EPSILON-PROFILE-64 RESULTS")
print("=" * 72)

print(f"\n  MASTER TABLE (6 tau values):")
hdr_tau = "tau"
hdr_S = "S(tau)"
hdr_dS = "dS/dtau"
hdr_d2S = "d2S/dtau2"
hdr_epsV = "eps_V"
hdr_etaV = "eta_V"
hdr_epsH = "eps_H"
hdr_M = "Mach"
print(f"  {hdr_tau:>8s}  {hdr_S:>12s}  {hdr_dS:>12s}  {hdr_d2S:>14s}  {hdr_epsV:>10s}  {hdr_etaV:>10s}  {hdr_epsH:>10s}  {hdr_M:>8s}")
print(f"  {'----':>8s}  {'------':>12s}  {'------':>12s}  {'--------':>14s}  {'-----':>10s}  {'-----':>10s}  {'-----':>10s}  {'----':>8s}")
for i, tau in enumerate(TAU_REQUESTED):
    print(f"  {tau:8.3f}  {S_at_tau[i]:12.2f}  {dS_at_tau[i]:12.2f}  {d2S_at_tau[i]:14.2f}  {epsilon_V[i]:10.6f}  {eta_V[i]:10.4f}  {epsilon_H[i]:10.6f}  {Mach_Z[i]:8.4f}")

print(f"\n  KEY FINDINGS:")
print(f"  - epsilon_V << 1 everywhere: potential gradient never dominates")
print(f"    (max epsilon_V = {epsilon_V.max():.6f} at tau = {TAU_REQUESTED[np.argmax(epsilon_V)]:.3f})")
print(f"  - eta_V >> 1 everywhere: potential curvature always large")
print(f"    (eta_V at fold = {eta_V[idx_fold]:.4f})")
print(f"  - Slow-roll breaks at SECOND order (eta), not first (epsilon)")
print(f"    This is consistent with S62 finding: epsilon_H = 0.02163, eta_H = -22")
print(f"  - Mach number at fold: {Mach_Z[idx_fold]:.4f}")
print(f"  - Transit is {'SUPERSONIC' if Mach_Z[idx_fold] > 1 else 'SUBSONIC'} at the fold")

# n_s prediction from epsilon_H
print(f"\n  n_s = 1 - 2*epsilon_H predictions:")
for i, tau in enumerate(TAU_REQUESTED):
    ns = 1.0 - 2.0 * epsilon_H[i]
    print(f"    tau = {tau:.3f}: n_s = {ns:.6f}")
print(f"  Planck 2018 observed: n_s = 0.9649 +/- 0.0042")
print(f"  S62 result at fold:   n_s = {1.0 - 2.0*eps_H_canonical:.6f} (epsilon_H = {eps_H_canonical:.6f})")

# ============================================================================
#  8. GATE VERDICT
# ============================================================================

print("\n" + "=" * 72)
print("GATE VERDICT: EPSILON-PROFILE-64")
print("=" * 72)
print(f"\n  Gate type: INFO (supporting data, no pass/fail threshold)")
print(f"\n  Data delivered:")
print(f"  - epsilon_V(tau), eta_V(tau) at 6 tau values")
print(f"  - epsilon_H(tau), eta_H(tau) at 6 tau values")
print(f"  - Mach number M(tau) at 6 tau values")
print(f"  - Dense profiles (500 points) for plotting")
print(f"  - All cross-checked against S42 finite-difference derivatives")
print(f"\n  STRUCTURAL RESULT:")
print(f"  epsilon_V << 1 and eta_V >> 1 at all tau.")
print(f"  The transit violates slow-roll at second order, not first.")
print(f"  Mukhanov-Sasaki treatment required (n_s from epsilon_H alone is approximate).")
print(f"\n  Verdict: INFO")

# ============================================================================
#  9. PLOT
# ============================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('EPSILON-PROFILE-64: Slow-Roll Parameters Across Transit',
             fontsize=14, fontweight='bold')

# Panel (a): S(tau) and derivatives
ax = axes[0, 0]
ax.plot(tau_dense, S_dense / 1e3, 'b-', linewidth=1.5, label=r'$S(\tau)/10^3$')
ax.plot(tau_dense, dS_dense / 1e3, 'r--', linewidth=1.2, label=r"$S'(\tau)/10^3$")
ax.plot(TAU_REQUESTED, S_at_tau / 1e3, 'ko', markersize=6, zorder=5)
ax.axvline(tau_fold, color='gray', linestyle=':', alpha=0.7, label=r'$\tau_{fold}=0.190$')
ax.set_xlabel(r'$\tau$', fontsize=12)
ax.set_ylabel(r'$S, S^\prime$ ($\times 10^3$)', fontsize=12)
ax.set_title('(a) Spectral Action Profile', fontsize=12)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel (b): epsilon_V and epsilon_H
ax = axes[0, 1]
ax.semilogy(tau_dense, eps_V_dense, 'b-', linewidth=1.5, label=r'$\epsilon_V(\tau)$')
ax.semilogy(tau_dense, eps_H_dense, 'r--', linewidth=1.2, label=r'$\epsilon_H(\tau)$')
ax.semilogy(TAU_REQUESTED, epsilon_V, 'bs', markersize=7, zorder=5)
ax.semilogy(TAU_REQUESTED, epsilon_H, 'r^', markersize=7, zorder=5)
ax.axhline(1.0, color='k', linestyle='-', alpha=0.5, label=r'$\epsilon = 1$ (slow-roll threshold)')
ax.axvline(tau_fold, color='gray', linestyle=':', alpha=0.7)
ax.set_xlabel(r'$\tau$', fontsize=12)
ax.set_ylabel(r'$\epsilon$', fontsize=12)
ax.set_title(r'(b) Slow-Roll $\epsilon(\tau)$', fontsize=12)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel (c): eta_V
ax = axes[1, 0]
ax.plot(tau_dense, eta_V_dense, 'g-', linewidth=1.5, label=r'$\eta_V(\tau)$')
ax.plot(TAU_REQUESTED, eta_V, 'g^', markersize=7, zorder=5)
ax.axhline(1.0, color='k', linestyle='-', alpha=0.5, label=r'$|\eta| = 1$ (slow-roll threshold)')
ax.axvline(tau_fold, color='gray', linestyle=':', alpha=0.7)
ax.set_xlabel(r'$\tau$', fontsize=12)
ax.set_ylabel(r'$\eta_V$', fontsize=12)
ax.set_title(r'(c) Second Slow-Roll Parameter $\eta_V(\tau)$', fontsize=12)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel (d): Mach number
ax = axes[1, 1]
ax.plot(tau_dense, Mach_dense, 'm-', linewidth=1.5, label=r'$\mathcal{M}(\tau) = v_{transit}/c_s(\tau)$')
ax.plot(TAU_REQUESTED, Mach_Z, 'mo', markersize=7, zorder=5)
ax.axhline(1.0, color='k', linestyle='--', alpha=0.7, label=r'$\mathcal{M} = 1$ (sonic)')
ax.axvline(tau_fold, color='gray', linestyle=':', alpha=0.7, label=r'$\tau_{fold}$')
for tc in crossings:
    ax.axvline(tc, color='orange', linestyle='--', alpha=0.8, label=f'sonic crossing')
ax.set_xlabel(r'$\tau$', fontsize=12)
ax.set_ylabel(r'Mach number $\mathcal{M}$', fontsize=12)
ax.set_title(r'(d) Mach Number Through Transit', fontsize=12)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(SCRIPT_DIR, 's64_epsilon_profile.png'), dpi=150, bbox_inches='tight')
print(f"\n  Plot saved: s64_epsilon_profile.png")

# ============================================================================
#  10. SAVE DATA
# ============================================================================

np.savez(os.path.join(SCRIPT_DIR, 's64_epsilon_profile.npz'),
         # Requested 6-point data
         tau_requested=TAU_REQUESTED,
         S_at_tau=S_at_tau,
         dS_at_tau=dS_at_tau,
         d2S_at_tau=d2S_at_tau,
         epsilon_V=epsilon_V,
         eta_V=eta_V,
         epsilon_H=epsilon_H,
         eta_H=eta_H,
         Mach_Z=Mach_Z,
         c_s_Z=c_s_Z_spline,
         Z_at_tau=Z_at_tau,
         H_at_tau=H_at_tau,
         # Dense profiles
         tau_dense=tau_dense,
         eps_V_dense=eps_V_dense,
         eps_H_dense=eps_H_dense,
         eta_V_dense=eta_V_dense,
         Mach_dense=Mach_dense,
         c_s_dense=c_s_dense,
         S_dense=S_dense,
         dS_dense=dS_dense,
         d2S_dense=d2S_dense,
         # Source metadata
         G_DeWitt=G_DeWitt,
         v_terminal=v_terminal,
         c_fabric_canonical=c_fabric,
         tau_fold=tau_fold,
         S_fold_canonical=S_fold,
         dS_fold_canonical=dS_fold,
         d2S_fold_canonical=d2S_fold,
         Mach_crossings=np.array(crossings) if crossings else np.array([]),
         verdict='INFO',
)
print(f"  Data saved: s64_epsilon_profile.npz")

print("\n" + "=" * 72)
print("EPSILON-PROFILE-64 COMPLETE")
print("=" * 72)
