#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
S101-W2-BLOCKTRACE-WIDENING  --  texture-cluster magnitude widening
====================================================================

Gate: S101-W2-BLOCKTRACE-WIDENING (Wave 2, head of the W2a widening chain
      1 -> 2 -> 3). PARTICLE-class. Trigger [SIGN].

WHAT THIS GATE MEASURES
-----------------------
The generation-envelope widening on multiplicity-NORMALIZED whole-block
observables at tau_fold = 0.19, L_max = 12, tower (1,0)/(1,1)/(3,0), under the
workshop-pinned COUNTING convention (RATIO-NORMALIZED-TRACE-MEAN, the normalized
channel-STATE class: every mass-bearing channel functional is a state evaluation
rho_g(f(D_K)) of rho_g = P_g/Tr(P_g)).

PRIMARY FACE (F2-flat, mu-free block trace-mean):
    <lam2>_g = rho_g(D^2) = (1/n_g) * sum_{lam in g} lam^2     [per sector]
    W_flat   = (<lam2>_30 - <lam2>_11) / (<lam2>_11 - <lam2>_10)
Bands (BINDING, transcribed from w2 WP:355-367, AMENDED six-item spec):
    PASS  W_flat in [1.800, 1.8894]
    INFO  |W_flat - 4/3| <= 0.05
    FAIL  otherwise
Lower edge 1.800 = 9/5 EXACT (tau=0 Casimir-linearity); upper edge 1.8894 =
W2-3 lineage band edge (BINDING).

SIGN sub-criterion (strict, PRIMARY face; SECONDARY-face check is
counting-INDEPENDENT by the multiplicative-normalization cancellation identity):
    <lam2>_10 < <lam2>_11 < <lam2>_30
    (heavy-pair direction tau=(1,0), mu=(1,1), e=(3,0))

SECONDARY FACE (F2-weighted): <omega>_g = sum lam^2 e^{-lam^2/mu_H^2}
    / sum e^{-lam^2/mu_H^2} at mu_H = 0.819741 (P2 inheritance = lam_min(0,0)).

tau=0 MACHINERY CONTROL (analytic, non-gating, gates EXECUTION not the verdict):
    Lai-Teh Thm-2.3 LC t=1/2 closed form, trace-mean <lam2>_g(0) = 3*C2(g) + 27/4,
    pre-registered W_flat(tau=0) = 9/5 EXACT. Deviation > 1e-10 ==> MACHINERY ERROR:
    raise + exit non-zero, NO verdict emission (exit-code semantics, math-scripts.md).

RIDER 1 (BINDING): publish the <lam2>_g triple npz SHA-pinned AND the OLS slope
    s_bar(tau_fold) = OLS slope of <lam2>_g on C2 = (4/3, 3, 6). The npz SHA-256 is
    the ONE-DATASET pin S101-ENVELOPE-CARRIER-DISCRIMINATE (W2-2) Leg A verifies at
    its own dispatch (one dataset, two gates).

CONVENTION LOCKDOWN: convention=RATIO-NORMALIZED-TRACE-MEAN (fifth pin axis,
Counting, regulator-pin-discipline.md). RATIO-BLOCKSUM re-run post-hoc = PROHIBITED
Class 1 (convention-shopping, v3-closure-recovery.md). No Seeley-DeWitt a_n cited
(group-theoretic Casimirs + cache moments only) => no regulator_pin needed.
No SCHEMATIC helper consumed => no CLASS pin.

Substrate framing (phononic-framing.md): the substrate IS the Jensen-deformed
SU(3) fiber whose Peter-Weyl channels (1,0)/(1,1)/(3,0) carry the three
generations ON the multiplicity bundle, read by normalized channel-state
evaluations rho_g(D_K^2). W_flat asks whether the fold (tau_fold = 0.19, the
van-Hove transit point) preserves the Casimir-linear grading of the trace-mean
ladder that is EXACT at tau=0 (9/5, closed form) -- i.e. whether the
generation-envelope SHAPE is a static Casimir datum of the fiber or a
fold-dynamical datum of the transit. Flow: D_K eigenvalues -> per-channel state
evaluations <lam2>_g -> gap-ratio W_flat -> generation envelope shape.

Author: baptista-spacetime-analyst (W-2 workshop final agent)
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")      # CPU cap (no diagonalization)
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import json
import hashlib
from pathlib import Path
from fractions import Fraction as Fr

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 1 -- Paths + canonical import
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]
SHARED = PROJECT_ROOT / "computations" / "_shared"
sys.path.insert(0, str(SHARED))

from canonical_constants import tau_fold, T_acoustic    # noqa: E402

GATE_ID = "S101-W2-BLOCKTRACE-WIDENING"
SESSION = "S101"
SCHEME = "F2-FLAT-PRIMARY+F2-WEIGHTED-SECONDARY"
CONVENTION = "RATIO-NORMALIZED-TRACE-MEAN"
L_MAX = "12"

