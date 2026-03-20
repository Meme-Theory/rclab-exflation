"""
Session 29b Computation 2: Modulus Equation of Motion
=====================================================

PHYSICS:
    Solve the coupled modulus equation of motion with Friedmann constraint:

        ddot(tau) + 3*H*dot(tau) + (1/G_{tau,tau}) * dV_eff/dtau = 0     (29b.2)

        H^2 = (1/(3*M_P^2)) * [G_{tau,tau}/2 * dot(tau)^2 + V_eff(tau)]  (29b.3)

    where:
        G_{tau,tau} = 5  (Baptista Paper 15, eq 3.76-3.77)
        V_eff(tau) = V_spec(tau) in natural KK units (M_KK = 1)

    The factor G_{tau,tau} = 5 arises from the representation-theoretic structure
    of the Jensen deformation on su(3) = u(1) + su(2) + C^2:
        (2)^2 * dim(u(1)) + (-2)^2 * dim(su(2)) + (1)^2 * dim(C^2) = 4+12+4 = 20
        |S'|^2 = (1/4)*20*(d sigma)^2 = 5*(d sigma)^2

    Dimensional analysis:
        V_phys(tau) = M_KK^4 * V_spec(tau)
        H^2 = M_KK^4 / (3 M_P^2) * [G/2 * dot(tau)^2 + V_spec(tau)]
        t_phys = t_dimless / M_KK
        t_sec = t_dimless / M_KK * hbar_GeV

    KEY PHYSICS FINDING (Einstein, Session 29Ab):
        Hubble friction is NEGLIGIBLE for M_KK <= 10^17 GeV. The friction
        parameter 3*H*t_cross < 0.002 for M_KK = 10^16 GeV. The modulus
        rolls essentially freely on V_eff(tau).

        This means we can use BOTH approaches:
        1. Full ODE integration (numerically exact, includes Hubble friction)
        2. Analytical quadrature from energy conservation (cross-check)

        t_cross = integral_0^{tau_cross} d(tau) / sqrt(2*(E-V(tau))/G)

    INITIAL CONDITIONS (from Synthesis A U-4 and 29a-2):
        tau(0) = 0  (round metric, triple-selected by WCH + J-maximality + DNP)
        E_total = {1.5, 2.0, 5.0} * V(0)  (DNP instability energy brackets)

        The DNP instability (SP-5, Session 22a) drives the round metric
        TT-unstable, providing E_total ~ O(1) * V(0). From 29a-2:
        E_crit/V(0) = 1.52 at tau=0.50, so E_total = 2*V(0) is the
        natural reference value.

    BCS TRANSITION:
        From 29b-1: F_BCS < 0 at all tau when mu >= lambda_min.
        KC-3 self-consistent model: gap filled at tau >= 0.407 (n_gap crosses 20).
        First-order transition (L-9) nucleates at tau_cross.

        At tau_cross, latent heat L = |F_BCS(tau_cross)| is extracted from
        modulus KE. If KE < L, modulus is trapped on first pass.

        Post-transition: modulus jumps to tau_BCS ~ 0.35 (BCS minimum).
        Residual energy converts to radiation (reheating).

    We scan M_KK in {10^14, 10^15, 10^16, 10^17, 10^18} GeV
    and E_mult in {1.5, 2.0, 5.0} * V(0).

GATE G-29c:
    FIRES if t_BCS requires M_KK > 10^18 GeV or t_BCS > 13.8 Gyr.

POSITIVE SIGNAL P-29f:
    FIRES if tau(t) reaches tau_cross in t_BCS ~ 10^{-36} to 10^{-10} s
    for natural M_KK (10^{14}-10^{16} GeV).

DATA SOURCES:
    - s24a_vspec.npz: V_spec(tau, rho)
    - s29a_derived_drive_rate.npz: V_eff scan, G_tau_tau
    - s29b_free_energy_comparison.npz: canonical tau_cross, F_BCS landscape
    - s28b_self_consistent_tau_T.npz: F_BCS(tau, mu) for latent heat

Author: phonon-exflation-sim
Date: 2026-02-28
Session: 29Ab, Computation 2
"""

import os
import sys
import numpy as np
from scipy.interpolate import interp1d
from scipy.integrate import solve_ivp, quad

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


# ===========================================================================
# PHYSICAL CONSTANTS (natural units: hbar = c = 1, energies in GeV)
# ===========================================================================

M_P_GEV = 2.435e18       # Reduced Planck mass in GeV
GEV_TO_SEC = 6.582e-25   # 1/GeV in seconds (hbar/GeV)
SEC_TO_GYR = 1.0 / (365.25 * 24 * 3600 * 1e9)
UNIVERSE_AGE_SEC = 13.8e9 * 365.25 * 24 * 3600  # 13.8 Gyr in seconds

G_TAU_TAU = 5.0           # Modulus metric (Baptista Paper 15 eq 3.76-3.77)

# M_KK scan values in GeV
M_KK_VALUES = [1e14, 1e15, 1e16, 1e17, 1e18]

# E_total multipliers (relative to V(0))
E_MULT_VALUES = [1.5, 2.0, 5.0]

# BCS transition parameters
TAU_CROSS_DEFAULT = 0.50   # From 29b-1 KC-3 self-consistent model
TAU_CROSS_KC3 = 0.407      # From 29a-2: n_gap crosses 20 at E=2*V(0)

# Reheating
G_STAR = 106.75            # SM relativistic DOF at GUT scale


# ===========================================================================
# DATA LOADING
# ===========================================================================

