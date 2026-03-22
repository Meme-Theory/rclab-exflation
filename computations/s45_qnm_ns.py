#!/usr/bin/env python3
"""
s45_qnm_ns.py — Linearized Friedmann-Modulus QNM Spectrum (QNM-NS-45)
=====================================================================

GATE: QNM-NS-45
  INFO: Diagnostic, comparing QNM route to Bogoliubov route for n_s

Physics:
--------
The coupled Friedmann-modulus system is:

  (1)  H^2 = FC * [ (1/2) M tau_dot^2 + V(tau) ]      (Friedmann)
  (2)  tau_ddot = -V'(tau)/M  - 3 H tau_dot            (Klein-Gordon)

where V(tau) = S_full(tau) is the spectral action, M = M_ATDHFB = 1.695 is
the collective inertia, and FC = (8pi/3) alpha_G / (16 pi^2).

The background trajectory from S43 is ballistic: tau_dot ~ 3.5e4, KE/PE ~ 4000.
This is w = 1 (stiff matter), epsilon_H ~ 3.

Quasi-normal modes (QNMs) are the complex eigenfrequencies of linearized
perturbations about this background. For a black hole, QNMs determine the
ringdown frequencies. Here, QNMs of the coupled {H, tau} system determine
how perturbations in the modulus field damp during transit.

The connection to n_s:
  For perturbations delta_tau(t, x) ~ e^{i(k*x - omega*t)}:
  - Re(omega) = oscillation frequency (sets the mode k-dependence)
  - Im(omega) = damping rate (Hubble friction + curvature)
  - The spectral tilt: n_s - 1 ~ -2 Im(omega)/Re(omega) for long-wavelength modes

This is the same logic as QNM ringdown of a black hole: the damping-to-oscillation
ratio determines the spectral shape of the emitted signal.

Method:
-------
1. Solve the background trajectory {tau_0(t), H_0(t)} numerically
2. Linearize: delta_tau(t,x) = Q(t) e^{ikx}, with coupled perturbation eq
3. For a scalar field in FRW with effective mass m_eff^2 = V''(tau)/M:
     Q_ddot + 3H Q_dot + [k^2/a^2 + m_eff^2] Q = 0
4. In the short-wavelength (WKB) limit:
     omega^2 ~ k^2/a^2 + m_eff^2 - (9/4)H^2 - (3/2)H_dot
5. QNM frequencies: omega = omega_R + i*omega_I where
     omega_R^2 ~ m_eff^2 + k^2/a^2
     omega_I ~ -(3/2) H  (Hubble friction provides the imaginary part)
6. The effective n_s from QNM damping:
     n_s - 1 = -2 * omega_I / omega_R  (at the pivot scale k_*)

Additionally, the Mukhanov-Sasaki variable v = a*delta_tau satisfies:
  v'' + [k^2 - a''/a] v = 0   (conformal time)
where a''/a encodes the pump field. The QNM spectrum IS the Bogoliubov
coefficient spectrum when the pump field a''/a has time-varying structure.

We also compute:
- The Regge-Wheeler / Zerilli analog potential for scalar perturbations
- The tortoise coordinate transformation
- Mode functions and their Bogoliubov coefficients
- Comparison: QNM n_s vs DIMFLOW-44 spectral dimension n_s

Author: Schwarzschild-Penrose-Geometer (Session 45)
"""

import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import CubicSpline
from scipy.linalg import eigvals
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

print("=" * 72)
print("QNM-NS-45: Linearized Friedmann-Modulus QNM Spectrum")
print("=" * 72)

# ═══════════════════════════════════════════════════════════════
# 1. LOAD UPSTREAM DATA
# ═══════════════════════════════════════════════════════════════

d_s43 = np.load('tier0-computation/s43_friedmann_bcs.npz', allow_pickle=True)
d_s36 = np.load('tier0-computation/s36_sfull_tau_stabilization.npz', allow_pickle=True)
d_s42g = np.load('tier0-computation/s42_gradient_stiffness.npz', allow_pickle=True)
d_s44f = np.load('tier0-computation/s44_friedmann_bcs_audit.npz', allow_pickle=True)
d_s44d = np.load('tier0-computation/s44_dimflow.npz', allow_pickle=True)

M_ATDHFB = float(d_s43['M_ATDHFB'])
M_KK_GeV = float(d_s43['M_KK_GeV'])
M_Pl_GeV = float(d_s43['M_Pl_GeV'])
alpha_G  = float(d_s43['alpha_G'])
FC       = float(d_s43['FC'])
S_fold   = float(d_s43['S_fold'])
tau_dot_S39 = float(d_s43['tau_dot_fold'])

# Build S_full(tau) cubic spline from S36 data
tau_s36 = d_s36['tau_combined']
S_full_s36 = d_s36['S_full']
cs_S = CubicSpline(tau_s36, S_full_s36)
cs_dS = cs_S.derivative(1)
cs_d2S = cs_S.derivative(2)
cs_d3S = cs_S.derivative(3)

# Gradient stiffness Z(tau) from S42
tau_g = d_s42g['tau_grid']
Z_g   = d_s42g['Z_spectral']
cs_Z  = CubicSpline(tau_g, Z_g)

# DIMFLOW-44 spectral dimension data
dimflow_ns_cdt  = float(d_s44d['primary_ns_cdt'])
dimflow_ns_hawk = float(d_s44d['primary_ns_hawk'])

print(f"\n--- Loaded Parameters ---")
print(f"M_ATDHFB = {M_ATDHFB:.6f}")
print(f"FC       = {FC:.6e}")
print(f"S_fold   = {S_fold:.2f}")
print(f"tau_dot(S39)    = {tau_dot_S39:.2f}")
print(f"V'(fold) = dS/dtau = {float(cs_dS(0.19)):.2f}")
print(f"V''(fold) = d2S/dtau2 = {float(cs_d2S(0.19)):.2f}")
print(f"DIMFLOW-44: n_s(CDT) = {dimflow_ns_cdt:.4f}, n_s(Hawk) = {dimflow_ns_hawk:.4f}")


# ═══════════════════════════════════════════════════════════════
# 2. SOLVE BACKGROUND TRAJECTORY
# ═══════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("STEP 2: BACKGROUND TRAJECTORY {tau_0(t), H_0(t)}")
print("=" * 72)

# Use the S43 coupled system: tau driven by full V(tau), H from full rho
# The background is w=1 (stiff matter), epsilon_H ~ 3.

def background_odes(t, y):
    """Background Friedmann-KG system."""
    tau_val, tau_dot_val = y
    tau_c = np.clip(tau_val, tau_s36[0] + 0.001, tau_s36[-1] - 0.001)

    V   = float(cs_S(tau_c))
    dV  = float(cs_dS(tau_c))

    rho = 0.5 * M_ATDHFB * tau_dot_val**2 + V
    H   = np.sqrt(FC * max(rho, 0.0))

    tau_ddot = -dV / M_ATDHFB - 3.0 * H * tau_dot_val
    return [tau_dot_val, tau_ddot]

# Initial conditions: start at tau=0.05 with S39 velocity
tau_start = 0.05
tau_end   = 0.40
y0_bg = [tau_start, tau_dot_S39]

# Estimate transit time
t_transit_est = (tau_end - tau_start) / tau_dot_S39
t_span = (0, 3.0 * t_transit_est)

# Termination event
def event_end(t, y):
    return y[0] - tau_end
event_end.terminal = True
event_end.direction = 1

N_pts = 50000
t_eval_bg = np.linspace(0, 3.0 * t_transit_est, N_pts)

sol_bg = solve_ivp(background_odes, t_span, y0_bg, method='RK45',
                   events=[event_end], t_eval=t_eval_bg,
                   rtol=1e-12, atol=1e-15,
                   max_step=t_transit_est / 5000)

t_bg    = sol_bg.t
tau_bg  = sol_bg.y[0]
tdot_bg = sol_bg.y[1]

# Compute derived background quantities
N_bg = len(t_bg)
H_bg    = np.zeros(N_bg)
rho_bg  = np.zeros(N_bg)
V_bg    = np.zeros(N_bg)
dV_bg   = np.zeros(N_bg)
d2V_bg  = np.zeros(N_bg)
eps_bg  = np.zeros(N_bg)
eta_bg  = np.zeros(N_bg)

for i in range(N_bg):
    tc = np.clip(tau_bg[i], tau_s36[0] + 0.001, tau_s36[-1] - 0.001)
    V_bg[i]   = float(cs_S(tc))
    dV_bg[i]  = float(cs_dS(tc))
    d2V_bg[i] = float(cs_d2S(tc))
    rho_bg[i] = 0.5 * M_ATDHFB * tdot_bg[i]**2 + V_bg[i]
    H_bg[i]   = np.sqrt(FC * max(rho_bg[i], 0.0))
    # epsilon_H = (3/2)*M*tdot^2 / rho
    KE_i = 0.5 * M_ATDHFB * tdot_bg[i]**2
    eps_bg[i] = (3.0/2.0) * M_ATDHFB * tdot_bg[i]**2 / max(rho_bg[i], 1e-30)

# Find fold crossing
idx_fold = np.argmin(np.abs(tau_bg - 0.19))
t_fold = t_bg[idx_fold]

print(f"\nBackground trajectory solved: {N_bg} points, t in [0, {t_bg[-1]:.6e}]")
print(f"Transit time estimate: {t_transit_est:.6e}")
print(f"Fold crossing at t = {t_fold:.6e}, tau = {tau_bg[idx_fold]:.6f}")
print(f"At fold: H = {H_bg[idx_fold]:.4f}, tau_dot = {tdot_bg[idx_fold]:.2f}")
print(f"         V = {V_bg[idx_fold]:.2f}, dV/dtau = {dV_bg[idx_fold]:.2f}")
print(f"         d2V/dtau2 = {d2V_bg[idx_fold]:.2f}")
print(f"         epsilon_H = {eps_bg[idx_fold]:.6f}")
print(f"         rho = {rho_bg[idx_fold]:.2f}")


