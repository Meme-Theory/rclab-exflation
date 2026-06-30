#!/usr/bin/env python3
"""
s57_parker_ba.py — Parker (cosmological) particle creation for 31 BA phonon modes
==================================================================================

Gate: PARKER-BA-57
  PASS: <n> > 1 for any BA mode at any tau in [0.10, 0.30]
  FAIL: <n> < 0.01 at all tau

Physics:
  The BA (Bogoliubov-Anderson) modes are dispersive phonons on the 32-cell fabric.
  Their frequencies omega_n(tau) change during the SU(3) transit (tau: 0 -> 0.5).
  A time-dependent frequency drives parametric particle creation — the Parker (1969)
  mechanism, identical to cosmological pair creation from the expansion of space.

  The mode equation for each mode n:
    d^2 phi_n / dt^2 + omega_n(t)^2 phi_n = 0

  We parametrize in terms of tau via dtau/dt = v_tau (constant transit velocity).
  Then dt = dtau / v_tau and d/dt = v_tau * d/dtau, giving:

    v_tau^2 * d^2 phi_n / dtau^2 + omega_n(tau)^2 * phi_n = 0

  This is equivalent to:
    d^2 phi_n / dtau^2 + [omega_n(tau) / v_tau]^2 * phi_n = 0

  Define the rescaled frequency Omega_n(tau) = omega_n(tau) / v_tau. Then:
    d^2 phi_n / dtau^2 + Omega_n(tau)^2 * phi_n = 0

  This is a standard parametric oscillator in the tau variable.

  Adiabatic vacuum initial conditions at tau_i:
    phi_n(tau_i) = 1 / sqrt(2 * Omega_n(tau_i))
    d(phi_n)/dtau(tau_i) = i * sqrt(Omega_n(tau_i) / 2)

  These are complex — we solve the real and imaginary parts simultaneously.

  Bogoliubov coefficient extraction at tau_f:
    |beta_n|^2 = (Omega_n(tau_f) * |phi_n(tau_f)|^2
                 + |d(phi_n)/dtau(tau_f)|^2 / Omega_n(tau_f) - 1) / 2

  Particle number per mode: <n_n> = |beta_n|^2

Method:
  1. Load omega_BA(tau) from s56_ba_spectrum.npz (50 tau x 31 modes)
  2. Interpolate each omega_n(tau) with cubic spline for smooth derivatives
  3. Solve mode equation via RK45 (scipy) with adaptive step for each mode
  4. Extract |beta|^2 at multiple tau checkpoints
  5. Compute adiabatic parameter |dOmega/dtau| / Omega^2 to diagnose regime

Also computes:
  - Sudden quench comparison: |beta_SQ|^2 = (r + 1/r - 2)/4 where r = omega_i/omega_f
  - Total particle number N_total = sum_n |beta_n|^2
  - Total energy E_Parker = sum_n omega_n * (|beta_n|^2 + 1/2)

Author: Landau condensed-matter-theorist agent (Session 57, Wave 2)
"""

import sys
import os
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.integrate import solve_ivp

# --- Import canonical constants ---
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    dt_transit, tau_fold, omega_tau, E_cond, N_cells,
    M_KK, omega_att, E_B1, E_B2_mean, E_B3_mean,
    T_acoustic, J_C2
)

# ============================================================================
#  LOAD DATA
# ============================================================================

data_dir = os.path.dirname(os.path.abspath(__file__))
ba_data = np.load(os.path.join(data_dir, "s56_ba_spectrum.npz"), allow_pickle=True)
s54_data = np.load(os.path.join(data_dir, "s54_scale_factor.npz"), allow_pickle=True)

tau_values = ba_data['tau_values']        # shape (50,), range [0, 0.5]
omega_BA = ba_data['omega_BA']            # shape (50, 31), frequencies in M_KK units
N_modes = omega_BA.shape[1]               # 31

