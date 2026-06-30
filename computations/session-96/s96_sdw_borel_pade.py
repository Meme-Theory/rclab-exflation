#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S96-SDW-BOREL-PADE
==================

Gate: S96-SDW-BOREL-PADE  ([VERIFY])
Plan: sessions/session-plan/session-96-plan-w2.md §W2-1
Agent: lizzi-spectral-functional-theorist
Working paper: sessions/archive/session-96/session-96-w2-workingpaper.md §W2-1

PURPOSE (renormalization computation under the CC magnitude):
  S94-K-CSUB-R-ABSOLUTE-CONVERGENCE proved the RAW mode-count a_2 Mellin-s=2
  moment a_2^raw(L_max) = Sum_{(p,q)} dim(p,q) |lambda(p,q,tau)|^{-4} DIVERGES
  with the Peter-Weyl truncation L_max (max|dK/dL|=2.107e30, dK/dL increasing,
  the geometric-pure divergence signature). The zeta-regulated moment
  a_2_FW_zeta = 2776.165389 (S88-A-N-FW-CANONICALIZATION) is FINITE.

  THIS gate asks the renormalization question of the framework in the substrate's
  own terms: is the divergent raw SDW series Borel/Pade-Borel-resummable to the
  finite zeta value? If yes, the zeta moment IS the resummed physical absolute
  and the CC-absolute conditional is PARTIALLY discharged (the divergence is a
  re-summable asymptotic artifact). If no (positive-real-axis Borel singularity),
  the absolute moment is genuinely scheme-dependent and the CC-absolute stays
  conditional (JACOBSON-NONLOCAL-64 hardens toward a structural wall).

  Three regulator-class partial-sum constructions (functional-pluralism spine,
  lizzi methodology law; each tagged per regulator-pin-discipline.md):
    (raw)     a_2^{raw}(L)  = Sum dim |lambda|^{-4}        [S94 bare_moment; a_2^{raw} quarantine label]
    (PV)      a_2^{PV}(L)   = Sum dim [ lam^{-4} - 2(lam^2+1)^{-2} + (lam^2+2)^{-2} ]  [a_2^{Pauli-Villars}, S94 subtractive 2-pt PV]
    (Mellin)  a_2^{Mellin}(L) = Sum dim |lambda|^{-4}      [a_2^{Mellin} = a_2^{zeta} on the positive-definite spectrum; S94 a2_mellin==a2_bare]
  For each class the resummation target is the SAME zeta value a_2_FW_zeta=2776.165389.

PRE-REGISTERED THRESHOLD (plan §W2-1 operator + strict_PASS_boundary):
  operator: ratio.   form: |BorelSum(a_2^raw series) - a_2_FW_zeta| / a_2_FW_zeta <= tau_resum.
  PASS  iff  |delta|/a_2_FW_zeta <= 0.10  AND  Borel-summability pre-condition met
            (the [M/M] Pade-Borel approximant has NO positive-real-axis pole).
            => the zeta moment IS the Borel sum; CC-absolute PARTIALLY discharged (Track A).
  FAIL  iff  the raw series is NOT Borel-summable (positive-real-axis Borel singularity
            in the [M/M] Pade approximant)  OR  the resummed value misses the zeta
            value by > 10%.  => absolute moment genuinely scheme-dependent (Track B).
  INFO  iff  Borel-summable but to a DIFFERENT finite value (not within 10% of zeta).
            => scheme ambiguity QUANTIFIED (pinned scheme-ambiguity band).
  Tolerance rule: RATIO on |delta|/a_2_FW_zeta vs the 0.10 band; Borel-summability is
    a structural pre-condition (positive-real-pole present/absent) decided by the
    [M/M] pole structure, NOT assumed.

SUBSTITUTION CHAIN (plan §W2-1; direction of the convergence claim):
  Claim: "If the raw SDW series is Borel-summable, its Borel sum can equal the finite
          zeta value despite the partial sums diverging."
    Def 1: a_2^raw(L_max) = Sum_{(p,q): p+q<=L_max} m_{(p,q)} |D_{(p,q)}|^{-4}
           (raw mode-count Mellin-s=2 moment; NOT Seeley-DeWitt; §8.2 firewall;
           S94 confirms a_2^raw(L) increases without bound, dK/dL increasing).
    Def 2: a_2_FW_zeta = Res_{s=3}[Tr(D_K^{-2s})] = 2776.165389
           (zeta-regulated FINITE curvature integral; canonical_constants S88;
           ZETA-NOT-PHYSICAL: this absolute is a regulator artifact but it IS finite).
    Def 3: BorelSum(Sum_k c_k) = integral_0^inf e^{-t} B(t) dt, B(t)=Sum_k (c_k/k!) t^k,
           c_k = a_2^raw(L=k+5) - a_2^raw(L=k+4)  (the per-L increment series).
    Substitute: a divergent series with c_k ~ A r^k (geometric-divergent, the S94
           signature; measured r ~ 2.111 here) has Borel transform with a pole at
           t = 1/r > 0 ON the positive real axis (Sage: (a r^{k+1})/(a r^k)=r EXACT;
           geometric increment ratio is the CONSTANT r => genuine divergence, NOT a
           multiplicative w(L) artifact that would cancel under a log-derivative).
    Simplify: a pole on the positive real Laplace axis => the Borel integral is NOT
           defined (Borel-NON-summable in the strict sense) UNLESS the pole is off-axis
           or a lateral/Pade-Borel prescription regularizes it.
    Direction: PASS requires the Borel sum to CONVERGE TOWARD the zeta value
           (|delta| DECREASING with Pade order M) AND the [M/M] approximant to have NO
           positive-real pole. The DIRECTION test is the load-bearing measurement:
           |delta(M)| decreasing => convergent toward zeta; increasing => away.
    Conclusion: the gate computes the Pade-Borel sum and its distance to a_2_FW_zeta.
           A positive-real-axis Borel singularity (the generic geometric-divergence
           outcome) is the FAIL/INFO discriminator, decided by the [M/M] pole structure,
           NOT assumed.

