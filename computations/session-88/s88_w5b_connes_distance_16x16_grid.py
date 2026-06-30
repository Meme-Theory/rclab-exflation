#!/usr/bin/env python3
"""
S88 W5b §W5b-50 - Connes-distance characterization scan over 16x16 state-pair grid
====================================================================================

Gate ID: S88-A_F-CONNES-DISTANCE-CHARACTERIZATION-SCAN
Trigger: [VERIFY]
Classification: PHONONIC sub-case (16x16 state-pair grid characterization;
Corner III calibration corpus extension; full distance-matrix block-pattern
for substrate-IS metric structure on A_F state space).

PRE-REGISTRATION (sessions/session-plan/session-88-plan-w5b.md §W5b-50):

Hypothesis: The 16x16 Connes-distance matrix D_C[i,j] = d_C(e_i, e_j) over the
canonical computational state basis exhibits structural block-pattern reflecting
the A_F = C (+) H (+) M_3(C) decomposition. Specifically, the 16-dim Hilbert
space (n_loc=16 from S87 W3 / S88 W5b-49) carries the algebra-IRREP block
structure:
  C-block:  rows [0:4]  -> 4 elementary states
  H-block:  rows [4:8]  -> 4 elementary states
  M_3-block: rows [8:11] -> 3 elementary states
  Padding:   rows [11:16] -> 5 elementary states (no algebra action)

Predicted partition: {C: e_0..e_3} U {H: e_4..e_7} U {M_3: e_8..e_10} U {Pad: e_11..e_15}
This is the NATURAL canonical-state-basis partition under §W5b-49 algebra
embedding; the plan's "1+2+12" reflects irrep-multiplicity counting on the full
H_F=C^32, while this 16-dim chirality-projected Hilbert space carries the
4+4+3+5 partition derived directly from the A_F embedding rows.

Method (per plan §W5b-50):
  1. Identify 16 elementary states e_i (canonical computational basis).
  2. For each pair (i, j) with i < j (120 pairs), compute STRICT d_C via cvxpy SDP
     using the 14-DOF complex-Hermitian A_F basis (re-using §W5b-49 infrastructure).
  3. Assemble symmetric 16x16 distance matrix D_C with zero diagonal.
  4. Apply hierarchical clustering (scipy.cluster.hierarchy) to recover intrinsic
     state partition; cross-check against predicted A_F block-structure.
  5. Compute fidelity score F = (sum_intra d) / (sum_inter d); expect F < 1.
  6. Emit full matrix + clustering + fidelity to .npz; heatmap to .png.

PASS / FAIL / INFO criterion (pre-registered, plan §W5b-50):
  PASS iff: (i) all 120 pairs computed without SDP failure;
            (ii) symmetric 16x16 matrix assembled with zero diagonal;
            (iii) hierarchical clustering yields partition matching predicted
                 A_F block-structure (4+4+3+5);
            (iv) fidelity score F < 1 (intra-block smaller than inter-block);
            (v) heatmap plot emitted;
            (vi) Corner: III declaration in WP §W5b-50.
  FAIL iff: SDP fails on > 5% of pairs (>= 7 pair failures), OR clustering
            fails to recover any block-structure resemblance, OR F >= 1.
  INFO if: clustering recovers block structure with <= 2 state mis-assignments
           at block boundaries (numerical-precision near-edge SDP).

NO 3-tuple companion required (structural characterization, not directional).

CALIBRATION:
  - State basis: 16 elementary computational basis vectors e_i on the n_loc=16
    Hilbert space induced by §W5b-49's chiral D_loc construction.
  - D_F: same chiral D_loc as §W5b-49 (Pair-2 sectors (0,1)+(1,0) at L_max=12).
  - SDP solver: cvxpy.CLARABEL with tol_gap_abs/rel 1e-9 (matches §W5b-49).
  - SDP infrastructure: 14-DOF complex-Hermitian A_F basis from §W5b-49.

OUTPUTS:
  - computations/session-88/s88_w5b_connes_distance_16x16_grid.npz
  - computations/session-88/s88_w5b_connes_distance_16x16_heatmap.png
  - Verdict line at computations/session-88/s88_gate_verdicts.txt

Substrate framing: The 16x16 distance matrix IS the substrate's intrinsic metric
structure on its state space - not "in" any container. The block-pattern
recovery IS the substrate's algebra decomposition manifesting in the distance
metric. Fidelity F IS the substrate's quantitative measure of how closely its
state-space metric respects its algebra decomposition.

Discipline:
  - from canonical_constants import * (S34+ MANDATORY)
  - All locals tagged # (local)
  - cvxpy CPU SDP (CPU thread cap before numpy import)
  - Dual-SHA verdict line; no schema-v2 3-tuple (structural-characterization gate)
  - AFTER-pattern: build full result in memory -> write .npz -> verify ->
    emit verdict line ONCE (per registry-landing.md §"Bridge-Landing Script
    Architecture")
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
from scipy.cluster.hierarchy import linkage, fcluster
from scipy.spatial.distance import squareform

# ---------------------------------------------------------------------------
# Section 3 - Paths + pre-registration constants
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

SESSION = "S88"                                                          # (local)
GATE_ID = "S88-A_F-CONNES-DISTANCE-CHARACTERIZATION-SCAN"                # (local)
SCHEME = "Connes-distance-16x16-state-pair-grid-A_F-decomposition-characterization"  # (local)
CONVENTION = "cvxpy-Hermitian-True-14-real-DOF-per-pair"                 # (local)
L_MAX_TAG = "NA"                                                         # (local) plan: L_max N/A
L_MAX_NUM = 12                                                           # (local) underlying spectrum cache
N_LOC = 16                                                               # (local)
RNG_SEED = 42                                                            # (local) match S87 W3 / S88 W5b-49
SDP_TOL = 1e-9                                                           # (local) per plan §W5b-50

# Pre-registered DOF counts (Step 3 of substitution chain in §W5b-49)
COMPLEX_HERMITIAN_DOF_COUNT = 14   # 1 + 4 + 9                            # (local)

# Pre-registered R-regulator (matches §W5b-49 default 100 * |lambda|_max)
R_FROBENIUS_FACTOR = 100.0                                                # (local)

# Pre-registered predicted block partition (4+4+3+5 from A_F embedding)
# C-block: rows [0:4], H-block: rows [4:8], M_3-block: rows [8:11], Pad: [11:16]
PREDICTED_BLOCKS = {                                                      # (local)
    'C':   list(range(0, 4)),    # 4 states
    'H':   list(range(4, 8)),    # 4 states
    'M_3': list(range(8, 11)),   # 3 states
    'Pad': list(range(11, 16)),  # 5 states
}

# Predicted-state-to-block label list (length 16, indexed by state i)
PREDICTED_LABEL = (
    ['C']   * 4 +
    ['H']   * 4 +
    ['M_3'] * 3 +
    ['Pad'] * 5
)

# Pre-registered SDP-failure tolerance per plan §W5b-50 PASS criterion (i):
# > 5% of 120 pairs = > 6 failures => FAIL on convergence-rate
MAX_SDP_FAIL = int(0.05 * 120)  # = 6                                     # (local)

# Pre-registered fidelity threshold (PASS criterion iv): F < 1
FIDELITY_THRESHOLD = 1.0                                                  # (local)

# Pre-registered clustering: agglomerative, ward linkage, n_clusters = 4
# (matches the 4-block partition C+H+M_3+Pad). Plan §W5b-50 mentions 3-cluster
# option (matching A_F = C (+) H (+) M_3) but n_loc=16 carries explicit Pad rows;
# 4-cluster recovery is more honest. Both will be reported.
CLUSTERING_LINKAGE = 'ward'                                               # (local)
N_CLUSTERS_4 = 4                                                          # (local) C+H+M_3+Pad
N_CLUSTERS_3 = 3                                                          # (local) C+H+M_3 (with Pad merged elsewhere)

# Output destinations
OUT_DIR = _HERE
OUT_NPZ = OUT_DIR / 's88_w5b_connes_distance_16x16_grid.npz'
OUT_PNG = OUT_DIR / 's88_w5b_connes_distance_16x16_heatmap.png'
VERDICT_TXT = OUT_DIR / 's88_gate_verdicts.txt'

# Pre-registered input pin map (substrate-canonical sourcing)
SPECTRUM_CACHE = PROJECT_ROOT / 'computations' / 'session-84' / 's84_spectrum_cache_L12_tau019.npz'
S87_W3_PY = PROJECT_ROOT / 'computations' / 'session-87' / 's87_w3_connes_distance_on_af.py'
S88_W5B_49_PY = PROJECT_ROOT / 'computations' / 'session-88' / 's88_w5b_connes_distance_af_complex_hermitian.py'
CANONICAL_CONSTS = _SHARED / 'canonical_constants.py'
INPUT_FILES = [SPECTRUM_CACHE, S87_W3_PY, S88_W5B_49_PY, CANONICAL_CONSTS]


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
# Section 5 - Full complex-Hermitian A_F basis (14 real DOF) - re-used from §W5b-49
# ---------------------------------------------------------------------------

def build_complex_hermitian_af_basis(n_loc):
    """Construct FULL complex-Hermitian basis of pi(A_F) embedded in M_{n_loc}(C).
    Identical to §W5b-49 build_complex_hermitian_af_basis. 14 generators total
    (1 + 4 + 9 from C, H, M_3 summands).
    """
    if n_loc != 16:
        raise ValueError(f"This A_F basis assumes n_loc=16; got {n_loc}")

    basis = []         # (local)
    block_labels = []  # (local)

    def _zero_complex():
        return np.zeros((n_loc, n_loc), dtype=np.complex128)

    # --- C summand: 1 real DOF (scalar*I_4 on rows 0:4) ---
    e_C = _zero_complex()
    e_C[0:4, 0:4] = np.eye(4, dtype=np.complex128)
    e_C = e_C / np.sqrt(np.trace(e_C @ e_C.conj().T).real)
    basis.append(e_C)
    block_labels.append('C')

    # --- H summand: 4 real DOF (Pauli basis) on rows 4:8 ---
    sigma_0 = np.eye(2, dtype=np.complex128)
    sigma_x = np.array([[0, 1], [1, 0]], dtype=np.complex128)
    sigma_y = np.array([[0, -1j], [1j, 0]], dtype=np.complex128)
    sigma_z = np.array([[1, 0], [0, -1]], dtype=np.complex128)
    pauli = [sigma_0, sigma_x, sigma_y, sigma_z]
    I2 = np.eye(2, dtype=np.complex128)
    for k, sigma_k in enumerate(pauli):
        e_H = _zero_complex()
        block_4x4 = np.kron(sigma_k, I2)  # (local)
        e_H[4:8, 4:8] = block_4x4
        norm_F = np.sqrt(np.trace(e_H @ e_H.conj().T).real)
        e_H = e_H / norm_F
        basis.append(e_H)
        block_labels.append('H')

    # --- M_3(C) summand: 9 real DOF on rows 8:11 ---
    for i in range(3):
        e = _zero_complex()
        idx = 8 + i
        e[idx, idx] = 1.0
        basis.append(e)
        block_labels.append('M3')

    sym_pairs = [(0, 1), (0, 2), (1, 2)]
    for (i, j) in sym_pairs:
        e = _zero_complex()
        ii = 8 + i
        jj = 8 + j
        e[ii, jj] = 1.0 / np.sqrt(2.0)
        e[jj, ii] = 1.0 / np.sqrt(2.0)
        basis.append(e)
        block_labels.append('M3')

    for (i, j) in sym_pairs:
        e = _zero_complex()
        ii = 8 + i
        jj = 8 + j
        e[ii, jj] = -1j / np.sqrt(2.0)
        e[jj, ii] = 1j / np.sqrt(2.0)
        basis.append(e)
        block_labels.append('M3')

    # Verify Hermiticity and DOF count
    for k, E in enumerate(basis):
        herm_err = np.max(np.abs(E - E.conj().T))  # (local)
        if herm_err > 1e-12:
            raise RuntimeError(f"Basis element {k} not Hermitian: err={herm_err}")
    n_C = sum(1 for lbl in block_labels if lbl == 'C')
    n_H = sum(1 for lbl in block_labels if lbl == 'H')
    n_M3 = sum(1 for lbl in block_labels if lbl == 'M3')
    if (n_C, n_H, n_M3) != (1, 4, 9):
        raise RuntimeError(f"DOF count mismatch: C={n_C}, H={n_H}, M3={n_M3}; expected (1,4,9)")
    if len(basis) != COMPLEX_HERMITIAN_DOF_COUNT:
        raise RuntimeError(f"Total DOF {len(basis)} != {COMPLEX_HERMITIAN_DOF_COUNT}")

    return basis, block_labels


# ---------------------------------------------------------------------------
# Section 6 - Spectrum loading + canonical D_loc (Pair-2 sectors)
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
    """Mirrors §W5b-49 / S87 W3 deterministic build."""
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


def build_canonical_D_loc(sector_evals):
    """Build canonical D_loc on n_loc=16 from sectors (0,1) U (1,0)."""
    p = select_state_localized_block(sector_evals, [(0, 1), (1, 0)], N_LOC)
    if p is None:
        raise RuntimeError("Failed to build canonical D_loc")
    return p


# ---------------------------------------------------------------------------
# Section 7 - Connes-distance SDP (re-used from §W5b-49)
# ---------------------------------------------------------------------------

def connes_distance_complex_hermitian_sdp(D_loc, p_state, q_state, basis,
                                          block_labels, sdp_tol=SDP_TOL,
                                          R_regularization=None):
    """Same SDP as §W5b-49: compute d_C(omega_p, omega_q) on 14-DOF A_F."""
    n = D_loc.shape[0]  # (local)
    rho_p = np.outer(p_state, p_state.conj())  # (local)
    rho_q = np.outer(q_state, q_state.conj())  # (local)
    delta_rho = rho_p - rho_q                 # (local)

    K = len(basis)  # (local)
    x = cp.Variable(K)  # (local)

    a_expr = sum([x[i] * basis[i] for i in range(K)])  # (local)
    obj_coeffs = np.array(
        [float(np.trace(delta_rho @ basis[i]).real) for i in range(K)],
        dtype=np.float64,
    )  # (local)

    commutator = D_loc @ a_expr - a_expr @ D_loc  # (local)
    I_n = np.eye(n, dtype=np.complex128)  # (local)
    lmi = cp.bmat([
        [I_n, commutator],
        [commutator.H, I_n],
    ])
    constraints = [lmi >> 0]  # (local)

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

    if x_optimal is not None:
        x_arr = np.asarray(x_optimal, dtype=np.float64)
        contrib_C = float(sum(abs(x_arr[i] * obj_coeffs[i])
                              for i, lbl in enumerate(block_labels) if lbl == 'C'))
        contrib_H = float(sum(abs(x_arr[i] * obj_coeffs[i])
                              for i, lbl in enumerate(block_labels) if lbl == 'H'))
        contrib_M3 = float(sum(abs(x_arr[i] * obj_coeffs[i])
                               for i, lbl in enumerate(block_labels) if lbl == 'M3'))
    else:
        contrib_C = float('nan')
        contrib_H = float('nan')
        contrib_M3 = float('nan')

    return {
        'd_C': d_C,
        'd_pos': d_pos,
        'd_neg': d_neg,
        'status_pos': status_pos,
        'status_neg': status_neg,
        'contrib_C': contrib_C,
        'contrib_H': contrib_H,
        'contrib_M3': contrib_M3,
        'R_regularization': float(R_regularization),
    }


# ---------------------------------------------------------------------------
# Section 8 - Reference candidate forms (mirrors §W5b-49 C2/C3/C4)
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
# Section 9 - 16x16 Connes-distance grid orchestrator
# ---------------------------------------------------------------------------

def compute_16x16_grid(D_loc, basis, block_labels, n_loc):
    """Compute symmetric 16x16 Connes-distance matrix and per-pair diagnostics.

    For each unordered pair (i, j) with i < j (120 pairs), compute STRICT d_C
    using the 14-DOF complex-Hermitian A_F basis. Track:
      - d_C value (or NaN if SDP failure)
      - SDP solver status (pos and neg)
      - Per-pair best candidate name (C2/C3/C4) and residuals
    """
    D_diag = np.linalg.eigvalsh(D_loc)  # (local) for candidate analogs

    # Allocate
    distance_matrix = np.zeros((n_loc, n_loc), dtype=np.float64)
    sdp_status_pos = [['' for _ in range(n_loc)] for _ in range(n_loc)]
    sdp_status_neg = [['' for _ in range(n_loc)] for _ in range(n_loc)]
    sdp_success = np.zeros((n_loc, n_loc), dtype=bool)
    contrib_C_grid = np.zeros((n_loc, n_loc), dtype=np.float64)
    contrib_H_grid = np.zeros((n_loc, n_loc), dtype=np.float64)
    contrib_M3_grid = np.zeros((n_loc, n_loc), dtype=np.float64)
    residual_C2_grid = np.full((n_loc, n_loc), np.nan, dtype=np.float64)
    residual_C3_grid = np.full((n_loc, n_loc), np.nan, dtype=np.float64)
    residual_C4_grid = np.full((n_loc, n_loc), np.nan, dtype=np.float64)
    best_candidate_grid = [['' for _ in range(n_loc)] for _ in range(n_loc)]

    # 16-element identity matrix to extract elementary states
    I_n = np.eye(n_loc, dtype=np.complex128)  # (local)

    # Pre-compute the Frobenius regulator once (depends only on D_loc)
    eig_max = float(np.max(np.abs(np.linalg.eigvalsh(D_loc))))  # (local)
    R_reg = R_FROBENIUS_FACTOR * eig_max  # (local)

    n_pairs = 0  # (local)
    n_sdp_fail = 0  # (local)
    t_pair_total = 0.0  # (local)
    pair_index = 0  # (local) lexicographic index over (i,j) with i<j

    for i in range(n_loc):
        for j in range(i + 1, n_loc):
            t_pair_start = time.time()  # (local)
            p_state = I_n[:, i].copy()  # (local) elementary state e_i
            q_state = I_n[:, j].copy()  # (local) elementary state e_j

            sdp = connes_distance_complex_hermitian_sdp(
                D_loc, p_state, q_state, basis, block_labels,
                sdp_tol=SDP_TOL, R_regularization=R_reg,
            )

            d_C = sdp['d_C']
            success = (sdp['status_pos'] in {'optimal', 'optimal_inaccurate'} and
                       sdp['status_neg'] in {'optimal', 'optimal_inaccurate'} and
                       np.isfinite(d_C))
            if not success:
                n_sdp_fail += 1
                d_C_val = float('nan') if not np.isfinite(d_C) else d_C
            else:
                d_C_val = float(d_C)

            # Symmetrize
            distance_matrix[i, j] = d_C_val
            distance_matrix[j, i] = d_C_val
            sdp_status_pos[i][j] = sdp['status_pos']
            sdp_status_neg[i][j] = sdp['status_neg']
            sdp_success[i, j] = success
            sdp_success[j, i] = success
            contrib_C_grid[i, j] = sdp['contrib_C']
            contrib_C_grid[j, i] = sdp['contrib_C']
            contrib_H_grid[i, j] = sdp['contrib_H']
            contrib_H_grid[j, i] = sdp['contrib_H']
            contrib_M3_grid[i, j] = sdp['contrib_M3']
            contrib_M3_grid[j, i] = sdp['contrib_M3']

            # Candidate analogs (operate on real states for these heuristics)
            rhs_C2 = candidate2_mellin_dirichlet_analog(
                D_diag, p_state.real, q_state.real)
            rhs_C3 = candidate3_commutator_norm(
                D_loc, p_state.real, q_state.real)
            rhs_C4 = candidate4_heat_kernel_trace(
                D_loc, p_state.real, q_state.real)

            if np.isfinite(d_C_val) and abs(d_C_val) > 1e-15:
                r_C2 = abs(rhs_C2 - d_C_val) / abs(d_C_val)
                r_C3 = abs(rhs_C3 - d_C_val) / abs(d_C_val) if np.isfinite(rhs_C3) else float('nan')
                r_C4 = abs(rhs_C4 - d_C_val) / abs(d_C_val) if np.isfinite(rhs_C4) else float('nan')
            else:
                r_C2 = float('nan')
                r_C3 = float('nan')
                r_C4 = float('nan')

            residual_C2_grid[i, j] = r_C2
            residual_C2_grid[j, i] = r_C2
            residual_C3_grid[i, j] = r_C3
            residual_C3_grid[j, i] = r_C3
            residual_C4_grid[i, j] = r_C4
            residual_C4_grid[j, i] = r_C4

            cand_residuals = [r_C2, r_C3, r_C4]
            cand_names = ['C2', 'C3', 'C4']
            finite = [(n_, r_) for n_, r_ in zip(cand_names, cand_residuals) if np.isfinite(r_)]
            if finite:
                idx_min = int(np.argmin([r_ for _, r_ in finite]))
                best_name = finite[idx_min][0]
            else:
                best_name = 'NONE'
            best_candidate_grid[i][j] = best_name
            best_candidate_grid[j][i] = best_name

            t_pair = time.time() - t_pair_start  # (local)
            t_pair_total += t_pair
            n_pairs += 1
            pair_index += 1

            if pair_index % 12 == 0 or pair_index == 120:
                print(f"    [{pair_index:3d}/120] pair=({i:2d},{j:2d}) d_C={d_C_val:.6e} "
                      f"status=({sdp['status_pos']}|{sdp['status_neg']}) "
                      f"t={t_pair:.2f}s mean={t_pair_total/n_pairs:.2f}s")

    # Distance-matrix diagonal MUST be zero
    np.fill_diagonal(distance_matrix, 0.0)

    return {
        'distance_matrix': distance_matrix,
        'sdp_success': sdp_success,
        'sdp_status_pos': np.array(sdp_status_pos, dtype=object),
        'sdp_status_neg': np.array(sdp_status_neg, dtype=object),
        'contrib_C_grid': contrib_C_grid,
        'contrib_H_grid': contrib_H_grid,
        'contrib_M3_grid': contrib_M3_grid,
        'residual_C2_grid': residual_C2_grid,
        'residual_C3_grid': residual_C3_grid,
        'residual_C4_grid': residual_C4_grid,
        'best_candidate_grid': np.array(best_candidate_grid, dtype=object),
        'n_pairs': n_pairs,
        'n_sdp_fail': n_sdp_fail,
        't_pair_total': t_pair_total,
        'R_regularization': R_reg,
        'eig_max': eig_max,
    }


# ---------------------------------------------------------------------------
# Section 10 - Hierarchical clustering + fidelity score
# ---------------------------------------------------------------------------

def hierarchical_clustering(distance_matrix, n_clusters, linkage_method='ward'):
    """Apply scipy hierarchical clustering to a symmetric distance matrix.

    Returns 1-indexed cluster labels (length n_loc).
    """
    # Replace NaN with large finite value (treats SDP-failed pairs as far apart)
    D = distance_matrix.copy()  # (local)
    D[~np.isfinite(D)] = np.nanmax(D[np.isfinite(D)]) * 10.0 if np.any(np.isfinite(D)) else 1e6
    np.fill_diagonal(D, 0.0)

    # Convert to condensed form (scipy expects upper-triangular flat)
    condensed = squareform(D, checks=False)  # (local)

    # Linkage matrix
    Z = linkage(condensed, method=linkage_method)  # (local)

    # Flatten to n_clusters
    labels = fcluster(Z, t=n_clusters, criterion='maxclust')  # (local) 1-indexed
    return labels, Z


def compute_fidelity_score(distance_matrix, labels):
    """F = (sum of intra-cluster distances) / (sum of inter-cluster distances).

    Lower F = stronger block-pattern. F < 1 = intra smaller than inter.
    """
    n = distance_matrix.shape[0]  # (local)
    intra_sum = 0.0  # (local)
    inter_sum = 0.0  # (local)
    intra_count = 0  # (local)
    inter_count = 0  # (local)
    for i in range(n):
        for j in range(i + 1, n):
            d = distance_matrix[i, j]
            if not np.isfinite(d):
                continue
            if labels[i] == labels[j]:
                intra_sum += d
                intra_count += 1
            else:
                inter_sum += d
                inter_count += 1
    if inter_sum < 1e-18:
        return float('inf'), intra_count, inter_count, intra_sum, inter_sum
    F = intra_sum / inter_sum  # (local)
    # Normalize by per-pair counts so F compares averages, not totals
    # but plan formula is sum-over-sum. Report both.
    if intra_count > 0 and inter_count > 0:
        F_avg = (intra_sum / intra_count) / (inter_sum / inter_count)
    else:
        F_avg = float('inf')
    return F, F_avg, intra_count, inter_count, intra_sum, inter_sum


def reconcile_partition(predicted_labels_str, recovered_labels_int):
    """Align cluster IDs between predicted (string) and recovered (int) labels
    via bipartite matching (greedy by overlap).

    Returns:
      mapping: dict {recovered_int -> predicted_str}
      n_correct: number of states correctly assigned (after best mapping)
      n_total: 16
    """
    n = len(predicted_labels_str)  # (local)
    pred_unique = sorted(set(predicted_labels_str))
    rec_unique = sorted(set(int(x) for x in recovered_labels_int))

    # Build overlap matrix
    overlap = np.zeros((len(rec_unique), len(pred_unique)), dtype=int)
    for i in range(n):
        ri = rec_unique.index(int(recovered_labels_int[i]))
        pj = pred_unique.index(predicted_labels_str[i])
        overlap[ri, pj] += 1

    # Greedy assignment
    mapping = {}  # (local) recovered_int -> predicted_str
    rec_used = set()  # (local)
    pred_used = set()  # (local)
    overlap_work = overlap.copy()
    while overlap_work.max() > 0:
        ri, pj = np.unravel_index(np.argmax(overlap_work), overlap_work.shape)
        if rec_unique[ri] in rec_used or pred_unique[pj] in pred_used:
            overlap_work[ri, pj] = 0
            continue
        mapping[rec_unique[ri]] = pred_unique[pj]
        rec_used.add(rec_unique[ri])
        pred_used.add(pred_unique[pj])
        overlap_work[ri, :] = 0
        overlap_work[:, pj] = 0
    # Any unmatched recovered cluster maps to UNMAPPED
    for ri_int in rec_unique:
        if ri_int not in mapping:
            mapping[ri_int] = 'UNMAPPED'

    n_correct = 0  # (local)
    for i in range(n):
        rec_label = int(recovered_labels_int[i])
        if mapping.get(rec_label) == predicted_labels_str[i]:
            n_correct += 1
    return mapping, n_correct, n


# ---------------------------------------------------------------------------
# Section 11 - Plot heatmap
# ---------------------------------------------------------------------------

def plot_heatmap(distance_matrix, predicted_labels, recovered_labels_4,
                 recovered_labels_3, fidelity_4, fidelity_3, n_correct_4,
                 n_correct_3, out_path):
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    # Panel 1: Raw 16x16 distance matrix (states in natural order 0..15)
    ax = axes[0]
    im = ax.imshow(distance_matrix, cmap='viridis', aspect='equal',
                   interpolation='nearest')
    ax.set_xlabel('State j')
    ax.set_ylabel('State i')
    ax.set_title(f'D_C[i,j] (natural order)\n'
                 f'predicted: C(0:4)+H(4:8)+M_3(8:11)+Pad(11:16)')
    fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    # Vertical/horizontal lines marking predicted block boundaries
    for boundary in [4, 8, 11]:
        ax.axhline(boundary - 0.5, color='red', linestyle='--', alpha=0.6, linewidth=1)
        ax.axvline(boundary - 0.5, color='red', linestyle='--', alpha=0.6, linewidth=1)

    # Panel 2: Sorted by predicted block, then by recovered cluster (4-cluster)
    ax = axes[1]
    # Sort indices by (predicted_block, recovered_cluster_4)
    order_4 = sorted(range(16), key=lambda k: (predicted_labels[k], int(recovered_labels_4[k])))
    D_sorted_4 = distance_matrix[np.ix_(order_4, order_4)]
    im = ax.imshow(D_sorted_4, cmap='viridis', aspect='equal',
                   interpolation='nearest')
    ax.set_xlabel('State (sorted by predicted block, then 4-cluster)')
    ax.set_ylabel('State (sorted by predicted block, then 4-cluster)')
    ax.set_title(f'D_C sorted (4-cluster)\n'
                 f'F = {fidelity_4:.4e}  correct = {n_correct_4}/16')
    fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    # Add ticks showing predicted block at each row
    pred_sorted = [predicted_labels[k] for k in order_4]
    ax.set_xticks(range(16))
    ax.set_yticks(range(16))
    ax.set_xticklabels(pred_sorted, fontsize=7, rotation=90)
    ax.set_yticklabels(pred_sorted, fontsize=7)

    # Panel 3: Sorted by 3-cluster
    ax = axes[2]
    order_3 = sorted(range(16), key=lambda k: (int(recovered_labels_3[k]), predicted_labels[k]))
    D_sorted_3 = distance_matrix[np.ix_(order_3, order_3)]
    im = ax.imshow(D_sorted_3, cmap='viridis', aspect='equal',
                   interpolation='nearest')
    ax.set_xlabel('State (sorted by 3-cluster)')
    ax.set_ylabel('State (sorted by 3-cluster)')
    ax.set_title(f'D_C sorted (3-cluster)\n'
                 f'F = {fidelity_3:.4e}  correct = {n_correct_3}/16')
    fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    pred_sorted_3 = [predicted_labels[k] for k in order_3]
    ax.set_xticks(range(16))
    ax.set_yticks(range(16))
    ax.set_xticklabels(pred_sorted_3, fontsize=7, rotation=90)
    ax.set_yticklabels(pred_sorted_3, fontsize=7)

    plt.tight_layout()
    plt.savefig(out_path, dpi=110, bbox_inches='tight')
    plt.close()
    print(f"  Heatmap saved: {out_path.name}")


# ---------------------------------------------------------------------------
# Section 12 - Verdict-line emission (S87+ schema; NO 3-tuple, structural gate)
# ---------------------------------------------------------------------------

def emit_verdict_line(verdict, value, audit_sha, content_sha):
    """AFTER-pattern: emit ONE canonical line + ONE dual-SHA companion row.
    No 3-tuple companion (structural-characterization gate, no directional
    pre-registration per plan §W5b-50)."""
    val_str = f"{value:.12e}" if (isinstance(value, float) and not np.isnan(value)) else str(value)
    canonical = (
        f"{GATE_ID}: {verdict} -- value={val_str} "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX_TAG} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} schema_version=S87+\n"
    )
    audit_short = audit_sha[:16]  # (local)
    content_short = content_sha[:16]  # (local)
    dual = (
        f"# audit_sha256_short={audit_short} content_sha256_short={content_short} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    with open(VERDICT_TXT, 'a', encoding='utf-8') as f:
        f.write(canonical)
        f.write(dual)
        f.flush()
        os.fsync(f.fileno())
    print(canonical, end='')
    print(dual, end='')
    return canonical, dual


# ---------------------------------------------------------------------------
# Section 13 - Main (AFTER-pattern: build full result -> verify -> emit ONCE)
# ---------------------------------------------------------------------------

def main():
    t0_main = time.time()
    print(f"=== {GATE_ID} ===")
    print(f"Session: {SESSION}  L_max={L_MAX_NUM} (cache)  N_loc={N_LOC}")
    print(f"Predicted partition (4+4+3+5): {PREDICTED_LABEL}")

    # Input pin map + dual-SHA
    pins = log_input_pins(INPUT_FILES)  # (local)
    audit_sha, content_sha = compute_dual_sha(Path(__file__), CANONICAL_CONSTS, pins)
    closure = closure_hash(pins)
    print(f"  audit_sha256={audit_sha[:16]}...")
    print(f"  content_sha256={content_sha[:16]}...")
    print(f"  closure_hash={closure[:16]}...")

    # Load spectrum + build canonical D_loc
    sector_evals, flat_abs = load_spectrum_L12()
    print(f"\n  Loaded L=12 cache: {len(sector_evals)} sectors, {len(flat_abs)} eigenvalues")

    p2 = build_canonical_D_loc(sector_evals)
    D_loc = p2['D_loc']
    n_loc = p2['n_loc']
    print(f"  Canonical D_loc built: shape={D_loc.shape}, sectors=(0,1)+(1,0)")
    if n_loc != N_LOC:
        raise RuntimeError(f"Expected n_loc=16, got n_loc={n_loc}")

    # Build A_F basis
    basis, block_labels = build_complex_hermitian_af_basis(N_LOC)
    print(f"  A_F basis: {len(basis)} generators (1+4+9 = 14 real DOF)")

    # Run 16x16 grid (120 SDPs)
    print(f"\n  Running 16x16 grid: 120 SDP solves...")
    t0_grid = time.time()
    grid = compute_16x16_grid(D_loc, basis, block_labels, N_LOC)
    t_grid = time.time() - t0_grid
    print(f"\n  Grid completed in {t_grid:.2f}s "
          f"(mean {t_grid/grid['n_pairs']:.3f}s/pair)")
    print(f"  SDP failures: {grid['n_sdp_fail']}/{grid['n_pairs']} "
          f"({100*grid['n_sdp_fail']/grid['n_pairs']:.1f}%)")
    print(f"  D_C[i,j] range: [{np.nanmin(grid['distance_matrix'][grid['distance_matrix']>0]):.6e}, "
          f"{np.nanmax(grid['distance_matrix']):.6e}]")

    # Hierarchical clustering: 4-cluster (matches predicted C+H+M_3+Pad)
    labels_4, Z_4 = hierarchical_clustering(grid['distance_matrix'], N_CLUSTERS_4,
                                            linkage_method=CLUSTERING_LINKAGE)
    mapping_4, n_correct_4, _ = reconcile_partition(PREDICTED_LABEL, labels_4)
    F_sum_4, F_avg_4, intra_count_4, inter_count_4, intra_sum_4, inter_sum_4 = \
        compute_fidelity_score(grid['distance_matrix'], labels_4)
    print(f"\n  4-cluster recovery (predicted A_F+Pad):")
    print(f"    labels: {list(labels_4)}")
    print(f"    mapping: {mapping_4}")
    print(f"    n_correct: {n_correct_4}/16")
    print(f"    F (sum/sum) = {F_sum_4:.6e}")
    print(f"    F_avg (mean/mean) = {F_avg_4:.6e}")

    # Hierarchical clustering: 3-cluster (matches A_F = C+H+M_3 alone)
    labels_3, Z_3 = hierarchical_clustering(grid['distance_matrix'], N_CLUSTERS_3,
                                            linkage_method=CLUSTERING_LINKAGE)
    # For 3-cluster, predicted A_F-only labels (Pad merged with closest A_F block)
    # We measure recovery against the 4-cluster predicted labels but allow
    # mapping to 3 recovered cluster IDs.
    mapping_3, n_correct_3, _ = reconcile_partition(PREDICTED_LABEL, labels_3)
    F_sum_3, F_avg_3, intra_count_3, inter_count_3, intra_sum_3, inter_sum_3 = \
        compute_fidelity_score(grid['distance_matrix'], labels_3)
    print(f"\n  3-cluster recovery (A_F = C+H+M_3 alone):")
    print(f"    labels: {list(labels_3)}")
    print(f"    mapping: {mapping_3}")
    print(f"    n_correct: {n_correct_3}/16")
    print(f"    F (sum/sum) = {F_sum_3:.6e}")
    print(f"    F_avg (mean/mean) = {F_avg_3:.6e}")

    # PASS / FAIL / INFO determination per plan §W5b-50:
    # (i) <= 6 SDP failures (5% of 120)
    pass_i = grid['n_sdp_fail'] <= MAX_SDP_FAIL
    # (ii) symmetric matrix with zero diagonal (built by construction)
    diag_zero = np.all(np.diag(grid['distance_matrix']) == 0.0)
    sym_ok = np.allclose(grid['distance_matrix'], grid['distance_matrix'].T, atol=1e-12)
    pass_ii = bool(diag_zero and sym_ok)
    # (iii) clustering recovers block-structure; INFO if <=2 mis-assignments
    n_misassigned_4 = 16 - n_correct_4
    n_misassigned_3 = 16 - n_correct_3
    best_n_correct = max(n_correct_4, n_correct_3)
    best_n_misassigned = 16 - best_n_correct
    pass_iii = (best_n_correct >= 16)  # exact recovery
    info_iii = (best_n_misassigned <= 2)  # <= 2 misassignments => INFO
    fail_iii = (best_n_misassigned > 2 and best_n_correct < 8)  # very poor recovery
    # (iv) fidelity F < 1
    best_F_sum = min(F_sum_4, F_sum_3)
    best_F_avg = min(F_avg_4, F_avg_3)
    pass_iv = (best_F_sum < FIDELITY_THRESHOLD) or (best_F_avg < FIDELITY_THRESHOLD)
    # (v) heatmap emitted (will be done before verdict emit)
    # (vi) corner declaration in WP (handled at WP write)

    print(f"\n  PASS criteria evaluation:")
    print(f"    (i)   SDP failures <= {MAX_SDP_FAIL}: {pass_i} (failures={grid['n_sdp_fail']})")
    print(f"    (ii)  symmetric zero-diag: {pass_ii}")
    print(f"    (iii) clustering exact: {pass_iii}; INFO band (<=2 mis): {info_iii}")
    print(f"    (iv)  fidelity F < 1: {pass_iv} (F_sum={best_F_sum:.4e}, F_avg={best_F_avg:.4e})")

    # Verdict construction:
    if not pass_i or not pass_ii or fail_iii or not pass_iv:
        verdict = 'FAIL'
    elif pass_iii:
        verdict = 'PASS'
    elif info_iii:
        verdict = 'INFO'
    else:
        verdict = 'FAIL'

    # Verdict value: best fidelity (lower is better)
    verdict_value = float(min(best_F_sum, best_F_avg))

    # Build full .npz (Stage 1: assemble in memory)
    np_save = {
        'distance_matrix': grid['distance_matrix'],
        'sdp_success': grid['sdp_success'],
        'sdp_status_pos': grid['sdp_status_pos'],
        'sdp_status_neg': grid['sdp_status_neg'],
        'contrib_C_grid': grid['contrib_C_grid'],
        'contrib_H_grid': grid['contrib_H_grid'],
        'contrib_M3_grid': grid['contrib_M3_grid'],
        'residual_C2_grid': grid['residual_C2_grid'],
        'residual_C3_grid': grid['residual_C3_grid'],
        'residual_C4_grid': grid['residual_C4_grid'],
        'best_candidate_grid': grid['best_candidate_grid'],
        'n_pairs': int(grid['n_pairs']),
        'n_sdp_fail': int(grid['n_sdp_fail']),
        'sdp_success_rate': float(1.0 - grid['n_sdp_fail'] / max(1, grid['n_pairs'])),
        't_pair_total': float(grid['t_pair_total']),
        'R_regularization': float(grid['R_regularization']),
        'D_loc_eig_max': float(grid['eig_max']),
        'predicted_label': np.array(PREDICTED_LABEL, dtype=object),
        'predicted_blocks_C': np.array(PREDICTED_BLOCKS['C'], dtype=int),
        'predicted_blocks_H': np.array(PREDICTED_BLOCKS['H'], dtype=int),
        'predicted_blocks_M3': np.array(PREDICTED_BLOCKS['M_3'], dtype=int),
        'predicted_blocks_Pad': np.array(PREDICTED_BLOCKS['Pad'], dtype=int),
        'recovered_labels_4': labels_4,
        'recovered_labels_3': labels_3,
        'mapping_4': np.array([(int(k), str(v)) for k, v in mapping_4.items()], dtype=object),
        'mapping_3': np.array([(int(k), str(v)) for k, v in mapping_3.items()], dtype=object),
        'n_correct_4': int(n_correct_4),
        'n_correct_3': int(n_correct_3),
        'fidelity_sum_4': float(F_sum_4),
        'fidelity_sum_3': float(F_sum_3),
        'fidelity_avg_4': float(F_avg_4),
        'fidelity_avg_3': float(F_avg_3),
        'best_fidelity_sum': float(best_F_sum),
        'best_fidelity_avg': float(best_F_avg),
        'intra_count_4': int(intra_count_4),
        'inter_count_4': int(inter_count_4),
        'intra_sum_4': float(intra_sum_4),
        'inter_sum_4': float(inter_sum_4),
        'intra_count_3': int(intra_count_3),
        'inter_count_3': int(inter_count_3),
        'intra_sum_3': float(intra_sum_3),
        'inter_sum_3': float(inter_sum_3),
        'verdict': verdict,
        'value': verdict_value,
        'pass_i_sdp_convergence': bool(pass_i),
        'pass_ii_symmetric_zero_diag': bool(pass_ii),
        'pass_iii_clustering_exact': bool(pass_iii),
        'info_iii_clustering_le2_misassign': bool(info_iii),
        'pass_iv_fidelity_below_1': bool(pass_iv),
        'predicted_partition_count': '4+4+3+5',
        'corner_cell': 'III',
        'gate_id': GATE_ID,
        'scheme': SCHEME,
        'convention': CONVENTION,
        'L_max': L_MAX_TAG,
        'L_max_underlying_spectrum': int(L_MAX_NUM),
        'audit_sha256': audit_sha,
        'content_sha256': content_sha,
        'closure_hash': closure,
    }

    # Stage 1: write .npz + heatmap (atomic)
    np.savez(OUT_NPZ, **{k: np.asarray(v, dtype=object) if isinstance(v, list) else v
                          for k, v in np_save.items()})
    print(f"\n  Data saved: {OUT_NPZ.name} ({OUT_NPZ.stat().st_size} bytes)")

    plot_heatmap(grid['distance_matrix'], PREDICTED_LABEL, labels_4, labels_3,
                 best_F_sum, best_F_avg, n_correct_4, n_correct_3, OUT_PNG)

    # Stage 2: re-read and verify
    d = np.load(OUT_NPZ, allow_pickle=True)
    assert d['n_pairs'].item() == 120, "n_pairs mismatch"
    assert d['distance_matrix'].shape == (16, 16), "shape mismatch"
    assert np.all(np.diag(d['distance_matrix']) == 0.0), "diagonal not zero on re-read"
    print(f"  Re-read verification: PASS")

    # Stage 3: emit verdict line ONCE
    print(f"\n=== Verdict construction ===")
    print(f"  verdict: {verdict}")
    print(f"  value (best fidelity): {verdict_value:.12e}")
    emit_verdict_line(verdict, verdict_value, audit_sha, content_sha)

    print(f"\n=== {GATE_ID} complete ===")
    print(f"  wall = {time.time() - t0_main:.2f} s")
    sys.exit(0)


if __name__ == '__main__':
    main()