# Transit velocity: dtau/dt = Delta_tau / dt_transit
Delta_tau = tau_values[-1] - tau_values[0]  # 0.5
v_tau = Delta_tau / dt_transit              # ~ 442.4 M_KK

print(f"Transit velocity: v_tau = {v_tau:.4f} M_KK")
print(f"  (from Delta_tau = {Delta_tau}, dt_transit = {dt_transit:.6e} M_KK^-1)")
print(f"Number of BA modes: {N_modes}")
print(f"tau range: [{tau_values[0]:.4f}, {tau_values[-1]:.4f}]")
print()

# ============================================================================
#  VERIFY: ADIABATIC PARAMETER
# ============================================================================
# The adiabatic parameter is eta_n(tau) = |d(omega_n)/dtau| / (omega_n^2 / v_tau)
# In terms of the rescaled frequency Omega_n = omega_n / v_tau:
#   eta_n = |dOmega_n/dtau| / Omega_n^2 = v_tau * |d(omega_n)/dtau| / omega_n^2
#
# If eta >> 1: non-adiabatic (sudden quench regime) -> large particle creation
# If eta << 1: adiabatic (exponential suppression) -> small particle creation

# Build cubic spline interpolators for each mode
splines = []
for n in range(N_modes):
    cs = CubicSpline(tau_values, omega_BA[:, n])
    splines.append(cs)

# Compute adiabatic parameter at each tau for each mode
eta_matrix = np.zeros_like(omega_BA)  # (50, 31)
for n in range(N_modes):
    domega_dtau = splines[n](tau_values, 1)  # first derivative
    omega_n = omega_BA[:, n]
    # Adiabatic parameter: |d(omega)/dt| / omega^2 = |d(omega)/dtau * v_tau| / omega^2
    # = v_tau * |d(omega)/dtau| / omega^2
    eta_matrix[:, n] = v_tau * np.abs(domega_dtau) / omega_n**2

# Evaluate at the fold region
fold_idx = np.argmin(np.abs(tau_values - tau_fold))
print(f"Adiabatic parameters at tau_fold = {tau_values[fold_idx]:.4f}:")
print(f"  min eta: {eta_matrix[fold_idx, :].min():.4f}")
print(f"  max eta: {eta_matrix[fold_idx, :].max():.4f}")
print(f"  mean eta: {eta_matrix[fold_idx, :].mean():.4f}")
print()

# ============================================================================
#  SOLVE MODE EQUATION VIA RK45
# ============================================================================
# For each mode, solve:
#   d^2 phi / dtau^2 + Omega_n(tau)^2 * phi = 0
# where Omega_n(tau) = omega_n(tau) / v_tau
#
# First-order form with complex phi:
#   y = [phi_R, pi_R, phi_I, pi_I]  where pi = d(phi)/dtau
#   d(phi_R)/dtau = pi_R
#   d(pi_R)/dtau = -Omega_n(tau)^2 * phi_R
#   d(phi_I)/dtau = pi_I
#   d(pi_I)/dtau = -Omega_n(tau)^2 * phi_I
#
# Initial conditions (adiabatic vacuum at tau_i):
#   phi(tau_i) = 1/sqrt(2*Omega_n(tau_i))           [real part]
#   d(phi)/dtau(tau_i) = i*sqrt(Omega_n(tau_i)/2)   [imaginary part of momentum]
# So:
#   phi_R(tau_i) = 1/sqrt(2*Omega_n_i), phi_I(tau_i) = 0
#   pi_R(tau_i) = 0, pi_I(tau_i) = sqrt(Omega_n_i/2)

# Checkpoint tau values for extraction
tau_checkpoints = [0.10, 0.15, tau_fold, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50]
tau_start = tau_values[0]  # 0.0

# Storage
beta_sq_full = np.zeros((N_modes, len(tau_checkpoints)))  # |beta|^2 at checkpoints
n_exc_full = np.zeros((N_modes, len(tau_checkpoints)))
alpha_sq_full = np.zeros((N_modes, len(tau_checkpoints)))

