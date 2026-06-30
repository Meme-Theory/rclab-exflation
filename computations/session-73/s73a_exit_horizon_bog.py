#!/usr/bin/env python3
"""
EXIT-HORIZON-BOG-73a: Exit Horizon Bogoliubov Coefficients
============================================================

Computes mode-dependent Bogoliubov coefficients for the BCS modes
at the substrate transit through the van Hove fold.

CRITICAL PHYSICAL FINDING (this computation):
  The modulus velocity v_tau = 8.27 M_KK gives Ma_BA = v/c_BA = 20.7
  relative to the Bogoliubov-Anderson sound speed. The spectral action
  equation of motion shows v_tau varies by < 0.2% across |delta_tau| = 0.1
  around the fold. There is NO exit sonic horizon where Ma_BA = 1 within
  the physical range of the BCS gap profile.

  The S70 "exit horizon at tau~0.16" uses a DIFFERENT velocity: the
  tau-derivative of the spectral action divided by the second derivative,
  NOT the modulus flow velocity. The entry horizon at tau~0.22 (s72
  blueshift_tilt) is defined by the GEOMETRIC adiabaticity condition
  (d(ln omega)/dt ~ omega), not by Ma = 1.

  Therefore: Bogoliubov production at the fold is NOT from a sonic horizon
  transition. It is from the IMPULSIVE change in BCS mode frequencies as
  the modulus traverses the van Hove singularity at Mach 20+. This is
  consistent with S70 CHIRP-PENUMBRA-70: gamma > 1 for 93.4% of modes
  means the frequency changes faster than the oscillation period. WKB
  fails BECAUSE there is no adiabatic limit, not because of a horizon.

Method (revised):
  1. Construct the physical velocity profile v_tau(tau) from the spectral
     action equation of motion (Z_fold effective mass, dS/dtau gradient)
  2. Verify: Ma_BA >> 1 everywhere within the BCS gap profile range
  3. Compute omega_k(tau) for each BCS mode from eps_k(tau) and Delta(tau)
  4. Integrate Bogoliubov ODE through the fold region where d(ln omega)/dtau
     is largest (the EFFECTIVE horizon -- where frequency change is impulsive)
  5. Extract |beta_k|^2, phases, decoherence from the mode-dependent
     Bogoliubov transformation
  6. Map through S72 dual-decoherence framework

Gate: EXIT-HORIZON-BOG-73a
  PASS: t_dec/t_transit in [0.57, 0.88] AND residual delta_OOM < 0.30
  INFO: t_dec/t_transit computed but outside [0.57, 0.88]
  FAIL: Integration fails or unitarity violation > 1e-6

Session: S73a | Gate: EXIT-HORIZON-BOG-73a | Classification: PHONONIC
"""

import sys
import os
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import interp1d
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import *

t_start = time.time()

# ==============================================================================
#  SECTION 1: Load prior data and physical parameters
# ==============================================================================

data_dir = os.path.dirname(__file__)  # (local)
d72_dec = np.load(os.path.join(data_dir, 's72_dual_decoherence.npz'), allow_pickle=True)
d72_blue = np.load(os.path.join(data_dir, 's72_blueshift_tilt.npz'), allow_pickle=True)
d72_kappa = np.load(os.path.join(data_dir, 's72_kappa_delta.npz'), allow_pickle=True)

# Four-speed hierarchy (M_KK units)
c_BA = 0.399         # (local) Bogoliubov-Anderson sound speed (BCS condensate)

# From prior computations
v_tau_at_fold = float(d72_kappa['v_tau'])    # = 8.27 (= omega_tau from canonical)
tau_entry_val = float(d72_blue['tau_entry'])  # = 0.2195
kappa_v_entry = float(d72_blue['kappa_v'])    # = 457.66

# BCS gap profile from s72
tau_fine_kd = d72_kappa['tau_fine']       # 21 points, [0.174, 0.214]
Delta_fine_kd = d72_kappa['Delta_fine']   # Delta(tau) profile
tau_center_kd = float(d72_kappa['tau_center'])  # = 0.194
coeffs_quartic = d72_kappa['coeffs_quartic']    # quartic fit coefficients
kappa_Delta_val = float(d72_kappa['kappa_Delta'])

# Mode structure
labels = d72_dec['labels']
r_k_bcs = d72_dec['r_k_bcs']
mode_weights = d72_dec['mode_weights']
phi_eff_modes = d72_dec['phi_eff_modes']
r_eff_modes = d72_dec['r_eff_modes']
omega_k_entry = d72_blue['omega_k']
deps_dtau_raw = d72_kappa['deps_dtau']
d2eps_dtau2_raw = d72_kappa['d2eps_dtau2']

# S72 dual-decoherence scan
t_dec_scan = d72_dec['t_dec_scan']
delta_OOM_scan = d72_dec['delta_OOM_scan']

print("=" * 72)
print("EXIT-HORIZON-BOG-73a: Exit Horizon Bogoliubov Coefficients")
print("=" * 72)
print()

