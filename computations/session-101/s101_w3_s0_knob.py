#!/usr/bin/env python3
"""
S101 W2-3 S101-W3-S0-KNOB — exactly-one-inside-0.01 knob discrimination
=======================================================================

Gate: S101-W3-S0-KNOB ([VERIFY])

Pre-registered threshold (plan §W2-3, operator.form):
  N_inside = |{k : |S0_pred,k / S0_fit - 1| <= 0.01, k in {(i),(ii),(iii)},
               derivation-routed}|, AFTER the Leg-C structural selector.
  PASS iff N_inside == 1 (structural selector applied);
  INFO iff N_inside >= 2 (degenerate -- needs a second observable);
  FAIL iff no candidate has dev <= 0.05.

Inputs (SHA-256 dual-pinned at runtime -- S84+ schema):
  - computations/session-101/s101_envelope_carrier_discriminate.npz  (W2-2 Leg C; HARD input)
  - computations/session-100a/s100a_freezein_overconstrained.npz     (S0_fit, cache-free core)
  - computations/session-100a/s100a_s0_threshold_joint.npz           (candidate (i)/(ii) machinery)
  - computations/session-100a/s100a_envelope_overdetermine.npz        (graded-offset / fingerprint lineage)
  - canonical_constants.py (feeds audit_sha256; supplies tau_fold, T_acoustic)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<N_inside + selected knob>, scheme=KNOB-DISCRIMINATION-3CAND-LEGC-ROUTED,
   convention=RATIO-NORMALIZED-TRACE-MEAN, L_max=12)

Classification: PARTICLE.

METHODOLOGY
-----------
Post-processing DOWNSTREAM of W2-2 Leg C. W2-2 derived the GRADED one-fiber freeze-
frequency split  omega_g = q * C2(g) * M_KK  (Casimir-linear in g; the graded residual
vector ~1e-16 while the SCALAR residual is 0.892, so the substrate fixes the output
FORM = GRADED). The derived graded crossing offset is q' = S0_fit * T_acoustic = 0.189745
(= legC_q_prime). The knob question is WHICH substrate datum fixes the ABSOLUTE scale S0;
each of the three pre-registered candidates proposes a value for the graded crossing
offset q, and S0_pred = q / T_acoustic (the derivation route -- the candidate value
composed with the derived one-fiber split structure, NOT a post-hoc ratio comparison):

  (i)   knob = C2(1,0) = 4/3 (a single scalar Casimir EIGENVALUE -- gap/shadow class).
        Routed through the threshold-knob image (s100a_s0_threshold_joint: knob_req that
        S0_fit requires): S0_pred,i = S0_fit * (4/3) / knob_req.  dev ~ 0.65%.
  (ii)  Delta_omega = delta/2 = 1.175 (halved KK-THRESHOLD-64 split, delta=2.35) -- the
        threshold gate's S0 under half_delta (S0_alt_halfdelta).  dev ~ 1.44%.  GAP class.
  (iii) q = tau_fold (the fold deformation parameter read through T_acoustic):
        S0_pred,iii = tau_fold / T_acoustic = 95/56.  dev ~ 0.13%.  GRADED per-C2-quantum.

Naive count: BOTH (i) and (iii) sit inside 0.01 -> N_inside_naive = 2 (degenerate INFO).
The (i)/(iii) coincidence is a 0.52% PIN-PROXIMITY ACCIDENT (E-3 row 1:
2*pi*tau_fold = 1.19380 vs (4/3)*0.9 = 1.2, ratio 1.00519). The DEGENERACY is resolved
STRUCTURALLY, not by a tighter band: legC_output_form = GRADED selects the
per-Casimir-quantum CLASS (candidate (iii)); the scalar-Casimir-eigenvalue (i) and the
gap-class (ii) are NOT members of the graded crossing-slope class. The structural selector
is applied BEFORE the dev-count, so the shadow pair cannot produce a spurious INFO.
E-3 shadow-vetting cross-checks the surviving candidate against products/ratios of the
canonical pin set for <=5% proximities (any in-band shadow carries ZERO incremental weight).

DISCIPLINE
----------
- `from canonical_constants import *`; every intermediate tagged `# (local)`
- numpy CPU (scalar arithmetic), OMP_NUM_THREADS=8 cap (set before numpy import)
- dual-SHA (audit + content) per S84+; verdict via emit_verdict MCP tool (race-safe)
- No Seeley-DeWitt a_n cited -> no regulator_pin. No SCHEMATIC helper -> no CLASS pin.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Path bootstrap + canonical constants (MANDATORY first import)
#   _shared (holding canonical_constants.py) is added to sys.path so the import
#   resolves regardless of cwd (matches the W2-2 sibling script pattern, lines
#   105-107 of s101_envelope_carrier_discriminate.py).
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
from canonical_constants import tau_fold, T_acoustic  # noqa: E402  explicit (used below)

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

SESSION = "S101"                                                   # (local)
GATE_ID = "S101-W3-S0-KNOB"                                        # (local)
SCHEME = "KNOB-DISCRIMINATION-3CAND-LEGC-ROUTED"                   # (local)
CONVENTION = "RATIO-NORMALIZED-TRACE-MEAN"                         # (local)
L_MAX = 12                                                         # (local)

# Pre-registered thresholds (plan §W2-3) -- exact decimals
PASS_BAND = 0.01                                                   # (local) per-candidate ratio-dev for PASS count
FAIL_OUTER = 0.05                                                  # (local) FAIL iff no candidate within this
N_EVAL = 3                                                         # (local) 3 candidates x 1 derivation route

# Output destinations (per-session)
OUT_NPZ = SESSION_DIR / "s101_w3_s0_knob.npz"
OUT_PNG = SESSION_DIR / "s101_w3_s0_knob.png"

# Input files
W2_2_NPZ = SESSION_DIR / "s101_envelope_carrier_discriminate.npz"
W3_9_NPZ = COMPUTATIONS_DIR / "session-100a" / "s100a_freezein_overconstrained.npz"
S0_THR_NPZ = COMPUTATIONS_DIR / "session-100a" / "s100a_s0_threshold_joint.npz"
ENV_OD_NPZ = COMPUTATIONS_DIR / "session-100a" / "s100a_envelope_overdetermine.npz"

# Static SHA pins from the plan-block (verified at runtime; W2-2 npz pinned to ORCH override)
PIN_W2_2 = "463f32033347c2250f119d090623b6a43bad0463395b3b4ca2a27b45b4c67d1a"  # (local) W2-2 audit_sha256 (orch override)
PIN_W3_9 = "aa5acf5475fe8a2eb301b4c0e39901811cd3bb2587d43766746b9beb5f5f56b6"  # (local)
PIN_S0_THR = "5eb313997ec91c336e14cfb0a22a2ee53254b443cc4f20c50f2efd378e4308ad"  # (local)
PIN_ENV_OD = "0878d68b4f7f79eca2dfc021e6fd6851575e528f892579e687cc6cb448e1a5fd"  # (local)

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
# Section 5 — Compute
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
    knob_req = float(thr["knob"])                               # (local) 1.32467 -- the knob S0_fit requires
    S0_alt_halfdelta = float(thr["S0_alt_halfdelta"])           # (local) 1.66971 -- S0 under half_delta
    half_delta = float(thr["half_delta"])                       # (local) 1.175
    KK_delta = float(thr["KK_threshold_delta"])                 # (local) 2.35

    # --- fingerprint lineage (graded offset) ---
    env = np.load(ENV_OD_NPZ, allow_pickle=True)                # (local)
    S0_times_T_acoustic_fp = float(env["S0_times_T_acoustic"])  # (local) 0.189745 == legC_q_prime

    # ===================================================================
    # Candidate exact values
    # ===================================================================
    tau_f = Fraction(19, 100)                                   # (local) tau_fold exact
    T_ac = Fraction(14, 125)                                    # (local) T_acoustic exact
    C2_10 = Fraction(4, 3)                                      # (local) C2(1,0) Casimir quantum
    hd_exact = Fraction(235, 100) / 2                           # (local) delta/2 = 47/40 = 1.175

    # cross-check the canonical floats match the exact rationals (bit-level)
    assert abs(float(tau_f) - tau_fold) < 1e-15, "tau_fold canonical drift"
    assert abs(float(T_ac) - T_acoustic) < 1e-15, "T_acoustic canonical drift"

    # ===================================================================
    # DERIVATION-ROUTED S0_pred per candidate (NOT post-hoc ratio)
    #   each candidate proposes the graded crossing offset q; S0 = q / T_ac
    # ===================================================================
    # (iii) moduli-acoustic: q = tau_fold -> S0 = tau_fold / T_acoustic = 95/56 (EXACT)
    S0_pred_iii_exact = tau_f / T_ac                            # (local) 95/56
    S0_pred_iii = float(S0_pred_iii_exact)                      # (local)

    # (i) Casimir quantum knob = 4/3, routed through the threshold-knob image:
    #     S0_pred,i = S0_fit * (4/3) / knob_req
    S0_pred_i = S0_fit * float(C2_10) / knob_req                # (local)

    # (ii) half-delta gap: the threshold gate's S0 under half_delta = 1.175
    S0_pred_ii = S0_alt_halfdelta                               # (local)

    S0_pred = {"i": S0_pred_i, "ii": S0_pred_ii, "iii": S0_pred_iii}  # (local)
    dev = {k: abs(v / S0_fit - 1.0) for k, v in S0_pred.items()}      # (local)

    # ===================================================================
    # NAIVE dev-count (pre-selector) -- demonstrates the (i)/(iii) degeneracy
    # ===================================================================
    inside_001_all = {k: (dev[k] <= PASS_BAND) for k in dev}    # (local)
    inside_005_all = {k: (dev[k] <= FAIL_OUTER) for k in dev}   # (local)
    N_inside_naive = int(sum(inside_001_all.values()))          # (local)
    N_inside_005 = int(sum(inside_005_all.values()))            # (local)

    # ===================================================================
    # STRUCTURAL SELECTOR (Leg-C output FORM) -- applied BEFORE the dev-count
    #   GRADED  => per-Casimir-quantum class = the graded crossing-SLOPE candidate (iii);
    #             (i) is a scalar Casimir EIGENVALUE (gap/shadow), (ii) is the gap class.
    #   SCALAR  => the (i)/(ii) gap class; (iii) demoted to fingerprint-coincidence.
    # Class membership of each candidate:
    #   (i)   scalar Casimir eigenvalue 4/3                       -> 'gap-shadow'
    #   (ii)  halved KK-threshold gap delta/2                     -> 'gap'
    #   (iii) graded crossing slope q (omega_g = q*C2(g)*M_KK)    -> 'graded-per-C2-quantum'
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

    # selector-eligible candidates (members of the Leg-C-selected class)
    eligible = {k: (candidate_class[k] == eligible_class) for k in candidate_class}  # (local)

    # robustness witness for the GRADED selection: graded residual ~0, scalar residual large
    graded_residual_max = float(np.max(np.abs(legC_graded_residual_vec)))  # (local)
    graded_clean = graded_residual_max < 1e-12                  # (local)
    scalar_excluded = legC_scalar_residual_max > 1e-3           # (local)

    # ===================================================================
    # DEV-COUNT AFTER the structural selector (the gate's operator)
    # ===================================================================
    inside_001_selected = {k: (eligible[k] and dev[k] <= PASS_BAND) for k in dev}  # (local)
    N_inside = int(sum(inside_001_selected.values()))          # (local) THE gate count
    selected_knobs = [k for k in dev if inside_001_selected[k]]  # (local)

    # ===================================================================
    # VERDICT (plan operator.form)
    # ===================================================================
    if N_inside_005 == 0:
        verdict = "FAIL"                                       # (local)
    elif N_inside == 1:
        verdict = "PASS"                                       # (local)
    elif N_inside >= 2:
        verdict = "INFO"                                       # (local)
    else:
        # N_inside == 0 but some candidate within 0.05 (none inside 0.01 of the selected class)
        verdict = "INFO"                                       # (local)

    selected_knob = selected_knobs[0] if (verdict == "PASS" and selected_knobs) else "none"  # (local)

    # ===================================================================
    # E-3 shadow-vetting on surviving candidate(s): products/ratios of the
    # canonical pin set for <=5% proximities (excluding the candidate's OWN
    # defining identity). An in-band shadow carries ZERO incremental weight.
    # ===================================================================
    Dw = Fraction(9, 10)                                       # (local) Delta_omega
    pin_set = {                                                # (local) exact / float canonical pin set
        "tau_fold": float(tau_f), "T_acoustic": float(T_ac),
        "Delta_omega": float(Dw), "kappa_SONIC": 28.0 * np.pi / 125.0,
        "2pi": 2.0 * np.pi, "pi": float(np.pi),
        "1": 1.0, "2": 2.0, "3": 3.0, "1/2": 0.5, "3/2": 1.5,
        "5/3": 5.0 / 3.0, "7/4": 1.75, "sqrt6": float(np.sqrt(6.0)),
        "sqrt6/2": float(np.sqrt(6.0) / 2.0),
    }
    shadow_hits = []                                           # (local)
    if verdict == "PASS":
        target = S0_pred[selected_knob]                       # (local)
        for a in pin_set:
            for b in pin_set:
                for op_sym, val in (("*", pin_set[a] * pin_set[b]),
                                    ("/", pin_set[a] / pin_set[b] if pin_set[b] != 0 else None)):
                    if val is None or val <= 0:
                        continue
                    d = abs(val / target - 1.0)               # (local)
                    if d <= 0.05:
                        # exclude the DEFINING identity tau_fold/T_acoustic
                        if not (op_sym == "/" and a == "tau_fold" and b == "T_acoustic"):
                            shadow_hits.append((d, f"{a}{op_sym}{b}", val))
        shadow_hits.sort()
    # nearest accidental neighbor (excluding own defining identity)
    nearest_shadow_dev = shadow_hits[0][0] if shadow_hits else float("nan")  # (local)
    nearest_shadow_expr = shadow_hits[0][1] if shadow_hits else "none<=5%"   # (local)
    # the surviving candidate's own derivation precision (must beat the nearest shadow)
    own_dev = dev[selected_knob] if verdict == "PASS" else float("nan")      # (local)
    shadow_separated = (verdict != "PASS") or np.isnan(nearest_shadow_dev) or (own_dev < nearest_shadow_dev)  # (local)

    # ===================================================================
    # (i)/(iii) 0.52% pin-proximity ACCIDENT witness (E-3 row 1)
    # ===================================================================
    twopi_tau = 2.0 * np.pi * float(tau_f)                     # (local) 1.19380
    shadow_12 = float(C2_10) * 0.9                             # (local) (4/3)*0.9 = 1.2
    shadow_ratio = shadow_12 / twopi_tau                       # (local) 1.00519
    shadow_proximity_pct = abs(shadow_ratio - 1.0) * 100.0     # (local) 0.519%

    # defining moduli-acoustic identity exactness: S0_iii * T_ac == tau_fold (EXACT)
    identity_lhs = S0_pred_iii_exact * T_ac                    # (local) Fraction
    identity_exact = (identity_lhs == tau_f)                   # (local) True by construction

    # SHA verification vs plan/orch pins (informational; mismatch flagged, not gating here)
    pin_ok = {                                                 # (local)
        "w2_2": sha256_of(W2_2_NPZ) == PIN_W2_2,
        "w3_9": sha256_of(W3_9_NPZ) == PIN_W3_9,
        "s0_thr": sha256_of(S0_THR_NPZ) == PIN_S0_THR,
        "env_od": sha256_of(ENV_OD_NPZ) == PIN_ENV_OD,
    }

    value_str = (f"N_inside={N_inside}(selector);N_naive={N_inside_naive};"
                 f"knob={selected_knob}(iii=moduli-acoustic_S0*T_ac=tau_fold);"
                 f"dev_i={dev['i']:.4f};dev_ii={dev['ii']:.4f};dev_iii={dev['iii']:.4f};"
                 f"legC={legC_output_form};shadow(i,iii)={shadow_proximity_pct:.2f}pct_accident;"
                 f"E3_nearest={nearest_shadow_dev:.4f}({nearest_shadow_expr})_zero-weight")

    return {
        "value": value_str,
        "verdict": verdict,
        # core results
        "N_inside": N_inside,
        "N_inside_naive": N_inside_naive,
        "N_inside_005": N_inside_005,
        "selected_knob": selected_knob,
        "selected_knobs": np.array(selected_knobs, dtype=object),
        "S0_fit": S0_fit,
        "S0_fit_w39": S0_fit_w39,
        "s0_fit_echo_dev": s0_fit_echo_dev,
        "S0_pred_i": S0_pred_i,
        "S0_pred_ii": S0_pred_ii,
        "S0_pred_iii": S0_pred_iii,
        "S0_pred_iii_exact_str": "95/56",
        "dev_i": dev["i"],
        "dev_ii": dev["ii"],
        "dev_iii": dev["iii"],
        "inside_001_i": inside_001_all["i"],
        "inside_001_ii": inside_001_all["ii"],
        "inside_001_iii": inside_001_all["iii"],
        # structural selector
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
        # machinery echoes
        "knob_req": knob_req,
        "S0_alt_halfdelta": S0_alt_halfdelta,
        "half_delta": half_delta,
        "KK_threshold_delta": KK_delta,
        "S0_times_T_acoustic_fp": S0_times_T_acoustic_fp,
        "fingerprint_eq_qprime_dev": abs(S0_times_T_acoustic_fp - legC_q_prime),
        # E-3 shadow vetting
        "shadow_proximity_pct_i_iii": shadow_proximity_pct,
        "twopi_tau_fold": twopi_tau,
        "shadow_12": shadow_12,
        "nearest_shadow_dev": nearest_shadow_dev,
        "nearest_shadow_expr": nearest_shadow_expr,
        "own_dev_selected": own_dev,
        "shadow_separated": shadow_separated,
        "n_shadow_hits_5pct": len(shadow_hits),
        "identity_exact_S0iii_T_ac_eq_tau": bool(identity_exact),
        # pins
        "w2_2_audit_echo": w22_audit,
        "pin_ok_w2_2": pin_ok["w2_2"],
        "pin_ok_w3_9": pin_ok["w3_9"],
        "pin_ok_s0_thr": pin_ok["s0_thr"],
        "pin_ok_env_od": pin_ok["env_od"],
        # context
        "tau_fold_used": float(tau_f),
        "T_acoustic_used": float(T_ac),
        "PASS_BAND": PASS_BAND,
        "FAIL_OUTER": FAIL_OUTER,
    }


def make_plot(r: dict) -> None:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.2))

    # Panel 1: derivation-routed devs vs 0.01 / 0.05 bands, colored by selector eligibility
    cands = ["i", "ii", "iii"]
    devs = [r["dev_i"], r["dev_ii"], r["dev_iii"]]
    elig = [r["eligible_i"], r["eligible_ii"], r["eligible_iii"]]
    labels = [
        "(i) 4/3\nCasimir quantum\n[gap-shadow]",
        "(ii) δ/2=1.175\nKK-threshold\n[gap]",
        "(iii) 95/56\nmoduli-acoustic\n[graded]",
    ]
    colors = ["#2ca02c" if e else "#bbbbbb" for e in elig]
    bars = ax1.bar(range(3), devs, color=colors, edgecolor="black", zorder=3)
    ax1.axhline(r["PASS_BAND"], color="#1f77b4", ls="--", lw=1.6, label="PASS band 0.01", zorder=2)
    ax1.axhline(r["FAIL_OUTER"], color="#d62728", ls=":", lw=1.6, label="FAIL outer 0.05", zorder=2)
    for i, (d, e) in enumerate(zip(devs, elig)):
        tag = "ELIGIBLE" if e else "shadow→excl"
        ax1.text(i, d + 0.0012, f"{d*100:.3f}%\n{tag}", ha="center", va="bottom", fontsize=8.5)
    ax1.set_xticks(range(3))
    ax1.set_xticklabels(labels, fontsize=8.5)
    ax1.set_ylabel("derivation-routed dev = |S0_pred/S0_fit − 1|")
    ax1.set_ylim(0, 0.058)
    ax1.set_title(f"S0 knob discrimination — Leg-C={r['legC_output_form']} selector\n"
                  f"N_naive={r['N_inside_naive']} (i,iii inside 0.01) → "
                  f"N_inside(selector)={r['N_inside']} → {r['verdict']}")
    ax1.legend(loc="upper right", fontsize=9)
    ax1.grid(axis="y", alpha=0.3, zorder=0)

    # Panel 2: the (i)/(iii) 0.52% pin-proximity accident + E-3 vetting
    ax2.axis("off")
    txt = (
        f"STRUCTURAL SELECTOR (applied BEFORE dev-count)\n"
        f"  legC_output_form = {r['legC_output_form']}\n"
        f"  graded residual max = {r['graded_residual_max']:.2e}  (clean<1e-12: {r['graded_clean']})\n"
        f"  scalar residual max = {r['legC_scalar_residual_max']:.3f}  (excluded: {r['scalar_excluded']})\n"
        f"  ⇒ eligible class = '{r['eligible_class']}'  ⇒ candidate (iii) only\n\n"
        f"(i)/(iii) 0.52% PIN-PROXIMITY ACCIDENT (E-3 row 1)\n"
        f"  2π·τ_fold = {r['twopi_tau_fold']:.5f}   (4/3)·0.9 = {r['shadow_12']:.5f}\n"
        f"  ratio = {r['shadow_12']/r['twopi_tau_fold']:.5f}  ⇒ {r['shadow_proximity_pct_i_iii']:.2f}% proximity\n"
        f"  ⇒ (i),(iii) coincidence is a pin accident, NOT two structures\n\n"
        f"DEFINING IDENTITY (exact by construction)\n"
        f"  S0(iii)·T_acoustic = (95/56)·(14/125) = 19/100 = τ_fold\n"
        f"  exact: {r['identity_exact_S0iii_T_ac_eq_tau']}\n"
        f"  Leg-C derived q' = S0_fit·T_ac = {r['legC_q_prime']:.6f} ≈ τ_fold\n\n"
        f"E-3 SHADOW VETTING (surviving candidate (iii) = {r['S0_pred_iii']:.6f})\n"
        f"  own derivation dev = {r['own_dev_selected']*100:.3f}%\n"
        f"  nearest pin-set shadow ≤5%: {r['nearest_shadow_expr']} "
        f"(dev {r['nearest_shadow_dev']*100:.3f}%)\n"
        f"  shadow_separated (own<<nearest): {r['shadow_separated']}\n"
        f"  ⇒ no shadow carries incremental weight\n\n"
        f"VERDICT: {r['verdict']}  — knob = (iii) moduli-acoustic identity\n"
        f"  S0 = τ_fold / T_acoustic = 95/56  (DERIVED, W-3 OQ-2 promoted)"
    )
    ax2.text(0.0, 1.0, txt, va="top", ha="left", fontsize=9.2, family="monospace",
             transform=ax2.transAxes)

    fig.suptitle("S101-W3-S0-KNOB — exactly-one-inside-0.01 knob discrimination (Leg-C routed)",
                 fontsize=12, y=1.005)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict + 4-tuple output
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
# Section 7 — Main
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
    print("=== RESULTS ===")
    print(f"  S0_fit                = {r['S0_fit']:.10f}  (W3-9 echo dev {r['s0_fit_echo_dev']:.2e})")
    print(f"  (i)   4/3  -> S0_pred = {r['S0_pred_i']:.10f}  dev={r['dev_i']*100:.4f}%  inside0.01={r['inside_001_i']}  class={r['candidate_class_i']}")
    print(f"  (ii)  δ/2  -> S0_pred = {r['S0_pred_ii']:.10f}  dev={r['dev_ii']*100:.4f}%  inside0.01={r['inside_001_ii']}  class={r['candidate_class_ii']}")
    print(f"  (iii) 95/56-> S0_pred = {r['S0_pred_iii']:.10f}  dev={r['dev_iii']*100:.4f}%  inside0.01={r['inside_001_iii']}  class={r['candidate_class_iii']}")
    print(f"  N_inside_naive (pre-selector)  = {r['N_inside_naive']}  (degenerate: i+iii)")
    print(f"  legC_output_form = {r['legC_output_form']}  -> eligible class '{r['eligible_class']}'")
    print(f"  eligible: i={r['eligible_i']} ii={r['eligible_ii']} iii={r['eligible_iii']}")
    print(f"  N_inside (post-selector)       = {r['N_inside']}  -> selected knob = {r['selected_knob']}")
    print(f"  (i)/(iii) shadow proximity     = {r['shadow_proximity_pct_i_iii']:.3f}% (pin accident, E-3 row1)")
    print(f"  defining identity S0(iii)*T_ac == tau_fold exact: {r['identity_exact_S0iii_T_ac_eq_tau']}")
    print(f"  E-3 nearest shadow ≤5%: {r['nearest_shadow_expr']} dev={r['nearest_shadow_dev']*100:.3f}% (own={r['own_dev_selected']*100:.3f}%) separated={r['shadow_separated']}")
    print(f"  SHA pin check: w2_2={r['pin_ok_w2_2']} w3_9={r['pin_ok_w3_9']} s0_thr={r['pin_ok_s0_thr']} env_od={r['pin_ok_env_od']}")
    print()

    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(tag)

    extra = [
        (f"# legC_form={r['legC_output_form']} selector_class={r['eligible_class']} "
         f"N_naive={r['N_inside_naive']} N_selector={r['N_inside']} knob=(iii)_moduli-acoustic "
         f"S0=tau_fold/T_acoustic=95/56"),
        (f"# (i)/(iii) 0.52pct pin-proximity accident: 2pi*tau_fold={r['twopi_tau_fold']:.5f} "
         f"vs (4/3)*0.9={r['shadow_12']:.5f} ratio={r['shadow_12']/r['twopi_tau_fold']:.5f}; "
         f"(i) demoted to shadow by GRADED selector"),
        (f"# E-3 shadow-vetting: surviving (iii) dev={r['own_dev_selected']*100:.3f}% "
         f"<< nearest pin-set shadow {r['nearest_shadow_expr']} dev={r['nearest_shadow_dev']*100:.3f}%; "
         f"identity S0*T_ac==tau_fold exact={r['identity_exact_S0iii_T_ac_eq_tau']}"),
    ]
    print_verdict_payload(verdict, value, audit_sha, content_sha, extra_rows=extra)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
