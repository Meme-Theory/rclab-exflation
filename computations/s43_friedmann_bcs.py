"""
s43_friedmann_bcs.py — Coupled Friedmann-BCS epsilon_H During Transition
=========================================================================

GATE: FRIEDMANN-BCS-43 (INFO)

Computes the slow-roll parameter epsilon_H = -dH/dt / H^2 during the
fold transit (tau = 0.05 to 0.30) using a coupled Friedmann-BCS solver.

Physics:
  - The spectral action S_full(tau) defines V(tau) = S_full(tau) * M_KK^4 / (16*pi^2)
  - S_full is monotonically increasing (CUTOFF-SA-37 theorem)
  - V(tau=0) is the global MINIMUM, NOT a maximum
  - The BCS instability drives the transit; spectral action is a restoring force
  - FRIED-39: gradient ratio |dV/dtau| / |dE_BCS/dtau| = 6596 at fold
  - M_ATDHFB = 1.695 (collective inertia from S40)
  - M_KK = 7.43e16 GeV (gravity route, s42_constants_snapshot)

Coupled ODEs in natural units (hbar = c = 1, M_KK = 1):
  (1) tau_ddot + 3*H*tau_dot + dV_eff/dtau = 0
  (2) H^2 = (8*pi/(3*M_Pl^2)) * [(1/2)*M_ATDHFB*tau_dot^2 + V(tau)]

where V_eff = V_SA + V_BCS, dV_SA/dtau = (dS/dtau)*M_KK^4/(16*pi^2),
and V_BCS is the BCS condensation energy (6e-7 of V_SA).

Initial condition: tau_dot from energy balance (all energy in kinetic
at tau=0.05, or from transit velocity estimate).

Two scenarios:
  A) BCS-driven transit: initial tau_dot = dS/dtau / M_ATDHFB
     (instantaneous BCS force balance, S39 formula)
  B) Energy-conserving: tau_dot from constant total energy
"""

import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import CubicSpline
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ==============================================================
# 1. LOAD DATA
# ==============================================================

d_s36 = np.load('tier0-computation/s36_sfull_tau_stabilization.npz', allow_pickle=True)
d_s42g = np.load('tier0-computation/s42_gradient_stiffness.npz', allow_pickle=True)
d_s40 = np.load('tier0-computation/s40_collective_inertia.npz', allow_pickle=True)
d_s42c = np.load('tier0-computation/s42_constants_snapshot.npz', allow_pickle=True)

# S_full(tau) data — 16 tau points
tau_s36 = d_s36['tau_combined']
S_full_s36 = d_s36['S_full']

# Gradient stiffness — 10 tau points
tau_g = d_s42g['tau_grid']
dS_dtau_g = d_s42g['dS_dtau']
d2S_dtau2_g = d_s42g['d2S_dtau2']
Z_g = d_s42g['Z_spectral']
S_total_g = d_s42g['S_total']

# Collective inertia
M_ATDHFB = float(d_s40['M_ATDHFB_TOTAL'])

# KK mass scale
M_KK_GeV = float(d_s42c['M_KK_from_GN'])  # 7.43e16 GeV
from canonical_constants import M_Pl_unreduced as M_Pl_GeV  # reduced -> unreduced (1.22e19)

# Derived: M_Pl in units of M_KK
M_Pl_MKK = M_Pl_GeV / M_KK_GeV

print("=" * 70)
print("FRIEDMANN-BCS-43: Coupled Friedmann-BCS epsilon_H During Transit")
print("=" * 70)
print(f"\nM_ATDHFB     = {M_ATDHFB:.4f}")
print(f"M_KK         = {M_KK_GeV:.4e} GeV")
print(f"M_Pl         = {M_Pl_GeV:.4e} GeV")
print(f"M_Pl/M_KK    = {M_Pl_MKK:.4f}")
print(f"(M_Pl/M_KK)^2 = {M_Pl_MKK**2:.2f}")

# ==============================================================
# 2. BUILD INTERPOLANTS
# ==============================================================

# Cubic spline for S_full(tau) — use the 16-point s36 data
cs_S = CubicSpline(tau_s36, S_full_s36)

# Derivative dS/dtau from the spline (cross-check with s42g data)
cs_dS = cs_S.derivative(1)
cs_d2S = cs_S.derivative(2)

print("\n--- Spline Cross-Check at fold tau=0.19 ---")
print(f"S_spline(0.19)   = {cs_S(0.19):.2f}  vs S_fold = {d_s42g['S_fold'].item():.2f}")
print(f"dS_spline(0.19)  = {cs_dS(0.19):.2f}  vs dS_fold = {d_s42g['dS_fold'].item():.2f}")
print(f"d2S_spline(0.19) = {cs_d2S(0.19):.2f}  vs d2S_fold = {d_s42g['d2S_fold'].item():.2f}")

# ==============================================================
# 3. POTENTIAL V(tau) in Planck units
# ==============================================================

# V(tau) = S(tau) * M_KK^4 / (16*pi^2)
# In reduced Planck units: V/M_Pl^4 = S(tau) / (16*pi^2) * (M_KK/M_Pl)^4
prefactor = 1.0 / (16.0 * np.pi**2)
MKK_over_MPl = M_KK_GeV / M_Pl_GeV
scale4 = MKK_over_MPl**4

print(f"\nPrefactor = 1/(16*pi^2) = {prefactor:.6e}")
print(f"M_KK/M_Pl = {MKK_over_MPl:.6e}")
print(f"(M_KK/M_Pl)^4 = {scale4:.6e}")

def V_Pl(tau):
    """Potential in Planck units (V/M_Pl^4)"""
    return cs_S(tau) * prefactor * scale4

def dV_dtau_Pl(tau):
    """dV/dtau in Planck units"""
    return cs_dS(tau) * prefactor * scale4

def d2V_dtau2_Pl(tau):
    """d2V/dtau2 in Planck units"""
    return cs_d2S(tau) * prefactor * scale4

# Test
V0 = V_Pl(0.0)
V_fold = V_Pl(0.19)
dV_fold = dV_dtau_Pl(0.19)

print(f"\nV(0)/M_Pl^4     = {V0:.6e}")
print(f"V(fold)/M_Pl^4  = {V_fold:.6e}")
print(f"dV/dtau(fold)/M_Pl^4 = {dV_fold:.6e}")

# BCS condensation energy for comparison (S36 ED-CONV-36: E_cond = -0.137 in M_KK units)
from canonical_constants import E_cond as E_BCS_MKK  # was -0.115
V_BCS_Pl = E_BCS_MKK * scale4  # in M_Pl^4
print(f"\nE_BCS/M_Pl^4    = {V_BCS_Pl:.6e}")
print(f"|E_BCS|/V(fold)  = {abs(V_BCS_Pl)/V_fold:.6e}")

# ==============================================================
# 4. COLLECTIVE MASS IN PLANCK UNITS
# ==============================================================

# The ATDHFB mass is in M_KK units:
#   L = (1/2) * M_ATDHFB * tau_dot^2 [in M_KK^4]
# Convert to Planck units:
#   L/M_Pl^4 = (1/2) * M_ATDHFB * (M_KK/M_Pl)^4 * tau_dot^2
# Effective mass in Planck units:
M_eff_Pl = M_ATDHFB * scale4

print(f"\nM_ATDHFB (M_KK units) = {M_ATDHFB:.4f}")
print(f"M_eff (Planck units)  = {M_eff_Pl:.6e}")

# Check: canonical field phi = sqrt(M_eff_Pl) * tau (for phi in Planck units)
# Slow-roll: epsilon_V = (1/2) * (V'/V)^2 * (1/M_eff_Pl)
# In canonical form: epsilon_V = (1/2) * (dV/dphi / V)^2 = (1/2) * (dV/dtau)^2 / (M_eff_Pl * V^2)

