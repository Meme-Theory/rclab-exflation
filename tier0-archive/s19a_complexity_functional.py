"""
Session 19a — S-5: Spectral Complexity Functional Omega(tau)
============================================================

Synthesizes diagnostics S-1 (level statistics), S-2 (spectral dimension),
and S-3 (spectral entropy) into a single complexity functional:

    Omega(tau) = d_s(tau, sigma_*) * S(tau, beta_*) * R_reg(tau) / R_reg(0)

where:
    d_s = spectral dimension at fiducial diffusion time sigma_*
    S   = spectral Shannon entropy at fiducial inverse temperature beta_*
    R_reg = regularized inter-sector level repulsion

The inter-sector level repulsion R_reg(tau) is computed independently here:

    R_reg(tau) = Sum_{n<m, sectors differ} 1 / [(lambda_n - lambda_m)^2 + epsilon^2]

This measures the pairwise interaction strength between eigenvalues in
DIFFERENT Peter-Weyl sectors. At tau=0, eigenvalues from different sectors
are uncorrelated (Poisson-like). At tau > 0, the Jensen deformation creates
inter-sector coupling via non-Killing C^2 fields (Paper 17 eq 3.8), pushing
eigenvalues apart (level repulsion).

Theoretical framework (Tesla-Resonance):
- R_reg captures the Anderson localization transition: localized (sector-pure)
  eigenspinors have no inter-sector repulsion; delocalized eigenspinors do.
- The Omega functional has a maximum at the point of maximum spectral complexity:
  where the internal geometry has the richest structure.
- This maximum is the "complexity-selected vacuum" — the spectral phase transition
  point tau_c where the universe's internal geometry supports the observed particle
  spectrum.

Constraint Conditions:
- CLOSED: Omega(tau) monotonically increasing with no structure.
- CLOSED: R_reg(tau) flat or monotonically increasing without inflection.
- CONFIRM: Omega(tau) has a maximum or plateau at tau_c consistent with S-1.

Author: Tesla-Resonance agent (Session 19a)
Date: 2026-02-15

References:
    - Session 19 Primer, Section II.5: Spectral Complexity Functional
    - Berry & Tabor (1977): Level clustering in regular spectrum
    - Bohigas, Giannoni, Schmit (1984): Chaotic spectra and GOE
    - Volovik (2003): Universe in a Helium Droplet (Paper 10)
    - Ambjorn, Jurkiewicz, Loll (2005): CDT spectral dimension (Paper 14)
"""

import sys
import os
import time
import numpy as np
from scipy.optimize import minimize_scalar
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Add tier0-computation to path for imports
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from s19a_sweep_data import load_sweep_data


# =============================================================================
# SECTION 1: INTER-SECTOR LEVEL REPULSION R_reg(tau)
# =============================================================================

def compute_inter_sector_repulsion(eigenvalues, sector_p, sector_q, epsilon=None):
    """
    Compute the regularized inter-sector level repulsion:

        R_reg = Sum_{n<m, sectors differ} 1 / [(lambda_n - lambda_m)^2 + epsilon^2]

    Only sums over pairs from DIFFERENT (p,q) sectors.

    Args:
        eigenvalues: (N,) array of |lambda| values
        sector_p: (N,) array of p-labels
        sector_q: (N,) array of q-labels
        epsilon: regularization parameter. If None, set to median intra-sector spacing
                 of the largest sector.

    Returns:
        R_reg: float, the inter-sector level repulsion
        epsilon_used: the epsilon value that was used
    """
    N = len(eigenvalues)

    # Determine epsilon from intra-sector spacing if not provided
    if epsilon is None:
        epsilon = _compute_epsilon(eigenvalues, sector_p, sector_q)

    eps2 = epsilon ** 2

    # Build sector identifiers for fast comparison
    sector_ids = sector_p * 1000 + sector_q  # unique sector ID

    # Compute pairwise repulsion for inter-sector pairs
    # O(N^2) but N ~ 1400 so this is ~10^6 pairs, fast
    R_reg = 0.0
    n_pairs = 0

    for n in range(N):
        for m in range(n + 1, N):
            if sector_ids[n] != sector_ids[m]:
                delta_sq = (eigenvalues[n] - eigenvalues[m]) ** 2
                R_reg += 1.0 / (delta_sq + eps2)
                n_pairs += 1

    return R_reg, epsilon, n_pairs


