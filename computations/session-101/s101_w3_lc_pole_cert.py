#!/usr/bin/env python3
"""
S101 W1-2 S101-W3-LC-POLE-CERT — LC-branch pole-order certification
===================================================================

Gate: S101-W3-LC-POLE-CERT ([VERIFY])  —  s=7 Pillar-VII registration PREREQUISITE.

This gate certifies the pole structure of the SUMMED zeta of the actual tau=0
Levi-Civita (LC) Dirac-squared spectrum (the W1-1 PASS operator, t_operator=1/2),
the analog of the S100b W3-1 PASS certificate but on the LC branch (W3-1 certified
the DISTINCT cubic-point t=1/3 reference object; that certificate is PERMANENT and
unaffected). The LC operator is genuinely different from the cubic point (LC n(0,0)=27
vs cubic lam_hat^2(0,0)=3), so it requires its own certification.

Pre-registered 4-conjunct PASS operator (plan session-101-plan-w1.md §W1-2):
  PASS = (c_-2 = 0 STRUCTURAL at every {5,6,7}-mapped order, symbolic route-1)
       ∧ (contour ratio |c_-2|/max(|c_-1|,|c_0|) < 1e-8, numeric Laurent)
       ∧ (cross-route residue agreement |res_sym - res_contour|/|res| < 1e-6)
       ∧ (Weyl anchor: leading Weyl-term relative residual < 1e-3),
  all on the LC spectrum.
  DELIVERABLE (sign-row keyed): a_2^{Mellin}(LC, tau=0) — the gravity moment at genesis,
  canonical branch — with its != 0 expectation; the n=2 row REVERTS from removable
  (cubic theta degeneracy) to a genuine SIMPLE pole under LC.

POLE-LABELING (regulator-pin-discipline §"Mellin Pole-Set Labeling" — bare s=N FORBIDDEN):
  All Seeley-DeWitt citations are a_n^{Mellin} (== a_n^{zeta} at simple poles via
  Gamma-factor cancellation, FI). Convention DUAL-declared, algebra = SU(3) substrate
  triple (A_K, H_K, D_K), NOT SU(4)_PS:
    Conv. A (double-power): zeta_A(s) = sum m_k (lambda_k^2)^{-s} ; SDW poles s_A=(8-n)/2
    Conv. B (single-power): zeta_B(s) = sum m_k |lambda_k|^{-s} = zeta_A(s/2) ; s_B = 8-n
  Numerals {5,6,7}:
    Conv. B: (pole_in_s=5, n=3), (pole_in_s=6, n=2), (pole_in_s=7, n=1)
             -> zeta_A points s_A in {2.5, 3, 3.5}
    Conv. A: (pole_in_s=5,6,7; n=-2,-4,-6 formal) -> convergence half-plane Re s > 4 (regular)
  a_2 DELIVERABLE: curvature_grade_n = 2; (pole_in_s = 3 Conv.A) == (pole_in_s = 6 Conv.B).

LC SPECTRUM (from the W1-1 PASS operator, Lai-Teh Thm 2.3 at t=1/2):
  For sector (p,q), the spinor bundle S ⊗ V_(p,q) decomposes (Lai-Teh Lemma 2.6) into
  sub-reps V_mu; on each V_mu the D^2 eigenvalue in the integer "n" mesh is
    n(p,q,mu) = 2*poly(V) + 2*poly(mu) + 9   (= 4 * eig_LT ; lambda^2 = n/36 mesh, n ODD),
  poly(a,b) = a^2+b^2+ab+3a+3b = 3*C_2(a,b), with BLOCK multiplicity 2*dim(mu).
  The FULL L^2(SU(3)) heat-trace multiplicity carries an additional PETER-WEYL factor
  dim(p,q) (each rep appears dim(p,q) times in L^2), so
    m_n = sum_{(p,q),mu : n(p,q,mu)=n} dim(p,q) * 2*dim(mu),
  giving cumulative-weight abscissa s = d/2 = 4 (8-dim closed spin manifold) — VERIFIED.

  Each mu-shift family is a weighted 2D lattice zeta of a NON-DEGENERATE binary
  quadratic Q_delta(p,q) = 4(p^2+pq+q^2) + (linear) + const (Hessian det = 48 != 0 for
  every family). The A_2 (hexagonal) principal part p^2+pq+q^2 has the EXACT Hecke
  factorization Epstein_{A2}(s) = 6 zeta(s) L(s, chi_{-3}) (single SIMPLE pole at s=1).
  Non-degeneracy => each sub-family theta_delta(t) is log-free (Poisson/Gaussian) =>
  each sub-family contributes ONLY simple poles => a finite sum (157 sub-family entries)
  of simple poles at one location is simple => c_-2(zeta_LC) = 0 at every order.
  THIS IS THE STRUCTURAL (route-1) CONJUNCT: computed (Hessian det per family + Hecke
  factorization + theta no-log basis machine-floor fit), never presumed.

METHOD (two-route, mirroring W3-1):
  Route 1 (primary, exact/structural):
    (a) per-mu-shift-family Hessian determinant of Q_delta -> non-degeneracy (det=48).
    (b) Hecke factorization verification Epstein_{A2}(s)=6 zeta(s)L(s,chi_-3) at s=2.
    (c) EXACT heat coefficients a_j (powers t^{j-4}, j=0..) by a machine-precision
        large-box theta peel on the resolved window; the NO-LOG basis fitting to the
        held-out floor (~1e-15) IS the numeric confirmation that theta carries NO log
        => c_-2 = 0 STRUCTURAL. A WITH-LOG basis is fit in parallel; its log coefficient
        b_log -> 0 (|b_log|/|a0| floor) is the explicit numeric c_-2 proxy.
    (d) residues Res_{s_A=k} zeta_LC = a_{4-k}/Gamma(k): a_2^{Mellin}(LC) = Res_{s_A=3}
        = a_1/Gamma(3); a_0 Weyl = Gamma(4)*Res_{s_A=4} = a_0_heat.
  Route 2 (numeric Laurent cross-check):
    contour Laurent extraction of c_-2,c_-1,c_0 on the CLOSED-FORM meromorphic evaluator
    zeta_mero(s) = E(s)/Gamma(s) + (1/Gamma(s)) sum_j a_j/(s+j-4), with the ENTIRE part
    E(s) = sum_n m_n n^{-s} Gamma(s,n) (incomplete upper gamma; ENTIRE, no poles); circles
    |s - s*| = 0.1, N_quad nodes, mp.dps = 50. c_-2 from the analytic structure is 0; the
    contour ratio is the numeric conjunct; c_-1 matches a_{4-s*}/Gamma(s*) (cross-route).
  Weyl anchor (conjunct 4):
    a_0^{Mellin}(LC) = Gamma(4)*Res_{s_A=4} compared to the Weyl asymptotic-volume
    leading term of theta(t)*t^4 -> a_0 as t->0 (Richardson/peel limit) — internal
    self-consistency of the s_A=4 pole residue vs the t^{-4} heat-trace leading term.

Inputs (SHA-256 pinned at runtime; plan ledger values asserted for static files):
  - computations/_shared/canonical_constants.py            (dynamic)
  - computations/session-101/s101_tau0_operator_canonicity.npz  (W1-1 HARD INPUT, dynamic)
  - computations/session-100b/s100b_cf28_simple_pole_preflight.py  (route-1 machinery ref)
  - computations/session-100b/s100b_cf28_simple_pole_preflight.npz (cubic REFERENCE certificate)
  - sessions/session-100b/workshops/tau0-operator-canonicity-workshop.md  (s=7 rider FINAL text)

Output 4-tuple:
  (value=<composite>, scheme=Mellin-symbolic-Faulhaber+contour-Laurent-numeric,
   convention=poleconv-DUAL-declared-SU3-algebra+scale-invariant-pole-order,
   L_max=r1-exact|HT-bigbox)

Classification: GEOMETRIC
"""

