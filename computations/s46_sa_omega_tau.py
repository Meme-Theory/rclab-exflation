"""
SA-ON-OMEGA-TAU-46: 2D Spectral Action Landscape on (tau, phi) Space
======================================================================

Computes S(tau, phi) = Tr f((D_K(tau) + phi * v_0(tau))^2 / Lambda^2)
where v_0(tau) is the lightest tachyonic scalar direction from
OMEGA-CLASSIFY-46, tracked continuously across tau.

The 2D landscape reveals whether the combined (tau, phi) space is:
  - SADDLE: negative curvature in phi, positive in tau (or vice versa)
  - VALLEY: both curvatures negative (trough)
  - RIDGE: both curvatures positive (peak)

Gate: SA-ON-OMEGA-TAU-46
  INFO: Classify the 2D landscape topology (saddle/valley/ridge).
  Pre-registered criterion: report Hessian eigenvalues at fold.

Mathematical framework:
  The spectral action on a finite spectral triple with eigenvalues {lambda_k}
  is S = sum_k f(lambda_k^2 / Lambda^2). For the perturbed operator
  D_phys = D_K(tau) + phi * v_0, the eigenvalues change and S changes.
  This is computed EXACTLY for the finite spectrum (no heat kernel approx).

  The lightest scalar v_0(tau) is the eigenvector of the kinetic mass matrix
  M^2_{ij} = Tr([D, phi_i]^dag [D, phi_j]) with smallest eigenvalue.
  It is tracked across tau by maximizing overlap with the previous tau's
  eigenvector (adiabatic continuation).

Input: s46_omega_classify.npz, s42_hauser_feshbach.npz, canonical_constants.py
Output: s46_sa_omega_tau.{npz,png}

Author: Connes-NCG-Theorist (Session 46 W4-SA)
Date: 2026-03-15
"""

import numpy as np
from numpy.linalg import norm as la_norm, svd, eigh, eigvalsh, eig
import sys
import os
import time
import warnings

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))

from canonical_constants import tau_fold as TAU_FOLD_CANON

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
    get_irrep,
    dirac_operator_on_irrep,
    _irrep_cache,
)

np.set_printoptions(precision=10, linewidth=140, suppress=True)
OUTDIR = os.path.dirname(os.path.abspath(__file__))


# =============================================================================
# SECTION 1: Reuse infrastructure from s46_omega_classify
# =============================================================================

def build_AF_generators():
    """Build 24 generators of A_F = C + H + M_3(C) on 16-dim spinor space."""
    AF_16 = []
    AF_names = []
    AF_factors = []

    def build_bimodule_16(L4, R4):
        """Build left-right bimodule action on 16-dim H_F = C^4 x C^4."""
        return np.kron(L4, R4)

    # C factor (1 generator: identity)
    AF_16.append(build_bimodule_16(np.eye(4, dtype=complex), np.eye(4, dtype=complex)))
    AF_names.append('C_1')
    AF_factors.append('C')

    # H factor (4 real generators: 1, i, j, k via Pauli embedding)
    sigma = [
        np.array([[1, 0], [0, 1]], dtype=complex),
        np.array([[1j, 0], [0, -1j]], dtype=complex),
        np.array([[0, 1], [-1, 0]], dtype=complex),
        np.array([[0, 1j], [1j, 0]], dtype=complex),
    ]
    for si, s in enumerate(sigma):
        L_h = np.zeros((4, 4), dtype=complex)
        L_h[:2, :2] = s
        if si == 0:
            L_h[2:, 2:] = s
        else:
            L_h[2:, 2:] = s.conj()
        AF_16.append(build_bimodule_16(L_h, np.eye(4, dtype=complex)))
        AF_names.append(f'H_{si}')
        AF_factors.append('H')

    # M_3(C) factor (18 generators: Re and Im parts of E_{ab})
    for a in range(3):
        for b in range(3):
            for part, val in [('Re', 1.0), ('Im', 1j)]:
                m_elem = np.zeros((3, 3), dtype=complex)
                m_elem[a, b] = val
                R_m = np.eye(4, dtype=complex)
                R_m[1:, 1:] = m_elem.conj().T
                AF_16.append(build_bimodule_16(np.eye(4), R_m))
                AF_names.append(f'M3_E{a}{b}_{part}')
                AF_factors.append('M3')

    return AF_16, AF_names, AF_factors


def build_DK(tau, gens, f_abc, B_ab, gammas, p, q):
    """Build D_K on rep (p,q) at deformation tau."""
    _irrep_cache.clear()
    rho, dim_rho = get_irrep(p, q, gens, f_abc)
    g_s = jensen_metric(B_ab, tau)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    Omega = spinor_connection_offset(Gamma, gammas)
    D_K = dirac_operator_on_irrep(rho, E, gammas, Omega)
    return D_K, dim_rho


