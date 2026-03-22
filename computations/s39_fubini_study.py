"""
Session 39 Gate FS-METRIC-39: Fubini-Study Quantum Metric at the Fold
=====================================================================

Computes the Fubini-Study quantum metric g_FS(tau) on the B2 eigenspace
of the Dirac operator D_K on (SU(3), g_tau) in the (0,0) trivial sector.

The quantum metric is defined as:
    g_FS_ij(tau) = Re[ <d_tau psi_i | (1 - P_B2) | d_tau psi_j> ]

where P_B2 = sum_{i in B2} |psi_i><psi_i| and |d_tau psi_i> is computed
via central finite differences.

The Berry curvature for a 1D parameter is:
    F_ij(tau) = -2 * Im[ <d_tau psi_i | (1 - P_B2) | d_tau psi_j> ]

Since we have a single parameter (tau), the Berry curvature 2-form vanishes
identically for Abelian (single-band) cases. For the non-Abelian B2 quartet,
the off-diagonal elements of F_ij capture the internal rearrangement of
eigenstates within the degenerate subspace.

Gate criterion (pre-registered):
    PASS: g_FS peaks within tau in [0.17, 0.21]
    FAIL: g_FS monotonic or peaks elsewhere

Physical significance:
    - Peotta-Torma theorem: superfluid weight D_s = g_FS * n_s
    - Large g_FS at fold => rapid eigenstate rotation => van Hove singularity
    - If g_FS diverges, this is the geometric origin of P_exc = 1.000

Author: gen-physicist (Session 39)
Date: 2026-03-09
"""

import os
import sys
import numpy as np
from scipy.linalg import eigh as scipy_eigh
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Add tier0-computation to path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

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
    validate_clifford,
)


# =============================================================================
# MODULE 1: COMPUTE D_K EIGENSTATES AT GIVEN TAU
# =============================================================================

def compute_omega_at_tau(tau, gens, f_abc, gammas):
    """
    Compute the spinor curvature offset Omega(tau) for the (0,0) trivial sector.

    In the trivial sector, the Dirac operator is D_{(0,0)} = Omega,
    a 16x16 anti-Hermitian matrix acting on spinor space alone.

    Args:
        tau: Jensen deformation parameter
        gens: su(3) generators
        f_abc: structure constants
        gammas: Clifford generators

    Returns:
        Omega: (16,16) anti-Hermitian matrix
        E: (8,8) orthonormal frame (for downstream use)
    """
    B_ab = compute_killing_form(f_abc)
    g_s = jensen_metric(B_ab, tau)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    Omega = spinor_connection_offset(Gamma, gammas)
    return Omega, E


def diagonalize_omega(Omega):
    """
    Diagonalize D_{(0,0)} = Omega via H = 1j * Omega (Hermitian).

    Returns real eigenvalues mu_n (of H) sorted ascending,
    and orthonormal eigenvectors as columns.

    The Dirac eigenvalues are lambda_n = -i * mu_n (purely imaginary).
    The physical eigenvalue magnitudes are |mu_n|.

    The spectrum has particle-hole symmetry: eigenvalues come in +/- pairs.
    Positive eigenvalues (ascending): B1(1), B2(4), B3(3) -- total 8.
    Negative eigenvalues: mirror of positive.

    Args:
        Omega: (16,16) anti-Hermitian matrix

    Returns:
        evals: (16,) real eigenvalues of H = 1j*Omega, sorted ascending
        evecs: (16,16) unitary, columns = eigenvectors
    """
    H = 1j * Omega
    # Verify Hermiticity
    h_err = np.max(np.abs(H - H.conj().T))
    if h_err > 1e-10:
        print(f"  WARNING: H = 1j*Omega not Hermitian, err={h_err:.2e}")

    evals, evecs = scipy_eigh(H)
    return evals, evecs