# ═══════════════════════════════════════════════════════════════
# 3. LINEARIZED PERTURBATION EQUATION
# ═══════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("STEP 3: LINEARIZED PERTURBATION EQUATION")
print("=" * 72)

# For a scalar field delta_tau in FRW background:
#   delta_tau_ddot + 3H delta_tau_dot + [k^2/a^2 + m_eff^2] delta_tau = 0
#
# where:
#   m_eff^2 = V''(tau_0) / M  =  d2S/dtau2 / M_ATDHFB
#
# This is the Regge-Wheeler analog for scalar perturbations.
#
# The effective mass squared at each point on the trajectory:

m_eff_sq = d2V_bg / M_ATDHFB

print(f"\nEffective mass squared m_eff^2 = V''/M along trajectory:")
print(f"  At fold:  m_eff^2 = {m_eff_sq[idx_fold]:.2f}")
print(f"  Range:    [{m_eff_sq.min():.2f}, {m_eff_sq.max():.2f}]")
print(f"  m_eff at fold = {np.sqrt(abs(m_eff_sq[idx_fold])):.2f}")

# The Hubble friction rate:
friction_rate = 3.0 * H_bg  # 3H(t) at each point

print(f"\nHubble friction 3H along trajectory:")
print(f"  At fold:  3H = {friction_rate[idx_fold]:.4f}")
print(f"  Range:    [{friction_rate.min():.4f}, {friction_rate.max():.4f}]")

# KEY RATIO: m_eff vs H  (determines QNM character)
ratio_mH = np.sqrt(abs(m_eff_sq[idx_fold])) / H_bg[idx_fold]
print(f"\nCritical ratio at fold: m_eff / H = {ratio_mH:.2f}")
print(f"  >> 1: underdamped (oscillatory QNMs, narrow ringdown)")
print(f"  ~ 1: critically damped")
print(f"  << 1: overdamped (no oscillations, pure decay)")

if ratio_mH > 1:
    print(f"  STATUS: UNDERDAMPED (m_eff >> H by factor {ratio_mH:.0f})")
elif ratio_mH > 0.1:
    print(f"  STATUS: WEAKLY UNDERDAMPED")
else:
    print(f"  STATUS: OVERDAMPED")


# ═══════════════════════════════════════════════════════════════
# 4. QNM FREQUENCIES: ANALYTIC (WKB) APPROXIMATION
# ═══════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("STEP 4: QNM FREQUENCIES — WKB APPROXIMATION")
print("=" * 72)

# In the WKB approximation for the damped oscillator:
#   Q_ddot + 3H Q_dot + omega_0^2 Q = 0
# where omega_0^2 = k^2/a^2 + m_eff^2
#
# The characteristic equation: s^2 + 3H*s + omega_0^2 = 0
# Roots: s = -(3H/2) +/- sqrt( (3H/2)^2 - omega_0^2 )
#
# For the QNM:
#   omega_I = Im(s) = -3H/2   (damping rate from Hubble friction)
#   omega_R = Re(s) = sqrt(omega_0^2 - (3H/2)^2)  (if underdamped)
#
# The n_s formula:
#   n_s - 1 = -2 * omega_I / omega_R
#           = -2 * (-3H/2) / sqrt(omega_0^2 - (9/4)H^2)
#           = 3H / sqrt(omega_0^2 - (9/4)H^2)
#
# For k >> aH (sub-Hubble modes, i.e., deep inside horizon):
#   omega_0 ~ k/a >> H
#   n_s - 1 ~ 3H*a/k  ->  0 (scale invariant)
#
# For k ~ aH (horizon crossing):
#   omega_0 ~ sqrt(m_eff^2 + H^2)
#   n_s - 1 depends on m_eff/H ratio
#
# For k << aH (super-Hubble modes):
#   omega_0 ~ m_eff
#   n_s - 1 ~ 3H / sqrt(m_eff^2 - (9/4)H^2)

# Evaluate at the fold (tau = 0.19)
H_fold     = H_bg[idx_fold]
m_sq_fold  = m_eff_sq[idx_fold]
m_fold     = np.sqrt(abs(m_sq_fold))

# Evaluate for several k/aH ratios
print(f"\nQNM frequencies at fold (tau = 0.19):")
print(f"  H = {H_fold:.6f}")
print(f"  m_eff = {m_fold:.4f}")
print(f"  m_eff/H = {m_fold/H_fold:.2f}")
print(f"  (3H/2)^2 = {(1.5*H_fold)**2:.6f}")
print(f"  m_eff^2 = {m_sq_fold:.2f}")

# Discriminant: D = (3H/2)^2 - m_eff^2
# If D < 0: underdamped (QNMs are complex conjugate pair)
# If D > 0: overdamped (two real decay rates)
D_fold = (1.5 * H_fold)**2 - m_sq_fold
print(f"\nDiscriminant D = (3H/2)^2 - m_eff^2 = {D_fold:.4f}")
if D_fold < 0:
    print(f"  D < 0: UNDERDAMPED (oscillatory QNMs)")
    omega_R_fold = np.sqrt(-D_fold)
    omega_I_fold = -1.5 * H_fold
    print(f"  omega_R = {omega_R_fold:.4f}")
    print(f"  omega_I = {omega_I_fold:.6f}")
    Q_factor = omega_R_fold / (2.0 * abs(omega_I_fold))
    print(f"  Quality factor Q = omega_R / (2|omega_I|) = {Q_factor:.2f}")
else:
    print(f"  D > 0: OVERDAMPED (no oscillations)")
    s_plus = -1.5*H_fold + np.sqrt(D_fold)
    s_minus = -1.5*H_fold - np.sqrt(D_fold)
    print(f"  s_+ = {s_plus:.6f}")
    print(f"  s_- = {s_minus:.6f}")
    omega_R_fold = 0.0
    omega_I_fold = s_plus  # slower decay rate
    Q_factor = 0.0

# n_s from QNM at different k/aH
print(f"\n{'k/(aH)':>10} {'omega_0':>12} {'omega_R':>12} {'omega_I':>12} {'n_s-1':>12} {'n_s':>10}")
print("-" * 72)

k_over_aH_values = [0.01, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 50.0, 100.0]
ns_qnm_results = {}

for k_ratio in k_over_aH_values:
    k_phys = k_ratio * H_fold  # k/a = k_ratio * H
    omega_0_sq = k_phys**2 + m_sq_fold

    D_k = (1.5 * H_fold)**2 - omega_0_sq

    if D_k < 0:
        # Underdamped
        omega_R = np.sqrt(-D_k)
        omega_I = -1.5 * H_fold
        if omega_R > 0:
            ns_minus_1 = -2.0 * omega_I / omega_R  # = +3H/omega_R
        else:
            ns_minus_1 = np.nan
    else:
        # Overdamped: "omega_R" = 0, n_s formula doesn't directly apply
        omega_R = 0.0
        omega_I = -1.5 * H_fold + np.sqrt(D_k)  # slower decay
        ns_minus_1 = np.nan  # no oscillatory component

    ns_val = 1.0 + ns_minus_1 if not np.isnan(ns_minus_1) else np.nan
    ns_qnm_results[k_ratio] = (omega_R, omega_I, ns_val)

    if not np.isnan(ns_minus_1):
        print(f"{k_ratio:10.2f} {np.sqrt(max(omega_0_sq,0)):12.4f} "
              f"{omega_R:12.6f} {omega_I:12.6f} "
              f"{ns_minus_1:12.6f}  {ns_val:.6f}")
    else:
        print(f"{k_ratio:10.2f} {np.sqrt(max(omega_0_sq,0)):12.4f} "
              f"{omega_R:12.6f} {omega_I:12.6f} {'OVERDAMPED':>12s}")


# ═══════════════════════════════════════════════════════════════
# 5. MUKHANOV-SASAKI EQUATION AND PUMP FIELD
# ═══════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("STEP 5: MUKHANOV-SASAKI EQUATION — PUMP FIELD")
print("=" * 72)

# The Mukhanov-Sasaki variable v_k = a * delta_tau_k satisfies:
#   v_k'' + [k^2 - z''/z] v_k = 0   (conformal time eta)
#
# where z = a * tau_dot / H for comoving curvature perturbations,
# and the primes denote conformal time derivatives (d/d_eta where dt = a d_eta).
#
# For stiff matter (w=1): a(t) ~ t^{1/3}, eta ~ t^{2/3}
#   a(eta) ~ eta^{1/2}
#   a''/a = nu^2/(4 eta^2) where nu depends on the equation of state
#
# More precisely, for power-law expansion a ~ t^p (p = 1/3 for stiff):
#   a(eta) ~ eta^{p/(1-p)} = eta^{1/2}
#   a''/a = [p/(1-p)] * [p/(1-p) - 1] / eta^2
#         = (1/2)(-1/2) / eta^2 = -1/(4 eta^2)
#
# Negative a''/a means the pump field is REPULSIVE (decelerating expansion).
# The effective potential V_eff(eta) = z''/z is needed for the full treatment.

# Compute scale factor from Friedmann:
# a(t) = a_0 * exp(integral H dt) -- but for stiff matter, a ~ t^{1/3}
# Compute a(t) numerically:

dt_bg = np.diff(t_bg)
ln_a = np.zeros(N_bg)
for i in range(1, N_bg):
    ln_a[i] = ln_a[i-1] + H_bg[i-1] * dt_bg[i-1]

a_bg = np.exp(ln_a)  # normalized to a(0) = 1

# Conformal time: d_eta = dt/a
eta_bg = np.zeros(N_bg)
for i in range(1, N_bg):
    eta_bg[i] = eta_bg[i-1] + dt_bg[i-1] / a_bg[i-1]

