#!/usr/bin/env python3
"""
S100a W2-4 -- S100a-CONNES-DISTANCE-LADDER
==========================================
Connes geodesic distances between generation-states on the multiplicity bundle:
the regulator-invariant route to the charged-lepton envelope.

Gate ID:        S100a-CONNES-DISTANCE-LADDER
Trigger:        [SIGN]
Classification: GEOMETRIC
Agent:          connes-ncg-theorist
Plan:           sessions/session-plan/session-100a-plan-w2.md SecW2-4 (R3 YAML)
Scheme:         CONNES-DISTANCE-MULTIPLICITY-BUNDLE
                (S88-CONNES-DISTANCE-FINITE-SPECTRUM-IDENTITY machinery lineage)
Convention:     substrate-state-pair-canonical (inherited from S88;
                functional-INDEPENDENT -- the Connes distance is regulator-invariant)

PRE-REGISTERED HYPOTHESIS (plan SecW2-4):
  The Connes geodesic distances d_i between generation-states on the multiplicity
  bundle (finite D_F / greybody-reweighted metric) reproduce the SAME charged-lepton
  e-vs-heavy envelope (~8 e-fold spread) as the Item-6 overlap integral via
  mass = e^{-d_i/ell}, with the widening in [1.80, 1.89] -- an INDEPENDENT,
  regulator-invariant route to the same envelope.

PASS-conjunction (operator block, frozen at plan-freeze):
  (i)   sign(d_e - d_heavy) > 0  AND  mass = e^{-d/ell} => m_e < m_heavy
        (e most distant; FAIL-mode of the gate = generation-DEGENERATE d_i)
  (ii)  |ln(m_max/m_min)| ~= 8 within +-2   (predicted spread in [6, 10] e-folds)
  (iii) widening W_Connes = (d_e - d_mu)/(d_mu - d_tau) in [1.80, 1.89]

CONSTRUCTION (frozen BEFORE compute; derivation in the substitution chain below):

  Finite real spectral triple (A_mult, H_F, D_F; J, gamma):

    A_mult = self-adjoint part of C^4 -- the CHANNEL ALGEBRA of the multiplicity
        bundle on the 4 channels {v = (0,0) vacuum/Higgs reference;
        g1 = (1,0); g2 = (1,1); g3 = (3,0)} (the triality-distinct generation
        tower + reference). Per SecVII.BL (Generation-Blindness Obstruction,
        STAGE-3-PERMANENT) A_K acts as the IDENTITY on the multiplicity index,
        so the metric-bearing algebra ON the multiplicity bundle is the channel
        function algebra: the canonical Iochum-Krajewski-Martinetti finite-point
        setting in which the Connes distance is FINITE and REGULATOR-FREE.
        (Contrast: the S87/S88 machinery gate S88-CONNES-DISTANCE-FINITE-
        SPECTRUM-IDENTITY = 0.9800418463588636 closed CLASS-gamma BECAUSE the
        full M_n(C) algebra makes the distance regulator-divergent -- any f(D^2)
        commutes with D. The commutative channel restriction is the structural
        cure, and the R-sweep below DEMONSTRATES the resulting invariance.)

    H_F = C^2_chirality (x) C^4_channels (x) C^2_{particle/antiparticle} = C^16.

    D_F = greybody-reweighted chiral star:
        D_F = [[0, S],[S, 0]]_particle  (+)  [[0, S_bar],[S_bar, 0]]_antiparticle
        S = star matrix on the channels: S[v, g] = S[g, v] = t_g, else 0,
        t_g = kappa / omega_g,   omega_g = lambda_g(tau_fold)^2,
        lambda_g = min |eigenvalue| of the (p,q)=g sector of D_K at tau_fold
        (L=12 master cache; the channel's spectral floor). kappa = 1 in cache
        units (one overall metric scale, absorbed into ell -- NOT a parameter).
        The antiparticle star S_bar uses the CONJUGATE sectors (0,1),(1,1),(0,3),
        whose floors equal the tower floors EXACTLY (BDI conjugate-pair theorem)
        => [J, D_F] = 0 by construction (verified numerically).

    J = (particle <-> antiparticle block swap) o complex conjugation;
    gamma = diag(+1_L, -1_R) (+) diag(-1_L, +1_R).
    KO-dim 6 sign triple (eps, eps', eps'') = (+1, +1, -1):
        J^2 = +1, J D_F = D_F J, J gamma = -gamma J  (all verified numerically).
    First-order condition: the multiplicity-bundle star inherits the framework's
        standing order-one obstruction (any D that RESOLVES generations must act
        on the multiplicity index, OUTSIDE every A_K-bimodule -- SecVII.BL);
        the residual is computed and REPORTED, not asserted zero. The Connes
        distance formula requires only (A, H, D); J enters as the compatibility
        constraint [J, D_F] = 0, which HOLDS.

  GREYBODY REWEIGHTING (why t_g = 1/omega_g, frozen a priori):
    The S99 fermion-mass panel four-lens synthesis pinned ONE modulus exponent in
    three languages:  d_i/ell  <->  2*pi*omega_i/kappa_grey  <->  k*C2(p,q).
    The Connes-metric realization of d_i linear in the channel D^2-floor
    (omega_i = lambda_i^2, the spectral-action energy variable, ~ C2 at
    undeformed scaling) is the star with t_g = kappa/omega_g, because the star
    closed form gives d(v, g) = 1/t_g = omega_g EXACTLY. The quantum-foam
    reading: the foam-mediated coupling of the reference channel to generation
    channel g is propagator-suppressed ~ 1/omega_g (higher channels transmit
    less -- greybody suppression); the suppressed coupling makes the high-C2
    channel the MOST DISTANT state, hence (mass = e^{-d/ell}) the LIGHTEST.
    At undeformed Casimir scaling omega ~ C2 = (4/3, 3, 6) the widening is
    (6-3)/(3-4/3) = 9/5 = 1.800 -- EXACTLY the plan's Casimir floor. The Jensen
    deformation of the actual floors at tau_fold supplies the correction the
    plan's band [1.80, 1.89] tests.

  STAR CLOSED FORMS (exact theorem, the SDP cross-check target):
    For the chiral star with diagonal channel algebra,
       ||[D_F, pi(a)]||_op = sqrt( sum_g t_g^2 (a_g - a_v)^2 ),
    hence  d_C(omega_v, omega_g) = 1/t_g = omega_g
    and    d_C(omega_g, omega_h) = sqrt(1/t_g^2 + 1/t_h^2)
                                 = sqrt(omega_g^2 + omega_h^2)   (Pythagorean).
    Proof: [S, diag(a)] = |v><x| - |x><v| with x_g = t_g(a_g - a_v), op norm
    ||x||_2; maximize (a_g - a_v) subject to ||x|| <= 1 by flattening the other
    legs; pairwise by Cauchy-Schwarz. The chiral doubling [[0,S],[S,0]] and the
    J-doubling preserve the norm (equal blocks).

  LADDER DISAMBIGUATION (frozen): the verdict-bearing d_i are the VACUUM-
    REFERENCED distances d_i = d_C(omega_v, omega_{g_i}) -- the mass map
    mass_i = e^{-d_i/ell} requires one common reference, and the vacuum/Higgs
    channel is the same reference object as Item-6's |s(h)|^2 overlap. The
    N_eval "2 adjacent Connes distances" = the two adjacent LADDER GAPS
    Delta_1 = d_e - d_mu, Delta_2 = d_mu - d_tau entering the widening. The
    PAIRWISE adjacent distances d_C(e,mu), d_C(mu,tau) (Pythagorean, NOT gaps)
    are computed and reported as a SECONDARY diagnostic (not verdict-bearing).

SUBSTITUTION CHAIN (math-scripts.md, mandatory for [SIGN]):
  Claim: non-degenerate ladder with e = argmax d (most distant => lightest),
         spread ~ 8 e-folds under the one-parameter ell-calibration,
         widening W_Connes in [1.80, 1.89].
  Step 1 (metric):   d(omega_i, omega_j) = sup{ |omega_i(a) - omega_j(a)| :
                       a in A_mult, ||[D_F, pi(a)]||_op <= 1 }     [Connes 1989]
  Step 2 (D_F):      t_g = kappa/omega_g, omega_g = lambda_g(tau_fold)^2
                       [greybody/foam transmission ~ 1/omega; S99 four-lens]
  Step 3 (closed):   d_g := d(omega_v, omega_g) = 1/t_g = omega_g/kappa
                       [star theorem above; SDP must reproduce to rtol 1e-6]
  Step 4 (Casimir):  omega_g ~ C2(g) at undeformed scaling
                       => W = (C2(3,0)-C2(1,1))/(C2(1,1)-C2(1,0)) = 3/(5/3)
                          = 9/5 = 1.800 exactly; Jensen deformation corrects.
  Step 5 (mass map): m = e^{-d/ell}, d(mass)/d(d) = -(1/ell) e^{-d/ell} < 0
                       for ell > 0  => largest d = lightest mass
                       => e-channel = argmax omega_g = (3,0) PREDICTED
                       (cache floor ordering lambda_(1,0) < lambda_(1,1) <
                        lambda_(3,0) strict => ladder strict, non-degenerate).
  Direction:  sign(d_e - d_heavy) = sign(omega_max - omega_min) > 0  [strict
              Casimir grading preserved by the Jensen deformation -- verified
              from the cache, not assumed]. Spread = (d_max - d_min)/ell_fit
              in [6,10]; W_Connes in [1.80, 1.89] iff the deformed quadratic
              floors keep the gap ratio within [0%, +5%] of the Casimir value.
  Conclusion: PASS iff (i) ^ (ii) ^ (iii); the gate's pre-registered FAIL mode
              is DEGENERACY (multiplicity-blindness re-confirmed); INFO mode is
              envelope-reproduced-but-widening-outside-band.

ell-CALIBRATION (frozen): mass_i = e^{-d_i/ell} predicts mass RATIOS only; the
  unique pairing-independent one-parameter least-squares is the CENTERED OLS
  slope of ln m_i^PDG on d_i (the centering constant is the non-physical overall
  scale, dropping out of every ratio): b = Sxy/Sxx, ell = -1/b. Two alternative
  pairings (tau-anchored cumulative; adjacent-gap) are reported as sensitivity
  diagnostics, NOT verdict-bearing. PDG anchors: m_e, m_mu, m_tau_PDG from
  canonical_constants (m_tau_PDG = 1.77686 GeV added S100a with provenance;
  the canonical m_tau = 2.062 is the S42 MODULUS mass in M_KK units -- a name
  collision, NEVER a PDG target).

VERDICT RUBRIC (frozen):
  crit_i   : non-degenerate [(d_max-d_min)/d_max >= 1e-6] AND strict pairwise
             ladder gaps [rel >= 1e-6] AND ell_fit > 0          -> sign_verdict
  crit_ii  : spread_pred = (d_max-d_min)/ell_fit in [6.0, 10.0]
  crit_iii : W_Connes in [1.80, 1.89]
  magnitude_verdict: PASS iff ii ^ iii; INFO iff ii ^ (not iii) [plan INFO
             branch: "envelope reproduced but widening outside band"];
             FAIL iff not ii.
  regime_verdict: VALID iff all SDP statuses in {optimal, optimal_inaccurate}
             AND max|d_SDP - d_closed|/d_closed < 1e-6 AND R-sweep max rel
             dev < 1e-8 AND doubling-invariance dev < 1e-6 AND KO-sign checks
             pass; MARGINAL iff statuses ok AND max closed-form dev < 1e-3;
             else BREAKDOWN.
  composite: canonical schema-v2 collapse rule (gate-verdicts.md).

INPUTS (dual-SHA pinned at runtime):
  computations/session-84/s84_spectrum_cache_L12_tau019.npz   [STATIC pin
      9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9 --
      HARD FAIL on mismatch]
  computations/_shared/canonical_constants.py                 [runtime]
  computations/session-100a/s100a_yukawa_overlap_offdiag.npz  [Item-6 OPTIONAL
      cross-check input; LANDED (verdict INFO); enables the same-envelope-
      two-ways coincidence test]
  S88 machinery value pin: S88-CONNES-DISTANCE-FINITE-SPECTRUM-IDENTITY
      = 0.9800418463588636 (literal pin in the audit pinmap)

OUTPUTS:
  computations/session-100a/s100a_connes_distance_ladder.npz
  computations/session-100a/s100a_connes_distance_ladder.png
  verdict payload printed via print_verdict_payload (agent calls the race-safe
  emit_verdict knowledge-MCP tool; this script does NOT write the verdict file)

PLAN-TEXT-DRIFT NOTE (substrate-first-canonical-sourcing Sec(ii.B)): the plan's
  prose pin "(1,0) dim=3 |lambda|_min=1.32766" misquotes the cache MAX of that
  sector (1.327661); the runtime ground truth minimum is 0.83589351 (the same
  value Item-6 consumed). Documented here + in the WP methodology subsection.

Substrate framing (GEOMETRIC): the Connes geodesic distance IS the intrinsic
  metric of the fabric's finite internal structure. The substrate IS the finite
  spectral triple; the three generations are three states on its multiplicity
  bundle; their distances from the vacuum/Higgs channel are the substrate's own
  notion of how far apart the generation channels sit. mass = e^{-d/ell}
  converts geodesic separation into mass: the electron is the MOST distant
  state. Flow: D_K sector floors -> greybody-reweighted star D_F -> Connes
  distances d_i -> mass envelope. No container, no imposed hierarchy.
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

SESSION = "100a"                                                   # (local)
GATE_ID = "S100a-CONNES-DISTANCE-LADDER"                           # (local)
SCHEME = "CONNES-DISTANCE-MULTIPLICITY-BUNDLE"                     # (local)
CONVENTION = "substrate-state-pair-canonical"                      # (local)
L_MAX = 12                                                         # (local)

# Pre-registered bands / tolerances (plan SecW2-4 machinery_pin_map)
W_BAND_LO = 1.80               # widening band lower edge (Casimir 9/5)  # (local)
W_BAND_HI = 1.89               # widening band upper edge (PDG-tilt)     # (local)
SPREAD_LO = 6.0                # e-fold spread band: 8 - 2               # (local)
SPREAD_HI = 10.0               # e-fold spread band: 8 + 2               # (local)
DEGEN_FLOOR_REL = 1e-6         # non-degeneracy floor (2 OOM above SDP rtol)  # (local)
SDP_TOL = 1e-8                 # Connes sup-norm optimisation rtol (plan pin)  # (local)
CLOSED_DEV_VALID = 1e-6        # SDP-vs-closed-form rel dev: VALID ceiling     # (local)
CLOSED_DEV_MARGINAL = 1e-3     # SDP-vs-closed-form rel dev: MARGINAL ceiling  # (local)
RSWEEP_DEV_VALID = 1e-8        # regulator-invariance rel-dev ceiling          # (local)
R_SWEEP_FACTORS = (10.0, 100.0, 1000.0)   # Frobenius bounds x max(omega)      # (local)

# Cross-session machinery pin (plan SecW2-4 + Wave-2 Input-SHA ledger)
S88_MACHINERY_VALUE = 0.9800418463588636   # S88-CONNES-DISTANCE-FINITE-SPECTRUM-IDENTITY (INFO, CLASS-gamma)  # (local)

# Tower (triality-distinct generation channels) + conjugates + reference
TOWER = [(1, 0), (1, 1), (3, 0)]           # (local) generation channels
TOWER_CONJ = [(0, 1), (1, 1), (0, 3)]      # (local) BDI conjugate sectors
REF_SECTOR = (0, 0)                        # (local) vacuum/Higgs reference channel
C2_TOWER = [4.0 / 3.0, 3.0, 6.0]           # (local) SU(3) quadratic Casimirs
W_CASIMIR_IDEAL = 9.0 / 5.0                # (local) undeformed-scaling widening floor

# Static input pin (plan SecW2-4 input_files; 64-hex, transcribed verbatim from
# sessions/session-plan/session-100a-plan-w2.md line 767)
SPECTRUM_CACHE_SHA_PIN = "9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9"

OUT_NPZ = _HERE / "s100a_connes_distance_ladder.npz"
OUT_PNG = _HERE / "s100a_connes_distance_ladder.png"

SPECTRUM_CACHE = PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
ITEM6_NPZ = _HERE / "s100a_yukawa_overlap_offdiag.npz"
CANONICAL_CONSTS = _SHARED / "canonical_constants.py"
INPUT_FILES = [SPECTRUM_CACHE, CANONICAL_CONSTS, ITEM6_NPZ]


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
    # Literal machinery pin (plan audit_discriminators: pinmap includes the
    # S88 machinery value as a cited cross-session constant)
    pins["S88-CONNES-DISTANCE-FINITE-SPECTRUM-IDENTITY"] = repr(S88_MACHINERY_VALUE)
    print(f"  S88-CONNES-DISTANCE-FINITE-SPECTRUM-IDENTITY={S88_MACHINERY_VALUE!r} (literal pin)")
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
    Session is the letter-suffixed string '100a' (tool schema accepts str)."""
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
# Section 5 -- Spectrum loading: channel floors at tau_fold (L=12 cache)
# ---------------------------------------------------------------------------
def load_floors():
    """Load the per-sector spectral floors lambda_g = min|eigenvalue| for the
    tower, the conjugate sectors, and the reference channel. HARD FAIL if the
    cache SHA does not match the plan's static pin."""
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

    floors = np.array([floor_of(k) for k in TOWER], dtype=np.float64)        # (local)
    floors_conj = np.array([floor_of(k) for k in TOWER_CONJ], dtype=np.float64)  # (local)
    floor_ref = floor_of(REF_SECTOR)  # (local) context only (reference is a state)
    n_sectors = len(sec)  # (local)
    return floors, floors_conj, floor_ref, n_sectors


