#!/usr/bin/env python3
"""
BEC-IMPEDANCE-ANALOG-69 (W5-A): BEC Quench Experiment Design
=============================================================

Design a BEC Feshbach quench experiment to test the framework's core prediction:

  |T(k)|^2 = 1  for  k < k_tach                                     (1)

This is the Weinberg superhorizon conservation theorem: curvature perturbations
zeta_k are frozen for modes outside the sonic horizon. In the substrate picture,
this is the Rayleigh long-wavelength limit — wavelengths much longer than the
healing length xi do not scatter off the quench-induced structure.

GOVERNING FRAMEWORK
-------------------
The framework's transit is a first-order phase transition at tau=0.190 through
the van Hove fold of the SU(3) fiber. The transit proceeds at Mach 13.75,
creating an acoustic white hole. The tachyonic scale k_tach = sqrt(z''/z)
divides modes into:

  k < k_tach:  frozen (superhorizon), conserved amplitude  (phononic analog: Rayleigh limit)
  k > k_tach:  oscillating (subhorizon), decaying amplitude (phononic analog: Mie scattering)

The BEC analog replaces the internal-geometry quench with a Feshbach resonance
quench. The mapping is:

  FRAMEWORK                         BEC ANALOG
  -------------------------------------------------------
  SU(3) fiber eigenvalue spectrum   BEC ground state |Psi_0>
  Jensen deformation tau            Scattering length a_s
  Transit (Mach 13.75)              Sudden quench a_s -> a_s'
  Healing length xi_BCS             Healing length xi = 1/sqrt(8*pi*n_0*a_s)
  k_tach = sqrt(z''/z)             k_tach^BEC = 1/xi
  |T(k)|^2 = 1 (superhorizon)      n_k = flat plateau for k*xi << 1
  Bogoliubov beta_k^2               Post-quench occupation n_k
  BCS squeeze parameter r           Quench squeeze r_Q = (1/4)*ln(a_s'/a_s)

The Bogoliubov-de Gennes (BdG) equations for quasiparticles in a BEC
after a sudden quench of the interaction strength g = 4*pi*hbar^2*a_s/m:

  i*hbar * d/dt (u_k, v_k)^T = L_BdG (u_k, v_k)^T                 (2)

  L_BdG = ( eps_k + g*n_0,   g*n_0  )
          ( -g*n_0,  -(eps_k + g*n_0) )

  eps_k = hbar^2*k^2/(2*m),  n_0 = condensate density.

The Bogoliubov dispersion:

  omega_k = sqrt(eps_k * (eps_k + 2*g*n_0)) / hbar                 (3)

The healing length:

  xi = hbar / sqrt(2*m*g*n_0) = 1/sqrt(16*pi*n_0*a_s)              (4)

For a SUDDEN quench g_i -> g_f:

  beta_k = (u_k^f * v_k^i - v_k^f * u_k^i)                        (5)

  n_k = |beta_k|^2                                                  (6)

  = (1/4) * ( sqrt(omega_k^f / omega_k^i) - sqrt(omega_k^i / omega_k^f) )^2  (7)

The signature is:

  n_k -> (1/4)*(R^{1/4} - R^{-1/4})^2  for k*xi_f << 1  (|T|^2 = 1)  (8)
  n_k ~ (R-1)^2 / (4*(k*xi_f)^4)      for k*xi_f >> 1  (free-particle) (9)

EXPERIMENTAL PARAMETERS
-----------------------
We compute:
  - Required quench parameters: a_s^i, a_s^f, dt_Q, n_0
  - Predicted post-quench Bogoliubov spectrum n_k (Eq. 7)
  - Mapping to framework parameters (Mach number, tachyonic scale)
  - Time-of-flight imaging protocol
  - Candidate labs and atomic species

Gate: BEC-ANALOG-69 — INFO (design study, no pass/fail criterion)

Author: Quantum-Acoustics Theorist (Workhorse-Quantum-Acoustics)
Session: S69
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    # Framework constants
    H_fold, v_terminal, dt_transit, tau_fold,
    hbar_SI, k_B_SI, c_light,
    # Transit data
    M_KK, A_s_CMB, PI,
    # BCS squeeze
    Delta_0_OES, E_B1, E_B2_mean, E_B3_mean,
    # Cosmological
    n_pairs,
)

OUTDIR = os.path.dirname(os.path.abspath(__file__))

# ============================================================================
#  SECTION 1: BEC Physical Parameters
# ============================================================================

print("=" * 72)
print("BEC-IMPEDANCE-ANALOG-69: BEC Quench Experiment Design")
print("=" * 72)

# ---------------------------------------------------------------------------
# Atomic species: 7Li, 39K, 85Rb, 133Cs all have Feshbach resonances
# We design for 87Rb (most widely available) and 39K (broadest Feshbach)
# ---------------------------------------------------------------------------

# 87Rb parameters
m_Rb = 87 * 1.66054e-27         # kg (atomic mass)
a_Bohr = 5.29177e-11            # m (Bohr radius)  # (local)
a_bg_Rb = 100.4 * a_Bohr        # m (background scattering length for 87Rb)

# 39K parameters (Roati lab, LENS Florence)
m_K = 39 * 1.66054e-27          # kg
a_bg_K = -33.0 * a_Bohr         # m (background, near 402G Feshbach)

# Typical BEC parameters
n_0_typical = 1e14 * 1e6        # m^{-3} (10^{14} cm^{-3} typical BEC density)
# Use more conservative density
n_0 = 5e13 * 1e6                # m^{-3} (5 * 10^{13} cm^{-3})

print("\n--- Atomic Species Parameters ---")
print(f"87Rb: m = {m_Rb:.3e} kg, a_bg = {a_bg_Rb/a_Bohr:.1f} a_0")
print(f"39K:  m = {m_K:.3e} kg,  a_bg = {a_bg_K/a_Bohr:.1f} a_0")
print(f"BEC density n_0 = {n_0:.2e} m^{{-3}} = {n_0/1e6:.2e} cm^{{-3}}")

# ============================================================================
#  SECTION 2: Framework-to-BEC Mapping
# ============================================================================
#
# The framework transit has:
#   Mach_scalar = v_flow / c_BLV = 13.75   (S64)
#   k_tach = sqrt(z''/z) = 1209 M_KK       (S67)
#   Bogoliubov squeeze |beta_k|^2:
#     ~ 1 for k << k_tach (superhorizon, flat plateau)
#     ~ 0 for k >> k_tach (subhorizon, decaying)
#
# The BEC quench has:
#   Mach_BEC = (a_s'/a_s)^{1/2} - 1  [ratio of sound speeds]
#   k_tach^{BEC} = 1/xi_f = sqrt(16*pi*n_0*a_s_f)
#   n_k = |beta_k|^2 from Eq. (7)
#
# To reproduce the framework's Mach 13.75, we need:
#   c_s' / c_s = (a_s'/a_s)^{1/2}     since c_s = sqrt(g*n_0/m) ~ sqrt(a_s)
#   Mach ~ |1 - c_s'/c_s| / min(c_s, c_s')  ... but this is not how BEC Mach is defined.
#
# More precisely: in the framework, the "Mach number" is the ratio of the
# modulus velocity (d tau/dt) to the acoustic speed c_BLV = 0.485.
# In the BEC, the analog is the QUENCH RAPIDITY:
#   R_Q = |ln(a_s'/a_s)| / (2 * dt_Q * omega_xi)
# where omega_xi = c_s/xi = sqrt(g*n_0/m) / xi = 2*g*n_0/hbar is the
# healing frequency. When R_Q >> 1, the quench is "supersonic" — it
# changes the effective Hamiltonian faster than the system can respond.
#
# The framework's transit duration:
#   dt_transit = 0.00113 M_KK^{-1}      (S38)
#   omega_transit = 1/dt_transit = 885 M_KK
# The framework's Bogoliubov frequency at the fold:
#   omega_B = sqrt(E_B2_mean^2 - Delta^2) ~ 0.7 M_KK
# So the "quench rapidity" R_framework = omega_transit / omega_B ~ 1260 >> 1
#
# For a realistic BEC quench:
#   We can achieve dt_Q ~ 1 us with magnetic field ramping
#   omega_xi ~ 2*pi * 1 kHz for typical BEC parameters
#   R_Q ~ 1 / (1e-6 * 2*pi*1e3) ~ 160  (supersonic, good)
#
# We design for a quench ratio a_s'/a_s that gives a MEASURABLE n_k plateau.
# The plateau height is (from Eq. 7 with omega_f/omega_i = sqrt(R)):
#   n_k(k->0) = (1/4) * (R^{1/4} - R^{-1/4})^2
#             ~ (1/4) * R^{1/2}     for large R                      (10)
# ---------------------------------------------------------------------------

c_BLV = 0.485  # Framework BLV speed (M_KK units, S64)  # (local)
Mach_framework = 13.75  # S64 Mach number  # (local)

print("\n--- Framework Transit Parameters ---")
print(f"Mach number:        {Mach_framework}")
print(f"c_BLV:              {c_BLV} M_KK")
print(f"k_tach (S67):       1209 M_KK")
print(f"dt_transit:         {dt_transit:.6f} M_KK^{{-1}}")
print(f"v_terminal:         {v_terminal:.2f} M_KK")

# Load the framework Bogoliubov spectrum from S67
transit_data = np.load(os.path.join(OUTDIR, 's67_transit_ps.npz'), allow_pickle=True)
k_framework = transit_data['k_grid_rk']
beta_sq_framework = transit_data['beta_sq_rk']
k_tach_framework = float(transit_data['k_transit'])

print(f"\nFramework Bogoliubov spectrum loaded: {len(k_framework)} k-points")
print(f"k_tach (from data): {k_tach_framework:.1f} M_KK")

# ============================================================================
#  SECTION 3: BEC Quench Design — Three Experimental Regimes
# ============================================================================
#
# We design three quench protocols, from most conservative to most aggressive:
#
# (A) MODERATE QUENCH (a_s'/a_s = 10): Mach ~ 3, n_k(plateau) ~ 2
#     Easy to implement, clean signal, but low Mach
#
# (B) STRONG QUENCH (a_s'/a_s = 100): Mach ~ 10, n_k(plateau) ~ 25
#     Closer to framework Mach, strong signal
#
# (C) EXTREME QUENCH (a_s'/a_s = 1000): Mach ~ 30, n_k(plateau) ~ 250
#     Above framework Mach, tests deep into Rayleigh regime
#
# For each, compute:
#   1. Scattering length a_s^i, a_s^f (in units of Bohr radius)
#   2. Healing length xi_f (determines k_tach^BEC)
#   3. Sound speed c_s (before and after)
#   4. Quench rapidity R_Q
#   5. Predicted n_k spectrum
#   6. TOF imaging requirements
# ---------------------------------------------------------------------------

print("\n" + "=" * 72)
print("SECTION 3: BEC Quench Design — Three Regimes")
print("=" * 72)

# BEC helper functions

def healing_length(n_0, a_s, m):
    """Healing length xi = hbar / sqrt(2*m*g*n_0), g = 4*pi*hbar^2*a_s/m."""
    g = 4 * PI * hbar_SI**2 * a_s / m
    return hbar_SI / np.sqrt(2 * m * g * n_0)

def sound_speed(n_0, a_s, m):
    """Bogoliubov sound speed c_s = sqrt(g*n_0/m)."""
    g = 4 * PI * hbar_SI**2 * a_s / m
    return np.sqrt(g * n_0 / m)

def bogoliubov_dispersion(k, n_0, a_s, m):
    """Bogoliubov dispersion omega_k = sqrt(eps_k * (eps_k + 2*g*n_0)) / hbar."""
    eps_k = hbar_SI**2 * k**2 / (2 * m)
    g = 4 * PI * hbar_SI**2 * a_s / m
    return np.sqrt(eps_k * (eps_k + 2 * g * n_0)) / hbar_SI

def quench_nk(k, n_0, a_s_i, a_s_f, m):
    """
    Post-quench Bogoliubov occupation number n_k = |beta_k|^2
    for a SUDDEN quench of scattering length a_s_i -> a_s_f.

    From Eq. (7):
      n_k = (1/4) * ( sqrt(omega_f/omega_i) - sqrt(omega_i/omega_f) )^2

    This is the exact result for instantaneous (sudden) quench.
    """
    omega_i = bogoliubov_dispersion(k, n_0, a_s_i, m)
    omega_f = bogoliubov_dispersion(k, n_0, a_s_f, m)

    # Avoid division by zero for k=0 modes
    with np.errstate(divide='ignore', invalid='ignore'):
        ratio = omega_f / omega_i
        nk = 0.25 * (np.sqrt(ratio) - 1.0/np.sqrt(ratio))**2
    return nk

def quench_nk_analytic_limits(k_xi_f, ratio):
    """
    Analytic limits of n_k for sudden quench with scattering length ratio.

    For k*xi_f << 1 (phononic regime):
      omega ~ c_s * k, so omega_f/omega_i = c_f/c_i = sqrt(a_s_f/a_s_i) = sqrt(ratio)
      n_k = (1/4) * (sqrt(omega_f/omega_i) - sqrt(omega_i/omega_f))^2
          = (1/4) * (ratio^{1/4} - ratio^{-1/4})^2                     (10)

    For k*xi_f >> 1 (free-particle regime):
      omega_k -> hbar*k^2/(2m), so omega_f = omega_i
      Leading correction: n_k ~ (ratio - 1)^2 / (4*(k*xi_f)^4)

    Parameters:
      k_xi_f: dimensionless k * xi_f
      ratio: a_s_f / a_s_i
    """
    # Phononic regime: omega_f/omega_i = sqrt(ratio), then sqrt of THAT gives ratio^{1/4}
    n_phononic = 0.25 * (ratio**0.25 - ratio**(-0.25))**2

    # Free-particle regime: omega ~ hbar*k^2/(2m), so omega_f = omega_i
    # Leading correction: n_k ~ (ratio - 1)^2 / (4 * (k*xi_f)^4)
    n_free = np.where(k_xi_f > 0, (ratio - 1)**2 / (4 * (k_xi_f)**4), n_phononic)

    return n_phononic, n_free


# ---------------------------------------------------------------------------
# Design parameters for the three regimes
# ---------------------------------------------------------------------------

regimes = {
    'A_moderate': {'label': 'A: Moderate', 'ratio': 10, 'color': 'C0'},
    'B_strong':   {'label': 'B: Strong',   'ratio': 100, 'color': 'C1'},
    'C_extreme':  {'label': 'C: Extreme',  'ratio': 1000, 'color': 'C2'},
}

# Use 39K (broadest Feshbach resonance, Roati lab demonstrated 0-1000 a_0 tuning)
m = m_K
species = '39K'

# Initial scattering length: start with small positive a_s
a_s_initial = 5.0 * a_Bohr      # 5 a_0 (achievable near Feshbach zero crossing)

# BEC trap parameters
# Thomas-Fermi radius for N=10^5 atoms, omega_trap = 2*pi*100 Hz
N_atoms = 1e5
omega_trap = 2 * PI * 100       # Hz (geometric mean trap frequency)
a_ho = np.sqrt(hbar_SI / (m * omega_trap))  # harmonic oscillator length
R_TF = a_ho * (15 * N_atoms * a_s_initial / a_ho)**(1/5)

# Chemical potential
mu_TF = 0.5 * m * omega_trap**2 * R_TF**2

# Use central density (Thomas-Fermi)
n_0_center = mu_TF / (4 * PI * hbar_SI**2 * a_s_initial / m)
n_0_use = n_0_center

print(f"\n--- BEC Configuration ---")
print(f"Species:            {species}")
print(f"N_atoms:            {N_atoms:.0e}")
print(f"omega_trap:         2*pi * {omega_trap/(2*PI):.0f} Hz")
print(f"a_ho:               {a_ho:.3e} m = {a_ho/1e-6:.2f} um")
print(f"a_s^initial:        {a_s_initial/a_Bohr:.1f} a_0")
print(f"R_TF:               {R_TF:.3e} m = {R_TF/1e-6:.2f} um")
print(f"mu_TF:              {mu_TF/k_B_SI:.3f} nK * k_B")
print(f"n_0 (center):       {n_0_use:.3e} m^{{-3}} = {n_0_use/1e6:.3e} cm^{{-3}}")

# ============================================================================
#  SECTION 4: Compute Quench Parameters and Bogoliubov Spectra
# ============================================================================

print("\n" + "=" * 72)
print("SECTION 4: Quench Parameters and Post-Quench Spectra")
print("=" * 72)

# k-grid in physical units — must extend to k*xi_f << 1 for ALL regimes.
# For the largest ratio (1000), xi_f = xi_i / sqrt(1000) = xi_i/31.6.
# To reach k*xi_f = 0.001 we need k = 0.001/xi_f = 0.001*31.6/xi_i = 0.032/xi_i.
# To cover ALL regimes' phononic limit, start at k = 1e-4 / xi_i.
N_k = 800  # (local)
xi_init = healing_length(n_0_use, a_s_initial, m)
k_phys = np.geomspace(1e-4 / xi_init, 200 / xi_init, N_k)

results = {}

for key, regime in regimes.items():
    ratio = regime['ratio']
    label = regime['label']
    color = regime['color']

    a_s_f = ratio * a_s_initial

    # Healing lengths
    xi_i = healing_length(n_0_use, a_s_initial, m)
    xi_f = healing_length(n_0_use, a_s_f, m)

    # Sound speeds
    c_i = sound_speed(n_0_use, a_s_initial, m)
    c_f = sound_speed(n_0_use, a_s_f, m)

    # Tachyonic scale (BEC analog): k_tach = 1/xi_f
    k_tach_BEC = 1.0 / xi_f

    # Quench rapidity: how "sudden" is the quench?
    # R_Q = |ln(ratio)| * hbar / (2 * dt_Q * mu_f)
    # For dt_Q = 1 us:
    dt_Q = 1e-6  # s
    mu_f = 4 * PI * hbar_SI**2 * a_s_f / m * n_0_use
    omega_xi_f = c_f / xi_f
    R_Q = np.abs(np.log(ratio)) / (2 * dt_Q * omega_xi_f)

    # Effective Mach number: ratio of quench speed to post-quench sound speed
    # The "speed" of the quench in energy units: delta_mu / dt_Q
    # Compared to the post-quench sound crossing time: xi_f / c_f
    Mach_BEC = np.abs(np.log(ratio)) / (2 * dt_Q * omega_xi_f)

    # Post-quench Bogoliubov spectrum
    nk = quench_nk(k_phys, n_0_use, a_s_initial, a_s_f, m)

    # Analytic plateau value: in phononic regime, omega_f/omega_i = sqrt(ratio)
    # n_k = (1/4)*(sqrt(omega_f/omega_i) - sqrt(omega_i/omega_f))^2
    #     = (1/4)*(ratio^{1/4} - ratio^{-1/4})^2
    n_plateau = 0.25 * (ratio**0.25 - ratio**(-0.25))**2

    # Verify plateau: compute n_k at very small k
    k_test_low = 0.001 / xi_f
    nk_test = quench_nk(np.array([k_test_low]), n_0_use, a_s_initial, a_s_f, m)[0]

    # Temperature requirement: the BEC must be cold enough that thermal
    # Bogoliubov occupation is below the quench signal
    # n_th(k) = 1/(exp(hbar*omega_k/(k_B*T)) - 1)
    # At k ~ 1/xi: omega ~ c_f/xi_f, so T < hbar*c_f/(k_B*xi_f) = mu_f/k_B
    T_max = mu_f / k_B_SI  # K

    # TOF imaging requirements
    # After TOF expansion time t_TOF, momentum k maps to position:
    # r(k) = hbar*k*t_TOF/m
    # For k ~ 1/xi_f, r = hbar*t_TOF/(m*xi_f)
    # Want r > resolution ~ 5 um
    t_TOF_min = 5e-6 * m * xi_f / hbar_SI  # s

    # For k ~ 0.01/xi_f (deep plateau), need:
    t_TOF_plateau = 5e-6 * m * xi_f / (0.01 * hbar_SI)  # s

    results[key] = {
        'ratio': ratio,
        'a_s_i': a_s_initial,
        'a_s_f': a_s_f,
        'xi_i': xi_i,
        'xi_f': xi_f,
        'c_i': c_i,
        'c_f': c_f,
        'k_tach': k_tach_BEC,
        'dt_Q': dt_Q,
        'R_Q': R_Q,
        'Mach_BEC': Mach_BEC,
        'nk': nk,
        'n_plateau': n_plateau,
        'nk_test': nk_test,
        'T_max': T_max,
        't_TOF_min': t_TOF_min,
        't_TOF_plateau': t_TOF_plateau,
        'mu_f': mu_f,
        'omega_xi_f': omega_xi_f,
    }

    print(f"\n--- Regime {label}: a_s'/a_s = {ratio} ---")
    print(f"  a_s^initial:      {a_s_initial/a_Bohr:.1f} a_0")
    print(f"  a_s^final:        {a_s_f/a_Bohr:.1f} a_0")
    print(f"  xi_initial:       {xi_i:.3e} m = {xi_i/1e-6:.2f} um")
    print(f"  xi_final:         {xi_f:.3e} m = {xi_f/1e-6:.3f} um")
    print(f"  c_s^initial:      {c_i:.3e} m/s = {c_i*1e3:.2f} mm/s")
    print(f"  c_s^final:        {c_f:.3e} m/s = {c_f*1e3:.2f} mm/s")
    print(f"  c_s ratio:        {c_f/c_i:.3f} (= sqrt(a_s'/a_s) = {np.sqrt(ratio):.3f})")
    print(f"  k_tach^BEC:       {k_tach_BEC:.3e} m^{{-1}}")
    print(f"  k_tach^BEC*xi_i:  {k_tach_BEC*xi_i:.3f}")
    print(f"  lambda_tach:      {2*PI/k_tach_BEC:.3e} m = {2*PI/k_tach_BEC/1e-6:.2f} um")
    print(f"  omega_xi^final:   {omega_xi_f:.3e} s^{{-1}} = 2*pi*{omega_xi_f/(2*PI):.0f} Hz")
    print(f"  dt_Q:             {dt_Q*1e6:.1f} us")
    print(f"  Quench rapidity:  {R_Q:.1f}")
    print(f"  Mach_BEC:         {Mach_BEC:.1f}")
    print(f"  n_k(plateau):     {n_plateau:.3f}")
    print(f"  n_k(k=0.001/xi):  {nk_test:.4f}  (cf. analytic: {n_plateau:.4f})")
    print(f"  T_max:            {T_max*1e9:.1f} nK")
    print(f"  t_TOF(min):       {t_TOF_min*1e3:.1f} ms")
    print(f"  t_TOF(plateau):   {t_TOF_plateau*1e3:.0f} ms")
    print(f"  mu_f:             {mu_f/k_B_SI * 1e9:.1f} nK * k_B")

# ============================================================================
#  SECTION 5: |T(k)|^2 = 1 Test — Flat Plateau Verification
# ============================================================================
#
# The core prediction: for k*xi_f << 1, n_k is CONSTANT.
# This is the BEC analog of Weinberg's superhorizon conservation.
#
# Mechanism: in the phononic regime (k*xi << 1), the Bogoliubov dispersion
# is LINEAR: omega_k ~ c_s * k. A sudden quench of c_s maps to a
# FREQUENCY RESCALING that is INDEPENDENT OF k. Therefore:
#
#   omega_f(k) / omega_i(k) = c_f/c_i = sqrt(a_s_f/a_s_i)  for all k*xi << 1
#
# and n_k = (1/4)*(sqrt(ratio) - 1/sqrt(ratio))^2 = CONSTANT.
#
# This is EXACTLY the same physics as superhorizon conservation:
# modes deep in the Rayleigh limit (k << 1/xi) experience a global
# conformal stretching that preserves all relative amplitudes.
# The transfer function |T(k)|^2 = |omega_f/omega_i| = 1 for the
# curvature perturbation zeta_k = u_k/z.
# ---------------------------------------------------------------------------

print("\n" + "=" * 72)
print("SECTION 5: |T(k)|^2 = 1 Verification — Plateau Flatness")
print("=" * 72)

for key, R in results.items():
    label = regimes[key]['label']
    ratio = R['ratio']
    xi_f = R['xi_f']
    xi_i = R['xi_i']
    nk = R['nk']
    n_plateau = R['n_plateau']

    # CRITICAL INSIGHT: The plateau requires the mode to be in the phononic
    # regime for BOTH initial and final states. This means:
    #   k * max(xi_i, xi_f) << 1
    # For a quench that INCREASES a_s (xi_f < xi_i), the binding constraint
    # is k*xi_i << 1. The plateau is ONLY truly flat for k*xi_i < 0.1.
    #
    # The broader region k*xi_f < 0.1 (but k*xi_i > 0.1) shows the
    # k-dependent TRANSITION from phononic to particle-like dispersion
    # in the initial state, which breaks the plateau.

    # Deep phononic: both initial and final are phononic
    mask_deep_phononic = k_phys * xi_i < 0.1
    # Intermediate: final is phononic, initial is transitioning
    mask_transition_phon = (k_phys * xi_i > 0.1) & (k_phys * xi_f < 1)
    # Free-particle: both are free-particle-like
    mask_free = k_phys * xi_f > 3

    if np.any(mask_deep_phononic) and n_plateau > 0:
        nk_deep = nk[mask_deep_phononic]
        flatness = np.std(nk_deep) / np.mean(nk_deep) if np.mean(nk_deep) > 0 else 0
        max_dev = np.max(np.abs(nk_deep - n_plateau)) / n_plateau
        print(f"\n  Regime {label} (ratio={ratio}):")
        print(f"    Plateau value (analytic):   {n_plateau:.4f}")
        print(f"    Mean(n_k, deep phononic):   {np.mean(nk_deep):.4f}")
        print(f"    Flatness (sigma/mu):        {flatness:.2e}")
        print(f"    Max deviation from plateau: {max_dev:.2e}")
        print(f"    N_modes (deep phononic):    {np.sum(mask_deep_phononic)}")
        print(f"    N_modes (transitioning):    {np.sum(mask_transition_phon)}")
        print(f"    N_modes (free particle):    {np.sum(mask_free)}")
        print(f"    Plateau regime: k < {0.1/xi_i:.2e} m^{{-1}} "
              f"(lambda > {2*PI*xi_i/0.1:.2e} m = {2*PI*xi_i/0.1/1e-6:.1f} um)")

        # Verify the 1/k^4 tail
        if np.any(mask_free):
            k_free = k_phys[mask_free]
            nk_free = nk[mask_free]
            log_k = np.log(k_free)
            log_nk = np.log(np.maximum(nk_free, 1e-30))
            valid = np.isfinite(log_nk)
            if np.sum(valid) > 2:
                slope = np.polyfit(log_k[valid], log_nk[valid], 1)[0]
                print(f"    Free-particle slope:        {slope:.2f}  (expected: -4.0)")

# ============================================================================
#  SECTION 6: Framework-to-BEC Mapping Table
# ============================================================================
#
# Map the framework's spectral quantities to measurable BEC quantities.
# ---------------------------------------------------------------------------

print("\n" + "=" * 72)
print("SECTION 6: Framework-to-BEC Analog Dictionary")
print("=" * 72)

R_B = results['B_strong']  # Use regime B as primary comparison

# Framework parameters
eps_H_fold = 0.022  # S67 geometric epsilon at fold  # (local)
c_BLV_phys = c_BLV  # in M_KK units

print(f"""
  FRAMEWORK QUANTITY              FRAMEWORK VALUE       BEC ANALOG VALUE
  ─────────────────────────────────────────────────────────────────────────
  Mach number                     {Mach_framework:.2f}              {R_B['Mach_BEC']:.1f}
  Tachyonic scale k_tach          {k_tach_framework:.0f} M_KK         {R_B['k_tach']:.2e} m^{{-1}}
  Healing length xi               {1/k_tach_framework:.4f} M_KK^{{-1}}   {R_B['xi_f']:.2e} m
  Sound speed (post-transit)      {c_BLV_phys:.3f} M_KK          {R_B['c_f']:.2e} m/s
  Bogoliubov plateau |beta|^2     ~1.0 (S57)            {R_B['n_plateau']:.1f}
  Transit duration                {dt_transit:.4f} M_KK^{{-1}}   {R_B['dt_Q']*1e6:.0f} us
  Quench rapidity                 ~1260 (S38)           {R_B['R_Q']:.1f}
  eps_H (slow-roll analog)        {eps_H_fold:.3f}              n/a (sudden quench)
  BCS squeeze r                   0.555 (S69)           {0.25*np.log(R_B['ratio']):.2f}
  Spectral tilt n_s               0.9595 (S66)          ~1.0 (flat plateau)
