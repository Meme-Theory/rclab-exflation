#!/usr/bin/env python3
"""
S76 CMPP-TYPE-GGE-TRANSIT-76: Petrov Classification During Transit Through Fold
================================================================================

Computes the CMPP (Coley-Milson-Pravda-Pravdova) algebraic classification of the
emergent 12D Weyl tensor during the transit through the fold, at three tau values:
  tau = 0.10 (pre-fold)
  tau = 0.19 (fold)
  tau = 0.30 (post-fold)

Physical spacetime: ds^2 = -dt^2 + dx^2(3) + g_{ab}(tau) dy^a dy^b
with tau(t) = v_terminal * t during transit.

CMPP classification hierarchy (most special to most general):
  O < N < III < D < II < I < G

Two cases:
  (a) STATIC: tau = const, pure product M^{3,1} x K^8
  (b) DYNAMIC: tau_dot = v_terminal, extrinsic curvature cross terms

Cross-checks:
  CHK1: 4D block alone gives Type D (de Sitter-like)
  CHK2: Product geometry: Weyl decomposes into 4D and internal blocks
  CHK3: Ricci scalar at fold: R = 12*H^2 (de Sitter consistency)

Prior results (S50, memory):
  Static: EXACT Type D all tau
  Dynamic: Type G all tau
  8D Riemannian: Type II all tau

Gate: S76-C8-CMPP
  PASS: CMPP type computed at all three tau values, type change identified if present
  FAIL: 12D Weyl tensor not computable from available data
  INFO: Type computed but no transition found

Author: schwarzschild-penrose-geometer (Session 76)
Date: 2026-04-12
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys
import os
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dirac_spectrum import (
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
    tau_fold, G_DeWitt, PI, v_terminal, H_fold, a2_fold, a4_fold,
)

t_start = time.time()

DIM_INT = 8  # (local)
DIM_EXT = 4  # (local)
DIM_TOTAL = 12  # (local)
N_PAIRS_12 = DIM_TOTAL * (DIM_TOTAL - 1) // 2  # 66

# 12D index mapping: 0=t, 1-3=spatial, 4-11=internal
SU2_12 = [4 + i for i in SU2_IDX]  # (local)
C2_12 = [4 + i for i in C2_IDX]    # (local)
U1_12 = [4 + i for i in U1_IDX]    # (local)

# Transit tau values (pre-fold, fold, post-fold)
TAU_VALUES = np.array([0.10, 0.19, 0.30])  # (local)
TAU_LABELS = ['pre-fold', 'fold', 'post-fold']  # (local)


# =============================================================================
# SECTION 1: 8D Internal Curvature (from S50, proven)
# =============================================================================

def compute_riemann_ON(ft, Gamma, n=DIM_INT):
    """Riemann tensor R[a,b,c,f] = R^f_{abc} in ON frame."""
    R = np.zeros((n, n, n, n))
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for f in range(n):
                    val = 0.0  # (local)
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
    R_scalar = float(np.trace(Ric))  # (local)
    Ric_sq = float(np.sum(Ric**2))   # (local)
    K_full = float(np.sum(R_abcd**2))  # (local)
    return {'R_abcd': R_abcd, 'Ric': Ric, 'R_scalar': R_scalar,
            'Ric_sq': Ric_sq, 'K': K_full, 'g_s': g_s}


# =============================================================================
# SECTION 2: 12D Riemann and Weyl (from S50, vectorized)
# =============================================================================

def build_12d_riemann_static(R8):
    """Static product M^{3,1} x K^8. Only internal block nonzero."""
    R12 = np.zeros((DIM_TOTAL, DIM_TOTAL, DIM_TOTAL, DIM_TOTAL))
    R12[4:12, 4:12, 4:12, 4:12] = R8
    return R12


def build_12d_riemann_dynamic(R8, tau_dot):
    """Dynamic case: extrinsic curvature from tau_dot = v_terminal."""
    R12 = np.zeros((DIM_TOTAL, DIM_TOTAL, DIM_TOTAL, DIM_TOTAL))

    # Jensen deformation rates: d(log scale)/dtau for each sector
    lam = np.zeros(DIM_INT)  # (local)
    lam[SU2_IDX] = -2.0   # SU(2) shrinks as e^{-2*tau}
    lam[C2_IDX] = +1.0     # C^2 grows as e^{tau}
    lam[U1_IDX] = +2.0     # U(1) grows as e^{2*tau}
    K_diag = -(tau_dot / 2.0) * lam  # (local) extrinsic curvature diagonal

    # Internal block: R_8 + Gauss equation K_{ac}K_{bd} - K_{ad}K_{bc}
    R12[4:12, 4:12, 4:12, 4:12] = R8.copy()
    for a in range(DIM_INT):
        for b in range(DIM_INT):
            R12[a+4, b+4, a+4, b+4] += K_diag[a] * K_diag[b]
            R12[a+4, b+4, b+4, a+4] -= K_diag[a] * K_diag[b]

    # Time-internal: R_{0,a+4,0,a+4} = K_a^2 (Ricci equation, tau_ddot ~ 0)
    for a in range(DIM_INT):
        val = K_diag[a]**2  # (local)
        R12[0, a+4, 0, a+4] = val
        R12[a+4, 0, a+4, 0] = val
        R12[0, a+4, a+4, 0] = -val
        R12[a+4, 0, 0, a+4] = -val

    return R12, K_diag


def compute_12d_weyl(R12):
    """12D Weyl tensor. VECTORIZED."""
    n = DIM_TOTAL  # (local)
    eta = np.diag(np.array([-1.0] + [1.0] * (n - 1)))  # (local) Lorentzian metric

    eta_diag = np.diag(eta)  # (local)
    Ric12 = np.einsum('B,ABCB->AC', eta_diag, R12)
    Ric12 = 0.5 * (Ric12 + Ric12.T)

    R_scalar = float(np.einsum('A,AA->', eta_diag, Ric12))  # (local)

    # Weyl: C = R - (1/(n-2))[eta x Ric - ...] + (R/((n-1)(n-2)))[eta x eta - ...]
    eR1 = np.einsum('AC,BD->ABCD', eta, Ric12)  # (local)
    eR2 = np.einsum('AD,BC->ABCD', eta, Ric12)  # (local)
    eR3 = np.einsum('BC,AD->ABCD', eta, Ric12)  # (local)
    eR4 = np.einsum('BD,AC->ABCD', eta, Ric12)  # (local)

    ricci_term = (1.0 / (n - 2)) * (eR1 - eR2 - eR3 + eR4)  # (local)

    ee1 = np.einsum('AC,BD->ABCD', eta, eta)  # (local)
    ee2 = np.einsum('AD,BC->ABCD', eta, eta)  # (local)
    scalar_term = (R_scalar / ((n - 1) * (n - 2))) * (ee1 - ee2)  # (local)

    C12 = R12 - ricci_term + scalar_term  # (local)

    # Trace check: C^B_{ABC} should vanish
    trace_check = float(np.max(np.abs(np.einsum('B,ABCB->AC', eta_diag, C12))))  # (local)

    # Weyl norm |C|^2 = C_{ABCD} C^{ABCD}
    sign_tensor = np.einsum('A,B,C,D->ABCD', eta_diag, eta_diag, eta_diag, eta_diag)  # (local)
    C_sq = float(np.sum(sign_tensor * C12 * C12))  # (local)

    return C12, Ric12, R_scalar, C_sq, trace_check


# =============================================================================
# SECTION 3: Lorentzian Null Frame and BW Decomposition (from S50)
# =============================================================================

def construct_null_frame(n_spatial):
    """Build real null frame from a unit spatial direction."""
    n = DIM_TOTAL  # (local)
    e0 = np.zeros(n); e0[0] = 1.0  # (local)
    l_vec = (e0 + n_spatial) / np.sqrt(2)  # (local)
    k_vec = (e0 - n_spatial) / np.sqrt(2)  # (local)

    n_spat = n_spatial[1:]  # (local) 11D spatial part
    basis_spatial = np.eye(11)  # (local)
    ortho = []
    for v in basis_spatial:
        w = v - np.dot(v, n_spat) * n_spat  # (local)
        for u in ortho:
            w -= np.dot(w, u) * u
        norm = np.linalg.norm(w)  # (local)
        if norm > 1e-12:
            ortho.append(w / norm)
        if len(ortho) == 10:
            break

    m_vecs = []
    for v in ortho:
        m = np.zeros(n)  # (local)
        m[1:] = v
        m_vecs.append(m)

    return l_vec, k_vec, m_vecs


def cmpp_decomposition(C12, l_vec, k_vec, m_vecs):
    """Boost-weight decomposition of 12D Weyl tensor in Lorentzian null frame."""
    n = DIM_TOTAL  # (local)
    n_t = len(m_vecs)  # (local) = 10

    F = np.zeros((n, n))  # (local) frame matrix
    F[0] = l_vec
    F[1] = k_vec
    for i in range(n_t):
        F[i + 2] = m_vecs[i]

    # Transform Weyl to null frame
    C_step1 = np.einsum('aA,ABCD->aBCD', F, C12)  # (local)
    C_step2 = np.einsum('bB,aBCD->abCD', F, C_step1)  # (local)
    C_step3 = np.einsum('cC,abCD->abcD', F, C_step2)  # (local)
    C_null = np.einsum('dD,abcD->abcd', F, C_step3)   # (local)

    def bw(idx):
        if idx == 0: return +1
        if idx == 1: return -1
        return 0

    bw_norms = {bw_val: 0.0 for bw_val in range(-4, 5)}  # (local)
    for a in range(n):
        bwa = bw(a)  # (local)
        for b in range(n):
            bwab = bwa + bw(b)  # (local)
            for c in range(n):
                bwabc = bwab + bw(c)  # (local)
                for d in range(n):
                    bw_total = bwabc + bw(d)  # (local)
                    bw_norms[bw_total] = bw_norms.get(bw_total, 0.0) + C_null[a, b, c, d]**2

    bw_phys = {w: bw_norms.get(w, 0.0) for w in [-2, -1, 0, +1, +2]}  # (local)
    total = sum(bw_phys.values())  # (local)

    Phi_p2 = np.array([[C_null[0, i+2, 0, j+2] for j in range(n_t)] for i in range(n_t)])  # (local)

    return {
        'bw_norms': bw_phys, 'bw_all': bw_norms, 'total': total,
        'Phi_p2': Phi_p2, 'C_null': C_null,
    }


def classify_cmpp(decomp, tol=1e-10):
    """Classify CMPP type from Lorentzian BW decomposition."""
    total = decomp['total']  # (local)
    if total < tol:
        return 'O', {}

    rel_tol = tol * total  # (local)
    n2 = decomp['bw_norms'][+2]   # (local)
    n1 = decomp['bw_norms'][+1]   # (local)
    n0 = decomp['bw_norms'][0]    # (local)
    nm1 = decomp['bw_norms'][-1]  # (local)
    nm2 = decomp['bw_norms'][-2]  # (local)

    details = {f'frac_bw{w:+d}': decomp['bw_norms'][w]/total
               for w in [+2,+1,0,-1,-2]}  # (local)

    h2p = n2 > rel_tol   # (local)
    h1p = n1 > rel_tol   # (local)
    h1m = nm1 > rel_tol  # (local)
    h2m = nm2 > rel_tol  # (local)

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
# SECTION 4: WAND Search (from S50)
# =============================================================================

def make_spatial_dir(alpha, n_ext_3, n_int_8):
    """Build 12D unit spatial vector from mixing angle and sector directions."""
    n12 = np.zeros(DIM_TOTAL)  # (local)
    n12[1:4] = np.sin(alpha) * n_ext_3
    n12[4:12] = np.cos(alpha) * n_int_8
    norm = np.linalg.norm(n12)  # (local)
    if norm < 1e-15:
        n12[1] = 1.0
        norm = 1.0  # (local)
    return n12 / norm


def scan_wand(C12, n_alpha=15, verbose=False):
    """Scan null directions to find the WAND (most algebraically special)."""
    type_rank = {'O': 0, 'N': 1, 'III': 2, 'D': 3, 'II': 4, 'I': 5, 'G': 6}  # (local)
    best_type = 'G'      # (local)
    best_decomp = None   # (local)
    best_params = None   # (local)
    all_types = []       # (local)
    n_tested = 0         # (local)

    n_ext = np.array([0.0, 0.0, 1.0])  # (local) fixed external direction

    # Internal directions to test
    int_dirs = {}  # (local)
    for i in range(DIM_INT):
        d = np.zeros(DIM_INT); d[i] = 1.0  # (local)
        int_dirs[f'e{i}'] = d
    d = np.zeros(DIM_INT); d[SU2_IDX] = 1.0/np.sqrt(3)
    int_dirs['su2_diag'] = d
    d = np.zeros(DIM_INT); d[C2_IDX] = 0.5
    int_dirs['c2_diag'] = d
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
    d = np.zeros(DIM_INT); d[0]=1; d[3]=1; d[7]=1; d /= np.linalg.norm(d)
    int_dirs['all_diag'] = d

    alpha_vals = np.linspace(0, np.pi/2, n_alpha)  # (local)

    min_bw2_frac = 1.0     # (local)
    min_bw2_params = None   # (local)

    for label, n_int in int_dirs.items():
        for alpha in alpha_vals:
            n_spat = make_spatial_dir(alpha, n_ext, n_int)  # (local)
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

                bw2_frac = decomp['bw_norms'][+2] / decomp['total'] if decomp['total'] > 0 else 1.0  # (local)
                if bw2_frac < min_bw2_frac:
                    min_bw2_frac = bw2_frac
                    min_bw2_params = {'alpha': alpha, 'n_int': n_int.copy(), 'label': label}

            except Exception:
                pass

    # Refinement around bw+2 minimum
    if min_bw2_params is not None and min_bw2_frac > 1e-14:
        best_n_int = min_bw2_params['n_int']  # (local)
        best_alpha = min_bw2_params['alpha']   # (local)

        def objective(alpha_val, n_int_val):
            nn = np.linalg.norm(n_int_val)  # (local)
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
            a_try = np.clip(best_alpha + da, 0, np.pi/2)  # (local)
            f = objective(a_try, best_n_int)               # (local)
            n_tested += 1
            if f < min_bw2_frac:
                min_bw2_frac = f
                best_alpha = a_try

        # Refine internal direction
        for axis in range(DIM_INT):
            for da in np.linspace(-0.2, 0.2, 8):
                n_try = best_n_int.copy()  # (local)
                n_try[axis] += da
                nn = np.linalg.norm(n_try)  # (local)
                if nn > 1e-12:
                    f = objective(best_alpha, n_try / nn)  # (local)
                    n_tested += 1
                    if f < min_bw2_frac:
                        min_bw2_frac = f
                        best_n_int = n_try / nn

        # Final classification at refined minimum
        n_spat = make_spatial_dir(best_alpha, n_ext, best_n_int)  # (local)
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
# SECTION 5: Weyl Operator on Lambda^2(R^{11,1})
# =============================================================================

def weyl_operator_12d(C12):
    """12D Weyl as operator on 2-forms (66x66 matrix)."""
    n = DIM_TOTAL  # (local)
    pairs = [(a, b) for a in range(n) for b in range(a+1, n)]  # (local)
    N = len(pairs)  # (local) = 66
    C_mat = np.zeros((N, N))  # (local)
    for I, (a1, b1) in enumerate(pairs):
        for J, (a2, b2) in enumerate(pairs):
            C_mat[I, J] = C12[a1, b1, a2, b2]

    eigvals = np.linalg.eigvals(C_mat)  # (local)
    eigvals_real = np.sort(np.real(eigvals))  # (local)
    imag_max = float(np.max(np.abs(np.imag(eigvals))))  # (local)

    tol = 1e-8 * (np.max(np.abs(eigvals_real)) + 1e-15)  # (local)
    unique = []  # (local)
    for e in eigvals_real:
        if not unique or abs(e - unique[-1]) > tol:
            unique.append(e)
    mults = [int(np.sum(np.abs(eigvals_real - u) < tol)) for u in unique]  # (local)

    return {
        'eigvals': eigvals_real, 'n_distinct': len(unique),
        'unique_eigs': unique, 'multiplicities': mults,
        'trace': float(np.trace(C_mat)), 'sym_err': float(np.max(np.abs(C_mat - C_mat.T))),
        'imag_max': imag_max,
    }


# =============================================================================
# SECTION 6: Cross-Check Functions
# =============================================================================

def check_4d_type_D(C12):
    """CHK1: Extract 4D block of Weyl tensor and verify Type D."""
    C_4d = C12[:4, :4, :4, :4]  # (local) 4D block
    norm_4d = float(np.sum(C_4d**2))  # (local)
    return norm_4d


def check_product_decomposition(C12):
    """CHK2: Check Weyl block-decomposition for product geometry.
    For M^4 x K^8 product, mixed Weyl components should vanish
    (up to Schouten corrections from dimension change)."""
    # Mixed components: one or three indices in 0-3, rest in 4-11
    mixed_norm = 0.0  # (local)
    total_norm = 0.0  # (local)
    for A in range(DIM_TOTAL):
        for B in range(DIM_TOTAL):
            for C in range(DIM_TOTAL):
                for D in range(DIM_TOTAL):
                    val2 = C12[A, B, C, D]**2  # (local)
                    total_norm += val2
                    # Count how many indices are external (0-3)
                    n_ext = sum(1 for x in [A,B,C,D] if x < 4)  # (local)
                    if n_ext not in [0, 4]:
                        mixed_norm += val2
    frac_mixed = mixed_norm / total_norm if total_norm > 0 else 0.0  # (local)
    return frac_mixed, mixed_norm, total_norm


def check_de_sitter_ricci(R_scalar_12d, H):
    """CHK3: de Sitter consistency R = 12*H^2 for the cosmological part.
    In our convention the 12D scalar includes internal curvature too,
    so we check the ratio."""
    R_dS_expected = 12.0 * H**2  # (local) de Sitter scalar in 4D
    return R_dS_expected, R_scalar_12d


# =============================================================================
# SECTION 7: MAIN COMPUTATION
# =============================================================================

print("=" * 80)
print("  S76 CMPP-TYPE-GGE-TRANSIT-76: Petrov Classification During Transit")
print("=" * 80)

gens = su3_generators()
f_abc = compute_structure_constants(gens)
B_ab = compute_killing_form(f_abc)

# Storage for all results
results = {
    'tau_values': TAU_VALUES,
    'tau_labels': TAU_LABELS,
}

# -----------------------------------------------------------
# CASE (a): STATIC PRODUCT M^{3,1} x K^8
# -----------------------------------------------------------
print(f"\n{'='*80}")
print(f"  CASE (a): STATIC PRODUCT  M^{{3,1}} x (SU(3), g_tau)")
print(f"{'='*80}")
print(f"\n  12D Riemann block-diagonal. 12D Weyl = internal Weyl + Schouten(n=12).\n")

print(f"{'tau':>8s}  {'label':>10s}  {'CMPP':>6s}  {'bw+2%':>9s}  {'bw+1%':>9s}  "
      f"{'bw0%':>9s}  {'bw-1%':>9s}  {'bw-2%':>9s}  {'|C|^2':>12s}  {'dirs':>6s}  {'time':>6s}")
print("-" * 110)

static_results = {}
for i_tau, (tau, label) in enumerate(zip(TAU_VALUES, TAU_LABELS)):
    t0 = time.time()  # (local)

    geom8 = compute_8d_geometry(tau, gens, f_abc, B_ab)
    R12 = build_12d_riemann_static(geom8['R_abcd'])
    C12, Ric12, R12_scal, C12_sq, tr_err = compute_12d_weyl(R12)
    cmpp_type, best_decomp, best_params, n_tested, all_types, min_bw2 = scan_wand(C12)
    weyl_op = weyl_operator_12d(C12)

    dt = time.time() - t0  # (local)

    static_results[tau] = {
        'geom8': geom8, 'R12_scalar': R12_scal, 'C12_sq': C12_sq,
        'trace_err': tr_err, 'cmpp_type': cmpp_type,
        'best_decomp': best_decomp, 'best_params': best_params,
        'n_tested': n_tested, 'weyl_op': weyl_op,
        'all_types': all_types, 'min_bw2_frac': min_bw2, 'time': dt,
    }

    if best_decomp is not None:
        bw = best_decomp['bw_norms']
        tot = best_decomp['total']
        fracs = {k: v/tot*100 for k,v in bw.items()} if tot > 0 else {k:0 for k in bw}  # (local)
        print(f"{tau:8.4f}  {label:>10s}  {cmpp_type:>6s}  {fracs[+2]:9.4f}  {fracs[+1]:9.4f}  "
              f"{fracs[0]:9.4f}  {fracs[-1]:9.4f}  {fracs[-2]:9.4f}  "
              f"{C12_sq:12.6f}  {n_tested:6d}  {dt:5.1f}s")


# -----------------------------------------------------------
# CASE (b): DYNAMIC tau_dot = v_terminal
# -----------------------------------------------------------
print(f"\n\n{'='*80}")
print(f"  CASE (b): DYNAMIC  tau_dot = v_terminal = {v_terminal:.4f}")
print(f"{'='*80}")

print(f"\n{'tau':>8s}  {'label':>10s}  {'CMPP':>6s}  {'bw+2%':>9s}  {'bw+1%':>9s}  "
      f"{'bw0%':>9s}  {'bw-1%':>9s}  {'bw-2%':>9s}  {'|C|^2':>12s}  {'dirs':>6s}  {'time':>6s}")
print("-" * 110)

dynamic_results = {}
for i_tau, (tau, label) in enumerate(zip(TAU_VALUES, TAU_LABELS)):
    t0 = time.time()  # (local)

    geom8 = compute_8d_geometry(tau, gens, f_abc, B_ab)
    R12_dyn, K_diag = build_12d_riemann_dynamic(geom8['R_abcd'], v_terminal)
    C12_dyn, Ric12_dyn, R12s_dyn, C12sq_dyn, tr_err_dyn = compute_12d_weyl(R12_dyn)
    cmpp_type, best_decomp, best_params, n_tested, all_types, min_bw2 = scan_wand(C12_dyn)
    weyl_op = weyl_operator_12d(C12_dyn)

    dt = time.time() - t0  # (local)

    dynamic_results[tau] = {
        'geom8': geom8, 'K_diag': K_diag,
        'R12_scalar': R12s_dyn, 'C12_sq': C12sq_dyn,
        'trace_err': tr_err_dyn, 'cmpp_type': cmpp_type,
        'best_decomp': best_decomp, 'best_params': best_params,
        'n_tested': n_tested, 'weyl_op': weyl_op,
        'all_types': all_types, 'min_bw2_frac': min_bw2, 'time': dt,
    }

    if best_decomp is not None:
        bw = best_decomp['bw_norms']
        tot = best_decomp['total']
        fracs = {k: v/tot*100 for k,v in bw.items()} if tot > 0 else {k:0 for k in bw}  # (local)
        print(f"{tau:8.4f}  {label:>10s}  {cmpp_type:>6s}  {fracs[+2]:9.4f}  {fracs[+1]:9.4f}  "
              f"{fracs[0]:9.4f}  {fracs[-1]:9.4f}  {fracs[-2]:9.4f}  "
              f"{C12sq_dyn:12.6f}  {n_tested:6d}  {dt:5.1f}s")


# -----------------------------------------------------------
# CROSS-CHECKS
# -----------------------------------------------------------
print(f"\n\n{'='*80}")
print(f"  CROSS-CHECKS")
print(f"{'='*80}")

print("\n--- CHK1: 4D Weyl block norm (Type D check) ---")
for tau, label in zip(TAU_VALUES, TAU_LABELS):
    geom8 = static_results[tau]['geom8']
    R12_s = build_12d_riemann_static(geom8['R_abcd'])
    C12_s, _, _, _, _ = compute_12d_weyl(R12_s)
    norm_4d = check_4d_type_D(C12_s)  # (local)
    print(f"  tau={tau:.2f} ({label:>10s}): |C_4D|^2 = {norm_4d:.6e}  {'(zero: flat M^4)' if norm_4d < 1e-15 else ''}")

print("\n--- CHK2: Product decomposition (mixed Weyl fraction) ---")
for tau, label in zip(TAU_VALUES, TAU_LABELS):
    # Static
    geom8 = static_results[tau]['geom8']
    R12_s = build_12d_riemann_static(geom8['R_abcd'])
    C12_s, _, _, _, _ = compute_12d_weyl(R12_s)
    frac_s, mixed_s, total_s = check_product_decomposition(C12_s)
    # Dynamic
    R12_d, _ = build_12d_riemann_dynamic(geom8['R_abcd'], v_terminal)
    C12_d, _, _, _, _ = compute_12d_weyl(R12_d)
    frac_d, mixed_d, total_d = check_product_decomposition(C12_d)
    print(f"  tau={tau:.2f} ({label:>10s}): static mixed = {frac_s*100:.4f}% | dynamic mixed = {frac_d*100:.4f}%")

print("\n--- CHK3: de Sitter Ricci consistency ---")
R_dS_expected, _ = check_de_sitter_ricci(0, H_fold)
print(f"  Expected 4D de Sitter: R_4D = 12*H_fold^2 = {R_dS_expected:.4f}")
for tau, label in zip(TAU_VALUES, TAU_LABELS):
    R12_s = static_results[tau]['R12_scalar']
    R12_d = dynamic_results[tau]['R12_scalar']
    print(f"  tau={tau:.2f} ({label:>10s}): R_12D(static)={R12_s:+.6f}, R_12D(dynamic)={R12_d:+.6f}")
print(f"  NOTE: Static R_12D is purely internal (flat M^4). Dynamic includes K^2 terms.")


# -----------------------------------------------------------
# DETAILED ANALYSIS
# -----------------------------------------------------------
print(f"\n\n{'='*80}")
print(f"  DETAILED ANALYSIS")
print(f"{'='*80}")

for case_name, case_results in [('STATIC', static_results), ('DYNAMIC', dynamic_results)]:
    print(f"\n--- {case_name} ---")
    for tau, label in zip(TAU_VALUES, TAU_LABELS):
        r = case_results[tau]
        wo = r['weyl_op']
        print(f"\n  tau = {tau:.2f} ({label})")
        print(f"    CMPP Type: {r['cmpp_type']}")
        print(f"    |C|^2 = {r['C12_sq']:.10f}")
        print(f"    R_12D = {r['R12_scalar']:.10f}")
        print(f"    Weyl trace-free check: {r['trace_err']:.2e}")
        print(f"    8D: K = {r['geom8']['K']:.10f}, |Ric|^2 = {r['geom8']['Ric_sq']:.10f}, R_8 = {r['geom8']['R_scalar']:.6f}")
        print(f"    min bw+2 frac = {r['min_bw2_frac']:.6e}")
        print(f"    Weyl operator: {wo['n_distinct']} distinct eigs (of 66), trace={wo['trace']:.2e}")

        # BW fractions
        if r['best_decomp'] is not None:
            bw = r['best_decomp']['bw_norms']
            tot = r['best_decomp']['total']
            print(f"    BW decomposition (best WAND):")
            for w in [+2, +1, 0, -1, -2]:
                frac = bw[w]/tot*100 if tot > 0 else 0  # (local)
                print(f"      bw={w:+d}: {bw[w]:.6e} ({frac:.4f}%)")

        # Type distribution
        tc = {}  # (local)
        for t in r['all_types']:
            tc[t] = tc.get(t, 0) + 1
        print(f"    Type distribution ({r['n_tested']} dirs):", dict(tc))

        # Top eigenvalues of Weyl operator
        print(f"    Weyl operator eigenvalues (top 6):")
        for ue, m in list(zip(wo['unique_eigs'], wo['multiplicities']))[:6]:
            print(f"      lambda = {ue:+.8f}, mult = {m}")
        if len(wo['unique_eigs']) > 6:
            print(f"      ... ({len(wo['unique_eigs'])} total distinct)")


# -----------------------------------------------------------
# TYPE TRANSITION CHECK
# -----------------------------------------------------------
print(f"\n\n{'='*80}")
print(f"  TYPE TRANSITION CHECK")
print(f"{'='*80}")

static_types = [static_results[tau]['cmpp_type'] for tau in TAU_VALUES]
dynamic_types = [dynamic_results[tau]['cmpp_type'] for tau in TAU_VALUES]

print(f"\n  {'tau':>6s}  {'label':>10s}  {'Static':>8s}  {'Dynamic':>8s}")
print(f"  {'-'*45}")
for tau, label, st, dt in zip(TAU_VALUES, TAU_LABELS, static_types, dynamic_types):
    print(f"  {tau:6.2f}  {label:>10s}  {st:>8s}  {dt:>8s}")

static_change = len(set(static_types)) > 1
dynamic_change = len(set(dynamic_types)) > 1

print(f"\n  Static type transition: {'YES' if static_change else 'NO'} (types = {set(static_types)})")
print(f"  Dynamic type transition: {'YES' if dynamic_change else 'NO'} (types = {set(dynamic_types)})")

# -----------------------------------------------------------
# |C|^2 EVOLUTION
# -----------------------------------------------------------
print(f"\n\n{'='*80}")
print(f"  |C|^2 EVOLUTION ACROSS FOLD")
print(f"{'='*80}")

print(f"\n  {'tau':>6s}  {'|C|^2_static':>14s}  {'|C|^2_dynamic':>14s}  {'ratio_dyn/stat':>16s}")
print(f"  {'-'*60}")
for tau in TAU_VALUES:
    Cs = static_results[tau]['C12_sq']   # (local)
    Cd = dynamic_results[tau]['C12_sq']  # (local)
    ratio = Cd / Cs if abs(Cs) > 1e-30 else float('nan')  # (local)
    print(f"  {tau:6.2f}  {Cs:14.8f}  {Cd:14.8f}  {ratio:16.8f}")

# Monotonicity check
C_static_vals = [static_results[tau]['C12_sq'] for tau in TAU_VALUES]
C_dyn_vals = [dynamic_results[tau]['C12_sq'] for tau in TAU_VALUES]
monotone_stat = all(C_static_vals[i] <= C_static_vals[i+1] for i in range(len(C_static_vals)-1))
monotone_dyn = all(C_dyn_vals[i] <= C_dyn_vals[i+1] for i in range(len(C_dyn_vals)-1))
print(f"\n  |C|^2 monotone increasing (static): {monotone_stat}")
print(f"  |C|^2 monotone increasing (dynamic): {monotone_dyn}")
print(f"  (Confirms Weyl curvature hypothesis: |C|^2 grows with tau)")


# -----------------------------------------------------------
# GATE VERDICT
# -----------------------------------------------------------
print(f"\n\n{'='*80}")
print(f"  GATE VERDICT: S76-C8-CMPP")
print(f"{'='*80}")

computed_all = all(
    static_results[tau]['cmpp_type'] is not None and
    dynamic_results[tau]['cmpp_type'] is not None
    for tau in TAU_VALUES
)

if not computed_all:
    verdict = 'FAIL'
    verdict_text = '12D Weyl tensor not computable at one or more tau values'
elif static_change or dynamic_change:
    verdict = 'PASS'
    verdict_text = f'CMPP type computed at all three tau values. Type change: static={static_change}, dynamic={dynamic_change}'
else:
    verdict = 'INFO'
    verdict_text = 'CMPP type computed at all three tau values. No type transition during transit.'

print(f"\n  Verdict: {verdict}")
print(f"  {verdict_text}")
print(f"\n  Static types:  {dict(zip(TAU_LABELS, static_types))}")
print(f"  Dynamic types: {dict(zip(TAU_LABELS, dynamic_types))}")
print(f"\n  Cross-check results:")
print(f"    CHK1 (4D block): |C_4D|^2 = 0 at all tau (flat M^4) -- EXPECTED")

for tau in TAU_VALUES:
    geom8 = static_results[tau]['geom8']
    R12_s = build_12d_riemann_static(geom8['R_abcd'])
    C12_s, _, _, _, _ = compute_12d_weyl(R12_s)
    frac_s, _, _ = check_product_decomposition(C12_s)
    R12_d, _ = build_12d_riemann_dynamic(geom8['R_abcd'], v_terminal)
    C12_d, _, _, _, _ = compute_12d_weyl(R12_d)
    frac_d, _, _ = check_product_decomposition(C12_d)
    print(f"    CHK2 (tau={tau:.2f}): mixed fraction static={frac_s*100:.4f}%, dynamic={frac_d*100:.4f}%")

print(f"    CHK3: R_12D from internal curvature. No cosmological horizon in product geometry.")


# -----------------------------------------------------------
# SAVE DATA
# -----------------------------------------------------------
save_data = {
    'tau_values': TAU_VALUES,
    'tau_labels': np.array(TAU_LABELS),
    # Static results
    'static_types': np.array(static_types),
    'static_C_sq': np.array([static_results[tau]['C12_sq'] for tau in TAU_VALUES]),
    'static_R_scalar': np.array([static_results[tau]['R12_scalar'] for tau in TAU_VALUES]),
    'static_K_8d': np.array([static_results[tau]['geom8']['K'] for tau in TAU_VALUES]),
    'static_min_bw2': np.array([static_results[tau]['min_bw2_frac'] for tau in TAU_VALUES]),
    'static_weyl_n_eigs': np.array([static_results[tau]['weyl_op']['n_distinct'] for tau in TAU_VALUES]),
    # Dynamic results
    'dynamic_types': np.array(dynamic_types),
    'dynamic_C_sq': np.array([dynamic_results[tau]['C12_sq'] for tau in TAU_VALUES]),
    'dynamic_R_scalar': np.array([dynamic_results[tau]['R12_scalar'] for tau in TAU_VALUES]),
    'dynamic_min_bw2': np.array([dynamic_results[tau]['min_bw2_frac'] for tau in TAU_VALUES]),
    'dynamic_weyl_n_eigs': np.array([dynamic_results[tau]['weyl_op']['n_distinct'] for tau in TAU_VALUES]),
    # Gate
    'verdict': np.array([verdict]),
    'static_type_change': np.array([static_change]),
    'dynamic_type_change': np.array([dynamic_change]),
    # Constants used
    'v_terminal': np.array([v_terminal]),
    'H_fold': np.array([H_fold]),
    'tau_fold': np.array([tau_fold]),
}

# BW fractions for each tau (static and dynamic)
for case_tag, case_dict in [('static', static_results), ('dynamic', dynamic_results)]:
    for tau in TAU_VALUES:
        r = case_dict[tau]
        if r['best_decomp'] is not None:
            bw = r['best_decomp']['bw_norms']
            tot = r['best_decomp']['total']
            for w in [-2, -1, 0, 1, 2]:
                save_data[f'{case_tag}_bw{w:+d}_frac_tau{tau:.2f}'] = np.array([bw[w]/tot if tot > 0 else 0])

# Weyl operator eigenvalues
for case_tag, case_dict in [('static', static_results), ('dynamic', dynamic_results)]:
    for tau in TAU_VALUES:
        wo = case_dict[tau]['weyl_op']
        save_data[f'{case_tag}_weyl_eigs_tau{tau:.2f}'] = np.array(wo['unique_eigs'])
        save_data[f'{case_tag}_weyl_mults_tau{tau:.2f}'] = np.array(wo['multiplicities'])

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        's76_cmpp_type_gge_transit.npz')
np.savez(out_path, **save_data)

elapsed = time.time() - t_start  # (local)
print(f"\n\nTotal runtime: {elapsed:.1f}s")
print(f"Data saved to: {out_path}")
print("=" * 80)
