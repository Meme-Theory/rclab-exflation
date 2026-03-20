#!/usr/bin/env python3
"""
Session 39, W3-3: BdG Time-Dependent Simulation (BDG-SIM-39)
=============================================================

Simulates the full 8-mode BdG equations through the fold transit to track
condensate dynamics in real time.

Physics:
  - 8 gap-edge modes: 4 B2 (degenerate, rho=14.023) + 1 B1 (rho=1) + 3 B3 (rho=1)
  - Single-particle energies epsilon_k(tau) interpolated from Kosmann data at 9 tau values
  - Coupling V_{kj} also tau-dependent, interpolated from Kosmann K_a matrices
  - mu = 0 (particle-hole symmetric, proven S34)
  - Quench protocol: tau(t) = tau_init + |v_terminal| * t, v_terminal = 26.545

BdG equations (mean-field, self-consistent):
  i d/dt |u_k, v_k> = H_BdG_k(t) |u_k, v_k>
  H_BdG_k = [ xi_k(tau(t))    Delta_k(t)  ]
            [ Delta_k*(t)     -xi_k(tau(t)) ]
  Delta_k(t) = sum_j V_kj(tau(t)) * rho_j * u_j(t) * conj(v_j(t))

Initial condition: BCS ground state at tau_init = 0.10 (equilibrium BdG solution).

Gate: BDG-SIM-39
  PASS: GPV peak visible in FT of |Delta(t)|^2 at omega in [0.70, 0.85] with Q > 3.
  FAIL: no identifiable GPV peak.

Author: gen-physicist (Session 39)
"""

import os
import sys
import time
import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import CubicSpline
from scipy.signal import find_peaks
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
t0_wall = time.time()

print("=" * 78)
print("Session 39, W3-3: BdG TIME-DEPENDENT SIMULATION (BDG-SIM-39)")
print("=" * 78)

# ======================================================================
#  Step 1: Load and interpolate tau-dependent single-particle data
# ======================================================================
print("\n" + "=" * 78)
print("STEP 1: LOAD TAU-DEPENDENT DATA")
print("=" * 78)

kosmann = np.load(os.path.join(SCRIPT_DIR, 's23a_kosmann_singlet.npz'),
                  allow_pickle=True)
vh_arbiter = np.load(os.path.join(SCRIPT_DIR, 's35a_vh_impedance_arbiter.npz'),
                     allow_pickle=True)
d36d = np.load(os.path.join(SCRIPT_DIR, 's36_tau_dynamics.npz'), allow_pickle=True)
d37 = np.load(os.path.join(SCRIPT_DIR, 's37_instanton_action.npz'), allow_pickle=True)
d37ps = np.load(os.path.join(SCRIPT_DIR, 's37_pair_susceptibility.npz'), allow_pickle=True)

# Transit parameters
v_terminal = abs(float(d36d['an_S_full_v_terminal']))  # 26.545
BCS_lo = float(d36d['BCS_window_lo'])                    # 0.175
BCS_hi = float(d36d['BCS_window_hi'])                    # 0.205
tau_fold = float(d37['tau_fold'])                          # 0.19016
E_cond_s37 = float(d37['E_cond_use'])                     # -0.1557

# DOS
rho_smooth = float(vh_arbiter['rho_at_physical'])  # 14.023
n_modes = 8

# S37 reference values
omega_PV_s37 = float(d37ps['omega_plus'])   # 0.792 (GPV frequency)
E_cond_s37ps = float(d37ps['E_cond'])       # -0.137

print(f"  v_terminal       = {v_terminal:.3f}")
print(f"  BCS window       = [{BCS_lo}, {BCS_hi}]")
print(f"  tau_fold          = {tau_fold:.5f}")
print(f"  rho_smooth (B2)   = {rho_smooth:.3f}")
print(f"  omega_PV (S37)    = {omega_PV_s37:.4f}")
print(f"  E_cond (S37)      = {E_cond_s37:.6f}")

# ======================================================================
#  Step 2: Build tau-dependent interpolators for E_k(tau) and V_kj(tau)
# ======================================================================
print("\n" + "=" * 78)
print("STEP 2: BUILD INTERPOLATORS")
print("=" * 78)

tau_grid = kosmann['tau_values']  # [0, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.5]
n_tau = len(tau_grid)

# Extract E_8(tau) and V_8x8(tau) at each grid point
E_8_grid = np.zeros((n_tau, n_modes))
V_8x8_grid = np.zeros((n_tau, n_modes, n_modes))

for ti in range(n_tau):
    evals = kosmann[f'eigenvalues_{ti}']
    si = np.argsort(evals)
    evals_s = evals[si]
    pos_idx = np.where(evals_s > 0)[0]

    B1_idx = pos_idx[0:1]
    B2_idx = pos_idx[1:5]
    B3_idx = pos_idx[5:8]
    full_idx = np.concatenate([B2_idx, B1_idx, B3_idx])

    E_8_grid[ti] = evals_s[full_idx]

    V_16 = np.zeros((16, 16))
    for a in range(8):
        K = kosmann[f'K_a_matrix_{ti}_{a}']
        V_16 += np.abs(K)**2
    V_8x8_grid[ti] = V_16[np.ix_(full_idx, full_idx)]

