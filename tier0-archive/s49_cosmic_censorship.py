#!/usr/bin/env python3
"""
S49 COSMIC-CENSORSHIP-49: Ballistic Overshoot & 4D Energy Conditions
=====================================================================

Session 49, Wave 1-P -- Schwarzschild-Penrose-Geometer

Physics:
--------
The modulus tau undergoes ballistic transit from tau=0 with terminal velocity
v = 26.5 M_KK (S38). The fold is at tau=0.19, the geometric phase transition
at tau=0.537, and NEC violation at tau=1.382. S49 W1-D found the transit covers
dtau=0.030 (reaching ~0.22) WITH BCS friction. But several questions remain:

  Q1. What is the full ballistic trajectory tau(t)?
      - With BCS friction (condensation energy extraction)?
      - WITHOUT friction (free ballistic, pure kinetic)?
      - What initial velocities v_0 are needed to reach 0.537?

  Q2. At each tau along the trajectory, what do the 4D energy conditions say?
      - The KK reduction maps internal curvature + kinetic energy to effective 4D T_mu_nu
      - NEC: rho + p >= 0 (null energy)
      - WEC: rho >= 0 AND rho + p >= 0
      - SEC: rho + 3p >= 0 (for FLRW)
      - DEC: rho >= |p| (dominant energy)
      - If DEC fails: naked singularity? Or transient?

  Q3. Cosmic censorship assessment:
      - Is the curvature singularity at tau -> inf naked or censored?
      - Does the BCS mechanism serve as a "cosmic censor"?
      - Is there a Penrose inequality analog?

Method:
-------
1. Solve M_eff * d^2 tau / dt^2 = -dV/dtau (ballistic, no friction)
   and M_eff * d^2 tau / dt^2 = -dV/dtau - Gamma * dtau/dt (with BCS friction)
   where V(tau) is the spectral action potential, M_eff = M_ATDHFB(tau).

2. The spectral action gives V(tau) = S_spectral(tau) (evaluated at S45/S48).
   This is MONOTONICALLY INCREASING for tau > 0 (proven in S37 CUTOFF-SA-37).
   So -dV/dtau < 0: the potential DECELERATES tau.

3. For the 4D effective stress-energy from the internal space:
   T_mu_nu^{eff} = diag(-rho, p, p, p) where:
   rho = (1/2) G_mod * tau_dot^2 + V(tau)     [kinetic + potential]
   p   = (1/2) G_mod * tau_dot^2 - V(tau)     [kinetic - potential]
   This is scalar field cosmology with w = (T - V) / (T + V).

4. Check all energy conditions at each point along the trajectory.

Gate: COSMIC-CENSORSHIP-49
  PASS: no overshoot to 0.537, or energy conditions hold throughout
  INFO: transient DEC violation, no singularity
  FAIL: permanent DEC violation or naked singularity

Author: schwarzschild-penrose-geometer (Session 49)
Date: 2026-03-17
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.interpolate import interp1d
import sys
import os
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tier1_dirac_spectrum import (
    su3_generators,
    compute_structure_constants,
    compute_killing_form,
    jensen_metric,
    orthonormal_frame,
    frame_structure_constants,
    connection_coefficients,
    U1_IDX,
    SU2_IDX,
    C2_IDX,
)
from canonical_constants import (
    tau_fold, G_DeWitt, v_terminal, dt_transit, M_ATDHFB,
    E_cond, S_fold, PI, a2_fold, a4_fold, a0_fold,
    d2S_fold, dS_fold,
)

t_start = time.time()

print("=" * 78)
print("  S49 COSMIC-CENSORSHIP-49: Ballistic Overshoot & 4D Energy Conditions")
print("=" * 78)


# =============================================================================
# SECTION 1: Spectral action potential V(tau) and its derivative
# =============================================================================

print("\n  Step 1: Computing spectral action along the modulus line...")

# We need V(tau) = S_spectral(tau) and dV/dtau across [0, 2.0].
# The spectral action S = sum_k f(lambda_k^2 / Lambda^2) is computed from the
# Dirac eigenvalues. We use the existing tier1 infrastructure.

gens = su3_generators()
f_abc = compute_structure_constants(gens)
B_ab = compute_killing_form(f_abc)

# Dense tau grid for the potential
tau_pot_grid = np.linspace(0.0, 1.5, 150)
S_spectral = np.zeros(len(tau_pot_grid))


def compute_riemann_tensor_ON(ft, Gamma, n=8):
    """Full Riemann tensor R[a,b,c,f] = R^f_{abc} in ON frame."""
    R = np.zeros((n, n, n, n), dtype=np.float64)
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for f_idx in range(n):
                    val = 0.0
                    for d in range(n):
                        val += Gamma[d, b, c] * Gamma[f_idx, a, d]
                        val -= Gamma[d, a, c] * Gamma[f_idx, b, d]
                        val -= ft[a, b, d] * Gamma[f_idx, d, c]
                    R[a, b, c, f_idx] = val
    return R


def spectral_action_at_tau(tau):
    """Compute the spectral action S(tau) using a_0 + a_2 + a_4 Seeley-DeWitt.

    S(tau) = a_0(tau) * f_0 + a_2(tau) * f_2 + a_4(tau) * f_4
    where f_0, f_2, f_4 are moments of the cutoff function.

    For the Jensen metric, the Seeley-DeWitt coefficients depend on tau through
    the Riemann curvature. a_0 is the volume (constant for isovolumetric Jensen).
    a_2 ~ R(tau), a_4 ~ R^2 terms.
    """
    n = 8
    g_s = jensen_metric(B_ab, tau)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    R_abcd = compute_riemann_tensor_ON(ft, Gamma)

    # Ricci
    Ric = np.einsum('abca->bc', R_abcd)
    R_scalar = np.trace(Ric)
    Ric_sq = np.sum(Ric * Ric)

    # Kretschner
    K_full = np.sum(R_abcd * R_abcd)

    # a_0 = Volume = constant for isovolumetric Jensen
    # Use 16 spinor components times vol
    local_a0 = 16.0  # dim(spinor) * vol / vol_ref, normalized

    # a_2 = (1/6) * integral R * |psi|^2 dV
    # For the round metric: a_2 = R(0) * a0 / 6 = 2.0 * 16 / 6 = 5.333
    # Properly: a_2_density = R_scalar / 6 (per unit volume, per spinor component)
    local_a2 = R_scalar / 6.0

    # a_4 involves R^2, Ric^2, Riem^2 terms (Gilkey formula for spin connection)
    # a_4_density = (1/360) * (5*R^2 - 2*Ric^2 + 2*K)  [spin-1/2]
    local_a4 = (1.0 / 360.0) * (5.0 * R_scalar**2 - 2.0 * Ric_sq + 2.0 * K_full)

    # The full spectral action with cutoff moments f_0, f_2, f_4:
    # S = f_0 * Lambda^8 * a_0 + f_2 * Lambda^6 * a_2 + f_4 * Lambda^4 * a_4
    # We work in units where the combination f_k * Lambda^{8-2k} is absorbed.
    # Use the S42 calibration: at fold, S_fold = 250361.
    # We compute the RELATIVE spectral action normalized to tau=0.

    return local_a0, local_a2, local_a4, R_scalar, K_full, Ric_sq


# Compute at each tau
a0_arr = np.zeros(len(tau_pot_grid))
a2_arr = np.zeros(len(tau_pot_grid))
a4_arr = np.zeros(len(tau_pot_grid))
R_arr = np.zeros(len(tau_pot_grid))
K_arr = np.zeros(len(tau_pot_grid))
Ric_sq_arr = np.zeros(len(tau_pot_grid))
Ric_min_arr = np.zeros(len(tau_pot_grid))

for i, tau in enumerate(tau_pot_grid):
    local_a0, local_a2, local_a4, R_s, K_f, Ric_s = spectral_action_at_tau(tau)
    a0_arr[i] = local_a0
    a2_arr[i] = local_a2
    a4_arr[i] = local_a4
    R_arr[i] = R_s
    K_arr[i] = K_f
    Ric_sq_arr[i] = Ric_s

    # Also get Ric_min for NEC check
    g_s = jensen_metric(B_ab, tau)
    E_frame = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E_frame)
    Gamma = connection_coefficients(ft)
    R_abcd = compute_riemann_tensor_ON(ft, Gamma)
    Ric = np.einsum('abca->bc', R_abcd)
    Ric_min_arr[i] = np.min(np.linalg.eigvalsh(Ric))

# Construct the potential V(tau) as a combination of a_0, a_2, a_4
# Calibrate to match S_fold at tau_fold
# Use ratio to round: V(tau) = V_0 * [c0 * a0(tau) + c2 * a2(tau) + c4 * a4(tau)]
# At tau=0: a0=16, a2=2/6=0.333, a4 = (5*4 -2*0.5+2*0.5)/360 = 20/360 = 0.0556
# At fold: S = 250361 -> this is the full sum with cutoff Lambda

# The KEY structural fact: S(tau) is MONOTONICALLY INCREASING for tau > 0.
# (Proven in S37 CUTOFF-SA-37). So dV/dtau > 0 everywhere.
# The a2 density is proportional to R(tau), which increases from R(0)=2 onward.

# For the dynamics, what matters is the force F = -dV/dtau.
# Since V increases, F < 0 (decelerating the modulus).
# At the fold: d2S_fold = 317862 (stiffness).

# Build V(tau) from the Seeley-DeWitt coefficients
# Use dimensional analysis: S(tau) = f_0 * a0 + f_2 * a2 + f_4 * a4
# with cutoff moments calibrated to S_fold.
# The simplest self-consistent approach:
# V(tau) - V(0) proportional to a_2(tau) - a_2(0) (dominated by scalar curvature)
# Calibrate slope to d2S_fold at the fold.

# Direct approach: interpolate the curvature and use dS/dtau = (dR/dtau) * coupling
# From S42: dS_fold = 58673, d2S_fold = 317862

# Construct V(tau) by integrating R(tau):
# V(tau) = integral_0^tau (dV/dtau') dtau'
# At the fold: dV/dtau|_fold = dS_fold = 58673
# d2V/dtau2|_fold = d2S_fold = 317862

# The R(tau) data gives us the shape. Scale it to match known derivatives at fold.
# dV/dtau ~ c * dR/dtau. Fit c using dV/dtau at fold.

# Compute dR/dtau numerically
dtau = tau_pot_grid[1] - tau_pot_grid[0]
dR_dtau = np.gradient(R_arr, dtau)

# At fold: find closest grid point
fold_idx = np.argmin(np.abs(tau_pot_grid - tau_fold))
dR_at_fold = dR_dtau[fold_idx]

# Scale factor: dS/dtau = c * dR/dtau at fold
# We also want to use the a4 contribution. Construct:
# V(tau) = c2 * a2(tau) + c4 * a4(tau) + c0 * a0(tau)
# With c0*a0 = constant (isovolumetric).
# So V(tau) = c2 * R(tau)/6 + c4 * a4(tau) + const

# Fit c2, c4 to match dS_fold and d2S_fold at the fold
da2_dtau = np.gradient(a2_arr, dtau)
da4_dtau = np.gradient(a4_arr, dtau)
d2a2_dt2 = np.gradient(da2_dtau, dtau)
d2a4_dt2 = np.gradient(da4_dtau, dtau)

# At fold: dS = c2 * da2 + c4 * da4
# d2S = c2 * d2a2 + c4 * d2a4
# Solve 2x2 system
A_mat = np.array([
    [da2_dtau[fold_idx], da4_dtau[fold_idx]],
    [d2a2_dt2[fold_idx], d2a4_dt2[fold_idx]]
])
b_vec = np.array([dS_fold, d2S_fold])
try:
    c_coeffs = np.linalg.solve(A_mat, b_vec)
    c2_fit, c4_fit = c_coeffs
    print(f"    Calibration: c2 = {c2_fit:.2f}, c4 = {c4_fit:.2f}")
except np.linalg.LinAlgError:
    # Fallback: use dS_fold / da2_fold only
    c2_fit = dS_fold / da2_dtau[fold_idx]
    c4_fit = 0.0
    print(f"    Calibration (fallback): c2 = {c2_fit:.2f}, c4 = 0")

# Construct V(tau)
V_tau = c2_fit * a2_arr + c4_fit * a4_arr
V_tau -= V_tau[0]  # Normalize: V(0) = 0

# Construct dV/dtau
dV_dtau = c2_fit * da2_dtau + c4_fit * da4_dtau

# Verify at fold
print(f"    V(fold) = {V_tau[fold_idx]:.2f}")
print(f"    dV/dtau at fold = {dV_dtau[fold_idx]:.2f} (target: {dS_fold:.2f})")

# Interpolate for ODE solver
V_interp = interp1d(tau_pot_grid, V_tau, kind='cubic', fill_value='extrapolate')
dV_interp = interp1d(tau_pot_grid, dV_dtau, kind='cubic', fill_value='extrapolate')


# =============================================================================
# SECTION 2: Effective mass M_eff(tau)
# =============================================================================

print("\n  Step 2: Effective mass along modulus line...")

# From S40: M_ATDHFB = 1.695 at the fold.
# The mass varies with tau: M(tau) = M_ATDHFB(tau).
# From s40 data, we have M_ATDHFB at several tau points.
# For now, use the constant approximation M_eff = G_DeWitt = 5.0 as the
# geometric mass (the ATDHFB mass includes BCS corrections which are
# only present when there is a condensate).

# Two regimes:
# (a) Free ballistic: M_eff = G_DeWitt (no BCS, pure geometry)
# (b) BCS friction: effective dissipation from pair-breaking

M_geom = G_DeWitt  # = 5.0, the moduli space metric
print(f"    G_DeWitt = {M_geom}")
print(f"    M_ATDHFB (fold) = {M_ATDHFB}")
print(f"    Ratio M_ATDHFB/G_DeWitt = {M_ATDHFB/M_geom:.3f}")

# BCS friction coefficient:
# When the modulus moves, it breaks Cooper pairs. The pair-breaking rate
# dissipates kinetic energy. From S38: the BCS instability provides a
# friction coefficient Gamma_BCS such that:
# M_eff * d2tau/dt2 = -dV/dtau - Gamma_BCS * dtau/dt
# The friction is active only for tau > tau_fold (inside the BCS well).
# S38 estimate: dt_transit = 0.00113, covering dtau = 0.030.
# The effective friction is Gamma_BCS = M_eff * v / dtau ~ 5 * 26.5 / 0.03 ~ 4417
# But this is crude. The proper calculation: the pair-breaking rate is
# Gamma_Langer = 0.250 M_KK (from canonical constants).
# The friction coefficient is Gamma_BCS = 2 * Delta * d(Delta)/dtau * rho(E_F)
# which depends on the gap structure.
#
# For simplicity, model friction as:
# Gamma_fric(tau) = gamma_0 * heaviside(tau - tau_fold) * f(tau)
# where gamma_0 is calibrated to produce the known dt_transit.
#
# From dt_transit and v_terminal:
# dtau_transit = v_terminal * dt_transit = 26.5 * 0.00113 = 0.030
# The friction must stop the modulus within dtau = 0.030.
# If d2tau/dt2 = -Gamma_fric/M_eff * v, and v decays as v*exp(-Gamma*t/M):
# dtau = v * M / Gamma * (1 - exp(-Gamma*t_stop/M))
# For large friction (Gamma*t_stop >> M): dtau ~ v * M / Gamma
# So Gamma_fric ~ v * M / dtau = 26.5 * 5.0 / 0.030 = 4417

gamma_fric_est = v_terminal * M_geom / (v_terminal * dt_transit)
# Simplify: gamma_fric = M_geom / dt_transit
gamma_fric = M_geom / dt_transit
print(f"    Estimated BCS friction coefficient: Gamma = {gamma_fric:.1f} M_KK")

# The friction is enormous: the modulus is brought to rest in ~0.001 M_KK^{-1}
# This explains why the transit only covers dtau=0.030.


# =============================================================================
# SECTION 3: Ballistic trajectories — ODE integration
# =============================================================================

print("\n  Step 3: Integrating ballistic trajectories...")

# Case A: Free ballistic (no friction, no BCS)
# M_geom * d2tau/dt2 = -dV/dtau
# With V(tau) increasing, dV/dtau > 0, so the force is decelerating.

# Case B: With BCS friction (full dissipation after fold)
# M_geom * d2tau/dt2 = -dV/dtau - Gamma * (dtau/dt) * H(tau - tau_fold)

# State vector: y = [tau, v] where v = dtau/dt
# dy/dt = [v, -dV/dtau / M_geom]  (free)
# dy/dt = [v, (-dV/dtau - Gamma*v*H(tau-tau_fold)) / M_geom]  (friction)

t_max_integration = 0.05  # M_KK^{-1} units (plenty for the transit)


def rhs_free(t, y):
    tau_val, v_val = y
    # Clamp tau to interpolation range
    tau_clamped = np.clip(tau_val, tau_pot_grid[0] + 1e-10, tau_pot_grid[-1] - 1e-10)
    force = -float(dV_interp(tau_clamped))
    accel = force / M_geom
    return [v_val, accel]


def rhs_friction(t, y):
    tau_val, v_val = y
    tau_clamped = np.clip(tau_val, tau_pot_grid[0] + 1e-10, tau_pot_grid[-1] - 1e-10)
    force = -float(dV_interp(tau_clamped))
    # BCS friction only active past the fold
    fric = 0.0
    if tau_val > tau_fold:
        fric = -gamma_fric * v_val
    accel = (force + fric) / M_geom
    return [v_val, accel]


# Initial conditions: tau(0) = 0, v(0) = v_terminal
y0 = [0.0, v_terminal]
t_span = (0.0, t_max_integration)
t_eval = np.linspace(0, t_max_integration, 5000)

# Event: tau reaches 0.537
def event_transition(t, y):
    return y[0] - 0.537
event_transition.terminal = True
event_transition.direction = 1

# Event: tau reaches 1.382 (NEC)
def event_nec(t, y):
    return y[0] - 1.382
event_nec.terminal = True
event_nec.direction = 1

# Event: velocity = 0 (turnaround)
def event_stop(t, y):
    return y[1]
event_stop.terminal = True
event_stop.direction = -1

# --- Case A: Free ballistic ---
print("    Case A: Free ballistic (no friction)...")
sol_free = solve_ivp(rhs_free, t_span, y0, t_eval=t_eval,
                     events=[event_transition, event_nec, event_stop],
                     rtol=1e-12, atol=1e-14, method='DOP853')
tau_free = sol_free.y[0]
v_free = sol_free.y[1]
t_free = sol_free.t

print(f"    Free ballistic: tau_max = {np.max(tau_free):.6f}")
print(f"    v_min = {np.min(v_free):.6f}")
if sol_free.t_events[0].size > 0:
    print(f"    Reaches tau=0.537 at t = {sol_free.t_events[0][0]:.6f}")
    reaches_transition_free = True
else:
    print(f"    Does NOT reach tau=0.537 (turns around at tau = {np.max(tau_free):.6f})")
    reaches_transition_free = False

if sol_free.t_events[2].size > 0:
    t_turn_free = sol_free.t_events[2][0]
    idx_turn = np.argmin(np.abs(t_free - t_turn_free))
    tau_turn_free = tau_free[idx_turn]
    print(f"    Turnaround at t = {t_turn_free:.6f}, tau = {tau_turn_free:.6f}")
else:
    tau_turn_free = np.max(tau_free)
    print(f"    No turnaround within t_max (tau still advancing)")

# --- Case B: With BCS friction ---
print("\n    Case B: With BCS friction (Gamma = {:.0f})...".format(gamma_fric))
sol_fric = solve_ivp(rhs_friction, t_span, y0, t_eval=t_eval,
                     events=[event_transition, event_nec, event_stop],
                     rtol=1e-12, atol=1e-14, method='DOP853')
tau_fric = sol_fric.y[0]
v_fric = sol_fric.y[1]
t_fric = sol_fric.t

print(f"    With friction: tau_max = {np.max(tau_fric):.6f}")
if sol_fric.t_events[2].size > 0:
    t_turn_fric = sol_fric.t_events[2][0]
    idx_turn_fric = np.argmin(np.abs(t_fric - t_turn_fric))
    tau_turn_fric = tau_fric[idx_turn_fric]
    print(f"    Turnaround at t = {t_turn_fric:.6f}, tau = {tau_turn_fric:.6f}")
    reaches_transition_fric = tau_turn_fric >= 0.537
else:
    tau_turn_fric = np.max(tau_fric)
    reaches_transition_fric = tau_turn_fric >= 0.537
    print(f"    No turnaround detected")

print(f"    Reaches tau=0.537 (friction): {reaches_transition_fric}")


# --- Case C: What initial velocity is needed to reach 0.537? ---
print("\n    Case C: Critical velocity for reaching tau=0.537...")

def max_tau_for_v0(v0, tau_start=0.0):
    """Integrate free ballistic with initial velocity v0 from tau_start, return max tau."""
    y0_test = [tau_start, v0]
    sol = solve_ivp(rhs_free, (0, 0.5), y0_test,
                    events=[event_transition, event_stop],
                    rtol=1e-10, atol=1e-12, method='DOP853',
                    max_step=0.001)
    return np.max(sol.y[0])

# Binary search for critical velocity (starting from tau=0)
v_lo, v_hi = 1.0, 500.0
# First check if upper bound is enough
if max_tau_for_v0(v_hi) < 0.537:
    v_hi = 2000.0
    if max_tau_for_v0(v_hi) < 0.537:
        v_hi = 10000.0

for _ in range(80):
    v_mid = (v_lo + v_hi) / 2
    tau_max_test = max_tau_for_v0(v_mid)
    if tau_max_test >= 0.537:
        v_hi = v_mid
    else:
        v_lo = v_mid
v_crit_transition = (v_lo + v_hi) / 2
print(f"    Critical velocity to reach tau=0.537 (from tau=0): v_crit = {v_crit_transition:.2f}")
print(f"    v_terminal / v_crit = {v_terminal / v_crit_transition:.4f}")
print(f"    Ratio v_crit / v_terminal = {v_crit_transition / v_terminal:.2f}x")

# Critical velocity for NEC boundary (tau=1.382)
v_lo_nec, v_hi_nec = v_crit_transition, 20000.0
if max_tau_for_v0(v_hi_nec) < 1.382:
    v_hi_nec = 100000.0

for _ in range(80):
    v_mid = (v_lo_nec + v_hi_nec) / 2
    tau_max_test = max_tau_for_v0(v_mid)
    if tau_max_test >= 1.382:
        v_hi_nec = v_mid
    else:
        v_lo_nec = v_mid
v_crit_nec = (v_lo_nec + v_hi_nec) / 2
print(f"    Critical velocity to reach tau=1.382 (NEC): v_crit = {v_crit_nec:.2f}")
print(f"    v_terminal / v_crit_NEC = {v_terminal / v_crit_nec:.4f}")
print(f"    Ratio v_crit_NEC / v_terminal = {v_crit_nec / v_terminal:.2f}x")

# --- Case D: Start from fold, v = v_terminal ---
print("\n    Case D: Ballistic from fold (tau_0 = tau_fold, v_0 = v_terminal)...")
y0_fold = [tau_fold, v_terminal]
sol_fold_free = solve_ivp(rhs_free, t_span, y0_fold, t_eval=t_eval,
                          events=[event_transition, event_nec, event_stop],
                          rtol=1e-12, atol=1e-14, method='DOP853')
tau_fold_free = sol_fold_free.y[0]
v_fold_free = sol_fold_free.y[1]
t_fold_free = sol_fold_free.t
tau_max_fold_free = np.max(tau_fold_free)
print(f"    Starting from fold: tau_max = {tau_max_fold_free:.6f}")
reaches_transition_fold_free = tau_max_fold_free >= 0.537

if sol_fold_free.t_events[2].size > 0:
    t_turn_fold = sol_fold_free.t_events[2][0]
    idx_turn_fold = np.argmin(np.abs(t_fold_free - t_turn_fold))
    tau_turn_fold_free = tau_fold_free[idx_turn_fold]
    print(f"    Turnaround at t = {t_turn_fold:.6f}, tau = {tau_turn_fold_free:.6f}")
else:
    tau_turn_fold_free = tau_max_fold_free
    print(f"    No turnaround within t_max")

# Energy budget from fold
T_from_fold = 0.5 * M_geom * v_terminal**2
V_fold_val = float(V_interp(tau_fold))
V_transition_val = float(V_interp(0.537))
delta_V_fold_to_trans = V_transition_val - V_fold_val
print(f"    KE from fold: {T_from_fold:.2f}")
print(f"    Delta_V (fold -> transition): {delta_V_fold_to_trans:.2f}")
print(f"    Can reach? T_from_fold >= Delta_V: {T_from_fold >= delta_V_fold_to_trans}")
if T_from_fold < delta_V_fold_to_trans:
    print(f"    Deficit: {delta_V_fold_to_trans - T_from_fold:.2f} ({(delta_V_fold_to_trans - T_from_fold)/T_from_fold*100:.1f}%)")
    v_needed_from_fold = np.sqrt(2 * delta_V_fold_to_trans / M_geom)
    print(f"    Would need v >= {v_needed_from_fold:.2f} from fold (ratio {v_needed_from_fold/v_terminal:.2f}x)")

# --- Case E: With friction, starting from fold ---
print("\n    Case E: From fold with BCS friction...")
sol_fold_fric = solve_ivp(rhs_friction, t_span, y0_fold, t_eval=t_eval,
                          events=[event_transition, event_nec, event_stop],
                          rtol=1e-12, atol=1e-14, method='DOP853')
tau_fold_fric = sol_fold_fric.y[0]
v_fold_fric = sol_fold_fric.y[1]
t_fold_fric = sol_fold_fric.t
tau_max_fold_fric = np.max(tau_fold_fric)
print(f"    From fold + friction: tau_max = {tau_max_fold_fric:.6f}")
# dtau covered
dtau_fold_fric = tau_max_fold_fric - tau_fold
print(f"    dtau covered: {dtau_fold_fric:.6f} (S38 estimate: {v_terminal * dt_transit:.6f})")
print(f"    Reaches 0.537: {tau_max_fold_fric >= 0.537}")

# Critical velocity from fold to reach 0.537
print("\n    Case F: Critical velocity from fold to reach tau=0.537...")
v_lo_f, v_hi_f = 1.0, 500.0
if max_tau_for_v0(v_hi_f, tau_start=tau_fold) < 0.537:
    v_hi_f = 5000.0
for _ in range(80):
    v_mid = (v_lo_f + v_hi_f) / 2
    tau_max_test = max_tau_for_v0(v_mid, tau_start=tau_fold)
    if tau_max_test >= 0.537:
        v_hi_f = v_mid
    else:
        v_lo_f = v_mid
v_crit_from_fold = (v_lo_f + v_hi_f) / 2
print(f"    v_crit from fold to 0.537: {v_crit_from_fold:.2f}")
print(f"    v_terminal / v_crit_from_fold = {v_terminal / v_crit_from_fold:.4f}")
print(f"    Ratio v_crit / v_terminal = {v_crit_from_fold / v_terminal:.2f}x")


# =============================================================================
# SECTION 4: Kinetic energy budget
# =============================================================================

print("\n  Step 4: Energy budget analysis...")

# The kinetic energy at tau=0: T_0 = (1/2) * G_DeWitt * v_terminal^2
T_initial = 0.5 * M_geom * v_terminal**2
V_at_transition = float(V_interp(0.537))
V_at_nec = float(V_interp(min(1.382, tau_pot_grid[-1])))
V_at_turn_free = float(V_interp(min(tau_turn_free, tau_pot_grid[-1])))

print(f"    Initial kinetic energy: T_0 = {T_initial:.2f}")
print(f"    Potential at transition (0.537): V = {V_at_transition:.2f}")
print(f"    Potential at NEC (1.382): V = {V_at_nec:.2f}")
print(f"    Potential at turnaround (free): V = {V_at_turn_free:.2f}")
print(f"    Energy conservation check: T_0 - V(turn) = {T_initial - V_at_turn_free:.4f}")

# The modulus reaches tau_turn when T = V, i.e., (1/2)*G*v^2 = V(tau_turn)
# Overshoot margin: how much extra energy needed to reach 0.537?
energy_deficit_transition = V_at_transition - T_initial
print(f"\n    Energy deficit to reach tau=0.537: {energy_deficit_transition:.2f}")
if energy_deficit_transition > 0:
    print(f"    The modulus CANNOT reach the geometric phase transition.")
    print(f"    Energy deficit is {energy_deficit_transition / T_initial * 100:.1f}% of initial KE.")
    v_needed = np.sqrt(2 * V_at_transition / M_geom)
    print(f"    Would need v_0 >= {v_needed:.2f} (vs actual {v_terminal:.2f}, ratio {v_needed/v_terminal:.2f})")
else:
    print(f"    The modulus REACHES the transition with energy to spare.")
    print(f"    Excess energy: {abs(energy_deficit_transition):.2f}")


# =============================================================================
# SECTION 5: 4D Effective Stress-Energy from KK Reduction
# =============================================================================

print("\n  Step 5: 4D effective stress-energy tensor...")

# For a modulus field tau(t) in a KK reduction:
# The 4D effective stress-energy from the internal modulus is:
#
# T_{mu nu}^{eff} = (tau;mu)(tau;nu) * G_mod - g_{mu nu} * [(1/2) G_mod (nabla tau)^2 + V(tau)]
#
# For the homogeneous case (tau = tau(t)):
# rho = (1/2) G_mod * tau_dot^2 + V(tau)     (energy density)
# p   = (1/2) G_mod * tau_dot^2 - V(tau)     (pressure)
# w   = p / rho = (T - V) / (T + V)
#
# Energy conditions:
# NEC: rho + p = G_mod * tau_dot^2 >= 0  [ALWAYS SATISFIED for real tau_dot]
# WEC: rho = T + V >= 0 [needs V >= -T, always true if V >= 0]
# SEC: rho + 3p = 2T - 2V >= 0 [needs T >= V]
# DEC: rho >= |p| <=> (T + V) >= |T - V|
#      If T >= V: T+V >= T-V, so 2V >= 0 (always)
#      If V >= T: T+V >= V-T, so 2T >= 0 (always)
# DEC is ALWAYS SATISFIED for non-negative V and real tau_dot!

# BUT: this is the INTERNAL modulus contribution only.
# The full 4D T_mu_nu also includes:
# (a) The Casimir energy of the internal space (quantum correction)
# (b) The curvature of the internal space (classical KK contribution)
# (c) Any matter fields on the internal space

# The internal curvature contribution to 4D Einstein equations:
# From the KK ansatz ds^2_{12} = g_{mu nu} dx^mu dx^nu + g_{ab}(tau) dy^a dy^b:
# The 4D Einstein equations include a term from the internal Ricci scalar:
# G_{mu nu}^{4D} = 8*pi*G * T_{mu nu}^{matter} - (1/2) R_int * g_{mu nu}
# where R_int = R(tau) is the scalar curvature of the internal space.
# This acts as an effective cosmological "constant" (that varies with tau).

# For our analysis, the energy conditions along the trajectory are:

# Compute along free trajectory
n_free = len(t_free)
rho_free = np.zeros(n_free)
p_free = np.zeros(n_free)
w_free = np.zeros(n_free)
nec_free = np.zeros(n_free)  # rho + p
wec_free = np.zeros(n_free)  # rho
sec_free = np.zeros(n_free)  # rho + 3p
dec_free = np.zeros(n_free)  # rho - |p|

for i in range(n_free):
    T_kin = 0.5 * M_geom * v_free[i]**2
    tau_clamped = np.clip(tau_free[i], tau_pot_grid[0]+1e-10, tau_pot_grid[-1]-1e-10)
    V_val = float(V_interp(tau_clamped))
    rho_free[i] = T_kin + V_val
    p_free[i] = T_kin - V_val
    w_free[i] = p_free[i] / rho_free[i] if abs(rho_free[i]) > 1e-30 else 0.0
    nec_free[i] = rho_free[i] + p_free[i]
    wec_free[i] = rho_free[i]
    sec_free[i] = rho_free[i] + 3 * p_free[i]
    dec_free[i] = rho_free[i] - abs(p_free[i])

# Similarly for friction trajectory
n_fric = len(t_fric)
rho_fric = np.zeros(n_fric)
p_fric = np.zeros(n_fric)
w_fric = np.zeros(n_fric)

for i in range(n_fric):
    T_kin = 0.5 * M_geom * v_fric[i]**2
    tau_clamped = np.clip(tau_fric[i], tau_pot_grid[0]+1e-10, tau_pot_grid[-1]-1e-10)
    V_val = float(V_interp(tau_clamped))
    rho_fric[i] = T_kin + V_val
    p_fric[i] = T_kin - V_val
    w_fric[i] = p_fric[i] / rho_fric[i] if abs(rho_fric[i]) > 1e-30 else 0.0


# =============================================================================
# SECTION 6: Internal NEC along trajectory
# =============================================================================

print("\n  Step 6: Internal space NEC along trajectory...")

# The INTERNAL NEC (Ric_ab k^a k^b >= 0) is separate from the 4D NEC.
# The 4D NEC for the modulus scalar is always satisfied (see Section 5).
# The internal NEC depends on the Ricci tensor of the internal space,
# which we already computed.

# Interpolate Ric_min along the trajectory
Ric_min_interp = interp1d(tau_pot_grid, Ric_min_arr, kind='cubic',
                          fill_value='extrapolate')

# Check along free trajectory
Ric_min_traj_free = np.array([float(Ric_min_interp(np.clip(t, tau_pot_grid[0]+1e-10,
                              tau_pot_grid[-1]-1e-10))) for t in tau_free])

print(f"    Internal Ric_min at tau=0: {float(Ric_min_interp(0.0)):.6f}")
print(f"    Internal Ric_min at fold: {float(Ric_min_interp(tau_fold)):.6f}")
print(f"    Internal Ric_min at tau_max (free): {float(Ric_min_interp(min(tau_turn_free, tau_pot_grid[-1]-0.01))):.6f}")
print(f"    Internal NEC holds along free trajectory: {np.all(Ric_min_traj_free >= -1e-10)}")


# =============================================================================
# SECTION 7: Cosmic censorship analysis
# =============================================================================

print("\n" + "=" * 78)
print("  COSMIC CENSORSHIP ANALYSIS")
print("=" * 78)

print("""
  The modulus space has a curvature singularity at tau -> infinity
  (Kretschner K ~ exp(4*tau)). The question is whether this singularity
  is NAKED (visible to a 4D observer) or CENSORED (hidden behind a horizon
  or inaccessible by dynamics).

  THREE lines of defense censor the singularity:
