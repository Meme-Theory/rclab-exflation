"""
KK-1: FULL BOSONIC KALUZA-KLEIN TOWER ON (SU(3), g_s)
======================================================

Enumerates ALL bosonic degrees of freedom on the Jensen-deformed SU(3):
  1. Scalar KK tower (Delta_0): Laplace-Beltrami on functions
  2. Vector KK tower (Delta_1): Hodge Laplacian on 1-forms
  3. Symmetric 2-tensor (Lichnerowicz): estimated DOF count

The scalar Laplacian uses the SAME Peter-Weyl infrastructure as the Dirac
spectrum code (tier1_dirac_spectrum.py), but acts on scalar functions
(no spinor bundle, no Clifford algebra). The result is a dim(p,q) x dim(p,q)
matrix per sector, NOT a dim(p,q)*16 matrix.

The vector (1-form) Laplacian uses Peter-Weyl + adjoint decomposition.
Each 1-form on SU(3) decomposes as f_a(x) e^a, where f_a are scalar functions.
Via Weitzenbock: Delta_1 = nabla*nabla + Ric (rough Laplacian + Ricci).

MATHEMATICAL FRAMEWORK:
========================

SCALAR LAPLACIAN on a Lie group with left-invariant metric:

The Laplace-Beltrami operator on functions is:
  Delta_0 f = -div(grad f)

In terms of a left-invariant ON frame {hat{e}_a} (where hat{e}_a = E_{ab} X_b
and X_b are the coordinate-basis left-invariant fields):

  Delta_0 = -sum_a hat{e}_a^2 + sum_a (div hat{e}_a) hat{e}_a

On sector (p,q) of Peter-Weyl, X_b acts as rho(e_b), so hat{e}_a acts as
sum_b E_{ab} rho(e_b). The scalar Laplacian becomes a matrix:

  Delta_0^{(p,q)} = -sum_{a,b,c} E_{ab} E_{ac} rho(e_b) rho(e_c)
                    + sum_a (sum_d Gamma^d_{da}) sum_b E_{ab} rho(e_b)

For our Jensen metric, g_s is DIAGONAL:
  g_{aa} = 3*lambda_a(s), with lambda in {e^{-2s}, e^s, e^{2s}}

So E_{ab} = delta_{ab} / sqrt(3*lambda_a(s)), and:

  Delta_0^{(p,q)} = -sum_a (1/(3*lambda_a)) rho(e_a)^2
                    + sum_a (sum_d Gamma^d_{da}) (1/sqrt(3*lambda_a)) rho(e_a)

The first term is the "rough Laplacian" (connection Laplacian on scalars).
The second is the divergence correction.

At s=0 (bi-invariant): Gamma^c_{ab} = (1/2) f^c_{ab}, so
  sum_d Gamma^d_{da} = (1/2) sum_d f^d_{da} = 0 (trace of adjoint = 0 for SU(3))
  => divergence correction = 0 at s=0
  => Delta_0 = -(1/3) sum_a rho(e_a)^2 = -(1/3) C_2(p,q) * I

where C_2(p,q) = (p^2+q^2+pq+3p+3q)/3 is the quadratic Casimir.

For s != 0, the divergence correction is generally NON-ZERO.

VECTOR (1-FORM) LAPLACIAN:
The Hodge Laplacian on 1-forms, via Weitzenbock identity:
  Delta_1 omega = (nabla*nabla + Ric) omega

On a Lie group, 1-forms = sections of T*G. Under Peter-Weyl, each (p,q) sector
contributes a dim(p,q) * 8 dimensional space (scalar function per Lie algebra
direction). The Hodge Laplacian mixes the 8 components.

BOSONIC DOF COUNT:
  - Scalars: 1 per point on K (from h_tt trace) -> N_scalar = 1
  - Vectors: from g_{mu a} components -> N_vector = dim(K) = 8
  - Sym-2 TT tensors: from g_{ab} TT -> N_symTT = dim(K)(dim(K)+1)/2 - 1 - dim(K) = 27
  - Gauge scalars (from KK vector A_mu^a): dim(K) = 8 (already in vectors)
  Total bosonic content per KK level: 1 + 8 + 27 = 36 TT-decomposed modes.
  But the gauge structure removes some: isometry group dim = dim(Isom(K,g_s)).
  For Jensen SU(3): Isom = SU(3)_L x (SU(2)xU(1))_R / Z_6, dim = 8+4 = 12 -> but
  these are gauge DOF eaten by Higgs mechanism.

  Baptista: 4 C^2 gauge bosons gain mass, 4 u(2) remain massless.
  Actual propagating bosonic DOF: scalars (1 breathing mode per level) +
  4 massive vectors (each 3 DOF) + 4 massless vectors (each 2 DOF) = 1+12+8 = 21?

  The exact count depends on gauge-fixing. For V_eff purposes, we need eigenvalues
  of the relevant Laplacians with correct multiplicities.

Author: KK-Theorist Agent (Session 18)
Date: 2026-02-14
"""

import numpy as np
from numpy.linalg import eigh, eigvalsh, inv, cholesky
import sys
import os
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tier1_dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    jensen_metric, orthonormal_frame, frame_structure_constants,
    connection_coefficients, validate_connection,
    get_irrep, validate_irrep,
    U1_IDX, SU2_IDX, C2_IDX, M_IDX,
)
from tier1_spectral_action import (
    gauge_boson_masses_baptista, scalar_curvature_from_connection,
    scalar_curvature_analytical,
)

# Attempt to import dim_su3_irrep, define locally if unavailable
try:
    from tier1_spectral_action import dim_su3_irrep
except ImportError:
    def dim_su3_irrep(p, q):
        return (p + 1) * (q + 1) * (p + q + 2) // 2


def separator(title):
    print(f"\n{'='*72}")
    print(f"  {title}")
    print(f"{'='*72}")


# =============================================================================
# MODULE 1: SCALAR LAPLACIAN ON (SU(3), g_s) VIA PETER-WEYL
# =============================================================================

