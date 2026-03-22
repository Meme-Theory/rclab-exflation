#!/usr/bin/env python3
"""
s46_quasistatic_ns.py — Quasi-Static Phase at q-Theory Equilibrium (QUASISTATIC-NS-46)
=======================================================================================

GATE: QUASISTATIC-NS-46
  PASS: N_e > 10 during dwell at tau*
  FAIL: N_e < 0.1

Physics:
--------
S46 W1-1 found that the q-theory Gibbs-Duhem crossing is marginal:
  - FLATBAND gaps: crossing at tau* = 0.210 (PASS)
  - Self-consistent gaps: no crossing (Delta_B3 too small)
  - Crossing appears when V_B3B3 > 0.015 (E_cond factor > 1.26)

S45 QNM-NS-45 found:
  - eps_V = 0.016 (the spectral action potential IS flat)
  - eps_H = 3.0 (the modulus is in ballistic transit, stiff-matter dominated)
  - velocity_reduction_needed = 0.00121 (829x reduction to reach slow roll)

THIS COMPUTATION: If the q-theory creates a local potential well where rho_gs = 0,
the modulus decelerates and oscillates around tau*. During this quasi-static phase:
  1. The kinetic energy converts to potential energy (deceleration by the q-theory force)
  2. Hubble friction damps the oscillation
  3. eps_H drops from 3 toward zero during the dwell
  4. If the dwell is long enough, N_e > 10 e-folds of inflation occur

The equation of motion near the crossing tau*:
  M * tau_ddot + 3*H*M*tau_dot + c_2*(tau - tau*) = 0

where c_2 = d^2(V_q)/dtau^2 at tau* is the curvature of the q-theory potential.
This is a DAMPED HARMONIC OSCILLATOR.

The critical question: does c_2 generate a restoring force strong enough to
capture the ballistic modulus (arriving at v ~ 34600 M_KK)?

Two scenarios are analyzed:
  A. FLATBAND crossing (tau* = 0.210): c_2 from the actual FLATBAND trace-log
  B. Hypothetical crossing AT the fold (tau* = 0.190): optimistic V_B3B3

For each, we solve the full nonlinear coupled Friedmann-modulus system with the
q-theory potential added.

Author: Hawking-Theorist (Session 46 W2-3)

References:
  - Klinkhamer & Volovik, PRD 77 085015 (2008) [q-theory]
  - Hawking, "Particle Creation by Black Holes" (Paper 05) [semiclassical methods]
  - S45 QNM-NS-45 (eps_V, eps_H, H_fold)
  - S46 W1-1 (q-theory self-consistent crossing)
"""

import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import CubicSpline
from scipy.optimize import brentq
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from canonical_constants import (
    M_KK_gravity as M_KK, M_Pl_reduced, M_Pl_unreduced,
    tau_fold, a0_fold, E_cond, Delta_0_GL, Delta_B3,
    M_ATDHFB, H_fold as H_fold_canonical, v_terminal,
    S_fold, dS_fold, d2S_fold, Z_fold,
    PI, a_GL, b_GL,
)

print("=" * 78)
print("QUASISTATIC-NS-46: Quasi-Static Phase at q-Theory Equilibrium")
print("=" * 78)

# ============================================================================
# STEP 0: Load upstream data
# ============================================================================
print("\n--- STEP 0: Load Upstream Data ---")

# Load S45 QNM background trajectory parameters
d_qnm = np.load('tier0-computation/s45_qnm_ns.npz', allow_pickle=True)
eps_V_fold = float(d_qnm['eps_V_fold'])
eta_V_fold = float(d_qnm['eta_V_fold'])
eps_H_fold = float(d_qnm['epsilon_H_fold'])
H_fold_qnm = float(d_qnm['H_fold'])  # = 44.6 M_KK (from Friedmann with FC)
tau_dot_fold = float(d_qnm['tau_dot_fold'])  # = 34603 M_KK
M_eff = float(d_qnm['M_ATDHFB'])
FC_qnm = float(d_qnm['FC'])

# Load q-theory crossing data from W1-1
d_qt = np.load('tier0-computation/s46_qtheory_selfconsistent.npz', allow_pickle=True)
tau_star_fb = float(d_qt['tau_star_flatband_s46'])  # = 0.2101
V_mat_raw = d_qt['V_mat_raw']
V_mat_const = d_qt['V_mat_constrained']
alpha_star = float(d_qt['alpha_star'])  # = 0.4347

# Load the full spectral action S(tau) for the gravitational potential
d_s36 = np.load('tier0-computation/s36_sfull_tau_stabilization.npz', allow_pickle=True)
tau_s36 = d_s36['tau_combined']
S_full_s36 = d_s36['S_full']
cs_S = CubicSpline(tau_s36, S_full_s36)
cs_dS = cs_S.derivative(1)
cs_d2S = cs_S.derivative(2)

# Load the FLATBAND trace-log for the q-theory potential
tau_scan_qt = d_qt['tau_scan']
TL_fb = d_qt['TL_flatband']
cs_TL_fb = CubicSpline(tau_scan_qt, TL_fb)

# Also load the FLATBAND rho_raw data
tau_dense_fb = d_qt['tau_dense_fb']
rho_raw_fb = d_qt['rho_raw_fb']

print(f"eps_V_fold = {eps_V_fold:.6f}")
print(f"eta_V_fold = {eta_V_fold:.6f}")
print(f"eps_H_fold = {eps_H_fold:.6f}")
print(f"H_fold (QNM) = {H_fold_qnm:.4f} M_KK")
print(f"tau_dot_fold = {tau_dot_fold:.4f} M_KK")
print(f"FC = {FC_qnm:.6e}")
print(f"tau*_FLATBAND = {tau_star_fb:.6f}")
print(f"M_ATDHFB = {M_eff:.6f}")

# ============================================================================
# STEP 1: Characterize the q-theory potential near the crossing
# ============================================================================
print("\n" + "=" * 78)
print("STEP 1: Q-Theory Potential Near the Crossing")
print("=" * 78)

# The q-theory Gibbs-Duhem potential is:
#   V_q(tau) = rho_gs(tau) = epsilon(tau) - tau * epsilon'(tau) - epsilon_0
# where epsilon(tau) = TL(tau) is the BCS trace-log.
#
# Near the crossing tau*, rho_gs ~ c_linear * (tau - tau*) + (1/2)*c_2*(tau-tau*)^2
# The LINEAR term is crucial: rho_gs crosses zero, so there IS a linear restoring force
# (the Gibbs-Duhem pressure restores the modulus toward tau* where rho_gs = 0).

# Compute the Gibbs-Duhem function from the FLATBAND trace-log
cs_rho = CubicSpline(tau_dense_fb, rho_raw_fb)

# At the crossing:
drho_dtau_at_star = float(cs_rho(tau_star_fb, 1))
d2rho_dtau2_at_star = float(cs_rho(tau_star_fb, 2))
rho_at_star = float(cs_rho(tau_star_fb))

print(f"\nGibbs-Duhem rho_raw at tau* = {tau_star_fb:.4f}:")
print(f"  rho(tau*) = {rho_at_star:.6f} (should be ~0)")
print(f"  drho/dtau = {drho_dtau_at_star:.6f} (LINEAR restoring force)")
print(f"  d2rho/dtau2 = {d2rho_dtau2_at_star:.6f}")

# The effective potential for the modulus near tau* comes from the q-theory requirement:
# The vacuum must adjust to make rho_gs = 0. This creates a force:
#   F_q = -d(V_q)/dtau = -drho_gs/dtau
# Near tau*, V_q(tau) ~ (1/2) * |drho/dtau| * (tau - tau*)^2 if rho_gs ~ linear crossing
# But actually, rho_gs IS the energy density, and its gradient IS the force.

# The key distinction: in q-theory (Klinkhamer-Volovik), the Gibbs-Duhem condition
# rho_gs = 0 is not imposed as a constraint but arises thermodynamically.
# The "potential" that drives the modulus toward tau* is:
#   V_q(tau) = integral of F_q dtau = (1/2) * (-drho/dtau) * (tau - tau*)
# For a linear crossing, drho/dtau = const, so:
#   V_q(tau) ~ (1/2) * K * (tau - tau*)^2
# where K = -drho/dtau|_{tau*} is the spring constant.

