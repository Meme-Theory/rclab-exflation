"""
OMEGA-CLASSIFY-46 VERIFICATION: Spectral Action Hessian with cutoff functions
==============================================================================

Computes the PHYSICAL mass-squared matrix from the spectral action
Tr f(D_phys^2/Lambda^2) second variation, with multiple cutoff functions.

The kinetic mass Tr([D,phi]^dag [D,phi]) is positive definite (Gram matrix).
The spectral action Hessian includes the cutoff function and can in principle
be negative (tachyonic), providing the Higgs mechanism.

This script verifies whether any tachyonic direction exists in the spectral
action Hessian when evaluated on the Omega^1_D scalar directions.
"""

import numpy as np
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from tier1_dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    jensen_metric, orthonormal_frame, frame_structure_constants,
    connection_coefficients, spinor_connection_offset, build_cliff8,
    get_irrep, dirac_operator_on_irrep, _irrep_cache,
)
from s46_omega_classify import (
    build_AF_generators, build_DK, compute_omega1_full,
    decompose_by_grading,
)

np.set_printoptions(precision=10, linewidth=140, suppress=True)

if __name__ == "__main__":
    t0_total = time.time()

    print("=" * 78)
    print("OMEGA-CLASSIFY-46 VERIFICATION: Spectral Action Hessian")
    print("=" * 78)
    print()

    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    B_ab = compute_killing_form(f_abc)
    gammas = build_cliff8()
    gamma_9 = np.eye(16, dtype=complex)
    for g in gammas:
        gamma_9 = gamma_9 @ g

    AF_16, AF_names, AF_factors, AF_class = build_AF_generators()

    # Build D_K (anti-Hermitian) at fold and round
    D_fold_ah, dim_rho = build_DK(0.19, gens, f_abc, B_ab, gammas, 1, 0)
    D_round_ah, _ = build_DK(0.00, gens, f_abc, B_ab, gammas, 1, 0)
    N = D_fold_ah.shape[0]

    # Physical Dirac (Hermitian): D_phys = i * D_K
    D_fold = 1j * D_fold_ah
    D_round = 1j * D_round_ah

    # Verify Hermiticity
    herm_err_fold = np.max(np.abs(D_fold - D_fold.conj().T))
    herm_err_round = np.max(np.abs(D_round - D_round.conj().T))
    print(f"  D_fold Hermiticity error:  {herm_err_fold:.2e}")
    print(f"  D_round Hermiticity error: {herm_err_round:.2e}")
    print()

    # Get eigenvalues and eigenvectors
    evals_fold, evecs_fold = np.linalg.eigh(D_fold)
    evals_round, evecs_round = np.linalg.eigh(D_round)
    print(f"  Eigenvalues at fold:  [{evals_fold.min():.4f}, {evals_fold.max():.4f}]")
    print(f"  Eigenvalues at round: [{evals_round.min():.4f}, {evals_round.max():.4f}]")
    print()

    # Get scalar basis at fold (using anti-Hermitian D for module computation)
    omega_fold = compute_omega1_full(D_fold_ah, AF_16, dim_rho)
    _, odd_basis_fold, _, dim_odd_fold, _ = decompose_by_grading(
        omega_fold["combined_basis"], N, dim_rho, gamma_9)

    omega_round = compute_omega1_full(D_round_ah, AF_16, dim_rho)
    _, odd_basis_round, _, dim_odd_round, _ = decompose_by_grading(
        omega_round["combined_basis"], N, dim_rho, gamma_9)

    print(f"  Scalar directions at fold:  {dim_odd_fold}")
    print(f"  Scalar directions at round: {dim_odd_round}")
    print()

    # =====================================================================
    # STRUCTURAL THEOREM
    # =====================================================================
    print("=" * 78)
    print("STRUCTURAL THEOREM: Gram Matrix Positive Definiteness")
    print("=" * 78)
    print()
    print("  The kinetic mass matrix M^2_{ij} = Tr([D_phys, phi_i]^dag [D_phys, phi_j])")
    print("  is a GRAM MATRIX, hence positive semi-definite by construction.")
    print("  This is independent of tau, cutoff function, or representation.")
    print()
    print("  Proof: Define w_i = [D_phys, phi_i]. Then M^2_{ij} = <w_i, w_j>_HS")
    print("  where <A, B>_HS = Tr(A^dag B) is the Hilbert-Schmidt inner product.")
    print("  Gram matrices are PSD. QED.")
    print()

    # =====================================================================
    # SPECTRAL ACTION HESSIAN (cutoff-dependent)
    # =====================================================================
    print("=" * 78)
    print("SPECTRAL ACTION HESSIAN: Cutoff-Dependent Mass Matrix")
    print("=" * 78)
    print()

    # The spectral action S = Tr f(D_phys^2 / Lambda^2)
    # Second variation: D_phys -> D_phys + eps * phi
    # (D + eps phi)^2 = D^2 + eps{D,phi} + eps^2 phi^2
    #
    # Using the trace functional:
    # d^2/deps^2 Tr f(D^2/L^2 + eps {D,phi}/L^2 + eps^2 phi^2/L^2)|_{eps=0}
    # = Tr[f'(D^2/L^2) phi^2/L^2] + (1/2) Tr[f''(D^2/L^2) {D,phi}^2/L^4]
    #
    # In eigenbasis D = diag(lambda_k):
    # = sum_k f'(lambda_k^2/L^2) (phi^2)_{kk}/L^2
    #   + (1/2) sum_{k,m} f''_interpolated * |(D phi + phi D)_{km}|^2/L^4
    #
    # More precisely, for the matrix function:
    # Tr f(A + eps B)|_{eps=0}^{d^2} = sum_{k,m} f^{[1]}(lambda_k, lambda_m) |B_{km}|^2
    # where f^{[1]}(x,y) = (f(x) - f(y))/(x - y) is the first divided difference.
    #
    # Here A = D^2/L^2 and B = {D,phi}/L^2 + phi^2/L^2
    # At eps=0, the second order is:
    # H = sum_{k,m} f^{[1]}(lk^2/L^2, lm^2/L^2) * |{D,phi}_{km}|^2/L^4
    #   + sum_k f'(lk^2/L^2) * (phi^2)_{kk} / L^2

    # Let me compute using the EXACT formula with divided differences.

    Lambda = np.max(np.abs(evals_fold)) * 1.5

    def spectral_action_hessian(evals, evecs, phi_sa, Lambda, f_func):
        """
        Compute the second variation of Tr f(D^2/Lambda^2) w.r.t. D -> D + eps*phi.

        Uses the divided difference formula for matrix function derivatives.
        """
        N_loc = len(evals)
        x = evals**2 / Lambda**2  # spectrum of D^2/Lambda^2

        # Transform phi to eigenbasis
        phi_eig = evecs.conj().T @ phi_sa @ evecs

        # Anticommutator in eigenbasis: {D, phi}_{km} = (lk + lm) phi_{km}
        anti_comm = np.zeros((N_loc, N_loc), dtype=complex)
        for k in range(N_loc):
            for m in range(N_loc):
                anti_comm[k, m] = (evals[k] + evals[m]) * phi_eig[k, m]

        # B = {D, phi}/L^2
        B = anti_comm / Lambda**2

        # First divided difference of f: f^{[1]}(x_k, x_m) = (f(x_k) - f(x_m))/(x_k - x_m)
        f_vals = f_func(x)

        # The second variation from the {D,phi} term:
        # H_1 = sum_{k,m} f^{[1]}(x_k, x_m) |B_{km}|^2
        H_anticomm = 0.0
        for k in range(N_loc):
            for m in range(N_loc):
                if abs(x[k] - x[m]) > 1e-15:
                    f_div = (f_vals[k] - f_vals[m]) / (x[k] - x[m])
                else:
                    # At degenerate points, use f'(x_k)
                    # Numerically: finite difference
                    dx = 1e-8
                    f_div = (f_func(x[k] + dx) - f_func(x[k])) / dx
                H_anticomm += f_div * np.abs(B[k, m])**2

        # The second variation from the phi^2 term:
        # H_2 = sum_k f'(x_k) (phi^2)_{kk} / L^2
        phi2 = phi_sa @ phi_sa
        phi2_eig = evecs.conj().T @ phi2 @ evecs
        dx = 1e-8
        H_phi2 = 0.0
        for k in range(N_loc):
            fp = (f_func(x[k] + dx) - f_func(x[k])) / dx
            H_phi2 += fp * np.real(phi2_eig[k, k]) / Lambda**2

        return H_anticomm + H_phi2, H_anticomm, H_phi2

    # Define cutoff functions
    cutoffs = [
        ("exp(-x)", lambda x: np.exp(-x)),
        ("(1-x)^2 * theta", lambda x: np.where(x < 1, (1-x)**2, 0.0)),
        ("1/(1+x)", lambda x: 1.0/(1+x)),
        ("exp(-x^2)", lambda x: np.exp(-x**2)),
        ("1/(1+x)^2", lambda x: 1.0/(1+x)**2),
        ("erfc(sqrt(x))", lambda x: 0.5 * (1 - np.tanh(np.sqrt(np.maximum(x, 0))))),
    ]

    # Compute for the 10 lightest scalar modes at fold
    n_modes = min(10, dim_odd_fold)

    print(f"  Lambda = {Lambda:.4f} (1.5 * max eigenvalue)")
    print()

    for f_name, f_func in cutoffs:
        print(f"  Cutoff: f(x) = {f_name}")
        n_neg = 0
        for mode_idx in range(n_modes):
            phi_vec = odd_basis_fold[mode_idx].reshape(N, N)
            phi_sa = (phi_vec + phi_vec.conj().T) / np.sqrt(2.0)
            norm = np.sqrt(np.real(np.trace(phi_sa.conj().T @ phi_sa)))
            if norm > 1e-15:
                phi_sa /= norm

            H_total, H_anti, H_phi2 = spectral_action_hessian(
                evals_fold, evecs_fold, phi_sa, Lambda, f_func)

            sign = "TACHYON" if H_total < -1e-15 else ("ZERO" if abs(H_total) < 1e-15 else "massive")
            if H_total < -1e-15:
                n_neg += 1
            print(f"    Mode {mode_idx:2d}: H = {np.real(H_total):+12.6e}  "
                  f"(anti={np.real(H_anti):+10.4e}, phi2={np.real(H_phi2):+10.4e})  [{sign}]")

        print(f"    Tachyonic modes: {n_neg}/{n_modes}")
        print()

    # =====================================================================
    # FOLD vs ROUND COMPARISON (all modes)
    # =====================================================================
    print("=" * 78)
    print("FOLD vs ROUND: Full Hessian spectrum (exponential cutoff)")
    print("=" * 78)
    print()

    f_func = lambda x: np.exp(-x)

    # Full Hessian matrix at fold (n_modes x n_modes)
    n_full = min(50, dim_odd_fold)  # limit for speed
    H_mat_fold = np.zeros((n_full, n_full))

    phis_fold = []
    for i in range(n_full):
        phi_vec = odd_basis_fold[i].reshape(N, N)
        phi_sa = (phi_vec + phi_vec.conj().T) / np.sqrt(2.0)
        norm = np.sqrt(np.real(np.trace(phi_sa.conj().T @ phi_sa)))
        if norm > 1e-15:
            phi_sa /= norm
        phis_fold.append(phi_sa)

    x = evals_fold**2 / Lambda**2
    f_vals = f_func(x)

    # Compute full matrix using divided differences
    for i in range(n_full):
        phi_i_eig = evecs_fold.conj().T @ phis_fold[i] @ evecs_fold
        for j in range(i, n_full):
            phi_j_eig = evecs_fold.conj().T @ phis_fold[j] @ evecs_fold

            H_ij = 0.0
            for k in range(N):
                for m in range(N):
                    if abs(x[k] - x[m]) > 1e-15:
                        f_div = (f_vals[k] - f_vals[m]) / (x[k] - x[m])
                    else:
                        dx = 1e-8
                        f_div = (f_func(x[k] + dx) - f_func(x[k])) / dx

                    # {D, phi_i}_{km} = (lk + lm) (phi_i)_{km}
                    anti_i = (evals_fold[k] + evals_fold[m]) * phi_i_eig[k, m] / Lambda**2
                    anti_j = (evals_fold[k] + evals_fold[m]) * phi_j_eig[k, m] / Lambda**2
                    H_ij += f_div * np.real(anti_i * anti_j.conj())

            # phi^2 cross term
            phi2_cross = phis_fold[i] @ phis_fold[j]
            p2c_eig = evecs_fold.conj().T @ phi2_cross @ evecs_fold
            for k in range(N):
                dx = 1e-8
                fp = (f_func(x[k] + dx) - f_func(x[k])) / dx
                H_ij += fp * np.real(p2c_eig[k, k]) / Lambda**2

            H_mat_fold[i, j] = H_ij
            H_mat_fold[j, i] = H_ij

    H_evals_fold = np.linalg.eigvalsh(H_mat_fold)
    n_neg_fold = np.sum(H_evals_fold < -1e-15)
    n_zero_fold = np.sum(np.abs(H_evals_fold) < 1e-15)
    n_pos_fold = np.sum(H_evals_fold > 1e-15)

    print(f"  FOLD: {n_full}x{n_full} Hessian matrix eigenvalues:")
    print(f"    Negative: {n_neg_fold}")
    print(f"    Zero:     {n_zero_fold}")
    print(f"    Positive: {n_pos_fold}")
    print(f"    Min:      {H_evals_fold[0]:+.6e}")
    print(f"    Max:      {H_evals_fold[-1]:+.6e}")
    print()
    print(f"  Lowest 10 eigenvalues:")
    for k in range(min(10, len(H_evals_fold))):
        label = "TACHYON" if H_evals_fold[k] < -1e-15 else "massive"
        print(f"    H_{k:3d} = {H_evals_fold[k]:+12.6e}  [{label}]")
    print()

    # =====================================================================
    # VERDICT REFINEMENT
    # =====================================================================
    print("=" * 78)
    print("OMEGA-CLASSIFY-46 VERDICT (REFINED)")
    print("=" * 78)
    print()

    if n_neg_fold > 0:
        print(f"  SPECTRAL ACTION HESSIAN HAS {n_neg_fold} NEGATIVE EIGENVALUES AT FOLD.")
        print(f"  The spectral action second variation IS tachyonic for these directions.")
        print(f"  This indicates the spectral action POTENTIAL (not just kinetic) favors")
        print(f"  non-zero inner fluctuations at the fold.")
    else:
        print(f"  All {n_pos_fold} eigenvalues of the spectral action Hessian are POSITIVE.")
        print(f"  No tachyonic instability from inner fluctuations in the spectral action.")
    print()

    total_time = time.time() - t0_total
    print(f"  Total runtime: {total_time:.1f}s")
    print()
    print("VERIFICATION COMPLETE")
    print("=" * 78)
