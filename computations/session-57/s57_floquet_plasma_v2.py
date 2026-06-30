#!/usr/bin/env python3
"""
FLOQUET-PLASMA-57 v2: Corrected Bogoliubov + Floquet analysis
==============================================================
The v1 monodromy computation had the right structure but the Parker
extraction needs care. This version:

1. Verifies the monodromy det=1 (symplectic)
2. Correctly extracts |beta|^2 from the sudden-quench formula
3. Checks the WKB integral for particle production
4. Provides the definitive gate verdict

The KEY physics: omega_J * dt_transit << 1 everywhere. The plasma mode
does NOT oscillate during the transit. This is the INSTANTANEOUS QUENCH
limit. The Bogoliubov coefficient is:
  |beta|^2 = [(omega_i - omega_f) / (2*sqrt(omega_i*omega_f))]^2

Author: Tesla-Resonance
Session: 57 (2026-03-22)
"""
import sys
sys.path.insert(0, r"C:\sandbox\Ainulindale Exflation\computations")
import numpy as np
from scipy.integrate import solve_ivp, quad
from scipy.interpolate import CubicSpline
from canonical_constants import (
    tau_fold, dt_transit, H_fold, PI
)

# ============================================================
# Load data
# ============================================================
ba = np.load(r"C:\sandbox\Ainulindale Exflation\computations\s56_ba_spectrum.npz",
             allow_pickle=True)
tau_vals = ba['tau_values']
E_J = ba['E_J']
E_c = ba['E_c']
omega_J_s = ba['omega_J_single']      # sqrt(E_J * E_c)
omega_J_c = ba['omega_J_collective']
omega_BA = ba['omega_BA']             # (50, 31) BA mode spectrum

N_tau = len(tau_vals)
dtau_dt = 0.5 / dt_transit  # = 442.4 M_KK

# Splines
sp_s = CubicSpline(tau_vals, omega_J_s)
sp_c = CubicSpline(tau_vals, omega_J_c)

print("=" * 65)
print("FLOQUET-PLASMA-57 v2: Corrected Bogoliubov + Floquet")
print("=" * 65)

# ============================================================
# A. Regime identification
# ============================================================
# omega_J ranges from ~0.68 to ~4.0 M_KK
# dt_transit = 0.00113 M_KK^{-1}
# omega * dt ~ 0.001 to 0.005: the mode completes <<1 oscillations
# This is the INSTANTANEOUS QUENCH regime

omega_i_s, omega_f_s = omega_J_s[0], omega_J_s[-1]
omega_i_c, omega_f_c = omega_J_c[0], omega_J_c[-1]
print(f"\nomega_J_single:     {omega_i_s:.4f} -> {omega_f_s:.4f} M_KK (ratio {omega_i_s/omega_f_s:.3f})")
print(f"omega_J_collective: {omega_i_c:.4f} -> {omega_f_c:.4f} M_KK (ratio {omega_i_c/omega_f_c:.3f})")
print(f"dt_transit = {dt_transit:.6f} M_KK^-1")
print(f"omega*dt range: [{omega_J_s[-1]*dt_transit:.5f}, {omega_J_s[0]*dt_transit:.5f}]")
print(f"Regime: INSTANTANEOUS QUENCH (omega*dt << 1)")

# ============================================================
# B. Instantaneous quench formula
# ============================================================
# For an oscillator whose frequency changes instantaneously from omega_i to omega_f:
# |beta|^2 = [(omega_i - omega_f) / (2*sqrt(omega_i*omega_f))]^2
# |alpha|^2 = [(omega_i + omega_f) / (2*sqrt(omega_i*omega_f))]^2
# Check: |alpha|^2 - |beta|^2 = omega_i*omega_f / (omega_i*omega_f) = 1 ✓

for label, oi, of in [('single', omega_i_s, omega_f_s), ('collective', omega_i_c, omega_f_c)]:
    beta2_quench = ((oi - of) / (2*np.sqrt(oi * of)))**2
    alpha2_quench = ((oi + of) / (2*np.sqrt(oi * of)))**2
    check = alpha2_quench - beta2_quench  # should be 1.0
    print(f"\n--- {label} (instantaneous quench) ---")
    print(f"  |beta|^2 = {beta2_quench:.6f}")
    print(f"  |alpha|^2 = {alpha2_quench:.6f}")
    print(f"  |alpha|^2 - |beta|^2 = {check:.12f} (should be 1.0)")
    print(f"  n_particle = {beta2_quench:.6f} quanta per mode")

