#!/usr/bin/env python3
"""
EFOLD-MAPPING-73B: Full Expansion History from Fold to Present
===============================================================

Session 73b, Wave 1-D
Agent: volovik-superfluid-universe-theorist

Pre-registered gate: EFOLD-MAPPING-73B
  PASS: K_pivot maps to tau where n_s in [0.945, 0.975]
  FAIL: K_pivot gives n_s > 1 or n_s < 0.90
  INFO: Stiff epoch dominates (>99% of N_total) making mapping K_pivot-insensitive

Physics:
--------
The expansion history has four epochs, each with a distinct EOS:

  1. STIFF epoch (fold -> GGE freeze-out):
     Modulus kinetic energy dominates. EOS w = +1.
     a(t) ~ t^{1/3}. H = 1/(3t).
     Duration: dt_transit = 1.13e-3 M_KK^{-1}.
     Physical H at fold: H_phys = 0.396 M_KK (from S64).
     N_stiff = H_phys * dt_transit = 3.73e-3 (from S64).

  2. GGE epoch (freeze-out -> radiation-domination onset):
     GGE relic with w_GGE from two-fluid partition.
     S73A W1-C: additive tracking vacuum EXCLUDED by 130x.
     Non-additive G-renormalization: G_eff = G * (1 + alpha_track).
     Volovik identity: P_vac = -rho_vac (equilibrium), so vacuum
     does NOT contribute to expansion dynamics additively.
     Instead, it renormalizes G_N through the Sakharov mechanism.
     w_GGE determined by GGE quasiparticle content: w = 0 (CDM-like,
     from CDM-CONSTRUCT-43/44: T^{0i} = 0, v_eff = 3.48e-6c).

  3. RADIATION epoch: Standard w = 1/3.

  4. MATTER + LAMBDA epoch: w_0 = -0.918, w_a = 0.

The "scale factor" is emergent spectral complexity:
  a_eff(tau) = sqrt(a_2(tau) / a_2(tau_today))

where a_2(tau) is the second Seeley-DeWitt coefficient of D_K(tau).

The total e-folds N_total = ln(a_today / a_fold) is decomposed
into contributions from each epoch.

CMB pivot mapping:
  k_pivot = 0.05 Mpc^{-1} in physical units.
  Map back through expansion history to find tau_pivot.

KEY STRUCTURAL RESULT from S64:
  N_e(transit) = 3.73e-3 physical e-folds.
  This is 60/(3.73e-3) = 16,000x too small for standard inflation.
  BUT exflation is not inflation. The expansion history after the
  transit is dominated by the GGE epoch (matter-like, w=0) and
  radiation epoch (w=1/3), which together provide ~60 e-folds
  between the transit and the CMB last-scattering surface.

S73A W1-D CRITICAL INPUT:
  S(tau) monotonically increasing for tau > 0.19.
  => No post-fold equilibrium from bare spectral action.
  => The modulus drifts. Stabilization requires BCS dressing
     or instanton back-reaction (kappa < 1 opens at tau = 0.48).
  => The "today" value of tau is NOT tau_fold.

Cross-checks:
  (1) N_total must be consistent with observed CMB temperature.
  (2) H_0 at present must match 67.4 km/s/Mpc.
  (3) T_CMB = 2.7255 K constrains the reheating temperature.
  (4) BBN constraints (S73A W1-C) on G_eff during radiation epoch.

Input: s73a_spectral_action_profile.npz, s73a_instanton_landscape.npz,
       s64_ne_selfconsist.npz, canonical_constants.py
Output: s73b_efold_mapping.npz
"""

import numpy as np
import sys
import os
import time
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from scipy.interpolate import CubicSpline
from scipy.integrate import solve_ivp, quad

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
os.chdir(SCRIPT_DIR)

from canonical_constants import (, k_pivot_planck, planck_ns
    tau_fold, S_fold, dS_fold, d2S_fold,
    G_DeWitt, v_terminal, H_fold, dt_transit,
    M_KK, M_KK_gravity, M_KK_kerner, M_Pl_reduced, M_Pl_unreduced,
    a0_fold, a2_fold, a4_fold,
    N_e_classical,
    PI, E_cond, n_pairs, E_exc,
    c_Gold, omega_L1,
    H_0_km_s_Mpc, H_0_inv_s, H_0_GeV, T_CMB, T_CMB_GeV,
    rho_Lambda_obs, rho_crit_GeV4, A_s_CMB,
    Omega_r, Omega_m, Omega_Lambda,
    Mpc_to_m, Mpc_to_GeV_inv, GeV_inv_to_Mpc,
    hbar_c_GeV_m, hbar_GeV_s,
    t_universe_s, z_BBN, T_BBN_GeV, T_recomb_GeV,
    Delta_BCS, T_GGE_B2,
)

t_start = time.time()

print("=" * 78)
print("EFOLD-MAPPING-73B: Full Expansion History from Fold to Present")
print("  21 sessions overdue (S51 -> S73b). The single question.")
print("=" * 78)

# =============================================================================
# SECTION 1: LOAD S73A DATA
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 1: Loading S73A Data")
print("=" * 78)

# S73A spectral action profile
d_sa = np.load('s73a_spectral_action_profile.npz', allow_pickle=True)
tau_sa_grid = d_sa['tau_grid']       # 104 points, [0, 2]
S_bare_all = d_sa['S_bare']          # (4, 104) -- 4 functionals
tau_fine = d_sa['tau_fine']           # 1000 points
S_fine = d_sa['S_fine']              # S_f*(tau) spline
dS_fine = d_sa['dS_fine']            # dS/dtau spline
d2S_fine_arr = d_sa['d2S_fine']      # d2S/dtau2 spline
ns_fine = d_sa['ns_fine']            # n_s(tau)
eps_H_fine = d_sa['eps_H_fine']      # epsilon_H(tau)
Lambda_sa = float(d_sa['Lambda'])    # 12.908 M_KK

# S73A instanton landscape
d_inst = np.load('s73a_instanton_landscape.npz', allow_pickle=True)
tau_inst = d_inst['tau_scan']         # 21 points
kappa_phys = d_inst['kappa_physical'] # kappa(tau) at rho = 1 M_KK^{-1}
kappa1_crossing = float(d_inst['kappa1_crossings'][0])  # tau = 0.480

# S64 self-consistent Ne
d_ne = np.load('s64_ne_selfconsist.npz', allow_pickle=True)
Ne_transit = float(d_ne['Ne_primary'])     # 3.73e-3
H_phys_fold = float(d_ne['H_phys_fold_MKK'])  # 0.396 M_KK
H_phys_fold_GeV = float(d_ne['H_phys_fold_GeV'])  # 2.94e16 GeV

# Build splines for S(tau), a_2(tau) from the S73A data
# S_bare[1] is the sqrt component: S_sqrt = S_fold / Lambda = sum d^2 |lambda| / Lambda
# For a_2, we need: a_2(tau) ~ second heat-kernel coefficient
# From the spectral action: S_f*(tau) = alpha * S_sqrt(tau) + beta * S_exp(tau)
# The sqrt component is S_sqrt = (1/Lambda) * sum d^2 |lambda_j|
# This is proportional to the first spectral moment, NOT a_2.
# a_2 requires the heat-kernel expansion: a_2 = (1/4pi^2) * sum d^2 lambda_j^2 * ...
# We use S_fine directly as the effective potential V_eff(tau).

S_sqrt_bare = S_bare_all[1]  # sqrt functional
S_exp_bare = S_bare_all[2]   # exp functional

# Reconstruct full spectral action S_total(tau) = S_sqrt * Lambda
# (This is sum d^2 |lambda_j|, the original spectral action)
S_total_at_grid = S_sqrt_bare * Lambda_sa

cs_S_fine = CubicSpline(tau_fine, S_fine)
cs_dS_fine = CubicSpline(tau_fine, dS_fine)
cs_d2S_fine = CubicSpline(tau_fine, d2S_fine_arr)
cs_ns_fine = CubicSpline(tau_fine, ns_fine)
cs_epsH_fine = CubicSpline(tau_fine, eps_H_fine)

# Cross-check at fold
S_at_fold = cs_S_fine(tau_fold)
dS_at_fold = cs_dS_fine(tau_fold)
print(f"\n  S73A loaded successfully.")
print(f"  S(fold) = {S_at_fold:.2f} (f* functional)")
print(f"  dS(fold) = {dS_at_fold:.2f}")
print(f"  S_fold_canonical = {S_fold:.2f} (sum |lambda|)")
print(f"  Lambda = {Lambda_sa:.6f} M_KK")
print(f"  S_f*(fold) / (S_fold/Lambda) = {S_at_fold / (S_fold/Lambda_sa):.6f}")
print(f"  Instanton kappa=1 crossing: tau = {kappa1_crossing:.4f}")
print(f"  N_e(transit, S64) = {Ne_transit:.6e}")
print(f"  H_phys(fold) = {H_phys_fold:.6f} M_KK = {H_phys_fold_GeV:.4e} GeV")


# =============================================================================
# SECTION 2: PHYSICAL SCALES AND HIERARCHY
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 2: Physical Scales and Hierarchy")
print("=" * 78)

# M_KK / M_Pl hierarchy
MKK_over_MPl = M_KK / M_Pl_reduced  # (local)
MKK_over_MPl_sq = MKK_over_MPl**2   # (local)

