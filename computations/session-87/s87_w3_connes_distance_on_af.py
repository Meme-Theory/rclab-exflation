#!/usr/bin/env python3
"""
S87 Workshop 3 — Connes-distance on A_F = C (+) H (+) M_3(C)
==============================================================

Companion to W1b-6 (S88-CONNES-DISTANCE-FINITE-SPECTRUM-IDENTITY-CONJECTURE).
W1b-6 closed CLASS-gamma (best_residual = 0.980) on the FULL M_n(C) algebra,
with the f(D^2)-commutant argument driving regulator-divergence d_C(R) ~ c*R
linearly across 3 OOM in R.

This script tests Workshop-3's two competing readings:

  Reading A (structural orthogonality theorem): the regulator-divergence is
  intrinsic to algebra-DEPENDENT state-pair functionals on EVERY finite
  spectral triple, including A_F. PASS-Reading-A iff d_C(R) ~ c*R linearly.

  Reading B (scope-limited closure): the W1b-6 CLASS-gamma is a feature of
  the FULL M_n(C) algebra alone. Restricting to A_F = C (+) H (+) M_3(C)
  gives a finite, well-defined Connes distance. PASS-Reading-B iff d_C(R)
  saturates to a finite value AND >= 1 of {C2, C3, C4} achieves residual
  < 1e-3 at >= 1 state-pair.

  INFO iff borderline (saturation at some R-range, divergence at others).

Pre-registration:
  Same 3 canonical state-pairs as W1b-6:
    Pair-1: vacuum (0,0) / n=0 quasi (0,1)+(1,0) lowest mode
    Pair-2: B1 acoustic min/max in (0,1) U (1,0)
    Pair-3: Cartan alpha_1 / alpha_2 in (1,1) adjoint
  Same R-sweep R in {1, 10, 100, 1000} (3 OOM)
  L_max = 12; spectrum cache s84_spectrum_cache_L12_tau019.npz
  Algebra restriction: a in pi(A_F) where pi : A_F -> M_{n_loc}(C) is the
    block-diagonal embedding C -> a*I_{4}, H -> 4-dim hermitian quaternion
    block, M_3(C) -> hermitian 3x3 block padded by zeros to 8 dims.
    Total real dimension of pi(A_F)_h: 1 + 4 + 9 = 14.

  PASS thresholds (pre-registered):
    PASS-A : R-sweep slope d/dlogR(d_C) > 0.5 across all 3 OOM AND d_C(R=1000)/d_C(R=1) > 100 (linearity test)
    PASS-B : d_C(R=1000) / d_C(R=1) < 2.0 (saturation) AND best non-definitional residual < 1e-3 at >=1 state-pair
    INFO   : neither A nor B fully satisfied (e.g., partial saturation, or finite d_C with all residuals > 1e-3)

  Output 4-tuple:
    (value=verdict_value, scheme=Connes-distance-A_F-subalgebra-restriction,
     convention=substrate-state-pair-canonical-A_F, L_max=12)

Classification: GEOMETRIC

Substitution chain (f(D^2)-commutant escape on A_F):
  Step 1 (definition): On M_n(C), for any polynomial f, f(D^2) lies in
    commutant of D (since D commutes with itself).
  Step 2 (substitution): On pi(A_F) viewed as a sub-algebra of M_n(C),
    f(D^2) lies in the commutant of D in M_n(C), but generically
    f(D^2) NOT in pi(A_F). Escape persists iff pi(A_F) intersect {commutant of D}
    contains an unbounded (non-scalar) direction.
  Step 3 (simplification): For generic D (not block-diagonal in the A_F
    decomposition), pi(A_F) intersect {f(D^2)} typically reduces to scalars
    (alpha*I via the C-summand). Only the identity-direction survives;
    f(D^2)-escape BLOCKED.
  Step 4 (direction): Whether the escape persists is EMPIRICAL —
    determined by whether D_loc commutes with non-trivial pi(A_F) elements.
    R-sweep distinguishes: PASS-A iff d_C(R) propto R; PASS-B iff finite.

DISCIPLINE
----------
- from canonical_constants import *
- All locals tagged # (local)
- cvxpy CPU SDP (small algebra: dim 14 on 16-dim Hilbert)
- Dual-SHA verdict line + 3-tuple companion (S87 schema-v2)
- SDP solver tolerance 1e-12 (CLARABEL)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 - Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 - Standard imports
# ---------------------------------------------------------------------------
import os
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

os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import hashlib
import json
import sys
import time
import warnings
from pathlib import Path

import numpy as np
import cvxpy as cp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 - Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S87"                                                        # (local)
GATE_ID = "S87-WORKSHOP3-CONNES-DISTANCE-ON-A_F"                       # (local)
SCHEME = "Connes-distance-A_F-subalgebra-restriction"                  # (local)
CONVENTION = "substrate-state-pair-canonical-A_F"                      # (local)
L_MAX = 12                                                             # (local)

# Pre-registered tolerance bands
INFO_CEILING = 1e-3            # CLASS-beta ceiling                    # (local)
PASS_THRESHOLD = 1e-9          # CLASS-alpha ceiling                   # (local)
SDP_TOL = 1e-10                # SDP solver tolerance                  # (local)
N_LOC = 16                     # state-localized subspace size         # (local)
RNG_SEED = 42                                                          # (local)

# Pre-registered R-sweep + verdict thresholds
R_SWEEP = np.array([1.0, 10.0, 100.0, 1000.0])                         # (local)
PASS_A_LINEARITY_THRESHOLD = 0.5    # d log d_C / d log R > 0.5         # (local)
PASS_A_RATIO_THRESHOLD = 100.0      # d_C(1000) / d_C(1) > 100          # (local)
PASS_B_SATURATION_THRESHOLD = 2.0   # d_C(1000) / d_C(1) < 2            # (local)

# Output destinations
OUT_NPZ = resolve_output(87, 's87_w3_connes_distance_on_af.npz')
OUT_PNG = resolve_output(87, 's87_w3_connes_distance_on_af.png')
VERDICT_TXT = resolve_output(87, 's87_gate_verdicts.txt')

SPECTRUM_CACHE = resolve_output(84, 's84_spectrum_cache_L12_tau019.npz')
CANONICAL_CONSTS = resolve_script(None, 'canonical_constants.py')
W1B6_REFERENCE_NPZ = resolve_output(87, 's87_w1b_connes_distance_finite_spectrum_identity.npz')
INPUT_FILES = [SPECTRUM_CACHE, CANONICAL_CONSTS, W1B6_REFERENCE_NPZ]


# ---------------------------------------------------------------------------
# Section 4 - SHA / dual-SHA helpers (S84+ schema)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} - input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins):
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path, canonical_path, pins):
    script_bytes = script_path.read_bytes() if script_path.exists() else b""  # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 5 - A_F = C (+) H (+) M_3(C) basis on M_{n_loc}(C)
# ---------------------------------------------------------------------------

def build_af_basis(n_loc):
    """Construct an orthonormal (Frobenius) basis for the hermitian elements
    of pi(A_F) embedded as a sub-algebra of M_{n_loc}(C).

    Decomposition of n_loc=16:
      n_loc = 4 (C-block) + 4 (H-block) + 8 (M_3-block)
    More precisely, A_F acts on its Hilbert space via:
      C -> alpha * I_4   on indices [0:4]    (1 hermitian dimension, scalar lambda)
      H -> 4-dim hermitian quaternion        on indices [4:8]
           ( q = a*I + b*i + c*j + d*k acts hermitian iff a real, (b,c,d) imaginary;
             the hermitian sub-algebra of H is 1-dim (only a*I_2 is hermitian
             over C); but H AS A REAL ALGEBRA is 4-dim. We take the full 4-dim
             real basis: I, i*sigma_x, i*sigma_y, i*sigma_z embedded in M_2(C),
             then tensor with I_2 on the 4-dim block. )
      M_3(C) -> hermitian 3x3 block          on indices [8:8+9]
                ( embeds via 9-dim hermitian basis on a 3-dim sub-block of the
                  8-dim slot, padded with 0 in the remaining 5 dimensions. )

    Total hermitian-element real dimension: 1 + 4 + 9 = 14.

    For the SDP we work over real-symmetric matrices (D is real symmetric in
    the chiral form, so a = a^* in the real-symmetric sense). The H block's
    quaternionic basis is realized as 4-dim antihermitian over R via the
    standard 4x4 real representation of unit quaternions. We adapt: take only
    the REAL-SYMMETRIC sub-basis to keep cvxpy happy. The C and M_3 blocks'
    hermitian-sub-algebras are real-symmetric over R; the H block over R is
    real-orthogonal (so its real-symmetric sub-algebra is just R*I_4). To
    preserve the RICHER quaternion structure, we use the real 4x4 quaternion
    representation:  i,j,k as real antisymmetric matrices; their product
    structure gives the hermitian-quaternion (= real-symmetric) sub-algebra
    as ONLY the identity (1-dim). For the SDP test we ENRICH with the
    symmetric off-diagonal pairs sym(e_ij) for the H block (this overshoots
    the strict A_F structure by including extra real-symmetric DOF; the
    resulting sub-algebra is at most as restrictive as {C + H_real-sym + M_3
    hermitian} = upper bound on A_F's reach).

    For unambiguous A_F-restricted testing, we instead use BLOCK-DIAGONAL
    real-symmetric on the three blocks separately:
      block-1: 4x4 real-symmetric on rows 0-3   (scalar*I = 1 dim if STRICT C
               summand; we take FULL 4x4 real-symmetric = 10 dim as a more
               permissive version, since pure C is too restrictive to test
               escape on a non-trivial 4-dim block)

    To keep the test unambiguous AND faithful to the substrate's A_F, we
    construct TWO basis sets:
      (a) STRICT: 1 (scalar*I_4) + 1 (scalar*I_4 on H block, since real-sym
          quaternions = only identity over R) + 9 (3x3 hermitian on M_3) = 11 dim
      (b) PERMISSIVE: 10 (4x4 real-sym on C block) + 10 (4x4 real-sym on H block)
          + 9 (3x3 hermitian on M_3 sub-block of 8-dim slot) = 29 dim

    The permissive set is an UPPER BOUND on what A_F can do; STRICT is the
    actual real-hermitian A_F. We run BOTH and compare:
      - if STRICT yields finite d_C across R-sweep -> A_F is genuinely finite
      - if PERMISSIVE yields divergent but STRICT yields finite -> escape
        is blocked at the strict A_F level
      - if both diverge -> structural orthogonality (Reading A) holds even
        for permissive A_F-like extensions, propagating to A_F itself

    Returns:
      strict_basis: list of n_loc x n_loc real-symmetric matrices
      permissive_basis: list of n_loc x n_loc real-symmetric matrices
    """
    if n_loc != 16:
        raise ValueError(f"This A_F basis assumes n_loc=16; got {n_loc}")

    strict = []     # (local)
    permissive = [] # (local)

    # Block ranges
    c_slc = slice(0, 4)        # C-block: 4 dims
    h_slc = slice(4, 8)        # H-block: 4 dims
    m3_slc = slice(8, 16)      # M_3-block: 8 dims (use first 3x3 sub-block)

    def _zero_mat():
        return np.zeros((n_loc, n_loc))

    # --- STRICT A_F (real-hermitian only) ---

    # C summand: scalar*I_4 on rows 0-3
    e_C = _zero_mat()
    e_C[c_slc, c_slc] = np.eye(4)
    strict.append(e_C / np.sqrt(np.trace(e_C @ e_C)))

    # H summand (real-hermitian sub-algebra): only scalar*I_4 (over R, hermitian
    # quaternions = R*I; the 3 imaginary units i,j,k are antisymmetric).
    e_H = _zero_mat()
    e_H[h_slc, h_slc] = np.eye(4)
    strict.append(e_H / np.sqrt(np.trace(e_H @ e_H)))

    # M_3(C) summand: 9-dim hermitian basis on first 3x3 of the 8-dim slot
    # (pad rest with 0). Hermitian basis: 3 real diagonal, 3 symmetric off-diag,
    # 3 antisymmetric (which are antihermitian over R but become hermitian
    # under i*antisym in C). For real-symmetric SDP we omit the antisym part
    # (it has no real-symmetric realization), keeping 3+3 = 6 real-symmetric
    # generators on M_3 sub-block + 3 zero-extension. We add the 3 antisym
    # generators as separate real-antisymmetric variables --- but cvxpy
    # symmetric=True forbids antisym. So STRICT keeps real-sym M_3 only:
    # 3 diag + 3 sym off-diag = 6 real-symmetric generators.
    # NB: this is a sub-set of the strict M_3(C) hermitian (which has 9 real DOF);
    # the i*antisymmetric part requires complex variables. We document this
    # clipping as an "M_3-real-sym sub-algebra of A_F".
    m3_dim = 3  # use 3x3 sub-block of the 8-dim M_3 slot          # (local)
    # 3 diagonal generators
    for i in range(m3_dim):
        e = _zero_mat()
        idx = 8 + i
        e[idx, idx] = 1.0
        strict.append(e)
    # 3 symmetric off-diagonal generators
    for i in range(m3_dim):
        for j in range(i + 1, m3_dim):
            e = _zero_mat()
            ii = 8 + i
            jj = 8 + j
            e[ii, jj] = 1.0 / np.sqrt(2.0)
            e[jj, ii] = 1.0 / np.sqrt(2.0)
            strict.append(e)

    # Total STRICT real-symmetric DOF: 1 (C) + 1 (H) + 3 (M_3 diag) + 3 (M_3 off) = 8

    # --- PERMISSIVE A_F (full block-diagonal real-symmetric) ---
    # 4x4 real-sym on C block: 10 dim
    for i in range(4):
        e = _zero_mat()
        e[i, i] = 1.0
        permissive.append(e)
    for i in range(4):
        for j in range(i + 1, 4):
            e = _zero_mat()
            e[i, j] = 1.0 / np.sqrt(2.0)
            e[j, i] = 1.0 / np.sqrt(2.0)
            permissive.append(e)

    # 4x4 real-sym on H block: 10 dim
    for i in range(4):
        e = _zero_mat()
        e[4 + i, 4 + i] = 1.0
        permissive.append(e)
    for i in range(4):
        for j in range(i + 1, 4):
            e = _zero_mat()
            e[4 + i, 4 + j] = 1.0 / np.sqrt(2.0)
            e[4 + j, 4 + i] = 1.0 / np.sqrt(2.0)
            permissive.append(e)

    # 3x3 real-sym on M_3 sub-block (rows 8-10): 6 dim
    for i in range(3):
        e = _zero_mat()
        e[8 + i, 8 + i] = 1.0
        permissive.append(e)
    for i in range(3):
        for j in range(i + 1, 3):
            e = _zero_mat()
            e[8 + i, 8 + j] = 1.0 / np.sqrt(2.0)
            e[8 + j, 8 + i] = 1.0 / np.sqrt(2.0)
            permissive.append(e)

    # Total PERMISSIVE real-symmetric DOF: 10 + 10 + 6 = 26

    return strict, permissive


# ---------------------------------------------------------------------------
# Section 6 - Spectrum loading + state-pair construction (mirrors W1b-6)
# ---------------------------------------------------------------------------

def load_spectrum_L12():
    d = np.load(SPECTRUM_CACHE, allow_pickle=True)  # (local)
    sec = d['sector_evals'].item()  # (local)
    flat_list = []  # (local)
    for k, v in sec.items():
        flat_list.append(np.asarray(v['abs_evals'], dtype=np.float64))
    flat_abs = np.concatenate(flat_list)  # (local)
    return sec, flat_abs


def select_state_localized_block(sector_evals, sector_keys, n_loc, rng=None):
    """Mirrors W1b-6 build: lowest-n_loc absolute eigvals from union of sectors,
    chiral D_loc = [[0, M], [M^T, 0]] with prescribed singular values.
    """
    pool_evals = []  # (local)
    for sk in sector_keys:
        if sk in sector_evals:
            pool_evals.append(np.asarray(sector_evals[sk]['abs_evals'], dtype=np.float64))
    if not pool_evals:
        return None
    pool = np.concatenate(pool_evals)  # (local)
    pool_sorted = np.sort(pool)  # (local)
    if len(pool_sorted) < n_loc:
        n_use = len(pool_sorted) - (len(pool_sorted) % 2)  # (local)
    else:
        n_use = n_loc - (n_loc % 2)  # (local)
    if n_use < 2:
        return None
    lambdas = pool_sorted[:n_use // 2]  # (local) m = n_use/2
    m = len(lambdas)  # (local)

    if rng is None:
        rng = np.random.default_rng(RNG_SEED)
    U_raw = rng.standard_normal((m, m))  # (local)
    V_raw = rng.standard_normal((m, m))  # (local)
    Q_U, _ = np.linalg.qr(U_raw)  # (local)
    Q_V, _ = np.linalg.qr(V_raw)  # (local)
    Sigma = np.diag(lambdas)  # (local)
    M = Q_U @ Sigma @ Q_V.T  # (local)

    Z = np.zeros((m, m))  # (local)
    D_loc = np.block([[Z, M], [M.T, Z]])  # (local) 2m x 2m

    return {
        'lambdas': lambdas,
        'D_loc': D_loc,
        'D_diag': np.concatenate([lambdas, -lambdas]),
        'n_loc': 2 * m,
        'M_block': M,
    }


def build_canonical_state_pairs(sector_evals):
    """Mirrors W1b-6: 3 PRE-REGISTERED state-pairs."""
    pairs = []  # (local)

    # Pair-1
    p1 = select_state_localized_block(sector_evals, [(0, 0), (0, 1), (1, 0)], N_LOC)
    if p1 is not None:
        n1 = p1['n_loc']
        p_state = np.zeros(n1); p_state[0] = 1.0  # (local)
        q_state = np.zeros(n1); q_state[1] = 1.0  # (local)
        pairs.append({
            'name': 'Pair-1: vacuum / n=0 quasi',
            'sectors': [(0, 0), (0, 1), (1, 0)],
            'D_loc': p1['D_loc'],
            'lambdas': p1['lambdas'],
            'D_diag': p1['D_diag'],
            'n_loc': n1,
            'p_state': p_state,
            'q_state': q_state,
        })

    # Pair-2
    p2 = select_state_localized_block(sector_evals, [(0, 1), (1, 0)], N_LOC)
    if p2 is not None:
        n2 = p2['n_loc']
        p_state = np.zeros(n2); p_state[0] = 1.0  # (local)
        q_state = np.zeros(n2); q_state[n2 - 1] = 1.0  # (local)
        pairs.append({
            'name': 'Pair-2: B1 acoustic min/max',
            'sectors': [(0, 1), (1, 0)],
            'D_loc': p2['D_loc'],
            'lambdas': p2['lambdas'],
            'D_diag': p2['D_diag'],
            'n_loc': n2,
            'p_state': p_state,
            'q_state': q_state,
        })

    # Pair-3
    p3 = select_state_localized_block(sector_evals, [(1, 1)], N_LOC)
    if p3 is not None:
        n3 = p3['n_loc']
        p_state = np.zeros(n3); p_state[0] = 1.0  # (local)
        q_state = np.zeros(n3); q_state[min(2, n3 - 1)] = 1.0  # (local)
        pairs.append({
            'name': 'Pair-3: Cartan alpha_1 / alpha_2',
            'sectors': [(1, 1)],
            'D_loc': p3['D_loc'],
            'lambdas': p3['lambdas'],
            'D_diag': p3['D_diag'],
            'n_loc': n3,
            'p_state': p_state,
            'q_state': q_state,
        })

    return pairs


# ---------------------------------------------------------------------------
# Section 7 - SDP on A_F sub-algebra (Connes distance with a in pi(A_F))
# ---------------------------------------------------------------------------

def connes_distance_af_sdp(D_loc, p_state, q_state, basis, sdp_tol=SDP_TOL,
                            R_regularization=None):
    """Connes distance restricted to algebra elements a = sum_i x_i * E_i
    where {E_i} is the supplied A_F basis.

      max     | <p|a|p> - <q|a|q> | = | sum_i x_i * tr(delta_rho * E_i) |
      s.t.    || [D, a] ||_op <= 1
              || a ||_F <= R                  (regulator)
              a = sum_i x_i * E_i             (A_F restriction)

    The Frobenius cap on a is included as the same regulator W1b-6 used,
    so the comparison is apples-to-apples. The structural difference is
    that a is now constrained to a low-dimensional sub-algebra.

    SDP variables: dim(basis) real scalars x_i.
    LMI of dim 2n for ||[D,a]||_op <= 1.
    """
    n = D_loc.shape[0]  # (local)
    rho_p = np.outer(p_state, p_state.conj()).real  # (local)
    rho_q = np.outer(q_state, q_state.conj()).real  # (local)
    delta_rho = (rho_p - rho_q)  # (local)

    K = len(basis)  # (local) basis dimension
    x = cp.Variable(K)  # (local) coefficients of basis expansion

    # a = sum_i x_i * E_i
    a = sum([x[i] * basis[i] for i in range(K)])  # (local) cvxpy expression

    # objective (symmetric: take both directions and pick max-magnitude)
    obj_coeffs = np.array([float(np.trace(delta_rho @ basis[i])) for i in range(K)])  # (local)
    objective_pos = cp.Maximize(obj_coeffs @ x)
    objective_neg = cp.Minimize(obj_coeffs @ x)

    # commutator = D @ a - a @ D
    commutator = D_loc @ a - a @ D_loc  # (local)

    I_n = np.eye(n)  # (local)
    lmi = cp.bmat([
        [I_n, commutator],
        [commutator.T, I_n],
    ])
    constraints = [lmi >> 0]  # (local)

    # Frobenius cap (matches W1b-6's regulator scheme)
    if R_regularization is None:
        eig_max = float(np.max(np.abs(np.linalg.eigvalsh(D_loc))))  # (local)
        R_regularization = 100.0 * eig_max
    constraints.append(cp.norm(a, 'fro') <= R_regularization)

    solver_kwargs = dict(  # (local)
        solver=cp.CLARABEL,
        tol_gap_abs=sdp_tol,
        tol_gap_rel=sdp_tol,
        tol_feas=sdp_tol,
        verbose=False,
    )

    try:
        prob_pos = cp.Problem(objective_pos, constraints)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            prob_pos.solve(**solver_kwargs)
        d_pos = float(prob_pos.value) if prob_pos.value is not None else float('nan')  # (local)
        status_pos = prob_pos.status  # (local)
    except Exception as ex:
        d_pos = float('nan')
        status_pos = f'SDP_FAIL_pos:{ex}'

    try:
        prob_neg = cp.Problem(objective_neg, constraints)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            prob_neg.solve(**solver_kwargs)
        d_neg = float(prob_neg.value) if prob_neg.value is not None else float('nan')  # (local)
        status_neg = prob_neg.status  # (local)
    except Exception as ex:
        d_neg = float('nan')
        status_neg = f'SDP_FAIL_neg:{ex}'

    if np.isnan(d_pos) and np.isnan(d_neg):
        d_C = float('nan')  # (local)
    else:
        d_C = max(abs(d_pos) if not np.isnan(d_pos) else 0.0,
                  abs(d_neg) if not np.isnan(d_neg) else 0.0)  # (local)

    return {
        'd_C': d_C,
        'd_pos': d_pos,
        'd_neg': d_neg,
        'status_pos': status_pos,
        'status_neg': status_neg,
    }


# ---------------------------------------------------------------------------
# Section 8 - Candidate identity forms (mirrors W1b-6 C2/C3/C4)
# ---------------------------------------------------------------------------

def candidate2_mellin_dirichlet_analog(D_diag, p_state, q_state):
    abs_lam = np.abs(D_diag)  # (local)
    if (abs_lam < 1e-14).any():
        abs_lam = np.where(abs_lam < 1e-14, 1e-14, abs_lam)
    coeffs = np.abs(p_state) ** 2 - np.abs(q_state) ** 2  # (local)
    alpha = 1.0  # (local)
    rhs = float(np.abs(np.sum(coeffs * abs_lam ** (-alpha))))  # (local)
    return rhs


def candidate3_commutator_norm(D_loc, p_state, q_state):
    rho_p = np.outer(p_state, p_state.conj()).real  # (local)
    rho_q = np.outer(q_state, q_state.conj()).real  # (local)
    a_pq = rho_p - rho_q  # (local)
    commutator = D_loc @ a_pq - a_pq @ D_loc  # (local)
    op_norm = float(np.linalg.norm(commutator, ord=2))  # (local)
    if op_norm < 1e-14:
        return float('inf')
    return 1.0 / op_norm


def candidate4_heat_kernel_trace(D_loc, p_state, q_state):
    n = D_loc.shape[0]  # (local)
    D_sq = D_loc @ D_loc  # (local)
    eigvals_Dsq = np.linalg.eigvalsh(D_sq)  # (local)
    if eigvals_Dsq.min() < 1e-14:
        D_inv2 = np.linalg.pinv(D_sq, hermitian=True)  # (local)
    else:
        D_inv2 = np.linalg.inv(D_sq)  # (local)
    Q_pq = np.outer(p_state, p_state.conj()).real + np.outer(q_state, q_state.conj()).real  # (local)
    trace_val = float(np.trace(Q_pq @ D_inv2).real)  # (local)
    if trace_val < 0:
        return float('nan')
    return float(np.sqrt(trace_val))


# ---------------------------------------------------------------------------
# Section 9 - Compute orchestrator
# ---------------------------------------------------------------------------

def compute():
    rng = np.random.default_rng(RNG_SEED)

    sector_evals, flat_abs = load_spectrum_L12()
    print(f"  Loaded L=12 cache: {len(sector_evals)} sectors, {len(flat_abs)} eigenvalues")
    print(f"  spectrum range: |lambda| in [{flat_abs.min():.6f}, {flat_abs.max():.6f}]")

    # Build A_F basis (n_loc=16)
    strict_basis, permissive_basis = build_af_basis(N_LOC)
    print(f"  STRICT A_F basis dim: {len(strict_basis)} (1 C + 1 H + 6 M_3-real-sym)")
    print(f"  PERMISSIVE A_F basis dim: {len(permissive_basis)} (10 C + 10 H + 6 M_3)")

    # ------------------------------------------------------------
    # Diagnostic 1: R-sweep on Pair-1 under STRICT and PERMISSIVE
    # ------------------------------------------------------------
    print("\n  -- R-sweep on Pair-1 (STRICT A_F basis) --")
    p_diag = select_state_localized_block(sector_evals, [(0, 0), (0, 1), (1, 0)], N_LOC)
    n_d = p_diag['n_loc']  # (local)
    p_st = np.zeros(n_d); p_st[0] = 1.0  # (local)
    q_st = np.zeros(n_d); q_st[1] = 1.0  # (local)

    R_sweep = R_SWEEP
    lhs_R_strict = np.zeros_like(R_sweep)  # (local)
    lhs_R_permissive = np.zeros_like(R_sweep)  # (local)
    for i_R, R_val in enumerate(R_sweep):
        sdp_s = connes_distance_af_sdp(p_diag['D_loc'], p_st, q_st,
                                        strict_basis, R_regularization=float(R_val))
        lhs_R_strict[i_R] = sdp_s['d_C']
        print(f"     [STRICT]      R={R_val:8.1f}  d_C(R) = {sdp_s['d_C']:.6e}  "
              f"d_C/R = {sdp_s['d_C']/R_val:.4f}  status_pos={sdp_s['status_pos']}")
        sdp_p = connes_distance_af_sdp(p_diag['D_loc'], p_st, q_st,
                                        permissive_basis, R_regularization=float(R_val))
        lhs_R_permissive[i_R] = sdp_p['d_C']
        print(f"     [PERMISSIVE]  R={R_val:8.1f}  d_C(R) = {sdp_p['d_C']:.6e}  "
              f"d_C/R = {sdp_p['d_C']/R_val:.4f}  status_pos={sdp_p['status_pos']}")

    # ------------------------------------------------------------
    # 3 canonical state-pairs: full table at default R (no regulator
    # saturation; lets A_F's intrinsic structure determine d_C)
    # ------------------------------------------------------------
    pairs = build_canonical_state_pairs(sector_evals)
    print(f"\n  Built {len(pairs)} canonical state pairs (PRE-REGISTERED)")

    candidate_names = [
        'C1: SDP sup-form (Connes 1996 on A_F)',
        'C2: Mellin-Dirichlet-analog Sum c_n * lambda_n^{-alpha}',
        'C3: Commutator-norm 1/||[D, rho_p - rho_q]||_op',
        'C4: Heat-kernel-trace sqrt(Tr[Q_pq * D^{-2}])',
    ]
    K = len(candidate_names)  # (local)
    J = len(pairs)  # (local)

    # We test STRICT primarily; PERMISSIVE is the upper-bound diagnostic
    lhs_per_pair_strict = np.zeros(J)         # (local)
    lhs_per_pair_permissive = np.zeros(J)     # (local)
    rhs_table = np.zeros((K, J))               # (local)
    residual_table_strict = np.zeros((K, J))   # (local)
    residual_table_permissive = np.zeros((K, J))  # (local)
    sdp_status_strict = []                     # (local)
    sdp_status_permissive = []                 # (local)

    for j, pair in enumerate(pairs):
        print(f"\n  -- Pair {j+1}: {pair['name']} (n_loc={pair['n_loc']}) --")

        # STRICT A_F SDP at default R = 100 * |lambda|_max (as W1b-6)
        sdp_s = connes_distance_af_sdp(pair['D_loc'], pair['p_state'], pair['q_state'],
                                       strict_basis)
        d_C_strict = sdp_s['d_C']  # (local)
        lhs_per_pair_strict[j] = d_C_strict
        sdp_status_strict.append((sdp_s['status_pos'], sdp_s['status_neg']))
        print(f"     LHS d_C [STRICT A_F]:      {d_C_strict:.12e}  status_pos={sdp_s['status_pos']}")

        # PERMISSIVE diagnostic
        sdp_p = connes_distance_af_sdp(pair['D_loc'], pair['p_state'], pair['q_state'],
                                       permissive_basis)
        d_C_permissive = sdp_p['d_C']  # (local)
        lhs_per_pair_permissive[j] = d_C_permissive
        sdp_status_permissive.append((sdp_p['status_pos'], sdp_p['status_neg']))
        print(f"     LHS d_C [PERMISSIVE A_F]:  {d_C_permissive:.12e}  status_pos={sdp_p['status_pos']}")

        # Candidate forms (depend only on D_loc, p_state, q_state -- same as W1b-6)
        rhs1_strict = d_C_strict  # C1 = LHS by definition
        rhs2 = candidate2_mellin_dirichlet_analog(
            pair['D_diag'], pair['p_state'], pair['q_state'])  # (local)
        rhs3 = candidate3_commutator_norm(
            pair['D_loc'], pair['p_state'], pair['q_state'])  # (local)
        rhs4 = candidate4_heat_kernel_trace(
            pair['D_loc'], pair['p_state'], pair['q_state'])  # (local)
        rhs_vals = [rhs1_strict, rhs2, rhs3, rhs4]  # (local)

        for k, rhs in enumerate(rhs_vals):
            rhs_table[k, j] = rhs
            # STRICT residuals
            if not np.isfinite(d_C_strict) or abs(d_C_strict) < 1e-15:
                residual_table_strict[k, j] = float('inf')
            else:
                residual_table_strict[k, j] = abs(rhs - d_C_strict) / abs(d_C_strict)
            # PERMISSIVE residuals
            if not np.isfinite(d_C_permissive) or abs(d_C_permissive) < 1e-15:
                residual_table_permissive[k, j] = float('inf')
            else:
                residual_table_permissive[k, j] = abs(rhs - d_C_permissive) / abs(d_C_permissive)
            print(f"     {candidate_names[k][:50]:<50} RHS={rhs:.6e} "
                  f"strict_res={residual_table_strict[k,j]:.6e} "
                  f"permissive_res={residual_table_permissive[k,j]:.6e}")

    # ------------------------------------------------------------
    # Verdict logic (PRE-REGISTERED)
    # ------------------------------------------------------------
    # PASS-A: regulator-divergence persists on STRICT A_F:
    #   d_C(R=1000) / d_C(R=1) > PASS_A_RATIO_THRESHOLD AND
    #   slope_logR > PASS_A_LINEARITY_THRESHOLD
    # PASS-B: STRICT A_F gives finite, saturated d_C:
    #   d_C(R=1000) / d_C(R=1) < PASS_B_SATURATION_THRESHOLD AND
    #   best non-definitional residual < INFO_CEILING at >= 1 state-pair

    R_min_idx = 0                       # (local)
    R_max_idx = len(R_sweep) - 1        # (local)
    if lhs_R_strict[R_min_idx] > 1e-15:
        ratio_strict = lhs_R_strict[R_max_idx] / lhs_R_strict[R_min_idx]  # (local)
    else:
        ratio_strict = float('inf')
    if lhs_R_permissive[R_min_idx] > 1e-15:
        ratio_permissive = lhs_R_permissive[R_max_idx] / lhs_R_permissive[R_min_idx]  # (local)
    else:
        ratio_permissive = float('inf')

    # log-slope across full R range (log-log regression slope)
    # only valid if all values positive
    log_slope_strict = float('nan')  # (local)
    if np.all(lhs_R_strict > 1e-15):
        log_R = np.log10(R_sweep)
        log_dC = np.log10(lhs_R_strict)
        log_slope_strict = float(np.polyfit(log_R, log_dC, 1)[0])
    log_slope_permissive = float('nan')  # (local)
    if np.all(lhs_R_permissive > 1e-15):
        log_R = np.log10(R_sweep)
        log_dC = np.log10(lhs_R_permissive)
        log_slope_permissive = float(np.polyfit(log_R, log_dC, 1)[0])

    # Best non-definitional residual on STRICT
    best_min_residual_strict = float('inf')  # (local)
    best_min_residual_idx_strict = -1  # (local)
    for k in range(1, K):  # skip C1 definitional
        finite_mask = np.isfinite(residual_table_strict[k, :])
        if finite_mask.sum() == 0:
            continue
        min_r = residual_table_strict[k, finite_mask].min()
        if min_r < best_min_residual_strict:
            best_min_residual_strict = min_r
            best_min_residual_idx_strict = k

    # Apply pre-registered verdict logic
    pass_A_ratio = (ratio_strict > PASS_A_RATIO_THRESHOLD)         # (local)
    pass_A_slope = (np.isfinite(log_slope_strict) and
                    log_slope_strict > PASS_A_LINEARITY_THRESHOLD)  # (local)
    pass_A = pass_A_ratio and pass_A_slope                          # (local)

    pass_B_saturation = (ratio_strict < PASS_B_SATURATION_THRESHOLD)  # (local)
    pass_B_residual = (best_min_residual_strict < INFO_CEILING)        # (local)
    pass_B = pass_B_saturation and pass_B_residual                     # (local)

    if pass_A and not pass_B:
        verdict_class = 'PASS-Reading-A'
        composite_top = 'PASS'
        verdict_value = float(log_slope_strict)
        sign_v = 'PASS'
        mag_v = 'PASS'
        regime_v = 'VALID'
    elif pass_B and not pass_A:
        verdict_class = 'PASS-Reading-B'
        composite_top = 'PASS'
        verdict_value = float(best_min_residual_strict)
        sign_v = 'PASS'
        mag_v = 'PASS'
        regime_v = 'VALID'
    else:
        # Neither fully satisfied OR both satisfied (impossible by construction
        # since pass_A_ratio and pass_B_saturation are mutually exclusive)
        verdict_class = 'INFO'
        composite_top = 'INFO'
        verdict_value = float(ratio_strict)
        sign_v = 'N/A'
        mag_v = 'INFO'
        regime_v = 'VALID'

    # SDP regime check
    accepted_statuses = {'optimal', 'optimal_inaccurate'}  # (local)
    sdp_all_converged_strict = all(s_pos in accepted_statuses
                                    for (s_pos, _) in sdp_status_strict)
    if not sdp_all_converged_strict:
        regime_v = 'MARGINAL'

    return {
        'value': float(verdict_value),
        'verdict_class': verdict_class,
        'composite_top': composite_top,
        'sign_verdict': sign_v,
        'magnitude_verdict': mag_v,
        'regime_verdict': regime_v,
        'pass_A': bool(pass_A),
        'pass_B': bool(pass_B),
        'ratio_strict': float(ratio_strict),
        'ratio_permissive': float(ratio_permissive),
        'log_slope_strict': float(log_slope_strict),
        'log_slope_permissive': float(log_slope_permissive),
        'lhs_R_strict': lhs_R_strict,
        'lhs_R_permissive': lhs_R_permissive,
        'R_sweep': R_sweep,
        'lhs_per_pair_strict': lhs_per_pair_strict,
        'lhs_per_pair_permissive': lhs_per_pair_permissive,
        'rhs_table': rhs_table,
        'residual_table_strict': residual_table_strict,
        'residual_table_permissive': residual_table_permissive,
        'best_min_residual_strict': float(best_min_residual_strict),
        'best_min_residual_idx_strict': int(best_min_residual_idx_strict),
        'candidate_names': candidate_names,
        'pair_names': [p['name'] for p in pairs],
        'strict_basis_dim': len(strict_basis),
        'permissive_basis_dim': len(permissive_basis),
        'flat_abs_count': int(len(flat_abs)),
        'flat_abs_min': float(flat_abs.min()),
        'flat_abs_max': float(flat_abs.max()),
        'sdp_status_strict': sdp_status_strict,
        'sdp_status_permissive': sdp_status_permissive,
    }


# ---------------------------------------------------------------------------
# Section 10 - Plot
# ---------------------------------------------------------------------------

def plot_results(result):
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    # Panel 1: R-sweep (STRICT vs PERMISSIVE vs W1b-6 FULL)
    ax = axes[0]
    R = result['R_sweep']
    ax.loglog(R, result['lhs_R_strict'], 'o-', label='STRICT A_F (1+1+6=8 dim)', color='tab:blue')
    ax.loglog(R, result['lhs_R_permissive'], 's-', label='PERMISSIVE A_F-like (10+10+6=26 dim)',
              color='tab:orange')
    # W1b-6 FULL M_n(C) baseline values from WP §2138-2147
    full_R = np.array([1.0, 10.0, 100.0, 1000.0])
    full_dC = np.array([1.4142, 11.099, 100.87, 876.23])
    ax.loglog(full_R, full_dC, '^--', label='FULL M_{16}(C) [W1b-6]', color='tab:red', alpha=0.6)
    ax.set_xlabel('R (Frobenius regulator)')
    ax.set_ylabel('d_C(R)')
    ax.set_title(f'R-sweep on Pair-1\nslope_strict={result["log_slope_strict"]:.3f}, '
                 f'ratio_strict={result["ratio_strict"]:.3e}')
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Panel 2: per-pair LHS comparison
    ax = axes[1]
    n_pairs = len(result['pair_names'])
    x_pos = np.arange(n_pairs)
    width = 0.35                        # (local)
    ax.bar(x_pos - width/2, result['lhs_per_pair_strict'], width, label='STRICT A_F')
    ax.bar(x_pos + width/2, result['lhs_per_pair_permissive'], width, label='PERMISSIVE A_F')
    ax.set_xticks(x_pos)
    ax.set_xticklabels(['P1', 'P2', 'P3'])
    ax.set_ylabel('d_C(LHS) at default R')
    ax.set_yscale('log')
    ax.set_title('LHS per state-pair')
    ax.legend()
    ax.grid(True, alpha=0.3, axis='y')

    # Panel 3: residual heatmap (STRICT)
    ax = axes[2]
    res = result['residual_table_strict']
    res_safe = np.where(np.isfinite(res), res, 1e3)
    im = ax.imshow(np.log10(res_safe + 1e-15), aspect='auto', cmap='RdYlGn_r', vmin=-5, vmax=2)
    plt.colorbar(im, ax=ax, label='log10(residual)')
    ax.set_yticks(range(len(result['candidate_names'])))
    ax.set_yticklabels([n[:30] for n in result['candidate_names']], fontsize=8)
    ax.set_xticks(range(len(result['pair_names'])))
    ax.set_xticklabels(['P1', 'P2', 'P3'])
    ax.set_title(f'STRICT A_F residual log10\nbest={result["best_min_residual_strict"]:.3e}')

    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=110)
    plt.close()
    print(f"  Plot saved: {OUT_PNG.name}")


# ---------------------------------------------------------------------------
# Section 11 - Verdict-line emission (S87 schema-v2)
# ---------------------------------------------------------------------------

def emit_verdict_line(result, audit_sha, content_sha):
    composite = result['composite_top']  # (local)
    val_str = f"{result['value']:.12e}" if not np.isnan(result['value']) else "NaN"
    canonical = (
        f"{GATE_ID}: {composite} -- value={val_str} "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} schema_version=S84+\n"
    )
    audit_short = audit_sha[:16]  # (local)
    content_short = content_sha[:16]  # (local)
    dual = (
        f"# audit_sha256_short={audit_short} content_sha256_short={content_short} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    triple = (
        f"# sign_verdict={result['sign_verdict']} "
        f"magnitude_verdict={result['magnitude_verdict']} "
        f"regime_verdict={result['regime_verdict']} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )
    with open(VERDICT_TXT, 'a', encoding='utf-8') as f:
        f.write(canonical)
        f.write(dual)
        f.write(triple)
    print(canonical, end='')
    print(dual, end='')
    print(triple, end='')


# ---------------------------------------------------------------------------
# Section 12 - Main
# ---------------------------------------------------------------------------

def main():
    t0 = time.time()
    print(f"=== {GATE_ID} ===")
    print(f"Session: {SESSION}  L_max={L_MAX}  N_loc={N_LOC}")

    pins = log_input_pins(INPUT_FILES)  # (local)
    audit_sha, content_sha = compute_dual_sha(Path(__file__), CANONICAL_CONSTS, pins)
    print(f"  audit_sha256={audit_sha[:16]}...")
    print(f"  content_sha256={content_sha[:16]}...")

    result = compute()

    print(f"\n=== Verdict construction ===")
    print(f"  pass_A: {result['pass_A']}")
    print(f"  pass_B: {result['pass_B']}")
    print(f"  ratio_strict (d_C(R=1000)/d_C(R=1)): {result['ratio_strict']:.3e}")
    print(f"  log_slope_strict: {result['log_slope_strict']:.3f}")
    print(f"  best_min_residual_strict: {result['best_min_residual_strict']:.3e}")
    print(f"  composite verdict: {result['composite_top']}")
    print(f"  verdict_class: {result['verdict_class']}")

    # Save .npz
    np_save = {  # (local)
        'value': result['value'],
        'verdict_class': result['verdict_class'],
        'composite_top': result['composite_top'],
        'sign_verdict': result['sign_verdict'],
        'magnitude_verdict': result['magnitude_verdict'],
        'regime_verdict': result['regime_verdict'],
        'pass_A': result['pass_A'],
        'pass_B': result['pass_B'],
        'ratio_strict': result['ratio_strict'],
        'ratio_permissive': result['ratio_permissive'],
        'log_slope_strict': result['log_slope_strict'],
        'log_slope_permissive': result['log_slope_permissive'],
        'R_sweep': result['R_sweep'],
        'lhs_R_strict': result['lhs_R_strict'],
        'lhs_R_permissive': result['lhs_R_permissive'],
        'lhs_per_pair_strict': result['lhs_per_pair_strict'],
        'lhs_per_pair_permissive': result['lhs_per_pair_permissive'],
        'rhs_table': result['rhs_table'],
        'residual_table_strict': result['residual_table_strict'],
        'residual_table_permissive': result['residual_table_permissive'],
        'best_min_residual_strict': result['best_min_residual_strict'],
        'best_min_residual_idx_strict': result['best_min_residual_idx_strict'],
        'candidate_names': result['candidate_names'],
        'pair_names': result['pair_names'],
        'strict_basis_dim': result['strict_basis_dim'],
        'permissive_basis_dim': result['permissive_basis_dim'],
        'flat_abs_count': result['flat_abs_count'],
        'flat_abs_min': result['flat_abs_min'],
        'flat_abs_max': result['flat_abs_max'],
        'sdp_status_strict_pos': [s[0] for s in result['sdp_status_strict']],
        'sdp_status_strict_neg': [s[1] for s in result['sdp_status_strict']],
        'sdp_status_permissive_pos': [s[0] for s in result['sdp_status_permissive']],
        'sdp_status_permissive_neg': [s[1] for s in result['sdp_status_permissive']],
        'gate_id': GATE_ID,
        'scheme': SCHEME,
        'convention': CONVENTION,
        'L_max': L_MAX,
        'audit_sha256': audit_sha,
        'content_sha256': content_sha,
    }
    np.savez(OUT_NPZ, **{k: np.asarray(v, dtype=object) if isinstance(v, list) else v
                           for k, v in np_save.items()})
    print(f"  Data saved: {OUT_NPZ.name} ({OUT_NPZ.stat().st_size} bytes)")

    plot_results(result)

    emit_verdict_line(result, audit_sha, content_sha)

    print(f"\n=== {GATE_ID} complete ===")
    print(f"  wall = {time.time() - t0:.2f} s")
    sys.exit(0)


if __name__ == '__main__':
    main()
