#!/usr/bin/env python3
"""
S100b W3-1 S100b-CF28-SIMPLE-POLE-PREFLIGHT — CF28 simple-vs-log pole-order pre-flight
=======================================================================================

Gate: S100b-CF28-SIMPLE-POLE-PREFLIGHT ([VERIFY])

Pre-registered threshold (plan sessions/session-plan/session-100b-plan-w3.md §W3-1):
  PASS iff for every s* mapped from {5,6,7} under BOTH pole conventions:
    [route 1: c_-2(s*) = 0 structurally (exhaustive collision enumeration)] AND
    [route 2: |c_-2(s*)| / max(|c_-1(s*)|, |c_0(s*)|, 1e-30) < 1e-8] AND
    [routes agree: |c_-1^r1 - c_-1^r2| / |c_-1^r1| < 1e-6 wherever c_-1 != 0] AND
    [a_0-pole internal Weyl-consistency residual < 1e-3] AND
    [prong-B shell exponents within +/-0.5 of analytic; L-stability <= 2x analytic
     tail at s_A in {5,6}]
  FAIL iff a log term is present at a {5,6,7}-mapped order (structural c_-2 != 0
    confirmed by both routes, or a continuation defect adjudicated by the r1/r2 split).
  INFO iff the route-1 j-sum interchange justification fails at a {5,6,7}-mapped point,
    OR a registration-target functional weight is non-convergent with no in-session
    continuation.

POLE-LABELING (regulator-pin-discipline §"Mellin Pole-Set Labeling" — bare s=N FORBIDDEN):
  All Seeley-DeWitt citations herein are a_n^{Mellin} (== a_n^{zeta} at simple poles via
  Gamma-factor cancellation, FI). Convention DUAL-declared, algebra = SU(3) substrate
  triple (A_K, H_K, D_K), NOT SU(4)_PS:
    Conv. A (double-power): zeta_A(s) = sum m_k (lambda_k^2)^(-s); SDW poles s_A=(8-n)/2
    Conv. B (single-power): zeta_B(s) = sum m_k |lambda_k|^(-s) = zeta_A(s/2); s_B = 8-n
  Numerals {5,6,7}:
    Conv. B: (pole_in_s=5, n=3), (pole_in_s=6, n=2), (pole_in_s=7, n=1)
             -> zeta_A points s_A in {2.5, 3, 3.5}
    Conv. A: (pole_in_s=5,6,7; n=-2,-4,-6 formal) -> convergence half-plane Re s > 4
  Exotic locus (Fucci-Stanfill Gamma-collision candidates): s_A in {0,-1,-2,-3}
             <-> n in {8,10,12,14}.

METHOD (two-prong, per plan):
  PRONG A route 1 (primary, exact): full-PW cubic-point zeta
      zeta_A(s) = 4 sum_{u,v>=1} u^2 v^2 (u+v)^2 (u^2+uv+v^2)^(-s)
    [16*dim^2 = 4 u^2v^2(u+v)^2 with dim = uv(u+v)/2; lambda_hat^2 = u^2+uv+v^2;
     pole ORDER is invariant under eigenvalue rescaling (Chain 3)].
    Binomial reduction: (u^2+uv+v^2)^(-s) = (u+v)^(-2s) (1 - uv/(u+v)^2)^(-s),
    |uv/(u+v)^2| <= 1/4 < 1 uniformly. Per j-term the inner sum over u+v=N is the
    EXACT integer-coefficient polynomial S_j(N) = sum_{u=1}^{N-1} u^{j+2}(N-u)^{j+2}
    (Faulhaber/Bernoulli closed form, exact rationals). Every term carries exactly ONE
    zeta_R/zeta_Hurwitz factor and a polynomial-in-s prefactor (s)_j/j! => per-term
    Laurent order <= 1 at every point; a sum of simple poles at one location is simple
    (never a double pole). Exhaustive collision enumeration over all (j,d).
    NUMERICAL-EVALUATION NOTE (honest in-session structural correction, disclosed):
    the naive "zeta_R(w)-1" monomial form is mathematically exact but numerically
    catastrophic (the monomial expansion of S_j(2)=1 carries Bernoulli-sized terms
    ~1e58 at j=40 -> ~58-digit cancellation at the N=2 term). The evaluator therefore
    uses the algebraically IDENTICAL Hurwitz split at N_0 = 64:
      sum_{N>=2} N^{2-2s-2j} S_j(N)
        = sum_{N=2}^{63} N^{2-2s-2j} S_j(N)  [exact integers, entire in s]
        + sum_d c_{j,d} zeta_H(2s+2j-2-d, 64)  [leading-dominated, no cancellation]
    Res_w zeta_H(w, a) = 1 for every a, so the POLE/RESIDUE bookkeeping (the
    gate-bearing object) is split-independent; N_0-independence is verified in-run.
  PRONG A route 2 (numerical cross-check): contour Laurent extraction c_-2, c_-1, c_0
    on circles |s - s*| = 0.1, N_quad = 64 trapezoid nodes, mp.dps = 50.
  Heat-trace dual artifact: K(t) = sum 4u^2v^2(u+v)^2 exp(-t lambda_hat^2) partial sums
    (pin L_huge = 4000; all terms with t*lambda_hat^2 > X_CUT = 160 are below 1e-40
    relative and covered by the rigorous integral tail bound) + no-log asymptotic
    series overlay (Mellin dictionary Chain 1 makes pole-order and heat-trace log-term
    statements EQUIVALENT).
  PRONG B (tau_fold consistency + convergence certificate): s84 L12 cache (sector
    (4,4) reconstructed in-script via get_irrep + dirac_operator_on_irrep at
    tau_fold = 0.19; lineage cross-checks rebuild (2,2) and (4,3) against the cache);
    Conv.-A direct sums at s_A in {5,6,7}; L=12-vs-L=10 stability vs 2x analytic tail
    at s_A in {5,6}; empirical shell-decay exponents (log-log fit, L in [6,12]) vs
    analytic 7-2s (double-power) and 7-s (single-power) within +/-0.5.

Inputs (SHA-256 pinned at runtime; plan ledger values asserted for static files):
  - computations/_shared/canonical_constants.py            (dynamic)
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz
  - computations/_shared/dirac_spectrum.py
  - computations/_shared/_analytic_zeta.py                 (INFO-route corridor pin)
  - computations/_shared/_cm_1995_residue_formula.py       (FULL-physical corridor template)
  - downloads/research-sweep-s99/spectral-geometry-math/01_Lai-Teh_...SU3.pdf

Output 4-tuple:
  (value=<composite>, scheme=Mellin-symbolic-Faulhaber+contour-Laurent-numeric,
   convention=poleconv-DUAL-declared-SU3-algebra+scale-invariant-pole-order,
   L_max=r1-exact|HT4000|prongB-12)

Classification: GEOMETRIC
"""

from __future__ import annotations

# --------------------------------------------------------------------------
# Section 0 — environment (CPU thread cap BEFORE numpy import; GPU via torch)
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

SCRIPT_DIR = Path(__file__).resolve().parent          # computations/session-100b
COMPUTATIONS_DIR = SCRIPT_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

# Section 1 — canonical constants (MANDATORY first import)
from canonical_constants import *  # noqa: F401,F403  (tau_fold, Vol_SU3_Haar, residue_s6_PS_Linf, M_KK, PI, ...)

import numpy as np
import mpmath as mp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

mp.mp.dps = 50                       # plan pin mp_dps=50 (route-2 / _analytic_zeta precision pin)

# --------------------------------------------------------------------------
# Section 2 — pre-registered pins (plan §W3-1 machinery_pin_map)
# --------------------------------------------------------------------------
SESSION = "100b"                                                # (local)
GATE_ID = "S100b-CF28-SIMPLE-POLE-PREFLIGHT"                    # (local)
SCHEME = "Mellin-symbolic-Faulhaber+contour-Laurent-numeric"    # (local)
CONVENTION = "poleconv-DUAL-declared-SU3-algebra+scale-invariant-pole-order"  # (local)
L_MAX_STR = "r1-exact|HT4000|prongB-12"                         # (local)