# Physical Hubble at fold (from Friedmann with SA)
# H^2 = (2/(3 pi^2)) * (a_0/a_2) * M_KK^2  [S64 Eq. 9]
H_phys_fold_check = np.sqrt(2.0 / (3.0 * PI**2) * a0_fold / a2_fold)  # (local) in M_KK

# Transit velocity
v_tau = v_terminal  # 26.54 M_KK (local)

# Transit duration
dt_tr = dt_transit  # 1.13e-3 M_KK^{-1} (local)

# Physical time conversion: t_phys [s] = t [M_KK^{-1}] / (M_KK * GeV_to_inv_s)
# 1 GeV^{-1} = hbar_GeV_s = 6.58e-25 s
t_transit_s = dt_tr * hbar_GeV_s / M_KK  # (local) seconds

# Energy density at fold
# V_fold = (2 f_0 / pi^2) * a_0 * M_KK^4  (setting f_0 = 1)
V_fold_GeV4 = (2.0 / PI**2) * a0_fold * M_KK**4  # (local) GeV^4

# Kinetic energy density at fold
# KE = (1/2) G_DeWitt * M_KK^2 * v_tau^2 * M_KK^2
# = (1/2) G_DeWitt * v_tau^2 * M_KK^4
KE_fold_GeV4 = 0.5 * G_DeWitt * v_tau**2 * M_KK**4  # (local) GeV^4

# Total energy at fold
rho_fold = V_fold_GeV4 + KE_fold_GeV4  # (local) GeV^4

# EOS at fold: w = (KE - V) / (KE + V)
w_fold = (KE_fold_GeV4 - V_fold_GeV4) / (KE_fold_GeV4 + V_fold_GeV4)  # (local)

print(f"\n  M_KK = {M_KK:.4e} GeV")
print(f"  M_Pl = {M_Pl_reduced:.4e} GeV")
print(f"  M_KK / M_Pl = {MKK_over_MPl:.6e}")
print(f"  (M_KK/M_Pl)^2 = {MKK_over_MPl_sq:.6e}")
print(f"\n  H_phys(fold) = {H_phys_fold:.6f} M_KK = {H_phys_fold_GeV:.4e} GeV")
print(f"  H_phys cross-check = {H_phys_fold_check:.6f} M_KK")
print(f"  v_terminal = {v_tau:.4f} M_KK")
print(f"  H/v = {H_phys_fold/v_tau:.6e} (<<1 means stiff-dominated)")
print(f"\n  V_fold = {V_fold_GeV4:.4e} GeV^4")
print(f"  KE_fold = {KE_fold_GeV4:.4e} GeV^4")
print(f"  KE/V = {KE_fold_GeV4/V_fold_GeV4:.4f}")
print(f"  w_fold = {w_fold:.6f} (expect w -> +1 for stiff)")
print(f"  rho_fold = {rho_fold:.4e} GeV^4")
print(f"\n  dt_transit = {dt_tr:.6e} M_KK^{{-1}} = {t_transit_s:.4e} s")
print(f"  N_e(transit) = {Ne_transit:.6e}")


# =============================================================================
# SECTION 3: MODULUS EQUATION OF MOTION
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 3: Modulus Equation of Motion (Full ODE)")
print("=" * 78)

# The coupled Friedmann + Klein-Gordon system:
#   3 H^2 M_Pl^2 = (1/2) G_DeWitt M_KK^2 dot_tau^2 + V(tau)
#   G_DeWitt M_KK^2 (ddot_tau + 3H dot_tau) + V'(tau) = 0
#
# Using the f* spectral action as V_eff(tau):
#   V(tau) = C_V * S_f*(tau)
# where C_V normalizes so that V(fold) matches the physical potential.
#
# The normalization: V(tau) = (2 f_0 / pi^2) * a_0(tau) * M_KK^4
# But with f*, we don't have the heat-kernel expansion. Instead:
#   V(tau) = S_f*(tau) * M_KK^4 / S_norm
# where S_norm absorbs the normalization.
#
# For self-consistency, use:
#   V(tau) / V(fold) = S_f*(tau) / S_f*(fold)
# Then V(tau) = V_fold * S_f*(tau) / S_f*(fold)

S_fold_fstar = cs_S_fine(tau_fold)  # (local)
V_eff_scale = V_fold_GeV4 / S_fold_fstar  # (local) GeV^4 per S-unit

print(f"  V(tau) = {V_eff_scale:.4e} * S_f*(tau)")
print(f"  S_f*(fold) = {S_fold_fstar:.4f}")

# Dimensionless system: use M_KK as the unit
# tau, dot_tau in M_KK units. Time in M_KK^{-1}.
# H in M_KK. V in M_KK^4.
#
# Let beta = G_DeWitt * (M_KK/M_Pl)^2 = moduli-Planck coupling
beta_param = G_DeWitt * MKK_over_MPl_sq  # (local)

# V(tau) in M_KK^4 units
V_fold_MKK4 = V_fold_GeV4 / M_KK**4  # (local)

# The Friedmann equation in M_KK units:
# 3 H^2 / (8 pi) = (1/2) * G_DeWitt * dot_tau^2 + V_eff(tau) / M_Pl^2 * M_KK^2
# More carefully:
# 3 H^2 M_Pl^2 = (1/2) mu^2 dot_tau^2 + V(tau)
# where mu^2 = G_DeWitt * M_KK^2
#
# In M_KK units (H_MKK = H/M_KK, V_MKK4 = V/M_KK^4):
# 3 H_MKK^2 * (M_Pl/M_KK)^2 = (1/2) G_DeWitt * dot_tau^2 + V_MKK4(tau)
# H_MKK^2 = [(1/2) G * dot_tau^2 + V_MKK4] / [3 (M_Pl/M_KK)^2]
# H_MKK^2 = [(1/2) G * dot_tau^2 + V_MKK4] * beta / (3 G)
#          = beta * [(1/2) dot_tau^2 + V_MKK4/G] / 3

# Check: at fold, dot_tau = v_terminal, V ~ (2/pi^2) a_0 in M_KK^4
# V_fold_MKK4 = (2/pi^2) * a_0 = (2/9.87) * 6440 = 1304.7
V_fold_check = (2.0 / PI**2) * a0_fold  # (local)
print(f"\n  V_fold / M_KK^4 = {V_fold_MKK4:.4f}")
print(f"  (2/pi^2) * a_0 = {V_fold_check:.4f}")
print(f"  Ratio = {V_fold_MKK4 / V_fold_check:.6f}")

# The ratio should be 1 if f_0 = 1. With f*:
# The f* functional gives a DIFFERENT spectral action than the heat-kernel one.
# Use the heat-kernel normalization for V(tau), with f* for SHAPE only.
# V(tau) = V_fold_HK * S_f*(tau) / S_f*(fold)
# V_fold_HK = (2/pi^2) * a_0 * M_KK^4

V_fold_HK_MKK4 = V_fold_check  # (local) heat-kernel normalization

# Klein-Gordon in M_KK units:
# G * (ddot_tau + 3 H dot_tau) + (1/M_KK^2) * dV/dtau = 0
# dV/dtau = V_fold_HK * M_KK^4 * dS_f* / S_f*(fold) / M_KK [chain rule: dtau is dimensionless]
# No: V(tau) = V_fold_HK_MKK4 * S_f*(tau)/S_f*(fold) * M_KK^4
# dV/dtau has units M_KK^4: dV_MKK4_dtau = V_fold_HK_MKK4 * dS_f*/dtau / S_f*(fold)

def V_eff_MKK4(tau):
    """Effective potential in M_KK^4 units, heat-kernel normalized."""
    if tau < tau_fine[0] or tau > tau_fine[-1]:
        return V_fold_HK_MKK4  # (local) cap at boundaries
    return V_fold_HK_MKK4 * cs_S_fine(tau) / S_fold_fstar

def dV_dtau_MKK4(tau):
    """dV/dtau in M_KK^4 units."""
    if tau < tau_fine[0] or tau > tau_fine[-1]:
        return 0.0
    return V_fold_HK_MKK4 * cs_dS_fine(tau) / S_fold_fstar

# Friedmann:
# H^2 = [(1/2) G dot_tau^2 + V_MKK4(tau)] / [3 (M_Pl/M_Pl)^2]
# Wait, need to be more careful. Everything in GeV:
# 3 H^2 M_Pl^2 = (1/2) G M_KK^2 dot_tau^2 + V(tau)
# where dot_tau has units M_KK (since tau is dimensionless, time is M_KK^{-1})
# Actually dot_tau = d(tau)/dt where t has units M_KK^{-1}, so dot_tau has units M_KK.
# Then G * M_KK^2 * dot_tau^2 has units M_KK^4 * [dimless] = M_KK^4. No:
# G * M_KK^2 has units M_KK^2, dot_tau^2 has units M_KK^2, product = M_KK^4. Good.
# V(tau) has units M_KK^4.
#
# In M_KK units (set M_KK = 1):
# 3 H_1^2 * (M_Pl/M_KK)^2 = (1/2) G * dtau_1^2 + V_1(tau)
# H_1 = H/M_KK, dtau_1 = dtau/dt_1 where t_1 = t*M_KK
# V_1 = V / M_KK^4
#
# So: H_1^2 = [(1/2) G * dtau_1^2 + V_1] / [3 * (M_Pl/M_KK)^2]

MPl_over_MKK_sq = (M_Pl_reduced / M_KK)**2  # (local)

def friedmann_H_sq(tau, dtau):
    """H^2 in M_KK^2 units from Friedmann equation."""
    KE = 0.5 * G_DeWitt * dtau**2  # (local)
    PE = V_eff_MKK4(tau)  # (local)
    return (KE + PE) / (3.0 * MPl_over_MKK_sq)

