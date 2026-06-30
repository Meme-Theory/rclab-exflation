#!/usr/bin/env python3
"""
S100a W2-2 S100a-YUKAWA-OVERLAP-OFFDIAG -- the |s(h)|^2-weighted Dirac-mass
overlap on the triality tower: diagonal envelope + off-diagonal w in ONE object.
==============================================================================

Gate: S100a-YUKAWA-OVERLAP-OFFDIAG ([SIGN])
Classification: PARTICLE
Agent: baptista-spacetime-analyst
Plan: sessions/session-plan/session-100a-plan-w2.md SS W2-2

Pre-registered operator (PASS-conjunction, plan SS W2-2):
  (i)   sign(ln d_e - ln d_heavy) < 0   (e lightest; envelope NOT 1:1:1)
  (ii)  |ln(d_max/d_min)| >= 4          (>= ~2 OOM spread; ~8-e-fold target floor)
  (iii) gap-asymmetry  |g_hi| > |g_lo|  with a coherent (monotone) ladder
  (iv)  widening  W = g_hi/g_lo in [1.800, 1.8894]  (Casimir floor .. PDG band)
  (v)   |w| > 1e-12                      (off-diagonal nonzero)
  with  g_lo = ln(d_(1,1)/d_(1,0)),  g_hi = ln(d_(3,0)/d_(1,1)).
  INFO iff envelope resolves (sign strict) but (ii) or (iii) or (iv) or (v)
  fails (plan INFO_meaning: widening needs the Item-7 Jensen-tilt closure).
  FAIL iff the diagonal is 1:1:1-degenerate (S97 signature; spread below the
  in-script degeneracy floor 0.05 e-folds; S97 itself sits at ~0.0195).

Output 4-tuple:
  (value=<payload>, scheme=JENSEN-FIBER-OVERLAP-SU3-HAAR, convention=RATIO,
   L_max=12)

GOVERNING STRUCTURE (Baptista lineage; structure first, computation second)
---------------------------------------------------------------------------
Submersion P = M4 x K, K = SU(3) with the Jensen left-invariant metric g_tau
at tau_fold = 0.19: metric scale factors lambda_1 = e^{2 tau} (u(1)),
lambda_2 = e^{-2 tau} (su(2)), lambda_3 = e^{tau} (C^2); volume-preserving
lambda_1 lambda_2^3 lambda_3^4 = 1 EXACTLY (Paper 13 eqs 2.37/3.35), hence
vol_{g_tau} = the Haar volume and "normalising by Vol_SU3_Haar" makes every
fiber integral below a NORMALIZED-Haar moment (the deformation enters the
spectral WEIGHT, never the measure).

The three charged-lepton generation channels are the triality-distinct
Peter-Weyl sectors (1,0), (1,1), (3,0) with SU(3) quadratic Casimir
C2 = (p^2+q^2+pq+3p+3q)/3 = 4/3, 3, 6 (exact). The Higgs is the |S|^2
transverse fiber-embedding mode in the C^2 c su(3) deformation direction;
its vertical profile is the eq-(2.104) uniqueness family
    s_phi(h) = alpha [ s_1(h) - 2 (1 + e^{2 i phi}) s_2(h) ],
    s_1 = h_11^2 + h_21^2 + h_31^2,   s_2 = h_11 h_21 + h_11 h_31 + h_21 h_31
(first-column degree-2 monomials; Item-5 lineage), unit-normalized by
alpha^2(phi) = 2 c(phi), c(phi) = 1/(1+8 cos^2 phi)  [S100a-DUAL-Z3-PHI-POINTS
PASS: c-multiset {1/9, 1/3, 1/3} exact].

THE OBSERVABLE (the overlap Paper 14 SS 3 leaves unwritten), one object with
two channels separated EXACTLY by center-Z3 (triality) selection:

  DIAGONAL (|s|^2-quadratic channel, triality-0 kernel):
      O_g = (1/Vol) Int_K Tr[ psi_g^dag |s(h)|^2 psi_g ] vol_{g_tau}
    The S62 theorem (knowledge MCP, PROVEN) -- "tree-level [s-LINEAR] Yukawa
    vanishes by PW orthogonality" -- forces the leading DIAGONAL mass weight
    into the |s|^2-quadratic channel. Spectral realization (S99 panel eq A1,
    O_g ~ N(p,q) exp(-Lambda_def/mu^2), Gaussian-in-Laplacian ansatz):
      O_g = <|s_hat|^2>_Haar * S_g(mu_H^2),
      S_g(mu^2) = sum_{lambda in abs_evals(p,q)} exp(-lambda^2 / mu^2),
    the plan-pinned "per-sector spectral sum over abs_evals" of the L=12
    cache -- the generation channel's spectral weight at the Higgs scale.
    <|s_hat|^2>_Haar = 1 exactly (unit normalization; Schur: the full-sector
    average of the kernel equals the Haar mean). The kernel's relative
    fluctuation (the un-factorized CG remainder, the seat of the Item-7
    Jensen-tilt closure) is computed EXACTLY below and reported as the
    honest factorization band.

  OFF-DIAGONAL (s-LINEAR channel, triality-2 kernel): the Dirac-mass element
    on the BDI pair t1 = (1,0) <-> t2 = (0,1) (the S97 t1/t2 classes; the
    panel's [[d, w], [w*, d]] block):
      w(phi) ~ M(phi) = M_1 + beta(phi) M_2,  beta(phi) = -2 (1 + e^{2 i phi}),
      M_{1,2}[(ij),(kl)] = 3 Int h~_{ij} {s_1, s_2}(h) h~_{kl} dh   (h~ = hbar)
    computed EXACTLY by degree-2 U(3) Weingarten (balanced degree 2 < N = 3,
    so SU(3) = U(3) moments; Wg(id;3) = 1/8, Wg(swap;3) = -1/24).
    CG/triality bookkeeping: s in (2,0), and (2,0) (x) (0,1) = (2,1) (+) (1,0)
    contains (1,0)  => the element is ALLOWED;  the plan substitution-chain's
    literal object <(1,0)| |s|^2 |(1,1)> has a triality-0 kernel between
    t = 1 and t = 0 sectors => ZERO EXACTLY by center-Z3 invariance
    (h -> omega h pulls out omega^{-1} != 1; Haar invariance kills it).
    The phase: arg(w_{M2-channel}) = arg(beta(phi)) = {pi, +2pi/3, -2pi/3}
    at the Z3 points -- the SECOND Z3 imprinted on the off-diagonal (the
    panel's Theta; CP-phase seed; survives reality because J^2 = +1, BDI).

SUBSTITUTION CHAIN (math-scripts.md, [SIGN] trigger; numbers substituted
at runtime and printed):
  Step 1 (defs):    O_g = S_g(mu_H^2) (unit kernel mean);  d_i = O_g / O_max;
                    g_lo = ln(d_(1,1)/d_(1,0));  g_hi = ln(d_(3,0)/d_(1,1));
                    W = g_hi/g_lo;  spread = |ln(d_max/d_min)|.
  Step 2 (mu pin):  mu_H = lambda_min over ALL 90 cached sectors
                    = lambda_min(0,0) = 0.819741 (verified in-script): the
                    fiber-SINGLET channel floor. The |S|^2 Higgs/modulus mode
                    is fiber-constant (left-invariant metric deformation)
                    => it lives in the (0,0) Peter-Weyl channel => its
                    Dirac-spectral anchor IS the (0,0) floor. (The 4D modulus
                    mass m_tau = 2.062 M_KK is the POTENTIAL-curvature mass,
                    not the fiber-spectral position; rejected as the pin.)
  Step 3 (floors):  cached lambda_min = 0.835894 / 0.872975 / 1.248264 for
                    (1,0)/(1,1)/(3,0); lambda_min^2 = 0.6987/0.7621/1.5582.
                    NOTE: the plan Definition-3 premise lambda_min ~ sqrt(C2)/r
                    is FALSIFIED by the cache (the plan text mislabeled the
                    (1,0) MAX 1.327661 as its min; the actual floors crowd --
                    floor(1,0)/floor(0,0) = 1.019705 = the S97 R_cross wall,
                    reproduced here as a cross-check).
  Step 4 (direction): exp(-lambda^2/mu^2) is monotone-DECREASING in lambda^2
                    => the channel with the LARGEST spectral weight at the
                    Higgs scale is the LOWEST tower rung => O decreases up
                    the C2 ladder => e (lightest, m ~ O) = argmin O at the
                    TOP of the ladder; ln d_e - ln d_heavy < 0 strictly iff
                    the envelope resolves (S97 1:1:1 would give 0).
  Step 5 (band):    pure-Casimir anchor W_Cas = (6-3)/(3-4/3) = 9/5 = 1.800
                    EXACT; the trace-mean Jensen tilt is gap-ratio-NEUTRAL:
                    Tr[pi(T_a) pi(T_b)] = (C2 dim/8) delta_ab (Dynkin) =>
                    mean deformed Laplacian = J(tau) C2 with
                    J(tau) = (3 e^{2tau} + 4 e^{-tau} + e^{-2tau})/8
                    = 1.047319 at tau_fold (slope-only). The PDG ceiling
                    1.8894 is the plan-pinned mack-domain anchor
                    ln(m_mu/m_e)/ln(m_tau/m_mu) [the plan's band-edge formula
                    label is inverted; the VALUE 1.8894 is the binding pin --
                    its provenance is verified in-script: the implied PDG
                    m_tau = m_mu exp(ln(m_mu/m_e)/1.8894) = 1.776 GeV].
  Conclusion:       evaluate (i)-(v) on the pinned primary; the realized W
                    against [1.800, 1.8894] is THE measurement; diagnostics
                    (per-mode, floor-only, scalar-Lambda_def anchor,
                    mu-sensitivity ribbon) are reported NON-VERDICT.

CONSTRUCTION PINS left open by the plan, fixed here BEFORE compute (PRDR):
  P1 spectral-weight form: plain per-sector block sum S_g = sum exp(-l^2/mu^2)
     over the cached 16*dim eigenvalues (the A1 form, multiplicity included;
     reduces to N(p,q) exp(-Lambda/mu^2) for a narrow band). Per-mode mean
     S_g/n_g and floor-only exp(-l_min^2/mu^2) are reported as DIAGNOSTICS.
  P2 mu pin: mu_H = global cached Dirac floor = lambda_min(0,0) (Step 2).
  P3 off-diagonal aggregate: |w|(phi) = alpha(phi) ||M_1 + beta(phi) M_2||_F /
     sqrt(d_A d_B), d_A = d_B = 3; phase reported per channel (M_1/M_2 have
     EXACTLY disjoint support, <M_1, M_2>_F = 0, verified).
  P4 degeneracy floor (FAIL signature): spread < 0.05 e-folds.
  These pins are structural commitments made before any number was computed;
  the verdict is evaluated ONLY at the pinned primary. No scan, no reruns.

DISCIPLINE
----------
- from canonical_constants import *  (tau_fold, Vol_SU3_Haar, m_e, m_mu,
  R_cross_yukawa_t1_t2 consumed; M_KK NOT needed -- all-ratio observables)
- spectrum cache SHA verified against the plan-freeze pin (HARD assert)
- every local intermediate tagged # (local)
- dual-SHA (S84+): audit = sha256(script || canonical || pinmap_json ||
  spectrum_cache_sha)  [plan audit_discriminators]; content = sha256(script)
- verdict PRINTED as an emit_verdict payload (print_verdict_payload); the
  dispatching agent calls mcp__knowledge__emit_verdict. NO open("a") append.
- exit 0 on script success regardless of scientific verdict
"""