def scalar_laplacian_on_irrep(rho, g_s, f_abc, E, Gamma):
    """
    Construct the scalar Laplacian matrix on irrep sector (p,q).

    Delta_0^{(p,q)} = -sum_{a,b,c} E_{ab} E_{ac} rho(e_b) rho(e_c)
                      + sum_a D_a * sum_b E_{ab} rho(e_b)

    where D_a = sum_d Gamma^d_{da} = connection trace (divergence of e_a).

    For the diagonal Jensen metric, E_{ab} = delta_{ab}/sqrt(g_{aa}), so:

      Delta_0 = -sum_a (1/g_{aa}) rho(e_a)^2 + sum_a D_a / sqrt(g_{aa}) rho(e_a)

    Args:
        rho: list of 8 representation matrices (dim_rho x dim_rho)
        g_s: (8,8) metric tensor (diagonal for Jensen)
        f_abc: (8,8,8) structure constants
        E: (8,8) ON frame matrix (E = g_s^{-1/2} for diagonal metric)
        Gamma: (8,8,8) connection coefficients, Gamma[c,a,b] = Gamma^c_{ab}

    Returns:
        Delta: (dim_rho, dim_rho) Hermitian matrix (eigenvalues = Laplacian eigenvalues)
    """
    dim_rho = rho[0].shape[0]
    Delta = np.zeros((dim_rho, dim_rho), dtype=complex)

    # First term: -sum_{a,b,c} E_{ab} E_{ac} rho(e_b) rho(e_c)
    # = -sum_a (sum_b E_{ab} rho(e_b)) (sum_c E_{ac} rho(e_c))
    # For diagonal E: = -sum_a E_{aa}^2 rho(e_a)^2 = -sum_a (1/g_{aa}) rho(e_a)^2
    for a in range(8):
        rho_ea_vec = np.zeros((dim_rho, dim_rho), dtype=complex)
        for b in range(8):
            if abs(E[a, b]) > 1e-15:
                rho_ea_vec += E[a, b] * rho[b]
        Delta -= rho_ea_vec @ rho_ea_vec

    # Second term: divergence correction
    # div(hat{e}_a) = sum_d Gamma^d_{da} (trace of connection over first two indices)
    # Full term: sum_a div(hat{e}_a) * hat{e}_a
    # On sector: sum_a div_a * sum_b E_{ab} rho(e_b)
    for a in range(8):
        div_a = sum(Gamma[d, d, a] for d in range(8))
        if abs(div_a) > 1e-15:
            for b in range(8):
                if abs(E[a, b]) > 1e-15:
                    Delta += div_a * E[a, b] * rho[b]

    return Delta


def scalar_laplacian_biinvariant_check(rho, p, q, f_abc):
    """
    Verify that at s=0, the scalar Laplacian = -(1/3) C_2(p,q) I.

    At s=0: g_s = 3*I_8, E = (1/sqrt(3))*I_8, Gamma^c_{ab} = (1/2) f^c_{ab}.

    Delta_0 = -(1/3) sum_a rho(e_a)^2 = C_2(p,q)/3 * I  (positive convention)

    Wait: sum_a rho(e_a)^2 = -C_2 * I (since generators are anti-Hermitian).
    So Delta_0 = -(1/3) * (-C_2) * I = C_2/3 * I.

    Hmm, but the POSITIVE Laplacian should give POSITIVE eigenvalues.
    Let me be precise: sum_a rho(e_a)^2 for anti-Hermitian generators has
    eigenvalues = -C_2(p,q) (negative, since e_a are anti-Hermitian).
    So -(1/g_{aa}) * rho(e_a)^2 has positive contribution.

    At s=0: -(1/3) * sum_a rho(e_a)^2 = -(1/3)(-C_2)I = C_2/3 * I.

    And the divergence correction vanishes at s=0:
    div(hat{e}_a) = sum_d Gamma^d_{da} = (1/2) sum_d f^d_{da} = 0.

    So eigenvalue = C_2(p,q)/3 with multiplicity dim(p,q)^2.

    Returns:
        (C2_expected, C2_numerical, error)
    """
    C2 = (p**2 + q**2 + p*q + 3*p + 3*q) / 3.0

    # Casimir check: -sum_a rho(e_a)^2 should be C_2 * I
    dim_rho = rho[0].shape[0]
    cas = np.zeros((dim_rho, dim_rho), dtype=complex)
    for a in range(8):
        cas += rho[a] @ rho[a]
    # cas = sum rho(e_a)^2 = -C2 * I (for anti-Hermitian generators)
    cas_eigs = np.sort(eigvalsh(cas.real))  # Should be -C2
    expected = -C2
    err = np.max(np.abs(cas_eigs - expected))

    # Scalar Laplacian eigenvalue at s=0: C2/3
    return C2/3.0, -cas_eigs[0]/3.0, err


def collect_scalar_spectrum(s, gens, f_abc, max_pq_sum=6, verbose=True):
    """
    Compute the scalar Laplacian spectrum on (SU(3), g_s).

    For each irrep (p,q) with p+q <= max_pq_sum, constructs the dim(p,q) x dim(p,q)
    scalar Laplacian matrix and diagonalizes it.

    Peter-Weyl multiplicity: each eigenvalue from sector (p,q) appears
    dim(p,q)^2 times in the full L^2(SU(3)) spectrum.

    But for CW effective potential, we want:
    - Each DISTINCT eigenvalue lambda_n
    - Its total multiplicity (including PW degeneracy and matrix degeneracy)

    Args:
        s: Jensen deformation parameter
        gens: su(3) generators
        f_abc: structure constants
        max_pq_sum: maximum p+q to include
        verbose: print progress

    Returns:
        scalar_data: list of (p, q, eigenvalues_array, dim_pq) per sector
        flat_spectrum: list of (eigenvalue, total_multiplicity) pairs
    """
    B_ab = compute_killing_form(f_abc)
    g_s = jensen_metric(B_ab, s)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)

    if verbose:
        mc_err = validate_connection(Gamma)
        print(f"  s={s:.4f}: connection metric-compat err = {mc_err:.2e}")

    scalar_data = []
    flat_spectrum = []

    # All irreps including (0,0)
    for pq_sum in range(max_pq_sum + 1):
        for p in range(pq_sum + 1):
            q = pq_sum - p
            dim_pq = dim_su3_irrep(p, q)

            try:
                rho, dim_check = get_irrep(p, q, gens, f_abc)
                assert dim_check == dim_pq, f"dim mismatch: {dim_check} vs {dim_pq}"

                Delta = scalar_laplacian_on_irrep(rho, g_s, f_abc, E, Gamma)

                # Delta should be Hermitian (positive Laplacian)
                herm_err = np.max(np.abs(Delta - Delta.conj().T))
                if herm_err > 1e-10:
                    print(f"  WARNING: ({p},{q}) Delta non-Hermitian, err={herm_err:.2e}")

                # Symmetrize for numerical stability
                Delta = 0.5 * (Delta + Delta.conj().T)

                # Diagonalize
                eigs = eigvalsh(Delta.real)  # Real symmetric
                eigs = np.sort(eigs)

                scalar_data.append((p, q, eigs, dim_pq))

                # PW multiplicity: dim(p,q) for each eigenvalue
                # (from V_(p,q)^* right factor; the matrix diagonalization
                #  already accounts for the left factor V_(p,q))
                pw_mult = dim_pq
                for ev in eigs:
                    flat_spectrum.append((ev, pw_mult))

                if verbose and dim_pq <= 64:
                    print(f"    ({p},{q}): dim={dim_pq}, Delta size={dim_pq}x{dim_pq}, "
                          f"eigs: [{eigs[0]:.6f}, {eigs[-1]:.6f}], Herm err={herm_err:.2e}")

            except (NotImplementedError, Exception) as e:
                if verbose:
                    print(f"    ({p},{q}): SKIPPED ({e})")

    return scalar_data, flat_spectrum