epsilon_V_fold = 0.5 * (dV_fold)**2 / (M_eff_Pl * V_fold**2)
print(f"\nepsilon_V(fold) = {epsilon_V_fold:.6e}")
# Cross-check: W1-8 gives epsilon_V(0) = 2.6e-12

epsilon_V_0 = 0.5 * dV_dtau_Pl(0.0)**2 / (M_eff_Pl * V_Pl(0.0)**2)
print(f"epsilon_V(0)    = {epsilon_V_0:.6e}")

eta_V_fold = d2V_dtau2_Pl(0.19) / (M_eff_Pl * V_fold)
print(f"eta_V(fold)     = {eta_V_fold:.6e}")

# ==============================================================
# 5. COUPLED FRIEDMANN-BCS ODEs
# ==============================================================

# State vector: y = [tau, tau_dot]
# Time is in Planck units (t * M_Pl)
#
# Friedmann: H^2 = (1/3) * [(1/2)*M_eff_Pl * tau_dot^2 + V_Pl(tau)]
#   (using 8*pi*G = 8*pi/M_Pl^2 = 1/M_Pl^2 in reduced Planck units,
#    so H^2 = rho/(3*M_Pl^2) but with rho already in M_Pl^4 units,
#    H^2 = rho/3 where rho is in M_Pl^4/M_Pl^2 = M_Pl^2 ...
#    Let me be careful.)
#
# In NATURAL units with M_Pl = 1:
#   H^2 = rho/3 where rho = (1/2)*M_eff*tau_dot^2 + V
#   tau_ddot + 3*H*tau_dot + (1/M_eff)*dV/dtau = 0
#
# But M_eff is tiny (scale4 ~ 10^{-8}), so tau_dot can be large.
#
# Actually, let's work in M_KK units throughout and convert at end.
# In M_KK units:
#   V(tau) = S(tau) / (16*pi^2)   [in M_KK^4]
#   rho = (1/2)*M_ATDHFB*tau_dot^2 + V(tau)  [in M_KK^4]
#   H^2 = (8*pi/(3*M_Pl^2)) * rho
#        = (8*pi/3) * (M_KK/M_Pl)^2 * (rho in M_KK^4 / M_KK^2)
#        ... this is getting confusing. Let me be very explicit.
#
# Working in units where M_KK = 1:
#   [V] = M_KK^4, [rho] = M_KK^4, [M_ATDHFB] = dimensionless (M_KK^4 / M_KK^2 = M_KK^2? No.)
#
# Actually: the spectral action S(tau) is dimensionless.
# The physical potential energy density is V = S(tau) * Lambda^4 / (16*pi^2)
# where Lambda is the cutoff scale ~ M_KK.
# The kinetic energy density is T = (1/2) * M_ATDHFB * tau_dot^2 * Lambda^4 / (16*pi^2)
# where M_ATDHFB is dimensionless.
#
# So rho = [S(tau) + (1/2)*M_ATDHFB*tau_dot^2] * M_KK^4 / (16*pi^2)
#
# Friedmann: H^2 = (8*pi*G/3) * rho = (8*pi/(3*M_Pl^2)) * rho
#            = (8*pi/(3*M_Pl^2)) * [S + (1/2)*M*tau_dot^2] * M_KK^4/(16*pi^2)
#            = (M_KK^4/(6*pi*M_Pl^2)) * [S + (1/2)*M*tau_dot^2]
#
# Time in natural units (hbar/M_KK):
#   H has units of M_KK, t has units of 1/M_KK.
#   H^2 = (M_KK^2/(6*pi)) * (M_KK/M_Pl)^2 * [S + (1/2)*M*tau_dot^2]
#
# Let me define everything in M_KK units:
#   H_MKK = H / M_KK (dimensionless)
#   t_MKK = t * M_KK (dimensionless)
#   tau_dot_MKK = d(tau)/d(t_MKK) (dimensionless)
#
# Then: H_MKK^2 = (1/(6*pi)) * (M_KK/M_Pl)^2 * [S(tau) + (1/2)*M_ATDHFB*tau_dot_MKK^2]
#
# Note: the 1/(16*pi^2) prefactor from the spectral action normalization
# should be included. Let me define:
#   V_dimless(tau) = S(tau) / (16*pi^2)
# Then:
#   rho_MKK4 = [V_dimless + (1/2)*(M_ATDHFB/(16*pi^2))*tau_dot^2] * (M_KK^4)
# Hmm, the mass parameter M_ATDHFB should also be in the same normalization.
#
# Let me follow the S43 working paper convention.
# From W1-8: rho(0)/M_Pl^4 = 2.1e-6, H(0) = 5.15e16 GeV.
# H(0) = sqrt(rho/3) (in Planck units)
# H(0)/M_Pl = sqrt(rho/M_Pl^4 / 3) = sqrt(2.1e-6/3) = 8.37e-4
# H(0) = 8.37e-4 * M_Pl = 8.37e-4 * 2.435e18 = 2.04e15 GeV
# But W1-8 says H(0) = 5.15e16 GeV.
# H(0)/M_Pl = 5.15e16 / 2.435e18 = 0.02115
# Then rho/M_Pl^4 = 3*H^2/M_Pl^2 = 3*(0.02115)^2 = 1.34e-3
# Hmm, discrepancy with the stated 2.1e-6.
#
# Let me just compute everything self-consistently.

# WORK IN M_KK = 1 UNITS.
# Define alpha_G = (M_KK/M_Pl)^2

alpha_G = (M_KK_GeV / M_Pl_GeV)**2
print(f"\nalpha_G = (M_KK/M_Pl)^2 = {alpha_G:.6e}")

# Spectral action normalization:
# The physical energy density is:
#   rho = S(tau) * f_0 * Lambda^4 / (2*pi^2)  (Chamseddine-Connes convention)
# where f_0 = f(0) is the zeroth moment of the cutoff function.
# We set Lambda = M_KK and f_0 = 1 (standard convention).
# Actually, from the working paper: V(tau) = S(tau) * M_KK^4 / (16*pi^2)
# Let's use that.

pf = 1.0 / (16.0 * np.pi**2)

# V(tau) in M_KK^4 units
def V_MKK4(tau):
    return cs_S(tau) * pf

def dV_dtau_MKK4(tau):
    return cs_dS(tau) * pf

V0_MKK4 = V_MKK4(0.0)
V_fold_MKK4 = V_MKK4(0.19)
print(f"\nV(0) = {V0_MKK4:.2f} M_KK^4")
print(f"V(fold) = {V_fold_MKK4:.2f} M_KK^4")
print(f"dV/dtau(fold) = {dV_dtau_MKK4(0.19):.2f} M_KK^4")

# Friedmann in M_KK units:
#   H^2 = (8*pi*G_N / 3) * rho
#        = (8*pi/(3*M_Pl^2)) * rho
# where rho and H are in physical units.
# In M_KK units (H_MKK = H/M_KK, rho = rho_MKK4 * M_KK^4):
#   (H_MKK * M_KK)^2 = (8*pi/(3*M_Pl^2)) * rho_MKK4 * M_KK^4
#   H_MKK^2 = (8*pi/3) * (M_KK/M_Pl)^2 * rho_MKK4
#            = (8*pi/3) * alpha_G * rho_MKK4

friedmann_coeff = (8.0 * np.pi / 3.0) * alpha_G
print(f"\nFriedmann coefficient = (8*pi/3)*alpha_G = {friedmann_coeff:.6e}")