def identify_B2_indices(evals, tol=1e-4):
    """
    Identify the B2 quartet among the positive eigenvalues.

    The (0,0) sector has 16 eigenvalues: 8 negative + 8 positive (by PH symmetry).
    Among the 8 positive eigenvalues (sorted ascending):
        B1: 1 mode (smallest positive)
        B2: 4 modes (4-fold degenerate, middle)
        B3: 3 modes (3-fold degenerate, largest)

    We identify B2 as the 4-fold degenerate cluster among positive eigenvalues.

    Args:
        evals: (16,) sorted eigenvalues
        tol: tolerance for degeneracy identification

    Returns:
        b2_idx: array of 4 indices into evals (the B2 quartet)
        b1_idx: array of 1 index (B1)
        b3_idx: array of 3 indices (B3)
    """
    pos_mask = evals > 0
    pos_indices = np.where(pos_mask)[0]
    pos_evals = evals[pos_indices]

    # Cluster the 8 positive eigenvalues
    # Sorted ascending: B1(1), B2(4), B3(3)
    # Find clusters by checking gaps
    clusters = []
    current_cluster = [0]
    for i in range(1, len(pos_evals)):
        if abs(pos_evals[i] - pos_evals[i-1]) < tol:
            current_cluster.append(i)
        else:
            clusters.append(current_cluster)
            current_cluster = [i]
    clusters.append(current_cluster)

    # Identify by multiplicity
    b1_local = None
    b2_local = None
    b3_local = None

    for c in clusters:
        if len(c) == 1:
            b1_local = c
        elif len(c) == 4:
            b2_local = c
        elif len(c) == 3:
            b3_local = c

    if b2_local is None:
        # Fallback: the middle 4 positive eigenvalues
        print("  WARNING: Could not identify B2 by degeneracy, using positional fallback")
        b1_local = [0]
        b2_local = [1, 2, 3, 4]
        b3_local = [5, 6, 7]

    b2_idx = pos_indices[b2_local]
    b1_idx = pos_indices[b1_local] if b1_local is not None else np.array([], dtype=int)
    b3_idx = pos_indices[b3_local] if b3_local is not None else np.array([], dtype=int)

    return np.array(b2_idx), np.array(b1_idx), np.array(b3_idx)


# =============================================================================
# MODULE 2: GAUGE-FIXING FOR DEGENERATE EIGENSTATES
# =============================================================================

def parallel_transport_gauge(evecs_prev, evecs_curr, b2_idx):
    """
    Fix the gauge of degenerate B2 eigenstates by parallel transport.

    For a degenerate subspace, scipy_eigh returns an arbitrary unitary rotation
    within the subspace at each tau. We fix this by requiring maximal overlap
    with the previous tau step (parallel transport gauge).

    Concretely: compute the 4x4 overlap matrix
        O_{ij} = <psi_i(tau_prev) | psi_j(tau_curr)>
    and apply the SVD rotation: U S V^dag = O, then psi_new = psi_curr @ V @ U^dag
    so that the new states maximally overlap the previous ones.

    Args:
        evecs_prev: (16,16) eigenvectors at previous tau
        evecs_curr: (16,16) eigenvectors at current tau
        b2_idx: indices of B2 states

    Returns:
        evecs_fixed: (16,16) eigenvectors with B2 gauge-fixed
    """
    n_b2 = len(b2_idx)
    psi_prev = evecs_prev[:, b2_idx]  # (16, 4)
    psi_curr = evecs_curr[:, b2_idx]  # (16, 4)

    # Overlap matrix
    O = psi_prev.conj().T @ psi_curr  # (4, 4)

    # SVD: O = U S V^dag
    U, S, Vdag = np.linalg.svd(O)

    # Rotation to align: R = V U^dag (acts on right: psi_new = psi_curr @ R)
    R = Vdag.conj().T @ U.conj().T  # (4, 4)

    evecs_fixed = evecs_curr.copy()
    evecs_fixed[:, b2_idx] = psi_curr @ R

    return evecs_fixed


# =============================================================================
# MODULE 3: FUBINI-STUDY QUANTUM METRIC COMPUTATION
# =============================================================================

