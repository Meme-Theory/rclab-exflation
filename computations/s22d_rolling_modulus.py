"""
E-1: ROLLING MODULUS ODE — THREE DYNAMICAL SCENARIOS
=====================================================

Session 22d — Einstein-Theorist

Solves the modulus equation of motion in an FRW background for three
physically distinct scenarios:

    Scenario A: Freund-Rubin trapping (V = V_FR, tau_i = 0.05, tau_dot_i = 0)
    Scenario B: Freund-Rubin overshoot (V = V_FR, tau_i = 0.05, tau_dot_i = 0.02)
    Scenario C: Pure CW roll (V = V_CW monotonic, tau_i = 0.05, tau_dot_i = 0)

EQUATIONS (natural units, M_Pl = 1):

    tau'' + 3*H*tau' + (1/G_tt)*V'(tau) = 0

    H^2 = (1/3)*(rho_m + rho_r + rho_tau)

    rho_tau = (G_tt/2)*tau'^2 + V(tau)
    p_tau   = (G_tt/2)*tau'^2 - V(tau)

    w(t) = p_tau / rho_tau

where G_tt = 5 (Baptista Paper 15, eq 3.79, sigma-model metric from KK
reduction of SU(3), confirmed Session 21b).

INTEGRATION VARIABLE: We use N = ln(a) (e-folds from today) as the
integration variable, which converts the ODE to:

    d(tau)/dN = tau' / H

    d(tau')/dN = -3*tau' - (1/G_tt)*V'(tau)/H

where tau' = dtau/dt and primes on V denote d/dtau. The Friedmann equation
closes the system.

ALTERNATIVELY, we integrate backward from today using redshift z as the
independent variable. Since dz/dt = -(1+z)*H, we can write:

    dtau/dz = tau_dot / [-(1+z)*H]
    dtau_dot/dz = [-3*H*tau_dot - V'(tau)/G_tt] / [-(1+z)*H]

We use scale factor a = 1/(1+z) as the independent variable.

POTENTIAL NORMALIZATION:

For Scenarios A and B, the Freund-Rubin potential is:
    V_FR(tau) = V_tree(tau) + beta_flux * |omega_3|^2(tau)
where beta_flux is chosen so V_FR has a minimum at tau_0 = 0.30.
The overall amplitude is set so V_FR(tau_0) = 3*H_0^2*Omega_Lambda
(in M_Pl=1, H_0=1 units), i.e. V provides the observed dark energy.

For Scenario C, V_CW is normalized so V_CW(tau_i) provides the same
Omega_Lambda fraction. The SHAPE is from the Session 20b monotonic
Coleman-Weinberg potential, interpolated from the 21-point data.

COSMOLOGICAL PARAMETERS:
    Omega_m0 = 0.315
    Omega_r0 = 9.1e-5
    Omega_DE0 = 1 - Omega_m0 - Omega_r0 = 0.6849
    H_0 = 1 (natural units)

DATA SOURCES:
    - tier0-computation/s22a_slow_roll.npz: V_total, V_tree, V_cw, tau grid
    - tier0-computation/s22c_instanton_action.npz: R_K(tau) dense grid
    - Analytical: V_tree, |omega_3|^2 formulas from Baptista

PRE-REGISTERED Constraint GateS (DESI DR2):
    DECISIVE:    w_0 in [-0.9,-0.75] AND w_a in [-0.8,-0.2]     BF=20-30
    COMPELLING:  w_0 in [-0.95,-0.65] AND w_a in [-1.2,-0.1]    BF=5-10
    MARGINAL:    w_0 = -1 exactly (vacuum energy)                BF=0.5
    CLOSED:        |w_0+1| > 0.3 AND direction wrong               BF=0.1

Author: Einstein-Theorist (Session 22d)
Date: 2026-02-20
"""

import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import CubicSpline
from scipy.optimize import minimize_scalar
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

print("=" * 78)
print("  E-1: ROLLING MODULUS ODE -- THREE DYNAMICAL SCENARIOS")
print("  Einstein-Theorist -- Session 22d")
print("=" * 78)

# ===========================================================================
# 0. CONSTANTS AND COSMOLOGICAL PARAMETERS
# ===========================================================================

G_tt = 5.0            # Sigma-model metric (Baptista Paper 15, eq 3.79)
Omega_m0 = 0.315      # Matter density fraction today
Omega_r0 = 9.1e-5     # Radiation density fraction today
Omega_DE0 = 1.0 - Omega_m0 - Omega_r0  # ~ 0.6849
H_0 = 1.0             # Hubble rate today (natural units, M_Pl = 1)

# In these units: rho_crit = 3*H_0^2 = 3.0
rho_crit = 3.0 * H_0**2

# Time conversion: 1/H_0 in years
# H_0 = 67.4 km/s/Mpc => 1/H_0 ~ 14.5 Gyr ~ 1.45e10 yr
H0_inv_yr = 1.45e10  # years per 1/H_0

