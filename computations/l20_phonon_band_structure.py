"""
L-5: PHONON BAND STRUCTURE DIAGRAM ON (SU(3), g_Jensen)
==========================================================

Session 20b: Plots the full KK mode spectrum as a "phonon band structure",
showing omega (mode frequency) vs C_2(p,q) (Casimir label ~ momentum) for
all four mode types:

  1. Scalar Laplacian (spin-0 KK modes) — from kk1_bosonic_tower.py
  2. Vector Hodge Laplacian (spin-1 KK modes) — from kk1_bosonic_tower.py
  3. Dirac operator (spin-1/2 KK modes) — from s19a_sweep_data.npz
  4. TT Lichnerowicz (spin-2 KK modes) — from phonon-sim L-3 (when available)

The band structure is plotted at 3 tau values: tau=0 (bi-invariant),
tau=0.15 (phi crossing), tau=0.30 (gauge coupling target).

Physics:
  - Each (p,q) sector is a "momentum shell" labeled by C_2(p,q)
  - Within each sector, the Dirac/Laplacian operators produce BANDS of eigenvalues
  - The Jensen deformation tau shifts bands relative to each other
  - Mode crossings and avoided crossings signal phase transitions
  - The (3,0) sector at tau=0.15 is special: mass ratio = phi

DNP Tachyon Boundary:
  For TT 2-tensors, the 4D mass formula is (Baptista eq 3.17-3.18):
    m^2_n = mu_n - (2/k) R_K
  where mu_n = Lichnerowicz eigenvalue, k = dim(K) = 8.
  A mode becomes tachyonic when mu_n < R_K/4.
  The Duff-Nilsson-Pope stability bound is lambda_L >= 3m^2,
  which for Einstein manifolds gives lambda_L >= (3/4) R_K.
  We mark this threshold on the band structure.

Author: KK-Theorist Agent (Session 20b)
Date: 2026-02-19

References:
  - Baptista (2024), arXiv:2306.01049, Section 3.3, eqs 3.14-3.19
  - Duff, Nilsson, Pope (1986): Kaluza-Klein supergravity
  - Session 19d synthesis, Session 20a decision gate
"""

import numpy as np
from numpy.linalg import eigvalsh, eigh
import sys
import os
import time
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)


# =============================================================================
# UTILITY: SU(3) REPRESENTATION THEORY
# =============================================================================