# H at tau=0:
rho_0 = V0_MKK4  # at rest, all potential
H_0_MKK = np.sqrt(friedmann_coeff * rho_0)
H_0_GeV = H_0_MKK * M_KK_GeV
print(f"\nH(tau=0) = {H_0_MKK:.6e} M_KK = {H_0_GeV:.4e} GeV")

# Cross-check with W1-8: H(0) = 5.15e16 GeV
print(f"W1-8 stated: H(0) = 5.15e16 GeV")

# Klein-Gordon equation for tau:
# M_ATDHFB appears in the kinetic term: T = (1/2)*M_ATDHFB*(dtau/dt)^2 * pf * M_KK^4
# Wait -- is M_ATDHFB already included in the spectral action S_full?
#
# From S40: the ATDHFB mass is a second-order response coefficient.
# The kinetic energy of the modulus is T = (1/2)*M_ATDHFB*(dtau/dt)^2
# in units of M_KK^4 (since M_ATDHFB is dimensionless in M_KK units
# and tau is dimensionless). But this should be multiplied by the same
# pf to get physical energy density.
#
# Actually: the key question is the correct normalization.
# From the working paper line 567: "Transit velocity dtau/dt = dS/dtau / M_ATDHFB = 34,615"
# This implies the EOM is: M_ATDHFB * d^2tau/dt^2 = -dS/dtau (in M_KK = 1 units)
# where the driving force is the SPECTRAL ACTION GRADIENT dS/dtau, not dV/dtau.
# So the pf = 1/(16*pi^2) cancels between kinetic and potential terms.
#
# The Friedmann equation uses:
#   rho = [(1/2)*M_ATDHFB*tau_dot^2 + S(tau)] * M_KK^4 / (16*pi^2)
# or equivalently:
#   rho_reduced = (1/2)*M_ATDHFB*tau_dot^2 + S(tau)  [dimensionless]
#   rho_phys = rho_reduced * pf * M_KK^4

# So in M_KK units with the pf absorbed:
# H_MKK^2 = (8*pi/3) * alpha_G * [(1/2)*M_ATDHFB*tau_dot^2 + S(tau)] * pf
#          = friedmann_coeff * pf * [(1/2)*M_ATDHFB*tau_dot^2 + S(tau)]

FC = friedmann_coeff * pf
print(f"\nFC = (8*pi/3)*alpha_G/(16*pi^2) = {FC:.6e}")

# Recompute H(0):
H_0_MKK_v2 = np.sqrt(FC * cs_S(0.0))
H_0_GeV_v2 = H_0_MKK_v2 * M_KK_GeV
print(f"H(0) = {H_0_MKK_v2:.6e} M_KK = {H_0_GeV_v2:.4e} GeV")

# EOM for tau (with Hubble friction):
# M_ATDHFB * tau_ddot + 3*H*M_ATDHFB*tau_dot + dS/dtau = 0
# tau_ddot = -(3*H*tau_dot + dS/dtau / M_ATDHFB)
#
# But wait: the Hubble friction term should come from the covariant
# conservation of energy. For a scalar field with non-canonical kinetic term:
# (d/dt)(rho) + 3*H*(rho + P) = 0
# For KG: rho = T + V, P = T - V, rho+P = 2T
# So: T_dot + V_dot + 6*H*T = 0
# M*tau_dot*tau_ddot + (dV/dtau)*tau_dot + 6*H*(1/2)*M*tau_dot^2 = 0
# Dividing by M*tau_dot:
# tau_ddot + (1/M)*dV/dtau + 3*H*tau_dot = 0
#
# Equivalently: tau_ddot = -(1/M)*dS/dtau - 3*H*tau_dot
# where V = S * pf * M_KK^4 and the M in the canonical equation should be
# M_ATDHFB (already in the proper normalization since pf cancels).

# ==============================================================
# 6. SOLVE THE COUPLED SYSTEM
# ==============================================================

def coupled_odes(t, y):
    """
    y = [tau, tau_dot]
    Returns [tau_dot, tau_ddot]
    Time t in units of 1/M_KK
    """
    tau_val, tau_dot_val = y

    # Clamp tau to interpolation range
    tau_clamped = np.clip(tau_val, 0.0, 0.5)

    S_val = float(cs_S(tau_clamped))
    dS_val = float(cs_dS(tau_clamped))

    # Energy density (dimensionless, S-units)
    rho_dimless = 0.5 * M_ATDHFB * tau_dot_val**2 + S_val

    # Hubble parameter
    H2 = FC * rho_dimless
    if H2 < 0:
        H2 = 0.0
    H_val = np.sqrt(H2)

    # tau equation of motion
    tau_ddot_val = -dS_val / M_ATDHFB - 3.0 * H_val * tau_dot_val

    return [tau_dot_val, tau_ddot_val]

# -------------------------------------------------------------------
# SCENARIO A: BCS-driven transit
# Initial condition: tau_dot from BCS instability
# From S39: dtau/dt = dS/dtau / M_ATDHFB at fold
# But at early tau, the transit velocity is set by the BCS driving.
# The BCS force balances the SA gradient locally, giving:
# tau_dot ~ (dS/dtau) / (M_ATDHFB * something)
#
# Actually, the issue is: what drives tau?
# S_full is monotonically INCREASING. dS/dtau > 0 at all tau.
# So dV/dtau > 0: the potential pushes tau BACK toward 0.
# The BCS instability provides a force in the +tau direction.
# But |dE_BCS/dtau| / |dS/dtau| = 1/6596 at the fold.
#
# In the S39 computation: the transit velocity was estimated as
# dtau/dt = dS/dtau / M_ATDHFB, which would correspond to a
# FORCE BALANCE where something provides the energy to climb.
# But that doesn't make mechanical sense with Hubble friction.
#
# Let me reconsider: the transit is driven by the BCS INSTABILITY.
# At tau=0, the round SU(3) geometry is unstable to BCS pairing.
# The BCS condensation energy E_cond = -0.115 M_KK^4 provides
# a small negative contribution to the effective potential.
# The total effective potential is V_eff = S(tau)/(16pi^2) + E_BCS(tau)/(16pi^2)
# but E_BCS is 6e-7 of S_full, so V_eff ~ S/(16pi^2) to excellent approximation.
#
# The STRUCTURAL result from S39 (FRIED-39):
# The modulus cannot be stabilized at the fold. It transits ballistically.
# Total N_e during transit = 0.041.
#
# Let me just solve the Friedmann-KG system with V = S(tau)*pf*M_KK^4
# and see what epsilon_H comes out.
#
# For the initial condition at tau=0.05:
# CASE 1: Start at rest (tau_dot = 0). But then dS/dtau > 0 pushes tau
#          BACK toward 0. No transit.
# CASE 2: Start with positive tau_dot sufficient to reach fold.
#          Energy conservation: (1/2)*M*tau_dot_0^2 = S(fold) - S(0.05) = Delta_S.
#          tau_dot_0 = sqrt(2*Delta_S/M)
# CASE 3: Start from tau=0 with a BCS-driven kick.
#          The BCS instability supplies the energy to climb from S(0) to S(fold).
# -------------------------------------------------------------------

# CASE 2: Energy-conserving (all kinetic to potential conversion)
# This gives a LOWER BOUND on tau_dot (just enough to reach fold)
Delta_S_05_fold = float(cs_S(0.30)) - float(cs_S(0.05))
tau_dot_min = np.sqrt(2.0 * Delta_S_05_fold / M_ATDHFB)
print(f"\n--- Initial Conditions ---")
print(f"S(0.05) = {cs_S(0.05):.2f}")
print(f"S(0.30) = {cs_S(0.30):.2f}")
print(f"Delta_S(0.05->0.30) = {Delta_S_05_fold:.2f}")
print(f"tau_dot_min (energy conservation, no friction) = {tau_dot_min:.2f}")

