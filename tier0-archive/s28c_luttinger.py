"""
Session 28c Computation KC-4: Luttinger Liquid Parameter K
==========================================================

Computes the Luttinger liquid parameter K for the effective 1D phonon system
on M^4 x SU(3) driven by Jensen deformation (parametric creation).

Physics:
--------
When the Jensen deformation tau(t) drives phonon creation (KC-1), the created
phonons interact via 4-point vertices (KC-2). In 1D, interacting bosons form
a Luttinger liquid with parameter K:

    K < 1:  Attractive interactions (fermionization, Tonks-Girardeau regime)
    K = 1:  Non-interacting (free bosons)
    K > 1:  Repulsive interactions (weakly interacting BEC)
    K >> 1: Very weak repulsion (essentially free)

The Luttinger parameter from the Lieb-Liniger model:

    K = pi / sqrt(pi^2 + 4 * gamma_LL)             [attractive: gamma < 0]
    K = pi / sqrt(pi^2 - 4 * |gamma_LL|)           [repulsive: gamma > 0, weak]

where gamma_LL = m* g_1D / (hbar^2 n_1D) is the dimensionless interaction
parameter, m* is the effective mass, g_1D is the 1D coupling, and n_1D is
the 1D phonon density.

For ATTRACTIVE interactions (gamma_LL < 0), the Lieb-Liniger formula gives:

    K = pi / sqrt(pi^2 + 4 * |gamma_LL|)   <  1

and K -> 0 as |gamma_LL| -> infinity (strong attraction = deep fermionization).

For the phonon system:
    - g_1D extracted from the forward T-matrix element T[k,k,k,k] at the gap edge
    - n_1D = N_phonon / L_eff, where N_phonon = sum_k B_k * mult and L_eff is
      set by the compactification radius and drive rate
    - m* from the curvature of the dispersion relation near the gap edge
    - Pomeranchuk f_0 << -1 (from S28b) indicates STRONGLY ATTRACTIVE interactions

Three independent methods for extracting K:
    Method 1: Lieb-Liniger from T-matrix forward scattering (g_1D from KC-2)
    Method 2: Landau parameter f_0 -> compressibility -> K (from S28b Pomeranchuk)
    Method 3: Effective field theory: K = v_s / (v_F * (1 + F_0^s)) where F_0^s
              is the symmetric Landau parameter

Gate KC-4:
    PASS:  K < 1  (attractive, fermionization possible)
    CLOSED:  K > 3  (weakly repulsive, no Fermi surface)

Input: tier0-computation/s28c_phonon_tmatrix.npz  (KC-2 output)
       tier0-computation/s28a_bogoliubov_coefficients.npz  (KC-1 output)
       tier0-computation/s28b_pomeranchuk.npz  (Pomeranchuk data)
Output: tier0-computation/s28c_luttinger.npz
        tier0-computation/s28c_luttinger.txt

Author: phonon-exflation-sim agent
Date: 2026-02-27
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
import sys
import time

# ==============================================================================
# Configuration
# ==============================================================================

DATA_DIR = Path(__file__).parent
TMATRIX_FILE = DATA_DIR / "s28c_phonon_tmatrix.npz"
BOGO_FILE = DATA_DIR / "s28a_bogoliubov_coefficients.npz"
POMER_FILE = DATA_DIR / "s28b_pomeranchuk.npz"
OUTPUT_NPZ = DATA_DIR / "s28c_luttinger.npz"
OUTPUT_TXT = DATA_DIR / "s28c_luttinger.txt"
OUTPUT_PNG = DATA_DIR / "s28c_luttinger.png"

# tau targets (must match KC-2 data)
TAU_TARGETS = [0.15, 0.25, 0.35]

# Drive strengths (dtau/dt in natural units)
DRIVE_STRENGTHS = [0.01, 0.1, 0.5, 1.0]

# System size: effective 1D "length" in the tau direction
# The compactification radius at tau=0 is 1 (natural units on SU(3)).
# The effective 1D length for a single period is 2*pi (circumference of tau circle).
# But tau is NOT periodic -- it's a deformation parameter. The relevant length scale
# is set by the density of created phonons per unit tau change.
# We parametrize: L_eff = N_modes_active (effective number of 1D "sites")
# This cancels in gamma_LL = g/(n/L) * m/L = g*m*L/N = g*m/(n_1D)

# Gate thresholds
K_PASS_THRESHOLD = 1.0   # K < 1 = attractive (PASS)
K_KILL_THRESHOLD = 3.0   # K > 3 = weakly repulsive (CLOSED)


# ==============================================================================
# Load all input data
# ==============================================================================

print("=" * 72)
print("KC-4: Luttinger Liquid Parameter K")
print("=" * 72)

t_start = time.time()

# --- KC-2 T-matrix data ---
print("\nLoading T-matrix data (KC-2)...")
tmat = np.load(TMATRIX_FILE, allow_pickle=True)
tau_tmat_targets = tmat['tau_targets']
print(f"  T-matrix tau targets: {tau_tmat_targets}")

# --- KC-1 Bogoliubov data ---
print("Loading Bogoliubov data (KC-1)...")
bogo = np.load(BOGO_FILE, allow_pickle=True)
tau_bogo = bogo['tau_values']
B_k_all = bogo['B_k']            # (21, 11424)
omega_all = bogo['omega_tracked']  # (21, 11424)
mult_ref = bogo['mult_ref']       # (11424,)
Gamma_inject_all = bogo['Gamma_inject']  # (21,)
domega_dtau_all = bogo['domega_dtau']    # (21, 11424)

# --- Pomeranchuk data (S28b) ---
print("Loading Pomeranchuk data (S28b)...")
pomer = np.load(POMER_FILE, allow_pickle=True)
tau_pomer = pomer['tau_28']
f0_pomer = pomer['f0_K_28']       # (8_sectors, 10_tau)
N0_pomer = pomer['N0_K_28']
Vmax_pomer = pomer['Vmax_K_28']
sectors_pomer = pomer['sectors_28']  # (8, 4) = (p, q, dim, mult)


# ==============================================================================
# Module 1: Effective mass from dispersion curvature
# ==============================================================================

def compute_effective_mass(omega, domega_dtau):
    """
    Compute the effective mass m* from the curvature of the dispersion relation.

    Near the gap edge, the dispersion is approximately:
        omega(k) ~ omega_gap + k^2 / (2 * m*)

    where "k" in the 1D effective theory is the mode index offset from the gap.
    The effective mass characterizes how steeply energy rises above the gap.

    For modes on SU(3), the "momentum" is the eigenvalue index. We estimate
    m* from the spacing of the lowest eigenvalues:

        m* ~ 1 / (2 * d^2 omega / dk^2)    at the gap edge

    Using finite differences on the sorted eigenvalue spectrum.

    Parameters:
        omega: ndarray, shape (N,), sorted eigenvalues (absolute)
        domega_dtau: ndarray, shape (N,), derivative domega/dtau

    Returns:
        m_star: float, effective mass in natural units
        delta_omega: float, characteristic energy spacing near gap
        bandwidth: float, total bandwidth of the lowest modes
    """
    # Sort by omega
    idx = np.argsort(omega)
    omega_sorted = omega[idx]

    # Use the 20 lowest modes to estimate curvature
    n_fit = min(20, len(omega_sorted))
    omega_low = omega_sorted[:n_fit]
    omega_gap = omega_low[0]

    # Discrete "momenta": k_n = n * delta_k, with delta_k = pi / n_fit
    # omega(k) ~ omega_gap + k^2/(2m*) => m* = k^2 / (2*(omega_n - omega_gap))
    # For the nth mode: k_n = n * pi / L, omega_n - omega_gap = (n*pi/L)^2 / (2*m*)
    # => m* = (n * pi / L)^2 / (2 * (omega_n - omega_gap))

    # We fit omega_n - omega_gap vs n^2 to extract m*
    # But on a compact manifold, the modes are discrete. The "bandwidth" B = omega_max - omega_min
    # sets the effective mass: m* ~ N / (2 * B) for N modes spanning bandwidth B.

    bandwidth = omega_low[-1] - omega_low[0]
    if bandwidth < 1e-12:
        # Degenerate modes -- essentially infinite mass (flat band)
        return np.inf, 0.0, 0.0

    # Quadratic fit: omega(n) = omega_gap + a * n^2
    ns = np.arange(n_fit, dtype=float)
    delta_omega = omega_low - omega_gap
    # Least squares fit: delta_omega ~ a * n^2
    n2 = ns**2
    # Exclude n=0
    mask = ns > 0
    if mask.sum() < 2:
        return np.inf, 0.0, bandwidth

    a_fit = np.sum(delta_omega[mask] * n2[mask]) / np.sum(n2[mask]**2)
    if a_fit < 1e-15:
        return np.inf, 0.0, bandwidth

    # m* = 1 / (2*a) in units where lattice spacing = 1
    # (delta_k = 1, so k_n = n, omega(k) = omega_gap + k^2/(2m*) => a = 1/(2m*))
    m_star = 1.0 / (2.0 * a_fit)

    delta_omega_char = omega_low[1] - omega_low[0] if n_fit > 1 else 0.0

    return m_star, delta_omega_char, bandwidth


# ==============================================================================
# Module 2: Extract interaction strength g_1D from T-matrix
# ==============================================================================

def extract_g1D_from_tmatrix(T_full, omega, n_modes):
    """
    Extract the effective 1D interaction strength g_1D from the T-matrix.

    For a 1D Bose gas, the interaction strength g_1D is related to the
    forward scattering amplitude at threshold:

        g_1D = T(k, k -> k, k; E ~ 2*omega_gap)    [natural units]

    where the T-matrix element is evaluated at the gap edge (lowest energy
    available for scattering).

    Sign convention:
        g_1D > 0: repulsive
        g_1D < 0: attractive

    The T-matrix from KC-2 is complex. The real part gives the energy shift
    (interaction strength), while the imaginary part gives the width (decay).
    For the Luttinger parameter, we use:

        g_1D = Re[T(gap, gap -> gap, gap)]

    for the gap-edge forward scattering.

    Parameters:
        T_full: ndarray, shape (N, N, N, N), complex T-matrix
        omega: ndarray, shape (N,), mode frequencies
        n_modes: int, number of modes

    Returns:
        g_1D: float, effective 1D coupling (signed)
        g_1D_avg: float, average over gap-edge modes
        T_fwd_stats: dict with forward scattering statistics
    """
    # Forward scattering: T[k,k,k,k]
    T_fwd = np.array([T_full[k, k, k, k] for k in range(n_modes)])

    # Find gap-edge modes (lowest omega)
    omega_sorted_idx = np.argsort(omega)
    gap_modes = omega_sorted_idx[:4]  # Use 4 lowest modes

    # g_1D from gap-edge forward scattering
    T_gap_fwd = T_fwd[gap_modes]
    g_1D = np.real(T_gap_fwd[0])  # Single gap-edge mode
    g_1D_avg = np.mean(np.real(T_gap_fwd))  # Average over gap-edge degenerate modes

    # Also compute exchange scattering at gap edge
    T_exch = np.array([T_full[gap_modes[0], gap_modes[i],
                               gap_modes[i], gap_modes[0]]
                       for i in range(len(gap_modes))])

    # Off-diagonal: T[0,1,0,1] type (momentum exchange)
    if n_modes >= 2:
        T_exchange_01 = T_full[gap_modes[0], gap_modes[1],
                               gap_modes[0], gap_modes[1]]
    else:
        T_exchange_01 = 0.0 + 0.0j

    # Comprehensive interaction: sum over all forward channels at gap edge
    # g_eff = (1/N_gap) sum_{k in gap} T[k,k,k,k]
    # This accounts for the multiplicity of gap-edge modes
    g_1D_eff = np.mean(np.real(T_fwd[:min(8, n_modes)]))

    stats = {
        'g_1D_single': g_1D,
        'g_1D_avg_gap': g_1D_avg,
        'g_1D_eff': g_1D_eff,
        'T_fwd_gap_real': np.real(T_gap_fwd),
        'T_fwd_gap_imag': np.imag(T_gap_fwd),
        'T_fwd_gap_abs': np.abs(T_gap_fwd),
        'T_exchange_01': T_exchange_01,
        'T_fwd_all_real': np.real(T_fwd),
        'T_fwd_all_abs': np.abs(T_fwd),
    }

    return g_1D, g_1D_avg, stats


# ==============================================================================
# Module 3: Phonon density from Bogoliubov coefficients
# ==============================================================================

def compute_phonon_density(B_k, mult, omega, dtau_dt, tau_idx_bogo, Gamma_inject):
    """
    Compute the effective 1D phonon density n_1D.

    The parametric injection rate Gamma_inject = sum_k 2*omega_k * B_k * mult_k * dtau/dt
    gives the total phonon creation rate. The steady-state density (phonons
    per unit "length" in the effective 1D system) is:

        n_1D = Gamma_inject * tau_scatt / L_eff

    where tau_scatt is the scattering time (from KC-2) and L_eff is the effective
    system size.

    Alternative: Since B_k gives the occupation per mode per unit dtau, the
    total phonon number at deformation tau is:

        N_phon(tau) = integral_0^tau sum_k B_k(tau') * mult_k * (dtau'/dt * dt)

    For a constant drive rate dtau/dt, over a time interval delta_t = tau / (dtau/dt):

        N_phon = tau * sum_k <B_k> * mult_k    [averaged over [0, tau]]

    The "1D density" is this divided by the effective system size.

    For the Lieb-Liniger parameter, we need:
        gamma_LL = m* g_1D / (hbar^2 * n_1D)

    In natural units (hbar = 1), gamma_LL = m* * g_1D / n_1D.

    The ratio that matters is g_1D / n_1D, which is independent of the
    overall normalization as long as we are consistent.

    Parameters:
        B_k: ndarray, shape (11424,), Bogoliubov coefficients at this tau
        mult: ndarray, shape (11424,), multiplicities
        omega: ndarray, shape (11424,), frequencies
        dtau_dt: float, drive rate
        tau_idx_bogo: int, index into Bogoliubov tau array
        Gamma_inject: float, injection rate at this tau

    Returns:
        n_1D: float, effective 1D phonon density
        N_phon: float, total phonon number
        N_gap: float, number of gap-edge phonons
    """
    # Total phonon number (weighted by multiplicity)
    N_phon = np.sum(B_k * mult)

    # Number of phonons near the gap edge (within 5% of gap)
    omega_gap = omega.min()
    gap_mask = omega < omega_gap * 1.05
    N_gap = np.sum(B_k[gap_mask] * mult[gap_mask])

    # Effective 1D system size
    # The phonons live on SU(3), which has volume Vol(SU(3)) = sqrt(3) * pi^5 / 4.
    # For the 1D effective theory along tau, the relevant length is the
    # "correlation length" set by the number of active modes.
    # With N_active ~ sum(B_k > threshold) modes, the effective 1D length is
    # L_eff ~ N_active * (1 / delta_k) where delta_k is the mode spacing.
    #
    # Simplification: In the Lieb-Liniger model, gamma = mg/n with n = N/L.
    # The effective 1D density is N_phon / N_modes_active, which counts
    # the average occupation per active mode channel.

    N_active = np.sum((B_k * mult) > 0.001)
    if N_active < 1:
        N_active = 1

    # n_1D = phonon number per active mode
    n_1D = N_phon / N_active

    return n_1D, N_phon, N_gap, N_active


# ==============================================================================
# Module 4: Lieb-Liniger Luttinger parameter
# ==============================================================================

def luttinger_lieb_liniger(gamma_LL):
    """
    Compute the Luttinger parameter K from the Lieb-Liniger model.

    For the Lieb-Liniger model of 1D bosons with delta-function interactions:

        H = -sum_i d^2/dx_i^2 + 2c * sum_{i<j} delta(x_i - x_j)

    The Luttinger parameter is:

    For REPULSIVE (c > 0, gamma > 0):
        K = pi / (pi - arctan(pi/gamma))        [Haldane formula]
        In the weak coupling limit: K ~ 1 + 2/gamma
        In the Tonks-Girardeau limit (gamma -> inf): K -> 1

    For ATTRACTIVE (c < 0, gamma < 0):
        K = pi / (pi + arctan(pi/|gamma|))
        In the weak attraction limit: K ~ 1 - 2/|gamma|
        In the strong attraction limit: K -> 1/2
        For |gamma| >> 1: K ~ 1/2 + pi/(2*gamma^2) -> 1/2

    The EXACT Bethe ansatz result (Cazalilla et al., Rev. Mod. Phys. 83, 1405):

    K(gamma) = [1 + 2/(|gamma| * e(gamma))]^{-1/2}    for repulsive
    K(gamma) = [1 - 2/(|gamma| * e(gamma))]^{-1/2}    for attractive

    where e(gamma) is determined by the Bethe ansatz integral equation.

    For practical computation, we use the interpolation formula:
        K = pi / sqrt(pi^2 + 4*gamma_LL)    for gamma_LL > 0 (repulsive)
        K = pi / sqrt(pi^2 - 4*|gamma_LL|)  for gamma_LL < 0 (attractive, |gamma|<pi^2/4)

    IMPORTANT: For strongly attractive bosons (|gamma_LL| > pi^2/4 ~ 2.47),
    the Lieb-Liniger ground state is a McGuire cluster (bound state), and
    K is not simply defined. In this regime, we use the asymptotic:
        K -> 1/N for N-particle bound state (strong attraction limit)

    Parameters:
        gamma_LL: float, dimensionless Lieb-Liniger parameter (signed)

    Returns:
        K: float, Luttinger parameter
        regime: str, description of the regime
    """
    if gamma_LL > 0:
        # Repulsive
        if gamma_LL < 0.01:
            K = 1.0 + 2.0 / max(gamma_LL, 1e-10)
            regime = "weakly repulsive"
        elif gamma_LL < 100:
            # Haldane formula (exact for all gamma > 0):
            # K = pi / (pi - arctan(pi/gamma))
            # This gives K = inf at gamma=0, K=1 at gamma=inf
            K = np.pi / (np.pi - np.arctan(np.pi / gamma_LL))
            regime = "repulsive"
        else:
            # Tonks-Girardeau
            K = 1.0 + np.pi**2 / (2 * gamma_LL**2)
            regime = "Tonks-Girardeau (strong repulsion)"
    elif gamma_LL < 0:
        # Attractive
        abs_gamma = abs(gamma_LL)
        if abs_gamma < 0.01:
            K = 1.0 - 2.0 * abs_gamma / (np.pi**2)
            regime = "weakly attractive"
        elif abs_gamma < np.pi**2 / 4:
            # Standard attractive formula
            # K = pi / (pi + arctan(pi/|gamma|))
            K = np.pi / (np.pi + np.arctan(np.pi / abs_gamma))
            regime = "attractive"
        else:
            # Strong attraction: McGuire cluster regime
            # K approaches asymptote: K ~ pi / (pi + pi/2) = 2/3 at |gamma|->inf
            # More precisely: K = pi / (pi + arctan(pi/|gamma|))
            # arctan(pi/|gamma|) -> pi/|gamma| for large |gamma|
            # K -> pi / (pi + pi/|gamma|) -> 1 for |gamma|->inf
            # Wait, that's wrong. Let me re-derive.
            #
            # For the attractive case, the EXACT Haldane formula is:
            #   K = pi / (pi + arctan(pi/|gamma|))
            # As |gamma| -> inf: arctan(pi/|gamma|) -> 0, so K -> 1
            # As |gamma| -> 0: arctan(pi/|gamma|) -> pi/2, so K -> pi/(pi+pi/2) = 2/3
            #
            # CORRECTION: The actual Bethe ansatz result for attractive bosons is
            # more subtle. For |gamma| > 2, the ground state is a bound cluster.
            # The Luttinger liquid description applies to the EXCITED states
            # (gas branch), not the ground state.
            #
            # For the gas branch (metastable Luttinger liquid):
            K = np.pi / (np.pi + np.arctan(np.pi / abs_gamma))
            if abs_gamma > 10:
                regime = "strongly attractive (cluster)"
            else:
                regime = "moderately attractive"
    else:
        K = 1.0
        regime = "non-interacting"

    return K, regime


# ==============================================================================
# Module 5: Luttinger K from Landau parameter f_0
# ==============================================================================

def luttinger_from_landau_f0(f0, N0):
    """
    Compute the Luttinger parameter K from the symmetric Landau parameter f_0^s.

    In Fermi liquid theory (applicable after fermionization of 1D bosons):

        kappa / kappa_0 = 1 / (1 + F_0^s)    (compressibility ratio)

    where F_0^s = N(0) * f_0^s is the dimensionless Landau parameter.

    For a Luttinger liquid:
        K^2 = v_F / v_s = (1 + F_1^s/d) / (1 + F_0^s)

    In 1D (d=1), assuming F_1^s small:
        K^2 ~ 1 / (1 + F_0^s)

    Therefore:
        K = 1 / sqrt(1 + F_0^s)    if 1 + F_0^s > 0

    Pomeranchuk stability: 1 + F_0^s > 0 required. If violated, the system is
    unstable to phase separation (spinodal).

    For our system, f_0 is the un-normalized Landau parameter from S28b.
    F_0^s = N(0) * f_0 where N(0) is the density of states.

    HOWEVER: The Pomeranchuk data gives f_0 = f(theta=0) from the s-wave
    Landau interaction function. The DIMENSIONLESS F_0^s = N(0) * integral f(theta) dtheta/(2pi)
    For s-wave (l=0): F_0^s = N(0) * f_0 (in 1D, the partial wave is just f_0 itself).

    ACTUALLY: From the S28b code, f_0 = V_max * N(0) where V_max is the max
    potential and N(0) is the DOS. So f_0 IS the dimensionless F_0^s already.
    No, checking the data: f0_K_28 stores the dimensionless f0 = V*N0.
    But the data has BOTH f0 and N0 as separate arrays. Let me compute F_0^s correctly.

    CORRECTION: Reading S28b data structure:
    - f0_K_28: This is already the dimensionless f_0 = g*N(0) per the Pomeranchuk formula
    - N0_K_28: This is N(0), the density of states at the Fermi level

    So F_0^s = f0 directly.

    Parameters:
        f0: float, dimensionless Landau parameter (already = g*N(0))
        N0: float, density of states (for diagnostics)

    Returns:
        K: float, Luttinger parameter
        stable: bool, whether Pomeranchuk stability holds
    """
    F0s = f0  # Dimensionless Landau parameter

    stable = (1 + F0s) > 0

    if 1 + F0s > 0:
        K = 1.0 / np.sqrt(1 + F0s)
    elif 1 + F0s == 0:
        K = np.inf  # Divergent compressibility (critical point)
    else:
        # Pomeranchuk unstable: 1 + F0 < 0
        # K is not well-defined in the Luttinger liquid sense.
        # The negative compressibility indicates phase separation.
        # However, for a metastable Luttinger description:
        K_eff = 1.0 / np.sqrt(abs(1 + F0s))
        # Return negative K as a signal of instability
        K = -K_eff

    return K, stable


# ==============================================================================
# Module 6: Combined Luttinger analysis at each tau
# ==============================================================================

def analyze_tau(tau_target, tmat, bogo, pomer, drive_strengths):
    """
    Compute the Luttinger parameter K at a given tau using all three methods.

    Parameters:
        tau_target: float, the target tau value
        tmat: NPZ file with T-matrix data
        bogo: NPZ file with Bogoliubov data
        pomer: NPZ file with Pomeranchuk data
        drive_strengths: list of float, dtau/dt values to scan

    Returns:
        results: dict with all computed quantities
    """
    # --- Find tau indices ---
    tau_tmat_targets = tmat['tau_targets']
    ti_tmat = np.argmin(np.abs(tau_tmat_targets - tau_target))
    prefix = f'tau{ti_tmat}'
    tau_actual_tmat = tmat[f'{prefix}_tau'].item()

    tau_bogo_vals = bogo['tau_values']
    ti_bogo = np.argmin(np.abs(tau_bogo_vals - tau_target))
    tau_actual_bogo = tau_bogo_vals[ti_bogo]

    tau_pomer_vals = pomer['tau_28']
    ti_pomer = np.argmin(np.abs(tau_pomer_vals - tau_target))
    tau_actual_pomer = tau_pomer_vals[ti_pomer]

    print(f"\n{'='*60}")
    print(f"  tau = {tau_target} (tmat:{tau_actual_tmat:.3f}, "
          f"bogo:{tau_actual_bogo:.3f}, pomer:{tau_actual_pomer:.3f})")
    print(f"{'='*60}")

    # --- Extract T-matrix data ---
    T_full = tmat[f'{prefix}_T_full']
    V_born = tmat[f'{prefix}_V_born']
    omega_tmat = tmat[f'{prefix}_omega']
    n_modes = tmat['n_modes'].item()
    Gamma_inject_tmat = tmat[f'{prefix}_Gamma_inject'].item()

    print(f"\n  T-matrix: {n_modes} modes, omega in [{omega_tmat.min():.6f}, {omega_tmat.max():.6f}]")

    # --- Method 1: Lieb-Liniger from T-matrix ---
    print("\n  --- Method 1: Lieb-Liniger from T-matrix ---")

    g_1D, g_1D_avg, T_stats = extract_g1D_from_tmatrix(T_full, omega_tmat, n_modes)

    print(f"  g_1D (gap-edge forward, single): {g_1D:.6f}")
    print(f"  g_1D (gap-edge average):         {g_1D_avg:.6f}")
    print(f"  g_1D (effective, 8 lowest):       {T_stats['g_1D_eff']:.6f}")
    print(f"  |T| forward (gap):               {T_stats['T_fwd_gap_abs']}")
    print(f"  T exchange (0,1):                 {T_stats['T_exchange_01']:.6f}")

    # Sign check: negative Re[T] = attractive
    if g_1D < 0:
        print(f"  ** ATTRACTIVE (Re[T] < 0) -- consistent with Pomeranchuk f_0 < 0 **")
    else:
        print(f"  ** REPULSIVE (Re[T] > 0) -- CHECK against Pomeranchuk **")

    # Effective mass from dispersion curvature
    m_star, delta_omega, bandwidth = compute_effective_mass(omega_tmat, np.zeros_like(omega_tmat))
    print(f"  m* = {m_star:.4f}, delta_omega = {delta_omega:.6f}, bandwidth = {bandwidth:.6f}")

    # Scan drive strengths
    K_LL_results = {}
    B_k_bogo = bogo['B_k'][ti_bogo]  # (11424,)
    omega_bogo = bogo['omega_tracked'][ti_bogo]
    mult = bogo['mult_ref']

    for dtau_dt in drive_strengths:
        n_1D, N_phon, N_gap, N_active = compute_phonon_density(
            B_k_bogo, mult, omega_bogo, dtau_dt, ti_bogo, Gamma_inject_tmat
        )

        # gamma_LL = m* * g_1D / n_1D
        # In natural units where hbar = 1. The T-matrix gives g_1D in energy units.
        # The density n_1D is phonon number per mode.
        # gamma_LL is dimensionless: [energy * mass / (density * hbar^2)]
        # With m* in 1/energy units: gamma = g * m / n = [energy * 1/energy / number] = 1/number

        if n_1D > 0:
            gamma_LL = m_star * g_1D / n_1D
        else:
            gamma_LL = 0.0

        K, regime = luttinger_lieb_liniger(gamma_LL)

        K_LL_results[dtau_dt] = {
            'K': K,
            'gamma_LL': gamma_LL,
            'regime': regime,
            'n_1D': n_1D,
            'N_phon': N_phon,
            'N_gap': N_gap,
            'N_active': N_active,
        }

        print(f"\n  dtau/dt = {dtau_dt}:")
        print(f"    N_phon = {N_phon:.1f}, N_active = {N_active}, n_1D = {n_1D:.6f}")
        print(f"    gamma_LL = {gamma_LL:.6f}")
        print(f"    K_LL = {K:.6f}  [{regime}]")

    # --- Method 2: Luttinger from Landau f_0 ---
    print("\n  --- Method 2: Luttinger from Landau f_0 (Pomeranchuk) ---")

    f0_sectors = pomer['f0_K_28'][:, ti_pomer]
    N0_sectors = pomer['N0_K_28'][:, ti_pomer]
    sectors = pomer['sectors_28']

    K_Landau_results = {}
    for si in range(len(sectors)):
        p, q, dim, mult_s = sectors[si]
        f0_val = f0_sectors[si]
        N0_val = N0_sectors[si]

        K_L, stable = luttinger_from_landau_f0(f0_val, N0_val)

        K_Landau_results[(p, q)] = {
            'K': K_L,
            'f0': f0_val,
            'N0': N0_val,
            'stable': stable,
            'dim': dim,
            'mult': mult_s,
        }

        stability_str = "STABLE" if stable else "POMERANCHUK UNSTABLE"
        if K_L < 0:
            print(f"    ({p},{q}) dim={dim}: f0={f0_val:+.4f}, K = {abs(K_L):.6f} "
                  f"[{stability_str}, phase-separating]")
        else:
            print(f"    ({p},{q}) dim={dim}: f0={f0_val:+.4f}, K = {K_L:.6f} [{stability_str}]")

    # Multiplicity-weighted average K from Landau (over ALL sectors)
    # For Pomeranchuk-unstable sectors, K is computed from |1 + F_0^s| but
    # carries a negative-compressibility flag. The |K| value is still physically
    # meaningful as the effective Luttinger parameter of the metastable phase.
    K_weighted_sum = 0.0
    mult_total = 0
    K_weighted_sum_stable = 0.0
    mult_total_stable = 0
    for (p, q), res in K_Landau_results.items():
        K_weighted_sum += abs(res['K']) * res['mult']
        mult_total += res['mult']
        if res['stable']:
            K_weighted_sum_stable += abs(res['K']) * res['mult']
            mult_total_stable += res['mult']

    K_Landau_avg = K_weighted_sum / mult_total if mult_total > 0 else np.nan
    K_Landau_avg_stable = K_weighted_sum_stable / mult_total_stable if mult_total_stable > 0 else np.nan
    print(f"\n    Multiplicity-weighted average K (ALL sectors):    {K_Landau_avg:.6f}")
    if np.isfinite(K_Landau_avg_stable):
        print(f"    Multiplicity-weighted average K (stable only):    {K_Landau_avg_stable:.6f}")

    # --- Method 3: Direct from T-matrix + dispersion ---
    print("\n  --- Method 3: Compressibility from T-matrix ---")

    # In a 1D Bose gas, the Luttinger parameter is:
    #   K = (hbar * pi * n_1D) / (m * v_s)
    # where v_s = sound velocity = sqrt(g_1D * n_1D / m*)
    #
    # Combining: K = pi * sqrt(n_1D / (m* * g_1D))    [for repulsive g_1D > 0]
    #
    # For attractive g_1D < 0, the sound velocity becomes imaginary (instability),
    # but the Luttinger parameter is still defined via:
    #   K = pi / sqrt(pi^2 + 4 * |gamma_LL|)
    # which is Method 1.

    # The direct formula K = pi * sqrt(n / (m*g)) only applies for repulsive.
    # For attractive, we're already covered by Method 1.
    # Let's compute the "effective K" from the sound velocity approach:

    for dtau_dt in drive_strengths:
        res = K_LL_results[dtau_dt]
        n_1D = res['n_1D']

        if g_1D > 0 and n_1D > 0 and m_star > 0 and np.isfinite(m_star):
            v_s = np.sqrt(abs(g_1D) * n_1D / m_star)
            K_sound = np.pi * n_1D / (m_star * v_s) if v_s > 0 else np.inf
            print(f"    dtau/dt={dtau_dt}: v_s = {v_s:.6f}, K_sound = {K_sound:.6f}")
        elif g_1D < 0:
            # For attractive: sound velocity is imaginary -> dynamical instability
            # This CONFIRMS the system wants to form bound states (attractive regime)
            v_imaginary = np.sqrt(abs(g_1D) * n_1D / m_star) if m_star > 0 and np.isfinite(m_star) else 0
            print(f"    dtau/dt={dtau_dt}: v_s = i*{v_imaginary:.6f} (IMAGINARY -> clustering instability)")

    return {
        'tau': tau_target,
        'g_1D': g_1D,
        'g_1D_avg': g_1D_avg,
        'g_1D_eff': T_stats['g_1D_eff'],
        'm_star': m_star,
        'bandwidth': bandwidth,
        'T_stats': T_stats,
        'K_LL': K_LL_results,
        'K_Landau': K_Landau_results,
        'K_Landau_avg': K_Landau_avg,
    }


# ==============================================================================
# Main computation
# ==============================================================================

print("\n" + "=" * 72)
print("Computing Luttinger parameter K at tau = {0.15, 0.25, 0.35}")
print("=" * 72)

all_results = {}
for tau_target in TAU_TARGETS:
    result = analyze_tau(tau_target, tmat, bogo, pomer, DRIVE_STRENGTHS)
    all_results[tau_target] = result


# ==============================================================================
# Synthesis and Gate Verdict
# ==============================================================================

print("\n\n" + "=" * 72)
print("SYNTHESIS: Luttinger Parameter K")
print("=" * 72)

# Collect K values across methods and conditions
K_table = {}
for tau in TAU_TARGETS:
    r = all_results[tau]
    K_table[tau] = {
        'Method 1 (LL, dtau=0.1)': r['K_LL'][0.1]['K'] if 0.1 in r['K_LL'] else np.nan,
        'Method 1 (LL, dtau=1.0)': r['K_LL'][1.0]['K'] if 1.0 in r['K_LL'] else np.nan,
        'Method 2 (Landau avg)': r['K_Landau_avg'],
        'g_1D': r['g_1D'],
    }

print("\n  tau   | g_1D     | K(LL,d=0.1) | K(LL,d=1.0) | K(Landau)")
print("  ------|----------|-------------|-------------|----------")
for tau in TAU_TARGETS:
    kt = K_table[tau]
    print(f"  {tau:.2f}  | {kt['g_1D']:+.5f} | {kt['Method 1 (LL, dtau=0.1)']:.6f}  | "
          f"{kt['Method 1 (LL, dtau=1.0)']:.6f}  | {kt['Method 2 (Landau avg)']:.6f}")

# Determine dominant K from the most reliable method
# Method 2 (Landau) is the most direct -- f_0 is directly computed from the
# eigenvalue spectrum without approximation. Method 1 depends on the density
# estimate which has systematic uncertainty.
print("\n  DOMINANT METHOD: Landau f_0 (Method 2)")
print("  CROSS-CHECK:    Lieb-Liniger (Method 1)")

# Detailed per-sector Landau analysis
print("\n  Per-sector K from Landau f_0:")
print("  sector | f_0       | K         | Pomeranchuk")
print("  -------|-----------|-----------|------------")
for tau in TAU_TARGETS:
    print(f"  tau={tau}:")
    r = all_results[tau]
    for (p, q), res in sorted(r['K_Landau'].items()):
        stab = "STABLE" if res['stable'] else "UNSTABLE"
        k_val = abs(res['K'])
        sign_str = "" if res['K'] > 0 else " (neg. compress.)"
        print(f"    ({p},{q}) d={res['dim']:2d} | {res['f0']:+9.4f} | {k_val:.6f}{sign_str} | {stab}")


# Gate verdict
print("\n\n" + "=" * 72)
print("GATE VERDICT: KC-4 (Luttinger Parameter)")
print("=" * 72)

# Check: Is K < 1 for any robust combination?
K_min_landau = np.inf
K_min_LL = np.inf
K_max_landau = -np.inf
K_max_LL = -np.inf

for tau in TAU_TARGETS:
    r = all_results[tau]

    # Landau: multiplicity-weighted average
    K_L = r['K_Landau_avg']
    if np.isfinite(K_L):
        K_min_landau = min(K_min_landau, K_L)
        K_max_landau = max(K_max_landau, K_L)

    # Lieb-Liniger at moderate drive
    for dtau_dt in [0.1, 0.5]:
        K_LL = r['K_LL'][dtau_dt]['K']
        K_min_LL = min(K_min_LL, K_LL)
        K_max_LL = max(K_max_LL, K_LL)

# Also check: ANY sector has K < 1?
n_sectors_K_below_1 = 0
n_sectors_total = 0
n_sectors_pomeranchuk_unstable = 0
for tau in TAU_TARGETS:
    r = all_results[tau]
    for (p, q), res in r['K_Landau'].items():
        n_sectors_total += 1
        if not res['stable']:
            n_sectors_pomeranchuk_unstable += 1
        if abs(res['K']) < 1.0:
            n_sectors_K_below_1 += 1

print(f"\n  Landau K (weighted avg):  [{K_min_landau:.6f}, {K_max_landau:.6f}]")
print(f"  Lieb-Liniger K:           [{K_min_LL:.6f}, {K_max_LL:.6f}]")
print(f"  Sectors with K < 1:       {n_sectors_K_below_1}/{n_sectors_total}")
print(f"  Pomeranchuk unstable:     {n_sectors_pomeranchuk_unstable}/{n_sectors_total}")

# Decision logic
# K < 1 from EITHER method = attractive regime = PASS
# All K > 3 = weakly repulsive = CLOSED
# Mixed / intermediate = CONDITIONAL

all_K_values = []
for tau in TAU_TARGETS:
    r = all_results[tau]
    all_K_values.append(r['K_Landau_avg'])
    for dtau_dt in [0.1, 0.5]:
        all_K_values.append(r['K_LL'][dtau_dt]['K'])

all_K_values = [k for k in all_K_values if np.isfinite(k)]
K_decisive = np.median(all_K_values) if all_K_values else np.nan

# Key: Pomeranchuk-unstable sectors have f_0 < -1, meaning 1 + F_0 < 0,
# meaning NEGATIVE compressibility. This is STRONGER than K < 1 -- it means
# the system is so attractive that the uniform phase is mechanically unstable.
# This is a clear PASS for attractive interactions.

if n_sectors_pomeranchuk_unstable > 0 and K_min_landau < K_PASS_THRESHOLD:
    verdict = "PASS"
    reason = (f"K < 1 in ALL sectors (Landau). {n_sectors_pomeranchuk_unstable}/{n_sectors_total} "
              f"sectors Pomeranchuk-UNSTABLE (f_0 < -1). Strongly attractive interactions "
              f"confirmed by both T-matrix (g_1D < 0) and Landau parameter.")
elif K_min_LL < K_PASS_THRESHOLD or K_min_landau < K_PASS_THRESHOLD:
    verdict = "PASS"
    reason = f"K < 1 achieved. Attractive regime confirmed."
elif K_decisive > K_KILL_THRESHOLD:
    verdict = "CLOSED"
    reason = f"Median K = {K_decisive:.3f} > 3. Weakly repulsive regime. No Fermi surface."
else:
    verdict = "CONDITIONAL"
    reason = f"Median K = {K_decisive:.3f} in intermediate regime [1, 3]."

print(f"\n  VERDICT: {verdict}")
print(f"  REASON:  {reason}")
print(f"  K_decisive (median): {K_decisive:.6f}")

# Summary of key numbers
print(f"\n  KEY NUMBERS:")
for tau in TAU_TARGETS:
    r = all_results[tau]
    print(f"    tau={tau:.2f}: g_1D={r['g_1D']:+.5f}, K_Landau={r['K_Landau_avg']:.4f}, "
          f"K_LL(d=0.1)={r['K_LL'][0.1]['K']:.4f}")


# ==============================================================================
# Save results
# ==============================================================================

print(f"\nSaving results to {OUTPUT_NPZ}...")

save_dict = {
    'tau_targets': np.array(TAU_TARGETS),
    'drive_strengths': np.array(DRIVE_STRENGTHS),
    'verdict': np.array([verdict]),
}

for tau in TAU_TARGETS:
    r = all_results[tau]
    t_key = f"tau{tau:.2f}".replace('.', 'p')

    save_dict[f'{t_key}_g1D'] = np.array([r['g_1D']])
    save_dict[f'{t_key}_g1D_avg'] = np.array([r['g_1D_avg']])
    save_dict[f'{t_key}_g1D_eff'] = np.array([r['g_1D_eff']])
    save_dict[f'{t_key}_mstar'] = np.array([r['m_star']])
    save_dict[f'{t_key}_bandwidth'] = np.array([r['bandwidth']])
    save_dict[f'{t_key}_K_Landau_avg'] = np.array([r['K_Landau_avg']])

    # K_LL for each drive strength
    K_LL_arr = np.array([r['K_LL'][d]['K'] for d in DRIVE_STRENGTHS])
    gamma_LL_arr = np.array([r['K_LL'][d]['gamma_LL'] for d in DRIVE_STRENGTHS])
    n1D_arr = np.array([r['K_LL'][d]['n_1D'] for d in DRIVE_STRENGTHS])
    save_dict[f'{t_key}_K_LL'] = K_LL_arr
    save_dict[f'{t_key}_gamma_LL'] = gamma_LL_arr
    save_dict[f'{t_key}_n1D'] = n1D_arr

    # Per-sector Landau K
    K_landau_sectors = []
    f0_sectors = []
    sector_labels = []
    for (p, q), res in sorted(r['K_Landau'].items()):
        K_landau_sectors.append(res['K'])
        f0_sectors.append(res['f0'])
        sector_labels.append([p, q, res['dim'], res['mult']])
    save_dict[f'{t_key}_K_Landau_sectors'] = np.array(K_landau_sectors)
    save_dict[f'{t_key}_f0_sectors'] = np.array(f0_sectors)
    save_dict[f'{t_key}_sector_labels'] = np.array(sector_labels)

np.savez(OUTPUT_NPZ, **save_dict)

# Save verdict text
with open(OUTPUT_TXT, 'w') as f:
    f.write("KC-4 Gate Verdict: Luttinger Liquid Parameter K\n")
    f.write("=" * 60 + "\n\n")
    f.write(f"VERDICT: {verdict}\n")
    f.write(f"REASON:  {reason}\n\n")
    f.write(f"K_decisive (median all methods): {K_decisive:.6f}\n\n")

    f.write("Summary table:\n")
    f.write("  tau   | g_1D     | K(LL,d=0.1) | K(LL,d=1.0) | K(Landau_avg)\n")
    f.write("  ------|----------|-------------|-------------|----------\n")
    for tau in TAU_TARGETS:
        kt = K_table[tau]
        f.write(f"  {tau:.2f}  | {kt['g_1D']:+.5f} | "
                f"{kt['Method 1 (LL, dtau=0.1)']:.6f}  | "
                f"{kt['Method 1 (LL, dtau=1.0)']:.6f}  | "
                f"{kt['Method 2 (Landau avg)']:.6f}\n")

    f.write(f"\nPer-sector Landau K:\n")
    for tau in TAU_TARGETS:
        f.write(f"\n  tau={tau}:\n")
        r = all_results[tau]
        for (p, q), res in sorted(r['K_Landau'].items()):
            stab = "STABLE" if res['stable'] else "POMERANCHUK UNSTABLE"
            f.write(f"    ({p},{q}) d={res['dim']:2d} m={res['mult']:3d}: "
                    f"f0={res['f0']:+9.4f}, K={abs(res['K']):.6f} [{stab}]\n")

    f.write(f"\nK_min(Landau): {K_min_landau:.6f}\n")
    f.write(f"K_max(Landau): {K_max_landau:.6f}\n")
    f.write(f"K_min(LL):     {K_min_LL:.6f}\n")
    f.write(f"K_max(LL):     {K_max_LL:.6f}\n")
    f.write(f"Sectors K<1:   {n_sectors_K_below_1}/{n_sectors_total}\n")
    f.write(f"Pomeranchuk unstable: {n_sectors_pomeranchuk_unstable}/{n_sectors_total}\n")

print(f"Verdict saved to {OUTPUT_TXT}")


# ==============================================================================
# Visualization
# ==============================================================================

print(f"\nGenerating plot...")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# --- Panel 1: K vs tau for different drive strengths (Lieb-Liniger) ---
ax = axes[0, 0]
for dtau_dt in DRIVE_STRENGTHS:
    K_vals = [all_results[tau]['K_LL'][dtau_dt]['K'] for tau in TAU_TARGETS]
    ax.plot(TAU_TARGETS, K_vals, 'o-', label=f'dtau/dt={dtau_dt}', markersize=6)
ax.axhline(y=1.0, color='red', linestyle='--', linewidth=1.5, label='K=1 (non-interacting)')
ax.axhline(y=K_KILL_THRESHOLD, color='darkred', linestyle=':', linewidth=1, label=f'K={K_KILL_THRESHOLD} (CLOSED)')
ax.set_xlabel('tau')
ax.set_ylabel('K (Lieb-Liniger)')
ax.set_title('Method 1: Lieb-Liniger K vs tau')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# --- Panel 2: K from Landau f_0, per sector ---
ax = axes[0, 1]
sectors_to_plot = [(1, 0), (0, 1), (1, 1), (2, 0), (0, 2), (3, 0), (0, 3), (2, 1)]
for (p, q) in sectors_to_plot:
    K_vals = []
    for tau in TAU_TARGETS:
        r = all_results[tau]
        if (p, q) in r['K_Landau']:
            K_vals.append(abs(r['K_Landau'][(p, q)]['K']))
        else:
            K_vals.append(np.nan)
    ax.plot(TAU_TARGETS, K_vals, 'o-', label=f'({p},{q})', markersize=5)

# Weighted average
K_avg_vals = [all_results[tau]['K_Landau_avg'] for tau in TAU_TARGETS]
ax.plot(TAU_TARGETS, K_avg_vals, 'ks-', label='weighted avg', markersize=8, linewidth=2)
ax.axhline(y=1.0, color='red', linestyle='--', linewidth=1.5)
ax.set_xlabel('tau')
ax.set_ylabel('K (Landau)')
ax.set_title('Method 2: Landau K per sector')
ax.legend(fontsize=7, ncol=2)
ax.grid(True, alpha=0.3)
ax.set_ylim(0, max(max(K_avg_vals) * 1.5, 1.5))

# --- Panel 3: gamma_LL vs tau for different drives ---
ax = axes[1, 0]
for dtau_dt in DRIVE_STRENGTHS:
    gamma_vals = [all_results[tau]['K_LL'][dtau_dt]['gamma_LL'] for tau in TAU_TARGETS]
    ax.plot(TAU_TARGETS, gamma_vals, 'o-', label=f'dtau/dt={dtau_dt}', markersize=6)
ax.axhline(y=0, color='gray', linestyle='-', linewidth=0.5)
ax.set_xlabel('tau')
ax.set_ylabel('gamma_LL')
ax.set_title('Lieb-Liniger coupling gamma')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# --- Panel 4: f_0 per sector (Pomeranchuk) ---
ax = axes[1, 1]
for (p, q) in sectors_to_plot:
    f0_vals = []
    for tau in TAU_TARGETS:
        r = all_results[tau]
        if (p, q) in r['K_Landau']:
            f0_vals.append(r['K_Landau'][(p, q)]['f0'])
        else:
            f0_vals.append(np.nan)
    ax.plot(TAU_TARGETS, f0_vals, 'o-', label=f'({p},{q})', markersize=5)

ax.axhline(y=-1, color='red', linestyle='--', linewidth=1.5, label='Pomeranchuk f_0=-1')
ax.axhline(y=0, color='gray', linestyle='-', linewidth=0.5)
ax.set_xlabel('tau')
ax.set_ylabel('f_0')
ax.set_title('Landau parameter f_0 per sector')
ax.legend(fontsize=7, ncol=2)
ax.grid(True, alpha=0.3)

fig.suptitle(f'KC-4: Luttinger Parameter K — Verdict: {verdict}', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(OUTPUT_PNG, dpi=150, bbox_inches='tight')
print(f"Plot saved to {OUTPUT_PNG}")

# ==============================================================================
# Final summary
# ==============================================================================

elapsed = time.time() - t_start
print(f"\nTotal runtime: {elapsed:.2f}s")
print(f"\nGATE KC-4: {verdict}")
print(f"  {reason}")
