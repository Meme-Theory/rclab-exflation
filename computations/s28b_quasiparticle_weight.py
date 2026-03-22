"""
Session 28b Computation 4: L-6 Quasiparticle Weight Z(tau)
==========================================================

PHYSICS:
    The quasiparticle weight Z measures how well D_can (canonical/torsionful)
    gap-edge eigenstates can be described in terms of D_K (Levi-Civita)
    eigenstates. This is the spectral analog of the Landau quasiparticle
    residue in condensed matter physics.

    Z(tau) = max_m |<psi_1^{can}(tau) | psi_m^{K}(tau)>|^2

    where:
        |psi_1^{can}> is the gap-edge eigenstate of D_can
        |psi_m^{K}>   are all eigenstates of D_K

    Z = 1: gap-edge states are identical in both bases (torsion has no
           effect on wavefunction structure, only on eigenvalues)
    Z = 0: gap-edge states are completely orthogonal (maximal torsion mixing)
    Z < 0.5: strong torsion mixing -- the gap-edge D_can state has less than
             50% overlap with any single D_K eigenstate

    PHYSICAL SIGNIFICANCE:
    If Z ~ 1, the D_can eigenstates are just relabeled D_K states, and
    switching from D_K to D_can does not change the BCS physics substantially.
    If Z << 1, torsion genuinely reshuffles the Hilbert space, creating
    new gap-edge states that are superpositions of many D_K modes.

METHOD:
    Reconstruct both D_can and D_K Dirac operators from tier1 infrastructure,
    diagonalize both, compute eigenvector overlaps.

    We also compute the full overlap matrix O_{nm} = |<psi_n^{can}|psi_m^{K}>|^2
    and extract:
    - Z_gap: overlap for gap-edge states only
    - IPR: inverse participation ratio in the K-basis (how many K-modes
            contribute to one can-mode)
    - Spectral distance: ||evals_can - sort(evals_K)||_2 as a sanity check

DATA SOURCE:
    Reconstructed from tier1_dirac_spectrum.py + s27_torsion_gap_gate.py
    (same infrastructure used in s28a_torsionful_bcs.py)

OUTPUT:
    - s28b_quasiparticle_weight.npz
    - s28b_quasiparticle_weight.png

GATE L-6: Diagnostic. Z_min < 0.5 at any tau would indicate strong
    torsion mixing.

Author: phonon-exflation-sim
Date: 2026-02-27
Session: 28b, Computation 4
"""

import sys
import os
import time
import numpy as np
from scipy.linalg import eigh
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

# Import geometry + irrep infrastructure
from tier1_dirac_spectrum import (
    su3_generators,
    compute_structure_constants,
    compute_killing_form,
    jensen_metric,
    orthonormal_frame,
    frame_structure_constants,
    connection_coefficients,
    spinor_connection_offset,
    build_cliff8,
    dirac_operator_on_irrep,
    get_irrep,
    _irrep_cache,
)

# Import M_Lie builder from s27
from s27_torsion_gap_gate import build_M_Lie


# ===========================================================================
# CONSTANTS
# ===========================================================================

TAU_VALUES = np.array([0.0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.50])
N_TAU = len(TAU_VALUES)

# Sectors: non-trivial with p+q <= 3
SECTORS = [
    (1, 0),   # fundamental (dim=3, N=48)
    (0, 1),   # anti-fundamental
    (1, 1),   # adjoint (dim=8, N=128)
    (2, 0),   # symmetric (dim=6, N=96)
    (0, 2),   # anti-symmetric
    (3, 0),   # (dim=10, N=160)
    (0, 3),
    (2, 1),   # (dim=15, N=240)
]
N_SECTORS = len(SECTORS)


# ===========================================================================
# GEOMETRY BUILDER
# ===========================================================================