print(f"\n  COSMOLOGICAL PARAMETERS:")
print(f"    Omega_m0 = {Omega_m0}")
print(f"    Omega_r0 = {Omega_r0}")
print(f"    Omega_DE = {Omega_DE0:.6f}")
print(f"    G_tt = {G_tt}")
print(f"    H_0 = {H_0} (natural units)")
print(f"    rho_crit = 3*H_0^2 = {rho_crit}")

# ===========================================================================
# 1. POTENTIAL DEFINITIONS
# ===========================================================================

print("\n  PART 1: POTENTIAL DEFINITIONS")

# --- Analytical V_tree and omega_3 ---

def V_tree(tau):
    """Baptista tree-level potential at sigma=0."""
    return 1.0 - (1.0/10.0)*(2*np.exp(2*tau) - 1 + 8*np.exp(-tau) - np.exp(-4*tau))

def dV_tree_dtau(tau):
    """Derivative of V_tree."""
    return -(1.0/10.0)*(4*np.exp(2*tau) - 8*np.exp(-tau) + 4*np.exp(-4*tau))

def omega3_sq(tau):
    """|omega_3|^2 on (SU(3), g_Jensen)."""
    return 0.5*np.exp(-4*tau) + 0.5 + (1.0/3.0)*np.exp(6*tau)

def d_omega3_sq(tau):
    """Derivative of |omega_3|^2."""
    return -2*np.exp(-4*tau) + 2*np.exp(6*tau)

# --- Freund-Rubin: V_FR = V_tree + beta_flux * |omega_3|^2 ---
# Choose beta_flux so dV_FR/dtau = 0 at tau_0 = 0.30

tau_0_FR = 0.30
beta_flux = -dV_tree_dtau(tau_0_FR) / d_omega3_sq(tau_0_FR)

print(f"\n  FREUND-RUBIN POTENTIAL:")
print(f"    beta_flux = {beta_flux:.10f}")
print(f"    (chosen for V_FR minimum at tau_0 = {tau_0_FR})")

# Verify second derivative (must be positive for true minimum)
d2V_tree = -(1.0/10.0)*(8*np.exp(2*tau_0_FR) + 8*np.exp(-tau_0_FR) - 16*np.exp(-4*tau_0_FR))
d2_omega = 8*np.exp(-4*tau_0_FR) + 12*np.exp(6*tau_0_FR)
d2V_FR_at_min = d2V_tree + beta_flux * d2_omega
print(f"    d2V_FR/dtau2 at tau_0: {d2V_FR_at_min:.6f} ({'MINIMUM' if d2V_FR_at_min > 0 else 'MAXIMUM/SADDLE'})")

# Oscillation frequency around the minimum
omega_osc = np.sqrt(abs(d2V_FR_at_min) / G_tt)
print(f"    Oscillation frequency: omega = {omega_osc:.6f} (in H_0 units)")

def V_FR_raw(tau):
    """Unnormalized FR potential."""
    return V_tree(tau) + beta_flux * omega3_sq(tau)

def dV_FR_raw(tau):
    """Derivative of unnormalized FR potential."""
    return dV_tree_dtau(tau) + beta_flux * d_omega3_sq(tau)

# Normalize: V_FR(tau_0) = rho_crit * Omega_DE = 3 * 0.685 = 2.055
V_FR_raw_at_tau0 = V_FR_raw(tau_0_FR)
V_FR_scale = rho_crit * Omega_DE0 / V_FR_raw_at_tau0

print(f"    V_FR_raw(tau_0) = {V_FR_raw_at_tau0:.8f}")
print(f"    V_FR_scale = {V_FR_scale:.6f}")
print(f"    V_FR_normalized(tau_0) = {V_FR_scale * V_FR_raw_at_tau0:.6f} = rho_DE")

def V_FR(tau):
    """Normalized FR potential: V_FR(tau_0) = rho_DE."""
    return V_FR_scale * V_FR_raw(tau)

def dV_FR(tau):
    """Derivative of normalized FR potential."""
    return V_FR_scale * dV_FR_raw(tau)

# Print potential shape
print(f"\n    V_FR(tau) normalized:")
for t in [0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.50, 1.0]:
    print(f"      tau={t:.2f}: V_FR = {V_FR(t):.8f}")

# Barrier analysis
V_FR_at_0 = V_FR(0.0)
V_FR_at_min = V_FR(tau_0_FR)
# Find the barrier (local maximum between tau=0 and tau_0)
res_max = minimize_scalar(lambda t: -V_FR(t), bounds=(0.01, tau_0_FR-0.01), method='bounded')
tau_barrier = res_max.x
V_FR_barrier = V_FR(tau_barrier)
barrier_height = V_FR_barrier - V_FR_at_0
barrier_depth = V_FR_barrier - V_FR_at_min