print("Solving mode equations...")

for n in range(N_modes):
    cs = splines[n]

    def rhs(tau, y):
        """Right-hand side for [phi_R, pi_R, phi_I, pi_I]."""
        omega_n = cs(tau)
        Omega_n = omega_n / v_tau
        Omega_sq = Omega_n**2
        return [y[1], -Omega_sq * y[0], y[3], -Omega_sq * y[2]]

    # Initial conditions
    omega_i = cs(tau_start)
    Omega_i = omega_i / v_tau
    phi_R_0 = 1.0 / np.sqrt(2.0 * Omega_i)
    phi_I_0 = 0.0  # (local)
    pi_R_0 = 0.0  # (local)
    pi_I_0 = np.sqrt(Omega_i / 2.0)
    y0 = [phi_R_0, pi_R_0, phi_I_0, pi_I_0]

    # Solve with dense output for checkpoint extraction
    sol = solve_ivp(
        rhs,
        [tau_start, tau_values[-1]],
        y0,
        method='RK45',
        rtol=1e-10,
        atol=1e-12,
        dense_output=True,
        max_step=0.001  # Fine stepping to resolve oscillations
    )

    if not sol.success:
        print(f"  WARNING: Mode {n} failed: {sol.message}")
        continue

    # Extract Bogoliubov coefficients at each checkpoint
    for ic, tau_c in enumerate(tau_checkpoints):
        if tau_c > tau_values[-1]:
            continue
        y_c = sol.sol(tau_c)
        phi_R, pi_R, phi_I, pi_I = y_c

        omega_c = cs(tau_c)
        Omega_c = omega_c / v_tau

        # |phi|^2 = phi_R^2 + phi_I^2
        phi_sq = phi_R**2 + phi_I**2
        # |pi|^2 = pi_R^2 + pi_I^2
        pi_sq = pi_R**2 + pi_I**2

        # Bogoliubov coefficient: |beta|^2 = (Omega*|phi|^2 + |pi|^2/Omega - 1)/2
        beta_sq = (Omega_c * phi_sq + pi_sq / Omega_c - 1.0) / 2.0

        # Also compute |alpha|^2 for consistency check (|alpha|^2 - |beta|^2 = 1)
        alpha_sq = (Omega_c * phi_sq + pi_sq / Omega_c + 1.0) / 2.0

        beta_sq_full[n, ic] = max(beta_sq, 0.0)  # numerical floor
        alpha_sq_full[n, ic] = alpha_sq
        n_exc_full[n, ic] = max(beta_sq, 0.0)

    if n % 10 == 0 or n == N_modes - 1:
        print(f"  Mode {n:2d}: omega_i={omega_i:.4f}, omega_f={cs(tau_values[-1]):.4f}, "
              f"|beta|^2(end)={beta_sq_full[n, -1]:.6f}")

print()

# ============================================================================
#  SUDDEN QUENCH COMPARISON
# ============================================================================
# For validation: the sudden-quench formula gives
#   |beta_SQ|^2 = (r + 1/r - 2) / 4  where r = omega_i / omega_f

beta_sq_SQ = np.zeros((N_modes, len(tau_checkpoints)))
for n in range(N_modes):
    omega_i = splines[n](tau_start)
    for ic, tau_c in enumerate(tau_checkpoints):
        omega_f = splines[n](tau_c)
        r = omega_i / omega_f
        beta_sq_SQ[n, ic] = (r + 1.0/r - 2.0) / 4.0

print("Sudden quench vs RK45 comparison at tau=0.5:")
for n in [0, 5, 10, 15, 20, 25, 30]:
    if n < N_modes:
        print(f"  Mode {n:2d}: |beta_RK|^2 = {beta_sq_full[n, -1]:.6f}, "
              f"|beta_SQ|^2 = {beta_sq_SQ[n, -1]:.6f}, "
              f"ratio = {beta_sq_full[n, -1] / max(beta_sq_SQ[n, -1], 1e-30):.4f}")