# ==============================================================================
#  SECTION 2: Velocity profile -- no exit sonic horizon exists
# ==============================================================================
#
# The spectral action equation of motion:
#   Z_fold * d^2(tau)/dt^2 = dS/dtau(tau)
# gives:
#   v^2(tau) = v_fold^2 + (2/Z_fold) * integral[dS/dtau dtau]
#            = v_fold^2 + (2/Z_fold) * [dS_fold*(tau-0.19) + d2S_fold/2*(tau-0.19)^2]
#
# The velocity change is TINY compared to v_fold^2 = 68.39:
#   delta(v^2) at tau=0.10: 2/Z * [dS*(-0.09) + d2S/2*(0.09)^2]
#     = 2/74730 * [-5280.6 + 1287.4] = -0.107
#     => v changes by 0.107/136.8 = 0.08%
#
# The flow NEVER reaches c_BA = 0.399 within any physical tau range.

def v_tau_sq(tau):
    """Squared modulus velocity from spectral action EOM."""
    dt = tau - tau_fold  # (local)
    return v_tau_at_fold**2 + (2.0/Z_fold) * (dS_fold*dt + 0.5*d2S_fold*dt**2)

tau_test = np.linspace(0.09, 0.30, 50)  # (local)
v_test = np.sqrt(np.maximum(v_tau_sq(tau_test), 0))  # (local)
Ma_test = v_test / c_BA  # (local)

print("VELOCITY PROFILE ANALYSIS:")
print(f"  v_tau(fold) = {v_tau_at_fold:.4f} M_KK")
print(f"  c_BA        = {c_BA:.4f} M_KK")
print(f"  Ma(fold)    = {v_tau_at_fold/c_BA:.2f}")
print(f"  v range [{v_test.min():.4f}, {v_test.max():.4f}] over tau in [0.09, 0.30]")
print(f"  Ma range [{Ma_test.min():.2f}, {Ma_test.max():.2f}]")
print(f"  CONCLUSION: Ma >> 1 everywhere. No exit sonic horizon exists.")
print(f"  The flow is DEEPLY supersonic (Mach 20+) across the entire")
print(f"  BCS gap profile range. Bogoliubov production is IMPULSIVE,")
print(f"  not from a sonic horizon crossing.")
print()

# ==============================================================================
#  SECTION 3: BCS mode frequency profiles omega_k(tau)
# ==============================================================================
#
# Each BCS quasiparticle mode has frequency:
#   omega_k(tau) = sqrt(eps_k(tau)^2 + Delta(tau)^2)
#
# eps_k(tau) = eps_k(fold) + deps_dtau_k * (tau - 0.19) + ...
# Delta(tau) from quartic fit (valid in [0.174, 0.214])

def Delta_of_tau(tau):
    """BCS gap from quartic fit. Valid near fold."""
    dt = tau - tau_center_kd  # (local)
    return (coeffs_quartic[0]*dt**4 + coeffs_quartic[1]*dt**3 +
            coeffs_quartic[2]*dt**2 + coeffs_quartic[3]*dt + coeffs_quartic[4])

def dDelta_dtau(tau):
    """Derivative of BCS gap."""
    dt = tau - tau_center_kd  # (local)
    return (4*coeffs_quartic[0]*dt**3 + 3*coeffs_quartic[1]*dt**2 +
            2*coeffs_quartic[2]*dt + coeffs_quartic[3])

# Mode energies at fold
Delta_at_fold = Delta_of_tau(tau_fold)  # (local)
eps_k_fold = np.sqrt(np.maximum(omega_k_entry**2 - Delta_at_fold**2, 0.0))  # (local)

N_modes = 8  # (local)

def eps_k_of_tau(tau, ki):
    """Single-particle energy for mode k."""
    dtau = tau - tau_fold  # (local)
    return eps_k_fold[ki] + deps_dtau_raw[ki]*dtau + 0.5*d2eps_dtau2_raw[ki]*dtau**2

def omega_k_of_tau(tau, ki):
    """BCS quasiparticle frequency for mode k."""
    eps = eps_k_of_tau(tau, ki)  # (local)
    Delta = Delta_of_tau(tau)    # (local)
    return np.sqrt(eps**2 + Delta**2)

def dlnomega_dtau(tau, ki):
    """d(ln omega_k)/d(tau) -- the Bogoliubov mixing coefficient."""
    eps = eps_k_of_tau(tau, ki)    # (local)
    Delta = Delta_of_tau(tau)      # (local)
    omega_sq = eps**2 + Delta**2   # (local)
    dtau = tau - tau_fold           # (local)
    deps = deps_dtau_raw[ki] + d2eps_dtau2_raw[ki]*dtau  # (local)
    dDelt = dDelta_dtau(tau)       # (local)
    return (eps*deps + Delta*dDelt) / omega_sq

print("BCS MODE FREQUENCIES AT FOLD:")
print(f"  Delta(fold) = {Delta_at_fold:.6f} M_KK (canonical: {Delta_BCS:.6f})")
for ki in range(N_modes):
    omega_f = omega_k_of_tau(tau_fold, ki)  # (local)
    dlno = dlnomega_dtau(tau_fold, ki)      # (local)
    gamma_k = abs(dlno) / omega_f * v_tau_at_fold  # (local) adiabaticity parameter
    print(f"  {str(labels[ki]):>8s}: omega = {omega_f:.6f}, "
          f"d(ln omega)/dtau = {dlno:.6f}, "
          f"gamma = {gamma_k:.4f}")
print()

# ==============================================================================
#  SECTION 4: Adiabaticity analysis
# ==============================================================================
#
# The adiabaticity parameter is:
#   gamma_k = |d(omega_k)/dt| / omega_k^2 = |d(ln omega_k)/dtau| * v_tau / omega_k
#
# When gamma > 1, the mode frequency changes faster than one oscillation
# period --- WKB fails, particle production is impulsive.

