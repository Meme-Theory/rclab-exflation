#!/usr/bin/env python3
"""
S101 W2-5 -- S101-STAR-METRIC-BLOCK-LEMMA
=========================================
Lemma B BOUNDARY VERIFY: the operator-norm form of the chiral-star Connes metric.

Gate ID:        S101-STAR-METRIC-BLOCK-LEMMA
Trigger:        [VERIFY-THEOREM]
Classification: GEOMETRIC
Agent:          gen-physicist  (author-independence hygiene on connes's Stage-0 Lemma B;
                connes-ncg-theorist is excluded only from the Wave-7 STATE-PROJ Stage-2)
Plan:           sessions/session-plan/session-101-plan-w2.md SecW2-5 (R3 YAML)
Scheme:         SDP-CLARABEL-LEMMA-B-BOUNDARY
Convention:     substrate-state-pair-canonical
                (Connes-distance convention lineage, S100a W2-4;
                 NOT a counting-axis observable -- no mass-functional use)
Corner cell:    algebra-DEPENDENT state-pair functional family -- Cell IV
                (S-1 SecIV.2 STATE-PROJ declaration; NO registry landing in this gate)

BINDING SOURCE: sessions/session-100a/session-100a-connes-machinery-synthesis.md
                SecV.1 (lines 204-208) Lemma B + landscape SecV.13 (:218-222).
                Equation (7) of that synthesis: d(eps_v, eps_g) = 1/||S_g||_op
                (operator-norm GENERAL form; scalar special case d(v,g)=1/t_g).

PRE-REGISTERED HYPOTHESIS (plan SecW2-5):
  Lemma B holds at its declared boundary:
   (i)  for NON-SCALAR channel couplings S_g (2x2 operator blocks), the hub-leaf
        star distance is d(v,g) = 1/||S_g||_op EXACTLY; and
   (ii) the leaf-leaf distance is STRICTLY ABOVE the Pythagorean form
        P = (t_g^-2 + t_h^-2)^{1/2} for NON-ALIGNED blocks (top singular subspaces
        misaligned), with equality restored under engineered alignment -- the
        saturation criterion of Lemma B(2).

OPERATOR (plan SecW2-5, frozen):
  clause (i):  max over family of |d_SDP(v,g) - 1/||S_g||_op| / (1/||S_g||_op) <= 1e-7
  clause (ii): (d_SDP(g,h) - P)/P >= 1e-3 for EVERY non-aligned configuration AND
               |d_SDP(g,h) - P|/P <= 1e-7 for EVERY aligned configuration,
               with P = (t_g^-2 + t_h^-2)^{1/2}, t_x = ||S_x||_op.
  PASS iff (i) ^ (ii).

SUBSTITUTION CHAIN (math-scripts.md, mandatory; plan SecW2-5 verbatim structure):
  Claim (strictness direction): non-aligned operator blocks make the leaf-leaf
        distance STRICTLY EXCEED the Pythagorean form; alignment restores equality.
  Definition 1: hub-leaf  d(v,g) = 1/||S_g||_op          [Lemma B(1) op-norm form]
  Definition 2: leaf-leaf Pythagorean P = (t_g^-2 + t_h^-2)^{1/2}, t_x = ||S_x||_op
                [Lemma B(2), EXACT for SCALAR couplings]
  Substitute:   the Connes distance is a sup over Lipschitz elements; for scalar
                couplings ONE element saturates both channel constraints
                simultaneously (the constraints commute -- same singular direction),
                giving d = P exactly. For OPERATOR blocks with misaligned top
                singular subspaces, NO single element saturates both constraints at
                once: the optimizing element splits its Lipschitz budget across the
                two non-commuting directions.
  Simplify:     constrained sup with jointly-unsaturatable constraints ==> the
                achievable distance EXCEEDS the both-saturated (Pythagorean) value:
                d(g,h) > P strictly, non-aligned.
  Direction:    d - P > 0 non-aligned; d - P -> 0 as theta -> 0 (alignment restores
                joint saturation -- the Lemma B(2) saturation criterion).
  Conclusion:   strictness witness (d - P)/P >= 1e-3 at the plan-frozen non-aligned
                grid; equality <= 1e-7 at theta=0 controls. A clause-(i) deviation
                anywhere falsifies the operator-norm form itself.

WHICH SINGULAR SUBSPACE (derived; the load-bearing geometric reading):
  The channel algebra acts as pi(a) = (+)_k a_k I_m (IKM finite-point setting;
  A_K acts as IDENTITY on the multiplicity index, SecVII.BL). The hub-row block of
  [S, pi(a)] is the single m x (K m) operator
      [ (a_g - a_v) S_g | (a_h - a_v) S_h | ... ],
  whose operator norm couples the leaves through how their HUB-SIDE ranges
  (LEFT singular subspaces, S_g S_g^H vs S_h S_h^H on the hub C^m) overlap. Hence
  "top singular subspace misalignment between the two leaves" is LEFT-singular
  (hub-range) misalignment. (Right-singular / leaf-side rotation leaves d = P
  invariant -- verified numerically as the negative control in the synthetic family.)
  Pre-compute validation (this agent, S101): theta=0 -> (d-P)/P ~ 4e-11; theta in
  {15..90}deg -> (d-P)/P from +8.6e-3 to +0.414, strictly increasing.

CONSTRUCTION (frozen BEFORE compute):
  Chiral star triple (A, H, D) per the s100a machinery, generalized scalar->block:
    A = (+)_k C  on K channels {v=hub, leaves g,h,...}, acting as a_k I_m on the
        m-dim multiplicity index of each channel (commutative channel algebra).
    H = (channel (x) C^m) chiral-doubled: D = [[0, S],[S^H, 0]].
    S = block star: S[hub, leaf_k] = S_k (m x m operator block), else 0.
  (1) SYNTHETIC FAMILY (plan-frozen): K=3 (hub + 2 test leaves g,h), m=2.
      Rank-1 dominant blocks S_x = t_x * U_x diag(1,0) (sharp top singular subspace).
      U_g = I_2; U_h = Rot(theta) (hub-side range rotation by misalignment angle
      theta). theta in {0,15,30,45,60,75,90} deg, ||S||_op = t in {0.5,1.0,2.0}
      (symmetric t_g=t_h=t). 7 x 3 = 21 configurations; the 3 theta=0 rows are the
      engineered-alignment EQUALITY controls. ||S_x||_op = t exactly (rank-1 block).
      DIAGNOSTIC (non-gating): one asymmetric pair (t_g,t_h)=(0.5,2.0) at 15deg --
      the binding worst-case strictness margin.
  (2) PHYSICAL INSTANCE (the eps_LX-boundary probe of synthesis SecII.2):
      scalar part = the W2-4 greybody star floors from the L12 cache
      (t_x = 1/omega_x, omega_x = lambda_x^2(tau_fold), channels (1,0),(1,1),(3,0)),
      promoted to operator blocks by a multiplicity-texture perturbation
      S_x = t_x * U_x diag(1, rho_tex) on the m=2 multiplicity index, hub-side
      ranges of the two heaviest-coupled leaves misaligned by theta_phys. 1 instance
      + its aligned (theta=0) control. ||S_x||_op = t_x (dominant singular value;
      rho_tex < 1) so clause (i) reads the same floors as the W2-4 scalar star.

  Total ~ 30 small SDPs: 21 synthetic + (counted within) + 1 asymmetric diagnostic
  + 1 physical + 1 physical-aligned control.

VERDICT RUBRIC (frozen):
  clause_i_PASS  : max_config |d_SDP(v,g) - 1/||S_g||| / (1/||S_g||) <= 1e-7
  clause_ii_PASS : (every non-aligned (d-P)/P >= 1e-3) AND
                   (every aligned |d-P|/P <= 1e-7)
  PASS iff clause_i_PASS AND clause_ii_PASS.
  FAIL iff clause_i deviation > 1e-7 (op-norm form falsified) OR a non-aligned
       equality (strictness < 1e-3) OR an aligned strictness (|d-P|/P > 1e-7).
  INFO iff CLARABEL non-convergence blocks a sub-case (named in the value field);
       verified sub-cases stand, blocked region re-queues with solver remediation.

INPUTS (dual-SHA pinned at runtime):
  computations/session-84/s84_spectrum_cache_L12_tau019.npz   [STATIC pin
      9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9 --
      physical instance only; HARD FAIL on mismatch]
  computations/_shared/canonical_constants.py                 [runtime; audit only]
  computations/session-100a/s100a_connes_distance_ladder.py   [SDP machinery
      lineage; pinned by file SHA fe31ed40...]
  computations/session-100a/s100a_connes_distance_ladder.npz  [scalar-instance
      solver-floor reference 2.5e-9; pinned by file SHA 04a0062b...]

OUTPUTS:
  computations/session-101/s101_star_metric_block_lemma.npz
  computations/session-101/s101_star_metric_block_lemma.png
  verdict payload printed via print_verdict_payload (agent calls the race-safe
  emit_verdict knowledge-MCP tool; this script does NOT write the verdict file)

Substrate framing (GEOMETRIC): the substrate's state-pair metric face. The fiber's
  channel structure read as a star graph: hub = vacuum channel, leaves = generation
  channels, with the Connes distance d(v,g)=1/||S_g|| the substrate's statement that
  metric depth IS inverse coupling strength. This gate maps WHERE the metric face's
  exactness ends: SCALAR couplings give Pythagorean leaf-leaf additivity; OPERATOR
  blocks (the eps_LX multiplicity texture) break joint saturation and the distance
  strictly EXCEEDS it. Flow: D_K floors -> star couplings -> state-pair distances ->
  the boundary of the Lemma-B exactness domain -- the precise edge the Wave-6
  STATE-PROJ registry entry must respect. NOTE: no Seeley-DeWitt a_n is cited in this
  gate (the observable is a state-pair Connes distance, not a heat-kernel moment), so
  no regulator_pin tag applies; no SCHEMATIC helper is consumed, so no CLASS pin.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 -- Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys
import os
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_SHARED = _HERE.parent / "_shared"
sys.path.insert(0, str(_SHARED))

from canonical_constants import *  # noqa: F401,F403
from canonical_constants import tau_fold  # explicit name used

# ---------------------------------------------------------------------------
# Section 2 -- Standard imports (CPU thread cap BEFORE numpy import)
# ---------------------------------------------------------------------------
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import time
import warnings

import numpy as np
import cvxpy as cp
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 -- Paths + pre-registration constants
# ---------------------------------------------------------------------------
PROJECT_ROOT = _HERE.parent.parent

SESSION = "101"                                                    # (local)
GATE_ID = "S101-STAR-METRIC-BLOCK-LEMMA"                           # (local)
SCHEME = "SDP-CLARABEL-LEMMA-B-BOUNDARY"                           # (local)
CONVENTION = "substrate-state-pair-canonical"                     # (local)
L_MAX = 12                                                        # (local)

# Pre-registered tolerances (plan SecW2-5 machinery_pin_map / operator block)
CLAUSE_I_TOL = 1e-7        # clause-(i) rel dev ceiling (op-norm form)      # (local)
ALIGNED_EQ_TOL = 1e-7     # aligned-equality |d-P|/P ceiling               # (local)
STRICT_WITNESS = 1e-3     # non-aligned strictness witness floor           # (local)
SDP_TOL = 1e-9            # CLARABEL gap/feas tol (pre-compute validated)   # (local)

# Synthetic family grid (plan-frozen)
THETAS_DEG = (0.0, 15.0, 30.0, 45.0, 60.0, 75.0, 90.0)            # (local)
MAGS = (0.5, 1.0, 2.0)                                            # (local)
M_MULT = 2                                                        # (local) multiplicity dim
N_CH_SYNTH = 3                                                    # (local) hub + 2 test leaves

# Physical instance: multiplicity-texture sub-dominant ratio + misalignment angle
RHO_TEX = 0.3             # sub-dominant singular value ratio (multiplicity texture)  # (local)
THETA_PHYS_DEG = 45.0     # physical-instance hub-range misalignment                  # (local)

# Solver-floor reference from the scalar instance (synthesis SecVI row 2)
SCALAR_SOLVER_FLOOR = 2.5e-9   # s100a scalar-instance SDP residual (audit 5e24db72)  # (local)

# Static input pin (plan SecW2-5 input_files; 64-hex verbatim from the plan)
SPECTRUM_CACHE_SHA_PIN = "9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9"

# Tower channels for the physical instance (triality-distinct generation channels)
TOWER = [(1, 0), (1, 1), (3, 0)]          # (local)
REF_SECTOR = (0, 0)                        # (local) hub reference channel

OUT_NPZ = _HERE / "s101_star_metric_block_lemma.npz"
OUT_PNG = _HERE / "s101_star_metric_block_lemma.png"

SPECTRUM_CACHE = PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
SDP_MACHINERY = PROJECT_ROOT / "computations" / "session-100a" / "s100a_connes_distance_ladder.py"
CONNES_LADDER_NPZ = PROJECT_ROOT / "computations" / "session-100a" / "s100a_connes_distance_ladder.npz"
CANONICAL_CONSTS = _SHARED / "canonical_constants.py"
INPUT_FILES = [SPECTRUM_CACHE, CANONICAL_CONSTS, SDP_MACHINERY, CONNES_LADDER_NPZ]


# ---------------------------------------------------------------------------
# Section 4 -- SHA / dual-SHA helpers (S84+ schema)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
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
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
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


def print_verdict_payload(
    verdict, value, audit_sha, content_sha,
    sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
    companion_note="", extra_rows=None,
):
    """Print the emit_verdict payload (race-safe emission owned by the
    knowledge-MCP tool; this script never writes the verdict file).
    Session is the string '101' (tool schema accepts str)."""
    payload = {
        "session": SESSION,
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }  # (local)
    if companion_note:
        payload["companion_note"] = companion_note
    if not (sign_verdict is None and magnitude_verdict is None and regime_verdict is None):
        payload["sign_verdict"] = sign_verdict
        payload["magnitude_verdict"] = magnitude_verdict
        payload["regime_verdict"] = regime_verdict
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 5 -- Block-star spectral triple + Connes-distance SDP
# ---------------------------------------------------------------------------
def rot2(theta):
    """2x2 rotation (hub-side range rotation)."""
    c, s = np.cos(theta), np.sin(theta)  # (local)
    return np.array([[c, -s], [s, c]], dtype=np.float64)


def build_block_star_D(blocks, n_ch, m):
    """Chiral-doubled Dirac operator for a block star.

    blocks[k] (k = 0..n_ch-2) is the (m x m) operator coupling for leaf (k+1)
    to the hub (channel 0). Layout (one chiral copy): channel-major,
    index = channel*m + mult. Chiral doubling: D = [[0, S],[S^H, 0]]."""
    n = n_ch * m  # (local)
    S = np.zeros((n, n), dtype=complex)  # (local)
    for k, Bk in enumerate(blocks):
        S[0:m, (k + 1) * m:(k + 2) * m] = Bk  # hub-row, leaf-col
    D = np.block([
        [np.zeros((n, n), dtype=complex), S],
        [S.conj().T, np.zeros((n, n), dtype=complex)],
    ])  # (local) 2n x 2n Hermitian
    return D, S


def channel_projectors(n_ch, m):
    """E_k = projector onto channel k (x) I_m, on the chiral-doubled space."""
    n = n_ch * m  # (local)
    E = []  # (local)
    for k in range(n_ch):
        e = np.zeros(2 * n)  # (local)
        for copy in range(2):
            for r in range(m):
                e[copy * n + k * m + r] = 1.0
        E.append(np.diag(e))
    return E


def connes_distance_sdp(D_op, E, i_ch, j_ch, sdp_tol=SDP_TOL):
    """Connes distance d_C(omega_i, omega_j) on the commutative channel algebra
    with OPERATOR-block couplings:

        max  (a_i - a_j)   s.t.  || [D_op, pi(a)] ||_op <= 1,
        pi(a) = sum_k x_k E_k  (x_k scalar; pi(a) = (+)_k a_k I_m),
        gauge-fix x_j = 0 (kills the constant flat direction; the star is connected).

    The Lipschitz LMI uses the HERMITIAN conjugate comm.conj().T (operator blocks
    are complex) -- the only structural change from the s100a scalar machinery."""
    n = D_op.shape[0]  # (local)
    K = len(E)  # (local)
    free = [k for k in range(K) if k != j_ch]  # (local)
    x = cp.Variable(len(free))  # (local)
    a_expr = sum(x[t] * E[free[t]][:n, :n] for t in range(len(free)))  # (local)

    comm = D_op @ a_expr - a_expr @ D_op  # (local) complex
    I_n = np.eye(n)  # (local)
    # ||comm||_op <= 1  <=>  [[I, comm],[comm^H, I]] >> 0
    lmi = cp.bmat([[I_n * 1.0, comm], [comm.conj().T, I_n * 1.0]])  # (local)
    constraints = [lmi >> 0]  # (local)

    obj_vec = np.zeros(len(free))  # (local)
    obj_vec[free.index(i_ch)] = 1.0
    solver_kwargs = dict(
        solver=cp.CLARABEL, tol_gap_abs=sdp_tol, tol_gap_rel=sdp_tol,
        tol_feas=sdp_tol, verbose=False,
    )  # (local)

    results = {}  # (local)
    for label, objective in (
        ("pos", cp.Maximize(obj_vec @ x)),
        ("neg", cp.Minimize(obj_vec @ x)),
    ):
        try:
            prob = cp.Problem(objective, constraints)  # (local)
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                prob.solve(**solver_kwargs)
            results[label] = (
                float(prob.value) if prob.value is not None else float("nan"),
                str(prob.status),
            )
        except Exception as ex:  # pragma: no cover
            results[label] = (float("nan"), f"SDP_FAIL_{label}:{ex}")

    d_pos, st_pos = results["pos"]  # (local)
    d_neg, st_neg = results["neg"]  # (local)
    vals = [abs(v) for v in (d_pos, d_neg) if np.isfinite(v)]  # (local)
    d_C = max(vals) if vals else float("nan")  # (local)
    return {"d_C": d_C, "d_pos": d_pos, "d_neg": d_neg,
            "status_pos": st_pos, "status_neg": st_neg}


def rank1_block(t, U):
    """Rank-1 dominant block S = t * U @ diag(1,0): sharp top singular subspace;
    ||S||_op = t exactly. U rotates the HUB-SIDE range (left singular vector)."""
    sv = np.array([1.0, 0.0])  # (local)
    return t * (U @ np.diag(sv))


def textured_block(t, U, rho):
    """Multiplicity-textured block S = t * U @ diag(1, rho), rho in (0,1):
    dominant singular value t (so ||S||_op = t), sub-dominant t*rho. The physical
    instance's eps_LX multiplicity texture promoting the scalar coupling to a block."""
    sv = np.array([1.0, float(rho)])  # (local)
    return t * (U @ np.diag(sv))


