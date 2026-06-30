#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
S100b-NONABELIAN-METRIC-FRACTION
================================================================================
Gate:   S100b-NONABELIAN-METRIC-FRACTION   (trigger [VERIFY], classification GEOMETRIC)
Agent:  berry-geometric-phase-theorist
Plan:   sessions/session-plan/session-100b-plan-w6.md  ## SECTION W6-2
WP:     sessions/session-100b/session-100b-w6-workingpaper.md  ### SECTION W6-2

SLOT LAW (plan W6-2): structural confirmation on the VII.AF.1.OP-PROJ bridge
object (quantum METRIC = Re QGT), NOT VII.W. The framework's Berry CURVATURE
vanishes identically on SU(3) (Im QGT = 0, max|Omega| < 4e-14, 12 zero
invariants; S25/S61/S96). The Chen-Karki-Hosur regime -- Tr R != 0 while
Chern = 0, metrically rich / topologically trivial -- IS the substrate's
regime; this gate verifies the substrate realizes it on its own degenerate
fiber: Tr R != Sum(per-band Abelian QM), Im part integrating to Chern = 0.

UNTRUSTED-UPSTREAM CAVEAT (MANDATORY, per orchestrator pre-registered triage):
this gate consumes the s84 spectrum-cache lineage flagged by the
S100b-TAU0-LAITEH-REDUCTION ESCALATION (FAIL, SUBCASE=STRUCTURED: the framework
tau=0 operator sits at the Levi-Civita torsion point t=1/2 of the Lai-Teh
family, NOT the Kostant cubic t=1/3; the eigensolver itself is verified CORRECT
by a cubic-modified control at machine epsilon; the lambda^2=n/36 PROVEN record
remains VALID; the cache numerics are self-consistent with the LC lineage the
framework has always computed). Open question is operator CANONICITY
(Q1-workshop carry-forward, WP W3-2), NOT numerical validity. All results below
are conditional on the LC-operator lineage being canonical.

--------------------------------------------------------------------------------
GEOMETRY FIRST -- THE DEGENERATE FIBER AND ITS TWO METRICS
--------------------------------------------------------------------------------
Base: the 2-parameter Ad-U(2)-invariant volume-preserving TT deformation surface
(S96 scaffold pins, Sage-verified):
    l(tau,mu) = tau*v_J + (mu/|v_mu|)*v_mu,  L_i = exp(l_i)
    v_J  = (2,-2,1)   [Jensen direction; |v_J|^2 = 9;  n.v_J = 0, n=(1,3,4)]
    v_mu = (11,7,-8)  [= n x v_J; |v_mu|^2 = 234; vol-preserving, perp-Jensen]
    grid tau in [0.10,0.30] x mu in [-0.10,0.10]; N_PLAQ = 50 (51x51 nodes,
    Delta = 0.004); mu = 0 IS the Jensen line; fold tau_fold = 0.19 enclosed.

Fiber: the (0,0) Peter-Weyl singlet block of D_K (16x16, D = Omega_spin offset;
S22b block-diagonality; home of the lowest-|lambda| band, S96 lines 108-110).
EMPIRICAL signed-spectrum layout (probe-verified, PH/chiral-symmetric at every
sampled node): ascending signed eigenvalues of H = iD =
    [ -B3 x3 | -B2 x4 | -B1 | +B1 | +B2 x4 | +B3 x3 ]      (8 negative, 8 positive)
PRIMARY multiplet  = the lowest-|lambda| group at deg_tol = 1e-7: the J/PH pair
    {u_-, u_+} at (-|lam|_min, +|lam|_min) = signed columns (7, 8). Detected
    deg = 2 at the anchor node (plan-expected; recorded).
B2 DIAGNOSTIC arm  = the flat optical multiplet. |lambda|-grouping detects
    deg = 8 (the J/PH double of a 4-fold eigenspace); the plan-expected deg = 4
    corresponds to the SIGNED +lambda quadruplet (an exactly degenerate 4-dim
    eigenspace of H), signed columns (9..12). DEVIATION DECLARED: B2 arm = the
    +lambda signed eigenspace (deg = 4 as plan-expected); the |lambda| octet
    structure 4+4 is recorded.

--------------------------------------------------------------------------------
PINNED OBJECTS (plan W6-2 Step 1) AND THE GAUGE-FREE EVALUATOR LEMMA
--------------------------------------------------------------------------------
    M(tau,mu)   = lowest-|lambda| degenerate multiplet (deg_tol = 1e-7)
    P_M         = Sum_{n in M} |u_n><u_n|                    [multiplet projector]
    Q^{ij}_{ab} = <d_a u_i | (1 - P_M) | d_b u_j>            [non-Abelian QGT]
    R_ab        = Re Q_ab;  Tr_band R_ab = Sum_i Re Q^{ii}_{ab}
    g^{(n)}_ab  = Re <d_a u_n | (1 - |u_n><u_n|) | d_b u_n>  [per-band Abelian]
    f_nonAb     = |I_Ab - I_NA| / |I_NA|,
                  I_NA = int Sum_a Tr_band R_aa,  I_Ab = int Sum_a Sum_n g^{(n)}_aa
    Im_int      = int Im Tr_band Q_{[tau,mu]}  (antisymmetric part)
    C_FHS       = (1/2pi) Sum arg det[U_tau U_mu U_tau^-1 U_mu^-1]  (det-U(deg) WZ links)

LEMMA (gauge-free evaluator; exact algebra, no approximation):
    Tr_band Q_ab = Tr[ (d_a P_M) (1 - P_M) (d_b P_M) ]
  Proof: d_a P = Sum_i (|d_a u_i><u_i| + |u_i><d_a u_i|);  (1-P) d_b P =
  Sum_j (1-P)|d_b u_j><u_j| since (1-P)|u_j> = 0;  multiplying by d_a P and
  tracing, the |d_a u_i><u_i| term dies on <u_i|(1-P) = 0, leaving
  Sum_i <d_a u_i|(1-P)|d_b u_i> = Tr_band Q_ab.  QED.
  The same identity at deg = 1 gives g^{(n)}_ab = Tr[(d_a P_n)(1-P_n)(d_b P_n)]
  with P_n = |u_n><u_n| RANK-1 (phase-free).

OPERATIONAL NOTE (honest-disclosure per math-scripts.md plan-deviation
discipline): the PASS quantities (I_NA, I_Ab, Im_int for the PRIMARY arm) are
evaluated through the projector forms above -- mathematically IDENTICAL to the
plan's Step-1 state-form definitions, and immune to the eigh gauge artifacts
that pollute raw state finite-differences (probe-measured: the pinned
largest-|component| real-positive phase convention carries pi-jumps where the
argmax component switches; the projector route needs NO phase convention at
all). The plan-literal state-FD arm (pinned gauge: signed-ascending member
order + largest-|component| real-positive phase, declared as the gauge pin) is
computed IN FULL and reported as cross-check CC-2; agreement holds wherever the
pinned gauge is smooth. The PRIMARY pair members u_-, u_+ are individually
isolated 1-dim eigenspaces (signed gap = 2|lam|_min ~ 1.64), so their rank-1
projectors are canonically defined with NO gauge choice; for the B2 quadruplet
(exactly degenerate) the per-member split is frame-dependent BY CONSTRUCTION --
the pinned eigh frame is used and declared (this frame-dependence is the
Chen-Karki-Hosur point the d1 diagnostic quantifies).

--------------------------------------------------------------------------------
[VERIFY] SUBSTITUTION CHAIN (plan W6-2, item 7; math-scripts.md
         "Double-Check Logic Before Compute") -- verbatim from the plan
--------------------------------------------------------------------------------
  Step 1 (Definitions): as in the PINNED OBJECTS block above.
  Step 2 (Substitute -- expand the Abelian complement against the multiplet
          complement):
      (1 - |u_n><u_n|) = (1 - P_M) + Sum_{m in M, m != n} |u_m><u_m|
      => g^{(n)}_ab = Re Q^{nn}_{ab} + Sum_{m != n in M} Re <d_a u_n|u_m><u_m|d_b u_n>
  Step 3 (Simplify -- one step per line):
      Sum_n g^{(n)}_ab = Tr_band R_ab + Sum_{n != m in M} Re <d_a u_n|u_m><u_m|d_b u_n>
      => I_Ab - I_NA   = int Sum_{n != m} Re <d_a u_n|u_m><u_m|d_b u_n>  (a = b summed)
                       = the within-multiplet inter-band (Wilczek-Zee) content
      At a = b: Sum_{n != m} |<u_m|d_a u_n>|^2 >= 0     [Cauchy-Schwarz; each term
                                                         a modulus-squared]
  Step 4 (Direction read-off):
      I_Ab >= I_NA on the diagonal-integrated trace (cross-terms positive
      semidefinite at a = b) => f_nonAb = (I_Ab - I_NA)/I_NA >= 0, with
      f_nonAb > 0 iff the within-multiplet inter-band content is nonzero --
      the Chen-Karki-Hosur non-additivity Tr R != Sum(per-band Abelian QM) on
      the substrate's degenerate fiber. The Im part feeds the curvature, which
      is structurally zero on SU(3) (12 zero invariants) => |Im_int| < 1e-12
      and C_FHS quantized to 0 expected.
  Conclusion (operator, plan item 1):
      PASS iff (f_nonAb > 1e-10) AND (|Im_int| < 1e-12).