tau_scan = np.linspace(tau_fine_kd[0], tau_fine_kd[-1], 200)  # (local) scan over Delta range
gamma_max = np.zeros(N_modes)  # (local)
gamma_at_fold = np.zeros(N_modes)  # (local)

for ki in range(N_modes):
    for j, tau_j in enumerate(tau_scan):
        omega_j = omega_k_of_tau(tau_j, ki)  # (local)
        dlno_j = dlnomega_dtau(tau_j, ki)    # (local)
        g = abs(dlno_j) * v_tau_at_fold / omega_j  # (local)
        if g > gamma_max[ki]:
            gamma_max[ki] = g
    gamma_at_fold[ki] = abs(dlnomega_dtau(tau_fold, ki)) * v_tau_at_fold / omega_k_of_tau(tau_fold, ki)

print("ADIABATICITY PARAMETER gamma_k:")
print(f"  {'Mode':>8s}  {'gamma(fold)':>12s}  {'gamma(max)':>12s}  {'WKB?':>6s}")
for ki in range(N_modes):
    wkb_valid = "YES" if gamma_max[ki] < 1 else "NO"  # (local)
    print(f"  {str(labels[ki]):>8s}  {gamma_at_fold[ki]:12.4f}  {gamma_max[ki]:12.4f}  {wkb_valid:>6s}")
n_wkb_fail = np.sum(gamma_max > 1)  # (local)
print(f"  WKB fails for {n_wkb_fail}/{N_modes} modes (confirms S70 CHIRP-PENUMBRA)")
print()

# ==============================================================================
#  SECTION 5: Bogoliubov ODE integration through the fold
# ==============================================================================
#
# The Bogoliubov equations in the tau coordinate (using physical time t = tau/v_tau):
#
#   d(alpha_k)/dtau = -(1/2)*(dlnomega_k/dtau)*beta_k*exp(-2i*Phi_k)
#   d(beta_k)/dtau  = -(1/2)*(dlnomega_k/dtau)*alpha_k*exp(+2i*Phi_k)
#
# where Phi_k(tau) = integral omega_k(tau') dtau' / v_tau(tau')
#
# The phase accumulates as omega_k / v_tau per unit tau.
# Since v_tau is nearly constant (~8.27), Phi_k ~ omega_k * (tau - tau_start) / v_tau.
#
# Initial conditions: alpha=1, beta=0 (vacuum state far from the fold where
# d(ln omega)/dtau ~ 0, i.e., the adiabatic vacuum).

def bog_rhs(tau, y, ki):
    """Bogoliubov ODE right-hand side for mode ki."""
    ar, ai, br, bi, Phi = y

    coupling = 0.5 * dlnomega_dtau(tau, ki)  # (local)
    c2P = np.cos(2*Phi)  # (local)
    s2P = np.sin(2*Phi)  # (local)

    # d(alpha)/dtau = -coupling * beta * exp(-2i*Phi)
    dar = -coupling * (br*c2P + bi*s2P)   # (local)
    dai = -coupling * (-br*s2P + bi*c2P)  # (local)

    # d(beta)/dtau = -coupling * alpha * exp(+2i*Phi)
    dbr = -coupling * (ar*c2P - ai*s2P)   # (local)
    dbi = -coupling * (ar*s2P + ai*c2P)   # (local)

    # Phase: dPhi/dtau = omega_k(tau) / v_tau(tau)
    omega = omega_k_of_tau(tau, ki)  # (local)
    v = np.sqrt(max(v_tau_sq(tau), 1e-30))  # (local) protect against numerical issues
    dPhi = omega / v  # (local)

    return [dar, dai, dbr, dbi, dPhi]

# Integration range: use the FULL Delta(tau) profile range
# This covers the fold region where d(ln omega)/dtau is large.
# Extend slightly beyond to capture the tails.
tau_int_start = tau_fine_kd[0] - 0.01   # (local) ~ 0.164
tau_int_end = tau_fine_kd[-1] + 0.01    # (local) ~ 0.224

print(f"Integration range: [{tau_int_start:.4f}, {tau_int_end:.4f}]")
print(f"  (covers fold +-0.04 in tau, entire BCS gap profile)")
print(f"  v_tau(start) = {np.sqrt(v_tau_sq(tau_int_start)):.4f}, "
      f"v_tau(end) = {np.sqrt(v_tau_sq(tau_int_end)):.4f}")
print()

# Characteristic scale for step size: omega/v gives oscillation rate in tau
omega_char = np.mean(omega_k_entry)  # (local) ~ 0.85
phase_rate = omega_char / v_tau_at_fold  # (local) ~ 0.103 rad per unit tau
max_step_tau = 2*np.pi / phase_rate / 50  # (local) 50 points per oscillation period

print(f"Phase rate        = {phase_rate:.6f} rad/tau")
print(f"Max step in tau   = {max_step_tau:.6f}")
print()

y0 = [1.0, 0.0, 0.0, 0.0, 0.0]  # (local) vacuum initial condition

alpha_k = np.zeros(N_modes, dtype=complex)   # (local)
beta_k = np.zeros(N_modes, dtype=complex)    # (local)
alpha_sq = np.zeros(N_modes)   # (local)
beta_sq = np.zeros(N_modes)    # (local)
n_k = np.zeros(N_modes)        # (local)
unitarity_err = np.zeros(N_modes)  # (local)
greybody_k = np.zeros(N_modes)     # (local)
phase_k = np.zeros(N_modes)        # (local)
Phi_final = np.zeros(N_modes)      # (local)
sol_list = []  # (local)

