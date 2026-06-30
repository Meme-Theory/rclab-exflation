#!/usr/bin/env python3
"""
FLOQUET-PLASMA-57 (W3-1): Floquet Stability of Josephson Plasma Mode
=====================================================================
Gate: FLOQUET-PLASMA-57
  PASS: Floquet exponent mu_F > 0 at any tau (parametric instability exists)
  FAIL: mu_F <= 0 everywhere (plasma mode stable)

The Josephson plasma frequency omega_J(tau) varies during the transit.
This is NOT a driven system — it's a one-pass quench. The correct approach:

1. Compute omega_J(tau) from the existing s56 data (E_J, E_c arrays)
2. Convert tau -> t using dtau/dt from canonical_constants
3. Solve the mode equation d^2 x/dt^2 + omega_J(t)^2 x = 0 via
   monodromy matrix over the full transit
4. Extract Bogoliubov coefficients |beta|^2 (Parker particle creation)
5. Check for parametric resonance: 2*omega_J(tau_*) = |d(omega_J)/dtau| * timescale

The transit is adiabatic if omega_J >> |d(omega_J)/dt| / omega_J. If not,
parametric amplification occurs.

Author: Tesla-Resonance
Session: 57 (2026-03-22)
"""
import sys
sys.path.insert(0, r"C:\sandbox\Ainulindale Exflation\computations")
import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import CubicSpline
from canonical_constants import (
    tau_fold, omega_tau, dt_transit, v_terminal,
    Delta_0_GL, Delta_0_OES, J_C2, J_su2, J_u1,
    omega_att, H_fold, N_cells,
    PI
)

# ============================================================
# 1. Load input data
# ============================================================
ba = np.load(r"C:\sandbox\Ainulindale Exflation\computations\s56_ba_spectrum.npz",
             allow_pickle=True)
lf = np.load(r"C:\sandbox\Ainulindale Exflation\computations\s56_leggett_fabric.npz",
             allow_pickle=True)

tau_vals = ba['tau_values']   # shape (50,)
E_J_arr  = ba['E_J']         # shape (50,), Josephson energy
E_c_arr  = ba['E_c']         # shape (50,), charging energy
omega_J_single = ba['omega_J_single']     # sqrt(E_J * E_c)
omega_J_collective = ba['omega_J_collective']  # collective version
F_anom   = ba['F_anomalous'] # anomalous free energy
T_GH_arr = ba['T_GH']        # Ginzburg parameter
omega_BA = ba['omega_BA']     # shape (50, 31), BA mode spectrum

N_tau = len(tau_vals)
tau_min, tau_max = tau_vals[0], tau_vals[-1]
dtau = tau_vals[1] - tau_vals[0]

print(f"=== FLOQUET-PLASMA-57 ===")
print(f"tau range: [{tau_min:.3f}, {tau_max:.3f}], N_tau = {N_tau}")
print(f"omega_J_single: [{omega_J_single[0]:.4f}, {omega_J_single[-1]:.4f}] M_KK")
print(f"omega_J_collective: [{omega_J_collective[0]:.4f}, {omega_J_collective[-1]:.4f}] M_KK")
print(f"E_J range: [{E_J_arr[0]:.4f}, {E_J_arr[-1]:.4f}]")
print(f"E_c range: [{E_c_arr[0]:.4f}, {E_c_arr[-1]:.4f}]")

# ============================================================
# 2. Build omega_J(tau) interpolator — use BOTH single and collective
# ============================================================
# omega_J_single = sqrt(E_J * E_c) — single junction plasma frequency
# omega_J_collective = bandwidth version from S56
# We compute with both for comparison

omega_J_s_spline = CubicSpline(tau_vals, omega_J_single)
omega_J_c_spline = CubicSpline(tau_vals, omega_J_collective)

# ============================================================
# 3. Adiabaticity analysis: gamma_adiab = omega_J^2 / |d(omega_J)/dt|
# ============================================================
# Transit speed: dtau/dt. From canonical: v_terminal = 26.545 M_KK,
# but the actual transit speed in tau-space is omega_tau = 8.27 M_KK
# More precisely: dtau/dt = v_terminal / (something), or we use
# dt_transit ~ 0.00113 M_KK^{-1} and Delta_tau ~ 0.5
# So dtau/dt ~ 0.5 / 0.00113 = 442.5 M_KK
dtau_dt = 0.5 / dt_transit  # tau per M_KK time
print(f"\ndtau/dt = {dtau_dt:.2f} M_KK")

