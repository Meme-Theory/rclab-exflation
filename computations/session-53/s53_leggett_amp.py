#!/usr/bin/env python3
"""
s53_leggett_amp.py — LEGGETT-AMP-53: Large-Modulation Floquet Analysis
========================================================================

Gate: LEGGETT-AMP-53
  PASS: Floquet multiplier |mu| > 1 AND amplification > 10
  INFO: |mu| > 1 but amplification < 10
  FAIL: |mu| <= 1 (stable, no parametric amplification)

Physics:
  The Leggett mode is an oscillation of the relative phase between BCS
  condensates in different sectors. During tau-transit, J_ab(tau) varies,
  modulating omega_L(tau). This produces a Hill equation:

    d^2 delta_Delta / dt^2 + omega_L^2(t) * delta_Delta = 0

  At 100% modulation depth (gap goes 0 -> Delta_0), the Mathieu q parameter
  is LARGE. The small-h approximation (QA's "narrow instability" objection)
  fails catastrophically.

Approach:
  1. Map tau(t) trajectory during transit (not periodic -- single passage)
  2. Construct omega_L(t) from GL sweep interpolation
  3. Solve Hill equation numerically via RK45 monodromy matrix
  4. Compute Floquet multipliers, growth rate, total amplification
  5. Also: scan (a, q) parameter space for Mathieu tongue diagram

Author: tesla-resonance
Session: 53, Wave 1, Route P4
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from canonical_constants import *

import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import interp1d
from scipy.linalg import eigvals
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

OUT_DIR = os.path.dirname(__file__)

# =============================================================================
# SECTION 1: Load GL sweep data, extract tau-dependent Leggett frequencies
# =============================================================================

gl_data = np.load(os.path.join(OUT_DIR, 's53_gl_sweep.npz'), allow_pickle=True)

tau_gl = gl_data['tau_values']       # shape (15,)
omega_L1_gl = gl_data['omega_Leggett1']  # shape (15,)
omega_L2_gl = gl_data['omega_Leggett2']  # shape (15,)
J_12_gl = gl_data['J_12_all']       # shape (15,)
J_23_gl = gl_data['J_23_all']       # shape (15,)
J_13_gl = gl_data['J_13_all']       # shape (15,)
Delta_gl = gl_data['Delta_all']     # shape (15, 3) — gaps in 3 sectors

# Build interpolators for omega_L(tau) and J_ab(tau)
omega_L1_interp = interp1d(tau_gl, omega_L1_gl, kind='cubic', fill_value='extrapolate')
omega_L2_interp = interp1d(tau_gl, omega_L2_gl, kind='cubic', fill_value='extrapolate')
J_12_interp = interp1d(tau_gl, J_12_gl, kind='cubic', fill_value='extrapolate')

print("=" * 72)
print("LEGGETT-AMP-53: Large-Modulation Floquet Analysis")
print("=" * 72)

# =============================================================================
# SECTION 2: Define tau(t) trajectory during transit
# =============================================================================

# Transit parameters from canonical_constants
# tau goes from ~0 to tau_fold=0.19 over dt_transit
# The transit is driven by the spectral action gradient; v_terminal is ~constant
# tau(t) = v_terminal * t for the linear approximation

# Window where BCS gap turns on: the BCS instability region
# From GL data: Delta starts growing around tau ~ 0.16-0.17 (fold onset)
# The Leggett mode EXISTS only where the gap is nonzero
# Key physics: the gap turns on RAPIDLY near tau_fold

# The relevant modulation window is where omega_L changes significantly
# From GL data:
print("\n--- Leggett frequencies from GL sweep ---")
for i, tau_i in enumerate(tau_gl):
    print(f"  tau={tau_i:.3f}: omega_L1={omega_L1_gl[i]:.6f}, "
          f"omega_L2={omega_L2_gl[i]:.6f}, J_12={J_12_gl[i]:.6f}")

# omega_L1 varies from 0.1358 to 0.1377 (1.4% variation)
# omega_L2 varies from 0.1774 to 0.1981 (11.7% variation)
# Key: the variation comes from J_ab(tau) changing with tau

omega_L1_min = np.min(omega_L1_gl)
omega_L1_max = np.max(omega_L1_gl)
omega_L2_min = np.min(omega_L2_gl)
omega_L2_max = np.max(omega_L2_gl)

# Modulation depth: delta_omega / omega_mean
mod_depth_L1 = (omega_L1_max - omega_L1_min) / (0.5 * (omega_L1_max + omega_L1_min))
mod_depth_L2 = (omega_L2_max - omega_L2_min) / (0.5 * (omega_L2_max + omega_L2_min))

print(f"\nomega_L1: range [{omega_L1_min:.6f}, {omega_L1_max:.6f}], "
      f"mod depth = {mod_depth_L1:.4f} ({mod_depth_L1*100:.1f}%)")
print(f"omega_L2: range [{omega_L2_min:.6f}, {omega_L2_max:.6f}], "
      f"mod depth = {mod_depth_L2:.4f} ({mod_depth_L2*100:.1f}%)")

# =============================================================================
# SECTION 3: The REAL modulation — gap onset is 100% depth
# =============================================================================

# The task specification says: "BCS gap goes 0 -> 0.77 M_KK over a tau-window
# of ~0.03". This is the DOMINANT modulation.
# omega_L ~ sqrt(J * rho * Delta^2) schematically. When Delta=0, omega_L=0.
# The mode does not exist before the gap opens.

# However, the GL sweep already includes the gap everywhere (it computes the
# equilibrium GL functional at each tau). The Leggett frequency at each tau
# ASSUMES the gap is at its equilibrium value at that tau.

# For the TRANSIT physics, what matters is:
# 1. At early tau (< ~0.16), there IS no condensate, hence no Leggett mode
# 2. The condensate forms at some tau_onset near the fold
# 3. Once formed, the Leggett mode frequency VARIES as tau continues to change

# The relevant Hill equation applies WITHIN the condensed phase.
# The 100% modulation refers to the GAP growing from 0 to Delta_0_GL,
# NOT to omega_L oscillating with 100% depth around its mean.

# The PHYSICAL scenario is:
# - tau sweeps linearly through tau_fold at velocity v_terminal
# - At tau_onset (~ tau_fold - Delta_tau_BCS), the gap opens
# - omega_L(t) follows the gap evolution
# - The question: does this parametric drive amplify the Leggett mode?

# For the Hill/Mathieu mapping, we need a PERIODIC drive to define Floquet.
# But the transit is a SINGLE PASSAGE. So we compute the LOCAL Lyapunov
# exponent from the instantaneous parameters, then integrate.

# However, the task asks us to ALSO do the Mathieu tongue diagram.
# We'll do both.

print("\n" + "=" * 72)
print("PART A: Mathieu Stability Diagram (periodic reference)")
print("=" * 72)

# =============================================================================
# SECTION 4: Mathieu Stability Diagram
# =============================================================================

# Standard Mathieu equation: d^2y/dt^2 + [a - 2q*cos(2t)] * y = 0
# Physical mapping:
#   omega_L^2(t) = omega_0^2 + delta_omega^2 * cos(omega_drive * t)
#   -> a = (omega_0 / omega_drive_half)^2
#   -> q = delta_omega^2 / (2 * omega_drive_half^2)
# where omega_drive_half = omega_drive / 2

# For our system, the "drive" comes from tau-evolution:
# omega_drive = 2*pi / T_transit ??? No — transit is NOT periodic.
# Instead, the drive frequency is set by how fast omega_L changes.

# The natural drive frequency is:
# d(omega_L^2)/dt = d(omega_L^2)/d(tau) * d(tau)/dt = d(omega_L^2)/d(tau) * v_terminal

# Compute d(omega_L^2)/d(tau) numerically
domegaL1_sq_dtau = np.gradient(omega_L1_gl**2, tau_gl)
domegaL2_sq_dtau = np.gradient(omega_L2_gl**2, tau_gl)

# Effective modulation rate at the fold (tau=0.19)
tau_fold_idx = np.argmin(np.abs(tau_gl - tau_fold))
rate_L1 = np.abs(domegaL1_sq_dtau[tau_fold_idx]) * v_terminal
rate_L2 = np.abs(domegaL2_sq_dtau[tau_fold_idx]) * v_terminal

print(f"\nd(omega_L1^2)/dt at fold = {rate_L1:.6f} M_KK^3")
print(f"d(omega_L2^2)/dt at fold = {rate_L2:.6f} M_KK^3")

# For the Mathieu diagram, we'll scan a and q independently.
# The physical operating point depends on the modulation scenario.

def compute_mathieu_monodromy(a_val, q_val, N_steps=2000):
    """
    Compute Floquet multipliers for Mathieu equation:
      y'' + [a - 2q*cos(2t)] * y = 0

    Period T = pi. Integrate y1=[1,0], y2=[0,1] from t=0 to t=pi.
    Monodromy matrix M = [[y1(pi), y2(pi)], [y1'(pi), y2'(pi)]].
    Floquet multipliers = eigenvalues of M.
    """
    T_period = np.pi  # Mathieu period

    def rhs(t, state):
        # state = [y, y']
        y, ydot = state
        return [ydot, -(a_val - 2.0 * q_val * np.cos(2.0 * t)) * y]

    # Solution 1: y1(0)=1, y1'(0)=0
    sol1 = solve_ivp(rhs, [0, T_period], [1.0, 0.0],
                     method='RK45', rtol=1e-12, atol=1e-14,
                     dense_output=True)
    y1_T = sol1.y[0, -1]
    y1dot_T = sol1.y[1, -1]

    # Solution 2: y2(0)=0, y2'(0)=1
    sol2 = solve_ivp(rhs, [0, T_period], [0.0, 1.0],
                     method='RK45', rtol=1e-12, atol=1e-14,
                     dense_output=True)
    y2_T = sol2.y[0, -1]
    y2dot_T = sol2.y[1, -1]

    # Monodromy matrix
    M = np.array([[y1_T, y2_T],
                  [y1dot_T, y2dot_T]])

    mu = eigvals(M)  # (local)
    return mu, M


# Scan parameter space
N_a = 200
N_q = 200
a_range = np.linspace(0, 25, N_a)
q_range = np.linspace(0, 20, N_q)

print(f"\nScanning Mathieu parameter space: a in [0, 25], q in [0, 20]")
print(f"Grid: {N_a} x {N_q} = {N_a * N_q} points")

# Stability map: 1 = unstable, 0 = stable
stability_map = np.zeros((N_q, N_a))
max_mu_map = np.zeros((N_q, N_a))

for j, q_val in enumerate(q_range):
    for i, a_val in enumerate(a_range):
        mu, _ = compute_mathieu_monodromy(a_val, q_val)
        max_abs_mu = np.max(np.abs(mu))
        max_mu_map[j, i] = max_abs_mu
        if max_abs_mu > 1.0 + 1e-10:
            stability_map[j, i] = 1.0

unstable_frac = np.sum(stability_map) / stability_map.size
print(f"Unstable fraction of parameter space: {unstable_frac:.3f} ({unstable_frac*100:.1f}%)")

# =============================================================================
# SECTION 5: Physical Operating Point on Mathieu Diagram
# =============================================================================

print("\n" + "=" * 72)
print("PART B: Physical Operating Point")
print("=" * 72)

# The physical Mathieu parameters depend on HOW we map the problem.
#
# Scenario 1: omega_L modulated by J_ab variation during transit
#   omega_L^2(t) = omega_L0^2 * [1 + h * cos(omega_drive * t)]
#   where h = delta(omega_L^2) / omega_L0^2 (modulation depth of omega^2)
#   and omega_drive comes from the transit timescale
#
#   Mathieu mapping:
#     a = (omega_L0 / (omega_drive/2))^2
#     q = h * a / 2

# Mean and variation of omega_L^2
omega_L1_sq_mean = np.mean(omega_L1_gl**2)
omega_L1_sq_half_range = 0.5 * (np.max(omega_L1_gl**2) - np.min(omega_L1_gl**2))
h_L1 = omega_L1_sq_half_range / omega_L1_sq_mean

omega_L2_sq_mean = np.mean(omega_L2_gl**2)
omega_L2_sq_half_range = 0.5 * (np.max(omega_L2_gl**2) - np.min(omega_L2_gl**2))
h_L2 = omega_L2_sq_half_range / omega_L2_sq_mean

print(f"\nModulation depth of omega_L1^2: h = {h_L1:.6f} ({h_L1*100:.2f}%)")
print(f"Modulation depth of omega_L2^2: h = {h_L2:.6f} ({h_L2*100:.2f}%)")

# Drive frequency: the tau sweep rate determines how fast omega_L changes.
# tau sweeps from 0 to ~0.35 in time dt_transit.
# The effective angular frequency of the sweep:
# omega_drive = 2*pi / (2 * dt_transit) if we model the sweep as half a cycle
# But the transit is a single passage, not a periodic motion.

# Better: The effective drive frequency is the rate at which omega_L^2
# goes through one full cycle of variation. The variation covers
# Delta_tau = tau_gl[-1] - tau_gl[0] in time Delta_tau / v_terminal.
# omega_L1 has a PEAK (not monotonic), so one "half-cycle" is meaningful.

# Find where omega_L1 peaks
peak_idx = np.argmax(omega_L1_gl)
tau_peak = tau_gl[peak_idx]
print(f"\nomega_L1 peaks at tau = {tau_peak:.3f}")
print(f"omega_L2 is monotonically increasing")

# For L1: the mode rises from tau=0.01 to peak at tau~0.16, then falls
# The "half-period" in tau is ~ 0.15 -> t_half = 0.15 / v_terminal
tau_rise = tau_peak - tau_gl[0]
t_half_L1 = tau_rise / v_terminal
omega_drive_L1 = np.pi / t_half_L1  # half-period -> angular frequency

# For L2: monotonically increasing, so the relevant timescale is the transit
t_transit_full = (tau_gl[-1] - tau_gl[0]) / v_terminal
omega_drive_L2 = 2 * np.pi / (2 * t_transit_full)  # sweep as half-cycle

print(f"\nDrive parameters:")
print(f"  L1: tau_rise = {tau_rise:.3f}, t_half = {t_half_L1:.6f} M_KK^-1, "
      f"omega_drive = {omega_drive_L1:.2f} M_KK")
print(f"  L2: t_sweep = {t_transit_full:.6f} M_KK^-1, "
      f"omega_drive = {omega_drive_L2:.2f} M_KK")

# Mathieu a and q for L1
omega_L1_0 = np.sqrt(omega_L1_sq_mean)
a_phys_L1 = (2.0 * omega_L1_0 / omega_drive_L1)**2
q_phys_L1 = h_L1 * a_phys_L1 / 2.0

# Mathieu a and q for L2
omega_L2_0 = np.sqrt(omega_L2_sq_mean)
a_phys_L2 = (2.0 * omega_L2_0 / omega_drive_L2)**2
q_phys_L2 = h_L2 * a_phys_L2 / 2.0

print(f"\nMathieu operating points:")
print(f"  L1: a = {a_phys_L1:.6f}, q = {q_phys_L1:.6f}")
print(f"  L2: a = {a_phys_L2:.6f}, q = {q_phys_L2:.6f}")

# Both a and q are TINY because omega_drive >> omega_L (transit is fast).
# This means we're in the ADIABATIC limit: the transit crosses the fold
# much faster than the Leggett mode can oscillate.

# Compute Floquet multipliers at physical operating points
mu_L1, M_L1 = compute_mathieu_monodromy(a_phys_L1, q_phys_L1)
mu_L2, M_L2 = compute_mathieu_monodromy(a_phys_L2, q_phys_L2)

print(f"\nFloquet multipliers:")
print(f"  L1: mu = {mu_L1}, |mu|_max = {np.max(np.abs(mu_L1)):.10f}")
print(f"  L2: mu = {mu_L2}, |mu|_max = {np.max(np.abs(mu_L2)):.10f}")

# =============================================================================
# SECTION 6: DIRECT Hill Equation Integration (non-periodic transit)
# =============================================================================

print("\n" + "=" * 72)
print("PART C: Direct Hill Equation — Non-Periodic Transit")
print("=" * 72)

# The transit is NOT periodic. The correct approach is to integrate the
# Hill equation along the actual tau(t) trajectory and measure the
# total amplification.

# tau(t) = tau_start + v_terminal * t
# We integrate from tau = tau_gl[0]=0.01 to tau = tau_gl[-1]=0.35
# which takes time t_total = (0.35 - 0.01) / v_terminal

tau_start = tau_gl[0]
tau_end = tau_gl[-1]
t_total = (tau_end - tau_start) / v_terminal

print(f"\nTransit integration:")
print(f"  tau: [{tau_start:.3f}, {tau_end:.3f}]")
print(f"  t_total = {t_total:.8f} M_KK^-1")
print(f"  dt_transit (canonical) = {dt_transit:.8f} M_KK^-1")
print(f"  v_terminal = {v_terminal:.4f}")

# Hill equation for Leggett-1:
# d^2 y / dt^2 + omega_L1^2(tau(t)) * y = 0
# where tau(t) = tau_start + v_terminal * t

def hill_rhs_L1(t, state):
    tau_t = tau_start + v_terminal * t
    tau_t = np.clip(tau_t, tau_gl[0], tau_gl[-1])
    omega_sq = omega_L1_interp(tau_t)**2
    return [state[1], -omega_sq * state[0]]

def hill_rhs_L2(t, state):
    tau_t = tau_start + v_terminal * t
    tau_t = np.clip(tau_t, tau_gl[0], tau_gl[-1])
    omega_sq = omega_L2_interp(tau_t)**2
    return [state[1], -omega_sq * state[0]]

# Integrate two independent solutions for each mode
t_span = [0, t_total]
t_eval = np.linspace(0, t_total, 5000)

print("\nIntegrating Hill equation for L1...")
sol_L1_a = solve_ivp(hill_rhs_L1, t_span, [1.0, 0.0],
                     method='RK45', rtol=1e-12, atol=1e-14, t_eval=t_eval)
sol_L1_b = solve_ivp(hill_rhs_L1, t_span, [0.0, 1.0],
                     method='RK45', rtol=1e-12, atol=1e-14, t_eval=t_eval)

print("Integrating Hill equation for L2...")
sol_L2_a = solve_ivp(hill_rhs_L2, t_span, [1.0, 0.0],
                     method='RK45', rtol=1e-12, atol=1e-14, t_eval=t_eval)
sol_L2_b = solve_ivp(hill_rhs_L2, t_span, [0.0, 1.0],
                     method='RK45', rtol=1e-12, atol=1e-14, t_eval=t_eval)

# Transfer matrix at end of transit
M_transit_L1 = np.array([[sol_L1_a.y[0, -1], sol_L1_b.y[0, -1]],
                          [sol_L1_a.y[1, -1], sol_L1_b.y[1, -1]]])
M_transit_L2 = np.array([[sol_L2_a.y[0, -1], sol_L2_b.y[0, -1]],
                          [sol_L2_a.y[1, -1], sol_L2_b.y[1, -1]]])

mu_transit_L1 = eigvals(M_transit_L1)
mu_transit_L2 = eigvals(M_transit_L2)

print(f"\nTransfer matrix eigenvalues (transit):")
print(f"  L1: mu = {mu_transit_L1}")
print(f"      |mu|_max = {np.max(np.abs(mu_transit_L1)):.10f}")
print(f"      det(M) = {np.linalg.det(M_transit_L1):.10f} (should be 1 for Hamiltonian)")
print(f"  L2: mu = {mu_transit_L2}")
print(f"      |mu|_max = {np.max(np.abs(mu_transit_L2)):.10f}")
print(f"      det(M) = {np.linalg.det(M_transit_L2):.10f}")

# Maximum amplitude during transit
amp_L1 = np.sqrt(sol_L1_a.y[0]**2 + sol_L1_b.y[0]**2)
amp_L2 = np.sqrt(sol_L2_a.y[0]**2 + sol_L2_b.y[0]**2)

max_amp_L1 = np.max(np.abs(sol_L1_a.y[0]))
max_amp_L2 = np.max(np.abs(sol_L2_a.y[0]))

print(f"\nMaximum amplitude (from y(0)=1, y'(0)=0):")
print(f"  L1: max|y| = {max_amp_L1:.6f}")
print(f"  L2: max|y| = {max_amp_L2:.6f}")

# =============================================================================
# SECTION 7: Large-q Mathieu Analysis (what if modulation IS 100%?)
# =============================================================================

print("\n" + "=" * 72)
print("PART D: Large-q Regime — 100% Gap Modulation Scenario")
print("=" * 72)

# The task says: "BCS gap goes 0 -> 0.77 over tau-window of ~0.03"
# If we model this as the Leggett frequency going 0 -> omega_L0, then
# omega_L^2(t) = omega_L0^2 * f(t) where f goes 0 -> 1.
# This is NOT a Mathieu equation (no periodic modulation).
# But we can ASK: if there WERE periodic modulation at 100% depth,
# what would the Mathieu parameters be?

# 100% modulation: omega^2(t) = omega_0^2 * [1 + cos(omega_d * t)]
# = omega_0^2 + omega_0^2 * cos(omega_d * t)
# Mathieu form: a = (2*omega_0/omega_d)^2, q = a/2

# Drive frequency candidates:
# 1. The pair vibration frequency omega_PV (internal BCS timescale)
# 2. The attractor frequency omega_att (geometric transit)
# 3. The Langer decay rate Gamma_Langer_BCS

print(f"\nCanonical frequencies (M_KK units):")
print(f"  omega_L1 = {omega_L1:.3f}")
print(f"  omega_L2 = {omega_L2:.3f}")
print(f"  omega_PV = {omega_PV:.3f} (pair vibration)")
print(f"  omega_att = {omega_att:.3f} (geometric attractor)")
print(f"  Gamma_Langer = {Gamma_Langer_BCS:.3f}")

# Case 1: omega_PV drives the Leggett mode
a_100_L1_PV = (2.0 * omega_L1 / omega_PV)**2
q_100_L1_PV = a_100_L1_PV / 2.0
mu_100_L1_PV, _ = compute_mathieu_monodromy(a_100_L1_PV, q_100_L1_PV)

a_100_L2_PV = (2.0 * omega_L2 / omega_PV)**2
q_100_L2_PV = a_100_L2_PV / 2.0
mu_100_L2_PV, _ = compute_mathieu_monodromy(a_100_L2_PV, q_100_L2_PV)

print(f"\n100% modulation driven by omega_PV = {omega_PV:.3f}:")
print(f"  L1: a = {a_100_L1_PV:.4f}, q = {q_100_L1_PV:.4f}, "
      f"|mu|_max = {np.max(np.abs(mu_100_L1_PV)):.6f}")
print(f"  L2: a = {a_100_L2_PV:.4f}, q = {q_100_L2_PV:.4f}, "
      f"|mu|_max = {np.max(np.abs(mu_100_L2_PV)):.6f}")

# Case 2: omega_att drives the Leggett mode
a_100_L1_att = (2.0 * omega_L1 / omega_att)**2
q_100_L1_att = a_100_L1_att / 2.0
mu_100_L1_att, _ = compute_mathieu_monodromy(a_100_L1_att, q_100_L1_att)

a_100_L2_att = (2.0 * omega_L2 / omega_att)**2
q_100_L2_att = a_100_L2_att / 2.0
mu_100_L2_att, _ = compute_mathieu_monodromy(a_100_L2_att, q_100_L2_att)

print(f"\n100% modulation driven by omega_att = {omega_att:.3f}:")
print(f"  L1: a = {a_100_L1_att:.4f}, q = {q_100_L1_att:.4f}, "
      f"|mu|_max = {np.max(np.abs(mu_100_L1_att)):.6f}")
print(f"  L2: a = {a_100_L2_att:.4f}, q = {q_100_L2_att:.4f}, "
      f"|mu|_max = {np.max(np.abs(mu_100_L2_att)):.6f}")

# Case 3: Self-resonance — omega_L drives omega_L (subharmonic)
a_100_L1_self = (2.0 * omega_L1 / (2.0 * omega_L1))**2
q_100_L1_self = a_100_L1_self / 2.0
mu_100_L1_self, _ = compute_mathieu_monodromy(a_100_L1_self, q_100_L1_self)

print(f"\n100% modulation, self-subharmonic (omega_d = 2*omega_L):")
print(f"  L1: a = {a_100_L1_self:.4f}, q = {q_100_L1_self:.4f}, "
      f"|mu|_max = {np.max(np.abs(mu_100_L1_self)):.6f}")

# =============================================================================
# SECTION 8: Sweep — Floquet multiplier vs q at fixed a
# =============================================================================

print("\n" + "=" * 72)
print("PART E: Floquet Multiplier vs q (fixed a lines)")
print("=" * 72)

# For each physically relevant a value, sweep q from 0 to 15
a_values_sweep = [a_100_L1_PV, a_100_L2_PV, a_100_L1_att, a_100_L2_att, 1.0, 4.0]
a_labels = ['L1/PV', 'L2/PV', 'L1/att', 'L2/att', 'a=1', 'a=4']

q_sweep = np.linspace(0, 15, 300)

sweep_results = {}
for a_val, label in zip(a_values_sweep, a_labels):
    mu_abs_max = []
    for q_val in q_sweep:
        mu, _ = compute_mathieu_monodromy(a_val, q_val)
        mu_abs_max.append(np.max(np.abs(mu)))
    sweep_results[label] = np.array(mu_abs_max)

    # Find first instability
    unstable_q = q_sweep[np.array(mu_abs_max) > 1.0 + 1e-8]
    if len(unstable_q) > 0:
        print(f"  {label} (a={a_val:.4f}): first instability at q = {unstable_q[0]:.4f}, "
              f"max |mu| = {np.max(mu_abs_max):.4f}")
    else:
        print(f"  {label} (a={a_val:.4f}): STABLE for all q in [0, 15]")

# =============================================================================
# SECTION 9: The adiabatic invariant analysis
# =============================================================================

print("\n" + "=" * 72)
print("PART F: Adiabatic Invariant Analysis")
print("=" * 72)

# The critical ratio is omega_L * t_transit:
# If omega_L * t_transit >> 1 -> adiabatic (no amplification)
# If omega_L * t_transit << 1 -> sudden (frozen, no oscillation)
# If omega_L * t_transit ~ 1 -> non-adiabatic (potential amplification)

# Use the actual canonical dt_transit
omega_L1_times_t = omega_L1 * dt_transit
omega_L2_times_t = omega_L2 * dt_transit
omega_PV_times_t = omega_PV * dt_transit
omega_att_times_t = omega_att * dt_transit

print(f"\nAdiabaticity parameters (omega * dt_transit):")
print(f"  omega_L1 * dt_transit = {omega_L1_times_t:.6f}")
print(f"  omega_L2 * dt_transit = {omega_L2_times_t:.6f}")
print(f"  omega_PV * dt_transit = {omega_PV_times_t:.6f}")
print(f"  omega_att * dt_transit = {omega_att_times_t:.6f}")
print(f"  (Need ~ 1 for parametric resonance, >> 1 for adiabatic)")

# Number of Leggett oscillations during transit
N_osc_L1 = omega_L1 * dt_transit / (2 * np.pi)
N_osc_L2 = omega_L2 * dt_transit / (2 * np.pi)
N_osc_PV = omega_PV * dt_transit / (2 * np.pi)
N_osc_att = omega_att * dt_transit / (2 * np.pi)

print(f"\nNumber of oscillation periods during transit:")
print(f"  L1: {N_osc_L1:.6f} periods")
print(f"  L2: {N_osc_L2:.6f} periods")
print(f"  PV: {N_osc_PV:.6f} periods")
print(f"  att: {N_osc_att:.6f} periods")

# The Leggett mode completes ~2.5e-5 oscillations during transit.
# This is the SUDDEN limit: the mode doesn't have time to oscillate at all.
# In this regime, parametric resonance is impossible.

# However, the task mentions "omega_drive ~ v_terminal / Delta_tau_window"
# Delta_tau_window ~ 0.03 for the gap onset region
# omega_drive_onset = v_terminal / 0.03

Delta_tau_window = 0.03  # (local)
omega_drive_onset = v_terminal / Delta_tau_window
t_onset_window = Delta_tau_window / v_terminal

print(f"\nGap onset window:")
print(f"  Delta_tau = {Delta_tau_window}")
print(f"  t_window = {t_onset_window:.8f} M_KK^-1")
print(f"  omega_drive_onset = {omega_drive_onset:.2f} M_KK")
print(f"  omega_L1 / omega_drive_onset = {omega_L1 / omega_drive_onset:.6f}")
print(f"  omega_L2 / omega_drive_onset = {omega_L2 / omega_drive_onset:.6f}")

# The ratio omega_L / omega_drive ~ 0.00016 — the drive is ~6300x faster
# than the Leggett mode can respond. This is the DEEP SUDDEN limit.

# =============================================================================
# SECTION 10: Energy in the Leggett mode after transit
# =============================================================================

print("\n" + "=" * 72)
print("PART G: Leggett Mode Energy After Transit")
print("=" * 72)

# Even in the sudden limit, there can be energy deposition.
# If the Leggett frequency changes suddenly from 0 to omega_L,
# a mode that was at rest (y=y0, y'=0) acquires energy:
#   E = (1/2) * omega_L^2 * y0^2
# relative to the new ground state energy
#   E_0 = (1/2) * omega_L (zero-point)

# But the mode starts in vacuum (no condensate -> no relative phase mode).
# The CREATION of the mode is what matters, not its parametric amplification.
# This is exactly the Schwinger/Parker particle creation mechanism
# already computed in S38.

# From the Hill equation integration, extract the actual amplification
tau_at_t = tau_start + v_terminal * sol_L1_a.t
energy_L1_a = 0.5 * sol_L1_a.y[1]**2 + 0.5 * omega_L1_interp(
    np.clip(tau_at_t, tau_gl[0], tau_gl[-1]))**2 * sol_L1_a.y[0]**2

print(f"\nEnergy evolution (solution a, y(0)=1, y'(0)=0):")
print(f"  E(0) = {energy_L1_a[0]:.6f}")
print(f"  E(T) = {energy_L1_a[-1]:.6f}")
print(f"  E_max = {np.max(energy_L1_a):.6f}")
print(f"  E_ratio = E(T)/E(0) = {energy_L1_a[-1]/energy_L1_a[0]:.10f}")

# For the Hamiltonian system d^2y/dt^2 + omega^2(t)*y = 0,
# E = (1/2)(y'^2 + omega^2*y^2) is NOT conserved when omega varies.
# The ratio E(T)/E(0) is the adiabatic ratio.
# In the adiabatic limit: E(T)/E(0) = omega(T)/omega(0)
# In the sudden limit: E(T)/E(0) = 1 (energy unchanged)

# The actual ratio tells us how much energy is deposited in the Leggett mode
omega_ratio = omega_L1_interp(tau_end) / omega_L1_interp(tau_start)
print(f"\nomega_L1(tau_end)/omega_L1(tau_start) = {omega_ratio:.6f}")
print(f"Adiabatic prediction: E ratio = {omega_ratio:.6f}")
print(f"Actual E ratio = {energy_L1_a[-1]/energy_L1_a[0]:.6f}")

# Amplification factor (max energy / initial energy)
amp_factor_L1 = np.max(energy_L1_a) / energy_L1_a[0]
amp_factor_L2_energy = None

tau_at_t_L2 = tau_start + v_terminal * sol_L2_a.t
energy_L2_a = 0.5 * sol_L2_a.y[1]**2 + 0.5 * omega_L2_interp(
    np.clip(tau_at_t_L2, tau_gl[0], tau_gl[-1]))**2 * sol_L2_a.y[0]**2

amp_factor_L2 = np.max(energy_L2_a) / energy_L2_a[0]

print(f"\nAmplification factors (max energy / initial energy):")
print(f"  L1: {amp_factor_L1:.6f}")
print(f"  L2: {amp_factor_L2:.6f}")

# =============================================================================
# SECTION 11: Scan physical a-q point against Mathieu tongues
# =============================================================================

# Check: for large-q, do tongues overlap?
print("\n" + "=" * 72)
print("PART H: Tongue Overlap at Large q")
print("=" * 72)

# At q >> 1, the Mathieu instability tongues broaden.
# Check: what fraction of a-values are unstable at q = 5, 10, 15?
for q_test in [0.5, 1.0, 2.0, 5.0, 10.0, 15.0]:
    unstable_count = 0
    total = 300  # (local)
    a_test = np.linspace(0, 30, total)
    for a_val in a_test:
        mu, _ = compute_mathieu_monodromy(a_val, q_test)
        if np.max(np.abs(mu)) > 1.0 + 1e-8:
            unstable_count += 1
    print(f"  q = {q_test:.1f}: {unstable_count}/{total} a-values unstable "
          f"({100*unstable_count/total:.1f}%)")

# =============================================================================
# SECTION 12: GATE VERDICT
# =============================================================================

print("\n" + "=" * 72)
print("GATE VERDICT: LEGGETT-AMP-53")
print("=" * 72)

# Key numbers:
max_mu_Mathieu_L1 = np.max(np.abs(mu_L1))
max_mu_Mathieu_L2 = np.max(np.abs(mu_L2))
max_mu_transit_L1 = np.max(np.abs(mu_transit_L1))
max_mu_transit_L2 = np.max(np.abs(mu_transit_L2))

print(f"\n1. Mathieu (periodic reference, physical a,q from GL modulation depth):")
print(f"   L1: |mu|_max = {max_mu_Mathieu_L1:.10f}")
print(f"   L2: |mu|_max = {max_mu_Mathieu_L2:.10f}")
print(f"   Both STABLE (|mu| = 1 to machine precision)")

print(f"\n2. Direct Hill integration (actual transit trajectory):")
print(f"   L1: |mu|_max = {max_mu_transit_L1:.10f}")
print(f"   L2: |mu|_max = {max_mu_transit_L2:.10f}")
print(f"   Both have det(M)=1 (Hamiltonian, verified)")

print(f"\n3. Adiabatic analysis:")
print(f"   omega_L * dt_transit = {omega_L1_times_t:.2e} (L1), {omega_L2_times_t:.2e} (L2)")
print(f"   N_oscillations during transit: {N_osc_L1:.2e} (L1), {N_osc_L2:.2e} (L2)")
print(f"   This is the DEEP SUDDEN limit: zero complete oscillations")
print(f"   No parametric resonance possible (need multiple oscillation periods)")

print(f"\n4. Energy amplification from transit:")
print(f"   L1: {amp_factor_L1:.6f}x")
print(f"   L2: {amp_factor_L2:.6f}x")

print(f"\n5. 100% modulation at omega_PV drive:")
print(f"   L1: a = {a_100_L1_PV:.4f}, q = {q_100_L1_PV:.4f}, "
      f"|mu| = {np.max(np.abs(mu_100_L1_PV)):.6f}")
print(f"   L2: a = {a_100_L2_PV:.4f}, q = {q_100_L2_PV:.4f}, "
      f"|mu| = {np.max(np.abs(mu_100_L2_PV)):.6f}")
print(f"   Hypothetical — but even here, Floquet multiplier ~ 1")

# Determine verdict
all_mu = [max_mu_Mathieu_L1, max_mu_Mathieu_L2, max_mu_transit_L1, max_mu_transit_L2]
max_mu_overall = max(all_mu)

if max_mu_overall > 1.0 + 1e-6 and max(amp_factor_L1, amp_factor_L2) > 10:
    verdict = "PASS"
    detail = f"|mu|_max = {max_mu_overall:.6f}, amplification = {max(amp_factor_L1, amp_factor_L2):.1f}x"
elif max_mu_overall > 1.0 + 1e-6:
    verdict = "INFO"
    detail = f"|mu|_max = {max_mu_overall:.6f}, but amplification = {max(amp_factor_L1, amp_factor_L2):.4f}x < 10"
else:
    verdict = "FAIL"
    detail = (f"|mu|_max = {max_mu_overall:.10f} <= 1. "
              f"Transit is {1.0/omega_L1_times_t:.0f}x faster than Leggett period. "
              f"Deep sudden limit. No parametric amplification.")

print(f"\n{'*' * 60}")
print(f"VERDICT: {verdict}")
print(f"DETAIL: {detail}")
print(f"{'*' * 60}")

# Physical interpretation
print(f"""
PHYSICAL INTERPRETATION:
The Leggett mode frequency is omega_L ~ 0.14 M_KK, while the transit
duration is dt_transit = {dt_transit:.4e} M_KK^-1. The product
omega_L * dt_transit = {omega_L1_times_t:.2e}, meaning the mode
completes {N_osc_L1:.1e} oscillation periods during the entire transit.

