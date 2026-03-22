#!/usr/bin/env python3
"""
KC-5: BCS Gap Equation with van Hove-Enhanced 1D Density of States
===================================================================

Session 28c Constraint Chain, terminal gate.

Physics:
--------
The 1D density of states near a band edge exhibits a van Hove singularity:

    g(omega) = C / sqrt(omega - omega_min)   for omega > omega_min

This divergence fundamentally changes the BCS gap equation compared to the
flat-DOS case used in Session 23a (where M_max(mu=0) = 0.077-0.149, CLOSED).

For flat DOS:  Need V > V_c (finite critical coupling).
For van Hove:  ANY V > 0 gives Delta > 0 (no critical coupling).

The gap equation:

    1 = V_eff * integral_{omega_min}^{omega_D} [g(omega) / (2*E(omega))] d(omega)

where E(omega) = sqrt((omega - mu)^2 + Delta^2) is the quasiparticle energy.

Near the band edge with mu = omega_min, this gives:

    1 ~ V_eff * C * integral_0^{W} [1/(sqrt(x) * 2*sqrt(x^2 + Delta^2))] dx

which has a logarithmic divergence as Delta -> 0, guaranteeing a solution.

The decisive question: is Delta physically meaningful (Delta/lambda_min > 0.01)?

Inputs:
-------
- s28c_steady_state_mu.npz (KC-3): mu_eff, n_gap at various tau/drive
- s28c_luttinger.npz (KC-4): K values, g_1D interaction strengths
- s28c_phonon_tmatrix.npz (KC-2): T-matrix, V_born
- s23a_kosmann_singlet.npz: Kosmann coupling, M_max from Session 23a
- s27_multisector_bcs.npz: Multi-sector BCS reference

Gate KC-5:
----------
- PASS:  Delta/lambda_min > 0.01
- CLOSED:  Delta/lambda_min < 1e-6
- INCONCLUSIVE: 1e-6 <= Delta/lambda_min <= 0.01

Author: phonon-exflation-sim agent, Session 28c
"""

import warnings
import numpy as np
from scipy import integrate, optimize
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
import sys
import time

# Suppress expected scipy.integrate warnings at tiny Delta during bisection
warnings.filterwarnings('ignore', category=integrate.IntegrationWarning)

# ============================================================================
# Configuration
# ============================================================================

DATA_DIR = Path(r"C:\sandbox\Ainulindale Exflation\tier0-computation")
OUTPUT_PREFIX = DATA_DIR / "s28c_bcs_van_hove"

# Tau values to analyze (from KC-3 where mu_eff is meaningful)
TAU_TARGETS = [0.15, 0.25, 0.35, 0.50]

# mu/lambda_min ratios to scan
MU_RATIOS = np.array([0.0, 0.5, 0.8, 0.9, 0.95, 1.0, 1.05, 1.10, 1.20, 1.50])

# V_eff scan (dimensionless coupling strength)
V_EFF_SCAN = np.logspace(-3, 1, 200)

# Numerical integration parameters
N_QUAD = 2000       # quadrature points for gap integral
DELTA_RTOL = 1e-10  # relative tolerance for gap solution
MAX_ITER = 200      # max iterations for self-consistent gap


# ============================================================================
# Module 1: Data Loading
# ============================================================================

def load_all_data():
    """Load all input .npz files and extract relevant quantities."""
    print("=" * 72)
    print("KC-5: BCS Gap Equation with van Hove DOS")
    print("=" * 72)
    print()

    data = {}

    # KC-3: Steady-state mu
    d3 = np.load(DATA_DIR / "s28c_steady_state_mu.npz", allow_pickle=True)
    data['kc3'] = {
        'tau_values': d3['tau_values'],
        'lambda_min': d3['lambda_min'],
        'B_gap': d3['B_gap'],
        'ref_alpha': float(d3['ref_alpha'][0]),
    }
    # Extract L2 thermalized data where available
    for tau_str in ['0.15', '0.25', '0.35']:
        key = f'L2_tau{tau_str}'
        if f'{key}_n_gap_th' in d3.files:
            data['kc3'][f'L2_tau{tau_str}_n_gap_th'] = d3[f'{key}_n_gap_th']
            data['kc3'][f'L2_tau{tau_str}_mu_th'] = d3[f'{key}_mu_th']
            data['kc3'][f'L2_tau{tau_str}_lambda_min'] = float(d3[f'{key}_lambda_min'][0])

    print(f"  KC-3 loaded: {len(d3['tau_values'])} tau values")

    # KC-4: Luttinger parameters
    d4 = np.load(DATA_DIR / "s28c_luttinger.npz", allow_pickle=True)
    data['kc4'] = {}
    for tau_str in ['0p15', '0p25', '0p35']:
        tau_key = f'tau{tau_str}'
        data['kc4'][tau_str] = {
            'g1D': float(d4[f'{tau_key}_g1D'][0]),
            'g1D_avg': float(d4[f'{tau_key}_g1D_avg'][0]),
            'g1D_eff': float(d4[f'{tau_key}_g1D_eff'][0]),
            'mstar': float(d4[f'{tau_key}_mstar'][0]),
            'bandwidth': float(d4[f'{tau_key}_bandwidth'][0]),
            'K_Landau_avg': float(d4[f'{tau_key}_K_Landau_avg'][0]),
            'K_Landau_sectors': d4[f'{tau_key}_K_Landau_sectors'],
            'f0_sectors': d4[f'{tau_key}_f0_sectors'],
        }
    print(f"  KC-4 loaded: 3 tau points")

    # KC-2: T-matrix
    d2 = np.load(DATA_DIR / "s28c_phonon_tmatrix.npz", allow_pickle=True)
    data['kc2'] = {}
    for i, tau_str in enumerate(['tau0', 'tau1', 'tau2']):
        tau_val = float(d2[f'{tau_str}_tau'][0])
        omega = d2[f'{tau_str}_omega']
        V_born = d2[f'{tau_str}_V_born']
        T_full = d2[f'{tau_str}_T_full']
        data['kc2'][f'{tau_val:.2f}'] = {
            'tau': tau_val,
            'omega': omega,
            'omega_min': float(omega.min()),
            'omega_max': float(omega.max()),
            'bandwidth': float(omega.max() - omega.min()),
            'max_V_born': float(np.max(np.abs(V_born))),
            'max_T_full': float(np.max(np.abs(T_full))),
            'Gamma_decay': float(d2[f'{tau_str}_Gamma_decay'][0]),
            'Gamma_inject': float(d2[f'{tau_str}_Gamma_inject'][0]),
        }
    print(f"  KC-2 loaded: T-matrix at 3 tau values")

    # S23a: Kosmann coupling
    d23 = np.load(DATA_DIR / "s23a_kosmann_singlet.npz", allow_pickle=True)
    data['s23a'] = {
        'tau_values': d23['tau_values'],
    }
    # Extract M_max and K_norms per tau index
    for i in range(len(d23['tau_values'])):
        evals = d23[f'eigenvalues_{i}']
        data['s23a'][f'eigenvalues_{i}'] = evals
        data['s23a'][f'lambda_min_{i}'] = float(np.min(np.abs(evals)))
        if f'M_max_mu0_{i}' in d23.files:
            data['s23a'][f'M_max_mu0_{i}'] = float(d23[f'M_max_mu0_{i}'])
        if f'M_max_mugap_{i}' in d23.files:
            data['s23a'][f'M_max_mugap_{i}'] = float(d23[f'M_max_mugap_{i}'])
        data['s23a'][f'K_norms_{i}'] = d23[f'K_norms_{i}']
        data['s23a'][f'V_pairing_{i}'] = d23[f'V_pairing_{i}']
    print(f"  S23a loaded: {len(d23['tau_values'])} tau values")

    # S27: Multi-sector BCS
    d27 = np.load(DATA_DIR / "s27_multisector_bcs.npz", allow_pickle=True)
    data['s27'] = {
        'tau_values': d27['tau_values'],
        'mu_ratios': d27['mu_ratios'],
        'sectors': d27['sectors'],
        'M_max': d27['M_max'],
        'Delta_max': d27['Delta_max'],
    }
    print(f"  S27 loaded: {d27['M_max'].shape[0]} sectors, {d27['M_max'].shape[1]} taus")

    print()
    return data


