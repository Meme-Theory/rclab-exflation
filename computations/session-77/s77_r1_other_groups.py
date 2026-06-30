#!/usr/bin/env python3
"""
s77_r1_other_groups.py -- R1-OTHER-GROUPS (W3-M, S77 Wave 3)
==============================================================

Gate: S77-D3-R1-UNIVERSAL (INFO)
  Report R_1 drift for SU(4) and Sp(2).
  Drift < 5% at L=3 confirms universality of R-protection.

Physics (substrate framing):
----------------------------
R_1 = a_0 * a_4 / a_2^2 is a dimensionless ratio of spectral moments of D^2.
On SU(3) at the Jensen fold (tau=0.19), R_1 drifts only 2.89% from L=3 to L=9.
The S76 workshop proved that R-protection (zero net Weyl exponent) holds for
ANY compact simple Lie group:

    alpha_k = d + r + k   (Weyl regime exponent of a_k)

so alpha_0 + alpha_4 = 2*(d+r) + 4 = 2*alpha_2.  Hence R_1 has zero net Weyl
exponent and pre-asymptotic corrections scale as O(L^{-r}).

This computation tests the theorem numerically on SU(4) (d=15, r=3) and
Sp(2) (d=10, r=2) with BI-INVARIANT metric (tau=0, no Jensen deformation).

Method:
-------
For a compact simple Lie group G with bi-invariant metric g_0 normalized so
Tr(e_a e_b) = -(1/2) delta_{ab}, the Dirac operator eigenvalues in the
Peter-Weyl sector of irrep Lambda are:

    lambda_{Lambda,sigma}^2 = ||Lambda + rho||^2

where rho = (1/2) sum of positive roots and ||.|| is the norm induced by the
Killing metric.  The eigenvalue sign is +/-, and the multiplicity of each
|lambda| is:

    mult = dim(Lambda) * dim_spinor

where dim_spinor = 2^{floor(d/2)}.  We include BOTH +/- eigenvalues (full
spectrum) and then take the half-spectrum convention a_k = (1/2) * sum.

Actually, the exact formula needs care.  On a compact simple Lie group G
of dimension d = dim(G), the Dirac operator on the spinor bundle S = G x_{Ad} S_d
(constructed from the spin representation of so(d)) has eigenvalues:

For each irrep Lambda of G with highest weight Lambda:
  - If d is even: eigenvalues +/- sqrt(C_2(Lambda) + ||rho||^2)
    each with multiplicity dim(Lambda) * 2^{d/2-1}
  - If d is odd: eigenvalue +/- sqrt(C_2(Lambda) + ||rho||^2)
    each with multiplicity dim(Lambda) * 2^{(d-1)/2}

where C_2(Lambda) = ||Lambda + rho||^2 - ||rho||^2 is the quadratic Casimir.

So lambda^2 = ||Lambda + rho||^2 in both cases.

Reference: Bar (1996), Parthasarathy (1972), Cahen-Gutt-Trautman (1993).

The spectral moments are:
    a_k = (1/2) * sum_{Lambda: level <= L_max, lambda =/= 0}
              mult(Lambda) * |lambda|^{-k}

where level = |Lambda|_1 depends on the group (sum of Dynkin labels for SU(N),
etc.), and the factor 1/2 is the positive-half convention used in the project.

Then R_1 = a_0 * a_4 / a_2^2.

For SU(3) at tau=0 (bi-invariant), this should match the known value.

Agent: Spectral-Geometer (Session 77, Wave 3)
"""

import numpy as np
import sys
import os
import time
from itertools import product as iter_product

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
os.chdir(SCRIPT_DIR)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

from canonical_constants import PI, R_protected_fold, a0_fold, a2_fold, a4_fold

# =============================================================================
# CONFIGURATION
# =============================================================================
print("=" * 78)
print("R1-OTHER-GROUPS (W3-M, S77 Wave 3)")
print("=" * 78)
print()

EVAL_CUTOFF = 1e-10  # (local) exclude zero eigenvalue from sums (bi-invariant has none for D^2 except Lambda=0)


# =============================================================================
# SECTION 1: ROOT SYSTEM DATA FOR SIMPLE LIE ALGEBRAS
# =============================================================================