def compute_inter_sector_repulsion_vectorized(eigenvalues, sector_p, sector_q, epsilon=None):
    """
    Vectorized version of inter-sector level repulsion.
    Uses broadcasting for speed on large arrays.

    For N ~ 1400, the full pairwise matrix is 1400x1400 ~ 2M entries, ~16 MB.
    Fits easily in memory.
    """
    N = len(eigenvalues)

    if epsilon is None:
        epsilon = _compute_epsilon(eigenvalues, sector_p, sector_q)

    eps2 = epsilon ** 2

    # Build sector IDs
    sector_ids = sector_p * 1000 + sector_q

    # Pairwise differences: (N, N) matrix
    # Only upper triangle matters (n < m)
    diff_sq = (eigenvalues[:, None] - eigenvalues[None, :]) ** 2  # (N, N)

    # Inter-sector mask: True where sectors differ
    inter_mask = sector_ids[:, None] != sector_ids[None, :]  # (N, N)

    # Upper triangle mask
    upper = np.triu(np.ones((N, N), dtype=bool), k=1)

    # Combined mask
    mask = inter_mask & upper

    # Compute repulsion
    repulsion_matrix = 1.0 / (diff_sq + eps2)
    R_reg = np.sum(repulsion_matrix[mask])
    n_pairs = int(np.sum(mask))

    return R_reg, epsilon, n_pairs


def _compute_epsilon(eigenvalues, sector_p, sector_q):
    """
    Compute the regularization epsilon as the median intra-sector spacing
    of the largest sector (by number of eigenvalues).
    """
    sector_ids = sector_p * 1000 + sector_q
    unique_sectors = np.unique(sector_ids)

    # Find the largest sector
    max_count = 0
    largest_sector_evals = None
    for sid in unique_sectors:
        mask = sector_ids == sid
        count = np.sum(mask)
        if count > max_count:
            max_count = count
            largest_sector_evals = np.sort(eigenvalues[mask])

    if largest_sector_evals is not None and len(largest_sector_evals) > 1:
        spacings = np.diff(largest_sector_evals)
        spacings = spacings[spacings > 1e-12]  # exclude degenerate pairs
        if len(spacings) > 0:
            return float(np.median(spacings))

    # Fallback: use median of all spacings
    sorted_evals = np.sort(eigenvalues)
    spacings = np.diff(sorted_evals)
    spacings = spacings[spacings > 1e-12]
    return float(np.median(spacings)) if len(spacings) > 0 else 0.01


# =============================================================================
# SECTION 2: SPECTRAL DIMENSION d_s(tau, sigma) — from S-2 data or recomputed
# =============================================================================

def compute_spectral_dimension(eigenvalues, multiplicities, sigma):
    """
    Compute the spectral dimension at a given sigma:

        K(sigma) = Sum_n mult_n * exp(-sigma * lambda_n^2)
        d_s = -2 * d(log K) / d(log sigma)

    Uses central finite differences in log-space for the derivative.

    Args:
        eigenvalues: (N,) array of |lambda|
        multiplicities: (N,) array of PW multiplicities
        sigma: float, diffusion time

    Returns:
        d_s: spectral dimension at this sigma
    """
    d_log_sigma = 0.01  # step in log-space

    sigma_minus = sigma * np.exp(-d_log_sigma)
    sigma_plus = sigma * np.exp(d_log_sigma)

    K_minus = np.sum(multiplicities * np.exp(-sigma_minus * eigenvalues ** 2))
    K_center = np.sum(multiplicities * np.exp(-sigma * eigenvalues ** 2))
    K_plus = np.sum(multiplicities * np.exp(-sigma_plus * eigenvalues ** 2))

    if K_minus <= 0 or K_plus <= 0 or K_center <= 0:
        return 0.0

    log_K_minus = np.log(K_minus)
    log_K_plus = np.log(K_plus)

    d_logK_d_logsigma = (log_K_plus - log_K_minus) / (2 * d_log_sigma)

    return -2.0 * d_logK_d_logsigma


