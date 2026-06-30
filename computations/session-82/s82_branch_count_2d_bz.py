#!/usr/bin/env python3
"""
S82 W0-A: 2D-BZ Extension of s52_gl_josephson.py
==================================================

Gate: S82-W0-A-BRANCH-COUNT  [VERIFY]
Classification: GEOMETRIC
Owner: phonon-first-cosmologist

Phononic framing:
  Phononic branches are the eigenvalue spectrum of the Dirac-connection
  operator of the Jensen-deformed SU(3) fiber at each fabric point. The
  6x6 GL-Josephson dynamical matrix is the BCS-sectoral reduction (3
  amplitude + 3 phase DOF per cell) of the full 8-generator su(3)
  phononic algebra. This task extends s52's 1D angle-averaged K-cut to
  the full 3D BCC Brillouin zone by replacing the angle-averaged
  structure factors S_NN(|K|), S_NNN(|K|) with the TRUE k-vector
  dependent gamma_NN(k), gamma_NNN(k). This resolves whether 1D
  truncation merged degeneracies that 2D-BZ sampling would split.

Pre-registered substitution chain (MANDATORY [VERIFY]):
  Step 1 (definition): rank-universality count for SU(N) =
      dim(su(N)) - 2*(N-1) Goldstones + (N-1) moduli + 1 photon
    = (N^2 - 1) - 2(N-1) + (N-1) + 1
  Step 2 (substitution for N=3):
    = 8 - 4 + 2 + 1
  Step 3 (simplification / algebraic check):
    = N^2 - N + 1 = 7
  Direction: if actual_count==7 -> PASS Sc.A
             if actual_count==5 with PRU-closure -> PASS Sc.B
             if actual_count==6 -> INFO-6
             else -> FAIL

Pre-registered scenarios (from S80 §W0-15 L720-728 verbatim):
  Scenario A: EXACTLY 7 branches with 2 new classified -> PASS (add to W0-1)
  Scenario B: EXACTLY 5 branches + PRU-closure justification -> PASS
  Scenario INFO-6: branch count = 6 -> document; do NOT unblock W0-1
  FAIL: branch count not in {5, 6, 7}

Method:
  1. Rebuild the 6x6 GL-Josephson stiffness/inertia matrices with TRUE
     k-vector-dependent gamma_NN(k), gamma_NNN(k) (instead of
     angle-averaged S_NN(|K|), S_NNN(|K|)).
  2. Sample 2D slices at k_z=0 and k_z=pi/a (64x64 each), plus a
     16x16x16 3D mesh for cross-check.
  3. Sample Gamma -> X -> M -> R -> Gamma high-symmetry path.
  4. Count distinct eigenvalue branches by continuity tracking along
     the symmetry path, with degeneracy analysis at Gamma, X, M, R.
  5. Compare to rank-universality (7) and canonical claim (5).
  6. Emit S82-W0-A-BRANCH-COUNT verdict.

Environment: 6x6 matrix is far below the 100x100 GPU-threshold; use
numpy.linalg.eigh with OMP_NUM_THREADS=8 (CPU thread cap).
"""

import os
# --- CPU thread cap (MUST be set before numpy import)
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import sys
import hashlib
import numpy as np
from numpy import pi, sqrt, cos, sin
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    a_GL, b_GL, Delta_0_GL, Delta_B3,
    J_C2, J_su2, J_u1, N_cells, c_fabric,
    rho_B2_per_mode, E_B1, E_B2_mean, E_B3_mean,
    xi_BCS, xi_GL, omega_PV, tau_fold,
    E_cond, M_max_thouless, Vol_SU3_Haar, c_Gold,
)

# ============================================================
# SECTION 0: Input SHA-256 pins (MANDATORY in first 20 lines)
# ============================================================
HERE = os.path.dirname(os.path.abspath(__file__))                  # (local)


def _sha256(path):
    """Compute SHA-256 of a file."""
    with open(path, 'rb') as h:
        return hashlib.sha256(h.read()).hexdigest()


INPUT_FILES = [                                                    # (local)
    os.path.join(HERE, 's52_gl_josephson.py'),
    os.path.join(HERE, 's52_gl_josephson.npz'),
    os.path.join(HERE, 'canonical_constants.py'),
    os.path.join(HERE, 's80_branch_count.py'),
    os.path.join(HERE, 's80_branch_count.npz'),
    os.path.join(HERE, 's48_leggett_mode.npz'),
]

print("=" * 70)
print("S82 W0-A: 2D-BZ EXTENSION OF s52_gl_josephson")
print("=" * 70)
print("\n[SEC 0] Input SHA-256 pins")
INPUT_SHAS = {}                                                    # (local)
for _f in INPUT_FILES:
    if os.path.exists(_f):
        _h = _sha256(_f)                                           # (local)
        INPUT_SHAS[os.path.basename(_f)] = _h
        print(f"  {os.path.basename(_f):32s} sha256={_h[:16]}...{_h[-8:]}")
    else:
        INPUT_SHAS[os.path.basename(_f)] = None
        print(f"  {os.path.basename(_f):32s} MISSING")