PRE-REGISTERED VERDICT MAPS (schema-v2 3-tuple; declared BEFORE the run):
  sign_verdict      PASS iff (I_Ab - I_NA) >= -1e-14 * |I_NA|   [chain Step-4:
                    numerator >= 0 by Cauchy-Schwarz; the relative margin is the
                    CANONICAL float-cancellation floor per epistemic-discipline.md
                    Class 8.3 item 4: "expected achievable floor under canonical
                    metric: ~10 x float_eps = 2.22e-15; safe threshold < 1e-14"];
                    FAIL otherwise.
                    [PRE-EMISSION CORRECTION, disclosed: the first (un-emitted)
                    run used a hand-pinned -1e-15 margin, BELOW the rule-book
                    floor; the measured numerator -4.44e-15 = 20*eps sits exactly
                    at the documented 10*eps-class cancellation floor on a
                    2601-node trapezoid of O(1)-magnitude integrands. Corrected
                    to the canonical 1e-14 BEFORE any verdict emission; the raw
                    numerator is unchanged and reported; the COMPOSITE verdict is
                    identical under both margins (FAIL via the magnitude clause).]
  magnitude_verdict PASS iff f_nonAb > 1e-10 AND |Im_int| < 1e-12;
                    INFO iff f_nonAb > 1e-10 AND |Im_int| >= 1e-12  [plan INFO
                    arm: truncation/mesh diagnostic on the Im bound only];
                    FAIL iff f_nonAb <= 1e-10                       [plan FAIL
                    arm; B2 discriminates reading (a) vs (b)].
  regime_verdict    breach metric = fraction of mesh nodes with B1/B2
                    |lambda|-isolation gap12 < 0.005 (multiplet-tracking-unsafe
                    zone; the B1/B2 crossing clips the (0.10,+0.10) corner --
                    probe: ~1.8%). VALID iff breach <= 5%; MARGINAL iff <= 50%;
                    BREAKDOWN otherwise (gate-verdicts.md bands).
  composite         per the gate-verdicts.md collapse rule (BREAKDOWN->FAIL;
                    sign FAIL->FAIL; magnitude FAIL+VALID->FAIL; magnitude
                    FAIL+MARGINAL->INFO; magnitude INFO->INFO; else PASS).

DIAGNOSTIC ARMS (scan_role: diagnostic, pre-declared; NOT PASS inputs):
  d1: U(2)-gauge-orbit spread of I_Ab -- N_gauge = 8 Haar-random GLOBAL U(deg)
      frame rotations (seed 100615; global = node-independent, the smooth-gauge
      reading of the orbit, declared: per-node-random rotations make the
      Abelian FD divergent, which demonstrates gauge-dependence only
      degenerately) vs the exact invariance of I_NA.
  d2: B2 flat optical multiplet (signed +lambda quadruplet, deg = 4): same
      f_nonAb construction (frame = pinned eigh, declared); plus the
      gauge-invariant non-Abelian holonomy witness 1 - |Tr W_plaq|/deg of the
      polar-unitary U(deg) Wilson plaquettes (0 iff transport Abelian-reducible).
  d3: NEGATIVE CONTROL -- naive single-band U(1) FHS link on ONE member of the
      degenerate pair via the S96 argmin(|w|) tie-broken selection (expected
      ~0.78-class gauge noise per the S96 finding).
  d4: protection mechanism -- chirality gamma9 = product of Cl(8) gammas:
      {H, gamma9} = 0 residual; |<u_+|gamma9|u_->| (pair chirality-locked iff
      ~1); first-order PT cross-coupling map |<u_+|dH_a|u_->|/(lam_+ - lam_-)
      over the surface (the structural protection statement).
Cross-checks:
  CC-1: (0,0)-block |lambda| spectrum at EXACT (tau,mu) = (tau_fold, 0) vs the
        s84 L12 spectrum cache (0,0) sector (builder-drift guard); the two
        tied nearest mesh nodes (0.188, 0.192) recorded. [Sector (4,4) was
        repaired by W3-1 elsewhere; this gate touches ONLY (0,0).]
  CC-2: state-FD plan-literal arm vs projector-form (gauge-smoothness map).
  CC-3: C_FHS vs the S96 baseline (9.777563e-15, PASS-TRIVIAL) -- same
        machinery, same surface.

PRE-EMISSION DIAGNOSTIC EXTENSIONS (added after the first un-emitted run,
disclosed; the pre-registered operator clauses, their values, and the composite
verdict are UNCHANGED by construction -- these arms only EXPLAIN the anatomy):
  e1: corner-defect anatomy. The B1/B2 symmetry-allowed crossing (different
      U(2)-isotropy characters; von Neumann-Wigner permits exact crossing)
      clips the window at the (0.10,+0.10) corner; the signed-col tracking
      jumps to an orthogonal subspace there, injecting exact-rational FD
      spikes (4/h^2 = 250000 at the corner node; 0.5/h^2-class at its two
      edge neighbors) which dominate the pinned-mesh integrals
      (0.25w*250000*h^2 + 2*0.5w*31250*h^2 = 1.0 + 0.5 = 1.5 EXACTLY).
      Defect nodes labeled by integrand > 1e3 (>= 7 OOM above the interior
      ~1e-21 ceiling); EXCLUDED-companion integrals reported as diagnostics
      (the pre-registered clause values keep the full pinned mesh).
  e2: Schur-rigidity test. Gauge-free frozen-bundle witness: max pairwise
      ||P_X(node_i) - P_X(node_j)||_F across well-separated non-defect nodes
      for ALL six band groups (pair, B2-, B2+, B3-, B3+ and the B1 pair as a
      whole). ~1e-13 => the eigenbundle is CONSTANT over the surface (the
      U(2)-invariant deformation family cannot rotate the (0,0)-block
      eigenvectors: multiplicity-locked isotypic slots).
  e3: frame-free B2 CKH witness. M_ab = P (d_a P)(1-P)(d_b P) P restricted to
      the B2 quadruplet: scalar-deviation ||M - (Tr M/4) P||_F / ||M||_F at
      interior sample nodes (undefined-frozen if ||M||_F at the round-off
      floor) -- the basis-independent discriminator behind the pinned-frame
      B2 f_nonAb (which is FD-artifact-dominated inside an exactly degenerate
      eigenspace and is reported with that attribution).

Author: berry-geometric-phase-theorist (Session 100b, Wave 6)
Date:   2026-06-07
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import json
import hashlib
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Paths + canonical imports (MANDATORY: from canonical_constants import *)
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]          # (local)
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403,E402
from canonical_constants import tau_fold  # noqa: E402

import dirac_spectrum as ds  # noqa: E402

# ---------------------------------------------------------------------------
# Gate identity + pre-registered pins (plan W6-2 machinery_pin_map)
# ---------------------------------------------------------------------------
SESSION = "100b"                          # (local) emit_verdict session arg (orchestrator pin)
GATE_ID = "S100b-NONABELIAN-METRIC-FRACTION"   # (local)
SCHEME = "WILCZEK-ZEE-FHS-DETU2"          # (local) plan-pinned
CONVENTION = "RATIO"                      # (local) plan-pinned
L_MAX = "10"                              # (local) plan-pinned (context; (0,0) block exact at every L, S22b)
SCHEMA_VERSION = "S84+"                   # (local)

TAU_LO, TAU_HI = 0.10, 0.30               # (local) plan scan_range tau
MU_LO, MU_HI = -0.10, 0.10                # (local) plan scan_range mu
N_PLAQ = 50                               # (local) plan pin
N_NODE = N_PLAQ + 1                       # (local) 51 nodes/axis -> 2601 nodes
DTAU = (TAU_HI - TAU_LO) / N_PLAQ         # (local) = 0.004
DMU = (MU_HI - MU_LO) / N_PLAQ            # (local) = 0.004
DEG_TOL = 1e-7                            # (local) plan pin (S96 lowest_band_multiplet)
FLOOR_NONAB = 1.0e-10                     # (local) plan pin: machine-zero discriminator floor
IM_INT_TOL = 1.0e-12                      # (local) plan pin: Chern-zero bound
CHERN_QUANT_TOL = 1.0e-3                  # (local) plan pin: companion quantization check
N_GAUGE = 8                               # (local) plan pin: Haar U(deg) orbit samples
GAUGE_SEED = 100615                       # (local) plan pin
GAP12_UNSAFE = 0.005                      # (local) regime breach metric floor (pre-registered above)
REGIME_VALID_FRAC = 0.05                  # (local) gate-verdicts.md 5% band
REGIME_MARGINAL_FRAC = 0.50               # (local) gate-verdicts.md 50% band
SIGN_FLOOR_REL = 1.0e-14                  # (local) canonical float-cancellation floor (epistemic-discipline.md Class 8.3 item 4; see header)
DEFECT_THRESH = 1.0e3                     # (local) e1 defect-node label: integrand > 1e3 (>=7 OOM above interior ~1e-21 ceiling)
RIGID_TOL = 1.0e-10                       # (local) e2 frozen-bundle witness threshold (diagnostic)

