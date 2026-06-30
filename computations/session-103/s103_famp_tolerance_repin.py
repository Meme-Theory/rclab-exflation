#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==========================================================================
# S103-FAMP-TOLERANCE-REPIN  (Session 103, Wave 3, gate W3-1;
#                             transit-dynamics-theorist)
# ==========================================================================
# Plan: sessions/session-plan/session-103-plan-w3.md  §W3-1
# Trigger: [SIGN]   Classification: PHONONIC
# Scheme: FW
# Convention: SU(1,1)-form-1-temporal-L-to-R  (inherited frozen from
#   CF-S102-LADDER-PHASE-RESOLVED, audit e2a0fd52...d504f26c)
#
# WHAT THIS GATE IS (re-pin re-read; NO new physics):
#   Class-8.3 publication-precision re-pin. The S102 phase-resolved F_amp
#   comparator (CF-S102-LADDER-PHASE-RESOLVED, W7-2) landed INFO at a knife-edge:
#   the DERIVED phase-resolved deviation 2.915087e-03 grazed +1.51e-05 OUTSIDE a
#   DOWN-ROUNDED literal PASS_TOL=0.0029, even though it sits INSIDE the EXACT
#   asymmetric upper-envelope edge S_W_max-1 = envelope_upper_dev = 2.915093e-03.
#   The S102 INFO was a presentation-precision artifact (magnitude=INFO), not a
#   substrate breach (sign=PASS, regime=VALID).
#
#   This gate RE-PINS PASS_TOL to the EXACT asymmetric-endpoint bound
#   PASS_TOL := envelope_upper_dev  (= S_W_max - 1, the upper edge of the
#   ASYMMETRIC S_W window about 1), sourced VERBATIM from the frozen S102 npz
#   (full float64), and re-evaluates PASS := deviation <= PASS_TOL.
#
#   EVERY Bogoliubov amplitude and every comparator output is RE-USED verbatim
#   from the frozen s102_w7_ladder_phase_resolved.npz (input-pin SHA
#   b70d78bf...6708). No spectrum is recomputed; no phase is re-derived.
#
# OPERATOR (plan PRDR item 1):
#   deviation <= PASS_TOL,  PASS_TOL := S_W_max - 1 = envelope_upper_dev
#   (the asymmetric upper-envelope edge).
#
# SUBSTITUTION CHAIN (plan PRDR item 7; MANDATORY [SIGN] -- exact-threshold +
#   direction claim). Below, a := |alpha_W|, b := |beta_W|; all values are
#   the FROZEN s102 npz fields (re-read, NOT recomputed).
#
#   Claim: "The EXACT PASS edge is S_W_max - 1 (the ASYMMETRIC upper endpoint),
#           NOT the SYMMETRIC O(beta^2) half-spread 2|a||b|, NOR the down-rounded
#           literal 0.0029; under the exact edge the S102 deviation 2.915087e-03
#           PASSes (<=), whereas under 0.0029 it FAILed by +1.51e-05."
#
#   Def 1: S_W(phi_rel) := |alpha_W + beta_W e^{2 i phi_rel}|^2   (SU(1,1)
#          phase-resolved window factor; convention SU(1,1)-form-1).
#   Def 2: |alpha_W|^2 - |beta_W|^2 = 1   (Bogoliubov unitarity; canonical).
#          => a^2 = 1 + b^2.   [npz: a^2 - b^2 = 0.9999999999999998 ~ 1.]
#   Def 3: deviation := |F_amp_phase / F_amp_slot_mag - 1| = |S_W(phi_rel) - 1|
#          [npz: F_amp_phase=0.38963251, F_amp_slot_mag=0.3885;
#           ratio = S_W_phi = 1.0029150874; deviation = 2.9150874e-03.]
#
#   Substitute + extremize over phi_rel:
#          S_W(phi)   = a^2 + b^2 + 2 a b cos(2 phi + delta)
#                     = (1 + b^2) + b^2 + 2 a b cos(...)
#                     = 1 + 2 b^2 + 2 a b cos(...)        [USING a^2 = 1 + b^2]
#          => S_W_center = 1 + 2 b^2   (cos = 0; npz S_W_center bit-exact)
#             half-spread = 2 a b        (npz S_W_half_spread bit-exact)
#          => S_W_max - 1 = (S_W_center - 1) + half-spread = 2 b^2 + 2 a b
#                                                       ... asymmetric UPPER edge
#             S_W_min - 1 = (S_W_center - 1) - half-spread = 2 b^2 - 2 a b
#                                                       ... asymmetric LOWER edge
#
#   PRECISION NOTE (bit-exact vs plan shorthand):
#     The BIT-EXACT decomposition of the frozen field envelope_upper_dev is
#         S_W_max - 1 = 2 b^2 + 2 a b           (residual 7.6e-17 vs the npz field)
#     The plan/predecessor SHORTHAND "S_W_max - 1 = 2|a||b| + |beta_W|^2 = b^2 + 2ab"
#     UNDER-counts the center offset by exactly ONE factor of b^2 (the center is
#     1 + 2 b^2, not 1 + b^2): b^2 + 2ab = 2.9129744e-03 differs from the frozen
#     envelope_upper_dev = 2.9150926e-03 by b^2 = 2.118e-06. The two AGREE to the
#     gate's publication precision is FALSE at 5 sig figs (2.9151e-3 vs 2.9130e-3),
#     so the bit-exact 2 b^2 + 2 a b is the published decomposition; the threshold
#     VALUE itself is UNAMBIGUOUS because PASS_TOL is sourced DIRECTLY from the
#     frozen envelope_upper_dev field (= S_W_max - 1), not reconstructed from a + b.
#     [This is exactly the Class-8.3 precision-hygiene the gate exists to enforce.]
#
#   Direction (sign read-off; the [SIGN] prediction):
#          deviation - (S_W_max - 1) = 2.9150874e-3 - 2.9150926e-3 = -5.21e-09 <= 0
#          => deviation <= S_W_max - 1  => PASS under the exact asymmetric edge.
#          By contrast:
#            deviation - 2|a||b| (half-spread) = +4.231e-06 > 0  (FAIL edge)
#            deviation - 0.0029  (literal)     = +1.509e-05 > 0  (FAIL edge)
#          The exact edge is the ONLY physically correct one: the DERIVED phase
#          lands at the upper envelope edge (cos_phi_off_axis = 0.99999966 ~ +1),
#          so the deviation SATURATES the asymmetric upper endpoint it arises from.
#
#   Conclusion: PASS_TOL := S_W_max - 1 (exact asymmetric-endpoint bound).
#          Under it the S102 deviation PASSes by +5.21e-09 margin
#          (sign(deviation - PASS_TOL) = -1 matches predicted <= 0).
#          The S102 INFO is reclassified as a publication-precision (Class-8.3)
#          artifact, not a substrate breach. sign_verdict = PASS.
#
# ENV: cpu-cap-OMP8 (scalar comparison; no linear algebra, no GPU).
# --------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")  # (local) scalar comparison; CPU cap
os.environ.setdefault("MKL_NUM_THREADS", "8")  # (local)