def compute_omega1_odd_basis(D_mat, AF_16_list, dim_rho, gammas):
    """
    Compute the odd (scalar) part of Omega^1_D(A_F) combined module.
    Returns the orthonormal basis for scalar inner fluctuations.
    """
    n_gen = len(AF_16_list)
    N = D_mat.shape[0]
    I_rho = np.eye(dim_rho, dtype=complex) if dim_rho > 1 else None

    linear_vecs = []
    quadratic_vecs = []

    for j in range(n_gen):
        b_full = np.kron(I_rho, AF_16_list[j]) if dim_rho > 1 else AF_16_list[j]
        comm_Db = D_mat @ b_full - b_full @ D_mat
        for i in range(n_gen):
            a_full = np.kron(I_rho, AF_16_list[i]) if dim_rho > 1 else AF_16_list[i]
            linear_vecs.append((a_full @ comm_Db).ravel())
            comm_Da = D_mat @ a_full - a_full @ D_mat
            quadratic_vecs.append((comm_Da @ comm_Db).ravel())

    combined_mat = np.vstack([np.array(linear_vecs), np.array(quadratic_vecs)])

    # SVD to extract basis
    _, S_c, Vh_c = svd(combined_mat, full_matrices=False)
    cutoff = S_c[0] * 1e-10
    dim_comb = int(np.sum(S_c > cutoff))
    comb_basis = Vh_c[:dim_comb]

    # Grading decomposition: gamma_9 = prod(gammas)
    gamma_9 = np.eye(16, dtype=complex)
    for g in gammas:
        gamma_9 = gamma_9 @ g
    gamma_full = np.kron(np.eye(dim_rho), gamma_9)

    # Project onto odd (scalar) subspace
    odd_vecs = []
    for k in range(dim_comb):
        omega = comb_basis[k].reshape(N, N)
        graded = gamma_full @ omega @ gamma_full
        odd_part = 0.5 * (omega - graded)
        if la_norm(odd_part, 'fro') > 1e-12:
            odd_vecs.append(odd_part.ravel())

    if len(odd_vecs) == 0:
        return np.zeros((0, N * N), dtype=complex), 0

    mat = np.array(odd_vecs)
    _, S_o, Vh_o = svd(mat, full_matrices=False)
    cutoff_o = S_o[0] * 1e-10
    dim_odd = int(np.sum(S_o > cutoff_o))
    return Vh_o[:dim_odd], dim_odd


def compute_lightest_scalar(odd_basis, D_mat, N):
    """
    Compute the kinetic mass matrix M^2 and return the lightest eigenvector
    as an NxN self-adjoint matrix (normalized).
    """
    n_scalar = odd_basis.shape[0]
    if n_scalar == 0:
        return None, None, np.array([])

    # Build self-adjoint operators and commutators
    phis = []
    comms = []
    for k in range(n_scalar):
        phi_k = odd_basis[k].reshape(N, N)
        phi_k_sa = (phi_k + phi_k.conj().T) / np.sqrt(2.0)
        norm_k = np.sqrt(np.real(np.trace(phi_k_sa.conj().T @ phi_k_sa)))
        if norm_k > 1e-15:
            phi_k_sa /= norm_k
        phis.append(phi_k_sa)
        comms.append(D_mat @ phi_k_sa - phi_k_sa @ D_mat)

    # Kinetic mass matrix (Gram matrix, PSD)
    M2 = np.zeros((n_scalar, n_scalar))
    for i in range(n_scalar):
        for j in range(i, n_scalar):
            val = np.real(np.trace(comms[i].conj().T @ comms[j]))
            M2[i, j] = val
            M2[j, i] = val

    evals, evecs = eigh(M2)

    # Lightest eigenvector in the operator basis
    lightest_coeffs = evecs[:, 0]  # smallest eigenvalue
    lightest_op = np.zeros((N, N), dtype=complex)
    for k in range(n_scalar):
        lightest_op += lightest_coeffs[k] * phis[k]

    # Normalize
    norm = np.sqrt(np.real(np.trace(lightest_op.conj().T @ lightest_op)))
    if norm > 1e-15:
        lightest_op /= norm

    return lightest_op, evals[0], evals


def track_lightest_scalar(v_prev, odd_basis, D_mat, N):
    """
    Compute lightest scalar at new tau, tracked by overlap with v_prev.
    Returns the eigenvector with maximum overlap to v_prev (adiabatic continuation).
    """
    n_scalar = odd_basis.shape[0]
    if n_scalar == 0 or v_prev is None:
        return compute_lightest_scalar(odd_basis, D_mat, N)

    phis = []
    comms = []
    for k in range(n_scalar):
        phi_k = odd_basis[k].reshape(N, N)
        phi_k_sa = (phi_k + phi_k.conj().T) / np.sqrt(2.0)
        norm_k = np.sqrt(np.real(np.trace(phi_k_sa.conj().T @ phi_k_sa)))
        if norm_k > 1e-15:
            phi_k_sa /= norm_k
        phis.append(phi_k_sa)
        comms.append(D_mat @ phi_k_sa - phi_k_sa @ D_mat)

    # Kinetic mass matrix
    M2 = np.zeros((n_scalar, n_scalar))
    for i in range(n_scalar):
        for j in range(i, n_scalar):
            val = np.real(np.trace(comms[i].conj().T @ comms[j]))
            M2[i, j] = val
            M2[j, i] = val

    evals, evecs = eigh(M2)

    # Compute overlaps of all eigenvectors with v_prev
    best_idx = 0
    best_overlap = 0.0
    for idx in range(min(5, n_scalar)):  # check lightest 5
        coeffs = evecs[:, idx]
        op = np.zeros((N, N), dtype=complex)
        for k in range(n_scalar):
            op += coeffs[k] * phis[k]
        norm = np.sqrt(np.real(np.trace(op.conj().T @ op)))
        if norm > 1e-15:
            op /= norm
        overlap = np.abs(np.trace(op.conj().T @ v_prev))
        if overlap > best_overlap:
            best_overlap = overlap
            best_idx = idx

    # Use the best-tracked eigenvector
    tracked_coeffs = evecs[:, best_idx]
    tracked_op = np.zeros((N, N), dtype=complex)
    for k in range(n_scalar):
        tracked_op += tracked_coeffs[k] * phis[k]
    norm = np.sqrt(np.real(np.trace(tracked_op.conj().T @ tracked_op)))
    if norm > 1e-15:
        tracked_op /= norm

    # Ensure consistent sign (avoid pi-flips)
    sign = np.real(np.trace(tracked_op.conj().T @ v_prev))
    if sign < 0:
        tracked_op = -tracked_op

    return tracked_op, evals[best_idx], evals