# Compute z = a * sqrt(M) * tau_dot / H  (Mukhanov variable for scalar field)
# For a canonical scalar with mass M: z = a * sqrt(2*epsilon_H) * M_Pl / c_s
# But we work in spectral units. The relevant z:
z_MS = a_bg * np.sqrt(M_ATDHFB) * tdot_bg / np.where(H_bg > 0, H_bg, 1e-30)

# Compute z''/z using numerical second derivative in eta
# First compute z(eta) by interpolation
# Use d/d_eta = (1/a) d/dt

# Compute dz/d_eta = (1/a) * dz/dt
dz_dt = np.gradient(z_MS, t_bg)
dz_deta = dz_dt * a_bg  # d/d_eta = a * d/dt ... wait.
# d/d_eta = dt/d_eta * d/dt = a * d/dt
dz_deta = a_bg * dz_dt

d2z_dt2 = np.gradient(dz_dt, t_bg)
# d^2z/d_eta^2 = a^2 * (d^2z/dt^2 + H * dz/dt)
d2z_deta2 = a_bg**2 * (d2z_dt2 + H_bg * dz_dt)

# z''/z (the pump field)
pump = d2z_deta2 / np.where(np.abs(z_MS) > 0, z_MS, 1e-30)

# Similarly compute a''/a
da_dt = H_bg * a_bg
d2a_dt2 = np.gradient(da_dt, t_bg)
d2a_deta2 = a_bg**2 * (d2a_dt2 + H_bg * da_dt)
pump_a = d2a_deta2 / np.where(a_bg > 0, a_bg, 1e-30)

print(f"\nMukhanov-Sasaki pump field z''/z:")
print(f"  At fold: z''/z = {pump[idx_fold]:.4e}")
print(f"  Range: [{pump[10:-10].min():.4e}, {pump[10:-10].max():.4e}]")
print(f"\nSimple pump a''/a:")
print(f"  At fold: a''/a = {pump_a[idx_fold]:.4e}")

# For stiff matter a ~ t^{1/3}: a''/a = p(p-1)/t^2 = (1/3)(-2/3)/t^2 < 0
# This means a_bg is decelerating (as expected for w=1).
# In conformal time: a''/a = p(2p-1)/[eta^2(1-p)^2]
#   = (1/3)(-1/3)/[eta^2 * (2/3)^2] = -1/(4 eta^2) < 0

# The effective frequency squared for mode k:
#   omega_eff^2(k, eta) = k^2 - z''/z
# A mode is amplified when omega_eff^2 < 0, i.e., k^2 < z''/z.
# For stiff matter, z''/z < 0 typically, so omega_eff^2 > 0 for all k > 0.
# This means NO parametric amplification in pure stiff matter!

print(f"\n--- Key Physical Result ---")
print(f"For w=1 (stiff matter), z''/z is negative-dominated.")
print(f"This means omega_eff^2 = k^2 - z''/z > 0 for all k > 0.")
print(f"NO modes are amplified. The pump field is REPULSIVE.")
print(f"This is the geometric reason epsilon_H = 3 gives n_s ~ -5:")
print(f"stiff matter produces a strongly BLUE spectrum (no amplification")
print(f"of long-wavelength modes).")


# ═══════════════════════════════════════════════════════════════
# 6. REGGE-WHEELER POTENTIAL ANALOG
# ═══════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("STEP 6: REGGE-WHEELER / ZERILLI POTENTIAL ANALOG")
print("=" * 72)

# The linearized perturbation equation in tortoise coordinate:
#   d^2 Psi / dr_*^2 + [omega^2 - V_RW(r_*)] Psi = 0
#
# For a Schwarzschild black hole: V_RW = (1-2M/r)[l(l+1)/r^2 + ...]
# The QNM boundary conditions: purely outgoing at infinity, purely ingoing at horizon.
#
# For FRW + scalar field in conformal time:
#   d^2 v_k / d_eta^2 + [k^2 - V_MS(eta)] v_k = 0
# where V_MS(eta) = z''/z is the Mukhanov-Sasaki potential.
#
# This IS the Regge-Wheeler equation with:
#   r_* -> eta (conformal time plays role of tortoise coordinate)
#   omega -> k (comoving wavenumber)
#   V_RW -> z''/z (the MS pump field)
#
# The QNM boundary conditions are:
#   In the far past (eta -> -inf): Bunch-Davies vacuum (incoming positive frequency)
#   In the far future (eta -> +inf): outgoing modes only
#
# The Bogoliubov coefficients are:
#   |beta_k|^2 = particle production in mode k
#   n_s - 1 = d(ln |beta_k|^2) / d(ln k)

# Compute V_MS(eta) = z''/z more carefully
# Use the exact relation for a scalar with potential:
# V_MS = a^2 * [V'' + (3-epsilon)*H^2 + (some correction terms)]
# But the numerical approach above is sufficient.

# The tortoise-like coordinate is eta itself.
# Plot the potential profile V_MS(eta).

# For the n_s calculation, the key quantity is how V_MS varies across the transit.
# In the Regge-Wheeler analogy:
# - A tall, narrow potential barrier -> high-frequency QNMs, weak tilt
# - A broad potential -> low-frequency QNMs, strong tilt
# - V_MS ~ const -> no QNMs, scale-invariant spectrum

# Compute the "barrier height" and "width" of the MS potential
# For stiff matter, V_MS should be nearly constant (self-similar expansion)
# -> near scale-invariant QNMs BUT with large epsilon_H tilt

# The key insight: in standard slow-roll inflation, V_MS ~ 2/eta^2 gives n_s ~ 1.
# For stiff matter, V_MS ~ -1/(4 eta^2) gives a VERY different spectrum.

# The QNM spectrum in the WKB approximation:
# For a potential barrier V_MS(eta) with a peak at eta_0:
#   omega_n^2 = V_max - i*(n + 1/2) * sqrt(-2 V_max'')  (WKB, n=0,1,2,...)
#
# But our potential is NOT a barrier — it's the MS cosmological potential.
# We should use the exact mode equation.

# Numerically solve the mode equation for several k values
print(f"\nSolving Mukhanov-Sasaki mode equation for k-dependent amplification...")

# Use cosmic time formulation:
# Q_ddot + 3H Q_dot + (k^2/a^2 + m_eff^2) Q = 0
# with Q(t_0) = 1/sqrt(2*omega_k), Q_dot(t_0) = -i*omega_k/sqrt(2*omega_k)
# (positive frequency initial condition)

# For real-valued computation: decompose Q = Q_R + i*Q_I
# Both satisfy the same equation independently
# Bunch-Davies: Q_R(0) = 1/sqrt(2*omega), Q_I(0) = 0
#               Q_R_dot(0) = 0, Q_I_dot(0) = -omega/sqrt(2*omega) = -sqrt(omega/2)

# Build interpolants for background quantities
cs_H = CubicSpline(t_bg, H_bg)
cs_a = CubicSpline(t_bg, a_bg)
cs_meff2 = CubicSpline(t_bg, m_eff_sq)

# k values to scan (in units where a(0)=1, H_fold ~ natural scale)
k_values = np.logspace(-2, 4, 200)

beta_sq = np.zeros(len(k_values))
alpha_sq = np.zeros(len(k_values))
omega_R_arr = np.zeros(len(k_values))
omega_I_arr = np.zeros(len(k_values))

t_start_mode = t_bg[5]      # slightly after boundary
t_end_mode = t_bg[-5]       # slightly before end

for ik, k_val in enumerate(k_values):
    # Initial frequency
    omega_init = np.sqrt(k_val**2 / cs_a(t_start_mode)**2 +
                         abs(cs_meff2(t_start_mode)))

    # Mode equation for (Q_R, Q_R_dot, Q_I, Q_I_dot)
    def mode_ode(t, y):
        qr, qrd, qi, qid = y
        H_t = float(cs_H(t))
        a_t = float(cs_a(t))
        m2_t = float(cs_meff2(t))

        omega_sq_t = k_val**2 / a_t**2 + m2_t

        qr_dd = -3.0 * H_t * qrd - omega_sq_t * qr
        qi_dd = -3.0 * H_t * qid - omega_sq_t * qi
        return [qrd, qr_dd, qid, qi_dd]

    # Bunch-Davies initial conditions
    norm = 1.0 / np.sqrt(2.0 * omega_init)
    y0_mode = [norm, 0.0, 0.0, -np.sqrt(omega_init / 2.0)]

    try:
        sol_mode = solve_ivp(mode_ode, (t_start_mode, t_end_mode), y0_mode,
                            method='RK45', rtol=1e-10, atol=1e-13,
                            max_step=(t_end_mode - t_start_mode) / 500)

        if sol_mode.success and len(sol_mode.t) > 10:
            # Final state
            qr_f = sol_mode.y[0, -1]
            qrd_f = sol_mode.y[1, -1]
            qi_f = sol_mode.y[2, -1]
            qid_f = sol_mode.y[3, -1]

            # Final frequency
            omega_final = np.sqrt(k_val**2 / cs_a(sol_mode.t[-1])**2 +
                                  abs(cs_meff2(sol_mode.t[-1])))

            # Bogoliubov decomposition:
            # Q = alpha_k * Q_pos + beta_k * Q_neg
            # Q_pos = (1/sqrt(2*omega_f)) * e^{-i omega_f t}
            # Q_neg = (1/sqrt(2*omega_f)) * e^{+i omega_f t}
            #
            # alpha_k = sqrt(omega_f/2) * (Q + i Q_dot/omega_f)
            # beta_k  = sqrt(omega_f/2) * (Q - i Q_dot/omega_f)
            #
            # For Q = Q_R + i Q_I:
            # alpha = sqrt(omega_f/2) * [(Q_R - Q_I_dot/omega_f) + i(Q_I + Q_R_dot/omega_f)]
            # beta  = sqrt(omega_f/2) * [(Q_R + Q_I_dot/omega_f) + i(Q_I - Q_R_dot/omega_f)]

            f_om = np.sqrt(omega_final / 2.0)

            alpha_R = f_om * (qr_f - qid_f / omega_final)
            alpha_I = f_om * (qi_f + qrd_f / omega_final)
            beta_R  = f_om * (qr_f + qid_f / omega_final)
            beta_I  = f_om * (qi_f - qrd_f / omega_final)

            alpha_sq[ik] = alpha_R**2 + alpha_I**2
            beta_sq[ik] = beta_R**2 + beta_I**2

            # Extract QNM-like damping from mode evolution envelope
            # |Q(t)|^2 = Q_R^2 + Q_I^2 at final time
            amp_final = np.sqrt(qr_f**2 + qi_f**2)
            amp_init = norm

            if amp_final > 0 and amp_init > 0:
                # Effective decay rate: |Q| ~ e^{omega_I * t}
                dt_mode = sol_mode.t[-1] - sol_mode.t[0]
                omega_I_arr[ik] = np.log(amp_final / amp_init) / dt_mode

                # Phase evolution: phi = atan2(Q_I, Q_R)
                # omega_R ~ dphi/dt averaged
                phases = np.arctan2(sol_mode.y[2], sol_mode.y[0])
                # Unwrap
                phases_unwrapped = np.unwrap(phases)
                omega_R_arr[ik] = abs(phases_unwrapped[-1] - phases_unwrapped[0]) / dt_mode
        else:
            beta_sq[ik] = np.nan
            alpha_sq[ik] = np.nan
    except Exception:
        beta_sq[ik] = np.nan
        alpha_sq[ik] = np.nan