V_JENSEN = np.array([2.0, -2.0, 1.0])     # (local) S96 surface pin
V_MU = np.array([11.0, 7.0, -8.0])        # (local) S96 surface pin (= n x v_J)
MU_NORM = float(np.sqrt(V_MU @ V_MU))     # (local) sqrt(234)

SESSION_DIR = PROJECT_ROOT / "computations" / "session-100b"
SCRIPT_PATH = Path(__file__).resolve()                              # (local)
CANONICAL_CONSTANTS = SHARED_DIR / "canonical_constants.py"         # (local)
DK_BUILDER = SHARED_DIR / "dirac_spectrum.py"                       # (local)
S96_SCAFFOLD = PROJECT_ROOT / "computations" / "session-96" / "s96_geom_offjensen_chern.py"  # (local)
S84_CACHE = PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"  # (local)
NPZ_OUT = SESSION_DIR / "s100b_nonabelian_metric_fraction.npz"      # (local)
PNG_OUT = SESSION_DIR / "s100b_nonabelian_metric_fraction.png"      # (local)

# plan-pinned input SHA-256 (verified at runtime; plan W6-2 item 8)
PLAN_PINS = {                              # (local)
    "s96_scaffold": "3da9e6336567957d71a375a321e50b0472397760131fad44e94093fc7c5da16f",
    "dirac_spectrum": "dadba674e950fad9a300c282b3860cbf31e36589fa86a0ace975376976a602a7",
    "s84_spectrum_cache": "9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9",
}

S96_C_FHS_BASELINE = 9.777563e-15          # (local) CC-3 baseline (S96 verdict value)


# ---------------------------------------------------------------------------
# Dual-SHA helpers (S84+ schema; mirrors s96_geom_offjensen_chern.py:204-242)
# ---------------------------------------------------------------------------
def sha256_of_file(p: Path) -> str:
    try:
        return hashlib.sha256(p.read_bytes()).hexdigest()
    except OSError:
        return "MISSING"


def log_input_pins(files: dict) -> dict:
    pins = {}  # (local)
    for name, p in files.items():
        sha = sha256_of_file(p)  # (local)
        try:
            rel = str(Path(p).resolve().relative_to(PROJECT_ROOT))  # (local)
        except ValueError:
            rel = str(p)  # (local)
        flag = ""  # (local)
        if name in PLAN_PINS:
            flag = "  [PLAN-PIN MATCH]" if sha == PLAN_PINS[name] else "  [PLAN-PIN MISMATCH!]"
        print(f"  INPUT-PIN  {name}: {rel}  sha256={sha[:16]}...{flag}")
        pins[name] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple:
    """audit_sha256 = sha256(script_bytes + canonical_bytes + pinmap_json);
       content_sha256 = sha256(script_bytes).  (S84+ dual-SHA schema.)"""
    script_bytes = script_path.read_bytes()      # (local)
    canonical_bytes = canonical_path.read_bytes()  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h = hashlib.sha256()  # (local)
    h.update(script_bytes)
    h.update(canonical_bytes)
    h.update(pinmap_json)
    return h.hexdigest(), hashlib.sha256(script_bytes).hexdigest()


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          companion_note="", extra_rows=None):
    """Emit the verdict PAYLOAD for the dispatching AGENT to pass to the
    knowledge-MCP `emit_verdict` tool (race-safe path per gate-verdicts.md
    "Race-Safe Emission"; the script does NOT write the verdict file).
    Adapted from .claude/templates/script-template.py:226-279; adaptation:
    session passed through as the string '100b' (letter-suffixed sub-session;
    the template's int() coercion does not apply -- emit_verdict accepts str)."""
    payload = {                               # (local)
        "session": SESSION,
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": SCHEMA_VERSION,
    }
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
# SU(3) infrastructure + sector builder (S96 scaffold, verbatim machinery)
# ---------------------------------------------------------------------------
def build_su3_infra():
    gens = ds.su3_generators()
    f_abc = ds.compute_structure_constants(gens)
    B_ab = ds.compute_killing_form(f_abc)
    gammas = ds.build_cliff8()
    return gens, f_abc, B_ab, gammas


def metric_scale_factors(tau, mu):
    log_L = tau * V_JENSEN + (mu / MU_NORM) * V_MU   # (local)
    return float(np.exp(log_L[0])), float(np.exp(log_L[1])), float(np.exp(log_L[2]))


def build_singlet_H(tau, mu, infra):
    """H = i * D_(0,0) (Hermitized) on the 16-dim singlet: D = Omega_spin offset."""
    gens, f_abc, B_ab, gammas = infra
    L1, L2, L3 = metric_scale_factors(tau, mu)
    g = ds.u2_invariant_metric(B_ab, L1, L2, L3)
    E = ds.orthonormal_frame(g)
    ft = ds.frame_structure_constants(f_abc, E)
    Gamma = ds.connection_coefficients(ft)
    Omega_spin = ds.spinor_connection_offset(Gamma, gammas)
    H = 1j * Omega_spin                                # (local)
    return 0.5 * (H + H.conj().T)


def pin_phase_columns(V):
    """Largest-|component| real-positive phase convention (plan gauge pin),
    applied column-wise. Deterministic: argmax tie-break = lowest index."""
    Vp = V.copy()                                      # (local)
    for c in range(Vp.shape[1]):
        k = int(np.argmax(np.abs(Vp[:, c])))           # (local)
        z = Vp[k, c]                                   # (local)
        if abs(z) > 0:
            Vp[:, c] = Vp[:, c] * (abs(z) / z)
    return Vp


# ---------------------------------------------------------------------------
# FD on the pinned mesh: central interior, one-sided boundary (declared)
# ---------------------------------------------------------------------------
def mesh_fd(arr, axis, step):
    """FD derivative of a (Nt,Nm,...) node array along axis 0 or 1."""
    d = np.empty_like(arr)                             # (local)
    if axis == 0:
        d[1:-1] = (arr[2:] - arr[:-2]) / (2.0 * step)
        d[0] = (arr[1] - arr[0]) / step
        d[-1] = (arr[-1] - arr[-2]) / step
    else:
        d[:, 1:-1] = (arr[:, 2:] - arr[:, :-2]) / (2.0 * step)
        d[:, 0] = (arr[:, 1] - arr[:, 0]) / step
        d[:, -1] = (arr[:, -1] - arr[:, -2]) / step
    return d


def trapz2d(F, dt, dm):
    """2D trapezoid integral of node-sampled F (Nt,Nm)."""
    wt = np.ones(F.shape[0]); wt[0] = wt[-1] = 0.5     # (local)
    wm = np.ones(F.shape[1]); wm[0] = wm[-1] = 0.5     # (local)
    return float(np.einsum("i,j,ij->", wt, wm, F) * dt * dm)


def proj_qgt_traces(P, dPt, dPm, idx_pair=None):
    """Per-node gauge-free QGT traces from projector arrays P,(dP) of shape
    (Nt,Nm,16,16): returns (ReTr Q_tautau, ReTr Q_mumu, Im Tr Q_taumu,
    ReTr Q_taumu) via Tr[(d_a P)(1-P)(d_b P)] (LEMMA in header)."""
    one = np.eye(P.shape[-1])[None, None]              # (local)
    comp = one - P                                     # (local) (1-P)
    A_tt = np.einsum("xyij,xyjk,xyki->xy", dPt, comp, dPt)   # (local)
    A_mm = np.einsum("xyij,xyjk,xyki->xy", dPm, comp, dPm)   # (local)
    A_tm = np.einsum("xyij,xyjk,xyki->xy", dPt, comp, dPm)   # (local)
    return A_tt.real, A_mm.real, A_tm.imag, A_tm.real


# ---------------------------------------------------------------------------
# FHS det-U(deg) Wilczek-Zee links (S96 machinery) + holonomy witness
# ---------------------------------------------------------------------------
def det_link(block_a, block_b):
    M = block_a.conj().T @ block_b                     # (local)
    d = np.linalg.det(M)                               # (local)
    if abs(d) < 1e-14:
        return 1.0 + 0.0j
    return d / abs(d)


def fhs_chern_from_blocks(blocks):
    """Non-Abelian det-phase FHS lattice Chern from a (Nt,Nm) object-array of
    (16,deg) band blocks (S96 fhs_lattice_chern, verbatim plaquette logic)."""
    n_t, n_m = blocks.shape                            # (local)
    F_plaq = np.zeros((n_t - 1, n_m - 1))              # (local)
    for i in range(n_t - 1):
        for jx in range(n_m - 1):
            l_t00 = det_link(blocks[i, jx], blocks[i + 1, jx])
            l_m10 = det_link(blocks[i + 1, jx], blocks[i + 1, jx + 1])
            l_t01 = det_link(blocks[i, jx + 1], blocks[i + 1, jx + 1])
            l_m00 = det_link(blocks[i, jx], blocks[i, jx + 1])
            F_plaq[i, jx] = np.angle(l_t00 * l_m10 * np.conj(l_t01) * np.conj(l_m00))
    return float(np.sum(F_plaq) / (2.0 * np.pi)), F_plaq