K_spring = -drho_dtau_at_star  # Spring constant (restoring force per unit displacement)
# Note: drho/dtau < 0 at the crossing (rho decreases through zero), so K > 0.

print(f"\n  Spring constant K = -drho/dtau = {K_spring:.6f} M_KK^4")

# The oscillation frequency:
omega_osc = np.sqrt(abs(K_spring) / M_eff)
print(f"  omega_osc = sqrt(K/M) = {omega_osc:.6f} M_KK")

# Hubble damping rate:
Gamma_H = 3 * H_fold_qnm / 2
print(f"  Gamma_H = (3/2)*H = {Gamma_H:.6f} M_KK")

# Quality factor:
Q_factor = omega_osc / Gamma_H if Gamma_H > 0 else float('inf')
print(f"  Q = omega/Gamma = {Q_factor:.6f}")

# Is the oscillator underdamped or overdamped?
if omega_osc > Gamma_H:
    print(f"  STATUS: UNDERDAMPED (oscillatory). Damped frequency = {np.sqrt(omega_osc**2 - Gamma_H**2):.4f}")
else:
    print(f"  STATUS: OVERDAMPED. Relaxation time = {1/Gamma_H:.6e}")

# ============================================================================
# STEP 2: Can the q-theory potential capture the ballistic modulus?
# ============================================================================
print("\n" + "=" * 78)
print("STEP 2: Capture Condition — Can the Potential Stop the Modulus?")
print("=" * 78)

# The modulus arrives at tau* with velocity v = tau_dot_fold = 34603 M_KK.
# Kinetic energy: KE = (1/2) * M * v^2
KE_ballistic = 0.5 * M_eff * tau_dot_fold**2
print(f"  KE_ballistic = (1/2)*M*v^2 = {KE_ballistic:.4f} M_KK^4")

# The q-theory potential well depth is ~ K * delta_tau^2 / 2
# where delta_tau is the range over which the potential acts.
# From the FLATBAND data, the potential is effective over a range ~0.05-0.1 in tau.
# Maximum displacement before the potential changes character:
delta_tau_range = 0.05  # conservative estimate
PE_max = 0.5 * K_spring * delta_tau_range**2
print(f"  PE_max at delta_tau={delta_tau_range} = {PE_max:.6f} M_KK^4")
print(f"  KE/PE_max = {KE_ballistic/PE_max:.2f}")

# The ratio KE/PE determines whether the modulus can be captured.
# If KE >> PE, the modulus sails through the potential well and is not captured.
# This is the analog of a particle scattering off a shallow potential in QM.

# For capture WITHOUT Hubble friction: need KE < PE_max -> delta_tau < sqrt(2*KE/K)
delta_tau_needed = np.sqrt(2 * KE_ballistic / K_spring)
print(f"\n  For capture: delta_tau needed = sqrt(2*KE/K) = {delta_tau_needed:.4f}")
print(f"  This is {delta_tau_needed/tau_fold:.2f}x tau_fold")
print(f"  Available range: ~0.05-0.10 in tau")
print(f"  VERDICT: {'CAPTURED' if delta_tau_needed < 0.15 else 'NOT CAPTURED'}")

# Even with Hubble friction, the modulus traverses the potential well in time:
t_cross = delta_tau_range / tau_dot_fold if tau_dot_fold > 0 else float('inf')
print(f"\n  Crossing time t_cross = delta_tau/v = {t_cross:.6e} M_KK^{{-1}}")
print(f"  Hubble time t_H = 1/H = {1/H_fold_qnm:.6e} M_KK^{{-1}}")
print(f"  t_cross/t_H = {t_cross * H_fold_qnm:.6e}")

# If t_cross << t_H, Hubble friction has no time to act.

# ============================================================================
# STEP 3: Full Nonlinear Simulation (Scenario A: FLATBAND tau* = 0.210)
# ============================================================================
print("\n" + "=" * 78)
print("STEP 3: Full Nonlinear Simulation — Scenario A (FLATBAND)")
print("=" * 78)

# The coupled system WITH q-theory potential:
#   M * tau_ddot = -V_SA'(tau) - V_q'(tau) - 3*H*M*tau_dot
# where:
#   V_SA(tau) = S_full(tau) (spectral action)
#   V_q(tau) = -integral of rho_gs(tau) dtau  (q-theory restoring potential)
#   H^2 = FC * [KE + V_SA + V_q]

# Actually, in q-theory, the vacuum energy IS rho_gs and the Friedmann equation is:
#   H^2 = FC * [(1/2)*M*tau_dot^2 + V_SA(tau) + V_q(tau)]
# The q-theory adds V_q such that the total vacuum energy vanishes at tau*.

# The simplest model: V_q(tau) provides a harmonic restoring force toward tau*.
# V_q(tau) = (1/2) * K * (tau - tau*)^2
# This modifies the equation of motion:
#   M * tau_ddot + 3*H*M*tau_dot + dV_SA/dtau + K*(tau - tau*) = 0

# Solve the full system numerically:
def odes_with_qtrap(t, y, tau_star, K_eff, include_spectral=True):
    """Coupled Friedmann-KG with q-theory harmonic trap."""
    tau_val, tau_dot_val = y
    tau_c = np.clip(tau_val, tau_s36[0] + 0.001, tau_s36[-1] - 0.001)

    if include_spectral:
        V_sa = float(cs_S(tau_c))
        dV_sa = float(cs_dS(tau_c))
    else:
        V_sa = S_fold
        dV_sa = 0.0

    V_q = 0.5 * K_eff * (tau_val - tau_star)**2
    dV_q = K_eff * (tau_val - tau_star)

    rho = 0.5 * M_eff * tau_dot_val**2 + V_sa + V_q
    H = np.sqrt(FC_qnm * max(rho, 0.0))

    tau_ddot = -(dV_sa + dV_q) / M_eff - 3.0 * H * tau_dot_val
    return [tau_dot_val, tau_ddot]

# We also need to track N_e = integral H dt
# We'll compute it post-hoc from H(t).

# Scenario A: FLATBAND crossing at tau* = 0.210
tau_star_A = tau_star_fb
K_A = K_spring  # from the FLATBAND Gibbs-Duhem derivative

# Initial conditions: modulus starts at tau=0.15 approaching the fold at ballistic velocity
tau_init = 0.15
v_init = tau_dot_fold  # = 34603

# Also need the spectral action potential to be self-consistent
# The spectral action V_SA is already loaded as cs_S

# Solve the system WITHOUT q-theory trap (baseline)
def event_exit_A(t, y):
    return y[0] - 0.30  # stop when tau > 0.30
event_exit_A.terminal = True
event_exit_A.direction = 1

def event_exit_low(t, y):
    return y[0] - 0.05  # stop if tau drops below 0.05
event_exit_low.terminal = True
event_exit_low.direction = -1

t_span = (0, 0.01)  # generous time range
N_out = 10000

# Baseline: no q-theory trap
sol_base = solve_ivp(
    lambda t, y: odes_with_qtrap(t, y, tau_star_A, 0.0, True),
    t_span, [tau_init, v_init],
    method='RK45', dense_output=True,
    events=[event_exit_A, event_exit_low],
    rtol=1e-12, atol=1e-15,
    max_step=1e-6
)
t_base = sol_base.t
tau_base = sol_base.y[0]
tdot_base = sol_base.y[1]

# Compute H, eps_H, N_e for baseline
H_base = np.zeros(len(t_base))
eps_H_base = np.zeros(len(t_base))
for i in range(len(t_base)):
    tc = np.clip(tau_base[i], tau_s36[0]+0.001, tau_s36[-1]-0.001)
    V_sa = float(cs_S(tc))
    rho = 0.5 * M_eff * tdot_base[i]**2 + V_sa
    H_base[i] = np.sqrt(FC_qnm * max(rho, 0.0))
    eps_H_base[i] = 1.5 * M_eff * tdot_base[i]**2 / max(rho, 1e-30)

