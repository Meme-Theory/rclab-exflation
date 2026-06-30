#!/usr/bin/env python3
"""
S101 W2-6 -- S101-CONNES-DISTANCE-DISCONNECT-BOUNDARY
====================================================
Theorem A clause 3 at its boundary: SEVER one star edge (t_g = 0) and the
severed pair's Frobenius-regulated Connes distance d_R grows LINEARLY in R
(log-log slope EXACTLY 1 -- the commutative CLASS-gamma signature), while every
connected pair stays R-flat once R exceeds the activation threshold rho*.

Gate ID:        S101-CONNES-DISTANCE-DISCONNECT-BOUNDARY
Trigger:        [VERIFY-THEOREM]   (no [SIGN] 3-tuple -- structural verify)
Classification: GEOMETRIC
Agent:          gen-physicist  (author-independence: NOT the S100a connes-ncg
                authoring agent; same SDP machinery + L12 cache floors as W2-5)
Plan:           sessions/session-plan/session-101-plan-w2.md SecW2-6 (R3 YAML)
Scheme:         SDP-CLARABEL-CLASS-GAMMA-DISCONNECT
Convention:     substrate-state-pair-canonical
                (Cell-IV algebra-DEPENDENT state-pair family per S-1 SecIV.2;
                 NO §VII registry landing occurs in this gate)

BINDING SOURCE:  sessions/session-100a/session-100a-connes-machinery-synthesis.md
                 SecV.2 (lines 210-214) Theorem A clause 3 + landscape SecV.14.

PRE-REGISTERED HYPOTHESIS (plan SecW2-6):
  Theorem A clause 3 holds at its boundary. Severing one star edge (t_g = 0)
  makes the severed pair's Frobenius-regulated distance d_R grow with log-log
  slope EXACTLY 1 (linear-in-R divergence, the commutative CLASS-gamma signature),
  while all connected pairs stay R-flat; the connected-pair activation threshold
  rho* (the one empirical residue of the S-1 synthesis) satisfies rho* <= 10*omega_max.

PASS-conjunction (operator block, frozen at plan-freeze):
  (a)  |d ln d_R / d ln R - 1| <= 1e-3   (severed pair; OLS over the 5-point R-grid)
  (b)  max_R |d_R/d_R0 - 1| <= 1e-8       (every connected pair; flat-window per the
       s100a flatness-window convention: measured on R >= rho*, R0 = first flat point)
  (c)  rho* <= 10*omega_max               (activation-threshold consistency)
  PASS iff (a) ^ (b) ^ (c).
  INFO  iff the severed-pair SDP flags UNBOUNDED before the largest R (acceptable
        DEGENERATE confirmation of the divergence; largest bounded R named).
  FAIL  iff severed-pair slope != 1 beyond 1e-3 (linear-divergence form falsified --
        a structural correction to Theorem A clause 3 is required; Wave-6 dichotomy
        clause halts as drafted), OR connected-pair flatness fails beyond 1e-8 with
        the solver clean (regulator-free claim on the connected side broken).

MACHINERY (frozen BEFORE compute; identical lineage to S100a-CONNES-DISTANCE-LADDER):

  Finite real spectral triple on the multiplicity bundle (A_mult, H_F, D_F):
    A_mult = self-adjoint part of C^4 -- the CHANNEL algebra over 4 channels
        {v = (0,0) vacuum/Higgs reference; g1 = (1,0); g2 = (1,1); g3 = (3,0)}.
    H_F    = C^2_chir (x) C^4_chan (x) C^2_{part/anti} = C^16 (doubled).
    D_F    = greybody-reweighted chiral star: S[v,g] = S[g,v] = t_g, else 0,
             t_g = kappa / omega_g, omega_g = lambda_g(tau_fold)^2, lambda_g =
             min|eigenvalue| of the (p,q)=g sector of D_K at tau_fold (L=12 cache).
             kappa = 1 (one overall metric scale, NOT a parameter).
    The Connes distance d_C(omega_i, omega_j) = sup{ |a_i - a_j| : ||[D_F, pi(a)]||_op
             <= 1 } is FINITE + regulator-free when the channel graph is CONNECTED
             (the S100a result, R-sweep dev 1.79e-9). THIS gate verifies the converse.

  DOUBLING-INVARIANCE NOTE: S100a verified d_C identical on the single 8-dim chiral
    star (D_p) and the J-doubled 16-dim D_F (max rel dev < 1e-6). The disconnect
    geometry is a property of the channel coupling graph, INDEPENDENT of the
    chiral/J doubling. This gate runs the single 8-dim chiral star (CPU-cheap; the
    physics is identical) and CROSS-CHECKS the primary severance on the 16-dim D_F.

  SEVERANCE (plan-frozen which-edge PRU closure):
    PRIMARY   = sever the (1,0) channel: t_{(1,0)} := 0  -> node g1 disconnects.
    DIAGNOSTIC= repeat on (1,1) and (3,0) severances (non-gating robustness rows).
    A severed edge cuts the Lipschitz path between node g and node v: || [D_F, pi(a)]
    || <= 1 no longer couples f(g) to f(v). The optimizer then pushes the inter-
    component offset to the Frobenius ball edge -> |f(v) - f(g)| = c*R (linear in R).

  R-SWEEP (the gate's observable, NOT a UV regulator):
    R in {1, 10, 100, 1000, 10000} * omega_max   -- the s100a grid (10/100/1000)
    extended ONE DECADE EACH WAY per the binding text. omega_max = max channel
    D^2-floor = max(omega_g), loaded from the s100a npz convention (the same scale
    the S100a R-sweep used: fac * float(omega.max())). The Frobenius bound
    ||pi(a)||_F <= R is a STATE-SPACE Lipschitz-ball radius on the metric face --
    its R-dependence IS the observable. No Seeley-DeWitt a_n is cited -> no
    a_n^{regulator} tag is required (plan SecW2-6 regulator-pin note).

SUBSTITUTION CHAIN (math-scripts.md; the slope-1 DIRECTION claim requires it):
  Claim: "the severed pair's regulated distance grows LINEARLY in R -- log-log
          slope EXACTLY 1; connected pairs are R-flat (slope 0 on the flat window)."
  Def 1 (regulated distance): d_R(p,q) = sup{ |f(p)-f(q)| : ||[D,f]||_op <= 1,
          ||f||_F <= R }                                  [the s100a machinery form]
  Def 2 (severed edge): t_g = 0 => the graph splits into two components; the
          Lipschitz constraint ||[D,f]|| <= 1 no longer couples f's values across
          components (no path of nonzero couplings).
  Substitute: between components |f(p)-f(q)| is bounded ONLY by the regulator: the
          optimizer pushes the inter-component offset to the ball edge,
          |f(p)-f(q)| = c*R, c the component-separation constant fixed by the gauge
          quotient within each component.
  Simplify:  d_R = c*R   =>   ln d_R = ln c + ln R
             d ln d_R / d ln R = 1   (EXACTLY; c drops out -- the multiplicative
             pre-factor is annihilated by the log-derivative: the math-scripts.md
             MANDATORY K=3 multiplicative-normalization-cancellation pattern on the
             regulator-scale axis. The SLOPE is the structural content; the intercept
             ln c is the empirical residue.)
  Direction: slope = +1 for the severed pair (CLASS-gamma commutative signature).
             For a connected pair the sup is attained INSIDE the ball once R > rho*
             (the activation threshold) => d_R INDEPENDENT of R -- slope 0, flat.
  Conclusion: |slope - 1| <= 1e-3 severed; R-dev <= 1e-8 connected (flat window);
             rho* <= 10*omega_max. A slope != 1 falsifies the linear-divergence form
             of Theorem A clause 3.

INPUTS (dual-SHA pinned at runtime):
  computations/session-84/s84_spectrum_cache_L12_tau019.npz   [STATIC pin
      9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9 -- HARD FAIL]
  computations/_shared/canonical_constants.py                 [runtime]
  computations/session-100a/s100a_connes_distance_ladder.py   [SDP machinery lineage;
      STATIC pin fe31ed40146a9aa148ecb72a4161b130d256cde8beeeb5c3d4a78df1a31bb97e]
  computations/session-100a/s100a_connes_distance_ladder.npz  [omega_max convention +
      flat-window reference; STATIC pin
      04a0062bdb94ff5e911695b71835d0a93923b99b98a2eb669adee1cee634e737]

OUTPUTS:
  computations/session-101/s101_connes_distance_disconnect_boundary.npz
  computations/session-101/s101_connes_distance_disconnect_boundary.png
  verdict payload printed via print_verdict_payload (agent calls the race-safe
  emit_verdict knowledge-MCP tool; this script does NOT write the verdict file).

Substrate framing (GEOMETRIC): the substrate's metric face is finite and regulator-
  free BECAUSE its channel coupling graph is connected -- connectivity IS the
  substrate property that makes state-pair geometry intrinsic. This gate verifies the
  converse: cut one coupling and the substrate's own metric announces the cut as a
  linear-in-R regulator dependence (CLASS-gamma) -- the geometry becomes container-
  dependent exactly where the substrate's relay structure is broken. Flow: D_K floors
  -> star couplings -> connectivity -> regulator-(in)dependence dichotomy.
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
from canonical_constants import tau_fold  # explicit name used for cache context

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
GATE_ID = "S101-CONNES-DISTANCE-DISCONNECT-BOUNDARY"               # (local)
SCHEME = "SDP-CLARABEL-CLASS-GAMMA-DISCONNECT"                     # (local)
CONVENTION = "substrate-state-pair-canonical"                      # (local)
L_MAX = 12                                                         # (local)

# Pre-registered thresholds (plan SecW2-6 operator block)
SLOPE_TOL = 1e-3                # |slope - 1| <= 1e-3 (severed pair)         # (local)
FLAT_TOL = 1e-8                 # connected-pair flat-window R-dev ceiling   # (local)
RHO_STAR_CEIL_FACTOR = 10.0     # rho* <= 10*omega_max                       # (local)
SDP_TOL = 1e-8                  # CLARABEL gap/feas rtol (s100a pin)         # (local)
R_SWEEP_FACTORS = (1.0, 10.0, 100.0, 1000.0, 10000.0)   # decade grid * omega_max  # (local)
PRIMARY_SEVER = (1, 0)          # plan-frozen primary severed channel        # (local)
DIAG_SEVER = [(1, 1), (3, 0)]   # diagnostic (non-gating) severances         # (local)
FLAT_ACTIVATION_TOL = 1e-8      # |d_R/d_intrinsic - 1| <= this -> activated # (local)

# Tower (triality-distinct generation channels) + conjugates + reference
TOWER = [(1, 0), (1, 1), (3, 0)]           # (local) generation channels
TOWER_CONJ = [(0, 1), (1, 1), (0, 3)]      # (local) BDI conjugate sectors
REF_SECTOR = (0, 0)                        # (local) vacuum/Higgs reference channel

# Static input pins (plan SecW2-6 input_files; 64-hex, verbatim)
SPECTRUM_CACHE_SHA_PIN = "9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9"
SDP_MACHINERY_SHA_PIN = "fe31ed40146a9aa148ecb72a4161b130d256cde8beeeb5c3d4a78df1a31bb97e"
CONNES_LADDER_NPZ_SHA_PIN = "04a0062bdb94ff5e911695b71835d0a93923b99b98a2eb669adee1cee634e737"

OUT_NPZ = _HERE / "s101_connes_distance_disconnect_boundary.npz"
OUT_PNG = _HERE / "s101_connes_distance_disconnect_boundary.png"

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
    """audit_sha256 over (script || canonical || sorted pinmap json), per the plan
    audit_discriminators: audit_sha256_inputs = [script, canonical, pinmap,
    s84_cache_sha, sdp_machinery_sha]. The cache + machinery SHAs enter the pinmap
    json (keyed by their relative paths), so the audit SHA covers all five inputs.
    content_sha256 over the script bytes alone."""
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
    companion_note="", extra_rows=None,
):
    """Print the emit_verdict payload (race-safe emission owned by the knowledge-MCP
    tool; this script never writes the verdict file). [VERIFY-THEOREM] -> NO 3-tuple.
    Session is the letter-free string '101' (tool schema accepts str)."""
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
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 5 -- Spectrum loading: channel floors at tau_fold (L=12 cache)
# ---------------------------------------------------------------------------
def load_floors():
    """Load per-sector spectral floors lambda_g = min|eigenvalue| for the tower.
    HARD FAIL if the cache SHA does not match the plan's static pin."""
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
    n_sectors = len(sec)  # (local)
    return floors, n_sectors


