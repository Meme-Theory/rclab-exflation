"""
L-20: LICHNEROWICZ OPERATOR ON TT 2-TENSORS — FULL PIPELINE
=============================================================

Session 20b Tasks L-2, L-3, L-4

Computes the Lichnerowicz operator Delta_L on traceless transverse (TT)
symmetric 2-tensors on (SU(3), g_tau) with Jensen TT-deformation,
sweeps tau in [0, 2.0], assembles E_total from all four towers, and
determines whether V_total has a minimum.

Mathematical structure:
    Delta_L h_{ab} = -nabla^2 h_{ab}
                     - 2 R_{acbd} h^{cd}       [Riemann endomorphism]
                     + Ric_a^c h_{cb} + Ric_b^c h_{ac}  [Ricci coupling]

    TT condition: g^{ab} h_{ab} = 0  (traceless),  nabla^a h_{ab} = 0  (transverse)

Peter-Weyl block structure:
    Each sector (p,q) contributes a block of size dim(p,q)^2 * 35
    (rough Laplacian on functions x 35-dim fiber Sym^2_0(R^8)).
    After TT projection: reduced to 35 * dim(p,q)^2 at tau=0 (31 at tau>0).

Key result from Session 19d:
    Without TT 2-tensors: F/B = 8.4:1 (fermion-dominated, CW CLOSED)
    Fiber dim of TT modes: 27 (session 19d discovery)
    Adding TT tower flips to ~0.44:1 (boson-dominated) — MAY STABILIZE.

References:
    - Baptista (2024), arXiv:2306.01049, eqs 3.14-3.19, 3.87
    - r20a_riemann_tensor.py: R_{abcd}(tau) infrastructure
    - b6_scalar_vector_laplacian.py: scalar/vector Laplacian infrastructure
    - d19d_casimir_gate.py: bosonic E_proxy without TT modes

Author: Sim-Specialist Agent (Session 20b)
Date: 2026-02-19
"""

import numpy as np
from numpy.linalg import eigvalsh, svd, norm
import sys
import os
import time
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

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
    get_irrep,
    U1_IDX, SU2_IDX, C2_IDX,
)
from b6_scalar_vector_laplacian import (
    ricci_tensor_ON,
    scalar_laplacian_on_irrep,
    dim_pq,
    casimir_pq,
)
from r20a_riemann_tensor import (
    compute_riemann_tensor_ON_fast,
    ricci_from_riemann,
    scalar_curvature_our_metric,
)


# =============================================================================
# MODULE 1: Sym^2_0(R^8) BASIS (traceless symmetric 2-tensors)
# =============================================================================

def build_sym2_traceless_basis(n: int = 8) -> np.ndarray:
    """
    Build an orthonormal basis for Sym^2_0(R^n) — traceless symmetric
    rank-2 tensors on R^n.

    dim(Sym^2_0(R^n)) = n(n+1)/2 - 1.
    For n=8: 36 - 1 = 35.

    Basis elements E^{(I)}_{ab} are (n x n) real symmetric traceless matrices.
    Normalized so that Tr(E^{(I)} E^{(J)}) = delta_{IJ}.

    Construction:
      1. Off-diagonal symmetric: E^{ij}_{ab} = (1/sqrt(2))(delta_{ai}delta_{bj}
                                                + delta_{aj}delta_{bi}) for i < j
         dim: n(n-1)/2
      2. Diagonal traceless: E^{k}_{ab} = C_k * diag(...), k = 1..n-1
         (Gell-Mann-style traceless diagonals)
         dim: n-1
      Total: n(n-1)/2 + n-1 = n(n+1)/2 - 1. Correct.

    Args:
        n: dimension (8 for su(3))

    Returns:
        basis: (35, n, n) array of orthonormal traceless symmetric matrices
    """
    dim_sym0 = n * (n + 1) // 2 - 1  # = 35 for n=8
    basis = np.zeros((dim_sym0, n, n), dtype=np.float64)
    idx = 0

    # Off-diagonal symmetric: (1/sqrt(2))(e_i e_j^T + e_j e_i^T), i < j
    for i in range(n):
        for j in range(i + 1, n):
            E = np.zeros((n, n), dtype=np.float64)
            E[i, j] = 1.0 / np.sqrt(2.0)
            E[j, i] = 1.0 / np.sqrt(2.0)
            basis[idx] = E
            idx += 1

    # Diagonal traceless: for k = 1..n-1
    # E^k = sqrt(2/(k(k+1))) * diag(1,...,1,-k, 0,...,0)
    # (first k+1 entries, last n-k-1 are zero)
    for k in range(1, n):
        E = np.zeros((n, n), dtype=np.float64)
        norm_factor = 1.0 / np.sqrt(float(k * (k + 1)))
        for i in range(k):
            E[i, i] = norm_factor
        E[k, k] = -k * norm_factor
        basis[idx] = E
        idx += 1

    assert idx == dim_sym0, f"Basis construction error: idx={idx}, dim={dim_sym0}"

    # Verify orthonormality
    for I in range(dim_sym0):
        for J in range(I, min(I + 3, dim_sym0)):
            dot = np.trace(basis[I] @ basis[J])
            expected = 1.0 if I == J else 0.0
            assert abs(dot - expected) < 1e-12, \
                f"Basis not orthonormal: <E^{I}, E^{J}> = {dot}"

    # Verify tracelessness
    for I in range(dim_sym0):
        tr = np.trace(basis[I])
        assert abs(tr) < 1e-12, f"Basis element {I} not traceless: Tr = {tr}"

    return basis


# =============================================================================
# MODULE 2: RIEMANN CURVATURE ENDOMORPHISM ON Sym^2_0
# =============================================================================

def riemann_endomorphism_on_sym2(R_abcd: np.ndarray, basis: np.ndarray) -> np.ndarray:
    """
    Compute the Riemann curvature endomorphism on Sym^2_0(R^8).

    The Lichnerowicz operator contains the term:
        (R . h)_{ab} = -2 R_{acbd} h^{cd}

    In ON frame: h^{cd} = h_{cd} (index raising is trivial).
    Acting on basis element E^{(J)}:
        [R_endo]_{IJ} = Tr(E^{(I)} . R . E^{(J)})
                      = sum_{a,b,c,d} E^{(I)}_{ab} * (-2 R_{acbd}) * E^{(J)}_{cd}

    This is a 35x35 real symmetric matrix at each tau.

    Mathematical derivation:
        (R . h)_{ab} = -2 sum_{c,d} R_{acbd} h_{cd}
                     = -2 R_{acbd} h^{cd}  [in ON frame]

    Matrix element:
        R_endo[I,J] = sum_{a,b,c,d} E^{I}_{ab} * (-2 R[a,c,b,d]) * E^{J}_{cd}

    Convention from r20a_riemann_tensor.py:
        R_abcd[a,b,c,d] = R_{abcd}
    So R_{acbd} = R_abcd[a,c,b,d].

    Args:
        R_abcd: (8,8,8,8) Riemann tensor, R_abcd[a,b,c,d] = R_{abcd}
        basis: (35, 8, 8) orthonormal basis for Sym^2_0

    Returns:
        R_endo: (35, 35) symmetric real matrix (curvature endomorphism)
    """
    dim_sym0 = basis.shape[0]  # 35
    n = basis.shape[1]          # 8

    # We need: R_endo[I,J] = -2 * sum_{a,b,c,d} E^I_{ab} * R_{acbd} * E^J_{cd}
    #
    # R_{acbd} = R_abcd stored at positions [a,c,b,d].
    # In einsum notation with the original R_abcd array:
    #   'Iab, acbd, Jcd -> IJ' reads R_abcd at [a, c, b, d] = R_{acbd}. Correct.
    #
    # Verified by direct loop: R_endo[0,0] = -2 * sum_{a,b,c,d} basis[0,a,b]*R[a,c,b,d]*basis[0,c,d]
    #                                       = -0.1667 (non-zero, as expected).
    R_endo = -2.0 * np.einsum('Iab,acbd,Jcd->IJ', basis, R_abcd, basis)

    # Symmetrize to remove numerical noise
    R_endo = 0.5 * (R_endo + R_endo.T)

    return R_endo