J_MAX = 40                       # (local) route-1 j-sum truncation pin
J_MAX_DIAG = 50                  # (local) stability diagnostic extension
N0_SPLIT = 64                    # (local) Hurwitz-split point (evaluator implementation; split-independent residues)
CONTOUR_R = 0.1                  # (local) route-2 contour radius pin
N_QUAD = 64                      # (local) trapezoid nodes pin
EPS_DOUBLE = 1e-8                # (local) route-2 double-pole ratio threshold
EPS_XROUTE = 1e-6                # (local) cross-route c_-1 agreement threshold
EPS_WEYL = 1e-3                  # (local) a_0 Weyl-consistency threshold
EPS_TAIL = 1e-30                 # (local) heat-trace truncation tail (relative per grid point)
SHELL_BAND = 0.5                 # (local) prong-B shell-exponent band
L_HUGE = 4000                    # (local) heat-trace / direct-sum partial-sum pin
X_CUT = 160.0                    # (local) heat-trace mask: t*lam2 > X_CUT covered by analytic bound
T_GRID = np.logspace(-4, 0, 200) # (local) heat-trace t-grid pin
EVAL_CUTOFF = 1e-6               # (local) IR cutoff (matches s84 cache producer)
TAU = float(tau_fold)            # (local alias) 0.19, canonical

# Scanned curvature grades (pre-registered): n in {0..8, 10, 12, 14}
SCAN_GRADES = [0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 14]           # (local)
# zeta_A scan points: s_A = (8-n)/2 for the 12 grades + Conv.-A numerals {5,6,7}
SA_FROM_GRADE = {n: Fraction(8 - n, 2) for n in SCAN_GRADES}    # (local)
CONVA_POINTS = [Fraction(5), Fraction(6), Fraction(7)]          # (local)
# Verdict KEY set: Conv.-B-mapped {s_A = 2.5, 3, 3.5} + Conv.-A {5, 6, 7}
KEY_SA = [Fraction(5, 2), Fraction(3), Fraction(7, 2),
          Fraction(5), Fraction(6), Fraction(7)]                # (local)

OUT_NPZ = SCRIPT_DIR / "s100b_cf28_simple_pole_preflight.npz"
OUT_PNG = SCRIPT_DIR / "s100b_cf28_simple_pole_preflight.png"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz",
    SHARED_DIR / "dirac_spectrum.py",
    SHARED_DIR / "_analytic_zeta.py",
    SHARED_DIR / "_cm_1995_residue_formula.py",
    PROJECT_ROOT / "downloads" / "research-sweep-s99" / "spectral-geometry-math"
    / "01_Lai-Teh_Dirac-Spectrum-Spectral-Action-SU3.pdf",
]
PLAN_STATIC_SHAS = {                                            # (local) plan Input-SHA ledger
    "computations/session-84/s84_spectrum_cache_L12_tau019.npz":
        "9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9",
    "computations/_shared/dirac_spectrum.py":
        "dadba674e950fad9a300c282b3860cbf31e36589fa86a0ace975376976a602a7",
    "computations/_shared/_analytic_zeta.py":
        "6383c87717c17040f596264a2e33cdc630089fb750681ab2eb149e934d84f660",
    "computations/_shared/_cm_1995_residue_formula.py":
        "ee02f2711d061c8da1b31b2fd9071a968f1e0bc27ed0169db95676488986e224",
    "downloads/research-sweep-s99/spectral-geometry-math/01_Lai-Teh_Dirac-Spectrum-Spectral-Action-SU3.pdf":
        "b5502a2fa4e719eb706a7a9e24d98a2ae00ffc2f787973f225e61103f8277cba",
}


# --------------------------------------------------------------------------
# Section 3 — SHA-256 dual-pin block (first 20 lines of stdout)
# --------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                        # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}                                                   # (local)
    for p in inputs:
        sha = sha256_of(p)                                      # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
        if rel in PLAN_STATIC_SHAS:
            assert sha == PLAN_STATIC_SHAS[rel], f"SHA drift vs plan ledger: {rel}"
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins) -> tuple:
    script_bytes = script_path.read_bytes()                     # (local)
    canonical_bytes = canonical_path.read_bytes()               # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode()  # (local)
    h_a = hashlib.sha256(); h_a.update(script_bytes); h_a.update(canonical_bytes); h_a.update(pinmap_json)
    h_c = hashlib.sha256(); h_c.update(script_bytes)
    return h_a.hexdigest(), h_c.hexdigest()


# --------------------------------------------------------------------------
# Section 4 — exact Faulhaber/Bernoulli machinery (route 1, Fractions)
# --------------------------------------------------------------------------
def bernoulli_list(nmax):
    """Bernoulli numbers B_0..B_nmax (B_1 = -1/2 convention), exact Fractions."""
    B = [Fraction(1)]                                           # (local)
    for m in range(1, nmax + 1):
        acc = Fraction(0)                                       # (local)
        binom = 1                                               # (local) C(m+1, i)
        for i in range(m):
            acc += binom * B[i]
            binom = binom * (m + 1 - i) // (i + 1)
        B.append(-acc / Fraction(m + 1))
    return B


BERN = bernoulli_list(2 * (J_MAX_DIAG + 2) + 2)                 # (local) up to B_106

# Euler-Maclaurin Hurwitz tail evaluator.
# WHY (honest in-session numerical-soundness correction, disclosed): mpmath's
# two-argument zeta(w, a) at COMPLEX w with large Re(w) returns ABSOLUTE noise
# ~1e-57*O(1) at dps=50 (instead of the true ~a^{-Re w} ~ 1e-154 at w~85, a=64);
# multiplied by the Bernoulli-sized low-degree Faulhaber coefficients (G_o ~ 1e64)
# this injected O(1e8) garbage into the contour nodes while the real axis (where
# mpmath uses an accurate path) was perfect. The EM form below carries the
# MULTIPLICATIVE prefactor a^{-w}, so its error is relative, never absolute:
#   zeta_H(w, a) = a^{-w} [ 1/2 + a/(w-1)
#                  + sum_{r=1}^{R} B_{2r}/(2r)! * (w)_{2r-1} * a^{1-2r} ] + err
# with (w)_{2r-1} the rising factorial; for a = 64, |w| <= ~92, R = 45 the term
# ratio is <= ((|w|+2r)/(2 pi a))^2 <= 0.2, giving ~1e-40 relative accuracy.
# Validated in-run against mpmath on the real axis (where mpmath is accurate).
R_EM = 45                                                       # (local) EM truncation order
B_OVER_FACT_MPF = [mp.mpf(0)] * (2 * R_EM + 3)                  # (local) B_{2r}/(2r)! as mpf
for _r in range(1, R_EM + 1):
    _b = BERN[2 * _r] / Fraction(math.factorial(2 * _r))        # (local)
    B_OVER_FACT_MPF[2 * _r] = mp.mpf(_b.numerator) / mp.mpf(_b.denominator)


def zetaH_EM(w, a, R=R_EM):
    """Hurwitz zeta(w, a) = sum_{n>=a} n^{-w} by Euler-Maclaurin (a integer >= 2).
    Multiplicatively accurate (~1e-40 rel) for |w| <= ~2*pi*a - 2R; valid as the
    analytic continuation for Re(w) > 1 - 2R."""
    w = mp.mpmathify(w)                                         # (local)
    am = mp.mpf(a)                                              # (local)
    pref = mp.power(am, -w)                                     # (local)
    out = mp.mpf('0.5') + am / (w - 1)                          # (local)
    rising = w                                                  # (local) (w)_1
    inv_a2 = 1 / (am * am)                                      # (local)
    apow = 1 / am                                               # (local) a^{1-2r} at r=1
    for r in range(1, R + 1):
        out += B_OVER_FACT_MPF[2 * r] * rising * apow
        rising = rising * (w + 2 * r - 1) * (w + 2 * r)
        apow = apow * inv_a2
    return pref * out


def faulhaber_coeffs(p):
    """Coefficients of P_p(N) = sum_{u=1}^{N-1} u^p (p >= 1): {degree: Fraction}."""
    out = {}                                                    # (local)
    binom = 1                                                   # (local) C(p+1, i)
    for i in range(p + 1):
        c = Fraction(binom) * BERN[i] / (p + 1)                 # (local)
        if c != 0:
            out[p + 1 - i] = out.get(p + 1 - i, Fraction(0)) + c
        binom = binom * (p + 1 - i) // (i + 1)
    return out