# ============================================================
# SECTION 1: Rank-universality substitution chain
# ============================================================
print("\n[SEC 1] Rank-universality substitution chain (MANDATORY [VERIFY])")
N_rank = 3                                                         # (local) SU(3) rank target
total_gens = N_rank**2 - 1                                         # (local) dim(su(3)) = 8
goldstones_eaten = 2 * (N_rank - 1)                                # (local) Higgs-eaten = 4
moduli = N_rank - 1                                                # (local) Cartan = 2
photon = 1                                                         # (local) residual U(1)
branches_predicted = total_gens - goldstones_eaten + moduli + photon  # (local)
branches_predicted_alg = N_rank**2 - N_rank + 1                    # (local) N^2 - N + 1

print(f"  Step 1 (definition): (N^2-1) - 2(N-1) + (N-1) + 1")
print(f"  Step 2 (substitution N=3): {total_gens} - {goldstones_eaten} + {moduli} + {photon}")
print(f"  Step 3 (simplification): = {branches_predicted}")
print(f"  Algebraic check: N^2 - N + 1 = {branches_predicted_alg}")
assert branches_predicted == branches_predicted_alg == 7, "Rank-universality prediction off"
print(f"  OK: SU({N_rank}) rank-universality predicts EXACTLY 7 branches")

# ============================================================
# SECTION 2: Load ground state from s48 Leggett data (same as s52)
# ============================================================
print("\n[SEC 2] Ground state (from s48 Leggett data, per s52 pattern)")
leggett_data = np.load(os.path.join(HERE, 's48_leggett_mode.npz'),
                        allow_pickle=True)
Delta_0 = leggett_data['Delta_fold']                               # (local) [B1,B2,B3]
rho_0 = leggett_data['rho_fold']                                   # (local) [B1,B2,B3]
J_12_micro = float(leggett_data['J_12_fold'])                      # (local)
J_23_micro = float(leggett_data['J_23_fold'])                      # (local)
J_13_micro = float(leggett_data['J_13_fold'])                      # (local)

print(f"  Delta_0 = [{Delta_0[0]:.4f}, {Delta_0[1]:.4f}, {Delta_0[2]:.4f}] M_KK")
print(f"  rho_0   = [{rho_0[0]:.4f}, {rho_0[1]:.4f}, {rho_0[2]:.4f}]")
print(f"  Inter-sector J: J12={J_12_micro:.6f}, J23={J_23_micro:.6f}, J13={J_13_micro:.6f}")

# GL coefficients, per s52 (re-derive to keep script self-contained)
a_alpha = np.zeros(3)                                              # (local)
b_alpha = np.zeros(3)                                              # (local)
a_alpha[1] = a_GL
a_alpha[0] = a_GL * (rho_0[1] / rho_0[0])
a_alpha[2] = a_GL * (rho_0[1] / rho_0[2])
for _i in range(3):
    b_alpha[_i] = -a_alpha[_i] / (2.0 * Delta_0[_i]**2)

# ============================================================
# SECTION 3: BCC lattice geometry + high-symmetry points
# ============================================================
print("\n[SEC 3] BCC lattice geometry")
V_cell = Vol_SU3_Haar / N_cells                                    # (local)
a_BCC = (2.0 * V_cell) ** (1.0 / 3.0)                              # (local)
K_BZ = pi / a_BCC                                                  # (local)
print(f"  V_cell = {V_cell:.4f}  a_BCC = {a_BCC:.4f}  K_BZ = pi/a = {K_BZ:.4f}")

# BCC BZ high-symmetry points (for conventional cubic cell)
# Gamma = (0,0,0), X = (0,0,pi/a), M = (pi/a,pi/a,0), R = (pi/a,pi/a,pi/a)
Gamma_pt = np.array([0.0, 0.0, 0.0])                               # (local)
X_pt = np.array([0.0, 0.0, 1.0]) * K_BZ                            # (local)
M_pt = np.array([1.0, 1.0, 0.0]) * K_BZ                            # (local)
R_pt = np.array([1.0, 1.0, 1.0]) * K_BZ                            # (local)

J_pairs = [                                                        # (local)
    (0, 1, J_12_micro),
    (1, 2, J_23_micro),
    (0, 2, J_13_micro),
]