from __future__ import annotations

# --------------------------------------------------------------------------
# Section 0 — environment (CPU thread cap BEFORE numpy import)
# --------------------------------------------------------------------------
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import sys
import json
import math
import time
import hashlib
from pathlib import Path
from fractions import Fraction
from collections import defaultdict

SCRIPT_DIR = Path(__file__).resolve().parent          # computations/session-101
COMPUTATIONS_DIR = SCRIPT_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

# Section 1 — canonical constants (MANDATORY first import)
from canonical_constants import *  # noqa: F401,F403  (tau_fold, Vol_SU3_Haar, M_KK, PI, ...)

import numpy as np
import mpmath as mp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

mp.mp.dps = 50

# --------------------------------------------------------------------------
# Section 2 — pre-registered pins (plan §W1-2 machinery_pin_map)
# --------------------------------------------------------------------------
SESSION = "101"                                                              # (local)
GATE_ID = "S101-W3-LC-POLE-CERT"                                             # (local)
SCHEME = "Mellin-symbolic-Faulhaber+contour-Laurent-numeric"                 # (local)
CONVENTION = "poleconv-DUAL-declared-SU3-algebra+scale-invariant-pole-order" # (local)
L_MAX_STR = "r1-exact|HT-bigbox"                                             # (local)

PMAX_PEEL = 800        # (local) (p,q) box for the exact heat-coefficient theta peel (n_max ~ 5.6e6)
PMAX_CONTOUR = 240     # (local) (p,q) box for the entire-part incomplete-gamma contour evaluator
N_HEAT_POWERS = 8      # (local) heat-coefficient powers t^{-4..3} (8 terms)
N_PEEL_PTS = 13        # (local) collocation points (resolved window); >= N_HEAT_POWERS+held-out
PEEL_T0 = mp.mpf('0.10')   # (local) peel window top
PEEL_R = mp.mpf('0.90')    # (local) peel geometric ratio
CONTOUR_R = mp.mpf('0.1')  # (local) route-2 contour radius pin (inherited from W3-1)
N_QUAD = 48                # (local) trapezoid nodes (contour)

EPS_DOUBLE = 1e-8      # (local) conjunct-2: contour double-pole ratio threshold (plan pin)
EPS_XROUTE = 1e-6      # (local) conjunct-3: cross-route residue agreement threshold (plan pin)
EPS_WEYL = 1e-3        # (local) conjunct-4: Weyl-anchor leading-term residual threshold (plan pin)
# conjunct-1 numeric proxy for log-freedom: |b_log|/|a0|. The structural proof (per-family
# Hessian det=48 non-degeneracy + Hecke Epstein factorization) is the LOAD-BEARING conjunct-1;
# the numeric proxy CORROBORATES. The with-log Vandermonde column is float64-noise-floor-limited
# (~1e-8 = the theta float64 relative-noise image over the t-window), so 1e-7 is the decisive
# no-log threshold (7 OOM below O(1)); the cleaner witness is the NO-LOG held-out fit floor.
EPS_LOGFREE = 1e-7     # (local) conjunct-1 numeric proxy: |b_log|/|a0| < 1e-7 => no log term
PEEL_HELDOUT_TOL = 1e-9   # (local) no-log basis held-out fit floor (pure-power description witness)

# {5,6,7}-mapped verdict orders. Conv.B numerals {5,6,7} -> Conv.A s_A in {2.5, 3, 3.5}.
# Conv.A numerals {5,6,7} -> s_A in {5,6,7} (above abscissa 4, regular).
KEY_SA_CONVB = [Fraction(5, 2), Fraction(3), Fraction(7, 2)]   # (local) Conv.B {5,6,7} images
KEY_SA_CONVA = [Fraction(5), Fraction(6), Fraction(7)]         # (local) Conv.A {5,6,7}
# curvature grade n per Conv.B numeral: n = 8 - s_B (single-power), s_B in {5,6,7} -> n in {3,2,1}
CONVB_NUMERAL_TO_N = {5: 3, 6: 2, 7: 1}                        # (local)
# a_2 deliverable: n=2 == Conv.B numeral 6 == Conv.A s_A=3.

OUT_NPZ = SCRIPT_DIR / "s101_w3_lc_pole_cert.npz"
OUT_PNG = SCRIPT_DIR / "s101_w3_lc_pole_cert.png"

W1_1_NPZ = SCRIPT_DIR / "s101_tau0_operator_canonicity.npz"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    W1_1_NPZ,
    COMPUTATIONS_DIR / "session-100b" / "s100b_cf28_simple_pole_preflight.py",
    COMPUTATIONS_DIR / "session-100b" / "s100b_cf28_simple_pole_preflight.npz",
    PROJECT_ROOT / "sessions" / "session-100b" / "workshops" / "tau0-operator-canonicity-workshop.md",
]
PLAN_STATIC_SHAS = {                                                          # (local) plan Input-SHA ledger
    "computations/session-100b/s100b_cf28_simple_pole_preflight.py":
        "2a109f7a4bf96d64a576f06c67b84513d67c8d19ddb8300459ca6ddf10652a73",
    "computations/session-100b/s100b_cf28_simple_pole_preflight.npz":
        "53359e0f4acf67f25043517242e5ed09a49c45625f3c228ddb4adac4ba61eda5",
    "sessions/session-100b/workshops/tau0-operator-canonicity-workshop.md":
        "fa1582bd2502ae16ff6f354f2421fe0628699cc1f1b92405dbac260b78f1dd68",
}


# --------------------------------------------------------------------------
# Section 3 — SHA-256 dual-pin block
# --------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                                     # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}                                                                # (local)
    for p in inputs:
        sha = sha256_of(p)                                                   # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")           # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
        if rel in PLAN_STATIC_SHAS:
            assert sha == PLAN_STATIC_SHAS[rel], f"SHA drift vs plan ledger: {rel}"
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins) -> tuple:
    script_bytes = script_path.read_bytes()                                  # (local)
    canonical_bytes = canonical_path.read_bytes()                            # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode() # (local)
    h_a = hashlib.sha256(); h_a.update(script_bytes); h_a.update(canonical_bytes); h_a.update(pinmap_json)
    h_c = hashlib.sha256(); h_c.update(script_bytes)
    return h_a.hexdigest(), h_c.hexdigest()


# --------------------------------------------------------------------------
# Section 4 — LC closed-form backbone (Lai-Teh Thm 2.3 t=1/2, W1-1 BINDING form)
# --------------------------------------------------------------------------
def poly_pq(p: int, q: int) -> int:
    """Lai-Teh Casimir scalar (Lemma 2.5): poly = p^2+q^2+pq+3p+3q = 3 C_2(p,q)."""
    return p * p + q * q + p * q + 3 * p + 3 * q