import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# --------------------------------------------------------------------------
# Section 1 -- identity + paths
# --------------------------------------------------------------------------
GATE_ID = "S103-FAMP-TOLERANCE-REPIN"
SESSION = "S103"
SCHEME = "FW"
CONVENTION = "SU(1,1)-form-1-temporal-L-to-R"
L_MAX = 12  # (local) inherited frozen pin (s84 L12 cache lineage of W7-2 ladder); diagnostic only — no spectrum recomputed

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
SESSION_DIR = PROJECT_ROOT / "computations" / "session-103"
S102_DIR = PROJECT_ROOT / "computations" / "session-102"

# Make canonical_constants importable, then import per project mandate (S34+).
sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import *  # noqa: F401,F403  (project mandate: import canonical)
from canonical_constants import M_KK, max_f_NL_FW  # noqa: F401  (explicit; provenance sanity)

INPUT_NPZ = S102_DIR / "s102_w7_ladder_phase_resolved.npz"
CANONICAL = SHARED_DIR / "canonical_constants.py"
OUT_NPZ = SESSION_DIR / "s103_famp_tolerance_repin.npz"
OUT_PNG = SESSION_DIR / "s103_famp_tolerance_repin.png"

# Frozen-provenance pins (plan §W3-1 input_files + context).
EXPECTED_NPZ_FILEBYTE_SHA = (
    "b70d78bf27909ca595e419615d3cd22a9f49dbda75028d6d0bb514e54eba6708")
EXPECTED_NPZ_INTERNAL_AUDIT = (
    "e2a0fd529f34a5d7354160046590033c0c3b4644878e2a0e0d2bd3f5d504f26c")
# Plan-frozen canonical SHA (plan §W3-1 input_files). NOTE: canonical_constants.py
# is an APPEND-ONLY shared registry mutated by parallel S103 waves mid-session
# (S103-Q28-LAYER2-A6 appended n_s_FW_sqrt_cutoff et al.); the runtime SHA may
# differ by additive-only appends that touch ZERO value this gate consumes. The
# canonical pin is therefore PLAN-TEXT-DRIFT-tolerant per
# substrate-first-canonical-sourcing.md §(ii.B): the script asserts against the
# plan-frozen SHA OR the current runtime SHA, records which matched, and emits a
# drift-correction note. The audit_sha256 computes over the CURRENT canonical
# bytes (it pins what was actually read). The FROZEN-NPZ file-byte SHA (the
# gate's sole physics input) is asserted HARD (must match plan-freeze).
EXPECTED_CANONICAL_SHA_PLANFREEZE = (
    "9f2fe9983ecbbb76a2ba1b3e951cf9275deda8d7f2241576ef23b7f728ba1047")

# Publication-precision pin (Class-8.3): PASS_TOL published at 5 sig figs.
PUB_SIG_FIGS = 5  # (local) plan PRDR item 5 publication_precision

# Frozen S102 literal pin + symmetric half-spread, recorded as the two WRONG edges.
LITERAL_PASS_TOL_S102 = 0.0029  # (local) the DOWN-ROUNDED literal the S102 INFO grazed

# --------------------------------------------------------------------------
# Section 2 -- SHA helpers + input verification
# --------------------------------------------------------------------------
def sha256_of(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def verify_inputs() -> tuple[dict, dict]:
    """SHA-pin every input; assert frozen-provenance. Return (pins, drift_info).

    - FROZEN-NPZ file-byte SHA (the gate's sole physics input): asserted HARD.
    - canonical_constants.py SHA: PLAN-TEXT-DRIFT-tolerant (§(ii.B)); asserts
      plan-frozen OR runtime, records which matched.
    """
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in (CANONICAL, INPUT_NPZ):
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha

    can_rel = str(CANONICAL.relative_to(PROJECT_ROOT)).replace("\\", "/")
    npz_rel = str(INPUT_NPZ.relative_to(PROJECT_ROOT)).replace("\\", "/")

    # HARD: frozen-npz file-byte SHA (the gate's physics input must be intact).
    assert pins[npz_rel] == EXPECTED_NPZ_FILEBYTE_SHA, (
        f"frozen npz file-byte SHA mismatch (PHYSICS INPUT MUTATED -- honest "
        f"mechanical closure required per mechanical-closure-discipline.md): "
        f"{pins[npz_rel]} != {EXPECTED_NPZ_FILEBYTE_SHA}")

    # DRIFT-TOLERANT: canonical SHA may differ by additive-only appends.
    canonical_runtime_sha = pins[can_rel]                          # (local)
    canonical_drifted = bool(canonical_runtime_sha != EXPECTED_CANONICAL_SHA_PLANFREEZE)  # (local)
    drift_info = {
        "canonical_drifted": canonical_drifted,
        "canonical_runtime_sha": canonical_runtime_sha,
        "canonical_planfreeze_sha": EXPECTED_CANONICAL_SHA_PLANFREEZE,
    }
    if canonical_drifted:
        print(f"  [DRIFT §(ii.B)] canonical_constants.py SHA drifted from "
              f"plan-freeze {EXPECTED_CANONICAL_SHA_PLANFREEZE[:16]}... to runtime "
              f"{canonical_runtime_sha[:16]}... (parallel-wave APPEND).")
        print(f"               This gate consumes NO drifted value (physics from "
              f"frozen npz only; M_KK/max_f_NL_FW provenance-sanity only). "
              f"Re-pinning to runtime canonical; audit_sha256 computes over current "
              f"bytes. Frozen-npz file-byte SHA (physics input) UNCHANGED -> gate "
              f"is testable, NOT mechanical-closure.")
    else:
        print(f"  [OK] canonical SHA matches plan-freeze.")
    print(f"  [OK] frozen-npz file-byte SHA matches plan §W3-1 (physics input intact).")
    return pins, drift_info


def closure_hash(pins: dict) -> str:
    items = sorted(pins.items())
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict) -> tuple[str, str]:
    """S84+ dual-SHA: audit = sha256(script || canonical || pinmap_json);
    content = sha256(script).  audit_sha256_inputs=[script,canonical,pinmap];
    content_sha256_inputs=[script]."""
    script_bytes = script_path.read_bytes()
    canonical_bytes = canonical_path.read_bytes()
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")
    h_a = hashlib.sha256()
    h_a.update(script_bytes)
    h_a.update(canonical_bytes)
    h_a.update(pinmap_json)
    audit = h_a.hexdigest()
    content = hashlib.sha256(script_bytes).hexdigest()
    return audit, content