Ne_base = np.trapezoid(H_base, t_base)

print(f"  BASELINE (no q-theory):")
print(f"    Transit time = {t_base[-1]:.6e} M_KK^{{-1}}")
print(f"    tau range = [{tau_base[0]:.4f}, {tau_base[-1]:.4f}]")
print(f"    N_e = {Ne_base:.6f}")
print(f"    eps_H at fold = {eps_H_base[np.argmin(np.abs(tau_base-0.19))]:.4f}")

# Now with q-theory trap: scan over K values
print("\n  SCAN over K (q-theory spring constant):")

K_values = [K_spring * f for f in [0.01, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 50.0, 100.0,
                                     500.0, 1000.0, 5000.0, 1e4, 5e4, 1e5, 5e5, 1e6, 1e7, 1e8]]
results_A = []

for K_val in K_values:
    try:
        sol = solve_ivp(
            lambda t, y, K=K_val: odes_with_qtrap(t, y, tau_star_A, K, True),
            t_span, [tau_init, v_init],
            method='RK45', dense_output=True,
            events=[event_exit_A, event_exit_low],
            rtol=1e-10, atol=1e-13,
            max_step=1e-5
        )
        t_sol = sol.t
        tau_sol = sol.y[0]
        tdot_sol = sol.y[1]

        # Compute H and N_e
        H_sol = np.zeros(len(t_sol))
        eps_H_sol = np.zeros(len(t_sol))
        for i in range(len(t_sol)):
            tc = np.clip(tau_sol[i], tau_s36[0]+0.001, tau_s36[-1]-0.001)
            V_sa = float(cs_S(tc))
            V_q = 0.5 * K_val * (tau_sol[i] - tau_star_A)**2
            rho = 0.5 * M_eff * tdot_sol[i]**2 + V_sa + V_q
            H_sol[i] = np.sqrt(FC_qnm * max(rho, 0.0))
            eps_H_sol[i] = 1.5 * M_eff * tdot_sol[i]**2 / max(rho, 1e-30)

        Ne_sol = np.trapezoid(H_sol, t_sol)

        # Check if modulus was captured (turns around)
        min_v_idx = np.argmin(np.abs(tdot_sol))
        captured = np.any(tdot_sol < 0)  # velocity reversal
        min_eps_H = np.min(eps_H_sol)

        # Check if there's a quasi-static phase (eps_H < 1 for some duration)
        mask_quasi = eps_H_sol < 1.0
        t_quasi = np.sum(np.diff(t_sol)[mask_quasi[:-1]]) if np.any(mask_quasi) else 0.0
        Ne_quasi = np.trapezoid(H_sol[mask_quasi], t_sol[mask_quasi]) if np.any(mask_quasi) else 0.0

        results_A.append({
            'K': K_val, 'Ne': Ne_sol, 'Ne_quasi': Ne_quasi,
            'captured': captured, 'min_eps_H': min_eps_H,
            't_total': t_sol[-1], 't_quasi': t_quasi,
            'tau_final': tau_sol[-1], 'v_final': tdot_sol[-1],
            'min_v': np.min(tdot_sol)
        })
    except Exception as e:
        results_A.append({
            'K': K_val, 'Ne': 0, 'Ne_quasi': 0,
            'captured': False, 'min_eps_H': 3.0,
            't_total': 0, 't_quasi': 0,
            'tau_final': 0, 'v_final': 0,
            'min_v': v_init,
            'error': str(e)
        })

print(f"\n  {'K':>12s}  {'N_e':>8s}  {'N_e(quasi)':>10s}  {'captured':>8s}  "
      f"{'min_eps_H':>10s}  {'t_quasi':>10s}  {'min_v':>10s}")
for r in results_A:
    print(f"  {r['K']:12.2e}  {r['Ne']:8.4f}  {r['Ne_quasi']:10.6f}  "
          f"{'YES' if r['captured'] else 'no':>8s}  {r['min_eps_H']:10.4f}  "
          f"{r['t_quasi']:10.6e}  {r['min_v']:10.2f}")

# ============================================================================
# STEP 4: Critical K for Capture (Energy Balance)
# ============================================================================
print("\n" + "=" * 78)
print("STEP 4: Critical K for Capture (Energy Balance)")
print("=" * 78)

# For the modulus to be captured (turn around), the potential energy at maximum
# displacement must equal the kinetic energy at tau*:
#   (1/2)*K*(tau_max - tau*)^2 = (1/2)*M*v^2
# where tau_max is determined by the spectral action profile.

# Maximum reasonable displacement: from tau* = 0.210 to the edge of the
# eigenvalue data (~0.40), so delta_tau_max ~ 0.19.
delta_tau_max = tau_s36[-1] - tau_star_A - 0.01  # leave 0.01 buffer

K_capture = M_eff * v_init**2 / delta_tau_max**2
print(f"  Capture condition: K > M*v^2/delta_tau_max^2")
print(f"  delta_tau_max = {delta_tau_max:.4f}")
print(f"  K_capture = {K_capture:.4e} M_KK^4")
print(f"  K_FLATBAND = {K_spring:.4e} M_KK^4")
print(f"  K_capture / K_FLATBAND = {K_capture / K_spring:.2f}")

# The FLATBAND K is derived from the Gibbs-Duhem crossing slope.
# K_capture >> K_FLATBAND means the q-theory potential is FAR too weak.

# With Hubble friction: the friction force is 3*H*M*v, which does work W_fric per unit time.
# Over a Hubble time 1/H, the friction dissipates:
#   delta_KE_fric = 3*H*M*v^2 * t_cross ~ 3*H*M*v * delta_tau
W_fric = 3 * H_fold_qnm * M_eff * v_init * delta_tau_max
print(f"\n  Friction work over delta_tau_max: W_fric = {W_fric:.4e} M_KK^4")
print(f"  KE_ballistic = {KE_ballistic:.4e} M_KK^4")
print(f"  W_fric / KE = {W_fric / KE_ballistic:.6f}")

# Friction is also negligible because the crossing time is much shorter than the Hubble time.

# ============================================================================
# STEP 5: Analytical Solution — Damped Oscillator
# ============================================================================
print("\n" + "=" * 78)
print("STEP 5: Analytical Damped Harmonic Oscillator Solution")
print("=" * 78)

# The linearized equation of motion:
#   M * tau_ddot + 3*H*M * tau_dot + K*(tau - tau*) = 0
# In terms of displacement x = tau - tau*, with initial conditions
# x(0) = tau_init - tau* = -0.060, x_dot(0) = v_init = 34603:
#
#   x_ddot + 2*gamma*x_dot + omega_0^2 * x = 0
# where gamma = 3H/2, omega_0 = sqrt(K/M)

# For FLATBAND K:
omega_0 = np.sqrt(K_spring / M_eff)
gamma = 3 * H_fold_qnm / 2
x_0 = tau_init - tau_star_A  # = -0.060
xdot_0 = v_init  # = 34603

print(f"  omega_0 = {omega_0:.6f} M_KK")
print(f"  gamma = {gamma:.6f} M_KK")
print(f"  omega_0 / gamma = {omega_0/gamma:.6f}")
print(f"  x(0) = {x_0:.6f}, x_dot(0) = {xdot_0:.4f}")