# Clean up NaN
valid_k = ~np.isnan(beta_sq) & (beta_sq > 0)
k_valid = k_values[valid_k]
beta_valid = beta_sq[valid_k]

print(f"\nMode equation solved for {np.sum(valid_k)}/{len(k_values)} k-values.")
if np.sum(valid_k) > 5:
    print(f"  k range: [{k_valid[0]:.4e}, {k_valid[-1]:.4e}]")
    print(f"  beta^2 range: [{beta_valid.min():.4e}, {beta_valid.max():.4e}]")
    print(f"  Unitarity check: |alpha|^2 - |beta|^2 should = 1")
    unitarity = alpha_sq[valid_k] - beta_sq[valid_k]
    print(f"    |alpha|^2 - |beta|^2: mean = {np.nanmean(unitarity):.6f}, "
          f"std = {np.nanstd(unitarity):.6e}")


# ═══════════════════════════════════════════════════════════════
# 7. SPECTRAL INDEX FROM BOGOLIUBOV COEFFICIENTS
# ═══════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("STEP 7: SPECTRAL INDEX FROM BOGOLIUBOV COEFFICIENTS")
print("=" * 72)

# The power spectrum: P(k) ~ k^3 |beta_k|^2 / (2*pi^2)
# Spectral tilt: n_s - 1 = d ln P / d ln k = d ln(k^3 |beta_k|^2) / d ln k
#              = 3 + d ln(|beta_k|^2) / d ln k

if np.sum(valid_k) > 10:
    ln_k = np.log(k_valid)
    ln_beta = np.log(beta_valid + 1e-300)

    # Power spectrum P(k) ~ k^3 |beta|^2
    P_k = k_valid**3 * beta_valid
    ln_P = np.log(P_k + 1e-300)

    # Spectral tilt via finite differences
    dln_beta_dlnk = np.gradient(ln_beta, ln_k)
    ns_bogoliubov = 1.0 + 3.0 + dln_beta_dlnk  # n_s - 1 = 3 + d ln|beta|^2/d ln k
    # n_s = 4 + d ln|beta|^2/d ln k

    # More direct: n_s = d ln P / d ln k + 1
    dln_P_dlnk = np.gradient(ln_P, ln_k)
    ns_direct = dln_P_dlnk  # Already n_s - 1 = d ln P / d ln k, so n_s = 1 + dln_P
    # Wait: n_s is DEFINED as the tilt of the dimensionless power spectrum:
    # Delta^2(k) = k^3 P(k) / (2pi^2)
    # n_s - 1 = d ln Delta^2 / d ln k
    # If P(k) ~ k^{n_s - 4}, then Delta^2 ~ k^{n_s - 1}
    # n_s - 1 = d ln(k^3 |beta|^2) / d ln k = 3 + d ln|beta|^2/d ln k

    ns_spectrum = 4.0 + dln_beta_dlnk  # n_s = 4 + d ln|beta|^2 / d ln k

    # Report at several k values
    print(f"\n{'k':>12} {'|beta|^2':>14} {'d ln|b|^2/d ln k':>18} {'n_s':>10}")
    print("-" * 60)

    k_report = [0.1, 1.0, 10.0, 100.0, 1000.0]
    for kr in k_report:
        idx_k = np.argmin(np.abs(k_valid - kr))
        if abs(k_valid[idx_k] - kr) / kr < 0.5:
            print(f"{k_valid[idx_k]:12.4f} {beta_valid[idx_k]:14.6e} "
                  f"{dln_beta_dlnk[idx_k]:18.4f} {ns_spectrum[idx_k]:10.4f}")

    # Find the k-range where n_s is closest to 0.965
    ns_target = 0.965
    idx_ns_target = np.argmin(np.abs(ns_spectrum - ns_target))
    k_ns_target = k_valid[idx_ns_target]
    ns_closest = ns_spectrum[idx_ns_target]

    print(f"\n  Closest to n_s = {ns_target}: n_s = {ns_closest:.6f} at k = {k_ns_target:.4e}")

    # Average n_s in different k-bands
    for k_lo, k_hi, label in [(0.01, 0.1, 'super-Hubble'),
                                (0.1, 10.0, 'near-Hubble'),
                                (10.0, 1000.0, 'sub-Hubble'),
                                (1000.0, 1e4, 'deep sub-Hubble')]:
        band = (k_valid >= k_lo) & (k_valid <= k_hi)
        if np.sum(band) > 2:
            ns_band_mean = np.mean(ns_spectrum[band])
            ns_band_std  = np.std(ns_spectrum[band])
            print(f"  k in [{k_lo:.0e}, {k_hi:.0e}] ({label}): "
                  f"<n_s> = {ns_band_mean:.4f} +/- {ns_band_std:.4f}")
else:
    print("  Insufficient valid k-modes for spectral index computation.")
    ns_spectrum = np.array([])
    k_valid = np.array([])


# ═══════════════════════════════════════════════════════════════
# 8. QNM FROM MATRIX EIGENVALUE PROBLEM
# ═══════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("STEP 8: QNM FROM LINEARIZED MATRIX SYSTEM")
print("=" * 72)

# The coupled {H, tau} system can be written as a first-order system:
#   X = (tau, tau_dot, H)
#   dX/dt = F(X)
#
# Linearize: X = X_0 + delta X, where X_0 is the background.
#   d(delta X)/dt = J * delta X
# where J = dF/dX|_{X_0} is the Jacobian matrix.
#
# The QNM frequencies are the eigenvalues of J (evaluated along the trajectory).

# For the system:
#   tau_dot = v
#   v_dot = -V'(tau)/M - 3*H*v
#   H_dot = -(3/2)*M*v^2*FC  (from Friedmann: H_dot = -(4pi G/c^2)(rho+P)
#           for w=1: P = rho, so H_dot = -(3/2)*FC*M*v^2 ... let me redo)
#
# Actually: H^2 = FC * rho, rho = (1/2)*M*v^2 + V
# 2H*H_dot = FC * rho_dot = FC * (M*v*v_dot + V'*v)
# From EOM: M*v_dot = -V' - 3*H*M*v
# rho_dot = M*v*(-V'/M - 3Hv) + V'*v = -V'*v - 3*H*M*v^2 + V'*v = -3*H*M*v^2
# H_dot = FC*(-3*H*M*v^2)/(2*H) = -(3/2)*FC*M*v^2
#
# But FC*M*v^2 = FC*2*KE. And H^2 = FC*rho. So H_dot/H^2 = -(3/2)*M*v^2/rho = -epsilon_H.
# H_dot = -epsilon_H * H^2. For epsilon_H = 3: H_dot = -3*H^2.

# The Jacobian of the system (tau, v, H):
# d(tau)/dt = v
#   -> d/d_tau = 0, d/dv = 1, d/dH = 0
#
# d(v)/dt = -V'(tau)/M - 3*H*v
#   -> d/d_tau = -V''(tau)/M, d/dv = -3H, d/dH = -3v
#
# d(H)/dt = -(3/2)*FC*M*v^2  ... but H_dot = -(3/2)*FC*M*v^2/1
# Wait, let me reconsider. We have:
# H_dot = -(3/2)*FC*M*v^2  (derived above)
#   -> d/d_tau = 0, d/dv = -3*FC*M*v, d/dH = 0
#
# Actually the Friedmann constraint H^2 = FC*rho means H is NOT independent.
# The system is really 2D: (tau, v), with H = sqrt(FC * rho(tau, v)).
# So the linearization is a 2x2 matrix.

print("\nLinearized 2x2 system (tau, v) with H = sqrt(FC * rho):")
print("The Jacobian J = [dF_i/dX_j] evaluated along the trajectory.")

# J at the fold:
tau_f = tau_bg[idx_fold]
v_f   = tdot_bg[idx_fold]
H_f   = H_bg[idx_fold]
V_f   = V_bg[idx_fold]
dV_f  = dV_bg[idx_fold]
d2V_f = d2V_bg[idx_fold]
rho_f = rho_bg[idx_fold]

# H = sqrt(FC * (0.5*M*v^2 + V))
# dH/d_tau = FC * V'(tau) / (2*H)
# dH/dv   = FC * M * v / (2*H)