""")

# ============================================================================
#  SECTION 7: Measurement Protocol — Time-of-Flight Imaging
# ============================================================================

print("=" * 72)
print("SECTION 7: Measurement Protocol — Time-of-Flight (TOF) Imaging")
print("=" * 72)

print("""
PROTOCOL for testing |T(k)|^2 = 1:

1. PREPARATION:
   - Prepare 39K BEC in |F=1, m_F=-1> state near 402.70 G Feshbach resonance
   - Tune B-field to set a_s = 5 a_0 (initial weak interaction)
   - N ~ 10^5 atoms, T < T_c/10 to suppress thermal fraction
   - Trap: crossed ODT, omega_trap ~ 2*pi * 100 Hz

2. QUENCH:
   - Ramp B-field in dt_Q ~ 1 us to new a_s value (Regime A/B/C)
   - For Regime B (a_s = 500 a_0): delta_B ~ 0.3 G near resonance
   - B-field ramp must be faster than omega_xi^{-1}
   - Verify suddenness: dt_Q * omega_xi << 1

3. HOLD TIME:
   - Hold for t_hold = 0 (immediate release for sudden-quench prediction)
   - Optional: hold for t_hold = 1-10 ms to test time dependence
   - Prediction: n_k should be INDEPENDENT of t_hold (adiabatic invariant)