if omega_0 > gamma:
    omega_d = np.sqrt(omega_0**2 - gamma**2)
    print(f"  UNDERDAMPED: omega_d = {omega_d:.6f}")
    # Solution: x(t) = e^{-gamma*t} * [A*cos(omega_d*t) + B*sin(omega_d*t)]
    A = x_0
    B = (xdot_0 + gamma * x_0) / omega_d
    print(f"  Amplitude: A = {A:.6f}, B = {B:.4f}")
    # Envelope amplitude:
    R = np.sqrt(A**2 + B**2)
    print(f"  Envelope amplitude R = {R:.4f}")
    # Maximum displacement:
    x_max = R  # envelope at t=0
    print(f"  Maximum displacement |x_max| = {x_max:.4f}")
    print(f"  This is {x_max:.2e} >> delta_tau_range ~ 0.05")
    print(f"  The oscillator AMPLITUDE exceeds the range of validity of the harmonic approx.")

    # Dwell time = 1/gamma (time for 1/e amplitude decay)
    t_dwell = 1 / gamma
    print(f"\n  Dwell time t_dwell = 1/gamma = {t_dwell:.6e} M_KK^{{-1}}")
    print(f"  N_e during dwell = H * t_dwell = {H_fold_qnm * t_dwell:.6f}")
    print(f"  Oscillation period = 2*pi/omega_d = {2*PI/omega_d:.6e}")
    print(f"  Number of oscillations in dwell time = {omega_d / (2*PI*gamma):.4f}")
else:
    print(f"  OVERDAMPED")
    kappa = np.sqrt(gamma**2 - omega_0**2)
    t_dwell = 1 / (gamma - kappa)
    print(f"  Slow decay rate = {gamma - kappa:.6e}")
    print(f"  Dwell time = {t_dwell:.6e} M_KK^{{-1}}")
    print(f"  N_e during dwell = {H_fold_qnm * t_dwell:.6f}")

# But the REAL issue is: the amplitude B ~ v/omega >> 1, so the modulus sails
# right through the potential well. The harmonic approximation breaks down.

# ============================================================================
# STEP 6: What K is NEEDED for N_e > 10?
# ============================================================================
print("\n" + "=" * 78)
print("STEP 6: Required K for N_e > 10")
print("=" * 78)

# For N_e > 10 during a quasi-static phase:
#   N_e = H * t_dwell > 10
#   t_dwell = 1/gamma = 2/(3H) (this is fixed by Hubble)
#   So N_e = H * 2/(3H) = 2/3 per damping time (this is a general result!)

# WAIT. This needs more care. During the quasi-static phase, if the modulus
# is trapped and oscillating, the POTENTIAL energy V_q dominates over KE,
# and V_q ~ K*(x_amplitude)^2 acts like a cosmological constant.
# H^2 = FC * V_q, and if V_q is large enough, H can be large.

# For the slow-roll regime (eps_H << 1), we need:
#   KE << V_SA + V_q
# The spectral action V_SA ~ 250360 at fold. So the modulus must lose essentially
# ALL of its kinetic energy KE = (1/2)*M*v^2 = (1/2)*1.695*34603^2 ~ 1.015e9 M_KK^4.

print(f"  KE_ballistic = {KE_ballistic:.4e} M_KK^4")
print(f"  V_SA(fold) = {S_fold:.2f} M_KK^4")
print(f"  KE/V_SA = {KE_ballistic/S_fold:.2f}")

# The kinetic energy is 4000x the potential energy. Even if the q-theory trap
# captured the modulus, V_q would need to be comparable to KE to actually drive
# inflation (H^2 ~ FC * V_q where V_q >> V_SA).

# For N_e = H*t_dwell > 10 with the Hubble-friction dwell time:
# t_dwell = 1/gamma = 2/(3H)
# N_e = H * 2/(3H) = 2/3 per dwell time. ALWAYS < 1!
#
# This is a FUNDAMENTAL result: Hubble friction alone gives N_e ~ O(1) at most.
# To get N_e >> 1, the modulus must be in SLOW ROLL (not oscillating).

print(f"\n  FUNDAMENTAL LIMIT: N_e per Hubble damping time = 2/3")
print(f"  For N_e > 10: need the modulus to SLOW ROLL, not oscillate")
print(f"  Slow roll requires eps_H < 1, i.e., KE < V_total")
print(f"  Currently: KE/V_SA ~ {KE_ballistic/S_fold:.0f}x (completely kinetic-dominated)")

# For slow roll: v must be reduced to v_slow where (1/2)*M*v_slow^2 < V_SA
v_slow_limit = np.sqrt(2 * S_fold / M_eff)
print(f"\n  For eps_H < 1: v < {v_slow_limit:.4f} M_KK")
print(f"  Current v = {v_init:.4f} M_KK")
print(f"  Velocity reduction needed = {v_init / v_slow_limit:.2f}x")

# This is the 829x velocity reduction from S45 QNM-NS-45.
# The q-theory potential would need to absorb this kinetic energy.
# K needed to slow the modulus over a displacement delta_tau:
# (1/2)*M*v^2 = (1/2)*K*delta_tau^2  =>  K = M*v^2/delta_tau^2
for dt in [0.01, 0.02, 0.05, 0.10]:
    K_needed = M_eff * v_init**2 / dt**2
    print(f"  K to capture over delta_tau={dt}: K = {K_needed:.4e} M_KK^4  ({K_needed/K_spring:.2e}x K_FLATBAND)")

# ============================================================================
# STEP 7: Scenario B — Hypothetical Strong Trap (K = K_capture)
# ============================================================================
print("\n" + "=" * 78)
print("STEP 7: Scenario B — Hypothetical K = K_capture")
print("=" * 78)

# Even if we ARTIFICIALLY set K to the capture value, what happens?
# Use K such that the modulus turns around within delta_tau = 0.05.

K_strong = M_eff * v_init**2 / (0.05)**2
tau_star_B = tau_fold  # optimistically at the fold

print(f"  K_strong = {K_strong:.4e} M_KK^4")
print(f"  tau*_B = {tau_star_B} (at fold)")

# Solve the system
try:
    sol_B = solve_ivp(
        lambda t, y: odes_with_qtrap(t, y, tau_star_B, K_strong, True),
        (0, 0.1), [tau_init, v_init],
        method='RK45', dense_output=True,
        events=[event_exit_A],
        rtol=1e-10, atol=1e-13,
        max_step=1e-6
    )
    t_B = sol_B.t
    tau_B = sol_B.y[0]
    tdot_B = sol_B.y[1]

    # Compute H, eps_H, N_e
    H_B = np.zeros(len(t_B))
    eps_H_B = np.zeros(len(t_B))
    for i in range(len(t_B)):
        tc = np.clip(tau_B[i], tau_s36[0]+0.001, tau_s36[-1]-0.001)
        V_sa = float(cs_S(tc))
        V_q = 0.5 * K_strong * (tau_B[i] - tau_star_B)**2
        rho_i = 0.5 * M_eff * tdot_B[i]**2 + V_sa + V_q
        H_B[i] = np.sqrt(FC_qnm * max(rho_i, 0.0))
        eps_H_B[i] = 1.5 * M_eff * tdot_B[i]**2 / max(rho_i, 1e-30)

    Ne_B = np.trapezoid(H_B, t_B)

    # Quasi-static phase
    mask_quasi_B = eps_H_B < 1.0
    Ne_quasi_B = np.trapezoid(H_B[mask_quasi_B], t_B[mask_quasi_B]) if np.any(mask_quasi_B) else 0.0
    t_quasi_B = np.sum(np.diff(t_B)[mask_quasi_B[:-1]]) if np.any(mask_quasi_B) else 0.0

    # Check for velocity reversal
    captured_B = np.any(tdot_B < 0)
    min_v_B = np.min(tdot_B)
    min_eps_B = np.min(eps_H_B)

    print(f"  Captured: {captured_B}")
    print(f"  min(v) = {min_v_B:.4f}")
    print(f"  min(eps_H) = {min_eps_B:.6f}")
    print(f"  N_e total = {Ne_B:.6f}")
    print(f"  N_e (quasi-static, eps_H<1) = {Ne_quasi_B:.6f}")
    print(f"  t_quasi = {t_quasi_B:.6e}")

    # During the oscillation, the modulus bounces. The key question is
    # whether eps_H ever drops below 1, and for how long.
    # The energy is: KE = (1/2)*M*v^2 ~ K*x^2 (oscillating)
    # At turning points: v=0, eps_H=0. Between turning points: eps_H ~ 3.
    # The AVERAGE eps_H over one oscillation:
    # <eps_H> = <3*KE/rho> = <3*KE/(KE+V_SA+V_q)>
    # If V_q >> V_SA: <eps_H> ~ <3*KE/(KE+V_q)> = 3/2 (virial theorem for harmonic)
    # So even with capture, the AVERAGE eps_H = 3/2 >> 1. No slow roll!

    print(f"\n  VIRIAL THEOREM RESULT:")
    print(f"  For harmonic oscillator: <KE> = <PE_q>, so <eps_H> = 3/2")
    print(f"  Oscillating modulus NEVER enters slow roll on average")
    print(f"  Slow roll requires eps_H << 1, which needs V_SA >> KE (no oscillation)")