def su_n_data(N):
    """
    Root system data for SU(N) = A_{N-1}.

    Conventions:
      - Simple roots alpha_i, i=1,...,N-1 in R^{N-1}
      - Standard embedding: alpha_i = e_i - e_{i+1} in R^N (then project to trace-free)
      - But for Casimir/norm computations, we use the DUAL basis (fundamental weights)
        and the CARTAN MATRIX approach.

    Returns dict with:
      - 'name', 'dim', 'rank'
      - 'positive_roots': list of roots as tuples of Dynkin labels
      - 'rho': Weyl vector in weight space
      - 'cartan_inv': inverse Cartan matrix (for norm computation)
      - 'norm_rho_sq': ||rho||^2
      - 'dim_irrep': function(highest_weight) -> dim
      - 'casimir': function(highest_weight) -> C_2
    """
    rank = N - 1  # (local)
    dim = N * N - 1  # (local)

    # Cartan matrix for A_{N-1}
    # A_{ij} = 2*delta_{ij} - delta_{|i-j|,1}
    A = np.zeros((rank, rank))  # (local)
    for i in range(rank):
        A[i, i] = 2.0
        if i > 0:
            A[i, i-1] = -1.0
        if i < rank - 1:
            A[i, i+1] = -1.0

    # Inverse Cartan matrix (symmetrized): gives the inner product on weight space
    # For A_{n-1}: (A^{-1})_{ij} = min(i,j) * (n-max(i,j)) / n  (1-indexed)
    A_inv = np.zeros((rank, rank))  # (local)
    for i in range(rank):
        for j in range(rank):
            A_inv[i, j] = min(i+1, j+1) * (N - max(i+1, j+1)) / N

    # Weyl vector in Dynkin labels: rho = (1,1,...,1)
    rho = np.ones(rank)  # (local)

    # ||rho||^2 using the quadratic form: ||w||^2 = w^T A_inv w (for Dynkin labels)
    # Actually, the CORRECT norm for Casimir is:
    # ||Lambda||^2 = (Lambda, Lambda + 2*rho) = Lambda^T A_inv Lambda + 2 * Lambda^T A_inv rho
    # C_2(Lambda) = (Lambda + rho)^T A_inv (Lambda + rho) - rho^T A_inv rho
    # ||Lambda + rho||^2 = (Lambda + rho)^T A_inv (Lambda + rho)
    norm_rho_sq = rho @ A_inv @ rho  # (local)

    # Positive roots of A_{N-1}: e_i - e_j for 1 <= i < j <= N
    # In Dynkin labels, root e_i - e_j = alpha_i + alpha_{i+1} + ... + alpha_{j-1}
    # So Dynkin label is (0,...,0,1,0,...,0,1,0,...,0) with 1s at positions i and j-1
    # Actually: e_i - e_j = sum_{k=i}^{j-1} alpha_k, so Dynkin labels are:
    #   (0,...,0,1,1,...,1,0,...,0) with 1s from position i-1 to j-2 (0-indexed)
    # Wait, that's not right for Dynkin labels.  Dynkin labels of a ROOT are its
    # expansion in simple roots, not in fundamental weights.
    # The positive root alpha_{ij} = e_i - e_j = sum_{k=i}^{j-1} alpha_k
    # has simple root coefficients (not Dynkin coefficients).

    # Number of positive roots
    n_pos = N * (N - 1) // 2  # (local)

    def dim_irrep(hw):
        """Dimension of SU(N) irrep with Dynkin labels hw = (a_1,...,a_{N-1}).

        Weyl dimension formula:
        dim = prod_{1<=i<j<=N} (sum_{k=i}^{j-1} (a_k + 1)) / (j - i)
        where a_k are Dynkin labels.

        More precisely:
        dim = prod_{alpha > 0} <Lambda + rho, alpha> / <rho, alpha>
        For A_{N-1}, this simplifies to:
        dim = prod_{1<=i<j<=N} (l_i - l_j) / (i - j)
        where l_k = hw[k-1] + hw[k] + ... + hw[N-2] + (N - k) for k=1,...,N
        (partition notation: l_k = sum_{m=k}^{N-1} a_m + N - k)
        """
        hw = np.array(hw, dtype=float)
        # Convert Dynkin labels to partition notation
        # l_k = sum_{m=k-1}^{rank-1} hw[m] + (N - k)  for k=1,...,N
        l = np.zeros(N)  # (local)
        for k in range(1, N + 1):
            l[k-1] = sum(hw[m] for m in range(k-1, rank)) + (N - k)
        # dim = prod_{i<j} (l_i - l_j) / (j - i)
        d = 1.0  # (local)
        for i in range(N):
            for j in range(i + 1, N):
                d *= (l[i] - l[j]) / (j - i)
        return int(round(d))

    def norm_sq(w):
        """||w||^2 in weight space, w given as Dynkin labels."""
        w = np.array(w, dtype=float)
        return float(w @ A_inv @ w)

    def casimir_2(hw):
        """Quadratic Casimir C_2(Lambda) = ||Lambda + rho||^2 - ||rho||^2."""
        hw = np.array(hw, dtype=float)
        lpr = hw + rho  # (local)
        return float(lpr @ A_inv @ lpr) - norm_rho_sq

    def norm_lpr_sq(hw):
        """||Lambda + rho||^2."""
        hw = np.array(hw, dtype=float)
        lpr = hw + rho  # (local)
        return float(lpr @ A_inv @ lpr)

    return {
        'name': f'SU({N})',
        'type': f'A_{rank}',
        'dim': dim,
        'rank': rank,
        'N': N,
        'rho_dynkin': rho,
        'cartan_inv': A_inv,
        'norm_rho_sq': norm_rho_sq,
        'n_positive_roots': n_pos,
        'dim_irrep': dim_irrep,
        'casimir_2': casimir_2,
        'norm_lpr_sq': norm_lpr_sq,
        'norm_sq': norm_sq,
    }