# ---------------------------------------------------------------------------
# Section 6 -- Finite real spectral triple: J-doubled greybody star
# ---------------------------------------------------------------------------
def build_star(t):
    """4x4 Hermitian star matrix: node 0 = vacuum reference, nodes 1..3 =
    generation channels; S[0,g] = S[g,0] = t[g-1]."""
    S = np.zeros((4, 4), dtype=np.float64)  # (local)
    for g in range(3):
        S[0, g + 1] = t[g]
        S[g + 1, 0] = t[g]
    return S


def build_triple(t_part, t_anti):
    """Build the J-doubled chiral star D_F (16x16), gamma, J (as a real
    permutation matrix composed with conjugation), and the channel-projector
    embedding for pi(a).

    Layout: index = copy*8 + chir*4 + channel, copy in {0=particle, 1=anti},
    chir in {0=L, 1=R}, channel in {0=v,1=g1,2=g2,3=g3}."""
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

    # gamma: diag(+1_L, -1_R) on particle; OPPOSITE on antiparticle (eps''=-1)
    g8 = np.diag([1.0] * 4 + [-1.0] * 4)  # (local)
    gamma = np.block([
        [g8, np.zeros((8, 8))],
        [np.zeros((8, 8)), -g8],
    ])  # (local)

    # J = Sigma o K with Sigma = particle<->antiparticle swap (real permutation)
    Sigma = np.zeros((16, 16))  # (local)
    Sigma[0:8, 8:16] = np.eye(8)
    Sigma[8:16, 0:8] = np.eye(8)

    # Channel projectors E_k (16x16): diagonal over chirality + copies
    E = []  # (local)
    for ch in range(4):
        e = np.zeros(16)  # (local)
        for copy in range(2):
            for chir in range(2):
                e[copy * 8 + chir * 4 + ch] = 1.0
        E.append(np.diag(e))
    return D_F, gamma, Sigma, E, D_p


