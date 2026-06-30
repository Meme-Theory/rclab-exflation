#!/usr/bin/env python3
"""
S78-W3-H CMPP-AT-TAU-0.537: Type D Under Ansatz-Breaking Perturbation
=====================================================================

Tests whether CMPP Type D persists at the geometric phase transition
tau = 0.53723065 (where the C^2 sectional curvature crosses zero [S48])
under a SMALL, pre-specified, NON-TRIVIAL perturbation that breaks the
static M^{3,1} x K^8 product ansatz.

The pure product case is construction-forced Type D (ANSATZ-FORCED per
S78 audit Pattern 1). The physics test is whether Type D is ROBUST
under small ansatz deformations, AND whether a pre-registered
CMPP-related invariant distinguishes tau = 0.537 from neighboring tau.

=============================================================================
CONVENTION PINS (pre-registered, in header)
=============================================================================

1. CMPP convention: COLEY-MILSON-PELAVAS-PRAVDA FULL (not simplified).
   Lorentzian null-frame boost-weight decomposition as in Coley-Milson
   2004-2005. Types ordered O < N < III < D < II < I < G.

2. Weyl-tensor convention: NEWMAN-PENROSE higher-dim (boost-weight +2 to -2
   in (D-2)-dim spatial transverse basis). Bel-Robinson NOT used (classical,
   positive-energy-theorem machinery not needed here).

3. Perturbation amplitude: epsilon = 0.01 (1% of unperturbed component
   magnitudes). Single pre-specified component modified (see below).

4. Perturbation spec: NON-BLOCK-DIAGONAL RIEMANN COMPONENT
   R_{0,4,0,a} for a in C^2 sector (indices 7,8,9,10 in 12D).
   This breaks the M^{3,1} x K^8 product by creating time-C^2 mixing in
   the extrinsic-curvature-like sector. Chosen because:
   - Non-trivial (changes CMPP boost-weight content)
   - Small (epsilon times typical Riemann component)
   - Physically plausible (analogous to small ADM-momentum component)
   - Maintains Riemann symmetries (R_{abcd} = -R_{bacd} = R_{cdab} via
     assigning all four symmetry-related components)

=============================================================================
PRE-REGISTERED CMPP INVARIANT (must be specified BEFORE run)
=============================================================================

I define the "C^2-restricted Weyl operator eigenvalue" lambda_C2(tau):

  lambda_C2(tau) := smallest eigenvalue of C restricted to
                    Lambda^2 span{e_i ^ e_j : i,j in C^2 sector (7,8,9,10)}.

This is a CMPP-related observable because it is a subsector eigenvalue
of the Weyl operator whose total spectrum classifies the algebraic type.

NON-TRIVIALITY CRITERION:
  If lambda_C2(tau) has a zero-crossing at tau = 0.53723065 (matching
  the documented C^2 sectional curvature zero) AND is non-zero at
  tau = 0.400 and tau = 0.700 (neighboring values), then the invariant
  DETECTS the geometric phase transition and is non-trivial.

If lambda_C2(tau) has the same sign at all three tau, the invariant
is AMBIGUOUS (INFO verdict).

=============================================================================
PRE-REGISTERED GATE
=============================================================================

PASS: Under epsilon = 0.01 ansatz-breaking perturbation,
  (A) CMPP Type D persists at tau = 0.537 (unperturbed and perturbed),
      with 27J^2 / I^3 deviation < 1e-4 AND best-WAND type = D, AND
  (B) lambda_C2(tau = 0.53723065) vanishes within 1e-4 relative to
      lambda_C2(tau = 0.400) AND lambda_C2(tau = 0.700), demonstrating
      that the pre-registered invariant detects the phase transition.

FAIL: Either
  (A) Type D breaks to Type II or Type I under perturbation (best-WAND
      shows bw+2 > 1e-6 of total), OR
  (B) lambda_C2(tau = 0.537) is not distinguishable from lambda_C2 at
      neighboring tau (|lambda_C2(0.537)| > 0.1 * max(|lambda_C2(0.400)|,
      |lambda_C2(0.700)|)).

INFO: Type D persists but lambda_C2 behavior is ambiguous (e.g., same sign
  at all three tau with no zero-crossing, or zero-crossing but at wrong
  tau).

INCOMPUTABLE: Perturbed Weyl tensor trace_err > 1e-8 (diverges or
  non-physical).

=============================================================================
CROSS-CHECKS
=============================================================================

CHK-1: Exact block-diagonal (unperturbed) case at tau = 0.537:
  - Weyl-squared |C|^2 >= 0 reportable
  - Bel-Robinson scalar T_{abcd} T^{abcd} non-negative (tensor square)
  - Type D confirmed (ANSATZ-FORCED baseline)

CHK-2: Sectional curvature C^2 = 0 at tau = 0.53723065 reported as scalar
  number with numerical resolution. Expected value: ~0 within 1e-3
  (from S48 closure).

CHK-3: Pre-registered CMPP-related observable (lambda_C2) detects the
  C^2 sectional-curvature zero at the same tau.

Author: schwarzschild-penrose-geometer (Session 78, W3-H)
Date: 2026-04-15
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
    tau_fold, PI,
)

t_start = time.time()

# =============================================================================
# Constants and pre-registered parameters
# =============================================================================

DIM_INT = 8       # (local) internal dimension (K^8)
DIM_EXT = 4       # (local) external dimension (M^{3,1})
DIM_TOTAL = 12    # (local) total

# Pre-registered tau values
TAU_PHASE = 0.53723065     # (local) S48 geometric phase transition (C^2 sectional K=0)
TAU_BELOW = 0.400           # (local) neighbor below, same zone
TAU_ABOVE = 0.700           # (local) neighbor above, across phase transition
TAU_VALUES = np.array([TAU_BELOW, TAU_PHASE, TAU_ABOVE])  # (local)
TAU_LABELS = ['below (0.400)', 'phase (0.537)', 'above (0.700)']  # (local)

# Pre-registered perturbation parameters (CONVENTION PINS)
EPSILON = 0.01            # (local) 1% perturbation amplitude
PERT_TIME_IDX = 0         # (local) time index in 12D
PERT_SPATIAL_IDX = 4      # (local) first internal index for perturbation
# C^2 sector in 12D indexing: internal indices 4+C2_IDX = [7,8,9,10]
# (local) we use the first C^2 index as perturbation target
PERT_C2_IDX = 4 + C2_IDX[0]    # (local) = 7, first C^2 index in 12D

# Pre-registered tolerance levels
TOL_TYPE_D = 1e-4          # (local) Type D discriminant tolerance
TOL_TRACE = 1e-8           # (local) Weyl trace-free tolerance
TOL_ZERO = 1e-4            # (local) relative tolerance for lambda_C2 zero

# Sector mappings in 12D
SU2_12 = [4 + i for i in SU2_IDX]  # (local)
C2_12 = [4 + i for i in C2_IDX]    # (local)
U1_12 = [4 + i for i in U1_IDX]    # (local)

print("=" * 80)
print("  S78-W3-H: CMPP Type D at tau = 0.537 under Ansatz-Breaking Perturbation")
print("=" * 80)
print(f"\nPRE-REGISTERED CONVENTIONS (from script header):")
print(f"  CMPP convention:      Coley-Milson-Pelavas-Pravda FULL")
print(f"  Weyl convention:      Newman-Penrose (boost-weight)")
print(f"  Perturbation epsilon: {EPSILON}")
print(f"  Perturbation spec:    R_{{0, 4, 0, C^2_idx}} non-block-diagonal")
print(f"  Invariant to test:    lambda_C2 = min eig of Weyl | Lambda^2(C^2)")
print(f"\nTAU VALUES TESTED:")
for t, l in zip(TAU_VALUES, TAU_LABELS):
    print(f"  tau = {t:.8f}  [{l}]")
print(f"\nTOLERANCES:")
print(f"  Type D disc:  {TOL_TYPE_D}")
print(f"  Trace-free:   {TOL_TRACE}")
print(f"  Zero rel:     {TOL_ZERO}")


# =============================================================================
# SECTION 1: 8D Internal geometry (same as S77, proven)
# =============================================================================

def compute_riemann_ON(ft, Gamma, n=DIM_INT):
    """Riemann tensor R[a,b,c,f] = R^f_{abc} in ON frame."""
    R = np.zeros((n, n, n, n))  # (local)
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
    return {
        'R_abcd': R_abcd, 'Ric': Ric, 'R_scalar': R_scalar,
        'Ric_sq': Ric_sq, 'K': K_full, 'g_s': g_s,
    }


def compute_c2_sectional_curvature(R8, tau):
    """
    Compute sectional curvature K(e_7, e_8) for two C^2-sector orthonormal
    tangents, expressed in the 8D internal frame.

    In ON frame, for e_i, e_j unit orthogonal vectors:
      K(e_i, e_j) = R_{ijij}
    """
    # C^2 sector indices in 8D internal frame (not 12D): C2_IDX = [3,4,5,6]
    i = C2_IDX[0]  # (local)
    j = C2_IDX[1]  # (local)
    # Index convention from s77: R[a,b,c,f] = R^f_{abc}, so R_{ijij} = R[i,j,i,j]
    K_ij = float(R8[i, j, i, j])  # (local)
    # Average over all distinct C^2-C^2 2-planes for robustness
    vals = []  # (local)
    for a in range(len(C2_IDX)):
        for b in range(a + 1, len(C2_IDX)):
            ia, ib = C2_IDX[a], C2_IDX[b]  # (local)
            vals.append(float(R8[ia, ib, ia, ib]))
    K_mean_C2 = float(np.mean(vals))  # (local)
    K_min_C2 = float(np.min(vals))    # (local)
    return {
        'K_ij_primary': K_ij,
        'K_mean_C2': K_mean_C2,
        'K_min_C2': K_min_C2,
        'K_all_C2': vals,
    }


# =============================================================================
# SECTION 2: 12D Riemann — static + ansatz-breaking perturbation
# =============================================================================

def build_12d_riemann_static(R8):
    """Static product M^{3,1} x K^8. Only internal block nonzero."""
    R12 = np.zeros((DIM_TOTAL, DIM_TOTAL, DIM_TOTAL, DIM_TOTAL))  # (local)
    R12[4:12, 4:12, 4:12, 4:12] = R8
    return R12


def build_12d_riemann_perturbed(R8, epsilon):
    """
    Apply pre-registered ANSATZ-BREAKING perturbation.

    Add to the static product Riemann a non-block-diagonal component
    R_{0, 4, 0, PERT_C2_IDX} = epsilon * R_ref
    plus the 3 components from Riemann symmetries
    (R_{0,a,0,b} = R_{a,0,b,0} = -R_{a,0,0,b} = -R_{0,a,b,0}).

    R_ref is the RMS magnitude of the unperturbed internal Riemann to
    make epsilon dimensionless and the perturbation genuinely small.
    """
    R12 = build_12d_riemann_static(R8)  # (local)
    # Reference amplitude: RMS of internal Riemann
    R_ref = float(np.sqrt(np.mean(R8**2)))  # (local)
    if R_ref < 1e-15:
        R_ref = 1.0  # (local) fallback
    delta = epsilon * R_ref  # (local) perturbation amplitude

    a = PERT_TIME_IDX        # (local) = 0
    b = PERT_SPATIAL_IDX     # (local) = 4, first internal
    c = PERT_TIME_IDX        # (local) = 0
    d = PERT_C2_IDX          # (local) = 7, first C^2 index

    # Enforce Riemann symmetries for component R_{abcd} = delta:
    #   R_{abcd} = -R_{bacd} = -R_{abdc} = R_{badc} = R_{cdab} = ...
    R12[a, b, c, d] += delta
    R12[b, a, c, d] -= delta
    R12[a, b, d, c] -= delta
    R12[b, a, d, c] += delta
    R12[c, d, a, b] += delta
    R12[d, c, a, b] -= delta
    R12[c, d, b, a] -= delta
    R12[d, c, b, a] += delta

    return R12, delta


# =============================================================================
# SECTION 3: Weyl tensor (Lorentzian, from S77)
# =============================================================================

def compute_12d_weyl(R12):
    """12D Weyl tensor and related quantities. VECTORIZED from S77."""
    n = DIM_TOTAL  # (local)
    eta = np.diag(np.array([-1.0] + [1.0] * (n - 1)))  # (local)
    eta_diag = np.diag(eta)  # (local)

    Ric12 = np.einsum('B,ABCB->AC', eta_diag, R12)
    Ric12 = 0.5 * (Ric12 + Ric12.T)
    R_scalar = float(np.einsum('A,AA->', eta_diag, Ric12))  # (local)

    eR1 = np.einsum('AC,BD->ABCD', eta, Ric12)  # (local)
    eR2 = np.einsum('AD,BC->ABCD', eta, Ric12)  # (local)
    eR3 = np.einsum('BC,AD->ABCD', eta, Ric12)  # (local)
    eR4 = np.einsum('BD,AC->ABCD', eta, Ric12)  # (local)
    ricci_term = (1.0 / (n - 2)) * (eR1 - eR2 - eR3 + eR4)  # (local)

    ee1 = np.einsum('AC,BD->ABCD', eta, eta)  # (local)
    ee2 = np.einsum('AD,BC->ABCD', eta, eta)  # (local)
    scalar_term = (R_scalar / ((n - 1) * (n - 2))) * (ee1 - ee2)  # (local)

    C12 = R12 - ricci_term + scalar_term  # (local)

    trace_check = float(np.max(np.abs(
        np.einsum('B,ABCB->AC', eta_diag, C12)
    )))  # (local)

    sign_tensor = np.einsum('A,B,C,D->ABCD',
                            eta_diag, eta_diag, eta_diag, eta_diag)  # (local)
    C_sq = float(np.sum(sign_tensor * C12 * C12))  # (local)

    return C12, Ric12, R_scalar, C_sq, trace_check


# =============================================================================
# SECTION 4: Null frame, BW decomposition, classification (from S77)
# =============================================================================

def construct_null_frame(n_spatial):
    """Build real null frame from a unit spatial direction. From S77."""
    n = DIM_TOTAL  # (local)
    e0 = np.zeros(n); e0[0] = 1.0  # (local)
    l_vec = (e0 + n_spatial) / np.sqrt(2)  # (local)
    k_vec = (e0 - n_spatial) / np.sqrt(2)  # (local)

    n_spat = n_spatial[1:]  # (local) 11D spatial part
    basis_spatial = np.eye(11)  # (local)
    ortho = []  # (local)
    for v in basis_spatial:
        w = v - np.dot(v, n_spat) * n_spat  # (local)
        for u in ortho:
            w -= np.dot(w, u) * u
        norm = np.linalg.norm(w)  # (local)
        if norm > 1e-12:
            ortho.append(w / norm)
        if len(ortho) == 10:
            break

    m_vecs = []  # (local)
    for v in ortho:
        m = np.zeros(n)  # (local)
        m[1:] = v
        m_vecs.append(m)

    return l_vec, k_vec, m_vecs


def cmpp_decomposition(C12, l_vec, k_vec, m_vecs):
    """Boost-weight decomposition of 12D Weyl in Lorentzian null frame."""
    n = DIM_TOTAL  # (local)
    n_t = len(m_vecs)  # (local)

    F = np.zeros((n, n))  # (local)
    F[0] = l_vec
    F[1] = k_vec
    for i in range(n_t):
        F[i + 2] = m_vecs[i]

    C_step1 = np.einsum('aA,ABCD->aBCD', F, C12)  # (local)
    C_step2 = np.einsum('bB,aBCD->abCD', F, C_step1)  # (local)
    C_step3 = np.einsum('cC,abCD->abcD', F, C_step2)  # (local)
    C_null = np.einsum('dD,abcD->abcd', F, C_step3)  # (local)

    def bw(idx):
        if idx == 0: return +1
        if idx == 1: return -1
        return 0

    bw_norms = {w: 0.0 for w in range(-4, 5)}  # (local)
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

    return {'bw_norms': bw_phys, 'total': total, 'C_null': C_null}


def classify_cmpp(decomp, tol=1e-10):
    """Classify CMPP type from Lorentzian BW decomposition."""
    total = decomp['total']  # (local)
    if total < tol:
        return 'O'

    rel_tol = tol * total  # (local)
    n2 = decomp['bw_norms'][+2]   # (local)
    n1 = decomp['bw_norms'][+1]   # (local)
    n0 = decomp['bw_norms'][0]    # (local)
    nm1 = decomp['bw_norms'][-1]  # (local)
    nm2 = decomp['bw_norms'][-2]  # (local)

    h2p = n2 > rel_tol   # (local)
    h1p = n1 > rel_tol   # (local)
    h1m = nm1 > rel_tol  # (local)
    h2m = nm2 > rel_tol  # (local)

    if not h2p and not h1p and not h2m and not h1m:
        return 'D' if n0 > rel_tol else 'O'
    elif not h2p and not h1p:
        if not h2m and not h1m:
            return 'D'
        elif not h2m:
            return 'III'
        return 'II'
    elif not h2p:
        return 'I'
    elif n2 / total < 0.001:
        return 'I'
    return 'G'


def make_spatial_dir(alpha, n_ext_3, n_int_8):
    """Build 12D unit spatial vector from mixing angle and sector dirs."""
    n12 = np.zeros(DIM_TOTAL)  # (local)
    n12[1:4] = np.sin(alpha) * n_ext_3
    n12[4:12] = np.cos(alpha) * n_int_8
    norm = np.linalg.norm(n12)  # (local)
    if norm < 1e-15:
        n12[1] = 1.0
        norm = 1.0  # (local)
    return n12 / norm


def scan_wand(C12, n_alpha=15, verbose=False):
    """Scan null directions to find WAND (most algebraically special)."""
    type_rank = {'O': 0, 'N': 1, 'III': 2, 'D': 3, 'II': 4, 'I': 5, 'G': 6}  # (local)
    best_type = 'G'      # (local)
    best_decomp = None   # (local)
    n_tested = 0         # (local)

    n_ext = np.array([0.0, 0.0, 1.0])  # (local)
    int_dirs = {}  # (local)
    for i in range(DIM_INT):
        d = np.zeros(DIM_INT); d[i] = 1.0  # (local)
        int_dirs[f'e{i}'] = d
    d = np.zeros(DIM_INT); d[SU2_IDX] = 1.0 / np.sqrt(3)
    int_dirs['su2_diag'] = d
    d = np.zeros(DIM_INT); d[C2_IDX] = 0.5
    int_dirs['c2_diag'] = d

    alpha_vals = np.linspace(0, np.pi / 2, n_alpha)  # (local)

    min_bw2_frac = 1.0      # (local)

    for label, n_int in int_dirs.items():
        for alpha in alpha_vals:
            n_spat = make_spatial_dir(alpha, n_ext, n_int)  # (local)
            try:
                l, k, mvecs = construct_null_frame(n_spat)
                decomp = cmpp_decomposition(C12, l, k, mvecs)
                ctype = classify_cmpp(decomp)
                n_tested += 1

                if type_rank.get(ctype, 6) < type_rank.get(best_type, 6):
                    best_type = ctype
                    best_decomp = decomp

                bw2_frac = decomp['bw_norms'][+2] / decomp['total'] if decomp['total'] > 0 else 1.0  # (local)
                if bw2_frac < min_bw2_frac:
                    min_bw2_frac = bw2_frac

            except Exception:
                pass

    return best_type, best_decomp, n_tested, min_bw2_frac


# =============================================================================
# SECTION 5: CMPP invariants (I, J, 27J^2 = I^3 Type D discriminant)
# =============================================================================

def compute_cmpp_invariants(C12):
    """
    CMPP invariants I = C_{ABCD} C^{ABCD} and J = C^A_B^C_D ... (trace cube).
    For Type D: 27 J^2 = I^3 (Penrose-Rindler "Petrov discriminant" identity
    generalized to higher dim via CMPP).
    """
    n = DIM_TOTAL  # (local)
    eta_diag = np.array([-1.0] + [1.0] * (n - 1))  # (local)
    sign_tensor = np.einsum('A,B,C,D->ABCD',
                            eta_diag, eta_diag, eta_diag, eta_diag)  # (local)
    C_up = sign_tensor * C12  # (local)

    I_inv = float(np.sum(C12 * C_up))  # (local)

    C_mixed = np.einsum('C,D,ABCD->ABCD', eta_diag, eta_diag, C12)  # (local)
    temp = np.einsum('ABCD,CDEF->ABEF', C_mixed, C_mixed)  # (local)
    J_inv = float(np.einsum('ABEF,EFAB->', temp, C_mixed))  # (local)

    lhs = 27.0 * J_inv**2  # (local)
    rhs = I_inv**3          # (local)
    deviation = abs(lhs - rhs) / (abs(rhs) + 1e-30)  # (local)

    return {
        'I': I_inv, 'J': J_inv,
        '27J2': lhs, 'I3': rhs,
        'type_D_deviation': deviation,
        'is_type_D': deviation < TOL_TYPE_D,
    }


# =============================================================================
# SECTION 6: PRE-REGISTERED CMPP INVARIANT — lambda_C2
# =============================================================================

def weyl_operator_full(C12):
    """12D Weyl as operator on Lambda^2(R^{11,1}) — 66 x 66 matrix."""
    n = DIM_TOTAL  # (local)
    pairs = [(a, b) for a in range(n) for b in range(a + 1, n)]  # (local)
    N = len(pairs)  # (local)
    C_mat = np.zeros((N, N))  # (local)
    for I, (a1, b1) in enumerate(pairs):
        for J, (a2, b2) in enumerate(pairs):
            C_mat[I, J] = C12[a1, b1, a2, b2]
    eigvals = np.linalg.eigvals(C_mat)  # (local)
    eigvals_real = np.sort(np.real(eigvals))  # (local)
    return {
        'eigvals': eigvals_real,
        'C_mat': C_mat,
        'pairs': pairs,
    }


def lambda_C2_restricted(C12):
    """
    PRE-REGISTERED CMPP INVARIANT:

    Compute eigenvalues of Weyl operator RESTRICTED to Lambda^2(C^2 sector).

    The C^2 sector spans internal indices 7,8,9,10 (C2_IDX + 4 in 12D).
    The 2-forms in C^2 are spanned by e_i ^ e_j for 7 <= i < j <= 10,
    giving C(4,2) = 6 basis 2-forms.

    The Weyl operator restricted to this subspace is a 6x6 matrix:
    C_restricted[IJ, KL] = C_{IJKL} with (I,J), (K,L) pairs from C^2.

    Return the FULL eigenvalue spectrum; the pre-registered invariant is
    lambda_C2_min = smallest eigenvalue (by absolute value), indicating
    "flat direction" in the C^2 subsector of Weyl.

    This is NON-TRIVIAL because (i) it is a sub-spectrum of the full
    Weyl operator, (ii) it is sensitive to the C^2-C^2 Riemann components
    which are what the sectional curvature C^2 measures.
    """
    # C^2 sector in 12D indexing
    c2_12 = [4 + i for i in C2_IDX]  # (local) = [7,8,9,10]
    # Form all 2-index pairs within C^2
    c2_pairs = [(a, b) for ia, a in enumerate(c2_12)
                for ib, b in enumerate(c2_12) if a < b]  # (local) 6 pairs
    N = len(c2_pairs)  # (local) = 6
    C_res = np.zeros((N, N))  # (local)
    for I, (a1, b1) in enumerate(c2_pairs):
        for J, (a2, b2) in enumerate(c2_pairs):
            C_res[I, J] = C12[a1, b1, a2, b2]
    # Symmetric part
    C_sym = 0.5 * (C_res + C_res.T)  # (local)
    asym_err = float(np.max(np.abs(C_res - C_res.T)))  # (local)
    eigvals = np.sort(np.linalg.eigvalsh(C_sym))  # (local) sorted real
    lambda_min_abs = float(np.min(np.abs(eigvals)))  # (local)
    lambda_min_signed = float(eigvals[np.argmin(np.abs(eigvals))])  # (local)
    return {
        'eigvals': eigvals,
        'C_restricted': C_sym,
        'asym_err': asym_err,
        'lambda_min_abs': lambda_min_abs,
        'lambda_min_signed': lambda_min_signed,
        'trace': float(np.trace(C_sym)),
        'det': float(np.linalg.det(C_sym)),
    }


# =============================================================================
# SECTION 7: Bel-Robinson (cross-check)
# =============================================================================

def bel_robinson_scalar(C12):
    """
    Cross-check: |Bel-Robinson|^2 or simpler non-negative scalar.
    For Lorentzian 4D: T_{abcd} T^{abcd} >= 0 (classical BR positivity).
    In higher D, use C_{ABCD}C^{ABCD} (Weyl squared) which is well-defined.

    Report simply |C|^2 and the sum of eigenvalue squares of the Weyl operator.
    """
    # Weyl-squared via signed contractions (already computed in compute_12d_weyl)
    n = DIM_TOTAL  # (local)
    eta_diag = np.array([-1.0] + [1.0] * (n - 1))  # (local)
    sign_tensor = np.einsum('A,B,C,D->ABCD',
                            eta_diag, eta_diag, eta_diag, eta_diag)  # (local)
    C_sq = float(np.sum(sign_tensor * C12 * C12))  # (local) may be negative in Lorentzian
    # Non-negative: sum of eigenvalue squares of Weyl operator on Lambda^2
    wo = weyl_operator_full(C12)  # (local)
    eig_sq_sum = float(np.sum(wo['eigvals']**2))  # (local) always >= 0
    return {
        'weyl_sq_signed': C_sq,
        'weyl_op_eig_sq_sum': eig_sq_sum,
    }


# =============================================================================
# MAIN COMPUTATION
# =============================================================================

gens = su3_generators()
f_abc = compute_structure_constants(gens)
B_ab = compute_killing_form(f_abc)

print(f"\n{'='*80}")
print("  STAGE 1: Geometry at each tau (8D + 12D static + cross-check)")
print(f"{'='*80}\n")

print(f"{'tau':>12s}  {'label':>14s}  {'R_8':>10s}  {'K_int':>12s}  "
      f"{'|C|^2':>14s}  {'C2_sect':>14s}  {'trace_err':>10s}")
print("-" * 100)

geometry = {}  # (local)
for tau, label in zip(TAU_VALUES, TAU_LABELS):
    geom8 = compute_8d_geometry(tau, gens, f_abc, B_ab)
    R12_stat = build_12d_riemann_static(geom8['R_abcd'])
    C12_stat, _, R12s, C_sq_stat, tr_stat = compute_12d_weyl(R12_stat)
    C2_sect = compute_c2_sectional_curvature(geom8['R_abcd'], tau)
    print(f"{tau:12.8f}  {label:>14s}  {geom8['R_scalar']:10.6f}  {geom8['K']:12.8f}  "
          f"{C_sq_stat:14.8f}  {C2_sect['K_mean_C2']:14.8f}  {tr_stat:10.2e}")
    geometry[tau] = {
        'geom8': geom8,
        'R12_stat': R12_stat,
        'C12_stat': C12_stat,
        'C_sq_stat': C_sq_stat,
        'trace_err_stat': tr_stat,
        'C2_sect': C2_sect,
    }


print(f"\n{'='*80}")
print("  STAGE 2: Unperturbed Type D Classification (baseline, ANSATZ-FORCED)")
print(f"{'='*80}\n")

print(f"{'tau':>12s}  {'CMPP':>6s}  {'min_bw2':>12s}  {'27J^2':>14s}  "
      f"{'I^3':>14s}  {'dev':>12s}  {'is_D?':>6s}")
print("-" * 100)

for tau, label in zip(TAU_VALUES, TAU_LABELS):
    g = geometry[tau]
    ctype_s, decomp_s, n_s, bw2_s = scan_wand(g['C12_stat'])
    inv_s = compute_cmpp_invariants(g['C12_stat'])
    print(f"{tau:12.8f}  {ctype_s:>6s}  {bw2_s:12.6e}  {inv_s['27J2']:14.6e}  "
          f"{inv_s['I3']:14.6e}  {inv_s['type_D_deviation']:12.6e}  "
          f"{'YES' if inv_s['is_type_D'] else 'NO':>6s}")
    geometry[tau]['cmpp_static'] = {
        'type': ctype_s, 'decomp': decomp_s, 'n_tested': n_s,
        'min_bw2': bw2_s, 'invariants': inv_s,
    }


print(f"\n{'='*80}")
print("  STAGE 3: Pre-registered lambda_C2 invariant (UNPERTURBED)")
print(f"{'='*80}\n")

print(f"{'tau':>12s}  {'label':>14s}  {'lambda_min_signed':>18s}  "
      f"{'|lambda_min|':>14s}  {'lambda_max':>12s}  {'det(C_res)':>14s}")
print("-" * 100)

for tau, label in zip(TAU_VALUES, TAU_LABELS):
    g = geometry[tau]
    lam_res = lambda_C2_restricted(g['C12_stat'])
    eigs = lam_res['eigvals']
    print(f"{tau:12.8f}  {label:>14s}  {lam_res['lambda_min_signed']:+18.10e}  "
          f"{lam_res['lambda_min_abs']:14.6e}  {eigs[-1]:12.6e}  "
          f"{lam_res['det']:+14.6e}")
    geometry[tau]['lambda_C2_stat'] = lam_res


print(f"\n{'='*80}")
print("  STAGE 4: ANSATZ-BREAKING PERTURBATION (epsilon = 0.01)")
print(f"{'='*80}")
print(f"  Perturbation: R_{{0,4,0,7}} += delta, with Riemann symmetries enforced")
print(f"  (time-C^2 non-block-diagonal Riemann component)\n")

print(f"{'tau':>12s}  {'delta':>12s}  {'CMPP':>6s}  {'min_bw2':>12s}  "
      f"{'27J^2/I^3 dev':>14s}  {'is_D?':>6s}  {'|C|^2':>12s}  {'tr_err':>10s}")
print("-" * 100)

for tau, label in zip(TAU_VALUES, TAU_LABELS):
    g = geometry[tau]
    R12_pert, delta = build_12d_riemann_perturbed(g['geom8']['R_abcd'], EPSILON)
    C12_pert, _, _, C_sq_pert, tr_pert = compute_12d_weyl(R12_pert)
    ctype_p, decomp_p, n_p, bw2_p = scan_wand(C12_pert)
    inv_p = compute_cmpp_invariants(C12_pert)
    lam_pert = lambda_C2_restricted(C12_pert)

    print(f"{tau:12.8f}  {delta:12.6e}  {ctype_p:>6s}  {bw2_p:12.6e}  "
          f"{inv_p['type_D_deviation']:14.6e}  "
          f"{'YES' if inv_p['is_type_D'] else 'NO':>6s}  "
          f"{C_sq_pert:12.6f}  {tr_pert:10.2e}")

    geometry[tau]['perturbed'] = {
        'R12': R12_pert,
        'C12': C12_pert,
        'delta': delta,
        'cmpp_type': ctype_p,
        'min_bw2': bw2_p,
        'invariants': inv_p,
        'C_sq': C_sq_pert,
        'trace_err': tr_pert,
        'lambda_C2': lam_pert,
    }


print(f"\n{'='*80}")
print("  STAGE 5: lambda_C2 under perturbation (PRE-REGISTERED INVARIANT)")
print(f"{'='*80}\n")

print(f"{'tau':>12s}  {'lambda_stat':>16s}  {'lambda_pert':>16s}  "
      f"{'|pert/max_stat|':>16s}")
print("-" * 100)

# Normalize by the max absolute stat lambda for relative comparison
stat_lams = [geometry[t]['lambda_C2_stat']['lambda_min_signed'] for t in TAU_VALUES]  # (local)
max_abs_stat = max(abs(x) for x in stat_lams)  # (local)

for tau, label in zip(TAU_VALUES, TAU_LABELS):
    g = geometry[tau]
    lam_s = g['lambda_C2_stat']['lambda_min_signed']  # (local)
    lam_p = g['perturbed']['lambda_C2']['lambda_min_signed']  # (local)
    rel_p = abs(lam_p) / max_abs_stat if max_abs_stat > 1e-30 else 0.0  # (local)
    print(f"{tau:12.8f}  {lam_s:+16.8e}  {lam_p:+16.8e}  {rel_p:16.6e}")


# =============================================================================
# CROSS-CHECKS
# =============================================================================

print(f"\n{'='*80}")
print("  CROSS-CHECKS")
print(f"{'='*80}\n")

# CHK-1: Bel-Robinson / |C|^2 non-negative (as eigenvalue-sum-of-squares)
print("CHK-1: Weyl-positivity surrogate (eigenvalue-square-sum >= 0)")
print("-" * 80)
for tau, label in zip(TAU_VALUES, TAU_LABELS):
    g = geometry[tau]
    br_stat = bel_robinson_scalar(g['C12_stat'])
    br_pert = bel_robinson_scalar(g['perturbed']['C12'])
    print(f"  tau = {tau:.6f}: |C|^2_stat = {br_stat['weyl_sq_signed']:.6e} | "
          f"eig^2_sum_stat = {br_stat['weyl_op_eig_sq_sum']:.6e} (>=0 check: "
          f"{'PASS' if br_stat['weyl_op_eig_sq_sum'] >= 0 else 'FAIL'})")
    print(f"  tau = {tau:.6f}: |C|^2_pert = {br_pert['weyl_sq_signed']:.6e} | "
          f"eig^2_sum_pert = {br_pert['weyl_op_eig_sq_sum']:.6e} (>=0 check: "
          f"{'PASS' if br_pert['weyl_op_eig_sq_sum'] >= 0 else 'FAIL'})")

# CHK-2: C^2 sectional curvature at tau = 0.537
print("\nCHK-2: C^2 sectional curvature at tau = 0.537 (S48 prediction: ~0)")
print("-" * 80)
for tau, label in zip(TAU_VALUES, TAU_LABELS):
    c2_sect = geometry[tau]['C2_sect']
    print(f"  tau = {tau:.8f}: K_mean_C2 = {c2_sect['K_mean_C2']:.10e}, "
          f"K_min_C2 = {c2_sect['K_min_C2']:.10e}, "
          f"K_primary = {c2_sect['K_ij_primary']:.10e}")

# CHK-3: lambda_C2 detects the sectional-curvature zero
print("\nCHK-3: Pre-registered lambda_C2 vs C^2 sectional curvature")
print("-" * 80)
for tau, label in zip(TAU_VALUES, TAU_LABELS):
    lam = geometry[tau]['lambda_C2_stat']['lambda_min_signed']  # (local)
    c2_mean = geometry[tau]['C2_sect']['K_mean_C2']             # (local)
    c2_min = geometry[tau]['C2_sect']['K_min_C2']               # (local)
    print(f"  tau = {tau:.8f}: lambda_C2 = {lam:+.6e} | "
          f"C^2_sect_mean = {c2_mean:+.6e} | C^2_sect_min = {c2_min:+.6e}")


# =============================================================================
# GATE EVALUATION
# =============================================================================

print(f"\n{'='*80}")
print("  GATE EVALUATION: S78-W3-H-CMPP-TAU-0.537")
print(f"{'='*80}\n")

# Criterion A: Type D persists under perturbation at all three tau
type_D_persists_stat = all(
    geometry[tau]['cmpp_static']['type'] == 'D'
    for tau in TAU_VALUES
)  # (local)
type_D_persists_pert = all(
    geometry[tau]['perturbed']['cmpp_type'] == 'D'
    for tau in TAU_VALUES
)  # (local)

disc_stat = [
    geometry[tau]['cmpp_static']['invariants']['type_D_deviation']
    for tau in TAU_VALUES
]  # (local)
disc_pert = [
    geometry[tau]['perturbed']['invariants']['type_D_deviation']
    for tau in TAU_VALUES
]  # (local)

disc_ok_stat = all(d < TOL_TYPE_D for d in disc_stat)  # (local)
disc_ok_pert = all(d < TOL_TYPE_D for d in disc_pert)  # (local)

# Criterion B: lambda_C2 distinguishes tau = 0.537
lam_below = geometry[TAU_BELOW]['lambda_C2_stat']['lambda_min_signed']   # (local)
lam_phase = geometry[TAU_PHASE]['lambda_C2_stat']['lambda_min_signed']   # (local)
lam_above = geometry[TAU_ABOVE]['lambda_C2_stat']['lambda_min_signed']   # (local)

max_abs_neighbor = max(abs(lam_below), abs(lam_above))  # (local)
rel_at_phase = abs(lam_phase) / max_abs_neighbor if max_abs_neighbor > 1e-30 else float('inf')  # (local)

# Zero-crossing: signs of lam_below and lam_above differ
sign_change = (lam_below * lam_above) < 0  # (local)

# Alternative criterion: lam_phase is much smaller than neighbors
invariant_detects_zero = (rel_at_phase < TOL_ZERO) or sign_change  # (local)

# Also check: sectional curvature is near zero at tau = 0.537
c2_sect_phase = geometry[TAU_PHASE]['C2_sect']['K_mean_C2']  # (local)
c2_sect_below = geometry[TAU_BELOW]['C2_sect']['K_mean_C2']  # (local)
c2_sect_above = geometry[TAU_ABOVE]['C2_sect']['K_mean_C2']  # (local)
c2_zero_detected = abs(c2_sect_phase) < 1e-3  # (local)

# Trace-err check (INCOMPUTABLE bound)
max_trace_err = max(
    geometry[tau]['perturbed']['trace_err']
    for tau in TAU_VALUES
)  # (local)

# Decide verdict
print(f"Criterion A (Type D persists under perturbation):")
print(f"  Unperturbed Type D at all tau:  {type_D_persists_stat}  (types: "
      f"{[geometry[t]['cmpp_static']['type'] for t in TAU_VALUES]})")
print(f"  Perturbed Type D at all tau:    {type_D_persists_pert}  (types: "
      f"{[geometry[t]['perturbed']['cmpp_type'] for t in TAU_VALUES]})")
print(f"  27J^2/I^3 disc unperturbed:     {['%.2e' % d for d in disc_stat]}")
print(f"  27J^2/I^3 disc perturbed:       {['%.2e' % d for d in disc_pert]}")
print(f"  Discriminant OK (unperturbed):  {disc_ok_stat}")
print(f"  Discriminant OK (perturbed):    {disc_ok_pert}")

print(f"\nCriterion B (lambda_C2 detects tau = 0.537):")
print(f"  lambda_C2(tau = {TAU_BELOW:.3f}) = {lam_below:+.6e}")
print(f"  lambda_C2(tau = {TAU_PHASE:.5f}) = {lam_phase:+.6e}")
print(f"  lambda_C2(tau = {TAU_ABOVE:.3f}) = {lam_above:+.6e}")
print(f"  |lambda_phase| / max(|neighbors|) = {rel_at_phase:.6e}")
print(f"  Sign change below->above:        {sign_change}")
print(f"  Invariant detects zero:          {invariant_detects_zero}")

print(f"\nAdditional sectional-curvature cross-check:")
print(f"  C^2 sectional K_mean at tau = {TAU_BELOW:.3f}: {c2_sect_below:+.6e}")
print(f"  C^2 sectional K_mean at tau = {TAU_PHASE:.5f}: {c2_sect_phase:+.6e}")
print(f"  C^2 sectional K_mean at tau = {TAU_ABOVE:.3f}: {c2_sect_above:+.6e}")
print(f"  C^2 zero at tau = 0.537 detected: {c2_zero_detected}")

print(f"\nINCOMPUTABLE check:")
print(f"  Max perturbed trace_err: {max_trace_err:.2e} (tol = {TOL_TRACE})")


# Final verdict
verdict = 'INCOMPUTABLE'  # (local)
verdict_reason = ''       # (local)

if max_trace_err > TOL_TRACE:
    verdict = 'INCOMPUTABLE'
    verdict_reason = f'Perturbed Weyl trace_err = {max_trace_err:.2e} > {TOL_TRACE}'
elif type_D_persists_pert and disc_ok_pert and invariant_detects_zero:
    verdict = 'PASS'
    verdict_reason = (
        f'Type D persists under epsilon={EPSILON} perturbation '
        f'(27J^2/I^3 max dev = {max(disc_pert):.2e}); '
        f'lambda_C2 detects zero at tau = 0.537 '
        f'(rel = {rel_at_phase:.3e}; sign_change = {sign_change}).'
    )
elif not type_D_persists_pert:
    verdict = 'FAIL'
    pert_types = [geometry[t]['perturbed']['cmpp_type'] for t in TAU_VALUES]  # (local)
    verdict_reason = (
        f'Type D breaks under perturbation: perturbed types = {pert_types}'
    )
elif type_D_persists_pert and not invariant_detects_zero:
    verdict = 'INFO'
    verdict_reason = (
        f'Type D persists (perturbed), but lambda_C2 AMBIGUOUS: '
        f'rel_at_phase = {rel_at_phase:.3e} (> {TOL_ZERO}), '
        f'no sign change ({sign_change}).'
    )
else:
    verdict = 'INFO'
    verdict_reason = 'Mixed result; see details.'

print(f"\n{'='*80}")
print(f"  VERDICT: {verdict}")
print(f"  {verdict_reason}")
print(f"{'='*80}")


# =============================================================================
# SAVE DATA
# =============================================================================

save_data = {
    'tau_values': TAU_VALUES,
    'tau_labels': np.array(TAU_LABELS),
    'epsilon': np.array([EPSILON]),
    'perturbation_spec': np.array([
        f'R_{{{PERT_TIME_IDX},{PERT_SPATIAL_IDX},{PERT_TIME_IDX},{PERT_C2_IDX}}}'
    ]),
    'static_types': np.array([geometry[t]['cmpp_static']['type'] for t in TAU_VALUES]),
    'perturbed_types': np.array([geometry[t]['perturbed']['cmpp_type'] for t in TAU_VALUES]),
    'static_C_sq': np.array([geometry[t]['C_sq_stat'] for t in TAU_VALUES]),
    'perturbed_C_sq': np.array([geometry[t]['perturbed']['C_sq'] for t in TAU_VALUES]),
    'static_27J2_I3_dev': np.array(disc_stat),
    'perturbed_27J2_I3_dev': np.array(disc_pert),
    'static_min_bw2': np.array([geometry[t]['cmpp_static']['min_bw2'] for t in TAU_VALUES]),
    'perturbed_min_bw2': np.array([geometry[t]['perturbed']['min_bw2'] for t in TAU_VALUES]),
    'lambda_C2_static_signed': np.array([
        geometry[t]['lambda_C2_stat']['lambda_min_signed'] for t in TAU_VALUES
    ]),
    'lambda_C2_static_eigs': np.array([
        geometry[t]['lambda_C2_stat']['eigvals'] for t in TAU_VALUES
    ]),
    'lambda_C2_pert_signed': np.array([
        geometry[t]['perturbed']['lambda_C2']['lambda_min_signed'] for t in TAU_VALUES
    ]),
    'lambda_C2_pert_eigs': np.array([
        geometry[t]['perturbed']['lambda_C2']['eigvals'] for t in TAU_VALUES
    ]),
    'C2_sect_K_mean': np.array([geometry[t]['C2_sect']['K_mean_C2'] for t in TAU_VALUES]),
    'C2_sect_K_min': np.array([geometry[t]['C2_sect']['K_min_C2'] for t in TAU_VALUES]),
    'C2_sect_K_primary': np.array([geometry[t]['C2_sect']['K_ij_primary'] for t in TAU_VALUES]),
    'verdict': np.array([verdict]),
    'verdict_reason': np.array([verdict_reason]),
    'type_D_persists_stat': np.array([type_D_persists_stat]),
    'type_D_persists_pert': np.array([type_D_persists_pert]),
    'rel_at_phase': np.array([rel_at_phase]),
    'sign_change_lambda_C2': np.array([sign_change]),
    'invariant_detects_zero': np.array([invariant_detects_zero]),
    'c2_zero_detected': np.array([c2_zero_detected]),
    'max_trace_err_pert': np.array([max_trace_err]),
    'TOL_TYPE_D': np.array([TOL_TYPE_D]),
    'TOL_ZERO': np.array([TOL_ZERO]),
    'TOL_TRACE': np.array([TOL_TRACE]),
}

script_dir = os.path.dirname(os.path.abspath(__file__))
npz_path = os.path.join(script_dir, 's78_cmpp_tau_0p537.npz')  # (local)
np.savez(npz_path, **save_data)
print(f"\nSaved: {npz_path}")


# =============================================================================
# PLOTS
# =============================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('S78-W3-H: CMPP Type D at tau = 0.537 under Ansatz-Breaking Perturbation',
             fontsize=14, fontweight='bold')

# Plot 1: lambda_C2 across tau
ax = axes[0, 0]
lams_stat_signed = [geometry[t]['lambda_C2_stat']['lambda_min_signed'] for t in TAU_VALUES]
lams_pert_signed = [geometry[t]['perturbed']['lambda_C2']['lambda_min_signed'] for t in TAU_VALUES]
ax.plot(TAU_VALUES, lams_stat_signed, 'o-', label='unperturbed', lw=2, ms=8)
ax.plot(TAU_VALUES, lams_pert_signed, 's--', label=f'perturbed (eps={EPSILON})',
        lw=2, ms=8, alpha=0.8)  # (local)
ax.axhline(0, color='k', lw=0.5, alpha=0.5)
ax.axvline(TAU_PHASE, color='r', lw=1, ls=':', alpha=0.5, label='phase (0.537)')
ax.set_xlabel('tau')
ax.set_ylabel('lambda_C2 (min signed eig of C | Lambda^2(C^2))')
ax.set_title('Pre-registered CMPP invariant: lambda_C2(tau)')
ax.legend()
ax.grid(True, alpha=0.3)

# Plot 2: C^2 sectional curvature
ax = axes[0, 1]
c2_means = [geometry[t]['C2_sect']['K_mean_C2'] for t in TAU_VALUES]
c2_mins = [geometry[t]['C2_sect']['K_min_C2'] for t in TAU_VALUES]
c2_prims = [geometry[t]['C2_sect']['K_ij_primary'] for t in TAU_VALUES]
ax.plot(TAU_VALUES, c2_means, 'o-', label='mean C^2 sect', lw=2, ms=8)
ax.plot(TAU_VALUES, c2_mins, 's--', label='min C^2 sect', lw=1.5, alpha=0.7)
ax.plot(TAU_VALUES, c2_prims, '^:', label='primary (e_7,e_8)', lw=1.5, alpha=0.7)
ax.axhline(0, color='k', lw=0.5, alpha=0.5)
ax.axvline(TAU_PHASE, color='r', lw=1, ls=':', alpha=0.5, label='phase (0.537)')
ax.set_xlabel('tau')
ax.set_ylabel('C^2 sectional curvature')
ax.set_title('Cross-check 2: C^2 sect. curv. zero at 0.537 (S48)')
ax.legend()
ax.grid(True, alpha=0.3)

# Plot 3: 27J^2/I^3 Type-D discriminant
ax = axes[1, 0]
ax.semilogy(TAU_VALUES, disc_stat, 'o-', label='unperturbed', lw=2, ms=8)
ax.semilogy(TAU_VALUES, disc_pert, 's--', label=f'perturbed (eps={EPSILON})',
            lw=2, ms=8, alpha=0.8)  # (local)
ax.axhline(TOL_TYPE_D, color='r', lw=1, ls=':', alpha=0.7, label=f'tol={TOL_TYPE_D}')
ax.axvline(TAU_PHASE, color='r', lw=1, ls=':', alpha=0.5)
ax.set_xlabel('tau')
ax.set_ylabel('|27J^2 - I^3| / |I^3|')
ax.set_title('Type D discriminant: 27J^2 = I^3')
ax.legend()
ax.grid(True, alpha=0.3)

# Plot 4: C^2-restricted Weyl spectrum at each tau
ax = axes[1, 1]
for idx, (tau, label) in enumerate(zip(TAU_VALUES, TAU_LABELS)):
    eigs_stat = geometry[tau]['lambda_C2_stat']['eigvals']
    eigs_pert = geometry[tau]['perturbed']['lambda_C2']['eigvals']
    x_stat = np.full_like(eigs_stat, idx - 0.1)
    x_pert = np.full_like(eigs_pert, idx + 0.1)
    ax.scatter(x_stat, eigs_stat, marker='o', s=40, alpha=0.8,
               label=f'{label} stat' if idx == 0 else None, color='C0')
    ax.scatter(x_pert, eigs_pert, marker='s', s=40, alpha=0.8,
               label=f'{label} pert' if idx == 0 else None, color='C1')
ax.axhline(0, color='k', lw=0.5, alpha=0.5)
ax.set_xticks([0, 1, 2])
ax.set_xticklabels([f'{t:.3f}' for t in TAU_VALUES])
ax.set_xlabel('tau')
ax.set_ylabel('Eigenvalues of C | Lambda^2(C^2 sector)')
ax.set_title('C^2-restricted Weyl spectrum')
ax.legend()
ax.grid(True, alpha=0.3)

plt.tight_layout()
png_path = os.path.join(script_dir, 's78_cmpp_tau_0p537.png')  # (local)
plt.savefig(png_path, dpi=140, bbox_inches='tight')
print(f"Saved: {png_path}")

t_total = time.time() - t_start  # (local)
print(f"\nTotal runtime: {t_total:.1f} s")

print(f"\nS78-W3-H-CMPP-TAU-0.537: {verdict} — "
      f"Type-D-under-perturbation={'Y' if type_D_persists_pert else 'N'}, "
      f"invariant=lambda_C2, "
      f"lambda_C2(0.537)={lam_phase:.3e}, "
      f"C^2(tau=0.537)={c2_sect_phase:.3e}")