def compute_spectral_dimension_curve(eigenvalues, multiplicities, sigma_values):
    """Compute d_s at multiple sigma values."""
    return np.array([
        compute_spectral_dimension(eigenvalues, multiplicities, s)
        for s in sigma_values
    ])


# =============================================================================
# SECTION 3: SPECTRAL ENTROPY S(tau, beta) — from S-3 data or recomputed
# =============================================================================

def compute_spectral_entropy(eigenvalues, multiplicities, beta):
    """
    Compute the spectral Shannon entropy:

        Z = Sum_n mult_n * exp(-beta * lambda_n^2)
        p_n = mult_n * exp(-beta * lambda_n^2) / Z
        S = -Sum_n p_n * log(p_n)

    Args:
        eigenvalues: (N,) array of |lambda|
        multiplicities: (N,) array of PW multiplicities
        beta: inverse temperature

    Returns:
        S: Shannon entropy
        Z: partition function
    """
    log_boltzmann = -beta * eigenvalues ** 2
    # Shift for numerical stability
    log_boltzmann_shifted = log_boltzmann - np.max(log_boltzmann)

    weights = multiplicities * np.exp(log_boltzmann_shifted)
    Z = np.sum(weights)

    if Z <= 0:
        return 0.0, 0.0

    p = weights / Z
    # Avoid log(0)
    mask = p > 1e-300
    S = -np.sum(p[mask] * np.log(p[mask]))

    return S, Z


# =============================================================================
# SECTION 4: COMPLEXITY FUNCTIONAL Omega(tau)
# =============================================================================