def build_geometry(tau, gens, f_abc, gammas):
    """Build all geometric objects for a given tau.

    Returns:
        E: (8,8) orthonormal frame
        Gamma_LC: (8,8,8) Levi-Civita connection coefficients
        Omega_LC: (16,16) spinor connection
    """
    B_ab = compute_killing_form(f_abc)
    g_s = jensen_metric(B_ab, tau)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma_LC = connection_coefficients(ft)
    Omega_LC = spinor_connection_offset(Gamma_LC, gammas)
    return E, Gamma_LC, Omega_LC


# ===========================================================================
# EIGENSYSTEM BUILDERS
# ===========================================================================

def compute_eigensystem_Dcan(p, q, gens, f_abc, gammas, E):
    """Build and diagonalize D_can = M_Lie for sector (p,q).

    Returns:
        evals: (N,) real eigenvalues of 1j * D_can, sorted ascending
        evecs: (N, N) unitary, columns = eigenvectors
    """
    rho, dim_rho = get_irrep(p, q, gens, f_abc)
    M_Lie = build_M_Lie(rho, E, gammas)

    # Verify anti-Hermiticity
    ah_err = np.max(np.abs(M_Lie + M_Lie.conj().T))
    if ah_err > 1e-10:
        print(f"    WARNING: D_can anti-Hermiticity = {ah_err:.2e} for ({p},{q})")

    H = 1j * M_Lie
    evals, evecs = eigh(H)
    return evals, evecs


def compute_eigensystem_DK(p, q, gens, f_abc, gammas, E, Omega_LC):
    """Build and diagonalize D_K for sector (p,q).

    Returns:
        evals: (N,) real eigenvalues of 1j * D_K, sorted ascending
        evecs: (N, N) unitary, columns = eigenvectors
    """
    rho, dim_rho = get_irrep(p, q, gens, f_abc)
    D_K = dirac_operator_on_irrep(rho, E, gammas, Omega_LC)
    H = 1j * D_K
    evals, evecs = eigh(H)
    return evals, evecs


# ===========================================================================
# QUASIPARTICLE WEIGHT COMPUTATION
# ===========================================================================

def compute_overlap_matrix(evecs_can, evecs_K):
    """Compute the overlap matrix O_{nm} = |<psi_n^{can}|psi_m^{K}>|^2.

    Parameters:
        evecs_can: (N, N) unitary, columns = D_can eigenstates
        evecs_K:   (N, N) unitary, columns = D_K eigenstates

    Returns:
        O: (N, N) real non-negative matrix, doubly stochastic
           O[n, m] = |<psi_n^{can}|psi_m^{K}>|^2
    """
    # Overlap: S_{nm} = <psi_n^{can}|psi_m^{K}> = (evecs_can^dag @ evecs_K)_{nm}
    S = evecs_can.conj().T @ evecs_K
    O = np.abs(S) ** 2

    # Verification: each row and column should sum to 1 (doubly stochastic)
    row_sums = np.sum(O, axis=1)
    col_sums = np.sum(O, axis=0)
    row_err = np.max(np.abs(row_sums - 1.0))
    col_err = np.max(np.abs(col_sums - 1.0))

    if row_err > 1e-10 or col_err > 1e-10:
        print(f"    WARNING: overlap matrix not doubly stochastic. "
              f"row_err={row_err:.2e}, col_err={col_err:.2e}")

    return O


def gap_edge_indices(evals, n_edge=2):
    """Find indices of the gap-edge eigenvalues (closest to zero).

    For Kramers-degenerate spectra, eigenvalues come in pairs.
    Returns indices of the n_edge eigenvalues with smallest |evals|.

    Parameters:
        evals: (N,) sorted eigenvalues
        n_edge: number of gap-edge states to return

    Returns:
        indices: (n_edge,) array of indices into evals
    """
    abs_evals = np.abs(evals)
    # Sort by |eval| and return indices of smallest
    sorted_idx = np.argsort(abs_evals)
    return sorted_idx[:n_edge]


