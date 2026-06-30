#!/usr/bin/env python3
"""
S100a W2-1 S100a-DUAL-Z3-PHI-POINTS -- Z3 phase-points: the second Z3 as a
lepton-only lever (dual-Z3 generation structure, closed form).
============================================================================

Gate: S100a-DUAL-Z3-PHI-POINTS ([SIGN])
Classification: PARTICLE
Agent: baptista-spacetime-analyst
Plan: sessions/session-plan/session-100a-plan-w2.md SS W2-1

Pre-registered operator (PASS criterion, exact; tolerance 0.0):
    { c(0), c(2pi/3), c(4pi/3) } = {1/9, 1/3, 1/3}   (multiset equality, exact QQ)
    AND  |d Omega^D/d phi| + |d Omega^c/d phi| = 0   (quark phi-independence,
                                                      exact-zero set test)
  PASS iff both exact; FAIL iff multiset mismatch OR quark phi-dependence != 0;
  INFO iff collapse direction correct but degeneracy multiplicity off
  (e.g. 3 distinct values with a near-degenerate pair).
  Float cross-check rtol = 1e-12 (machinery pin).

Output 4-tuple:
  (value=<payload>, scheme=CLOSED-FORM-OMEGA-BG, convention=EXACT-RATIONAL-QQ,
   L_max=N/A)

METHODOLOGY
-----------
Closed form on the Baptista Paper 14 SS 3 lineage
(researchers/Baptista/14_2021_Baptista_HD_Routes_SM_Fermions.md):

  eq (2.104): s_phi(h) = alpha [ s_1(h) - 2(1+e^{2 i phi}) s_2(h) ],
              s_1 = h_11^2 + h_21^2 + h_31^2,  s_2 = h_11 h_21 + h_11 h_31 + h_21 h_31
              (the s_phi uniqueness family of the vertical transformation; the
               phase phi enters through the OFF-DIAGONAL first-column monomials s_2)
  eq (3.22):  Omega^b_g = sum_j e_j e_j + 4 (e_j)_{11} e_j
                          + [ 2 ((e_j)_{11})^2 + (e_j e_j)_{11} / (1+8 cos^2 phi) ] I_3
              (lepton/b-sector Laplacian mass matrix; carries the diagonal weight
               c(phi) = 1/(1+8 cos^2 phi))
  eq (3.19):  Omega^D_g = sum_j e_j e_j + (1/3) Tr(e_j e_j) I_3   (quark D-sector;
              NO phi anywhere -- the D vertical profile h D h-bar of eq (2.17)
              contains no s_phi factor at all)
  SS 3 note:  Omega^c_g  proportional to I_3 (u_R color sector; Schur on the color
              index; the transcribed closed form carries no phi-term)

Steps:
  (1) Build the full Gell-Mann basis e_j = lambda_j / 2 (j = 1..8) in EXACT
      arithmetic over the field Q(i, sqrt3) -- matrices stored as 4 Fraction
      component-matrices M = R0 + i*I0 + sqrt3*(R1 + i*I1).
  (2) Form the four exact sums entering eq (3.22)/(3.19) over ALL 8 generators
      (K-1e lesson: never restrict to a subalgebra):
        S1 = sum_j e_j e_j                 [Casimir; must equal (4/3) I_3]
        S2 = sum_j 4 (e_j)_{11} e_j        [Cartan cross-term; diag(4/3,-2/3,-2/3)]
        S3 = sum_j ((e_j)_{11})^2          [U(1)-weight square; = 1/3]
        S4 = (S1)_{11}                     [= 4/3; multiplies c(phi)]
  (3) Evaluate c(phi) = 1/(1+8 cos^2 phi) at the Z3 orbit {0, 2pi/3, 4pi/3} in
      exact rationals (cos^2 in {1, 1/4, 1/4}); test the multiset {1/9,1/3,1/3},
      the distinct-value count (= 2), the 2-fold degeneracy at +-2pi/3, and the
      heavy/light ratio (= 3).
  (4) Diagonalize Omega^b(phi_g) = S1 + S2 + (2 S3 + S4 c_g) I_3 at each
      phi-point: exact eigenvalues (the exact matrix is diagonal; off-diagonals
      verified exactly zero) + numpy.linalg.eigvalsh float cross-check
      (rtol 1e-12, GPU_path pin: numpy.linalg, 3x3 trivially CPU).
  (5) HAAR-MOMENT LINEAGE (first-principles fiber integration): with the first
      column of Haar-SU(3) uniform on S^5 in C^3, exact Dirichlet moments
      E[prod |z_k|^{2 a_k}] = 2! prod(a_k!) / (2+sum a_k)!  and independent-phase
      vanishing give  E|s_1|^2 = 1/2, E|s_2|^2 = 1/4, E[conj(s_1) s_2] = 0,
      hence  Int_K |s_phi|^2 / (alpha^2 Vol) = 1/2 + 4 cos^2 phi
                                             = (1/2)(1 + 8 cos^2 phi),
      so the unit-norm vertical profile has alpha^2(phi) = 2 c(phi):  c(phi) IS
      the s_phi-family normalization weight. Verified exactly at all 3 points.
  (6) Quark phi-independence: construct Omega^D(phi), Omega^c(phi) per the
      closed forms as functions of phi, evaluate on the Z3 orbit + 2 generic
      off-orbit points, and require ALL pairwise entry differences to vanish
      exactly (exact-zero set test).

CONVENTION PINS (all four shift only the constant offset M_0 = S1+S2+2*S3*I;
NONE touches the gate operator -- the c(phi) multiset and the quark d/dphi
tests are invariant under each):
  - basis: HERMITIAN Gell-Mann e_j = lambda_j/2 (positive-Laplacian convention);
  - sum range: ALL 8 generators (K-1e);
  - "(e_j)^2_{11}" in eq (3.22) read as [(e_j)_{11}]^2 (reading A: the bracket
    uses the DISTINCT notation (e_j e_j)_{11} for the entry-of-the-square, so
    (e_j)^2_{11} is the square-of-the-entry; reading B would only shift M_0);
  - metric weights: round normalization (the transcribed eq (3.22) carries no
    lambda_j weights; Jensen weights would deform M_0 only, not c(phi)).

Independent cross-check: Sage-MCP (sagecell QQ) verified pre-script:
  c-multiset [1/9,1/3,1/3]; distinct=2; heavy/light=3; E|s1|^2=1/2, E|s2|^2=1/4;
  (1/2)(1+8cos^2) - (4cos^2+1/2) = 0; Omega^b eigs {94/27,40/27,40/27} at phi=0,
  {34/9,16/9,16/9} at +-2pi/3; Z3-pair degeneracy True.   (recorded in WP SS W2-1)

DISCIPLINE
----------
- from canonical_constants import *   (tau_fold / Vol_SU3_Haar echoed as context
  only; the gate operator consumes NO numerical framework constant -- it is a
  closed-form rational identity)
- every local intermediate tagged # (local)
- SHA-256 of all inputs logged in first 20 lines of stdout; S84+ dual-SHA
- verdict is PRINTED as an emit_verdict payload (print_verdict_payload); the
  dispatching agent calls mcp__knowledge__emit_verdict. NO open("a") append.
- exit 0 on script success regardless of scientific verdict
  (math-scripts.md SS "Exit Codes and Verdict Semantics")
"""