def S_coeffs(j):
    """Exact monomial coefficients of S_j(N) = sum_{u=1}^{N-1} u^{j+2} (N-u)^{j+2}."""
    k = j + 2                                                   # (local)
    out = {}                                                    # (local)
    binom = 1                                                   # (local) C(k, m)
    for m in range(k + 1):
        P = faulhaber_coeffs(k + m)                             # (local)
        sgn = -1 if (m % 2) else 1                              # (local)
        for d, c in P.items():
            dd = d + k - m                                      # (local)
            out[dd] = out.get(dd, Fraction(0)) + sgn * binom * c
        binom = binom * (k - m) // (m + 1)
    return {d: c for d, c in out.items() if c != 0}


def S_direct_int(j, N):
    """Exact integer S_j(N) by direct summation (no cancellation)."""
    k = j + 2                                                   # (local)
    return sum(u**k * (N - u)**k for u in range(1, N))


def poch_frac(s_frac, j):
    """(s)_j / j! exact (s rational)."""
    out = Fraction(1)                                           # (local)
    for i in range(j):
        out *= (s_frac + i) / Fraction(i + 1)
    return out


# --------------------------------------------------------------------------
# Section 5 — route-1 pole enumeration + exact residues
# --------------------------------------------------------------------------
def build_route1(jmax_diag):
    SC = [S_coeffs(j) for j in range(jmax_diag + 1)]            # (local)
    # exact polynomial-vs-direct verification + even-degree audit
    even_violations = 0                                         # (local)
    for j in range(jmax_diag + 1):
        for N in (2, 3, 5, 9, 17):
            poly = sum(c * Fraction(N) ** d for d, c in SC[j].items())  # (local)
            assert poly == S_direct_int(j, N), f"S_{j}({N}) Faulhaber mismatch"
        even_violations += sum(1 for d in SC[j] if d % 2 == 0)
    return SC, even_violations


def route1_point_data(SC, sa, jmax):
    """At zeta_A point sa (Fraction): enumerate ALL candidate pole terms (j,d) with
    pole location (3+d-2j)/2 == sa; classify genuine vs Pochhammer-killed; exact residue.
    Returns dict."""
    cand = []                                                   # (local)
    genuine = []                                                # (local)
    res = Fraction(0)                                           # (local)
    for j in range(jmax + 1):
        d_num = 2 * sa + 2 * j - 3                              # (local) required degree
        if d_num.denominator != 1:
            continue
        d = int(d_num)                                          # (local)
        c = SC[j].get(d)                                        # (local)
        if c is None:
            continue
        cand.append((j, d))
        pj = poch_frac(sa, j)                                   # (local)
        if pj != 0:
            genuine.append((j, d))
            res += pj * c / 2
    res *= 4
    return {"sa": sa, "candidates": cand, "genuine": genuine,
            "m_p_candidate": len(cand), "m_p_genuine": len(genuine),
            "c_m1_exact": res, "c_m2_structural": Fraction(0)}


# --------------------------------------------------------------------------
# Section 6 — route-1 continuation evaluator (Hurwitz split at N0_SPLIT)
# --------------------------------------------------------------------------
class ZetaAEvaluator:
    def __init__(self, SC, jmax, n0):
        self.jmax = jmax
        self.n0 = n0
        # exact integer S_j(N) for N < n0 -> mpf
        self.S_int = [[mp.mpf(S_direct_int(j, N)) for N in range(2, n0)]
                      for j in range(jmax + 1)]
        self.Ns = list(range(2, n0))
        # group (j,d) coefficient lists by integer offset o = 2j-2-d
        self.by_offset = {}                                     # o -> list of (j, mpf(c))
        for j in range(jmax + 1):
            for d, c in SC[j].items():
                o = 2 * j - 2 - d                               # (local)
                cf = mp.mpf(c.numerator) / mp.mpf(c.denominator)  # (local)
                self.by_offset.setdefault(o, []).append((j, cf))

    def __call__(self, s):
        s = mp.mpmathify(s)                                     # (local)
        # Pochhammer/j! prefactors P_j(s)
        P = [mp.mpf(1)] * (self.jmax + 1)                       # (local)
        acc = mp.mpf(1) if mp.im(s) == 0 else mp.mpc(1)         # (local)
        for j in range(1, self.jmax + 1):
            acc = acc * (s + (j - 1)) / j
            P[j] = acc
        # finite part: per-N geometric ladder W_N(j) = N^(2-2s-2j)
        W = [mp.power(mp.mpf(N), 2 - 2 * s) for N in self.Ns]   # (local)
        inv2 = [mp.mpf(N) ** -2 for N in self.Ns]               # (local)
        tot = mp.mpf(0)                                         # (local)
        for j in range(self.jmax + 1):
            if j > 0:
                W = [w * iv for w, iv in zip(W, inv2)]
            fin_j = mp.fsum(w * sint for w, sint in zip(W, self.S_int[j]))  # (local)
            tot += P[j] * fin_j
        # Hurwitz tails grouped by offset (EM evaluator — see zetaH_EM note)
        for o, lst in self.by_offset.items():
            zh = zetaH_EM(2 * s + o, self.n0)                   # (local)
            G = mp.fsum(P[j] * cf for j, cf in lst)             # (local)
            tot += G * zh
        return 4 * tot

    def j_term_magnitudes(self, s):
        """|4 P_j(s) (Fin_j + Hur_j)| per j, for the interchange-justification check."""
        s = mp.mpmathify(s)
        P = [mp.mpf(1)] * (self.jmax + 1)                       # (local)
        acc = mp.mpf(1) if mp.im(s) == 0 else mp.mpc(1)         # (local)
        for j in range(1, self.jmax + 1):
            acc = acc * (s + (j - 1)) / j
            P[j] = acc
        W = [mp.power(mp.mpf(N), 2 - 2 * s) for N in self.Ns]   # (local)
        inv2 = [mp.mpf(N) ** -2 for N in self.Ns]               # (local)
        # per-j Hurwitz parts (EM evaluator — see zetaH_EM note)
        hur = [mp.mpf(0)] * (self.jmax + 1)                     # (local)
        for o, lst in self.by_offset.items():
            zh = zetaH_EM(2 * s + o, self.n0)                   # (local)
            for j, cf in lst:
                hur[j] += cf * zh
        mags = []                                               # (local)
        for j in range(self.jmax + 1):
            if j > 0:
                W = [w * iv for w, iv in zip(W, inv2)]
            fin_j = mp.fsum(w * sint for w, sint in zip(W, self.S_int[j]))  # (local)
            mags.append(float(abs(4 * P[j] * (fin_j + hur[j]))))
        return mags


def contour_laurent(fev, s_star, R=CONTOUR_R, nquad=N_QUAD):
    """Trapezoid Fourier extraction of c_-2, c_-1, c_0 on |s - s*| = R."""
    cm2 = mp.mpc(0); cm1 = mp.mpc(0); c0 = mp.mpc(0)            # (local)
    for kk in range(nquad):
        th = 2 * mp.pi * kk / nquad                             # (local)
        z = mp.mpc(mp.cos(th), mp.sin(th))                      # (local)
        fz = fev(mp.mpf(s_star) + R * z)                        # (local)
        cm2 += fz * z ** 2
        cm1 += fz * z
        c0 += fz
    cm2 = cm2 * (R ** 2) / nquad
    cm1 = cm1 * R / nquad
    c0 = c0 / nquad
    return cm2, cm1, c0


# --------------------------------------------------------------------------
# Section 7 — prong-A direct convergent sums (Conv.-A s in {5,6,7}) — float64
# --------------------------------------------------------------------------
def zeta_A_direct_f64(s, Nmax=L_HUGE):
    tot = 0.0                                                   # (local)
    for N in range(2, Nmax + 1):
        u = np.arange(1, N, dtype=np.float64)                   # (local)
        v = N - u                                               # (local)
        lam2 = u * u + u * v + v * v                            # (local)
        tot += float(np.sum(4.0 * (u * v) ** 2 * N ** 2 * lam2 ** (-s)))
    # rigorous tail bound: per-shell <= (N^7/4)*((3/4)N^2)^(-s); sum_{N>Nmax} <= integral
    tail = (4.0 / 3.0) ** s / 4.0 * Nmax ** (8 - 2 * s) / (2 * s - 8)  # (local)
    return tot, tail