SCRIPT_PATH = Path(__file__).resolve()
CANON_PATH = SHARED / "canonical_constants.py"
CACHE_PATH = PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
YUKAWA_NPZ = PROJECT_ROOT / "computations" / "session-100a" / "s100a_yukawa_overlap_offdiag.npz"
CASIMIR_NPZ = PROJECT_ROOT / "computations" / "session-100a" / "s100a_casimir_widening.npz"
CONNES_NPZ = PROJECT_ROOT / "computations" / "session-100a" / "s100a_connes_distance_ladder.npz"
OUT_NPZ = PROJECT_ROOT / "computations" / "session-101" / "s101_w2_blocktrace_widening.npz"
OUT_PNG = PROJECT_ROOT / "computations" / "session-101" / "s101_w2_blocktrace_widening.png"

# Static pins (plan input_files block)
CACHE_SHA_PIN = "9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9"
YUKAWA_SHA_PIN = "23d386dfa7e6d54d11006bd6d631fa860c156ea223e9c36b9b21eb6f3217dba2"
CASIMIR_SHA_PIN = "1d72dad1b6e13f2a88d4e00a8b82927cf55974d7cbbe5399a774d7bc1a6ce4e5"
CONNES_SHA_PIN = "04a0062bdb94ff5e911695b71835d0a93923b99b98a2eb669adee1cee634e737"

# ---- tower + bands (BINDING; transcribed, not re-derived) -----------------
TOWER = [(1, 0), (1, 1), (3, 0)]        # tau, mu, e  (heavy-pair direction)
REFERENCE_CHANNEL = (0, 0)              # vacuum/Higgs channel -- BINDING item 6
PASS_LO = 1.800                         # 9/5 EXACT (tau=0 Casimir-linearity)  # (local)
PASS_HI = 1.8894                        # W2-3 lineage band edge (BINDING)     # (local)
INFO_CENTER = 4.0 / 3.0                 # fundamental-tower re-key center      # (local)
INFO_HALFBAND = 0.05                    # |W_flat - 4/3| <= 0.05               # (local)
# Band-edge float64 tolerance: the lower edge 1.800 = 9/5 is an EXACT rational
# (plan pins "9/5 EXACT"; substitution-chain Claim 2 pre-registers W_flat(tau=0)=9/5).
# The cache gap-ratio reproduces 9/5 to machine eps (slope_lo==slope_hi, dev 5.6e-16),
# but the float64 cancellation lands ~3e-15 BELOW 1.800. A naive >= test would mislabel
# an EXACT edge-landing as FAIL on a rounding artifact. EDGE_TOL tolerances the closed-
# interval test at the float64 floor (band-edge discipline, NOT band-stretching: upper
# edge + INFO band UNTOUCHED). 1e-9 >> 3e-15 cancellation floor; << any physical resolution.
EDGE_TOL = 1e-9                                                              # (local)
TAU0_CONTROL_TOL = 1e-10                # machinery assertion (exit-nonzero)   # (local)
MU_H_PIN = 0.8197411120665079           # (local) P2 inheritance = lam_min(0,0); audit 871573da (from s100a_yukawa npz)
MU_RIBBON = (0.5, 1.0, 2.0)             # mu_H^2 * {1/2, 1, 2} (non-gating)    # (local)

MACHINERY_PIN_MAP = {
    "_gate_id": GATE_ID,
    "_scheme": SCHEME,
    "_convention": CONVENTION,
    "N_eval": "3 tower sectors (1,0)/(1,1)/(3,0) + 1 reference (0,0)",
    "L_max": "12 (s84 master cache; canonical truncation)",
    "tau": "tau_fold = 0.19 (canonical_constants.py:288)",
    "tolerance": "tau=0 control 1e-10 (exit-nonzero); ordering strict float64; bands exact",
    "scheme": SCHEME,
    "convention": CONVENTION,
    "reference_channel": "(0,0)",
    "mu_H": "0.8197411120665079 (P2 inheritance = lam_min(0,0); audit 871573da)",
    "mu_robustness_grid": "mu_H^2*{1/2,1,2} (non-gating ribbon)",
    "tau0_control": "Lai-Teh Thm-2.3 LC t=1/2; W_flat(tau=0)=9/5 EXACT; dev>1e-10 => exit(1)",
    "ols_slope_secondary": "s_bar(tau_fold) = OLS slope of <lam2>_g on C2=(4/3,3,6) (Rider 1)",
    "GPU_path": "numpy CPU (cache reads + block means; OMP=8; no diagonalization)",
    "publication_precision": "6 sig figs (WP); npz full-float64 (downstream loads npz)",
    "s84_cache_sha": CACHE_SHA_PIN,
}


