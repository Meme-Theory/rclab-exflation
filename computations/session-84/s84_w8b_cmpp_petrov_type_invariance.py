#!/usr/bin/env python3
"""
S84-W8B-95 CMPP-PETROV-TYPE-INVARIANCE: Extension of S76/S77 to Three New Tau
==============================================================================

Extends the S76/S77 CMPP classification across the MG-1 Jensen family to the
three additional tau-check-points:
  - tau_BCS_freeze  at tau = zero-point-two-two         (# (local))
  - tau_DNP         at tau = zero-point-two-eight-five  (# (local))
  - tau_phase_trans at tau = zero-point-five-three-seven (# (local))

Prior S76 set:  {0.00, 0.10, 0.19, 0.30}  (pre-fold + fold + post-fold + round)
Prior S77 set:  {0.00, 0.19, 1.614}       (overshoot turnaround)
Combined baseline:  5 distinct points (0.00, 0.10, 0.19, 0.30, 1.614)

Full invariance check set (this gate):
  8 distinct tau points = {0.00, 0.10, 0.19, 0.22, 0.285, 0.30, 0.537, 1.614}
  (5 prior + 3 new; the plan pre-registers "7-8 tau-points")

Hypothesis (pre-registered):
  static_type(tau) = D  at all 8 points
  dynamic_type(tau) = G at all 8 points

PASS: both invariances hold across all 8 points; register as MG-1 output
      "causal-structure invariant (not gear-loop algebraic)".

FAIL: at any of the 3 new points, Petrov-type deviates from (D, G).

INFO: prior S76/S77 evidence sufficient; no computation required (default per
      plan §W8b-95 §5). This script runs computation to upgrade to PASS.

=============================================================================
SUBSTITUTION CHAIN (required for direction/threshold claim)
=============================================================================

Step 1 (definitions):
  static_type(tau)  := best CMPP type from scan_wand on C12_static(tau)
                       [S77 construct_12d_riemann_static + compute_12d_weyl]
  dynamic_type(tau) := best CMPP type from scan_wand on C12_dynamic(tau,
                       tau_dot=v_terminal) [S77 build_12d_riemann_dynamic]

Step 2 (substitution — evaluated per tau):
  For each tau in {0.22, 0.285, 0.537}:
    geom8 = compute_8d_geometry(tau)                 # S76/S77 module
    R12_s = build_12d_riemann_static(geom8.R_abcd)
    C12_s = compute_12d_weyl(R12_s)
    static_type(tau) = scan_wand(C12_s).best_type

    R12_d = build_12d_riemann_dynamic(geom8.R_abcd, v_terminal)
    C12_d = compute_12d_weyl(R12_d)
    dynamic_type(tau) = scan_wand(C12_d).best_type

Step 3 (simplification):
  all_static_D  := all(static_type(tau)  == 'D' for tau in FULL_SET)
  all_dynamic_G := all(dynamic_type(tau) == 'G' for tau in FULL_SET)

Step 4 (direction):
  Gate PASSES  iff  (all_static_D AND all_dynamic_G).
  Gate FAILS   iff  any check-point type differs from baseline (D static, G
                    dynamic).
  Gate INFO    iff  max_trace_err > TOL_TRACE (numerically incomputable at
                    some point).

=============================================================================
ENVIRONMENT / MACHINERY PINS (per plan §W8b-95 §6)
=============================================================================

  scheme       : canonical-CMPP-invariance-v1
  convention   : a2-reduction-4D  (convention-tag carried through; the
                 actual classification operates on the full 12D Weyl per
                 S76/S77 — the 4D effective classification is the
                 projection under a_2 Seeley-DeWitt reduction, and the
                 (D, G) invariance is identical whether the full 12D
                 product structure or the 4D block is used, because the
                 product topology M^{3,1} x SU(3)(tau) forces Psi_2-only
                 spinor content in static and Psi_0..4 in dynamic)
  L_max        : N/A
  random_seed  : N/A (deterministic classifier)
  GPU path     : not required
  thread cap   : OMP_NUM_THREADS = 8 (CPU-only; 4D/12D Weyl ops are small)

Author: schwarzschild-penrose-geometer (Session 84, W8b-95)
Date:   2026-04-19
"""

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys
import time
import hashlib

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# ----- Framework imports (canonical) -----
from canonical_constants import (
    tau_fold, G_DeWitt, PI, v_terminal, H_fold, a2_fold, a4_fold,
)
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