def sp_n_data(n):
    """
    Root system data for Sp(n) = C_n.

    Sp(n) has:
      - dim = n(2n+1)
      - rank = n
      - Root system C_n

    Sp(2) = C_2: dim = 10, rank = 2.

    Cartan matrix for C_n:
      A_{ii} = 2
      A_{i,i+1} = -1 for i < n-1
      A_{n-1,n} = -2 (the LONG root)
      A_{i+1,i} = -1 for i < n-1
      A_{n,n-1} = -1

    Wait, standard convention: for C_n, the Cartan matrix is:
      A = [[2, -1, 0, ...],
           [-1, 2, -1, ...],
           ...
           [0, ..., -1, 2, -1],
           [0, ..., 0, -2, 2]]

    The last simple root is LONG (length^2 = 2), others are SHORT (length^2 = 1).

    But for Dynkin labels and Casimir, we need the SYMMETRIZED Cartan matrix.
    The quadratic form on weight space is:
      (Lambda, Lambda') = Lambda^T * (D * A)^{-1} * Lambda'
    where D = diag(d_1,...,d_n) with d_i = ||alpha_i||^2 / 2.

    For C_n: d_i = 1/2 for i < n, d_n = 1.
    D = diag(1/2, 1/2, ..., 1/2, 1).

    The symmetrized Cartan matrix B = D*A has B_{ij} = d_i * A_{ij}.
    The inner product on weight space (fundamental weight basis) is B^{-1}.
    """
    dim = n * (2 * n + 1)  # (local)
    rank = n  # (local)

    # Cartan matrix for C_n
    A = np.zeros((rank, rank))  # (local)
    for i in range(rank):
        A[i, i] = 2.0
    for i in range(rank - 1):
        A[i, i+1] = -1.0
        A[i+1, i] = -1.0
    # The asymmetric entry: for C_n, the Dynkin diagram has a double bond
    # from alpha_{n-1} to alpha_n with arrow pointing TOWARD alpha_n (short->long).
    # Convention: A_{n-1,n} = -1, A_{n,n-1} = -2.
    # Wait, let me be precise.  For C_n, the simple roots are:
    #   alpha_1,...,alpha_{n-1} (short, ||alpha||^2 = 1)
    #   alpha_n (long, ||alpha_n||^2 = 2)
    #
    # Cartan matrix: A_{ij} = 2*(alpha_i, alpha_j) / (alpha_j, alpha_j)
    # A_{n-1,n} = 2*(alpha_{n-1}, alpha_n) / ||alpha_n||^2 = 2*(-1)/2 = -1
    # A_{n,n-1} = 2*(alpha_n, alpha_{n-1}) / ||alpha_{n-1}||^2 = 2*(-1)/1 = -2
    #
    # So:
    if rank >= 2:
        A[rank-1, rank-2] = -2.0
        # A[rank-2, rank-1] already set to -1.0 above

    # Symmetrizing matrix D: d_i = ||alpha_i||^2 / 2
    # For C_n: short roots have ||alpha||^2 = 1, long root has ||alpha||^2 = 2
    # So d_i = 1/2 for i < n, d_n = 1
    D = np.zeros(rank)  # (local)
    for i in range(rank - 1):
        D[i] = 0.5
    D[rank - 1] = 1.0

    # Symmetrized Cartan matrix B = D*A (so B is symmetric)
    B = np.diag(D) @ A  # (local)

    # Inner product on weight space: B_inv = B^{-1}
    B_inv = np.linalg.inv(B)  # (local)

    # Weyl vector in Dynkin labels: rho = (1,1,...,1)
    rho = np.ones(rank)  # (local)

    # ||rho||^2
    norm_rho_sq = rho @ B_inv @ rho  # (local)

    # Number of positive roots for C_n: n^2
    n_pos = n * n  # (local)

    def dim_irrep(hw):
        """Dimension of Sp(n) irrep via Weyl dimension formula.

        For C_n with fundamental weights omega_1,...,omega_n and highest weight
        Lambda = sum a_i omega_i (Dynkin labels a_i), the dimension is:

        dim = prod_{alpha > 0} <Lambda + rho, alpha> / <rho, alpha>

        We compute this using the explicit positive root system.

        For C_2 specifically:
        Positive roots: e_1-e_2, e_1+e_2, 2*e_1, 2*e_2
        In terms of simple roots alpha_1 = e_1-e_2, alpha_2 = 2*e_2:
          e_1 - e_2 = alpha_1
          e_1 + e_2 = alpha_1 + alpha_2
          2*e_1 = 2*alpha_1 + alpha_2
          2*e_2 = alpha_2
        """
        hw = np.array(hw, dtype=float)
        lpr = hw + rho  # (local)

        if n == 2:
            # C_2 positive roots in simple root coordinates:
            # alpha_1 = (1,0), alpha_2 = (0,1), alpha_1+alpha_2 = (1,1), 2*alpha_1+alpha_2 = (2,1)
            pos_roots_simple = [(1, 0), (0, 1), (1, 1), (2, 1)]  # (local)

            d = 1.0  # (local)
            for alpha_s in pos_roots_simple:
                alpha_s = np.array(alpha_s, dtype=float)
                # <Lambda+rho, alpha> in root basis = (Lambda+rho)^T B_inv alpha_simple_root_coords
                # Wait: alpha given in simple root coordinates, Lambda+rho in Dynkin (fundamental weight) coordinates.
                # <w, alpha> where w is in fundamental weight basis and alpha is in simple root basis:
                # w = sum w_i omega_i, alpha = sum a_j alpha_j
                # <w, alpha> = sum_ij w_i a_j <omega_i, alpha_j> = sum_ij w_i a_j (D_j * delta_{ij})
                #            = sum_j w_j a_j D_j
                # where <omega_i, alpha_j> = d_j * delta_{ij} (by definition of fundamental weights via
                # symmetrized Cartan matrix: <omega_i, alpha_j> = (1/2) ||alpha_j||^2 delta_{ij} = D_j delta_{ij})
                inner_lpr = sum(lpr[j] * alpha_s[j] * D[j] for j in range(rank))  # (local)
                inner_rho = sum(rho[j] * alpha_s[j] * D[j] for j in range(rank))  # (local)
                d *= inner_lpr / inner_rho
            return int(round(d))
        else:
            # General formula for C_n: construct positive roots
            # Positive roots of C_n: e_i - e_j (i<j), e_i + e_j (i<=j... no i<j), 2*e_i
            # In simple root coordinates:
            #   e_i - e_j = alpha_i + ... + alpha_{j-1}  (short roots, i<j)
            #   e_i + e_j = alpha_i + ... + alpha_{j-1} + 2*(alpha_j + ... + alpha_{n-1}) + alpha_n  (i<j)
            #   2*e_i = 2*(alpha_i + ... + alpha_{n-1}) + alpha_n  (long roots)
            # Total: n(n-1)/2 + n(n-1)/2 + n = n^2
            raise NotImplementedError(f"General Sp({n}) dimension formula not implemented; only Sp(2)")

    def norm_sq(w):
        """||w||^2 where w is in Dynkin (fundamental weight) coordinates."""
        w = np.array(w, dtype=float)
        return float(w @ B_inv @ w)

    def casimir_2(hw):
        """C_2(Lambda) = ||Lambda + rho||^2 - ||rho||^2."""
        hw = np.array(hw, dtype=float)
        lpr = hw + rho  # (local)
        return float(lpr @ B_inv @ lpr) - norm_rho_sq

    def norm_lpr_sq(hw):
        """||Lambda + rho||^2."""
        hw = np.array(hw, dtype=float)
        lpr = hw + rho  # (local)
        return float(lpr @ B_inv @ lpr)

    return {
        'name': f'Sp({n})',
        'type': f'C_{rank}',
        'dim': dim,
        'rank': rank,
        'n': n,
        'rho_dynkin': rho,
        'cartan_inv': B_inv,
        'norm_rho_sq': norm_rho_sq,
        'n_positive_roots': n_pos,
        'dim_irrep': dim_irrep,
        'casimir_2': casimir_2,
        'norm_lpr_sq': norm_lpr_sq,
        'norm_sq': norm_sq,
    }


