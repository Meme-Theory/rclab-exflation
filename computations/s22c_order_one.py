"""
C-2: ORDER-ONE CONDITION [[D, a], JbJ^{-1}] = 0 vs TAU
========================================================

Tests whether the NCG first-order condition is satisfied for the
Jensen-deformed Dirac operator D_K(tau) acting as D_F.

MATHEMATICAL FRAMEWORK
-----------------------

The order-one condition for a spectral triple (A, H, D, J):
    [[D, a], JbJ^{-1}] = 0   for all a, b in A

In the phonon-exflation framework:
    D_K(tau) on sector (p,q) = sum_a E_{ab} rho(X_b) x gamma_a + I x Omega(tau)

A_F = C + H + M_3(C) acts on the C^16 spinor factor via the bimodule action
pi(a) = I_{dim_rho} x a_16, and the opposite algebra acts as
o(b) = I_{dim_rho} x (Xi @ b_16^T @ Xi) on the C^32 = C^16_+ + C^16_- space.

The order-one condition on each (p,q) sector decomposes:

    [[D, I x a], I x o(b)]
    = sum_{alpha} E_{alpha,beta} rho(X_beta) x [[gamma_alpha, a_16], o(b_16)]
      + I x [[Omega(tau), a_16], o(b_16)]

For this to vanish for all a, b in A_F:
    PART 1 (tau-independent): [[gamma_alpha, a_16], o(b_16)] = 0  for alpha=1..8
    PART 2 (tau-dependent):   [[Omega(tau), a_16], o(b_16)] = 0

If Part 1 fails: order-one violated at ALL tau (framework-level problem).
If Part 1 passes but Part 2 fails: tau_max exists where Omega drives violation.
If both pass: order-one satisfied for all tau in [0, 2.0].

IMPORTANT: We work on Psi_+ (16-dim) first, then check full 32-dim.
On Psi_+ alone, the o-map is different from on the full 32-dim space.
The correct test is on the full 32x32 space.

Author: Connes-NCG-Theorist Agent (Session 22c)
Date: 2026-02-20
"""

import numpy as np
from numpy.linalg import eigh, inv
import sys
import os
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))

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
    build_chirality,
    get_irrep,
    dirac_operator_on_irrep,
)

np.set_printoptions(precision=10, linewidth=140, suppress=True)


# =============================================================================
# SECTION 1: A_F ALGEBRA INFRASTRUCTURE (from phase25 scripts)
# =============================================================================

def flat_idx(row, col):
    """Map (row, col) in 4x4 to flat index in 16-dim."""
    if row == 0 and col == 0: return 0
    if row == 0: return col
    if col == 0: return row + 3
    return 7 + 3 * (row - 1) + (col - 1)


def build_bimodule_16(L4, R4):
    """
    Build 16x16 matrix for bimodule action on Psi_+ (4x4 matrix space).
    The action is X -> L4 . X . R4^T, represented in the flattened basis.
    pi_{flat(i,j), flat(k,l)} = L4[i,k] * R4[l,j]
    """
    gen = np.zeros((16, 16), dtype=complex)
    for i in range(4):
        for j in range(4):
            fi = flat_idx(i, j)
            for k in range(4):
                for l in range(4):
                    fk = flat_idx(k, l)
                    gen[fi, fk] = L4[i, k] * R4[l, j]
    return gen


# Chirality structure
gamma5_diag = np.array([1.0, 1.0, -1.0, -1.0])

def get_column_index(flat_idx_val):
    if flat_idx_val == 0: return 0
    elif 1 <= flat_idx_val <= 3: return flat_idx_val
    elif 4 <= flat_idx_val <= 6: return 0
    else: return (flat_idx_val - 7) % 3 + 1

G5_signs = np.array([-gamma5_diag[get_column_index(k)] for k in range(16)])
G5 = np.diag(G5_signs)