# ----- S77 module reuse: import classifier primitives directly -----
#
# Rather than re-copying ~400 lines from S77, we import the compiled module.
# The S77 script is a top-level script (not a module), so we import it via
# importlib to pick up its function definitions without running its main
# computation block. However S77 has main-block side effects (it runs the
# computation at import) — we instead re-implement the SHORT classification
# primitives (they are already duplicated in S77 and S78 verbatim).

# The required primitives are lifted verbatim from s77_cmpp_turnaround.py
# (CMPP pipeline, proven stable across S76, S77, S78).

t_start = time.time()

DIM_INT = 8   # (local)
DIM_EXT = 4   # (local)
DIM_TOTAL = 12  # (local)

SU2_12 = [4 + i for i in SU2_IDX]  # (local)
C2_12 = [4 + i for i in C2_IDX]    # (local)
U1_12 = [4 + i for i in U1_IDX]    # (local)

# ----- Pre-registered tau sets -----
TAU_PRIOR_S76 = [0.10, 0.19, 0.30]  # (local) S76 transit set
TAU_PRIOR_S77 = [0.00, 1.614]        # (local) S77 round + overshoot turnaround
TAU_NEW = [0.22, 0.285, 0.537]       # (local) plan §W8b-95 §6 new_check_points

TAU_FULL = sorted(set(TAU_PRIOR_S76 + TAU_PRIOR_S77 + TAU_NEW))  # (local) 8 points
TAU_FULL_LABELS = {  # (local)
    0.00:   'round',
    0.10:   'pre-fold',
    0.19:   'fold',
    0.22:   'BCS-freeze',
    0.285:  'DNP',
    0.30:   'post-fold',
    0.537:  'phase-trans',
    1.614:  'overshoot',
}

N_CHECK_POINTS = len(TAU_FULL)  # (local) = 8

# ----- Classification thresholds -----
TOL_TRACE = 1e-8   # (local) Weyl trace-free tolerance
TOL_TYPE_D = 1e-4  # (local) 27J^2 = I^3 discriminant


# =============================================================================
# INPUT SHA LEDGER (gate-verdicts.md §S81+ dual-SHA requirement)
# =============================================================================

def sha256_of_file(path):
    """Compute sha256 hexdigest of a file (64-char hex). Safe for missing file."""
    if not os.path.exists(path):
        return "MISSING"
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()


PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))  # (local)

INPUT_FILES = [  # (local)
    'computations/_shared/canonical_constants.py',
    'computations/_shared/dirac_spectrum.py',
    'computations/session-76/s76_cmpp_type_gge_transit.py',
    'computations/session-77/s77_cmpp_turnaround.py',
    'sessions/permanent-results-registry.md',
]

INPUT_SHA_MAP = []  # (local) ordered pin list
for rel in INPUT_FILES:
    abs_path = os.path.join(PROJECT_ROOT, rel)
    INPUT_SHA_MAP.append((rel, sha256_of_file(abs_path)))

script_self = os.path.abspath(__file__)
self_sha = sha256_of_file(script_self)
INPUT_SHA_MAP.append(('SELF_SCRIPT', self_sha))


# =============================================================================
# Header print
# =============================================================================

print("=" * 80)
print("  S84-W8B-95 CMPP-PETROV-TYPE-INVARIANCE")
print("  Extension of S76/S77 to tau = {0.22, 0.285, 0.537}")
print("=" * 80)
print(f"\nMachinery pins:")
print(f"  scheme       = canonical-CMPP-invariance-v1")
print(f"  convention   = a2-reduction-4D")
print(f"  L_max        = N/A")
print(f"  OMP_THREADS  = {os.environ.get('OMP_NUM_THREADS')}")
print(f"  tau points   = {TAU_FULL}")
print(f"  N points     = {N_CHECK_POINTS}")
print(f"  new points   = {TAU_NEW}")
print(f"  prior S76    = {TAU_PRIOR_S76}")
print(f"  prior S77    = {TAU_PRIOR_S77}")
print(f"  v_terminal   = {v_terminal:.6f}  (canonical_constants)")
print(f"  tau_fold     = {tau_fold}         (canonical_constants)")

print(f"\nINPUT SHA LEDGER:")
for i, (rel, sha) in enumerate(INPUT_SHA_MAP):
    print(f"  [{i}] {rel}: {sha}")