print(f"\n    DOUBLE-WELL STRUCTURE:")
print(f"      V_FR(0) = {V_FR_at_0:.8f} (UV fixed point)")
print(f"      V_FR barrier at tau = {tau_barrier:.4f}: {V_FR_barrier:.8f}")
print(f"      V_FR(tau_0 = 0.30) = {V_FR_at_min:.8f} (IR minimum)")
print(f"      Barrier above tau=0: {barrier_height:.8f} ({barrier_height/V_FR_at_0*100:.4f}%)")
print(f"      Barrier above tau_0: {barrier_depth:.8f} ({barrier_depth/V_FR_at_min*100:.4f}%)")

# --- CW Potential (Scenario C) ---
# Load from data and interpolate
cw_data = np.load(os.path.join(SCRIPT_DIR, 's22a_slow_roll.npz'), allow_pickle=True)
tau_cw_grid = cw_data['tau']         # 21 points: 0 to 2
V_cw_grid = cw_data['V_total']       # V_tree + V_CW + E_Casimir
dV_cw_grid = cw_data['V_prime']      # dV/dtau

# CW interpolation
V_cw_spline = CubicSpline(tau_cw_grid, V_cw_grid)
dV_cw_spline = V_cw_spline.derivative()

# Normalize CW: set V_CW(tau_i=0.05) to provide Omega_DE at present
tau_i = 0.05
V_CW_scale = rho_crit * Omega_DE0 / V_cw_spline(tau_i)

def V_CW(tau):
    """Normalized CW potential."""
    return V_CW_scale * float(V_cw_spline(tau))

def dV_CW(tau):
    """Derivative of normalized CW potential."""
    return V_CW_scale * float(dV_cw_spline(tau))

print(f"\n  COLEMAN-WEINBERG POTENTIAL (Scenario C):")
print(f"    V_CW_raw(tau_i={tau_i}) = {float(V_cw_spline(tau_i)):.6e}")
print(f"    V_CW_scale = {V_CW_scale:.6e}")
print(f"    V_CW_normalized(tau_i) = {V_CW(tau_i):.6f}")

# ===========================================================================
# 2. FRIEDMANN + MODULUS ODE SYSTEM
# ===========================================================================

print("\n  PART 2: ODE SYSTEM DEFINITION")
print()
print("  Integration variable: a (scale factor), a=1 today, a=0 at Big Bang")
print("  State vector: y = [tau, pi_tau]")
print("  where pi_tau = G_tt * dtau/dt = G_tt * a*H * dtau/da")
print()

# The system in terms of a:
#
#   dtau/da = pi / (G_tt * a * H)
#   dpi/da  = -3*pi/a - (1/H) * dV/dtau / a
#
# where pi = G_tt * dtau/dt (conjugate momentum),
# H^2 = (1/3)*(Omega_m0/a^3 + Omega_r0/a^4 + (pi^2/(2*G_tt) + V(tau))) * rho_crit/rho_crit
#
# In our units (H_0 = 1, rho_crit = 3):
# H^2 = H_0^2 * (Omega_m0/a^3 + Omega_r0/a^4) + (1/3)*(pi^2/(2*G_tt) + V(tau))

def make_rhs(V_func, dV_func):
    """Create RHS for the ODE system given a potential."""

    def rhs(a, y):
        tau_val = y[0]
        pi_val = y[1]  # pi = G_tt * dtau/dt

        if a < 1e-10:
            return [0.0, 0.0]

        # Energy densities (in units of 3*H_0^2)
        rho_m = Omega_m0 / a**3
        rho_r = Omega_r0 / a**4

        # Modulus energy density
        K_tau = pi_val**2 / (2 * G_tt)  # kinetic
        V_tau = V_func(tau_val)          # potential

        rho_tau_over_3H02 = (K_tau + V_tau) / rho_crit

        # Friedmann: H^2 = H_0^2 * (Omega_m/a^3 + Omega_r/a^4 + Omega_tau)
        H_sq = H_0**2 * (rho_m + rho_r + rho_tau_over_3H02)

        if H_sq <= 0:
            return [0.0, 0.0]

        H = np.sqrt(H_sq)

        # dtau/da = pi / (G_tt * a * H)
        dtau_da = pi_val / (G_tt * a * H)

        # dpi/da = d(G_tt * tau_dot)/da
        # From EOM: G_tt * tau_ddot + 3*H*G_tt*tau_dot + dV/dtau = 0
        # => d(pi)/dt = -3*H*pi - dV/dtau
        # => d(pi)/da = d(pi)/dt * dt/da = (-3*H*pi - dV/dtau) / (a*H)
        dpi_da = (-3 * H * pi_val - dV_func(tau_val)) / (a * H)

        return [dtau_da, dpi_da]

    return rhs

# ===========================================================================
# 3. INITIAL CONDITIONS AND INTEGRATION
# ===========================================================================

print("  PART 3: INTEGRATION")
print()

# Integration range: from a_start (early universe) to a=1 (today)
# Start at a = a_start corresponding to z_start
# We integrate FORWARD from a_start to a=1.

# For cosmological evolution: start at z ~ 10 (a ~ 0.09) to capture
# the matter-dominated era transition to dark energy domination.
# But to capture the full dynamics, start earlier: z ~ 1000 (a ~ 0.001)
# in the matter-radiation era.

