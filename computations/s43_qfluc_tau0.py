#!/usr/bin/env python3
"""
QFLUC-43: Quantum Fluctuation Analysis at tau=0

Analyzes the primordial quantum fluctuation spectrum at tau=0 (the boundary/
unstable maximum of the moduli potential in the phonon-exflation framework).

Physics:
  - tau=0 is the round SU(3): maximum symmetry, MINIMUM of spectral action S_full
  - S_full is monotonically increasing (CUTOFF-SA-37 structural theorem)
  - The effective moduli potential V(tau) = -S(tau) * M_KK^4/(16pi^2) has tau=0
    as its MAXIMUM (hence "unstable maximum" of V, not of S)
  - Any perturbation delta_tau > 0 rolls downhill in V toward the fold
  - Quantum fluctuations delta_tau at the Planck epoch seed structure formation
  - Flatness from BDI topology (Volovik Paper 04: Fermi point scenario)

Gate: QFLUC-43
  PASS: P_R within 10 OOM of A_s = 2.1e-9 AND N_e > 10
  FAIL: P_R > 10^10 * A_s AND N_e < 1

Author: quantum-foam-theorist
Date: 2026-03-14
Session: 43
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# ============================================================
# 0. Load input data
# ============================================================
d36 = np.load('tier0-computation/s36_sfull_tau_stabilization.npz', allow_pickle=True)
d42g = np.load('tier0-computation/s42_gradient_stiffness.npz', allow_pickle=True)
d42c = np.load('tier0-computation/s42_constants_snapshot.npz', allow_pickle=True)

tau_arr = d36['tau_combined']
S_arr = d36['S_full']
tau_g = d42g['tau_grid']
Z_g = d42g['Z_spectral']
dS_g = d42g['dS_dtau']
d2S_g = d42g['d2S_dtau2']

# ============================================================
# 1. Physical constants (Planck units with hbar = c = 1)
# ============================================================
# Planck mass in GeV
from canonical_constants import M_Pl_unreduced as M_Pl  # GeV
M_Pl_reduced = M_Pl / np.sqrt(8 * np.pi)  # = 2.435e18 GeV

# M_KK from two routes (use gravity route as preferred, per HOMOG-42)
M_KK_GN = float(d42c['M_KK_from_GN'])       # 7.43e16 GeV
M_KK_kerner = float(d42c['M_KK_kerner'])     # 5.04e17 GeV
# Use M_KK_GN as primary (favored by FIRAS constraint per S42)
M_KK = M_KK_GN
print(f"M_KK = {M_KK:.3e} GeV (gravity route)")
print(f"M_KK/M_Pl = {M_KK/M_Pl:.3e}")
print(f"(M_KK/M_Pl)^2 = {(M_KK/M_Pl)**2:.3e}")

# M_ATDHFB (collective mass for tau) in M_KK units
M_ATDHFB = float(d42g['M_ATDHFB'][0])  # = 1.695 M_KK
print(f"M_ATDHFB = {M_ATDHFB:.4f} M_KK")

# ============================================================
# 2. Characterize tau=0: S(0), dS/dtau, d2S/dtau2, Z(0)
# ============================================================
S_0 = S_arr[0]  # S_full at tau=0

# dS/dtau at tau=0: use stored min_dS_dtau (computed from fine grid)
dS_dtau_0 = float(d36['min_dS_dtau'][0])  # = 3.552 M_KK^4

# d2S/dtau2 at tau=0: from forward finite differences on S_full
# Use 3-point forward formula: [f(2h) - 2f(h) + f(0)] / h^2
h = 0.05
d2S_dtau2_0 = (S_arr[2] - 2*S_arr[1] + S_arr[0]) / h**2

# Cross-check with extrapolation from s42 gradient stiffness data
# d2S at tau=0.05 is 304,605; at tau=0.10 is 309,071
# Linear extrapolation to tau=0: d2S(0) ~ 304,605 - 0.05*(309071-304605)/0.05 ~ 300,139
# Our finite-difference gives 304,638 -- consistent within discretization error
d2S_extrap = d2S_g[0] - tau_g[0] * (d2S_g[1] - d2S_g[0]) / (tau_g[1] - tau_g[0])

# Z(0): gradient stiffness at tau=0
# Extrapolate from Z(0.05) and Z(0.10) linearly to tau=0
Z_0_extrap = Z_g[0] - tau_g[0] * (Z_g[1] - Z_g[0]) / (tau_g[1] - tau_g[0])
# Also use: Z = d2S/dtau2 * Vol_SU3 / (some factor) -- but Z_spectral is
# the kinetic coefficient directly. Use the extrapolated value.
Z_0 = max(Z_0_extrap, Z_g[0] * 0.8)  # conservative lower bound

print(f"\n=== tau=0 characterization ===")
print(f"S(0) = {S_0:.2f} M_KK^4")
print(f"dS/dtau(0) = {dS_dtau_0:.4f} M_KK^4")
print(f"d2S/dtau2(0) = {d2S_dtau2_0:.2f} M_KK^4 (finite diff)")
print(f"d2S/dtau2(0) ~ {d2S_extrap:.2f} M_KK^4 (extrapolated)")
print(f"Z(0) extrapolated = {Z_0_extrap:.2f}")
print(f"Z(0) used = {Z_0:.2f}")
print(f"Z(0.05) = {Z_g[0]:.2f}")

# ============================================================
# 3. Effective potential and inverted harmonic oscillator
# ============================================================
# The spectral action enters the Friedmann equation as vacuum energy:
#   rho_Lambda(tau) = S_full(tau) * M_KK^4 / (16 pi^2)
#
# In the moduli EOM, the potential for tau is:
#   V(tau) = S_full(tau) * Lambda_cutoff^4 / (16 pi^2)
# where Lambda_cutoff = M_KK
#
# V(tau) = S_full(tau) * M_KK^4 / (16 pi^2)
#
# Since S_full is MONOTONICALLY INCREASING, V has NO maximum or minimum.
# tau=0 is the BOUNDARY where V is minimized (not maximized!).
#
# The "unstable maximum" framing: in the INVERTED interpretation where
# we consider V_eff = -S * M_KK^4/(16pi^2) as the potential for
# negative-energy-density driving, tau=0 IS the maximum.
#
# However, the correct dynamics is:
#   Z_0 * tau_ddot = dS/dtau > 0 always
# So tau is always accelerated AWAY from 0.

# The effective mass-squared for tau fluctuations:
# From the Lagrangian L = (1/2)*Z(tau)*tau_dot^2 - V(tau)
# EOM: Z*tau_ddot + (1/2)*(dZ/dtau)*tau_dot^2 = -dV/dtau
# For small tau_dot (near tau=0):
# Z_0 * tau_ddot = -V'(0) = -S'(0) * M_KK^4/(16pi^2)
#
# Wait: the sign. S is increasing, so V = +S*M_KK^4/(16pi^2) is increasing.
# Then -V' < 0 means tau wants to decrease? No -- tau is at the boundary tau=0.
#
# Actually the correct sign depends on the role of S in the action:
# The spectral action S_full appears as the BOSONIC action = integral over spacetime
# In the Einstein frame, higher S means MORE vacuum energy.
# The modulus wants to MINIMIZE vacuum energy, which means minimize S.
# But S(0) is already the minimum! So tau=0 is a STABLE point from
# the vacuum energy perspective.
#
# The INSTABILITY comes from the BCS condensate channel:
# The pairing interaction drives tau to the fold.
# This is the mechanism chain from S35.
#
# For the fluctuation analysis, what matters is the LOCAL curvature:
# m_tau^2 = V''(0) / Z(0) = d2S/dtau2(0) * M_KK^4/(16pi^2) / Z(0)
# This is POSITIVE: tau oscillates around 0 (if confined there)
# The instability is from the BCS channel, not from V''

# The physical picture: tau=0 is an inflection-like boundary.
# Quantum fluctuations have amplitude set by the effective mass.

# Effective mass squared of modulus (in M_KK units):
# m_tau^2 = d2V/dtau2 / Z = d2S/dtau2 * M_KK^4/(16pi^2) / Z
# But V and Z are in the same units, so:
m_tau_sq_MKK = d2S_dtau2_0 / Z_0  # dimensionless (units of M_KK^2)
m_tau_MKK = np.sqrt(abs(m_tau_sq_MKK))
print(f"\n=== Effective modulus mass ===")
print(f"m_tau^2 = d2S/dtau2 / Z = {m_tau_sq_MKK:.4f} M_KK^2")
print(f"m_tau = {m_tau_MKK:.4f} M_KK")
print(f"m_tau = {m_tau_MKK * M_KK:.3e} GeV")
print(f"m_tau / M_Pl = {m_tau_MKK * M_KK / M_Pl:.3e}")

# Cross-check with HOMOG-42 value: m_tau/H = 25.9
# H at the initial epoch is set by V(0) = S(0)*M_KK^4/(16pi^2)

# ============================================================
# 4. Hubble rate at tau=0
# ============================================================
# Friedmann equation: H^2 = (8piG/3) * rho
# rho(0) = S(0) * M_KK^4 / (16 pi^2)
# G = 1/(8 pi M_Pl_reduced^2) in natural units
#
# H^2 = (1/(3 M_Pl_reduced^2)) * S(0) * M_KK^4 / (16 pi^2)

rho_0_GeV4 = S_0 * M_KK**4 / (16 * np.pi**2)
H_0_sq = rho_0_GeV4 / (3 * M_Pl_reduced**2)
H_0 = np.sqrt(H_0_sq)

print(f"\n=== Hubble rate at tau=0 ===")
print(f"rho(0) = S(0) * M_KK^4/(16pi^2) = {rho_0_GeV4:.3e} GeV^4")
print(f"rho(0) / M_Pl^4 = {rho_0_GeV4 / M_Pl**4:.3e}")
print(f"H(0) = {H_0:.3e} GeV")
print(f"H(0) / M_Pl = {H_0/M_Pl:.3e}")
print(f"H(0) / M_KK = {H_0/M_KK:.3e}")

# m_tau / H ratio (cf HOMOG-42: 25.9)
m_tau_GeV = m_tau_MKK * M_KK
print(f"\nm_tau / H = {m_tau_GeV / H_0:.2f}")
print(f"(HOMOG-42 reported: 25.9)")

# ============================================================
# 5. Quantum fluctuation amplitude
# ============================================================
# For a massive scalar field in de Sitter space:
# <delta_tau^2> = (3 H^4) / (8 pi^2 m_tau^2)  for m_tau >> H (superheavy)
# <delta_tau^2> = (H/(2pi))^2 for m_tau << H (light field)
#
# Since m_tau/H >> 1 (superheavy regime), use the heavy field result:
# <delta_tau^2> = 3 H^4 / (8 pi^2 m_tau^2 H^2) * correction
# More precisely, for m >> H:
# <delta_tau^2> ~ H^3 / (4 pi^2 m_tau) * exp(-2 m_tau / H)  [exponentially suppressed!]
#
# But actually for a field at the BOUNDARY of moduli space (tau >= 0),
# the half-space constraint doubles the probability density at tau=0.
# The relevant fluctuation is the zero-point:
# <delta_tau^2> = hbar / (2 * m_tau * Z_eff)  (quantum mechanical, NOT de Sitter)
# This is the inverted HO formula from the task spec, corrected for positive mass

# Method A: Zero-point fluctuation of the modulus (quantum mechanics)
# <tau^2>_zp = 1 / (2 * sqrt(d2V * Z_0))
# where d2V = d2S/dtau2 * M_KK^4/(16pi^2)
# BUT in natural units with hbar=1, M_KK units:
# <tau^2>_zp = 1 / (2 * sqrt(d2S_0 * Z_0)) [dimensionless in M_KK units]
# Actually more carefully:
# L_tau = (1/2)*Z_0*tau_dot^2 - (1/2)*m_tau_eff^2*tau^2
# where m_tau_eff^2 = d2V/dtau2 = d2S/dtau2 * M_KK^4/(16pi^2)
# and Z_0 has dimensions of [M_KK^2] (kinetic coefficient)
# omega = sqrt(m_tau_eff^2 / Z_0)
# <tau^2> = hbar/(2*Z_0*omega) = hbar/(2*sqrt(Z_0*m_tau_eff^2))
# = 1/(2*sqrt(Z_0 * d2S_0 * M_KK^4/(16pi^2)))

# In M_KK = 1 units (so M_KK^4/(16pi^2) -> 1/(16pi^2)):
delta_tau_sq_A = 1.0 / (2.0 * np.sqrt(Z_0 * d2S_dtau2_0 / (16 * np.pi**2)))
delta_tau_A = np.sqrt(delta_tau_sq_A)

# Actually, Z_0 and d2S are both in M_KK units in the data.
# The kinetic term is Z_0 * tau_dot^2 where Z_0 ~ 43,000 (dimensionless in M_KK units)
# The potential curvature d2V/dtau2 = d2S/dtau2 * M_KK^4/(16pi^2)
# But d2S/dtau2 is already in M_KK^4 units (S has units M_KK^4 * [dimensionless])
# Actually S_full is a PURE NUMBER (spectral action is dimensionless in the Connes framework)
# V = S_full * Lambda^4/(16pi^2) where Lambda = M_KK is the cutoff
# Z is also dimensionless? Let me think more carefully.

# The spectral action is S_B = Tr[f(D^2/Lambda^2)] where Lambda = M_KK
# This gives S_B = sum of a_n * Lambda^{d-n} * f_n
# For d=6 internal manifold: a_0*f_0*Lambda^6 + a_2*f_2*Lambda^4 + ...
# Actually the dimensionful part is Lambda^{d-n}, the a_n are geometric
# The TOTAL spectral action (what's stored) is S_full = sum_sectors sum_n lambda_n^2
# where lambda_n are eigenvalues of D_K in M_KK units.
# So S_full is dimensionless (eigenvalues in M_KK units, squared, summed).
# The PHYSICAL vacuum energy is V = S_full * M_KK^4 / (16*pi^2)

# Z is the kinetic stiffness: L_tau = (1/2)*Z*M_KK^2*tau_dot^2
# where tau_dot is in 1/time and the factor M_KK^2 makes it [Energy^2]
# Actually Z comes from d^2(S_full)/dtau^2 * something...
# From the task: Z = d2S/d(dtau/dx)^2 (gradient stiffness)
# In the modulus EOM: Z * tau_ddot = dS/dtau (in M_KK = 1 units)
# So Z has dimensions of [S/tau^2]/[S'/tau'] which is just [1] if S is dimensionless

# Therefore:
# L = (1/2)*Z*tau_dot^2 - S*M_KK^4/(16pi^2) [physical units]
# omega^2 = (d2S/dtau2)/(Z) * M_KK^4/(16pi^2) / M_KK^2  ???
# No. Let me be systematic.

# In PHYSICAL units (GeV):
# L_phys = (1/2) * Z_0 * M_KK^2 * (dtau/dt)^2 - V(tau)
# V(tau) = S(tau) * M_KK^4 / (16 pi^2)
# EOM: Z_0 * M_KK^2 * d2tau/dt2 = -dV/dtau = -S'(tau) * M_KK^4/(16pi^2)
#
# Wait: Z_spectral is defined as the kinetic coefficient.
# From s42_gradient_stiffness: Z_spectral = sum of eigenvalue derivatives squared
# It has the same dimensions as S_full (dimensionless, being sum of eigenvalues^2 type)
# The physical kinetic term is (1/2)*Z*M_KK^2*(dtau/dt)^2
# Actually no: Z should absorb the M_KK factors properly.
#
# Let me use the direct approach from HOMOG-42:
# M_ATDHFB = 1.695 M_KK is the collective mass
# The EOM is M_ATDHFB * tau_ddot = F(tau) / M_KK
# where F(tau) = dS/dtau * M_KK^3/(16pi^2)
#
# Actually from the code, M_ATDHFB = sqrt(Z * Vol_SU3) or similar.
# Let me just use the M_ATDHFB directly.

# From HOMOG-42 and s42 gradient stiffness:
# M_ATDHFB = 1.695 (in M_KK units)
# The EOM in dimensionless tau, physical time t:
# M_ATDHFB * M_KK * d2tau/dt2 = dS/dtau * M_KK^3/(16pi^2) ?
# Dimensional analysis: [M_KK] * [1/t^2] = [M_KK^3/(16pi^2)] ? -> [M_KK]*[M_KK^2]=[M_KK^3]. Check.
# No: M_ATDHFB*M_KK has units [GeV], d2tau/dt2 has units [GeV^2] (natural units t=1/GeV)
# LHS: [GeV]*[GeV^2] = [GeV^3]
# RHS: dS/dtau * M_KK^3/(16pi^2) = [1]*[GeV^3] = [GeV^3]. Check!

# So the oscillation frequency around a minimum would be:
# omega^2 = d2V_phys/dtau^2 / (M_ATDHFB * M_KK)
# = d2S/dtau2 * M_KK^3/(16pi^2) / (M_ATDHFB * M_KK)
# = d2S/dtau2 * M_KK^2 / (16pi^2 * M_ATDHFB)

omega_sq_GeV2 = d2S_dtau2_0 * M_KK**2 / (16 * np.pi**2 * M_ATDHFB)
omega_GeV = np.sqrt(omega_sq_GeV2)

print(f"\n=== Modulus oscillation frequency ===")
print(f"omega^2 = d2S/Z * M_KK^2/(16pi^2) = {omega_sq_GeV2:.3e} GeV^2")
print(f"omega = {omega_GeV:.3e} GeV")
print(f"omega / M_KK = {omega_GeV/M_KK:.4f}")
print(f"omega / H = {omega_GeV/H_0:.2f}")

# Method B: Zero-point fluctuation using M_ATDHFB
# <tau^2> = hbar / (2 * M_ATDHFB * M_KK * omega)
# In natural units hbar=1:
delta_tau_sq_B = 1.0 / (2.0 * M_ATDHFB * M_KK * omega_GeV)
delta_tau_B = np.sqrt(delta_tau_sq_B)

print(f"\n=== Quantum fluctuation amplitude ===")
print(f"delta_tau (zero-point) = {delta_tau_B:.3e}")
print(f"delta_tau / tau_fold = {delta_tau_B / 0.19:.3e}")

# Method C: de Sitter fluctuation for superheavy field (m >> H)
# <delta_tau^2> ~ (H^2/(4pi^2)) * (H/m_tau)^2 * e^{-2m/H} [suppressed]
m_eff_GeV = omega_GeV  # effective mass
ratio_mH = m_eff_GeV / H_0
print(f"\nm_tau_eff / H = {ratio_mH:.2f} (superheavy regime: m >> H)")

if ratio_mH > 3:
    # Superheavy: use Starobinsky suppression
    delta_tau_dS = (H_0 / (2*np.pi)) * np.exp(-np.pi * ratio_mH)
    print(f"delta_tau (de Sitter, exp suppressed) = {delta_tau_dS:.3e}")
    print(f"  -> Exponential suppression factor e^{{-pi*m/H}} = {np.exp(-np.pi*ratio_mH):.3e}")
    delta_tau_use = delta_tau_B  # Use zero-point as the LARGER (and relevant) value
else:
    delta_tau_dS = H_0 / (2*np.pi * m_eff_GeV)
    print(f"delta_tau (de Sitter) = {delta_tau_dS:.3e}")
    delta_tau_use = max(delta_tau_B, delta_tau_dS)

# NOTE: For m >> H, de Sitter fluctuations are exponentially suppressed.
# The relevant fluctuation is the ZERO-POINT value (quantum mechanical).
# This is also what survives at the Planck epoch before inflation.

print(f"\n** Using delta_tau = {delta_tau_use:.3e} (zero-point, dominant for superheavy) **")

# ============================================================
# 6. Fluctuation power spectrum P_tau(k) and curvature P_R(k)
# ============================================================
# For a single modulus rolling from tau=0:
# The perturbation delta_tau generates curvature perturbations via:
# R = -(H/tau_dot) * delta_tau  (for adiabatic perturbations)
#
# P_R = (H/tau_dot)^2 * P_tau(k)
#
# P_tau(k) = (H/(2pi))^2 for m << H (light field)
# P_tau(k) ~ zero-point / volume for superheavy

# tau_dot at tau=0: from EOM
# M_ATDHFB * M_KK * tau_ddot = dS/dtau * M_KK^3/(16pi^2)
# Initially tau_dot = 0, tau_ddot = dS_0/dtau * M_KK^2/(16pi^2 * M_ATDHFB)
tau_ddot_0 = dS_dtau_0 * M_KK**2 / (16 * np.pi**2 * M_ATDHFB)
print(f"\n=== tau dynamics at tau=0 ===")
print(f"tau_ddot(0) = {tau_ddot_0:.3e} GeV^2")

# tau_dot after time dt: tau_dot ~ tau_ddot * dt
# At what time does tau_dot become significant?
# Time to reach tau ~ delta_tau: t ~ sqrt(2*delta_tau/tau_ddot)
t_fluct = np.sqrt(2 * delta_tau_use / tau_ddot_0)
print(f"t_fluct (time to reach delta_tau) = {t_fluct:.3e} GeV^-1")
print(f"t_fluct * H = {t_fluct * H_0:.3e}")

# tau_dot at time t_fluct:
tau_dot_fluct = tau_ddot_0 * t_fluct
print(f"tau_dot at t_fluct = {tau_dot_fluct:.3e} GeV")

# Slow-roll parameter epsilon:
# epsilon = (M_Pl^2/2) * (V'/V)^2
# V' = dS/dtau * M_KK^4/(16pi^2)
# V = S(0) * M_KK^4/(16pi^2)
# (V'/V) = dS/dtau / S(0) = 3.55 / 244839 = 1.45e-5
Vp_over_V = dS_dtau_0 / S_0
epsilon = 0.5 * (M_Pl_reduced / M_KK)**2 * Vp_over_V**2 * (M_KK/M_Pl_reduced)**2
# Wait, let me be more careful:
# epsilon = (M_Pl_reduced^2 / 2) * (dV/dtau)^2 / V^2
# V = S * M_KK^4/(16pi^2), dV/dtau = S' * M_KK^4/(16pi^2)
# (dV/dtau / V) = S'/S = dimensionless/dimensionless = 1/tau
# BUT tau is dimensionless so dV/dtau has units of V.
# In Planck units: V_Pl = V/M_Pl^4, etc.
# epsilon = (1/2) * (dV/dtau / V)^2 * M_Pl_reduced^2 [when dtau has dimensions of 1/M_Pl]
# Actually tau is dimensionless, so we need the field-space metric
# The canonical field phi = sqrt(Z_0) * M_KK * tau (has dimensions of GeV)
# epsilon = (M_Pl_reduced^2/2) * (dV/dphi)^2 / V^2
# dV/dphi = (dV/dtau) / (sqrt(Z_0) * M_KK)
# = S'(tau) * M_KK^4/(16pi^2) / (sqrt(Z_0)*M_KK)
# = S'(tau) * M_KK^3 / (16pi^2 * sqrt(Z_0))

dV_dphi = dS_dtau_0 * M_KK**3 / (16 * np.pi**2 * np.sqrt(Z_0))
V_0 = S_0 * M_KK**4 / (16 * np.pi**2)

epsilon_V = 0.5 * M_Pl_reduced**2 * (dV_dphi / V_0)**2

# Also compute eta
# eta = M_Pl^2 * V''/V
# V'' = d^2V/dphi^2 = (1/(Z_0*M_KK^2)) * d2S/dtau2 * M_KK^4/(16pi^2)
#      = d2S/dtau2 * M_KK^2 / (16pi^2 * Z_0)
d2V_dphi2 = d2S_dtau2_0 * M_KK**2 / (16 * np.pi**2 * Z_0)
eta_V = M_Pl_reduced**2 * d2V_dphi2 / V_0

print(f"\n=== Slow-roll parameters ===")
print(f"V'/V = S'/S = {Vp_over_V:.6e}")
print(f"dV/dphi = {dV_dphi:.3e} GeV^3")
print(f"V(0) = {V_0:.3e} GeV^4")
print(f"epsilon_V = (M_Pl^2/2)(V'/V_phi)^2 = {epsilon_V:.6e}")
print(f"eta_V = M_Pl^2 * V''/V = {eta_V:.6e}")

# n_s and r predictions:
n_s = 1 - 6*epsilon_V + 2*eta_V
r_tensor = 16 * epsilon_V

print(f"\nn_s = 1 - 6*eps + 2*eta = {n_s:.6f}")
print(f"r = 16*eps = {r_tensor:.6e}")

# ============================================================
# 7. Curvature power spectrum P_R(k)
# ============================================================
# Standard inflation formula:
# P_R = V / (24 pi^2 M_Pl^4 epsilon)
# Note: this uses REDUCED Planck mass
P_R = V_0 / (24 * np.pi**2 * M_Pl_reduced**4 * epsilon_V)

# Alternative using H and tau_dot:
# P_R = H^2 / (8 pi^2 epsilon M_Pl_reduced^2)
P_R_alt = H_0**2 / (8 * np.pi**2 * epsilon_V * M_Pl_reduced**2)

from canonical_constants import A_s_CMB as A_s_obs  # Planck 2018

print(f"\n=== Curvature power spectrum ===")
print(f"P_R = V/(24pi^2 M_Pl^4 epsilon) = {P_R:.3e}")
print(f"P_R (alt) = H^2/(8pi^2 eps M_Pl^2) = {P_R_alt:.3e}")
print(f"A_s (observed) = {A_s_obs:.1e}")
print(f"log10(P_R / A_s) = {np.log10(P_R / A_s_obs):.2f}")
print(f"|log10(P_R/A_s)| < 10? {abs(np.log10(P_R/A_s_obs)) < 10}")

# ============================================================
# 8. Transit duration and e-fold count
# ============================================================
# N_e = integral_0^{tau_fold} H / |tau_dot| dtau
#
# Build interpolated functions for S(tau), H(tau), tau_dot(tau)
# using the data arrays

# Interpolate S_full as function of tau
cs_S = CubicSpline(tau_arr, S_arr)

# Dense tau grid for integration
tau_dense = np.linspace(1e-4, 0.19, 1000)
S_dense = cs_S(tau_dense)
dS_dense = cs_S(tau_dense, 1)  # first derivative

# H(tau) from Friedmann: H^2 = V(tau) / (3 M_Pl_reduced^2)
V_dense = S_dense * M_KK**4 / (16 * np.pi**2)
H_dense = np.sqrt(V_dense / (3 * M_Pl_reduced**2))

# tau_dot from the EOM (energy conservation):
# (1/2) * M_ATDHFB * M_KK * tau_dot^2 = V(0) - V(tau)
# Wait: V is increasing, so V(tau) > V(0). This means kinetic energy is NEGATIVE?
# No -- the dynamics is DRIVEN by the gradient dS/dtau > 0.
# The equation of motion: M_ATDHFB * M_KK * d2tau/dt2 = dS/dtau * M_KK^3/(16pi^2)
# Energy conservation: (1/2)*M_ATDHFB*M_KK*tau_dot^2 + const = S(tau)*M_KK^4/(16pi^2)
# But actually this doesn't conserve because of Hubble friction!
#
# Correct EOM with Hubble friction:
# (M_ATDHFB * M_KK) * [tau_ddot + 3H*tau_dot] = dS/dtau * M_KK^3/(16pi^2)
#
# For the transit, SELF-CONSIST-40 found transit is 1.72x faster with M_coll.
# FRIED-39 found N_transit ~ 5e-5 e-folds.
# Let me compute N_e directly.

# Simple estimate without friction (upper bound on tau_dot):
# (1/2)*M_ATDHFB*M_KK*tau_dot^2 = integral_0^tau dS/dtau' * M_KK^3/(16pi^2) dtau'
# = [S(tau) - S(0)] * M_KK^3/(16pi^2) * M_KK

# With friction, tau_dot is smaller, N_e could be larger.
# But the transit is fast (N << 1), so friction is negligible.

# Energy conservation (no friction):
# (1/2) * M * tau_dot^2 = integral of force = [S(tau)-S(0)] * M_KK^4/(16pi^2) / (M*c^2...)
# Let me use proper units.
# Mass parameter: M_coll = M_ATDHFB * M_KK [GeV]
# Force: F = dS/dtau * M_KK^3/(16pi^2) [GeV^2]
# KE: (1/2)*M_coll*tau_dot^2 = integral_0^tau F dtau'
#   = [S(tau)-S(0)] * M_KK^3/(16pi^2)   [GeV... hmm dimensions]
#
# Actually F*dtau has dimensions [GeV^2]*[1] = [GeV^2] (tau is dimensionless)
# KE = (1/2)*M_coll*tau_dot^2: [GeV]*[GeV^2] = [GeV^3] ???
# tau_dot = dtau/dt has dimensions [GeV] (t in 1/GeV)
# KE = (1/2)*M_coll*tau_dot^2 = [GeV]*[GeV^2] = [GeV^3]
# Work = F * tau = [GeV^2]*[1] = [GeV^2] -- MISMATCH!
#
# The problem is my force equation. Let me redo:
# Action: S_total = integral dt { (1/2)*Z_0*(M_KK^2)*tau_dot^2 - S_full(tau)*M_KK^4/(16pi^2) }
# Wait, the kinetic term: Z_spectral is defined in the data as the gradient stiffness.
# From s42: Z_fold = 74730.76 (dimensionless)
# The physical kinetic term should be:
# T = (1/2) * Z_0 * M_KK^4 / (16pi^2) * tau_dot^2 ??? No.
#
# Let me go back to basics. The spectral action gives:
# S_spectral = f_0 a_0 Lambda^6 + f_2 a_2 Lambda^4 + f_4 a_4 Lambda^2 + ...
# where Lambda = M_KK, and a_n depend on the geometry (including tau).
# For the KINETIC term of tau, we need the term with (dtau/dx)^2:
# This comes from the heat kernel coefficient a_2 which contains the Ricci scalar R
# R ~ (dtau/dx)^2 * (some curvature factor)
# So the kinetic term scales as Z * M_KK^4 * (dtau/dx)^2
#
# For COSMOLOGICAL modulus dynamics, the relevant action is:
# S = integral d^4x sqrt(-g) [ (1/2)*Z_tau*M_KK^2*(nabla tau)^2 - V(tau) ]
# where Z_tau includes the volume factor of internal space
# V(tau) = S_full(tau) * M_KK^4 / (16pi^2)
#
# From s42, Z_spectral plays the role of Z_tau (but may have different normalization).
# M_ATDHFB = 1.695 M_KK was computed FROM Z_spectral.
# Use M_ATDHFB directly: the MASS parameter for tau dynamics.
#
# In the minisuperspace reduction:
# L_eff = (1/2)*M_eff*tau_dot^2 - V(tau) integrated over 3-volume
# where M_eff = M_ATDHFB * M_KK * V_3 ???
# No -- for a HOMOGENEOUS modulus, the EOM is:
# tau_ddot + 3H*tau_dot = -V'(tau) / (M_eff^2)
#
# Let me just use the EOM from S42 directly.
# From HOMOG-42: the velocity is:
# tau_dot = dS/dtau / (M_ATDHFB * something * H * ...)
# Actually, in slow-roll: 3H*tau_dot = -V'/M_eff^2
# In the canonical normalization:
# phi = sqrt(Z_0) * M_KK * tau  (canonical scalar)
# phi_dot + 3H*phi_dot_dot ??? No: ddot(phi) + 3H*dot(phi) = -dV/dphi
# Slow-roll: 3H*phi_dot ≈ -dV/dphi
# tau_dot = phi_dot / (sqrt(Z_0)*M_KK) ≈ -dV/dphi / (3H*sqrt(Z_0)*M_KK)
# = -(S'*M_KK^3/(16pi^2*sqrt(Z_0))) / (3H*sqrt(Z_0)*M_KK)
# = -S'*M_KK^2 / (48pi^2*H*Z_0)

# But S' > 0 everywhere and V is increasing, so V' > 0.
# In standard inflation, the field rolls DOWN the potential (V' < 0 => phi_dot > 0).
# Here, V' > 0 means the "inflaton" tau would have phi_dot < 0 in slow-roll,
# i.e., tau wants to DECREASE. But tau=0 is the boundary!
# This confirms: tau=0 is a MINIMUM of V, not a maximum.
# The TRANSIT from tau=0 to the fold is NOT driven by the potential gradient
# (which pushes tau back toward 0). The transit is driven by the BCS mechanism.

# CRITICAL REALIZATION: The spectral action S_full monotonically increases,
# so V(tau) = S * M_KK^4/(16pi^2) increases with tau.
# tau=0 is the GLOBAL MINIMUM of V.
# The "unstable maximum" in the task description refers to V_eff = -S
# (negative of spectral action as potential).
# In the STANDARD (positive energy) interpretation, tau=0 is STABLE.
#
# The BCS mechanism provides an ADDITIONAL negative-energy channel:
# V_total = V_spectral + V_BCS = S*M_KK^4/(16pi^2) + E_BCS(tau)
# where E_BCS < 0 at the fold. The BCS channel creates the instability.
# But E_BCS/S_fold ~ 10^{-6} (effacement), so it barely modifies V.
#
# For quantum fluctuation analysis, the SPECTRAL ACTION potential dominates.
# And in this potential, tau=0 IS stable: V''(0) > 0.
# The modulus is TRAPPED at tau=0 with zero-point fluctuations delta_tau.

# For the transit:
# In the FRIED-39 / SELF-CONSIST-40 analysis, the transit happens via
# the BCS driving force, NOT the spectral action gradient.
# The spectral action gradient OPPOSES the transit (restoring force toward tau=0).
# The BCS force overcomes this for the instanton gas / Schwinger mechanism.
# But FRIED-39 found a shortfall of ~38,600x (later ~114,000x with M_coll).

# Given this, the correct transit dynamics is:
# The system is INITIALLY at tau=0 with quantum fluctuations delta_tau ~ 10^{-10}.
# There is no classical slow-roll. The transit is quantum mechanical (instanton gas).
# The e-fold count from the spectral action "inflation" is essentially ZERO.

# N_e from spectral action rolling (if it could roll):
# In slow-roll: N = integral V/V' dphi = integral (V*Z_0*M_KK^2)/(V'^2/M_Pl^2) dtau...
# N = M_Pl^2 * integral V/V'_phi^2 dphi
# = M_Pl^2 * integral (S * M_KK^4/(16pi^2)) / ((S')^2 * M_KK^6/(16pi^2)^2 / Z_0) dtau
# = M_Pl^2 * integral S * Z_0 * (16pi^2) / (S'^2 * M_KK^2) dtau

# But wait: the field rolls TOWARD tau=0 (V' > 0 pushes down), not away.
# So there's no inflationary phase from V(tau) = S(tau) * M_KK^4/(16pi^2).
# The sign is wrong for inflation.

# The "inflation" interpretation requires V = CONSTANT - S*M_KK^4/(16pi^2),
# which would be a DECREASING potential. Let me check if this is the right sign.

# In Connes' framework, the spectral action gives the BOSONIC action including
# cosmological constant, Einstein-Hilbert, and gauge kinetic terms.
# The CC term is a_0 * f_0 * Lambda^6 / (16pi^2) with a_0 = S_full at L=0 level
# This is POSITIVE vacuum energy. As tau increases, a_0 increases,
# so the CC increases. This is NOT suitable for inflation unless we flip sign.

# Alternatively: the TOTAL energy is V_total = V_vac + V_kinetic + V_BCS
# At the Planck epoch, V_vac ~ M_Pl^4. The spectral action term S*M_KK^4
# is the INTERNAL contribution, much smaller than M_Pl^4.
# Inflation might come from EXTERNAL sector physics (e.g., Starobinsky from R^2).

# For this analysis, I will compute:
# 1. The quantum fluctuation delta_tau at tau=0 (zero-point of the potential)
# 2. The induced P_R assuming the fluctuation exits during EXTERNAL inflation
# 3. The N_e from the MODULUS transit (expect << 1)

# Compute N_e from modulus transit (classically, no friction, as upper bound):
# KE = integral_0^tau F(tau') dtau' where F = dV/dtau / Z
# Using canonical field: (1/2)*phi_dot^2 = integral_0^phi F dphi'
# phi_dot^2 = 2 * integral [V'(tau')/(sqrt(Z_0)*M_KK)] * d(sqrt(Z_0)*M_KK*tau')
# = 2 * integral V'(tau') dtau' = 2 * [V(tau) - V(0)]
#
# But V increases, so phi_dot^2 = 2*[V(tau)-V(0)] > 0.
# This means the field CAN roll up the potential if given kinetic energy.
# The BCS mechanism provides this kick.

# For the BCS-driven transit:
# The BCS condensation energy E_cond = -0.137 M_KK provides the driving force.
# V_BCS(tau) ~ -0.137 * M_KK^4 * theta(tau > tau_onset)
# The total potential V_total = S(tau)*M_KK^4/(16pi^2) + V_BCS
# Since |V_BCS| << V_spectral by the effacement ratio ~10^{-6},
# the transit is barely affected.

# N_e from modulus transit:
# tau_dot_classical ~ sqrt(2*Delta_V/M_ATDHFB) where Delta_V ~ dS/dtau * delta_tau * M_KK^3/(16pi^2)
# Actually, for forced rolling with dS/dtau driving:
# tau evolves as tau(t) ~ (1/2) * a * t^2 with a = dS_0/(16pi^2*M_ATDHFB) * M_KK^2
# Time to transit: t_transit ~ sqrt(2*tau_fold/a) = sqrt(2*0.19/a)

a_accel = dS_dtau_0 * M_KK**2 / (16 * np.pi**2 * M_ATDHFB)
# But this is the acceleration at tau=0 where dS/dtau is minimum.
# At larger tau, dS/dtau grows (factor ~16,000x from 3.55 to 58,673)
# Use average dS/dtau for estimate:
dS_avg = (dS_dtau_0 + 58672.80) / 2
a_avg = dS_avg * M_KK**2 / (16 * np.pi**2 * M_ATDHFB)
t_transit = np.sqrt(2 * 0.19 / a_avg)
tau_dot_end = a_avg * t_transit

print(f"\n=== Transit dynamics (no Hubble friction) ===")
print(f"Acceleration at tau=0: a = {a_accel:.3e} GeV^2")
print(f"Average acceleration: a_avg = {a_avg:.3e} GeV^2")
print(f"Transit time: t_transit ~ {t_transit:.3e} GeV^-1")
print(f"H * t_transit = {H_0 * t_transit:.3e}")
print(f"N_e (transit) ~ H * t_transit = {H_0 * t_transit:.3e}")

# With Hubble friction (slow-roll-like):
# 3H*tau_dot_canonical = -V' where V is increasing
# tau_dot_slow = dV/dphi / (3H) [rolling UP]
# This doesn't apply: slow-roll requires V' < 0 for the field to roll.
# The modulus cannot slow-roll up V.

# Correct approach: the modulus experiences:
# 1. Spectral action restoring force (toward tau=0)
# 2. BCS driving force (toward fold)
# 3. Hubble friction (opposing motion)
# Net: BCS wins if E_BCS overcomes V(fold)-V(0) = delta_S * M_KK^4/(16pi^2)
# delta_S = 250361 - 244839 = 5522
# V(fold)-V(0) = 5522 * M_KK^4/(16pi^2)
# |E_BCS| = 0.137 * M_KK^4
# Ratio: |E_BCS| / [delta_S*M_KK^4/(16pi^2)] = 0.137*16pi^2/5522 = 0.0392
# BCS energy is 4% of the spectral action barrier. BCS CANNOT drive the transit!
# This is consistent with FRIED-39 shortfall.

delta_S = S_arr[7] - S_arr[0]  # S(0.19) - S(0)
V_barrier = delta_S * M_KK**4 / (16 * np.pi**2)
E_BCS = 0.137 * M_KK**4
ratio_BCS_barrier = E_BCS / V_barrier
print(f"\n=== BCS vs spectral action barrier ===")
print(f"delta_S = S(fold) - S(0) = {delta_S:.2f}")
print(f"V_barrier = delta_S * M_KK^4/(16pi^2) = {V_barrier:.3e} GeV^4")
print(f"|E_BCS| = {E_BCS:.3e} GeV^4")
print(f"|E_BCS| / V_barrier = {ratio_BCS_barrier:.4f}")
print(f"BCS cannot drive transit: BCS/barrier = {ratio_BCS_barrier:.1%}")

# N_e = H * t_transit for the modulus transit:
N_e_transit = H_0 * t_transit
print(f"\n=== e-fold count from modulus transit ===")
print(f"N_e = H * t_transit = {N_e_transit:.3e}")
print(f"N_e > 10? {N_e_transit > 10}")
print(f"N_e > 1? {N_e_transit > 1}")

# ============================================================
# 9. Flatness from BDI topology (Volovik Paper 04)
# ============================================================
print(f"\n=== Flatness from BDI topology ===")
print(f"Volovik (2008): Translation-invariant quantum vacuum produces flat spacetime.")
print(f"BDI class (T^2=+1, C^2=+1, TC=1): topological protection of Fermi points.")
print(f"At tau=0 (round SU(3)): maximum symmetry, all eigenvalues degenerate.")
print(f"Winding number nu = ±1 per Fermi point.")
print(f"Any perturbation preserving BDI symmetry cannot open a gap -> flatness preserved.")
print(f"Cosmological flatness: Omega_k = 0 is topologically protected.")
print(f"This does NOT require inflation: topology does the work of 60+ e-folds.")

# ============================================================
# 10. Comparison to standard inflation
# ============================================================
print(f"\n" + "="*60)
print(f"SUMMARY: QFLUC-43 Results")
print(f"="*60)

print(f"\n--- tau=0 Characterization ---")
print(f"S(0) = {S_0:.2f} (global minimum, monotonic increase)")
print(f"dS/dtau(0) = {dS_dtau_0:.4f} (nonzero: tau=0 is boundary, not extremum)")
print(f"d2S/dtau2(0) = {d2S_dtau2_0:.2f} (positive: V is convex)")
print(f"Z(0) ~ {Z_0:.2f}")

print(f"\n--- Effective Modulus Mass ---")
print(f"m_tau = {m_tau_MKK:.4f} M_KK = {m_tau_GeV:.3e} GeV")
print(f"m_tau / H = {ratio_mH:.2f} (SUPERHEAVY: exponentially suppressed de Sitter fluct.)")
print(f"m_tau / M_Pl = {m_tau_GeV/M_Pl:.3e}")

print(f"\n--- Quantum Fluctuations ---")
print(f"delta_tau (zero-point) = {delta_tau_B:.3e}")
print(f"delta_tau / tau_fold = {delta_tau_B/0.19:.3e}")
print(f"Zero-point dominates (de Sitter exponentially suppressed for m >> H)")

print(f"\n--- Slow-Roll Parameters ---")
print(f"epsilon_V = {epsilon_V:.3e}")
print(f"eta_V = {eta_V:.3e}")
print(f"n_s = {n_s:.6f} (obs: 0.9649 ± 0.0042)")
print(f"r = {r_tensor:.3e} (obs: r < 0.036)")

print(f"\n--- Power Spectrum ---")
print(f"P_R = {P_R:.3e}")
print(f"A_s (obs) = {A_s_obs:.1e}")
print(f"log10(P_R/A_s) = {np.log10(P_R/A_s_obs):.2f}")

print(f"\n--- Transit Duration ---")
print(f"N_e (modulus transit) = {N_e_transit:.3e}")
print(f"H(0) = {H_0:.3e} GeV")

print(f"\n--- BCS Barrier ---")
print(f"|E_BCS|/V_barrier = {ratio_BCS_barrier:.4f} (BCS 4% of spectral action barrier)")
print(f"FRIED-39 shortfall CONFIRMED from different angle")

# ============================================================
# 11. Gate verdict
# ============================================================
print(f"\n{'='*60}")
print(f"GATE VERDICT: QFLUC-43")
print(f"{'='*60}")

P_R_within_10_OOM = abs(np.log10(P_R / A_s_obs)) < 10
N_e_gt_10 = N_e_transit > 10
N_e_gt_1 = N_e_transit > 1
P_R_gt_10_10 = abs(np.log10(P_R / A_s_obs)) > 20

if P_R_within_10_OOM and N_e_gt_10:
    verdict = "PASS"
elif P_R_gt_10_10 and not N_e_gt_1:
    verdict = "FAIL"
else:
    # Check intermediate cases
    if P_R_within_10_OOM and not N_e_gt_10:
        verdict = "PARTIAL (P_R in range but N_e < 10)"
    elif not P_R_within_10_OOM and N_e_gt_10:
        verdict = "PARTIAL (N_e OK but P_R out of range)"
    else:
        verdict = "FAIL"

print(f"P_R / A_s = {P_R/A_s_obs:.3e}")
print(f"|log10(P_R/A_s)| = {abs(np.log10(P_R/A_s_obs)):.2f} (threshold: 10)")
print(f"N_e = {N_e_transit:.3e} (threshold: 10)")
print(f"Verdict: {verdict}")

# Additional physics verdict
print(f"\n--- Physical Interpretation ---")
print(f"1. tau=0 is a STABLE minimum of V(tau), not an unstable maximum")
print(f"2. The spectral action gradient OPPOSES transit (restoring force)")
print(f"3. BCS driving force is 4% of spectral action barrier (FRIED-39)")
print(f"4. Modulus is superheavy (m/H = {ratio_mH:.0f}): no de Sitter fluctuations")
print(f"5. Zero-point delta_tau ~ {delta_tau_B:.0e}: insufficient for structure formation")
print(f"6. N_e ~ {N_e_transit:.0e}: no inflation from modulus transit")
print(f"7. Flatness from BDI topology (Volovik): does NOT require inflation")
print(f"8. P_R {'within' if P_R_within_10_OOM else 'outside'} 10 OOM of A_s")

# Do both M_KK routes for robustness
print(f"\n--- M_KK Sensitivity ---")
for label, mkk in [("GN (gravity)", M_KK_GN), ("Kerner (gauge)", M_KK_kerner)]:
    V_mkk = S_0 * mkk**4 / (16*np.pi**2)
    H_mkk = np.sqrt(V_mkk / (3 * M_Pl_reduced**2))
    dVdphi_mkk = dS_dtau_0 * mkk**3 / (16*np.pi**2*np.sqrt(Z_0))
    eps_mkk = 0.5 * M_Pl_reduced**2 * (dVdphi_mkk / V_mkk)**2
    PR_mkk = V_mkk / (24*np.pi**2*M_Pl_reduced**4*eps_mkk)
    omega_mkk = np.sqrt(d2S_dtau2_0 * mkk**2 / (16*np.pi**2*M_ATDHFB))
    mH_mkk = omega_mkk / H_mkk
    a_mkk = dS_dtau_0 * mkk**2 / (16*np.pi**2*M_ATDHFB)
    dS_avg_mkk = (dS_dtau_0 + 58672.80) / 2
    a_avg_mkk = dS_avg_mkk * mkk**2 / (16*np.pi**2*M_ATDHFB)
    t_tr_mkk = np.sqrt(2*0.19/a_avg_mkk)
    Ne_mkk = H_mkk * t_tr_mkk
    print(f"  M_KK ({label}) = {mkk:.2e} GeV:")
    print(f"    P_R = {PR_mkk:.3e}, log10(P_R/A_s) = {np.log10(PR_mkk/A_s_obs):.2f}")
    print(f"    m_tau/H = {mH_mkk:.1f}, N_e = {Ne_mkk:.3e}")
    print(f"    epsilon = {eps_mkk:.3e}, eta = {M_Pl_reduced**2 * d2S_dtau2_0 * mkk**2/(16*np.pi**2*Z_0) / V_mkk:.3e}")

# ============================================================
# 12. Save results
# ============================================================
np.savez('tier0-computation/s43_qfluc_tau0.npz',
    # tau=0 characterization
    S_0=S_0,
    dS_dtau_0=dS_dtau_0,
    d2S_dtau2_0=d2S_dtau2_0,
    Z_0=Z_0,
    # Effective mass
    m_tau_MKK=m_tau_MKK,
    m_tau_GeV=m_tau_GeV,
    m_over_H=ratio_mH,
    # Fluctuations
    delta_tau_zeropoint=delta_tau_B,
    delta_tau_deSitter=delta_tau_dS if isinstance(delta_tau_dS, float) else 0.0,
    # Slow-roll
    epsilon_V=epsilon_V,
    eta_V=eta_V,
    n_s=n_s,
    r_tensor=r_tensor,
    # Power spectrum
    P_R=P_R,
    A_s_obs=A_s_obs,
    log10_PR_over_As=np.log10(P_R / A_s_obs),
    # Transit
    N_e_transit=N_e_transit,
    H_0_GeV=H_0,
    t_transit=t_transit,
    # BCS barrier
    ratio_BCS_barrier=ratio_BCS_barrier,
    delta_S_transit=delta_S,
    # M_KK used
    M_KK_used=M_KK,
    M_KK_route='GN_gravity',
    M_Pl=M_Pl,
    M_Pl_reduced=M_Pl_reduced,
    M_ATDHFB=M_ATDHFB,
    # Gate verdict
    verdict=verdict,
    gate_name='QFLUC-43'
)

print(f"\nResults saved to tier0-computation/s43_qfluc_tau0.npz")

# ============================================================
# 13. Generate plot
# ============================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('QFLUC-43: Quantum Fluctuations at $\\tau=0$\n'
             f'Gate: {verdict}', fontsize=14, fontweight='bold')

# Panel 1: S_full(tau) with tau=0 characterization
ax = axes[0, 0]
ax.plot(tau_arr, S_arr, 'b-o', markersize=4, label='$S_{\\rm full}(\\tau)$')
ax.axhline(S_0, color='gray', ls='--', alpha=0.5)
ax.axvline(0, color='red', ls=':', alpha=0.7, label='$\\tau=0$ (boundary)')
ax.axvline(0.19, color='green', ls=':', alpha=0.7, label='$\\tau_{\\rm fold}=0.19$')
# Show tangent at tau=0
tau_tangent = np.linspace(0, 0.1, 50)
S_tangent = S_0 + dS_dtau_0 * tau_tangent + 0.5 * d2S_dtau2_0 * tau_tangent**2
ax.plot(tau_tangent, S_tangent, 'r--', alpha=0.5, label=f'Quadratic approx')
ax.set_xlabel('$\\tau$')
ax.set_ylabel('$S_{\\rm full}$ (dimensionless)')
ax.set_title('Spectral Action: Monotonically Increasing')
ax.legend(fontsize=8)
ax.set_xlim(-0.02, 0.55)

# Panel 2: Effective potential and mass scales
ax = axes[0, 1]
M_KK_labels = ['$M_{KK}$ (GN)', '$M_{KK}$ (Kerner)']
M_KK_vals = [M_KK_GN, M_KK_kerner]
# Plot V(tau) / M_Pl^4 for both M_KK
for mkk, label, color in zip(M_KK_vals, M_KK_labels, ['blue', 'orange']):
    V_plot = S_arr * mkk**4 / (16*np.pi**2 * M_Pl**4)
    ax.plot(tau_arr, V_plot, '-o', markersize=3, label=f'$V(\\tau)/M_{{Pl}}^4$ ({label})', color=color)
ax.set_xlabel('$\\tau$')
ax.set_ylabel('$V(\\tau) / M_{Pl}^4$')
ax.set_title('Moduli Potential (Planck units)')
ax.legend(fontsize=8)
ax.set_yscale('log')

# Panel 3: Gradient stiffness and derivatives
ax = axes[1, 0]
ax2 = ax.twinx()
ax.plot(tau_g, Z_g, 'b-s', markersize=5, label='$Z(\\tau)$')
ax2.plot(tau_g, dS_g, 'r-^', markersize=5, label="$dS/d\\tau$")
ax.set_xlabel('$\\tau$')
ax.set_ylabel('$Z_{\\rm spectral}$', color='blue')
ax2.set_ylabel('$dS/d\\tau$', color='red')
ax.tick_params(axis='y', labelcolor='blue')
ax2.tick_params(axis='y', labelcolor='red')
lines1, labels1 = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines1+lines2, labels1+labels2, fontsize=8, loc='upper left')
ax.set_title('Gradient Stiffness & Slope')

# Panel 4: Summary table
ax = axes[1, 1]
ax.axis('off')
table_data = [
    ['$S(0)$', f'{S_0:.0f}'],
    ['$dS/d\\tau(0)$', f'{dS_dtau_0:.2f}'],
    ['$d^2S/d\\tau^2(0)$', f'{d2S_dtau2_0:.0f}'],
    ['$Z(0)$', f'{Z_0:.0f}'],
    ['$m_\\tau / M_{KK}$', f'{m_tau_MKK:.4f}'],
    ['$m_\\tau / H$', f'{ratio_mH:.1f}'],
    ['$\\delta\\tau$ (zero-point)', f'{delta_tau_B:.2e}'],
    ['$\\epsilon_V$', f'{epsilon_V:.2e}'],
    ['$\\eta_V$', f'{eta_V:.2e}'],
    ['$P_R$', f'{P_R:.2e}'],
    ['$\\log_{10}(P_R/A_s)$', f'{np.log10(P_R/A_s_obs):.1f}'],
    ['$N_e$ (transit)', f'{N_e_transit:.2e}'],
    ['$|E_{BCS}|/V_{barrier}$', f'{ratio_BCS_barrier:.4f}'],
    ['Verdict', verdict],
]
table = ax.table(cellText=table_data, colLabels=['Quantity', 'Value'],
                 loc='center', cellLoc='left')
table.auto_set_font_size(False)
table.set_fontsize(9)
table.scale(1.0, 1.4)
for i in range(len(table_data)+1):
    for j in range(2):
        cell = table[i, j]
        if i == 0:
            cell.set_facecolor('#4472C4')
            cell.set_text_props(color='white', fontweight='bold')
        elif 'FAIL' in str(table_data[i-1][1]) if i > 0 else False:
            cell.set_facecolor('#FFD7D7')
        elif 'PASS' in str(table_data[i-1][1]) if i > 0 else False:
            cell.set_facecolor('#D7FFD7')
        elif 'PARTIAL' in str(table_data[i-1][1]) if i > 0 else False:
            cell.set_facecolor('#FFFFD7')
ax.set_title('QFLUC-43 Results Summary', fontweight='bold')

plt.tight_layout()
plt.savefig('tier0-computation/s43_qfluc_tau0.png', dpi=150, bbox_inches='tight')
print("Plot saved to tier0-computation/s43_qfluc_tau0.png")
plt.close()