def load_omega_max_convention():
    """Load omega_max from the s100a connes-ladder npz (the R-sweep scale
    convention). HARD FAIL on SHA mismatch. omega_max = max channel D^2-floor =
    max(omega_D2_floors); this is the SAME scale the s100a R-sweep used
    (fac * float(omega.max())). Also returns the s100a connected-pair R-dev floor
    (rsweep_max_reldev) for the flatness-threshold provenance cross-check."""
    sha = sha256_of(CONNES_LADDER_NPZ)  # (local)
    if sha != CONNES_LADDER_NPZ_SHA_PIN:
        raise RuntimeError(
            f"s100a connes-ladder npz SHA mismatch: got {sha}, pinned {CONNES_LADDER_NPZ_SHA_PIN}"
        )
    d = np.load(CONNES_LADDER_NPZ, allow_pickle=True)  # (local)
    omega_s100a = np.asarray(d["omega_D2_floors"], dtype=np.float64)  # (local)
    omega_max = float(omega_s100a.max())  # (local)
    s100a_rsweep_floor = float(d["rsweep_max_reldev"])  # (local) the 1.79e-9 reference
    return omega_max, omega_s100a, s100a_rsweep_floor


# ---------------------------------------------------------------------------
# Section 6 -- Greybody chiral star (single 8-dim copy + J-doubled 16-dim)
# ---------------------------------------------------------------------------
def build_star(t):
    """4x4 Hermitian star: node 0 = vacuum reference, nodes 1..3 = generation
    channels; S[0,g] = S[g,0] = t[g-1]. A severed edge has t[g-1] = 0."""
    S = np.zeros((4, 4), dtype=np.float64)  # (local)
    for g in range(3):
        S[0, g + 1] = t[g]
        S[g + 1, 0] = t[g]
    return S