from __future__ import annotations

# --- CPU thread cap BEFORE numpy import (machinery pin: numpy.linalg OMP8) ---
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 1 -- Canonical constants (MANDATORY first project import)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

_SHARED = Path(__file__).resolve().parent.parent / "_shared"   # (local)
sys.path.insert(0, str(_SHARED))
from canonical_constants import *  # noqa: F401,F403  (tau_fold, Vol_SU3_Haar, m_e, m_mu, R_cross_yukawa_t1_t2)

# ---------------------------------------------------------------------------
# Section 2 -- Standard imports
# ---------------------------------------------------------------------------
import cmath
import hashlib
import json
import time
from fractions import Fraction as Fr
from itertools import combinations_with_replacement
from math import cos, exp, factorial, log, pi, sqrt

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 -- Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "100a"                                                    # (local)
GATE_ID = "S100a-YUKAWA-OVERLAP-OFFDIAG"                            # (local)
SCHEME = "JENSEN-FIBER-OVERLAP-SU3-HAAR"                            # (local)
CONVENTION = "RATIO"                                                # (local)
L_MAX = "12"                                                        # (local)

# Pre-registered thresholds (plan SS W2-2 operator block; plan-pinned)
W_BAND_LO = 1.800        # Casimir floor 9/5 exact                  # (local)
W_BAND_HI = 1.8894       # PDG anchor (mack-domain band edge)       # (local)
SPREAD_MIN = 4.0         # e-fold floor, criterion (ii)             # (local)
W_NONZERO_TOL = 1e-12    # |w| > 0 test, plan tolerance pin         # (local)
DEGEN_FLOOR = 0.05       # P4: 1:1:1 FAIL signature (S97 ~ 0.0195)  # (local)
PDG_EFOLD_TARGET = 8.0   # ~8-e-fold e-vs-tau context target        # (local)

TOWER = [(1, 0), (1, 1), (3, 0)]   # triality-distinct generation tower (plan)
BDI_PAIR = [(1, 0), (0, 1)]        # t1/t2 fund/antifund (off-diag channel)
HIGGS_SECTOR = (0, 0)              # fiber-singlet channel (mu_H pin, P2)

CACHE_PATH = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
CACHE_SHA_PIN = "9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9"  # plan-freeze pin

OUT_NPZ = SESSION_DIR / "s100a_yukawa_overlap_offdiag.npz"
OUT_PNG = SESSION_DIR / "s100a_yukawa_overlap_offdiag.png"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    CACHE_PATH,
]