def compute_fubini_study(tau_values, gens, f_abc, gammas, dtau=None):
    """
    Compute the Fubini-Study quantum metric g_FS(tau) and Berry curvature
    F_Berry(tau) on the B2 eigenspace across a range of tau values.

    Method:
        1. At each tau, compute Omega and diagonalize to get eigenstates.
        2. Gauge-fix by parallel transport.
        3. Compute |d_tau psi_i> via central finite differences.
        4. Compute g_FS_ij = Re[<d_tau psi_i | Q | d_tau psi_j>]
           where Q = 1 - P_B2.
        5. Compute F_ij = -2 Im[<d_tau psi_i | Q | d_tau psi_j>]

    For steps requiring tau +/- dtau, we also need eigenstates at those points.
    We use a fine mesh with spacing dtau and compute derivatives at interior points.

    Args:
        tau_values: array of tau values at which to report g_FS
        gens, f_abc, gammas: algebraic infrastructure
        dtau: finite difference step (default: min spacing / 10)

    Returns:
        results: dict with keys:
            'tau': array of tau values
            'g_FS_scalar': scalar quantum metric Tr(g_FS)/4 at each tau
            'g_FS_tensor': (N, 4, 4) quantum metric tensor at each tau
            'F_Berry_tensor': (N, 4, 4) Berry curvature tensor at each tau
            'evals_B2': (N, 4) B2 eigenvalues at each tau
            'evals_B1': (N,) B1 eigenvalue at each tau
            'evals_B3': (N, 3) B3 eigenvalues at each tau
            'all_evals': (N, 16) all eigenvalues at each tau
    """
    if dtau is None:
        dtau = 1e-5  # Very fine step for numerical derivative

    N = len(tau_values)

    # Storage
    g_FS_scalar = np.zeros(N)
    g_FS_tensor = np.zeros((N, 4, 4))
    F_Berry_tensor = np.zeros((N, 4, 4))
    evals_B2 = np.zeros((N, 4))
    evals_B1 = np.zeros(N)
    evals_B3 = np.zeros((N, 3))
    all_evals = np.zeros((N, 16))

    # For parallel transport gauge: compute at a reference tau first
    # We use the first tau value as reference
    Omega_ref, _ = compute_omega_at_tau(tau_values[0], gens, f_abc, gammas)
    evals_ref, evecs_ref = diagonalize_omega(Omega_ref)
    b2_idx_ref, b1_idx_ref, b3_idx_ref = identify_B2_indices(evals_ref)

    print(f"\n  Reference (tau={tau_values[0]:.3f}):")
    print(f"    B1 eigenvalue: {evals_ref[b1_idx_ref]}")
    print(f"    B2 eigenvalues: {evals_ref[b2_idx_ref]}")
    print(f"    B3 eigenvalues: {evals_ref[b3_idx_ref]}")

    prev_evecs = evecs_ref

    for n, tau in enumerate(tau_values):
        print(f"\n  tau = {tau:.4f} ({n+1}/{N})")

        # --- Step A: Compute eigenstates at tau, tau-dtau, tau+dtau ---
        Omega_c, _ = compute_omega_at_tau(tau, gens, f_abc, gammas)
        Omega_m, _ = compute_omega_at_tau(tau - dtau, gens, f_abc, gammas)
        Omega_p, _ = compute_omega_at_tau(tau + dtau, gens, f_abc, gammas)

        evals_c, evecs_c = diagonalize_omega(Omega_c)
        evals_m, evecs_m = diagonalize_omega(Omega_m)
        evals_p, evecs_p = diagonalize_omega(Omega_p)

        # Identify B2 indices at center point
        b2_idx, b1_idx, b3_idx = identify_B2_indices(evals_c)

        # Store eigenvalues
        all_evals[n] = evals_c
        evals_B2[n] = evals_c[b2_idx]
        if len(b1_idx) > 0:
            evals_B1[n] = evals_c[b1_idx[0]]
        if len(b3_idx) >= 3:
            evals_B3[n] = evals_c[b3_idx[:3]]

        # --- Step B: Gauge-fix all three sets of eigenvectors ---
        # First gauge-fix center to previous
        evecs_c = parallel_transport_gauge(prev_evecs, evecs_c, b2_idx)
        # Then gauge-fix minus and plus to center
        # Need to identify B2 at minus and plus points too
        b2_idx_m, _, _ = identify_B2_indices(evals_m)
        b2_idx_p, _, _ = identify_B2_indices(evals_p)

        evecs_m = parallel_transport_gauge(evecs_c, evecs_m, b2_idx_m)
        evecs_p = parallel_transport_gauge(evecs_c, evecs_p, b2_idx_p)

        # Update prev for next iteration
        prev_evecs = evecs_c

        # --- Step C: Numerical derivative of B2 states ---
        # |d_tau psi_i> = (|psi_i(tau+dtau)> - |psi_i(tau-dtau)>) / (2*dtau)
        psi_c = evecs_c[:, b2_idx]      # (16, 4)
        psi_m = evecs_m[:, b2_idx_m]    # (16, 4)
        psi_p = evecs_p[:, b2_idx_p]    # (16, 4)

        dpsi = (psi_p - psi_m) / (2.0 * dtau)  # (16, 4)

        # --- Step D: Projector onto B2 subspace ---
        # P_B2 = |psi_c><psi_c| for B2 states
        P_B2 = psi_c @ psi_c.conj().T  # (16, 16)

        # Q = 1 - P_B2
        Q = np.eye(16, dtype=complex) - P_B2

        # --- Step E: Quantum metric tensor ---
        # g_FS_ij = Re[ <d_tau psi_i | Q | d_tau psi_j> ]
        # Q_dpsi = Q @ dpsi  # (16, 4)
        Q_dpsi = Q @ dpsi

        g_FS_ij = np.real(dpsi.conj().T @ Q_dpsi)  # (4, 4)
        g_FS_tensor[n] = g_FS_ij

        # Scalar quantum metric: Tr(g_FS) / dim(B2)
        g_FS_scalar[n] = np.trace(g_FS_ij) / 4.0

        # --- Step F: Berry curvature tensor ---
        # F_ij = -2 * Im[ <d_tau psi_i | Q | d_tau psi_j> ]
        F_ij = -2.0 * np.imag(dpsi.conj().T @ Q_dpsi)  # (4, 4)
        F_Berry_tensor[n] = F_ij

        # Print diagnostics
        g_eigenvalues = np.linalg.eigvalsh(g_FS_ij)
        print(f"    B2 evals: {evals_c[b2_idx]}")
        print(f"    g_FS trace/4 = {g_FS_scalar[n]:.6f}")
        print(f"    g_FS eigenvalues: {g_eigenvalues}")
        print(f"    |F_Berry| max element: {np.max(np.abs(F_ij)):.6f}")

        # Sanity check: <dpsi|dpsi> total (before Q projection)
        total_dpsi_sq = np.real(np.trace(dpsi.conj().T @ dpsi)) / 4.0
        print(f"    <d_tau psi|d_tau psi>/4 (total, no Q) = {total_dpsi_sq:.6f}")

    results = {
        'tau': tau_values,
        'g_FS_scalar': g_FS_scalar,
        'g_FS_tensor': g_FS_tensor,
        'F_Berry_tensor': F_Berry_tensor,
        'evals_B2': evals_B2,
        'evals_B1': evals_B1,
        'evals_B3': evals_B3,
        'all_evals': all_evals,
    }
    return results