def chiral(S):
    """8x8 chiral doubling [[0,S],[S,0]]."""
    Z = np.zeros((4, 4))  # (local)
    return np.block([[Z, S], [S, Z]])


def projectors8():
    """Channel projectors E_k on the single 8-dim chiral star (summed over the
    2 chirality copies)."""
    E = []  # (local)
    for ch in range(4):
        e = np.zeros(8)  # (local)
        for chir in range(2):
            e[chir * 4 + ch] = 1.0
        E.append(np.diag(e))
    return E


def build_doubled_16(t_part, t_anti):
    """J-doubled 16-dim D_F + 16-dim channel projectors (for the primary-severance
    cross-check; layout = copy*8 + chir*4 + channel)."""
    D_p = chiral(build_star(t_part))  # (local) 8x8
    D_a = chiral(build_star(t_anti))  # (local) 8x8
    D_F = np.block([
        [D_p, np.zeros((8, 8))],
        [np.zeros((8, 8)), D_a],
    ])  # (local) 16x16
    E16 = []  # (local)
    for ch in range(4):
        e = np.zeros(16)  # (local)
        for copy in range(2):
            for chir in range(2):
                e[copy * 8 + chir * 4 + ch] = 1.0
        E16.append(np.diag(e))
    return D_F, E16


# ---------------------------------------------------------------------------
# Section 7 -- Connes-distance SDP on the channel algebra (IKM finite form)
# ---------------------------------------------------------------------------
def connes_distance_sdp(D_op, E, i_ch, j_ch, frob_bound=None, sdp_tol=SDP_TOL):
    """d_C(omega_i, omega_j) on the commutative channel algebra:

        max  (a_i - a_j)   s.t.  || [D_op, pi(a)] ||_op <= 1,
        pi(a) = sum_k x_k E_k,  gauge-fix x_j = 0.

    Optional Frobenius bound ||pi(a)||_F <= frob_bound (the R-sweep regulator).
    On a CONNECTED graph the feasible set is compact and d_C is finite; on a
    DISCONNECTED graph (severed edge) the inter-component offset is bounded ONLY
    by frob_bound, so d_C grows = c*frob_bound. Returns d_C plus the pos/neg
    objective values and CLARABEL statuses (status='unbounded' on disconnect with
    no frob bound is the expected degenerate certificate)."""
    n = D_op.shape[0]  # (local)
    K = len(E)  # (local)
    free = [k for k in range(K) if k != j_ch]  # (local)
    x = cp.Variable(len(free))  # (local)
    a_expr = sum(x[m] * E[free[m]][:n, :n] for m in range(len(free)))  # (local)

    comm = D_op @ a_expr - a_expr @ D_op  # (local)
    I_n = np.eye(n)  # (local)
    lmi = cp.bmat([[I_n, comm], [comm.T, I_n]])  # (local)
    constraints = [lmi >> 0]  # (local)
    if frob_bound is not None:
        constraints.append(cp.norm(a_expr, "fro") <= float(frob_bound))

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


def ols_loglog_slope(R_vals, d_vals):
    """Centered OLS slope of ln d on ln R over the finite points. Returns
    (slope, n_finite, intercept_ln_c)."""
    R_vals = np.asarray(R_vals, dtype=np.float64)  # (local)
    d_vals = np.asarray(d_vals, dtype=np.float64)  # (local)
    fin = np.isfinite(d_vals) & (d_vals > 0)  # (local)
    if fin.sum() < 2:
        return float("nan"), int(fin.sum()), float("nan")
    lnR = np.log(R_vals[fin])  # (local)
    lnd = np.log(d_vals[fin])  # (local)
    xc = lnR - lnR.mean()  # (local)
    yc = lnd - lnd.mean()  # (local)
    slope = float((xc @ yc) / (xc @ xc))  # (local)
    intercept = float(lnd.mean() - slope * lnR.mean())  # (local) ln c
    return slope, int(fin.sum()), intercept