print()

# ============================================================================
#  SUMMARY STATISTICS
# ============================================================================

# At each checkpoint, compute totals
N_total = np.sum(n_exc_full, axis=0)     # total particle number
E_Parker = np.zeros(len(tau_checkpoints))
E_ZPE = np.zeros(len(tau_checkpoints))
for ic, tau_c in enumerate(tau_checkpoints):
    for n in range(N_modes):
        omega_c = splines[n](tau_c)
        E_Parker[ic] += omega_c * n_exc_full[n, ic]                    # excitation energy
        E_ZPE[ic] += omega_c * (n_exc_full[n, ic] + 0.5)              # total energy (incl ZPE)

print("=" * 80)
print("PARKER-BA-57: Summary at key checkpoints")
print("=" * 80)
print(f"{'tau':>6s} {'N_total':>10s} {'max<n>':>10s} {'E_Parker':>12s} {'E_ZPE':>12s} {'mode(max)':>10s}")
print("-" * 70)
for ic, tau_c in enumerate(tau_checkpoints):
    max_n = np.max(n_exc_full[:, ic])
    max_mode = np.argmax(n_exc_full[:, ic])
    print(f"{tau_c:6.3f} {N_total[ic]:10.4f} {max_n:10.6f} {E_Parker[ic]:12.6f} {E_ZPE[ic]:12.6f} {max_mode:10d}")
print()

# Focus on the gate region [0.10, 0.30]
gate_mask = [ic for ic, tc in enumerate(tau_checkpoints) if 0.10 <= tc <= 0.30]
max_n_gate = 0.0
max_n_mode_gate = -1
max_n_tau_gate = -1.0
for ic in gate_mask:
    mn = np.max(n_exc_full[:, ic])
    if mn > max_n_gate:
        max_n_gate = mn
        max_n_mode_gate = np.argmax(n_exc_full[:, ic])
        max_n_tau_gate = tau_checkpoints[ic]

print(f"GATE REGION [0.10, 0.30]:")
print(f"  Maximum <n> = {max_n_gate:.6f} at mode {max_n_mode_gate}, tau = {max_n_tau_gate:.3f}")
print()

# Overall maximum across all checkpoints
max_n_all = np.max(n_exc_full)
max_loc = np.unravel_index(np.argmax(n_exc_full), n_exc_full.shape)
print(f"OVERALL MAXIMUM:")
print(f"  <n> = {max_n_all:.6f} at mode {max_loc[0]}, tau = {tau_checkpoints[max_loc[1]]:.3f}")
print()

# ============================================================================
#  TOP 5 MODES BY |beta|^2 AT END (tau=0.5)
# ============================================================================

end_idx = len(tau_checkpoints) - 1  # tau = 0.5
sorted_modes = np.argsort(n_exc_full[:, end_idx])[::-1]

print("Top 10 modes by |beta|^2 at tau=0.5:")
print(f"{'Mode':>6s} {'omega_i':>10s} {'omega_f':>10s} {'ratio':>8s} {'|beta|^2':>12s} {'|beta_SQ|^2':>12s} {'eta(fold)':>10s}")
print("-" * 80)
for rank in range(min(10, N_modes)):
    n = sorted_modes[rank]
    omega_i = splines[n](tau_start)
    omega_f = splines[n](tau_values[-1])
    r = omega_i / omega_f
    print(f"{n:6d} {omega_i:10.4f} {omega_f:10.4f} {r:8.4f} "
          f"{n_exc_full[n, end_idx]:12.6f} {beta_sq_SQ[n, end_idx]:12.6f} "
          f"{eta_matrix[fold_idx, n]:10.4f}")
print()

# ============================================================================
#  ADIABATIC PARAMETER ANALYSIS
# ============================================================================