def ko_sign_checks(D_F, gamma, Sigma):
    """Numerical KO-dim-6 sign checks for J = Sigma o K (real matrices: K acts
    trivially on the real D_F, gamma; J^2 = Sigma^2)."""
    eps_J2 = float(np.max(np.abs(Sigma @ Sigma - np.eye(16))))          # (local) J^2 = +1
    comm_JD = float(np.max(np.abs(Sigma @ D_F - D_F @ Sigma)))          # (local) [J, D] = 0
    anti_Jg = float(np.max(np.abs(Sigma @ gamma + gamma @ Sigma)))      # (local) J gamma = -gamma J
    odd_Dg = float(np.max(np.abs(gamma @ D_F + D_F @ gamma)))           # (local) gamma D = -D gamma
    return eps_J2, comm_JD, anti_Jg, odd_Dg


def first_order_residual(D_F, E):
    """Max ||[[D_F, pi(a)], pi(b)^o]||_op over canonical channel projectors
    (b^o = J pi(b)* J^-1 = pi(b) for this layout). REPORTED, not asserted zero:
    a generation-resolving D_F on the multiplicity bundle sits outside every
    A_K-bimodule (SecVII.BL); this is the standing order-one obstruction."""
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

        max  (a_i - a_j)   s.t.  || [D_op, pi(a)] ||_op <= 1,
        pi(a) = sum_k x_k E_k,  gauge-fix x_j = 0 (kills the constant flat
        direction; the star graph is connected so the feasible set is compact).

    Optional Frobenius bound ||pi(a)||_F <= frob_bound for the R-sweep
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

    # BDI conjugate-pair iso-spectrality (reality constraint feeds [J,D_F]=0)
    bdi_dev = float(np.max(np.abs(floors - floors_conj) / floors))  # (local)
    print(f"  BDI conjugate-floor max rel dev: {bdi_dev:.3e}")

    # Strict floor ordering (Casimir grading preserved by the Jensen deformation)
    strict_floor_order = bool(floors[0] < floors[1] < floors[2])  # (local)
    print(f"  strict floor ordering lambda(1,0) < lambda(1,1) < lambda(3,0): {strict_floor_order}")

    # D^2-floors (the spectral-action energy variable) + greybody couplings
    omega = floors ** 2          # (local) channel D^2-floors
    omega_conj = floors_conj ** 2  # (local)
    t_part = 1.0 / omega         # (local) greybody-reweighted couplings (kappa=1)
    t_anti = 1.0 / omega_conj    # (local)
    print(f"  omega_g = lambda_g^2: {omega[0]:.9f}, {omega[1]:.9f}, {omega[2]:.9f}")
    print(f"  greybody couplings t_g = 1/omega_g: {t_part[0]:.6f}, {t_part[1]:.6f}, {t_part[2]:.6f}")

    # Build the J-doubled triple + KO-dim-6 sign checks
    D_F, gamma, Sigma, E, D_p = build_triple(t_part, t_anti)
    eps_J2, comm_JD, anti_Jg, odd_Dg = ko_sign_checks(D_F, gamma, Sigma)
    print(f"  KO-dim-6 checks: |J^2-1|={eps_J2:.3e}  ||[J,D_F]||={comm_JD:.3e}  "
          f"||{{J,gamma}}||={anti_Jg:.3e}  ||{{gamma,D_F}}||={odd_Dg:.3e}")
    ko_ok = bool(eps_J2 < 1e-12 and comm_JD < 1e-12 and anti_Jg < 1e-12 and odd_Dg < 1e-12)  # (local)

    fo_resid = first_order_residual(D_F, E)
    print(f"  first-order residual max||[[D,a],b^o]||: {fo_resid:.6f}  "
          f"(REPORTED; standing SecVII.BL multiplicity-bundle obstruction)")

    # --- Connes distances: vacuum-referenced ladder (PRIMARY, 3 SDPs, doubled op)
    print("\n  -- vacuum-referenced Connes distances (J-doubled 16-dim operator) --")
    d_vac = np.zeros(3)        # (local)
    d_vac_closed = omega.copy()  # (local) star theorem: d(v,g) = omega_g
    statuses = []  # (local)
    for g in range(3):
        r = connes_distance_sdp(D_F, E, i_ch=g + 1, j_ch=0)  # (local)
        d_vac[g] = r["d_C"]
        statuses += [r["status_pos"], r["status_neg"]]
        dev = abs(r["d_C"] - d_vac_closed[g]) / d_vac_closed[g]  # (local)
        print(f"    d(v, {TOWER[g]}): SDP={r['d_C']:.12f}  closed={d_vac_closed[g]:.12f}  "
              f"reldev={dev:.3e}  [{r['status_pos']}|{r['status_neg']}]")

    # --- doubling-invariance: same distances on the SINGLE 8-dim chiral star
    print("  -- doubling-invariance check (single 8-dim chiral star) --")
    E8 = [e[:8, :8] for e in E]  # (local) channel projectors on the particle copy
    d_vac_single = np.zeros(3)  # (local)
    for g in range(3):
        r = connes_distance_sdp(D_p, E8, i_ch=g + 1, j_ch=0)  # (local)
        d_vac_single[g] = r["d_C"]
        statuses += [r["status_pos"], r["status_neg"]]
    doubling_dev = float(np.max(np.abs(d_vac_single - d_vac) / d_vac))  # (local)
    print(f"    max rel dev (doubled vs single): {doubling_dev:.3e}")

    # --- assignment by metric ordering: most distant = lightest = e
    order_desc = np.argsort(-d_vac)  # (local) indices into TOWER, descending d
    sec_e, sec_mu, sec_tau = (TOWER[order_desc[0]], TOWER[order_desc[1]], TOWER[order_desc[2]])  # (local)
    d_e, d_mu_v, d_tau_v = (d_vac[order_desc[0]], d_vac[order_desc[1]], d_vac[order_desc[2]])  # (local)
    print(f"\n  assignment (most distant = lightest): e={sec_e}  mu={sec_mu}  tau={sec_tau}")
    print(f"  d_e={d_e:.9f}  d_mu={d_mu_v:.9f}  d_tau={d_tau_v:.9f}")

    # non-degeneracy + strictness
    degen_rel = (d_vac.max() - d_vac.min()) / d_vac.max()  # (local)
    gap1_rel = (d_e - d_mu_v) / d_vac.max()   # (local)
    gap2_rel = (d_mu_v - d_tau_v) / d_vac.max()  # (local)
    nondegenerate = bool(degen_rel >= DEGEN_FLOOR_REL)  # (local)
    strict_ladder = bool(gap1_rel >= DEGEN_FLOOR_REL and gap2_rel >= DEGEN_FLOOR_REL)  # (local)
    print(f"  degeneracy rel spread: {degen_rel:.6e}  (floor {DEGEN_FLOOR_REL})  "
          f"nondegenerate={nondegenerate}  strict={strict_ladder}")

    # --- adjacent ladder gaps (the N_eval '2 adjacent Connes distances') + widening
    Delta_1 = d_e - d_mu_v   # (local) e-mu ladder gap
    Delta_2 = d_mu_v - d_tau_v  # (local) mu-tau ladder gap
    W_Connes = Delta_1 / Delta_2  # (local) THE widening (verdict-bearing)
    print(f"\n  ladder gaps: Delta_1(e-mu)={Delta_1:.9f}  Delta_2(mu-tau)={Delta_2:.9f}")
    print(f"  W_Connes = Delta_1/Delta_2 = {W_Connes:.9f}   "
          f"[band ({W_BAND_LO}, {W_BAND_HI}); Casimir ideal {W_CASIMIR_IDEAL}]")

    # --- pairwise adjacent distances (SECONDARY diagnostic; Pythagorean star forms)
    print("  -- pairwise adjacent Connes distances (secondary diagnostic) --")
    pair_em = connes_distance_sdp(D_F, E, i_ch=int(order_desc[0]) + 1, j_ch=int(order_desc[1]) + 1)  # (local)
    pair_mt = connes_distance_sdp(D_F, E, i_ch=int(order_desc[1]) + 1, j_ch=int(order_desc[2]) + 1)  # (local)
    statuses += [pair_em["status_pos"], pair_em["status_neg"],
                 pair_mt["status_pos"], pair_mt["status_neg"]]
    d_pair_em_closed = float(np.sqrt(d_e ** 2 + d_mu_v ** 2) / 1.0)  # (local) sqrt(omega_e^2+omega_mu^2) via d=omega
    d_pair_mt_closed = float(np.sqrt(d_mu_v ** 2 + d_tau_v ** 2))    # (local)
    W_pairwise = pair_em["d_C"] / pair_mt["d_C"]  # (local) accumulated-ladder diagnostic
    print(f"    d_C(e,mu)={pair_em['d_C']:.9f} (closed {d_pair_em_closed:.9f})  "
          f"d_C(mu,tau)={pair_mt['d_C']:.9f} (closed {d_pair_mt_closed:.9f})")
    print(f"    W_pairwise (diagnostic) = {W_pairwise:.9f}")

    # --- closed-form fidelity (regime input)
    closed_devs = [
        abs(d_vac[g] - d_vac_closed[g]) / d_vac_closed[g] for g in range(3)
    ] + [
        abs(pair_em["d_C"] - d_pair_em_closed) / d_pair_em_closed,
        abs(pair_mt["d_C"] - d_pair_mt_closed) / d_pair_mt_closed,
    ]  # (local)
    max_closed_dev = float(np.max(closed_devs))  # (local)
    print(f"  max SDP-vs-closed-form rel dev: {max_closed_dev:.3e}")

    # --- R-sweep regulator-invariance (contrast with S87 M_n(C) CLASS-gamma)
    print("  -- R-sweep regulator-invariance (Frobenius bound on pi(a)) --")
    d_ref = d_vac[order_desc[0]]  # (local) the e-channel distance
    rsweep_vals = []  # (local)
    for fac in R_SWEEP_FACTORS:
        R = fac * float(omega.max())  # (local)
        r = connes_distance_sdp(D_F, E, i_ch=int(order_desc[0]) + 1, j_ch=0, frob_bound=R)  # (local)
        statuses += [r["status_pos"], r["status_neg"]]
        rsweep_vals.append(r["d_C"])
        print(f"    R={R:10.3f}: d_C={r['d_C']:.12f}")
    rsweep_dev = float(np.max(np.abs(np.array(rsweep_vals) - d_ref) / d_ref))  # (local)
    print(f"    max rel dev across R-sweep: {rsweep_dev:.3e}  "
          f"(S87 full-M_n(C) lineage diverged ~linearly in R; machinery value "
          f"{S88_MACHINERY_VALUE} INFO CLASS-gamma)")

    # --- bare-metric contrast (closed-form diagnostic, NOT verdict-bearing)
    d_bare = 1.0 / floors  # (local) unreweighted two-point forms d = 1/lambda
    bare_order = np.argsort(-d_bare)  # (local)
    W_bare = (d_bare[bare_order[0]] - d_bare[bare_order[1]]) / (
        d_bare[bare_order[1]] - d_bare[bare_order[2]])  # (local)
    print(f"  bare-metric contrast (diagnostic): d=1/lambda ladder, "
          f"e={TOWER[bare_order[0]]}, W_bare={W_bare:.6f}")

    # --- ell-calibration: centered OLS of ln m^PDG on d_i (PRIMARY)
    ln_m = np.array([np.log(m_e), np.log(m_mu), np.log(m_tau_PDG)])  # (local) ascending mass
    d_sorted_desc = np.array([d_e, d_mu_v, d_tau_v])  # (local) pairs with [m_e, m_mu, m_tau]
    x = d_sorted_desc  # (local)
    y = ln_m  # (local)
    xc = x - x.mean()  # (local)
    yc = y - y.mean()  # (local)
    b_ols = float((xc @ yc) / (xc @ xc))  # (local) slope = -1/ell
    ell = -1.0 / b_ols  # (local)
    r2 = float((xc @ yc) ** 2 / ((xc @ xc) * (yc @ yc)))  # (local)
    spread_pred = float((x.max() - x.min()) / ell)  # (local) predicted e-folds
    spread_pdg = float(ln_m[2] - ln_m[0])  # (local) PDG target spread
    print(f"\n  ell-calibration (centered OLS): slope={b_ols:.6f}  ell={ell:.9f}  R^2={r2:.6f}")
    print(f"  predicted spread (d_max-d_min)/ell = {spread_pred:.6f} e-folds  "
          f"[band ({SPREAD_LO}, {SPREAD_HI}); PDG {spread_pdg:.6f}]")

    # sensitivity variants (diagnostics, not verdict-bearing)
    g1_pdg = float(np.log(m_mu / m_e))        # (local)
    g2_pdg = float(np.log(m_tau_PDG / m_mu))  # (local)
    W_pdg = g1_pdg / g2_pdg                   # (local)
    dd_mu = d_mu_v - d_tau_v   # (local) cumulative from tau
    dd_e = d_e - d_tau_v       # (local)
    s_anch = (g2_pdg * dd_mu + spread_pdg * dd_e) / (dd_mu ** 2 + dd_e ** 2)  # (local)
    spread_anch = float((x.max() - x.min()) * s_anch)  # (local)
    s_gap = (g1_pdg * Delta_1 + g2_pdg * Delta_2) / (Delta_1 ** 2 + Delta_2 ** 2)  # (local)
    spread_gap = float((x.max() - x.min()) * s_gap)  # (local)
    print(f"  sensitivity: tau-anchored spread={spread_anch:.4f}; "
          f"adjacent-gap spread={spread_gap:.4f}  (diagnostics)")
    print(f"  PDG widening anchor: W_PDG = ln(m_mu/m_e)/ln(m_tau/m_mu) = {W_pdg:.6f}")

    # --- Item-6 cross-check: same envelope two ways (file LANDED)
    print("\n  -- Item-6 cross-check (same-envelope-two-ways coincidence) --")
    item6 = {}  # (local)
    if ITEM6_NPZ.exists():
        d6 = np.load(ITEM6_NPZ, allow_pickle=True)  # (local)
        item6_d_i = np.asarray(d6["d_i"], dtype=np.float64)  # (local) overlap envelope
        item6_e_sector = tuple(int(v) for v in np.asarray(d6["e_sector"]).ravel())  # (local)
        item6_floors = np.asarray(d6["floors_lambda_min"], dtype=np.float64)  # (local)
        item6_W = float(d6["widening_W"])  # (local)
        item6_W_floor_only = float(d6["W_floor_only"])  # (local)
        item6_spread = float(d6["spread_efolds"])  # (local)
        item6_verdict = str(d6["verdict"])  # (local)
        floors_match = float(np.max(np.abs(item6_floors - floors) / floors))  # (local)
        e_match = bool(item6_e_sector == sec_e)  # (local)
        # Spearman rank correlation between the two mass orderings on the tower
        # mass ranks: overlap route m ~ O_g (ascending overlap = ascending mass);
        # Connes route m ~ e^{-d} (descending d = ascending m => rank by -d)
        rank6 = np.argsort(np.argsort(item6_d_i))     # (local) 0=lightest
        rank_c = np.argsort(np.argsort(-d_vac))       # (local) 0=lightest
        dr = rank6 - rank_c  # (local)
        rho_s = float(1.0 - 6.0 * np.sum(dr ** 2) / (3 * (9 - 1)))  # (local)
        my_W_vs_their_floor_diag = abs(W_Connes - item6_W_floor_only) / abs(item6_W_floor_only)  # (local)
        item6 = {
            "present": True, "d_i": item6_d_i, "e_sector": item6_e_sector,
            "floors_match_reldev": floors_match, "e_sector_match": e_match,
            "rho_spearman": rho_s, "widening_W": item6_W,
            "W_floor_only": item6_W_floor_only, "spread_efolds": item6_spread,
            "verdict": item6_verdict,
            "W_vs_their_floor_diag_reldev": my_W_vs_their_floor_diag,
        }
        print(f"    Item-6 verdict={item6_verdict}; overlap envelope d_i={item6_d_i}")
        print(f"    floors identity (same cache): max rel dev = {floors_match:.3e}")
        print(f"    e-sector: Item-6 {item6_e_sector} vs Connes {sec_e}  -> MATCH={e_match}")
        print(f"    Spearman rho (full 3-sector mass ordering): {rho_s:.3f}")
        print(f"    widening: Connes {W_Connes:.6f} vs Item-6 W_floor_only "
              f"{item6_W_floor_only:.6f} (reldev {my_W_vs_their_floor_diag:.3e}; "
              f"SAME-SOURCE identity check, not independent evidence) vs "
              f"Item-6 overlap widening {item6_W:.6f}")
    else:  # pragma: no cover -- orchestrator confirmed LANDED
        item6 = {"present": False}
        print("    Item-6 npz ABSENT -> coincidence test held INFO-pending")

    # --- criteria + 3-tuple
    crit_i = bool(nondegenerate and strict_ladder and ell > 0)  # (local)
    crit_ii = bool(SPREAD_LO <= spread_pred <= SPREAD_HI)  # (local)
    crit_iii = bool(W_BAND_LO <= W_Connes <= W_BAND_HI)  # (local)
    print(f"\n  crit_i (sign: nondegenerate strict ladder, ell>0): {crit_i}")
    print(f"  crit_ii (spread in [{SPREAD_LO},{SPREAD_HI}]):        {crit_ii}  ({spread_pred:.4f})")
    print(f"  crit_iii (W in [{W_BAND_LO},{W_BAND_HI}]):            {crit_iii}  ({W_Connes:.6f})")

    sign_v = "PASS" if crit_i else "FAIL"  # (local)
    if crit_ii and crit_iii:
        mag_v = "PASS"  # (local)
    elif crit_ii and not crit_iii:
        mag_v = "INFO"  # plan INFO branch: envelope reproduced, widening outside band
    else:
        mag_v = "FAIL"

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
        "Delta_1": Delta_1, "Delta_2": Delta_2, "W_Connes": W_Connes,
        "d_pair_em": pair_em["d_C"], "d_pair_mt": pair_mt["d_C"],
        "d_pair_em_closed": d_pair_em_closed, "d_pair_mt_closed": d_pair_mt_closed,
        "W_pairwise": W_pairwise,
        "max_closed_dev": max_closed_dev, "rsweep_vals": np.array(rsweep_vals),
        "rsweep_dev": rsweep_dev, "d_bare": d_bare, "W_bare": W_bare,
        "bare_e_sector": TOWER[bare_order[0]],
        "ell": ell, "b_ols": b_ols, "r2": r2,
        "spread_pred": spread_pred, "spread_pdg": spread_pdg,
        "spread_anch": spread_anch, "spread_gap": spread_gap,
        "g1_pdg": g1_pdg, "g2_pdg": g2_pdg, "W_pdg": W_pdg,
        "item6": item6, "statuses": statuses, "n_inaccurate": n_inaccurate,
        "crit_i": crit_i, "crit_ii": crit_ii, "crit_iii": crit_iii,
        "sign_v": sign_v, "mag_v": mag_v, "regime_v": regime_v, "composite": composite,
    }


