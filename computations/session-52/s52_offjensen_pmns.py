#!/usr/bin/env python3
"""
S52 OFFJENSEN-PMNS-52: Off-Jensen PMNS Overlap Computation
===========================================================

Computes D_K eigenvalues and eigenvectors at off-Jensen points in the
U(2)-invariant left-invariant metric family on SU(3). Extracts the 3x3
PMNS overlap matrix between eigenspaces at off-Jensen and Jensen reference.
Tests for nonzero mixing angles.

Physics:
  Jensen metric: g_s = L1*g0|u1 + L2*g0|su2 + L3*g0|C2
    with L1=e^{2s}, L2=e^{-2s}, L3=e^s (volume-preserving 1-param family)

  Off-Jensen: independent (L1, L2, L3), or further breaking U(2) by splitting
  C^2 into two 2D subspaces with different scales (L3a, L3b).

  On Jensen curve, eigenspace overlap U = I exactly (Schur's lemma, S36).
  Off-Jensen may break this and generate nontrivial PMNS mixing.

Gate: PMNS-OFFJENSEN-52
  PASS: sin^2(theta_12) in [0.25, 0.35] at any off-Jensen point
  FAIL: All mixing angles < 0.01 at all tested points

Author: Neutrino-Detection-Specialist (Session 52)
Date: 2026-03-20
"""

import numpy as np
from numpy.linalg import eigh, cholesky, inv, eigvalsh
import sys
import os
import time
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===


# Add computations to path
sys.path.insert(0, str(_x2_shared_dir()))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from canonical_constants import tau_fold, E_B1, E_B2_mean, E_B3_mean

# ============================================================================
# SECTION 1: SU(3) LIE ALGEBRA INFRASTRUCTURE (self-contained)
# ============================================================================

def gell_mann_matrices():
    """Standard Gell-Mann matrices lambda_1,...,lambda_8."""
    lam = []
    # lambda_1
    lam.append(np.array([[0,1,0],[1,0,0],[0,0,0]], dtype=complex))
    # lambda_2
    lam.append(np.array([[0,-1j,0],[1j,0,0],[0,0,0]], dtype=complex))
    # lambda_3
    lam.append(np.array([[1,0,0],[0,-1,0],[0,0,0]], dtype=complex))
    # lambda_4
    lam.append(np.array([[0,0,1],[0,0,0],[1,0,0]], dtype=complex))
    # lambda_5
    lam.append(np.array([[0,0,-1j],[0,0,0],[1j,0,0]], dtype=complex))
    # lambda_6
    lam.append(np.array([[0,0,0],[0,0,1],[0,1,0]], dtype=complex))
    # lambda_7
    lam.append(np.array([[0,0,0],[0,0,-1j],[0,1j,0]], dtype=complex))
    # lambda_8
    lam.append(np.array([[1,0,0],[0,1,0],[0,0,-2]], dtype=complex) / np.sqrt(3))
    return lam


def su3_generators():
    """Anti-Hermitian generators e_a = -i/2 * lambda_a. Tr(e_a e_b) = -1/2 delta_{ab}."""
    gm = gell_mann_matrices()
    return [-1j / 2.0 * lam for lam in gm]


def compute_structure_constants(gens):
    """f_{abc} from [e_a, e_b] = f_{abc} e_c. Uses trace formula."""
    n = len(gens)
    f = np.zeros((n, n, n), dtype=np.float64)
    for a in range(n):
        for b in range(a+1, n):
            comm = gens[a] @ gens[b] - gens[b] @ gens[a]
            for c in range(n):
                val = -2.0 * np.trace(comm @ gens[c])  # (local)
                f[a,b,c] = val.real
                f[b,a,c] = -val.real
    return f


# ============================================================================
# SECTION 2: METRIC CONSTRUCTION
# ============================================================================

# Decomposition indices: su(3) = u(1) + su(2) + C^2
U1_IDX = [7]
SU2_IDX = [0, 1, 2]
C2_IDX = [3, 4, 5, 6]


def u2_invariant_metric(B_ab, L1, L2, L3):
    """
    U(2)-invariant left-invariant metric on SU(3).
    g = L1*g0|u1 + L2*g0|su2 + L3*g0|C2
    g0 = |B_ab| (positive-definite base from Killing form)
    """
    g0 = np.abs(B_ab)
    g = np.zeros((8,8), dtype=np.float64)
    for a in U1_IDX:
        for b in U1_IDX:
            g[a,b] = g0[a,b] * L1
    for a in SU2_IDX:
        for b in SU2_IDX:
            g[a,b] = g0[a,b] * L2
    for a in C2_IDX:
        for b in C2_IDX:
            g[a,b] = g0[a,b] * L3
    return g


def general_metric(B_ab, scales):
    """
    General left-invariant metric on SU(3) with per-generator scales.
    scales: array of 8 positive floats, one per generator direction.
    g = diag(s_0, ..., s_7) * g0
    This breaks U(2) when the C^2 scales are not all equal.
    """
    g0 = np.abs(B_ab)
    g = np.zeros((8,8), dtype=np.float64)
    for a in range(8):
        g[a,a] = g0[a,a] * scales[a]
    return g


def jensen_metric(B_ab, s):
    """Jensen curve: L1=e^{2s}, L2=e^{-2s}, L3=e^s. Volume-preserving."""
    L1 = np.exp(2.0*s)
    L2 = np.exp(-2.0*s)
    L3 = np.exp(s)
    return u2_invariant_metric(B_ab, L1, L2, L3)


# ============================================================================
# SECTION 3: FRAME, CONNECTION, DIRAC OPERATOR
# ============================================================================

def orthonormal_frame(g_s):
    """E such that E g_s E^T = I. E = inv(cholesky(g_s))."""
    L = cholesky(g_s)
    return inv(L)


def frame_structure_constants(f_abc, E):
    """Structure constants in ON frame: ft^f_{ab} = E_{ac} E_{bd} f_{cde} (E^{-1})_{ef}"""
    E_inv = inv(E)
    return np.einsum('ac,bd,cde,ef->abf', E, E, f_abc, E_inv)


def connection_coefficients(ft):
    """Levi-Civita connection: 2*Gamma_{cab} = ft_{abc} - ft_{bca} + ft_{cab}"""
    n = ft.shape[0]
    Gamma = np.zeros((n,n,n), dtype=np.float64)
    for c in range(n):
        for a in range(n):
            for b in range(n):
                Gamma[c,a,b] = 0.5*(ft[a,b,c] - ft[b,c,a] + ft[c,a,b])
    return Gamma


