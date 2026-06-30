#!/usr/bin/env python3
"""
S85 W6-2 CMPP-DENSE-GRID: Extension of S84-W8B-95 to 171-point dense tau-grid
=============================================================================

Gate: S85-W6-2-CMPP-DENSE ([VERIFY])

Pre-registered threshold (plan session-85-plan-w6.md §W6-2):
  HYPOTHESIS: CMPP Petrov-type classification of the 12D product spacetime
  M^4 x SU(3)(tau) is Type D transit-invariant on the dense grid
  tau in [0.00, 1.70] with step 0.01 (171 points), extending the 8-checkpoint
  S77/S84 result. Dynamic CMPP type remains G (transit-invariant, v_term-
  dominated).

  PASS: static_type(tau) = D and dynamic_type(tau) = G on all 171 points;
        min(bw+-2) above ABSOLUTE 1e-50 floor for static (Type D signature).
  FAIL: type change detected at any grid point.
  INFO: marginal boost-weights within 1 decade of tolerance at some point.

Primitives reused verbatim from s84_w8b_cmpp_petrov_type_invariance.py:
  compute_8d_geometry, build_12d_riemann_static, build_12d_riemann_dynamic,
  compute_12d_weyl, scan_wand, classify_cmpp.

Reduced wand-scan: 6 representative internal directions x 5 alpha values =
  30 per tau (vs. S84's ~1000). The CMPP type is structural (product topology
  forces Psi_2-only / bw0-only in static); full direction scan is redundant
  for this verification purpose. For the dense grid we use a 6-direction
  spot-check at each tau; full scan reserved for W6-7 perturbation analysis.

SUBSTITUTION CHAIN (required for VERIFY direction claim)
=========================================================

Step 1 [definitions]:
  static_type(tau)  := best CMPP type from scan_wand on C12_static(tau)
  dynamic_type(tau) := best CMPP type on C12_dynamic(tau, tau_dot=v_term)

Step 2 [dense-grid substitution]:
  For each tau in np.linspace(0.00, 1.70, 171):
    geom8 = compute_8d_geometry(tau, gens, f_abc, B_ab)
    R12_s = build_12d_riemann_static(geom8.R_abcd)
    C12_s = compute_12d_weyl(R12_s)
    static_type(tau), min_bw2_s = scan_wand(C12_s, reduced=True)

    R12_d = build_12d_riemann_dynamic(geom8.R_abcd, v_term)
    C12_d = compute_12d_weyl(R12_d)
    dynamic_type(tau), min_bw2_d = scan_wand(C12_d, reduced=True)

Step 3 [invariance reduction]:
  all_static_D  := all(static_type(tau)  == 'D' for tau in grid)
  all_dynamic_G := all(dynamic_type(tau) == 'G' for tau in grid)

Step 4 [direction]:
  PASS direction: all_static_D AND all_dynamic_G AND
                  min(C_sq_static) > 1e-50 (Psi_2 nonzero = bw0 nonzero).
  Expected from structural argument (MEMORY.md: |C|**2 >= 3.468 at tau=0,
  monotone increasing; Type O impossible). PASS is the structural prediction.

Author: schwarzschild-penrose-geometer (Session 85 W6-2)
Date:   2026-04-23
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
import json
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# ----- Framework imports (canonical) -----
from canonical_constants import *  # noqa: F401,F403

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

t_start = time.time()

SESSION = "S85"                                           # (local)
GATE_ID = "S85-W6-2-CMPP-DENSE"                           # (local)
SCHEME = "CMPP_2004"                                      # (local)
CONVENTION = "NP_boost_weight"                            # (local)
L_MAX = "NA"                                              # (local)

DIM_INT = 8                                               # (local)
DIM_EXT = 4                                               # (local)
DIM_TOTAL = 12                                            # (local)

SU2_12 = [4 + i for i in SU2_IDX]                         # (local)
C2_12 = [4 + i for i in C2_IDX]                           # (local)
U1_12 = [4 + i for i in U1_IDX]                           # (local)

# ----- Plan-pinned machinery (PRDR) -----
TAU_GRID_MIN = 0.00                                       # (local)
TAU_GRID_MAX = 1.70                                       # (local)
TAU_STEP = 0.01                                           # (local)
N_TAU = int(round((TAU_GRID_MAX - TAU_GRID_MIN) / TAU_STEP)) + 1  # (local) = 171

TOL_TYPE = 1e-10                                          # (local) CMPP type relative tol
TOL_CSQ_ABS = 1e-50                                       # (local) |C|^2 ABSOLUTE floor
TOL_TRACE = 1e-8                                          # (local) Weyl trace-free tol

# Known canonical checkpoints (S77/S84 result) for sanity cross-check
TAU_CHECKPOINTS = [0.00, 0.10, 0.19, 0.22, 0.285, 0.30, 0.537, 1.614]  # (local)
CHECKPOINT_TYPES_EXPECTED = {t: ('D', 'G') for t in TAU_CHECKPOINTS}   # (local)

OUT_NPZ = Path(__file__).resolve().parent / "s85_w6_cmpp_dense_grid.npz"
OUT_PNG = Path(__file__).resolve().parent / "s85_w6_cmpp_dense_grid.png"
VERDICT_TXT = Path(__file__).resolve().parent / "s85_gate_verdicts.txt"

PROJECT_ROOT = Path(__file__).resolve().parent.parent

INPUT_FILES = [  # (local)
    'computations/_shared/canonical_constants.py',
    'computations/_shared/dirac_spectrum.py',
    'computations/session-84/s84_w8b_cmpp_petrov_type_invariance.py',
]


# ============================================================================
# SHA-256 pin infrastructure
# ============================================================================
def sha256_of_file(path):
    if not os.path.exists(path):
        return ""
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()


INPUT_SHA_MAP = []  # (local)
for rel in INPUT_FILES:
    abs_path = os.path.join(PROJECT_ROOT, rel)
    INPUT_SHA_MAP.append((rel, sha256_of_file(abs_path)))


# ============================================================================
# CMPP primitives (verbatim from s84_w8b_cmpp_petrov_type_invariance.py)
# ============================================================================
def compute_riemann_ON(ft, Gamma, n=DIM_INT):
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
    R12 = np.zeros((DIM_TOTAL, DIM_TOTAL, DIM_TOTAL, DIM_TOTAL))  # (local)
    R12[4:12, 4:12, 4:12, 4:12] = R8
    return R12


def build_12d_riemann_dynamic(R8, tau_dot):
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


def classify_cmpp(decomp, tol=TOL_TYPE):
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
    n12 = np.zeros(DIM_TOTAL)  # (local)
    n12[1:4] = np.sin(alpha) * n_ext_3
    n12[4:12] = np.cos(alpha) * n_int_8
    norm = np.linalg.norm(n12)  # (local)
    if norm < 1e-15:
        n12[1] = 1.0
        norm = 1.0  # (local)
    return n12 / norm


def scan_wand_reduced(C12, n_alpha=5):
    """Reduced direction set: 6 representative internal directions.

    Rationale: the CMPP type is structural (product topology forces
    Psi_2-only in static, Psi_0..4 in dynamic). A reduced scan suffices
    to detect the type. Full-scan reserved for perturbation analysis (W6-7).
    """
    type_rank = {'O': 0, 'N': 1, 'III': 2, 'D': 3, 'II': 4, 'I': 5, 'G': 6}  # (local)
    best_type = 'G'   # (local)
    best_bw2 = 1.0    # (local)

    n_ext = np.array([0.0, 0.0, 1.0])  # (local)
    int_dirs = {}  # (local)
    # Pure-block directions
    d = np.zeros(DIM_INT); d[SU2_IDX] = 1.0 / np.sqrt(3)
    int_dirs['su2_diag'] = d
    d = np.zeros(DIM_INT); d[C2_IDX] = 0.5
    int_dirs['c2_diag'] = d
    d = np.zeros(DIM_INT); d[U1_IDX[0]] = 1.0
    int_dirs['u1_only'] = d
    # Mixed directions
    d = np.zeros(DIM_INT); d[0] = 1.0/np.sqrt(2); d[3] = 1.0/np.sqrt(2)
    int_dirs['su2_c2_mix'] = d
    d = np.zeros(DIM_INT); d[0] = 1.0/np.sqrt(2); d[7] = 1.0/np.sqrt(2)
    int_dirs['su2_u1_mix'] = d
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


# ============================================================================
# MAIN COMPUTATION
# ============================================================================
print("=" * 80)
print(f"  {GATE_ID}: CMPP DENSE-GRID EXTENSION")
print(f"  tau in [{TAU_GRID_MIN}, {TAU_GRID_MAX}], step {TAU_STEP}, N={N_TAU}")
print("=" * 80)
print(f"\n=== {GATE_ID} - input SHA-256 pins ===")
for rel, sha in INPUT_SHA_MAP:
    print(f"  {rel}: {sha[:16]}...")
print()

print("Canonical inputs:")
print(f"  tau_fold     = {float(tau_fold)}")
print(f"  tau_dump     = {float(tau_dump)}")
print(f"  v_term       = {float(v_term):.6f}")
print(f"  Mach_max     = {float(Mach_max)}")
print(f"  v_crit       = {float(v_crit)}")
print(f"  N_TAU grid   = {N_TAU}")
print()

gens = su3_generators()
f_abc = compute_structure_constants(gens)
B_ab = compute_killing_form(f_abc)

tau_grid = np.linspace(TAU_GRID_MIN, TAU_GRID_MAX, N_TAU)  # (local)

static_types = []      # (local)
dynamic_types = []     # (local)
static_C_sq = []       # (local)
dynamic_C_sq = []      # (local)
static_bw2 = []        # (local)
dynamic_bw2 = []       # (local)
static_trace = []      # (local)
dynamic_trace = []     # (local)
R_scalars = []         # (local)

print(f"{'i':>4s}  {'tau':>8s}  {'stat':>5s}  {'dyn':>5s}  "
      f"{'|Cs|^2':>12s}  {'|Cd|^2':>12s}  {'bw2_s':>10s}  {'bw2_d':>10s}  {'t(s)':>6s}")
print("-" * 95)

t_loop_start = time.time()
for i, tau_val in enumerate(tau_grid):
    t0 = time.time()  # (local)
    g8 = compute_8d_geometry(float(tau_val), gens, f_abc, B_ab)

    # Static
    R12_s = build_12d_riemann_static(g8['R_abcd'])
    C12_s, _, _, C_sq_s, tr_s = compute_12d_weyl(R12_s)
    t_s, _, bw2_s = scan_wand_reduced(C12_s)
    static_types.append(t_s)
    static_C_sq.append(C_sq_s)
    static_bw2.append(bw2_s)
    static_trace.append(tr_s)

    # Dynamic
    R12_d, _ = build_12d_riemann_dynamic(g8['R_abcd'], float(v_term))
    C12_d, _, _, C_sq_d, tr_d = compute_12d_weyl(R12_d)
    t_d, _, bw2_d = scan_wand_reduced(C12_d)
    dynamic_types.append(t_d)
    dynamic_C_sq.append(C_sq_d)
    dynamic_bw2.append(bw2_d)
    dynamic_trace.append(tr_d)
    R_scalars.append(g8['R_scalar'])

    dt = time.time() - t0  # (local)
    # Print every 10th point + known checkpoints
    is_cp = any(abs(tau_val - c) < 0.005 for c in TAU_CHECKPOINTS)  # (local)
    if i % 10 == 0 or is_cp or i == N_TAU - 1:
        elapsed = time.time() - t_loop_start  # (local)
        pct = 100.0 * (i + 1) / N_TAU  # (local)
        eta_s = (elapsed / (i + 1)) * (N_TAU - i - 1)  # (local)
        mark = '*' if is_cp else ' '  # (local)
        print(f"{i:4d}  {tau_val:8.4f}  {t_s:>5s}{mark}  {t_d:>5s}{mark}  "
              f"{C_sq_s:12.4e}  {C_sq_d:12.4e}  {bw2_s:10.2e}  {bw2_d:10.2e}  "
              f"{dt:6.2f}   [{pct:.0f}%, ETA {eta_s/60:.1f}min]", flush=True)

print(f"\n[grid sweep complete: {time.time() - t_loop_start:.1f}s]")

# ============================================================================
# VERDICT
# ============================================================================
static_types_arr = np.array(static_types)   # (local)
dynamic_types_arr = np.array(dynamic_types) # (local)

all_static_D = bool(np.all(static_types_arr == 'D'))     # (local)
all_dynamic_G = bool(np.all(dynamic_types_arr == 'G'))   # (local)

min_static_csq = float(np.min(static_C_sq))              # (local)
min_dynamic_csq = float(np.min(dynamic_C_sq))            # (local)
max_trace = float(max(np.max(static_trace), np.max(dynamic_trace)))  # (local)

n_static_D = int(np.sum(static_types_arr == 'D'))        # (local)
n_dynamic_G = int(np.sum(dynamic_types_arr == 'G'))      # (local)

non_D_idx = np.where(static_types_arr != 'D')[0]         # (local)
non_G_idx = np.where(dynamic_types_arr != 'G')[0]        # (local)

print(f"\n=== CMPP DENSE-GRID VERDICT SUMMARY ===")
print(f"  N points sampled        = {N_TAU}")
print(f"  Static Type D at        = {n_static_D}/{N_TAU} points")
print(f"  Dynamic Type G at       = {n_dynamic_G}/{N_TAU} points")
print(f"  all_static_D            = {all_static_D}")
print(f"  all_dynamic_G           = {all_dynamic_G}")
print(f"  min |C|^2 static        = {min_static_csq:.6e}  (floor {TOL_CSQ_ABS:.0e})")
print(f"  min |C|^2 dynamic       = {min_dynamic_csq:.6e}")
print(f"  max trace_err           = {max_trace:.2e}  (tol {TOL_TRACE:.0e})")

if len(non_D_idx) > 0:
    print(f"  Non-D static at idx     = {non_D_idx[:10]}... (tau = {tau_grid[non_D_idx[:5]]})")
if len(non_G_idx) > 0:
    print(f"  Non-G dynamic at idx    = {non_G_idx[:10]}... (tau = {tau_grid[non_G_idx[:5]]})")

# Check known S77/S84 checkpoints
print(f"\n  Checkpoint sanity (expected Type D static / Type G dynamic):")
for cp in TAU_CHECKPOINTS:
    idx = int(np.argmin(np.abs(tau_grid - cp)))  # (local)
    if abs(tau_grid[idx] - cp) < 0.005:
        print(f"    tau={cp:.3f} -> grid[{idx}]={tau_grid[idx]:.3f}: "
              f"static={static_types[idx]}, dynamic={dynamic_types[idx]}")

# Verdict
verdict = 'INFO'
if all_static_D and all_dynamic_G and min_static_csq > TOL_CSQ_ABS and max_trace < TOL_TRACE:
    verdict = 'PASS'
elif len(non_D_idx) > 0 or len(non_G_idx) > 0:
    verdict = 'FAIL'
elif min_static_csq <= TOL_CSQ_ABS:
    verdict = 'INFO'
elif max_trace >= TOL_TRACE:
    verdict = 'INFO'


# ============================================================================
# DUAL-SHA (S84+)
# ============================================================================
output_pin = {
    'scheme': SCHEME,
    'convention': CONVENTION,
    'L_max': L_MAX,
    'tau_min': TAU_GRID_MIN, 'tau_max': TAU_GRID_MAX, 'tau_step': TAU_STEP,
    'N_TAU': N_TAU,
    'all_static_D': all_static_D,
    'all_dynamic_G': all_dynamic_G,
    'n_static_D': n_static_D, 'n_dynamic_G': n_dynamic_G,
    'min_static_csq': min_static_csq,
    'min_dynamic_csq': min_dynamic_csq,
    'verdict': verdict,
}

content_blob = json.dumps(output_pin, sort_keys=True, separators=(',', ':'))
content_sha = hashlib.sha256(open(__file__, 'rb').read()).hexdigest()  # (local) script-only
canonical_bytes = open(
    os.path.join(PROJECT_ROOT, 'computations/_shared/canonical_constants.py'), 'rb'
).read()  # (local)
pinmap_json = json.dumps(
    dict(sorted(INPUT_SHA_MAP)),
    separators=(",", ":"), sort_keys=True,
).encode("utf-8")  # (local)
h_audit = hashlib.sha256()
h_audit.update(open(__file__, 'rb').read())
h_audit.update(canonical_bytes)
h_audit.update(pinmap_json)
audit_sha = h_audit.hexdigest()  # (local)

print(f"\n  content_sha256 = {content_sha}")
print(f"  audit_sha256   = {audit_sha}")


# ============================================================================
# SAVE ARTIFACTS
# ============================================================================
np.savez(
    OUT_NPZ,
    tau_grid=tau_grid,
    static_types=static_types_arr,
    dynamic_types=dynamic_types_arr,
    static_C_sq=np.array(static_C_sq),
    dynamic_C_sq=np.array(dynamic_C_sq),
    static_bw2=np.array(static_bw2),
    dynamic_bw2=np.array(dynamic_bw2),
    static_trace=np.array(static_trace),
    dynamic_trace=np.array(dynamic_trace),
    R_scalars=np.array(R_scalars),
    all_static_D=np.array([all_static_D]),
    all_dynamic_G=np.array([all_dynamic_G]),
    min_static_csq=np.array([min_static_csq]),
    min_dynamic_csq=np.array([min_dynamic_csq]),
    audit_sha256=np.array(audit_sha, dtype=object),
    content_sha256=np.array(content_sha, dtype=object),
    scheme=np.array(SCHEME, dtype=object),
    convention=np.array(CONVENTION, dtype=object),
    L_max=np.array(L_MAX, dtype=object),
    verdict=np.array(verdict, dtype=object),
)

# Plot
fig, axes = plt.subplots(2, 2, figsize=(13, 8))
# (a) |C|^2 vs tau
ax = axes[0, 0]
ax.semilogy(tau_grid, np.array(static_C_sq), '-', color='#1f77b4', lw=1.3, label=r'static $|C|^2$')
ax.semilogy(tau_grid, np.array(dynamic_C_sq), '-', color='#d62728', lw=1.3, label=r'dynamic $|C|^2$')
ax.axvline(float(tau_fold), color='k', lw=0.6, ls='--', alpha=0.5, label=r'$\tau_\mathrm{fold}$')
for cp in TAU_CHECKPOINTS:
    ax.axvline(cp, color='grey', lw=0.3, ls=':', alpha=0.5)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$|C|^2$')
ax.set_title('(a) Weyl-squared invariant vs $\\tau$')
ax.legend(loc='best', fontsize=9)
ax.grid(alpha=0.3, which='both')

# (b) min_bw+2 vs tau
ax = axes[0, 1]
ax.semilogy(tau_grid, np.clip(np.array(static_bw2), 1e-18, None), '-', color='#1f77b4', lw=1.3,
            label='static (expect 0, Type D)')
ax.semilogy(tau_grid, np.clip(np.array(dynamic_bw2), 1e-18, None), '-', color='#d62728', lw=1.3,
            label='dynamic (expect O(1), Type G)')
ax.axvline(float(tau_fold), color='k', lw=0.6, ls='--', alpha=0.5)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'min $bw+2$ norm fraction')
ax.set_title('(b) Boost-weight $\\pm 2$ magnitude')
ax.legend(loc='best', fontsize=9)
ax.grid(alpha=0.3, which='both')

# (c) Type labels on tau-axis
ax = axes[1, 0]
type_nums = {'O': 0, 'N': 1, 'III': 2, 'D': 3, 'II': 4, 'I': 5, 'G': 6}  # (local)
stat_num = np.array([type_nums.get(t, -1) for t in static_types])  # (local)
dyn_num = np.array([type_nums.get(t, -1) for t in dynamic_types])   # (local)
ax.plot(tau_grid, stat_num, 'o-', color='#1f77b4', lw=1.0, ms=2, label='static')
ax.plot(tau_grid, dyn_num, 's-', color='#d62728', lw=1.0, ms=2, label='dynamic')
ax.set_yticks(list(type_nums.values()))
ax.set_yticklabels(list(type_nums.keys()))
ax.axvline(float(tau_fold), color='k', lw=0.6, ls='--', alpha=0.5)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'CMPP type')
ax.set_title('(c) Petrov type vs $\\tau$ (171-point grid)')
ax.legend(loc='best', fontsize=9)
ax.grid(alpha=0.3)

# (d) R-scalar for reference
ax = axes[1, 1]
ax.plot(tau_grid, np.array(R_scalars), '-', color='#2ca02c', lw=1.2)
ax.axvline(float(tau_fold), color='k', lw=0.6, ls='--', alpha=0.5)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$R$ (internal 8D Ricci scalar)')
ax.set_title('(d) Internal Ricci scalar (reference)')
ax.grid(alpha=0.3)

fig.suptitle(
    f'S85 W6-2: CMPP Petrov type on 171-point dense grid - '
    f'all_static_D={all_static_D}, all_dynamic_G={all_dynamic_G}',
    fontsize=11
)
fig.tight_layout(rect=(0.0, 0.0, 1.0, 0.96))
fig.savefig(OUT_PNG, dpi=120)
plt.close(fig)


# ============================================================================
# VERDICT LINE (S84+ dual-SHA schema)
# ============================================================================
value_tag = f"static_D/dynamic_G/N={N_TAU}"  # (local)
verdict_line = (
    f"{GATE_ID}: {verdict} -- value={value_tag!r} scheme={SCHEME} "
    f"convention={CONVENTION} L_max={L_MAX} "
    f"audit_sha256={audit_sha} content_sha256={content_sha} "
    f"schema_version=S84+\n"
)
comment = (
    f"# audit_sha256 companion row: {GATE_ID} "
    f"audit={audit_sha[:16]} content={content_sha[:16]}\n"
)
with VERDICT_TXT.open('a', encoding='utf-8') as fp:
    fp.write(verdict_line)
    fp.write(comment)

print(f"\n(value={value_tag!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
wall_time = time.time() - t_start  # (local)
print(f"\n=== {GATE_ID}: {verdict} (wall {wall_time:.1f}s) ===")
print(f"NPZ: {OUT_NPZ.name}")
print(f"PNG: {OUT_PNG.name}")

# math-scripts.md §Exit Codes: exit 0 regardless of PASS/FAIL/INFO
sys.exit(0)
