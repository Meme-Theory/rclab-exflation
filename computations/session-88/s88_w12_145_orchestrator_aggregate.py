"""
S88 W12-145 Orchestrator Aggregator — Reading_1 Closed
========================================================

PASS-AND on Reading_1 (generic-pluralism reading) for the W-9 spectral
↔ dynamical anti-correlation pole-scope structural correlation.

Axis-A connes: FAIL-Reading_1 (4 sub-clauses all FAIL)
  1. pole_scope_subclause: FAIL — Reading_1 violates Pole-Scope MANDATORY
  2. algebra_axis_orthogonality: FAIL — Reading_1 violates "cross-pole
     co-primary FORBIDDEN" (MANDATORY at K=3)
  3. cross_regulator_spread: FAIL — empirical 0.8946 > pre-reg 0.30 (2.98×)
  4. structural_anchor_independence: FAIL — 4-class projection
     ρ_S(s=4) = -1.0 is tautology of script's anchor construction

Axis-B volovik: FAIL-Reading_1 (cross_regulator_spread = 0.894591 ≫
  pre-reg 0.30; PLUS three transit-side structural defects: dynamical-
  axis-frozen artifact, s=4 anchor-formula non-existence, atlas
  regulator-class dependence)

PASS-AND on Reading_1: BOTH axes FAIL → joint Reading_1 FAIL.
Reading_2 (pole-specific to s=3) is the structurally supported reading
in BOTH cross-reviewer verdicts; promote Reading_2 as canonical.

Composite: FAIL on Reading_1 generic-pluralism; INFO on Reading_2
pole-specific reading is canonical (NOT a top-level FAIL — the gate's
purpose was to discriminate readings; both axes reach the same
discrimination → Reading_2 canonical).

Per gate-verdicts.md composite-collapse: the literal verdict is
"PASS-Reading_2 / FAIL-Reading_1" — under the discrimination-gate
semantics this collapses to FAIL on the Reading_1 hypothesis tested.
Theorem-promotion-blocked at Stage-1 for Reading_1; Reading_2 retained
as the operative pole-scoping convention.

Volovik also flagged citation drift in `pru-class-corpus.md §3 line 87`:
pole-scope corpus instance #4 cites intermediate state (PASS spread
0.0513) but canonical-final state under Option A is FAIL spread 0.8946.
Routes to S89 corpus-citation-correction.
"""

import hashlib
import json
import sys
from pathlib import Path

_THIS = Path(__file__).resolve()
_REPO = _THIS.parent.parent.parent
sys.path.insert(0, str(_REPO / "computations" / "_shared"))
from canonical_constants import tau_fold  # noqa: E402,F401

GATE_ID = "S88-POLE-SCOPE-GENERIC-PLURALISM-VERIFY"
SCHEME = "stage-2-cross-axis-PASS-AND-aggregation-Reading_1-vs-Reading_2"
CONVENTION = "joint-theorem-promotion-md-stage-2-protocol-connes-axis-A-volovik-axis-B"


def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(d: dict) -> str:
    return hashlib.sha256(json.dumps(d, sort_keys=True, default=str).encode()).hexdigest()