def compute_complexity_functional(data, sigma_star=1.0, beta_star=1.0):
    """
    Compute the Spectral Complexity Functional across all tau-values:

        Omega(tau) = d_s(tau, sigma_*) * S(tau, beta_*) * R_reg(tau) / R_reg(0)

    IMPORTANT: epsilon for R_reg is computed ONCE from the tau=0 spectrum
    and held FIXED across all tau-values. This prevents the regularization
    from dominating the tau-dependence of R_reg.

    Args:
        data: sweep data dict from load_sweep_data()
        sigma_star: fiducial diffusion time for spectral dimension
        beta_star: fiducial inverse temperature for entropy

    Returns:
        results: dict with keys:
            'tau_values': (N_tau,) array
            'd_s': (N_tau,) array of spectral dimensions
            'S': (N_tau,) array of spectral entropies
            'R_reg': (N_tau,) array of inter-sector level repulsion
            'Omega': (N_tau,) array of complexity functional
            'epsilon': float, the fixed regularization parameter
            'n_inter_pairs': (N_tau,) array of number of inter-sector pairs
    """
    tau_values = data['tau_values']
    N_tau = len(tau_values)

    d_s_arr = np.zeros(N_tau)
    S_arr = np.zeros(N_tau)
    R_reg_arr = np.zeros(N_tau)
    n_pairs_arr = np.zeros(N_tau, dtype=int)

    # Compute epsilon ONCE from tau=0 data (fixed regularization)
    epsilon_fixed = _compute_epsilon(
        data['eigenvalues'][0], data['sector_p'][0], data['sector_q'][0]
    )
    print("Computing Omega(tau) components...")
    print(f"  sigma_* = {sigma_star:.4f}")
    print(f"  beta_* = {beta_star:.4f}")
    print(f"  epsilon (fixed from tau=0) = {epsilon_fixed:.6f}")

    for i, tau in enumerate(tau_values):
        t_start = time.time()

        evals = data['eigenvalues'][i]
        sp = data['sector_p'][i]
        sq = data['sector_q'][i]
        mults = data['multiplicities'][i]

        # Component 1: Spectral dimension
        d_s_arr[i] = compute_spectral_dimension(evals, mults, sigma_star)

        # Component 2: Spectral entropy
        S_arr[i], _ = compute_spectral_entropy(evals, mults, beta_star)

        # Component 3: Inter-sector level repulsion (vectorized, FIXED epsilon)
        R_reg_arr[i], _, n_pairs_arr[i] = \
            compute_inter_sector_repulsion_vectorized(evals, sp, sq, epsilon=epsilon_fixed)

        dt = time.time() - t_start
        print(f"  tau={tau:.2f}: d_s={d_s_arr[i]:.4f}, S={S_arr[i]:.4f}, "
              f"R_reg={R_reg_arr[i]:.4e}, "
              f"n_pairs={n_pairs_arr[i]}, time={dt:.1f}s")

    # Normalize R_reg by R_reg(0)
    R_reg_0 = R_reg_arr[0] if R_reg_arr[0] > 0 else 1.0
    R_reg_normalized = R_reg_arr / R_reg_0

    # Complexity functional
    Omega = d_s_arr * S_arr * R_reg_normalized

    return {
        'tau_values': tau_values,
        'd_s': d_s_arr,
        'S': S_arr,
        'R_reg': R_reg_arr,
        'R_reg_normalized': R_reg_normalized,
        'Omega': Omega,
        'epsilon': epsilon_fixed,
        'n_inter_pairs': n_pairs_arr,
        'sigma_star': sigma_star,
        'beta_star': beta_star,
    }


# =============================================================================
# SECTION 5: ANALYSIS AND STRUCTURE DETECTION
# =============================================================================

def find_extrema(tau_values, y_values, name="y"):
    """
    Find local maxima and minima in a 1D array.
    Uses simple comparison with neighbors.

    Returns:
        maxima: list of (tau, y) tuples
        minima: list of (tau, y) tuples
    """
    maxima = []
    minima = []

    for i in range(1, len(y_values) - 1):
        if y_values[i] > y_values[i-1] and y_values[i] > y_values[i+1]:
            maxima.append((tau_values[i], y_values[i]))
        if y_values[i] < y_values[i-1] and y_values[i] < y_values[i+1]:
            minima.append((tau_values[i], y_values[i]))

    if maxima:
        print(f"  {name} local maxima: {len(maxima)}")
        for tau, val in maxima:
            print(f"    tau = {tau:.2f}: {name} = {val:.6f}")
    else:
        print(f"  {name}: NO local maxima detected (monotonic or flat)")

    return maxima, minima


def find_inflection_points(tau_values, y_values, name="y"):
    """
    Find inflection points (where the second derivative changes sign).
    Uses central differences for d^2y/dtau^2.

    Returns:
        inflections: list of (tau, y, d2y) tuples
    """
    dtau = np.diff(tau_values)
    # First derivative
    dy = np.diff(y_values) / dtau
    # Second derivative (on interior points)
    tau_mid = (tau_values[:-1] + tau_values[1:]) / 2
    dtau_mid = np.diff(tau_mid)
    d2y = np.diff(dy) / dtau_mid

    inflections = []
    for i in range(len(d2y) - 1):
        if d2y[i] * d2y[i+1] < 0:  # sign change
            # Linear interpolation for the zero crossing
            frac = -d2y[i] / (d2y[i+1] - d2y[i])
            tau_infl = tau_mid[i+1] + frac * dtau_mid[i] if i+1 < len(dtau_mid) else tau_mid[i+1]
            y_infl = np.interp(tau_infl, tau_values, y_values)
            inflections.append((tau_infl, y_infl))

    if inflections:
        print(f"  {name} inflection points: {len(inflections)}")
        for tau, val in inflections:
            print(f"    tau = {tau:.3f}: {name} = {val:.6f}")
    else:
        print(f"  {name}: NO inflection points detected")

    return inflections