# CASE 3: S39 transit velocity at fold
tau_dot_S39 = float(cs_dS(0.19)) / M_ATDHFB
print(f"tau_dot(S39 transit at fold) = {tau_dot_S39:.2f}")

# The S39 velocity is MUCH larger than the minimum. This means the
# kinetic energy far exceeds Delta_S. In the S39 picture, the BCS
# instability pumps energy continuously.

# Let me try multiple scenarios:

print("\n" + "=" * 70)
print("SCENARIO SWEEP")
print("=" * 70)

tau_start = 0.05
tau_end = 0.30
tau_fold = 0.19

results = {}

# For each scenario, solve and extract epsilon_H
scenarios = {
    'A_S39_velocity': tau_dot_S39,
    'B_energy_conserving': tau_dot_min,
    'C_10x_minimum': 10.0 * tau_dot_min,
    'D_100x_minimum': 100.0 * tau_dot_min,
    'E_half_S39': 0.5 * tau_dot_S39,
}

# Also compute without Hubble friction to see its effect
for name, tau_dot_init in scenarios.items():
    print(f"\n--- Scenario {name}: tau_dot_0 = {tau_dot_init:.2f} ---")

    y0 = [tau_start, tau_dot_init]

    # Initial H
    rho0 = 0.5 * M_ATDHFB * tau_dot_init**2 + float(cs_S(tau_start))
    H0 = np.sqrt(FC * rho0)
    print(f"  H_0 = {H0:.6e} M_KK = {H0 * M_KK_GeV:.4e} GeV")
    print(f"  rho_0 = {rho0:.2f} (S-units)")
    print(f"  KE/PE = {0.5*M_ATDHFB*tau_dot_init**2/float(cs_S(tau_start)):.4f}")

    # Estimate transit time
    t_transit_est = (tau_end - tau_start) / tau_dot_init
    t_span = (0, 5.0 * t_transit_est)  # give 5x margin

    # Dense output for smooth epsilon_H
    t_eval = np.linspace(0, 5.0 * t_transit_est, 20000)

    # Event: tau reaches tau_end
    def event_end(t, y):
        return y[0] - tau_end
    event_end.terminal = True
    event_end.direction = 1

    # Event: tau returns to 0
    def event_zero(t, y):
        return y[0]
    event_zero.terminal = True
    event_zero.direction = -1

    sol = solve_ivp(coupled_odes, t_span, y0, method='RK45',
                    events=[event_end, event_zero],
                    t_eval=t_eval, rtol=1e-12, atol=1e-15,
                    max_step=t_transit_est/1000)

    t = sol.t
    tau_arr = sol.y[0]
    tau_dot_arr = sol.y[1]

    # Compute H(t), epsilon_H(t)
    S_arr = np.array([float(cs_S(np.clip(tv, 0.0, 0.5))) for tv in tau_arr])
    dS_arr = np.array([float(cs_dS(np.clip(tv, 0.0, 0.5))) for tv in tau_arr])

    rho_arr = 0.5 * M_ATDHFB * tau_dot_arr**2 + S_arr
    H_arr = np.sqrt(FC * np.maximum(rho_arr, 0.0))

    # H_dot from: H_dot = -(1/2) * FC * M_ATDHFB * tau_dot^2
    # (this follows from Friedmann + continuity: H_dot = -(4piG/c^2)(rho + P)
    #  = -(1/2)*(8piG/c^2)*2T = -FC * M_ATDHFB * tau_dot^2 / 2)
    # Actually: H_dot = -rho_dot / (6*H) = -(rho+P) * 3H / (6H) = -(rho+P)/2
    # For scalar field: rho+P = M*tau_dot^2 (kinetic only)
    # H_dot = -(1/2)*FC*M_ATDHFB*tau_dot^2
    # No wait, H^2 = FC * rho, so 2*H*H_dot = FC * rho_dot
    # rho_dot = M_ATDHFB * tau_dot * tau_ddot + dS/dtau * tau_dot
    # From EOM: M * tau_ddot = -dS/dtau - 3*H*M*tau_dot
    # So M*tau_dot*tau_ddot = -dS/dtau*tau_dot - 3*H*M*tau_dot^2
    # rho_dot = -dS*tau_dot - 3*H*M*tau_dot^2 + dS*tau_dot = -3*H*M*tau_dot^2
    # 2*H*H_dot = FC * (-3*H*M*tau_dot^2) => H_dot = -(3/2)*FC*M*tau_dot^2
    # Hmm no. Let me redo:
    # H^2 = FC * rho = FC * [(1/2)*M*tdot^2 + S]
    # d/dt(H^2) = 2*H*Hdot = FC * [M*tdot*tddot + (dS/dtau)*tdot]
    # From EOM: M*tddot = -dS/dtau - 3*H*M*tdot
    # => M*tdot*tddot = -dS/dtau * tdot - 3*H*M*tdot^2
    # => 2*H*Hdot = FC * [-dS*tdot - 3*H*M*tdot^2 + dS*tdot]
    # => 2*H*Hdot = FC * (-3*H*M*tdot^2)
    # => Hdot = -(3/2)*FC*M*tdot^2 / (2) ... no
    # => Hdot = -FC * 3*H*M*tdot^2 / (2*H) = -(3/2)*FC*M*tdot^2
    # Wait: 2*H*Hdot = -3*H*FC*M*tdot^2
    # Hdot = -(3/2)*FC*M*tdot^2
    #
    # Actually this should give the standard result:
    # Hdot = -(4*pi*G) * (rho+P) where rho+P = M*tdot^2 * pf * M_KK^4
    # (4*pi*G) * M*tdot^2 * pf * M_KK^4 = (4*pi/(M_Pl^2)) * M*tdot^2 * pf * M_KK^4
    # = (4*pi) * alpha_G * pf * M * tdot^2
    # = FC * (3/2) * M * tdot^2
    # Yes! Because FC = (8*pi/3)*alpha_G*pf, so (4*pi)*alpha_G*pf = FC * 3/2.
    # Therefore Hdot = -(3/2)*FC*M*tdot^2 is WRONG by sign? No:
    # Hdot = -(4*pi*G)*(rho+P) = negative since rho+P > 0.
    # Hdot = -FC*(3/2)*M*tdot^2. Yes, this is correct.

    H_dot_arr = -(3.0/2.0) * FC * M_ATDHFB * tau_dot_arr**2

    # epsilon_H = -H_dot / H^2
    with np.errstate(divide='ignore', invalid='ignore'):
        epsilon_H_arr = -H_dot_arr / H_arr**2
        # Simplify: epsilon_H = (3/2)*FC*M*tdot^2 / (FC*rho) = (3/2)*M*tdot^2/rho
        # = (3/2) * KE / rho = 3*T / (T + V)
        epsilon_H_check = (3.0/2.0) * M_ATDHFB * tau_dot_arr**2 / rho_arr

    # Find fold crossing
    fold_mask = (tau_arr >= tau_fold - 0.005) & (tau_arr <= tau_fold + 0.005)
    if np.any(fold_mask):
        idx_fold = np.argmin(np.abs(tau_arr - tau_fold))
    else:
        idx_fold = len(tau_arr) // 2

    # eta_H = d(epsilon_H)/dt / (H * epsilon_H)
    # Compute numerically
    deps_dt = np.gradient(epsilon_H_arr, t)
    with np.errstate(divide='ignore', invalid='ignore'):
        eta_H_arr = deps_dt / (H_arr * epsilon_H_arr)

    # Number of e-folds
    # N = integral H dt
    N_efolds = np.trapezoid(H_arr, t)

    # Find when tau reaches fold
    if idx_fold < len(t):
        eps_at_fold = epsilon_H_arr[idx_fold]
        eta_at_fold = eta_H_arr[idx_fold] if idx_fold < len(eta_H_arr) else np.nan
        H_at_fold = H_arr[idx_fold]
        tau_at_fold = tau_arr[idx_fold]
        t_at_fold = t[idx_fold]
    else:
        eps_at_fold = np.nan
        eta_at_fold = np.nan
        H_at_fold = np.nan
        tau_at_fold = np.nan
        t_at_fold = np.nan

    # n_s and r
    ns = 1.0 - 2.0 * eps_at_fold - eta_at_fold if np.isfinite(eta_at_fold) else np.nan
    ns_approx = 1.0 - 2.0 * eps_at_fold
    r = 16.0 * eps_at_fold

    print(f"  Transit completed: tau_final = {tau_arr[-1]:.4f}")
    print(f"  Time to fold: {t_at_fold:.4e} M_KK^-1")
    print(f"  N_e (total) = {N_efolds:.6f}")
    print(f"  H at fold = {H_at_fold:.6e} M_KK")
    print(f"  epsilon_H at fold = {eps_at_fold:.6e}")
    print(f"  eta_H at fold = {eta_at_fold:.6e}")
    print(f"  n_s = 1 - 2*eps = {ns_approx:.6f}")
    print(f"  n_s = 1 - 2*eps - eta = {ns:.6f}")
    print(f"  r = 16*eps = {r:.6f}")
    print(f"  tau_dot at fold = {tau_dot_arr[idx_fold]:.2f}")

    # Check: epsilon_H should equal 3*KE/(KE+PE)
    KE_fold = 0.5 * M_ATDHFB * tau_dot_arr[idx_fold]**2
    PE_fold = S_arr[idx_fold]
    eps_check = (3.0/2.0) * M_ATDHFB * tau_dot_arr[idx_fold]**2 / (KE_fold + PE_fold)
    print(f"  epsilon_H check (3T/(T+V)) = {eps_check:.6e}")
    print(f"  KE/PE at fold = {KE_fold/PE_fold:.4f}")

    results[name] = {
        't': t, 'tau': tau_arr, 'tau_dot': tau_dot_arr,
        'H': H_arr, 'epsilon_H': epsilon_H_arr, 'eta_H': eta_H_arr,
        'N_efolds': N_efolds, 'eps_fold': eps_at_fold, 'eta_fold': eta_at_fold,
        'ns_approx': ns_approx, 'ns': ns, 'r': r,
        'tau_dot_init': tau_dot_init, 'H_fold': H_at_fold,
        'KE_PE_fold': KE_fold/PE_fold
    }