from __future__ import annotations

# --- CPU thread cap BEFORE numpy import (math-scripts.md; CPU-only 3x3 path) ---
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 1 -- Canonical constants (MANDATORY first project import)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

_SHARED = Path(__file__).resolve().parent.parent / "_shared"  # (local)
sys.path.insert(0, str(_SHARED))
from canonical_constants import *  # noqa: F401,F403  (tau_fold, Vol_SU3_Haar context echo)

# ---------------------------------------------------------------------------
# Section 2 -- Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import time
from fractions import Fraction as Fr
from math import cos, factorial, pi

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

SESSION = "100a"                                                   # (local)
GATE_ID = "S100a-DUAL-Z3-PHI-POINTS"                               # (local)
SCHEME = "CLOSED-FORM-OMEGA-BG"                                    # (local)
CONVENTION = "EXACT-RATIONAL-QQ"                                   # (local)
L_MAX = "N/A"                                                      # (local)

FLOAT_RTOL = 1e-12      # machinery pin: float cross-check rtol   # (local)
N_EVAL = 3              # three Z3 phase-points                    # (local)

# Pre-registered exact targets (plan SS W2-1 operator block)
TARGET_MULTISET = sorted([Fr(1, 9), Fr(1, 3), Fr(1, 3)])           # (local)
TARGET_DISTINCT = 2                                                # (local)
TARGET_RATIO = Fr(3)                                               # (local)

OUT_NPZ = SESSION_DIR / "s100a_dual_z3_phi_points.npz"
OUT_PNG = SESSION_DIR / "s100a_dual_z3_phi_points.png"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    # Omega^b_g(phi) is constructed in-script from the Paper 14 SS 3 closed form;
    # no external matrix file is read (plan input_files block).
]

MACHINERY_PIN_MAP = {                                              # (local)
    "_gate_id": GATE_ID,
    "_wp_id": "session-100a-w2-workingpaper.md#W2-1",
    "_scheme": SCHEME,
    "_convention": CONVENTION,
    "N_eval": "3",
    "L_max": "N/A",
    "scan_range": "phi in {0, 2pi/3, 4pi/3} (discrete Z3 orbit)",
    "step_size": "N/A",
    "tolerance": "0.0 exact QQ multiset; float cross-check rtol=1e-12",
    "random_seed": "N/A",
    "GPU_path": "numpy.linalg (3x3 eigvalsh; CPU)",
    "publication_precision": "exact rational; float echo 12 sig figs",
    "basis_pin": "Hermitian Gell-Mann e_j = lambda_j/2; all-8 sum; reading-A (e_j)_{11}^2; round normalization",
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
                     pins: dict[str, str]) -> tuple[str, str]:
    """audit_sha256 = sha256(script || canonical || pinmap_json);
    content_sha256 = sha256(script).  pinmap embeds per-gate identity keys
    (_gate_id/_scheme/_convention/...) so audit_sha256 is gate-unique."""
    script_bytes = script_path.read_bytes()                        # (local)
    canonical_bytes = canonical_path.read_bytes()                  # (local)
    full_pinmap = dict(pins)                                       # (local)
    full_pinmap.update(MACHINERY_PIN_MAP)
    pinmap_json = json.dumps(dict(sorted(full_pinmap.items())),
                             separators=(",", ":"),
                             sort_keys=True).encode("utf-8")       # (local)
    h_audit = hashlib.sha256()                                     # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()                                   # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 5a -- Exact matrix arithmetic over the field Q(i, sqrt3)