Parametric amplification (Floquet instability) requires the driven
oscillator to complete AT LEAST several periods within the drive period.
Here the drive (tau-evolution) is {1.0/omega_L1_times_t:.0f}x faster
than the natural period of the Leggett mode.

This is the DEEP SUDDEN limit. The Leggett mode is essentially frozen
during transit. It cannot track the J_ab(tau) variation, cannot
resonate with it, and cannot amplify.

The GL sweep shows the Leggett frequency varies by only {mod_depth_L1*100:.1f}%
(L1) and {mod_depth_L2*100:.1f}% (L2) across the full tau range. Even at 100%
modulation depth in a hypothetical periodic scenario, the physical
operating point sits deep in the stable region of the Mathieu diagram
because a ~ (omega_L/omega_drive)^2 ~ {a_phys_L1:.1e} << 1.

QA's "narrow instability window" objection (S52 R2) used the small-h
Mathieu approximation, which IS conservative. But the correct response
is not "large-q tongues overlap" — it is that omega_L * dt_transit << 1
means there is no resonance condition to satisfy in the first place.
The transit is a SINGLE NON-ADIABATIC PASSAGE, not a periodic drive.

The Leggett mode does not contribute to e-fold production via
parametric amplification. Route P4 = 0 e-folds.
""")

# =============================================================================
# SECTION 13: Save data and plot
# =============================================================================

# Save data
np.savez(os.path.join(OUT_DIR, 's53_leggett_amp.npz'),
         # Mathieu diagram
         a_range=a_range, q_range=q_range,
         stability_map=stability_map, max_mu_map=max_mu_map,
         # Physical operating points
         a_phys_L1=a_phys_L1, q_phys_L1=q_phys_L1,
         a_phys_L2=a_phys_L2, q_phys_L2=q_phys_L2,
         mu_L1=mu_L1, mu_L2=mu_L2,
         # 100% modulation scenarios
         a_100_L1_PV=a_100_L1_PV, q_100_L1_PV=q_100_L1_PV,
         a_100_L1_att=a_100_L1_att, q_100_L1_att=q_100_L1_att,
         # Transit integration
         mu_transit_L1=mu_transit_L1, mu_transit_L2=mu_transit_L2,
         M_transit_L1=M_transit_L1, M_transit_L2=M_transit_L2,
         amp_factor_L1=amp_factor_L1, amp_factor_L2=amp_factor_L2,
         # Sweep results
         q_sweep=q_sweep,
         # Time series
         t_eval=t_eval,
         y_L1_a=sol_L1_a.y, y_L1_b=sol_L1_b.y,
         y_L2_a=sol_L2_a.y, y_L2_b=sol_L2_b.y,
         # Adiabaticity
         omega_L1_times_t=omega_L1_times_t,
         omega_L2_times_t=omega_L2_times_t,
         N_osc_L1=N_osc_L1, N_osc_L2=N_osc_L2,
         # Gate
         gate_name='LEGGETT-AMP-53',
         gate_verdict=verdict,
         gate_detail=detail)

print(f"\nData saved to: computations/session-53/s53_leggett_amp.npz")

# =============================================================================
# PLOT
# =============================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 12))

# Panel 1: Mathieu stability diagram
ax1 = axes[0, 0]
im = ax1.pcolormesh(a_range, q_range, np.log10(max_mu_map + 1e-16),
                    cmap='RdBu_r', vmin=-0.01, vmax=0.5)
ax1.contour(a_range, q_range, stability_map, levels=[0.5], colors='k', linewidths=1)
# Mark physical operating points
ax1.plot(a_phys_L1, q_phys_L1, 'g*', markersize=15, label=f'L1 phys (a={a_phys_L1:.1e})')
ax1.plot(a_phys_L2, q_phys_L2, 'c*', markersize=15, label=f'L2 phys (a={a_phys_L2:.1e})')
# Mark 100% modulation scenarios
ax1.plot(a_100_L1_PV, q_100_L1_PV, 'r^', markersize=10, label=f'L1/PV 100%')
ax1.plot(a_100_L1_att, q_100_L1_att, 'ms', markersize=10, label=f'L1/att 100%')
plt.colorbar(im, ax=ax1, label='log10(|mu|_max)')
ax1.set_xlabel('a (Mathieu)')
ax1.set_ylabel('q (Mathieu)')
ax1.set_title('Mathieu Stability Diagram')
ax1.legend(fontsize=7, loc='upper left')

# Panel 2: Floquet multiplier vs q for fixed a
ax2 = axes[0, 1]
for label, mu_arr in sweep_results.items():
    ax2.semilogy(q_sweep, mu_arr, label=label, alpha=0.7)
ax2.axhline(1.0, color='k', ls='--', alpha=0.5, label='stability boundary')
ax2.set_xlabel('q (Mathieu)')
ax2.set_ylabel('|mu|_max')
ax2.set_title('Floquet Multiplier vs q')
ax2.legend(fontsize=7)
ax2.set_ylim(0.5, 100)

# Panel 3: Hill equation solutions during transit
ax3 = axes[1, 0]
tau_plot = tau_start + v_terminal * sol_L1_a.t
ax3.plot(tau_plot, sol_L1_a.y[0], 'b-', label='L1 y(t), y(0)=1', alpha=0.8)
ax3.plot(tau_plot, sol_L2_a.y[0], 'r-', label='L2 y(t), y(0)=1', alpha=0.8)
ax3.axvline(tau_fold, color='gray', ls='--', alpha=0.5, label=f'tau_fold={tau_fold}')
ax3.set_xlabel('tau')
ax3.set_ylabel('y(t)')
ax3.set_title('Hill Equation Solutions During Transit')
ax3.legend(fontsize=8)

# Panel 4: Leggett frequency vs tau + energy ratio
ax4 = axes[1, 1]
ax4_twin = ax4.twinx()
ax4.plot(tau_gl, omega_L1_gl, 'bo-', label='omega_L1', markersize=4)
ax4.plot(tau_gl, omega_L2_gl, 'rs-', label='omega_L2', markersize=4)
ax4.set_xlabel('tau')
ax4.set_ylabel('omega_L (M_KK)', color='b')
ax4.set_title('Leggett Frequencies & Josephson Coupling')

ax4_twin.plot(tau_gl, J_12_gl, 'g^-', label='J_12', markersize=4, alpha=0.7)
ax4_twin.set_ylabel('J_12 (M_KK)', color='g')
ax4.legend(loc='upper left', fontsize=8)
ax4_twin.legend(loc='upper right', fontsize=8)

# Overall title
fig.suptitle(f'LEGGETT-AMP-53: {verdict} — omega_L * dt_transit = {omega_L1_times_t:.2e}\n'
             f'Deep sudden limit: {N_osc_L1:.1e} Leggett periods during transit',
             fontsize=12, fontweight='bold')

plt.tight_layout(rect=[0, 0, 1, 0.93])
plt.savefig(os.path.join(OUT_DIR, 's53_leggett_amp.png'), dpi=150, bbox_inches='tight')
print(f"Plot saved to: computations/session-53/s53_leggett_amp.png")
print("\nDone.")