# Xi operator (charge conjugation / J on 32-dim)
Xi = np.zeros((32, 32))
Xi[:16, 16:] = -G5
Xi[16:, :16] = -G5

# Chirality grading on 32-dim
gamma_F = np.zeros((32, 32))
gamma_F[:16, :16] = np.eye(16)
gamma_F[16:, 16:] = -np.eye(16)


def rho_minus(rho_plus_v):
    """Conjugate representation: rho_- = G5 conj(rho_+) G5"""
    return G5 @ np.conj(rho_plus_v) @ G5


def full_32(gen_16):
    """Lift a 16x16 generator to the full 32-dim space: [[gen, 0], [0, rho_minus(gen)]]"""
    g32 = np.zeros((32, 32), dtype=complex)
    g32[:16, :16] = gen_16
    g32[16:, 16:] = rho_minus(gen_16)
    return g32


def o_map(gen_32):
    """
    Opposite algebra action: o(b) = J pi(b*) J^{-1}
    In matrix form: Xi @ gen_32^T @ Xi
    """
    return Xi @ gen_32.T @ Xi


def build_AF_generators():
    """
    Build all generators of A_F = C + H + M_3(C) as 32x32 matrices.
    Returns:
        AF_32: list of 32x32 matrices (left action pi(a))
        AF_names: list of names
        AF_factors: list of algebra factors ('C', 'H', 'M3')
    """
    AF_16 = []
    AF_names = []
    AF_factors = []

    # C factor (2 generators: real part = projector, imaginary part)
    L_CIm = np.diag([1j, 1.0, 1.0, 1.0])
    AF_16.append(build_bimodule_16(L_CIm, np.eye(4)))
    AF_names.append('C_Im'); AF_factors.append('C')

    L_CRe = np.diag([1.0, 0.0, 0.0, 0.0])
    AF_16.append(build_bimodule_16(L_CRe, np.eye(4)))
    AF_names.append('C_proj'); AF_factors.append('C')

    # H factor (4 generators: 1, i, j, k)
    L_Hi = np.diag([1j, -1j, 1j, -1j])
    AF_16.append(build_bimodule_16(L_Hi, np.eye(4)))
    AF_names.append('H_i'); AF_factors.append('H')

    L_Hj = np.zeros((4, 4), dtype=complex)
    L_Hj[2, 3] = 1.0; L_Hj[3, 2] = -1.0
    AF_16.append(build_bimodule_16(L_Hj, np.eye(4)))
    AF_names.append('H_j'); AF_factors.append('H')

    L_Hk = np.zeros((4, 4), dtype=complex)
    L_Hk[2, 3] = 1j; L_Hk[3, 2] = 1j
    AF_16.append(build_bimodule_16(L_Hk, np.eye(4)))
    AF_names.append('H_k'); AF_factors.append('H')

    AF_16.append(build_bimodule_16(np.eye(4), np.eye(4)))
    AF_names.append('H_1'); AF_factors.append('H')

    # M_3(C) factor (18 generators: Re and Im parts of each E_{ab})
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

    # Lift to 32-dim
    AF_32 = [full_32(g) for g in AF_16]

    return AF_32, AF_names, AF_factors


# =============================================================================
# SECTION 2: EMBED CLIFFORD AND OMEGA INTO 32-DIM SPACE
# =============================================================================