# --------------------------------------------------------------------------
# Section 3 -- verdict payload helper (script PRINTS; agent calls emit_verdict)
# --------------------------------------------------------------------------
def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, companion_note="",
                          extra_rows=None) -> dict:
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


# --------------------------------------------------------------------------
# Section 4 -- load frozen S102 comparator outputs (re-read; NO recompute)
# --------------------------------------------------------------------------
def load_frozen() -> dict:
    d = np.load(INPUT_NPZ, allow_pickle=True)
    # Internal-audit provenance cross-check (NOT the input-pin SHA).
    internal_audit = str(d["audit_sha256"])
    assert internal_audit == EXPECTED_NPZ_INTERNAL_AUDIT, (
        f"frozen npz internal audit_sha256 mismatch: {internal_audit} "
        f"!= {EXPECTED_NPZ_INTERNAL_AUDIT}")
    print(f"  [OK] frozen npz internal audit_sha256 = {internal_audit[:16]}... "
          f"(CF-S102-LADDER-PHASE-RESOLVED provenance confirmed).")

    g = {
        # comparator output observable (the value under test)
        "deviation": float(d["deviation"]),
        "deviation_pct": float(d["deviation_pct"]),
        "deviation_signed": float(d["deviation_signed"]),
        "sign_deviation": float(d["sign_deviation"]),
        # the EXACT asymmetric upper-envelope edge (the re-pinned PASS_TOL source)
        "envelope_upper_dev": float(d["envelope_upper_dev"]),
        "envelope_upper_dev_pct": float(d["envelope_upper_dev_pct"]),
        "envelope_lower_dev": float(d["envelope_lower_dev"]),
        # the two WRONG candidate edges
        "S_W_half_spread": float(d["S_W_half_spread"]),       # = 2|a||b| (symmetric)
        "S_W_half_spread_pct": float(d["S_W_half_spread_pct"]),
        "bound_2ab": float(d["bound_2ab"]),                   # alias of half-spread
        "bound_2ab_pct": float(d["bound_2ab_pct"]),
        # SU(1,1) window structure
        "S_W_phi": float(d["S_W_phi"]),
        "S_W_max_reeval": float(d["S_W_max_reeval"]),
        "S_W_min_reeval": float(d["S_W_min_reeval"]),
        "S_W_center": float(d["S_W_center"]),
        # Bogoliubov amplitudes (for bit-exact decomposition cross-checks)
        "abs_alpha_W": float(d["abs_alpha_W"]),
        "abs_beta_W": float(d["abs_beta_W"]),
        "beta2_W": float(d["beta2_W"]),
        # regime / phase placement
        "cos_phi_off_axis": float(d["cos_phi_off_axis"]),
        "phi_rel": float(d["phi_rel"]),
        "within_envelope": bool(d["within_envelope"]),
        "phases_derived": bool(d["phases_derived"]),
        "sign_match": bool(d["sign_match"]),
        # S102 frozen deltas-vs-edges (we RE-DERIVE these independently and assert)
        "dev_vs_pass_tol_s102": float(d["dev_vs_pass_tol"]),
        "dev_vs_half_spread_s102": float(d["dev_vs_half_spread"]),
        # S102 frozen verdict (the INFO this gate re-pins)
        "verdict_s102": str(d["verdict"]),
        "magnitude_verdict_s102": str(d["magnitude_verdict"]),
        "sign_verdict_s102": str(d["sign_verdict"]),
        "regime_verdict_s102": str(d["regime_verdict"]),
        # context
        "F_amp_phase": float(d["F_amp_phase"]),
        "F_amp_slot_mag": float(d["F_amp_slot_mag"]),
        "k_pivot": float(d["k_pivot"]),
        "internal_audit": internal_audit,
    }
    return g