z_start = 1000.0
a_start = 1.0 / (1.0 + z_start)
a_end = 1.0

# Dense output for plotting — ensure endpoints are strictly inside t_span
a_eval = np.logspace(np.log10(a_start * 1.001), np.log10(a_end * 0.999), 2000)

# Initial conditions at a_start:
# tau_i and tau_dot_i specified in the prompt
# pi_i = G_tt * tau_dot_i

# Convert tau_dot_i from "per Hubble time" to natural units:
# tau_dot_i = 0.02 means dtau/dt = 0.02 * H_0
# So pi_i = G_tt * tau_dot_i_physical = G_tt * 0.02 * H_0 = 5 * 0.02 * 1 = 0.1

scenarios = {
    'A': {
        'name': 'FR trapping (tau_i=0.05, tau_dot=0)',
        'V': V_FR, 'dV': dV_FR,
        'tau_i': 0.05, 'pi_i': 0.0,
    },
    'B': {
        'name': 'FR overshoot (tau_i=0.05, tau_dot=0.02)',
        'V': V_FR, 'dV': dV_FR,
        'tau_i': 0.05, 'pi_i': G_tt * 0.02,  # pi = G_tt * tau_dot
    },
    'C': {
        'name': 'Pure CW roll (tau_i=0.05, tau_dot=0)',
        'V': V_CW, 'dV': dV_CW,
        'tau_i': 0.05, 'pi_i': 0.0,
    },
    'D': {
        'name': 'FR frozen at minimum (tau_i=0.30, tau_dot=0)',
        'V': V_FR, 'dV': dV_FR,
        'tau_i': 0.30, 'pi_i': 0.0,
    },
    'E': {
        'name': 'FR near-minimum (tau_i=0.29, tau_dot=0)',
        'V': V_FR, 'dV': dV_FR,
        'tau_i': 0.29, 'pi_i': 0.0,
    },
    'F': {
        'name': 'FR settling (tau_i=0.25, tau_dot=0.001)',
        'V': V_FR, 'dV': dV_FR,
        'tau_i': 0.25, 'pi_i': G_tt * 0.001,  # small residual velocity from FP cavity
    },
}

results = {}