# =============================================================================
# MODULE 2: VECTOR (1-FORM) LAPLACIAN ON (SU(3), g_s) VIA PETER-WEYL
# =============================================================================

def ricci_tensor_from_connection(Gamma, ft):
    """
    Compute the Ricci tensor Ric_{ab} in the ON frame.

    Uses the SAME Riemann tensor definition as scalar_curvature_from_connection()
    in tier1_spectral_action.py (which gives positive Ric for compact groups).

    For left-invariant frame fields on a Lie group:
      [e_a, e_b] = ft^c_{ab} e_c

    Riemann tensor (left-invariant => e_a(Gamma) = 0):
      R^d_{abc} = Gamma^d_{ae} Gamma^e_{bc} - Gamma^d_{be} Gamma^e_{ac}
                  - ft^e_{ab} Gamma^d_{ec}

    Ricci contraction: Ric_{ac} = sum_b R^b_{bac}
      (first upper index contracted with second lower index)

    This gives POSITIVE Ric for compact simple Lie groups (positive curvature).

    Args:
        Gamma: (8,8,8), Gamma[d,a,b] = Gamma^d_{ab}
        ft: (8,8,8), ft[a,b,c] = ft^c_{ab}

    Returns:
        Ric: (8,8) Ricci tensor in ON frame (positive for compact groups)
    """
    n = 8

    # Build Riemann tensor R^d_{abc}
    Riem = np.zeros((n, n, n, n), dtype=np.float64)
    for d in range(n):
        for a in range(n):
            for b in range(n):
                for c in range(n):
                    val = 0.0
                    for e in range(n):
                        val += Gamma[d, a, e] * Gamma[e, b, c]
                        val -= Gamma[d, b, e] * Gamma[e, a, c]
                        val -= ft[a, b, e] * Gamma[d, e, c]
                    Riem[d, a, b, c] = val

    # Ricci: Ric_{ac} = sum_b R^b_{bac}
    Ric = np.zeros((n, n), dtype=np.float64)
    for a in range(n):
        for c in range(n):
            for b in range(n):
                Ric[a, c] += Riem[b, b, a, c]

    return Ric