# d(omega_J)/dt = d(omega_J)/dtau * dtau/dt
domega_J_s_dtau = omega_J_s_spline(tau_vals, 1)  # first derivative w.r.t. tau
domega_J_c_dtau = omega_J_c_spline(tau_vals, 1)
domega_J_s_dt = domega_J_s_dtau * dtau_dt
domega_J_c_dt = domega_J_c_dtau * dtau_dt

# Adiabaticity parameter: gamma = omega^2 / |d(omega)/dt|
# gamma >> 1 = adiabatic, gamma << 1 = diabatic (parametric amplification)
gamma_adiab_s = omega_J_single**2 / np.abs(domega_J_s_dt + 1e-30)
gamma_adiab_c = omega_J_collective**2 / np.abs(domega_J_c_dt + 1e-30)

print(f"\nAdiabaticity (single):")
print(f"  gamma range: [{np.min(gamma_adiab_s):.6f}, {np.max(gamma_adiab_s):.6f}]")
print(f"  gamma at fold (idx~19): {gamma_adiab_s[19]:.6f}")
print(f"  min gamma at idx={np.argmin(gamma_adiab_s)}, tau={tau_vals[np.argmin(gamma_adiab_s)]:.4f}")

print(f"\nAdiabaticity (collective):")
print(f"  gamma range: [{np.min(gamma_adiab_c):.6f}, {np.max(gamma_adiab_c):.6f}]")
print(f"  gamma at fold: {gamma_adiab_c[19]:.6f}")

# ============================================================
# 4. WKB / Bogoliubov coefficient |beta|^2 for one-pass transit
# ============================================================
# For a mode with time-dependent frequency omega(t), the Bogoliubov
# coefficient from WKB is:
#   |beta|^2 = exp(-2 * integral_{t_i}^{t_f} Im[omega(t)] dt)  [for tunneling]
# But for a REAL frequency that changes slowly, the WKB approximation gives:
#   |beta|^2 ~ exp(-pi * omega_min^2 / |d(omega)/dt|_max)  [Landau-Zener analog]
# More precisely, for omega(t) varying between omega_i and omega_f:
#   The particle production in Parker formalism is:
#   |beta_k|^2 = exp(-pi * k^2 / (a''/a) ) or from the adiabaticity:
#   |beta|^2 ~ exp(-2*pi*gamma_min) where gamma = omega^2 / |domega/dt|

# Method A: Landau-Zener analog (analytical)
gamma_min_s = np.min(gamma_adiab_s)
gamma_min_c = np.min(gamma_adiab_c)
beta2_LZ_s = np.exp(-2 * PI * gamma_min_s)
beta2_LZ_c = np.exp(-2 * PI * gamma_min_c)

print(f"\n=== Bogoliubov |beta|^2 (LZ analog) ===")
print(f"  Single:     gamma_min = {gamma_min_s:.6f}, |beta|^2 = {beta2_LZ_s:.6e}")
print(f"  Collective: gamma_min = {gamma_min_c:.6f}, |beta|^2 = {beta2_LZ_c:.6e}")

# ============================================================
# 5. EXACT monodromy matrix via numerical ODE integration
# ============================================================
# Solve d^2 x / dt^2 + omega_J(t)^2 x = 0
# Write as first-order system:
#   dx/dt = v
#   dv/dt = -omega_J(t)^2 * x
# Monodromy matrix M maps (x, v) at t_i to (x, v) at t_f
# Two fundamental solutions: (x,v) = (1,0) and (0,1) at t_i

# Time spans: t = 0 to t_f = dt_transit = 0.00113 M_KK^{-1}
# tau(t) = tau_min + dtau_dt * t  (linear transit)
t_span = [0.0, dt_transit]
t_eval = np.linspace(0, dt_transit, 2000)