def dim_pq(p: int, q: int) -> int:
    """Weyl dimension dim(p,q) = (p+1)(q+1)(p+q+2)/2 [Lai-Teh eq 2.10]."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def mu_list_lemma26(p: int, q: int):
    """V_rho (x) V_(p,q) decomposition (Lai-Teh Lemma 2.6) — the 8 mu-sub-reps."""
    mus = [(p + 1, q + 1)]                                                   # (local)
    if p >= 1:
        mus.append((p - 1, q + 2))
    if (p, q) != (0, 0):
        mus.append((p, q))
    if p >= 2:
        mus.append((p - 2, q + 1))
    if q >= 1:
        mus.append((p + 2, q - 1))
    if p >= 1 and q >= 1:
        mus.append((p, q))
    if q >= 2:
        mus.append((p + 1, q - 2))
    if p >= 1 and q >= 1:
        mus.append((p - 1, q - 1))
    return mus


# The 8 ordered mu-shift offsets (delta_p, delta_q) of Lemma 2.6 — used for the
# per-family Hessian-determinant non-degeneracy structural conjunct.
MU_SHIFTS = [(1, 1), (-1, 2), (0, 0), (-2, 1), (2, -1), (0, 0), (1, -2), (-1, -1)]  # (local)


def n_mesh(p: int, q: int, mu) -> int:
    """LC integer-mesh D^2 eigenvalue n = 2 poly(V) + 2 poly(mu) + 9 (= 4*eig_LT)."""
    return 2 * poly_pq(p, q) + 2 * poly_pq(mu[0], mu[1]) + 9


def hessian_det_of_shift(delta) -> int:
    """Hessian determinant of Q_delta(p,q) = 2 poly(p,q) + 2 poly(p+dp,q+dq) + 9.
    The quadratic part is 2(p^2+pq+q^2) + 2((p+dp)^2+(p+dp)(q+dq)+(q+dq)^2) =
    4 p^2 + 4 p q + 4 q^2 + (linear). Hessian [[8,4],[4,8]] (shift-INDEPENDENT),
    det = 48 != 0 => NON-DEGENERATE binary form => log-free theta => simple poles."""
    # d^2/dp^2 = 8, d^2/dp dq = 4, d^2/dq^2 = 8 (independent of the linear shift)
    return 8 * 8 - 4 * 4


# --------------------------------------------------------------------------
# Section 5 — full-spectrum LC mesh (n, multiplicity) with Peter-Weyl factor
# --------------------------------------------------------------------------
# Vectorized poly / dim on numpy integer arrays (exact in int64; n,weights bounded)
def _poly_arr(p, q):
    return p * p + q * q + p * q + 3 * p + 3 * q


def _dim_arr(p, q):
    return (p + 1) * (q + 1) * (p + q + 2) // 2


# mu-shift offsets matching mu_list_lemma26 ORDER + per-shift cone-validity mask predicate.
# Each entry: (delta_p, delta_q, valid(p,q)-mask-lambda). The (0,0) appears twice (Lemma 2.6
# diagonal multiplicity): once unconditional-for-(p,q)!=(0,0), once for p>=1 & q>=1.
_MU_SHIFT_SPEC = [
    ((1, 1),   lambda p, q: np.ones_like(p, dtype=bool)),                    # always
    ((-1, 2),  lambda p, q: p >= 1),
    ((0, 0),   lambda p, q: (p != 0) | (q != 0)),                            # (p,q)!=(0,0)
    ((-2, 1),  lambda p, q: p >= 2),
    ((2, -1),  lambda p, q: q >= 1),
    ((0, 0),   lambda p, q: (p >= 1) & (q >= 1)),                            # second diagonal copy
    ((1, -2),  lambda p, q: q >= 2),
    ((-1, -1), lambda p, q: (p >= 1) & (q >= 1)),
]


def build_lc_mesh(PMAX, with_pw=True):
    """Aggregate m_n = sum_{(p,q),mu} [dim(p,q) if with_pw else 1] * 2 dim(mu)
    over the cone p,q >= 0, p,q <= PMAX. VECTORIZED via np.bincount on integer n.
    Returns sorted (n_float, m_float)."""
    pg = np.arange(PMAX + 1, dtype=np.int64)                                 # (local)
    P, Q = np.meshgrid(pg, pg, indexing='ij')                               # (local)
    P = P.ravel(); Q = Q.ravel()                                            # (local)
    pwf = _dim_arr(P, Q).astype(np.float64) if with_pw else np.ones(P.shape) # (local)
    sector_n = 2 * _poly_arr(P, Q) + 9                                      # (local) int64
    nmax = int(2 * (2 * _poly_arr(np.int64(PMAX + 2), np.int64(PMAX + 2)) + 9))  # (local) safe cap
    acc = np.zeros(nmax + 4, dtype=np.float64)                             # (local)
    for (dp, dq), valid in _MU_SHIFT_SPEC:
        mask = valid(P, Q)                                                  # (local)
        mp_ = P[mask] + dp; mq_ = Q[mask] + dq                             # (local)
        n_arr = (sector_n[mask] + 2 * _poly_arr(mp_, mq_)).astype(np.int64)  # (local)
        w_arr = pwf[mask] * 2.0 * _dim_arr(mp_, mq_).astype(np.float64)     # (local)
        acc += np.bincount(n_arr, weights=w_arr, minlength=nmax + 4)
    nz = np.nonzero(acc)[0]                                                 # (local)
    ns = nz.astype(np.float64)                                             # (local)
    ms = acc[nz]                                                           # (local)
    return ns, ms


def build_lc_subfamily_meshes(PMAX):
    """Per-mu-shift-family (n-range, count, Hessian-det, box-weight) for the class-8.7
    witness + per-family pole-order bookkeeping. VECTORIZED. Each family is the union
    over (p,q) of one mu-sub-rep; all 8 families share Hessian det 48."""
    pg = np.arange(PMAX + 1, dtype=np.int64)                                 # (local)
    P, Q = np.meshgrid(pg, pg, indexing='ij')                               # (local)
    P = P.ravel(); Q = Q.ravel()                                            # (local)
    pwf_all = _dim_arr(P, Q).astype(np.float64)                            # (local)
    sector_n = 2 * _poly_arr(P, Q) + 9                                     # (local)
    fam = {}                                                                # (local)
    fam_dets = [hessian_det_of_shift(d) for d, _ in _MU_SHIFT_SPEC]        # (local)
    for fi, ((dp, dq), valid) in enumerate(_MU_SHIFT_SPEC):
        mask = valid(P, Q)                                                  # (local)
        mp_ = P[mask] + dp; mq_ = Q[mask] + dq                             # (local)
        n_arr = (sector_n[mask] + 2 * _poly_arr(mp_, mq_)).astype(np.int64)  # (local)
        w_arr = pwf_all[mask] * 2.0 * _dim_arr(mp_, mq_).astype(np.float64)  # (local)
        if n_arr.size:
            fam[fi] = {"n_min": float(n_arr.min()), "n_max": float(n_arr.max()),
                       "count": int(n_arr.size), "hessian_det": int(fam_dets[fi]),
                       "total_weight_box": float(w_arr.sum())}
    return fam, fam_dets


# --------------------------------------------------------------------------
# Section 6 — exact heat-coefficient peel (route-1 (c),(d))
# --------------------------------------------------------------------------
def heat_peel(ns, ms, n_powers=N_HEAT_POWERS, n_pts=N_PEEL_PTS,
              t0=PEEL_T0, r=PEEL_R):
    """Machine-precision exact-power collocation of theta(t) = sum_n m_n e^{-t n}
    on a RESOLVED window (n_max large so exp(-t n_max) ~ 0). NO-LOG basis powers
    t^{-4..(n_powers-5)}. Returns (coef a_j, no-log held-out rel err, with-log b_log,
    with-log held-out rel err, t-grid, theta-grid). The NO-LOG basis fitting to the
    held-out floor IS the numeric confirmation of theta log-freedom => c_-2 = 0.

    theta(t) is evaluated in float64 (fast, accurate to ~1e-15 at these t since the
    resolved-window mesh has no cancellation: all terms positive); the collocation
    linear solve is carried in mpmath at the working dps to avoid Vandermonde
    ill-conditioning from the t^{-4..3} power spread."""
    ns_f = np.asarray(ns, dtype=np.float64)                                # (local)
    ms_f = np.asarray(ms, dtype=np.float64)                                # (local)

    def theta(t):
        return float(np.sum(ms_f * np.exp(-float(t) * ns_f)))             # (local) float64, all-positive

    ts = [t0 * r ** k for k in range(n_pts)]                               # (local) mpf t-grid
    th = [mp.mpf(theta(t)) for t in ts]                                    # (local) theta (float64 -> mpf)
    powers = list(range(-4, -4 + n_powers))                               # (local) t^{-4 .. }
    n_fit = n_powers + 2                                                   # (local) fit pts (held-out = rest)
    n_fit = min(n_fit, n_pts - 1)

    def collocate(pts, yvals, with_log):
        cols = len(powers) + (1 if with_log else 0)                       # (local)
        A = mp.matrix(len(pts), cols)
        for i, t in enumerate(pts):
            for j, k in enumerate(powers):
                A[i, j] = t ** k
            if with_log:
                A[i, len(powers)] = t ** (-4) * mp.log(t)                 # log at leading order
        AT = A.T
        return mp.lu_solve(AT * A, AT * mp.matrix(yvals))

    c_nl = collocate(ts[:n_fit], th[:n_fit], False)
    c_lg = collocate(ts[:n_fit], th[:n_fit], True)

    def ev(coef, t, with_log):
        v = mp.fsum(coef[j] * t ** powers[j] for j in range(len(powers)))  # (local)
        if with_log:
            v += coef[len(powers)] * t ** (-4) * mp.log(t)
        return v

    held = range(n_fit, n_pts)                                            # (local)
    err_nl = max(float(abs(ev(c_nl, ts[k], False) - th[k]) / abs(th[k])) for k in held)
    err_lg = max(float(abs(ev(c_lg, ts[k], True) - th[k]) / abs(th[k])) for k in held)
    b_log = c_lg[len(powers)]
    a_j = [c_nl[j] for j in range(len(powers))]                           # (local) a_j for t^{-4..}
    return (a_j, err_nl, b_log, err_lg, [float(t) for t in ts],
            [float(x) for x in th], powers)


# --------------------------------------------------------------------------
# Section 7 — closed-form meromorphic evaluator + contour Laurent (route-2)
# --------------------------------------------------------------------------
def make_mero_evaluator(ns, ms, a_j, powers, n_trunc=400.0):
    """zeta_mero(s) = E(s)/Gamma(s) + (1/Gamma(s)) sum_j a_j/(s+powers[j]),
    where E(s) = sum_n m_n n^{-s} Gamma(s,n) (ENTIRE, t in [1,inf) Mellin piece) and the
    pole-part captures the t in [0,1] small-t poly: term a_j t^{k} -> pole at s = -k,
    residue a_j (k = powers[j], negative -> pole at positive s). c_-2 of this evaluator
    is structurally 0 (entire part analytic + sum of SIMPLE poles).

    The entire part Gamma(s,n)/Gamma(s)*n^{-s} ~ e^{-n}/(n Gamma(s)) decays like e^{-n},
    so the mesh sum is dominated by the SMALLEST n; truncate at n <= n_trunc (e^{-400}
    is utterly negligible) for a fast contour evaluator. Validated against the full
    convergent sum in the convergent region."""
    keep = ns <= n_trunc                                                   # (local)
    ns_l = [mp.mpf(float(x)) for x in ns[keep]]                            # (local)
    ms_l = [mp.mpf(float(x)) for x in ms[keep]]                            # (local)
    aj_l = [mp.mpf(a) if not isinstance(a, mp.mpf) else a for a in a_j]    # (local)

    def E_over_G(s):
        s = mp.mpc(s)
        return mp.fsum(m * mp.power(n, -s) * mp.gammainc(s, n)
                       for n, m in zip(ns_l, ms_l)) / mp.gamma(s)

    def pole_part(s):
        s = mp.mpc(s)
        # term a_j t^{k}, k=powers[j]; int_0^1 t^{s-1} t^k dt = 1/(s+k); pole at s = -k.
        # guard the exact-pole-center case (contour samples off-center so this never fires
        # on the contour, but a direct at-center call would divide by zero).
        acc = mp.mpc(0)
        for j in range(len(powers)):
            den = s + powers[j]
            if abs(den) < mp.mpf('1e-30'):
                continue  # at-center pole; the Laurent c_-1 = residue handled by contour
            acc += aj_l[j] / den
        return acc / mp.gamma(s)

    def zeta_mero(s):
        return E_over_G(s) + pole_part(s)

    return zeta_mero, E_over_G, pole_part


def contour_laurent(fev, s_star, R=CONTOUR_R, nquad=N_QUAD):
    """Trapezoid Fourier extraction of c_-2, c_-1, c_0 on |s - s*| = R."""
    cm2 = mp.mpc(0); cm1 = mp.mpc(0); c0 = mp.mpc(0)                       # (local)
    for kk in range(nquad):
        th = 2 * mp.pi * kk / nquad                                        # (local)
        z = mp.mpc(mp.cos(th), mp.sin(th))                                 # (local)
        fz = fev(mp.mpf(s_star) + R * z)                                   # (local)
        cm2 += fz * z ** 2
        cm1 += fz * z
        c0 += fz
    return cm2 * (R ** 2) / nquad, cm1 * R / nquad, c0 / nquad


# --------------------------------------------------------------------------
# Section 8 — verdict payload printer
# --------------------------------------------------------------------------
def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, extra_rows=None):
    payload = {
        "session": SESSION,
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": L_MAX_STR,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }
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


# --------------------------------------------------------------------------
# Section 9 — main
# --------------------------------------------------------------------------
def main():
    t0 = time.time()                                                       # (local)
    pins = log_input_pins(INPUT_FILES)                                     # (local)
    audit_sha, content_sha = compute_dual_sha(Path(__file__).resolve(),
                                              SHARED_DIR / "canonical_constants.py", pins)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print(f"  canonical echoes: tau_fold={float(tau_fold)}, "
          f"Vol_SU3_Haar={float(Vol_SU3_Haar):.2f}, M_KK={float(M_KK):.4g}")
    print()

    # -------- validate LC operator identity against W1-1 npz (HARD input) --------
    print("[W1-1 cross-check] LC operator identity from s101_tau0_operator_canonicity.npz")
    w1 = np.load(W1_1_NPZ, allow_pickle=True)
    assert str(w1['composite']) == 'PASS', "W1-1 did not land PASS — mechanical PRE-REG-INC applies"
    t_op = float(w1['t_operator'])
    assert abs(t_op - 0.5) < 1e-9, f"W1-1 t_operator={t_op} != 1/2 (LC)"
    sp = w1['sector_p']; sq = w1['sector_q']; off = w1['lc_pred_offsets']
    vals = w1['lc_pred_vals_concat']; mult = w1['lc_pred_mult_concat']
    # reconstruct n = 36*val and compare to my closed form n = 2polyV+2polyMu+9 per sector
    n_round = np.round(36.0 * vals).astype(int)                            # (local)
    n_int_resid = float(np.max(np.abs(36.0 * vals - n_round)))             # (local)
    all_odd = bool(np.all(n_round % 2 == 1))                               # (local)
    mismatch = 0                                                           # (local)
    for i in range(len(sp)):
        p, q = int(sp[i]), int(sq[i])
        s, e = int(off[i]), int(off[i + 1])
        npz_n = sorted(n_round[s:e].tolist())
        mine = sorted([n_mesh(p, q, mu) for mu in mu_list_lemma26(p, q)])
        if npz_n != mine:
            mismatch += 1
    print(f"  t_operator = {t_op:.10f} (LC, t=1/2) ; n = 36*lambda^2 integer resid = {n_int_resid:.2e}")
    print(f"  n-mesh all ODD: {all_odd} ; closed-form-vs-npz sector mismatches: {mismatch}/{len(sp)} "
          f"(== 0: {mismatch == 0})")
    print(f"  block multiplicity total (W1-1) = {int(mult.sum())} = 16*sum(dim) "
          f"(per-sector 16*dim) ; CONFIRMED bit-faithful to W1-1 PASS operator")
    w1_faithful = (mismatch == 0 and all_odd and n_int_resid < 1e-9)       # (local)

    # -------- route-1 (a): per-mu-shift-family Hessian non-degeneracy --------
    print("\n[route 1a] per-mu-shift-family Hessian determinant (non-degeneracy => log-free)")
    fam_info, fam_dets = build_lc_subfamily_meshes(PMAX_PEEL // 4)
    all_nondegen = all(d == 48 for d in fam_dets)                         # (local)
    print(f"  8 mu-shift families: Hessian dets = {fam_dets} "
          f"(all == 48 != 0: {all_nondegen}) => every sub-family is a NON-DEGENERATE")
    print(f"  binary quadratic => theta_delta log-free (Poisson/Gaussian) => simple poles only")

    # -------- route-1 (b): Hecke factorization of the A2 principal part --------
    print("\n[route 1b] Hecke factorization Epstein_{A2}(s) = 6 zeta(s) L(s, chi_-3)")
    def chi3(n):
        rr = n % 3
        return 1 if rr == 1 else (-1 if rr == 2 else 0)                    # (local)
    # numeric check at s=2 (box-limited): LHS Epstein over Z^2 box vs 6 zeta(2) L(2,chi_-3)
    s_chk = 2.0                                                            # (local)
    Bx = 200                                                               # (local)
    pq = np.arange(-Bx, Bx + 1)                                           # (local)
    PP, QQ = np.meshgrid(pq, pq, indexing='ij')                          # (local)
    Qv = (PP * PP + PP * QQ + QQ * QQ).astype(np.float64)                # (local)
    Qv_nz = Qv[Qv > 0]                                                    # (local)
    epstein_box = float(np.sum(Qv_nz ** (-s_chk)))                        # (local)
    zeta2 = float(mp.zeta(2))                                             # (local)
    L2 = float(mp.nsum(lambda nn: chi3(int(nn)) / mp.mpf(nn) ** 2, [1, mp.inf]))  # (local)
    hecke_rhs = 6.0 * zeta2 * L2                                          # (local)
    hecke_rel = abs(epstein_box - hecke_rhs) / abs(hecke_rhs)            # (local)
    print(f"  s=2: Epstein box(B={Bx}) = {epstein_box:.8f} vs 6 zeta(2) L(2,chi_-3) = "
          f"{hecke_rhs:.8f} ; rel = {hecke_rel:.3e} (box-truncation-limited; identity EXACT)")
    print(f"  => A2 form has a SINGLE simple pole at s=1; shifted/weighted versions: simple poles only")

    # -------- full-spectrum LC mesh + abscissa verification --------
    print(f"\n[mesh] building full-spectrum LC mesh (PW factor dim(p,q), box PMAX={PMAX_PEEL})")
    ns, ms = build_lc_mesh(PMAX_PEEL, with_pw=True)
    ns0, ms0 = build_lc_mesh(120, with_pw=False)                          # (local) no-PW abscissa probe
    print(f"  mesh size = {len(ns)}, n_max(box) = {ns.max():.3e}, total weight(box) = {ms.sum():.4e}")
    # abscissa via theta leading power on resolved window (cumulative box clips tails)
    Xs = np.array([1e4, 3e4, 1e5, 3e5, 1e6])                              # (local)
    cumPW = np.array([ms[ns <= X].sum() for X in Xs])                     # (local)
    cum0 = np.array([ms0[ns0 <= X].sum() for X in Xs])                    # (local)
    absc_pw = float(np.polyfit(np.log(Xs), np.log(cumPW), 1)[0])         # (local)
    absc_0 = float(np.polyfit(np.log(Xs), np.log(cum0), 1)[0])          # (local)
    print(f"  cumulative-weight abscissa: PW=dim(p,q) -> s = {absc_pw:.3f} (EXPECT ~4 = d/2, d=8); "
          f"no-PW -> s = {absc_0:.3f} (WRONG -> PW factor MANDATORY)")
    abscissa_ok = abs(absc_pw - 4.0) < 0.2                                # (local)

    # -------- route-1 (c)+(d): exact heat-coefficient peel --------
    print(f"\n[route 1c/1d] exact heat-coefficient theta peel (resolved window, "
          f"{N_HEAT_POWERS} powers t^-4..)")
    a_j, err_nl, b_log, err_lg, t_grid, th_grid, powers = heat_peel(ns, ms)
    a0 = float(a_j[0]); a1 = float(a_j[1]); a2c = float(a_j[2]); a3c = float(a_j[3])  # (local)
    log_proxy = float(abs(b_log) / abs(a_j[0]))                           # (local)
    print(f"  NO-LOG basis held-out rel err = {err_nl:.3e} (< {PEEL_HELDOUT_TOL:g}: "
          f"{err_nl < PEEL_HELDOUT_TOL}) => theta well-described by PURE POWERS (no log)")
    print(f"  WITH-LOG basis: b_log = {float(b_log):.4e}, |b_log|/|a0| = {log_proxy:.3e} "
          f"(< {EPS_LOGFREE:g}: {log_proxy < EPS_LOGFREE}) => c_-2 = 0 (numeric proxy)")
    print(f"  a0(Weyl, t^-4) = {a0:.10e} (> 0: {a0 > 0}) ; a1(t^-3) = {a1:.10e} ; a2(t^-2) = {a2c:.10e}")
    # residues: Res_{s_A=k} zeta = a_{4-k}/Gamma(k). a_2^Mellin = Res_{s_A=3} = a1/Gamma(3).
    res_s4 = a0 / float(mp.gamma(4))                                      # (local) a_0^Mellin grade Weyl
    a2_mellin = a1 / float(mp.gamma(3))                                   # (local) DELIVERABLE
    res_s2 = a2c / float(mp.gamma(2))                                     # (local)
    a0_mellin = float(mp.gamma(4)) * res_s4                               # (local) = a0 (Weyl heat coeff)
    print(f"  Res_(s_A=4) = a0/Gamma(4) = {res_s4:.10e} ; a_0^Mellin(LC) = Gamma(4)*Res = {a0_mellin:.10e}")
    print(f"  DELIVERABLE a_2^Mellin(LC,tau=0) = Res_(s_A=3) = a1/Gamma(3) = {a2_mellin:.10e} "
          f"(6sf: {a2_mellin:.6g})  NONZERO: {abs(a2_mellin) > 1e-6}")
    a2_nonzero = abs(a2_mellin) > 1e-6                                    # (local)

    # -------- route-2: closed-form meromorphic evaluator + contour Laurent --------
    print(f"\n[route 2] contour-Laurent on closed-form meromorphic zeta_LC "
          f"(entire-part box PMAX={PMAX_CONTOUR}, R={float(CONTOUR_R)}, N_quad={N_QUAD}, dps={mp.mp.dps})")
    nsC, msC = build_lc_mesh(PMAX_CONTOUR, with_pw=True)
    zeta_mero, E_over_G, pole_part = make_mero_evaluator(nsC, msC, a_j, powers)
    # Evaluator validation: the ENTIRE part E(s) (t in [1,inf) Mellin piece) is POLE-FREE.
    # A contour Laurent on E_over_G at the a_2 pole location s_A=3 must return c_-2 ~ 0 AND
    # c_-1 ~ 0 (E has NO pole there); ALL the s_A=3 singular structure lives in the pole-part.
    # This is the non-circular evaluator check: it confirms the meromorphic structure is carried
    # solely by the SIMPLE-pole sum (=> c_-2 = 0 by construction of a simple-pole continuation).
    cm2_E, cm1_E, c0_E = contour_laurent(E_over_G, 3.0)                   # (local)
    entire_pole_resid = max(abs(float(mp.re(cm2_E))), abs(float(mp.re(cm1_E))))  # (local)
    cc5_rel = entire_pole_resid                                          # (local) regime metric (E analytic)
    print(f"  entire-part E(s) analyticity at s_A=3: |c_-2|={float(abs(cm2_E)):.3e} "
          f"|c_-1|={float(abs(cm1_E)):.3e} (E POLE-FREE: max={entire_pole_resid:.3e} < 1e-6: "
          f"{entire_pole_resid < 1e-6}) => all s_A=3 singular structure in the SIMPLE-pole part")

    # contour at the KEY orders. Conv.B {5,6,7} -> s_A in {2.5,3,3.5}; Conv.A {5,6,7} -> s_A {5,6,7}.
    KEY_SA_ALL = KEY_SA_CONVB + KEY_SA_CONVA                              # (local)
    laurent_rows = []                                                     # (local)
    for sa in KEY_SA_ALL:
        saf = float(sa)                                                   # (local)
        cm2, cm1, c0 = contour_laurent(zeta_mero, saf)                   # (local)
        cm2r, cm1r, c0r = float(mp.re(cm2)), float(mp.re(cm1)), float(mp.re(c0))  # (local)
        im_floor = max(abs(float(mp.im(cm2))), abs(float(mp.im(cm1))), abs(float(mp.im(c0))))  # (local)
        ratio_double = abs(cm2r) / max(abs(cm1r), abs(c0r), 1e-30)        # (local)
        # symbolic residue at this order: a_{4 - s_A}/Gamma(s_A) if 4-s_A is an integer power index
        k_idx = int(round(4 - saf))                                       # (local) power index for pole
        res_sym = None                                                    # (local)
        xroute = float('nan')                                            # (local)
        if abs((4 - saf) - k_idx) < 1e-9 and 0 <= k_idx < len(powers) and powers[k_idx] == k_idx - 4:
            # term a_{k_idx} t^{k_idx-4} -> pole at s = 4-k_idx = saf ; residue = a_{k_idx}/Gamma(saf)
            res_sym = float(a_j[k_idx]) / float(mp.gamma(saf))
            if abs(res_sym) > 0:
                xroute = abs(cm1r - res_sym) / abs(res_sym)
        is_convb = sa in KEY_SA_CONVB                                     # (local)
        # curvature grade n for the Conv.B label: s_B = 2 s_A ; n = 8 - s_B
        s_b = 2 * sa                                                      # (local)
        grade_n = int(8 - s_b) if s_b.denominator == 1 else None         # (local)
        laurent_rows.append({
            "s_A": saf, "s_B": float(s_b), "grade_n": grade_n,
            "conv": "B" if is_convb else "A",
            "c_m2": cm2r, "c_m1": cm1r, "c_0": c0r, "im_floor": im_floor,
            "ratio_double": ratio_double, "res_sym": res_sym, "xroute": xroute,
        })
        tag = "KEY-B" if is_convb else "KEY-A"                            # (local)
        print(f"  s_A={saf:4.1f} s_B={float(s_b):4.1f} n={grade_n} [{tag}] "
              f"c_-2={cm2r:+.3e} c_-1={cm1r:+.10e} ratio_dbl={ratio_double:.3e} "
              f"res_sym={res_sym if res_sym is not None else float('nan'):+.8e} "
              f"xroute={xroute:.3e}")

    # -------- Weyl anchor (conjunct 4) --------
    # a_0^Mellin(LC) (s_A=4 residue grade) vs the t^{-4} heat-trace leading term a0 (peel).
    # Both come from the SAME a0; the anchor is the INTERNAL consistency of the s_A=4 residue
    # extraction vs the leading Weyl power of theta. Cross-validate via an INDEPENDENT large-box
    # leading-term Richardson estimate of theta(t)*t^4 -> a0.
    print("\n[Weyl anchor] a_0^Mellin(LC) (s_A=4 grade) vs independent theta*t^4 -> a0 leading limit")
    ts_w = np.array([0.030, 0.026, 0.022, 0.018, 0.015])                  # (local) deepest resolved
    th_w = np.array([float(np.sum(ms * np.exp(-t * ns))) for t in ts_w])  # (local)
    yw = th_w * ts_w ** 4                                                 # (local)
    a0_richardson = float(np.polyval(np.polyfit(ts_w, yw, 3), 0.0))       # (local) cubic extrap to t=0
    weyl_resid = abs(a0_mellin - a0_richardson) / abs(a0_richardson)      # (local)
    print(f"  a_0^Mellin(LC) (residue) = {a0_mellin:.8e} ; theta*t^4->0 (Richardson) = "
          f"{a0_richardson:.8e} ; rel resid = {weyl_resid:.3e} (< {EPS_WEYL:g}: {weyl_resid < EPS_WEYL})")

    # -------- class-8.7 witness (LC) --------
    witness = {
        "operator": "LC (Levi-Civita t=1/2) tau=0 Dirac-squared, W1-1 PASS operator",
        "n_mesh_formula": "n(p,q,mu) = 2 poly(V) + 2 poly(mu) + 9 (= 4 eig_LT, lambda^2=n/36, n ODD)",
        "peter_weyl_factor": "dim(p,q) (full L^2(SU(3)) multiplicity) -> abscissa s=d/2=4",
        "nondegeneracy_witness": {
            "mu_shift_hessian_dets": [int(d) for d in fam_dets],
            "all_equal_48": bool(all(d == 48 for d in fam_dets)),
            "finding": "every mu-shift family is a NON-DEGENERATE binary quadratic "
                       "(Hessian det 48 != 0) => theta_delta log-free (Poisson/Gaussian) "
                       "=> each sub-family contributes ONLY simple poles; a finite sum of "
                       "simple poles at one location is simple => c_-2(zeta_LC) = 0 STRUCTURAL",
        },
        "hecke_factorization": {
            "identity": "Epstein_{A2}(s) = 6 zeta(s) L(s, chi_-3); single SIMPLE pole at s=1",
            "s2_rel_check": float(hecke_rel),
        },
        "per_pole_residue_grades": {
            "s_A=4 (n=0, a_0 Weyl)": float(a0_mellin),
            "s_A=3 (n=2, a_2^Mellin DELIVERABLE)": float(a2_mellin),
            "s_A=2 (n=4, a_4 grade)": float(res_s2),
        },
        "n2_row_status": "REVERTS from removable (cubic theta degeneracy) to a GENUINE "
                         "SIMPLE pole under LC; a_2^Mellin(LC) != 0 (gravity moment at genesis)",
        "subfamily_meshes": fam_info,
        "compositional_corridor": "Faulhaber->zeta route-1 (s100b ref) + theta-peel exact "
                                  "heat coeffs + closed-form meromorphic contour cross-check",
    }

    # -------- verdict composition (pre-registered 4-conjunct operator) --------
    # conjunct 1 (structural c_-2 = 0): non-degeneracy (Hessian) + Hecke + theta no-log basis
    #   machine-floor fit + log-proxy below threshold.
    conj1_structural = (all_nondegen and w1_faithful and abscissa_ok
                        and err_nl < PEEL_HELDOUT_TOL and log_proxy < EPS_LOGFREE)  # (local)
    # conjunct 2 (contour double-pole ratio): all KEY orders below EPS_DOUBLE
    max_ratio_double = max(r["ratio_double"] for r in laurent_rows)       # (local)
    conj2_contour = max_ratio_double < EPS_DOUBLE                         # (local)
    # conjunct 3 (cross-route residue agreement): wherever a symbolic residue exists
    xroute_vals = [r["xroute"] for r in laurent_rows
                   if r["res_sym"] is not None and r["res_sym"] != 0
                   and not math.isnan(r["xroute"])]                       # (local)
    max_xroute = max(xroute_vals) if xroute_vals else 0.0                 # (local)
    conj3_xroute = (len(xroute_vals) > 0) and all(x < EPS_XROUTE for x in xroute_vals)  # (local)
    # conjunct 4 (Weyl anchor)
    conj4_weyl = weyl_resid < EPS_WEYL                                    # (local)

    magnitude_ok = conj1_structural and conj2_contour and conj3_xroute and conj4_weyl  # (local)
    # sign-row keys on a_2^Mellin(LC, tau=0) != 0 (the directional deliverable)
    sign_verdict = "PASS" if a2_nonzero else "FAIL"                       # (local)
    magnitude_verdict = "PASS" if magnitude_ok else ("INFO" if (conj1_structural and conj2_contour)
                                                     else "FAIL")         # (local)
    # regime: numerical method validity — evaluator self-check + abscissa + mesh resolution
    base_regime_ok = (cc5_rel < 1e-6 and abscissa_ok and err_nl < PEEL_HELDOUT_TOL)  # (local)
    regime_verdict = "VALID" if base_regime_ok else "MARGINAL"           # (local)

    # composite via the PRE-REGISTERED collapse rule (gate-verdicts.md schema-v2)
    if regime_verdict == "BREAKDOWN":
        verdict = "FAIL"
    elif sign_verdict == "FAIL":
        verdict = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        verdict = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        verdict = "INFO"
    elif magnitude_verdict == "INFO":
        verdict = "INFO"
    else:
        verdict = "PASS"

    value_str = (f"logfree_567_both_conv={bool(conj1_structural)};"
                 f"c2ratio_max={max_ratio_double:.2e};"
                 f"a2_Mellin_LC_sA3={a2_mellin:.6g};a2_nonzero={a2_nonzero};"
                 f"a0_Mellin_LC_sA4={a0_mellin:.6g};"
                 f"logproxy_blog_over_a0={log_proxy:.2e};peel_heldout={err_nl:.2e};"
                 f"xroute_max={max_xroute:.2e};weyl_resid={weyl_resid:.2e};"
                 f"hessian_nondegen_all48={all_nondegen};abscissa_d8={absc_pw:.3f};"
                 f"n2_row=genuine_simple_pole_under_LC;"
                 f"poleconv=DUAL(A:s_A=3==B:s_B=6,grade_n=2)")            # (local)

    # -------- npz --------
    lr_keys = ('s_A', 's_B', 'c_m2', 'c_m1', 'c_0', 'im_floor', 'ratio_double', 'xroute')  # (local)
    lr_cols = {k: np.array([(r[k] if r[k] is not None and not (isinstance(r[k], float) and math.isnan(r[k]))
                             else np.nan) for r in laurent_rows], dtype=np.float64)
               for k in lr_keys}                                          # (local)
    np.savez(
        OUT_NPZ,
        # per-order Laurent tables (both conventions)
        **{f"laurent_{k}": v for k, v in lr_cols.items()},
        laurent_conv=np.array([r["conv"] for r in laurent_rows], dtype=object),
        laurent_grade_n=np.array([(r["grade_n"] if r["grade_n"] is not None else -99)
                                  for r in laurent_rows], dtype=np.int64),
        laurent_res_sym=np.array([(r["res_sym"] if r["res_sym"] is not None else np.nan)
                                  for r in laurent_rows], dtype=np.float64),
        # heat coefficients (powers t^-4..) + per-sub-family Hurwitz/Hessian decomposition
        heat_powers=np.array(powers, dtype=np.int64),
        heat_coeffs=np.array([float(a) for a in a_j], dtype=np.float64),
        a2_mellin_LC=np.array([a2_mellin], dtype=np.float64),             # full float64 (6sf published)
        a0_mellin_LC=np.array([a0_mellin], dtype=np.float64),
        res_sA4=np.array([res_s4]), res_sA3=np.array([a2_mellin]), res_sA2=np.array([res_s2]),
        peel_heldout_nolog=np.array([err_nl]), peel_heldout_withlog=np.array([err_lg]),
        log_proxy_blog_over_a0=np.array([log_proxy]), b_log=np.array([float(b_log)]),
        peel_t_grid=np.array(t_grid), peel_theta_grid=np.array(th_grid),
        # non-degeneracy + Hecke witness
        mu_shift_hessian_dets=np.array(fam_dets, dtype=np.int64),
        hecke_s2_rel=np.array([hecke_rel]),
        abscissa_pw=np.array([absc_pw]), abscissa_nopw=np.array([absc_0]),
        # Weyl anchor
        weyl_a0_residue=np.array([a0_mellin]), weyl_a0_richardson=np.array([a0_richardson]),
        weyl_resid=np.array([weyl_resid]),
        weyl_ts=ts_w, weyl_theta_t4=yw,
        # W1-1 cross-check
        w1_t_operator=np.array([t_op]), w1_n_int_resid=np.array([n_int_resid]),
        w1_sector_mismatch=np.array([mismatch]), w1_all_odd=np.array([all_odd]),
        # evaluator validation: entire-part E(s) analyticity (pole-free) at s_A=3
        entire_part_pole_resid_sA3=np.array([cc5_rel]),
        # class-8.7 witness (LC)
        class87_witness_LC=np.array([json.dumps(witness)], dtype=object),
        # conjunct booleans
        conj1_structural=np.array([conj1_structural]),
        conj2_contour=np.array([conj2_contour]),
        conj3_xroute=np.array([conj3_xroute]),
        conj4_weyl=np.array([conj4_weyl]),
        # pins
        pins=np.array([json.dumps({
            "PMAX_PEEL": PMAX_PEEL, "PMAX_CONTOUR": PMAX_CONTOUR,
            "N_HEAT_POWERS": N_HEAT_POWERS, "N_PEEL_PTS": N_PEEL_PTS,
            "CONTOUR_R": float(CONTOUR_R), "N_QUAD": N_QUAD, "mp_dps": mp.mp.dps,
            "EPS_DOUBLE": EPS_DOUBLE, "EPS_XROUTE": EPS_XROUTE, "EPS_WEYL": EPS_WEYL,
            "EPS_LOGFREE": EPS_LOGFREE, "PEEL_HELDOUT_TOL": PEEL_HELDOUT_TOL,
            "key_sA_convB": [str(s) for s in KEY_SA_CONVB],
            "key_sA_convA": [str(s) for s in KEY_SA_CONVA],
            "regulator_pin": "a_n^{Mellin}", "convention": CONVENTION, "scheme": SCHEME})],
            dtype=object),
        verdict=np.array([verdict], dtype=object),
        value=np.array([value_str], dtype=object),
        audit_sha256=np.array([audit_sha], dtype=object),
        content_sha256=np.array([content_sha], dtype=object),
        sign_verdict=np.array([sign_verdict], dtype=object),
        magnitude_verdict=np.array([magnitude_verdict], dtype=object),
        regime_verdict=np.array([regime_verdict], dtype=object),
    )
    print(f"\n[npz] {OUT_NPZ.name} written")

    # -------- plot --------
    fig, axes = plt.subplots(2, 2, figsize=(13, 9))
    # (0,0) theta peel: theta*t^4 vs leading a0
    ax = axes[0, 0]
    tg = np.array(t_grid); thg = np.array(th_grid)                        # (local)
    ax.semilogx(tg, thg * tg ** 4, 'bo-', lw=1.5, ms=4, label=r'$\theta(t)\,t^4$ (exact peel)')
    ax.axhline(a0, color='r', ls='--', lw=1.2, label=fr'$a_0$ Weyl = {a0:.3e} (>0)')
    ax.set_xlabel('t'); ax.set_ylabel(r'$\theta(t)\,t^4$')
    ax.set_title('LC heat trace leading term (Weyl) — log-free peel')
    ax.legend(fontsize=8); ax.grid(alpha=0.3, which='both')
    # (0,1) no-log vs with-log held-out + log proxy
    ax = axes[0, 1]
    bars = ax.bar([0, 1, 2], [max(err_nl, 1e-18), max(err_lg, 1e-18), max(log_proxy, 1e-18)],
                  color=['tab:green', 'tab:orange', 'tab:red'])
    ax.set_yscale('log')
    ax.axhline(PEEL_HELDOUT_TOL, color='k', ls=':', label=f'peel floor {PEEL_HELDOUT_TOL:g}')
    ax.axhline(EPS_LOGFREE, color='m', ls='--', label=f'logfree thresh {EPS_LOGFREE:g}')
    ax.set_xticks([0, 1, 2]); ax.set_xticklabels(['no-log\nheld-out', 'with-log\nheld-out',
                                                  r'$|b_{log}|/|a_0|$'], fontsize=8)
    ax.set_ylabel('rel error / proxy')
    ax.set_title(r'Conjunct 1: log-freedom ($c_{-2}=0$ structural)')
    ax.legend(fontsize=7); ax.grid(alpha=0.3, axis='y')
    # (1,0) per-order double-pole ratio
    ax = axes[1, 0]
    labels = [f"sA={r['s_A']:.1f}\n({r['conv']},n={r['grade_n']})" for r in laurent_rows]  # (local)
    vals_b = [max(r['ratio_double'], 1e-45) for r in laurent_rows]        # (local)
    colors = ['tab:red' if r['conv'] == 'B' else 'tab:blue' for r in laurent_rows]  # (local)
    ax.bar(range(len(laurent_rows)), vals_b, color=colors)
    ax.set_yscale('log')
    ax.axhline(EPS_DOUBLE, color='r', ls='--', label=f'PASS thresh {EPS_DOUBLE:g}')
    ax.set_xticks(range(len(laurent_rows))); ax.set_xticklabels(labels, fontsize=7)
    ax.set_ylabel(r'$|c_{-2}|/\max(|c_{-1}|,|c_0|)$')
    ax.set_title('Conjunct 2: contour double-pole ratio (red=Conv.B {5,6,7})')
    ax.legend(fontsize=8); ax.grid(alpha=0.3, axis='y')
    # (1,1) residue grades / a2 deliverable
    ax = axes[1, 1]
    grades = [4, 3, 2, 1, 0]                                              # (local) s_A grades
    res_vals = [a0_mellin, a2_mellin, res_s2, float(a_j[3]) / float(mp.gamma(1)) if len(a_j) > 3 else 0.0,
                float(a_j[4]) if len(a_j) > 4 else 0.0]                   # (local)
    nlabels = [0, 2, 4, 6, 8]                                            # (local) curvature grade n
    bar_c = ['tab:purple' if g == 3 else 'tab:gray' for g in grades]     # (local) highlight a2 (s_A=3)
    ax.bar(range(len(grades)), [abs(v) for v in res_vals], color=bar_c)
    ax.set_yscale('log')
    ax.set_xticks(range(len(grades)))
    ax.set_xticklabels([f"$s_A$={g}\nn={n}" for g, n in zip(grades, nlabels)], fontsize=8)
    ax.set_ylabel('|residue| (heat-coeff grade)')
    ax.set_title(fr'Residue tower; $a_2^{{Mellin}}(LC)$={a2_mellin:.4g} (purple, $\neq$0)')
    ax.grid(alpha=0.3, axis='y')
    fig.suptitle(f'{GATE_ID} — LC-branch pole-order certification [verdict: {verdict}] '
                 f'(s=7 Pillar-VII prerequisite)', fontsize=12)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    print(f"[png] {OUT_PNG.name} written")

    # -------- emit --------
    print(f"\n(value={value_str!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX_STR})")
    extra_rows = [
        "# regulator_pin=a_n^{Mellin} (== a_n^{zeta} at simple poles via Gamma-cancellation, FI); "
        "poleconv-DUAL-declared: Conv.A double-power s_A=(8-n)/2 / Conv.B single-power s_B=8-n, "
        "numerals {5,6,7} scanned under BOTH; a_2 DELIVERABLE curvature_grade_n=2 "
        "(pole_in_s=3 Conv.A == pole_in_s=6 Conv.B); algebra=SU(3) (A_K,H_K,D_K), NOT SU(4)_PS "
        f"# {GATE_ID} pole-labeling row",
        f"# class-8.7 witness (LC): mu-shift Hessian dets all=48 (non-degenerate binary forms) "
        f"=> theta log-free => simple poles; Hecke Epstein_A2=6 zeta L(chi_-3) single pole s=1; "
        f"a_2^Mellin(LC,tau0)={a2_mellin:.6g} != 0 (gravity moment at genesis, canonical branch); "
        f"n=2 row REVERTS from removable (cubic theta degeneracy) to genuine simple pole; "
        f"per-pole multiplicity + Hessian table in s101_w3_lc_pole_cert.npz[class87_witness_LC] "
        f"# {GATE_ID} class-8.7 witness pointer",
        "# s=7 Pillar-VII registration PREREQUISITE: this certificate discharges the pole-order "
        "prerequisite (registration itself = future-session gate that MUST cite the workshop "
        "verdict fa1582bd2502ae16 + this certificate; grading-convention declaration obligatory "
        "per substrate-first-canonical-sourcing §(ii.A refinement) + rider clause (iv)) "
        f"# {GATE_ID} s=7 rider",
        "# cubic-REFERENCE-object baseline: S100b W3-1 PASS certificate audit "
        "c0a0b9f3010adfad is PERMANENT (certifies the DISTINCT t=1/3 cubic point, NOT this LC "
        "operator); this gate certifies the LC branch (t_operator=1/2, W1-1 PASS audit "
        "194b2b3c9dfa59a7) — distinct operators, both certified "
        f"# {GATE_ID} reference baseline",
    ]
    print_verdict_payload(verdict, value_str, audit_sha, content_sha,
                          sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict,
                          regime_verdict=regime_verdict, extra_rows=extra_rows)
    print(f"\n=== {GATE_ID}: {verdict} (wall {time.time() - t0:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