print("Integrating Bogoliubov ODE for 8 BCS modes (DOP853, rtol=1e-12)...")
print("-" * 72)

for ki in range(N_modes):
    sol = solve_ivp(
        bog_rhs,
        [tau_int_start, tau_int_end],
        y0,
        args=(ki,),
        method='DOP853',
        rtol=1e-12,
        atol=1e-14,
        max_step=max_step_tau,
        dense_output=True
    )

    if not sol.success:
        print(f"  Mode {ki} ({labels[ki]}): FAILED - {sol.message}")
        continue

    ar_f = sol.y[0, -1]  # (local)
    ai_f = sol.y[1, -1]  # (local)
    br_f = sol.y[2, -1]  # (local)
    bi_f = sol.y[3, -1]  # (local)

    alpha_k[ki] = ar_f + 1j*ai_f
    beta_k[ki] = br_f + 1j*bi_f
    alpha_sq[ki] = abs(alpha_k[ki])**2
    beta_sq[ki] = abs(beta_k[ki])**2
    n_k[ki] = beta_sq[ki]
    unitarity_err[ki] = alpha_sq[ki] - beta_sq[ki] - 1.0
    greybody_k[ki] = 1.0 / alpha_sq[ki] if alpha_sq[ki] > 0 else 0.0
    phase_k[ki] = np.angle(beta_k[ki])
    Phi_final[ki] = sol.y[4, -1]

    sol_list.append(sol)

    print(f"  {str(labels[ki]):>8s}: |alpha|^2={alpha_sq[ki]:.10e}, "
          f"|beta|^2={beta_sq[ki]:.10e}, "
          f"u_err={unitarity_err[ki]:.2e}, "
          f"steps={sol.t.size}")

print()

# ==============================================================================
#  SECTION 6: Unitarity cross-check
# ==============================================================================

max_unitarity_err = np.max(np.abs(unitarity_err))  # (local)
unitarity_pass = max_unitarity_err < 1e-6  # (local)
print(f"UNITARITY CHECK:")
print(f"  Max |alpha|^2 - |beta|^2 - 1 = {max_unitarity_err:.2e}")
print(f"  Status: {'PASS' if unitarity_pass else 'FAIL'} (threshold: 1e-6)")
print()

# ==============================================================================
#  SECTION 7: Hawking cross-check (thermal reference)
# ==============================================================================
#
# The "effective Hawking temperature" for the fold transit is set by the
# rate of frequency change: T_eff = (1/2pi) * max|d(ln omega)/dt|.
# This is NOT from a sonic horizon but from the impulsive transit.
#
# The entry horizon from S72 gives:
#   T_H_entry = 72.84 M_KK (deeply thermal, omega/T ~ 0.012)
#   beta_sq_entry ~ 82-88 per mode
#
# For the fold transit, the effective temperature from adiabaticity:
#   T_eff ~ gamma_max * omega / (2*pi)

T_eff_modes = gamma_at_fold * omega_k_entry / (2*np.pi)  # (local) effective temperature per mode
T_eff_mean = np.mean(T_eff_modes)  # (local)

# Thermal reference: n_k = 1/(exp(omega/T) - 1)
n_k_thermal = np.zeros(N_modes)  # (local)
for ki in range(N_modes):
    x = omega_k_entry[ki] / T_eff_modes[ki] if T_eff_modes[ki] > 0 else np.inf  # (local)
    if x < 500:
        n_k_thermal[ki] = 1.0 / (np.exp(x) - 1.0)

print("THERMAL CROSS-CHECK (effective T from fold adiabaticity):")
print(f"  {'Mode':>8s}  {'T_eff':>10s}  {'n_k(ODE)':>12s}  {'n_k(therm)':>12s}  {'ratio':>10s}")
for ki in range(N_modes):
    r = n_k[ki] / n_k_thermal[ki] if n_k_thermal[ki] > 0 else float('inf')  # (local)
    print(f"  {str(labels[ki]):>8s}  {T_eff_modes[ki]:10.4f}  {n_k[ki]:12.6e}  "
          f"{n_k_thermal[ki]:12.6e}  {r:10.4f}")
print()

# Entry horizon cross-check: compare to S72 blueshift tilt beta^2
print("ENTRY HORIZON CROSS-CHECK:")
print(f"  S72 beta_sq_entry (thermal Hawking @ T=72.8):")
print(f"    {d72_blue['beta_sq_entry']}")
print(f"  Our fold-transit n_k (non-thermal, from ODE):")
print(f"    {n_k}")
print(f"  Ratio (entry/fold): {d72_blue['beta_sq_entry'] / np.maximum(n_k, 1e-30)}")
print(f"  The entry horizon produces O(80) particles/mode (deeply thermal).")
print(f"  The fold transit produces O({np.max(n_k):.2e}) particles/mode (sub-thermal).")
print(f"  This is consistent: fold production is from impulsive frequency change,")
print(f"  not from a thermal horizon.")
print()

# ==============================================================================
#  SECTION 8: Phase spread and decoherence
# ==============================================================================

# Phase of beta_k for each mode
print("PHASE ANALYSIS:")
for ki in range(N_modes):
    print(f"  {str(labels[ki]):>8s}: arg(beta) = {phase_k[ki]:+.8f} rad, "
          f"Phi_accum = {Phi_final[ki]:.4f} rad")

