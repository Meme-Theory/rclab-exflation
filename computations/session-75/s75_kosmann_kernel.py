#!/usr/bin/env python3
"""
S75-M1-KOSMANN: Kosmann Lift Kernel Dimension Tau-Scan
======================================================

Computes dim Ker(K_a) (Kosmann lift kernel) at tau = {0.00, 0.05, 0.10, 0.15, 0.190}.

The Kosmann lift operator K_a for direction e_a is defined by (Baptista Paper 17,
eq 4.1; Fatibene-Ferraris-Francaviglia Paper 44, eq 3.19):

    K_a = (1/8) sum_{r,s} [Gamma^s_{r,a} - Gamma^r_{s,a}] gamma_r gamma_s

where Gamma^b_{ca} are Levi-Civita connection coefficients in the ON frame.

The kernel Ker(K_a) consists of spinors psi such that K_a psi = 0.

Structure:
    - For U(2) Killing directions (a = 0,1,2,7): K_a represents the standard
      isometry action on spinors. Its kernel dimension depends on the
      representation theory of U(2) acting on Cliff(8) spinors.
    - For C^2 non-Killing directions (a = 3,4,5,6): K_a involves the Lie
      derivative of the Jensen-deformed metric. Its kernel may change with tau.

Pre-registered Gate S75-M1-KOSMANN:
    PASS: dim Ker(K_a) constant across all 5 tau (topological invariant)
    INFO: Changes but systematic pattern
    FAIL: Erratic

Output:
    s75_kosmann_kernel.npz: kernel dimensions, singular values, operator norms
    Section W4-I of session-75-results-workingpaper.md

Author: Baptista Spacetime Analyst (S75)
Date: 2026-04-12
"""

import sys
import os
import time
import numpy as np
from scipy.linalg import svd, eigh

# Path setup
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from canonical_constants import tau_fold
from dirac_spectrum import (
    su3_generators,
    compute_structure_constants,
    compute_killing_form,
    jensen_metric,
    orthonormal_frame,
    frame_structure_constants,
    connection_coefficients,
    spinor_connection_offset,
    build_cliff8,
    build_chirality,
    validate_clifford,
    validate_connection,
    U1_IDX, SU2_IDX, C2_IDX, U2_IDX,
)

# ============================================================================
# Configuration
# ============================================================================

TAU_VALUES = np.array([0.00, 0.05, 0.10, 0.15, 0.190])  # (local)
N_TAU = len(TAU_VALUES)  # (local)
SVD_THRESHOLD = 1e-12  # (local) singular value threshold for kernel detection
DIM_SPIN = 16  # (local) dimension of spinor space for Cliff(8)

# ============================================================================
# Kosmann lift operator construction
# ============================================================================

def kosmann_operator(Gamma, gammas, a):
    """
    Compute Kosmann lift operator K_a for direction e_a.

    K_a = (1/8) sum_{r,s} [Gamma^s_{r,a} - Gamma^r_{s,a}] gamma_r gamma_s

    Parameters:
        Gamma: (8,8,8) connection coefficients, Gamma[c,a,b] = Gamma^c_{ab}
        gammas: list of 8 Clifford generators (16x16)
        a: direction index

    Returns:
        K_a: (16,16) complex matrix
        A_antisym: (8,8) float, antisymmetric tensor
        Lg_sym: (8,8) float, symmetric tensor (metric Lie derivative)
    """
    dim_spin = gammas[0].shape[0]
    K = np.zeros((dim_spin, dim_spin), dtype=complex)
    A_antisym = np.zeros((8, 8), dtype=np.float64)  # (local)
    Lg_sym = np.zeros((8, 8), dtype=np.float64)  # (local)

    for r in range(8):
        for s in range(8):
            # Antisymmetric part: enters Kosmann correction
            # Gamma^s_{ra} = Gamma[s, r, a]
            # Gamma^r_{sa} = Gamma[r, s, a]
            A_rs = Gamma[s, r, a] - Gamma[r, s, a]  # (local)
            A_antisym[r, s] = A_rs

            # Symmetric part: metric Lie derivative (L_{e_a} g)(e_r, e_s)
            L_rs = Gamma[s, r, a] + Gamma[r, s, a]  # (local)
            Lg_sym[r, s] = L_rs

            if abs(A_rs) > 1e-15:
                K += A_rs * (gammas[r] @ gammas[s])

    K *= (1.0 / 8.0)

    return K, A_antisym, Lg_sym