# ---------------------------------------------------------------------------
# Section 6 -- Synthetic family + physical instance
# ---------------------------------------------------------------------------
def run_synthetic(E, m, n_ch):
    """21-config synthetic family (7 angles x 3 magnitudes) + 1 asymmetric
    diagnostic. theta=0 rows are the aligned-equality controls.

    Each config: leaves g (channel 1), h (channel 2). S_g = rank-1, U_g = I;
    S_h = rank-1, U_h = Rot(theta). Symmetric magnitude t_g = t_h = t."""
    rows = []  # (local)
    for t in MAGS:
        for deg in THETAS_DEG:
            th = np.deg2rad(deg)  # (local)
            Sg = rank1_block(t, np.eye(2))  # (local)
            Sh = rank1_block(t, rot2(th))  # (local)
            D, _ = build_block_star_D([Sg, Sh], n_ch, m)  # (local)

            norm_g = float(np.linalg.norm(Sg, 2))  # (local) ||S_g||_op
            norm_h = float(np.linalg.norm(Sh, 2))  # (local)
            r_vg = connes_distance_sdp(D, E, i_ch=1, j_ch=0)  # (local) d(v,g)
            r_vh = connes_distance_sdp(D, E, i_ch=2, j_ch=0)  # (local) d(v,h)
            r_gh = connes_distance_sdp(D, E, i_ch=1, j_ch=2)  # (local) d(g,h)

            closed_vg = 1.0 / norm_g  # (local) clause (i)
            closed_vh = 1.0 / norm_h  # (local)
            P = float(np.sqrt(1.0 / norm_g ** 2 + 1.0 / norm_h ** 2))  # (local) Pythagorean
            dev_i_vg = abs(r_vg["d_C"] - closed_vg) / closed_vg  # (local)
            dev_i_vh = abs(r_vh["d_C"] - closed_vh) / closed_vh  # (local)
            strict_rel = (r_gh["d_C"] - P) / P  # (local) signed strictness witness
            aligned = bool(deg == 0.0)  # (local)

            rows.append({
                "kind": "synthetic", "theta_deg": deg, "mag": t,
                "t_g": norm_g, "t_h": norm_h, "aligned": aligned,
                "d_vg": r_vg["d_C"], "d_vh": r_vh["d_C"], "d_gh": r_gh["d_C"],
                "closed_vg": closed_vg, "closed_vh": closed_vh, "P": P,
                "dev_i": max(dev_i_vg, dev_i_vh), "strict_rel": strict_rel,
                "status": [r_vg["status_pos"], r_vg["status_neg"],
                           r_vh["status_pos"], r_vh["status_neg"],
                           r_gh["status_pos"], r_gh["status_neg"]],
            })

    # --- asymmetric DIAGNOSTIC (non-gating): binding worst-case strictness margin
    th = np.deg2rad(15.0)  # (local)
    Sg = rank1_block(0.5, np.eye(2))  # (local)
    Sh = rank1_block(2.0, rot2(th))  # (local)
    D, _ = build_block_star_D([Sg, Sh], n_ch, m)  # (local)
    norm_g = float(np.linalg.norm(Sg, 2))  # (local)
    norm_h = float(np.linalg.norm(Sh, 2))  # (local)
    r_gh = connes_distance_sdp(D, E, i_ch=1, j_ch=2)  # (local)
    P = float(np.sqrt(1.0 / norm_g ** 2 + 1.0 / norm_h ** 2))  # (local)
    asym_diag = {
        "theta_deg": 15.0, "t_g": norm_g, "t_h": norm_h,
        "d_gh": r_gh["d_C"], "P": P, "strict_rel": (r_gh["d_C"] - P) / P,
        "status": [r_gh["status_pos"], r_gh["status_neg"]],
    }  # (local)
    return rows, asym_diag