def build_cliff8():
    """Cliff(R^8) generators: 8 Hermitian 16x16 matrices, {gamma_a, gamma_b} = 2*delta_{ab}*I."""
    s1 = np.array([[0,1],[1,0]], dtype=complex)
    s2 = np.array([[0,-1j],[1j,0]], dtype=complex)
    s3 = np.array([[1,0],[0,-1]], dtype=complex)
    I2 = np.eye(2, dtype=complex)
    def kron4(A,B,C,D):
        return np.kron(A, np.kron(B, np.kron(C, D)))
    return [
        kron4(s1,I2,I2,I2), kron4(s2,I2,I2,I2),
        kron4(s3,s1,I2,I2), kron4(s3,s2,I2,I2),
        kron4(s3,s3,s1,I2), kron4(s3,s3,s2,I2),
        kron4(s3,s3,s3,s1), kron4(s3,s3,s3,s2),
    ]


def spinor_connection_offset(Gamma, gammas):
    """Omega = (1/4) sum_{a,b,c} Gamma^b_{ac} gamma_a gamma_b gamma_c"""
    n = len(gammas)
    dim_spin = gammas[0].shape[0]
    Omega = np.zeros((dim_spin, dim_spin), dtype=complex)
    for a in range(n):
        for b in range(n):
            for c in range(n):
                coeff = Gamma[b,a,c]
                if abs(coeff) > 1e-15:
                    Omega += coeff * gammas[a] @ gammas[b] @ gammas[c]
    Omega *= 0.25
    return Omega


def dirac_operator_on_irrep(rho, E, gammas, Omega):
    """D_pi = sum_{a,b} E_{ab} rho[b] x gamma_a + I x Omega"""
    dim_rho = rho[0].shape[0]
    dim_spin = 16  # (local)
    dim_total = dim_rho * dim_spin
    D = np.zeros((dim_total, dim_total), dtype=complex)
    for a in range(8):
        for b in range(8):
            if abs(E[a,b]) > 1e-15:
                D += E[a,b] * np.kron(rho[b], gammas[a])
    D += np.kron(np.eye(dim_rho), Omega)
    return D


# ============================================================================
# SECTION 4: IRREP CONSTRUCTION
# ============================================================================

def irrep_fundamental(gens):
    """(1,0) representation, dim=3."""
    return [g.copy() for g in gens]

def irrep_antifundamental(gens):
    """(0,1) representation, dim=3."""
    return [-g.T for g in gens]

def irrep_adjoint(f_abc):
    """(1,1) representation, dim=8."""
    rho = []
    for a in range(8):
        M = f_abc[a,:,:].T
        rho.append(M.astype(complex))
    return rho

def irrep_symmetric2(gens):
    """(2,0) representation, dim=6. Sym^2(C^3)."""
    I3 = np.eye(3, dtype=complex)
    sym_vecs = []
    for i in range(3):
        v = np.zeros(9, dtype=complex)
        v[3*i+i] = 1.0
        sym_vecs.append(v)
    for i in range(3):
        for j in range(i+1, 3):
            v = np.zeros(9, dtype=complex)
            v[3*i+j] = 1.0/np.sqrt(2)
            v[3*j+i] = 1.0/np.sqrt(2)
            sym_vecs.append(v)
    P = np.column_stack(sym_vecs)
    rho = []
    for X in gens:
        rho_9 = np.kron(X, I3) + np.kron(I3, X)
        rho.append(P.conj().T @ rho_9 @ P)
    return rho

def irrep_symmetric3(gens):
    """(3,0) representation, dim=10. Sym^3(C^3)."""
    from itertools import permutations
    I3 = np.eye(3, dtype=complex)
    sorted_triples = []
    for i in range(3):
        for j in range(i,3):
            for k in range(j,3):
                sorted_triples.append((i,j,k))
    sym_vecs = []
    for trip in sorted_triples:
        v = np.zeros(27, dtype=complex)
        perms = set(permutations(trip))
        norm = np.sqrt(len(perms))
        for p in perms:
            idx = p[0]*9 + p[1]*3 + p[2]
            v[idx] = 1.0/norm
        sym_vecs.append(v)
    P = np.column_stack(sym_vecs)
    rho = []
    for X in gens:
        rho_27 = (np.kron(np.kron(X,I3),I3) + np.kron(np.kron(I3,X),I3) + np.kron(np.kron(I3,I3),X))
        rho.append(P.conj().T @ rho_27 @ P)
    return rho

def irrep_via_casimir_projection(rho_A, rho_B, target_dim, target_pq=None):
    """General irrep via tensor product + Casimir projection."""
    dim_A = rho_A[0].shape[0]
    dim_B = rho_B[0].shape[0]
    dim_prod = dim_A * dim_B
    rho_prod = []
    C2 = np.zeros((dim_prod, dim_prod), dtype=complex)
    for a in range(8):
        rho_a = np.kron(rho_A[a], np.eye(dim_B)) + np.kron(np.eye(dim_A), rho_B[a])
        rho_prod.append(rho_a)
        C2 += rho_a @ rho_a
    evals, evecs = np.linalg.eigh(C2)
    tol = 1e-8  # (local)
    groups = []
    for i, ev in enumerate(sorted(zip(evals, range(dim_prod)))):
        val, idx = ev
        if not groups or abs(val - groups[-1][0]) > tol:
            groups.append((val, [idx]))
        else:
            groups[-1][1].append(idx)
    target_eval = None
    for val, indices in groups:
        if len(indices) == target_dim:
            target_eval = val
            break
    if target_eval is None:
        group_info = [(val, len(indices)) for val, indices in groups]
        label = f"({target_pq[0]},{target_pq[1]})" if target_pq else f"dim={target_dim}"
        raise RuntimeError(f"Cannot find {target_dim}-dim eigenspace for {label}. Dims: {group_info}")
    mask = np.abs(evals - target_eval) < tol
    P = evecs[:, mask]
    if P.shape[1] != target_dim:
        raise RuntimeError(f"Projection gave dim={P.shape[1]}, expected {target_dim}")
    rho = []
    for a in range(8):
        rho.append(P.conj().T @ rho_prod[a] @ P)
    return rho