for label, sc in scenarios.items():
    print(f"\n  --- SCENARIO {label}: {sc['name']} ---")

    rhs = make_rhs(sc['V'], sc['dV'])
    y0 = [sc['tau_i'], sc['pi_i']]

    print(f"    tau_i = {sc['tau_i']}")
    print(f"    pi_i = {sc['pi_i']} (= G_tt * tau_dot_i = {sc['pi_i']/G_tt})")
    print(f"    V(tau_i) = {sc['V'](sc['tau_i']):.8f}")
    print(f"    Integration: a = [{a_start:.6f}, {a_end}] (z = [{z_start}, 0])")

    # Solve
    sol = solve_ivp(
        rhs,
        t_span=[a_start, a_end],
        y0=y0,
        method='RK45',
        t_eval=a_eval,
        rtol=1e-10,
        atol=1e-12,
        max_step=0.01,
    )

    if not sol.success:
        print(f"    *** INTEGRATION FAILED: {sol.message}")
        # Try with less stringent tolerances
        sol = solve_ivp(
            rhs,
            t_span=[a_start, a_end],
            y0=y0,
            method='RK45',
            t_eval=a_eval,
            rtol=1e-8,
            atol=1e-10,
            max_step=0.001,
        )
        if not sol.success:
            print(f"    *** RETRY ALSO FAILED: {sol.message}")
            results[label] = None
            continue

    a_sol = sol.t
    tau_sol = sol.y[0]
    pi_sol = sol.y[1]
    z_sol = 1.0 / a_sol - 1.0

    # Derived quantities
    tau_dot_sol = pi_sol / G_tt  # dtau/dt in H_0 units

    # Hubble parameter
    K_sol = pi_sol**2 / (2 * G_tt)
    V_sol = np.array([sc['V'](t) for t in tau_sol])
    rho_tau_sol = K_sol + V_sol
    p_tau_sol = K_sol - V_sol

    rho_m_sol = rho_crit * Omega_m0 / a_sol**3
    rho_r_sol = rho_crit * Omega_r0 / a_sol**4

    H_sq_sol = (rho_m_sol + rho_r_sol + rho_tau_sol) / rho_crit
    H_sol = np.sqrt(np.maximum(H_sq_sol, 1e-30))

    # Equation of state
    w_sol = np.where(rho_tau_sol > 1e-30, p_tau_sol / rho_tau_sol, -1.0)

    # Omega_tau
    Omega_tau_sol = rho_tau_sol / (rho_crit * H_sq_sol)

    # w_0 and w_a (CPL parametrization: w(a) = w_0 + w_a*(1-a))
    # w_0 = w(a=1) = w(today)
    w_0 = w_sol[-1]

    # w_a = -dw/da at a=1
    # Use finite difference from the last few points
    if len(a_sol) >= 5:
        da = a_sol[-1] - a_sol[-5]
        dw = w_sol[-1] - w_sol[-5]
        w_a = -dw / da
    else:
        w_a = 0.0

    # More robust: fit w(a) = w_0 + w_a*(1-a) to the low-z portion (z < 2, a > 0.33)
    low_z_mask = a_sol > 0.33
    if np.sum(low_z_mask) > 10:
        a_fit = a_sol[low_z_mask]
        w_fit = w_sol[low_z_mask]
        # Linear fit: w = w_0 + w_a*(1-a), so w = (w_0 + w_a) - w_a*a
        # fit w vs a: w = c0 + c1*a => w_0 = c0 + c1, w_a = -c1
        coeffs = np.polyfit(a_fit, w_fit, 1)
        w_a_fit = -coeffs[0]
        w_0_fit = coeffs[0] + coeffs[1]  # = w_0 + w_a evaluated at a=1
        # But actually: w(a=1) = coeffs[0]*1 + coeffs[1] = coeffs[0] + coeffs[1]
        w_0_fit = coeffs[0] + coeffs[1]
    else:
        w_0_fit = w_0
        w_a_fit = w_a

    print(f"\n    RESULTS:")
    print(f"      tau(today) = {tau_sol[-1]:.8f}")
    print(f"      tau_dot(today) = {tau_dot_sol[-1]:.8e}")
    print(f"      V(tau_today) = {V_sol[-1]:.8f}")
    print(f"      K(today) = {K_sol[-1]:.8e}")
    print(f"      Omega_tau(today) = {Omega_tau_sol[-1]:.6f}")
    print(f"      w_0 = w(today) = {w_0:.8f}")
    print(f"      w_a (finite diff) = {w_a:.8f}")
    print(f"      w_0 (CPL fit) = {w_0_fit:.8f}")
    print(f"      w_a (CPL fit) = {w_a_fit:.8f}")

    # Trajectory at key redshifts
    print(f"\n      Trajectory at key redshifts:")
    key_z = [1000, 100, 10, 3, 1, 0.5, 0.1, 0]
    for zk in key_z:
        ak = 1.0 / (1.0 + zk)
        idx = np.argmin(np.abs(a_sol - ak))
        print(f"        z={zk:>5}: a={a_sol[idx]:.6f}, tau={tau_sol[idx]:.6f}, "
              f"w={w_sol[idx]:.6f}, Omega_tau={Omega_tau_sol[idx]:.6e}")

    # Store
    results[label] = {
        'a': a_sol,
        'z': z_sol,
        'tau': tau_sol,
        'tau_dot': tau_dot_sol,
        'pi': pi_sol,
        'H': H_sol,
        'w': w_sol,
        'Omega_tau': Omega_tau_sol,
        'V': V_sol,
        'K': K_sol,
        'w_0': w_0,
        'w_a': w_a,
        'w_0_fit': w_0_fit,
        'w_a_fit': w_a_fit,
    }

# ===========================================================================
# 4. DESI COMPARISON
# ===========================================================================

print("\n" + "=" * 78)
print("  PART 4: DESI DR2 COMPARISON")
print("=" * 78)
print()

# DESI DR2: w_0 ~ -0.83 +/- 0.09, w_a ~ -0.45 +/- 0.31
w0_DESI = -0.83
w0_DESI_err = 0.09
wa_DESI = -0.45
wa_DESI_err = 0.31

print(f"  DESI DR2 (2026-02):")
print(f"    w_0 = {w0_DESI} +/- {w0_DESI_err}")
print(f"    w_a = {wa_DESI} +/- {wa_DESI_err}")
print()

for label in ['A', 'B', 'C', 'D', 'E', 'F']:
    r = results.get(label)
    if r is None:
        print(f"  Scenario {label}: FAILED (no result)")
        continue

    # Use CPL fit values for DESI comparison
    w0 = r['w_0_fit']
    wa = r['w_a_fit']

    # Distance from DESI central value
    d_w0 = (w0 - w0_DESI) / w0_DESI_err
    d_wa = (wa - wa_DESI) / wa_DESI_err
    chi_sq = d_w0**2 + d_wa**2

    print(f"  Scenario {label}:")
    print(f"    w_0 = {w0:.6f} (DESI deviation: {d_w0:.2f} sigma)")
    print(f"    w_a = {wa:.6f} (DESI deviation: {d_wa:.2f} sigma)")
    print(f"    Combined chi^2 = {chi_sq:.2f}")

    # Classification
    decisive = (-0.9 <= w0 <= -0.75) and (-0.8 <= wa <= -0.2)
    compelling = (-0.95 <= w0 <= -0.65) and (-1.2 <= wa <= -0.1)
    marginal_kill = abs(w0 + 1) < 0.01
    closure = abs(w0 + 1) > 0.3

    if decisive:
        verdict = "DECISIVE"
        bf = "20-30"
        shift = "+15-20 pp"
    elif compelling:
        verdict = "COMPELLING"
        bf = "5-10"
        shift = "+8-12 pp"
    elif marginal_kill:
        verdict = "MARGINAL CLOSURE"
        bf = "0.5"
        shift = "-3-5 pp"
    elif closure:
        if w0 > -0.7:  # wrong direction
            verdict = "CLOSED (w_0 too high)"
            bf = "0.1"
            shift = "-8-12 pp"
        else:
            verdict = "CLOSED (w_0 too low)"
            bf = "0.1"
            shift = "-8-12 pp"
    else:
        verdict = "MARGINAL"
        bf = "1-3"
        shift = "+0-5 pp"

    print(f"    *** VERDICT: {verdict} (BF = {bf}, shift = {shift}) ***")
    print()