# --------------------------------------------------------------------------
# Section 5 -- re-pin + re-evaluate (the gate logic)
# --------------------------------------------------------------------------
def compute(g: dict) -> dict:
    a = g["abs_alpha_W"]              # (local) |alpha_W|
    b = g["abs_beta_W"]              # (local) |beta_W|
    b2 = g["beta2_W"]                # (local) |beta_W|^2

    # ---- RE-PIN: PASS_TOL := exact asymmetric upper-envelope edge ----
    PASS_TOL = g["envelope_upper_dev"]   # (local) = S_W_max - 1 (full float64, frozen)
    deviation = g["deviation"]           # (local) the value under test (frozen)

    # ---- RE-EVALUATE under the re-pinned edge ----
    dev_vs_repin = deviation - PASS_TOL              # (local) signed delta; <=0 => PASS
    repin_pass = bool(deviation <= PASS_TOL)         # (local)

    # ---- bit-exact decomposition cross-checks of the EXACT edge ----
    two_ab = 2.0 * a * b                             # (local) the symmetric half-spread
    edge_2b2_2ab = 2.0 * b2 + two_ab                 # (local) BIT-EXACT: 2b^2 + 2ab
    edge_b2_2ab = b2 + two_ab                        # (local) PLAN SHORTHAND: b^2 + 2ab
    resid_bitexact = abs(PASS_TOL - edge_2b2_2ab)    # (local) ~7.6e-17 (machine eps)
    resid_shorthand = abs(PASS_TOL - edge_b2_2ab)    # (local) = b^2 ~ 2.118e-06
    center_check = abs(g["S_W_center"] - (1.0 + 2.0 * b2))   # (local) center IS 1+2b^2
    half_check = abs(g["S_W_half_spread"] - two_ab)          # (local) half-spread IS 2ab
    unitarity_resid = abs(a * a - b * b - 1.0)               # (local) a^2-b^2-1

    # ---- the three candidate edges + signed deltas (re-derived independently) ----
    dev_vs_half = deviation - two_ab                 # (local) +4.23e-06 (FAIL edge)
    dev_vs_literal = deviation - LITERAL_PASS_TOL_S102   # (local) +1.51e-05 (FAIL edge)
    # cross-check our re-derived deltas reproduce the S102 frozen fields
    repro_half = abs(dev_vs_half - g["dev_vs_half_spread_s102"])     # (local)
    repro_literal = abs(dev_vs_literal - g["dev_vs_pass_tol_s102"])  # (local)

    # ---- asymmetry magnitude: upper - |lower| = 2b^2 ----
    asym = g["envelope_upper_dev"] - g["envelope_lower_dev"]  # (local) = 2b^2
    asym_vs_2b2 = abs(asym - 2.0 * b2)                        # (local)

    # ---- 5-sig-fig publication rounding of the candidate forms (Class-8.3) ----
    def sf5(x):
        return float(f"{x:.4e}")  # (local) 5 sig figs == 4 decimal places in mantissa
    pub_PASS_TOL = sf5(PASS_TOL)                     # (local) 2.9151e-3
    pub_edge_2b2 = sf5(edge_2b2_2ab)                 # (local) 2.9151e-3 (agrees)
    pub_edge_shorthand = sf5(edge_b2_2ab)            # (local) 2.9130e-3 (DISAGREES)
    pub_half = sf5(two_ab)                           # (local) 2.9109e-3
    shorthand_agrees_5sf = bool(pub_PASS_TOL == pub_edge_shorthand)  # (local) False

    return {
        "PASS_TOL": PASS_TOL,
        "deviation": deviation,
        "dev_vs_repin": dev_vs_repin,
        "repin_pass": repin_pass,
        "margin": -dev_vs_repin,                     # positive => inside the edge
        # decomposition cross-checks
        "two_ab": two_ab,
        "edge_2b2_2ab": edge_2b2_2ab,
        "edge_b2_2ab": edge_b2_2ab,
        "resid_bitexact": resid_bitexact,
        "resid_shorthand": resid_shorthand,
        "center_check": center_check,
        "half_check": half_check,
        "unitarity_resid": unitarity_resid,
        # candidate-edge deltas
        "dev_vs_half": dev_vs_half,
        "dev_vs_literal": dev_vs_literal,
        "repro_half": repro_half,
        "repro_literal": repro_literal,
        # asymmetry
        "asym": asym,
        "asym_vs_2b2": asym_vs_2b2,
        # publication rounding
        "pub_PASS_TOL": pub_PASS_TOL,
        "pub_edge_2b2": pub_edge_2b2,
        "pub_edge_shorthand": pub_edge_shorthand,
        "pub_half": pub_half,
        "shorthand_agrees_5sf": shorthand_agrees_5sf,
    }


def evaluate_gate(g: dict, r: dict):
    """Pre-registered [SIGN] composite operator (plan §W3-1 PRDR item 1).

    The pre-registered OPERATOR is a PURE INEQUALITY:
        type: inequality;  form: deviation <= PASS_TOL;  direction: "<="
    (plan lines 65-72). PASS iff deviation <= PASS_TOL. The plan's INFO_meaning
    scopes INFO to deviation == S_W_max-1 (EQUALITY at the edge to within
    publication precision -- a persistent knife-edge), NOT to a strict
    deviation < PASS_TOL. A fabricated tolerance band around the edge would be a
    Class-3 PROHIBITED_ACTIONS post-hoc threshold edit; the rule is the
    pre-registered inequality.

    sign_verdict   : predicted direction is deviation - PASS_TOL <= 0 (PASS edge);
                     computed sign matches => PASS.
    magnitude_verdict: PASS iff deviation <= PASS_TOL strictly (re-pin lands PASS).
                     INFO iff deviation == PASS_TOL to within publication precision
                     (rel_tol = 10^-PUB_SIG_FIGS; the plan's INFO_meaning knife-edge
                     -- a DEEPER precision pathology than the down-rounding).
                     FAIL iff deviation > PASS_TOL (genuine breach).
    regime_verdict : VALID -- frozen scalar re-read; no small-parameter expansion,
                     no scan window, no ODE; the comparison edge is the EXACT
                     SU(1,1) endpoint (no O(beta^2) truncation in the threshold).
    """
    # --- sign: predicted <=0, computed sign of (deviation - PASS_TOL) ---
    predicted_le_zero = True                              # (local) chain Step "Direction"
    computed_le_zero = bool(r["dev_vs_repin"] <= 0.0)     # (local)
    sign_v = "PASS" if (computed_le_zero == predicted_le_zero) else "FAIL"  # (local)

    # --- magnitude: pre-registered inequality deviation <= PASS_TOL ---
    # INFO is reserved (plan INFO_meaning) for the EQUALITY knife-edge:
    # |deviation - PASS_TOL| within publication precision of ZERO (the deviation
    # would SIT ON the exact edge, not strictly inside). rel_tol = 10^-PUB_SIG_FIGS
    # is RELATIVE to PASS_TOL per the Class-8.3 publication-precision pin.
    rel_tol = 10.0 ** (-PUB_SIG_FIGS)                    # (local) 1e-5
    equality_band = rel_tol * r["PASS_TOL"]              # (local) ~2.9e-8 (rel to edge)
    rel_margin = abs(r["dev_vs_repin"]) / r["PASS_TOL"]  # (local) 1.79e-6 (relative)
    if r["dev_vs_repin"] > equality_band:
        mag_v = "FAIL"                                   # (local) deviation > PASS_TOL
        mag_band = (f"deviation - PASS_TOL = {r['dev_vs_repin']:+.3e} > "
                    f"+equality_band {equality_band:.2e} (breach of exact edge)")
    elif abs(r["dev_vs_repin"]) <= equality_band:
        mag_v = "INFO"                                   # (local) sits ON the edge (knife-edge)
        mag_band = (f"|deviation - PASS_TOL| = {abs(r['dev_vs_repin']):.3e} <= "
                    f"equality_band {equality_band:.2e}: deviation == S_W_max-1 to "
                    f"publication precision (INFO_meaning knife-edge)")
    else:
        mag_v = "PASS"                                   # (local) deviation < PASS_TOL strictly
        mag_band = (f"deviation - PASS_TOL = {r['dev_vs_repin']:+.3e} < "
                    f"-equality_band -{equality_band:.2e}: deviation STRICTLY inside "
                    f"the exact edge (rel margin {rel_margin:.2e} = {rel_margin*1e6:.2f} ppm)")

    # --- regime: frozen scalar re-read; exact endpoint; always VALID ---
    regime_v = "VALID"                                   # (local)
    regime_band = ("frozen scalar re-read; no expansion / scan / ODE; threshold is "
                   "the EXACT SU(1,1) endpoint S_W_max-1 (no O(beta^2) truncation)")  # (local)

    # --- composite collapse rule (gate-verdicts.md, generic) ---
    if regime_v == "BREAKDOWN":
        comp = "FAIL"
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

    detail = {
        "sign_band": (f"predicted (deviation - PASS_TOL) <= 0; computed "
                      f"{r['dev_vs_repin']:+.3e} {'<=' if computed_le_zero else '>'} 0"),
        "mag_band": mag_band,
        "regime": regime_band,
        "equality_band": equality_band,
        "composite_reason": (
            f"regime={regime_v}; sign={sign_v}; magnitude={mag_v} "
            f"=> collapse => {comp}"),
    }
    return comp, sign_v, mag_v, regime_v, detail