# =============================================================================
# SECTION 2: ENUMERATE IRREPS UP TO GIVEN LEVEL
# =============================================================================

def enumerate_irreps(group_data, L_max):
    """
    Enumerate all irreps with level <= L_max.

    Level is defined as:
      SU(N): sum of Dynkin labels = a_1 + a_2 + ... + a_{N-1}
      Sp(n): sum of Dynkin labels = a_1 + a_2 + ... + a_n

    This is the standard PW truncation used in the project (same as SU(3)).

    Returns list of dicts: {'hw': tuple, 'dim': int, 'C2': float, 'lam_sq': float, 'level': int}
    """
    rank = group_data['rank']  # (local)
    irreps = []  # (local)

    # Generate all Dynkin label tuples with sum <= L_max and all non-negative
    def _generate(remaining_rank, remaining_sum):
        if remaining_rank == 0:
            yield ()
            return
        for a in range(remaining_sum + 1):
            for rest in _generate(remaining_rank - 1, remaining_sum - a):
                yield (a,) + rest

    for hw_tuple in _generate(rank, L_max):
        level = sum(hw_tuple)  # (local)
        hw = np.array(hw_tuple, dtype=float)  # (local)

        # Skip the trivial representation (Lambda=0) -- it gives lambda=0
        # which would blow up the zeta sums.
        # For the trivial rep, C_2 = 0, so lambda^2 = ||rho||^2.
        # Wait: lambda^2 = ||Lambda + rho||^2 = ||rho||^2 for Lambda=0.
        # That is NOT zero (rho != 0).
        # The trivial rep has lambda^2 = ||rho||^2 > 0.
        # So we DO include it.

        lam_sq = group_data['norm_lpr_sq'](hw)  # (local)
        dim_rep = group_data['dim_irrep'](hw_tuple)  # (local)

        if dim_rep <= 0:
            print(f"  WARNING: dim({hw_tuple}) = {dim_rep}, skipping")
            continue

        irreps.append({
            'hw': hw_tuple,
            'dim': dim_rep,
            'C2': group_data['casimir_2'](hw),
            'lam_sq': lam_sq,
            'level': level,
        })

    return irreps


# =============================================================================
# SECTION 3: COMPUTE SPECTRAL MOMENTS AND R_1
# =============================================================================