# ==============================================================
# 7. ANALYTIC CROSS-CHECKS
# ==============================================================

print("\n" + "=" * 70)
print("ANALYTIC CROSS-CHECKS")
print("=" * 70)

# For the S39 transit velocity:
# KE = (1/2)*M*tau_dot^2 = (1/2)*1.695*34615^2 = 1.016e9
# PE = S(0.19) = 250361
# KE/PE = 4057
# epsilon_H = 3*KE/(KE+PE) = 3*1.016e9/(1.016e9+250361) = 2.9993
# This means epsilon_H ~ 3 !! Deeply non-inflationary.

KE_S39 = 0.5 * M_ATDHFB * tau_dot_S39**2
PE_S39 = float(cs_S(0.19))
eps_S39_analytic = (3.0/2.0) * M_ATDHFB * tau_dot_S39**2 / (KE_S39 + PE_S39)
print(f"\nS39 transit at fold:")
print(f"  KE = {KE_S39:.2e}")
print(f"  PE = S(0.19) = {PE_S39:.2f}")
print(f"  KE/PE = {KE_S39/PE_S39:.2f}")
print(f"  epsilon_H = 3*KE/(KE+PE) = {eps_S39_analytic:.6f}")
print(f"  n_s = 1 - 2*eps = {1.0-2.0*eps_S39_analytic:.6f}")
print(f"  r = 16*eps = {16.0*eps_S39_analytic:.6f}")

# For epsilon_H = 0.0176 (needed for n_s = 0.965):
# epsilon_H = 3*KE/(KE+PE) = 0.0176
# => KE/PE = 0.0176/(3 - 0.0176) = 0.00590
# => M*tau_dot^2 = 2*0.00590*S(0.19) = 2*0.00590*250361 = 2954
# => tau_dot = sqrt(2954/1.695) = 41.7
# Compare to S39: tau_dot = 34615. Need 830x smaller velocity.

KE_needed = 0.0176 / (3.0 - 0.0176) * PE_S39
tau_dot_needed = np.sqrt(2.0 * KE_needed / M_ATDHFB)
print(f"\nFor epsilon_H = 0.0176:")
print(f"  KE needed = {KE_needed:.2f}")
print(f"  tau_dot needed = {tau_dot_needed:.2f}")
print(f"  tau_dot(S39) / tau_dot(needed) = {tau_dot_S39/tau_dot_needed:.1f}")

# What is tau_dot_needed? It's ~41.7 in M_KK units.
# This means the transit takes t = 0.19/41.7 = 0.0046 in 1/M_KK
# H = sqrt(FC * rho) ~ sqrt(FC * 250361)
H_at_needed = np.sqrt(FC * (KE_needed + PE_S39))
N_efolds_needed = H_at_needed * 0.19 / tau_dot_needed
print(f"  H at this velocity = {H_at_needed:.6e} M_KK")
print(f"  N_e ~ H * Delta_tau / tau_dot = {N_efolds_needed:.6f}")

# For epsilon_H << 1 (quasi-de Sitter):
# Need KE << PE, i.e., tau_dot very small.
# But then dS/dtau (positive!) decelerates tau, making tau_dot even smaller
# or reversing direction entirely. There's no minimum to orbit around.
# The modulus cannot slow-roll in the positive dS/dtau direction.

# CRITICAL INSIGHT: epsilon_H = 3*T/(T+V) = 3/(1 + V/T)
# For epsilon_H << 1: need V >> T, i.e., slow roll.
# But with V = S(tau) monotonically increasing and dV/dtau > 0,
# a modulus moving in the +tau direction is climbing the hill.
# It decelerates. The velocity decreases. epsilon_H decreases.
# But also, the modulus STOPS and reverses.
#
# For a modulus moving in the -tau direction (coming back from fold),
# it accelerates, epsilon_H increases.

print("\n" + "=" * 70)
print("CRITICAL STRUCTURAL RESULT")
print("=" * 70)

# Compute epsilon_H for various KE/PE ratios
ratios = [1e-6, 1e-4, 1e-2, 0.0059, 1.0, 10.0, 100.0, 4057.0]
print(f"\n{'KE/PE':>12} {'epsilon_H':>12} {'n_s':>10} {'r':>10}")
for ratio in ratios:
    eps = 3.0 * ratio / (1.0 + ratio)
    ns_val = 1.0 - 2.0 * eps
    r_val = 16.0 * eps
    print(f"{ratio:12.4e} {eps:12.6e} {ns_val:10.6f} {r_val:10.6f}")

# ==============================================================
# 8. SCENARIO F: SLOW TRANSIT (tau_dot = tau_dot_needed)
# ==============================================================

print("\n" + "=" * 70)
print("SCENARIO F: SLOW TRANSIT (epsilon_H ~ 0.0176 target)")
print("=" * 70)

y0_F = [tau_start, tau_dot_needed]
rho0_F = 0.5 * M_ATDHFB * tau_dot_needed**2 + float(cs_S(tau_start))
H0_F = np.sqrt(FC * rho0_F)
print(f"tau_dot_0 = {tau_dot_needed:.4f}")
print(f"H_0 = {H0_F:.6e} M_KK = {H0_F * M_KK_GeV:.4e} GeV")