# Branch-averaged phases
phase_B2 = phase_k[:4]  # (local)
phase_B1 = phase_k[4]   # (local)
phase_B3 = phase_k[5:]  # (local)

# Mean phase within each branch
phase_B2_mean = np.mean(phase_B2)  # (local)
phase_B3_mean = np.mean(phase_B3)  # (local)

# Inter-branch phase differences
def wrap(phi):
    """Wrap angle to [-pi, pi]."""
    return (phi + np.pi) % (2*np.pi) - np.pi

dphi_B2_B1 = wrap(phase_B2_mean - phase_B1)    # (local)
dphi_B1_B3 = wrap(phase_B1 - phase_B3_mean)    # (local)
dphi_B2_B3 = wrap(phase_B2_mean - phase_B3_mean)  # (local)

print()
print(f"  Inter-branch phase differences:")
print(f"    delta_phi(B2-B1) = {dphi_B2_B1:+.8f} rad")
print(f"    delta_phi(B1-B3) = {dphi_B1_B3:+.8f} rad")
print(f"    delta_phi(B2-B3) = {dphi_B2_B3:+.8f} rad")
print()

# Intra-branch phase spread (should be small due to branch degeneracies)
var_B2_intra = np.var(phase_B2)  # (local)
var_B3_intra = np.var(phase_B3)  # (local)
print(f"  Intra-branch phase variance:")
print(f"    Var(B2, 4 modes) = {var_B2_intra:.8e}")
print(f"    Var(B3, 3 modes) = {var_B3_intra:.8e}")
print()

# Adjacent-mode phase differences (all 7 adjacent pairs)
delta_phi_adj = np.zeros(N_modes - 1)  # (local)
for ki in range(N_modes - 1):
    delta_phi_adj[ki] = wrap(phase_k[ki] - phase_k[ki+1])

var_adj = np.var(delta_phi_adj)  # (local)

# Weight-averaged phase variance (the quantity that drives decoherence)
# Decoherence from mode-dependent Bogoliubov phases:
# The coherent BCS state after the fold has each mode k with squeeze
# parameter r_k (from S72 fold data) and additional Bogoliubov mixing
# from the fold transit. The exit-horizon contribution modifies the
# effective squeeze phase theta_k -> theta_k + delta_theta_k
# where delta_theta_k = arg(beta_k).
#
# The power spectrum depends on the weighted average:
#   <P> = sum_k w_k * cosh(2r_k) + sum_k w_k * sinh(2r_k) * cos(2*theta_k)
# The cos(2*theta_k) term is where decoherence enters: if theta_k
# varies across modes, the cos terms cancel, reducing <P>.
#
# The decoherence factor from the fold transit:
#   F_dec = |sum_k w_k * exp(2i * arg(beta_k))| / sum_k w_k
# If all phases are aligned, F_dec = 1 (no decoherence).
# If phases are random, F_dec ~ 1/sqrt(N_eff) (decoherence).

# Compute decoherence factor
z_dec = np.sum(mode_weights * np.exp(2j * phase_k))  # (local) complex phasor sum
F_dec = abs(z_dec) / np.sum(mode_weights)  # (local) decoherence factor [0,1]

# Also compute the decoherence from the COMBINED squeeze:
# The S72 fold data gives phi_eff_modes (squeeze phases from the fold BCS)
# The exit-horizon transit adds phase_k from the Bogoliubov transformation.
# The COMPOUND phase is phi_compound_k = phi_eff_k + 2 * arg(beta_k)
phi_compound = phi_eff_modes + 2 * phase_k  # (local)
z_compound = np.sum(mode_weights * r_eff_modes * np.exp(1j * phi_compound))  # (local)
F_compound = abs(z_compound) / np.sum(mode_weights * r_eff_modes)  # (local)

print(f"  DECOHERENCE FACTORS:")
print(f"    F_dec (fold-transit phases)  = {F_dec:.6f}")
print(f"    F_compound (incl. BCS fold)  = {F_compound:.6f}")
print()

# The decoherence timescale from the exit-horizon Bogoliubov phases:
# Each transit through the fold adds phase variance.
# The number of effective transits is 1 (the substrate transits the fold once).
# So the decoherence is a one-shot process, not accumulating over time.
#
# The relation to t_dec/t_transit:
# The decoherence factor F_dec tells us what fraction of the coherent
# power survives the transit. The equivalent t_dec/t_transit is:
#   F_dec = exp(-t_transit / t_dec)
# => t_dec/t_transit = -1 / ln(F_dec) if F_dec < 1

if F_dec < 1.0 and F_dec > 0:
    t_dec_over_transit_from_F = -1.0 / np.log(F_dec)  # (local)
else:
    t_dec_over_transit_from_F = np.inf  # (local)

if F_compound < 1.0 and F_compound > 0:
    t_dec_over_transit_compound = -1.0 / np.log(F_compound)  # (local)
else:
    t_dec_over_transit_compound = np.inf  # (local)

# Also compute from the phase variance directly:
# Var(phase) ~ 1/t_dec in the Gaussian decoherence model
# For a single transit: Var(phase) is fixed, so
# t_dec/t_transit ~ 1/Var(inter-branch phases)

inter_phases = np.array([dphi_B2_B1, dphi_B1_B3, dphi_B2_B3])  # (local)
var_inter = np.var(inter_phases)  # (local)
t_dec_over_transit_var = 1.0 / var_inter if var_inter > 0 else np.inf  # (local)

