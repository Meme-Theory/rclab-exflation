#!/usr/bin/env python3
"""
Session 36: TAU-DYN-36 -- Tau Dynamics: Moduli Trajectory Through the Fold
===========================================================================

CONTEXT:
  The Jensen deformation parameter tau is a modulus field that ROLLS in the
  effective 4D theory. The spectral action S(tau) provides the potential energy
  landscape. tau(t) obeys a Klein-Gordon equation coupled to Friedmann expansion.

  The framework claims that tau starts at some initial value and rolls toward
  tau = 0 (round SU(3), the minimum of S_full). During this roll, tau passes
  through the van Hove fold at tau_fold ~ 0.190, where the BCS pairing window
  [0.175, 0.205] opens. The question: does the trajectory DWELL in the fold
  region long enough for BCS condensation to activate?

  This is the nuclear physicist's question about reaction timescales:
  the compound nucleus must live long enough for the relevant decay channel
  to compete. Here, the "compound state" is the fold configuration, and
  the "decay channel" is BCS pair formation.

PHYSICS:
  1. Moduli space metric G_mod from KK reduction of Einstein-Hilbert on SU(3).
     For the Jensen volume-preserving deformation, G_mod is CONSTANT:
       G_mod = (1/4) sum_I n_I (d ln g_I / dtau)^2 = 5.0
     (scale factor normalization, standard Scherk-Schwarz)
     Jensen: lambda_2 = e^{-2tau} (SU(2), x3), lambda_3 = e^{tau} (coset, x4),
             lambda_1 = e^{2tau} (U(1), x1).
     Volume-preserving: d ln g_I / dtau sums to zero (3*(-2) + 4*(1) + 1*(2) = 0).
     G_mod = (1/4)*[3*4 + 4*1 + 1*4] = 5.0 (constant, tau-independent).

  2. Effective potential V_eff(tau) = S_full(tau) from multi-sector spectral action.
     Monotonically increasing: V_eff' > 0 for all tau in [0, 0.5].
     Minimum at tau = 0 (round SU(3)).

  3. Equation of motion (FRW background):
       G_mod * d^2tau/dt^2 + 3H * G_mod * dtau/dt + V_eff'(tau) = 0
     Friedmann: H^2 = (1/3) * [(1/2)*G_mod*(dtau/dt)^2 + V_eff(tau)]

  4. The system is OVERDAMPED: 3H/(2*omega) = 1.74 at the fold.
     Terminal velocity: v_term = -V'/(3*H*G_mod).
     This determines the dwell time analytically.

  5. Slow-roll parameters epsilon and eta from standard inflationary definitions
     adapted to the moduli space metric.

GATE TAU-DYN-36 (pre-registered):
  PASS:      tau_dwell / tau_BCS > 1  -> condensation has time to activate
  SLOW ROLL: epsilon < 1 at fold      -> tau lingers in fold region
  FAST ROLL: epsilon >> 1 AND tau_dwell/tau_BCS < 1 -> no condensation
  TRAPPED:   BCS back-reaction creates local trapping

Author: nazarewicz-nuclear-structure-theorist, Session 36 Wave 4
Date: 2026-03-07
"""

import os
import time
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
t0_wall = time.time()

# ======================================================================
#  Constants
# ======================================================================
# Moduli space metric (CONSTANT for volume-preserving Jensen deformation)
# G_mod = (1/4) * [3*(-2)^2 + 4*(1)^2 + 1*(2)^2] = 5.0
G_MOD = 5.0
G_MOD_ALT = 20.0 / 7.0  # Trace-free projected (alternative normalization)

# BCS parameters (from Session 35/36)
DELTA_MAX = 0.025           # Max BCS gap
TAU_BCS = 1.0 / DELTA_MAX  # BCS formation timescale = 40.0
E_COND_PEAK = -0.156        # Peak BCS condensation energy
from canonical_constants import tau_fold as TAU_FOLD
BCS_WINDOW = (0.175, 0.205) # Pairing window (width = 0.030)
WINDOW_WIDTH = BCS_WINDOW[1] - BCS_WINDOW[0]


# ======================================================================
#  Load Data
# ======================================================================
def load_data():
    """Load spectral action and BCS data."""
    print("Step 1: Loading data...")
    strutinsky = np.load(os.path.join(SCRIPT_DIR, 's33a_strutinsky.npz'),
                         allow_pickle=True)
    gcm = np.load(os.path.join(SCRIPT_DIR, 's36_gcm_self_consistent.npz'),
                  allow_pickle=True)

    tau_coarse = strutinsky['tau_values']
    S_singlet = strutinsky['S_singlet']
    S_full = strutinsky['S_full']
    tau_fine = gcm['tau_fine']
    E_BCS_fine = gcm['E_BCS_fine']

    print(f"  tau_coarse: {tau_coarse}")
    print(f"  S_full:     [{S_full[0]:.1f}, ..., {S_full[-1]:.1f}]")
    print(f"  S_singlet:  [{S_singlet[0]:.4f}, ..., {S_singlet[-1]:.4f}]")

    return tau_coarse, S_singlet, S_full, tau_fine, E_BCS_fine