# Build cubic splines for each quantity
E_splines = [CubicSpline(tau_grid, E_8_grid[:, k]) for k in range(n_modes)]
V_splines = [[CubicSpline(tau_grid, V_8x8_grid[:, k, j]) for j in range(n_modes)]
              for k in range(n_modes)]

# DOS array: B2 modes get rho_smooth, B1/B3 get 1.0
rho = np.array([rho_smooth]*4 + [1.0, 1.0, 1.0, 1.0])
mu = 0.0

def get_E(tau_val):
    """Return E_8 at given tau."""
    return np.array([E_splines[k](tau_val) for k in range(n_modes)])

def get_V(tau_val):
    """Return V_8x8 at given tau."""
    V = np.zeros((n_modes, n_modes))
    for k in range(n_modes):
        for j in range(n_modes):
            V[k, j] = V_splines[k][j](tau_val)
    return V

# Validate at tau = 0.20
E_test = get_E(0.20)
V_test = get_V(0.20)
print(f"  Interpolator validation at tau = 0.20:")
print(f"    E_B2 = {E_test[:4]}")
print(f"    E_B1 = {E_test[4]:.6f}")
print(f"    E_B3 = {E_test[5:8]}")
print(f"    V(B1,B1) = {V_test[4,4]:.2e} (should be ~0)")
print(f"    V(B2,B1) = {V_test[:4,4]}")

# ======================================================================
#  Step 3: Static BCS solution at tau_init for initial conditions
# ======================================================================
print("\n" + "=" * 78)
print("STEP 3: INITIAL CONDITION (STATIC BCS AT tau_init)")
print("=" * 78)

tau_init = 0.10
tau_final = 0.30

def solve_bcs_static(tau_val, max_iter=500, tol=1e-12):
    """Self-consistent BCS solution at given tau.
    Returns (u_k, v_k, Delta_k, E_qp_k) for all 8 modes.
    """
    E = get_E(tau_val)
    V = get_V(tau_val)
    xi = E - mu  # mu = 0

    # Physical V_kj with DOS weighting: V_eff_kj = V_kj * sqrt(rho_k * rho_j)
    # Actually: Delta_k = sum_j V_kj * rho_j * u_j * v_j^*
    # Standard BCS gap equation: Delta_k = sum_j V_kj * rho_j * Delta_j / (2 * E_qp_j)

    # Start with uniform trial gap
    Delta = np.ones(n_modes) * 0.05

    for iteration in range(max_iter):
        E_qp = np.sqrt(xi**2 + Delta**2)
        # Gap equation: Delta_k = sum_j V_kj * rho_j * Delta_j / (2 * E_qp_j)
        new_Delta = np.zeros(n_modes)
        for k in range(n_modes):
            for j in range(n_modes):
                new_Delta[k] += V[k, j] * rho[j] * Delta[j] / (2.0 * E_qp[j])

        # Check convergence
        diff = np.max(np.abs(new_Delta - Delta))
        Delta = new_Delta.copy()
        if diff < tol:
            break

    E_qp = np.sqrt(xi**2 + Delta**2)
    # BCS amplitudes
    u = np.sqrt(0.5 * (1.0 + xi / E_qp))
    v = np.sqrt(0.5 * (1.0 - xi / E_qp))
    # Sign convention: v has same sign as Delta
    v = np.sign(Delta) * np.abs(v)

    return u, v, Delta, E_qp

u0, v0, Delta0, Eqp0 = solve_bcs_static(tau_init)
E_init = get_E(tau_init)
xi_init = E_init - mu

print(f"  tau_init = {tau_init}")
print(f"  E_k(tau_init) = {E_init}")
print(f"  xi_k(tau_init) = {xi_init}")
print(f"  Static BCS gap: Delta_k = {Delta0}")
print(f"  E_qp = {Eqp0}")
print(f"  u_k = {u0}")
print(f"  v_k = {v0}")
print(f"  Condensation energy check: E_cond ~ -sum rho_k Delta_k^2 / (2*E_qp_k)")
E_cond_check = -np.sum(rho * Delta0**2 / (2.0 * Eqp0))
print(f"    E_cond ~ {E_cond_check:.6f}")

# Also solve at fold for reference
u_fold, v_fold, Delta_fold, Eqp_fold = solve_bcs_static(tau_fold)
print(f"\n  Static BCS at fold (tau={tau_fold:.5f}):")
print(f"    Delta_k = {Delta_fold}")
print(f"    E_qp = {Eqp_fold}")

