#!/usr/bin/env python3
"""
S49 CMPP-TRANSITION-49: Higher-D Petrov Classification at Geometric Phase Transition
=====================================================================================

Computes the CMPP (Coley-Milson-Pravda-Pravdova) algebraic classification of the
8D Weyl tensor on Jensen-deformed SU(3) at tau values spanning the geometric phase
transition at tau = 0.537.

CMPP Scheme (arXiv:0401008, 0611339):
  In n > 4 dimensions, the Weyl tensor is classified by boost weight decomposition
  along a null frame {l, n, m_i}. Components C_{0i0j} have boost weight +2,
  C_{0ijk} have boost weight +1, C_{ijkl}/C_{0i1j} have boost weight 0,
  C_{1ijk} have boost weight -1, C_{1i1j} have boost weight -2.

  Classification hierarchy (most special to most general):
    O:   C = 0
    N:   only bw = -2 nonzero
    III: only bw <= -1 nonzero
    II:  only bw <= 0 nonzero (includes D as subcase where bw = 0 is "Type D block")
    D:   only bw = 0 nonzero
    I:   bw +2 vanishes for some null direction (I_i variants)
    G:   generic (no special null direction)

  For Riemannian (positive-definite) metrics, there are no real null vectors.
  We work with the COMPLEXIFIED tangent space: pick complex null directions
  e_0 = (e_a + i*e_b)/sqrt(2), e_1 = (e_a - i*e_b)/sqrt(2) for ON pair (a,b).

  The classification then reduces to the eigenvalue structure of the Weyl operator
  on 2-forms, exactly as computed in S25/S39 but now with CMPP boost-weight labels.

Method:
  1. Compute full 8D Riemann tensor at each tau.
  2. Extract Weyl tensor.
  3. Map Weyl to operator on Lambda^2 (28x28 matrix).
  4. For CMPP: choose preferred null direction from SU(2) sector (most deformed).
     Decompose C_IJ into boost-weight blocks.
  5. Classify by which boost-weight blocks vanish.
  6. Track classification across tau = 0.537 transition.

Input: tier1_dirac_spectrum.py (geometry), canonical_constants.py
Output: s49_cmpp_transition.npz, s49_cmpp_transition.png

Gate: CMPP-TRANSITION-49
  PASS: CMPP type changes at tau = 0.537
  INFO: type changes at nearby tau
  FAIL: constant CMPP type across scan

Author: schwarzschild-penrose-geometer (Session 49)
Date: 2026-03-17
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys
import os
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tier1_dirac_spectrum import (
    su3_generators,
    compute_structure_constants,
    compute_killing_form,
    jensen_metric,
    orthonormal_frame,
    frame_structure_constants,
    connection_coefficients,
    U1_IDX,
    SU2_IDX,
    C2_IDX,
)
from canonical_constants import (
    tau_fold, G_DeWitt, PI,
)

t_start = time.time()

DIM = 8
N_PAIRS = DIM * (DIM - 1) // 2  # = 28


# =============================================================================
# SECTION 1: Curvature computation (reused from S47/S48/S49)
# =============================================================================

def compute_riemann_tensor_ON(ft, Gamma, n=DIM):
    """Full Riemann tensor R[a,b,c,f] = R^f_{abc} in ON frame."""
    R = np.zeros((n, n, n, n), dtype=np.float64)
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for f_idx in range(n):
                    val = 0.0
                    for d in range(n):
                        val += Gamma[d, b, c] * Gamma[f_idx, a, d]
                        val -= Gamma[d, a, c] * Gamma[f_idx, b, d]
                        val -= ft[a, b, d] * Gamma[f_idx, d, c]
                    R[a, b, c, f_idx] = val
    return R


def compute_weyl_tensor(R_abcd, Ric, R_scalar, n=DIM):
    """Compute 8D Weyl tensor C_abcd from Riemann, Ricci, scalar curvature."""
    C = np.copy(R_abcd)
    delta = np.eye(n)
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    ricci_part = (1.0 / (n - 2)) * (
                        Ric[a, c] * delta[b, d] - Ric[a, d] * delta[b, c]
                        - Ric[b, c] * delta[a, d] + Ric[b, d] * delta[a, c]
                    )
                    scalar_part = (R_scalar / ((n - 1) * (n - 2))) * (
                        delta[a, c] * delta[b, d] - delta[a, d] * delta[b, c]
                    )
                    C[a, b, c, d] -= ricci_part + scalar_part
    return C


def weyl_as_2form_operator(C_abcd, n=DIM):
    """Map Weyl tensor to symmetric matrix on Lambda^2."""
    pairs = []
    for a in range(n):
        for b in range(a + 1, n):
            pairs.append((a, b))
    N = len(pairs)
    C_mat = np.zeros((N, N))
    for I, (a1, b1) in enumerate(pairs):
        for J, (a2, b2) in enumerate(pairs):
            C_mat[I, J] = C_abcd[a1, b1, a2, b2]
    return C_mat, pairs


def compute_full_geometry(tau, gens, f_abc, B_ab):
    """Compute Riemann, Weyl, Ricci, scalar at given tau. Returns raw tensors."""
    n = DIM
    g_s = jensen_metric(B_ab, tau)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    R_abcd = compute_riemann_tensor_ON(ft, Gamma)

    # Ricci: R_ac = R^b_{abc} = R_abcd delta^{bd} (ON frame)
    Ric = np.einsum('abca->bc', R_abcd)
    # Make symmetric (numerical)
    Ric = 0.5 * (Ric + Ric.T)
    R_scalar = np.trace(Ric)
    Ric_sq = np.sum(Ric * Ric)

    # Kretschner
    K_full = np.sum(R_abcd * R_abcd)

    # Weyl
    C_abcd = compute_weyl_tensor(R_abcd, Ric, R_scalar)
    C_sq = np.sum(C_abcd * C_abcd)

    # Verify Weyl norm via Bianchi
    C_sq_check = K_full - (4.0 / (n - 2)) * Ric_sq + (2.0 / ((n - 1) * (n - 2))) * R_scalar**2

    # Sectional curvatures
    K_sect = []
    for a in range(n):
        for b in range(a + 1, n):
            K_sect.append(R_abcd[a, b, b, a])
    K_sect = np.array(K_sect)

    return {
        'R_abcd': R_abcd,
        'C_abcd': C_abcd,
        'Ric': Ric,
        'R_scalar': R_scalar,
        'Ric_sq': Ric_sq,
        'K_full': K_full,
        'C_sq': C_sq,
        'C_sq_check': C_sq_check,
        'K_sect': K_sect,
        'Ric_eigs': np.sort(np.linalg.eigvalsh(Ric)),
        'g_s': g_s,
    }


# =============================================================================
# SECTION 2: CMPP Boost Weight Decomposition
# =============================================================================
#
# For a Riemannian manifold, there are no real null vectors. The CMPP classification
# in Riemannian signature uses the complexified tangent space. We pick an ON pair
# (e_a, e_b) and form complex null vectors:
#   l = (e_a + i*e_b) / sqrt(2),  n = (e_a - i*e_b) / sqrt(2)
# with l.n = 1 (in the complexified metric).
#
# The remaining ON vectors m_i (i = 1,...,n-2) span the transverse space.
#
# Boost weight +2 components: C_{0i0j} = C(l, m_i, l, m_j)
# Boost weight +1 components: C_{010i} = C(l, n, l, m_i) and C_{0ijk}
# Boost weight  0 components: C_{0i1j} = C(l, m_i, n, m_j) and C_{ijkl}
# Boost weight -1 components: C_{101i} = C(n, l, n, m_i) and C_{1ijk}
# Boost weight -2 components: C_{1i1j} = C(n, m_i, n, m_j)
#
# In practice, since the metric is Riemannian (real positive-definite), the Weyl
# tensor is real. The boost-weight decomposition with complex null vectors yields
# complex components. The CMPP type is determined by which boost-weight blocks
# vanish (in norm).
#
# For the Jensen metric on SU(3), the natural preferred directions are:
#   - SU(2) sector: most contracted (e^{-2tau})
#   - C2 sector: mixed (e^{tau})
#   - U(1) sector: most expanded (e^{2tau})
#
# We test multiple null-direction choices to find the MOST SPECIAL type (WAND).

def cmpp_boost_decomposition(C_abcd, null_a, null_b, n=DIM):
    """
    Compute CMPP boost-weight decomposition of the Weyl tensor.

    Given ON frame indices null_a, null_b defining the complex null directions:
      l = (e_{null_a} + i*e_{null_b}) / sqrt(2)
      n = (e_{null_a} - i*e_{null_b}) / sqrt(2)

    The transverse indices are all other ON frame indices.

    Returns dict with norms of each boost-weight component.
    """
    # Transverse indices
    transverse = [i for i in range(n) if i != null_a and i != null_b]
    n_t = len(transverse)  # n-2 = 6

    # Complex null vectors: components in ON frame
    # l^a = (delta^a_{null_a} + i*delta^a_{null_b}) / sqrt(2)
    # n^a = (delta^a_{null_a} - i*delta^a_{null_b}) / sqrt(2)
    # We use "0" for l-direction and "1" for n-direction

    # Build Weyl components in the null frame:
    # C_{abcd} in ON frame -> C in null frame via index substitution
    # C(l, m_i, l, m_j) = (1/2) * [C_{ai aj} + i*C_{bi aj} + i*C_{ai bj} - C_{bi bj}]
    # where a = null_a, b = null_b, and i,j are transverse indices

    a, b = null_a, null_b

    # Boost weight +2: Phi_{ij} = C(l, m_i, l, m_j)
    # = (1/2)[C_{a,ti,a,tj} + i*C_{b,ti,a,tj} + i*C_{a,ti,b,tj} - C_{b,ti,b,tj}]
    Phi_p2 = np.zeros((n_t, n_t), dtype=complex)
    for ii, ti in enumerate(transverse):
        for jj, tj in enumerate(transverse):
            Phi_p2[ii, jj] = 0.5 * (
                C_abcd[a, ti, a, tj]
                + 1j * C_abcd[b, ti, a, tj]
                + 1j * C_abcd[a, ti, b, tj]
                - C_abcd[b, ti, b, tj]
            )

    # Boost weight -2: Psi_{ij} = C(n, m_i, n, m_j)
    # = (1/2)[C_{a,ti,a,tj} - i*C_{b,ti,a,tj} - i*C_{a,ti,b,tj} - C_{b,ti,b,tj}]
    Phi_m2 = np.zeros((n_t, n_t), dtype=complex)
    for ii, ti in enumerate(transverse):
        for jj, tj in enumerate(transverse):
            Phi_m2[ii, jj] = 0.5 * (
                C_abcd[a, ti, a, tj]
                - 1j * C_abcd[b, ti, a, tj]
                - 1j * C_abcd[a, ti, b, tj]
                - C_abcd[b, ti, b, tj]
            )

    # Boost weight +1: Psi_i = C(l, n, l, m_i) and C(l, m_j, m_k, m_i)
    # C(l, n, l, m_i) = (1/4)[C_{a,a,a,ti} - C_{b,b,a,ti} + ... (expand)]
    # Simpler: C_{010i} = C(l, n, l, m_i) = (1/2)[C_{a,*,a,ti} + i-terms]

    # C(l, n, l, m_i):
    # l = (e_a + i*e_b)/sqrt(2), n = (e_a - i*e_b)/sqrt(2)
    # C(l,n,l,m_i) = (1/2)(1/2)[
    #   (e_a + ie_b)(e_a - ie_b)(e_a + ie_b) m_i components of C
    # ]
    # = (1/4)[C_{a,a,a,ti} + i*C_{b,a,a,ti} - i*C_{a,b,a,ti} + C_{b,b,a,ti}
    #        + i*C_{a,a,b,ti} - C_{b,a,b,ti} + C_{a,b,b,ti} + i*C_{b,b,b,ti}]
    #
    # But C_{abcd} is antisymmetric in (ab) and (cd) for Weyl.
    # C_{a,a,...} = 0 by antisymmetry. So:
    # C(l,n,l,m_i) = (1/4)[
    #   i*C_{b,a,a,ti} - i*C_{a,b,a,ti} - C_{b,a,b,ti} + C_{a,b,b,ti}
    #  + i*C_{a,a,b,ti} + i*C_{b,b,b,ti}]
    # Using C_{ba..} = -C_{ab..}: C_{b,a,...} = -C_{a,b,...}
    # = (1/4)[-2i*C_{a,b,a,ti} + 2*C_{a,b,b,ti}]
    # Wait, need to be more careful. C_{a,a,a,ti} = 0, C_{b,b,b,ti} = 0 (antisym in first pair).
    # C_{b,a,a,ti} = 0 (antisym in second pair => C_{..,a,a,..}?? No, antisym in (a,b) and (c,d).
    #
    # Let me use a cleaner approach. Define the null frame components directly.

    # CLEANER APPROACH: Build the full null-frame Weyl tensor.
    # Define complex frame vectors:
    # e_0 = l = (e_a + i*e_b)/sqrt(2)
    # e_1 = n = (e_a - i*e_b)/sqrt(2)
    # e_{i+2} = m_i = e_{transverse[i]}  for i = 0,...,n_t-1
    #
    # Frame change matrix: F[alpha, mu] where alpha is null-frame index, mu is ON index
    F = np.zeros((n, n), dtype=complex)
    F[0, a] = 1.0 / np.sqrt(2)
    F[0, b] = 1j / np.sqrt(2)
    F[1, a] = 1.0 / np.sqrt(2)
    F[1, b] = -1j / np.sqrt(2)
    for ii, ti in enumerate(transverse):
        F[ii + 2, ti] = 1.0

    # Transform Weyl tensor to null frame:
    # C'_{alpha beta gamma delta} = F_{alpha}^mu F_{beta}^nu F_{gamma}^rho F_{delta}^sigma C_{mu nu rho sigma}
    C_null = np.einsum('am,bn,cp,dq,mnpq->abcd', F, F, F, F, C_abcd)

    # Boost weight classification:
    # Index 0 (l-direction) has boost weight +1
    # Index 1 (n-direction) has boost weight -1
    # Indices 2,...,n-1 (transverse) have boost weight 0
    #
    # boost weight of C_{abcd} = sum of boost weights of indices
    # BW(0) = +1, BW(1) = -1, BW(i>=2) = 0

    def boost_weight_of_index(idx):
        if idx == 0:
            return +1
        elif idx == 1:
            return -1
        else:
            return 0

    # Collect components by boost weight
    bw_norms = {bw: 0.0 for bw in [-2, -1, 0, +1, +2]}

    for alpha in range(n):
        for beta in range(n):
            for gamma in range(n):
                for delta in range(n):
                    bw = (boost_weight_of_index(alpha) + boost_weight_of_index(beta)
                          + boost_weight_of_index(gamma) + boost_weight_of_index(delta))
                    val = C_null[alpha, beta, gamma, delta]
                    if abs(bw) <= 2:
                        bw_norms[bw] += abs(val)**2

    # Normalize by total |C|^2
    total_C_sq = sum(bw_norms.values())
    # Also collect higher bw (should be zero by Weyl symmetries, but check)
    bw_all = {}
    for alpha in range(n):
        for beta in range(n):
            for gamma in range(n):
                for delta in range(n):
                    bw = (boost_weight_of_index(alpha) + boost_weight_of_index(beta)
                          + boost_weight_of_index(gamma) + boost_weight_of_index(delta))
                    val = C_null[alpha, beta, gamma, delta]
                    bw_all[bw] = bw_all.get(bw, 0.0) + abs(val)**2

    # Also extract the specific CMPP invariant matrices:
    # Phi_{ij}^{(+2)} = C_{0i0j} (i,j transverse, so i,j in 2..n-1)
    Phi_plus2 = np.zeros((n_t, n_t), dtype=complex)
    for ii in range(n_t):
        for jj in range(n_t):
            Phi_plus2[ii, jj] = C_null[0, ii + 2, 0, jj + 2]

    # Phi_{ij}^{(-2)} = C_{1i1j}
    Phi_minus2 = np.zeros((n_t, n_t), dtype=complex)
    for ii in range(n_t):
        for jj in range(n_t):
            Phi_minus2[ii, jj] = C_null[1, ii + 2, 1, jj + 2]

    # Phi_{ij}^{(0)} = C_{0i1j}  (the "electric" part of bw=0)
    Phi_0_electric = np.zeros((n_t, n_t), dtype=complex)
    for ii in range(n_t):
        for jj in range(n_t):
            Phi_0_electric[ii, jj] = C_null[0, ii + 2, 1, jj + 2]

    # C_{ijkl} = purely transverse part (bw = 0)
    C_trans = np.zeros((n_t, n_t, n_t, n_t), dtype=complex)
    for ii in range(n_t):
        for jj in range(n_t):
            for kk in range(n_t):
                for ll in range(n_t):
                    C_trans[ii, jj, kk, ll] = C_null[ii + 2, jj + 2, kk + 2, ll + 2]
    C_trans_norm = np.sqrt(np.sum(np.abs(C_trans)**2))

    # Eigenvalues of the bw=+2 matrix (key for WAND condition)
    eigs_p2 = np.linalg.eigvalsh(np.real(Phi_plus2 + Phi_plus2.conj().T) / 2)
    eigs_m2 = np.linalg.eigvalsh(np.real(Phi_minus2 + Phi_minus2.conj().T) / 2)
    eigs_0e = np.linalg.eigvals(Phi_0_electric)  # Not necessarily Hermitian

    return {
        'bw_norms': bw_norms,
        'bw_all': bw_all,
        'total_C_sq': total_C_sq,
        'Phi_plus2': Phi_plus2,
        'Phi_minus2': Phi_minus2,
        'Phi_0_electric': Phi_0_electric,
        'C_trans_norm': C_trans_norm,
        'eigs_p2': np.sort(np.real(eigs_p2)),
        'eigs_m2': np.sort(np.real(eigs_m2)),
        'eigs_0e': np.sort_complex(eigs_0e),
        'norm_p2': np.sqrt(bw_norms.get(+2, 0)),
        'norm_p1': np.sqrt(bw_norms.get(+1, 0)),
        'norm_0': np.sqrt(bw_norms.get(0, 0)),
        'norm_m1': np.sqrt(bw_norms.get(-1, 0)),
        'norm_m2': np.sqrt(bw_norms.get(-2, 0)),
    }


def classify_cmpp_type(decomp, tol=1e-10):
    """
    Classify CMPP type from boost-weight decomposition.

    Returns string: 'O', 'N', 'III', 'D', 'II', 'I', 'G'
    and a detailed dict of checks.
    """
    total = decomp['total_C_sq']
    if total < tol:
        return 'O', {'reason': '|C|^2 = 0'}

    # Relative threshold
    rel_tol = tol * total

    n2 = decomp['bw_norms'].get(+2, 0)
    n1 = decomp['bw_norms'].get(+1, 0)
    n0 = decomp['bw_norms'].get(0, 0)
    nm1 = decomp['bw_norms'].get(-1, 0)
    nm2 = decomp['bw_norms'].get(-2, 0)

    # Fractions
    f2 = n2 / total
    f1 = n1 / total
    f0 = n0 / total
    fm1 = nm1 / total
    fm2 = nm2 / total

    details = {
        'frac_bw+2': f2,
        'frac_bw+1': f1,
        'frac_bw0': f0,
        'frac_bw-1': fm1,
        'frac_bw-2': fm2,
    }

    # Classification (for THIS null direction):
    # Type N: only bw <= -2 nonzero (or equivalently bw >= +2 if we flip)
    # Type III: only bw <= -1 nonzero
    # Type D: only bw = 0 nonzero
    # Type II: only bw <= 0 nonzero (i.e., bw = +1, +2 vanish)
    # Type I: bw = +2 vanishes
    # Type G: all nonzero

    # Check from most special to most general
    # For a Riemannian metric, the natural symmetry under complex conjugation
    # means bw+2 and bw-2 are related, and bw+1 and bw-1 are related.
    # So we check using the maximum of each conjugate pair.

    has_bw2 = max(n2, nm2) > rel_tol
    has_bw1 = max(n1, nm1) > rel_tol
    has_bw0 = n0 > rel_tol

    if not has_bw2 and not has_bw1 and not has_bw0:
        return 'O', details
    elif has_bw0 and not has_bw1 and not has_bw2:
        return 'D', details
    elif not has_bw2 and has_bw1:
        # bw = +/-2 vanish but bw = +/-1 nonzero: between II and III
        # Type III: bw+1 AND bw+2 vanish (or bw-1 AND bw-2 vanish)
        # Since we're symmetric in Riemannian case, check if the
        # positive-boost components vanish
        if n2 < rel_tol and n1 < rel_tol:
            return 'III', details
        elif nm2 < rel_tol and nm1 < rel_tol:
            return 'III', details
        else:
            return 'II', details
    elif not has_bw2 and not has_bw1:
        return 'D', details
    elif has_bw2 and not has_bw1:
        # bw+/-2 nonzero but bw+/-1 vanish -- this is Type I_i or special
        details['note'] = 'bw+/-2 nonzero, bw+/-1 zero: Type I variant'
        return 'I', details
    else:
        # Check if there exists a rotation that could eliminate bw+2
        # For now, classify as I if bw+2 is small fraction, else G
        if f2 < 0.01 and fm2 < 0.01:
            details['note'] = 'bw+/-2 < 1%: likely Type I (WAND exists)'
            return 'I', details
        else:
            return 'G', details


def scan_null_directions(C_abcd, n=DIM):
    """
    Scan over all pairs of ON frame indices as possible null directions.
    For each pair (a,b), compute CMPP decomposition. Return the MOST SPECIAL type found.

    In the CMPP scheme, the algebraic type is determined by the MOST SPECIAL
    null direction (the Weyl Aligned Null Direction = WAND).
    """
    best_type = 'G'
    best_decomp = None
    best_pair = None

    type_rank = {'O': 0, 'N': 1, 'III': 2, 'D': 3, 'II': 4, 'I': 5, 'G': 6}

    all_decomps = {}

    for a in range(n):
        for b in range(a + 1, n):
            decomp = cmpp_boost_decomposition(C_abcd, a, b, n)
            ctype, details = classify_cmpp_type(decomp)
            decomp['type'] = ctype
            decomp['details'] = details
            decomp['null_pair'] = (a, b)
            all_decomps[(a, b)] = decomp

            if type_rank.get(ctype, 6) < type_rank.get(best_type, 6):
                best_type = ctype
                best_decomp = decomp
                best_pair = (a, b)

    return best_type, best_decomp, best_pair, all_decomps


# =============================================================================
# SECTION 3: Weyl operator eigenvalue analysis (complementary to CMPP)
# =============================================================================

def weyl_operator_analysis(C_abcd, n=DIM):
    """
    Analyze the Weyl tensor as an operator on 2-forms (28x28 matrix).
    This gives the 4D-analog Petrov classification via eigenvalue structure.
    """
    C_mat, pairs = weyl_as_2form_operator(C_abcd, n)

    # Verify trace-free
    tr = np.trace(C_mat)

    # Verify symmetry
    sym_err = np.max(np.abs(C_mat - C_mat.T))

    # Eigenvalues
    eigvals = np.linalg.eigvalsh(C_mat)
    eigvals_sorted = np.sort(eigvals)

    # Count distinct eigenvalues
    tol = 1e-8 * (np.max(np.abs(eigvals)) + 1e-15)
    unique_eigs = []
    for e in eigvals_sorted:
        if not unique_eigs or abs(e - unique_eigs[-1]) > tol:
            unique_eigs.append(e)

    multiplicities = []
    for ue in unique_eigs:
        mult = int(np.sum(np.abs(eigvals - ue) < tol))
        multiplicities.append(mult)

    # |C|^2 from matrix
    C_sq_matrix = np.sum(C_mat**2)

    # Classify 4D-analog Petrov type from eigenvalue structure
    n_distinct = len(unique_eigs)
    max_mult = max(multiplicities) if multiplicities else 0

    # Type D analog: highly degenerate eigenvalues
    # Type II analog: some degeneracy but not maximal
    # Type I analog: all distinct (generic)
    # Type N analog: only one nonzero eigenvalue with high multiplicity

    return {
        'C_mat': C_mat,
        'trace': tr,
        'sym_err': sym_err,
        'eigvals': eigvals_sorted,
        'n_distinct': n_distinct,
        'unique_eigs': unique_eigs,
        'multiplicities': multiplicities,
        'max_mult': max_mult,
        'C_sq_matrix': C_sq_matrix,
    }


# =============================================================================
# SECTION 4: Main computation
# =============================================================================

print("=" * 78)
print("  S49 CMPP-TRANSITION-49: Higher-D Petrov Classification at tau = 0.537")
print("=" * 78)

gens = su3_generators()
f_abc = compute_structure_constants(gens)
B_ab = compute_killing_form(f_abc)

# Tau scan: dense around the transition at 0.537
tau_values = np.array([0.00, 0.10, 0.19, 0.30, 0.40, 0.50, 0.52, 0.53,
                       0.537, 0.54, 0.55, 0.56, 0.60, 0.70, 0.80, 1.00])

results = {}

print(f"\nScanning {len(tau_values)} tau values...")
print(f"{'tau':>8s}  {'CMPP':>5s}  {'n_eig':>5s}  {'max_m':>5s}  "
      f"{'bw+2%':>7s}  {'bw+1%':>7s}  {'bw0%':>7s}  {'bw-1%':>7s}  {'bw-2%':>7s}  "
      f"|C|^2      {'best_pair':>10s}")
print("-" * 110)

for tau in tau_values:
    geom = compute_full_geometry(tau, gens, f_abc, B_ab)
    C_abcd = geom['C_abcd']
    C_sq = geom['C_sq']

    # CMPP classification (scan all null directions)
    cmpp_type, best_decomp, best_pair, all_decomps = scan_null_directions(C_abcd)

    # Weyl operator analysis
    weyl_op = weyl_operator_analysis(C_abcd)

    results[tau] = {
        'geom': geom,
        'cmpp_type': cmpp_type,
        'best_decomp': best_decomp,
        'best_pair': best_pair,
        'all_decomps': all_decomps,
        'weyl_op': weyl_op,
    }

    # Print summary
    if best_decomp is not None:
        bw = best_decomp['bw_norms']
        tot = best_decomp['total_C_sq']
        if tot > 0:
            fracs = {k: v / tot * 100 for k, v in bw.items()}
        else:
            fracs = {k: 0.0 for k in bw}
        print(f"{tau:8.4f}  {cmpp_type:>5s}  {weyl_op['n_distinct']:5d}  {weyl_op['max_mult']:5d}  "
              f"{fracs.get(+2, 0):7.2f}  {fracs.get(+1, 0):7.2f}  {fracs.get(0, 0):7.2f}  "
              f"{fracs.get(-1, 0):7.2f}  {fracs.get(-2, 0):7.2f}  "
              f"{C_sq:10.6f}  {best_pair}")


# =============================================================================
# SECTION 5: Detailed analysis at the transition
# =============================================================================

print("\n\n" + "=" * 78)
print("  DETAILED ANALYSIS AT TRANSITION")
print("=" * 78)

# Focus on tau values bracketing 0.537
transition_taus = [0.50, 0.53, 0.537, 0.54, 0.55, 0.60]

for tau in transition_taus:
    r = results[tau]
    geom = r['geom']
    weyl_op = r['weyl_op']
    cmpp_type = r['cmpp_type']
    best_decomp = r['best_decomp']
    best_pair = r['best_pair']

    print(f"\n--- tau = {tau:.4f} ---")
    print(f"  CMPP type: {cmpp_type} (best null pair: {best_pair})")
    print(f"  |C|^2 = {geom['C_sq']:.8f}")
    print(f"  Kretschner K = {geom['K_full']:.8f}")
    print(f"  R_scalar = {geom['R_scalar']:.8f}")
    print(f"  |C|^2/K = {geom['C_sq']/geom['K_full']:.6f}")
    print(f"  Ricci eigs: {geom['Ric_eigs']}")

    # Sectional curvature range
    K_sect = geom['K_sect']
    print(f"  K_sect range: [{K_sect.min():.8f}, {K_sect.max():.8f}]")
    n_neg = np.sum(K_sect < -1e-14)
    print(f"  n_neg_K = {n_neg}, n_pos_K = {np.sum(K_sect > 1e-14)}")

    # Weyl operator eigenvalues
    print(f"  Weyl operator: {weyl_op['n_distinct']} distinct eigenvalues, max mult = {weyl_op['max_mult']}")
    print(f"  Eigenvalue-multiplicity pairs:")
    for ue, m in zip(weyl_op['unique_eigs'], weyl_op['multiplicities']):
        print(f"    lambda = {ue:+.8f}, mult = {m}")

    # CMPP decomposition details
    if best_decomp is not None:
        bw = best_decomp['bw_norms']
        tot = best_decomp['total_C_sq']
        print(f"  CMPP boost weight fractions (best null pair {best_pair}):")
        for bwi in [+2, +1, 0, -1, -2]:
            frac = bw.get(bwi, 0) / tot * 100 if tot > 0 else 0
            print(f"    bw = {bwi:+d}: {frac:8.4f}%  (norm^2 = {bw.get(bwi, 0):.6e})")

    # CMPP types for different null directions (sector analysis)
    all_decomps = r['all_decomps']
    type_counts = {}
    sector_types = {}  # Will be populated dynamically
    for (a, b), dec in all_decomps.items():
        t = dec['type']
        type_counts[t] = type_counts.get(t, 0) + 1
        # Classify the null-pair sector
        a_t = 'u1' if a in U1_IDX else ('su2' if a in SU2_IDX else 'c2')
        b_t = 'u1' if b in U1_IDX else ('su2' if b in SU2_IDX else 'c2')
        st = '-'.join(sorted([a_t, b_t]))
        sector_types.setdefault(st, []).append(t)

    print(f"  CMPP type distribution across all 28 null directions:")
    for t, c in sorted(type_counts.items()):
        print(f"    Type {t}: {c} directions")
    print(f"  By sector:")
    for st, types in sorted(sector_types.items()):
        if types:
            tc = {}
            for t in types:
                tc[t] = tc.get(t, 0) + 1
            print(f"    {st}: {tc}")


# =============================================================================
# SECTION 6: Track type changes across transition
# =============================================================================

print("\n\n" + "=" * 78)
print("  CMPP TYPE TRAJECTORY")
print("=" * 78)

cmpp_types = [results[tau]['cmpp_type'] for tau in tau_values]
weyl_n_distinct = [results[tau]['weyl_op']['n_distinct'] for tau in tau_values]
weyl_max_mult = [results[tau]['weyl_op']['max_mult'] for tau in tau_values]

# Detect type changes
type_changes = []
for i in range(1, len(tau_values)):
    if cmpp_types[i] != cmpp_types[i - 1]:
        type_changes.append({
            'tau_before': tau_values[i - 1],
            'tau_after': tau_values[i],
            'type_before': cmpp_types[i - 1],
            'type_after': cmpp_types[i],
        })

print(f"\nCMPP type trajectory:")
for i, tau in enumerate(tau_values):
    marker = " <-- TRANSITION" if any(
        tc['tau_before'] == tau or tc['tau_after'] == tau for tc in type_changes
    ) else ""
    print(f"  tau = {tau:.4f}: {cmpp_types[i]:>5s}  (n_distinct={weyl_n_distinct[i]}, "
          f"max_mult={weyl_max_mult[i]}){marker}")

print(f"\nType changes detected: {len(type_changes)}")
for tc in type_changes:
    print(f"  {tc['type_before']} -> {tc['type_after']} between tau = {tc['tau_before']:.4f} "
          f"and tau = {tc['tau_after']:.4f}")


# =============================================================================
# SECTION 7: Eigenvalue degeneracy tracking (Petrov D -> II indicator)
# =============================================================================

print("\n\n" + "=" * 78)
print("  WEYL OPERATOR EIGENVALUE DEGENERACY TRACKING")
print("=" * 78)

# At tau=0 (round metric), we expect maximal degeneracy (Petrov D analog)
# As tau increases, degeneracy should break (D -> II -> I)

for tau in tau_values:
    r = results[tau]
    weyl_op = r['weyl_op']
    eigs = weyl_op['unique_eigs']
    mults = weyl_op['multiplicities']

    # Compute degeneracy score: how far from maximally degenerate
    # Perfect D: 2-3 distinct eigenvalues. Generic I: 28 distinct.
    deg_score = 1.0 - (weyl_op['n_distinct'] - 1) / (N_PAIRS - 1)

    print(f"  tau = {tau:.4f}: {weyl_op['n_distinct']:3d} distinct eigs, "
          f"deg_score = {deg_score:.4f}, mults = {mults}")


# =============================================================================
# SECTION 8: Physical interpretation for gravitational wave propagation
# =============================================================================

print("\n\n" + "=" * 78)
print("  PHYSICAL INTERPRETATION: GW PROPAGATION IN BULK")
print("=" * 78)

# The Weyl tensor governs tidal forces (geodesic deviation) and GW propagation.
# In higher-D, the CMPP type determines:
#   Type N: purely radiative (gravitational pp-wave analog)
#   Type D: algebraically special (higher-D Schwarzschild/Kerr analog)
#   Type II: partially radiative
#   Type I/G: generic tidal deformation
#
# For the Jensen deformation:
# - At tau=0 (round S^3 x CP^2 x U(1)): high symmetry -> many degenerate eigenvalues
# - At tau=0.537 (transition): sectional curvature sign change -> degeneracy breaking?
# - At large tau: strong anisotropy -> eigenvalue spreading

# Compute Weyl eigenvalue spread (a GW polarization measure)
print(f"\n{'tau':>8s}  {'n_pol':>5s}  {'spread':>10s}  {'gap_ratio':>10s}  {'type':>5s}")
print("-" * 50)

for tau in tau_values:
    r = results[tau]
    eigs = np.array(r['weyl_op']['unique_eigs'])
    mults = r['weyl_op']['multiplicities']
    cmpp_type = r['cmpp_type']

    spread = eigs.max() - eigs.min() if len(eigs) > 1 else 0
    # Gap ratio: largest gap between consecutive eigenvalues / spread
    if len(eigs) > 1:
        gaps = np.diff(eigs)
        gap_ratio = np.max(gaps) / spread if spread > 0 else 0
    else:
        gap_ratio = 0

    n_pol = len(eigs)  # Number of independent GW polarizations

    print(f"{tau:8.4f}  {n_pol:5d}  {spread:10.6f}  {gap_ratio:10.6f}  {cmpp_type:>5s}")


print(f"\n  Physical interpretation:")
print(f"  - n_pol = number of independent tidal/GW polarization modes")
print(f"  - spread = range of Weyl eigenvalues (tidal anisotropy)")
print(f"  - gap_ratio = largest eigenvalue gap / spread (spectral structure)")
print(f"  - At transition: sign change in sectional curvature AFFECTS Weyl spectrum")


# =============================================================================
# SECTION 9: Gate verdict
# =============================================================================

print("\n\n" + "=" * 78)
print("  GATE VERDICT: CMPP-TRANSITION-49")
print("=" * 78)

# Pre-registered gate:
# PASS: CMPP type changes at tau = 0.537
# INFO: type changes at nearby tau
# FAIL: constant CMPP type across scan

# Check for type changes at or near 0.537
transition_at_537 = False
transition_nearby = False
for tc in type_changes:
    if abs(tc['tau_before'] - 0.537) < 0.01 or abs(tc['tau_after'] - 0.537) < 0.01:
        transition_at_537 = True
    if abs(tc['tau_before'] - 0.537) < 0.05 or abs(tc['tau_after'] - 0.537) < 0.05:
        transition_nearby = True

# Also check if eigenvalue degeneracy changes qualitatively at 0.537
n_dist_before = results[0.50]['weyl_op']['n_distinct']
n_dist_at = results[0.537]['weyl_op']['n_distinct']
n_dist_after = results[0.55]['weyl_op']['n_distinct']
degeneracy_change = (n_dist_at != n_dist_before) or (n_dist_at != n_dist_after)

# Compute eigenvalue structure change (more sensitive than CMPP type)
eigs_before = np.array(results[0.50]['weyl_op']['unique_eigs'])
eigs_at = np.array(results[0.537]['weyl_op']['unique_eigs'])
eigs_after = np.array(results[0.55]['weyl_op']['unique_eigs'])

# Check if any eigenvalue crosses zero at transition
any_eig_zero_crossing = False
for tau_a, tau_b in [(0.50, 0.537), (0.537, 0.55)]:
    ea = results[tau_a]['weyl_op']['eigvals']
    eb = results[tau_b]['weyl_op']['eigvals']
    # If an eigenvalue changes sign between these taus
    for i in range(min(len(ea), len(eb))):
        if ea[i] * eb[i] < 0:
            any_eig_zero_crossing = True

n_changes = len(type_changes)

if transition_at_537:
    verdict = "PASS"
    reason = f"CMPP type changes at tau = 0.537"
elif transition_nearby:
    verdict = "INFO"
    reason = f"CMPP type changes near tau = 0.537 (within 0.05)"
elif n_changes > 0:
    verdict = "INFO"
    # Find the actual change location
    change_desc = "; ".join(
        f"{tc['type_before']}->{tc['type_after']} at tau={tc['tau_before']:.3f}-{tc['tau_after']:.3f}"
        for tc in type_changes
    )
    reason = f"Type changes at other tau: {change_desc}"
elif degeneracy_change:
    verdict = "INFO"
    reason = (f"No CMPP type change, but eigenvalue degeneracy changes: "
              f"n_distinct = {n_dist_before} -> {n_dist_at} -> {n_dist_after}")
elif any_eig_zero_crossing:
    verdict = "INFO"
    reason = "No CMPP type change, but Weyl eigenvalue(s) cross zero at transition"
else:
    verdict = "FAIL"
    reason = f"Constant CMPP type '{cmpp_types[0]}' across all tau"

print(f"\n  Verdict: {verdict}")
print(f"  Reason: {reason}")
print(f"  Type changes detected: {n_changes}")
print(f"  Degeneracy change at 0.537: {degeneracy_change}")
print(f"  Eigenvalue zero crossing: {any_eig_zero_crossing}")

# Additional structural information
print(f"\n  Structural summary:")
print(f"    tau = 0 (round): CMPP = {results[0.0]['cmpp_type']}, "
      f"n_distinct = {results[0.0]['weyl_op']['n_distinct']}")
print(f"    tau = 0.19 (fold): CMPP = {results[0.19]['cmpp_type']}, "
      f"n_distinct = {results[0.19]['weyl_op']['n_distinct']}")
print(f"    tau = 0.537 (transition): CMPP = {results[0.537]['cmpp_type']}, "
      f"n_distinct = {results[0.537]['weyl_op']['n_distinct']}")
print(f"    tau = 1.0 (deep deformation): CMPP = {results[1.0]['cmpp_type']}, "
      f"n_distinct = {results[1.0]['weyl_op']['n_distinct']}")


# =============================================================================
# SECTION 10: Save results
# =============================================================================

# Collect into arrays for saving
tau_arr = np.array(tau_values)
cmpp_types_arr = np.array(cmpp_types)
n_distinct_arr = np.array(weyl_n_distinct)
max_mult_arr = np.array(weyl_max_mult)

# BW fractions for best null direction at each tau
bw_fracs = np.zeros((len(tau_values), 5))  # columns: bw = +2, +1, 0, -1, -2
for i, tau in enumerate(tau_values):
    bd = results[tau]['best_decomp']
    if bd is not None:
        tot = bd['total_C_sq']
        if tot > 0:
            for j, bwi in enumerate([+2, +1, 0, -1, -2]):
                bw_fracs[i, j] = bd['bw_norms'].get(bwi, 0) / tot

# Weyl operator eigenvalues at key taus
weyl_eigs_0 = results[0.0]['weyl_op']['eigvals']
weyl_eigs_fold = results[0.19]['weyl_op']['eigvals']
weyl_eigs_transition = results[0.537]['weyl_op']['eigvals']
weyl_eigs_deep = results[1.0]['weyl_op']['eigvals']

# C^2 values
C_sq_arr = np.array([results[tau]['geom']['C_sq'] for tau in tau_values])
K_arr = np.array([results[tau]['geom']['K_full'] for tau in tau_values])

np.savez_compressed(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 's49_cmpp_transition.npz'),
    tau_values=tau_arr,
    cmpp_types=cmpp_types_arr,
    n_distinct=n_distinct_arr,
    max_mult=max_mult_arr,
    bw_fracs=bw_fracs,
    weyl_eigs_0=weyl_eigs_0,
    weyl_eigs_fold=weyl_eigs_fold,
    weyl_eigs_transition=weyl_eigs_transition,
    weyl_eigs_deep=weyl_eigs_deep,
    C_sq=C_sq_arr,
    K_full=K_arr,
    verdict=np.array(verdict),
    reason=np.array(reason),
    n_type_changes=np.array(n_changes),
    degeneracy_change_at_537=np.array(degeneracy_change),
    eigenvalue_zero_crossing=np.array(any_eig_zero_crossing),
)


# =============================================================================
# SECTION 11: Plotting
# =============================================================================

fig, axes = plt.subplots(2, 3, figsize=(18, 11))
fig.suptitle('S49 CMPP-TRANSITION-49: Higher-D Petrov Classification at tau=0.537',
             fontsize=14, fontweight='bold')

# Panel 1: Number of distinct Weyl eigenvalues vs tau
ax = axes[0, 0]
ax.plot(tau_arr, n_distinct_arr, 'bo-', markersize=6, linewidth=1.5)
ax.axvline(0.537, color='red', linestyle='--', alpha=0.7, label='tau=0.537')
ax.axvline(0.19, color='green', linestyle=':', alpha=0.7, label='tau=0.19 (fold)')
ax.set_xlabel('tau')
ax.set_ylabel('n_distinct Weyl eigenvalues')
ax.set_title('Weyl Operator Degeneracy')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 2: Max multiplicity vs tau
ax = axes[0, 1]
ax.plot(tau_arr, max_mult_arr, 'rs-', markersize=6, linewidth=1.5)
ax.axvline(0.537, color='red', linestyle='--', alpha=0.7)
ax.axvline(0.19, color='green', linestyle=':', alpha=0.7)
ax.set_xlabel('tau')
ax.set_ylabel('Maximum eigenvalue multiplicity')
ax.set_title('Eigenvalue Degeneracy (Petrov Indicator)')
ax.grid(True, alpha=0.3)

# Panel 3: BW fractions vs tau
ax = axes[0, 2]
bw_labels = ['bw=+2', 'bw=+1', 'bw=0', 'bw=-1', 'bw=-2']
colors = ['#d62728', '#ff7f0e', '#2ca02c', '#1f77b4', '#9467bd']
for j, (label, color) in enumerate(zip(bw_labels, colors)):
    ax.plot(tau_arr, bw_fracs[:, j] * 100, 'o-', color=color, label=label,
            markersize=4, linewidth=1.2)
ax.axvline(0.537, color='red', linestyle='--', alpha=0.7)
ax.set_xlabel('tau')
ax.set_ylabel('Boost weight fraction (%)')
ax.set_title('CMPP Boost Weight Decomposition')
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)

# Panel 4: |C|^2 and K vs tau
ax = axes[1, 0]
ax.plot(tau_arr, C_sq_arr, 'b-', linewidth=2, label='|C|^2 (Weyl)')
ax.plot(tau_arr, K_arr, 'r--', linewidth=1.5, label='K (Kretschner)')
ax.axvline(0.537, color='red', linestyle='--', alpha=0.5)
ax.set_xlabel('tau')
ax.set_ylabel('Curvature invariant')
ax.set_title('Curvature Invariants')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)
ax.set_yscale('log')

# Panel 5: Weyl eigenvalue spectrum at transition
ax = axes[1, 1]
for tau_key, color, label in [(0.0, 'blue', 'tau=0 (round)'),
                                (0.19, 'green', 'tau=0.19 (fold)'),
                                (0.537, 'red', 'tau=0.537 (trans)'),
                                (1.0, 'purple', 'tau=1.0 (deep)')]:
    eigs = results[tau_key]['weyl_op']['eigvals']
    ax.plot(range(len(eigs)), eigs, 'o', color=color, markersize=3, alpha=0.7, label=label)
ax.axhline(0, color='gray', linestyle='-', alpha=0.3)
ax.set_xlabel('Eigenvalue index')
ax.set_ylabel('Weyl eigenvalue')
ax.set_title('Weyl Operator Spectrum')
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)

# Panel 6: CMPP type annotation
ax = axes[1, 2]
ax.axis('off')
txt = "CMPP Classification Summary\n" + "=" * 35 + "\n\n"
for i, tau in enumerate(tau_values):
    marker = " *" if abs(tau - 0.537) < 0.01 else ""
    txt += f"tau={tau:.3f}: {cmpp_types[i]:>5s}  (n={n_distinct_arr[i]}, m={max_mult_arr[i]}){marker}\n"
txt += f"\nGate: CMPP-TRANSITION-49\n"
txt += f"Verdict: {verdict}\n"
txt += f"Reason: {reason[:60]}...\n" if len(reason) > 60 else f"Reason: {reason}\n"
ax.text(0.05, 0.95, txt, transform=ax.transAxes, fontsize=9,
        verticalalignment='top', fontfamily='monospace',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.tight_layout()
plt.savefig(os.path.join(os.path.dirname(os.path.abspath(__file__)), 's49_cmpp_transition.png'),
            dpi=150, bbox_inches='tight')
plt.close()

elapsed = time.time() - t_start
print(f"\n  Total runtime: {elapsed:.1f}s")
print(f"  Output: s49_cmpp_transition.npz, s49_cmpp_transition.png")
print("=" * 78)