MACHINERY_PIN_MAP = {                                               # (local)
    "_gate_id": GATE_ID,
    "_wp_id": "session-100a-w2-workingpaper.md#W2-2",
    "_scheme": SCHEME,
    "_convention": CONVENTION,
    "N_eval": "3 diagonal sectors + 1 off-diagonal element (t1<->t2)",
    "L_max": "12",
    "scan_range": "N/A -- fixed tau_fold, fixed L_max=12, fixed tower {(1,0),(1,1),(3,0)}",
    "step_size": "N/A -- discrete sector set",
    "tolerance": "envelope sign exact; widening band [1.800, 1.8894]; |w| > 1e-12",
    "random_seed": "N/A -- deterministic (cached spectrum + closed-form kernel)",
    "GPU_path": "numpy.linalg (per-sector sums <= 160 entries; CPU, OMP-capped 8)",
    "publication_precision": "6 sig figs (|w|, widening cited by Wave 3 Item 9 / Wave 4 Item 14)",
    "construction_pins": ("P1 block-sum exp(-l^2/mu^2) over cached abs_evals; "
                          "P2 mu_H=lambda_min(0,0) global floor; "
                          "P3 |w|=alpha(phi)||M1+beta(phi)M2||_F/3 Weingarten-exact; "
                          "P4 degeneracy floor 0.05 e-folds"),
    "spectrum_cache_sha": CACHE_SHA_PIN,
}


# ---------------------------------------------------------------------------
# Section 4 -- SHA-256 input-pin block (S84+ dual-SHA)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str], cache_sha: str) -> tuple[str, str]:
    """audit_sha256 = sha256(script || canonical || pinmap_json || cache_sha);
    content_sha256 = sha256(script). Pinmap embeds per-gate identity keys
    (_gate_id/_scheme/...) so audit_sha256 is gate-unique. The cache SHA is a
    4th audit ingredient per the plan audit_discriminators block."""
    script_bytes = script_path.read_bytes()                         # (local)
    canonical_bytes = canonical_path.read_bytes()                   # (local)
    full_pinmap = dict(pins)                                        # (local)
    full_pinmap.update(MACHINERY_PIN_MAP)
    pinmap_json = json.dumps(dict(sorted(full_pinmap.items())),
                             separators=(",", ":"),
                             sort_keys=True).encode("utf-8")        # (local)
    h_audit = hashlib.sha256()                                      # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_audit.update(cache_sha.encode("ascii"))
    h_content = hashlib.sha256()                                    # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 5a -- Exact Haar-moment polynomial engine (first column of SU(3))
#
# A polynomial in (z, zbar), z = first column of h (uniform on S^5 in C^3),
# is a dict {(a, b): Fraction} with a, b multi-indices (3-tuples).
# E[ z^a zbar^b ] = 0 unless a == b (independent-phase invariance), else the
# Dirichlet moment 2! prod(a_k!) / (2 + sum a)!   (Item-5 engine, generalized).
# ---------------------------------------------------------------------------

def dirichlet_moment(a: tuple) -> Fr:
    num = factorial(2)                                              # (local)
    for ak in a:
        num *= factorial(ak)
    return Fr(num, factorial(2 + sum(a)))


def poly_conj(p: dict) -> dict:
    return {(b, a): c for (a, b), c in p.items()}


def poly_mul(p: dict, q: dict) -> dict:
    out: dict = {}                                                  # (local)
    for (a1, b1), c1 in p.items():
        for (a2, b2), c2 in q.items():
            key = (tuple(x + y for x, y in zip(a1, a2)),
                   tuple(x + y for x, y in zip(b1, b2)))            # (local)
            out[key] = out.get(key, Fr(0)) + c1 * c2
    return out


def poly_E(p: dict) -> Fr:
    tot = Fr(0)                                                     # (local)
    for (a, b), c in p.items():
        if a == b:
            tot += c * dirichlet_moment(a)
    return tot


def mono(z_exps: tuple, coeff=Fr(1)) -> dict:
    """Holomorphic monomial z^exps."""
    return {(z_exps, (0, 0, 0)): Fr(coeff)}


def poly_add(p: dict, q: dict, cq=Fr(1)) -> dict:
    out = dict(p)                                                   # (local)
    for k, v in q.items():
        out[k] = out.get(k, Fr(0)) + cq * v
    return out


# s_1 = z1^2 + z2^2 + z3^2 ;  s_2 = z1 z2 + z1 z3 + z2 z3
S1_POLY = poly_add(poly_add(mono((2, 0, 0)), mono((0, 2, 0))), mono((0, 0, 2)))
S2_POLY = poly_add(poly_add(mono((1, 1, 0)), mono((1, 0, 1))), mono((0, 1, 1)))


# ---------------------------------------------------------------------------
# Section 5b -- Degree-2 U(3) Weingarten engine (balanced k=2 < N=3, so the
# SU(3) moments coincide with U(3); no det/epsilon twist at this degree).
# ---------------------------------------------------------------------------

WG_ID = Fr(1, 8)     # Wg(id; 3)  = 1/(n^2-1)                       # (local)
WG_SW = Fr(-1, 24)   # Wg(swap;3) = -1/(n(n^2-1))                   # (local)


def wein2(r1, c1, r2, c2, R1, C1, R2, C2) -> Fr:
    """Int_{SU(3)} h_{r1 c1} h_{r2 c2} hbar_{R1 C1} hbar_{R2 C2} dh (norm. Haar)
    = sum_{sigma, tau in S2} Wg(sigma tau^{-1}) delta_rows(sigma) delta_cols(tau)."""
    tot = Fr(0)                                                     # (local)
    for sg in (0, 1):
        rr = (R1, R2) if sg == 0 else (R2, R1)                      # (local)
        if (r1, r2) != rr:
            continue
        for ta in (0, 1):
            cc = (C1, C2) if ta == 0 else (C2, C1)                  # (local)
            if (c1, c2) != cc:
                continue
            tot += WG_ID if sg == ta else WG_SW
    return tot


def weingarten_selftest() -> bool:
    """Two independent anchors: Int |h11|^4 = 1/6 (= Dirichlet E|z1|^4);
    Int |h11|^2 |h12|^2 = 1/12 (= row-Dirichlet E|z1|^2 |z2|^2)."""
    t1 = wein2(0, 0, 0, 0, 0, 0, 0, 0) == Fr(1, 6)                  # (local)
    t2 = wein2(0, 0, 0, 1, 0, 0, 0, 1) == Fr(1, 12)                 # (local)
    t3 = dirichlet_moment((2, 0, 0)) == Fr(1, 6)                    # (local)
    t4 = dirichlet_moment((1, 1, 0)) == Fr(1, 12)                   # (local)
    return t1 and t2 and t3 and t4


# ---------------------------------------------------------------------------
# Section 5c -- Off-diagonal channel tensors M_1, M_2 (BDI pair (1,0)<->(0,1))
#
# Sector-(1,0) PW basis functions f^A_{ij} = sqrt(3) h_{ij}; sector-(0,1)
# f^B_{kl} = sqrt(3) hbar_{kl}.  Matrix element of a holomorphic first-column
# monomial m(z) between them:
#   M[(ij),(kl)] = 3 Int hbar_{ij} m(z) hbar_{kl} dh,   z_a = h_{a 0}.
# ---------------------------------------------------------------------------

def channel_tensor(poly_monos: list) -> np.ndarray:
    """poly_monos: list of ((a,b) pairs as ordered row indices of the two h's).
    Returns the exact 9x9 tensor as float64 (entries are small rationals;
    exact Fractions kept for norms below)."""
    M = [[Fr(0)] * 9 for _ in range(9)]                             # (local)
    for (ra, rb) in poly_monos:
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    for l in range(3):
                        v = wein2(ra, 0, rb, 0, i, j, k, l)         # (local)
                        if v != 0:
                            M[3 * i + j][3 * k + l] += 3 * v
    return M