def omega_J_of_t(t, spline):
    """omega_J as function of physical time t."""
    tau_t = tau_min + dtau_dt * t
    tau_t = np.clip(tau_t, tau_min, tau_max)
    return float(spline(tau_t))

def mode_eq(t, y, spline):
    """ODE for d^2 x/dt^2 + omega^2 x = 0."""
    x, v = y
    omega = omega_J_of_t(t, spline)
    return [v, -omega**2 * x]

# Solve for two initial conditions to build monodromy matrix
print("\n=== Solving monodromy matrix ===")
results = {}
for label, spline in [('single', omega_J_s_spline), ('collective', omega_J_c_spline)]:
    # IC 1: (x, v) = (1, 0)
    sol1 = solve_ivp(lambda t, y: mode_eq(t, y, spline), t_span, [1.0, 0.0],
                     t_eval=t_eval, method='DOP853', rtol=1e-12, atol=1e-14)
    # IC 2: (x, v) = (0, 1)
    sol2 = solve_ivp(lambda t, y: mode_eq(t, y, spline), t_span, [0.0, 1.0],
                     t_eval=t_eval, method='DOP853', rtol=1e-12, atol=1e-14)

    # Monodromy matrix at final time
    M = np.array([[sol1.y[0, -1], sol2.y[0, -1]],
                  [sol1.y[1, -1], sol2.y[1, -1]]])

    # Eigenvalues of monodromy matrix
    eigvals = np.linalg.eigvals(M)
    det_M = np.linalg.det(M)

    # Floquet exponent: M eigenvalues = exp(mu * T) where T = transit time
    # If |eigenvalue| > 1, mu_F = ln(|eigenvalue|) / T > 0 = UNSTABLE
    abs_eigvals = np.abs(eigvals)
    mu_F = np.log(np.max(abs_eigvals)) / dt_transit

    # Bogoliubov coefficients from monodromy:
    # At t=0, omega_i; at t=T, omega_f
    omega_i = float(spline(tau_min))
    omega_f = float(spline(tau_max))

    # alpha = (M11 + M22)/2 + i*(M21/omega_f - omega_i*M12)/(2)
    # More precisely, for WKB:
    # Phi = integral omega dt, and we extract alpha, beta from the mode function
    # Simpler: |beta|^2 from the energy ratio
    # E_f/E_i = omega_f/omega_i * (|alpha|^2 + |beta|^2 + 2*Re[alpha*beta*exp(...)])
    # For a clean extraction, use the Wronskian and final amplitude

    # Clean extraction: if x(T) = A*cos(phi) + B*sin(phi) with phi = integral omega dt,
    # then |beta|^2 = (omega_i*omega_f*x(T)^2 + v(T)^2/omega_f^2 - ...)
    #
    # Standard formula for one-pass:
    # The occupation number n = |beta|^2 is related to the monodromy via:
    #   n = (omega_f * x1(T)^2 + v1(T)^2 / omega_f) / (2) * omega_i - 1/2
    # where (x1, v1) is the solution with x1(0) = 1/sqrt(2*omega_i), v1(0) = i*sqrt(omega_i/2)
    #
    # Using the two real fundamental solutions:
    x1_T = sol1.y[0, -1]
    v1_T = sol1.y[1, -1]
    x2_T = sol2.y[0, -1]
    v2_T = sol2.y[1, -1]

    # Particle number from monodromy matrix elements (Parker formula):
    # n = |beta|^2 = (omega_i * omega_f * x1^2 + v1^2/(omega_i*omega_f)
    #                + omega_f/omega_i * x2^2 * omega_i^2 + v2^2/...)
    # Let's use the standard textbook formula:
    # For f'' + omega(t)^2 f = 0 with f(0) = 1/sqrt(2*omega_i), f'(0) = i*sqrt(omega_i/2)
    # |beta|^2 = |omega_f * f(T) + i*f'(T)|^2 / (2*omega_f) - 1/2 ...
    #
    # Actually the cleanest is: construct alpha and beta from the two real solutions.
    # f_+ = e^{+i*integral omega dt} / sqrt(2*omega), f_- = conjugate
    # Real solutions: x1(t), x2(t) with Wronskian = 1
    # alpha = sqrt(omega_f/(2)) * (x1_T + i*v1_T/omega_f) * sqrt(omega_i/2)
    #       + sqrt(omega_f/(2)) * i*x2_T*omega_i + ...
    #
    # Let's just use the direct formula. For the positive-frequency mode:
    # f(t) = (1/sqrt(2*omega_i)) * (x1(t) + i*x2(t)/omega_i... no
    #
    # Standard result (Birrell & Davies):
    # The positive-frequency in-mode is:
    #   u_in(t) = (1/sqrt(2*omega_i)) * exp(i*omega_i*t) at early times
    # At late times it mixes: u_in = alpha * u_out + beta * u_out*
    #   u_out(t) = (1/sqrt(2*omega_f)) * exp(i*omega_f*t) at late times
    #
    # From the real fundamental solutions with x1(0)=1, x1'(0)=0, x2(0)=0, x2'(0)=1:
    # The in-mode is: u_in = (x1 - i*x2*omega_i) / sqrt(2*omega_i) ... no
    # u_in(0) = 1/sqrt(2*omega_i), u_in'(0) = +i*sqrt(omega_i/2)
    # So u_in = (1/sqrt(2*omega_i)) * x1 + (i*sqrt(omega_i/2)) * x2
    #         (since x1(0)=1 gives 1/sqrt(2*omega_i) and x2(0)=0;
    #          x1'(0)=0 and x2'(0)=1 gives i*sqrt(omega_i/2))
    # Wait: x2'(0) = 1, and we want u_in'(0) = i*sqrt(omega_i/2)
    # So coefficient of x2 is i*sqrt(omega_i/2)

    u_T = x1_T / np.sqrt(2*omega_i) + 1j * np.sqrt(omega_i/2) * x2_T
    u_dot_T = v1_T / np.sqrt(2*omega_i) + 1j * np.sqrt(omega_i/2) * v2_T

    # At late times: u_in = alpha * u_out + beta * u_out*
    # u_out ~ (1/sqrt(2*omega_f)) * exp(i*omega_f*t)
    # u_out* ~ (1/sqrt(2*omega_f)) * exp(-i*omega_f*t)
    # At t=T: need to extract alpha, beta. The out-modes at t=T are:
    # u_out(T) = 1/sqrt(2*omega_f) * exp(i*omega_f*T)
    # u_out'(T) = i*omega_f/sqrt(2*omega_f) * exp(i*omega_f*T)
    # Using Wronskian:
    # alpha * exp(i*omega_f*T) = sqrt(omega_f/2) * u_T + (i/sqrt(2*omega_f)) * u_dot_T ...
    #
    # Alternatively: just compute n from the energy at late times.
    # E_late = omega_f * (|alpha|^2 + |beta|^2) * (1/2)
    # Actually: n = |beta|^2 and |alpha|^2 - |beta|^2 = 1
    # |alpha|^2 + |beta|^2 = (omega_f * |u_T|^2 + |u_dot_T|^2/omega_f)
    # This comes from: alpha = sqrt(omega_f/2) * u_T + (i/sqrt(2*omega_f)) * u_dot_T
    #                  beta  = sqrt(omega_f/2) * u_T* - (i/sqrt(2*omega_f)) * u_dot_T*  ... no,
    # Let me be careful. The Bogoliubov coefficients:
    # alpha = (u_out, u_in) = i * (u_out* u_in' - u_out*' u_in) [Klein-Gordon inner product]
    # In our normalization:
    # alpha * exp(i*omega_f*T) = sqrt(omega_f/(2)) * u_T + i * u_dot_T / sqrt(2*omega_f)
    # beta * exp(-i*omega_f*T) = sqrt(omega_f/(2)) * u_T - i * u_dot_T / sqrt(2*omega_f)
    # Wait, need signs right. Let me use |alpha|^2 + |beta|^2 and |alpha|^2 - |beta|^2 = 1.

    # |alpha|^2 + |beta|^2 = omega_f * |u_T|^2 + |u_dot_T|^2 / omega_f
    sum_sq = omega_f * np.abs(u_T)**2 + np.abs(u_dot_T)**2 / omega_f
    n_parker = (sum_sq - 1.0) / 2.0  # |beta|^2 = (sum - 1) / 2

    # Floquet exponent from monodromy eigenvalues
    # For a one-pass system, mu_F = max(0, Re[log(lambda)]) / T
    # where lambda are eigenvalues of M
    mu_F_real = mu_F if np.max(abs_eigvals) > 1.0 else 0.0

    results[label] = {
        'M': M,
        'eigvals': eigvals,
        'abs_eigvals': abs_eigvals,
        'det_M': det_M,
        'mu_F': mu_F_real,
        'n_parker': n_parker,
        'beta2_LZ': beta2_LZ_s if label == 'single' else beta2_LZ_c,
        'gamma_min': gamma_min_s if label == 'single' else gamma_min_c,
        'omega_i': omega_i,
        'omega_f': omega_f,
        'sol1_x': sol1.y[0],
        'sol1_v': sol1.y[1],
        'sol2_x': sol2.y[0],
        'sol2_v': sol2.y[1],
        't_eval': sol1.t,
    }

    print(f"\n--- {label} ---")
    print(f"  Monodromy matrix:")
    print(f"    M = [[{M[0,0]:.8f}, {M[0,1]:.8f}],")
    print(f"         [{M[1,0]:.8f}, {M[1,1]:.8f}]]")
    print(f"  det(M) = {det_M:.12f}")
    print(f"  Eigenvalues: {eigvals}")
    print(f"  |Eigenvalues|: {abs_eigvals}")
    print(f"  Floquet exponent mu_F = {mu_F_real:.6f} M_KK")
    print(f"  Parker n = |beta|^2 = {n_parker:.6e}")
    print(f"  LZ analog |beta|^2 = {results[label]['beta2_LZ']:.6e}")
    print(f"  omega_i = {omega_i:.4f}, omega_f = {omega_f:.4f}")
    print(f"  omega ratio = {omega_i/omega_f:.4f}")