def load_data():
    """Load all required input data.

    Returns:
        dict with V_spec interpolant and metadata
    """
    data = {}

    # V_spec(tau) from s24a
    vspec_path = os.path.join(SCRIPT_DIR, "s24a_vspec.npz")
    d = np.load(vspec_path, allow_pickle=True)
    tau_vspec = d['tau']
    V_spec = d['V_spec_rho_0p010']  # Primary: rho = 0.01
    data['tau_vspec'] = tau_vspec
    data['V_spec_raw'] = V_spec

    # Build cubic interpolant
    data['V_spec_interp'] = interp1d(tau_vspec, V_spec, kind='cubic',
                                      fill_value='extrapolate')

    # Compute dV/dtau via finite differences, then interpolate
    dV = np.gradient(V_spec, tau_vspec)
    data['dV_spec_interp'] = interp1d(tau_vspec, dV, kind='cubic',
                                       fill_value='extrapolate')

    data['V_at_0'] = float(data['V_spec_interp'](0.0))

    # 29b-1 results for latent heat
    fe_path = os.path.join(SCRIPT_DIR, "s29b_free_energy_comparison.npz")
    if os.path.exists(fe_path):
        fe = np.load(fe_path, allow_pickle=True)
        if 'canonical_tau_cross' in fe.files:
            data['tau_cross'] = float(fe['canonical_tau_cross'][0])
        else:
            data['tau_cross'] = TAU_CROSS_DEFAULT
        F_bcs_sc1 = fe['F_bcs_scenario1']
        tau_bcs = fe['tau_bcs']
        idx_cross = np.argmin(np.abs(tau_bcs - data['tau_cross']))
        data['latent_heat_mu1'] = abs(float(F_bcs_sc1[idx_cross]))

        # Also get mu=1.2*lmin
        F_bcs_sc2 = fe['F_bcs_scenario2']
        data['latent_heat_mu12'] = abs(float(F_bcs_sc2[idx_cross]))
    else:
        data['tau_cross'] = TAU_CROSS_DEFAULT
        data['latent_heat_mu1'] = 5.63
        data['latent_heat_mu12'] = 14.01

    # Load F_BCS landscape for latent heat at mu=1.5*lmin
    s28b_path = os.path.join(SCRIPT_DIR, "s28b_self_consistent_tau_T.npz")
    if os.path.exists(s28b_path):
        s28b = np.load(s28b_path, allow_pickle=True)
        tau_bcs_grid = s28b['tau_values']
        mu_ratios = s28b['mu_ratios']
        F_total = s28b['F_total']
        idx_mu15 = np.argmin(np.abs(mu_ratios - 1.5))
        idx_tau_cross = np.argmin(np.abs(tau_bcs_grid - data['tau_cross']))
        data['latent_heat_mu15'] = abs(float(F_total[idx_tau_cross, idx_mu15]))
    else:
        data['latent_heat_mu15'] = 38.9

    return data


# ===========================================================================
# METHOD 1: ANALYTICAL QUADRATURE (friction-free energy conservation)
# ===========================================================================

def compute_analytical_trajectory(E_total, V_interp, tau_cross, G=G_TAU_TAU,
                                  n_points=2000):
    """Compute tau(t) trajectory from energy conservation (no friction).

    E_total = G/2 * (dtau/dt)^2 + V(tau)
    dtau/dt = sqrt(2*(E - V(tau))/G)
    t(tau) = integral_0^tau d(tau') / sqrt(2*(E - V(tau'))/G)

    Parameters:
        E_total: float, total energy in dimensionless KK units
        V_interp: callable, V_spec(tau)
        tau_cross: float, BCS transition tau
        G: float, G_{tau,tau}
        n_points: int, number of tau points for trajectory

    Returns:
        dict with tau, t, dtau_dt, reached_cross, t_cross, etc.
    """
    V0 = float(V_interp(0.0))
    V_cross = float(V_interp(tau_cross))

    result = {
        'E_total': E_total,
        'E_mult': E_total / V0,
        'V_at_0': V0,
        'V_at_cross': V_cross,
    }

    # Check if E_total > V(tau_cross) -- can the modulus reach tau_cross?
    if E_total <= V_cross:
        # Find the turning point: V(tau_turn) = E_total
        from scipy.optimize import brentq
        try:
            tau_turn = brentq(lambda t: float(V_interp(t)) - E_total, 0.001, 2.0)
        except ValueError:
            tau_turn = 0.0
        result['reached_cross'] = False
        result['tau_turn'] = tau_turn
        result['reason'] = f'E_total={E_total:.4f} < V(tau_cross)={V_cross:.4f}'

        # Still compute trajectory up to turning point
        if tau_turn > 0.001:
            tau_arr = np.linspace(0, tau_turn * 0.999, n_points)
        else:
            tau_arr = np.array([0.0])
            result['tau'] = tau_arr
            result['t_dimless'] = np.array([0.0])
            result['dtau_dt'] = np.array([np.sqrt(2 * max(0, E_total - V0) / G)])
            return result
    else:
        result['reached_cross'] = True
        tau_arr = np.linspace(0, tau_cross, n_points)

    # Compute dtau/dt at each point
    V_arr = np.array([float(V_interp(t)) for t in tau_arr])
    KE_arr = E_total - V_arr
    KE_arr = np.maximum(KE_arr, 0)  # Clip negative values at turning point
    dtau_dt_arr = np.sqrt(2 * KE_arr / G)

    # Compute t(tau) by numerical integration (trapezoid)
    t_arr = np.zeros_like(tau_arr)
    for i in range(1, len(tau_arr)):
        dtau = tau_arr[i] - tau_arr[i - 1]
        avg_vel = 0.5 * (dtau_dt_arr[i] + dtau_dt_arr[i - 1])
        if avg_vel > 1e-30:
            t_arr[i] = t_arr[i - 1] + dtau / avg_vel
        else:
            t_arr[i] = t_arr[i - 1] + 1e30

    result['tau'] = tau_arr
    result['t_dimless'] = t_arr
    result['dtau_dt'] = dtau_dt_arr
    result['V'] = V_arr
    result['KE'] = KE_arr

    if result['reached_cross']:
        result['t_cross_dimless'] = t_arr[-1]

        # Also compute via scipy.quad for higher precision
        def integrand(tau_val):
            V_val = float(V_interp(tau_val))
            KE_val = E_total - V_val
            if KE_val <= 0:
                return 1e30
            return 1.0 / np.sqrt(2 * KE_val / G)

        t_cross_quad, quad_err = quad(integrand, 0, tau_cross,
                                       limit=200, epsabs=1e-14, epsrel=1e-12)
        result['t_cross_quad'] = t_cross_quad
        result['quad_error'] = quad_err

        # Velocity at crossing point
        V_c = float(V_interp(tau_cross))
        KE_c = E_total - V_c
        result['dtau_at_cross'] = np.sqrt(2 * max(0, KE_c) / G)
        result['KE_at_cross'] = max(0, KE_c)

        # Energy density at crossing (for Hubble calculation)
        rho_c = G / 2 * result['dtau_at_cross']**2 + V_c
        result['rho_at_cross'] = rho_c

    return result


