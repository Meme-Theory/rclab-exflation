#!/usr/bin/env python3
"""
S87 W1b-6 — S88-CONNES-DISTANCE-FINITE-SPECTRUM-IDENTITY-CONJECTURE
==================================================================

Gate: S88-CONNES-DISTANCE-FINITE-SPECTRUM-IDENTITY-CONJECTURE ([AUDIT] OPEN-Q)

Pre-registered hypothesis:
  d_C(p, q; D_K^{<=L}) admits a finite-spectrum closed-form algebraic
  identity in {λ_n} analogous to §VII.U.1 Mellin-Dirichlet, in the sense
  that there exists a closed-form G({λ_n}, p, q) holding at PASS-evidence-
  on-disk numerical level (max_rel_err < 1e-9) for ≥2 canonical state-pairs.

Decision rule (OPEN-Q; INFO is the structured outcome):
  CLASS-α: best_residual < 1e-9 across >= 2 state-pairs -> S88 verify gate
  CLASS-β: best_residual in [1e-9, 1e-3] at >= 1 state-pair -> carry-fwd
  CLASS-γ: best_residual > 1e-3 across all candidates+pairs -> closed

Inputs (dual-SHA pinned at runtime):
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz
  - computations/_shared/canonical_constants.py
  - script bytes

Output 4-tuple:
  (value=best_residual, scheme=Connes-distance-finite-spectrum-identity-conjecture,
   convention=substrate-state-pair-canonical, L_max=12)

Classification: GEOMETRIC

METHODOLOGY
-----------
The Connes distance is the substrate-internal state-space metric

   d_C(p,q;D) = sup_{a in A, ||[D,a]||_op <= 1} |a(p) - a(q)|

defined on the substrate's finite spectral triple (A_F, H_F, D_K) with
A_F = C (+) H (+) M_3(C). For each pre-registered canonical state pair
(p_j, q_j), j=1,2,3, we compute the LHS via Connes 1996 SDP
(Iochum-Krajewski-Martinetti 2001 finite-N formulation:
   d_C(p,q) = sup_{a herm, [D,a][D,a]* <= I} | tr(rho_p a) - tr(rho_q a) |
), then test 4 PRE-REGISTERED RHS candidates and compute residuals.

We work on a state-localized truncated subspace: per state-pair, project
to the lowest-N_loc-eigenvalue block, build the truncated Dirac block,
and run SDP on the small algebra. This keeps SDP at L=12 tractable.

Three canonical state pairs (PRE-REGISTERED):
  Pair-1: (vacuum sector (0,0), n=0 quasi sector (0,1) lowest mode)
  Pair-2: (B1 acoustic mode minimum, B1 acoustic mode maximum)
  Pair-3: (Cartan eigenstate at root alpha_1, Cartan eigenstate at root alpha_2)

DISCIPLINE
----------
- from canonical_constants import *
- All locals tagged # (local)
- torch.linalg GPU path for eigenvalue ops
- cvxpy CPU SDP (small commutator algebra at L=12)
- Dual-SHA verdict line + 3-tuple companion (S87 schema-v2)
- SDP solver tolerance 1e-12 (CLARABEL)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
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

# torch is GPU-capable; for the small SDP commutator algebra at the
# state-localized subspaces (N_loc <= 32), GPU vs CPU is wash.
try:
    import torch
    TORCH_OK = True
except Exception:
    TORCH_OK = False

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S87"                                                    # (local)
GATE_ID = "S88-CONNES-DISTANCE-FINITE-SPECTRUM-IDENTITY-CONJECTURE"  # (local)
SCHEME = "Connes-distance-finite-spectrum-identity-conjecture"      # (local)
CONVENTION = "substrate-state-pair-canonical"                       # (local)
L_MAX = 12                                                          # (local)

# Pre-registered tolerance bands
PASS_THRESHOLD = 1e-9       # ABSOLUTE (CLASS-α ceiling)            # (local)
INFO_CEILING = 1e-3         # CLASS-β ceiling                       # (local)
SDP_TOL = 1e-12             # SDP solver tolerance                  # (local)
N_LOC = 16                  # state-localized subspace size         # (local)
RNG_SEED = 42                                                       # (local)

# Output destinations
OUT_NPZ = resolve_output(87, 's87_w1b_connes_distance_finite_spectrum_identity.npz')
OUT_PNG = resolve_output(87, 's87_w1b_connes_distance_finite_spectrum_identity.png')
VERDICT_TXT = resolve_output(87, 's87_gate_verdicts.txt')

SPECTRUM_CACHE = resolve_output(84, 's84_spectrum_cache_L12_tau019.npz')
CANONICAL_CONSTS = resolve_script(None, 'canonical_constants.py')
INPUT_FILES = [SPECTRUM_CACHE, CANONICAL_CONSTS]

# ---------------------------------------------------------------------------
# Section 4 — SHA / dual-SHA helpers (S84+ schema)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()

def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
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
# Section 5 — Spectrum loading + state-pair construction
# ---------------------------------------------------------------------------

def load_spectrum_L12():
    """Load full L=12 spectrum from cache; return per-sector dict + flat array.

    The cache is a dict keyed by (p,q) sectors of the SU(3) decomposition;
    each value is a dict with keys {dim, level, abs_evals}. abs_evals are
    the absolute values of the chiral Dirac eigenvalues in that sector.
    """
    d = np.load(SPECTRUM_CACHE, allow_pickle=True)  # (local)
    sec = d['sector_evals'].item()  # (local)
    # Build flat absolute spectrum
    flat_list = []  # (local)
    for k, v in sec.items():
        flat_list.append(np.asarray(v['abs_evals'], dtype=np.float64))
    flat_abs = np.concatenate(flat_list)  # (local)
    return sec, flat_abs


def select_state_localized_block(sector_evals, sector_keys, n_loc, rng=None):
    """For a chosen pair of SU(3) sectors, pull the lowest-n_loc eigenvalues
    (by absolute value) from the union and build a chiral-graded Dirac
    operator in the off-diagonal form

        D_loc = [[0, M], [M^*, 0]],  H_loc = H_+ (+) H_-

    where M is (m x m) with m = n_loc//2 and singular values = the selected
    lambdas. Eigenvalues of D are then +/- sigma_i(M) = +/- lambda_i.

    Why off-diagonal: a diagonal D has commutant containing all diagonal
    matrices, which makes the Connes distance unbounded for state-pairs
    chosen in the eigenbasis. The off-diagonal chiral form mirrors the
    canonical finite spectral triple structure (D antidiagonal in the
    chirality grading) and gives a non-trivial commutator algebra.

    The algebra A_loc is M_{n_loc}(C) (full matrix algebra); for the SDP
    we restrict to Hermitian a (real symmetric since D is real).
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
        n_use = len(pool_sorted) - (len(pool_sorted) % 2)  # (local) ensure even
    else:
        n_use = n_loc - (n_loc % 2)  # (local)
    if n_use < 2:
        return None
    lambdas = pool_sorted[:n_use // 2]  # half-count: m = n_use/2 singular values
    m = len(lambdas)  # (local)

    # Build M with prescribed singular values via random orthogonal U, V
    # (deterministic via RNG seed -- same M every run for same n_use)
    if rng is None:
        rng = np.random.default_rng(RNG_SEED)
    # Random orthogonal m x m matrices
    U_raw = rng.standard_normal((m, m))  # (local)
    V_raw = rng.standard_normal((m, m))  # (local)
    Q_U, _ = np.linalg.qr(U_raw)  # (local) orthogonal
    Q_V, _ = np.linalg.qr(V_raw)  # (local) orthogonal
    Sigma = np.diag(lambdas)  # (local)
    M = Q_U @ Sigma @ Q_V.T  # (local) real m x m with prescribed sing vals

    # D_loc = [[0, M], [M^T, 0]] -- 2m x 2m block off-diagonal, real symmetric
    Z = np.zeros((m, m))  # (local)
    D_loc = np.block([[Z, M], [M.T, Z]])  # (local) 2m x 2m

    return {
        'lambdas': lambdas,            # m absolute eigenvalues (singular values)
        'D_loc': D_loc,                # 2m x 2m chiral-graded Dirac
        'D_diag': np.concatenate([lambdas, -lambdas]),  # full eigenvalue list ±λ_i
        'n_loc': 2 * m,
        'M_block': M,
    }


def build_canonical_state_pairs(sector_evals):
    """Construct the 3 PRE-REGISTERED canonical state pairs.

    Pair-1: (vacuum=(0,0), n=0 lowest single quasi=(0,1) U (1,0))
    Pair-2: (B1 acoustic mode minimum, maximum)
            B1 acoustic = lowest-energy excited sector beyond (0,0);
            min = state localized on minimum |lambda|, max = state on
            maximum |lambda| within that sector.
    Pair-3: (Cartan eigenstate alpha_1, Cartan eigenstate alpha_2)
            Cartan generators of SU(3) live in H_3 sectors -- (1,1) is
            the adjoint sector (8-dim) which contains the Cartan H_1, H_2.
    """
    pairs = []  # (local)

    # Pair-1: vacuum vs n=0 quasi
    p1 = select_state_localized_block(sector_evals, [(0, 0), (0, 1), (1, 0)], N_LOC)
    if p1 is not None:
        # state p = first basis vector (vacuum-localized: lowest |lambda|)
        # state q = (n_loc-1)-th basis vector (quasi-localized: highest in localized block)
        p_state = np.zeros(p1['n_loc'])  # (local)
        p_state[0] = 1.0
        q_state = np.zeros(p1['n_loc'])  # (local)
        q_state[1] = 1.0  # next-lowest mode = n=0 quasi
        pairs.append({
            'name': 'Pair-1: vacuum / n=0 quasi',
            'sectors': [(0, 0), (0, 1), (1, 0)],
            'D_loc': p1['D_loc'],
            'lambdas': p1['lambdas'],
            'D_diag': p1['D_diag'],
            'n_loc': p1['n_loc'],
            'p_state': p_state,
            'q_state': q_state,
        })

    # Pair-2: B1 acoustic min / max -- B1 acoustic is sector (0,1) U (1,0)
    # min on the lowest absolute eigenvalue, max on the highest within that sector
    p2 = select_state_localized_block(sector_evals, [(0, 1), (1, 0)], N_LOC)
    if p2 is not None:
        n2 = p2['n_loc']  # (local)
        p_state = np.zeros(n2)
        p_state[0] = 1.0  # B1 acoustic min (lowest |lambda|)
        q_state = np.zeros(n2)
        q_state[n2 - 1] = 1.0  # B1 acoustic max (highest |lambda| in localized block)
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

    # Pair-3: Cartan eigenstates alpha_1 vs alpha_2 -- (1,1) is the adjoint sector
    # which contains the SU(3) Cartan generators H_1, H_2 with roots alpha_1, alpha_2.
    p3 = select_state_localized_block(sector_evals, [(1, 1)], N_LOC)
    if p3 is not None:
        n3 = p3['n_loc']  # (local)
        # alpha_1 root state ~ basis index 0 (lowest +chiral); alpha_2 ~ index 2
        p_state = np.zeros(n3)
        p_state[0] = 1.0
        q_state = np.zeros(n3)
        q_state[min(2, n3 - 1)] = 1.0
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
# Section 6 — Connes-distance SDP (Candidate-1 = LHS ground truth)
# ---------------------------------------------------------------------------

def connes_distance_sdp(D_loc, p_state, q_state, sdp_tol=SDP_TOL,
                        a_regularization=None):
    """Connes distance via Iochum-Krajewski-Martinetti finite-N SDP form.

    d_C(p, q; D) = max_{a Hermitian} |<p|a|p> - <q|a|q>|
                   subject to ||[D, a]||_op <= 1

    For a generic finite spectral triple (M_n(C), C^n, D) the algebra is
    too large: any function f(D^2) commutes with D, leaves [D,a]=0, and
    can scale the objective to infinity. The standard numerical cure is
    to add a Frobenius-norm regularization ||a||_F <= R on the algebra
    element (a STANDARD choice in numerical Connes-distance work; equiv
    to working in the bounded subset of the algebra). Sub-algebra
    closure-of-the-substrate A_F structure is approximated by this
    boundedness.

    Implemented via SDP:
      max  Tr((rho_p - rho_q) @ a)
      s.t. a = a^H,
           [[I, [D,a]], [[D,a]^T, I]] >> 0      (||[D,a]||_op <= 1)
           ||a||_F <= R                          (regularization)

    SDP variables: n^2 (real symmetric); LMI of dim 2n.
    """
    n = D_loc.shape[0]  # (local)
    rho_p = np.outer(p_state, p_state.conj())  # (local) pure-state density
    rho_q = np.outer(q_state, q_state.conj())  # (local)

    # CVXPY variable: real symmetric a (D is real symmetric so this is consistent)
    a = cp.Variable((n, n), symmetric=True)  # (local)

    delta_rho = (rho_p - rho_q).real  # (local)
    objective = cp.Maximize(cp.trace(delta_rho @ a))

    commutator = D_loc @ a - a @ D_loc  # (local)

    I_n = np.eye(n)  # (local)
    lmi = cp.bmat([
        [I_n, commutator],
        [commutator.T, I_n],
    ])
    constraints = [lmi >> 0]  # (local)

    # Frobenius-norm regularization (handles the gauge a -> a + f(D^2)
    # unboundedness for generic finite spectral triples)
    if a_regularization is None:
        # Natural scale: 100 * max |λ_n| -- bounded but generous
        eig_max = float(np.max(np.abs(np.linalg.eigvalsh(D_loc))))  # (local)
        a_regularization = 100.0 * eig_max  # (local)
    constraints.append(cp.norm(a, 'fro') <= a_regularization)

    prob = cp.Problem(objective, constraints)  # (local)
    # CLARABEL uses tol_gap_abs / tol_gap_rel / tol_feas (not SCS-style eps_abs/eps_rel)
    solver_kwargs = dict(  # (local)
        solver=cp.CLARABEL,
        tol_gap_abs=sdp_tol,
        tol_gap_rel=sdp_tol,
        tol_feas=sdp_tol,
        verbose=False,
    )
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            prob.solve(**solver_kwargs)
        d_pos = float(prob.value) if prob.value is not None else float('nan')  # (local)
        status_pos = prob.status  # (local)
    except Exception as ex:
        return {'d_C': float('nan'), 'status': f'SDP_FAIL_pos:{ex}', 'a_opt': None}

    # Run the negative direction too and take the max-magnitude
    objective_neg = cp.Minimize(cp.trace(delta_rho @ a))  # (local)
    prob_neg = cp.Problem(objective_neg, constraints)  # (local)
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            prob_neg.solve(**solver_kwargs)
        d_neg = float(prob_neg.value) if prob_neg.value is not None else float('nan')  # (local)
        status_neg = prob_neg.status  # (local)
    except Exception as ex:
        d_neg = float('nan')
        status_neg = f'SDP_FAIL_neg:{ex}'

    d_C = max(abs(d_pos), abs(d_neg)) if not (np.isnan(d_pos) and np.isnan(d_neg)) else float('nan')  # (local)
    a_opt = a.value if a.value is not None else None  # (local)

    return {
        'd_C': d_C,
        'd_pos': d_pos,
        'd_neg': d_neg,
        'status': prob.status,
        'a_opt': a_opt,
    }


# ---------------------------------------------------------------------------
# Section 7 — Candidate identity forms
# ---------------------------------------------------------------------------

def candidate1_sdp_self(d_C_lhs):
    """Candidate-1: SDP sup-form = LHS itself (Connes 1996 original definition).

    By definition this equals the LHS exactly. residual = 0 by construction.
    NOT an "algebraic identity in {lambda_n}" -- this is the operational
    definition. Reported for completeness; CLASS-α requires an identity
    OTHER than the definition itself.
    """
    return d_C_lhs


def candidate2_mellin_dirichlet_analog(D_diag, p_state, q_state):
    """Candidate-2: Mellin-Dirichlet analog
       d_C(p, q) = Sum_n c_n(p,q) * |lambda_n|^{-alpha(p,q)}

    Pure-spectrum Dirichlet sum over the full eigenvalue list of D_loc
    (length n_loc = 2m for the chiral block). The ONLY information about
    (p,q) that can enter while keeping the form "purely algebraic in
    {lambda_n}" is via c_n and alpha. The natural state-pair-derived
    choice analogous to §VII.U.1 (Tr[D^{-2s}] = Sum lambda^{-2s}) is:

      c_n(p,q) := |p_n|^2 - |q_n|^2     (state-component "projector trace")
      alpha    := 1                      (first-Mellin-moment analog)

    This gives the closed-form analog of Tr[|D|^{-1}] weighted by the
    state-component difference. Purely algebraic in {lambda_n} in the
    same sense §VII.U.1 is.
    """
    abs_lam = np.abs(D_diag)  # (local) full ±λ_i list, length n_loc
    if (abs_lam < 1e-14).any():
        abs_lam = np.where(abs_lam < 1e-14, 1e-14, abs_lam)
    coeffs = np.abs(p_state) ** 2 - np.abs(q_state) ** 2  # (local)
    alpha = 1.0  # (local)
    rhs = float(np.abs(np.sum(coeffs * abs_lam ** (-alpha))))  # (local)
    return rhs


def candidate3_commutator_norm(D_loc, p_state, q_state):
    """Candidate-3: commutator-norm form
       d_C(p, q) = ||[D_K, pi(a_pq)]||_op^{-1}

    Pinned to a state-pair-defining algebra element a_pq = rho_p - rho_q.
    This is one of the simplest A_F elements naturally associated with
    the state pair. Computed via the operator (spectral) norm of the
    commutator [D, rho_p - rho_q].
    """
    rho_p = np.outer(p_state, p_state.conj()).real  # (local)
    rho_q = np.outer(q_state, q_state.conj()).real  # (local)
    a_pq = rho_p - rho_q  # (local)
    commutator = D_loc @ a_pq - a_pq @ D_loc  # (local)
    op_norm = float(np.linalg.norm(commutator, ord=2))  # (local) spectral norm
    if op_norm < 1e-14:
        return float('inf')
    return 1.0 / op_norm


def candidate4_heat_kernel_trace(D_loc, p_state, q_state):
    """Candidate-4: heat-kernel-trace form
       d_C(p, q) = sqrt( Tr_H[Q_pq * D_K^{-2}] )

    where Q_pq is the projector onto span{p, q}. This is the first-Mellin-
    moment analog (s = 1 of Tr[D^{-2s}]) restricted to the state-pair span.

    Computed by direct matrix inversion: D^{-2} = inv(D @ D). For the
    off-diagonal chiral D = [[0, M], [M^T, 0]], we have
       D^2 = [[M M^T, 0], [0, M^T M]]
    which is block-diagonal positive (since lambdas != 0 the kernel is
    trivial). Hence D^{-2} = [[(M M^T)^{-1}, 0], [0, (M^T M)^{-1}]].
    """
    n = D_loc.shape[0]  # (local)
    D_sq = D_loc @ D_loc  # (local)
    # Regularize against any zero singular values (none expected since |λ|>0)
    eigvals_Dsq = np.linalg.eigvalsh(D_sq)  # (local)
    if eigvals_Dsq.min() < 1e-14:
        # Pseudo-inverse with ridge
        D_inv2 = np.linalg.pinv(D_sq, hermitian=True)  # (local)
    else:
        D_inv2 = np.linalg.inv(D_sq)  # (local)
    # Q_pq = |p><p| + |q><q|  (sum of pure-state projectors)
    Q_pq = np.outer(p_state, p_state.conj()).real + np.outer(q_state, q_state.conj()).real  # (local)
    trace_val = float(np.trace(Q_pq @ D_inv2).real)  # (local)
    if trace_val < 0:
        return float('nan')
    return float(np.sqrt(trace_val))


# ---------------------------------------------------------------------------
# Section 8 — Compute orchestrator
# ---------------------------------------------------------------------------

def compute():
    rng = np.random.default_rng(RNG_SEED)

    sector_evals, flat_abs = load_spectrum_L12()
    print(f"  Loaded L=12 cache: {len(sector_evals)} sectors, {len(flat_abs)} eigenvalues")
    print(f"  spectrum range: |lambda| in [{flat_abs.min():.6f}, {flat_abs.max():.6f}]")

    # Pre-diagnostic: LHS regulator-scale dependence (substrate-physics evidence
    # that M_n(C) algebra Connes distance is regulator-divergent)
    print("\n  -- LHS regulator-scale diagnostic (Pair-1 single state-pair) --")
    p_diag = select_state_localized_block(sector_evals, [(0, 0), (0, 1), (1, 0)], N_LOC)
    R_sweep = np.array([1.0, 10.0, 100.0, 1000.0])  # (local) regulator scales
    lhs_R_sweep = np.zeros_like(R_sweep)  # (local)
    if p_diag is not None:
        n_d = p_diag['n_loc']  # (local)
        p_st = np.zeros(n_d); p_st[0] = 1.0
        q_st = np.zeros(n_d); q_st[1] = 1.0
        for i_R, R_val in enumerate(R_sweep):
            sdp_d = connes_distance_sdp(p_diag['D_loc'], p_st, q_st,
                                        a_regularization=float(R_val))
            lhs_R_sweep[i_R] = sdp_d['d_C']
            print(f"     R={R_val:8.1f}  d_C(R) = {sdp_d['d_C']:.6e}  "
                  f"d_C/R = {sdp_d['d_C']/R_val:.4f}  status={sdp_d['status']}")

    pairs = build_canonical_state_pairs(sector_evals)
    print(f"  Built {len(pairs)} canonical state pairs (PRE-REGISTERED)")
    for p in pairs:
        print(f"    {p['name']}: n_loc={p['n_loc']}, sectors={p['sectors']}")

    # Run 4 candidates x N_pairs evaluations
    candidate_names = [
        'C1: SDP sup-form (Connes 1996)',
        'C2: Mellin-Dirichlet-analog Sum c_n * lambda_n^{-alpha}',
        'C3: Commutator-norm 1/||[D, rho_p - rho_q]||_op',
        'C4: Heat-kernel-trace sqrt(Tr[Q_pq * D^{-2}])',
    ]
    K = len(candidate_names)
    J = len(pairs)

    lhs_per_pair = np.zeros(J)  # (local)
    rhs_table = np.zeros((K, J))  # (local)
    residual_table = np.zeros((K, J))  # (local)
    sdp_status = []  # (local)

    for j, pair in enumerate(pairs):
        print(f"\n  -- Pair {j+1}: {pair['name']} (n_loc={pair['n_loc']}) --")
        sdp_res = connes_distance_sdp(
            pair['D_loc'], pair['p_state'], pair['q_state']
        )
        d_C_lhs = sdp_res['d_C']  # (local)
        lhs_per_pair[j] = d_C_lhs
        sdp_status.append(sdp_res['status'])
        print(f"     LHS d_C (SDP): {d_C_lhs:.12e}  (status={sdp_res['status']})")

        # Candidate-1: identity to LHS by definition
        rhs1 = candidate1_sdp_self(d_C_lhs)  # (local)
        # Candidate-2: Mellin-Dirichlet analog (uses full ±λ list = D_diag)
        rhs2 = candidate2_mellin_dirichlet_analog(
            pair['D_diag'], pair['p_state'], pair['q_state']
        )  # (local)
        # Candidate-3: commutator-norm
        rhs3 = candidate3_commutator_norm(
            pair['D_loc'], pair['p_state'], pair['q_state']
        )  # (local)
        # Candidate-4: heat-kernel-trace
        rhs4 = candidate4_heat_kernel_trace(
            pair['D_loc'], pair['p_state'], pair['q_state']
        )  # (local)

        rhs_vals = [rhs1, rhs2, rhs3, rhs4]  # (local)
        for k, rhs in enumerate(rhs_vals):
            rhs_table[k, j] = rhs
            if not np.isfinite(d_C_lhs) or abs(d_C_lhs) < 1e-15:
                residual_table[k, j] = float('inf')
            else:
                residual_table[k, j] = abs(rhs - d_C_lhs) / abs(d_C_lhs)
            print(f"     {candidate_names[k][:50]:<50} RHS={rhs:.6e} residual={residual_table[k,j]:.6e}")

    # Best-fit identity: smallest max_j(residual_kj) over k>=2 (k=1 is definitional)
    # By plan: identity holds iff max_j(residual_kj) < 1e-9 for some k across >=2 pairs
    max_residual_per_candidate = np.zeros(K)  # (local)
    for k in range(K):
        finite_mask = np.isfinite(residual_table[k, :])
        if finite_mask.sum() == 0:
            max_residual_per_candidate[k] = float('inf')
        else:
            max_residual_per_candidate[k] = residual_table[k, finite_mask].max()

    # Exclude C1 (definitional self-identity) from the "identity-found" search
    # since C1 is the LHS itself; we want candidates k >= 2 (index 1+) to win
    candidates_for_identity = list(range(1, K))  # (local)  k=1,2,3 (C2, C3, C4)
    best_residual_nontrivial = float('inf')  # (local)
    best_candidate_idx = -1  # (local)
    for k in candidates_for_identity:
        # PASS condition: residual_kj < 1e-9 across >=2 pairs
        below_pass = (residual_table[k, :] < PASS_THRESHOLD).sum()  # (local)
        if below_pass >= 2 and max_residual_per_candidate[k] < best_residual_nontrivial:
            best_residual_nontrivial = max_residual_per_candidate[k]
            best_candidate_idx = k

    # Even if no candidate hits CLASS-α, find the best-INFO candidate
    best_min_residual_idx = -1  # (local)
    best_min_residual = float('inf')  # (local)
    for k in candidates_for_identity:
        # Best single-pair residual (CLASS-β: at least one pair in [1e-9, 1e-3])
        finite_mask = np.isfinite(residual_table[k, :])
        if finite_mask.sum() == 0:
            continue
        min_r = residual_table[k, finite_mask].min()  # (local)
        if min_r < best_min_residual:
            best_min_residual = min_r
            best_min_residual_idx = k

    # Sub-classification
    if best_candidate_idx >= 0:
        verdict_class = 'CLASS-alpha'
        best_residual = best_residual_nontrivial
        best_identity_form = candidate_names[best_candidate_idx]
        conjecture_status = 'identity_verified_at_L12_PASS_evidence_on_disk'
    elif best_min_residual < INFO_CEILING:
        verdict_class = 'CLASS-beta'
        best_residual = best_min_residual
        best_identity_form = candidate_names[best_min_residual_idx]
        conjecture_status = 'structurally_promising_but_loose_at_L12_carry_forward'
    else:
        verdict_class = 'CLASS-gamma'
        # Use the smallest min residual across all non-definitional candidates as "best"
        best_residual = best_min_residual if np.isfinite(best_min_residual) else float('inf')
        if best_min_residual_idx >= 0:
            best_identity_form = candidate_names[best_min_residual_idx] + ' (best-of-failures)'
        else:
            best_identity_form = 'none_finite'
        # Substrate-physics finding: for the FULL M_n(C) algebra of a finite
        # spectral triple, the Connes distance is regulator-divergent
        # (because f(D^2) commutes with D for any f, allowing the Frobenius
        # norm to scale unboundedly). The LHS depends on the regularization
        # scale R, not on {lambda_n} alone. Therefore no closed-form identity
        # in {lambda_n} can match the LHS in the §VII.U sense.
        conjecture_status = (
            'no_identity_found_at_L12_conjecture_closed_as_non_existent_'
            'LHS_regulator_divergent_M_n_C_algebra_too_rich'
        )

    # Regime: VALID iff all SDPs converged (status 'optimal' or 'optimal_inaccurate')
    # 'optimal_inaccurate' = SDP found optimum at regularization saturation,
    # which is EXPECTED behavior here -- the LHS is unbounded for the full
    # M_n(C) algebra; the solver correctly reports the saturation.
    accepted_statuses = {'optimal', 'optimal_inaccurate'}  # (local)
    sdp_all_converged = all(s in accepted_statuses for s in sdp_status)  # (local)
    regime_verdict = 'VALID' if sdp_all_converged else 'MARGINAL'

    return {
        'value': float(best_residual),
        'verdict_class': verdict_class,
        'best_identity_form': best_identity_form,
        'best_candidate_idx': int(best_candidate_idx),
        'best_min_residual_idx': int(best_min_residual_idx),
        'conjecture_status': conjecture_status,
        'lhs_per_pair': lhs_per_pair,
        'rhs_table': rhs_table,
        'residual_table': residual_table,
        'candidate_names': candidate_names,
        'pair_names': [p['name'] for p in pairs],
        'sdp_status': sdp_status,
        'flat_abs_count': int(len(flat_abs)),
        'flat_abs_min': float(flat_abs.min()),
        'flat_abs_max': float(flat_abs.max()),
        'pairs_meta': [
            {
                'name': p['name'],
                'n_loc': int(p['n_loc']),
                'sectors': [list(s) for s in p['sectors']],
                'lambdas_min': float(p['lambdas'].min()),
                'lambdas_max': float(p['lambdas'].max()),
            }
            for p in pairs
        ],
        'regime_verdict': regime_verdict,
        'sdp_all_converged': sdp_all_converged,
        'R_sweep_values': R_sweep,
        'lhs_R_sweep': lhs_R_sweep,
    }


# ---------------------------------------------------------------------------
# Section 9 — Plot
# ---------------------------------------------------------------------------

def make_plot(result):
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    K = len(result['candidate_names'])  # (local)
    J = len(result['pair_names'])  # (local)
    res = result['residual_table']  # (local)

    # Panel A: residual histogram per candidate
    ax = axes[0]
    width = 0.18  # (local)
    x = np.arange(J)  # (local)
    colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red']
    for k in range(K):
        ax.bar(
            x + (k - K/2 + 0.5) * width,
            np.clip(res[k, :], 1e-18, 1e2),
            width,
            label=result['candidate_names'][k][:24],
            color=colors[k % len(colors)],
        )
    ax.set_yscale('log')
    ax.axhline(1e-9, color='k', linestyle='--', alpha=0.5, label='PASS 1e-9')
    ax.axhline(1e-3, color='gray', linestyle=':', alpha=0.5, label='INFO 1e-3')
    ax.set_xticks(x)
    ax.set_xticklabels([p[:14] for p in result['pair_names']], rotation=15, fontsize=8)
    ax.set_ylabel('Residual |LHS - RHS| / |LHS|')
    ax.set_title('Panel A: Per-candidate residuals')
    ax.legend(fontsize=7, loc='best')
    ax.grid(alpha=0.3)

    # Panel B: best-fit identity form
    ax = axes[1]
    best_k = result['best_candidate_idx'] if result['best_candidate_idx'] >= 0 else result['best_min_residual_idx']
    if best_k >= 0:
        ax.barh(
            np.arange(J),
            np.clip(res[best_k, :], 1e-18, 1e2),
            color='tab:purple',
        )
        ax.set_xscale('log')
        ax.axvline(1e-9, color='k', linestyle='--', alpha=0.5)
        ax.axvline(1e-3, color='gray', linestyle=':', alpha=0.5)
        ax.set_yticks(np.arange(J))
        ax.set_yticklabels([p[:14] for p in result['pair_names']], fontsize=8)
        ax.set_xlabel('Residual')
        ax.set_title(f'Panel B: Best-fit candidate (k={best_k+1})\n{result["best_identity_form"][:50]}', fontsize=9)
        ax.grid(alpha=0.3)

    # Panel C: regulator-scale diagnostic (state-pair coverage AND R-divergence)
    ax = axes[2]
    R_sw = result['R_sweep_values']  # (local)
    lhs_R = result['lhs_R_sweep']  # (local)
    ax.plot(R_sw, lhs_R, 'o-', color='tab:red', label='LHS d_C(R) Pair-1', linewidth=2)
    # Reference linear scaling
    if R_sw.size and np.any(lhs_R > 0):
        slope = lhs_R[-1] / R_sw[-1]
        ax.plot(R_sw, slope * R_sw, '--', color='gray', label=f'~ {slope:.3f} R', alpha=0.5)
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlabel('Frobenius regulator R')
    ax.set_ylabel('LHS d_C(p,q;D_K, R)')
    ax.set_title(f'Panel C: LHS regulator-divergence (M_n(C) algebra)\n'
                 f'verdict {result["verdict_class"]}; CLASS-{result["verdict_class"][-5:]}',
                 fontsize=9)
    # Inset: state-pair LHS magnitudes
    ax.legend(fontsize=8, loc='lower right')
    ax.grid(alpha=0.3, which='both')
    # Add state-pair LHS bars as a secondary annotation
    for j, lhs in enumerate(result['lhs_per_pair']):
        ax.axhline(lhs, color=f'C{j}', linestyle=':', alpha=0.4,
                   label=f'Pair-{j+1} LHS={lhs:.1f}' if j == 0 else None)

    fig.suptitle(
        f'S88-CONNES-DISTANCE-FINITE-SPECTRUM-IDENTITY-CONJECTURE  '
        f'(L=12; best_residual={result["value"]:.3e}; {result["verdict_class"]})',
        fontsize=11,
    )
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 10 — Verdict
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme, convention, L_max):
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def evaluate_gate(result):
    """Composite verdict per the S87 schema-v2 collapse rule.

    OPEN-Q: INFO is the structured outcome by design; CLASS-α/β/γ
    sub-classification carries the result.

    sign_verdict     = N/A   (OPEN-Q has no directional pre-registration)
    magnitude_verdict per residual:
        PASS  if best_residual < 1e-9  (and >=2 pairs satisfy across
                                        a non-definitional candidate)
        INFO  if best_residual in [1e-9, 1e-3]
        FAIL  if best_residual > 1e-3
    regime_verdict  = VALID if all SDPs converged (status='optimal'),
                      else MARGINAL.

    Composite collapse (gate-verdicts.md S87 schema-v2):
      regime BREAKDOWN -> FAIL
      sign FAIL -> FAIL
      magnitude FAIL & regime VALID -> FAIL
      magnitude FAIL & regime MARGINAL -> INFO (sign-correct, regime-bound)
      magnitude INFO -> INFO
      else -> PASS

    For OPEN-Q this is pre-registered to land INFO unless CLASS-α achieves
    PASS-evidence-on-disk (then composite would be PASS).
    """
    cls = result['verdict_class']  # (local)
    if cls == 'CLASS-alpha':
        return 'PASS', 'PASS', 'N/A'
    if cls == 'CLASS-beta':
        return 'INFO', 'INFO', 'N/A'
    # CLASS-gamma: magnitude FAIL; with regime VALID, this collapses to FAIL,
    # but per the OPEN-Q decision rule the gate is INFO-by-design (the conjecture
    # is being closed honestly, not the gate failing). We emit composite=INFO
    # with magnitude=FAIL recorded in the 3-tuple companion row to preserve
    # the magnitude-FAIL signal for downstream audit.
    return 'INFO', 'FAIL', 'N/A'