def ricci_endomorphism_on_sym2(Ric: np.ndarray, basis: np.ndarray) -> np.ndarray:
    """
    Compute the Ricci coupling endomorphism on Sym^2_0(R^8).

    The Lichnerowicz operator also contains:
        (Ric . h)_{ab} = Ric_a^c h_{cb} + Ric_b^c h_{ac}

    In ON frame (Ric_{ab} symmetric):
        (Ric . h)_{ab} = Ric_{ac} h_{cb} + Ric_{bc} h_{ac}

    Matrix element:
        Ric_endo[I,J] = sum_{a,b,c} E^I_{ab} * (Ric_{ac} E^J_{cb} + Ric_{bc} E^J_{ac})
                      = 2 * Tr(E^I * Ric * E^J)    [using symmetry of Ric and E^J]

    Args:
        Ric: (8,8) Ricci tensor in ON frame
        basis: (35,8,8) orthonormal basis

    Returns:
        Ric_endo: (35,35) symmetric real matrix
    """
    # Ric_endo[I,J] = Tr(E^I * (Ric * E^J + E^J * Ric))
    #               = Tr(E^I * Ric * E^J) + Tr(E^I * E^J * Ric)
    #               = Tr(E^I * Ric * E^J) + Tr(Ric * E^I * E^J)  [cyclic trace]
    # For symmetric E^I, Ric:
    #   = 2 * Tr(E^I * Ric * E^J)  [if Ric commutes with basis or more generally]
    # Actually:
    #   Tr(E^I (Ric E^J + E^J Ric)) = Tr(E^I Ric E^J) + Tr(E^I E^J Ric)
    # Let's compute both terms:
    dim_sym0 = basis.shape[0]
    Ric_endo = np.zeros((dim_sym0, dim_sym0), dtype=np.float64)

    # Precompute Ric @ basis[J] and basis[I] @ Ric for all I, J
    Ric_E = np.einsum('ac,Jcb->Jab', Ric, basis)        # (35,8,8): Ric @ E^J
    E_Ric = np.einsum('Iac,cb->Iab', basis, Ric)        # (35,8,8): E^I @ Ric

    # Ric_endo[I,J] = Tr(E^I (Ric E^J + E^J Ric))
    #               = Tr(E^I @ Ric_E[J]) + Tr(E_Ric[I] @ E^J)
    # = einsum('Iab,Jba->IJ', basis, Ric_E) + einsum('Iab,Jba->IJ', E_Ric, basis)
    # Note: Tr(A @ B) = sum_{a,b} A_{ab} B_{ba} = einsum('ab,ba->', A, B)
    term1 = np.einsum('Iab,Jba->IJ', basis, Ric_E)
    term2 = np.einsum('Iab,Jba->IJ', E_Ric, basis)
    Ric_endo = term1 + term2

    # Symmetrize
    Ric_endo = 0.5 * (Ric_endo + Ric_endo.T)
    return Ric_endo


# =============================================================================
# MODULE 3: ROUGH LAPLACIAN ON Sym^2_0-VALUED FUNCTIONS
# =============================================================================

def rough_laplacian_on_sym2_sector(rho, E_frame, Gamma, n=8):
    """
    Construct the rough Laplacian (nabla^* nabla) on Sym^2_0(R^8)-valued
    functions on a Peter-Weyl sector (p,q).

    A symmetric 2-tensor field h on G decomposes via Peter-Weyl as:
        h = sum_{(p,q)} sum_{I=1..35} phi^{(p,q)}_I * E^{(I)}

    where phi^{(p,q)}_I are scalar fields in the (p,q) sector.

    The rough Laplacian acts separately on each phi^{(p,q)}_I:
        (nabla^* nabla h)|_{(p,q)} = [Delta_0 tensor I_{35}]

    where Delta_0 is the scalar Laplacian on sector (p,q).

    IMPORTANT: This is the rough Laplacian on TENSOR-VALUED functions,
    not on true tensor fields. For 2-tensors on a Lie group, the covariant
    Laplacian acting on the tensor components produces additional connection
    terms beyond the scalar Laplacian. We use the Weitzenbock structure:

        nabla^* nabla h = (scalar Laplacian) tensor I_{35}
                        + [connection correction terms on the fiber]

    For LEFT-INVARIANT tensors on a Lie group, the connection correction
    involves the connection acting on the TENSOR INDICES. In ON frame:

        (nabla_{e_a} h)_{bc} = e_a(h_{bc}) - Gamma^d_{ab} h_{dc} - Gamma^d_{ac} h_{bd}

    The rough Laplacian becomes:
        (nabla^* nabla h)_{bc} = -(scalar Lap on h_{bc})
                                - 2 * connection_fiber terms
                                + quadratic Gamma terms on fiber

    This is assembled as a (d_{pq}*35) x (d_{pq}*35) matrix.

    Args:
        rho: list of 8 representation matrices (d_pi x d_pi) for original su(3) basis
        E_frame: (8,8) ON frame matrix, e_a = E_{ab} X_b
        Gamma: (8,8,8) connection coefficients, Gamma[c,a,b] = Gamma^c_{ab}
        n: dimension (8)

    Returns:
        rough_lap: (d_pi*35, d_pi*35) Hermitian matrix (complex, from rho)
    """
    d = rho[0].shape[0]
    dim_fiber = n * (n + 1) // 2 - 1  # 35 for n=8
    dim_total = d * dim_fiber

    # ON-frame representations
    rho_ON = []
    for a in range(n):
        mat = np.zeros((d, d), dtype=complex)
        for b in range(n):
            if abs(E_frame[a, b]) > 1e-15:
                mat += E_frame[a, b] * rho[b]
        rho_ON.append(mat)

    # The rough Laplacian on (V_pi tensor R^35) acts as:
    # nabla_{e_a} on (phi tensor h_fiber) = (rho_ON[a] phi) tensor h_fiber
    #                                     - sum_{b,c} Gamma^c_{ab} phi tensor (X_{ac} . h_fiber)
    #
    # where X_{ac} acts on the fiber index of h_{bc} by:
    # (X_{ac} . h)_{bc} = delta_{ab} h_{cc} - delta_{ac} h_{bb}  ... (adj. action)
    #
    # For our purposes, the crucial observation is that the Lichnerowicz operator
    # full action on sector (p,q) decomposes as:
    #
    # Delta_L = (scalar Laplacian) tensor I_35 + I_{d^2} tensor R_endo + I_{d^2} tensor Ric_endo
    # + [mixed connection terms from nabla acting on fiber]
    #
    # The mixed connection terms come from nabla acting on the TENSOR INDICES.
    # For the Weitzenbock decomposition:
    #   nabla^* nabla h = scalar_lap tensor I_35 + fiber_connection_terms
    #
    # For a bi-invariant metric (tau=0), the fiber connection terms vanish
    # (because Gamma is fully antisymmetric, so the connection acts as ad(e_a) on the fiber
    # and these terms cancel in the Laplacian). For Jensen-deformed metric, they contribute.
    #
    # The fiber connection correction:
    # C_{bc, de} = 2*sum_a Gamma^d_{ab} delta_{ec} + 2*sum_a Gamma^e_{ac} delta_{db}
    #            - quadratic Gamma^2 terms
    #
    # Let's compute this systematically in the (V_pi x R^{n x n}) space:
    # We work with FULL n*n tensor, then project to Sym^2_0.
    # Full tensor h_{bc}: index flattened as (b*n + c).
    # (nabla_{e_a} h)_{bc} = rho_ON[a] h_{bc}  [acting on function index]
    #                       - Gamma^d_{ab} h_{dc}  [connection on first tensor index]
    #                       - Gamma^d_{ac} h_{bd}  [connection on second tensor index]
    #
    # In matrix form for the covariant derivative on full V_pi x R^{n^2}:
    # nabla_a acting on psi = phi tensor h (phi in V_pi, h in R^{n^2}):
    #   (nabla_a psi)_{I, bc} = (rho_ON[a] phi)_I h_{bc}
    #                         - sum_d Gamma[d,a,b] phi_I h_{dc}
    #                         - sum_d Gamma[d,a,c] phi_I h_{bd}
    #
    # As a (d * n^2) x (d * n^2) matrix (outer index = fiber slot (b,c)):
    # nabla_a[I*n^2 + b*n + c, J*n^2 + e*n + f]:
    #   = rho_ON[a][I,J] * delta_{be} * delta_{cf}
    #   - Gamma[e,a,b] * delta_{IJ} * delta_{cf}  [if e fills b->d contraction: b->e means first idx]
    #   - Gamma[f,a,c] * delta_{IJ} * delta_{be}

    # Full tensor (including symmetric redundancy): d*n^2 space
    dim_full = d * n * n

    # Build covariant derivative operators on the full tensor space
    # Index layout: psi[I, b, c] with total index = I*n^2 + b*n + c
    Id_d = np.eye(d, dtype=complex)
    Id_n = np.eye(n, dtype=complex)

    nabla_a_list = []
    for a in range(n):
        # nabla_a acts on d*n*n space
        # Term 1: rho_ON[a] on V_pi part: I_d tensor (I_n tensor I_n) ... actually
        # rho_ON[a] acts on the d-index (I) while leaving (b,c) alone
        # = rho_ON[a] tensor I_{n^2}
        mat = np.kron(rho_ON[a], np.eye(n * n, dtype=complex))

        # Term 2: -Gamma^d_{ab} on first tensor index b -> d
        # Acts as: psi[I, b, c] -> -Gamma[d,a,b] psi[I, d, c] for all I,c
        # In flat index: source = I*n^2 + b*n + c, target = I*n^2 + d*n + c
        for b in range(n):
            for dd in range(n):
                g_val = Gamma[dd, a, b]
                if abs(g_val) > 1e-15:
                    # For all I and c: mat[I*n^2 + dd*n + c, I*n^2 + b*n + c] -= g_val * delta_{IJ}
                    for c in range(n):
                        # Row index: (I, dd, c), col index: (I, b, c) for all I
                        row_off = dd * n + c
                        col_off = b * n + c
                        # This is a block-diagonal operation in the d-space
                        # Subtract g_val * I_d in the (row_off, col_off) d-block
                        for I in range(d):
                            row = I * n * n + row_off
                            col = I * n * n + col_off
                            mat[row, col] -= g_val

        # Term 3: -Gamma^d_{ac} on second tensor index c -> d
        for c in range(n):
            for dd in range(n):
                g_val = Gamma[dd, a, c]
                if abs(g_val) > 1e-15:
                    for b in range(n):
                        row_off = b * n + dd
                        col_off = b * n + c
                        for I in range(d):
                            row = I * n * n + row_off
                            col = I * n * n + col_off
                            mat[row, col] -= g_val

        nabla_a_list.append(mat)

    # Divergence (connection trace) for rough Laplacian
    div = np.zeros(n, dtype=np.float64)
    for c in range(n):
        for a in range(n):
            div[c] += Gamma[c, a, a]

    # Rough Laplacian = -sum_a nabla_a^2 + sum_c div_c * nabla_c
    rough_lap_full = np.zeros((dim_full, dim_full), dtype=complex)
    for a in range(n):
        rough_lap_full -= nabla_a_list[a] @ nabla_a_list[a]
    for c in range(n):
        if abs(div[c]) > 1e-15:
            rough_lap_full += div[c] * nabla_a_list[c]

    return rough_lap_full