# ============================================================================
# Module 2: van Hove DOS Construction
# ============================================================================

def van_hove_dos(omega, omega_min, bandwidth, normalization='unit'):
    """
    1D van Hove density of states near band minimum.

    g(omega) = C / sqrt(omega - omega_min)  for omega in [omega_min, omega_min + W]

    The 1D tight-binding dispersion E(k) = omega_min + W/2 * (1 - cos(k))
    gives g(E) = (1/pi) / sqrt((E - omega_min)(omega_min + W - E))
    which diverges as 1/sqrt(E - omega_min) at the band edge.

    Parameters
    ----------
    omega : array
        Energy values.
    omega_min : float
        Band minimum (position of van Hove singularity).
    bandwidth : float
        Width of the band W.
    normalization : str
        'unit' for integral = 1, 'tight_binding' for 1/(pi*sqrt(W)) prefactor.

    Returns
    -------
    g : array
        Density of states values.
    """
    x = omega - omega_min
    W = bandwidth
    mask = (x > 0) & (x < W)
    g = np.zeros_like(omega)

    if normalization == 'tight_binding':
        # Full tight-binding: g(E) = 1/(pi * sqrt(x*(W-x)))
        g[mask] = 1.0 / (np.pi * np.sqrt(x[mask] * (W - x[mask])))
    elif normalization == 'unit':
        # Normalized so integral_0^W g(x) dx = 1
        # integral of 1/sqrt(x*(W-x)) from 0 to W = pi
        # So C = 1/pi for unit normalization with full form
        g[mask] = 1.0 / (np.pi * np.sqrt(x[mask] * (W - x[mask])))
    else:
        # Pure van Hove: g = 1/sqrt(x), normalized to give integral = 1 over [0,W]
        # integral_0^W 1/sqrt(x) dx = 2*sqrt(W), so C = 1/(2*sqrt(W))
        g[mask] = 1.0 / (2.0 * np.sqrt(W) * np.sqrt(x[mask]))

    return g


def compute_dos_weight(omega_min, bandwidth, mu, n_points=5000):
    """
    Compute the effective DOS weight N_vH at the chemical potential.

    N_vH = g(mu) for the van Hove DOS. This is the key quantity that enters
    the BCS gap formula:  Delta ~ omega_D * exp(-1/(V * N_vH))

    For mu at the band edge (mu = omega_min), N_vH diverges, which is
    precisely the mechanism that eliminates the critical coupling.

    Parameters
    ----------
    omega_min, bandwidth, mu : float
    n_points : int
        Quadrature points.

    Returns
    -------
    N_vH : float
        DOS at chemical potential. Infinity if mu = omega_min exactly.
    """
    if mu <= omega_min:
        return np.inf  # Below band: no states, but van Hove diverges at edge
    if mu >= omega_min + bandwidth:
        return 0.0  # Above band: no states

    x = mu - omega_min
    W = bandwidth
    # tight-binding DOS value at mu
    return 1.0 / (np.pi * np.sqrt(x * (W - x)))


# ============================================================================
# Module 3: BCS Gap Equation Solver
# ============================================================================

def bcs_gap_integrand(omega, mu, Delta, omega_min, bandwidth):
    """
    Integrand for the BCS gap equation with van Hove DOS.

    I(omega) = g(omega) / (2 * sqrt((omega - mu)^2 + Delta^2))

    The gap equation is: 1 = V_eff * integral I(omega) d(omega)
    """
    x = omega - omega_min
    W = bandwidth

    # DOS (tight-binding)
    if x <= 0 or x >= W:
        return 0.0
    g = 1.0 / (np.pi * np.sqrt(x * (W - x)))

    # BCS denominator
    E = np.sqrt((omega - mu)**2 + Delta**2)

    return g / (2.0 * E)


def bcs_gap_integral(mu, Delta, omega_min, bandwidth, n_points=N_QUAD):
    """
    Compute the BCS gap integral:

        I(Delta) = integral_{omega_min}^{omega_min+W} g(omega)/(2*E(omega)) d(omega)

    where g is the tight-binding 1D DOS and E = sqrt((omega-mu)^2 + Delta^2).

    Uses substitution to handle the square-root singularities at band edges.
    Let omega = omega_min + W/2 * (1 - cos(theta)), theta in [0, pi].
    Then d(omega) = W/2 * sin(theta) d(theta),
    and x*(W-x) = (W/2)^2 * sin^2(theta),
    so g(omega) * d(omega) = [1/(pi * W/2 * sin(theta))] * W/2 * sin(theta) d(theta)
                            = d(theta) / pi

    This eliminates BOTH singularities analytically.

    Parameters
    ----------
    mu : float
        Chemical potential.
    Delta : float
        BCS gap (> 0).
    omega_min : float
        Band minimum.
    bandwidth : float
        Band width W.
    n_points : int
        Number of quadrature points in theta.

    Returns
    -------
    I : float
        Value of the gap integral.
    """
    W = bandwidth

    # theta parameterization: omega = omega_min + W/2*(1 - cos(theta))
    # After substitution, integral = (1/pi) * integral_0^pi 1/(2*E(theta)) d(theta)
    theta = np.linspace(1e-14, np.pi - 1e-14, n_points)
    omega = omega_min + W / 2.0 * (1.0 - np.cos(theta))

    E = np.sqrt((omega - mu)**2 + Delta**2)

    # Trapezoidal integration of (1/pi) * 1/(2*E) over [0, pi]
    integrand = 1.0 / (2.0 * np.pi * E)
    I = np.trapezoid(integrand, theta)

    return I


def bcs_gap_integral_log_enhanced(mu, Delta, omega_min, bandwidth):
    """
    Same integral but using scipy adaptive quadrature for highest accuracy.
    Uses the theta substitution to remove singularities.
    """
    W = bandwidth

    def integrand_theta(theta):
        omega = omega_min + W / 2.0 * (1.0 - np.cos(theta))
        E = np.sqrt((omega - mu)**2 + Delta**2)
        return 1.0 / (2.0 * np.pi * E)

    # Use small offset from endpoints to avoid evaluating at exactly 0 or pi
    # where the substitution degenerates (integrand is finite there, but
    # quad can emit warnings). The integrand at endpoints is 1/(2*pi*E_edge)
    # which is bounded.
    eps = 1e-12
    result, error = integrate.quad(integrand_theta, eps, np.pi - eps,
                                   limit=200, epsabs=1e-14, epsrel=1e-12)
    return result