except Exception as e:
    print(f"  Simulation error: {e}")
    Ne_B = 0
    Ne_quasi_B = 0

# ============================================================================
# STEP 8: Scenario C — Pure q-Theory (no spectral action gradient)
# ============================================================================
print("\n" + "=" * 78)
print("STEP 8: Scenario C — What K Gives N_e = 10?")
print("=" * 78)

# The only way to get N_e >> 1 is if the modulus energy is dominated by V_q
# (acting as a cosmological constant) while the modulus is nearly at rest.
# This requires:
# 1. Capture: K large enough to stop the modulus
# 2. Slow roll: After capture, the modulus slowly rolls to tau* under friction
# 3. During slow roll: V_q(x) ~ V_q(x_0) ~ constant >> KE

# After capture at turning point x = x_max with v=0:
# The slow-roll phase begins. The modulus rolls from x_max toward x=0.
# In slow roll: 3*H*M*x_dot = -K*x  =>  x_dot = -K*x / (3*H*M)
# H^2 = FC * (V_SA + V_q)  ~ FC * V_q (if V_q >> V_SA)
# V_q = (1/2)*K*x^2

# x_dot = -K*x / (3*sqrt(FC*K/2)*|x|*M) = -sqrt(K/(18*FC*M^2)) * sign(x)
# This gives x(t) = x_max * exp(-t/t_roll) where
# Actually, the slow-roll solution is more subtle.

# For the harmonic potential V = (1/2)*K*x^2 with Hubble friction:
# In the attractor regime (after damping): the potential-dominated Hubble is
#   H = sqrt(FC * V) = sqrt(FC*K/2) * |x|
# Slow roll: 3*H*v = -K*x
#   v = -K*x/(3*H) = -(K*x)/(3*sqrt(FC*K/2)*|x|) = -sqrt(K/(18*FC))/3 = const!
# This is a CONSTANT velocity slow roll. The slow-roll parameters are:
eps_V_harmonic = 1 / (FC_qnm * M_eff)  # eps_V = M_Pl^2/(2*M) * (V'/V)^2 (but in our units...)
# Actually, eps_V for V = (1/2)*K*x^2: V'/V = 2/x, so eps_V = (1/2)*(V'/V)^2 / (FC*M) = 2/(FC*M*x^2)

# For the S45 definition: eps_V = (1/(2*FC*M_eff)) * (dV/dtau / V)^2
# With V = (1/2)*K*x^2: dV/dtau = K*x, V = (1/2)*K*x^2
# eps_V = (1/(2*FC*M_eff)) * (K*x / ((1/2)*K*x^2))^2 = (1/(2*FC*M_eff)) * 4/x^2 = 2/(FC*M_eff*x^2)

# For slow roll (eps_V < 1): x^2 > 2/(FC*M_eff)
x_min_slowroll = np.sqrt(2 / (FC_qnm * M_eff))
print(f"  eps_V < 1 requires |x| > {x_min_slowroll:.4f}")
print(f"  (This is {x_min_slowroll:.4f} / tau_fold = {x_min_slowroll/tau_fold:.2f})")

# For the harmonic potential V=(1/2)*K*x^2, N_e between x_1 and x_2:
# N_e = integral H dt = integral H/(x_dot) dx
# In slow roll: H = sqrt(FC*K/2)*|x|, x_dot = -K*x/(3*H*M) = -sqrt(K/(18*FC))/3
# Actually x_dot = -K*x / (3*H*M_eff) and H = sqrt(FC*(K/2)*x^2)
# So x_dot = -K*x / (3*sqrt(FC*K/2)*|x|*M_eff) = -sqrt(K/(18*FC)) / (M_eff)
# Hmm, let me redo this carefully.

# Slow roll in FRW: 3*H*M_eff*x_dot + K*x = 0
# H^2 = FC * (1/2)*K*x^2 (potential dominated)
# H = sqrt(FC*K/2) * |x|
# x_dot = -K*x / (3*H*M_eff) = -K*x / (3*sqrt(FC*K/2)*|x|*M_eff) = -sqrt(K/(18*FC)) * sgn(x) / M_eff
# This is indeed a constant velocity (slow roll for harmonic potential).

v_slow_roll = np.sqrt(K_spring / (18 * FC_qnm)) / M_eff
print(f"\n  Slow-roll velocity (FLATBAND K): v_sr = {v_slow_roll:.4f} M_KK")
print(f"  Ballistic velocity: v_ball = {v_init:.4f} M_KK")
print(f"  v_ball / v_sr = {v_init/v_slow_roll:.2f}")

# N_e from slow roll across range x_1 to x_2:
# N_e = integral H dt = integral [H/x_dot] dx = integral [sqrt(FC*K/2)*|x| / (sqrt(K/(18*FC))/M_eff)] dx
# = integral [sqrt(FC*K/2) * M_eff * sqrt(18*FC/K) * |x|] dx
# = integral [sqrt(9*FC^2*M_eff^2) * |x|] dx = 3*FC*M_eff * integral |x| dx
# = 3*FC*M_eff * (x_1^2 - x_2^2) / 2  (from x_1 to x_2, x_2 < x_1)
# Actually: for x going from x_1 > 0 to x_2 = 0:
# N_e = (3/2) * FC * M_eff * x_1^2

# So for N_e > 10:
x_1_needed = np.sqrt(10 / (1.5 * FC_qnm * M_eff))
print(f"\n  For N_e = 10 from slow roll on V = (1/2)*K*x^2:")
print(f"  x_1 = sqrt(10 / (1.5*FC*M)) = {x_1_needed:.4f}")
print(f"  This requires the modulus to start at |tau - tau*| = {x_1_needed:.4f}")
print(f"  Which is {x_1_needed/tau_fold:.2f}x tau_fold")

# This is a MASSIVE displacement. The slow-roll formula for a quadratic potential
# requires an enormous initial displacement to get N_e ~ 10, because FC is tiny
# (~ 2e-6) and M is O(1).

# The eta_V for harmonic potential:
# eta_V = (1/(FC*M_eff)) * V''/V = (1/(FC*M_eff)) * K / ((1/2)*K*x^2) = 2/(FC*M_eff*x^2)
# = eps_V (for harmonic potential, eps_V = eta_V always!)
# So n_s = 1 - 6*eps_V + 2*eta_V = 1 - 4*eps_V = 1 - 8/(FC*M*x^2)
# At x = x_1 (start of slow roll): eps_V = 2/(FC*M*x_1^2)
# If N_e = (3/2)*FC*M*x_1^2, then eps_V = 2/((2/3)*N_e) = 3/N_e
# So: n_s = 1 - 4*3/N_e = 1 - 12/N_e

print(f"\n  For harmonic potential slow roll:")
print(f"  eps_V = 3/N_e = {3/10:.3f} (at N_e=10)")
print(f"  eta_V = eps_V = {3/10:.3f}")
print(f"  n_s = 1 - 12/N_e = {1 - 12/10:.3f} (at N_e=10)")
print(f"  n_s = 1 - 12/N_e = {1 - 12/60:.3f} (at N_e=60)")
print(f"  n_s = 1 - 12/N_e = {1 - 12/100:.3f} (at N_e=100)")
print(f"  NOTE: n_s = 0.80 at N_e=60 -- TOO RED compared to Planck 0.965")
print(f"  The quadratic potential gives n_s = 1 - 12/N (not 1 - 2/N)")
print(f"  This is the well-known exclusion of phi^2 inflation by Planck.")

# ============================================================================
# STEP 9: Comprehensive N_e Calculation
# ============================================================================
print("\n" + "=" * 78)
print("STEP 9: N_e Computation for All Scenarios")
print("=" * 78)