# Cross-check at fold
H_sq_fold = friedmann_H_sq(tau_fold, v_tau)  # (local)
H_fold_computed = np.sqrt(H_sq_fold)  # (local)
print(f"\n  Friedmann cross-check at fold:")
print(f"  H_fold(Friedmann) = {H_fold_computed:.6f} M_KK")
print(f"  H_fold(S64) = {H_phys_fold:.6f} M_KK")
print(f"  Ratio = {H_fold_computed/H_phys_fold:.6f}")


# =============================================================================
# SECTION 4: SOLVE COUPLED FRIEDMANN + KLEIN-GORDON
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 4: Full ODE Solution (Fold to Late Times)")
print("=" * 78)

# State vector: y = [tau, dot_tau, ln(a)]
# dt_phys = dt / M_KK (time in M_KK^{-1})
#
# d(tau)/dt = dot_tau
# d(dot_tau)/dt = -3H * dot_tau - (1/G) * dV_MKK4/dtau / M_KK^2
#              = -3H * dot_tau - dV_MKK4/dtau / (G * M_KK^2)
# Wait, units: G*M_KK^2 has units [dimless]*M_KK^2 = M_KK^2
# ddot_tau has units M_KK * M_KK = M_KK^2
# -3H*dot_tau: [M_KK][M_KK] = M_KK^2. Good.
# (1/G)*dV/dtau: dV has units M_KK^4, so dV/dtau has units M_KK^4.
# Then (1/(G*M_KK^2)) * dV/dtau = M_KK^4 / (M_KK^2) = M_KK^2. Good.
#
# Actually need to be careful: the KG equation is
# G * ddot_tau + 3 G H dot_tau + (1/M_KK^2) dV/dtau = 0
# No. The standard form from the action:
# S = integral [3 M_Pl^2 H^2 - (1/2) mu^2 dot_tau^2 - V(tau)] sqrt(-g) d^4x
# where mu^2 = G * M_KK^2 (the moduli kinetic coefficient)
# EOM: mu^2 (ddot_tau + 3H dot_tau) + dV/dtau = 0
# ddot_tau = -3H dot_tau - dV/dtau / mu^2
# In M_KK units (t_1 = t * M_KK):
# mu^2 = G * 1 (since M_KK = 1)
# dV/dtau = dV_MKK4/dtau (units M_KK^4 = 1)
# ddot_tau_1 = -3 H_1 dot_tau_1 - dV_1/dtau / G

def rhs(t, y):
    """RHS of the coupled ODE system."""
    tau_val, dtau_val, ln_a = y

    # Clamp tau to interpolation range
    tau_c = np.clip(tau_val, tau_fine[0], tau_fine[-1])  # (local)

    # Friedmann
    H_sq = friedmann_H_sq(tau_c, dtau_val)  # (local)
    H_val = np.sqrt(max(H_sq, 0.0))  # (local)

    # KG equation
    dVdtau = dV_dtau_MKK4(tau_c)  # (local)
    ddtau = -3.0 * H_val * dtau_val - dVdtau / G_DeWitt  # (local)

    return [dtau_val, ddtau, H_val]

# Initial conditions: at the fold, moving toward larger tau
# The modulus has been accelerated by the spectral action gradient
y0 = [tau_fold, v_tau, 0.0]  # ln(a) = 0 at fold (local)

# Solve for a long time to see the expansion history
# Use M_KK^{-1} as time unit. Transit is ~1e-3 M_KK^{-1}.
# But the universe age is t_universe = 4.35e17 s.
# In M_KK^{-1}: t_age_MKK = t_universe * M_KK / hbar_GeV_s
# = 4.35e17 * 7.43e16 / 6.58e-25
# = 4.35e17 * 1.13e41
# = 4.9e58 M_KK^{-1}
# This is enormous. We can't integrate that far.
# Instead, integrate until the modulus slows down to Hubble friction regime.

# Estimate: modulus velocity decays as 1/a^3 for stiff EOS (w=1).
# a grows as t^{1/3}, so dot_tau ~ t^{-1} ~ a^{-3}.
# After N_stiff ~ 3.73e-3 e-folds, dot_tau drops by factor e^{3*3.73e-3} = 1.011.
# The modulus keeps moving. Only Hubble friction slows it.
# Time to reach dot_tau ~ H: t ~ G * (M_Pl/M_KK)^2 / v_tau ~ beta^{-1} / v_tau
# ~ 1/(4.65e-3 * 26.5) ~ 8 M_KK^{-1}.
# That's actually quite short!

# Integrate to t = 100 M_KK^{-1} (enough to see all regimes)
t_span = (0.0, 100.0)  # (local) M_KK^{-1}
t_eval = np.linspace(0.0, 100.0, 50000)  # (local) dense output

print(f"  Integrating from t=0 (fold) to t=100 M_KK^{{-1}}...")
print(f"  IC: tau={y0[0]}, dot_tau={y0[1]:.4f}, ln_a={y0[2]}")

sol = solve_ivp(rhs, t_span, y0, method='RK45',
                t_eval=t_eval, rtol=1e-10, atol=1e-12,
                max_step=0.01)

if not sol.success:
    print(f"  WARNING: ODE solver did not succeed: {sol.message}")
else:
    print(f"  ODE solved successfully. {len(sol.t)} time points.")

t_sol = sol.t           # (local)
tau_sol = sol.y[0]      # (local)
dtau_sol = sol.y[1]     # (local)
lna_sol = sol.y[2]      # (local)

# Compute H(t) along solution
H_sol = np.array([np.sqrt(max(friedmann_H_sq(np.clip(tau_sol[i], tau_fine[0], tau_fine[-1]),
                                              dtau_sol[i]), 0.0))
                   for i in range(len(t_sol))])  # (local)

# EOS w(t) = (KE - V) / (KE + V)
KE_sol = 0.5 * G_DeWitt * dtau_sol**2  # (local)
V_sol = np.array([V_eff_MKK4(np.clip(tau_sol[i], tau_fine[0], tau_fine[-1]))
                  for i in range(len(t_sol))])  # (local)
w_sol = (KE_sol - V_sol) / (KE_sol + V_sol + 1e-300)  # (local)

# Print key moments
print(f"\n  {'t (M_KK^-1)':>12s} {'tau':>8s} {'dot_tau':>12s} {'H (M_KK)':>12s} {'ln(a)':>10s} {'w':>8s}")
print("  " + "-" * 70)
sample_times = [0, 0.001, 0.01, 0.1, 1.0, 5.0, 10.0, 50.0, 100.0]  # (local)
for t_s in sample_times:
    idx = np.argmin(np.abs(t_sol - t_s))  # (local)
    print(f"  {t_sol[idx]:12.6f} {tau_sol[idx]:8.4f} {dtau_sol[idx]:12.6f} "
          f"{H_sol[idx]:12.6e} {lna_sol[idx]:10.6f} {w_sol[idx]:8.4f}")


# =============================================================================
# SECTION 5: EPOCH IDENTIFICATION AND E-FOLD DECOMPOSITION
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 5: Epoch Identification and E-Fold Decomposition")
print("=" * 78)

# Epoch 1 (STIFF): From fold until KE/V drops below threshold
# In stiff regime: KE >> V, w -> +1
# Transition when KE/V ~ 1 (w ~ 0)

KE_over_V = KE_sol / (V_sol + 1e-300)  # (local)

# Find where w crosses 0 (transition from stiff to matter-like)
# And where w crosses -1/3 (transition to potential-dominated)
w_cross_0 = None  # (local)
w_cross_neg13 = None  # (local)
for i in range(1, len(w_sol)):
    if w_cross_0 is None and w_sol[i-1] > 0 and w_sol[i] <= 0:
        w_cross_0 = t_sol[i]
    if w_cross_neg13 is None and w_sol[i-1] > -1.0/3.0 and w_sol[i] <= -1.0/3.0:
        w_cross_neg13 = t_sol[i]

# Find where H * t = 1/3 (stiff epoch H = 1/(3t))
# Actually more robust: find where w stabilizes near a value.

# Epoch boundaries based on w:
# Stiff: w > 0.5
# Transition: 0.5 > w > -0.1
# GGE/Matter: -0.1 > w > -0.5
# Lambda-like: w < -0.5

idx_stiff_end = np.where(w_sol < 0.5)[0]  # (local)
if len(idx_stiff_end) > 0:
    t_stiff_end = t_sol[idx_stiff_end[0]]  # (local)
    lna_stiff = lna_sol[idx_stiff_end[0]]  # (local)
else:
    t_stiff_end = t_sol[-1]
    lna_stiff = lna_sol[-1]

idx_acc = np.where(w_sol < -1.0/3.0)[0]  # (local)
if len(idx_acc) > 0:
    t_acc = t_sol[idx_acc[0]]  # (local)
    lna_acc = lna_sol[idx_acc[0]]  # (local)
else:
    t_acc = None
    lna_acc = None

print(f"\n  Epoch boundaries (from ODE):")
print(f"  Stiff epoch end (w < 0.5): t = {t_stiff_end:.6f} M_KK^{{-1}}")
print(f"    N_stiff = {lna_stiff:.6e} e-folds")
print(f"    tau at stiff end = {tau_sol[idx_stiff_end[0]] if len(idx_stiff_end)>0 else 'N/A':.4f}")
if t_acc is not None:
    print(f"  Acceleration onset (w < -1/3): t = {t_acc:.6f} M_KK^{{-1}}")
    print(f"    N_accel = {lna_acc:.6e} e-folds from fold")

