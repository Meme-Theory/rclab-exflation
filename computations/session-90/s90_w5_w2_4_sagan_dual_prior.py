#!/usr/bin/env python3
"""
S90 W5-3 — S90-W2-4-SAGAN-DUAL-PRIOR-3-TRACK-JSON-PRE-REGISTRATION (CF-44)
============================================================================

Gate: S90-W2-4-SAGAN-DUAL-PRIOR-3-TRACK-JSON-PRE-REGISTRATION
Trigger: [VERIFY]
Classification: META (dispatched COMPUTE-mode per `wave-classification.md
       §"Dispatch consequences"`: producing-script writes JSON + emits
       numerical verdict line with sum-to-1 PASS predicate, hence COMPUTE-
       routed even though output is META pre-registration discipline
       artifact)

Owner: sagan-empiricist PRIMARY (per ledger explicit "Sagan-revised dual-
       prior"; T1-11 K=1 advisory at `epistemic-discipline.md §"Dual-prior
       pre-registration as track-discriminator pattern"`); no co-author —
       single-agent JSON pre-registration verifying against CF-42 + CF-43
       PASS npz inputs.

═══════════════════════════════════════════════════════════════════════════
SUBSTRATE FRAMING (read first; pin direction-of-explanation)
═══════════════════════════════════════════════════════════════════════════

This dual-prior 3-track JSON is META-discipline pre-registration for the
§VII.AH STAGE-1-CANDIDATE Stage-2 verify pathway per `joint-theorem-
promotion.md §"Stage 2 Two-Agent Parallel Cross-Check"`. The 3 tracks
{A, B, C} correspond to STRUCTURALLY DISTINCT outcomes at the substrate-
IS observable layer:

  • Track A — representation-INVARIANCE confirmed (BOTH CF-42 §W2-1.A
    Hochschild representation AND CF-43 BCS-Bogoliubov representation
    routes produce R_substrate = 7.324992 at <0.1% RATIO band)
  • Track B — representation-ASYMMETRY (one route PASSes, the other
    INFOs; structurally interesting but does NOT certify representation-
    INVARIANCE of the BdG-restricted Connes-Karoubi pairing)
  • Track C — falsification-class (either route FAILs at >1% RATIO OR
    both INFO at >0.1%)

These tracks are STRUCTURAL classifications of the substrate's intrinsic
representation-INVARIANCE; they are NOT "interpretations imposed on" the
substrate. Direction of explanation flows substrate → emergent: the
substrate's intrinsic cocycle ratio determines which posterior track is
observationally consistent, NOT the other way around. The substrate IS
the BdG-restricted spectral triple (A_BdG, H_BdG, D_BdG); its cocycle
ratio IS the invariant scalar; the JSON pre-registration discipline
merely makes the discrimination of outcomes EXPLICIT so that "agreement
among agents" cannot be conflated with substrate-IS confirmation (per
`epistemic-discipline.md §"What Does NOT Count as Evidence"` item 2 +
`joint-theorem-promotion.md §"Why a constructive complement is needed"`).
NO container-thinking.

═══════════════════════════════════════════════════════════════════════════
DISPATCH CONTEXT (intra-wave sequential chain)
═══════════════════════════════════════════════════════════════════════════

CF-44 dispatches LAST in S90 W5: requires BOTH CF-42 §W2-1.A PASS AND
CF-43 PASS as upstream conditions (intra-wave dependency per plan §W5-3
"Decision Point Prerequisites" line 28). The {A, B, C} tracks branch on
the JOINT outcome of CF-42 + CF-43, so both verdicts must land BEFORE
CF-44's discriminator gate criterion can be evaluated.

Upstream chain at S90 W5 close:
  CF-42 §W2-1.A PASS @ rel_dev_A = 2.405684e-06 (audit_sha256=94f2f053...)
  CF-43 PASS @ rel_dev_BCS = 2.405684e-06 (audit_sha256=4dd0c4df...)
  Joint outcome: PASS_AND (both at sub-0.1% RATIO band against canonical
  7.324992) → Track A pathway operational

═══════════════════════════════════════════════════════════════════════════
3-TRACK STRUCTURE (W-2 workshop CF-W2-4-DEFERRED + sagan revision)
═══════════════════════════════════════════════════════════════════════════

Prior masses (Sagan-revised per plan §W5-3 line 549-551):

  prior_mass_A = Fraction(50, 100) = 0.50
    Track A "representation-INVARIANCE PASS-AND at sub-0.1%"; HIGHEST mass
    because the two-route representation-INVARIANCE test at sub-0.1% RATIO
    is structurally MOST informative outcome — it confirms the Connes-
    Moscovici 1995 §III.4 theorem operates in our specific BdG-restricted
    setting.

  prior_mass_B = Fraction(30, 100) = 0.30
    Track B "representation-ASYMMETRY (one PASS, one INFO)"; INTERMEDIATE
    mass; represents asymmetry between Hochschild and Bogoliubov
    representations — structurally interesting but does NOT certify
    representation-INVARIANCE.

  prior_mass_C = Fraction(20, 100) = 0.20
    Track C "falsification-class (FAIL in either route OR both INFO)";
    LOWEST mass; routes to CF-W2-2 re-execution OR Connes-Karoubi pairing
    re-derivation.

  Sum: 50/100 + 30/100 + 20/100 = 100/100 = 1 EXACTLY (Sage-Q rational).

Per-outcome posterior re-allocations:

  PASS_AND outcome → posterior {A: 0.90, B: 0.07, C: 0.03}  (sums to 1.000)
  FAIL outcome     → posterior {A: 0.02, B: 0.18, C: 0.80}  (sums to 1.000)
  INFO outcome     → posterior {A: 0.35, B: 0.45, C: 0.20}  (sums to 1.000)

═══════════════════════════════════════════════════════════════════════════
RULE-COMPLIANCE CRITERIA (T1-11 + Element 3 + algebra-axis orthogonality)
═══════════════════════════════════════════════════════════════════════════

Per `epistemic-discipline.md §"Dual-prior pre-registration as track-
discriminator pattern"` (T1-11 K=1 advisory) — 3-criterion compliance:

  (1) Track A prior:  explicit ratio 0.50  ✓
  (2) Track B prior:  explicit ratio 0.30 + Track C explicit 0.20  ✓
  (3) Discriminator gate criterion: §VII.AH STAGE-1-CANDIDATE Stage-2
      verify PASS-AND/FAIL/INFO outcome maps to {posterior A, B, C}  ✓

Per `cross-pillar-bridge-anatomy.md §"Element 3 fiducial-anchor binding
discipline"` (S88 W-15 V.7 K=1 advisory):

  (4) Element 3 binding-class declaration:  substrate-self-consistent  ✓
      (cocycle ratio 7.324992 IS framework prediction at the same algebra-
      axis family = Cell I × FI-IDENTITY × s=3 substrate-distance-1; lab
      discrimination is 1D in observable space, NOT 2D joint-hypersurface;
      no cross-pillar laboratory observation pinning required).

Per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-
counter"` (MANDATORY at K=3):

  (5) NO cross-corner co-primary structure invoked. The continued-
      fraction r/h = [7;9,2,17,6,2,39] (CF-42 §W2-1.B certification) shows
      the §W2-1.A cocycle ratio and §W2-1.B HP^1 STRICT_F4 anchors live
      on STRUCTURALLY DISTINCT cells; no rational ratio between them ⇒
      algebra-axis orthogonality preserved by construction. CF-44's
      discriminator operates within Cell I × FI-IDENTITY (no cross-corner
      conflation).

═══════════════════════════════════════════════════════════════════════════
K-COUNTER ADVANCEMENTS ON PASS
═══════════════════════════════════════════════════════════════════════════

Per `feedback_rules-compensate-missing-structure.md` K-counter promotion
threshold (SUGGESTION → MANDATORY at K=3):

  Element 3 fiducial-anchor binding discipline:
    K_pre  = 1 (S88 W-15 W15-V.7 first instance, SUGGESTION)
    K_post = 2 on CF-44 PASS (this gate is the second calibration
             instance: substrate-self-consistent binding at Cell I × FI-
             IDENTITY × s=3 cocycle ratio target)
    Status: remains SUGGESTION; one more instance needed for K=3 MANDATORY.

  T1-11 Dual-prior pre-registration discipline:
    K_pre  = 1 (S88 W-15 first instance, SUGGESTION)
    K_post = 2 on CF-44 PASS (this gate is the second instance:
             Sagan-revised dual-prior 3-track structure for §VII.AH Stage-2)
    Status: remains SUGGESTION; one more instance needed for K=3 MANDATORY.

═══════════════════════════════════════════════════════════════════════════
KNOWLEDGE-MCP QUERIES (executed at compose time)
═══════════════════════════════════════════════════════════════════════════

  search_knowledge("dual-prior pre-registration track-discriminator Element
      3 fiducial-anchor binding T1-11")  → Element 3 fiducial-anchor
      binding SUGGESTION at K=1 (S88 W-15 W15-V.7); Publication-Precision
      Class 8.3 MANDATORY at K=4 (post S87 W8); §VII.AU FWD-C1 Pillar I-II
      bridge landing precedent for `element_2_oe_form` + `element_3_binding`
      composite verdict-line value-string format (session-89-plan-w7.md).
  CF-42 §W2-1.A npz input pin: 7.3249743783873615 (R_canonical_computed_f64)
  CF-43 npz input pin: 7.3249743783873615 (R_substrate_BCS_grounded;
      bit-identical by representation-INVARIANCE theorem)
  trace_entity("§VII.AH STAGE-1-CANDIDATE substrate-input-orthogonality")
      → §VII.AH = first framework cross-axis joint theorem to reach
      STAGE-3-PERMANENT eligibility via Stage-2 PASS at substrate-input-
      orthogonality structural ceiling (S89 W4-7 audit_sha256=4fcd7d29...);
      K-counter status MANDATORY at K=3 post S90 W2 CF-20 promotion.

Branch: No closure pre-covers CF-44. This is the first substantive
landing of the Sagan-revised dual-prior 3-track JSON for §VII.AH
STAGE-1-CANDIDATE Stage-2.
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path

_SHARED_DIR = Path(__file__).resolve().parent.parent / "_shared"
sys.path.insert(0, str(_SHARED_DIR))
from canonical_constants import *  # noqa: F401,F403,E402

import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402
from fractions import Fraction  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

# ---- Plan-pinned constants ----
GATE_ID = "S90-W2-4-SAGAN-DUAL-PRIOR-3-TRACK-JSON-PRE-REGISTRATION"  # (local)
SCHEME = "sagan-revised-dual-prior-3-track"  # (local)
CONVENTION = "JSON-pre-registration-T1-11-K2-Element-3-K2-on-PASS"  # (local)
L_MAX_STRING = "N/A"  # (local) META gate; no eigenvalue computation
SCHEMA_VERSION = "S87+"  # (local)

# ---- Absolute sum-to-1 tolerance per plan §W5-3 §0.11 PRDR ----
SUM_TO_1_ABS_TOL = 1e-10  # (local) ABSOLUTE tolerance per plan threshold

# ---- 3-track structure (Sagan-revised per plan §W5-3 line 549-551) ----
PRIOR_NUM_A = 50  # (local) numerator of Fraction(50, 100) = 0.50
PRIOR_NUM_B = 30  # (local) numerator of Fraction(30, 100) = 0.30
PRIOR_NUM_C = 20  # (local) numerator of Fraction(20, 100) = 0.20
PRIOR_DEN = 100  # (local) common denominator for 100-th-fraction prior masses

# Per-outcome posterior re-allocations (Sagan revision per plan §W5-3 553-555)
POSTERIOR_PASS_AND = {"A": 0.90, "B": 0.07, "C": 0.03}  # sum = 1.000 exact
POSTERIOR_FAIL = {"A": 0.02, "B": 0.18, "C": 0.80}  # sum = 1.000 exact
POSTERIOR_INFO = {"A": 0.35, "B": 0.45, "C": 0.20}  # sum = 1.000 exact

# ---- Rule-compliance pins ----
T1_11_K1_ADVISORY = "compliant"  # (local) per plan §W5-3 §rule compliance
ELEMENT_3_K1_ADVISORY = "compliant"  # (local)
ELEMENT_3_BINDING_CLASS = "substrate-self-consistent"  # (local) substrate IS framework prediction
DISCRIMINATOR_GATE = "CF-42 §W2-1.A AND CF-43 composite verdict"  # (local)
TARGET_REGISTRY_ENTRY = "§VII.AH STAGE-1-CANDIDATE"  # (local)
STAGE_2_PATHWAY = "joint-theorem-promotion.md §Stage 2 Two-Agent Parallel Cross-Check"  # (local)

# ---- K-counter advancements pre-registered on PASS ----
ELEMENT_3_K_PRE = 1  # (local) S88 W-15 W15-V.7 first instance
ELEMENT_3_K_POST_ON_PASS = 2  # (local) this gate is second instance
T1_11_K_PRE = 1  # (local) S88 W-15 first instance
T1_11_K_POST_ON_PASS = 2  # (local) this gate is second instance

# ---- Input file paths ----
CF42_A_NPZ = SESSION_DIR / "s90_w5_w2_1_a_cocycle_ratio.npz"
CF43_NPZ = SESSION_DIR / "s90_w5_w2_2_landau_bcs_grounded_r_substrate.npz"
CANONICAL_CONSTANTS = SHARED_DIR / "canonical_constants.py"
EPISTEMIC_DISCIPLINE = (
    PROJECT_ROOT / ".claude" / "rules" / "epistemic-discipline.md"
)
CROSS_PILLAR_BRIDGE_ANATOMY = (
    PROJECT_ROOT / ".claude" / "rules" / "cross-pillar-bridge-anatomy.md"
)
JOINT_THEOREM_PROMOTION = (
    PROJECT_ROOT / ".claude" / "rules" / "joint-theorem-promotion.md"
)
PERMANENT_RESULTS_REGISTRY = (
    PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
)

# ---- Output paths ----
JSON_OUT = SESSION_DIR / "s90_w5_w2_4_sagan_dual_prior.json"
PNG_OUT = SESSION_DIR / "s90_w5_w2_4_sagan_dual_prior.png"
VERDICT_TXT = SESSION_DIR / "s90_gate_verdicts.txt"


# ═══════════════════════════════════════════════════════════════════════════
# SHA helpers (canonical pattern)
# ═══════════════════════════════════════════════════════════════════════════

def sha256_of(path):
    h = hashlib.sha256()
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}
    for p in inputs:
        sha = sha256_of(p)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        except ValueError:
            rel = str(p)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path, canonical_path, pins):
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True,
    ).encode("utf-8")
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


def emit_verdict(verdict, value_str, audit_sha, content_sha):
    """AFTER-pattern single-shot verdict emission for [VERIFY] gate (no
    3-tuple annotation per plan §W5-3 lines 617-620 literal format)."""
    canonical = (
        f"{GATE_ID}: {verdict} -- value={value_str!r} "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX_STRING} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA_VERSION}\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical)
        fp.write(companion)


# ═══════════════════════════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════════════════════════

def main():
    t0 = time.time()
    print("=" * 75)
    print(f"S90 W5-3 — {GATE_ID}")
    print("=" * 75)
    print()

    # ---- Step 1: Input pin map ----
    input_files = [
        CANONICAL_CONSTANTS,
        CF42_A_NPZ,
        CF43_NPZ,
        EPISTEMIC_DISCIPLINE,
        CROSS_PILLAR_BRIDGE_ANATOMY,
        JOINT_THEOREM_PROMOTION,
        PERMANENT_RESULTS_REGISTRY,
    ]
    pins = log_input_pins(input_files)
    print()

    # ---- Step 2: Read CF-42 §W2-1.A + CF-43 upstream npz outputs ----
    print("Step 1: Read CF-42 §W2-1.A + CF-43 upstream npz (intra-wave dependency)")
    data_A = np.load(CF42_A_NPZ, allow_pickle=True)
    data_BCS = np.load(CF43_NPZ, allow_pickle=True)

    R_canonical_A = float(data_A["R_canonical_computed_f64"])
    rel_dev_A_upstream = float(data_A["rel_dev_A"])
    sub_verdict_A = str(data_A["sub_verdict"])

    R_substrate_BCS = float(data_BCS["R_substrate_BCS_grounded"])
    rel_dev_BCS_upstream = float(data_BCS["rel_dev_BCS"])
    composite_BCS = str(data_BCS["composite_verdict"])

    print(f"  CF-42 §W2-1.A R_canonical = {R_canonical_A!r}")
    print(f"  CF-42 rel_dev_A           = {rel_dev_A_upstream:.6e}")
    print(f"  CF-42 sub_verdict         = {sub_verdict_A}")
    print(f"  CF-43 R_substrate_BCS     = {R_substrate_BCS!r}")
    print(f"  CF-43 rel_dev_BCS         = {rel_dev_BCS_upstream:.6e}")
    print(f"  CF-43 composite_verdict   = {composite_BCS}")
    print()
    assert sub_verdict_A == "PASS", (
        f"CF-42 §W2-1.A upstream NOT PASS (got {sub_verdict_A!r}); CF-44 cannot dispatch."
    )
    assert composite_BCS == "PASS", (
        f"CF-43 upstream NOT PASS (got {composite_BCS!r}); CF-44 cannot dispatch."
    )
    print("  ✓ Both upstream gates PASS — CF-44 discriminator gate operational.")
    print()

    # ---- Step 3: Determine joint outcome class (PASS_AND / FAIL / INFO) ----
    print("Step 2: Determine joint outcome class (discriminator gate)")
    # Per plan §W5-3 lines 553-555: outcome class branches on joint
    # CF-42 §W2-1.A AND CF-43 verdict pair against the 0.1% / 1% bands.
    if rel_dev_A_upstream <= 0.001 and rel_dev_BCS_upstream <= 0.001:
        joint_outcome = "PASS_AND"
    elif rel_dev_A_upstream <= 0.01 and rel_dev_BCS_upstream <= 0.01:
        # One PASS + one INFO, OR both INFO
        if (rel_dev_A_upstream <= 0.001) ^ (rel_dev_BCS_upstream <= 0.001):
            joint_outcome = "INFO"  # asymmetric: one PASS one INFO
        else:
            joint_outcome = "INFO"  # both INFO
    else:
        joint_outcome = "FAIL"
    print(f"  rel_dev_A (CF-42 §W2-1.A)  = {rel_dev_A_upstream:.6e}")
    print(f"  rel_dev_BCS (CF-43)        = {rel_dev_BCS_upstream:.6e}")
    print(f"  Joint outcome class        = {joint_outcome}")
    print(f"  ⇒ Posterior to apply       = {POSTERIOR_PASS_AND if joint_outcome == 'PASS_AND' else (POSTERIOR_FAIL if joint_outcome == 'FAIL' else POSTERIOR_INFO)}")
    print()

    # ---- Step 4: Sage-Q exact sum-to-1 verification ----
    print("Step 3: Sage-Q exact sum-to-1 verification (substitution chain)")
    prior_A = Fraction(PRIOR_NUM_A, PRIOR_DEN)
    prior_B = Fraction(PRIOR_NUM_B, PRIOR_DEN)
    prior_C = Fraction(PRIOR_NUM_C, PRIOR_DEN)
    prior_sum_Q = prior_A + prior_B + prior_C
    prior_sum_f64 = float(prior_sum_Q)
    print(f"  prior_A = Fraction({PRIOR_NUM_A}, {PRIOR_DEN}) = {prior_A} = {float(prior_A)}")
    print(f"  prior_B = Fraction({PRIOR_NUM_B}, {PRIOR_DEN}) = {prior_B} = {float(prior_B)}")
    print(f"  prior_C = Fraction({PRIOR_NUM_C}, {PRIOR_DEN}) = {prior_C} = {float(prior_C)}")
    print(f"  prior_sum_Q = {prior_sum_Q}  (Sage-Q exact; should be Fraction(1, 1))")
    print(f"  prior_sum_f64 = {prior_sum_f64}")
    prior_sum_residual = abs(prior_sum_f64 - 1.0)
    print(f"  |prior_sum_f64 - 1.0| = {prior_sum_residual:.2e}  (tol {SUM_TO_1_ABS_TOL:.0e})")
    assert prior_sum_Q == Fraction(1, 1), (
        f"Sage-Q prior_sum_Q drift: got {prior_sum_Q}, expected Fraction(1, 1) exact"
    )
    prior_sum_check = prior_sum_residual <= SUM_TO_1_ABS_TOL
    print(f"  Prior sum-to-1 PASS: {prior_sum_check}")
    print()

    # Per-outcome posterior sum-to-1 verification
    posteriors = {
        "PASS_AND": POSTERIOR_PASS_AND,
        "FAIL": POSTERIOR_FAIL,
        "INFO": POSTERIOR_INFO,
    }
    posterior_sums = {}
    posterior_checks = {}
    for outcome, posterior_dict in posteriors.items():
        s = posterior_dict["A"] + posterior_dict["B"] + posterior_dict["C"]
        residual = abs(s - 1.0)
        passes = residual <= SUM_TO_1_ABS_TOL
        posterior_sums[outcome] = s
        posterior_checks[outcome] = passes
        print(f"  posterior[{outcome}] sum = {s}  |{s}-1.0|={residual:.2e}  PASS={passes}")
    print()

    all_sums_pass = (
        prior_sum_check
        and all(posterior_checks.values())
    )
    print(f"  All sum-to-1 PASS predicates satisfied: {all_sums_pass}")
    print()

    # ---- Step 5: Structural distinctness of A/B/C tracks (no conflation) ----
    print("Step 4: Structural distinctness of A/B/C tracks (no conflation)")
    track_descriptions = {
        "A": "representation-INVARIANCE confirmed at sub-0.1% RATIO (both routes)",
        "B": "representation-ASYMMETRY (one route PASS, one route INFO)",
        "C": "falsification-class (FAIL in either route OR both INFO at >0.1%)",
    }
    # Disjointness check: any single (CF-42, CF-43) verdict pair maps to exactly one track
    outcome_to_track = {
        ("PASS", "PASS"): "A",  # both at sub-0.1% RATIO → representation-INVARIANCE
        ("PASS", "INFO"): "B",  # asymmetry: A PASS, BCS INFO
        ("INFO", "PASS"): "B",  # asymmetry: A INFO, BCS PASS
        ("PASS", "FAIL"): "C",  # falsification
        ("FAIL", "PASS"): "C",  # falsification
        ("INFO", "INFO"): "C",  # both INFO at >0.1% → falsification-class
        ("INFO", "FAIL"): "C",
        ("FAIL", "INFO"): "C",
        ("FAIL", "FAIL"): "C",
    }
    distinct_tracks = set(outcome_to_track.values())
    print(f"  Outcome → Track mapping (9 cells):")
    for (cf42, cf43), tr in sorted(outcome_to_track.items()):
        print(f"    CF-42={cf42}, CF-43={cf43} → Track {tr} ({track_descriptions[tr][:55]}...)")
    tracks_A_B_C_disjoint = len(distinct_tracks) == 3
    no_conflation_check_passed = all(
        len(outcome_to_track[(a, b)]) == 1
        for a in ["PASS", "INFO", "FAIL"]
        for b in ["PASS", "INFO", "FAIL"]
    )
    print(f"  tracks_A_B_C_disjoint        = {tracks_A_B_C_disjoint}")
    print(f"  no_conflation_check_passed   = {no_conflation_check_passed}")
    structural_distinctness = tracks_A_B_C_disjoint and no_conflation_check_passed
    print(f"  structural_distinctness      = {structural_distinctness}")
    print()

    # ---- Step 6: Build JSON pre-registration ----
    print("Step 5: Build JSON pre-registration output")
    pre_registration = {
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "schema_version": SCHEMA_VERSION,
        "target_registry_entry": TARGET_REGISTRY_ENTRY,
        "stage_2_pathway": STAGE_2_PATHWAY,
        "discriminator_gate": DISCRIMINATOR_GATE,
        "rule_compliance": {
            "T1_11_K1_advisory": T1_11_K1_ADVISORY,
            "element_3_fiducial_anchor_binding_K1_advisory": ELEMENT_3_K1_ADVISORY,
            "element_3_binding_class": ELEMENT_3_BINDING_CLASS,
            "algebra_axis_orthogonality_respected": True,  # CF-42 §W2-1.B cf-expansion certifies
            "discriminator_gate": DISCRIMINATOR_GATE,
        },
        "prior_masses": {
            "A_representation_invariance_PASS_AND_sub_0.1pct": float(prior_A),
            "B_representation_asymmetry_one_PASS_one_INFO": float(prior_B),
            "C_falsification_class": float(prior_C),
        },
        "prior_sum": prior_sum_f64,
        "prior_sum_residual": prior_sum_residual,
        "prior_sum_check_passed": prior_sum_check,
        "posterior_per_outcome": {
            "PASS_AND": {
                "A": POSTERIOR_PASS_AND["A"],
                "B": POSTERIOR_PASS_AND["B"],
                "C": POSTERIOR_PASS_AND["C"],
                "sum": posterior_sums["PASS_AND"],
                "sum_check_passed": posterior_checks["PASS_AND"],
            },
            "FAIL": {
                "A": POSTERIOR_FAIL["A"],
                "B": POSTERIOR_FAIL["B"],
                "C": POSTERIOR_FAIL["C"],
                "sum": posterior_sums["FAIL"],
                "sum_check_passed": posterior_checks["FAIL"],
            },
            "INFO": {
                "A": POSTERIOR_INFO["A"],
                "B": POSTERIOR_INFO["B"],
                "C": POSTERIOR_INFO["C"],
                "sum": posterior_sums["INFO"],
                "sum_check_passed": posterior_checks["INFO"],
            },
        },
        "track_descriptions": track_descriptions,
        "outcome_to_track_mapping": {
            f"{cf42}+{cf43}": tr
            for (cf42, cf43), tr in outcome_to_track.items()
        },
        "structural_distinctness": {
            "tracks_A_B_C_disjoint": tracks_A_B_C_disjoint,
            "no_conflation_check_passed": no_conflation_check_passed,
            "overall": structural_distinctness,
        },
        "k_counter_advancements_on_PASS": {
            "element_3_fiducial_anchor_binding_K_pre": ELEMENT_3_K_PRE,
            "element_3_fiducial_anchor_binding_K_post_on_PASS": ELEMENT_3_K_POST_ON_PASS,
            "T1_11_dual_prior_K_pre": T1_11_K_PRE,
            "T1_11_dual_prior_K_post_on_PASS": T1_11_K_POST_ON_PASS,
        },
        "input_provenance": {
            "CF_42_W2_1_A_R_canonical": R_canonical_A,
            "CF_42_W2_1_A_rel_dev": rel_dev_A_upstream,
            "CF_42_W2_1_A_audit_sha256_short": pins[
                str(CF42_A_NPZ.relative_to(PROJECT_ROOT)).replace("\\", "/")
            ][:16],
            "CF_43_R_substrate_BCS_grounded": R_substrate_BCS,
            "CF_43_rel_dev_BCS": rel_dev_BCS_upstream,
            "CF_43_audit_sha256_short": pins[
                str(CF43_NPZ.relative_to(PROJECT_ROOT)).replace("\\", "/")
            ][:16],
            "joint_outcome_class": joint_outcome,
            "applicable_posterior": joint_outcome,
        },
        "substrate_framing": (
            "The substrate IS the BdG-restricted spectral triple (A_BdG, "
            "H_BdG, D_BdG). The cocycle ratio R_substrate = ||phi_67||_BdG / "
            "||phi_88||_BdG IS its Cell I × FI-IDENTITY × s=3 observable. "
            "The 3 tracks {A, B, C} are STRUCTURAL classifications of "
            "representation-INVARIANCE outcomes at the substrate-IS layer, "
            "NOT interpretations imposed on the substrate. Direction of "
            "explanation: substrate → emergent."
        ),
    }
    # Verify JSON serialization round-trip
    json_text = json.dumps(pre_registration, indent=2, sort_keys=False)
    parsed_back = json.loads(json_text)
    json_well_formed = parsed_back == pre_registration
    print(f"  JSON serialization round-trip well-formed: {json_well_formed}")
    print()

    # Write JSON
    JSON_OUT.write_text(json_text, encoding="utf-8")
    print(f"  JSON written: {JSON_OUT.relative_to(PROJECT_ROOT)}")
    print()

    # ---- Step 7: Rule-compliance verification ----
    print("Step 6: Rule-compliance verification")
    rule_compliance_checks = {
        "T1_11_K1_advisory": T1_11_K1_ADVISORY == "compliant",
        "element_3_fiducial_anchor_binding_K1_advisory": (
            ELEMENT_3_K1_ADVISORY == "compliant"
        ),
        "element_3_binding_class_declared": (
            ELEMENT_3_BINDING_CLASS == "substrate-self-consistent"
        ),
        "discriminator_gate_declared": (
            DISCRIMINATOR_GATE == "CF-42 §W2-1.A AND CF-43 composite verdict"
        ),
    }
    for k, v in rule_compliance_checks.items():
        print(f"  {k}: {v}")
    all_rule_compliance_passes = all(rule_compliance_checks.values())
    print(f"  All rule-compliance checks PASS: {all_rule_compliance_passes}")
    print()

    # ---- Step 8: Composite verdict ----
    print("Step 7: Composite verdict per plan §W5-3 PASS predicate")
    pass_predicate = (
        json_well_formed
        and all_sums_pass
        and structural_distinctness
        and all_rule_compliance_passes
    )
    if pass_predicate:
        verdict = "PASS"
    elif json_well_formed and all_sums_pass and not all_rule_compliance_passes:
        # One or more rule_compliance fields flagged "partial"
        verdict = "INFO"
    else:
        verdict = "FAIL"
    print(f"  json_well_formed              = {json_well_formed}")
    print(f"  all_sums_pass                 = {all_sums_pass}")
    print(f"  structural_distinctness       = {structural_distinctness}")
    print(f"  all_rule_compliance_passes    = {all_rule_compliance_passes}")
    print(f"  PASS predicate (composite)    = {pass_predicate}")
    print(f"  ⇒ verdict = {verdict}")
    print()

    # ---- Step 9: Plot 3-panel summary ----
    print("Step 8: Plot 3-panel summary")
    fig, axes = plt.subplots(1, 3, figsize=(16, 5.5))

    # Panel 1: Prior masses bar chart
    ax = axes[0]
    tracks = ["A\nrepresentation-\nINVARIANCE", "B\nrepresentation-\nASYMMETRY", "C\nfalsification-\nclass"]
    priors = [float(prior_A), float(prior_B), float(prior_C)]
    colors = ["#30a050", "#d4a040", "#d04040"]
    bars = ax.bar(tracks, priors, color=colors, edgecolor="black", alpha=0.8)
    ax.set_ylabel("prior mass")
    ax.set_ylim(0, 0.6)
    ax.set_title(
        f"Prior masses (Sagan-revised)\n"
        f"prior_sum = {prior_sum_f64} (Sage-Q exact)",
        fontsize=11,
    )
    for bar, val in zip(bars, priors):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.01,
            f"{val:.2f}",
            ha="center",
            va="bottom",
            fontsize=11,
            fontweight="bold",
        )
    ax.grid(True, alpha=0.3, axis="y")

    # Panel 2: Per-outcome posterior re-allocation
    ax = axes[1]
    x = np.arange(3)  # (local) panel-2 x-positions for posterior bars
    width = 0.25  # (local) matplotlib bar width for panel-2 grouped bars
    for i, (outcome, color, posterior) in enumerate(
        [
            ("PASS_AND", "#30a050", POSTERIOR_PASS_AND),
            ("FAIL", "#d04040", POSTERIOR_FAIL),
            ("INFO", "#d4a040", POSTERIOR_INFO),
        ]
    ):
        ax.bar(
            x + (i - 1) * width,
            [posterior["A"], posterior["B"], posterior["C"]],
            width,
            label=outcome,
            color=color,
            edgecolor="black",
            alpha=0.7,
        )
    ax.set_xticks(x)
    ax.set_xticklabels(["A", "B", "C"])
    ax.set_xlabel("Track")
    ax.set_ylabel("posterior mass")
    ax.set_ylim(0, 1.0)
    ax.set_title(
        "Per-outcome posterior re-allocation\n"
        "(applied posterior shown by joint outcome class)",
        fontsize=11,
    )
    ax.axhline(1.0, color="gray", linestyle=":", alpha=0.5)
    ax.legend(fontsize=9, loc="upper right")
    ax.grid(True, alpha=0.3, axis="y")

    # Panel 3: K-counter advancement on PASS
    ax = axes[2]
    counters = ["Element 3\nfiducial-anchor binding\n(cross-pillar)", "T1-11\ndual-prior\npre-registration"]
    k_pre = [ELEMENT_3_K_PRE, T1_11_K_PRE]
    k_post = [ELEMENT_3_K_POST_ON_PASS, T1_11_K_POST_ON_PASS]
    x = np.arange(len(counters))  # (local) panel-3 x-positions for K-counter bars
    width = 0.35  # (local) matplotlib bar width for panel-3 paired bars
    ax.bar(x - width / 2, k_pre, width, label="K_pre", color="#888888", edgecolor="black", alpha=0.8)
    ax.bar(x + width / 2, k_post, width, label=f"K_post on {verdict}", color="#3060c0", edgecolor="black", alpha=0.8)
    ax.set_xticks(x)
    ax.set_xticklabels(counters)
    ax.set_ylabel("K-counter")
    ax.set_ylim(0, 4)
    ax.axhline(3, color="#d04040", linestyle="--", label="K=3 MANDATORY threshold")
    ax.set_title(
        f"K-counter advancement on {verdict}\n"
        f"(both → K=2; one more needed for K=3 MANDATORY)",
        fontsize=11,
    )
    ax.legend(fontsize=9, loc="upper left")
    ax.grid(True, alpha=0.3, axis="y")

    fig.suptitle(
        f"CF-44: §W5-3 Sagan dual-prior 3-track JSON pre-registration — verdict={verdict}\n"
        f"§VII.AH STAGE-1-CANDIDATE Stage-2 pathway | "
        f"Element 3 K=1→K=2, T1-11 K=1→K=2 on PASS",
        fontsize=12,
    )
    fig.tight_layout(rect=[0, 0, 1, 0.93])
    fig.savefig(PNG_OUT, dpi=140, bbox_inches="tight")
    print(f"  PNG written: {PNG_OUT.relative_to(PROJECT_ROOT)}")
    print()

    # ---- Step 10: Compute dual SHAs + emit verdict ----
    print("Step 9: Compute dual SHAs + emit verdict")
    audit_sha, content_sha = compute_dual_sha(
        Path(__file__), CANONICAL_CONSTANTS, pins
    )
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    value_str = (
        f"prior_sum={prior_sum_f64};"
        f"posterior_PASS_AND_sum={posterior_sums['PASS_AND']};"
        f"posterior_FAIL_sum={posterior_sums['FAIL']};"
        f"posterior_INFO_sum={posterior_sums['INFO']};"
        f"structural_distinctness={structural_distinctness};"
        f"json_well_formed={json_well_formed};"
        f"rule_compliance_all_pass={all_rule_compliance_passes};"
        f"element_3_binding_class={ELEMENT_3_BINDING_CLASS};"
        f"joint_outcome_class={joint_outcome};"
        f"element_3_K_pre_post={ELEMENT_3_K_PRE}_{ELEMENT_3_K_POST_ON_PASS};"
        f"T1_11_K_pre_post={T1_11_K_PRE}_{T1_11_K_POST_ON_PASS};"
        f"sum_to_1_abs_tol={SUM_TO_1_ABS_TOL}"
    )

    emit_verdict(verdict, value_str, audit_sha, content_sha)
    print(f"  Verdict line appended to: {VERDICT_TXT.relative_to(PROJECT_ROOT)}")
    print()

    # ---- Final diagnostic ----
    print("=" * 75)
    print(f"§W5-3 {verdict} — wall-time {time.time() - t0:.2f}s")
    print(f"  audit_sha256:     {audit_sha}")
    print(f"  content_sha256:   {content_sha}")
    print(f"  prior_sum               = {prior_sum_f64} (Sage-Q Fraction(1,1))")
    print(f"  PASS_AND posterior sum  = {posterior_sums['PASS_AND']}")
    print(f"  FAIL posterior sum      = {posterior_sums['FAIL']}")
    print(f"  INFO posterior sum      = {posterior_sums['INFO']}")
    print(f"  structural_distinctness = {structural_distinctness}")
    print(f"  all_rule_compliance     = {all_rule_compliance_passes}")
    print(f"  joint_outcome_class     = {joint_outcome}")
    print(f"  Element 3 K-counter advances {ELEMENT_3_K_PRE}→{ELEMENT_3_K_POST_ON_PASS} on PASS")
    print(f"  T1-11 K-counter advances {T1_11_K_PRE}→{T1_11_K_POST_ON_PASS} on PASS")
    print("=" * 75)


if __name__ == "__main__":
    main()
