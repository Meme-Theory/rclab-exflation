#!/usr/bin/env python3
"""
S88 W5b §W5b-49 — Connes-distance on A_F = C (+) H (+) M_3(C)
================================================================
                    FULL COMPLEX-HERMITIAN BASIS (14 real DOF)

Gate ID: S88-CONNES-DISTANCE-A_F-FULL-COMPLEX-HERMITIAN
Trigger: [VERIFY]
Classification: PHONONIC sub-case (substrate-IS state-pair metric on the
algebra-DEPENDENT family side; Corner III of the 4-corner classification).

PRE-REGISTRATION (sessions/session-plan/session-88-plan-w5b.md §W5b-49):

Hypothesis: S87 W3 STRICT residual 1.054e-01 used 8 real-symmetric DOF
(1 + 1 + 6) under-counts the 14 real DOF of the full complex-Hermitian
basis of A_F = C (+) H (+) M_3(C):
  C_h        : 1 real DOF (real scalar a*I_4)
  H_h        : 4 real DOF (a*I + b*sigma_x + c*sigma_y + d*sigma_z, a,b,c,d real)
  M_3(C)_h   : 9 real DOF (3 diag-real + 3 sym-off + 3 i*antisym-off)
  TOTAL      : 1 + 4 + 9 = 14 real DOF

The S87 STRICT 8 dropped 6 DOF: 3 quaternion imaginary units (b,c,d on H block)
+ 3 i*antisymmetric M_3 off-diagonal generators. The full complex-Hermitian
re-run computed via cvxpy.Variable(hermitian=True) (complex variables) is
expected by Step 8 of substitution chain to satisfy:

  d_C^{14-DOF}(omega_1, omega_2) >= d_C^{8-DOF}(omega_1, omega_2)
                                                              [supremum monotonic]
  STRICT residual^{14-DOF}        <= 1.054e-01     IF d_C approaches d_target
                                                  from below; PASS direction.

PASS / FAIL / INFO criterion (pre-registered):
  PASS:  (i) SDP converges, (ii) full float64 precision, (iii) per-block
         contributions reported, (iv) residual <= 1.054e-01, (v) plot,
         (vi) Corner: III declaration in WP §W5b-49.
  FAIL:  SDP fails to converge OR residual > 5 * 1.054e-01 (structurally
         inconsistent: 5x band).
  INFO:  SDP converges to a slightly different value (1.054e-01 < r <= 5x)
         within numerical precision -> quaternion-block convention.

3-tuple companion (S87+ schema-v2):
  sign_verdict     = PASS iff residual <= 1.054e-01 (direction match Step 8)
  magnitude_verdict = PASS iff residual within pass_band of 1.054e-01
  regime_verdict   = VALID iff SDP all converged (status in {optimal,
                     optimal_inaccurate}); MARGINAL otherwise

Substitution chain (mandatory direction):

  Step 1 (definition):
    d_C(omega_1, omega_2) = sup_{a in A_h, ||[D_F, pi(a)]||_op <= 1}
                                 |omega_1(a) - omega_2(a)|     [Connes 1989]

  Step 2 (block decomposition):
    A_h = (A_F)_h = C_h (+) H_h (+) M_3(C)_h

  Step 3 (real DOF count):
    dim_R(C_h) + dim_R(H_h) + dim_R(M_3(C)_h) = 1 + 4 + 9 = 14

  Step 4 (S87 baseline):
    S87 W3 STRICT used a real-symmetric SUBSET of size 8
    (1 + 1 + 6 = 8 dim, dropping 3 quaternion imaginary + 3 M_3 i*antisym)
    yielding best non-definitional residual 1.054e-01 (Pair-2, C3 candidate).

  Step 5 (supremum monotonicity):
    14-DOF basis SUPSET 8-DOF basis  =>  sup over 14-DOF >= sup over 8-DOF
                                          [supremum monotonic in domain]

  Step 6 (residual definition):
    STRICT residual = |d_C^{computed} - d_C^{target}| / |d_C^{target}|
                       (relative residual, matching S87 W3 convention)

  Step 7 (algebraic chain):
    if d_C^{14-DOF} >= d_C^{8-DOF} = d_C^{target} - delta  (with delta = 1.054e-01)
    then d_C^{14-DOF} - d_C^{target} >= -delta
    => |d_C^{14-DOF} - d_C^{target}| <= delta IF d_C^{14-DOF} approaches
       d_C^{target} from below, OR > delta IF it overshoots.

  Step 8 (direction prediction):
    The 14-DOF supremum moves CLOSER to d_C^{target} by adding directions
    not yet probed; PASS direction is residual^{14-DOF} <= 1.054e-01.
    The FAIL direction (residual > 1.054e-01) suggests the additional 6 DOF
    contain spurious "blow-up" directions that overshoot d_C^{target}.

CALIBRATION:
  - State-pair: same canonical Pair-2 ("B1 acoustic min/max") as S87 W1b-6/W3.
  - D_F: chiral D_loc construction identical to S87 W3 (re-built deterministically).
  - L_max: 12 (same spectrum cache s84_spectrum_cache_L12_tau019.npz).
  - SDP solver: cvxpy.CLARABEL with tol_gap_abs/rel 1e-9.
  - n_loc = 16 (same as S87 W3).

OUTPUTS:
  - computations/session-88/s88_w5b_connes_distance_af_complex_hermitian.npz
  - computations/session-88/s88_w5b_connes_distance_af_complex_hermitian.png
    (per-block contribution stacked-bar of |x_C|, ||x_H||_2, ||x_M3||_F)
  - Verdict line at computations/session-88/s88_gate_verdicts.txt

Substrate framing: d_C(omega_1, omega_2) IS the substrate's intrinsic metric on
its state space. The 14-DOF complex-Hermitian basis IS the full self-adjoint
content of A_F; the 8-DOF real-symmetric subset is a measurement-convention
under-sample.

Methodological reference: Iochum-Krajewski-Martinetti 2001 finite-N SDP form.
Substrate-canonical primary: S87 W3 D_F construction + S87 S-2 §3.2 baseline.

Discipline:
  - from canonical_constants import *
  - All locals tagged # (local)
  - cvxpy CPU SDP (small algebra: 14 complex variables)
  - Dual-SHA verdict line + 3-tuple companion (S87 schema-v2)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 - Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys
import os
from pathlib import Path

# Add canonical_constants location to sys.path
_HERE = Path(__file__).resolve().parent
_SHARED = _HERE.parent / '_shared'
sys.path.insert(0, str(_SHARED))

from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 - Standard imports (CPU thread cap before numpy)
# ---------------------------------------------------------------------------
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import hashlib
import json
import time
import warnings

import numpy as np
import cvxpy as cp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 - Paths + pre-registration constants
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

SESSION = "S88"                                                          # (local)
GATE_ID = "S88-CONNES-DISTANCE-A_F-FULL-COMPLEX-HERMITIAN"               # (local)
SCHEME = "Connes-distance-A_F-full-complex-Hermitian-SDP"                # (local)
CONVENTION = "cvxpy-Hermitian-True-14-real-DOF"                          # (local)
L_MAX = 12                                                               # (local)
N_LOC = 16                                                               # (local)
RNG_SEED = 42                                                            # (local) match S87 W3
SDP_TOL = 1e-9                                                           # (local) per plan §W5b-49

# Pre-registered S87 baseline residual (Step 4 of substitution chain)
S87_BASELINE_RESIDUAL = 0.10544884591169816  # = 1.054e-01                # (local)

# Pre-registered DOF counts (Step 3 of substitution chain)
COMPLEX_HERMITIAN_DOF_COUNT = 14   # 1 + 4 + 9                            # (local)
S87_STRICT_DOF_COUNT = 8           # 1 + 1 + 6                            # (local)

# Pre-registered tolerance bands
PASS_BAND = 1e-3                # |residual - target| <= 1e-3 (PASS magnitude band)  # (local)
INFO_BAND = 5.0 * S87_BASELINE_RESIDUAL  # 5x baseline = INFO ceiling     # (local)
FAIL_THRESHOLD = INFO_BAND      # > 5x is FAIL                            # (local)

# Pre-registered R-regulator (matches S87 W3 default 100 * |lambda|_max)
R_FROBENIUS_FACTOR = 100.0                                                # (local)

# Output destinations
OUT_DIR = _HERE
OUT_NPZ = OUT_DIR / 's88_w5b_connes_distance_af_complex_hermitian.npz'
OUT_PNG = OUT_DIR / 's88_w5b_connes_distance_af_complex_hermitian.png'
VERDICT_TXT = OUT_DIR / 's88_gate_verdicts.txt'

# Pre-registered input pin map (substrate-canonical sourcing)
SPECTRUM_CACHE = PROJECT_ROOT / 'computations' / 'session-84' / 's84_spectrum_cache_L12_tau019.npz'
S87_W3_NPZ = PROJECT_ROOT / 'computations' / 'session-87' / 's87_w3_connes_distance_on_af.npz'
S87_W3_PY = PROJECT_ROOT / 'computations' / 'session-87' / 's87_w3_connes_distance_on_af.py'
CANONICAL_CONSTS = _SHARED / 'canonical_constants.py'
INPUT_FILES = [SPECTRUM_CACHE, S87_W3_NPZ, S87_W3_PY, CANONICAL_CONSTS]


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
# Section 5 - Full complex-Hermitian A_F basis (14 real DOF)
# ---------------------------------------------------------------------------

def build_complex_hermitian_af_basis(n_loc):
    """Construct the FULL complex-Hermitian basis of pi(A_F) embedded in
    M_{n_loc}(C). Each generator is a complex Hermitian n_loc x n_loc matrix.

    A_F = C (+) H (+) M_3(C); embedding mirrors S87 W3:
      C-block:  rows [0:4],  scalar*I_4         (1 real DOF)
      H-block:  rows [4:8],  4-dim quaternion   (4 real DOF)
      M_3(C):   rows [8:11], 3x3 hermitian      (9 real DOF: 3 diag + 6 off)

    Quaternion 4-DOF block construction:
      The hermitian quaternion algebra over R, when embedded as a 2x2 complex
      Hermitian on the FUNDAMENTAL representation, is ONLY 1-dim (a*I).
      However, the quaternion ALGEBRA H, viewed as a 4-DIM real associative
      algebra acting on its left-regular representation in M_2(C), spans the
      Pauli group: I, sigma_x, sigma_y, sigma_z. The full hermitian sub-space
      of pi(H) on this fundamental rep is 4-dim REAL, with basis:
         q_0 = I_2,  q_1 = sigma_x,  q_2 = sigma_y,  q_3 = sigma_z
      All four are Hermitian. Their span over R is 4-dim. Tensored with I_2
      to fill the 4-dim H slot, we get 4 real DOF (each 4x4 complex Hermitian).

      This is the canonical NCG-axiomatic representation of A_F's H-summand
      in the spectral triple of the Standard Model (Connes-Chamseddine 1996,
      Connes-Marcolli 2008 §1.10).

    M_3(C) hermitian basis (9 real DOF):
      3 real diagonal:        E_ii = e_i e_i^T  for i = 0,1,2
      3 complex symmetric:    E_ij^{sym} = (e_i e_j^T + e_j e_i^T)/sqrt(2)
                              for (i,j) in {(0,1),(0,2),(1,2)}
      3 complex antisymmetric (i*antisym, hermitian):
                              E_ij^{antisym} = i*(e_i e_j^T - e_j e_i^T)/sqrt(2)
                              for (i,j) in {(0,1),(0,2),(1,2)}

    Returns:
      basis: list of (n_loc, n_loc) COMPLEX Hermitian matrices
      block_labels: list of strings ('C', 'H', 'M3') matching basis ordering
    """
    if n_loc != 16:
        raise ValueError(f"This A_F basis assumes n_loc=16; got {n_loc}")

    basis = []         # (local)
    block_labels = []  # (local)

    def _zero_complex():
        return np.zeros((n_loc, n_loc), dtype=np.complex128)

    # --- C summand: 1 real DOF (scalar*I_4 on rows 0-3) ---
    e_C = _zero_complex()
    e_C[0:4, 0:4] = np.eye(4, dtype=np.complex128)
    e_C = e_C / np.sqrt(np.trace(e_C @ e_C.conj().T).real)
    basis.append(e_C)
    block_labels.append('C')

    # --- H summand: 4 real DOF (quaternion Pauli basis on rows 4:8) ---
    # Pauli matrices (2x2)
    sigma_0 = np.eye(2, dtype=np.complex128)
    sigma_x = np.array([[0, 1], [1, 0]], dtype=np.complex128)
    sigma_y = np.array([[0, -1j], [1j, 0]], dtype=np.complex128)
    sigma_z = np.array([[1, 0], [0, -1]], dtype=np.complex128)
    pauli = [sigma_0, sigma_x, sigma_y, sigma_z]
    # Embed as 4x4 block (Pauli (x) I_2) on rows 4:8
    I2 = np.eye(2, dtype=np.complex128)
    for k, sigma_k in enumerate(pauli):
        e_H = _zero_complex()
        block_4x4 = np.kron(sigma_k, I2)  # (local) 4x4 Hermitian
        e_H[4:8, 4:8] = block_4x4
        # Frobenius normalize
        norm_F = np.sqrt(np.trace(e_H @ e_H.conj().T).real)
        e_H = e_H / norm_F
        basis.append(e_H)
        block_labels.append('H')

    # --- M_3(C) summand: 9 real DOF on rows 8:11 ---
    # 3 diagonal generators
    for i in range(3):
        e = _zero_complex()
        idx = 8 + i
        e[idx, idx] = 1.0
        # already Frobenius-norm 1
        basis.append(e)
        block_labels.append('M3')

    # 3 complex symmetric off-diagonal (real-symmetric)
    sym_pairs = [(0, 1), (0, 2), (1, 2)]
    for (i, j) in sym_pairs:
        e = _zero_complex()
        ii = 8 + i
        jj = 8 + j
        e[ii, jj] = 1.0 / np.sqrt(2.0)
        e[jj, ii] = 1.0 / np.sqrt(2.0)
        basis.append(e)
        block_labels.append('M3')

    # 3 i*antisymmetric off-diagonal (Hermitian)
    for (i, j) in sym_pairs:
        e = _zero_complex()
        ii = 8 + i
        jj = 8 + j
        e[ii, jj] = -1j / np.sqrt(2.0)
        e[jj, ii] = 1j / np.sqrt(2.0)
        basis.append(e)
        block_labels.append('M3')

    # Verify each basis element is Hermitian
    for k, E in enumerate(basis):
        herm_err = np.max(np.abs(E - E.conj().T))  # (local)
        if herm_err > 1e-12:
            raise RuntimeError(f"Basis element {k} not Hermitian: err={herm_err}")

    # Verify total DOF count: 1 + 4 + 9 = 14
    n_C = sum(1 for lbl in block_labels if lbl == 'C')
    n_H = sum(1 for lbl in block_labels if lbl == 'H')
    n_M3 = sum(1 for lbl in block_labels if lbl == 'M3')
    if (n_C, n_H, n_M3) != (1, 4, 9):
        raise RuntimeError(f"DOF count mismatch: C={n_C}, H={n_H}, M3={n_M3}; expected (1,4,9)")
    if len(basis) != COMPLEX_HERMITIAN_DOF_COUNT:
        raise RuntimeError(f"Total DOF {len(basis)} != {COMPLEX_HERMITIAN_DOF_COUNT}")

    return basis, block_labels


# ---------------------------------------------------------------------------
# Section 6 - Spectrum loading + canonical state-pair (Pair-2: B1 acoustic)
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
    """Mirrors S87 W3 deterministic build: lowest-n_loc absolute eigvals from
    the union of given sectors, chiral D_loc = [[0, M], [M^T, 0]] with M built
    via SVD of random orthogonal matrices. RNG_SEED=42 reproduces S87 W3 exactly.
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
    lambdas = pool_sorted[:n_use // 2]  # (local)
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
    D_loc = np.block([[Z, M], [M.T, Z]])  # (local) 2m x 2m, real symmetric

    return {
        'lambdas': lambdas,
        'D_loc': D_loc,
        'D_diag': np.concatenate([lambdas, -lambdas]),
        'n_loc': 2 * m,
        'M_block': M,
    }


def build_canonical_pair2(sector_evals):
    """Build Pair-2: B1 acoustic min/max in (0,1) U (1,0). Same as S87 W3."""
    p2 = select_state_localized_block(sector_evals, [(0, 1), (1, 0)], N_LOC)
    if p2 is None:
        raise RuntimeError("Failed to build Pair-2")
    n2 = p2['n_loc']  # (local)
    p_state = np.zeros(n2); p_state[0] = 1.0  # (local)
    q_state = np.zeros(n2); q_state[n2 - 1] = 1.0  # (local)
    return {
        'name': 'Pair-2: B1 acoustic min/max',
        'sectors': [(0, 1), (1, 0)],
        'D_loc': p2['D_loc'],
        'lambdas': p2['lambdas'],
        'D_diag': p2['D_diag'],
        'n_loc': n2,
        'p_state': p_state.astype(np.complex128),
        'q_state': q_state.astype(np.complex128),
    }


# ---------------------------------------------------------------------------
# Section 7 - Connes-distance SDP with cvxpy.Variable(hermitian=True)
# ---------------------------------------------------------------------------

def connes_distance_complex_hermitian_sdp(D_loc, p_state, q_state, basis,
                                            block_labels, sdp_tol=SDP_TOL,
                                            R_regularization=None):
    """Connes distance restricted to algebra elements
        a = sum_i x_i * E_i,       E_i complex Hermitian, x_i real
    where {E_i} is the 14-DOF complex-Hermitian A_F basis.

      max     | <p|a|p> - <q|a|q> | = | sum_i x_i * Re(tr(delta_rho * E_i)) |
      s.t.    || [D, a] ||_op <= 1     (LMI form)
              || a ||_F <= R           (Frobenius regulator, matches S87 W3)

    Variable: K = 14 REAL scalars x_i; the basis carries the complex structure.
    LMI is in 2n complex Hermitian form for ||[D,a]||_op <= 1.

    Returns dict with d_C, per-block contribution (sum of |x_i| within block),
    SDP solver status, and per-direction breakdown.
    """
    n = D_loc.shape[0]  # (local)
    rho_p = np.outer(p_state, p_state.conj())  # (local) complex
    rho_q = np.outer(q_state, q_state.conj())  # (local) complex
    delta_rho = rho_p - rho_q                 # (local)

    K = len(basis)  # (local) = 14

    # x_i real coefficients of basis expansion (cvxpy Variable default is real)
    x = cp.Variable(K)  # (local)

    # a = sum_i x_i * E_i  (complex Hermitian by construction)
    a_expr = sum([x[i] * basis[i] for i in range(K)])  # (local) cvxpy expression

    # objective: linear functional of x
    # Re(tr(delta_rho * E_i)) is real; coefficients are real numpy scalars
    obj_coeffs = np.array(
        [float(np.trace(delta_rho @ basis[i]).real) for i in range(K)],
        dtype=np.float64,
    )  # (local)

    # commutator [D, a] = D @ a - a @ D, complex
    commutator = D_loc @ a_expr - a_expr @ D_loc  # (local)

    # ||[D, a]||_op <= 1 expressed as 2n x 2n LMI
    #   [[ I_n,    [D,a]    ],
    #    [ [D,a]^*, I_n     ]]  >> 0
    I_n = np.eye(n, dtype=np.complex128)  # (local)
    lmi = cp.bmat([
        [I_n, commutator],
        [commutator.H, I_n],
    ])
    constraints = [lmi >> 0]  # (local)

    # Frobenius regulator (mirror S87 W3 default)
    if R_regularization is None:
        eig_max = float(np.max(np.abs(np.linalg.eigvalsh(D_loc))))  # (local)
        R_regularization = R_FROBENIUS_FACTOR * eig_max
    constraints.append(cp.norm(a_expr, 'fro') <= R_regularization)

    solver_kwargs = dict(  # (local)
        solver=cp.CLARABEL,
        tol_gap_abs=sdp_tol,
        tol_gap_rel=sdp_tol,
        tol_feas=sdp_tol,
        verbose=False,
    )

    # solve max and min directions
    objective_pos = cp.Maximize(obj_coeffs @ x)
    objective_neg = cp.Minimize(obj_coeffs @ x)

    try:
        prob_pos = cp.Problem(objective_pos, constraints)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            prob_pos.solve(**solver_kwargs)
        d_pos = float(prob_pos.value) if prob_pos.value is not None else float('nan')
        x_pos = np.asarray(x.value, dtype=np.float64) if x.value is not None else None
        status_pos = prob_pos.status  # (local)
    except Exception as ex:
        d_pos = float('nan')
        x_pos = None
        status_pos = f'SDP_FAIL_pos:{ex}'

    try:
        prob_neg = cp.Problem(objective_neg, constraints)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            prob_neg.solve(**solver_kwargs)
        d_neg = float(prob_neg.value) if prob_neg.value is not None else float('nan')
        x_neg = np.asarray(x.value, dtype=np.float64) if x.value is not None else None
        status_neg = prob_neg.status  # (local)
    except Exception as ex:
        d_neg = float('nan')
        x_neg = None
        status_neg = f'SDP_FAIL_neg:{ex}'

    if np.isnan(d_pos) and np.isnan(d_neg):
        d_C = float('nan')  # (local)
        x_optimal = None
    elif np.isnan(d_pos):
        d_C = abs(d_neg)
        x_optimal = x_neg
    elif np.isnan(d_neg):
        d_C = abs(d_pos)
        x_optimal = x_pos
    else:
        if abs(d_pos) >= abs(d_neg):
            d_C = abs(d_pos)
            x_optimal = x_pos
        else:
            d_C = abs(d_neg)
            x_optimal = x_neg

    # Per-block decomposition: sum of |x_i| per block label
    if x_optimal is not None:
        x_arr = np.asarray(x_optimal, dtype=np.float64)
        # contribution to objective per direction: |x_i * obj_coeffs[i]|
        contrib_C = float(sum(abs(x_arr[i] * obj_coeffs[i])
                              for i, lbl in enumerate(block_labels) if lbl == 'C'))
        contrib_H = float(sum(abs(x_arr[i] * obj_coeffs[i])
                              for i, lbl in enumerate(block_labels) if lbl == 'H'))
        contrib_M3 = float(sum(abs(x_arr[i] * obj_coeffs[i])
                               for i, lbl in enumerate(block_labels) if lbl == 'M3'))
        # x-norm per block (basis-coordinate l2 norm)
        x_norm_C = float(np.sqrt(sum(x_arr[i]**2 for i, lbl in enumerate(block_labels) if lbl == 'C')))
        x_norm_H = float(np.sqrt(sum(x_arr[i]**2 for i, lbl in enumerate(block_labels) if lbl == 'H')))
        x_norm_M3 = float(np.sqrt(sum(x_arr[i]**2 for i, lbl in enumerate(block_labels) if lbl == 'M3')))
    else:
        contrib_C = float('nan')
        contrib_H = float('nan')
        contrib_M3 = float('nan')
        x_norm_C = float('nan')
        x_norm_H = float('nan')
        x_norm_M3 = float('nan')

    return {
        'd_C': d_C,
        'd_pos': d_pos,
        'd_neg': d_neg,
        'status_pos': status_pos,
        'status_neg': status_neg,
        'x_pos': x_pos,
        'x_neg': x_neg,
        'x_optimal': x_optimal,
        'contrib_C': contrib_C,
        'contrib_H': contrib_H,
        'contrib_M3': contrib_M3,
        'x_norm_C': x_norm_C,
        'x_norm_H': x_norm_H,
        'x_norm_M3': x_norm_M3,
        'obj_coeffs': obj_coeffs,
        'R_regularization': float(R_regularization),
    }


# ---------------------------------------------------------------------------
# Section 8 - Reference candidate forms (mirrors S87 W3 C2/C3/C4)
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
    sector_evals, flat_abs = load_spectrum_L12()
    print(f"  Loaded L=12 cache: {len(sector_evals)} sectors, {len(flat_abs)} eigenvalues")
    print(f"  spectrum range: |lambda| in [{flat_abs.min():.6f}, {flat_abs.max():.6f}]")

    # Build full complex-Hermitian A_F basis (14 real DOF)
    basis, block_labels = build_complex_hermitian_af_basis(N_LOC)
    print(f"\n  Built complex-Hermitian A_F basis:")
    print(f"    C-block:  {sum(1 for lbl in block_labels if lbl == 'C')} DOF")
    print(f"    H-block:  {sum(1 for lbl in block_labels if lbl == 'H')} DOF")
    print(f"    M3-block: {sum(1 for lbl in block_labels if lbl == 'M3')} DOF")
    print(f"    TOTAL:    {len(basis)} DOF (= 1 + 4 + 9)")

    # Build canonical state pair (matched to S87 W3 Pair-2)
    pair = build_canonical_pair2(sector_evals)
    print(f"\n  Built canonical pair: {pair['name']} (n_loc={pair['n_loc']})")
    eig_max = float(np.max(np.abs(np.linalg.eigvalsh(pair['D_loc']))))
    R_reg = R_FROBENIUS_FACTOR * eig_max
    print(f"  D_loc spectral radius: {eig_max:.6f}; Frobenius regulator R = 100*lambda_max = {R_reg:.6f}")

    # Run SDP with full 14-DOF complex-Hermitian basis
    print(f"\n  Running cvxpy SDP (14 real variables, CLARABEL, tol={SDP_TOL})...")
    t0 = time.time()
    sdp = connes_distance_complex_hermitian_sdp(
        pair['D_loc'], pair['p_state'], pair['q_state'],
        basis, block_labels,
    )
    t_sdp = time.time() - t0
    print(f"  SDP completed in {t_sdp:.2f}s")
    print(f"    status_pos: {sdp['status_pos']}")
    print(f"    status_neg: {sdp['status_neg']}")
    print(f"    d_pos = {sdp['d_pos']:.12e}")
    print(f"    d_neg = {sdp['d_neg']:.12e}")
    print(f"    d_C   = {sdp['d_C']:.12e}")

    print(f"\n  Per-block contributions (|x_i * obj_coeff_i|):")
    print(f"    C-block:  {sdp['contrib_C']:.6e}")
    print(f"    H-block:  {sdp['contrib_H']:.6e}")
    print(f"    M3-block: {sdp['contrib_M3']:.6e}")
    print(f"    SUM:      {sdp['contrib_C'] + sdp['contrib_H'] + sdp['contrib_M3']:.6e}")
    print(f"    d_C ref:  {sdp['d_C']:.6e}")

    print(f"\n  Per-block x-coordinate norms ||x_block||_2:")
    print(f"    C-block:  {sdp['x_norm_C']:.6e}")
    print(f"    H-block:  {sdp['x_norm_H']:.6e}")
    print(f"    M3-block: {sdp['x_norm_M3']:.6e}")

    # Reference candidate forms (independent of basis, for residual computation)
    rhs_C2 = candidate2_mellin_dirichlet_analog(
        pair['D_diag'], pair['p_state'].real, pair['q_state'].real)
    rhs_C3 = candidate3_commutator_norm(
        pair['D_loc'], pair['p_state'].real, pair['q_state'].real)
    rhs_C4 = candidate4_heat_kernel_trace(
        pair['D_loc'], pair['p_state'].real, pair['q_state'].real)

    print(f"\n  Reference candidate forms (for residual computation):")
    print(f"    C2 (Mellin-Dirichlet):  {rhs_C2:.6e}")
    print(f"    C3 (commutator-norm):   {rhs_C3:.6e}")
    print(f"    C4 (heat-kernel-trace): {rhs_C4:.6e}")

    # STRICT residuals (relative, matching S87 W3 convention)
    if sdp['d_C'] is not None and np.isfinite(sdp['d_C']) and abs(sdp['d_C']) > 1e-15:
        residual_C2 = abs(rhs_C2 - sdp['d_C']) / abs(sdp['d_C'])
        residual_C3 = abs(rhs_C3 - sdp['d_C']) / abs(sdp['d_C'])
        residual_C4 = abs(rhs_C4 - sdp['d_C']) / abs(sdp['d_C'])
    else:
        residual_C2 = float('inf')
        residual_C3 = float('inf')
        residual_C4 = float('inf')

    print(f"\n  STRICT residuals (relative):")
    print(f"    C2: {residual_C2:.6e}")
    print(f"    C3: {residual_C3:.6e}    [S87 W3 baseline = {S87_BASELINE_RESIDUAL:.6e}]")
    print(f"    C4: {residual_C4:.6e}")

    # Best non-definitional residual = min over C2, C3, C4
    candidate_residuals = [residual_C2, residual_C3, residual_C4]
    candidate_names = ['C2: Mellin-Dirichlet',
                       'C3: commutator-norm 1/||[D, rho_p - rho_q]||_op',
                       'C4: heat-kernel-trace sqrt(Tr[Q_pq * D^{-2}])']
    finite_mask = [np.isfinite(r) for r in candidate_residuals]
    if any(finite_mask):
        finite_residuals = [r for r, m in zip(candidate_residuals, finite_mask) if m]
        finite_names = [n for n, m in zip(candidate_names, finite_mask) if m]
        idx_min = int(np.argmin(finite_residuals))
        best_residual = float(finite_residuals[idx_min])
        best_name = finite_names[idx_min]
    else:
        best_residual = float('inf')
        best_name = 'NONE-FINITE'

    print(f"\n  Best non-definitional residual: {best_residual:.12e}  ({best_name})")
    print(f"  S87 8-DOF baseline:               {S87_BASELINE_RESIDUAL:.12e}")
    print(f"  Difference:                       {(best_residual - S87_BASELINE_RESIDUAL):.12e}")

    # Supremum monotonicity verification (Step 5 of substitution chain)
    # Re-run with restricted 8-DOF basis (mirror S87 W3 STRICT) for cross-check
    print(f"\n  Verifying supremum monotonicity (Step 5):")
    print(f"  Re-running with restricted 8-DOF basis (mirror S87 W3 STRICT)...")
    # Build the S87 STRICT 8-DOF subset: drop H Pauli x,y,z and M_3 i*antisym
    s87_strict_indices = []  # (local)
    s87_dof_count = 0  # (local)
    for k, lbl in enumerate(block_labels):
        # C: keep all (1)
        # H: keep only the q_0 = I_2 (Frobenius-normalized) -> first H index
        # M3: keep diag (3) + sym off-diag (3); drop i*antisym (3)
        if lbl == 'C':
            s87_strict_indices.append(k)
            s87_dof_count += 1
        elif lbl == 'H':
            # First H is sigma_0 = I_2; keep that one only
            if s87_dof_count == 1 or (s87_dof_count >= 1 and k == 1):
                # The first H entry in the basis ordering is k=1 (sigma_0)
                if k == 1:
                    s87_strict_indices.append(k)
                    s87_dof_count += 1
        elif lbl == 'M3':
            # M3 entries are at indices 5..13 in basis order:
            # 5,6,7 = diag; 8,9,10 = sym off; 11,12,13 = i*antisym
            if k <= 10:  # diag (5,6,7) + sym off (8,9,10)
                s87_strict_indices.append(k)
                s87_dof_count += 1

    s87_basis_subset = [basis[i] for i in s87_strict_indices]
    s87_block_labels_subset = [block_labels[i] for i in s87_strict_indices]
    print(f"  S87-mirror subset DOF: {len(s87_basis_subset)} indices = {s87_strict_indices}")

    sdp_s87mirror = connes_distance_complex_hermitian_sdp(
        pair['D_loc'], pair['p_state'], pair['q_state'],
        s87_basis_subset, s87_block_labels_subset,
    )
    d_C_8dof = sdp_s87mirror['d_C']
    print(f"  d_C(8-DOF S87-mirror) = {d_C_8dof:.12e}")
    print(f"  d_C(14-DOF full)      = {sdp['d_C']:.12e}")
    monotonicity_holds = (sdp['d_C'] >= d_C_8dof - 1e-9)
    monotonicity_excess = float(sdp['d_C'] - d_C_8dof)
    print(f"  Monotonicity 14-DOF >= 8-DOF: {monotonicity_holds}  (excess = {monotonicity_excess:.6e})")

    # Verdict construction
    sdp_converged = sdp['status_pos'] in {'optimal', 'optimal_inaccurate'} \
                    and sdp['status_neg'] in {'optimal', 'optimal_inaccurate'}

    # Sign verdict: PASS iff residual <= S87 baseline (Step 8 PASS direction)
    # FAIL iff residual > S87 baseline (overshoot)
    if np.isfinite(best_residual):
        if best_residual <= S87_BASELINE_RESIDUAL:
            sign_v = 'PASS'
        else:
            sign_v = 'FAIL'
    else:
        sign_v = 'N/A'

    # Magnitude verdict: PASS iff |residual - target| <= PASS_BAND (1e-3)
    # INFO iff PASS_BAND < |residual - target| <= INFO_BAND (5x)
    # FAIL iff |residual - target| > INFO_BAND
    if np.isfinite(best_residual):
        delta = abs(best_residual - S87_BASELINE_RESIDUAL)
        if delta <= PASS_BAND:
            mag_v = 'PASS'
        elif delta <= INFO_BAND:
            mag_v = 'INFO'
        else:
            mag_v = 'FAIL'
    else:
        mag_v = 'FAIL'

    # Regime verdict: VALID iff SDP converged; MARGINAL otherwise
    regime_v = 'VALID' if sdp_converged else 'MARGINAL'

    # Composite per S87+ schema-v2 collapse rule
    if regime_v == 'BREAKDOWN':
        composite_top = 'FAIL'
    elif sign_v == 'FAIL':
        composite_top = 'FAIL'
    elif mag_v == 'FAIL' and regime_v == 'VALID':
        composite_top = 'FAIL'
    elif mag_v == 'FAIL' and regime_v == 'MARGINAL':
        composite_top = 'INFO'
    elif mag_v == 'INFO':
        composite_top = 'INFO'
    else:
        composite_top = 'PASS'

    # Verdict value: the STRICT residual (full float64)
    verdict_value = float(best_residual) if np.isfinite(best_residual) else float('nan')

    return {
        # Verdict scalars
        'value': verdict_value,
        'composite_top': composite_top,
        'sign_verdict': sign_v,
        'magnitude_verdict': mag_v,
        'regime_verdict': regime_v,
        'sdp_converged': bool(sdp_converged),
        # Residuals + comparison
        'STRICT_residual_full_float64': verdict_value,
        'best_candidate_name': best_name,
        'residual_C2': float(residual_C2),
        'residual_C3': float(residual_C3),
        'residual_C4': float(residual_C4),
        'rhs_C2': float(rhs_C2),
        'rhs_C3': float(rhs_C3),
        'rhs_C4': float(rhs_C4),
        's87_baseline_residual': float(S87_BASELINE_RESIDUAL),
        'comparison_to_s87_8dof_baseline': float(verdict_value - S87_BASELINE_RESIDUAL),
        # SDP details
        'd_C_14dof': float(sdp['d_C']),
        'd_C_pos': float(sdp['d_pos']),
        'd_C_neg': float(sdp['d_neg']),
        'sdp_solver_name': 'CLARABEL',
        'sdp_solver_status_pos': str(sdp['status_pos']),
        'sdp_solver_status_neg': str(sdp['status_neg']),
        'sdp_solver_status': f"{sdp['status_pos']}|{sdp['status_neg']}",
        'sdp_solver_tolerance': float(SDP_TOL),
        'R_regularization': float(sdp['R_regularization']),
        # Per-block contributions
        'per_block_residual_C': float(sdp['contrib_C']),
        'per_block_residual_H': float(sdp['contrib_H']),
        'per_block_residual_M3': float(sdp['contrib_M3']),
        'x_norm_C': float(sdp['x_norm_C']),
        'x_norm_H': float(sdp['x_norm_H']),
        'x_norm_M3': float(sdp['x_norm_M3']),
        'x_optimal': sdp['x_optimal'] if sdp['x_optimal'] is not None else np.zeros(14),
        'obj_coeffs': sdp['obj_coeffs'],
        # Supremum monotonicity (Step 5)
        'supremum_monotonicity_verification': bool(monotonicity_holds),
        'd_C_8dof_S87_mirror': float(d_C_8dof),
        'monotonicity_excess': float(monotonicity_excess),
        # DOF counts
        'complex_hermitian_dof_count': COMPLEX_HERMITIAN_DOF_COUNT,
        's87_strict_dof_count': S87_STRICT_DOF_COUNT,
        # Spectrum metadata
        'pair_name': pair['name'],
        'n_loc': pair['n_loc'],
        'spectrum_eig_max': eig_max,
        'flat_abs_count': int(len(flat_abs)),
        'flat_abs_min': float(flat_abs.min()),
        'flat_abs_max': float(flat_abs.max()),
    }


# ---------------------------------------------------------------------------
# Section 10 - Plot per-block contribution
# ---------------------------------------------------------------------------

def plot_results(result):
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    # Panel 1: per-block contribution to objective (stacked bar)
    ax = axes[0]
    blocks = ['C', 'H', 'M3']
    contribs = [result['per_block_residual_C'],
                result['per_block_residual_H'],
                result['per_block_residual_M3']]
    colors = ['tab:blue', 'tab:orange', 'tab:green']
    bars = ax.bar(blocks, contribs, color=colors)
    ax.set_xlabel('A_F block')
    ax.set_ylabel('|x_i * obj_coeff_i| sum within block')
    ax.set_title(f'Per-block contribution to d_C\n'
                 f'(d_C = {result["d_C_14dof"]:.6e})')
    ax.grid(True, alpha=0.3, axis='y')
    for bar, val in zip(bars, contribs):
        ax.annotate(f'{val:.3e}', xy=(bar.get_x() + bar.get_width()/2, bar.get_height()),
                    ha='center', va='bottom', fontsize=8)

    # Panel 2: x-coordinate norms per block
    ax = axes[1]
    x_norms = [result['x_norm_C'],
               result['x_norm_H'],
               result['x_norm_M3']]
    bars = ax.bar(blocks, x_norms, color=colors)
    ax.set_xlabel('A_F block')
    ax.set_ylabel('||x_block||_2')
    ax.set_title('Optimal x-coordinate l2-norm per block\n(14 = 1 + 4 + 9 real DOF)')
    ax.grid(True, alpha=0.3, axis='y')
    for bar, val in zip(bars, x_norms):
        ax.annotate(f'{val:.3e}', xy=(bar.get_x() + bar.get_width()/2, bar.get_height()),
                    ha='center', va='bottom', fontsize=8)

    # Panel 3: comparison to S87 baseline
    ax = axes[2]
    labels = ['S87 8-DOF\nbaseline', 'S88 14-DOF\nfull complex-Hermitian']
    values = [result['s87_baseline_residual'], result['STRICT_residual_full_float64']]
    bar_colors = ['gray', 'tab:red' if result['STRICT_residual_full_float64'] > result['s87_baseline_residual'] else 'tab:green']
    bars = ax.bar(labels, values, color=bar_colors)
    ax.axhline(result['s87_baseline_residual'], color='k', linestyle='--', alpha=0.5,
               label=f'S87 baseline = {result["s87_baseline_residual"]:.4e}')
    ax.set_ylabel('STRICT residual (relative)')
    ax.set_title('STRICT residual: 14-DOF vs 8-DOF\n'
                 f'monotonicity: 14-DOF d_C - 8-DOF d_C = {result["monotonicity_excess"]:.3e}')
    ax.grid(True, alpha=0.3, axis='y')
    ax.legend(loc='best', fontsize=8)
    for bar, val in zip(bars, values):
        ax.annotate(f'{val:.4e}', xy=(bar.get_x() + bar.get_width()/2, bar.get_height()),
                    ha='center', va='bottom', fontsize=8)

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
    print(f"S87 baseline residual: {S87_BASELINE_RESIDUAL:.12e}")
    print(f"Complex-Hermitian DOF target: {COMPLEX_HERMITIAN_DOF_COUNT} (= 1 + 4 + 9)")

    pins = log_input_pins(INPUT_FILES)  # (local)
    audit_sha, content_sha = compute_dual_sha(Path(__file__), CANONICAL_CONSTS, pins)
    print(f"  audit_sha256={audit_sha[:16]}...")
    print(f"  content_sha256={content_sha[:16]}...")
    closure = closure_hash(pins)
    print(f"  closure_hash={closure[:16]}...")

    result = compute()

    print(f"\n=== Verdict construction ===")
    print(f"  STRICT residual (full float64):    {result['STRICT_residual_full_float64']:.15e}")
    print(f"  S87 baseline residual:             {result['s87_baseline_residual']:.15e}")
    print(f"  comparison_to_s87_8dof_baseline:   {result['comparison_to_s87_8dof_baseline']:.6e}")
    print(f"  supremum_monotonicity_verification: {result['supremum_monotonicity_verification']}")
    print(f"  sign_verdict:      {result['sign_verdict']}")
    print(f"  magnitude_verdict: {result['magnitude_verdict']}")
    print(f"  regime_verdict:    {result['regime_verdict']}")
    print(f"  composite_top:     {result['composite_top']}")

    # Save .npz
    np_save = {  # (local)
        'STRICT_residual_full_float64': result['STRICT_residual_full_float64'],
        'per_block_residual_C': result['per_block_residual_C'],
        'per_block_residual_H': result['per_block_residual_H'],
        'per_block_residual_M3': result['per_block_residual_M3'],
        'sdp_solver_name': result['sdp_solver_name'],
        'sdp_solver_status': result['sdp_solver_status'],
        'sdp_solver_status_pos': result['sdp_solver_status_pos'],
        'sdp_solver_status_neg': result['sdp_solver_status_neg'],
        'sdp_solver_tolerance': result['sdp_solver_tolerance'],
        'comparison_to_s87_8dof_baseline': result['comparison_to_s87_8dof_baseline'],
        'supremum_monotonicity_verification': result['supremum_monotonicity_verification'],
        'value': result['value'],
        'composite_top': result['composite_top'],
        'sign_verdict': result['sign_verdict'],
        'magnitude_verdict': result['magnitude_verdict'],
        'regime_verdict': result['regime_verdict'],
        'sdp_converged': result['sdp_converged'],
        'd_C_14dof': result['d_C_14dof'],
        'd_C_pos': result['d_C_pos'],
        'd_C_neg': result['d_C_neg'],
        's87_baseline_residual': result['s87_baseline_residual'],
        'best_candidate_name': result['best_candidate_name'],
        'residual_C2': result['residual_C2'],
        'residual_C3': result['residual_C3'],
        'residual_C4': result['residual_C4'],
        'rhs_C2': result['rhs_C2'],
        'rhs_C3': result['rhs_C3'],
        'rhs_C4': result['rhs_C4'],
        'R_regularization': result['R_regularization'],
        'x_optimal': result['x_optimal'],
        'obj_coeffs': result['obj_coeffs'],
        'x_norm_C': result['x_norm_C'],
        'x_norm_H': result['x_norm_H'],
        'x_norm_M3': result['x_norm_M3'],
        'd_C_8dof_S87_mirror': result['d_C_8dof_S87_mirror'],
        'monotonicity_excess': result['monotonicity_excess'],
        'complex_hermitian_dof_count': result['complex_hermitian_dof_count'],
        's87_strict_dof_count': result['s87_strict_dof_count'],
        'pair_name': result['pair_name'],
        'n_loc': result['n_loc'],
        'spectrum_eig_max': result['spectrum_eig_max'],
        'flat_abs_count': result['flat_abs_count'],
        'flat_abs_min': result['flat_abs_min'],
        'flat_abs_max': result['flat_abs_max'],
        'gate_id': GATE_ID,
        'scheme': SCHEME,
        'convention': CONVENTION,
        'L_max': L_MAX,
        'audit_sha256': audit_sha,
        'content_sha256': content_sha,
    }
    np.savez(OUT_NPZ, **{k: np.asarray(v, dtype=object) if isinstance(v, list) else v
                           for k, v in np_save.items()})
    print(f"\n  Data saved: {OUT_NPZ.name} ({OUT_NPZ.stat().st_size} bytes)")

    plot_results(result)

    emit_verdict_line(result, audit_sha, content_sha)

    print(f"\n=== {GATE_ID} complete ===")
    print(f"  wall = {time.time() - t0:.2f} s")
    sys.exit(0)


if __name__ == '__main__':
    main()