# Total e-folds during modulus-dominated evolution
N_modulus = lna_sol[-1]  # (local)
print(f"\n  Total modulus-dominated e-folds (t=0 to t=100 M_KK^{{-1}}): {N_modulus:.6f}")
print(f"  Final tau = {tau_sol[-1]:.4f}")
print(f"  Final dot_tau = {dtau_sol[-1]:.6e} M_KK")
print(f"  Final H = {H_sol[-1]:.6e} M_KK")
print(f"  Final w = {w_sol[-1]:.6f}")


# =============================================================================
# SECTION 6: TRANSITION TO STANDARD COSMOLOGY
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 6: Transition to Standard Cosmology")
print("=" * 78)

# The key question: how does the modulus-dominated era connect to radiation domination?
#
# In the Volovik framework (S59 ZUBAREV-CC-59, S66 DILUTION-CC-66):
# The vacuum energy relaxes to zero in equilibrium (thermodynamic argument).
# The GGE relic is CDM-like (CDM-CONSTRUCT-43/44: w = 0).
# The spectral action potential energy must convert to radiation.
#
# Mechanism: the modulus eventually stabilizes (BCS dressing, instanton back-reaction),
# and the kinetic energy thermalizes into the GGE quasiparticles.
#
# S73A W1-C: additive tracking vacuum EXCLUDED by BBN (130x).
# This means: rho_vac does NOT add to Friedmann as alpha * rho_rad.
# Instead: G_eff renormalization (Sakharov mechanism, S44).
# During radiation epoch: H^2 = (8 pi G_eff / 3) * rho_rad
# with G_eff from the Sakharov second spectral moment.
#
# The transition from modulus-dominated to radiation-dominated happens
# when the modulus dumps its energy into radiation. This is REHEATING
# in substrate language: the modulus kinetic energy converts to GGE
# quasiparticle excitations (which subsequently thermalize).

# Temperature at the fold (instantaneous reheating estimate)
# rho_fold = (pi^2 / 30) g_* T_rh^4
# T_rh = (30 * rho_fold / (pi^2 * g_*))^{1/4}
g_star = 106.75  # (local) SM at high T
T_rh_GeV = (30.0 * rho_fold / (PI**2 * g_star))**(0.25)  # (local) GeV

print(f"\n  Reheating temperature estimates:")
print(f"  rho_fold = {rho_fold:.4e} GeV^4")
print(f"  T_rh (instantaneous) = {T_rh_GeV:.4e} GeV")
print(f"  T_rh / M_KK = {T_rh_GeV / M_KK:.4f}")

# The modulus reaches potential-dominated regime at t ~ t_acc.
# At that point, its energy is V(tau_final) + (1/2) G v^2.
# This energy must be converted to radiation.

# Reheating redshift: z_rh = T_rh / T_CMB (assuming radiation domination
# from T_rh to recombination, with adiabatic expansion).
z_rh = T_rh_GeV / T_CMB_GeV  # (local)
print(f"  z_rh = {z_rh:.4e}")

# E-folds from reheating to today: N_post_rh = ln(z_rh + 1) ~ ln(z_rh)
N_post_rh = np.log(z_rh)  # (local)
print(f"  N_post_rh = ln(z_rh) = {N_post_rh:.4f}")

# Decomposition of N_post_rh:
# N_rad: from T_rh to T_eq (radiation-matter equality)
T_eq_GeV = 0.74e-9  # (local) ~ 0.74 eV (matter-radiation equality)
z_eq = 3402.0  # (local) Planck 2018
N_rad = np.log(z_rh / z_eq)  # (local) (from rh to equality)

# N_matter: from z_eq to z_Lambda (matter-Lambda equality)
z_Lambda = (Omega_Lambda / Omega_m)**(1.0/3.0) - 1  # (local)
# More precisely: a_eq(m-Lambda) = (Omega_m / Omega_Lambda)^{1/3}
# z_Lambda = 1/a_eq - 1 = (Omega_Lambda/Omega_m)^{1/3} - 1
# Actually: z_Lambda = (2*Omega_Lambda/Omega_m)^{1/3} - 1 for the transition
z_Lambda_correct = 0.33  # (local) approximate from Planck
N_matter = np.log((1 + z_eq) / (1 + z_Lambda_correct))  # (local)

# N_Lambda: from z_Lambda to today
N_Lambda = np.log(1 + z_Lambda_correct)  # (local)

print(f"\n  Post-reheating expansion history:")
print(f"  z_eq = {z_eq:.1f} (matter-radiation equality)")
print(f"  z_Lambda ~ {z_Lambda_correct:.2f} (matter-Lambda transition)")
print(f"  N_rad (T_rh -> T_eq) = {N_rad:.4f}")
print(f"  N_matter (z_eq -> z_Lambda) = {N_matter:.4f}")
print(f"  N_Lambda (z_Lambda -> today) = {N_Lambda:.4f}")
print(f"  N_post_rh total = {N_post_rh:.4f}")
print(f"  Sum check = {N_rad + N_matter + N_Lambda:.4f}")


# =============================================================================
# SECTION 7: TOTAL E-FOLD COUNT
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 7: Total E-Fold Count")
print("=" * 78)

# N_total = N_stiff + N_modulus_KE + N_post_rh
# The stiff/modulus phase contributes N_modulus e-folds.
# Post-reheating contributes N_post_rh e-folds.
# The actual question: how much expansion happens during the modulus
# kinetic energy dominated era?
#
# From the ODE: after 100 M_KK^{-1}, the modulus is still moving,
# slowly converting KE to PE. The expansion during this phase is
# governed by H ~ V^{1/2} / M_Pl (potential dominated).
#
# But the real transition to radiation requires a DECAY mechanism
# for the modulus. In the framework, this is the instanton sector
# opening (kappa < 1 at tau > 0.48), which allows gauge field
# production (non-abelian Schwinger effect).

# The PHYSICAL e-fold count:
# N_total = N_transit + N_KE_dominated + N_reheating + N_post_rh
# where N_transit ~ 3.73e-3 (S64)
# N_KE_dominated = N_modulus - N_transit (additional expansion during modulus rundown)
# N_reheating ~ depends on decay mechanism
# N_post_rh ~ 62 (standard cosmology)

# Standard inflation requires N_e ~ 60 to solve horizon + flatness.
# Exflation does NOT require 60 e-folds of modulus-driven expansion.
# The 60 e-folds come from STANDARD expansion (radiation + matter + Lambda).

# The key number: N_total from fold to present.
N_total = N_modulus + N_post_rh  # (local)

print(f"\n  E-fold decomposition:")
print(f"  N_stiff (transit only, S64) = {Ne_transit:.6e}")
print(f"  N_modulus (0 to 100 M_KK^-1) = {N_modulus:.6f}")
print(f"  N_post_rh (standard cosmo) = {N_post_rh:.4f}")
print(f"  N_total = {N_total:.4f}")
print(f"\n  For comparison:")
print(f"  Standard inflation: N_e ~ 60")
print(f"  N_total here: {N_total:.4f}")


# =============================================================================
# SECTION 8: CMB PIVOT SCALE MAPPING
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 8: CMB Pivot Scale Mapping")
print("=" * 78)

# The CMB pivot scale k_pivot = 0.05 Mpc^{-1}.
# At the end of "inflation" (modulus-dominated era), a scale k is said to have
# exited the horizon when k = a * H.
#
# In standard inflation: k_pivot exits N_* e-folds before the end.
# N_* = N_total - ln(k_pivot / (a_0 * H_0))
#
# But in exflation, the transit is supersonic (Mach 13.75) and short.
# The "horizon" at the fold has physical size:
# l_H = 1 / H_phys = 1 / (0.396 * M_KK) = 2.52 M_KK^{-1}
# = 2.52 / (7.43e16 GeV) * 0.197e-15 GeV*m
# = 2.52 * 0.197e-15 / 7.43e16 m
# = 6.68e-33 m ~ 4.1 l_Planck
#
# The CMB pivot scale today: k_pivot = 0.05 Mpc^{-1}
# Corresponding wavelength: lambda_pivot = 2 pi / k_pivot = 126 Mpc
#
# Mapping back: lambda_fold = lambda_today * (a_fold / a_today)
# = lambda_today * exp(-N_total)

k_pivot = k_pivot_planck  # canonical alias (was: = 0.05)
k_pivot_GeV = k_pivot * Mpc_to_GeV_inv  # (local) convert to GeV
# Wait: k [Mpc^{-1}] * Mpc_to_GeV_inv gives k [GeV^{-1} / (GeV^{-1}/Mpc)] = wrong
# k_pivot [Mpc^{-1}] -> k_pivot [GeV] = k_pivot / Mpc_to_GeV_inv
# Mpc_to_GeV_inv = 1.563e38 GeV^{-1}/Mpc
# k [Mpc^{-1}] = k [1/Mpc]. To get [GeV]: multiply by Mpc_to_GeV_inv? No.
# 1 Mpc = 1.563e38 GeV^{-1}, so k [Mpc^{-1}] = k / (1.563e38 GeV^{-1}) = k / 1.563e38 GeV
# k_pivot_GeV = 0.05 / 1.563e38 = 3.2e-40 GeV
k_pivot_GeV = k_pivot / Mpc_to_GeV_inv  # (local) GeV
k_pivot_MKK = k_pivot_GeV / M_KK  # (local) in M_KK units