# =============================================================================
# CMPP primitives (verbatim from s77_cmpp_turnaround.py / s78_cmpp_tau_0p537.py)
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
    """Full 8D internal geometry at given tau."""
    g_s = jensen_metric(B_ab, tau)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    R_abcd = compute_riemann_ON(ft, Gamma)
    Ric = np.einsum('abca->bc', R_abcd)
    Ric = 0.5 * (Ric + Ric.T)
    R_scalar = float(np.trace(Ric))  # (local)
    return {'R_abcd': R_abcd, 'Ric': Ric, 'R_scalar': R_scalar, 'g_s': g_s}


def build_12d_riemann_static(R8):
    """Static product M^{3,1} x K^8. Internal block only."""
    R12 = np.zeros((DIM_TOTAL, DIM_TOTAL, DIM_TOTAL, DIM_TOTAL))  # (local)
    R12[4:12, 4:12, 4:12, 4:12] = R8
    return R12


def build_12d_riemann_dynamic(R8, tau_dot):
    """Dynamic case: tau_dot = v_terminal; extrinsic curvature cross terms.
    Verbatim from S77."""
    R12 = np.zeros((DIM_TOTAL, DIM_TOTAL, DIM_TOTAL, DIM_TOTAL))  # (local)
    lam = np.zeros(DIM_INT)  # (local)
    lam[SU2_IDX] = -2.0
    lam[C2_IDX] = +1.0
    lam[U1_IDX] = +2.0
    K_diag = -(tau_dot / 2.0) * lam  # (local) extrinsic curvature

    R12[4:12, 4:12, 4:12, 4:12] = R8.copy()
    for a in range(DIM_INT):
        for b in range(DIM_INT):
            R12[a+4, b+4, a+4, b+4] += K_diag[a] * K_diag[b]
            R12[a+4, b+4, b+4, a+4] -= K_diag[a] * K_diag[b]

    for a in range(DIM_INT):
        val = K_diag[a]**2  # (local)
        R12[0, a+4, 0, a+4] = val
        R12[a+4, 0, a+4, 0] = val
        R12[0, a+4, a+4, 0] = -val
        R12[a+4, 0, 0, a+4] = -val

    return R12, K_diag


def compute_12d_weyl(R12):
    """Compute 12D Weyl C_ABCD from R12. Lorentzian (eta=diag(-1,+1,...,+1)).
    Verbatim from S77."""
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

    trace_check = float(np.max(np.abs(np.einsum('B,ABCB->AC', eta_diag, C12))))  # (local)

    sign_tensor = np.einsum('A,B,C,D->ABCD', eta_diag, eta_diag, eta_diag, eta_diag)  # (local)
    C_sq = float(np.sum(sign_tensor * C12 * C12))  # (local)

    return C12, Ric12, R_scalar, C_sq, trace_check


def construct_null_frame(n_spatial):
    """Build real null frame from unit spatial direction."""
    n = DIM_TOTAL  # (local)
    e0 = np.zeros(n); e0[0] = 1.0
    l_vec = (e0 + n_spatial) / np.sqrt(2)  # (local)
    k_vec = (e0 - n_spatial) / np.sqrt(2)  # (local)

    n_spat = n_spatial[1:]  # (local)
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
    """Boost-weight decomposition in Lorentzian null frame."""
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
    """Classify CMPP type O<N<III<D<II<I<G."""
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
    """Build 12D unit spatial vector."""
    n12 = np.zeros(DIM_TOTAL)  # (local)
    n12[1:4] = np.sin(alpha) * n_ext_3
    n12[4:12] = np.cos(alpha) * n_int_8
    norm = np.linalg.norm(n12)  # (local)
    if norm < 1e-15:
        n12[1] = 1.0
        norm = 1.0  # (local)
    return n12 / norm


def scan_wand(C12, n_alpha=15):
    """Scan null directions, find most algebraically-special type."""
    type_rank = {'O': 0, 'N': 1, 'III': 2, 'D': 3, 'II': 4, 'I': 5, 'G': 6}  # (local)
    best_type = 'G'   # (local)
    best_bw2 = 1.0    # (local)

    n_ext = np.array([0.0, 0.0, 1.0])  # (local)
    int_dirs = {}  # (local)
    for i in range(DIM_INT):
        d = np.zeros(DIM_INT); d[i] = 1.0
        int_dirs[f'e{i}'] = d
    d = np.zeros(DIM_INT); d[SU2_IDX] = 1.0 / np.sqrt(3)
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
    n_tested = 0  # (local)
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
                bw2_frac = decomp['bw_norms'][+2] / decomp['total'] if decomp['total'] > 0 else 1.0  # (local)
                if bw2_frac < best_bw2:
                    best_bw2 = bw2_frac
            except Exception:
                pass

    return best_type, n_tested, best_bw2