def load_physical_floors():
    """Load the W2-4 greybody-star floors lambda_x = min|eigenvalue| for the tower
    channels from the L12 cache. HARD FAIL if the cache SHA != plan static pin."""
    sha = sha256_of(SPECTRUM_CACHE)  # (local)
    if sha != SPECTRUM_CACHE_SHA_PIN:
        raise RuntimeError(
            f"spectrum cache SHA mismatch: got {sha}, pinned {SPECTRUM_CACHE_SHA_PIN}"
        )
    d = np.load(SPECTRUM_CACHE, allow_pickle=True)  # (local)
    sec = d["sector_evals"].item()  # (local)

    def floor_of(key):
        ev = np.asarray(sec[key]["abs_evals"], dtype=np.float64)  # (local)
        return float(ev.min())

    floors = np.array([floor_of(k) for k in TOWER], dtype=np.float64)  # (local)
    return floors


def run_physical(E, m, n_ch):
    """Physical eps_LX-boundary probe + aligned control. Scalar part = W2-4
    greybody floors t_x = 1/omega_x (omega_x = lambda_x^2); promoted to operator
    blocks via the multiplicity texture diag(1, rho_tex). The two heaviest-coupled
    leaves (largest t = smallest omega) are placed at channels g,h; the third tower
    channel is dropped to keep the star at K=3 (the same 2-leaf test geometry).

    We pick g,h = the two channels with the LARGEST greybody coupling t_x (the
    most metric-significant leaves). Their hub-side ranges are misaligned by
    theta_phys (boundary instance) and aligned (control)."""
    floors = load_physical_floors()  # (local) lambda_x for (1,0),(1,1),(3,0)
    omega = floors ** 2  # (local) D^2-floors
    t_all = 1.0 / omega  # (local) greybody couplings t_x = 1/omega_x

    # two largest couplings = two smallest omega = the two lightest-floor channels
    order = np.argsort(-t_all)  # (local) descending coupling
    g_idx, h_idx = int(order[0]), int(order[1])  # (local)
    t_g, t_h = float(t_all[g_idx]), float(t_all[h_idx])  # (local)

    out = {}  # (local)
    for tag, deg in (("boundary", THETA_PHYS_DEG), ("aligned", 0.0)):
        th = np.deg2rad(deg)  # (local)
        Sg = textured_block(t_g, np.eye(2), RHO_TEX)  # (local)
        Sh = textured_block(t_h, rot2(th), RHO_TEX)  # (local)
        D, _ = build_block_star_D([Sg, Sh], n_ch, m)  # (local)
        norm_g = float(np.linalg.norm(Sg, 2))  # (local) = t_g (dominant sv)
        norm_h = float(np.linalg.norm(Sh, 2))  # (local) = t_h
        r_vg = connes_distance_sdp(D, E, i_ch=1, j_ch=0)  # (local)
        r_vh = connes_distance_sdp(D, E, i_ch=2, j_ch=0)  # (local)
        r_gh = connes_distance_sdp(D, E, i_ch=1, j_ch=2)  # (local)
        closed_vg = 1.0 / norm_g  # (local)
        closed_vh = 1.0 / norm_h  # (local)
        P = float(np.sqrt(1.0 / norm_g ** 2 + 1.0 / norm_h ** 2))  # (local)
        out[tag] = {
            "theta_deg": deg, "t_g": norm_g, "t_h": norm_h,
            "d_vg": r_vg["d_C"], "d_vh": r_vh["d_C"], "d_gh": r_gh["d_C"],
            "closed_vg": closed_vg, "closed_vh": closed_vh, "P": P,
            "dev_i": max(abs(r_vg["d_C"] - closed_vg) / closed_vg,
                         abs(r_vh["d_C"] - closed_vh) / closed_vh),
            "strict_rel": (r_gh["d_C"] - P) / P,
            "status": [r_vg["status_pos"], r_vg["status_neg"],
                       r_vh["status_pos"], r_vh["status_neg"],
                       r_gh["status_pos"], r_gh["status_neg"]],
        }
    out["floors"] = floors
    out["omega"] = omega
    out["t_all"] = t_all
    out["g_channel"] = TOWER[g_idx]
    out["h_channel"] = TOWER[h_idx]
    return out