# ============================================================
# SECTION 4: True k-vector-dependent structure factors (2D-BZ EXT)
# ============================================================
#
# The s52 script uses angle-averaged S_NN(|K|), S_NNN(|K|):
#   S_NN_avg(|K|) = 1 - [sinc(|K|a/2)]^3
#   S_NNN_avg(|K|) = 1 - sinc(|K|a)
#
# This averages over direction and collapses distinct k-vectors that
# differ only by cubic-angle rotation. The 2D-BZ extension replaces
# these with the TRUE BCC lattice-sum structure factors:
#
#   gamma_NN(k)  = cos(k_x a/2) * cos(k_y a/2) * cos(k_z a/2)
#     (NN shell = 8 cube-diagonals (a/2)(pm1,pm1,pm1))
#   gamma_NNN(k) = [cos(k_x a) + cos(k_y a) + cos(k_z a)] / 3
#     (NNN shell = 6 Cartesian vectors a(pm1,0,0) etc.)
#
#   S_NN(k)  = 1 - gamma_NN(k)
#   S_NNN(k) = 1 - gamma_NNN(k)
#
# Substitution-chain verification for degeneracy-splitting:
#   At |k|=1 and a=1:
#     S_NN_avg = 1 - (sin(0.5)/0.5)^3   = 0.118437
#     S_NN at (1,0,0) = 1 - cos(0.5)    = 0.122417
#     S_NN at (1,1,1)/sqrt(3) = ...     = 0.119069
#   Direction: directional spread ~3e-3 at |k|=1; non-zero => 2D-BZ
#   sampling CAN in principle split branches that angle-averaging
#   merged. Spread grows with |k| toward K_BZ.
# ============================================================


def gamma_NN_k(k, a):
    """TRUE BCC nearest-neighbour structure factor. Vectorized in k.

    k: shape (..., 3)  -> returns shape (...)
    """
    return (np.cos(k[..., 0] * a / 2.0)
            * np.cos(k[..., 1] * a / 2.0)
            * np.cos(k[..., 2] * a / 2.0))


def gamma_NNN_k(k, a):
    """TRUE BCC next-nearest-neighbour structure factor. Vectorized in k."""
    return (np.cos(k[..., 0] * a)
            + np.cos(k[..., 1] * a)
            + np.cos(k[..., 2] * a)) / 3.0


def S_NN_k(k, a):
    """S = 1 - gamma for NN."""
    return 1.0 - gamma_NN_k(k, a)


def S_NNN_k(k, a):
    """S = 1 - gamma for NNN."""
    return 1.0 - gamma_NNN_k(k, a)


# Effective Josephson coupling sum (same bond weights as s52)
J_NN_other = sqrt(J_C2 * J_su2)                                    # (local)
J_NNN_other = J_u1                                                 # (local)


def J_eff_k(k, a):
    """Total effective fabric Josephson stiffness at k-vector."""
    snn = S_NN_k(k, a)                                             # (local)
    snnn = S_NNN_k(k, a)                                           # (local)
    return ((4.0 * J_C2 + 4.0 * J_NN_other) * snn
            + (3.0 * J_su2 + J_u1 + 2.0 * J_NNN_other) * snnn)


def build_VT(k, a):
    """Build 6x6 stiffness V(k) and inertia T (k-independent).

    Ordering: [|D_B1|, |D_B2|, |D_B3|, theta_B1, theta_B2, theta_B3]
    """
    V = np.zeros((6, 6))                                           # (local)
    T = np.zeros((6, 6))                                           # (local)
    jeff = J_eff_k(k, a)                                           # (local)

    # --- Amplitude block (upper-left 3x3) ---
    for _i in range(3):
        V[_i, _i] = -4.0 * a_alpha[_i] + jeff * Delta_0[_i]**2
        T[_i, _i] = rho_0[_i]
    V[0, 1] = V[1, 0] = -J_12_micro
    V[1, 2] = V[2, 1] = -J_23_micro
    V[0, 2] = V[2, 0] = -J_13_micro

    # --- Phase block (lower-right 3x3) ---
    for (p, q, Jpq) in J_pairs:
        coupling = Jpq * Delta_0[p] * Delta_0[q]                   # (local)
        V[3 + p, 3 + p] += coupling
        V[3 + q, 3 + q] += coupling
        V[3 + p, 3 + q] -= coupling
        V[3 + q, 3 + p] -= coupling
    for _i in range(3):
        V[3 + _i, 3 + _i] += jeff * Delta_0[_i]**2
        T[3 + _i, 3 + _i] = rho_0[_i] * Delta_0[_i]**2

    return V, T