# ---------------------------------------------------------------------------
# Section 8 -- one severance configuration
# ---------------------------------------------------------------------------
def run_severance(t_full, omega_max, sever_ch_idx, sever_label, D_doubled=None,
                  E16=None):
    """Sever channel index `sever_ch_idx` (0-based into TOWER) on the single 8-dim
    chiral star, run the full 5-point R-sweep on the severed pair and on the
    connected pairs, fit the severed-pair log-log slope, find rho*, and (optionally,
    primary only) cross-check on the doubled 16-dim D_F.

    Returns a dict with all per-configuration measurements."""
    E8 = projectors8()  # (local)
    sever_node = sever_ch_idx + 1  # (local) channel node index (1..3)

    t_sev = t_full.copy()  # (local)
    t_sev[sever_ch_idx] = 0.0
    D_p = chiral(build_star(t_sev))  # (local) single 8-dim severed star

    R_grid = np.array([f * omega_max for f in R_SWEEP_FACTORS], dtype=np.float64)  # (local)

    # --- severed pair d(v, severed_node) over the R-grid (8-dim)
    sev_d = []  # (local)
    sev_status = []  # (local)
    for R in R_grid:
        r = connes_distance_sdp(D_p, E8, i_ch=sever_node, j_ch=0, frob_bound=R)  # (local)
        sev_d.append(r["d_C"])
        sev_status.append(f"{r['status_pos']}|{r['status_neg']}")
    sev_d = np.array(sev_d)  # (local)
    sev_bounded = np.isfinite(sev_d)  # (local)
    slope, n_fin, ln_c = ols_loglog_slope(R_grid[sev_bounded], sev_d[sev_bounded])  # (local)
    slope_dev = abs(slope - 1.0) if np.isfinite(slope) else float("nan")  # (local)

    # severed-pair UNREGULATED check (no frob bound) -> expected 'unbounded'
    sev_unreg = connes_distance_sdp(D_p, E8, i_ch=sever_node, j_ch=0)  # (local)
    sev_unreg_unbounded = bool(
        "unbounded" in (sev_unreg["status_pos"] + sev_unreg["status_neg"]).lower()
        or not np.isfinite(sev_unreg["d_C"])
    )  # (local)

    # INFO degenerate path: UNBOUNDED in the regulated sweep before the largest R
    info_degenerate = bool(not np.all(sev_bounded))  # (local)
    largest_bounded_R = float(R_grid[sev_bounded].max()) if sev_bounded.any() else float("nan")  # (local)

    # --- connected pairs: the OTHER two channels d(v, ch)
    connected_idx = [k for k in range(3) if k != sever_ch_idx]  # (local)
    conn_results = {}  # (local)
    rho_star_per_pair = []  # (local)
    conn_flat_reldev_per_pair = []  # (local)
    conn_full_reldev_per_pair = []  # (local)
    for ch_idx in connected_idx:
        node = ch_idx + 1  # (local)
        # intrinsic (unregulated) distance on the severed graph
        intr = connes_distance_sdp(D_p, E8, i_ch=node, j_ch=0)  # (local)
        d_intr = intr["d_C"]  # (local)
        d_grid = []  # (local)
        st_grid = []  # (local)
        for R in R_grid:
            r = connes_distance_sdp(D_p, E8, i_ch=node, j_ch=0, frob_bound=R)  # (local)
            d_grid.append(r["d_C"])
            st_grid.append(f"{r['status_pos']}|{r['status_neg']}")
        d_grid = np.array(d_grid)  # (local)
        # activation: first R where |d_R/d_intr - 1| <= FLAT_ACTIVATION_TOL
        rho_star = float("inf")  # (local)
        for i in range(len(R_grid)):
            if np.isfinite(d_grid[i]) and abs(d_grid[i] / d_intr - 1.0) <= FLAT_ACTIVATION_TOL:
                rho_star = float(R_grid[i])
                break
        # flat-window flatness: rel dev across R >= rho* (R0 = first flat point)
        flat_mask = (R_grid >= rho_star) & np.isfinite(d_grid)  # (local)
        if flat_mask.sum() >= 2:
            flat_vals = d_grid[flat_mask]  # (local)
            flat_reldev = float(np.max(np.abs(flat_vals / flat_vals[0] - 1.0)))  # (local)
        elif flat_mask.sum() == 1:
            flat_reldev = 0.0  # (local) single flat point: trivially flat
        else:
            flat_reldev = float("nan")
        # full-grid rel dev (diagnostic; includes sub-rho* ball-limited points)
        if np.all(np.isfinite(d_grid)):
            full_reldev = float(np.max(np.abs(d_grid / d_grid[0] - 1.0)))  # (local)
        else:
            full_reldev = float("nan")
        conn_results[f"{TOWER[ch_idx]}"] = {
            "node": node, "d_intrinsic": d_intr, "d_grid": d_grid,
            "status_grid": st_grid, "rho_star": rho_star,
            "flat_reldev": flat_reldev, "full_reldev": full_reldev,
        }
        rho_star_per_pair.append(rho_star)
        conn_flat_reldev_per_pair.append(flat_reldev)
        conn_full_reldev_per_pair.append(full_reldev)

    rho_star = float(np.max(rho_star_per_pair))  # (local) activation = max over connected pairs
    conn_flat_reldev = float(np.nanmax(conn_flat_reldev_per_pair))  # (local) worst flat-window dev
    conn_full_reldev = float(np.nanmax(conn_full_reldev_per_pair))  # (local) worst full-grid dev

    # --- primary-only: doubled-16 cross-check of the severed-pair slope
    doubled = {}  # (local)
    if D_doubled is not None and E16 is not None:
        d16 = []  # (local)
        for R in R_grid:
            r = connes_distance_sdp(D_doubled, E16, i_ch=sever_node, j_ch=0, frob_bound=R)  # (local)
            d16.append(r["d_C"])
        d16 = np.array(d16)  # (local)
        fin16 = np.isfinite(d16)  # (local)
        slope16, _, _ = ols_loglog_slope(R_grid[fin16], d16[fin16])  # (local)
        doubling_slope_dev = abs(slope16 - slope) if np.isfinite(slope16) and np.isfinite(slope) else float("nan")  # (local)
        doubled = {"d16_grid": d16, "slope16": slope16,
                   "doubling_slope_dev": doubling_slope_dev}

    return {
        "sever_label": sever_label, "sever_node": sever_node,
        "sever_ch": TOWER[sever_ch_idx],
        "R_grid": R_grid, "R_factors": np.array(R_SWEEP_FACTORS),
        "sev_d": sev_d, "sev_status": sev_status, "sev_bounded": sev_bounded,
        "slope": slope, "slope_dev": slope_dev, "ln_c": ln_c, "n_finite": n_fin,
        "sev_unreg_unbounded": sev_unreg_unbounded,
        "info_degenerate": info_degenerate, "largest_bounded_R": largest_bounded_R,
        "connected_idx": connected_idx, "conn": conn_results,
        "rho_star": rho_star, "conn_flat_reldev": conn_flat_reldev,
        "conn_full_reldev": conn_full_reldev,
        "doubled": doubled,
    }