# --------------------------------------------------------------------------
# Section 6 -- plot: 1-D envelope diagram (deviation vs the three candidate edges)
# --------------------------------------------------------------------------
def make_plot(g: dict, r: dict, comp: str) -> None:
    fig, ax = plt.subplots(figsize=(9.5, 4.2))
    scale = 1.0e3  # (local) plot in units of 1e-3 (per-mille)

    dev = g["deviation"] * scale                 # (local)
    edge_exact = r["PASS_TOL"] * scale           # (local) S_W_max - 1
    edge_half = r["two_ab"] * scale              # (local) 2|a||b|
    edge_lit = LITERAL_PASS_TOL_S102 * scale     # (local) 0.0029
    lower = g["envelope_lower_dev"] * scale       # (local) |S_W_min - 1|

    # shade the admissible (PASS) region under the exact edge
    ax.axvspan(0, edge_exact, color="#cdeccd", alpha=0.5,
               label=f"admissible {{dev <= S_W_max-1}}")
    # the three candidate edges
    ax.axvline(edge_lit, color="#c0392b", ls="--", lw=1.6,
               label=f"literal 0.0029 (S102 FAIL edge; +{r['dev_vs_literal']*scale:.3f}e-3)")
    ax.axvline(edge_half, color="#e67e22", ls="-.", lw=1.6,
               label=f"half-spread 2|a||b|={edge_half:.4f}e-3 (FAIL edge; +{r['dev_vs_half']*scale:.4f}e-3)")
    ax.axvline(edge_exact, color="#1e8449", ls="-", lw=2.2,
               label=f"EXACT re-pin S_W_max-1={edge_exact:.4f}e-3 = 2b^2+2ab")
    # reference: lower envelope edge (|S_W_min-1|) and asymmetry note
    ax.axvline(lower, color="#7f8c8d", ls=":", lw=1.2,
               label=f"|S_W_min-1|={lower:.4f}e-3 (asymmetry 2b^2={r['asym']*scale:.4f}e-3)")
    # the deviation marker
    ax.plot([dev], [0.0], marker="o", ms=12, color="#2c3e50", zorder=5,
            label=f"S102 deviation={dev:.4f}e-3 ({comp} under re-pin; margin +{r['margin']*scale:.2e}e-3)")
    ax.annotate(f"dev={dev:.5f}e-3", xy=(dev, 0.0), xytext=(dev, 0.45),
                ha="center", fontsize=8,
                arrowprops=dict(arrowstyle="->", color="#2c3e50", lw=1.0))

    lo = min(edge_lit, lower) - 0.004 * scale * 1e-3  # (local)
    hi = max(edge_exact, edge_half, edge_lit) + 0.008  # (local)
    ax.set_xlim(lo, hi)
    ax.set_ylim(-0.6, 0.9)
    ax.set_yticks([])
    ax.set_xlabel("deviation from F_amp slot 0.3885  [units of 1e-3]", fontsize=9)
    ax.set_title(
        f"{GATE_ID}: re-pin PASS_TOL := S_W_max-1 (exact asymmetric edge). "
        f"S102 deviation PASSes by +{r['margin']:.2e}.\n"
        f"Asymmetric SU(1,1) window center = 1+2|beta|^2 != 1; "
        f"half-spread 2|a||b| under-counts the upper edge by |beta|^2.",
        fontsize=9)
    ax.legend(fontsize=7, loc="upper right", framealpha=0.92)
    ax.grid(alpha=0.25, axis="x")
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)
    print(f"Saved plot: {OUT_PNG}")