# =============================================================================
# SECTION 6: PLOTTING
# =============================================================================

def plot_complexity_results(results, output_dir):
    """Generate plots for the complexity functional analysis."""

    tau = results['tau_values']

    # --- Plot 1: All three components ---
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    ax = axes[0, 0]
    ax.plot(tau, results['d_s'], 'b-o', markersize=4, label=f"sigma*={results['sigma_star']:.1f}")
    ax.axhline(y=8, color='gray', linestyle='--', alpha=0.5, label='d_s = 8 (bi-invariant)')
    ax.axhline(y=4, color='red', linestyle='--', alpha=0.5, label='d_s = 4 (CDT target)')
    ax.set_xlabel('tau')
    ax.set_ylabel('d_s')
    ax.set_title('Spectral Dimension')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    ax = axes[0, 1]
    ax.plot(tau, results['S'], 'g-o', markersize=4, label=f"beta*={results['beta_star']:.1f}")
    ax.set_xlabel('tau')
    ax.set_ylabel('S')
    ax.set_title('Spectral Entropy')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    ax = axes[1, 0]
    ax.plot(tau, results['R_reg_normalized'], 'r-o', markersize=4)
    ax.set_xlabel('tau')
    ax.set_ylabel('R_reg / R_reg(0)')
    ax.set_title('Normalized Inter-Sector Repulsion')
    ax.grid(True, alpha=0.3)

    ax = axes[1, 1]
    ax.plot(tau, results['Omega'], 'k-o', markersize=5, linewidth=2)
    ax.set_xlabel('tau')
    ax.set_ylabel('Omega(tau)')
    ax.set_title('Spectral Complexity Functional')
    ax.grid(True, alpha=0.3)

    # Mark any maxima
    maxima, _ = find_extrema(tau, results['Omega'], "Omega")
    for tau_m, omega_m in maxima:
        ax.axvline(x=tau_m, color='red', linestyle=':', alpha=0.7)
        ax.annotate(f'tau_c={tau_m:.2f}', xy=(tau_m, omega_m),
                    xytext=(tau_m + 0.1, omega_m),
                    fontsize=9, color='red')

    plt.suptitle('S-5: Spectral Complexity Functional Omega(tau)', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 's19a_complexity_functional.png'), dpi=150)
    plt.close()
    print(f"  Saved: {os.path.join(output_dir, 's19a_complexity_functional.png')}")

    # --- Plot 2: dOmega/dtau and inflection points ---
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Numerical derivative of Omega
    dtau = np.diff(tau)
    dOmega = np.diff(results['Omega']) / dtau
    tau_mid = (tau[:-1] + tau[1:]) / 2

    ax = axes[0]
    ax.plot(tau_mid, dOmega, 'k-o', markersize=4)
    ax.axhline(y=0, color='gray', linestyle='--', alpha=0.5)
    ax.set_xlabel('tau')
    ax.set_ylabel('dOmega/dtau')
    ax.set_title('Complexity Growth Rate')
    ax.grid(True, alpha=0.3)

    # dR_reg/dtau
    dR = np.diff(results['R_reg_normalized']) / dtau
    ax = axes[1]
    ax.plot(tau_mid, dR, 'r-o', markersize=4)
    ax.axhline(y=0, color='gray', linestyle='--', alpha=0.5)
    ax.set_xlabel('tau')
    ax.set_ylabel('d(R_reg/R_0)/dtau')
    ax.set_title('Inter-Sector Repulsion Growth Rate')
    ax.grid(True, alpha=0.3)

    plt.suptitle('S-5: Growth Rates and Structure', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 's19a_complexity_derivatives.png'), dpi=150)
    plt.close()
    print(f"  Saved: {os.path.join(output_dir, 's19a_complexity_derivatives.png')}")

    # --- Plot 3: R_reg alone with physical reference lines ---
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(tau, results['R_reg'], 'r-o', markersize=5, linewidth=2, label='R_reg(tau)')
    ax.set_xlabel('tau', fontsize=12)
    ax.set_ylabel('R_reg(tau)', fontsize=12)
    ax.set_title('Inter-Sector Level Repulsion (absolute)', fontsize=14)

    # Reference lines at known tau values
    reference_taus = {
        0.15: 'phi mass ratio',
        0.164: 'Boltzmann min (17a)',
        0.2994: 'sin^2(theta_W)',
    }
    for t_ref, label in reference_taus.items():
        ax.axvline(x=t_ref, color='blue', linestyle=':', alpha=0.5)
        ax.text(t_ref + 0.02, ax.get_ylim()[1] * 0.95, label,
                fontsize=8, color='blue', rotation=90, va='top')

    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 's19a_inter_sector_repulsion.png'), dpi=150)
    plt.close()
    print(f"  Saved: {os.path.join(output_dir, 's19a_inter_sector_repulsion.png')}")