# ---------------------------------------------------------------------------
# Section 9 -- Compute orchestrator
# ---------------------------------------------------------------------------
def compute():
    floors, n_sectors = load_floors()
    omega_max, omega_s100a, s100a_rsweep_floor = load_omega_max_convention()
    print(f"  L=12 cache loaded: {n_sectors} sectors")
    print(f"  tower floors lambda_g(tau_fold={tau_fold}): "
          f"(1,0)={floors[0]:.8f} (1,1)={floors[1]:.8f} (3,0)={floors[2]:.8f}")

    omega = floors ** 2  # (local) channel D^2-floors
    t_full = 1.0 / omega  # (local) greybody couplings (kappa=1; full connected star)
    print(f"  omega_g = lambda_g^2: {omega[0]:.9f}, {omega[1]:.9f}, {omega[2]:.9f}")
    print(f"  greybody t_g = 1/omega_g (full star): {t_full[0]:.6f}, {t_full[1]:.6f}, {t_full[2]:.6f}")

    # omega_max convention cross-check: our cache floors must reproduce the s100a
    # omega_D2_floors exactly (same cache, same tau_fold)
    omega_match = float(np.max(np.abs(omega - omega_s100a) / omega_s100a))  # (local)
    print(f"  omega_max (s100a convention, max channel D^2-floor) = {omega_max:.9f}")
    print(f"  omega vs s100a omega_D2_floors max rel dev: {omega_match:.3e}  "
          f"(same cache identity)")
    print(f"  s100a connected-pair R-sweep floor (provenance ref): {s100a_rsweep_floor:.3e}  "
          f"(plan flatness ceiling {FLAT_TOL} sits above it: {FLAT_TOL > s100a_rsweep_floor})")
    print(f"  R-grid factors: {R_SWEEP_FACTORS}  -> R = factor * omega_max")
    print(f"  rho* ceiling = {RHO_STAR_CEIL_FACTOR}*omega_max = "
          f"{RHO_STAR_CEIL_FACTOR * omega_max:.9f}")

    # antiparticle couplings for the doubled-16 cross-check (conjugate sectors,
    # iso-spectral by BDI => same floors => same t)
    t_anti = t_full.copy()  # (local) conjugate floors equal tower floors (BDI)

    # --- PRIMARY severance: (1,0), with doubled-16 cross-check
    print(f"\n  === PRIMARY severance: {PRIMARY_SEVER} (t = 0; plan-frozen) ===")
    prim_idx = TOWER.index(PRIMARY_SEVER)  # (local)
    t_sev_part = t_full.copy(); t_sev_part[prim_idx] = 0.0  # (local)
    t_sev_anti = t_anti.copy(); t_sev_anti[prim_idx] = 0.0  # (local)
    D_F16, E16 = build_doubled_16(t_sev_part, t_sev_anti)  # (local) doubled severed
    prim = run_severance(t_full, omega_max, prim_idx, f"{PRIMARY_SEVER}",
                         D_doubled=D_F16, E16=E16)
    print(f"  severed pair d(v,{PRIMARY_SEVER}) over R-grid:")
    for i, R in enumerate(prim["R_grid"]):
        print(f"    R={R:12.4f}: d_R={prim['sev_d'][i]:.9f}  [{prim['sev_status'][i]}]")
    print(f"  severed-pair log-log OLS slope = {prim['slope']:.9f}  "
          f"|slope-1| = {prim['slope_dev']:.3e}  (intercept ln c = {prim['ln_c']:.6f}; "
          f"c = {np.exp(prim['ln_c']):.6f})")
    print(f"  severed-pair UNREGULATED status unbounded: {prim['sev_unreg_unbounded']} "
          f"(no Lipschitz path across the cut)")
    if prim["doubled"]:
        print(f"  doubled-16 cross-check slope = {prim['doubled']['slope16']:.9f}  "
              f"(|slope16-slope8| = {prim['doubled']['doubling_slope_dev']:.3e})")
    print(f"  connected pairs (R-flat once R > rho*):")
    for nm, c in prim["conn"].items():
        print(f"    d(v,{nm}): intrinsic={c['d_intrinsic']:.9f}  rho*={c['rho_star']:.6f}  "
              f"flat-window reldev={c['flat_reldev']:.3e}  full-grid reldev={c['full_reldev']:.3e}")
    print(f"  rho* (max over connected pairs) = {prim['rho_star']:.9f}  "
          f"(<= {RHO_STAR_CEIL_FACTOR}*omega_max = {RHO_STAR_CEIL_FACTOR*omega_max:.6f}: "
          f"{prim['rho_star'] <= RHO_STAR_CEIL_FACTOR * omega_max})")
    print(f"  connected worst flat-window reldev = {prim['conn_flat_reldev']:.3e}")

    # --- DIAGNOSTIC severances: (1,1), (3,0) [non-gating]
    diag = []  # (local)
    for sev_ch in DIAG_SEVER:
        print(f"\n  --- DIAGNOSTIC severance: {sev_ch} (non-gating) ---")
        idx = TOWER.index(sev_ch)  # (local)
        dres = run_severance(t_full, omega_max, idx, f"{sev_ch}")  # (local)
        print(f"    severed slope = {dres['slope']:.9f}  |slope-1| = {dres['slope_dev']:.3e}  "
              f"(bounded pts {dres['n_finite']}/5; UNBOUNDED-unreg {dres['sev_unreg_unbounded']})")
        print(f"    rho* = {dres['rho_star']:.6f}  conn flat-window reldev = {dres['conn_flat_reldev']:.3e}")
        diag.append(dres)

    # --- gating verdict (PRIMARY only; diagnostics are robustness rows)
    rho_star_ceil = RHO_STAR_CEIL_FACTOR * omega_max  # (local)
    crit_a = bool(np.isfinite(prim["slope_dev"]) and prim["slope_dev"] <= SLOPE_TOL)  # (local)
    crit_b = bool(np.isfinite(prim["conn_flat_reldev"]) and prim["conn_flat_reldev"] <= FLAT_TOL)  # (local)
    crit_c = bool(np.isfinite(prim["rho_star"]) and prim["rho_star"] <= rho_star_ceil)  # (local)
    print(f"\n  crit_a (|slope-1| <= {SLOPE_TOL}):              {crit_a}  ({prim['slope_dev']:.3e})")
    print(f"  crit_b (connected flat-window reldev <= {FLAT_TOL}): {crit_b}  ({prim['conn_flat_reldev']:.3e})")
    print(f"  crit_c (rho* <= {RHO_STAR_CEIL_FACTOR}*omega_max):       {crit_c}  "
          f"({prim['rho_star']:.6f} <= {rho_star_ceil:.6f})")

    # solver cleanliness on the gating configuration (all SDPs optimal)
    ok_status = {"optimal", "optimal_inaccurate"}  # (local)
    sev_statuses_ok = all(
        all(s.strip() in ok_status for s in stat.split("|"))
        for stat in prim["sev_status"]
    )  # (local)
    conn_statuses_ok = all(
        all(s.strip() in ok_status for s in stat.split("|"))
        for c in prim["conn"].values() for stat in c["status_grid"]
    )  # (local)
    solver_clean = bool(sev_statuses_ok and conn_statuses_ok)  # (local)
    print(f"  solver_clean (all gating SDP statuses optimal): {solver_clean}")

    # --- composite (plan rubric):
    #   INFO  iff severed-pair UNBOUNDED before largest R (degenerate confirmation)
    #   PASS  iff (a) ^ (b) ^ (c)
    #   FAIL  otherwise (slope != 1 beyond tol, OR connected flatness broken w/ clean solver)
    if prim["info_degenerate"]:
        composite = "INFO"  # (local) degenerate divergence confirmation
        verdict_reason = (
            f"severed-pair SDP UNBOUNDED before largest R; degenerate divergence "
            f"confirmation; largest bounded R = {prim['largest_bounded_R']:.4f}"
        )  # (local)
    elif crit_a and crit_b and crit_c:
        composite = "PASS"
        verdict_reason = "linear-in-R CLASS-gamma divergence (slope 1) + connected R-flat + rho* consistent"
    else:
        composite = "FAIL"
        fails = []  # (local)
        if not crit_a:
            fails.append(f"slope!=1 ({prim['slope']:.6f}, dev {prim['slope_dev']:.3e}>{SLOPE_TOL})")
        if not crit_b:
            fails.append(f"connected-flatness ({prim['conn_flat_reldev']:.3e}>{FLAT_TOL}, solver_clean={solver_clean})")
        if not crit_c:
            fails.append(f"rho*>{RHO_STAR_CEIL_FACTOR}*omega_max ({prim['rho_star']:.6f}>{rho_star_ceil:.6f})")
        verdict_reason = "; ".join(fails)
    print(f"\n  composite verdict: {composite}  ({verdict_reason})")

    return {
        "floors": floors, "omega": omega, "t_full": t_full, "omega_max": omega_max,
        "omega_match": omega_match, "s100a_rsweep_floor": s100a_rsweep_floor,
        "rho_star_ceil": rho_star_ceil,
        "prim": prim, "diag": diag,
        "crit_a": crit_a, "crit_b": crit_b, "crit_c": crit_c,
        "solver_clean": solver_clean, "composite": composite,
        "verdict_reason": verdict_reason,
    }