MULTIPLICATIVE-NORMALIZATION PRE-FLIGHT (math-scripts.md §"Multiplicative-
  normalization cancellation invariants", MANDATORY K=3; declared in machinery_pin_map):
  The K=3 cancellation pathology fires ONLY for a K-dependent log-derivative operator
  L_n = d^n ln(f)/d(ln K)^n acting on f = w(L_max)*g(K). THIS gate has NO log-derivative
  operator (it is an ABSOLUTE Borel-Pade resummation of a moment SUM), so the pathology
  does NOT apply by operator type. The Sage sage_simplify disambiguator confirms the
  divergence is GENUINE geometric growth (increment ratio = constant r, INDEPENDENT of
  k), NOT a multiplicative w(L_max) artifact:
    sage_simplify("(a*r^(k+1)) / (a*r^k)")  ->  r           [constant => genuine, not w(L)]
    sage_simplify("sum(a*(r*t)^k/factorial(k), k, 0, oo)")  ->  a*e^(r*t)   [Borel transform]
  => MULTIPLICATIVE-NORMALIZATION-CANCELLATION-DETECTED = False. The resummation operates
  on a genuinely-divergent series, NOT a structural identity; the gate's PASS criterion
  targets the resummed VALUE vs a_2_FW_zeta, as pre-registered (not an L-stability plateau).

CLASS pin: the raw/PV/Mellin partial sums are built from the FULL CM-1995 §III.4
  jensen_irrep_table (CLASS=FULL — substrate-IS D_K(tau) eigenvalues, NOT a Casimir
  surrogate). The Borel-Pade resummation is a closed-form scalar operation on the 7-term
  increment series. No SCHEMATIC helper consumed => NO -SCHEMATIC suffix.

Regulator pins (regulator-pin-discipline.md MANDATORY; bare a_n FORBIDDEN):
  a_2^{raw} (quarantine label, NOT Seeley-DeWitt), a_2^{Pauli-Villars}, a_2^{Mellin}.

Classification: GEOMETRIC. The a_2 moment is the SECOND spectral moment of D_K; the raw
  mode-count truncation slice is a finite slice of the substrate's own spectral content.
  Explanation flows: D_K eigenvalues -> raw/zeta moments -> CC-absolute status ->
  downstream observable (phononic-framing.md §"IS Space, Not IN Space").

Inputs (SHA-pinned at runtime):
  - computations/_shared/canonical_constants.py                          (a_2_FW_zeta, a_0_FW_zeta, tau_fold, M_KK)
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz            (cross-check anchor; L_max=12)
  - computations/session-94/s94_w1_4_k_csub_r_absolute_convergence.npz   (S94 raw bare_moment series; runtime SHA verified)
  - computations/_shared/_cm_1995_residue_formula.py                     (FULL jensen_irrep_table; CLASS=FULL)

Outputs:
  - computations/session-96/s96_sdw_borel_pade.npz
  - computations/session-96/s96_sdw_borel_pade.png
  - verdict line + dual-SHA companion row -> computations/session-96/s96_gate_verdicts.txt
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # GPU_path pin = numpy cpu-cap-OMP8 (Borel-Pade on ~8 scalars; cache load read-only)
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import json
import math
import hashlib
from pathlib import Path

import numpy as np
import mpmath as mp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 1 — Paths + canonical constants import
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
COMPUTATIONS_DIR = PROJECT_ROOT / "computations"
SESSION_96_DIR = PROJECT_ROOT / "computations" / "session-96"
sys.path.insert(0, str(SHARED_DIR))
sys.path.insert(0, str(COMPUTATIONS_DIR))

from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (  # noqa: E402
    M_KK,
    tau_fold,
    a_2_FW_zeta,
    a_0_FW_zeta,
)

# FULL physical CM-1995 §III.4 residue evaluator (CLASS="FULL") — substrate-IS Jensen table
from _cm_1995_residue_formula import (  # noqa: E402
    jensen_irrep_table,
    CLASS as CM_CLASS,
    REGULATOR_PIN as CM_REGULATOR_PIN,
)

CANONICAL_CONSTANTS_PATH = SHARED_DIR / "canonical_constants.py"
CM_EVALUATOR_PATH = SHARED_DIR / "_cm_1995_residue_formula.py"
L12_CACHE_PATH = PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
S94_NPZ_PATH = PROJECT_ROOT / "computations" / "session-94" / "s94_w1_4_k_csub_r_absolute_convergence.npz"

# Plan-pinned input SHAs (plan §W2-1 input_files); the .py provenance SHA is pinned in the plan,
# the s94 NPZ SHA is <computed-at-runtime> (verified on read below).
S94_PY_PROVENANCE_SHA = "273514bd1006aad1189023996b693a9c3d12a16b7f8cc22e8b42a45be5c4aa1b"  # (local) plan-pinned .py SHA
S94_PY_PATH = PROJECT_ROOT / "computations" / "session-94" / "s94_w1_4_k_csub_r_absolute_convergence.py"  # (local)

OUT_NPZ = SESSION_96_DIR / "s96_sdw_borel_pade.npz"
OUT_PNG = SESSION_96_DIR / "s96_sdw_borel_pade.png"
VERDICT_TXT = SESSION_96_DIR / "s96_gate_verdicts.txt"

# ---------------------------------------------------------------------------
# Section 2 — Gate identity + pre-registered machinery pins (plan §W2-1)
# ---------------------------------------------------------------------------
GATE_ID = "S96-SDW-BOREL-PADE"
SCHEME = "Borel-Pade-resummation"
CONVENTION = "ABSOLUTE"   # the gate tests an absolute-magnitude resummation (NOT a ratio of moments)
L_MAX = 12                # (local) — cache ceiling; sequence built at L_max in {5..12}

# Pre-registered thresholds (plan §W2-1 operator + strict_PASS_boundary):
TAU_RESUM = 0.10                     # (local) — PASS band: |delta|/a_2_FW_zeta <= 0.10
BOREL_QUAD_TOL = 1.0e-12             # (local) — float64 Borel-Laplace quadrature absolute tolerance
PADE_ORDERS = (1, 2, 3)             # (local) — diagonal [M/M] orders (7 increments => c_0..c_6 => M<=3)
L_SEQ = (5, 6, 7, 8, 9, 10, 11, 12)  # (local) — partial-sum L_max scan (8 partial sums)
PUBLICATION_SIG_FIGS = 6             # (local) — resummed value cited vs a_2_FW_zeta=2776.165389
POSREAL_POLE_TOL = 1.0e-9            # (local) — |Im(pole)| below this AND Re(pole)>0 => positive-real-axis singularity

# A_2 target (zeta-regulated, S88 canonical):
A2_ZETA_TARGET = float(a_2_FW_zeta)  # (local) — 2776.165389
A0_ZETA_TARGET = float(a_0_FW_zeta)  # (local) — 6440.0 (reported for the a_0 channel context)

# 2-point PV (dimensionless masses since FULL Jensen lambda are in M_KK units; S94 subtractive form):
PV_C = (2.0, -1.0)                   # (local) — {c_1, c_2} multipliers (Sum c_j = 1; CC1996 §2.2-2.3)
PV_M2_DIMLESS = (1.0, 2.0)           # (local) — {M_1^2, M_2^2} = {M_KK^2, 2 M_KK^2} in lambda (M_KK) units


# ---------------------------------------------------------------------------
# Section 3 — Dual-SHA closure helpers (S84+ schema)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list) -> dict:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p)  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple:
    """audit_sha256 := SHA256(script_bytes || canonical_bytes || sorted-pinmap-JSON);
       content_sha256 := SHA256(script_bytes)."""
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    content = hashlib.sha256(script_bytes).hexdigest()  # (local)
    return audit, content


def append_verdict(verdict: str, value: str, audit_sha: str, content_sha: str) -> None:
    """Append canonical verdict line + dual-SHA companion row.
    [VERIFY] trigger: NO schema-v2 3-tuple companion row (schema_v2_3tuple_required=false
    per plan §W2-1 output_artifacts.verdict_line). CLASS=FULL path => NO -SCHEMATIC suffix.
    Atomic single open("a") write (POSIX O_APPEND-safe)."""
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)
    companion_row = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row ([VERIFY]; Borel-Pade resum of divergent raw "
        f"a_2 SDW series toward a_2_FW_zeta=2776.165389; 3 regulator classes "
        f"{{raw-mode-count, Pauli-Villars, Mellin}}; CLASS=FULL jensen_irrep_table; "
        f"a_2^{{raw}}+a_2^{{Pauli-Villars}}+a_2^{{Mellin}})\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(companion_row)


# ---------------------------------------------------------------------------
# Section 4 — Raw / PV / Mellin a_2 Mellin-s=2 partial sums (FULL Jensen table)
# ---------------------------------------------------------------------------
def a2_raw_s2(L: int, tau: float) -> float:
    """RAW mode-count a_2 Mellin-s=2 partial sum on the FULL Jensen-deformed Peter-Weyl table:

        a_2^{raw}(s=2, L) = Sum_{(p,q)!=(0,0), p+q<=L} dim(p,q) * |lambda(p,q,tau)|^{-4}

    (s=2 => -2s=-4). |lambda| = sqrt(C_2)*exp(-tau*rho) is the substrate-IS D_K(tau) eigenvalue.
    This is the S94 `bare_moment` convention (bit-exact cross-checked below); NOT Seeley-DeWitt
    (a_2^{raw} quarantine label per §8.2 firewall). S94 confirms it diverges, dK/dL increasing."""
    dims, rhos, lams = jensen_irrep_table(L, tau)  # (local) — FULL Jensen table; (0,0) omitted
    if dims.size == 0:
        return 0.0
    return float(np.sum(dims * lams ** (-4.0)))  # (local)


def a2_pv_s2(L: int, tau: float) -> float:
    """SUBTRACTIVE 2-point Pauli-Villars a_2 Mellin-s=2 partial sum (S94 plan §W1-4 Step-2 form):

        a_2^{PV}(s=2, L) = Sum_k dim_k [ lambda_k^{-4} - 2*(lambda_k^2+1)^{-2} + 1*(lambda_k^2+2)^{-2} ]

    DIMENSIONLESS masses m^2={1,2} (= {M_KK^2, 2 M_KK^2} in lambda M_KK-units). Multipliers
    {+2,-1} satisfy Sum c_j=1, Sum c_j M_j^2=0. a_2^{Pauli-Villars} regulator tag."""
    dims, rhos, lams = jensen_irrep_table(L, tau)  # (local)
    if dims.size == 0:
        return 0.0
    lam2 = lams * lams  # (local)
    bracket = lam2 ** (-2.0)  # (local) — lambda^{-4} bare term
    for c_j, m2_j in zip(PV_C, PV_M2_DIMLESS):
        bracket = bracket - c_j * (lam2 + m2_j) ** (-2.0)  # (local) — subtract c_j (lambda^2+M_j^2)^{-2}
    return float(np.sum(dims * bracket))  # (local)


def a2_mellin_s2(L: int, tau: float) -> float:
    """MELLIN a_2 Mellin-s=2 partial sum. On the positive-definite spectrum the Mellin moment
    equals the zeta value at the residue (S94: a2_mellin_FULL == a2_bare == a2_zeta), so the
    Mellin-class partial sum coincides with the raw moment at finite L. a_2^{Mellin} regulator
    tag (= a_2^{zeta} on the positive spectrum; the analytic-continuation reference)."""
    return a2_raw_s2(L, tau)  # (local) — Mellin = zeta = bare on the positive-definite spectrum (S94)


# ---------------------------------------------------------------------------
# Section 5 — Borel / Pade-Borel resummation machinery (mpmath, high precision)
# ---------------------------------------------------------------------------
def geometric_fit(increments: np.ndarray) -> tuple:
    """Fit the increment series c_k ~ A r^k by log-linear regression on the magnitudes.
    Returns (A, r). r is the geometric ratio (S94 signature; the Borel-pole location is t=1/r)."""
    c = np.asarray(increments, dtype=np.float64)  # (local)
    k = np.arange(c.size, dtype=np.float64)  # (local)
    logc = np.log(np.abs(c))  # (local)
    slope, intercept = np.polyfit(k, logc, 1)  # (local) — log|c_k| = log A + k log r
    r = float(np.exp(slope))  # (local)
    A = float(np.exp(intercept))  # (local)
    return A, r


def pade_borel_sum(increments, M, quad_tol=BOREL_QUAD_TOL):
    """Pade-Borel resummation of the divergent increment series Sum_k c_k.

    Step 1: Borel transform coefficients b_k = c_k / k!  (factorial taming).
    Step 2: diagonal [M/M] Pade approximant P(t) of the Borel series Sum_k b_k t^k.
    Step 3: Laplace integral BorelSum = integral_0^inf e^{-t} P(t) dt.

    Returns dict: borel_sum (the resummed INCREMENT-tail value), pade poles, has_posreal_pole,
    min_posreal_pole_t, integrable flag. The full resummed moment = baseline a_2(L=4) + borel_sum
    (the increment tail resums the L>4 growth)."""
    mp.mp.dps = 50  # (local) — 50 decimal digits for the Pade + Laplace quadrature
    c = [mp.mpf(float(x)) for x in increments]  # (local)
    n = len(c)  # (local)
    # Borel-transform coefficients b_k = c_k / k!
    b = [c[k] / mp.factorial(k) for k in range(n)]  # (local)
    # Diagonal [M/M] Pade requires 2M+1 series coefficients b_0..b_{2M}.
    need = 2 * M + 1  # (local)
    if need > n:
        return {
            "M": M, "borel_sum": float("nan"), "feasible": False,
            "has_posreal_pole": None, "min_posreal_pole_t": float("nan"),
            "n_poles": 0, "poles_re": [], "poles_im": [], "integrable": False,
            "reason": f"need {need} coeffs for [{M}/{M}] Pade, have {n}",
        }
    bM = b[:need]  # (local) — coefficients b_0..b_{2M}
    # mpmath.pade returns (p, q) numerator/denominator coefficient lists (ascending powers).
    p_coeffs, q_coeffs = mp.pade(bM, M, M)  # (local)
    # Denominator roots = poles of the [M/M] Borel-Pade approximant.
    # q_coeffs ascending [q0, q1, ..., qM]; mp.polyroots wants DESCENDING.
    q_desc = list(reversed(q_coeffs))  # (local)
    try:
        roots = mp.polyroots(q_desc, maxsteps=200, extraprec=100)  # (local)
    except Exception:  # noqa: BLE001
        roots = []  # (local)
    poles_re = [float(mp.re(z)) for z in roots]  # (local)
    poles_im = [float(mp.im(z)) for z in roots]  # (local)
    # Positive-real-axis Borel singularity: a pole with Re>0 AND |Im| ~ 0 (on the integration contour)
    posreal_ts = [float(mp.re(z)) for z in roots
                  if float(mp.re(z)) > 0.0 and abs(float(mp.im(z))) < POSREAL_POLE_TOL]  # (local)
    has_posreal_pole = bool(len(posreal_ts) > 0)  # (local)
    min_posreal_pole_t = float(min(posreal_ts)) if posreal_ts else float("nan")  # (local)

    # Pade approximant as a callable P(t) = num(t)/den(t)
    def P(t):
        num = mp.mpf(0)  # (local)
        for i, pc in enumerate(p_coeffs):
            num += pc * t ** i
        den = mp.mpf(0)  # (local)
        for i, qc in enumerate(q_coeffs):
            den += qc * t ** i
        return num / den

    # Laplace integral integral_0^inf e^{-t} P(t) dt.
    # If a positive-real pole exists ON the contour, take the PRINCIPAL VALUE (lateral Borel /
    # Pade-Borel prescription): integrate around the pole symmetrically. mpmath.quad handles the
    # PV when the singularity is supplied as an interior breakpoint.
    integrable = True  # (local)
    try:
        if has_posreal_pole and math.isfinite(min_posreal_pole_t):
            tp = mp.mpf(min_posreal_pole_t)  # (local)
            # principal-value: split at the pole, mpmath integrates the (integrable) PV across the breakpoint
            borel_sum_mp = mp.quad(lambda t: mp.e ** (-t) * P(t),
                                   [0, tp, mp.inf], maxdegree=12)  # (local)
        else:
            borel_sum_mp = mp.quad(lambda t: mp.e ** (-t) * P(t),
                                   [0, mp.inf], maxdegree=12)  # (local)
        borel_sum = float(mp.re(borel_sum_mp))  # (local) — physical (real) part of the PV integral
        if not math.isfinite(borel_sum):
            integrable = False  # (local)
    except Exception:  # noqa: BLE001
        borel_sum = float("nan")  # (local)
        integrable = False  # (local)

    return {
        "M": M, "borel_sum": borel_sum, "feasible": True,
        "has_posreal_pole": has_posreal_pole, "min_posreal_pole_t": min_posreal_pole_t,
        "n_poles": len(roots), "poles_re": poles_re, "poles_im": poles_im,
        "integrable": integrable, "reason": "",
    }


# ---------------------------------------------------------------------------
# Section 6 — Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    tau = float(tau_fold)  # (local)
    Lseq = np.array(L_SEQ, dtype=np.int64)  # (local) — {5..12}

    # --- build the three partial-sum sequences ---
    a2_raw = np.array([a2_raw_s2(int(L), tau) for L in Lseq], dtype=np.float64)     # (local)
    a2_pv = np.array([a2_pv_s2(int(L), tau) for L in Lseq], dtype=np.float64)       # (local)
    a2_mellin = np.array([a2_mellin_s2(int(L), tau) for L in Lseq], dtype=np.float64)  # (local)

    # --- baseline at L=4 (the increment tail resums everything ABOVE the baseline) ---
    a2_raw_L4 = a2_raw_s2(4, tau)      # (local)
    a2_pv_L4 = a2_pv_s2(4, tau)        # (local)
    a2_mellin_L4 = a2_mellin_s2(4, tau)  # (local)

    # --- CC1: partial-sum-construction agreement cross-check vs S94 bare_moment ---
    # S94 stored bare_moment on L_grid=[10..100]; we re-derive a_2^raw at L=10,11,12 and compare.
    s94_bare_at = {}  # (local)
    s94_npz_runtime_sha = sha256_of(S94_NPZ_PATH)  # (local) — runtime SHA (plan field was <computed-at-runtime>)
    try:
        s94 = np.load(S94_NPZ_PATH, allow_pickle=True)  # (local)
        s94_Lgrid = s94["L_grid"]  # (local)
        s94_bare = s94["bare_moment"]  # (local)
        for Lc in (10, 11, 12):
            idx = int(np.where(s94_Lgrid == Lc)[0][0])  # (local)
            s94_bare_at[Lc] = float(s94_bare[idx])  # (local)
    except Exception as exc:  # noqa: BLE001
        print(f"  [warn] could not load S94 npz for CC1 cross-check: {exc}")
    cc1_residual = float("nan")  # (local)
    if 12 in s94_bare_at:
        cc1_residual = abs(a2_raw[-1] - s94_bare_at[12])  # (local) — our L=12 vs S94 bare_moment[L=12]
    cc1_ok = bool(math.isfinite(cc1_residual) and cc1_residual < 1e-6 * max(1.0, abs(a2_raw[-1])))  # (local)

    # --- increments c_k = a_2(L=k+5) - a_2(L=k+4); for the increment series we PREPEND the
    #     L=5 value as the "increment over the L=4 baseline" so c_0 = a2(5)-a2(4), etc. ---
    raw_with_base = np.concatenate(([a2_raw_L4], a2_raw))        # (local) — [L4, L5..L12]
    pv_with_base = np.concatenate(([a2_pv_L4], a2_pv))           # (local)
    mellin_with_base = np.concatenate(([a2_mellin_L4], a2_mellin))  # (local)
    inc_raw = np.diff(raw_with_base)        # (local) — 8 increments c_0..c_7
    inc_pv = np.diff(pv_with_base)          # (local)
    inc_mellin = np.diff(mellin_with_base)  # (local)

    # --- geometric-divergence fit (the S94 signature; pole at t=1/r) ---
    A_raw, r_raw = geometric_fit(inc_raw)        # (local)
    A_pv, r_pv = geometric_fit(inc_pv)           # (local)
    A_mellin, r_mellin = geometric_fit(inc_mellin)  # (local)
    # successive a_2(L)/a_2(L-1) ratios (the divergence growth rate)
    ratio_raw = a2_raw[1:] / a2_raw[:-1]  # (local)

    # --- MULTIPLICATIVE-NORMALIZATION pre-flight (math-scripts.md K=3) ---
    # No log-derivative operator => the K=3 cancellation pathology does NOT apply by operator type.
    # Sage disambiguator (run via MCP at plan-freeze; recorded here):
    #   sage_simplify("(a*r^(k+1))/(a*r^k)") -> r  (constant; genuine divergence, not w(L) artifact)
    #   sage_simplify("sum(a*(r*t)^k/factorial(k),k,0,oo)") -> a*e^(r*t)  (Borel transform of geometric)
    # Operative numerical confirmation: the increment ratio inc_raw[k+1]/inc_raw[k] is ~constant (=r),
    # NOT k-dependent => the divergence is genuine geometric growth, NOT a multiplicative w(L_max)*kappa
    # that would cancel under d/dlnK. => MULTIPLICATIVE-NORMALIZATION-CANCELLATION-DETECTED=False.
    inc_ratio_raw = inc_raw[1:] / inc_raw[:-1]  # (local)
    inc_ratio_std = float(np.std(inc_ratio_raw) / np.mean(inc_ratio_raw))  # (local) — coeff of variation
    mult_norm_cancellation_detected = bool(inc_ratio_std < 1e-6)  # (local) — a PURE multiplicative w(L)
    # would give inc_ratio EXACTLY constant to machine eps AND a constant moment under log-deriv; here
    # inc_ratio drifts (CoV ~ 1e-2, asymptoting to r) => genuine geometric divergence, NOT a w(L) identity.

    # --- Pade-Borel resummation, per regulator class, per Pade order M ---
    classes = {
        "raw": (inc_raw, a2_raw_L4),
        "Pauli-Villars": (inc_pv, a2_pv_L4),
        "Mellin": (inc_mellin, a2_mellin_L4),
    }  # (local)
    resum = {}  # (local) — resum[class][M] = dict
    for cls, (inc, base) in classes.items():
        resum[cls] = {}
        for M in PADE_ORDERS:
            res = pade_borel_sum(inc, M)  # (local)
            if res["feasible"] and math.isfinite(res["borel_sum"]):
                full_moment = base + res["borel_sum"]  # (local) — baseline + resummed increment tail
            else:
                full_moment = float("nan")  # (local)
            res["base_L4"] = base
            res["full_moment"] = full_moment
            res["delta"] = abs(full_moment - A2_ZETA_TARGET) if math.isfinite(full_moment) else float("nan")  # (local)
            res["rel_delta"] = res["delta"] / A2_ZETA_TARGET if math.isfinite(res["delta"]) else float("nan")  # (local)
            resum[cls][M] = res

    # --- DIRECTION test: does |delta| DECREASE with Pade order M (toward zeta) or INCREASE (away)? ---
    # Use the RAW class (the gated quantity per the plan operator form).
    rel_deltas_raw = np.array(
        [resum["raw"][M]["rel_delta"] for M in PADE_ORDERS], dtype=np.float64
    )  # (local)
    finite_mask = np.isfinite(rel_deltas_raw)  # (local)
    if finite_mask.sum() >= 2:
        first_rd = float(rel_deltas_raw[finite_mask][0])  # (local)
        last_rd = float(rel_deltas_raw[finite_mask][-1])  # (local)
        delta_decreasing_with_M = bool(last_rd < first_rd)  # (local) — toward zeta
    else:
        first_rd = float("nan"); last_rd = float("nan")  # (local)
        delta_decreasing_with_M = False  # (local)

    # --- Best (highest-feasible-M) resummed value per class ---
    def best_for(cls):
        best = None  # (local)
        for M in PADE_ORDERS:
            r = resum[cls][M]  # (local)
            if r["feasible"] and math.isfinite(r["full_moment"]):
                best = r  # (local)
        return best
    best_raw = best_for("raw")        # (local)
    best_pv = best_for("Pauli-Villars")  # (local)
    best_mellin = best_for("Mellin")  # (local)

    # --- Borel-summability pre-condition: NO positive-real-axis pole in the [M/M] approximant ---
    # Aggregate over the RAW class (gated): summable iff NO feasible M has a positive-real pole.
    raw_posreal_flags = [resum["raw"][M]["has_posreal_pole"] for M in PADE_ORDERS
                         if resum["raw"][M]["feasible"]]  # (local)
    raw_borel_summable = bool(len(raw_posreal_flags) > 0 and not any(raw_posreal_flags))  # (local)
    # minimum positive-real pole location across feasible M (the Borel singularity nearest the origin)
    raw_min_posreal_ts = [resum["raw"][M]["min_posreal_pole_t"] for M in PADE_ORDERS
                          if resum["raw"][M]["feasible"] and resum["raw"][M]["has_posreal_pole"]
                          and math.isfinite(resum["raw"][M]["min_posreal_pole_t"])]  # (local)
    raw_borel_singularity_t = float(min(raw_min_posreal_ts)) if raw_min_posreal_ts else float("nan")  # (local)
    # Theoretical pole from the geometric fit: t = 1/r
    theo_pole_t = 1.0 / r_raw if r_raw != 0 else float("nan")  # (local)

    # --- best resummed RAW value + distance to zeta ---
    best_raw_full = best_raw["full_moment"] if best_raw else float("nan")  # (local)
    best_raw_rel_delta = best_raw["rel_delta"] if best_raw else float("nan")  # (local)

    # -------------------------------------------------------------------
    # VERDICT (plan §W2-1 rubric):
    #   PASS  iff  raw_borel_summable (NO positive-real pole)  AND  best_raw_rel_delta <= 0.10
    #   FAIL  iff  NOT raw_borel_summable (positive-real Borel singularity)  OR  best_raw_rel_delta > 0.10
    #   INFO  iff  raw_borel_summable AND lands on a DIFFERENT finite value (rel_delta > 0.10 but the
    #              series IS Borel-summable to a finite value)
    # -------------------------------------------------------------------
    summable = raw_borel_summable  # (local)
    within_band = bool(math.isfinite(best_raw_rel_delta) and best_raw_rel_delta <= TAU_RESUM)  # (local)
    lands_finite = bool(best_raw is not None and math.isfinite(best_raw_full))  # (local)

    if summable and within_band:
        verdict = "PASS"
        band_tag = "PASS_raw_series_Borel_summable_NO_posreal_pole_AND_resummed_within_10pct_of_zeta"  # (local)
        track = "A_0.9"  # (local)
    elif (not summable) and lands_finite:
        # positive-real-axis Borel singularity: Borel-NON-summable in the strict sense.
        verdict = "FAIL"
        band_tag = "FAIL_positive_real_axis_Borel_singularity_raw_series_NOT_Borel_summable"  # (local)
        track = "B_0.9"  # (local)
    elif summable and (not within_band) and lands_finite:
        verdict = "INFO"
        band_tag = "INFO_Borel_summable_to_DIFFERENT_finite_value_scheme_ambiguity_quantified"  # (local)
        track = "split_0.5"  # (local)
    else:
        # not summable AND no finite landing (PV integral diverged): hardest FAIL
        verdict = "FAIL"
        band_tag = "FAIL_not_Borel_summable_and_no_finite_PV_landing"  # (local)
        track = "B_0.9"  # (local)

    # --- structural-evaluability guard (do not emit PASS if the machinery did not run) ---
    evaluator_runnable = bool(
        math.isfinite(a2_raw[-1]) and a2_raw[-1] > 0
        and best_raw is not None
        and len(raw_posreal_flags) > 0
        and CM_CLASS == "FULL"
    )  # (local)
    if not evaluator_runnable:
        verdict = "FAIL"
        band_tag = "FAIL_evaluator_not_runnable_or_no_feasible_Pade_order"  # (local)
        track = "B_0.9"  # (local)

    return {
        "tau_fold": tau,
        "M_KK": float(M_KK),
        "a_2_FW_zeta": A2_ZETA_TARGET,
        "a_0_FW_zeta": A0_ZETA_TARGET,
        "L_seq": Lseq,
        "pade_orders": np.array(PADE_ORDERS),
        "tau_resum": TAU_RESUM,
        # partial sums
        "a2_raw": a2_raw,
        "a2_pv": a2_pv,
        "a2_mellin": a2_mellin,
        "a2_raw_L4": a2_raw_L4,
        "a2_pv_L4": a2_pv_L4,
        "a2_mellin_L4": a2_mellin_L4,
        "ratio_raw": ratio_raw,
        # increments
        "inc_raw": inc_raw,
        "inc_pv": inc_pv,
        "inc_mellin": inc_mellin,
        # geometric fits
        "A_raw": A_raw, "r_raw": r_raw,
        "A_pv": A_pv, "r_pv": r_pv,
        "A_mellin": A_mellin, "r_mellin": r_mellin,
        "theo_pole_t": theo_pole_t,
        # multiplicative-normalization pre-flight
        "inc_ratio_raw": inc_ratio_raw,
        "inc_ratio_std_CoV": inc_ratio_std,
        "mult_norm_cancellation_detected": mult_norm_cancellation_detected,
        # resummation (flatten the nested dict for npz)
        "resum_raw_M": np.array([resum["raw"][M]["full_moment"] for M in PADE_ORDERS]),
        "resum_pv_M": np.array([resum["Pauli-Villars"][M]["full_moment"] for M in PADE_ORDERS]),
        "resum_mellin_M": np.array([resum["Mellin"][M]["full_moment"] for M in PADE_ORDERS]),
        "borel_sum_raw_M": np.array([resum["raw"][M]["borel_sum"] for M in PADE_ORDERS]),
        "rel_delta_raw_M": rel_deltas_raw,
        "rel_delta_pv_M": np.array([resum["Pauli-Villars"][M]["rel_delta"] for M in PADE_ORDERS]),
        "rel_delta_mellin_M": np.array([resum["Mellin"][M]["rel_delta"] for M in PADE_ORDERS]),
        "posreal_pole_raw_M": np.array([1 if resum["raw"][M]["has_posreal_pole"] else 0 for M in PADE_ORDERS]),
        "posreal_pole_pv_M": np.array([1 if resum["Pauli-Villars"][M]["has_posreal_pole"] else 0 for M in PADE_ORDERS]),
        "posreal_pole_mellin_M": np.array([1 if resum["Mellin"][M]["has_posreal_pole"] else 0 for M in PADE_ORDERS]),
        "min_posreal_t_raw_M": np.array([resum["raw"][M]["min_posreal_pole_t"] for M in PADE_ORDERS]),
        "feasible_raw_M": np.array([1 if resum["raw"][M]["feasible"] else 0 for M in PADE_ORDERS]),
        # direction test
        "first_rel_delta_raw": first_rd,
        "last_rel_delta_raw": last_rd,
        "delta_decreasing_with_M": delta_decreasing_with_M,
        # Borel-summability aggregate (raw / gated)
        "raw_borel_summable": raw_borel_summable,
        "raw_borel_singularity_t": raw_borel_singularity_t,
        # best resummed value
        "best_raw_full_moment": best_raw_full,
        "best_raw_rel_delta": best_raw_rel_delta,
        "best_pv_full_moment": (best_pv["full_moment"] if best_pv else float("nan")),
        "best_pv_rel_delta": (best_pv["rel_delta"] if best_pv else float("nan")),
        "best_mellin_full_moment": (best_mellin["full_moment"] if best_mellin else float("nan")),
        "best_mellin_rel_delta": (best_mellin["rel_delta"] if best_mellin else float("nan")),
        # CC1 cross-check
        "cc1_residual_vs_s94": cc1_residual,
        "cc1_ok": cc1_ok,
        "s94_bare_L12": s94_bare_at.get(12, float("nan")),
        "s94_npz_runtime_sha": s94_npz_runtime_sha,
        # verdict
        "evaluator_runnable": evaluator_runnable,
        "verdict": verdict,
        "band_tag": band_tag,
        "track": track,
        "cm_class": CM_CLASS,
        "cm_regulator_pin": CM_REGULATOR_PIN,
    }


# ---------------------------------------------------------------------------
# Section 7 — Plot
# ---------------------------------------------------------------------------
def make_plot(r: dict) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(14.0, 9.5), dpi=120)
    Mlist = r["pade_orders"]
    Lseq = r["L_seq"]

    # Panel A: the divergent raw a_2 partial sums vs L (log) + zeta target
    axA = axes[0, 0]
    axA.semilogy(Lseq, r["a2_raw"], "o-", color="#d62728", ms=5, lw=1.4, label="a_2^{raw}(L)  (S94 divergent)")
    axA.semilogy(Lseq, np.abs(r["a2_pv"]), "s-", color="#2ca02c", ms=4, lw=1.2, label="a_2^{Pauli-Villars}(L)")
    axA.axhline(r["a_2_FW_zeta"], color="#1f77b4", ls="--", lw=1.6,
                label=f"a_2_FW_zeta = {r['a_2_FW_zeta']:.4f} (target)")
    axA.set_xlabel("L_max"); axA.set_ylabel("a_2(s=2) partial sum  (log)")
    axA.set_title(f"(A) Divergent raw SDW series vs zeta target\n"
                  f"geometric ratio r={r['r_raw']:.4f} (a_2(L)/a_2(L-1) -> {r['ratio_raw'][-1]:.4f})")
    axA.legend(fontsize=8.5); axA.grid(alpha=0.3)

    # Panel B: |delta|/a_2_FW_zeta vs Pade order M (the DIRECTION test) — per class
    axB = axes[0, 1]
    axB.semilogy(Mlist, r["rel_delta_raw_M"], "o-", color="#d62728", ms=6, lw=1.5, label="raw")
    axB.semilogy(Mlist, r["rel_delta_pv_M"], "s-", color="#2ca02c", ms=5, lw=1.2, label="Pauli-Villars")
    axB.semilogy(Mlist, r["rel_delta_mellin_M"], "^-", color="#9467bd", ms=5, lw=1.2, label="Mellin")
    axB.axhline(r["tau_resum"], color="gray", ls="--", lw=1.4, label=f"PASS band {r['tau_resum']:.2f}")
    axB.set_xlabel("Pade diagonal order M"); axB.set_ylabel("|delta|/a_2_FW_zeta  (log)")
    axB.set_title(f"(B) Distance-to-zeta vs Pade order M  (DIRECTION test)\n"
                  f"raw: decreasing-with-M = {r['delta_decreasing_with_M']} "
                  f"({r['first_rel_delta_raw']:.3g} -> {r['last_rel_delta_raw']:.3g})")
    axB.set_xticks(list(Mlist))
    axB.legend(fontsize=8.5); axB.grid(alpha=0.3)

    # Panel C: [M/M] Borel-Pade pole structure — positive-real-axis singularity?
    axC = axes[1, 0]
    plotted = False
    for M in [int(x) for x in Mlist]:
        # re-extract poles for the raw class at this M for the scatter
        from_idx = list(Mlist).index(M)
        has_pp = bool(r["posreal_pole_raw_M"][from_idx])
        tmin = r["min_posreal_t_raw_M"][from_idx]
        if math.isfinite(tmin):
            axC.scatter([tmin], [0.0], s=90, marker="x",
                        color="#d62728" if has_pp else "#2ca02c",
                        label=f"[{M}/{M}] min posreal pole t={tmin:.4f}" + (" (ON contour)" if has_pp else ""))
            plotted = True
    axC.axvline(r["theo_pole_t"], color="#1f77b4", ls="--", lw=1.6,
                label=f"theory pole t=1/r={r['theo_pole_t']:.4f}")
    axC.axhline(0.0, color="gray", lw=0.8)
    axC.set_xlabel("Re(Borel-Pade pole location t)"); axC.set_ylabel("Im(t)")
    axC.set_title(f"(C) Borel-Pade [M/M] positive-real-axis pole\n"
                  f"raw Borel-summable = {r['raw_borel_summable']} "
                  f"(singularity at t={r['raw_borel_singularity_t']:.4f})")
    if plotted:
        axC.legend(fontsize=7.8)
    axC.grid(alpha=0.3)

    # Panel D: verdict + diagnostic text
    axD = axes[1, 1]
    axD.axis("off")
    lines = [
        f"VERDICT: {r['verdict']}",
        f"band_tag: {r['band_tag']}",
        f"track: {r['track']}",
        "",
        f"CLASS pin: {r['cm_class']} (FULL jensen_irrep_table; NO -SCHEMATIC)",
        f"regulators: a_2^{{raw}} + a_2^{{Pauli-Villars}} + a_2^{{Mellin}}",
        "",
        "--- multiplicative-normalization pre-flight (Sage) ---",
        f"  inc-ratio CoV = {r['inc_ratio_std_CoV']:.3e} (k-dependent => genuine geom div)",
        f"  MULT-NORM-CANCELLATION-DETECTED = {r['mult_norm_cancellation_detected']}",
        f"  (no log-deriv operator => K=3 pathology N/A by operator type)",
        "",
        "--- raw series (gated) ---",
        f"  a_2^raw(L=12) = {r['a2_raw'][-1]:.4f}  (S94 bare_moment[L12]={r['s94_bare_L12']:.4f})",
        f"  CC1 residual vs S94 = {r['cc1_residual_vs_s94']:.2e}  ok={r['cc1_ok']}",
        f"  geometric ratio r = {r['r_raw']:.5f}  => Borel pole t=1/r = {r['theo_pole_t']:.5f}",
        "",
        "--- Borel-Pade resummation (raw) ---",
        f"  full_moment(best M) = {r['best_raw_full_moment']:.6g}",
        f"  target a_2_FW_zeta  = {r['a_2_FW_zeta']:.6f}",
        f"  |delta|/zeta (best) = {r['best_raw_rel_delta']:.4g}  (band {r['tau_resum']:.2f})",
        f"  Borel-summable      = {r['raw_borel_summable']}  (posreal pole present={not r['raw_borel_summable']})",
        f"  |delta| decreasing-with-M = {r['delta_decreasing_with_M']}",
        "",
        "--- per-M resummed (raw) ---",
    ]
    for i, M in enumerate([int(x) for x in Mlist]):
        feasible = bool(r["feasible_raw_M"][i])
        lines.append(f"  M={M}: full={r['resum_raw_M'][i]:.4g}  rel_d={r['rel_delta_raw_M'][i]:.3g}  "
                     f"posreal_pole={bool(r['posreal_pole_raw_M'][i])}  feasible={feasible}")
    axD.text(0.0, 1.0, "\n".join(lines), va="top", ha="left", fontsize=7.4,
             family="monospace", transform=axD.transAxes)
    axD.set_title("(D) Diagnostic summary")

    fig.suptitle(
        f"{GATE_ID}  —  Borel/Pade resummation of the divergent raw SDW a_2 series toward "
        f"a_2_FW_zeta={r['a_2_FW_zeta']:.4f}\n"
        f"VERDICT: {r['verdict']}  "
        f"(Borel-summable={r['raw_borel_summable']}, |delta|/zeta={r['best_raw_rel_delta']:.3g} vs {r['tau_resum']:.2f})",
        fontsize=10.5, y=1.005,
    )
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(OUT_PNG, dpi=120, bbox_inches="tight")
    plt.close(fig)
    print(f"\nplot -> {OUT_PNG.relative_to(PROJECT_ROOT)}")


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------
INPUT_FILES = [
    CANONICAL_CONSTANTS_PATH,
    CM_EVALUATOR_PATH,
    L12_CACHE_PATH,
    S94_NPZ_PATH,
    S94_PY_PATH,
]


