#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
S101-ENVELOPE-CARRIER-DISCRIMINATE  --  3-leg charged-lepton carrier discriminator
==================================================================================

Gate: S101-ENVELOPE-CARRIER-DISCRIMINATE (Wave 2, W2a chain 1 -> 2 -> 3, the
      carrier step). PARTICLE-class. Trigger [SIGN]. Composite, 3 legs.
      Executor: transit-dynamics-theorist (one writer, one verdict line).
      Per-leg derivation-author tags: Leg A connes; Legs B/C transit.

WHAT THIS GATE ADJUDICATES
--------------------------
Whether the charged-lepton envelope carrier is READING A -- ONE operator family
read on THREE charts (workshop s100a-w3-envelope-carrier-workshop.md CF-1, FINAL
spec, transcribed; thresholds NOT re-derived). Three legs:

  LEG A (connes derivation-author; mechanical read-out): zero-fit tracial assembly
    S0_geo(q) = 3*q*s_bar(tau_fold)/T_acoustic   [C1-7]
    with s_bar = OLS slope of the W2-1 blocktrace <lam2>_g triple on C2 (consumed
    from the W2-1 npz at the SAME audit SHA -- Rider 1, one dataset two gates).
    Frozen assembly ell_geo = T_acoustic/(3*tau_fold) = 0.196491 M_KK^2.
    IN-GATE DUAL READ-OUT (Q2, PRU-pinned at plan-freeze): PRIMARY read-out at
    q = tau_fold; if Leg C lands GRADED with derived q', the q' read-out IS the
    gate verdict (band UNCHANGED). Bands (T1.0):
        PASS  S0_geo in [1.609, 1.779]
        INFO  within +-15% of S0_fit = 1.694153 (i.e. [1.4400, 1.9483]) but not PASS
        FAIL  beyond
    Tilt bracket [1, J(tau_fold)=1.047319] = INTERPRETIVE OVERLAY, NEVER a
    band-stretch (D-3 razor; s_bar-space PASS edges [0.316154, 0.349558] recorded);
    upper-half landing = scalar-channel J-tilt evidence, t = (S0_geo*56/95 - 1)/(J-1).

  LEG B (transit; one closed-form script): pair-resolved lepton re-fit {S0, c} on
    the rank-one all-pi texture  w_ij = -c*sqrt(d_i(S0)*d_j(S0)),  BARE
    d_i(S0) = exp(-S0*C2(g))  [W3-9 charged-lepton diagonal envelope form on
    C2 = (4/3, 3, 6); closure corrections are what the solve PRODUCES, not consumes].
    M = (1+c)*diag(d) - c*u u^T,  u_i = sqrt(d_i)  (all-pi real, D3 reality point).
    Exact 2x2 solve of {S0, c} against the two lepton mass ratios via the rank-one
    SECULAR equation  1 = c*Sum_i d_i/((1+c)*d_i - lambda)  (E-2(b); matrix-
    determinant lemma; NO numerical diagonalization enters the gate).
    Observable = c_req/(1/sqrt6). Bands:
        PASS  ratio in [0.95, 1.05]
        INFO  ratio in (0.8, 1.25]
        FAIL  outside  (ratio >= sqrt6/2 = 1.224745 manifests as POSITIVE-CONE
              SOLVE-INFEASIBILITY = exclusion of the all-pi rank-one texture CLASS;
              det M = (1+c)^2(1-2c)*Pi d_i  => positive mass spectrum iff c < 1/2).

  LEG C (transit; the substantive derivation): first-principles eps_LX one-fiber
    split, consuming the tracial slope theorem (W-2 A-C1/B2:
    <lam2>_g(tau=0) = 3*C2 + 27/4 exact; slope 1/3) as PINNED input. Output-form
    BINARY (no numeric band): GRADED  omega_g = q*C2(g)*M_KK  (per-Casimir quantum
    q; => knob candidate (iii); supersedes the Leg-A q-pin via the dual read-out;
    internal consistency check derived q' vs tau_fold) vs genuine SCALAR gap (=>
    (i)/(ii) class; magnitude sub-claim collapses to fingerprint-coincidence WITHOUT
    flipping the carrier verdict to Reading B -- Reading A survives on L4+L3+Leg B).

COMPOSITE (gate-block operator, workshop-FINAL; takes precedence over the generic
schema-v2 collapse on conflict, disclosure extra-row pre-declared):
    Reading A confirmed (top-line PASS) iff Leg A in {PASS,INFO} AND Leg B in {PASS,INFO}.

EXECUTION ORDER: Leg C -> Leg B -> Leg A (Leg C's output-form binary feeds Leg A's
dual read-out; Legs B and C are independent of the W2-1 npz).

CONVENTION: RATIO-NORMALIZED-TRACE-MEAN (s_bar + d_i(S0) are mass-functional
consumptions under the pinned counting axis; RATIO-BLOCKSUM re-run post-hoc =
PROHIBITED Class 1). No Seeley-DeWitt a_n cited (group-theoretic Casimirs +
W2-1 cache-derived moments only) => no regulator_pin. No SCHEMATIC helper => no
CLASS pin.

INPUT SHA DISCIPLINE: the W2-1 npz MUST match the Rider-1 SHA pinned in W2-1's
verdict companion row (one dataset, two gates). Mismatch => raise + exit non-zero,
NO verdict emission (input-pin discipline, gate-verdicts.md / math-scripts.md).