# Gap magnitude for plotting reference
Delta_scalar_init = np.sqrt(np.sum(rho * Delta0**2))
Delta_scalar_fold = np.sqrt(np.sum(rho * Delta_fold**2))
print(f"\n  |Delta|_rms(init) = {Delta_scalar_init:.6f}")
print(f"  |Delta|_rms(fold) = {Delta_scalar_fold:.6f}")

# ======================================================================
#  Step 4: Define BdG time evolution (ODE system)
# ======================================================================
print("\n" + "=" * 78)
print("STEP 4: BdG TIME-DEPENDENT EQUATIONS")
print("=" * 78)

# State vector: y = [Re(u_0), Im(u_0), Re(v_0), Im(v_0),
#                     Re(u_1), Im(u_1), Re(v_1), Im(v_1), ...]
# Total: 8 modes * 4 real components = 32 real ODEs

def bdg_rhs(t, y):
    """Right-hand side of BdG equations.

    i d/dt [u_k] = [  xi_k    Delta_k ] [u_k]
            [v_k]   [ Delta_k* -xi_k   ] [v_k]

    Delta_k = sum_j V_kj * rho_j * u_j * conj(v_j)
    """
    # Unpack complex amplitudes
    u = np.zeros(n_modes, dtype=complex)
    v = np.zeros(n_modes, dtype=complex)
    for k in range(n_modes):
        base = 4 * k
        u[k] = y[base] + 1j * y[base + 1]
        v[k] = y[base + 2] + 1j * y[base + 3]

    # Current tau
    tau_t = tau_init + v_terminal * t

    # Clamp tau to interpolation range
    tau_t = np.clip(tau_t, tau_grid[0] + 1e-10, tau_grid[-1] - 1e-10)

    # Get tau-dependent quantities
    E = get_E(tau_t)
    V = get_V(tau_t)
    xi = E - mu

    # Self-consistent gap
    # Delta_k = sum_j V_kj * rho_j * u_j * conj(v_j)
    kappa = u * np.conj(v)  # anomalous density
    Delta = np.zeros(n_modes, dtype=complex)
    for k in range(n_modes):
        Delta[k] = np.sum(V[k, :] * rho * kappa)

    # BdG equations: i d/dt u_k = xi_k * u_k + Delta_k * v_k
    #                i d/dt v_k = Delta_k^* * u_k - xi_k * v_k
    du = np.zeros(n_modes, dtype=complex)
    dv = np.zeros(n_modes, dtype=complex)
    for k in range(n_modes):
        du[k] = -1j * (xi[k] * u[k] + Delta[k] * v[k])
        dv[k] = -1j * (np.conj(Delta[k]) * u[k] - xi[k] * v[k])

    # Pack back to real
    dydt = np.zeros(4 * n_modes)
    for k in range(n_modes):
        base = 4 * k
        dydt[base] = du[k].real
        dydt[base + 1] = du[k].imag
        dydt[base + 2] = dv[k].real
        dydt[base + 3] = dv[k].imag

    return dydt


# Initial condition
y0 = np.zeros(4 * n_modes)
for k in range(n_modes):
    base = 4 * k
    y0[base] = u0[k].real      # Re(u_k)
    y0[base + 1] = 0.0         # Im(u_k) = 0 (real initial state)
    y0[base + 2] = v0[k].real  # Re(v_k)
    y0[base + 3] = 0.0         # Im(v_k) = 0

# Time range: tau goes from tau_init=0.10 to tau_final=0.30
# t_transit = (tau_final - tau_init) / v_terminal
t_transit = (tau_final - tau_init) / v_terminal
T_total = 100.0  # natural units (>> 10 * T_OTOC ~ 67)

# But also check: time to reach tau_final
t_reach_final = (tau_final - tau_init) / v_terminal
t_reach_edge = (tau_grid[-1] - tau_init) / v_terminal

print(f"  Number of ODE components: {4 * n_modes}")
print(f"  t_transit (BCS window): {t_transit:.6e}")
print(f"  t to reach tau=0.30: {t_reach_final:.6e}")
print(f"  t to reach tau=0.50: {t_reach_edge:.6e}")
print(f"  T_total = {T_total}")
print(f"  T_total / t_transit = {T_total / t_transit:.0f}")

# After tau reaches the edge of interpolation, the modulus is beyond the
# BCS window. We continue evolution but with frozen tau at the boundary.
# In practice: once tau > 0.50, single-particle levels are well above the
# BCS instability region and the condensate is destroyed.

# ======================================================================
#  Step 5: Integrate
# ======================================================================
print("\n" + "=" * 78)
print("STEP 5: NUMERICAL INTEGRATION")
print("=" * 78)

t_start = time.time()

# Dense output for smooth time series
n_points = 20000
t_eval = np.linspace(0, T_total, n_points)