def get_irreps_for_spectrum(gens, f_abc, max_pq_sum=3):
    """
    Return list of (p, q, dim, rho) for all irreps with p+q <= max_pq_sum.

    For neutrino physics we need the lowest eigenvalues, which come from
    small irreps. max_pq_sum=3 covers (0,0), (1,0), (0,1), (1,1), (2,0), (0,2),
    (3,0), (0,3), (2,1), (1,2).
    """
    irreps = []
    for p in range(max_pq_sum + 1):
        for q in range(max_pq_sum + 1 - p):
            dim_pq = (p+1)*(q+1)*(p+q+2)//2
            try:
                if (p,q) == (0,0):
                    rho = [np.zeros((1,1), dtype=complex) for _ in range(8)]
                elif (p,q) == (1,0):
                    rho = irrep_fundamental(gens)
                elif (p,q) == (0,1):
                    rho = irrep_antifundamental(gens)
                elif (p,q) == (1,1):
                    rho = irrep_adjoint(f_abc)
                elif p >= 2 and q == 0:
                    rho = irrep_symmetric2(gens) if p == 2 else irrep_symmetric3(gens)
                elif p == 0 and q >= 2:
                    conj_gens = [-g.T for g in gens]
                    rho = irrep_symmetric2(conj_gens) if q == 2 else irrep_symmetric3(conj_gens)
                elif (p,q) == (2,1):
                    rho_3 = irrep_fundamental(gens)
                    rho_8 = irrep_adjoint(f_abc)
                    rho = irrep_via_casimir_projection(rho_3, rho_8, dim_pq, (p,q))
                elif (p,q) == (1,2):
                    conj_gens = [-g.T for g in gens]
                    conj_f = compute_structure_constants(conj_gens)
                    rho_3c = irrep_fundamental(conj_gens)
                    rho_8c = irrep_adjoint(conj_f)
                    rho = irrep_via_casimir_projection(rho_3c, rho_8c, dim_pq, (2,1))
                else:
                    print(f"  Skipping ({p},{q}): not implemented for max_pq_sum={max_pq_sum}")
                    continue
                irreps.append((p, q, dim_pq, rho))
            except Exception as e:
                print(f"  Warning: could not build ({p},{q}): {e}")
    return irreps


# ============================================================================
# SECTION 5: SPECTRUM AND EIGENSPACE COMPUTATION
# ============================================================================

def compute_spectrum(g_metric, gens, f_abc, gammas, irreps_data, return_evecs=False):
    """
    Compute D_K eigenvalues (and optionally eigenvectors) for a given metric.

    Returns:
        evals_all: sorted array of all eigenvalues (imaginary parts of i*D)
        evecs_dict: if return_evecs, dict mapping (p,q) -> (evals, evecs) for each irrep
    """
    E = orthonormal_frame(g_metric)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    Omega = spinor_connection_offset(Gamma, gammas)

    all_evals = []
    evecs_dict = {}

    for (p, q, dim_rho, rho) in irreps_data:
        D = dirac_operator_on_irrep(rho, E, gammas, Omega)

        # D is anti-Hermitian in math convention. Eigenvalues are purely imaginary.
        # We multiply by -1j to get a Hermitian matrix with real eigenvalues.
        iD = -1j * D

        # Check Hermiticity
        herm_err = np.max(np.abs(iD - iD.conj().T))
        if herm_err > 1e-10:
            print(f"  WARNING: ({p},{q}) Hermiticity error = {herm_err:.2e}")

        evals, evecs = np.linalg.eigh(iD)

        # Each eigenvalue has degeneracy dim_rho^2 from Weyl (already built in)
        # but in the Peter-Weyl decomposition, irrep (p,q) appears with
        # multiplicity dim_rho (right regular representation).
        # So each eigenvalue of D_(p,q) has total multiplicity dim_rho.
        for ev in evals:
            all_evals.extend([ev] * dim_rho)

        if return_evecs:
            evecs_dict[(p,q)] = (evals, evecs)

    all_evals = np.array(sorted(all_evals))
    return all_evals, evecs_dict


def identify_sectors(evals, tol=1e-8):
    """
    Identify B1, B2, B3 sectors from eigenvalue clustering.

    At the Jensen fold (tau~0.19):
      B1 (trivial, 1-fold): lowest positive eigenvalue ~0.819
      B2 (fundamental, 4-fold): next cluster ~0.845
      B3 (adjoint, 3-fold): next cluster ~0.971

    Returns:
        sectors: dict with keys 'B1', 'B2', 'B3', values are (mean_eval, indices_in_evals)
    """
    # Get unique positive eigenvalues
    pos_evals = evals[evals > tol]

    # Cluster by proximity
    clusters = []
    current_cluster = [pos_evals[0]]
    for ev in pos_evals[1:]:
        if abs(ev - current_cluster[-1]) < tol:
            current_cluster.append(ev)
        else:
            clusters.append(np.array(current_cluster))
            current_cluster = [ev]
    clusters.append(np.array(current_cluster))

    # The 3 lowest clusters are B1, B2, B3
    if len(clusters) < 3:
        print(f"  WARNING: only {len(clusters)} clusters found, expected >= 3")
        return None

    sectors = {}
    names = ['B1', 'B2', 'B3']
    for i, name in enumerate(names):
        sectors[name] = {
            'mean': np.mean(clusters[i]),
            'count': len(clusters[i]),
            'evals': clusters[i]
        }

    return sectors


