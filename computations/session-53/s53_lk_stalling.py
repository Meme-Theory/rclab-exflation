#!/usr/bin/env python3
"""
s53_lk_stalling.py — Landau-Khalatnikov Critical Slowing Modifier (Route P6)
==============================================================================

Gate: LK-STALLING-53 (INFO)
Agent: landau-condensed-matter-theorist

Physics:
--------
Near a BCS phase transition, the order parameter (gap Delta) has a characteristic
relaxation time that diverges at a critical/spinodal point. This Landau-Khalatnikov
(LK) critical slowing stretches the effective dwell time at the fold, amplifying
e-fold contributions from other routes (P1-P5).

The BCS transition on SU(3) is WEAKLY first-order:
  - barrier_0d = 0.0047 M_KK (0.6% of gap energy)
  - S_inst = 0.069 (quantum critical point)
  - Classified as sd-shell / ^24Mg nuclear analog

For a weakly first-order transition, the relevant critical slowing occurs at the
SPINODAL point tau_sp where the metastable minimum vanishes (curvature -> 0).
Between the first-order line and the spinodal, the order parameter relaxation time
grows as:
    tau_LK = tau_0 / |d^2 F / d(Delta)^2|

At the spinodal, d^2F/d(Delta)^2 = 0 and tau_LK diverges.

Classification: Model A dynamics (non-conserved order parameter).
  - z = 2 (diffusive relaxation, TDGL)
  - nu = 1/2 (mean-field BCS)
  - Product nu*z = 1

The key competition is Kibble-Zurek: when the transit velocity is finite, the system
cannot actually reach the divergent slowing. Freeze-out occurs at the KZ scale.

References:
  - Landau & Khalatnikov, Dokl. Akad. Nauk SSSR 96, 469 (1954)
  - Hohenberg & Halperin, Rev. Mod. Phys. 49, 435 (1977)  [Model A: z=2]
  - Ko et al., Nature Physics 15, 1227 (2019)  [KZ in BCS-BEC]
  - Zurek, Nature 317, 505 (1985)  [Kibble-Zurek mechanism]
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from canonical_constants import (
    tau_fold, v_terminal, dt_transit, omega_att,
    barrier_0d, S_inst, a_GL, b_GL, Delta_0_GL,
    xi_BCS, xi_GL, E_cond, Gamma_Langer_BCS,
    omega_PV, L_over_xi, M_KK, c_Gold
)

# ======================================================================
#  SECTION 1: Dynamic universality classification
# ======================================================================

print("=" * 72)
print("LK-STALLING-53: Landau-Khalatnikov Critical Slowing Modifier")
print("=" * 72)

# The BCS gap Delta is the order parameter.
# Delta is NOT a conserved quantity => Model A dynamics
# Model A: z = 2 (TDGL relaxation), nu = 1/2 (mean-field)
z_dyn = 2       # dynamic critical exponent, Model A
nu_mf = 0.5     # correlation length exponent, mean-field BCS
nuz = nu_mf * z_dyn  # product = 1

print("\n--- Section 1: Dynamic Universality Classification ---")
print(f"Order parameter: BCS gap Delta (complex scalar, non-conserved)")
print(f"Dynamic universality class: Model A (Hohenberg-Halperin)")
print(f"Justification: Delta is NOT conserved (particles pair/unpair freely)")
print(f"  z = {z_dyn}  (diffusive/relaxational)")
print(f"  nu = {nu_mf}  (mean-field BCS)")
print(f"  nu*z = {nuz}  (governs tau_LK divergence exponent)")
print(f"")
print(f"Note: Model B (z=4) would apply if particle number N were the order")
print(f"parameter, but N is conserved by a DIFFERENT mechanism. The pairing")
print(f"gap Delta fluctuates freely => Model A is correct.")

# ======================================================================
#  SECTION 2: Microscopic relaxation time
# ======================================================================

print("\n--- Section 2: Microscopic Relaxation Time ---")

# tau_0 = microscopic relaxation time
# Natural choice: 1/omega_att (the attractor frequency, geometric)
# omega_att = 1.430 M_KK, so tau_0 = 1/1.430 = 0.699 M_KK^{-1}
tau_0_att = 1.0 / omega_att
print(f"omega_att = {omega_att:.3f} M_KK  (fully geometric, S38)")
print(f"tau_0 = 1/omega_att = {tau_0_att:.4f} M_KK^{{-1}}")

# Alternative: 1/omega_PV (pair vibration frequency)
tau_0_pv = 1.0 / omega_PV
print(f"omega_PV = {omega_PV:.4f} M_KK  (pair vibration, S37)")
print(f"tau_0_PV = 1/omega_PV = {tau_0_pv:.4f} M_KK^{{-1}}")

# Alternative: Langer decay rate
tau_0_langer = 1.0 / Gamma_Langer_BCS
print(f"Gamma_Langer = {Gamma_Langer_BCS:.4f} M_KK  (Langer decay, S38)")
print(f"tau_0_Langer = 1/Gamma_Langer = {tau_0_langer:.4f} M_KK^{{-1}}")

# Use omega_att as the canonical microscopic time (geometric, no free parameters)
tau_0 = tau_0_att
print(f"\nCanonical choice: tau_0 = {tau_0:.4f} M_KK^{{-1}} (from omega_att)")

# ======================================================================
#  SECTION 3: GL free energy structure and spinodal analysis
# ======================================================================

print("\n--- Section 3: GL Free Energy & Spinodal ---")

# The GL free energy is:
#   F(Delta) = a_GL * |Delta|^2 + b_GL * |Delta|^4
# At the fold (tau_fold = 0.19):
#   a_GL = -0.5245  (negative => ordered phase)
#   b_GL = 0.4418   (positive => stabilizing)
#
# Equilibrium: Delta_eq^2 = -a_GL / (2*b_GL)
Delta_eq_sq = -a_GL / (2 * b_GL)
Delta_eq = np.sqrt(Delta_eq_sq)
print(f"a_GL = {a_GL:.4f} M_KK^2")
print(f"b_GL = {b_GL:.4f} M_KK^0")
print(f"Delta_eq = sqrt(-a/(2b)) = {Delta_eq:.4f} M_KK")
print(f"Delta_0_GL (canonical) = {Delta_0_GL:.4f} M_KK")
print(f"Consistency: Delta_eq/Delta_0_GL = {Delta_eq/Delta_0_GL:.4f}")

# The curvature of F at the equilibrium:
# d^2F/d(Delta)^2 |_{Delta_eq} = 2*a_GL + 12*b_GL*Delta_eq^2
#                                = 2*a_GL + 12*b_GL*(-a_GL/(2*b_GL))
#                                = 2*a_GL - 6*a_GL = -4*a_GL
curvature_eq = -4 * a_GL
print(f"d^2F/d(Delta^2) at equilibrium = -4*a_GL = {curvature_eq:.4f} M_KK^2")

# For a weakly first-order transition, as tau increases through the fold,
# a_GL passes through zero (from negative to positive) at the spinodal.
# The transition to the disordered phase occurs when a_GL changes sign.
#
# Near the spinodal tau_sp: a_GL(tau) ~ a'*(tau - tau_sp)
# The curvature d^2F/d(Delta)^2 = 2*a_GL(tau) (at Delta=0 in the disordered phase)
# tau_LK = tau_0 / |2*a_GL(tau)| = tau_0 / |2*a'*(tau - tau_sp)|

# Estimate a' = da_GL/dtau from the barrier height
# barrier_0d = a_GL^2 / (4*b_GL)  (GL barrier for 0D, standard result)
barrier_computed = a_GL**2 / (4 * b_GL)
print(f"\nBarrier height (GL): a^2/(4b) = {barrier_computed:.6f} M_KK")
print(f"barrier_0d (canonical) = {barrier_0d:.6f} M_KK")
print(f"Ratio = {barrier_computed/barrier_0d:.3f}")
# Note: barrier_0d from canonical was computed differently; use the GL formula

# The spinodal occurs at the tau where a_GL(tau) = 0.
# At tau_fold = 0.19, a_GL = -0.5245 (ordered).
# The transit takes the system from ordered to disordered.
# We need da_GL/dtau. From the spectral action structure:
# a_GL ~ (tau - tau_sp) near the spinodal. Estimate tau_sp from the data.

# The transit window extends from tau ~ 0.0 to tau ~ 0.285.
# At tau_fold = 0.19, the system is near the maximum pairing region.
# The spinodal is at tau_sp where the BCS solution ceases to exist.
# From S38: the transit completes at tau ~ 0.285 (DNP instability at tau < 0.285, S22a)
# For our purposes, estimate the width of the pairing region.

# Key: the "transition" is NOT at tau_fold but as tau sweeps THROUGH the fold.
# The system is driven at v_terminal through the fold region.

# ======================================================================
#  SECTION 4: LK relaxation time vs transit time
# ======================================================================

print("\n--- Section 4: tau_LK vs tau_transit ---")

print(f"Transit duration: dt_transit = {dt_transit:.6f} M_KK^{{-1}}")
print(f"Transit velocity: v_terminal = {v_terminal:.4f} M_KK")

# The LK relaxation time in the ordered phase (near equilibrium):
# tau_LK = tau_0 / curvature_eq  (at the minimum)
# where curvature_eq = -4*a_GL = 2.098 at the fold
tau_LK_eq = tau_0 / curvature_eq
print(f"\ntau_LK at equilibrium (fold): tau_0/(-4*a_GL) = {tau_LK_eq:.6f} M_KK^{{-1}}")
print(f"Ratio tau_transit / tau_LK_eq = {dt_transit / tau_LK_eq:.4f}")

# Near the spinodal (where curvature -> 0):
# tau_LK(delta_tau) = tau_0 / (2*|a'|*delta_tau)
# where delta_tau = |tau - tau_sp|

# How rapidly does a_GL change with tau?
# a_GL ~ linear in (tau - tau_sp) near spinodal. We need the slope.
# From the GL parameters: a_GL(tau_fold) = -0.5245, and the fold region
# spans roughly Delta_tau_fold ~ 0.1 (from ~0.14 to ~0.24 based on S35).
# So |da_GL/dtau| ~ 0.5245 / 0.1 ~ 5.25

# More precise: the curvature at the fold is -4*a_GL = 2.098.
# The system traverses tau at velocity v_terminal = 26.54.
# In time dt, it covers delta_tau = v_terminal * dt.
# The curvature changes at rate |d(curvature)/dt| ~ v_terminal * |d(curvature)/d(tau)|

# Use the GL structure: d^2F/d(Delta)^2 at Delta=0 is 2*a_GL(tau)
# At the spinodal, this is zero. Rate of change: 2*da_GL/dtau.
# Estimate: da_GL/dtau ~ a_GL(fold) / delta_tau_fold
delta_tau_fold = 0.10  # NOTE: local estimate of pairing region width, not a canonical constant  # (local)
da_GL_dtau = abs(a_GL) / delta_tau_fold  # ~ 5.245 M_KK^2 per unit tau
print(f"\nEstimated |da_GL/dtau| = {da_GL_dtau:.3f} M_KK^2 (per unit tau)")

# The curvature at distance delta_tau from the spinodal:
# curvature(delta_tau) = 2 * da_GL_dtau * delta_tau
# tau_LK(delta_tau) = tau_0 / (2 * da_GL_dtau * delta_tau)
# = tau_0 / (2 * 5.245 * delta_tau)
# = 0.699 / (10.49 * delta_tau)
# = 0.0667 / delta_tau

coeff_lk = tau_0 / (2 * da_GL_dtau)
print(f"tau_LK(delta_tau) = {coeff_lk:.6f} / delta_tau  (M_KK^{{-1}})")

# ======================================================================
#  SECTION 5: Kibble-Zurek freeze-out analysis
# ======================================================================

print("\n--- Section 5: Kibble-Zurek Freeze-Out ---")

# The Kibble-Zurek freeze-out occurs when the relaxation time equals
# the time remaining before the system reaches the critical/spinodal point.
#
# Freeze-out condition: tau_LK(t*) = |t*|
# where t* is the time before reaching the spinodal.
#
# In our parameterization with tau as the control variable:
# delta_tau = v_terminal * t_remaining
# So t_remaining = delta_tau / v_terminal
#
# Freeze-out: tau_LK(delta_tau*) = delta_tau* / v_terminal
# => tau_0 / (2 * da_GL_dtau * delta_tau*) = delta_tau* / v_terminal
# => delta_tau*^2 = tau_0 * v_terminal / (2 * da_GL_dtau)
# => delta_tau* = sqrt(tau_0 * v_terminal / (2 * da_GL_dtau))

delta_tau_star = np.sqrt(tau_0 * v_terminal / (2 * da_GL_dtau))
print(f"KZ freeze-out scale: delta_tau* = {delta_tau_star:.6f}")

# The freeze-out time:
t_freeze = delta_tau_star / v_terminal
print(f"Freeze-out time: t* = delta_tau*/v_terminal = {t_freeze:.6f} M_KK^{{-1}}")

# The LK relaxation time at freeze-out:
tau_LK_freeze = coeff_lk / delta_tau_star
print(f"tau_LK at freeze-out: {tau_LK_freeze:.6f} M_KK^{{-1}}")
print(f"Consistency check: tau_LK_freeze / t_freeze = {tau_LK_freeze/t_freeze:.4f} (should be 1.0)")

# The frozen correlation length at freeze-out:
xi_freeze = xi_GL * (delta_tau_star / delta_tau_fold)**(-nu_mf)
# More precisely: xi(delta_tau) = xi_0 * |delta_tau|^{-nu}
# where xi_0 ~ xi_GL * delta_tau_fold^{nu} at the fold
xi_0_est = xi_GL * delta_tau_fold**nu_mf
xi_freeze_v2 = xi_0_est * delta_tau_star**(-nu_mf)
print(f"\nFrozen correlation length: xi_freeze ~ {xi_freeze_v2:.4f} M_KK^{{-1}}")
print(f"(using xi_0 = xi_GL * delta_tau_fold^nu = {xi_0_est:.4f})")

# ======================================================================
#  SECTION 6: Transit through the fold — effective velocity reduction
# ======================================================================

print("\n--- Section 6: Effective Velocity Reduction ---")

# The critical slowing does NOT actually slow the GEOMETRIC transit
# (that is driven by the spectral action gradient, not by Delta).
# What it DOES is slow the ORDER PARAMETER RESPONSE.
#
# This is the inverted Born-Oppenheimer regime (IBO, S38):
# geometry (tau) evolves FAST, pairing (Delta) responds SLOWLY.
# The IBO ratio is already 1118:1 (S52).
#
# The effect of LK stalling is to EXTEND the period during which
# the condensate exists (because Delta cannot relax to zero as fast
# as tau moves through the spinodal). This extends the window for:
# - acoustic metric contribution (P1)
# - GPE effects (P2)
# - Leggett mode amplification (P4)

# Define the "stalling window": the region where tau_LK > dt_transit
# tau_LK(delta_tau) > dt_transit
# => tau_0 / (2 * da_GL_dtau * delta_tau) > dt_transit
# => delta_tau < tau_0 / (2 * da_GL_dtau * dt_transit)
delta_tau_stall = tau_0 / (2 * da_GL_dtau * dt_transit)
print(f"Stalling window: |delta_tau| < {delta_tau_stall:.4f}")
print(f"  (region where tau_LK > dt_transit)")

# Time spent in stalling window (free passage):
t_free = 2 * delta_tau_stall / v_terminal
print(f"Free passage time through stalling window: {t_free:.6f} M_KK^{{-1}}")

# The actual time spent in this window, accounting for LK slowing:
# The velocity of the geometric modulus tau is NOT reduced by LK slowing.
# LK slowing affects the ORDER PARAMETER, not the drive.
# The GEOMETRIC velocity remains v_terminal.
#
# HOWEVER, the condensate persists beyond the spinodal because Delta
# cannot relax to zero fast enough. The condensate "overshoots" by
# a time ~ tau_LK(delta_tau*) = t_freeze.
#
# This gives an effective dwell time extension:
t_overshoot = tau_LK_freeze  # condensate persists this long after spinodal
print(f"\nCondensate overshoot time: {t_overshoot:.6f} M_KK^{{-1}}")
print(f"dt_transit = {dt_transit:.6f} M_KK^{{-1}}")
amplification_factor_overshoot = (dt_transit + t_overshoot) / dt_transit
print(f"Dwell time amplification (overshoot): {amplification_factor_overshoot:.4f}")

# ======================================================================
#  SECTION 7: Proper amplification from TDGL integral
# ======================================================================

print("\n--- Section 7: TDGL Integral — Proper Amplification ---")

# The question is: how much does the order parameter Delta persist
# after the geometric modulus has passed the fold?
#
# The TDGL equation: d(Delta)/dt = -(1/tau_0) * dF/d(Delta)
#
# As tau sweeps through the spinodal at velocity v_terminal, the
# effective curvature changes sign. The order parameter must then
# relax from Delta_eq to 0, but with rate ~ 1/tau_LK which is slow
# near the spinodal.
#
# The key timescale comparison:
# - Geometric sweep rate through the fold: v_terminal = 26.54 M_KK
# - Order parameter relaxation rate: Gamma_LK = 1/tau_LK
#
# The adiabatic condition (OP tracks geometry) requires:
# Gamma_LK >> |d(ln Delta_eq)/dt|
# => 1/tau_LK >> (1/Delta_eq) * |dDelta_eq/dtau| * v_terminal
#
# Estimate |dDelta_eq/dtau| from GL:
# Delta_eq(tau) = sqrt(-a(tau) / (2*b))
# dDelta_eq/dtau = (1/(2*Delta_eq)) * (-da/dtau) / (2*b)
#                = -da/(dtau * 4*b*Delta_eq)
dDelta_dtau = da_GL_dtau / (4 * b_GL * Delta_eq)
drive_rate = dDelta_dtau * v_terminal / Delta_eq  # |d(ln Delta)/dt|
print(f"|d(Delta_eq)/dtau| = {dDelta_dtau:.4f} M_KK per unit tau")
print(f"|d(ln Delta_eq)/dt| = v_terminal * |dDelta_dtau| / Delta_eq = {drive_rate:.4f} M_KK")

# Adiabatic parameter: epsilon = drive_rate * tau_LK
# At the fold: epsilon_fold = drive_rate * tau_LK_eq
epsilon_fold = drive_rate * tau_LK_eq
print(f"\nAdiabaticity parameter at fold:")
print(f"  epsilon = drive_rate * tau_LK_eq = {epsilon_fold:.6f}")
print(f"  epsilon << 1 means adiabatic (OP tracks geometry)")
print(f"  epsilon >> 1 means non-adiabatic (OP frozen, KZ regime)")

if epsilon_fold < 1:
    print(f"  => ADIABATIC at the fold center")
else:
    print(f"  => NON-ADIABATIC at the fold center")

# At the spinodal (delta_tau -> 0): epsilon -> infinity (always non-adiabatic)
# The KZ freeze-out gives the transition between regimes.

# ======================================================================
#  SECTION 8: Comprehensive amplification factor
# ======================================================================

print("\n--- Section 8: Amplification Factor ---")

# The amplification factor quantifies how much longer the condensate
# effectively exists compared to the naive geometric transit time.
#
# Two contributions:
# A) The condensate persists beyond the geometric spinodal by ~ tau_LK_freeze
# B) Before the spinodal, the OP responds sluggishly, effectively
#    averaging over a wider window of the geometry.
#
# HOWEVER, the crucial physical point is that the BCS transition on SU(3)
# is FIRST-ORDER with barrier_0d = 0.0047. For a first-order transition,
# the system does NOT pass through a divergent-xi critical point.
# Instead, it tunnels (or thermally activates) across the barrier.
#
# The "critical slowing" at a first-order transition is:
# tau_nucleation ~ tau_0 * exp(barrier / T_eff)
# where T_eff is the effective temperature (= compound temperature from quench).

print("CRITICAL DISTINCTION: First-order vs. second-order transition")
print(f"  barrier_0d = {barrier_0d:.6f} M_KK")
print(f"  S_inst = {S_inst:.6f} (quantum critical point regime)")
print(f"  barrier_0d / omega_PV = {barrier_0d/omega_PV:.4f}")
print(f"  (barrier is 0.6% of one pair vibration quantum)")

# The barrier is so small (0.6% of the oscillation quantum) that the
# transition is effectively CONTINUOUS for dynamical purposes.
# This validates treating it with LK critical slowing rather than
# Arrhenius nucleation kinetics.

print(f"\nSince barrier_0d << omega_PV, the transition is 'weakly first-order'")
print(f"and the LK critical slowing analysis is applicable.")

# Now compute the proper amplification.
# The condensate e-fold window has two parts:
# 1. The geometric transit through the pairing region (dt_transit)
# 2. The overshoot due to LK slowing (tau_LK_freeze)

# But there is a THIRD effect: during the transit, the condensate
# density |Delta|^2 is not at its equilibrium value — it lags behind.
# This REDUCES the instantaneous pairing relative to equilibrium.
#
# Net amplification is the ratio of the time-integrated condensate
# density to the adiabatic (instantaneous equilibrium) value.

# Compute the integral of |Delta(t)|^2 through the transit:
# In the adiabatic limit: int |Delta_eq(tau(t))|^2 dt
# In the KZ limit: the condensate freezes at Delta_freeze and persists

# Numerical integration of the TDGL response
# d(Delta)/dt = -(1/tau_0) * (2*a(tau(t)) * Delta + 4*b*Delta^3)
# tau(t) = tau_fold + v_terminal * t (linear sweep)
# a(tau) = a_GL + da_GL_dtau * (tau - tau_fold)

print("\n--- Numerical TDGL integration ---")
N_steps = 100000  # (local)
t_span = 0.02  # M_KK^{-1}, wide enough to capture the full transit + overshoot  # (local)
dt_num = t_span / N_steps
t_arr = np.linspace(-t_span/2, t_span/2, N_steps)

# Initial condition: at t = -t_span/2, the system is in the ordered phase
# far from the spinodal, so Delta ~ Delta_eq
Delta_tdgl = np.zeros(N_steps)
Delta_eq_arr = np.zeros(N_steps)

# The spinodal is where a(tau) = 0.
# a(tau) = a_GL + da_GL_dtau * (tau - tau_fold) (but note a_GL is negative at the fold)
# Set t=0 at the spinodal crossing:
# a(tau_sp) = 0 => tau_sp = tau_fold + |a_GL|/da_GL_dtau
tau_sp = tau_fold + abs(a_GL) / da_GL_dtau
print(f"Spinodal: tau_sp = {tau_sp:.4f}")

# Redefine: t=0 is when the system reaches the spinodal
# tau(t) = tau_sp + v_terminal * t (so tau < tau_sp for t < 0, ordered phase)
# a(tau(t)) = da_GL_dtau * v_terminal * t  (= 0 at t=0, negative for t<0)

# TDGL: dDelta/dt = -(1/tau_0) * (2*a(t)*Delta + 4*b*Delta^3)
#      where a(t) = -da_GL_dtau * v_terminal * t  [negative for t>0 => disordered]
# Wait: if tau increases and a_GL goes from negative (ordered) to positive (disordered),
# then a(t) = da_GL_dtau * v_terminal * t (positive when t > 0 => disordered)
# Actually a = a_GL(tau_fold) + da_dtau * (tau - tau_fold)
# = -|a_GL| + da_dtau * v_terminal * (t - t_fold_arrival)
# We need to be careful with signs.

# Let's define: a(t) = a_slope * t where a_slope = da_GL_dtau * v_terminal
# At t < 0: a(t) < 0 (ordered, condensate exists)
# At t = 0: a(t) = 0 (spinodal)
# At t > 0: a(t) > 0 (disordered, condensate decays)
a_slope = da_GL_dtau * v_terminal  # M_KK^2 per M_KK^{-1} time unit
print(f"a(t) = a_slope * t,  a_slope = {a_slope:.4f} M_KK^3")

# Initial condition at t_start = -t_span/2:
t_start = -t_span / 2
a_start = a_slope * t_start  # should be large and negative => deep in ordered phase
Delta_eq_start = np.sqrt(max(0, -a_start / (2 * b_GL)))
Delta_tdgl[0] = Delta_eq_start

for i in range(N_steps - 1):
    t = t_arr[i]
    a_t = a_slope * t
    Delta_i = Delta_tdgl[i]

    # Equilibrium value at this a(t)
    if a_t < 0:
        Delta_eq_arr[i] = np.sqrt(-a_t / (2 * b_GL))
    else:
        Delta_eq_arr[i] = 0.0

    # TDGL: dDelta/dt = -(1/tau_0) * dF/dDelta
    # F = a*Delta^2 + b*Delta^4
    # dF/dDelta = 2*a*Delta + 4*b*Delta^3
    dFdDelta = 2 * a_t * Delta_i + 4 * b_GL * Delta_i**3
    dDelta_dt = -(1.0 / tau_0) * dFdDelta

    # Forward Euler with clipping (Delta >= 0 since it's an amplitude)
    Delta_tdgl[i + 1] = max(0.0, Delta_i + dDelta_dt * dt_num)

# Fill last equilibrium value
a_last = a_slope * t_arr[-1]
Delta_eq_arr[-1] = np.sqrt(max(0, -a_last / (2 * b_GL))) if a_last < 0 else 0.0

# Compute time-integrated condensate density
integral_tdgl = np.trapezoid(Delta_tdgl**2, t_arr)
integral_adiabatic = np.trapezoid(Delta_eq_arr**2, t_arr)

print(f"\nTime-integrated condensate density:")
print(f"  TDGL (with LK slowing): {integral_tdgl:.6f}")
print(f"  Adiabatic (instant equilibrium): {integral_adiabatic:.6f}")

if integral_adiabatic > 0:
    amplification_tdgl = integral_tdgl / integral_adiabatic
    print(f"  Amplification factor (TDGL/adiabatic): {amplification_tdgl:.4f}")
else:
    amplification_tdgl = float('inf')
    print(f"  Adiabatic integral is zero (system enters from ordered phase)")

# Time at which TDGL Delta drops below 1% of initial
threshold = 0.01 * Delta_tdgl[0]  # (local)
tdgl_decay_idx = np.argmax(Delta_tdgl < threshold)
if tdgl_decay_idx > 0:
    t_decay_tdgl = t_arr[tdgl_decay_idx]
else:
    t_decay_tdgl = t_arr[-1]

# Compare with equilibrium decay (instantaneous)
eq_decay_idx = np.argmax(Delta_eq_arr < threshold)
if eq_decay_idx > 0 and eq_decay_idx < N_steps - 1:
    t_decay_eq = t_arr[eq_decay_idx]
else:
    t_decay_eq = 0.0  # equilibrium drops to 0 at spinodal  # (local)

print(f"\nDecay time (Delta drops to 1% of initial):")
print(f"  TDGL: t_decay = {t_decay_tdgl:.6f} M_KK^{{-1}}")
print(f"  Equilibrium: t_decay = {t_decay_eq:.6f} M_KK^{{-1}} (at spinodal)")
overshoot_time = t_decay_tdgl - t_decay_eq
print(f"  Overshoot: {overshoot_time:.6f} M_KK^{{-1}}")
print(f"  Overshoot / dt_transit = {overshoot_time/dt_transit:.4f}")

# ======================================================================
#  SECTION 9: First-order transition correction
# ======================================================================

print("\n--- Section 9: First-Order Transition Correction ---")

# For a weakly first-order transition, the GL potential has a cubic term
# (or the effective barrier from S_inst). The system can nucleate before
# reaching the spinodal, cutting off the critical slowing.
#
# Nucleation rate: Gamma_nuc ~ omega_att * exp(-S_inst / S_thermal)
# where S_thermal is the thermal action.
#
# In the quantum regime (S_inst = 0.069 << 1), tunneling is 93% (S37).
# The nucleation timescale is:
tau_nucleation = (1.0 / omega_att) * np.exp(S_inst)
print(f"Nucleation timescale: tau_nuc = (1/omega_att)*exp(S_inst)")
print(f"  = {tau_nucleation:.6f} M_KK^{{-1}}")
print(f"  tau_nuc / dt_transit = {tau_nucleation/dt_transit:.4f}")

# Since S_inst = 0.069 is tiny, exp(S_inst) = 1.071.
# The nucleation time is barely different from tau_0!
# This means the first-order nature does NOT significantly modify
# the LK analysis — the barrier is effectively transparent.
print(f"\nexp(S_inst) = {np.exp(S_inst):.4f}  (barrier nearly transparent)")
print(f"Conclusion: First-order correction is negligible (7.1% increase in tau_0)")

# ======================================================================
#  SECTION 10: Physical interpretation — the actual modifier
# ======================================================================

print("\n--- Section 10: Physical Interpretation & Modifier ---")

# The LK stalling effect has TWO components:
#
# COMPONENT A: Condensate persistence overshoot
# After the geometric modulus passes the spinodal, Delta persists for
# an additional time ~ tau_LK_freeze. This extends the window for
# acoustic metric effects, GPE backreaction, Leggett modes, etc.
#
# COMPONENT B: Adiabaticity failure
# The condensate cannot track the rapidly changing equilibrium,
# so |Delta(t)|^2 is an average over the pre-spinodal region
# rather than the local equilibrium value. This typically INCREASES
# the time-averaged condensate density (since the frozen value is
# the pre-freeze equilibrium, which is larger than the shrinking
# equilibrium near the spinodal).

# The effective modification to P1-P5:
# Each route contributes N_e ~ f(Delta, rho, c_s, ...) * dt_eff
# The LK modifier changes dt_eff from dt_transit to dt_eff_stalled

# dt_eff_stalled = dt_transit + overshoot_time (from TDGL)
dt_eff_stalled = dt_transit + abs(overshoot_time)
amplification_final = dt_eff_stalled / dt_transit

print(f"dt_transit = {dt_transit:.6f} M_KK^{{-1}}")
print(f"dt_eff_stalled = {dt_eff_stalled:.6f} M_KK^{{-1}}")
print(f"Amplification factor = {amplification_final:.4f}")

print(f"\n{'='*72}")
print(f"SUMMARY: LK-STALLING-53 RESULTS")
print(f"{'='*72}")
print(f"")
print(f"1. Dynamic universality: Model A, z=2, nu=1/2, nu*z=1")
print(f"2. Microscopic relaxation: tau_0 = {tau_0:.4f} M_KK^{{-1}} (from omega_att)")
print(f"3. KZ freeze-out scale: delta_tau* = {delta_tau_star:.6f}")
print(f"4. KZ freeze-out time: t* = {t_freeze:.6f} M_KK^{{-1}}")
print(f"5. tau_LK at freeze-out: {tau_LK_freeze:.6f} M_KK^{{-1}}")
print(f"6. tau_transit / tau_LK_eq = {dt_transit/tau_LK_eq:.4f}")
print(f"   (transit is {dt_transit/tau_LK_eq:.1f}x the equilibrium relaxation time)")
print(f"7. TDGL overshoot time: {abs(overshoot_time):.6f} M_KK^{{-1}}")
print(f"8. TDGL amplification factor: {amplification_tdgl:.4f}")
print(f"9. First-order correction: exp(S_inst)={np.exp(S_inst):.4f} (negligible)")
print(f"10. Effective amplification: {amplification_final:.4f}")
print(f"")
print(f"GATE VERDICT: LK-STALLING-53 = INFO")
print(f"  tau_transit/tau_LK_eq = {dt_transit/tau_LK_eq:.4f}")
print(f"  Amplification factor = {amplification_final:.4f}")
print(f"")

# Physical assessment
print(f"PHYSICAL ASSESSMENT:")
print(f"  The adiabaticity parameter epsilon = {epsilon_fold:.2f} >> 1 confirms that")
print(f"  the condensate is DEEPLY NON-ADIABATIC throughout the transit.")
print(f"  The OP CANNOT track the rapidly evolving geometry (IBO regime).")
print(f"")
print(f"  The KZ freeze-out scale delta_tau* = {delta_tau_star:.4f} exceeds the")
print(f"  pairing region width (~0.10), meaning freeze-out occurs OUTSIDE")
print(f"  the physical tau range. The condensate is frozen at its initial")
print(f"  value from the start of the transit and only decays AFTER the")
print(f"  geometric drive ceases (or the curvature becomes large enough).")
print(f"")
print(f"  The TDGL integration gives the definitive answer: the condensate")
print(f"  persists {abs(overshoot_time)/dt_transit:.1f}x longer than the geometric transit.")
print(f"  Time-integrated condensate density is {amplification_tdgl:.2f}x the adiabatic value.")
print(f"")
print(f"  The effective amplification factor = {amplification_final:.2f}x applies as a")
print(f"  multiplier to ALL condensate-dependent routes (P1, P2, P4).")
print(f"")
print(f"  CRITICAL PHYSICAL INSIGHT: In the inverted Born-Oppenheimer")
print(f"  regime (IBO ratio = 1118, S52), the geometry is the fast variable")
print(f"  and the pairing is the slow variable. LK slowing is the MECHANISM")
print(f"  underlying IBO. This computation quantifies the overshoot beyond")
print(f"  the geometric transit window.")
print(f"")
print(f"  PHONONIC CLASSIFICATION: PARTICLE")
print(f"  (Modifies quasiparticle condensate lifetime near a phase boundary)")

# Save results
results = {
    'z_dyn': z_dyn,
    'nu_mf': nu_mf,
    'nuz': nuz,
    'tau_0': tau_0,
    'tau_LK_eq': tau_LK_eq,
    'tau_LK_freeze': tau_LK_freeze,
    'delta_tau_star': delta_tau_star,
    't_freeze': t_freeze,
    'dt_transit': dt_transit,
    'v_terminal': v_terminal,
    'amplification_factor': amplification_final,
    'amplification_tdgl': amplification_tdgl,
    'epsilon_fold': epsilon_fold,
    'overshoot_time': overshoot_time,
    'tau_nucleation': tau_nucleation,
    'da_GL_dtau': da_GL_dtau,
    'a_slope': a_slope,
    't_arr': t_arr,
    'Delta_tdgl': Delta_tdgl,
    'Delta_eq_arr': Delta_eq_arr,
}

np.savez(os.path.join(os.path.dirname(__file__), 's53_lk_stalling.npz'), **results)
print(f"\nData saved to s53_lk_stalling.npz")