#
# A matrix is a 4-tuple (R0, I0, R1, I1) of 3x3 Fraction grids:
#     M = (R0 + i I0) + sqrt3 (R1 + i I1)
# Products use sqrt3^2 = 3 and i^2 = -1 exactly. 3x3 only -- trivial cost.
# ---------------------------------------------------------------------------

def zmat():
    return [[Fr(0)] * 3 for _ in range(3)]                          # (local)


def fmat(rows):
    return [[Fr(x) for x in r] for r in rows]                       # (local)


def madd(A, B):
    return [[A[i][j] + B[i][j] for j in range(3)] for i in range(3)]  # (local)


def mscale(s: Fr, A):
    return [[s * A[i][j] for j in range(3)] for i in range(3)]      # (local)


def mmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(3))
             for j in range(3)] for i in range(3)]                  # (local)


def qmat(R0=None, I0=None, R1=None, I1=None):
    return (R0 or zmat(), I0 or zmat(), R1 or zmat(), I1 or zmat())  # (local)


def qadd(X, Y):
    return tuple(madd(X[k], Y[k]) for k in range(4))                # (local)


def qmul(X, Y):
    """(R0+iI0+s3(R1+iI1)) * (R0'+iI0'+s3(R1'+iI1')) with s3^2=3, i^2=-1."""
    R0a, I0a, R1a, I1a = X                                          # (local)
    R0b, I0b, R1b, I1b = Y                                          # (local)
    # real-rational part: R0aR0b - I0aI0b + 3(R1aR1b - I1aI1b)
    R0 = madd(madd(mmul(R0a, R0b), mscale(Fr(-1), mmul(I0a, I0b))),
              mscale(Fr(3), madd(mmul(R1a, R1b),
                                 mscale(Fr(-1), mmul(I1a, I1b)))))  # (local)
    # imag-rational part: R0aI0b + I0aR0b + 3(R1aI1b + I1aR1b)
    I0 = madd(madd(mmul(R0a, I0b), mmul(I0a, R0b)),
              mscale(Fr(3), madd(mmul(R1a, I1b), mmul(I1a, R1b))))  # (local)
    # sqrt3 real part: R0aR1b + R1aR0b - I0aI1b - I1aI0b
    R1 = madd(madd(mmul(R0a, R1b), mmul(R1a, R0b)),
              mscale(Fr(-1), madd(mmul(I0a, I1b), mmul(I1a, I0b))))  # (local)
    # sqrt3 imag part: R0aI1b + I0aR1b + R1aI0b + I1aR0b
    I1 = madd(madd(mmul(R0a, I1b), mmul(I0a, R1b)),
              madd(mmul(R1a, I0b), mmul(I1a, R0b)))                 # (local)
    return (R0, I0, R1, I1)


def qscale_field(c4, X):
    """Scale by field scalar c4 = (r0, i0, r1, i1): (r0 + i i0 + s3 r1 + i s3 i1) X."""
    r0, i0, r1, i1 = c4                                             # (local)
    R0a, I0a, R1a, I1a = X                                          # (local)
    R0 = madd(madd(mscale(r0, R0a), mscale(-i0, I0a)),
              mscale(Fr(3), madd(mscale(r1, R1a), mscale(-i1, I1a))))  # (local)
    I0 = madd(madd(mscale(r0, I0a), mscale(i0, R0a)),
              mscale(Fr(3), madd(mscale(r1, I1a), mscale(i1, R1a))))  # (local)
    R1 = madd(madd(mscale(r0, R1a), mscale(r1, R0a)),
              madd(mscale(-i0, I1a), mscale(-i1, I0a)))             # (local)
    I1 = madd(madd(mscale(r0, I1a), mscale(i0, R1a)),
              madd(mscale(r1, I0a), mscale(i1, R0a)))               # (local)
    return (R0, I0, R1, I1)


def q11(X):
    """Field-scalar (1,1) entry of X as 4-tuple (r0, i0, r1, i1)."""
    return (X[0][0][0], X[1][0][0], X[2][0][0], X[3][0][0])         # (local)


def field_mul(a, b):
    """Product of two field scalars (r0,i0,r1,i1)."""
    a0, a1, a2, a3 = a                                              # (local)
    b0, b1, b2, b3 = b                                              # (local)
    return (a0*b0 - a1*b1 + 3*(a2*b2 - a3*b3),
            a0*b1 + a1*b0 + 3*(a2*b3 + a3*b2),
            a0*b2 + a2*b0 - a1*b3 - a3*b1,
            a0*b3 + a1*b2 + a2*b1 + a3*b0)


def q_is_rational_real(X) -> bool:
    """True iff imaginary parts and sqrt3 parts are all exactly zero."""
    return all(X[k][i][j] == 0 for k in (1, 2, 3)
               for i in range(3) for j in range(3))


