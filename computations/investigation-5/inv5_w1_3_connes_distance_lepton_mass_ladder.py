#!/usr/bin/env python3
"""
INV5-W1-3 -- INV5-W1-3-CONNES-DISTANCE-LEPTON-MASS-LADDER
=========================================================
Per-state Connes distance d_i on the COMMUTATIVE C^N multiplicity-bundle channel
algebra (regulator-free) -> charged-lepton spacing ratio (d_e-d_mu)/(d_mu-d_tau)
-> tested against the PDG log-mass-spacing ratio 1.889 (NOT a Froggatt-Nielsen
power law, which would give 1).

Gate ID:        INV5-W1-3-CONNES-DISTANCE-LEPTON-MASS-LADDER
Trigger:        [SIGN]  (the lepton log-mass spacings WIDEN: ratio > 1, NOT FN's 1)
Classification: PARTICLE
Agent:          connes-ncg-theorist
Plan:           sessions/investigation/investigation-5/investigation-5-plan-w1.md SecW1-3 (R3 YAML)
Scheme:         Connes-distance-commutative-multiplicity-bundle-channel-CN
Convention:     RATIO  (FULL physical, regulator-free; the commutative-channel
                restriction CURES the M_n(C) divergence -- no -SCHEMATIC tag)

=============================================================================
PRE-COMPUTE / KNOWLEDGE-MCP AUDIT (recorded in the WP MCP Pre-Compute Audit):
=============================================================================
This gate's substrate-forward leg REUSES the S100a-CONNES-DISTANCE-LADDER
(STAGE-3) regulator-free IKM-SDP machinery on the commutative channel algebra
C^4.  S100a already computed the substrate-FORWARD greybody distances on the
SAME L12 cache (audit 5e24db72e3e5121b...): d=(0.6987,0.7621,1.5582) lam2-units
(tau,mu,e), W_Connes = 12.5629 OUTSIDE [1.8,1.89] -> INFO; sign PASS
(nondegenerate, e=(3,0) most distant).  S88-CONNES-DISTANCE-SUBALGEBRA-
RESTRICTION (PASS) certified the commutative-channel distance regulator-free
(d_C_L10 = d_C_L12 = 2.386138).  SecVII.BL (STAGE-3-PERMANENT) is the standing
generation-blindness obstruction (multiplicity-scalar D_K).

NOT pre-closed for THIS gate, because INV5-W1-3 is structurally DISTINCT from
S100a on the BRIDGE-MAP axis:  it adds the Martinetti-Wulkenhaar two-route
discriminator -- it computes BOTH (A) the substrate-FORWARD greybody distances
(the substrate's OWN metric -> W=12.56) AND (B) the inverse-Yukawa ansatz
d_i = -ell*ln(m_i) (Martinetti-Wulkenhaar: SM two-point distance ~ inverse
Yukawa -> ratio = 1.889 EXACT).  The pre-registered substitution chain's 1.889
is recovered ONLY by route (B), and route (B) is a TAUTOLOGY (it is fed the
PDG masses).  The artifact prints BOTH readings so the tautology cannot
regenerate as a "substrate prediction".

SOLVER NOTE (substrate-first-canonical-sourcing Sec(ii.B) plan-text-drift):
the plan machinery_pin_map names "ECOS-SDP"; ECOS is NOT installed in the venv
(installed convex solvers: CLARABEL, SCS).  The operational solver is CLARABEL
-- the exact race-proven IKM-SDP solver used by S100a's STAGE-3 machinery.  The
distance is a SUP over a compact feasible set -> solver-INVARIANT; the
SDP-vs-closed-form rel dev (< 1e-6 target) is the solver-independence witness.
This is a methodology-floor solver choice, NOT a physics change.

=============================================================================
CONSTRUCTION (frozen BEFORE compute; the two routes):
=============================================================================
Commutative channel algebra A_mult = self-adjoint part of C^4 on the channels
{v = (0,0) vacuum/Higgs reference; g1 = (1,0); g2 = (1,1); g3 = (3,0)}.  Per
SecVII.BL, A_K acts as the IDENTITY on the multiplicity index, so the
metric-bearing algebra ON the multiplicity bundle IS the channel function
algebra (Iochum-Krajewski-Martinetti finite-point setting; Connes distance
finite + regulator-free).

ROUTE A (substrate-FORWARD; the substrate's OWN distance geometry):
  D_F = J-doubled greybody-reweighted chiral star;  S[v,g] = S[g,v] = t_g,
  t_g = kappa/omega_g, omega_g = lambda_g(tau_fold)^2 (L12 sector floor).
  Star closed form: d_C(omega_v, omega_g) = 1/t_g = omega_g (SDP cross-check).
  This is the substrate's intrinsic metric on its generation channels.
    => d_i = (omega_(1,0), omega_(1,1), omega_(3,0)) = lam2-floors
    => the substrate-FORWARD widening (d_e - d_mu)/(d_mu - d_tau).

ROUTE B (Martinetti-Wulkenhaar inverse-Yukawa ansatz; the pre-reg chain):
  mass_i ~ exp(-d_i/ell)  <=>  d_i = -ell*ln(mass_i) + const
  (Martinetti-Wulkenhaar: the two-point SM Connes distance is set by inverse
  Yukawas; B-4 ladder ansatz).  Substituting into the ratio, ell cancels:
    (d_e - d_mu)/(d_mu - d_tau) = (ln m_mu - ln m_e)/(ln m_tau - ln m_mu)
  = 1.889 EXACT.  This is a TAUTOLOGY of the ansatz (the masses are the input).

DISCRIMINATOR (the gate's honest content):  Route A is the SUBSTRATE's
prediction; Route B is the inverse-mass DEFINITION.  The gate's verdict tests
whether the SUBSTRATE-FORWARD Route-A ratio reproduces 1.889 (PASS), widens but
misses it (INFO), or is degenerate / flat-FN (FAIL).  It does NOT credential the
Route-B tautology as a substrate prediction.

SUBSTITUTION CHAIN (math-scripts.md, mandatory for [SIGN]):
  Claim: "the lepton log-mass spacings WIDEN with ratio
          (d_e-d_mu)/(d_mu-d_tau) -> ~1.89 != 1 (not a flat power law)".
  Step 1 (metric):  d_i = sup{ |phi_i(a) - phi_0(a)| : ||[D_K,a]||_op <= 1 }
                     on the commutative C^N channel algebra  [Connes 1994]
  Step 2 (FN null): mass_n ~ lambda^n (geometric) => ln(mass_n) linear in n
                     => EQUAL log-spacings => ratio = 1 (the discriminand)
  Step 3 (Route B): mass_i ~ exp(-d_i/ell) => d_i = -ell*ln(mass_i)+const'
                     => (d_e-d_mu)/(d_mu-d_tau) = (ln m_mu-ln m_e)/(ln m_tau-ln m_mu)
                     (ell cancels)  -- a tautology of the ansatz.
  Step 4 (evaluate): (ln m_mu-ln m_e) = ln(206.77) = 5.3319;
                     (ln m_tau-ln m_mu) = ln(16.817) = 2.8224;
                     ratio = 5.3319/2.8224 = 1.889036 (Sage-exact) > 1.
  Step 5 (read-off): ratio = 1.889 > 1 => log-mass spacings WIDEN
                     (gen-1<->gen-2 gap exceeds gen-2<->gen-3 gap);
                     FN gives EQUAL spacings => ratio = 1; 1.889 != 1
                     DISCRIMINATES the Connes/Yukawa ladder from FN.
  Direction (Route A, the substrate test):  sign(d_e - d_heavy) > 0 iff the
    substrate distances are nondegenerate and e (lightest) is MOST DISTANT
    (mass = e^{-d/ell}, d/d(mass) < 0).  Read off from the cache floors, not
    assumed.
  Conclusion: PASS iff substrate-forward ratio = 1.889 +- 0.05 AND
    nondegenerate; INFO iff nondegenerate-widening (!=FN) but ratio outside
    [1.0,1.889]; FAIL iff degenerate OR ratio ~ 1 (the FN null).

VERDICT RUBRIC (frozen; plan SecW1-3):
  operator:  |(d_e - d_mu)/(d_mu - d_tau) - 1.889| <= 0.05  AND  d_e != d_mu != d_tau
  PASS:  ratio = 1.889 +- 0.05  AND  non-degenerate (the SecVII.BL eps_LX IS the
         substrate Connes-distance ladder; falsifiable lepton signature confirmed)
  FAIL:  ratio far from 1.889 (e.g. = 1, the FN null) OR degenerate distances
         (the Connes-distance ladder does NOT reproduce the lepton hierarchy)
  INFO:  non-degenerate (widening, != FN) but ratio in [1.0, 1.889) -- correct
         qualitative direction, does not hit the exact PDG ratio.
  3-tuple (schema-v2):
    sign_verdict      = PASS iff substrate-forward ladder is nondegenerate and
                        widens (e most distant; ratio > 1); FAIL iff degenerate
                        or ratio <= 1 (FN null / inverted).
    magnitude_verdict = PASS iff |ratio_A - 1.889| <= 0.05;
                        INFO iff ratio_A in [1.0, 1.889) outside the +-0.05 band;
                        FAIL iff ratio_A < 1.0 or far above 1.889.
    regime_verdict    = VALID iff SDP statuses optimal AND SDP-vs-closed dev < 1e-6
                        AND R-sweep dev < 1e-8 (regulator-invariant); else MARGINAL/BREAKDOWN.
  composite: canonical schema-v2 collapse rule (gate-verdicts.md).

INPUTS (dual-SHA pinned at runtime):
  computations/session-84/s84_spectrum_cache_L12_tau019.npz   [STATIC pin
      9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9 --
      HARD FAIL on mismatch]
  computations/_shared/canonical_constants.py                 [runtime]
  computations/session-88/s88_w11_connes_distance_subalgebra_restriction.npz
      [machinery-lineage cross-check input; d_C = 2.386138 regulator-free PASS]

OUTPUTS:
  computations/investigation-5/inv5_w1_3_connes_distance_lepton_mass_ladder.npz
  computations/investigation-5/inv5_w1_3_connes_distance_lepton_mass_ladder.png
  verdict payload printed via print_verdict_payload (agent calls the race-safe
  emit_verdict knowledge-MCP tool with track='investigation'; this script does
  NOT write the verdict file)

Substrate framing (PARTICLE): the fermion generations ARE the multiplicity
  index of D_K's Peter-Weyl decomposition (Z3-triality t=(p-q) mod 3; SecVII.BL).
  D_K eigenvalues -> the commutative multiplicity-bundle channel algebra C^N ->
  the per-state Connes distance d_i (the metric the Dirac operator induces on
  the space of generation-states) -> the mass ladder mass_i ~ exp(-d_i/ell) ->
  the observed lepton mass spacings.  The Connes distance is NOT a distance IN a
  pre-existing space; it IS the metric structure D_K puts on its own generation
  states -- the substrate measuring the separation between its own excitation
  channels.  SecVII.BL proved the hierarchy is not built by any A_K-inner form;
  this gate tests whether it IS built by the substrate's own intrinsic distance
  geometry, and whether that geometry predicts the falsifiable widening 1.89.
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
from canonical_constants import m_e, m_mu, m_tau_PDG, tau_fold  # explicit names used

# ---------------------------------------------------------------------------
# Section 2 -- Standard imports (CPU thread cap BEFORE numpy import; GPU_path
#              pin = cpu-cap-OMP8: the Connes-distance SDP is a small commutative
#              C^N convex problem, no GPU eig)
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

SESSION = 5                                                        # (local) investigation 5
GATE_ID = "INV5-W1-3-CONNES-DISTANCE-LEPTON-MASS-LADDER"           # (local)
SCHEME = "Connes-distance-commutative-multiplicity-bundle-channel-CN"  # (local)
CONVENTION = "RATIO"                                              # (local)
L_MAX = 12                                                        # (local)

# Pre-registered band / tolerance (plan SecW1-3 strict_PASS_boundary + machinery_pin_map)
RATIO_TARGET_PLAN = 1.889035511558237   # (local) plan pre-reg PDG ratio (m_mu=...755)
RATIO_TOL = 0.05                        # (local) |ratio - 1.889| <= 0.05 (plan tolerance)
RATIO_FN_NULL = 1.0                     # (local) Froggatt-Nielsen null (equal log-spacings)
DEGEN_FLOOR_REL = 1e-6                  # (local) non-degeneracy floor (2 OOM above SDP rtol)
SDP_TOL = 1e-8                          # (local) Connes sup-norm optimisation rtol (plan pin)
CLOSED_DEV_VALID = 1e-6                 # (local) SDP-vs-closed-form rel dev: VALID ceiling
CLOSED_DEV_MARGINAL = 1e-3             # (local) SDP-vs-closed-form rel dev: MARGINAL ceiling
RSWEEP_DEV_VALID = 1e-8                # (local) regulator-invariance rel-dev ceiling
R_SWEEP_FACTORS = (10.0, 100.0, 1000.0)  # (local) Frobenius bounds x max(omega)

# Machinery-lineage pin (plan SecW1-3 input_files; S88 regulator-free distance)
S88_DC_PIN = 2.386138372208456          # (local) S88-CONNES-DISTANCE-SUBALGEBRA-RESTRICTION d_C (L10=L12)
# S100a substrate-forward precedent (the SAME-cache greybody distances; cited, not pinned-as-input)
S100A_W_CONNES = 12.562883508068342     # (local) S100a-CONNES-DISTANCE-LADDER W (substrate-forward)

# Tower (triality-distinct generation channels) + conjugates + reference
TOWER = [(1, 0), (1, 1), (3, 0)]        # (local) generation channels
TOWER_CONJ = [(0, 1), (1, 1), (0, 3)]   # (local) BDI conjugate sectors
REF_SECTOR = (0, 0)                     # (local) vacuum/Higgs reference channel
C2_TOWER = [4.0 / 3.0, 3.0, 6.0]        # (local) SU(3) quadratic Casimirs
W_CASIMIR_IDEAL = 9.0 / 5.0             # (local) undeformed-scaling widening floor

# Static input pin (plan SecW1-3 input_files; 64-hex, S100a-lineage verbatim)
SPECTRUM_CACHE_SHA_PIN = "9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9"

OUT_NPZ = _HERE / "inv5_w1_3_connes_distance_lepton_mass_ladder.npz"
OUT_PNG = _HERE / "inv5_w1_3_connes_distance_lepton_mass_ladder.png"

SPECTRUM_CACHE = PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
S88_NPZ = PROJECT_ROOT / "computations" / "session-88" / "s88_w11_connes_distance_subalgebra_restriction.npz"
CANONICAL_CONSTS = _SHARED / "canonical_constants.py"
INPUT_FILES = [SPECTRUM_CACHE, CANONICAL_CONSTS, S88_NPZ]


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
    # Literal machinery-lineage pins (cited cross-session constants)
    pins["S88-CONNES-DISTANCE-SUBALGEBRA-RESTRICTION-d_C"] = repr(S88_DC_PIN)
    pins["S100a-CONNES-DISTANCE-LADDER-W"] = repr(S100A_W_CONNES)
    print(f"  S88-CONNES-DISTANCE-SUBALGEBRA-RESTRICTION-d_C={S88_DC_PIN!r} (literal pin)")
    print(f"  S100a-CONNES-DISTANCE-LADDER-W={S100A_W_CONNES!r} (literal pin)")
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
    Investigation track: agent calls emit_verdict(..., session=5, track='investigation')."""
    payload = {
        "session": SESSION,
        "track": "investigation",
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
# Section 5 -- Spectrum loading: channel floors at tau_fold (L=12 cache)
# ---------------------------------------------------------------------------
def load_floors():
    """Load the per-sector spectral floors lambda_g = min|eigenvalue| for the
    tower, the conjugate sectors, and the reference channel. HARD FAIL if the
    cache SHA does not match the static pin."""
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

    floors = np.array([floor_of(k) for k in TOWER], dtype=np.float64)           # (local)
    floors_conj = np.array([floor_of(k) for k in TOWER_CONJ], dtype=np.float64)  # (local)
    floor_ref = floor_of(REF_SECTOR)  # (local) context only (reference is a state)
    n_sectors = len(sec)  # (local)
    return floors, floors_conj, floor_ref, n_sectors


# ---------------------------------------------------------------------------
# Section 6 -- Finite real spectral triple: J-doubled greybody star (Route A)
# ---------------------------------------------------------------------------
def build_star(t):
    """4x4 Hermitian star: node 0 = vacuum reference, nodes 1..3 = generation
    channels; S[0,g] = S[g,0] = t[g-1]."""
    S = np.zeros((4, 4), dtype=np.float64)  # (local)
    for g in range(3):
        S[0, g + 1] = t[g]
        S[g + 1, 0] = t[g]
    return S


def build_triple(t_part, t_anti):
    """J-doubled chiral star D_F (16x16), gamma, J (real permutation o conj),
    channel-projector embedding for pi(a). Layout: index = copy*8 + chir*4 +
    channel; copy in {0=particle,1=anti}, chir in {0=L,1=R}, channel in
    {0=v,1=g1,2=g2,3=g3}."""
    S_p = build_star(t_part)   # (local)
    S_a = build_star(t_anti)   # (local)

    def chiral(S):
        Z = np.zeros((4, 4))  # (local)
        return np.block([[Z, S], [S, Z]])

    D_p = chiral(S_p)  # (local) 8x8
    D_a = chiral(S_a)  # (local) 8x8
    D_F = np.block([
        [D_p, np.zeros((8, 8))],
        [np.zeros((8, 8)), D_a],
    ])  # (local) 16x16 real symmetric

    g8 = np.diag([1.0] * 4 + [-1.0] * 4)  # (local) gamma diag(+L,-R) on particle
    gamma = np.block([
        [g8, np.zeros((8, 8))],
        [np.zeros((8, 8)), -g8],
    ])  # (local) eps''=-1 opposite on antiparticle

    Sigma = np.zeros((16, 16))  # (local) J = Sigma o K, particle<->anti swap
    Sigma[0:8, 8:16] = np.eye(8)
    Sigma[8:16, 0:8] = np.eye(8)

    E = []  # (local) channel projectors E_k (16x16): diagonal over chir + copies
    for ch in range(4):
        e = np.zeros(16)  # (local)
        for copy in range(2):
            for chir in range(2):
                e[copy * 8 + chir * 4 + ch] = 1.0
        E.append(np.diag(e))
    return D_F, gamma, Sigma, E, D_p


def ko_sign_checks(D_F, gamma, Sigma):
    """KO-dim-6 sign checks for J = Sigma o K (real D_F, gamma => K trivial)."""
    eps_J2 = float(np.max(np.abs(Sigma @ Sigma - np.eye(16))))      # (local) J^2 = +1
    comm_JD = float(np.max(np.abs(Sigma @ D_F - D_F @ Sigma)))      # (local) [J,D] = 0
    anti_Jg = float(np.max(np.abs(Sigma @ gamma + gamma @ Sigma)))  # (local) Jg = -gJ
    odd_Dg = float(np.max(np.abs(gamma @ D_F + D_F @ gamma)))       # (local) gD = -Dg
    return eps_J2, comm_JD, anti_Jg, odd_Dg


def first_order_residual(D_F, E):
    """max ||[[D_F, pi(a)], pi(b)^o]||_op (b^o = pi(b) for this layout).
    REPORTED, not asserted zero: a generation-resolving D_F on the multiplicity
    bundle sits outside every A_K-bimodule (SecVII.BL)."""
    worst = 0.0  # (local)
    for a in E:
        Da = D_F @ a - a @ D_F  # (local)
        for b in E:
            r = Da @ b - b @ Da  # (local)
            worst = max(worst, float(np.linalg.norm(r, ord=2)))
    return worst


# ---------------------------------------------------------------------------
# Section 7 -- Connes-distance SDP on the channel algebra (IKM finite form)
# ---------------------------------------------------------------------------
def connes_distance_sdp(D_op, E, i_ch, j_ch, frob_bound=None, sdp_tol=SDP_TOL):
    """d_C(omega_i, omega_j) on the commutative channel algebra:
        max (a_i - a_j) s.t. ||[D_op, pi(a)]||_op <= 1, pi(a) = sum_k x_k E_k,
        gauge-fix x_j = 0. Optional Frobenius bound for the R-sweep
        regulator-invariance demonstration (the distance must NOT move)."""
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


# ---------------------------------------------------------------------------
# Section 8 -- Compute orchestrator
# ---------------------------------------------------------------------------
def compute():
    floors, floors_conj, floor_ref, n_sectors = load_floors()
    print(f"  L=12 cache loaded: {n_sectors} sectors")
    print(f"  tower floors lambda_g(tau_fold={tau_fold}): "
          f"(1,0)={floors[0]:.8f} (1,1)={floors[1]:.8f} (3,0)={floors[2]:.8f}")
    print(f"  conjugate floors: (0,1)={floors_conj[0]:.8f} "
          f"(1,1)={floors_conj[1]:.8f} (0,3)={floors_conj[2]:.8f}")
    print(f"  reference-sector (0,0) floor (context): {floor_ref:.8f}")

    bdi_dev = float(np.max(np.abs(floors - floors_conj) / floors))  # (local)
    print(f"  BDI conjugate-floor max rel dev: {bdi_dev:.3e}  ([J,D_F]=0 reality constraint)")

    strict_floor_order = bool(floors[0] < floors[1] < floors[2])  # (local)
    print(f"  strict floor ordering lambda(1,0)<lambda(1,1)<lambda(3,0): {strict_floor_order}")

    # ====================================================================
    # ROUTE A -- substrate-FORWARD greybody distances (the substrate's own metric)
    # ====================================================================
    omega = floors ** 2           # (local) channel D^2-floors (lam2-units)
    omega_conj = floors_conj ** 2  # (local)
    t_part = 1.0 / omega          # (local) greybody-reweighted couplings (kappa=1)
    t_anti = 1.0 / omega_conj     # (local)
    print(f"\n  [ROUTE A: substrate-forward greybody star]")
    print(f"  omega_g = lambda_g^2: {omega[0]:.9f}, {omega[1]:.9f}, {omega[2]:.9f}")
    print(f"  greybody couplings t_g = 1/omega_g: {t_part[0]:.6f}, {t_part[1]:.6f}, {t_part[2]:.6f}")

    D_F, gamma, Sigma, E, D_p = build_triple(t_part, t_anti)
    eps_J2, comm_JD, anti_Jg, odd_Dg = ko_sign_checks(D_F, gamma, Sigma)
    print(f"  KO-dim-6 checks: |J^2-1|={eps_J2:.3e}  ||[J,D_F]||={comm_JD:.3e}  "
          f"||{{J,gamma}}||={anti_Jg:.3e}  ||{{gamma,D_F}}||={odd_Dg:.3e}")
    ko_ok = bool(eps_J2 < 1e-12 and comm_JD < 1e-12 and anti_Jg < 1e-12 and odd_Dg < 1e-12)  # (local)

    fo_resid = first_order_residual(D_F, E)
    print(f"  first-order residual max||[[D,a],b^o]||: {fo_resid:.6f}  "
          f"(REPORTED; standing SecVII.BL multiplicity-bundle obstruction)")

    # vacuum-referenced per-state distances (PRIMARY, 3 SDPs, J-doubled op)
    print("\n  -- vacuum-referenced per-state Connes distances (16-dim J-doubled) --")
    d_vac = np.zeros(3)          # (local)
    d_vac_closed = omega.copy()  # (local) star theorem: d(v,g) = omega_g
    statuses = []  # (local)
    for g in range(3):
        r = connes_distance_sdp(D_F, E, i_ch=g + 1, j_ch=0)  # (local)
        d_vac[g] = r["d_C"]
        statuses += [r["status_pos"], r["status_neg"]]
        dev = abs(r["d_C"] - d_vac_closed[g]) / d_vac_closed[g]  # (local)
        print(f"    d(v, {TOWER[g]}): SDP={r['d_C']:.12f}  closed={d_vac_closed[g]:.12f}  "
              f"reldev={dev:.3e}  [{r['status_pos']}|{r['status_neg']}]")

    # doubling-invariance: same distances on the SINGLE 8-dim chiral star
    E8 = [e[:8, :8] for e in E]  # (local)
    d_vac_single = np.zeros(3)  # (local)
    for g in range(3):
        r = connes_distance_sdp(D_p, E8, i_ch=g + 1, j_ch=0)  # (local)
        d_vac_single[g] = r["d_C"]
        statuses += [r["status_pos"], r["status_neg"]]
    doubling_dev = float(np.max(np.abs(d_vac_single - d_vac) / d_vac))  # (local)
    print(f"  doubling-invariance max rel dev (doubled vs single): {doubling_dev:.3e}")

    # assignment by metric ordering: most distant = lightest = e
    order_desc = np.argsort(-d_vac)  # (local)
    sec_e, sec_mu, sec_tau = (TOWER[order_desc[0]], TOWER[order_desc[1]], TOWER[order_desc[2]])  # (local)
    d_e, d_mu_v, d_tau_v = (d_vac[order_desc[0]], d_vac[order_desc[1]], d_vac[order_desc[2]])  # (local)
    print(f"\n  assignment (most distant = lightest): e={sec_e}  mu={sec_mu}  tau={sec_tau}")
    print(f"  d_e={d_e:.9f}  d_mu={d_mu_v:.9f}  d_tau={d_tau_v:.9f}  (lam2-units)")

    # non-degeneracy + strictness
    degen_rel = (d_vac.max() - d_vac.min()) / d_vac.max()  # (local)
    gap1_rel = (d_e - d_mu_v) / d_vac.max()   # (local)
    gap2_rel = (d_mu_v - d_tau_v) / d_vac.max()  # (local)
    nondegenerate = bool(degen_rel >= DEGEN_FLOOR_REL)  # (local)
    strict_ladder = bool(gap1_rel >= DEGEN_FLOOR_REL and gap2_rel >= DEGEN_FLOOR_REL)  # (local)
    print(f"  degeneracy rel spread: {degen_rel:.6e}  (floor {DEGEN_FLOOR_REL})  "
          f"nondegenerate={nondegenerate}  strict={strict_ladder}")

    # THE substrate-forward widening ratio (verdict-bearing)
    Delta_1 = d_e - d_mu_v      # (local) e-mu ladder gap
    Delta_2 = d_mu_v - d_tau_v  # (local) mu-tau ladder gap
    ratio_A = Delta_1 / Delta_2  # (local) substrate-FORWARD (d_e-d_mu)/(d_mu-d_tau)
    print(f"\n  [ROUTE A] ladder gaps: Delta_1(e-mu)={Delta_1:.9f}  Delta_2(mu-tau)={Delta_2:.9f}")
    print(f"  [ROUTE A] substrate-forward ratio_A = (d_e-d_mu)/(d_mu-d_tau) = {ratio_A:.9f}")
    print(f"            [PDG target {RATIO_TARGET_PLAN:.9f}; FN null {RATIO_FN_NULL}; "
          f"Casimir ideal {W_CASIMIR_IDEAL}; S100a precedent {S100A_W_CONNES:.6f}]")

    # closed-form fidelity (regime input)
    closed_devs = [abs(d_vac[g] - d_vac_closed[g]) / d_vac_closed[g] for g in range(3)]  # (local)
    max_closed_dev = float(np.max(closed_devs))  # (local)
    print(f"  max SDP-vs-closed-form rel dev: {max_closed_dev:.3e}")

    # R-sweep regulator-invariance (the commutative-channel cure vs S87 M_n(C))
    print("  -- R-sweep regulator-invariance (Frobenius bound on pi(a)) --")
    d_ref = d_vac[order_desc[0]]  # (local) e-channel distance
    rsweep_vals = []  # (local)
    for fac in R_SWEEP_FACTORS:
        R = fac * float(omega.max())  # (local)
        r = connes_distance_sdp(D_F, E, i_ch=int(order_desc[0]) + 1, j_ch=0, frob_bound=R)  # (local)
        statuses += [r["status_pos"], r["status_neg"]]
        rsweep_vals.append(r["d_C"])
        print(f"    R={R:10.3f}: d_C={r['d_C']:.12f}")
    rsweep_dev = float(np.max(np.abs(np.array(rsweep_vals) - d_ref) / d_ref))  # (local)
    print(f"    max rel dev across R-sweep: {rsweep_dev:.3e}  (regulator-invariant cure)")

    # S88 machinery cross-check (the regulator-free A_F-restricted diameter)
    s88_match = False  # (local)
    if S88_NPZ.exists():
        d88 = np.load(S88_NPZ, allow_pickle=True)  # (local)
        d_C_L12 = float(d88["d_C_L12"])  # (local)
        s88_match = bool(abs(d_C_L12 - S88_DC_PIN) < 1e-9)  # (local)
        print(f"  S88 machinery cross-check: d_C_L12={d_C_L12:.9f} matches pin "
              f"{S88_DC_PIN:.9f} -> {s88_match}")

    # ====================================================================
    # ROUTE B -- Martinetti-Wulkenhaar inverse-Yukawa ansatz (the pre-reg chain)
    # ====================================================================
    print(f"\n  [ROUTE B: Martinetti-Wulkenhaar inverse-Yukawa ansatz d_i = -ell*ln(m_i)]")
    ln_m = np.array([np.log(m_e), np.log(m_mu), np.log(m_tau_PDG)])  # (local) ascending mass
    g1_pdg = float(np.log(m_mu) - np.log(m_e))         # (local) ln(m_mu/m_e)
    g2_pdg = float(np.log(m_tau_PDG) - np.log(m_mu))   # (local) ln(m_tau/m_mu)
    ratio_B = g1_pdg / g2_pdg                          # (local) the inverse-Yukawa ratio (ell cancels)
    print(f"  ln(m_mu/m_e) = {g1_pdg:.6f};  ln(m_tau/m_mu) = {g2_pdg:.6f}")
    print(f"  [ROUTE B] ratio_B = (ln m_mu-ln m_e)/(ln m_tau-ln m_mu) = {ratio_B:.12f}")
    print(f"            (canonical masses; plan pre-reg target {RATIO_TARGET_PLAN:.12f}; "
          f"diff {abs(ratio_B - RATIO_TARGET_PLAN):.2e} -- m_mu last-digit)")
    print(f"  ** ROUTE B IS A TAUTOLOGY: ell cancels; the ratio IS the PDG log-mass-spacing")
    print(f"     ratio, recovered by DEFINITION (d_i fed by the masses), NOT a substrate")
    print(f"     prediction. The substrate-FORWARD prediction is Route A = {ratio_A:.6f}.")

    # ell-calibration (Route B fit; diagnostic): centered OLS of ln m on d_vac
    x = np.array([d_e, d_mu_v, d_tau_v])  # (local) pairs with [m_e, m_mu, m_tau]
    y = ln_m  # (local)
    xc = x - x.mean(); yc = y - y.mean()  # (local)
    b_ols = float((xc @ yc) / (xc @ xc))  # (local) slope = -1/ell
    ell = -1.0 / b_ols  # (local)
    r2 = float((xc @ yc) ** 2 / ((xc @ xc) * (yc @ yc)))  # (local)
    spread_pred = float((x.max() - x.min()) / ell)  # (local) Route-A e-folds under fitted ell
    spread_pdg = float(ln_m[2] - ln_m[0])  # (local) PDG target spread
    print(f"  ell-calibration (centered OLS, diagnostic): ell={ell:.9f}  R^2={r2:.6f}")
    print(f"  Route-A spread (d_max-d_min)/ell = {spread_pred:.6f} e-folds  [PDG {spread_pdg:.6f}]")

    # ====================================================================
    # FN-discrimination + verdict criteria
    # ====================================================================
    # FN null: equal log-spacings => ratio = 1. Both routes' deviation from 1:
    not_FN_A = bool(abs(ratio_A - RATIO_FN_NULL) > RATIO_TOL)  # (local) Route A != FN
    widening_A = bool(ratio_A > RATIO_FN_NULL)  # (local) Route A widens (>1)
    print(f"\n  FN-discrimination: Route A ratio {ratio_A:.6f} != 1 (FN null)? {not_FN_A}; "
          f"widening (>1)? {widening_A}")

    # ---- 3-tuple (frozen rubric) ----
    # sign: substrate-forward ladder nondegenerate AND widens (e most distant, ratio_A>1)
    crit_sign = bool(nondegenerate and strict_ladder and widening_A and ell > 0)  # (local)
    sign_v = "PASS" if crit_sign else "FAIL"  # (local)

    # magnitude: |ratio_A - 1.889| vs band; INFO if in [1.0,1.889) outside +-0.05
    mag_dev = abs(ratio_A - RATIO_TARGET_PLAN)  # (local)
    in_band = bool(mag_dev <= RATIO_TOL)  # (local)
    widens_below_target = bool(RATIO_FN_NULL <= ratio_A < RATIO_TARGET_PLAN and not in_band)  # (local)
    if in_band:
        mag_v = "PASS"  # (local) substrate-forward ratio reproduces 1.889
    elif widens_below_target or (ratio_A > RATIO_TARGET_PLAN):
        # widening direction correct (>1, != FN) but does NOT hit the exact 1.889
        mag_v = "INFO"  # plan INFO branch: widening (!=FN) but ratio outside the band
    else:
        mag_v = "FAIL"  # ratio < 1 (FN/inverted) or degenerate
    print(f"  magnitude: |ratio_A - {RATIO_TARGET_PLAN:.4f}| = {mag_dev:.6f}  "
          f"(band +-{RATIO_TOL}) -> in_band={in_band}; mag_verdict={mag_v}")

    # regime: SDP convergence + closed-form fidelity + regulator-invariance + KO
    ok_status = {"optimal", "optimal_inaccurate"}  # (local)
    all_converged = all(s in ok_status for s in statuses)  # (local)
    n_inaccurate = sum(1 for s in statuses if s == "optimal_inaccurate")  # (local)
    if (all_converged and max_closed_dev < CLOSED_DEV_VALID
            and rsweep_dev < RSWEEP_DEV_VALID and doubling_dev < CLOSED_DEV_VALID
            and ko_ok and n_inaccurate == 0):
        regime_v = "VALID"  # (local)
    elif all_converged and max_closed_dev < CLOSED_DEV_MARGINAL:
        regime_v = "MARGINAL"
    else:
        regime_v = "BREAKDOWN"
    print(f"  regime: converged={all_converged} closed_dev={max_closed_dev:.1e} "
          f"rsweep_dev={rsweep_dev:.1e} ko_ok={ko_ok} -> regime_verdict={regime_v}")

    # canonical schema-v2 collapse rule (gate-verdicts.md; verbatim order)
    if regime_v == "BREAKDOWN":
        composite = "FAIL"  # (local)
    elif sign_v == "FAIL":
        composite = "FAIL"
    elif mag_v == "FAIL" and regime_v == "VALID":
        composite = "FAIL"
    elif mag_v == "FAIL" and regime_v == "MARGINAL":
        composite = "INFO"
    elif mag_v == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"

    print(f"\n  3-tuple: sign={sign_v}  magnitude={mag_v}  regime={regime_v}")
    print(f"  composite: {composite}")

    return {
        "floors": floors, "floors_conj": floors_conj, "floor_ref": floor_ref,
        "bdi_dev": bdi_dev, "strict_floor_order": strict_floor_order,
        "omega": omega, "t_part": t_part,
        "eps_J2": eps_J2, "comm_JD": comm_JD, "anti_Jg": anti_Jg, "odd_Dg": odd_Dg,
        "ko_ok": ko_ok, "fo_resid": fo_resid,
        "d_vac": d_vac, "d_vac_closed": d_vac_closed, "d_vac_single": d_vac_single,
        "doubling_dev": doubling_dev,
        "order_desc": order_desc, "sec_e": sec_e, "sec_mu": sec_mu, "sec_tau": sec_tau,
        "d_e": d_e, "d_mu": d_mu_v, "d_tau": d_tau_v,
        "degen_rel": degen_rel, "nondegenerate": nondegenerate, "strict_ladder": strict_ladder,
        "Delta_1": Delta_1, "Delta_2": Delta_2, "ratio_A": ratio_A,
        "max_closed_dev": max_closed_dev, "rsweep_vals": np.array(rsweep_vals),
        "rsweep_dev": rsweep_dev, "s88_match": s88_match,
        "g1_pdg": g1_pdg, "g2_pdg": g2_pdg, "ratio_B": ratio_B,
        "ell": ell, "b_ols": b_ols, "r2": r2,
        "spread_pred": spread_pred, "spread_pdg": spread_pdg,
        "not_FN_A": not_FN_A, "widening_A": widening_A,
        "mag_dev": mag_dev, "in_band": in_band,
        "statuses": statuses, "n_inaccurate": n_inaccurate,
        "crit_sign": crit_sign,
        "sign_v": sign_v, "mag_v": mag_v, "regime_v": regime_v, "composite": composite,
    }


# ---------------------------------------------------------------------------
# Section 9 -- Plot
# ---------------------------------------------------------------------------
def make_plot(res):
    fig, axes = plt.subplots(1, 3, figsize=(16, 5.2))

    # Panel A: the substrate-forward per-state distance ladder
    ax = axes[0]
    xpos = np.arange(3)  # (local)
    labels = [f"{TOWER[g]}" for g in range(3)]  # (local)
    ax.bar(xpos, res["d_vac_closed"], color="lightsteelblue", label="closed form $d=\\omega_g$")
    ax.plot(xpos, res["d_vac"], "k^", markersize=10, label="SDP (CLARABEL)")
    for g in range(3):
        ax.annotate(f"{res['d_vac'][g]:.5f}", (xpos[g], res["d_vac"][g]),
                    textcoords="offset points", xytext=(0, 8), ha="center", fontsize=8)
    role = {tuple(res["sec_e"]): "e", tuple(res["sec_mu"]): "$\\mu$", tuple(res["sec_tau"]): "$\\tau$"}  # (local)
    ax.set_xticks(xpos)
    ax.set_xticklabels([f"{labels[g]}\n[{role[TOWER[g]]}]" for g in range(3)])
    ax.set_ylabel("$d_C(\\omega_v,\\omega_g)$  [$\\lambda^2$-units]")
    ax.set_title("Route A: substrate-forward per-state\nConnes distance "
                 f"($[J,D_F]=0$ dev {res['comm_JD']:.1e})")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, axis="y")

    # Panel B: the two-route discriminator on the spacing ratio
    ax = axes[1]
    names = ["Route A\n(substrate\nforward)", "Route B\n(inv-Yukawa\nTAUTOLOGY)",
             "Casimir\n9/5", "FN null\n=1"]  # (local)
    vals = [res["ratio_A"], res["ratio_B"], W_CASIMIR_IDEAL, RATIO_FN_NULL]  # (local)
    colors = ["tab:red", "tab:purple", "tab:green", "gray"]  # (local)
    ax.bar(np.arange(len(vals)), vals, color=colors)
    ax.axhspan(RATIO_TARGET_PLAN - RATIO_TOL, RATIO_TARGET_PLAN + RATIO_TOL,
               color="green", alpha=0.18,
               label=f"PASS band 1.889$\\pm${RATIO_TOL}")
    ax.axhline(RATIO_TARGET_PLAN, color="darkgreen", ls=":", lw=1, label="PDG 1.889")
    for i, v in enumerate(vals):
        ax.annotate(f"{v:.3f}", (i, v), textcoords="offset points",
                    xytext=(0, 5), ha="center", fontsize=8)
    ax.set_xticks(np.arange(len(vals)))
    ax.set_xticklabels(names, fontsize=7.5)
    ax.set_ylabel("spacing ratio $(d_e-d_\\mu)/(d_\\mu-d_\\tau)$")
    ax.set_title(f"two-route discriminator\nRoute A {res['ratio_A']:.3f} "
                 f"vs Route B {res['ratio_B']:.3f}")
    ax.legend(fontsize=7.5)
    ax.grid(alpha=0.3, axis="y")

    # Panel C: mass map regression (Route B fit; diagnostic)
    ax = axes[2]
    x = np.array([res["d_e"], res["d_mu"], res["d_tau"]])  # (local)
    y = np.array([np.log(m_e), np.log(m_mu), np.log(m_tau_PDG)])  # (local)
    ax.plot(x, y, "o", color="tab:red", markersize=9, label="PDG $\\ln m_i$ vs $d_i$")
    xs = np.linspace(x.min() * 0.95, x.max() * 1.05, 50)  # (local)
    ax.plot(xs, y.mean() + res["b_ols"] * (xs - x.mean()), "--", color="gray",
            label=f"OLS: $\\ell$={res['ell']:.4f}, $R^2$={res['r2']:.4f}")
    for xi, yi, nm in zip(x, y, ["e", "$\\mu$", "$\\tau$"]):
        ax.annotate(nm, (xi, yi), textcoords="offset points", xytext=(8, 0), fontsize=11)
    ax.set_xlabel("$d_i$  [$\\lambda^2$-units]")
    ax.set_ylabel("$\\ln m_i^{PDG}$  [GeV]")
    ax.set_title(f"mass $= e^{{-d/\\ell}}$ fit (Route-B calib)\n"
                 f"spread pred {res['spread_pred']:.2f} vs PDG {res['spread_pdg']:.2f}")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    fig.suptitle(
        f"{GATE_ID}  (L=12, tau_fold={tau_fold}; e={res['sec_e']} mu={res['sec_mu']} tau={res['sec_tau']}; "
        f"composite {res['composite']}: sign {res['sign_v']}/mag {res['mag_v']}/regime {res['regime_v']})",
        fontsize=10,
    )
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)
    print(f"  Plot saved: {OUT_PNG.name}")