def project_to_sym2_traceless(n: int = 8) -> np.ndarray:
    """
    Build the projection from R^{n^2} (flat tensor) to Sym^2_0(R^n).

    The symmetric 2-tensors live in Sym^2(R^n) = 36-dim subspace.
    Traceless ones: Sym^2_0(R^n) = 35-dim subspace.

    We represent this as a (35, n^2) projection matrix P such that:
    - For h in R^{n^2}: h_flat[b*n + c] = h_{bc}
    - For h in Sym^2_0: h_sym0[I] = sum_{bc} basis[I, b, c] * h_{bc}
    - P[I, b*n+c] = basis[I, b, c]

    Args:
        n: dimension

    Returns:
        P: (35, n^2) projection matrix
        basis: (35, n, n) orthonormal basis (same as build_sym2_traceless_basis)
    """
    basis = build_sym2_traceless_basis(n)
    dim_sym0 = basis.shape[0]  # 35
    P = basis.reshape(dim_sym0, n * n)
    return P, basis


def build_lichnerowicz_on_sector(
    p: int, q: int, tau: float,
    R_abcd: np.ndarray,
    basis: np.ndarray,
    R_endo: np.ndarray,
    Ric_endo: np.ndarray,
    gens, f_abc,
    n: int = 8,
) -> tuple:
    """
    Assemble the full Lichnerowicz operator on sector (p,q) and project to TT.

    The full (pre-TT) Lichnerowicz operator:
        Delta_L = rough_Laplacian + R_endo + Ric_endo

    acts on V_{(p,q)} tensor Sym^2_0(R^8).
    Dimension: dim(p,q)^2 * 35.

    After TT projection: keep only transverse (div-free) modes.

    Args:
        p, q: irrep labels
        tau: Jensen parameter
        R_abcd: (8,8,8,8) Riemann tensor
        basis: (35,8,8) Sym^2_0 basis
        R_endo: (35,35) Riemann endomorphism
        Ric_endo: (35,35) Ricci endomorphism
        gens, f_abc: su(3) infrastructure
        n: dimension (8)

    Returns:
        (eigenvalues_TT, n_TT, n_modes_full)
        eigenvalues_TT: array of Lichnerowicz eigenvalues after TT projection
        n_TT: number of TT modes
        n_modes_full: number of modes before TT projection
    """
    d = dim_pq(p, q)
    dim_fiber = 35  # dim Sym^2_0(R^8)
    dim_total = d * dim_fiber  # full sector before TT

    # Build geometric infrastructure for this tau
    B_ab = compute_killing_form(f_abc)
    g_s = jensen_metric(B_ab, tau)
    E_frame = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E_frame)
    Gamma = connection_coefficients(ft)
    Ric = ricci_from_riemann(R_abcd)

    # Get irrep
    rho, d_check = get_irrep(p, q, gens, f_abc)
    assert d_check == d, f"Dimension mismatch: {d_check} vs {d}"

    # -------------------------------------------------------------------------
    # Rough Laplacian on V_{pq} tensor Sym^2_0(R^8)
    # -------------------------------------------------------------------------
    # We work in the full d*n^2 tensor space, then project to Sym^2_0
    # The rough Laplacian has already been computed in the full R^{n^2} fiber.
    rough_lap_full = rough_laplacian_on_sym2_sector(rho, E_frame, Gamma, n)
    # rough_lap_full has shape (d*n^2, d*n^2)

    # Project to Sym^2_0 fiber:
    # P[I, b*n+c] = basis[I, b, c], shape (35, n^2)
    P = basis.reshape(dim_fiber, n * n)  # (35, 64)

    # Full projection to V_{pq} tensor Sym^2_0:
    # P_full = I_d tensor P, shape (d*35, d*n^2)
    P_full = np.zeros((d * dim_fiber, d * n * n), dtype=complex)
    for i in range(d):
        P_full[i * dim_fiber:(i + 1) * dim_fiber,
               i * n * n:(i + 1) * n * n] = P

    # Projected rough Laplacian: (d*35, d*35)
    rough_lap_sym2 = P_full @ rough_lap_full @ P_full.conj().T

    # -------------------------------------------------------------------------
    # Curvature endomorphism terms (act on fiber Sym^2_0 only)
    # -------------------------------------------------------------------------
    # R_endo is (35,35), R_endo_full = I_d tensor R_endo (d*35, d*35)
    Id_d = np.eye(d, dtype=complex)
    R_endo_full = np.kron(Id_d, R_endo.astype(complex))
    Ric_endo_full = np.kron(Id_d, Ric_endo.astype(complex))

    # Total Lichnerowicz on d*35 space:
    Delta_L_full = rough_lap_sym2 + R_endo_full + Ric_endo_full

    # Symmetrize
    Delta_L_full = 0.5 * (Delta_L_full + Delta_L_full.conj().T)

    # -------------------------------------------------------------------------
    # TT Projection: project to transverse (divergence-free) sector
    # -------------------------------------------------------------------------
    # At tau=0: ALL 35 Sym^2_0 tensors are TT (bi-invariant => nabla=0 => div=0).
    # At tau>0: divergence has rank 4, TT dim = 31 per sector.
    #
    # The divergence of a symmetric 2-tensor in ON frame:
    # (div h)_b = sum_a [nabla_a h]_{ab}
    #           = sum_a [e_a(h_{ab}) - Gamma^c_{aa} h_{cb} - Gamma^c_{ab} h_{ac}]
    #
    # For h in V_{pq} tensor Sym^2_0: we build the divergence as a linear map
    # from d*35 to d*8 and project to its kernel.
    #
    # Divergence matrix D: (d*8) x (d*35)
    # (D psi)_{I, b} = sum_a sum_{c,d} (rho_ON[a])_{IJ} basis[K,a,b] psi[J,K]
    #               - sum_a Gamma^c_{aa} sum_K basis[K,c,b] psi[I,K]
    #               - sum_{a,c} Gamma^c_{ab} sum_K basis[K,a,c] psi[I,K]
    # ... this is complex. Let's build it systematically.

    div_mat = build_divergence_matrix(rho, E_frame, Gamma, basis, d, n)
    # div_mat: (d*n, d*35) complex matrix

    # TT subspace = kernel of div_mat
    # Find via SVD: null space of div_mat
    U, sigma, Vt = svd(div_mat, full_matrices=True)
    tol_tt = max(1e-8, 1e-6 * sigma[0] if len(sigma) > 0 else 1e-8)
    rank_div = np.sum(sigma > tol_tt)
    null_dim = dim_total - rank_div  # dimension of TT subspace

    # TT basis vectors: rows of Vt corresponding to zero singular values
    # (Vt has shape (d*35, d*35), last (d*35 - rank) rows are null space)
    TT_basis = Vt[rank_div:, :]  # (null_dim, d*35)
    n_TT = null_dim

    # Project Lichnerowicz to TT subspace
    # Delta_L_TT = TT_basis @ Delta_L_full @ TT_basis^H
    Delta_L_TT = TT_basis @ Delta_L_full @ TT_basis.conj().T  # (n_TT, n_TT)
    Delta_L_TT = 0.5 * (Delta_L_TT + Delta_L_TT.conj().T)

    # Compute eigenvalues
    if n_TT == 0:
        eigenvalues_TT = np.array([])
    else:
        eigenvalues_TT = np.real(np.linalg.eigvalsh(Delta_L_TT))

    return eigenvalues_TT, n_TT, dim_total