def compute_kernel_dimension(K_a, threshold=SVD_THRESHOLD):
    """
    Compute dim Ker(K_a) via SVD.

    The kernel dimension equals the number of singular values below threshold.

    Parameters:
        K_a: (n, n) complex matrix
        threshold: float, cutoff for singular value to be "zero"

    Returns:
        dim_ker: int, kernel dimension
        svals: (n,) singular values in ascending order
        rank: int, numerical rank
    """
    _, svals, _ = svd(K_a)
    svals_sorted = np.sort(svals)  # (local) ascending order
    dim_ker = np.sum(svals_sorted < threshold)  # (local)
    rank = K_a.shape[0] - dim_ker  # (local)
    return int(dim_ker), svals_sorted, int(rank)


def compute_full_kosmann_operator(Gamma, gammas):
    """
    Compute the FULL Kosmann operator rho_V = L_V + (1/2) div(V)
    summed over all C^2 directions.

    This is the total operator that enters the gauge-fermion coupling
    (Paper 17, eq 6.1). Its kernel has a more direct physical meaning
    than individual K_a kernels: spinors in Ker(rho_V) decouple from
    the non-Killing gauge fields entirely.

    We compute: K_total = sum_{a in C^2} K_a^dag K_a
    The kernel of K_total equals the INTERSECTION of all Ker(K_a).

    Parameters:
        Gamma: connection coefficients
        gammas: Clifford generators

    Returns:
        K_total: (16,16) positive semidefinite Hermitian matrix
        dim_ker_total: dimension of joint kernel
    """
    dim_spin = gammas[0].shape[0]
    K_total = np.zeros((dim_spin, dim_spin), dtype=complex)  # (local)

    for a in C2_IDX:
        K_a, _, _ = kosmann_operator(Gamma, gammas, a)
        K_total += K_a.conj().T @ K_a

    # K_total is Hermitian positive semi-definite by construction
    evals_total = np.sort(np.linalg.eigvalsh(K_total))  # (local)
    dim_ker_total = int(np.sum(evals_total < SVD_THRESHOLD))  # (local)

    return K_total, dim_ker_total, evals_total


# ============================================================================
# Main computation
# ============================================================================