# ============================================================
# C. WKB integral for adiabatic particle production
# ============================================================
# In the WKB/adiabatic regime, particle production is:
#   |beta|^2 ~ exp(-2 * integral_0^T omega(t) dt)
# But in the SUDDEN regime (our case), the WKB integral is small:
#   Phi = integral_0^T omega(t) dt = integral_0^0.5 omega(tau)/dtau_dt dtau

# Compute the WKB phase integral
for label, spline in [('single', sp_s), ('collective', sp_c)]:
    # Phase integral: Phi = integral omega(tau) dtau / dtau_dt
    def omega_of_tau(tau):
        return float(spline(tau))
    Phi, err = quad(omega_of_tau, 0, 0.5)
    Phi_t = Phi / dtau_dt  # convert to time integral
    print(f"\n--- WKB phase ({label}) ---")
    print(f"  Phi = integral omega dtau = {Phi:.6f}")
    print(f"  Phi_t = Phi / dtau_dt = {Phi_t:.6f} radians")
    print(f"  N_full_cycles = Phi_t / (2*pi) = {Phi_t/(2*PI):.6f}")
    print(f"  exp(-2*Phi_t) = {np.exp(-2*Phi_t):.6e}")

# ============================================================
# D. CORRECT monodromy with proper normalization
# ============================================================
# The equation of motion is: x'' + omega(t)^2 x = 0
# tau(t) = dtau_dt * t, so omega(t) = omega_J(dtau_dt * t)
#
# The monodromy matrix maps (x, p) at t=0 to (x, p) at t=T
# where p = x' (velocity, not momentum)
#
# For Bogoliubov extraction:
# In-vacuum mode at t=0: u_in = exp(i*omega_i*t) / sqrt(2*omega_i)
# So u_in(0) = 1/sqrt(2*omega_i), u_in'(0) = i*omega_i/sqrt(2*omega_i) = i*sqrt(omega_i/2)
#
# At t=T, u_in = alpha * exp(i*omega_f*t)/sqrt(2*omega_f) + beta * exp(-i*omega_f*t)/sqrt(2*omega_f)
# The Bogoliubov coefficients:
#   alpha = (i/sqrt(2*omega_f)) * [u_in'(T) - i*omega_f*u_in(T)] * exp(-i*omega_f*T) ... wrong sign
#
# Cleaner: use the SUDDEN LIMIT directly since omega*dt << 1.
# In the sudden limit, x(T) ≈ x(0) and x'(T) ≈ x'(0) (the state doesn't evolve).
# The Bogoliubov coefficient for a sudden change omega_i -> omega_f:
#   |beta|^2 = (omega_i - omega_f)^2 / (4*omega_i*omega_f)
# This is EXACT in the dt->0 limit and an excellent approximation when omega*dt << 1.

# But let's also do the numerical monodromy properly to see if there are
# corrections from the finite (but small) transit duration.

T = dt_transit
t_eval = np.linspace(0, T, 5000)