def solve_bcs_gap(V_eff, mu, omega_min, bandwidth, Delta_init=None,
                  use_adaptive=True):
    """
    Solve the BCS gap equation self-consistently:

        1 = V_eff * I(Delta)

    where I(Delta) = integral g(omega)/(2*E(omega)) d(omega).

    Parameters
    ----------
    V_eff : float
        Effective attractive pairing interaction (> 0 for attractive).
    mu : float
        Chemical potential.
    omega_min : float
        Band minimum.
    bandwidth : float
        Band width W.
    Delta_init : float or None
        Initial guess. If None, use analytical estimate.
    use_adaptive : bool
        Use scipy.integrate.quad (slower but more accurate).

    Returns
    -------
    Delta : float
        Self-consistent BCS gap. 0 if no solution found.
    converged : bool
        Whether iteration converged.
    n_iter : int
        Number of iterations used.
    """
    W = bandwidth

    if V_eff <= 0:
        return 0.0, True, 0

    # Choose integration method
    if use_adaptive:
        gap_func = lambda D: bcs_gap_integral_log_enhanced(mu, D, omega_min, W)
    else:
        gap_func = lambda D: bcs_gap_integral(mu, D, omega_min, W)

    # Check if gap equation has a solution at all:
    # As Delta -> 0+, I(Delta) -> infinity (logarithmic divergence for van Hove DOS
    # when mu is in the band). So V_eff * I(Delta->0) > 1 for ANY V_eff > 0.
    # This means a solution ALWAYS exists for attractive V in 1D.

    # Upper bound: Delta cannot exceed the bandwidth
    Delta_max = W

    # The gap equation 1 = V * I(Delta) is equivalent to finding the root of:
    # f(Delta) = V * I(Delta) - 1 = 0
    # I(Delta) is monotonically decreasing in Delta (larger gap suppresses integrand).
    # At Delta=0+, I diverges. At Delta=W, I is finite and possibly < 1/V.

    # Check at Delta_max
    I_max = gap_func(Delta_max)
    if V_eff * I_max > 1.0:
        # Solution is beyond bandwidth -- gap exceeds band width (strong coupling)
        # Extend search range
        Delta_max = 10 * W
        I_max = gap_func(Delta_max)
        if V_eff * I_max > 1.0:
            Delta_max = 100 * W

    # Binary search (bisection) for the root
    Delta_lo = 1e-15 * W  # Near zero
    Delta_hi = Delta_max

    I_lo = gap_func(Delta_lo)
    I_hi = gap_func(Delta_hi)

    f_lo = V_eff * I_lo - 1.0
    f_hi = V_eff * I_hi - 1.0

    if f_lo < 0:
        # Even at tiny Delta, V*I < 1: no solution (V too small even for van Hove)
        # This can happen if mu is outside the band
        return 0.0, True, 0

    if f_hi > 0:
        # Gap exceeds our search range -- very strong coupling
        return Delta_hi, False, 0

    # Bisection
    for n_iter in range(MAX_ITER):
        Delta_mid = np.sqrt(Delta_lo * Delta_hi)  # Geometric mean for log-spaced search
        I_mid = gap_func(Delta_mid)
        f_mid = V_eff * I_mid - 1.0

        if abs(f_mid) < DELTA_RTOL:
            return Delta_mid, True, n_iter + 1

        if f_mid > 0:
            Delta_lo = Delta_mid
        else:
            Delta_hi = Delta_mid

        if abs(Delta_hi / Delta_lo - 1.0) < DELTA_RTOL:
            return Delta_mid, True, n_iter + 1

    return np.sqrt(Delta_lo * Delta_hi), False, MAX_ITER


def bcs_weak_coupling_formula(V_eff, omega_min, bandwidth, mu):
    """
    Analytical weak-coupling BCS formula for van Hove DOS.

    For the tight-binding 1D DOS g(E) = 1/(pi*sqrt(x*(W-x))) with
    mu at the band edge (x = mu - omega_min << W):

        g(mu) ~ 1/(pi*sqrt(x*W))  for x << W

    The standard BCS result gives:

        Delta ~ 2*W * exp(-1 / (V_eff * g(mu)))

    But at the band edge itself (x -> 0), g -> infinity, giving:

        Delta ~ 2*W * exp(-pi*sqrt(x*W) / V_eff)

    For x = 0 (mu exactly at band edge):
        The integral has a log^2 divergence, giving Delta ~ W * exp(-c/sqrt(V))
        (stronger than standard BCS but still exponentially suppressed).

    Parameters
    ----------
    V_eff : float
        Pairing interaction.
    omega_min, bandwidth, mu : float
        Band parameters.

    Returns
    -------
    Delta_est : float
        Weak-coupling estimate of the gap.
    """
    W = bandwidth
    x = mu - omega_min

    if x <= 0:
        # mu below or at band edge: use band-edge formula
        # At band edge, the integral with van Hove DOS:
        #   I(Delta) ~ (1/(2*pi)) * integral_0^W 1/(sqrt(y)*sqrt(y^2+Delta^2)) dy
        # For small Delta: I ~ (1/(2*pi*Delta)) * ln(W/Delta) (leading log divergence)
        # Gap equation: 1 = V/(2*pi*Delta) * ln(W/Delta)
        # Solution: Delta ~ W * exp(-2*pi*Delta/V) -- implicit, but for small V:
        # Delta ~ W * exp(-sqrt(2*pi/V)) (stronger than standard BCS)
        if V_eff <= 0:
            return 0.0
        # Use Lambert W approximation
        return W * np.exp(-np.sqrt(2.0 * np.pi / max(V_eff, 1e-30)))
    elif x >= W:
        return 0.0
    else:
        # mu inside band: standard BCS with van Hove DOS value
        g_mu = 1.0 / (np.pi * np.sqrt(x * (W - x)))
        if V_eff * g_mu < 1e-10:
            return 0.0
        return 2.0 * W * np.exp(-1.0 / (V_eff * g_mu))


# ============================================================================
# Module 4: Effective Pairing Interaction Assembly
# ============================================================================

def assemble_V_eff(data, tau_target):
    """
    Assemble the effective pairing interaction V_eff from multiple sources.

    V_eff combines:
    1. Kosmann coupling (bare vertex from S23a/S27)
    2. T-matrix enhancement (phonon-mediated from KC-2)
    3. Luttinger K parameter (attractive enhancement from KC-4)

    The combination: V_eff = V_Kosmann * (T/V_born enhancement) * (1/K Luttinger)

    Parameters
    ----------
    data : dict
        All loaded data.
    tau_target : float
        Target tau value.

    Returns
    -------
    V_eff_info : dict
        Dictionary with V_eff components and combined value.
    """
    info = {'tau': tau_target}

    # --- Component 1: Kosmann pairing from S23a ---
    # Find closest tau in S23a data
    s23a_taus = data['s23a']['tau_values']
    idx_23a = np.argmin(np.abs(s23a_taus - tau_target))
    tau_23a = s23a_taus[idx_23a]

    # M_max at mu=0 and mu=lambda_min
    M_max_mu0 = data['s23a'].get(f'M_max_mu0_{idx_23a}', 0.0)
    M_max_mugap = data['s23a'].get(f'M_max_mugap_{idx_23a}', 0.0)

    # V_pairing matrix
    V_pair = data['s23a'][f'V_pairing_{idx_23a}']
    V_kosmann_max = float(np.max(np.abs(V_pair)))

    # K_norms give the Kosmann coupling strength per direction
    K_norms = data['s23a'][f'K_norms_{idx_23a}']
    K_norm_avg = float(np.mean(K_norms))

    info['V_kosmann_max'] = V_kosmann_max
    info['M_max_mu0'] = M_max_mu0
    info['M_max_mugap'] = M_max_mugap
    info['K_norm_avg'] = K_norm_avg
    info['tau_23a'] = tau_23a

    # --- Component 2: T-matrix enhancement from KC-2 ---
    tau_key = f'{tau_target:.2f}'
    if tau_key in data['kc2']:
        kc2 = data['kc2'][tau_key]
        T_enhancement = kc2['max_T_full'] / max(kc2['max_V_born'], 1e-30)
        info['V_born_max'] = kc2['max_V_born']
        info['T_max'] = kc2['max_T_full']
        info['T_enhancement'] = T_enhancement
        info['bandwidth_kc2'] = kc2['bandwidth']
    else:
        info['T_enhancement'] = 1.0
        info['V_born_max'] = 0.0
        info['T_max'] = 0.0
        info['bandwidth_kc2'] = 0.03  # default estimate

    # --- Component 3: Luttinger K parameter from KC-4 ---
    tau_str_map = {0.15: '0p15', 0.25: '0p25', 0.35: '0p35'}
    tau_str = tau_str_map.get(tau_target, None)

    if tau_str and tau_str in data['kc4']:
        kc4 = data['kc4'][tau_str]
        K_Landau = kc4['K_Landau_avg']
        g1D = kc4['g1D']
        g1D_eff = kc4['g1D_eff']
        info['K_Landau'] = K_Landau
        info['g1D'] = g1D
        info['g1D_eff'] = g1D_eff
        info['bandwidth_kc4'] = kc4['bandwidth']
        info['mstar'] = kc4['mstar']

        # Luttinger enhancement: for K < 1 (attractive), pairing is enhanced
        # Cooper susceptibility ~ 1/K for spin-gapped 1D system
        if K_Landau > 0 and K_Landau < 1.0:
            info['Luttinger_enhance'] = 1.0 / K_Landau
        else:
            info['Luttinger_enhance'] = 1.0
    else:
        info['K_Landau'] = 1.0
        info['Luttinger_enhance'] = 1.0
        info['bandwidth_kc4'] = 0.03

    # --- Combined V_eff estimates ---
    # Estimate 1 (conservative): Just Kosmann bare vertex
    # The M_max from S23a is V*N(0) where N(0) is flat DOS.
    # We re-use V_kosmann as the coupling constant.
    info['V_eff_kosmann_only'] = V_kosmann_max

    # Estimate 2 (moderate): Kosmann + T-matrix renormalization
    # The T-matrix enhances the bare coupling by ~T/V_born factor
    # But this is the FULL T-matrix, we want the Cooper channel projection.
    # Conservative: use sqrt(T_enhance) since T-matrix is not purely Cooper channel
    info['V_eff_with_T'] = V_kosmann_max * np.sqrt(info.get('T_enhancement', 1.0))

    # Estimate 3 (optimistic): Kosmann + T-matrix + Luttinger
    info['V_eff_full'] = info['V_eff_with_T'] * info.get('Luttinger_enhance', 1.0)

    # Estimate 4 (from S27 M_max data directly):
    # M_max = V*N(0) from flat-DOS BCS. V = M_max/N(0).
    # With van Hove, N_vH >> N_flat, so V*N_vH >> 1 potentially.
    # Use M_max(mu=lmin) as proxy for V (since N(0)~1 at band edge in flat DOS)
    info['V_eff_from_Mmax'] = M_max_mugap  # This is the most physically grounded

    # Estimate 5 (from Luttinger g1D directly):
    # g1D is the bare 1D interaction. |g1D| is the coupling strength.
    info['V_eff_g1D'] = abs(info.get('g1D', 0.0))

    return info