# For mode 0 (lowest frequency) — most likely to be excited
print("Adiabatic parameter eta for mode 0 across transit:")
for i in range(0, len(tau_values), 5):
    print(f"  tau={tau_values[i]:.4f}: eta={eta_matrix[i, 0]:.4f}, "
          f"omega={omega_BA[i, 0]:.6f}, Omega={omega_BA[i, 0]/v_tau:.6e}")
print()

# The key diagnostic: Omega_n / v_tau. If Omega_n << 1, many oscillations per
# transit time -> adiabatic. If Omega_n >> 1, few oscillations -> non-adiabatic.
# But here Omega_n = omega_n / v_tau. Since v_tau ~ 442, even omega_n ~ 0.1
# gives Omega_n ~ 2.3e-4, meaning the RESCALED frequency is very small.
# This means in the tau variable, the oscillation period is ~ 1/Omega_n ~ 4400,
# FAR larger than the transit range Delta_tau = 0.5.
# Equivalently: the modes complete only Omega_n * Delta_tau / (2*pi) oscillations
# during the transit.

n_oscillations = np.zeros(N_modes)
for n in range(N_modes):
    # Average Omega over transit
    Omega_avg = np.mean(omega_BA[:, n]) / v_tau
    n_oscillations[n] = Omega_avg * Delta_tau / (2.0 * np.pi)

print("Number of oscillations during transit:")
print(f"  Mode 0  (lowest omega): {n_oscillations[0]:.6f}")
print(f"  Mode 15 (median):       {n_oscillations[15]:.6f}")
print(f"  Mode 30 (highest):      {n_oscillations[30]:.6f}")
print(f"  All modes < 1 oscillation: {np.all(n_oscillations < 1.0)}")
print()

# ============================================================================
#  PHYSICAL INTERPRETATION: SUDDEN QUENCH REGIME
# ============================================================================
# Since n_oscillations << 1 for ALL modes, the system is deeply in the
# sudden quench regime. The RK45 result should closely match the sudden
# quench formula. Any deviations come from the non-trivial shape of
# omega_n(tau) — the transit is not an instantaneous jump but a smooth ramp.

# Compute the ratio RK45/SQ to quantify how much the smooth transit matters
ratio_end = beta_sq_full[:, end_idx] / np.maximum(beta_sq_SQ[:, end_idx], 1e-30)
print("RK45 / Sudden-quench ratio at tau=0.5:")
print(f"  mean:   {np.mean(ratio_end):.4f}")
print(f"  min:    {np.min(ratio_end):.4f}")
print(f"  max:    {np.max(ratio_end):.4f}")
print(f"  std:    {np.std(ratio_end):.4f}")
print()

# ============================================================================
#  ENERGY BUDGET COMPARISON
# ============================================================================
# E_matter from W1-2: |F_BCS| + F_BA = 11.40 M_KK
E_matter = 11.40  # M_KK, from W1-2  # (local)

# At tau = 0.5 (end of transit)
E_P_end = E_Parker[-1]
E_ZPE_end = E_ZPE[-1]
N_total_end = N_total[-1]

# BA ZPE at tau = 0.5
BA_ZPE = 0.0  # (local)
for n in range(N_modes):
    BA_ZPE += 0.5 * splines[n](tau_values[-1])

print("Energy budget at end of transit (tau = 0.5):")
print(f"  N_total (particles)  = {N_total_end:.4f}")
print(f"  E_Parker (excitation)= {E_P_end:.4f} M_KK")
print(f"  BA ZPE               = {BA_ZPE:.4f} M_KK")
print(f"  E_total (exc + ZPE)  = {E_ZPE_end:.4f} M_KK")
print(f"  E_matter              = {E_matter:.4f} M_KK")
print(f"  f_DM_exc = E_Parker / E_matter   = {E_P_end / E_matter:.4f}")
print(f"  f_DM_ZPE = E_total / E_matter    = {E_ZPE_end / E_matter:.4f}")
print()