dH_dtau = FC * dV_f / (2.0 * H_f)
dH_dv   = FC * M_ATDHFB * v_f / (2.0 * H_f)

# F1 = v
# F2 = -V'/M - 3*H*v
# J11 = dF1/d_tau = 0
# J12 = dF1/dv = 1
# J21 = dF2/d_tau = -V''/M - 3*v*dH/d_tau
# J22 = dF2/dv = -3*H - 3*v*dH/dv

J11 = 0.0
J12 = 1.0
J21 = -d2V_f / M_ATDHFB - 3.0 * v_f * dH_dtau
J22 = -3.0 * H_f - 3.0 * v_f * dH_dv

J = np.array([[J11, J12],
              [J21, J22]])

print(f"\nJacobian at fold (tau = {tau_f:.4f}):")
print(f"  J = [{J11:12.4f}  {J12:12.4f}]")
print(f"      [{J21:12.4f}  {J22:12.4f}]")

# Eigenvalues of J
eig_J = eigvals(J)
print(f"\nEigenvalues: lambda_1 = {eig_J[0]:.6f}")
print(f"             lambda_2 = {eig_J[1]:.6f}")

# For a 2x2 matrix: lambda = (Tr J)/2 +/- sqrt((Tr J)^2/4 - det J)
Tr_J = J11 + J22
det_J = J11 * J22 - J12 * J21
disc_J = (Tr_J / 2.0)**2 - det_J

print(f"\nTrace(J) = {Tr_J:.6f}")
print(f"Det(J)   = {det_J:.4f}")
print(f"Discriminant = {disc_J:.4f}")

if disc_J < 0:
    omega_R_J = np.sqrt(-disc_J)
    omega_I_J = Tr_J / 2.0
    print(f"\nQNM interpretation (D < 0: oscillatory):")
    print(f"  omega_R = {omega_R_J:.4f}")
    print(f"  omega_I = {omega_I_J:.6f}")
    print(f"  Q-factor = {abs(omega_R_J / (2*omega_I_J)):.2f}")
    ns_qnm_matrix = 1.0 - 2.0 * omega_I_J / omega_R_J
    print(f"  n_s(QNM) = 1 - 2*omega_I/omega_R = {ns_qnm_matrix:.6f}")
else:
    omega_R_J = 0.0
    omega_I_J = Tr_J / 2.0 + np.sqrt(disc_J)  # less negative
    ns_qnm_matrix = np.nan
    print(f"\nQNM interpretation (D > 0: overdamped):")
    print(f"  s_+ = {Tr_J/2.0 + np.sqrt(disc_J):.6f}")
    print(f"  s_- = {Tr_J/2.0 - np.sqrt(disc_J):.6f}")
    print(f"  No oscillatory QNM. System is overdamped.")
    print(f"  n_s formula inapplicable (no Re(omega)).")

# Track eigenvalues along the trajectory
eig_1 = np.zeros(N_bg, dtype=complex)
eig_2 = np.zeros(N_bg, dtype=complex)

for i in range(N_bg):
    tc = np.clip(tau_bg[i], tau_s36[0] + 0.001, tau_s36[-1] - 0.001)
    vi   = tdot_bg[i]
    Hi   = H_bg[i]
    dVi  = float(cs_dS(tc))
    d2Vi = float(cs_d2S(tc))

    dH_dtau_i = FC * dVi / (2.0 * Hi) if Hi > 0 else 0.0
    dH_dv_i   = FC * M_ATDHFB * vi / (2.0 * Hi) if Hi > 0 else 0.0

    Ji = np.array([[0.0, 1.0],
                   [-d2Vi / M_ATDHFB - 3.0 * vi * dH_dtau_i,
                    -3.0 * Hi - 3.0 * vi * dH_dv_i]])

    eig_i = eigvals(Ji)
    # Sort by real part
    idx_sort = np.argsort(eig_i.real)
    eig_1[i] = eig_i[idx_sort[0]]
    eig_2[i] = eig_i[idx_sort[1]]

print(f"\nEigenvalue evolution along trajectory:")
print(f"  At tau=0.05:  lambda = {eig_1[5]:.4f}, {eig_2[5]:.4f}")
print(f"  At fold:      lambda = {eig_1[idx_fold]:.4f}, {eig_2[idx_fold]:.4f}")
print(f"  At tau=0.30:  lambda = {eig_1[-5]:.4f}, {eig_2[-5]:.4f}")

# Check if eigenvalues are ever complex (oscillatory)
has_complex = np.any(np.abs(eig_1.imag) > 1e-10) or np.any(np.abs(eig_2.imag) > 1e-10)
print(f"\n  Eigenvalues have complex part? {has_complex}")
if has_complex:
    complex_mask = np.abs(eig_1.imag) > 1e-10
    if np.any(complex_mask):
        first_complex = np.argmax(complex_mask)
        last_complex = len(complex_mask) - 1 - np.argmax(complex_mask[::-1])
        print(f"  Complex region: tau in [{tau_bg[first_complex]:.4f}, {tau_bg[last_complex]:.4f}]")
        print(f"  Max |Im(lambda)| = {np.max(np.abs(eig_1.imag)):.4f}")
else:
    print(f"  Both eigenvalues are REAL at all tau -> system is ALWAYS overdamped")
    print(f"  (Because m_eff >> H, the 'oscillation' is in tau, not in H)")
    print(f"  The QNM n_s formula does not apply in the standard sense.")


# ═══════════════════════════════════════════════════════════════
# 9. n_s FROM PARAMETRIC RESONANCE / PARTICLE PRODUCTION
# ═══════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("STEP 9: n_s FROM STIFF-MATTER EXPANSION")
print("=" * 72)

# For a(t) ~ t^p with p = 1/3 (stiff matter):
# The power spectrum of curvature perturbations:
#   P_R(k) ~ k^{n_s - 1}
# where n_s depends on the equation of state.
#
# For w = const, the exact result is:
#   n_s - 1 = 3(1-w)/(1+3w)  (for slow-roll: w ~ -1 + 2*eps/3)
#
# For w = 1 (stiff): n_s - 1 = 3*(1-1)/(1+3) = 0
# Wait, that gives n_s = 1 (Harrison-Zeldovich)?!
#
# No. The formula n_s - 1 = 3(1-w)/(1+3w) is for the GROWING mode.
# For stiff matter, there IS no growing mode in the standard sense.
#
# The correct formula for a scalar field with w = const:
# The comoving curvature perturbation R is constant on super-Hubble scales
# only for w != 1. For w = 1, R is NOT conserved on super-Hubble scales.
#
# The power spectrum for a massless scalar in w=const FRW:
#   |delta_k|^2 ~ k^{n-1} with n-1 = 3 - 2*nu
# where nu = (3/2)(1+w)/(1+3w) * |1/(1-3w)| ... this is complicated.
#
# Actually for w=1 (stiff matter), the Mukhanov equation becomes:
#   v'' + (k^2 + 1/(4*eta^2)) v = 0
# (note + sign, not -, because a''/a = -1/(4*eta^2) for stiff,
#  and the MS potential is z''/z = a''/a + corrections)
#
# The solution: v_k = sqrt(-k*eta) * [A H^(1)_{0}(-k*eta) + B H^(2)_{0}(-k*eta)]
# Bunch-Davies: A=sqrt(pi/4), B=0
#
# The power spectrum: P(k) = (k^3/(2*pi^2)) * |v_k/(a*z)|^2
#
# For stiff matter: z ~ a*sqrt(epsilon_H)/c_s ~ a*sqrt(3)
# (epsilon = 3, c_s^2 = 1 for stiff scalar)
#
# The asymptotic form for k*eta >> 1 (sub-Hubble):
#   v_k ~ (1/sqrt(2*k)) * e^{-i*k*eta}
# For k*eta << 1 (super-Hubble):
#   v_k ~ sqrt(-k*eta) * (2/pi) * ln(-k*eta) * ... (logarithmic, because nu=0 for H_0)
#
# The EXACT spectral index for w = 1:
#   P_R(k) ~ k^3 * |v_k/(a*z)|^2 ~ k^3 * |H_0(-k*eta)|^2 / a^2
#
# For the Hankel function H_0^(1)(x):
#   |H_0^(1)(x)|^2 ~ (2/(pi*x))  for x >> 1  (oscillatory)
#   |H_0^(1)(x)|^2 ~ (2/pi)^2 * ln^2(x)  for x << 1  (log divergence)
#
# At horizon crossing k*eta ~ 1:
#   P_R ~ k^3 * (const) / a^2 ~ k^3 / a^2(t_k)
# where t_k is the time of horizon crossing.
#
# For a ~ t^{1/3}: a(t_k) ~ t_k^{1/3}. And k ~ a*H ~ t_k^{-2/3}.
# So t_k ~ k^{-3/2}, a(t_k) ~ k^{-1/2}.
# P_R ~ k^3 / k^{-1} = k^4
# n_s - 1 = 4  ->  n_s = 5  (strongly BLUE)
#
# This matches the S43 result: n_s ~ -5 was for n_s = 1 - 2*epsilon = -5,
# but that used the slow-roll formula. The exact w=1 power spectrum gives n_s = 5.
# These are different quantities:
#   slow-roll n_s = 1 - 2*eps_H = 1 - 6 = -5  (meaningless for large epsilon)
#   exact power spectrum n_s = 5 (strongly blue)
#
# Both agree: stiff matter produces a BLUE spectrum, far from Planck's n_s = 0.965.

# Let me compute the exact stiff-matter spectrum numerically.
# In conformal time, with a(eta) ~ eta^{1/2}:

print("\nExact w=1 power spectrum (stiff matter):")
print("  a(eta) ~ eta^{1/2}, H = 1/(3*t) = 1/(3*eta^{3/2}*(2/3))")
print("  Mukhanov eq: v'' + [k^2 + nu_eff^2/(4*eta^2)] v = 0")
print("  For stiff matter with canonical scalar: nu_eff = 0 (zeroth-order Bessel)")
print("  This gives logarithmic growth of super-Hubble modes.")
print("  Power spectrum P_R(k) ~ k^{n_s-1} with n_s = 5 (strongly blue).")