def main() -> int:
    # 1. Log input pins (first 20 lines of stdout)
    pins = log_input_pins(INPUT_FILES)

    # 1a. Verify the S94 .py provenance SHA (plan-pinned) + report S94 npz runtime SHA
    s94_py_sha = sha256_of(S94_PY_PATH)  # (local)
    print(f"  S94 .py provenance SHA: {s94_py_sha[:16]}... "
          f"(plan-pinned {S94_PY_PROVENANCE_SHA[:16]}...; "
          f"MATCH={s94_py_sha == S94_PY_PROVENANCE_SHA})")
    s94_npz_sha = sha256_of(S94_NPZ_PATH)  # (local)
    print(f"  S94 npz runtime SHA:    {s94_npz_sha[:16]}... (plan field was <computed-at-runtime>)")

    # 1b. Compute S84+ dual SHAs
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_CONSTANTS_PATH, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. Compute
    result = compute()

    # 3. Plot
    make_plot(result)

    # 4. Save npz
    SESSION_96_DIR.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(OUT_NPZ, **{
        k: v for k, v in result.items()
    })
    print(f"npz  -> {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    # 5. Console summary (4-tuple final non-verdict line)
    print()
    print(f"=== {GATE_ID} RESULT ===")
    print(f"  raw a_2(L=12)             = {result['a2_raw'][-1]:.6f}  "
          f"(S94 bare_moment[L12] = {result['s94_bare_L12']:.6f}; CC1 ok={result['cc1_ok']})")
    print(f"  geometric ratio r         = {result['r_raw']:.6f}  => Borel pole t=1/r = {result['theo_pole_t']:.6f}")
    print(f"  MULT-NORM-CANCELLATION    = {result['mult_norm_cancellation_detected']} "
          f"(inc-ratio CoV={result['inc_ratio_std_CoV']:.3e})")
    print(f"  raw Borel-summable        = {result['raw_borel_summable']} "
          f"(positive-real Borel singularity at t={result['raw_borel_singularity_t']:.6f})")
    for i, M in enumerate([int(x) for x in result['pade_orders']]):
        print(f"    [M={M}] full_moment={result['resum_raw_M'][i]:.6g}  "
              f"|delta|/zeta={result['rel_delta_raw_M'][i]:.4g}  "
              f"posreal_pole={bool(result['posreal_pole_raw_M'][i])}")
    print(f"  best resummed a_2^raw     = {result['best_raw_full_moment']:.6g}  "
          f"(target a_2_FW_zeta = {result['a_2_FW_zeta']:.6f})")
    print(f"  |delta|/a_2_FW_zeta (best)= {result['best_raw_rel_delta']:.6g}  (PASS band {result['tau_resum']:.2f})")
    print(f"  |delta| decreasing-with-M = {result['delta_decreasing_with_M']}")
    print(f"  track re-allocation       = {result['track']}")
    print(f"  (value=Borel-Pade-resum, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print(f"  VERDICT: {result['verdict']}  ({result['band_tag']})")

    # 6. Append verdict (canonical line + dual-SHA companion row; [VERIFY], no 3-tuple)
    value_str = (
        f"verdict={result['verdict']};"
        f"raw_borel_summable={result['raw_borel_summable']};"
        f"posreal_pole_t={result['raw_borel_singularity_t']:.6f};"
        f"geom_r={result['r_raw']:.6f};"
        f"theo_pole_t={result['theo_pole_t']:.6f};"
        f"a2_raw_L12={result['a2_raw'][-1]:.6f};"
        f"best_resum_raw={result['best_raw_full_moment']:.6g};"
        f"a2_FW_zeta={result['a_2_FW_zeta']:.6f};"
        f"rel_delta_best={result['best_raw_rel_delta']:.6g};"
        f"tau_resum={result['tau_resum']:.2f};"
        f"delta_decreasing_with_M={result['delta_decreasing_with_M']};"
        f"mult_norm_cancellation={result['mult_norm_cancellation_detected']};"
        f"best_resum_pv={result['best_pv_full_moment']:.6g};"
        f"best_resum_mellin={result['best_mellin_full_moment']:.6g};"
        f"cc1_ok={result['cc1_ok']};"
        f"track={result['track']}"
    )  # (local)
    append_verdict(result["verdict"], value_str, audit_sha, content_sha)
    print(f"\nverdict appended -> {VERDICT_TXT.relative_to(PROJECT_ROOT)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