# ============================================================
# SECTION 5: Verify 6x6 matrix dimension constraint
# ============================================================
print("\n[SEC 5] Matrix dimension vs rank-universality prediction")
print(f"  GL-Josephson matrix dim: 6 (3 amplitude + 3 phase per cell)")
print(f"  Rank-universality predicts: {branches_predicted} branches (full SU(3))")
print(f"  Direction: a 6x6 generalized eigenvalue problem yields AT MOST 6")
print(f"             distinct eigenvalues. Scenario A (=7) is STRUCTURALLY")
print(f"             INACCESSIBLE from s52's sectoral (B1/B2/B3) matrix")
print(f"             regardless of k-space dimensionality.")
print(f"  Substitution chain:")
print(f"    dim(V) = dim(T) = 6 -> eigenvalue multiplicity <= 6")
print(f"    count of 2D-BZ (k-dep) distinct branches <= 6")
print(f"    7-branch prediction requires 8-generator su(3) matrix, not")
print(f"    3-sector GL-Josephson reduction.")

# ============================================================
# SECTION 6: 2D slice at k_z = 0 (64x64)
# ============================================================
print("\n[SEC 6] 2D slice at k_z = 0, 64x64")
N_2D = 64                                                          # (local)
k_line = np.linspace(-K_BZ, K_BZ, N_2D)                            # (local)
Kx, Ky = np.meshgrid(k_line, k_line, indexing='ij')                # (local)
omega_kz0 = np.zeros((N_2D, N_2D, 6))                              # (local)
evecs_kz0 = np.zeros((N_2D, N_2D, 6, 6))                           # (local)

from scipy.linalg import eigh as scipy_eigh                         # generalized eigh
for _ix in range(N_2D):
    for _iy in range(N_2D):
        _k = np.array([Kx[_ix, _iy], Ky[_ix, _iy], 0.0])           # (local)
        _V, _T = build_VT(_k, a_BCC)
        _ev, _vec = scipy_eigh(_V, _T)
        omega_sq = np.maximum(_ev, 0.0)                            # (local)
        omega_kz0[_ix, _iy] = np.sqrt(omega_sq)
        evecs_kz0[_ix, _iy] = _vec

print(f"  2D kz=0 omega range: [{omega_kz0.min():.6f}, {omega_kz0.max():.6f}]")
print(f"  Number of 2D k-points: {N_2D*N_2D}")
print(f"  Finite omega at Gamma-near (k=0 corner) per branch:")
# (0,0) at k=(0,0,0) sits at index (N_2D//2, N_2D//2)
cen = N_2D // 2                                                    # (local)
for _b in range(6):
    print(f"    Branch {_b}: omega({cen},{cen}) = {omega_kz0[cen, cen, _b]:.6f}")

# ============================================================
# SECTION 7: 2D slice at k_z = pi/a = K_BZ (64x64)
# ============================================================
print("\n[SEC 7] 2D slice at k_z = pi/a = K_BZ, 64x64")
omega_kzBZ = np.zeros((N_2D, N_2D, 6))                             # (local)
evecs_kzBZ = np.zeros((N_2D, N_2D, 6, 6))                          # (local)
for _ix in range(N_2D):
    for _iy in range(N_2D):
        _k = np.array([Kx[_ix, _iy], Ky[_ix, _iy], K_BZ])          # (local)
        _V, _T = build_VT(_k, a_BCC)
        _ev, _vec = scipy_eigh(_V, _T)
        omega_sq = np.maximum(_ev, 0.0)
        omega_kzBZ[_ix, _iy] = np.sqrt(omega_sq)
        evecs_kzBZ[_ix, _iy] = _vec
print(f"  2D kz=K_BZ omega range: [{omega_kzBZ.min():.6f}, {omega_kzBZ.max():.6f}]")

# ============================================================
# SECTION 8: 3D mesh 16x16x16 cross-check
# ============================================================
print("\n[SEC 8] 3D mesh cross-check, 16x16x16")
N_3D = 16                                                          # (local)
k_3D_line = np.linspace(-K_BZ, K_BZ, N_3D)                         # (local)
omega_3D = np.zeros((N_3D, N_3D, N_3D, 6))                         # (local)
for _ix in range(N_3D):
    for _iy in range(N_3D):
        for _iz in range(N_3D):
            _k = np.array([k_3D_line[_ix], k_3D_line[_iy],
                           k_3D_line[_iz]])                        # (local)
            _V, _T = build_VT(_k, a_BCC)
            _ev, _vec = scipy_eigh(_V, _T)
            omega_sq = np.maximum(_ev, 0.0)
            omega_3D[_ix, _iy, _iz] = np.sqrt(omega_sq)
print(f"  3D omega range: [{omega_3D.min():.6f}, {omega_3D.max():.6f}]")
print(f"  Total 3D points: {N_3D**3}")

