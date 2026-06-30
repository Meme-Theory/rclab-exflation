#!/usr/bin/env python3
"""
S77 CMPP-TURNAROUND: Static CMPP Type at tau = 1.614 (Overshoot)
================================================================

Computes the CMPP algebraic classification of the 12D Weyl tensor at the
modulus overshoot point tau = 1.614, where S73B ODE shows the modulus
reaches its maximum excursion before returning.

Comparison points:
  tau = 0.00  (round metric)
  tau = 0.19  (fold, S76 reference)
  tau = 1.614 (overshoot turnaround)

Both static (product M^{3,1} x K^8) and dynamic (tau_dot = v_terminal)
cases computed, following S76 protocol exactly.

CMPP classification hierarchy (most special to most general):
  O < N < III < D < II < I < G

Prior results (S76 memory):
  Static: EXACT Type D at tau = {0.10, 0.19, 0.30}
  Dynamic: Type G at tau = {0.10, 0.19, 0.30}
  No type transition across fold

Gate: S77-C1-CMPP-TURN (INFO)
  Report CMPP type at tau = 1.614.
  Type D or II would be structurally significant.

Author: schwarzschild-penrose-geometer (Session 77)
Date: 2026-04-13
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

# Tau values: round metric, fold, overshoot
TAU_OVERSHOOT = 1.614  # (local) S73B W1-D modulus overshoot maximum
TAU_VALUES = np.array([0.00, tau_fold, TAU_OVERSHOOT])  # (local)
TAU_LABELS = ['round', 'fold', 'overshoot']  # (local)


# =============================================================================
# SECTION 1: 8D Internal Curvature (from S76, proven)
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
# SECTION 2: 12D Riemann and Weyl (from S76)
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
# SECTION 3: Null Frame and BW Decomposition (from S76)
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
# SECTION 4: WAND Search (from S76)
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
# SECTION 6: CMPP Invariants I, J and Type D Test
# =============================================================================

def compute_cmpp_invariants(C12):
    """Compute CMPP invariants I and J for the 12D Weyl tensor.

    I = C_{ABCD} C^{ABCD}
    J = C_{AB}^{  CD} C_{CD}^{  EF} C_{EF}^{  AB}

    Type D criterion: 27 J^2 = I^3  (algebraically special)
    """
    n = DIM_TOTAL  # (local)
    eta = np.diag(np.array([-1.0] + [1.0] * (n - 1)))  # (local)
    eta_diag = np.diag(eta)  # (local)

    # Raise indices: C^{ABCD} = eta^{AA'} eta^{BB'} eta^{CC'} eta^{DD'} C_{A'B'C'D'}
    sign_tensor = np.einsum('A,B,C,D->ABCD', eta_diag, eta_diag, eta_diag, eta_diag)  # (local)
    C_up = sign_tensor * C12  # (local) C^{ABCD}

    # I = C_{ABCD} C^{ABCD}
    I_inv = float(np.sum(C12 * C_up))  # (local)

    # J = C_{AB}^{  CD} C_{CD}^{  EF} C_{EF}^{  AB}
    # First: C_{AB}^{  CD} = eta^{CC'} eta^{DD'} C_{ABC'D'}
    C_mixed = np.einsum('C,D,ABCD->ABCD', eta_diag, eta_diag, C12)  # (local)

    # J = C_{AB}^{CD} * C_{CD}^{EF} * C_{EF}^{AB}
    # = sum over all indices
    temp = np.einsum('ABCD,CDEF->ABEF', C_mixed, C_mixed)  # (local)
    J_inv = float(np.einsum('ABEF,EFAB->', temp, C_mixed))  # (local)

    # Type D criterion: 27 J^2 = I^3
    lhs = 27.0 * J_inv**2  # (local)
    rhs = I_inv**3          # (local)
    deviation = abs(lhs - rhs) / (abs(rhs) + 1e-30)  # (local) relative deviation

    return {
        'I': I_inv, 'J': J_inv,
        '27J2': lhs, 'I3': rhs,
        'type_D_deviation': deviation,
        'is_type_D': deviation < 1e-6,
    }


# =============================================================================
# SECTION 7: Cross-Check Functions
# =============================================================================

def check_weyl_tracefree(C12):
    """Verify Weyl tensor is tracefree: C^B_{ABC} = 0."""
    eta_diag = np.diag(np.diag(np.array([[-1.0] + [1.0]*11])))  # (local)
    eta_diag = np.array([-1.0] + [1.0]*11)  # (local)
    trace = np.einsum('B,ABCB->AC', eta_diag, C12)  # (local)
    return float(np.max(np.abs(trace)))


def check_product_decomposition(C12):
    """Check mixed Weyl fraction for product geometry."""
    mixed_norm = 0.0  # (local)
    total_norm = 0.0  # (local)
    for A in range(DIM_TOTAL):
        for B in range(DIM_TOTAL):
            for C in range(DIM_TOTAL):
                for D in range(DIM_TOTAL):
                    val2 = C12[A, B, C, D]**2  # (local)
                    total_norm += val2
                    n_ext = sum(1 for x in [A,B,C,D] if x < 4)  # (local)
                    if n_ext not in [0, 4]:
                        mixed_norm += val2
    frac_mixed = mixed_norm / total_norm if total_norm > 0 else 0.0  # (local)
    return frac_mixed, mixed_norm, total_norm


# =============================================================================
# SECTION 8: MAIN COMPUTATION
# =============================================================================

print("=" * 80)
print("  S77 CMPP-TURNAROUND: Algebraic Type at Modulus Overshoot tau = 1.614")
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
# Print Jensen metric at overshoot for reference
# -----------------------------------------------------------
print(f"\n  Jensen metric eigenvalues at tau = {TAU_OVERSHOOT}:")
g_over = jensen_metric(B_ab, TAU_OVERSHOOT)  # (local)
g_diag = np.diag(g_over)  # (local)
print(f"    SU(2) scales: {g_diag[SU2_IDX]}")
print(f"    C^2 scales:   {g_diag[C2_IDX]}")
print(f"    U(1) scales:  {g_diag[U1_IDX]}")
cond_num = np.max(g_diag) / np.min(g_diag)  # (local)
print(f"    Condition number: {cond_num:.2f}")
print(f"    (For reference: cond at fold = {np.exp(4*tau_fold):.2f})")

# -----------------------------------------------------------
# CASE (a): STATIC PRODUCT M^{3,1} x K^8
# -----------------------------------------------------------
print(f"\n{'='*80}")
print(f"  CASE (a): STATIC PRODUCT  M^{{3,1}} x (SU(3), g_tau)")
print(f"{'='*80}")

print(f"\n{'tau':>8s}  {'label':>10s}  {'CMPP':>6s}  {'bw+2%':>9s}  {'bw+1%':>9s}  "
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
    cmpp_inv = compute_cmpp_invariants(C12)

    dt = time.time() - t0  # (local)

    static_results[tau] = {
        'geom8': geom8, 'R12_scalar': R12_scal, 'C12_sq': C12_sq,
        'trace_err': tr_err, 'cmpp_type': cmpp_type,
        'best_decomp': best_decomp, 'best_params': best_params,
        'n_tested': n_tested, 'weyl_op': weyl_op,
        'all_types': all_types, 'min_bw2_frac': min_bw2, 'time': dt,
        'cmpp_inv': cmpp_inv,
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
    cmpp_inv = compute_cmpp_invariants(C12_dyn)

    dt = time.time() - t0  # (local)

    dynamic_results[tau] = {
        'geom8': geom8, 'K_diag': K_diag,
        'R12_scalar': R12s_dyn, 'C12_sq': C12sq_dyn,
        'trace_err': tr_err_dyn, 'cmpp_type': cmpp_type,
        'best_decomp': best_decomp, 'best_params': best_params,
        'n_tested': n_tested, 'weyl_op': weyl_op,
        'all_types': all_types, 'min_bw2_frac': min_bw2, 'time': dt,
        'cmpp_inv': cmpp_inv,
    }

    if best_decomp is not None:
        bw = best_decomp['bw_norms']
        tot = best_decomp['total']
        fracs = {k: v/tot*100 for k,v in bw.items()} if tot > 0 else {k:0 for k in bw}  # (local)
        print(f"{tau:8.4f}  {label:>10s}  {cmpp_type:>6s}  {fracs[+2]:9.4f}  {fracs[+1]:9.4f}  "
              f"{fracs[0]:9.4f}  {fracs[-1]:9.4f}  {fracs[-2]:9.4f}  "
              f"{C12sq_dyn:12.6f}  {n_tested:6d}  {dt:5.1f}s")


# -----------------------------------------------------------
# CMPP INVARIANTS ANALYSIS
# -----------------------------------------------------------
print(f"\n\n{'='*80}")
print(f"  CMPP INVARIANTS (I, J, Type-D Test: 27J^2 = I^3)")
print(f"{'='*80}")

for case_name, case_results in [('STATIC', static_results), ('DYNAMIC', dynamic_results)]:
    print(f"\n  --- {case_name} ---")
    print(f"  {'tau':>8s}  {'label':>10s}  {'I':>14s}  {'J':>14s}  {'27J^2':>14s}  {'I^3':>14s}  {'dev':>12s}  {'TypeD?':>6s}")
    print(f"  {'-'*90}")
    for tau, label in zip(TAU_VALUES, TAU_LABELS):
        inv = case_results[tau]['cmpp_inv']
        print(f"  {tau:8.4f}  {label:>10s}  {inv['I']:14.6e}  {inv['J']:14.6e}  "
              f"{inv['27J2']:14.6e}  {inv['I3']:14.6e}  {inv['type_D_deviation']:12.6e}  "
              f"{'YES' if inv['is_type_D'] else 'NO':>6s}")


# -----------------------------------------------------------
# CROSS-CHECKS
# -----------------------------------------------------------
print(f"\n\n{'='*80}")
print(f"  CROSS-CHECKS")
print(f"{'='*80}")

print("\n--- CHK1: Weyl tracefree (max |C^B_ABC|) ---")
for tau, label in zip(TAU_VALUES, TAU_LABELS):
    geom8 = static_results[tau]['geom8']
    R12_s = build_12d_riemann_static(geom8['R_abcd'])
    C12_s, _, _, _, _ = compute_12d_weyl(R12_s)
    tr = static_results[tau]['trace_err']  # (local)
    print(f"  tau={tau:.3f} ({label:>10s}): trace_err = {tr:.2e}")

print("\n--- CHK2: Product decomposition (mixed Weyl fraction) ---")
for tau, label in zip(TAU_VALUES, TAU_LABELS):
    geom8 = static_results[tau]['geom8']
    R12_s = build_12d_riemann_static(geom8['R_abcd'])
    C12_s, _, _, _, _ = compute_12d_weyl(R12_s)
    frac_s, mixed_s, total_s = check_product_decomposition(C12_s)
    R12_d, _ = build_12d_riemann_dynamic(geom8['R_abcd'], v_terminal)
    C12_d, _, _, _, _ = compute_12d_weyl(R12_d)
    frac_d, mixed_d, total_d = check_product_decomposition(C12_d)
    print(f"  tau={tau:.3f} ({label:>10s}): static mixed = {frac_s*100:.4f}% | dynamic mixed = {frac_d*100:.4f}%")


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
        print(f"\n  tau = {tau:.3f} ({label})")
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
print(f"  TYPE TRANSITION CHECK (round -> fold -> overshoot)")
print(f"{'='*80}")

static_types = [static_results[tau]['cmpp_type'] for tau in TAU_VALUES]
dynamic_types = [dynamic_results[tau]['cmpp_type'] for tau in TAU_VALUES]

print(f"\n  {'tau':>6s}  {'label':>10s}  {'Static':>8s}  {'Dynamic':>8s}")
print(f"  {'-'*45}")
for tau, label, st, dtt in zip(TAU_VALUES, TAU_LABELS, static_types, dynamic_types):
    print(f"  {tau:6.3f}  {label:>10s}  {st:>8s}  {dtt:>8s}")

static_change = len(set(static_types)) > 1
dynamic_change = len(set(dynamic_types)) > 1

print(f"\n  Static type transition: {'YES' if static_change else 'NO'} (types = {set(static_types)})")
print(f"  Dynamic type transition: {'YES' if dynamic_change else 'NO'} (types = {set(dynamic_types)})")


# -----------------------------------------------------------
# |C|^2 EVOLUTION
# -----------------------------------------------------------
print(f"\n\n{'='*80}")
print(f"  |C|^2 EVOLUTION (round -> fold -> overshoot)")
print(f"{'='*80}")

print(f"\n  {'tau':>8s}  {'|C|^2_static':>14s}  {'|C|^2_dynamic':>14s}  {'ratio_dyn/stat':>16s}  {'K_8D':>12s}  {'R_8D':>12s}")
print(f"  {'-'*80}")
for tau in TAU_VALUES:
    Cs = static_results[tau]['C12_sq']   # (local)
    Cd = dynamic_results[tau]['C12_sq']  # (local)
    K8 = static_results[tau]['geom8']['K']  # (local)
    R8 = static_results[tau]['geom8']['R_scalar']  # (local)
    ratio = Cd / Cs if abs(Cs) > 1e-30 else float('nan')  # (local)
    print(f"  {tau:8.4f}  {Cs:14.8f}  {Cd:14.8f}  {ratio:16.8f}  {K8:12.6f}  {R8:12.6f}")

# Monotonicity check
C_static_vals = [static_results[tau]['C12_sq'] for tau in TAU_VALUES]
C_dyn_vals = [dynamic_results[tau]['C12_sq'] for tau in TAU_VALUES]
monotone_stat = all(C_static_vals[i] <= C_static_vals[i+1] for i in range(len(C_static_vals)-1))
monotone_dyn = all(C_dyn_vals[i] <= C_dyn_vals[i+1] for i in range(len(C_dyn_vals)-1))
print(f"\n  |C|^2 monotone increasing (static): {monotone_stat}")
print(f"  |C|^2 monotone increasing (dynamic): {monotone_dyn}")
print(f"  (Weyl curvature hypothesis: |C|^2 should grow with tau)")

# Growth factor
growth_fold = C_static_vals[1] / C_static_vals[0] if C_static_vals[0] > 1e-30 else float('nan')  # (local)
growth_over = C_static_vals[2] / C_static_vals[0] if C_static_vals[0] > 1e-30 else float('nan')  # (local)
print(f"  |C|^2 growth: fold/round = {growth_fold:.4f}, overshoot/round = {growth_over:.4f}")


# -----------------------------------------------------------
# GATE VERDICT
# -----------------------------------------------------------
print(f"\n\n{'='*80}")
print(f"  GATE VERDICT: S77-C1-CMPP-TURN")
print(f"{'='*80}")

computed_all = all(
    static_results[tau]['cmpp_type'] is not None and
    dynamic_results[tau]['cmpp_type'] is not None
    for tau in TAU_VALUES
)

overshoot_static_type = static_results[TAU_OVERSHOOT]['cmpp_type']  # (local)
overshoot_dynamic_type = dynamic_results[TAU_OVERSHOOT]['cmpp_type']  # (local)
fold_static_type = static_results[tau_fold]['cmpp_type']  # (local)
fold_dynamic_type = dynamic_results[tau_fold]['cmpp_type']  # (local)

verdict = 'INFO'  # (local)
verdict_text = (  # (local)
    f'CMPP type computed at all tau values. '
    f'Static: {overshoot_static_type} at overshoot (vs {fold_static_type} at fold). '
    f'Dynamic: {overshoot_dynamic_type} at overshoot (vs {fold_dynamic_type} at fold). '
    f'Type transition: static={static_change}, dynamic={dynamic_change}.'
)

print(f"\n  Verdict: {verdict}")
print(f"  {verdict_text}")
print(f"\n  Static types:  {dict(zip(TAU_LABELS, static_types))}")
print(f"  Dynamic types: {dict(zip(TAU_LABELS, dynamic_types))}")

# Type D significance
inv_over_s = static_results[TAU_OVERSHOOT]['cmpp_inv']  # (local)
inv_over_d = dynamic_results[TAU_OVERSHOOT]['cmpp_inv']  # (local)
print(f"\n  Type D test at overshoot:")
print(f"    Static:  27J^2/I^3 deviation = {inv_over_s['type_D_deviation']:.6e} -> {'Type D CONFIRMED' if inv_over_s['is_type_D'] else 'Not Type D'}")
print(f"    Dynamic: 27J^2/I^3 deviation = {inv_over_d['type_D_deviation']:.6e} -> {'Type D CONFIRMED' if inv_over_d['is_type_D'] else 'Not Type D'}")

print(f"\n  Cross-checks:")
for tau, label in zip(TAU_VALUES, TAU_LABELS):
    print(f"    tau={tau:.3f} ({label}): trace_err(static)={static_results[tau]['trace_err']:.2e}, "
          f"trace_err(dyn)={dynamic_results[tau]['trace_err']:.2e}")


# -----------------------------------------------------------
# SAVE DATA
# -----------------------------------------------------------
save_data = {
    'tau_values': TAU_VALUES,
    'tau_labels': np.array(TAU_LABELS),
    'tau_overshoot': np.array([TAU_OVERSHOOT]),
    # Static results
    'static_types': np.array(static_types),
    'static_C_sq': np.array([static_results[tau]['C12_sq'] for tau in TAU_VALUES]),
    'static_R_scalar': np.array([static_results[tau]['R12_scalar'] for tau in TAU_VALUES]),
    'static_K_8d': np.array([static_results[tau]['geom8']['K'] for tau in TAU_VALUES]),
    'static_Ric_sq': np.array([static_results[tau]['geom8']['Ric_sq'] for tau in TAU_VALUES]),
    'static_R_8d': np.array([static_results[tau]['geom8']['R_scalar'] for tau in TAU_VALUES]),
    'static_min_bw2': np.array([static_results[tau]['min_bw2_frac'] for tau in TAU_VALUES]),
    'static_weyl_n_eigs': np.array([static_results[tau]['weyl_op']['n_distinct'] for tau in TAU_VALUES]),
    # Dynamic results
    'dynamic_types': np.array(dynamic_types),
    'dynamic_C_sq': np.array([dynamic_results[tau]['C12_sq'] for tau in TAU_VALUES]),
    'dynamic_R_scalar': np.array([dynamic_results[tau]['R12_scalar'] for tau in TAU_VALUES]),
    'dynamic_min_bw2': np.array([dynamic_results[tau]['min_bw2_frac'] for tau in TAU_VALUES]),
    'dynamic_weyl_n_eigs': np.array([dynamic_results[tau]['weyl_op']['n_distinct'] for tau in TAU_VALUES]),
    # CMPP invariants
    'static_I': np.array([static_results[tau]['cmpp_inv']['I'] for tau in TAU_VALUES]),
    'static_J': np.array([static_results[tau]['cmpp_inv']['J'] for tau in TAU_VALUES]),
    'static_typeD_dev': np.array([static_results[tau]['cmpp_inv']['type_D_deviation'] for tau in TAU_VALUES]),
    'dynamic_I': np.array([dynamic_results[tau]['cmpp_inv']['I'] for tau in TAU_VALUES]),
    'dynamic_J': np.array([dynamic_results[tau]['cmpp_inv']['J'] for tau in TAU_VALUES]),
    'dynamic_typeD_dev': np.array([dynamic_results[tau]['cmpp_inv']['type_D_deviation'] for tau in TAU_VALUES]),
    # Gate
    'verdict': np.array([verdict]),
    'static_type_change': np.array([static_change]),
    'dynamic_type_change': np.array([dynamic_change]),
    # Constants used
    'v_terminal': np.array([v_terminal]),
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
                save_data[f'{case_tag}_bw{w:+d}_frac_tau{tau:.3f}'] = np.array([bw[w]/tot if tot > 0 else 0])

# Weyl operator eigenvalues
for case_tag, case_dict in [('static', static_results), ('dynamic', dynamic_results)]:
    for tau in TAU_VALUES:
        wo = case_dict[tau]['weyl_op']
        save_data[f'{case_tag}_weyl_eigs_tau{tau:.3f}'] = np.array(wo['unique_eigs'])
        save_data[f'{case_tag}_weyl_mults_tau{tau:.3f}'] = np.array(wo['multiplicities'])

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        's77_cmpp_turnaround.npz')
np.savez(out_path, **save_data)

elapsed = time.time() - t_start  # (local)
print(f"\n\nTotal runtime: {elapsed:.1f}s")
print(f"Data saved to: {out_path}")