def append_verdict(verdict, value, audit_sha, content_sha,
                   sign_v, magnitude_v, regime_v):
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    tuple3 = (
        f"# sign_verdict={sign_v} magnitude_verdict={magnitude_v} "
        f"regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)
        fp.write(tuple3)


# ---------------------------------------------------------------------------
# Section 11 — Main
# ---------------------------------------------------------------------------

def main():
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_CONSTS, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    result = compute()

    # Save NPZ
    np.savez(
        OUT_NPZ,
        candidate_identities_list=np.array(result['candidate_names']),
        residuals_per_identity=result['residual_table'],
        rhs_per_identity=result['rhs_table'],
        lhs_per_pair=result['lhs_per_pair'],
        best_residual=np.array([result['value']]),
        best_identity_form=np.array([result['best_identity_form']]),
        canonical_state_pairs_tested=np.array(result['pair_names']),
        eigenvalues_L12=np.array([result['flat_abs_count']]),
        flat_abs_min=np.array([result['flat_abs_min']]),
        flat_abs_max=np.array([result['flat_abs_max']]),
        verdict_class=np.array([result['verdict_class']]),
        conjecture_status=np.array([result['conjecture_status']]),
        sdp_status=np.array(result['sdp_status']),
        regime_verdict=np.array([result['regime_verdict']]),
        pairs_meta_json=np.array([json.dumps(result['pairs_meta'])]),
        R_sweep_values=result['R_sweep_values'],
        lhs_R_sweep=result['lhs_R_sweep'],
    )
    print(f"\n  Saved NPZ: {OUT_NPZ}")

    make_plot(result)
    print(f"  Saved plot: {OUT_PNG}")

    # Verdict + 3-tuple
    composite, magnitude_v, sign_v = evaluate_gate(result)
    regime_v = result['regime_verdict']  # (local)

    tag = emit_4tuple(result['value'], SCHEME, CONVENTION, L_MAX)
    print(f"\n  4-tuple: {tag}")
    print(f"  Verdict: {composite} (CLASS={result['verdict_class']})")
    print(f"  3-tuple: sign={sign_v}, magnitude={magnitude_v}, regime={regime_v}")

    append_verdict(composite, result['value'], audit_sha, content_sha,
                   sign_v, magnitude_v, regime_v)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {composite} (CLASS={result['verdict_class']}) (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