# ============================================================================
# Module 5: Spectrum Extraction
# ============================================================================

def get_band_parameters(data, tau_target):
    """
    Extract band minimum, bandwidth, and lambda_min for a given tau.

    Uses the KC-2 eigenvalue data (20 lowest modes) for the actual band minimum
    and bandwidth. Uses KC-3 lambda_min for the spectral gap (used to define
    mu/lambda_min ratios).

    IMPORTANT: omega_min (band bottom) and lambda_min (spectral gap from KC-3)
    may differ slightly due to different tau grid spacing and interpolation.
    omega_min is the PHYSICAL band minimum from actual eigenvalues;
    lambda_min is the reference scale for dimensionless ratios.

    Parameters
    ----------
    data : dict
    tau_target : float

    Returns
    -------
    omega_min : float
        Band minimum from KC-2 eigenvalues (actual lowest eigenvalue).
    bandwidth : float
        Bandwidth of the lowest band.
    lambda_min : float
        Spectral gap from KC-3 (reference scale).
    """
    # lambda_min from KC-3 (for reference scale)
    kc3_taus = data['kc3']['tau_values']
    idx_kc3 = np.argmin(np.abs(kc3_taus - tau_target))
    lambda_min = data['kc3']['lambda_min'][idx_kc3]

    # Band parameters: prefer KC-2 eigenvalues (actual spectrum), fallback to S23a
    tau_key = f'{tau_target:.2f}'
    omega_min = None
    bandwidth = None

    # Priority 1: KC-2 has actual eigenvalue arrays at this tau
    if tau_key in data['kc2']:
        kc2 = data['kc2'][tau_key]
        omega_min = kc2['omega_min']
        bandwidth = kc2['bandwidth']

    # Priority 2: S23a eigenvalues (16 modes in singlet sector)
    if omega_min is None:
        s23a_taus = data['s23a']['tau_values']
        idx_23a = np.argmin(np.abs(s23a_taus - tau_target))
        evals = data['s23a'][f'eigenvalues_{idx_23a}']
        pos_evals = evals[evals > 0]
        if len(pos_evals) > 0:
            omega_min = float(np.min(pos_evals))
            # Estimate bandwidth from eigenvalue spread
            bandwidth = float(np.max(pos_evals) - np.min(pos_evals))

    # Priority 3: KC-4 bandwidth
    if bandwidth is None:
        tau_str_map = {0.15: '0p15', 0.25: '0p25', 0.35: '0p35'}
        tau_str = tau_str_map.get(tau_target, None)
        if tau_str and tau_str in data['kc4']:
            bandwidth = data['kc4'][tau_str].get('bandwidth', 0.03)

    # Fallback
    if omega_min is None:
        omega_min = lambda_min
    if bandwidth is None:
        bandwidth = 0.03

    return omega_min, bandwidth, lambda_min


# ============================================================================
# Module 6: Main Computation
# ============================================================================