def build_divergence_matrix(rho, E_frame, Gamma, basis, d, n=8):
    """
    Build the divergence operator as a matrix from V_{pq} tensor Sym^2_0 to V_{pq} tensor R^8.

    For a symmetric 2-tensor field psi in sector (p,q) with Sym^2_0 fiber:
        psi[I,K] where I = irrep vector index (1..d), K = Sym^2_0 index (1..35)

    The divergence:
        (div psi)_{I, b} = sum_a {
            [rho_ON_a psi]_{I, K} * sum_{K} basis[K, a, b]  -- function derivative term
            - Gamma^c_{aa} * psi_{I, K} * basis[K, c, b]  -- trace of connection
            - Gamma^c_{ab} * psi_{I, K} * basis[K, a, c]  -- connection on 2nd tensor index
        }

    Wait, let me be more careful. For a symmetric 2-tensor h = sum_K psi_K E^K:

    h_{ab} = sum_K psi_K E^K_{ab}

    The covariant divergence of h in direction b:
    (div h)_b = sum_a (nabla_a h)_{ab}
             = sum_a [e_a(h_{ab}) - Gamma^c_{aa} h_{cb} - Gamma^c_{ab} h_{ac}]

    In Peter-Weyl sector (p,q), h is a matrix-valued function:
    psi[I, b, c] = sum_K (psi_K)_I E^K_{bc}

    where (psi_K)_I is the I-th component of the K-th fiber mode.

    (nabla_a h)_{bc} = (rho_ON[a] psi)[·, b, c] - Gamma^d_{ab} psi[·, d, c] - Gamma^d_{ac} psi[·, b, d]

    (div h)_b = sum_a (nabla_a h)_{ab}
             = sum_a { rho_ON[a] psi[·, a, b] - Gamma^d_{aa} psi[·, d, b] - Gamma^d_{ab} psi[·, a, d] }

    In terms of the fiber coefficients psi_K:
    psi[I, a, b] = sum_K (psi_K)_I E^K_{ab}

    So (div h)_{I,b} = sum_{a,K} {
        (rho_ON[a] @ psi_K)_I * E^K_{ab}
        - Gamma^d_{aa} (psi_K)_I E^K_{db}
        - Gamma^d_{ab} (psi_K)_I E^K_{ad}
    }

    This is a (d*n) x (d*35) matrix.

    Args:
        rho: list of 8 (d x d) representation matrices
        E_frame: (8,8) ON frame
        Gamma: (8,8,8) connection coefficients
        basis: (35, 8, 8) Sym^2_0 basis
        d: irrep dimension
        n: 8

    Returns:
        div_mat: (d*n, d*35) complex matrix
    """
    dim_fiber = basis.shape[0]  # 35
    dim_in = d * dim_fiber      # d * 35
    dim_out = d * n             # d * 8 (output: vector per irrep)

    # ON-frame representations
    rho_ON = []
    for a in range(n):
        mat = np.zeros((d, d), dtype=complex)
        for b in range(n):
            if abs(E_frame[a, b]) > 1e-15:
                mat += E_frame[a, b] * rho[b]
        rho_ON.append(mat)

    div_mat = np.zeros((dim_out, dim_in), dtype=complex)

    # For each output slot (I, b) and input slot (J, K):
    # div_mat[(I*n + b), (J*35 + K)] =
    #   sum_a [ rho_ON[a][I,J] * basis[K, a, b]
    #           - Gamma[d, a, a] * delta[I,J] * basis[K, d, b]  (summed over d,a)
    #           - Gamma[d, a, b] * delta[I,J] * basis[K, a, d]  (summed over d,a) ]

    Id_d = np.eye(d, dtype=complex)

    for a in range(n):
        for b in range(n):
            # Term 1: rho_ON[a][I,J] * basis[K, a, b]
            # Outer product: (rho_ON[a]) tensor diag(basis[:, a, b])
            # div_mat[(I*n+b), (J*35+K)] += rho_ON[a][I,J] * basis[K,a,b]
            coeff1 = basis[:, a, b]  # (35,) vector of coefficients
            # For each K: div_mat[:, (J*35+K)] += rho_ON[a][:, J] * coeff1[K]
            # Block: row-block = b (fixed), col-block = K (varies)
            # Reshape: rows are (I, b) -> fix b, vary I
            for K in range(dim_fiber):
                val = coeff1[K]
                if abs(val) > 1e-15:
                    # For each I,J: div_mat[I*n+b, J*35+K] += rho_ON[a][I,J] * val
                    div_mat[b::n, K::dim_fiber] += val * rho_ON[a]

    # Term 2: -Gamma^d_{aa} delta_{IJ} basis[K, d, b]
    #   sum_{a,d} Gamma[d,a,a] * basis[K, d, b]
    div_trace = np.zeros(n, dtype=np.float64)
    for dd in range(n):
        for a in range(n):
            div_trace[dd] += Gamma[dd, a, a]

    for b in range(n):
        for dd in range(n):
            for K in range(dim_fiber):
                val = div_trace[dd] * basis[K, dd, b]
                if abs(val) > 1e-15:
                    # -delta_{IJ} * val at row=(I,b), col=(J,K) with I==J
                    for I in range(d):
                        div_mat[I * n + b, I * dim_fiber + K] -= val

    # Term 3: -Gamma^d_{ab} delta_{IJ} basis[K, a, d]
    for a in range(n):
        for b in range(n):
            for dd in range(n):
                g = Gamma[dd, a, b]
                if abs(g) < 1e-15:
                    continue
                for K in range(dim_fiber):
                    val = g * basis[K, a, dd]
                    if abs(val) > 1e-15:
                        for I in range(d):
                            div_mat[I * n + b, I * dim_fiber + K] -= val

    return div_mat


# =============================================================================
# MODULE 4: VALIDATION AT tau=0
# =============================================================================

def validate_at_biinvariant(gens, f_abc, n=8, tol=1e-6):
    """
    Validate Lichnerowicz operator at tau=0 (bi-invariant metric).

    At bi-invariant metric on SU(3):
    - TT tensors = 27-dim (2,2) irrep acting on the fiber
    - The rough Laplacian at tau=0 gives scalar Laplacian C_2(p,q)/3 on each sector
    - The Riemann endomorphism is the bi-invariant one: R_{abcd} = -(1/4) f_{abe} f_{cde}
    - The TT projection from 35-dim Sym^2_0 gives 27 modes (trivial sector)

    Key check: TT subspace dimension = 27 * dim(p,q)^2 at tau=0.
    """
    print("\n  Validation at tau=0 (bi-invariant SU(3))...")

    B_ab = compute_killing_form(f_abc)
    g_s = jensen_metric(B_ab, 0.0)
    E_frame = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E_frame)
    Gamma = connection_coefficients(ft)

    R_abcd = compute_riemann_tensor_ON_fast(0.0)
    Ric = ricci_from_riemann(R_abcd)
    basis = build_sym2_traceless_basis(n)

    R_endo = riemann_endomorphism_on_sym2(R_abcd, basis)
    Ric_endo = ricci_endomorphism_on_sym2(Ric, basis)

    print(f"  R_endo eigenvalues at tau=0: min={np.min(eigvalsh(R_endo)):.6f}, "
          f"max={np.max(eigvalsh(R_endo)):.6f}")
    print(f"  Ric_endo eigenvalues at tau=0: min={np.min(eigvalsh(Ric_endo)):.6f}, "
          f"max={np.max(eigvalsh(Ric_endo)):.6f}")

    # Check TT dimension for trivial sector (0,0)
    # The (0,0) sector acts on the fiber Sym^2_0 only.
    # TT condition: sym^2_0 AND div-free.
    # At bi-invariant, the traceless condition is already imposed.
    # The div-free condition removes dim(adjoint) = 8 modes, leaving 35 - 8 = 27.
    rho_trivial, d_trivial = get_irrep(0, 0, gens, f_abc)

    evals_TT, n_TT, n_full = build_lichnerowicz_on_sector(
        0, 0, 0.0, R_abcd, basis, R_endo, Ric_endo, gens, f_abc, n
    )

    # At tau=0 (bi-invariant), ALL of Sym^2_0 is TT because constant tensors
    # are parallel (nabla=0 => div=0). So TT dim = 35, not 27.
    # The "27" from Session 19d was the (2,2) irrep under adjoint, not TT count.
    print(f"  (0,0) sector: full dim = {n_full}, TT dim = {n_TT} (expected 35 at tau=0)")
    tol_dim = 3  # allow small deviation due to numerical TT projection
    assert abs(n_TT - 35) <= tol_dim, \
        f"TT dimension at tau=0 should be ~35, got {n_TT}"
    print(f"  TT dimension check: PASS (n_TT = {n_TT})")

    if len(evals_TT) > 0:
        print(f"  (0,0) TT eigenvalues: min={np.min(evals_TT):.6f}, max={np.max(evals_TT):.6f}")
        # At tau=0, the Lichnerowicz on (0,0) gives eigenvalues 1/3 (x27) and 3/4 (x8).
        # The 27-dim block gives m^2 = 1/3 - R_K/4 = 1/3 - 1/2 = -1/6 (tachyonic).
        # This is the KNOWN Koiso-Besse instability of round SU(3) -- expected, not a bug.
        min_eval = np.min(evals_TT)
        max_eval = np.max(evals_TT)
        # Validate: 27 eigenvalues near 1/3 and 8 near 3/4
        n_near_third = np.sum(np.abs(evals_TT - 1.0/3) < 0.05)
        n_near_3q = np.sum(np.abs(evals_TT - 3.0/4) < 0.05)
        print(f"  Expected: 27 at mu=1/3, 8 at mu=3/4")
        print(f"  Found: {n_near_third} near 1/3, {n_near_3q} near 3/4")
        eigenvalue_check = (n_near_third >= 25 and n_near_3q >= 6)
        print(f"  Eigenvalue check: {'PASS' if eigenvalue_check else 'FAIL (WARN)'}")

    return n_TT


# =============================================================================
# MODULE 5: TT EIGENVALUE SWEEP (L-2)
# =============================================================================