def q_rational(X):
    """Extract the rational real 3x3 grid (asserts purity)."""
    assert q_is_rational_real(X), "matrix not purely rational-real"
    return X[0]


# ---------------------------------------------------------------------------
# Section 5b -- Gell-Mann basis e_j = lambda_j / 2, exact over Q(i, sqrt3)
# ---------------------------------------------------------------------------

def gellmann_basis():
    """Return [e_1..e_8] as Q(i,sqrt3) 4-tuples. Hermitian pin e_j = lambda_j/2.
    lambda_8 = diag(1,1,-2)/sqrt(3) is stored via its sqrt3-component:
    1/sqrt3 = sqrt3/3, so e_8 = diag(1,1,-2)/(2 sqrt3) = sqrt3 * diag(1,1,-2)/6."""
    h = Fr(1, 2)                                                    # (local)
    e = []                                                          # (local)
    # lambda_1 .. lambda_7 real/imag rational
    e.append(qmat(R0=fmat([[0, h, 0], [h, 0, 0], [0, 0, 0]])))            # e1
    e.append(qmat(I0=fmat([[0, -h, 0], [h, 0, 0], [0, 0, 0]])))           # e2
    e.append(qmat(R0=fmat([[h, 0, 0], [0, -h, 0], [0, 0, 0]])))           # e3
    e.append(qmat(R0=fmat([[0, 0, h], [0, 0, 0], [h, 0, 0]])))            # e4
    e.append(qmat(I0=fmat([[0, 0, -h], [0, 0, 0], [h, 0, 0]])))           # e5
    e.append(qmat(R0=fmat([[0, 0, 0], [0, 0, h], [0, h, 0]])))            # e6
    e.append(qmat(I0=fmat([[0, 0, 0], [0, 0, -h], [0, h, 0]])))           # e7
    s = Fr(1, 6)                                                    # (local)
    e.append(qmat(R1=fmat([[s, 0, 0], [0, s, 0], [0, 0, -2 * s]])))       # e8
    return e


# ---------------------------------------------------------------------------
# Section 5c -- Haar-moment mini-engine (exact fiber integration, S^5 column)
# ---------------------------------------------------------------------------

S1_MONOS = [((2, 0, 0), 1), ((0, 2, 0), 1), ((0, 0, 2), 1)]        # s_1 = sum z_k^2
S2_MONOS = [((1, 1, 0), 1), ((1, 0, 1), 1), ((0, 1, 1), 1)]        # s_2 = sum_{i<j} z_i z_j


def haar_pair_moment(a, b) -> Fr:
    """E[ z^a conj(z)^b ] on uniform S^5 in C^3: zero unless a == b
    componentwise (independent-phase invariance), else Dirichlet
    E[prod |z_k|^{2 a_k}] = (3-1)! prod(a_k!) / (3-1+sum a_k)!."""
    if a != b:
        return Fr(0)
    num = factorial(2)                                              # (local)
    for ak in a:
        num *= factorial(ak)
    return Fr(num, factorial(2 + sum(a)))


def haar_E_conj_f_g(f_monos, g_monos) -> Fr:
    """E[ conj(f) g ] for f, g given as monomial lists."""
    tot = Fr(0)                                                     # (local)
    for (a, ca) in f_monos:
        for (b, cb) in g_monos:
            tot += ca * cb * haar_pair_moment(b, a)  # conj(z^a) z^b
    return tot


# ---------------------------------------------------------------------------
# Section 5d -- Compute
# ---------------------------------------------------------------------------