def embed_spinor_op_32(M_16):
    """
    Embed a 16x16 spinor operator into the 32-dim space.
    Acts as [[M, 0], [0, rho_minus(M)]] on Psi_+ + Psi_-.

    But WAIT: the Clifford gamma_a and Omega are spinorial operators.
    In the NCG convention, D_F = [[0, M^dag], [M, 0]] is off-diagonal.

    For testing [D, a] where D has specific structure:
    - The gamma_a act on the 16-dim spinor space within each (p,q) sector
    - In the full D_K, gamma_a is NOT the same as the D_F chirality structure

    CRITICAL DISTINCTION:
    - gamma_a (a=1..8) are Cliff(R^8) generators: 16x16 Hermitian matrices
    - These are the SPINOR REPRESENTATION of the tangent space of SU(3)
    - They are NOT the same as the internal gamma_5 (chirality of D_F)

    For the order-one test on the 16-dim spinor space:
    The A_F generators act on 16-dim via build_bimodule_16.
    The gamma_a act on 16-dim as Cliff(R^8) generators.
    The question is: do [[gamma_a, a_16], o_16(b_16)] vanish?

    On the 16-dim space, the o-map needs care:
    The opposite algebra action on Psi_+ alone is NOT well-defined in the
    standard NCG sense (which requires the full J operator on 32-dim).

    CORRECT APPROACH: Work on the full 32-dim space throughout.
    """
    M_32 = np.zeros((32, 32), dtype=complex)
    M_32[:16, :16] = M_16
    M_32[16:, 16:] = rho_minus(M_16)
    return M_32


# =============================================================================
# SECTION 3: MAIN COMPUTATION
# =============================================================================

def compute_order_one_norms(tau_values, gens, f_abc, gammas, max_pq_sum=3):
    """
    Compute the order-one condition norm at each tau value.

    For each tau:
    1. Build Omega(tau) as a spinor operator
    2. Embed gamma_a and Omega(tau) into 32-dim space
    3. For each a_F, b_F in A_F generators:
       Compute ||[[gamma_a_32, a_32], o(b_32)]|| and ||[[Omega_32, a_32], o(b_32)]||
    4. Report the maximum norm over all (a, b, alpha) triples

    Returns:
        results: dict with tau, clifford_norms, omega_norms, total_norms
    """
    AF_32, AF_names, AF_factors = build_AF_generators()
    n_gen = len(AF_32)

    B_ab = compute_killing_form(f_abc)

    cliff_norms = np.zeros(len(tau_values))
    omega_norms = np.zeros(len(tau_values))
    total_norms = np.zeros(len(tau_values))

    # Detail arrays for tracking which (a, b, alpha) triple is worst
    cliff_detail = []
    omega_detail = []

    for t_idx, tau in enumerate(tau_values):
        t0 = time.time()

        # Build geometry at this tau
        g_s = jensen_metric(B_ab, tau)
        E = orthonormal_frame(g_s)
        ft = frame_structure_constants(f_abc, E)
        Gamma = connection_coefficients(ft)
        Omega_16 = spinor_connection_offset(Gamma, gammas)

        # Embed into 32-dim
        gamma_32 = [embed_spinor_op_32(g) for g in gammas]
        Omega_32 = embed_spinor_op_32(Omega_16)

        # Test Part 1: Clifford generators (should be tau-independent, but
        # the embedding into 32-dim uses rho_minus which involves G5 conjugation,
        # and the gamma_a are fixed -- so this truly IS tau-independent)
        max_cliff = 0.0
        worst_cliff = None
        for alpha in range(8):
            for i in range(n_gen):
                Da_cliff = gamma_32[alpha] @ AF_32[i] - AF_32[i] @ gamma_32[alpha]
                for j in range(n_gen):
                    ob = o_map(AF_32[j])
                    dc = Da_cliff @ ob - ob @ Da_cliff
                    err = np.max(np.abs(dc))
                    if err > max_cliff:
                        max_cliff = err
                        worst_cliff = (alpha, AF_names[i], AF_names[j], err)

        # Test Part 2: Omega(tau)
        max_omega = 0.0
        worst_omega = None
        for i in range(n_gen):
            Da_omega = Omega_32 @ AF_32[i] - AF_32[i] @ Omega_32
            for j in range(n_gen):
                ob = o_map(AF_32[j])
                dc = Da_omega @ ob - ob @ Da_omega
                err = np.max(np.abs(dc))
                if err > max_omega:
                    max_omega = err
                    worst_omega = (AF_names[i], AF_names[j], err)

        cliff_norms[t_idx] = max_cliff
        omega_norms[t_idx] = max_omega
        total_norms[t_idx] = max(max_cliff, max_omega)
        cliff_detail.append(worst_cliff)
        omega_detail.append(worst_omega)

        dt = time.time() - t0
        print(f"  tau={tau:.2f}: cliff={max_cliff:.3e}, omega={max_omega:.3e}, "
              f"total={total_norms[t_idx]:.3e}  ({dt:.1f}s)")
        if worst_cliff:
            print(f"    Worst cliff: gamma_{worst_cliff[0]+1}, "
                  f"a={worst_cliff[1]}, b={worst_cliff[2]}")
        if worst_omega:
            print(f"    Worst omega: a={worst_omega[0]}, b={worst_omega[1]}")

    return {
        'tau': tau_values,
        'cliff_norms': cliff_norms,
        'omega_norms': omega_norms,
        'total_norms': total_norms,
        'cliff_detail': cliff_detail,
        'omega_detail': omega_detail,
    }