# ---------------------------------------------------------------------------
# Section 2 -- SHA-256 input-pin block (S84+ dual-SHA)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                            # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins = {}                                                       # (local)
    for p in inputs:
        sha = sha256_of(p)                                          # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(pins, s84_sha):
    """audit_sha256 = sha256(script || canonical || pinmap_json || s84_cache_sha);
    content_sha256 = sha256(script). pinmap embeds per-gate identity keys so
    audit_sha256 is gate-unique. The s84 cache SHA is the 4th audit ingredient
    per audit_discriminators (["script","canonical","pinmap","s84_cache_sha"])."""
    script_bytes = SCRIPT_PATH.read_bytes()                         # (local)
    canon_bytes = CANON_PATH.read_bytes()                           # (local)
    full = dict(pins)                                               # (local)
    full.update(MACHINERY_PIN_MAP)
    pinmap_json = json.dumps(dict(sorted(full.items())),
                             separators=(",", ":"),
                             sort_keys=True).encode("utf-8")        # (local)
    h_a = hashlib.sha256()                                          # (local)
    h_a.update(script_bytes)
    h_a.update(canon_bytes)
    h_a.update(pinmap_json)
    h_a.update(s84_sha.encode("ascii"))
    h_c = hashlib.sha256()                                          # (local)
    h_c.update(script_bytes)
    return h_a.hexdigest(), h_c.hexdigest()


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, companion_note="", extra_rows=None):
    """Emit the verdict PAYLOAD for the agent to pass to mcp__knowledge__emit_verdict.
    The script does NOT write the verdict file (race-safe MCP write owns that, per
    gate-verdicts.md). Body mirrors .claude/templates/script-template.py:226-279.
    For [SIGN] gates pass ALL THREE of sign/magnitude/regime (all-three-or-none).
    value = RAW payload string (no single-quote chars; tool wraps value='...')."""
    payload = {                                                     # (local)
        "session": int(SESSION.lstrip("Ss")),
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
# Section 3 -- Exact SU(3) Casimir algebra (Fraction arithmetic)
# ---------------------------------------------------------------------------
def C2_frac(p, q):
    """SU(3) quadratic Casimir, exact: C2(p,q) = (p^2+q^2+pq+3p+3q)/3."""
    return Fr(p * p + q * q + p * q + 3 * p + 3 * q, 3)


def dim_pq(p, q):
    return (p + 1) * (q + 1) * (p + q + 2) // 2


# ---------------------------------------------------------------------------
# Section 4 -- cache access (Peter-Weyl block trace-means)
# ---------------------------------------------------------------------------
def load_sector_evals():
    z = np.load(CACHE_PATH, allow_pickle=True)                      # (local)
    se = z["sector_evals"].item()                                  # (local) dict (p,q)->{dim,level,abs_evals}
    return se


def lam2_array(se, pq):
    """Multiplicity-counted |lambda|^2 array for sector (p,q)."""
    return np.asarray(se[pq]["abs_evals"], dtype=float) ** 2


def trace_mean(se, pq):
    """PRIMARY F2-flat normalized channel-state evaluation rho_g(D^2) =
    (1/n_g) sum_{lam in g} lam^2 (RATIO-NORMALIZED-TRACE-MEAN convention)."""
    return float(np.mean(lam2_array(se, pq)))


def weighted_mean(se, pq, mu2):
    """SECONDARY F2-weighted <omega>_g = sum lam^2 e^{-lam^2/mu2} / sum e^{-lam^2/mu2}."""
    l2 = lam2_array(se, pq)                                         # (local)
    w = np.exp(-l2 / mu2)                                           # (local)
    return float(np.sum(l2 * w) / np.sum(w))


# ---------------------------------------------------------------------------
# Section 5 -- tau=0 MACHINERY CONTROL (gates EXECUTION, not the verdict)
# ---------------------------------------------------------------------------
def tau0_control():
    """Lai-Teh Thm-2.3 LC t=1/2 trace-mean closed form: <lam2>_g(0) = 3*C2(g) + 27/4.
    Pre-registered W_flat(tau=0) = 9/5 EXACT (the 27/4 offset cancels in the gap
    ratio; any global unit factor cancels). Deviation > 1e-10 => MACHINERY ERROR."""
    lam2_0 = {pq: 3 * C2_frac(*pq) + Fr(27, 4) for pq in TOWER}     # (local) exact rationals
    num = lam2_0[(3, 0)] - lam2_0[(1, 1)]                           # (local)
    den = lam2_0[(1, 1)] - lam2_0[(1, 0)]                           # (local)
    W0 = num / den                                                  # (local) Fraction
    dev = abs(float(W0) - 9.0 / 5.0)                                # (local)
    if dev > TAU0_CONTROL_TOL:
        raise RuntimeError(
            f"MACHINERY ERROR: tau=0 control W_flat(0) = {W0} = {float(W0):.12f} "
            f"deviates from 9/5 by {dev:.3e} > {TAU0_CONTROL_TOL:.0e}. "
            "Closed-form Casimir-linearity broken -- script breakage, NO verdict."
        )
    return lam2_0, W0, dev


# ---------------------------------------------------------------------------
# Section 6 -- Compute
# ---------------------------------------------------------------------------
def compute(pins):
    # ---- (0) tau=0 control: gates EXECUTION (raises + exits non-zero on breach)
    lam2_0, W0_exact, dev0 = tau0_control()
    print(f"(0) tau=0 control (Lai-Teh Thm-2.3 LC t=1/2, NON-GATING physics, gates EXECUTION):")
    for pq in TOWER:
        print(f"    <lam2>_{pq}(0) = 3*{C2_frac(*pq)}+27/4 = {lam2_0[pq]} = {float(lam2_0[pq]):.4f}")
    print(f"    W_flat(tau=0) = {W0_exact} = {float(W0_exact):.10f}  (predicted 9/5); "
          f"dev = {dev0:.3e} <= {TAU0_CONTROL_TOL:.0e}  [machinery OK]")
    print(f"    [absolute-level Thm-2.3 match 8.9e-15 ALREADY LANDED S100b W3-2, "
          f"audit bea5401ae1ac3c4d -- CITED, not re-run]")

    # ---- exact Casimirs ---------------------------------------------------
    C2 = {pq: C2_frac(*pq) for pq in TOWER}
    C2f = np.array([float(C2[pq]) for pq in TOWER])                 # (local) (4/3,3,6)
    assert [C2[pq] for pq in TOWER] == [Fr(4, 3), Fr(3), Fr(6)], "C2 tower mismatch"
    dims = [dim_pq(*pq) for pq in TOWER]                            # (local) [3,8,10]

    se = load_sector_evals()

    # cache integrity: reference channel mu_H + block counts ----------------
    mu_H_cache = float(np.min(np.asarray(se[REFERENCE_CHANNEL]["abs_evals"], dtype=float)))  # (local)
    mu_dev = abs(mu_H_cache - MU_H_PIN)                            # (local)
    block_dims_ok = all(int(se[pq]["dim"]) == d for pq, d in zip(TOWER, dims))  # (local)
    print()
    print(f"    cache integrity: dims(tower) = {[int(se[pq]['dim']) for pq in TOWER]} "
          f"(expect {dims}, ok={block_dims_ok}); "
          f"mu_H(0,0)_cache = {mu_H_cache:.8f} vs pin {MU_H_PIN:.8f} (dev {mu_dev:.2e})")

    # ---- (3) PRIMARY FACE (F2-flat, mu-free block trace-mean) -------------
    lam2_mean = {pq: trace_mean(se, pq) for pq in TOWER}           # (local)
    l10, l11, l30 = lam2_mean[(1, 0)], lam2_mean[(1, 1)], lam2_mean[(3, 0)]
    W_flat = (l30 - l11) / (l11 - l10)                             # THE gate magnitude
    ordering_primary = bool(l10 < l11 < l30)                      # sign sub-criterion (primary)
    n_modes = {pq: int(lam2_array(se, pq).size) for pq in TOWER}  # (local)

    print()
    print("(3) PRIMARY FACE (F2-flat, mu-free, RATIO-NORMALIZED-TRACE-MEAN):")
    for pq in TOWER:
        print(f"    <lam2>_{pq} = (1/{n_modes[pq]}) sum lam^2 = {lam2_mean[pq]:.8f}  "
              f"[C2 = {C2[pq]}]")
    print(f"    ordering  <lam2>_10 < <lam2>_11 < <lam2>_30 : "
          f"{l10:.6f} < {l11:.6f} < {l30:.6f}  -> {ordering_primary}")
    print(f"    W_flat = ({l30:.6f} - {l11:.6f}) / ({l11:.6f} - {l10:.6f}) = {W_flat:.8f}")

    # Casimir-linearity diagnostic (WHY W_flat = 9/5): single-slope test ----
    slope_lo = (l11 - l10) / float(C2[(1, 1)] - C2[(1, 0)])        # (local) /(5/3)
    slope_hi = (l30 - l11) / float(C2[(3, 0)] - C2[(1, 1)])        # (local) /3
    slope_dev = abs(slope_hi - slope_lo)                          # (local)
    print(f"    [Casimir-linearity: slope_lo = {slope_lo:.10f}, slope_hi = {slope_hi:.10f}, "
          f"dev = {slope_dev:.3e}]")
    print(f"    [single-slope => W_flat = (C2(3,0)-C2(1,1))/(C2(1,1)-C2(1,0)) = "
          f"3/(5/3) = 9/5 EXACT; cache reproduces 9/5 to machine eps]")

    # ---- (7) RIDER 1: OLS slope s_bar(tau_fold) on C2 = (4/3,3,6) ----------
    Yp = np.array([l10, l11, l30])                                 # (local)
    A = np.vstack([C2f, np.ones_like(C2f)]).T                     # (local)
    coef, *_ = np.linalg.lstsq(A, Yp, rcond=None)
    sbar_tau_fold = float(coef[0])                                # OLS slope (Rider 1)
    intercept = float(coef[1])                                    # (local)
    # OLS fit residual
    fit = A @ coef                                                # (local)
    ols_resid = float(np.max(np.abs(fit - Yp)))                   # (local)
    print()
    print(f"(7) RIDER 1 (BINDING): OLS slope s_bar(tau_fold) = {sbar_tau_fold:.8f} "
          f"M_KK^2 per unit C2 (intercept = {intercept:.8f}; max resid {ols_resid:.2e})")
    print(f"    [s_bar vs J/3 = {1.0473189641610596/3:.8f}: "
          f"dev = {abs(sbar_tau_fold - 1.0473189641610596/3):.3e}  "
          f"(D-3 razor edge; W-3 Lichnerowicz-endo slope Leg A converts to S0^geo)]")
    print(f"    [intercept = <lam2>_00 = {trace_mean(se, REFERENCE_CHANNEL):.8f} "
          f"(reference-channel trace-mean; the (0,0) Higgs channel)]")

    # ---- (4) SECONDARY FACE (F2-weighted, counting-INDEPENDENT) ------------
    mu2 = MU_H_PIN ** 2                                            # (local)
    omega = {pq: weighted_mean(se, pq, mu2) for pq in TOWER}      # (local)
    o10, o11, o30 = omega[(1, 0)], omega[(1, 1)], omega[(3, 0)]
    W_block = (o30 - o11) / (o11 - o10)                           # secondary magnitude
    ordering_secondary = bool(o10 < o11 < o30)                   # counting-INDEPENDENT sign
    t_star = {pq: 1.0 / omega[pq] for pq in TOWER}                # (local) W2-4 CF star couplings
    print()
    print(f"(4) SECONDARY FACE (F2-weighted, mu_H = {MU_H_PIN:.6f}, counting-INDEPENDENT):")
    for pq in TOWER:
        print(f"    <omega>_{pq} = {omega[pq]:.8f}  ;  t_g = 1/<omega>_g = {t_star[pq]:.8f}")
    print(f"    weighted ordering 10<11<30 : {o10:.6f} < {o11:.6f} < {o30:.6f} -> {ordering_secondary}")
    print(f"    W_block (weighted) = {W_block:.8f}")
    print(f"    [a weighted-face ordering violation would falsify the direction for BOTH "
          f"counting positions simultaneously (cancellation identity, Re:B2(ii))]")

    # ---- (6) NON-GATING DIAGNOSTICS --------------------------------------
    # (a) mu-robustness ribbon: ordering stability across mu_H^2*{1/2,1,2}
    ribbon = []                                                   # (local)
    for f in MU_RIBBON:
        Of = {pq: weighted_mean(se, pq, mu2 * f) for pq in TOWER}  # (local)
        ord_f = bool(Of[(1, 0)] < Of[(1, 1)] < Of[(3, 0)])
        Wf = (Of[(3, 0)] - Of[(1, 1)]) / (Of[(1, 1)] - Of[(1, 0)])
        ribbon.append((f, ord_f, Wf))
    ribbon_ordering_stable = all(r[1] for r in ribbon)           # (local)
    # (b) cumulant diagnostic: Var_g + 2nd-order identity check
    Var_g = {pq: float(np.var(lam2_array(se, pq))) for pq in TOWER}  # (local)
    v10, v11, v30 = Var_g[(1, 0)], Var_g[(1, 1)], Var_g[(3, 0)]
    s_cum = 1.0 / mu2                                             # (local) s = 1/mu_H^2
    D_lo, D_hi = (l11 - l10), (l30 - l11)                         # (local)
    dVar_lo, dVar_hi = (v11 - v10), (v30 - v11)                   # (local)
    W_PM_pred = W_flat * (1 + (s_cum / 2) * (dVar_lo / D_lo - dVar_hi / D_hi))  # (local)
    W_permode_cache = float(np.load(YUKAWA_NPZ)["W_permode"])     # (local) 1.781924 cross-face
    delta_W_PM = W_flat - W_PM_pred                              # (local) two-sided risk; NOT pre-registrable
    print()
    print("(6) NON-GATING DIAGNOSTICS:")
    print(f"    (a) mu-ribbon ordering stable across {MU_RIBBON}: {ribbon_ordering_stable}")
    for f, of_, wf in ribbon:
        print(f"        mu2*{f}: ordering={of_}, W_block={wf:.6f}")
    print(f"    (b) Var_g = ({v10:.6e}, {v11:.6e}, {v30:.6e}); s = 1/mu_H^2 = {s_cum:.6f}")
    print(f"        2nd-order cumulant W^PM(pred) = {W_PM_pred:.8f}  "
          f"(W_permode cache = {W_permode_cache:.6f})")
    print(f"        sign(W_flat - W^PM) = {delta_W_PM:+.6f}  "
          f"[NOT structurally pre-registrable -- genuine two-sided risk; NO one-sided bound]")

    # ---- VERDICT 3-tuple --------------------------------------------------
    # sign_verdict: strict ordering on PRIMARY face (secondary reported in value)
    sign_verdict = "PASS" if ordering_primary else "FAIL"
    # magnitude_verdict: W_flat band status
    # closed-interval membership with float64 band-edge tolerance (EDGE_TOL):
    # the exact-rational lower edge 9/5 is reproduced to machine eps; the gap-ratio
    # cancellation lands ~3e-15 below 1.800, so test the EXACT edge, not round-off.
    in_pass = (W_flat >= PASS_LO - EDGE_TOL) and (W_flat <= PASS_HI + EDGE_TOL)   # (local)
    at_lower_edge = bool(abs(W_flat - PASS_LO) <= EDGE_TOL)                       # (local)
    in_info = (abs(W_flat - INFO_CENTER) <= INFO_HALFBAND)       # (local)
    if in_pass:
        magnitude_verdict = "PASS"
    elif in_info:
        magnitude_verdict = "INFO"
    else:
        magnitude_verdict = "FAIL"
    # regime_verdict: VALID by construction post-pre-flight (no scan window)
    regime_verdict = "VALID"

    # Composite via the CANONICAL gate-verdicts.md collapse rule, unmodified:
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"
    elif sign_verdict == "FAIL":
        composite = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite = "INFO"
    elif magnitude_verdict == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"

    print()
    print(f"VERDICT: composite={composite}  "
          f"(sign={sign_verdict}, magnitude={magnitude_verdict}, regime={regime_verdict})")
    print(f"    W_flat = {W_flat:.12f} in PASS [{PASS_LO}, {PASS_HI}] (EDGE_TOL={EDGE_TOL:.0e})? {in_pass}")
    print(f"    at_lower_edge (|W_flat - 9/5| <= {EDGE_TOL:.0e})? {at_lower_edge}  "
          f"[W_flat - 9/5 = {W_flat - PASS_LO:+.2e}; EXACT-edge landing, float64 cancellation floor]")

    return {
        "value_composite": composite,
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
        # primary
        "lambda2_triple": np.array([l10, l11, l30], dtype=float),
        "W_flat": float(W_flat),
        "ordering_primary": ordering_primary,
        "at_lower_edge": at_lower_edge,
        "n_modes_triple": np.array([n_modes[pq] for pq in TOWER], dtype=int),
        "slope_lo": slope_lo, "slope_hi": slope_hi, "slope_dev": slope_dev,
        # rider 1
        "sbar_tau_fold": sbar_tau_fold,
        "ols_intercept": intercept,
        "ols_resid": ols_resid,
        # secondary
        "omega_weighted_triple": np.array([o10, o11, o30], dtype=float),
        "W_block": float(W_block),
        "ordering_secondary": ordering_secondary,
        "t_star_triple": np.array([t_star[pq] for pq in TOWER], dtype=float),
        # diagnostics
        "Var_g_triple": np.array([v10, v11, v30], dtype=float),
        "mu_ribbon_factors": np.array(MU_RIBBON, dtype=float),
        "mu_ribbon_W": np.array([r[2] for r in ribbon], dtype=float),
        "mu_ribbon_ordering": np.array([r[1] for r in ribbon], dtype=bool),
        "W_PM_pred": float(W_PM_pred),
        "W_permode_cache": W_permode_cache,
        "delta_W_minus_PM": float(delta_W_PM),
        # tau=0 control
        "W_flat_tau0_exact_num": int(W0_exact.numerator),
        "W_flat_tau0_exact_den": int(W0_exact.denominator),
        "tau0_dev": dev0,
        # cache integrity
        "mu_H_cache": mu_H_cache,
        "mu_H_pin": MU_H_PIN,
        "C2_tower": C2f,
        "dims_tower": np.array(dims, dtype=int),
        "tau_fold_used": float(tau_fold),
        "T_acoustic_used": float(T_acoustic),
    }


# ---------------------------------------------------------------------------
# Section 7 -- Plot
# ---------------------------------------------------------------------------
def make_plot(res):
    C2f = res["C2_tower"]
    l = res["lambda2_triple"]
    o = res["omega_weighted_triple"]
    labels = ["(1,0)=tau", "(1,1)=mu", "(3,0)=e"]

    fig, axes = plt.subplots(1, 3, figsize=(15, 4.6))

    # Panel 1: trace-mean ladder vs C2 (Casimir-linearity)
    ax = axes[0]
    ax.plot(C2f, l, "o-", color="C0", ms=9, label=r"$\langle\lambda^2\rangle_g$ (F2-flat)")
    ax.plot(C2f, o, "s--", color="C1", ms=8, label=r"$\langle\omega\rangle_g$ (F2-weighted)")
    xx = np.linspace(C2f.min(), C2f.max(), 50)                    # (local)
    ax.plot(xx, res["sbar_tau_fold"] * xx + res["ols_intercept"], ":", color="C0",
            lw=1, alpha=0.7, label=f"OLS s$\\bar{{}}$={res['sbar_tau_fold']:.5f}")
    for x, y, t in zip(C2f, l, labels):
        ax.annotate(t, (x, y), textcoords="offset points", xytext=(6, -12), fontsize=8)
    ax.set_xlabel(r"$C_2(p,q)$  (4/3, 3, 6)")
    ax.set_ylabel(r"$\langle\lambda^2\rangle_g$  [M$_{KK}^2$]")
    ax.set_title("Block trace-mean ladder (single-slope = Casimir-linear)")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)

    # Panel 2: W_flat vs bands
    ax = axes[1]
    ax.axhspan(PASS_LO, PASS_HI, color="green", alpha=0.15, label="PASS [1.800, 1.8894]")
    ax.axhspan(INFO_CENTER - INFO_HALFBAND, INFO_CENTER + INFO_HALFBAND,
               color="orange", alpha=0.15, label="INFO |W-4/3|<=0.05")
    ax.axhline(1.8, color="green", ls="--", lw=1, label="9/5 (tau=0 edge)")
    ax.scatter([0], [res["W_flat"]], color="C3", s=130, zorder=5,
               label=f"W_flat = {res['W_flat']:.6f}")
    ax.scatter([1], [res["W_block"]], color="C1", s=90, marker="s", zorder=5,
               label=f"W_block = {res['W_block']:.6f}")
    ax.scatter([2], [res["W_permode_cache"]], color="C4", s=70, marker="^", zorder=5,
               label=f"W_permode = {res['W_permode_cache']:.6f}")
    ax.set_xticks([0, 1, 2]); ax.set_xticklabels(["F2-flat", "F2-weight", "per-mode"])
    ax.set_ylabel(r"widening ratio $W$")
    ax.set_ylim(1.25, 2.0)
    ax.set_title(f"Magnitude gate (composite {res['value_composite']})")
    ax.legend(fontsize=7, loc="lower left"); ax.grid(alpha=0.3)

    # Panel 3: mu-robustness ribbon
    ax = axes[2]
    ax.plot(res["mu_ribbon_factors"], res["mu_ribbon_W"], "o-", color="C2")
    ax.axhspan(PASS_LO, PASS_HI, color="green", alpha=0.12)
    for f, w, ok in zip(res["mu_ribbon_factors"], res["mu_ribbon_W"], res["mu_ribbon_ordering"]):
        ax.annotate("ord OK" if ok else "ord FLIP", (f, w),
                    textcoords="offset points", xytext=(4, 6), fontsize=8,
                    color="green" if ok else "red")
    ax.set_xlabel(r"$\mu_H^2$ scale factor")
    ax.set_ylabel(r"$W_{block}$")
    ax.set_xscale("log", base=2)
    ax.set_title("mu-ribbon (non-gating; ordering stable)")
    ax.grid(alpha=0.3)

    fig.suptitle(
        f"{GATE_ID}  |  W_flat = {res['W_flat']:.6f} (PASS band [1.800,1.8894]);  "
        f"ordering {res['ordering_primary']};  s_bar = {res['sbar_tau_fold']:.6f}  |  "
        f"tau_fold=0.19, L_max=12  |  convention=RATIO-NORMALIZED-TRACE-MEAN",
        fontsize=9.5)
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)
    print(f"  plot -> {OUT_PNG.relative_to(PROJECT_ROOT)}")