# ===========================================================================
# 5. E-2: EARLY DARK ENERGY BOUND
# ===========================================================================

print("=" * 78)
print("  E-2: EARLY DARK ENERGY BOUND (Omega_tau at z=10)")
print("=" * 78)
print()

for label in ['A', 'B', 'C', 'D', 'E', 'F']:
    r = results.get(label)
    if r is None:
        continue

    # Find Omega_tau at z=10
    a_z10 = 1.0 / 11.0
    idx_z10 = np.argmin(np.abs(r['a'] - a_z10))
    Omega_tau_z10 = r['Omega_tau'][idx_z10]

    print(f"  Scenario {label}: Omega_tau(z=10) = {Omega_tau_z10:.6e}")

    if Omega_tau_z10 < 0.02:
        ede_verdict = "PASS (BF = 2)"
    elif Omega_tau_z10 < 0.10:
        ede_verdict = "MARGINAL (BF = 0.8)"
    else:
        ede_verdict = "CMB CLOSED (BF = 0.1)"

    print(f"    *** {ede_verdict} ***")
    print()

# ===========================================================================
# 6. E-3: ATOMIC CLOCK CONSTRAINT
# ===========================================================================

print("=" * 78)
print("  E-3: ATOMIC CLOCK AND WEP CONSTRAINT")
print("=" * 78)
print()

# alpha_FS_dot / alpha_FS = -4*cos^2(theta_W) * tau_dot
# where cos^2(theta_W) = 1 - sin^2(theta_W) = 1 - 0.231 = 0.769
cos2_thetaW = 0.769
coupling_factor = -4.0 * cos2_thetaW  # = -3.076

print(f"  alpha_FS_dot / alpha_FS = {coupling_factor:.3f} * tau_dot")
print(f"  Bound: |alpha_dot/alpha| < 1e-16 yr^{-1}")
print(f"  => |tau_dot| < {1e-16 / abs(coupling_factor):.4e} yr^{-1}")
print(f"  => |tau_dot| < {1e-16 / abs(coupling_factor) * H0_inv_yr:.4e} (in H_0 units)")
print()

tau_dot_bound_H0 = 1e-16 / abs(coupling_factor) * H0_inv_yr  # in H_0 units

# Also: |alpha_dot/alpha| < 1e-17 yr^{-1} is the PASS threshold
tau_dot_pass_H0 = 1e-17 / abs(coupling_factor) * H0_inv_yr

for label in ['A', 'B', 'C', 'D', 'E', 'F']:
    r = results.get(label)
    if r is None:
        continue

    tau_dot_today = r['tau_dot'][-1]  # in H_0 units
    alpha_dot_over_alpha = coupling_factor * tau_dot_today / H0_inv_yr  # in yr^{-1}

    print(f"  Scenario {label}:")
    print(f"    tau_dot(today) = {tau_dot_today:.8e} (H_0 units)")
    print(f"    alpha_dot/alpha = {alpha_dot_over_alpha:.4e} yr^{-1}")
    print(f"    |alpha_dot/alpha| = {abs(alpha_dot_over_alpha):.4e} yr^{-1}")

    if abs(alpha_dot_over_alpha) < 1e-17:
        clock_verdict = "PASS (BF = 3)"
    elif abs(alpha_dot_over_alpha) < 1e-16:
        clock_verdict = "MARGINAL (BF = 0.9)"
    else:
        clock_verdict = "CLOCK CLOSED (BF = 0.1)"

    print(f"    *** {clock_verdict} ***")
    print()

# ===========================================================================
# 7. SAVE DATA
# ===========================================================================

print("=" * 78)
print("  SAVING OUTPUT")
print("=" * 78)

save_dict = {}
for label in ['A', 'B', 'C', 'D', 'E', 'F']:
    r = results.get(label)
    if r is None:
        # Store NaN arrays for failed scenarios
        save_dict[f'tau_{label}'] = np.array([np.nan])
        save_dict[f'H_{label}'] = np.array([np.nan])
        save_dict[f'w_{label}'] = np.array([np.nan])
        save_dict[f'w0_{label}'] = np.nan
        save_dict[f'wa_{label}'] = np.nan
        continue

    save_dict[f'a_{label}'] = r['a']
    save_dict[f'z_{label}'] = r['z']
    save_dict[f'tau_{label}'] = r['tau']
    save_dict[f'H_{label}'] = r['H']
    save_dict[f'w_{label}'] = r['w']
    save_dict[f'Omega_tau_{label}'] = r['Omega_tau']
    save_dict[f'V_{label}'] = r['V']
    save_dict[f'K_{label}'] = r['K']
    save_dict[f'tau_dot_{label}'] = r['tau_dot']
    save_dict[f'w0_{label}'] = r['w_0_fit']
    save_dict[f'wa_{label}'] = r['w_a_fit']
    save_dict[f'w0_raw_{label}'] = r['w_0']
    save_dict[f'wa_raw_{label}'] = r['w_a']