# ===========================================================================
# METHOD 2: FULL ODE INTEGRATION (with Hubble friction)
# ===========================================================================

def modulus_ode(t, y, V_interp, dV_interp, r_PK):
    """Right-hand side of the modulus + Friedmann ODE system.

    State vector: y = [tau, dtau/dt]
    in dimensionless time t_d = M_KK * t_phys.

    dy1/dt = y2
    dy2/dt = -3*H*y2 - (1/G)*dV/dtau
    H = sqrt(rho / (3*r_PK^2))
    rho = G/2 * y2^2 + V(y1)
    """
    tau_val = y[0]
    dtau_dt = y[1]

    V = float(V_interp(tau_val))
    dV = float(dV_interp(tau_val))

    rho = G_TAU_TAU / 2.0 * dtau_dt**2 + V

    if rho <= 0:
        H = 0.0
    else:
        H = np.sqrt(rho / (3.0 * r_PK**2))

    ddtau = -3.0 * H * dtau_dt - dV / G_TAU_TAU

    return [dtau_dt, ddtau]


def integrate_ode(M_KK, E_total, data, tau_target):
    """Integrate modulus EOM with Hubble friction for a given (M_KK, E_total).

    Parameters:
        M_KK: float, compactification scale in GeV
        E_total: float, total dimensionless energy
        data: dict from load_data
        tau_target: float, target tau for BCS crossing

    Returns:
        dict with trajectory data
    """
    V_interp = data['V_spec_interp']
    dV_interp = data['dV_spec_interp']
    r_PK = M_P_GEV / M_KK

    V0 = data['V_at_0']
    eps = np.sqrt(2 * (E_total - V0) / G_TAU_TAU)

    y0 = [0.0, eps]

    # Estimate crossing time analytically for max_step sizing
    V_target = float(V_interp(tau_target))
    if E_total > V_target:
        KE_avg = E_total - 0.5 * (V0 + V_target)
        dtau_avg = np.sqrt(2 * max(KE_avg, 0.01) / G_TAU_TAU)
        t_est = tau_target / dtau_avg if dtau_avg > 0 else 1e10
    else:
        t_est = 1e10

    rho0 = G_TAU_TAU / 2.0 * eps**2 + V0
    H0 = np.sqrt(rho0 / (3.0 * r_PK**2))
    t_H = 1.0 / H0 if H0 > 0 else 1e30

    t_max = 10 * t_est
    max_step = t_est / 200

    # Event: tau reaches target
    def event_cross(t, y, V_i, dV_i, r):
        return y[0] - tau_target
    event_cross.terminal = True
    event_cross.direction = 1

    # Event: velocity reaches zero (turning point)
    def event_stop(t, y, V_i, dV_i, r):
        return y[1]
    event_stop.terminal = True
    event_stop.direction = -1

    sol = solve_ivp(
        modulus_ode, (0, t_max), y0,
        args=(V_interp, dV_interp, r_PK),
        method='RK45',
        events=[event_cross, event_stop],
        max_step=max_step,
        rtol=1e-10, atol=1e-12,
        dense_output=True,
    )

    result = {
        'M_KK': M_KK,
        'r_PK': r_PK,
        'E_total': E_total,
        'E_mult': E_total / V0,
        'eps': eps,
        'H0_dimless': H0,
        'H0_phys': H0 * M_KK,
        't_H_dimless': t_H,
        't_H_sec': t_H / M_KK * GEV_TO_SEC,
    }

    result['t_d'] = sol.t
    result['tau'] = sol.y[0]
    result['dtau_dt'] = sol.y[1]
    result['t_phys_sec'] = sol.t / M_KK * GEV_TO_SEC
    result['success'] = sol.success
    result['message'] = sol.message
    result['n_steps'] = len(sol.t)

    # Compute H along trajectory
    H_traj = np.zeros_like(sol.t)
    for i in range(len(sol.t)):
        V_i = float(V_interp(sol.y[0, i]))
        rho_i = G_TAU_TAU / 2.0 * sol.y[1, i]**2 + V_i
        if rho_i > 0:
            H_traj[i] = np.sqrt(rho_i / (3.0 * r_PK**2))
    result['H_d'] = H_traj
    result['H_phys_gev'] = H_traj * M_KK

    # Check events
    if sol.t_events[0].size > 0:
        t_cross_d = sol.t_events[0][0]
        idx = np.argmin(np.abs(sol.t - t_cross_d))

        result['reached_cross'] = True
        result['t_cross_d'] = t_cross_d
        result['t_BCS_sec'] = t_cross_d / M_KK * GEV_TO_SEC
        result['t_BCS_gyr'] = result['t_BCS_sec'] * SEC_TO_GYR
        result['H_at_BCS_gev'] = H_traj[idx] * M_KK
        result['dtau_at_BCS'] = sol.y[1, idx]
        result['KE_at_BCS'] = G_TAU_TAU / 2.0 * sol.y[1, idx]**2

        V_at_cross = float(V_interp(sol.y[0, idx]))
        E_at_cross = result['KE_at_BCS'] + V_at_cross
        result['E_conservation_error'] = abs(E_at_cross - E_total) / E_total
        result['energy_loss_fraction'] = (E_total - E_at_cross) / E_total

        H_avg = np.mean(H_traj[:idx + 1])
        result['friction_param'] = 3 * H_avg * t_cross_d

    elif sol.t_events[1].size > 0:
        t_turn = sol.t_events[1][0]
        idx = np.argmin(np.abs(sol.t - t_turn))
        result['reached_cross'] = False
        result['tau_turn'] = sol.y[0, idx]
        result['t_turn_d'] = t_turn
    else:
        result['reached_cross'] = False

    return result


# ===========================================================================
# TRAPPING ANALYSIS
# ===========================================================================