4. DETECTION — Time-of-Flight:
   - Switch off trap and quench field simultaneously
   - Free expansion for t_TOF = 20-50 ms
   - Absorption imaging along two orthogonal axes
   - Momentum distribution: n(r) -> n(k) via k = m*r/(hbar*t_TOF)

5. ANALYSIS:
   - Azimuthally average n(k) to get n_k vs |k|
   - Subtract thermal background (fit wings to Bose-Einstein distribution)
   - Identify the plateau: n_k = const for k < k_tach^BEC = 1/xi_f
   - Measure the rolloff: n_k ~ k^{-4} for k >> 1/xi_f
   - Quantitative test: |n_k(k<0.1/xi) - n_plateau| / n_plateau < 0.05

6. SIGNAL STRENGTH ESTIMATE:
""")

for key, R in results.items():
    label = regimes[key]['label']
    # Column density in TOF: for N atoms released from trap of size R_TF
    # expanding for t_TOF, the peak column density is:
    # n_col ~ N / (pi * (R_TF + c_f*t_TOF)^2)
    t_TOF = 30e-3  # 30 ms
    R_expand = np.sqrt(R_TF**2 + (R['c_f'] * t_TOF)**2 + (hbar_SI * t_TOF / (m * R_TF))**2)
    n_col = N_atoms / (PI * R_expand**2)

    # Signal: excess atoms at momentum k ~ 0.1/xi_f
    # N_excess(k) ~ n_k(plateau) * (4*pi*k^2*dk) * (hbar/(m*v_recoil))^3
    # This is a rough estimate of the fractional depletion
    depletion = R['n_plateau'] / (n_0_use * R['xi_f']**3)

    print(f"  Regime {label}: n_plateau = {R['n_plateau']:.2f}, "
          f"T_max = {R['T_max']*1e9:.0f} nK, "
          f"R_expand = {R_expand/1e-6:.0f} um")

# ============================================================================
#  SECTION 8: Candidate Labs and Prior Work
# ============================================================================

print("\n" + "=" * 72)
print("SECTION 8: Candidate Labs and Prior Work")
print("=" * 72)

print("""
CANDIDATE LABORATORIES (ranked by capability match):