# =============================================================================
# SECTION 7: DECISION GATE ASSESSMENT
# =============================================================================

def assess_decision_gate(results):
    """
    Evaluate the spectral complexity hypothesis against closure/confirm conditions.

    Returns a structured assessment string.
    """
    tau = results['tau_values']
    Omega = results['Omega']
    R_reg = results['R_reg_normalized']
    d_s = results['d_s']

    assessment = []
    assessment.append("\n" + "=" * 70)
    assessment.append("S-5 DECISION GATE ASSESSMENT")
    assessment.append("=" * 70)

    # Check 1: Does Omega have structure?
    Omega_maxima, _ = find_extrema(tau, Omega, "Omega")
    Omega_inflections = find_inflection_points(tau, Omega, "Omega")

    if Omega_maxima:
        tau_c_omega = Omega_maxima[0][0]
        assessment.append(f"\n[CONFIRM] Omega(tau) has maximum at tau_c = {tau_c_omega:.3f}")
        assessment.append(f"  Omega_max = {Omega_maxima[0][1]:.6f}")

        # Check if tau_c is in the convergence range [0.15, 0.30]
        if 0.15 <= tau_c_omega <= 0.30:
            assessment.append(f"  *** tau_c IN [0.15, 0.30] — THREE ROUTES CONVERGE ***")
        elif tau_c_omega <= 0.50:
            assessment.append(f"  tau_c in [0.30, 0.50] — suggestive but not convergent")
        else:
            assessment.append(f"  tau_c > 0.50 — outside expected range")
    elif Omega_inflections:
        assessment.append(f"\n[PARTIAL] Omega has inflection but no maximum — plateau behavior")
    else:
        assessment.append(f"\n[CLOSED] Omega(tau) is featureless — no maximum, no inflection")
        assessment.append(f"  Spectral complexity functional adds nothing beyond components")

    # Check 2: Does R_reg show structure?
    R_maxima, _ = find_extrema(tau, R_reg, "R_reg")
    R_inflections = find_inflection_points(tau, R_reg, "R_reg")

    if R_maxima:
        assessment.append(f"\n[INFO] R_reg has maximum at tau = {R_maxima[0][0]:.3f}")
    elif R_inflections:
        assessment.append(f"\n[INFO] R_reg has inflection at tau = {R_inflections[0][0]:.3f}")
    else:
        assessment.append(f"\n[INFO] R_reg is monotonic (no maximum or inflection)")

    # Check 3: d_s departure from 8
    d_s_departure = np.max(np.abs(d_s - 8.0))
    d_s_at_0 = d_s[0]
    assessment.append(f"\n[INFO] d_s(tau=0) = {d_s_at_0:.4f} (expected: 8.0)")
    assessment.append(f"  Max departure from 8: {d_s_departure:.4f}")

    # Check if d_s crosses 4
    d_s_crosses_4 = False
    for i in range(len(d_s) - 1):
        if (d_s[i] - 4) * (d_s[i+1] - 4) < 0:
            frac = (4 - d_s[i]) / (d_s[i+1] - d_s[i])
            tau_cross = tau[i] + frac * (tau[i+1] - tau[i])
            assessment.append(f"  d_s = 4 crossing at tau ~ {tau_cross:.3f} [CDT CONNECTION]")
            d_s_crosses_4 = True

    if not d_s_crosses_4 and d_s_departure > 0.1:
        assessment.append(f"  d_s departs from 8 but does not reach 4 — partial CDT connection")
    elif d_s_departure < 0.1:
        assessment.append(f"  d_s ~ 8 everywhere — NO dimensional reduction [CLOSED for CDT]")

    assessment.append("\n" + "=" * 70)

    result_str = "\n".join(assessment)
    print(result_str)
    return result_str