# =============================================================================
# MODULE 4: PEOTTA-TORMA COMPARISON
# =============================================================================

def peotta_torma_comparison(g_FS_at_fold, bcs_data_path):
    """
    Compare g_FS with the Peotta-Torma flat-band superfluid weight.

    Peotta-Torma theorem (2015): For flat-band superconductors,
        D_s = (n_s / m*) * g_FS
    where n_s = 2|v_k|^2 is the superfluid density and g_FS is the
    quantum metric (band-averaged).

    For BCS: Delta_0 relates to D_s through the London penetration depth,
    but the more direct comparison is:
        D_s = g_FS * |Delta_0|^2 / (E_F * V_cell)
    in the flat-band limit.

    We compare qualitatively: is g_FS large enough to make the B2 band
    effectively flat from a superfluid weight perspective?

    Args:
        g_FS_at_fold: scalar quantum metric at the fold
        bcs_data_path: path to s37 pair susceptibility data

    Returns:
        comparison: dict with comparison quantities
    """
    comparison = {}

    if os.path.exists(bcs_data_path):
        d = np.load(bcs_data_path, allow_pickle=True)
        E_cond = float(d['E_cond'])
        E_8 = d['E_8']
        rho = d['rho']

        # BCS gap from E_cond: Delta_0 ~ sqrt(2 * |E_cond| / N(E_F))
        # From s37: E_cond = -0.137, rho(B2) = 14.02
        N_EF = rho[0]  # DOS at Fermi level for B2
        Delta_0_est = np.sqrt(2.0 * abs(E_cond) / N_EF)

        # Flat-band superfluid weight: D_s = g_FS * filling * Delta^2
        # For our case: filling f = 1/2 (half-filled B2 quartet)
        # D_s = g_FS * (1/2) * Delta_0^2 per mode
        D_s = g_FS_at_fold * 0.5 * Delta_0_est**2

        # Conventional BCS: D_s = n_s / (4 * m*) = Delta_0^2 * N(E_F) / (4 * m*)
        # The ratio D_s_flat / D_s_BCS = g_FS / (N(E_F) * bandwidth)
        # For flat band: bandwidth -> 0, so ratio -> infinity (flat band dominates)

        # B2 bandwidth at fold (from eigenvalue spread)
        B2_bandwidth = np.max(E_8[:4]) - np.min(E_8[:4])

        comparison['E_cond'] = E_cond
        comparison['Delta_0_est'] = Delta_0_est
        comparison['N_EF'] = N_EF
        comparison['D_s_flat'] = D_s
        comparison['B2_bandwidth'] = B2_bandwidth
        comparison['g_FS'] = g_FS_at_fold

        print(f"\n  Peotta-Torma comparison:")
        print(f"    g_FS at fold = {g_FS_at_fold:.6f}")
        print(f"    E_cond = {E_cond:.6f}")
        print(f"    Delta_0 (est) = {Delta_0_est:.6f}")
        print(f"    N(E_F) = {N_EF:.4f}")
        print(f"    B2 bandwidth (from s37) = {B2_bandwidth:.6e}")
        print(f"    D_s (flat-band) = {D_s:.6f}")
        print(f"    Flat-band ratio g_FS * Delta^2 / bandwidth = "
              f"{g_FS_at_fold * Delta_0_est**2 / max(B2_bandwidth, 1e-15):.4f}")
    else:
        print(f"  WARNING: BCS data not found at {bcs_data_path}")

    return comparison