sol = solve_ivp(
    bdg_rhs,
    (0, T_total),
    y0,
    method='RK45',
    t_eval=t_eval,
    rtol=1e-10,
    atol=1e-12,
    max_step=0.01  # Ensure good resolution during transit
)

t_integrate = time.time() - t_start
print(f"  Integration time: {t_integrate:.2f} s")
print(f"  Status: {sol.message}")
print(f"  N steps (internal): {sol.nfev}")
print(f"  Solution shape: {sol.y.shape}")

if not sol.success:
    print("  WARNING: Integration failed!")
    sys.exit(1)

t_arr = sol.t
y_arr = sol.y

# ======================================================================
#  Step 6: Extract observables
# ======================================================================
print("\n" + "=" * 78)
print("STEP 6: EXTRACT OBSERVABLES")
print("=" * 78)

# Reconstruct u_k(t), v_k(t), Delta_k(t)
u_t = np.zeros((n_modes, len(t_arr)), dtype=complex)
v_t = np.zeros((n_modes, len(t_arr)), dtype=complex)

for k in range(n_modes):
    base = 4 * k
    u_t[k] = y_arr[base] + 1j * y_arr[base + 1]
    v_t[k] = y_arr[base + 2] + 1j * y_arr[base + 3]

# Self-consistent gap Delta_k(t) = sum_j V_kj(tau(t)) * rho_j * u_j * conj(v_j)
Delta_t = np.zeros((n_modes, len(t_arr)), dtype=complex)
tau_t_arr = tau_init + v_terminal * t_arr
tau_t_arr = np.clip(tau_t_arr, tau_grid[0] + 1e-10, tau_grid[-1] - 1e-10)

kappa_t = u_t * np.conj(v_t)  # anomalous density (n_modes, n_times)

for idx in range(len(t_arr)):
    tau_val = tau_t_arr[idx]
    V = get_V(tau_val)
    for k in range(n_modes):
        Delta_t[k, idx] = np.sum(V[k, :] * rho * kappa_t[:, idx])

# Total gap squared (scalar order parameter)
Delta_sq = np.sum(rho[:, None] * np.abs(Delta_t)**2, axis=0)
Delta_scalar = np.sqrt(Delta_sq)

# Also compute per-branch gaps
Delta_B2_sq = np.sum(rho[:4, None] * np.abs(Delta_t[:4])**2, axis=0)
Delta_B1_sq = rho[4] * np.abs(Delta_t[4])**2
Delta_B3_sq = np.sum(rho[5:8, None] * np.abs(Delta_t[5:8])**2, axis=0)

# Quasiparticle occupation: n_k(t) = |v_k(t)|^2
n_qp_t = np.abs(v_t)**2

# Normalization check: |u_k|^2 + |v_k|^2 should be 1
norm_check = np.abs(u_t)**2 + np.abs(v_t)**2
norm_max_dev = np.max(np.abs(norm_check - 1.0))
print(f"  Max normalization deviation: {norm_max_dev:.2e} (should be << 1)")

# Pair number N_pair(t) = sum_k rho_k |v_k(t)|^2
N_pair_t = np.sum(rho[:, None] * np.abs(v_t)**2, axis=0)

# Find transit time: when tau crosses the BCS window
t_enter_BCS = (BCS_lo - tau_init) / v_terminal
t_exit_BCS = (BCS_hi - tau_init) / v_terminal
t_cross_fold = (tau_fold - tau_init) / v_terminal

print(f"\n  Transit markers:")
print(f"    t_enter_BCS (tau={BCS_lo}): {t_enter_BCS:.6e}")
print(f"    t_cross_fold (tau={tau_fold:.3f}): {t_cross_fold:.6e}")
print(f"    t_exit_BCS (tau={BCS_hi}): {t_exit_BCS:.6e}")
print(f"    BCS transit time: {t_exit_BCS - t_enter_BCS:.6e}")

print(f"\n  Order parameter:")
print(f"    |Delta|_rms(t=0)     = {Delta_scalar[0]:.6f}")
print(f"    |Delta|_rms(t_fold)  = {Delta_scalar[np.argmin(np.abs(t_arr - t_cross_fold))]:.6f}")
i_post = np.argmin(np.abs(t_arr - t_exit_BCS))
print(f"    |Delta|_rms(t_exit)  = {Delta_scalar[i_post]:.6f}")
print(f"    |Delta|_rms(T/2)     = {Delta_scalar[len(t_arr)//2]:.6f}")
print(f"    |Delta|_rms(T_end)   = {Delta_scalar[-1]:.6f}")
print(f"    max |Delta|_rms      = {np.max(Delta_scalar):.6f}")

print(f"\n  Pair number:")
print(f"    N_pair(t=0)   = {N_pair_t[0]:.6f}")
print(f"    N_pair(t_end) = {N_pair_t[-1]:.6f}")

# ======================================================================
#  Step 7: Fourier analysis of post-transit gap dynamics
# ======================================================================
print("\n" + "=" * 78)
print("STEP 7: FOURIER ANALYSIS")
print("=" * 78)