def main():
    AXIS_A_JSON = _REPO / "computations" / "session-88" / "s88_w12_145_stage2_axis_a_connes.json"
    AXIS_B_JSON = _REPO / "computations" / "session-88" / "s88_w12_145_stage2_axis_b_volovik.json"
    PLAN_PATH = _REPO / "sessions" / "session-plan" / "session-88-plan-w12.md"
    JOINT_RULE_PATH = _REPO / ".claude" / "rules" / "joint-theorem-promotion.md"

    sha_axis_a = file_sha256(AXIS_A_JSON)
    sha_axis_b = file_sha256(AXIS_B_JSON)
    sha_plan = file_sha256(PLAN_PATH)
    sha_joint_rule = file_sha256(JOINT_RULE_PATH)

    # Per-axis Reading_1 verdicts
    axis_a_reading_1 = "FAIL"  # connes
    axis_b_reading_1 = "FAIL"  # volovik
    PASS_AND_reading_1 = (axis_a_reading_1 == "PASS" and axis_b_reading_1 == "PASS")

    # Composite: BOTH axes FAIL Reading_1 → Reading_1 closed; Reading_2
    # canonical
    sign_verdict = "N/A"
    magnitude_verdict = "FAIL"  # Reading_1 FAILS in both axes
    regime_verdict = "VALID"    # Stage-2 protocol fully satisfied
    composite_verdict = "FAIL"  # FAIL on Reading_1 generic-pluralism
    reading_outcome = "Reading_2-pole-specific-to-s3-canonical"

    print("=" * 72)
    print(f"ORCHESTRATOR AGGREGATE: {GATE_ID}")
    print("=" * 72)
    print()
    print(f"  Axis-A (connes) Reading_1: {axis_a_reading_1}")
    print(f"  Axis-B (volovik) Reading_1: {axis_b_reading_1}")
    print(f"  PASS-AND on Reading_1: {PASS_AND_reading_1}")
    print(f"  Reading_2 (pole-specific to s=3) canonical: True (both axes)")
    print(f"  composite          = {composite_verdict}")
    print(f"  reading_outcome    = {reading_outcome}")
    print()

    input_pin_map = {
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "axis_a_reading_1_verdict": axis_a_reading_1,
        "axis_b_reading_1_verdict": axis_b_reading_1,
        "PASS_AND_reading_1": PASS_AND_reading_1,
        "input_sha_axis_a": sha_axis_a,
        "input_sha_axis_b": sha_axis_b,
        "input_sha_plan": sha_plan,
        "input_sha_joint_rule": sha_joint_rule,
    }
    audit_sha256 = closure_hash(input_pin_map)
    content_sha256 = closure_hash({
        "sign_verdict": sign_verdict, "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict, "composite_verdict": composite_verdict,
        "reading_outcome": reading_outcome,
    })
    print(f"  audit_sha256:   {audit_sha256}")
    print(f"  content_sha256: {content_sha256}")

    verdict_file = _REPO / "computations" / "session-88" / "s88_gate_verdicts.txt"
    canonical_line = (
        f"{GATE_ID}: {composite_verdict} -- "
        f"value='stage2_BOTH_axes_FAIL_Reading_1_generic_pluralism;"
        f"axis_A_connes_4_subclause_FAIL_pole_scope_orthogonality_spread_anchor;"
        f"axis_B_volovik_FAIL_cross_regulator_spread_0_8946_GT_pre_reg_0_30_factor_2_98x;"
        f"plus_3_transit_side_structural_defects_dynamical_axis_frozen_anchor_formula_nonexistence_atlas_regulator_dependence;"
        f"Reading_2_pole_specific_to_s_3_CANONICAL_in_BOTH_axes;"
        f"VII_AH_clause_c_pole_specificity_scoping_RETAINED' "
        f"scheme={SCHEME} convention={CONVENTION} L_max=N/A "
        f"audit_sha256={audit_sha256} content_sha256={content_sha256} "
        f"schema_version=S87+\n"
    )
    dual_sha = (
        f"# audit_sha256_short={audit_sha256[:16]} "
        f"content_sha256_short={content_sha256[:16]} # {GATE_ID} "
        f"dual-SHA companion row (W9a-99 split)\n"
    )
    triple = (
        f"# sign_verdict={sign_verdict} magnitude_verdict={magnitude_verdict} "
        f"regime_verdict={regime_verdict} # {GATE_ID} 3-tuple annotation "
        f"(S87 schema-v2)\n"
    )
    diag = (
        f"# DIAGNOSTIC: Stage-2 cross-axis verify on Reading_1 (generic pluralism) "
        f"vs Reading_2 (pole-specific to s=3) for the W-9 spectral ↔ dynamical "
        f"anti-correlation. BOTH cross-reviewers FAIL Reading_1 with no shared "
        f"workshop context: connes (Axis-A) on 4 sub-clauses (Pole-Scope MANDATORY "
        f"violation, cross-pole co-primary FORBIDDEN violation, cross_regulator_"
        f"spread=0.8946 ≫ 0.30 by 2.98×, structural-anchor tautology); volovik "
        f"(Axis-B) on the same cross_regulator_spread numeric + 3 additional "
        f"transit-side structural defects (dynamical-axis frozen at s=4 = s=3 "
        f"baseline; s=4 anchor-formula non-existence; atlas regulator-class "
        f"dependence at s=4: zeta=-1.0 vs Zubarev=-0.105 spread 0.895). "
        f"Reading_1 CLOSED structurally. Reading_2 (pole-specific to s=3) is "
        f"canonical in BOTH axes; the §VII.AH STAGE-1-CANDIDATE clause (c) "
        f"pole-specificity scoping retained as Corrigendum 2 wording. "
        f"Volovik also flagged citation drift in `pru-class-corpus.md §3 line "
        f"87`: pole-scope corpus instance #4 cites intermediate-state PASS-"
        f"Reading_1 (cross_reg_spread=0.0513) but canonical-final state under "
        f"Option A latest-non-superseded reading is FAIL (cross_reg_spread="
        f"0.894591); routes to S89 corpus-citation-correction. Axis-A JSON "
        f"closure_sha=7983c32621cfcad6...; Axis-B JSON closure_sha="
        f"d7fabd737512f3c7....\n"
    )
    with open(verdict_file, "a", encoding="utf-8") as fh:
        fh.write(canonical_line)
        fh.write(dual_sha)
        fh.write(triple)
        fh.write(diag)
    print(f"\n[done] aggregate appended to {verdict_file}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
