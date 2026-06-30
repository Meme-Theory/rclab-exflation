#!/usr/bin/env python3
"""
S102 W3-14 — S102-TRD2-MONOTONICITY-ANALYTIC
============================================

Gate: S102-TRD2-MONOTONICITY-ANALYTIC ([SIGN])

TIMEBOXED closed-form proof attempt (Stratum-1 checklist box 4): promote the
E7 Structural Monotonicity Theorem (dS_SA/dtau > 0, equivalently <lambda^2>(tau)
strictly increasing) from 9,600-numerical-check status to an analytic Theorem
via the Weitzenbock/Lichnerowicz decomposition D_K^2 = -nabla^2 + R_K/4 and the
explicit Jensen metric g_tau.

Pre-registered threshold (gate-block operator field):
  dS_SA/dtau (closed form) > 0 for all tau in [0, tau_NEC=1.383)
  AND |dS_SA/dtau|_fold,analytic - 58672.8| / 58672.8 < tol_xcheck=1e-3.
  PASS = full closed-form positivity AND magnitude xcheck;
  FAIL = per-sector dC/dtau step does not close in the timebox;
  INFO = positivity proven on sub-domain OR modulo a stated auxiliary issue
         (PLAN INFO_meaning).

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/dirac_spectrum.py  (per-sector Casimir/frame structure;
    the same D_K construction the S42 anchor and item-11 keystone validate)
  - canonical_constants.py (feeds audit_sha256; supplies dS_fold, tau_NEC, tau_fold)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<analytic positivity verdict + sign 3-tuple>,
   scheme=WEITZENBOCK-LICHNEROWICZ,
   convention=SYMBOLIC-CLOSED-FORM-SAGE-QQ,
   L_max=general-(p,q)-symbolic / L_max_xcheck=10)

Classification: GEOMETRIC.

METHODOLOGY
-----------
The physical second spectral moment per Peter-Weyl sector (p,q) is

    M2(p,q;tau) = sum_k mu_k^2 = -Tr D_pi^2          [D_pi anti-Hermitian: lambda = i*mu]

Direct trace of the matrix Dirac operator (dirac_operator_on_irrep) gives an
EXACT closed form (cross-term Tr(rho(X_b))*Tr(gamma_a Omega) = 0 by tracelessness
of su(3) generators):

    Tr D_pi^2 = 16 * Casimir_g(p,q;tau) + d(p,q) * Tr(Omega^2)(tau)

with the two closed forms (machine-eps verified, Sage-certified):

  (1) Metric-contracted Casimir (the frame-deformed C(p,q;tau)):
        Casimir_g(p,q;tau) = -(C2(p,q)*d(p,q)/24) * (3 e^{2tau} + 4 e^{-tau} + e^{-2tau})
      via the EQUIPARTITION THEOREM (machine-eps over all p+q<=7):
        the per-block rep traces split as S_su2 : S_c2 : S_u1 = 3 : 4 : 1
        = block dimensions, so the (1/3)(g_s^{-1}) blocks (e^{2tau},e^{-tau},e^{-2tau})
        weight a single Casimir C2*d.

  (2) Spinor curvature offset trace (Weitzenbock/Lichnerowicz endomorphism):
        Tr(Omega^2)(tau) = -5 e^{2tau} - 4 e^{-tau} - 2 e^{-2tau} - (1/2) e^{-4tau} - 1/2

Hence (M2 = -Tr D_pi^2):

    M2(p,q;tau) = (2/3) C2 d (3 e^{2tau}+4 e^{-tau}+e^{-2tau})
                  + d (5 e^{2tau}+4 e^{-tau}+2 e^{-2tau}+(1/2) e^{-4tau}+1/2)

    dM2/dtau = d * [ C2 * gC(tau) + gS(tau) ]
      gC(tau) = 4 e^{2tau} - (8/3) e^{-tau} - (4/3) e^{-2tau}
      gS(tau) = 10 e^{2tau} - 4 e^{-tau} - 4 e^{-2tau} - 2 e^{-4tau}

PROOF OF STRICT POSITIVITY (Sage QQ, exact):
  Let u = e^{tau} >= 1 for tau >= 0. Then
      gC(tau) * e^{2tau} = 4 u^4 - (8/3) u - 4/3 = (u-1)(4 u^3 + 4 u^2 + 4 u + 4/3)
      gS(tau) * e^{4tau} = 10 u^6 - 4 u^3 - 4 u^2 - 2
                         = (u-1)(10 u^5 + 10 u^4 + 10 u^3 + 6 u^2 + 2 u + 2)
  Both cofactors have ALL-POSITIVE rational coefficients => strictly positive for u>0.
  Therefore for u>=1 (tau>=0): gC, gS = (u-1)*(positive) >= 0, ZERO iff u=1 (tau=0),
  STRICTLY > 0 for tau > 0. Since C2 >= 0 (all sectors) and d > 0:
      dM2/dtau = 0 at tau=0,  dM2/dtau > 0 strictly for tau > 0,  ALL (p,q).
  Monotonicity holds TERM-BY-TERM per sector => the Peter-Weyl sum is monotone
  => L-UNIFORM (no truncation dependence). This IS the E7 <lambda^2>(tau) content.

CROSS-CHECK / HONEST SCOPING (the load-bearing distinction):
  The pinned anchor dS_fold = +58672.8 is dS_full/dtau, the |lambda|-SPECTRAL-ACTION
  gradient: S_full = sum_{(p,q)} dim(p,q)^2 * sum_k |lambda_k(tau)|  (f(x)=sqrt(x)).
  This script reproduces it (FD) to confirm the construction is bit-identical to S42.
  The object PROVEN above is the lambda^2-moment (f(x)=x), whose gradient at the
  fold is a DIFFERENT, larger number. Individual |lambda| eigenvalues (11/18/...
  distinct roots per sector) admit NO clean closed form; only the lambda^2 MOMENT
  (a trace) does. So:
    - SIGN  : analytic dM2/dtau > 0 MATCHES anchor sign (both strictly > 0). PASS.
    - MAGNITUDE (literal pre-reg) : |analytic_lambda^2_grad - 58672.8|/58672.8 NOT < 1e-3,
      because the anchor is the |lambda|-action, a DIFFERENT functional. FAIL on the
      literal clause -- NOT redefined to manufacture a PASS.
    - REGIME : valid on the entire physical domain [0, tau_NEC) (in fact all tau>0).
  Composite => INFO (PLAN INFO_meaning): the SIGN -- the literal E7 monotonicity of
  <lambda^2> -- is proven in EXACT closed form (genuine numerical->analytic upgrade);
  the magnitude clause tests a different functional and is flagged, not forced.
  E7's 9,600-numerical status is UNCHANGED; the lambda^2-moment monotonicity is now
  additionally an analytic Theorem. (E7's "ALL monotone f" covers the |lambda|-action
  SIGN as a corollary, but its closed-form MAGNITUDE is not delivered by this method.)

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- 4-tuple printed as the final non-verdict line
- Gate verdict emitted via the `emit_verdict` knowledge-MCP tool (the script PRINTS
  the payload; the agent calls mcp__knowledge__emit_verdict). No open-coded append.

regulator_pin: a_0^{zeta}, a_2^{zeta}, a_4^{zeta} (Gilkey-zeta; S_SA=a_0-a_2+a_4 per E7).
  The monotonicity target is <lambda^2>(tau)/Tr D_K^2(tau), whose tau-derivative sign
  is regulator-robust (E7: ALL monotone f, ALL Lambda). The a_n^{zeta} tag pins the
  SA-moment combination behind the |_fold numerical cross-check.

Author: spectral-geometer (Session 102, Wave 3, item 14; checklist box 4)
Date: 2026-06-09
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
import sys

SHARED_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "_shared"))  # (local)
sys.path.insert(0, SHARED_DIR)

from canonical_constants import *  # noqa: F401,F403
from canonical_constants import dS_fold, tau_NEC, tau_fold

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import dirac_spectrum as DS
from dirac_spectrum import (
    su3_generators,
    compute_structure_constants,
    compute_killing_form,
    jensen_metric,
    orthonormal_frame,
    frame_structure_constants,
    connection_coefficients,
    spinor_connection_offset,
    build_cliff8,
    get_irrep,
    dirac_operator_on_irrep,
)
from numpy.linalg import eigvalsh

# ---------------------------------------------------------------------------
# Section 3 — Gate identity
# ---------------------------------------------------------------------------
SESSION = "S102"                                       # (local)
GATE_ID = "S102-TRD2-MONOTONICITY-ANALYTIC"            # (local)
SCHEME = "WEITZENBOCK-LICHNEROWICZ"                    # (local)
CONVENTION = "SYMBOLIC-CLOSED-FORM-SAGE-QQ"            # (local)
L_MAX = "general-(p,q)-symbolic/xcheck-10"            # (local)
TOL_XCHECK = 1e-3                                      # (local) RATIO tol vs +58672.8 (plan)
MACHINE_EPS_TOL = 1e-10                                # (local) closed-form vs numeric ceiling

INPUT_FILES = [                                        # (local)
    os.path.join(SHARED_DIR, "dirac_spectrum.py"),
    os.path.join(SHARED_DIR, "canonical_constants.py"),
]


# ---------------------------------------------------------------------------
# Section 4 — Dual-SHA helpers (per .claude/templates/script-template.py)
# ---------------------------------------------------------------------------
def log_input_pins(files):
    pins = {}  # (local)
    print("=== INPUT SHA-256 PINS ===")
    for f in files:
        try:
            b = Path(f).read_bytes()  # (local)
            sha = hashlib.sha256(b).hexdigest()  # (local)
        except OSError:
            sha = "MISSING"  # (local)
        rel = os.path.relpath(f, start=os.path.dirname(os.path.dirname(SHARED_DIR)))  # (local)
        pins[rel] = sha
        print(f"  {rel}: {sha[:16]}...")
    return pins


def closure_hash(pins):
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path, canonical_path, pins):
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
    pinmap_json = json.dumps(pins, sort_keys=True, separators=(",", ":")).encode("utf-8")  # (local)
    audit = hashlib.sha256(script_bytes + canonical_bytes + pinmap_json).hexdigest()  # (local)
    content = hashlib.sha256(script_bytes).hexdigest()  # (local)
    return audit, content


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, companion_note="", extra_rows=None):
    payload = {
        "session": 102,
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
# Section 5 — Closed forms (the proof's analytic objects)
# ---------------------------------------------------------------------------
def dim_pq(p, q):
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def C2_pq(p, q):
    return (p ** 2 + q ** 2 + p * q + 3 * p + 3 * q) / 3.0


def casimir_g_closed(p, q, tau):
    """Frame-deformed metric Casimir C(p,q;tau) (closed form)."""
    d = dim_pq(p, q)  # (local)
    C2 = C2_pq(p, q)  # (local)
    return -(C2 * d / 24.0) * (3 * np.exp(2 * tau) + 4 * np.exp(-tau) + np.exp(-2 * tau))


def tr_omega2_closed(tau):
    """Spinor curvature offset trace Tr(Omega^2)(tau) (closed form)."""
    return (-5 * np.exp(2 * tau) - 4 * np.exp(-tau) - 2 * np.exp(-2 * tau)
            - 0.5 * np.exp(-4 * tau) - 0.5)


def M2_closed(p, q, tau):
    """Physical 2nd spectral moment per sector: M2 = -Tr D_pi^2."""
    d = dim_pq(p, q)  # (local)
    return -16.0 * casimir_g_closed(p, q, tau) - d * tr_omega2_closed(tau)


def dM2_dtau_closed(p, q, tau):
    """Analytic derivative dM2/dtau = d*(C2*gC + gS)."""
    d = dim_pq(p, q)  # (local)
    C2 = C2_pq(p, q)  # (local)
    gC = 4 * np.exp(2 * tau) - (8.0 / 3.0) * np.exp(-tau) - (4.0 / 3.0) * np.exp(-2 * tau)  # (local)
    gS = 10 * np.exp(2 * tau) - 4 * np.exp(-tau) - 4 * np.exp(-2 * tau) - 2 * np.exp(-4 * tau)  # (local)
    return d * (C2 * gC + gS)


# ---------------------------------------------------------------------------
# Section 6 — Compute / verify / prove
# ---------------------------------------------------------------------------
def compute():
    out = {}  # (local)
    gens = su3_generators()  # (local)
    f_abc = compute_structure_constants(gens)  # (local)
    B_ab = compute_killing_form(f_abc)  # (local)
    gammas = build_cliff8()  # (local)

    # ---- (A) Closed-form vs numeric Tr D_pi^2 (machine-eps validation) ----
    tau0 = float(tau_fold)  # (local) 0.19
    g_s = jensen_metric(B_ab, tau0)  # (local)
    E = orthonormal_frame(g_s)  # (local)
    ft = frame_structure_constants(f_abc, E)  # (local)
    Gamma = connection_coefficients(ft)  # (local)
    Omega = spinor_connection_offset(Gamma, gammas)  # (local)

    max_rel_M2 = 0.0  # (local)
    for p in range(0, 4):
        for q in range(0, 4 - p):
            if p == 0 and q == 0:
                D = Omega.copy()  # (local)
            else:
                rho, _ = get_irrep(p, q, gens, f_abc)  # (local)
                D = dirac_operator_on_irrep(rho, E, gammas, Omega)  # (local)
            M2_num = -np.trace(D @ D).real  # (local)
            M2_cl = M2_closed(p, q, tau0)  # (local)
            max_rel_M2 = max(max_rel_M2, abs(M2_num - M2_cl) / abs(M2_num))
    out["max_rel_M2_closed_vs_numeric"] = max_rel_M2

    # ---- (B) Equipartition theorem check (S_su2:S_c2:S_u1 = 3:4:1) ----
    max_equipart_dev = 0.0  # (local)
    for p in range(0, 8):
        for q in range(0, 8 - p):
            if p == 0 and q == 0:
                continue
            rho, _ = get_irrep(p, q, gens, f_abc)  # (local)
            Bd = np.array([[np.trace(rho[b] @ rho[d]).real for d in range(8)] for b in range(8)])  # (local)
            S_su2 = sum(Bd[i, i] for i in [0, 1, 2])  # (local)
            S_c2 = sum(Bd[i, i] for i in [3, 4, 5, 6])  # (local)
            S_u1 = Bd[7, 7]  # (local)
            base = -C2_pq(p, q) * dim_pq(p, q) / 8.0  # (local)
            dev = max(abs(S_su2 - 3 * base), abs(S_c2 - 4 * base), abs(S_u1 - 1 * base))  # (local)
            max_equipart_dev = max(max_equipart_dev, dev)
    out["max_equipartition_deviation"] = max_equipart_dev

    # ---- (C) Tr(Omega^2) closed form vs numeric over the domain ----
    taus = np.linspace(0.0, float(tau_NEC), 24)  # (local)
    max_rel_TrO2 = 0.0  # (local)
    for t in taus:
        gst = jensen_metric(B_ab, t)  # (local)
        Et = orthonormal_frame(gst)  # (local)
        ftt = frame_structure_constants(f_abc, Et)  # (local)
        Gt = connection_coefficients(ftt)  # (local)
        Ot = spinor_connection_offset(Gt, gammas)  # (local)
        num = np.trace(Ot @ Ot).real  # (local)
        cl = tr_omega2_closed(t)  # (local)
        max_rel_TrO2 = max(max_rel_TrO2, abs(num - cl) / max(abs(num), 1e-12))
    out["max_rel_TrOmega2_closed_vs_numeric"] = max_rel_TrO2

    # ---- (D) Sage-certified factorization (proof certificate, recomputed here in QQ-equivalent integers) ----
    # gC*e^{2tau} = 4u^4 - 8/3 u - 4/3 = (u-1)(4u^3+4u^2+4u+4/3); cofactor coeffs *3 = [4,12,12,12] all>0
    # gS*e^{4tau} = 10u^6 - 4u^3 - 4u^2 - 2 = (u-1)(10u^5+10u^4+10u^3+6u^2+2u+2); coeffs [10,10,10,6,2,2] all>0
    # Verify the factorization by exact integer polynomial division (scaled by 3 to clear the 1/3).
    gC_scaled = np.array([12, 0, 0, -8, -4], dtype=np.int64)  # (local) 3*gC*e^{2tau}: 12u^4 +0 +0 -8u -4
    gS_int = np.array([10, 0, 0, -4, -4, 0, -2], dtype=np.int64)  # (local) gS*e^{4tau}: 10u^6 .. -2
    # synthetic division by (u-1): remainder = poly evaluated at u=1
    remC = int(np.polyval(gC_scaled, 1))  # (local) == 0 if (u-1) divides
    remS = int(np.polyval(gS_int, 1))  # (local)
    cofC = np.polydiv(gC_scaled.astype(float), np.array([1.0, -1.0]))[0]  # (local)
    cofS = np.polydiv(gS_int.astype(float), np.array([1.0, -1.0]))[0]  # (local)
    cofC_int = np.rint(cofC).astype(np.int64)  # (local) [12,12,12,4]  (=3*[4,4,4,4/3])
    cofS_int = np.rint(cofS).astype(np.int64)  # (local) [10,10,10,6,2,2]
    out["factor_remainder_gC"] = remC
    out["factor_remainder_gS"] = remS
    out["cofactor_gC_all_positive"] = bool(np.all(cofC_int > 0))
    out["cofactor_gS_all_positive"] = bool(np.all(cofS_int > 0))
    out["cofactor_gC"] = cofC_int.tolist()
    out["cofactor_gS"] = cofS_int.tolist()

    # ---- (E) Boundary at tau=0 and strict positivity scan over (0, tau_NEC), p+q<=10 ----
    dM2_at0_max = 0.0  # (local)
    for p in range(0, 11):
        for q in range(0, 11 - p):
            if p == 0 and q == 0:
                continue
            dM2_at0_max = max(dM2_at0_max, abs(dM2_dtau_closed(p, q, 0.0)))
    out["dM2_dtau_at_tau0_maxabs"] = dM2_at0_max  # should be ~0 (gC(0)=gS(0)=0)

    scan_t = np.linspace(1e-6, float(tau_NEC), 400)  # (local)
    min_dM2 = np.inf  # (local)
    argmin = None  # (local)
    for p in range(0, 11):
        for q in range(0, 11 - p):
            if p == 0 and q == 0:
                continue
            vals = dM2_dtau_closed(p, q, scan_t)  # (local) vectorized
            mloc = float(np.min(vals))  # (local)
            if mloc < min_dM2:
                min_dM2 = mloc
                argmin = (p, q, float(scan_t[int(np.argmin(vals))]))
    out["min_dM2_dtau_over_domain"] = min_dM2  # > 0 confirms strict positivity
    out["argmin_dM2"] = argmin

    # analytic-vs-numeric dM2 at fold (FD of the closed M2)
    h = 1e-5  # (local)
    max_rel_dM2 = 0.0  # (local)
    for p in range(0, 4):
        for q in range(0, 4 - p):
            an = dM2_dtau_closed(p, q, tau0)  # (local)
            nd = (M2_closed(p, q, tau0 + h) - M2_closed(p, q, tau0 - h)) / (2 * h)  # (local)
            max_rel_dM2 = max(max_rel_dM2, abs(an - nd) / abs(nd))
    out["max_rel_dM2_analytic_vs_numdiff"] = max_rel_dM2

    # ---- (F) Anchor cross-check: reproduce dS_full/dtau (|lambda|-action) AND analytic lambda^2-action grad ----
    KK = [(0, 0), (1, 0), (0, 1), (1, 1), (2, 0), (0, 2), (3, 0), (0, 3), (2, 1), (1, 2)]  # (local)
    h_anchor = 0.001  # (local) match S42 FD step

    def S_full(t):
        gst = jensen_metric(B_ab, t)  # (local)
        Et = orthonormal_frame(gst)  # (local)
        ftt = frame_structure_constants(f_abc, Et)  # (local)
        Gt = connection_coefficients(ftt)  # (local)
        Ot = spinor_connection_offset(Gt, gammas)  # (local)
        DS._irrep_cache.clear()
        S = 0.0  # (local)
        for (p, q) in KK:
            if p == 0 and q == 0:
                Dm = Ot.copy()  # (local)
            else:
                rho, _ = get_irrep(p, q, gens, f_abc)  # (local)
                Dm = dirac_operator_on_irrep(rho, Et, gammas, Ot)  # (local)
            ev = eigvalsh(1j * Dm)  # (local)
            S += (dim_pq(p, q) ** 2) * float(np.sum(np.abs(ev)))
        return S

    Sm = S_full(tau0 - h_anchor)  # (local)
    Sp = S_full(tau0 + h_anchor)  # (local)
    dS_full_dtau = (Sp - Sm) / (2 * h_anchor)  # (local) reproduces dS_fold
    out["dS_full_dtau_reproduced"] = dS_full_dtau
    out["dS_fold_canonical"] = float(dS_fold)
    out["anchor_repro_rel_err"] = abs(dS_full_dtau - float(dS_fold)) / abs(float(dS_fold))

    # analytic lambda^2-spectral-action gradient with the SAME mult=dim^2 weighting
    dS2_dtau = 0.0  # (local)
    for (p, q) in KK:
        dS2_dtau += (dim_pq(p, q) ** 2) * dM2_dtau_closed(p, q, tau0)
    out["dS2_lambda2_action_grad_analytic"] = dS2_dtau

    # the LITERAL pre-reg magnitude cross-check (against +58672.8): tests a DIFFERENT functional
    out["literal_xcheck_ratio"] = abs(dS2_dtau - float(dS_fold)) / abs(float(dS_fold))
    out["literal_xcheck_pass"] = bool(out["literal_xcheck_ratio"] < TOL_XCHECK)

    # SIGN cross-check: analytic gradient sign vs anchor sign
    out["sign_match"] = bool((dS2_dtau > 0) == (dS_full_dtau > 0) and dS2_dtau > 0)

    return out


def build_plot(res, taus, png_path):
    gens = su3_generators()  # (local)
    f_abc = compute_structure_constants(gens)  # (local)
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.6))  # (local)

    # Left: dM2/dtau per sector vs tau, showing strict positivity + tau=0 zero
    for (p, q) in [(1, 0), (1, 1), (2, 0), (3, 0), (2, 2)]:
        axes[0].plot(taus, dM2_dtau_closed(p, q, taus), label=f"({p},{q})")
    axes[0].axhline(0, color="k", lw=0.6)
    axes[0].axvline(float(tau_fold), color="r", ls=":", lw=0.8, label=f"fold {float(tau_fold):.2f}")
    axes[0].axvline(float(tau_NEC), color="m", ls="--", lw=0.8, label=f"tau_NEC {float(tau_NEC):.3f}")
    axes[0].set_xlabel("tau")
    axes[0].set_ylabel("dM2/dtau  (per sector)")
    axes[0].set_title("Per-sector d<lambda^2>/dtau > 0 (=0 at tau=0)")
    axes[0].legend(fontsize=7, ncol=2)
    axes[0].grid(alpha=0.3)

    # Right: the two cofactor-clearing polynomials gC*e^{2tau}, gS*e^{4tau} in u=e^tau >=1
    u = np.linspace(1.0, np.exp(float(tau_NEC)), 200)  # (local)
    gC_poly = 4 * u ** 4 - (8.0 / 3.0) * u - 4.0 / 3.0  # (local)
    gS_poly = 10 * u ** 6 - 4 * u ** 3 - 4 * u ** 2 - 2  # (local)
    axes[1].plot(u, gC_poly, label="gC*e^{2tau} = 4u^4-8/3u-4/3")
    axes[1].plot(u, gS_poly, label="gS*e^{4tau} = 10u^6-4u^3-4u^2-2")
    axes[1].axhline(0, color="k", lw=0.6)
    axes[1].axvline(1.0, color="g", ls=":", lw=0.8, label="u=1 (tau=0, root)")
    axes[1].set_xlabel("u = e^tau")
    axes[1].set_ylabel("cleared polynomial")
    axes[1].set_title("(u-1)*(all-positive cofactor): zero at u=1, >0 for u>1")
    axes[1].legend(fontsize=7)
    axes[1].grid(alpha=0.3)

    fig.suptitle("S102 W3-14: analytic dM2/dtau > 0 (Weitzenbock + Jensen g_tau); E7 lambda^2-monotonicity",
                 fontsize=10)
    fig.tight_layout()
    fig.savefig(png_path, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------
def main():
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = Path(SHARED_DIR) / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    res = compute()

    # --- proof gates (the closed forms must be EXACT; positivity must hold) ---
    closed_forms_exact = (
        res["max_rel_M2_closed_vs_numeric"] < MACHINE_EPS_TOL
        and res["max_equipartition_deviation"] < 1e-9
        and res["max_rel_TrOmega2_closed_vs_numeric"] < MACHINE_EPS_TOL
        and res["max_rel_dM2_analytic_vs_numdiff"] < 1e-6
    )  # (local)
    factorization_certified = (
        res["factor_remainder_gC"] == 0
        and res["factor_remainder_gS"] == 0
        and res["cofactor_gC_all_positive"]
        and res["cofactor_gS_all_positive"]
    )  # (local)
    strict_positive = (res["min_dM2_dtau_over_domain"] > 0.0
                       and res["dM2_dtau_at_tau0_maxabs"] < 1e-10)  # (local)
    sign_proof = closed_forms_exact and factorization_certified and strict_positive  # (local)

    print("=== PROOF CERTIFICATE ===")
    print(f"  closed M2 vs numeric Tr D^2 (max rel)     : {res['max_rel_M2_closed_vs_numeric']:.2e}")
    print(f"  equipartition 3:4:1 (max dev, p+q<=7)     : {res['max_equipartition_deviation']:.2e}")
    print(f"  Tr(Omega^2) closed vs numeric (max rel)   : {res['max_rel_TrOmega2_closed_vs_numeric']:.2e}")
    print(f"  analytic dM2 vs numdiff (max rel)         : {res['max_rel_dM2_analytic_vs_numdiff']:.2e}")
    print(f"  gC factor remainder / gS factor remainder : {res['factor_remainder_gC']} / {res['factor_remainder_gS']}")
    print(f"  cofactor gC {res['cofactor_gC']} all>0    : {res['cofactor_gC_all_positive']}")
    print(f"  cofactor gS {res['cofactor_gS']} all>0    : {res['cofactor_gS_all_positive']}")
    print(f"  dM2/dtau|_tau=0 (maxabs, all sectors)     : {res['dM2_dtau_at_tau0_maxabs']:.2e}  (=0 boundary)")
    print(f"  min dM2/dtau over (0,tau_NEC), p+q<=10    : {res['min_dM2_dtau_over_domain']:.3e}  at {res['argmin_dM2']}")
    print(f"  => SIGN PROOF (dM2/dtau>0 strict, tau>0)  : {sign_proof}")
    print()
    print("=== ANCHOR CROSS-CHECK ===")
    print(f"  dS_full/dtau reproduced (|lambda|-action) : {res['dS_full_dtau_reproduced']:.4f}")
    print(f"  dS_fold canonical                         : {res['dS_fold_canonical']:.4f}")
    print(f"  anchor reproduction rel err               : {res['anchor_repro_rel_err']:.2e}  (validates construction)")
    print(f"  analytic lambda^2-action gradient         : {res['dS2_lambda2_action_grad_analytic']:.4f}")
    print(f"  LITERAL xcheck |lam2 - 58672.8|/58672.8   : {res['literal_xcheck_ratio']:.4f}  PASS<{TOL_XCHECK}? {res['literal_xcheck_pass']}")
    print(f"  SIGN match (analytic vs anchor, both >0)  : {res['sign_match']}")
    print()

    # --- [SIGN] 3-tuple ---
    # sign:      the proven analytic gradient sign matches the anchor (both strictly > 0)
    # magnitude: the LITERAL pre-reg magnitude xcheck (vs +58672.8, the |lambda|-action) FAILs,
    #            because the anchor is a DIFFERENT functional than the lambda^2 object proven.
    # regime:    valid on the entire physical domain [0, tau_NEC) (in fact all tau>0).
    sign_verdict = "PASS" if (sign_proof and res["sign_match"]) else "FAIL"  # (local)
    magnitude_verdict = "PASS" if res["literal_xcheck_pass"] else "FAIL"  # (local)
    regime_verdict = "VALID"  # (local) proof holds on full domain; no breakdown

    # Composite: SIGN proven exactly (the literal E7 <lambda^2>-monotonicity content);
    # magnitude clause tests a different functional => INFO per PLAN INFO_meaning
    # ("strict positivity proven ... modulo a clearly-stated [scope] issue;
    #  Partial-Theorem status"). NOT forced to PASS (would require redefining the
    #  cross-check = convention-shopping). NOT FAIL (the proof of the E7 sign is complete
    #  and the magnitude clause is a plan-side functional conflation, not a proof failure).
    if not sign_proof:
        composite = "FAIL"  # (local)
    elif magnitude_verdict == "PASS":
        composite = "PASS"  # (local) would require lambda^2-action to equal +58672.8
    else:
        composite = "INFO"  # (local) sign proven; magnitude clause tests a different functional

    value = (
        f"SIGN-PROVEN-CLOSED-FORM_dM2dtau>0_strict_tau>0_=0_at_tau0_L-uniform; "
        f"factor_gC=(u-1)(4u3+4u2+4u+4/3)_gS=(u-1)(10u5+10u4+10u3+6u2+2u+2)_cofactors_all_pos; "
        f"min_dM2dtau={res['min_dM2_dtau_over_domain']:.3e}>0; "
        f"closed_vs_numeric_max_rel={res['max_rel_M2_closed_vs_numeric']:.1e}; "
        f"equipart_dev={res['max_equipartition_deviation']:.1e}; "
        f"anchor_repro={res['dS_full_dtau_reproduced']:.2f}_vs_dSfold_58672.80_relerr={res['anchor_repro_rel_err']:.1e}; "
        f"lambda2_action_grad={res['dS2_lambda2_action_grad_analytic']:.1f}_NEQ_58672.8_DIFFERENT-FUNCTIONAL; "
        f"literal_mag_xcheck_FAIL_ratio={res['literal_xcheck_ratio']:.3f}; "
        f"E7_lambda2_monotonicity_PROVEN_analytic_E7_9600numeric_UNCHANGED"
    )  # (local)

    extra_rows = [
        "# composite-precedence: session-102-plan-w3.md §W3-14 INFO_meaning ('positivity proven ... modulo a clearly-stated [scope] issue; Partial-Theorem status') + dual_prior discriminator ('INFO => unchanged'). PLAN-FROZEN operator overrides the generic gate-verdicts.md collapse (mag=FAIL & regime=VALID => FAIL): here mag=FAIL is a plan-side functional conflation (anchor = |lambda|-action, proof = lambda^2-moment), NOT a proof failure; SIGN (the literal E7 content) is proven exactly.",
        "# regulator_pin: a_0^{zeta}, a_2^{zeta}, a_4^{zeta} (Gilkey-zeta; S_SA=a_0-a_2+a_4 per E7)",
        "# proof: dM2/dtau=d*(C2*gC+gS); gC*e^{2tau}=(u-1)(4u^3+4u^2+4u+4/3); gS*e^{4tau}=(u-1)(10u^5+10u^4+10u^3+6u^2+2u+2); u=e^tau>=1 => strict>0 for tau>0",
        "# scope: SIGN proven for f(x)=x (lambda^2 moment, closed-form exact, L-uniform); anchor +58672.8 = |lambda|-action f(x)=sqrt(x), DIFFERENT functional (no per-sector closed form); E7 'ALL monotone f' covers anchor SIGN as corollary",
        f"# dual_prior_posterior: INFO => unchanged (Track A 0.6 / Track B 0.4 per plan discriminator); E7 9,600-numerical status UNCHANGED",
    ]  # (local)

    tag = f"(value=<{composite}>, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})"  # (local)
    print(tag)

    print_verdict_payload(
        composite, value, audit_sha, content_sha,
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict,
        companion_note="E7 lambda^2-monotonicity proven analytic (Weitzenbock+Jensen g_tau); magnitude clause tests |lambda|-action (different functional)",
        extra_rows=extra_rows,
    )

    # ---- save artifacts ----
    here = Path(__file__).resolve().parent  # (local)
    npz_path = here / "s102_trd2_monotonicity_analytic.npz"  # (local)
    png_path = here / "s102_trd2_monotonicity_analytic.png"  # (local)
    taus_plot = np.linspace(0.0, float(tau_NEC), 200)  # (local)
    np.savez(
        npz_path,
        max_rel_M2=res["max_rel_M2_closed_vs_numeric"],
        max_equipartition_deviation=res["max_equipartition_deviation"],
        max_rel_TrOmega2=res["max_rel_TrOmega2_closed_vs_numeric"],
        max_rel_dM2=res["max_rel_dM2_analytic_vs_numdiff"],
        factor_remainder_gC=res["factor_remainder_gC"],
        factor_remainder_gS=res["factor_remainder_gS"],
        cofactor_gC=np.array(res["cofactor_gC"]),
        cofactor_gS=np.array(res["cofactor_gS"]),
        cofactor_gC_all_positive=res["cofactor_gC_all_positive"],
        cofactor_gS_all_positive=res["cofactor_gS_all_positive"],
        dM2_dtau_at_tau0_maxabs=res["dM2_dtau_at_tau0_maxabs"],
        min_dM2_dtau_over_domain=res["min_dM2_dtau_over_domain"],
        argmin_dM2=np.array(res["argmin_dM2"]),
        dS_full_dtau_reproduced=res["dS_full_dtau_reproduced"],
        dS_fold_canonical=res["dS_fold_canonical"],
        anchor_repro_rel_err=res["anchor_repro_rel_err"],
        dS2_lambda2_action_grad_analytic=res["dS2_lambda2_action_grad_analytic"],
        literal_xcheck_ratio=res["literal_xcheck_ratio"],
        literal_xcheck_pass=res["literal_xcheck_pass"],
        sign_match=res["sign_match"],
        sign_verdict=sign_verdict,
        magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict,
        composite=composite,
        tau_fold=float(tau_fold),
        tau_NEC=float(tau_NEC),
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )
    build_plot(res, taus_plot, str(png_path))
    print(f"\n  saved: {npz_path.name}, {png_path.name}")

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {composite} "
          f"(sign={sign_verdict}/mag={magnitude_verdict}/regime={regime_verdict}, wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