# Post-transit signal: t > t_exit_BCS (well after BCS window)
# Use generous margin: start from 2 * t_exit_BCS to avoid transients
t_post_start = max(5.0 * t_exit_BCS, 0.01)  # at least 0.01 to clear initial transient

mask_post = t_arr > t_post_start
t_post = t_arr[mask_post]
Delta_sq_post = Delta_sq[mask_post]

if len(t_post) < 100:
    print("  WARNING: Very few post-transit points!")
else:
    print(f"  Post-transit window: t in [{t_post[0]:.4f}, {t_post[-1]:.4f}]")
    print(f"  Number of post-transit points: {len(t_post)}")

    # Uniform resampling for FFT
    dt_post = (t_post[-1] - t_post[0]) / (len(t_post) - 1)
    print(f"  dt (post-transit) = {dt_post:.6e}")
    print(f"  Nyquist frequency = {0.5/dt_post:.2f}")

    # Remove DC component
    Delta_sq_ac = Delta_sq_post - np.mean(Delta_sq_post)

    # Hann window to reduce spectral leakage
    window = np.hanning(len(Delta_sq_ac))
    Delta_sq_windowed = Delta_sq_ac * window

    # FFT
    N_fft = len(Delta_sq_windowed)
    fft_vals = np.fft.rfft(Delta_sq_windowed)
    freqs = np.fft.rfftfreq(N_fft, dt_post)
    power = np.abs(fft_vals)**2

    # Convert to angular frequency
    omega_fft = 2 * np.pi * freqs

    # Normalize power spectrum
    power_norm = power / np.max(power) if np.max(power) > 0 else power

    # Find peaks
    # Search in the range [0.3, 3.0] for physical content
    mask_phys = (omega_fft > 0.3) & (omega_fft < 3.0)
    if np.any(mask_phys):
        omega_phys = omega_fft[mask_phys]
        power_phys = power_norm[mask_phys]

        peaks, properties = find_peaks(power_phys, height=0.01, distance=5,
                                        prominence=0.005)

        print(f"\n  Peaks found in omega = [0.3, 3.0]:")
        peak_data = []
        for ip, p in enumerate(peaks):
            omega_p = omega_phys[p]
            height_p = power_phys[p]
            print(f"    Peak {ip}: omega = {omega_p:.4f}, rel_power = {height_p:.4f}")
            peak_data.append((omega_p, height_p))

        # Check GPV window [0.70, 0.85]
        mask_gpv = (omega_fft > 0.70) & (omega_fft < 0.85)
        if np.any(mask_gpv):
            gpv_power = np.max(power_norm[mask_gpv])
            gpv_omega = omega_fft[mask_gpv][np.argmax(power_norm[mask_gpv])]
            print(f"\n  GPV window [0.70, 0.85]:")
            print(f"    Peak omega = {gpv_omega:.4f}")
            print(f"    Peak power = {gpv_power:.6f}")

            # Q-factor: find FWHM around GPV peak
            if gpv_power > 0.001:
                # Find the peak in the GPV window more precisely
                half_max = gpv_power / 2.0
                gpv_region = power_norm[mask_gpv]
                gpv_omegas = omega_fft[mask_gpv]
                above_half = gpv_region >= half_max

                if np.any(above_half):
                    first_above = gpv_omegas[above_half][0]
                    last_above = gpv_omegas[above_half][-1]
                    fwhm = last_above - first_above
                    if fwhm > 0:
                        Q_factor = gpv_omega / fwhm
                    else:
                        # Peak is narrower than frequency resolution
                        domega = omega_fft[1] - omega_fft[0]
                        Q_factor = gpv_omega / domega
                    print(f"    FWHM = {fwhm:.4f}")
                    print(f"    Q-factor = {Q_factor:.2f}")
                else:
                    Q_factor = 0.0
                    fwhm = np.inf
            else:
                Q_factor = 0.0
                fwhm = np.inf
                print(f"    GPV power too low for Q measurement")
        else:
            gpv_omega = 0.0
            gpv_power = 0.0
            Q_factor = 0.0
            fwhm = np.inf
            print(f"\n  No data in GPV window!")

        # Also check pair-breaking continuum around omega ~ 0.93 and 2*Delta
        print(f"\n  Pair-breaking region [0.85, 1.10]:")
        mask_pb = (omega_fft > 0.85) & (omega_fft < 1.10)
        if np.any(mask_pb):
            pb_power = np.max(power_norm[mask_pb])
            pb_omega = omega_fft[mask_pb][np.argmax(power_norm[mask_pb])]
            print(f"    Peak omega = {pb_omega:.4f}, power = {pb_power:.6f}")
        else:
            pb_omega = 0.0
            pb_power = 0.0

        # Total spectral weight fractions
        total_weight = np.sum(power_norm[(omega_fft > 0.01)])
        gpv_weight = np.sum(power_norm[mask_gpv]) if np.any(mask_gpv) else 0
        pb_weight = np.sum(power_norm[mask_pb]) if np.any(mask_pb) else 0
        frac_gpv = gpv_weight / total_weight if total_weight > 0 else 0
        frac_pb = pb_weight / total_weight if total_weight > 0 else 0
        print(f"\n  Spectral weight fractions:")
        print(f"    GPV [0.70-0.85]: {frac_gpv:.4f} ({frac_gpv*100:.1f}%)")
        print(f"    PB [0.85-1.10]:  {frac_pb:.4f} ({frac_pb*100:.1f}%)")

    else:
        print("  No data in physical frequency range!")
        gpv_omega = 0.0
        gpv_power = 0.0
        Q_factor = 0.0
        fwhm = np.inf
        peak_data = []