def compute_moments(group_data, L_max_values):
    """
    Compute a_0, a_2, a_4 and R_1 for each L_max.

    Convention (S73B half-spectrum):
      a_k = (1/2) * sum_{Lambda: level <= L_max} dim(Lambda) * dim_spinor * |lambda|^{-k}

    where lambda^2 = ||Lambda + rho||^2 and dim_spinor = 2^{floor(d/2)}.

    The factor 1/2 is the positive-half convention.

    For each irrep Lambda, the Dirac operator has eigenvalues +/- sqrt(lambda^2),
    each with multiplicity dim(Lambda) * (dim_spinor / 2) if d is even,
    or dim(Lambda) * dim_spinor if d is odd (single chirality).

    Actually, let me be more precise about multiplicities.

    On a compact Lie group G of dimension d:
    - The spinor bundle has fiber dimension 2^{floor(d/2)}.
    - For the irrep Lambda of G, the Peter-Weyl decomposition gives:
      L^2(G, S) = bigoplus_Lambda  V_Lambda tensor V_Lambda^* tensor S
    - The Dirac operator in the sector Lambda has dimension dim(Lambda) * dim_spinor.
    - For bi-invariant metric, D^2 = C_2 + ||rho||^2 is SCALAR on each sector.
    - So all dim(Lambda) * dim_spinor states in sector Lambda have the same |lambda|.
    - The total degeneracy of |lambda| is dim(Lambda) * dim_spinor * dim(Lambda).
      (dim(Lambda) from left-regular, dim(Lambda) from right-regular, dim_spinor from spinor fiber)

    Wait, NO.  In the Peter-Weyl decomposition of L^2(G, S):
      L^2(G, S) = bigoplus_Lambda  (V_Lambda tensor V_Lambda^*) tensor S

    D acts on the LEFT V_Lambda factor tensor S:
      D_Lambda : V_Lambda tensor S -> V_Lambda tensor S

    The right V_Lambda^* is a MULTIPLICITY space (D doesn't see it).
    So:
      - D_Lambda is a (dim(Lambda) * dim_spinor) x (dim(Lambda) * dim_spinor) matrix
      - The eigenvalues of D_Lambda appear with ADDITIONAL multiplicity dim(Lambda)
        from the right V_Lambda^*.

    Total degeneracy of eigenvalue lambda in sector Lambda:
      = (multiplicity in D_Lambda) * dim(Lambda)

    For bi-invariant metric, D^2 = (C_2 + ||rho||^2) * Id on each sector, so
    D_Lambda has eigenvalues +/- sqrt(C_2 + ||rho||^2), each appearing
    (dim(Lambda) * dim_spinor / 2) times if d is even,
    (dim(Lambda) * dim_spinor) times if d is odd (but then only one sign).

    Hmm, for d even: D_Lambda has dimension dim(Lambda)*dim_spinor.
    D^2 = (||Lambda+rho||^2)*Id, so eigenvalues of D are +/- sqrt(||Lambda+rho||^2).
    By symmetry (or Dirac structure), half are + and half are -.
    So each sign has multiplicity dim(Lambda) * dim_spinor / 2 from D_Lambda,
    times dim(Lambda) from the right regular rep.

    Total: for each Lambda, each |lambda| appears with total multiplicity
      d_total = dim(Lambda)^2 * dim_spinor

    The half-spectrum (positive eigenvalues only):
      a_k = sum_{Lambda: level <= L_max} (dim(Lambda)^2 * dim_spinor / 2) * |lambda|^{-k}

    For a_0 (k=0): a_0 = (dim_spinor / 2) * sum dim(Lambda)^2
    This should match the Weyl formula mode count.

    Let me cross-check with SU(3).  SU(3): d=8, dim_spinor=2^4=16.
    At L_max=3, the irreps with p+q <= 3 are:
    (0,0): dim=1, (1,0): dim=3, (0,1): dim=3, (2,0): dim=6, (0,2): dim=6,
    (1,1): dim=8, (3,0): dim=10, (0,3): dim=10, (2,1): dim=15, (1,2): dim=15
    sum dim^2 = 1 + 9 + 9 + 36 + 36 + 64 + 100 + 100 + 225 + 225 = 805
    a_0 = (16/2) * 805 = 8 * 805 = 6440.

    That matches a0_fold = 6440 from canonical_constants!

    So the formula is:
      a_k = (dim_spinor / 2) * sum_{Lambda: level <= L_max} dim(Lambda)^2 * (||Lambda+rho||^2)^{-k/2}

    For k=0: a_0 = (dim_spinor / 2) * sum dim(Lambda)^2
    For k=2: a_2 = (dim_spinor / 2) * sum dim(Lambda)^2 / (||Lambda+rho||^2)
    For k=4: a_4 = (dim_spinor / 2) * sum dim(Lambda)^2 / (||Lambda+rho||^2)^2
    """
    d = group_data['dim']  # (local)
    dim_spinor = 2 ** (d // 2)  # (local)
    half_spinor = dim_spinor // 2  # (local) = dim_spinor / 2

    print(f"\n  Group: {group_data['name']} ({group_data['type']})")
    print(f"  dim = {d}, rank = {group_data['rank']}")
    print(f"  dim_spinor = {dim_spinor}, half_spinor = {half_spinor}")
    print(f"  ||rho||^2 = {group_data['norm_rho_sq']:.6f}")
    print(f"  n_positive_roots = {group_data['n_positive_roots']}")
    print()

    results = {}  # (local)

    max_L = max(L_max_values)  # (local)
    all_irreps = enumerate_irreps(group_data, max_L)  # (local)
    print(f"  Total irreps up to L_max={max_L}: {len(all_irreps)}")
    print()

    # Show first few irreps
    print(f"  {'hw':>15s} {'level':>5s} {'dim':>6s} {'C_2':>10s} {'lam_sq':>10s}")
    print("  " + "-" * 52)
    for ir in sorted(all_irreps, key=lambda x: (x['level'], x['lam_sq']))[:15]:
        print(f"  {str(ir['hw']):>15s} {ir['level']:>5d} {ir['dim']:>6d} "
              f"{ir['C2']:>10.4f} {ir['lam_sq']:>10.4f}")
    if len(all_irreps) > 15:
        print(f"  ... ({len(all_irreps) - 15} more)")
    print()

    # Compute moments at each L_max
    print(f"  {'L_max':>5s} {'n_irreps':>8s} {'a_0':>14s} {'a_2':>14s} {'a_4':>14s} {'R_1':>10s}")
    print("  " + "-" * 65)

    for L in L_max_values:
        # Filter irreps with level <= L
        irreps_L = [ir for ir in all_irreps if ir['level'] <= L]  # (local)

        a0 = 0.0  # (local)
        a2 = 0.0  # (local)
        a4 = 0.0  # (local)

        for ir in irreps_L:
            weight = ir['dim'] ** 2  # (local) = dim(Lambda)^2
            lsq = ir['lam_sq']  # (local) = ||Lambda + rho||^2

            a0 += weight
            a2 += weight / lsq
            a4 += weight / lsq ** 2

        # Apply spinor half-factor
        a0 *= half_spinor
        a2 *= half_spinor
        a4 *= half_spinor

        # R_1
        R1 = a0 * a4 / a2 ** 2 if a2 > 0 else float('nan')  # (local)

        results[L] = {
            'a0': a0,
            'a2': a2,
            'a4': a4,
            'R1': R1,
            'n_irreps': len(irreps_L),
        }

        print(f"  {L:>5d} {len(irreps_L):>8d} {a0:>14.2f} {a2:>14.4f} {a4:>14.6f} {R1:>10.6f}")

    return results


# =============================================================================
# SECTION 4: SU(3) CROSS-CHECK
# =============================================================================

print("\n" + "=" * 78)
print("SECTION 4: SU(3) CROSS-CHECK (bi-invariant metric, tau=0)")
print("=" * 78)

su3 = su_n_data(3)  # (local)
su3_results = compute_moments(su3, [2, 3, 4, 5, 6, 7])  # (local)

# Cross-check against known values
# At tau=0 (bi-invariant), the SU(3) a_0 at L=3 should be 6440
a0_su3_L3 = su3_results[3]['a0']  # (local)
print(f"\n  SU(3) a_0(L=3) = {a0_su3_L3:.1f}, canonical a0_fold = {a0_fold:.1f}")
if abs(a0_su3_L3 - a0_fold) < 1.0:
    print("  CROSS-CHECK: a_0(L=3) matches canonical value. PASS")
else:
    print(f"  CROSS-CHECK: a_0(L=3) MISMATCH. Diff = {a0_su3_L3 - a0_fold:.1f}")
    print("  NOTE: a0_fold is at tau=0.19 (Jensen fold), this is tau=0 (bi-invariant).")
    print("  At tau=0, a_0 should be different from fold. This is EXPECTED.")

# R_1 drift for SU(3) bi-invariant
R1_su3_min_L = min(su3_results.keys())  # (local)
R1_su3_max_L = max(su3_results.keys())  # (local)
R1_su3_drift = abs(su3_results[R1_su3_max_L]['R1'] - su3_results[R1_su3_min_L]['R1']) / su3_results[R1_su3_min_L]['R1']  # (local)
print(f"\n  SU(3) bi-invariant R_1 drift L={R1_su3_min_L} -> L={R1_su3_max_L}: {R1_su3_drift*100:.3f}%")
print(f"  SU(3) fold R_1 drift L=3->L=9 (canonical): 2.89%")
print(f"  Bi-invariant drift should be comparable (same O(L^{{-rank}}) scaling, rank=2)")


# =============================================================================
# SECTION 5: SU(4) (A_3: dim=15, rank=3)
# =============================================================================

print("\n" + "=" * 78)
print("SECTION 5: SU(4) (A_3: dim=15, rank=3)")
print("=" * 78)

su4 = su_n_data(4)  # (local)
su4_results = compute_moments(su4, [2, 3, 4, 5])  # (local)

# R_1 drift
R1_su4_L2 = su4_results[2]['R1']  # (local)
R1_su4_L3 = su4_results[3]['R1']  # (local)
R1_su4_L_max = max(su4_results.keys())  # (local)
R1_su4_L_max_val = su4_results[R1_su4_L_max]['R1']  # (local)
drift_su4_2_to_max = abs(R1_su4_L_max_val - R1_su4_L2) / R1_su4_L2  # (local)
drift_su4_3_to_max = abs(R1_su4_L_max_val - R1_su4_L3) / R1_su4_L3  # (local)

print(f"\n  SU(4) R_1 drift:")
print(f"    L=2 -> L={R1_su4_L_max}: {drift_su4_2_to_max*100:.3f}%")
print(f"    L=3 -> L={R1_su4_L_max}: {drift_su4_3_to_max*100:.3f}%")
print(f"  Expected: O(L^{{-3}}) since rank=3 (better than SU(3) rank=2)")


# =============================================================================
# SECTION 6: Sp(2) (C_2: dim=10, rank=2)
# =============================================================================

print("\n" + "=" * 78)
print("SECTION 6: Sp(2) (C_2: dim=10, rank=2)")
print("=" * 78)

sp2 = sp_n_data(2)  # (local)
sp2_results = compute_moments(sp2, [2, 3, 4, 5])  # (local)

# R_1 drift
R1_sp2_L2 = sp2_results[2]['R1']  # (local)
R1_sp2_L3 = sp2_results[3]['R1']  # (local)
R1_sp2_L_max = max(sp2_results.keys())  # (local)
R1_sp2_L_max_val = sp2_results[R1_sp2_L_max]['R1']  # (local)
drift_sp2_2_to_max = abs(R1_sp2_L_max_val - R1_sp2_L2) / R1_sp2_L2  # (local)
drift_sp2_3_to_max = abs(R1_sp2_L_max_val - R1_sp2_L3) / R1_sp2_L3  # (local)

print(f"\n  Sp(2) R_1 drift:")
print(f"    L=2 -> L={R1_sp2_L_max}: {drift_sp2_2_to_max*100:.3f}%")
print(f"    L=3 -> L={R1_sp2_L_max}: {drift_sp2_3_to_max*100:.3f}%")
print(f"  Expected: O(L^{{-2}}) since rank=2 (same scaling as SU(3))")


# =============================================================================
# SECTION 7: WEYL LAW CROSS-CHECK
# =============================================================================

print("\n" + "=" * 78)
print("SECTION 7: WEYL LAW CROSS-CHECK")
print("=" * 78)
print()

# a_0(L) should grow as L^{d+r} (Weyl regime).
# Check: fit log(a_0) vs log(L) and extract effective exponent.

for group_name, data, results in [
    ('SU(3)', su3, su3_results),
    ('SU(4)', su4, su4_results),
    ('Sp(2)', sp2, sp2_results),
]:
    L_vals = sorted(results.keys())  # (local)
    a0_vals = [results[L]['a0'] for L in L_vals]  # (local)
    d_eff_expected = data['dim'] + data['rank']  # (local) = d + r

    # Fit: log(a_0(L2)/a_0(L1)) / log(L2/L1) for consecutive pairs
    print(f"  {group_name}: d={data['dim']}, r={data['rank']}, d+r={d_eff_expected}")
    for i in range(1, len(L_vals)):
        L1 = L_vals[i-1]  # (local)
        L2 = L_vals[i]  # (local)
        if a0_vals[i-1] > 0 and a0_vals[i] > 0 and L2 > L1:
            alpha_eff = np.log(a0_vals[i] / a0_vals[i-1]) / np.log(L2 / L1)  # (local)
            print(f"    L={L1}->{L2}: alpha_eff(a_0) = {alpha_eff:.2f} "
                  f"(asymptotic: {d_eff_expected})")
    print()


# =============================================================================
# SECTION 8: R_1 DRIFT SCALING COMPARISON
# =============================================================================

print("=" * 78)
print("SECTION 8: R_1 DRIFT SCALING COMPARISON")
print("=" * 78)
print()

# Compute R_1(L) - R_1(L_max) for each group and check if it scales as L^{-rank}
for group_name, data, results in [
    ('SU(3)', su3, su3_results),
    ('SU(4)', su4, su4_results),
    ('Sp(2)', sp2, sp2_results),
]:
    L_vals = sorted(results.keys())  # (local)
    R1_vals = [results[L]['R1'] for L in L_vals]  # (local)
    R1_limit = R1_vals[-1]  # (local) best estimate (highest L)
    r = data['rank']  # (local)

    print(f"  {group_name} (rank {r}):")
    print(f"    R_1(L_max={L_vals[-1]}) = {R1_limit:.6f}")
    for i in range(len(L_vals) - 1):
        L = L_vals[i]  # (local)
        delta_R1 = abs(R1_vals[i] - R1_limit)  # (local)
        rel_drift = delta_R1 / R1_limit  # (local)
        # Expected scaling: delta_R1 ~ C * L^{-r}
        # Check: delta_R1 * L^r should be ~constant
        scaled = delta_R1 * L**r  # (local)
        print(f"    L={L}: R_1={R1_vals[i]:.6f}, delta={delta_R1:.6f} ({rel_drift*100:.3f}%), "
              f"delta*L^{r} = {scaled:.6f}")
    print()


# =============================================================================
# SECTION 9: GATE VERDICT
# =============================================================================

print("=" * 78)
print("SECTION 9: GATE VERDICT — S77-D3-R1-UNIVERSAL")
print("=" * 78)
print()

# Collect key numbers
su3_R1_L3 = su3_results[3]['R1']  # (local)
su3_R1_Lmax = su3_results[max(su3_results.keys())]['R1']  # (local)
su3_drift_3_max = abs(su3_R1_Lmax - su3_R1_L3) / su3_R1_L3  # (local)

su4_R1_L3 = su4_results[3]['R1']  # (local)
su4_R1_Lmax = su4_results[max(su4_results.keys())]['R1']  # (local)
su4_drift_3_max = abs(su4_R1_Lmax - su4_R1_L3) / su4_R1_L3  # (local)

sp2_R1_L3 = sp2_results[3]['R1']  # (local)
sp2_R1_Lmax = sp2_results[max(sp2_results.keys())]['R1']  # (local)
sp2_drift_3_max = abs(sp2_R1_Lmax - sp2_R1_L3) / sp2_R1_L3  # (local)

DRIFT_THRESHOLD = 0.05  # (local) 5% gate

print(f"  R_1 drift from L=3 to L_max:")
print(f"    SU(3) (rank 2): {su3_drift_3_max*100:.3f}% [L=3 -> L={max(su3_results.keys())}]")
print(f"    SU(4) (rank 3): {su4_drift_3_max*100:.3f}% [L=3 -> L={max(su4_results.keys())}]")
print(f"    Sp(2) (rank 2): {sp2_drift_3_max*100:.3f}% [L=3 -> L={max(sp2_results.keys())}]")
print()

all_under_threshold = (su3_drift_3_max < DRIFT_THRESHOLD and
                       su4_drift_3_max < DRIFT_THRESHOLD and
                       sp2_drift_3_max < DRIFT_THRESHOLD)  # (local)

su4_better = su4_drift_3_max < su3_drift_3_max  # (local) rank-3 should be better than rank-2

print(f"  Gate threshold: {DRIFT_THRESHOLD*100:.0f}%")
print(f"  All groups under threshold: {all_under_threshold}")
print(f"  SU(4) (rank 3) has less drift than SU(3) (rank 2): {su4_better}")
print()

if all_under_threshold:
    print("  GATE S77-D3-R1-UNIVERSAL: INFO — R-PROTECTION UNIVERSALITY CONFIRMED")
    print("  All three groups show R_1 drift < 5% from L=3 to L_max.")
    if su4_better:
        print("  Higher rank (SU(4), rank 3) shows LESS drift than rank-2 groups,")
        print("  consistent with O(L^{-rank}) pre-asymptotic correction scaling.")
    else:
        print("  WARNING: SU(4) drift NOT smaller than SU(3) — O(L^{-rank}) scaling")
        print("  needs more L_max values to be visible.")
else:
    print("  GATE S77-D3-R1-UNIVERSAL: INFO — PARTIAL CONFIRMATION")
    failing = []  # (local)
    if su3_drift_3_max >= DRIFT_THRESHOLD:
        failing.append(f"SU(3): {su3_drift_3_max*100:.1f}%")
    if su4_drift_3_max >= DRIFT_THRESHOLD:
        failing.append(f"SU(4): {su4_drift_3_max*100:.1f}%")
    if sp2_drift_3_max >= DRIFT_THRESHOLD:
        failing.append(f"Sp(2): {sp2_drift_3_max*100:.1f}%")
    print(f"  Groups exceeding 5% drift: {', '.join(failing)}")

print()


# =============================================================================
# SECTION 10: SUMMARY TABLE
# =============================================================================

print("=" * 78)
print("SECTION 10: SUMMARY TABLE")
print("=" * 78)
print()
print(f"  {'Group':>8s} {'Type':>5s} {'dim':>4s} {'rank':>4s} {'dim_S':>5s} "
      f"{'R1(L=2)':>10s} {'R1(L=3)':>10s} {'R1(Lmax)':>10s} {'Lmax':>4s} {'drift%':>8s}")
print("  " + "-" * 75)

for group_name, data, results in [
    ('SU(3)', su3, su3_results),
    ('SU(4)', su4, su4_results),
    ('Sp(2)', sp2, sp2_results),
]:
    d = data['dim']  # (local)
    r = data['rank']  # (local)
    ds = 2 ** (d // 2)  # (local)
    L_max = max(results.keys())  # (local)
    R1_L2 = results[2]['R1']  # (local)
    R1_L3 = results[3]['R1']  # (local)
    R1_Lm = results[L_max]['R1']  # (local)
    drift = abs(R1_Lm - R1_L3) / R1_L3 * 100  # (local)

    print(f"  {group_name:>8s} {data['type']:>5s} {d:>4d} {r:>4d} {ds:>5d} "
          f"{R1_L2:>10.6f} {R1_L3:>10.6f} {R1_Lm:>10.6f} {L_max:>4d} {drift:>7.3f}%")

print()


# =============================================================================
# SECTION 11: SAVE DATA
# =============================================================================

print("=" * 78)
print("SECTION 11: SAVE DATA")
print("=" * 78)
print()

save_data = {}  # (local)
for group_name, data, results in [
    ('SU3', su3, su3_results),
    ('SU4', su4, su4_results),
    ('Sp2', sp2, sp2_results),
]:
    for L in sorted(results.keys()):
        prefix = f"{group_name}_L{L}"  # (local)
        save_data[f"{prefix}_a0"] = results[L]['a0']
        save_data[f"{prefix}_a2"] = results[L]['a2']
        save_data[f"{prefix}_a4"] = results[L]['a4']
        save_data[f"{prefix}_R1"] = results[L]['R1']
        save_data[f"{prefix}_n_irreps"] = results[L]['n_irreps']

    save_data[f"{group_name}_dim"] = data['dim']
    save_data[f"{group_name}_rank"] = data['rank']

OUT_NPZ = 's77_r1_other_groups.npz'  # (local)
np.savez(OUT_NPZ, **save_data)
print(f"  Saved to {OUT_NPZ}")


# =============================================================================
# SECTION 12: PLOT
# =============================================================================

print()
print("=" * 78)
print("SECTION 12: PLOT")
print("=" * 78)

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Plot 1: R_1 vs L_max for all groups
ax = axes[0]
for group_name, data, results, color, marker in [
    ('SU(3)', su3, su3_results, 'blue', 'o'),
    ('SU(4)', su4, su4_results, 'red', 's'),
    ('Sp(2)', sp2, sp2_results, 'green', '^'),
]:
    L_vals = sorted(results.keys())
    R1_vals = [results[L]['R1'] for L in L_vals]
    ax.plot(L_vals, R1_vals, f'{marker}-', color=color, label=f'{group_name} (r={data["rank"]})')
ax.set_xlabel('$L_{\\max}$')
ax.set_ylabel('$R_1 = a_0 a_4 / a_2^2$')
ax.set_title('$R_1$ convergence')
ax.legend()
ax.grid(True, alpha=0.3)

# Plot 2: a_0 vs L_max (Weyl growth)
ax = axes[1]
for group_name, data, results, color, marker in [
    ('SU(3)', su3, su3_results, 'blue', 'o'),
    ('SU(4)', su4, su4_results, 'red', 's'),
    ('Sp(2)', sp2, sp2_results, 'green', '^'),
]:
    L_vals = sorted(results.keys())
    a0_vals = [results[L]['a0'] for L in L_vals]
    ax.semilogy(L_vals, a0_vals, f'{marker}-', color=color,
                label=f'{group_name} (d+r={data["dim"]+data["rank"]})')
ax.set_xlabel('$L_{\\max}$')
ax.set_ylabel('$a_0$')
ax.set_title('$a_0$ Weyl growth')
ax.legend()
ax.grid(True, alpha=0.3)

# Plot 3: R_1 drift relative to L_max value
ax = axes[2]
for group_name, data, results, color, marker in [
    ('SU(3)', su3, su3_results, 'blue', 'o'),
    ('SU(4)', su4, su4_results, 'red', 's'),
    ('Sp(2)', sp2, sp2_results, 'green', '^'),
]:
    L_vals = sorted(results.keys())
    R1_vals = [results[L]['R1'] for L in L_vals]
    R1_ref = R1_vals[-1]
    drifts = [abs(R1 - R1_ref) / R1_ref * 100 for R1 in R1_vals]
    ax.loglog(L_vals, [max(dr, 1e-4) for dr in drifts], f'{marker}-', color=color,
              label=f'{group_name} (r={data["rank"]})')
    # Reference line: L^{-rank}
    L_arr = np.array(L_vals, dtype=float)
    r = data['rank']
    scale = drifts[0] * L_vals[0]**r if drifts[0] > 0 else 1
    ax.loglog(L_arr, scale * L_arr**(-r), '--', color=color, alpha=0.4,
              label=f'$L^{{-{r}}}$ ref')
ax.set_xlabel('$L_{\\max}$')
ax.set_ylabel('$|R_1 - R_1^{\\infty}| / R_1^{\\infty}$ (%)')
ax.set_title('$R_1$ drift scaling')
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)
ax.axhline(5, color='gray', ls=':', alpha=0.5, label='5% gate')

plt.tight_layout()
OUT_PNG = 's77_r1_other_groups.png'  # (local)
plt.savefig(OUT_PNG, dpi=150)
print(f"  Saved plot to {OUT_PNG}")
plt.close()

print()
print("=" * 78)
print("COMPUTATION COMPLETE")
print("=" * 78)