def compute_singlet_overlap(evecs_ref, evecs_off, evals_ref, evals_off, tol=1e-6):
    """
    Compute the 3x3 overlap matrix between B1, B2, B3 eigenspaces
    at reference (Jensen) and off-Jensen points.

    For the singlet (0,0), the Dirac matrix is 16x16, giving 8 positive
    and 8 negative eigenvalues (paired by J symmetry).

    The positive eigenvalues cluster into:
      B1 (1 eigenvalue), B2 (4 eigenvalues), B3 (3 eigenvalues)

    The overlap matrix U_{ij} = sum_k |<psi_i^ref | psi_j^off>|^2
    where i runs over the B_i eigenspace at Jensen, j over B_j at off-Jensen.

    For PMNS extraction, we need the overlap between the 3 SECTORS (not individual
    modes). So we define:
      O_{IJ} = (1/n_I) * sum_{i in B_I^ref} sum_{j in B_J^off} |<psi_i | psi_j>|^2

    where n_I is the dimension of sector I.

    If U(2) is preserved, O = I (Schur's lemma). If broken, O develops off-diagonal
    elements that encode PMNS-like mixing.
    """
    # Sort positive eigenvalues and identify sectors
    pos_mask_ref = evals_ref > 1e-6
    pos_idx_ref = np.where(pos_mask_ref)[0]
    pos_evals_ref = evals_ref[pos_idx_ref]

    pos_mask_off = evals_off > 1e-6
    pos_idx_off = np.where(pos_mask_off)[0]
    pos_evals_off = evals_off[pos_idx_off]

    # Sort by eigenvalue
    sort_ref = np.argsort(pos_evals_ref)
    sort_off = np.argsort(pos_evals_off)

    sorted_idx_ref = pos_idx_ref[sort_ref]
    sorted_idx_off = pos_idx_off[sort_off]
    sorted_evals_ref = pos_evals_ref[sort_ref]
    sorted_evals_off = pos_evals_off[sort_off]

    # Identify sectors: B1 (1 mode), B2 (4 modes), B3 (3 modes)
    # Total = 8 positive eigenvalues for the singlet
    if len(sorted_idx_ref) != 8 or len(sorted_idx_off) != 8:
        print(f"  WARNING: Expected 8 positive eigenvalues, got ref={len(sorted_idx_ref)}, off={len(sorted_idx_off)}")
        return None, None, None

    # Cluster the eigenvalues
    def cluster_8(sorted_evals):
        """Identify B1, B2, B3 boundaries from 8 sorted eigenvalues."""
        # Try standard assignment: 1 + 4 + 3
        # Look at gaps between consecutive eigenvalues
        gaps = np.diff(sorted_evals)
        # The two largest gaps should separate B1|B2 and B2|B3
        gap_order = np.argsort(gaps)[::-1]

        # Check: the two biggest gaps
        g1, g2 = sorted(gap_order[:2])

        # Boundaries
        boundaries = sorted([g1+1, g2+1])

        # Check expected sizes
        sizes = [boundaries[0], boundaries[1]-boundaries[0], 8-boundaries[1]]

        return boundaries, sizes

    bounds_ref, sizes_ref = cluster_8(sorted_evals_ref)
    bounds_off, sizes_off = cluster_8(sorted_evals_off)

    # Sector index ranges
    def sector_ranges(bounds):
        return {
            'B1': list(range(0, bounds[0])),
            'B2': list(range(bounds[0], bounds[1])),
            'B3': list(range(bounds[1], 8))
        }

    sec_ref = sector_ranges(bounds_ref)
    sec_off = sector_ranges(bounds_off)

    # Build the full overlap matrix between all 8 positive eigenstates
    overlap_full = np.zeros((8, 8))
    for i in range(8):
        for j in range(8):
            v_ref = evecs_ref[:, sorted_idx_ref[i]]
            v_off = evecs_off[:, sorted_idx_off[j]]
            overlap_full[i, j] = np.abs(np.vdot(v_ref, v_off))**2

    # Build the 3x3 sector overlap matrix
    sector_names = ['B1', 'B2', 'B3']
    O = np.zeros((3, 3))
    for I, name_I in enumerate(sector_names):
        for J, name_J in enumerate(sector_names):
            total = 0.0  # (local)
            n_I = len(sec_ref[name_I])
            for i in sec_ref[name_I]:
                for j in sec_off[name_J]:
                    total += overlap_full[i, j]
            O[I, J] = total / n_I if n_I > 0 else 0.0

    return O, overlap_full, {
        'ref_evals': sorted_evals_ref,
        'off_evals': sorted_evals_off,
        'ref_sectors': sec_ref,
        'off_sectors': sec_off,
        'ref_sizes': sizes_ref,
        'off_sizes': sizes_off
    }


def extract_pmns_angles(O):
    """
    Extract PMNS mixing angles from the 3x3 overlap matrix O.

    Standard PMNS parameterization:
      |U_{e1}|^2 = cos^2(theta_12) * cos^2(theta_13)
      |U_{e2}|^2 = sin^2(theta_12) * cos^2(theta_13)
      |U_{e3}|^2 = sin^2(theta_13)
      |U_{mu3}|^2 = sin^2(theta_23) * cos^2(theta_13)

    But our overlap matrix O is |U|^2 in the sector basis, where sectors
    have different dimensions. The PMNS-relevant extraction depends on how
    we identify "mass eigenstates" with sectors.

    For a proper extraction: O_{IJ} plays the role of |U_{IJ}|^2.

    sin^2(theta_13) = O[0,2]  (B1-B3 mixing)
    sin^2(theta_12) = O[0,1] / (1 - O[0,2])  (B1-B2 mixing in 1-2 subspace)
    sin^2(theta_23) = O[1,2] / (1 - O[0,2])  (B2-B3 mixing in 2-3 subspace)
    """
    # Ensure O rows sum to ~1
    row_sums = np.sum(O, axis=1)

    sin2_13 = O[0, 2]
    cos2_13 = 1.0 - sin2_13

    if cos2_13 > 1e-10:
        sin2_12 = O[0, 1] / cos2_13
        sin2_23 = O[1, 2] / cos2_13
    else:
        sin2_12 = 0.0  # (local)
        sin2_23 = 0.0  # (local)

    # Clip to [0, 1] for safety
    sin2_12 = np.clip(sin2_12, 0.0, 1.0)
    sin2_13 = np.clip(sin2_13, 0.0, 1.0)
    sin2_23 = np.clip(sin2_23, 0.0, 1.0)

    return sin2_12, sin2_13, sin2_23, row_sums


# ============================================================================
# SECTION 6: OFF-JENSEN METRIC POINTS
# ============================================================================