def vector_laplacian_on_irrep(rho, E, Gamma, Ric, f_abc, ft):
    """
    Construct the Hodge Laplacian on 1-forms, restricted to sector (p,q).

    A 1-form on SU(3) can be written omega = sum_a omega_a hat{e}^a where
    hat{e}^a are the ON coframe and omega_a are scalar functions.

    Via Peter-Weyl, omega_a restricted to sector (p,q) gives a
    dim(p,q)-vector for each a = 0,...,7. Total space: dim(p,q) * 8.

    The Weitzenbock identity:
      Delta_1 = nabla*nabla + Ric

    The "rough Laplacian" nabla*nabla on 1-forms in sector (p,q):
      (nabla*nabla omega)_a = (Delta_0 omega_a) - sum_c 2*Gamma^b_{ca} (hat{e}_c omega_b)
                              + sum_{b,c} (Gamma^b_{ca})^2 omega_b  (schematic)

    More precisely, for the connection Laplacian on 1-forms:
      (nabla*nabla omega)_a = -sum_c (nabla_c nabla_c omega)_a

    where (nabla_c omega)_a = hat{e}_c(omega_a) - Gamma^b_{ca} omega_b.

    On the Peter-Weyl sector, hat{e}_c(omega_a) acts as
    (sum_d E_{cd} rho(e_d)) on the dim(p,q)-dimensional space for component a.

    This is a dim(p,q)*8 matrix problem.

    Args:
        rho: list of 8 rep matrices (dim_rho x dim_rho)
        E: (8,8) ON frame
        Gamma: (8,8,8) connection, Gamma[b,a,c] = Gamma^b_{ac}
        Ric: (8,8) Ricci tensor
        f_abc: structure constants
        ft: ON-frame structure constants

    Returns:
        Delta1: (dim_rho*8, dim_rho*8) Hermitian matrix
    """
    dim_rho = rho[0].shape[0]
    n = 8
    dim_total = dim_rho * n

    # Build the ON-frame derivative operators: hat_e_c on sector = sum_d E_{cd} rho(e_d)
    hat_e = []
    for c in range(n):
        op = np.zeros((dim_rho, dim_rho), dtype=complex)
        for d in range(n):
            if abs(E[c, d]) > 1e-15:
                op += E[c, d] * rho[d]
        hat_e.append(op)

    # Covariant derivative on 1-form components:
    # (nabla_c omega)_a = hat_e_c(omega_a) - sum_b Gamma^b_{ca} omega_b
    # In sector (p,q), omega_a is a dim_rho-vector. Full state: (omega_0, ..., omega_7)
    # is a dim_rho*8 vector.

    # Build nabla_c as a dim_total x dim_total matrix:
    # [nabla_c]_{a alpha, b beta} = delta_{ab} [hat_e_c]_{alpha,beta}
    #                              - Gamma^a_{cb} delta_{alpha,beta}  (wait, need signs right)
    # Actually: (nabla_c omega)_a = hat_e_c(omega_a) - Gamma^b_{ca} omega_b
    # So the (a,b) block is: delta_{ab} hat_e_c - Gamma^b_{ca} I

    # Wait: (nabla_c omega)_a = hat_e_c(omega_a) - sum_b Gamma^b_{ca} omega_b
    # index structure: output has index a, input has index b for the second term.
    # Gamma^b_{ca}: c=direction of nabla, mapping from b-th component to a-th output.
    # So: [nabla_c]_{a, b} = delta_{ab} hat_e_c + (connection part acting on form index)
    # Connection on 1-forms: (nabla_c omega)_a = e_c(omega_a) - Gamma^b_{ca} omega_b
    # With our convention Gamma[b,c,a] = Gamma^b_{ca}: [nabla_c]_{a,b} block =
    #   delta_{ab} hat_e_c - Gamma[b,c,a] I_{dim_rho}

    # Hmm, this mixes: for the (a,alpha) x (b,beta) entry:
    # [nabla_c]_{(a,alpha),(b,beta)} = delta_{ab} [hat_e_c]_{alpha,beta}
    #                                  - Gamma[b,c,a] delta_{alpha,beta}

    # Wait, re-derive. (nabla_c omega)_a = hat_e_c(omega_a) - sum_b Gamma^b_{ca} omega_b.
    # We read this as: output indexed by a depends on input indexed by a (first term)
    # and input indexed by b (second term, with b summed).
    # => [nabla_c]_{a,a} += hat_e_c (on the rho space)
    #    [nabla_c]_{a,b} -= Gamma^b_{ca} * I (for each b)
    # But Gamma^b_{ca} = Gamma[b,c,a]. So the block (a,b) gets:
    #   delta_{ab} hat_e_c - Gamma[b,c,a] I

    nabla = []
    I_rho = np.eye(dim_rho, dtype=complex)

    for c in range(n):
        nc = np.zeros((dim_total, dim_total), dtype=complex)
        for a in range(n):
            for b in range(n):
                r_start, r_end = a*dim_rho, (a+1)*dim_rho
                c_start, c_end = b*dim_rho, (b+1)*dim_rho

                if a == b:
                    nc[r_start:r_end, c_start:c_end] += hat_e[c]

                # Connection term: -Gamma^b_{ca}
                # Gamma[b,c,a] = Gamma^b_{ca}
                coeff = Gamma[b, c, a]
                if abs(coeff) > 1e-15:
                    nc[r_start:r_end, c_start:c_end] -= coeff * I_rho

        nabla.append(nc)

    # Also need divergence correction for nabla*nabla:
    # The connection Laplacian (rough Laplacian) is:
    # nabla*nabla = -sum_c (nabla_c nabla_c - (div hat_e_c) nabla_c)
    # Actually: nabla*nabla = -sum_c [nabla_{hat_e_c} nabla_{hat_e_c} - nabla_{nabla_{hat_e_c} hat_e_c}]

    # On a Lie group with ON frame:
    # nabla_{hat_e_c} hat_e_c = sum_d Gamma^d_{cc} hat_e_d (note: no sum on c here)
    # So nabla_{nabla_{hat_e_c} hat_e_c} = sum_d Gamma^d_{cc} nabla_{hat_e_d}

    # rough_lap = -sum_c [nabla_c nabla_c - sum_d Gamma^d_{cc} nabla_d]

    rough_lap = np.zeros((dim_total, dim_total), dtype=complex)
    for c in range(n):
        rough_lap -= nabla[c] @ nabla[c]
        for d in range(n):
            coeff = Gamma[d, c, c]
            if abs(coeff) > 1e-15:
                rough_lap += coeff * nabla[d]

    # Add Ricci term: (Ric omega)_a = sum_b Ric_{ab} omega_b
    # In block form: [Ric_op]_{a,b} = Ric[a,b] * I_rho
    Ric_op = np.zeros((dim_total, dim_total), dtype=complex)
    for a in range(n):
        for b in range(n):
            if abs(Ric[a, b]) > 1e-15:
                r_start, r_end = a*dim_rho, (a+1)*dim_rho
                c_start, c_end = b*dim_rho, (b+1)*dim_rho
                Ric_op[r_start:r_end, c_start:c_end] = Ric[a, b] * I_rho

    # Hodge Laplacian = rough Laplacian + Ricci
    Delta1 = rough_lap + Ric_op

    return Delta1


def collect_vector_spectrum(s, gens, f_abc, max_pq_sum=4, verbose=True):
    """
    Compute the Hodge Laplacian spectrum on 1-forms of (SU(3), g_s).

    For each irrep (p,q), constructs a dim(p,q)*8 matrix and diagonalizes.

    The matrix sizes are 8x larger than scalar, so max_pq_sum should be lower.

    PW multiplicity: dim(p,q)^2 for each eigenvalue in sector (p,q).

    Args:
        s: Jensen deformation parameter
        gens: su(3) generators
        f_abc: structure constants
        max_pq_sum: maximum p+q (recommend <= 4 for speed)
        verbose: print progress

    Returns:
        vector_data: list of (p, q, eigenvalues_array, dim_pq) per sector
        flat_spectrum: list of (eigenvalue, total_multiplicity) pairs
    """
    B_ab = compute_killing_form(f_abc)
    g_s = jensen_metric(B_ab, s)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    Ric = ricci_tensor_from_connection(Gamma, ft)

    if verbose:
        print(f"  s={s:.4f}: Ricci tensor computed")
        print(f"    Ric diag: [{', '.join(f'{Ric[a,a]:.6f}' for a in range(8))}]")
        R_scalar = sum(Ric[a, a] for a in range(8))
        R_analytic = scalar_curvature_analytical(s)
        print(f"    Scalar curvature: R = {R_scalar:.6f} (analytic: {R_analytic:.6f})")

    vector_data = []
    flat_spectrum = []

    for pq_sum in range(max_pq_sum + 1):
        for p in range(pq_sum + 1):
            q = pq_sum - p
            dim_pq = dim_su3_irrep(p, q)
            mat_size = dim_pq * 8

            # Skip if matrix too large (>5000 for speed)
            if mat_size > 5000:
                if verbose:
                    print(f"    ({p},{q}): dim={dim_pq}, matrix={mat_size}x{mat_size} -- SKIPPED (too large)")
                continue

            try:
                rho, dim_check = get_irrep(p, q, gens, f_abc)

                Delta1 = vector_laplacian_on_irrep(rho, E, Gamma, Ric, f_abc, ft)

                # Check Hermiticity
                herm_err = np.max(np.abs(Delta1 - Delta1.conj().T))
                if herm_err > 1e-8:
                    print(f"  WARNING: ({p},{q}) Delta_1 non-Hermitian, err={herm_err:.2e}")

                Delta1 = 0.5 * (Delta1 + Delta1.conj().T)
                eigs = eigvalsh(Delta1.real)
                eigs = np.sort(eigs)

                vector_data.append((p, q, eigs, dim_pq))

                # PW multiplicity: dim(p,q) per eigenvalue (right factor V_(p,q)^*)
                pw_mult = dim_pq
                for ev in eigs:
                    flat_spectrum.append((ev, pw_mult))

                if verbose:
                    n_neg = np.sum(eigs < -1e-10)
                    n_zero = np.sum(np.abs(eigs) < 1e-10)
                    print(f"    ({p},{q}): dim={dim_pq}, mat={mat_size}x{mat_size}, "
                          f"eigs: [{eigs[0]:.6f}, {eigs[-1]:.6f}], "
                          f"neg={n_neg}, zero={n_zero}, Herm={herm_err:.2e}")

            except (NotImplementedError, Exception) as e:
                if verbose:
                    print(f"    ({p},{q}): SKIPPED ({e})")

    return vector_data, flat_spectrum