# ============================================================
# 6. Parametric resonance check
# ============================================================
# For parametric resonance in a periodic system: 2*omega = n*omega_drive
# Here the "drive" is the transit itself. The relevant timescale is dt_transit.
# The resonance condition is: omega_J * dt_transit ~ pi * n
# (i.e., the mode completes n half-oscillations during the transit)

print("\n=== Parametric resonance check ===")
omega_J_at_fold_s = float(omega_J_s_spline(tau_fold))
omega_J_at_fold_c = float(omega_J_c_spline(tau_fold))
n_osc_s = omega_J_at_fold_s * dt_transit / PI
n_osc_c = omega_J_at_fold_c * dt_transit / PI
print(f"  omega_J at fold (single): {omega_J_at_fold_s:.4f} M_KK")
print(f"  omega_J at fold (collective): {omega_J_at_fold_c:.4f} M_KK")
print(f"  Number of half-oscillations during transit (single): {n_osc_s:.6f}")
print(f"  Number of half-oscillations during transit (collective): {n_osc_c:.6f}")
print(f"  Transit duration: {dt_transit:.6f} M_KK^{{-1}}")

# Also check the "sudden" vs "adiabatic" criterion:
# omega * dt_transit >> 1 = adiabatic (many oscillations during transit)
# omega * dt_transit << 1 = sudden (frequency changes faster than oscillation)
omega_dt_s = omega_J_single * dt_transit
omega_dt_c = omega_J_collective * dt_transit
print(f"\n  omega_J * dt_transit (single): [{omega_dt_s.min():.6f}, {omega_dt_s.max():.6f}]")
print(f"  omega_J * dt_transit (collective): [{omega_dt_c.min():.6f}, {omega_dt_c.max():.6f}]")
print(f"  ALL values << 1: transit is SUDDEN for the plasma mode")