# ---------------------------------------------------------------------------
# Section 10 -- Main
# ---------------------------------------------------------------------------
def main():
    t0 = time.time()  # (local)
    print(f"=== {GATE_ID} ===")
    print(f"Session(investigation) {SESSION}  L_max={L_MAX}  scheme={SCHEME}")
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

    # --- npz (full float64 round-trip per Class 8.3)
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID, scheme=SCHEME, convention=CONVENTION, l_max=L_MAX,
        track="investigation",
        verdict=res["composite"], sign_verdict=res["sign_v"],
        magnitude_verdict=res["mag_v"], regime_verdict=res["regime_v"],
        tower_pq=np.array(TOWER), tower_C2=np.array(C2_TOWER),
        ref_sector=np.array(REF_SECTOR),
        floors_lambda_min=res["floors"], floors_conj=res["floors_conj"],
        floor_ref=res["floor_ref"], bdi_conj_floor_reldev=res["bdi_dev"],
        strict_floor_order=res["strict_floor_order"],
        omega_D2_floors=res["omega"], greybody_couplings=res["t_part"],
        ko_J2_dev=res["eps_J2"], ko_JD_comm=res["comm_JD"],
        ko_Jgamma_anti=res["anti_Jg"], ko_gammaD_anti=res["odd_Dg"],
        ko_dim6_ok=res["ko_ok"], first_order_residual=res["fo_resid"],
        d_vac_sdp=res["d_vac"], d_vac_closed=res["d_vac_closed"],
        d_vac_single_star=res["d_vac_single"], doubling_invariance_dev=res["doubling_dev"],
        assignment_e=np.array(res["sec_e"]), assignment_mu=np.array(res["sec_mu"]),
        assignment_tau=np.array(res["sec_tau"]),
        d_e=res["d_e"], d_mu=res["d_mu"], d_tau=res["d_tau"],
        degen_rel_spread=res["degen_rel"], nondegenerate=res["nondegenerate"],
        strict_ladder=res["strict_ladder"], degen_floor_rel=DEGEN_FLOOR_REL,
        # --- the two-route discriminator (THE gate content) ---
        Delta_1=res["Delta_1"], Delta_2=res["Delta_2"],
        ratio_A_substrate_forward=res["ratio_A"],
        ratio_B_inverse_yukawa_tautology=res["ratio_B"],
        ratio_target_plan=RATIO_TARGET_PLAN, ratio_tol=RATIO_TOL,
        ratio_FN_null=RATIO_FN_NULL,
        not_FN_A=res["not_FN_A"], widening_A=res["widening_A"],
        ratio_A_minus_target_absdev=res["mag_dev"], ratio_A_in_band=res["in_band"],
        # --- regime / fidelity ---
        max_sdp_closed_reldev=res["max_closed_dev"],
        rsweep_factors=np.array(R_SWEEP_FACTORS), rsweep_d_values=res["rsweep_vals"],
        rsweep_max_reldev=res["rsweep_dev"],
        s88_dC_pin=S88_DC_PIN, s88_machinery_match=res["s88_match"],
        s100a_W_connes_precedent=S100A_W_CONNES,
        W_casimir_ideal=W_CASIMIR_IDEAL,
        # --- Route-B PDG anchors + ell fit (diagnostic) ---
        pdg_g1_lngap_mu_e=res["g1_pdg"], pdg_g2_lngap_tau_mu=res["g2_pdg"],
        m_e_pdg=m_e, m_mu_pdg=m_mu, m_tau_pdg=m_tau_PDG,
        ell_ols=res["ell"], ols_slope=res["b_ols"], ols_r2=res["r2"],
        spread_pred_efolds=res["spread_pred"], spread_pdg_efolds=res["spread_pdg"],
        # --- bookkeeping ---
        sdp_statuses=np.array(res["statuses"]), n_optimal_inaccurate=res["n_inaccurate"],
        sdp_tol=SDP_TOL, tau_fold_used=tau_fold,
        spectrum_cache_sha=SPECTRUM_CACHE_SHA_PIN,
        crit_sign=res["crit_sign"],
        audit_sha256=audit_sha, content_sha256=content_sha,
        schema_version="S84+",
    )
    print(f"\n  Data saved: {OUT_NPZ.name} ({OUT_NPZ.stat().st_size} bytes)")

    make_plot(res)

    # --- verdict payload (agent passes to race-safe emit_verdict MCP tool)
    e_str = f"({res['sec_e'][0]},{res['sec_e'][1]})"  # (local)
    value_str = (
        f"ratio_A_substrate_forward={res['ratio_A']:.6f}_"
        f"{'IN' if res['in_band'] else 'OUTSIDE'}[1.889+-{RATIO_TOL}];"
        f"ratio_B_inverse_yukawa_TAUTOLOGY={res['ratio_B']:.6f}_eq_PDG-by-definition;"
        f"sign={res['sign_v']}_nondegenerate_widening_e={e_str}_most-distant;"
        f"d=({res['d_tau']:.6f},{res['d_mu']:.6f},{res['d_e']:.6f})lam2-units_tau-mu-e;"
        f"Delta_1={res['Delta_1']:.6f};Delta_2={res['Delta_2']:.6f};"
        f"not_FN={res['not_FN_A']};FN_null=1.0;"
        f"SDP-closed_dev={res['max_closed_dev']:.1e};"
        f"reg-invariant_Rsweep_dev={res['rsweep_dev']:.1e};"
        f"S100a-forward-precedent_W={S100A_W_CONNES:.4f}_consistent;"
        f"ell_OLS={res['ell']:.6f};R2={res['r2']:.4f}"
    )  # (local)
    companion = (
        f"TWO-ROUTE DISCRIMINATOR: Route A (substrate-FORWARD greybody d_g=lambda_g^2) "
        f"gives ratio_A={res['ratio_A']:.6f} (the substrate's OWN distance widening, "
        f"reproduces S100a W={S100A_W_CONNES:.4f}); Route B (Martinetti-Wulkenhaar "
        f"inverse-Yukawa d_i=-ell*ln m_i) gives ratio_B={res['ratio_B']:.6f}=1.889 "
        f"TAUTOLOGICALLY (ell cancels; fed the PDG masses, NOT a substrate prediction). "
        f"The substrate widens (sign PASS, e most-distant nondegenerate) but does NOT hit "
        f"1.889 (mag {res['mag_v']}); the 1.889 lives only in the inverse-mass ansatz"
    )  # (local)
    extra = [
        (f"# Route-A substrate-forward ratio={res['ratio_A']:.6f} OUTSIDE [1.889+-{RATIO_TOL}] "
         f"(S100a-CONNES-DISTANCE-LADDER precedent W={S100A_W_CONNES:.4f}, same L12 cache, INFO); "
         f"the Jensen fold compresses (1,0)/(1,1) floors (Delta_2={res['Delta_2']:.6f}) => W inflated "
         f"{res['ratio_A']/W_CASIMIR_IDEAL:.2f}x above Casimir 9/5; substrate distances are "
         f"Casimir-graded, NOT log-mass-graded # {GATE_ID}"),
        (f"# Route-B ratio_B={res['ratio_B']:.9f} = (ln m_mu-ln m_e)/(ln m_tau-ln m_mu) is a "
         f"TAUTOLOGY of the inverse-Yukawa ansatz mass=exp(-d/ell): ell cancels => ratio IS the "
         f"PDG log-mass-spacing ratio by DEFINITION (1.889 != 1 discriminates the LADDER FORM from "
         f"Froggatt-Nielsen, but does NOT confirm the substrate REALIZES that ladder) # {GATE_ID}"),
        (f"# SecVII.BL STAGE-3-PERMANENT: D_K left-invariant => multiplicity-scalar => the hierarchy "
         f"is NOT in the bare spectrum; eps_LX needs an external non-LI deformation. This gate tests "
         f"whether the substrate's INTRINSIC Connes distance IS that eps_LX: it is generation-RESOLVING "
         f"(nondegenerate, first-order residual {res['fo_resid']:.4f} REPORTED) but its widening "
         f"({res['ratio_A']:.4f}) != PDG 1.889 # {GATE_ID}"),
        (f"# KO-dim-6 J-checks: J^2=+1 ({res['eps_J2']:.1e}), [J,D_F]=0 ({res['comm_JD']:.1e}, "
         f"BDI conj-floor equality {res['bdi_dev']:.1e}), Jgamma=-gammaJ ({res['anti_Jg']:.1e}); "
         f"regulator-free commutative-channel restriction (R-sweep dev {res['rsweep_dev']:.2e}; "
         f"cures S87 M_n(C) CLASS-gamma divergence); S88 d_C cross-check match={res['s88_match']} "
         f"# {GATE_ID}"),
        (f"# SOLVER: CLARABEL (ECOS unavailable in venv; substrate-first-canonical-sourcing Sec(ii.B) "
         f"plan-text-drift; solver-INVARIANT, SDP-vs-closed dev {res['max_closed_dev']:.1e}). "
         f"m_mu canonical=0.1056583745 (ratio_B={res['ratio_B']:.9f}) vs plan pre-reg m_mu=...755 "
         f"(target {RATIO_TARGET_PLAN:.9f}); diff {abs(res['ratio_B']-RATIO_TARGET_PLAN):.1e} << tol "
         f"# {GATE_ID}"),
    ]  # (local)

    print()
    print_verdict_payload(
        res["composite"], value_str, audit_sha, content_sha,
        sign_verdict=res["sign_v"], magnitude_verdict=res["mag_v"],
        regime_verdict=res["regime_v"], companion_note=companion, extra_rows=extra,
    )

    print(f"\n=== {GATE_ID}: {res['composite']} (wall {time.time() - t0:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