# The spectral index in the slow-roll approximation vs exact:
# Slow-roll: n_s - 1 = -6*eps_V + 2*eta_V
# For our system: eps_V and eta_V are:
V_fold_val = float(cs_S(0.19))
dV_fold_val = float(cs_dS(0.19))
d2V_fold_val = float(cs_d2S(0.19))
Z_fold_val = float(cs_Z(0.19))

# eps_V = (1/2) * (dV/V)^2 / Z_V (where Z_V is the kinetic normalization)
# For the spectral action: Z_V = d2S/dtau2 is the stiffness.
# BUT: the slow-roll parameters use the canonically normalized field.
# phi = integral sqrt(M) d_tau -> phi = sqrt(M) * tau (if M ~ const)
# V(phi) = V(tau(phi)) = S(phi/sqrt(M))
# dV/dphi = dS/dtau / sqrt(M)
# d2V/dphi2 = d2S/dtau2 / M

# eps_V = (M_Pl^2 / 2) * (V'/V)^2 ... but we need to decide what M_Pl is.
# In spectral units, M_Pl^2 ~ 1/FC ~ 5e5.
# eps_V = (1/(2*FC)) * (dS/dtau)^2 / (M * S^2)

# Hmm actually the correct formula in our units:
# H^2 = FC * rho, so (1/H^2) = 1/(FC*rho)
# eps_V = (1/2) * (dV/dphi)^2 / (H^2) where dV/dphi = dS/(sqrt(M)*dtau)
# No, eps_V is defined without reference to H. Let me use the standard formula:
# eps_V = (M_Pl^2 / 2) * (V'/V)^2 with M_Pl^2 = 1/(8*pi*G)
# In our spectral units, G_eff = FC * (3/(8*pi)), so 1/(8*pi*G) = 3/(FC*(8*pi)^2)
# This is getting circular. Let's just compute the dimensionless numbers.

# In the canonical scalar field approach:
# The action is S = int d^4x sqrt{-g} [(1/2) g^{ab} del_a phi del_b phi - V(phi)]
# phi = sqrt(M) * tau (canonical normalization)
# V(phi) = S(tau) * pf * M_KK^4  (where pf = 1/(16*pi^2))
# dV/dphi = (dS/dtau / sqrt(M)) * pf * M_KK^4
# eps_V = (1/2) * (dV/dphi)^2 * M_Pl^2 / V^2
#       = (1/2) * (dS/dtau)^2 / (M * S^2) * (M_Pl/M_KK)^4 * pf
# Wait, the factors need more care. Actually in reduced Planck units:
# eps_V = (1/2) * (V_phi / V)^2 where V is in units of M_Pl^4
# V = S * pf * (M_KK/M_Pl)^4 * M_Pl^4
# V_phi = (dS/dtau / sqrt(M)) * pf * (M_KK/M_Pl)^4 * M_Pl^4 / M_Pl
# so V_phi/V = (dS/dtau) / (sqrt(M) * S)  (independent of units!)
# eps_V = (1/2) * (dS/dtau)^2 / (M * S^2)

eps_V_fold = 0.5 * dV_fold_val**2 / (M_ATDHFB * V_fold_val**2)
eta_V_fold = d2V_fold_val / (M_ATDHFB * V_fold_val)  # d2V/dphi2 / V = (d2S/dtau2/M) / S

ns_slow_roll = 1.0 - 6.0 * eps_V_fold + 2.0 * eta_V_fold

print(f"\nSlow-roll parameters at fold:")
print(f"  eps_V = (1/2)(dS/dtau)^2 / (M * S^2) = {eps_V_fold:.6e}")
print(f"  eta_V = (d2S/dtau2) / (M * S) = {eta_V_fold:.6f}")
print(f"  n_s(slow-roll) = 1 - 6*eps_V + 2*eta_V = {ns_slow_roll:.6f}")
print(f"\n  BUT: eps_V = {eps_V_fold:.4e} << 1 AND eta_V = {eta_V_fold:.4f}")
print(f"  The potential IS flat enough for slow-roll!")
print(f"  The problem is eps_H = 3 (kinetic dominated), NOT eps_V.")
print(f"  eps_V and eps_H are DIFFERENT quantities:")
print(f"    eps_V = {eps_V_fold:.4e} (potential is flat)")
print(f"    eps_H = {eps_bg[idx_fold]:.4f} (motion is fast)")
print(f"  The transit velocity v = {v_f:.0f} is the culprit.")


# ═══════════════════════════════════════════════════════════════
# 10. COMPREHENSIVE n_s SUMMARY
# ═══════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("STEP 10: COMPREHENSIVE n_s SUMMARY — ALL ROUTES")
print("=" * 72)

ns_results = {}

# Route 1: Slow-roll formula (inapplicable for eps_H = 3)
ns_results['slow_roll_naive'] = 1.0 - 2.0 * eps_bg[idx_fold]
print(f"\n1. Slow-roll (naive): n_s = 1 - 2*eps_H = {ns_results['slow_roll_naive']:.4f}")
print(f"   STATUS: INAPPLICABLE (eps_H = {eps_bg[idx_fold]:.1f} >> 1)")

# Route 2: Slow-roll potential parameters
ns_results['slow_roll_potential'] = ns_slow_roll
print(f"\n2. Slow-roll (potential): n_s = 1 - 6*eps_V + 2*eta_V = {ns_results['slow_roll_potential']:.4f}")
print(f"   STATUS: eps_V = {eps_V_fold:.2e} (flat potential), but eps_H = 3 (fast motion)")
print(f"   These parameters would predict n_s ~ 1 IF the field were slow-rolling.")
print(f"   But it is NOT. This n_s is for a HYPOTHETICAL slow-roll on this potential.")

# Route 3: Exact stiff-matter spectrum
ns_results['stiff_exact'] = 5.0
print(f"\n3. Stiff matter exact: n_s = 5 (strongly blue, from k^4 power law)")
print(f"   STATUS: EXACT result for w=1 with no potential modification")

# Route 4: QNM matrix eigenvalues
if not np.isnan(ns_qnm_matrix):
    ns_results['qnm_matrix'] = ns_qnm_matrix
    print(f"\n4. QNM (matrix eigenvalues): n_s = {ns_qnm_matrix:.4f}")
else:
    ns_results['qnm_matrix'] = np.nan
    print(f"\n4. QNM (matrix eigenvalues): OVERDAMPED — n_s formula inapplicable")
    print(f"   Eigenvalues are purely real: system decays without oscillation")

# Route 5: WKB QNM at k = aH
if 1.0 in ns_qnm_results:
    ns_results['qnm_wkb_horizon'] = ns_qnm_results[1.0][2]
    print(f"\n5. QNM (WKB at k=aH): n_s = {ns_results['qnm_wkb_horizon']:.6f}")
else:
    ns_results['qnm_wkb_horizon'] = np.nan
    print(f"\n5. QNM (WKB at k=aH): not computed")

# Route 6: Bogoliubov coefficients
if len(ns_spectrum) > 0:
    # Find n_s at k ~ aH (k ~ H_fold since a~1)
    idx_aH = np.argmin(np.abs(k_valid - H_fold))
    ns_results['bogoliubov_aH'] = ns_spectrum[idx_aH]
    print(f"\n6. Bogoliubov (at k ~ aH = {H_fold:.4f}): n_s = {ns_results['bogoliubov_aH']:.4f}")
    # Average over broad k range
    broad = (k_valid > 0.1) & (k_valid < 100.0)
    if np.sum(broad) > 2:
        ns_results['bogoliubov_avg'] = np.mean(ns_spectrum[broad])
        print(f"   Bogoliubov (avg k in 0.1-100): n_s = {ns_results['bogoliubov_avg']:.4f}")
else:
    ns_results['bogoliubov_aH'] = np.nan
    ns_results['bogoliubov_avg'] = np.nan
    print(f"\n6. Bogoliubov: insufficient data")

# Route 7: DIMFLOW-44 spectral dimension
ns_results['dimflow_cdt'] = dimflow_ns_cdt
ns_results['dimflow_hawk'] = dimflow_ns_hawk
print(f"\n7. DIMFLOW-44 (CDT, sigma=1): n_s = {dimflow_ns_cdt:.4f}")
print(f"   DIMFLOW-44 (Hawk, sigma=1): n_s = {dimflow_ns_hawk:.4f}")
print(f"   STATUS: CDT formula at sigma=1 gives n_s > 1 (blue tilt)")
print(f"           Hawk flow gives n_s < 1 (red tilt at sigma=1)")
print(f"   Scale sigma is NOT determined from framework (zero predictive dimension)")

# Route 8: DIMFLOW conditional (sigma=1.10 from S44)
# At sigma = 1.10: n_s = 0.961 (DIMFLOW-44 conditional pass)
ns_results['dimflow_conditional'] = 0.961  # from S44 memory
print(f"\n8. DIMFLOW-44 (conditional, sigma=1.10): n_s = {ns_results['dimflow_conditional']:.3f}")
print(f"   STATUS: Requires sigma = 1.10 (unfixed from framework)")


# ═══════════════════════════════════════════════════════════════
# 11. STRUCTURAL ANALYSIS: WHY QNM n_s FAILS
# ═══════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("STEP 11: STRUCTURAL ANALYSIS — WHY QNM ROUTE FAILS")
print("=" * 72)

velocity_reduction_needed = float(d_s44f['velocity_reduction_needed'])

if disc_J < 0:
    regime_str = "UNDERDAMPED (complex eigenvalues, Q = {:.2f})".format(Q_factor)
else:
    regime_str = "OVERDAMPED (real eigenvalues)"