# --------------------------------------------------------------------------
# Section 8 — heat-trace artifact K(t) + rigorous truncation bound
# --------------------------------------------------------------------------
def heat_trace(t_grid):
    n_grid = int(np.ceil(np.sqrt(X_CUT / t_grid.min()))) + 2    # (local) effective grid
    n_grid = min(n_grid, L_HUGE)
    u = np.arange(1, n_grid + 1, dtype=np.float64)              # (local)
    U, V = np.meshgrid(u, u, indexing='ij')                     # (local)
    LAM2 = (U * U + U * V + V * V).ravel()                      # (local)
    W = (4.0 * (U * V) ** 2 * (U + V) ** 2).ravel()             # (local)
    K = np.empty_like(t_grid)                                   # (local)
    tail_rel = np.empty_like(t_grid)                            # (local)
    for i, t in enumerate(t_grid):
        msk = LAM2 * t <= X_CUT                                 # (local)
        K[i] = float(np.sum(W[msk] * np.exp(-t * LAM2[msk])))
        # rigorous bound on everything with t*lam2 > X_CUT (covers grid->L_huge->inf):
        # weight w = 4(uv)^2(u+v)^2 <= 2 m^3 (m = lam2: uv <= m/2, (u+v)^2 <= 3m/2);
        # cumulative count N(m) <= pi m/4 < m; Abel summation with decreasing
        # g(m) = 2 m^3 e^{-tm} is dominated by 2 int_{Lc}^inf m^4 e^{-tm} dm
        # = 2 e^{-t Lc} sum_{i=0}^4 (4!/i!) Lc^i / t^(5-i)  [exact incomplete-Gamma]
        Lc = X_CUT / t                                          # (local)
        s5 = np.exp(-X_CUT) * sum((24.0 / math.factorial(ii)) * Lc ** ii / t ** (5 - ii)
                                  for ii in range(5))           # (local)
        tail_rel[i] = 2.0 * s5 / K[i]
    return K, tail_rel, n_grid


# --------------------------------------------------------------------------
# Section 9 — prong B: s84 cache + (4,4) reconstruction + shell analytics
# --------------------------------------------------------------------------
def reconstruct_sector(p, q, tds, torch, gens, f_abc, E_frame, gammas, Omega):
    rho, dim_check = tds.get_irrep(p, q, gens, f_abc)           # (local)
    hom_err, ah_err = tds.validate_irrep(rho, f_abc)            # (local)
    assert hom_err < 1e-10 and ah_err < 1e-10, f"({p},{q}) irrep validation failed"
    dim_rho = rho[0].shape[0]                                   # (local)
    D = np.zeros((dim_rho * 16, dim_rho * 16), dtype=np.complex128)  # (local)
    for a in range(8):
        for b in range(8):
            if abs(E_frame[a, b]) > 1e-15:
                D += E_frame[a, b] * np.kron(rho[b], gammas[a])
    D += np.kron(np.eye(dim_rho), Omega)
    H = 1j * D                                                  # (local)
    H = 0.5 * (H + H.conj().T)
    if torch.cuda.is_available() and H.shape[0] >= 100:
        Ht = torch.tensor(H, dtype=torch.complex128, device='cuda')  # (local)
        evals = torch.linalg.eigvalsh(Ht).cpu().numpy()         # (local)
        del Ht
        torch.cuda.empty_cache()
    else:
        evals = np.linalg.eigvalsh(H)                           # (local)
    abs_evals = np.abs(evals)                                   # (local)
    return np.sort(abs_evals[abs_evals > EVAL_CUTOFF]), dim_rho, hom_err


def prong_b():
    import torch
    import dirac_spectrum as tds
    cache = np.load(COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz",
                    allow_pickle=True)
    sector_evals = {k: {'dim': int(d['dim']), 'level': int(d['level']),
                        'abs_evals': np.asarray(d['abs_evals'], dtype=np.float64)}
                    for k, d in cache['sector_evals'].item().items()}
    assert (4, 4) not in sector_evals and len(sector_evals) == 90

    gens = tds.su3_generators()                                 # (local)
    f_abc = tds.compute_structure_constants(gens)               # (local)
    B_ab = tds.compute_killing_form(f_abc)                      # (local)
    g_s = tds.jensen_metric(B_ab, TAU)                          # (local)
    E_frame = tds.orthonormal_frame(g_s)                        # (local)
    ft = tds.frame_structure_constants(f_abc, E_frame)          # (local)
    Gamma_conn = tds.connection_coefficients(ft)                # (local)
    gammas = tds.build_cliff8()                                 # (local)
    Omega = tds.spinor_connection_offset(Gamma_conn, gammas)    # (local)

    # lineage cross-checks: rebuild cached sectors (2,2) and (4,3), compare
    lineage = {}                                                # (local)
    for (p, q) in [(2, 2), (4, 3)]:
        ev, dim_rho, hom = reconstruct_sector(p, q, tds, torch, gens, f_abc,
                                              E_frame, gammas, Omega)
        cached = np.sort(sector_evals[(p, q)]['abs_evals'])     # (local)
        n_cmp = min(len(ev), len(cached))                       # (local)
        lineage[(p, q)] = {
            'max_abs_diff': float(np.max(np.abs(ev[:n_cmp] - cached[:n_cmp]))),
            'count_rebuilt': int(len(ev)), 'count_cached': int(len(cached)),
            'hom_err': float(hom)}

    # (4,4) reconstruction (dim 125, block 2000x2000)
    ev44, dim44, hom44 = reconstruct_sector(4, 4, tds, torch, gens, f_abc,
                                            E_frame, gammas, Omega)
    assert dim44 == 125
    sector_evals[(4, 4)] = {'dim': 125, 'level': 8, 'abs_evals': ev44}

    # per-sector state-count integrity (no IR-cutoff drops expected)
    deficits = {k: 16 * d['dim'] - len(d['abs_evals'])
                for k, d in sector_evals.items()
                if 16 * d['dim'] != len(d['abs_evals'])}        # (local)

    # Conv.-A direct sums + shell sums (both families)
    sA_list = [5.0, 6.0, 7.0]                                   # (local)
    shell_A = {s: {} for s in sA_list}                          # (local) per-shell double-power
    shell_B = {s: {} for s in sA_list}                          # (local) per-shell single-power
    for (p, q), d in sector_evals.items():
        L = p + q                                               # (local)
        lam = d['abs_evals']                                    # (local)
        w = float(d['dim'])                                     # (local) PW multiplicity factor
        for s in sA_list:
            shell_A[s][L] = shell_A[s].get(L, 0.0) + w * float(np.sum(lam ** (-2 * s)))
            shell_B[s][L] = shell_B[s].get(L, 0.0) + w * float(np.sum(lam ** (-s)))

    zA_L12 = {s: sum(v for L, v in shell_A[s].items() if L <= 12) for s in sA_list}  # (local)
    zA_L10 = {s: sum(v for L, v in shell_A[s].items() if L <= 10) for s in sA_list}  # (local)

    fits = {}                                                   # (local)
    Lfit = np.arange(6, 13)                                     # (local)
    for s in sA_list:
        yA = np.array([shell_A[s][L] for L in Lfit])            # (local)
        yB = np.array([shell_B[s][L] for L in Lfit])            # (local)
        slA = np.polyfit(np.log(Lfit), np.log(yA), 1)[0]        # (local)
        slB = np.polyfit(np.log(Lfit), np.log(yB), 1)[0]        # (local)
        fits[s] = {'exp_A_meas': float(slA), 'exp_A_pred': 7.0 - 2 * s,
                   'exp_B_meas': float(slB), 'exp_B_pred': 7.0 - s}

    # L=12-vs-L=10 stability vs 2x analytic tail (s_A in {5, 6})
    stab = {}                                                   # (local)
    for s in [5.0, 6.0]:
        meas = zA_L12[s] - zA_L10[s]                            # (local) shells 11+12
        amp = np.mean([shell_A[s][L] / L ** (7 - 2 * s) for L in range(6, 11)])  # (local)
        tail_est = amp * (11.0 ** (7 - 2 * s) + 12.0 ** (7 - 2 * s))  # (local)
        stab[s] = {'measured_delta': float(meas), 'tail_est': float(tail_est),
                   'ratio': float(meas / tail_est), 'ok': bool(meas <= 2.0 * tail_est)}

    return (sector_evals, lineage, ev44, hom44, deficits,
            shell_A, shell_B, zA_L12, zA_L10, fits, stab)