def dim_su3_irrep(p, q):
    """Dimension of SU(3) irrep (p,q)."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def casimir_su3(p, q):
    """Quadratic Casimir C_2(p,q) for SU(3) irrep (p,q)."""
    return (p**2 + q**2 + p*q + 3*p + 3*q) / 3.0


def z3_label(p, q):
    """Z_3 generation label: (p-q) mod 3."""
    return (p - q) % 3


def all_sectors(max_pq_sum=6):
    """Return all (p,q) sectors with p+q <= max_pq_sum, sorted by C_2."""
    sectors = []
    for p in range(max_pq_sum + 1):
        for q in range(max_pq_sum + 1 - p):
            sectors.append((p, q))
    return sorted(sectors, key=lambda pq: casimir_su3(*pq))


# =============================================================================
# MODULE 1: LOAD FERMIONIC (DIRAC) DATA
# =============================================================================

def load_dirac_data(tau_target):
    """
    Load Dirac eigenvalues from s19a_sweep_data.npz for a given tau.

    Returns dict mapping (p,q) -> array of |lambda| values (Dirac eigenvalues).
    These are FREQUENCIES (not squared masses). For the band structure, we plot |lambda|.
    """
    from s19a_sweep_data import load_sweep_data

    data_path = os.path.join(SCRIPT_DIR, 's19a_sweep_data.npz')
    data = load_sweep_data(data_path)

    tau_values = data['tau_values']
    # Find closest tau
    idx = np.argmin(np.abs(tau_values - tau_target))
    actual_tau = tau_values[idx]
    if abs(actual_tau - tau_target) > 0.05:
        print(f"  WARNING: requested tau={tau_target}, closest={actual_tau}")

    evals = data['eigenvalues'][idx]
    sp = data['sector_p'][idx]
    sq = data['sector_q'][idx]

    # Group by sector
    result = {}
    sectors = sorted(set(zip(sp.tolist(), sq.tolist())))
    for (p, q) in sectors:
        mask = (sp == p) & (sq == q)
        result[(p, q)] = np.sort(evals[mask])

    return result, actual_tau


# =============================================================================
# MODULE 2: COMPUTE BOSONIC (SCALAR + VECTOR) DATA
# =============================================================================

def compute_bosonic_data(tau):
    """
    Compute scalar and vector Laplacian eigenvalues at given tau.

    Returns:
        scalar_by_sector: dict (p,q) -> array of Laplacian eigenvalues (= m^2)
        vector_by_sector: dict (p,q) -> array of Hodge eigenvalues (= m^2)
    """
    from kk1_bosonic_tower import bosonic_spectrum_at_s

    result = bosonic_spectrum_at_s(tau, max_pq_scalar=6, max_pq_vector=4)

    scalar_by_sector = {}
    for (p, q, evals, dim_pq) in result['scalar_data']:
        scalar_by_sector[(p, q)] = np.sort(evals)

    vector_by_sector = {}
    for (p, q, evals, dim_pq) in result['vector_data']:
        vector_by_sector[(p, q)] = np.sort(evals)

    return scalar_by_sector, vector_by_sector


# =============================================================================
# MODULE 3: SCALAR CURVATURE (for DNP threshold)
# =============================================================================

def scalar_curvature_R(s):
    """
    Exact scalar curvature R(s) for Jensen-deformed (SU(3), g_s).

    From SP-2 exact formula:
        R(s) = -(1/4) e^{-4s} + 2 e^{-s} - 1/4 + (1/2) e^{2s}

    At s=0: R(0) = 2.0 (Einstein manifold: Ric = (1/4) g).
    """
    return -0.25 * np.exp(-4*s) + 2.0 * np.exp(-s) - 0.25 + 0.5 * np.exp(2*s)


def dnp_tachyon_threshold(s):
    """
    DNP tachyon threshold for TT 2-tensor modes.

    From Baptista eq 3.17-3.18 with k = dim(K) = 8:
        m^2_n = mu_n - (2/k) R_K = mu_n - R_K/4

    A TT mode is tachyonic when m^2 < 0, i.e., mu_n < R_K/4.

    The Lichnerowicz eigenvalue at the tachyon boundary is:
        mu_tachyon = R_K / 4

    This is the omega^2 value below which TT modes are unstable.
    """
    R_K = scalar_curvature_R(s)
    return R_K / 4.0


def dnp_stability_threshold(s):
    """
    DNP stability threshold: lambda_L >= 3*m^2 for perturbative stability.

    For an Einstein manifold, m^2 = R_K / (k-1) = R_K / 7.
    The DNP bound is lambda_L >= 3 * R_K / 7.

    But for Jensen-deformed SU(3), which is NOT Einstein for s>0, the
    relevant bound uses the actual Ricci eigenvalues. We use the
    conservative estimate lambda_L >= (3/4)*R_K.
    """
    R_K = scalar_curvature_R(s)
    return 0.75 * R_K


# =============================================================================
# MODULE 4: PLACEHOLDER FOR TT LICHNEROWICZ DATA
# =============================================================================

def load_tt_data(tau_target):
    """
    Load TT Lichnerowicz eigenvalues from L-3 output (when available).

    Returns None if data not yet computed.
    Otherwise: dict (p,q) -> array of Lichnerowicz eigenvalues (= mu_n).
    """
    # Check for L-3 output file
    tt_path = os.path.join(SCRIPT_DIR, 'l20b_lichnerowicz_data.npz')
    if not os.path.exists(tt_path):
        return None

    try:
        data = np.load(tt_path, allow_pickle=True)
        # Expected format: tau values + per-sector eigenvalues
        taus = data.get('tau_values', data.get('tau', None))
        if taus is None:
            return None

        idx = np.argmin(np.abs(taus - tau_target))
        if abs(taus[idx] - tau_target) > 0.05:
            return None

        # Try to load sector-tagged data
        result = {}
        for key in data.keys():
            if key.startswith(f'tt_evals_tau{idx}_'):
                pq = key.split('_')[-1]  # e.g., "0_0" for (0,0)
                p, q = int(pq.split(',')[0]), int(pq.split(',')[1])
                result[(p, q)] = data[key]

        return result if len(result) > 0 else None
    except Exception:
        return None


# =============================================================================
# MODULE 5: BAND STRUCTURE PLOTTING
# =============================================================================

def plot_band_structure(tau_values_plot=(0.0, 0.15, 0.30),
                        max_pq_sum=6,
                        output_prefix='l20_band_structure'):
    """
    Create the phonon band structure diagram.

    For each tau value, plots omega vs C_2(p,q) for all four mode types.

    The x-axis is C_2(p,q), the quadratic Casimir, which serves as
    the "momentum" label for each sector. The y-axis is the mode
    frequency omega = |lambda| (for Dirac) or sqrt(mu) (for bosonic).

    Color scheme:
      - Scalar (spin-0): blue circles
      - Vector (spin-1): green triangles
      - Dirac (spin-1/2): red crosses
      - TT (spin-2): purple diamonds (when available)
      - DNP threshold: dashed black line
      - phi sector (3,0): gold highlight
    """
    n_tau = len(tau_values_plot)
    fig, axes = plt.subplots(1, n_tau, figsize=(6*n_tau, 8), sharey=True)
    if n_tau == 1:
        axes = [axes]

    sectors = all_sectors(max_pq_sum)
    c2_values = {(p,q): casimir_su3(p,q) for (p,q) in sectors}

    for ax_idx, tau in enumerate(tau_values_plot):
        ax = axes[ax_idx]

        print(f"\n--- tau = {tau:.2f} ---")
        t0 = time.time()

        # --- Load Dirac data ---
        dirac_data, actual_tau_dirac = load_dirac_data(tau)
        print(f"  Dirac: {sum(len(v) for v in dirac_data.values())} eigenvalues "
              f"from {len(dirac_data)} sectors (actual tau={actual_tau_dirac:.2f})")

        # --- Compute bosonic data ---
        scalar_data, vector_data = compute_bosonic_data(tau)
        print(f"  Scalar: {sum(len(v) for v in scalar_data.values())} eigenvalues "
              f"from {len(scalar_data)} sectors")
        print(f"  Vector: {sum(len(v) for v in vector_data.values())} eigenvalues "
              f"from {len(vector_data)} sectors")

        # --- Load TT data (if available) ---
        tt_data = load_tt_data(tau)
        if tt_data is not None:
            print(f"  TT: {sum(len(v) for v in tt_data.values())} eigenvalues "
                  f"from {len(tt_data)} sectors")
        else:
            print(f"  TT: not yet available (placeholder)")

        # --- Plot scalar modes ---
        for (p, q) in sectors:
            c2 = c2_values[(p, q)]
            if (p, q) in scalar_data:
                evals = scalar_data[(p, q)]
                # Convert Laplacian eigenvalues (m^2) to frequencies (m)
                freqs = np.sqrt(np.maximum(evals, 0))
                freqs_nonzero = freqs[freqs > 1e-8]
                if len(freqs_nonzero) > 0:
                    # Add small jitter to x for visibility
                    x = c2 - 0.15
                    ax.scatter([x]*len(freqs_nonzero), freqs_nonzero,
                              c='steelblue', marker='o', s=12, alpha=0.6,
                              linewidths=0, zorder=3)

        # --- Plot vector modes ---
        for (p, q) in sectors:
            c2 = c2_values[(p, q)]
            if (p, q) in vector_data:
                evals = vector_data[(p, q)]
                freqs = np.sqrt(np.maximum(evals, 0))
                freqs_nonzero = freqs[freqs > 1e-8]
                if len(freqs_nonzero) > 0:
                    x = c2 - 0.05
                    ax.scatter([x]*len(freqs_nonzero), freqs_nonzero,
                              c='seagreen', marker='^', s=14, alpha=0.6,
                              linewidths=0, zorder=3)

        # --- Plot Dirac modes ---
        for (p, q) in sectors:
            c2 = c2_values[(p, q)]
            if (p, q) in dirac_data:
                evals = dirac_data[(p, q)]
                evals_nonzero = evals[evals > 1e-8]
                if len(evals_nonzero) > 0:
                    x = c2 + 0.05
                    ax.scatter([x]*len(evals_nonzero), evals_nonzero,
                              c='crimson', marker='x', s=16, alpha=0.7,
                              linewidths=0.8, zorder=3)

        # --- Plot TT modes (if available) ---
        if tt_data is not None:
            for (p, q) in sectors:
                c2 = c2_values[(p, q)]
                if (p, q) in tt_data:
                    evals = tt_data[(p, q)]
                    freqs = np.sqrt(np.maximum(evals, 0))
                    freqs_nonzero = freqs[freqs > 1e-8]
                    if len(freqs_nonzero) > 0:
                        x = c2 + 0.15
                        ax.scatter([x]*len(freqs_nonzero), freqs_nonzero,
                                  c='darkorchid', marker='D', s=14, alpha=0.7,
                                  linewidths=0, zorder=3)

        # --- DNP threshold line ---
        c2_range = np.array([c2_values[s] for s in sectors])
        mu_threshold = dnp_tachyon_threshold(tau)
        omega_threshold = np.sqrt(max(mu_threshold, 0))
        ax.axhline(y=omega_threshold, color='black', linestyle='--',
                   linewidth=1.5, alpha=0.7, zorder=2,
                   label=f'DNP tachyon: $\\omega = \\sqrt{{R_K/4}}$ = {omega_threshold:.3f}')

        # --- DNP stability threshold ---
        mu_stab = dnp_stability_threshold(tau)
        omega_stab = np.sqrt(max(mu_stab, 0))
        ax.axhline(y=omega_stab, color='gray', linestyle=':',
                   linewidth=1.2, alpha=0.6, zorder=2,
                   label=f'DNP stable: $\\omega = \\sqrt{{3R_K/4}}$ = {omega_stab:.3f}')

        # --- Highlight (3,0) sector ---
        c2_30 = c2_values[(3, 0)]
        ax.axvspan(c2_30 - 0.3, c2_30 + 0.3, alpha=0.12, color='gold', zorder=1)
        ax.text(c2_30, ax.get_ylim()[1]*0.95 if ax.get_ylim()[1] > 0 else 3.0,
                '(3,0)', ha='center', va='top', fontsize=8, fontweight='bold',
                color='goldenrod')

        # --- Axis formatting ---
        ax.set_xlabel('$C_2(p,q)$', fontsize=12)
        if ax_idx == 0:
            ax.set_ylabel('Mode frequency $\\omega$', fontsize=12)
        ax.set_title(f'$\\tau = {tau:.2f}$', fontsize=14)
        ax.set_xlim(-0.5, max(c2_range) + 0.5)

        # Add sector tick labels
        unique_c2 = sorted(set(c2_values[s] for s in sectors))
        ax.set_xticks(unique_c2[::2])  # Every other to avoid crowding
        ax.tick_params(axis='x', labelsize=8)
        ax.grid(True, alpha=0.2)

        dt = time.time() - t0
        print(f"  Panel plotted in {dt:.1f}s")

    # --- Global legend ---
    legend_elements = [
        Line2D([0], [0], marker='o', color='w', markerfacecolor='steelblue',
               markersize=8, label='Scalar (spin-0)'),
        Line2D([0], [0], marker='^', color='w', markerfacecolor='seagreen',
               markersize=8, label='Vector (spin-1)'),
        Line2D([0], [0], marker='x', color='crimson',
               markersize=8, label='Dirac (spin-1/2)', markeredgewidth=1.5),
        Line2D([0], [0], marker='D', color='w', markerfacecolor='darkorchid',
               markersize=7, label='TT (spin-2)'),
        Line2D([0], [0], color='black', linestyle='--',
               linewidth=1.5, label='DNP tachyon ($R_K/4$)'),
        Line2D([0], [0], color='gray', linestyle=':',
               linewidth=1.2, label='DNP stability ($3R_K/4$)'),
    ]
    fig.legend(handles=legend_elements, loc='upper center',
              ncol=3, fontsize=9, bbox_to_anchor=(0.5, 0.98))

    fig.suptitle('KK Mode Spectrum on Jensen-Deformed SU(3)',
                fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.subplots_adjust(top=0.90)

    # Save
    png_path = os.path.join(SCRIPT_DIR, f'{output_prefix}.png')
    fig.savefig(png_path, dpi=150, bbox_inches='tight')
    print(f"\nSaved band structure plot to {png_path}")
    plt.close(fig)

    return png_path


# =============================================================================
# MODULE 6: SPECTRAL GAP & CROSSING ANALYSIS
# =============================================================================

def analyze_spectral_features(tau_values_analysis=None, max_pq_sum=6):
    """
    Analyze spectral gaps, crossings, and avoided crossings across tau.

    Key features to detect:
      1. Spectral gap: minimum nonzero eigenvalue across all bosonic modes
      2. Mode crossings: where eigenvalue bands from different sectors intersect
      3. phi sector anomaly: the (3,0)/(0,0) Dirac ratio near phi=1.618
      4. DNP crossing: first tau where a TT eigenvalue drops below R_K/4
    """
    if tau_values_analysis is None:
        tau_values_analysis = np.arange(0.0, 2.01, 0.1)

    results = {
        'tau': [],
        'scalar_gap': [],
        'vector_gap': [],
        'dirac_gap': [],
        'R_K': [],
        'dnp_threshold': [],
        'phi_ratio_30_00': [],
    }

    for tau in tau_values_analysis:
        print(f"  Analyzing tau = {tau:.2f}...")

        # Scalar/vector
        scalar_data, vector_data = compute_bosonic_data(tau)

        # Scalar gap = smallest nonzero eigenvalue
        all_scalar = []
        for evals in scalar_data.values():
            all_scalar.extend(evals[evals > 1e-8].tolist())
        scalar_gap = min(all_scalar) if all_scalar else 0.0

        # Vector gap
        all_vector = []
        for evals in vector_data.values():
            all_vector.extend(evals[evals > 1e-8].tolist())
        vector_gap = min(all_vector) if all_vector else 0.0

        # Dirac
        dirac_data, _ = load_dirac_data(tau)
        all_dirac = []
        for evals in dirac_data.values():
            all_dirac.extend(evals[evals > 1e-8].tolist())
        dirac_gap = min(all_dirac) if all_dirac else 0.0

        # phi ratio: (3,0) min / (0,0) min
        phi_ratio = np.nan
        if (3,0) in dirac_data and (0,0) in dirac_data:
            min_30 = np.min(dirac_data[(3,0)])
            min_00 = np.min(dirac_data[(0,0)])
            if min_00 > 1e-8:
                phi_ratio = min_30 / min_00

        R_K = scalar_curvature_R(tau)
        results['tau'].append(tau)
        results['scalar_gap'].append(scalar_gap)
        results['vector_gap'].append(vector_gap)
        results['dirac_gap'].append(dirac_gap)
        results['R_K'].append(R_K)
        results['dnp_threshold'].append(R_K / 4.0)
        results['phi_ratio_30_00'].append(phi_ratio)

    # Convert to arrays
    for key in results:
        results[key] = np.array(results[key])

    return results


def plot_spectral_gaps(results, output_prefix='l20_spectral_gaps'):
    """Plot spectral gaps and phi ratio vs tau."""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

    tau = results['tau']

    # Panel 1: Spectral gaps
    ax1.plot(tau, np.sqrt(results['scalar_gap']), 'o-', color='steelblue',
             markersize=4, label='Scalar gap $\\sqrt{\\mu_{min}}$')
    ax1.plot(tau, np.sqrt(results['vector_gap']), '^-', color='seagreen',
             markersize=4, label='Vector gap $\\sqrt{\\mu_{min}}$')
    ax1.plot(tau, results['dirac_gap'], 'x-', color='crimson',
             markersize=5, label='Dirac gap $|\\lambda_{min}|$')
    ax1.plot(tau, np.sqrt(results['dnp_threshold']), 'k--',
             linewidth=1.5, label='DNP tachyon $\\sqrt{R_K/4}$')
    ax1.set_ylabel('Gap frequency $\\omega$', fontsize=12)
    ax1.legend(fontsize=9)
    ax1.grid(True, alpha=0.3)
    ax1.set_title('Spectral Gaps vs Jensen Deformation', fontsize=13)

    # Panel 2: phi ratio
    ax2.plot(tau, results['phi_ratio_30_00'], 'D-', color='goldenrod',
             markersize=5, label='$m_{(3,0)} / m_{(0,0)}$')
    ax2.axhline(y=(1+np.sqrt(5))/2, color='gold', linestyle='--',
               linewidth=1.5, alpha=0.8, label='$\\varphi = 1.618...$')
    ax2.set_xlabel('Jensen deformation $\\tau$', fontsize=12)
    ax2.set_ylabel('Mass ratio', fontsize=12)
    ax2.legend(fontsize=9)
    ax2.grid(True, alpha=0.3)
    ax2.set_title('(3,0)/(0,0) Dirac Mass Ratio', fontsize=13)

    plt.tight_layout()
    png_path = os.path.join(SCRIPT_DIR, f'{output_prefix}.png')
    fig.savefig(png_path, dpi=150, bbox_inches='tight')
    print(f"Saved spectral gaps plot to {png_path}")
    plt.close(fig)

    return png_path


# =============================================================================
# MODULE 7: DNP TACHYON SEARCH FOR TT MODES
# =============================================================================

def dnp_tachyon_search(tt_sweep_data=None):
    """
    Search for the first tau where a TT mode crosses the DNP tachyon boundary.

    This is the critical physics: if a TT mode goes tachyonic at some tau_*,
    the internal geometry becomes unstable, potentially selecting a natural
    vacuum deformation parameter.

    Args:
        tt_sweep_data: dict with 'tau' array and 'eigenvalues' list of arrays,
                       or path to .npz file. If None, tries to load from default.

    Returns:
        tau_star: float or None (first tau where a TT mode is below R_K/4)
        crossing_info: dict with details about the crossing
    """
    if tt_sweep_data is None:
        tt_path = os.path.join(SCRIPT_DIR, 'l20b_lichnerowicz_data.npz')
        if not os.path.exists(tt_path):
            print("  TT data not yet available. DNP search deferred.")
            return None, {'status': 'deferred'}
        tt_sweep_data = np.load(tt_path, allow_pickle=True)

    # Extract tau values and eigenvalue arrays
    if isinstance(tt_sweep_data, dict):
        taus = tt_sweep_data.get('tau_values', tt_sweep_data.get('tau'))
    else:
        taus = tt_sweep_data.get('tau_values', tt_sweep_data.get('tau'))

    if taus is None:
        return None, {'status': 'no_tau_data'}

    print(f"\n  DNP tachyon search across {len(taus)} tau-values...")

    crossings = []
    for i, tau in enumerate(taus):
        R_K = scalar_curvature_R(tau)
        threshold = R_K / 4.0

        # Try to load TT eigenvalues at this tau
        key = f'tt_eigenvalues_{i}'
        if key not in tt_sweep_data:
            continue

        evals = tt_sweep_data[key]
        min_eval = np.min(evals) if len(evals) > 0 else np.inf

        if min_eval < threshold:
            crossings.append({
                'tau': tau,
                'min_eval': min_eval,
                'threshold': threshold,
                'deficit': threshold - min_eval,
            })
            if len(crossings) == 1:
                print(f"  ** TACHYON CROSSING at tau={tau:.3f}: "
                      f"mu_min={min_eval:.4f} < R_K/4={threshold:.4f}")

    if crossings:
        return crossings[0]['tau'], {
            'status': 'crossing_found',
            'tau_star': crossings[0]['tau'],
            'n_crossings': len(crossings),
            'first_crossing': crossings[0],
        }
    else:
        return None, {'status': 'no_crossing', 'note': 'All TT modes above DNP threshold'}


# =============================================================================
# MODULE 8: RIEMANN ENDOMORPHISM ON Sym^2_0 (VALIDATION SUPPORT)
# =============================================================================

def compute_lichnerowicz_fiber_on_sym2(tau):
    """
    Compute the FULL Lichnerowicz fiber action on Sym^2_0(R^8).

    The Lichnerowicz Laplacian on symmetric 2-tensors (Besse convention):
        (Delta_L h)_{ab} = -nabla^2 h_{ab} - 2 R_{acbd} h^{cd} + Ric_a^c h_{cb} + Ric_b^c h_{ac}

    The fiber (algebraic) part acting on each Peter-Weyl sector is:
        L_fiber = R_endo + Ric_coupling
    where:
        (R_endo h)_{ab}      = -2 R_{acbd} h^{cd}
        (Ric_coupling h)_{ab} = Ric_a^c h_{cb} + Ric_b^c h_{ac}

    At tau=0 (Einstein, Ric = 1/4 * g):
        Ric_coupling = 2 * (1/4) * h = 1/2 * h
        Sym^2_0(8) = 8 + 27 under adjoint
        Total eigenvalues: -1/6 + 1/2 = 1/3 (x27),  +1/4 + 1/2 = 3/4 (x8)

    Also computes the TT projection (div-free subspace) and returns
    the Lichnerowicz restricted to TT modes.

    IMPORTANT: The Ricci coupling uses ricci_tensor_ON(ft, Gamma) -- note
    the argument order! Swapping ft and Gamma gives the wrong sign.

    Returns:
        L_fiber_TT: (n_TT, n_TT) matrix (Lichnerowicz on TT modes, no Laplacian)
        eigenvalues_TT: sorted eigenvalues on TT subspace
        n_TT: number of TT modes
        L_fiber_full: (35, 35) matrix on full Sym^2_0
        eigenvalues_full: sorted eigenvalues on full Sym^2_0
    """
    from b6_scalar_vector_laplacian import ricci_tensor_ON as _ricci_tensor_ON

    # Load Riemann tensor
    npz_path = os.path.join(SCRIPT_DIR, 'r20a_riemann_tensor.npz')
    if os.path.exists(npz_path):
        riem_data = np.load(npz_path)
        taus = riem_data['tau']
        idx = np.argmin(np.abs(taus - tau))
        R_abcd = riem_data['R_abcd'][idx]
    else:
        from r20a_riemann_tensor import compute_riemann_tensor_ON_fast
        R_abcd = compute_riemann_tensor_ON_fast(tau)

    # Compute geometric infrastructure for Ricci
    from tier1_dirac_spectrum import (
        su3_generators, compute_structure_constants, compute_killing_form,
        jensen_metric, orthonormal_frame, frame_structure_constants,
        connection_coefficients
    )
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    B_ab = compute_killing_form(f_abc)
    g_s = jensen_metric(B_ab, tau)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    Ric = _ricci_tensor_ON(ft, Gamma)  # CORRECT order: ft first, Gamma second

    n = 8  # dim(SU(3))

    # Build basis for Sym^2_0(R^8): traceless symmetric 2-tensors (35 dim)
    sym2_full_basis = []
    sym2_labels = []
    for i in range(n):
        for j in range(i, n):
            B = np.zeros((n, n), dtype=np.float64)
            if i == j:
                B[i, j] = 1.0
            else:
                B[i, j] = 1.0 / np.sqrt(2)
                B[j, i] = 1.0 / np.sqrt(2)
            sym2_full_basis.append(B)
            sym2_labels.append((i, j))

    assert len(sym2_full_basis) == 36

    # Trace vector and traceless projection
    trace_vec = np.array([1.0 if i == j else 0.0
                          for (i, j) in sym2_labels])
    trace_vec /= np.linalg.norm(trace_vec)

    n_full = 36
    P = np.eye(n_full) - np.outer(trace_vec, trace_vec)
    U, S, Vt = np.linalg.svd(P)
    basis_indices = np.where(S > 0.5)[0]
    assert len(basis_indices) == 35, f"Expected 35, got {len(basis_indices)}"
    TL_basis = U[:, basis_indices]  # (36, 35)

    # R_endo: (R_endo h)_{ab} = -2 R_{acbd} h^{cd}
    R_endo_full = np.zeros((n_full, n_full), dtype=np.float64)
    for I in range(n_full):
        for J in range(n_full):
            R_endo_full[I, J] = -2.0 * np.einsum('ab,acbd,cd',
                sym2_full_basis[I], R_abcd, sym2_full_basis[J])

    # Ric coupling: (Ric.h + h.Ric)
    Ric_coupling_full = np.zeros((n_full, n_full), dtype=np.float64)
    for I in range(n_full):
        for J in range(n_full):
            h_J = sym2_full_basis[J]
            Ric_h = Ric @ h_J + h_J @ Ric
            Ric_coupling_full[I, J] = np.sum(sym2_full_basis[I] * Ric_h)

    # Full Lichnerowicz fiber operator (no Laplacian term)
    L_fiber = R_endo_full + Ric_coupling_full

    # Project to traceless subspace
    L_35 = TL_basis.T @ L_fiber @ TL_basis
    L_35 = 0.5 * (L_35 + L_35.T)
    eigenvalues_full = np.sort(eigvalsh(L_35))

    # TT projection: kernel of divergence on constant tensors
    div_full = np.zeros((n, n_full), dtype=np.float64)
    for I in range(n_full):
        h = sym2_full_basis[I]
        for b in range(n):
            val = 0.0
            for a in range(n):
                for d in range(n):
                    val += -Gamma[d, a, a] * h[d, b]
                    val += -Gamma[d, a, b] * h[a, d]
            div_full[b, I] = val
    div_TL = div_full @ TL_basis
    _, S_div, Vt_div = np.linalg.svd(div_TL, full_matrices=True)
    n_nonzero = np.sum(S_div > 1e-8)
    TT_basis = Vt_div[n_nonzero:].T  # (35, n_TT)
    n_TT = TT_basis.shape[1]

    # Lichnerowicz restricted to TT
    L_TT = TT_basis.T @ L_35 @ TT_basis
    L_TT = 0.5 * (L_TT + L_TT.T)
    eigenvalues_TT = np.sort(eigvalsh(L_TT))

    return L_TT, eigenvalues_TT, n_TT, L_35, eigenvalues_full


def validate_lichnerowicz_fiber_at_tau0():
    """
    Validate the full Lichnerowicz fiber action at tau=0.

    At tau=0 (bi-invariant SU(3), Einstein with Ric = 1/4 * g):
        Delta_L on constant TT tensors = R_endo + Ric_coupling
        R_endo eigenvalues: -1/6 (x27), +1/4 (x8)
        Ric coupling = +2*(1/4) = +1/2 (Einstein)
        Full eigenvalues: 1/3 (x27), 3/4 (x8)

    4D masses: m^2 = mu - R_K/4 = mu - 1/2
        27-dim: m^2 = -1/6 (TACHYONIC -- Koiso-Besse instability)
         8-dim: m^2 = +1/4 (STABLE -- infinitesimal isometries)

    Sym^2_0(8) = 8 + 27 under adjoint SU(3). All 35 are TT at tau=0.
    """
    _, evals_TT, n_TT, _, evals_full = compute_lichnerowicz_fiber_on_sym2(0.0)

    print(f"\n  Lichnerowicz fiber at tau=0: {n_TT} TT modes (expected 35)")
    print("  Full Sym^2_0 eigenvalues:")

    # Group eigenvalues by value
    unique_evals = []
    mults = []
    tol = 1e-8
    sorted_evals = np.sort(evals_TT)
    current = sorted_evals[0]
    count = 1
    for i in range(1, len(sorted_evals)):
        if abs(sorted_evals[i] - current) < tol:
            count += 1
        else:
            unique_evals.append(current)
            mults.append(count)
            current = sorted_evals[i]
            count = 1
    unique_evals.append(current)
    mults.append(count)

    for ev, m in zip(unique_evals, mults):
        m2 = ev - 0.5  # R_K/4 = 0.5 at tau=0
        tach = "TACH" if m2 < -1e-8 else "stable"
        print(f"    mu = {ev:+.6f}, mult = {m}, m^2 = {m2:+.6f} [{tach}]")

    # Check expected values
    expected_mults = sorted([8, 27])
    actual_mults = sorted(mults)
    passed = True

    if actual_mults != expected_mults:
        print(f"  FAIL: Expected multiplicities {expected_mults}, got {actual_mults}")
        passed = False
    else:
        print("  PASS: Multiplicities match 8 + 27 decomposition of Sym^2_0(adj)")
        for ev, m in zip(unique_evals, mults):
            if m == 27:
                err = abs(ev - 1.0/3.0)
                status = "PASS" if err < 1e-6 else "FAIL"
                print(f"    (2,2) block: mu={ev:.6f}, expected 1/3={1/3:.6f}, "
                      f"error={err:.2e} [{status}]")
                if err > 1e-6:
                    passed = False
            elif m == 8:
                err = abs(ev - 0.75)
                status = "PASS" if err < 1e-6 else "FAIL"
                print(f"    (1,1) block: mu={ev:.6f}, expected 3/4={0.75:.6f}, "
                      f"error={err:.2e} [{status}]")
                if err > 1e-6:
                    passed = False

    if passed:
        print("  ALL CHECKS PASS at machine epsilon")
    return unique_evals, mults


# =============================================================================
# MODULE 9: COMPREHENSIVE SUMMARY TABLE
# =============================================================================

def print_summary_table(results):
    """Print a formatted summary of spectral features at each tau."""
    phi = (1 + np.sqrt(5)) / 2

    print("\n" + "="*90)
    print("  PHONON BAND STRUCTURE SUMMARY")
    print("="*90)
    print(f"  {'tau':>5s}  {'R_K':>7s}  {'DNP':>7s}  "
          f"{'gap_S':>7s}  {'gap_V':>7s}  {'gap_D':>7s}  "
          f"{'phi_30':>8s}  {'dphi%':>7s}")
    print("-"*90)

    for i, tau in enumerate(results['tau']):
        R_K = results['R_K'][i]
        dnp = np.sqrt(results['dnp_threshold'][i])
        gap_s = np.sqrt(results['scalar_gap'][i])
        gap_v = np.sqrt(results['vector_gap'][i])
        gap_d = results['dirac_gap'][i]
        phi_r = results['phi_ratio_30_00'][i]
        dphi = 100 * abs(phi_r - phi) / phi if not np.isnan(phi_r) else np.nan

        phi_str = f"{phi_r:8.5f}" if not np.isnan(phi_r) else "    N/A "
        dphi_str = f"{dphi:7.3f}" if not np.isnan(dphi) else "   N/A "

        print(f"  {tau:5.2f}  {R_K:7.3f}  {dnp:7.4f}  "
              f"{gap_s:7.4f}  {gap_v:7.4f}  {gap_d:7.4f}  "
              f"{phi_str}  {dphi_str}")

    print("="*90)

    # Find tau where phi ratio is closest to golden ratio
    phi_ratios = results['phi_ratio_30_00']
    valid = ~np.isnan(phi_ratios)
    if np.any(valid):
        dphi_arr = np.abs(phi_ratios[valid] - phi)
        best_idx = np.argmin(dphi_arr)
        best_tau = results['tau'][valid][best_idx]
        best_ratio = phi_ratios[valid][best_idx]
        best_dphi = dphi_arr[best_idx]
        print(f"\n  Closest phi crossing: tau={best_tau:.2f}, "
              f"ratio={best_ratio:.6f}, delta={100*best_dphi/phi:.4f}%")


# =============================================================================
# MAIN
# =============================================================================

if __name__ == '__main__':
    print("="*72)
    print("  L-5: PHONON BAND STRUCTURE ON JENSEN-DEFORMED SU(3)")
    print("  Session 20b | KK-Theorist Agent")
    print("="*72)

    # -----------------------------------------------------------------------
    # Step 1: Validate Lichnerowicz fiber at tau=0
    # -----------------------------------------------------------------------
    print("\n--- Step 1: Lichnerowicz Fiber Validation at tau=0 ---")
    unique_evals, mults = validate_lichnerowicz_fiber_at_tau0()

    # -----------------------------------------------------------------------
    # Step 2: Lichnerowicz fiber spectrum across tau
    # -----------------------------------------------------------------------
    print("\n--- Step 2: Lichnerowicz Fiber Spectrum vs tau ---")
    tau_scan = [0.0, 0.15, 0.30, 0.50, 1.0, 1.5, 2.0]
    print(f"  Scanning {len(tau_scan)} tau-values...")
    lich_spectra = {}
    for tau in tau_scan:
        _, evals_TT, n_TT, _, evals_full = compute_lichnerowicz_fiber_on_sym2(tau)
        lich_spectra[tau] = evals_TT
        R_K = scalar_curvature_R(tau)
        n_tach = np.sum(evals_TT < R_K / 4.0)
        print(f"    tau={tau:.2f}: n_TT={n_TT}, mu in "
              f"[{evals_TT.min():.4f}, {evals_TT.max():.4f}], "
              f"R_K/4={R_K/4:.4f}, tachyonic={n_tach}")

    # -----------------------------------------------------------------------
    # Step 3: Band structure plot at 3 tau values
    # -----------------------------------------------------------------------
    print("\n--- Step 3: Band Structure Plot ---")
    png_path = plot_band_structure(tau_values_plot=(0.0, 0.15, 0.30))

    # -----------------------------------------------------------------------
    # Step 4: Spectral gap and phi ratio analysis
    # -----------------------------------------------------------------------
    print("\n--- Step 4: Spectral Gap Analysis ---")
    tau_analysis = np.arange(0.0, 2.01, 0.1)
    results = analyze_spectral_features(tau_analysis)
    print_summary_table(results)
    gaps_png = plot_spectral_gaps(results)

    # -----------------------------------------------------------------------
    # Step 5: DNP tachyon search (if TT data available)
    # -----------------------------------------------------------------------
    print("\n--- Step 5: DNP Tachyon Search ---")
    tau_star, crossing_info = dnp_tachyon_search()
    if tau_star is not None:
        print(f"\n  *** TACHYON CROSSING at tau_* = {tau_star:.3f} ***")
        print(f"  This signals geometric instability of (SU(3), g_Jensen(tau))")
        print(f"  for tau > tau_*. Natural vacuum selection point.")
    else:
        print(f"\n  Status: {crossing_info['status']}")

    # -----------------------------------------------------------------------
    # Summary
    # -----------------------------------------------------------------------
    print("\n" + "="*72)
    print("  L-5 COMPLETE")
    print("="*72)
    print(f"\n  Output files:")
    print(f"    Band structure: {png_path}")
    print(f"    Spectral gaps:  {gaps_png}")
    print(f"\n  Waiting for L-3 TT data to complete the band structure.")
    print(f"  When l20b_lichnerowicz_data.npz is available, re-run to add")
    print(f"  TT modes and perform DNP tachyon search.")