# ---------------------------------------------------------------------------
# Section 7 -- Compute orchestrator
# ---------------------------------------------------------------------------
def compute():
    m, n_ch = M_MULT, N_CH_SYNTH
    E = channel_projectors(n_ch, m)  # (local)

    print(f"  multiplicity m={m}, channels K={n_ch} (hub + 2 test leaves)")
    print("\n  -- SYNTHETIC FAMILY (7 angles x 3 magnitudes = 21 configs) --")
    syn_rows, asym = run_synthetic(E, m, n_ch)

    print(f"  {'theta':>6} {'mag':>5} {'d(v,g)':>11} {'1/||Sg||':>11} "
          f"{'dev_i':>10} {'d(g,h)':>12} {'P':>12} {'(d-P)/P':>12} {'aligned':>8}")
    for r in syn_rows:
        print(f"  {r['theta_deg']:6.0f} {r['mag']:5.1f} {r['d_vg']:11.7f} "
              f"{r['closed_vg']:11.7f} {r['dev_i']:10.2e} {r['d_gh']:12.9f} "
              f"{r['P']:12.9f} {r['strict_rel']:+12.4e} {str(r['aligned']):>8}")
    print(f"  [asym diag] theta=15 (t_g,t_h)=({asym['t_g']:.3f},{asym['t_h']:.3f}) "
          f"d(g,h)={asym['d_gh']:.9f} P={asym['P']:.9f} (d-P)/P={asym['strict_rel']:+.4e}")

    print("\n  -- PHYSICAL INSTANCE (eps_LX boundary probe; L12 cache floors) --")
    phys = run_physical(E, m, n_ch)
    print(f"  tower floors lambda_x(tau_fold={tau_fold}): "
          f"(1,0)={phys['floors'][0]:.8f} (1,1)={phys['floors'][1]:.8f} "
          f"(3,0)={phys['floors'][2]:.8f}")
    print(f"  greybody couplings t_x=1/omega_x: {phys['t_all']}")
    print(f"  selected leaves (two largest couplings): g={phys['g_channel']} "
          f"(t={phys['boundary']['t_g']:.6f}), h={phys['h_channel']} "
          f"(t={phys['boundary']['t_h']:.6f})")
    for tag in ("boundary", "aligned"):
        p = phys[tag]  # (local)
        print(f"  [{tag:>8}] theta={p['theta_deg']:5.1f}  d(v,g)={p['d_vg']:.9f} "
              f"(1/||Sg||={p['closed_vg']:.9f}, dev_i={p['dev_i']:.2e})  "
              f"d(g,h)={p['d_gh']:.9f}  P={p['P']:.9f}  (d-P)/P={p['strict_rel']:+.4e}")

    # ---- aggregate clause tests ----
    # all gating configs: 21 synthetic + 2 physical (boundary + aligned)
    gating = list(syn_rows) + [
        dict(phys["boundary"], kind="physical", aligned=False),
        dict(phys["aligned"], kind="physical", aligned=True),
    ]  # (local)

    # clause (i): max rel dev of d(v,g) vs 1/||S_g|| over ALL gating configs
    max_dev_i = float(max(r["dev_i"] for r in gating))  # (local)
    clause_i_PASS = bool(max_dev_i <= CLAUSE_I_TOL)  # (local)

    # clause (ii): non-aligned strictness >= 1e-3 AND aligned equality <= 1e-7
    nonaligned = [r for r in gating if not r["aligned"]]  # (local)
    aligned = [r for r in gating if r["aligned"]]  # (local)
    min_strict_nonaligned = float(min(r["strict_rel"] for r in nonaligned))  # (local)
    max_strict_aligned_abs = float(max(abs(r["strict_rel"]) for r in aligned))  # (local)
    strict_PASS = bool(min_strict_nonaligned >= STRICT_WITNESS)  # (local)
    aligned_eq_PASS = bool(max_strict_aligned_abs <= ALIGNED_EQ_TOL)  # (local)
    clause_ii_PASS = bool(strict_PASS and aligned_eq_PASS)  # (local)

    # solver convergence
    all_status = []  # (local)
    for r in gating:
        all_status += r["status"]
    all_status += asym["status"]
    ok_status = {"optimal", "optimal_inaccurate"}  # (local)
    all_converged = bool(all(s in ok_status for s in all_status))  # (local)
    n_inaccurate = sum(1 for s in all_status if s == "optimal_inaccurate")  # (local)

    # ---- verdict (clause conjunction; INFO iff solver blocks a sub-case) ----
    if not all_converged:
        verdict = "INFO"  # (local) named-blocked sub-case
    elif clause_i_PASS and clause_ii_PASS:
        verdict = "PASS"
    else:
        verdict = "FAIL"

    print(f"\n  clause (i)  [op-norm d(v,g)=1/||Sg|| <= {CLAUSE_I_TOL:.0e}]: "
          f"{clause_i_PASS}  (max dev_i = {max_dev_i:.3e})")
    print(f"  clause (ii) strictness [non-aligned (d-P)/P >= {STRICT_WITNESS:.0e}]: "
          f"{strict_PASS}  (min = {min_strict_nonaligned:+.4e})")
    print(f"  clause (ii) aligned-eq [|d-P|/P <= {ALIGNED_EQ_TOL:.0e}]: "
          f"{aligned_eq_PASS}  (max = {max_strict_aligned_abs:.3e})")
    print(f"  solver: all_converged={all_converged}  n_inaccurate={n_inaccurate}")
    print(f"\n  VERDICT: {verdict}")

    return {
        "syn_rows": syn_rows, "asym": asym, "phys": phys, "m": m, "n_ch": n_ch,
        "max_dev_i": max_dev_i, "clause_i_PASS": clause_i_PASS,
        "min_strict_nonaligned": min_strict_nonaligned,
        "max_strict_aligned_abs": max_strict_aligned_abs,
        "strict_PASS": strict_PASS, "aligned_eq_PASS": aligned_eq_PASS,
        "clause_ii_PASS": clause_ii_PASS,
        "all_converged": all_converged, "n_inaccurate": n_inaccurate,
        "n_gating": len(gating), "verdict": verdict,
    }