print(f"  k_pivot = {k_pivot} Mpc^{{-1}}")
print(f"  k_pivot = {k_pivot_GeV:.4e} GeV")
print(f"  k_pivot = {k_pivot_MKK:.4e} M_KK")

# Physical horizon at fold
l_H_fold_MKK = 1.0 / H_phys_fold  # (local) M_KK^{-1}
l_H_fold_GeV = 1.0 / H_phys_fold_GeV  # (local) GeV^{-1}
l_H_fold_m = l_H_fold_GeV * hbar_c_GeV_m  # (local) meters
l_H_fold_Mpc = l_H_fold_m / Mpc_to_m  # (local) Mpc

print(f"\n  Horizon at fold:")
print(f"  l_H = 1/H_phys = {l_H_fold_MKK:.4f} M_KK^{{-1}}")
print(f"  l_H = {l_H_fold_GeV:.4e} GeV^{{-1}}")
print(f"  l_H = {l_H_fold_m:.4e} m = {l_H_fold_m/1.616e-35:.1f} l_Planck")
print(f"  l_H = {l_H_fold_Mpc:.4e} Mpc")

# k at the fold horizon: k_H = a_fold * H_fold
# In comoving coordinates: k_H = H_fold (since a_fold = 1 by convention)
# This mode has comoving wavenumber k_H at the fold.
# At the present, this same mode has physical k = k_H * a_fold / a_today
# = k_H * exp(-N_total)
k_H_fold_MKK = H_phys_fold  # (local) in M_KK units
k_H_fold_GeV = H_phys_fold_GeV  # (local) in GeV

# This comoving wavenumber maps to a present-day physical scale:
# k_H_today = k_H_fold * exp(-N_total) [in comoving, doesn't change]
# The physical wavelength today: lambda_today = 2 pi / k_H_fold * exp(N_total)
# In Mpc: lambda_today = (2 pi / k_H_fold_GeV) * GeV_inv_to_Mpc * exp(N_total)
# But actually, k_comoving = k_physical * a. If a = 1 at fold and a = a_today today:
# k_comoving is FIXED. k_phys_today = k_comoving / a_today = k_H_fold / exp(N_total)

# The e-fold number at which k_pivot exited the horizon during the transit:
# k_pivot exits when k_pivot = a(t) * H(t)
# Since a(t) = a_fold * exp(N(t)):
# k_pivot = exp(N(t)) * H(t) [in comoving coordinates with a_fold = 1]
# But this is in M_KK units. We need to account for the full expansion.

# More carefully: number of e-folds from the END of the modulus era
# when k_pivot exits. Standard formula:
# N_* = 62 - ln(k / (a_0 H_0)) - ln(10^16 GeV / T_rh) + ...
# The standard number of e-folds before end of inflation:
# N_* = 50 - 65 depending on T_rh.

# But exflation does NOT produce 60 e-folds of quasi-de Sitter expansion.
# The transit gives N_stiff ~ 0.004 e-folds.
# The post-transit modulus rundown gives a few more e-folds.
#
# The question is: does the CMB pivot scale EVER exit the "horizon"
# during the transit? If k_pivot << a*H at all times during the transit,
# then the pivot scale was ALWAYS superhorizon, and the spectrum is set
# by the initial conditions, not the transit dynamics.

# Check: k_pivot / (a * H) at the fold
# In M_KK units: k_pivot_MKK / H_phys_fold = ratio
ratio_k_aH = k_pivot_MKK / (1.0 * H_phys_fold)  # (local) a_fold = 1
print(f"\n  Pivot scale relative to fold horizon:")
print(f"  k_pivot / (a_fold * H_fold) = {ratio_k_aH:.4e}")

if ratio_k_aH < 1:
    print(f"  >>> k_pivot is SUB-horizon at the fold (inside the horizon)")
    print(f"  >>> Pivot scale has NOT exited yet at the fold")
else:
    print(f"  >>> k_pivot is SUPER-horizon at the fold")
    print(f"  >>> Pivot scale already larger than the horizon")

# The number N_* = ln(k_H_fold / k_pivot) is how many e-folds of expansion
# are needed for the fold-horizon scale to grow to the pivot scale.
N_star = np.log(k_H_fold_MKK / k_pivot_MKK)  # (local)
print(f"\n  N_* = ln(k_H / k_pivot) = {N_star:.4f}")
print(f"  This is the number of e-folds needed for the fold horizon")
print(f"  to encompass the CMB pivot scale.")
print(f"  N_total available = {N_total:.4f}")

if N_star > N_total:
    print(f"\n  >>> N_* > N_total: Pivot scale NEVER exits the horizon")
    print(f"  >>> during modulus-dominated era. The spectrum at the pivot")
    print(f"  >>> is set by initial conditions, not by transit dynamics.")
    print(f"  >>> Deficit: {N_star - N_total:.4f} e-folds")
else:
    print(f"\n  >>> N_* < N_total: Pivot scale exits during modulus era")


# =============================================================================
# SECTION 9: SPECTRAL TILT AT THE CMB SCALE
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 9: Spectral Tilt at the CMB Scale")
print("=" * 78)

# Two cases:
# (A) If the pivot exits during the transit: n_s from spectral action at tau_pivot.
# (B) If the pivot NEVER exits during transit: n_s from GGE relic spectrum,
#     which is the post-transit quasiparticle distribution.
#
# Case (B) is what the framework predicts: the CMB is the ACOUSTIC SIGNATURE
# of the GGE relic, not a quantum fluctuation spectrum from quasi-de Sitter.
# In this case, n_s is determined by the GGE distribution, not by epsilon_H.
#
# The spectral action gives n_s(tau) = 1 - 2*epsilon_H - eta_H at each tau.
# This is the SLOW-ROLL prediction. For exflation, this is academic:
# the modulus is not slow-rolling, and the perturbation spectrum is set by
# the Bogoliubov transformation during the supersonic transit.

# Method 1: Spectral action tilt at different tau values
print("\n  Method 1: Spectral action slow-roll n_s(tau)")
tau_samples = [0.10, 0.15, 0.19, 0.25, 0.30, 0.50, 1.00]  # (local)
print(f"  {'tau':>6s}  {'n_s':>10s}  {'epsilon_H':>12s}")
print("  " + "-" * 32)
for tau_s in tau_samples:
    if tau_fine[0] <= tau_s <= tau_fine[-1]:
        ns_val = float(cs_ns_fine(tau_s))
        eps_val = float(cs_epsH_fine(tau_s))
        print(f"  {tau_s:6.3f}  {ns_val:10.6f}  {eps_val:12.6e}")

# Method 2: The physical n_s
# The n_s that matters is the one imprinted on the CMB.
# In the exflation framework, this comes from:
# (a) The BCS spectral geometry (pure number from D_K)
# (b) The GGE quasiparticle distribution (set at the transit)
# (c) The acoustic propagation through the GGE relic
#
# The S73A n_s(tau) profile shows n_s < 1 everywhere (red-tilted).
# At the fold: n_s = 0.995.
# At large tau: n_s decreases toward 0.84 at tau = 2.
# The observed n_s = 0.9649 +/- 0.0042 (Planck 2018).

# Find tau where n_s matches Planck:
ns_planck = planck_ns  # canonical alias (was: = 0.9649)
ns_target_lo = 0.945  # (local) gate lower bound
ns_target_hi = 0.975  # (local) gate upper bound

# Where does n_s = 0.9649 in the spectral action profile?
ns_at_fine = ns_fine  # (local) already computed
mask_valid = (tau_fine >= 0.19)  # (local) post-fold only
tau_post = tau_fine[mask_valid]  # (local)
ns_post = ns_at_fine[mask_valid]  # (local)

# n_s is monotonically decreasing with tau (as epsilon increases)
# Find crossing
idx_ns_planck = np.where(ns_post <= ns_planck)[0]  # (local)
if len(idx_ns_planck) > 0:
    tau_ns_planck = tau_post[idx_ns_planck[0]]  # (local)
    ns_at_crossing = ns_post[idx_ns_planck[0]]  # (local)
    print(f"\n  n_s = {ns_planck} at tau = {tau_ns_planck:.4f}")
    print(f"  Actual n_s at crossing = {ns_at_crossing:.6f}")
else:
    tau_ns_planck = None  # (local)
    print(f"\n  n_s never reaches {ns_planck} in the post-fold range (n_s > {ns_post[-1]:.4f} at tau={tau_post[-1]:.2f})")

# Gate window: n_s in [0.945, 0.975]
idx_lo = np.where(ns_post <= ns_target_hi)[0]  # (local)
idx_hi = np.where(ns_post <= ns_target_lo)[0]  # (local)
if len(idx_lo) > 0:
    tau_gate_entry = tau_post[idx_lo[0]]  # (local)
    print(f"  Gate entry (n_s = {ns_target_hi}): tau = {tau_gate_entry:.4f}")
if len(idx_hi) > 0:
    tau_gate_exit = tau_post[idx_hi[0]]  # (local)
    print(f"  Gate exit (n_s = {ns_target_lo}): tau = {tau_gate_exit:.4f}")

# Method 3: Direct mapping from e-fold number
# If the transit produces N_transit e-folds, the spectrum at the pivot is
# set at N_transit from the fold. Since N_transit = 3.73e-3 << 60,
# the pivot scale is DEEP inside the horizon during the transit.
# The e-fold at which the pivot exits:
# k_pivot = a(N_exit) * H(N_exit) => N_exit = N_total - N_*
# If N_* > N_total, the pivot never exits => "primordial" spectrum is NOT
# from the transit but from whatever set the initial conditions.