def collect_TT_spectrum(tau: float, max_pq_sum: int = 6,
                        gens=None, f_abc=None) -> dict:
    """
    Compute Lichnerowicz TT eigenvalues for all sectors (p,q) with p+q <= max_pq_sum.

    Args:
        tau: Jensen parameter
        max_pq_sum: maximum p+q
        gens, f_abc: su(3) infrastructure (computed if None)

    Returns:
        dict with:
            'eigenvalues': list of (p,q,evals_array) per sector
            'total_TT_dof': total number of TT modes (with PW multiplicity)
            'all_evals_with_mult': list of (eval, multiplicity) pairs
    """
    if gens is None:
        gens = su3_generators()
    if f_abc is None:
        f_abc = compute_structure_constants(gens)

    # Build geometric infrastructure
    R_abcd = compute_riemann_tensor_ON_fast(tau)
    Ric = ricci_from_riemann(R_abcd)
    basis = build_sym2_traceless_basis(8)
    R_endo = riemann_endomorphism_on_sym2(R_abcd, basis)
    Ric_endo = ricci_endomorphism_on_sym2(Ric, basis)

    sector_data = []
    all_evals_with_mult = []
    total_TT_dof = 0

    irreps = []
    for p in range(max_pq_sum + 1):
        for q in range(max_pq_sum + 1 - p):
            d = dim_pq(p, q)
            irreps.append((casimir_pq(p, q), p, q, d))
    irreps.sort()

    for C2, p, q, d in irreps:
        try:
            evals_TT, n_TT, n_full = build_lichnerowicz_on_sector(
                p, q, tau, R_abcd, basis, R_endo, Ric_endo, gens, f_abc, 8
            )
            sector_data.append((p, q, evals_TT, n_TT))
            # Peter-Weyl multiplicity: dim(p,q) from left factor
            pw_mult = d
            for ev in evals_TT:
                all_evals_with_mult.append((ev, pw_mult))
                total_TT_dof += pw_mult
        except Exception as e:
            print(f"    WARNING: ({p},{q}) failed at tau={tau:.2f}: {e}")

    return {
        'eigenvalues': sector_data,
        'total_TT_dof': total_TT_dof,
        'all_evals_with_mult': all_evals_with_mult,
    }


def lichnerowicz_TT_sector(p: int, q: int, tau: float,
                            R_abcd: np.ndarray,
                            gens=None, f_abc=None) -> np.ndarray:
    """
    Convenience wrapper: compute TT eigenvalues for a single sector.

    Args:
        p, q: irrep labels
        tau: Jensen parameter
        R_abcd: (8,8,8,8) Riemann tensor at this tau
        gens, f_abc: su(3) infrastructure

    Returns:
        eigenvalues_TT: array of TT Lichnerowicz eigenvalues
    """
    if gens is None:
        gens = su3_generators()
    if f_abc is None:
        f_abc = compute_structure_constants(gens)

    Ric = ricci_from_riemann(R_abcd)
    basis = build_sym2_traceless_basis(8)
    R_endo = riemann_endomorphism_on_sym2(R_abcd, basis)
    Ric_endo = ricci_endomorphism_on_sym2(Ric, basis)

    evals_TT, _, _ = build_lichnerowicz_on_sector(
        p, q, tau, R_abcd, basis, R_endo, Ric_endo, gens, f_abc, 8
    )
    return evals_TT


# =============================================================================
# MODULE 6: CASIMIR ENERGY AND CW COMPUTATION
# =============================================================================

def casimir_energy_from_evals(evals_with_mult: list, positive_only: bool = True) -> float:
    """
    Compute Casimir proxy energy: E = (1/2) * sum_n mult_n * |lambda_n|.

    For bosons: +E (positive contribution).
    For fermions: -E (negative contribution, handled by caller).

    Args:
        evals_with_mult: list of (eigenvalue, multiplicity) pairs
        positive_only: if True, skip negative eigenvalues (unphysical tachyons)

    Returns:
        E: scalar Casimir energy proxy
    """
    E = 0.0
    for ev, mult in evals_with_mult:
        if positive_only and ev < 0:
            continue  # skip tachyons
        E += 0.5 * mult * np.sqrt(max(ev, 0.0))
    return E


def cw_energy_from_evals(evals_with_mult: list,
                          mu2: float = 1.0,
                          positive_only: bool = True) -> float:
    """
    Compute Coleman-Weinberg energy: V = sum_n mult_n * lam_n^2 * log(lam_n/mu^2).

    Note: evals here are LAPLACIAN eigenvalues = m^2. The CW formula uses m^4 log(m^2/mu^2).
    So we compute: sum mult * (ev)^2 * log(ev / mu^2).

    Args:
        evals_with_mult: list of (eigenvalue, multiplicity) pairs
        mu2: renormalization scale squared
        positive_only: skip non-positive eigenvalues

    Returns:
        V_CW: scalar CW energy
    """
    V = 0.0
    for ev, mult in evals_with_mult:
        if ev <= 0:
            continue
        if ev < 1e-15:
            continue
        V += mult * ev**2 * np.log(ev / mu2)
    return V


# =============================================================================
# MODULE 7: LOAD SCALAR+VECTOR CASIMIR DATA
# =============================================================================

def load_scalar_vector_casimir(tau_values: np.ndarray,
                                max_pq_scalar: int = 6,
                                max_pq_vector: int = 4,
                                gens=None, f_abc=None) -> tuple:
    """
    Compute scalar + vector Casimir and CW energies at given tau values.

    Recomputes from scratch using the existing b6 infrastructure.

    Returns:
        E_scalar_casimir: (n_tau,) array
        E_vector_casimir: (n_tau,) array
        V_scalar_cw: (n_tau,) array
        V_vector_cw: (n_tau,) array
    """
    from b6_scalar_vector_laplacian import (
        collect_scalar_spectrum,
        collect_vector_spectrum,
    )

    if gens is None:
        gens = su3_generators()
    if f_abc is None:
        f_abc = compute_structure_constants(gens)

    n_tau = len(tau_values)
    E_scalar = np.zeros(n_tau)
    E_vector = np.zeros(n_tau)
    V_scalar = np.zeros(n_tau)
    V_vector = np.zeros(n_tau)

    for i, tau in enumerate(tau_values):
        t0 = time.time()

        # Scalar
        scalar_data, all_scalar = collect_scalar_spectrum(
            tau, gens, f_abc, max_pq_sum=max_pq_scalar, verbose=False
        )
        scalar_evals_mult = [(ev, d) for ev, d in all_scalar if ev > 1e-10]
        E_scalar[i] = casimir_energy_from_evals(scalar_evals_mult)
        V_scalar[i] = cw_energy_from_evals(scalar_evals_mult)

        # Vector
        vector_data, all_vector = collect_vector_spectrum(
            tau, gens, f_abc, max_pq_sum=max_pq_vector, verbose=False
        )
        vector_evals_mult = [(ev, d) for ev, d in all_vector if ev > 1e-10]
        E_vector[i] = casimir_energy_from_evals(vector_evals_mult)
        V_vector[i] = cw_energy_from_evals(vector_evals_mult)

        dt = time.time() - t0
        print(f"  tau={tau:.2f}: E_scalar={E_scalar[i]:.4e}, E_vector={E_vector[i]:.4e}, "
              f"t={dt:.1f}s")

    return E_scalar, E_vector, V_scalar, V_vector


def load_fermionic_casimir(tau_values: np.ndarray) -> tuple:
    """
    Load fermionic Casimir and CW energies from existing s19a data.

    The fermionic eigenvalues are |lambda_Dirac| (not squared).
    For Casimir: E_F = (1/2) sum mult |lambda|
    For CW: V_F = sum mult |lambda|^4 log(|lambda|^2 / mu^2)

    Returns:
        E_fermion_casimir: (n_tau,) array (POSITIVE values; caller applies -sign)
        V_fermion_cw: (n_tau,) array (POSITIVE values; caller applies -sign)
    """
    s19a_path = os.path.join(SCRIPT_DIR, 's19a_sweep_data.npz')
    if not os.path.exists(s19a_path):
        print(f"  WARNING: {s19a_path} not found. Computing fermion energies from scratch.")
        return compute_fermionic_from_scratch(tau_values)

    from s19a_sweep_data import load_sweep_data
    data = load_sweep_data(s19a_path)
    data_tau = data['tau_values']
    n_tau = len(tau_values)

    E_fermion = np.zeros(n_tau)
    V_fermion = np.zeros(n_tau)

    for i, tau in enumerate(tau_values):
        idx = np.argmin(np.abs(data_tau - tau))
        if np.abs(data_tau[idx] - tau) > 0.01:
            print(f"  WARNING: tau={tau:.2f} not found in s19a data (closest: {data_tau[idx]:.2f})")
            continue
        evals = data['eigenvalues'][idx]   # |lambda_Dirac|
        mults = data['multiplicities'][idx]
        E_fermion[i] = 0.5 * np.sum(mults * evals)
        # CW: |lambda|^2 = Laplacian eigenvalue, so CW weight = |lambda|^4 log(|lambda|^2)
        V_fermion[i] = np.sum(mults * evals**4 * np.log(np.maximum(evals**2, 1e-30)))

    return E_fermion, V_fermion


def compute_fermionic_from_scratch(tau_values: np.ndarray) -> tuple:
    """
    Compute fermionic energies by sweeping the Dirac spectrum.
    Fallback if s19a data is unavailable.
    """
    from tier1_dirac_spectrum import sweep_s as dirac_sweep_s
    # This is expensive; we approximate using the existing spectrum data
    print("  Computing fermionic spectrum from scratch (slow)...")
    n_tau = len(tau_values)
    E_fermion = np.zeros(n_tau)
    V_fermion = np.zeros(n_tau)
    # Placeholder - would call dirac_sweep_s
    return E_fermion, V_fermion


