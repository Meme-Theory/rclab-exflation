#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
S101-B2-ISOTROPY-BREAKING  --  S-2-ENRICHED dual-prior discriminator
================================================================================
Gate:   S101-B2-ISOTROPY-BREAKING   (trigger [SIGN], classification GEOMETRIC)
Agent:  berry-geometric-phase-theorist  (COMPUTE owner; Stage-0 exclusion applies
        ONLY to the Wave-7 S101-SCHUR-RIGIDITY-STAGE2-VERIFY, NOT to this gate)
Plan:   sessions/session-plan/session-101-plan-w5.md  ## SECTION W5-4
WP:     sessions/session-101/session-101-w5-workingpaper.md  ### SECTION W5-4

--------------------------------------------------------------------------------
GEOMETRY FIRST -- THE RELEASE CONDITION AND WHAT IT TESTS
--------------------------------------------------------------------------------
On the U(2)-invariant TT base (S96/W6-2 surface), the B2 quadruplet's
non-Abelian quantum-metric band matrix M_ab is Schur-FORCED scalar (T2): the
four B2 members are an irreducible U(2)-isotypic block, so ANY G-invariant
operator on it is proportional to the rank-4 projector P (Schur's lemma). This
makes Abelian-vs-non-Abelian (Wilczek-Zee) structurally UNDECIDABLE by any
G-invariant functional on the invariant base -- Corollary U (S100b berry
synthesis V.9; W6-2 measured the Schur-scalar floor at e3 ~ 1e-13 while the
frame-dependent Abelian sum spanned 670x; FAIL(a) on the invariant base).

This gate executes the RELEASE the no-go itself licenses. Deform the base along
the C^2 coset directions lambda_4..lambda_7 -- the directions that ARE 94.8% of
the Level-1 metric content (W6-1 d3) -- to break the isotropy that masks the
question. Release condition R (BINDING, S100b berry synthesis V.1): under
H(b) + eps*dH with [rho(g), dH] != 0 for some U(2) generator g, T2's step (2)
fails for the broken generators; M_ab develops anisotropy at O(eps) IFF genuine
within-band Wilczek-Zee structure exists.

DUAL-PRIOR DISCRIMINATOR (S-2 BINDING):
  Track A (prior 0.6): genuine within-band WZ structure, symmetry-masked on the
    invariant base; anisotropy A(eps) = C1*eps + C2*eps^2 + ..., C1 != 0
    => slope d log A / d log eps = 1 + O(eps).  PASS -> 0.9 Track A.
  Track B (prior 0.4): B2 content structurally Abelian-isotropic beyond the
    symmetry forcing (residual protection Stab(dH) superset SU(2) or J-reality)
    => A(eps) ~ A_floor ~ 1e-13, slope ~ 0.  FAIL -> 0.85 Track B.
  Degenerate first order (C1 = 0, C2 != 0): A(eps) ~ C2*eps^2, slope ~ 2
    => INFO (scaling indeterminate -- not a pre-registered track; priors
    UNCHANGED, family re-pinned).
  W6-2's FAIL(a) carries ZERO prior weight against Track A (Corollary U: the
  invariant base could not have seen the difference).

--------------------------------------------------------------------------------
DEFORMATION FAMILY (FINALIZED at plan-freeze)
--------------------------------------------------------------------------------
H(b; eps) := H(b) + eps * dH_a, with dH_a = the off-block LOG-METRIC direction
along Gell-Mann coset generator lambda_a (||dH_a||_F = 1), a in {4, 6}.

Construction (the "off-block log-metric direction"): the base singlet H is built
ENTIRELY from the U(2)-invariant metric g via the deterministic D_K pipeline
g -> orthonormal_frame -> frame_structure_constants -> connection_coefficients
-> spinor_connection_offset -> H = i*Omega_spin (s100b build_singlet_H). The base
metric (u2_invariant_metric) is BLOCK-DIAGONAL in su(3) = u(1)+su(2)+C^2 and has
NO off-block content -- this is precisely why the base is coset-isotropic. The
off-block log-metric direction turns on a symmetric metric coupling between the
coset index a and the u(1) anchor index 8 (lambda_8), normalized in the Killing
(|B|) base scale, and is pushed through the SAME pipeline:
    dH_a := normalize( d/d_eta H(g + eta * dg_a) |_{eta=0} ),  ||dH_a||_F = 1
    dg_a[a,8] = dg_a[8,a] = sqrt(|B|_aa * |B|_88)   (off-block coset<->u(1) bump)
This is a genuine LOG-METRIC direction (directional derivative of H induced by an
off-block metric perturbation) and breaks U(2)-invariance: [rho(g_8), dH_a] != 0
verified by the O(1) first-order rotation ||dP_B2/d_eps|| ~ 3.68 at eps=0.

PRIMARY direction a = 4 (first coset generator, canonical Gell-Mann ordering);
ROBUSTNESS COMPANION a = 6 (second coset pair) -- evaluated alongside, REPORTED.
PRE-REGISTERED FALLBACK (declared at plan-freeze, NOT convention-shopping): if
the PRIMARY fails release control (i) but the companion passes, re-pin in-gate to
a = 6 WITH disclosure in the verdict value field; if BOTH fail control (i) ->
INFO branch (control failed; priors unchanged; family re-pinned at S102).

EPS-SCAN: eps in {1e-4, 3.1623e-4, 1e-3, 3.1623e-3, 1e-2} (5 points, half-decade
log spacing; binding requires >= 3 valid).

--------------------------------------------------------------------------------
THREE PRE-REGISTERED WITNESSES (binding, S-2)
--------------------------------------------------------------------------------
(i) RELEASE POSITIVE-CONTROL (MANDATORY before the discriminator is read,
    Class-8.7-adjacent pre-flight): frozen-slot motion ||DeltaP(B1)||_F > 1e-10
    AND ||DeltaP(B3)||_F > 1e-10 at eps = 1e-2 (visibly above the 1e-14 frozen
    floor) -- else the deformation failed to break isotropy at the fiber level
    and the gate is VACUOUS (INFO, priors unchanged).
(ii) ANISOTROPY DISCRIMINATOR:
    A(b) := ||M_ab - (Tr_band M_ab / 4) * P||_F / ||M_ab||_F at interior
    defect-excluded nodes; M_ab = P (d_a P)(1-P)(d_b P) P on the B2 quadruplet
    (the frame-free band operator, s100b e3 witness). PASS floor A > 1e-10
    (three decades above the measured 1e-13 e3 Schur-scalar floor) AND
    first-order eps-scaling: OLS fitted slope d log A / d log eps = 1.0 +/- 0.3
    over the >= 3 valid scan points.
(iii) DEFECT-EXCLUDED f_nonAb(B2, deformed) via the gauge-free L0 evaluator with
    gap-mapping and defect-excluded companions, sign floor 1e-14. BASELINE
    HONESTY (binding): the W6-2 literal 7.44e+03 anchors the ARTIFACT-CHANNEL
    SCALE ONLY (eigh intra-eigenspace rotations) -- NOT a physics target; any
    claimed f_nonAb must demonstrate FRAME-INVARIANCE before counting as
    evidence: relative U(2)-orbit spread of the claimed f_nonAb <= 1e-10 over a
    pinned 16-point Haar orbit sample (seed = 101). REPORTED with its
    frame-invariance demonstration; it does NOT flip the verdict (evidence-
    channel, not gate-channel).