# ---------------------------------------------------------------------------
# Section 10 -- Plot
# ---------------------------------------------------------------------------
def make_plot(res):
    prim = res["prim"]  # (local)
    fig, axes = plt.subplots(1, 3, figsize=(16, 5.2))

    # Panel A: severed-pair log-log divergence (slope 1) + connected flat lines
    ax = axes[0]
    R = prim["R_grid"]  # (local)
    ax.loglog(R, prim["sev_d"], "r^-", markersize=9,
              label=f"severed {prim['sever_ch']}: slope={prim['slope']:.4f}")
    # slope-1 reference through the first severed point
    c0 = prim["sev_d"][0] / R[0] if np.isfinite(prim["sev_d"][0]) else 1.0  # (local)
    ax.loglog(R, c0 * R, "k--", alpha=0.6, label="slope-1 reference $d=cR$")
    for nm, c in prim["conn"].items():
        ax.loglog(R, c["d_grid"], "o-", markersize=6, label=f"connected {nm} (flat)")
    ax.axvline(prim["rho_star"], color="gray", ls=":", alpha=0.7,
               label=f"$\\rho^*$={prim['rho_star']:.3f}")
    ax.axvline(res["rho_star_ceil"], color="green", ls="--", alpha=0.5,
               label=f"$10\\,\\omega_{{max}}$={res['rho_star_ceil']:.3f}")
    ax.set_xlabel("$R$  (Frobenius ball radius) [$\\omega_{max}$ units]")
    ax.set_ylabel("$d_R(v, g)$")
    ax.set_title(f"disconnect divergence: severed slope {prim['slope']:.6f}\n"
                 f"|slope-1|={prim['slope_dev']:.1e} (tol {SLOPE_TOL})")
    ax.legend(fontsize=7)
    ax.grid(alpha=0.3, which="both")

    # Panel B: connected-pair flat-window rel-dev + rho* per pair
    ax = axes[1]
    names = list(prim["conn"].keys())  # (local)
    flat_devs = [prim["conn"][n]["flat_reldev"] for n in names]  # (local)
    full_devs = [prim["conn"][n]["full_reldev"] for n in names]  # (local)
    xpos = np.arange(len(names))  # (local)
    w = 0.35  # (local)
    ax.bar(xpos - w / 2, flat_devs, w, color="tab:green", label="flat-window reldev (gated)")
    ax.bar(xpos + w / 2, full_devs, w, color="tab:orange", alpha=0.7,
           label="full-grid reldev (diag)")
    ax.axhline(FLAT_TOL, color="red", ls="--", label=f"flatness ceiling {FLAT_TOL}")
    ax.axhline(res["s100a_rsweep_floor"], color="purple", ls=":",
               label=f"s100a R-dev floor {res['s100a_rsweep_floor']:.1e}")
    ax.set_yscale("log")
    ax.set_xticks(xpos)
    ax.set_xticklabels([f"connected\n{n}" for n in names], fontsize=8)
    ax.set_ylabel("max rel dev across R")
    ax.set_title(f"connected-pair R-flatness\nworst flat-window {prim['conn_flat_reldev']:.1e}")
    ax.legend(fontsize=7)
    ax.grid(alpha=0.3, axis="y", which="both")

    # Panel C: severed-pair slope across all 3 severance configs (primary + diag)
    ax = axes[2]
    labels = [f"{prim['sever_ch']}\n(PRIMARY)"] + [f"{d['sever_ch']}\n(diag)" for d in res["diag"]]  # (local)
    slopes = [prim["slope"]] + [d["slope"] for d in res["diag"]]  # (local)
    colors = ["tab:red"] + ["tab:blue"] * len(res["diag"])  # (local)
    xp = np.arange(len(slopes))  # (local)
    ax.bar(xp, slopes, color=colors)
    ax.axhspan(1 - SLOPE_TOL, 1 + SLOPE_TOL, color="green", alpha=0.25,
               label=f"slope-1 band $\\pm${SLOPE_TOL}")
    ax.axhline(1.0, color="k", ls="--", alpha=0.6)
    for i, s in enumerate(slopes):
        if np.isfinite(s):
            ax.annotate(f"{s:.6f}", (i, s), textcoords="offset points",
                        xytext=(0, 5), ha="center", fontsize=8)
    ax.set_xticks(xp)
    ax.set_xticklabels(labels, fontsize=8)
    ax.set_ylabel("log-log slope")
    ax.set_ylim(0.95, 1.05)
    ax.set_title(f"severed-pair slope (all 3 severances)\ncomposite={res['composite']}")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, axis="y")

    fig.suptitle(
        f"{GATE_ID}  (L=12, tau_fold={tau_fold}; sever {prim['sever_ch']}; "
        f"slope {prim['slope']:.6f}; rho*={prim['rho_star']:.3f}<=10wmax={res['rho_star_ceil']:.3f}; "
        f"{res['composite']})",
        fontsize=10,
    )
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)
    print(f"  Plot saved: {OUT_PNG.name}")