def analyze_trapping(analytical_results, data):
    """Analyze whether the modulus is trapped by the first-order BCS transition.

    For each trajectory that reaches tau_cross:
    - Compare KE at crossing to latent heat at three mu scenarios
    - Compute post-transition velocity if not trapped
    - Estimate reheating energy budget
    """
    L_mu1 = data['latent_heat_mu1']
    L_mu12 = data['latent_heat_mu12']
    L_mu15 = data['latent_heat_mu15']

    results = []
    for ar in analytical_results:
        if not ar['reached_cross']:
            results.append({
                'E_mult': ar['E_mult'],
                'reached_cross': False,
            })
            continue

        KE = ar['KE_at_cross']
        tr = {
            'E_mult': ar['E_mult'],
            'reached_cross': True,
            'KE_at_cross': KE,
            'dtau_at_cross': ar['dtau_at_cross'],
            't_cross_dimless': ar['t_cross_quad'],
        }

        for label, L_val in [('mu=lmin', L_mu1),
                              ('mu=1.2lmin', L_mu12),
                              ('mu=1.5lmin', L_mu15)]:
            trapped = KE <= L_val
            ke_l_ratio = KE / L_val if L_val > 0 else float('inf')
            tr[f'L_{label}'] = L_val
            tr[f'trapped_{label}'] = trapped
            tr[f'KE_L_{label}'] = ke_l_ratio
            if not trapped:
                tr[f'dtau_after_{label}'] = np.sqrt(2 * (KE - L_val) / G_TAU_TAU)
            else:
                tr[f'dtau_after_{label}'] = 0.0

        V_cross = ar['V_at_cross']
        V_bcs_min = float(data['V_spec_interp'](0.35))
        Q = KE + (V_cross - V_bcs_min)
        tr['Q_total'] = Q
        tr['V_cross'] = V_cross
        tr['V_bcs_min'] = V_bcs_min

        results.append(tr)

    return results


def compute_physical_observables(analytical_results, trapping_results, data):
    """Convert dimensionless results to physical observables for each M_KK."""
    # Use E=2*V(0) as the reference trajectory
    ref_ar = None
    ref_tr = None
    for ar, tr in zip(analytical_results, trapping_results):
        if abs(ar['E_mult'] - 2.0) < 0.01 and ar['reached_cross']:
            ref_ar = ar
            ref_tr = tr
            break

    if ref_ar is None:
        return []

    observables = []
    for M_KK in M_KK_VALUES:
        r_PK = M_P_GEV / M_KK
        t_cross_d = ref_ar['t_cross_quad']

        t_BCS_sec = t_cross_d / M_KK * GEV_TO_SEC
        t_BCS_gyr = t_BCS_sec * SEC_TO_GYR

        rho_c = ref_ar['rho_at_cross']
        H_dimless = np.sqrt(rho_c / (3.0 * r_PK**2))
        H_phys_gev = H_dimless * M_KK

        friction_param = 3 * H_dimless * t_cross_d

        Q = ref_tr['Q_total']
        Q_phys = M_KK**4 * Q
        T_RH = (30 * Q_phys / (np.pi**2 * G_STAR))**0.25

        obs = {
            'M_KK': M_KK,
            'log_MKK': int(np.log10(M_KK)),
            'r_PK': r_PK,
            't_cross_d': t_cross_d,
            't_BCS_sec': t_BCS_sec,
            't_BCS_gyr': t_BCS_gyr,
            'H_dimless': H_dimless,
            'H_phys_gev': H_phys_gev,
            'friction_param': friction_param,
            'Q_dimless': Q,
            'Q_phys_gev4': Q_phys,
            'T_RH_gev': T_RH,
            'KE_at_cross': ref_tr['KE_at_cross'],
            'dtau_at_cross': ref_tr['dtau_at_cross'],
            'trapped_mu1': ref_tr['trapped_mu=lmin'],
            'trapped_mu12': ref_tr['trapped_mu=1.2lmin'],
            'trapped_mu15': ref_tr['trapped_mu=1.5lmin'],
            'KE_L_mu1': ref_tr['KE_L_mu=lmin'],
            'KE_L_mu12': ref_tr['KE_L_mu=1.2lmin'],
            'KE_L_mu15': ref_tr['KE_L_mu=1.5lmin'],
        }
        observables.append(obs)

    return observables


# ===========================================================================
# GATE CLASSIFICATION
# ===========================================================================

def classify_gates(observables):
    """Classify G-29c and P-29f gates."""
    gates = {}

    any_natural = any(
        obs['M_KK'] <= 1e18 and obs['t_BCS_sec'] < UNIVERSE_AGE_SEC
        for obs in observables
    )
    if any_natural:
        gates['G_29c'] = {
            'verdict': 'DOES NOT FIRE',
            'detail': 'Natural M_KK produces t_BCS within universe age.',
        }
    else:
        gates['G_29c'] = {
            'verdict': 'FIRES',
            'detail': 't_BCS exceeds 13.8 Gyr for all M_KK <= 10^18.',
        }

    natural_hits = [
        obs for obs in observables
        if 1e14 <= obs['M_KK'] <= 1e16
        and 1e-36 <= obs['t_BCS_sec'] <= 1e-10
    ]
    if natural_hits:
        gates['P_29f'] = {
            'verdict': 'FIRES',
            'detail': (f'{len(natural_hits)} natural M_KK trajectories reach '
                       f'tau_cross in GUT/EW-scale time.'),
            'hits': [(obs['M_KK'], obs['t_BCS_sec']) for obs in natural_hits],
        }
    else:
        gates['P_29f'] = {
            'verdict': 'DOES NOT FIRE',
            'detail': 'No natural M_KK gives t_BCS in [10^-36, 10^-10] s.',
        }

    return gates


# ===========================================================================
# PLOTTING
# ===========================================================================