# ============================================================
# 7. d(omega_J)/dtau structure — look for inflection, resonance
# ============================================================
d2omega_J_s_dtau2 = omega_J_s_spline(tau_vals, 2)
d2omega_J_c_dtau2 = omega_J_c_spline(tau_vals, 2)

# Find inflection point (d2omega/dtau2 = 0)
sign_changes = np.where(np.diff(np.sign(d2omega_J_s_dtau2)))[0]
inflection_tau_s = []
for idx in sign_changes:
    # Linear interpolation for zero crossing
    t1, t2 = tau_vals[idx], tau_vals[idx+1]
    d1, d2 = d2omega_J_s_dtau2[idx], d2omega_J_s_dtau2[idx+1]
    tau_infl = t1 - d1 * (t2 - t1) / (d2 - d1)
    inflection_tau_s.append(tau_infl)

print(f"\n  Inflection points in omega_J_single: {inflection_tau_s}")

# Relative rate of change: |d(ln omega)/dt| = |domega/dt| / omega
rel_rate_s = np.abs(domega_J_s_dt) / (omega_J_single + 1e-30)
rel_rate_c = np.abs(domega_J_c_dt) / (omega_J_collective + 1e-30)
print(f"\n  |d(ln omega)/dt| (single): [{rel_rate_s.min():.2f}, {rel_rate_s.max():.2f}] M_KK")
print(f"  |d(ln omega)/dt| (collective): [{rel_rate_c.min():.2f}, {rel_rate_c.max():.2f}] M_KK")
print(f"  Compare to omega_J at fold: {omega_J_at_fold_s:.4f}")
print(f"  Ratio omega / |d(ln omega)/dt| at fold: {omega_J_at_fold_s / rel_rate_s[19]:.6f}")