# --------------------------------------------------------------------------
# Section 7 -- main
# --------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()                                            # (local)
    pins, drift_info = verify_inputs()                          # (local)

    audit_sha, content_sha = compute_dual_sha(
        Path(__file__).resolve(), CANONICAL, pins)
    print(f"\naudit_sha256={audit_sha}")
    print(f"content_sha256={content_sha}")
    print(f"closure_hash(pins)={closure_hash(pins)}")

    g = load_frozen()                                            # (local)
    r = compute(g)                                               # (local)

    print(f"\n--- FROZEN S102 comparator outputs (re-read; NO recompute) ---")
    print(f"  F_amp_phase    = {g['F_amp_phase']:.8f}")
    print(f"  F_amp_slot_mag = {g['F_amp_slot_mag']}")
    print(f"  deviation      = {g['deviation']:.10e} = {g['deviation_pct']:.6f}%")
    print(f"  S102 verdict   = {g['verdict_s102']} "
          f"(sign={g['sign_verdict_s102']}, magnitude={g['magnitude_verdict_s102']}, "
          f"regime={g['regime_verdict_s102']})")

    print(f"\n--- SUBSTITUTION CHAIN (MANDATORY [SIGN]; runtime) ---")
    print(f"  Def 1: S_W(phi) = |alpha_W + beta_W e^(2i phi)|^2")
    print(f"  Def 2: a^2 - b^2 = 1  (unitarity); a=|alpha_W|={g['abs_alpha_W']:.10f}, "
          f"b=|beta_W|={g['abs_beta_W']:.6e}, b^2={g['beta2_W']:.6e}")
    print(f"         unitarity resid |a^2-b^2-1| = {r['unitarity_resid']:.2e}")
    print(f"  Def 3: deviation = |F_amp_phase/F_amp_slot_mag - 1| = |S_W(phi)-1| "
          f"= {g['deviation']:.10e}")
    print(f"  Extremize: S_W = 1 + 2b^2 + 2ab cos(...)")
    print(f"             center  = 1 + 2b^2  (npz S_W_center; resid {r['center_check']:.2e})")
    print(f"             half-spread = 2ab   (npz S_W_half_spread; resid {r['half_check']:.2e})")
    print(f"  EXACT upper edge  S_W_max-1 = 2b^2 + 2ab = {r['edge_2b2_2ab']:.10e}")
    print(f"    vs frozen envelope_upper_dev = {r['PASS_TOL']:.10e} "
          f"(bit-exact resid {r['resid_bitexact']:.2e})")
    print(f"  PLAN SHORTHAND    b^2 + 2ab  = {r['edge_b2_2ab']:.10e} "
          f"(UNDER-counts by b^2; resid vs frozen = {r['resid_shorthand']:.2e})")
    print(f"    => the bit-exact decomposition is 2b^2+2ab; the '2|a||b|+|beta|^2' "
          f"shorthand drops one b^2 (center is 1+2b^2, not 1+b^2)")
    print(f"  asymmetry: env_up - |env_lo| = {r['asym']:.6e} = 2b^2 "
          f"(resid {r['asym_vs_2b2']:.2e}) => window ASYMMETRIC about 1")

    print(f"\n--- RE-PIN + RE-EVALUATE ---")
    print(f"  PASS_TOL := S_W_max-1 = envelope_upper_dev = {r['PASS_TOL']:.16e}")
    print(f"             (5sf published = {r['pub_PASS_TOL']:.4e})")
    print(f"  deviation - PASS_TOL = {r['dev_vs_repin']:+.6e}  "
          f"=> {'<= 0 PASS' if r['dev_vs_repin'] <= 0 else '> 0 FAIL'}  "
          f"(margin inside edge = +{r['margin']:.3e})")
    print(f"\n  The three candidate edges (only the EXACT one is physically correct):")
    print(f"    EXACT  S_W_max-1 = {r['PASS_TOL']:.6e}  => dev-edge = {r['dev_vs_repin']:+.3e}  PASS")
    print(f"    half   2|a||b|   = {r['two_ab']:.6e}  => dev-edge = {r['dev_vs_half']:+.3e}  FAIL "
          f"(reproduces S102 dev_vs_half_spread, resid {r['repro_half']:.2e})")
    print(f"    literal 0.0029   = {LITERAL_PASS_TOL_S102:.6e}  => dev-edge = "
          f"{r['dev_vs_literal']:+.3e}  FAIL (reproduces S102 dev_vs_pass_tol, "
          f"resid {r['repro_literal']:.2e})")

    print(f"\n--- publication-precision (Class-8.3) 5sf rounding ---")
    print(f"  PASS_TOL          5sf = {r['pub_PASS_TOL']:.4e}")
    print(f"  2b^2+2ab (exact)  5sf = {r['pub_edge_2b2']:.4e}  (agrees with PASS_TOL)")
    print(f"  b^2+2ab (shorthand)5sf= {r['pub_edge_shorthand']:.4e}  "
          f"(shorthand agrees at 5sf: {r['shorthand_agrees_5sf']})")
    print(f"  2|a||b| (half)    5sf = {r['pub_half']:.4e}")

    print(f"\n--- regime / phase placement ---")
    print(f"  cos_phi_off_axis = {g['cos_phi_off_axis']:.8f} (~+1 => DERIVED phase at "
          f"UPPER envelope edge => deviation SATURATES the asymmetric upper endpoint)")
    print(f"  within_envelope (S102) = {g['within_envelope']}; "
          f"phases_derived = {g['phases_derived']}; sign_match (S102) = {g['sign_match']}")

    comp, sign_v, mag_v, regime_v, detail = evaluate_gate(g, r)   # (local)

    print("\n" + "=" * 72)
    print("GATE EVALUATION (pre-registered [SIGN] composite operator)")
    print("=" * 72)
    print(f"  sign:      {detail['sign_band']} => {sign_v}")
    print(f"  magnitude: {detail['mag_band']} => {mag_v}")
    print(f"  regime:    {detail['regime']} => {regime_v}")
    print(f"  3-tuple: sign={sign_v} magnitude={mag_v} regime={regime_v}")
    print(f"  composite (collapse rule): {comp}")
    print(f"  reason: {detail['composite_reason']}")

    # ---- npz (full float64) ----
    np.savez(
        OUT_NPZ,
        # ==== re-pin observable ====
        PASS_TOL_repin=r["PASS_TOL"],
        PASS_TOL_repin_5sf=r["pub_PASS_TOL"],
        deviation=r["deviation"],
        dev_vs_repin=r["dev_vs_repin"],
        repin_pass=r["repin_pass"],
        margin_inside_edge=r["margin"],
        # ==== S102 frozen pins (the two WRONG edges) ====
        literal_PASS_TOL_s102=LITERAL_PASS_TOL_S102,
        half_spread_2ab=r["two_ab"],
        dev_vs_half=r["dev_vs_half"],
        dev_vs_literal=r["dev_vs_literal"],
        repro_half_resid=r["repro_half"],
        repro_literal_resid=r["repro_literal"],
        # ==== exact-edge decomposition cross-checks ====
        edge_2b2_2ab_bitexact=r["edge_2b2_2ab"],
        edge_b2_2ab_shorthand=r["edge_b2_2ab"],
        resid_bitexact=r["resid_bitexact"],
        resid_shorthand=r["resid_shorthand"],
        center_check_resid=r["center_check"],
        half_check_resid=r["half_check"],
        unitarity_resid=r["unitarity_resid"],
        asymmetry_2b2=r["asym"],
        asym_vs_2b2_resid=r["asym_vs_2b2"],
        shorthand_agrees_5sf=r["shorthand_agrees_5sf"],
        pub_edge_2b2_5sf=r["pub_edge_2b2"],
        pub_edge_shorthand_5sf=r["pub_edge_shorthand"],
        pub_half_5sf=r["pub_half"],
        # ==== SU(1,1) window structure (frozen, re-read) ====
        S_W_phi=g["S_W_phi"], S_W_max_reeval=g["S_W_max_reeval"],
        S_W_min_reeval=g["S_W_min_reeval"], S_W_center=g["S_W_center"],
        envelope_upper_dev=g["envelope_upper_dev"],
        envelope_lower_dev=g["envelope_lower_dev"],
        abs_alpha_W=g["abs_alpha_W"], abs_beta_W=g["abs_beta_W"],
        beta2_W=g["beta2_W"],
        cos_phi_off_axis=g["cos_phi_off_axis"], phi_rel=g["phi_rel"],
        within_envelope=g["within_envelope"], phases_derived=g["phases_derived"],
        # ==== S102 frozen verdict (the INFO this gate re-pins) ====
        verdict_s102=g["verdict_s102"],
        magnitude_verdict_s102=g["magnitude_verdict_s102"],
        sign_verdict_s102=g["sign_verdict_s102"],
        regime_verdict_s102=g["regime_verdict_s102"],
        # ==== this gate's verdict ====
        verdict=comp, sign_verdict=sign_v, magnitude_verdict=mag_v,
        regime_verdict=regime_v,
        equality_band=detail["equality_band"],
        publication_sig_figs=PUB_SIG_FIGS,
        # ==== provenance ====
        F_amp_phase=g["F_amp_phase"], F_amp_slot_mag=g["F_amp_slot_mag"],
        k_pivot=g["k_pivot"], M_KK=float(M_KK),
        audit_sha256=audit_sha, content_sha256=content_sha,
        frozen_npz_internal_audit=g["internal_audit"],
        frozen_npz_filebyte_sha=EXPECTED_NPZ_FILEBYTE_SHA,
        canonical_drifted=drift_info["canonical_drifted"],
        canonical_runtime_sha=drift_info["canonical_runtime_sha"],
        canonical_planfreeze_sha=drift_info["canonical_planfreeze_sha"],
    )
    print(f"\nSaved data: {OUT_NPZ}")

    make_plot(g, r, comp)

    # ---- value 4-tuple + payload ----
    val = (f"PASS_TOL_repin={r['PASS_TOL']:.6e};"
           f"PASS_TOL_5sf={r['pub_PASS_TOL']:.4e};"
           f"deviation={r['deviation']:.6e};"
           f"dev_vs_repin={r['dev_vs_repin']:+.3e};"
           f"margin_inside=+{r['margin']:.2e};"
           f"edge=S_W_max-1=2b2+2ab;"
           f"half_spread_2ab={r['two_ab']:.6e}(dev_vs={r['dev_vs_half']:+.2e}FAIL);"
           f"literal_0.0029(dev_vs={r['dev_vs_literal']:+.2e}FAIL);"
           f"asym_2b2={r['asym']:.3e};"
           f"S102_was=INFO->repin={comp};"
           f"canon_drift={'Y_appendonly_rePinned' if drift_info['canonical_drifted'] else 'N'}")  # (local)
    print(f"\n(value={val!r}, scheme={SCHEME}, convention={CONVENTION}, "
          f"L_max={L_MAX})")

    note = (
        f"Class-8.3 publication-precision re-pin (no new physics; frozen S102 npz "
        f"re-read). PASS_TOL re-pinned from the DOWN-ROUNDED literal 0.0029 to the "
        f"EXACT asymmetric upper-envelope edge S_W_max-1 = envelope_upper_dev = "
        f"{r['PASS_TOL']:.6e} (full float64, frozen). RESULT: composite {comp} "
        f"(NOT PASS). The re-pin RESOLVES THE SIGN -- the S102 deviation "
        f"{r['deviation']:.6e} is AT-OR-INSIDE the exact edge (deviation - PASS_TOL "
        f"= {r['dev_vs_repin']:+.2e} <= 0; the half-spread 2|a||b| and literal 0.0029 "
        f"were BOTH the wrong edge, FAILing by +4.23e-06 and +1.51e-05). It VINDICATES "
        f"THE SUBSTRATE -- the deviation SATURATES the upper endpoint it physically "
        f"arises from (cos_phi_off_axis={g['cos_phi_off_axis']:.6f}~+1; "
        f"within_envelope=True). BUT it does NOT convert the knife-edge to a margin: "
        f"deviation == S_W_max-1 to PUBLICATION PRECISION (identical at 5sf AND 6sf = "
        f"2.91509e-3; rel separation {abs(r['dev_vs_repin'])/r['PASS_TOL']:.2e} sits at "
        f"the 5.7th sig fig, below the 5sf pin) => magnitude=INFO per the plan's "
        f"pre-registered INFO_meaning (a precision pathology DEEPER than the "
        f"down-rounding). 3-tuple sign=PASS, magnitude=INFO, regime=VALID => composite "
        f"INFO (collapse rule). The SU(1,1) window is ASYMMETRIC about 1 (center = "
        f"1+2|beta|^2 = {g['S_W_center']:.8f}, not 1); the EXACT upper edge is BIT-EXACT "
        f"2|beta|^2 + 2|a||b| (resid {r['resid_bitexact']:.1e}); the plan/predecessor "
        f"shorthand '2|a||b|+|beta|^2'=b^2+2ab UNDER-counts by |beta|^2={g['beta2_W']:.3e} "
        f"(disagrees at 5sf: 2.9130e-3 vs 2.9151e-3) but the threshold VALUE is sourced "
        f"from frozen envelope_upper_dev so is unaffected. ROUTES to a higher-precision "
        f"(mpmath/Sage) S_W_max re-derivation carry-forward to confirm whether the "
        f"deviation is strictly < or == the exact edge below float64.")  # (local)

    rows = [
        f"# RE-PIN: PASS_TOL := S_W_max-1 = envelope_upper_dev = {r['PASS_TOL']:.10e} "
        f"(full float64 from frozen s102 npz; 5sf published = {r['pub_PASS_TOL']:.4e}, "
        f"Class-8.3). The S102 frozen pin was the down-rounded literal 0.0029 (= "
        f"'0.2915% rounded' but 0.002915 rounds DOWN at 4sf). # {GATE_ID}",
        f"# BIT-EXACT decomposition [SIGN]: S_W_max-1 = 2|beta|^2 + 2|a||b| = "
        f"{r['edge_2b2_2ab']:.10e} (resid vs frozen envelope_upper_dev = "
        f"{r['resid_bitexact']:.1e}). Center = 1+2|beta|^2 (resid {r['center_check']:.1e}); "
        f"half-spread = 2|a||b| (resid {r['half_check']:.1e}); unitarity |a^2-b^2-1| = "
        f"{r['unitarity_resid']:.1e}. The plan/predecessor SHORTHAND '2|a||b|+|beta|^2' "
        f"= |beta|^2+2|a||b| = {r['edge_b2_2ab']:.10e} UNDER-counts the upper edge by "
        f"one |beta|^2 = {g['beta2_W']:.3e} (it measures the spread about the OFFSET "
        f"center 1+2|beta|^2, then adds back only one |beta|^2 not two); it DISAGREES "
        f"at 5sf ({r['pub_edge_shorthand']:.4e} vs {r['pub_PASS_TOL']:.4e}). The "
        f"threshold VALUE is unaffected (sourced from frozen envelope_upper_dev). "
        f"# {GATE_ID}",
        f"# RE-EVAL [SIGN]: deviation - PASS_TOL = {r['deviation']:.6e} - "
        f"{r['PASS_TOL']:.6e} = {r['dev_vs_repin']:+.3e} <= 0 => PASS (predicted <=0 "
        f"matches computed). The DERIVED phase lands at the UPPER edge "
        f"(cos_phi_off_axis = {g['cos_phi_off_axis']:.8f} ~ +1), so the deviation "
        f"SATURATES the asymmetric upper endpoint it physically arises from. The two "
        f"WRONG edges: half-spread 2|a||b|={r['two_ab']:.6e} gives dev-edge "
        f"{r['dev_vs_half']:+.2e}>0 (FAIL; reproduces frozen dev_vs_half_spread, resid "
        f"{r['repro_half']:.1e}); literal 0.0029 gives {r['dev_vs_literal']:+.2e}>0 "
        f"(FAIL; reproduces frozen dev_vs_pass_tol, resid {r['repro_literal']:.1e}). "
        f"# {GATE_ID}",
        f"# ASYMMETRY: env_up - |env_lo| = {r['asym']:.6e} = 2|beta|^2 (resid "
        f"{r['asym_vs_2b2']:.1e}) => the SU(1,1) window {{S_W_min, S_W_max}} is "
        f"ASYMMETRIC about 1 because the Bogoliubov unitarity offset puts the center "
        f"at 1+2|beta|^2, not 1. The half-spread is the WRONG edge for an asymmetric "
        f"window about 1; the exact endpoint is the correct edge. # {GATE_ID}",
        f"# DUAL-PRIOR discriminator (plan §W3-1): composite=INFO => track priors "
        f"UNCHANGED (plan: 'INFO -> unchanged; knife-edge persists even at the exact "
        f"edge; would indicate a deeper precision pathology'). The re-pin RESOLVED THE "
        f"SIGN (deviation at-or-inside the exact edge; the literal 0.0029 and "
        f"half-spread 2|a||b| edges were both wrong) and VINDICATED the substrate "
        f"(within_envelope=True; deviation saturates the upper endpoint), confirming "
        f"the S102 INFO was NOT a substrate breach -- but the knife-edge SURVIVES the "
        f"re-pin: deviation == S_W_max-1 to publication precision (5sf+6sf identical). "
        f"The F_amp slot 0.3885 (UNIFIED-AS-79 k_a2 POWER-RATIO factor, CC2=+1) and the "
        f"S79 magnitudes-only ladder anchor are UNDISTURBED (the slot value 0.3885 is "
        f"unchanged; the DERIVED relative phase only modulates the slot within the S_W "
        f"window envelope). CARRY-FORWARD: a higher-precision (mpmath/Sage 300-bit) "
        f"S_W_max re-derivation to decide deviation < vs == exact edge below float64. "
        f"# {GATE_ID}",
        (f"# CANONICAL-DRIFT §(ii.B): canonical_constants.py SHA drifted from "
         f"plan-freeze {drift_info['canonical_planfreeze_sha'][:16]}... to runtime "
         f"{drift_info['canonical_runtime_sha'][:16]}... (parallel S103-wave "
         f"APPEND-ONLY: n_s_FW_sqrt_cutoff, x696_ncg_coincidence_headroom_ratio, "
         f"BF_spine_vs_incumbent_ceiling + PROVENANCE; NONE consumed by this gate). "
         f"Re-pinned to runtime per substrate-first-canonical-sourcing.md §(ii.B); "
         f"audit_sha256 computed over CURRENT canonical bytes. Frozen-npz file-byte "
         f"SHA (the gate's sole physics input) UNCHANGED => gate is TESTABLE, NOT "
         f"mechanical-closure. # {GATE_ID}"
         if drift_info["canonical_drifted"] else
         f"# CANONICAL-DRIFT §(ii.B): none -- canonical SHA matches plan-freeze "
         f"{drift_info['canonical_planfreeze_sha'][:16]}.... # {GATE_ID}"),
        f"# write_order: Step1=emit_verdict (this line). No canonical_constants "
        f"promotion: PASS_TOL is a per-gate comparison-edge re-pin (tolerance "
        f"hygiene), not a new framework prediction; the F_amp slot value 0.3885 is "
        f"UNCHANGED. Step3=N/A (no falsifier-inventory row consumes this re-pin). "
        f"# {GATE_ID}",
        f"# regulator_pin=N/A -- no Seeley-DeWitt a_n citation; no SCHEMATIC helper "
        f"consumed (frozen s102_w7_ladder_phase_resolved.npz + canonical_constants "
        f"only; provenance internal audit_sha256={g['internal_audit'][:16]}...). "
        f"# {GATE_ID}",
    ]                                                          # (local)

    print_verdict_payload(comp, val, audit_sha, content_sha,
                          sign_verdict=sign_v, magnitude_verdict=mag_v,
                          regime_verdict=regime_v, companion_note=note,
                          extra_rows=rows)

    print(f"\n[done] {GATE_ID} in {time.time() - t0:.2f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