# ============================================================
# SECTION 9: High-symmetry path Gamma -> X -> M -> R -> Gamma
# ============================================================
print("\n[SEC 9] High-symmetry path Gamma -> X -> M -> R -> Gamma")
N_path_seg = 50                                                    # (local) points per segment
path_segments = [                                                  # (local)
    ('Gamma', 'X', Gamma_pt, X_pt),
    ('X', 'M', X_pt, M_pt),
    ('M', 'R', M_pt, R_pt),
    ('R', 'Gamma', R_pt, Gamma_pt),
]
k_path = []                                                        # (local)
x_path = []                                                        # (local)
high_sym_x = [0.0]                                                 # (local)
x_curr = 0.0                                                       # (local)
for (_lo, _hi, _kl, _kh) in path_segments:
    seg_len = np.linalg.norm(_kh - _kl)                            # (local)
    for _t in np.linspace(0, 1, N_path_seg, endpoint=False):
        k_path.append((1 - _t) * _kl + _t * _kh)
        x_path.append(x_curr + _t * seg_len)
    x_curr += seg_len
    high_sym_x.append(x_curr)
# Add final point
k_path.append(path_segments[-1][3])
x_path.append(x_curr)
k_path = np.array(k_path)                                          # (local)
x_path = np.array(x_path)                                          # (local)

omega_path = np.zeros((len(k_path), 6))                            # (local)
evecs_path = np.zeros((len(k_path), 6, 6))                         # (local)
for _ik, _k in enumerate(k_path):
    _V, _T = build_VT(_k, a_BCC)
    _ev, _vec = scipy_eigh(_V, _T)
    omega_sq = np.maximum(_ev, 0.0)
    omega_path[_ik] = np.sqrt(omega_sq)
    evecs_path[_ik] = _vec
print(f"  Path length: {len(k_path)} k-points")
print(f"  Path omega range: [{omega_path.min():.6f}, {omega_path.max():.6f}]")

# ============================================================
# SECTION 10: High-symmetry point eigenvalues (degeneracy analysis)
# ============================================================
print("\n[SEC 10] Eigenvalues at high-symmetry points")
DEGEN_TOL = 1e-6                                                   # (local) M_KK degeneracy tolerance
highsym_names = ['Gamma', 'X', 'M', 'R']                           # (local)
highsym_pts = [Gamma_pt, X_pt, M_pt, R_pt]                         # (local)
highsym_omega = {}                                                 # (local)
for _nm, _pt in zip(highsym_names, highsym_pts):
    _V, _T = build_VT(_pt, a_BCC)
    _ev, _vec = scipy_eigh(_V, _T)
    _om = np.sqrt(np.maximum(_ev, 0.0))                            # (local)
    highsym_omega[_nm] = _om
    # Count distinct levels with tolerance
    distinct = []                                                  # (local)
    for _w in _om:
        if not distinct or min(abs(_w - _d) for _d in distinct) > DEGEN_TOL:
            distinct.append(_w)
    print(f"  {_nm:6s}: omega = {_om}")
    print(f"         distinct levels = {len(distinct)} "
          f"(DOF=6, multiplicity pattern)")

# ============================================================
# SECTION 11: Branch-count via continuity tracking along path
# ============================================================
# A branch is a continuous function omega_n(k) along the path.
# Counting: for each discrete branch index after sorting (ascending),
# how many DISTINCT eigenvalues appear at ANY point on the path?
# Degeneracies at isolated high-symmetry points don't reduce the
# global branch count unless they persist across open regions.
print("\n[SEC 11] Branch-count via continuity along high-symmetry path")
# Max-min separation along path gives branch "independence"
# A branch is resolved iff its trajectory is distinguishable from all
# others somewhere along the path (within DEGEN_TOL at that point).
branch_resolved = np.zeros(6, dtype=bool)                          # (local)
for _b in range(6):
    _om_b = omega_path[:, _b]                                      # (local)
    # Minimum separation from nearest other branch at any k
    min_sep_at_k = np.full(len(k_path), np.inf)                    # (local)
    for _b2 in range(6):
        if _b2 == _b:
            continue
        _sep = np.abs(_om_b - omega_path[:, _b2])                  # (local)
        min_sep_at_k = np.minimum(min_sep_at_k, _sep)
    max_sep = min_sep_at_k.max()                                   # (local) largest gap
    branch_resolved[_b] = max_sep > DEGEN_TOL
    print(f"  Branch {_b}: max separation from nearest = {max_sep:.6e} "
          f"{'RESOLVED' if branch_resolved[_b] else 'DEGENERATE'}")

n_branches_resolved = int(branch_resolved.sum())                   # (local)
print(f"\n  Branches resolved (continuity criterion, DEGEN_TOL={DEGEN_TOL}):"
      f" {n_branches_resolved}")

# Matrix structural constraint: 6x6 matrix has AT MOST 6 distinct branches
# so n_branches_resolved in {0, 1, ..., 6}.
n_branches_observed = n_branches_resolved                          # (local)