def generate_offjensen_points(tau_ref):
    """
    Generate off-Jensen test points.

    The Jensen curve at tau is: L1=e^{2*tau}, L2=e^{-2*tau}, L3=e^{tau}

    Off-Jensen directions:
    1. U(2)-preserving: keep diagonal structure but break the Jensen constraint
       - Vary L3 while keeping L1, L2 at Jensen values
       - Vary L1 independently while keeping L2, L3 at Jensen
       - Scale L1 up and L2 down differently from Jensen

    2. U(2)-breaking: split C^2 into two 2D blocks with different scales
       - g_45 != g_67 breaks the SU(2) acting on C^2
       - This is the most promising direction for PMNS mixing

    Each point: dict with 'name', 'scales' (8-vector of per-generator factors),
    and 'description'.
    """
    s = tau_ref
    L1_J = np.exp(2*s)
    L2_J = np.exp(-2*s)
    L3_J = np.exp(s)

    points = []

    # --- U(2)-preserving off-Jensen ---

    # OJ-1: Increase L3 by 20% (C^2 directions expanded)
    eps = 0.20
    L3_new = L3_J * (1 + eps)
    scales = np.array([L2_J]*3 + [L3_new]*4 + [L1_J])
    points.append({
        'name': 'OJ-1: L3+20%',
        'scales': scales,
        'L1': L1_J, 'L2': L2_J, 'L3': L3_new,
        'type': 'U(2)-preserving',
        'description': f'C^2 scale L3 increased 20% from {L3_J:.4f} to {L3_new:.4f}'
    })

    # OJ-2: Decrease L3 by 20%
    L3_new = L3_J * (1 - eps)
    scales = np.array([L2_J]*3 + [L3_new]*4 + [L1_J])
    points.append({
        'name': 'OJ-2: L3-20%',
        'scales': scales,
        'L1': L1_J, 'L2': L2_J, 'L3': L3_new,
        'type': 'U(2)-preserving',
        'description': f'C^2 scale L3 decreased 20% from {L3_J:.4f} to {L3_new:.4f}'
    })

    # OJ-3: Increase L1 by 50% (u(1) direction expanded)
    L1_new = L1_J * 1.5
    scales = np.array([L2_J]*3 + [L3_J]*4 + [L1_new])
    points.append({
        'name': 'OJ-3: L1+50%',
        'scales': scales,
        'L1': L1_new, 'L2': L2_J, 'L3': L3_J,
        'type': 'U(2)-preserving',
        'description': f'u(1) scale L1 increased 50% from {L1_J:.4f} to {L1_new:.4f}'
    })

    # --- U(2)-breaking: split C^2 ---

    # OJ-4: Split C^2 into (4,5) and (6,7) blocks. L3a != L3b.
    # This breaks the SU(2)_R that acts on the doublet (4,5)<->(6,7)
    split = 0.10  # 10% split
    L3a = L3_J * (1 + split)
    L3b = L3_J * (1 - split)
    scales = np.array([L2_J]*3 + [L3a, L3a, L3b, L3b] + [L1_J])
    points.append({
        'name': 'OJ-4: C2 split 10%',
        'scales': scales,
        'L3a': L3a, 'L3b': L3b,
        'type': 'U(2)-breaking',
        'description': f'C^2 split: (4,5)={L3a:.4f}, (6,7)={L3b:.4f}'
    })

    # OJ-5: Larger C^2 split (30%)
    split = 0.30
    L3a = L3_J * (1 + split)
    L3b = L3_J * (1 - split)
    scales = np.array([L2_J]*3 + [L3a, L3a, L3b, L3b] + [L1_J])
    points.append({
        'name': 'OJ-5: C2 split 30%',
        'scales': scales,
        'L3a': L3a, 'L3b': L3b,
        'type': 'U(2)-breaking',
        'description': f'C^2 split: (4,5)={L3a:.4f}, (6,7)={L3b:.4f}'
    })

    # OJ-6: C^2 split with individual scales (all different)
    # This maximally breaks the C^2 symmetry
    L3_vals = [L3_J*1.15, L3_J*0.95, L3_J*1.05, L3_J*0.85]
    scales = np.array([L2_J]*3 + L3_vals + [L1_J])
    points.append({
        'name': 'OJ-6: C2 all-different',
        'scales': scales,
        'type': 'U(2)-breaking',
        'description': f'C^2 all different: {[f"{v:.4f}" for v in L3_vals]}'
    })

    # OJ-7: Break SU(2) sub-block too (all 8 scales different)
    # This breaks ALL symmetry
    L_su2 = [L2_J*1.1, L2_J*0.95, L2_J*1.05]
    scales = np.array(L_su2 + L3_vals + [L1_J*1.2])
    points.append({
        'name': 'OJ-7: All-8 different',
        'scales': scales,
        'type': 'Fully broken',
        'description': 'All 8 generator scales independent'
    })

    # OJ-8: Small perturbation of C^2 (epsilon = 0.01)
    eps_small = 0.01  # (local)
    L3a = L3_J * (1 + eps_small)
    L3b = L3_J * (1 - eps_small)
    scales = np.array([L2_J]*3 + [L3a, L3a, L3b, L3b] + [L1_J])
    points.append({
        'name': 'OJ-8: C2 split 1%',
        'scales': scales,
        'L3a': L3a, 'L3b': L3b,
        'type': 'U(2)-breaking',
        'description': f'C^2 split: (4,5)={L3a:.4f}, (6,7)={L3b:.4f}'
    })

    # OJ-9: At tau=0.15 (away from fold) with 30% C^2 split
    s2 = 0.15
    L1_2 = np.exp(2*s2)
    L2_2 = np.exp(-2*s2)
    L3_2 = np.exp(s2)
    split = 0.30
    L3a = L3_2 * (1 + split)
    L3b = L3_2 * (1 - split)
    scales = np.array([L2_2]*3 + [L3a, L3a, L3b, L3b] + [L1_2])
    points.append({
        'name': 'OJ-9: tau=0.15, C2 split 30%',
        'scales': scales,
        'L3a': L3a, 'L3b': L3b,
        'type': 'U(2)-breaking',
        'description': f'tau=0.15 base, C^2 split: (4,5)={L3a:.4f}, (6,7)={L3b:.4f}'
    })

    # OJ-10: Large asymmetric deformation
    # One C^2 pair at 2x, the other at 0.5x, with compensating L1
    L3a = L3_J * 2.0
    L3b = L3_J * 0.5
    scales = np.array([L2_J]*3 + [L3a, L3a, L3b, L3b] + [L1_J])
    points.append({
        'name': 'OJ-10: C2 extreme (2x/0.5x)',
        'scales': scales,
        'L3a': L3a, 'L3b': L3b,
        'type': 'U(2)-breaking',
        'description': f'C^2 extreme split: (4,5)={L3a:.4f}, (6,7)={L3b:.4f}'
    })

    return points


# ============================================================================
# SECTION 7: MAIN COMPUTATION
# ============================================================================