# ======================================================================
#  Step 7b: Also do Fourier analysis of INDIVIDUAL mode kappa_k(t)
# ======================================================================
print("\n--- Mode-resolved Fourier analysis ---")

# The anomalous density kappa_k = u_k * v_k^* carries the pairing info
kappa_scalar = np.sum(rho[:, None] * np.abs(kappa_t)**2, axis=0)
kappa_sq_post = kappa_scalar[mask_post]
kappa_ac = kappa_sq_post - np.mean(kappa_sq_post)
kappa_windowed = kappa_ac * window

fft_kappa = np.fft.rfft(kappa_windowed)
power_kappa = np.abs(fft_kappa)**2
power_kappa_norm = power_kappa / np.max(power_kappa) if np.max(power_kappa) > 0 else power_kappa

mask_gpv_k = (omega_fft > 0.70) & (omega_fft < 0.85)
if np.any(mask_gpv_k):
    gpv_kappa_power = np.max(power_kappa_norm[mask_gpv_k])
    gpv_kappa_omega = omega_fft[mask_gpv_k][np.argmax(power_kappa_norm[mask_gpv_k])]
    print(f"  kappa^2 FT: GPV peak omega = {gpv_kappa_omega:.4f}, power = {gpv_kappa_power:.6f}")

# ======================================================================
#  Step 8: Alternative analysis — direct oscillation frequency from time domain
# ======================================================================
print("\n" + "=" * 78)
print("STEP 8: TIME-DOMAIN OSCILLATION ANALYSIS")
print("=" * 78)

# Look for oscillations in Delta_sq after transit
# Use zero-crossing method for frequency estimation
t_late = t_arr > 0.1  # well after transit
Delta_sq_late = Delta_sq[t_late]
t_late_arr = t_arr[t_late]

if len(Delta_sq_late) > 100:
    # Remove DC
    Delta_sq_mean = np.mean(Delta_sq_late)
    Delta_sq_fluct = Delta_sq_late - Delta_sq_mean

    # Find zero crossings
    zero_crossings = np.where(np.diff(np.sign(Delta_sq_fluct)))[0]
    if len(zero_crossings) >= 4:
        periods = np.diff(t_late_arr[zero_crossings[::2]])  # every other crossing = full period
        if len(periods) > 0:
            mean_period = np.mean(periods)
            omega_zc = 2 * np.pi / mean_period
            print(f"  Zero-crossing analysis:")
            print(f"    Number of zero crossings: {len(zero_crossings)}")
            print(f"    Mean half-period: {np.mean(np.diff(t_late_arr[zero_crossings])):.6f}")
            print(f"    Mean full period: {mean_period:.6f}")
            print(f"    omega_oscillation = {omega_zc:.4f}")
            print(f"    Relative amplitude: {np.std(Delta_sq_fluct) / Delta_sq_mean:.4f}" if Delta_sq_mean > 0 else "")
        else:
            omega_zc = 0.0
            print(f"  Not enough oscillation periods found")
    else:
        omega_zc = 0.0
        print(f"  Zero crossings: {len(zero_crossings)} (too few)")

    # Oscillation amplitude decay?
    if len(zero_crossings) > 10:
        env_upper = []
        env_t = []
        for i in range(len(zero_crossings) - 1):
            idx_range = slice(zero_crossings[i], zero_crossings[i+1])
            seg = Delta_sq_fluct[idx_range]
            if len(seg) > 0:
                env_upper.append(np.max(np.abs(seg)))
                env_t.append(np.mean(t_late_arr[idx_range]))
        if len(env_upper) > 3:
            env_upper = np.array(env_upper)
            env_t = np.array(env_t)
            # Fit exponential decay
            if np.all(env_upper > 0):
                log_env = np.log(env_upper)
                p = np.polyfit(env_t, log_env, 1)
                gamma_decay = -p[0]
                t_decay = 1.0 / gamma_decay if gamma_decay > 0 else np.inf
                print(f"\n  Envelope analysis:")
                print(f"    Decay rate gamma = {gamma_decay:.4f}")
                print(f"    Decay time = {t_decay:.2f}")
                if omega_zc > 0:
                    Q_time_domain = omega_zc / (2 * gamma_decay) if gamma_decay > 0 else np.inf
                    print(f"    Q (time domain) = {Q_time_domain:.2f}")