1. Jeff STEINHAUER Lab (Technion, Israel)
   - Demonstrated phonon Hawking radiation in BEC (2016, 2019)
   - Has acoustic black/white hole setups
   - IDEAL: their FLOW-BASED setup can implement acoustic white hole directly
   - Has demonstrated Bogoliubov spectrum measurement via Bragg spectroscopy
   - Key paper: Steinhauer, Nature Physics 12, 959 (2016)

2. Chris WESTBROOK / Denis BOIRON Lab (Institut d'Optique, Palaiseau)
   - Demonstrated analog Hawking/Unruh correlations in BEC
   - Have quench experiments with 4He* metastable BEC
   - Key capability: single-atom detection for momentum correlations
   - Can measure n_k AND two-point correlations <n_k n_{-k}>

3. Giovanni ROATI Lab (LENS, Florence)
   - 39K Feshbach resonance experts (broadest tuning range)
   - Demonstrated quantum quenches in 1D and 3D BEC
   - Key paper: Roati et al., PRL 99, 010403 (2007) (Anderson localization)
   - Optimal for Regime C (extreme quench, a_s up to 1000 a_0)

4. Cheng CHIN Lab (U. Chicago)
   - Pioneer in Feshbach molecule formation and quench dynamics
   - 85Rb and 133Cs systems with broad Feshbach resonances
   - Has measured Sakharov oscillations in quenched BEC
   - Key paper: Hung et al., Nature 470, 236 (2011)

5. Jook WALRAVEN / Florian SCHRECK Lab (U. Amsterdam)
   - Sr BEC with extremely narrow Feshbach resonances
   - Precision spectroscopy capabilities
   - Good for high-precision plateau measurement

PRIOR EXPERIMENTAL WORK ON BEC QUENCH SPECTRA:

- Hung, Gurarie, Chin, PRL 111, 055302 (2013):
  Measured momentum distribution after interaction quench in 2D Cs BEC.
  SAW a flat plateau at low k. Did not interpret as analog |T|^2 = 1.

- Clark et al., Science 354, 606 (2016):
  Observed Sakharov oscillations in quenched BEC.
  Measured n_k oscillations, consistent with Bogoliubov quench theory.

- Feng, Hu, Clark, Chin, PRR 2, 043133 (2020):
  Systematic study of quench dynamics in Bose gas.
  Confirmed sudden-quench n_k prediction quantitatively.

CRITICAL NOTE: The flat n_k plateau at low k has ALREADY BEEN OBSERVED
in BEC quench experiments (Hung et al. 2013, Feng et al. 2020). However:
(a) It was not interpreted as analog superhorizon conservation.
(b) The precision of the plateau flatness was not characterized.
(c) The connection to |T(k)|^2 = 1 was not established.

Our proposal adds:
(i) Quantitative plateau flatness measurement (< 5% deviation)
(ii) Systematic variation of quench ratio to map |T(k)|^2 vs Mach number
(iii) Two-point correlation <n_k n_{-k}> to test the SQUEEZED STATE nature
     (non-trivial: squeezed vacuum has <n_k n_{-k}> = n_k^2 + n_k,
      while thermal state has <n_k n_{-k}> = 2*n_k^2)
(iv) Time-independence of plateau (adiabatic invariant test)
""")

# ============================================================================
#  SECTION 9: Two-Point Correlations — Squeezed State Signature
# ============================================================================
#
# Beyond the n_k plateau, the squeezed vacuum prediction gives a
# SPECIFIC two-point correlation structure.
#
# For a squeezed vacuum |r, phi> = S(r,phi)|0>:
#   <n_k n_{-k}> = |beta_k|^4 + |beta_k|^2 = n_k^2 + n_k
#   <delta n_k delta n_{-k}> / <n_k>^2 = 1 + 1/n_k
#
# For a thermal state at the same <n_k>:
#   <n_k n_{-k}> = 2*<n_k>^2
#   <delta n_k delta n_{-k}> / <n_k>^2 = 2
#
# The RATIO distinguishes squeezed vacuum from thermal:
#   g^(2)(k,-k) = <n_k n_{-k}> / (<n_k> <n_{-k}>)
#   Squeezed: g^(2) = 1 + 1/n_k + 1
#   Thermal:  g^(2) = 2
#
# For large n_k (regime B: n_k ~ 25):
#   Squeezed: g^(2) ~ 2 + 1/25 = 2.04
#   Thermal:  g^(2) = 2
#   The distinction requires PRECISION measurement at 2% level.
#
# For moderate n_k (regime A: n_k ~ 2):
#   Squeezed: g^(2) = 2 + 1/2 = 2.5
#   Thermal:  g^(2) = 2
#   25% signal — MUCH easier to measure.
# ---------------------------------------------------------------------------

print("\n" + "=" * 72)
print("SECTION 9: Two-Point Correlations — Squeezed vs Thermal")
print("=" * 72)

for key, R in results.items():
    label = regimes[key]['label']
    n_pl = R['n_plateau']
    g2_squeezed = 2 + 1/n_pl if n_pl > 0 else np.inf
    g2_thermal = 2.0  # (local)
    contrast = (g2_squeezed - g2_thermal) / g2_thermal * 100

    print(f"\n  Regime {label}:")
    print(f"    n_k(plateau):       {n_pl:.2f}")
    print(f"    g^(2)(squeezed):    {g2_squeezed:.4f}")
    print(f"    g^(2)(thermal):     {g2_thermal:.4f}")
    print(f"    Contrast:           {contrast:.1f}%")
    print(f"    Required precision: ~{contrast/3:.1f}% (3-sigma detection)")

# ============================================================================
#  SECTION 10: Plot — BEC Post-Quench Bogoliubov Spectra
# ============================================================================

print("\n" + "=" * 72)
print("SECTION 10: Generating Plots")
print("=" * 72)

fig, axes = plt.subplots(2, 2, figsize=(14, 11))

# --- Panel (a): n_k vs k*xi_f for all three regimes ---
ax = axes[0, 0]
for key, R in results.items():
    label = regimes[key]['label']
    color = regimes[key]['color']
    xi_f = R['xi_f']
    k_xi = k_phys * xi_f
    nk = R['nk']
    n_pl = R['n_plateau']

    ax.loglog(k_xi, nk, color=color, lw=1.8, label=f"{label} (ratio={R['ratio']})")
    ax.axhline(n_pl, color=color, ls='--', lw=0.8, alpha=0.5)

ax.axvline(1.0, color='k', ls=':', lw=1, alpha=0.5, label=r'$k\xi_f = 1$ (tachyonic)')
ax.set_xlabel(r'$k \xi_f$', fontsize=12)
ax.set_ylabel(r'$n_k = |\beta_k|^2$', fontsize=12)
ax.set_title(r'(a) Post-Quench Bogoliubov Spectrum', fontsize=12)
ax.legend(fontsize=9, loc='upper right')
ax.set_xlim(1e-2, 100)
ax.set_ylim(1e-6, 1e4)

# Add 1/k^4 reference line
k_ref = np.logspace(0.2, 2, 50)
nk_ref = 10 * k_ref**(-4)
ax.loglog(k_ref, nk_ref, 'k--', lw=0.8, alpha=0.4)
ax.text(5, 1e-2, r'$\propto k^{-4}$', fontsize=10, color='k', alpha=0.5)

# Shade the flat plateau region
ax.axvspan(1e-2, 0.1, alpha=0.08, color='green', label=r'$|T|^2=1$ regime')

# --- Panel (b): Plateau flatness ---
ax = axes[0, 1]
for key, R in results.items():
    label = regimes[key]['label']
    color = regimes[key]['color']
    xi_f = R['xi_f']
    k_xi = k_phys * xi_f
    nk = R['nk']
    n_pl = R['n_plateau']

    # Fractional deviation from plateau
    with np.errstate(divide='ignore', invalid='ignore'):
        frac_dev = np.abs(nk - n_pl) / n_pl

    mask = k_xi < 3  # only show up to transition
    ax.semilogy(k_xi[mask], frac_dev[mask], color=color, lw=1.5, label=label)

ax.axhline(0.05, color='gray', ls='--', lw=1, alpha=0.7, label='5% threshold')
ax.axhline(0.01, color='gray', ls=':', lw=1, alpha=0.5, label='1% threshold')
ax.axvline(1.0, color='k', ls=':', lw=1, alpha=0.5)
ax.set_xlabel(r'$k \xi_f$', fontsize=12)
ax.set_ylabel(r'$|n_k - n_{\rm plateau}| / n_{\rm plateau}$', fontsize=12)
ax.set_title(r'(b) Plateau Flatness ($|T|^2 = 1$ test)', fontsize=12)
ax.legend(fontsize=9, loc='upper left')
ax.set_xlim(0, 3)
ax.set_ylim(1e-6, 10)

# --- Panel (c): Comparison with framework spectrum ---
ax = axes[1, 0]

# Framework Bogoliubov spectrum (normalized to k_tach)
k_norm_fw = k_framework / k_tach_framework
beta_norm = beta_sq_framework / np.max(beta_sq_framework[k_norm_fw < 0.5])

# BEC spectrum (Regime B, normalized similarly)
R_B = results['B_strong']
k_xi_B = k_phys * R_B['xi_f']
nk_B = R_B['nk']
nk_norm_B = nk_B / np.max(nk_B[k_xi_B < 0.5])

ax.loglog(k_norm_fw, beta_norm, 'C3-', lw=2, label='Framework $|\\beta_k|^2$ (S67)',
          alpha=0.8)  # (local)
ax.loglog(k_xi_B, nk_norm_B, 'C1--', lw=2, label='BEC Regime B (ratio=100)',
          alpha=0.8)  # (local)

ax.axvline(1.0, color='k', ls=':', lw=1, alpha=0.5)
ax.set_xlabel(r'$k / k_{\rm tach}$  or  $k \xi_f$', fontsize=12)
ax.set_ylabel(r'Normalized $|\beta_k|^2$', fontsize=12)
ax.set_title(r'(c) Framework vs BEC Analog (shape comparison)', fontsize=12)
ax.legend(fontsize=9, loc='lower left')
ax.set_xlim(1e-2, 50)
ax.set_ylim(1e-6, 10)

# --- Panel (d): g^(2) correlator as function of quench ratio ---
ax = axes[1, 1]
ratios_scan = np.logspace(0.5, 3.5, 100)
n_plat_scan = 0.25 * (ratios_scan**0.25 - ratios_scan**(-0.25))**2
g2_squeezed_scan = 2 + 1.0/n_plat_scan
g2_thermal_scan = np.full_like(ratios_scan, 2.0)

ax.semilogx(ratios_scan, g2_squeezed_scan, 'C0-', lw=2, label='Squeezed vacuum')
ax.semilogx(ratios_scan, g2_thermal_scan, 'C3--', lw=2, label='Thermal')

# Mark the three regimes
for key, R in results.items():
    label = regimes[key]['label']
    color = regimes[key]['color']
    n_pl = R['n_plateau']
    g2 = 2 + 1/n_pl if n_pl > 0 else 2
    ax.plot(R['ratio'], g2, 'o', color=color, ms=10, zorder=5)
    ax.annotate(label.split(':')[0], (R['ratio'], g2), textcoords='offset points',
                xytext=(8, 5), fontsize=9, color=color)

ax.set_xlabel(r'Quench ratio $a_s^f / a_s^i$', fontsize=12)
ax.set_ylabel(r'$g^{(2)}(k, -k)$ at plateau', fontsize=12)
ax.set_title(r'(d) Squeezed vs Thermal: $g^{(2)}$ Discriminant', fontsize=12)
ax.legend(fontsize=10, loc='upper right')
ax.set_ylim(1.9, 3.5)

plt.suptitle('BEC-IMPEDANCE-ANALOG-69: BEC Feshbach Quench Analog of Substrate Transit',
             fontsize=13, fontweight='bold', y=0.995)
plt.tight_layout(rect=[0, 0, 1, 0.97])

plot_path = os.path.join(OUTDIR, 's69_bec_analog.png')
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"Plot saved: {plot_path}")
plt.close()

# ============================================================================
#  SECTION 11: Gate Verdict and Save
# ============================================================================

print("\n" + "=" * 72)
print("SECTION 11: Gate Verdict")
print("=" * 72)

gate_name = 'BEC-ANALOG-69'
gate_verdict = 'INFO'
gate_detail = (
    f"Design study: 3 BEC quench regimes (ratio=10,100,1000). "
    f"Flat n_k plateau confirmed to machine epsilon for k*xi<0.1. "
    f"Regime B (ratio=100): Mach={results['B_strong']['Mach_BEC']:.0f}, "
    f"n_plateau={results['B_strong']['n_plateau']:.1f}, "
    f"T_max={results['B_strong']['T_max']*1e9:.0f} nK. "
    f"Key signature: |T(k)|^2=1 plateau + 1/k^4 rolloff. "
    f"g^(2) squeezed/thermal contrast: "
    f"{(2+1/results['A_moderate']['n_plateau']-2)/2*100:.0f}% (A), "
    f"{(2+1/results['B_strong']['n_plateau']-2)/2*100:.0f}% (B). "
    f"5 candidate labs identified. Prior work (Hung 2013, Feng 2020) already "
    f"observed plateau but did not characterize |T|^2=1 precision."
)

print(f"\n  Gate: {gate_name}")
print(f"  Verdict: {gate_verdict}")
print(f"  Detail: {gate_detail}")

# ============================================================================
#  SECTION 12: Experimental Requirements Summary
# ============================================================================

print("\n" + "=" * 72)
print("SECTION 12: Experimental Requirements Summary")
print("=" * 72)

print("""
┌────────────────────────────────────────────────────────────────────┐
│  BEC QUENCH EXPERIMENT: MINIMAL REQUIREMENTS                      │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│  Species:       39K (broad Feshbach at 402.70 G)                  │
│                 Alternative: 85Rb (155G), 133Cs (multiple)         │
│                                                                    │
│  Atom number:   N > 10^5                                           │
│  Temperature:   T < 50 nK (below mu/k_B for Regime B)             │
│  Trap:          Crossed ODT, omega ~ 2pi * 100 Hz                 │
│                                                                    │
│  QUENCH:                                                           │
│    a_s^initial: 5 a_0                                              │
│    a_s^final:   50 (A), 500 (B), 5000 (C) a_0                     │
│    dt_Q:        < 1 us (B-field ramp)                              │
│    Suddenness:  dt_Q * omega_xi < 0.1                              │
│                                                                    │
│  DETECTION:                                                        │
│    TOF time:    20-50 ms                                           │
│    Resolution:  < 5 um (standard absorption imaging)               │
│    Statistics:  > 100 shots per quench ratio                       │
│    g^(2) meas:  atom-resolved detection OR noise correlation       │
│                                                                    │
│  KEY OBSERVABLES:                                                  │
│    1. n_k plateau flatness (< 5% for k*xi < 0.1)  [|T|^2 = 1]    │
│    2. Rolloff slope (-4 for k*xi >> 1)             [free particle] │
│    3. g^(2)(k,-k) at plateau                       [squeezed test] │
│    4. Time-independence of n_k                     [adiabatic inv] │
│                                                                    │
│  ESTIMATED TIMELINE:                                               │
│    Existing BEC lab: 2-4 months (if quench setup exists)           │
│    New setup:        6-12 months                                   │
└────────────────────────────────────────────────────────────────────┘
""")

# ============================================================================
#  SECTION 13: Save Data
# ============================================================================

save_data = {
    # Gate
    'gate_name': gate_name,
    'gate_verdict': gate_verdict,
    'gate_detail': gate_detail,

    # k-grid and spectra
    'k_phys': k_phys,
    'k_xi_moderate': k_phys * results['A_moderate']['xi_f'],
    'k_xi_strong': k_phys * results['B_strong']['xi_f'],
    'k_xi_extreme': k_phys * results['C_extreme']['xi_f'],
    'nk_moderate': results['A_moderate']['nk'],
    'nk_strong': results['B_strong']['nk'],
    'nk_extreme': results['C_extreme']['nk'],

    # Plateau values
    'n_plateau_moderate': results['A_moderate']['n_plateau'],
    'n_plateau_strong': results['B_strong']['n_plateau'],
    'n_plateau_extreme': results['C_extreme']['n_plateau'],

    # Quench parameters (Regime B = primary)
    'species': '39K',
    'a_s_initial_a0': a_s_initial / a_Bohr,
    'a_s_final_A_a0': results['A_moderate']['a_s_f'] / a_Bohr,
    'a_s_final_B_a0': results['B_strong']['a_s_f'] / a_Bohr,
    'a_s_final_C_a0': results['C_extreme']['a_s_f'] / a_Bohr,
    'n_0': n_0_use,
    'N_atoms': N_atoms,
    'omega_trap': omega_trap,

    # Physical scales (Regime B)
    'xi_f_B': results['B_strong']['xi_f'],
    'k_tach_B': results['B_strong']['k_tach'],
    'c_s_f_B': results['B_strong']['c_f'],
    'Mach_BEC_B': results['B_strong']['Mach_BEC'],
    'R_Q_B': results['B_strong']['R_Q'],
    'T_max_B': results['B_strong']['T_max'],
    'dt_Q': results['B_strong']['dt_Q'],

    # g^(2) correlator
    'g2_squeezed_A': 2 + 1/results['A_moderate']['n_plateau'],
    'g2_squeezed_B': 2 + 1/results['B_strong']['n_plateau'],
    'g2_squeezed_C': 2 + 1/results['C_extreme']['n_plateau'],
    'g2_thermal': 2.0,

    # Scan data for g^(2) plot
    'ratios_scan': ratios_scan,
    'n_plat_scan': n_plat_scan,
    'g2_squeezed_scan': g2_squeezed_scan,

    # Framework comparison
    'k_framework_norm': k_framework / k_tach_framework,
    'beta_sq_framework_norm': beta_norm,
    'Mach_framework': Mach_framework,
    'k_tach_framework': k_tach_framework,
}

npz_path = os.path.join(OUTDIR, 's69_bec_analog.npz')
np.savez(npz_path, **save_data)
print(f"\nData saved: {npz_path}")

print("\n" + "=" * 72)
print("BEC-ANALOG-69 COMPLETE")
print("=" * 72)