# =============================================================================
# MODULE 5: CONVERGENCE VALIDATION
# =============================================================================

def validate_convergence(tau_test, gens, f_abc, gammas):
    """
    Validate that the finite-difference step dtau gives converged g_FS.

    Compute g_FS at tau_test for dtau = 1e-4, 1e-5, 1e-6, 1e-7 and check
    that the result stabilizes.

    Returns:
        dtau_values: array of step sizes
        g_FS_values: array of g_FS at each step size
        converged_dtau: recommended step size
    """
    dtau_values = [1e-3, 1e-4, 1e-5, 1e-6, 1e-7]
    g_FS_values = []

    # Get eigenstates at tau_test
    Omega_c, _ = compute_omega_at_tau(tau_test, gens, f_abc, gammas)
    evals_c, evecs_c = diagonalize_omega(Omega_c)
    b2_idx, _, _ = identify_B2_indices(evals_c)

    psi_c = evecs_c[:, b2_idx]
    P_B2 = psi_c @ psi_c.conj().T
    Q = np.eye(16, dtype=complex) - P_B2

    for dtau in dtau_values:
        Omega_m, _ = compute_omega_at_tau(tau_test - dtau, gens, f_abc, gammas)
        Omega_p, _ = compute_omega_at_tau(tau_test + dtau, gens, f_abc, gammas)

        _, evecs_m = diagonalize_omega(Omega_m)
        _, evecs_p = diagonalize_omega(Omega_p)

        b2_idx_m, _, _ = identify_B2_indices(np.sort(np.linalg.eigvalsh(1j * Omega_m)))
        b2_idx_p, _, _ = identify_B2_indices(np.sort(np.linalg.eigvalsh(1j * Omega_p)))

        # Gauge-fix
        evecs_m = parallel_transport_gauge(evecs_c, evecs_m, b2_idx_m)
        evecs_p = parallel_transport_gauge(evecs_c, evecs_p, b2_idx_p)

        psi_m = evecs_m[:, b2_idx_m]
        psi_p = evecs_p[:, b2_idx_p]

        dpsi = (psi_p - psi_m) / (2.0 * dtau)
        Q_dpsi = Q @ dpsi
        g_FS_ij = np.real(dpsi.conj().T @ Q_dpsi)
        g_val = np.trace(g_FS_ij) / 4.0
        g_FS_values.append(g_val)

    g_FS_values = np.array(g_FS_values)

    print(f"\n  Convergence test at tau={tau_test:.3f}:")
    for i, (dt, gv) in enumerate(zip(dtau_values, g_FS_values)):
        if i > 0:
            rel_change = abs(gv - g_FS_values[i-1]) / max(abs(g_FS_values[i-1]), 1e-15)
            print(f"    dtau={dt:.0e}: g_FS = {gv:.8f} (rel change: {rel_change:.2e})")
        else:
            print(f"    dtau={dt:.0e}: g_FS = {gv:.8f}")

    # Find converged step: first where relative change < 1e-4
    converged_dtau = dtau_values[-1]
    for i in range(1, len(dtau_values)):
        rel_change = abs(g_FS_values[i] - g_FS_values[i-1]) / max(abs(g_FS_values[i-1]), 1e-15)
        if rel_change < 1e-4:
            converged_dtau = dtau_values[i]
            break

    print(f"    Recommended dtau: {converged_dtau:.0e}")
    return np.array(dtau_values), g_FS_values, converged_dtau


# =============================================================================
# MODULE 6: VISUALIZATION
# =============================================================================