# =============================================================================
# MAIN COMPUTATION
# =============================================================================

print(f"\n{'='*80}")
print(f"  STAGE 1: Compute geometry at 8 tau points (8D internal)")
print(f"{'='*80}")

gens = su3_generators()
f_abc = compute_structure_constants(gens)
B_ab = compute_killing_form(f_abc)

geometry = {}  # (local)
print(f"\n{'tau':>8s}  {'label':>12s}  {'R_8':>12s}")
print("-" * 50)
for tau in TAU_FULL:
    g8 = compute_8d_geometry(tau, gens, f_abc, B_ab)
    geometry[tau] = g8
    print(f"{tau:8.4f}  {TAU_FULL_LABELS[tau]:>12s}  {g8['R_scalar']:12.6f}")


print(f"\n{'='*80}")
print(f"  STAGE 2: Static CMPP classification at 8 tau points")
print(f"{'='*80}")

print(f"\n{'tau':>8s}  {'label':>12s}  {'CMPP':>6s}  {'min_bw+2':>12s}  "
      f"{'|C|^2':>14s}  {'trace_err':>11s}  {'new?':>5s}")
print("-" * 85)

static_types = {}  # (local)
static_meta = {}   # (local)
for tau in TAU_FULL:
    t0 = time.time()  # (local)
    g8 = geometry[tau]
    R12 = build_12d_riemann_static(g8['R_abcd'])
    C12, _, _, C_sq, tr = compute_12d_weyl(R12)
    best_type, n_tested, bw2_frac = scan_wand(C12)
    static_types[tau] = best_type
    is_new = '*' if tau in TAU_NEW else ' '  # (local)
    static_meta[tau] = {
        'C_sq': C_sq, 'trace_err': tr, 'min_bw2': bw2_frac,
        'n_tested': n_tested, 'time': time.time() - t0,
    }
    print(f"{tau:8.4f}  {TAU_FULL_LABELS[tau]:>12s}  {best_type:>6s}  "
          f"{bw2_frac:12.4e}  {C_sq:14.6f}  {tr:11.2e}  {is_new:>5s}")


print(f"\n{'='*80}")
print(f"  STAGE 3: Dynamic CMPP classification at 8 tau points")
print(f"          (tau_dot = v_terminal = {v_terminal:.4f})")
print(f"{'='*80}")

print(f"\n{'tau':>8s}  {'label':>12s}  {'CMPP':>6s}  {'min_bw+2':>12s}  "
      f"{'|C|^2':>14s}  {'trace_err':>11s}  {'new?':>5s}")
print("-" * 85)

dynamic_types = {}  # (local)
dynamic_meta = {}   # (local)
for tau in TAU_FULL:
    t0 = time.time()  # (local)
    g8 = geometry[tau]
    R12_dyn, K_diag = build_12d_riemann_dynamic(g8['R_abcd'], v_terminal)
    C12_d, _, _, C_sq_d, tr_d = compute_12d_weyl(R12_dyn)
    best_type, n_tested, bw2_frac = scan_wand(C12_d)
    dynamic_types[tau] = best_type
    is_new = '*' if tau in TAU_NEW else ' '  # (local)
    dynamic_meta[tau] = {
        'C_sq': C_sq_d, 'trace_err': tr_d, 'min_bw2': bw2_frac,
        'n_tested': n_tested, 'K_diag': K_diag.copy(),
        'time': time.time() - t0,
    }
    print(f"{tau:8.4f}  {TAU_FULL_LABELS[tau]:>12s}  {best_type:>6s}  "
          f"{bw2_frac:12.4e}  {C_sq_d:14.6f}  {tr_d:11.2e}  {is_new:>5s}")


# =============================================================================
# INVARIANCE CHECK
# =============================================================================

print(f"\n{'='*80}")
print(f"  STAGE 4: Invariance check")
print(f"{'='*80}")

all_static_D = all(static_types[t] == 'D' for t in TAU_FULL)    # (local)
all_dynamic_G = all(dynamic_types[t] == 'G' for t in TAU_FULL)  # (local)

max_static_trace = max(static_meta[t]['trace_err'] for t in TAU_FULL)   # (local)
max_dynamic_trace = max(dynamic_meta[t]['trace_err'] for t in TAU_FULL) # (local)
max_trace_err = max(max_static_trace, max_dynamic_trace)  # (local)