else:
    omega_zc = 0.0
    print(f"  Too few post-transit points for time-domain analysis")

# ======================================================================
#  Step 9: Cross-checks with S37 and S38
# ======================================================================
print("\n" + "=" * 78)
print("STEP 9: CROSS-CHECKS")
print("=" * 78)

print(f"  S37 reference: omega_PV = {omega_PV_s37:.4f}")
print(f"  S38 predictions:")
print(f"    GPV strength retention: 50-70% (S38 W1)")
print(f"    Q > 5 (S38 W1 prediction)")
print(f"    Transit destroys condensate: P_exc = 1.0 (S38 KZ)")
print(f"    Post-transit: GGE (non-thermal)")
print(f"    t_therm/t_transit = 5253 (S39 INTEG-39)")

# Energy check
E_init_total = np.sum(rho * xi_init * np.abs(v0)**2)
print(f"\n  Initial kinetic energy: {E_init_total:.6f}")

# ======================================================================
#  Step 10: Gate verdict
# ======================================================================
print("\n" + "=" * 78)
print("STEP 10: GATE VERDICT")
print("=" * 78)

# Gate: BDG-SIM-39
# PASS: GPV peak visible in FT at omega in [0.70, 0.85] with Q > 3
# FAIL: no identifiable GPV peak

# Use the best Q estimate (from FT or time domain)
try:
    Q_best = Q_factor
except:
    Q_best = 0.0

try:
    if omega_zc > 0 and 'Q_time_domain' in dir():
        Q_td = Q_time_domain
    else:
        Q_td = 0.0
except:
    Q_td = 0.0

# Also check: is there ANY oscillation at the GPV frequency?
gpv_detected = (gpv_power > 0.01)  # at least 1% of max power
gpv_in_range = (0.70 <= gpv_omega <= 0.85) if gpv_detected else False

# Also check time-domain oscillation frequency
try:
    td_in_range = (0.70 <= omega_zc <= 0.85)
except:
    td_in_range = False

print(f"\n  GPV peak in FT:")
print(f"    omega = {gpv_omega:.4f}")
print(f"    Relative power = {gpv_power:.6f}")
print(f"    Q (FT) = {Q_best:.2f}")
print(f"    In range [0.70, 0.85]? {gpv_in_range}")

print(f"\n  Time-domain oscillation:")
print(f"    omega_zc = {omega_zc:.4f}")
try:
    print(f"    Q (TD) = {Q_td:.2f}")
except:
    print(f"    Q (TD) = N/A")
print(f"    In range [0.70, 0.85]? {td_in_range}")

# Verdict
if gpv_in_range and Q_best > 3.0:
    verdict = "PASS"
    verdict_detail = f"GPV peak at omega={gpv_omega:.4f} with Q={Q_best:.1f} > 3"
elif td_in_range and Q_td > 3.0:
    verdict = "PASS"
    verdict_detail = f"GPV oscillation at omega={omega_zc:.4f} with Q_TD={Q_td:.1f} > 3"
elif gpv_detected and gpv_in_range:
    verdict = "MARGINAL"
    verdict_detail = f"GPV peak at omega={gpv_omega:.4f} but Q={Q_best:.1f} < 3"
else:
    verdict = "FAIL"
    # Identify what IS the dominant frequency
    if len(peak_data) > 0:
        dom_omega, dom_power = peak_data[0]
        verdict_detail = f"No GPV in [0.70, 0.85]. Dominant: omega={dom_omega:.4f}"
    else:
        verdict_detail = "No identifiable oscillation peaks"

print(f"\n{'='*78}")
print(f"  GATE BDG-SIM-39: {verdict}")
print(f"  Detail: {verdict_detail}")
print(f"{'='*78}")

# ======================================================================
#  Step 11: Save data
# ======================================================================
print("\n" + "=" * 78)
print("STEP 11: SAVE DATA")
print("=" * 78)