def frob_inner(A, B) -> Fr:
    tot = Fr(0)                                                     # (local)
    for i in range(9):
        for j in range(9):
            tot += A[i][j] * B[i][j]
    return tot


# ---------------------------------------------------------------------------
# Section 6 -- Compute
# ---------------------------------------------------------------------------

def compute(pins: dict) -> dict:
    res: dict = {}                                                  # (local)

    # ---- (0) Engine self-tests ----
    assert weingarten_selftest(), "Weingarten/Dirichlet self-test failed"
    E_s1s1 = poly_E(poly_mul(poly_conj(S1_POLY), S1_POLY))          # (local)
    E_s2s2 = poly_E(poly_mul(poly_conj(S2_POLY), S2_POLY))          # (local)
    E_s1s2 = poly_E(poly_mul(poly_conj(S1_POLY), S2_POLY))          # (local)
    E_s1_4 = poly_E(poly_mul(poly_mul(poly_conj(S1_POLY), S1_POLY),
                             poly_mul(poly_conj(S1_POLY), S1_POLY)))  # (local)
    haar_ok = (E_s1s1 == Fr(1, 2) and E_s2s2 == Fr(1, 4)
               and E_s1s2 == 0 and E_s1_4 == Fr(1, 3))              # (local)
    print("Haar-moment engine (exact Dirichlet, S^5 column):")
    print(f"  E|s1|^2 = {E_s1s1} (=1/2), E|s2|^2 = {E_s2s2} (=1/4), "
          f"E[conj(s1)s2] = {E_s1s2} (=0), E|s1|^4 = {E_s1_4} (=1/3): {haar_ok}")
    assert haar_ok, "Haar engine anchors failed"

    # ---- (1) Load + verify the spectrum cache (HARD SHA assert) ----
    cache_sha = pins[str(CACHE_PATH.relative_to(PROJECT_ROOT)).replace("\\", "/")]  # (local)
    assert cache_sha == CACHE_SHA_PIN, (
        f"spectrum cache SHA mismatch: {cache_sha} != plan pin {CACHE_SHA_PIN}")
    cache = np.load(CACHE_PATH, allow_pickle=True)                  # (local)
    se = cache["sector_evals"].item()                               # (local)
    n_sectors = len(se)                                             # (local)
    print(f"\nSpectrum cache: {n_sectors} sectors; SHA matches plan-freeze pin.")

    # global Dirac floor over ALL sectors (P2 pin) + Higgs-sector identity
    global_floor = min(float(np.min(np.asarray(d["abs_evals"])))
                       for d in se.values())                        # (local)
    floor_00 = float(np.min(np.asarray(se[HIGGS_SECTOR]["abs_evals"])))  # (local)
    mu_H = global_floor                                             # (local)
    mu2 = mu_H ** 2                                                 # (local)
    pin_ok = abs(global_floor - floor_00) < 1e-15                   # (local)
    print(f"  mu_H pin (P2): global floor = {global_floor:.9f} == "
          f"lambda_min(0,0) = {floor_00:.9f}: {pin_ok}")
    assert pin_ok, "P2 pin violated: global floor is not the (0,0) sector floor"

    # tower + BDI-pair data; block completeness (regime check)
    sectors = {}                                                    # (local)
    blocks_complete = True                                          # (local)
    for pq in TOWER + [(0, 1), HIGGS_SECTOR]:
        d = se[pq]                                                  # (local)
        ev = np.sort(np.asarray(d["abs_evals"], dtype=np.float64))  # (local)
        ok = (ev.size == 16 * int(d["dim"]))                        # (local)
        blocks_complete = blocks_complete and ok
        sectors[pq] = dict(dim=int(d["dim"]), evals=ev,
                           lam_min=float(ev[0]), lam_max=float(ev[-1]))
        print(f"  sector {pq}: dim={d['dim']} n_evals={ev.size} "
              f"(=16*dim: {ok}) lam_min={ev[0]:.6f} lam_max={ev[-1]:.6f}")
    assert blocks_complete, "cache block incomplete (n_evals != 16*dim)"

    # S97 wall reproduction cross-check (canonical R_cross_yukawa_t1_t2)
    r_cross_repro = sectors[(1, 0)]["lam_min"] / floor_00           # (local)
    r_cross_dev = abs(r_cross_repro - R_cross_yukawa_t1_t2)         # (local)
    print(f"  S97 cross-check: floor(1,0)/floor(0,0) = {r_cross_repro:.6f} "
          f"vs R_cross_yukawa_t1_t2 = {R_cross_yukawa_t1_t2} "
          f"(|dev| = {r_cross_dev:.2e})")
    assert r_cross_dev < 1e-5, "S97 R_cross reproduction failed -- wrong cache?"

    # BDI pair degeneracy (dual-Z3 / Item-5 sector-assignment cross-check).
    # The conjugate blocks were diagonalized SEPARATELY at S84, so the
    # KO-dim-6 / [J, D_K] = 0 degeneracy holds to machine precision, not
    # bit-identity; the check tolerance is the wave float-cross-check pin
    # rtol = 1e-12 (Item-5 machinery pin), with the deviation stored.
    bdi_dev = float(np.max(np.abs(sectors[(1, 0)]["evals"]
                                  - sectors[(0, 1)]["evals"])
                           / np.maximum(sectors[(1, 0)]["evals"], 1e-300)))  # (local)
    bdi_equal = bool(bdi_dev < 1e-12)                               # (local)
    print(f"  BDI pair (1,0) == (0,1) spectra machine-degenerate "
          f"(max rel dev = {bdi_dev:.2e} < 1e-12): {bdi_equal}")

    # ---- (2) Exact Casimir / Jensen anchors ----
    def c2_exact(p, q):
        return Fr(p * p + q * q + p * q + 3 * p + 3 * q, 3)
    C2 = [c2_exact(*pq) for pq in TOWER]                            # (local)
    W_cas = (C2[2] - C2[1]) / (C2[1] - C2[0])                       # (local)
    J_tau = (3.0 * exp(2 * tau_fold) + 4.0 * exp(-tau_fold)
             + exp(-2 * tau_fold)) / 8.0                            # (local)
    spread_scalar = J_tau * float(C2[2] - C2[0]) / mu2              # (local)
    print(f"\nExact anchors: C2 = {[str(c) for c in C2]}; "
          f"W_Casimir = {W_cas} = {float(W_cas):.6f} (exact 9/5)")
    print(f"  Jensen trace-mean slope J(tau_fold) = {J_tau:.6f} "
          f"(gap-ratio-NEUTRAL by the Dynkin identity Tr[T_a T_b] ~ delta_ab)")
    print(f"  scalar-channel A1 anchor: W = 9/5 exact, "
          f"spread = J*(C2_max-C2_min)/mu2 = {spread_scalar:.4f} e-folds")
    assert W_cas == Fr(9, 5), "Casimir anchor failed"

    # ---- (3) Kernel normalization + fluctuation (exact Haar moments) ----
    # s_0 = s_1 - 4 s_2 (phi = 0 principal Z3 point); alpha^2(0) = 2 c(0) = 2/9
    c_phi = [Fr(1, 9), Fr(1, 3), Fr(1, 3)]                          # (local)
    alpha2 = [2 * c for c in c_phi]                                 # (local)
    s0 = poly_add(S1_POLY, S2_POLY, Fr(-4))                         # (local)
    ker0 = poly_mul(poly_conj(s0), s0)                              # |s_0|^2  (local)
    E_ker0 = poly_E(ker0)                                           # (local)
    mean_unit = alpha2[0] * E_ker0                                  # (local)
    E_ker0_sq = poly_E(poly_mul(ker0, ker0))                        # (local)
    relvar = alpha2[0] ** 2 * E_ker0_sq - mean_unit ** 2            # (local)
    print(f"\nKernel (phi=0): E|s_0|^2 = {E_ker0} (=9/2); "
          f"alpha^2 E|s_0|^2 = {mean_unit} (=1, unit norm exact)")
    print(f"  kernel fluctuation: E|s_hat|^4 - 1 = {relvar} "
          f"= {float(relvar):.6f} (relative variance; the un-factorized CG "
          f"remainder / Item-7 Jensen-tilt seat)")
    assert mean_unit == 1, "kernel unit normalization failed"

    # ---- (4) PRIMARY diagonal: per-sector Gaussian heat sums at mu_H ----
    O = {}                                                          # (local)
    tailfrac = {}                                                   # (local)
    for pq in TOWER + [(0, 1)]:
        ev = sectors[pq]["evals"]                                   # (local)
        wts = np.exp(-(ev ** 2) / mu2)                              # (local)
        O[pq] = float(np.sum(wts))     # <|s_hat|^2>_Haar = 1 multiplies this
        tailfrac[pq] = float(wts[-1] / np.sum(wts))                 # (local)
    O_arr = np.array([O[pq] for pq in TOWER])                       # (local)
    d_norm = O_arr / O_arr.max()                                    # (local)
    bdi_O_dev = abs(O[(1, 0)] - O[(0, 1)]) / O[(1, 0)]              # (local)
    bdi_O_equal = bool(bdi_O_dev < 1e-12)                           # (local)

    lnO = np.log(O_arr)                                             # (local)
    g_lo = float(lnO[1] - lnO[0])      # ln(d_(1,1)/d_(1,0))        # (local)
    g_hi = float(lnO[2] - lnO[1])      # ln(d_(3,0)/d_(1,1))        # (local)
    monotone = (g_lo * g_hi > 0)                                    # (local)
    W = g_hi / g_lo if g_lo != 0 else float("inf")                  # (local)
    spread = float(np.max(lnO) - np.min(lnO))                       # (local)
    i_min = int(np.argmin(O_arr))                                   # (local)
    i_max = int(np.argmax(O_arr))                                   # (local)
    sign_ln = float(lnO[i_min] - lnO[i_max])   # ln d_e - ln d_heavy (local)
    e_sector = TOWER[i_min]                                         # (local)
    heavy_sector = TOWER[i_max]                                     # (local)

    print(f"\nPRIMARY diagonal (P1 block sums at mu_H = {mu_H:.6f}, "
          f"mu2 = {mu2:.6f}):")
    for k, pq in enumerate(TOWER):
        print(f"  O_{pq} = {O_arr[k]:.9f}   d_norm = {d_norm[k]:.9f}   "
              f"(tail-term frac {tailfrac[pq]:.2e})")
    print(f"  O_(0,1) = {O[(0, 1)]:.9f}; BDI-degenerate with O_(1,0) "
          f"(rel dev {bdi_O_dev:.2e} < 1e-12): {bdi_O_equal}")
    print(f"  g_lo = ln(O11/O10) = {g_lo:+.6f}")
    print(f"  g_hi = ln(O30/O11) = {g_hi:+.6f}")
    print(f"  monotone ladder (same sign): {monotone}")
    print(f"  widening W = g_hi/g_lo = {W:.6f}   "
          f"(band [{W_BAND_LO}, {W_BAND_HI}]; Casimir floor 1.800)")
    print(f"  spread = |ln(O_max/O_min)| = {spread:.6f} e-folds "
          f"(criterion >= {SPREAD_MIN}; PDG context target ~{PDG_EFOLD_TARGET})")
    print(f"  envelope: e-channel (argmin O) = {e_sector}, "
          f"heavy-channel (argmax O) = {heavy_sector}; "
          f"sign(ln d_e - ln d_heavy) = {sign_ln:+.6f}")

    # ---- (5) DIAGNOSTICS (non-verdict; pre-registered as such) ----
    O_permode = O_arr / np.array([sectors[pq]["evals"].size
                                  for pq in TOWER], dtype=float)    # (local)
    ln_pm = np.log(O_permode)                                       # (local)
    W_permode = float((ln_pm[2] - ln_pm[1]) / (ln_pm[1] - ln_pm[0]))  # (local)
    spread_pm = float(ln_pm.max() - ln_pm.min())                    # (local)
    floors2 = np.array([sectors[pq]["lam_min"] ** 2 for pq in TOWER])  # (local)
    gflo_lo = (floors2[1] - floors2[0]) / mu2                       # (local)
    gflo_hi = (floors2[2] - floors2[1]) / mu2                       # (local)
    W_floor = float(gflo_hi / gflo_lo)                              # (local)
    spread_floor = float((floors2[2] - floors2[0]) / mu2)           # (local)
    # mu-sensitivity ribbon (diagnostic ONLY; verdict stays at pinned mu_H)
    ribbon = {}                                                     # (local)
    for tag, fac in (("half", 0.5), ("pin", 1.0), ("twice", 2.0)):
        s_r = [float(np.sum(np.exp(-(sectors[pq]["evals"] ** 2) / (mu2 * fac))))
               for pq in TOWER]                                     # (local)
        l_r = np.log(s_r)                                           # (local)
        ribbon[tag] = (float((l_r[2] - l_r[1]) / (l_r[1] - l_r[0])),
                       float(l_r.max() - l_r.min()))
    print("\nDIAGNOSTICS (non-verdict):")
    print(f"  per-mode mean:  W = {W_permode:.6f}, spread = {spread_pm:.4f}")
    print(f"  floor-only:     W = {W_floor:.6f}, spread = {spread_floor:.4f}")
    print(f"  scalar-channel: W = 9/5 exact,  spread = {spread_scalar:.4f}")
    print(f"  mu-ribbon (W, spread): half={ribbon['half'][0]:.4f}/"
          f"{ribbon['half'][1]:.4f}  pin={ribbon['pin'][0]:.4f}/"
          f"{ribbon['pin'][1]:.4f}  twice={ribbon['twice'][0]:.4f}/"
          f"{ribbon['twice'][1]:.4f}")

    # ---- (6) OFF-DIAGONAL channel (Weingarten-exact, BDI pair) ----
    s1_rows = [(0, 0), (1, 1), (2, 2)]   # z_a^2 monomials (row pairs) (local)
    s2_rows = [(0, 1), (0, 2), (1, 2)]   # z_a z_b, a<b                (local)
    M1 = channel_tensor(s1_rows)                                    # (local)
    M2 = channel_tensor(s2_rows)                                    # (local)
    n1 = frob_inner(M1, M1)                                         # (local)
    n2 = frob_inner(M2, M2)                                         # (local)
    n12 = frob_inner(M1, M2)                                        # (local)
    print(f"\nOFF-DIAGONAL channel (BDI pair (1,0)<->(0,1), s-LINEAR Dirac-mass"
          f" element; degree-2 Weingarten exact):")
    print(f"  ||M1||_F^2 = {n1} = {float(n1):.6f}; ||M2||_F^2 = {n2} "
          f"= {float(n2):.6f}; <M1,M2>_F = {n12} (disjoint support => 0)")
    assert n12 == 0, "M1/M2 support-disjointness failed"
    # w(phi) = alpha(phi) ||M1 + beta(phi) M2||_F / sqrt(d_A d_B), sqrt(9)=3
    phi_labels = ["0", "2pi/3", "4pi/3"]                            # (local)
    phi_floats = [0.0, 2 * pi / 3, 4 * pi / 3]                      # (local)
    abs_w = []                                                      # (local)
    arg_w_m2 = []                                                   # (local)
    for pf, a2 in zip(phi_floats, alpha2):
        beta = -2.0 * (1.0 + cmath.exp(2j * pf))                    # (local)
        norm2 = float(n1) + abs(beta) ** 2 * float(n2)              # (local)
        absw = sqrt(float(a2)) * sqrt(norm2) / 3.0                  # (local)
        abs_w.append(absw)
        arg_w_m2.append(cmath.phase(beta))
    for lab, aw, ag in zip(phi_labels, abs_w, arg_w_m2):
        print(f"  phi={lab:>6}: |w| = {aw:.6f}; arg(w_M2-channel) = "
              f"{ag:+.6f} rad (= arg[-2(1+e^(2 i phi))])")
    print(f"  arg(w) at the Z3 orbit = {{pi, +2pi/3, -2pi/3}} EXACT -- the "
          f"second-Z3 phase imprinted on the off-diagonal (CP seed, BDI J^2=+1)")
    # the plan-chain literal object: <(1,0)| |s|^2 |(1,1)> -- center-Z3 zero
    print(f"  literal (1,0)<->(1,1) |s|^2 element: ZERO EXACTLY "
          f"[center-Z3: h -> omega h gives omega^(-1) x 1 x 1 != 1; "
          f"Haar invariance => integral = 0; also CG: triality-0 kernel "
          f"cannot connect t=1 to t=0]")

    # ---- (7) PDG anchors (canonical m_e, m_mu; band edge provenance) ----
    pdg_gap_mue = log(m_mu / m_e)                                   # (local)
    m_tau_implied = m_mu * exp(pdg_gap_mue / W_BAND_HI)             # (local)
    print(f"\nPDG anchors: ln(m_mu/m_e) = {pdg_gap_mue:.6f} "
          f"(canonical m_e, m_mu, GeV)")
    print(f"  band-edge provenance: 1.8894 = ln(m_mu/m_e)/ln(m_tau/m_mu) => "
          f"implied m_tau = {m_tau_implied:.4f} GeV (PDG 1.77686; the plan "
          f"band-edge formula label was inverted, the VALUE is the pin)")

    res.update(dict(
        mu_H=mu_H, mu2=mu2, sectors=sectors, O=O, O_arr=O_arr,
        d_norm=d_norm, g_lo=g_lo, g_hi=g_hi, W=W, spread=spread,
        monotone=monotone, sign_ln=sign_ln, e_sector=e_sector,
        heavy_sector=heavy_sector, bdi_equal=bdi_equal, bdi_dev=bdi_dev,
        bdi_O_equal=bdi_O_equal, bdi_O_dev=bdi_O_dev,
        r_cross_repro=r_cross_repro,
        C2=C2, W_cas=W_cas, J_tau=J_tau, spread_scalar=spread_scalar,
        relvar=relvar, E_ker0=E_ker0, c_phi=c_phi, alpha2=alpha2,
        W_permode=W_permode, spread_pm=spread_pm, W_floor=W_floor,
        spread_floor=spread_floor, ribbon=ribbon,
        n1=n1, n2=n2, n12=n12, abs_w=abs_w, arg_w_m2=arg_w_m2,
        phi_labels=phi_labels, phi_floats=phi_floats,
        tailfrac=tailfrac, blocks_complete=blocks_complete,
        pdg_gap_mue=pdg_gap_mue, m_tau_implied=m_tau_implied,
        E_s1s1=E_s1s1, E_s2s2=E_s2s2, E_s1_4=E_s1_4,
    ))
    return res