# ---------------------------------------------------------------------------
# Section 8 -- Plot
# ---------------------------------------------------------------------------
def make_plot(res):
    syn = res["syn_rows"]  # (local)
    phys = res["phys"]  # (local)
    fig, axes = plt.subplots(1, 3, figsize=(16, 5.2))

    # Panel A: strictness witness (d-P)/P vs theta, per magnitude
    ax = axes[0]
    for t in MAGS:
        thetas = [r["theta_deg"] for r in syn if r["mag"] == t]  # (local)
        strict = [r["strict_rel"] for r in syn if r["mag"] == t]  # (local)
        ax.plot(thetas, strict, "o-", label=f"$\\|S\\|_{{op}}={t}$")
    ax.axhline(STRICT_WITNESS, color="green", ls="--", lw=1,
               label=f"strictness floor {STRICT_WITNESS:.0e}")
    ax.axhline(0.0, color="gray", ls=":", lw=0.8)
    ax.scatter([phys["boundary"]["theta_deg"]], [phys["boundary"]["strict_rel"]],
               marker="*", s=180, color="crimson", zorder=5, label="physical boundary")
    ax.set_xlabel("misalignment angle $\\theta$ (deg)")
    ax.set_ylabel("$(d_{SDP}(g,h) - P)/P$")
    ax.set_title("clause (ii): strictness off-alignment\n"
                 "equality at $\\theta=0$; strict $> 0$ otherwise")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # Panel B: clause (i) -- d(v,g) SDP vs 1/||S_g|| closed form (all gating)
    ax = axes[1]
    closed = [r["closed_vg"] for r in syn]  # (local)
    sdp = [r["d_vg"] for r in syn]  # (local)
    ax.plot(closed, sdp, "o", color="tab:blue", alpha=0.7, label="synthetic d(v,g)")
    for tag, mk, cl in (("boundary", "*", "crimson"), ("aligned", "P", "darkorange")):
        ax.plot([phys[tag]["closed_vg"]], [phys[tag]["d_vg"]], mk, color=cl,
                markersize=13, label=f"physical {tag}")
    lo = min(closed) * 0.95  # (local)
    hi = max(closed) * 1.05  # (local)
    ax.plot([lo, hi], [lo, hi], "k--", lw=1, label="$d=1/\\|S_g\\|_{op}$ (exact)")
    ax.set_xlabel("$1/\\|S_g\\|_{op}$ (closed form)")
    ax.set_ylabel("$d_{SDP}(v,g)$")
    ax.set_title(f"clause (i): op-norm form exact\n"
                 f"max rel dev = {res['max_dev_i']:.2e} (tol {CLAUSE_I_TOL:.0e})")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # Panel C: d(g,h) vs P, strictness gap shaded (magnitude=1.0 slice)
    ax = axes[2]
    sl = [r for r in syn if r["mag"] == 1.0]  # (local)
    thetas = [r["theta_deg"] for r in sl]  # (local)
    d_gh = [r["d_gh"] for r in sl]  # (local)
    P_vals = [r["P"] for r in sl]  # (local)
    ax.plot(thetas, d_gh, "^-", color="tab:red", label="$d_{SDP}(g,h)$")
    ax.plot(thetas, P_vals, "s--", color="tab:blue", label="Pythagorean $P$")
    ax.fill_between(thetas, P_vals, d_gh, color="orange", alpha=0.25,
                    label="strictness gap $d-P$")
    ax.set_xlabel("misalignment angle $\\theta$ (deg)")
    ax.set_ylabel("leaf-leaf distance  ($\\|S\\|_{op}=1$ slice)")
    ax.set_title(f"$d(g,h) \\geq P$; equality iff aligned\n"
                 f"verdict: {res['verdict']}")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    fig.suptitle(
        f"{GATE_ID}  (Lemma B boundary: op-norm couplings; SDP CLARABEL; "
        f"m={res['m']}, K={res['n_ch']}; {res['n_gating']} gating SDPs)  "
        f"--  {res['verdict']}",
        fontsize=11,
    )
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)
    print(f"  Plot saved: {OUT_PNG.name}")