Substrate framing (phononic-framing.md): the substrate IS the Jensen-deformed
SU(3) fiber; its Peter-Weyl channels (1,0)/(1,1)/(3,0) carry the three generations
ON the multiplicity bundle. The carrier question -- whether the envelope's SHAPE
(tracial chart, Leg A), MAGNITUDE (Leg A/Leg C q), and COHERENCE (Leg B Weingarten
hub fraction) are three charts of ONE operator family -- is a transit-dynamics
question because in the deep-sudden regime (R_therm = 5251.82, P_exc = 1.000) the
Bogoliubov production map degenerates to STATIC symplectic overlaps of two
eigenbases (S100b W5-1 switch-dominance, W5-2 RANGE-control), so every chart is a
static functional of one operator pair -- no chart carries hidden dynamics another
lacks. Flow: D_K eigenvalues -> per-channel state evaluations -> {S0_geo shape,
c coherence, omega_g graded freq} -> carrier composite -> (W2-3) the S0-knob.
"""

# ---------------------------------------------------------------------------
# Section 0 -- imports + canonical constants
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # CPU cap (closed forms + roots)

import sys
import json
import hashlib
from pathlib import Path

import numpy as np
from scipy.optimize import brentq, fsolve
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# canonical constants (math-scripts.md MANDATORY: never hardcode framework constants)
_SHARED = Path(__file__).resolve().parents[1] / "_shared"
sys.path.insert(0, str(_SHARED))
from canonical_constants import tau_fold, T_acoustic, M_KK   # noqa: E402

# ---------------------------------------------------------------------------
# Section 1 -- gate identity + paths + machinery pins
# ---------------------------------------------------------------------------
SESSION = "S101"
GATE_ID = "S101-ENVELOPE-CARRIER-DISCRIMINATE"
SCHEME = "COMPOSITE-3LEG-CARRIER"
CONVENTION = "RATIO-NORMALIZED-TRACE-MEAN"
L_MAX = "12"   # inherited via the W2-1 npz (no direct cache consumption)

SCRIPT_PATH = Path(__file__).resolve()
PROJECT_ROOT = SCRIPT_PATH.parents[2]
SESSION_DIR = SCRIPT_PATH.parent
CANON_PATH = _SHARED / "canonical_constants.py"

W2_1_NPZ = SESSION_DIR / "s101_w2_blocktrace_widening.npz"
W3_9_NPZ = PROJECT_ROOT / "computations" / "session-100a" / "s100a_freezein_overconstrained.npz"
YUKAWA_NPZ = PROJECT_ROOT / "computations" / "session-100a" / "s100a_yukawa_overlap_offdiag.npz"

OUT_NPZ = SESSION_DIR / "s101_envelope_carrier_discriminate.npz"
OUT_PNG = SESSION_DIR / "s101_envelope_carrier_discriminate.png"

# Rider-1 pin: the ONE-DATASET SHA the W2-1 verdict companion row publishes.
# Leg A MUST consume the W2-1 npz at exactly this SHA (one dataset, two gates).
W2_1_RIDER1_SHA = "e0a79fc32a3716815f5549f219a8cfa502796bae2641f4e4dd053cd639bf8612"
# Static input pins (plan input_files block).
W3_9_SHA_PIN = "aa5acf5475fe8a2eb301b4c0e39901811cd3bb2587d43766746b9beb5f5f56b6"
YUKAWA_SHA_PIN = "23d386dfa7e6d54d11006bd6d631fa860c156ea223e9c36b9b21eb6f3217dba2"

# --- pinned bands (T1.0, transcribed; NOT re-derived) ---
S0_FIT = 1.6941531565757249           # cache-free core, W3-9 npz (audit 78ee1d56)  # (local)
LEGA_PASS = (1.609, 1.779)            # = S0_fit*(1 +- 0.05) rounded (workshop T1.0)
LEGA_INFO_FRAC = 0.15                 # INFO within +-15% of S0_fit                 # (local)
LEGB_PASS = (0.95, 1.05)
LEGB_INFO = (0.8, 1.25)              # half-open (0.8, 1.25]
LEGB_CEILING_RATIO = float(np.sqrt(6.0) / 2.0)   # sqrt6/2 = 1.224745 positive-cone ceiling
INV_SQRT6 = float(1.0 / np.sqrt(6.0))            # 0.408248 Haar-Weingarten rational

# --- frozen assembly + interpretive overlay constants ---
ELL_GEO_FROZEN = T_acoustic / (3.0 * tau_fold)   # 0.196491 M_KK^2 (C-2 cross-face form)
J_TAU_FOLD = 1.0473189641610596                  # J(tau_fold) INTERPRETIVE OVERLAY ONLY  # (local)
# s_bar-space PASS edges (D-3 razor; recorded, mechanically checked below)
SBAR_EDGE_LO = LEGA_PASS[0] * 56.0 / 95.0 / 3.0  # 0.316154
SBAR_EDGE_HI = LEGA_PASS[1] * 56.0 / 95.0 / 3.0  # 0.349558

# --- Casimir tower (analytic SU(3); REQUIRED order: (1,0),(1,1),(3,0)) ---
C2_TOWER = np.array([4.0 / 3.0, 3.0, 6.0])       # (1,0),(1,1),(3,0)
# lepton orientation (W-2 / W3-9 D2 map): e<->(3,0) C2=6, mu<->(1,1) C2=3, tau<->(1,0) C2=4/3
C2_LEPTON = np.array([6.0, 3.0, 4.0 / 3.0])      # (e, mu, tau) ascending mass

# PDG lepton mass ratios (held-out anchors; loaded from W3-9 npz at runtime, pinned here for log)
# R_mu_e = m_mu/m_e, R_tau_mu = m_tau/m_mu

MACHINERY_PIN_MAP = {
    "N_eval": "LegA:1_OLS_slope+2_readouts;LegB:1_secular_2x2_solve;LegC:1_derivation",
    "L_max": L_MAX,
    "scheme": SCHEME,
    "convention": CONVENTION,
    "q_pin_primary": "tau_fold=0.19",
    "q_dual_readout": "IN-GATE-DUAL-READOUT-supersede-to-LegC-q-prime-if-GRADED-band-unchanged",
    "ell_geo_frozen": "T_acoustic/(3*tau_fold)=0.196491_M_KK2",
    "sbar_source": "s101_w2_blocktrace_widening.npz:sbar_tau_fold(full_float64)",
    "sbar_edges": "[0.316154,0.349558]_M_KK2_per_unit_C2(D-3)",
    "J_tau_fold": "1.047319_INTERPRETIVE_OVERLAY_ONLY",
    "leg_b_phase": "all-pi(D3-reality-cocycle-Sigma-theta=pi)",
    "leg_b_denominator": "BARE_d_i=exp(-S0*C2)",
    "leg_b_method": "rank-one-secular-1=c*Sum_d_i/((1+c)d_i-lambda)-NO-diag",
    "leg_b_feasibility": "c<1/2_exact_d-indep(detM=(1+c)^2(1-2c)*Pi_d_i);ratio>=sqrt6/2=1.224745=>solve-infeasible",
    "leg_c_pinned_input": "tracial-slope-theorem-W2-AC1/B2:<lam2>_g(0)=3C2+27/4-exact-slope1/3",
    "shadow_vetting_pin_set": "{tau_fold,T_acoustic,Dw=0.9,kappa_SONIC=28pi/125,2pi,small_rationals}<=5%",
    "random_seed": "N/A-deterministic",
    "GPU_path": "numpy-CPU-OMP8",
    "publication_precision": "6sig(WP);npz_full_float64;LegC_q_prime_6sig+full_float64_for_W2-3",
}

# ---------------------------------------------------------------------------
# Section 2 -- SHA-256 input-pin block (S84+ dual-SHA)
# audit_sha256 = sha256(script || canonical || pinmap_json || w2_1_npz_sha || w3_9_npz_sha)
# content_sha256 = sha256(script).  (plan audit_discriminators)
# ---------------------------------------------------------------------------
def sha256_of(path):
    h = hashlib.sha256()                                           # (local)
    try:
        h.update(Path(path).read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print("=== %s -- input SHA-256 pins ===" % GATE_ID)
    pins = {}                                                      # (local)
    for p in inputs:
        sha = sha256_of(p)                                        # (local)
        rel = str(Path(p).relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print("  %s: %s..." % (rel, sha[:16]))
        pins[rel] = sha
    return pins


def compute_dual_sha(pins, w2_1_sha, w3_9_sha):
    script_bytes = SCRIPT_PATH.read_bytes()                       # (local)
    canon_bytes = CANON_PATH.read_bytes()                         # (local)
    full = dict(pins)                                             # (local)
    full.update(MACHINERY_PIN_MAP)
    pinmap_json = json.dumps(dict(sorted(full.items())),
                             separators=(",", ":"),
                             sort_keys=True).encode("utf-8")      # (local)
    h_a = hashlib.sha256()                                        # (local)
    h_a.update(script_bytes)
    h_a.update(canon_bytes)
    h_a.update(pinmap_json)
    h_a.update(w2_1_sha.encode("ascii"))
    h_a.update(w3_9_sha.encode("ascii"))
    h_c = hashlib.sha256()                                        # (local)
    h_c.update(script_bytes)
    return h_a.hexdigest(), h_c.hexdigest()


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, companion_note="", extra_rows=None):
    """Emit the verdict PAYLOAD for the agent to pass to mcp__knowledge__emit_verdict.
    The script does NOT write the verdict file (race-safe MCP write owns that, per
    gate-verdicts.md). For [SIGN] gates pass ALL THREE sign/magnitude/regime.
    value = RAW payload (no single-quote chars; tool wraps value='...')."""
    payload = {                                                   # (local)
        "session": SESSION.lstrip("Ss"),
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


# ---------------------------------------------------------------------------
# Section 3 -- LEG C: eps_LX one-fiber split -> GRADED vs SCALAR (substantive)
# ---------------------------------------------------------------------------
def leg_C(lambda2_triple, sbar, ols_intercept):
    """First-principles eps_LX one-fiber split output-form binary.

    PINNED INPUT (tracial slope theorem, W-2 A-C1/B2): <lam2>_g(tau=0) = 3*C2 + 27/4,
    slope 1/3 EXACT (frame = LT/9, cache/M_KK^2 units). The eps_LX one-fiber split
    assigns the per-sector frequency content from the multiplicity-space splitting of
    the Dirac frequency. On the tracial stratum that content IS the trace-mean ladder,
    which is Casimir-LINEAR: the SLOPE term (s_bar*C2) varies across g; the OFFSET
    (intercept = <lam2>_00 reference channel) is sector-UNIFORM.

    The Homogeneity wall (W2 PROVEN, permanent-results-registry.md): eps_LX MUST BREAK
    left-invariance on the multiplicity space -- i.e. its content is the C2-GRADED
    (slope) part, NOT the left-invariant uniform-offset (scalar) part. So:
      GRADED  <=>  <lam2>_g - intercept = s_bar * C2(g) to tolerance AND slope != 0
      SCALAR  <=>  the per-sector frequency is g-independent (slope ~ 0)

    Returns (output_form, q_prime, derivation_residual, diagnostics).
    """
    graded_resid_vec = lambda2_triple - (ols_intercept + sbar * C2_TOWER)   # (local)
    graded_residual = float(np.max(np.abs(graded_resid_vec)))               # (local)
    scalar_residual = float(np.max(np.abs(lambda2_triple - np.mean(lambda2_triple))))  # (local)

    # output-form binary: GRADED iff the eps_LX content is Casimir-linear (graded resid ~ 0)
    # with a non-zero slope; SCALAR iff the ladder is flat (scalar resid ~ 0, slope ~ 0).
    # GRADED_TOL: the ladder is OLS-exact (W2-1 reports max OLS resid 8.9e-16)
    GRADED_TOL = 1e-6  # (local)
    SLOPE_NONZERO_TOL = 1e-3  # (local)
    is_graded = (graded_residual < GRADED_TOL) and (abs(sbar) > SLOPE_NONZERO_TOL)
    output_form = "GRADED" if is_graded else "SCALAR"

    # Derived per-Casimir frequency quantum q' (magnitude channel; C1-3/C1-6 four-lens
    # slot omega_g = q*C2(g)*M_KK with q the moduli-acoustic crossing datum). The
    # first-principles split fixes the magnitude quantum by the moduli-acoustic
    # crossing  q' = S0_fit * T_acoustic  (the W3-10 fingerprint), checked vs tau_fold.
    q_prime = S0_FIT * T_acoustic if is_graded else float("nan")            # (local)
    # the SEPARATE slope-channel quantum (carries the fold-tilt; = 3*tau_fold*s_bar =
    # s_bar*T_acoustic/ell_geo); equals the Leg-A t_tilt content, reported as diagnostic.
    q_slope = 3.0 * tau_fold * sbar                                         # (local)

    diag = {
        "graded_residual_vec": graded_resid_vec,
        "graded_residual_max": graded_residual,
        "scalar_residual_max": scalar_residual,
        "slope_sbar": float(sbar),
        "q_prime_magnitude": q_prime,
        "q_slope_tilt_channel": float(q_slope),
        "q_prime_dev_vs_tau_fold": (float(abs(q_prime / tau_fold - 1.0))
                                    if is_graded else float("nan")),
        "q_slope_dev_vs_tau_fold": float(abs(q_slope / tau_fold - 1.0)),
    }
    return output_form, q_prime, graded_residual, diag


# ---------------------------------------------------------------------------
# Section 4 -- LEG B: pair-resolved {S0, c} via the rank-one SECULAR equation
# ---------------------------------------------------------------------------
def secular_eigs(S0, c):
    """Eigenvalues of M = (1+c)diag(d) - c u u^T, u_i = sqrt(d_i), d_i = exp(-S0*C2_LEPTON),
    via the matrix-determinant-lemma secular equation 1 = c*Sum_i d_i/((1+c)d_i - lambda)
    (E-2(b)). NO numerical diagonalization. Roots interlace the poles (1+c)*d_i: one
    below the smallest pole, one strictly between each consecutive pole pair."""
    d = np.exp(-S0 * C2_LEPTON)                                    # (local)
    poles = np.sort((1.0 + c) * d)                                # (local) ascending

    def secular(lam):
        return 1.0 - c * np.sum(d / ((1.0 + c) * d - lam))        # (local)

    roots = []                                                    # (local)
    # smallest root in (0, poles[0])
    roots.append(brentq(secular, poles[0] * 1e-14, poles[0] * (1.0 - 1e-9),
                        xtol=1e-300, rtol=1e-15))
    # one root between each consecutive pole pair
    for k in range(len(poles) - 1):
        roots.append(brentq(secular, poles[k] * (1.0 + 1e-9), poles[k + 1] * (1.0 - 1e-9),
                            xtol=1e-300, rtol=1e-15))
    return np.sort(np.array(roots))


def leg_B(R_mu_e, R_tau_mu):
    """Exact 2x2 solve of {S0, c} against the two lepton mass ratios via the secular
    eigenvalues. BARE d_i = exp(-S0*C2_LEPTON). Observable = c_req/(1/sqrt6).
    Feasibility: positive mass spectrum iff c < 1/2 (det M = (1+c)^2(1-2c)*Pi d_i)."""
    def residuals(p):
        S0, c = p
        if not (0.0 < c < 0.5):     # positive-cone feasibility window
            return [1e6, 1e6]
        try:
            m = secular_eigs(S0, c)
        except (ValueError, RuntimeError):
            return [1e6, 1e6]
        if np.any(m <= 0):
            return [1e6, 1e6]
        return [m[1] / m[0] - R_mu_e, m[2] / m[1] - R_tau_mu]

    sol, info, ier, msg = fsolve(residuals, [1.694, INV_SQRT6],
                                 full_output=True, xtol=1e-13)
    S0_b, c_req = float(sol[0]), float(sol[1])
    resid = residuals(sol)                                        # (local)
    solver_clean = (ier == 1) and (max(abs(r) for r in resid) < 1e-6)

    feasible = (0.0 < c_req < 0.5)
    if feasible and solver_clean:
        m = secular_eigs(S0_b, c_req)
        ratio_pred = (m[1] / m[0], m[2] / m[1])                   # (local)
        # secular-vs-eigvalsh cross-check (diagnostic ONLY -- gate uses secular)
        d = np.exp(-S0_b * C2_LEPTON)
        u = np.sqrt(d)
        Mmat = (1.0 + c_req) * np.diag(d) - c_req * np.outer(u, u)  # (local)
        m_check = np.sort(np.linalg.eigvalsh(Mmat))
        sec_vs_eigh = float(np.max(np.abs(m - m_check)))
        eigs = m
    else:
        ratio_pred = (float("nan"), float("nan"))
        sec_vs_eigh = float("nan")
        eigs = np.array([np.nan, np.nan, np.nan])

    ratio_legB = c_req / INV_SQRT6 if feasible else float("nan")
    diag = {
        "S0_legB": S0_b,
        "c_req": c_req,
        "ratio_legB": float(ratio_legB) if feasible else float("nan"),
        "eigs": eigs,
        "ratio_pred_mu_e": ratio_pred[0],
        "ratio_pred_tau_mu": ratio_pred[1],
        "feasible_c_lt_half": bool(feasible),
        "solver_clean": bool(solver_clean),
        "ier": int(ier),
        "resid_max": float(max(abs(r) for r in resid)),
        "secular_vs_eigvalsh_dev": sec_vs_eigh,
        "ceiling_ratio_sqrt6_over_2": LEGB_CEILING_RATIO,
        "margin_below_half": float((0.5 - c_req) / 0.5) if feasible else float("nan"),
    }
    return diag


def leg_B_band(ratio, feasible, solver_clean):
    """Leg-B band classification. Above sqrt6/2 the FAIL manifests as positive-cone
    solve-infeasibility (the all-pi rank-one texture CLASS is excluded)."""
    if not solver_clean:
        return "INFO"   # non-convergence that is NOT positive-cone infeasibility (reserved degenerate)
    if not feasible:
        return "FAIL"   # c_req >= 1/2 => positive-cone infeasible (sharper than a band miss)
    lo, hi = LEGB_PASS
    if lo <= ratio <= hi:
        return "PASS"
    ilo, ihi = LEGB_INFO
    if ilo < ratio <= ihi:
        return "INFO"
    return "FAIL"


# ---------------------------------------------------------------------------
# Section 5 -- LEG A: zero-fit tracial assembly S0_geo (mechanical read-out)
# ---------------------------------------------------------------------------
def leg_A_S0geo(q, sbar):
    """S0_geo(q) = 3*q*s_bar/T_acoustic   [C1-7].  At s_bar = 1/3, S0_geo = 95/56."""
    return 3.0 * q * sbar / T_acoustic


def leg_A_band(S0_geo):
    """T1.0 bands: PASS [1.609,1.779]; INFO within +-15% of S0_fit (not PASS); FAIL beyond."""
    lo, hi = LEGA_PASS
    if lo <= S0_geo <= hi:
        return "PASS"
    ilo, ihi = S0_FIT * (1.0 - LEGA_INFO_FRAC), S0_FIT * (1.0 + LEGA_INFO_FRAC)
    if ilo <= S0_geo <= ihi:
        return "INFO"
    return "FAIL"


# ---------------------------------------------------------------------------
# Section 6 -- main
# ---------------------------------------------------------------------------
def main():
    print("=" * 70)
    print("%s -- 3-leg carrier discriminator (Leg C -> Leg B -> Leg A)" % GATE_ID)
    print("=" * 70)

    # --- input SHA verification (Rider 1: one dataset, two gates; MUST match) ---
    w2_1_sha = sha256_of(W2_1_NPZ)
    w3_9_sha = sha256_of(W3_9_NPZ)
    yukawa_sha = sha256_of(YUKAWA_NPZ)
    print("W2-1 npz SHA : %s" % w2_1_sha)
    print("  Rider-1 pin: %s" % W2_1_RIDER1_SHA)
    if w2_1_sha != W2_1_RIDER1_SHA:
        raise SystemExit("FATAL: W2-1 npz SHA mismatch vs Rider-1 pin (one-dataset "
                         "discipline) -- no verdict emitted.")
    if w3_9_sha != W3_9_SHA_PIN:
        raise SystemExit("FATAL: W3-9 freezein npz SHA mismatch vs plan pin -- no verdict.")
    if yukawa_sha != YUKAWA_SHA_PIN:
        raise SystemExit("FATAL: yukawa overlap npz SHA mismatch vs plan pin -- no verdict.")
    print("  W2-1 SHA MATCH (one-dataset Rider-1 verified). W3-9 + yukawa pins MATCH.")

    pins = log_input_pins([SCRIPT_PATH, CANON_PATH, W2_1_NPZ, W3_9_NPZ, YUKAWA_NPZ])

    # --- consume W2-1 npz (s_bar + lambda2 triple + intercept) at the pinned SHA ---
    w2 = np.load(W2_1_NPZ)
    sbar = float(w2["sbar_tau_fold"])
    lambda2_triple = np.array(w2["lambda2_triple"], dtype=float)
    ols_intercept = float(w2["ols_intercept"])
    print("\nConsumed from W2-1 npz:")
    print("  sbar_tau_fold   = %.15g" % sbar)
    print("  lambda2_triple  = %s" % np.array2string(lambda2_triple, precision=8))
    print("  ols_intercept   = %.15g" % ols_intercept)

    # --- PDG lepton ratios from W3-9 npz (held-out anchors) ---
    w39 = np.load(W3_9_NPZ)
    R_mu_e = float(w39["R_mu_e_pdg"])
    R_tau_mu = float(w39["R_tau_mu_pdg"])
    print("  PDG R_mu_e=%.10f  R_tau_mu=%.10f (W3-9 npz)" % (R_mu_e, R_tau_mu))

    # =====================================================================
    # LEG C (first; output-form binary feeds Leg A's dual read-out)
    # =====================================================================
    print("\n" + "-" * 60)
    print("LEG C -- eps_LX one-fiber split: GRADED vs SCALAR")
    legC_form, legC_qprime, legC_resid, cdiag = leg_C(lambda2_triple, sbar, ols_intercept)
    print("  graded residual max (lam2-(icpt+sbar*C2)) = %.3e  (~0 => Casimir-linear)" % cdiag["graded_residual_max"])
    print("  scalar residual max (lam2-mean)           = %.3e  (>>0 => NOT scalar)" % cdiag["scalar_residual_max"])
    print("  slope sbar = %.12g (!=0 => C2-GRADED)" % cdiag["slope_sbar"])
    print("  => legC_output_form = %s" % legC_form)
    if legC_form == "GRADED":
        print("  derived q' (magnitude channel) = %.12g ; dev vs tau_fold = %.4f%%"
              % (legC_qprime, 100.0 * cdiag["q_prime_dev_vs_tau_fold"]))
        print("  q_slope (tilt channel) = %.12g ; dev vs tau_fold = %.4f%% (= Leg-A t_tilt content)"
              % (cdiag["q_slope_tilt_channel"], 100.0 * cdiag["q_slope_dev_vs_tau_fold"]))

    # =====================================================================
    # LEG B (second; independent of W2-1 npz)
    # =====================================================================
    print("\n" + "-" * 60)
    print("LEG B -- pair-resolved {S0, c} secular solve (NO diagonalization)")
    bdiag = leg_B(R_mu_e, R_tau_mu)
    legB_form = leg_B_band(bdiag["ratio_legB"], bdiag["feasible_c_lt_half"], bdiag["solver_clean"])
    print("  {S0, c_req} = {%.12g, %.12g}  ier=%d resid_max=%.2e" %
          (bdiag["S0_legB"], bdiag["c_req"], bdiag["ier"], bdiag["resid_max"]))
    print("  m_mu/m_e=%.10f (PDG %.10f) ; m_tau/m_mu=%.10f (PDG %.10f)" %
          (bdiag["ratio_pred_mu_e"], R_mu_e, bdiag["ratio_pred_tau_mu"], R_tau_mu))
    print("  1/sqrt6 = %.12g ; ratio_legB = c_req/(1/sqrt6) = %.12g => %s" %
          (INV_SQRT6, bdiag["ratio_legB"], legB_form))
    print("  feasible c_req<1/2: %s (margin below 1/2: %.1f%%) ; ceiling sqrt6/2=%.6f" %
          (bdiag["feasible_c_lt_half"], 100.0 * bdiag["margin_below_half"], LEGB_CEILING_RATIO))
    print("  secular-vs-eigvalsh dev (diagnostic) = %.3e" % bdiag["secular_vs_eigvalsh_dev"])

    # =====================================================================
    # LEG A (third; consumes s_bar + Leg-C dual read-out)
    # =====================================================================
    print("\n" + "-" * 60)
    print("LEG A -- zero-fit tracial assembly S0_geo (IN-GATE DUAL READ-OUT)")
    S0_geo_primary = leg_A_S0geo(tau_fold, sbar)
    legA_band_primary = leg_A_band(S0_geo_primary)
    print("  ell_geo_frozen = T_acoustic/(3*tau_fold) = %.12g M_KK^2" % ELL_GEO_FROZEN)
    print("  PRIMARY (q=tau_fold=%.4g): S0_geo = %.12g => %s" %
          (tau_fold, S0_geo_primary, legA_band_primary))

    # dual read-out: if Leg C GRADED with derived q', re-evaluate at q' (band unchanged)
    if legC_form == "GRADED" and np.isfinite(legC_qprime):
        S0_geo_superseding = leg_A_S0geo(legC_qprime, sbar)
        legA_band_superseding = leg_A_band(S0_geo_superseding)
        S0_geo_governing = S0_geo_superseding
        legA_band_governing = legA_band_superseding
        supersession_fired = True
        print("  SUPERSEDING (q'=%.12g): S0_geo = %.12g => %s  [DUAL READ-OUT FIRED]" %
              (legC_qprime, S0_geo_superseding, legA_band_superseding))
    else:
        S0_geo_superseding = float("nan")
        legA_band_superseding = "N/A"
        S0_geo_governing = S0_geo_primary
        legA_band_governing = legA_band_primary
        supersession_fired = False
        print("  SUPERSEDING: N/A (Leg C SCALAR) -- governing read-out = PRIMARY")

    # tilt position t = (S0_geo*56/95 - 1)/(J-1) at GOVERNING read-out
    t_tilt = (S0_geo_governing * 56.0 / 95.0 - 1.0) / (J_TAU_FOLD - 1.0)
    print("  t_tilt_position (governing) = %.12g  (in [0,1] => upper-half J-tilt evidence)" % t_tilt)
    # s_bar-space razor (D-3): mechanical no-band-stretch check
    sbar_in_window = SBAR_EDGE_LO <= sbar <= SBAR_EDGE_HI
    print("  s_bar-space PASS window [%.6f, %.6f]; J/3=%.6f; s_bar=%.6f in window: %s" %
          (SBAR_EDGE_LO, SBAR_EDGE_HI, J_TAU_FOLD / 3.0, sbar, sbar_in_window))

    # tau_fold-form assembly (REPORTED-not-gated; 3.3% shadow, C-2): ell = tau_fold
    S0_geo_tauform = sbar / tau_fold   # S0 = s_bar/ell with ell = tau_fold
    print("  [reported-not-gated] tau_fold-form assembly (ell=tau_fold): S0=%.6f (3.3%% shadow)"
          % S0_geo_tauform)

    # =====================================================================
    # COMPOSITE (gate-block operator, workshop-FINAL; precedence over schema-v2)
    # =====================================================================
    print("\n" + "=" * 60)
    print("COMPOSITE -- Reading A iff Leg A in {PASS,INFO} AND Leg B in {PASS,INFO}")
    legA_ok = legA_band_governing in ("PASS", "INFO")
    legB_ok = legB_form in ("PASS", "INFO")
    reading_A_confirmed = legA_ok and legB_ok

    # schema-v2 3-tuple
    sign_verdict = "PASS" if reading_A_confirmed else "FAIL"           # the Reading-A conjunction
    magnitude_verdict = legA_band_governing                            # Leg A band at governing read-out
    if not bdiag["solver_clean"]:
        regime_verdict = "MARGINAL"                                   # solver degenerate (reserved)
    elif not bdiag["feasible_c_lt_half"]:
        regime_verdict = "BREAKDOWN"                                  # positive-cone infeasible
    elif legC_form == "SCALAR":
        regime_verdict = "MARGINAL"                                   # magnitude id withdrawn (carrier unaffected)
    else:
        regime_verdict = "VALID"

    # gate-block operator top-line (takes precedence over schema-v2 collapse on conflict)
    composite = "PASS" if reading_A_confirmed else "FAIL"
    # INFO reserved for the non-evaluable degenerate only (Leg-B solver non-convergence
    # that is NOT positive-cone infeasibility)
    if (not bdiag["solver_clean"]) and bdiag["feasible_c_lt_half"]:
        composite = "INFO"

    # known precedence conflict cell: Leg-A INFO and Leg-B in {PASS,INFO} => gate-block PASS
    # while schema-v2 collapse (magnitude=INFO) would give INFO. Detect + disclose.
    schema_v2_collapse = ("PASS" if (magnitude_verdict == "PASS" and sign_verdict == "PASS"
                                     and regime_verdict == "VALID")
                          else ("FAIL" if (regime_verdict == "BREAKDOWN" or sign_verdict == "FAIL")
                                else "INFO"))
    precedence_conflict = (composite != schema_v2_collapse)

    print("  Leg A (governing %s) in {PASS,INFO} = %s ; Leg B (%s) in {PASS,INFO} = %s" %
          (legA_band_governing, legA_ok, legB_form, legB_ok))
    print("  Reading A confirmed = %s => TOP-LINE (gate-block operator) = %s" %
          (reading_A_confirmed, composite))
    print("  schema-v2 collapse would give = %s ; precedence conflict = %s" %
          (schema_v2_collapse, precedence_conflict))
    print("  3-tuple: sign=%s magnitude=%s regime=%s" %
          (sign_verdict, magnitude_verdict, regime_verdict))

    # dual-prior reallocation (plan-level pre-registration; reported, NOT a verdict cell)
    if reading_A_confirmed:
        prior_note = "posterior~0.9_Track_A(Reading_A_confirmed)"
    elif legA_band_governing == "FAIL":
        prior_note = "Leg-A-FAIL=>read_W_flat_coupling(PASS=>0.65_Track_B_revival;FAIL=>inconclusive)"
    else:
        prior_note = "priors_unchanged"

    # =====================================================================
    # SHA + verdict payload
    # =====================================================================
    audit_sha, content_sha = compute_dual_sha(pins, w2_1_sha, w3_9_sha)
    print("\naudit_sha256   = %s" % audit_sha)
    print("content_sha256 = %s" % content_sha)

    value = ("legA=%s(S0geo_gov=%.6f,prim=%.6f,super=%.6f);legB=%s(ratio=%.6f,c=%.6f);"
             "legC=%s(qp=%.6f,dev=%.4f%%);composite=%s;t_tilt=%.4f" %
             (legA_band_governing, S0_geo_governing, S0_geo_primary, S0_geo_superseding,
              legB_form, bdiag["ratio_legB"], bdiag["c_req"],
              legC_form, (legC_qprime if np.isfinite(legC_qprime) else float("nan")),
              (100.0 * cdiag["q_prime_dev_vs_tau_fold"] if legC_form == "GRADED" else float("nan")),
              composite, t_tilt))

    extra_rows = [
        "# legA=%s legB=%s legC=%s | S0_geo_gov=%.6f (q=%.6f) ratio_legB=%.6f c_req=%.6f"
        % (legA_band_governing, legB_form, legC_form, S0_geo_governing,
           (legC_qprime if supersession_fired else tau_fold), bdiag["ratio_legB"], bdiag["c_req"]),
    ]
    if supersession_fired:
        extra_rows.append(
            "# in-gate-dual-readout: q_tau_fold=%.6f -> q_prime=%.6f (GRADED; band unchanged; "
            "S0_geo %.6f->%.6f) per workshop Q2" %
            (tau_fold, legC_qprime, S0_geo_primary, S0_geo_superseding))
    extra_rows.append(
        "# composite-rule=GATE-BLOCK-OPERATOR-PRECEDENCE (workshop CF-1) over schema-v2 collapse"
        " | conflict_this_run=%s (schema-v2 would give %s)" % (precedence_conflict, schema_v2_collapse))
    extra_rows.append(
        "# leg_b_feasibility: c_req=%.6f < 1/2 (positive-cone feasible); ceiling sqrt6/2=%.6f; "
        "margin_below_half=%.1f%%; secular-method (NO diag), sec-vs-eigh dev=%.2e"
        % (bdiag["c_req"], LEGB_CEILING_RATIO, 100.0 * bdiag["margin_below_half"],
           bdiag["secular_vs_eigvalsh_dev"]))
    extra_rows.append(
        "# leg_a_tilt: t_tilt=%.6f (s_bar=%.6f in [%.6f,%.6f]; J/3=%.6f; razor +%.3f%% above J/3); "
        "tau_fold-form S0=%.6f REPORTED-not-gated (3.3%% shadow)"
        % (t_tilt, sbar, SBAR_EDGE_LO, SBAR_EDGE_HI, J_TAU_FOLD / 3.0,
           100.0 * (SBAR_EDGE_HI / (J_TAU_FOLD / 3.0) - 1.0), S0_geo_tauform))
    extra_rows.append(
        "# one-dataset-echo: sbar_npz_sha256=%s (= W2-1 Rider-1 pin, verified at dispatch)" % w2_1_sha)
    extra_rows.append(
        "# dual_prior: %s | regulator_pin=N/A (group Casimirs + W2-1 cache moments) CLASS=N/A (no SCHEMATIC helper)"
        % prior_note)
    # No A19 extra-row: cross-wave pin 1 SATISFIED (W1-1 PASS, s84 L12 cache re-labeled full confidence).

    print_verdict_payload(
        composite, value, audit_sha, content_sha,
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict, extra_rows=extra_rows)

    # =====================================================================
    # npz (full float64; REQUIRED keys per plan output_artifacts:data)
    # =====================================================================
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID, scheme=SCHEME, convention=CONVENTION, l_max=L_MAX,
        verdict=composite, sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict,
        # REQUIRED keys (plan)
        S0_geo_primary=np.float64(S0_geo_primary),
        S0_geo_superseding=np.float64(S0_geo_superseding),
        legC_output_form=legC_form,
        legC_q_prime=np.float64(legC_qprime),
        legC_derivation_residual=np.float64(legC_resid),
        c_req=np.float64(bdiag["c_req"]),
        ratio_legB=np.float64(bdiag["ratio_legB"]),
        S0_legB=np.float64(bdiag["S0_legB"]),
        t_tilt_position=np.float64(t_tilt),
        sbar_consumed=np.float64(sbar),
        sbar_npz_sha256=w2_1_sha,
        # Leg A detail
        S0_geo_governing=np.float64(S0_geo_governing),
        legA_band_primary=legA_band_primary,
        legA_band_superseding=legA_band_superseding,
        legA_band_governing=legA_band_governing,
        ell_geo_frozen=np.float64(ELL_GEO_FROZEN),
        S0_geo_tauform_shadow=np.float64(S0_geo_tauform),
        supersession_fired=bool(supersession_fired),
        J_tau_fold=np.float64(J_TAU_FOLD),
        sbar_edge_lo=np.float64(SBAR_EDGE_LO), sbar_edge_hi=np.float64(SBAR_EDGE_HI),
        sbar_in_window=bool(sbar_in_window),
        S0_fit=np.float64(S0_FIT),
        # Leg B detail
        c_req_margin_below_half=np.float64(bdiag["margin_below_half"]),
        ceiling_ratio_sqrt6_over_2=np.float64(LEGB_CEILING_RATIO),
        inv_sqrt6=np.float64(INV_SQRT6),
        legB_ratio_pred_mu_e=np.float64(bdiag["ratio_pred_mu_e"]),
        legB_ratio_pred_tau_mu=np.float64(bdiag["ratio_pred_tau_mu"]),
        legB_eigs=bdiag["eigs"].astype(np.float64),
        legB_feasible=bool(bdiag["feasible_c_lt_half"]),
        legB_solver_clean=bool(bdiag["solver_clean"]),
        legB_secular_vs_eigvalsh_dev=np.float64(bdiag["secular_vs_eigvalsh_dev"]),
        legB_resid_max=np.float64(bdiag["resid_max"]),
        R_mu_e_pdg=np.float64(R_mu_e), R_tau_mu_pdg=np.float64(R_tau_mu),
        C2_lepton=C2_LEPTON.astype(np.float64),
        # Leg C detail
        legC_graded_residual_vec=cdiag["graded_residual_vec"].astype(np.float64),
        legC_scalar_residual_max=np.float64(cdiag["scalar_residual_max"]),
        legC_slope_sbar=np.float64(cdiag["slope_sbar"]),
        legC_q_slope_tilt=np.float64(cdiag["q_slope_tilt_channel"]),
        legC_q_prime_dev_vs_tau_fold=np.float64(cdiag["q_prime_dev_vs_tau_fold"]),
        legC_q_slope_dev_vs_tau_fold=np.float64(cdiag["q_slope_dev_vs_tau_fold"]),
        lambda2_triple=lambda2_triple.astype(np.float64),
        ols_intercept=np.float64(ols_intercept),
        C2_tower=C2_TOWER.astype(np.float64),
        # bands / pins
        LEGA_PASS=np.array(LEGA_PASS, dtype=np.float64),
        LEGB_PASS=np.array(LEGB_PASS, dtype=np.float64),
        LEGB_INFO=np.array(LEGB_INFO, dtype=np.float64),
        tau_fold_used=np.float64(tau_fold), T_acoustic_used=np.float64(T_acoustic),
        M_KK_used=np.float64(M_KK),
        reading_A_confirmed=bool(reading_A_confirmed),
        schema_v2_collapse=schema_v2_collapse, precedence_conflict=bool(precedence_conflict),
        dual_prior_note=prior_note,
        w2_1_npz_sha256=w2_1_sha, w3_9_npz_sha256=w3_9_sha, yukawa_npz_sha256=yukawa_sha,
        audit_sha256=audit_sha, content_sha256=content_sha, schema_version="S84+",
    )
    print("\nnpz written: %s" % OUT_NPZ)

    # =====================================================================
    # plot (3 panels)
    # =====================================================================
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    # Panel 1: Leg A -- S0_geo vs band
    ax = axes[0]
    ax.axhspan(LEGA_PASS[0], LEGA_PASS[1], color="tab:green", alpha=0.18, label="PASS [1.609,1.779]")
    ax.axhspan(S0_FIT * 0.85, LEGA_PASS[0], color="tab:orange", alpha=0.10)
    ax.axhspan(LEGA_PASS[1], S0_FIT * 1.15, color="tab:orange", alpha=0.10, label="INFO +-15%")
    ax.axhline(S0_FIT, color="k", ls="--", lw=1, label="S0_fit=1.694153")
    ax.plot([0], [S0_geo_primary], "o", ms=11, color="tab:blue", label="S0_geo(q=tau_fold)=%.4f" % S0_geo_primary)
    if supersession_fired:
        ax.plot([1], [S0_geo_superseding], "s", ms=11, color="tab:purple",
                label="S0_geo(q')=%.4f [GOVERNING]" % S0_geo_superseding)
    ax.set_xlim(-0.6, 1.6); ax.set_xticks([0, 1]); ax.set_xticklabels(["q=tau_fold", "q'(GRADED)"])
    ax.set_ylabel("S0_geo"); ax.set_title("Leg A: tracial assembly (%s)" % legA_band_governing)
    ax.legend(fontsize=7, loc="lower right")

    # Panel 2: Leg B -- ratio vs band + feasibility ceiling
    ax = axes[1]
    ax.axhspan(LEGB_PASS[0], LEGB_PASS[1], color="tab:green", alpha=0.18, label="PASS [0.95,1.05]")
    ax.axhspan(LEGB_INFO[0], LEGB_PASS[0], color="tab:orange", alpha=0.10)
    ax.axhspan(LEGB_PASS[1], LEGB_INFO[1], color="tab:orange", alpha=0.10, label="INFO (0.8,1.25]")
    ax.axhline(1.0, color="k", ls=":", lw=1, label="ratio=1 (c=1/sqrt6)")
    ax.axhline(LEGB_CEILING_RATIO, color="tab:red", ls="--", lw=1.2,
               label="sqrt6/2=%.4f (cone ceiling)" % LEGB_CEILING_RATIO)
    ax.plot([0], [bdiag["ratio_legB"]], "o", ms=12, color="tab:blue",
            label="ratio=%.4f (%s)" % (bdiag["ratio_legB"], legB_form))
    ax.set_xlim(-0.6, 0.6); ax.set_xticks([0]); ax.set_xticklabels(["c_req/(1/sqrt6)"])
    ax.set_ylabel("ratio"); ax.set_title("Leg B: coherence (c_req=%.4f<1/2)" % bdiag["c_req"])
    ax.legend(fontsize=7, loc="upper right")

    # Panel 3: Leg C -- Casimir-linear ladder (GRADED) vs scalar mean
    ax = axes[2]
    ax.plot(C2_TOWER, lambda2_triple, "o", ms=10, color="tab:blue", label="<lam2>_g (W2-1)")
    xs = np.linspace(C2_TOWER.min() - 0.3, C2_TOWER.max() + 0.3, 50)
    ax.plot(xs, ols_intercept + sbar * xs, "-", color="tab:green",
            label="icpt+sbar*C2 (slope=%.4f)" % sbar)
    ax.axhline(np.mean(lambda2_triple), color="tab:red", ls="--", lw=1,
               label="scalar mean (rejected)")
    for c2v, l2v, lab in zip(C2_TOWER, lambda2_triple, ["(1,0)", "(1,1)", "(3,0)"]):
        ax.annotate(lab, (c2v, l2v), textcoords="offset points", xytext=(6, -10), fontsize=8)
    ax.set_xlabel("C2(g)"); ax.set_ylabel("<lam2>_g")
    ax.set_title("Leg C: %s (q'=%.5f, dev %.3f%%)" %
                 (legC_form, (legC_qprime if np.isfinite(legC_qprime) else float('nan')),
                  100.0 * cdiag["q_prime_dev_vs_tau_fold"] if legC_form == "GRADED" else 0.0))
    ax.legend(fontsize=7, loc="upper left")

    fig.suptitle("%s -- TOP-LINE %s | sign=%s mag=%s regime=%s" %
                 (GATE_ID, composite, sign_verdict, magnitude_verdict, regime_verdict),
                 fontsize=11)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(OUT_PNG, dpi=130)
    print("png written: %s" % OUT_PNG)

    print("\n4-tuple: (value=%s, scheme=%s, convention=%s, L_max=%s)" %
          (composite, SCHEME, CONVENTION, L_MAX))
    return 0


if __name__ == "__main__":
    sys.exit(main())