# ---------------------------------------------------------------------------
# Section 7 -- Gate verdict + [SIGN] 3-tuple
# ---------------------------------------------------------------------------

def evaluate_gate(r: dict) -> tuple[str, str, str, str, dict]:
    """(composite, sign, magnitude, regime, crit-dict) per plan operator +
    gate-verdicts.md collapse rule. Evaluated ONLY at the pinned primary."""
    degenerate = (r["spread"] < DEGEN_FLOOR)                        # (local)
    # SIGN: strict envelope resolution, e = argmin O (m ~ O), NOT 1:1:1
    sign_v = "FAIL" if degenerate else ("PASS" if r["sign_ln"] < 0 else "FAIL")
    crit = dict(
        i_sign=(not degenerate) and (r["sign_ln"] < 0),
        ii_spread=(r["spread"] >= SPREAD_MIN),
        iii_gap=(r["monotone"] and abs(r["g_hi"]) > abs(r["g_lo"])),
        iv_band=(r["monotone"] and (W_BAND_LO <= r["W"] <= W_BAND_HI)),
        v_offdiag=(min(r["abs_w"]) > W_NONZERO_TOL),
    )                                                               # (local)
    if degenerate:
        mag_v = "FAIL"                                              # (local)
    elif all(crit.values()):
        mag_v = "PASS"                                              # (local)
    else:
        mag_v = "INFO"   # plan INFO_meaning: resolves, needs Item-7 closure
    # REGIME: complete blocks (exact sums, no truncation inside a sector);
    # the Gaussian weight is evaluated on the FULL block => no window breach.
    regime_v = "VALID" if (r["blocks_complete"] and r["mu2"] > 0) else "BREAKDOWN"
    if regime_v == "BREAKDOWN":
        comp = "FAIL"                                               # (local)
    elif sign_v == "FAIL":
        comp = "FAIL"
    elif mag_v == "FAIL" and regime_v == "VALID":
        comp = "FAIL"
    elif mag_v == "FAIL" and regime_v == "MARGINAL":
        comp = "INFO"
    elif mag_v == "INFO":
        comp = "INFO"
    else:
        comp = "PASS"
    return comp, sign_v, mag_v, regime_v, crit


