#!/usr/bin/env python3
"""
s58_acoustic_metric.py — ACOUSTIC-METRIC-58
Unruh acoustic metric construction on the phononic fabric.

Physics
-------
Unruh (1981) showed that sound propagation in a moving fluid is governed by
an effective Lorentzian metric:

    ds^2 = (rho/c_s)[ -(c_s^2 - v^2) dt^2 - 2v dt dx + dx^2 ]

In the phonon-exflation framework:
  - c_s = c_BA(tau), the Bogoliubov-Anderson sound speed on the CG(24) fabric
  - v = background flow velocity (the rate at which the geometry evolves)
  - rho = effective spectral-weight density
  - tau = the Jensen deformation parameter (internal clock)

Subtlety: H(tau) from S54 is H_tau = (1/a)(da/dtau), the moduli-space
Hubble parameter. The physical flow velocity seen by phonons is NOT H itself
but rather H_tau converted to the phonon's propagation coordinate.

Key question: does T_acoustic match T_GH?

T_GH = H_tau / (2*pi)           — geometric Gibbons-Hawking temperature
T_acoustic = kappa / (2*pi)     — acoustic surface gravity temperature

Three temperature definitions are tested:
  1. Conformal: from the rate of change of the acoustic lapse function
  2. Parker: from the cosmological redshift of the sound speed |d(ln c)/dtau|
  3. Direct surface gravity: from |dc/dtau|

Gate: ACOUSTIC-METRIC-58
  PASS: |T_acoustic/T_GH - 1| < 0.5 at the fold
  INFO: T_acoustic computed but ratio outside range

Author: quantum-acoustics-theorist (rewrite)
Session: S58 W3-1
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    tau_fold, N_cells, PI,
    rho_B2_per_mode, dt_transit
)

# =============================================================================
# 1. LOAD DATA
# =============================================================================
print("=" * 72)
print("ACOUSTIC-METRIC-58: Unruh Acoustic Metric Construction")
print("=" * 72)

d56 = np.load(os.path.join(os.path.dirname(__file__), 's56_ba_spectrum.npz'))
d54 = np.load(os.path.join(os.path.dirname(__file__), 's54_scale_factor.npz'))

tau_50 = d56['tau_values']            # (50,) from 0 to 0.5
c_BA   = d56['c_BA']                  # (50,) BA sound speed [M_KK]
omega_BA = d56['omega_BA']            # (50, 31) BA frequencies [M_KK]
T_GH_s56 = d56['T_GH']               # (50,) Gibbons-Hawking temp [M_KK]

tau_10 = d54['tau']                    # (10,) from 0 to ~0.347
a_10   = d54['a']                      # (10,) scale factor
H_10   = d54['H']                      # (10,) H = (1/a)(da/dtau) [M_KK]

N_tau = len(tau_50)
N_modes = omega_BA.shape[1]
dtau = tau_50[1] - tau_50[0]

print(f"\nInput: {N_tau} tau points, {N_modes} BA modes")
print(f"Scale factor: {len(tau_10)} points, tau in [{tau_10[0]:.3f}, {tau_10[-1]:.3f}]")
print(f"c_BA range: [{c_BA.min():.4f}, {c_BA.max():.4f}] M_KK")
print(f"T_GH range: [{T_GH_s56.min():.6f}, {T_GH_s56.max():.6f}] M_KK")

# =============================================================================
# 2. INTERPOLATE H(tau) AND a(tau) TO 50 POINTS
# =============================================================================
cs_H = CubicSpline(tau_10, H_10, extrapolate=True)
cs_a = CubicSpline(tau_10, a_10, extrapolate=True)

H_50 = cs_H(tau_50)
a_50 = cs_a(tau_50)

# Clip extrapolated H to positive (physical)
H_50 = np.maximum(H_50, 1e-6)

fold_idx = np.argmin(np.abs(tau_50 - tau_fold))
print(f"\nH_tau interpolated: H(0)={H_50[0]:.4f}, H(fold)={H_50[fold_idx]:.4f}, H(0.5)={H_50[-1]:.4f}")
print(f"a interpolated: a(0)={a_50[0]:.4f}, a(fold)={a_50[fold_idx]:.4f}, a(0.5)={a_50[-1]:.4f}")
print(f"Fold index: {fold_idx}, tau_fold = {tau_50[fold_idx]:.4f}")

# =============================================================================
# 3. FLOW VELOCITY
# =============================================================================
# H(tau) = (1/a)(da/dtau) is the Hubble rate in moduli time.
# Since T_GH = H/(2*pi) uses THIS H, the comparison T_acoustic vs T_GH
# must use the SAME time variable tau.
#
# In the Unruh picture: phonons propagate with speed c_BA on the CG graph
# (coordinate x = graph distance). The "flow" is the time evolution of
# the background geometry. In moduli time tau, the flow velocity at each
# point is v = da/dtau / a_local, but this is just H_tau again.
#
# Physical interpretation: as the modulus evolves, the sound speed changes.
# A phonon emitted at tau_1 with frequency omega arrives at tau_2 > tau_1
# with a different frequency because c_BA has changed. The effective
# "flow velocity" for the Unruh construction is the velocity at which
# the background sweeps past the phonon: v_flow = H_tau * L_eff where
# L_eff is the effective length scale of the CG graph.
#
# However, for the (1+1)D acoustic metric in (tau, x) coordinates:
# The time coordinate IS tau, and x is the graph distance.
# The flow velocity in these coordinates is:
#   v = dx_background/dtau   (how fast does a "fluid element" move in x)
#
# On the CG graph, the "fluid" is the phonon bath. The background geometry
# evolves uniformly (all cells change together via the Jensen deformation).
# So v_fluid = 0 in the x-direction — the fluid is AT REST in graph
# coordinates. There is no spatial flow.
#
# This means the Unruh sonic-horizon picture does NOT directly apply.
# Instead, the correct analog is the COSMOLOGICAL particle creation picture
# (Parker 1969): the time-dependent background creates particles via the
# parametric change of the mode frequencies omega_BA(tau).
#
# For a cosmological spacetime ds^2 = -dtau^2 + a(tau)^2 dx^2,
# the acoustic analog is:
#   ds^2_acoustic = -c_BA(tau)^2 dtau^2 + dx^2
#
# This is a FRIEDMANN-LIKE acoustic metric where c_BA plays the role of the
# lapse function (converting coordinate time to proper time for phonons).

# Since the fluid is at rest (v=0), the Unruh metric simplifies to diagonal:
# ds^2 = (rho/c) * [-c^2 dtau^2 + dx^2]
#       = -rho*c dtau^2 + (rho/c) dx^2
#
# But we should also account for the EXPANSION of the background:
# The physical distance on the CG graph scales with a(tau), so:
# ds^2 = -c_BA^2 dtau^2 + a(tau)^2 dx^2   (in natural units)
#
# This is the acoustic FRW metric. The effective "Hubble parameter" for
# phonons is:
#   H_acoustic = (1/a)(da/dtau) = H_tau  (the same!)
#
# So naively T_acoustic = H_tau/(2*pi) = T_GH exactly.
# But this is too simple — it just says the phonons live in the same
# background. The ACOUSTIC Hubble parameter should be defined differently:
# phonons see an effective metric determined by c_BA(tau), not a(tau).
#
# The key insight: for the PHONONIC sector, the effective scale factor
# is NOT a(tau) but rather a_phonon(tau) = a(tau) / c_BA(tau).
# This is because the phonon wavelength lambda ~ a/k, but the phonon
# dispersion omega = c_BA * k means the effective conformal factor
# for the phonon action is a/c_BA.
#
# From the phonon action: S = integral [omega^2 - c_BA^2 k^2] a^d dtau dx^d
# In 1+1D: ds^2_phonon = -(c_BA/a)^2 a^2 dtau^2 + a^2 dx^2
#                       = -c_BA^2 dtau^2 + a^2 dx^2
#
# The acoustic Hubble parameter (from the FRW analog):
#   H_acoustic = d(ln a)/dtau = H_tau (same as geometric!)
#
# BUT: the particle creation depends on the TIME-DEPENDENT MODE FREQUENCY:
#   omega_n(tau) = c_BA(tau) * k_n / a(tau)   (physical frequency)
# The adiabaticity parameter (Zeldovich-Starobinsky):
#   Q = |d(omega)/dtau| / omega^2
#
# When Q << 1: adiabatic (no particle creation)
# When Q ~ 1: significant particle creation
#
# The effective temperature from non-adiabatic particle creation:
#   T_particle_creation ~ omega * Q / (2*pi)
#                       = |d(omega)/dtau| / (2*pi * omega)
#
# For omega = c_BA * k / a:
#   d(ln omega)/dtau = d(ln c_BA)/dtau - d(ln a)/dtau
#                    = d(ln c_BA)/dtau - H_tau
#
# So: T_acoustic = |d(ln c_BA)/dtau - H_tau| / (2*pi)
# And: T_GH = H_tau / (2*pi)
# Ratio: T_acoustic/T_GH = |d(ln c_BA)/dtau / H_tau - 1|
#
# If the sound speed is constant: T_acoustic = T_GH exactly (ratio = 1).
# If the sound speed changes: the ratio deviates from 1 by the relative
# importance of sound-speed evolution vs geometric expansion.

# Compute d(ln c_BA)/dtau using cubic spline for smooth derivatives
cs_c = CubicSpline(tau_50, np.log(np.abs(c_BA) + 1e-30))
dlnc_dtau = cs_c(tau_50, 1)  # d(ln c_BA)/dtau

# Adiabaticity parameter for mode frequency evolution
# Q_omega = |d(ln omega)/dtau| where omega = c_BA * k / a
# d(ln omega)/dtau = d(ln c)/dtau - H_tau
omega_evolution = dlnc_dtau - H_50  # d(ln omega)/dtau
Q_adiabatic = np.abs(omega_evolution)  # dimensionless adiabaticity

print(f"\nMode frequency evolution d(ln omega)/dtau:")
print(f"  d(ln c)/dtau at fold: {dlnc_dtau[fold_idx]:.4f}")
print(f"  H_tau at fold: {H_50[fold_idx]:.4f}")
print(f"  d(ln omega)/dtau at fold: {omega_evolution[fold_idx]:.4f}")
print(f"  |Q| range: [{Q_adiabatic.min():.4f}, {Q_adiabatic.max():.4f}]")

# =============================================================================
# 4. CONSTRUCT ACOUSTIC FRW METRIC
# =============================================================================
# ds^2_acoustic = -c_BA(tau)^2 dtau^2 + a(tau)^2 dx^2
#
# This is the (1+1)D metric for phonon propagation.
# g_tt = -c_BA^2, g_xx = a^2, g_tx = 0 (no flow in graph coordinates)

g_tt = -c_BA**2
g_tx = np.zeros(N_tau)
g_xx = a_50**2

det_g = g_tt * g_xx  # = -c_BA^2 * a^2 (negative: Lorentzian)

print(f"\nAcoustic FRW metric at fold (tau={tau_50[fold_idx]:.4f}):")
print(f"  g_tt = -c_BA^2 = {g_tt[fold_idx]:.6f}")
print(f"  g_xx =  a^2    = {g_xx[fold_idx]:.6f}")
print(f"  det(g) = {det_g[fold_idx]:.6f}")

# Also construct the full Unruh metric WITH conformal factor
# ds^2_Unruh = (rho/c) * [-c^2 dtau^2 + dx^2]  (no flow)
# where rho is the spectral weight density
omega_sum = np.sum(omega_BA, axis=1)
rho_eff = omega_sum / N_cells  # spectral weight per cell [M_KK]

conformal = rho_eff / c_BA
g_tt_unruh = -conformal * c_BA**2  # = -rho * c
g_xx_unruh = conformal * 1.0       # = rho / c

print(f"\nUnruh metric (with conformal factor) at fold:")
print(f"  (rho/c) = {conformal[fold_idx]:.4f}")
print(f"  g_tt_U  = -rho*c = {g_tt_unruh[fold_idx]:.6f}")
print(f"  g_xx_U  = rho/c  = {g_xx_unruh[fold_idx]:.6f}")

# =============================================================================
# 5. RICCI SCALAR OF THE ACOUSTIC FRW METRIC
# =============================================================================
# For ds^2 = -N(tau)^2 dtau^2 + a(tau)^2 dx^2 (diagonal, N = c_BA, a = a(tau)):
#
# In (1+1)D, R is computed from:
#   sqrt(-g) = N * a = c_BA * a
#   R = -(2/(N*a)) * d/dtau[a'*N'/a + N''/N - ... ]
#
# More precisely, for ds^2 = -N^2 dt^2 + a^2 dx^2 in 1+1D:
# The non-zero Christoffel symbols (with ' = d/dtau):
#   Gamma^0_{00} = N'/N
#   Gamma^0_{11} = a*a'/(N^2)  ... wait, let me derive carefully.
#   Gamma^1_{01} = a'/a
#   Gamma^1_{10} = a'/a
#
# Gamma^a_{bc} = (1/2) g^{ad} (g_{db,c} + g_{dc,b} - g_{bc,d})
# g^{00} = -1/N^2, g^{11} = 1/a^2
#
# Gamma^0_{00}: (1/2) g^{00} (g_{00,0} + g_{00,0} - g_{00,0}) = (1/2)(-1/N^2)(- 2N N') = N'/N
# Gamma^0_{11}: (1/2) g^{00} (g_{01,1} + g_{01,1} - g_{11,0}) = (1/2)(-1/N^2)(0 + 0 - 2a a')
#             = a*a'/N^2
# Gamma^1_{01}: (1/2) g^{11} (g_{10,1} + g_{11,0} - g_{01,1}) = (1/2)(1/a^2)(0 + 2a a' - 0)
#             = a'/a
# All other Christoffels vanish.
#
# Riemann tensor R^0_{101}:
# R^0_{101} = d_1 Gamma^0_{01} - d_0 Gamma^0_{11} + Gamma^0_{1e}Gamma^e_{01} - Gamma^0_{0e}Gamma^e_{11}
# Wait, let me use the correct index convention:
# R^rho_{sigma mu nu} = partial_mu Gamma^rho_{nu sigma} - partial_nu Gamma^rho_{mu sigma}
#                      + Gamma^rho_{mu lambda} Gamma^lambda_{nu sigma}
#                      - Gamma^rho_{nu lambda} Gamma^lambda_{mu sigma}
#
# R^0_{101}: rho=0, sigma=1, mu=0, nu=1
# = partial_0 Gamma^0_{11} - partial_1 Gamma^0_{01}
#   + Gamma^0_{0 lambda} Gamma^lambda_{11} - Gamma^0_{1 lambda} Gamma^lambda_{01}
#
# partial_1 = 0 (no x-dependence). So:
# R^0_{101} = d/dtau[Gamma^0_{11}] + Gamma^0_{00}*Gamma^0_{11} + Gamma^0_{01}*Gamma^1_{11}
#            - Gamma^0_{10}*Gamma^0_{01} - Gamma^0_{11}*Gamma^1_{01}
#
# But Gamma^0_{01} = 0 (because g_{00,1} = g_{01,0} = 0... wait)
# Actually Gamma^0_{01} = (1/2) g^{00} (g_{00,1} + g_{01,0} - g_{01,0})
#   g_{00,1} = 0 (no x-dependence), g_{01,0} = 0 (g_{01} = 0)
#   So Gamma^0_{01} = 0. Good.
#
# And Gamma^1_{11} = (1/2) g^{11} (g_{11,1} + g_{11,1} - g_{11,1}) = (1/2)(1/a^2)(0) = 0
#
# So: R^0_{101} = d/dtau[a*a'/N^2] + (N'/N)(a*a'/N^2) + 0 - 0 - (a*a'/N^2)(a'/a)
#              = d/dtau[a a'/N^2] + (N'/N)(a a'/N^2) - (a')^2/N^2
#
# Let me compute d/dtau[a a'/N^2]:
# d/dtau[a a'/N^2] = [(a')^2 + a a'']/N^2 - 2 a a' N'/N^3
#
# So: R^0_{101} = [(a')^2 + a a'']/N^2 - 2 a a' N'/(N^3) + a a' N'/(N^3) - (a')^2/N^2
#              = a a''/N^2 - a a' N'/N^3
#              = (a/N^2)(a'' - a' N'/N)
#
# The Ricci tensor in 2D: R_{00} = R^1_{010}, R_{11} = R^0_{101} * (... lowered)
# Actually, in 2D with our conventions:
# R = g^{00} R_{00} + g^{11} R_{11}
# R_{00} = R^m_{0m0} = R^1_{010} = -R^1_{001}
# R_{11} = R^m_{1m1} = R^0_{101}
#
# R^1_{010}: rho=1, sigma=0, mu=1, nu=0
# = partial_1 Gamma^1_{00} - partial_0 Gamma^1_{10}
#   + Gamma^1_{1 lambda} Gamma^lambda_{00} - Gamma^1_{0 lambda} Gamma^lambda_{10}
# = 0 - d/dtau[a'/a] + (a'/a)(N'/N) - (a'/a)(a'/a) ... wait
# Gamma^1_{1 lambda}: lambda=0 => Gamma^1_{10} = a'/a. lambda=1 => Gamma^1_{11} = 0.
# Gamma^lambda_{00}: lambda=0 => Gamma^0_{00} = N'/N. lambda=1 => Gamma^1_{00} = 0.
#   Wait: Gamma^1_{00} = (1/2) g^{11}(g_{10,0} + g_{10,0} - g_{00,1}) = (1/2)(1/a^2)(0+0-0) = 0.
# Gamma^1_{0 lambda}: lambda=0 => Gamma^1_{00} = 0. lambda=1 => Gamma^1_{01} = a'/a.
# Gamma^lambda_{10}: lambda=0 => Gamma^0_{10} = 0. lambda=1 => Gamma^1_{10} = a'/a.
#
# R^1_{010} = 0 - d/dtau[a'/a] + (a'/a)(N'/N) - (a'/a)(a'/a)
#           = -(a''/a - (a')^2/a^2) + (a'/a)(N'/N) - (a'/a)^2
#           = -a''/a + (a')^2/a^2 + a' N'/(a N) - (a')^2/a^2
#           = -a''/a + a' N'/(a N)
#
# So: R_{00} = R^1_{010} * g_{00}^? No:
# R_{00} = R^1_{010} (this is the correct Ricci tensor component for sigma=0)
#   Actually R_{00} = sum_m R^m_{0m0} = R^0_{000} + R^1_{010}
#   R^0_{000} = 0 (antisymmetry)
#   R_{00} = R^1_{010} = -a''/a + a'N'/(aN)
#
# R_{11} = sum_m R^m_{1m1} = R^0_{101} + R^1_{111}
#   R^1_{111} = 0 (antisymmetry)
#   R_{11} = R^0_{101} = (a/N^2)(a'' - a'N'/N)
#
# R = g^{00} R_{00} + g^{11} R_{11}
#   = (-1/N^2)(-a''/a + a'N'/(aN)) + (1/a^2)(a/N^2)(a'' - a'N'/N)
#   = (1/N^2)(a''/a - a'N'/(aN)) + (1/(aN^2))(a'' - a'N'/N)
#   = (1/N^2)(a''/a) - a'N'/(a N^3) + a''/(aN^2) - a'N'/(aN^3)
#   = 2a''/(aN^2) - 2a'N'/(aN^3)
#   = (2/(aN^2))(a'' - a'N'/N)
#
# With N = c_BA(tau) and a = a(tau):
# R = (2/(a * c_BA^2)) * (a'' - a' * c_BA' / c_BA)

# Compute derivatives using cubic splines
cs_c_BA = CubicSpline(tau_50, c_BA)
cs_a50  = CubicSpline(tau_50, a_50)

a_prime = cs_a50(tau_50, 1)    # da/dtau
a_double_prime = cs_a50(tau_50, 2)  # d^2a/dtau^2
c_prime = cs_c_BA(tau_50, 1)   # dc_BA/dtau

R_acoustic = (2.0 / (a_50 * c_BA**2)) * (a_double_prime - a_prime * c_prime / c_BA)

print(f"\n--- Ricci scalar R_acoustic(tau) ---")
print(f"  R(0)     = {R_acoustic[0]:.6f} M_KK^2")
print(f"  R(fold)  = {R_acoustic[fold_idx]:.6f} M_KK^2")
print(f"  R(0.5)   = {R_acoustic[-1]:.6f} M_KK^2")
print(f"  R range: [{R_acoustic.min():.4f}, {R_acoustic.max():.4f}]")

# Check: For FRW in 1+1D with N=const: R = 2*a''/a * N^{-2}
# With N=1: R = 2*a''/a (should be ~2*H'*a/a + 2*H^2)
# Quick check at tau=0: a''(0)/a(0) ~ H'^2 + H''*tau ~ H(0)^2 ~ 15.6
# R ~ 2*15.6/c^2 ~ 25. Let's see...
print(f"  Sanity: 2*a''/a at tau=0 = {2*a_double_prime[0]/a_50[0]:.4f}")
print(f"          c_BA^2 at tau=0  = {c_BA[0]**2:.4f}")
print(f"          Ratio = R ~ {2*a_double_prime[0]/(a_50[0]*c_BA[0]**2):.4f}")

# =============================================================================
# 6. TEMPERATURES
# =============================================================================
# Three physically motivated temperature definitions:
#
# 1. T_conformal: from the conformal acoustic Hubble parameter
#    The phonon effective scale factor: a_eff = a / c_BA
#    H_eff = d(ln a_eff)/dtau = d(ln a)/dtau - d(ln c_BA)/dtau = H_tau - d(ln c)/dtau
#    T_conformal = |H_eff| / (2*pi)
#
# 2. T_Parker: from the non-adiabatic particle creation rate
#    omega_n(tau) = c_BA(tau) * k_n (physical frequency in graph coordinates)
#    T_Parker = |d(ln omega_n)/dtau| / (2*pi) = |d(ln c_BA)/dtau| / (2*pi)
#    (Note: on a fixed graph, k_n does not evolve. Expansion a(tau) does not
#     affect the graph distance — a(tau) is the 4D scale factor.)
#
# 3. T_geometric: directly from the Ricci scalar
#    In 2D, R determines the curvature completely.
#    T_Ricci = sqrt(|R|) / (4*pi)  (dimensional analysis)
#
# Meanwhile: T_GH = H_tau / (2*pi) with H_tau = (1/a)(da/dtau)

# T_Parker: the sound speed evolution rate
# This is the cleanest definition: it measures how fast the mode
# frequencies change, which directly determines particle creation.
T_Parker = np.abs(dlnc_dtau) / (2.0 * PI)

# T_conformal: from the effective Hubble parameter
# On the CG graph, the physical phonon frequency is omega = c_BA * k.
# The graph is fixed (k doesn't redshift with a(tau)).
# So d(ln omega)/dtau = d(ln c_BA)/dtau = dlnc_dtau.
# T_conformal = |dlnc_dtau - H_50| / (2*pi)
# BUT: phonons on the CG graph don't see the 4D expansion directly.
# Their effective "horizon" comes from the sound speed evolution alone.
# So T_Parker is the right answer, not T_conformal.

T_conformal = np.abs(dlnc_dtau - H_50) / (2.0 * PI)

# T_Ricci: from the curvature
T_Ricci = np.sqrt(np.abs(R_acoustic)) / (4.0 * PI)

# T_GH (from data)
T_GH = T_GH_s56

print(f"\n--- Temperatures at fold (tau={tau_50[fold_idx]:.4f}) ---")
print(f"  T_GH       = {T_GH[fold_idx]:.6f} M_KK  [= H_tau/(2*pi)]")
print(f"  T_Parker   = {T_Parker[fold_idx]:.6f} M_KK  [= |d(ln c)/dtau|/(2*pi)]")
print(f"  T_conformal = {T_conformal[fold_idx]:.6f} M_KK  [= |d(ln c)/dtau - H|/(2*pi)]")
print(f"  T_Ricci    = {T_Ricci[fold_idx]:.6f} M_KK  [= sqrt(|R|)/(4*pi)]")

# =============================================================================
# 7. TEMPERATURE RATIOS
# =============================================================================
ratio_Parker  = T_Parker / T_GH
ratio_conformal = T_conformal / T_GH
ratio_Ricci   = T_Ricci / T_GH

print(f"\n--- Temperature ratios at fold ---")
print(f"  T_Parker/T_GH    = {ratio_Parker[fold_idx]:.6f}")
print(f"  T_conformal/T_GH = {ratio_conformal[fold_idx]:.6f}")
print(f"  T_Ricci/T_GH     = {ratio_Ricci[fold_idx]:.6f}")

# Full table
print(f"\n{'tau':>8s}  {'T_GH':>10s}  {'T_Parker':>10s}  {'T_conf':>10s}  {'T_Ricci':>10s}  "
      f"{'P/GH':>8s}  {'C/GH':>8s}  {'R/GH':>8s}")
print("-" * 90)
for i in range(0, N_tau, 5):
    print(f"{tau_50[i]:8.4f}  {T_GH[i]:10.6f}  {T_Parker[i]:10.6f}  {T_conformal[i]:10.6f}  "
          f"{T_Ricci[i]:10.6f}  {ratio_Parker[i]:8.4f}  {ratio_conformal[i]:8.4f}  {ratio_Ricci[i]:8.4f}")

# =============================================================================
# 8. IDENTITY ANALYSIS
# =============================================================================
# Key structural result: T_Parker/T_GH = |d(ln c_BA)/dtau| / H_tau
# = |d(ln c_BA)/dtau| / |d(ln a)/dtau|
# = |d(ln c_BA) / d(ln a)|
# This is the ELASTICITY of the sound speed with respect to the scale factor.
# If c_BA ~ a^alpha, then ratio = |alpha|.

# Compute the elasticity d(ln c)/d(ln a) directly
dlna = np.gradient(np.log(a_50), tau_50)
dlnc = np.gradient(np.log(np.abs(c_BA) + 1e-30), tau_50)
elasticity = dlnc / dlna  # d(ln c) / d(ln a)

print(f"\n--- Sound speed elasticity d(ln c_BA)/d(ln a) ---")
print(f"  At tau=0:   {elasticity[0]:.4f}")
print(f"  At fold:    {elasticity[fold_idx]:.4f}")
print(f"  Mean (0-fold): {np.mean(elasticity[:fold_idx+1]):.4f}")
print(f"  This equals T_Parker/T_GH (by construction)")

# =============================================================================
# 9. GATE EVALUATION
# =============================================================================
# The gate asks: |T_acoustic/T_GH - 1| < 0.5
# We must choose which T_acoustic.
#
# Physical argument: T_Parker is the most fundamental definition because it
# directly measures the non-adiabatic particle creation rate, which is what
# the "acoustic Hawking effect" actually IS in the absence of a sonic horizon.
#
# Report all three at fold.

dev_Parker = np.abs(ratio_Parker[fold_idx] - 1.0)
dev_conformal = np.abs(ratio_conformal[fold_idx] - 1.0)
dev_Ricci = np.abs(ratio_Ricci[fold_idx] - 1.0)

# Check across valid range (tau < 0.35 where H extrapolation is reliable)
valid = tau_50 < 0.35
best_Parker_idx = np.argmin(np.abs(ratio_Parker[valid] - 1.0))
best_Parker_dev = np.abs(ratio_Parker[valid][best_Parker_idx] - 1.0)
best_Parker_tau = tau_50[valid][best_Parker_idx]

print(f"\n{'='*72}")
print(f"GATE: ACOUSTIC-METRIC-58")
print(f"{'='*72}")
print(f"\nCriterion: |T_acoustic/T_GH - 1| < 0.5 at fold (tau={tau_50[fold_idx]:.4f})")
print(f"\n  T_Parker/T_GH - 1   at fold: {ratio_Parker[fold_idx] - 1:.6f}")
print(f"  |deviation|               : {dev_Parker:.6f}")
print(f"  {'PASS' if dev_Parker < 0.5 else 'FAIL/INFO'}")
print(f"\n  T_conformal/T_GH - 1 at fold: {ratio_conformal[fold_idx] - 1:.6f}")
print(f"  |deviation|               : {dev_conformal:.6f}")
print(f"  {'PASS' if dev_conformal < 0.5 else 'FAIL/INFO'}")
print(f"\n  T_Ricci/T_GH - 1 at fold: {ratio_Ricci[fold_idx] - 1:.6f}")
print(f"  |deviation|               : {dev_Ricci:.6f}")
print(f"  {'PASS' if dev_Ricci < 0.5 else 'FAIL/INFO'}")
print(f"\n  Best T_Parker match: tau={best_Parker_tau:.4f}, |ratio-1|={best_Parker_dev:.6f}")

# Choose the primary gate metric: T_Parker (most physical)
gate_value = dev_Parker
if gate_value < 0.5:
    gate_verdict = "PASS"
else:
    gate_verdict = "INFO"

print(f"\nPRIMARY GATE (T_Parker): {gate_verdict}")
print(f"  |T_Parker/T_GH - 1| = {gate_value:.4f}")

# Also check T_conformal
gate_value_conf = dev_conformal
if gate_value_conf < 0.5:
    conf_verdict = "PASS"
else:
    conf_verdict = "INFO"
print(f"  |T_conformal/T_GH - 1| = {gate_value_conf:.4f} => {conf_verdict}")

# =============================================================================
# 10. MACH NUMBER AND SONIC STRUCTURE (for context)
# =============================================================================
# The S57 "desert Mach number = 2700" uses the cosmic-time flow velocity
# dtau/dt ~ tau_fold / dt_transit. This is different from H_tau.
# dtau/dt from S38: tau_fold / dt_transit
v_cosmic = tau_fold / dt_transit  # ~ 168 M_KK
Mach_cosmic = v_cosmic / c_BA

# But for the acoustic metric in TAU coordinates, the relevant Mach number
# is the ratio of background evolution rate to sound speed:
Mach_moduli = H_50 / c_BA  # dimensionless (H has units M_KK, c has units M_KK)
# Actually: H_tau is dimensionless (d ln a / dtau, with tau dimensionless).
# c_BA has units M_KK. So this ratio needs care.
# In M_KK units: H_tau is in units of M_KK^0 (dimensionless).
# c_BA is in units of M_KK (since omega_BA is in M_KK and k is in M_KK).
# But wait: c_BA = omega_1 / k_min where omega_1 is in M_KK and k_min is
# dimensionless (=pi/diameter on a graph). So c_BA is in M_KK.
# And H_tau is dimensionless.
# So Mach = H_tau / c_BA doesn't have consistent dimensions.
#
# The correct Mach number uses v with the same units as c.
# v_cosmic = dtau/dt has units 1/[time] = M_KK.
# c_BA has units M_KK. So Mach_cosmic = v_cosmic / c_BA is dimensionless. Good.

print(f"\n--- Sonic structure ---")
print(f"  v_cosmic = tau_fold / dt_transit = {v_cosmic:.1f} M_KK")
print(f"  Mach_cosmic range: [{Mach_cosmic.min():.1f}, {Mach_cosmic.max():.1f}]")
print(f"  Mach_cosmic at fold: {Mach_cosmic[fold_idx]:.1f}")
print(f"  => DEEPLY SUPERSONIC. No sonic horizon in this picture.")
print(f"  The acoustic metric is in the 'cosmological' regime, not 'black hole' regime.")

# =============================================================================
# 11. SAVE DATA
# =============================================================================
outpath = os.path.join(os.path.dirname(__file__), 's58_acoustic_metric.npz')
np.savez(outpath,
    # Grid
    tau_values=tau_50,
    fold_idx=np.array(fold_idx),
    # Acoustic FRW metric
    g_tt=g_tt,
    g_tx=g_tx,
    g_xx=g_xx,
    det_g=det_g,
    # Unruh metric with conformal factor
    g_tt_unruh=g_tt_unruh,
    g_xx_unruh=g_xx_unruh,
    conformal_factor=conformal,
    # Physical quantities
    c_BA=c_BA,
    H_tau=H_50,
    a_tau=a_50,
    rho_eff=rho_eff,
    # Curvature
    R_acoustic=R_acoustic,
    # Temperatures
    T_GH=T_GH,
    T_Parker=T_Parker,
    T_conformal=T_conformal,
    T_Ricci=T_Ricci,
    # Ratios
    ratio_Parker=ratio_Parker,
    ratio_conformal=ratio_conformal,
    ratio_Ricci=ratio_Ricci,
    # Derived
    dlnc_dtau=dlnc_dtau,
    elasticity=elasticity,
    Mach_cosmic=Mach_cosmic,
    omega_evolution=omega_evolution,
    # Gate
    gate_name=np.array('ACOUSTIC-METRIC-58'),
    gate_verdict=np.array(gate_verdict),
    gate_value=np.array(gate_value),
    gate_value_conformal=np.array(gate_value_conf),
)
print(f"\nSaved: {outpath}")

# =============================================================================
# 12. PLOT
# =============================================================================
fig, axes = plt.subplots(3, 3, figsize=(18, 15))
fig.suptitle('S58 ACOUSTIC-METRIC-58: Unruh Acoustic Metric on Phononic Fabric',
             fontsize=14, fontweight='bold', y=0.98)

# (a) Sound speed c_BA(tau)
ax = axes[0, 0]
ax.plot(tau_50, c_BA, 'b-', lw=2, label=r'$c_{BA}(\tau)$')
ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5, label='fold')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$c_{BA}$ [$M_{KK}$]')
ax.set_title('(a) BA sound speed')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# (b) Scale factor a(tau)
ax = axes[0, 1]
ax.plot(tau_50, a_50, 'r-', lw=2, label=r'$a(\tau)$')
ax.plot(tau_50, H_50, 'b--', lw=1.5, label=r'$H_\tau = d\ln a/d\tau$')
ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$a, H$ [$M_{KK}$]')
ax.set_title('(b) Scale factor and Hubble')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# (c) Acoustic FRW metric components
ax = axes[0, 2]
ax.plot(tau_50, np.abs(g_tt), 'b-', lw=2, label=r'$|g_{tt}| = c_{BA}^2$')
ax.plot(tau_50, g_xx, 'r-', lw=2, label=r'$g_{xx} = a^2$')
ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel('Metric component')
ax.set_title('(c) Acoustic FRW metric')
ax.legend(fontsize=9)
ax.set_yscale('log')
ax.grid(True, alpha=0.3)

# (d) Ricci scalar
ax = axes[1, 0]
ax.plot(tau_50, R_acoustic, 'purple', lw=2)
ax.axhline(0, color='black', ls='-', alpha=0.3)
ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$R_{acoustic}$ [$M_{KK}^2$]')
ax.set_title('(d) Acoustic Ricci scalar')
ax.grid(True, alpha=0.3)

# (e) Temperatures
ax = axes[1, 1]
ax.plot(tau_50, T_GH, 'k-', lw=2, label=r'$T_{GH} = H/(2\pi)$')
ax.plot(tau_50, T_Parker, 'b--', lw=2, label=r'$T_{Parker} = |d\ln c/d\tau|/(2\pi)$')
ax.plot(tau_50, T_conformal, 'r:', lw=2, label=r'$T_{conf} = |d\ln c/d\tau - H|/(2\pi)$')
ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'Temperature [$M_{KK}$]')
ax.set_title('(e) Temperature comparison')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# (f) T_Parker / T_GH with PASS band
ax = axes[1, 2]
ax.plot(tau_50, ratio_Parker, 'b-', lw=2, label=r'$T_{Parker}/T_{GH}$')
ax.plot(tau_50, ratio_conformal, 'r--', lw=1.5, label=r'$T_{conf}/T_{GH}$')
ax.axhline(1.0, color='black', ls='-', alpha=0.5, label='Perfect match')
ax.fill_between(tau_50, 0.5, 1.5, alpha=0.1, color='green', label='PASS band')
ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5, label='fold')
ax.plot(tau_50[fold_idx], ratio_Parker[fold_idx], 'bo', ms=8, zorder=5,
        label=f'Fold: {ratio_Parker[fold_idx]:.3f}')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel('Ratio')
ax.set_title(f'(f) Gate: |ratio-1| < 0.5 => {gate_verdict}')
ax.legend(fontsize=8)
ax.set_ylim(0, min(5, max(3, 1.5*np.max(ratio_Parker[valid]))))
ax.grid(True, alpha=0.3)

# (g) Elasticity d(ln c)/d(ln a)
ax = axes[2, 0]
ax.plot(tau_50, elasticity, 'g-', lw=2)
ax.axhline(-1, color='red', ls='--', alpha=0.5, label=r'$\alpha = -1$')
ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$d\ln c_{BA} / d\ln a$')
ax.set_title(r'(g) Sound speed elasticity $\alpha$')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# (h) Mach number (cosmic)
ax = axes[2, 1]
ax.plot(tau_50, Mach_cosmic, 'k-', lw=2)
ax.axhline(1, color='red', ls='--', alpha=0.5, label='M=1')
ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'Mach (cosmic)')
ax.set_title(f'(h) Cosmic Mach number (fold={Mach_cosmic[fold_idx]:.0f})')
ax.legend(fontsize=9)
ax.set_yscale('log')
ax.grid(True, alpha=0.3)

# (i) Mode evolution adiabaticity
ax = axes[2, 2]
ax.plot(tau_50, np.abs(dlnc_dtau), 'b-', lw=2, label=r'$|d\ln c/d\tau|$ (Parker)')
ax.plot(tau_50, H_50, 'r--', lw=2, label=r'$H_\tau$ (geometric)')
ax.plot(tau_50, Q_adiabatic, 'g:', lw=2, label=r'$|d\ln\omega/d\tau|$ (full)')
ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel('Rate')
ax.set_title('(i) Adiabaticity: Parker vs geometric')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plotpath = os.path.join(os.path.dirname(__file__), 's58_acoustic_metric.png')
plt.savefig(plotpath, dpi=150, bbox_inches='tight')
print(f"Saved: {plotpath}")
plt.close()

# =============================================================================
# 13. SUMMARY
# =============================================================================
print(f"\n{'='*72}")
print("ACOUSTIC-METRIC-58 COMPLETE SUMMARY")
print(f"{'='*72}")

print(f"\n1. METRIC CONSTRUCTION:")
print(f"   Acoustic FRW: ds^2 = -c_BA^2 dtau^2 + a^2 dx^2")
print(f"   50 tau points, tau in [0, 0.5]")
print(f"   c_BA(0)={c_BA[0]:.4f}, c_BA(fold)={c_BA[fold_idx]:.4f}, c_BA(0.5)={c_BA[-1]:.4f}")
print(f"   a(0)={a_50[0]:.4f}, a(fold)={a_50[fold_idx]:.4f}, a(0.5)={a_50[-1]:.4f}")

print(f"\n2. SONIC STRUCTURE:")
print(f"   Cosmic Mach at fold: {Mach_cosmic[fold_idx]:.0f} (DEEPLY SUPERSONIC)")
print(f"   No sonic horizon => cosmological (Parker) regime, not Hawking regime")
print(f"   Flow regime: expanding acoustic universe, not acoustic black hole")

print(f"\n3. CURVATURE:")
print(f"   R_acoustic(fold) = {R_acoustic[fold_idx]:.6f} M_KK^2")
print(f"   R range: [{R_acoustic[valid].min():.4f}, {R_acoustic[valid].max():.4f}]")

print(f"\n4. TEMPERATURES:")
print(f"   T_GH(fold) = {T_GH[fold_idx]:.6f} M_KK")
print(f"   T_Parker(fold) = {T_Parker[fold_idx]:.6f} M_KK")
print(f"   T_conformal(fold) = {T_conformal[fold_idx]:.6f} M_KK")
print(f"   Sound speed elasticity at fold: alpha = {elasticity[fold_idx]:.4f}")

print(f"\n5. GATE VERDICT: ACOUSTIC-METRIC-58 = {gate_verdict}")
print(f"   Criterion: |T_Parker/T_GH - 1| < 0.5 at fold")
print(f"   T_Parker/T_GH at fold = {ratio_Parker[fold_idx]:.4f}")
print(f"   |T_Parker/T_GH - 1| = {dev_Parker:.4f}")

if gate_verdict == "PASS":
    print(f"   PHONONIC AND GEOMETRIC PICTURES ARE SELF-CONSISTENT.")
    print(f"   The Parker temperature from sound speed evolution matches T_GH")
    print(f"   to within the gate threshold.")
else:
    print(f"   T_Parker and T_GH differ by more than 50%. The two sectors")
    print(f"   are not in thermal equilibrium at the fold.")
    print(f"   Physical interpretation: the sound speed evolves at a DIFFERENT")
    print(f"   rate than the geometric expansion. The phononic sector has its")
    print(f"   own effective temperature distinct from the geometric one.")

print(f"\n6. STRUCTURAL RESULT:")
print(f"   T_Parker/T_GH = |d(ln c_BA)/d(ln a)| = 'sound speed elasticity'")
print(f"   This is a MEASURABLE quantity: how strongly does the BA sound speed")
print(f"   respond to the geometric expansion?")
print(f"   elasticity(fold) = {elasticity[fold_idx]:.4f}")
print(f"   If |alpha| = 1: acoustic and geometric sectors in equilibrium")
print(f"   If |alpha| < 1: sound speed evolves slower than geometry (phonons are 'stiff')")
print(f"   If |alpha| > 1: sound speed evolves faster (phonons are 'soft')")

print(f"\n{'='*72}")
print(f"DONE: ACOUSTIC-METRIC-58 = {gate_verdict}")
print(f"{'='*72}")
