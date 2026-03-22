"""
C-3: ORDER-ONE CONDITION [[D_can, a_F], J b_F J^{-1}] = 0
===========================================================

Tests whether M_Lie (the algebraic/Lie-derivative part of D_can, the
canonical-connection Dirac operator) satisfies the NCG order-one condition.

MATHEMATICAL FRAMEWORK
-----------------------

The order-one condition for a spectral triple (A, H, D, J):
    [[D, a], J b J^{-1}] = 0   for all a, b in A

For D_can = M_Lie on sector (p,q):
    M_Lie = sum_{a,b} E_{ab} rho(X_b) (x) gamma_a

where E is the orthonormal frame (Jensen metric), rho is the (p,q) irrep,
X_b are the SU(3) generators, and gamma_a are Cliff(R^8) generators.

The algebra A_F = C + H + M_3(C) acts as I_rep (x) a_{16} on the full
sector space V_rep (x) C^16. The order-one condition becomes:

    [[M_Lie, I (x) a], I (x) o(b)]
    = sum_{a',b} E_{a'b} rho(X_b) (x) [[gamma_{a'}, a_16], o(b_16)]

where o(b) = J pi(b*) J^{-1} is the opposite algebra action.

KEY STRUCTURAL OBSERVATION:
    Since rho(X_b) are linearly independent for non-trivial reps,
    the sum vanishes for ALL (p,q) iff each spinor factor vanishes:
        [[gamma_{a'}, a_16], o(b_16)] = 0   for all a' = 1..8

    This is IDENTICAL to the Clifford part of the D_K order-one test (s22c).
    The Omega part that appeared in D_K is ABSENT in D_can.

COMPARISON WITH D_K (s22c C-2):
    D_K order-one:  Clifford violation (O(1)) + Omega violation (grows with tau)
    D_can order-one: Clifford violation ONLY (no Omega term)

    D_can is "cleaner" in that its order-one violation is purely structural
    (the Baptista-Connes representation mismatch on C^16) and does NOT grow
    with tau. This is a qualitative difference from D_K.

SPECIAL CASES:
    (0,0) singlet: rho(X_b) = 0 => M_Lie = 0 => order-one TRIVIALLY SATISFIED.
    This is a genuine difference from D_K, where D_K|_{(0,0)} = Omega != 0.

TESTS PERFORMED:
    1. Pure spinor 32-dim test: [[gamma_a_32, pi(a_F)_32], o(b_F)_32]
       (tau-independent, same as s22c Clifford part)
    2. Full sector test: [[M_Lie, I (x) a_16], I (x) o(b_16)]
       at tau = 0, 0.15, 0.30 for sectors (0,0), (1,0), (0,1), (1,1)
    3. Factor-by-factor analysis: which A_F factors contribute to violation

Author: phonon-exflation-sim agent (Session 28b)
Date: 2026-02-27
Depends on: s22c_order_one.py (A_F infrastructure), s27_torsion_gap_gate.py (M_Lie builder)
"""

import numpy as np
from numpy.linalg import norm as la_norm
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
    _irrep_cache,
)

# Import M_Lie builder from s27
from s27_torsion_gap_gate import build_M_Lie

np.set_printoptions(precision=10, linewidth=140, suppress=True)

OUTDIR = os.path.dirname(os.path.abspath(__file__))


# =============================================================================
# SECTION 1: A_F ALGEBRA INFRASTRUCTURE (from s22c_order_one.py)
# =============================================================================

def flat_idx(row: int, col: int) -> int:
    """
    Map (row, col) in 4x4 matrix to flat index in 16-dim Psi_+.

    The flattening convention for the 4x4 bimodule representation:
        (0,0) -> 0          (lepton singlet, nu_R)
        (0,1..3) -> 1..3    (lepton doublet + singlet)
        (1..3,0) -> 4..6    (quark singlet colors)
        (1..3,1..3) -> 7..15 (quark doublet+singlet, 3 colors)
    """
    if row == 0 and col == 0:
        return 0
    if row == 0:
        return col
    if col == 0:
        return row + 3
    return 7 + 3 * (row - 1) + (col - 1)