def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, companion_note="",
                          extra_rows=None) -> dict:
    """Print the emit_verdict payload (race-safe MCP single-writer path).
    The script does NOT write the verdict file."""
    payload: dict = {                                               # (local)
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
    }
    if companion_note:
        payload["companion_note"] = companion_note
    if not (sign_verdict is None and magnitude_verdict is None
            and regime_verdict is None):
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
# Section 8 -- Plot + data
# ---------------------------------------------------------------------------

def make_plot(r: dict, verdict: str) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(13.5, 10.0))            # (local)
    ax1, ax2, ax3, ax4 = axes.flat                                  # (local)
    cols = {(1, 0): "tab:blue", (1, 1): "tab:green", (3, 0): "tab:red"}  # (local)

    # Panel 1: per-sector spectra under the Gaussian Higgs-scale weight
    for pq in TOWER:
        ev = r["sectors"][pq]["evals"]                              # (local)
        ax1.semilogy(ev, np.exp(-(ev ** 2) / r["mu2"]), ".",
                     ms=4, color=cols[pq],
                     label=f"{pq}: S = {r['O'][pq]:.4f}")
    ax1.axvline(r["mu_H"], color="k", ls="--", lw=1.0,
                label=rf"$\mu_H$ = {r['mu_H']:.4f} (floor (0,0))")
    ax1.set_xlabel(r"$|\lambda|$ (cached $D_K$ block eigenvalues)")
    ax1.set_ylabel(r"$e^{-\lambda^2/\mu_H^2}$")
    ax1.set_title("Per-sector Dirac spectra under the Higgs-scale Gaussian\n"
                  r"$O_g = \langle|\hat s|^2\rangle_{\rm Haar}\cdot"
                  r"\sum_{\lambda\in g} e^{-\lambda^2/\mu_H^2}$")
    ax1.legend(fontsize=8)

    # Panel 2: envelope ladder ln O vs C2 (primary + diagnostics)
    c2f = [float(c) for c in r["C2"]]                               # (local)
    lnO = np.log(r["O_arr"])                                        # (local)
    ax2.plot(c2f, lnO - lnO.max(), "o-", color="tab:purple", lw=2,
             label=f"primary block-sum (W={r['W']:.3f})")
    ln_pm = np.log(r["O_arr"] / np.array(
        [r["sectors"][pq]["evals"].size for pq in TOWER]))          # (local)
    ax2.plot(c2f, ln_pm - ln_pm.max(), "s--", color="tab:orange",
             label=f"per-mode mean (W={r['W_permode']:.3f})")
    fl = -np.array([r["sectors"][pq]["lam_min"] ** 2 for pq in TOWER]) / r["mu2"]  # (local)
    ax2.plot(c2f, fl - fl.max(), "^:", color="tab:gray",
             label=f"floor-only (W={r['W_floor']:.3f})")
    sc = -r["J_tau"] * np.array(c2f) / r["mu2"]                     # (local)
    ax2.plot(c2f, sc - sc.max(), "d-.", color="tab:cyan",
             label="scalar-channel anchor (W=9/5 exact)")
    for x, pq in zip(c2f, TOWER):
        ax2.annotate(str(pq), (x, (lnO - lnO.max())[TOWER.index(pq)]),
                     textcoords="offset points", xytext=(6, 6), fontsize=9)
    ax2.set_xlabel(r"$C_2(p,q)$")
    ax2.set_ylabel(r"$\ln O_g - \ln O_{\max}$")
    ax2.set_title(f"Envelope ladder (spread = {r['spread']:.3f} e-folds; "
                  f"e-channel = {r['e_sector']})")
    ax2.legend(fontsize=8)

    # Panel 3: widening anatomy vs the pre-registered band
    names = ["primary", "per-mode", "floor-only", "scalar (9/5)"]   # (local)
    Ws = [r["W"], r["W_permode"], r["W_floor"], 1.8]                # (local)
    bars = ax3.bar(names, Ws,
                   color=["tab:purple", "tab:orange", "tab:gray", "tab:cyan"])
    ax3.axhspan(W_BAND_LO, W_BAND_HI, color="tab:green", alpha=0.25,
                label=f"PASS band [{W_BAND_LO}, {W_BAND_HI}]")
    ax3.axhline(1.8, color="k", ls="--", lw=0.8)
    for b, wv in zip(bars, Ws):
        ax3.text(b.get_x() + b.get_width() / 2, wv, f"{wv:.3f}",
                 ha="center", va="bottom", fontsize=9)
    ax3.set_ylabel(r"widening $W = g_{\rm hi}/g_{\rm lo}$")
    ax3.set_title("Widening vs pre-registered band\n"
                  "(verdict reads the PRIMARY bar only; others diagnostic)")
    ax3.legend(fontsize=8)

    # Panel 4: off-diagonal channel at the Z3 points
    xs = np.arange(3)                                               # (local)
    ax4.bar(xs - 0.15, r["abs_w"], width=0.3, color="tab:blue",
            label=r"$|w|(\varphi)$ (BDI $(1,0)\leftrightarrow(0,1)$, exact)")
    ax4.bar(xs + 0.15, [0, 0, 0], width=0.3, color="tab:red",
            label=r"$(1,0)\leftrightarrow(1,1)$ $|s|^2$ elem (= 0, center-$Z_3$)")
    for x, aw, ag in zip(xs, r["abs_w"], r["arg_w_m2"]):
        ax4.text(x - 0.15, aw, f"{aw:.4f}\narg={ag:+.3f}",
                 ha="center", va="bottom", fontsize=8)
    ax4.set_xticks(xs, [rf"$\varphi$={s}" for s in r["phi_labels"]])
    ax4.set_ylabel(r"$|w|$")
    ax4.set_title(r"Off-diagonal Dirac-mass channel: $|w|>0$;"
                  "\n" r"arg$(w_{M_2})$ = {$\pi$, $+2\pi/3$, $-2\pi/3$} "
                  "(second-$Z_3$ phase, CP seed)")
    ax4.legend(fontsize=8)

    fig.suptitle(f"{GATE_ID}: {verdict} -- |s(h)|^2-weighted Dirac-mass "
                 f"overlap, diagonal envelope + off-diagonal w "
                 f"(L_max=12 cache, tau_fold={tau_fold})", fontsize=12)
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    fig.savefig(OUT_PNG, dpi=150)
    plt.close(fig)
    print(f"\nplot -> {OUT_PNG.name}")