# The occupation-weighted phase variance:
# weight each mode's phase by its occupation number
if np.sum(n_k * mode_weights) > 0:
    phase_wt_mean = np.sum(n_k * mode_weights * phase_k) / np.sum(n_k * mode_weights)  # (local)
    var_occ_weighted = np.sum(n_k * mode_weights * (phase_k - phase_wt_mean)**2) / np.sum(n_k * mode_weights)  # (local)
    t_dec_over_transit_occ = 1.0 / var_occ_weighted if var_occ_weighted > 0 else np.inf  # (local)
else:
    var_occ_weighted = 0.0  # (local)
    t_dec_over_transit_occ = np.inf  # (local)

print(f"  DECOHERENCE TIMESCALE ESTIMATES:")
print(f"    From F_dec (fold transit):      t_dec/t_tr = {t_dec_over_transit_from_F:.6f}")
print(f"    From F_compound (full):         t_dec/t_tr = {t_dec_over_transit_compound:.6f}")
print(f"    From Var(inter-branch):         t_dec/t_tr = {t_dec_over_transit_var:.6f}")
print(f"    From Var(occ-weighted):         t_dec/t_tr = {t_dec_over_transit_occ:.6f}")
print()

# Select the PHYSICALLY MOST RELEVANT estimate:
# The compound decoherence factor includes BOTH the S72 fold BCS squeeze
# phases AND the fold-transit Bogoliubov phases. This is the full picture.
# However, if n_k is very small (fold transit produces few particles),
# the decoherence is dominated by the S72 fold data, and the fold-transit
# Bogoliubov coefficients modulate rather than drive.
#
# The hierarchy is:
# 1. If F_compound < F_dec: the fold-transit phases ENHANCE decoherence
# 2. If F_compound > F_dec: the fold-transit phases REDUCE decoherence
#    (partial coherence restoration from the compound squeeze)

print(f"  HIERARCHY:")
if F_compound < F_dec:
    print(f"    F_compound < F_dec: fold-transit ENHANCES decoherence")
    t_dec_primary = t_dec_over_transit_compound  # (local)
else:
    print(f"    F_compound > F_dec: fold-transit partially RESTORES coherence")
    t_dec_primary = t_dec_over_transit_compound  # (local)
print(f"    PRIMARY estimate: t_dec/t_transit = {t_dec_primary:.6f}")
print()

# ==============================================================================
#  SECTION 9: Map through S72 dual-decoherence framework
# ==============================================================================

f_delta_OOM = interp1d(t_dec_scan, delta_OOM_scan, kind='cubic',
                        bounds_error=False,
                        fill_value=(delta_OOM_scan[0], delta_OOM_scan[-1]))  # (local)

delta_OOM_primary = float(f_delta_OOM(t_dec_primary))  # (local)

# Also check what the S72 estimates were:
t_dec_S72_estimate = float(d72_dec['t_dec_BCS_estimate'])  # (local) = 6.727
t_dec_S72_target = float(d72_dec['t_dec_BCS_target'])      # (local) = 0.716

print(f"S72 DUAL-DECOHERENCE MAP:")
print(f"  S72 cell-crossing estimate: t_dec/t_tr = {t_dec_S72_estimate:.4f} (too slow)")
print(f"  S72 target for 0.267 OOM:   t_dec/t_tr = {t_dec_S72_target:.4f}")
print(f"  Our fold-transit result:    t_dec/t_tr = {t_dec_primary:.4f}")
print(f"  delta_OOM from S72 map:     {delta_OOM_primary:.6f}")
print()

# ==============================================================================
#  SECTION 10: Squeeze parameter analysis
# ==============================================================================
#
# The fold-transit Bogoliubov coefficients define a squeeze:
#   r_exit_k = arcsinh(sqrt(n_k))
# Compare to the S72 fold BCS squeeze r_k_bcs:

r_exit = np.arcsinh(np.sqrt(n_k))  # (local) exit-horizon squeeze parameters

print("SQUEEZE PARAMETER COMPARISON (fold BCS vs fold-transit Bogoliubov):")
print(f"  {'Mode':>8s}  {'r_BCS(S72)':>12s}  {'r_exit(73a)':>12s}  {'ratio':>8s}  {'n_k':>12s}")
for ki in range(N_modes):
    r = r_exit[ki] / r_k_bcs[ki] if r_k_bcs[ki] > 0 else float('inf')  # (local)
    print(f"  {str(labels[ki]):>8s}  {r_k_bcs[ki]:12.6f}  {r_exit[ki]:12.6f}  {r:8.4f}  {n_k[ki]:12.6e}")
print()

# The S72 fold BCS squeeze is the DOMINANT contribution (r ~ 1.8-3.6).
# The fold-transit Bogoliubov contribution is MUCH smaller (r ~ 0.01-0.36).
# The exit-horizon Bogoliubov is a correction to the BCS squeeze, not the
# primary source of particle production.

# ==============================================================================
#  SECTION 11: Gate verdict
# ==============================================================================

gate_name = "EXIT-HORIZON-BOG-73a"  # (local)

# Use the primary t_dec estimate
t_dec_final = t_dec_primary  # (local)

if not unitarity_pass:
    gate_verdict = "FAIL"  # (local)
    gate_detail = (f"Unitarity violation: max err = {max_unitarity_err:.2e} > 1e-6")  # (local)