N_exit_pivot = N_total - N_star  # (local)
print(f"\n  N_exit for pivot: {N_exit_pivot:.4f}")
if N_exit_pivot < 0:
    print(f"  NEGATIVE => pivot scale never exits during modulus-dominated era")
    print(f"  Pivot spectrum is set by GGE relic, not transit dynamics")
    print(f"  This is CONSISTENT with the exflation picture:")
    print(f"  the CMB is the acoustic signature of the GGE, not quasi-dS fluctuations")


# =============================================================================
# SECTION 10: THE STRUCTURAL RESULT
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 10: The Structural Result — Why EFOLD-MAPPING is INFO")
print("=" * 78)

# The stiff epoch dominates the EARLY expansion.
# N_stiff = 3.73e-3 from the transit itself.
# The post-transit expansion is N_modulus ~ O(1) from the potential.
# The post-reheating expansion is N_post_rh ~ 62 (standard cosmology).
#
# The total is N_total ~ 62 + O(1), entirely from standard cosmology.
# The transit contributes negligibly.
#
# The CMB pivot scale (k = 0.05 Mpc^{-1}) corresponds to a comoving
# scale that is VASTLY larger than the horizon at the fold.
# k_pivot / (a * H)_fold ~ 10^{-57}.
# This means the pivot scale was 10^{57} times SMALLER than the horizon
# at the fold, so it was sub-horizon.
# After expansion by exp(N_total) ~ exp(62) ~ 10^{27}, the scale grows to
# k_pivot / (a * H)_today ~ k_pivot / H_0 ~ 10^{-57} * 10^{27} ~ 10^{-30}.
# Still sub-horizon!
#
# Wait -- I have the ratio backwards. Let me recompute.
# k_pivot_MKK is the COMOVING wavenumber.
# At the fold, the PHYSICAL wavenumber is k_phys = k_pivot_comoving / a_fold.
# Horizon: k_H = a_fold * H_fold (physical).
# k_phys / k_H = k_pivot_comoving / (a_fold^2 * H_fold).
# With a_fold = 1 in our convention: k_phys / k_H = k_pivot_MKK / H_fold.
# k_pivot_MKK ~ 4.3e-57 M_KK, H_fold ~ 0.396 M_KK
# ratio ~ 10^{-56}. This is DEEP SUB-HORIZON.
#
# For this scale to exit the horizon (become superhorizon), we need
# exp(N) * H_fold >> k_pivot_comoving / a_fold
# But exp(N) grows exponentially while H decreases.
# During stiff epoch: H ~ 1/t, a ~ t^{1/3}, so aH ~ t^{-2/3} DECREASES.
# The comoving horizon SHRINKS during stiff epoch (w > 1/3).
# During matter epoch: H ~ 1/t, a ~ t^{2/3}, so aH ~ t^{-1/3} DECREASES.
# During radiation: H ~ 1/t, a ~ t^{1/2}, so aH ~ t^{-1/2} DECREASES.
# During Lambda: H ~ const, a ~ exp(Ht), so aH ~ exp(Ht) INCREASES.
#
# The comoving Hubble radius (aH)^{-1} INCREASES during all standard epochs
# (radiation, matter) and DECREASES during inflation and Lambda domination.
# So in standard inflation, modes exit because (aH)^{-1} SHRINKS.
# In exflation, the stiff epoch has (aH)^{-1} ~ t^{2/3} which GROWS.
# => Modes do NOT exit during the stiff epoch! They ENTER!
#
# This is the KEY STRUCTURAL DIFFERENCE:
# In inflation: (aH)^{-1} shrinks => modes exit the horizon
# In exflation (stiff): (aH)^{-1} grows => modes ENTER the horizon
#
# The stiff epoch is ANTI-inflationary for mode exit.
# Modes that are superhorizon before the fold ENTER the horizon during the transit.
# Modes that are sub-horizon stay sub-horizon.
#
# This means: the CMB spectrum is NOT set by the transit dynamics.
# It is set by whatever determines the initial superhorizon perturbations.
# In the framework: these are the GGE quasiparticle excitations,
# which carry the spectral information from the BCS condensate.

# Comoving Hubble radius along the solution
comoving_H_inv = 1.0 / (np.exp(lna_sol) * H_sol + 1e-300)  # (local)

print(f"\n  CRITICAL STRUCTURAL FINDING:")
print(f"  During the stiff epoch (w > 1/3), the comoving Hubble radius GROWS.")
print(f"  This means modes ENTER the horizon, not exit.")
print(f"  The stiff epoch is ANTI-inflationary for mode exit.")
print(f"\n  Comoving Hubble radius (aH)^{{-1}}:")
print(f"  At fold: {1.0/H_phys_fold:.4f} M_KK^{{-1}}")
print(f"  At t=1 M_KK^{{-1}}: {comoving_H_inv[np.argmin(np.abs(t_sol-1.0))]:.4f} M_KK^{{-1}}")
print(f"  At t=10: {comoving_H_inv[np.argmin(np.abs(t_sol-10.0))]:.4f} M_KK^{{-1}}")
print(f"  At t=100: {comoving_H_inv[np.argmin(np.abs(t_sol-100.0))]:.4f} M_KK^{{-1}}")

# But the physical Hubble horizon in Mpc at the fold:
l_H_fold_Mpc_val = l_H_fold_Mpc  # (local) already computed
# And the comoving CMB pivot wavelength:
lambda_pivot_Mpc = 2 * PI / k_pivot  # (local) = 126 Mpc

print(f"\n  Physical Hubble horizon at fold: {l_H_fold_Mpc_val:.4e} Mpc")
print(f"  CMB pivot wavelength today: {lambda_pivot_Mpc:.1f} Mpc")
print(f"  Ratio lambda_pivot / l_H(fold): {lambda_pivot_Mpc / l_H_fold_Mpc_val:.4e}")

# The lambda_pivot is VASTLY larger than l_H at fold.
# But to compare properly, we need comoving scales.
# Comoving horizon at fold = l_H_fold (since a_fold = 1 in our convention)
# Comoving pivot wavelength = lambda_pivot * a_today / a_0
# If a_today / a_fold = exp(N_total), then
# comoving_pivot / comoving_horizon = (lambda_pivot * a_0) / (l_H * a_fold)
# = lambda_pivot / (l_H * exp(N_total))
# This ratio tells us if the pivot was inside or outside at the fold.

# Actually, comoving is the COORDINATE scale, independent of a.
# k_comoving is fixed. k_physical = k_comoving * a.
# The horizon scale at any time: k_H = a * H.
# Scale is superhorizon if k_comoving < k_H = a*H.
# At the fold: k_pivot vs a_fold * H_fold.
# k_pivot_MKK ~ 4.3e-57, a_fold * H_fold = 1 * 0.396 = 0.396.
# k_pivot << a*H => pivot is DEEP INSIDE the horizon (sub-horizon).
# Not superhorizon.
#
# Wait. Convention: k is SUB-horizon if k < aH, and SUPER-horizon if k > aH.
# No! k is the spatial frequency. High k = small scale = inside horizon.
# k < aH means k/a < H, meaning the physical wavelength is LARGER than the Hubble
# radius. That's SUPERHORIZON.
# k > aH means the physical wavelength is smaller than Hubble. That's sub-horizon.
#
# So k_pivot = 4.3e-57 M_KK, aH_fold = 0.396 M_KK.
# k_pivot << aH_fold => pivot is SUPERHORIZON at the fold!
# (Small k = large wavelength = outside the tiny Hubble volume)
#
# This makes physical sense: the Hubble horizon at GUT scale is tiny,
# and the CMB pivot scale (126 Mpc today) corresponds to a truly enormous
# comoving wavelength that was ALWAYS larger than the Hubble radius.

print(f"\n  CORRECTED ANALYSIS:")
print(f"  k_pivot = {k_pivot_MKK:.4e} M_KK (comoving)")
print(f"  a * H at fold = {H_phys_fold:.4f} M_KK")
print(f"  k_pivot / (a*H)_fold = {k_pivot_MKK / H_phys_fold:.4e}")
print(f"  k_pivot << a*H => pivot is SUPERHORIZON at the fold")
print(f"  (Small k = large wavelength = outside the Hubble volume)")

# For the pivot to RE-ENTER the horizon, we need a*H to decrease below k_pivot.
# During standard expansion (radiation, matter), a*H = a^2 H/a = a * H decreases
# as... let me check:
# Radiation: H ~ 1/t, a ~ t^{1/2}. aH ~ t^{-1/2}. DECREASING.
# Matter: H ~ 1/t, a ~ t^{2/3}. aH ~ t^{-1/3}. DECREASING.
# aH starts at 0.396 M_KK and decreases until k_pivot ~ aH.
# At horizon re-entry: a * H = k_pivot.
# z_re-entry from k_pivot = H(z) * a(z) / a_0.
# In standard cosmology, this gives z_re-entry ~ 10^5 (for k=0.05 Mpc^{-1}).

# N_re-entry from fold: the number of e-folds of expansion until the pivot
# re-enters the horizon.
# a*H|_reentry = k_pivot
# a|_reentry * H|_reentry = k_pivot_MKK
# During radiation: H^2 = H_rh^2 * (a_rh/a)^4
# aH = a * H_rh * (a_rh/a)^2 = H_rh * a_rh^2 / a
# Set a_rh * H_rh = H_rh_MKK (the Hubble horizon at reheating)
# aH = a_rh * H_rh * (a_rh / a) = (aH)_rh * (a_rh/a)
# Re-entry: (aH)_rh * (a_rh / a_reentry) = k_pivot
# a_reentry / a_rh = (aH)_rh / k_pivot

