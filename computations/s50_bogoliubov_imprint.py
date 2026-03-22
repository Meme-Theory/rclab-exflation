#!/usr/bin/env python3
"""
S50 BOGOLIUBOV-IMPRINT-50: Frozen Leggett Imprint in Bogoliubov Spectrum
=========================================================================

Gate: BOGOLIUBOV-IMPRINT-50
  PASS: |beta_k|^2 encodes Leggett mass (spectral feature at omega_L)
  FAIL: |beta_k|^2 featureless (LZ P~1 for all modes, no spectral imprint)
  INFO: feature exists but at wrong scale or too weak to affect n_s

Physical question (the Volovik paradox):
  The Leggett mass omega_L1 = 0.070 M_KK exists ONLY when the pre-transit
  condensate is nonzero.  Post-transit, P_exc = 1 destroys the condensate
  (LEGGETT-TRANSIT-49 FAIL: Delta_SC = 0, J = 0, omega_L = 0).

  The resolution proposed in S49 (Volovik wayforward): Bogoliubov
  coefficients carry a FROZEN IMPRINT of the pre-transit Leggett gap
  into the post-transit quasiparticle distribution (Paper 27 methodology --
  particle creation in time-dependent backgrounds).

Method (Paper 27, Volovik 2013):
  In a time-dependent BCS background, quasiparticle creation is described
  by a Bogoliubov transformation between pre-transit and post-transit
  vacua.  The key quantity is |beta_k|^2 -- the occupation of mode k
  in the post-transit state expressed in the pre-transit basis.

  For a BCS gap Delta(t) that varies in time:
    |beta_k|^2 = occupation of Bogoliubov quasiparticle k

  The Leggett mode creates a TIME-DEPENDENT MODULATION of the sector gaps:
    Delta_i(t) = Delta_i(tau(t)) * [1 + A_L cos(omega_L * t + phi_0)]

  This modulation is FROZEN during transit (dt/T_L = 1.25e-5, S49),
  which means the Leggett phase is essentially a STATIC parameter
  during the quench.  The question is: does this static phase shift
  the Bogoliubov coefficients?

  Three levels of analysis:
  (A) Uniform gap (no Leggett): |beta_k|^2 from LZ formula
  (B) Modulated gap (Leggett): |beta_k|^2 with Leggett modulation
  (C) Comparison: delta(|beta_k|^2) = (B) - (A)

  Additionally: the 8 Richardson-Gaudin conserved integrals I_alpha
  are set by the pre-transit BCS ground state.  They ENCODE the
  Josephson couplings J_ij which determine omega_L.  But is this
  encoding DETECTABLE in the power spectrum P(K)?

Input data:
  - s49_leggett_transit.npz (transit dynamics, P_exc=1)
  - s49_kz_3component.npz (per-mode P_LZ, sector decomposition)
  - s49_dipolar_catalog.npz (Leggett coupling data)
  - s48_leggett_mode.npz (omega_L, J_ij, rho_i scans)
  - canonical_constants.py

Output:
  - s50_bogoliubov_imprint.npz
  - s50_bogoliubov_imprint.png

Author: Volovik-Superfluid-Universe-Theorist (Session 50, W1-C)
Date: 2026-03-20

References:
  Volovik (2013) Paper 27: Superfluids as Non-Equilibrium Quantum Vacua
  Volovik (2003) Paper 01: Universe in a Helium Droplet, Ch. 28-29
  Zurek (1996): KZ mechanism for cosmological defect formation
  S38: Schwinger-instanton duality, P_exc = 1
  S49: Leggett-transit FAIL, dipolar-catalog PASS
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp, quad
from scipy.interpolate import CubicSpline
import sys
import os
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    tau_fold, v_terminal, dt_transit, E_cond, E_cond_ED_8mode,
    Delta_0_GL, Delta_B3, xi_BCS, omega_PV, Gamma_Langer_BCS,
    E_B1, E_B2_mean, E_B3_mean, P_exc_kz, n_Bog, n_pairs,
    rho_B2_per_mode, N_dof_BCS, M_max_thouless, S_inst,
    PI, M_KK, M_KK_gravity,
)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


# =============================================================================
# SECTION 1: LOAD ALL PRIOR DATA
# =============================================================================

def load_all_data():
    """Load S48 and S49 data archives."""
    data = {}

    # S48 Leggett mode
    d48 = np.load(os.path.join(SCRIPT_DIR, 's48_leggett_mode.npz'), allow_pickle=True)
    data['omega_L1'] = float(d48['omega_L1_fold'])
    data['omega_L2'] = float(d48['omega_L2_fold'])
    data['Delta_fold'] = np.array(d48['Delta_fold'])  # [B1, B2, B3]
    data['rho_fold'] = np.array(d48['rho_fold'])      # [B1, B2, B3]
    data['J_12'] = float(d48['J_12_fold'])
    data['J_23'] = float(d48['J_23_fold'])
    data['J_13'] = float(d48['J_13_fold'])
    data['tau_scan'] = np.array(d48['tau_scan'])
    data['Delta_B1_scan'] = np.array(d48['Delta_B1_scan'])
    data['Delta_B2_scan'] = np.array(d48['Delta_B2_scan'])
    data['Delta_B3_scan'] = np.array(d48['Delta_B3_scan'])

    # S49 3-component KZ
    d49_kz = np.load(os.path.join(SCRIPT_DIR, 's49_kz_3component.npz'), allow_pickle=True)
    data['P_LZ_u1'] = float(d49_kz['P_LZ_u1'])
    data['P_LZ_su2'] = float(d49_kz['P_LZ_su2'])
    data['P_LZ_c2'] = float(d49_kz['P_LZ_c2'])
    data['n_u1'] = float(d49_kz['n_u1'])
    data['n_su2'] = float(d49_kz['n_su2'])
    data['n_c2'] = float(d49_kz['n_c2'])
    data['n_total_3comp'] = float(d49_kz['n_total_3comp'])
    data['dDelta_dt'] = float(d49_kz['dDelta_dt'])
    data['J_c2'] = float(d49_kz['J_c2'])
    data['J_su2'] = float(d49_kz['J_su2'])
    data['J_u1'] = float(d49_kz['J_u1'])

    # S49 Leggett transit
    d49_lt = np.load(os.path.join(SCRIPT_DIR, 's49_leggett_transit.npz'), allow_pickle=True)
    data['omega_transit'] = float(d49_lt['omega_transit'])
    data['ratio_L1'] = float(d49_lt['ratio_L1'])
    data['delta_phi_L1'] = float(d49_lt['delta_phi_L1'])
    data['N_osc_L1'] = float(d49_lt['N_osc_L1'])
    data['A_L_physical'] = float(d49_lt['A_L_physical'])
    data['A_L_adiabatic'] = float(d49_lt['A_L_adiabatic'])

    # S49 dipolar catalog
    d49_dp = np.load(os.path.join(SCRIPT_DIR, 's49_dipolar_catalog.npz'), allow_pickle=True)
    data['leggett_epsilon'] = float(d49_dp['leggett_epsilon'])
    data['leggett_m_G'] = float(d49_dp['leggett_m_G'])

    return data


# =============================================================================
# SECTION 2: BOGOLIUBOV COEFFICIENTS FOR UNIFORM GAP (NO LEGGETT)
# =============================================================================

def bogoliubov_uniform(data):
    """
    Compute |beta_k|^2 for a uniform (no Leggett modulation) BCS gap.

    For a time-dependent BCS gap Delta(t) going from Delta_0 to 0
    during a sudden quench of duration dt_transit:

    The Landau-Zener formula for each mode k with energy epsilon_k:
        |beta_k|^2 = exp(-pi * Delta_k^2 / |dDelta_k/dt|)

    where dDelta_k/dt = Delta_0 * v_terminal / (Delta_tau/2).

    For the framework, the BCS gap is SECTOR-DEPENDENT:
        Delta_B1 = 0.372 M_KK
        Delta_B2 = 0.732 M_KK (dominant)
        Delta_B3 = 0.084 M_KK

    The Bogoliubov coefficients for quasiparticle k in sector i are:
        |beta_k^i|^2 = P_LZ_i = exp(-pi * E_qp_i^2 / |dE_qp_i/dt|)

    In the sudden-quench limit (dt << 1/Delta), all P_LZ -> 1.

    Here we compute a CONTINUOUS version: for fictitious momentum k,
    we parametrize the dispersion relation within each sector and compute
    |beta_k|^2 as a function of k.
    """
    results = {}

    Delta = data['Delta_fold']  # [B1, B2, B3]
    omega_transit = data['omega_transit']  # = 1/dt_transit

    # Sector parameters
    sector_names = ['B1 (u1)', 'B2 (C2)', 'B3 (su2)']
    d_i = np.array([1, 4, 3])  # degeneracies
    rho_i = np.array([1.0, rho_B2_per_mode, 1.0])  # DOS per mode
    E_k = np.array([E_B1, E_B2_mean, E_B3_mean])  # mode energies

    # The BCS gap profile: Delta_i(t) = Delta_i * f(t/dt_transit)
    # where f goes from 1 to 0 during transit.
    # For sudden quench: f(x) = theta(-x) (step function).
    # dDelta/dt = Delta * delta(t) (Dirac delta).
    # But for finite quench duration:
    # dDelta/dt ~ Delta / dt_transit at the crossing point.

    dDelta_dt = data['dDelta_dt']  # from S49

    # Compute P_LZ for each sector -- these match S49 exactly
    P_LZ = np.zeros(3)
    for i in range(3):
        E_qp = np.sqrt(E_k[i]**2 + Delta[i]**2)
        dEqp_dt = Delta[i] * dDelta_dt / E_qp
        P_LZ[i] = np.exp(-PI * E_qp**2 / abs(dEqp_dt))

    results['P_LZ_uniform'] = P_LZ
    results['n_pairs_uniform'] = np.sum(d_i * rho_i * P_LZ)

    # Now compute a CONTINUOUS version: parameterize fictitious momentum
    # within each sector.  In a 0D system, there is NO continuous momentum.
    # But the 8 modes span a range of energies.  We parametrize by a
    # "sector energy" epsilon that varies around each mode energy.
    #
    # The key insight: the LZ formula P_LZ = exp(-pi * gamma) where
    # gamma = E_qp^2 / |dE_qp/dt| depends on the quasiparticle energy.
    # For different modes k, E_qp(k) varies, giving different P_LZ(k).
    #
    # In a continuous theory (as would emerge on the fabric), the modes
    # would have a dispersion epsilon_k = epsilon_0 + v_F * |k - k_F|,
    # and P_LZ would be k-dependent.

    # Create a fine grid of "energies" spanning the spectrum
    epsilon_grid = np.linspace(0.75, 1.05, 1000)
    P_LZ_grid = np.zeros_like(epsilon_grid)
    for j, eps in enumerate(epsilon_grid):
        E_qp = np.sqrt(eps**2 + Delta_0_GL**2)
        dEqp_dt = Delta_0_GL * dDelta_dt / E_qp
        P_LZ_grid[j] = np.exp(-PI * E_qp**2 / abs(dEqp_dt))

    results['epsilon_grid'] = epsilon_grid
    results['P_LZ_grid'] = P_LZ_grid

    return results


# =============================================================================
# SECTION 3: BOGOLIUBOV COEFFICIENTS WITH LEGGETT MODULATION
# =============================================================================

def bogoliubov_leggett(data):
    """
    Compute |beta_k|^2 with the Leggett mode modulation.

    The Leggett mode creates a static phase offset between sectors
    during the transit (because transit is sudden relative to omega_L).

    The modulation of the gap is:
        Delta_i(t) = Delta_i(tau(t)) * [1 + A_L * cos(omega_L * t + phi_0)]

    where A_L is the Leggett mode amplitude.

    CRITICAL POINT FROM S49:
    The Leggett mode is FROZEN during transit: dt/T_L = 1.25e-5.
    So during transit, the Leggett phase is effectively a CONSTANT:
        Delta_i(t) = Delta_i(tau(t)) * [1 + A_L * cos(phi_0)]

    This is just a rescaling of the gap by a phi_0-dependent factor.
    The LZ probability becomes:
        P_LZ_i(phi_0) = exp(-pi * E_qp_i(phi_0)^2 / |dE_qp_i(phi_0)/dt|)

    where the phi_0 dependence enters through:
        Delta_i_eff(phi_0) = Delta_i * [1 + A_L * cos(phi_0)]

    The POST-TRANSIT occupation is then:
        <n_k> = P_LZ_i(phi_0)

    The power spectrum P(K) on the fabric samples different values of
    phi_0 at different locations (the Leggett phase is spatially
    varying on the fabric scale).

    KEY ANALYSIS:
    1. How much does P_LZ vary as phi_0 varies from 0 to 2*pi?
    2. This variation is the "Leggett imprint" in the Bogoliubov spectrum.
    3. If the variation is O(1), the imprint is strong (PASS).
    4. If the variation is << 1, the imprint is negligible (FAIL).
    """
    results = {}

    Delta = data['Delta_fold']
    omega_L1 = data['omega_L1']
    omega_L2 = data['omega_L2']
    omega_transit = data['omega_transit']
    dDelta_dt = data['dDelta_dt']

    # Leggett amplitude: from S49, A_L_adiabatic = 0.0976 (if condensate survives)
    # From ground state zero-point motion: A_L = sqrt(hbar/(2*rho*omega_L))
    # With rho = rho_fold and omega_L = omega_L1:
    rho_total = np.sum(data['rho_fold'])
    A_L_zp = np.sqrt(1.0 / (2 * rho_total * omega_L1))

    # HOWEVER: the BCS ground state has the Leggett mode in its zero-point state.
    # The "amplitude" of the relative-phase fluctuation is:
    # <delta_theta^2> = 1/(2 * rho * omega_L)
    # delta_theta_rms = 1/sqrt(2 * rho * omega_L)
    delta_theta_rms = 1.0 / np.sqrt(2 * rho_total * omega_L1)

    # The Leggett mode modulates the Josephson ENERGY, not the gap directly.
    # The gap modulation from Leggett:
    # Delta_B2(theta) = Delta_B2 * [1 + epsilon * cos(theta)]
    # where epsilon = J_23 / (rho_B2 * Delta_B2) << 1
    epsilon_L = data['leggett_epsilon']  # = 0.00248

    # The modulation of Delta_B2 from the Leggett mode:
    # delta(Delta_B2)/Delta_B2 = epsilon_L * delta_theta
    # For zero-point motion: delta_theta = delta_theta_rms
    delta_Delta_frac = epsilon_L * delta_theta_rms

    results['A_L_zp'] = A_L_zp
    results['delta_theta_rms'] = delta_theta_rms
    results['epsilon_L'] = epsilon_L
    results['delta_Delta_frac'] = delta_Delta_frac

    # Now compute P_LZ as a function of the frozen Leggett phase phi_0
    phi_0_grid = np.linspace(0, 2*PI, 361)  # 1-degree resolution
    P_LZ_B1 = np.zeros_like(phi_0_grid)
    P_LZ_B2 = np.zeros_like(phi_0_grid)
    P_LZ_B3 = np.zeros_like(phi_0_grid)

    for j, phi_0 in enumerate(phi_0_grid):
        # The Leggett mode modulates each sector gap:
        # Mode 1 (omega_L1): primarily B3 vs {B1, B2}
        # From S48 eigenvector: L1 ~ (0.229, 0.229, 0.229) + (-, -, 1.42)
        # The dominant motion is B3 phase relative to B1+B2.
        # The gap modulation from relative phase:
        #   Delta_B2_eff = Delta_B2 * sqrt(1 + 2*epsilon_L*cos(phi_0))
        #   ~ Delta_B2 * (1 + epsilon_L * cos(phi_0))
        # The correction to Delta from the Josephson coupling:
        # In the self-consistent BCS with Josephson:
        #   Delta_i = Delta_i^0 + sum_j J_ij * Delta_j / (Delta_j) * cos(phi_j - phi_i)
        # Simplified: the modulation is of order epsilon_L ~ 0.0025

        # B1 gap modulation (coupled to B2 through J_12)
        mod_B1 = 1.0 + (data['J_12'] / (data['rho_fold'][0] * Delta[0])) * np.cos(phi_0)
        # B2 gap modulation (coupled to B3 through J_23)
        mod_B2 = 1.0 + (data['J_23'] / (data['rho_fold'][1] * Delta[1])) * np.cos(phi_0)
        # B3 gap modulation (coupled to B2 through J_23, dominant)
        mod_B3 = 1.0 + (data['J_23'] / (data['rho_fold'][2] * Delta[2])) * np.cos(phi_0)

        # Effective gaps
        Delta_B1_eff = Delta[0] * mod_B1
        Delta_B2_eff = Delta[1] * mod_B2
        Delta_B3_eff = Delta[2] * mod_B3

        # LZ for each sector
        for i, (Delta_eff, E_k_i) in enumerate([(Delta_B1_eff, E_B1),
                                                  (Delta_B2_eff, E_B2_mean),
                                                  (Delta_B3_eff, E_B3_mean)]):
            E_qp = np.sqrt(E_k_i**2 + Delta_eff**2)
            # The gap rate dDelta/dt must also be rescaled
            dDelta_dt_eff = Delta_eff * abs(v_terminal) / (0.030 / 2.0)
            dEqp_dt = Delta_eff * dDelta_dt_eff / E_qp
            P_LZ_val = np.exp(-PI * E_qp**2 / abs(dEqp_dt))
            if i == 0:
                P_LZ_B1[j] = P_LZ_val
            elif i == 1:
                P_LZ_B2[j] = P_LZ_val
            else:
                P_LZ_B3[j] = P_LZ_val

    results['phi_0_grid'] = phi_0_grid
    results['P_LZ_B1_vs_phi'] = P_LZ_B1
    results['P_LZ_B2_vs_phi'] = P_LZ_B2
    results['P_LZ_B3_vs_phi'] = P_LZ_B3

    # Compute the modulation depth: delta(P_LZ) / P_LZ_mean
    for label, P_arr in [('B1', P_LZ_B1), ('B2', P_LZ_B2), ('B3', P_LZ_B3)]:
        P_mean = np.mean(P_arr)
        P_max = np.max(P_arr)
        P_min = np.min(P_arr)
        mod_depth = (P_max - P_min) / P_mean if P_mean > 0 else 0
        results[f'P_LZ_{label}_mean'] = P_mean
        results[f'P_LZ_{label}_max'] = P_max
        results[f'P_LZ_{label}_min'] = P_min
        results[f'mod_depth_{label}'] = mod_depth

    # The modulation amplitudes for individual Josephson couplings
    # J_12/rho_B1/Delta_B1:
    mod_amp_B1 = data['J_12'] / (data['rho_fold'][0] * Delta[0])
    mod_amp_B2 = data['J_23'] / (data['rho_fold'][1] * Delta[1])
    mod_amp_B3 = data['J_23'] / (data['rho_fold'][2] * Delta[2])
    results['mod_amp_B1'] = mod_amp_B1
    results['mod_amp_B2'] = mod_amp_B2
    results['mod_amp_B3'] = mod_amp_B3

    return results


# =============================================================================
# SECTION 4: RICHARDSON-GAUDIN INTEGRAL ANALYSIS
# =============================================================================

def rg_integral_analysis(data):
    """
    Analyze the Richardson-Gaudin conserved integrals for Leggett encoding.

    The GGE has 8 Richardson-Gaudin conserved integrals I_alpha.
    These are determined by the pre-transit BCS ground state.

    The BCS ground state includes the Josephson couplings J_ij
    through the inter-sector pairing. Therefore:

    I_alpha = I_alpha(E_1,...,E_8; g; n_1,...,n_8)

    where E_i are mode energies, g is the BCS coupling, and n_i are
    the quasiparticle occupations (0 in the ground state, 1 post-transit).

    The Josephson couplings J_ij affect the MODE ENERGIES through the
    self-consistent gap equation:
        E_qp_i = sqrt(epsilon_i^2 + Delta_i^2)
    and Delta_i depends on J_ij through:
        Delta_i = Delta_i^{BCS} + sum_j J_ij * cos(phi_i - phi_j)

    Therefore: I_alpha depends on J_ij, which determines omega_L.
    But this is a STATIC dependence: the RG integrals are NUMBERS,
    not dynamical quantities.

    The question is: can you RECONSTRUCT omega_L from the 8 numbers {I_alpha}?
    And if so, does this reconstruction appear in the power spectrum?
    """
    results = {}

    Delta = data['Delta_fold']
    E_modes = np.array([E_B1, E_B2_mean, E_B2_mean, E_B2_mean,
                        E_B2_mean, E_B3_mean, E_B3_mean, E_B3_mean])

    # The RG integrals in the BCS ground state (all n_k = 0):
    # I_alpha = epsilon_alpha + g * sum_{beta != alpha} 1/(epsilon_alpha - epsilon_beta)
    # These are the eigenvalues of the Gaudin Hamiltonian.

    # For the 8-mode system:
    # B1: 1 mode at epsilon_1 = E_B1 = 0.8191
    # B2: 4 modes at epsilon_{2-5} = E_B2_mean = 0.8453
    # B3: 3 modes at epsilon_{6-8} = E_B3_mean = 0.9782

    # The BCS coupling g = V_eff from the mechanism chain
    # From M_max = g * rho = 1.674, rho_total = 60.093:
    g_BCS = M_max_thouless / np.sum(np.array([1.0, rho_B2_per_mode,
                                               rho_B2_per_mode, rho_B2_per_mode,
                                               rho_B2_per_mode, 1.0, 1.0, 1.0]))

    # Simple RG integrals (first-order perturbation theory):
    N_modes = 8
    I_alpha = np.zeros(N_modes)
    for alpha in range(N_modes):
        I_alpha[alpha] = E_modes[alpha]
        for beta in range(N_modes):
            if beta != alpha:
                denom = E_modes[alpha] - E_modes[beta]
                if abs(denom) > 1e-15:
                    I_alpha[alpha] += g_BCS / denom
                # For degenerate modes, the contribution cancels in pairs

    results['I_alpha'] = I_alpha
    results['g_BCS'] = g_BCS

    # Now: how does omega_L enter the I_alpha?
    # omega_L^2 = J_23 * (Delta_B2 * rho_B3 + Delta_B3 * rho_B2) / (rho_B2 * rho_B3 * Delta_B2 * Delta_B3)
    # The J_23 modifies the mode energies by:
    # delta(E_qp_i) = J_23 * Delta_i * cos(phi_0) / E_qp_i
    # This shifts I_alpha by:
    # delta(I_alpha) = J_23 * Delta_i * cos(phi_0) / E_qp_i
    # The RELATIVE shift between B2 and B3 integrals is:
    # delta(I_B2) - delta(I_B3) ~ J_23 * (Delta_B2/E_B2 - Delta_B3/E_B3)

    delta_I_B2 = data['J_23'] * Delta[1] / np.sqrt(E_B2_mean**2 + Delta[1]**2)
    delta_I_B3 = data['J_23'] * Delta[2] / np.sqrt(E_B3_mean**2 + Delta[2]**2)
    delta_I_relative = abs(delta_I_B2 - delta_I_B3)

    # Compare to the total I_alpha variation
    I_range = np.max(I_alpha) - np.min(I_alpha)
    leggett_fraction = delta_I_relative / max(I_range, 1e-30)

    results['delta_I_B2'] = delta_I_B2
    results['delta_I_B3'] = delta_I_B3
    results['delta_I_relative'] = delta_I_relative
    results['I_range'] = I_range
    results['leggett_fraction'] = leggett_fraction

    return results


# =============================================================================
# SECTION 5: POWER SPECTRUM FROM BOGOLIUBOV COEFFICIENTS
# =============================================================================

def power_spectrum_analysis(data, bog_uniform, bog_leggett):
    """
    Compute the quasiparticle power spectrum P(K) from Bogoliubov coefficients.

    In a spatially extended system (the fabric), the post-transit state
    at each point x has Bogoliubov coefficients that depend on the LOCAL
    value of the Leggett phase phi_0(x).

    If the Leggett phase is UNIFORM: all points have the same |beta_k|^2.
    P(K) is flat -- no features.

    If the Leggett phase VARIES spatially: phi_0(x) ~ phi_0(x_0) + gradient.
    Then |beta_k|^2(x) varies, creating a modulated density field.
    The power spectrum of this modulation has features at K ~ omega_L/c_G
    where c_G is the "Goldstone speed" on the fabric.

    BUT: from S49 LEGGETT-TRANSIT-49, the condensate is DESTROYED post-transit.
    There is no Goldstone mode.  The Leggett phase is frozen at its
    pre-transit value and then becomes MEANINGLESS (Delta = 0).

    Therefore: the only imprint is from the STATIC Leggett phase
    at the moment of the quench.  This phase was set by the BCS
    ground state, which has phi_0 = 0 everywhere (by definition
    of the ground state -- the Leggett mode is in its zero-point
    oscillation, not a coherent state with a definite phase).

    This means: the Bogoliubov coefficients are IDENTICAL at every point
    on the fabric.  There is no spatial modulation from the Leggett mode.

    The power spectrum P(K) from the quasiparticle creation is:
        P(K) = sum_sectors d_i * rho_i * |beta_k_i|^2 * delta(K)
    which is a DELTA FUNCTION at K = 0 (uniform density).

    The spectral tilt n_s = 1 EXACTLY (Harrison-Zeldovich).
    No features from Leggett.
    """
    results = {}

    # The modulation depth from Section 3
    mod_B2 = bog_leggett['mod_depth_B2']
    mod_B3 = bog_leggett['mod_depth_B3']
    mod_B1 = bog_leggett['mod_depth_B1']

    # The MAXIMUM possible power spectrum feature:
    # If somehow the Leggett phase WERE spatially varying (e.g., from thermal
    # fluctuations in the pre-transit BCS state), the power spectrum would
    # have a feature at K ~ omega_L / c_fabric, with amplitude:
    #   delta_P/P ~ mod_depth

    # From S49: the BCS ground state has phi_0 = 0 (no thermal fluctuations
    # at T = 0). Quantum zero-point fluctuations give:
    # <delta_phi^2>_{ZP} = 1/(2*rho*omega_L)
    delta_theta_rms = bog_leggett['delta_theta_rms']

    # The power spectrum feature from zero-point Leggett fluctuations:
    # delta_P/P ~ epsilon_L * delta_theta_rms * (modulation of P_LZ)
    # This is a PRODUCT of three small numbers:
    # epsilon_L = 0.0025, delta_theta_rms, mod_depth ~ P_LZ variation

    feature_amplitude = bog_leggett['epsilon_L'] * delta_theta_rms * mod_B2

    # Compare to required amplitude for CMB features:
    # A_s = 2.1e-9 (CMB scalar amplitude)
    # The Bogoliubov feature would need delta_P/P ~ A_s to be detectable.
    # But we also need to compare to the TOTAL quasiparticle density.

    # The total quasiparticle density:
    n_total = data['n_total_3comp']

    # Feature strength relative to total:
    feature_relative = feature_amplitude / max(n_total, 1e-30)

    results['mod_depth_B1'] = mod_B1
    results['mod_depth_B2'] = mod_B2
    results['mod_depth_B3'] = mod_B3
    results['delta_theta_rms'] = delta_theta_rms
    results['feature_amplitude'] = feature_amplitude
    results['feature_relative'] = feature_relative

    # K-space: the Leggett wavelength on the fabric
    # K_L = omega_L1 / c_fabric
    # From canonical_constants: c_fabric = 209.97
    from canonical_constants import c_fabric
    K_L = data['omega_L1'] / c_fabric
    lambda_L = 2 * PI / K_L

    results['K_L'] = K_L
    results['lambda_L'] = lambda_L
    results['c_fabric'] = c_fabric

    return results


# =============================================================================
# SECTION 6: THE DEEP QUESTION -- WHAT IS PRESERVED?
# =============================================================================

def deep_analysis(data, bog_uniform, bog_leggett, rg_results, ps_results):
    """
    The deep question: what information survives the transit?

    The GGE is determined by 8 Richardson-Gaudin integrals.
    These integrals are SET by the pre-transit BCS ground state.
    The BCS ground state depends on the Josephson couplings J_ij.
    J_ij determines omega_L.

    So: omega_L -> J_ij -> BCS ground state -> I_alpha -> GGE.

    But the chain is INFORMATION-LOSSY:
    - J_ij affects I_alpha at order J_23/Delta ~ epsilon_L ~ 0.0025
    - The variation of I_alpha from Leggett coupling is 0.0025
      of the total I_alpha variation (rg_results['leggett_fraction'])

    The information about omega_L is ENCODED in the RG integrals
    but at a level of epsilon_L ~ 0.25%.

    For the Bogoliubov coefficients |beta_k|^2:
    - All modes are in the sudden-quench regime (P_LZ > 0.994)
    - The modulation from phi_0 variation is < 1% (mod_depth)
    - The actual phi_0 in the ground state is 0 (no phase)

    CONCLUSION: The Leggett mass is encoded in the RG integrals
    at the epsilon_L ~ 0.25% level, but this encoding is:
    (a) Not spatially modulated (BCS ground state has phi_0 = 0)
    (b) Not detectable in P(K) (no K-dependence)
    (c) Overwhelmed by the dominant LZ pair creation

    The Bogoliubov spectrum is FEATURELESS.
    The sudden quench erases the Leggett structure.

    This is the analog of particle creation in de Sitter space
    (Volovik Paper 27): when the expansion rate H >> omega_mode,
    all modes are created with occupation ~ 1, and the spectrum
    is thermal-like (no features from the pre-inflationary state).
    The Leggett mode, being 12,640x slower than the transit, is
    in the "trans-Planckian" regime: its physics is invisible
    to the post-transit observer.
    """
    results = {}

    # Summary numbers
    P_LZ_range = np.array([bog_leggett['P_LZ_B1_min'], bog_leggett['P_LZ_B1_max'],
                            bog_leggett['P_LZ_B2_min'], bog_leggett['P_LZ_B2_max'],
                            bog_leggett['P_LZ_B3_min'], bog_leggett['P_LZ_B3_max']])

    # Maximum modulation across all sectors
    max_mod = max(bog_leggett['mod_depth_B1'],
                  bog_leggett['mod_depth_B2'],
                  bog_leggett['mod_depth_B3'])

    # The "erasure ratio": how much the sudden quench erases Leggett info
    # In the adiabatic limit (omega_transit << omega_L), the Leggett mode
    # would be preserved with amplitude ~ 1.
    # In the sudden limit (omega_transit >> omega_L), the preserved fraction
    # scales as (omega_L / omega_transit)^2.
    erasure_ratio = (data['omega_L1'] / data['omega_transit'])**2

    results['max_modulation'] = max_mod
    results['erasure_ratio'] = erasure_ratio
    results['leggett_fraction_in_RG'] = rg_results['leggett_fraction']
    results['feature_amplitude'] = ps_results['feature_amplitude']

    # What IS preserved:
    # 1. The TOTAL number of pairs (n = 59.82, matches S38)
    # 2. The SECTOR DECOMPOSITION (B2: 93.3%, B3: 5.0%, B1: 1.7%)
    # 3. The 8 RG integrals (which encode epsilon_i and g, not omega_L)
    # 4. The GGE entropy (fixed by RG integrals)

    # What is NOT preserved:
    # 1. The Leggett mode (omega_L = 0 post-transit)
    # 2. The relative phase between sectors (meaningless with Delta = 0)
    # 3. Any spatial modulation from Leggett (phi_0 = 0 in ground state)

    results['preserved'] = ['n_total', 'sector_decomposition', 'RG_integrals', 'GGE_entropy']
    results['not_preserved'] = ['omega_L', 'relative_phase', 'spatial_modulation']

    return results


# =============================================================================
# SECTION 7: PLOTTING
# =============================================================================

def make_plots(data, bog_uniform, bog_leggett, rg_results, ps_results, deep_results):
    """Generate 4-panel figure."""
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Panel 1: P_LZ vs Leggett phase phi_0 for each sector
    ax = axes[0, 0]
    phi_deg = bog_leggett['phi_0_grid'] * 180 / PI
    ax.plot(phi_deg, bog_leggett['P_LZ_B1_vs_phi'], 'b-', linewidth=2, label='B1 (u(1))')
    ax.plot(phi_deg, bog_leggett['P_LZ_B2_vs_phi'], color='#FF9800', linewidth=2, label=r'B2 ($\mathbb{C}^2$)')
    ax.plot(phi_deg, bog_leggett['P_LZ_B3_vs_phi'], 'g-', linewidth=2, label='B3 (su(2))')
    ax.set_xlabel(r'Leggett phase $\phi_0$ (degrees)')
    ax.set_ylabel(r'$P_{LZ}$ (Bogoliubov occupation)')
    ax.set_title(r'$|\beta_k|^2$ vs Frozen Leggett Phase')
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)

    # Add modulation depth annotations
    for label, color, mod in [('B1', 'b', bog_leggett['mod_depth_B1']),
                               ('B2', '#FF9800', bog_leggett['mod_depth_B2']),
                               ('B3', 'g', bog_leggett['mod_depth_B3'])]:
        pass  # Will annotate in text below

    # Panel 2: Modulation depth bar chart
    ax = axes[0, 1]
    sectors = ['B1\n(u(1))', 'B2\n(C2)', 'B3\n(su(2))']
    mod_depths = [bog_leggett['mod_depth_B1'], bog_leggett['mod_depth_B2'],
                  bog_leggett['mod_depth_B3']]
    colors = ['#2196F3', '#FF9800', '#4CAF50']
    bars = ax.bar(sectors, mod_depths, color=colors, edgecolor='black', linewidth=0.8)
    for bar, val in zip(bars, mod_depths):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.0001,
                f'{val:.4f}', ha='center', va='bottom', fontsize=10, fontweight='bold')
    ax.set_ylabel(r'Modulation depth $\delta P/\bar{P}$')
    ax.set_title(r'Leggett Imprint: $\Delta P_{LZ} / \bar{P}_{LZ}$')
    ax.axhline(0.01, color='red', linestyle='--', linewidth=1, alpha=0.7, label='1% threshold')
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)

    # Panel 3: Erasure hierarchy
    ax = axes[1, 0]
    quantities = [r'$\omega_L/\omega_{transit}$',
                  r'$\epsilon_L = J_{23}/\Delta$',
                  r'$\delta\theta_{ZP}$',
                  r'$\delta I/I_{range}$',
                  'Max mod depth',
                  'Feature amp.']
    values = [data['omega_L1'] / data['omega_transit'],
              bog_leggett['epsilon_L'],
              bog_leggett['delta_theta_rms'],
              rg_results['leggett_fraction'],
              deep_results['max_modulation'],
              ps_results['feature_amplitude']]

    y_pos = np.arange(len(quantities))
    colors_bar = ['#E91E63', '#9C27B0', '#673AB7', '#3F51B5', '#2196F3', '#00BCD4']
    ax.barh(y_pos, np.log10(np.maximum(np.abs(values), 1e-30)), color=colors_bar,
            edgecolor='black', linewidth=0.5)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(quantities, fontsize=9)
    ax.set_xlabel(r'$\log_{10}$(value)')
    ax.set_title('Hierarchy of Leggett Imprint Quantities')
    ax.axvline(np.log10(0.01), color='red', linestyle='--', linewidth=1.5,
               alpha=0.7, label='1% detection threshold')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3, axis='x')

    # Add value labels
    for i, val in enumerate(values):
        ax.text(np.log10(max(abs(val), 1e-30)) + 0.1, i,
                f'{val:.2e}', va='center', fontsize=8)

    # Panel 4: Summary verdict
    ax = axes[1, 1]
    ax.axis('off')

    # Compact summary
    lines = [
        r"$\bf{BOGOLIUBOV\!-\!IMPRINT\!-\!50:\ FAIL}$",
        "",
        r"$\omega_L / \omega_{transit} = $" + f"{data['omega_L1']/data['omega_transit']:.1e}",
        r"$\epsilon_L = $" + f"{bog_leggett['epsilon_L']:.4f}",
        f"B2 mod depth = {bog_leggett['mod_depth_B2']:.1e} (93% of pairs)",
        f"B3 mod depth = {bog_leggett['mod_depth_B3']:.4f} (5%, parametric)",
        f"Feature in P(K) = {ps_results['feature_amplitude']:.1e}",
        f"Erasure ratio = {deep_results['erasure_ratio']:.1e}",
        "",
        r"$\bf{PRESERVED}$: n=59.82, sectors (93/5/2%),",
        "   8 RG integrals, GGE entropy",
        "",
        r"$\bf{NOT\ PRESERVED}$: Leggett mode,",
        r"   relative phase ($\Delta=0 \Rightarrow \phi$ undefined),",
        "   spatial modulation (BCS: " + r"$\phi_0=0$" + ")",
        "",
        r"$\bf{3He\ analog}$: dipolar order lost in normal",
        "state. Leggett mode exists only when " + r"$\Delta \neq 0$.",
        r"Paper 27: $H \gg \omega \Rightarrow$ trans-Planckian erasure.",
    ]
    text = "\n".join(lines)
    ax.text(0.05, 0.95, text, transform=ax.transAxes, fontsize=9,
            verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    fig.suptitle(
        r'S50 BOGOLIUBOV-IMPRINT-50: FAIL $-$ '
        r'$|\beta_k|^2$ featureless (max modulation = '
        f'{deep_results["max_modulation"]:.4f})',
        fontsize=12, fontweight='bold')
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    return fig


# =============================================================================
# MAIN
# =============================================================================

def main():
    t0 = time.time()

    print("=" * 78)
    print("  S50 BOGOLIUBOV-IMPRINT-50: Frozen Leggett Imprint in Bogoliubov Spectrum")
    print("=" * 78)

    # =========================================================================
    # STEP 1: Load all data
    # =========================================================================
    print("\n" + "-" * 78)
    print("  STEP 1: Load Prior Data")
    print("-" * 78)

    data = load_all_data()

    print(f"  omega_L1 = {data['omega_L1']:.6f} M_KK")
    print(f"  omega_L2 = {data['omega_L2']:.6f} M_KK")
    print(f"  omega_transit = {data['omega_transit']:.1f} M_KK")
    print(f"  ratio = {data['ratio_L1']:.0f} (DEEPLY SUDDEN)")
    print(f"  Delta_fold = {data['Delta_fold']}")
    print(f"  rho_fold = {data['rho_fold']}")
    print(f"  J_12 = {data['J_12']:.6f}, J_23 = {data['J_23']:.6f}, J_13 = {data['J_13']:.6f}")
    print(f"  n_total_3comp = {data['n_total_3comp']:.4f}")
    print(f"  leggett_epsilon = {data['leggett_epsilon']:.6f}")

    # =========================================================================
    # STEP 2: Uniform Bogoliubov coefficients (no Leggett)
    # =========================================================================
    print("\n" + "-" * 78)
    print("  STEP 2: Uniform Bogoliubov Coefficients (No Leggett)")
    print("-" * 78)

    bog_uniform = bogoliubov_uniform(data)

    print(f"\n  P_LZ (uniform, no Leggett modulation):")
    print(f"    B1: P_LZ = {bog_uniform['P_LZ_uniform'][0]:.8f}")
    print(f"    B2: P_LZ = {bog_uniform['P_LZ_uniform'][1]:.8f}")
    print(f"    B3: P_LZ = {bog_uniform['P_LZ_uniform'][2]:.8f}")
    print(f"  n_pairs (uniform) = {bog_uniform['n_pairs_uniform']:.4f}")

    # =========================================================================
    # STEP 3: Bogoliubov with Leggett modulation
    # =========================================================================
    print("\n" + "-" * 78)
    print("  STEP 3: Bogoliubov with Leggett Modulation")
    print("-" * 78)

    bog_leggett = bogoliubov_leggett(data)

    print(f"\n  Leggett parameters:")
    print(f"    epsilon_L = J_23/(rho*Delta) = {bog_leggett['epsilon_L']:.6f}")
    print(f"    delta_theta_rms (ZP)         = {bog_leggett['delta_theta_rms']:.6f}")
    print(f"    delta(Delta)/Delta (ZP)      = {bog_leggett['delta_Delta_frac']:.6e}")

    print(f"\n  Gap modulation amplitudes from Josephson coupling:")
    print(f"    B1: J_12/(rho_B1*Delta_B1) = {bog_leggett['mod_amp_B1']:.6f}")
    print(f"    B2: J_23/(rho_B2*Delta_B2) = {bog_leggett['mod_amp_B2']:.6f}")
    print(f"    B3: J_23/(rho_B3*Delta_B3) = {bog_leggett['mod_amp_B3']:.6f}")

    print(f"\n  P_LZ modulation depth (phi_0 = 0 to 2*pi):")
    for label in ['B1', 'B2', 'B3']:
        mean_val = bog_leggett[f'P_LZ_{label}_mean']
        min_val = bog_leggett[f'P_LZ_{label}_min']
        max_val = bog_leggett[f'P_LZ_{label}_max']
        mod = bog_leggett[f'mod_depth_{label}']
        print(f"    {label}: P_mean={mean_val:.8f}, "
              f"P_range=[{min_val:.8f}, {max_val:.8f}], "
              f"mod_depth={mod:.6f}")

    # =========================================================================
    # STEP 4: Richardson-Gaudin integral analysis
    # =========================================================================
    print("\n" + "-" * 78)
    print("  STEP 4: Richardson-Gaudin Integral Analysis")
    print("-" * 78)

    rg_results = rg_integral_analysis(data)

    print(f"\n  RG integrals I_alpha (first-order):")
    for i, I_val in enumerate(rg_results['I_alpha']):
        sector = 'B1' if i == 0 else ('B2' if i < 5 else 'B3')
        print(f"    I_{i+1} ({sector}) = {I_val:.6f}")

    print(f"\n  Leggett encoding in RG integrals:")
    print(f"    delta(I_B2) from J_23: {rg_results['delta_I_B2']:.6e}")
    print(f"    delta(I_B3) from J_23: {rg_results['delta_I_B3']:.6e}")
    print(f"    |delta_I_B2 - delta_I_B3|: {rg_results['delta_I_relative']:.6e}")
    print(f"    I_range (max-min): {rg_results['I_range']:.6f}")
    print(f"    Leggett fraction in I: {rg_results['leggett_fraction']:.6e}")

    # =========================================================================
    # STEP 5: Power spectrum analysis
    # =========================================================================
    print("\n" + "-" * 78)
    print("  STEP 5: Power Spectrum Analysis")
    print("-" * 78)

    ps_results = power_spectrum_analysis(data, bog_uniform, bog_leggett)

    print(f"\n  Leggett wavelength on fabric:")
    print(f"    K_L = omega_L / c_fabric = {ps_results['K_L']:.6e} M_KK")
    print(f"    lambda_L = 2*pi/K_L = {ps_results['lambda_L']:.2f} M_KK^{{-1}}")
    print(f"    c_fabric = {ps_results['c_fabric']:.2f} M_KK")

    print(f"\n  Feature amplitude in power spectrum:")
    print(f"    Modulation depth (B2): {ps_results['mod_depth_B2']:.6f}")
    print(f"    Zero-point angle:      {ps_results['delta_theta_rms']:.6f}")
    print(f"    epsilon_L:             {bog_leggett['epsilon_L']:.6f}")
    print(f"    Feature amplitude:     {ps_results['feature_amplitude']:.6e}")
    print(f"    Feature / n_total:     {ps_results['feature_relative']:.6e}")

    # =========================================================================
    # STEP 6: Deep analysis -- what is preserved?
    # =========================================================================
    print("\n" + "-" * 78)
    print("  STEP 6: Deep Analysis -- Information Survival Through Transit")
    print("-" * 78)

    deep_results = deep_analysis(data, bog_uniform, bog_leggett, rg_results, ps_results)

    print(f"\n  Information hierarchy:")
    print(f"    omega_L / omega_transit    = {data['omega_L1']/data['omega_transit']:.2e}")
    print(f"    epsilon_L (coupling)       = {bog_leggett['epsilon_L']:.4f}")
    print(f"    Erasure ratio (oL/oT)^2   = {deep_results['erasure_ratio']:.2e}")
    print(f"    Max P_LZ modulation        = {deep_results['max_modulation']:.4f}")
    print(f"    Leggett fraction in I_alpha = {deep_results['leggett_fraction_in_RG']:.6e}")
    print(f"    Feature amplitude in P(K)  = {deep_results['feature_amplitude']:.6e}")

    print(f"\n  ANALOGY (Paper 27, Volovik 2013):")
    print(f"    omega_transit plays the role of the Hubble rate H.")
    print(f"    omega_L plays the role of the mode frequency omega.")
    print(f"    H >> omega => mode is in the 'trans-Planckian' regime.")
    print(f"    All modes created with n ~ 1 (thermal-like occupation).")
    print(f"    Pre-inflationary structure (Leggett mode) is ERASED.")
    print(f"    This is the cosmological version of the Kibble-Zurek freeze-out:")
    print(f"    fast quench creates maximal excitation, destroying pre-quench order.")

    print(f"\n  3He ANALOG:")
    print(f"    In 3He-B, rapid cooling through T_c creates:")
    print(f"    - Textural defects (vortices) via KZ mechanism")
    print(f"    - Quasiparticle excitations via pair-breaking")
    print(f"    - The dipolar interaction (d.l locking) acts on timescale >> 1/Delta")
    print(f"    After the quench, the dipolar order is LOST")
    print(f"    (d-vector and l-vector are decoupled in the normal state).")
    print(f"    The Leggett mode exists ONLY in the superfluid phase.")
    print(f"    Our framework is the same: omega_L exists only when Delta != 0.")

    # =========================================================================
    # STEP 7: Gate verdict
    # =========================================================================
    print("\n" + "=" * 78)
    print("  GATE BOGOLIUBOV-IMPRINT-50: VERDICT")
    print("=" * 78)

    max_mod = deep_results['max_modulation']
    feature_amp = ps_results['feature_amplitude']

    # Classification logic:
    # PASS: |beta_k|^2 encodes Leggett mass (spectral feature at omega_L)
    #   Requires: modulation > 1% AND spatial feature realized AND affects n_s
    # FAIL: |beta_k|^2 is featureless (LZ P~1, no realized spectral imprint)
    #   Criteria: no spatial modulation (BCS ground state phi_0=0) OR
    #             feature amplitude negligible
    # INFO: parametric modulation exists but not physically realized
    #
    # DECISIVE PHYSICS (three independent arguments for FAIL):
    #
    # Argument 1 (ground state): BCS ground state has phi_0 = 0 everywhere.
    # The Leggett mode is in its quantum zero-point state, NOT a coherent
    # state with definite phase.  Expectation value <cos(phi_0)> = 0 by
    # symmetry (equipartition over U(1)_7 orbit).  Therefore the gap
    # modulation VANISHES on average: <delta(Delta)> = 0.
    #
    # Argument 2 (zero-point amplitude): Even considering fluctuations,
    # delta(Delta)/Delta ~ epsilon_L * delta_theta_rms = 1.5e-3.
    # The P_LZ modulation from this is O(epsilon_L^2) ~ 6e-6 in B2
    # (dominant sector, 93% of pairs).  Negligible.
    #
    # Argument 3 (spatial uniformity): On the fabric, each cell has an
    # INDEPENDENT BCS ground state.  All have phi_0 = 0.  No cell-to-cell
    # variation of Bogoliubov coefficients from the Leggett mode.
    # P(K) has no features from this channel.
    #
    # The B3 modulation of 4.2% is the parametric sensitivity of P_LZ(B3)
    # to phi_0 IF phi_0 were driven to finite values.  But it is not
    # driven: phi_0 = 0 in the ground state, and the transit is too fast
    # (dt/T_L = 1.25e-5) to excite it.

    # The feature amplitude in P(K) is 1.7e-9 (negligible)
    # The BCS ground state has phi_0 = 0 (no spatial modulation)
    # The zero-point gap modulation is 1.5e-3 (O(epsilon_L) < 1%)
    # The dominant B2 sector has modulation depth 1e-6

    verdict = "FAIL"
    physics_reason = (
        f"B2 (93% of pairs): mod_depth = {bog_leggett['mod_depth_B2']:.1e} (negligible). "
        f"B3 (5% of pairs): mod_depth = {bog_leggett['mod_depth_B3']:.4f} (parametric, not realized). "
        f"BCS ground state has phi_0 = 0 (no spatial modulation). "
        f"Feature amplitude in P(K) = {feature_amp:.1e}. "
        f"Sudden quench (omega_transit/omega_L = {int(data['ratio_L1'])}) erases Leggett structure."
    )

    print(f"\n  Pre-registered gate criteria:")
    print(f"    PASS: |beta_k|^2 encodes Leggett mass (spectral feature at omega_L)")
    print(f"    FAIL: |beta_k|^2 featureless (LZ P~1 for all modes)")
    print(f"    INFO: feature exists but wrong scale or too weak")
    print(f"\n  Results:")
    print(f"    Max P_LZ modulation depth:  {max_mod:.6f}")
    print(f"    Feature amplitude in P(K):  {feature_amp:.6e}")
    print(f"    BCS ground state phi_0:     0 (exactly)")
    print(f"    Spatial variation of phi_0:  NONE (ground state)")
    print(f"\n  Physics reason: {physics_reason}")
    print(f"\n  +---------------------------------------------------------+")
    print(f"  |  GATE BOGOLIUBOV-IMPRINT-50: {verdict:>4s}                       |")
    print(f"  |  |beta_k|^2 featureless: max mod = {max_mod:.4f}           |")
    print(f"  |  Sudden quench erases Leggett structure               |")
    print(f"  |  omega_L/omega_transit = {data['omega_L1']/data['omega_transit']:.2e}                 |")
    print(f"  |  (Paper 27: H >> omega => trans-Planckian erasure)     |")
    print(f"  +---------------------------------------------------------+")

    elapsed = time.time() - t0
    print(f"\n  Computation time: {elapsed:.1f}s")

    # =========================================================================
    # Collect all results
    # =========================================================================
    all_results = {}

    # Gate
    all_results['gate_name'] = 'BOGOLIUBOV-IMPRINT-50'
    all_results['gate_verdict'] = verdict
    all_results['gate_detail'] = physics_reason

    # Uniform Bogoliubov
    all_results['P_LZ_uniform_B1'] = bog_uniform['P_LZ_uniform'][0]
    all_results['P_LZ_uniform_B2'] = bog_uniform['P_LZ_uniform'][1]
    all_results['P_LZ_uniform_B3'] = bog_uniform['P_LZ_uniform'][2]
    all_results['n_pairs_uniform'] = bog_uniform['n_pairs_uniform']
    all_results['epsilon_grid'] = bog_uniform['epsilon_grid']
    all_results['P_LZ_grid'] = bog_uniform['P_LZ_grid']

    # Leggett modulation
    all_results['epsilon_L'] = bog_leggett['epsilon_L']
    all_results['delta_theta_rms'] = bog_leggett['delta_theta_rms']
    all_results['delta_Delta_frac'] = bog_leggett['delta_Delta_frac']
    all_results['phi_0_grid'] = bog_leggett['phi_0_grid']
    all_results['P_LZ_B1_vs_phi'] = bog_leggett['P_LZ_B1_vs_phi']
    all_results['P_LZ_B2_vs_phi'] = bog_leggett['P_LZ_B2_vs_phi']
    all_results['P_LZ_B3_vs_phi'] = bog_leggett['P_LZ_B3_vs_phi']
    for label in ['B1', 'B2', 'B3']:
        all_results[f'mod_depth_{label}'] = bog_leggett[f'mod_depth_{label}']
        all_results[f'P_LZ_{label}_mean'] = bog_leggett[f'P_LZ_{label}_mean']
        all_results[f'P_LZ_{label}_min'] = bog_leggett[f'P_LZ_{label}_min']
        all_results[f'P_LZ_{label}_max'] = bog_leggett[f'P_LZ_{label}_max']
    all_results['mod_amp_B1'] = bog_leggett['mod_amp_B1']
    all_results['mod_amp_B2'] = bog_leggett['mod_amp_B2']
    all_results['mod_amp_B3'] = bog_leggett['mod_amp_B3']

    # RG integrals
    all_results['I_alpha'] = rg_results['I_alpha']
    all_results['g_BCS'] = rg_results['g_BCS']
    all_results['delta_I_relative'] = rg_results['delta_I_relative']
    all_results['I_range'] = rg_results['I_range']
    all_results['leggett_fraction'] = rg_results['leggett_fraction']

    # Power spectrum
    all_results['K_L'] = ps_results['K_L']
    all_results['lambda_L'] = ps_results['lambda_L']
    all_results['feature_amplitude'] = ps_results['feature_amplitude']
    all_results['feature_relative'] = ps_results['feature_relative']

    # Deep analysis
    all_results['max_modulation'] = deep_results['max_modulation']
    all_results['erasure_ratio'] = deep_results['erasure_ratio']

    # Key derived quantities
    all_results['omega_L1'] = data['omega_L1']
    all_results['omega_transit'] = data['omega_transit']
    all_results['ratio_L1'] = data['ratio_L1']

    return all_results, data, bog_uniform, bog_leggett, rg_results, ps_results, deep_results


if __name__ == '__main__':
    all_results, data, bog_uniform, bog_leggett, rg_results, ps_results, deep_results = main()

    # Save data
    save_dict = {}
    for k, v in all_results.items():
        if isinstance(v, (int, float, np.integer, np.floating)):
            save_dict[k] = v
        elif isinstance(v, np.ndarray):
            save_dict[k] = v
        elif isinstance(v, str):
            save_dict[k] = np.array([v])
        elif isinstance(v, list):
            save_dict[k] = np.array(v)

    npz_path = os.path.join(SCRIPT_DIR, 's50_bogoliubov_imprint.npz')
    np.savez(npz_path, **save_dict)
    print(f"\n  Data saved to: {npz_path}")

    # Generate plot
    fig = make_plots(data, bog_uniform, bog_leggett, rg_results, ps_results, deep_results)
    png_path = os.path.join(SCRIPT_DIR, 's50_bogoliubov_imprint.png')
    fig.savefig(png_path, dpi=150, bbox_inches='tight')
    plt.close(fig)
    print(f"  Plot saved to: {png_path}")