def compute_sector_dependence(tau_values, gens, f_abc, gammas, max_pq_sum=3):
    """
    Check if the order-one condition depends on the (p,q) sector.

    On sector (p,q), D_{(p,q)} = sum E_{ab} rho(X_b) x gamma_a + I x Omega.
    The [D, a] commutator with a = I_rep x a_16 gives:
        [D, a] = sum E_{ab} rho(X_b) x [gamma_a, a_16] + I x [Omega, a_16]

    The double commutator [[D,a], o(b)] with o(b) = I_rep x o_16(b) is:
        sum E_{ab} rho(X_b) x [[gamma_a, a_16], o(b_16)] + I x [[Omega, a_16], o(b_16)]

    Since rho(X_b) x [[...]] has a non-trivial rep-space factor,
    the NORM of this operator depends on ||rho(X_b)|| which varies by sector.
    BUT the CONDITION for vanishing is that EACH tensor factor independently
    vanishes (since the sum over a is a sum of independent tensor products).

    Actually, that's not quite right: the sum is sum_a E_{ab} rho(X_b) x M_a
    where M_a = [[gamma_a, a_16], o(b_16)]. This vanishes for all (p,q) iff
    either (a) M_a = 0 for all a, OR (b) the sum is in the kernel of every
    rho. But (b) would require E_{ab} rho(X_b) = 0 for all (p,q), which
    is impossible for non-trivial reps.

    Therefore: the order-one condition is sector-INDEPENDENT. It reduces to
    the 32-dim (or 16-dim spinor) test already computed in compute_order_one_norms.

    This function verifies this claim numerically by checking a few sectors.
    """
    B_ab = compute_killing_form(f_abc)
    AF_32, AF_names, AF_factors = build_AF_generators()

    # Use a_16 (Psi_+ part) for the sector test
    AF_16 = [g[:16, :16] for g in AF_32]

    # Test at tau = 0.0 and tau = 0.30
    test_taus = [0.0, 0.30]
    sectors = [(0,0), (1,0), (0,1), (1,1), (2,0)]

    results = {}

    for tau in test_taus:
        g_s = jensen_metric(B_ab, tau)
        E = orthonormal_frame(g_s)
        ft = frame_structure_constants(f_abc, E)
        Gamma = connection_coefficients(ft)
        Omega = spinor_connection_offset(Gamma, gammas)

        sector_norms = {}
        for (p, q) in sectors:
            rho_mats, dim_rho = get_irrep(p, q, gens, f_abc)

            # Build full D_{(p,q)} on V_rep x C^16
            D_pq = dirac_operator_on_irrep(rho_mats, E, gammas, Omega)
            dim_total = dim_rho * 16

            # Test order-one on the full sector space
            max_norm = 0.0
            for i_a in range(min(6, len(AF_16))):  # Sample a few generators
                # a acts as I_rep x a_16
                a_full = np.kron(np.eye(dim_rho), AF_16[i_a])
                Da = D_pq @ a_full - a_full @ D_pq

                for i_b in range(min(6, len(AF_16))):
                    # o(b) on 16-dim: needs the o-map
                    # On the rep x spinor space, o(b) = I_rep x o_16(b_16)
                    # But o_map is defined on 32-dim. For 16-dim (Psi_+ only),
                    # we need the restriction.
                    #
                    # On the full 32-dim: o(b) = Xi @ pi(b)^T @ Xi
                    # Restricted to 16x16 upper-left block:
                    # o(b)|_{16} = (-G5) @ pi(b)|_{16}^T @ (-G5) = G5 @ pi(b)_16^T @ G5
                    ob_16 = G5 @ AF_16[i_b].T @ G5
                    ob_full = np.kron(np.eye(dim_rho), ob_16)

                    dc = Da @ ob_full - ob_full @ Da
                    err = np.max(np.abs(dc))
                    max_norm = max(max_norm, err)

            sector_norms[(p, q)] = max_norm

        results[tau] = sector_norms

    return results


# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == '__main__':
    print("=" * 78)
    print("C-2: ORDER-ONE CONDITION [[D, a], JbJ^{-1}] = 0 vs TAU")
    print("=" * 78)
    print()

    # Setup infrastructure
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    gammas = build_cliff8()

    # =========================================================================
    # TEST 1: 32-dim pure spinor test (sector-independent part)
    # =========================================================================
    print("=" * 78)
    print("TEST 1: 32-DIM SPINOR ORDER-ONE (tau-independent Clifford + tau-dependent Omega)")
    print("=" * 78)
    print()
    print("Testing [[gamma_a_32, pi(a_F)_32], o(b_F)_32] and [[Omega_32, pi(a_F)_32], o(b_F)_32]")
    print(f"  A_F generators: C(2) + H(4) + M_3(C)(18) = 24 total")
    print(f"  Clifford generators: gamma_1 through gamma_8")
    print()

    # Use 16 tau values covering [0, 2.0]
    tau_values = np.array([0.0, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40,
                           0.50, 0.60, 0.80, 1.00, 1.20, 1.50, 1.80, 2.00])

    results = compute_order_one_norms(tau_values, gens, f_abc, gammas)

    print()
    print("-" * 78)
    print("SUMMARY: 32-dim spinor order-one norms")
    print("-" * 78)
    print(f"  Clifford part (tau-independent):")
    print(f"    min = {np.min(results['cliff_norms']):.3e}")
    print(f"    max = {np.max(results['cliff_norms']):.3e}")
    print(f"    Should be zero (or machine epsilon) if order-one holds for gamma_a")
    print()
    print(f"  Omega part (tau-dependent):")
    print(f"    min = {np.min(results['omega_norms']):.3e}")
    print(f"    max = {np.max(results['omega_norms']):.3e}")
    print(f"    Growth pattern: {'GROWING' if results['omega_norms'][-1] > 2 * results['omega_norms'][0] else 'STABLE'}")
    print()

    # Check for tau_max (where total exceeds a threshold)
    threshold = 0.01  # 1% of typical D_K eigenvalue
    above = results['total_norms'] > threshold
    if np.any(above):
        tau_max_idx = np.argmax(above)
        tau_max = tau_values[tau_max_idx]
        print(f"  tau_max (norm > {threshold}): {tau_max:.2f}")
    else:
        print(f"  tau_max: NONE (norm < {threshold} everywhere in [0, 2.0])")

    # =========================================================================
    # TEST 2: Sector dependence check
    # =========================================================================
    print()
    print("=" * 78)
    print("TEST 2: SECTOR DEPENDENCE (verify order-one is sector-independent)")
    print("=" * 78)
    print()

    sector_results = compute_sector_dependence(tau_values[:2], gens, f_abc, gammas)

    for tau_val, s_norms in sector_results.items():
        print(f"  tau = {tau_val:.2f}:")
        for (p, q), norm in sorted(s_norms.items()):
            print(f"    ({p},{q}): max||[[D,a],o(b)]|| = {norm:.3e}")

    # =========================================================================
    # TEST 3: Factor-by-factor analysis
    # =========================================================================
    print()
    print("=" * 78)
    print("TEST 3: FACTOR-BY-FACTOR ANALYSIS (which algebra factors contribute)")
    print("=" * 78)
    print()

    AF_32, AF_names, AF_factors = build_AF_generators()
    B_ab = compute_killing_form(f_abc)

    # Test at tau = 0.0 and tau = 0.30
    for tau in [0.0, 0.30]:
        g_s = jensen_metric(B_ab, tau)
        E = orthonormal_frame(g_s)
        ft = frame_structure_constants(f_abc, E)
        Gamma = connection_coefficients(ft)
        Omega_16 = spinor_connection_offset(Gamma, gammas)
        Omega_32 = embed_spinor_op_32(Omega_16)
        gamma_32 = [embed_spinor_op_32(g) for g in gammas]

        print(f"  tau = {tau:.2f}:")

        # Factor pairs: C-C, C-H, C-M3, H-H, H-M3, M3-M3
        factor_pairs = {}
        n_gen = len(AF_32)

        for i in range(n_gen):
            for j in range(n_gen):
                f_pair = (AF_factors[i], AF_factors[j])
                if f_pair not in factor_pairs:
                    factor_pairs[f_pair] = {'cliff': 0.0, 'omega': 0.0}

                ob = o_map(AF_32[j])

                # Clifford part
                for alpha in range(8):
                    Da_cliff = gamma_32[alpha] @ AF_32[i] - AF_32[i] @ gamma_32[alpha]
                    dc = Da_cliff @ ob - ob @ Da_cliff
                    err = np.max(np.abs(dc))
                    factor_pairs[f_pair]['cliff'] = max(factor_pairs[f_pair]['cliff'], err)

                # Omega part
                Da_omega = Omega_32 @ AF_32[i] - AF_32[i] @ Omega_32
                dc = Da_omega @ ob - ob @ Da_omega
                err = np.max(np.abs(dc))
                factor_pairs[f_pair]['omega'] = max(factor_pairs[f_pair]['omega'], err)

        for (f1, f2), norms in sorted(factor_pairs.items()):
            status_c = "PASS" if norms['cliff'] < 1e-10 else f"FAIL ({norms['cliff']:.3e})"
            status_o = "PASS" if norms['omega'] < 1e-10 else f"FAIL ({norms['omega']:.3e})"
            print(f"    ({f1:3s}, {f2:3s}): cliff={status_c}, omega={status_o}")

    # =========================================================================
    # VERDICT
    # =========================================================================
    print()
    print("=" * 78)
    print("VERDICT")
    print("=" * 78)
    print()

    cliff_max = np.max(results['cliff_norms'])
    omega_max = np.max(results['omega_norms'])
    total_max = np.max(results['total_norms'])

    cliff_pass = cliff_max < 1e-10
    omega_pass = omega_max < 1e-10

    if cliff_pass and omega_pass:
        print("  CLOSED (order-one satisfied for all tau in [0, 2.0])")
        print("  The NCG axiom provides NO constraint on tau.")
        print("  Probability shift: -1 pp")
        verdict = "CLOSED"
        bf = 0.5
        shift = "-1 pp"
    elif not cliff_pass:
        print("  NEUTRAL/FATAL: Clifford part violates order-one")
        print(f"  Max Clifford violation: {cliff_max:.3e}")
        print("  This means the order-one condition is violated at ALL tau,")
        print("  including tau=0 (bi-invariant metric). Framework inconsistency.")
        print()
        # Check if violation is O(1) or small
        if cliff_max > 0.1:
            print("  SEVERE: O(1) violation. The A_F bimodule structure is incompatible")
            print("  with the Cliff(R^8) algebra. This challenges the identification")
            print("  D_K = D_F at the axiomatic level.")
            print("  Probability shift: -15 pp")
            verdict = "NEUTRAL"
            bf = 0.1
            shift = "-15 pp"
        else:
            print(f"  MILD: Violation at {cliff_max:.3e} level.")
            print("  May indicate approximate order-one (broken at sub-leading order).")
            print("  Probability shift: -3 to -5 pp")
            verdict = "MILD_VIOLATION"
            bf = 0.3
            shift = "-3 to -5 pp"
    else:
        # cliff_pass but not omega_pass
        print("  Clifford part: PASS (exact, tau-independent)")
        print("  Omega part: FAIL (tau-dependent violation)")
        print()

        # Find tau_max
        omega_norms = results['omega_norms']
        # Threshold: O(1) relative to typical Omega norm
        # Use the Omega norm itself as reference
        omega_abs = np.max(np.abs(Omega_16))  # recompute at last tau for reference
        threshold_rel = 0.01 * omega_abs if omega_abs > 0 else 1e-6

        omega_above = omega_norms > threshold_rel
        if np.any(omega_above):
            tau_max_idx = np.argmax(omega_above)
            tau_max = tau_values[tau_max_idx]

            if 0.30 <= tau_max <= 0.40:
                print(f"  DECISIVE: tau_max = {tau_max:.2f} in [0.30, 0.40]")
                print(f"  Probability shift: +15 to +20 pp")
                verdict = "DECISIVE"
                bf = 40
                shift = "+15 to +20 pp"
            elif 0.20 <= tau_max <= 0.60:
                print(f"  COMPELLING: tau_max = {tau_max:.2f} in [0.20, 0.60]")
                print(f"  Probability shift: +8 to +12 pp")
                verdict = "COMPELLING"
                bf = 15
                shift = "+8 to +12 pp"
            elif 1.0 <= tau_max <= 2.0:
                print(f"  INTERESTING: tau_max = {tau_max:.2f} in [1.0, 2.0]")
                print(f"  Probability shift: +1 to +2 pp")
                verdict = "INTERESTING"
                bf = 3
                shift = "+1 to +2 pp"
            else:
                print(f"  tau_max = {tau_max:.2f} (outside pre-registered windows)")
                verdict = "NEUTRAL"
                bf = 1
                shift = "0 pp"
        else:
            print(f"  Omega violation too small to establish tau_max")
            print(f"  Max omega violation: {omega_max:.3e}")
            print(f"  May be growing but has not reached threshold")
            verdict = "INCONCLUSIVE"
            bf = 1
            shift = "0 pp"

    print()
    print(f"  Final verdict: {verdict}")
    print(f"  Bayes factor: {bf}")
    print(f"  Probability shift: {shift}")
    print()

    # =========================================================================
    # SAVE RESULTS
    # =========================================================================
    output_txt = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                              's22c_order_one.txt')
    with open(output_txt, 'w') as f:
        f.write("C-2: ORDER-ONE CONDITION [[D, a], JbJ^{-1}] = 0 vs TAU\n")
        f.write("=" * 60 + "\n\n")

        f.write("tau | cliff_norm | omega_norm | total_norm\n")
        f.write("-" * 60 + "\n")
        for idx in range(len(tau_values)):
            f.write(f"{tau_values[idx]:6.2f}  {results['cliff_norms'][idx]:.6e}  "
                    f"{results['omega_norms'][idx]:.6e}  "
                    f"{results['total_norms'][idx]:.6e}\n")

        f.write(f"\nCliff max: {cliff_max:.6e}\n")
        f.write(f"Omega max: {omega_max:.6e}\n")
        f.write(f"Verdict: {verdict}\n")
        f.write(f"BF: {bf}\n")
        f.write(f"Shift: {shift}\n")

    print(f"  Results saved to: {output_txt}")
    print()
    print("C-2 COMPUTATION COMPLETE")
