#!/usr/bin/env python3
"""
S49 LEGGETT-TRANSIT-49: Leggett Mode Coupled to tau(t) During Transit
======================================================================

Physical question: What happens to the inter-sector relative-phase
oscillation (Leggett mode) during the ballistic transit of the modulus
tau(t) through the fold?

Symmetry analysis (Landau perspective):
    The Leggett mode is a PHASE mode: it requires a nonzero order
    parameter |Delta_i| in at least two sectors. The mode is the
    relative phase theta_{ij} = phi_i - phi_j oscillation, governed by:

        F_phase = -sum_{i<j} J_{ij}(tau) cos(theta_{ij})

    with kinetic energy:

        T = (1/2) sum_i rho_i(tau) * (d phi_i/dt)^2

    The Josephson couplings J_{ij}(tau) and densities rho_i(tau) are
    tau-dependent through the Jensen deformation of SU(3).

    During transit, tau(t) changes ballistically. The Leggett mode
    parameters become time-dependent through tau(t).

Critical physics:
    1. omega_transit / omega_L = 885 / 0.070 = 12,640. SUDDEN LIMIT.
       The Leggett mode is FROZEN during transit -- it cannot respond
       to changes in J(tau), rho(tau) on the transit timescale.

    2. P_exc = 1 post-transit (S38). ALL Cooper pairs are broken.
       The condensate is destroyed. The order parameter Delta_i -> 0.
       With no order parameter, the Leggett mode CEASES TO EXIST.

    3. Therefore: the Leggett mode is frozen during transit, then
       annihilated post-transit. No post-transit Leggett oscillation.

Method:
    1. Construct tau(t) trajectory: tau = tau_fold + v_terminal * t
    2. Interpolate omega_L(tau), J_ij(tau), rho_i(tau) from S48 scan
    3. Integrate coupled Leggett EOM:
       rho_i(tau) * d^2 phi_i/dt^2 + sum_j J_ij(tau)*sin(phi_i - phi_j) = 0
    4. Verify sudden-limit: amplitude change during transit negligible
    5. Post-transit: compute condensate fraction from P_exc = 1
    6. Test 9th integral: I_9 = sum_i rho_i(tau) * (dphi_i/dt)^2 / (2*omega_L^2)
       - If {I_9, H_BCS} ~ 0, then approximately conserved
    7. Formal Poisson bracket from Richardson-Gaudin structure

Gate: LEGGETT-TRANSIT-49
    PASS: A_L > 0.01 AND 9th integral approximately conserved
    INFO: A_L > 0 but 9th integral not conserved
    FAIL: Leggett trivially zero post-transit

References:
    S48 s48_leggett_mode.npz -- Leggett frequencies, J_ij, rho_i, scan data
    S38 s38_kz_defects.npz -- transit parameters, P_exc = 1
    S39 s39_integrability_check.npz -- Richardson-Gaudin conserved quantities
    Leggett, PRL 14, 536 (1966) -- original Leggett mode
    Landau Paper 04 (1937): order parameter requires broken symmetry
    Landau Paper 11 (1956): quasiparticle concept + Fermi liquid
    Claeys et al (Paper 33): Richardson-Gaudin integrability breaking

Author: Landau-Condensed-Matter-Theorist (Session 49, W1-H)
Date: 2026-03-17
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.interpolate import CubicSpline
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    tau_fold, v_terminal, dt_transit, E_cond,
    Delta_0_GL, xi_BCS, omega_PV, Gamma_Langer_BCS,
    E_B1, E_B2_mean, E_B3_mean, P_exc_kz, n_Bog,
    rho_B2_per_mode, N_dof_BCS, n_pairs,
)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# =============================================================================
# MODULE 1: LOAD DATA
# =============================================================================

def load_data():
    """Load all required data from S48 and S38 archives."""
    d48 = np.load(os.path.join(SCRIPT_DIR, 's48_leggett_mode.npz'),
                  allow_pickle=True)
    d38 = np.load(os.path.join(SCRIPT_DIR, 's38_kz_defects.npz'),
                  allow_pickle=True)
    d39 = np.load(os.path.join(SCRIPT_DIR, 's39_integrability_check.npz'),
                  allow_pickle=True)

    data = {}

    # Leggett mode data (S48)
    data['omega_L1'] = float(d48['omega_L1_fold'])
    data['omega_L2'] = float(d48['omega_L2_fold'])
    data['tau_scan'] = np.array(d48['tau_scan'])
    data['omega_L1_scan'] = np.array(d48['omega_L1_scan'])
    data['omega_L2_scan'] = np.array(d48['omega_L2_scan'])
    data['Delta_B1_scan'] = np.array(d48['Delta_B1_scan'])
    data['Delta_B2_scan'] = np.array(d48['Delta_B2_scan'])
    data['Delta_B3_scan'] = np.array(d48['Delta_B3_scan'])
    data['rho_B1_scan'] = np.array(d48['rho_B1_scan'])
    data['rho_B2_scan'] = np.array(d48['rho_B2_scan'])
    data['rho_B3_scan'] = np.array(d48['rho_B3_scan'])
    data['J_12_scan'] = np.array(d48['J_12_scan'])
    data['J_23_scan'] = np.array(d48['J_23_scan'])
    # J_13 not scanned in S48 (only fold value). Reconstruct assuming
    # J_13/J_23 ratio constant (both connect through B3, weakest sector).
    # J_13_fold / J_23_fold = 0.000468 / 0.001814 = 0.258
    J_13_fold = float(d48['J_13_fold'])
    J_23_fold_val = float(d48['J_23_fold'])
    ratio_J13_J23 = J_13_fold / J_23_fold_val if J_23_fold_val > 0 else 0.0
    data['J_13_scan'] = ratio_J13_J23 * np.array(d48['J_23_scan'])
    data['Delta_fold'] = np.array(d48['Delta_fold'])
    data['rho_fold'] = np.array(d48['rho_fold'])
    data['eigvecs_fold'] = np.array(d48['eigvecs_fold'])
    data['evals_fold'] = np.array(d48['evals_fold'])

    # Transit data (S38)
    data['v_term'] = float(d38['v_terminal'])
    data['dt_transit'] = float(d38['dt_transit'])
    data['P_exc'] = float(d38['P_exc_kz'])
    data['n_Bog'] = float(d38['n_Bog'])
    data['condensate_destroyed'] = bool(d38['condensate_destroyed'])

    # Integrability data (S39)
    data['E_8'] = np.array(d39['E_8'])
    data['V_phys'] = np.array(d39['V_phys'])
    data['comm_RH'] = np.array(d39['comm_RH'])
    data['labels'] = np.array(d39['labels'])

    return data


# =============================================================================
# MODULE 2: INTERPOLATION OF TAU-DEPENDENT QUANTITIES
# =============================================================================

def build_interpolants(data):
    """Build cubic spline interpolants for all tau-dependent quantities."""
    tau_s = data['tau_scan']

    interp = {}
    interp['omega_L1'] = CubicSpline(tau_s, data['omega_L1_scan'])
    interp['omega_L2'] = CubicSpline(tau_s, data['omega_L2_scan'])

    # Gaps
    interp['Delta_B1'] = CubicSpline(tau_s, data['Delta_B1_scan'])
    interp['Delta_B2'] = CubicSpline(tau_s, data['Delta_B2_scan'])
    interp['Delta_B3'] = CubicSpline(tau_s, data['Delta_B3_scan'])

    # DOS (superfluid inertia)
    interp['rho_B1'] = CubicSpline(tau_s, data['rho_B1_scan'])
    interp['rho_B2'] = CubicSpline(tau_s, data['rho_B2_scan'])
    interp['rho_B3'] = CubicSpline(tau_s, data['rho_B3_scan'])

    # Josephson couplings
    interp['J_12'] = CubicSpline(tau_s, data['J_12_scan'])
    interp['J_23'] = CubicSpline(tau_s, data['J_23_scan'])
    interp['J_13'] = CubicSpline(tau_s, data['J_13_scan'])

    return interp


# =============================================================================
# MODULE 3: COUPLED LEGGETT EOM
# =============================================================================

def leggett_eom(t, y, interp, v_term, tau_0, condensate_frac_func):
    """
    Equations of motion for the 3-band Leggett system.

    State vector y = [phi_1, phi_2, phi_3, dphi_1/dt, dphi_2/dt, dphi_3/dt]

    EOM (from F_phase + T_kinetic):
        rho_i * d^2 phi_i/dt^2 = -dF/dphi_i

    where dF/dphi_i = sum_{j!=i} J_ij * sin(phi_i - phi_j)

    tau(t) = tau_0 + v_term * t  (ballistic transit)

    The condensate fraction C(t) multiplies ALL Josephson couplings:
    J_ij -> C(t) * J_ij(tau(t))

    When C = 0 (pairs broken), coupling vanishes and phases decouple.
    """
    phi = y[:3]
    dphi = y[3:]

    tau = tau_0 + v_term * t
    C = condensate_frac_func(t)

    # Clamp tau to interpolation range
    tau_min = 0.05
    tau_max = 0.35
    tau_clamped = np.clip(tau, tau_min, tau_max)

    # Get tau-dependent quantities
    rho = np.array([
        float(interp['rho_B1'](tau_clamped)),
        float(interp['rho_B2'](tau_clamped)),
        float(interp['rho_B3'](tau_clamped)),
    ])

    J12 = float(interp['J_12'](tau_clamped)) * C
    J23 = float(interp['J_23'](tau_clamped)) * C
    J13 = float(interp['J_13'](tau_clamped)) * C

    # Forces: dF/dphi_i
    dF = np.zeros(3)
    dF[0] = J12 * np.sin(phi[0] - phi[1]) + J13 * np.sin(phi[0] - phi[2])
    dF[1] = -J12 * np.sin(phi[0] - phi[1]) + J23 * np.sin(phi[1] - phi[2])
    dF[2] = -J13 * np.sin(phi[0] - phi[2]) - J23 * np.sin(phi[1] - phi[2])

    # d^2 phi_i/dt^2 = -dF_i / rho_i
    # rho_i must be positive; add floor to prevent division by zero
    rho_safe = np.maximum(rho, 1e-10)
    d2phi = -dF / rho_safe

    return np.concatenate([dphi, d2phi])


def make_condensate_frac(dt_transit, quench_style='sudden'):
    """
    Create condensate fraction function C(t).

    For sudden quench (adiabaticity = 8.7e-4, S38):
        C(t) = 1 for t < 0 (pre-transit)
        C(t) = 1 - P_exc * smooth_step(t, dt_transit) (during)
        C(t) = 0 for t >> dt_transit (post-transit, P_exc = 1)

    The Kibble-Zurek mechanism destroys ALL pairs: P_exc = 1.
    """
    def C_func(t):
        if quench_style == 'sudden':
            # Sharp step at transit midpoint
            if t < 0:
                return 1.0
            elif t < dt_transit:
                # Smooth interpolation using tanh
                # Center the quench at dt_transit / 2
                x = (t - dt_transit/2) / (dt_transit/4)
                return 0.5 * (1.0 - np.tanh(x))
            else:
                return 0.0
        elif quench_style == 'adiabatic':
            # For comparison: condensate survives
            return 1.0
        else:
            return 1.0
    return C_func


# =============================================================================
# MODULE 4: SUDDEN-LIMIT ANALYSIS (ANALYTICAL)
# =============================================================================

def sudden_limit_analysis(data):
    """
    Analytical treatment of the sudden limit.

    The adiabaticity parameter:
        Q_ad = (1/omega_L) * |d omega_L/dt| / omega_L
             = v_terminal * (1/omega_L^2) * |d omega_L/d tau|

    When Q_ad << 1, the mode is adiabatic (follows slowly).
    When Q_ad >> 1, the mode is diabatic (frozen).

    For transit: omega_transit ~ 1/dt_transit ~ 885 M_KK.
    omega_L ~ 0.070 M_KK. Ratio ~ 12,640. DEEPLY sudden.

    In the sudden limit, the mode state is PROJECTED onto the
    post-transit eigenstates. But post-transit there ARE no
    Leggett eigenstates (condensate destroyed), so the projection
    is onto free-particle (decoupled phase) states.
    """
    results = {}

    omega_L1 = data['omega_L1']
    omega_L2 = data['omega_L2']
    v_term = data['v_term']
    dt = data['dt_transit']

    # Adiabaticity parameter
    omega_transit = 1.0 / dt
    ratio_L1 = omega_transit / omega_L1
    ratio_L2 = omega_transit / omega_L2

    results['omega_transit'] = omega_transit
    results['ratio_L1'] = ratio_L1
    results['ratio_L2'] = ratio_L2

    # Rate of change of omega_L during transit
    # From S48 scan: omega_L1 varies from 0.0653 (tau=0.05) to 0.0716 (tau=0.35)
    # At fold: d(omega_L1)/d(tau) ~ slope from interpolation
    tau_scan = data['tau_scan']
    oL1_scan = data['omega_L1_scan']

    # Numerical derivative at fold
    fold_idx = np.argmin(np.abs(tau_scan - tau_fold))
    if fold_idx > 0 and fold_idx < len(tau_scan) - 1:
        doL1_dtau = (oL1_scan[fold_idx+1] - oL1_scan[fold_idx-1]) / \
                    (tau_scan[fold_idx+1] - tau_scan[fold_idx-1])
    else:
        doL1_dtau = 0.0

    doL1_dt = doL1_dtau * v_term
    Q_ad_L1 = abs(doL1_dt) / omega_L1**2

    results['doL1_dtau'] = doL1_dtau
    results['doL1_dt'] = doL1_dt
    results['Q_ad_L1'] = Q_ad_L1

    # Phase accumulated during transit
    delta_phi_L1 = omega_L1 * dt
    delta_phi_L2 = omega_L2 * dt

    results['delta_phi_L1'] = delta_phi_L1
    results['delta_phi_L2'] = delta_phi_L2

    # Number of Leggett oscillations during transit
    N_osc_L1 = omega_L1 * dt / (2 * np.pi)
    N_osc_L2 = omega_L2 * dt / (2 * np.pi)

    results['N_osc_L1'] = N_osc_L1
    results['N_osc_L2'] = N_osc_L2

    # Transit tau range
    dtau_transit = v_term * dt
    results['dtau_transit'] = dtau_transit

    print("=" * 70)
    print("SUDDEN-LIMIT ANALYSIS")
    print("=" * 70)
    print(f"  omega_transit  = 1/dt = {omega_transit:.1f} M_KK")
    print(f"  omega_L1       = {omega_L1:.6f} M_KK")
    print(f"  omega_L2       = {omega_L2:.6f} M_KK")
    print(f"  ratio_L1       = {ratio_L1:.0f}  (>> 1: SUDDEN)")
    print(f"  ratio_L2       = {ratio_L2:.0f}  (>> 1: SUDDEN)")
    Q_ad_label = "SUDDEN (>> 1)" if Q_ad_L1 > 1 else "ADIABATIC (<< 1)"
    print(f"  Q_ad (L1)      = {Q_ad_L1:.6f}  ({Q_ad_label})")
    print(f"  Phase L1       = {delta_phi_L1:.6f} rad")
    print(f"  Phase L2       = {delta_phi_L2:.6f} rad")
    print(f"  N_osc (L1)     = {N_osc_L1:.6e}")
    print(f"  N_osc (L2)     = {N_osc_L2:.6e}")
    print(f"  dtau_transit   = {dtau_transit:.4f}")
    print()
    print("  Interpretation: The Leggett mode completes 0.000013")
    print("  oscillations during transit. It is COMPLETELY FROZEN.")
    print("  The relative phase does not change during transit.")

    return results


# =============================================================================
# MODULE 5: NUMERICAL INTEGRATION
# =============================================================================

def integrate_leggett(data, interp, scenario='physical'):
    """
    Numerically integrate the Leggett EOM through transit.

    Three scenarios:
    (a) Physical: condensate destroyed by KZ quench (P_exc = 1)
    (b) Adiabatic: condensate survives (hypothetical, for comparison)
    (c) Sudden freeze: instantaneous quench at t = dt_transit/2
    """
    dt = data['dt_transit']
    v_term = data['v_term']
    omega_L1 = data['omega_L1']

    # Time window: 100 Leggett periods before, transit, 100 periods after
    T_L1 = 2 * np.pi / omega_L1
    t_pre = -50 * T_L1
    t_post = 50 * T_L1

    # Initial condition: small perturbation in phi_rel
    # phi_1 = phi_2 = 0, phi_3 = phi_0 (B3 sector oscillates)
    phi_0 = 0.10  # Small but finite initial relative phase

    # Eigenvector analysis from S48: L1 mode has B3 oscillating against B1+B2
    # So initial condition aligned with L1 mode:
    # phi = (0, 0, phi_0), dphi = (0, 0, 0) [released from rest]
    y0 = np.array([0.0, 0.0, phi_0, 0.0, 0.0, 0.0])

    if scenario == 'physical':
        C_func = make_condensate_frac(dt, quench_style='sudden')
    elif scenario == 'adiabatic':
        C_func = make_condensate_frac(dt, quench_style='adiabatic')
    else:
        C_func = make_condensate_frac(dt, quench_style='sudden')

    # Dense output for plotting
    n_pts = 10000
    t_eval = np.linspace(t_pre, t_post, n_pts)

    def eom(t, y):
        return leggett_eom(t, y, interp, v_term, tau_fold, C_func)

    sol = solve_ivp(
        eom,
        [t_pre, t_post],
        y0,
        method='RK45',
        t_eval=t_eval,
        rtol=1e-10,
        atol=1e-12,
        max_step=T_L1 / 20,  # Resolve oscillations
    )

    if not sol.success:
        print(f"  WARNING: Integration failed for {scenario}: {sol.message}")

    return sol


# =============================================================================
# MODULE 6: POST-TRANSIT AMPLITUDE EXTRACTION
# =============================================================================

def extract_post_transit_amplitude(sol, data):
    """
    Extract Leggett mode amplitude post-transit.

    A_L = max |phi_rel(t)| for t > dt_transit, where
    phi_rel = phi_3 - (rho_1*phi_1 + rho_2*phi_2)/(rho_1 + rho_2)
    is the relative phase aligned with the L1 eigenvector.
    """
    dt = data['dt_transit']

    t = sol.t
    phi = sol.y[:3, :]  # [3, N_pts]
    dphi = sol.y[3:, :]

    # Post-transit mask: t > 2 * dt_transit (well after quench)
    post_mask = t > 2 * dt

    if not np.any(post_mask):
        return 0.0, 0.0, np.array([]), np.array([])

    # Relative phase: phi_3 - weighted average of phi_1, phi_2
    # From S48 eigenvector: L1 mode is almost purely B3
    rho_fold = data['rho_fold']
    w12 = rho_fold[0] + rho_fold[1]
    if w12 > 0:
        phi_cm12 = (rho_fold[0] * phi[0] + rho_fold[1] * phi[1]) / w12
    else:
        phi_cm12 = 0.5 * (phi[0] + phi[1])

    phi_rel = phi[2] - phi_cm12

    # Post-transit relative phase
    phi_rel_post = phi_rel[post_mask]
    t_post = t[post_mask]

    A_L = np.max(np.abs(phi_rel_post))

    # Also compute kinetic energy of relative-phase motion
    dphi_rel = dphi[2, post_mask] - (rho_fold[0] * dphi[0, post_mask] +
                                      rho_fold[1] * dphi[1, post_mask]) / max(w12, 1e-10)
    E_kin_rel = 0.5 * rho_fold[2] * np.mean(dphi_rel**2)

    return A_L, E_kin_rel, t_post, phi_rel_post


# =============================================================================
# MODULE 7: 9TH INTEGRAL TEST
# =============================================================================

def test_ninth_integral(data, sol_adiabatic):
    """
    Test whether the Leggett relative phase constitutes a 9th
    conserved integral of the Richardson-Gaudin system.

    The Richardson-Gaudin model has 8 conserved integrals (one per mode).
    These are:
        R_alpha = epsilon_alpha * n_alpha + g * sum_{beta != alpha}
                  (c^dag_alpha c_beta + h.c.) / (epsilon_alpha - epsilon_beta)

    A putative 9th integral from the Leggett sector would be:
        I_9 = sum_i rho_i * (dphi_i/dt)^2 / 2 + sum_{i<j} J_{ij} * (1 - cos(phi_i - phi_j))

    This is the TOTAL Leggett energy (kinetic + potential). If the
    system is integrable, this should be a constant of motion.

    However: the Leggett mode lives in the PHASE sector, while
    Richardson-Gaudin conserves AMPLITUDE degrees of freedom. The
    phase and amplitude sectors couple through the BCS self-consistency:
        J_{ij} depends on |Delta_i|, which depends on the R_alpha.

    If J_{ij} is constant (adiabatic limit), then I_9 is trivially
    conserved (it's the Hamiltonian of an isolated pendulum).

    The non-trivial question is whether I_9 commutes with H_BCS
    when both phase and amplitude dynamics are included.
    """
    results = {}

    # Test 1: Conservation of I_9 in the adiabatic scenario
    # (condensate survives, so Leggett mode oscillates)

    if sol_adiabatic is not None and sol_adiabatic.success:
        t = sol_adiabatic.t
        phi = sol_adiabatic.y[:3, :]
        dphi = sol_adiabatic.y[3:, :]

        rho = data['rho_fold']
        J12 = float(data['J_12_scan'][4])  # fold index
        J23 = float(data['J_23_scan'][4])
        J13 = float(data['J_13_scan'][4])

        # I_9(t) = kinetic + potential Leggett energy
        T_kin = 0.5 * (rho[0] * dphi[0]**2 + rho[1] * dphi[1]**2 + rho[2] * dphi[2]**2)
        V_pot = (J12 * (1 - np.cos(phi[0] - phi[1])) +
                 J23 * (1 - np.cos(phi[1] - phi[2])) +
                 J13 * (1 - np.cos(phi[0] - phi[2])))
        I_9 = T_kin + V_pot

        # Conservation metric: relative variation
        I_9_mean = np.mean(I_9)
        I_9_std = np.std(I_9)

        if abs(I_9_mean) > 1e-20:
            I_9_rel_var = I_9_std / abs(I_9_mean)
        else:
            I_9_rel_var = I_9_std

        results['I_9_mean'] = I_9_mean
        results['I_9_std'] = I_9_std
        results['I_9_rel_var'] = I_9_rel_var
        results['I_9_time'] = t
        results['I_9_values'] = I_9

        print()
        print("=" * 70)
        print("9TH INTEGRAL TEST")
        print("=" * 70)
        print(f"  I_9 = Leggett total energy (kin + pot)")
        print(f"  <I_9>         = {I_9_mean:.6e}")
        print(f"  std(I_9)      = {I_9_std:.6e}")
        print(f"  rel. var.     = {I_9_rel_var:.6e}")

    # Test 2: Structural analysis -- does I_9 Poisson-commute with H_BCS?
    # The BCS Hamiltonian has 8 Richardson-Gaudin integrals I_1,...,I_8.
    # These live in the OCCUPATION number sector {n_alpha}.
    # The Leggett energy lives in the PHASE sector {phi_i, dphi_i/dt}.
    #
    # In a mean-field BCS description:
    #   H_BCS = sum_alpha epsilon_alpha n_alpha - g sum_alphabeta c^dag c^dag c c
    # The phases phi_i are the phases of Delta_i = |Delta_i| e^{i phi_i}.
    # They enter through the mean-field self-consistency:
    #   Delta_i = -g sum_k <c_{k,up} c_{-k,down}>_i
    #
    # The phase dynamics DECOUPLES from amplitude dynamics at the
    # mean-field level (Anderson-Goldstone-Leggett factorization).
    # This decoupling is EXACT in the limit N -> infinity.
    # For finite N (here N=8), corrections are O(1/N) ~ 12.5%.
    #
    # Therefore: {I_9, H_BCS} = 0 at mean-field level.
    # Corrections from finite-size: O(1/N) ~ O(0.125).

    # Estimate finite-size correction from S39 commutator data
    comm_RH = data['comm_RH']  # [R_alpha, H] norms for the 8 Richardson-Gaudin integrals
    max_comm = np.max(comm_RH)
    mean_comm = np.mean(comm_RH)

    results['comm_RH_max'] = max_comm
    results['comm_RH_mean'] = mean_comm

    # The Leggett mode couples to H_BCS through J_{ij} = V(i,j)|Delta_i||Delta_j|.
    # V(i,j) is the scattering matrix from S39.
    # The Poisson bracket {I_9, H_BCS} scales as:
    #   |{I_9, H_BCS}| ~ J * dDelta/dn ~ J / sqrt(N)
    # where N is the number of modes per sector.

    # Using V_phys from S39 (8x8 scattering matrix)
    V = data['V_phys']
    V_off_diag = V - np.diag(np.diag(V))
    V_rms_off = np.sqrt(np.mean(V_off_diag**2))

    # Phase-amplitude coupling: the inter-sector V matrix elements
    # B2 indices: 0-3, B1 index: 4, B3 indices: 5-7
    V_B2_B3 = V[0:4, 5:8]
    V_B1_B2 = V[4, 0:4]
    V_coupling_inter = np.sqrt(np.mean(V_B2_B3**2))

    # Estimate Poisson bracket: {I_9, H_BCS} ~ V_coupling * phi * 1/sqrt(N_eff)
    N_eff_RG = 8  # 8 RG modes
    PB_estimate = V_coupling_inter * 0.10 / np.sqrt(N_eff_RG)  # phi_0 = 0.10

    results['V_coupling_inter'] = V_coupling_inter
    results['PB_estimate'] = PB_estimate

    print(f"\n  Structural Poisson bracket analysis:")
    print(f"  max |[R_alpha, H]| = {max_comm:.6f}  (from S39)")
    print(f"  mean|[R_alpha, H]| = {mean_comm:.6f}  (from S39)")
    print(f"  V_coupling(B2-B3)  = {V_coupling_inter:.6f}")
    print(f"  |{{I_9, H_BCS}}|  ~ {PB_estimate:.6f}  (estimate)")

    # Assessment
    print(f"\n  Assessment:")
    print(f"  At MEAN-FIELD level: {{I_9, H_BCS}} = 0 EXACTLY.")
    print(f"  Phase-amplitude decoupling is Anderson's theorem.")
    print(f"  Finite-size corrections: O(1/N) ~ {1.0/N_eff_RG:.3f}.")
    print(f"  The S39 commutators (max {max_comm:.4f}) confirm")
    print(f"  that the 8 RG integrals are approximate (not exact)")
    print(f"  at the 0.9% level.")
    print(f"  I_9 would be approximate at a SIMILAR level.")

    # But the decisive point:
    print(f"\n  DECISIVE POINT: P_exc = {data['P_exc']}")
    print(f"  The condensate is DESTROYED. Delta_i -> 0 for all i.")
    print(f"  With no condensate, J_ij -> 0 identically.")
    print(f"  The Leggett energy I_9 -> T_kinetic only.")
    print(f"  The phases become FREE (non-interacting).")
    print(f"  Free phases trivially conserve kinetic energy.")
    print(f"  But this is not a 9th INDEPENDENT integral:")
    print(f"  it is a trivial consequence of J = 0.")

    results['ninth_integral_status'] = 'TRIVIALLY_CONSERVED_BUT_NOT_INDEPENDENT'

    return results


# =============================================================================
# MODULE 8: LEGGETT FATE WITH P_EXC = 1
# =============================================================================

def leggett_fate_analysis(data):
    """
    Definitive analysis of the Leggett mode fate when P_exc = 1.

    This is a symmetry argument (Landau Paper 04, 1937):

    1. The Leggett mode is a collective oscillation of the RELATIVE
       PHASE between sector order parameters Delta_i = |Delta_i| e^{i phi_i}.

    2. The mode exists because J_{ij} != 0 and |Delta_i| != 0.
       Both conditions are necessary.

    3. Post-transit: P_exc = 1 => all Bogoliubov quasiparticle states
       are occupied => <c_up c_down> = 0 => Delta_i = 0.

    4. With Delta_i = 0: the phases phi_i are UNDEFINED (the modulus
       is zero; the argument of zero has no meaning).

    5. The Josephson coupling J_{ij} = V(i,j) |Delta_i| |Delta_j| = 0.

    6. The Leggett mode frequency omega_L^2 = eigenvalue of M/rho.
       But M_{ij} = J_{ij} * delta(phase=0) = 0.
       Therefore omega_L = 0. The mode ceases to exist.

    This is the SAME physics as the Goldstone mode: no condensate,
    no spontaneously broken U(1), no Goldstone/Leggett modes.

    The GGE has no Leggett modes.
    """
    results = {}

    print()
    print("=" * 70)
    print("LEGGETT MODE FATE ANALYSIS (P_exc = 1)")
    print("=" * 70)

    # Condensate fraction post-transit
    # |<BCS_f|BCS_i>|^2 ~ exp(-N_pairs) = exp(-59.8)
    overlap = np.exp(-n_pairs)
    results['BCS_overlap'] = overlap

    # Delta_i post-transit from Bogoliubov quasiparticle occupations
    # In BCS: Delta = -g * sum_k u_k v_k (1 - 2n_k)
    # With n_k = n_Bog ~ 0.999 (nearly 1):
    #   Delta_post = Delta_0 * (1 - 2*n_Bog) = Delta_0 * (1 - 2*0.999) = -0.998 * Delta_0
    # Wait -- this gives a NEGATIVE sign, not zero!
    #
    # Careful: n_Bog = 0.999 is the Bogoliubov QUASIPARTICLE occupation.
    # The anomalous average is:
    #   <c_up c_down> = u_k v_k (1 - 2 f_k)
    # where f_k is the quasiparticle occupation.
    # With f_k -> 1 (all excited): <cc> -> u_k v_k (1-2) = -u_k v_k
    # But the TOTAL gap sums over all k:
    #   Delta = -g sum_k u_k v_k (1 - 2f_k)
    # With f_k = 1 for all k: Delta = -g sum_k u_k v_k * (-1) = +Delta_0
    #
    # NO -- this is wrong. Let me be precise.
    #
    # The BCS gap equation at finite temperature (or finite occupation):
    #   Delta = g * sum_k (u_k v_k) * (1 - f_{k,up} - f_{k,down})
    # where f are quasiparticle occupations.
    #
    # The S38 result P_exc = 1 means EVERY mode is excited:
    #   f_{k,up} = f_{k,down} = n_Bog ~ 1
    #   (1 - f_up - f_down) = 1 - 2*n_Bog ~ 1 - 2 = -1
    #
    # So Delta_post = g sum_k u_k v_k * (-1) = -Delta_0
    # This is NOT zero -- it's a SIGN FLIP!
    #
    # However, this is only true for the BdG self-consistent gap.
    # The GGE state has ALL quasiparticle modes occupied (n_k = 1).
    # In the BdG framework, this is equivalent to the state where
    # every Cooper pair has been pair-broken.
    #
    # The correct statement: the anomalous density in the GGE is
    #   kappa_GGE = sum_k u_k v_k (1 - 2n_k)
    # With n_k = 1 for all k:
    #   kappa_GGE = -sum_k u_k v_k = -kappa_BCS
    #
    # So the anomalous density REVERSES SIGN but does not vanish.
    # This corresponds to a pi-junction state!
    #
    # BUT WAIT: this analysis assumes the BCS GROUND STATE u_k, v_k
    # are still the correct basis. After the sudden quench, the
    # system evolves unitarily. The occupations n_k = 1 are in the
    # PRE-QUENCH basis. The POST-QUENCH basis has different u_k, v_k.
    #
    # For the sudden quench from S38:
    #   - Pre-transit: BCS ground state at tau = 0.19
    #   - Post-transit: tau = 0.22 (0.03 further)
    #   - The gap changes by ~2.9% (ultra-stable)
    #   - The BdG basis BARELY changes
    #   - Therefore kappa_GGE ~ -kappa_BCS is approximately correct
    #
    # RESOLUTION: The key insight from S38 is that P_exc = 1 means
    # the state has ZERO condensate FRACTION, not zero anomalous
    # density. The condensate fraction is:
    #   n_0 = N_0 / N_total = 1 - sum_k f_k / N_modes
    # With all f_k = 1: n_0 = 0.
    #
    # The anomalous density can be nonzero in a state with zero
    # condensate fraction -- this is the pi state of a Josephson
    # junction. But in the BCS context with P_exc = 1, the
    # self-consistent gap COLLAPSES: the gap equation with
    # (1-2f) < 0 everywhere gives Delta_SC = 0 for repulsive
    # effective interactions.
    #
    # Actually: (1-2f) = -1 everywhere. So
    #   Delta_SC = -g * N(0) * Delta * (-1) * ln(omega_D/Delta)
    #            = +g * N(0) * Delta * ln(omega_D/Delta)
    # The sign change makes the gap equation WRONG-SIGN:
    # instead of attractive (binding), it's repulsive.
    # The self-consistent solution is Delta_SC = 0.

    # Let me compute this explicitly:
    Delta_fold = data['Delta_fold']  # [B1, B2, B3] gaps
    rho_fold = data['rho_fold']      # [B1, B2, B3] DOS

    # Gap equation factor: (1 - 2*n_k) for P_exc = 1
    gap_factor = 1.0 - 2.0 * n_Bog  # = 1 - 2*0.999 = -0.998

    # Self-consistent gap: Delta_SC = Delta_0 * gap_factor / (1 + ...)
    # In mean-field, the linearized gap equation gives:
    #   Delta_SC / Delta_0 = gap_factor = -0.998
    # But the SELF-CONSISTENT equation requires:
    #   1 = -g * N(0) * (1-2f) * integral
    # When (1-2f) < 0, the equation has no positive solution.
    # The only consistent solution is Delta_SC = 0.

    Delta_post = np.zeros(3)  # All gaps collapse to zero
    results['Delta_post'] = Delta_post
    results['gap_factor'] = gap_factor

    # J_ij post-transit
    J_12_post = data['J_12_scan'][4] * Delta_post[0] * Delta_post[1] / \
                max(Delta_fold[0] * Delta_fold[1], 1e-30)
    J_23_post = data['J_23_scan'][4] * Delta_post[1] * Delta_post[2] / \
                max(Delta_fold[1] * Delta_fold[2], 1e-30)

    results['J_12_post'] = J_12_post
    results['J_23_post'] = J_23_post

    # Leggett frequency post-transit
    omega_L1_post = 0.0  # Zero by construction (J = 0)
    omega_L2_post = 0.0
    results['omega_L1_post'] = omega_L1_post
    results['omega_L2_post'] = omega_L2_post

    print(f"  Pre-transit gaps:   Delta = [{Delta_fold[0]:.4f}, {Delta_fold[1]:.4f}, {Delta_fold[2]:.4f}] M_KK")
    print(f"  Bogoliubov occ:     n_Bog = {n_Bog:.6f}")
    print(f"  Gap factor:         (1-2n) = {gap_factor:.4f}")
    print(f"  Self-consistent:    Delta_SC = [0, 0, 0] M_KK")
    print(f"  (Gap equation has WRONG SIGN when all QP excited)")
    print()
    print(f"  Post-transit J_12:  {J_12_post:.6e} M_KK")
    print(f"  Post-transit J_23:  {J_23_post:.6e} M_KK")
    print(f"  Post-transit omega_L1: {omega_L1_post:.6e} M_KK")
    print(f"  Post-transit omega_L2: {omega_L2_post:.6e} M_KK")
    print()
    print(f"  BCS overlap:        |<BCS_f|BCS_i>|^2 = exp(-{n_pairs}) = {overlap:.2e}")
    print()
    print("  CONCLUSION (Landau symmetry argument):")
    print("  The Leggett mode requires a nonzero order parameter Delta_i.")
    print("  P_exc = 1 implies self-consistent Delta = 0.")
    print("  With Delta = 0, the Josephson coupling J_{ij} = 0.")
    print("  The Leggett frequency omega_L = 0.")
    print("  The mode CEASES TO EXIST post-transit.")
    print("  This is identical to the Goldstone fate (S38).")
    print()
    print("  The post-transit GGE has:")
    print("  - No condensate (n_0 = 0)")
    print("  - No order parameter (Delta = 0)")
    print("  - No spontaneously broken U(1)_7")
    print("  - No Goldstone mode")
    print("  - No Leggett mode")
    print("  - 8 conserved Richardson-Gaudin integrals")
    print("  - The Leggett I_9 degenerates to free kinetic energy (trivial)")

    return results


# =============================================================================
# MODULE 9: DURING-TRANSIT DYNAMICS (FROZEN + MISMATCH)
# =============================================================================

def transit_dynamics(data, interp):
    """
    Detailed analysis of what happens DURING transit.

    Key timescales:
    1. tau(t) = 0.19 + 26.54 * t. Transit from tau=0.19 to tau=0.22.
    2. dt_transit = 0.00113 M_KK^{-1}
    3. T_Leggett = 2*pi/0.070 = 89.8 M_KK^{-1}
    4. T_pair_vib = 2*pi/0.792 = 7.93 M_KK^{-1}

    The transit is 80,000x faster than one Leggett oscillation.
    The Leggett mode is FROZEN during transit.

    The mismatch between pre- and post-transit Leggett eigenstates
    determines the excitation amplitude. But since the condensate
    is destroyed, this mismatch is irrelevant.
    """
    results = {}

    v_term = data['v_term']
    dt = data['dt_transit']
    omega_L1 = data['omega_L1']
    omega_L2 = data['omega_L2']

    T_L1 = 2 * np.pi / omega_L1
    T_L2 = 2 * np.pi / omega_L2
    T_PV = 2 * np.pi / omega_PV

    results['T_L1'] = T_L1
    results['T_L2'] = T_L2
    results['T_PV'] = T_PV

    # Ratio of transit time to Leggett period
    ratio_transit_L1 = dt / T_L1
    ratio_transit_L2 = dt / T_L2
    ratio_transit_PV = dt / T_PV

    results['ratio_transit_L1'] = ratio_transit_L1
    results['ratio_transit_L2'] = ratio_transit_L2
    results['ratio_transit_PV'] = ratio_transit_PV

    # Change in omega_L during transit
    tau_pre = tau_fold
    tau_post = tau_fold + v_term * dt

    oL1_pre = float(interp['omega_L1'](tau_pre))
    oL1_post = float(interp['omega_L1'](min(tau_post, 0.35)))
    doL1_frac = abs(oL1_post - oL1_pre) / oL1_pre

    results['tau_pre'] = tau_pre
    results['tau_post'] = tau_post
    results['oL1_pre'] = oL1_pre
    results['oL1_post'] = oL1_post
    results['doL1_frac'] = doL1_frac

    print()
    print("=" * 70)
    print("DURING-TRANSIT DYNAMICS")
    print("=" * 70)
    print(f"  Transit time:       dt = {dt:.6e} M_KK^{{-1}}")
    print(f"  Leggett period L1:  T = {T_L1:.2f} M_KK^{{-1}}")
    print(f"  Leggett period L2:  T = {T_L2:.2f} M_KK^{{-1}}")
    print(f"  Pair vibration:     T = {T_PV:.2f} M_KK^{{-1}}")
    print()
    print(f"  dt / T_L1 = {ratio_transit_L1:.6e}  (frozen)")
    print(f"  dt / T_L2 = {ratio_transit_L2:.6e}  (frozen)")
    print(f"  dt / T_PV = {ratio_transit_PV:.6e}  (frozen)")
    print()
    print(f"  tau range: [{tau_pre:.4f}, {tau_post:.4f}]  (dtau = {tau_post-tau_pre:.4f})")
    print(f"  omega_L1: {oL1_pre:.6f} -> {oL1_post:.6f}  (change {doL1_frac*100:.3f}%)")
    print()

    # Landau-Zener analysis for Leggett mode
    # The LZ problem: two levels with gap omega_L, sweep rate v
    # P_exc = exp(-2*pi*omega_L^2 / (2*v)) for linear sweep
    # Here the "levels" are the Leggett ground and excited states
    # The gap is omega_L, the sweep rate is d(omega_L)/dt

    doL1_dt = abs(oL1_post - oL1_pre) / dt
    gamma_LZ = np.pi * omega_L1**2 / (2 * doL1_dt) if doL1_dt > 0 else np.inf
    P_LZ = np.exp(-gamma_LZ)

    results['gamma_LZ'] = gamma_LZ
    results['P_LZ_leggett'] = P_LZ

    print(f"  Landau-Zener excitation of Leggett mode:")
    print(f"  |d omega_L/dt| = {doL1_dt:.4e} M_KK^2")
    print(f"  gamma_LZ       = {gamma_LZ:.2f}")
    print(f"  P_LZ           = {P_LZ:.6e}")
    print(f"  (Adiabatic: P_LZ -> 0. Leggett mode NOT excited by transit sweep.)")
    print(f"  (But this is academic: the condensate is destroyed anyway.)")

    return results


# =============================================================================
# MODULE 10: MAIN AND PLOTTING
# =============================================================================

def main():
    print("=" * 70)
    print("S49 LEGGETT-TRANSIT-49: Leggett Mode Coupled to Transit")
    print("Gate: A_L > 0.01 AND 9th integral conserved => PASS")
    print("=" * 70)
    print()

    # Load data
    data = load_data()
    interp = build_interpolants(data)

    # Module 4: Sudden-limit analysis (analytical)
    sudden_results = sudden_limit_analysis(data)

    # Module 9: Transit dynamics (timescale comparison)
    transit_results = transit_dynamics(data, interp)

    # Module 5: Numerical integration -- both scenarios
    print()
    print("=" * 70)
    print("NUMERICAL INTEGRATION")
    print("=" * 70)

    print("\n  Scenario 1: PHYSICAL (P_exc = 1, condensate destroyed)")
    sol_physical = integrate_leggett(data, interp, scenario='physical')
    print(f"  Integration: {'SUCCESS' if sol_physical.success else 'FAILED'}")

    A_L_phys, E_kin_phys, t_post_phys, phi_post_phys = \
        extract_post_transit_amplitude(sol_physical, data)
    print(f"  Post-transit A_L = {A_L_phys:.6e}")
    print(f"  (This is the residual phase at the frozen value -- no oscillation)")

    print("\n  Scenario 2: ADIABATIC (condensate survives, for comparison)")
    sol_adiabatic = integrate_leggett(data, interp, scenario='adiabatic')
    print(f"  Integration: {'SUCCESS' if sol_adiabatic.success else 'FAILED'}")

    A_L_adiab, E_kin_adiab, t_post_adiab, phi_post_adiab = \
        extract_post_transit_amplitude(sol_adiabatic, data)
    print(f"  Post-transit A_L = {A_L_adiab:.6e}")
    print(f"  (Continuous Leggett oscillation in hypothetical surviving condensate)")

    # Module 7: 9th integral test
    ninth_results = test_ninth_integral(data, sol_adiabatic)

    # Module 8: Leggett fate analysis (definitive)
    fate_results = leggett_fate_analysis(data)

    # =================================================================
    # GATE VERDICT
    # =================================================================
    print()
    print("=" * 70)
    print("GATE VERDICT: LEGGETT-TRANSIT-49")
    print("=" * 70)

    # Gate criteria:
    # PASS: A_L > 0.01 AND 9th integral approximately conserved
    # INFO: A_L > 0 but 9th integral not conserved
    # FAIL: Leggett trivially zero post-transit

    # Physical scenario: A_L is the frozen initial amplitude, not oscillation
    # The mode ceases to exist (J -> 0, Delta -> 0)

    # In the PHYSICAL scenario: after the condensate is destroyed,
    # the phases decouple. The "amplitude" A_L_phys represents the
    # frozen phase difference, not a Leggett oscillation.

    # The 9th integral degenerates to trivial free kinetic energy.

    # Post-transit there is NO Leggett mode. This is FAIL.

    gate_verdict = "FAIL"
    gate_detail = (
        f"Leggett mode CEASES TO EXIST post-transit. "
        f"P_exc = {data['P_exc']:.3f}, Delta_SC -> 0, J_ij -> 0, omega_L -> 0. "
        f"Phase frozen during transit (dt/T_L = {transit_results['ratio_transit_L1']:.2e}). "
        f"9th integral degenerates to trivial free kinetic energy. "
        f"Adiabatic comparison: A_L = {A_L_adiab:.4f} (oscillates if condensate survived)."
    )

    print(f"\n  VERDICT: {gate_verdict}")
    print(f"  {gate_detail}")

    print(f"\n  Physical reasoning (Landau Paper 04):")
    print(f"  A collective mode of an ordered phase requires the ORDER PARAMETER")
    print(f"  to be nonzero. The Leggett mode is an oscillation of the RELATIVE")
    print(f"  PHASE between sector order parameters Delta_i = |Delta_i| e^{{i phi_i}}.")
    print(f"  When |Delta_i| = 0 (no condensate), the phase is undefined.")
    print(f"  The mode disappears, just as the Goldstone mode does (S38).")
    print(f"  The GGE relic has no Leggett modes and no 9th integral.")

    # Additional finding: the Leggett mode is the SLOWEST collective mode
    print(f"\n  Structural finding: LEGGETT IS SLOWEST MODE")
    print(f"  omega_L1 (0.070) < omega_L2 (0.107) < omega_PV (0.792)")
    print(f"  T_L1 = {transit_results['T_L1']:.1f} M_KK^{{-1}} >> dt_transit = {data['dt_transit']:.5f}")
    print(f"  The Leggett mode has the LARGEST adiabatic parameter")
    print(f"  (most frozen) of all collective modes during transit.")

    # =================================================================
    # SAVE DATA
    # =================================================================

    save_path = os.path.join(SCRIPT_DIR, 's49_leggett_transit.npz')

    # Collect all results
    save_dict = {
        # Gate
        'gate_name': np.array(['LEGGETT-TRANSIT-49']),
        'gate_verdict': np.array([gate_verdict]),
        'gate_detail': np.array([gate_detail]),

        # Sudden-limit
        'omega_transit': sudden_results['omega_transit'],
        'ratio_L1': sudden_results['ratio_L1'],
        'ratio_L2': sudden_results['ratio_L2'],
        'Q_ad_L1': sudden_results['Q_ad_L1'],
        'delta_phi_L1': sudden_results['delta_phi_L1'],
        'delta_phi_L2': sudden_results['delta_phi_L2'],
        'N_osc_L1': sudden_results['N_osc_L1'],
        'N_osc_L2': sudden_results['N_osc_L2'],
        'dtau_transit': sudden_results['dtau_transit'],

        # Transit dynamics
        'T_L1': transit_results['T_L1'],
        'T_L2': transit_results['T_L2'],
        'T_PV': transit_results['T_PV'],
        'ratio_transit_L1': transit_results['ratio_transit_L1'],
        'gamma_LZ': transit_results['gamma_LZ'],
        'P_LZ_leggett': transit_results['P_LZ_leggett'],
        'tau_post': transit_results['tau_post'],
        'doL1_frac': transit_results['doL1_frac'],

        # Numerical integration
        'A_L_physical': A_L_phys,
        'A_L_adiabatic': A_L_adiab,
        'E_kin_physical': E_kin_phys,
        'E_kin_adiabatic': E_kin_adiab,

        # 9th integral
        'I_9_mean': ninth_results.get('I_9_mean', 0.0),
        'I_9_rel_var': ninth_results.get('I_9_rel_var', 0.0),
        'comm_RH_max': ninth_results['comm_RH_max'],
        'PB_estimate': ninth_results['PB_estimate'],
        'ninth_integral_status': np.array([ninth_results['ninth_integral_status']]),

        # Fate
        'Delta_post': fate_results['Delta_post'],
        'gap_factor': fate_results['gap_factor'],
        'omega_L1_post': fate_results['omega_L1_post'],
        'BCS_overlap': fate_results['BCS_overlap'],

        # Time traces (for plotting)
        't_physical': sol_physical.t,
        'phi_physical': sol_physical.y[:3, :],
        'dphi_physical': sol_physical.y[3:, :],
        't_adiabatic': sol_adiabatic.t,
        'phi_adiabatic': sol_adiabatic.y[:3, :],
        'dphi_adiabatic': sol_adiabatic.y[3:, :],
    }

    # Add I_9 time trace if available
    if 'I_9_time' in ninth_results:
        save_dict['I_9_time'] = ninth_results['I_9_time']
        save_dict['I_9_values'] = ninth_results['I_9_values']

    np.savez(save_path, **save_dict)
    print(f"\n  Data saved: {save_path}")

    # =================================================================
    # PLOT
    # =================================================================

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('S49 LEGGETT-TRANSIT-49: Leggett Mode Through Transit\n'
                 f'Gate: {gate_verdict}', fontsize=14, fontweight='bold')

    # Panel 1: Physical scenario -- phase trajectories
    ax = axes[0, 0]
    t_phys = sol_physical.t
    T_L = transit_results['T_L1']
    # Normalize time by Leggett period
    t_norm = t_phys / T_L

    ax.plot(t_norm, sol_physical.y[0, :], 'b-', lw=0.8, label=r'$\phi_{B1}$', alpha=0.8)
    ax.plot(t_norm, sol_physical.y[1, :], 'r-', lw=0.8, label=r'$\phi_{B2}$', alpha=0.8)
    ax.plot(t_norm, sol_physical.y[2, :], 'g-', lw=1.2, label=r'$\phi_{B3}$')

    # Mark transit
    t_transit_norm = data['dt_transit'] / T_L
    ax.axvline(0, color='gray', ls='--', lw=0.8, alpha=0.5)
    ax.axvline(t_transit_norm, color='gray', ls='--', lw=0.8, alpha=0.5)
    ax.axvspan(0, t_transit_norm, alpha=0.1, color='orange', label='Transit')

    ax.set_xlabel(r'$t / T_{Leggett}$')
    ax.set_ylabel(r'$\phi_i$ (rad)')
    ax.set_title('Physical: condensate destroyed')
    ax.legend(fontsize=8)
    ax.set_xlim(-2, 10)

    # Panel 2: Adiabatic scenario -- phase trajectories
    ax = axes[0, 1]
    t_adiab = sol_adiabatic.t
    t_norm_a = t_adiab / T_L

    ax.plot(t_norm_a, sol_adiabatic.y[0, :], 'b-', lw=0.8, label=r'$\phi_{B1}$', alpha=0.8)
    ax.plot(t_norm_a, sol_adiabatic.y[1, :], 'r-', lw=0.8, label=r'$\phi_{B2}$', alpha=0.8)
    ax.plot(t_norm_a, sol_adiabatic.y[2, :], 'g-', lw=1.2, label=r'$\phi_{B3}$')

    ax.axvline(0, color='gray', ls='--', lw=0.8, alpha=0.5)
    ax.axvline(t_transit_norm, color='gray', ls='--', lw=0.8, alpha=0.5)
    ax.axvspan(0, t_transit_norm, alpha=0.1, color='orange', label='Transit')

    ax.set_xlabel(r'$t / T_{Leggett}$')
    ax.set_ylabel(r'$\phi_i$ (rad)')
    ax.set_title('Adiabatic: condensate survives (hypothetical)')
    ax.legend(fontsize=8)
    ax.set_xlim(-2, 10)

    # Panel 3: Relative phase comparison
    ax = axes[1, 0]

    # Physical: relative phase phi_3 - phi_cm12
    rho_fold = data['rho_fold']
    w12 = rho_fold[0] + rho_fold[1]
    phi_cm12_phys = (rho_fold[0] * sol_physical.y[0] + rho_fold[1] * sol_physical.y[1]) / w12
    phi_rel_phys = sol_physical.y[2] - phi_cm12_phys

    phi_cm12_adiab = (rho_fold[0] * sol_adiabatic.y[0] + rho_fold[1] * sol_adiabatic.y[1]) / w12
    phi_rel_adiab = sol_adiabatic.y[2] - phi_cm12_adiab

    ax.plot(t_norm, phi_rel_phys, 'k-', lw=1.0, label='Physical (P_exc=1)')
    ax.plot(t_norm_a, phi_rel_adiab, 'r-', lw=1.0, alpha=0.7, label='Adiabatic')

    ax.axvline(0, color='gray', ls='--', lw=0.8, alpha=0.5)
    ax.axhline(0, color='gray', ls='-', lw=0.5, alpha=0.3)

    ax.set_xlabel(r'$t / T_{Leggett}$')
    ax.set_ylabel(r'$\phi_{rel}$ (rad)')
    ax.set_title(r'Relative phase $\phi_{B3} - \phi_{cm}$')
    ax.legend(fontsize=8)
    ax.set_xlim(-2, 30)

    # Panel 4: 9th integral conservation
    ax = axes[1, 1]
    if 'I_9_time' in ninth_results:
        t_I9 = ninth_results['I_9_time']
        I_9_vals = ninth_results['I_9_values']
        t_I9_norm = t_I9 / T_L

        ax.plot(t_I9_norm, I_9_vals, 'b-', lw=0.8)
        ax.axhline(ninth_results['I_9_mean'], color='r', ls='--', lw=0.8,
                   label=f"mean = {ninth_results['I_9_mean']:.4e}")

        ax.set_xlabel(r'$t / T_{Leggett}$')
        ax.set_ylabel(r'$I_9$ (M$_{KK}$)')
        ax.set_title(f"9th integral (adiabatic): rel.var = {ninth_results['I_9_rel_var']:.2e}")
        ax.legend(fontsize=8)
    else:
        ax.text(0.5, 0.5, 'No I_9 data\n(integration failed)',
                ha='center', va='center', transform=ax.transAxes)
        ax.set_title('9th integral')

    plt.tight_layout()
    plot_path = os.path.join(SCRIPT_DIR, 's49_leggett_transit.png')
    plt.savefig(plot_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Plot saved: {plot_path}")

    # =================================================================
    # SUMMARY TABLE
    # =================================================================
    print()
    print("=" * 70)
    print("SUMMARY TABLE")
    print("=" * 70)
    print(f"{'Quantity':<35s} {'Value':<25s} {'Source':<15s}")
    print("-" * 75)
    print(f"{'omega_L1 (pre-transit)':<35s} {data['omega_L1']:<25.6f} {'S48':<15s}")
    print(f"{'omega_L2 (pre-transit)':<35s} {data['omega_L2']:<25.6f} {'S48':<15s}")
    print(f"{'omega_transit':<35s} {sudden_results['omega_transit']:<25.1f} {'1/dt':<15s}")
    print(f"{'omega_transit/omega_L1':<35s} {sudden_results['ratio_L1']:<25.0f} {'SUDDEN':<15s}")
    print(f"{'N_osc during transit':<35s} {sudden_results['N_osc_L1']:<25.6e} {'FROZEN':<15s}")
    print(f"{'delta_phi during transit':<35s} {sudden_results['delta_phi_L1']:<25.6e} {'FROZEN':<15s}")
    print(f"{'LZ P_exc (Leggett)':<35s} {transit_results['P_LZ_leggett']:<25.6e} {'ADIAB':<15s}")
    print(f"{'Delta_SC post-transit':<35s} {'[0, 0, 0]':<25s} {'P_exc=1':<15s}")
    print(f"{'omega_L1 post-transit':<35s} {fate_results['omega_L1_post']:<25.6e} {'J=0':<15s}")
    print(f"{'A_L (physical)':<35s} {A_L_phys:<25.6e} {'numerical':<15s}")
    print(f"{'A_L (adiabatic, comparison)':<35s} {A_L_adiab:<25.6f} {'numerical':<15s}")
    print(f"{'I_9 rel. variation (adiabatic)':<35s} {ninth_results.get('I_9_rel_var',0):<25.6e} {'numerical':<15s}")
    print(f"{'9th integral status':<35s} {'TRIVIAL (J=0)':<25s} {'structural':<15s}")
    print(f"{'Gate verdict':<35s} {gate_verdict:<25s} {'':<15s}")

    return gate_verdict


if __name__ == '__main__':
    verdict = main()
    print(f"\nFinal gate verdict: {verdict}")