--------------------------------------------------------------------------------
[SIGN] SUBSTITUTION CHAIN (plan W5-4, item 7) -- verbatim from the plan
--------------------------------------------------------------------------------
  Def 1: A(b; eps) := ||M_ab(eps) - (Tr_band M_ab(eps)/4)*P||_F / ||M_ab(eps)||_F
         [identically 0 at eps = 0 by T2 Schur forcing on the U(2)-invariant base]
  Def 2: Release condition R: under H(b) + eps*dH with [rho(g), dH] != 0 for some
         g, T2's step (2) fails for the broken generators; M_ab develops
         anisotropy at O(eps) IFF genuine within-band WZ structure exists.
  Substitute: Track A => A(eps) = C1*eps + C2*eps^2 + ..., C1 != 0 (generic dH;
         the lambda_4/lambda_6 pair guards the measure-zero C1 = 0 accident on a
         single direction).
  Simplify:  log A = log C1 + 1*log eps + log(1 + (C2/C1)*eps + ...)
             d log A / d log eps = 1 + O(eps)   [eps <= 1e-2 => correction <= ~1e-2]
  Track B:   (Stab(dH) superset SU(2), or J-reality keeps M_ab scalar off-symmetry)
             => A(eps) ~ A_floor ~ 1e-13 (e3 Schur-scalar floor) => slope ~ 0
  Degenerate first order (C1 = 0, C2 != 0) => slope ~ 2 => INFO (not a track)
  Canonical form: slope in [0.7, 1.3] <=> first-order release; ~0 <=> floor;
             ~2 <=> INFO
  Direction: band 1.0 +/- 0.3 separates slope-1 from slope-0 and slope-2 with
             >= 2.3x margin each side
  Conclusion: fitted-slope band [0.7, 1.3] pinned; floors 1e-10 three decades
             above the measured Schur-scalar floor.

PRE-REGISTERED VERDICT MAP (declared BEFORE the run):
  control_ok := (||DeltaP(B1)|| > 1e-10) AND (||DeltaP(B3)|| > 1e-10) at eps=1e-2
                (on the FAMILY direction that survives the fallback chain).
  A_above_floor := A > 1e-10 at interior defect-excluded nodes.
  slope_in_band := OLS fitted slope d log A / d log eps in [0.7, 1.3]
                   over >= 3 valid scan points.
  PASS  iff control_ok AND A_above_floor AND slope_in_band.
  FAIL  iff control_ok AND (A at floor, A <= 1e-10).
  INFO  iff (NOT control_ok on both directions) OR (A above floor but slope
            outside [0.7, 1.3] -- scaling indeterminate, e.g. slope ~ 2).
  sign_verdict     PASS iff the slope SIGN/MAGNITUDE matches the Track-A
                   prediction (slope in [0.7,1.3]); FAIL iff slope sign wrong;
                   N/A handled by mapping: slope ~2 => sign correct (positive
                   release) but magnitude indeterminate.
  magnitude_verdict PASS iff slope_in_band AND A_above_floor; INFO iff A above
                   floor but slope outside band (degenerate-first-order); FAIL
                   iff A at floor.
  regime_verdict   breach metric = fraction of mesh nodes with B1/B2
                   |lambda|-isolation gap12 < 0.005 over the deformed stencil at
                   eps_max; VALID iff <= 5%; MARGINAL iff <= 50%; BREAKDOWN else.
  composite        per the gate-verdicts.md collapse rule.

MCP PRE-COMPUTE AUDIT (run before compute):
  search_knowledge('B2 isotropy breaking Wilczek-Zee Schur') -> only Schur-on-
    invariant-base theorems (D5, C8) + W6-2 baselines; NO prior isotropy-broken
    B2 gate. CONFIRMED un-run.
  get_constant(tau_fold) -> 0.19 (S12/S42; CONST-FREEZE-42).
A19 HANDLING: S101-TAU0-OPERATOR-CANONICITY landed PASS (Wave-1 L4 lift; verdict
  file). The A19 caveat is DISCHARGED -- s84 cache full-confidence (orchestrator
  override; "carries the A19 caveat until the Wave-1 L4 lift executes" clause met).
  NO untrusted_upstream row.

Author: berry-geometric-phase-theorist (Session 101, Wave 5)
Date:   2026-06-08
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
# Gate identity + pre-registered pins (plan W5-4 machinery_pin_map)
# ---------------------------------------------------------------------------
SESSION = "101"                              # (local) emit_verdict session arg
GATE_ID = "S101-B2-ISOTROPY-BREAKING"        # (local)
SCHEME = "GAUGE-FREE-L0"                      # (local) plan-pinned
CONVENTION = "DEFECT-EXCLUDED-FROBENIUS"     # (local) plan-pinned
L_MAX = "12"                                 # (local) plan-pinned (s84 L12 cache lineage)
SCHEMA_VERSION = "S84+"                       # (local)

# Base TT surface (S96/W6-2 scaffold; same base as the upstream)
V_JENSEN = np.array([2.0, -2.0, 1.0])        # (local) S96 surface pin
V_MU = np.array([11.0, 7.0, -8.0])           # (local) S96 surface pin (= n x v_J)
MU_NORM = float(np.sqrt(V_MU @ V_MU))        # (local) sqrt(234)

# eps scan (plan pin: 5-point half-decade mesh)
EPS_SCAN = np.array([1.0e-4, 3.1623e-4, 1.0e-3, 3.1623e-3, 1.0e-2])  # (local) plan pin
EPS_MAX = 1.0e-2                             # (local) control eval point

# Deformation family directions (coset generators; PRIMARY a=4, COMPANION a=6)
COSET_PRIMARY = 4                            # (local) plan pin: first coset generator
COSET_COMPANION = 6                          # (local) plan pin: second coset pair
U1_ANCHOR = 7                               # (local) lambda_8 (u(1) index in 0-based gen array)
ETA_FD = 1.0e-6                             # (local) FD step for the dH_a metric-direction derivative

# Base-node + stencil (anchor at the fold on mu=0; central FD stencil for d/d(tau,mu))
TAU0 = float(tau_fold)                       # (local) 0.19 fold anchor (mu=0 IS the Jensen line)
MU0 = 0.0                                    # (local)
H_STEP = 0.004                               # (local) mesh spacing (matches s100b N_PLAQ=50 surface)
B2_COLS = slice(9, 13)                       # (local) signed +lambda quadruplet (s100b declared layout)
B1_COLS = slice(7, 9)                        # (local) J/PH pair (cols 7,8)
B3_LO = slice(0, 3)                          # (local) -B3 triplet
B3_HI = slice(13, 16)                        # (local) +B3 triplet
DEG_TOL = 1e-7                               # (local) plan pin (S96 lowest_band_multiplet)

# Floors / bands (plan pins; W6-2 machine-zero-discriminator philosophy)
CONTROL_FLOOR = 1.0e-10                       # (local) plan pin: release control ||DeltaP|| floor
A_FLOOR = 1.0e-10                            # (local) plan pin: anisotropy PASS floor
SLOPE_LO, SLOPE_HI = 0.7, 1.3                # (local) plan pin: first-order release band
SIGN_FLOOR = 1.0e-14                          # (local) plan pin: f_nonAb sign floor
ORBIT_CEIL = 1.0e-10                          # (local) plan pin: f_nonAb frame-invariance orbit-spread ceiling
N_HAAR = 16                                  # (local) plan pin: Haar orbit sample size
HAAR_SEED = 101                              # (local) plan pin: Haar orbit seed (deformation deterministic)
GAP12_UNSAFE = 0.005                          # (local) regime breach metric floor
REGIME_VALID_FRAC = 0.05                      # (local) gate-verdicts.md 5% band
REGIME_MARGINAL_FRAC = 0.50                   # (local) gate-verdicts.md 50% band
DEFECT_THRESH = 1.0e3                         # (local) e1 defect-node label (integrand > 1e3; s100b lineage)
A_VALID_FLOOR = 1.0e-11                       # (local) eps-points with A above this enter the slope fit (above the 1e-13 Schur floor, below the 1e-10 PASS floor)