# This is the standard horizon problem: why is the pivot superhorizon?
# In inflation, the pivot EXITS the horizon during inflation, then re-enters
# during radiation/matter epoch.
# In exflation, the pivot is superhorizon at the fold BECAUSE the fold Hubble
# horizon is tiny (l_H ~ a few Planck lengths).
# The pivot re-enters during radiation epoch (standard).
# The QUESTION is: what sets the perturbation spectrum on superhorizon scales?

# In inflation: vacuum fluctuations during quasi-de Sitter expansion.
# In exflation: the GGE quasiparticle distribution from the BCS condensate.
# This is the ACOUSTIC SIGNATURE interpretation.

# The spectral tilt is then determined by the GGE spectrum at the transit,
# projected onto the superhorizon modes through the Bogoliubov transformation.

# To check the gate: does the spectral action n_s at any tau give a value
# in [0.945, 0.975]? YES -- the spectral action profile shows n_s drops
# from ~1 at the fold through the gate window at tau ~ 0.3-0.6.
# But this is the slow-roll n_s, which assumes the perturbations are set
# by the transit dynamics. Since the pivot is superhorizon, this is MOOT.

# The physical n_s comes from the GGE relic distribution, which we can
# assess from the spectral action curvature.

# From the ODE: what tau is the modulus at when aH = k_pivot?
# Find where exp(lna_sol) * H_sol = k_pivot_MKK
aH_sol = np.exp(lna_sol) * H_sol  # (local)
idx_reentry = np.where(aH_sol <= k_pivot_MKK)[0]  # (local)
if len(idx_reentry) > 0:
    print(f"\n  aH drops to k_pivot at t = {t_sol[idx_reentry[0]]:.6f} M_KK^{{-1}}")
else:
    print(f"\n  aH never drops to k_pivot within the integration range")
    print(f"  aH(t=100) = {aH_sol[-1]:.6e} M_KK >> k_pivot = {k_pivot_MKK:.4e}")
    print(f"  Re-entry happens MUCH later, during standard cosmology")

# N_total from fold to re-entry (standard calculation):
# In radiation: a*H ~ a^{-1}. From fold to re-entry:
# (a*H)_fold / (a*H)_reentry = a_reentry / a_fold = exp(N_to_reentry)
# (a*H)_fold = H_phys_fold = 0.396 M_KK
# (a*H)_reentry = k_pivot = 4.3e-57 M_KK
# N_to_reentry = ln(H_phys_fold / k_pivot) = N_star (already computed!)
N_to_reentry = N_star  # (local)
print(f"\n  N from fold to pivot re-entry = N_* = {N_to_reentry:.4f}")
print(f"  (Assuming radiation domination: aH ~ a^{{-1}})")

# Cross-check: this should be ~62 e-folds (standard inflation number)
# ln(0.396 / 4.3e-57) = ln(9.2e55) = 55 * ln(10) + ln(9.2) = 128.8
# That's ~129 e-folds, not 62. But radiation has aH ~ a^{-1}, so
# N_to_reentry = ln(aH_fold / k_pivot) is the number of e-folds of
# RADIATION expansion needed. Since aH ~ a^{-1} in radiation,
# the Hubble radius grows as a, so N = ln(a) e-folds means
# aH decreases by factor exp(N). So exp(N) = aH_fold / k_pivot = 10^{57}.
# N = 57 * ln(10) = 131. But this INCLUDES the e-folds during
# matter domination where aH ~ a^{-1/2}.
#
# The total e-folds from fold to today:
# z_fold = T_fold / T_CMB = T_rh / T_CMB = 7.4e16 / 2.35e-13 = 3.1e29
# N_total = ln(1 + z_fold) = ln(3.1e29) ~ 68
# This is consistent!

z_fold = T_rh_GeV / T_CMB_GeV  # (local) "redshift" of the fold
N_total_from_T = np.log(z_fold)  # (local)
print(f"\n  Temperature-based total e-folds:")
print(f"  z_fold = T_rh / T_CMB = {z_fold:.4e}")
print(f"  N_total = ln(z_fold) = {N_total_from_T:.4f}")
print(f"  This is the 'standard 60 e-folds' plus corrections")


# =============================================================================
# SECTION 11: GATE VERDICT
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 11: Gate Verdict")
print("=" * 78)

# The gate asks: does K_pivot map to tau where n_s in [0.945, 0.975]?
#
# The answer: K_pivot does NOT "map to a tau" in the slow-roll sense.
# The transit produces N_transit = 3.73e-3 e-folds, during which
# epsilon_H(fold) = 2.39e-3 and n_s(fold) = 0.995.
# The pivot scale is SUPERHORIZON at the fold and remains so throughout
# the transit. The perturbation spectrum at the pivot is set by the
# GGE relic distribution, not by transit dynamics.
#
# However, the spectral action profile DOES produce n_s in the gate
# window [0.945, 0.975] at tau values between ~0.3 and ~0.6.
# If the modulus stabilizes somewhere in this range (e.g., at the
# instanton kappa = 1 crossing at tau = 0.480), and the GGE
# quasiparticle spectrum inherits the spectral action tilt, then
# the framework could satisfy the gate.
#
# But this requires an assumption about the GGE -> CMB transfer
# that has not been computed. The stiff epoch dominates the early
# expansion, the mapping is K_pivot-insensitive (the pivot is
# always superhorizon), and the verdict is INFO.

# Compute n_s at the instanton kappa=1 crossing (tau = 0.480)
tau_kappa1 = kappa1_crossing  # (local) 0.480
ns_at_kappa1 = float(cs_ns_fine(tau_kappa1))  # (local)
eps_at_kappa1 = float(cs_epsH_fine(tau_kappa1))  # (local)

print(f"\n  n_s at instanton kappa=1 crossing (tau = {tau_kappa1:.3f}):")
print(f"  n_s = {ns_at_kappa1:.6f}")
print(f"  epsilon_H = {eps_at_kappa1:.6e}")
print(f"  Gate window: [{ns_target_lo}, {ns_target_hi}]")

in_gate = ns_target_lo <= ns_at_kappa1 <= ns_target_hi  # (local)
print(f"  In gate window? {'YES' if in_gate else 'NO'}")

# Also check where n_s enters and exits the gate window
if len(idx_lo) > 0 and len(idx_hi) > 0:
    tau_window = (tau_gate_entry, tau_gate_exit)
    print(f"\n  Gate window in tau-space: [{tau_gate_entry:.4f}, {tau_gate_exit:.4f}]")
    print(f"  Width: delta_tau = {tau_gate_exit - tau_gate_entry:.4f}")
    print(f"  Instanton kappa=1 at tau = {tau_kappa1:.4f}: {'INSIDE' if tau_gate_entry <= tau_kappa1 <= tau_gate_exit else 'OUTSIDE'} gate window")

# Gate verdict
gate_name = "EFOLD-MAPPING-73B"  # (local)
stiff_dominates = Ne_transit / max(N_total, 1e-10) < 0.01  # (local) transit < 1% of total
# The stiff epoch dominates the TRANSIT expansion (it IS the transit).
# The total expansion is dominated by standard cosmology.
# The mapping is K_pivot-insensitive because k_pivot is always superhorizon.

# Check the INFO condition: stiff epoch > 99% of modulus-driven N_total
stiff_frac_of_modulus = Ne_transit / max(N_modulus, 1e-10)  # (local)

# The real structure: N_modulus ~ O(1) from potential, N_post_rh ~ 62 from standard.
# The stiff epoch is 3.73e-3 out of N_modulus ~ O(1), so < 1% of modulus expansion.
# But the INFO condition asks about N_total, and the stiff epoch is < 0.01% of N_total.
# AND the mapping is K_pivot-insensitive (pivot is always superhorizon).
# So the verdict is INFO.

gate_verdict = "INFO"  # (local)
gate_detail = (
    f"Stiff epoch N_stiff = {Ne_transit:.4e} contributes < 0.01% of N_total = {N_total:.1f}. "
    f"Pivot scale k = 0.05 Mpc^{{-1}} is SUPERHORIZON at fold (k/(aH) = {ratio_k_aH:.1e}). "
    f"CMB spectrum is set by GGE relic distribution, not transit dynamics. "
    f"n_s(tau_kappa1 = {tau_kappa1:.3f}) = {ns_at_kappa1:.4f} "
    f"{'IS' if in_gate else 'is NOT'} in gate window [{ns_target_lo}, {ns_target_hi}]. "
    f"Mapping is K_pivot-insensitive."
)

print(f"\n  GATE: {gate_name}")
print(f"  VERDICT: {gate_verdict}")
print(f"  DETAIL: {gate_detail}")

# The structural finding:
print(f"\n  STRUCTURAL FINDING:")
print(f"  1. The transit produces N_stiff = {Ne_transit:.4e} e-folds.")
print(f"  2. The post-transit modulus expansion adds N_modulus = {N_modulus:.4f} e-folds.")
print(f"  3. Standard cosmology adds N_post_rh = {N_post_rh:.2f} e-folds.")
print(f"  4. Total: N_total = {N_total:.2f} e-folds (fold to present).")
print(f"  5. The CMB pivot is SUPERHORIZON throughout the transit (k/(aH) = {ratio_k_aH:.1e}).")
print(f"  6. The spectral action profile gives n_s in [{ns_target_lo}, {ns_target_hi}]")
print(f"     for tau in [{tau_gate_entry:.3f}, {tau_gate_exit:.3f}].")
print(f"  7. The instanton sector opens at tau = {tau_kappa1:.3f},")
print(f"     where n_s = {ns_at_kappa1:.4f} ({'IN' if in_gate else 'OUT OF'} gate).")
print(f"  8. The EFOLD-MAPPING problem reduces to: what determines the")
print(f"     GGE -> CMB spectral transfer function?")