# Scenario A: FLATBAND crossing, actual K
Ne_A = H_fold_qnm * (1/gamma)  # = H * 2/(3H) = 2/3
print(f"  Scenario A (FLATBAND K={K_spring:.4f}, tau*={tau_star_fb:.4f}):")
print(f"    omega_0 = {omega_0:.6f}")
print(f"    gamma = {gamma:.6f}")
print(f"    t_dwell = 1/gamma = {1/gamma:.6e}")
print(f"    N_e = H*t_dwell = {Ne_A:.6f}")
print(f"    Verdict: {'PASS' if Ne_A > 10 else 'FAIL'} (threshold: 10)")

# Scenario B: Strong trap, K = K_capture
omega_0_B = np.sqrt(K_strong / M_eff)
gamma_B = gamma  # same Hubble
Q_B = omega_0_B / gamma_B
Ne_B_analytic = H_fold_qnm * (1/gamma)  # same dwell time
print(f"\n  Scenario B (K_capture={K_strong:.4e}, tau*={tau_fold}):")
print(f"    omega_0 = {omega_0_B:.4f}")
print(f"    gamma = {gamma_B:.4f}")
print(f"    Q = {Q_B:.4f}")
print(f"    N_e (dwell) = {Ne_B_analytic:.6f}")
print(f"    Even with capture, oscillation gives <eps_H> = 3/2 (virial)")
print(f"    N_e during quasi-static (from simulation) = {Ne_quasi_B:.6f}")

# Scenario C: Slow roll after capture at x_1 = 0.05
N_e_slowroll_005 = 1.5 * FC_qnm * M_eff * (0.05)**2
N_e_slowroll_01 = 1.5 * FC_qnm * M_eff * (0.10)**2
N_e_slowroll_1 = 1.5 * FC_qnm * M_eff * (1.0)**2
N_e_slowroll_10 = 1.5 * FC_qnm * M_eff * (10.0)**2
N_e_slowroll_100 = 1.5 * FC_qnm * M_eff * (100.0)**2
print(f"\n  Scenario C (slow-roll on V=(1/2)*K*x^2, FC={FC_qnm:.4e}, M={M_eff:.4f}):")
print(f"    x=0.05:  N_e = {N_e_slowroll_005:.6e}")
print(f"    x=0.10:  N_e = {N_e_slowroll_01:.6e}")
print(f"    x=1.0:   N_e = {N_e_slowroll_1:.6e}")
print(f"    x=10.0:  N_e = {N_e_slowroll_10:.6e}")
print(f"    x=100.0: N_e = {N_e_slowroll_100:.6e}")
print(f"    x for N_e=10: {x_1_needed:.4f}")
print(f"    x for N_e=60: {np.sqrt(60/(1.5*FC_qnm*M_eff)):.4f}")

# ============================================================================
# STEP 10: The Three Obstructions (Structural Analysis)
# ============================================================================
print("\n" + "=" * 78)
print("STEP 10: Three Obstructions to Quasi-Static Inflation")
print("=" * 78)

print("""
Obstruction 1: CAPTURE (KE >> PE_q)
  The modulus arrives at tau* with KE = {KE:.4e} M_KK^4.
  The q-theory spring constant K = {K:.4f} M_KK^4 produces PE = K*dx^2/2.
  For dx = 0.05: PE = {PE:.6f} M_KK^4.
  KE/PE = {ratio:.2e}. The modulus sails through without slowing.

Obstruction 2: OSCILLATION (virial <eps_H> = 3/2)
  Even if K were made large enough to capture the modulus (K ~ {Kcap:.4e}),
  the modulus would oscillate around tau* as a damped harmonic oscillator.
  By the virial theorem, <KE> = <PE_q>, so <eps_H> = 3/2 > 1.
  An oscillating modulus NEVER achieves slow-roll on average.

Obstruction 3: QUADRATIC INFLATION EXCLUDED BY PLANCK
  Even if slow roll could be achieved on the q-theory quadratic potential
  V = (1/2)*K*(tau-tau*)^2, the spectral tilt would be n_s = 1 - 12/N.
  For N_e = 60: n_s = 0.80 (5 sigma below Planck 0.965).
  The phi^2 potential is excluded at >10 sigma by Planck+BICEP.
""".format(KE=KE_ballistic, K=K_spring, PE=0.5*K_spring*0.05**2,
           ratio=KE_ballistic/(0.5*K_spring*0.05**2),
           Kcap=K_capture))

# ============================================================================
# STEP 11: Gate Verdict
# ============================================================================
print("=" * 78)
print("STEP 11: Gate Verdict")
print("=" * 78)

# The N_e during any quasi-static phase:
Ne_best = max(Ne_A, Ne_quasi_B if 'Ne_quasi_B' in dir() else 0)

# For the actual FLATBAND K:
Ne_primary = Ne_A  # = 2/3

gate_verdict = "FAIL"
gate_detail = ""

if Ne_primary > 10:
    gate_verdict = "PASS"
    gate_detail = f"N_e = {Ne_primary:.4f} > 10 (quasi-static inflation achieved)"
elif Ne_primary > 0.1:
    gate_verdict = "INFO"
    gate_detail = f"N_e = {Ne_primary:.4f} in [0.1, 10] (marginal, insufficient for inflation)"
else:
    gate_verdict = "FAIL"
    gate_detail = f"N_e = {Ne_primary:.4f} < 0.1 (no quasi-static phase)"

print(f"\n  GATE QUASISTATIC-NS-46: {gate_verdict}")
print(f"  {gate_detail}")
print(f"\n  N_e values:")
print(f"    FLATBAND analytical:        {Ne_A:.6f}")
print(f"    K_capture simulated:        {Ne_quasi_B:.6f}")
print(f"    Slow-roll (x=0.05):         {N_e_slowroll_005:.6e}")
print(f"\n  Three structural obstructions prevent N_e > 10:")
print(f"    1. KE/PE_q ~ {KE_ballistic/(0.5*K_spring*0.05**2):.2e} (no capture)")
print(f"    2. Virial <eps_H> = 3/2 (no slow roll during oscillation)")
print(f"    3. phi^2 inflation excluded by Planck (n_s = 0.80 at N_e=60)")

# ============================================================================
# STEP 12: Slow-Roll n_s IF Quasi-Static Were Achieved
# ============================================================================
print("\n" + "=" * 78)
print("STEP 12: Hypothetical n_s (If Slow Roll Were Achieved)")
print("=" * 78)

# Using the S45 QNM-NS values eps_V and eta_V:
ns_slowroll_qnm = 1 - 6*eps_V_fold + 2*eta_V_fold
print(f"  From S45 QNM-NS-45 (spectral action potential):")
print(f"    eps_V = {eps_V_fold:.6f}")
print(f"    eta_V = {eta_V_fold:.6f}")
print(f"    n_s = 1 - 6*eps_V + 2*eta_V = {ns_slowroll_qnm:.4f}")
print(f"    This is from the SPECTRAL ACTION potential, not the q-theory potential.")

# For the q-theory harmonic potential V = (1/2)*K*x^2:
# eps_V = eta_V = 2/(FC*M*x^2) = 3/N_e
ns_qtrap = lambda Ne: 1 - 12.0/Ne
print(f"\n  From q-theory harmonic potential V = (1/2)*K*(tau-tau*)^2:")
print(f"    n_s = 1 - 12/N_e")
for Ne_val in [10, 20, 40, 60, 80, 100, 200]:
    print(f"    N_e = {Ne_val:4d}: n_s = {ns_qtrap(Ne_val):.4f}  ({'PASS' if abs(ns_qtrap(Ne_val) - 0.965) < 0.01 else 'FAIL'})")

# For the spectral action potential (eps_V = 0.016, eta_V = 0.749):
# n_s = 2.40 (WAY too blue). This was known from S45.