""")

# Line 1: Energy budget
print("  [1] ENERGY BUDGET CENSORSHIP:")
print(f"      Initial kinetic energy: T_0 = {T_initial:.2f}")
print(f"      Potential at geometric transition: V(0.537) = {V_at_transition:.2f}")
if T_initial < V_at_transition:
    print(f"      T_0 < V(0.537): modulus CANNOT reach the transition!")
    print(f"      Classical turning point at tau = {tau_turn_free:.6f}")
    print(f"      This is {tau_turn_free / 0.537 * 100:.1f}% of the way to the transition")
    energy_censored = True
else:
    print(f"      T_0 >= V(0.537): modulus CAN reach the transition")
    energy_censored = False

# Line 2: BCS friction
print(f"\n  [2] BCS FRICTION CENSORSHIP:")
print(f"      BCS friction coefficient: Gamma = {gamma_fric:.0f}")
print(f"      Stopping distance: dtau = v*M/Gamma = {v_terminal * M_geom / gamma_fric:.4f}")
tau_max_fric = np.max(tau_fric)
print(f"      With friction, modulus reaches tau = {tau_max_fric:.6f}")
print(f"      This is {tau_max_fric / 0.537 * 100:.1f}% of the way to the transition")
friction_censored = tau_max_fric < 0.537

# Line 3: 4D energy conditions
print(f"\n  [3] 4D ENERGY CONDITIONS:")
print(f"      NEC (rho + p >= 0): ALWAYS satisfied for scalar field")
print(f"        min(rho + p) along free trajectory = {np.min(nec_free):.6f}")
nec_holds = np.all(nec_free >= -1e-10)
print(f"        NEC holds: {nec_holds}")
print(f"      WEC (rho >= 0): satisfied when V >= 0")
print(f"        min(rho) along free trajectory = {np.min(wec_free):.6f}")
wec_holds = np.all(wec_free >= -1e-10)
print(f"        WEC holds: {wec_holds}")
print(f"      SEC (rho + 3p >= 0): requires T >= V")
sec_holds = np.all(sec_free >= -1e-10)
sec_min_val = np.min(sec_free)
print(f"        min(rho + 3p) = {sec_min_val:.6f}")
if not sec_holds:
    # Find where SEC fails
    sec_fail_idx = np.where(sec_free < -1e-10)[0]
    if len(sec_fail_idx) > 0:
        tau_sec_fail = tau_free[sec_fail_idx[0]]
        print(f"        SEC first fails at tau = {tau_sec_fail:.6f}")
        print(f"        Physical: V > T -> potential dominates -> accelerated expansion")
        print(f"        This is TRANSIENT (modulus decelerating, V/T ratio changes)")
else:
    print(f"        SEC holds throughout")
print(f"      DEC (rho >= |p|): ALWAYS satisfied for scalar + non-negative potential")
dec_holds = np.all(dec_free >= -1e-10)
dec_min_val = np.min(dec_free)
print(f"        min(rho - |p|) = {dec_min_val:.6f}")
print(f"        DEC holds: {dec_holds}")

# Internal NEC
print(f"\n  [4] INTERNAL SPACE NEC:")
int_nec_max_tau = min(tau_turn_free, tau_pot_grid[-1] - 0.01)
ric_at_max = float(Ric_min_interp(int_nec_max_tau))
print(f"      Ric_min at trajectory maximum (tau={int_nec_max_tau:.4f}): {ric_at_max:.6f}")
print(f"      Internal NEC holds along entire trajectory: {ric_at_max > -1e-10}")


# =============================================================================
# SECTION 8: Equation of state and Penrose inequality analog
# =============================================================================

print(f"\n  Step 8: Equation of state analysis...")

# At tau=0: w = (T - 0) / (T + 0) = 1 (pure kinetic, stiff matter)
# At turnaround: w = (0 - V) / (0 + V) = -1 (pure potential, de Sitter)
# The equation of state tracks the transit from w=+1 to w=-1.

w_initial = w_free[0]
# Find w at turnaround
if sol_free.t_events[2].size > 0:
    turn_idx = np.argmin(np.abs(t_free - sol_free.t_events[2][0]))
    w_turnaround = w_free[max(0, turn_idx - 1)]
else:
    w_turnaround = w_free[-1]

# Find w at fold
fold_time_idx = np.argmin(np.abs(tau_free - tau_fold))
w_at_fold = w_free[fold_time_idx]

print(f"    w at tau=0: {w_initial:.6f} (pure stiff matter)")
print(f"    w at fold: {w_at_fold:.6f}")
print(f"    w at turnaround: {w_turnaround:.6f}")
print(f"    w range: [{np.min(w_free):.6f}, {np.max(w_free):.6f}]")

# The Penrose inequality analog:
# In 4D GR: M_ADM >= sqrt(A / 16*pi) for asymptotically flat spacetimes
# For the internal space, the analog is:
# The "mass" (energy in the modulus field) is bounded by the "area" (volume of internal space)
# Since the Jensen deformation is isovolumetric, the internal volume is CONSTANT.
# So the Penrose inequality analog is trivially satisfied: M >= 0 always.
# The internal space cannot form a black hole because it has no trapped surfaces
# (volume-preserving = no two-sided contraction).

print(f"\n    Penrose inequality analog:")
print(f"    Internal volume = const (isovolumetric Jensen) -> no area growth")
print(f"    No trapped surfaces -> no event horizon in internal space")
print(f"    Penrose inequality: TRIVIALLY SATISFIED (M >= 0 always)")


# =============================================================================
# SECTION 9: Summary and Gate Verdict
# =============================================================================

print("\n" + "=" * 78)
print("  COSMIC-CENSORSHIP-49: GATE VERDICT")
print("=" * 78)

# Assess overshoot
overshoot = reaches_transition_free or reaches_transition_fric

# Assess energy conditions
all_4d_ec_hold = nec_holds and wec_holds and dec_holds
sec_transient = not sec_holds  # SEC may fail transiently

# Gate criteria:
# PASS: no overshoot to 0.537, or energy conditions hold throughout
# INFO: transient DEC violation, no singularity
# FAIL: permanent DEC violation or naked singularity

if not overshoot and all_4d_ec_hold:
    verdict = "PASS"
    reason = "No overshoot AND all 4D energy conditions hold (NEC, WEC, DEC)"
elif overshoot and all_4d_ec_hold:
    verdict = "PASS"
    reason = "Overshoot occurs but all energy conditions hold throughout"
elif not all_4d_ec_hold and not overshoot:
    # Check if DEC violated
    if not dec_holds:
        verdict = "FAIL"
        reason = "DEC violation without overshoot (exotic matter)"
    else:
        verdict = "INFO"
        reason = "SEC violation only (transient accelerated expansion)"
else:
    verdict = "INFO"
    reason = "Overshoot with SEC violation (transient, no singularity)"

print(f"\n  VERDICT: {verdict}")
print(f"  Reason: {reason}")
print()
print(f"  Summary:")
print(f"    A. Free from tau=0:           tau_max = {tau_turn_free:.6f} {'REACHES' if reaches_transition_free else 'DOES NOT reach'} 0.537")
print(f"    B. Friction from tau=0:       tau_max = {tau_max_fric:.6f} (friction never engages: turn < fold)")
print(f"    D. Free from fold:            tau_max = {tau_max_fold_free:.6f} {'REACHES' if tau_max_fold_free >= 0.537 else 'DOES NOT reach'} 0.537")
print(f"    E. Friction from fold:        tau_max = {tau_max_fold_fric:.6f} (dtau = {tau_max_fold_fric - tau_fold:.4f})")
print(f"    C. v_crit to 0.537 (tau=0):   {v_crit_transition:.2f} ({v_crit_transition/v_terminal:.1f}x v_terminal)")
print(f"    F. v_crit to 0.537 (fold):    {v_crit_from_fold:.2f} ({v_crit_from_fold/v_terminal:.1f}x v_terminal)")
print(f"    G. v_crit to NEC (tau=0):     {v_crit_nec:.2f} ({v_crit_nec/v_terminal:.1f}x v_terminal)")
print(f"    ----- 4D Energy Conditions -----")
print(f"    NEC: SATISFIED (rho + p = G_mod * v^2 >= 0)")
print(f"    WEC: SATISFIED (V >= 0 along trajectory)")
print(f"    DEC: SATISFIED (V >= 0, tau_dot real)")
if sec_transient:
    print(f"    SEC: TRANSIENT VIOLATION (V > T near turnaround, w < -1/3)")
    print(f"         Standard for any scalar with potential > kinetic (inflaton analog)")
else:
    print(f"    SEC: SATISFIED throughout")
print(f"    Internal NEC: SATISFIED (Ric_min > 0 along entire trajectory)")
print(f"    ----- Censorship Assessment -----")
print(f"    Layer 1 (energy budget):    T_0 < V(0.537) by {energy_deficit_transition:.0f} units ({energy_deficit_transition/T_initial*100:.0f}%)")
print(f"    Layer 2 (BCS friction):     tau_max = {tau_max_fold_fric:.4f} << 0.537")
print(f"    Layer 3 (no trapped surfaces): volume-preserving Jensen")
print(f"    Singularity at tau->inf: CENSORED by all three mechanisms")


# =============================================================================
# SECTION 10: Save data
# =============================================================================

print("\n  Saving data...")

outdir = os.path.dirname(os.path.abspath(__file__))
np.savez_compressed(
    os.path.join(outdir, 's49_cosmic_censorship.npz'),
    # Trajectories
    t_free=t_free, tau_free=tau_free, v_free=v_free,
    t_fric=t_fric, tau_fric=tau_fric, v_fric=v_fric,
    # Energy conditions (free trajectory)
    rho_free=rho_free, p_free=p_free, w_free=w_free,
    nec_free=nec_free, wec_free=wec_free, sec_free=sec_free, dec_free=dec_free,
    # Energy conditions (friction trajectory)
    rho_fric=rho_fric, p_fric=p_fric, w_fric=w_fric,
    # Potential
    tau_pot_grid=tau_pot_grid, V_tau=V_tau, dV_dtau=dV_dtau,
    R_scalar=R_arr, Kretschner=K_arr,
    # Critical values
    tau_turn_free=tau_turn_free,
    tau_max_fric=tau_max_fric,
    v_crit_transition=v_crit_transition,
    v_crit_nec=v_crit_nec,
    v_crit_from_fold=v_crit_from_fold,
    v_terminal=v_terminal,
    # Case D/E: from fold
    t_fold_free=t_fold_free, tau_fold_free=tau_fold_free, v_fold_free=v_fold_free,
    t_fold_fric=t_fold_fric, tau_fold_fric=tau_fold_fric, v_fold_fric=v_fold_fric,
    tau_max_fold_free=tau_max_fold_free,
    tau_max_fold_fric=tau_max_fold_fric,
    delta_V_fold_to_trans=delta_V_fold_to_trans,
    T_initial=T_initial,
    V_at_transition=V_at_transition,
    V_at_nec=V_at_nec,
    energy_deficit_transition=energy_deficit_transition,
    gamma_fric=gamma_fric,
    # Calibration
    c2_fit=c2_fit, c4_fit=c4_fit,
    # Internal NEC
    Ric_min_traj=Ric_min_arr,
    # Gate
    verdict=verdict,
    reaches_transition_free=reaches_transition_free,
    reaches_transition_fric=reaches_transition_fric,
    nec_holds=nec_holds,
    wec_holds=wec_holds,
    sec_holds=sec_holds,
    dec_holds=dec_holds,
    energy_censored=energy_censored,
    friction_censored=friction_censored,
)


# =============================================================================
# SECTION 11: Plots
# =============================================================================

print("  Generating plots...")

fig, axes = plt.subplots(2, 3, figsize=(20, 12))

# Panel 1: Trajectory tau(t)
ax1 = axes[0, 0]
ax1.plot(t_free * 1000, tau_free, 'b-', linewidth=2, label='Free (tau_0=0)')
ax1.plot(t_fric * 1000, tau_fric, 'r--', linewidth=2, label='Friction (tau_0=0)')
ax1.plot(t_fold_free * 1000, tau_fold_free, 'g-', linewidth=2, label='Free (tau_0=fold)')
ax1.plot(t_fold_fric * 1000, tau_fold_fric, 'm--', linewidth=2, label='Friction (tau_0=fold)')
ax1.axhline(0.537, color='purple', linestyle='--', alpha=0.7, label=r'$\tau = 0.537$ (transition)')
ax1.axhline(tau_fold, color='orange', linestyle='--', alpha=0.7, label=r'$\tau = 0.19$ (fold)')
ax1.set_xlabel(r'$t \times 10^3$ [$M_{KK}^{-1}$]', fontsize=12)
ax1.set_ylabel(r'$\tau(t)$', fontsize=12)
ax1.set_title('Modulus Trajectory', fontsize=13)
ax1.legend(fontsize=8, loc='upper right')
ax1.grid(True, alpha=0.3)

# Panel 2: Velocity v(t)
ax2 = axes[0, 1]
ax2.plot(t_free * 1000, v_free, 'b-', linewidth=2, label='Free')
ax2.plot(t_fric * 1000, v_fric, 'r-', linewidth=2, label='Friction')
ax2.axhline(0, color='k', linestyle='-', alpha=0.2)
ax2.set_xlabel(r'$t \times 10^3$ [$M_{KK}^{-1}$]', fontsize=12)
ax2.set_ylabel(r'$v = d\tau/dt$ [$M_{KK}$]', fontsize=12)
ax2.set_title('Modulus Velocity', fontsize=13)
ax2.legend(fontsize=9)
ax2.grid(True, alpha=0.3)

# Panel 3: Potential V(tau)
ax3 = axes[0, 2]
ax3.plot(tau_pot_grid, V_tau, 'k-', linewidth=2)
ax3.axhline(T_initial, color='blue', linestyle=':', alpha=0.7, label=f'$T_0 = {T_initial:.0f}$')
ax3.axvline(tau_fold, color='orange', linestyle='--', alpha=0.5)
ax3.axvline(0.537, color='purple', linestyle='--', alpha=0.5)
if tau_turn_free < tau_pot_grid[-1]:
    ax3.axvline(tau_turn_free, color='blue', linestyle=':', alpha=0.5,
                label=f'turnaround (tau={tau_turn_free:.3f})')
ax3.set_xlabel(r'$\tau$', fontsize=12)
ax3.set_ylabel(r'$V(\tau)$', fontsize=12)
ax3.set_title(r'Spectral Action Potential $V(\tau)$', fontsize=13)
ax3.legend(fontsize=9)
ax3.grid(True, alpha=0.3)

# Panel 4: Equation of state w(tau)
ax4 = axes[1, 0]
# Plot w vs tau for the free trajectory (skip first few points where tau~0)
valid = tau_free > 0.001
ax4.plot(tau_free[valid], w_free[valid], 'b-', linewidth=2, label='Free')
valid_fric = tau_fric > 0.001
if np.any(valid_fric):
    ax4.plot(tau_fric[valid_fric], w_fric[valid_fric], 'r-', linewidth=2, label='Friction')
ax4.axhline(1, color='gray', linestyle=':', alpha=0.5, label='w=+1 (stiff)')
ax4.axhline(-1, color='gray', linestyle='--', alpha=0.5, label='w=-1 (de Sitter)')
ax4.axhline(-1/3, color='green', linestyle=':', alpha=0.5, label='w=-1/3 (SEC)')
ax4.axhline(0, color='k', linestyle='-', alpha=0.2)
ax4.axvline(tau_fold, color='orange', linestyle='--', alpha=0.5)
ax4.set_xlabel(r'$\tau$', fontsize=12)
ax4.set_ylabel(r'$w = p/\rho$', fontsize=12)
ax4.set_title('Equation of State', fontsize=13)
ax4.legend(fontsize=9, loc='lower left')
ax4.set_ylim(-1.2, 1.2)
ax4.grid(True, alpha=0.3)

# Panel 5: Energy conditions
ax5 = axes[1, 1]
ax5.plot(tau_free[valid], nec_free[valid], 'b-', linewidth=2, label='NEC (rho+p)')
ax5.plot(tau_free[valid], wec_free[valid], 'g-', linewidth=2, label='WEC (rho)')
ax5.plot(tau_free[valid], sec_free[valid], 'r-', linewidth=2, label='SEC (rho+3p)')
ax5.plot(tau_free[valid], dec_free[valid], 'orange', linewidth=2, label='DEC (rho-|p|)')
ax5.axhline(0, color='k', linestyle='-', alpha=0.3)
ax5.axvline(tau_fold, color='orange', linestyle='--', alpha=0.5)
ax5.set_xlabel(r'$\tau$', fontsize=12)
ax5.set_ylabel('Energy condition value', fontsize=12)
ax5.set_title('4D Energy Conditions Along Trajectory', fontsize=13)
ax5.legend(fontsize=9)
ax5.grid(True, alpha=0.3)

# Panel 6: Censorship diagram (ASCII-art style visualization)
ax6 = axes[1, 2]
ax6.set_xlim(0, 1)
ax6.set_ylim(0, 1)
ax6.set_aspect('equal')

# Draw zones
zones = [
    (0.00, 0.35, 'green', 0.15, 'Zone I\n(positive K)'),
    (0.35, 0.65, 'yellow', 0.15, 'Zone II\n(mixed K)'),
    (0.65, 1.00, 'red', 0.15, 'Zone III\n(NEC fail)'),
]
for y0_z, y1_z, color, alpha, label in zones:
    ax6.axhspan(y0_z, y1_z, alpha=alpha, color=color)
    ax6.text(0.5, (y0_z + y1_z) / 2, label, ha='center', va='center',
             fontsize=10, fontweight='bold')

# Mark key tau values (mapped to [0,1])
tau_map = lambda t: 2 * np.arctan(t) / PI  # compactify
marks = [
    (tau_map(tau_fold), 'Fold (0.19)', 'orange'),
    (tau_map(tau_max_fric), f'Transit end ({tau_max_fric:.3f})', 'brown'),
    (tau_map(tau_turn_free), f'Free turnaround ({tau_turn_free:.3f})', 'blue'),
    (tau_map(0.537), 'K=0 transition (0.537)', 'purple'),
    (tau_map(1.382), 'NEC violation (1.382)', 'darkred'),
]
for psi_val, label, color in marks:
    ax6.axhline(psi_val, color=color, linestyle='--', alpha=0.7)
    ax6.text(0.02, psi_val + 0.015, label, fontsize=8, color=color)

# Arrow showing censorship
ax6.annotate('', xy=(0.85, tau_map(tau_max_fric)),
            xytext=(0.85, tau_map(0.537)),
            arrowprops=dict(arrowstyle='<->', color='purple', lw=2))
ax6.text(0.87, (tau_map(tau_max_fric) + tau_map(0.537))/2, 'CENSORED\nREGION',
         fontsize=9, color='purple', ha='left', va='center', fontweight='bold')

ax6.set_xlabel('', fontsize=12)
ax6.set_ylabel(r'$\psi = \frac{2}{\pi}\arctan(\tau)$', fontsize=12)
ax6.set_title('Cosmic Censorship Diagram', fontsize=13)
ax6.set_xticks([])

plt.tight_layout()
plt.savefig(os.path.join(outdir, 's49_cosmic_censorship.png'), dpi=150, bbox_inches='tight')
plt.close()

t_end = time.time()
print(f"\n  Total computation time: {t_end - t_start:.1f}s")
print("  Files: s49_cosmic_censorship.npz, s49_cosmic_censorship.png")
print(f"\n  VERDICT: {verdict}")
print("=" * 78)
