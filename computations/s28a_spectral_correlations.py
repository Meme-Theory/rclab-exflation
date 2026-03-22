"""
SESSION 28a COMPUTATION C-4: SPECTRAL CORRELATION R_2(s)
=========================================================

Compute the two-point spectral correlation function for D_K and D_can
spectra across Peter-Weyl sectors. Wigner-Dyson statistics (GUE/GOE)
indicate spectral rigidity from quantum chaos; Poisson statistics indicate
integrability.

Physics:
  D_K is exactly block-diagonal in Peter-Weyl (Session 22b Theorem 2).
  Within each block, the Dirac operator is a finite Hermitian matrix of
  size dim(p,q)*16. Random matrix theory predicts:
    - Integrable systems -> Poisson: P(s) = exp(-s), no level repulsion
    - Chaotic systems -> Wigner-Dyson: P(s) ~ s^beta * exp(-c*s^2),
      with beta = 1 (GOE, time-reversal), 2 (GUE, broken TR), 4 (GSE)
  The Brody distribution interpolates: P(s;q) ~ s^q * exp(-c*s^{q+1}),
  with q=0 (Poisson) and q=1 (GOE) as limits.

  CRITICAL NOTE from Session 19a: D_K block-diagonal means eigenvalues
  from different sectors are UNCORRELATED by construction. Poisson-to-GOE
  transition CANNOT be tested by pooling sectors. We test WITHIN each
  sector individually. Sectors with dim(p,q)*16 < 30 have too few
  eigenvalues for reliable statistics, so we focus on larger sectors.

  D_can = M_Lie (canonical connection Dirac) is also block-diagonal
  (same Peter-Weyl structure). It represents the pure Lie derivative
  without spin connection. Comparing D_K vs D_can statistics tests
  whether the spin connection (Omega_LC) induces/destroys spectral chaos.

Method:
  1. For each sector and tau: extract D_K eigenvalues from s27 data
  2. Recompute D_can eigenvalues from tier1 infrastructure
  3. Spectral unfolding: staircase -> polynomial fit -> rescaled spacings
  4. Nearest-neighbor spacing distribution P(s) and number variance
  5. Brody distribution fit: P(s) = A*s^q*exp(-c*s^{q+1}), report q
  6. Compare D_can vs D_K at each tau

Input:
  tier0-computation/s27_multisector_bcs.npz (D_K eigenvalues, 9 sectors, 9 tau)

Output:
  tier0-computation/s28a_spectral_correlations.npz
  tier0-computation/s28a_spectral_correlations.png

Gate C-4: DIAGNOSTIC
  Wigner-Dyson in D_can but Poisson in D_K at the same tau would indicate
  torsion induces spectral chaos. Conversely, GOE in D_K but Poisson in
  D_can would mean spin connection drives level repulsion.

Author: phonon-exflation-sim agent (Session 28a)
Date: 2026-02-27
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.special import gamma as gamma_func
import sys
import os
import time

# Add tier0-computation to path for tier1 imports
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from tier1_dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    jensen_metric, orthonormal_frame, frame_structure_constants,
    connection_coefficients, spinor_connection_offset, build_cliff8,
    dirac_operator_on_irrep, get_irrep, _irrep_cache
)

OUTDIR = SCRIPT_DIR


# =============================================================================
# BRODY DISTRIBUTION
# =============================================================================

def brody_pdf(s, q):
    """
    Brody distribution PDF.

    P(s; q) = (q+1) * b * s^q * exp(-b * s^{q+1})

    where b = [Gamma((q+2)/(q+1))]^{q+1} ensures <s> = 1 after unfolding.

    Interpolates between:
      q = 0: Poisson (exponential), P(s) = exp(-s)
      q = 1: Wigner (GOE), P(s) = (pi/2)*s*exp(-pi*s^2/4)

    Args:
        s: array of spacings (non-negative)
        q: Brody parameter in [0, 1]

    Returns:
        P(s): probability density values
    """
    b = (gamma_func((q + 2.0) / (q + 1.0))) ** (q + 1.0)
    return (q + 1.0) * b * s**q * np.exp(-b * s**(q + 1.0))


def brody_cdf(s, q):
    """
    Brody distribution CDF.

    F(s; q) = 1 - exp(-b * s^{q+1})

    Args:
        s: array of spacings
        q: Brody parameter

    Returns:
        F(s): cumulative distribution values
    """
    b = (gamma_func((q + 2.0) / (q + 1.0))) ** (q + 1.0)
    return 1.0 - np.exp(-b * s**(q + 1.0))


def fit_brody(spacings, method='mle'):
    """
    Fit the Brody parameter q to a set of nearest-neighbor spacings.

    Uses maximum likelihood estimation (MLE) via the relationship:
    For Brody distribution, the MLE of q satisfies:
      <ln(s)> = [psi((q+2)/(q+1)) - ln(b)] / (q+1)
    where psi is the digamma function.

    We use scipy curve_fit on the CDF for robustness.

    Args:
        spacings: 1D array of unfolded nearest-neighbor spacings
        method: 'cdf' (default, robust) or 'hist' (binned)

    Returns:
        q: fitted Brody parameter
        q_err: estimated uncertainty (from covariance)
    """
    s = np.sort(spacings)
    s = s[s > 0]  # Remove exact zeros

    if len(s) < 10:
        return np.nan, np.nan

    # CDF fitting method (most robust)
    empirical_cdf = np.arange(1, len(s) + 1) / len(s)

    try:
        popt, pcov = curve_fit(brody_cdf, s, empirical_cdf,
                               p0=[0.5], bounds=(0.0, 3.0),
                               maxfev=5000)
        q = popt[0]
        q_err = np.sqrt(pcov[0, 0]) if pcov[0, 0] > 0 else np.nan
    except (RuntimeError, ValueError):
        q, q_err = np.nan, np.nan

    return q, q_err


# =============================================================================
# SPECTRAL UNFOLDING
# =============================================================================

def extract_distinct_levels(eigenvalues, tol=1e-8):
    """
    Extract distinct eigenvalue levels from a degenerate spectrum.

    On SU(3) with Peter-Weyl decomposition, eigenvalues are highly degenerate
    (Kramers doubling, representation multiplicity). For meaningful RMT
    analysis, we must work with distinct levels, not raw eigenvalues.

    Session 19a established this: "11,424 raw -> 45 distinct at tau=0,
    791 at tau>0. Must use extract_distinct_levels() for meaningful statistics."

    Args:
        eigenvalues: 1D array of eigenvalues (may be degenerate)
        tol: tolerance for identifying degenerate levels

    Returns:
        distinct: sorted array of distinct eigenvalue levels
        degeneracies: array of degeneracy counts for each level
    """
    E = np.sort(eigenvalues)
    if len(E) == 0:
        return np.array([]), np.array([], dtype=int)

    distinct = [E[0]]
    degens = [1]
    for i in range(1, len(E)):
        if abs(E[i] - distinct[-1]) < tol:
            degens[-1] += 1
        else:
            distinct.append(E[i])
            degens.append(1)

    return np.array(distinct), np.array(degens, dtype=int)


def unfold_spectrum(eigenvalues, poly_order=5):
    """
    Spectral unfolding procedure.

    Given sorted eigenvalues {E_i}, compute the integrated density of states
    (staircase function) N(E) = #{E_i <= E}, fit a smooth polynomial
    N_smooth(E), and define unfolded spacings:
      s_i = N_smooth(E_{i+1}) - N_smooth(E_i)

    IMPORTANT: Input should be DISTINCT eigenvalue levels (degeneracies removed).
    On Jensen-deformed SU(3), the Dirac spectrum has massive degeneracies
    (83%+ of spacings are exactly zero at max_pq_sum=3). Feeding raw
    degenerate eigenvalues produces meaningless Poisson statistics.

    The unfolded spacings should have <s> = 1 if the smooth part is
    correctly estimated.

    Args:
        eigenvalues: 1D array of sorted DISTINCT eigenvalues
        poly_order: degree of polynomial for smooth staircase fit

    Returns:
        spacings: unfolded nearest-neighbor spacings
        mean_spacing: mean of the spacings (should be ~1.0)
    """
    E = np.sort(eigenvalues)
    N = len(E)

    if N < 2 * poly_order:
        # Too few eigenvalues for reliable unfolding
        return np.array([]), 0.0

    # Staircase function: N(E_i) = i + 0.5 (midpoint convention)
    staircase = np.arange(1, N + 1) - 0.5

    # Fit polynomial to staircase
    # Normalize energy range to [0,1] for numerical stability
    E_min, E_max = E[0], E[-1]
    if E_max - E_min < 1e-15:
        return np.array([]), 0.0

    E_norm = (E - E_min) / (E_max - E_min)

    # Adapt poly_order to number of points
    effective_order = min(poly_order, max(2, N // 4))

    try:
        coeffs = np.polyfit(E_norm, staircase, effective_order)
        N_smooth = np.polyval(coeffs, E_norm)
    except (np.linalg.LinAlgError, ValueError):
        return np.array([]), 0.0

    # Unfolded spacings
    spacings = np.diff(N_smooth)

    # Remove negative spacings (can occur at spectrum edges from polynomial fit)
    spacings = spacings[spacings > 0]

    if len(spacings) == 0:
        return np.array([]), 0.0

    # Normalize to unit mean
    mean_s = np.mean(spacings)
    if mean_s > 0:
        spacings = spacings / mean_s

    return spacings, mean_s


# =============================================================================
# NUMBER VARIANCE
# =============================================================================

def number_variance(unfolded_levels, L_values):
    """
    Compute the number variance Sigma^2(L).

    Sigma^2(L) = <(n(E, E+L) - L)^2>_E

    where n(E, E+L) is the number of unfolded levels in [E, E+L].

    For Poisson: Sigma^2(L) = L
    For GOE: Sigma^2(L) ~ (2/pi^2) * [ln(2*pi*L) + gamma_Euler + 1 - pi^2/8]
    For GUE: Sigma^2(L) ~ (1/pi^2) * [ln(2*pi*L) + gamma_Euler + 1 - pi^2/8]

    Args:
        unfolded_levels: sorted unfolded eigenvalue positions
        L_values: array of interval lengths to probe

    Returns:
        sigma2: number variance at each L
    """
    levels = np.sort(unfolded_levels)
    N = len(levels)
    sigma2 = np.zeros(len(L_values))

    for i, L in enumerate(L_values):
        counts = []
        # Slide window of length L across the spectrum
        for j in range(N):
            E_start = levels[j]
            E_end = E_start + L
            n = np.searchsorted(levels, E_end) - j
            counts.append(n)

        counts = np.array(counts, dtype=float)
        # Sigma^2(L) = Var(n) = <n^2> - <n>^2
        sigma2[i] = np.var(counts)

    return sigma2


# =============================================================================
# BUILD D_can (M_Lie) FOR ANY SECTOR
# =============================================================================

def build_M_Lie(rho, E, gammas):
    """
    Build the Lie derivative part of the Dirac operator.

    M_Lie = sum_{a,b} E_{ab} rho[b] (x) gamma_a

    This equals D_can (canonical connection Dirac, since Omega_can = 0).

    Args:
        rho: list of 8 representation matrices
        E: (8,8) orthonormal frame matrix
        gammas: list of 8 Clifford generators (16x16)

    Returns:
        M: (dim_rho*16, dim_rho*16) complex matrix
    """
    dim_rho = rho[0].shape[0]
    dim_spin = gammas[0].shape[0]
    dim_total = dim_rho * dim_spin
    M = np.zeros((dim_total, dim_total), dtype=complex)

    for a in range(8):
        for b in range(8):
            if abs(E[a, b]) > 1e-15:
                M += E[a, b] * np.kron(rho[b], gammas[a])

    return M


def compute_Dcan_eigenvalues(p, q, tau, gens, f_abc, B_ab, gammas):
    """
    Compute D_can = M_Lie eigenvalues for sector (p,q) at given tau.

    Returns sorted real eigenvalues (imaginary parts of anti-Hermitian D_can).
    Convention matches s27_multisector_bcs.npz: eigenvalues are stored as
    real numbers representing the physical spectrum.

    Args:
        p, q: irrep labels
        tau: Jensen deformation parameter
        gens, f_abc, B_ab: SU(3) infrastructure
        gammas: Clifford generators

    Returns:
        evals: sorted real array of eigenvalues (imag parts of anti-Herm D_can)
    """
    g_s = jensen_metric(B_ab, tau)
    E = orthonormal_frame(g_s)

    if p == 0 and q == 0:
        # Trivial rep: M_Lie = 0
        return np.zeros(16)

    _irrep_cache.clear()
    rho, dim_rho = get_irrep(p, q, gens, f_abc)
    M = build_M_Lie(rho, E, gammas)

    # D_can is anti-Hermitian, eigenvalues are purely imaginary
    evals_raw = np.linalg.eigvalsh(1j * M)  # Hermitianize: i*M is Hermitian
    # eigvalsh returns real eigenvalues in ascending order
    # These are the imaginary parts of i*M's eigenvalues
    # The physical eigenvalues of M are i * (eigenvalues of i*M) with negative sign
    # Convention: return the signed real values matching BCS convention
    return np.sort(-evals_raw)


# =============================================================================
# MAIN COMPUTATION
# =============================================================================

def main():
    print("=" * 72)
    print("SESSION 28a COMPUTATION C-4: SPECTRAL CORRELATION R_2(s)")
    print("=" * 72)
    t_start = time.time()

    # -------------------------------------------------------------------------
    # 1. Load D_K eigenvalues from s27 multi-sector BCS data
    # -------------------------------------------------------------------------
    bcs_file = os.path.join(OUTDIR, 's27_multisector_bcs.npz')
    print(f"\nLoading D_K eigenvalues from {bcs_file}")
    bcs_data = np.load(bcs_file, allow_pickle=True)

    sectors_info = bcs_data['sectors']  # (9, 4): p, q, dim, mult
    tau_values = bcs_data['tau_values']  # (9,)
    n_sectors = len(sectors_info)
    n_tau = len(tau_values)

    print(f"  {n_sectors} sectors, {n_tau} tau values")
    for i, (p, q, d, m) in enumerate(sectors_info):
        print(f"  Sector {i}: ({p},{q}), dim={d}, mult={m}, "
              f"matrix size = {d*16}")

    # -------------------------------------------------------------------------
    # 2. Build SU(3) infrastructure for D_can computation
    # -------------------------------------------------------------------------
    print("\nBuilding SU(3) algebraic infrastructure...")
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    B_ab = compute_killing_form(f_abc)
    gammas = build_cliff8()

    # -------------------------------------------------------------------------
    # 3. Select sectors with enough eigenvalues for meaningful statistics
    # -------------------------------------------------------------------------
    # Minimum eigenvalue count for spectral statistics
    MIN_EVALS = 30
    usable_sectors = []
    for i, (p, q, d, m) in enumerate(sectors_info):
        n_evals = d * 16
        if n_evals >= MIN_EVALS:
            usable_sectors.append(i)

    print(f"\nUsable sectors (>= {MIN_EVALS} eigenvalues): "
          f"{[f'({sectors_info[i,0]},{sectors_info[i,1]}):n={sectors_info[i,2]*16}' for i in usable_sectors]}")

    # -------------------------------------------------------------------------
    # 4. Compute Brody parameter q for D_K and D_can across sectors and tau
    # -------------------------------------------------------------------------
    # Storage: q values
    q_K = np.full((n_sectors, n_tau), np.nan)
    q_K_err = np.full((n_sectors, n_tau), np.nan)
    q_can = np.full((n_sectors, n_tau), np.nan)
    q_can_err = np.full((n_sectors, n_tau), np.nan)

    # Store spacing distributions for plotting
    # Key tau indices: tau = 0.0, 0.15, 0.30, 0.50
    plot_tau_indices = [0, 2, 5, 8]  # indices into tau_values
    plot_tau_labels = [f'{tau_values[i]:.2f}' for i in plot_tau_indices]

    # Store spacings for plotting
    spacings_K_plot = {}   # (sector_idx, tau_idx) -> spacings array
    spacings_can_plot = {}

    # Number variance data
    L_values = np.linspace(0.1, 5.0, 50)
    numvar_K = {}
    numvar_can = {}

    print("\n" + "-" * 72)
    print("Computing spectral statistics per sector per tau...")
    print("-" * 72)

    # Degeneracy statistics for reporting
    degen_stats = {}  # (sec_idx, tau_idx) -> (n_raw, n_distinct, max_degen)

    for sec_idx in usable_sectors:
        p, q_rep, dim_rep, mult = sectors_info[sec_idx]
        n_evals = dim_rep * 16
        print(f"\n  Sector ({p},{q_rep}): {n_evals} raw eigenvalues per operator")

        for tau_idx, tau in enumerate(tau_values):
            # --- D_K eigenvalues ---
            key_K = f'evals_{p}_{q_rep}_{tau_idx}'
            evals_K_raw = bcs_data[key_K]

            # Use absolute values for spacing analysis (spectrum is symmetric)
            evals_K_pos = np.sort(np.abs(evals_K_raw))

            # CRITICAL: Extract distinct levels before unfolding
            # Session 19a lesson: degenerate spectra produce meaningless Poisson
            distinct_K, degens_K = extract_distinct_levels(evals_K_pos)
            n_distinct_K = len(distinct_K)
            max_degen_K = np.max(degens_K) if len(degens_K) > 0 else 0
            degen_stats[(sec_idx, tau_idx, 'K')] = (n_evals, n_distinct_K, max_degen_K)

            # Unfold the DISTINCT levels
            sp_K, mean_K = unfold_spectrum(distinct_K, poly_order=min(5, max(2, n_distinct_K // 4)))

            if len(sp_K) >= 8:
                q_val, q_e = fit_brody(sp_K)
                q_K[sec_idx, tau_idx] = q_val
                q_K_err[sec_idx, tau_idx] = q_e

                if tau_idx in plot_tau_indices:
                    spacings_K_plot[(sec_idx, tau_idx)] = sp_K

                    # Number variance from unfolded levels
                    unf_levels = np.cumsum(np.concatenate([[0], sp_K]))
                    if len(unf_levels) > 10:
                        numvar_K[(sec_idx, tau_idx)] = number_variance(unf_levels, L_values)

            # --- D_can eigenvalues ---
            evals_can_raw = compute_Dcan_eigenvalues(
                p, q_rep, tau, gens, f_abc, B_ab, gammas)
            evals_can_pos = np.sort(np.abs(evals_can_raw))

            distinct_can, degens_can = extract_distinct_levels(evals_can_pos)
            n_distinct_can = len(distinct_can)
            max_degen_can = np.max(degens_can) if len(degens_can) > 0 else 0
            degen_stats[(sec_idx, tau_idx, 'can')] = (n_evals, n_distinct_can, max_degen_can)

            sp_can, mean_can = unfold_spectrum(distinct_can, poly_order=min(5, max(2, n_distinct_can // 4)))

            if len(sp_can) >= 8:
                q_val, q_e = fit_brody(sp_can)
                q_can[sec_idx, tau_idx] = q_val
                q_can_err[sec_idx, tau_idx] = q_e

                if tau_idx in plot_tau_indices:
                    spacings_can_plot[(sec_idx, tau_idx)] = sp_can

                    unf_levels = np.cumsum(np.concatenate([[0], sp_can]))
                    if len(unf_levels) > 10:
                        numvar_can[(sec_idx, tau_idx)] = number_variance(unf_levels, L_values)

            # Print per-point with degeneracy info
            qK_str = f"{q_K[sec_idx, tau_idx]:.3f}" if not np.isnan(q_K[sec_idx, tau_idx]) else "N/A"
            qC_str = f"{q_can[sec_idx, tau_idx]:.3f}" if not np.isnan(q_can[sec_idx, tau_idx]) else "N/A"
            print(f"    tau={tau:.2f}: q_K={qK_str} ({n_distinct_K} distinct/{n_evals}), "
                  f"q_can={qC_str} ({n_distinct_can} distinct/{n_evals})")

    # -------------------------------------------------------------------------
    # 5. ANALYSIS AND VERDICT
    # -------------------------------------------------------------------------
    print("\n" + "=" * 72)
    print("ANALYSIS")
    print("=" * 72)

    # Degeneracy summary
    print("\nDegeneracy analysis (CRITICAL for RMT validity):")
    print(f"{'Sector':<10} {'tau':<6} {'raw':<6} {'K_dist':<8} {'K_degen%':<10} "
          f"{'can_dist':<10} {'can_degen%'}")
    print("-" * 66)
    for sec_idx in usable_sectors:
        p, q_rep = sectors_info[sec_idx, 0], sectors_info[sec_idx, 1]
        for tau_idx in [0, 2, 5, 8]:
            if tau_idx >= n_tau:
                continue
            key_K = (sec_idx, tau_idx, 'K')
            key_can = (sec_idx, tau_idx, 'can')
            if key_K in degen_stats and key_can in degen_stats:
                nraw, ndK, mdK = degen_stats[key_K]
                _, ndC, mdC = degen_stats[key_can]
                pctK = 100.0 * (1.0 - ndK / nraw)
                pctC = 100.0 * (1.0 - ndC / nraw)
                print(f"({p},{q_rep}){'':<5} {tau_values[tau_idx]:.2f}  "
                      f"{nraw:<6} {ndK:<8} {pctK:<10.1f} {ndC:<10} {pctC:.1f}")

    # Summary table
    print("\nBrody parameter q summary (q=0: Poisson, q=1: GOE, q=2: GUE):")
    print("NOTE: Analysis uses DISTINCT eigenvalue levels (degeneracies removed)")
    print(f"{'Sector':<12} {'tau':<6} {'q_K':<10} {'q_can':<10} {'Delta_q':<10} {'Note'}")
    print("-" * 60)

    delta_q_all = []
    for sec_idx in usable_sectors:
        p, q_rep, dim_rep, _ = sectors_info[sec_idx]
        for tau_idx, tau in enumerate(tau_values):
            qK = q_K[sec_idx, tau_idx]
            qC = q_can[sec_idx, tau_idx]
            if not (np.isnan(qK) or np.isnan(qC)):
                dq = qC - qK
                delta_q_all.append(dq)
                note = ""
                if abs(qK) < 0.15:
                    note += "K:Poisson "
                elif abs(qK - 1.0) < 0.2:
                    note += "K:GOE "
                if abs(qC) < 0.15:
                    note += "can:Poisson "
                elif abs(qC - 1.0) < 0.2:
                    note += "can:GOE "
                print(f"({p},{q_rep}){'':<7} {tau:.2f}  {qK:<10.4f} {qC:<10.4f} {dq:<+10.4f} {note}")

    delta_q_all = np.array(delta_q_all)

    print(f"\nAggregate statistics:")
    if len(delta_q_all) > 0:
        print(f"  Mean q_K  = {np.nanmean(q_K[q_K != 0]):.4f} +/- {np.nanstd(q_K[~np.isnan(q_K)]):.4f}")
        q_can_valid = q_can[~np.isnan(q_can)]
        print(f"  Mean q_can = {np.nanmean(q_can_valid):.4f} +/- {np.nanstd(q_can_valid):.4f}")
        print(f"  Mean Delta_q (can - K) = {np.mean(delta_q_all):.4f} +/- {np.std(delta_q_all):.4f}")
        print(f"  Max |Delta_q| = {np.max(np.abs(delta_q_all)):.4f}")

    # Check for Wigner-Dyson in one but Poisson in other
    crossovers = 0
    for sec_idx in usable_sectors:
        for tau_idx in range(n_tau):
            qK = q_K[sec_idx, tau_idx]
            qC = q_can[sec_idx, tau_idx]
            if np.isnan(qK) or np.isnan(qC):
                continue
            # Definition: Poisson = q < 0.2, GOE = q > 0.7
            K_poisson = qK < 0.2
            K_goe = qK > 0.7
            C_poisson = qC < 0.2
            C_goe = qC > 0.7
            if (K_poisson and C_goe) or (K_goe and C_poisson):
                crossovers += 1
                p, q_rep = sectors_info[sec_idx, 0], sectors_info[sec_idx, 1]
                print(f"  CROSSOVER: ({p},{q_rep}) at tau={tau_values[tau_idx]:.2f}: "
                      f"q_K={qK:.3f}, q_can={qC:.3f}")

    # Tau evolution: does q change monotonically with tau?
    print("\nTau evolution of Brody q:")
    for sec_idx in usable_sectors:
        p, q_rep = sectors_info[sec_idx, 0], sectors_info[sec_idx, 1]
        qK_vs_tau = q_K[sec_idx, :]
        qC_vs_tau = q_can[sec_idx, :]
        valid_K = ~np.isnan(qK_vs_tau)
        valid_C = ~np.isnan(qC_vs_tau)
        n_valid_K = np.sum(valid_K)
        n_valid_C = np.sum(valid_C)

        parts = [f"  ({p},{q_rep}):"]

        if n_valid_K >= 3:
            diffs_K = np.diff(qK_vs_tau[valid_K])
            mono_K = "increasing" if np.all(diffs_K > 0) else (
                "decreasing" if np.all(diffs_K < 0) else "non-monotonic")
            parts.append(f"q_K is {mono_K} "
                         f"[{qK_vs_tau[valid_K][0]:.3f} -> {qK_vs_tau[valid_K][-1]:.3f}]")
        elif n_valid_K > 0:
            parts.append(f"q_K: {n_valid_K} valid points (too few)")
        else:
            parts.append("q_K: no valid data")

        if n_valid_C >= 3:
            diffs_C = np.diff(qC_vs_tau[valid_C])
            mono_C = "increasing" if np.all(diffs_C > 0) else (
                "decreasing" if np.all(diffs_C < 0) else "non-monotonic")
            parts.append(f"q_can is {mono_C} "
                         f"[{qC_vs_tau[valid_C][0]:.3f} -> {qC_vs_tau[valid_C][-1]:.3f}]")
        elif n_valid_C > 0:
            parts.append(f"q_can: {n_valid_C} valid points (too few)")
        else:
            parts.append("q_can: no valid data")

        print(", ".join(parts))

    # -------------------------------------------------------------------------
    # 6. GATE VERDICT
    # -------------------------------------------------------------------------
    print("\n" + "=" * 72)
    print("GATE C-4 VERDICT: DIAGNOSTIC")
    print("=" * 72)

    if crossovers > 0:
        verdict = "SIGNAL"
        print(f"  {crossovers} spectral phase crossover(s) detected.")
        print("  Torsion/spin-connection DOES induce a qualitative change in level statistics.")
    else:
        verdict = "NULL"
        mean_qK = np.nanmean(q_K[~np.isnan(q_K)])
        mean_qC = np.nanmean(q_can[~np.isnan(q_can)])
        print(f"  No Poisson-to-GOE crossovers between D_K and D_can.")
        print(f"  Both operators show similar level statistics.")
        print(f"  Mean q_K = {mean_qK:.3f}, Mean q_can = {mean_qC:.3f}")
        if mean_qK < 0.3 and mean_qC < 0.3:
            print("  BOTH operators are near-Poisson (integrable/block-diagonal artifact).")
            print("  CONSISTENT with Session 19a: block-diagonal structure forces Poisson.")
        elif mean_qK > 0.6 and mean_qC > 0.6:
            print("  BOTH operators show GOE-like level repulsion.")
            print("  Within-sector quantum chaos present for both connections.")

    print(f"\n  VERDICT: C-4 = DIAGNOSTIC ({verdict})")
    print("  This is a diagnostic gate -- no closure/pass implications.")

    # -------------------------------------------------------------------------
    # 7. SAVE DATA
    # -------------------------------------------------------------------------
    outfile = os.path.join(OUTDIR, 's28a_spectral_correlations.npz')
    save_dict = {
        'q_K': q_K,
        'q_K_err': q_K_err,
        'q_can': q_can,
        'q_can_err': q_can_err,
        'tau_values': tau_values,
        'sectors': sectors_info,
        'L_values': L_values,
        'verdict': np.array(verdict),
        'usable_sectors': np.array(usable_sectors),
    }

    # Save spacing distributions for plot tau values
    for key, sp in spacings_K_plot.items():
        save_dict[f'sp_K_{key[0]}_{key[1]}'] = sp
    for key, sp in spacings_can_plot.items():
        save_dict[f'sp_can_{key[0]}_{key[1]}'] = sp
    # Save number variance
    for key, nv in numvar_K.items():
        save_dict[f'nv_K_{key[0]}_{key[1]}'] = nv
    for key, nv in numvar_can.items():
        save_dict[f'nv_can_{key[0]}_{key[1]}'] = nv

    np.savez_compressed(outfile, **save_dict)
    print(f"\nData saved to {outfile}")

    # -------------------------------------------------------------------------
    # 8. PLOT
    # -------------------------------------------------------------------------
    print("\nGenerating plots...")
    fig = plt.figure(figsize=(20, 16))

    # Define reference distributions
    s_ref = np.linspace(0.001, 4.0, 200)
    poisson_pdf = np.exp(-s_ref)
    goe_pdf = (np.pi / 2.0) * s_ref * np.exp(-np.pi * s_ref**2 / 4.0)

    # --- Row 1: P(s) histograms for D_K at 4 tau values ---
    # Pick the largest usable sector for best statistics
    best_sector = max(usable_sectors, key=lambda i: sectors_info[i, 2])
    p_best, q_best = sectors_info[best_sector, 0], sectors_info[best_sector, 1]

    for col, tau_idx in enumerate(plot_tau_indices):
        ax = fig.add_subplot(4, 4, col + 1)
        key = (best_sector, tau_idx)
        if key in spacings_K_plot and len(spacings_K_plot[key]) > 5:
            sp = spacings_K_plot[key]
            ax.hist(sp, bins=min(20, max(8, len(sp) // 5)), density=True,
                    alpha=0.6, color='steelblue', label=f'D_K (n={len(sp)})')
            q_val = q_K[best_sector, tau_idx]
            if not np.isnan(q_val):
                ax.plot(s_ref, brody_pdf(s_ref, q_val), 'b-', lw=1.5,
                        label=f'Brody q={q_val:.2f}')
        ax.plot(s_ref, poisson_pdf, 'k--', lw=1, alpha=0.5, label='Poisson')
        ax.plot(s_ref, goe_pdf, 'r--', lw=1, alpha=0.5, label='GOE')
        ax.set_title(f'D_K ({p_best},{q_best}) tau={tau_values[tau_idx]:.2f}',
                     fontsize=10)
        ax.set_xlabel('s')
        ax.set_ylabel('P(s)')
        ax.set_xlim(0, 4)
        ax.legend(fontsize=7, loc='upper right')

    # --- Row 2: P(s) histograms for D_can at 4 tau values ---
    for col, tau_idx in enumerate(plot_tau_indices):
        ax = fig.add_subplot(4, 4, col + 5)
        key = (best_sector, tau_idx)
        if key in spacings_can_plot and len(spacings_can_plot[key]) > 5:
            sp = spacings_can_plot[key]
            ax.hist(sp, bins=min(20, max(8, len(sp) // 5)), density=True,
                    alpha=0.6, color='darkorange', label=f'D_can (n={len(sp)})')
            q_val = q_can[best_sector, tau_idx]
            if not np.isnan(q_val):
                ax.plot(s_ref, brody_pdf(s_ref, q_val), color='darkorange',
                        ls='-', lw=1.5, label=f'Brody q={q_val:.2f}')
        ax.plot(s_ref, poisson_pdf, 'k--', lw=1, alpha=0.5, label='Poisson')
        ax.plot(s_ref, goe_pdf, 'r--', lw=1, alpha=0.5, label='GOE')
        ax.set_title(f'D_can ({p_best},{q_best}) tau={tau_values[tau_idx]:.2f}',
                     fontsize=10)
        ax.set_xlabel('s')
        ax.set_ylabel('P(s)')
        ax.set_xlim(0, 4)
        ax.legend(fontsize=7, loc='upper right')

    # --- Row 3: Brody q vs tau for all usable sectors ---
    ax_qK = fig.add_subplot(4, 2, 5)
    ax_qC = fig.add_subplot(4, 2, 6)
    colors = plt.cm.tab10(np.linspace(0, 1, len(usable_sectors)))

    for ci, sec_idx in enumerate(usable_sectors):
        p, q_rep = sectors_info[sec_idx, 0], sectors_info[sec_idx, 1]
        label = f'({p},{q_rep})'

        valid_K = ~np.isnan(q_K[sec_idx])
        if np.any(valid_K):
            ax_qK.plot(tau_values[valid_K], q_K[sec_idx, valid_K],
                       'o-', color=colors[ci], label=label, markersize=4)
            ax_qK.fill_between(tau_values[valid_K],
                               q_K[sec_idx, valid_K] - q_K_err[sec_idx, valid_K],
                               q_K[sec_idx, valid_K] + q_K_err[sec_idx, valid_K],
                               alpha=0.1, color=colors[ci])

        valid_C = ~np.isnan(q_can[sec_idx])
        if np.any(valid_C):
            ax_qC.plot(tau_values[valid_C], q_can[sec_idx, valid_C],
                       's-', color=colors[ci], label=label, markersize=4)
            ax_qC.fill_between(tau_values[valid_C],
                               q_can[sec_idx, valid_C] - q_can_err[sec_idx, valid_C],
                               q_can[sec_idx, valid_C] + q_can_err[sec_idx, valid_C],
                               alpha=0.1, color=colors[ci])

    for ax, title in [(ax_qK, 'D_K: Brody q vs tau'),
                       (ax_qC, 'D_can: Brody q vs tau')]:
        ax.axhline(0, color='k', ls='--', lw=0.8, alpha=0.5, label='Poisson')
        ax.axhline(1, color='r', ls='--', lw=0.8, alpha=0.5, label='GOE')
        ax.set_xlabel('tau')
        ax.set_ylabel('Brody q')
        ax.set_title(title)
        ax.legend(fontsize=7, ncol=2)
        ax.set_ylim(-0.2, 2.5)

    # --- Row 4: Number variance at best sector + Delta q comparison ---
    ax_nv = fig.add_subplot(4, 2, 7)
    # Plot number variance for D_K and D_can at tau=0 for best sector
    tau_idx_0 = plot_tau_indices[0]
    key0 = (best_sector, tau_idx_0)
    if key0 in numvar_K:
        ax_nv.plot(L_values, numvar_K[key0], 'b-', lw=1.5,
                   label=f'D_K tau=0')
    if key0 in numvar_can:
        ax_nv.plot(L_values, numvar_can[key0], color='darkorange', ls='-',
                   lw=1.5, label=f'D_can tau=0')
    # Also at tau=0.30
    tau_idx_30 = plot_tau_indices[2]
    key30 = (best_sector, tau_idx_30)
    if key30 in numvar_K:
        ax_nv.plot(L_values, numvar_K[key30], 'b--', lw=1.2,
                   label=f'D_K tau={tau_values[tau_idx_30]:.2f}')
    if key30 in numvar_can:
        ax_nv.plot(L_values, numvar_can[key30], color='darkorange', ls='--',
                   lw=1.2, label=f'D_can tau={tau_values[tau_idx_30]:.2f}')
    # Reference lines
    ax_nv.plot(L_values, L_values, 'k--', lw=0.8, alpha=0.5, label='Poisson')
    goe_nv = (2.0 / np.pi**2) * (np.log(2 * np.pi * L_values + 1e-10)
                                   + 0.5772 + 1 - np.pi**2 / 8)
    goe_nv = np.maximum(goe_nv, 0)
    ax_nv.plot(L_values, goe_nv, 'r--', lw=0.8, alpha=0.5, label='GOE')
    ax_nv.set_xlabel('L')
    ax_nv.set_ylabel('Sigma^2(L)')
    ax_nv.set_title(f'Number Variance ({p_best},{q_best})')
    ax_nv.legend(fontsize=7)
    ax_nv.set_ylim(0, max(6, np.max(L_values)))

    # Delta q scatter plot
    ax_dq = fig.add_subplot(4, 2, 8)
    for ci, sec_idx in enumerate(usable_sectors):
        p, q_rep = sectors_info[sec_idx, 0], sectors_info[sec_idx, 1]
        for tau_idx in range(n_tau):
            qK = q_K[sec_idx, tau_idx]
            qC = q_can[sec_idx, tau_idx]
            if not (np.isnan(qK) or np.isnan(qC)):
                ax_dq.scatter(qK, qC, color=colors[ci], s=20, alpha=0.7,
                              zorder=3)
    # Add identity line and reference points
    ax_dq.plot([0, 3], [0, 3], 'k--', lw=0.8, alpha=0.5)
    ax_dq.axhline(0, color='gray', ls=':', lw=0.5)
    ax_dq.axhline(1, color='r', ls=':', lw=0.5)
    ax_dq.axvline(0, color='gray', ls=':', lw=0.5)
    ax_dq.axvline(1, color='r', ls=':', lw=0.5)
    ax_dq.set_xlabel('q_K (D_K)')
    ax_dq.set_ylabel('q_can (D_can)')
    ax_dq.set_title('D_K vs D_can Brody parameter')
    # Add sector legend
    for ci, sec_idx in enumerate(usable_sectors):
        p, q_rep = sectors_info[sec_idx, 0], sectors_info[sec_idx, 1]
        ax_dq.scatter([], [], color=colors[ci], s=20, label=f'({p},{q_rep})')
    ax_dq.legend(fontsize=7, ncol=2)
    ax_dq.set_xlim(-0.2, 2.5)
    ax_dq.set_ylim(-0.2, 2.5)

    plt.suptitle('C-4: Spectral Correlations — D_K vs D_can Level Statistics',
                 fontsize=14, fontweight='bold')
    plt.tight_layout(rect=[0, 0, 1, 0.96])

    plotfile = os.path.join(OUTDIR, 's28a_spectral_correlations.png')
    plt.savefig(plotfile, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Plot saved to {plotfile}")

    total_time = time.time() - t_start
    print(f"\nTotal computation time: {total_time:.1f}s")
    print("DONE.")


if __name__ == '__main__':
    main()