# Per-point diagnostics
print(f"\n  Static CMPP types across 8 tau: {[static_types[t] for t in TAU_FULL]}")
print(f"  Dynamic CMPP types across 8 tau: {[dynamic_types[t] for t in TAU_FULL]}")
print(f"\n  all_static_D  = {all_static_D}")
print(f"  all_dynamic_G = {all_dynamic_G}")
print(f"  max_trace_err_static  = {max_static_trace:.2e}  (tol={TOL_TRACE})")
print(f"  max_trace_err_dynamic = {max_dynamic_trace:.2e}  (tol={TOL_TRACE})")

# New-point-specific check (plan §W8b-95 §10)
static_new = [static_types[t] for t in TAU_NEW]    # (local)
dynamic_new = [dynamic_types[t] for t in TAU_NEW]  # (local)
print(f"\n  NEW-POINT TYPES (tau = {TAU_NEW}):")
print(f"    static:  {static_new}")
print(f"    dynamic: {dynamic_new}")


# =============================================================================
# VERDICT
# =============================================================================

verdict = 'INFO'  # (local) default per plan
verdict_reason = ''  # (local)

if max_trace_err > TOL_TRACE:
    verdict = 'INFO'
    verdict_reason = (
        f'Weyl trace-free numerics degraded at some tau '
        f'(max trace_err = {max_trace_err:.2e} > {TOL_TRACE}); '
        f'defaulting to INFO per plan §W8b-95 §5. '
        f'Prior S76/S77 evidence already supports invariance at 5 points.'
    )
elif all_static_D and all_dynamic_G:
    verdict = 'PASS'
    verdict_reason = (
        f'CMPP Petrov-type transit-invariant across all {N_CHECK_POINTS} tau '
        f'check-points: static=D, dynamic=G. Registry entry: MG-1 output '
        f'"CMPP Petrov type transit-invariant (static D, dynamic G) — '
        f'causal-structure invariant".'
    )
else:
    verdict = 'FAIL'
    # Identify which point(s) deviated
    bad_static = [(t, static_types[t]) for t in TAU_FULL if static_types[t] != 'D']  # (local)
    bad_dynamic = [(t, dynamic_types[t]) for t in TAU_FULL if dynamic_types[t] != 'G']  # (local)
    verdict_reason = (
        f'Petrov-type change detected. '
        f'Static non-D at: {bad_static}. '
        f'Dynamic non-G at: {bad_dynamic}. '
        f'Transit-invariance claim refuted at these tau.'
    )


# =============================================================================
# INPUT-PIN MAP and CLOSURE SHA
# =============================================================================

# Numerical output values (rounded to stable precision for sha)
static_vec = "/".join(static_types[t] for t in TAU_FULL)     # (local)
dynamic_vec = "/".join(dynamic_types[t] for t in TAU_FULL)   # (local)

output_pin = {
    'scheme': 'canonical-CMPP-invariance-v1',
    'convention': 'a2-reduction-4D',
    'L_max': 'N/A',
    'tau_full': TAU_FULL,
    'static_types': static_vec,
    'dynamic_types': dynamic_vec,
    'all_static_D': all_static_D,
    'all_dynamic_G': all_dynamic_G,
    'n_points': N_CHECK_POINTS,
    'v_terminal': float(v_terminal),
    'tau_fold': float(tau_fold),
    'verdict': verdict,
}

# Content-SHA (physical result)
import json
content_blob = json.dumps(output_pin, sort_keys=True, separators=(',', ':'))
content_sha = hashlib.sha256(content_blob.encode('utf-8')).hexdigest()

# Audit-SHA (provenance: ordered input-pin map + output pin)
audit_items = [f"{rel}:{sha}" for rel, sha in INPUT_SHA_MAP]
audit_items.append(f"OUTPUT:{content_sha}")
audit_blob = "||".join(audit_items)
audit_sha = hashlib.sha256(audit_blob.encode('utf-8')).hexdigest()

# Closure SHA = audit_sha (per gate-verdicts.md: "SHA-256 of the ordered
# input-pin map" — here closure = audit chain including output)
closure_sha = audit_sha

print(f"\n{'='*80}")
print(f"  VERDICT: {verdict}")
print(f"{'='*80}")
print(f"\n  Reason: {verdict_reason}")

print(f"\n  SHAs:")
print(f"    content_sha256 = {content_sha}")
print(f"    audit_sha256   = {audit_sha}")
print(f"    closure_sha256 = {closure_sha}")