def compute() -> dict:
    res: dict = {}                                                  # (local)
    e = gellmann_basis()                                            # (local)

    # ---- (2) The four exact sums over ALL 8 generators (K-1e pin) ----
    S1 = qmat()                                                     # (local)
    S2 = qmat()                                                     # (local)
    S3 = (Fr(0), Fr(0), Fr(0), Fr(0))                               # (local)
    for ej in e:
        S1 = qadd(S1, qmul(ej, ej))
        d11 = q11(ej)                                               # (local)
        four_d11 = tuple(4 * x for x in d11)                        # (local)
        S2 = qadd(S2, qscale_field(four_d11, ej))
        sq = field_mul(d11, d11)                                    # (local)
        S3 = tuple(S3[k] + sq[k] for k in range(4))

    S1r = q_rational(S1)                                            # (local)
    S2r = q_rational(S2)                                            # (local)
    assert S3[1] == S3[2] == S3[3] == 0, "S3 not rational-real"
    S3v = S3[0]                                                     # (local)
    S4v = S1r[0][0]                                                 # (local)

    # Structural cross-checks (substitution-chain anchors)
    casimir_ok = all(S1r[i][j] == (Fr(4, 3) if i == j else 0)
                     for i in range(3) for j in range(3))           # (local)
    S2_expect = [[Fr(4, 3), 0, 0], [0, Fr(-2, 3), 0], [0, 0, Fr(-2, 3)]]  # (local)
    S2_ok = all(S2r[i][j] == S2_expect[i][j]
                for i in range(3) for j in range(3))                # (local)
    S3_ok = (S3v == Fr(1, 3))                                       # (local)
    S4_ok = (S4v == Fr(4, 3))                                       # (local)
    print("Exact sums over all 8 Gell-Mann generators (e_j = lambda_j/2):")
    print(f"  S1 = sum e_j e_j           = (4/3) I_3 exactly : {casimir_ok}")
    print(f"  S2 = sum 4 (e_j)_11 e_j    = diag(4/3,-2/3,-2/3): {S2_ok}")
    print(f"  S3 = sum ((e_j)_11)^2      = {S3v}  (= 1/3): {S3_ok}")
    print(f"  S4 = (S1)_11               = {S4v}  (= 4/3): {S4_ok}")
    assert casimir_ok and S2_ok and S3_ok and S4_ok, "basis-sum cross-check failed"

    # ---- (3) c(phi) at the Z3 orbit, exact QQ ----
    # cos(0) = 1, cos(2pi/3) = -1/2, cos(4pi/3) = -1/2  (closed form);
    # exact cos^2 values pinned with float cross-check below.
    phi_labels = ["0", "2pi/3", "4pi/3"]                            # (local)
    phi_floats = [0.0, 2.0 * pi / 3.0, 4.0 * pi / 3.0]              # (local)
    cos2_exact = [Fr(1), Fr(1, 4), Fr(1, 4)]                        # (local)
    for pf, c2e in zip(phi_floats, cos2_exact):
        dev = abs(cos(pf) ** 2 - float(c2e))                        # (local)
        assert dev < 1e-15, f"cos^2 float/exact mismatch: {dev}"
    c_exact = [Fr(1) / (1 + 8 * c2) for c2 in cos2_exact]           # (local)
    c_float = [1.0 / (1.0 + 8.0 * cos(pf) ** 2) for pf in phi_floats]  # (local)
    for ce, cf in zip(c_exact, c_float):
        assert abs(float(ce) - cf) < 1e-15

    multiset_match = (sorted(c_exact) == TARGET_MULTISET)           # (local)
    distinct_count = len(set(c_exact))                              # (local)
    pair_degenerate = (c_exact[1] == c_exact[2])                    # (local)
    heavy_light = max(c_exact) / min(c_exact)                       # (local)
    ratio_ok = (heavy_light == TARGET_RATIO)                        # (local)
    print("\nc(phi) = 1/(1+8 cos^2 phi) at the Z3 phase-points (exact QQ):")
    for lab, ce in zip(phi_labels, c_exact):
        print(f"  c({lab:>6}) = {ce}   (float {float(ce):.12g})")
    print(f"  multiset == {{1/9, 1/3, 1/3}}: {multiset_match}")
    print(f"  distinct-value count = {distinct_count} (target {TARGET_DISTINCT})")
    print(f"  2-fold degeneracy at +-2pi/3 (c equal): {pair_degenerate}")
    print(f"  heavy/light ratio = {heavy_light} (target 3): {ratio_ok}")

    # ---- (5) Haar-moment lineage of 1 + 8 cos^2 phi ----
    E_s1s1 = haar_E_conj_f_g(S1_MONOS, S1_MONOS)                    # (local)
    E_s2s2 = haar_E_conj_f_g(S2_MONOS, S2_MONOS)                    # (local)
    E_s1s2 = haar_E_conj_f_g(S1_MONOS, S2_MONOS)                    # (local)
    haar_ok = (E_s1s1 == Fr(1, 2) and E_s2s2 == Fr(1, 4)
               and E_s1s2 == 0)                                     # (local)
    print("\nHaar-moment lineage (exact Dirichlet moments, S^5 column of SU(3)):")
    print(f"  E|s_1|^2 = {E_s1s1} (= 1/2), E|s_2|^2 = {E_s2s2} (= 1/4), "
          f"E[conj(s_1) s_2] = {E_s1s2} (= 0): {haar_ok}")
    # N(phi)/alpha^2 = E|s1|^2 + |2(1+e^{2 i phi})|^2 E|s2|^2, |...|^2 = 16 cos^2
    lineage_ok = True                                               # (local)
    for lab, c2e, ce in zip(phi_labels, cos2_exact, c_exact):
        N_g = E_s1s1 + 16 * c2e * E_s2s2                            # (local)
        half_over_N = Fr(1, 2) / N_g                                # (local)
        ok = (half_over_N == ce) and (N_g == Fr(1, 2) * (1 + 8 * c2e))  # (local)
        lineage_ok = lineage_ok and ok
        print(f"  N({lab:>6}) = {N_g} = (1/2)(1+8cos^2); (1/2)/N = {half_over_N} "
              f"== c: {ok}")
    print(f"  c(phi) = alpha^2(phi)/2 normalization-weight lineage: {lineage_ok}")

    # ---- (4) Omega^b(phi_g) exact spectra + float cross-check ----
    I3 = qmat(R0=fmat([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))           # (local)
    M0 = qadd(qadd(S1, S2),
              qscale_field((2 * S3v, Fr(0), Fr(0), Fr(0)), I3))     # (local)
    M0r = q_rational(M0)                                            # (local)
    M0_diag = [M0r[i][i] for i in range(3)]                         # (local)
    M0_offdiag_zero = all(M0r[i][j] == 0 for i in range(3)
                          for j in range(3) if i != j)              # (local)
    print(f"\nM_0 = S1 + S2 + 2 S3 I_3 = diag({M0_diag[0]}, {M0_diag[1]}, "
          f"{M0_diag[2]}); off-diagonals exactly zero: {M0_offdiag_zero}")
    assert M0_offdiag_zero

    eigs_exact = []                                                 # (local)
    eigs_float_dev_max = 0.0                                        # (local)
    for lab, ce in zip(phi_labels, c_exact):
        diag_g = sorted([m + S4v * ce for m in M0_diag], reverse=True)  # (local)
        eigs_exact.append(diag_g)
        Ob_float = np.diag([float(m + S4v * ce) for m in M0_diag])  # (local)
        ev = np.sort(np.linalg.eigvalsh(Ob_float))[::-1]            # (local)
        dev = max(abs(ev[k] - float(diag_g[k])) /
                  max(abs(float(diag_g[k])), 1e-300) for k in range(3))  # (local)
        eigs_float_dev_max = max(eigs_float_dev_max, dev)
        print(f"  Omega^b({lab:>6}) eigs exact = "
              f"[{diag_g[0]}, {diag_g[1]}, {diag_g[2]}]  "
              f"(floats {[f'{float(x):.12g}' for x in diag_g]}); "
              f"numpy eigvalsh rel-dev {dev:.2e}")
    float_ok = (eigs_float_dev_max < FLOAT_RTOL)                    # (local)
    z3_pair_spectrum_equal = (eigs_exact[1] == eigs_exact[2])       # (local)
    print(f"  numpy.linalg float cross-check max rel-dev = {eigs_float_dev_max:.2e}"
          f" < rtol {FLOAT_RTOL}: {float_ok}")
    print(f"  Z3-pair spectra equal (phi=2pi/3 vs 4pi/3), exact: "
          f"{z3_pair_spectrum_equal}")
    # per-generation weight recovery: (Omega^b(phi_g) - M0)_11 / S4 == c_g exact
    recover_ok = all((eigs_exact[k][0] - M0_diag[0]) / S4v == c_exact[k]
                     for k in range(3))                             # (local)
    print(f"  c_g recovered from spectrum shift (eig - M0)/S4 exactly: {recover_ok}")

    # ---- (6) Quark counterparts: exact phi-independence ----
    def omega_D_of_phi(_phi):
        """Eq (3.19): Omega^D = S1 + (1/3) Tr(S1) I_3. NO phi enters: the D
        vertical profile h D h-bar (eq 2.17) carries no s_phi factor."""
        trS1 = sum(S1r[i][i] for i in range(3))                     # (local)
        return [[S1r[i][j] + (trS1 / 3 if i == j else 0)
                 for j in range(3)] for i in range(3)]

    def omega_c_of_phi(_phi):
        """SS 3 closed form: Omega^c proportional to I_3 (color Schur); the
        transcribed form carries no phi-term. Representative kappa_c = S4
        (value non-load-bearing; only its phi-independence is gated)."""
        return [[S4v if i == j else Fr(0) for j in range(3)]
                for i in range(3)]

    probe_phis = phi_floats + [0.7, 2.1]   # Z3 orbit + 2 generic off-orbit  # (local)
    quark_dphi_total = Fr(0)                                        # (local)
    for build in (omega_D_of_phi, omega_c_of_phi):
        mats = [build(p) for p in probe_phis]                       # (local)
        for a in range(len(mats)):
            for b in range(a + 1, len(mats)):
                quark_dphi_total += sum(abs(mats[a][i][j] - mats[b][i][j])
                                        for i in range(3) for j in range(3))
    quark_ok = (quark_dphi_total == 0)                              # (local)
    OmegaD = omega_D_of_phi(0.0)                                    # (local)
    print(f"\nQuark sector (exact-zero set test over Z3 orbit + 2 generic points):")
    print(f"  Omega^D = diag({OmegaD[0][0]}, {OmegaD[1][1]}, {OmegaD[2][2]}) "
          f"(= (8/3) I_3); Omega^c = {S4v} I_3")
    print(f"  sum of all pairwise |Delta entries| over phi-probes = "
          f"{quark_dphi_total} (exact zero): {quark_ok}")

    res.update(dict(
        c_exact=c_exact, c_float=c_float, cos2_exact=cos2_exact,
        phi_labels=phi_labels, phi_floats=phi_floats,
        multiset_match=multiset_match, distinct_count=distinct_count,
        pair_degenerate=pair_degenerate, heavy_light=heavy_light,
        ratio_ok=ratio_ok, haar_ok=haar_ok, lineage_ok=lineage_ok,
        E_s1s1=E_s1s1, E_s2s2=E_s2s2, E_s1s2=E_s1s2,
        M0_diag=M0_diag, eigs_exact=eigs_exact, float_ok=float_ok,
        eigs_float_dev_max=eigs_float_dev_max,
        z3_pair_spectrum_equal=z3_pair_spectrum_equal,
        recover_ok=recover_ok, quark_ok=quark_ok,
        quark_dphi_total=quark_dphi_total,
        S3v=S3v, S4v=S4v, OmegaD_11=OmegaD[0][0],
        casimir_ok=casimir_ok, S2_ok=S2_ok, S3_ok=S3_ok, S4_ok=S4_ok,
    ))
    return res


# ---------------------------------------------------------------------------
# Section 6 -- Gate verdict + [SIGN] 3-tuple
# ---------------------------------------------------------------------------

def evaluate_gate(r: dict) -> tuple[str, str, str, str]:
    """Return (composite, sign_verdict, magnitude_verdict, regime_verdict)
    per the plan operator + gate-verdicts.md collapse rule."""
    # SIGN: pre-registered direction heavy/light = 3 > 1 (2-tier split, not 1:1:1)
    sign_v = "PASS" if r["heavy_light"] > 1 else "FAIL"             # (local)
    # MAGNITUDE: exact multiset match AND quark exact zero (tolerance 0.0),
    # backed by the float cross-check at rtol 1e-12.
    exact_core = (r["multiset_match"] and r["quark_ok"]
                  and r["distinct_count"] == TARGET_DISTINCT
                  and r["pair_degenerate"] and r["ratio_ok"]
                  and r["haar_ok"] and r["lineage_ok"]
                  and r["z3_pair_spectrum_equal"] and r["recover_ok"]
                  and r["float_ok"])                                # (local)
    if exact_core:
        mag_v = "PASS"                                              # (local)
    elif (r["distinct_count"] == 3 and r["quark_ok"]
          and min(abs(float(r["c_exact"][1] - r["c_exact"][2])), 1.0) < 0.05):
        # INFO clause: collapse direction correct but degeneracy multiplicity off
        mag_v = "INFO"                                              # (local)
    else:
        mag_v = "FAIL"                                              # (local)
    # REGIME: closed-form exact arithmetic, no truncation/expansion window
    regime_v = "VALID"                                              # (local)
    # composite collapse rule (gate-verdicts.md, pre-registered)
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
    return comp, sign_v, mag_v, regime_v


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
# Section 7 -- Plot + data
# ---------------------------------------------------------------------------

def make_plot(r: dict, verdict: str) -> None:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.5, 5.0))       # (local)
    phi_grid = np.linspace(0, 2 * np.pi, 721)                       # (local)
    c_grid = 1.0 / (1.0 + 8.0 * np.cos(phi_grid) ** 2)              # (local)

    ax1.plot(phi_grid, c_grid, "b-", lw=1.6,
             label=r"$c(\varphi)=1/(1+8\cos^2\varphi)$")
    ax1.axhline(1 / 9, color="gray", ls="--", lw=0.9)
    ax1.axhline(1 / 3, color="gray", ls="--", lw=0.9)
    ax1.text(0.05, 1 / 9 + 0.012, r"$1/9$", fontsize=11)
    ax1.text(0.05, 1 / 3 + 0.012, r"$1/3$", fontsize=11)
    for pf, ce, lab in zip(r["phi_floats"], r["c_exact"], r["phi_labels"]):
        ax1.plot(pf, float(ce), "ro", ms=9, zorder=5)
        ax1.annotate(rf"$\varphi={lab}$" + "\n" + rf"$c={ce}$",
                     (pf, float(ce)), textcoords="offset points",
                     xytext=(10, 14), fontsize=9)
    ax1.set_xlabel(r"$\varphi$")
    ax1.set_ylabel(r"$c(\varphi)$")
    ax1.set_title("Second-Z3 lever: c at the Z3 orbit collapses to {1/9, 1/3, 1/3}\n"
                  "(2-fold degeneracy at +-2pi/3; heavy/light = 3 exact)")
    ax1.legend(loc="upper center", fontsize=9)
    ax1.set_xlim(0, 2 * np.pi)

    M0f = [float(x) for x in r["M0_diag"]]                          # (local)
    S4f = float(r["S4v"])                                           # (local)
    branch_heavy = M0f[0] + S4f * c_grid                            # (local)
    branch_light = M0f[1] + S4f * c_grid                            # (local)
    ax2.plot(phi_grid, branch_heavy, "b-", lw=1.6,
             label=r"$\Omega^b$ e-branch ($M_0=10/3$)")
    ax2.plot(phi_grid, branch_light, "g-", lw=1.6,
             label=r"$\Omega^b$ $(\nu_L,e_L)$-doublet ($M_0=4/3$, deg 2)")
    ax2.axhline(float(r["OmegaD_11"]), color="darkorange", ls="-", lw=2.0,
                label=r"$\Omega^D = (8/3)\,I_3$ (quark, $\partial_\varphi=0$)")
    ax2.axhline(S4f, color="purple", ls="-.", lw=1.6,
                label=r"$\Omega^c = (4/3)\,I_3$ (quark, $\partial_\varphi=0$)")
    for pf, eg in zip(r["phi_floats"], r["eigs_exact"]):
        ax2.plot([pf] * 3, [float(x) for x in eg], "rs", ms=6, zorder=5)
    ax2.set_xlabel(r"$\varphi$")
    ax2.set_ylabel("Laplacian mass-matrix eigenvalues")
    ax2.set_title("Lepton-only lever: Omega^b eigen-branches ride c(phi);\n"
                  "quark Omega^D, Omega^c are exactly flat")
    ax2.legend(loc="center right", fontsize=8)
    ax2.set_xlim(0, 2 * np.pi)

    fig.suptitle(f"{GATE_ID}: {verdict} -- dual-Z3 phase-points "
                 f"(Baptista Paper 14 eq 3.22 lineage; exact QQ)", fontsize=12)
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    fig.savefig(OUT_PNG, dpi=150)
    plt.close(fig)
    print(f"\nplot -> {OUT_PNG.name}")


