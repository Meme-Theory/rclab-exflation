#!/usr/bin/env python3
"""
S50 LORENTZIAN-CMPP-50: 12D Lorentzian CMPP Classification
============================================================

Context (S49 CMPP-TRANSITION-49):
  The 8D Riemannian CMPP classification on (SU(3), g_Jensen) is locked at
  Type II for all tau in [0, 1.0]. Root cause: complexified null frames in
  Riemannian signature always produce residual bw+/-1 components.
  SP's priority: test whether LORENTZIAN 12D classification differs.

Physical spacetime:
  ds^2 = -dt^2 + dx_1^2 + dx_2^2 + dx_3^2 + g_{ab}(tau) dy^a dy^b
  Signature: (-,+^{11})

  Case (a) STATIC: tau = const -> block-diagonal Riemann
  Case (b) DYNAMIC: tau(t) = v_terminal * t -> extrinsic curvature cross terms

CMPP in Lorentzian:
  REAL null vectors exist. No complexification needed.
  This is the physically correct classification.

Gate: LORENTZIAN-CMPP-50
  PASS: CMPP type changes at or near tau = 0.537
  FAIL: CMPP type constant across all tau
  INFO: Type change at other tau, or Lorentzian differs from Riemannian

Author: schwarzschild-penrose-geometer (Session 50)
Date: 2026-03-20
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
    su3_generators, compute_structure_constants, compute_killing_form,
    jensen_metric, orthonormal_frame, frame_structure_constants,
    connection_coefficients, U1_IDX, SU2_IDX, C2_IDX,
)
from canonical_constants import tau_fold, G_DeWitt, PI, v_terminal

t_start = time.time()

DIM_INT = 8
DIM_EXT = 4
DIM_TOTAL = 12
N_PAIRS_12 = DIM_TOTAL * (DIM_TOTAL - 1) // 2  # 66

# 12D index mapping: 0=t, 1-3=spatial, 4-11=internal
SU2_12 = [4 + i for i in SU2_IDX]
C2_12 = [4 + i for i in C2_IDX]
U1_12 = [4 + i for i in U1_IDX]


# =============================================================================
# SECTION 1: 8D Internal Curvature
# =============================================================================

def compute_riemann_ON(ft, Gamma, n=DIM_INT):
    """Riemann tensor R[a,b,c,f] in ON frame. Vectorized where possible."""
    R = np.zeros((n, n, n, n))
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for f in range(n):
                    val = 0.0
                    for d in range(n):
                        val += Gamma[d, b, c] * Gamma[f, a, d]
                        val -= Gamma[d, a, c] * Gamma[f, b, d]
                        val -= ft[a, b, d] * Gamma[f, d, c]
                    R[a, b, c, f] = val
    return R


def compute_8d_geometry(tau, gens, f_abc, B_ab):
    """Full 8D geometry at given tau."""
    g_s = jensen_metric(B_ab, tau)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    R_abcd = compute_riemann_ON(ft, Gamma)
    Ric = np.einsum('abca->bc', R_abcd)
    Ric = 0.5 * (Ric + Ric.T)
    R_scalar = float(np.trace(Ric))
    Ric_sq = float(np.sum(Ric**2))
    K_full = float(np.sum(R_abcd**2))
    return {'R_abcd': R_abcd, 'Ric': Ric, 'R_scalar': R_scalar,
            'Ric_sq': Ric_sq, 'K': K_full, 'g_s': g_s}


# =============================================================================
# SECTION 2: 12D Riemann and Weyl (VECTORIZED)
# =============================================================================

def build_12d_riemann_static(R8):
    """Static product M^{3,1} x K^8. Only internal block nonzero."""
    R12 = np.zeros((DIM_TOTAL, DIM_TOTAL, DIM_TOTAL, DIM_TOTAL))
    R12[4:12, 4:12, 4:12, 4:12] = R8
    return R12


def build_12d_riemann_dynamic(R8, tau_dot):
    """Dynamic case with extrinsic curvature."""
    R12 = np.zeros((DIM_TOTAL, DIM_TOTAL, DIM_TOTAL, DIM_TOTAL))

    lam = np.zeros(DIM_INT)
    lam[SU2_IDX] = -2.0
    lam[C2_IDX] = +1.0
    lam[U1_IDX] = +2.0
    K_diag = -(tau_dot / 2.0) * lam

    # Internal block: Gauss equation (vectorized for diagonal K)
    # K_{ac}K_{bd} - K_{ad}K_{bc}: nonzero only when both pairs are diagonal
    # K_{ac}K_{bd} = K_a * K_b * delta_{ac} * delta_{bd}
    # So the correction is K_a*K_b*(delta_{ac}*delta_{bd} - delta_{ad}*delta_{bc})
    R12[4:12, 4:12, 4:12, 4:12] = R8.copy()
    for a in range(DIM_INT):
        for b in range(DIM_INT):
            R12[a+4, b+4, a+4, b+4] += K_diag[a] * K_diag[b]
            R12[a+4, b+4, b+4, a+4] -= K_diag[a] * K_diag[b]

    # Time-internal: R_{0,a,0,a} = K_a^2 (Ricci equation, tau_ddot~0)
    for a in range(DIM_INT):
        val = K_diag[a]**2
        R12[0, a+4, 0, a+4] = val
        R12[a+4, 0, a+4, 0] = val
        R12[0, a+4, a+4, 0] = -val
        R12[a+4, 0, 0, a+4] = -val

    return R12, K_diag


def compute_12d_weyl(R12):
    """12D Weyl tensor. VECTORIZED — no Python quadruple loop."""
    n = DIM_TOTAL
    eta = np.diag(np.array([-1.0] + [1.0] * (n - 1)))

    # Ricci: R_{AC} = eta^{BB} R_{ABCB}
    eta_diag = np.diag(eta)  # shape (12,)
    # R_{ABCB} summed over B with eta^{BB} weight
    Ric12 = np.einsum('B,ABCB->AC', eta_diag, R12)
    Ric12 = 0.5 * (Ric12 + Ric12.T)

    R_scalar = float(np.einsum('A,AA->', eta_diag, Ric12))

    # Weyl tensor (vectorized):
    # C_{ABCD} = R_{ABCD}
    #   - (1/(n-2)) [eta_{AC} Ric_{BD} - eta_{AD} Ric_{BC} - eta_{BC} Ric_{AD} + eta_{BD} Ric_{AC}]
    #   + (R/((n-1)(n-2))) [eta_{AC} eta_{BD} - eta_{AD} eta_{BC}]

    # Build the Schouten subtraction terms using outer products
    # Term: eta_{AC} Ric_{BD} -> eta[:, None, :, None] * Ric[None, :, None, :]
    # Use broadcasting: build (n,n,n,n) tensors from (n,n) pieces
    eR1 = np.einsum('AC,BD->ABCD', eta, Ric12)  # eta_{AC} Ric_{BD}
    eR2 = np.einsum('AD,BC->ABCD', eta, Ric12)  # eta_{AD} Ric_{BC}
    eR3 = np.einsum('BC,AD->ABCD', eta, Ric12)  # eta_{BC} Ric_{AD}
    eR4 = np.einsum('BD,AC->ABCD', eta, Ric12)  # eta_{BD} Ric_{AC}

    ricci_term = (1.0 / (n - 2)) * (eR1 - eR2 - eR3 + eR4)

    ee1 = np.einsum('AC,BD->ABCD', eta, eta)
    ee2 = np.einsum('AD,BC->ABCD', eta, eta)
    scalar_term = (R_scalar / ((n - 1) * (n - 2))) * (ee1 - ee2)

    C12 = R12 - ricci_term + scalar_term

    # Trace check: C^B_{ABC} = 0
    trace_check = float(np.max(np.abs(np.einsum('B,ABCB->AC', eta_diag, C12))))

    # Weyl norm: C_{ABCD} C^{ABCD} with metric raising
    sign_tensor = np.einsum('A,B,C,D->ABCD', eta_diag, eta_diag, eta_diag, eta_diag)
    C_sq = float(np.sum(sign_tensor * C12 * C12))

    return C12, Ric12, R_scalar, C_sq, trace_check


# =============================================================================
# SECTION 3: Lorentzian Null Frame Construction and BW Decomposition
# =============================================================================

def construct_null_frame(n_spatial):
    """
    Build real null frame from a unit spatial direction n_spatial (11D unit vector).

    l = (e_0 + n) / sqrt(2),  k = (e_0 - n) / sqrt(2)
    l.k = -1, l.l = k.k = 0

    Transverse: 10 spacelike ON vectors orthogonal to n (and thus to l,k).

    n_spatial: 12D vector with n_spatial[0] = 0, |n_spatial[1:]| = 1
    """
    n = DIM_TOTAL
    e0 = np.zeros(n); e0[0] = 1.0
    l_vec = (e0 + n_spatial) / np.sqrt(2)
    k_vec = (e0 - n_spatial) / np.sqrt(2)

    # Transverse space: orthogonal complement of n_spatial in the spacelike sector
    # Start with standard basis e_1, ..., e_{11}, remove component along n_spatial
    n_spat = n_spatial[1:]  # 11D spatial part

    # Gram-Schmidt in the 11D spatial subspace orthogonal to n_spat
    basis_spatial = np.eye(11)
    ortho = []
    for v in basis_spatial:
        w = v - np.dot(v, n_spat) * n_spat
        for u in ortho:
            w -= np.dot(w, u) * u
        norm = np.linalg.norm(w)
        if norm > 1e-12:
            ortho.append(w / norm)
        if len(ortho) == 10:
            break

    # Embed back into 12D: m_i has zero time component
    m_vecs = []
    for v in ortho:
        m = np.zeros(n)
        m[1:] = v
        m_vecs.append(m)

    return l_vec, k_vec, m_vecs


def cmpp_decomposition(C12, l_vec, k_vec, m_vecs):
    """
    Boost-weight decomposition of 12D Weyl tensor in Lorentzian null frame.

    All quantities are REAL (no complexification).

    bw+2: C(l, m_i, l, m_j) = l^A m_i^B l^C m_j^D C_{ABCD}
    bw+1: C(l, k, l, m_i) and C(l, m_j, m_k, m_i)
    bw 0: C(l, m_i, k, m_j) and C(m_i, m_j, m_k, m_l) and C(l, k, l, k)
    bw-1: C(k, l, k, m_i) and C(k, m_j, m_k, m_i)
    bw-2: C(k, m_i, k, m_j)
    """
    n = DIM_TOTAL
    n_t = len(m_vecs)  # 10

    # Build frame matrix F[frame_idx, spacetime_idx]
    F = np.zeros((n, n))
    F[0] = l_vec
    F[1] = k_vec
    for i in range(n_t):
        F[i + 2] = m_vecs[i]

    # Transform Weyl to null frame: C'_{abcd} = F_a^A F_b^B F_c^C F_d^D C_{ABCD}
    # Use two-step einsum for efficiency
    C_step1 = np.einsum('aA,ABCD->aBCD', F, C12)
    C_step2 = np.einsum('bB,aBCD->abCD', F, C_step1)
    C_step3 = np.einsum('cC,abCD->abcD', F, C_step2)
    C_null = np.einsum('dD,abcD->abcd', F, C_step3)

    # Boost weight of each frame index
    def bw(idx):
        if idx == 0: return +1
        if idx == 1: return -1
        return 0

    # Accumulate ||C||^2 by boost weight
    bw_norms = {bw_val: 0.0 for bw_val in range(-4, 5)}
    for a in range(n):
        bwa = bw(a)
        for b in range(n):
            bwab = bwa + bw(b)
            for c in range(n):
                bwabc = bwab + bw(c)
                for d in range(n):
                    bw_total = bwabc + bw(d)
                    bw_norms[bw_total] = bw_norms.get(bw_total, 0.0) + C_null[a, b, c, d]**2

    bw_phys = {w: bw_norms.get(w, 0.0) for w in [-2, -1, 0, +1, +2]}
    total = sum(bw_phys.values())

    # Extract bw+2 matrix: Phi_{ij} = C(l, m_i, l, m_j) = C_null[0, i+2, 0, j+2]
    Phi_p2 = np.array([[C_null[0, i+2, 0, j+2] for j in range(n_t)] for i in range(n_t)])

    return {
        'bw_norms': bw_phys, 'bw_all': bw_norms, 'total': total,
        'Phi_p2': Phi_p2, 'C_null': C_null,
    }


def classify_cmpp(decomp, tol=1e-10):
    """Classify CMPP type from Lorentzian BW decomposition."""
    total = decomp['total']
    if total < tol:
        return 'O', {}

    rel_tol = tol * total
    n2 = decomp['bw_norms'][+2]
    n1 = decomp['bw_norms'][+1]
    n0 = decomp['bw_norms'][0]
    nm1 = decomp['bw_norms'][-1]
    nm2 = decomp['bw_norms'][-2]

    details = {f'frac_bw{w:+d}': decomp['bw_norms'][w]/total
               for w in [+2,+1,0,-1,-2]}

    h2p = n2 > rel_tol
    h1p = n1 > rel_tol
    h1m = nm1 > rel_tol
    h2m = nm2 > rel_tol

    if not h2p and not h1p and not h2m and not h1m:
        return ('D' if n0 > rel_tol else 'O'), details
    elif not h2p and not h1p:
        if not h2m and not h1m:
            return 'D', details
        elif not h2m:
            return 'III', details
        return 'II', details
    elif not h2p:
        return 'I', details
    elif n2/total < 0.001:
        details['note'] = f'bw+2={n2/total*100:.4f}%'
        return 'I', details
    return 'G', details


# =============================================================================
# SECTION 4: WAND Search (Optimized)
# =============================================================================

def make_spatial_dir(alpha, n_ext_3, n_int_8):
    """Build 12D unit spatial vector from mixing angle and sector directions."""
    n12 = np.zeros(DIM_TOTAL)
    n12[1:4] = np.sin(alpha) * n_ext_3
    n12[4:12] = np.cos(alpha) * n_int_8
    norm = np.linalg.norm(n12)
    if norm < 1e-15:
        n12[1] = 1.0
        norm = 1.0
    return n12 / norm


def scan_wand(C12, n_alpha=15, verbose=False):
    """
    Scan null directions to find the WAND (most algebraically special).
    Uses physically motivated internal directions and a coarse-to-fine strategy.
    """
    type_rank = {'O': 0, 'N': 1, 'III': 2, 'D': 3, 'II': 4, 'I': 5, 'G': 6}
    best_type = 'G'
    best_decomp = None
    best_params = None
    all_types = []
    n_tested = 0

    # Fixed external direction (result independent for flat M^4)
    n_ext = np.array([0.0, 0.0, 1.0])

    # Internal directions to test
    int_dirs = {}
    for i in range(DIM_INT):
        d = np.zeros(DIM_INT); d[i] = 1.0
        int_dirs[f'e{i}'] = d
    # SU(2) diagonal
    d = np.zeros(DIM_INT); d[SU2_IDX] = 1.0/np.sqrt(3)
    int_dirs['su2_diag'] = d
    # C2 diagonal
    d = np.zeros(DIM_INT); d[C2_IDX] = 0.5
    int_dirs['c2_diag'] = d
    # Mixed directions
    for i in SU2_IDX:
        for j in C2_IDX:
            d = np.zeros(DIM_INT); d[i] = 1.0/np.sqrt(2); d[j] = 1.0/np.sqrt(2)
            int_dirs[f'mix_{i}_{j}'] = d
    for i in SU2_IDX:
        d = np.zeros(DIM_INT); d[i] = 1.0/np.sqrt(2); d[U1_IDX[0]] = 1.0/np.sqrt(2)
        int_dirs[f'su2u1_{i}'] = d
    for j in C2_IDX:
        d = np.zeros(DIM_INT); d[j] = 1.0/np.sqrt(2); d[U1_IDX[0]] = 1.0/np.sqrt(2)
        int_dirs[f'c2u1_{j}'] = d
    # All-sector
    d = np.zeros(DIM_INT); d[0]=1; d[3]=1; d[7]=1; d /= np.linalg.norm(d)
    int_dirs['all_diag'] = d

    alpha_vals = np.linspace(0, np.pi/2, n_alpha)

    # Track minimum bw+2 fraction for refinement
    min_bw2_frac = 1.0
    min_bw2_params = None

    for label, n_int in int_dirs.items():
        for alpha in alpha_vals:
            n_spat = make_spatial_dir(alpha, n_ext, n_int)
            try:
                l, k, mvecs = construct_null_frame(n_spat)
                decomp = cmpp_decomposition(C12, l, k, mvecs)
                ctype, details = classify_cmpp(decomp)
                decomp['type'] = ctype
                decomp['details'] = details
                all_types.append(ctype)
                n_tested += 1

                if type_rank.get(ctype, 6) < type_rank.get(best_type, 6):
                    best_type = ctype
                    best_decomp = decomp
                    best_params = {'alpha': alpha, 'label': label, 'n_int': n_int.copy()}

                # Track bw+2 minimum
                bw2_frac = decomp['bw_norms'][+2] / decomp['total'] if decomp['total'] > 0 else 1.0
                if bw2_frac < min_bw2_frac:
                    min_bw2_frac = bw2_frac
                    min_bw2_params = {'alpha': alpha, 'n_int': n_int.copy(), 'label': label}

            except Exception:
                pass

    # Refinement around the best bw+2 minimum (gradient-free golden section)
    if min_bw2_params is not None and min_bw2_frac > 1e-14:
        best_n_int = min_bw2_params['n_int']
        best_alpha = min_bw2_params['alpha']

        def objective(alpha_val, n_int_val):
            nn = np.linalg.norm(n_int_val)
            if nn < 1e-15: return 1.0
            n_spat = make_spatial_dir(alpha_val, n_ext, n_int_val / nn)
            try:
                l, k, mvecs = construct_null_frame(n_spat)
                decomp = cmpp_decomposition(C12, l, k, mvecs)
                return decomp['bw_norms'][+2] / decomp['total'] if decomp['total'] > 0 else 1.0
            except Exception:
                return 1.0

        # Refine alpha
        for da in np.linspace(-0.15, 0.15, 15):
            a_try = np.clip(best_alpha + da, 0, np.pi/2)
            f = objective(a_try, best_n_int)
            n_tested += 1
            if f < min_bw2_frac:
                min_bw2_frac = f
                best_alpha = a_try

        # Refine internal direction
        for axis in range(DIM_INT):
            for da in np.linspace(-0.2, 0.2, 8):
                n_try = best_n_int.copy()
                n_try[axis] += da
                nn = np.linalg.norm(n_try)
                if nn > 1e-12:
                    f = objective(best_alpha, n_try / nn)
                    n_tested += 1
                    if f < min_bw2_frac:
                        min_bw2_frac = f
                        best_n_int = n_try / nn

        # Final classification at refined minimum
        n_spat = make_spatial_dir(best_alpha, n_ext, best_n_int)
        try:
            l, k, mvecs = construct_null_frame(n_spat)
            decomp = cmpp_decomposition(C12, l, k, mvecs)
            ctype, details = classify_cmpp(decomp)
            decomp['type'] = ctype
            decomp['details'] = details
            if type_rank.get(ctype, 6) < type_rank.get(best_type, 6):
                best_type = ctype
                best_decomp = decomp
                best_params = {'alpha': best_alpha, 'label': min_bw2_params['label'],
                               'n_int': best_n_int, 'bw2_frac_refined': min_bw2_frac}
        except Exception:
            pass

    return best_type, best_decomp, best_params, n_tested, all_types, min_bw2_frac


# =============================================================================
# SECTION 5: Weyl operator on Lambda^2(R^{11,1})
# =============================================================================

def weyl_operator_12d(C12):
    """12D Weyl as operator on 2-forms (66x66 matrix)."""
    n = DIM_TOTAL
    pairs = [(a, b) for a in range(n) for b in range(a+1, n)]
    N = len(pairs)
    C_mat = np.zeros((N, N))
    for I, (a1, b1) in enumerate(pairs):
        for J, (a2, b2) in enumerate(pairs):
            C_mat[I, J] = C12[a1, b1, a2, b2]

    eigvals = np.linalg.eigvals(C_mat)
    eigvals_real = np.sort(np.real(eigvals))
    imag_max = float(np.max(np.abs(np.imag(eigvals))))

    tol = 1e-8 * (np.max(np.abs(eigvals_real)) + 1e-15)
    unique = []
    for e in eigvals_real:
        if not unique or abs(e - unique[-1]) > tol:
            unique.append(e)
    mults = [int(np.sum(np.abs(eigvals_real - u) < tol)) for u in unique]

    return {
        'eigvals': eigvals_real, 'n_distinct': len(unique),
        'unique_eigs': unique, 'multiplicities': mults,
        'trace': float(np.trace(C_mat)), 'sym_err': float(np.max(np.abs(C_mat - C_mat.T))),
        'imag_max': imag_max,
    }


# =============================================================================
# SECTION 6: MAIN COMPUTATION
# =============================================================================

print("=" * 80)
print("  S50 LORENTZIAN-CMPP-50: 12D Lorentzian CMPP Classification")
print("=" * 80)

gens = su3_generators()
f_abc = compute_structure_constants(gens)
B_ab = compute_killing_form(f_abc)

tau_values = np.array([0.00, 0.19, 0.537, 0.895, 1.00])

# -----------------------------------------------------------
# CASE (a): STATIC
# -----------------------------------------------------------
print(f"\n{'='*80}")
print(f"  CASE (a): STATIC PRODUCT  M^{{3,1}} x (SU(3), g_tau)")
print(f"{'='*80}")
print(f"\n  12D Riemann block-diagonal. 12D Weyl = internal Weyl + Schouten(n=12).\n")

results_static = {}

print(f"{'tau':>8s}  {'CMPP':>6s}  {'bw+2%':>9s}  {'bw+1%':>9s}  {'bw0%':>9s}  "
      f"{'bw-1%':>9s}  {'bw-2%':>9s}  {'|C|^2':>12s}  {'n_dir':>6s}  {'time':>6s}")
print("-" * 98)

for tau in tau_values:
    t0 = time.time()

    geom8 = compute_8d_geometry(tau, gens, f_abc, B_ab)
    R12 = build_12d_riemann_static(geom8['R_abcd'])
    C12, Ric12, R12_scal, C12_sq, tr_err = compute_12d_weyl(R12)
    cmpp_type, best_decomp, best_params, n_tested, all_types, min_bw2 = scan_wand(C12)
    weyl_op = weyl_operator_12d(C12)

    dt = time.time() - t0

    results_static[tau] = {
        'geom8': geom8, 'R12_scalar': R12_scal, 'C12_sq': C12_sq,
        'trace_err': tr_err, 'cmpp_type': cmpp_type,
        'best_decomp': best_decomp, 'best_params': best_params,
        'n_tested': n_tested, 'weyl_op': weyl_op,
        'all_types': all_types, 'min_bw2_frac': min_bw2, 'time': dt,
    }

    if best_decomp is not None:
        bw = best_decomp['bw_norms']
        tot = best_decomp['total']
        fracs = {k: v/tot*100 for k,v in bw.items()} if tot > 0 else {k:0 for k in bw}
        print(f"{tau:8.4f}  {cmpp_type:>6s}  {fracs[+2]:9.4f}  {fracs[+1]:9.4f}  "
              f"{fracs[0]:9.4f}  {fracs[-1]:9.4f}  {fracs[-2]:9.4f}  "
              f"{C12_sq:12.6f}  {n_tested:6d}  {dt:5.1f}s")


# -----------------------------------------------------------
# DETAILED ANALYSIS (static)
# -----------------------------------------------------------
print(f"\n\n{'='*80}")
print(f"  DETAILED STATIC ANALYSIS")
print(f"{'='*80}")

for tau in tau_values:
    r = results_static[tau]
    wo = r['weyl_op']
    print(f"\n--- tau = {tau:.4f} ---")
    print(f"  12D CMPP: {r['cmpp_type']},  min bw+2 frac = {r['min_bw2_frac']:.6e}")
    print(f"  12D |C|^2 = {r['C12_sq']:.10f},  R_{12} = {r['R12_scalar']:.10f}")
    print(f"  Weyl trace-free check: {r['trace_err']:.2e}")
    print(f"  8D K = {r['geom8']['K']:.10f},  8D |Ric|^2 = {r['geom8']['Ric_sq']:.10f}")
    print(f"  Weyl operator: {wo['n_distinct']} distinct eigs (of 66), "
          f"trace={wo['trace']:.2e}, sym={wo['sym_err']:.2e}, imag={wo['imag_max']:.2e}")
    print(f"  Eigenvalue-multiplicity pairs (top 10):")
    for ue, m in list(zip(wo['unique_eigs'], wo['multiplicities']))[:10]:
        print(f"    lambda = {ue:+.8f}, mult = {m}")
    if len(wo['unique_eigs']) > 10:
        print(f"    ... ({len(wo['unique_eigs'])} total)")

    if r['best_params'] is not None:
        bp = r['best_params']
        print(f"  Best null direction: alpha = {bp['alpha']:.4f} ({np.degrees(bp['alpha']):.1f} deg)")
        print(f"    Internal label: {bp['label']}")
        if 'n_int' in bp:
            ni = bp['n_int']
            su2c = np.linalg.norm(ni[SU2_IDX])
            c2c = np.linalg.norm(ni[C2_IDX])
            u1c = np.linalg.norm(ni[U1_IDX])
            print(f"    |n|_SU2={su2c:.4f}, |n|_C2={c2c:.4f}, |n|_U1={u1c:.4f}")

    if r['best_decomp'] is not None:
        bw = r['best_decomp']['bw_norms']
        tot = r['best_decomp']['total']
        print(f"  BW decomposition (best WAND):")
        for w in [+2, +1, 0, -1, -2]:
            frac = bw[w]/tot*100 if tot > 0 else 0
            print(f"    bw={w:+d}: {bw[w]:.6e} ({frac:.4f}%)")

    # Type distribution
    tc = {}
    for t in r['all_types']:
        tc[t] = tc.get(t, 0) + 1
    print(f"  Type distribution ({r['n_tested']} directions):")
    for t, c in sorted(tc.items()):
        print(f"    {t}: {c} ({c/r['n_tested']*100:.1f}%)")


# -----------------------------------------------------------
# CASE (b): DYNAMIC
# -----------------------------------------------------------
print(f"\n\n{'='*80}")
print(f"  CASE (b): DYNAMIC  tau_dot = {v_terminal:.4f}")
print(f"{'='*80}")

results_dynamic = {}

print(f"\n{'tau':>8s}  {'CMPP':>6s}  {'bw+2%':>9s}  {'bw+1%':>9s}  {'bw0%':>9s}  "
      f"{'bw-1%':>9s}  {'bw-2%':>9s}  {'|C|^2':>12s}  {'time':>6s}")
print("-" * 90)

for tau in tau_values:
    t0 = time.time()

    geom8 = compute_8d_geometry(tau, gens, f_abc, B_ab)
    R12_dyn, K_diag = build_12d_riemann_dynamic(geom8['R_abcd'], v_terminal)
    C12_dyn, Ric12_dyn, R12s_dyn, C12sq_dyn, tr_err_dyn = compute_12d_weyl(R12_dyn)
    cmpp_type, best_decomp, best_params, n_tested, all_types, min_bw2 = scan_wand(C12_dyn)
    weyl_op = weyl_operator_12d(C12_dyn)

    dt = time.time() - t0

    results_dynamic[tau] = {
        'geom8': geom8, 'K_diag': K_diag,
        'R12_scalar': R12s_dyn, 'C12_sq': C12sq_dyn,
        'cmpp_type': cmpp_type, 'best_decomp': best_decomp,
        'best_params': best_params, 'n_tested': n_tested,
        'weyl_op': weyl_op, 'all_types': all_types,
        'min_bw2_frac': min_bw2, 'time': dt,
    }

    if best_decomp is not None:
        bw = best_decomp['bw_norms']
        tot = best_decomp['total']
        fracs = {k: v/tot*100 for k,v in bw.items()} if tot > 0 else {k:0 for k in bw}
        print(f"{tau:8.4f}  {cmpp_type:>6s}  {fracs[+2]:9.4f}  {fracs[+1]:9.4f}  "
              f"{fracs[0]:9.4f}  {fracs[-1]:9.4f}  {fracs[-2]:9.4f}  "
              f"{C12sq_dyn:12.6f}  {dt:5.1f}s")


# Dynamic details
print(f"\n--- Dynamic case details ---")
for tau in tau_values:
    r = results_dynamic[tau]
    print(f"\n  tau={tau:.4f}: CMPP={r['cmpp_type']}, |C|^2={r['C12_sq']:.6f}, "
          f"min_bw2={r['min_bw2_frac']:.6e}")
    print(f"    K_diag = {r['K_diag']}")
    print(f"    |K|^2 = {np.sum(r['K_diag']**2):.6f}")
    wo = r['weyl_op']
    print(f"    Weyl op: {wo['n_distinct']} distinct eigs, "
          f"trace={wo['trace']:.2e}, sym={wo['sym_err']:.2e}")


# -----------------------------------------------------------
# COMPARISON: 8D Riemannian vs 12D Lorentzian
# -----------------------------------------------------------
print(f"\n\n{'='*80}")
print(f"  COMPARISON: 8D RIEMANNIAN (S49) vs 12D LORENTZIAN (S50)")
print(f"{'='*80}")

s49_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 's49_cmpp_transition.npz')
if os.path.exists(s49_path):
    s49 = np.load(s49_path, allow_pickle=True)
    s49_taus = s49['tau_values']
    s49_types = s49['cmpp_types']
    s49_bw = s49['bw_fracs']

    print(f"\n  {'tau':>8s}  {'8D_Riem':>8s}  {'8D_bw1%':>9s}  "
          f"{'12D_Lor_S':>10s}  {'12D_bw1%':>9s}  {'12D_bw2%':>9s}  "
          f"{'12D_Lor_D':>10s}  {'CHANGE?':>8s}")
    print("-" * 90)

    for tau in tau_values:
        idx49 = np.argmin(np.abs(s49_taus - tau))
        rtype = str(s49_types[idx49]) if abs(s49_taus[idx49] - tau) < 0.01 else 'N/A'
        rbw1 = s49_bw[idx49, 1]*100 if rtype != 'N/A' else float('nan')

        sr = results_static[tau]
        dr = results_dynamic[tau]
        st = sr['cmpp_type']
        dt_type = dr['cmpp_type']

        if sr['best_decomp'] is not None:
            sbw = sr['best_decomp']['bw_norms']
            stot = sr['best_decomp']['total']
            sbw1 = sbw[+1]/stot*100 if stot > 0 else 0
            sbw2 = sbw[+2]/stot*100 if stot > 0 else 0
        else:
            sbw1, sbw2 = 0, 0

        changed = "YES" if st != rtype and rtype != 'N/A' else "NO"
        print(f"  {tau:8.4f}  {rtype:>8s}  {rbw1:9.4f}  "
              f"{st:>10s}  {sbw1:9.4f}  {sbw2:9.4f}  "
              f"{dt_type:>10s}  {changed:>8s}")
else:
    print("  S49 data not found.")


# -----------------------------------------------------------
# GATE VERDICT
# -----------------------------------------------------------
print(f"\n\n{'='*80}")
print(f"  GATE VERDICT: LORENTZIAN-CMPP-50")
print(f"{'='*80}")

static_types = [results_static[t]['cmpp_type'] for t in tau_values]
dynamic_types = [results_dynamic[t]['cmpp_type'] for t in tau_values]

# Detect changes
def find_changes(types_list):
    changes = []
    for i in range(1, len(tau_values)):
        if types_list[i] != types_list[i-1]:
            changes.append((tau_values[i-1], tau_values[i], types_list[i-1], types_list[i]))
    return changes

sc = find_changes(static_types)
dc = find_changes(dynamic_types)

def near_537(changes, tol):
    return any(abs(a - 0.537) < tol or abs(b - 0.537) < tol for a, b, _, _ in changes)

lorentzian_differs = any(st != 'II' for st in static_types)

if near_537(sc, 0.01) or near_537(dc, 0.01):
    verdict = "PASS"
    reason = "CMPP type changes at tau = 0.537"
elif near_537(sc, 0.1) or near_537(dc, 0.1):
    verdict = "INFO"
    reason = "CMPP type changes near tau = 0.537"
elif sc or dc:
    verdict = "INFO"
    parts = [f"static:{a:.3f}-{b:.3f} {t1}->{t2}" for a,b,t1,t2 in sc]
    parts += [f"dynamic:{a:.3f}-{b:.3f} {t1}->{t2}" for a,b,t1,t2 in dc]
    reason = "Type changes elsewhere: " + "; ".join(parts)
elif lorentzian_differs:
    verdict = "INFO"
    reason = "Lorentzian 12D type differs from Riemannian 8D but constant across tau"
else:
    verdict = "FAIL"
    reason = f"Constant type across all tau (static={static_types[0]}, dynamic={dynamic_types[0]})"

print(f"\n  Static:  {list(zip([f'{t:.3f}' for t in tau_values], static_types))}")
print(f"  Dynamic: {list(zip([f'{t:.3f}' for t in tau_values], dynamic_types))}")
print(f"  Static changes: {len(sc)} {sc}")
print(f"  Dynamic changes: {len(dc)} {dc}")
print(f"  Lorentzian differs from Riemannian: {lorentzian_differs}")

# Additional: track min bw+2 across tau
print(f"\n  Min bw+2 fraction across tau (static):")
for tau in tau_values:
    print(f"    tau={tau:.4f}: min_bw+2 = {results_static[tau]['min_bw2_frac']:.6e}")
print(f"  Min bw+2 fraction across tau (dynamic):")
for tau in tau_values:
    print(f"    tau={tau:.4f}: min_bw+2 = {results_dynamic[tau]['min_bw2_frac']:.6e}")

print(f"\n  VERDICT: {verdict}")
print(f"  REASON: {reason}")


# -----------------------------------------------------------
# SAVE DATA
# -----------------------------------------------------------
tau_arr = np.array(tau_values)

bw_s = np.zeros((len(tau_values), 5))
bw_d = np.zeros((len(tau_values), 5))
for i, tau in enumerate(tau_values):
    for case, bw_arr in [(results_static, bw_s), (results_dynamic, bw_d)]:
        bd = case[tau]['best_decomp']
        if bd is not None and bd['total'] > 0:
            for j, w in enumerate([+2,+1,0,-1,-2]):
                bw_arr[i, j] = bd['bw_norms'][w] / bd['total']

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 's50_lorentzian_cmpp.npz')
np.savez_compressed(out_path,
    tau_values=tau_arr,
    static_cmpp_types=np.array(static_types),
    dynamic_cmpp_types=np.array(dynamic_types),
    bw_fracs_static=bw_s,
    bw_fracs_dynamic=bw_d,
    C12_sq_static=np.array([results_static[t]['C12_sq'] for t in tau_values]),
    C12_sq_dynamic=np.array([results_dynamic[t]['C12_sq'] for t in tau_values]),
    n_distinct_static=np.array([results_static[t]['weyl_op']['n_distinct'] for t in tau_values]),
    n_distinct_dynamic=np.array([results_dynamic[t]['weyl_op']['n_distinct'] for t in tau_values]),
    min_bw2_static=np.array([results_static[t]['min_bw2_frac'] for t in tau_values]),
    min_bw2_dynamic=np.array([results_dynamic[t]['min_bw2_frac'] for t in tau_values]),
    verdict=np.array([verdict]),
    reason=np.array([reason]),
)
print(f"\n  Data saved: {out_path}")

# -----------------------------------------------------------
# PLOT
# -----------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

bw_labels = ['bw+2', 'bw+1', 'bw 0', 'bw-1', 'bw-2']
for j, lab in enumerate(bw_labels):
    axes[0,0].plot(tau_arr, bw_s[:, j]*100, 'o-', label=lab, ms=5)
axes[0,0].set_xlabel('tau'); axes[0,0].set_ylabel('Fraction (%)')
axes[0,0].set_title('Static 12D: BW fractions (best WAND)')
axes[0,0].legend(fontsize=8)
axes[0,0].axvline(0.537, color='gray', ls='--', alpha=0.5)
axes[0,0].set_yscale('symlog', linthresh=0.1)

for j, lab in enumerate(bw_labels):
    axes[0,1].plot(tau_arr, bw_d[:, j]*100, 'o-', label=lab, ms=5)
axes[0,1].set_xlabel('tau'); axes[0,1].set_ylabel('Fraction (%)')
axes[0,1].set_title(f'Dynamic 12D: BW fractions (v={v_terminal:.1f})')
axes[0,1].legend(fontsize=8)
axes[0,1].axvline(0.537, color='gray', ls='--', alpha=0.5)
axes[0,1].set_yscale('symlog', linthresh=0.1)

C_s = np.array([results_static[t]['C12_sq'] for t in tau_values])
C_d = np.array([results_dynamic[t]['C12_sq'] for t in tau_values])
axes[1,0].plot(tau_arr, C_s, 'bo-', label='Static')
axes[1,0].plot(tau_arr, C_d, 'rs-', label='Dynamic')
axes[1,0].set_xlabel('tau'); axes[1,0].set_ylabel('|C|^2_{12D}')
axes[1,0].set_title('12D Weyl norm squared')
axes[1,0].legend()
axes[1,0].axvline(0.537, color='gray', ls='--', alpha=0.5)

mbw2_s = np.array([results_static[t]['min_bw2_frac'] for t in tau_values])
mbw2_d = np.array([results_dynamic[t]['min_bw2_frac'] for t in tau_values])
axes[1,1].semilogy(tau_arr, mbw2_s, 'bo-', label='Static min(bw+2)')
axes[1,1].semilogy(tau_arr, mbw2_d, 'rs-', label='Dynamic min(bw+2)')
axes[1,1].set_xlabel('tau'); axes[1,1].set_ylabel('min bw+2 / total')
axes[1,1].set_title('Minimum bw+2 fraction (lower = more special)')
axes[1,1].legend()
axes[1,1].axvline(0.537, color='gray', ls='--', alpha=0.5)

plt.tight_layout()
ppath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 's50_lorentzian_cmpp.png')
plt.savefig(ppath, dpi=150)
print(f"  Plot saved: {ppath}")

t_end = time.time()
print(f"\n  Total runtime: {t_end - t_start:.1f}s")
print(f"\n{'='*80}")
print(f"  COMPUTATION COMPLETE")
print(f"{'='*80}")