def main():
    t_start = time.time()
    print("=" * 72)
    print("S52 OFFJENSEN-PMNS-52: Off-Jensen PMNS Overlap")
    print("=" * 72)

    # --- Setup Lie algebra ---
    print("\n[1] Setting up SU(3) Lie algebra infrastructure...")
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    B_ab = np.einsum('acd,bcd->ab', f_abc, f_abc)
    gammas = build_cliff8()

    # Validate Clifford algebra
    cliff_err = 0.0  # (local)
    for a in range(8):
        for b in range(8):
            ac = gammas[a] @ gammas[b] + gammas[b] @ gammas[a]
            target = 2.0 * (1 if a == b else 0) * np.eye(16)
            cliff_err = max(cliff_err, np.max(np.abs(ac - target)))
    print(f"  Clifford algebra error: {cliff_err:.2e}")

    # Killing form
    print(f"  Killing form diagonal (should be -3): {B_ab[0,0]:.4f}")

    # --- Build irreps ---
    print("\n[2] Building irrep representations (max p+q = 3)...")
    irreps_data = get_irreps_for_spectrum(gens, f_abc, max_pq_sum=3)
    print(f"  Built {len(irreps_data)} irreps:")
    for p, q, dim, _ in irreps_data:
        print(f"    ({p},{q}): dim = {dim}")

    # --- Reference Jensen spectrum ---
    tau_ref = tau_fold  # 0.19
    print(f"\n[3] Computing reference Jensen spectrum at tau = {tau_ref}...")
    g_jensen = jensen_metric(B_ab, tau_ref)
    print(f"  Jensen metric diagonal: {np.diag(g_jensen)}")

    evals_ref_all, evecs_ref_dict = compute_spectrum(g_jensen, gens, f_abc, gammas, irreps_data, return_evecs=True)

    # Report singlet eigenvalues
    if (0,0) in evecs_ref_dict:
        e00_ref, v00_ref = evecs_ref_dict[(0,0)]
        pos_ref = e00_ref[e00_ref > 1e-6]
        print(f"  Singlet (0,0) positive eigenvalues: {sorted(pos_ref)}")

    # Also report (1,0) eigenvalues for R computation
    if (1,0) in evecs_ref_dict:
        e10_ref, v10_ref = evecs_ref_dict[(1,0)]
        pos_10_ref = sorted(e10_ref[e10_ref > 1e-6])
        print(f"  Fundamental (1,0) positive eigenvalues (first 12): {pos_10_ref[:12]}")

    # Identify reference sectors from (0,0) singlet
    ref_evals_singlet = evecs_ref_dict[(0,0)][0]
    ref_evecs_singlet = evecs_ref_dict[(0,0)][1]

    # Verify against known values
    pos_ref = sorted(ref_evals_singlet[ref_evals_singlet > 1e-6])
    print(f"\n  Reference singlet B1, B2, B3 eigenvalues:")
    print(f"    B1 (1 mode):  {pos_ref[0]:.6f}  (expected ~{E_B1:.4f})")
    print(f"    B2 (4 modes): {pos_ref[1]:.6f} - {pos_ref[4]:.6f}  (expected ~{E_B2_mean:.4f})")
    print(f"    B3 (3 modes): {pos_ref[5]:.6f} - {pos_ref[7]:.6f}  (expected ~{E_B3_mean:.4f})")

    R_ref = (pos_ref[5]**2 - pos_ref[1]**2) / (pos_ref[1]**2 - pos_ref[0]**2)
    print(f"    R = (E_B3^2 - E_B2^2)/(E_B2^2 - E_B1^2) = {R_ref:.2f}")

    # --- Off-Jensen scan ---
    print(f"\n[4] Generating off-Jensen test points...")
    oj_points = generate_offjensen_points(tau_ref)
    print(f"  Generated {len(oj_points)} off-Jensen points")

    # Storage for results
    results = []
    max_sin2_12 = 0.0
    max_sin2_13 = 0.0
    max_sin2_23 = 0.0

    print(f"\n[5] Computing off-Jensen spectra and overlaps...")
    print("-" * 72)

    for idx, pt in enumerate(oj_points):
        print(f"\n  Point {idx+1}/{len(oj_points)}: {pt['name']}")
        print(f"    Type: {pt['type']}")
        print(f"    {pt['description']}")

        # Construct the metric
        g_off = general_metric(B_ab, pt['scales'])

        # Verify positive definiteness
        g_evals = np.linalg.eigvalsh(g_off)
        if np.any(g_evals <= 0):
            print(f"    SKIP: metric not positive definite (min eigenvalue = {np.min(g_evals):.2e})")
            results.append({'name': pt['name'], 'type': pt['type'], 'skip': True})
            continue

        # Compute spectrum
        try:
            evals_off_all, evecs_off_dict = compute_spectrum(g_off, gens, f_abc, gammas, irreps_data, return_evecs=True)
        except Exception as e:
            print(f"    ERROR computing spectrum: {e}")
            results.append({'name': pt['name'], 'type': pt['type'], 'error': str(e)})
            continue

        # Singlet overlap
        if (0,0) in evecs_off_dict:
            off_evals_singlet = evecs_off_dict[(0,0)][0]
            off_evecs_singlet = evecs_off_dict[(0,0)][1]

            pos_off = sorted(off_evals_singlet[off_evals_singlet > 1e-6])
            print(f"    Singlet positive eigenvalues: {[f'{v:.6f}' for v in pos_off]}")

            # Compute R at this off-Jensen point
            if len(pos_off) >= 6:
                R_off = (pos_off[5]**2 - pos_off[1]**2) / (pos_off[1]**2 - pos_off[0]**2) if (pos_off[1]**2 - pos_off[0]**2) > 1e-12 else float('inf')
                print(f"    R = {R_off:.2f}")
            else:
                R_off = None

            # Compute overlap matrix
            O, overlap_full, info = compute_singlet_overlap(
                ref_evecs_singlet, off_evecs_singlet,
                ref_evals_singlet, off_evals_singlet
            )

            if O is not None:
                print(f"    Overlap matrix O (3x3 sector):")
                for i in range(3):
                    print(f"      [{O[i,0]:.6f}  {O[i,1]:.6f}  {O[i,2]:.6f}]")

                row_sums = np.sum(O, axis=1)
                print(f"    Row sums: {row_sums}")
                print(f"    Sector sizes (ref): {info['ref_sizes']}, (off): {info['off_sizes']}")

                # Extract mixing angles
                sin2_12, sin2_13, sin2_23, _ = extract_pmns_angles(O)
                print(f"    sin^2(theta_12) = {sin2_12:.6f}  (target: 0.303)")
                print(f"    sin^2(theta_13) = {sin2_13:.6f}  (target: 0.0222)")
                print(f"    sin^2(theta_23) = {sin2_23:.6f}  (target: 0.451)")

                max_sin2_12 = max(max_sin2_12, sin2_12)
                max_sin2_13 = max(max_sin2_13, sin2_13)
                max_sin2_23 = max(max_sin2_23, sin2_23)

                results.append({
                    'name': pt['name'],
                    'type': pt['type'],
                    'O': O,
                    'overlap_full': overlap_full,
                    'sin2_12': sin2_12,
                    'sin2_13': sin2_13,
                    'sin2_23': sin2_23,
                    'R': R_off,
                    'pos_evals': pos_off,
                    'info': info,
                    'scales': pt['scales'],
                })
            else:
                results.append({'name': pt['name'], 'type': pt['type'], 'error': 'overlap computation failed'})
        else:
            results.append({'name': pt['name'], 'type': pt['type'], 'error': 'no singlet data'})

    # Also compute overlaps from (1,0) fundamental sector
    print(f"\n[6] Computing (1,0) fundamental sector overlaps...")
    print("-" * 72)

    fund_results = []
    if (1,0) in evecs_ref_dict:
        e10_ref_all, v10_ref_all = evecs_ref_dict[(1,0)]

        for idx, pt in enumerate(oj_points):
            if idx >= len(results) or 'error' in results[idx] or results[idx].get('skip'):
                continue

            # Re-get the off-Jensen data
            g_off = general_metric(B_ab, pt['scales'])
            _, evecs_off_dict = compute_spectrum(g_off, gens, f_abc, gammas, irreps_data, return_evecs=True)

            if (1,0) in evecs_off_dict:
                e10_off, v10_off = evecs_off_dict[(1,0)]

                # For (1,0), dim=3, so D is 48x48 (3*16).
                # 24 positive eigenvalues grouped as:
                #   B1-like, B2-like, B3-like (with dim=3 multiplicity each -> more eigenvalues)
                pos_10_off = sorted(e10_off[e10_off > 1e-6])

                # Compute the FULL overlap between all positive eigenvectors
                n_pos_ref = np.sum(e10_ref_all > 1e-6)
                n_pos_off = np.sum(e10_off > 1e-6)

                # For a rough sector identification, cluster the positive eigenvalues
                print(f"\n  (1,0) at {pt['name']}:")
                print(f"    Positive eigenvalues ({n_pos_off}): first 8 = {[f'{v:.4f}' for v in pos_10_off[:8]]}")

                fund_results.append({
                    'name': pt['name'],
                    'n_pos': n_pos_off,
                    'first_evals': pos_10_off[:12] if len(pos_10_off) >= 12 else pos_10_off
                })

    # --- Gate evaluation ---
    print(f"\n{'=' * 72}")
    print(f"[7] GATE EVALUATION: PMNS-OFFJENSEN-52")
    print(f"{'=' * 72}")

    print(f"\n  Maximum mixing angles across all off-Jensen points:")
    print(f"    max sin^2(theta_12) = {max_sin2_12:.6f}")
    print(f"    max sin^2(theta_13) = {max_sin2_13:.6f}")
    print(f"    max sin^2(theta_23) = {max_sin2_23:.6f}")

    # Gate criteria
    pass_criterion = (0.25 <= max_sin2_12 <= 0.35)
    fail_criterion = (max_sin2_12 < 0.01 and max_sin2_13 < 0.01 and max_sin2_23 < 0.01)

    if pass_criterion:
        verdict = "PASS"
        detail = f"sin^2(theta_12) = {max_sin2_12:.6f} falls in [0.25, 0.35]"
    elif fail_criterion:
        verdict = "FAIL"
        detail = f"All mixing angles < 0.01 at all points tested"
    else:
        verdict = "INTERMEDIATE"
        detail = f"Nonzero mixing found (max sin2_12={max_sin2_12:.6f}) but outside [0.25, 0.35]"

    print(f"\n  Gate verdict: {verdict}")
    print(f"  Detail: {detail}")

    # --- Summary table ---
    print(f"\n{'=' * 72}")
    print(f"[8] SUMMARY TABLE")
    print(f"{'=' * 72}")
    print(f"{'Point':<28s} {'Type':<18s} {'sin2_12':>8s} {'sin2_13':>8s} {'sin2_23':>8s} {'R':>8s}")
    print("-" * 90)
    for r in results:
        if 'sin2_12' in r:
            R_str = f"{r['R']:.1f}" if r['R'] is not None else "N/A"
            print(f"{r['name']:<28s} {r['type']:<18s} {r['sin2_12']:>8.6f} {r['sin2_13']:>8.6f} {r['sin2_23']:>8.6f} {R_str:>8s}")
        elif r.get('skip'):
            print(f"{r['name']:<28s} {r['type']:<18s} {'SKIP':>8s}")
        else:
            print(f"{r['name']:<28s} {r['type']:<18s} {'ERROR':>8s}")

    # --- NuFit comparison ---
    print(f"\n{'=' * 72}")
    print(f"[9] COMPARISON TO NuFit-6.0 (NO)")
    print(f"{'=' * 72}")
    print(f"  Measured:  sin2_12 = 0.303 +/- 0.012")
    print(f"  Measured:  sin2_13 = 0.02225 +/- 0.00065")
    print(f"  Measured:  sin2_23 = 0.451 +/- 0.019")
    print(f"  Measured:  R = Delta_m32^2/Delta_m21^2 = 33.8")
    print(f"  Framework: max sin2_12 = {max_sin2_12:.6f}")
    print(f"  Framework: max sin2_13 = {max_sin2_13:.6f}")
    print(f"  Framework: max sin2_23 = {max_sin2_23:.6f}")

    # --- Save data ---
    print(f"\n[10] Saving results...")

    # Prepare arrays for .npz
    names_arr = np.array([r['name'] for r in results])
    types_arr = np.array([r['type'] for r in results])
    sin2_12_arr = np.array([r.get('sin2_12', np.nan) for r in results])
    sin2_13_arr = np.array([r.get('sin2_13', np.nan) for r in results])
    sin2_23_arr = np.array([r.get('sin2_23', np.nan) for r in results])
    R_arr = np.array([r.get('R', np.nan) if r.get('R') is not None else np.nan for r in results])

    # Collect overlap matrices
    O_matrices = []
    for r in results:
        if 'O' in r:
            O_matrices.append(r['O'])
        else:
            O_matrices.append(np.full((3,3), np.nan))
    O_matrices = np.array(O_matrices)

    np.savez("computations/session-52/s52_offjensen_pmns.npz",
        tau_ref=tau_ref,
        n_points=len(results),
        names=names_arr,
        types=types_arr,
        sin2_12=sin2_12_arr,
        sin2_13=sin2_13_arr,
        sin2_23=sin2_23_arr,
        R_values=R_arr,
        O_matrices=O_matrices,
        max_sin2_12=max_sin2_12,
        max_sin2_13=max_sin2_13,
        max_sin2_23=max_sin2_23,
        gate_verdict=verdict,
        gate_detail=detail,
        ref_pos_evals=np.array(pos_ref),
        jensen_metric_diag=np.diag(g_jensen),
    )
    print(f"  Saved to computations/session-52/s52_offjensen_pmns.npz")

    # --- Plot ---
    print(f"\n[11] Generating plot...")
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('OFFJENSEN-PMNS-52: Off-Jensen PMNS Overlap', fontsize=14, fontweight='bold')

    # Panel 1: Mixing angles vs point index
    ax = axes[0, 0]
    valid_idx = [i for i, r in enumerate(results) if 'sin2_12' in r]
    if valid_idx:
        x = range(len(valid_idx))
        ax.semilogy(x, [sin2_12_arr[i] for i in valid_idx], 'o-', label=r'$\sin^2\theta_{12}$', markersize=8)
        ax.semilogy(x, [sin2_13_arr[i] for i in valid_idx], 's-', label=r'$\sin^2\theta_{13}$', markersize=8)
        ax.semilogy(x, [sin2_23_arr[i] for i in valid_idx], '^-', label=r'$\sin^2\theta_{23}$', markersize=8)
        ax.axhline(0.303, color='blue', ls='--', alpha=0.5, label='NuFit $\\sin^2\\theta_{12}$')
        ax.axhline(0.0222, color='orange', ls='--', alpha=0.5, label='NuFit $\\sin^2\\theta_{13}$')
        ax.axhline(0.451, color='green', ls='--', alpha=0.5, label='NuFit $\\sin^2\\theta_{23}$')
        ax.axhline(0.01, color='red', ls=':', alpha=0.7, label='FAIL threshold')
        ax.set_xticks(x)
        ax.set_xticklabels([results[i]['name'].split(':')[0] for i in valid_idx], rotation=45, ha='right', fontsize=7)
        ax.set_ylabel('Mixing angle')
        ax.set_title('Mixing angles at off-Jensen points')
        ax.legend(fontsize=7, loc='upper left')
        ax.set_ylim(bottom=1e-16)

    # Panel 2: Overlap matrix heatmap for the most-mixed point
    ax = axes[0, 1]
    if valid_idx:
        best_idx = valid_idx[np.argmax([sin2_12_arr[i] for i in valid_idx])]
        if 'O' in results[best_idx]:
            O_best = results[best_idx]['O']
            im = ax.imshow(O_best, cmap='Blues', vmin=0, vmax=1)
            ax.set_xticks([0,1,2])
            ax.set_yticks([0,1,2])
            ax.set_xticklabels(['B1 (off)', 'B2 (off)', 'B3 (off)'])
            ax.set_yticklabels(['B1 (ref)', 'B2 (ref)', 'B3 (ref)'])
            for i in range(3):
                for j in range(3):
                    ax.text(j, i, f'{O_best[i,j]:.4f}', ha='center', va='center', fontsize=10,
                           color='white' if O_best[i,j] > 0.5 else 'black')
            ax.set_title(f'Best overlap matrix: {results[best_idx]["name"]}')
            plt.colorbar(im, ax=ax, shrink=0.8)

    # Panel 3: R values at off-Jensen points
    ax = axes[1, 0]
    if valid_idx:
        R_valid = [R_arr[i] for i in valid_idx if not np.isnan(R_arr[i])]
        x_valid = [k for k, i in enumerate(valid_idx) if not np.isnan(R_arr[i])]
        if R_valid:
            ax.bar(x_valid, R_valid, alpha=0.7, color='steelblue')
            ax.axhline(33.8, color='red', ls='--', label='Target R = 33.8')
            ax.set_ylabel('R = $\\Delta m^2_{32}/\\Delta m^2_{21}$')
            ax.set_title('Mass ratio R at off-Jensen points')
            ax.set_xticks(range(len(valid_idx)))
            ax.set_xticklabels([results[i]['name'].split(':')[0] for i in valid_idx], rotation=45, ha='right', fontsize=7)
            ax.legend()

    # Panel 4: Eigenvalue spectra comparison
    ax = axes[1, 1]
    if valid_idx and pos_ref:
        ax.plot(pos_ref, 'ko-', label='Jensen (reference)', markersize=8)
        # Plot a few off-Jensen spectra
        colors = ['blue', 'red', 'green', 'purple']
        for k, vi in enumerate(valid_idx[:4]):
            if 'pos_evals' in results[vi]:
                ax.plot(results[vi]['pos_evals'], 'o--', color=colors[k%4],
                       label=results[vi]['name'], markersize=5, alpha=0.7)
        ax.set_xlabel('Mode index')
        ax.set_ylabel('Eigenvalue (M_KK units)')
        ax.set_title('Singlet positive eigenvalue spectra')
        ax.legend(fontsize=7)

    plt.tight_layout()
    plt.savefig("computations/session-52/s52_offjensen_pmns.png", dpi=150, bbox_inches='tight')
    print(f"  Saved plot to computations/session-52/s52_offjensen_pmns.png")

    # --- Timing ---
    elapsed = time.time() - t_start
    print(f"\n  Total computation time: {elapsed:.1f} s")

    print(f"\n{'=' * 72}")
    print(f"COMPUTATION COMPLETE")
    print(f"Gate: PMNS-OFFJENSEN-52 = {verdict}")
    print(f"{'=' * 72}")

    return verdict, results


if __name__ == "__main__":
    main()