def compute_Z(O, gap_idx_can, gap_idx_K=None):
    """Compute quasiparticle weight Z from overlap matrix.

    Z = max_m |<psi_gap^{can} | psi_m^{K}>|^2

    This is the maximum overlap of a D_can gap-edge state with ANY D_K state.

    Also computes IPR = 1 / sum_m O[n,m]^2 (inverse participation ratio),
    which measures how many D_K states contribute to the D_can gap-edge state.

    Parameters:
        O: (N, N) overlap matrix
        gap_idx_can: indices of gap-edge states in D_can basis
        gap_idx_K: indices of gap-edge states in D_K basis (optional, for
                   gap-to-gap overlap)

    Returns:
        Z_max: max overlap of any gap-edge can state with any K state
        Z_gap_gap: overlap specifically between can gap-edge and K gap-edge
        IPR: inverse participation ratio
        Z_per_state: (n_edge,) Z for each gap-edge state
    """
    n_edge = len(gap_idx_can)

    # Z for each gap-edge can state: max over all K states
    Z_per_state = np.array([np.max(O[i, :]) for i in gap_idx_can])
    Z_max = np.max(Z_per_state)

    # Gap-to-gap overlap
    if gap_idx_K is not None:
        Z_gap_gap = np.max(O[np.ix_(gap_idx_can, gap_idx_K)])
    else:
        Z_gap_gap = Z_max

    # IPR for each gap-edge state (in K basis)
    # IPR = 1 / sum_m O[n,m]^2, measures effective number of K states
    IPR_per_state = np.array([
        1.0 / np.sum(O[i, :] ** 2) for i in gap_idx_can
    ])
    IPR = np.mean(IPR_per_state)

    return Z_max, Z_gap_gap, IPR, Z_per_state


# ===========================================================================
# MAIN COMPUTATION
# ===========================================================================