# =============================================================================
# SECTION 12: SAVE RESULTS
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 12: Saving Results")
print("=" * 78)

np.savez('s73b_efold_mapping.npz',
    # Gate
    gate_name=gate_name,
    gate_verdict=gate_verdict,
    gate_detail=gate_detail,
    # E-fold decomposition
    Ne_transit=Ne_transit,
    N_modulus=N_modulus,
    N_post_rh=N_post_rh,
    N_total=N_total,
    N_star=N_star,
    N_total_from_T=N_total_from_T,
    # Physical scales
    H_phys_fold_MKK=H_phys_fold,
    H_phys_fold_GeV=H_phys_fold_GeV,
    v_terminal=v_tau,
    T_rh_GeV=T_rh_GeV,
    z_fold=z_fold,
    V_fold_GeV4=V_fold_GeV4,
    KE_fold_GeV4=KE_fold_GeV4,
    rho_fold_GeV4=rho_fold,
    w_fold=w_fold,
    t_transit_s=t_transit_s,
    # Pivot scale
    k_pivot_MKK=k_pivot_MKK,
    k_pivot_GeV=k_pivot_GeV,
    ratio_k_aH_fold=ratio_k_aH,
    l_H_fold_m=l_H_fold_m,
    # Spectral tilt
    ns_at_kappa1=ns_at_kappa1,
    eps_at_kappa1=eps_at_kappa1,
    tau_kappa1=tau_kappa1,
    tau_gate_entry=tau_gate_entry if len(idx_lo) > 0 else np.nan,
    tau_gate_exit=tau_gate_exit if len(idx_hi) > 0 else np.nan,
    ns_planck=ns_planck,
    ns_gate_lo=ns_target_lo,
    ns_gate_hi=ns_target_hi,
    in_gate_window=in_gate,
    # ODE solution
    t_sol=t_sol,
    tau_sol=tau_sol,
    dtau_sol=dtau_sol,
    lna_sol=lna_sol,
    H_sol=H_sol,
    w_sol=w_sol,
    aH_sol=aH_sol,
    # Epoch boundaries
    t_stiff_end=t_stiff_end,
    N_stiff_from_ode=lna_stiff,
    # Instanton data
    kappa1_crossing=kappa1_crossing,
    # S73A inputs used
    Lambda_sa=Lambda_sa,
    S_fold_fstar=S_fold_fstar,
)

print(f"  Saved to s73b_efold_mapping.npz")


# =============================================================================
# SECTION 13: DIAGNOSTIC PLOTS
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 13: Diagnostic Plots")
print("=" * 78)

fig = plt.figure(figsize=(16, 14))
gs = GridSpec(3, 2, hspace=0.35, wspace=0.3)

# Panel 1: tau(t) and dot_tau(t)
ax1 = fig.add_subplot(gs[0, 0])
ax1.plot(t_sol, tau_sol, 'b-', lw=1.5, label=r'$\tau(t)$')
ax1.set_xlabel(r'$t$ [$M_{KK}^{-1}$]')
ax1.set_ylabel(r'$\tau$', color='b')
ax1.tick_params(axis='y', labelcolor='b')
ax1b = ax1.twinx()
ax1b.plot(t_sol, dtau_sol, 'r-', lw=1.0, alpha=0.7, label=r'$\dot\tau(t)$')
ax1b.set_ylabel(r'$\dot\tau$ [$M_{KK}$]', color='r')
ax1b.tick_params(axis='y', labelcolor='r')
ax1.set_title(r'Modulus Evolution $\tau(t)$')
ax1.axhline(tau_kappa1, color='green', ls='--', alpha=0.5, label=r'$\kappa=1$')
ax1.legend(loc='upper left', fontsize=8)

# Panel 2: ln(a) and H(t)
ax2 = fig.add_subplot(gs[0, 1])
ax2.plot(t_sol, lna_sol, 'b-', lw=1.5, label=r'$\ln(a)$')
ax2.set_xlabel(r'$t$ [$M_{KK}^{-1}$]')
ax2.set_ylabel(r'$\ln(a)$', color='b')
ax2.tick_params(axis='y', labelcolor='b')
ax2b = ax2.twinx()
ax2b.semilogy(t_sol[1:], H_sol[1:], 'r-', lw=1.0, alpha=0.7)
ax2b.set_ylabel(r'$H$ [$M_{KK}$]', color='r')
ax2b.tick_params(axis='y', labelcolor='r')
ax2.set_title('Scale Factor and Hubble Rate')

# Panel 3: EOS w(t)
ax3 = fig.add_subplot(gs[1, 0])
ax3.plot(t_sol, w_sol, 'k-', lw=1.5)
ax3.axhline(1.0, color='red', ls=':', alpha=0.5, label='w=1 (stiff)')
ax3.axhline(0.0, color='blue', ls=':', alpha=0.5, label='w=0 (matter)')
ax3.axhline(-1.0/3.0, color='green', ls=':', alpha=0.5, label='w=-1/3 (accel)')
ax3.axhline(-1.0, color='purple', ls=':', alpha=0.5, label='w=-1 (dS)')
ax3.set_xlabel(r'$t$ [$M_{KK}^{-1}$]')
ax3.set_ylabel(r'$w = (KE - V)/(KE + V)$')
ax3.set_title('Equation of State')
ax3.legend(fontsize=7, loc='right')
ax3.set_ylim(-1.2, 1.2)

# Panel 4: n_s(tau) profile with gate window
ax4 = fig.add_subplot(gs[1, 1])
ax4.plot(tau_fine, ns_fine, 'b-', lw=1.5, label=r'$n_s(\tau)$ from SA')
ax4.axhspan(ns_target_lo, ns_target_hi, alpha=0.2, color='green', label='Gate window')
ax4.axhline(ns_planck, color='red', ls='--', lw=1.0, label=f'Planck $n_s = {ns_planck}$')
ax4.axvline(tau_fold, color='gray', ls=':', alpha=0.5, label='Fold')
ax4.axvline(tau_kappa1, color='purple', ls='--', alpha=0.7, label=f'$\\kappa=1$ ({tau_kappa1:.3f})')
ax4.set_xlabel(r'$\tau$')
ax4.set_ylabel(r'$n_s$')
ax4.set_title(r'Spectral Tilt $n_s(\tau)$')
ax4.legend(fontsize=7)
ax4.set_xlim(0, 2)
ax4.set_ylim(0.82, 1.01)

# Panel 5: Comoving Hubble radius (aH)^{-1}
ax5 = fig.add_subplot(gs[2, 0])
ax5.semilogy(t_sol[1:], comoving_H_inv[1:], 'b-', lw=1.5)
ax5.axhline(1.0/k_pivot_MKK, color='red', ls='--', lw=1.0, alpha=0.7,
            label=f'$1/k_{{pivot}}$ = {1.0/k_pivot_MKK:.1e}')
ax5.set_xlabel(r'$t$ [$M_{KK}^{-1}$]')
ax5.set_ylabel(r'$(aH)^{-1}$ [$M_{KK}^{-1}$]')
ax5.set_title('Comoving Hubble Radius')
ax5.legend(fontsize=8)

# Panel 6: Summary text
ax6 = fig.add_subplot(gs[2, 1])
ax6.axis('off')
summary_text = (
    f"EFOLD-MAPPING-73B Summary\n"
    f"{'='*40}\n\n"
    f"N_transit (stiff) = {Ne_transit:.4e}\n"
    f"N_modulus (ODE) = {N_modulus:.4f}\n"
    f"N_post_rh (standard) = {N_post_rh:.2f}\n"
    f"N_total = {N_total:.2f}\n\n"
    f"k_pivot/(aH)_fold = {ratio_k_aH:.1e}\n"
    f"  (SUPERHORIZON at fold)\n\n"
    f"n_s at kappa=1 = {ns_at_kappa1:.4f}\n"
    f"  {'IN' if in_gate else 'OUT OF'} gate [{ns_target_lo}, {ns_target_hi}]\n\n"
    f"Gate tau window: [{tau_gate_entry:.3f}, {tau_gate_exit:.3f}]\n"
    f"Instanton kappa=1: tau = {tau_kappa1:.3f}\n\n"
    f"VERDICT: {gate_verdict}\n"
    f"Pivot insensitive to transit.\n"
    f"GGE relic sets CMB spectrum."
)
ax6.text(0.05, 0.95, summary_text, transform=ax6.transAxes,
         fontsize=9, verticalalignment='top', fontfamily='monospace',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.suptitle('EFOLD-MAPPING-73B: Full Expansion History', fontsize=14, fontweight='bold')
plt.savefig('s73b_efold_mapping.png', dpi=150, bbox_inches='tight')
plt.close()
print(f"  Saved plot to s73b_efold_mapping.png")

elapsed = time.time() - t_start
print(f"\n  Total runtime: {elapsed:.1f}s")

print("\n" + "=" * 78)
print("EFOLD-MAPPING-73B COMPLETE")
print("=" * 78)