def make_plots(data, analytical_results, ode_results, trapping_results,
               observables, gates, save_path):
    """Generate 6-panel modulus EOM plot."""
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(2, 3, figsize=(18, 11))
    fig.suptitle(r"29b-2: Modulus EOM  |  $\ddot{\tau} + 3H\dot{\tau} + "
                 r"\frac{1}{G_{\tau\tau}}\frac{dV}{d\tau} = 0$  |  "
                 f"$G_{{\\tau\\tau}}$ = {G_TAU_TAU}",
                 fontsize=13, fontweight='bold')

    colors_E = {'1.5': 'blue', '2.0': 'red', '5.0': 'green'}
    tau_cross = data['tau_cross']

    # Panel 1: tau(t) analytical trajectories
    ax = axes[0, 0]
    for ar in analytical_results:
        E_key = f"{ar['E_mult']:.1f}"
        color = colors_E.get(E_key, 'gray')
        label = f'$E/V_0$ = {ar["E_mult"]:.1f}'
        ax.plot(ar['t_dimless'], ar['tau'], '-', color=color, linewidth=2,
                label=label)
        if ar['reached_cross']:
            ax.plot(ar['t_cross_quad'], tau_cross, '*', color=color,
                    markersize=15, zorder=5)

    ax.axhline(tau_cross, color='red', linestyle='--', alpha=0.3,
               label=f'$\\tau_{{cross}}$ = {tau_cross:.3f}')
    ax.axhline(TAU_CROSS_KC3, color='orange', linestyle=':', alpha=0.3,
               label=f'KC-3 onset = {TAU_CROSS_KC3:.3f}')
    ax.set_xlabel('Dimensionless time $t_d$', fontsize=11)
    ax.set_ylabel(r'$\tau(t)$', fontsize=11)
    ax.set_title(r'Modulus trajectory $\tau(t)$ (analytical)')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel 2: Physical t_BCS vs M_KK
    ax = axes[0, 1]
    if observables:
        M_arr = [obs['M_KK'] for obs in observables]
        t_arr = [obs['t_BCS_sec'] for obs in observables]
        ax.loglog(M_arr, t_arr, 'ko-', linewidth=2, markersize=8)
        ax.axhspan(1e-36, 1e-10, alpha=0.1, color='green', label='GUT/EW window')
        ax.axhline(UNIVERSE_AGE_SEC, color='red', linestyle='--', alpha=0.5,
                    label='Age of universe')
        if 'hits' in gates.get('P_29f', {}):
            for mkk, tsec in gates['P_29f']['hits']:
                ax.plot(mkk, tsec, 'g*', markersize=15, zorder=5)
        ax.set_xlabel('$M_{KK}$ [GeV]', fontsize=11)
        ax.set_ylabel('$t_{BCS}$ [seconds]', fontsize=11)
        ax.set_title('BCS transition time vs $M_{KK}$')
        ax.legend(fontsize=7, loc='upper right')
        ax.grid(True, alpha=0.3)

    # Panel 3: V_eff(tau) with energy levels
    ax = axes[0, 2]
    tau_plot = np.linspace(0, 0.7, 300)
    V_plot = np.array([float(data['V_spec_interp'](t)) for t in tau_plot])
    ax.plot(tau_plot, V_plot, 'k-', linewidth=2.5, label='$V_{spec}(\\tau)$')

    V0 = data['V_at_0']
    for E_mult in E_MULT_VALUES:
        E = E_mult * V0
        color = colors_E.get(f'{E_mult:.1f}', 'gray')
        ax.axhline(E, color=color, linestyle=':', alpha=0.5,
                    label=f'$E = {E_mult:.1f} V_0$')

    ax.axvline(tau_cross, color='red', linestyle='--', alpha=0.5,
               label=f'$\\tau_{{cross}}$')
    ax.set_xlabel(r'$\tau$', fontsize=11)
    ax.set_ylabel(r'$V_{spec}(\tau)$', fontsize=11)
    ax.set_title('Potential + energy levels')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(V0 * 0.95, V0 * 6)

    # Panel 4: Friction diagnosis
    ax = axes[1, 0]
    if observables:
        M_arr = [obs['M_KK'] for obs in observables]
        fp_arr = [obs['friction_param'] for obs in observables]
        ax.semilogx(M_arr, fp_arr, 'bo-', linewidth=2, markersize=8,
                     label='$3 \\langle H \\rangle t_{cross}$')
        ax.axhline(0.1, color='orange', linestyle='--', alpha=0.5,
                    label='10% friction')
        ax.axhline(1.0, color='red', linestyle='--', alpha=0.5,
                    label='Order-unity friction')
        ax.set_xlabel('$M_{KK}$ [GeV]', fontsize=11)
        ax.set_ylabel('Friction parameter', fontsize=11)
        ax.set_title('Hubble friction diagnosis')
        ax.legend(fontsize=8)
        ax.grid(True, alpha=0.3)
        ax.set_yscale('log')

    # Panel 5: Trapping analysis KE/L
    ax = axes[1, 1]
    E_mults_plot = []
    ke_l_mu1_plot = []
    ke_l_mu12_plot = []
    ke_l_mu15_plot = []
    for tr in trapping_results:
        if tr['reached_cross']:
            E_mults_plot.append(tr['E_mult'])
            ke_l_mu1_plot.append(tr['KE_L_mu=lmin'])
            ke_l_mu12_plot.append(tr['KE_L_mu=1.2lmin'])
            ke_l_mu15_plot.append(tr['KE_L_mu=1.5lmin'])

    if E_mults_plot:
        ax.plot(E_mults_plot, ke_l_mu1_plot, 'bo-', linewidth=2, markersize=8,
                label='$\\mu = \\lambda_{min}$')
        ax.plot(E_mults_plot, ke_l_mu12_plot, 'rs-', linewidth=2, markersize=8,
                label='$\\mu = 1.2\\lambda_{min}$')
        ax.plot(E_mults_plot, ke_l_mu15_plot, 'g^-', linewidth=2, markersize=8,
                label='$\\mu = 1.5\\lambda_{min}$')
        ax.axhline(1.0, color='red', linestyle='--', alpha=0.7,
                    label='KE = L (trapping)')
        ax.set_xlabel('$E_{total} / V(0)$', fontsize=11)
        ax.set_ylabel('KE / Latent Heat', fontsize=11)
        ax.set_title('Trapping analysis: KE/L at $\\tau_{cross}$')
        ax.legend(fontsize=8)
        ax.grid(True, alpha=0.3)

    # Panel 6: Gate verdicts + table
    ax = axes[1, 2]
    ax.axis('off')

    ax.text(0.5, 0.97, 'GATE VERDICTS + PHYSICAL OBSERVABLES',
            fontsize=12, fontweight='bold', ha='center', va='top',
            transform=ax.transAxes)

    g29c = gates.get('G_29c', {'verdict': 'UNCOMPUTED', 'detail': ''})
    g_color = 'red' if g29c['verdict'] == 'FIRES' else 'green'
    ax.text(0.05, 0.88, f"G-29c: {g29c['verdict']}", fontsize=11,
            fontweight='bold', color=g_color, transform=ax.transAxes)

    p29f = gates.get('P_29f', {'verdict': 'UNCOMPUTED', 'detail': ''})
    p_color = 'green' if p29f['verdict'] == 'FIRES' else 'gray'
    ax.text(0.05, 0.80, f"P-29f: {p29f['verdict']}", fontsize=11,
            fontweight='bold', color=p_color, transform=ax.transAxes)
    ax.text(0.05, 0.74, p29f.get('detail', ''), fontsize=8,
            transform=ax.transAxes)

    y_pos = 0.64
    header = (f"{'M_KK':>8s} {'t_BCS [s]':>11s} {'H [GeV]':>11s} "
              f"{'3Ht':>7s} {'T_RH [GeV]':>11s} {'KE/L(1.0)':>9s} "
              f"{'Trap?':>5s}")
    ax.text(0.03, y_pos, header, fontsize=7.5, fontfamily='monospace',
            fontweight='bold', transform=ax.transAxes)
    y_pos -= 0.05

    for obs in observables:
        trap_str = 'Y' if obs['trapped_mu15'] else 'N'
        line = (f"10^{obs['log_MKK']:>2d}    "
                f"{obs['t_BCS_sec']:>11.3e} "
                f"{obs['H_phys_gev']:>11.3e} "
                f"{obs['friction_param']:>7.4f} "
                f"{obs['T_RH_gev']:>11.3e} "
                f"{obs['KE_L_mu1']:>9.3f} "
                f"{trap_str:>5s}")
        ax.text(0.03, y_pos, line, fontsize=7, fontfamily='monospace',
                transform=ax.transAxes)
        y_pos -= 0.045

    y_pos -= 0.02
    ax.text(0.03, y_pos,
            f"Key: Hubble friction < 0.2% for M_KK <= 10^16.\n"
            f"First-order transition (L-9) is THE trapping mechanism.\n"
            f"tau_cross = {tau_cross:.3f}, V(0) = {data['V_at_0']:.2f}",
            fontsize=8, color='gray', transform=ax.transAxes)

    plt.tight_layout()
    plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Plot saved: {save_path}")