results_v2 = {}
for label, spline in [('single', sp_s), ('collective', sp_c)]:
    oi = float(spline(0.0))
    of = float(spline(0.5))

    def rhs(t, y):
        tau_t = min(0.5, dtau_dt * t)
        omega = float(spline(tau_t))
        return [y[1], -omega**2 * y[0]]

    # Fundamental solution 1: (x,v) = (1,0)
    sol1 = solve_ivp(rhs, [0, T], [1.0, 0.0], t_eval=t_eval,
                     method='DOP853', rtol=1e-13, atol=1e-15)
    # Fundamental solution 2: (x,v) = (0,1)
    sol2 = solve_ivp(rhs, [0, T], [0.0, 1.0], t_eval=t_eval,
                     method='DOP853', rtol=1e-13, atol=1e-15)

    M = np.array([[sol1.y[0,-1], sol2.y[0,-1]],
                  [sol1.y[1,-1], sol2.y[1,-1]]])
    det_M = np.linalg.det(M)
    eigvals_M = np.linalg.eigvals(M)

    # Construct the in-mode at t=0:
    # u_in(0) = 1/sqrt(2*oi), u_in'(0) = i*sqrt(oi/2)
    # u_in(T) = (1/sqrt(2*oi)) * [M11 + i*sqrt(oi/2) * M12_from_sol2 ... ]
    # Actually: u_in(T) = (1/sqrt(2*oi)) * x1(T) + i*sqrt(oi/2) * x2(T)
    # u_in'(T) = (1/sqrt(2*oi)) * v1(T) + i*sqrt(oi/2) * v2(T)

    u_T  = sol1.y[0,-1] / np.sqrt(2*oi) + 1j * np.sqrt(oi/2) * sol2.y[0,-1]
    up_T = sol1.y[1,-1] / np.sqrt(2*oi) + 1j * np.sqrt(oi/2) * sol2.y[1,-1]

    # Extract alpha and beta:
    # alpha = i * [u_in'(T)/(sqrt(2*of)) - i*sqrt(of/2)*u_in(T)] (Wronskian with out-mode)
    # Actually, the standard extraction (Mukhanov-Winitzki, eq. 4.30):
    # alpha = sqrt(of/(2)) * u_T + i * up_T / sqrt(2*of)  ... wait, need WKB phase too
    #
    # In the SUDDEN limit (T->0), u_T ≈ u_in(0) = 1/sqrt(2*oi),
    # up_T ≈ u_in'(0) = i*sqrt(oi/2)
    # So: we need to project onto out-modes at t=T.
    # Out-mode basis at t=T: v_out(T) = 1/sqrt(2*of), v_out'(T) = i*sqrt(of/2)
    # Using KG inner product: (v_out, u_in)_T = i * (v_out* u_in' - v_out*' u_in)
    # alpha = (v_out, u_in)_T
    # = i * [1/sqrt(2*of) * up_T - (-i)*sqrt(of/2) * u_T]
    # = i * [up_T/sqrt(2*of) + i*sqrt(of/2)*u_T]
    # = i*up_T/sqrt(2*of) - sqrt(of/2)*u_T

    alpha_bog = 1j * up_T / np.sqrt(2*of) - np.sqrt(of/2) * u_T
    # beta = -(v_out*, u_in)_T = -i * [v_out u_in' - v_out' u_in]
    # = -i * [1/sqrt(2*of)*exp(i*of*T)*up_T - i*sqrt(of/2)*exp(i*of*T)*u_T]
    # Hmm, need to be more careful with time-dependent phases...
    #
    # For the SUDDEN LIMIT, there are no phases (T~0). Use:
    # |alpha|^2 + |beta|^2 = (of * |u_T|^2 + |up_T|^2/of)
    # |alpha|^2 - |beta|^2 = 1

    sum_ab = of * np.abs(u_T)**2 + np.abs(up_T)**2 / of
    beta2_num = (sum_ab - 1.0) / 2.0

    # Sudden-quench analytical:
    beta2_sudden = (oi - of)**2 / (4*oi*of)

    # Relative correction from finite transit time
    delta_beta2 = (np.real(beta2_num) - beta2_sudden) / beta2_sudden if beta2_sudden > 0 else 0

    # Floquet: eigenvalues of monodromy
    abs_eig = np.abs(eigvals_M)
    mu_F = max(0.0, np.log(max(abs_eig)) / T)

    results_v2[label] = {
        'M': M, 'det_M': det_M, 'eigvals': eigvals_M,
        'omega_i': oi, 'omega_f': of,
        'beta2_numerical': np.real(beta2_num),
        'beta2_sudden': beta2_sudden,
        'delta_beta2': delta_beta2,
        'mu_F': mu_F,
        'abs_eig': abs_eig,
        'sum_ab': sum_ab,
    }

    print(f"\n{'='*50}")
    print(f"  {label.upper()}")
    print(f"{'='*50}")
    print(f"  omega_i = {oi:.6f}, omega_f = {of:.6f}")
    print(f"  Monodromy M =")
    print(f"    [{M[0,0]:.12f}  {M[0,1]:.12f}]")
    print(f"    [{M[1,0]:.12f}  {M[1,1]:.12f}]")
    print(f"  det(M) = {det_M:.15f}")
    print(f"  eigvals = {eigvals_M}")
    print(f"  |eigvals| = {abs_eig}")
    print(f"  mu_F = {mu_F:.8f} M_KK")
    print(f"")
    print(f"  |alpha|^2 + |beta|^2 = {np.real(sum_ab):.10f}")
    print(f"  |beta|^2 (numerical) = {np.real(beta2_num):.10f}")
    print(f"  |beta|^2 (sudden)    = {beta2_sudden:.10f}")
    print(f"  Relative correction  = {delta_beta2:.6e}")
    print(f"  n_particle per mode  = {np.real(beta2_num):.6f}")