def tau0_window_diag():
    """Regime discriminator for the prong-B shell-exponent clause (decision
    procedure PRE-STATED before computing): fit the EXACT tau=0 closed-form
    (cubic-point) shell sums on the SAME window L in [6,12] (sectors u+v = L+2)
    with the SAME log-log procedure. If the IDEAL spectrum's window slope also
    misses the +/-0.5 band around the asymptotic exponent 7-2s IN THE SAME
    DIRECTION, the analytic-exponent comparison is out-of-regime on the pinned
    window (pre-asymptotic) -> regime MARGINAL per gate-verdicts.md schema-v2;
    otherwise the tau_fold miss is a genuine anomaly -> regime VALID and the
    magnitude FAIL stands at composite level."""
    out = {}                                                    # (local)
    Lw = np.arange(6, 13)                                       # (local)
    for s in (5.0, 6.0, 7.0):
        sh = []                                                 # (local)
        for L in Lw:
            N = L + 2                                           # (local) u+v = p+q+2
            u = np.arange(1, N, dtype=np.float64)               # (local)
            v = N - u                                           # (local)
            lam2 = u * u + u * v + v * v                        # (local)
            sh.append(float(np.sum(4.0 * (u * v) ** 2 * N ** 2 * lam2 ** (-s))))
        sl = float(np.polyfit(np.log(Lw), np.log(sh), 1)[0])    # (local)
        out[s] = {'exp_tau0_window': sl, 'exp_analytic': 7.0 - 2 * s,
                  'dev': sl - (7.0 - 2 * s)}
    return out