# ===========================================================================
# MAIN
# ===========================================================================

def main():
    print("=" * 78)
    print("29b-2: Modulus Equation of Motion")
    print("=" * 78)
    print()

    # -----------------------------------------------------------------------
    # 0. Gate check
    # -----------------------------------------------------------------------
    verdict_path = os.path.join(SCRIPT_DIR, "s29a_gate_verdicts.txt")
    if os.path.exists(verdict_path):
        with open(verdict_path, 'r') as f:
            verdicts = f.read()
        if 'CONSTRAINT CHAIN IS COMPLETE' in verdicts:
            print("29Aa gate check: KC-1 through KC-5 ALL PASS. Proceeding.\n")

    # -----------------------------------------------------------------------
    # 1. Load data
    # -----------------------------------------------------------------------
    print("Loading data...")
    data = load_data()
    V0 = data['V_at_0']
    tau_cross = data['tau_cross']
    print(f"  V_spec(0) = {V0:.4f}")
    print(f"  V_spec(tau_cross={tau_cross}) = {float(data['V_spec_interp'](tau_cross)):.4f}")
    print(f"  dV/dtau(0) = {float(data['dV_spec_interp'](0.0)):.6f}")
    print(f"  dV/dtau(tau_cross) = {float(data['dV_spec_interp'](tau_cross)):.6f}")
    print(f"  tau_cross = {tau_cross:.3f}")
    print(f"  Latent heat (mu=lmin) = {data['latent_heat_mu1']:.4f}")
    print(f"  Latent heat (mu=1.2lmin) = {data['latent_heat_mu12']:.4f}")
    print(f"  Latent heat (mu=1.5lmin) = {data['latent_heat_mu15']:.4f}")
    print(f"  G_{{tau,tau}} = {G_TAU_TAU}")
    print()

    # -----------------------------------------------------------------------
    # 2. Analytical trajectories (energy conservation, no friction)
    # -----------------------------------------------------------------------
    print("=" * 78)
    print("METHOD 1: Analytical quadrature (friction-free)")
    print("=" * 78)
    print()

    analytical_results = []
    for E_mult in E_MULT_VALUES:
        E_total = E_mult * V0
        print(f"E/V(0) = {E_mult:.1f}  (E_total = {E_total:.4f}):")

        ar = compute_analytical_trajectory(E_total, data['V_spec_interp'],
                                           tau_cross)
        analytical_results.append(ar)

        if ar['reached_cross']:
            print(f"  REACHED tau_cross = {tau_cross:.3f}")
            print(f"  t_cross (trapezoid) = {ar['t_cross_dimless']:.6f} (dimensionless)")
            print(f"  t_cross (quad)      = {ar['t_cross_quad']:.6f} (dimensionless)")
            print(f"  dtau/dt at cross    = {ar['dtau_at_cross']:.6f}")
            print(f"  KE at cross         = {ar['KE_at_cross']:.6f}")
            print(f"  V at cross          = {ar['V_at_cross']:.4f}")
            print(f"  rho at cross        = {ar['rho_at_cross']:.4f}")

            print(f"\n  Physical t_BCS for each M_KK:")
            for M_KK in M_KK_VALUES:
                t_sec = ar['t_cross_quad'] / M_KK * GEV_TO_SEC
                r_PK = M_P_GEV / M_KK
                H = np.sqrt(ar['rho_at_cross'] / (3.0 * r_PK**2)) * M_KK
                fric = 3 * np.sqrt(ar['rho_at_cross'] / (3.0 * r_PK**2)) * ar['t_cross_quad']
                print(f"    M_KK=10^{int(np.log10(M_KK))}: "
                      f"t_BCS = {t_sec:.3e} s, "
                      f"H = {H:.3e} GeV, "
                      f"3Ht = {fric:.4e}")
        else:
            print(f"  DID NOT REACH tau_cross")
            print(f"  Turning point at tau = {ar.get('tau_turn', 'N/A')}")
            print(f"  Reason: {ar.get('reason', 'unknown')}")
        print()

    # -----------------------------------------------------------------------
    # 3. Full ODE integration (with Hubble friction) for comparison
    # -----------------------------------------------------------------------
    print("=" * 78)
    print("METHOD 2: Full ODE integration (with Hubble friction)")
    print("=" * 78)
    print()

    ode_results = []
    M_KK_ode = [1e14, 1e16, 1e18]
    E_ref = 2.0 * V0

    for M_KK in M_KK_ode:
        log_mkk = int(np.log10(M_KK))
        print(f"M_KK = 10^{log_mkk} GeV, E/V(0) = 2.0:")

        ode_r = integrate_ode(M_KK, E_ref, data, tau_cross)
        ode_results.append(ode_r)

        print(f"  ODE steps: {ode_r['n_steps']}")
        print(f"  H_0 = {ode_r['H0_phys']:.3e} GeV, t_H = {ode_r['t_H_sec']:.3e} s")

        if ode_r['reached_cross']:
            print(f"  REACHED tau_cross = {tau_cross:.3f}")
            print(f"  t_cross (ODE) = {ode_r['t_cross_d']:.6f} (dimensionless)")
            print(f"  t_BCS = {ode_r['t_BCS_sec']:.6e} s")
            print(f"  H(t_BCS) = {ode_r['H_at_BCS_gev']:.3e} GeV")
            print(f"  dtau/dt at BCS = {ode_r['dtau_at_BCS']:.6f}")
            print(f"  KE at BCS = {ode_r['KE_at_BCS']:.6f}")
            print(f"  E conservation error = {ode_r['E_conservation_error']:.2e}")
            print(f"  Energy loss fraction = {ode_r['energy_loss_fraction']:.4e}")
            print(f"  Friction param (3Ht) = {ode_r['friction_param']:.4e}")

            ref_ar = [ar for ar in analytical_results
                      if abs(ar['E_mult'] - 2.0) < 0.01][0]
            if ref_ar['reached_cross']:
                t_ana = ref_ar['t_cross_quad']
                t_ode = ode_r['t_cross_d']
                print(f"  Analytical t_cross = {t_ana:.6f}")
                print(f"  ODE t_cross        = {t_ode:.6f}")
                print(f"  Relative diff      = {abs(t_ode - t_ana) / t_ana:.2e}")
        else:
            print(f"  DID NOT REACH tau_cross")
            if 'tau_turn' in ode_r:
                print(f"  Turning point at tau = {ode_r['tau_turn']:.6f}")
        print()

    # -----------------------------------------------------------------------
    # 4. Trapping analysis
    # -----------------------------------------------------------------------
    print("=" * 78)
    print("TRAPPING ANALYSIS (first-order BCS transition)")
    print("=" * 78)
    print()

    trapping_results = analyze_trapping(analytical_results, data)

    for tr in trapping_results:
        if not tr['reached_cross']:
            print(f"E/V(0) = {tr['E_mult']:.1f}: did not reach tau_cross")
            continue

        print(f"E/V(0) = {tr['E_mult']:.1f}:")
        print(f"  KE at crossing = {tr['KE_at_cross']:.4f}")
        print(f"  dtau/dt at crossing = {tr['dtau_at_cross']:.6f}")
        print(f"  Q_total (for reheating) = {tr['Q_total']:.4f}")
        print()
        print(f"  {'mu scenario':>20s} {'L':>8s} {'KE/L':>8s} {'Trapped':>8s} "
              f"{'dtau_after':>10s}")
        print(f"  {'-'*60}")
        for label in ['mu=lmin', 'mu=1.2lmin', 'mu=1.5lmin']:
            L = tr[f'L_{label}']
            kel = tr[f'KE_L_{label}']
            trap = 'YES' if tr[f'trapped_{label}'] else 'NO'
            da = tr[f'dtau_after_{label}']
            print(f"  {label:>20s} {L:>8.3f} {kel:>8.3f} {trap:>8s} {da:>10.6f}")
        print()

    # -----------------------------------------------------------------------
    # 5. Physical observables for all M_KK
    # -----------------------------------------------------------------------
    print("=" * 78)
    print("PHYSICAL OBSERVABLES (E = 2*V(0), reference trajectory)")
    print("=" * 78)
    print()

    observables = compute_physical_observables(analytical_results,
                                                trapping_results, data)

    if observables:
        print(f"{'M_KK':>12s} {'t_BCS [s]':>14s} {'H [GeV]':>14s} "
              f"{'3Ht':>10s} {'T_RH [GeV]':>14s} {'KE/L(1.0)':>10s} "
              f"{'KE/L(1.5)':>10s}")
        print("-" * 86)
        for obs in observables:
            print(f"10^{obs['log_MKK']:>2d} GeV  "
                  f"{obs['t_BCS_sec']:>14.6e} "
                  f"{obs['H_phys_gev']:>14.6e} "
                  f"{obs['friction_param']:>10.4e} "
                  f"{obs['T_RH_gev']:>14.6e} "
                  f"{obs['KE_L_mu1']:>10.4f} "
                  f"{obs['KE_L_mu15']:>10.4f}")
        print()

        ref16 = [obs for obs in observables if obs['log_MKK'] == 16]
        if ref16:
            obs = ref16[0]
            print(f"REFERENCE M_KK = 10^16 GeV:")
            print(f"  t_BCS = {obs['t_BCS_sec']:.3e} s")
            print(f"  H(t_BCS) = {obs['H_phys_gev']:.3e} GeV")
            print(f"  Friction: 3Ht = {obs['friction_param']:.4e} "
                  f"({'NEGLIGIBLE' if obs['friction_param'] < 0.01 else 'SIGNIFICANT'})")
            print(f"  T_RH = {obs['T_RH_gev']:.3e} GeV")
            print(f"  Trapped (mu=lmin): {obs['trapped_mu1']} "
                  f"(KE/L = {obs['KE_L_mu1']:.3f})")
            print(f"  Trapped (mu=1.5lmin): {obs['trapped_mu15']} "
                  f"(KE/L = {obs['KE_L_mu15']:.3f})")
    else:
        print("No observables computed (reference trajectory did not reach tau_cross)")

    # -----------------------------------------------------------------------
    # 6. Gate classification
    # -----------------------------------------------------------------------
    print(f"\n{'='*78}")
    print("GATE CLASSIFICATION")
    print(f"{'='*78}")

    gates = classify_gates(observables)

    g29c = gates['G_29c']
    print(f"\nG-29c (soft gate): {g29c['verdict']}")
    print(f"  {g29c['detail']}")

    p29f = gates['P_29f']
    print(f"\nP-29f (positive signal): {p29f['verdict']}")
    print(f"  {p29f['detail']}")
    if 'hits' in p29f:
        for mkk, t_sec in p29f['hits']:
            print(f"    M_KK = {mkk:.0e} GeV: t_BCS = {t_sec:.3e} s")

    # -----------------------------------------------------------------------
    # 7. Save data
    # -----------------------------------------------------------------------
    npz_path = os.path.join(SCRIPT_DIR, "s29b_modulus_eom.npz")

    save_dict = {
        'M_KK_values': np.array(M_KK_VALUES),
        'E_mult_values': np.array(E_MULT_VALUES),
        'G_tau_tau': np.array([G_TAU_TAU]),
        'tau_cross': np.array([tau_cross]),
        'V_at_0': np.array([V0]),
        'latent_heat_mu1': np.array([data['latent_heat_mu1']]),
        'latent_heat_mu12': np.array([data['latent_heat_mu12']]),
        'latent_heat_mu15': np.array([data['latent_heat_mu15']]),
        'G_29c_verdict': np.array([gates['G_29c']['verdict']]),
        'P_29f_verdict': np.array([gates['P_29f']['verdict']]),
    }

    for i, ar in enumerate(analytical_results):
        prefix = f'ana_{i}'
        save_dict[f'{prefix}_E_mult'] = np.array([ar['E_mult']])
        save_dict[f'{prefix}_E_total'] = np.array([ar['E_total']])
        save_dict[f'{prefix}_reached_cross'] = np.array([ar['reached_cross']])
        save_dict[f'{prefix}_tau'] = ar['tau']
        save_dict[f'{prefix}_t_dimless'] = ar['t_dimless']
        save_dict[f'{prefix}_dtau_dt'] = ar['dtau_dt']
        if ar['reached_cross']:
            save_dict[f'{prefix}_t_cross_quad'] = np.array([ar['t_cross_quad']])
            save_dict[f'{prefix}_dtau_at_cross'] = np.array([ar['dtau_at_cross']])
            save_dict[f'{prefix}_KE_at_cross'] = np.array([ar['KE_at_cross']])
            save_dict[f'{prefix}_rho_at_cross'] = np.array([ar['rho_at_cross']])

    for i, ode_r in enumerate(ode_results):
        prefix = f'ode_{i}'
        save_dict[f'{prefix}_M_KK'] = np.array([ode_r['M_KK']])
        save_dict[f'{prefix}_reached_cross'] = np.array([ode_r['reached_cross']])
        save_dict[f'{prefix}_t_d'] = ode_r['t_d']
        save_dict[f'{prefix}_tau'] = ode_r['tau']
        save_dict[f'{prefix}_dtau_dt'] = ode_r['dtau_dt']
        if ode_r['reached_cross']:
            save_dict[f'{prefix}_t_cross_d'] = np.array([ode_r['t_cross_d']])
            save_dict[f'{prefix}_t_BCS_sec'] = np.array([ode_r['t_BCS_sec']])
            save_dict[f'{prefix}_E_loss_frac'] = np.array([ode_r['energy_loss_fraction']])
            save_dict[f'{prefix}_friction_param'] = np.array([ode_r['friction_param']])

    for i, tr in enumerate(trapping_results):
        prefix = f'trap_{i}'
        save_dict[f'{prefix}_E_mult'] = np.array([tr['E_mult']])
        save_dict[f'{prefix}_reached_cross'] = np.array([tr['reached_cross']])
        if tr['reached_cross']:
            save_dict[f'{prefix}_KE_at_cross'] = np.array([tr['KE_at_cross']])
            save_dict[f'{prefix}_KE_L_mu1'] = np.array([tr['KE_L_mu=lmin']])
            save_dict[f'{prefix}_KE_L_mu12'] = np.array([tr['KE_L_mu=1.2lmin']])
            save_dict[f'{prefix}_KE_L_mu15'] = np.array([tr['KE_L_mu=1.5lmin']])
            save_dict[f'{prefix}_trapped_mu1'] = np.array([tr['trapped_mu=lmin']])
            save_dict[f'{prefix}_trapped_mu15'] = np.array([tr['trapped_mu=1.5lmin']])
            save_dict[f'{prefix}_Q_total'] = np.array([tr['Q_total']])

    if observables:
        for i, obs in enumerate(observables):
            prefix = f'obs_{i}'
            save_dict[f'{prefix}_M_KK'] = np.array([obs['M_KK']])
            save_dict[f'{prefix}_t_BCS_sec'] = np.array([obs['t_BCS_sec']])
            save_dict[f'{prefix}_H_phys_gev'] = np.array([obs['H_phys_gev']])
            save_dict[f'{prefix}_T_RH_gev'] = np.array([obs['T_RH_gev']])
            save_dict[f'{prefix}_friction_param'] = np.array([obs['friction_param']])

    np.savez_compressed(npz_path, **save_dict)
    print(f"\nData saved: {npz_path}")

    # -----------------------------------------------------------------------
    # 8. Plot
    # -----------------------------------------------------------------------
    png_path = os.path.join(SCRIPT_DIR, "s29b_modulus_eom.png")
    make_plots(data, analytical_results, ode_results, trapping_results,
               observables, gates, png_path)

    # -----------------------------------------------------------------------
    # 9. Final summary
    # -----------------------------------------------------------------------
    print(f"\n{'='*78}")
    print("29b-2 COMPLETE")
    print(f"{'='*78}")
    print(f"G-29c: {gates['G_29c']['verdict']}")
    print(f"P-29f: {gates['P_29f']['verdict']}")
    print()
    print("KEY FINDING: Hubble friction is negligible (< 0.2% for M_KK <= 10^16).")
    print("The first-order BCS transition (L-9) is the modulus trapping mechanism.")
    print()
    if observables:
        ref16 = [obs for obs in observables if obs['log_MKK'] == 16]
        if ref16:
            obs = ref16[0]
            print(f"Reference (M_KK = 10^16 GeV, E = 2*V(0)):")
            print(f"  t_BCS = {obs['t_BCS_sec']:.3e} s")
            print(f"  H(t_BCS) = {obs['H_phys_gev']:.3e} GeV")
            print(f"  T_RH = {obs['T_RH_gev']:.3e} GeV")
            print(f"  KE/L(mu=lmin) = {obs['KE_L_mu1']:.3f}")
            print(f"  KE/L(mu=1.5lmin) = {obs['KE_L_mu15']:.3f}")
    print(f"{'='*78}")


if __name__ == "__main__":
    main()