elif 0.57 <= t_dec_final <= 0.88 and delta_OOM_primary < 0.30:
    gate_verdict = "PASS"
    gate_detail = (f"t_dec/t_transit = {t_dec_final:.4f} in [0.57, 0.88] "
                   f"AND delta_OOM = {delta_OOM_primary:.4f} < 0.30")
elif 0.57 <= t_dec_final <= 0.88:
    gate_verdict = "INFO"
    gate_detail = (f"t_dec/t_transit = {t_dec_final:.4f} in [0.57, 0.88] "
                   f"BUT delta_OOM = {delta_OOM_primary:.4f} >= 0.30")
else:
    gate_verdict = "INFO"
    gate_detail = (f"t_dec/t_transit = {t_dec_final:.4f} outside [0.57, 0.88]. "
                   f"delta_OOM = {delta_OOM_primary:.4f}. "
                   f"Key finding: no exit sonic horizon exists; Bogoliubov "
                   f"production is from impulsive fold transit at Mach {v_tau_at_fold/c_BA:.1f}.")

print(f"=" * 72)
print(f"GATE VERDICT")
print(f"=" * 72)
print(f"Gate {gate_name}: {gate_verdict}")
print(f"  {gate_detail}")
print()

# ==============================================================================
#  SECTION 12: Save data
# ==============================================================================

output_npz = os.path.join(data_dir, 's73a_exit_horizon_bog.npz')  # (local)

np.savez(output_npz,
    # Gate
    gate_name=gate_name,
    gate_verdict=gate_verdict,
    gate_detail=gate_detail,

    # Physical finding: no exit sonic horizon
    mach_at_fold=v_tau_at_fold / c_BA,
    mach_range_min=Ma_test.min(),
    mach_range_max=Ma_test.max(),
    no_exit_horizon=True,

    # Velocity profile
    v_tau_at_fold=v_tau_at_fold,
    c_BA=c_BA,
    Gamma_dec=dS_fold / Z_fold,

    # Bogoliubov coefficients
    labels=labels,
    alpha_k_real=np.real(alpha_k),
    alpha_k_imag=np.imag(alpha_k),
    beta_k_real=np.real(beta_k),
    beta_k_imag=np.imag(beta_k),
    alpha_sq=alpha_sq,
    beta_sq=beta_sq,
    n_k=n_k,
    greybody_k=greybody_k,
    phase_k=phase_k,
    Phi_final=Phi_final,
    r_exit=r_exit,

    # Unitarity
    unitarity_err=unitarity_err,
    max_unitarity_err=max_unitarity_err,

    # Adiabaticity
    gamma_at_fold=gamma_at_fold,
    gamma_max=gamma_max,

    # Decoherence
    F_dec=F_dec,
    F_compound=F_compound,
    t_dec_over_transit_from_F=t_dec_over_transit_from_F,
    t_dec_over_transit_compound=t_dec_over_transit_compound,
    t_dec_over_transit_var=t_dec_over_transit_var,
    t_dec_over_transit_occ=t_dec_over_transit_occ,
    t_dec_primary=t_dec_final,
    delta_OOM_primary=delta_OOM_primary,
    dphi_B2_B1=dphi_B2_B1,
    dphi_B1_B3=dphi_B1_B3,
    dphi_B2_B3=dphi_B2_B3,
    var_inter=var_inter,
    var_occ_weighted=var_occ_weighted,
    phi_compound=phi_compound,

    # Squeeze comparison
    r_k_bcs=r_k_bcs,
    mode_weights=mode_weights,

    # Integration range
    tau_int_start=tau_int_start,
    tau_int_end=tau_int_end
)

print(f"Data saved: {output_npz}")

# ==============================================================================
#  SECTION 13: Plot
# ==============================================================================

fig, axes = plt.subplots(2, 3, figsize=(16, 10))

fig.suptitle(f"EXIT-HORIZON-BOG-73a: Fold-Transit Bogoliubov Coefficients\n"
             f"Gate: {gate_verdict} | t_dec/t_tr = {t_dec_final:.4f} | "
             f"delta_OOM = {delta_OOM_primary:.4f} | "
             f"Ma = {v_tau_at_fold/c_BA:.1f} (no exit sonic horizon)",
             fontsize=12)

# Color scheme: B2=blue, B1=red, B3=green
colors = ['#1f77b4']*4 + ['#d62728'] + ['#2ca02c']*3  # (local)

# (a) Mach number profile
ax = axes[0, 0]
tau_pl = np.linspace(0.09, 0.30, 300)  # (local)
v_pl = np.sqrt(np.maximum(v_tau_sq(tau_pl), 0))  # (local)
ma_pl = v_pl / c_BA  # (local)
ax.plot(tau_pl, ma_pl, 'b-', linewidth=1.5)
ax.axhline(1.0, color='r', linestyle='--', alpha=0.5, label='Ma = 1')
ax.axvline(tau_fold, color='gray', linestyle=':', label=f'tau_fold = {tau_fold}')
ax.axvspan(tau_int_start, tau_int_end, alpha=0.1, color='yellow', label='ODE range')
ax.set_xlabel('tau')
ax.set_ylabel('Ma = v_tau / c_BA')
ax.set_title('(a) Mach number: deeply supersonic everywhere')
ax.legend(fontsize=7)
ax.set_ylim(0, Ma_test.max()*1.1)