def make_plots(results, results_ext, save_path):
    """
    Generate publication-quality plots of g_FS(tau) and F_Berry(tau).

    Includes both the requested 11-point window and the extended [0.01, 0.50] sweep.
    """
    tau = results['tau']
    g_FS = results['g_FS_scalar']
    F_Berry = results['F_Berry_tensor']
    evals_B2 = results['evals_B2']
    evals_B1 = results['evals_B1']
    evals_B3 = results['evals_B3']

    tau_ext = results_ext['tau']
    g_FS_ext = results_ext['g_FS_scalar']
    evals_B2_ext = results_ext['evals_B2']

    # Berry curvature scalar: Frobenius norm of F_ij
    F_norm = np.array([np.sqrt(np.sum(F_Berry[n]**2)) for n in range(len(tau))])

    # Also compute g_FS eigenvalues at each tau
    g_eigs = np.zeros((len(tau), 4))
    for n in range(len(tau)):
        g_eigs[n] = np.linalg.eigvalsh(results['g_FS_tensor'][n])

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Panel 1: g_FS(tau) — EXTENDED SWEEP with requested points overlaid
    ax = axes[0, 0]
    ax.plot(tau_ext, g_FS_ext, 'b-', linewidth=1.5, alpha=0.6, label='Extended sweep')
    ax.plot(tau, g_FS, 'bo', markersize=7, label='Requested 11 points')
    ax.axvline(x=0.17, color='gray', linestyle='--', alpha=0.5)
    ax.axvline(x=0.21, color='gray', linestyle='--', alpha=0.5)
    ax.axvspan(0.17, 0.21, alpha=0.1, color='green', label='Gate window [0.17, 0.21]')
    peak_idx_ext = np.argmax(g_FS_ext)
    ax.axvline(x=tau_ext[peak_idx_ext], color='red', linestyle='-', alpha=0.7,
               label=f'True peak: tau={tau_ext[peak_idx_ext]:.3f}')
    # Mark van Hove point
    ax.axvline(x=0.19, color='purple', linestyle=':', alpha=0.7,
               label=r'Van Hove ($dE_{B2}/d\tau=0$)')
    ax.set_xlabel(r'$\tau$', fontsize=13)
    ax.set_ylabel(r'$g_{FS}(\tau)$', fontsize=13)
    ax.set_title('Fubini-Study Quantum Metric (B2 quartet)', fontsize=13)
    ax.legend(fontsize=9, loc='lower right')
    ax.grid(True, alpha=0.3)

    # Panel 2: g_FS vs E_B2 (parametric, showing decorrelation)
    ax = axes[0, 1]
    E_B2_mean_ext = np.mean(evals_B2_ext, axis=1)
    ax.plot(E_B2_mean_ext, g_FS_ext, 'b-o', markersize=3, linewidth=1.5)
    # Mark fold point and g_FS peak
    fold_idx = np.argmin(E_B2_mean_ext)
    ax.plot(E_B2_mean_ext[fold_idx], g_FS_ext[fold_idx], 'r^', markersize=12,
            zorder=5, label=f'E_B2 min (tau={tau_ext[fold_idx]:.2f})')
    ax.plot(E_B2_mean_ext[peak_idx_ext], g_FS_ext[peak_idx_ext], 'gs', markersize=12,
            zorder=5, label=f'g_FS peak (tau={tau_ext[peak_idx_ext]:.2f})')
    ax.set_xlabel(r'$\langle E_{B2} \rangle$', fontsize=13)
    ax.set_ylabel(r'$g_{FS}$', fontsize=13)
    ax.set_title(r'$g_{FS}$ vs $E_{B2}$ (parametric in $\tau$)', fontsize=13)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)

    # Panel 3: dE_B2/dtau and g_FS on same axes (normalized)
    ax = axes[1, 0]
    # Compute dE/dtau on extended sweep
    E_B2_mean = np.mean(evals_B2_ext, axis=1)
    dE = np.gradient(E_B2_mean, tau_ext)
    ax2 = ax.twinx()
    l1, = ax.plot(tau_ext, g_FS_ext, 'b-', linewidth=2, label=r'$g_{FS}$')
    l2, = ax2.plot(tau_ext, dE, 'r-', linewidth=2, label=r'$dE_{B2}/d\tau$')
    ax2.axhline(y=0, color='r', linestyle=':', alpha=0.3)
    ax.axvspan(0.17, 0.21, alpha=0.1, color='green')
    ax.set_xlabel(r'$\tau$', fontsize=13)
    ax.set_ylabel(r'$g_{FS}(\tau)$', fontsize=13, color='b')
    ax2.set_ylabel(r'$dE_{B2}/d\tau$', fontsize=13, color='r')
    ax.set_title(r'Quantum metric vs eigenvalue derivative', fontsize=13)
    ax.legend(handles=[l1, l2], fontsize=10, loc='upper left')
    ax.grid(True, alpha=0.3)

    # Panel 4: B2 eigenvalues vs tau with extended range
    ax = axes[1, 1]
    evals_B1_ext = results_ext['evals_B1']
    evals_B3_ext = results_ext['evals_B3']
    ax.plot(tau_ext, evals_B1_ext, 'g--', linewidth=1.5, label='B1')
    for i in range(4):
        lbl = 'B2' if i == 0 else None
        ax.plot(tau_ext, evals_B2_ext[:, i], 'b-', linewidth=1.5, label=lbl, alpha=0.8)
    for i in range(3):
        lbl = 'B3' if i == 0 else None
        ax.plot(tau_ext, evals_B3_ext[:, i], 'r--', linewidth=1.5, label=lbl, alpha=0.8)
    ax.axvspan(0.17, 0.21, alpha=0.1, color='green')
    ax.set_xlabel(r'$\tau$', fontsize=13)
    ax.set_ylabel(r'Eigenvalue $\mu$', fontsize=13)
    ax.set_title(r'$D_K$ eigenvalues (0,0) sector, positive branch', fontsize=13)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(save_path, dpi=150)
    plt.close()
    print(f"\n  Plot saved to {save_path}")


