"""
BA-31-6: Order-One Condition Severity Assessment
==================================================

Assesses the severity of the order-one condition (Axiom 5) violation
by comparing the framework's violation norm (4.000) to the distribution
of violations from random anti-Hermitian matrices matching D_K's structure.

The order-one condition requires: [[D, a], b^0] = 0 for all a, b in A.
For M4 x K with continuous K, this becomes a constraint on [[D_K, rho(X)], rho(Y)^0]
for all X, Y in the Lie algebra.

The violation norm is max_XY || [[D_K, rho(X)], rho(Y)^0] ||.

Gate BA-31-oo:
  SEVERE if 4.000 > 95th percentile of random
  NATURAL if within the random distribution

Author: sim (phonon-exflation-sim), Session 31Aa
Date: 2026-03-02
"""

import numpy as np
import sys
import os
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))

from tier1_dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    build_cliff8, jensen_metric, orthonormal_frame, frame_structure_constants,
    connection_coefficients, spinor_connection_offset,
    dirac_operator_on_irrep, get_irrep
)


def compute_order_one_violation(D, rho_list, dim_rho, dim_spin=16):
    """
    Compute max_XY || [[D, rho(X) x I_spin], I_rho x (rho(Y) x I_spin)^0] ||_op

    For the order-one condition test, a acts as rho(X) x I_spin on V_rho x S,
    and b^0 acts as I_rho x (something on S).

    The simpler form: for Lie group NCG, the order-one condition tests
    [[D, pi_L(X)], pi_R(Y)] = 0
    where pi_L/R are left/right regular rep restricted to the irrep sector.

    In our case with D on V_{(p,q)} x C^16:
    - "a" acts on V_{(p,q)} via rho(e_a), tensored with I_16
    - "b^0" acts on V_{(p,q)} via I_dim x (something on C^16)
    - For the Lie group geometry, b^0 would be the right-regular rep,
      but for the continuous case this is rho_bar(e_a) = complex conjugate rep

    Simplified test: compute [[D, A_a], B_b] where
      A_a = rho(e_a) x I_16   (left action)
      B_b = I_dim x gamma_b   (Clifford algebra action, proxy for right action)

    This is the test performed in Session 28b/28c.

    Returns:
        max_norm: maximum operator norm of the double commutator
    """
    dim_total = D.shape[0]
    gammas = build_cliff8()
    I_rho = np.eye(dim_rho, dtype=complex)
    I_spin = np.eye(dim_spin, dtype=complex)

    max_norm = 0.0

    for a in range(8):
        A_a = np.kron(rho_list[a], I_spin)  # dim_total x dim_total
        comm_DA = D @ A_a - A_a @ D  # [D, A_a]

        for b in range(8):
            B_b = np.kron(I_rho, gammas[b])  # dim_total x dim_total
            double_comm = comm_DA @ B_b - B_b @ comm_DA  # [[D, A_a], B_b]

            # Operator norm (largest singular value)
            norm = np.linalg.norm(double_comm, ord=2)
            max_norm = max(max_norm, norm)

    return max_norm


def random_anti_hermitian(n, rng):
    """Generate a random n x n anti-Hermitian matrix."""
    A = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
    return (A - A.conj().T) / 2.0


def compute_violation_random(dim_rho, rho_list, n_trials=100, seed=42):
    """
    Compute order-one violation for random anti-Hermitian matrices
    matching D_K's structure: dim_rho * 16.

    The random D_rand is structured as: a general anti-Hermitian matrix
    on V_rho x S. This is the null hypothesis for "no special structure."

    For a fairer comparison, we also test block-structured randoms:
    D_rand = sum_a rho(e_a) x R_a + I x Omega_rand
    where R_a are random 16x16 anti-Hermitian.
    """
    dim_spin = 16
    dim_total = dim_rho * dim_spin
    rng = np.random.default_rng(seed)

    # General random anti-Hermitian
    violations_general = np.zeros(n_trials)
    for i in range(n_trials):
        D_rand = random_anti_hermitian(dim_total, rng)
        # Scale to match D_K norm
        D_rand *= 2.0 / np.linalg.norm(D_rand, ord=2)
        violations_general[i] = compute_order_one_violation(
            D_rand, rho_list, dim_rho, dim_spin
        )

    # Structured random: D = sum_a rho(e_a) x R_a + I x Omega_rand
    violations_structured = np.zeros(n_trials)
    I_rho = np.eye(dim_rho, dtype=complex)
    for i in range(n_trials):
        D_struct = np.zeros((dim_total, dim_total), dtype=complex)
        for a in range(8):
            R_a = random_anti_hermitian(dim_spin, rng)
            D_struct += np.kron(rho_list[a], R_a)
        Omega_rand = random_anti_hermitian(dim_spin, rng)
        D_struct += np.kron(I_rho, Omega_rand)
        # Scale to match D_K norm
        D_struct *= 2.0 / np.linalg.norm(D_struct, ord=2)
        violations_structured[i] = compute_order_one_violation(
            D_struct, rho_list, dim_rho, dim_spin
        )

    return violations_general, violations_structured