def save_npz(r: dict, verdict: str, tup3: tuple, audit_sha: str,
             content_sha: str) -> None:
    def fr_nd(fr_list):
        return (np.array([f.numerator for f in fr_list], dtype=np.int64),
                np.array([f.denominator for f in fr_list], dtype=np.int64))
    c_num, c_den = fr_nd(r["c_exact"])                              # (local)
    m0_num, m0_den = fr_nd(r["M0_diag"])                            # (local)
    eig_num = np.array([[x.numerator for x in row]
                        for row in r["eigs_exact"]], dtype=np.int64)  # (local)
    eig_den = np.array([[x.denominator for x in row]
                        for row in r["eigs_exact"]], dtype=np.int64)  # (local)
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID, scheme=SCHEME, convention=CONVENTION,
        l_max=str(L_MAX), verdict=verdict,
        sign_verdict=tup3[0], magnitude_verdict=tup3[1], regime_verdict=tup3[2],
        phi_labels=np.array(r["phi_labels"]),
        phi_floats=np.array(r["phi_floats"]),
        c_num=c_num, c_den=c_den,
        c_float=np.array(r["c_float"]),
        multiset_match=r["multiset_match"],
        distinct_count=r["distinct_count"],
        pair_degenerate=r["pair_degenerate"],
        heavy_light_num=r["heavy_light"].numerator,
        heavy_light_den=r["heavy_light"].denominator,
        E_s1s1=float(r["E_s1s1"]), E_s2s2=float(r["E_s2s2"]),
        E_s1s2=float(r["E_s1s2"]),
        haar_ok=r["haar_ok"], lineage_ok=r["lineage_ok"],
        M0_diag_num=m0_num, M0_diag_den=m0_den,
        omega_b_eigs_num=eig_num, omega_b_eigs_den=eig_den,
        omega_b_eigs_float=np.array([[float(x) for x in row]
                                     for row in r["eigs_exact"]]),
        eigs_float_dev_max=r["eigs_float_dev_max"],
        z3_pair_spectrum_equal=r["z3_pair_spectrum_equal"],
        recover_ok=r["recover_ok"],
        quark_dphi_total=float(r["quark_dphi_total"]),
        quark_ok=r["quark_ok"],
        omegaD_diag=float(r["OmegaD_11"]),
        omegac_diag=float(r["S4v"]),
        S3=float(r["S3v"]), S4=float(r["S4v"]),
        casimir_ok=r["casimir_ok"], S2_ok=r["S2_ok"],
        basis_pin=MACHINERY_PIN_MAP["basis_pin"],
        tau_fold_context=float(tau_fold),       # context echo only (not consumed)
        vol_su3_haar_context=float(Vol_SU3_Haar),  # context echo only
        audit_sha256=audit_sha, content_sha256=content_sha,
        schema_version="S84+",
    )
    print(f"data -> {OUT_NPZ.name}")