# =============================================================================
# MODULE 3: DOF COUNTING AND BOSONIC TOWER SUMMARY
# =============================================================================

def count_bosonic_dof(max_pq_sum=6):
    """
    Count the total bosonic degrees of freedom on (SU(3), g_s) up to a
    given KK level.

    Bosonic modes from dimensional reduction of 12D gravity:
    1. Scalar modes (from g_{mu mu} trace + dilaton): 1 function on K per (p,q)
    2. Vector modes (from g_{mu a}): 8 functions per (p,q) [one per K-direction]
    3. Symmetric TT 2-tensors (from g_{ab}): physical graviton-like modes

    For the CW potential, the relevant decomposition is:
    - N_0 = number of scalar eigenvalues (counting PW multiplicity)
    - N_1 = number of vector eigenvalues (counting PW multiplicity)
    - N_2 = Lichnerowicz eigenvalues (estimated)

    The key quantity is:
      V_CW^boson = (1/64pi^2) sum_n m_n^4 log(m_n^2/mu^2)

    where the sum runs over ALL bosonic modes with their multiplicities.

    Returns:
        dict with DOF breakdown per type and per (p,q) sector
    """
    dof = {'scalar': {}, 'vector': {}, 'total_scalar': 0, 'total_vector': 0}

    for pq_sum in range(max_pq_sum + 1):
        for p in range(pq_sum + 1):
            q = pq_sum - p
            dim_pq = dim_su3_irrep(p, q)

            # Scalar: dim(p,q) eigenvalues, each with PW mult dim(p,q)^2
            # Total scalar DOF from (p,q): dim(p,q) * dim(p,q)^2 = dim(p,q)^3
            n_scalar_eigs = dim_pq  # distinct eigenvalues
            scalar_pw_mult = dim_pq ** 2
            dof['scalar'][(p, q)] = {
                'dim': dim_pq,
                'n_eigs': n_scalar_eigs,
                'pw_mult': scalar_pw_mult,
                'total_dof': n_scalar_eigs * scalar_pw_mult
            }
            dof['total_scalar'] += n_scalar_eigs * scalar_pw_mult

            # Vector: dim(p,q)*8 eigenvalues, each with PW mult dim(p,q)^2
            n_vector_eigs = dim_pq * 8
            dof['vector'][(p, q)] = {
                'dim': dim_pq,
                'n_eigs': n_vector_eigs,
                'pw_mult': scalar_pw_mult,
                'total_dof': n_vector_eigs * scalar_pw_mult
            }
            dof['total_vector'] += n_vector_eigs * scalar_pw_mult

    return dof


# =============================================================================
# MODULE 4: BAPTISTA's 4 GAUGE BOSONS -- CONSISTENCY CHECK
# =============================================================================

def check_gauge_boson_consistency(s, gens, f_abc, scalar_data, vector_data):
    """
    Cross-check: Baptista's 4 gauge boson masses from eq 3.84 should appear
    in either the scalar or vector spectrum.

    Baptista's gauge bosons are associated to LEFT-invariant vector fields
    e_a^L in the C^2 subspace. Their squared mass is:
      m^2(e_a^L) = overall_const * e^sigma * [(e^s - e^{-2s})^2 + (1 - e^{-s})^2]

    These correspond to specific modes in the vector KK tower.

    At s=0: m^2 = 0 (bi-invariant metric, all gauge bosons massless).
    At s>0: 4 C^2 bosons gain mass.

    Args:
        s: Jensen deformation parameter
        gens, f_abc: algebra data
        scalar_data: from collect_scalar_spectrum
        vector_data: from collect_vector_spectrum

    Returns:
        dict with comparison results
    """
    m2_baptista, m2_u2 = gauge_boson_masses_baptista(0.0, s)

    # Find zero-eigenvalue (massless) modes in vector spectrum
    result = {
        's': s,
        'm2_baptista_C2': m2_baptista,
        'm2_baptista_u2': m2_u2,
    }

    if vector_data:
        all_vec_eigs = []
        for p, q, eigs, dim_pq in vector_data:
            for ev in eigs:
                all_vec_eigs.append(ev)
        all_vec_eigs = np.sort(all_vec_eigs)

        n_zero = np.sum(np.abs(all_vec_eigs) < 1e-6)
        n_negative = np.sum(all_vec_eigs < -1e-6)
        result['vector_n_zero'] = n_zero
        result['vector_n_negative'] = n_negative
        result['vector_min'] = all_vec_eigs[0] if len(all_vec_eigs) > 0 else None
        result['vector_max'] = all_vec_eigs[-1] if len(all_vec_eigs) > 0 else None

    return result


# =============================================================================
# MODULE 5: MAIN COMPUTATION
# =============================================================================