# ---------------------------------------------------------------------------
# Section 11 -- Main
# ---------------------------------------------------------------------------
def _flat_obj_arr(list_of_dicts, key):
    """Pack a per-config 1-D array under `key` into an object array for npz."""
    return np.array([d[key] for d in list_of_dicts], dtype=object)


def main():
    t0 = time.time()  # (local)
    print(f"=== {GATE_ID} ===")
    print(f"Session {SESSION}  L_max={L_MAX}  scheme={SCHEME}")
    print(f"convention={CONVENTION}  (Cell-IV state-pair; no §VII landing)")

    pins = log_input_pins(INPUT_FILES)  # (local)
    closure = closure_hash(pins)  # (local)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_CONSTS, pins)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print()

    res = compute()
    prim = res["prim"]  # (local)

    # --- npz (full float64 round-trip per Class 8.3)
    diag_labels = np.array([d["sever_label"] for d in res["diag"]])  # (local)
    diag_slopes = np.array([d["slope"] for d in res["diag"]])  # (local)
    diag_slope_devs = np.array([d["slope_dev"] for d in res["diag"]])  # (local)
    diag_rho_stars = np.array([d["rho_star"] for d in res["diag"]])  # (local)
    diag_conn_flat = np.array([d["conn_flat_reldev"] for d in res["diag"]])  # (local)
    diag_sev_d = np.array([d["sev_d"] for d in res["diag"]])  # (local) (2,5)
    diag_n_finite = np.array([d["n_finite"] for d in res["diag"]])  # (local)
    diag_unreg_unbounded = np.array([d["sev_unreg_unbounded"] for d in res["diag"]])  # (local)

    # connected-pair grids for the primary config (object arrays: variable channel set)
    prim_conn_names = list(prim["conn"].keys())  # (local)
    prim_conn_intr = np.array([prim["conn"][n]["d_intrinsic"] for n in prim_conn_names])  # (local)
    prim_conn_grids = np.array([prim["conn"][n]["d_grid"] for n in prim_conn_names])  # (local)
    prim_conn_rho = np.array([prim["conn"][n]["rho_star"] for n in prim_conn_names])  # (local)
    prim_conn_flat = np.array([prim["conn"][n]["flat_reldev"] for n in prim_conn_names])  # (local)
    prim_conn_full = np.array([prim["conn"][n]["full_reldev"] for n in prim_conn_names])  # (local)

    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID, scheme=SCHEME, convention=CONVENTION, l_max=L_MAX,
        verdict=res["composite"], verdict_reason=res["verdict_reason"],
        trigger="[VERIFY-THEOREM]", corner_cell="Cell-IV-state-pair-algebra-DEPENDENT",
        tau_fold_used=tau_fold,
        # cache + convention
        tower_pq=np.array(TOWER), ref_sector=np.array(REF_SECTOR),
        floors_lambda_min=res["floors"], omega_D2_floors=res["omega"],
        greybody_couplings_full=res["t_full"], omega_max=res["omega_max"],
        omega_vs_s100a_reldev=res["omega_match"],
        s100a_rsweep_floor=res["s100a_rsweep_floor"],
        R_sweep_factors=np.array(R_SWEEP_FACTORS),
        R_grid=prim["R_grid"], rho_star_ceiling=res["rho_star_ceil"],
        # PRIMARY severance (gating)
        primary_sever_channel=np.array(PRIMARY_SEVER), primary_sever_node=prim["sever_node"],
        primary_severed_d_grid=prim["sev_d"], primary_severed_status=np.array(prim["sev_status"]),
        primary_slope=prim["slope"], primary_slope_dev=prim["slope_dev"],
        primary_intercept_ln_c=prim["ln_c"], primary_c=float(np.exp(prim["ln_c"])),
        primary_n_finite=prim["n_finite"],
        primary_sev_unreg_unbounded=prim["sev_unreg_unbounded"],
        primary_info_degenerate=prim["info_degenerate"],
        primary_largest_bounded_R=prim["largest_bounded_R"],
        primary_rho_star=prim["rho_star"], primary_conn_flat_reldev=prim["conn_flat_reldev"],
        primary_conn_full_reldev=prim["conn_full_reldev"],
        primary_conn_names=np.array(prim_conn_names), primary_conn_intrinsic=prim_conn_intr,
        primary_conn_d_grids=prim_conn_grids, primary_conn_rho_star=prim_conn_rho,
        primary_conn_flat_reldev_per_pair=prim_conn_flat,
        primary_conn_full_reldev_per_pair=prim_conn_full,
        # doubled-16 cross-check
        doubled16_slope=prim["doubled"].get("slope16", np.nan),
        doubled16_slope_dev=prim["doubled"].get("doubling_slope_dev", np.nan),
        doubled16_d_grid=prim["doubled"].get("d16_grid", np.array([])),
        # DIAGNOSTIC severances (non-gating)
        diag_sever_labels=diag_labels, diag_slopes=diag_slopes,
        diag_slope_devs=diag_slope_devs, diag_rho_stars=diag_rho_stars,
        diag_conn_flat_reldev=diag_conn_flat, diag_severed_d_grids=diag_sev_d,
        diag_n_finite=diag_n_finite, diag_sev_unreg_unbounded=diag_unreg_unbounded,
        # thresholds + criteria
        slope_tol=SLOPE_TOL, flat_tol=FLAT_TOL,
        rho_star_ceil_factor=RHO_STAR_CEIL_FACTOR, sdp_tol=SDP_TOL,
        crit_a=res["crit_a"], crit_b=res["crit_b"], crit_c=res["crit_c"],
        solver_clean=res["solver_clean"],
        spectrum_cache_sha=SPECTRUM_CACHE_SHA_PIN,
        sdp_machinery_sha=SDP_MACHINERY_SHA_PIN,
        connes_ladder_npz_sha=CONNES_LADDER_NPZ_SHA_PIN,
        audit_sha256=audit_sha, content_sha256=content_sha,
        schema_version="S84+",
    )
    print(f"\n  Data saved: {OUT_NPZ.name} ({OUT_NPZ.stat().st_size} bytes)")

    make_plot(res)

    # --- verdict payload (agent passes to race-safe emit_verdict MCP tool)
    value_str = (
        f"slope={prim['slope']:.6f}_"
        f"{'IN' if res['crit_a'] else 'OUTSIDE'}[1+-{SLOPE_TOL}];"
        f"|slope-1|={prim['slope_dev']:.2e};"
        f"sever={PRIMARY_SEVER[0]},{PRIMARY_SEVER[1]}_t=0;"
        f"d_R=({prim['sev_d'][0]:.4f}..{prim['sev_d'][-1]:.2f})linear_c={np.exp(prim['ln_c']):.6f};"
        f"connected_flat-window_reldev={prim['conn_flat_reldev']:.2e}_"
        f"{'<=' if res['crit_b'] else '>'}{FLAT_TOL};"
        f"rho*={prim['rho_star']:.4f}_"
        f"{'<=' if res['crit_c'] else '>'}10wmax={res['rho_star_ceil']:.4f};"
        f"omega_max={res['omega_max']:.6f};"
        f"crit_abc=({res['crit_a']},{res['crit_b']},{res['crit_c']});"
        f"solver_clean={res['solver_clean']};"
        f"unreg_unbounded={prim['sev_unreg_unbounded']}"
    )  # (local)
    companion = (
        f"severed (1,0) edge t=0 disconnects node g1: d_R=c*R EXACT (c={np.exp(prim['ln_c']):.6f}=1/sqrt2 "
        f"on the 2-node component), log-log slope {prim['slope']:.9f} (intercept ln c "
        f"annihilated by the log-derivative -- math-scripts.md K=3 multiplicative-cancellation "
        f"on the regulator-scale axis; SLOPE is structure, ln c is the empirical residue); "
        f"connected pairs flat once R>rho* (S100a CLASS-gamma converse: full M_n(C) diverges, "
        f"commutative channel restriction finite-and-flat WHEN connected)"
    )  # (local)
    extra = [
        (f"# DIAGNOSTIC severances (non-gating robustness): "
         f"(1,1) slope={res['diag'][0]['slope']:.6f} (dev {res['diag'][0]['slope_dev']:.1e}, "
         f"rho*={res['diag'][0]['rho_star']:.4f}, conn-flat {res['diag'][0]['conn_flat_reldev']:.1e}); "
         f"(3,0) slope={res['diag'][1]['slope']:.6f} (dev {res['diag'][1]['slope_dev']:.1e}, "
         f"rho*={res['diag'][1]['rho_star']:.4f}, conn-flat {res['diag'][1]['conn_flat_reldev']:.1e}) "
         f"# {GATE_ID}"),
        (f"# doubled-16 D_F cross-check: severed-pair slope16={prim['doubled'].get('slope16', float('nan')):.6f} "
         f"(|slope16-slope8|={prim['doubled'].get('doubling_slope_dev', float('nan')):.1e}); the disconnect "
         f"geometry is doubling-invariant (a property of the channel coupling graph, not of the chiral/J "
         f"doubling) # {GATE_ID}"),
        (f"# omega_max convention: max channel D^2-floor = {res['omega_max']:.9f} (loaded from "
         f"s100a_connes_distance_ladder.npz omega_D2_floors; same cache identity dev {res['omega_match']:.1e}); "
         f"flatness ceiling {FLAT_TOL} sits above the s100a connected R-dev floor {res['s100a_rsweep_floor']:.2e}; "
         f"Cell-IV state-pair (algebra-DEPENDENT), NO §VII landing in this gate # {GATE_ID}"),
    ]  # (local)

    print()
    print_verdict_payload(
        res["composite"], value_str, audit_sha, content_sha,
        companion_note=companion, extra_rows=extra,
    )

    print(f"\n=== {GATE_ID}: {res['composite']} (wall {time.time() - t0:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