# ---------------------------------------------------------------------------
# Section 9 -- Plot
# ---------------------------------------------------------------------------
def make_plot(res):
    fig, axes = plt.subplots(1, 3, figsize=(16, 5.2))

    # Panel A: the Connes distance ladder
    ax = axes[0]
    labels = [f"{TOWER[g]}" for g in range(3)]  # (local)
    xpos = np.arange(3)  # (local)
    ax.bar(xpos, res["d_vac_closed"], color="lightsteelblue", label="closed form $d=\\omega_g$")
    ax.plot(xpos, res["d_vac"], "k^", markersize=10, label="SDP (CLARABEL)")
    for g in range(3):
        ax.annotate(f"{res['d_vac'][g]:.6f}", (xpos[g], res["d_vac"][g]),
                    textcoords="offset points", xytext=(0, 8), ha="center", fontsize=8)
    role = {tuple(res["sec_e"]): "e", tuple(res["sec_mu"]): "$\\mu$", tuple(res["sec_tau"]): "$\\tau$"}  # (local)
    ax.set_xticks(xpos)
    ax.set_xticklabels([f"{labels[g]}\n[{role[TOWER[g]]}]" for g in range(3)])
    ax.set_ylabel("$d_C(\\omega_v, \\omega_g)$  [cache units$^2$]")
    ax.set_title("Connes distance ladder (greybody star)\n"
                 f"$[J,D_F]=0$ dev {res['comm_JD']:.1e}; SDP-closed dev {res['max_closed_dev']:.1e}")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, axis="y")

    # Panel B: mass map regression
    ax = axes[1]
    x = np.array([res["d_e"], res["d_mu"], res["d_tau"]])  # (local)
    y = np.array([np.log(m_e), np.log(m_mu), np.log(m_tau_PDG)])  # (local)
    ax.plot(x, y, "o", color="tab:red", markersize=9, label="PDG $\\ln m_i$ vs $d_i$")
    xs = np.linspace(x.min() * 0.95, x.max() * 1.05, 50)  # (local)
    ax.plot(xs, y.mean() + res["b_ols"] * (xs - x.mean()), "--", color="gray",
            label=f"OLS: $\\ell$={res['ell']:.5f}, $R^2$={res['r2']:.4f}")
    for xi, yi, nm in zip(x, y, ["e", "$\\mu$", "$\\tau$"]):
        ax.annotate(nm, (xi, yi), textcoords="offset points", xytext=(8, 0), fontsize=11)
    ax.set_xlabel("$d_i$  [cache units$^2$]")
    ax.set_ylabel("$\\ln m_i^{PDG}$  [GeV]")
    ax.set_title(f"mass $= e^{{-d/\\ell}}$ calibration\n"
                 f"spread: pred {res['spread_pred']:.3f} vs PDG {res['spread_pdg']:.3f} e-folds")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # Panel C: widening vs band
    ax = axes[2]
    names = ["$W_{Connes}$", "Casimir\n9/5", "PDG", "$W_{pairwise}$\n(diag)", "Item-6\noverlap W"]  # (local)
    item6_W = res["item6"].get("widening_W", np.nan) if res["item6"].get("present") else np.nan  # (local)
    vals = [res["W_Connes"], W_CASIMIR_IDEAL, res["W_pdg"], res["W_pairwise"], item6_W]  # (local)
    colors = ["tab:red", "tab:green", "tab:blue", "tab:orange", "tab:purple"]  # (local)
    ax.bar(np.arange(len(vals)), vals, color=colors)
    ax.axhspan(W_BAND_LO, W_BAND_HI, color="green", alpha=0.18,
               label=f"PASS band [{W_BAND_LO}, {W_BAND_HI}]")
    for i, v in enumerate(vals):
        if np.isfinite(v):
            ax.annotate(f"{v:.4f}", (i, v), textcoords="offset points",
                        xytext=(0, 5 if v >= 0 else -14), ha="center", fontsize=8)
    ax.set_xticks(np.arange(len(vals)))
    ax.set_xticklabels(names, fontsize=8)
    ax.set_ylabel("widening")
    ax.set_title(f"widening: {res['W_Connes']:.4f} vs band\n"
                 f"crit_iii={res['crit_iii']}; composite={res['composite']}")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, axis="y")

    fig.suptitle(
        f"{GATE_ID}  (L=12, tau_fold={tau_fold}; e={res['sec_e']} mu={res['sec_mu']} tau={res['sec_tau']}; "
        f"composite {res['composite']}: sign {res['sign_v']} / mag {res['mag_v']} / regime {res['regime_v']})",
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

    # --- npz (full float64 round-trip per Class 8.3)
    item6 = res["item6"]  # (local)
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID, scheme=SCHEME, convention=CONVENTION, l_max=L_MAX,
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
        Delta_1=res["Delta_1"], Delta_2=res["Delta_2"], W_Connes=res["W_Connes"],
        d_pair_em_sdp=res["d_pair_em"], d_pair_mt_sdp=res["d_pair_mt"],
        d_pair_em_closed=res["d_pair_em_closed"], d_pair_mt_closed=res["d_pair_mt_closed"],
        W_pairwise_diag=res["W_pairwise"],
        max_sdp_closed_reldev=res["max_closed_dev"],
        rsweep_factors=np.array(R_SWEEP_FACTORS), rsweep_d_values=res["rsweep_vals"],
        rsweep_max_reldev=res["rsweep_dev"],
        s88_machinery_value=S88_MACHINERY_VALUE,
        d_bare_diag=res["d_bare"], W_bare_diag=res["W_bare"],
        bare_e_sector=np.array(res["bare_e_sector"]),
        ell_ols=res["ell"], ols_slope=res["b_ols"], ols_r2=res["r2"],
        spread_pred_efolds=res["spread_pred"], spread_pdg_efolds=res["spread_pdg"],
        spread_tau_anchored=res["spread_anch"], spread_adjacent_gap=res["spread_gap"],
        pdg_g1_lngap_mu_e=res["g1_pdg"], pdg_g2_lngap_tau_mu=res["g2_pdg"],
        W_pdg_anchor=res["W_pdg"], m_e_pdg=m_e, m_mu_pdg=m_mu, m_tau_pdg=m_tau_PDG,
        W_band=np.array([W_BAND_LO, W_BAND_HI]),
        spread_band=np.array([SPREAD_LO, SPREAD_HI]),
        W_casimir_ideal=W_CASIMIR_IDEAL,
        crit_i=res["crit_i"], crit_ii=res["crit_ii"], crit_iii=res["crit_iii"],
        item6_present=item6.get("present", False),
        item6_d_i=item6.get("d_i", np.array([])),
        item6_e_sector=np.array(item6.get("e_sector", ())),
        item6_e_sector_match=item6.get("e_sector_match", False),
        item6_floors_match_reldev=item6.get("floors_match_reldev", np.nan),
        item6_rho_spearman=item6.get("rho_spearman", np.nan),
        item6_widening_W=item6.get("widening_W", np.nan),
        item6_W_floor_only=item6.get("W_floor_only", np.nan),
        item6_spread_efolds=item6.get("spread_efolds", np.nan),
        item6_verdict=item6.get("verdict", "ABSENT"),
        W_vs_item6_floor_diag_reldev=item6.get("W_vs_their_floor_diag_reldev", np.nan),
        sdp_statuses=np.array(res["statuses"]), n_optimal_inaccurate=res["n_inaccurate"],
        sdp_tol=SDP_TOL, tau_fold_used=tau_fold,
        spectrum_cache_sha=SPECTRUM_CACHE_SHA_PIN,
        audit_sha256=audit_sha, content_sha256=content_sha,
        schema_version="S84+",
    )
    print(f"\n  Data saved: {OUT_NPZ.name} ({OUT_NPZ.stat().st_size} bytes)")

    make_plot(res)

    # --- verdict payload (agent passes to race-safe emit_verdict MCP tool)
    e_str = f"({res['sec_e'][0]},{res['sec_e'][1]})"  # (local)
    value_str = (
        f"W_Connes={res['W_Connes']:.6f}_"
        f"{'IN' if res['crit_iii'] else 'OUTSIDE'}[{W_BAND_LO},{W_BAND_HI}];"
        f"spread={res['spread_pred']:.4f}efolds_"
        f"{'IN' if res['crit_ii'] else 'OUTSIDE'}[{SPREAD_LO:.0f},{SPREAD_HI:.0f}];"
        f"sign={res['sign_v']}_nondegenerate_e={e_str}_most-distant;"
        f"d=({res['d_tau']:.6f},{res['d_mu']:.6f},{res['d_e']:.6f})lam2-units_tau-mu-e;"
        f"ell_OLS={res['ell']:.6f};R2={res['r2']:.4f};"
        f"e-sector_match_Item6={res['item6'].get('e_sector_match', 'ABSENT')};"
        f"rhoS_vs_Item6={res['item6'].get('rho_spearman', float('nan')):.2f};"
        f"SDP-closed_dev={res['max_closed_dev']:.1e};"
        f"reg-invariant_Rsweep_dev={res['rsweep_dev']:.1e};"
        f"W_pairwise_diag={res['W_pairwise']:.4f};W_bare_diag={res['W_bare']:.4f}"
    )  # (local)
    companion = (
        f"greybody star t_g=1/lambda_g^2(tau_fold): d(v,g)=lambda_g^2 EXACT (star closed form, "
        f"SDP dev {res['max_closed_dev']:.1e}); Jensen fold compresses (1,0)/(1,1) floors "
        f"(Delta_2={res['Delta_2']:.6f} vs Casimir-ideal ~5/3 scaling) => W inflated "
        f"{res['W_Connes'] / W_CASIMIR_IDEAL:.2f}x above Casimir 9/5"
    )  # (local)
    extra = [
        (f"# S88-machinery lineage: S88-CONNES-DISTANCE-FINITE-SPECTRUM-IDENTITY="
         f"{S88_MACHINERY_VALUE!r} (INFO CLASS-gamma: full M_n(C) regulator-divergent); "
         f"this gate restricts to the commutative multiplicity-bundle channel algebra C^4 "
         f"=> distance finite + regulator-invariant (R-sweep maxdev={res['rsweep_dev']:.2e}) "
         f"# {GATE_ID}"),
        (f"# KO-dim-6 J-checks: J^2=+1 ({res['eps_J2']:.1e}), [J,D_F]=0 ({res['comm_JD']:.1e}, "
         f"BDI conj-floor equality {res['bdi_dev']:.1e}), Jgamma=-gammaJ ({res['anti_Jg']:.1e}); "
         f"first-order residual {res['fo_resid']:.4f} REPORTED (standing SecVII.BL "
         f"multiplicity-bundle obstruction: generation-resolving D_F lies outside every "
         f"A_K-bimodule) # {GATE_ID}"),
        (f"# m_tau_PDG=1.77686 GeV added to canonical_constants S100a (PDG tau pole mass; "
         f"canonical m_tau=2.062 is the S42 MODULUS mass in M_KK units -- name collision; "
         f"plan-w2 ledger mis-grouping documented; plan prose floor pin 1.32766 for (1,0) "
         f"misquotes the cache MAX, true min 0.83589351) # {GATE_ID}"),
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