# Store metadata
save_dict['G_tt'] = np.array([G_tt])
save_dict['beta_flux'] = np.array([beta_flux])
save_dict['tau_0_FR'] = np.array([tau_0_FR])
save_dict['V_FR_scale'] = np.array([V_FR_scale])
save_dict['Omega_m0'] = np.array([Omega_m0])
save_dict['Omega_r0'] = np.array([Omega_r0])
save_dict['Omega_DE0'] = np.array([Omega_DE0])

out_file = os.path.join(SCRIPT_DIR, 's22d_rolling_trajectories.npz')
np.savez(out_file, **save_dict)
print(f"\n  Saved: {out_file}")
print(f"  Keys: {sorted(save_dict.keys())}")

# ===========================================================================
# 8. PLOT
# ===========================================================================

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 3, figsize=(18, 12))
fig.suptitle('E-1: Rolling Modulus ODE -- Three Scenarios\n'
             'Einstein-Theorist, Session 22d',
             fontsize=14, fontweight='bold')

colors = {'A': 'blue', 'B': 'red', 'C': 'green', 'D': 'purple', 'E': 'orange', 'F': 'brown'}
styles = {'A': '-', 'B': '--', 'C': ':', 'D': '-.', 'E': '-', 'F': '--'}

# Panel 1: tau(z)
ax = axes[0, 0]
for label in ['A', 'B', 'C', 'D', 'E', 'F']:
    r = results.get(label)
    if r is None:
        continue
    mask = r['z'] < 20
    ax.plot(r['z'][mask], r['tau'][mask],
            color=colors[label], ls=styles[label], lw=2,
            label=f'Scenario {label}')
ax.axhline(tau_0_FR, color='purple', ls=':', alpha=0.5, label=f'FR min tau={tau_0_FR}')
ax.set_xlabel('Redshift z')
ax.set_ylabel(r'$\tau(z)$')
ax.set_title(r'Modulus trajectory $\tau(z)$')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)
ax.invert_xaxis()

# Panel 2: w(z)
ax = axes[0, 1]
for label in ['A', 'B', 'C', 'D', 'E', 'F']:
    r = results.get(label)
    if r is None:
        continue
    mask = r['z'] < 5
    ax.plot(r['z'][mask], r['w'][mask],
            color=colors[label], ls=styles[label], lw=2,
            label=f'Scenario {label}')
ax.axhline(-1, color='gray', ls='-', alpha=0.3, label='w = -1 (Lambda)')
ax.axhline(w0_DESI, color='orange', ls='--', alpha=0.7, label=f'DESI w_0={w0_DESI}')
ax.fill_between([0, 5], w0_DESI - w0_DESI_err, w0_DESI + w0_DESI_err,
                alpha=0.15, color='orange')
ax.set_xlabel('Redshift z')
ax.set_ylabel('w(z)')
ax.set_title('Equation of state w(z)')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)
ax.set_ylim(-1.5, 0)
ax.invert_xaxis()

# Panel 3: Omega_tau(z)
ax = axes[0, 2]
for label in ['A', 'B', 'C', 'D', 'E', 'F']:
    r = results.get(label)
    if r is None:
        continue
    mask = r['z'] < 100
    ax.semilogy(r['z'][mask], r['Omega_tau'][mask],
                color=colors[label], ls=styles[label], lw=2,
                label=f'Scenario {label}')
ax.axhline(0.1, color='red', ls='--', alpha=0.5, label='EDE bound (0.10)')
ax.axhline(0.02, color='orange', ls=':', alpha=0.5, label='EDE safe (0.02)')
ax.axhline(Omega_DE0, color='purple', ls=':', alpha=0.5, label=f'Omega_DE today')
ax.set_xlabel('Redshift z')
ax.set_ylabel(r'$\Omega_\tau(z)$')
ax.set_title(r'Dark energy fraction $\Omega_\tau(z)$')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)
ax.invert_xaxis()

# Panel 4: V_FR potential shape
ax = axes[1, 0]
tau_plot = np.linspace(0, 0.8, 200)
V_FR_plot = np.array([V_FR(t) for t in tau_plot])
V_CW_plot = np.array([V_CW(min(max(t, 0), 2.0)) for t in tau_plot])
ax.plot(tau_plot, V_FR_plot, 'b-', lw=2, label=r'$V_{FR}$')
ax.plot(tau_plot, V_CW_plot, 'g--', lw=2, label=r'$V_{CW}$ (normalized)')
ax.axvline(tau_0_FR, color='purple', ls=':', alpha=0.5, label=f'FR min')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$V(\tau)$')
ax.set_title('Potential shapes')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 5: w_0 vs w_a (DESI plane)
ax = axes[1, 1]
for label in ['A', 'B', 'C', 'D', 'E', 'F']:
    r = results.get(label)
    if r is None:
        continue
    ax.plot(r['w_0_fit'], r['w_a_fit'],
            'o', color=colors[label], ms=10, label=f'Scenario {label}')