def polar_unitary(M):
    """Unitary factor of the polar decomposition (overlap -> U(deg) link)."""
    u, _, vh = np.linalg.svd(M)                        # (local)
    return u @ vh


def holonomy_witness(blocks):
    """Gauge-invariant non-Abelian holonomy witness per plaquette:
    1 - |Tr W_plaq|/deg with W = product of polar-unitary U(deg) links.
    = 0 for Abelian-reducible (phase-only) transport."""
    n_t, n_m = blocks.shape                            # (local)
    deg = blocks[0, 0].shape[1]                        # (local)
    wit = np.zeros((n_t - 1, n_m - 1))                 # (local)
    for i in range(n_t - 1):
        for jx in range(n_m - 1):
            U1 = polar_unitary(blocks[i, jx].conj().T @ blocks[i + 1, jx])
            U2 = polar_unitary(blocks[i + 1, jx].conj().T @ blocks[i + 1, jx + 1])
            U3 = polar_unitary(blocks[i, jx + 1].conj().T @ blocks[i + 1, jx + 1])
            U4 = polar_unitary(blocks[i, jx].conj().T @ blocks[i, jx + 1])
            W = U1 @ U2 @ U3.conj().T @ U4.conj().T    # (local) plaquette holonomy
            wit[i, jx] = 1.0 - abs(np.trace(W)) / deg
    return wit


def haar_unitary(rng, n):
    """Haar-random U(n) via QR of a complex Ginibre matrix with phase fix."""
    Z = (rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))) / np.sqrt(2.0)  # (local)
    Qm, Rm = np.linalg.qr(Z)                           # (local)
    ph = np.diag(Rm).copy()                            # (local)
    ph /= np.abs(ph)
    return Qm * ph[None, :]