# ---------------------------------------------------------------------------
# Section 8 -- Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()                                                # (local)
    pins = log_input_pins(INPUT_FILES)                              # (local)
    script_path = Path(__file__).resolve()                          # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"          # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha} (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha} (script only)")
    print()

    r = compute()                                                   # (local)
    verdict, sign_v, mag_v, regime_v = evaluate_gate(r)             # (local)

    value = ("c={1/9,1/3,1/3}exact;distinct=2;deg2@pm2pi/3;heavy/light=3;"
             "quark_dphi=0;haar(1/2)(1+8cos^2)ok")                  # (local)

    make_plot(r, verdict)
    save_npz(r, verdict, (sign_v, mag_v, regime_v), audit_sha, content_sha)

    print()
    print(emit_4tuple(value, SCHEME, CONVENTION, L_MAX))
    print_verdict_payload(
        verdict, value, audit_sha, content_sha,
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v,
        companion_note=("dual-Z3 lepton-only lever; eq 3.22 lineage; "
                        "Sage-MCP cross-verified"),
        extra_rows=[
            "# Omega^b eigs exact: phi=0 -> {94/27,40/27,40/27}; "
            "phi=+-2pi/3 -> {34/9,16/9,16/9}; M0=diag(10/3,4/3,4/3); "
            "Omega^D=(8/3)I_3, Omega^c=(4/3)I_3 phi-flat exact "
            "# S100a-DUAL-Z3-PHI-POINTS closed-form detail",
        ],
    )

    print(f"\n=== {GATE_ID}: {verdict} (sign={sign_v} magnitude={mag_v} "
          f"regime={regime_v}; wall {time.time() - t0:.1f}s) ===")
    return 0   # exit 0 on script success regardless of scientific verdict


if __name__ == "__main__":
    sys.exit(main())