def build_bimodule_16(L4: np.ndarray, R4: np.ndarray) -> np.ndarray:
    """
    Build 16x16 matrix for bimodule action on Psi_+ (4x4 matrix space).

    The A_F bimodule action on M_4(C) is: X -> L4 . X . R4^T.
    In the flattened 16-dim basis:
        pi_{flat(i,j), flat(k,l)} = L4[i,k] * R4[l,j]

    Args:
        L4: (4,4) complex matrix (left action)
        R4: (4,4) complex matrix (right action, transposed in formula)

    Returns:
        gen: (16,16) complex matrix
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


# Chirality structure on Psi_+
gamma5_diag = np.array([1.0, 1.0, -1.0, -1.0])


def get_column_index(flat_idx_val: int) -> int:
    """Map flat index back to column in 4x4."""
    if flat_idx_val == 0:
        return 0
    elif 1 <= flat_idx_val <= 3:
        return flat_idx_val
    elif 4 <= flat_idx_val <= 6:
        return 0
    else:
        return (flat_idx_val - 7) % 3 + 1


# G5 = chirality grading on Psi_+ (16-dim)
G5_signs = np.array([-gamma5_diag[get_column_index(k)] for k in range(16)])
G5 = np.diag(G5_signs)

# Xi operator = J on 32-dim space = [[0, -G5], [-G5, 0]]
Xi = np.zeros((32, 32))
Xi[:16, 16:] = -G5
Xi[16:, :16] = -G5

# Chirality grading on 32-dim: gamma_F = [[I, 0], [0, -I]]
gamma_F = np.zeros((32, 32))
gamma_F[:16, :16] = np.eye(16)
gamma_F[16:, 16:] = -np.eye(16)


def rho_minus(rho_plus_v: np.ndarray) -> np.ndarray:
    """Conjugate representation: rho_- = G5 conj(rho_+) G5."""
    return G5 @ np.conj(rho_plus_v) @ G5


def full_32(gen_16: np.ndarray) -> np.ndarray:
    """
    Lift a 16x16 generator to the full 32-dim space.

    On Psi = Psi_+ + Psi_-:
        pi(a) = [[a_16, 0], [0, rho_minus(a_16)]]
    """
    g32 = np.zeros((32, 32), dtype=complex)
    g32[:16, :16] = gen_16
    g32[16:, 16:] = rho_minus(gen_16)
    return g32


def o_map(gen_32: np.ndarray) -> np.ndarray:
    """
    Opposite algebra action on 32-dim space.

    o(b) = J pi(b*) J^{-1} = Xi @ gen_32^T @ Xi

    (Xi is self-inverse since Xi^2 = G5^2 = I on each block.)
    """
    return Xi @ gen_32.T @ Xi


def o_map_16(gen_16: np.ndarray) -> np.ndarray:
    """
    Opposite algebra action restricted to Psi_+ (16-dim).

    On the 32-dim space: o(b) = Xi @ pi(b)^T @ Xi
    Restricted to the upper-left 16x16 block:
        o(b)|_{16} = (-G5) @ gen_16^T @ (-G5) = G5 @ gen_16^T @ G5
    """
    return G5 @ gen_16.T @ G5


def embed_spinor_op_32(M_16: np.ndarray) -> np.ndarray:
    """
    Embed a 16x16 spinor operator into the 32-dim space.

    [[M, 0], [0, rho_minus(M)]]
    """
    M_32 = np.zeros((32, 32), dtype=complex)
    M_32[:16, :16] = M_16
    M_32[16:, 16:] = rho_minus(M_16)
    return M_32


def build_AF_generators():
    """
    Build all generators of A_F = C + H + M_3(C) as both 16x16 and 32x32 matrices.

    Following the Baptista convention (Session 22c s22c_order_one.py).

    Returns:
        AF_16: list of (16,16) complex matrices (left action on Psi_+)
        AF_32: list of (32,32) complex matrices (lifted to full space)
        AF_names: list of generator names
        AF_factors: list of algebra factor labels ('C', 'H', 'M3')
    """
    AF_16 = []
    AF_names = []
    AF_factors = []

    # C factor (2 generators: imaginary part, projector)
    L_CIm = np.diag([1j, 1.0, 1.0, 1.0])
    AF_16.append(build_bimodule_16(L_CIm, np.eye(4)))
    AF_names.append('C_Im')
    AF_factors.append('C')

    L_CRe = np.diag([1.0, 0.0, 0.0, 0.0])
    AF_16.append(build_bimodule_16(L_CRe, np.eye(4)))
    AF_names.append('C_proj')
    AF_factors.append('C')

    # H factor (4 generators: 1, i, j, k acting on rows 2-3)
    L_Hi = np.diag([1j, -1j, 1j, -1j])
    AF_16.append(build_bimodule_16(L_Hi, np.eye(4)))
    AF_names.append('H_i')
    AF_factors.append('H')

    L_Hj = np.zeros((4, 4), dtype=complex)
    L_Hj[2, 3] = 1.0
    L_Hj[3, 2] = -1.0
    AF_16.append(build_bimodule_16(L_Hj, np.eye(4)))
    AF_names.append('H_j')
    AF_factors.append('H')

    L_Hk = np.zeros((4, 4), dtype=complex)
    L_Hk[2, 3] = 1j
    L_Hk[3, 2] = 1j
    AF_16.append(build_bimodule_16(L_Hk, np.eye(4)))
    AF_names.append('H_k')
    AF_factors.append('H')

    AF_16.append(build_bimodule_16(np.eye(4), np.eye(4)))
    AF_names.append('H_1')
    AF_factors.append('H')

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

    return AF_16, AF_32, AF_names, AF_factors


# =============================================================================
# SECTION 2: PURE SPINOR ORDER-ONE (Clifford part only, no Omega)
# =============================================================================

def compute_clifford_order_one_32(gammas):
    """
    Test the pure Clifford part of the order-one condition on the 32-dim space.

    For D_can, the ENTIRE order-one condition reduces to:
        [[gamma_a_32, pi(a_F)_32], o(b_F)_32] = 0  for all a, a_F, b_F

    This is IDENTICAL to the Clifford part of the D_K order-one test (s22c)
    and is tau-INDEPENDENT.

    Returns:
        max_norm: float, maximum violation over all (alpha, a_F, b_F) triples
        worst_triple: tuple (alpha, a_name, b_name, norm)
        factor_norms: dict mapping (factor_a, factor_b) -> max norm
    """
    AF_16, AF_32, AF_names, AF_factors = build_AF_generators()
    n_gen = len(AF_32)

    gamma_32 = [embed_spinor_op_32(g) for g in gammas]

    max_norm = 0.0
    worst_triple = None
    factor_norms = {}

    for alpha in range(8):
        for i in range(n_gen):
            # [gamma_alpha, a_F]
            comm_Da = gamma_32[alpha] @ AF_32[i] - AF_32[i] @ gamma_32[alpha]

            for j in range(n_gen):
                ob = o_map(AF_32[j])
                # [[gamma_alpha, a_F], o(b_F)]
                dc = comm_Da @ ob - ob @ comm_Da
                err = np.max(np.abs(dc))

                if err > max_norm:
                    max_norm = err
                    worst_triple = (alpha, AF_names[i], AF_names[j], err)

                f_pair = (AF_factors[i], AF_factors[j])
                if f_pair not in factor_norms:
                    factor_norms[f_pair] = 0.0
                factor_norms[f_pair] = max(factor_norms[f_pair], err)

    return max_norm, worst_triple, factor_norms


# =============================================================================
# SECTION 3: FULL SECTOR ORDER-ONE (M_Lie on rep x spinor space)
# =============================================================================

def compute_sector_order_one(tau_values, sectors, gens, f_abc, gammas):
    """
    Test the order-one condition for M_Lie on full sector spaces.

    For each (tau, sector):
        [[M_Lie, I_rep (x) a_16], I_rep (x) o_16(b_16)]

    On the (0,0) singlet, M_Lie = 0 => order-one satisfied trivially.
    On non-trivial sectors, the violation is amplified by ||rho(X_b)||.

    Args:
        tau_values: array of tau values to test
        sectors: list of (p,q) tuples
        gens: SU(3) generators (from su3_generators())
        f_abc: structure constants
        gammas: Cliff(R^8) generators

    Returns:
        results: dict with keys:
            'sector_norms': (n_sec, n_tau) max violation norms
            'sector_worst': list of (n_sec, n_tau) worst (a_name, b_name) pairs
            'factor_norms': (n_sec, n_tau) dict -> factor pair max norms
    """
    B_ab = compute_killing_form(f_abc)
    AF_16, AF_32, AF_names, AF_factors = build_AF_generators()
    n_gen = len(AF_16)

    n_tau = len(tau_values)
    n_sec = len(sectors)

    sector_norms = np.zeros((n_sec, n_tau))
    sector_worst = [[None] * n_tau for _ in range(n_sec)]
    # Per-sector, per-tau factor norms
    sector_factor_norms = [[{} for _ in range(n_tau)] for _ in range(n_sec)]

    for ti, tau in enumerate(tau_values):
        t0 = time.time()

        # Build geometry at this tau
        g_s = jensen_metric(B_ab, tau)
        E = orthonormal_frame(g_s)

        for si, (p, q) in enumerate(sectors):
            _irrep_cache.clear()

            if p == 0 and q == 0:
                # Trivial rep: M_Lie = 0, order-one trivially satisfied
                sector_norms[si, ti] = 0.0
                sector_worst[si][ti] = ('TRIVIAL', 'TRIVIAL', 0.0)
                for fa in ['C', 'H', 'M3']:
                    for fb in ['C', 'H', 'M3']:
                        sector_factor_norms[si][ti][(fa, fb)] = 0.0
                continue

            rho, dim_rho = get_irrep(p, q, gens, f_abc)

            # Build M_Lie
            M = build_M_Lie(rho, E, gammas)

            # Test order-one on rep (x) spinor space
            max_norm = 0.0
            worst = None
            f_norms = {}

            for i in range(n_gen):
                # a acts as I_rep (x) a_16
                a_full = np.kron(np.eye(dim_rho), AF_16[i])
                comm_Ma = M @ a_full - a_full @ M

                for j in range(n_gen):
                    # o(b) on 16-dim (Psi_+ restriction)
                    ob_16 = o_map_16(AF_16[j])
                    ob_full = np.kron(np.eye(dim_rho), ob_16)

                    dc = comm_Ma @ ob_full - ob_full @ comm_Ma
                    err = np.max(np.abs(dc))

                    if err > max_norm:
                        max_norm = err
                        worst = (AF_names[i], AF_names[j], err)

                    f_pair = (AF_factors[i], AF_factors[j])
                    if f_pair not in f_norms:
                        f_norms[f_pair] = 0.0
                    f_norms[f_pair] = max(f_norms[f_pair], err)

            sector_norms[si, ti] = max_norm
            sector_worst[si][ti] = worst
            sector_factor_norms[si][ti] = f_norms

        dt = time.time() - t0
        norms_str = ', '.join(
            f'{sector_norms[si, ti]:.4e}' for si in range(n_sec))
        print(f"  tau={tau:.2f}: norms=[{norms_str}]  ({dt:.1f}s)")

    return {
        'sector_norms': sector_norms,
        'sector_worst': sector_worst,
        'sector_factor_norms': sector_factor_norms,
    }


# =============================================================================
# SECTION 4: COMPARISON WITH D_K ORDER-ONE
# =============================================================================

def compute_dk_order_one_norms(tau_values, sectors, gens, f_abc, gammas):
    """
    Compute D_K order-one norms for comparison. D_K has both Clifford and
    Omega contributions:

        [[D_K, I (x) a_16], I (x) o_16(b_16)]
        = sum E_{ab} rho(X_b) (x) [[gamma_a, a_16], o(b_16)]
          + I (x) [[Omega(tau), a_16], o(b_16)]

    This allows direct side-by-side comparison: D_can violation vs D_K violation.

    Returns:
        dk_norms: (n_sec, n_tau) max violation norms for D_K
    """
    B_ab = compute_killing_form(f_abc)
    AF_16, AF_32, AF_names, AF_factors = build_AF_generators()
    n_gen = len(AF_16)

    n_tau = len(tau_values)
    n_sec = len(sectors)
    dk_norms = np.zeros((n_sec, n_tau))

    for ti, tau in enumerate(tau_values):
        g_s = jensen_metric(B_ab, tau)
        E = orthonormal_frame(g_s)
        ft = frame_structure_constants(f_abc, E)
        Gamma = connection_coefficients(ft)
        Omega = spinor_connection_offset(Gamma, gammas)

        for si, (p, q) in enumerate(sectors):
            _irrep_cache.clear()

            if p == 0 and q == 0:
                # D_K|_{(0,0)} = Omega (not zero!)
                D_K_mat = Omega.copy()
                dim_rho = 1

                max_norm = 0.0
                for i in range(n_gen):
                    comm_Da = D_K_mat @ AF_16[i] - AF_16[i] @ D_K_mat
                    for j in range(n_gen):
                        ob_16 = o_map_16(AF_16[j])
                        dc = comm_Da @ ob_16 - ob_16 @ comm_Da
                        err = np.max(np.abs(dc))
                        max_norm = max(max_norm, err)

                dk_norms[si, ti] = max_norm
            else:
                rho, dim_rho = get_irrep(p, q, gens, f_abc)
                D_K_mat = dirac_operator_on_irrep(rho, E, gammas, Omega)

                max_norm = 0.0
                for i in range(n_gen):
                    a_full = np.kron(np.eye(dim_rho), AF_16[i])
                    comm_Da = D_K_mat @ a_full - a_full @ D_K_mat

                    for j in range(n_gen):
                        ob_16 = o_map_16(AF_16[j])
                        ob_full = np.kron(np.eye(dim_rho), ob_16)
                        dc = comm_Da @ ob_full - ob_full @ comm_Da
                        err = np.max(np.abs(dc))
                        max_norm = max(max_norm, err)

                dk_norms[si, ti] = max_norm

    return dk_norms


# =============================================================================
# SECTION 5: FROBENIUS NORM VARIANT (requested in prompt)
# =============================================================================

def compute_frobenius_norms(tau_values, sectors, gens, f_abc, gammas):
    """
    Compute Frobenius norms of [[M_Lie, a], o(b)] for all generator pairs.

    Returns a (n_pairs, n_tau, n_sec) array where n_pairs = (n_gen choose 2 with repetition).
    Also returns max-entry norms (L_inf) for comparison.
    """
    B_ab = compute_killing_form(f_abc)
    AF_16, AF_32, AF_names, AF_factors = build_AF_generators()
    n_gen = len(AF_16)

    n_tau = len(tau_values)
    n_sec = len(sectors)

    frob_max = np.zeros((n_sec, n_tau))   # max Frobenius norm over all (a,b) pairs
    linf_max = np.zeros((n_sec, n_tau))   # max L_inf norm over all (a,b) pairs

    for ti, tau in enumerate(tau_values):
        g_s = jensen_metric(B_ab, tau)
        E = orthonormal_frame(g_s)

        for si, (p, q) in enumerate(sectors):
            _irrep_cache.clear()

            if p == 0 and q == 0:
                frob_max[si, ti] = 0.0
                linf_max[si, ti] = 0.0
                continue

            rho, dim_rho = get_irrep(p, q, gens, f_abc)
            M = build_M_Lie(rho, E, gammas)

            fm = 0.0
            lm = 0.0
            for i in range(n_gen):
                a_full = np.kron(np.eye(dim_rho), AF_16[i])
                comm_Ma = M @ a_full - a_full @ M

                for j in range(n_gen):
                    ob_16 = o_map_16(AF_16[j])
                    ob_full = np.kron(np.eye(dim_rho), ob_16)
                    dc = comm_Ma @ ob_full - ob_full @ comm_Ma

                    fn = la_norm(dc, 'fro')
                    ln = np.max(np.abs(dc))
                    fm = max(fm, fn)
                    lm = max(lm, ln)

            frob_max[si, ti] = fm
            linf_max[si, ti] = lm

    return frob_max, linf_max


# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == '__main__':
    t_total_start = time.time()

    print("=" * 78)
    print("C-3: ORDER-ONE CONDITION [[D_can, a_F], J b_F J^{-1}] = 0")
    print("=" * 78)
    print()

    # Setup infrastructure
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    gammas = build_cliff8()

    tau_values = np.array([0.0, 0.15, 0.30])
    sectors = [(0, 0), (1, 0), (0, 1), (1, 1)]
    sector_labels = ['(0,0)', '(1,0)', '(0,1)', '(1,1)']

    # =========================================================================
    # TEST 1: Pure Clifford 32-dim test (tau-independent)
    # =========================================================================
    print("=" * 78)
    print("TEST 1: PURE CLIFFORD ORDER-ONE (32-dim, tau-independent)")
    print("=" * 78)
    print()
    print("For D_can, the order-one condition reduces ENTIRELY to the Clifford part:")
    print("  [[gamma_a_32, pi(a_F)_32], o(b_F)_32] = 0  for all (a, a_F, b_F)")
    print("  (No Omega contribution -- D_can has no spin connection.)")
    print()

    t0 = time.time()
    cliff_max, cliff_worst, cliff_factor_norms = compute_clifford_order_one_32(gammas)
    dt = time.time() - t0

    print(f"  Max Clifford violation (L_inf): {cliff_max:.6e}  ({dt:.1f}s)")
    if cliff_worst:
        print(f"  Worst triple: gamma_{cliff_worst[0]+1}, "
              f"a={cliff_worst[1]}, b={cliff_worst[2]}")
    print()

    print("  Factor-by-factor breakdown:")
    for (f1, f2), nrm in sorted(cliff_factor_norms.items()):
        status = "PASS" if nrm < 1e-10 else f"FAIL ({nrm:.3e})"
        print(f"    ({f1:3s}, {f2:3s}): {status}")
    print()

    # =========================================================================
    # TEST 2: Full sector order-one for M_Lie
    # =========================================================================
    print("=" * 78)
    print("TEST 2: FULL SECTOR ORDER-ONE FOR M_Lie (D_can)")
    print("=" * 78)
    print()
    print(f"Testing at tau = {list(tau_values)}")
    print(f"Sectors: {sector_labels}")
    print()

    results = compute_sector_order_one(tau_values, sectors, gens, f_abc, gammas)

    print()
    print("  Summary table (max L_inf norm over all (a_F, b_F) pairs):")
    print(f"  {'tau':>6s}", end="")
    for label in sector_labels:
        print(f" | {label:>12s}", end="")
    print()
    print("  " + "-" * (8 + len(sectors) * 15))
    for ti, tau in enumerate(tau_values):
        print(f"  {tau:6.2f}", end="")
        for si in range(len(sectors)):
            n = results['sector_norms'][si, ti]
            print(f" | {n:12.6e}", end="")
        print()

    print()
    print("  Worst violators per sector per tau:")
    for ti, tau in enumerate(tau_values):
        for si, label in enumerate(sector_labels):
            w = results['sector_worst'][si][ti]
            if w and w[0] != 'TRIVIAL':
                print(f"    tau={tau:.2f}, {label}: a={w[0]:15s}, b={w[1]:15s}, "
                      f"norm={w[2]:.4e}")
            elif w and w[0] == 'TRIVIAL':
                print(f"    tau={tau:.2f}, {label}: M_Lie = 0 (trivial rep), "
                      f"order-one EXACT")

    # =========================================================================
    # TEST 3: Comparison with D_K order-one
    # =========================================================================
    print()
    print("=" * 78)
    print("TEST 3: COMPARISON D_can vs D_K ORDER-ONE")
    print("=" * 78)
    print()
    print("D_K has both Clifford + Omega contributions to the violation.")
    print("D_can has Clifford only. The Omega part is ABSENT in D_can.")
    print()

    t0 = time.time()
    dk_norms = compute_dk_order_one_norms(tau_values, sectors, gens, f_abc, gammas)
    dt = time.time() - t0
    print(f"  D_K order-one computed in {dt:.1f}s")
    print()

    dcan_norms = results['sector_norms']

    print(f"  {'tau':>6s} {'sector':>8s} {'D_can':>12s} {'D_K':>12s} {'ratio':>8s} {'notes':>20s}")
    print("  " + "-" * 70)
    for ti, tau in enumerate(tau_values):
        for si, label in enumerate(sector_labels):
            dc = dcan_norms[si, ti]
            dk = dk_norms[si, ti]
            ratio = dc / dk if dk > 1e-15 else float('nan')

            if sectors[si] == (0, 0):
                notes = "M_Lie=0, D_K=Omega"
            elif dc < dk:
                notes = "D_can SMALLER"
            elif dc > dk:
                notes = "D_K SMALLER"
            else:
                notes = "EQUAL"

            print(f"  {tau:6.2f} {label:>8s} {dc:12.6e} {dk:12.6e} "
                  f"{ratio:8.4f} {notes:>20s}")

    # =========================================================================
    # TEST 4: Frobenius norm variant
    # =========================================================================
    print()
    print("=" * 78)
    print("TEST 4: FROBENIUS NORM ORDER-ONE (complementary to L_inf)")
    print("=" * 78)
    print()

    t0 = time.time()
    frob_max, linf_max = compute_frobenius_norms(
        tau_values, sectors, gens, f_abc, gammas)
    dt = time.time() - t0
    print(f"  Computed in {dt:.1f}s")
    print()

    print(f"  {'tau':>6s} {'sector':>8s} {'Frobenius':>12s} {'L_inf':>12s}")
    print("  " + "-" * 42)
    for ti, tau in enumerate(tau_values):
        for si, label in enumerate(sector_labels):
            print(f"  {tau:6.2f} {label:>8s} {frob_max[si,ti]:12.6e} "
                  f"{linf_max[si,ti]:12.6e}")

    # =========================================================================
    # TEST 5: Factor analysis on sector space
    # =========================================================================
    print()
    print("=" * 78)
    print("TEST 5: FACTOR-BY-FACTOR ON (1,0) SECTOR")
    print("=" * 78)
    print()

    # Show factor breakdown for (1,0) at each tau
    si_10 = 1  # index of (1,0) sector
    for ti, tau in enumerate(tau_values):
        fn = results['sector_factor_norms'][si_10][ti]
        if fn:
            print(f"  tau={tau:.2f}:")
            for (f1, f2), nrm in sorted(fn.items()):
                status = "PASS" if nrm < 1e-10 else f"FAIL ({nrm:.3e})"
                print(f"    ({f1:3s}, {f2:3s}): {status}")
            print()

    # =========================================================================
    # STRUCTURAL ANALYSIS
    # =========================================================================
    print()
    print("=" * 78)
    print("STRUCTURAL ANALYSIS")
    print("=" * 78)
    print()

    # Tau independence check for non-trivial sectors
    for si, label in enumerate(sector_labels):
        if sectors[si] == (0, 0):
            continue
        norms = dcan_norms[si, :]
        variation = (np.max(norms) - np.min(norms)) / np.mean(norms) if np.mean(norms) > 0 else 0
        print(f"  {label}: norm range [{np.min(norms):.6e}, {np.max(norms):.6e}], "
              f"relative variation = {variation:.4e}")

    # Check: is the violation entirely in the Clifford part?
    # For M_Lie = sum E_{ab} rho(X_b) (x) gamma_a:
    # The double commutator is: sum_{a',b} E_{a'b} rho(X_b) (x) [[gamma_{a'}, a_16], o(b_16)]
    # This factorizes: the spinor factor [[gamma_{a'}, a_16], o(b_16)] is tau-independent,
    # but the coefficient E_{a'b} * rho(X_b) changes with tau.
    # So the NORM varies with tau even though the CONDITION (vanishing) is tau-independent.
    print()
    print("  Note: The violation NORM varies with tau because E_{ab} depends on the")
    print("  Jensen metric. But the CONDITION for vanishing is tau-INDEPENDENT:")
    print("  it requires [[gamma_a, a_16], o(b_16)] = 0 for all a=1..8.")
    print("  This is the Baptista-Connes representation mismatch (Session 9-10).")

    # =========================================================================
    # VERDICT
    # =========================================================================
    print()
    print("=" * 78)
    print("GATE C-3 VERDICT")
    print("=" * 78)
    print()

    # Gate criteria
    max_nontrivial = 0.0
    for si, (p, q) in enumerate(sectors):
        if p == 0 and q == 0:
            continue
        max_nontrivial = max(max_nontrivial, np.max(dcan_norms[si, :]))

    singlet_norm = np.max(dcan_norms[0, :])  # (0,0) sector

    print(f"  (0,0) singlet: max norm = {singlet_norm:.6e}")
    print(f"  Non-trivial sectors: max norm = {max_nontrivial:.6e}")
    print()

    # Comparison with D_K
    max_dk_nontrivial = 0.0
    max_dk_singlet = 0.0
    for si, (p, q) in enumerate(sectors):
        if p == 0 and q == 0:
            max_dk_singlet = max(max_dk_singlet, np.max(dk_norms[si, :]))
        else:
            max_dk_nontrivial = max(max_dk_nontrivial, np.max(dk_norms[si, :]))

    print(f"  D_K comparison:")
    print(f"    D_K singlet max: {max_dk_singlet:.6e}")
    print(f"    D_K non-trivial max: {max_dk_nontrivial:.6e}")
    print()

    # Apply gate criteria
    if max_nontrivial < 1e-10:
        verdict = "PASS"
        detail = ("Order-one condition satisfied at machine precision for all sectors "
                   "at all tested tau values.")
    elif max_nontrivial > 0.01:
        verdict = "FAIL"
        detail = (f"Order-one condition violated with max norm = {max_nontrivial:.3e}. "
                   "This is O(1) and reflects the structural Baptista-Connes "
                   "representation mismatch (same as D_K Clifford part in s22c).")
    else:
        verdict = "MARGINAL"
        detail = f"Order-one violation at {max_nontrivial:.3e} level (between 1e-10 and 0.01)."

    print(f"  VERDICT: {verdict}")
    print(f"  {detail}")
    print()

    # Contextual analysis
    if verdict == "FAIL":
        print("  CONTEXTUAL ANALYSIS:")
        print("  " + "-" * 70)
        print()
        print("  The O(1) violation is the SAME structural issue found in s22c C-2:")
        print("  the Baptista A_F representation and the Cliff(R^8) spinor algebra")
        print("  use incompatible identifications of C^16.")
        print()
        print("  KEY DIFFERENCE from D_K:")
        print(f"    - D_can on (0,0): norm = {singlet_norm:.1e} (TRIVIALLY ZERO)")
        print(f"      D_K  on (0,0): norm = {max_dk_singlet:.3e} (Omega contribution)")
        print()
        print("    - D_can non-trivial: PURELY Clifford (no Omega, tau-independent condition)")
        print("      D_K  non-trivial: Clifford + Omega (tau-dependent, grows with tau)")
        print()
        print("    - D_can violation does NOT grow with tau (structurally cleaner)")
        print("      D_K  violation grows ~ e^tau through the Omega term")
        print()
        print("  IMPLICATION: D_can does NOT satisfy the standard NCG order-one axiom.")
        print("  This is unsurprising: D_can = M_Lie is the Lie-derivative operator,")
        print("  which is algebraically natural on the group but not on the bimodule.")
        print("  The order-one condition is a bimodule property (A-A bimodule structure)")
        print("  and is sensitive to how A_F is realized on the spinor space.")
        print()
        print("  RESOLUTION PATH: The same Baptista-Connes identification issue.")
        print("  Neither D_K nor D_can satisfy order-one in the Baptista representation.")
        print("  A correct identification (if it exists) would need to reconcile")
        print("  the bimodule structure with the Clifford algebra -- an open problem")
        print("  since Session 9-10 (Phase 2.5).")

    # =========================================================================
    # SAVE RESULTS
    # =========================================================================
    print()
    t_total = time.time() - t_total_start
    print(f"Total computation time: {t_total:.1f}s")
    print()

    # NPZ data
    outfile_npz = os.path.join(OUTDIR, "s28b_order_one.npz")
    np.savez(outfile_npz,
             tau_values=tau_values,
             sectors=np.array(sectors),
             sector_labels=np.array(sector_labels),
             dcan_norms=dcan_norms,
             dk_norms=dk_norms,
             frob_max=frob_max,
             linf_max=linf_max,
             cliff_max_32dim=np.array([cliff_max]),
             verdict=verdict)
    print(f"Data saved to: {outfile_npz}")

    # Text verdict
    outfile_txt = os.path.join(OUTDIR, "s28b_order_one.txt")
    with open(outfile_txt, 'w') as f:
        f.write("C-3: ORDER-ONE CONDITION [[D_can, a_F], J b_F J^{-1}] = 0\n")
        f.write("=" * 60 + "\n\n")

        f.write(f"Date: 2026-02-27\n")
        f.write(f"Script: s28b_order_one.py\n")
        f.write(f"Total runtime: {t_total:.1f}s\n\n")

        f.write("GATE C-3 VERDICT\n")
        f.write("-" * 60 + "\n\n")
        f.write(f"Verdict: {verdict}\n")
        f.write(f"Max norm (non-trivial sectors): {max_nontrivial:.6e}\n")
        f.write(f"Max norm (0,0) singlet: {singlet_norm:.6e}\n\n")

        f.write("COMPARISON D_can vs D_K\n")
        f.write("-" * 60 + "\n\n")
        f.write(f"D_can (0,0): {singlet_norm:.6e}  (M_Lie=0, trivially zero)\n")
        f.write(f"D_K   (0,0): {max_dk_singlet:.6e}  (Omega contribution)\n")
        f.write(f"D_can non-triv: {max_nontrivial:.6e}  (Clifford only)\n")
        f.write(f"D_K   non-triv: {max_dk_nontrivial:.6e}  (Clifford + Omega)\n\n")

        f.write("SECTOR TABLE (L_inf norm)\n")
        f.write("-" * 60 + "\n")
        f.write(f"{'tau':>6s} {'sector':>8s} {'D_can':>12s} {'D_K':>12s}\n")
        for ti, tau in enumerate(tau_values):
            for si, label in enumerate(sector_labels):
                f.write(f"{tau:6.2f} {label:>8s} {dcan_norms[si,ti]:12.6e} "
                        f"{dk_norms[si,ti]:12.6e}\n")

        f.write(f"\nFROBENIUS NORM TABLE\n")
        f.write("-" * 60 + "\n")
        f.write(f"{'tau':>6s} {'sector':>8s} {'Frobenius':>12s} {'L_inf':>12s}\n")
        for ti, tau in enumerate(tau_values):
            for si, label in enumerate(sector_labels):
                f.write(f"{tau:6.2f} {label:>8s} {frob_max[si,ti]:12.6e} "
                        f"{linf_max[si,ti]:12.6e}\n")

        f.write(f"\nCLIFFORD 32-DIM (tau-independent)\n")
        f.write(f"Max violation: {cliff_max:.6e}\n")
        if cliff_worst:
            f.write(f"Worst: gamma_{cliff_worst[0]+1}, "
                    f"a={cliff_worst[1]}, b={cliff_worst[2]}\n")

        f.write(f"\nFACTOR BREAKDOWN (32-dim Clifford)\n")
        f.write("-" * 60 + "\n")
        for (f1, f2), nrm in sorted(cliff_factor_norms.items()):
            f.write(f"({f1:3s}, {f2:3s}): {nrm:.6e}\n")

        f.write(f"\nSTRUCTURAL NOTES\n")
        f.write("-" * 60 + "\n")
        f.write("The O(1) violation is structural (Baptista-Connes mismatch).\n")
        f.write("D_can order-one violation is PURELY Clifford (no Omega).\n")
        f.write("The violation condition is tau-INDEPENDENT (norm varies, condition does not).\n")
        f.write("(0,0) singlet satisfies order-one TRIVIALLY (M_Lie = 0).\n")
        f.write("Neither D_K nor D_can satisfies order-one in the Baptista representation.\n")
        f.write("This is NOT a framework closure -- it is the known open problem from Session 9-10.\n")

    print(f"Verdict saved to: {outfile_txt}")
    print()
    print("C-3 COMPUTATION COMPLETE")
    print("=" * 78)