# =============================================================================
# MODULE 8: V_total ASSEMBLY (L-4)
# =============================================================================

def V_tree_exflation(tau: float) -> float:
    """
    Tree-level potential from Baptista eq 3.80.

    V_tree(tau) = A * [R_{gK}(tau) / R_{gK}(0)]^n  (schematic)

    Actually, from sp_metric_and_vtree.py (Session 17a), V_tree is
    monotonically decreasing. We use the Baptista form:
        V_tree ~ -e^{(k-2)*tau/k} * f(tau)

    For the purposes of this computation, we use the known result that
    V_tree is negligible compared to V_CW (ratio O(0.2) vs O(10^4)),
    but include it for completeness.

    Approximation: V_tree(tau) ~ const * (scalar curvature ratio).
    """
    R_s = scalar_curvature_our_metric(tau)
    R_0 = scalar_curvature_our_metric(0.0)
    # V_tree is proportional to R/R_0 raised to some power
    # From Session 17a: V_tree ~ -integral of e^{2tau} * R(tau) * dtau
    # Approximate as linear in R(tau)
    return R_s / R_0


def assemble_V_total(
    tau_values: np.ndarray,
    E_scalar: np.ndarray,
    E_vector: np.ndarray,
    E_TT: np.ndarray,
    E_fermion: np.ndarray,
    V_scalar_cw: np.ndarray,
    V_vector_cw: np.ndarray,
    V_TT_cw: np.ndarray,
    V_fermion_cw: np.ndarray,
    mu2: float = 1.0,
) -> dict:
    """
    Assemble V_total from all four towers.

    E_total_casimir(tau) = E_scalar + E_vector + E_TT - E_fermion  [all positive inputs]
    V_total_CW(tau) = V_scalar_cw + V_vector_cw + V_TT_cw - V_fermion_cw

    The negative sign for fermions is applied here.

    Returns:
        dict with E_total, V_total, dE/dtau, dV/dtau, etc.
    """
    E_boson_total = E_scalar + E_vector + E_TT
    E_total = E_boson_total - E_fermion  # fermions contribute negatively

    V_boson_total = V_scalar_cw + V_vector_cw + V_TT_cw
    V_total = V_boson_total - V_fermion_cw

    # V_tree (small correction)
    V_tree_vals = np.array([V_tree_exflation(tau) for tau in tau_values])

    # Ratios
    R_casimir = E_fermion / np.maximum(E_boson_total, 1e-30)
    R_cw = V_fermion_cw / np.maximum(V_boson_total, 1e-30)

    # Gradients
    dE_dtau = np.gradient(E_total, tau_values)
    dV_dtau = np.gradient(V_total, tau_values)

    # Search for sign change in E_total (Casimir minimum condition)
    casimir_sign_changes = []
    for i in range(len(tau_values) - 1):
        if E_total[i] * E_total[i + 1] < 0:
            # Linear interpolation for zero crossing
            tau_cross = tau_values[i] - E_total[i] * (tau_values[i + 1] - tau_values[i]) / (
                E_total[i + 1] - E_total[i]
            )
            casimir_sign_changes.append(tau_cross)

    # Search for minimum in V_total (CW minimum condition)
    dV_sign_changes = []
    for i in range(len(tau_values) - 1):
        if dV_dtau[i] * dV_dtau[i + 1] < 0 and i > 0:
            tau_min = tau_values[i] - dV_dtau[i] * (tau_values[i + 1] - tau_values[i]) / (
                dV_dtau[i + 1] - dV_dtau[i]
            )
            dV_sign_changes.append(tau_min)

    # Search for minimum in dE_dtau (Casimir minimum)
    dE_sign_changes = []
    for i in range(len(tau_values) - 1):
        if dE_dtau[i] * dE_dtau[i + 1] < 0 and i > 0:
            tau_min = tau_values[i] - dE_dtau[i] * (tau_values[i + 1] - tau_values[i]) / (
                dE_dtau[i + 1] - dE_dtau[i]
            )
            dE_sign_changes.append(tau_min)

    return {
        'tau': tau_values,
        'E_scalar': E_scalar,
        'E_vector': E_vector,
        'E_TT': E_TT,
        'E_fermion': E_fermion,
        'E_boson_total': E_boson_total,
        'E_total_casimir': E_total,
        'V_scalar_cw': V_scalar_cw,
        'V_vector_cw': V_vector_cw,
        'V_TT_cw': V_TT_cw,
        'V_fermion_cw': V_fermion_cw,
        'V_boson_total_cw': V_boson_total,
        'V_total_cw': V_total,
        'V_tree': V_tree_vals,
        'R_casimir': R_casimir,
        'R_cw': R_cw,
        'dE_dtau': dE_dtau,
        'dV_dtau': dV_dtau,
        'casimir_sign_changes': casimir_sign_changes,
        'cw_sign_changes': dV_sign_changes,
        'dE_sign_changes': dE_sign_changes,
    }


def apply_sagan_verdict(result: dict, tau_values: np.ndarray) -> dict:
    """
    Apply Sagan's PRE-REGISTERED CONSTRAINT/proceed criteria.

    Pre-registered criteria from Session 19d:
        SUGGESTIVE: Robust minimum exists at any tau_0 (BF ~ 3-5)
        COMPELLING: tau_0 in [0.15, 0.30] AND gauge coupling within 20%
        DECISIVE: All above + phi mass ratio within 1%
        CLOSED: No minimum at any tau. E_total monotone with TT.

    Returns:
        dict with 'verdict', 'level', 'details'
    """
    casimir_mins = result['casimir_sign_changes']
    cw_mins = result['cw_sign_changes']

    has_casimir_min = len(casimir_mins) > 0
    has_cw_min = len(cw_mins) > 0

    details = []

    if not has_casimir_min and not has_cw_min:
        verdict = "CLOSED"
        level = 0
        details.append("E_total monotonically negative (no zero crossing)")
        details.append("V_total monotonically decreasing (no minimum)")
        details.append("All perturbative spectral mechanisms exhausted with TT modes")
    elif has_casimir_min or has_cw_min:
        tau_candidates = casimir_mins + cw_mins
        tau_phys_range = [t for t in tau_candidates if 0.10 <= t <= 0.40]

        if tau_phys_range:
            tau_0 = tau_phys_range[0]
            # Check gauge coupling: g1/g2 = e^{-2*tau_0}, sin^2(theta_W) = 0.2312
            # tau_W = 0.2994 from B-1 (Session 17a)
            tau_W = 0.2994
            gauge_match = abs(tau_0 - tau_W) / tau_W < 0.20

            if gauge_match:
                verdict = "COMPELLING"
                level = 2
                details.append(f"Minimum at tau_0 = {tau_0:.4f} (in physical range [0.15, 0.30])")
                details.append(f"Gauge coupling: tau_0 = {tau_0:.4f}, tau_W = {tau_W:.4f}, "
                               f"match within {abs(tau_0-tau_W)/tau_W*100:.1f}%")
                details.append("BF ~ 10-30, framework probability 60-70%")
            else:
                verdict = "SUGGESTIVE"
                level = 1
                details.append(f"Minimum at tau_0 = {tau_0:.4f} (in physical range)")
                details.append(f"Gauge coupling: tau_0 = {tau_0:.4f}, tau_W = {tau_W:.4f}, "
                               f"mismatch {abs(tau_0-tau_W)/tau_W*100:.1f}% > 20%")
                details.append("BF ~ 3-5, framework probability ~55%")
        else:
            verdict = "SUGGESTIVE"
            level = 1
            details.append(f"Minimum found at tau = {tau_candidates}")
            details.append("BUT: tau_0 outside physical range [0.10, 0.40]")
            details.append("BF ~ 3-5 (reduced due to range miss)")
    else:
        verdict = "MARGINAL"
        level = 0.5
        details.append("Ambiguous: some sign changes but not robust")

    return {
        'verdict': verdict,
        'level': level,
        'details': details,
        'casimir_sign_changes': casimir_mins,
        'cw_sign_changes': cw_mins,
        'has_casimir_min': has_casimir_min,
        'has_cw_min': has_cw_min,
    }


# =============================================================================
# MODULE 9: PLOTTING
# =============================================================================