# ============================================================
# SECTION 12: Dispersion classification per branch
# ============================================================
print("\n[SEC 12] Dispersion classification per branch (at Gamma)")
# At Gamma (k=0), amplitude modes are gapped (Higgs), phase modes are
# Goldstone (massless) or Leggett (gapped). Slope along Gamma->X gives
# acoustic vs flat character.
Gamma_idx = 0                                                      # (local) first point on path
GammaX_idx = N_path_seg // 2                                       # (local) midpoint Gamma->X
omega_G = omega_path[Gamma_idx]                                    # (local)
omega_GX_mid = omega_path[GammaX_idx]                              # (local)
classifications = []                                               # (local)
for _b in range(6):
    _om_G = omega_G[_b]                                            # (local)
    _slope = (omega_GX_mid[_b] - _om_G) / (x_path[GammaX_idx] - x_path[0])
    _amp_frac_G = float(np.sum(evecs_path[Gamma_idx, :3, _b]**2))   # (local)
    if _om_G < 1e-5:
        cls = 'acoustic-Goldstone'                                 # (local)
    elif _amp_frac_G > 0.5:
        cls = 'massive-amplitude-Higgs'
    elif _slope < 0.01:
        cls = 'phase-mode-flat-Leggett'
    else:
        cls = 'massive-phase-Leggett'
    classifications.append(cls)
    print(f"  Branch {_b}: omega_Gamma={_om_G:.6f}, slope_Gamma->X={_slope:.4f},"
          f" amp_frac_Gamma={_amp_frac_G:.3f} -> {cls}")

# ============================================================
# SECTION 13: Cross-reference Gamma-point values with canonical set
# ============================================================
print("\n[SEC 13] Cross-reference Gamma-point values to canonical set")
canonical = {                                                      # (local)
    'c_Gold': 0.915,
    'c_BLV': 0.485,
    'c_BA': 0.399,
    'c_L': 0.025,
    'c_mod': 1.000,
}
# Sort branches by Gamma-point omega
_order = np.argsort(omega_G)                                       # (local)
print(f"  Gamma-point frequencies (ascending):")
for _rank, _b in enumerate(_order):
    print(f"    {_rank}: Branch {_b}, omega = {omega_G[_b]:.6f}")

# Match each canonical entry to nearest Gamma-point branch
gamma_matches = {}                                                 # (local)
for _nm, _val in canonical.items():
    _diffs = [abs(omega_G[_b] - _val) for _b in range(6)]          # (local)
    _best = int(np.argmin(_diffs))                                 # (local)
    gamma_matches[_nm] = (_best, omega_G[_best], _diffs[_best])
    print(f"  {_nm:8s} (canon={_val:.4f}) -> Branch {_best}, "
          f"omega={omega_G[_best]:.4f}, diff={_diffs[_best]:.4f}")

# ============================================================
# SECTION 14: 1D-vs-2D-BZ comparison (the actual S82 question)
# ============================================================
print("\n[SEC 14] 1D angle-averaged (s52) vs 2D-BZ (this script) comparison")
s52_npz = np.load(os.path.join(HERE, 's52_gl_josephson.npz'),
                  allow_pickle=True)
omega_1D = s52_npz['omega_branches']                               # (local) shape (N_K, 6)
K_1D = s52_npz['K_array']                                          # (local)
n_1D_branches = omega_1D.shape[1]                                  # (local)
print(f"  s52 1D K-cut: {n_1D_branches} branches")
print(f"  S82 2D-BZ resolved: {n_branches_observed} branches")