t_transit_F = (tau_end - tau_start) / tau_dot_needed
t_span_F = (0, 10.0 * t_transit_F)
t_eval_F = np.linspace(0, 10.0 * t_transit_F, 20000)

sol_F = solve_ivp(coupled_odes, t_span_F, y0_F, method='RK45',
                  events=[event_end, event_zero],
                  t_eval=t_eval_F, rtol=1e-12, atol=1e-15,
                  max_step=t_transit_F/1000)

t_F = sol_F.t
tau_F = sol_F.y[0]
tdot_F = sol_F.y[1]

S_F = np.array([float(cs_S(np.clip(tv, 0.0, 0.5))) for tv in tau_F])
rho_F = 0.5 * M_ATDHFB * tdot_F**2 + S_F
H_F = np.sqrt(FC * np.maximum(rho_F, 0.0))

Hdot_F = -(3.0/2.0) * FC * M_ATDHFB * tdot_F**2
eps_H_F = np.where(H_F > 0, -Hdot_F / H_F**2, 0.0)

deps_dt_F = np.gradient(eps_H_F, t_F)
eta_H_F = np.where((H_F > 0) & (eps_H_F > 0), deps_dt_F / (H_F * eps_H_F), 0.0)

N_F = np.cumsum(H_F[:-1] * np.diff(t_F))
N_F = np.append(0, N_F)

# Find tau reversal point
reversal_idx = np.argmax(tau_F)
print(f"tau_max reached = {tau_F[reversal_idx]:.6f} at t = {t_F[reversal_idx]:.4e}")
print(f"tau_max - tau_start = {tau_F[reversal_idx] - tau_start:.6f}")
print(f"tau_dot at reversal = {tdot_F[reversal_idx]:.4e}")
print(f"epsilon_H at reversal = {eps_H_F[reversal_idx]:.6e}")
print(f"epsilon_H at start = {eps_H_F[0]:.6e}")
print(f"N_e at reversal = {N_F[reversal_idx]:.6e}")

# Find fold crossing
fold_mask_F = tau_F >= tau_fold
if np.any(fold_mask_F):
    idx_fold_F = np.where(fold_mask_F)[0][0]
    print(f"\nFold reached at t = {t_F[idx_fold_F]:.4e}")
    print(f"  epsilon_H(fold) = {eps_H_F[idx_fold_F]:.6e}")
    print(f"  eta_H(fold) = {eta_H_F[idx_fold_F]:.6e}")
    print(f"  n_s = {1.0 - 2.0*eps_H_F[idx_fold_F] - eta_H_F[idx_fold_F]:.6f}")
    print(f"  N_e(fold) = {N_F[idx_fold_F]:.6e}")
else:
    print(f"\nFold NOT reached! tau never gets to {tau_fold}")
    print(f"Deceleration from dS/dtau > 0 reverses the modulus before fold")

# ==============================================================
# 9. STRUCTURAL ANALYSIS: WHAT epsilon_H CAN THE FRAMEWORK PRODUCE?
# ==============================================================

print("\n" + "=" * 70)
print("STRUCTURAL ANALYSIS")
print("=" * 70)

# The key structural result is:
# epsilon_H = 3 * T / (T + V) where T = (1/2)*M*tau_dot^2, V = S(tau)
#
# During transit FROM tau=0 toward fold:
# dV/dtau > 0 at all tau (monotonic). So V increases. T decreases.
# epsilon_H starts at some value and DECREASES during transit.
# Eventually T -> 0 (tau reverses) and epsilon_H -> 0.
#
# For a modulus that reaches the fold, it must have had enough initial KE.
# The BCS provides E_BCS = -0.115 M_KK^4 (in S-units) ~ 0.115/S(0) ~ 5e-7 of PE.
# So the BCS-kicked modulus has KE/PE ~ 5e-7 initially.
# epsilon_H ~ 3 * 5e-7 / (1 + 5e-7) ~ 1.5e-6.
# WAY below the needed 0.0176.

# But in the S39 picture, the transit velocity is 34,615 which gives KE >> PE.
# How? The S39 velocity came from dtau/dt = dS/dtau / M, which is NOT from energy
# conservation but from some kind of force balance. That formula implies an
# EXTERNAL driving force supplying enormous energy.
# With that velocity, epsilon_H ~ 3.

# The bottom line is:
# (a) BCS energy alone: epsilon_H ~ 1.5e-6 (but modulus can't reach fold)
# (b) S39 driven transit: epsilon_H ~ 3 (too fast, N_e ~ 0.04)
# (c) Target: epsilon_H = 0.0176 requires specific tau_dot ~ 42

# For epsilon_H = 0.0176 at the fold:
# KE = 1478.6, tau_dot = 41.7
# But Delta_S = S(fold) - S(0) = 5522
# So KE < Delta_S means the modulus CAN reach fold by energy conservation
# if it started at tau=0 with KE_initial = Delta_S + KE_fold = 5522+1478 = 7000
# Initial tau_dot = sqrt(2*7000/1.695) = 90.8

KE_total_needed = (float(cs_S(0.19)) - float(cs_S(0.0))) + KE_needed
tau_dot_initial_needed = np.sqrt(2.0 * KE_total_needed / M_ATDHFB)
print(f"\nTo reach fold with epsilon_H = 0.0176:")
print(f"  Need initial KE = Delta_S + KE_target = {KE_total_needed:.1f}")
print(f"  Initial tau_dot = {tau_dot_initial_needed:.2f}")
print(f"  This is {tau_dot_initial_needed / tau_dot_S39 * 100:.2f}% of S39 velocity")
print(f"  Required KE / BCS energy = {KE_total_needed / 0.115:.0f}")

# The required initial KE is 60,870x larger than the BCS condensation energy.
# There is no mechanism within the framework to provide this.

print(f"\n  KE_total_needed / |E_BCS| = {KE_total_needed / 0.115:.0f}x")
print(f"  STRUCTURAL OBSTRUCTION: No known energy source within framework")

# ==============================================================
# 10. COMPLETE PARAMETER SPACE MAP
# ==============================================================

print("\n" + "=" * 70)
print("PARAMETER SPACE MAP: epsilon_H vs tau_dot at fold")
print("=" * 70)

tau_dot_range = np.logspace(-3, 5, 200)
S_fold_val = float(cs_S(0.19))
eps_range = (3.0/2.0) * M_ATDHFB * tau_dot_range**2 / (0.5*M_ATDHFB*tau_dot_range**2 + S_fold_val)

# Print key points
print(f"\n{'tau_dot':>12} {'KE/PE':>12} {'epsilon_H':>12} {'n_s (approx)':>14} {'r':>10}")
key_tdots = [0.01, 0.1, 1.0, 10.0, 41.7, 100.0, 1000.0, 34615.0]
for td in key_tdots:
    ke = 0.5*M_ATDHFB*td**2
    ratio_kp = ke/S_fold_val
    eps_val = 3.0*ratio_kp/(1.0+ratio_kp)
    ns_val = 1.0 - 2.0*eps_val
    r_val = 16.0*eps_val
    marker = ""
    if abs(td - 41.7) < 1:
        marker = " <-- epsilon_H = 0.0176 target"
    elif abs(td - 34615) < 1:
        marker = " <-- S39 transit velocity"
    print(f"{td:12.1f} {ratio_kp:12.4e} {eps_val:12.6e} {ns_val:14.6f} {r_val:10.6f}{marker}")

# ==============================================================
# 11. SOLVE SCENARIO G: EXACT epsilon_H=0.0176 at tau=0
# ==============================================================

print("\n" + "=" * 70)
print("SCENARIO G: tau_dot tuned for epsilon_H=0.0176 at tau=0.05")
print("=" * 70)