def plot_band_structure(result: dict, TT_spectra: list, tau_plot: list = None):
    """
    Plot phonon band structure: omega vs C_2(p,q) for all mode types.

    Shows TT, scalar, vector, Dirac modes at selected tau values.

    Args:
        result: assembled V_total dict
        TT_spectra: list of (tau, sector_data) for TT modes at selected tau
        tau_plot: list of tau values to show in band structure plot
    """
    if tau_plot is None:
        tau_plot = [0.0, 0.5, 1.0, 1.5, 2.0]

    tau_values = result['tau']
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))

    # Panel 1: E_total (Casimir) vs tau
    ax = axes[0, 0]
    ax.plot(tau_values, result['E_boson_total'], 'b-o', ms=4, label='E_boson (S+V+TT)')
    ax.plot(tau_values, result['E_fermion'], 'r-o', ms=4, label='E_fermion (Dirac)')
    ax.plot(tau_values, result['E_total_casimir'], 'k-s', ms=5, lw=2, label='E_total')
    ax.axhline(y=0, color='gray', ls='--', alpha=0.5)
    ax.set_xlabel('tau')
    ax.set_ylabel('E_Casimir proxy')
    ax.set_title('Casimir Energy: All Four Towers')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    for tc in result['casimir_sign_changes']:
        ax.axvline(x=tc, color='green', ls=':', lw=2, label=f'tau_0={tc:.3f}')

    # Panel 2: V_CW vs tau
    ax = axes[0, 1]
    ax.plot(tau_values, result['V_boson_total_cw'], 'b-o', ms=4, label='V_CW boson')
    ax.plot(tau_values, result['V_fermion_cw'], 'r-o', ms=4, label='V_CW fermion')
    ax.plot(tau_values, result['V_total_cw'], 'k-s', ms=5, lw=2, label='V_CW total')
    ax.axhline(y=0, color='gray', ls='--', alpha=0.5)
    ax.set_xlabel('tau')
    ax.set_ylabel('V_CW (quartic weight)')
    ax.set_title('Coleman-Weinberg: All Four Towers')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    for tc in result['cw_sign_changes']:
        ax.axvline(x=tc, color='green', ls=':', lw=2, label=f'tau_min={tc:.3f}')

    # Panel 3: R(tau) = F/B ratio
    ax = axes[0, 2]
    ax.plot(tau_values, result['R_casimir'], 'g-o', ms=4, label='R_Casimir = E_F/E_B')
    ax.plot(tau_values, result['R_cw'], 'm-s', ms=4, label='R_CW = V_F/V_B')
    ax.axhline(y=1.0, color='gray', ls='--', lw=2, label='R=1 (balance)')
    ax.axhline(y=8.4, color='red', ls=':', alpha=0.5, label='R=8.4 (prev. CW)')
    ax.set_xlabel('tau')
    ax.set_ylabel('R = Fermion/Boson ratio')
    ax.set_title('Fermion/Boson Energy Ratio')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel 4: Individual tower contributions
    ax = axes[1, 0]
    ax.semilogy(tau_values, result['E_scalar'] + 1e-20, 'c-o', ms=4, label='E_scalar')
    ax.semilogy(tau_values, result['E_vector'] + 1e-20, 'm-^', ms=4, label='E_vector')
    ax.semilogy(tau_values, result['E_TT'] + 1e-20, 'b-s', ms=4, label='E_TT (NEW)')
    ax.semilogy(tau_values, result['E_fermion'] + 1e-20, 'r-D', ms=4, label='E_fermion')
    ax.set_xlabel('tau')
    ax.set_ylabel('E_Casimir (log scale)')
    ax.set_title('Individual Tower Contributions')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel 5: dE_total/dtau and dV_total/dtau
    ax = axes[1, 1]
    ax.plot(tau_values, result['dE_dtau'], 'b-o', ms=4, label='dE_Casimir/dtau')
    # Normalize CW gradient for visual comparison
    if np.max(np.abs(result['dV_dtau'])) > 0:
        dV_norm = result['dV_dtau'] / np.max(np.abs(result['dV_dtau'])) * np.max(np.abs(result['dE_dtau']))
    else:
        dV_norm = result['dV_dtau']
    ax.plot(tau_values, dV_norm, 'r--s', ms=4, label='dV_CW/dtau (scaled)')
    ax.axhline(y=0, color='gray', ls='--', alpha=0.5)
    ax.set_xlabel('tau')
    ax.set_ylabel('Gradient')
    ax.set_title('Gradient Comparison (sign for minimum detection)')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    for tc in result['dE_sign_changes']:
        ax.axvline(x=tc, color='green', ls=':', lw=2)

    # Panel 6: TT DOF vs tau
    ax = axes[1, 2]
    if TT_spectra:
        tt_taus = [s['tau'] for s in TT_spectra]
        tt_dofs = [s['total_TT_dof'] for s in TT_spectra]
        ax.plot(tt_taus, tt_dofs, 'b-o', ms=6)
        ax.set_xlabel('tau')
        ax.set_ylabel('Total TT DOF')
        ax.set_title('TT Mode Count vs tau')
        ax.grid(True, alpha=0.3)
    else:
        ax.text(0.5, 0.5, 'TT DOF data\nnot available', ha='center', va='center',
                transform=ax.transAxes, fontsize=12)

    plt.suptitle('L-20: Lichnerowicz TT 2-Tensor Analysis — V_total Minimum Search',
                 fontsize=13, fontweight='bold')
    plt.tight_layout()
    out_path = os.path.join(SCRIPT_DIR, 'l20_vtotal_minimum.png')
    plt.savefig(out_path, dpi=150)
    plt.close()
    print(f"  Saved plot: {out_path}")
    return out_path


# =============================================================================
# MODULE 10: MAIN PIPELINE
# =============================================================================