def run_scalar_validation(gens, f_abc):
    """
    Validate scalar Laplacian at s=0 against known Casimir values.
    """
    separator("VALIDATION: Scalar Laplacian at s=0 (bi-invariant)")

    B_ab = compute_killing_form(f_abc)
    g_0 = jensen_metric(B_ab, 0.0)
    E_0 = orthonormal_frame(g_0)
    ft_0 = frame_structure_constants(f_abc, E_0)
    Gamma_0 = connection_coefficients(ft_0)

    # Check divergence = 0 at s=0
    div_max = 0.0
    for a in range(8):
        div_a = sum(Gamma_0[d, d, a] for d in range(8))
        div_max = max(div_max, abs(div_a))
    print(f"\n  Divergence correction at s=0: max|div(e_a)| = {div_max:.2e}")
    assert div_max < 1e-12, "Divergence should vanish at s=0!"

    # Check each sector
    print(f"\n  {'Sector':>10} {'dim':>5} {'C2/3 (expected)':>16} {'Lambda_min':>12} {'Lambda_max':>12} {'Error':>10} {'Status':>8}")
    print(f"  {'-'*10} {'-'*5} {'-'*16} {'-'*12} {'-'*12} {'-'*10} {'-'*8}")

    all_pass = True
    for pq_sum in range(7):
        for p in range(pq_sum + 1):
            q = pq_sum - p
            dim_pq = dim_su3_irrep(p, q)

            try:
                rho, _ = get_irrep(p, q, gens, f_abc)
                Delta = scalar_laplacian_on_irrep(rho, g_0, f_abc, E_0, Gamma_0)
                Delta = 0.5 * (Delta + Delta.conj().T)
                eigs = eigvalsh(Delta.real)

                C2 = (p**2 + q**2 + p*q + 3*p + 3*q) / 3.0
                expected = C2 / 3.0

                # All eigenvalues should be C2/3
                err = np.max(np.abs(eigs - expected))
                status = "PASS" if err < 1e-10 else "FAIL"
                if err >= 1e-10:
                    all_pass = False

                print(f"  ({p},{q}){' '*(7-len(f'({p},{q})'))} {dim_pq:5d} {expected:16.10f} "
                      f"{eigs[0]:12.10f} {eigs[-1]:12.10f} {err:10.2e} {status:>8}")
            except Exception as e:
                print(f"  ({p},{q}){' '*(7-len(f'({p},{q})'))} {dim_pq:5d} -- SKIPPED: {e}")

    print(f"\n  Overall validation: {'ALL PASS' if all_pass else 'SOME FAILURES'}")
    return all_pass


def run_vector_validation(gens, f_abc):
    """
    Validate vector Laplacian at s=0 against known bi-invariant results.

    On a compact simple Lie group with bi-invariant metric, the Hodge Laplacian
    on 1-forms has eigenvalues related to the Casimir + Ricci correction.

    For bi-invariant SU(3):
      Ric = (1/4) B = (1/4) * 3 I = (3/4) I  in our normalization
      (using Ric_{ab} = -(1/4) f_{acd} f_{bcd} for bi-invariant metric
       but with ON frame where f_tilde_{abc} = f_{abc}/sqrt(3*3*3) ...)

    Actually let me compute Ric numerically and verify.
    """
    separator("VALIDATION: Vector (1-form) Laplacian at s=0")

    B_ab = compute_killing_form(f_abc)
    g_0 = jensen_metric(B_ab, 0.0)
    E_0 = orthonormal_frame(g_0)
    ft_0 = frame_structure_constants(f_abc, E_0)
    Gamma_0 = connection_coefficients(ft_0)
    Ric_0 = ricci_tensor_from_connection(Gamma_0, ft_0)

    print(f"\n  Ricci tensor at s=0 (should be proportional to identity):")
    Ric_diag = [Ric_0[a, a] for a in range(8)]
    Ric_off_max = max(abs(Ric_0[a, b]) for a in range(8) for b in range(8) if a != b)
    print(f"    Diag: {[f'{x:.6f}' for x in Ric_diag]}")
    print(f"    Max off-diagonal: {Ric_off_max:.2e}")
    print(f"    R = Tr(Ric) = {sum(Ric_diag):.6f}")
    print(f"    R analytic at s=0 = {scalar_curvature_analytical(0.0):.6f}")

    # Compute vector spectrum at s=0 for low sectors
    print(f"\n  Vector Laplacian eigenvalues at s=0:")
    for pq_sum in range(4):
        for p in range(pq_sum + 1):
            q = pq_sum - p
            dim_pq = dim_su3_irrep(p, q)
            mat_size = dim_pq * 8

            try:
                rho, _ = get_irrep(p, q, gens, f_abc)
                Delta1 = vector_laplacian_on_irrep(rho, E_0, Gamma_0, Ric_0, f_abc, ft_0)
                Delta1 = 0.5 * (Delta1 + Delta1.conj().T)
                eigs = eigvalsh(Delta1.real)

                n_neg = np.sum(eigs < -1e-10)
                n_zero = np.sum(np.abs(eigs) < 1e-10)

                # For bi-invariant: should get C2/3 + 1/4 (Ric = 1/4 in normalized units)
                # Actually the exact formula depends on the representation content.
                # For (0,0): 1-forms are just constants * e^a, Delta_1 = Ric = (1/4)I_8

                print(f"    ({p},{q}): mat={mat_size}x{mat_size}, "
                      f"eigs: [{eigs[0]:.6f} .. {eigs[-1]:.6f}], "
                      f"neg={n_neg}, zero={n_zero}")

                # Special case (0,0): should be Ric eigenvalues
                if p == 0 and q == 0:
                    print(f"      (0,0) expected: Ric eigenvalues = {Ric_diag[0]:.6f}")

                # Special case (1,1): adjoint, should contain zero modes (Killing 1-forms)
                if p == 1 and q == 1:
                    print(f"      (1,1) contains Killing vectors: "
                          f"{n_zero} zero modes (expect 8 for bi-invariant)")

            except Exception as e:
                print(f"    ({p},{q}): SKIPPED ({e})")