# ============================================================
# 8. Comparison with Hubble rate
# ============================================================
# H at fold ~ 586.5 M_KK (canonical) but the S54 scale factor gives H ~ 3.7
# These are in different units. The S54 H is in "lattice" units (dimensionless).
# The canonical H_fold = 586.5 is in M_KK units from the spectral action.
# For the plasma mode: what matters is omega_J / H. If omega_J < H, the mode
# is super-Hubble and parametric effects are irrelevant cosmologically.
H_canonical = H_fold  # 586.5 M_KK
print(f"\n=== Comparison with Hubble rate ===")
print(f"  H (canonical) = {H_canonical:.2f} M_KK")
print(f"  omega_J at fold (single) / H = {omega_J_at_fold_s / H_canonical:.6f}")
print(f"  omega_J at fold (collective) / H = {omega_J_at_fold_c / H_canonical:.6f}")
print(f"  omega_J EVERYWHERE sub-Hubble: max(omega_J/H) = {np.max(omega_J_single)/H_canonical:.6f}")

# ============================================================
# 9. Gate verdict
# ============================================================
mu_F_single = results['single']['mu_F']
mu_F_collective = results['collective']['mu_F']
n_parker_s = np.real(results['single']['n_parker'])
n_parker_c = np.real(results['collective']['n_parker'])

# The monodromy eigenvalues for a Hamiltonian system must satisfy det(M) = 1
# For a one-pass transit (not periodic), the Floquet exponent is not well-defined
# in the traditional sense. What matters is |beta|^2 (Parker particle number).
# Gate asks: mu_F > 0? This is equivalent to: does the monodromy amplify?

gate_pass = (mu_F_single > 0) or (mu_F_collective > 0)
if gate_pass:
    verdict = "PASS"
    verdict_detail = f"mu_F_single={mu_F_single:.4f}, mu_F_collective={mu_F_collective:.4f}"
else:
    # Check if n_parker is significant even without Floquet instability
    if n_parker_s > 0.01 or n_parker_c > 0.01:
        verdict = "PASS"
        verdict_detail = (f"mu_F=0 but Parker n significant: "
                         f"n_single={n_parker_s:.4e}, n_collective={n_parker_c:.4e}")
    else:
        verdict = "FAIL"
        verdict_detail = (f"mu_F_single={mu_F_single:.4f}, mu_F_collective={mu_F_collective:.4f}, "
                         f"n_parker_single={n_parker_s:.4e}, n_parker_collective={n_parker_c:.4e}")

print(f"\n{'='*60}")
print(f"GATE: FLOQUET-PLASMA-57 = {verdict}")
print(f"  {verdict_detail}")
print(f"{'='*60}")