save_path = os.path.join(SCRIPT_DIR, 's39_bdg_simulation.npz')
np.savez(save_path,
    # Time series
    t=t_arr,
    tau_of_t=tau_t_arr,
    Delta_sq=Delta_sq,
    Delta_scalar=Delta_scalar,
    Delta_B2_sq=Delta_B2_sq,
    Delta_B1_sq=Delta_B1_sq,
    Delta_B3_sq=Delta_B3_sq,
    N_pair=N_pair_t,
    norm_max_dev=norm_max_dev,
    # Fourier analysis
    omega_fft=omega_fft,
    power_norm=power_norm,
    power_kappa_norm=power_kappa_norm,
    # GPV results
    gpv_omega=gpv_omega,
    gpv_power=gpv_power,
    Q_factor=Q_best,
    Q_time_domain=Q_td,
    omega_zc=omega_zc,
    fwhm=fwhm,
    # Gate
    verdict=np.array([verdict]),
    verdict_detail=np.array([verdict_detail]),
    # Parameters
    tau_init=tau_init,
    tau_final=tau_final,
    v_terminal=v_terminal,
    T_total=T_total,
    t_transit=t_transit,
    n_modes=n_modes,
    # Initial state
    u0=u0,
    v0=v0,
    Delta0=Delta0,
    # Reference
    omega_PV_s37=omega_PV_s37,
    E_cond_s37=E_cond_s37,
)
print(f"  Saved: {save_path}")

# ======================================================================
#  Step 12: Plots
# ======================================================================
print("\n" + "=" * 78)
print("STEP 12: PLOTS")
print("=" * 78)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: |Delta(t)|^2 time series
ax = axes[0, 0]
ax.semilogy(t_arr, Delta_sq, 'b-', linewidth=0.5, label=r'$|\Delta(t)|^2$ (total)')
ax.semilogy(t_arr, Delta_B2_sq, 'r-', linewidth=0.5, alpha=0.7, label='B2 only')
ax.axvline(t_enter_BCS, color='gray', linestyle='--', alpha=0.5, label='BCS window')
ax.axvline(t_exit_BCS, color='gray', linestyle='--', alpha=0.5)
ax.axvline(t_cross_fold, color='green', linestyle=':', alpha=0.5, label='fold')
ax.set_xlabel('t (natural units)')
ax.set_ylabel(r'$|\Delta(t)|^2$')
ax.set_title(r'Order Parameter $|\Delta(t)|^2$')
ax.legend(fontsize=8)

# Panel 2: Zoom on transit and early post-transit
ax = axes[0, 1]
t_zoom_max = min(1.0, T_total)
mask_zoom = t_arr < t_zoom_max
ax.plot(t_arr[mask_zoom], Delta_sq[mask_zoom], 'b-', linewidth=0.8)
ax.axvline(t_enter_BCS, color='gray', linestyle='--', alpha=0.5)
ax.axvline(t_exit_BCS, color='gray', linestyle='--', alpha=0.5)
ax.axvline(t_cross_fold, color='green', linestyle=':', alpha=0.5)
ax.set_xlabel('t (natural units)')
ax.set_ylabel(r'$|\Delta(t)|^2$')
ax.set_title(r'Early-time zoom (t < 1)')

# Panel 3: Power spectrum
ax = axes[1, 0]
mask_plot = (omega_fft > 0.01) & (omega_fft < 3.0)
ax.semilogy(omega_fft[mask_plot], power_norm[mask_plot], 'b-', linewidth=0.8,
            label=r'$|\Delta|^2$ FT')
ax.semilogy(omega_fft[mask_plot], power_kappa_norm[mask_plot], 'r--', linewidth=0.8,
            alpha=0.7, label=r'$|\kappa|^2$ FT')
ax.axvline(omega_PV_s37, color='green', linestyle=':', alpha=0.7,
           label=f'S37 GPV ({omega_PV_s37:.3f})')
ax.axvspan(0.70, 0.85, alpha=0.1, color='green', label='GPV window')
ax.set_xlabel(r'$\omega$ (natural units)')
ax.set_ylabel('Power (normalized)')
ax.set_title('Fourier Spectrum (post-transit)')
ax.legend(fontsize=8)

# Panel 4: Quasiparticle occupation
ax = axes[1, 1]
for k in range(4):
    ax.plot(t_arr, np.abs(v_t[k])**2, label=f'B2[{k}]', linewidth=0.5)
ax.plot(t_arr, np.abs(v_t[4])**2, 'k-', label='B1', linewidth=0.8)
for k in range(5, 8):
    ax.plot(t_arr, np.abs(v_t[k])**2, '--', label=f'B3[{k-5}]', linewidth=0.5)
ax.axvline(t_enter_BCS, color='gray', linestyle='--', alpha=0.5)
ax.axvline(t_exit_BCS, color='gray', linestyle='--', alpha=0.5)
ax.set_xlabel('t (natural units)')
ax.set_ylabel(r'$|v_k(t)|^2$')
ax.set_title('Quasiparticle occupation')
ax.legend(fontsize=7, ncol=2)

plt.suptitle(f'BDG-SIM-39: BdG Time-Dependent Simulation | Verdict: {verdict}',
             fontsize=13, fontweight='bold')
plt.tight_layout()

plot_path = os.path.join(SCRIPT_DIR, 's39_bdg_simulation.png')
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"  Saved: {plot_path}")

print(f"\n  Total wall time: {time.time() - t0_wall:.1f} s")
print(f"\n{'='*78}")
print("DONE")
print(f"{'='*78}")