print(f"\n  CONCLUSION: Neither potential gives acceptable n_s.")
print(f"  Spectral action (eps_V=0.016, eta_V=0.749): n_s = {ns_slowroll_qnm:.4f} (too blue)")
print(f"  q-theory harmonic (phi^2): n_s = 0.80 at N_e=60 (too red)")
print(f"  The n_s crisis (S45) is NOT resolved by the q-theory quasi-static phase.")

# ============================================================================
# STEP 13: Save Results
# ============================================================================
print("\n--- Saving Results ---")

save_dict = {
    'gate_name': np.array(['QUASISTATIC-NS-46']),
    'gate_verdict': np.array([gate_verdict]),
    'gate_detail': np.array([gate_detail]),

    # Q-theory potential parameters
    'tau_star_fb': np.float64(tau_star_fb),
    'K_spring': np.float64(K_spring),
    'drho_dtau_at_star': np.float64(drho_dtau_at_star),
    'd2rho_dtau2_at_star': np.float64(d2rho_dtau2_at_star),
    'omega_osc': np.float64(omega_0),
    'gamma_Hubble': np.float64(gamma),
    'Q_factor': np.float64(Q_factor),

    # Energy balance
    'KE_ballistic': np.float64(KE_ballistic),
    'PE_max_005': np.float64(0.5 * K_spring * 0.05**2),
    'KE_over_PE': np.float64(KE_ballistic / (0.5 * K_spring * 0.05**2)),
    'K_capture': np.float64(K_capture),
    'K_over_K_FLATBAND': np.float64(K_capture / K_spring),

    # N_e results
    'Ne_flatband_analytic': np.float64(Ne_A),
    'Ne_capture_simulated': np.float64(Ne_quasi_B),
    'Ne_slowroll_x005': np.float64(N_e_slowroll_005),
    'x_for_Ne10': np.float64(x_1_needed),

    # Slow-roll parameters
    'eps_V_spectral': np.float64(eps_V_fold),
    'eta_V_spectral': np.float64(eta_V_fold),
    'ns_spectral': np.float64(ns_slowroll_qnm),
    'ns_qtrap_Ne60': np.float64(ns_qtrap(60)),

    # Velocity parameters
    'v_ballistic': np.float64(v_init),
    'v_slow_limit': np.float64(v_slow_limit),
    'velocity_reduction_needed': np.float64(v_init / v_slow_limit),

    # Upstream references
    'H_fold_qnm': np.float64(H_fold_qnm),
    'FC': np.float64(FC_qnm),
    'M_ATDHFB': np.float64(M_eff),
    'eps_H_fold': np.float64(eps_H_fold),

    # Scan results
    'K_scan': np.array([r['K'] for r in results_A]),
    'Ne_scan': np.array([r['Ne'] for r in results_A]),
    'Ne_quasi_scan': np.array([r['Ne_quasi'] for r in results_A]),
    'captured_scan': np.array([r['captured'] for r in results_A]),
    'min_eps_H_scan': np.array([r['min_eps_H'] for r in results_A]),
}

np.savez('tier0-computation/s46_quasistatic_ns.npz', **save_dict)
print("Saved: tier0-computation/s46_quasistatic_ns.npz")

# ============================================================================
# STEP 14: Plots
# ============================================================================
print("Generating plots...")

fig = plt.figure(figsize=(18, 14))
gs = GridSpec(3, 3, figure=fig, hspace=0.35, wspace=0.30)
fig.suptitle('QUASISTATIC-NS-46: Quasi-Static Phase at q-Theory Equilibrium\n'
             f'Gate: {gate_verdict}', fontsize=13, fontweight='bold')

# A: Q-theory potential (Gibbs-Duhem)
ax = fig.add_subplot(gs[0, 0])
mask = (tau_dense_fb > 0.10) & (tau_dense_fb < 0.35)
ax.plot(tau_dense_fb[mask], rho_raw_fb[mask], 'C0-', lw=1.5, label='FLATBAND $\\rho_{raw}$')
ax.axhline(0, color='gray', ls='--', lw=0.5)
ax.axvline(tau_star_fb, color='green', ls=':', label=f'$\\tau^* = {tau_star_fb:.3f}$')
ax.axvline(tau_fold, color='red', ls=':', label=f'$\\tau_{{fold}} = {tau_fold}$')
ax.set_xlabel('$\\tau$'); ax.set_ylabel('$\\rho_{raw}$ ($M_{KK}^4$)')
ax.set_title('A: Gibbs-Duhem Crossing')
ax.legend(fontsize=7)

# B: Energy balance
ax = fig.add_subplot(gs[0, 1])
log_K = np.log10([r['K'] for r in results_A])
log_KE = np.log10(KE_ballistic)
ax.axhline(log_KE, color='red', ls='--', lw=2, label=f'log KE = {log_KE:.1f}')
for i, r in enumerate(results_A):
    PE_at_005 = 0.5 * r['K'] * 0.05**2
    if PE_at_005 > 0:
        ax.plot(log_K[i], np.log10(PE_at_005), 'C0o', ms=4)
ax.plot(log_K, [np.log10(0.5*r['K']*0.05**2) if r['K']>0 else -10 for r in results_A],
        'C0-', label='PE at $\\delta\\tau = 0.05$')
ax.axvline(np.log10(K_spring), color='green', ls=':', label=f'K_FB = {K_spring:.2f}')
ax.axvline(np.log10(K_capture), color='purple', ls=':', label=f'K_cap = {K_capture:.1e}')
ax.set_xlabel('log$_{10}$ K'); ax.set_ylabel('log$_{10}$ Energy')
ax.set_title('B: Energy Balance for Capture')
ax.legend(fontsize=6)

# C: N_e vs K
ax = fig.add_subplot(gs[0, 2])
Ne_arr = np.array([r['Ne'] for r in results_A])
K_arr = np.array([r['K'] for r in results_A])
mask_pos = Ne_arr > 0
ax.semilogx(K_arr[mask_pos], Ne_arr[mask_pos], 'C0o-', ms=4)
ax.axhline(10, color='red', ls='--', label='N_e = 10 (PASS)')
ax.axhline(0.1, color='orange', ls='--', label='N_e = 0.1 (FAIL)')
ax.axvline(K_spring, color='green', ls=':', label=f'K_FB')
ax.set_xlabel('K ($M_{KK}^4$)'); ax.set_ylabel('$N_e$')
ax.set_title('C: $N_e$ vs Spring Constant K')
ax.legend(fontsize=7)

# D: eps_H during transit (baseline)
ax = fig.add_subplot(gs[1, 0])
mask_fold = np.abs(tau_base - 0.19) < 0.08
if np.any(mask_fold):
    ax.plot(tau_base[mask_fold], eps_H_base[mask_fold], 'C0-', lw=1.5)
ax.axhline(1, color='red', ls='--', label='$\\epsilon_H = 1$')
ax.axhline(3, color='orange', ls=':', label='Stiff matter')
ax.axvline(tau_fold, color='red', ls=':', alpha=0.5)
ax.set_xlabel('$\\tau$'); ax.set_ylabel('$\\epsilon_H$')
ax.set_title('D: $\\epsilon_H$ During Transit (no trap)')
ax.legend(fontsize=7)
ax.set_ylim(0, 4)

# E: Harmonic oscillator phase portrait
ax = fig.add_subplot(gs[1, 1])
# Draw the phase space for the damped HO with FLATBAND K
t_ho = np.linspace(0, 5/gamma, 1000)
if omega_0 > gamma:
    omega_d_val = np.sqrt(omega_0**2 - gamma**2)
    A_ho = x_0
    B_ho = (xdot_0 + gamma * x_0) / omega_d_val
    x_ho = np.exp(-gamma*t_ho) * (A_ho * np.cos(omega_d_val*t_ho) + B_ho * np.sin(omega_d_val*t_ho))
    xdot_ho = (np.exp(-gamma*t_ho) *
               ((-gamma*A_ho + omega_d_val*B_ho)*np.cos(omega_d_val*t_ho) +
                (-gamma*B_ho - omega_d_val*A_ho)*np.sin(omega_d_val*t_ho)))