def main():
    t_start = time.time()

    print("=" * 70)
    print("BA-31-6: ORDER-ONE CONDITION SEVERITY ASSESSMENT")
    print("=" * 70)

    # Load existing data
    oo_data = np.load('tier0-computation/s28b_order_one.npz', allow_pickle=True)
    ax_data = np.load('tier0-computation/s28c_12d_axioms.npz', allow_pickle=True)

    framework_violation = float(ax_data['a5_max_norm'])
    print(f"\nFramework order-one violation: {framework_violation:.4f}")
    print(f"Axiom verdicts: {ax_data['axiom_verdicts']}")
    print(f"Gate verdict: {ax_data['gate_verdict']}")

    # Per-tau and per-sector breakdown from s28b
    print(f"\nPer-sector violation norms (Frobenius max):")
    for i, label in enumerate(oo_data['sector_labels']):
        print(f"  {label}: {oo_data['frob_max'][i]} (tau=0, 0.15, 0.30)")
    print(f"  Cliff max 32dim: {oo_data['cliff_max_32dim']}")

    # ========================================================================
    # Random matrix comparison
    # ========================================================================
    print(f"\n--- Random Matrix Comparison ---")
    print(f"Using (1,1) adjoint sector: dim_rho=8, dim_total=128")

    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    rho_adj, dim_adj = get_irrep(1, 1, gens, f_abc)
    assert dim_adj == 8

    n_trials = 100

    # Compute actual D_K violation at tau=0 for reference
    B_ab = compute_killing_form(f_abc)
    gammas = build_cliff8()

    print(f"\nComputing D_K violation at tau=0, 0.15, 0.30...")
    for tau in [0.0, 0.15, 0.30]:
        g_s = jensen_metric(B_ab, tau)
        E = orthonormal_frame(g_s)
        ft = frame_structure_constants(f_abc, E)
        Gamma = connection_coefficients(ft)
        Omega = spinor_connection_offset(Gamma, gammas)

        D_adj = dirac_operator_on_irrep(rho_adj, E, gammas, Omega)
        violation = compute_order_one_violation(D_adj, rho_adj, dim_adj)
        D_norm = np.linalg.norm(D_adj, ord=2)
        print(f"  tau={tau:.2f}: violation = {violation:.4f}, ||D||_op = {D_norm:.4f}, "
              f"violation/||D|| = {violation/D_norm:.4f}")

    print(f"\nGenerating {n_trials} random matrices ({n_trials} general + {n_trials} structured)...")
    t0 = time.time()

    viol_gen, viol_struct = compute_violation_random(
        dim_adj, rho_adj, n_trials=n_trials, seed=42
    )

    dt_rand = time.time() - t0
    print(f"  Compute time: {dt_rand:.1f}s")

    # Statistics
    print(f"\n--- General Random D (no structure) ---")
    print(f"  Mean: {np.mean(viol_gen):.4f}")
    print(f"  Std:  {np.std(viol_gen):.4f}")
    print(f"  Min:  {np.min(viol_gen):.4f}")
    print(f"  Max:  {np.max(viol_gen):.4f}")
    print(f"  5th percentile: {np.percentile(viol_gen, 5):.4f}")
    print(f"  50th percentile: {np.percentile(viol_gen, 50):.4f}")
    print(f"  95th percentile: {np.percentile(viol_gen, 95):.4f}")
    print(f"  Framework {framework_violation:.3f} percentile: "
          f"{np.mean(viol_gen <= framework_violation) * 100:.1f}%")

    print(f"\n--- Structured Random D (sum rho(e_a) x R_a + I x Omega) ---")
    print(f"  Mean: {np.mean(viol_struct):.4f}")
    print(f"  Std:  {np.std(viol_struct):.4f}")
    print(f"  Min:  {np.min(viol_struct):.4f}")
    print(f"  Max:  {np.max(viol_struct):.4f}")
    print(f"  5th percentile: {np.percentile(viol_struct, 5):.4f}")
    print(f"  50th percentile: {np.percentile(viol_struct, 50):.4f}")
    print(f"  95th percentile: {np.percentile(viol_struct, 95):.4f}")
    print(f"  Framework {framework_violation:.3f} percentile: "
          f"{np.mean(viol_struct <= framework_violation) * 100:.1f}%")

    # ========================================================================
    # Gate verdict
    # ========================================================================
    print("\n" + "=" * 70)
    print("GATE BA-31-oo ASSESSMENT")
    print("=" * 70)

    # Use the structured comparison as the primary benchmark
    # (it matches D_K's tensor product structure)
    pct_struct = np.mean(viol_struct <= framework_violation) * 100
    p95_struct = np.percentile(viol_struct, 95)

    if framework_violation > p95_struct:
        verdict = "SEVERE"
        print(f"  Framework violation {framework_violation:.3f} > 95th percentile {p95_struct:.3f}")
        print(f"  Percentile rank: {pct_struct:.1f}%")
        print(f"  --> BA-31-oo: SEVERE")
        print(f"      Violation is anomalously large even compared to structured random matrices.")
    else:
        verdict = "NATURAL"
        print(f"  Framework violation {framework_violation:.3f} within structured random distribution")
        print(f"  95th percentile: {p95_struct:.3f}")
        print(f"  Percentile rank: {pct_struct:.1f}%")
        print(f"  --> BA-31-oo: NATURAL")
        print(f"      Violation is typical for continuous K with tensor product spinor structure.")

    # Also report general comparison
    pct_gen = np.mean(viol_gen <= framework_violation) * 100
    p95_gen = np.percentile(viol_gen, 95)
    print(f"\n  General random comparison: {pct_gen:.1f}% percentile, 95th = {p95_gen:.3f}")

    # ========================================================================
    # Save
    # ========================================================================
    np.savez('tier0-computation/s31alt_order_one_severity.npz',
             framework_violation=framework_violation,
             viol_general=viol_gen,
             viol_structured=viol_struct,
             pct_general=pct_gen,
             pct_structured=pct_struct,
             p95_general=p95_gen,
             p95_structured=p95_struct,
             n_trials=n_trials,
             verdict=np.array(verdict))
    print(f"\nSaved: tier0-computation/s31alt_order_one_severity.npz")

    elapsed = time.time() - t_start
    print(f"Total runtime: {elapsed:.1f}s")
    print(f"\nGATE BA-31-oo: {verdict}")

    return verdict


if __name__ == '__main__':
    main()