# At tau=0.05: S = cs_S(0.05)
S_05 = float(cs_S(0.05))
# epsilon_H = 3*KE/(KE+PE) = 0.0176
# KE = 0.0176/(3-0.0176) * PE = 0.00590 * S_05
KE_05 = 0.0176 / (3.0 - 0.0176) * S_05
tdot_05 = np.sqrt(2.0 * KE_05 / M_ATDHFB)

y0_G = [0.05, tdot_05]
rho0_G = KE_05 + S_05
H0_G = np.sqrt(FC * rho0_G)

print(f"S(0.05) = {S_05:.2f}")
print(f"KE needed = {KE_05:.2f}")
print(f"tau_dot = {tdot_05:.4f}")
print(f"H(0.05) = {H0_G:.6e} M_KK")
print(f"epsilon_H(0.05) = {3.0*KE_05/(KE_05+S_05):.6f}")

t_tr_G = 0.25/tdot_05
sol_G = solve_ivp(coupled_odes, (0, 20*t_tr_G), y0_G, method='RK45',
                  events=[event_end, event_zero],
                  t_eval=np.linspace(0, 20*t_tr_G, 50000),
                  rtol=1e-12, atol=1e-15, max_step=t_tr_G/2000)

t_G = sol_G.t
tau_G = sol_G.y[0]
tdot_G = sol_G.y[1]
S_G = np.array([float(cs_S(np.clip(tv, 0.0, 0.5))) for tv in tau_G])
rho_G = 0.5*M_ATDHFB*tdot_G**2 + S_G
H_G = np.sqrt(FC * np.maximum(rho_G, 0.0))
eps_H_G = np.where(H_G > 0, (3.0/2.0)*M_ATDHFB*tdot_G**2 / rho_G, 0.0)
N_G = np.cumsum(H_G[:-1] * np.diff(t_G))
N_G = np.append(0, N_G)

rev_G = np.argmax(tau_G)
fold_reach_G = tau_G[rev_G] >= tau_fold

print(f"\ntau_max = {tau_G[rev_G]:.6f}")
print(f"Reaches fold? {fold_reach_G}")
print(f"N_e at reversal = {N_G[rev_G]:.6e}")
print(f"epsilon_H at tau_max = {eps_H_G[rev_G]:.6e}")
print(f"epsilon_H range = [{eps_H_G[:rev_G+1].min():.6e}, {eps_H_G[:rev_G+1].max():.6e}]")
if fold_reach_G:
    idx_f = np.argmin(np.abs(tau_G[:rev_G+1] - tau_fold))
    print(f"epsilon_H at fold = {eps_H_G[idx_f]:.6e}")
    print(f"n_s at fold = {1.0-2.0*eps_H_G[idx_f]:.6f}")
    print(f"r at fold = {16.0*eps_H_G[idx_f]:.6f}")

# ==============================================================
# 12. SAVE RESULTS
# ==============================================================

# Use scenario A (S39 velocity) as the primary result
res_A = results['A_S39_velocity']

np.savez('tier0-computation/s43_friedmann_bcs.npz',
    # Primary result at fold
    epsilon_H_fold=res_A['eps_fold'],
    eta_H_fold=res_A['eta_fold'],
    ns_approx=res_A['ns_approx'],
    ns_full=res_A['ns'],
    r_tensor=res_A['r'],
    N_efolds=res_A['N_efolds'],
    H_fold=res_A['H_fold'],
    tau_dot_fold=tau_dot_S39,
    KE_PE_fold=res_A['KE_PE_fold'],

    # Structural formula
    # epsilon_H = 3*KE/(KE+PE) = 3*(M/2*tdot^2) / (M/2*tdot^2 + S)
    M_ATDHFB=M_ATDHFB,
    S_fold=float(cs_S(0.19)),

    # For target epsilon_H = 0.0176
    tau_dot_needed_for_0p0176=tau_dot_needed,
    KE_needed_for_0p0176=KE_needed,
    ratio_KE_BCS=KE_total_needed/0.115,

    # Scenario comparison
    scenario_names=np.array(['A_S39_velocity', 'B_energy_conserving', 'C_10x_minimum',
                             'D_100x_minimum', 'E_half_S39', 'F_slow_target', 'G_tuned']),
    scenario_eps_fold=np.array([
        results['A_S39_velocity']['eps_fold'],
        results['B_energy_conserving']['eps_fold'],
        results['C_10x_minimum']['eps_fold'],
        results['D_100x_minimum']['eps_fold'],
        results['E_half_S39']['eps_fold'],
        eps_H_G[rev_G] if not fold_reach_G else eps_H_G[np.argmin(np.abs(tau_G[:rev_G+1]-0.19))],
        eps_H_G[0]
    ]),

    # Time series for Scenario A
    t_A=res_A['t'],
    tau_A=res_A['tau'],
    tdot_A=res_A['tau_dot'],
    H_A=res_A['H'],
    eps_A=res_A['epsilon_H'],

    # Time series for Scenario G
    t_G=t_G,
    tau_G=tau_G,
    tdot_G=tdot_G,
    H_G=H_G,
    eps_G=eps_H_G,
    N_G=N_G,

    # Parameter space map
    tau_dot_map=tau_dot_range,
    epsilon_H_map=eps_range,

    # Constants used
    M_KK_GeV=M_KK_GeV,
    M_Pl_GeV=M_Pl_GeV,
    alpha_G=alpha_G,
    FC=FC,

    # Gate
    gate_name='FRIEDMANN-BCS-43',
    gate_type='INFO'
)

print("\nData saved to tier0-computation/s43_friedmann_bcs.npz")

# ==============================================================
# 13. PLOT
# ==============================================================

fig, axes = plt.subplots(2, 3, figsize=(18, 11))
fig.suptitle('FRIEDMANN-BCS-43: Coupled Friedmann-BCS epsilon_H During Transit',
             fontsize=14, fontweight='bold')

# Panel 1: V(tau) = S(tau)
ax = axes[0, 0]
tau_plot = np.linspace(0, 0.35, 500)
S_plot = np.array([float(cs_S(t)) for t in tau_plot])
ax.plot(tau_plot, S_plot, 'b-', lw=2)
ax.axvline(0.19, color='r', ls='--', alpha=0.7, label='fold')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$S(\tau)$ [dimensionless]')
ax.set_title(r'Spectral Action $S(\tau)$ — Monotonic, No Minimum')
ax.legend()
ax.grid(True, alpha=0.3)

# Panel 2: epsilon_H vs tau_dot at fold (structural formula)
ax = axes[0, 1]
ax.loglog(tau_dot_range, eps_range, 'b-', lw=2)
ax.axhline(0.0176, color='r', ls='--', lw=1.5, label=r'$\epsilon_H = 0.0176$ (Planck $n_s$)')
ax.axhline(3.0, color='gray', ls=':', lw=1, label=r'$\epsilon_H = 3$ (stiff)')
ax.axvline(tau_dot_S39, color='orange', ls='--', lw=1.5, label=f'S39 transit: {tau_dot_S39:.0f}')
ax.axvline(tau_dot_needed, color='green', ls='--', lw=1.5, label=f'Target: {tau_dot_needed:.1f}')
ax.fill_between([1e-3, 1e5], [0.036/16]*2, [3]*2, alpha=0.1, color='red',
                label=r'$r > 0.036$ BICEP excluded')
ax.set_xlabel(r'$\dot{\tau}$ at fold [$M_{KK}$ units]')
ax.set_ylabel(r'$\epsilon_H = 3T/(T+V)$')
ax.set_title(r'$\epsilon_H$ vs Transit Velocity at Fold')
ax.set_xlim(1e-3, 1e5)
ax.set_ylim(1e-8, 5)
ax.legend(fontsize=7, loc='lower right')
ax.grid(True, alpha=0.3, which='both')