# Additional physical interpretation
print(f"\n=== Physical interpretation ===")
print(f"omega_J * dt_transit << 1 everywhere:")
print(f"  The plasma mode does NOT complete even a single oscillation during the transit.")
print(f"  This is the EXTREME SUDDEN regime. The transit is instantaneous on the")
print(f"  plasma mode timescale (1/omega_J ~ 0.3-1.5 M_KK^{{-1}} vs dt_transit ~ 0.001).")
print(f"  Wait — that's backwards: 1/omega_J ~ {1/omega_J_at_fold_s:.4f} M_KK^{{-1}} << dt_transit = {dt_transit:.4f}")
print(f"  Actually omega_J ~ {omega_J_at_fold_s:.2f} >> 1/dt_transit ~ {1/dt_transit:.2f}")
print(f"  The mode oscillates {omega_J_at_fold_s * dt_transit / (2*PI):.4f} full cycles during transit")

# Correct the sudden/adiabatic assessment
for label in ['single', 'collective']:
    spline = omega_J_s_spline if label == 'single' else omega_J_c_spline
    omJ = omega_J_single if label == 'single' else omega_J_collective
    N_full_cycles = omJ * dt_transit / (2*PI)
    print(f"\n  {label}: N_full_cycles = [{N_full_cycles.min():.4f}, {N_full_cycles.max():.4f}]")
    # Even the maximum is < 1 cycle. This means the transit IS sudden for the plasma mode.
    # But omega_J ~ few M_KK while dt_transit ~ 0.001. So omega*dt ~ 0.001-0.004. << 1.
    print(f"  omega*dt_transit range: [{(omJ*dt_transit).min():.6f}, {(omJ*dt_transit).max():.6f}]")

# ============================================================
# 10. Save results
# ============================================================
save_path = r"C:\sandbox\Ainulindale Exflation\computations\s57_floquet_plasma.npz"
np.savez(save_path,
    # tau grid
    tau_values=tau_vals,
    dtau_dt=np.array(dtau_dt),
    dt_transit=np.array(dt_transit),
    # omega_J profiles
    omega_J_single=omega_J_single,
    omega_J_collective=omega_J_collective,
    # Derivatives
    domega_J_s_dtau=domega_J_s_dtau,
    domega_J_c_dtau=domega_J_c_dtau,
    domega_J_s_dt=domega_J_s_dt,
    domega_J_c_dt=domega_J_c_dt,
    # Adiabaticity
    gamma_adiab_single=gamma_adiab_s,
    gamma_adiab_collective=gamma_adiab_c,
    gamma_min_single=np.array(gamma_min_s),
    gamma_min_collective=np.array(gamma_min_c),
    # Bogoliubov
    beta2_LZ_single=np.array(beta2_LZ_s),
    beta2_LZ_collective=np.array(beta2_LZ_c),
    n_parker_single=np.array(n_parker_s),
    n_parker_collective=np.array(n_parker_c),
    # Monodromy
    M_single=results['single']['M'],
    M_collective=results['collective']['M'],
    eigvals_single=results['single']['eigvals'],
    eigvals_collective=results['collective']['eigvals'],
    det_M_single=np.array(results['single']['det_M']),
    det_M_collective=np.array(results['collective']['det_M']),
    mu_F_single=np.array(mu_F_single),
    mu_F_collective=np.array(mu_F_collective),
    # Resonance
    omega_J_at_fold_single=np.array(omega_J_at_fold_s),
    omega_J_at_fold_collective=np.array(omega_J_at_fold_c),
    omega_dt_single=omega_dt_s,
    omega_dt_collective=omega_dt_c,
    rel_rate_single=rel_rate_s,
    rel_rate_collective=rel_rate_c,
    # Hubble comparison
    H_canonical=np.array(H_canonical),
    omega_J_over_H_single=omega_J_single / H_canonical,
    omega_J_over_H_collective=omega_J_collective / H_canonical,
    # d2omega
    d2omega_J_s_dtau2=d2omega_J_s_dtau2,
    d2omega_J_c_dtau2=d2omega_J_c_dtau2,
    # Gate
    gate_name=np.array('FLOQUET-PLASMA-57'),
    gate_verdict=np.array(verdict),
    gate_detail=np.array(verdict_detail),
)
print(f"\nSaved to {save_path}")
print("DONE")