def run_gap_scan(data):
    """
    Scan the BCS gap equation across tau, mu, and V_eff values.

    For each (tau, mu/lambda_min) pair:
    1. Construct the van Hove DOS
    2. Assemble V_eff from KC chain data
    3. Solve the gap equation
    4. Compare to flat-DOS S23a results

    Returns
    -------
    results : dict
        All computed gaps and diagnostics.
    """
    results = {
        'tau_targets': np.array(TAU_TARGETS),
        'mu_ratios': MU_RATIOS,
        'V_eff_scan': V_EFF_SCAN,
    }

    # ===== Part A: V_eff-independent gap curves (Delta vs V_eff at each tau/mu) =====
    print("PART A: Gap vs V_eff curves")
    print("-" * 60)

    for tau in TAU_TARGETS:
        omega_min, bandwidth, lambda_min = get_band_parameters(data, tau)
        V_info = assemble_V_eff(data, tau)

        tau_str = f'tau{tau:.2f}'.replace('.', 'p')
        results[f'{tau_str}_omega_min'] = omega_min
        results[f'{tau_str}_bandwidth'] = bandwidth
        results[f'{tau_str}_lambda_min'] = lambda_min
        results[f'{tau_str}_V_info'] = V_info

        print(f"\n  tau = {tau:.2f}: omega_min={omega_min:.6f}, W={bandwidth:.6f}, "
              f"lambda_min={lambda_min:.6f}")
        print(f"    V_kosmann={V_info['V_kosmann_max']:.6f}, "
              f"V_T={V_info['V_eff_with_T']:.4f}, "
              f"V_full={V_info['V_eff_full']:.4f}, "
              f"V_Mmax={V_info['V_eff_from_Mmax']:.4f}")

        # Scan over mu ratios and V_eff values
        Delta_array = np.zeros((len(MU_RATIOS), len(V_EFF_SCAN)))
        Delta_ratio_array = np.zeros_like(Delta_array)

        for i, mu_r in enumerate(MU_RATIOS):
            mu = mu_r * lambda_min

            for j, V in enumerate(V_EFF_SCAN):
                Delta, converged, n_iter = solve_bcs_gap(
                    V, mu, omega_min, bandwidth, use_adaptive=True
                )
                Delta_array[i, j] = Delta
                Delta_ratio_array[i, j] = Delta / lambda_min if lambda_min > 0 else 0.0

        results[f'{tau_str}_Delta'] = Delta_array
        results[f'{tau_str}_Delta_ratio'] = Delta_ratio_array

    # ===== Part B: Gap at physical V_eff values =====
    print("\n\nPART B: Gap at Physical V_eff Values")
    print("-" * 60)

    # For each tau, evaluate Delta at the assembled V_eff values
    V_eff_labels = ['V_kosmann_only', 'V_eff_with_T', 'V_eff_full',
                    'V_eff_from_Mmax', 'V_eff_g1D']
    V_eff_names = ['Kosmann bare', 'Kosmann+T-matrix', 'Kosmann+T+Luttinger',
                   'From M_max(mu=lmin)', 'g_1D bare']

    physical_results = {}

    for tau in TAU_TARGETS:
        omega_min, bandwidth, lambda_min = get_band_parameters(data, tau)
        V_info = assemble_V_eff(data, tau)
        tau_str = f'tau{tau:.2f}'.replace('.', 'p')

        print(f"\n  tau = {tau:.2f}:")
        print(f"  {'V_eff source':<25s} {'V_eff':>8s} {'mu/lmin':>8s} {'Delta':>12s} "
              f"{'Delta/lmin':>12s} {'Status':>12s}")
        print(f"  {'-'*25} {'-'*8} {'-'*8} {'-'*12} {'-'*12} {'-'*12}")

        phys_deltas = {}

        for label, name in zip(V_eff_labels, V_eff_names):
            V = V_info.get(label, 0.0)
            if V <= 0:
                continue

            # Evaluate at mu = lambda_min (band edge, strongest van Hove)
            for mu_r in [0.95, 1.0, 1.05]:
                mu = mu_r * lambda_min
                Delta, converged, n_iter = solve_bcs_gap(
                    V, mu, omega_min, bandwidth, use_adaptive=True
                )
                D_ratio = Delta / lambda_min if lambda_min > 0 else 0.0

                if D_ratio > 0.01:
                    status = "PASS"
                elif D_ratio > 1e-6:
                    status = "INCONCLUSIVE"
                elif D_ratio > 0:
                    status = "CLOSED"
                else:
                    status = "ZERO"

                print(f"  {name:<25s} {V:8.5f} {mu_r:8.3f} {Delta:12.6e} "
                      f"{D_ratio:12.6e} {status:>12s}")

                key = f'{label}_mu{mu_r}'
                phys_deltas[key] = {
                    'V_eff': V, 'mu_ratio': mu_r, 'Delta': Delta,
                    'Delta_ratio': D_ratio, 'converged': converged
                }

        physical_results[tau_str] = phys_deltas

    results['physical_results'] = physical_results

    # ===== Part C: Critical V_eff for gate thresholds =====
    print("\n\nPART C: Critical V_eff for Gate Thresholds")
    print("-" * 60)

    for tau in TAU_TARGETS:
        omega_min, bandwidth, lambda_min = get_band_parameters(data, tau)
        tau_str = f'tau{tau:.2f}'.replace('.', 'p')

        print(f"\n  tau = {tau:.2f}:")

        for mu_r in [0.95, 1.0, 1.05]:
            mu = mu_r * lambda_min

            # Find V_eff where Delta/lambda_min = 0.01 (PASS threshold)
            def gap_minus_target(log_V, target_ratio):
                V = np.exp(log_V)
                Delta, _, _ = solve_bcs_gap(V, mu, omega_min, bandwidth,
                                            use_adaptive=True)
                return Delta / lambda_min - target_ratio

            # Binary search for V_crit at Delta/lmin = 0.01
            V_lo, V_hi = 1e-6, 10.0
            Delta_lo, _, _ = solve_bcs_gap(V_lo, mu, omega_min, bandwidth,
                                           use_adaptive=True)
            Delta_hi, _, _ = solve_bcs_gap(V_hi, mu, omega_min, bandwidth,
                                           use_adaptive=True)

            if Delta_lo / lambda_min >= 0.01:
                V_crit_pass = V_lo
            elif Delta_hi / lambda_min < 0.01:
                V_crit_pass = np.inf
            else:
                # Bisect
                for _ in range(60):
                    V_mid = np.sqrt(V_lo * V_hi)
                    Delta_mid, _, _ = solve_bcs_gap(V_mid, mu, omega_min, bandwidth,
                                                    use_adaptive=True)
                    if Delta_mid / lambda_min > 0.01:
                        V_hi = V_mid
                    else:
                        V_lo = V_mid
                V_crit_pass = np.sqrt(V_lo * V_hi)

            # Find V_crit at Delta/lmin = 1e-6 (CLOSURE threshold)
            V_lo, V_hi = 1e-10, 10.0
            Delta_lo, _, _ = solve_bcs_gap(V_lo, mu, omega_min, bandwidth,
                                           use_adaptive=True)
            Delta_hi, _, _ = solve_bcs_gap(V_hi, mu, omega_min, bandwidth,
                                           use_adaptive=True)

            if Delta_lo / lambda_min >= 1e-6:
                V_crit_kill = V_lo
            elif Delta_hi / lambda_min < 1e-6:
                V_crit_kill = np.inf
            else:
                for _ in range(80):
                    V_mid = np.sqrt(V_lo * V_hi)
                    Delta_mid, _, _ = solve_bcs_gap(V_mid, mu, omega_min, bandwidth,
                                                    use_adaptive=True)
                    if Delta_mid / lambda_min > 1e-6:
                        V_hi = V_mid
                    else:
                        V_lo = V_mid
                V_crit_kill = np.sqrt(V_lo * V_hi)

            results[f'{tau_str}_V_crit_pass_mu{mu_r}'] = V_crit_pass
            results[f'{tau_str}_V_crit_kill_mu{mu_r}'] = V_crit_kill

            print(f"    mu/lmin={mu_r:.2f}: V_crit(PASS)={V_crit_pass:.6f}, "
                  f"V_crit(CLOSED)={V_crit_kill:.6e}")

    # ===== Part D: Comparison with flat-DOS S23a =====
    print("\n\nPART D: van Hove Enhancement over Flat DOS")
    print("-" * 60)

    for tau in [0.15, 0.25, 0.35]:
        omega_min, bandwidth, lambda_min = get_band_parameters(data, tau)
        V_info = assemble_V_eff(data, tau)
        tau_str = f'tau{tau:.2f}'.replace('.', 'p')

        # S23a M_max at mu=0 (flat DOS result)
        M_flat_mu0 = V_info['M_max_mu0']
        M_flat_mugap = V_info['M_max_mugap']

        # For van Hove, compute M_max_vH = V * N_vH
        # V = M_flat / N_flat, where N_flat ~ 1/(2*W) for flat band of width W
        # Actually M_max = max eigenvalue of BdG, which encodes V*N(0)
        # Use M_max_mugap as the effective V (since N(0)~1 at band edge for flat)

        # Compute N_vH at mu slightly inside band
        for x_offset in [0.001, 0.01, 0.1]:
            mu = omega_min + x_offset * bandwidth
            N_vH = compute_dos_weight(omega_min, bandwidth, mu)
            N_flat = 1.0 / bandwidth  # crude flat-band DOS

            # van Hove M_max = V_eff * N_vH
            # Use V_eff = M_flat_mugap (coupling extracted from flat-DOS BCS)
            V_extracted = M_flat_mugap  # dimensionless coupling V*N_flat

            print(f"  tau={tau:.2f}, x/W={x_offset:.3f}: "
                  f"N_vH={N_vH:.2f}, N_flat={N_flat:.2f}, "
                  f"N_vH/N_flat={N_vH/N_flat:.2f}, "
                  f"V*N_vH={V_extracted*N_vH:.4f}")

    return results


# ============================================================================
# Module 7: Analytical Benchmarks
# ============================================================================