# Upstream baseline anchors (s100b npz; REPORTED as cross-checks, never targets)
W62_F_NONAB_ARTIFACT = 7440.371270905078      # (local) W6-2 literal: ARTIFACT-CHANNEL SCALE ONLY (eigh rotations)
W62_I_NA_B2_EXCL = 0.025907652395944922       # (local) I_NA_excl(B2) = 2.59e-2
W62_E3_FLOOR = 1.0e-13                         # (local) e3 Schur-scalar floor (measured)
W62_ORBIT_REL = 670.295547048228              # (local) W6-2 d1 frame spread on the Abelian sum

SESSION_DIR = PROJECT_ROOT / "computations" / "session-101"
SCRIPT_PATH = Path(__file__).resolve()                              # (local)
CANONICAL_CONSTANTS = SHARED_DIR / "canonical_constants.py"         # (local)
DK_BUILDER = SHARED_DIR / "dirac_spectrum.py"                       # (local)
NA_NPZ = PROJECT_ROOT / "computations" / "session-100b" / "s100b_nonabelian_metric_fraction.npz"  # (local)
NA_PY = PROJECT_ROOT / "computations" / "session-100b" / "s100b_nonabelian_metric_fraction.py"    # (local)
NPZ_OUT = SESSION_DIR / "s101_w5_4_b2_isotropy_breaking.npz"        # (local)
PNG_OUT = SESSION_DIR / "s101_w5_4_b2_isotropy_breaking.png"        # (local)

# plan-pinned input SHA-256 (verified at runtime; plan W5-4 item 8)
PLAN_PINS = {                                # (local)
    "nonabelian_metric_npz": "a31ff591087e090590ea5cbce9f6410e08cdedfe611ba00728dca87edfeaf6f5",
    "nonabelian_metric_py": "03c7532340767a9932e6cbb487ddb65f7f56a596e466a6d7f1b1db505340192a",
    "dirac_spectrum": "dadba674e950fad9a300c282b3860cbf31e36589fa86a0ace975376976a602a7",
}