def main():
    t_start = time.time()  # (local)

    print("=" * 74)
    print("S75-M1-KOSMANN: Kosmann Lift Kernel Dimension Tau-Scan")
    print("=" * 74)
    print(f"Tau values: {TAU_VALUES}")
    print(f"tau_fold (canonical): {tau_fold}")
    print(f"SVD threshold: {SVD_THRESHOLD}")
    print(f"Spinor dim: {DIM_SPIN}")
    print(f"Directions: U(2) = {U2_IDX}, C^2 = {C2_IDX}")
    print()

    # Initialize infrastructure
    gens = su3_generators()  # (local)
    f_abc = compute_structure_constants(gens)  # (local)
    gammas = build_cliff8()  # (local)
    gamma9 = build_chirality(gammas)  # (local)

    cliff_err = validate_clifford(gammas)  # (local)
    print(f"Clifford validation: max_err = {cliff_err:.2e}")

    # Verify gamma9 properties
    g9_sq_err = np.max(np.abs(gamma9 @ gamma9 - np.eye(DIM_SPIN)))  # (local)
    g9_herm_err = np.max(np.abs(gamma9 - gamma9.conj().T))  # (local)
    print(f"gamma_9 involution err: {g9_sq_err:.2e}, Hermiticity err: {g9_herm_err:.2e}")

    # Storage for results
    results = {
        'tau_values': TAU_VALUES,
        'svd_threshold': SVD_THRESHOLD,
    }

    # Per-direction, per-tau storage
    # dim_ker[tau_idx, dir_idx]
    dim_ker_all = np.zeros((N_TAU, 8), dtype=int)  # (local)
    rank_all = np.zeros((N_TAU, 8), dtype=int)  # (local)
    frob_norm_all = np.zeros((N_TAU, 8), dtype=float)  # (local)
    min_sval_all = np.zeros((N_TAU, 8), dtype=float)  # (local)
    max_sval_all = np.zeros((N_TAU, 8), dtype=float)  # (local)
    lg_norm_all = np.zeros((N_TAU, 8), dtype=float)  # (local) metric Lie derivative norms

    # Joint kernel (intersection over C^2 directions)
    dim_ker_joint = np.zeros(N_TAU, dtype=int)  # (local)

    # Chirality decomposition
    dim_ker_plus_all = np.zeros((N_TAU, 8), dtype=int)  # (local) Ker(K_a) intersect V+
    dim_ker_minus_all = np.zeros((N_TAU, 8), dtype=int)  # (local) Ker(K_a) intersect V-

    # Connection validation
    mc_err_all = np.zeros(N_TAU, dtype=float)  # (local)

    print()

    for ti, tau in enumerate(TAU_VALUES):
        print(f"{'=' * 70}")
        print(f"tau = {tau:.3f}  ({ti + 1}/{N_TAU})")
        print(f"{'=' * 70}")

        # Build geometry at this tau
        B_ab = compute_killing_form(f_abc)  # (local)
        g_s = jensen_metric(B_ab, tau)  # (local)
        E = orthonormal_frame(g_s)  # (local)
        ft = frame_structure_constants(f_abc, E)  # (local)
        Gamma = connection_coefficients(ft)  # (local)

        mc_err = validate_connection(Gamma)  # (local)
        mc_err_all[ti] = mc_err
        print(f"  Connection metric-compat err: {mc_err:.2e}")

        # Compute chirality projectors in spinor space
        # V_+ = eigenspace of gamma_9 with eigenvalue +1
        # V_- = eigenspace of gamma_9 with eigenvalue -1
        P_plus = 0.5 * (np.eye(DIM_SPIN) + gamma9)  # (local)
        P_minus = 0.5 * (np.eye(DIM_SPIN) - gamma9)  # (local)

        # Header
        print(f"\n  {'Dir':>4s} {'Type':>8s} {'dimKer':>7s} {'Rank':>5s} "
              f"{'||K_a||':>12s} {'min(sv)':>12s} {'max(sv)':>12s} "
              f"{'||Lg||':>12s} {'Ker+':>5s} {'Ker-':>5s}")
        print(f"  {'-' * 95}")

        for a in range(8):
            K_a, A_antisym, Lg_sym = kosmann_operator(Gamma, gammas, a)

            # Kernel dimension via SVD
            dim_ker, svals, rank = compute_kernel_dimension(K_a)

            # Frobenius norm
            frob = np.linalg.norm(K_a, 'fro')  # (local)

            # Metric Lie derivative norm
            lg_norm = np.linalg.norm(Lg_sym, 'fro')  # (local)

            dim_ker_all[ti, a] = dim_ker
            rank_all[ti, a] = rank
            frob_norm_all[ti, a] = frob
            min_sval_all[ti, a] = svals[0]
            max_sval_all[ti, a] = svals[-1]
            lg_norm_all[ti, a] = lg_norm

            # Chirality decomposition of kernel
            # Project K_a into chiral sectors
            K_plus = P_plus @ K_a @ P_plus  # (local) K_a restricted to V+
            K_minus = P_minus @ K_a @ P_minus  # (local) K_a restricted to V-
            K_cross_pm = P_plus @ K_a @ P_minus  # (local) V- -> V+
            K_cross_mp = P_minus @ K_a @ P_plus  # (local) V+ -> V-

            # For the full kernel, we need the SVD of K_a on each chiral sector.
            # Ker(K_a) intersect V_+ : count singular values below threshold
            # in the restriction of K_a to V+
            # But K_a may mix chiralities. Check:
            cross_norm = np.linalg.norm(K_cross_pm, 'fro') + np.linalg.norm(K_cross_mp, 'fro')  # (local)

            # If K_a preserves chirality (cross terms = 0), then
            # Ker(K_a) = Ker(K_a|V+) + Ker(K_a|V-)
            # From Paper 17, eq 4.5: L_X always commutes with Gamma_K (chirality).
            # Therefore K_a preserves chiral sectors: cross terms should vanish.

            # Extract the 8x8 blocks
            # gamma9 eigenvalues: P_plus projects onto the +1 eigenspace (8D)
            # P_minus projects onto -1 eigenspace (8D)
            evals_g9, evecs_g9 = eigh(gamma9)  # (local)
            idx_plus = np.where(evals_g9 > 0.5)[0]  # (local) +1 eigenvalues
            idx_minus = np.where(evals_g9 < -0.5)[0]  # (local) -1 eigenvalues

            # Restrict K_a to chiral subspaces
            K_plus_block = evecs_g9[:, idx_plus].conj().T @ K_a @ evecs_g9[:, idx_plus]  # (local)
            K_minus_block = evecs_g9[:, idx_minus].conj().T @ K_a @ evecs_g9[:, idx_minus]  # (local)

            dk_plus, _, _ = compute_kernel_dimension(K_plus_block)  # (local)
            dk_minus, _, _ = compute_kernel_dimension(K_minus_block)  # (local)

            dim_ker_plus_all[ti, a] = dk_plus
            dim_ker_minus_all[ti, a] = dk_minus

            dir_type = "Killing" if a in U2_IDX else "C^2"  # (local)
            print(f"  {a:>4d} {dir_type:>8s} {dim_ker:>7d} {rank:>5d} "
                  f"{frob:12.6e} {svals[0]:12.6e} {svals[-1]:12.6e} "
                  f"{lg_norm:12.6e} {dk_plus:>5d} {dk_minus:>5d}")

            # Store full data
            results[f'K_a_{ti}_{a}'] = K_a
            results[f'svals_{ti}_{a}'] = svals
            results[f'A_antisym_{ti}_{a}'] = A_antisym
            results[f'Lg_sym_{ti}_{a}'] = Lg_sym

        # Cross-norm check: chirality preservation
        cross_total = 0.0  # (local)
        for a in range(8):
            K_a = results[f'K_a_{ti}_{a}']
            cn = np.linalg.norm(P_plus @ K_a @ P_minus, 'fro')  # (local)
            cn += np.linalg.norm(P_minus @ K_a @ P_plus, 'fro')
            cross_total += cn
        print(f"\n  Chirality cross-norm total (all 8 dirs): {cross_total:.2e}")
        print(f"  (Should be 0 if K_a commutes with gamma_9)")

        # Joint kernel over C^2 directions
        _, dk_joint, evals_joint = compute_full_kosmann_operator(Gamma, gammas)
        dim_ker_joint[ti] = dk_joint
        results[f'joint_evals_{ti}'] = evals_joint
        print(f"\n  Joint kernel dim (intersection of Ker(K_a), a in C^2): {dk_joint}")
        print(f"  Joint K_total smallest 4 evals: {evals_joint[:4]}")

    # ========================================================================
    # Summary and Gate Evaluation
    # ========================================================================

    print(f"\n{'=' * 74}")
    print("SUMMARY: dim Ker(K_a) at each tau")
    print(f"{'=' * 74}")
    print(f"\n{'tau':>8s}", end="")
    for a in range(8):
        label = f"K_{a}"  # (local)
        print(f"  {label:>6s}", end="")
    print(f"  {'Joint':>6s}")
    print("-" * 80)

    for ti, tau in enumerate(TAU_VALUES):
        print(f"{tau:8.3f}", end="")
        for a in range(8):
            print(f"  {dim_ker_all[ti, a]:>6d}", end="")
        print(f"  {dim_ker_joint[ti]:>6d}")

    # Chiral decomposition summary
    print(f"\n{'=' * 74}")
    print("CHIRAL DECOMPOSITION: dim Ker(K_a) = Ker+ + Ker-")
    print(f"{'=' * 74}")
    print(f"\n{'tau':>8s}", end="")
    for a in C2_IDX:
        print(f"  K_{a}+  K_{a}-", end="")
    print()
    print("-" * 80)

    for ti, tau in enumerate(TAU_VALUES):
        print(f"{tau:8.3f}", end="")
        for a in C2_IDX:
            print(f"  {dim_ker_plus_all[ti, a]:>4d}  {dim_ker_minus_all[ti, a]:>4d}", end="")
        print()

    # Frobenius norm evolution
    print(f"\n{'=' * 74}")
    print("FROBENIUS NORMS: ||K_a||_F at each tau")
    print(f"{'=' * 74}")
    print(f"\n{'tau':>8s}", end="")
    for a in range(8):
        print(f"  {'K_' + str(a):>10s}", end="")
    print()
    print("-" * 100)

    for ti, tau in enumerate(TAU_VALUES):
        print(f"{tau:8.3f}", end="")
        for a in range(8):
            print(f"  {frob_norm_all[ti, a]:10.6f}", end="")
        print()

    # Metric Lie derivative norms
    print(f"\n{'=' * 74}")
    print("METRIC LIE DERIVATIVE: ||L_{e_a} g||_F at each tau")
    print(f"{'=' * 74}")
    print(f"\n{'tau':>8s}", end="")
    for a in range(8):
        print(f"  {'e_' + str(a):>10s}", end="")
    print()
    print("-" * 100)

    for ti, tau in enumerate(TAU_VALUES):
        print(f"{tau:8.3f}", end="")
        for a in range(8):
            print(f"  {lg_norm_all[ti, a]:10.6f}", end="")
        print()

    # ========================================================================
    # GATE EVALUATION: S75-M1-KOSMANN
    # ========================================================================

    print(f"\n{'=' * 74}")
    print("GATE EVALUATION: S75-M1-KOSMANN")
    print(f"{'=' * 74}")

    # Check constancy of dim Ker(K_a) across tau for each direction
    constant_directions = []  # (local)
    changing_directions = []  # (local)
    systematic_pattern = True  # (local)

    for a in range(8):
        ker_vals = dim_ker_all[:, a]  # (local) across all tau
        if np.all(ker_vals == ker_vals[0]):
            constant_directions.append(a)
        else:
            changing_directions.append(a)
            # Check if the change is monotone (systematic)
            diffs = np.diff(ker_vals)  # (local)
            if not (np.all(diffs >= 0) or np.all(diffs <= 0)):
                systematic_pattern = False

    # Joint kernel constancy
    joint_constant = np.all(dim_ker_joint == dim_ker_joint[0])  # (local)

    # Gate verdict
    n_constant = len(constant_directions)  # (local)
    n_changing = len(changing_directions)  # (local)

    print(f"\n  Constant dim Ker directions: {constant_directions} ({n_constant}/8)")
    print(f"  Changing dim Ker directions: {changing_directions} ({n_changing}/8)")
    print(f"  Joint kernel constant: {joint_constant} (dim = {dim_ker_joint[0]} at tau=0)")

    if n_changing == 0 and joint_constant:
        verdict = "PASS"
        verdict_msg = (f"dim Ker(K_a) constant across all 5 tau for all 8 directions. "
                       f"Joint C^2 kernel = {dim_ker_joint[0]}. Topological invariant confirmed.")
    elif n_changing > 0 and systematic_pattern:
        verdict = "INFO"
        verdict_msg = (f"{n_changing}/8 directions show changing Ker dimension, "
                       f"but pattern is systematic (monotone). Not a topological invariant.")
    else:
        verdict = "FAIL"
        verdict_msg = f"Erratic Ker dimension changes in {n_changing}/8 directions."

    print(f"\n  Gate S75-M1-KOSMANN: {verdict}")
    print(f"  {verdict_msg}")

    # ========================================================================
    # Detailed structural analysis
    # ========================================================================

    print(f"\n{'=' * 74}")
    print("STRUCTURAL ANALYSIS")
    print(f"{'=' * 74}")

    # At tau=0 (bi-invariant), check Killing condition for ALL directions
    print("\n  tau=0 (bi-invariant): ALL directions are Killing.")
    print(f"  Metric Lie derivative norms at tau=0: {lg_norm_all[0, :]}")
    bi_inv_killing = np.all(lg_norm_all[0, :] < 1e-10)  # (local)
    print(f"  All L_{'{'}e_a{'}'} g = 0 at tau=0: {bi_inv_killing}")

    # At tau>0 (Jensen deformed), check which directions are Killing
    for ti in range(1, N_TAU):
        tau = TAU_VALUES[ti]
        u2_killing = np.all(lg_norm_all[ti, U2_IDX] < 1e-10)  # (local)
        c2_nonkilling = np.all(lg_norm_all[ti, C2_IDX] > 1e-10)  # (local)
        print(f"\n  tau={tau:.3f}: U(2) Killing: {u2_killing}, C^2 non-Killing: {c2_nonkilling}")
        print(f"    U(2) Lg norms: {lg_norm_all[ti, U2_IDX]}")
        print(f"    C^2  Lg norms: {lg_norm_all[ti, C2_IDX]}")

    # Cross-check: At tau=0 the Kosmann operator should be the standard
    # isometry action for all directions (bi-invariant = all Killing).
    # K_a = (1/8) * 2 * Gamma[s,r,a] * gamma_r gamma_s (since Gamma[s,r,a] = -Gamma[r,s,a])
    # This equals the spin representation of the generator e_a.
    print(f"\n  Bi-invariant cross-check (tau=0):")
    print(f"  K_a should equal (1/4) * sum_{{r,s}} Gamma[s,r,a] gamma_r gamma_s")
    print(f"  = standard spin rep of e_a (up to normalization)")

    # ========================================================================
    # Save results
    # ========================================================================

    results['dim_ker_all'] = dim_ker_all
    results['rank_all'] = rank_all
    results['frob_norm_all'] = frob_norm_all
    results['min_sval_all'] = min_sval_all
    results['max_sval_all'] = max_sval_all
    results['lg_norm_all'] = lg_norm_all
    results['dim_ker_joint'] = dim_ker_joint
    results['dim_ker_plus_all'] = dim_ker_plus_all
    results['dim_ker_minus_all'] = dim_ker_minus_all
    results['mc_err_all'] = mc_err_all
    results['gate_verdict'] = verdict
    results['constant_directions'] = np.array(constant_directions)
    results['changing_directions'] = np.array(changing_directions)

    output_path = os.path.join(SCRIPT_DIR, "s75_kosmann_kernel.npz")  # (local)
    np.savez_compressed(output_path, **results)
    file_size = os.path.getsize(output_path)  # (local)

    elapsed = time.time() - t_start  # (local)
    print(f"\n{'=' * 74}")
    print(f"Saved: {output_path}")
    print(f"File size: {file_size / 1024:.1f} KB")
    print(f"Total runtime: {elapsed:.2f}s")
    print(f"{'=' * 74}")

    return verdict, dim_ker_all, dim_ker_joint


if __name__ == "__main__":
    verdict, dim_ker_all, dim_ker_joint = main()