# =============================================================================
# MAIN
# =============================================================================

def main():
    print("=" * 80)
    print("FS-METRIC-39: FUBINI-STUDY QUANTUM METRIC AT THE FOLD")
    print("=" * 80)

    # --- Step 0: Infrastructure ---
    print("\n[0] Building su(3) + Cliff(8) infrastructure...")
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    gammas = build_cliff8()
    cliff_err = validate_clifford(gammas)
    print(f"    Clifford err: {cliff_err:.2e}")

    # --- Step 1: Convergence validation ---
    print("\n[1] Convergence validation at tau=0.19 (near fold)...")
    dtau_vals, g_vals, best_dtau = validate_convergence(
        0.19, gens, f_abc, gammas
    )

    # --- Step 2: Main computation (requested 11 tau points) ---
    tau_values = np.array([0.14, 0.15, 0.16, 0.17, 0.18, 0.19,
                           0.20, 0.21, 0.22, 0.23, 0.24])
    print(f"\n[2] Computing g_FS at {len(tau_values)} tau values with dtau={best_dtau:.0e}...")
    results = compute_fubini_study(tau_values, gens, f_abc, gammas, dtau=best_dtau)

    # --- Step 2b: Extended sweep [0.01, 0.50] to locate true peak ---
    print(f"\n[2b] Extended sweep [0.01, 0.50] to locate g_FS peak...")
    tau_ext = np.linspace(0.01, 0.50, 50)
    results_ext = compute_fubini_study(tau_ext, gens, f_abc, gammas, dtau=best_dtau)

    # --- Step 3: Gate verdict ---
    print(f"\n{'='*80}")
    print("[3] GATE VERDICT: FS-METRIC-39")
    print("=" * 80)

    g_FS = results['g_FS_scalar']
    g_FS_ext = results_ext['g_FS_scalar']

    # Use extended sweep to find true peak
    peak_idx_ext = np.argmax(g_FS_ext)
    tau_peak_ext = tau_ext[peak_idx_ext]
    g_peak_ext = g_FS_ext[peak_idx_ext]

    # Also check requested window
    peak_idx = np.argmax(g_FS)
    tau_peak = tau_values[peak_idx]
    g_peak = g_FS[peak_idx]

    print(f"\n  g_FS values (requested 11 tau points):")
    for i, (t, g) in enumerate(zip(tau_values, g_FS)):
        marker = " <-- LOCAL MAX" if i == peak_idx else ""
        print(f"    tau={t:.2f}: g_FS = {g:.6f}{marker}")

    print(f"\n  Extended sweep peak: g_FS = {g_peak_ext:.6f} at tau = {tau_peak_ext:.4f}")
    print(f"  Within [0.14,0.24]: g_FS ranges [{np.min(g_FS):.6f}, {np.max(g_FS):.6f}]")

    # Check monotonicity within requested window
    diffs = np.diff(g_FS)
    is_monotonic_window = np.all(diffs >= 0) or np.all(diffs <= 0)

    # Check if true peak is within gate window
    if is_monotonic_window and (0.17 <= tau_peak_ext <= 0.21):
        verdict = "PASS"
        reason = f"g_FS peaks at tau={tau_peak_ext:.4f}, within [0.17, 0.21]"
    elif 0.17 <= tau_peak_ext <= 0.21:
        verdict = "PASS"
        reason = f"g_FS peaks at tau={tau_peak_ext:.4f}, within [0.17, 0.21]"
    elif is_monotonic_window:
        verdict = "FAIL"
        reason = (f"g_FS monotonic within [0.14,0.24]. True peak at "
                  f"tau={tau_peak_ext:.4f} (OUTSIDE [0.17,0.21])")
    else:
        verdict = "FAIL"
        reason = f"g_FS peaks at tau={tau_peak_ext:.4f}, OUTSIDE [0.17, 0.21]"

    print(f"\n  VERDICT: {verdict}")
    print(f"  REASON: {reason}")

    # --- Step 4: Peotta-Torma comparison ---
    print(f"\n{'='*80}")
    print("[4] Peotta-Torma comparison...")
    bcs_path = os.path.join(SCRIPT_DIR, 's37_pair_susceptibility.npz')
    pt_comparison = peotta_torma_comparison(g_peak, bcs_path)

    # --- Step 5: Additional diagnostics ---
    print(f"\n{'='*80}")
    print("[5] Additional diagnostics...")

    # Check if g_FS >> 1 at fold (indicating geometric origin of P_exc = 1.000)
    print(f"\n  g_FS at fold: {g_peak:.6f}")
    if g_peak > 1.0:
        print(f"    g_FS >> 1: YES. Eigenstates rotate rapidly at fold.")
        print(f"    This provides geometric explanation for P_exc = 1.000.")
    elif g_peak > 0.1:
        print(f"    g_FS ~ O(1): Moderate eigenstate rotation at fold.")
    else:
        print(f"    g_FS << 1: Eigenstates rotate slowly. No geometric enhancement.")

    # Eigenvalue derivatives: d(E_B2)/d(tau) -- should vanish at fold (van Hove)
    evals_B2 = results['evals_B2']
    dE_dtau = np.zeros(len(tau_values))
    for n in range(1, len(tau_values) - 1):
        dE_dtau[n] = (np.mean(evals_B2[n+1]) - np.mean(evals_B2[n-1])) / (
            tau_values[n+1] - tau_values[n-1])
    dE_dtau[0] = (np.mean(evals_B2[1]) - np.mean(evals_B2[0])) / (
        tau_values[1] - tau_values[0])
    dE_dtau[-1] = (np.mean(evals_B2[-1]) - np.mean(evals_B2[-2])) / (
        tau_values[-1] - tau_values[-2])

    print(f"\n  dE_B2/dtau:")
    for t, de in zip(tau_values, dE_dtau):
        print(f"    tau={t:.2f}: dE/dtau = {de:.6f}")

    min_de_idx = np.argmin(np.abs(dE_dtau[1:-1])) + 1
    print(f"\n  Van Hove point (|dE/dtau| min): tau={tau_values[min_de_idx]:.4f}, "
          f"|dE/dtau|={abs(dE_dtau[min_de_idx]):.6f}")

    # Berry curvature analysis
    F_Berry = results['F_Berry_tensor']
    print(f"\n  Berry curvature analysis (non-Abelian, off-diagonal):")
    for n, t in enumerate(tau_values):
        Fnorm = np.sqrt(np.sum(F_Berry[n]**2))
        Ftrace = np.trace(F_Berry[n])
        print(f"    tau={t:.2f}: ||F||_F = {Fnorm:.6f}, Tr(F) = {Ftrace:.6f}")

    # --- Step 6: Save data ---
    print(f"\n{'='*80}")
    print("[6] Saving data...")

    save_path = os.path.join(SCRIPT_DIR, 's39_fubini_study.npz')
    np.savez(save_path,
             tau=tau_values,
             g_FS_scalar=g_FS,
             g_FS_tensor=results['g_FS_tensor'],
             F_Berry_tensor=results['F_Berry_tensor'],
             evals_B2=results['evals_B2'],
             evals_B1=results['evals_B1'],
             evals_B3=results['evals_B3'],
             all_evals=results['all_evals'],
             dE_dtau=dE_dtau,
             verdict=verdict,
             tau_peak=tau_peak_ext,
             g_FS_peak=g_peak_ext,
             dtau_used=best_dtau,
             convergence_dtau=dtau_vals,
             convergence_gFS=g_vals,
             tau_ext=tau_ext,
             g_FS_ext=g_FS_ext,
             evals_B2_ext=results_ext['evals_B2'],
             **{f'pt_{k}': v for k, v in pt_comparison.items()
                if isinstance(v, (int, float, np.ndarray))},
             )
    print(f"  Saved to {save_path}")

    # --- Step 7: Plot ---
    print(f"\n[7] Generating plot...")
    plot_path = os.path.join(SCRIPT_DIR, 's39_fubini_study.png')
    make_plots(results, results_ext, plot_path)

    # --- Final summary ---
    print(f"\n{'='*80}")
    print("SUMMARY")
    print("=" * 80)
    print(f"  Gate: FS-METRIC-39")
    print(f"  Criterion: g_FS peaks within [0.17, 0.21]")
    print(f"  Result: Peak at tau={tau_peak:.4f}, g_FS={g_peak:.6f}")
    print(f"  Verdict: {verdict}")
    print(f"  Files:")
    print(f"    Script: {os.path.abspath(__file__)}")
    print(f"    Data: {save_path}")
    print(f"    Plot: {plot_path}")
    print("=" * 80)


if __name__ == "__main__":
    main()