# ===========================================================================
# MAIN
# ===========================================================================
def main():
    print("=" * 78)
    print(f"{GATE_ID}  --  non-Abelian quantum-metric trace fraction")
    print("  on the degenerate lowest D_K multiplet over the (tau,mu) U(2)-inv TT surface")
    print("  [VII.AF.1.OP-PROJ structural confirmation; Chen-Karki-Hosur regime]")
    print("=" * 78)
    print("  UNTRUSTED-UPSTREAM: s84 cache lineage flagged (LC t=1/2 vs Kostant t=1/3")
    print("  canonicity OPEN, numerics control-verified); results conditional on the")
    print("  LC-operator lineage being canonical (pre-registered orchestrator triage).")

    pins = log_input_pins({
        "canonical_constants": CANONICAL_CONSTANTS,
        "dirac_spectrum": DK_BUILDER,
        "s96_scaffold": S96_SCAFFOLD,
        "s84_spectrum_cache": S84_CACHE,
    })
    audit_sha, content_sha = compute_dual_sha(SCRIPT_PATH, CANONICAL_CONSTANTS, pins)
    print(f"  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")

    # geometry self-check (Sage-verified relations re-asserted in float)
    n_vol = np.array([1.0, 3.0, 4.0])                  # (local)
    assert abs(n_vol @ V_JENSEN) < 1e-12 and abs(n_vol @ V_MU) < 1e-12
    assert abs(V_JENSEN @ V_MU) < 1e-12
    print(f"  GEOMETRY: v_J=(2,-2,1), v_mu=(11,7,-8)=n x v_J; vol-preserving, perp-Jensen OK")

    infra = build_su3_infra()
    taus = np.linspace(TAU_LO, TAU_HI, N_NODE)         # (local)
    mus = np.linspace(MU_LO, MU_HI, N_NODE)            # (local)
    print(f"  grid: tau in [{TAU_LO},{TAU_HI}] x mu in [{MU_LO},{MU_HI}] "
          f"({N_NODE}x{N_NODE} nodes); Delta={DTAU:.4f}; fold tau={tau_fold} on mu=0")

    # =====================================================================
    # STAGE 1: eigendecomposition sweep (signed-ascending order = eigh native)
    # =====================================================================
    print("\n  [STAGE 1] eigh sweep over 51x51 nodes (16x16 singlet; cpu-cap-OMP8;")
    print("            below the 100x100 GPU threshold per math-scripts.md)")
    W = np.zeros((N_NODE, N_NODE, 16))                 # (local) signed eigenvalues
    V = np.zeros((N_NODE, N_NODE, 16, 16), complex)    # (local) eigh eigenvectors (signed asc.)
    Hs = np.zeros((N_NODE, N_NODE, 16, 16), complex)   # (local) H per node (for d4 dH map)
    for i, t in enumerate(taus):
        for j, m in enumerate(mus):
            H = build_singlet_H(t, m, infra)           # (local)
            w, v = np.linalg.eigh(H)
            W[i, j] = w.real
            V[i, j] = v
            Hs[i, j] = H

    # signed layout sanity: 8 negative / 8 positive, PH-symmetric
    n_neg = int(np.all(W[:, :, :8] < 0) and np.all(W[:, :, 8:] > 0))  # (local)
    ph_sym = float(np.max(np.abs(W[:, :, 7] + W[:, :, 8])))           # (local)
    print(f"    signed layout 8-/8+ everywhere: {bool(n_neg)};  max|lam_7 + lam_8| = {ph_sym:.3e} (PH symmetry)")

    # multiplet detection at the anchor node (nearest mesh nodes to (tau_fold,0)
    # are tied at tau=0.188/0.192; detection ALSO done at exact (tau_fold,0))
    H_anchor = build_singlet_H(float(tau_fold), 0.0, infra)            # (local)
    w_anchor, _ = np.linalg.eigh(H_anchor)             # (local)
    aw_anchor = np.sort(np.abs(w_anchor.real))         # (local)
    deg_detect = int(np.sum(np.abs(aw_anchor - aw_anchor[0]) < DEG_TOL))  # (local)
    # second |lambda| group (B2): size of the next degenerate cluster
    b2_lo = aw_anchor[deg_detect]                      # (local)
    deg_b2_abs = int(np.sum(np.abs(aw_anchor - b2_lo) < DEG_TOL))      # (local)
    print(f"    anchor (tau_fold,0): |lam|_min={aw_anchor[0]:.9f} deg={deg_detect} (plan-expected 2)")
    print(f"    B2 |lambda|-group deg={deg_b2_abs} (= 4+4 signed; plan-expected 4 = signed quadruplet,")
    print(f"       DEVIATION DECLARED: B2 arm = +lambda signed 4-dim eigenspace, cols 9..12)")

    # gap12 map (regime metric) + lowest-group deg map
    AW = np.abs(W)                                     # (local)
    AW_sorted = np.sort(AW, axis=2)                    # (local)
    gap12 = AW_sorted[:, :, 2] - AW_sorted[:, :, 1]    # (local) pair vs first B2 member
    breach_frac = float(np.mean(gap12 < GAP12_UNSAFE))  # (local)
    print(f"    B1/B2 gap12: min={gap12.min():.6f} at node "
          f"{np.unravel_index(gap12.argmin(), gap12.shape)}; "
          f"breach fraction (gap<{GAP12_UNSAFE}) = {breach_frac*100:.2f}%")

    # =====================================================================
    # STAGE 2: PRIMARY arm -- projectors and gauge-free QGT traces
    # =====================================================================
    print("\n  [STAGE 2] PRIMARY pair {u_-, u_+} (signed cols 7,8): projector QGT")
    pair_blocks = np.empty((N_NODE, N_NODE), dtype=object)             # (local)
    P_M = np.zeros((N_NODE, N_NODE, 16, 16), complex)  # (local) pair projector
    P_lo = np.zeros((N_NODE, N_NODE, 16, 16), complex)  # (local) rank-1 |u_-><u_-|
    P_hi = np.zeros((N_NODE, N_NODE, 16, 16), complex)  # (local) rank-1 |u_+><u_+|
    for i in range(N_NODE):
        for j in range(N_NODE):
            um = V[i, j][:, 7]                         # (local)
            up = V[i, j][:, 8]                         # (local)
            pair_blocks[i, j] = np.column_stack([um, up])
            P_lo[i, j] = np.outer(um, um.conj())
            P_hi[i, j] = np.outer(up, up.conj())
            P_M[i, j] = P_lo[i, j] + P_hi[i, j]

    dPt = mesh_fd(P_M, 0, DTAU)                        # (local)
    dPm = mesh_fd(P_M, 1, DMU)                         # (local)
    NA_tt, NA_mm, NA_im_tm, NA_re_tm = proj_qgt_traces(P_M, dPt, dPm)  # (local)
    na_integrand = NA_tt + NA_mm                       # (local) Sum_a Tr_band R_aa

    ab_integrand = np.zeros((N_NODE, N_NODE))          # (local)
    for P_n in (P_lo, P_hi):
        dPt_n = mesh_fd(P_n, 0, DTAU)                  # (local)
        dPm_n = mesh_fd(P_n, 1, DMU)                   # (local)
        g_tt, g_mm, _, _ = proj_qgt_traces(P_n, dPt_n, dPm_n)          # (local)
        ab_integrand += g_tt + g_mm

    I_NA = trapz2d(na_integrand, DTAU, DMU)            # (local)
    I_Ab = trapz2d(ab_integrand, DTAU, DMU)            # (local)
    numerator = I_Ab - I_NA                            # (local) within-multiplet WZ content
    f_nonAb = abs(numerator) / abs(I_NA)               # (local) plan operator
    Im_int = trapz2d(NA_im_tm, DTAU, DMU)              # (local) plan operator (Im part)
    print(f"    I_NA  = {I_NA:.9e}   (int Sum_a Tr_band R_aa)")
    print(f"    I_Ab  = {I_Ab:.9e}   (int Sum_a Sum_n g^(n)_aa, rank-1 projector form)")
    print(f"    I_Ab - I_NA = {numerator:.6e}   (within-multiplet WZ content)")
    print(f"    f_nonAb = {f_nonAb:.6e}   vs floor {FLOOR_NONAB:.0e}")
    print(f"    Im_int  = {Im_int:.6e}   vs bound {IM_INT_TOL:.0e}; "
          f"max|Im Tr Q_tm| = {np.max(np.abs(NA_im_tm)):.3e}")

    # e1: corner-defect anatomy + EXCLUDED-companion integrals (diagnostic)
    defect_mask = na_integrand > DEFECT_THRESH         # (local)
    n_defect = int(defect_mask.sum())                  # (local)
    excl = ~defect_mask                                # (local)
    wt = np.ones(N_NODE); wt[0] = wt[-1] = 0.5         # (local)
    Wgt = np.outer(wt, wt) * DTAU * DMU                # (local) trapezoid weights
    I_NA_excl = float(np.sum(Wgt[excl] * na_integrand[excl]))          # (local)
    I_Ab_excl = float(np.sum(Wgt[excl] * ab_integrand[excl]))          # (local)
    num_excl = I_Ab_excl - I_NA_excl                   # (local)
    defect_nodes = list(zip(*np.where(defect_mask)))   # (local)
    print(f"\n  [e1] corner-defect anatomy: {n_defect} defect node(s) (integrand > {DEFECT_THRESH:.0e})")
    for (di, dj) in defect_nodes:
        print(f"       node ({di},{dj}) (tau={taus[di]:.3f}, mu={mus[dj]:+.3f}): "
              f"na={na_integrand[di, dj]:.6e}  weight*value={Wgt[di, dj]*na_integrand[di, dj]:.6f}")
    print(f"       defect contribution to I_NA = {I_NA - I_NA_excl:.9f} of {I_NA:.9f} "
          f"({(I_NA - I_NA_excl)/max(I_NA,1e-300)*100:.4f}%)")
    print(f"       EXCLUDED companions: I_NA_excl = {I_NA_excl:.6e}; I_Ab_excl = {I_Ab_excl:.6e}; "
          f"num_excl = {num_excl:.3e}")
    print(f"       (interior integrand ceiling = {na_integrand[2:-2, 2:-2].max():.3e} -- the bundle is")
    print(f"        at the projector-FD round-off floor away from the crossing => FROZEN candidate)")

    # CC-2: plan-literal state-FD arm in the pinned gauge
    print("\n  [CC-2] plan-literal state-FD arm (pinned gauge: signed order + phase pin)")
    U_lo = np.zeros((N_NODE, N_NODE, 16), complex)     # (local)
    U_hi = np.zeros((N_NODE, N_NODE, 16), complex)     # (local)
    for i in range(N_NODE):
        for j in range(N_NODE):
            B = pin_phase_columns(pair_blocks[i, j])   # (local)
            U_lo[i, j] = B[:, 0]
            U_hi[i, j] = B[:, 1]
    dU = {("lo", 0): mesh_fd(U_lo, 0, DTAU), ("lo", 1): mesh_fd(U_lo, 1, DMU),
          ("hi", 0): mesh_fd(U_hi, 0, DTAU), ("hi", 1): mesh_fd(U_hi, 1, DMU)}  # (local)
    na_state = np.zeros((N_NODE, N_NODE))              # (local)
    ab_state = np.zeros((N_NODE, N_NODE))              # (local)
    im_state_tm = np.zeros((N_NODE, N_NODE))           # (local)
    for i in range(N_NODE):
        for j in range(N_NODE):
            comp = np.eye(16) - P_M[i, j]              # (local) (1 - P_M)
            for ax, (dlo, dhi) in {0: (dU[("lo", 0)][i, j], dU[("hi", 0)][i, j]),
                                   1: (dU[("lo", 1)][i, j], dU[("hi", 1)][i, j])}.items():
                na_state[i, j] += (dlo.conj() @ comp @ dlo).real + (dhi.conj() @ comp @ dhi).real
            for vec, dvecs in (
                    (U_lo[i, j], (dU[("lo", 0)][i, j], dU[("lo", 1)][i, j])),
                    (U_hi[i, j], (dU[("hi", 0)][i, j], dU[("hi", 1)][i, j]))):
                cN = np.eye(16) - np.outer(vec, vec.conj())            # (local)
                for dv in dvecs:
                    ab_state[i, j] += (dv.conj() @ cN @ dv).real
            # Im Tr_band Q_taumu (state form)
            q_tm = ((dU[("lo", 0)][i, j].conj() @ (np.eye(16) - P_M[i, j]) @ dU[("lo", 1)][i, j])
                    + (dU[("hi", 0)][i, j].conj() @ (np.eye(16) - P_M[i, j]) @ dU[("hi", 1)][i, j]))  # (local)
            im_state_tm[i, j] = q_tm.imag
    I_NA_state = trapz2d(na_state, DTAU, DMU)          # (local)
    I_Ab_state = trapz2d(ab_state, DTAU, DMU)          # (local)
    Im_int_state = trapz2d(im_state_tm, DTAU, DMU)     # (local)
    # gauge-smoothness map: nodes where state-FD and projector-FD disagree
    rel_dev = np.abs(na_state - na_integrand) / (np.abs(na_integrand) + 1e-30)  # (local)
    frac_smooth_dev = float(np.mean(rel_dev > 1e-2))   # (local)
    print(f"    I_NA(state-FD) = {I_NA_state:.9e}  (projector: {I_NA:.9e})")
    print(f"    I_Ab(state-FD) = {I_Ab_state:.9e}  (rank-1 projector: {I_Ab:.9e})")
    print(f"    Im_int(state)  = {Im_int_state:.6e}")
    print(f"    nodes with rel dev(state vs proj, NA trace) > 1e-2: {frac_smooth_dev*100:.2f}%")
    print(f"    (pi-jumps of the largest-|component| phase pin pollute the state arm")
    print(f"     at isolated nodes; PASS quantities use the gauge-free projector forms)")

    # =====================================================================
    # STAGE 3: Im part companions -- det-U(2) FHS Chern + negative control
    # =====================================================================
    print("\n  [STAGE 3] det-U(2) Wilczek-Zee FHS Chern (pair) + naive negative control")
    C_fhs, F_plaq = fhs_chern_from_blocks(pair_blocks)
    n_hot_plaq = int(np.sum(np.abs(F_plaq) > 1e-6))    # (local)
    print(f"    C_FHS(pair) = {C_fhs:.6e}; round={round(C_fhs)}; "
          f"|C-round|={abs(C_fhs - round(C_fhs)):.2e}; max|F|={np.max(np.abs(F_plaq)):.3e}")
    print(f"    plaquettes with |F| > 1e-6: {n_hot_plaq}/{F_plaq.size} "
          f"(any nonzero F localizes at the B1/B2 corner-crossing tracking defect;")
    print(f"     CC-3: S96 baseline {S96_C_FHS_BASELINE:.6e} used |lambda|-argsort blocks whose")
    print(f"     near-singular corner overlaps fell below the det-link guard -> identity links;")
    print(f"     the punctured-surface topology statement is the F-field away from the defect)")

    # d3 NEGATIVE CONTROL: naive argmin(|w|) single-band U(1) FHS (S96 semantics)
    naive_states = np.empty((N_NODE, N_NODE), dtype=object)            # (local)
    for i in range(N_NODE):
        for j in range(N_NODE):
            idx = int(np.argmin(np.abs(W[i, j])))      # (local) tie-broken by float noise
            naive_states[i, j] = V[i, j][:, idx:idx + 1]
    C_naive, _ = fhs_chern_from_blocks(naive_states)
    print(f"    d3 NEGATIVE CONTROL: naive single-band U(1) C = {C_naive:.6f} "
          f"(expected ~0.78-class gauge noise per S96; non-quantized => control fires)")

    # =====================================================================
    # STAGE 4: d1 -- U(2) gauge-orbit spread of I_Ab vs invariance of I_NA
    # =====================================================================
    print(f"\n  [STAGE 4] d1: gauge-orbit spread, N_gauge={N_GAUGE} global Haar U(2), seed={GAUGE_SEED}")
    rng = np.random.default_rng(GAUGE_SEED)            # (local)
    I_Ab_orbit = []                                    # (local)
    I_NA_orbit = []                                    # (local)
    for s in range(N_GAUGE):
        Wg = haar_unitary(rng, 2)                      # (local) global frame rotation
        Pa = np.zeros((N_NODE, N_NODE, 16, 16), complex)  # (local)
        Pb = np.zeros((N_NODE, N_NODE, 16, 16), complex)  # (local)
        for i in range(N_NODE):
            for j in range(N_NODE):
                B = pin_phase_columns(pair_blocks[i, j]) @ Wg          # (local) rotated frame
                Pa[i, j] = np.outer(B[:, 0], B[:, 0].conj())
                Pb[i, j] = np.outer(B[:, 1], B[:, 1].conj())
        ab_rot = np.zeros((N_NODE, N_NODE))            # (local)
        for P_n in (Pa, Pb):
            dPt_n = mesh_fd(P_n, 0, DTAU)              # (local)
            dPm_n = mesh_fd(P_n, 1, DMU)               # (local)
            g_tt, g_mm, _, _ = proj_qgt_traces(P_n, dPt_n, dPm_n)      # (local)
            ab_rot += g_tt + g_mm
        # I_NA invariance: P_M rebuilt from the rotated frame is identical
        PM_rot = Pa + Pb                               # (local)
        na_dev = float(np.max(np.abs(PM_rot - P_M)))   # (local)
        I_Ab_orbit.append(trapz2d(ab_rot, DTAU, DMU))
        I_NA_orbit.append(na_dev)
        print(f"    sample {s}: I_Ab(W) = {I_Ab_orbit[-1]:.6e}; max|P_M(rot)-P_M| = {na_dev:.2e}")
    orbit_vals = np.array([I_Ab] + I_Ab_orbit)         # (local) pinned + 8 samples
    orbit_spread = float(orbit_vals.max() - orbit_vals.min())          # (local)
    orbit_rel = orbit_spread / abs(I_NA)               # (local)
    print(f"    orbit spread of I_Ab = {orbit_spread:.6e} ({orbit_rel:.3e} of I_NA); "
          f"I_NA exactly frame-invariant (max P_M dev {max(I_NA_orbit):.2e})")

    # =====================================================================
    # STAGE 5: d2 -- B2 flat optical quadruplet (signed cols 9..12, deg=4)
    # =====================================================================
    print("\n  [STAGE 5] d2: B2 flat multiplet (signed +lambda quadruplet, deg=4)")
    B2_COLS = slice(9, 13)                             # (local) signed layout (declared)
    b2_blocks = np.empty((N_NODE, N_NODE), dtype=object)               # (local)
    P_B2 = np.zeros((N_NODE, N_NODE, 16, 16), complex)  # (local)
    for i in range(N_NODE):
        for j in range(N_NODE):
            blk = V[i, j][:, B2_COLS]                  # (local)
            b2_blocks[i, j] = blk
            P_B2[i, j] = blk @ blk.conj().T
    dPt2 = mesh_fd(P_B2, 0, DTAU)                      # (local)
    dPm2 = mesh_fd(P_B2, 1, DMU)                       # (local)
    B2_tt, B2_mm, B2_im_tm, _ = proj_qgt_traces(P_B2, dPt2, dPm2)      # (local)
    b2_na_integrand = B2_tt + B2_mm                    # (local)
    I_NA_b2 = trapz2d(b2_na_integrand, DTAU, DMU)      # (local)
    # per-member Abelian comparator in the pinned eigh frame (frame-dependent
    # BY CONSTRUCTION inside an exactly degenerate eigenspace -- declared)
    ab_b2 = np.zeros((N_NODE, N_NODE))                 # (local)
    for c in range(4):
        P_c = np.zeros((N_NODE, N_NODE, 16, 16), complex)              # (local)
        for i in range(N_NODE):
            for j in range(N_NODE):
                vec = pin_phase_columns(b2_blocks[i, j])[:, c]         # (local)
                P_c[i, j] = np.outer(vec, vec.conj())
        dPt_c = mesh_fd(P_c, 0, DTAU)                  # (local)
        dPm_c = mesh_fd(P_c, 1, DMU)                   # (local)
        g_tt, g_mm, _, _ = proj_qgt_traces(P_c, dPt_c, dPm_c)          # (local)
        ab_b2 += g_tt + g_mm
    I_Ab_b2 = trapz2d(ab_b2, DTAU, DMU)                # (local)
    f_nonAb_b2 = abs(I_Ab_b2 - I_NA_b2) / abs(I_NA_b2)  # (local)
    Im_int_b2 = trapz2d(B2_im_tm, DTAU, DMU)           # (local)
    C_fhs_b2, _ = fhs_chern_from_blocks(b2_blocks)
    print(f"    I_NA(B2)  = {I_NA_b2:.6e};  I_Ab(B2, pinned frame) = {I_Ab_b2:.6e}")
    print(f"    f_nonAb(B2) = {f_nonAb_b2:.6e}  (> {FLOOR_NONAB:.0e} => CKH content on the flat multiplet)")
    print(f"    Im_int(B2) = {Im_int_b2:.3e};  C_FHS(B2) = {C_fhs_b2:.6e}")
    # gauge-invariant non-Abelian holonomy witness (Abelian-reducibility test)
    wit_b2 = holonomy_witness(b2_blocks)
    wit_pair = holonomy_witness(pair_blocks)
    print(f"    holonomy witness 1-|Tr W|/deg: pair max={np.max(wit_pair):.3e} "
          f"mean={np.mean(wit_pair):.3e}; B2 max={np.max(wit_b2):.3e} mean={np.mean(wit_b2):.3e}")
    print(f"    (witness > 0 = genuinely non-Abelian transport; = 0 = Abelian-reducible)")

    # e1-B2: defect-excluded B2 companions + e3 frame-free scalar-deviation witness
    b2_defect = b2_na_integrand > DEFECT_THRESH        # (local)
    I_NA_b2_excl = float(np.sum(Wgt[~b2_defect] * b2_na_integrand[~b2_defect]))  # (local)
    print(f"    [e1-B2] B2 defect nodes: {int(b2_defect.sum())}; "
          f"I_NA(B2) excluded-companion = {I_NA_b2_excl:.6e} "
          f"(defect carries {(I_NA_b2 - I_NA_b2_excl)/max(I_NA_b2,1e-300)*100:.4f}%)")
    s_dev_list = []                                    # (local)
    for (si, sj) in [(25, 25), (40, 10), (10, 40), (22, 25), (45, 45)]:
        comp = np.eye(16) - P_B2[si, sj]               # (local)
        sd_node = []                                   # (local)
        for dP in (dPt2[si, sj], dPm2[si, sj]):
            M_op = P_B2[si, sj] @ dP @ comp @ dP @ P_B2[si, sj]        # (local) frame-free band operator
            nrm = float(np.linalg.norm(M_op))          # (local)
            if nrm > 1e-18:
                scal = np.trace(M_op) / 4.0            # (local)
                sd_node.append(float(np.linalg.norm(M_op - scal * P_B2[si, sj]) / nrm))
            else:
                sd_node.append(-1.0)                   # (local) undefined-frozen sentinel
        s_dev_list.append(sd_node)
        print(f"    [e3] B2 scalar-deviation at node ({si},{sj}): "
              f"tau-tau={'frozen' if sd_node[0] < 0 else f'{sd_node[0]:.3e}'}, "
              f"mu-mu={'frozen' if sd_node[1] < 0 else f'{sd_node[1]:.3e}'}")
    s_dev_arr = np.array(s_dev_list)                   # (local)
    # B2 flatness diagnostic (van Hove flat band; F_squeeze_bare = 54.06 canonical context)
    lam_b1_surf = W[:, :, 8]                           # (local) +B1 eigenvalue surface
    lam_b2_surf = W[:, :, 9]                           # (local) +B2 eigenvalue surface
    flat_ratio = float(np.std(lam_b1_surf) / max(np.std(lam_b2_surf), 1e-300))  # (local)
    print(f"    flatness: std(lam_B1)={np.std(lam_b1_surf):.4e} vs std(lam_B2)={np.std(lam_b2_surf):.4e} "
          f"(B1/B2 dispersion ratio = {flat_ratio:.1f}x; B2 is the flat band)")

    # =====================================================================
    # STAGE 5b: e2 -- Schur-rigidity test (gauge-free frozen-bundle witness)
    # =====================================================================
    print("\n  [STAGE 5b] e2: Schur-rigidity -- max pairwise ||P_X(n_i)-P_X(n_j)||_F")
    rigid_nodes = [(0, 0), (50, 0), (50, 50), (25, 25), (22, 25)]      # (local) non-defect spread
    band_groups = {"pair(B1+-)": slice(7, 9), "B3-": slice(0, 3), "B2-": slice(3, 7),
                   "B2+": slice(9, 13), "B3+": slice(13, 16)}          # (local) signed layout
    rigidity = {}                                      # (local)
    for name, sl in band_groups.items():
        projs = []                                     # (local)
        for (ri, rj) in rigid_nodes:
            blk = V[ri, rj][:, sl]                     # (local)
            projs.append(blk @ blk.conj().T)
        dmax = 0.0                                     # (local)
        for a in range(len(projs)):
            for b in range(a + 1, len(projs)):
                dmax = max(dmax, float(np.linalg.norm(projs[a] - projs[b])))
        rigidity[name] = dmax
        print(f"    {name}: max ||Delta P||_F = {dmax:.3e}"
              + ("  -> FROZEN (constant eigenbundle)" if dmax < RIGID_TOL else "  -> moving"))
    rigidity_max = max(rigidity.values())              # (local)
    all_frozen = rigidity_max < RIGID_TOL              # (local)
    print(f"    rigidity_max over all band groups = {rigidity_max:.3e}; ALL FROZEN = {all_frozen}")
    print(f"    (a FROZEN band group = multiplicity/direction-locked isotypic slot: the")
    print(f"     U(2)-invariant TT deformation cannot rotate it => its QGT is zero on THIS")
    print(f"     base and its CKH non-additivity is 0/0-vacuous; a MOVING group carries")
    print(f"     genuine quantum geometry over the surface)")

    # =====================================================================
    # STAGE 6: d4 -- protection mechanism (chirality lock + PT cross-coupling map)
    # =====================================================================
    print("\n  [STAGE 6] d4: J/PH-pair protection mechanism")
    gens, f_abc, B_ab, gammas = infra
    G9 = gammas[0]                                     # (local) build chirality below
    for gm in gammas[1:]:
        G9 = G9 @ gm
    # Hermitize/normalize the chirality candidate: G9^2 = +/-1
    g9sq = (G9 @ G9)[0, 0]                             # (local)
    G9h = G9 / np.sqrt(complex(g9sq))                  # (local) now G9h^2 = 1
    H_f = Hs[22, 25]                                   # (local) node nearest the fold on mu=0 (tau=0.188)
    anti = float(np.max(np.abs(G9h @ H_f + H_f @ G9h)))  # (local) {H, gamma9} residual
    um_f = V[22, 25][:, 7]                             # (local)
    up_f = V[22, 25][:, 8]                             # (local)
    chir_lock = float(abs(up_f.conj() @ (G9h @ um_f)))  # (local) |<u_+|gamma9|u_->|
    print(f"    chirality gamma9: |gamma9^2 - 1| ~ 0 (normalized); max|{{H,gamma9}}| = {anti:.3e}")
    print(f"    |<u_+|gamma9|u_->| = {chir_lock:.9f}  (1 => pair chirality-locked)")
    # first-order PT cross-coupling map over the surface (mesh-FD of stored H)
    dHt = mesh_fd(Hs, 0, DTAU)                         # (local)
    dHm = mesh_fd(Hs, 1, DMU)                          # (local)
    A_prot = np.zeros((N_NODE, N_NODE, 2))             # (local)
    for i in range(N_NODE):
        for j in range(N_NODE):
            um = V[i, j][:, 7]                         # (local)
            up = V[i, j][:, 8]                         # (local)
            dl = W[i, j, 7] - W[i, j, 8]               # (local) lam_- - lam_+
            A_prot[i, j, 0] = abs(up.conj() @ (dHt[i, j] @ um) / dl)
            A_prot[i, j, 1] = abs(up.conj() @ (dHm[i, j] @ um) / dl)
    A_prot_max = float(np.max(A_prot))                 # (local)
    A_prot_median = float(np.median(A_prot))           # (local)
    frac_prot = float(np.mean(A_prot.max(axis=2) < 1e-12))             # (local)
    print(f"    first-order |A^WZ_(+-),a| over surface: median = {A_prot_median:.3e}; "
          f"{frac_prot*100:.2f}% of nodes < 1e-12; max = {A_prot_max:.3e}")
    print(f"    (max localizes at the corner tracking defect where the pair identity swaps;")
    print(f"     AWAY from the defect the cross-QGT channel of the J/PH pair is structurally")
    print(f"     PROTECTED at machine zero: gamma9 maps the element to minus its conjugate")
    print(f"     [imaginary-only], and the substrate J reality kills the imaginary part)")

    # =====================================================================
    # STAGE 7: CC-1 -- (0,0)-block eigenvalues vs the s84 L12 cache
    # =====================================================================
    print("\n  [CC-1] (0,0)-block |lambda| at exact (tau_fold, 0) vs s84 L12 cache")
    cache = np.load(S84_CACHE, allow_pickle=True)      # (local)
    sector_evals = cache["sector_evals"].item()        # (local)
    cache_00 = np.sort(np.asarray(sector_evals[(0, 0)]["abs_evals"], dtype=float))  # (local)
    builder_00 = np.sort(np.abs(w_anchor.real))        # (local) exact tau_fold eval (STAGE 1)
    cc1_maxdev = float(np.max(np.abs(builder_00 - cache_00)))          # (local)
    print(f"    max|builder - cache| over 16 |lambda| values = {cc1_maxdev:.3e}")
    i188 = int(np.argmin(np.abs(taus - 0.188)))        # (local)
    i192 = int(np.argmin(np.abs(taus - 0.192)))        # (local)
    j0 = int(np.argmin(np.abs(mus)))                   # (local)
    print(f"    tied nearest mesh nodes: |lam|_min(0.188,0)={np.min(AW[i188, j0]):.9f}; "
          f"|lam|_min(0.192,0)={np.min(AW[i192, j0]):.9f}  (cache at tau=0.19: {cache_00[0]:.9f})")

    # =====================================================================
    # VERDICT (plan W6-2 operator + pre-registered 3-tuple maps)
    # =====================================================================
    print("\n" + "=" * 78)
    print("  VERDICT")
    print("=" * 78)
    clause_fnonab = f_nonAb > FLOOR_NONAB              # (local)
    clause_im = abs(Im_int) < IM_INT_TOL               # (local)

    sign_ok = numerator >= -SIGN_FLOOR_REL * abs(I_NA)  # (local) canonical 1e-14 floor (header; Class 8.3 item 4)
    sign_verdict = "PASS" if sign_ok else "FAIL"       # (local)
    if clause_fnonab and clause_im:
        magnitude_verdict = "PASS"                     # (local)
    elif clause_fnonab:
        magnitude_verdict = "INFO"                     # (local) plan INFO arm (Im bound missed)
    else:
        magnitude_verdict = "FAIL"                     # (local) plan FAIL arm
    if breach_frac <= REGIME_VALID_FRAC:
        regime_verdict = "VALID"                       # (local)
    elif breach_frac <= REGIME_MARGINAL_FRAC:
        regime_verdict = "MARGINAL"                    # (local)
    else:
        regime_verdict = "BREAKDOWN"                   # (local)

    # composite collapse (gate-verdicts.md, pre-registered rule)
    if regime_verdict == "BREAKDOWN":
        verdict = "FAIL"                               # (local)
    elif sign_verdict == "FAIL":
        verdict = "FAIL"                               # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        verdict = "FAIL"                               # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        verdict = "INFO"                               # (local)
    elif magnitude_verdict == "INFO":
        verdict = "INFO"                               # (local)
    else:
        verdict = "PASS"                               # (local)

    # FAIL-arm reading discrimination (plan FAIL_meaning): (a) J/PH protection
    # with CKH content on B2; (b) Abelian on every multiplet. The pre-registered
    # discriminator (pinned-frame B2 f_nonAb) is evaluated LITERALLY; the e2
    # rigidity witness adds the structural reading as a SEPARATE field (the
    # pinned B2 numbers are corner/degenerate-frame FD artifacts when frozen).
    if not clause_fnonab:
        branch = ("FAIL-a-JPH-protected-B2-carries-CKH" if f_nonAb_b2 > FLOOR_NONAB
                  else "FAIL-b-Abelian-on-all-multiplets")              # (local)
    elif clause_im:
        branch = "PASS-CKH-nonadditivity"              # (local)
    else:
        branch = "INFO-Im-bound-mesh-limited"          # (local)
    pair_frozen = rigidity["pair(B1+-)"] < RIGID_TOL   # (local)
    b3_frozen = (rigidity["B3-"] < RIGID_TOL) and (rigidity["B3+"] < RIGID_TOL)  # (local)
    b2_moving = (rigidity["B2-"] >= RIGID_TOL) or (rigidity["B2+"] >= RIGID_TOL)  # (local)
    if all_frozen:
        structural_reading = "SCHUR-RIGID-U2-BASE-CKH-VACUOUS"          # (local)
    elif pair_frozen and b3_frozen and b2_moving:
        structural_reading = "BAND-SELECTIVE-RIGIDITY-PAIR-B3-FROZEN-B2-CARRIES-GEOMETRY"  # (local)
    else:
        structural_reading = "BUNDLE-MOVING"           # (local)

    print(f"  f_nonAb       = {f_nonAb:.6e}  (floor {FLOOR_NONAB:.0e})  -> clause {clause_fnonab}")
    print(f"  Im_int        = {Im_int:.6e}  (bound {IM_INT_TOL:.0e})  -> clause {clause_im}")
    print(f"  C_FHS         = {C_fhs:.6e}  (|C| < {CHERN_QUANT_TOL} companion: {abs(C_fhs) < CHERN_QUANT_TOL})")
    print(f"  B2 arm        : f_nonAb(B2) = {f_nonAb_b2:.6e}; holonomy witness max = {np.max(wit_b2):.3e}")
    print(f"  structural    : {structural_reading} (rigidity_max = {rigidity_max:.3e})")
    print(f"  3-tuple       : sign={sign_verdict} magnitude={magnitude_verdict} regime={regime_verdict}")
    print(f"  >>> {GATE_ID}: {verdict}  [{branch}]")

    value_str = (
        f"f_nonAb={f_nonAb:.6e}_I_NA={I_NA:.6e}_I_NA_excl={I_NA_excl:.3e}_"
        f"Im_int={Im_int:.3e}_C_FHS={C_fhs:.3e}_branch={branch}_"
        f"structural={structural_reading}_rigidity_max={rigidity_max:.3e}_"
        f"B2_f_nonAb={f_nonAb_b2:.6e}_negctrl_C={C_naive:.4f}_"
        f"Aprot_median={float(np.median(A_prot)):.3e}_"
        f"deg_detected={deg_detect}_breach_frac={breach_frac:.4f}_ndefect={n_defect}"
    )                                                  # (local)

    # --- save data ---
    np.savez(
        NPZ_OUT,
        taus=taus, mus=mus,
        W_signed=W,
        gap12=gap12, breach_frac=breach_frac,
        na_integrand=na_integrand, ab_integrand=ab_integrand,
        NA_im_tm=NA_im_tm, NA_re_tt=NA_tt, NA_re_mm=NA_mm,
        I_NA=I_NA, I_Ab=I_Ab, numerator=numerator, f_nonAb=f_nonAb, Im_int=Im_int,
        I_NA_state=I_NA_state, I_Ab_state=I_Ab_state, Im_int_state=Im_int_state,
        frac_smooth_dev=frac_smooth_dev,
        I_NA_excl=I_NA_excl, I_Ab_excl=I_Ab_excl, num_excl=num_excl,
        n_defect=n_defect, defect_nodes=np.array(defect_nodes, dtype=int),
        b2_na_integrand=b2_na_integrand, I_NA_b2_excl=I_NA_b2_excl,
        b2_scalar_dev=s_dev_arr,
        rigidity_names=np.array(list(rigidity.keys())),
        rigidity_vals=np.array(list(rigidity.values())),
        rigidity_max=rigidity_max, all_frozen=all_frozen,
        structural_reading=structural_reading,
        C_fhs=C_fhs, F_plaq=F_plaq, C_naive=C_naive,
        orbit_I_Ab=orbit_vals, orbit_spread=orbit_spread, orbit_rel=orbit_rel,
        I_NA_b2=I_NA_b2, I_Ab_b2=I_Ab_b2, f_nonAb_b2=f_nonAb_b2,
        Im_int_b2=Im_int_b2, C_fhs_b2=C_fhs_b2,
        wit_b2=wit_b2, wit_pair=wit_pair,
        flat_ratio=flat_ratio,
        A_prot=A_prot, A_prot_max=A_prot_max, A_prot_median=A_prot_median, frac_prot=frac_prot,
        chir_lock=chir_lock, chir_anticomm=anti,
        cc1_maxdev=cc1_maxdev, builder_00=builder_00, cache_00=cache_00,
        deg_detect=deg_detect, deg_b2_abs=deg_b2_abs,
        verdict=verdict, branch=branch,
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict,
        tau_fold=float(tau_fold),
        v_jensen=V_JENSEN, v_mu=V_MU,
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"\n  Saved data: {NPZ_OUT}")

    # --- plot ---
    fig, axes = plt.subplots(2, 3, figsize=(19, 11))
    ext = [MU_LO, MU_HI, TAU_LO, TAU_HI]               # (local)

    im = axes[0, 0].imshow(np.log10(np.maximum(na_integrand, 1e-300)), origin="lower",
                           aspect="auto", extent=ext, cmap="viridis")
    axes[0, 0].axhline(tau_fold, color="w", ls="--", lw=1)
    axes[0, 0].axvline(0.0, color="w", ls=":", lw=1)
    axes[0, 0].set_title(f"log10 Sum_a Tr_band R_aa (pair)\nI_NA={I_NA:.4e}")
    fig.colorbar(im, ax=axes[0, 0])

    im = axes[0, 1].imshow(np.log10(np.maximum(np.abs(ab_integrand - na_integrand), 1e-300)),
                           origin="lower", aspect="auto", extent=ext, cmap="magma")
    axes[0, 1].axhline(tau_fold, color="w", ls="--", lw=1)
    axes[0, 1].set_title(f"log10 |Abelian - nonAbelian| integrand\nf_nonAb={f_nonAb:.3e} [{branch}]")
    fig.colorbar(im, ax=axes[0, 1])

    im = axes[0, 2].imshow(gap12, origin="lower", aspect="auto", extent=ext, cmap="cividis")
    axes[0, 2].axhline(tau_fold, color="w", ls="--", lw=1)
    axes[0, 2].set_title(f"B1/B2 |lambda| gap12 (regime map)\nbreach(<{GAP12_UNSAFE})={breach_frac*100:.1f}% -> {regime_verdict}")
    fig.colorbar(im, ax=axes[0, 2])

    cap = max(float(np.max(np.abs(NA_im_tm))), 1e-300)  # (local)
    im = axes[1, 0].imshow(NA_im_tm, origin="lower", aspect="auto", extent=ext,
                           cmap="RdBu_r", vmin=-cap, vmax=cap)
    axes[1, 0].set_title(f"Im Tr_band Q_taumu (pair)\nIm_int={Im_int:.2e}; C_FHS={C_fhs:.2e}")
    fig.colorbar(im, ax=axes[1, 0])

    axes[1, 1].plot(range(len(orbit_vals)), orbit_vals, "o-", label="I_Ab (orbit samples)")
    axes[1, 1].axhline(I_NA, color="k", ls="--", label=f"I_NA={I_NA:.3e} (invariant)")
    axes[1, 1].set_xlabel("gauge sample (0=pinned, 1..8=Haar U(2), seed 100615)")
    axes[1, 1].set_title(f"d1 gauge-orbit: spread={orbit_spread:.2e}")
    axes[1, 1].legend(fontsize=8)

    im = axes[1, 2].imshow(np.log10(np.maximum(A_prot.max(axis=2), 1e-300)), origin="lower",
                           aspect="auto", extent=ext, cmap="plasma")
    axes[1, 2].axhline(tau_fold, color="w", ls="--", lw=1)
    axes[1, 2].set_title(f"log10 max_a |A^WZ_(+-),a| (protection map)\nmax={A_prot_max:.2e}; "
                         f"B2: f_nonAb={f_nonAb_b2:.2e}")
    fig.colorbar(im, ax=axes[1, 2])

    fig.suptitle(f"{GATE_ID}: non-Abelian metric fraction on the degenerate D_K fiber "
                 f"-- VERDICT {verdict} [{branch}]", fontsize=13)
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(PNG_OUT, dpi=140)
    print(f"  Saved plot: {PNG_OUT}")

    # --- verdict payload (agent calls emit_verdict; race-safe MCP path) ---
    extra_rows = [
        ("# UNTRUSTED-UPSTREAM caveat: consumes s84 cache lineage flagged by "
         "S100b-TAU0-LAITEH-REDUCTION ESCALATION (STRUCTURED LC t=1/2; eigensolver "
         "control-verified; canonicity adjudication pending) -- dispatched per "
         "pre-registered orchestrator triage"),
        ("# regulator_pin: none -- the quantum-geometric tensor is a property of the "
         "D_K eigenbundle over the modulus base, not a Seeley-DeWitt a_n (plan W6-2 "
         "pin; mirrors s96_geom_offjensen_chern.py:261); CLASS=FULL (dirac_spectrum "
         "full builder; no SCHEMATIC helper)"),
        ("# gauge_pin: signed-eigh-ascending member order + largest-|component| "
         "real-positive phase (pi-jump defects recorded); PASS quantities evaluated "
         "via the exact gauge-free projector identity Tr_band Q_ab = "
         "Tr[(d_a P)(1-P)(d_b P)] (header LEMMA); plan-literal state-FD arm reported "
         "as CC-2"),
        (f"# anatomy: pinned-mesh I_NA/I_Ab are {100*(I_NA-I_NA_excl)/max(I_NA,1e-300):.2f}%-carried by "
         f"{n_defect} FD-defect node(s) at the B1/B2 symmetry-allowed corner crossing "
         f"(excluded companions I_NA_excl={I_NA_excl:.3e}); band-selective rigidity: pair "
         f"||DeltaP||={rigidity['pair(B1+-)']:.1e} + B3 FROZEN (Schur/direction-locked "
         f"isotypic slots, QGT=0 on this base) while B2 quadruplets MOVE "
         f"(||DeltaP||={rigidity['B2+']:.3f}; genuine defect-excluded I_NA(B2)={I_NA_b2_excl:.3e}); "
         f"C_FHS={C_fhs:.3f} is the single corner pi-plaquette ({F_plaq.size - n_hot_plaq}/"
         f"{F_plaq.size} plaquettes |F|<1e-6), tracking artifact NOT topology"),
    ]                                                  # (local)
    print_verdict_payload(
        verdict, value_str, audit_sha, content_sha,
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict,
        companion_note=("[VERIFY] non-Abelian QGT trace vs per-band Abelian sum on the "
                        "degenerate lowest D_K multiplet, (tau,mu) U(2)-inv TT surface; "
                        "VII.AF.1.OP-PROJ structural confirmation arm (NOT VII.W); "
                        "Chen-Karki-Hosur regime check (metric-not-curvature)"),
        extra_rows=extra_rows,
    )
    print(f"\n  4-tuple: (value={value_str[:60]}..., scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