def save_npz(r: dict, verdict: str, tup3: tuple, crit: dict,
             audit_sha: str, content_sha: str) -> None:
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID, scheme=SCHEME, convention=CONVENTION,
        l_max=str(L_MAX), verdict=verdict,
        sign_verdict=tup3[0], magnitude_verdict=tup3[1], regime_verdict=tup3[2],
        # --- primary observable (Item-7 HARD input; Items 8/9/14 soft) ---
        tower_pq=np.array(TOWER, dtype=np.int64),
        tower_C2=np.array([float(c) for c in r["C2"]]),
        tower_C2_num=np.array([c.numerator for c in r["C2"]], dtype=np.int64),
        tower_C2_den=np.array([c.denominator for c in r["C2"]], dtype=np.int64),
        O_g=r["O_arr"],                       # raw diagonal overlaps, tower order
        d_i=r["d_norm"],                      # normalized envelope d_i = O/O_max
        O_01=r["O"][(0, 1)],                  # BDI partner (== O_(1,0) exactly)
        g_lo=r["g_lo"], g_hi=r["g_hi"], widening_W=r["W"],
        spread_efolds=r["spread"], sign_ln_e_minus_heavy=r["sign_ln"],
        monotone_ladder=r["monotone"],
        e_sector=np.array(r["e_sector"], dtype=np.int64),
        heavy_sector=np.array(r["heavy_sector"], dtype=np.int64),
        mu_H=r["mu_H"], mu2=r["mu2"],
        evals_10=r["sectors"][(1, 0)]["evals"],
        evals_01=r["sectors"][(0, 1)]["evals"],
        evals_11=r["sectors"][(1, 1)]["evals"],
        evals_30=r["sectors"][(3, 0)]["evals"],
        evals_00=r["sectors"][(0, 0)]["evals"],
        floors_lambda_min=np.array([r["sectors"][pq]["lam_min"] for pq in TOWER]),
        dims=np.array([r["sectors"][pq]["dim"] for pq in TOWER], dtype=np.int64),
        n_evals=np.array([r["sectors"][pq]["evals"].size for pq in TOWER],
                         dtype=np.int64),
        # --- off-diagonal channel (Wave-3 |w| seed; Wave-4 eps_LX seed) ---
        abs_w_phi=np.array(r["abs_w"]),       # |w| at phi = 0, 2pi/3, 4pi/3
        arg_w_M2_phi=np.array(r["arg_w_m2"]),  # = {pi, +2pi/3, -2pi/3} exact
        phi_floats=np.array(r["phi_floats"]),
        M1_norm2=float(r["n1"]), M2_norm2=float(r["n2"]),
        M12_inner=float(r["n12"]),            # = 0 exact (disjoint support)
        w_chain_literal_t0=0.0,               # (1,0)<->(1,1) |s|^2 elem, exact 0
        w_chain_zero_proof=np.array(
            "center-Z3: h->omega*h pulls omega^-1 from conj(f_(1,0)), "
            "|s|^2 and f_(1,1) invariant; Haar invariance => 0; "
            "CG: triality-0 kernel cannot connect t=1 to t=0"),
        eps_lx_block_phi0=np.array(
            [[r["O"][(1, 0)], r["abs_w"][0]],
             [r["abs_w"][0], r["O"][(0, 1)]]]),   # [[d,|w|],[|w|,d]] seed
        # --- kernel (exact Haar moments) ---
        kernel_mean_unit=1.0,
        kernel_relvar_phi0=float(r["relvar"]),
        E_abs_s0_sq=float(r["E_ker0"]),
        c_phi=np.array([float(c) for c in r["c_phi"]]),
        alpha2_phi=np.array([float(a) for a in r["alpha2"]]),
        # --- anchors + cross-checks ---
        W_casimir_exact=1.8, W_casimir_num=9, W_casimir_den=5,
        J_tau=r["J_tau"], spread_scalar_anchor=r["spread_scalar"],
        W_permode=r["W_permode"], spread_permode=r["spread_pm"],
        W_floor_only=r["W_floor"], spread_floor_only=r["spread_floor"],
        mu_ribbon_W=np.array([r["ribbon"]["half"][0], r["ribbon"]["pin"][0],
                              r["ribbon"]["twice"][0]]),
        mu_ribbon_spread=np.array([r["ribbon"]["half"][1], r["ribbon"]["pin"][1],
                                   r["ribbon"]["twice"][1]]),
        bdi_pair_spectra_equal=r["bdi_equal"],
        bdi_pair_max_rel_dev=r["bdi_dev"],
        bdi_pair_O_equal=r["bdi_O_equal"],
        bdi_pair_O_rel_dev=r["bdi_O_dev"],
        r_cross_repro=r["r_cross_repro"],
        r_cross_canonical=float(R_cross_yukawa_t1_t2),
        pdg_lngap_mu_e=r["pdg_gap_mue"],
        m_tau_implied_by_band_edge=r["m_tau_implied"],
        # --- criteria + pins ---
        crit_i=crit["i_sign"], crit_ii=crit["ii_spread"],
        crit_iii=crit["iii_gap"], crit_iv=crit["iv_band"],
        crit_v=crit["v_offdiag"],
        W_band=np.array([W_BAND_LO, W_BAND_HI]),
        spread_min=SPREAD_MIN, degen_floor=DEGEN_FLOOR,
        w_nonzero_tol=W_NONZERO_TOL,
        tau_fold_used=float(tau_fold),
        vol_su3_haar=float(Vol_SU3_Haar),     # volume-preserving => Haar measure
        spectrum_cache_sha=CACHE_SHA_PIN,
        audit_sha256=audit_sha, content_sha256=content_sha,
        schema_version="S84+",
    )
    print(f"data -> {OUT_NPZ.name}")