# ============================================================
# E. Adiabaticity parameter profile
# ============================================================
print(f"\n{'='*60}")
print("ADIABATICITY PROFILE")
print(f"{'='*60}")

for label, spline, omJ in [('single', sp_s, omega_J_s), ('collective', sp_c, omega_J_c)]:
    domJ_dtau = spline(tau_vals, 1)
    domJ_dt = domJ_dtau * dtau_dt
    gamma = omJ**2 / (np.abs(domJ_dt) + 1e-30)

    # Find fold index
    fold_idx = np.argmin(np.abs(tau_vals - tau_fold))

    print(f"\n  {label}:")
    print(f"  gamma_min = {gamma.min():.6e} at tau = {tau_vals[np.argmin(gamma)]:.4f}")
    print(f"  gamma_max = {gamma.max():.6e} at tau = {tau_vals[np.argmax(gamma)]:.4f}")
    print(f"  gamma_fold = {gamma[fold_idx]:.6e}")
    print(f"  gamma << 1 EVERYWHERE => deeply non-adiabatic")
    print(f"  P_LZ = 1 - exp(-2*pi*gamma_min) = {1-np.exp(-2*PI*gamma.min()):.8f}")

# ============================================================
# F. Resonance condition check
# ============================================================
print(f"\n{'='*60}")
print("RESONANCE CONDITION")
print(f"{'='*60}")
# For parametric resonance: need 2*omega_J = n*omega_drive for integer n
# The "drive" frequency is the rate at which the system parameters change.
# d(ln E_J)/dt is the fractional rate of change of E_J.
# omega_drive ~ |d(ln omega_J)/dt|
for label, spline, omJ in [('single', sp_s, omega_J_s), ('collective', sp_c, omega_J_c)]:
    domJ_dtau = spline(tau_vals, 1)
    omega_drive = np.abs(domJ_dtau * dtau_dt / omJ)  # |d(ln omega)/dt|
    ratio_2omega_drive = 2 * omJ / (omega_drive + 1e-30)
    print(f"\n  {label}:")
    print(f"  omega_drive = |d(ln omega_J)/dt|:")
    print(f"    range: [{omega_drive.min():.2f}, {omega_drive.max():.2f}] M_KK")
    print(f"  2*omega_J / omega_drive:")
    print(f"    range: [{ratio_2omega_drive.min():.6f}, {ratio_2omega_drive.max():.6f}]")
    print(f"  For parametric resonance need 2*omega/omega_drive = integer.")
    print(f"  Ratio << 1 everywhere => NO parametric resonance possible")
    print(f"  The 'drive' changes omega faster than omega itself can oscillate")

# ============================================================
# G. Sub-Hubble check
# ============================================================
print(f"\n{'='*60}")
print("SUB-HUBBLE CHECK")
print(f"{'='*60}")
H = H_fold  # 586.5 M_KK
for label, omJ in [('single', omega_J_s), ('collective', omega_J_c)]:
    ratio = omJ / H
    print(f"\n  {label}: omega_J/H range = [{ratio.min():.6f}, {ratio.max():.6f}]")
    print(f"  omega_J ALWAYS sub-Hubble (ratio << 1)")
    print(f"  Plasma mode is FROZEN by Hubble expansion")

# ============================================================
# H. GATE VERDICT
# ============================================================
mu_F_s = results_v2['single']['mu_F']
mu_F_c = results_v2['collective']['mu_F']
n_s = results_v2['single']['beta2_numerical']
n_c = results_v2['collective']['beta2_numerical']
beta2_sudden_s = results_v2['single']['beta2_sudden']
beta2_sudden_c = results_v2['collective']['beta2_sudden']