# DESI contours (approximate 1-sigma and 2-sigma)
from matplotlib.patches import Ellipse
for nsig, alpha in [(1, 0.3), (2, 0.15)]:
    ell = Ellipse((w0_DESI, wa_DESI),
                  2*nsig*w0_DESI_err, 2*nsig*wa_DESI_err,
                  color='orange', alpha=alpha,
                  label=f'DESI {nsig}$\\sigma$' if nsig == 1 else None)
    ax.add_patch(ell)

# Classification regions
ax.axvspan(-0.9, -0.75, alpha=0.08, color='green', label='DECISIVE w_0')
ax.axhspan(-0.8, -0.2, alpha=0.08, color='green')
ax.plot(-1, 0, 'kx', ms=15, mew=3, label='Lambda CDM')
ax.set_xlabel('$w_0$')
ax.set_ylabel('$w_a$')
ax.set_title('$w_0$-$w_a$ DESI plane')
ax.set_xlim(-1.5, -0.3)
ax.set_ylim(-2, 1)
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)

# Panel 6: Phase portrait (tau, tau_dot)
ax = axes[1, 2]
for label in ['A', 'B', 'C', 'D', 'E', 'F']:
    r = results.get(label)
    if r is None:
        continue
    mask = r['z'] < 50
    ax.plot(r['tau'][mask], r['tau_dot'][mask],
            color=colors[label], ls=styles[label], lw=2,
            label=f'Scenario {label}')
    # Mark today
    ax.plot(r['tau'][-1], r['tau_dot'][-1],
            '*', color=colors[label], ms=12)
ax.axhline(0, color='gray', ls='-', alpha=0.3)
ax.axvline(tau_0_FR, color='purple', ls=':', alpha=0.5, label=f'FR min')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$\dot{\tau}$ (H_0 units)')
ax.set_title(r'Phase portrait $(\tau, \dot{\tau})$')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plot_file = os.path.join(SCRIPT_DIR, 's22d_rolling_trajectories.png')
plt.savefig(plot_file, dpi=150, bbox_inches='tight')
print(f"\n  Plot saved: {plot_file}")
plt.close()

# ===========================================================================
# 9. SUMMARY
# ===========================================================================

print("\n" + "=" * 78)
print("  E-1/E-2/E-3 SUMMARY")
print("=" * 78)
print()

print("  SCENARIO RESULTS:")
print(f"  {'Scenario':>10} {'w_0':>10} {'w_a':>10} {'Omega_tau(z=10)':>16} {'|dalpha/alpha|':>16} {'DESI':>12} {'EDE':>10} {'Clock':>10}")
print(f"  {'--------':>10} {'---':>10} {'---':>10} {'---------------':>16} {'--------------':>16} {'----':>12} {'---':>10} {'-----':>10}")

for label in ['A', 'B', 'C', 'D', 'E', 'F']:
    r = results.get(label)
    if r is None:
        print(f"  {'Scenario '+label:>10} {'FAILED':>10}")
        continue

    a_z10 = 1.0 / 11.0
    idx_z10 = np.argmin(np.abs(r['a'] - a_z10))
    Omega_z10 = r['Omega_tau'][idx_z10]

    tau_dot_today = r['tau_dot'][-1]
    alpha_dot = coupling_factor * tau_dot_today / H0_inv_yr

    w0 = r['w_0_fit']
    wa = r['w_a_fit']

    # DESI classification
    if (-0.9 <= w0 <= -0.75) and (-0.8 <= wa <= -0.2):
        desi = "DECISIVE"
    elif (-0.95 <= w0 <= -0.65) and (-1.2 <= wa <= -0.1):
        desi = "COMPELLING"
    elif abs(w0 + 1) < 0.01:
        desi = "MARG CLOSED"
    elif abs(w0 + 1) > 0.3:
        desi = "CLOSED"
    else:
        desi = "MARGINAL"

    # EDE classification
    if Omega_z10 < 0.02:
        ede = "PASS"
    elif Omega_z10 < 0.10:
        ede = "MARGINAL"
    else:
        ede = "CLOSED"

    # Clock classification
    if abs(alpha_dot) < 1e-17:
        clock = "PASS"
    elif abs(alpha_dot) < 1e-16:
        clock = "MARGINAL"
    else:
        clock = "CLOSED"

    print(f"  {'Scen '+label:>10} {w0:10.6f} {wa:10.6f} {Omega_z10:16.6e} {abs(alpha_dot):16.4e} {desi:>12} {ede:>10} {clock:>10}")

print()
print("=" * 78)