# At fold (tau ~ 0.19)
fold_ckpt_idx = None
for ic, tc in enumerate(tau_checkpoints):
    if abs(tc - tau_fold) < 0.01:
        fold_ckpt_idx = ic
        break
if fold_ckpt_idx is not None:
    print(f"Energy budget at fold (tau ~ {tau_checkpoints[fold_ckpt_idx]:.3f}):")
    print(f"  N_total              = {N_total[fold_ckpt_idx]:.4f}")
    print(f"  E_Parker             = {E_Parker[fold_ckpt_idx]:.4f} M_KK")
    print(f"  E_total              = {E_ZPE[fold_ckpt_idx]:.4f} M_KK")
    print()

# ============================================================================
#  GATE VERDICT
# ============================================================================

print("=" * 80)
print("GATE: PARKER-BA-57")
print("=" * 80)
print(f"  Criterion: PASS if <n> > 1 for any BA mode at any tau in [0.10, 0.30]")
print(f"  Criterion: FAIL if <n> < 0.01 at all tau")
print()
print(f"  Maximum <n> in gate region: {max_n_gate:.6f}")
print(f"    at mode {max_n_mode_gate}, tau = {max_n_tau_gate:.3f}")
print()

if max_n_gate > 1.0:
    verdict = "PASS"
    print(f"  VERDICT: **PASS** — <n> = {max_n_gate:.4f} > 1")
elif max_n_gate < 0.01:
    verdict = "FAIL"
    print(f"  VERDICT: **FAIL** — <n> = {max_n_gate:.6f} < 0.01 everywhere in gate region")
else:
    verdict = "INFO"
    print(f"  VERDICT: **INFO** — 0.01 < <n> = {max_n_gate:.6f} < 1 (intermediate)")

# Overall max (including outside gate region)
if max_n_all > 1.0:
    print(f"  Note: max <n> overall = {max_n_all:.4f} at mode {max_loc[0]}, tau = {tau_checkpoints[max_loc[1]]:.3f}")
elif max_n_all >= 0.01:
    print(f"  Note: max <n> overall = {max_n_all:.6f} at mode {max_loc[0]}, tau = {tau_checkpoints[max_loc[1]]:.3f}")

print()

# ============================================================================
#  SAVE
# ============================================================================

outpath = os.path.join(data_dir, "s57_parker_ba.npz")
np.savez(
    outpath,
    # Mode equation results
    tau_checkpoints=np.array(tau_checkpoints),
    beta_sq=beta_sq_full,           # (31, 9) |beta|^2 at checkpoints
    n_exc=n_exc_full,               # (31, 9) same as beta_sq (particle number)
    alpha_sq=alpha_sq_full,         # (31, 9) |alpha|^2
    beta_sq_SQ=beta_sq_SQ,         # (31, 9) sudden quench comparison
    # Totals
    N_total=N_total,                # (9,) total particle number at checkpoints
    E_Parker=E_Parker,              # (9,) total excitation energy
    E_ZPE=E_ZPE,                    # (9,) total energy incl ZPE
    # Adiabatic parameters
    eta_matrix=eta_matrix,          # (50, 31) at original tau grid
    n_oscillations=n_oscillations,  # (31,)
    # Transit
    v_tau=v_tau,
    Delta_tau=Delta_tau,
    dt_transit=dt_transit,
    # Gate
    gate_name="PARKER-BA-57",
    gate_verdict=verdict,
    max_n_gate=max_n_gate,
    max_n_mode_gate=max_n_mode_gate,
    max_n_tau_gate=max_n_tau_gate,
    max_n_all=max_n_all,
    # Comparison with W1-2
    E_matter=E_matter,
    f_DM_exc=E_P_end / E_matter,
    f_DM_ZPE=E_ZPE_end / E_matter,
)

print(f"Saved: {outpath}")
print("DONE")