else:
    x_ho = x_0 * np.exp(-gamma*t_ho) * np.cosh(gamma*t_ho)
    xdot_ho = xdot_0 * np.exp(-gamma*t_ho)

ax.plot(x_ho[:200] + tau_star_A, xdot_ho[:200], 'C0-', lw=0.8, alpha=0.7)
ax.plot(x_ho[0] + tau_star_A, xdot_ho[0], 'go', ms=8, label='Start')
ax.axvline(tau_star_A, color='green', ls=':', alpha=0.5)
ax.axvline(tau_fold, color='red', ls=':', alpha=0.5)
ax.set_xlabel('$\\tau$'); ax.set_ylabel('$\\dot{\\tau}$ ($M_{KK}$)')
ax.set_title('E: Phase Portrait (FLATBAND K)')
ax.legend(fontsize=7)

# F: N_e as function of starting displacement (slow-roll on phi^2)
ax = fig.add_subplot(gs[1, 2])
x_range = np.logspace(-2, 4, 100)
Ne_sr = 1.5 * FC_qnm * M_eff * x_range**2
ax.loglog(x_range, Ne_sr, 'C0-', lw=2)
ax.axhline(10, color='red', ls='--', label='$N_e = 10$')
ax.axhline(60, color='blue', ls='--', label='$N_e = 60$')
ax.axvspan(0, 0.4, color='green', alpha=0.1, label='Physical $\\tau$ range')
ax.set_xlabel('Starting displacement $|\\tau - \\tau^*|$')
ax.set_ylabel('$N_e$ (slow roll)')
ax.set_title('F: $N_e$ from Quadratic Slow Roll')
ax.legend(fontsize=7)

# G: n_s vs N_e for different potentials
ax = fig.add_subplot(gs[2, 0])
Ne_plot = np.linspace(5, 200, 100)
ns_phi2 = 1 - 12/Ne_plot
ns_phi4 = 1 - 20/Ne_plot  # phi^4 for comparison
ns_monomial = lambda p, N: 1 - (2+p)*(2+p)/(p*N)  # n_s for V ~ phi^p
ax.plot(Ne_plot, ns_phi2, 'C0-', lw=2, label='$V \\sim \\phi^2$ (q-theory)')
ax.plot(Ne_plot, 1-2/Ne_plot, 'C1--', lw=1.5, label='$V \\sim e^{-\\phi}$ (Starobinsky)')
ax.axhline(0.965, color='red', ls='--', lw=2, label='Planck $n_s = 0.965$')
ax.axhspan(0.955, 0.975, color='red', alpha=0.1)
ax.axvline(60, color='gray', ls=':', alpha=0.5)
ax.set_xlabel('$N_e$'); ax.set_ylabel('$n_s$')
ax.set_title('G: $n_s$ vs $N_e$ by Potential')
ax.legend(fontsize=7)
ax.set_ylim(0.7, 1.05)

# H: Three obstructions summary
ax = fig.add_subplot(gs[2, 1])
obs_names = ['Capture\n(KE/PE)', 'Oscillation\n(<eps_H>=3/2)', 'n_s at N=60\n(vs Planck)']
obs_vals = [KE_ballistic/(0.5*K_spring*0.05**2), 1.5, abs(0.80 - 0.965)]
obs_thresh = [1.0, 1.0, 0.01]  # thresholds
colors = ['red' if v > th else 'green' for v, th in zip(obs_vals, obs_thresh)]
ax.bar(obs_names, [np.log10(obs_vals[0]), obs_vals[1], obs_vals[2]*100],
       color=colors, alpha=0.7, edgecolor='black')
ax.set_ylabel('Obstruction Magnitude')
ax.set_title('H: Three Obstructions')
for i, (v, txt) in enumerate(zip(obs_vals, [f'{v:.1e}' for v in obs_vals])):
    ax.text(i, ax.get_ylim()[1]*0.9, txt, ha='center', fontsize=8, fontweight='bold')

# I: Summary text
ax = fig.add_subplot(gs[2, 2])
ax.axis('off')
summary_text = (
    f"QUASISTATIC-NS-46: {gate_verdict}\n"
    f"{'='*40}\n\n"
    f"Q-theory crossing: tau* = {tau_star_fb:.4f} (FLATBAND)\n"
    f"Spring constant: K = {K_spring:.4f} M_KK^4\n"
    f"omega_osc = {omega_0:.4f}, gamma = {gamma:.4f}\n"
    f"Q = {Q_factor:.4f}\n\n"
    f"Ballistic KE = {KE_ballistic:.2e} M_KK^4\n"
    f"PE(delta=0.05) = {0.5*K_spring*0.05**2:.2e} M_KK^4\n"
    f"KE/PE = {KE_ballistic/(0.5*K_spring*0.05**2):.2e}\n\n"
    f"N_e (FLATBAND) = {Ne_A:.4f}\n"
    f"N_e (capture) = {Ne_quasi_B:.4f}\n\n"
    f"Three obstructions:\n"
    f"  1. No capture (KE >> PE)\n"
    f"  2. Virial eps_H = 3/2\n"
    f"  3. phi^2 excluded by Planck"
)
ax.text(0.05, 0.95, summary_text, transform=ax.transAxes,
        fontsize=9, verticalalignment='top', fontfamily='monospace',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.savefig('tier0-computation/s46_quasistatic_ns.png', dpi=150, bbox_inches='tight')
print("Saved: tier0-computation/s46_quasistatic_ns.png")

# ============================================================================
# FINAL SUMMARY
# ============================================================================
print("\n" + "=" * 78)
print("FINAL SUMMARY: QUASISTATIC-NS-46")
print("=" * 78)

print(f"""
  GATE: QUASISTATIC-NS-46 = {gate_verdict}
  {gate_detail}

  === Q-Theory Potential ===
  Crossing: tau* = {tau_star_fb:.4f} (FLATBAND only, SC has no crossing)
  Spring constant: K = drho/dtau = {K_spring:.4f} M_KK^4
  Oscillation frequency: omega_0 = {omega_0:.6f} M_KK
  Hubble damping: gamma = 3H/2 = {gamma:.4f} M_KK
  Quality factor: Q = {Q_factor:.4f} ({'under' if omega_0 < gamma else 'over'}damped)

  === Energy Balance ===
  KE_ballistic = {KE_ballistic:.4e} M_KK^4
  PE_q(delta=0.05) = {0.5*K_spring*0.05**2:.4e} M_KK^4
  KE/PE = {KE_ballistic/(0.5*K_spring*0.05**2):.2e}
  K needed for capture = {K_capture:.4e} M_KK^4 = {K_capture/K_spring:.2e} x K_FLATBAND

  === N_e Results ===
  N_e (FLATBAND, analytical) = {Ne_A:.4f}
  N_e (K_capture, simulated) = {Ne_quasi_B:.4f}
  N_e (slow-roll, x=0.05) = {N_e_slowroll_005:.2e}
  x needed for N_e = 10: {x_1_needed:.4f}
  x needed for N_e = 60: {np.sqrt(60/(1.5*FC_qnm*M_eff)):.4f}

  === Hypothetical n_s ===
  Spectral action slow roll: n_s = {ns_slowroll_qnm:.4f} (eps_V={eps_V_fold:.3f}, eta_V={eta_V_fold:.3f})
  q-theory phi^2 (N_e=60): n_s = {ns_qtrap(60):.4f}
  Planck: n_s = 0.9649 +/- 0.0042

  === Three Structural Obstructions ===
  1. CAPTURE: KE/PE ~ {KE_ballistic/(0.5*K_spring*0.05**2):.2e} >> 1. Modulus not captured.
  2. VIRIAL: Even if captured, <eps_H> = 3/2 (oscillation, not slow roll).
  3. PLANCK: phi^2 inflation gives n_s = 0.80 at N_e=60 (excluded at >10 sigma).

  === Constraint Map Update ===
  Quasi-static inflation at q-theory equilibrium: CLOSED.
  Three independent obstructions, any one of which is sufficient.
  The n_s crisis is NOT resolved by the q-theory potential.

  Files: s46_quasistatic_ns.py, .npz, .png
""")

print("=" * 78)
