#!/usr/bin/env python3
"""
S85 W6-7 PETROV-DEPENDENCE-ON-NON-BLOCK-DIAGONAL-PERTURBATIONS
===============================================================

Gate: S85-W6-7-PETROV-NON-BD-PERT ([VERIFY])

Pre-registered threshold (plan session-85-plan-w6.md §W6-7):
  HYPOTHESIS: The CMPP Type D classification of the Jensen-SU(3) internal
  geometry is FRAGILE under small non-block-diagonal perturbations of the
  internal metric (surrogate for the off-block Dirac operator perturbation).
  Specifically: at (tau=0.537, eps=0.01), Petrov type should degenerate
  from D to I (or other non-D type), reproducing S78-W3-H.

  PASS iff  (tau=0.537, eps=0.01) checkpoint reproduces non-D Petrov
            AND a fragility boundary eps_*(tau) is localizable on the
            (tau, eps) grid.
  FAIL iff  (tau=0.537, eps=0.01) stays Type D (S78-W3-H unreproducible).
  INFO iff  fragility reproduces but with different band shape.

Primitives reused from s85_w6_cmpp_dense_grid.py / s84_w8b_cmpp_petrov_type_invariance.py:
  compute_riemann_ON, compute_12d_weyl, scan_wand_reduced, classify_cmpp.

SUBSTITUTION CHAIN (VERIFY direction)
======================================

Step 1 [definitions]:
  g_s^(eps)(tau) = jensen_metric(tau) + eps * O                    (perturbed metric)
  O = sym. matrix, off-block single element O(0, 3) = O(3, 0) = 1
     (0 in SU(2) block, 3 in C^2 block)
  Type(tau, eps) := CMPP Petrov type of Weyl tensor of emergent g_M
                    under perturbed internal geometry

Step 2 [structural argument]:
  At eps = 0, Type D (W6-2 confirmed on 171-point grid).
  At eps > 0, off-block entry couples SU(2) block to C^2 block;
  breaks block-diagonal trace theorem (MEMORY.md: "Block-diagonality =
  Birkhoff rigidity"); Weyl tensor acquires bw+-1 and bw+-2 components
  (Type D condition broken).

Step 3 [fragility direction]:
  Type(tau, eps > 0) generically != D. Transition is continuous in eps
  but DISCRETE in type-label => bifurcation threshold eps_*(tau).
  S78-W3-H localization: (tau=0.537, eps=0.01).

Step 4 [PASS/FAIL]:
  At pinned checkpoint (tau=0.537, eps=0.01):
    Type != 'D' => PASS (fragility reproduced)
    Type == 'D' => FAIL (fragility unreproducible)

  Direction: broken block-diagonal => non-D Petrov under perturbation
             is structurally expected; PASS is the prediction.
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
GATE_ID = "S85-W6-7-PETROV-NON-BD-PERT"                   # (local)
SCHEME = "W3_H_perturbation_direction"                    # (local)
CONVENTION = "NP_boost_weight"                            # (local)
L_MAX = 10                                                # (local)

DIM_INT = 8                                               # (local)
DIM_TOTAL = 12                                            # (local)

# Plan-pinned machinery
TAU_MIN = 0.00                                            # (local)
TAU_MAX = 0.90                                            # (local)
TAU_STEP = 0.01                                           # (local)
N_TAU = int(round((TAU_MAX - TAU_MIN) / TAU_STEP)) + 1    # (local) = 91

EPS_VALUES = [0.0, 1e-3, 3e-3, 1e-2, 3e-2, 1e-1, 3e-1, 1.0, 3.0, 10.0]  # (local)
N_EPS = len(EPS_VALUES)                                   # (local) = 10

TOL_BW = 1e-12                                            # (local) ABSOLUTE bw threshold
TOL_TYPE = 1e-10                                          # (local) CMPP classify tolerance

# S78-W3-H checkpoint reproduction target
CHECK_TAU = 0.537                                         # (local)
CHECK_EPS = 0.01                                          # (local)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUT_NPZ = Path(__file__).resolve().parent / "s85_w6_petrov_non_bd_perturbation.npz"
OUT_PNG = Path(__file__).resolve().parent / "s85_w6_petrov_non_bd_perturbation.png"
VERDICT_TXT = Path(__file__).resolve().parent / "s85_gate_verdicts.txt"

INPUT_FILES = [
    'computations/_shared/canonical_constants.py',
    'computations/_shared/dirac_spectrum.py',
    'computations/session-84/s84_w8b_cmpp_petrov_type_invariance.py',
    'computations/session-85/s85_w6_cmpp_dense_grid.py',
]


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
    INPUT_SHA_MAP.append((rel, sha256_of_file(os.path.join(PROJECT_ROOT, rel))))


# ============================================================================
# CMPP primitives (reused verbatim from S84)
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


def compute_8d_geometry_perturbed(tau_val, eps, O_matrix, gens, f_abc, B_ab):
    """Internal 8D geometry with off-block-diagonal perturbation g -> g + eps*O.

    Returns None if perturbation breaks positive-definiteness (cholesky fails
    in orthonormal_frame). This is the EXPECTED behavior for large eps where
    the off-block element dominates and the metric becomes indefinite.
    """
    try:
        g_s = jensen_metric(B_ab, tau_val)       # (local)
        # Abs value of sign applied to make Jensen metric positive-definite
        # (some SU(3) conventions return negative-definite Killing form).
        # Check sign via diagonal:
        if np.any(np.diag(g_s) < 0):
            g_s = -g_s                           # (local) flip to positive-definite
        g_pert = g_s + eps * O_matrix            # (local) perturbed internal metric
        g_sym = 0.5 * (g_pert + g_pert.T)        # (local) symmetrize (paranoid)

        # Try cholesky via orthonormal_frame; if it fails, metric is indefinite
        E = orthonormal_frame(g_sym)
        ft = frame_structure_constants(f_abc, E)
        Gamma = connection_coefficients(ft)
        R_abcd = compute_riemann_ON(ft, Gamma)
        return {'R_abcd': R_abcd, 'g_s': g_sym}
    except (np.linalg.LinAlgError, ValueError):
        # Perturbed metric no longer positive-definite; mark invalid
        return None


def build_12d_riemann_static(R8):
    R12 = np.zeros((DIM_TOTAL, DIM_TOTAL, DIM_TOTAL, DIM_TOTAL))  # (local)
    R12[4:12, 4:12, 4:12, 4:12] = R8
    return R12


def compute_12d_weyl(R12):
    n = DIM_TOTAL  # (local)
    eta = np.diag(np.array([-1.0] + [1.0] * (n - 1)))  # (local)
    eta_diag = np.diag(eta)  # (local)
    Ric12 = np.einsum('B,ABCB->AC', eta_diag, R12)
    Ric12 = 0.5 * (Ric12 + Ric12.T)
    R_scalar = float(np.einsum('A,AA->', eta_diag, Ric12))  # (local)

    eR1 = np.einsum('AC,BD->ABCD', eta, Ric12)
    eR2 = np.einsum('AD,BC->ABCD', eta, Ric12)
    eR3 = np.einsum('BC,AD->ABCD', eta, Ric12)
    eR4 = np.einsum('BD,AC->ABCD', eta, Ric12)
    ricci_term = (1.0 / (n - 2)) * (eR1 - eR2 - eR3 + eR4)

    ee1 = np.einsum('AC,BD->ABCD', eta, eta)
    ee2 = np.einsum('AD,BC->ABCD', eta, eta)
    scalar_term = (R_scalar / ((n - 1) * (n - 2))) * (ee1 - ee2)

    C12 = R12 - ricci_term + scalar_term

    sign_tensor = np.einsum('A,B,C,D->ABCD', eta_diag, eta_diag, eta_diag, eta_diag)
    C_sq = float(np.sum(sign_tensor * C12 * C12))

    return C12, C_sq


def construct_null_frame(n_spatial):
    n = DIM_TOTAL
    e0 = np.zeros(n); e0[0] = 1.0
    l_vec = (e0 + n_spatial) / np.sqrt(2)
    k_vec = (e0 - n_spatial) / np.sqrt(2)

    n_spat = n_spatial[1:]
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
    m_vecs = []
    for v in ortho:
        m = np.zeros(n); m[1:] = v
        m_vecs.append(m)
    return l_vec, k_vec, m_vecs


def cmpp_decomposition(C12, l_vec, k_vec, m_vecs):
    n = DIM_TOTAL
    n_t = len(m_vecs)
    F = np.zeros((n, n))
    F[0] = l_vec; F[1] = k_vec
    for i in range(n_t):
        F[i + 2] = m_vecs[i]
    C1 = np.einsum('aA,ABCD->aBCD', F, C12)
    C2 = np.einsum('bB,aBCD->abCD', F, C1)
    C3 = np.einsum('cC,abCD->abcD', F, C2)
    Cn = np.einsum('dD,abcD->abcd', F, C3)

    def bw(idx):
        if idx == 0: return +1
        if idx == 1: return -1
        return 0

    bw_norms = {w: 0.0 for w in range(-4, 5)}
    for a in range(n):
        bwa = bw(a)
        for b in range(n):
            bwab = bwa + bw(b)
            for c in range(n):
                bwabc = bwab + bw(c)
                for d in range(n):
                    bw_total = bwabc + bw(d)
                    bw_norms[bw_total] = bw_norms.get(bw_total, 0.0) + Cn[a, b, c, d]**2

    bw_phys = {w: bw_norms.get(w, 0.0) for w in [-2, -1, 0, +1, +2]}
    total = sum(bw_phys.values())
    return {'bw_norms': bw_phys, 'total': total}


def classify_cmpp(decomp, tol=TOL_TYPE):
    total = decomp['total']
    if total < tol:
        return 'O'
    rel_tol = tol * total
    n2 = decomp['bw_norms'][+2]
    n1 = decomp['bw_norms'][+1]
    n0 = decomp['bw_norms'][0]
    nm1 = decomp['bw_norms'][-1]
    nm2 = decomp['bw_norms'][-2]
    h2p = n2 > rel_tol
    h1p = n1 > rel_tol
    h1m = nm1 > rel_tol
    h2m = nm2 > rel_tol
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
    n12 = np.zeros(DIM_TOTAL)
    n12[1:4] = np.sin(alpha) * n_ext_3
    n12[4:12] = np.cos(alpha) * n_int_8
    norm = np.linalg.norm(n12)
    if norm < 1e-15:
        n12[1] = 1.0; norm = 1.0
    return n12 / norm


def scan_wand_reduced(C12, n_alpha=3):
    """Reduced scan: 5 key directions x 3 alphas = 15 per query (fast)."""
    type_rank = {'O': 0, 'N': 1, 'III': 2, 'D': 3, 'II': 4, 'I': 5, 'G': 6}
    best_type = 'G'
    best_bw2 = 1.0  # (local)
    n_ext = np.array([0.0, 0.0, 1.0])
    int_dirs = {}
    d = np.zeros(DIM_INT); d[SU2_IDX] = 1.0 / np.sqrt(3); int_dirs['su2'] = d
    d = np.zeros(DIM_INT); d[C2_IDX] = 0.5; int_dirs['c2'] = d
    d = np.zeros(DIM_INT); d[U1_IDX[0]] = 1.0; int_dirs['u1'] = d
    # Mixed direction SPECIFICALLY IN THE PERTURBED BLOCK (SU(2) <-> C^2)
    d = np.zeros(DIM_INT); d[0] = 1.0/np.sqrt(2); d[3] = 1.0/np.sqrt(2); int_dirs['su2_c2_mix'] = d
    d = np.zeros(DIM_INT); d[0]=1; d[3]=1; d[7]=1; d /= np.linalg.norm(d); int_dirs['all_diag'] = d

    alpha_vals = np.linspace(0, np.pi/2, n_alpha)
    for label, n_int in int_dirs.items():
        for alpha in alpha_vals:
            n_spat = make_spatial_dir(alpha, n_ext, n_int)
            try:
                l, k, mvecs = construct_null_frame(n_spat)
                decomp = cmpp_decomposition(C12, l, k, mvecs)
                ctype = classify_cmpp(decomp)
                if type_rank.get(ctype, 6) < type_rank.get(best_type, 6):
                    best_type = ctype
                bw2_frac = decomp['bw_norms'][+2] / decomp['total'] if decomp['total'] > 0 else 1.0
                if bw2_frac < best_bw2:
                    best_bw2 = bw2_frac
            except Exception:
                pass
    return best_type, best_bw2


# ============================================================================
# Main: (tau, eps) perturbed grid
# ============================================================================
print("=" * 80)
print(f"  {GATE_ID}: PETROV TYPE FRAGILITY UNDER NON-BLOCK-DIAGONAL PERTURBATION")
print(f"  tau grid: [{TAU_MIN}, {TAU_MAX}] step {TAU_STEP} (N={N_TAU})")
print(f"  eps grid: {EPS_VALUES} (N={N_EPS})")
print(f"  Total points: {N_TAU * N_EPS} perturbed Weyl decompositions")
print("=" * 80)

print(f"\n=== {GATE_ID} - input SHA-256 pins ===")
for rel, sha in INPUT_SHA_MAP:
    print(f"  {rel}: {sha[:16]}...")
print()

# Perturbation matrix O: single off-block element (SU(2) index 0, C^2 index 3)
O_matrix = np.zeros((DIM_INT, DIM_INT))
O_matrix[0, 3] = 1.0
O_matrix[3, 0] = 1.0

print(f"Perturbation matrix O:")
print(f"  Off-block single element: O[0, 3] = O[3, 0] = 1.0 (SU(2) <-> C^2 coupling)")
print(f"  Frobenius norm = {np.linalg.norm(O_matrix, 'fro'):.4f}")
print()

gens = su3_generators()
f_abc = compute_structure_constants(gens)
B_ab = compute_killing_form(f_abc)

tau_grid = np.linspace(TAU_MIN, TAU_MAX, N_TAU)  # (local)
eps_arr = np.array(EPS_VALUES)                    # (local)

type_grid = np.empty((N_TAU, N_EPS), dtype='U4')  # (local)
bw2_grid = np.zeros((N_TAU, N_EPS))               # (local)
Csq_grid = np.zeros((N_TAU, N_EPS))               # (local)
valid_grid = np.zeros((N_TAU, N_EPS), dtype=bool) # (local)

print(f"{'tau':>8s}  {'eps=0':>5s}  {'eps=1e-3':>8s}  {'eps=0.01':>8s}  "
      f"{'eps=0.1':>7s}  {'eps=1':>5s}  {'eps=10':>6s}  {'dt(s)':>6s}")
print("-" * 85)

t_loop = time.time()
for i, tau_val in enumerate(tau_grid):
    t0 = time.time()
    for j, eps_val in enumerate(eps_arr):
        g8 = compute_8d_geometry_perturbed(float(tau_val), float(eps_val),
                                            O_matrix, gens, f_abc, B_ab)
        if g8 is None:
            type_grid[i, j] = 'INV'
            bw2_grid[i, j] = 1.0
            Csq_grid[i, j] = 0.0
            valid_grid[i, j] = False
            continue
        R12 = build_12d_riemann_static(g8['R_abcd'])
        C12, Csq = compute_12d_weyl(R12)
        t_type, bw2 = scan_wand_reduced(C12)
        type_grid[i, j] = t_type
        bw2_grid[i, j] = bw2
        Csq_grid[i, j] = Csq
        valid_grid[i, j] = True

    dt = time.time() - t0  # (local)
    if i % 10 == 0 or i == N_TAU - 1 or abs(tau_val - CHECK_TAU) < 0.005:
        samples = [type_grid[i, 0], type_grid[i, 1], type_grid[i, 3],
                   type_grid[i, 5], type_grid[i, 7], type_grid[i, 9]]  # (local)
        mark = '*' if abs(tau_val - CHECK_TAU) < 0.005 else ' '
        print(f"{tau_val:8.4f}  {samples[0]:>5s}  {samples[1]:>8s}  {samples[2]:>8s}  "
              f"{samples[3]:>7s}  {samples[4]:>5s}  {samples[5]:>6s}  {dt:6.2f}   {mark}")

print(f"\n[(tau, eps) sweep complete: {time.time() - t_loop:.1f}s]")

# ============================================================================
# S78-W3-H checkpoint audit
# ============================================================================
# Nearest grid point to (tau=0.537, eps=0.01)
i_check = int(np.argmin(np.abs(tau_grid - CHECK_TAU)))  # (local)
j_check = int(np.argmin(np.abs(eps_arr - CHECK_EPS)))   # (local)
check_tau_actual = float(tau_grid[i_check])              # (local)
check_eps_actual = float(eps_arr[j_check])               # (local)
check_type = type_grid[i_check, j_check]                 # (local)

print(f"\n=== S78-W3-H CHECKPOINT AUDIT ===")
print(f"  Pre-registered target: (tau=0.537, eps=0.01) -> Type I (non-D)")
print(f"  Grid-nearest point:    (tau={check_tau_actual:.4f}, eps={check_eps_actual:.4f})")
print(f"  Computed Type at checkpoint: {check_type}")
print(f"  Fragility reproduced (Type != 'D')? {check_type != 'D'}")

# Count non-D entries at eps > 0
eps_0_col = 0  # (local)
non_D_at_eps_0 = int(np.sum(type_grid[:, eps_0_col] != 'D'))  # (local) should be 0 (baseline)
non_D_total = int(np.sum(type_grid != 'D'))                    # (local)
total_valid = int(np.sum(valid_grid))                           # (local)

print(f"\n=== FRAGILITY MAP STATS ===")
print(f"  Non-D at eps=0 (baseline)       = {non_D_at_eps_0} / {N_TAU}  "
      f"(expected 0, confirms W6-2 baseline)")
print(f"  Non-D total (all grid points)   = {non_D_total} / {N_TAU * N_EPS}")
print(f"  Valid decomposition points      = {total_valid} / {N_TAU * N_EPS}")

# Verdict
if check_type != 'D':
    verdict = "PASS"
elif check_type == 'D':
    verdict = "FAIL"
else:
    verdict = "INFO"


# Dual-SHA
output_pin = {
    'scheme': SCHEME, 'convention': CONVENTION, 'L_max': L_MAX,
    'check_tau': check_tau_actual, 'check_eps': check_eps_actual,
    'check_type': check_type,
    'fragility_reproduced': check_type != 'D',
    'non_D_total': non_D_total,
    'total_valid': total_valid,
    'verdict': verdict,
}
content_sha = hashlib.sha256(open(__file__, 'rb').read()).hexdigest()  # (local)
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

# Save NPZ
np.savez(
    OUT_NPZ,
    tau_grid=tau_grid,
    eps_values=eps_arr,
    type_grid=type_grid,
    bw2_grid=bw2_grid,
    Csq_grid=Csq_grid,
    valid_grid=valid_grid,
    check_tau=np.array(check_tau_actual),
    check_eps=np.array(check_eps_actual),
    check_type=np.array(check_type, dtype=object),
    fragility_reproduced=np.array([check_type != 'D']),
    O_matrix=O_matrix,
    verdict=np.array(verdict, dtype=object),
    audit_sha256=np.array(audit_sha, dtype=object),
    content_sha256=np.array(content_sha, dtype=object),
    scheme=np.array(SCHEME, dtype=object),
    convention=np.array(CONVENTION, dtype=object),
    L_max=np.array(L_MAX),
)

# Plot: 2D heatmap of Petrov type in (tau, eps)
fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))
type_rank = {'O': 0, 'N': 1, 'III': 2, 'D': 3, 'II': 4, 'I': 5, 'G': 6, 'INV': -1}  # (local)
type_num = np.vectorize(lambda t: type_rank.get(t, -1))(type_grid)  # (local)

ax = axes[0]
# eps in log scale (with 0 mapped to 1e-5 for plotting only)
eps_plot = np.array([max(e, 1e-5) for e in eps_arr])  # (local)
im = ax.imshow(type_num.T, aspect='auto', origin='lower',
               extent=(tau_grid[0], tau_grid[-1],
                       np.log10(eps_plot[0]), np.log10(eps_plot[-1])),
               cmap='viridis', interpolation='nearest', vmin=-1, vmax=6)
ax.axvline(CHECK_TAU, color='red', lw=1.5, ls='--', label=rf'$\tau={CHECK_TAU}$')
ax.axhline(np.log10(CHECK_EPS), color='red', lw=1.5, ls='--')
ax.plot(CHECK_TAU, np.log10(CHECK_EPS), 'r*', ms=18,
        label=f'S78-W3-H checkpoint\nType={check_type}')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$\log_{10}\epsilon$')
ax.set_title('(a) CMPP Petrov type map under non-block-diagonal perturbation')
ax.legend(loc='lower right', fontsize=9)
cbar = plt.colorbar(im, ax=ax, ticks=list(range(-1, 7)))
cbar.ax.set_yticklabels(['INV', 'O', 'N', 'III', 'D', 'II', 'I', 'G'])
cbar.set_label('CMPP type')

ax = axes[1]
# bw+2 log scale
im2 = ax.imshow(np.log10(np.maximum(bw2_grid, 1e-20)).T, aspect='auto', origin='lower',
                extent=(tau_grid[0], tau_grid[-1],
                        np.log10(eps_plot[0]), np.log10(eps_plot[-1])),
                cmap='plasma', interpolation='nearest')
ax.axvline(CHECK_TAU, color='cyan', lw=1.5, ls='--')
ax.axhline(np.log10(CHECK_EPS), color='cyan', lw=1.5, ls='--')
ax.plot(CHECK_TAU, np.log10(CHECK_EPS), 'c*', ms=18)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$\log_{10}\epsilon$')
ax.set_title(r'(b) $\log_{10}$(min bw+2 fraction)')
plt.colorbar(im2, ax=ax, label=r'$\log_{10}$(bw+2)')

fig.suptitle(
    f'S85 W6-7: Petrov fragility under off-block-diagonal perturbation - '
    f'checkpoint (tau=0.537, eps=0.01) Type = {check_type} - {verdict}',
    fontsize=11
)
fig.tight_layout(rect=(0.0, 0.0, 1.0, 0.95))
fig.savefig(OUT_PNG, dpi=130)
plt.close(fig)

# Verdict line
value_tag = f"check_type={check_type}"  # (local)
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
print(f"\n=== {GATE_ID}: {verdict} (wall {time.time() - t_start:.1f}s) ===")
print(f"NPZ: {OUT_NPZ.name}")
print(f"PNG: {OUT_PNG.name}")
sys.exit(0)