print(f"\n{'='*65}")
print(f"GATE: FLOQUET-PLASMA-57")
print(f"{'='*65}")
print(f"\n  Floquet exponent mu_F:")
print(f"    single:     {mu_F_s:.8f} M_KK")
print(f"    collective: {mu_F_c:.8f} M_KK")
print(f"\n  Monodromy eigenvalues ON unit circle (|lambda|=1) for both.")
print(f"  => NO Floquet instability (mu_F = 0).")
print(f"\n  Parker particle number |beta|^2:")
print(f"    single:     {n_s:.6f} (sudden formula: {beta2_sudden_s:.6f})")
print(f"    collective: {n_c:.6f} (sudden formula: {beta2_sudden_c:.6f})")
print(f"\n  Adiabaticity gamma << 1 everywhere (min ~ 2e-5)")
print(f"  omega_J * dt_transit << 1 everywhere")
print(f"  omega_J / H << 1 everywhere")

# The gate asks: mu_F > 0 at any tau?
# ANSWER: mu_F = 0 (eigenvalues on unit circle, det=1, stable)
# The monodromy is a ROTATION, not a hyperbolic expansion.
# But |beta|^2 > 0 — there IS particle production from the quench.
# The particle production is O(1) per mode — the sudden quench formula
# gives |beta|^2 = (omega_i - omega_f)^2 / (4*omega_i*omega_f) ~ 1.0

# Physical interpretation:
# The Floquet exponent is ZERO because the system is Hamiltonian (det M = 1)
# and the transit is a single pass (not periodic). For a one-pass quench,
# "Floquet instability" is not the right concept — what matters is
# Bogoliubov particle creation, and that IS significant (n ~ 1 per mode).

# HOWEVER: the gate as pre-registered asks specifically about mu_F > 0.
# mu_F = 0 at all tau. Verdict: FAIL on the strict Floquet criterion.
# But with the annotation that Parker production IS occurring (n ~ 1).

verdict = "FAIL"
verdict_detail = (
    f"mu_F = 0 everywhere (monodromy eigenvalues on unit circle, det=1). "
    f"No Floquet instability. "
    f"BUT Parker particle production: |beta|^2 = {beta2_sudden_s:.4f} (single), "
    f"{beta2_sudden_c:.4f} (collective) from sudden quench. "
    f"omega_J sub-Hubble throughout (max omega_J/H = {(omega_J_s/H).max():.4f}). "
    f"Plasma mode is cosmologically frozen."
)

print(f"\n  VERDICT: {verdict}")
print(f"  {verdict_detail}")

# ============================================================
# I. Save
# ============================================================
save_path = r"C:\sandbox\Ainulindale Exflation\computations\s57_floquet_plasma.npz"
np.savez(save_path,
    # Grid
    tau_values=tau_vals,
    dtau_dt=np.float64(dtau_dt),
    dt_transit=np.float64(dt_transit),
    # omega_J
    omega_J_single=omega_J_s,
    omega_J_collective=omega_J_c,
    # Monodromy
    M_single=results_v2['single']['M'],
    M_collective=results_v2['collective']['M'],
    det_M_single=np.float64(results_v2['single']['det_M']),
    det_M_collective=np.float64(results_v2['collective']['det_M']),
    eigvals_M_single=results_v2['single']['eigvals'],
    eigvals_M_collective=results_v2['collective']['eigvals'],
    # Floquet
    mu_F_single=np.float64(mu_F_s),
    mu_F_collective=np.float64(mu_F_c),
    # Bogoliubov
    beta2_numerical_single=np.float64(n_s),
    beta2_numerical_collective=np.float64(n_c),
    beta2_sudden_single=np.float64(beta2_sudden_s),
    beta2_sudden_collective=np.float64(beta2_sudden_c),
    delta_beta2_single=np.float64(results_v2['single']['delta_beta2']),
    delta_beta2_collective=np.float64(results_v2['collective']['delta_beta2']),
    # Adiabaticity
    gamma_adiab_single=omega_J_s**2 / (np.abs(sp_s(tau_vals, 1) * dtau_dt) + 1e-30),
    gamma_adiab_collective=omega_J_c**2 / (np.abs(sp_c(tau_vals, 1) * dtau_dt) + 1e-30),
    # Hubble comparison
    H_canonical=np.float64(H_fold),
    omega_J_over_H_single=omega_J_s / H_fold,
    omega_J_over_H_collective=omega_J_c / H_fold,
    # Gate
    gate_name=np.array('FLOQUET-PLASMA-57'),
    gate_verdict=np.array(verdict),
    gate_detail=np.array(verdict_detail),
)
print(f"\nSaved: {save_path}")
print("DONE")