def spectral_action_exact(D_mat, f_func, Lambda):
    """
    Compute S = Tr f(D^2 / Lambda^2) exactly for a finite-dimensional D_mat.
    This is the EXACT spectral action, no heat kernel approximation.
    """
    evals = eigvalsh(D_mat)
    x = evals**2 / Lambda**2
    return np.sum(f_func(x))


# =============================================================================
# MAIN COMPUTATION
# =============================================================================

if __name__ == '__main__':
    t_total_start = time.time()

    print("=" * 78)
    print("SA-ON-OMEGA-TAU-46: 2D Spectral Action Landscape")
    print("=" * 78)
    print()

    # Setup infrastructure
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    B_ab = compute_killing_form(f_abc)
    gammas = build_cliff8()

    AF_16, AF_names, AF_factors = build_AF_generators()
    n_gen = len(AF_16)

    p_sector, q_sector = 1, 0

    # Cutoff function: exponential (canonical choice)
    f_exp = lambda x: np.exp(-x)

    # =========================================================================
    # STEP 1: Tau grid and phi grid
    # =========================================================================
    print("STEP 1: Grid setup")
    print("-" * 40)

    n_tau = 24
    n_phi = 41
    tau_grid = np.linspace(0.0, 0.5, n_tau)
    phi_grid = np.linspace(-1.0, 1.0, n_phi)

    print(f"  tau grid: {n_tau} points in [0, 0.5]")
    print(f"  phi grid: {n_phi} points in [-1, 1]")
    print(f"  Total evaluations: {n_tau * n_phi}")
    print()

    # =========================================================================
    # STEP 2: Build lightest scalar at each tau (adiabatic tracking)
    # =========================================================================
    print("STEP 2: Adiabatic tracking of lightest scalar direction v_0(tau)")
    print("-" * 40)

    v0_list = [None] * n_tau          # lightest scalar operator at each tau
    m2_lightest = np.zeros(n_tau)     # kinetic mass eigenvalue
    D_K_list = [None] * n_tau         # D_K matrices
    Lambda_list = np.zeros(n_tau)     # Lambda at each tau
    overlaps = np.zeros(n_tau)        # overlap with previous v_0

    for ti, tau in enumerate(tau_grid):
        t0 = time.time()
        D_K, dim_rho = build_DK(tau, gens, f_abc, B_ab, gammas, p_sector, q_sector)
        D_K_list[ti] = D_K
        N = D_K.shape[0]

        # Lambda = 1.5 * max |eigenvalue| (same convention as s46_omega_verify)
        evals_abs_max = np.max(np.abs(eigvalsh(D_K)))
        Lambda_list[ti] = evals_abs_max * 1.5

        # Compute odd basis
        odd_basis, dim_odd = compute_omega1_odd_basis(D_K, AF_16, dim_rho, gammas)

        if ti == 0:
            v0, m2_val, m2_all = compute_lightest_scalar(odd_basis, D_K, N)
        else:
            v0, m2_val, m2_all = track_lightest_scalar(v0_list[ti - 1], odd_basis, D_K, N)

        v0_list[ti] = v0
        m2_lightest[ti] = m2_val if m2_val is not None else np.nan

        # Compute overlap with previous
        if ti > 0 and v0_list[ti - 1] is not None and v0 is not None:
            overlaps[ti] = np.abs(np.trace(v0.conj().T @ v0_list[ti - 1]))
        else:
            overlaps[ti] = 1.0

        dt = time.time() - t0
        print(f"  tau={tau:.3f}: m^2_lightest={m2_lightest[ti]:+.6f}, "
              f"overlap={overlaps[ti]:.4f}, dim_odd={dim_odd}, "
              f"Lambda={Lambda_list[ti]:.3f}, dt={dt:.1f}s")

    # Check adiabatic continuity
    min_overlap = np.min(overlaps[1:])
    print(f"\n  Adiabatic tracking: min overlap = {min_overlap:.4f}")
    if min_overlap < 0.5:
        print("  WARNING: Level crossing detected. Tracking may be unreliable.")
    print()

    # =========================================================================
    # STEP 3: Compute S(tau, phi) on the 2D grid
    # =========================================================================
    print("STEP 3: Computing S(tau, phi) on 2D grid")
    print("-" * 40)

    S_landscape = np.zeros((n_tau, n_phi))

    for ti in range(n_tau):
        t0 = time.time()
        D_K = D_K_list[ti]
        v0 = v0_list[ti]
        Lambda = Lambda_list[ti]

        if v0 is None:
            S_landscape[ti, :] = np.nan
            print(f"  tau={tau_grid[ti]:.3f}: SKIPPED (no scalar direction)")
            continue

        for pi, phi_val in enumerate(phi_grid):
            # D_phys = D_K + phi * v_0
            D_phys = D_K + phi_val * v0
            S_landscape[ti, pi] = spectral_action_exact(D_phys, f_exp, Lambda)

        dt = time.time() - t0
        print(f"  tau={tau_grid[ti]:.3f}: S range = [{S_landscape[ti,:].min():.4f}, "
              f"{S_landscape[ti,:].max():.4f}], dt={dt:.1f}s")

    print()

    # =========================================================================
    # STEP 4: Compute Hessian at each tau (at phi=0)
    # =========================================================================
    print("STEP 4: Hessian of S(tau, phi) at phi=0")
    print("-" * 40)

    # d^2S/dphi^2 at phi=0: numerical second derivative
    dphi = phi_grid[1] - phi_grid[0]
    phi0_idx = n_phi // 2  # phi=0 index
    assert abs(phi_grid[phi0_idx]) < 1e-10, f"phi_grid center is {phi_grid[phi0_idx]}, not 0"

    d2S_dphi2 = np.zeros(n_tau)
    dS_dphi = np.zeros(n_tau)
    for ti in range(n_tau):
        # Second derivative in phi
        d2S_dphi2[ti] = (S_landscape[ti, phi0_idx + 1]
                         - 2 * S_landscape[ti, phi0_idx]
                         + S_landscape[ti, phi0_idx - 1]) / dphi**2
        # First derivative in phi (should be ~0 by symmetry)
        dS_dphi[ti] = (S_landscape[ti, phi0_idx + 1]
                        - S_landscape[ti, phi0_idx - 1]) / (2 * dphi)

    # d^2S/dtau^2 at phi=0: numerical second derivative
    dtau = tau_grid[1] - tau_grid[0]
    d2S_dtau2 = np.zeros(n_tau)
    dS_dtau = np.zeros(n_tau)
    for ti in range(1, n_tau - 1):
        d2S_dtau2[ti] = (S_landscape[ti + 1, phi0_idx]
                         - 2 * S_landscape[ti, phi0_idx]
                         + S_landscape[ti - 1, phi0_idx]) / dtau**2
        dS_dtau[ti] = (S_landscape[ti + 1, phi0_idx]
                        - S_landscape[ti - 1, phi0_idx]) / (2 * dtau)
    # Boundary: forward/backward difference
    d2S_dtau2[0] = (S_landscape[2, phi0_idx]
                     - 2 * S_landscape[1, phi0_idx]
                     + S_landscape[0, phi0_idx]) / dtau**2
    d2S_dtau2[-1] = (S_landscape[-1, phi0_idx]
                      - 2 * S_landscape[-2, phi0_idx]
                      + S_landscape[-3, phi0_idx]) / dtau**2
    dS_dtau[0] = (S_landscape[1, phi0_idx] - S_landscape[0, phi0_idx]) / dtau
    dS_dtau[-1] = (S_landscape[-1, phi0_idx] - S_landscape[-2, phi0_idx]) / dtau

    # Mixed derivative d^2S/dtau dphi
    d2S_dtaudphi = np.zeros(n_tau)
    for ti in range(1, n_tau - 1):
        d2S_dtaudphi[ti] = (
            S_landscape[ti + 1, phi0_idx + 1] - S_landscape[ti + 1, phi0_idx - 1]
            - S_landscape[ti - 1, phi0_idx + 1] + S_landscape[ti - 1, phi0_idx - 1]
        ) / (4 * dtau * dphi)

    print(f"  {'tau':>6s}  {'d2S/dphi2':>12s}  {'d2S/dtau2':>12s}  {'dS/dtau':>12s}  "
          f"{'d2S/dtaudphi':>14s}  {'type':>8s}")
    for ti in range(n_tau):
        h_phi = d2S_dphi2[ti]
        h_tau = d2S_dtau2[ti]
        if h_phi < 0 and h_tau > 0:
            htype = "SADDLE"
        elif h_phi > 0 and h_tau < 0:
            htype = "SADDLE"
        elif h_phi < 0 and h_tau < 0:
            htype = "VALLEY"
        elif h_phi > 0 and h_tau > 0:
            htype = "RIDGE"
        else:
            htype = "FLAT"
        print(f"  {tau_grid[ti]:6.3f}  {h_phi:+12.4f}  {h_tau:+12.4f}  {dS_dtau[ti]:+12.4f}  "
              f"{d2S_dtaudphi[ti]:+14.4f}  {htype:>8s}")

    print()

    # =========================================================================
    # STEP 5: 2D Hessian eigenvalues at the fold
    # =========================================================================
    print("STEP 5: 2D Hessian eigenvalues at fold (tau ~ 0.19)")
    print("-" * 40)

    # Find fold index
    fold_idx = np.argmin(np.abs(tau_grid - TAU_FOLD_CANON))
    tau_at_fold = tau_grid[fold_idx]
    print(f"  Fold at tau_grid[{fold_idx}] = {tau_at_fold:.3f}")

    # 2D Hessian matrix at fold
    H_2d_fold = np.array([
        [d2S_dtau2[fold_idx],    d2S_dtaudphi[fold_idx]],
        [d2S_dtaudphi[fold_idx], d2S_dphi2[fold_idx]]
    ])
    h_evals = np.linalg.eigvalsh(H_2d_fold)
    det_H = np.linalg.det(H_2d_fold)
    tr_H = np.trace(H_2d_fold)

    print(f"  H_2d = [[{H_2d_fold[0,0]:+.4f}, {H_2d_fold[0,1]:+.4f}],")
    print(f"          [{H_2d_fold[1,0]:+.4f}, {H_2d_fold[1,1]:+.4f}]]")
    print(f"  Eigenvalues: {h_evals[0]:+.4f}, {h_evals[1]:+.4f}")
    print(f"  Determinant: {det_H:+.4f}")
    print(f"  Trace: {tr_H:+.4f}")

    if h_evals[0] * h_evals[1] < 0:
        landscape_type_fold = "SADDLE"
    elif h_evals[0] < 0 and h_evals[1] < 0:
        landscape_type_fold = "TROUGH"
    elif h_evals[0] > 0 and h_evals[1] > 0:
        landscape_type_fold = "RIDGE"
    else:
        landscape_type_fold = "DEGENERATE"

    print(f"  Landscape type at fold: {landscape_type_fold}")
    print()

    # =========================================================================
    # STEP 6: Gradient flow trajectory
    # =========================================================================
    print("STEP 6: Gradient flow trajectory from phi=0")
    print("-" * 40)

    # The gradient of S in the (tau, phi) plane.
    # Gradient descent: d(tau,phi)/dt = -grad S
    # We trace the gradient flow starting from (tau_fold, 0).

    # Compute full gradient field
    grad_tau = np.zeros((n_tau, n_phi))
    grad_phi = np.zeros((n_tau, n_phi))

    for ti in range(1, n_tau - 1):
        for pi in range(1, n_phi - 1):
            grad_tau[ti, pi] = (S_landscape[ti + 1, pi] - S_landscape[ti - 1, pi]) / (2 * dtau)
            grad_phi[ti, pi] = (S_landscape[ti, pi + 1] - S_landscape[ti, pi - 1]) / (2 * dphi)

    # Compute gradient flow from (tau_fold, phi=0) using Euler integration
    n_flow = 200
    flow_dt = 0.001  # step size (dimensionless)
    flow_tau = np.zeros(n_flow)
    flow_phi = np.zeros(n_flow)
    flow_S = np.zeros(n_flow)
    flow_tau[0] = tau_at_fold
    flow_phi[0] = 0.0
    flow_S[0] = S_landscape[fold_idx, phi0_idx]

    for step in range(1, n_flow):
        # Bilinear interpolation of gradient
        tau_now = flow_tau[step - 1]
        phi_now = flow_phi[step - 1]

        # Clip to grid bounds
        if (tau_now < tau_grid[1] or tau_now > tau_grid[-2] or
                phi_now < phi_grid[1] or phi_now > phi_grid[-2]):
            flow_tau[step:] = flow_tau[step - 1]
            flow_phi[step:] = flow_phi[step - 1]
            flow_S[step:] = flow_S[step - 1]
            break

        # Find grid cell
        ti_f = (tau_now - tau_grid[0]) / dtau
        pi_f = (phi_now - phi_grid[0]) / dphi
        ti0 = int(np.floor(ti_f))
        pi0 = int(np.floor(pi_f))
        ti0 = max(1, min(ti0, n_tau - 3))
        pi0 = max(1, min(pi0, n_phi - 3))
        ft = ti_f - ti0
        fp = pi_f - pi0

        # Bilinear interpolation
        g_tau = ((1 - ft) * (1 - fp) * grad_tau[ti0, pi0]
                 + ft * (1 - fp) * grad_tau[ti0 + 1, pi0]
                 + (1 - ft) * fp * grad_tau[ti0, pi0 + 1]
                 + ft * fp * grad_tau[ti0 + 1, pi0 + 1])
        g_phi = ((1 - ft) * (1 - fp) * grad_phi[ti0, pi0]
                 + ft * (1 - fp) * grad_phi[ti0 + 1, pi0]
                 + (1 - ft) * fp * grad_phi[ti0, pi0 + 1]
                 + ft * fp * grad_phi[ti0 + 1, pi0 + 1])

        # Gradient descent
        flow_tau[step] = tau_now - flow_dt * g_tau
        flow_phi[step] = phi_now - flow_dt * g_phi

        # Interpolate S
        s_tau = ((1 - ft) * (1 - fp) * S_landscape[ti0, pi0]
                 + ft * (1 - fp) * S_landscape[ti0 + 1, pi0]
                 + (1 - ft) * fp * S_landscape[ti0, pi0 + 1]
                 + ft * fp * S_landscape[ti0 + 1, pi0 + 1])
        flow_S[step] = s_tau

    # Trim flow to valid region
    valid_mask = (flow_tau > tau_grid[0]) & (flow_tau < tau_grid[-1])
    n_valid = np.sum(valid_mask)

    print(f"  Flow from (tau={tau_at_fold:.3f}, phi=0):")
    print(f"  Valid steps: {n_valid}/{n_flow}")
    if n_valid > 1:
        delta_tau_flow = flow_tau[n_valid - 1] - flow_tau[0]
        delta_phi_flow = flow_phi[n_valid - 1] - flow_phi[0]
        print(f"  Endpoint: (tau={flow_tau[n_valid-1]:.4f}, phi={flow_phi[n_valid-1]:.4f})")
        print(f"  Delta tau: {delta_tau_flow:+.4f}")
        print(f"  Delta phi: {delta_phi_flow:+.4f}")
        print(f"  Flow direction: {'tau-increasing' if delta_tau_flow > 0 else 'tau-decreasing'}, "
              f"{'phi-increasing' if abs(delta_phi_flow) > 0.01 else 'phi-stable'}")
        flow_angle = np.arctan2(delta_phi_flow, delta_tau_flow) * 180 / np.pi
        print(f"  Flow angle: {flow_angle:.1f} degrees from tau axis")
    print()

    # =========================================================================
    # STEP 7: Spectral action Hessian (divided-difference, cutoff-dependent)
    # =========================================================================
    print("STEP 7: SA Hessian (divided-difference) at fold for lightest scalar")
    print("-" * 40)

    D_fold = D_K_list[fold_idx]
    v0_fold = v0_list[fold_idx]
    Lambda_fold = Lambda_list[fold_idx]

    evals_fold_sorted, evecs_fold = eigh(D_fold)

    cutoffs = [
        ("exp(-x)", lambda x: np.exp(-x)),
        ("(1-x)^2 theta", lambda x: np.where(x < 1, (1 - x)**2, 0.0)),
        ("1/(1+x)", lambda x: 1.0 / (1 + x)),
    ]

    SA_hessian_phi = {}
    for f_name, f_func in cutoffs:
        # phi -> v_0 direction: compute d^2S/dphi^2 at phi=0 via divided differences
        x = evals_fold_sorted**2 / Lambda_fold**2
        f_vals = f_func(x)

        # v_0 in eigenbasis
        v0_eig = evecs_fold.conj().T @ v0_fold @ evecs_fold
        N_loc = len(evals_fold_sorted)

        # Anticommutator {D, v_0}_{km} = (lk + lm) * (v_0)_{km}
        # Divided difference: (f(xk) - f(xm)) / (xk - xm)
        H_anti = 0.0
        for k in range(N_loc):
            for m in range(N_loc):
                anti_km = (evals_fold_sorted[k] + evals_fold_sorted[m]) * v0_eig[k, m] / Lambda_fold**2
                if abs(x[k] - x[m]) > 1e-15:
                    f_div = (f_vals[k] - f_vals[m]) / (x[k] - x[m])
                else:
                    dx = 1e-8
                    f_div = (f_func(x[k] + dx) - f_func(x[k])) / dx
                H_anti += f_div * np.abs(anti_km)**2

        # phi^2 term
        v0_sq = v0_fold @ v0_fold
        v0_sq_eig = evecs_fold.conj().T @ v0_sq @ evecs_fold
        H_phi2 = 0.0
        for k in range(N_loc):
            dx = 1e-8
            fp = (f_func(x[k] + dx) - f_func(x[k])) / dx
            H_phi2 += fp * np.real(v0_sq_eig[k, k]) / Lambda_fold**2

        H_total = np.real(H_anti + H_phi2)
        SA_hessian_phi[f_name] = H_total
        print(f"  {f_name:20s}: H_phi = {H_total:+12.6e}  "
              f"(anti={np.real(H_anti):+10.4e}, phi2={np.real(H_phi2):+10.4e})")

    print()

    # =========================================================================
    # STEP 8: Curvature ratio analysis
    # =========================================================================
    print("STEP 8: Curvature ratio analysis")
    print("-" * 40)

    # Ratio |d^2S/dphi^2| / |d^2S/dtau^2| at fold
    ratio_curv = abs(d2S_dphi2[fold_idx]) / abs(d2S_dtau2[fold_idx]) if abs(d2S_dtau2[fold_idx]) > 1e-15 else np.inf
    print(f"  At fold (tau={tau_at_fold:.3f}):")
    print(f"    |d^2S/dphi^2| = {abs(d2S_dphi2[fold_idx]):.4f}")
    print(f"    |d^2S/dtau^2| = {abs(d2S_dtau2[fold_idx]):.4f}")
    print(f"    Ratio |H_phi/H_tau| = {ratio_curv:.4f}")
    print(f"    Kinetic mass m^2_lightest = {m2_lightest[fold_idx]:+.6f}")
    print(f"    SA Hessian (exp) = {SA_hessian_phi.get('exp(-x)', np.nan):+.6e}")
    print()

    # =========================================================================
    # STEP 9: Spectral action along phi at selected tau values
    # =========================================================================
    print("STEP 9: S(phi) profiles at selected tau values")
    print("-" * 40)

    for tau_val in [0.0, 0.10, 0.19, 0.30, 0.50]:
        ti = np.argmin(np.abs(tau_grid - tau_val))
        S_phi = S_landscape[ti, :]
        S_center = S_phi[phi0_idx]
        S_edge = S_phi[-1]
        delta_S = S_edge - S_center
        print(f"  tau={tau_grid[ti]:.3f}: S(0)={S_center:.4f}, S(1)={S_edge:.4f}, "
              f"Delta S={delta_S:+.4f}, concavity={'DOWN' if d2S_dphi2[ti] < 0 else 'UP'}")

    print()

    # =========================================================================
    # VERDICT
    # =========================================================================
    print("=" * 78)
    print("SA-ON-OMEGA-TAU-46 VERDICT")
    print("=" * 78)
    print()

    # Count landscape types across tau
    n_saddle = 0
    n_trough = 0
    n_ridge = 0
    for ti in range(n_tau):
        h_phi = d2S_dphi2[ti]
        h_tau = d2S_dtau2[ti]
        if h_phi < 0 and h_tau > 0:
            n_saddle += 1
        elif h_phi > 0 and h_tau < 0:
            n_saddle += 1
        elif h_phi < 0 and h_tau < 0:
            n_trough += 1
        elif h_phi > 0 and h_tau > 0:
            n_ridge += 1

    print(f"  Landscape type distribution across tau:")
    print(f"    SADDLE: {n_saddle}/{n_tau}")
    print(f"    TROUGH: {n_trough}/{n_tau}")
    print(f"    RIDGE:  {n_ridge}/{n_tau}")
    print()

    print(f"  At fold (tau={tau_at_fold:.3f}):")
    print(f"    Landscape: {landscape_type_fold}")
    print(f"    H_tau = {d2S_dtau2[fold_idx]:+.4f}")
    print(f"    H_phi = {d2S_dphi2[fold_idx]:+.4f}")
    print(f"    H_mixed = {d2S_dtaudphi[fold_idx]:+.4f}")
    print(f"    2D eigenvalues: {h_evals[0]:+.4f}, {h_evals[1]:+.4f}")
    print()

    gate_verdict = "INFO"
    if landscape_type_fold == "SADDLE":
        gate_detail = (
            f"2D landscape is a SADDLE at the fold. "
            f"d^2S/dtau^2 = {d2S_dtau2[fold_idx]:+.4f} (tau direction), "
            f"d^2S/dphi^2 = {d2S_dphi2[fold_idx]:+.4f} (scalar direction). "
            f"Opposite signs: tau wants to increase, scalar wants to roll. "
            f"The combined (tau, phi) trajectory is a saddle-crossing transit."
        )
    elif landscape_type_fold == "TROUGH":
        gate_detail = (
            f"2D landscape is a TROUGH at the fold. "
            f"Both directions have negative curvature. "
            f"The spectral action drives motion in both tau and phi simultaneously."
        )
    elif landscape_type_fold == "RIDGE":
        gate_detail = (
            f"2D landscape is a RIDGE at the fold. "
            f"Both directions have positive curvature. "
            f"Unexpected: spectral action disfavors motion in both directions."
        )
    else:
        gate_detail = f"2D landscape is {landscape_type_fold} at the fold."

    print(f"  Gate: SA-ON-OMEGA-TAU-46 = {gate_verdict}")
    print(f"  {gate_detail}")
    print()

    # =========================================================================
    # SAVE RESULTS
    # =========================================================================
    t_total = time.time() - t_total_start

    outfile = os.path.join(OUTDIR, "s46_sa_omega_tau.npz")
    np.savez(outfile,
             # Grid
             tau_grid=tau_grid,
             phi_grid=phi_grid,
             # 2D landscape
             S_landscape=S_landscape,
             # Derivatives at phi=0
             d2S_dphi2=d2S_dphi2,
             d2S_dtau2=d2S_dtau2,
             dS_dtau=dS_dtau,
             dS_dphi=dS_dphi,
             d2S_dtaudphi=d2S_dtaudphi,
             # Per-tau tracking
             m2_lightest=m2_lightest,
             Lambda_arr=Lambda_list,
             overlaps=overlaps,
             # 2D Hessian at fold
             H_2d_fold=H_2d_fold,
             H_2d_eigenvalues=h_evals,
             landscape_type_fold=np.array([landscape_type_fold]),
             fold_idx=fold_idx,
             tau_at_fold=tau_at_fold,
             # Gradient flow
             flow_tau=flow_tau[:n_valid],
             flow_phi=flow_phi[:n_valid],
             flow_S=flow_S[:n_valid],
             # SA Hessian (divided-difference)
             SA_hessian_exp=SA_hessian_phi.get('exp(-x)', np.nan),
             # Metadata
             n_tau=n_tau,
             n_phi=n_phi,
             gate_verdict=np.array([gate_verdict]),
             runtime=t_total,
             )

    print(f"  Data saved to: {outfile}")
    print(f"  Total runtime: {t_total:.1f}s")
    print()

    # =========================================================================
    # PLOT
    # =========================================================================
    print("Generating plot...")
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib import cm

    fig = plt.figure(figsize=(18, 14))

    # Panel 1: 2D contour of S(tau, phi)
    ax1 = fig.add_subplot(2, 3, 1)
    TAU, PHI = np.meshgrid(tau_grid, phi_grid, indexing='ij')
    S_rel = S_landscape - S_landscape[:, phi0_idx:phi0_idx+1]  # relative to phi=0
    levels = np.linspace(S_rel.min(), S_rel.max(), 30)
    cf = ax1.contourf(TAU, PHI, S_rel, levels=levels, cmap='RdBu_r')
    plt.colorbar(cf, ax=ax1, label='S(tau,phi) - S(tau,0)')
    # Overlay gradient flow
    ax1.plot(flow_tau[:n_valid], flow_phi[:n_valid], 'k-', lw=2, label='Gradient flow')
    ax1.plot(tau_at_fold, 0, 'r*', ms=15, zorder=5, label=f'Fold ({tau_at_fold:.2f})')
    ax1.set_xlabel('tau')
    ax1.set_ylabel('phi (lightest scalar)')
    ax1.set_title('S(tau,phi) - S(tau,0)')
    ax1.legend(loc='upper right', fontsize=8)

    # Panel 2: S(phi) profiles at selected tau
    ax2 = fig.add_subplot(2, 3, 2)
    tau_show = [0.0, 0.10, 0.19, 0.30, 0.50]
    colors = plt.cm.viridis(np.linspace(0, 1, len(tau_show)))
    for k, tau_val in enumerate(tau_show):
        ti = np.argmin(np.abs(tau_grid - tau_val))
        S_phi_rel = S_landscape[ti, :] - S_landscape[ti, phi0_idx]
        ax2.plot(phi_grid, S_phi_rel, color=colors[k], lw=2,
                 label=f'tau={tau_grid[ti]:.2f}')
    ax2.set_xlabel('phi')
    ax2.set_ylabel('S(phi) - S(0)')
    ax2.set_title('S(phi) cross-sections')
    ax2.legend(fontsize=8)
    ax2.axhline(0, color='gray', ls='--', lw=0.5)

    # Panel 3: Hessian components vs tau
    ax3 = fig.add_subplot(2, 3, 3)
    ax3.plot(tau_grid, d2S_dphi2, 'b-', lw=2, label=r'$\partial^2 S/\partial\phi^2$')
    ax3.plot(tau_grid, d2S_dtau2, 'r-', lw=2, label=r'$\partial^2 S/\partial\tau^2$')
    ax3.plot(tau_grid, d2S_dtaudphi, 'g--', lw=1.5, label=r'$\partial^2 S/\partial\tau\partial\phi$')
    ax3.axhline(0, color='gray', ls='--', lw=0.5)
    ax3.axvline(tau_at_fold, color='orange', ls=':', lw=1, label='Fold')
    ax3.set_xlabel('tau')
    ax3.set_ylabel('Hessian component')
    ax3.set_title('2D Hessian at phi=0')
    ax3.legend(fontsize=8)

    # Panel 4: S(tau, phi=0) and dS/dtau
    ax4 = fig.add_subplot(2, 3, 4)
    ax4.plot(tau_grid, S_landscape[:, phi0_idx], 'k-', lw=2, label='S(tau, 0)')
    ax4.axvline(tau_at_fold, color='orange', ls=':', lw=1, label='Fold')
    ax4.set_xlabel('tau')
    ax4.set_ylabel('S(tau, phi=0)')
    ax4.set_title('Spectral action along tau (phi=0)')
    ax4.legend(fontsize=8)

    # Panel 5: Kinetic mass m^2_lightest vs tau
    ax5 = fig.add_subplot(2, 3, 5)
    ax5.plot(tau_grid, m2_lightest, 'b-o', lw=2, ms=4)
    ax5.axvline(tau_at_fold, color='orange', ls=':', lw=1, label='Fold')
    ax5.set_xlabel('tau')
    ax5.set_ylabel(r'$m^2_{\rm lightest}$ (kinetic)')
    ax5.set_title('Lightest kinetic mass vs tau')
    ax5.legend(fontsize=8)

    # Panel 6: Overlap tracking
    ax6 = fig.add_subplot(2, 3, 6)
    ax6.plot(tau_grid, overlaps, 'g-o', lw=2, ms=4)
    ax6.axvline(tau_at_fold, color='orange', ls=':', lw=1, label='Fold')
    ax6.set_xlabel('tau')
    ax6.set_ylabel('|overlap with prev|')
    ax6.set_title('Adiabatic tracking quality')
    ax6.legend(fontsize=8)
    ax6.set_ylim(0, 1.1)

    fig.suptitle('SA-ON-OMEGA-TAU-46: 2D Spectral Action Landscape on (tau, phi)',
                 fontsize=14, fontweight='bold')
    fig.tight_layout(rect=[0, 0, 1, 0.96])

    pngfile = os.path.join(OUTDIR, "s46_sa_omega_tau.png")
    fig.savefig(pngfile, dpi=150, bbox_inches='tight')
    print(f"  Plot saved to: {pngfile}")
    plt.close(fig)

    print()
    print("SA-ON-OMEGA-TAU-46 COMPUTATION COMPLETE")
    print("=" * 78)