# =============================================================================
# MAIN
# =============================================================================

if __name__ == '__main__':
    # Configuration
    DATA_PATH = os.path.join(SCRIPT_DIR, 's19a_sweep_data.npz')
    OUTPUT_DIR = SCRIPT_DIR
    SIGMA_STAR = 1.0    # Fiducial diffusion time
    BETA_STAR = 1.0     # Will be updated from S-3 beta-independence analysis

    print("Session 19a — S-5: Spectral Complexity Functional")
    print("=" * 60)

    # Check for data
    if not os.path.exists(DATA_PATH):
        print(f"ERROR: Sweep data not found at {DATA_PATH}")
        print("Run s19a_sweep_data.py first to generate eigenvalue data.")
        sys.exit(1)

    # Load sweep data
    print(f"\nLoading sweep data from {DATA_PATH}...")
    data = load_sweep_data(DATA_PATH)
    tau_values = data['tau_values']
    print(f"  {len(tau_values)} tau-values loaded, range [{tau_values[0]:.1f}, {tau_values[-1]:.1f}]")

    # Compute complexity functional
    print(f"\nComputing Omega(tau) with sigma*={SIGMA_STAR}, beta*={BETA_STAR}...")
    results = compute_complexity_functional(data, sigma_star=SIGMA_STAR, beta_star=BETA_STAR)

    # Analysis: find extrema and inflection points
    print("\n--- Structure Detection ---")
    print("\nOmega(tau):")
    find_extrema(tau_values, results['Omega'], "Omega")
    find_inflection_points(tau_values, results['Omega'], "Omega")

    print("\nR_reg/R_0:")
    find_extrema(tau_values, results['R_reg_normalized'], "R_reg")
    find_inflection_points(tau_values, results['R_reg_normalized'], "R_reg")

    print("\nd_s:")
    find_extrema(tau_values, results['d_s'], "d_s")

    print("\nS:")
    find_extrema(tau_values, results['S'], "S")

    # Decision gate
    gate = assess_decision_gate(results)

    # Plots
    print("\n--- Generating Plots ---")
    plot_complexity_results(results, OUTPUT_DIR)

    # Print summary table
    print("\n--- Summary Table ---")
    print(f"{'tau':>6s}  {'d_s':>8s}  {'S':>10s}  {'R_reg':>12s}  {'R_reg/R0':>10s}  {'Omega':>12s}")
    print("-" * 70)
    for i, tau in enumerate(tau_values):
        print(f"{tau:6.2f}  {results['d_s'][i]:8.4f}  {results['S'][i]:10.4f}  "
              f"{results['R_reg'][i]:12.4e}  {results['R_reg_normalized'][i]:10.6f}  "
              f"{results['Omega'][i]:12.6f}")

    print("\nDone.")