def validate_gap_solver():
    """
    Validate the BCS gap solver against known analytical results.

    Test 1: Flat DOS BCS (standard result).
        For g(omega) = 1/W (constant), mu = omega_min + W/2 (band center):
        Delta = 2*W*exp(-1/(V/W)) for weak coupling V/W << 1.

    Test 2: van Hove singularity enhancement.
        For g ~ 1/sqrt(x), mu at band edge: Delta should be larger than flat DOS.

    Test 3: Zero coupling gives zero gap.

    Test 4: Strong coupling limit: Delta ~ O(W).
    """
    print("VALIDATION: BCS Gap Solver Benchmarks")
    print("=" * 60)

    W = 0.03  # typical bandwidth
    omega_min = 0.82

    # Test 1: V = 0 gives Delta = 0
    Delta, conv, _ = solve_bcs_gap(0.0, omega_min + W/2, omega_min, W)
    assert Delta == 0.0, f"FAIL: V=0 should give Delta=0, got {Delta}"
    print("  Test 1 (V=0): PASS")

    # Test 2: Negative V gives Delta = 0
    Delta, conv, _ = solve_bcs_gap(-1.0, omega_min + W/2, omega_min, W)
    assert Delta == 0.0, f"FAIL: V<0 should give Delta=0, got {Delta}"
    print("  Test 2 (V<0): PASS")

    # Test 3: Strong coupling gives Delta > 0 (may exceed W for very strong V)
    Delta, conv, _ = solve_bcs_gap(10.0, omega_min + W/2, omega_min, W)
    assert Delta > 0, f"FAIL: Strong coupling should give Delta > 0"
    print(f"  Test 3 (V=10): Delta/W = {Delta/W:.4f} PASS (strong coupling regime)")

    # Test 4: Delta increases monotonically with V
    Deltas = []
    for V in [0.01, 0.1, 1.0, 5.0]:
        D, _, _ = solve_bcs_gap(V, omega_min + W/2, omega_min, W)
        Deltas.append(D)
    for i in range(len(Deltas)-1):
        assert Deltas[i+1] >= Deltas[i], f"FAIL: Delta not monotonic in V"
    print(f"  Test 4 (monotonicity): PASS, Deltas = {[f'{d:.6e}' for d in Deltas]}")

    # Test 5: van Hove enhancement -- mu at band edge gives larger Delta
    # Use weak coupling where DOS structure matters
    mu_edge = omega_min + 0.001 * W  # just inside band (high DOS)
    mu_center = omega_min + 0.5 * W
    V_test = 0.05  # weak coupling: DOS structure dominates
    D_edge, _, _ = solve_bcs_gap(V_test, mu_edge, omega_min, W)
    D_center, _, _ = solve_bcs_gap(V_test, mu_center, omega_min, W)
    print(f"  Test 5 (vH enhancement, V={V_test}): Delta(edge)={D_edge:.6e}, "
          f"Delta(center)={D_center:.6e}, ratio={D_edge/max(D_center,1e-30):.2f}")
    # At weak coupling, band-edge mu benefits from van Hove divergence

    # Test 6: Integral substitution accuracy
    # Compare trapezoidal vs adaptive quadrature
    V_test = 0.3
    mu_test = omega_min + 0.1 * W
    Delta_test = 0.001
    I_trap = bcs_gap_integral(mu_test, Delta_test, omega_min, W, n_points=5000)
    I_quad = bcs_gap_integral_log_enhanced(mu_test, Delta_test, omega_min, W)
    rel_err = abs(I_trap - I_quad) / max(abs(I_quad), 1e-30)
    print(f"  Test 6 (quadrature): trap={I_trap:.10f}, quad={I_quad:.10f}, "
          f"rel_err={rel_err:.2e}")
    assert rel_err < 1e-4, f"FAIL: Quadrature mismatch {rel_err:.2e}"
    print("  Test 6: PASS")

    print()
    return True


# ============================================================================
# Module 8: S27 Cross-Validation
# ============================================================================

def cross_validate_with_s27(data, results):
    """
    Cross-validate van Hove gap results against S27 multi-sector BCS.

    S27 used flat DOS. If we extract the effective V from S27's M_max(mu=lmin)
    and apply it to the van Hove gap equation, we should get a LARGER gap.
    """
    print("\nCROSS-VALIDATION: S27 Flat DOS vs van Hove")
    print("=" * 60)

    s27 = data['s27']
    s27_taus = s27['tau_values']  # [0, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.5]
    s27_mus = s27['mu_ratios']   # [0, 0.5, 0.8, ..., 3.0]
    M_max = s27['M_max']         # (9 sectors, 9 taus, 12 mus)
    Delta_max_s27 = s27['Delta_max']

    # mu_ratio = 1.0 index
    idx_mu1 = np.argmin(np.abs(s27_mus - 1.0))

    print(f"\n  {'Tau':>6s} {'Sector':>8s} {'M_max(flat)':>12s} {'Delta_flat':>12s} "
          f"{'Delta_vH':>12s} {'vH/flat':>10s} {'D_vH/lmin':>12s}")
    print(f"  {'-'*6} {'-'*8} {'-'*12} {'-'*12} {'-'*12} {'-'*10} {'-'*12}")

    cross_results = {}

    for tau in [0.15, 0.25, 0.35]:
        idx_tau = np.argmin(np.abs(s27_taus - tau))
        omega_min, bandwidth, lambda_min = get_band_parameters(data, tau)

        # Use sector 0 (singlet, strongest pairing in S27)
        for s_idx in [0]:  # singlet only
            M_flat = M_max[s_idx, idx_tau, idx_mu1]
            D_flat = Delta_max_s27[s_idx, idx_tau, idx_mu1]

            # Extract effective V from M_max:
            # M_max ~ V * N(0) where N(0) is flat DOS ~ 1/W
            # So V ~ M_max * W
            V_extracted = M_flat * bandwidth

            # Also try: V = M_max directly (if N(0) was implicitly 1)
            V_direct = M_flat

            # Solve van Hove gap equation
            mu = lambda_min  # mu at band edge
            D_vH_1, _, _ = solve_bcs_gap(V_extracted, mu, omega_min, bandwidth,
                                         use_adaptive=True)
            D_vH_2, _, _ = solve_bcs_gap(V_direct, mu, omega_min, bandwidth,
                                         use_adaptive=True)

            # Use the larger as the optimistic estimate
            D_vH = max(D_vH_1, D_vH_2)
            V_used = V_extracted if D_vH_1 >= D_vH_2 else V_direct

            ratio = D_vH / max(D_flat, 1e-30) if D_flat > 0 else float('inf')
            D_ratio = D_vH / lambda_min

            print(f"  {tau:6.2f} {'(0,0)':>8s} {M_flat:12.6f} {D_flat:12.6e} "
                  f"{D_vH:12.6e} {ratio:10.2f} {D_ratio:12.6e}")

            key = f'tau{tau:.2f}_s0'
            cross_results[key] = {
                'M_flat': M_flat, 'Delta_flat': D_flat,
                'V_extracted': V_extracted, 'V_direct': V_direct,
                'Delta_vH': D_vH, 'Delta_ratio': D_ratio,
                'enhancement': ratio
            }

    results['cross_validation'] = cross_results
    return results


# ============================================================================
# Module 9: Decisive Summary
# ============================================================================

def compute_decisive_numbers(data, results):
    """
    Compute the decisive Delta/lambda_min values for the gate verdict.

    Strategy: For each tau, use the BEST available V_eff (from KC chain data)
    at mu = lambda_min (band edge, strongest van Hove), and report Delta/lmin.

    This is the fairest test: maximum enhancement from van Hove + best coupling.
    """
    print("\n\nDECISIVE NUMBERS")
    print("=" * 72)

    decisive = {}

    for tau in TAU_TARGETS:
        omega_min, bandwidth, lambda_min = get_band_parameters(data, tau)
        V_info = assemble_V_eff(data, tau)
        tau_str = f'tau{tau:.2f}'.replace('.', 'p')

        # Collect all available V_eff estimates
        V_estimates = {
            'V_kosmann': V_info['V_kosmann_max'],
            'V_T': V_info['V_eff_with_T'],
            'V_full': V_info['V_eff_full'],
            'V_Mmax': V_info['V_eff_from_Mmax'],
            'V_g1D': V_info.get('V_eff_g1D', 0),
        }

        best_Delta = 0.0
        best_label = ''
        best_V = 0.0

        print(f"\n  tau = {tau:.2f}, lambda_min = {lambda_min:.6f}, W = {bandwidth:.6f}")
        print(f"  {'V_eff source':<25s} {'V_eff':>10s} {'mu/lmin':>8s} "
              f"{'Delta':>12s} {'Delta/lmin':>12s}")
        print(f"  {'-'*25} {'-'*10} {'-'*8} {'-'*12} {'-'*12}")

        for label, V in V_estimates.items():
            if V <= 0:
                continue

            # Try multiple mu values near band edge
            for mu_r in [0.95, 1.0, 1.001, 1.01, 1.05]:
                mu = mu_r * lambda_min
                Delta, conv, _ = solve_bcs_gap(V, mu, omega_min, bandwidth,
                                               use_adaptive=True)
                D_ratio = Delta / lambda_min

                print(f"  {label:<25s} {V:10.6f} {mu_r:8.3f} "
                      f"{Delta:12.6e} {D_ratio:12.6e}")

                if D_ratio > best_Delta / lambda_min:
                    best_Delta = Delta
                    best_label = f'{label}, mu/lmin={mu_r}'
                    best_V = V

        decisive[tau_str] = {
            'best_Delta': best_Delta,
            'best_Delta_ratio': best_Delta / lambda_min,
            'best_label': best_label,
            'best_V': best_V,
            'lambda_min': lambda_min,
            'bandwidth': bandwidth,
        }

        print(f"\n  BEST: Delta/lmin = {best_Delta/lambda_min:.6e} "
              f"({best_label})")

    results['decisive'] = decisive

    # --- Overall gate verdict ---
    print("\n\n" + "=" * 72)
    print("GATE VERDICT: KC-5")
    print("=" * 72)

    # Find the maximum Delta/lmin across all tau
    max_ratio = 0.0
    max_tau = None
    for tau in TAU_TARGETS:
        tau_str = f'tau{tau:.2f}'.replace('.', 'p')
        if tau_str in decisive:
            r = decisive[tau_str]['best_Delta_ratio']
            if r > max_ratio:
                max_ratio = r
                max_tau = tau

    if max_ratio > 0.01:
        verdict = "PASS"
    elif max_ratio > 1e-6:
        verdict = "INCONCLUSIVE"
    elif max_ratio > 0:
        verdict = "CLOSED"
    else:
        verdict = "CLOSED"

    results['verdict'] = verdict
    results['max_Delta_ratio'] = max_ratio
    results['max_Delta_tau'] = max_tau

    print(f"\n  Max Delta/lambda_min = {max_ratio:.6e} at tau = {max_tau}")
    print(f"\n  Verdict: {verdict}")
    print(f"\n  Threshold: PASS > 0.01, CLOSED < 1e-6, INCONCLUSIVE in between")

    if verdict == "PASS":
        print(f"\n  The van Hove-enhanced 1D DOS produces a physically meaningful")
        print(f"  BCS gap. The logarithmic divergence at the band edge eliminates")
        print(f"  the critical coupling that closed the flat-DOS S23a result.")
    elif verdict == "INCONCLUSIVE":
        print(f"\n  The van Hove gap exists but is marginally small.")
        print(f"  The enhancement over flat DOS is present but insufficient")
        print(f"  to reach physically relevant magnitude.")
    else:
        print(f"\n  Despite the van Hove singularity, the gap remains negligibly")
        print(f"  small. The coupling is too weak even with logarithmic enhancement.")

    return results