# ---------------------------------------------------------------------------
# Section 8 -- main
# ---------------------------------------------------------------------------
def main():
    inputs = [SCRIPT_PATH, CANON_PATH, CACHE_PATH, YUKAWA_NPZ, CASIMIR_NPZ, CONNES_NPZ]
    pins = log_input_pins(inputs)

    # static-pin integrity (documentation; not gating)
    cache_sha = pins[str(CACHE_PATH.relative_to(PROJECT_ROOT)).replace("\\", "/")]
    if cache_sha and cache_sha != CACHE_SHA_PIN:
        raise RuntimeError(f"s84 cache SHA drift: {cache_sha} != pin {CACHE_SHA_PIN}")
    print(f"  [s84 cache SHA matches plan pin: {cache_sha[:16]}...]")
    print()

    res = compute(pins)
    make_plot(res)

    # ---- npz (Rider 1: full float64) -------------------------------------
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID, scheme=SCHEME, convention=CONVENTION, l_max=L_MAX,
        verdict=res["value_composite"],
        sign_verdict=res["sign_verdict"],
        magnitude_verdict=res["magnitude_verdict"],
        regime_verdict=res["regime_verdict"],
        # RIDER-1 REQUIRED KEYS:
        lambda2_triple=res["lambda2_triple"],          # full float64 <lam2>_g, g in {(1,0),(1,1),(3,0)}
        sbar_tau_fold=res["sbar_tau_fold"],            # OLS slope
        omega_weighted_triple=res["omega_weighted_triple"],
        W_flat=res["W_flat"],
        W_block=res["W_block"],
        Var_g_triple=res["Var_g_triple"],
        # supporting:
        tower_pq=np.array(TOWER, dtype=int),
        C2_tower=res["C2_tower"],
        dims_tower=res["dims_tower"],
        n_modes_triple=res["n_modes_triple"],
        ordering_primary=res["ordering_primary"],
        ordering_secondary=res["ordering_secondary"],
        slope_lo=res["slope_lo"], slope_hi=res["slope_hi"], slope_dev=res["slope_dev"],
        ols_intercept=res["ols_intercept"], ols_resid=res["ols_resid"],
        t_star_triple=res["t_star_triple"],
        mu_ribbon_factors=res["mu_ribbon_factors"],
        mu_ribbon_W=res["mu_ribbon_W"],
        mu_ribbon_ordering=res["mu_ribbon_ordering"],
        W_PM_pred=res["W_PM_pred"],
        W_permode_cache=res["W_permode_cache"],
        delta_W_minus_PM=res["delta_W_minus_PM"],
        W_flat_tau0_exact_num=res["W_flat_tau0_exact_num"],
        W_flat_tau0_exact_den=res["W_flat_tau0_exact_den"],
        tau0_dev=res["tau0_dev"],
        mu_H_cache=res["mu_H_cache"], mu_H_pin=res["mu_H_pin"],
        tau_fold_used=res["tau_fold_used"], T_acoustic_used=res["T_acoustic_used"],
        PASS_band=np.array([PASS_LO, PASS_HI]),
        INFO_center=INFO_CENTER, INFO_halfband=INFO_HALFBAND,
        edge_tol=EDGE_TOL, at_lower_edge=res["at_lower_edge"],
        spectrum_cache_sha=CACHE_SHA_PIN,
    )
    npz_sha = sha256_of(OUT_NPZ)                                  # (local) Rider-1 ONE-DATASET pin
    print(f"  npz  -> {OUT_NPZ.relative_to(PROJECT_ROOT)}  (SHA {npz_sha[:16]}...)")

    # ---- dual-SHA + verdict payload --------------------------------------
    audit_sha, content_sha = compute_dual_sha(pins, CACHE_SHA_PIN)

    # value payload (no single-quote chars; the tool wraps value='...')
    value = (
        f"W_flat={res['W_flat']:.6f}_AT-9/5-lower-edge[1.800,1.8894]_"
        f"at_lower_edge={res['at_lower_edge']}(EDGE_TOL=1e-9)_"
        f"ordering_primary={res['ordering_primary']}_"
        f"ordering_secondary={res['ordering_secondary']}_"
        f"W_block={res['W_block']:.6f}_W_permode={res['W_permode_cache']:.6f}_"
        f"sbar_tau_fold={res['sbar_tau_fold']:.6f}_"
        f"W_flat(tau0)=9/5_EXACT_dev{res['tau0_dev']:.1e}_"
        f"slope_lo=slope_hi_dev{res['slope_dev']:.1e}_"
        f"deltaW-PM={res['delta_W_minus_PM']:+.4f}_mu-ribbon-ordering-stable"
    )

    extra_rows = [
        f"# rider1_npz_sha256={npz_sha}",
        (f"# primary <lam2>_g=({res['lambda2_triple'][0]:.6f},"
         f"{res['lambda2_triple'][1]:.6f},{res['lambda2_triple'][2]:.6f}) "
         f"C2=(4/3,3,6); single-slope sbar={res['sbar_tau_fold']:.6f} "
         f"(slope_lo=slope_hi dev {res['slope_dev']:.1e}) => W_flat=9/5 to machine eps"),
        (f"# secondary <omega>_g=({res['omega_weighted_triple'][0]:.6f},"
         f"{res['omega_weighted_triple'][1]:.6f},{res['omega_weighted_triple'][2]:.6f}) "
         f"ordering={res['ordering_secondary']} (counting-INDEPENDENT cancellation identity)"),
        (f"# non-gating: deltaW-PM={res['delta_W_minus_PM']:+.6f} (two-sided, NOT pre-registrable); "
         f"W_permode={res['W_permode_cache']:.6f} cross-face; mu-ribbon ordering stable {MU_RIBBON}"),
        ("# regulator_pin=N/A (group-theoretic Casimirs + cache moments only; no Seeley-DeWitt a_n); "
         "CLASS=N/A (no SCHEMATIC helper)"),
    ]

    payload = print_verdict_payload(
        verdict=res["value_composite"],
        value=value,
        audit_sha=audit_sha,
        content_sha=content_sha,
        sign_verdict=res["sign_verdict"],
        magnitude_verdict=res["magnitude_verdict"],
        regime_verdict=res["regime_verdict"],
        extra_rows=extra_rows,
    )
    return payload


if __name__ == "__main__":
    main()