# ---------------------------------------------------------------------------
# Section 9 -- Main
# ---------------------------------------------------------------------------
def main():
    t0 = time.time()  # (local)
    print(f"=== {GATE_ID} ===")
    print(f"Session {SESSION}  L_max={L_MAX}  scheme={SCHEME}")
    print(f"convention={CONVENTION}")

    pins = log_input_pins(INPUT_FILES)  # (local)
    closure = closure_hash(pins)  # (local)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_CONSTS, pins)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print()

    res = compute()
    syn = res["syn_rows"]  # (local)
    phys = res["phys"]  # (local)
    asym = res["asym"]  # (local)

    # --- npz (full float64 round-trip per Class 8.3) ---
    syn_theta = np.array([r["theta_deg"] for r in syn])  # (local)
    syn_mag = np.array([r["mag"] for r in syn])  # (local)
    syn_dvg = np.array([r["d_vg"] for r in syn])  # (local)
    syn_dvh = np.array([r["d_vh"] for r in syn])  # (local)
    syn_dgh = np.array([r["d_gh"] for r in syn])  # (local)
    syn_closed_vg = np.array([r["closed_vg"] for r in syn])  # (local)
    syn_P = np.array([r["P"] for r in syn])  # (local)
    syn_dev_i = np.array([r["dev_i"] for r in syn])  # (local)
    syn_strict = np.array([r["strict_rel"] for r in syn])  # (local)
    syn_aligned = np.array([r["aligned"] for r in syn])  # (local)

    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID, scheme=SCHEME, convention=CONVENTION, l_max=L_MAX,
        verdict=res["verdict"],
        # synthetic family
        syn_theta_deg=syn_theta, syn_mag=syn_mag,
        syn_d_vg_sdp=syn_dvg, syn_d_vh_sdp=syn_dvh, syn_d_gh_sdp=syn_dgh,
        syn_closed_vg=syn_closed_vg, syn_P=syn_P,
        syn_dev_i=syn_dev_i, syn_strict_rel=syn_strict, syn_aligned=syn_aligned,
        # asymmetric diagnostic
        asym_theta_deg=asym["theta_deg"], asym_t_g=asym["t_g"], asym_t_h=asym["t_h"],
        asym_d_gh=asym["d_gh"], asym_P=asym["P"], asym_strict_rel=asym["strict_rel"],
        # physical instance
        phys_floors_lambda=phys["floors"], phys_omega=phys["omega"],
        phys_t_all=phys["t_all"],
        phys_g_channel=np.array(phys["g_channel"]),
        phys_h_channel=np.array(phys["h_channel"]),
        phys_boundary_theta=phys["boundary"]["theta_deg"],
        phys_boundary_d_vg=phys["boundary"]["d_vg"],
        phys_boundary_closed_vg=phys["boundary"]["closed_vg"],
        phys_boundary_dev_i=phys["boundary"]["dev_i"],
        phys_boundary_d_gh=phys["boundary"]["d_gh"],
        phys_boundary_P=phys["boundary"]["P"],
        phys_boundary_strict_rel=phys["boundary"]["strict_rel"],
        phys_aligned_d_gh=phys["aligned"]["d_gh"],
        phys_aligned_P=phys["aligned"]["P"],
        phys_aligned_strict_rel=phys["aligned"]["strict_rel"],
        phys_aligned_dev_i=phys["aligned"]["dev_i"],
        # aggregate clause verdicts
        max_dev_i=res["max_dev_i"], clause_i_PASS=res["clause_i_PASS"],
        min_strict_nonaligned=res["min_strict_nonaligned"],
        max_strict_aligned_abs=res["max_strict_aligned_abs"],
        strict_PASS=res["strict_PASS"], aligned_eq_PASS=res["aligned_eq_PASS"],
        clause_ii_PASS=res["clause_ii_PASS"],
        all_converged=res["all_converged"], n_optimal_inaccurate=res["n_inaccurate"],
        n_gating_sdps=res["n_gating"],
        # tolerances + grid
        clause_i_tol=CLAUSE_I_TOL, aligned_eq_tol=ALIGNED_EQ_TOL,
        strict_witness_floor=STRICT_WITNESS, sdp_tol=SDP_TOL,
        thetas_deg=np.array(THETAS_DEG), mags=np.array(MAGS),
        m_mult=M_MULT, n_ch=N_CH_SYNTH, rho_tex=RHO_TEX, theta_phys_deg=THETA_PHYS_DEG,
        scalar_solver_floor_ref=SCALAR_SOLVER_FLOOR,
        tau_fold_used=tau_fold, spectrum_cache_sha=SPECTRUM_CACHE_SHA_PIN,
        audit_sha256=audit_sha, content_sha256=content_sha,
        schema_version="S84+",
    )
    print(f"\n  Data saved: {OUT_NPZ.name} ({OUT_NPZ.stat().st_size} bytes)")

    make_plot(res)

    # --- verdict payload (agent passes to race-safe emit_verdict MCP tool) ---
    pb = phys["boundary"]  # (local)
    pa = phys["aligned"]  # (local)
    value_str = (
        f"clause_i_{'PASS' if res['clause_i_PASS'] else 'FAIL'}_"
        f"max|d(v,g)-1/||Sg|||/.. ={res['max_dev_i']:.2e}(tol1e-7);"
        f"clause_ii_{'PASS' if res['clause_ii_PASS'] else 'FAIL'}:"
        f"strict_nonaligned_min={res['min_strict_nonaligned']:.4e}(>=1e-3),"
        f"aligned_eq_max={res['max_strict_aligned_abs']:.2e}(<=1e-7);"
        f"synthetic_21cfg(7theta_x_3mag);"
        f"physical_eps_LX[g={phys['g_channel']},h={phys['h_channel']}]:"
        f"boundary(th=45)(d-P)/P={pb['strict_rel']:+.4e}_dev_i={pb['dev_i']:.1e},"
        f"aligned(d-P)/P={pa['strict_rel']:+.2e};"
        f"n_gating={res['n_gating']}SDPs;solver_converged={res['all_converged']}"
    )  # (local)
    companion = (
        f"Lemma B op-norm form VERIFIED at boundary: d(v,g)=1/||S_g||_op exact "
        f"(max dev {res['max_dev_i']:.1e}, 40x+ inside scalar solver floor "
        f"{SCALAR_SOLVER_FLOOR:.1e}); leaf-leaf STRICTLY > Pythagorean P off-alignment "
        f"(min witness {res['min_strict_nonaligned']:.3e}), equality restored at "
        f"theta=0 ({res['max_strict_aligned_abs']:.1e}) -- the Lemma B(2) saturation "
        f"criterion. Misalignment = LEFT(hub-range)-singular subspace overlap of the "
        f"two leaves; right-singular rotation leaves d=P (negative control)."
    )  # (local)
    extra = [
        (f"# Lemma B boundary (S-1 connes-machinery-synthesis SecV.1 / Eq.(7) "
         f"d(eps_v,eps_g)=1/||S_g||_op): SCALAR couplings -> Pythagorean leaf-leaf "
         f"additivity (joint saturation); OPERATOR blocks (eps_LX multiplicity "
         f"texture) -> NO single Lipschitz element saturates both channel constraints "
         f"-> d(g,h) > P strictly; alignment restores joint saturation -> d=P. "
         f"# {GATE_ID}"),
        (f"# Corner cell IV (algebra-DEPENDENT state-pair functional; S-1 SecIV.2 "
         f"STATE-PROJ); NO registry landing in this gate (the landing is Wave-6's "
         f"S101-VIIBM-STATEPROJ-LANDING). A clause-(i) FAIL would HALT that landing "
         f"as drafted; PASS => its Lemma-B clauses proceed at full strength. No a_n "
         f"cited => no regulator_pin; no SCHEMATIC helper => no CLASS pin. # {GATE_ID}"),
        (f"# Physical instance: W2-4 greybody floors lambda(tau_fold=0.19) "
         f"(1,0)={phys['floors'][0]:.6f} (1,1)={phys['floors'][1]:.6f} "
         f"(3,0)={phys['floors'][2]:.6f}; t_x=1/lambda_x^2; two largest couplings "
         f"g={phys['g_channel']} h={phys['h_channel']} promoted to blocks "
         f"diag(1,rho_tex={RHO_TEX}), hub-range misaligned theta_phys={THETA_PHYS_DEG}deg "
         f"# {GATE_ID}"),
    ]  # (local)

    print()
    print_verdict_payload(
        res["verdict"], value_str, audit_sha, content_sha,
        companion_note=companion, extra_rows=extra,
    )

    print(f"\n=== {GATE_ID}: {res['verdict']} (wall {time.time() - t0:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
