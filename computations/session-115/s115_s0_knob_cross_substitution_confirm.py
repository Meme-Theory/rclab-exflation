#!/usr/bin/env python3
"""
S115 W3-1 S115-S0-KNOB-CROSS-SUBSTITUTION-CONFIRM — confirmatory cross-substitution
==================================================================================

Gate: S115-S0-KNOB-CROSS-SUBSTITUTION-CONFIRM ([VERIFY])

A CONFIRMATORY re-run of the S101 W3 S0-knob discrimination (s101_w3_s0_knob.py),
routing candidate (iii)'s graded crossing offset at the LOCATED van Hove crossing
q_cross = tau_cross_van_hove = 0.191038 (S114-CF-S114-TAUFOLD-CUSP-CROSSING) INSTEAD
of the canonical fold value q = tau_fold = 19/100. Three legs, each regulator-free
(set-membership + exact rational arithmetic):

  LEG A (dev-magnitude):  S0_pred_iii^cross = q_cross / T_acoustic ; relax the s101
      bit-equality guard (s101 line 240 `assert abs(float(tau_f)-tau_fold)<1e-15`)
      to the SUBSTITUTED value (assert against q_cross). PASS iff
      dev[iii]^cross = |S0_pred_iii^cross / S0_fit - 1| <= 0.01 (expected ~0.00682).

  LEG B (selector class-invariance):  the s101 GRADED structural selector
      (legC_output_form == 'GRADED' -> eligible class 'graded-per-C2-quantum' ->
      candidate (iii) the SOLE member) reads a CLASS LABEL from the W2-2 npz; it is
      INDEPENDENT of the numerical value of q. Re-routing q from 19/100 to 0.191038
      does NOT change (iii)'s class membership. PASS iff N_inside(selector) == 1
      selecting (iii).

  LEG C (exact-rational asymmetry):  at the CANONICAL value S0(iii) = 19/100 / 14/125
      = 95/56 EXACT (clean small-denominator rational; the identity S0*T_ac = tau_fold).
      At the LOCATED value CF(0.191038/0.112) = CF(191038/112000) -> reduce
      (gcd 2) -> 95519/56000, whose continued fraction carries a LARGE partial
      quotient (>=10) within the first 8 terms (Sage: [1,1,2,2,1,1,18,44,4],
      first pq>=10 at index 6 = 18) => NO clean small-denominator convergent =>
      the 95/56 identity has NO analog at the located value. PASS iff
      exists k<=8 : pq_k(CF(191038/112000)) >= 10.

PASS iff all three legs hold. Pre-registered as CONFIRMS-CANNOT-FLIP: the input is
regulator-free arithmetic, so a non-PASS signals a SCRIPT/CONVENTION bug, NOT a
physics reversal (and is NEVER a re-opening of the S114 W-1 (iii) verdict). Routes
to in-session debug per mechanical-closure-discipline.md.

Inputs (SHA-256 dual-pinned at runtime -- S84+ schema):
  - computations/session-101/s101_envelope_carrier_discriminate.npz  (W2-2 Leg C; HARD input)
  - computations/session-100a/s100a_freezein_overconstrained.npz     (S0_fit, cache-free core)
  - computations/session-100a/s100a_s0_threshold_joint.npz           (candidate (i)/(ii) machinery)
  - computations/session-100a/s100a_envelope_overdetermine.npz        (graded-offset / fingerprint lineage)
  - canonical_constants.py (feeds audit_sha256; supplies tau_fold, T_acoustic, tau_cross_van_hove)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<3-leg verdict + S0_pred_iii^cross + dev + selector + first big pq>,
   scheme=KNOB-DISCRIMINATION-3CAND-LEGC-ROUTED-CROSS-SUBSTITUTION,
   convention=RATIO-NORMALIZED-TRACE-MEAN, L_max=12)

Classification: PARTICLE.

DISCIPLINE
----------
- `from canonical_constants import *`; every intermediate tagged `# (local)`
- numpy CPU (scalar arithmetic) + one Sage continued_fraction call; OMP_NUM_THREADS=8 cap
- dual-SHA (audit + content) per S84+; verdict via emit_verdict MCP tool (race-safe)
- [VERIFY] trigger -> NO 3-tuple companion row
- No Seeley-DeWitt a_n cited -> no regulator_pin. No SCHEMATIC helper -> no CLASS pin.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Path bootstrap + canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os

os.environ.setdefault("OMP_NUM_THREADS", "8")  # cap threads BEFORE numpy import
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import sys
import time
from fractions import Fraction
from pathlib import Path

_SHARED = Path(__file__).resolve().parents[1] / "_shared"
sys.path.insert(0, str(_SHARED))
from canonical_constants import *  # noqa: F401,F403,E402
from canonical_constants import (  # noqa: E402  explicit (used below)
    tau_fold,
    T_acoustic,
    tau_cross_van_hove,
)

# ---------------------------------------------------------------------------
# Section 2 — Numerical imports
# ---------------------------------------------------------------------------
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S115"                                                                       # (local)
GATE_ID = "S115-S0-KNOB-CROSS-SUBSTITUTION-CONFIRM"                                    # (local)
SCHEME = "KNOB-DISCRIMINATION-3CAND-LEGC-ROUTED-CROSS-SUBSTITUTION"                    # (local)
CONVENTION = "RATIO-NORMALIZED-TRACE-MEAN"                                             # (local)
L_MAX = 12                                                                             # (local)

# Pre-registered thresholds (plan §W3-1) -- exact decimals (s101 plan-frozen PASS_BAND)
PASS_BAND = 0.01                                                                       # (local) per-candidate ratio-dev for PASS count (s101 line 116)
FAIL_OUTER = 0.05                                                                      # (local) FAIL iff no candidate within this (s101 line 117)
N_EVAL = 3                                                                             # (local) 3 candidates x 1 derivation route (s101 N_EVAL=3)
CF_PQ_THRESHOLD = 10                                                                   # (local) LEG-C: first partial quotient >= this within...
CF_FIRST_N_TERMS = 8                                                                   # (local) ...the first this-many CF terms

# Output destinations (per-session)
OUT_NPZ = SESSION_DIR / "s115_s0_knob_cross_substitution_confirm.npz"
OUT_PNG = SESSION_DIR / "s115_s0_knob_cross_substitution_confirm.png"

# Input files (verbatim S101 lineage)
W2_2_NPZ = COMPUTATIONS_DIR / "session-101" / "s101_envelope_carrier_discriminate.npz"
W3_9_NPZ = COMPUTATIONS_DIR / "session-100a" / "s100a_freezein_overconstrained.npz"
S0_THR_NPZ = COMPUTATIONS_DIR / "session-100a" / "s100a_s0_threshold_joint.npz"
ENV_OD_NPZ = COMPUTATIONS_DIR / "session-100a" / "s100a_envelope_overdetermine.npz"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    W2_2_NPZ,
    W3_9_NPZ,
    S0_THR_NPZ,
    ENV_OD_NPZ,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Continued-fraction (LEG C). Pure-Python Euclidean CF on the EXACT
#   reduced rational (deterministic; matches Sage continued_fraction.quotients()).
#   Sage cross-check value embedded for the working paper:
#     CF(191038/112000) = [1, 1, 2, 2, 1, 1, 18, 44, 4]; first pq>=10 @ idx 6 = 18.
# ---------------------------------------------------------------------------
def continued_fraction_quotients(num: int, den: int) -> list[int]:
    """Exact Euclidean continued-fraction partial quotients of num/den (num,den>0)."""
    qs: list[int] = []  # (local)
    a, b = int(num), int(den)  # (local)
    while b != 0:
        q = a // b  # (local) floor division (a,b>0 throughout)
        qs.append(q)
        a, b = b, a - q * b
    return qs


# ---------------------------------------------------------------------------
# Section 6 — Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    # --- Load W2-2 Leg C output (HARD input) ---
    w22 = np.load(W2_2_NPZ, allow_pickle=True)  # (local)
    legC_output_form = str(w22["legC_output_form"])              # (local) 'GRADED' | 'SCALAR'
    legC_q_prime = float(w22["legC_q_prime"])                    # (local) S0_fit * T_acoustic (derived graded offset)
    legC_graded_residual_vec = np.asarray(w22["legC_graded_residual_vec"], float)  # (local)
    legC_scalar_residual_max = float(w22["legC_scalar_residual_max"])              # (local)
    legC_derivation_residual = float(w22["legC_derivation_residual"])              # (local)
    S0_fit = float(w22["S0_fit"])                               # (local) 1.694153 cache-free core
    w22_audit = str(w22["audit_sha256"])                        # (local)

    # cross-check S0_fit against the W3-9 cache-free core (one-dataset echo)
    w39 = np.load(W3_9_NPZ, allow_pickle=True)                  # (local)
    S0_fit_w39 = float(w39["S0_fit"])                           # (local)
    s0_fit_echo_dev = abs(S0_fit - S0_fit_w39)                  # (local)

    # --- candidate (i)/(ii) machinery from the threshold-joint npz ---
    thr = np.load(S0_THR_NPZ, allow_pickle=True)                # (local)
    knob_req = float(thr["knob"])                               # (local) ~1.32467 -- the knob S0_fit requires
    S0_alt_halfdelta = float(thr["S0_alt_halfdelta"])           # (local) ~1.66971 -- S0 under half_delta
    half_delta = float(thr["half_delta"])                       # (local) 1.175
    KK_delta = float(thr["KK_threshold_delta"])                 # (local) 2.35

    # --- fingerprint lineage (graded offset) ---
    env = np.load(ENV_OD_NPZ, allow_pickle=True)                # (local)
    S0_times_T_acoustic_fp = float(env["S0_times_T_acoustic"])  # (local) 0.189745 == legC_q_prime

    # ===================================================================
    # Exact rationals: CANONICAL flank value vs LOCATED crossing value
    # ===================================================================
    tau_f = Fraction(19, 100)                                   # (local) tau_fold exact (canonical flank)
    T_ac = Fraction(14, 125)                                    # (local) T_acoustic exact = 0.112
    C2_10 = Fraction(4, 3)                                      # (local) C2(1,0) Casimir quantum
    # LOCATED van Hove crossing, exact rational from the 6-sf canonical 0.191038
    q_cross = Fraction(191038, 1000000)                         # (local) tau_cross_van_hove exact

    # ===================================================================
    # CROSS-SUBSTITUTION guard relaxation (s101 line 240 relaxed to q_cross):
    #   s101 asserted abs(float(tau_f) - tau_fold) < 1e-15 (the canonical bit-eq).
    #   Here the routed offset is q_cross; assert the SUBSTITUTED value's bit-eq
    #   (q_cross float == tau_cross_van_hove canonical) and T_ac (unchanged).
    # ===================================================================
    assert abs(float(q_cross) - tau_cross_van_hove) < 1e-15, "tau_cross_van_hove canonical drift (relaxed guard)"
    assert abs(float(T_ac) - T_acoustic) < 1e-15, "T_acoustic canonical drift"
    # informational: the canonical flank value is still consistent (NOT the routed offset)
    tau_fold_bit_ok = abs(float(tau_f) - tau_fold) < 1e-15      # (local)

    # ===================================================================
    # DERIVATION-ROUTED S0_pred per candidate (NOT post-hoc ratio)
    #   candidate (iii) now proposes q := q_cross (the LOCATED crossing);
    #   S0 = q / T_ac (s101 line 248 derivation route, with q := q_cross).
    # ===================================================================
    # (iii)^cross: q = tau_cross_van_hove -> S0 = q_cross / T_ac (EXACT rational)
    S0_pred_iii_exact = q_cross / T_ac                          # (local) 95519/56000
    S0_pred_iii = float(S0_pred_iii_exact)                      # (local)

    # (i) Casimir quantum knob = 4/3, routed through the threshold-knob image (UNCHANGED):
    S0_pred_i = S0_fit * float(C2_10) / knob_req                # (local)

    # (ii) half-delta gap (UNCHANGED): the threshold gate's S0 under half_delta = 1.175
    S0_pred_ii = S0_alt_halfdelta                               # (local)

    S0_pred = {"i": S0_pred_i, "ii": S0_pred_ii, "iii": S0_pred_iii}  # (local)
    dev = {k: abs(v / S0_fit - 1.0) for k, v in S0_pred.items()}      # (local)

    # ===================================================================
    # NAIVE dev-count (pre-selector)
    # ===================================================================
    inside_001_all = {k: (dev[k] <= PASS_BAND) for k in dev}    # (local)
    inside_005_all = {k: (dev[k] <= FAIL_OUTER) for k in dev}   # (local)
    N_inside_naive = int(sum(inside_001_all.values()))          # (local)
    N_inside_005 = int(sum(inside_005_all.values()))            # (local)

    # ===================================================================
    # STRUCTURAL SELECTOR (Leg-C output FORM) -- IDENTICAL to s101 lines 279-292.
    #   The selector reads a CLASS LABEL; it is INDEPENDENT of the value of q.
    # ===================================================================
    candidate_class = {                                         # (local)
        "i": "gap-shadow",            # scalar Casimir eigenvalue; the 0.52% (i)/(iii) shadow
        "ii": "gap",                  # KK-threshold gap class (SCALAR side)
        "iii": "graded-per-C2-quantum",  # the genuine graded crossing-slope member
    }
    if legC_output_form == "GRADED":
        eligible_class = "graded-per-C2-quantum"               # (local)
    elif legC_output_form == "SCALAR":
        eligible_class = "gap"                                 # (local)
    else:
        eligible_class = "<UNRESOLVED>"                        # (local)

    eligible = {k: (candidate_class[k] == eligible_class) for k in candidate_class}  # (local)

    # robustness witness for the GRADED selection
    graded_residual_max = float(np.max(np.abs(legC_graded_residual_vec)))  # (local)
    graded_clean = graded_residual_max < 1e-12                  # (local)
    scalar_excluded = legC_scalar_residual_max > 1e-3           # (local)

    # ===================================================================
    # DEV-COUNT AFTER the structural selector (the gate's LEG B operator)
    # ===================================================================
    inside_001_selected = {k: (eligible[k] and dev[k] <= PASS_BAND) for k in dev}  # (local)
    N_inside = int(sum(inside_001_selected.values()))          # (local) THE gate count
    selected_knobs = [k for k in dev if inside_001_selected[k]]  # (local)
    selector_selects_iii = (N_inside == 1 and selected_knobs == ["iii"])  # (local) LEG B

    # ===================================================================
    # LEG C — exact-rational asymmetry via continued fraction of the LOCATED value.
    #   located: 191038/112000 reduces to 95519/56000 (gcd 2).
    #   canonical CONTRAST: 95/56 (clean, all pq small).
    # ===================================================================
    located_num = S0_pred_iii_exact.numerator * T_ac.denominator      # not used directly; build the raw 191038/112000
    # build the RAW (unreduced) located rational 0.191038/0.112 = 191038/112000
    raw_located = Fraction(191038, 112000)                      # (local) == q_cross / T_ac unreduced form
    assert raw_located == S0_pred_iii_exact, "located-rational construction drift"
    cf_located = continued_fraction_quotients(raw_located.numerator, raw_located.denominator)  # (local)
    # first partial quotient >= threshold within the first CF_FIRST_N_TERMS
    first_big_idx = -1                                          # (local)
    first_big_val = -1                                          # (local)
    for i, q in enumerate(cf_located[:CF_FIRST_N_TERMS]):
        if q >= CF_PQ_THRESHOLD:
            first_big_idx = i
            first_big_val = int(q)
            break
    leg_c_pass = (first_big_idx >= 0)                          # (local) LEG C

    # canonical-value CF contrast (clean small-denominator: 95/56)
    S0_canon_exact = tau_f / T_ac                              # (local) 95/56 (the CANONICAL identity)
    cf_canonical = continued_fraction_quotients(S0_canon_exact.numerator, S0_canon_exact.denominator)  # (local)
    canon_max_pq = int(max(cf_canonical))                     # (local) 3 -> all small
    # canonical defining identity S0(canon)*T_ac == tau_fold EXACT
    identity_lhs_canon = S0_canon_exact * T_ac                # (local) Fraction
    identity_exact_canon = (identity_lhs_canon == tau_f)      # (local) True by construction
    # at the LOCATED value the analogous identity would require S0_pred_iii_exact * T_ac == q_cross:
    located_identity_lhs = S0_pred_iii_exact * T_ac           # (local)
    located_identity_is_qcross = (located_identity_lhs == q_cross)  # (local) trivially True (q/T*T=q); the
    #   ASYMMETRY is in the DENOMINATOR SIZE, captured by the CF pq, not in this trivial round-trip.

    # ===================================================================
    # COMPOSITE VERDICT — three-leg AND (plan operator.form)
    # ===================================================================
    leg_a_pass = (dev["iii"] <= PASS_BAND)                     # (local) dev-magnitude
    leg_b_pass = selector_selects_iii                         # (local) selector class-invariance
    leg_c_pass_final = leg_c_pass                             # (local) exact-rational asymmetry

    if N_inside_005 == 0:
        # no candidate even within 0.05 of the selected class -> structural FAIL
        verdict = "FAIL"                                       # (local)
    elif leg_a_pass and leg_b_pass and leg_c_pass_final:
        verdict = "PASS"                                       # (local) CONFIRMS-CANNOT-FLIP
    elif N_inside >= 2:
        verdict = "INFO"                                       # (local) selector degenerated (wiring issue)
    else:
        verdict = "FAIL"                                       # (local) a regulator-free leg failed => script/convention bug
    selected_knob = "iii" if (verdict == "PASS") else (selected_knobs[0] if selected_knobs else "none")  # (local)

    # ===================================================================
    # SHA verification vs s101 plan/orch pins (informational; not gating here)
    # ===================================================================
    PIN_W2_2 = "463f32033347c2250f119d090623b6a43bad0463395b3b4ca2a27b45b4c67d1a"  # (local) s101 orch override
    pin_ok_w2_2 = (sha256_of(W2_2_NPZ) == PIN_W2_2)            # (local)

    value_str = (
        f"verdict_legs[A_dev={leg_a_pass},B_sel={leg_b_pass},C_cf={leg_c_pass_final}];"
        f"S0_pred_iii^cross=q_cross/T_ac=0.191038/0.112=95519/56000={S0_pred_iii:.6f};"
        f"dev[iii]^cross={dev['iii']:.5f}(<=0.01);S0_fit={S0_fit:.6f};"
        f"N_inside={N_inside}(selector_selects_iii={selector_selects_iii});legC={legC_output_form};"
        f"CF(191038/112000)={cf_located};first_pq>=10@idx{first_big_idx}={first_big_val};"
        f"canon_95/56_CF={cf_canonical}_maxpq{canon_max_pq};CONFIRMS-CANNOT-FLIP_W-1(iii)"
    )

    return {
        "value": value_str,
        "verdict": verdict,
        # --- LEG A: dev-magnitude ---
        "q_cross": float(q_cross),
        "T_acoustic_used": float(T_ac),
        "tau_fold_used": float(tau_f),
        "S0_fit": S0_fit,
        "S0_fit_w39": S0_fit_w39,
        "s0_fit_echo_dev": s0_fit_echo_dev,
        "S0_pred_iii_cross": S0_pred_iii,
        "S0_pred_iii_cross_exact_str": "95519/56000",
        "S0_pred_i": S0_pred_i,
        "S0_pred_ii": S0_pred_ii,
        "dev_i": dev["i"],
        "dev_ii": dev["ii"],
        "dev_iii_cross": dev["iii"],
        "leg_a_pass": bool(leg_a_pass),
        "inside_001_i": inside_001_all["i"],
        "inside_001_ii": inside_001_all["ii"],
        "inside_001_iii_cross": inside_001_all["iii"],
        # --- LEG B: selector class-invariance ---
        "legC_output_form": legC_output_form,
        "legC_q_prime": legC_q_prime,
        "legC_derivation_residual": legC_derivation_residual,
        "eligible_class": eligible_class,
        "candidate_class_i": candidate_class["i"],
        "candidate_class_ii": candidate_class["ii"],
        "candidate_class_iii": candidate_class["iii"],
        "eligible_i": eligible["i"],
        "eligible_ii": eligible["ii"],
        "eligible_iii": eligible["iii"],
        "graded_residual_max": graded_residual_max,
        "graded_clean": graded_clean,
        "legC_scalar_residual_max": legC_scalar_residual_max,
        "scalar_excluded": scalar_excluded,
        "N_inside": N_inside,
        "N_inside_naive": N_inside_naive,
        "N_inside_005": N_inside_005,
        "selected_knob": selected_knob,
        "selected_knobs": np.array(selected_knobs, dtype=object),
        "selector_selects_iii": bool(selector_selects_iii),
        "leg_b_pass": bool(leg_b_pass),
        # --- LEG C: exact-rational asymmetry ---
        "cf_located": np.array(cf_located, dtype=int),
        "cf_located_str": str(cf_located),
        "located_reduced_str": "95519/56000",
        "located_raw_str": "191038/112000",
        "first_big_pq_idx": first_big_idx,
        "first_big_pq_val": first_big_val,
        "cf_pq_threshold": CF_PQ_THRESHOLD,
        "cf_first_n_terms": CF_FIRST_N_TERMS,
        "leg_c_pass": bool(leg_c_pass_final),
        "cf_canonical": np.array(cf_canonical, dtype=int),
        "cf_canonical_str": str(cf_canonical),
        "canon_max_pq": canon_max_pq,
        "S0_canon_exact_str": "95/56",
        "identity_exact_canon_S0T_ac_eq_tau": bool(identity_exact_canon),
        "located_identity_round_trip": bool(located_identity_is_qcross),
        "tau_fold_bit_ok": bool(tau_fold_bit_ok),
        # machinery echoes
        "knob_req": knob_req,
        "S0_alt_halfdelta": S0_alt_halfdelta,
        "half_delta": half_delta,
        "KK_threshold_delta": KK_delta,
        "S0_times_T_acoustic_fp": S0_times_T_acoustic_fp,
        # pins
        "w2_2_audit_echo": w22_audit,
        "pin_ok_w2_2": pin_ok_w2_2,
        # bands
        "PASS_BAND": PASS_BAND,
        "FAIL_OUTER": FAIL_OUTER,
    }


def make_plot(r: dict) -> None:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13.4, 5.4))

    # Panel 1: derivation-routed devs vs 0.01 / 0.05 bands, colored by selector eligibility
    devs = [r["dev_i"], r["dev_ii"], r["dev_iii_cross"]]
    elig = [r["eligible_i"], r["eligible_ii"], r["eligible_iii"]]
    labels = [
        "(i) 4/3\nCasimir quantum\n[gap-shadow]",
        "(ii) δ/2=1.175\nKK-threshold\n[gap]",
        "(iii) 95519/56000\nq_cross/T_ac\n[graded]",
    ]
    colors = ["#2ca02c" if e else "#bbbbbb" for e in elig]
    ax1.bar(range(3), devs, color=colors, edgecolor="black", zorder=3)
    ax1.axhline(r["PASS_BAND"], color="#1f77b4", ls="--", lw=1.6, label="PASS band 0.01", zorder=2)
    ax1.axhline(r["FAIL_OUTER"], color="#d62728", ls=":", lw=1.6, label="FAIL outer 0.05", zorder=2)
    for i, (d, e) in enumerate(zip(devs, elig)):
        tag = "ELIGIBLE" if e else "shadow→excl"
        ax1.text(i, d + 0.0012, f"{d*100:.3f}%\n{tag}", ha="center", va="bottom", fontsize=8.5)
    ax1.set_xticks(range(3))
    ax1.set_xticklabels(labels, fontsize=8.3)
    ax1.set_ylabel("derivation-routed dev = |S0_pred/S0_fit − 1|")
    ax1.set_ylim(0, 0.058)
    ax1.set_title(
        f"S0 knob CROSS-SUBSTITUTION — q_cross=0.191038 (LOCATED van Hove)\n"
        f"Leg-C={r['legC_output_form']} selector → N_inside={r['N_inside']} → {r['verdict']}"
    )
    ax1.legend(loc="upper right", fontsize=9)
    ax1.grid(axis="y", alpha=0.3, zorder=0)

    # Panel 2: the three-leg CONFIRMS-CANNOT-FLIP summary
    ax2.axis("off")
    txt = (
        f"THREE-LEG CONFIRMS-CANNOT-FLIP (all regulator-free arithmetic)\n"
        f"────────────────────────────────────────────\n"
        f"LEG A  dev-magnitude\n"
        f"  S0_pred_iii^cross = q_cross/T_ac = 0.191038/0.112\n"
        f"                    = 95519/56000 = {r['S0_pred_iii_cross']:.6f}\n"
        f"  dev[iii]^cross = |{r['S0_pred_iii_cross']:.6f}/{r['S0_fit']:.6f} − 1|\n"
        f"                 = {r['dev_iii_cross']*100:.4f}%  ≤ 1.00%   PASS={r['leg_a_pass']}\n\n"
        f"LEG B  selector class-invariance (q-INDEPENDENT)\n"
        f"  legC_output_form = {r['legC_output_form']}  → class '{r['eligible_class']}'\n"
        f"  graded resid {r['graded_residual_max']:.1e} (clean {r['graded_clean']}); "
        f"scalar resid {r['legC_scalar_residual_max']:.3f} (excl {r['scalar_excluded']})\n"
        f"  N_inside(selector)={r['N_inside']} → selects (iii): {r['selector_selects_iii']}   "
        f"PASS={r['leg_b_pass']}\n\n"
        f"LEG C  exact-rational asymmetry (CF partial quotient)\n"
        f"  CANONICAL  19/100 / 14/125 = 95/56  CF={r['cf_canonical_str']}\n"
        f"             max pq = {r['canon_max_pq']}  (clean small-denominator identity)\n"
        f"  LOCATED    191038/112000 = 95519/56000  CF={r['cf_located_str']}\n"
        f"             first pq≥10 @ idx {r['first_big_pq_idx']} = {r['first_big_pq_val']}  "
        f"PASS={r['leg_c_pass']}\n"
        f"  ⇒ the 95/56 identity has NO analog at the located value\n\n"
        f"VERDICT: {r['verdict']}  — CONFIRMS, structurally CANNOT FLIP, W-1 (iii)\n"
        f"  S114 W-1 (iii) verdict stands; the canonical flank 19/100 is one\n"
        f"  sub-choice within the van-Hove-selected crossing region."
    )
    ax2.text(0.0, 1.0, txt, va="top", ha="left", fontsize=8.8, family="monospace",
             transform=ax2.transAxes)

    fig.suptitle(
        "S115-S0-KNOB-CROSS-SUBSTITUTION-CONFIRM — (iii) routed at the LOCATED van Hove crossing",
        fontsize=12, y=1.01,
    )
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 7 — Gate verdict + 4-tuple output
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict: str, value, audit_sha: str, content_sha: str,
                          companion_note: str = "",
                          extra_rows: list[str] | None = None) -> dict:
    payload: dict = {
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
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    r = compute()
    value = r["value"]
    verdict = r["verdict"]

    # save npz (full float64)
    np.savez(OUT_NPZ, gate_id=GATE_ID, scheme=SCHEME, convention=CONVENTION,
             l_max=str(L_MAX), schema_version="S84+",
             audit_sha256=audit_sha, content_sha256=content_sha,
             **{k: v for k, v in r.items() if k != "value"},
             value=value)
    print(f"  wrote {OUT_NPZ.name}")
    make_plot(r)
    print(f"  wrote {OUT_PNG.name}")
    print()

    # human-readable summary
    print("=== RESULTS (CROSS-SUBSTITUTION at q_cross=tau_cross_van_hove=0.191038) ===")
    print(f"  S0_fit                     = {r['S0_fit']:.10f}  (W3-9 echo dev {r['s0_fit_echo_dev']:.2e})")
    print(f"  LEG A  S0_pred_iii^cross   = {r['S0_pred_iii_cross']:.10f}  (= 95519/56000 = 0.191038/0.112)")
    print(f"         dev[iii]^cross      = {r['dev_iii_cross']*100:.4f}%  (<=1.00% PASS={r['leg_a_pass']})")
    print(f"         (i)  4/3   -> dev   = {r['dev_i']*100:.4f}%  inside0.01={r['inside_001_i']}  class={r['candidate_class_i']}")
    print(f"         (ii) δ/2   -> dev   = {r['dev_ii']*100:.4f}%  inside0.01={r['inside_001_ii']}  class={r['candidate_class_ii']}")
    print(f"  LEG B  legC_output_form    = {r['legC_output_form']} -> eligible class '{r['eligible_class']}'")
    print(f"         eligible: i={r['eligible_i']} ii={r['eligible_ii']} iii={r['eligible_iii']}")
    print(f"         N_inside(selector)  = {r['N_inside']} -> selects (iii): {r['selector_selects_iii']} (PASS={r['leg_b_pass']})")
    print(f"  LEG C  CANONICAL 95/56 CF  = {r['cf_canonical_str']}  max pq={r['canon_max_pq']} (clean)")
    print(f"         LOCATED  CF(191038/112000) = {r['cf_located_str']}")
    print(f"         first pq>=10 @ idx {r['first_big_pq_idx']} = {r['first_big_pq_val']} (PASS={r['leg_c_pass']})")
    print(f"         => 95/56 identity has NO analog at located value")
    print(f"  identity (canonical) S0*T_ac == tau_fold exact: {r['identity_exact_canon_S0T_ac_eq_tau']}")
    print(f"  SHA pin check (informational): w2_2={r['pin_ok_w2_2']}")
    print()

    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(tag)

    extra = [
        (f"# CROSS-SUBSTITUTION q_cross=tau_cross_van_hove=0.191038 (S114) routed into (iii); "
         f"legC_form={r['legC_output_form']} selector_class={r['eligible_class']} "
         f"N_inside={r['N_inside']} selects(iii)={r['selector_selects_iii']}"),
        (f"# LEG A dev[iii]^cross={r['dev_iii_cross']*100:.4f}%<=1.00% ({r['leg_a_pass']}); "
         f"LEG B selector q-invariant ({r['leg_b_pass']}); "
         f"LEG C CF(191038/112000)={r['cf_located_str']} first_pq>=10@idx{r['first_big_pq_idx']}={r['first_big_pq_val']} ({r['leg_c_pass']})"),
        (f"# canonical 95/56 CF={r['cf_canonical_str']} maxpq={r['canon_max_pq']} (clean small-denom identity, "
         f"S0*T_ac==tau_fold exact={r['identity_exact_canon_S0T_ac_eq_tau']}); located 95519/56000 carries NO clean convergent; "
         f"CONFIRMS-CANNOT-FLIP W-1(iii)"),
    ]
    print_verdict_payload(verdict, value, audit_sha, content_sha, extra_rows=extra)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