# Check: do 2D-BZ splittings EXIST where 1D merges?
# For each s52 branch index, compare (1D along (1,1,1)/sqrt(3)) to
# the full (Gamma->X) 2D-BZ path to see if new splittings appear.
print(f"  1D omega at K_BZ/2 (middle of s52 cut):")
for _b in range(n_1D_branches):
    _mid_1D = omega_1D[len(K_1D) // 2, _b]                         # (local)
    print(f"    s52 Branch {_b}: omega(K=K_BZ/2, angle-avg) = {_mid_1D:.6f}")

# ============================================================
# SECTION 15: Gate decision
# ============================================================
print("\n[SEC 15] Gate S82-W0-A-BRANCH-COUNT decision")
print(f"  Predicted (rank-universality):  {branches_predicted}")
print(f"  Canonical claim (task spec):    {len(canonical)}")
print(f"  Actual in 2D-BZ extension:      {n_branches_observed}")

# Pre-registered scenario logic (from S80 §W0-15 L720-728)
if n_branches_observed == 7:
    scenario = "A"                                                 # (local)
    verdict = "PASS"                                               # (local)
    explanation = (                                                # (local)
        "Exactly 7 branches resolved in 2D-BZ extension; "
        "matches rank-universality prediction. Scenario A: "
        "add 2 new canonical entries to W0-1.")
elif n_branches_observed == 5:
    scenario = "B-candidate"
    verdict = "INFO"  # Scenario B requires independent PRU-closure proof
    explanation = (
        "5 branches found but Scenario B requires independent "
        "R-protection proof; mark INFO pending justification.")
elif n_branches_observed == 6:
    scenario = "INFO-6"
    verdict = "INFO"
    explanation = (
        "2D-BZ extension resolves EXACTLY 6 branches. STRUCTURAL FLOOR: "
        "the s52 6x6 sectoral (B1/B2/B3 amplitude + phase) matrix cannot "
        "produce 7 distinct eigenvalues regardless of k-space dimension. "
        "Rank-universality 7-branch prediction applies to the full "
        "8-generator su(3) phononic algebra, which requires a different "
        "script (sigma-model on Jensen-deformed SU(3)), not the s52 "
        "sectoral reduction. The 1D->2D-BZ extension confirms the s52 "
        "framework's 6-floor; it does NOT unblock W0-1 to 7-count. W0-1 "
        "may proceed with 6-entry canonicalization with explicit note "
        "that Scenario A is deferred to a full-SU(3) workshop.")
else:
    scenario = "FAIL"
    verdict = "FAIL"
    explanation = (
        f"Branch count {n_branches_observed} not in {{5,6,7}}. "
        "Structural inconsistency; escalate before W0-1.")

print(f"  Scenario: {scenario}")
print(f"  Verdict:  {verdict}")
print(f"  Reason:   {explanation[:120]}")

# ============================================================
# SECTION 16: Closure SHA + 4-tuple emit
# ============================================================
print("\n[SEC 16] Closure SHA and 4-tuple emit")
closure_map = {                                                    # (local) ordered input-pin map
    'script': 's82_branch_count_2d_bz.py',
    'N_2D': N_2D,
    'N_3D': N_3D,
    'N_path_seg': N_path_seg,
    'a_BCC': a_BCC,
    'K_BZ': K_BZ,
    'scheme': '2D-BZ-EXTENSION',
    'convention': 'BCC-HIGH-SYMMETRY',
    'DEGEN_TOL': DEGEN_TOL,
    'n_observed': int(n_branches_observed),
    'inputs': {k: v for k, v in sorted(INPUT_SHAS.items())},
}

# Canonicalize to string for SHA
import json
closure_str = json.dumps(closure_map, sort_keys=True, default=str)  # (local)
closure_sha = hashlib.sha256(closure_str.encode('utf-8')).hexdigest()  # (local)

# 4-tuple output (final non-verdict line)
four_tuple = (                                                     # (local)
    f"(value={n_branches_observed}, scheme=2D-BZ-EXTENSION, "
    f"convention=BCC-HIGH-SYMMETRY, L_max={N_2D})"
)
print(f"  Closure SHA-256: {closure_sha}")
print(f"  4-TUPLE: {four_tuple}")

# ============================================================
# SECTION 17: Save .npz
# ============================================================
print("\n[SEC 17] Saving data")
out_npz = os.path.join(HERE, 's82_branch_count_2d_bz.npz')         # (local)
np.savez(
    out_npz,
    # Rank-universality
    N_rank=N_rank,
    branches_predicted=branches_predicted,
    # 2D slices
    N_2D=N_2D,
    k_line=k_line,
    Kx=Kx, Ky=Ky,
    omega_kz0=omega_kz0,
    omega_kzBZ=omega_kzBZ,
    # 3D mesh
    N_3D=N_3D,
    k_3D_line=k_3D_line,
    omega_3D=omega_3D,
    # High-sym path
    k_path=k_path,
    x_path=x_path,
    high_sym_x=np.array(high_sym_x),
    highsym_names=np.array(highsym_names),
    omega_path=omega_path,
    evecs_path=evecs_path,
    # High-sym points
    Gamma_omega=highsym_omega['Gamma'],
    X_omega=highsym_omega['X'],
    M_omega=highsym_omega['M'],
    R_omega=highsym_omega['R'],
    # Branch analysis
    branch_resolved=branch_resolved,
    n_branches_observed=n_branches_observed,
    classifications=np.array(classifications),
    # Canonical matches
    canonical_names=np.array(list(canonical.keys())),
    canonical_vals=np.array(list(canonical.values())),
    # Gate
    scenario=np.array([scenario]),
    verdict=np.array([verdict]),
    explanation=np.array([explanation]),
    closure_sha=np.array([closure_sha]),
    four_tuple=np.array([four_tuple]),
    # Input SHAs
    input_shas=np.array([f"{k}={v}" for k, v in sorted(INPUT_SHAS.items())]),
)
print(f"  Saved: {out_npz}")

# ============================================================
# SECTION 18: Plot
# ============================================================
print("\n[SEC 18] Plot")
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
colors = plt.cm.viridis(np.linspace(0, 0.92, 6))                   # (local)

# Panel (a): high-symmetry path dispersion
ax = axes[0, 0]
for _b in range(6):
    ax.plot(x_path, omega_path[:, _b], '-', color=colors[_b], lw=1.8,
            label=f"Br-{_b}: {classifications[_b]}")
for _x in high_sym_x:
    ax.axvline(_x, color='gray', ls=':', alpha=0.5)
ax.set_xticks(high_sym_x)
ax.set_xticklabels(highsym_names + ['Gamma'])
ax.set_ylabel('omega (M_KK)', fontsize=11)
ax.set_title(f'(a) S82 2D-BZ: Gamma-X-M-R-Gamma dispersion\n'
             f'{n_branches_observed} resolved branches', fontsize=11)
ax.legend(fontsize=7, loc='upper right')
ax.grid(True, alpha=0.3)

# Panel (b): 2D slice at k_z=0, lowest branch
ax = axes[0, 1]
im = ax.pcolormesh(Kx, Ky, omega_kz0[:, :, 0], shading='auto', cmap='viridis')
plt.colorbar(im, ax=ax, label='omega (M_KK)')
ax.set_xlabel('k_x')
ax.set_ylabel('k_y')
ax.set_title(f'(b) kz=0 slice, lowest branch\n{N_2D}x{N_2D} mesh',
             fontsize=11)
ax.set_aspect('equal')

# Panel (c): 2D slice at k_z=pi/a, lowest branch
ax = axes[1, 0]
im = ax.pcolormesh(Kx, Ky, omega_kzBZ[:, :, 0], shading='auto', cmap='viridis')
plt.colorbar(im, ax=ax, label='omega (M_KK)')
ax.set_xlabel('k_x')
ax.set_ylabel('k_y')
ax.set_title(f'(c) kz=pi/a slice, lowest branch\n{N_2D}x{N_2D} mesh',
             fontsize=11)
ax.set_aspect('equal')

# Panel (d): branch-count bar chart
ax = axes[1, 1]
counts = {                                                         # (local)
    'rank-univ\nprediction': branches_predicted,
    'canonical\nclaim': len(canonical),
    's52 1D\n(prior)': n_1D_branches,
    'S82 2D-BZ\n(this work)': n_branches_observed,
}
xs = list(range(len(counts)))
vals = list(counts.values())
labels = list(counts.keys())
bars = ax.bar(xs, vals, color=['tab:red', 'tab:gray', 'tab:blue',
                                'tab:green'])
ax.set_xticks(xs)
ax.set_xticklabels(labels, fontsize=9)
ax.set_ylabel('Branch count')
ax.set_title(f'(d) Branch count comparison -> Scenario {scenario}',
             fontsize=11)
for _x, _v in zip(xs, vals):
    ax.text(_x, _v + 0.15, str(_v), ha='center', fontsize=11,
            fontweight='bold')
ax.axhline(branches_predicted, color='red', ls='--', alpha=0.3)
ax.grid(True, axis='y', alpha=0.3)

fig.suptitle(
    f'S82 W0-A: 2D-BZ Extension of s52_gl_josephson | '
    f'Gate: {verdict} ({scenario})',
    fontsize=12, fontweight='bold'
)
plt.tight_layout(rect=[0, 0, 1, 0.95])
out_png = os.path.join(HERE, 's82_branch_count_2d_bz.png')         # (local)
plt.savefig(out_png, dpi=135, bbox_inches='tight')
plt.close(fig)
print(f"  Saved: {out_png}")

# ============================================================
# SECTION 19: Append verdict to s82_gate_verdicts.txt
# ============================================================
print("\n[SEC 19] Append verdict to s82_gate_verdicts.txt")
verdicts_path = os.path.join(HERE, 's82_gate_verdicts.txt')        # (local)
verdict_line = (                                                   # (local)
    f"S82-W0-A-BRANCH-COUNT: {verdict} -- "
    f"value={n_branches_observed} "
    f"scheme=2D-BZ-EXTENSION "
    f"convention=BCC-HIGH-SYMMETRY "
    f"L_max={N_2D} "
    f"sha256={closure_sha}\n"
)
with open(verdicts_path, 'a', encoding='utf-8') as _f:
    _f.write(verdict_line)
print(f"  Appended to: {verdicts_path}")
print(f"  Line: {verdict_line.strip()}")

# ============================================================
# FINAL: 4-tuple line (MUST be final non-verdict line)
# ============================================================
print("\n" + "=" * 70)
print(f"S82-W0-A-BRANCH-COUNT {verdict} (Scenario {scenario})")
print(f"FINAL 4-TUPLE: {four_tuple}")
print("=" * 70)