# ---------------------------------------------------------------------------
# Section 9 -- Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()                                                # (local)
    pins = log_input_pins(INPUT_FILES)                              # (local)
    script_path = Path(__file__).resolve()                          # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"          # (local)
    cache_rel = str(CACHE_PATH.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
    audit_sha, content_sha = compute_dual_sha(
        script_path, canonical_path, pins, pins[cache_rel])
    print(f"  audit_sha256:   {audit_sha} (script+canonical+pinmap+cache_sha)")
    print(f"  content_sha256: {content_sha} (script only)")
    print()

    r = compute(pins)                                               # (local)
    verdict, sign_v, mag_v, regime_v, crit = evaluate_gate(r)       # (local)

    print(f"\nCriteria: (i) sign={crit['i_sign']}  (ii) spread>=4={crit['ii_spread']}  "
          f"(iii) gap-asym={crit['iii_gap']}  (iv) W-band={crit['iv_band']}  "
          f"(v) |w|>0={crit['v_offdiag']}")

    value = (f"W={r['W']:.6f}_band[1.800,1.8894];spread={r['spread']:.4f}ef_min4;"
             f"signlnEH={r['sign_ln']:+.4f};mono={r['monotone']};"
             f"d=[{r['d_norm'][0]:.4e},{r['d_norm'][1]:.4e},{r['d_norm'][2]:.4e}];"
             f"e_ch={r['e_sector']};|w|0={r['abs_w'][0]:.6f};"
             f"argw_Z3={{pi,+2pi/3,-2pi/3}};w_t0chain=0_centerZ3;"
             f"mu={r['mu_H']:.6f}_floor00;W_cas=9/5;"
             f"W_scalar_spread={r['spread_scalar']:.3f};"
             f"Rxrepro={r['r_cross_repro']:.6f}")                   # (local)

    make_plot(r, verdict)
    save_npz(r, verdict, (sign_v, mag_v, regime_v), crit, audit_sha, content_sha)

    print()
    print(emit_4tuple(value, SCHEME, CONVENTION, L_MAX))
    print_verdict_payload(
        verdict, value, audit_sha, content_sha,
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v,
        companion_note=("Dirac-channel Gaussian block-sum primary at "
                        "mu_H=lambda_min(0,0)=0.819741; kernel exact-Haar "
                        "unit-normalized (Item-5 alpha^2=2c lineage); BDI pair "
                        "(1,0)/(0,1) machine-degenerate diagonal (rel dev "
                        f"{r['bdi_O_dev']:.1e})"),
        extra_rows=[
            (f"# diagnostics(non-verdict): W_permode={r['W_permode']:.4f} "
             f"W_flooronly={r['W_floor']:.4f} W_scalarLambda=1.800exact "
             f"spread_scalar={r['spread_scalar']:.3f}ef "
             f"kernel_relvar_phi0={float(r['relvar']):.4f} "
             f"mu_ribbon_W=[{r['ribbon']['half'][0]:.3f},{r['ribbon']['pin'][0]:.3f},"
             f"{r['ribbon']['twice'][0]:.3f}] # {GATE_ID}"),
            (f"# off-diag: |w|(0)={r['abs_w'][0]:.6f} |w|(2pi/3)={r['abs_w'][1]:.6f} "
             f"arg_w(Z3)={{pi,+2pi/3,-2pi/3}} exact (second-Z3 on BDI "
             f"fund<->antifund, s-LINEAR channel); literal (1,0)<->(1,1) "
             f"|s|^2 element=0 exact (center-Z3/triality selection) # {GATE_ID}"),
        ],
    )

    print(f"\n=== {GATE_ID}: {verdict} (sign={sign_v} magnitude={mag_v} "
          f"regime={regime_v}; wall {time.time() - t0:.1f}s) ===")
    return 0   # exit 0 on script success regardless of scientific verdict


if __name__ == "__main__":
    sys.exit(main())