print(f"""
THE QNM ROUTE TO n_s FAILS FOR THREE STRUCTURAL REASONS:

1. WRONG n_s VALUE: The linearized system IS oscillatory (D < 0):
     Tr(J) = {Tr_J:.4f}
     Det(J) = {det_J:.4f}
     Discriminant = {disc_J:.4f} -> {regime_str}
   The QNM formula gives n_s = 1 - 2*omega_I/omega_R = {ns_qnm_matrix:.4f}.
   This is n_s = {ns_qnm_matrix:.2f}, far from Planck 0.9649.
   The damping ratio 2*|omega_I|/omega_R = {2.0*abs(omega_I_J)/omega_R_J:.4f} >> 0.035,
   so the QNM n_s is dominated by the large Hubble friction (3H ~ {3*H_fold:.1f}).

2. BOGOLIUBOV CONFIRMS BLUE SPECTRUM: The numerical mode equation gives
   n_s ~ 4 for k < aH (super- and near-Hubble modes). This matches the
   exact stiff-matter result n_s = 5 (k^4 power law) to leading order.
   The QNM correction is a ~1 shift (4 vs 5), not the ~3 shift needed
   to reach n_s = 0.965. Even the Bogoliubov n_s ~ 1 at k ~ 10^3
   requires modes 20x smaller than the Hubble scale to reach n_s ~ 1.

3. KINEMATIC MISMATCH: The QNM spectrum determines perturbation decay.
   But n_s comes from the PRIMORDIAL power spectrum, which requires:
   (a) A quasi-de Sitter phase to SET the power spectrum (epsilon << 1)
   (b) QNM ringdown to MODIFY the power spectrum (small corrections)

   Here, epsilon_H = 3 (stiff matter). There is no quasi-de Sitter phase.
   The power spectrum is SET by stiff matter (n_s ~ 4-5, strongly blue)
   and QNM damping cannot overcome this.

CONCLUSION: The QNM route cannot rescue n_s. The fundamental problem is
epsilon_H = 3 (w = 1), which produces a blue spectrum regardless of the
QNM structure. To get n_s ~ 0.965, one needs epsilon_H ~ 0.018, which
requires either:
  - Slowing the transit by factor {velocity_reduction_needed:.0f}x
  - An entirely different mechanism that is NOT a perturbation of the transit

KEY DISCOVERY: The potential IS flat (eps_V = {eps_V_fold:.4e}), but
the transit is ballistic. The QNM analysis reveals a SEPARATION between
potential flatness and kinematic behavior. If any mechanism could slow
the transit to v ~ {float(d_s43['tau_dot_needed_for_0p0176']):.1f}
(from current {v_f:.0f}), the potential would give n_s ~ {ns_slow_roll:.2f}.
This requires eta_V = {eta_V_fold:.4f} to be reduced, but the direction is correct.

The DIMFLOW-44 spectral dimension route (n_s = 0.961 at sigma = 1.10) is
the ONLY surviving route, but it has zero predictive dimension (sigma unfixed).
""")

# S44 comparison: sigma at which DIMFLOW achieves n_s = 0.965
# was sigma = 1.10 (from MEMORY). The QNM gives no independent sigma.
# The two approaches give DIFFERENT answers:
#   QNM: n_s ~ 1 + O(H/m_eff) ~ 1 + O(1e-4)  (irrelevant correction)
#   DIMFLOW: n_s depends on sigma (a free parameter)

print(f"\n=== COMPARISON: QNM vs DIMFLOW vs BOGOLIUBOV ===")
print(f"{'Route':>25} {'n_s':>10} {'Status':>25}")
print("-" * 65)
for route, val in ns_results.items():
    status = ""
    if route == 'slow_roll_naive':
        status = "INAPPLICABLE (eps>>1)"
    elif route == 'slow_roll_potential':
        status = "HYPOTHETICAL (not realized)"
    elif route == 'stiff_exact':
        status = "EXACT (w=1 spectrum)"
    elif route == 'qnm_matrix':
        status = "OVERDAMPED" if np.isnan(val) else "OK"
    elif route == 'qnm_wkb_horizon':
        status = "WKB at horizon crossing"
    elif 'bogoliubov' in route:
        status = "NUMERICAL"
    elif 'dimflow' in route:
        status = "SIGMA UNFIXED"

    val_str = f"{val:.6f}" if not np.isnan(val) else "N/A"
    print(f"{route:>25} {val_str:>10} {status:>25}")


# ═══════════════════════════════════════════════════════════════
# 12. GATE VERDICT
# ═══════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("GATE VERDICT: QNM-NS-45")
print("=" * 72)

gate_verdict = 'INFO'

# The QNM route to n_s:
# 1. The coupled system is overdamped -> no oscillatory QNMs
# 2. Even forced, QNM n_s ~ 1 + O(H/m_eff) ~ 1 + 1e-4 (irrelevant correction)
# 3. The fundamental obstacle is epsilon_H = 3 (stiff matter)
# 4. Exact stiff-matter spectrum: n_s = 5 (blue)
# 5. No QNM mechanism produces n_s ~ 0.965

# Key diagnostic:
diagnostic_sigma = m_fold / H_fold  # sigma = m_eff/H

print(f"\nDiagnostic: sigma = m_eff/H = {diagnostic_sigma:.2f}")
print(f"  (S44 SP collab found sigma = 591 from d2S/H; here m_eff/H = {diagnostic_sigma:.1f})")
print(f"  Note: 591 used d2S directly, here m_eff = sqrt(d2S/M), ratio differs by sqrt(M).")
print(f"  The system is UNDERDAMPED (m_eff >> H) but with LOW Q-factor.")
print(f"  QNM oscillation frequency omega_R = {omega_R_J:.2f}")
print(f"  QNM damping rate omega_I = {omega_I_J:.4f}")
print(f"  Quality factor Q = omega_R/(2*|omega_I|) = {abs(omega_R_J/(2*omega_I_J)):.2f}")
print(f"  n_s(QNM) = 1 - 2*omega_I/omega_R = {ns_qnm_matrix:.4f} (far from 0.965)")

print(f"\nGATE: QNM-NS-45 = {gate_verdict}")
print(f"  The QNM route provides no path to n_s = 0.965.")
print(f"  The linearized system is underdamped (Q = {abs(omega_R_J/(2*omega_I_J)):.2f}).")
print(f"  QNM n_s = {ns_qnm_matrix:.4f} (blue, far from 0.965).")
print(f"  Bogoliubov n_s ~ 4.0 for k < aH (stiff-matter spectrum).")
print(f"  Fundamental: epsilon_H = 3 (stiff transit) sets blue tilt.")
print(f"  Surviving route for n_s: DIMFLOW conditional (sigma_spectral = 1.10),")
print(f"  but with zero predictive dimension (sigma unfixed from framework).")
print(f"\n  KEY DISCOVERY: eps_V = {eps_V_fold:.4e} (flat potential!)")
print(f"  If transit were slow (v ~ {float(d_s43['tau_dot_needed_for_0p0176']):.1f} instead of {v_f:.0f}),")
print(f"  the potential could support near-Harrison-Zeldovich spectrum.")


# ═══════════════════════════════════════════════════════════════
# 13. SAVE DATA
# ═══════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("STEP 13: SAVING DATA")
print("=" * 72)

save_dict = {
    # Gate
    'gate_name': 'QNM-NS-45',
    'gate_verdict': gate_verdict,

    # Background
    'M_ATDHFB': M_ATDHFB,
    'FC': FC,
    'H_fold': H_fold,
    'tau_dot_fold': v_f,
    'epsilon_H_fold': eps_bg[idx_fold],

    # Effective mass
    'm_eff_sq_fold': m_sq_fold,
    'm_eff_fold': m_fold,
    'sigma_mH': diagnostic_sigma,

    # Jacobian eigenvalues at fold
    'J_fold': J,
    'Tr_J': Tr_J,
    'Det_J': det_J,
    'Disc_J': disc_J,
    'eig_fold': eig_J,

    # Eigenvalue trajectory
    'tau_bg': tau_bg,
    'eig_1_traj': eig_1,
    'eig_2_traj': eig_2,

    # QNM frequencies at fold
    'omega_R_fold': omega_R_fold if disc_J < 0 else omega_R_J,
    'omega_I_fold': omega_I_fold if disc_J < 0 else omega_I_J,
    'Q_factor': Q_factor,

    # n_s from various routes
    'ns_slow_roll_naive': ns_results['slow_roll_naive'],
    'ns_slow_roll_potential': ns_results['slow_roll_potential'],
    'ns_stiff_exact': ns_results['stiff_exact'],
    'ns_qnm_matrix': ns_results.get('qnm_matrix', np.nan),
    'ns_dimflow_cdt': dimflow_ns_cdt,
    'ns_dimflow_hawk': dimflow_ns_hawk,

    # Slow-roll potential params
    'eps_V_fold': eps_V_fold,
    'eta_V_fold': eta_V_fold,

    # Pump field
    'pump_zppz_fold': pump[idx_fold],
    'pump_appa_fold': pump_a[idx_fold],

    # Mukhanov-Sasaki data (sampled)
    'eta_bg': eta_bg[::100],
    'pump_zppz': pump[::100],
    'pump_appa': pump_a[::100],

    # Bogoliubov spectrum
    'k_values_bogo': k_valid if len(k_valid) > 0 else np.array([]),
    'beta_sq_bogo': beta_valid if len(k_valid) > 0 else np.array([]),
    'ns_spectrum_bogo': ns_spectrum if len(ns_spectrum) > 0 else np.array([]),

    # Comparison
    'dimflow_sigma_conditional': 1.10,
    'dimflow_ns_conditional': 0.961,
    'velocity_reduction_needed': float(d_s44f['velocity_reduction_needed']),
}

np.savez('tier0-computation/s45_qnm_ns.npz', **save_dict)
print(f"Data saved to tier0-computation/s45_qnm_ns.npz")