# --------------------------------------------------------------------------
# Section 10 — verdict payload printer (template-conform; emit via MCP tool)
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
# Section 11 — main
# --------------------------------------------------------------------------
def main():
    t0 = time.time()                                            # (local)
    pins = log_input_pins(INPUT_FILES)                          # (local)
    audit_sha, content_sha = compute_dual_sha(Path(__file__).resolve(),
                                              SHARED_DIR / "canonical_constants.py", pins)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print(f"  canonical echoes: tau_fold={TAU}, Vol_SU3_Haar={float(Vol_SU3_Haar):.2f}, "
          f"M_KK={float(M_KK):.4g}")
    print(f"  cross-algebra caveat: residue_s6_PS_Linf={residue_s6_PS_Linf:.6e} is the "
          f"SU(4)_PS rank-4 algebra pole — NOT comparable to SU(3) values here (declared, not compared)")
    print()

    # ---------------- route 1: exact machinery ----------------
    print("[route 1] building exact Faulhaber/Bernoulli reduction "
          f"(J_max={J_MAX}, diag to {J_MAX_DIAG}) ...")
    SC, even_nonzero = build_route1(J_MAX_DIAG)
    print(f"  S_j(N) exact-poly-vs-direct verification PASS for j<=50; "
          f"even-degree nonzero coefficients: {even_nonzero} (odd-degree theorem "
          f"{'HOLDS' if even_nonzero == 0 else 'VIOLATED'})")

    # global pole-location census (exhaustive collision enumeration)
    pole_locs = {}                                              # (local) sa -> count of candidate (j,d)
    for j in range(J_MAX + 1):
        for d in SC[j]:
            sa = Fraction(3 + d - 2 * j, 2)                     # (local)
            pole_locs[sa] = pole_locs.get(sa, 0) + 1
    max_pole = max(pole_locs)                                   # (local)
    half_int_locs = [sa for sa in pole_locs if sa.denominator != 1]  # (local)
    print(f"  candidate pole locations: {len(pole_locs)} distinct; max = {max_pole} "
          f"(no candidate poles at s_A > 4: {'OK' if max_pole <= 4 else 'VIOLATION'})")
    print(f"  half-integer candidate locations: {len(half_int_locs)} "
          f"(odd-grade regularity structural iff 0)")

    # per scanned order: route-1 data (J_MAX) + J-stability diagnostic (J_MAX_DIAG)
    scan_points = [(n, SA_FROM_GRADE[n]) for n in SCAN_GRADES]  # (local)
    conva_rows = [(None, sa) for sa in CONVA_POINTS]            # (local)
    r1 = {}                                                     # (local) sa -> data
    for n, sa in scan_points + conva_rows:
        dat = route1_point_data(SC, sa, J_MAX)                  # (local)
        dat_diag = route1_point_data(SC, sa, J_MAX_DIAG)        # (local)
        dat['c_m1_exact_J50'] = dat_diag['c_m1_exact']
        dat['J_stability'] = float(abs(dat_diag['c_m1_exact'] - dat['c_m1_exact']))
        r1[sa] = dat

    genuine_poles = sorted([sa for sa, d in r1.items() if d['m_p_genuine'] > 0],
                           reverse=True)                        # (local)
    print(f"  genuine poles among scanned points: {[str(s) for s in genuine_poles]} "
          f"(canonical S_d={{0,2,4,6,8}} predicts s_A in {{4,3,2,1}} + Gamma-poles)")
    for sa in genuine_poles:
        d = r1[sa]
        print(f"    s_A={sa}: m_p_cand={d['m_p_candidate']} m_p_genuine={d['m_p_genuine']} "
              f"Res={float(d['c_m1_exact']):.12e} |J50-J40|={d['J_stability']:.3e}")

    # ---------------- evaluator + internal validation ----------------
    print("\n[evaluator] Hurwitz-split continuation (N0=64) ...")
    # EM-tail validation against mpmath's REAL-axis path. Certification target
    # 1e-12 (4 OOM margin over the 1e-8 gate threshold): the cross-check is
    # bounded by mpmath's own real-path accuracy at large w (~5e-15 observed),
    # NOT by the EM error (~1e-40 by the term-ratio bound); EM correctness is
    # independently certified by the bit-exact contour-vs-exact-residue
    # agreement at s_A=4 and the direct-sum agreements at s_A in {6,7}.
    em_dev = 0.0                                                # (local)
    for w_t in (85.0, 33.0, 12.4, 3.0, 1.5, -5.0, -13.0):
        ref = mp.zeta(mp.mpf(w_t), N0_SPLIT)                    # (local)
        em = zetaH_EM(mp.mpf(w_t), N0_SPLIT)                    # (local)
        if abs(ref) > 0:
            em_dev = max(em_dev, float(abs(em - ref) / abs(ref)))
    em_ok = em_dev < 1e-12                                      # (local)
    print(f"  EM-Hurwitz vs mpmath (real axis, w in [-13, 85]): max rel dev = "
          f"{em_dev:.3e} ({'OK' if em_ok else 'FAIL'}; target 1e-12, bounded by "
          f"mpmath real-path accuracy at large w)")
    fev = ZetaAEvaluator(SC, J_MAX, N0_SPLIT)
    fev96 = ZetaAEvaluator(SC, J_MAX, 96)                       # (local) split-independence probe
    n0_check = max(float(abs(fev(mp.mpf('3.7')) - fev96(mp.mpf('3.7')))),
                   float(abs(fev(mp.mpf('-2.6')) - fev96(mp.mpf('-2.6')))))  # (local)
    print(f"  N0-split independence (s=3.7, -2.6): max |delta| = {n0_check:.3e}")

    # direct-sum cross-check at Conv.-A points (validates interchange + continuation)
    direct_checks = {}                                          # (local)
    for sa in (5.0, 6.0, 7.0):
        dsum, dtail = zeta_A_direct_f64(sa)                     # (local)
        ev = float(fev(mp.mpf(sa)))                             # (local)
        direct_checks[sa] = {'direct': dsum, 'tail_bound': dtail, 'evaluator': ev,
                             'abs_diff': abs(ev - dsum),
                             'ok': bool(abs(ev - dsum) <= 2.0 * dtail + 1e-12 * abs(ev))}
        print(f"  s_A={sa}: direct(N<={L_HUGE})={dsum:.15e} evaluator={ev:.15e} "
              f"|diff|={abs(ev - dsum):.2e} tail_bound={dtail:.2e} "
              f"{'OK' if direct_checks[sa]['ok'] else 'MISMATCH'}")

    # j-sum interchange justification: geometric decay of j-term magnitudes at key points
    jdecay = {}                                                 # (local)
    for sa in KEY_SA:
        s_probe = float(sa) + 0.1                               # (local) off-pole probe
        mags = fev.j_term_magnitudes(mp.mpf(s_probe))           # (local)
        m = np.array(mags[20:J_MAX + 1])                        # (local)
        m = np.where(m > 0, m, 1e-300)                          # (local)
        ratio = float(np.exp(np.polyfit(np.arange(20, J_MAX + 1), np.log(m), 1)[0]))  # (local)
        jdecay[float(sa)] = ratio
    jdecay_ok = all(rr < 1.0 for rr in jdecay.values())         # (local)
    print(f"  j-term decay ratios at key points (expect ~0.25, must be <1): "
          f"{ {k: round(v, 4) for k, v in jdecay.items()} } -> "
          f"{'OK' if jdecay_ok else 'INTERCHANGE-FAIL -> INFO'}")

    # ---------------- route 2: contour Laurent extraction ----------------
    print("\n[route 2] contour Laurent extraction "
          f"(R={CONTOUR_R}, N_quad={N_QUAD}, dps={mp.mp.dps}) ...")
    table = []                                                  # (local) per-order rows
    for n, sa in scan_points + conva_rows:
        t_c = time.time()                                       # (local)
        cm2, cm1, c0 = contour_laurent(fev, float(sa))          # (local)
        im_floor = max(abs(float(mp.im(cm2))), abs(float(mp.im(cm1))),
                       abs(float(mp.im(c0))))                   # (local)
        cm2r, cm1r, c0r = (float(mp.re(cm2)), float(mp.re(cm1)), float(mp.re(c0)))  # (local)
        ratio_double = abs(cm2r) / max(abs(cm1r), abs(c0r), 1e-30)  # (local)
        c1_exact = float(r1[sa]['c_m1_exact'])                  # (local)
        xroute = (abs(c1_exact - cm1r) / abs(c1_exact)) if c1_exact != 0 else float('nan')  # (local)
        row = {
            'n': (n if n is not None else -99),
            's_A': float(sa),
            's_B': float(2 * sa),
            'm_p_candidate': r1[sa]['m_p_candidate'],
            'm_p_genuine': r1[sa]['m_p_genuine'],
            'c_m2_r1': 0.0,
            'c_m1_r1': c1_exact,
            'c_m2_r2': cm2r, 'c_m1_r2': cm1r, 'c_0_r2': c0r,
            'ratio_double': ratio_double,
            'xroute_rel': xroute,
            'im_floor': im_floor,
            'gamma_collision': bool(n in (8, 10, 12, 14)) if n is not None else False,
            'key_set': bool(sa in KEY_SA),
        }
        table.append(row)
        tagk = "KEY" if row['key_set'] else ("exotic" if row['gamma_collision'] else "anchor")  # (local)
        print(f"  n={str(row['n']):>3s} s_A={row['s_A']:5.1f} s_B={row['s_B']:5.1f} [{tagk:6s}] "
              f"m_p={row['m_p_genuine']:2d} c_-2={cm2r:+.2e} c_-1={cm1r:+.14e} "
              f"c_0={c0r:+.6e} dbl_ratio={ratio_double:.2e} "
              f"xroute={xroute if xroute == xroute else float('nan'):.2e} ({time.time()-t_c:.1f}s)"
              .replace("n=-99", "n=  -"))

    # ---------------- Weyl anchor (a_0 internal consistency) ----------------
    f_ang = lambda phi: (mp.cos(phi) ** 2 * mp.sin(phi) ** 2
                         * (mp.cos(phi) + mp.sin(phi)) ** 2
                         / (1 + mp.cos(phi) * mp.sin(phi)) ** 4)  # (local)
    a0_weyl = float(12 * mp.quad(f_ang, [0, mp.pi / 2]))        # (local)
    res4 = float(r1[Fraction(4)]['c_m1_exact'])                 # (local)
    a0_res = 6.0 * res4                                         # (local) Gamma(4) * Res
    weyl_resid = abs(a0_res - a0_weyl) / a0_weyl                # (local)
    vol_implied = a0_res * (4 * np.pi) ** 4 / 16.0              # (local) diagnostic, kappa-convention
    print(f"\n[Weyl anchor] Gamma(4)*Res_(s_A=4) = {a0_res:.15e} vs Weyl integral "
          f"{a0_weyl:.15e}: resid = {weyl_resid:.3e} (< {EPS_WEYL}: "
          f"{'OK' if weyl_resid < EPS_WEYL else 'FAIL'})")
    print(f"  diagnostic: implied Vol (lambda_hat units) = {vol_implied:.2f} vs "
          f"Vol_SU3_Haar = {float(Vol_SU3_Haar):.2f} (kappa-convention dependent, "
          f"Chain-3 scale freedom — NOT gating)")

    # ---------------- heat-trace artifact ----------------
    print("\n[heat trace] K(t) partial sums + no-log series overlay ...")
    K, tail_rel, n_grid_eff = heat_trace(T_GRID)
    ht_tail_max = float(np.max(tail_rel))                       # (local)
    # no-log asymptotic series from route-1 residues + route-2 finite parts
    by_sa = {row['s_A']: row for row in table}                  # (local)
    a_heat = {                                                  # (local) heat coefficients (lambda_hat units)
        0: 6.0 * float(r1[Fraction(4)]['c_m1_exact']),
        2: 2.0 * float(r1[Fraction(3)]['c_m1_exact']),
        4: 1.0 * float(r1[Fraction(2)]['c_m1_exact']),
        6: 1.0 * float(r1[Fraction(1)]['c_m1_exact']),
        8: by_sa[0.0]['c_0_r2'],
    }
    c_t = {1: -by_sa[-1.0]['c_0_r2'],
           2: by_sa[-2.0]['c_0_r2'] / 2.0,
           3: -by_sa[-3.0]['c_0_r2'] / 6.0}                     # (local) (-1)^k zeta_A(-k)/k!
    series = (a_heat[0] / T_GRID ** 4 + a_heat[2] / T_GRID ** 3
              + a_heat[4] / T_GRID ** 2 + a_heat[6] / T_GRID
              + a_heat[8] + c_t[1] * T_GRID + c_t[2] * T_GRID ** 2
              + c_t[3] * T_GRID ** 3)                           # (local)
    resid_rel = np.abs(K - series) / K                          # (local)
    small_t_resid = float(np.max(resid_rel[T_GRID <= 1e-2]))    # (local)
    print(f"  effective grid {n_grid_eff} (terms beyond mask < 1e-40 of K; pin L_huge={L_HUGE}); "
          f"max truncation tail (rel) = {ht_tail_max:.2e} (< {EPS_TAIL}: "
          f"{'OK' if ht_tail_max < EPS_TAIL else 'FAIL'})")
    print(f"  no-log series residual: max over t<=1e-2 = {small_t_resid:.2e} "
          f"(O(t^4) expected; visual artifact in PNG)")

    # ---------------- prong B ----------------
    print("\n[prong B] s84 L12 cache + (4,4) reconstruction at tau_fold ...")
    (sector_evals, lineage, ev44, hom44, deficits,
     shell_A, shell_B, zA_L12, zA_L10, fits, stab) = prong_b()
    print(f"  lineage cross-checks: (2,2) max|dlam| = {lineage[(2,2)]['max_abs_diff']:.2e}, "
          f"(4,3) max|dlam| = {lineage[(4,3)]['max_abs_diff']:.2e}")
    print(f"  (4,4) reconstructed: dim 125, block 2000x2000, {len(ev44)} states, "
          f"hom_err={hom44:.2e}, |lam| in [{ev44.min():.4f}, {ev44.max():.4f}]")
    print(f"  per-sector state-count deficits: {len(deficits)} "
          f"({deficits if deficits else 'none — all 16*dim states present'})")
    shells_ok = True                                            # (local)
    for s, f in fits.items():
        okA = abs(f['exp_A_meas'] - f['exp_A_pred']) <= SHELL_BAND  # (local)
        okB = abs(f['exp_B_meas'] - f['exp_B_pred']) <= SHELL_BAND  # (local)
        shells_ok = shells_ok and okA and okB
        print(f"  s_A={s}: shell exp (double-power) {f['exp_A_meas']:+.3f} vs {f['exp_A_pred']:+.1f} "
              f"[{'OK' if okA else 'OUT'}]; (single-power s_B={int(2*s)} family at exponent s) "
              f"{f['exp_B_meas']:+.3f} vs {f['exp_B_pred']:+.1f} [{'OK' if okB else 'OUT'}]")
    lstab_ok = all(v['ok'] for v in stab.values())              # (local)
    for s, v in stab.items():
        print(f"  L-stability s_A={s}: shells-11+12 measured {v['measured_delta']:.3e} vs "
              f"tail_est {v['tail_est']:.3e} (ratio {v['ratio']:.2f} <= 2: "
              f"{'OK' if v['ok'] else 'FAIL'})")
    print(f"  Conv.-A tau_fold sums: " +
          ", ".join(f"zeta_A({s})={zA_L12[s]:.6e}" for s in (5.0, 6.0, 7.0)))

    # regime discriminator: EXACT tau=0 closed form on the SAME window/procedure
    t0d = tau0_window_diag()
    window_artifact = True                                      # (local)
    for s, f in fits.items():
        devA = f['exp_A_meas'] - f['exp_A_pred']                # (local)
        in_band = abs(devA) <= SHELL_BAND                       # (local)
        t0_dev = t0d[s]['dev']                                  # (local)
        t0_out_same_dir = (abs(t0_dev) > SHELL_BAND
                           and np.sign(t0_dev) == np.sign(devA))  # (local)
        if not (in_band or t0_out_same_dir):
            window_artifact = False
        print(f"  [regime diag] s_A={s}: tau0-EXACT window slope "
              f"{t0d[s]['exp_tau0_window']:+.3f} vs analytic {t0d[s]['exp_analytic']:+.1f} "
              f"(dev {t0_dev:+.3f}); tau_fold dev {devA:+.3f} -> "
              f"{'window-artifact (ideal spectrum misses band too)' if t0_out_same_dir else 'tau_fold-specific'}")
    # top-end local slope (approach-to-asymptotic indicator)
    local_top = {s: float(np.log(shell_A[s][12] / shell_A[s][11]) / np.log(12.0 / 11.0))
                 for s in (5.0, 6.0, 7.0)}                      # (local)
    print(f"  [regime diag] top-end local slopes (L=11->12): "
          + ", ".join(f"s_A={s}: {local_top[s]:+.3f}" for s in (5.0, 6.0, 7.0)))

    # ---------------- Class-8.7 witness ----------------
    witness = {
        "coincident_root_declaration": {
            "gamma_collision_loci_sA": [0, -1, -2, -3],
            "gamma_collision_grades_n": [8, 10, 12, 14],
            "finding": "zeta_A REGULAR at all four loci (every candidate (j,d) term "
                       "Pochhammer-annihilated: (s*)_j = 0 for the j range carrying the "
                       "degree match) => Gamma*zeta_A poles there are SIMPLE (clean "
                       "a_8/a_10/a_12/a_14^{Mellin}); no Fucci-Stanfill log branch on the "
                       "closed substrate",
            "faulhaber_same_location_collisions": {
                str(sa): r1[sa]['m_p_candidate'] for sa in r1
                if r1[sa]['m_p_candidate'] > 1},
        },
        "per_pole_multiplicity_m_p": {
            str(sa): {"candidate": r1[sa]['m_p_candidate'],
                      "genuine": r1[sa]['m_p_genuine']} for sa in r1},
        "compositional_corridor_pin": {
            "primary": "Faulhaber->zeta_R/zeta_Hurwitz reduction corridor (route 1, exact)",
            "canonical_evaluator_template": "computations/_shared/_cm_1995_residue_formula.py (FULL physical)",
            "info_route_corridor": "computations/_shared/_analytic_zeta.py (S86 off-pole-Hankel, convention=off-pole-Hankel)",
        },
        "finite_triple_note": "the L12-truncated tau_fold spectrum is a FINITE sum -> its "
                              "zeta is ENTIRE (finite-cardinality tautology under canonical "
                              "Gamma(s) on a finite spectral triple, Class-8.7 canonical "
                              "framing); prong B therefore certifies CONVERGENCE/decay data "
                              "only, the continuum pole-order classification is prong A's",
    }

    # ---------------- verdict composition (pre-registered operator form) ----------------
    key_rows = [row for row in table if row['key_set']]         # (local)
    r1_structural_ok = (even_nonzero == 0 and max_pole <= 4 and
                        all(r1[sa]['c_m2_structural'] == 0 for sa in KEY_SA))  # (local)
    r2_ratio_ok = all(row['ratio_double'] < EPS_DOUBLE for row in key_rows)  # (local)
    max_ratio_double = max(row['ratio_double'] for row in key_rows)  # (local)
    xroute_vals = [row['xroute_rel'] for row in table
                   if row['c_m1_r1'] != 0]                      # (local) wherever c_-1 != 0
    xroute_ok = all(x < EPS_XROUTE for x in xroute_vals)        # (local)
    max_xroute = max(xroute_vals) if xroute_vals else 0.0       # (local)
    weyl_ok = weyl_resid < EPS_WEYL                             # (local)
    conv_certs_ok = all(direct_checks[s]['ok'] for s in (5.0, 6.0, 7.0))  # (local)
    prongb_ok = shells_ok and lstab_ok                          # (local)

    info_trigger = not jdecay_ok                                # (local) interchange failure (plan INFO clause)
    log_evidence = any(row['ratio_double'] >= EPS_DOUBLE and row['m_p_genuine'] > 0
                       for row in key_rows)                     # (local) FAIL_meaning discriminator

    # schema-v2 3-tuple (Chain-2 directional predictions pre-registered: Conv.-A
    # CONVERGES at s_A in {5,6,7} (shell exp < -1); Conv.-B DIVERGES at s_B in
    # {5,6,7} (shell exp > -1))
    convB_diverge_confirmed = all(fits[s]['exp_B_meas'] > -1.0
                                  for s in (5.0, 6.0, 7.0))     # (local)
    convA_converge_confirmed = all(fits[s]['exp_A_meas'] < -1.0
                                   for s in (5.0, 6.0, 7.0))    # (local)
    sign_verdict = "PASS" if (convB_diverge_confirmed and convA_converge_confirmed) else "FAIL"  # (local)
    magnitude_ok = (r1_structural_ok and r2_ratio_ok and xroute_ok and weyl_ok
                    and prongb_ok and conv_certs_ok)            # (local) plan operator conjunction
    base_regime_ok = (ht_tail_max < EPS_TAIL and n0_check < 1e-20 and em_ok)  # (local)
    exponent_only_failure = ((not shells_ok) and r1_structural_ok and r2_ratio_ok
                             and xroute_ok and weyl_ok and conv_certs_ok
                             and lstab_ok)                      # (local)
    if info_trigger:
        magnitude_verdict = "INFO"                              # (local) classification deferred
        regime_verdict = "MARGINAL"                             # (local)
    else:
        magnitude_verdict = "PASS" if magnitude_ok else "FAIL"  # (local)
        if magnitude_ok:
            regime_verdict = "VALID" if base_regime_ok else "MARGINAL"  # (local)
        else:
            # PRE-STATED adjudication (tau0_window_diag docstring): a magnitude
            # FAIL carried SOLELY by the shell-exponent clause, with the EXACT
            # tau=0 closed form missing the band on the same window in the same
            # direction, is an out-of-regime measurement of the asymptotic
            # exponent (pre-asymptotic window) -> MARGINAL; anything else VALID
            # (the FAIL stands at composite level) unless base numerics degrade.
            if exponent_only_failure and window_artifact and base_regime_ok:
                regime_verdict = "MARGINAL"                     # (local)
            else:
                regime_verdict = "VALID" if base_regime_ok else "MARGINAL"  # (local)

    # composite via the PRE-REGISTERED collapse rule (gate-verdicts.md schema-v2)
    if regime_verdict == "BREAKDOWN":
        verdict = "FAIL"                                        # (local)
    elif sign_verdict == "FAIL":
        verdict = "FAIL"                                        # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        verdict = "FAIL"                                        # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        verdict = "INFO"                                        # (local)
    elif magnitude_verdict == "INFO":
        verdict = "INFO"                                        # (local)
    else:
        verdict = "PASS"                                        # (local)

    a2_res = float(r1[Fraction(3)]['c_m1_exact'])               # (local)
    value_str = (f"log_free_567_both_conv={r1_structural_ok and r2_ratio_ok};"
                 f"c2ratio_max={max_ratio_double:.2e};"
                 f"a2pole_sA3_res={a2_res:.10e};"
                 f"xroute_max={max_xroute:.2e};weyl_resid={weyl_resid:.2e};"
                 f"oddgrades_regular={len(half_int_locs) == 0};"
                 f"exotic_locus_logfree={all(r1[SA_FROM_GRADE[n]]['m_p_genuine'] == 0 for n in (8, 10, 12, 14))};"
                 f"shells_ok={shells_ok};Lstab_ok={lstab_ok};"
                 f"expclause_regime={'preasymptotic-window-artifact' if window_artifact else 'in-regime'}")  # (local)

    # ---------------- npz ----------------
    tab_cols = {k: np.array([row[k] for row in table]) for k in
                ('n', 's_A', 's_B', 'm_p_candidate', 'm_p_genuine', 'c_m2_r1',
                 'c_m1_r1', 'c_m2_r2', 'c_m1_r2', 'c_0_r2', 'ratio_double',
                 'xroute_rel', 'im_floor', 'gamma_collision', 'key_set')}  # (local)
    np.savez(
        OUT_NPZ,
        **{f"laurent_{k}": v for k, v in tab_cols.items()},
        residues_exact_str=np.array([
            f"s_A={sa}: Res={r1[sa]['c_m1_exact']}" for sa in genuine_poles], dtype=object),
        j_stability=np.array([[float(sa), r1[sa]['J_stability']] for sa in r1]),
        class87_witness=np.array([json.dumps(witness)], dtype=object),
        jdecay=np.array([[k, v] for k, v in jdecay.items()]),
        n0_split_check=np.array([n0_check]),
        direct_checks=np.array([json.dumps({str(k): v for k, v in direct_checks.items()})], dtype=object),
        weyl=np.array([a0_res, a0_weyl, weyl_resid, vol_implied]),
        t_grid=T_GRID, K_t=K, series_t=series, ht_tail_rel=tail_rel,
        ht_tail_max=np.array([ht_tail_max]), ht_grid_effective=np.array([n_grid_eff]),
        a_heat=np.array([a_heat[0], a_heat[2], a_heat[4], a_heat[6], a_heat[8],
                         c_t[1], c_t[2], c_t[3]]),
        evals_44_reconstructed=ev44,
        lineage=np.array([json.dumps({f"{k}": v for k, v in lineage.items()})], dtype=object),
        shell_A=np.array([json.dumps({str(s): {str(L): val for L, val in d.items()}
                                      for s, d in shell_A.items()})], dtype=object),
        shell_B=np.array([json.dumps({str(s): {str(L): val for L, val in d.items()}
                                      for s, d in shell_B.items()})], dtype=object),
        shell_fits=np.array([json.dumps({str(s): f for s, f in fits.items()})], dtype=object),
        l_stability=np.array([json.dumps({str(s): v for s, v in stab.items()})], dtype=object),
        tau0_window_diag=np.array([json.dumps({str(s): d for s, d in t0d.items()})], dtype=object),
        local_top_slopes=np.array([json.dumps({str(s): v for s, v in local_top.items()})], dtype=object),
        window_artifact=np.array([window_artifact]),
        em_validation_dev=np.array([em_dev]),
        zA_tau_fold=np.array([[s, zA_L12[s], zA_L10[s]] for s in (5.0, 6.0, 7.0)]),
        pins=np.array([json.dumps({
            "J_MAX": J_MAX, "J_MAX_DIAG": J_MAX_DIAG, "N0_SPLIT": N0_SPLIT,
            "CONTOUR_R": CONTOUR_R, "N_QUAD": N_QUAD, "mp_dps": mp.mp.dps,
            "EPS_DOUBLE": EPS_DOUBLE, "EPS_XROUTE": EPS_XROUTE, "EPS_WEYL": EPS_WEYL,
            "EPS_TAIL": EPS_TAIL, "SHELL_BAND": SHELL_BAND, "L_HUGE": L_HUGE,
            "X_CUT": X_CUT, "EVAL_CUTOFF": EVAL_CUTOFF, "tau_fold": TAU,
            "scan_grades": SCAN_GRADES, "key_sA": [str(s) for s in KEY_SA],
            "regulator_pin": "a_n^{Mellin}",
            "convention": CONVENTION, "scheme": SCHEME})], dtype=object),
        verdict=np.array([verdict], dtype=object),
        value=np.array([value_str], dtype=object),
        audit_sha256=np.array([audit_sha], dtype=object),
        content_sha256=np.array([content_sha], dtype=object),
    )
    print(f"\n[npz] {OUT_NPZ.name} written")

    # ---------------- plot ----------------
    fig, axes = plt.subplots(2, 2, figsize=(13, 9))
    ax = axes[0, 0]
    ax.semilogx(T_GRID, K * T_GRID ** 4, 'b-', lw=2, label=r'$K(t)\,t^4$ (exact partial sums)')
    ax.semilogx(T_GRID, series * T_GRID ** 4, 'r--', lw=1.4,
                label='no-log asymptotic series (8 terms)')
    ax.set_xlabel('t'); ax.set_ylabel(r'$K(t)\,t^4$')
    ax.set_title(r'Heat trace vs no-log series (cubic-point $\hat\lambda^2$ units)')
    ax.legend(); ax.grid(alpha=0.3)
    ax = axes[0, 1]
    ax.loglog(T_GRID, np.maximum(resid_rel, 1e-18), 'k-', lw=1.5)
    ax.set_xlabel('t'); ax.set_ylabel(r'$|K-\mathrm{series}|/K$')
    ax.set_title('No-log series residual (log admixture would floor this)')
    ax.grid(alpha=0.3, which='both')
    ax = axes[1, 0]
    labels = [f"n={row['n']}" if row['n'] != -99 else f"sA={row['s_A']:.0f}"
              for row in table]                                 # (local)
    vals = [max(row['ratio_double'], 1e-45) for row in table]   # (local)
    colors = ['tab:red' if row['key_set'] else
              ('tab:orange' if row['gamma_collision'] else 'tab:blue')
              for row in table]                                 # (local)
    ax.bar(range(len(table)), vals, color=colors)
    ax.set_yscale('log')
    ax.axhline(EPS_DOUBLE, color='r', ls='--', label=f'PASS threshold {EPS_DOUBLE}')
    ax.set_xticks(range(len(table))); ax.set_xticklabels(labels, rotation=60, fontsize=8)
    ax.set_ylabel(r'$|c_{-2}|/\max(|c_{-1}|,|c_0|)$')
    ax.set_title('Per-order double-pole ratio (red=verdict key set, orange=exotic locus)')
    ax.legend(); ax.grid(alpha=0.3, axis='y')
    ax = axes[1, 1]
    Lfit = np.arange(6, 13)                                     # (local)
    for s, mk in zip((5.0, 6.0, 7.0), ('o', 's', '^')):
        y = np.array([shell_A[s][L] for L in Lfit])             # (local)
        ax.loglog(Lfit, y, mk + '-', label=f'$s_A$={int(s)}: meas {fits[s]["exp_A_meas"]:+.2f} '
                                           f'(pred {fits[s]["exp_A_pred"]:+.0f})')
    ax.set_xlabel('shell L = p+q'); ax.set_ylabel('per-shell $\\zeta_A$ contribution')
    ax.set_title(r'Prong B: $\tau_{fold}$ shell decay (Conv.-A family, L12 cache + (4,4) repair)')
    ax.legend(fontsize=8); ax.grid(alpha=0.3, which='both')
    fig.suptitle(f'{GATE_ID} — pole-order pre-flight at the {{5,6,7}}-mapped orders '
                 f'[verdict: {verdict}]', fontsize=12)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    print(f"[png] {OUT_PNG.name} written")

    # ---------------- emit ----------------
    print(f"\n(value={value_str!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX_STR})")
    extra_rows = [
        "# regulator_pin=a_n^{Mellin} (== a_n^{zeta} at simple poles via Gamma-cancellation, FI); "
        "poleconv-DUAL-declared: Conv.A double-power s_A=(8-n)/2 / Conv.B single-power s_B=8-n, "
        "numerals {5,6,7} scanned under BOTH; algebra=SU(3) (A_K,H_K,D_K), NOT SU(4)_PS "
        f"# {GATE_ID} pole-labeling row",
        "# Class-8.7 witness: coincident-root loci pre-declared s_A in {0,-1,-2,-3} (n in {8,10,12,14}); "
        "zeta_A REGULAR there (Pochhammer annihilation) => Gamma*zeta_A simple; per-pole m_p table + "
        "Faulhaber->zeta_R corridor pin in s100b_cf28_simple_pole_preflight.npz[class87_witness]; "
        "_cm_1995_residue_formula.py FULL-physical template; _analytic_zeta.py off-pole-Hankel INFO corridor "
        f"# {GATE_ID} Class-8.7 witness pointer",
    ]
    print_verdict_payload(verdict, value_str, audit_sha, content_sha,
                          sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict,
                          regime_verdict=regime_verdict, extra_rows=extra_rows)
    print(f"\n=== {GATE_ID}: {verdict} (wall {time.time() - t0:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