# ======================================================================
#  Build Spline Potentials
# ======================================================================
def build_potentials(tau_coarse, S_singlet, S_full, tau_fine, E_BCS_fine):
    """Build cubic spline interpolators for the potentials."""
    cs_full = CubicSpline(tau_coarse, S_full)
    cs_sing = CubicSpline(tau_coarse, S_singlet)
    cs_EBCS = CubicSpline(tau_fine, E_BCS_fine)
    return cs_full, cs_sing, cs_EBCS


# ======================================================================
#  Slow-Roll Parameters
# ======================================================================
def compute_slow_roll(cs_V, G_mod, label=""):
    """Compute epsilon(tau) and eta(tau) for a given potential."""
    tau_arr = np.linspace(0.001, 0.499, 1000)
    V = cs_V(tau_arr)
    dV = cs_V(tau_arr, 1)
    d2V = cs_V(tau_arr, 2)

    epsilon = (1.0 / (2.0 * G_mod)) * (dV / V)**2
    eta = (1.0 / G_mod) * (d2V / V)

    # At fold
    V_f = cs_V(TAU_FOLD)
    dV_f = cs_V(TAU_FOLD, 1)
    d2V_f = cs_V(TAU_FOLD, 2)
    eps_f = (1.0 / (2.0 * G_mod)) * (dV_f / V_f)**2
    eta_f = (1.0 / G_mod) * (d2V_f / V_f)

    print(f"\n  Slow-roll ({label}, G_mod={G_mod:.3f}):")
    print(f"    V(fold)={V_f:.4f}, V'(fold)={dV_f:.4f}, V''(fold)={d2V_f:.4f}")
    print(f"    epsilon(fold)={eps_f:.6f}, eta(fold)={eta_f:.6f}")
    print(f"    epsilon<1: {eps_f<1}, |eta|<1: {abs(eta_f)<1}")

    return tau_arr, epsilon, eta, eps_f, eta_f


# ======================================================================
#  Analytical Estimates (Overdamped Regime)
# ======================================================================
def analytical_estimates(cs_V, G_mod, label=""):
    """Compute terminal velocity and transit time analytically."""
    V_f = cs_V(TAU_FOLD)
    dV_f = cs_V(TAU_FOLD, 1)
    d2V_f = cs_V(TAU_FOLD, 2)

    H_f = np.sqrt(V_f / 3.0)        # Hubble at fold (KE << V)
    omega_f = np.sqrt(abs(d2V_f) / G_mod)  # Oscillation frequency
    zeta = 3.0 * H_f / (2.0 * omega_f)     # Damping ratio

    # Terminal velocity in overdamped regime
    v_term = -dV_f / (3.0 * H_f * G_mod)

    # Transit time through BCS window
    dt_transit = WINDOW_WIDTH / abs(v_term)

    print(f"\n  Analytical ({label}):")
    print(f"    H(fold)         = {H_f:.4f}")
    print(f"    omega(fold)     = {omega_f:.4f}")
    print(f"    Damping ratio   = {zeta:.4f} ({'overdamped' if zeta>1 else 'underdamped'})")
    print(f"    v_terminal      = {v_term:.6f}")
    print(f"    dt_transit      = {dt_transit:.6e}")
    print(f"    dt/tau_BCS      = {dt_transit/TAU_BCS:.6e}")

    return {
        'H_fold': H_f, 'omega_fold': omega_f, 'zeta': zeta,
        'v_terminal': v_term, 'dt_transit': dt_transit,
        'dt_over_tau_BCS': dt_transit / TAU_BCS,
    }