# Panel 3: Scenario A time evolution
ax = axes[0, 2]
res = results['A_S39_velocity']
ax.plot(res['t'] * M_KK_GeV, res['tau'], 'b-', lw=2)
ax.axhline(0.19, color='r', ls='--', alpha=0.5)
ax.set_xlabel(r'$t$ [GeV$^{-1}$]')
ax.set_ylabel(r'$\tau(t)$')
ax.set_title(f'Scenario A: S39 Transit ($\\dot{{\\tau}}_0$ = {tau_dot_S39:.0f})')
ax.grid(True, alpha=0.3)

# Panel 4: epsilon_H(t) for Scenario A
ax = axes[1, 0]
mask_A = res['tau'] < 0.35
ax.semilogy(res['tau'][mask_A], res['epsilon_H'][mask_A], 'b-', lw=2)
ax.axhline(0.0176, color='r', ls='--', lw=1.5, label=r'$\epsilon_H = 0.0176$')
ax.axvline(0.19, color='gray', ls=':', alpha=0.5)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$\epsilon_H$')
ax.set_title(r'$\epsilon_H(\tau)$ — Scenario A')
ax.legend()
ax.grid(True, alpha=0.3)
ax.set_ylim(1e-1, 5)

# Panel 5: Scenario G (tuned for epsilon_H = 0.0176)
ax = axes[1, 1]
mask_fwd = np.arange(rev_G+1)
ax.plot(tau_G[mask_fwd], eps_H_G[mask_fwd], 'g-', lw=2, label='Forward transit')
ax.axhline(0.0176, color='r', ls='--', lw=1.5, label=r'$\epsilon_H = 0.0176$')
ax.axvline(0.19, color='gray', ls=':', alpha=0.5, label='Fold')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$\epsilon_H$')
ax.set_title(f'Scenario G: Tuned ($\\dot{{\\tau}}_0$ = {tdot_05:.1f})')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 6: Summary table
ax = axes[1, 2]
ax.axis('off')
summary_text = (
    "STRUCTURAL RESULT\n"
    "=" * 40 + "\n"
    f"epsilon_H = 3*KE / (KE + S(tau))\n\n"
    f"S39 transit (tdot={tau_dot_S39:.0f}):\n"
    f"  epsilon_H = {results['A_S39_velocity']['eps_fold']:.4f}\n"
    f"  n_s = {results['A_S39_velocity']['ns_approx']:.4f}\n"
    f"  r = {results['A_S39_velocity']['r']:.4f}\n"
    f"  N_e = {results['A_S39_velocity']['N_efolds']:.4f}\n\n"
    f"Target (epsilon_H=0.0176):\n"
    f"  tdot_needed = {tau_dot_needed:.1f}\n"
    f"  KE_needed/|E_BCS| = {KE_total_needed/0.115:.0f}x\n"
    f"  Fold reached? {fold_reach_G}\n\n"
    f"CONCLUSION:\n"
    f"  S39 transit: epsilon_H ~ 3\n"
    f"    (n_s ~ -5, r ~ 48, N_e ~ 0.04)\n"
    f"  BCS energy alone: epsilon_H ~ 1e-6\n"
    f"    (n_s ~ 1.000, r ~ 2e-5)\n"
    f"  Neither matches Planck n_s = 0.965"
)
ax.text(0.05, 0.95, summary_text, transform=ax.transAxes, fontsize=9,
        verticalalignment='top', fontfamily='monospace',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.tight_layout()
plt.savefig('tier0-computation/s43_friedmann_bcs.png', dpi=150, bbox_inches='tight')
print("Plot saved to tier0-computation/s43_friedmann_bcs.png")

# ==============================================================
# 14. FINAL SUMMARY
# ==============================================================

print("\n" + "=" * 70)
print("FINAL SUMMARY: FRIEDMANN-BCS-43")
print("=" * 70)

print(f"""
GATE: FRIEDMANN-BCS-43 (INFO)

STRUCTURAL FORMULA:
  epsilon_H = (3/2) * M_ATDHFB * tau_dot^2 / [(1/2)*M_ATDHFB*tau_dot^2 + S(tau)]
            = 3 * KE / (KE + PE)

AT THE FOLD (tau = 0.19, S = {float(cs_S(0.19)):.0f}):

  Scenario A (S39 transit, tau_dot = {tau_dot_S39:.0f}):
    KE/PE = {results['A_S39_velocity']['KE_PE_fold']:.0f}
    epsilon_H = {results['A_S39_velocity']['eps_fold']:.4f}
    n_s = 1 - 2*eps = {results['A_S39_velocity']['ns_approx']:.4f}
    r = 16*eps = {results['A_S39_velocity']['r']:.4f}
    N_e = {results['A_S39_velocity']['N_efolds']:.4f}
    STATUS: KINETIC-DOMINATED (epsilon_H ~ 3, stiff-matter regime)

  For epsilon_H = 0.0176 (Planck n_s = 0.965):
    tau_dot needed = {tau_dot_needed:.1f}
    KE/PE = 0.0059
    ENERGY SOURCE SHORTFALL: {KE_total_needed/0.115:.0f}x above BCS condensation energy
    Fold reached with this velocity? {fold_reach_G}

COMPARISON TO W1-2/W3-5 ASSUMED VALUE:
  Assumed epsilon_H = 0.0176 -> n_s = 0.965 (Planck match)
  Computed epsilon_H = {results['A_S39_velocity']['eps_fold']:.4f} -> n_s = {results['A_S39_velocity']['ns_approx']:.4f}
  DISCREPANCY: {results['A_S39_velocity']['eps_fold']/0.0176:.0f}x

STRUCTURAL OBSTRUCTION:
  The spectral action S(tau) is monotonically increasing with S ~ 250,000.
  For epsilon_H << 1, need KE << S, i.e., tau_dot << sqrt(2*S/M) = {np.sqrt(2*float(cs_S(0.19))/M_ATDHFB):.0f}.
  But for epsilon_H = 0.0176 specifically, need tau_dot = {tau_dot_needed:.1f}.
  The BCS mechanism provides |E_BCS| = 0.115 M_KK^4, giving
  max tau_dot_BCS = sqrt(2*0.115/M) = {np.sqrt(2*0.115/M_ATDHFB):.3f}.
  At this velocity: epsilon_H = {3.0*(0.5*M_ATDHFB*(2*0.115/M_ATDHFB))/(0.5*M_ATDHFB*(2*0.115/M_ATDHFB)+float(cs_S(0.19))):.2e}.

  THE TWO REGIMES:
  1. BCS-only energy: epsilon_H ~ 10^(-6), n_s ~ 1.000, no tilt
  2. S39 driven transit: epsilon_H ~ 3, n_s ~ -5, stiff matter (not inflation)

  No intermediate regime is mechanically accessible within the framework.
  The assumed epsilon_H = 0.0176 requires an energy source {KE_total_needed/0.115:.0f}x
  larger than BCS condensation and {tau_dot_S39/tau_dot_needed:.0f}x slower than the
  S39 force-balance velocity. It occupies a desert in parameter space.

IMPACT ON FRAMEWORK:
  The n_s = 0.965 prediction from W1-2/W3-5 was INPUT (epsilon_H assumed = 0.0176),
  not OUTPUT (computed from dynamics). The actual dynamics produce either:
  (a) n_s ~ 1.000 (too blue, if BCS energy only)
  (b) n_s ~ -5 (deeply unphysical, if S39 transit)

  Neither matches Planck. The n_s constraint surface is EMPTY for the
  spectral-action-driven Friedmann-BCS system.
""")