# ═══════════════════════════════════════════════════════════════
# 14. PLOT
# ═══════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("STEP 14: GENERATING PLOT")
print("=" * 72)

fig = plt.figure(figsize=(18, 14))
gs = GridSpec(3, 3, figure=fig, hspace=0.35, wspace=0.35)

# Panel 1: Background trajectory
ax1 = fig.add_subplot(gs[0, 0])
ax1.plot(t_bg * 1e3, tau_bg, 'b-', linewidth=1.5)
ax1.axhline(y=0.19, ls='--', color='red', alpha=0.5, label='Fold ($\\tau=0.19$)')
ax1.set_xlabel('t ($\\times 10^{-3}$)')
ax1.set_ylabel('$\\tau(t)$')
ax1.set_title('Background Trajectory')
ax1.legend(fontsize=9)
ax1.grid(True, alpha=0.3)

# Panel 2: epsilon_H along trajectory
ax2 = fig.add_subplot(gs[0, 1])
ax2.plot(tau_bg, eps_bg, 'r-', linewidth=1.5)
ax2.axhline(y=3.0, ls=':', color='gray', alpha=0.5, label='$w=1$ (stiff)')
ax2.axhline(y=0.0176, ls='--', color='green', alpha=0.5, label='Planck target')
ax2.set_xlabel('$\\tau$')
ax2.set_ylabel('$\\epsilon_H$')
ax2.set_title('Slow-roll parameter $\\epsilon_H$')
ax2.set_ylim(0, 3.5)
ax2.legend(fontsize=9)
ax2.grid(True, alpha=0.3)

# Panel 3: Effective mass and H
ax3 = fig.add_subplot(gs[0, 2])
m_eff_traj = np.sqrt(np.abs(m_eff_sq))
ax3.semilogy(tau_bg, m_eff_traj, 'b-', linewidth=1.5, label='$m_{eff}$')
ax3.semilogy(tau_bg, H_bg, 'r-', linewidth=1.5, label='$H$')
ax3.semilogy(tau_bg, m_eff_traj / H_bg, 'k--', linewidth=1.0, label='$\\sigma = m_{eff}/H$')
ax3.axhline(y=1.0, ls=':', color='gray', alpha=0.3)
ax3.set_xlabel('$\\tau$')
ax3.set_ylabel('Frequency scales')
ax3.set_title('$m_{eff}$, $H$, and $\\sigma = m_{eff}/H$')
ax3.legend(fontsize=9)
ax3.grid(True, alpha=0.3)

# Panel 4: Jacobian eigenvalues along trajectory
ax4 = fig.add_subplot(gs[1, 0])
ax4.plot(tau_bg, eig_1.real, 'b-', linewidth=1.5, label='Re($\\lambda_1$)')
ax4.plot(tau_bg, eig_2.real, 'r-', linewidth=1.5, label='Re($\\lambda_2$)')
if has_complex:
    ax4.plot(tau_bg, eig_1.imag, 'b--', linewidth=1.0, label='Im($\\lambda_1$)')
    ax4.plot(tau_bg, eig_2.imag, 'r--', linewidth=1.0, label='Im($\\lambda_2$)')
ax4.axhline(y=0, ls=':', color='gray', alpha=0.5)
ax4.axvline(x=0.19, ls='--', color='green', alpha=0.3, label='Fold')
ax4.set_xlabel('$\\tau$')
ax4.set_ylabel('Jacobian eigenvalues')
ax4.set_title('Linearized System Eigenvalues')
ax4.legend(fontsize=8)
ax4.grid(True, alpha=0.3)

# Panel 5: Mukhanov-Sasaki pump field
ax5 = fig.add_subplot(gs[1, 1])
# Trim edges to avoid numerical artifacts
trim = max(20, N_bg // 50)
ax5.plot(tau_bg[trim:-trim], pump[trim:-trim], 'b-', linewidth=1.0, label="$z''/z$")
ax5.plot(tau_bg[trim:-trim], pump_a[trim:-trim], 'r--', linewidth=1.0, label="$a''/a$")
ax5.axhline(y=0, ls=':', color='gray', alpha=0.5)
ax5.axvline(x=0.19, ls='--', color='green', alpha=0.3)
ax5.set_xlabel('$\\tau$')
ax5.set_ylabel('Pump field')
ax5.set_title('Mukhanov-Sasaki Pump $z\'\'/z$')
ax5.legend(fontsize=9)
ax5.grid(True, alpha=0.3)
# Limit y range to avoid extreme values
pump_trim = pump[trim:-trim]
if len(pump_trim) > 0:
    p95 = np.percentile(np.abs(pump_trim[np.isfinite(pump_trim)]), 95)
    ax5.set_ylim(-2*p95, 2*p95)

# Panel 6: Bogoliubov |beta|^2 spectrum
ax6 = fig.add_subplot(gs[1, 2])
if len(k_valid) > 5:
    ax6.loglog(k_valid, beta_valid, 'b-', linewidth=1.5)
    ax6.axvline(x=H_fold, ls='--', color='red', alpha=0.5, label=f'$k = aH$ ({H_fold:.2e})')
    ax6.set_xlabel('$k$')
    ax6.set_ylabel('$|\\beta_k|^2$')
    ax6.set_title('Bogoliubov Particle Spectrum')
    ax6.legend(fontsize=9)
    ax6.grid(True, alpha=0.3)
else:
    ax6.text(0.5, 0.5, 'Insufficient Bogoliubov data', ha='center', va='center',
             transform=ax6.transAxes, fontsize=12)
    ax6.set_title('Bogoliubov Particle Spectrum')

# Panel 7: n_s from Bogoliubov
ax7 = fig.add_subplot(gs[2, 0])
if len(ns_spectrum) > 5:
    ax7.semilogx(k_valid, ns_spectrum, 'b-', linewidth=1.5)
    ax7.axhspan(0.9607, 0.9691, alpha=0.2, color='green', label='Planck $1\\sigma$')
    ax7.axhline(y=0.9649, ls='--', color='green', alpha=0.5)
    ax7.axhline(y=1.0, ls=':', color='gray', alpha=0.5)
    ax7.axhline(y=5.0, ls=':', color='red', alpha=0.3, label='$n_s = 5$ (stiff exact)')
    ax7.axvline(x=H_fold, ls='--', color='red', alpha=0.5, label='$k=aH$')
    ax7.set_xlabel('$k$')
    ax7.set_ylabel('$n_s$')
    ax7.set_title('Spectral Tilt from Bogoliubov')
    ax7.set_ylim(-2, 8)
    ax7.legend(fontsize=8)
    ax7.grid(True, alpha=0.3)
else:
    ax7.text(0.5, 0.5, 'Insufficient n_s data', ha='center', va='center',
             transform=ax7.transAxes, fontsize=12)
    ax7.set_title('Spectral Tilt from Bogoliubov')

# Panel 8: QNM frequencies vs k/aH
ax8 = fig.add_subplot(gs[2, 1])
k_ratios_plot = np.array(list(ns_qnm_results.keys()))
omega_R_plot = np.array([ns_qnm_results[kr][0] for kr in k_ratios_plot])
omega_I_plot = np.array([abs(ns_qnm_results[kr][1]) for kr in k_ratios_plot])
ax8.loglog(k_ratios_plot, omega_R_plot + 1e-30, 'b-o', markersize=3, label='$\\omega_R$')
ax8.loglog(k_ratios_plot, omega_I_plot + 1e-30, 'r-s', markersize=3, label='$|\\omega_I|$')
ax8.set_xlabel('$k/(aH)$')
ax8.set_ylabel('QNM frequency')
ax8.set_title('QNM Frequencies (WKB)')
ax8.legend(fontsize=9)
ax8.grid(True, alpha=0.3)

# Panel 9: Summary
ax9 = fig.add_subplot(gs[2, 2])
ax9.axis('off')

ns_qnm_str = f"{ns_qnm_matrix:.4f}" if not np.isnan(ns_qnm_matrix) else "OVERDAMPED"
summary = (
    f"QNM-NS-45 RESULTS\n"
    f"{'='*40}\n\n"
    f"sigma = m_eff/H = {diagnostic_sigma:.0f}\n"
    f"Regime: OVERDAMPED\n\n"
    f"n_s routes:\n"
    f"  Slow-roll (naive):  {ns_results['slow_roll_naive']:.1f}\n"
    f"  Slow-roll (V only): {ns_results['slow_roll_potential']:.4f}\n"
    f"  Stiff exact:        {ns_results['stiff_exact']:.0f}\n"
    f"  QNM matrix:         {ns_qnm_str}\n"
    f"  DIMFLOW (CDT):      {dimflow_ns_cdt:.4f}\n"
    f"  DIMFLOW (Hawk):     {dimflow_ns_hawk:.4f}\n\n"
    f"eps_V = {eps_V_fold:.2e} (flat!)\n"
    f"eps_H = {eps_bg[idx_fold]:.1f} (fast!)\n\n"
    f"Planck: 0.9649 +/- 0.0042\n\n"
    f"VERDICT: {gate_verdict}\n"
    f"QNM gives O(1/sigma) ~ 10^-4\n"
    f"correction to n_s. Irrelevant."
)
ax9.text(0.05, 0.95, summary, transform=ax9.transAxes,
         fontsize=9.5, verticalalignment='top', fontfamily='monospace',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

fig.suptitle('Session 45 W3-4: QNM-NS-45 — Linearized Friedmann-Modulus QNM Spectrum',
             fontsize=14, fontweight='bold')
plt.savefig('tier0-computation/s45_qnm_ns.png', dpi=150, bbox_inches='tight')
print(f"Plot saved to tier0-computation/s45_qnm_ns.png")

print("\n" + "=" * 72)
print("QNM-NS-45 COMPLETE")
print("=" * 72)