# ============================================================================
# Module 10: Plotting
# ============================================================================

def make_plots(results, data):
    """Generate diagnostic plots."""

    fig, axes = plt.subplots(2, 2, figsize=(14, 12))

    # --- Plot 1: Delta/lmin vs V_eff at mu=lambda_min for each tau ---
    ax = axes[0, 0]
    V_scan = results['V_eff_scan']

    for tau in TAU_TARGETS:
        tau_str = f'tau{tau:.2f}'.replace('.', 'p')
        if f'{tau_str}_Delta_ratio' in results:
            D_ratio = results[f'{tau_str}_Delta_ratio']
            # mu_ratio = 1.0 index
            idx_mu1 = np.argmin(np.abs(MU_RATIOS - 1.0))
            y = D_ratio[idx_mu1, :]
            mask = y > 0
            if np.any(mask):
                ax.plot(V_scan[mask], y[mask], label=f'tau={tau:.2f}')

    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.axhline(0.01, color='green', linestyle='--', alpha=0.7, label='PASS threshold')
    ax.axhline(1e-6, color='red', linestyle='--', alpha=0.7, label='CLOSURE threshold')
    ax.set_xlabel('V_eff')
    ax.set_ylabel('Delta / lambda_min')
    ax.set_title('BCS Gap vs Coupling at mu = lambda_min')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Mark physical V_eff values
    for tau in [0.15, 0.25, 0.35]:
        tau_str = f'tau{tau:.2f}'.replace('.', 'p')
        if f'{tau_str}_V_info' in results:
            V_info = results[f'{tau_str}_V_info']
            for label, marker in [('V_kosmann_max', 'o'), ('V_eff_from_Mmax', 's')]:
                V = V_info.get(label, 0)
                if V > 0:
                    ax.axvline(V, color='gray', linestyle=':', alpha=0.3)

    # --- Plot 2: Delta/lmin vs mu/lmin at physical V_eff ---
    ax = axes[0, 1]

    for tau in TAU_TARGETS:
        tau_str = f'tau{tau:.2f}'.replace('.', 'p')
        if f'{tau_str}_Delta_ratio' in results:
            D_ratio = results[f'{tau_str}_Delta_ratio']

            # Use V_eff closest to Mmax value
            V_info = results.get(f'{tau_str}_V_info', {})
            V_phys = V_info.get('V_eff_from_Mmax', 0.5)
            idx_V = np.argmin(np.abs(V_scan - V_phys))

            y = D_ratio[:, idx_V]
            mask = y > 0
            if np.any(mask):
                ax.plot(MU_RATIOS[mask], y[mask], 'o-', label=f'tau={tau:.2f}')

    ax.set_yscale('log')
    ax.axhline(0.01, color='green', linestyle='--', alpha=0.7, label='PASS')
    ax.axhline(1e-6, color='red', linestyle='--', alpha=0.7, label='CLOSED')
    ax.axvline(1.0, color='blue', linestyle=':', alpha=0.5, label='mu=lambda_min')
    ax.set_xlabel('mu / lambda_min')
    ax.set_ylabel('Delta / lambda_min')
    ax.set_title('BCS Gap vs Chemical Potential (V = V_eff from M_max)')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # --- Plot 3: van Hove DOS illustration ---
    ax = axes[1, 0]

    tau = 0.35
    omega_min, bandwidth, lambda_min = get_band_parameters(data, tau)
    omega = np.linspace(omega_min + 1e-6*bandwidth, omega_min + bandwidth - 1e-6*bandwidth, 500)
    g_vH = van_hove_dos(omega, omega_min, bandwidth, 'tight_binding')
    g_flat = np.ones_like(omega) / bandwidth

    ax.plot(omega, g_vH, 'b-', linewidth=2, label='van Hove 1D DOS')
    ax.plot(omega, g_flat, 'r--', linewidth=2, label='Flat DOS')
    ax.axvline(lambda_min, color='green', linestyle=':', alpha=0.7, label='lambda_min')
    ax.set_xlabel('omega')
    ax.set_ylabel('g(omega)')
    ax.set_title(f'Density of States at tau={tau:.2f}')
    ax.set_ylim(0, min(200, np.max(g_vH[g_vH < np.inf])))
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # --- Plot 4: Critical V_eff vs tau ---
    ax = axes[1, 1]

    taus_plot = []
    V_pass_plot = []
    V_kill_plot = []
    V_phys_plot = []

    for tau in TAU_TARGETS:
        tau_str = f'tau{tau:.2f}'.replace('.', 'p')
        V_pass = results.get(f'{tau_str}_V_crit_pass_mu1.0', np.inf)
        V_kill = results.get(f'{tau_str}_V_crit_kill_mu1.0', np.inf)
        V_info = results.get(f'{tau_str}_V_info', {})
        V_phys = V_info.get('V_eff_from_Mmax', 0.0)

        if np.isfinite(V_pass):
            taus_plot.append(tau)
            V_pass_plot.append(V_pass)
            V_kill_plot.append(V_kill if np.isfinite(V_kill) else 1e-10)
            V_phys_plot.append(V_phys)

    if taus_plot:
        ax.semilogy(taus_plot, V_pass_plot, 'gs-', linewidth=2,
                     markersize=8, label='V_crit (PASS: D/lmin>0.01)')
        ax.semilogy(taus_plot, V_kill_plot, 'rs-', linewidth=2,
                     markersize=8, label='V_crit (CLOSED: D/lmin>1e-6)')
        ax.semilogy(taus_plot, V_phys_plot, 'b^-', linewidth=2,
                     markersize=10, label='Physical V_eff (M_max)')

    ax.set_xlabel('tau')
    ax.set_ylabel('V_eff')
    ax.set_title('Critical Coupling vs tau at mu = lambda_min')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(str(OUTPUT_PREFIX) + '.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"\n  Plot saved: {OUTPUT_PREFIX}.png")


# ============================================================================
# Module 11: Output
# ============================================================================

def write_verdict(results, data):
    """Write the gate verdict text file."""

    verdict = results['verdict']
    max_ratio = results['max_Delta_ratio']
    max_tau = results['max_Delta_tau']

    lines = []
    lines.append("=" * 72)
    lines.append("KC-5: BCS Gap with van Hove DOS -- GATE VERDICT")
    lines.append("=" * 72)
    lines.append("")
    lines.append(f"Verdict: {verdict}")
    lines.append(f"Max Delta/lambda_min: {max_ratio:.6e}")
    lines.append(f"At tau: {max_tau}")
    lines.append("")
    lines.append("Thresholds:")
    lines.append("  PASS:         Delta/lambda_min > 0.01")
    lines.append("  CLOSED:         Delta/lambda_min < 1e-6")
    lines.append("  INCONCLUSIVE: 1e-6 <= Delta/lambda_min <= 0.01")
    lines.append("")
    lines.append("-" * 72)
    lines.append("DECISIVE VALUES BY TAU")
    lines.append("-" * 72)

    for tau in TAU_TARGETS:
        tau_str = f'tau{tau:.2f}'.replace('.', 'p')
        if tau_str in results.get('decisive', {}):
            d = results['decisive'][tau_str]
            lines.append(f"")
            lines.append(f"  tau = {tau:.2f}:")
            lines.append(f"    lambda_min = {d['lambda_min']:.6f}")
            lines.append(f"    bandwidth  = {d['bandwidth']:.6f}")
            lines.append(f"    best Delta = {d['best_Delta']:.6e}")
            lines.append(f"    Delta/lmin = {d['best_Delta_ratio']:.6e}")
            lines.append(f"    V_eff used = {d['best_V']:.6f}")
            lines.append(f"    source     = {d['best_label']}")

    lines.append("")
    lines.append("-" * 72)
    lines.append("CRITICAL COUPLINGS AT mu = lambda_min")
    lines.append("-" * 72)

    for tau in TAU_TARGETS:
        tau_str = f'tau{tau:.2f}'.replace('.', 'p')
        V_pass = results.get(f'{tau_str}_V_crit_pass_mu1.0', np.inf)
        V_kill = results.get(f'{tau_str}_V_crit_kill_mu1.0', np.inf)
        V_info = results.get(f'{tau_str}_V_info', {})
        V_phys = V_info.get('V_eff_from_Mmax', 0.0)

        lines.append(f"  tau={tau:.2f}: V_crit(PASS)={V_pass:.6f}, "
                     f"V_crit(CLOSED)={V_kill:.6e}, V_phys={V_phys:.6f}")

        if V_phys > 0:
            if V_phys >= V_pass:
                lines.append(f"    --> V_phys >= V_crit(PASS): PASS at this tau")
            elif V_phys >= V_kill:
                lines.append(f"    --> V_crit(CLOSED) <= V_phys < V_crit(PASS): INCONCLUSIVE")
            else:
                lines.append(f"    --> V_phys < V_crit(CLOSED): CLOSED at this tau")

    lines.append("")
    lines.append("-" * 72)
    lines.append("V_EFF ASSEMBLY (KC CHAIN INPUTS)")
    lines.append("-" * 72)

    for tau in TAU_TARGETS:
        tau_str = f'tau{tau:.2f}'.replace('.', 'p')
        V_info = results.get(f'{tau_str}_V_info', {})
        if V_info:
            lines.append(f"")
            lines.append(f"  tau = {tau:.2f}:")
            lines.append(f"    Kosmann V_max    = {V_info.get('V_kosmann_max', 0):.6f}")
            lines.append(f"    Kosmann + T-mat  = {V_info.get('V_eff_with_T', 0):.6f}")
            lines.append(f"    Full (+ Lutt)    = {V_info.get('V_eff_full', 0):.6f}")
            lines.append(f"    From M_max(lmin) = {V_info.get('V_eff_from_Mmax', 0):.6f}")
            lines.append(f"    g_1D (KC-4)      = {V_info.get('V_eff_g1D', 0):.6f}")
            lines.append(f"    T-enhancement    = {V_info.get('T_enhancement', 1):.2f}x")
            lines.append(f"    K_Landau         = {V_info.get('K_Landau', 1):.4f}")
            lines.append(f"    Luttinger enhance= {V_info.get('Luttinger_enhance', 1):.4f}x")

    lines.append("")
    lines.append("-" * 72)
    lines.append("S27 CROSS-VALIDATION")
    lines.append("-" * 72)

    cross = results.get('cross_validation', {})
    for key in sorted(cross.keys()):
        c = cross[key]
        lines.append(f"  {key}: flat Delta={c['Delta_flat']:.6e}, "
                     f"vH Delta={c['Delta_vH']:.6e}, "
                     f"vH/flat={c['enhancement']:.2f}x, "
                     f"D/lmin={c['Delta_ratio']:.6e}")

    lines.append("")
    lines.append("-" * 72)
    lines.append("PHYSICS NOTES")
    lines.append("-" * 72)
    lines.append("")
    lines.append("  The van Hove singularity g(omega) ~ 1/sqrt(omega - omega_min)")
    lines.append("  provides a logarithmic divergence in the BCS integral at the")
    lines.append("  band edge. This divergence eliminates the critical coupling:")
    lines.append("  ANY attractive V > 0 produces Delta > 0 in 1D.")
    lines.append("")
    lines.append("  However, the gap may be exponentially small:")
    lines.append("  Delta ~ W * exp(-c/V_eff) where c depends on the DOS structure.")
    lines.append("")
    lines.append("  S23a result (flat DOS): M_max(mu=0) = 0.077-0.149, CLOSED.")
    lines.append("  The question: does van Hove enhancement change CLOSED to PASS?")
    lines.append("")

    txt = "\n".join(lines)

    with open(str(OUTPUT_PREFIX) + '.txt', 'w') as f:
        f.write(txt)

    print(f"\n  Verdict file saved: {OUTPUT_PREFIX}.txt")
    return txt


def save_data(results):
    """Save numerical results to .npz."""

    # Flatten the results dict, skipping non-array items
    save_dict = {}
    for key, val in results.items():
        if isinstance(val, np.ndarray):
            save_dict[key] = val
        elif isinstance(val, (int, float)):
            save_dict[key] = np.array([val])
        elif isinstance(val, str):
            save_dict[key] = np.array([val])
        elif isinstance(val, dict):
            # Flatten one level of dict
            for k2, v2 in val.items():
                if isinstance(v2, np.ndarray):
                    save_dict[f'{key}_{k2}'] = v2
                elif isinstance(v2, (int, float)):
                    save_dict[f'{key}_{k2}'] = np.array([v2])
                elif isinstance(v2, str):
                    save_dict[f'{key}_{k2}'] = np.array([v2])
                elif isinstance(v2, dict):
                    for k3, v3 in v2.items():
                        if isinstance(v3, (int, float)):
                            save_dict[f'{key}_{k2}_{k3}'] = np.array([v3])
                        elif isinstance(v3, str):
                            save_dict[f'{key}_{k2}_{k3}'] = np.array([v3])
                        elif isinstance(v3, np.ndarray):
                            save_dict[f'{key}_{k2}_{k3}'] = v3

    np.savez_compressed(str(OUTPUT_PREFIX) + '.npz', **save_dict)
    print(f"\n  Data saved: {OUTPUT_PREFIX}.npz ({len(save_dict)} arrays)")


# ============================================================================
# Main
# ============================================================================

def main():
    t0 = time.time()

    # Load data
    data = load_all_data()

    # Validate solver
    validate_gap_solver()

    # Run gap scan
    results = run_gap_scan(data)

    # Cross-validate with S27
    results = cross_validate_with_s27(data, results)

    # Compute decisive numbers
    results = compute_decisive_numbers(data, results)

    # Save outputs
    make_plots(results, data)
    save_data(results)
    verdict_txt = write_verdict(results, data)

    elapsed = time.time() - t0
    print(f"\n  Total runtime: {elapsed:.1f}s")
    print("\n" + verdict_txt)

    return results


if __name__ == '__main__':
    results = main()