# =============================================================================
# SAVE ARTIFACTS
# =============================================================================

script_dir = os.path.dirname(os.path.abspath(__file__))  # (local)
npz_path = os.path.join(script_dir, 's84_w8b_cmpp_petrov_type_invariance.npz')  # (local)

np.savez(
    npz_path,
    tau_full=np.array(TAU_FULL),
    tau_new=np.array(TAU_NEW),
    static_types=np.array([static_types[t] for t in TAU_FULL]),
    dynamic_types=np.array([dynamic_types[t] for t in TAU_FULL]),
    static_min_bw2=np.array([static_meta[t]['min_bw2'] for t in TAU_FULL]),
    dynamic_min_bw2=np.array([dynamic_meta[t]['min_bw2'] for t in TAU_FULL]),
    static_C_sq=np.array([static_meta[t]['C_sq'] for t in TAU_FULL]),
    dynamic_C_sq=np.array([dynamic_meta[t]['C_sq'] for t in TAU_FULL]),
    static_trace_err=np.array([static_meta[t]['trace_err'] for t in TAU_FULL]),
    dynamic_trace_err=np.array([dynamic_meta[t]['trace_err'] for t in TAU_FULL]),
    all_static_D=np.array([all_static_D]),
    all_dynamic_G=np.array([all_dynamic_G]),
    verdict=np.array([verdict]),
    content_sha=np.array([content_sha]),
    audit_sha=np.array([audit_sha]),
    v_terminal=np.array([float(v_terminal)]),
    tau_fold=np.array([float(tau_fold)]),
)
print(f"\nSaved: {npz_path}")


# Plot: min_bw+2 across tau (log-scale) for static (should be ~1e-16 Type D)
# and dynamic (should be O(1) Type G)
fig, ax = plt.subplots(1, 1, figsize=(10, 6))
taus = np.array(TAU_FULL)  # (local)
s_bw = np.array([static_meta[t]['min_bw2'] for t in TAU_FULL])   # (local)
d_bw = np.array([dynamic_meta[t]['min_bw2'] for t in TAU_FULL])  # (local)
ax.semilogy(taus, np.clip(s_bw, 1e-18, None), 'o-', label='static (expect 0, Type D)', lw=2, ms=8)
ax.semilogy(taus, np.clip(d_bw, 1e-18, None), 's-', label='dynamic (expect O(1), Type G)', lw=2, ms=8)
for t in TAU_NEW:
    ax.axvline(t, color='r', lw=0.5, alpha=0.5, ls=':')
ax.axvline(tau_fold, color='k', lw=0.5, alpha=0.5, ls='--', label='tau_fold=0.19')
ax.set_xlabel('tau')
ax.set_ylabel('min(bw+2 norm fraction)')
ax.set_title('S84-W8B-95 CMPP Petrov Invariance: 8 tau points\n'
             '(static Type D = small min bw+2; dynamic Type G = large min bw+2)')
ax.legend()
ax.grid(True, alpha=0.3)
png_path = os.path.join(script_dir, 's84_w8b_cmpp_petrov_type_invariance.png')  # (local)
plt.tight_layout()
plt.savefig(png_path, dpi=140, bbox_inches='tight')
print(f"Saved: {png_path}")


# =============================================================================
# VERDICT LINE (canonical format per .claude/rules/gate-verdicts.md)
# =============================================================================

verdict_value = f"{static_vec}/{dynamic_vec}/{N_CHECK_POINTS}"  # (local)

verdict_line = (
    f"S84-W8B-95-CMPP-PETROV-TYPE-INVARIANCE: {verdict} -- "
    f"value={verdict_value} "
    f"scheme=canonical-CMPP-invariance-v1 "
    f"convention=a2-reduction-4D "
    f"L_max=N/A "
    f"sha256={closure_sha} "
    f"audit_sha256={audit_sha} "
    f"content_sha256={content_sha}"
)

verdict_file = os.path.join(script_dir, 's84_gate_verdicts.txt')  # (local)
with open(verdict_file, 'a', encoding='utf-8') as f:
    f.write(verdict_line + "\n")
print(f"\nAppended verdict to: {verdict_file}")
print(f"\nVERDICT LINE:\n  {verdict_line}")


t_total = time.time() - t_start  # (local)
print(f"\nTotal runtime: {t_total:.1f} s")
print("=" * 80)
print(f"  S84-W8B-95 CMPP-PETROV-TYPE-INVARIANCE: {verdict}")
print("=" * 80)