# ======================================================================
#  Numerical Integration
# ======================================================================
def solve_trajectory(cs_V, G_mod, tau0, t_end, max_step=1e-6,
                     include_BCS=False, cs_EBCS=None, label=""):
    """Solve the moduli EOM numerically with fine time resolution."""

    def rhs(t, y):
        tau, v = y
        tau_c = np.clip(tau, 0.0, 0.50)
        V = cs_V(tau_c)
        dV = cs_V(tau_c, 1)
        if include_BCS and cs_EBCS is not None:
            if BCS_WINDOW[0] <= tau_c <= BCS_WINDOW[1]:
                V += cs_EBCS(tau_c)
                dV += cs_EBCS(tau_c, 1)
        KE = 0.5 * G_mod * v**2
        H2 = (1.0/3.0) * (KE + V)
        H = np.sqrt(max(H2, 0))
        a = -3.0 * H * v - dV / G_mod
        return [v, a]

    sol = solve_ivp(rhs, (0, t_end), [tau0, 0.0], method='RK45',
                    max_step=max_step, rtol=1e-12, atol=1e-14,
                    dense_output=True)

    if not sol.success:
        print(f"  WARNING: Integration failed for {label}: {sol.message}")
        return None

    # Dense evaluation for precise dwell time
    n_pts = max(200000, int(t_end / max_step))
    n_pts = min(n_pts, 500000)
    t = np.linspace(0, sol.t[-1], n_pts)
    y = sol.sol(t)
    tau = y[0]
    v = y[1]

    # Dwell time in BCS window
    in_w = (tau >= BCS_WINDOW[0]) & (tau <= BCS_WINDOW[1])
    if np.any(in_w):
        t_in = t[in_w]
        dt_dwell = t_in[-1] - t_in[0]
        idx_mid = np.where(in_w)[0][len(t_in)//2]
        v_mid = v[idx_mid]
    else:
        dt_dwell = 0.0
        v_mid = 0.0

    # Velocity at fold
    idx_fold = np.argmin(np.abs(tau - TAU_FOLD))
    v_fold = v[idx_fold]

    # Fold crossing analysis
    crosses = np.where(np.diff(np.sign(tau - TAU_FOLD)))[0]
    t_cross = t[crosses[0]] if len(crosses) > 0 else np.nan

    info = {
        't': t, 'tau': tau, 'v': v, 'sol': sol,
        't_dwell': dt_dwell, 'v_fold': v_fold, 'v_mid_window': v_mid,
        't_cross': t_cross, 'label': label,
    }

    print(f"\n  Trajectory ({label}):")
    print(f"    tau0={tau0:.2f}, t_end={t_end}")
    print(f"    tau final={tau[-1]:.6f}, v at fold={v_fold:.6f}")
    print(f"    Dwell time={dt_dwell:.6e}, Dwell/tau_BCS={dt_dwell/TAU_BCS:.6e}")
    if not np.isnan(t_cross):
        print(f"    Fold crossing at t={t_cross:.6e}")

    return info


# ======================================================================
#  MAIN
# ======================================================================
def main():
    print("=" * 78)
    print("TAU-DYN-36: Tau Dynamics -- Moduli Trajectory Through the Fold")
    print("Nazarewicz Nuclear Structure Theorist")
    print("=" * 78)

    # Load data
    tau_coarse, S_singlet, S_full, tau_fine, E_BCS_fine = load_data()
    cs_full, cs_sing, cs_EBCS = build_potentials(
        tau_coarse, S_singlet, S_full, tau_fine, E_BCS_fine)

    # ================================================================
    #  MODULI SPACE METRIC
    # ================================================================
    print(f"\n{'='*78}")
    print(f"Step 2: Moduli Space Metric")
    print(f"{'='*78}")
    print(f"  Jensen metric: lambda_1=e^(2tau), lambda_2=e^(-2tau), lambda_3=e^(tau)")
    print(f"  Multiplicities: n_1=1 (U(1)), n_2=3 (SU(2)), n_3=4 (coset)")
    print(f"  d ln g / dtau: [2, -2, -2, -2, 1, 1, 1, 1]")
    print(f"  Trace check: 1*2 + 3*(-2) + 4*1 = {1*2 + 3*(-2) + 4*1} (volume-preserving)")
    print(f"  G_mod = (1/4)*sum n_I*(d ln g_I/dtau)^2 = (1/4)*{3*4+4*1+1*4} = {G_MOD:.1f}")
    print(f"  G_mod (projected trace-free) = 20/7 = {G_MOD_ALT:.4f}")
    print(f"  G_mod is CONSTANT (tau-independent, because volume-preserving)")

    # ================================================================
    #  SLOW-ROLL ANALYSIS
    # ================================================================
    print(f"\n{'='*78}")
    print(f"Step 3: Slow-Roll Parameters")
    print(f"{'='*78}")

    sr_results = {}
    for pot_label, cs_V in [("S_full", cs_full), ("S_singlet", cs_sing)]:
        for G_label, G_val in [("standard", G_MOD), ("projected", G_MOD_ALT)]:
            key = f"{pot_label}_{G_label}"
            tau_arr, eps, eta, eps_f, eta_f = compute_slow_roll(
                cs_V, G_val, label=f"{pot_label}, {G_label}")
            sr_results[key] = {
                'tau': tau_arr, 'epsilon': eps, 'eta': eta,
                'eps_fold': eps_f, 'eta_fold': eta_f,
            }

    # ================================================================
    #  ANALYTICAL ESTIMATES
    # ================================================================
    print(f"\n{'='*78}")
    print(f"Step 4: Analytical Estimates (Overdamped Terminal Velocity)")
    print(f"{'='*78}")

    an_results = {}
    for pot_label, cs_V in [("S_full", cs_full), ("S_singlet", cs_sing)]:
        an = analytical_estimates(cs_V, G_MOD, label=pot_label)
        an_results[pot_label] = an

    # ================================================================
    #  NUMERICAL TRAJECTORIES
    # ================================================================
    print(f"\n{'='*78}")
    print(f"Step 5: Numerical Trajectories")
    print(f"{'='*78}")

    trajectories = {}

    # --- S_full trajectories ---
    # Timescale: omega ~ 505, T ~ 0.012. With H ~ 587, overdamped.
    # Terminal velocity ~ 27. Transit through 0.030 window ~ 0.001.
    # Use max_step=1e-7 for sub-window resolution.

    for tau0 in [0.50, 0.40, 0.25, 0.21]:
        key = f"S_full_tau0={tau0:.2f}"
        info = solve_trajectory(cs_full, G_MOD, tau0, t_end=0.05,
                               max_step=1e-7, label=key)
        if info is not None:
            trajectories[key] = info

    # S_full with BCS back-reaction
    key_bcs = "S_full_tau0=0.40_BCS"
    info_bcs = solve_trajectory(cs_full, G_MOD, 0.40, t_end=0.05,
                                max_step=1e-7, include_BCS=True,
                                cs_EBCS=cs_EBCS, label=key_bcs)
    if info_bcs is not None:
        trajectories[key_bcs] = info_bcs

    # --- S_singlet trajectories (for comparison) ---
    for tau0 in [0.50, 0.40, 0.25]:
        key = f"S_singlet_tau0={tau0:.2f}"
        info = solve_trajectory(cs_sing, G_MOD, tau0, t_end=5.0,
                               max_step=1e-5, label=key)
        if info is not None:
            trajectories[key] = info

    # S_singlet with BCS back-reaction
    key_sing_bcs = "S_singlet_tau0=0.40_BCS"
    info_sing_bcs = solve_trajectory(cs_sing, G_MOD, 0.40, t_end=5.0,
                                     max_step=1e-5, include_BCS=True,
                                     cs_EBCS=cs_EBCS, label=key_sing_bcs)
    if info_sing_bcs is not None:
        trajectories[key_sing_bcs] = info_sing_bcs

    # ================================================================
    #  ENERGY CONSERVATION CHECK (no-Hubble case)
    # ================================================================
    print(f"\n{'='*78}")
    print(f"Step 6: Energy Conservation Check")
    print(f"{'='*78}")

    def rhs_no_hubble(t, y):
        tau, v = y
        tc = np.clip(tau, 0.0, 0.5)
        dV = cs_full(tc, 1)
        a = -dV / G_MOD
        return [v, a]

    sol_nh = solve_ivp(rhs_no_hubble, (0, 0.02), [0.40, 0.0],
                       method='RK45', max_step=1e-7, rtol=1e-13, atol=1e-15,
                       dense_output=True)
    t_nh = np.linspace(0, sol_nh.t[-1], 100000)
    y_nh = sol_nh.sol(t_nh)
    KE_nh = 0.5 * G_MOD * y_nh[1]**2
    tau_nh = np.clip(y_nh[0], 0.0, 0.5)
    PE_nh = cs_full(tau_nh)
    E_nh = KE_nh + PE_nh
    dE_rel = abs(E_nh[-1] - E_nh[0]) / abs(E_nh[0])
    print(f"  No-Hubble case (tau0=0.40):")
    print(f"    E(0)   = {E_nh[0]:.6f}")
    print(f"    E(end) = {E_nh[-1]:.6f}")
    print(f"    |dE|/E = {dE_rel:.2e}")
    print(f"    Conservation: {'PASS' if dE_rel < 1e-6 else 'MARGINAL'}")

    # Also check: does tau leave [0, 0.5] in the no-Hubble case?
    # If so, the spline extrapolation is unreliable.
    tau_min_nh = np.min(y_nh[0])
    print(f"    tau_min (no clamp) = {tau_min_nh:.6f}")
    print(f"    tau leaves [0,0.5]? {tau_min_nh < 0 or np.max(y_nh[0]) > 0.5}")

    # ================================================================
    #  BCS BACK-REACTION ANALYSIS
    # ================================================================
    print(f"\n{'='*78}")
    print(f"Step 7: BCS Back-Reaction")
    print(f"{'='*78}")

    key_A = "S_full_tau0=0.40"
    key_E = "S_full_tau0=0.40_BCS"
    if key_A in trajectories and key_E in trajectories:
        dt_no = trajectories[key_A]['t_dwell']
        dt_with = trajectories[key_E]['t_dwell']
        v_no = trajectories[key_A]['v_fold']
        v_with = trajectories[key_E]['v_fold']

        print(f"  Without BCS: dwell={dt_no:.6e}, v_fold={v_no:.6f}")
        print(f"  With BCS:    dwell={dt_with:.6e}, v_fold={v_with:.6f}")
        if dt_no > 0:
            print(f"  Enhancement: {dt_with/dt_no:.4f}x")

        # Energy budget
        E_BCS_fold = cs_EBCS(TAU_FOLD)
        dV_fold = cs_full(TAU_FOLD, 1)
        print(f"\n  Energy budget:")
        print(f"    E_BCS(fold)          = {E_BCS_fold:.6f}")
        print(f"    dV/dtau(fold, S_full)= {dV_fold:.1f}")
        print(f"    |E_BCS|/|dV|         = {abs(E_BCS_fold)/abs(dV_fold):.2e}")
        print(f"    BCS gradient max     ~ {abs(E_COND_PEAK)/WINDOW_WIDTH:.2f}")
        print(f"    SA gradient at fold  = {abs(dV_fold):.1f}")
        print(f"    Ratio (BCS/SA grad)  = {abs(E_COND_PEAK)/(WINDOW_WIDTH*abs(dV_fold)):.2e}")

    # ================================================================
    #  COMPREHENSIVE COMPARISON TABLE
    # ================================================================
    print(f"\n{'='*78}")
    print(f"Step 8: Comprehensive Results")
    print(f"{'='*78}")

    print(f"\n  {'Scenario':<35s} {'t_dwell':>12s} {'dwell/BCS':>12s} {'v_fold':>10s}")
    print(f"  {'='*35} {'='*12} {'='*12} {'='*10}")
    for key, info in sorted(trajectories.items()):
        td = info['t_dwell']
        vf = info['v_fold']
        print(f"  {key:<35s} {td:12.6e} {td/TAU_BCS:12.6e} {vf:10.6f}")

    # Analytical comparison
    print(f"\n  {'Source':<35s} {'dt_transit':>12s} {'dt/tau_BCS':>12s}")
    print(f"  {'='*35} {'='*12} {'='*12}")
    for pot_label, an in an_results.items():
        print(f"  {pot_label+' (analytical)':<35s} {an['dt_transit']:12.6e} {an['dt_over_tau_BCS']:12.6e}")

    # ================================================================
    #  GATE VERDICT
    # ================================================================
    print(f"\n{'='*78}")
    print(f"Step 9: GATE VERDICT -- TAU-DYN-36")
    print(f"{'='*78}")

    # Primary scenario: S_full, tau0=0.40
    primary = trajectories.get("S_full_tau0=0.40", {})
    dt_primary = primary.get('t_dwell', 0)
    dwell_ratio = dt_primary / TAU_BCS

    eps_fold = sr_results['S_full_standard']['eps_fold']
    eta_fold = sr_results['S_full_standard']['eta_fold']

    print(f"\n  PRIMARY METRICS:")
    print(f"    G_mod               = {G_MOD:.1f} (constant)")
    print(f"    V_eff(fold)         = {cs_full(TAU_FOLD):.1f}")
    print(f"    dV/dtau(fold)       = {cs_full(TAU_FOLD, 1):.1f}")
    print(f"    d2V/dtau2(fold)     = {cs_full(TAU_FOLD, 2):.1f}")
    print(f"    H(fold)             = {an_results['S_full']['H_fold']:.2f}")
    print(f"    omega(fold)         = {an_results['S_full']['omega_fold']:.2f}")
    print(f"    Damping ratio       = {an_results['S_full']['zeta']:.4f} (overdamped)")
    print(f"    v_terminal          = {an_results['S_full']['v_terminal']:.6f}")
    print(f"    epsilon(fold)       = {eps_fold:.6f}")
    print(f"    eta(fold)           = {eta_fold:.6f}")
    print(f"    tau_BCS             = {TAU_BCS:.1f}")
    print(f"    BCS window          = [{BCS_WINDOW[0]}, {BCS_WINDOW[1]}], width={WINDOW_WIDTH}")
    print(f"    t_dwell (numerical) = {dt_primary:.6e}")
    print(f"    t_dwell/tau_BCS     = {dwell_ratio:.6e}")

    # The key finding: epsilon < 1 (technically slow-roll), but the potential
    # is SO steep that the terminal velocity is ~27, and the BCS window (width 0.030)
    # is traversed in ~1e-3, while tau_BCS = 40. The ratio is ~3e-5.
    # epsilon < 1 is MISLEADING here because epsilon measures V'/V, and V ~ 10^6
    # is enormous. The relevant comparison is dwell time vs BCS timescale.

    if dwell_ratio > 1.0:
        verdict = "PASS"
    elif eps_fold < 1.0 and dwell_ratio > 0.01:
        verdict = "SLOW ROLL (marginal dwell)"
    elif eps_fold < 1.0 and dwell_ratio < 0.01:
        verdict = "FAST ROLL"
        # Explanation: epsilon < 1 is technically "slow roll" but this is misleading.
        # The potential is shallow RELATIVE TO ITS OWN HEIGHT, but the absolute
        # gradient is enormous (233,000). The dwell time is 40,000x too short.
    else:
        verdict = "FAST ROLL"

    print(f"\n  VERDICT: {verdict}")
    print(f"\n  EXPLANATION:")
    print(f"    epsilon(fold) = {eps_fold:.6f} < 1 nominally qualifies as 'slow roll'.")
    print(f"    However, epsilon = (V'/V)^2/(2*G_mod) is small because V ~ 10^6 is huge.")
    print(f"    The ABSOLUTE gradient dV/dtau = {cs_full(TAU_FOLD, 1):.0f} drives the terminal")
    print(f"    velocity to |v| ~ {abs(an_results['S_full']['v_terminal']):.1f}, yielding transit time")
    print(f"    through the BCS window of {an_results['S_full']['dt_transit']:.2e}.")
    print(f"    This is {TAU_BCS/an_results['S_full']['dt_transit']:.0f}x shorter than tau_BCS = {TAU_BCS:.0f}.")
    print(f"    BCS condensation CANNOT activate during the passage.")
    print(f"    BCS back-reaction is negligible: |E_BCS/dV| = {abs(cs_EBCS(TAU_FOLD))/abs(cs_full(TAU_FOLD,1)):.2e}.")

    # Singlet-only comparison
    dt_sing = trajectories.get("S_singlet_tau0=0.40", {}).get('t_dwell', 0)
    print(f"\n  SINGLET-ONLY COMPARISON (hypothetical):")
    print(f"    t_dwell(singlet)     = {dt_sing:.6e}")
    print(f"    t_dwell/tau_BCS      = {dt_sing/TAU_BCS:.6e}")
    print(f"    Still {TAU_BCS/max(dt_sing,1e-15):.0f}x too short even for singlet-only potential.")
    print(f"    Root cause: H ~ sqrt(V/3) generates Hubble friction that locks in")
    print(f"    terminal velocity v_term = -V'/(3*H*G_mod) regardless of V scale.")

    # ================================================================
    #  SAVE DATA
    # ================================================================
    print(f"\nSaving data...")

    save_dict = {
        'G_mod_standard': np.float64(G_MOD),
        'G_mod_projected': np.float64(G_MOD_ALT),
        'tau_BCS': np.float64(TAU_BCS),
        'tau_fold': np.float64(TAU_FOLD),
        'BCS_window_lo': np.float64(BCS_WINDOW[0]),
        'BCS_window_hi': np.float64(BCS_WINDOW[1]),
        'window_width': np.float64(WINDOW_WIDTH),
        'verdict': np.array([verdict]),
    }

    # Slow-roll data
    for key, sr in sr_results.items():
        save_dict[f'sr_{key}_tau'] = sr['tau']
        save_dict[f'sr_{key}_epsilon'] = sr['epsilon']
        save_dict[f'sr_{key}_eta'] = sr['eta']
        save_dict[f'sr_{key}_eps_fold'] = np.float64(sr['eps_fold'])
        save_dict[f'sr_{key}_eta_fold'] = np.float64(sr['eta_fold'])

    # Analytical estimates
    for key, an in an_results.items():
        for ak, av in an.items():
            save_dict[f'an_{key}_{ak}'] = np.float64(av)

    # Trajectory data (main scenarios only, to keep file size reasonable)
    main_keys = ["S_full_tau0=0.40", "S_full_tau0=0.40_BCS",
                 "S_singlet_tau0=0.40", "S_singlet_tau0=0.40_BCS"]
    for key in main_keys:
        if key in trajectories:
            info = trajectories[key]
            sk = key.replace('=', '').replace('.', 'p')
            save_dict[f'traj_{sk}_t'] = info['t'][::10]  # subsample for storage
            save_dict[f'traj_{sk}_tau'] = info['tau'][::10]
            save_dict[f'traj_{sk}_v'] = info['v'][::10]
            save_dict[f'traj_{sk}_t_dwell'] = np.float64(info['t_dwell'])
            save_dict[f'traj_{sk}_v_fold'] = np.float64(info['v_fold'])

    np.savez(os.path.join(SCRIPT_DIR, 's36_tau_dynamics.npz'), **save_dict)
    print(f"  Saved: s36_tau_dynamics.npz")

    # ================================================================
    #  PLOT
    # ================================================================
    print(f"\nGenerating plot...")

    fig = plt.figure(figsize=(16, 16))
    gs = GridSpec(3, 2, figure=fig, hspace=0.38, wspace=0.30)

    # --- Panel 1: Potential landscape ---
    ax1 = fig.add_subplot(gs[0, 0])
    tau_pl = np.linspace(0.001, 0.499, 500)
    ax1.plot(tau_pl, cs_full(tau_pl)/1e6, 'b-', lw=2, label='$S_{full}(\\tau)$')
    ax1r = ax1.twinx()
    ax1r.plot(tau_pl, cs_sing(tau_pl), 'r--', lw=1.5, label='$S_{singlet}(\\tau)$')
    ax1.axvline(TAU_FOLD, color='gray', ls='--', alpha=0.7)
    ax1.axvspan(BCS_WINDOW[0], BCS_WINDOW[1], color='green', alpha=0.12)
    ax1.set_xlabel('$\\tau$', fontsize=12)
    ax1.set_ylabel('$S_{full}$ ($\\times 10^6$)', fontsize=12, color='b')
    ax1r.set_ylabel('$S_{singlet}$', fontsize=12, color='r')
    ax1.set_title('Effective Potential $V_{eff}(\\tau) = S(\\tau)$', fontsize=13)
    ax1.legend(loc='upper left', fontsize=9)
    ax1r.legend(loc='center right', fontsize=9)

    # --- Panel 2: Slow-roll epsilon ---
    ax2 = fig.add_subplot(gs[0, 1])
    sr_sf = sr_results['S_full_standard']
    sr_ss = sr_results['S_singlet_standard']
    ax2.semilogy(sr_sf['tau'], sr_sf['epsilon'], 'b-', lw=2, label='$\\epsilon_{S_{full}}$')
    ax2.semilogy(sr_ss['tau'], sr_ss['epsilon'], 'r--', lw=1.5, label='$\\epsilon_{S_{singlet}}$')
    ax2.axhline(1.0, color='k', ls=':', alpha=0.5, label='$\\epsilon=1$')
    ax2.axvline(TAU_FOLD, color='gray', ls='--', alpha=0.5)
    ax2.axvspan(BCS_WINDOW[0], BCS_WINDOW[1], color='green', alpha=0.12)
    ax2.set_xlabel('$\\tau$', fontsize=12)
    ax2.set_ylabel('$\\epsilon(\\tau)$', fontsize=12)
    ax2.set_title('Slow-Roll $\\epsilon = (V\'/V)^2 / (2 G_{mod})$', fontsize=13)
    ax2.legend(fontsize=9)
    ax2.set_ylim(1e-8, 1)

    # --- Panel 3: S_full trajectories ---
    ax3 = fig.add_subplot(gs[1, 0])
    colors = {'S_full_tau0=0.50': 'green', 'S_full_tau0=0.40': 'blue',
              'S_full_tau0=0.25': 'orange', 'S_full_tau0=0.21': 'red',
              'S_full_tau0=0.40_BCS': 'purple'}
    for key in ['S_full_tau0=0.50', 'S_full_tau0=0.40', 'S_full_tau0=0.25',
                'S_full_tau0=0.21', 'S_full_tau0=0.40_BCS']:
        if key in trajectories:
            info = trajectories[key]
            n = min(5000, len(info['t']))
            idx = np.linspace(0, len(info['t'])-1, n, dtype=int)
            lbl = key.replace('S_full_', '').replace('_BCS', '+BCS')
            ax3.plot(info['t'][idx], info['tau'][idx], color=colors.get(key, 'gray'),
                    lw=1.5, label=lbl)

    ax3.axhline(TAU_FOLD, color='gray', ls='--', alpha=0.7, label='fold')
    ax3.axhspan(BCS_WINDOW[0], BCS_WINDOW[1], color='green', alpha=0.15)
    ax3.set_xlabel('$t$ (spectral action units)', fontsize=12)
    ax3.set_ylabel('$\\tau(t)$', fontsize=12)
    ax3.set_title('$S_{full}$ Trajectories: Rapid Roll', fontsize=13)
    ax3.legend(fontsize=8, ncol=2)
    ax3.set_xlim(0, 0.02)
    ax3.set_ylim(-0.05, 0.55)

    # --- Panel 4: S_singlet trajectories ---
    ax4 = fig.add_subplot(gs[1, 1])
    colors_s = {'S_singlet_tau0=0.50': 'green', 'S_singlet_tau0=0.40': 'blue',
                'S_singlet_tau0=0.25': 'orange', 'S_singlet_tau0=0.40_BCS': 'purple'}
    for key in ['S_singlet_tau0=0.50', 'S_singlet_tau0=0.40',
                'S_singlet_tau0=0.25', 'S_singlet_tau0=0.40_BCS']:
        if key in trajectories:
            info = trajectories[key]
            n = min(5000, len(info['t']))
            idx = np.linspace(0, len(info['t'])-1, n, dtype=int)
            lbl = key.replace('S_singlet_', '').replace('_BCS', '+BCS')
            ax4.plot(info['t'][idx], info['tau'][idx], color=colors_s.get(key, 'gray'),
                    lw=1.5, label=lbl)

    ax4.axhline(TAU_FOLD, color='gray', ls='--', alpha=0.7, label='fold')
    ax4.axhspan(BCS_WINDOW[0], BCS_WINDOW[1], color='green', alpha=0.15)
    ax4.set_xlabel('$t$ (spectral action units)', fontsize=12)
    ax4.set_ylabel('$\\tau(t)$', fontsize=12)
    ax4.set_title('$S_{singlet}$ Trajectories (hypothetical)', fontsize=13)
    ax4.legend(fontsize=8, ncol=2)
    ax4.set_xlim(0, 3.0)
    ax4.set_ylim(-0.05, 0.55)

    # --- Panel 5: Dwell time comparison bar chart ---
    ax5 = fig.add_subplot(gs[2, 0])
    bar_keys = ["S_full_tau0=0.40", "S_full_tau0=0.50",
                "S_full_tau0=0.40_BCS", "S_singlet_tau0=0.40",
                "S_singlet_tau0=0.40_BCS"]
    bar_labels = []
    bar_vals = []
    for k in bar_keys:
        if k in trajectories:
            bar_labels.append(k.replace('S_full_', 'Full ').replace('S_singlet_', 'Sing ')
                             .replace('_BCS', '+BCS').replace('tau0=', ''))
            bar_vals.append(trajectories[k]['t_dwell'])

    if bar_vals:
        x_pos = range(len(bar_labels))
        bars = ax5.bar(x_pos, bar_vals, color=['steelblue', 'green', 'purple', 'salmon', 'plum'])
        ax5.axhline(TAU_BCS, color='red', ls='--', lw=2,
                    label=f'$\\tau_{{BCS}} = {TAU_BCS:.0f}$')
        ax5.set_xticks(x_pos)
        ax5.set_xticklabels(bar_labels, rotation=35, ha='right', fontsize=9)
        ax5.set_ylabel('Dwell time in BCS window', fontsize=12)
        ax5.set_title('Dwell Time vs BCS Formation Time', fontsize=13)
        ax5.legend(fontsize=10)
        ax5.set_yscale('log')
        # Annotate ratios
        for i, (v, l) in enumerate(zip(bar_vals, bar_labels)):
            if v > 0:
                ax5.text(i, v*1.5, f'{v/TAU_BCS:.1e}', ha='center', fontsize=8)

    # --- Panel 6: Phase space (tau, v) for S_full ---
    ax6 = fig.add_subplot(gs[2, 1])
    key_phase = "S_full_tau0=0.40"
    if key_phase in trajectories:
        info = trajectories[key_phase]
        n = min(5000, len(info['t']))
        idx = np.linspace(0, len(info['t'])-1, n, dtype=int)
        ax6.plot(info['tau'][idx], info['v'][idx], 'b-', lw=1.5, label='$S_{full}$, $\\tau_0=0.40$')

    key_phase_s = "S_singlet_tau0=0.40"
    if key_phase_s in trajectories:
        info_s = trajectories[key_phase_s]
        n_s = min(5000, len(info_s['t']))
        idx_s = np.linspace(0, len(info_s['t'])-1, n_s, dtype=int)
        ax6.plot(info_s['tau'][idx_s], info_s['v'][idx_s], 'r--', lw=1.5,
                label='$S_{singlet}$, $\\tau_0=0.40$')

    ax6.axvline(TAU_FOLD, color='gray', ls='--', alpha=0.7)
    ax6.axvspan(BCS_WINDOW[0], BCS_WINDOW[1], color='green', alpha=0.12)
    ax6.set_xlabel('$\\tau$', fontsize=12)
    ax6.set_ylabel('$d\\tau/dt$', fontsize=12)
    ax6.set_title('Phase Space ($\\tau$, $d\\tau/dt$)', fontsize=13)
    ax6.legend(fontsize=9)

    fig.suptitle('TAU-DYN-36: Moduli Trajectory Through the Van Hove Fold\n'
                 'Nazarewicz Nuclear Structure Theorist, Session 36', fontsize=14, fontweight='bold')

    plt.savefig(os.path.join(SCRIPT_DIR, 's36_tau_dynamics.png'), dpi=150, bbox_inches='tight')
    print(f"  Saved: s36_tau_dynamics.png")

    # ================================================================
    #  FINAL REPORT
    # ================================================================
    dt = time.time() - t0_wall
    print(f"\n{'='*78}")
    print(f"TAU-DYN-36 COMPLETE ({dt:.1f}s)")
    print(f"{'='*78}")
    print(f"\n  VERDICT: {verdict}")
    print(f"  t_dwell/tau_BCS = {dwell_ratio:.2e} (need > 1, got {dwell_ratio:.2e})")
    print(f"  Shortfall factor: {TAU_BCS/max(dt_primary, 1e-30):.0f}x")
    print(f"  epsilon(fold) = {eps_fold:.6f} (formally < 1 but misleading)")
    print(f"  Hubble friction drives overdamped terminal velocity |v| ~ {abs(an_results['S_full']['v_terminal']):.1f}")
    print(f"  BCS window traversed in {an_results['S_full']['dt_transit']:.2e} << tau_BCS = {TAU_BCS:.0f}")

    return verdict, dwell_ratio, eps_fold, eta_fold


if __name__ == '__main__':
    main()