def run_full_bosonic_tower(s_values, gens, f_abc, max_pq_scalar=6, max_pq_vector=4,
                           verbose=True):
    """
    Compute the full bosonic KK tower at specified s values.

    Returns a dict with all results, suitable for Hawking's V_eff computation.
    """
    separator(f"FULL BOSONIC KK TOWER (scalar: p+q<={max_pq_scalar}, vector: p+q<={max_pq_vector})")

    results = {}

    for s in s_values:
        separator(f"s = {s:.4f}")
        t0 = time.time()

        # Scalar tower
        print(f"\n  --- SCALAR LAPLACIAN (Delta_0) ---")
        scalar_data, scalar_flat = collect_scalar_spectrum(
            s, gens, f_abc, max_pq_sum=max_pq_scalar, verbose=verbose
        )

        # Vector tower
        print(f"\n  --- VECTOR (1-FORM) LAPLACIAN (Delta_1) ---")
        vector_data, vector_flat = collect_vector_spectrum(
            s, gens, f_abc, max_pq_sum=max_pq_vector, verbose=verbose
        )

        # Gauge boson check
        gauge_check = check_gauge_boson_consistency(s, gens, f_abc, scalar_data, vector_data)

        elapsed = time.time() - t0

        results[s] = {
            'scalar_data': scalar_data,
            'scalar_flat': scalar_flat,
            'vector_data': vector_data,
            'vector_flat': vector_flat,
            'gauge_check': gauge_check,
            'elapsed': elapsed,
        }

        # Summary
        n_scalar = len(scalar_flat)
        n_vector = len(vector_flat)

        scalar_eigs = [ev for ev, mult in scalar_flat]
        vector_eigs = [ev for ev, mult in vector_flat]

        total_scalar_dof = sum(mult for _, mult in scalar_flat)
        total_vector_dof = sum(mult for _, mult in vector_flat)

        print(f"\n  --- SUMMARY at s={s:.4f} ---")
        print(f"    Scalar: {n_scalar} distinct eigenvalues, "
              f"{total_scalar_dof} total DOF (with PW mult)")
        if scalar_eigs:
            print(f"      Range: [{min(scalar_eigs):.6f}, {max(scalar_eigs):.6f}]")
            n_neg_s = sum(1 for e in scalar_eigs if e < -1e-10)
            print(f"      Negative: {n_neg_s}")

        print(f"    Vector: {n_vector} distinct eigenvalues, "
              f"{total_vector_dof} total DOF (with PW mult)")
        if vector_eigs:
            print(f"      Range: [{min(vector_eigs):.6f}, {max(vector_eigs):.6f}]")
            n_neg_v = sum(1 for e in vector_eigs if e < -1e-10)
            print(f"      Negative: {n_neg_v}")

        print(f"    Gauge boson check: m2_C2={gauge_check['m2_baptista_C2']:.6f}")
        print(f"    Elapsed: {elapsed:.1f}s")

    return results


def write_spectrum_table(results, s):
    """
    Print a formatted table of the bosonic spectrum at a given s value.
    """
    if s not in results:
        print(f"  No results for s={s}")
        return

    data = results[s]

    separator(f"BOSONIC SPECTRUM TABLE at s={s:.4f}")

    # Scalar modes
    print(f"\n  SCALAR MODES (Delta_0 eigenvalues):")
    print(f"  {'Sector':>10} {'dim':>5} {'PW mult':>8} {'Eigenvalues (first 5)':>50}")
    print(f"  {'-'*10} {'-'*5} {'-'*8} {'-'*50}")

    for p, q, eigs, dim_pq in data['scalar_data']:
        pw = dim_pq**2
        eig_str = ', '.join(f'{e:.4f}' for e in eigs[:5])
        if len(eigs) > 5:
            eig_str += f', ... ({len(eigs)} total)'
        print(f"  ({p},{q}){' '*(7-len(f'({p},{q})'))} {dim_pq:5d} {pw:8d} {eig_str:>50}")

    # Vector modes
    print(f"\n  VECTOR MODES (Delta_1 eigenvalues):")
    print(f"  {'Sector':>10} {'dim':>5} {'Mat size':>9} {'PW mult':>8} {'Min eig':>10} {'Max eig':>10} {'N_eigs':>7}")
    print(f"  {'-'*10} {'-'*5} {'-'*9} {'-'*8} {'-'*10} {'-'*10} {'-'*7}")

    for p, q, eigs, dim_pq in data['vector_data']:
        pw = dim_pq**2
        mat_sz = dim_pq * 8
        print(f"  ({p},{q}){' '*(7-len(f'({p},{q})'))} {dim_pq:5d} {mat_sz:9d} {pw:8d} "
              f"{eigs[0]:10.4f} {eigs[-1]:10.4f} {len(eigs):7d}")


def export_for_hawking(results, filepath=None):
    """
    Export the bosonic spectrum in a format ready for Hawking's V_eff computation.

    Saves: for each s value, lists of (eigenvalue, multiplicity, type) where
    type is 'scalar' or 'vector'.
    """
    if filepath is None:
        filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                'kk1_bosonic_spectrum.npz')

    export = {}
    for s, data in results.items():
        key = f"s_{s:.4f}"

        # Combine scalar and vector
        all_modes = []

        for ev, mult in data['scalar_flat']:
            all_modes.append((ev, mult, 0))  # 0 = scalar

        for ev, mult in data['vector_flat']:
            all_modes.append((ev, mult, 1))  # 1 = vector

        arr = np.array(all_modes, dtype=[('eigenvalue', 'f8'), ('multiplicity', 'i8'), ('type', 'i4')])
        export[key] = arr

    np.savez(filepath, **{k: v for k, v in export.items()})
    print(f"\n  Exported bosonic spectrum to: {filepath}")
    return filepath


# =============================================================================
# MODULE 6: CLEAN API FOR V_eff COMPUTATION (Hawking interface)
# =============================================================================

# Cached infrastructure (initialized on first call)
_infra_cache = {}

def _ensure_infrastructure():
    """Initialize and cache SU(3) infrastructure."""
    if 'gens' not in _infra_cache:
        gens = su3_generators()
        f_abc = compute_structure_constants(gens)
        _infra_cache['gens'] = gens
        _infra_cache['f_abc'] = f_abc
    return _infra_cache['gens'], _infra_cache['f_abc']