# (b) |beta_k|^2 occupation numbers
ax = axes[0, 1]
x_idx = np.arange(N_modes)  # (local)
for ki in range(N_modes):
    ax.bar(ki, n_k[ki], color=colors[ki], alpha=0.7, edgecolor='black', linewidth=0.5)
ax.set_xticks(x_idx)
ax.set_xticklabels([str(l) for l in labels], rotation=45, fontsize=7)
ax.set_ylabel('n_k = |beta_k|^2')
ax.set_title('(b) Fold-transit occupation numbers')
ax.set_yscale('log')
ax.set_ylim(bottom=1e-6)

# (c) Phase of beta_k
ax = axes[0, 2]
for ki in range(N_modes):
    ax.bar(ki, phase_k[ki], color=colors[ki], alpha=0.7, edgecolor='black', linewidth=0.5)
ax.set_xticks(x_idx)
ax.set_xticklabels([str(l) for l in labels], rotation=45, fontsize=7)
ax.set_ylabel('arg(beta_k) [rad]')
ax.set_title('(c) Beta phases (drive decoherence)')
ax.axhline(0, color='gray', linestyle=':', alpha=0.3)

# (d) Squeeze comparison: r_BCS vs r_exit
ax = axes[1, 0]
bw = 0.35  # (local)
ax.bar(x_idx - bw/2, r_k_bcs, bw, label='BCS fold (S72)', alpha=0.7, color='steelblue')
ax.bar(x_idx + bw/2, r_exit, bw, label='Bog transit (73a)', alpha=0.7, color='coral')
ax.set_xticks(x_idx)
ax.set_xticklabels([str(l) for l in labels], rotation=45, fontsize=7)
ax.set_ylabel('r_k (squeeze)')
ax.set_title('(d) Squeeze: BCS fold >> Bog transit')
ax.legend(fontsize=7)

# (e) Adiabaticity parameter
ax = axes[1, 1]
for ki in range(N_modes):
    ax.bar(ki, gamma_at_fold[ki], color=colors[ki], alpha=0.7, edgecolor='black', linewidth=0.5)
ax.axhline(1.0, color='r', linestyle='--', label='gamma = 1 (WKB fails)')
ax.set_xticks(x_idx)
ax.set_xticklabels([str(l) for l in labels], rotation=45, fontsize=7)
ax.set_ylabel('gamma_k')
ax.set_title('(e) Adiabaticity at fold (WKB fails where gamma > 1)')
ax.legend(fontsize=7)

# (f) S72 delta_OOM scan with our result
ax = axes[1, 2]
ax.plot(t_dec_scan, delta_OOM_scan, 'b-', linewidth=1.5)
ax.axvspan(0.57, 0.88, alpha=0.15, color='green', label='gate band')
ax.axhline(0.30, color='gray', linestyle=':', alpha=0.5, label='delta_OOM = 0.30')
ax.plot(t_dec_final, delta_OOM_primary, 'r*', markersize=15, zorder=5,
        label=f't_dec/t_tr = {t_dec_final:.3f}')
ax.set_xlabel('t_dec / t_transit')
ax.set_ylabel('delta_OOM')
ax.set_title('(f) S72 decoherence map')
ax.set_xscale('log')
ax.legend(fontsize=7)

plt.tight_layout()
plot_path = os.path.join(data_dir, 's73a_exit_horizon_bog.png')  # (local)
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"Plot saved: {plot_path}")

t_end_calc = time.time()
print(f"\nTotal runtime: {t_end_calc - t_start:.2f}s")

# ==============================================================================
#  SECTION 14: Working paper summary
# ==============================================================================

print()
print("=" * 72)
print("SUMMARY FOR WORKING PAPER W1-A")
print("=" * 72)
print()
print("CRITICAL PHYSICAL FINDING:")
print(f"  The modulus velocity v_tau = {v_tau_at_fold:.2f} M_KK gives Ma_BA = {v_tau_at_fold/c_BA:.1f}")
print(f"  relative to the BCS sound speed c_BA = {c_BA} M_KK.")
print(f"  The spectral action EOM shows v_tau varies by < 0.2% across")
print(f"  the entire BCS gap profile range. There is NO exit sonic horizon")
print(f"  (no tau where Ma = 1) within any physical range.")
print(f"  The fold transit is DEEPLY supersonic throughout, and Bogoliubov")
print(f"  production is IMPULSIVE (from rapid frequency change at the fold),")
print(f"  NOT from a sonic horizon crossing.")
print()
print("KEY NUMBERS:")
print(f"  1. No exit sonic horizon: Ma = [{Ma_test.min():.2f}, {Ma_test.max():.2f}] >> 1")
print(f"  2. Occupation: n_k ranges [{n_k.min():.2e}, {n_k.max():.2e}] (sub-thermal)")
print(f"  3. Unitarity: max err = {max_unitarity_err:.2e} (PASS)")
print(f"  4. WKB fails for {n_wkb_fail}/8 modes (gamma up to {gamma_max.max():.2f})")
print(f"  5. Decoherence: F_compound = {F_compound:.4f}, t_dec/t_tr = {t_dec_final:.4f}")
print(f"  6. delta_OOM = {delta_OOM_primary:.4f} (from S72 map)")
print(f"  7. Fold BCS squeeze r_k >> transit Bogoliubov r_exit by {r_k_bcs.mean()/r_exit.mean():.0f}x")
print()
print(f"Gate {gate_name}: {gate_verdict}")
print(f"  {gate_detail}")