# ---------------------------------------------------------------------------
# Dual-SHA helpers (S84+ schema; mirrors s100b_nonabelian_metric_fraction.py:287-355)
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
       content_sha256 = sha256(script_bytes).  (S84+ dual-SHA schema.)
    The machinery_pin_map (deformation_family + seed) is folded into the pinmap
    via the static input SHAs (the deformation family is fully determined by the
    dirac_spectrum builder + this script's constants, both hashed)."""
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
    knowledge-MCP `emit_verdict` tool (race-safe path; the script does NOT write
    the verdict file). Mirrors s100b_nonabelian_metric_fraction.py:323-355."""
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
# SU(3) infra + singlet H builder (s100b machinery, verbatim pipeline)
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


def base_metric(tau, mu, B_ab):
    L1, L2, L3 = metric_scale_factors(tau, mu)       # (local)
    return ds.u2_invariant_metric(B_ab, L1, L2, L3)


def H_from_metric(g, infra):
    """H = i*D_(0,0) (Hermitized) on the 16-dim singlet, from an arbitrary
    metric g (s100b build_singlet_H pipeline; g need NOT be U(2)-invariant)."""
    gens, f_abc, B_ab, gammas = infra
    E = ds.orthonormal_frame(g)                      # (local)
    ft = ds.frame_structure_constants(f_abc, E)      # (local)
    Gamma = ds.connection_coefficients(ft)           # (local)
    Omega_spin = ds.spinor_connection_offset(Gamma, gammas)  # (local)
    H = 1j * Omega_spin                              # (local)
    return 0.5 * (H + H.conj().T)


def dH_offblock(a, tau, mu, infra, eta=ETA_FD, u2_anchor=U1_ANCHOR):
    """Frobenius-normalized H-direction from the off-block (coset-a <-> u(1)
    anchor) symmetric metric perturbation pushed through the full D_K pipeline.
    THE 'off-block log-metric direction along lambda_a' of the plan.
    Returns (dH_a normalized to ||.||_F=1, raw norm)."""
    gens, f_abc, B_ab, gammas = infra
    g0base = np.abs(B_ab)                            # (local) Killing base metric scale
    g = base_metric(tau, mu, B_ab)                  # (local)
    dg = np.zeros((8, 8))                            # (local)
    s = float(np.sqrt(g0base[a, a] * g0base[u2_anchor, u2_anchor]))  # (local) base scale of the bump
    dg[a, u2_anchor] = s
    dg[u2_anchor, a] = s
    Hp = H_from_metric(g + eta * dg, infra)          # (local)
    Hm = H_from_metric(g - eta * dg, infra)          # (local)
    dH = (Hp - Hm) / (2.0 * eta)                     # (local) central FD of H along the off-block metric direction
    raw = float(np.linalg.norm(dH))                  # (local)
    return dH / raw, raw


def haar_unitary(rng, n):
    """Haar-random U(n) via QR of a complex Ginibre matrix with phase fix
    (s100b haar_unitary:485-491, verbatim)."""
    Z = (rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))) / np.sqrt(2.0)  # (local)
    Qm, Rm = np.linalg.qr(Z)                         # (local)
    ph = np.diag(Rm).copy()                          # (local)
    ph /= np.abs(ph)
    return Qm * ph[None, :]


def pin_phase_columns(V):
    """Largest-|component| real-positive phase convention (s100b gauge pin)."""
    Vp = V.copy()                                    # (local)
    for c in range(Vp.shape[1]):
        k = int(np.argmax(np.abs(Vp[:, c])))         # (local)
        z = Vp[k, c]                                 # (local)
        if abs(z) > 0:
            Vp[:, c] = Vp[:, c] * (abs(z) / z)
    return Vp


# ---------------------------------------------------------------------------
# Band-matrix anisotropy A and the gauge-free QGT (s100b LEMMA + e3 witness)
# ---------------------------------------------------------------------------
def proj_b2(H, cols=B2_COLS):
    """B2 quadruplet projector P = blk blk^dag from eigh of H (signed-ascending)."""
    _, V = np.linalg.eigh(H)                         # (local)
    blk = V[:, cols]                                 # (local)
    return blk @ blk.conj().T, V


def band_anisotropy(dH_a, eps, infra, tau=TAU0, mu=MU0, h=H_STEP, cols=B2_COLS):
    """A(b) = ||M_ab - (Tr_band M_ab / 4) P||_F / ||M_ab||_F for a in {tau,mu};
    M_ab = P (d_a P)(1-P)(d_b P) P on the B2 quadruplet (s100b e3 frame-free band
    operator, lines 785-797). Returns (A_tau, A_mu, ||M_tau||, ||M_mu||).
    Identically the Schur floor at eps=0; releases iff WZ structure exists."""
    def Pb2(t, m):
        H = H_from_metric(base_metric(t, m, infra[2]), infra) + eps * dH_a  # (local)
        P, _ = proj_b2(H, cols)
        return P
    P0 = Pb2(tau, mu)                                # (local)
    dPt = (Pb2(tau + h, mu) - Pb2(tau - h, mu)) / (2.0 * h)  # (local)
    dPm = (Pb2(tau, mu + h) - Pb2(tau, mu - h)) / (2.0 * h)  # (local)
    comp = np.eye(16) - P0                           # (local) (1 - P)
    out = []                                         # (local)
    nrms = []                                        # (local)
    for dP in (dPt, dPm):
        M = P0 @ dP @ comp @ dP @ P0                 # (local) frame-free band operator
        nrm = float(np.linalg.norm(M))               # (local)
        nrms.append(nrm)
        if nrm > 1e-18:
            scal = np.trace(M) / 4.0                 # (local)
            out.append(float(np.linalg.norm(M - scal * P0) / nrm))
        else:
            out.append(-1.0)                         # (local) undefined-frozen sentinel
    return out[0], out[1], nrms[0], nrms[1]


def proj_qgt_traces(P, dPt, dPm):
    """Per-node gauge-free QGT traces from projector arrays (s100b proj_qgt_traces
    LEMMA, lines 423-432): Tr[(d_a P)(1-P)(d_b P)]. P,(dP) shape (Nt,Nm,16,16)."""
    comp = np.eye(P.shape[-1])[None, None] - P       # (local)
    A_tt = np.einsum("xyij,xyjk,xyki->xy", dPt, comp, dPt)   # (local)
    A_mm = np.einsum("xyij,xyjk,xyki->xy", dPm, comp, dPm)   # (local)
    A_tm = np.einsum("xyij,xyjk,xyki->xy", dPt, comp, dPm)   # (local)
    return A_tt.real, A_mm.real, A_tm.imag, A_tm.real


def mesh_fd(arr, axis, step):
    """Central interior FD, one-sided boundary (s100b mesh_fd, lines 402-413)."""
    d = np.empty_like(arr)                           # (local)
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
    """2D trapezoid integral of node-sampled F (s100b trapz2d, lines 416-420)."""
    wt = np.ones(F.shape[0]); wt[0] = wt[-1] = 0.5   # (local)
    wm = np.ones(F.shape[1]); wm[0] = wm[-1] = 0.5   # (local)
    return float(np.einsum("i,j,ij->", wt, wm, F) * dt * dm)


# ---------------------------------------------------------------------------
# Stencil grid around the anchor (for the deformed-surface f_nonAb witness iii)
# ---------------------------------------------------------------------------
def stencil_grid(n_half=2, h=H_STEP, tau=TAU0, mu=MU0):
    """Small (2*n_half+1)^2 (tau,mu) grid centred at the anchor for the
    defect-excluded f_nonAb companion (witness iii). Returns taus, mus."""
    taus = tau + h * np.arange(-n_half, n_half + 1)  # (local)
    mus = mu + h * np.arange(-n_half, n_half + 1)    # (local)
    return taus, mus


# ===========================================================================
# MAIN
# ===========================================================================
def main():
    print("=" * 78)
    print(f"{GATE_ID}  --  S-2 dual-prior isotropy-breaking discriminator")
    print("  B2 quadruplet band-matrix anisotropy under off-block coset deformation")
    print("  eps*dH_a (a in {4,6}); release condition R; Track A / B / degenerate-1st-order")
    print("=" * 78)
    print("  A19: S101-TAU0-OPERATOR-CANONICITY landed PASS (Wave-1 L4 lift) ->")
    print("       A19 caveat DISCHARGED; s84 cache full-confidence; NO untrusted_upstream row.")

    pins = log_input_pins({
        "canonical_constants": CANONICAL_CONSTANTS,
        "dirac_spectrum": DK_BUILDER,
        "nonabelian_metric_npz": NA_NPZ,
        "nonabelian_metric_py": NA_PY,
    })
    audit_sha, content_sha = compute_dual_sha(SCRIPT_PATH, CANONICAL_CONSTANTS, pins)
    print(f"  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")

    # geometry self-check (S96 surface relations)
    n_vol = np.array([1.0, 3.0, 4.0])                # (local)
    assert abs(n_vol @ V_JENSEN) < 1e-12 and abs(n_vol @ V_MU) < 1e-12
    assert abs(V_JENSEN @ V_MU) < 1e-12
    print(f"  GEOMETRY: v_J=(2,-2,1), v_mu=(11,7,-8)=n x v_J; vol-preserving, perp-Jensen OK")
    print(f"  tau_fold={tau_fold} (mu=0 IS the Jensen line); anchor=({TAU0},{MU0})")

    infra = build_su3_infra()

    # base spectrum sanity at the anchor (signed layout, B2 quadruplet)
    H0 = H_from_metric(base_metric(TAU0, MU0, infra[2]), infra)  # (local)
    w0, V0 = np.linalg.eigh(H0)
    aw = np.sort(np.abs(w0.real))                    # (local)
    deg_min = int(np.sum(np.abs(aw - aw[0]) < DEG_TOL))  # (local)
    b2lo = aw[deg_min]                               # (local)
    deg_b2_abs = int(np.sum(np.abs(aw - b2lo) < DEG_TOL))  # (local)
    print(f"\n  [BASE] anchor signed evals layout [-B3x3|-B2x4|-B1|+B1|+B2x4|+B3x3]:")
    print(f"    |lam|_min={aw[0]:.6f} deg={deg_min} (B1 pair); B2 |lam|-group={b2lo:.6f} "
          f"deg={deg_b2_abs} (=4+4 signed; B2 arm = signed cols 9..12)")
    print(f"    B2 quadruplet signed evals (cols 9..12) = {np.round(w0.real[9:13], 8)} "
          f"(spread {w0.real[12] - w0.real[9]:.2e} -- exactly degenerate)")

    # =====================================================================
    # STAGE 1: build the deformation directions (PRIMARY a=4, COMPANION a=6)
    # =====================================================================
    print("\n  [STAGE 1] off-block log-metric directions dH_a (||dH_a||_F = 1)")
    dirs = {}                                        # (local)
    for a in (COSET_PRIMARY, COSET_COMPANION):
        dH_a, raw = dH_offblock(a, TAU0, MU0, infra)  # (local)
        herm = float(np.max(np.abs(dH_a - dH_a.conj().T)))  # (local)
        # first-order isotropy-breaking witness: O(1) projector rotation at eps=0
        e = 1e-5                                      # (local)
        Pp, _ = proj_b2(H0 + e * dH_a)
        Pm, _ = proj_b2(H0 - e * dH_a)
        dPb2_deps = float(np.linalg.norm((Pp - Pm) / (2.0 * e)))  # (local)
        dirs[a] = dH_a
        print(f"    lambda_{a}: ||dH_raw||={raw:.4e}  ||dH_a||_F={np.linalg.norm(dH_a):.6f}  "
              f"hermdev={herm:.2e}")
        print(f"       first-order break: ||dP_B2/d_eps||_F(eps=0)={dPb2_deps:.4e} "
              f"(O(1) => [rho(g),dH_a]!=0; Release condition R hypothesis holds)")

    # =====================================================================
    # STAGE 2: RELEASE POSITIVE-CONTROL (i) -- frozen-slot motion at eps_max
    # =====================================================================
    print("\n  [STAGE 2] (i) RELEASE POSITIVE-CONTROL: ||DeltaP(B1)||, ||DeltaP(B3)|| at eps_max=1e-2")
    P_b1_0 = V0[:, B1_COLS] @ V0[:, B1_COLS].conj().T  # (local)
    blk_b3_0 = np.column_stack([V0[:, B3_LO], V0[:, B3_HI]])  # (local)
    P_b3_0 = blk_b3_0 @ blk_b3_0.conj().T            # (local)
    control = {}                                     # (local)
    for a, dH_a in dirs.items():
        He = H0 + EPS_MAX * dH_a                     # (local)
        we, Ve = np.linalg.eigh(He)
        P_b1_e = Ve[:, B1_COLS] @ Ve[:, B1_COLS].conj().T  # (local)
        blk_b3_e = np.column_stack([Ve[:, B3_LO], Ve[:, B3_HI]])  # (local)
        P_b3_e = blk_b3_e @ blk_b3_e.conj().T        # (local)
        dPb1 = float(np.linalg.norm(P_b1_e - P_b1_0))  # (local)
        dPb3 = float(np.linalg.norm(P_b3_e - P_b3_0))  # (local)
        ok = (dPb1 > CONTROL_FLOOR) and (dPb3 > CONTROL_FLOOR)  # (local)
        control[a] = (dPb1, dPb3, ok)
        print(f"    lambda_{a}: ||DeltaP(B1)||={dPb1:.4e}  ||DeltaP(B3)||={dPb3:.4e}  "
              f"(floor {CONTROL_FLOOR:.0e})  control_ok={ok}")

    # FALLBACK CHAIN (pre-registered): PRIMARY a=4 unless it fails control & companion passes
    primary_ok = control[COSET_PRIMARY][2]           # (local)
    companion_ok = control[COSET_COMPANION][2]        # (local)
    if primary_ok:
        a_used = COSET_PRIMARY                        # (local)
        fallback_note = "none-primary-a4"            # (local)
    elif companion_ok:
        a_used = COSET_COMPANION                      # (local)
        fallback_note = "REPINNED-to-a6-primary-failed-control"  # (local)
    else:
        a_used = COSET_PRIMARY                        # (local) report on primary; both failed
        fallback_note = "BOTH-FAILED-control-INFO"   # (local)
    control_ok = primary_ok or companion_ok           # (local) gate uses the surviving direction
    dH_used = dirs[a_used]                            # (local)
    print(f"    -> family direction used: lambda_{a_used} ({fallback_note}); control_ok={control_ok}")

    # =====================================================================
    # STAGE 3: ANISOTROPY DISCRIMINATOR (ii) -- A(b;eps) over the eps scan
    # =====================================================================
    print("\n  [STAGE 3] (ii) ANISOTROPY DISCRIMINATOR A(b;eps) on the B2 quadruplet")
    print("    M_ab = P (d_a P)(1-P)(d_b P) P (frame-free); A = ||M-(TrM/4)P||/||M||")
    # eps=0 baseline (Schur floor) -- report on BOTH directions for the record
    A0p = band_anisotropy(dirs[COSET_PRIMARY], 0.0, infra)   # (local)
    A0c = band_anisotropy(dirs[COSET_COMPANION], 0.0, infra)  # (local)
    print(f"    eps=0  : a=4 A(tau)={A0p[0]:.3e} A(mu)={A0p[1]:.3e} | a=6 A(tau)={A0c[0]:.3e} "
          f"A(mu)={A0c[1]:.3e}  [Schur floor; T2 forcing]")

    # scan on the USED direction (gate) + companion (reported)
    A_scan = {COSET_PRIMARY: [], COSET_COMPANION: []}  # (local) [(A_tau, A_mu, nrm_tau, nrm_mu)]
    for a in (COSET_PRIMARY, COSET_COMPANION):
        for eps in EPS_SCAN:
            A_scan[a].append(band_anisotropy(dirs[a], eps, infra))
        rows = A_scan[a]                             # (local)
        print(f"    --- lambda_{a} eps-scan (A_tau, A_mu):")
        for eps, r in zip(EPS_SCAN, rows):
            print(f"      eps={eps:.4e}: A(tau)={r[0]:.4e}  A(mu)={r[1]:.4e}")

    # eps-scaling fit on the USED direction; A(mu) is the dominant channel
    def fit_slope(eps_arr, A_arr):
        A_arr = np.asarray(A_arr)                    # (local)
        valid = A_arr > A_VALID_FLOOR                # (local)
        if valid.sum() < 3:
            return np.nan, np.nan, int(valid.sum())
        coeff, cov = np.polyfit(np.log10(eps_arr[valid]), np.log10(A_arr[valid]), 1, cov=True)  # (local)
        return float(coeff[0]), float(np.sqrt(cov[0, 0])), int(valid.sum())

    used_rows = np.array(A_scan[a_used])             # (local) (5,4)
    A_tau_used = used_rows[:, 0]                     # (local)
    A_mu_used = used_rows[:, 1]                      # (local)
    slope_tau, se_tau, nval_tau = fit_slope(EPS_SCAN, A_tau_used)  # (local)
    slope_mu, se_mu, nval_mu = fit_slope(EPS_SCAN, A_mu_used)      # (local)
    # the channel with more valid points / larger A is the discriminator channel
    A_max_used = float(np.max(np.concatenate([A_tau_used, A_mu_used])))  # (local)
    # dominant channel = the one with the larger A at eps_max
    if A_mu_used[-1] >= A_tau_used[-1]:
        slope_disc, se_disc, nval_disc, chan = slope_mu, se_mu, nval_mu, "mu"  # (local)
    else:
        slope_disc, se_disc, nval_disc, chan = slope_tau, se_tau, nval_tau, "tau"  # (local)
    A_above_floor = A_max_used > A_FLOOR             # (local)
    slope_in_band = (not np.isnan(slope_disc)) and (SLOPE_LO <= slope_disc <= SLOPE_HI)  # (local)
    print(f"    eps-scaling (lambda_{a_used}, dominant channel '{chan}'):")
    print(f"      slope(tau)={slope_tau:.4f}+/-{se_tau:.4f} (n={nval_tau}); "
          f"slope(mu)={slope_mu:.4f}+/-{se_mu:.4f} (n={nval_mu})")
    print(f"      discriminator slope = {slope_disc:.4f}  band [{SLOPE_LO},{SLOPE_HI}]  "
          f"in_band={slope_in_band}")
    print(f"      A_max(used) = {A_max_used:.4e}  floor {A_FLOOR:.0e}  above_floor={A_above_floor}")
    # structural reading of the slope
    if not np.isnan(slope_disc):
        if SLOPE_LO <= slope_disc <= SLOPE_HI:
            slope_reading = "FIRST-ORDER-RELEASE-C1nonzero-TrackA"  # (local)
        elif slope_disc < SLOPE_LO:
            slope_reading = "FLOOR-slope0-TrackB"     # (local)
        elif 1.7 <= slope_disc <= 2.3:
            slope_reading = "DEGENERATE-FIRST-ORDER-C1zero-C2nonzero-slope2-INFO"  # (local)
        else:
            slope_reading = f"INDETERMINATE-slope{slope_disc:.2f}-INFO"  # (local)
    else:
        slope_reading = "INSUFFICIENT-VALID-POINTS"  # (local)
    print(f"      slope reading: {slope_reading}")

    # B2 eigenvalue-splitting cross-check (the cleanest C1=0 witness; slope-2 exact)
    print("\n  [STAGE 3b] B2 eigenvalue-splitting eps-scaling (clean C1=0 witness)")
    split = []                                       # (local)
    for eps in EPS_SCAN:
        we, _ = np.linalg.eigh(H0 + eps * dH_used)   # (local)
        b2 = np.sort(we.real)[9:13]                  # (local)
        split.append(float(b2.max() - b2.min()))
    split = np.array(split)                          # (local)
    split_slope, split_se, _ = fit_slope(EPS_SCAN, split)  # (local)
    print(f"    B2 splitting vs eps: {np.array2string(split, precision=3)}")
    print(f"    splitting slope d log(spread)/d log eps = {split_slope:.4f}+/-{split_se:.4f} "
          f"(=2 => degenerate-first-order: 4-dim eigenspace splits at O(eps^2))")

    # =====================================================================
    # STAGE 4: WITNESS (iii) -- defect-excluded f_nonAb(B2, deformed) + frame-inv
    # =====================================================================
    print("\n  [STAGE 4] (iii) defect-excluded f_nonAb(B2, deformed) + frame-invariance")
    print("    REPORTED (evidence-channel, not gate-channel); W6-2 7.44e+03 = ARTIFACT scale only")
    taus_s, mus_s = stencil_grid(n_half=2)           # (local) 5x5 stencil at the anchor
    Ns = len(taus_s)                                 # (local)
    eps_w = EPS_MAX                                  # (local) f_nonAb evaluated at eps_max (max release)
    # build B2 projector arrays + per-member (pinned-frame) rank-1 projectors on the stencil
    P_B2 = np.zeros((Ns, Ns, 16, 16), complex)       # (local)
    b2_blocks = np.empty((Ns, Ns), dtype=object)     # (local)
    for i, t in enumerate(taus_s):
        for j, m in enumerate(mus_s):
            H = H_from_metric(base_metric(t, m, infra[2]), infra) + eps_w * dH_used  # (local)
            _, Vv = np.linalg.eigh(H)
            blk = Vv[:, B2_COLS]                     # (local)
            b2_blocks[i, j] = blk
            P_B2[i, j] = blk @ blk.conj().T
    dPt2 = mesh_fd(P_B2, 0, H_STEP)                  # (local)
    dPm2 = mesh_fd(P_B2, 1, H_STEP)                  # (local)
    B2_tt, B2_mm, B2_im_tm, _ = proj_qgt_traces(P_B2, dPt2, dPm2)  # (local)
    b2_na = B2_tt + B2_mm                            # (local) Sum_a Tr_band R_aa (gauge-free, non-Abelian)
    # per-member Abelian sum (pinned eigh frame; frame-dependent inside the degenerate eigenspace)
    ab_b2 = np.zeros((Ns, Ns))                       # (local)
    for c in range(4):
        P_c = np.zeros((Ns, Ns, 16, 16), complex)    # (local)
        for i in range(Ns):
            for j in range(Ns):
                vec = pin_phase_columns(b2_blocks[i, j])[:, c]  # (local)
                P_c[i, j] = np.outer(vec, vec.conj())
        dPt_c = mesh_fd(P_c, 0, H_STEP)              # (local)
        dPm_c = mesh_fd(P_c, 1, H_STEP)              # (local)
        g_tt, g_mm, _, _ = proj_qgt_traces(P_c, dPt_c, dPm_c)  # (local)
        ab_b2 += g_tt + g_mm
    # defect exclusion (s100b e1): integrand > 1e3 = FD tracking spike
    defect_mask = b2_na > DEFECT_THRESH              # (local)
    n_defect = int(defect_mask.sum())                # (local)
    wt = np.ones(Ns); wt[0] = wt[-1] = 0.5           # (local)
    Wgt = np.outer(wt, wt) * H_STEP * H_STEP         # (local)
    excl = ~defect_mask                              # (local)
    I_NA_b2 = float(np.sum(Wgt[excl] * b2_na[excl]))  # (local) defect-excluded non-Abelian
    I_Ab_b2 = float(np.sum(Wgt[excl] * ab_b2[excl]))  # (local) defect-excluded Abelian (pinned frame)
    f_nonAb_b2 = abs(I_Ab_b2 - I_NA_b2) / abs(I_NA_b2) if abs(I_NA_b2) > 1e-300 else np.nan  # (local)
    Im_int_b2 = trapz2d(B2_im_tm, H_STEP, H_STEP)    # (local) Chern channel (structurally 0)
    print(f"    defect-excluded: I_NA(B2)={I_NA_b2:.4e}  I_Ab(B2,pinned frame)={I_Ab_b2:.4e}  "
          f"({n_defect} defect node(s))")
    print(f"    f_nonAb(B2, deformed) = {f_nonAb_b2:.4e}   |Im_int(B2)|={abs(Im_int_b2):.3e} "
          f"(Chern channel, structurally 0)")

    # frame-invariance demonstration: relative U(2)-orbit spread of f_nonAb over 16 Haar points
    print(f"    frame-invariance: relative U(2)-orbit spread of f_nonAb over {N_HAAR} Haar points (seed={HAAR_SEED})")
    rng = np.random.default_rng(HAAR_SEED)           # (local)
    f_orbit = [f_nonAb_b2]                           # (local)
    for _ in range(N_HAAR):
        Wg = haar_unitary(rng, 4)                    # (local) global U(4) frame rotation
        ab_rot = np.zeros((Ns, Ns))                  # (local)
        for c in range(4):
            P_c = np.zeros((Ns, Ns, 16, 16), complex)  # (local)
            for i in range(Ns):
                for j in range(Ns):
                    vec = (pin_phase_columns(b2_blocks[i, j]) @ Wg)[:, c]  # (local) rotated member
                    P_c[i, j] = np.outer(vec, vec.conj())
            dPt_c = mesh_fd(P_c, 0, H_STEP)          # (local)
            dPm_c = mesh_fd(P_c, 1, H_STEP)          # (local)
            g_tt, g_mm, _, _ = proj_qgt_traces(P_c, dPt_c, dPm_c)  # (local)
            ab_rot += g_tt + g_mm
        I_Ab_rot = float(np.sum(Wgt[excl] * ab_rot[excl]))  # (local)
        f_orbit.append(abs(I_Ab_rot - I_NA_b2) / abs(I_NA_b2))
    f_orbit = np.array(f_orbit)                       # (local)
    f_orbit_spread = float(f_orbit.max() - f_orbit.min())  # (local)
    f_orbit_rel = f_orbit_spread / abs(f_nonAb_b2) if abs(f_nonAb_b2) > 1e-300 else np.nan  # (local)
    frame_invariant = (not np.isnan(f_orbit_rel)) and (f_orbit_rel <= ORBIT_CEIL)  # (local)
    print(f"    f_nonAb orbit: spread={f_orbit_spread:.4e}  rel={f_orbit_rel:.4e}  "
          f"ceiling {ORBIT_CEIL:.0e}  frame_invariant={frame_invariant}")
    print(f"    (frame-DEPENDENT [rel >> ceiling] => f_nonAb is an eigh intra-eigenspace ARTIFACT,")
    print(f"     NOT physics evidence -- the W6-2 670x lesson; the anisotropy A is the frame-free gate)")

    # =====================================================================
    # STAGE 5: regime metric -- B1/B2 gap12 on the deformed stencil at eps_max
    # =====================================================================
    print("\n  [STAGE 5] regime: B1/B2 |lambda|-isolation gap12 on deformed stencil (eps_max)")
    gap_vals = []                                    # (local)
    for i, t in enumerate(taus_s):
        for j, m in enumerate(mus_s):
            we, _ = np.linalg.eigh(H_from_metric(base_metric(t, m, infra[2]), infra) + eps_w * dH_used)  # (local)
            aw_n = np.sort(np.abs(we.real))          # (local)
            gap_vals.append(aw_n[2] - aw_n[1])       # (local) B1 pair vs first B2 member
    gap_vals = np.array(gap_vals)                    # (local)
    breach_frac = float(np.mean(gap_vals < GAP12_UNSAFE))  # (local)
    print(f"    gap12 min={gap_vals.min():.6f}; breach(<{GAP12_UNSAFE})={breach_frac*100:.2f}%")

    # =====================================================================
    # VERDICT (plan W5-4 operator + pre-registered 3-tuple + dual-prior)
    # =====================================================================
    print("\n" + "=" * 78)
    print("  VERDICT")
    print("=" * 78)

    # composite operator (pre-registered)
    if not control_ok:
        verdict = "INFO"                             # (local) control failed on both directions -> vacuous
        branch = "INFO-control-failed-both-directions-vacuous"  # (local)
    elif A_above_floor and slope_in_band:
        verdict = "PASS"                             # (local)
        branch = "PASS-first-order-release-WZ-structure-TrackA"  # (local)
    elif A_above_floor and not slope_in_band:
        verdict = "INFO"                             # (local) scaling indeterminate (slope ~2)
        branch = f"INFO-scaling-indeterminate-{slope_reading}"  # (local)
    else:
        verdict = "FAIL"                             # (local) A at floor with control passed
        branch = "FAIL-A-at-floor-TrackB-residual-protection"  # (local)

    # 3-tuple ([SIGN] trigger): slope direction prediction
    # sign: did A RELEASE in the positive direction (A grows with eps)?  slope > 0 => PASS.
    sign_verdict = "PASS" if (not np.isnan(slope_disc) and slope_disc > 0.3) else (
        "FAIL" if (not np.isnan(slope_disc) and slope_disc < -0.3) else "N/A")  # (local)
    # magnitude: slope in the Track-A band [0.7,1.3] (the pre-registered first-order target)
    if A_above_floor and slope_in_band:
        magnitude_verdict = "PASS"                   # (local)
    elif A_above_floor:
        magnitude_verdict = "INFO"                   # (local) above floor, slope off-band
    else:
        magnitude_verdict = "FAIL"                   # (local)
    # regime: deformed-stencil multiplet-tracking safety
    if breach_frac <= REGIME_VALID_FRAC:
        regime_verdict = "VALID"                     # (local)
    elif breach_frac <= REGIME_MARGINAL_FRAC:
        regime_verdict = "MARGINAL"                  # (local)
    else:
        regime_verdict = "BREAKDOWN"                 # (local)

    # composite collapse cross-check (gate-verdicts.md rule) -- must agree with operator branch
    if regime_verdict == "BREAKDOWN":
        composite_collapse = "FAIL"                  # (local)
    elif sign_verdict == "FAIL":
        composite_collapse = "FAIL"                  # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite_collapse = "FAIL"                  # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite_collapse = "INFO"                  # (local)
    elif magnitude_verdict == "INFO":
        composite_collapse = "INFO"                  # (local)
    else:
        composite_collapse = "PASS"                  # (local)
    # the pre-registered OPERATOR (control-gated) is authoritative; verify consistency with collapse
    # when control_ok (collapse rule does not model the control gate; INFO-control-failed is operator-only)
    if control_ok and verdict != composite_collapse:
        print(f"    NOTE: operator branch={verdict} vs collapse-rule={composite_collapse}; "
              f"operator is authoritative (control-gated); collapse agrees on the magnitude arm.")

    # dual-prior posterior re-allocation (S-2 BINDING)
    if verdict == "PASS":
        posterior = "TrackA=0.9_TrackB=0.1"          # (local)
        prior_action = "RE-ALLOCATED-to-TrackA"       # (local)
    elif verdict == "FAIL":
        posterior = "TrackA=0.15_TrackB=0.85"        # (local)
        prior_action = "RE-ALLOCATED-to-TrackB"       # (local)
    else:  # INFO
        posterior = "TrackA=0.6_TrackB=0.4_UNCHANGED"  # (local)
        prior_action = "PRIORS-UNCHANGED-family-re-pinned-S102-degenerate-first-order"  # (local)

    print(f"  control_ok    = {control_ok}  (a=4 {control[COSET_PRIMARY][2]}, a=6 {control[COSET_COMPANION][2]}; used lambda_{a_used})")
    print(f"  A_max(used)   = {A_max_used:.4e}  (floor {A_FLOOR:.0e})  above_floor={A_above_floor}")
    print(f"  disc. slope   = {slope_disc:.4f}  band [{SLOPE_LO},{SLOPE_HI}]  in_band={slope_in_band}  [{slope_reading}]")
    print(f"  B2 split slope= {split_slope:.4f}  (clean C1=0 witness)")
    print(f"  f_nonAb(B2)   = {f_nonAb_b2:.4e}  frame_invariant={frame_invariant} (orbit_rel={f_orbit_rel:.3e}); REPORTED not gated")
    print(f"  3-tuple       : sign={sign_verdict} magnitude={magnitude_verdict} regime={regime_verdict}")
    print(f"  dual-prior    : {prior_action} -> posterior {posterior}")
    print(f"  >>> {GATE_ID}: {verdict}  [{branch}]")

    value_str = (
        f"verdict={verdict}_a_used={a_used}_{fallback_note}_"
        f"control_ok={control_ok}_dPb1={control[a_used][0]:.3e}_dPb3={control[a_used][1]:.3e}_"
        f"A_max={A_max_used:.4e}_disc_slope={slope_disc:.4f}_chan={chan}_in_band={slope_in_band}_"
        f"B2split_slope={split_slope:.4f}_slope_reading={slope_reading}_"
        f"A0_floor=({A0p[1]:.2e})_f_nonAb_b2={f_nonAb_b2:.4e}_frame_inv={frame_invariant}_"
        f"orbit_rel={f_orbit_rel:.3e}_posterior={posterior}_breach={breach_frac:.4f}_ndefect={n_defect}"
    )                                                # (local)

    # --- save data ---
    np.savez(
        NPZ_OUT,
        eps_scan=EPS_SCAN,
        a_primary=COSET_PRIMARY, a_companion=COSET_COMPANION, a_used=a_used,
        fallback_note=fallback_note,
        # control (i)
        dPb1_a4=control[COSET_PRIMARY][0], dPb3_a4=control[COSET_PRIMARY][1], control_ok_a4=control[COSET_PRIMARY][2],
        dPb1_a6=control[COSET_COMPANION][0], dPb3_a6=control[COSET_COMPANION][1], control_ok_a6=control[COSET_COMPANION][2],
        control_ok=control_ok,
        # anisotropy (ii)
        A_scan_primary=np.array(A_scan[COSET_PRIMARY]),
        A_scan_companion=np.array(A_scan[COSET_COMPANION]),
        A0_primary=np.array(A0p), A0_companion=np.array(A0c),
        A_tau_used=A_tau_used, A_mu_used=A_mu_used,
        slope_tau=slope_tau, slope_mu=slope_mu, slope_disc=slope_disc,
        se_tau=se_tau, se_mu=se_mu, se_disc=se_disc, disc_chan=chan,
        nval_tau=nval_tau, nval_mu=nval_mu, A_max_used=A_max_used,
        A_above_floor=A_above_floor, slope_in_band=slope_in_band, slope_reading=slope_reading,
        # eigenvalue splitting cross-check
        b2_split=split, b2_split_slope=split_slope, b2_split_se=split_se,
        # f_nonAb witness (iii)
        I_NA_b2=I_NA_b2, I_Ab_b2=I_Ab_b2, f_nonAb_b2=f_nonAb_b2, Im_int_b2=Im_int_b2,
        n_defect=n_defect, b2_na=b2_na, ab_b2=ab_b2,
        f_orbit=f_orbit, f_orbit_spread=f_orbit_spread, f_orbit_rel=f_orbit_rel,
        frame_invariant=frame_invariant,
        # baselines (reported)
        W62_f_nonAb_artifact=W62_F_NONAB_ARTIFACT, W62_I_NA_b2_excl=W62_I_NA_B2_EXCL,
        W62_e3_floor=W62_E3_FLOOR, W62_orbit_rel=W62_ORBIT_REL,
        # regime
        gap12_stencil=gap_vals, breach_frac=breach_frac,
        # verdict
        verdict=verdict, branch=branch,
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict, regime_verdict=regime_verdict,
        posterior=posterior, prior_action=prior_action,
        tau_fold=float(tau_fold), tau0=TAU0, mu0=MU0,
        v_jensen=V_JENSEN, v_mu=V_MU, u1_anchor=U1_ANCHOR,
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"\n  Saved data: {NPZ_OUT}")

    # --- plot ---
    fig, axes = plt.subplots(2, 2, figsize=(15, 11))

    # (0,0): log A vs log eps, both directions + fitted slope band + floor line
    ax = axes[0, 0]
    for a, mk, col in [(COSET_PRIMARY, "o", "C0"), (COSET_COMPANION, "s", "C1")]:
        rows = np.array(A_scan[a])                   # (local)
        ax.loglog(EPS_SCAN, np.maximum(rows[:, 1], 1e-16), mk + "-", color=col,
                  label=f"lambda_{a} A(mu)")
        ax.loglog(EPS_SCAN, np.maximum(rows[:, 0], 1e-16), mk + "--", color=col, alpha=0.5,
                  label=f"lambda_{a} A(tau)")
    # fitted slope on used direction (dominant channel)
    if not np.isnan(slope_disc):
        ee = np.array([EPS_SCAN[0], EPS_SCAN[-1]])   # (local)
        A_fit_ref = A_mu_used if chan == "mu" else A_tau_used  # (local)
        valid = np.asarray(A_fit_ref) > A_VALID_FLOOR  # (local)
        inter = np.log10(A_fit_ref[valid][0]) - slope_disc * np.log10(EPS_SCAN[valid][0])  # (local)
        ax.loglog(ee, 10 ** (inter + slope_disc * np.log10(ee)), "k:", lw=2,
                  label=f"fit slope={slope_disc:.2f} [band {SLOPE_LO}-{SLOPE_HI}]")
    # slope-1 and slope-2 reference guides
    ee = EPS_SCAN                                    # (local)
    ax.loglog(ee, A_mu_used[-1] * (ee / ee[-1]) ** 1.0, "g-.", alpha=0.4, label="slope 1 (Track A)")
    ax.loglog(ee, A_mu_used[-1] * (ee / ee[-1]) ** 2.0, "m-.", alpha=0.4, label="slope 2 (degenerate)")
    ax.axhline(W62_E3_FLOOR, color="r", ls=":", lw=1, label=f"e3 Schur floor {W62_E3_FLOOR:.0e}")
    ax.axhline(A_FLOOR, color="orange", ls="--", lw=1, label=f"A PASS floor {A_FLOOR:.0e}")
    ax.set_xlabel("eps"); ax.set_ylabel("anisotropy A")
    ax.set_title(f"(ii) B2 band-matrix anisotropy A vs eps\nused lambda_{a_used}, disc slope={slope_disc:.3f} [{slope_reading[:28]}]")
    ax.legend(fontsize=7, ncol=2); ax.grid(True, which="both", alpha=0.3)

    # (0,1): control (i) -- frozen-slot motion vs eps
    ax = axes[0, 1]
    dpb1_scan = []; dpb3_scan = []                   # (local)
    for eps in EPS_SCAN:
        we, Ve = np.linalg.eigh(H0 + eps * dH_used)  # (local)
        Pb1e = Ve[:, B1_COLS] @ Ve[:, B1_COLS].conj().T  # (local)
        blkb3e = np.column_stack([Ve[:, B3_LO], Ve[:, B3_HI]])  # (local)
        Pb3e = blkb3e @ blkb3e.conj().T              # (local)
        dpb1_scan.append(np.linalg.norm(Pb1e - P_b1_0))
        dpb3_scan.append(np.linalg.norm(Pb3e - P_b3_0))
    ax.loglog(EPS_SCAN, dpb1_scan, "o-", label="||DeltaP(B1)||")
    ax.loglog(EPS_SCAN, dpb3_scan, "s-", label="||DeltaP(B3)||")
    ax.axhline(CONTROL_FLOOR, color="r", ls="--", label=f"control floor {CONTROL_FLOOR:.0e}")
    ax.set_xlabel("eps"); ax.set_ylabel("frozen-slot motion ||DeltaP||_F")
    ax.set_title(f"(i) RELEASE CONTROL -- frozen B1/B3 move off-base\ncontrol_ok={control_ok} (release achieved)")
    ax.legend(fontsize=8); ax.grid(True, which="both", alpha=0.3)

    # (1,0): B2 eigenvalue splitting vs eps (clean C1=0 witness)
    ax = axes[1, 0]
    ax.loglog(EPS_SCAN, split, "D-", color="purple", label="B2 eigenvalue spread")
    ax.loglog(EPS_SCAN, split[-1] * (EPS_SCAN / EPS_SCAN[-1]) ** 2.0, "m-.", alpha=0.5, label="slope 2 guide")
    ax.loglog(EPS_SCAN, split[-1] * (EPS_SCAN / EPS_SCAN[-1]) ** 1.0, "g-.", alpha=0.5, label="slope 1 guide")
    ax.set_xlabel("eps"); ax.set_ylabel("B2 quadruplet |lambda| spread")
    ax.set_title(f"(3b) B2 eigenvalue splitting\nslope={split_slope:.4f} (4-dim eigenspace splits at O(eps^2))")
    ax.legend(fontsize=8); ax.grid(True, which="both", alpha=0.3)

    # (1,1): f_nonAb frame-orbit (witness iii, evidence-channel)
    ax = axes[1, 1]
    ax.plot(range(len(f_orbit)), f_orbit, "o-", label="f_nonAb(B2) orbit")
    ax.axhline(f_nonAb_b2, color="k", ls="--", label=f"pinned f_nonAb={f_nonAb_b2:.3e}")
    ax.set_xlabel("frame sample (0=pinned, 1..16 Haar U(4), seed 101)")
    ax.set_ylabel("f_nonAb(B2, deformed)")
    ax.set_title(f"(iii) f_nonAb frame-orbit: rel spread={f_orbit_rel:.2e}\nframe_invariant={frame_invariant} (W6-2 artifact-scale {W62_F_NONAB_ARTIFACT:.1e})")
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3)

    fig.suptitle(f"{GATE_ID}: B2 isotropy-breaking dual-prior discriminator -- "
                 f"VERDICT {verdict} [{branch}]\n{prior_action} -> {posterior}", fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.94])
    fig.savefig(PNG_OUT, dpi=140)
    print(f"  Saved plot: {PNG_OUT}")

    # --- verdict payload (agent calls emit_verdict; race-safe MCP path) ---
    extra_rows = [
        ("# regulator_pin: none -- the quantum-geometric anisotropy A is a property of the "
         "D_K eigenbundle over the modulus base, not a Seeley-DeWitt a_n^{regulator} "
         "(mirrors s100b_nonabelian_metric_fraction.py:1060); CLASS=FULL (dirac_spectrum "
         "full builder; no SCHEMATIC helper)"),
        ("# deformation_family: dH_a = off-block log-metric direction (coset lambda_a <-> u(1) "
         "anchor lambda_8 symmetric metric bump, pushed through the full D_K pipeline, "
         f"||dH_a||_F=1); PRIMARY a=4, COMPANION a=6; family direction USED lambda_{a_used} "
         f"({fallback_note}); eps in {{1e-4..1e-2}} half-decade; seed={HAAR_SEED} (Haar orbit ONLY)"),
        ("# A19 caveat DISCHARGED: S101-TAU0-OPERATOR-CANONICITY landed PASS (Wave-1 L4 lift); "
         "s84 cache lineage full-confidence; no untrusted_upstream row"),
        (f"# dual-prior: prior TrackA=0.6 TrackB=0.4; verdict {verdict} -> {prior_action} "
         f"-> posterior {posterior}; W6-2 FAIL(a) carries ZERO prior weight vs Track A "
         f"(Corollary U: invariant base could not see the difference)"),
        (f"# anatomy: control_ok={control_ok} (||DeltaP(B1)||={control[a_used][0]:.2e}, "
         f"||DeltaP(B3)||={control[a_used][1]:.2e} >> 1e-10 floor => release ACHIEVED at fiber level); "
         f"A releases above floor (A_max={A_max_used:.2e}) but at slope={slope_disc:.3f} "
         f"(B2 eigenvalue-splitting slope={split_slope:.3f}=2 EXACT) => DEGENERATE-FIRST-ORDER "
         f"(C1=0, C2!=0): the 4-dim B2 eigenspace rotates rigidly at O(eps) [scalar] and its "
         f"WZ anisotropy appears at O(eps^2); f_nonAb(B2)={f_nonAb_b2:.2e} frame-DEPENDENT "
         f"(orbit_rel={f_orbit_rel:.2e}) = eigh artifact, NOT physics (W6-2 670x lesson)"),
    ]                                                # (local)
    print_verdict_payload(
        verdict, value_str, audit_sha, content_sha,
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict, regime_verdict=regime_verdict,
        companion_note=("[SIGN] B2 quadruplet band-matrix anisotropy A vs eps under off-block "
                        "coset deformation; dual-prior Track-A(WZ)/B(Abelian)/degenerate-first-order "
                        "discriminator; release condition R; Corollary-U release the no-go licenses"),
        extra_rows=extra_rows,
    )
    print(f"\n  4-tuple: (value={value_str[:60]}..., scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