def main():
    t_start = time.time()

    print("=" * 72)
    print("SESSION 28b L-6: QUASIPARTICLE WEIGHT Z(tau)")
    print("=" * 72)
    print()

    # Initialize algebra
    print("Initializing SU(3) algebra and Clifford algebra...")
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    gammas = build_cliff8()
    n_gam = len(gammas)
    dim_gam = gammas[0].shape[0]
    print(f"  8 generators, {n_gam} Clifford matrices ({dim_gam}x{dim_gam})")
    print()

    # Storage
    Z_max_arr = np.full((N_SECTORS, N_TAU), np.nan)
    Z_gg_arr = np.full((N_SECTORS, N_TAU), np.nan)
    IPR_arr = np.full((N_SECTORS, N_TAU), np.nan)
    spectral_dist_arr = np.full((N_SECTORS, N_TAU), np.nan)
    eval_diff_max_arr = np.full((N_SECTORS, N_TAU), np.nan)

    # Number of gap-edge states to track
    N_EDGE = 4

    # Also store the full Z profile for the gap-edge states
    Z_profile = {}  # key: (i_s, i_t), value: (N_EDGE,) array

    # Header
    print(f"{'Sector':>8s} {'tau':>5s} {'Z_max':>8s} {'Z_gg':>8s} "
          f"{'IPR':>8s} {'spec_d':>10s} {'eval_d':>10s}")
    print("-" * 65)

    for i_s, (p, q) in enumerate(SECTORS):
        for i_t, tau in enumerate(TAU_VALUES):
            # Build geometry
            E, Gamma_LC, Omega_LC = build_geometry(tau, gens, f_abc, gammas)

            # Diagonalize both operators
            evals_can, evecs_can = compute_eigensystem_Dcan(p, q, gens, f_abc, gammas, E)
            evals_K, evecs_K = compute_eigensystem_DK(p, q, gens, f_abc, gammas, E, Omega_LC)

            # Overlap matrix
            O = compute_overlap_matrix(evecs_can, evecs_K)

            # Gap-edge indices
            gap_can = gap_edge_indices(evals_can, N_EDGE)
            gap_K = gap_edge_indices(evals_K, N_EDGE)

            # Quasiparticle weight
            Z_max, Z_gg, IPR, Z_per = compute_Z(O, gap_can, gap_K)

            Z_max_arr[i_s, i_t] = Z_max
            Z_gg_arr[i_s, i_t] = Z_gg
            IPR_arr[i_s, i_t] = IPR
            Z_profile[(i_s, i_t)] = Z_per

            # Spectral distance: how different are the eigenvalue spectra
            evals_can_sorted = np.sort(np.abs(evals_can))
            evals_K_sorted = np.sort(np.abs(evals_K))
            spectral_dist = np.linalg.norm(evals_can_sorted - evals_K_sorted)
            spectral_dist_arr[i_s, i_t] = spectral_dist

            # Max eigenvalue difference
            eval_diff_max_arr[i_s, i_t] = np.max(np.abs(evals_can_sorted - evals_K_sorted))

            # Print for selected tau
            if tau in [0.0, 0.15, 0.25, 0.35, 0.50]:
                print(f"  ({p},{q})  {tau:5.2f} {Z_max:8.5f} {Z_gg:8.5f} "
                      f"{IPR:8.2f} {spectral_dist:10.5f} {eval_diff_max_arr[i_s, i_t]:10.5f}")

        print()

    # ------------------------------------------------------------------
    # ANALYSIS
    # ------------------------------------------------------------------
    print("=" * 72)
    print("QUASIPARTICLE WEIGHT SUMMARY")
    print("=" * 72)
    print()

    print("--- Minimum Z_max per sector (lower = stronger torsion mixing) ---")
    print(f"  {'Sector':>8s} {'min Z':>8s} {'at tau':>7s} {'Z(0)':>8s} {'Z(0.50)':>8s} {'IPR_max':>8s}")
    print("  " + "-" * 50)

    Z_global_min = 1.0
    Z_global_min_sector = None
    Z_global_min_tau = 0.0

    for i_s, (p, q) in enumerate(SECTORS):
        min_Z = np.nanmin(Z_max_arr[i_s, :])
        min_tau = TAU_VALUES[np.nanargmin(Z_max_arr[i_s, :])]
        Z0 = Z_max_arr[i_s, 0]
        Z50 = Z_max_arr[i_s, -1]
        ipr_max = np.nanmax(IPR_arr[i_s, :])

        print(f"  ({p},{q})  {min_Z:8.5f} {min_tau:7.2f} {Z0:8.5f} {Z50:8.5f} {ipr_max:8.2f}")

        if min_Z < Z_global_min:
            Z_global_min = min_Z
            Z_global_min_sector = (p, q)
            Z_global_min_tau = min_tau

    print()
    print(f"  GLOBAL MINIMUM: Z = {Z_global_min:.5f} in ({Z_global_min_sector[0]},{Z_global_min_sector[1]}) "
          f"at tau = {Z_global_min_tau:.2f}")
    print()

    # --- tau=0 special case ---
    print("--- tau=0 diagnostic (bi-invariant metric) ---")
    print("  At tau=0, D_can and D_K should differ maximally OR minimally")
    print("  depending on whether Omega_LC mixes degenerate subspaces.")
    print()
    for i_s, (p, q) in enumerate(SECTORS):
        Z0 = Z_max_arr[i_s, 0]
        IPR0 = IPR_arr[i_s, 0]
        sdist0 = spectral_dist_arr[i_s, 0]
        print(f"  ({p},{q}): Z(0)={Z0:.5f}, IPR(0)={IPR0:.2f}, spec_dist(0)={sdist0:.5f}")
    print()

    # --- Gap-to-gap overlap ---
    print("--- Gap-to-gap overlap Z_gg (can gap-edge vs K gap-edge) ---")
    print(f"  {'Sector':>8s} ", end="")
    for t in TAU_VALUES:
        print(f"{'t=' + f'{t:.2f}':>8s}", end="")
    print()
    print("  " + "-" * (8 + 8 * N_TAU))
    for i_s, (p, q) in enumerate(SECTORS):
        print(f"  ({p},{q})  ", end="")
        for i_t in range(N_TAU):
            print(f"{Z_gg_arr[i_s, i_t]:8.4f}", end="")
        print()
    print()

    # --- IPR evolution ---
    print("--- IPR evolution (effective number of K-modes in can gap-edge) ---")
    print(f"  {'Sector':>8s} ", end="")
    for t in TAU_VALUES:
        print(f"{'t=' + f'{t:.2f}':>8s}", end="")
    print()
    print("  " + "-" * (8 + 8 * N_TAU))
    for i_s, (p, q) in enumerate(SECTORS):
        print(f"  ({p},{q})  ", end="")
        for i_t in range(N_TAU):
            print(f"{IPR_arr[i_s, i_t]:8.2f}", end="")
        print()
    print()

    # ------------------------------------------------------------------
    # GATE VERDICT
    # ------------------------------------------------------------------
    print("=" * 72)
    print("GATE L-6 VERDICT")
    print("=" * 72)
    print()

    strong_mixing = Z_global_min < 0.5
    moderate_mixing = Z_global_min < 0.7

    print(f"Z_min = {Z_global_min:.5f} in ({Z_global_min_sector[0]},{Z_global_min_sector[1]}) "
          f"at tau = {Z_global_min_tau:.2f}")
    print()

    if strong_mixing:
        verdict = (f"STRONG TORSION MIXING: Z_min = {Z_global_min:.4f} < 0.5. "
                   f"D_can gap-edge states are genuine superpositions of multiple D_K modes.")
    elif moderate_mixing:
        verdict = (f"MODERATE TORSION MIXING: Z_min = {Z_global_min:.4f} in [0.5, 0.7). "
                   f"Torsion partially reshuffles gap-edge states.")
    else:
        verdict = (f"WEAK TORSION MIXING: Z_min = {Z_global_min:.4f} >= 0.7. "
                   f"D_can gap-edge states are predominantly single D_K eigenstates.")

    print(f"VERDICT: {verdict}")
    print()

    # Check trend: does Z decrease with tau?
    for i_s, (p, q) in enumerate(SECTORS):
        Z_row = Z_max_arr[i_s, :]
        if Z_row[-1] < Z_row[0]:
            trend = "DECREASING"
        elif Z_row[-1] > Z_row[0]:
            trend = "INCREASING"
        else:
            trend = "FLAT"
        print(f"  ({p},{q}): Z(0)={Z_row[0]:.4f} -> Z(0.5)={Z_row[-1]:.4f} [{trend}]")

    print()

    # Identify tau where Z has minimum for each sector
    print("  Minimum-Z tau per sector:")
    for i_s, (p, q) in enumerate(SECTORS):
        min_idx = np.nanargmin(Z_max_arr[i_s, :])
        print(f"    ({p},{q}): tau_min = {TAU_VALUES[min_idx]:.2f}, "
              f"Z_min = {Z_max_arr[i_s, min_idx]:.5f}")
    print()

    # ------------------------------------------------------------------
    # SAVE DATA
    # ------------------------------------------------------------------
    outpath = os.path.join(SCRIPT_DIR, "s28b_quasiparticle_weight.npz")
    save_dict = {
        "tau_values": TAU_VALUES,
        "sectors": np.array(SECTORS),
        "Z_max": Z_max_arr,
        "Z_gap_gap": Z_gg_arr,
        "IPR": IPR_arr,
        "spectral_dist": spectral_dist_arr,
        "eval_diff_max": eval_diff_max_arr,
        "verdict": np.array(verdict),
    }
    np.savez_compressed(outpath, **save_dict)
    print(f"Saved: {outpath}")
    print()

    # ------------------------------------------------------------------
    # PLOT
    # ------------------------------------------------------------------
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle("L-6 Quasiparticle Weight Z(tau)", fontsize=14, fontweight='bold')

    sector_labels = [f"({p},{q})" for p, q in SECTORS]
    colors = plt.cm.tab10(np.linspace(0, 1, N_SECTORS))

    # --- Panel (a): Z_max vs tau line plot ---
    ax = axes[0, 0]
    for i_s, (p, q) in enumerate(SECTORS):
        ax.plot(TAU_VALUES, Z_max_arr[i_s, :], 'o-', color=colors[i_s],
                label=f"({p},{q})", markersize=4)
    ax.axhline(y=0.5, color='red', linestyle=':', linewidth=2, label='Z=0.5 threshold')
    ax.axhline(y=0.7, color='orange', linestyle=':', linewidth=1, label='Z=0.7 moderate')
    ax.set_xlabel(r"$\tau$")
    ax.set_ylabel(r"$Z_{\max}(\tau)$")
    ax.set_title(r"Quasiparticle weight $Z = \max_m |\langle\psi_{gap}^{can}|\psi_m^K\rangle|^2$")
    ax.legend(fontsize=7, ncol=2)
    ax.set_ylim(-0.05, 1.05)
    ax.grid(True, alpha=0.3)

    # --- Panel (b): Z_gap_gap vs tau ---
    ax = axes[0, 1]
    for i_s, (p, q) in enumerate(SECTORS):
        ax.plot(TAU_VALUES, Z_gg_arr[i_s, :], 'o-', color=colors[i_s],
                label=f"({p},{q})", markersize=4)
    ax.axhline(y=0.5, color='red', linestyle=':', linewidth=2, label='Z=0.5')
    ax.set_xlabel(r"$\tau$")
    ax.set_ylabel(r"$Z_{gap-gap}(\tau)$")
    ax.set_title(r"Gap-to-gap overlap (can gap-edge $\leftrightarrow$ K gap-edge)")
    ax.legend(fontsize=7, ncol=2)
    ax.set_ylim(-0.05, 1.05)
    ax.grid(True, alpha=0.3)

    # --- Panel (c): IPR vs tau ---
    ax = axes[1, 0]
    for i_s, (p, q) in enumerate(SECTORS):
        ax.plot(TAU_VALUES, IPR_arr[i_s, :], 's-', color=colors[i_s],
                label=f"({p},{q})", markersize=4)
    ax.axhline(y=1.0, color='gray', linestyle=':', linewidth=1, label='IPR=1 (no mixing)')
    ax.set_xlabel(r"$\tau$")
    ax.set_ylabel("IPR")
    ax.set_title("Inverse participation ratio (effective # of K-modes in can gap-edge)")
    ax.legend(fontsize=7, ncol=2)
    ax.grid(True, alpha=0.3)

    # --- Panel (d): Heatmap of Z_max ---
    ax = axes[1, 1]
    im = ax.imshow(Z_max_arr, aspect='auto', cmap='RdYlGn',
                   vmin=0, vmax=1, interpolation='nearest')
    ax.set_xticks(range(N_TAU))
    ax.set_xticklabels([f"{t:.2f}" for t in TAU_VALUES], fontsize=8, rotation=45)
    ax.set_yticks(range(N_SECTORS))
    ax.set_yticklabels(sector_labels, fontsize=9)
    ax.set_xlabel(r"$\tau$")
    ax.set_ylabel("Sector (p,q)")
    ax.set_title(r"$Z_{\max}$ heatmap")
    plt.colorbar(im, ax=ax, label=r"$Z_{\max}$")
    for i_s in range(N_SECTORS):
        for i_t in range(N_TAU):
            val = Z_max_arr[i_s, i_t]
            if not np.isnan(val):
                ax.text(i_t, i_s, f"{val:.2f}", ha='center', va='center',
                        fontsize=6, color='white' if val < 0.4 else 'black')

    plt.tight_layout()
    figpath = os.path.join(SCRIPT_DIR, "s28b_quasiparticle_weight.png")
    fig.savefig(figpath, dpi=150, bbox_inches='tight')
    print(f"Saved: {figpath}")
    plt.close(fig)

    elapsed = time.time() - t_start
    print(f"\nTotal time: {elapsed:.1f}s")


if __name__ == "__main__":
    main()