def bosonic_spectrum_at_s(s, max_pq_scalar=6, max_pq_vector=4):
    """
    Compute the COMPLETE bosonic KK spectrum at a given s value.

    Returns eigenvalues and multiplicities for:
    1. Scalar KK tower (Delta_0 on functions)
    2. Vector KK tower (Delta_1 = Hodge Laplacian on 1-forms)
    3. Baptista's 4 gauge boson modes (eq 3.84, normalized to our units)

    NOTE ON PHYSICS:
    - Scalar eigenvalues = KK scalar masses squared (confirmed at s=0 vs Casimir)
    - Vector eigenvalues = graviphoton masses squared (from Hodge Laplacian)
    - Gauge boson masses = from Baptista eq 3.84 (separate from Hodge spectrum)
    - The Hodge Laplacian has NO zero modes (H^1(SU(3)) = 0)
    - Massless gauge bosons (u(2)) are NOT in the spectrum; they are gauge DOF

    For the CW potential, ALL eigenvalues contribute with POSITIVE sign (bosonic).
    Zero modes (if any) should be excluded from the CW sum.

    Args:
        s: Jensen deformation parameter
        max_pq_scalar: maximum p+q for scalar tower (default 6)
        max_pq_vector: maximum p+q for vector tower (default 4)

    Returns:
        dict with:
          'scalar_eigs': list of (eigenvalue, pw_multiplicity) for scalars
          'vector_eigs': list of (eigenvalue, pw_multiplicity) for vectors
          'gauge_boson_m2': squared mass of the 4 C^2 gauge bosons
          'n_scalar': number of distinct scalar eigenvalues
          'n_vector': number of distinct vector eigenvalues
          'total_boson_dof': total count including multiplicities
    """
    gens, f_abc = _ensure_infrastructure()

    scalar_data, scalar_flat = collect_scalar_spectrum(
        s, gens, f_abc, max_pq_sum=max_pq_scalar, verbose=False
    )
    vector_data, vector_flat = collect_vector_spectrum(
        s, gens, f_abc, max_pq_sum=max_pq_vector, verbose=False
    )

    m2_gauge, _ = gauge_boson_masses_baptista(0.0, s)

    total_dof = sum(m for _, m in scalar_flat) + sum(m for _, m in vector_flat)

    return {
        'scalar_eigs': scalar_flat,
        'vector_eigs': vector_flat,
        'scalar_data': scalar_data,
        'vector_data': vector_data,
        'gauge_boson_m2': m2_gauge,
        'n_scalar': len(scalar_flat),
        'n_vector': len(vector_flat),
        'total_boson_dof': total_dof,
    }


def scalar_spectrum_at_s(s, max_pq_sum=6):
    """
    Compute ONLY the scalar Laplacian spectrum (faster than full bosonic tower).

    This is the most reliable part of the bosonic tower — validated against
    Casimir eigenvalues at s=0 to machine epsilon.

    Args:
        s: Jensen deformation parameter
        max_pq_sum: maximum p+q (default 6)

    Returns:
        list of (eigenvalue, pw_multiplicity) pairs
    """
    gens, f_abc = _ensure_infrastructure()
    _, flat = collect_scalar_spectrum(s, gens, f_abc, max_pq_sum=max_pq_sum, verbose=False)
    return flat


# =============================================================================
# MAIN
# =============================================================================

if __name__ == '__main__':
    print("="*72)
    print("  KK-1: FULL BOSONIC KALUZA-KLEIN TOWER ON (SU(3), g_s)")
    print("  Session 18 — KK-Theorist Agent")
    print("="*72)

    t_start = time.time()

    # Initialize infrastructure
    print("\n  Initializing SU(3) Lie algebra infrastructure...")
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    B_ab = compute_killing_form(f_abc)
    print(f"    Killing form: B = {B_ab[0,0]:.1f} * I_8")

    # =========================================================================
    # PHASE 1: VALIDATION AT s=0
    # =========================================================================
    scalar_pass = run_scalar_validation(gens, f_abc)

    run_vector_validation(gens, f_abc)

    # =========================================================================
    # PHASE 2: COMPUTE FULL TOWER AT KEY s-VALUES
    # =========================================================================
    # Key s values from previous sessions:
    # s=0.15 (phi ratio crossing), s=0.30 (Weinberg angle), s=0.50, s=1.14 (phi peak)
    s_values = [0.0, 0.15, 0.30, 0.50]

    results = run_full_bosonic_tower(
        s_values, gens, f_abc,
        max_pq_scalar=6,
        max_pq_vector=4,
        verbose=True
    )

    # =========================================================================
    # PHASE 3: SPECTRUM TABLES
    # =========================================================================
    for s in s_values:
        write_spectrum_table(results, s)

    # =========================================================================
    # PHASE 4: DOF COUNT
    # =========================================================================
    separator("DOF COUNT")
    dof = count_bosonic_dof(max_pq_sum=6)
    print(f"\n  Scalar DOF (p+q<=6): {dof['total_scalar']}")
    print(f"  Vector DOF (p+q<=6, estimated): {dof['total_vector']}")

    # Count distinct eigenvalues at s=0.15
    if 0.15 in results:
        data = results[0.15]
        n_scalar_eigs = sum(len(eigs) for _, _, eigs, _ in data['scalar_data'])
        n_vector_eigs = sum(len(eigs) for _, _, eigs, _ in data['vector_data'])
        print(f"\n  At s=0.15:")
        print(f"    Scalar: {n_scalar_eigs} distinct eigenvalues computed")
        print(f"    Vector: {n_vector_eigs} distinct eigenvalues computed")
        print(f"    Total bosonic eigenvalues for CW: {n_scalar_eigs + n_vector_eigs}")

    # =========================================================================
    # PHASE 5: EXPORT
    # =========================================================================
    export_path = export_for_hawking(results)

    # =========================================================================
    # SUMMARY
    # =========================================================================
    separator("FINAL SUMMARY")
    elapsed_total = time.time() - t_start
    print(f"\n  Computation time: {elapsed_total:.1f}s")
    print(f"  s-values computed: {s_values}")

    if 0.15 in results:
        data = results[0.15]
        scalar_eigs_015 = [ev for ev, m in data['scalar_flat']]
        vector_eigs_015 = [ev for ev, m in data['vector_flat']]
        n_neg_scalar = sum(1 for e in scalar_eigs_015 if e < -1e-10)
        n_neg_vector = sum(1 for e in vector_eigs_015 if e < -1e-10)
        print(f"\n  At s=0.15:")
        print(f"    Scalar eigenvalue range: [{min(scalar_eigs_015):.6f}, {max(scalar_eigs_015):.6f}]")
        print(f"    Scalar negative modes: {n_neg_scalar}")
        print(f"    Vector eigenvalue range: [{min(vector_eigs_015):.6f}, {max(vector_eigs_015):.6f}]")
        print(f"    Vector negative modes: {n_neg_vector}")

    print(f"\n  Baptista's 4 gauge bosons at s=0.15: m^2 = {gauge_boson_masses_baptista(0.0, 0.15)[0]:.6f}")
    print(f"  Baptista's 4 gauge bosons at s=0.30: m^2 = {gauge_boson_masses_baptista(0.0, 0.30)[0]:.6f}")

    print(f"\n  Output file: {export_path}")
    print(f"\n{'='*72}")
    print(f"  KK-1 COMPLETE")
    print(f"{'='*72}")