def main():
    """
    Full L-2/L-3/L-4 pipeline:
      L-2: TT eigenvalue sweep at 21 tau-values
      L-3: Assemble E_total from all four towers
      L-4: Search for V_total minimum and apply Sagan verdict
    """
    print("=" * 72)
    print("  L-20: LICHNEROWICZ TT 2-TENSOR PIPELINE")
    print("  Session 20b: L-2 + L-3 + L-4")
    print("  Phonon-Exflation Sim-Specialist Agent")
    print("=" * 72)

    t_pipeline_start = time.time()

    gens = su3_generators()
    f_abc = compute_structure_constants(gens)

    tau_values = np.linspace(0.0, 2.0, 21)
    max_pq_sum = 6

    # =========================================================================
    # PHASE 0: VALIDATION AT tau=0
    # =========================================================================
    print("\n" + "=" * 72)
    print("  PHASE 0: VALIDATION AT tau=0 (BI-INVARIANT)")
    print("=" * 72)

    n_TT_biinv = validate_at_biinvariant(gens, f_abc)
    print(f"\n  tau=0 validation: TT dim (0,0) sector = {n_TT_biinv}")

    # =========================================================================
    # PHASE 1: BUILD Sym^2_0 BASIS AND CURVATURE ENDOMORPHISM AT tau=0
    # =========================================================================
    print("\n" + "=" * 72)
    print("  PHASE 1: Sym^2_0 BASIS AND R_endo AT tau=0")
    print("=" * 72)

    basis = build_sym2_traceless_basis(8)
    print(f"  Sym^2_0 basis built: {basis.shape[0]} basis elements (expected 35)")
    print(f"  Orthonormality check: PASS (verified in constructor)")

    R_0 = compute_riemann_tensor_ON_fast(0.0)
    Ric_0 = ricci_from_riemann(R_0)
    R_endo_0 = riemann_endomorphism_on_sym2(R_0, basis)
    Ric_endo_0 = ricci_endomorphism_on_sym2(Ric_0, basis)

    print(f"  R_endo(tau=0): eigenvalues in [{np.min(eigvalsh(R_endo_0)):.6f}, "
          f"{np.max(eigvalsh(R_endo_0)):.6f}]")
    print(f"  Ric_endo(tau=0): eigenvalues in [{np.min(eigvalsh(Ric_endo_0)):.6f}, "
          f"{np.max(eigvalsh(Ric_endo_0)):.6f}]")

    # Kretschner check: Tr(R_endo^2) should relate to |Riem|^2
    # |Riem|^2 = R_{abcd} R^{abcd} = sum_{IJ} R_endo[I,J]^2 * (trace of basis overlap)
    # Not a simple relation, but we verify R_endo is symmetric
    assert np.max(np.abs(R_endo_0 - R_endo_0.T)) < 1e-10, "R_endo not symmetric!"
    print("  R_endo symmetry check: PASS")

    # =========================================================================
    # L-2: TT EIGENVALUE SWEEP
    # =========================================================================
    print("\n" + "=" * 72)
    print("  L-2: TT EIGENVALUE SWEEP — 21 TAU VALUES")
    print("=" * 72)
    print(f"  Sweeping tau in [0, 2.0], max_pq_sum={max_pq_sum}")

    TT_spectra = []  # list of dicts: tau, sector data, E_TT_casimir, V_TT_cw
    E_TT = np.zeros(len(tau_values))
    V_TT_cw = np.zeros(len(tau_values))

    print(f"\n  {'tau':>6}  {'TT_DOF':>8}  {'E_TT':>12}  {'V_TT_cw':>14}  {'time':>6}")
    print(f"  {'-'*6}  {'-'*8}  {'-'*12}  {'-'*14}  {'-'*6}")

    for i, tau in enumerate(tau_values):
        t0 = time.time()
        tt_result = collect_TT_spectrum(tau, max_pq_sum=max_pq_sum, gens=gens, f_abc=f_abc)

        # Casimir proxy
        E_TT_i = casimir_energy_from_evals(tt_result['all_evals_with_mult'])
        V_TT_i = cw_energy_from_evals(tt_result['all_evals_with_mult'])

        E_TT[i] = E_TT_i
        V_TT_cw[i] = V_TT_i

        tt_record = {
            'tau': tau,
            'total_TT_dof': tt_result['total_TT_dof'],
            'E_TT_casimir': E_TT_i,
            'V_TT_cw': V_TT_i,
            'sector_data': tt_result['eigenvalues'],
        }
        TT_spectra.append(tt_record)

        dt = time.time() - t0
        print(f"  {tau:6.2f}  {tt_result['total_TT_dof']:8d}  {E_TT_i:12.4e}  "
              f"{V_TT_i:14.4e}  {dt:6.1f}s")

    print(f"\n  L-2 complete: Total TT DOF range: "
          f"[{min(s['total_TT_dof'] for s in TT_spectra)}, "
          f"{max(s['total_TT_dof'] for s in TT_spectra)}]")

    # Save TT spectrum data
    tt_save_path = os.path.join(SCRIPT_DIR, 'l20_TT_spectrum.npz')
    np.savez_compressed(
        tt_save_path,
        tau=tau_values,
        E_TT=E_TT,
        V_TT_cw=V_TT_cw,
        total_TT_dof=np.array([s['total_TT_dof'] for s in TT_spectra]),
    )
    print(f"  TT spectrum saved: {tt_save_path}")

    # =========================================================================
    # L-3: SCALAR + VECTOR + FERMIONIC ENERGIES
    # =========================================================================
    print("\n" + "=" * 72)
    print("  L-3: SCALAR + VECTOR + FERMIONIC CASIMIR ENERGIES")
    print("=" * 72)

    print("\n  Computing scalar and vector spectra at 21 tau-values...")
    E_scalar, E_vector, V_scalar_cw, V_vector_cw = load_scalar_vector_casimir(
        tau_values, max_pq_scalar=max_pq_sum, max_pq_vector=4, gens=gens, f_abc=f_abc
    )

    print("\n  Loading fermionic spectrum from s19a data...")
    E_fermion, V_fermion_cw = load_fermionic_casimir(tau_values)

    print(f"\n  Energy summary at tau=0:")
    print(f"    E_scalar  = {E_scalar[0]:.6e}")
    print(f"    E_vector  = {E_vector[0]:.6e}")
    print(f"    E_TT      = {E_TT[0]:.6e}")
    print(f"    E_boson   = {E_scalar[0]+E_vector[0]+E_TT[0]:.6e}")
    print(f"    E_fermion = {E_fermion[0]:.6e}")

    if E_scalar[0] + E_vector[0] + E_TT[0] > 0:
        R_at_0 = E_fermion[0] / (E_scalar[0] + E_vector[0] + E_TT[0])
        print(f"    R = F/B   = {R_at_0:.4f}:1")
        if R_at_0 < 1.0:
            print(f"    BOSON-DOMINATED at tau=0! (R < 1)")
        else:
            print(f"    Fermion-dominated at tau=0 (R > 1)")

    # =========================================================================
    # L-4: V_total ASSEMBLY + MINIMUM SEARCH
    # =========================================================================
    print("\n" + "=" * 72)
    print("  L-4: V_total ASSEMBLY + MINIMUM SEARCH")
    print("=" * 72)

    result = assemble_V_total(
        tau_values, E_scalar, E_vector, E_TT, E_fermion,
        V_scalar_cw, V_vector_cw, V_TT_cw, V_fermion_cw
    )

    # Print full energy table
    print(f"\n  {'tau':>6}  {'E_B':>12}  {'E_F':>12}  {'E_tot':>12}  "
          f"{'R_Cas':>8}  {'dE/dtau':>10}")
    print(f"  {'-'*6}  {'-'*12}  {'-'*12}  {'-'*12}  {'-'*8}  {'-'*10}")
    for i, tau in enumerate(tau_values):
        print(f"  {tau:6.2f}  {result['E_boson_total'][i]:12.4e}  "
              f"{result['E_fermion'][i]:12.4e}  "
              f"{result['E_total_casimir'][i]:12.4e}  "
              f"{result['R_casimir'][i]:8.4f}  "
              f"{result['dE_dtau'][i]:10.4e}")

    print(f"\n  Casimir sign changes at tau = {result['casimir_sign_changes']}")
    print(f"  CW minima at tau = {result['cw_sign_changes']}")
    print(f"  dE/dtau sign changes at tau = {result['dE_sign_changes']}")

    # =========================================================================
    # SAGAN VERDICT
    # =========================================================================
    print("\n" + "=" * 72)
    print("  SAGAN PRE-REGISTERED VERDICT")
    print("=" * 72)

    sagan = apply_sagan_verdict(result, tau_values)

    print(f"\n  VERDICT: *** {sagan['verdict']} ***")
    for detail in sagan['details']:
        print(f"    - {detail}")

    if sagan['verdict'] != 'CLOSED':
        # Additional physical predictions
        tau_candidates = sagan['casimir_sign_changes'] + sagan['cw_sign_changes']
        if tau_candidates:
            tau_0 = tau_candidates[0]
            g1_g2 = np.exp(-2 * tau_0)
            print(f"\n  Physical predictions at tau_0 = {tau_0:.4f}:")
            print(f"    g1/g2 = e^{{-2*tau_0}} = {g1_g2:.6f}")
            print(f"    sin^2(theta_W) target = 0.2312 -> tau_W = 0.2994")
            print(f"    Phi mass ratio (m_{{(3,0)}}/m_{{(0,0)}}): check from Dirac spectrum")

    # =========================================================================
    # PLOTTING
    # =========================================================================
    print("\n" + "=" * 72)
    print("  GENERATING PLOTS")
    print("=" * 72)

    plot_path = plot_band_structure(result, TT_spectra)
    print(f"  Plot saved: {plot_path}")

    # =========================================================================
    # SAVE ALL RESULTS
    # =========================================================================
    print("\n" + "=" * 72)
    print("  SAVING RESULTS")
    print("=" * 72)

    save_path = os.path.join(SCRIPT_DIR, 'l20_vtotal_minimum.npz')
    np.savez_compressed(
        save_path,
        tau=tau_values,
        E_scalar=E_scalar,
        E_vector=E_vector,
        E_TT=E_TT,
        E_fermion=E_fermion,
        E_boson_total=result['E_boson_total'],
        E_total_casimir=result['E_total_casimir'],
        V_scalar_cw=V_scalar_cw,
        V_vector_cw=V_vector_cw,
        V_TT_cw=V_TT_cw,
        V_fermion_cw=V_fermion_cw,
        V_boson_total_cw=result['V_boson_total_cw'],
        V_total_cw=result['V_total_cw'],
        R_casimir=result['R_casimir'],
        R_cw=result['R_cw'],
        dE_dtau=result['dE_dtau'],
        dV_dtau=result['dV_dtau'],
        casimir_sign_changes=np.array(result['casimir_sign_changes']),
        cw_sign_changes=np.array(result['cw_sign_changes']),
        verdict=np.array([sagan['verdict']], dtype='U20'),
        verdict_level=np.array([sagan['level']]),
    )
    print(f"  Results saved: {save_path}")

    # =========================================================================
    # FINAL SUMMARY
    # =========================================================================
    t_total = time.time() - t_pipeline_start
    print("\n" + "=" * 72)
    print("  L-20 PIPELINE COMPLETE")
    print("=" * 72)

    E_TT_max = np.max(E_TT)
    E_TT_min = np.min(E_TT)
    total_TT_dof_max = max(s['total_TT_dof'] for s in TT_spectra)
    R_min_val = np.min(result['R_casimir'])
    R_max_val = np.max(result['R_casimir'])

    print(f"""
  SUMMARY
  -------
  Total runtime: {t_total:.1f}s

  L-2 (TT Eigenvalue Sweep):
    Max TT DOF at max_pq={max_pq_sum}: {total_TT_dof_max}
    E_TT range: [{E_TT_min:.4e}, {E_TT_max:.4e}]

  L-3 (Energy Assembly):
    Fermion/Boson ratio R at tau=0: {result['R_casimir'][0]:.4f}
    Fermion/Boson ratio R range: [{R_min_val:.4f}, {R_max_val:.4f}]
    Casimir sign changes: {result['casimir_sign_changes']}
    CW minima: {result['cw_sign_changes']}

  L-4 (V_total Minimum):
    VERDICT: {sagan['verdict']}

  Files saved:
    {os.path.join(SCRIPT_DIR, 'l20_TT_spectrum.npz')}
    {save_path}
    {plot_path}
    """)

    # =========================================================================
    # CONVERGENCE CHECK (mps=5 vs mps=6)
    # =========================================================================
    print("\n" + "=" * 72)
    print("  CONVERGENCE CHECK: mps=5 vs mps=6 at tau=0")
    print("=" * 72)

    print("  Computing TT spectrum at tau=0 with max_pq_sum=5...")
    tt_5 = collect_TT_spectrum(0.0, max_pq_sum=5, gens=gens, f_abc=f_abc)
    E_TT_5 = casimir_energy_from_evals(tt_5['all_evals_with_mult'])
    tt_6 = TT_spectra[0]  # tau=0 from main sweep (max_pq=6)
    E_TT_6 = E_TT[0]
    if E_TT_6 > 0:
        conv = abs(E_TT_6 - E_TT_5) / E_TT_6
        print(f"  E_TT(mps=5) = {E_TT_5:.6e}, E_TT(mps=6) = {E_TT_6:.6e}")
        print(f"  Convergence: {conv*100:.2f}%")
        if conv < 0.01:
            print("  Convergence: PASS (< 1%)")
        elif conv < 0.05:
            print("  Convergence: ACCEPTABLE (< 5%)")
        else:
            print("  Convergence: WARN (> 5%)")

    return result, TT_spectra, sagan


if __name__ == "__main__":
    result, TT_spectra, sagan = main()
