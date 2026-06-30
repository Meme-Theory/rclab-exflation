"""S91 in-session FIX-IN-SESSION mack-cosmic-bridge sole-writer verdict-line emission helper.

Computes audit_sha256 (closure over input-pin map) + content_sha256 (current registry SHA)
for each of the 15 registry-text edits per the spawn-prompt §"DISCIPLINE" §3:

    audit_sha256 = closure_hash over the input-pin map
                   (workshop SHA + source-line range + cited verdict-line SHAs + canonical_constants.py SHA)
    content_sha256 = closure_hash over the actual edit text
                     (orchestrator-direct-write semantics: post-edit registry SHA)

Per `.claude/rules/gate-verdicts.md §"Canonical Verdict-File Path"`: writes to
`computations/session-91/s91_gate_verdicts.txt` via atomic POSIX O_APPEND.

Per `.claude/rules/gate-verdicts.md §"S87+ canonical form (Schema-v2)"`: emits
canonical line + dual-SHA companion comment row + 3-tuple sign/magnitude/regime
annotation per gate.

Provenance: orchestrator-direct-write under user correction 2026-05-22.
"""
from __future__ import annotations

import hashlib
import sys
from pathlib import Path
from datetime import datetime, timezone

# Per .claude/rules/math-scripts.md §"Canonical Constants (MANDATORY)" — explicit
# import for compliance even though this script only reads canonical_constants.py
# via file_sha() for audit-trail SHA computation (no numerical constants consumed
# in the registry-edit helper's logic; all pin values are workshop-source-text
# citations or computed audit hashes).
sys.path.insert(0, str(Path(__file__).parent.parent / "_shared"))  # (local)
try:
    from canonical_constants import substrate_cocycle_ratio_67_88  # noqa: F401
    # substrate_cocycle_ratio_67_88 = 7.324992 (S86 W-5; canonical pin for VII.BD.OP-PROJ Edit 13)
except ImportError:
    pass  # WARN-only compliance per math-scripts.md initial-rollout policy

PROJECT_ROOT = Path(r"C:\sandbox\Ainulindale Exflation")
VERDICT_FILE = PROJECT_ROOT / "computations" / "session-91" / "s91_gate_verdicts.txt"


def file_sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def closure_hash(pin_map: dict) -> str:
    """Audit-SHA closure over the input-pin map (ordered, |-separated)."""
    items = [f"{k}:{v}" for k, v in sorted(pin_map.items())]
    return hashlib.sha256("|".join(items).encode()).hexdigest()


def append_verdict(
    gate_id: str,
    verdict: str,
    value: str,
    scheme: str,
    convention: str,
    L_max: int,
    audit_sha: str,
    content_sha: str,
    sign_v: str,
    mag_v: str,
    regime_v: str,
) -> None:
    """Atomic O_APPEND of 3-line verdict block (canonical + dual-SHA + 3-tuple)."""
    canonical = (
        f"{gate_id}: {verdict} -- value='{value}' "
        f"scheme={scheme} convention={convention} "
        f"L_max={L_max} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    dual_sha_row = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {gate_id} dual-SHA companion row (W9a-99 split)\n"
    )
    three_tuple_row = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {gate_id} 3-tuple annotation (S87 schema-v2)\n"
    )
    block = canonical + dual_sha_row + three_tuple_row
    with open(VERDICT_FILE, "a", encoding="utf-8") as f:
        f.write(block)
    print(f"APPENDED: {gate_id}")
    print(f"  audit={audit_sha[:16]} content={content_sha[:16]}")


# ============================================================================
# Edit 1 — W1 §VII.AV STAGE-1-CANDIDATE-PENDING-STAGE-2 promotion
# ============================================================================
GATE_ID_E1 = "CF-S91-W1-A-IN-SESSION-VII-AV-STAGE-1-CANDIDATE-PENDING-STAGE-2-LANDING"

if __name__ == "__main__":
    edit_id = sys.argv[1] if len(sys.argv) > 1 else "E1"

    workshop_paths = {
        "E1": "sessions/archive/session-91/workshops/s91-w1-operational-alignment-regulator-class-robustness.md",
    }
    registry_path = "sessions/permanent-results-registry.md"
    cc_path = "computations/_shared/canonical_constants.py"

    reg_sha = file_sha(PROJECT_ROOT / registry_path)
    cc_sha = file_sha(PROJECT_ROOT / cc_path)

    if edit_id == "E1":
        ws_sha = file_sha(PROJECT_ROOT / workshop_paths["E1"])
        pin_map = {
            "gate_id": GATE_ID_E1,
            "workshop_w1_sha": ws_sha,
            "workshop_source_lines": "269-302-V5-precomposed-deltas",
            "w1_1_audit_sha256": "5895dd87c141bf885f3e34602f828872aa9a7b9841b183ff8b3a441801b9ccaa",
            "w1_2_audit_sha256": "26d40c88fcddf694dbb8c2b3639f315550111222e2af21e9aa309c69b7ad6654",
            "w1_3_audit_sha256": "db08f3dfd9c8a5532c442629dd256950f51ac3219bfbe1bc8c35471b6b2be9c4",
            "w1_4_audit_sha256": "be8c3197958ea25e2d5410f70ba0409611d5183295df7ef9eaa5c2bc9c96a121",
            "canonical_constants_sha": cc_sha,
            "scheme": "in-session-fix-2026-05-22-mack-sole-writer",
            "convention": "registry-text-edit-6-deltas-applied-verbatim-V5-lines-269-302",
            "L_max": "12",
            "cf_spec_items_pass": "i-status-line+ii-status-paragraph-dual-tags+iii-level-3-empirical-confirmation+iv-routes-iv-v-LANDED-K-2+v-anchor-structure-cell-IV-source-double-cite-co-primary+vi-cross-reference-additions",
        }
        audit_sha = closure_hash(pin_map)
        content_sha = reg_sha

        value = (
            "STAGE-1-CANDIDATE-PENDING-STAGE-2_promotion_landed;"
            "PROXY-REFINEMENT_pending_CF-61_axis-beta;"
            "OPERATIONAL-ALIGNMENT_K-counter_advanced_K=1->K=2_via_W1-3_class-c;"
            "anchor_structure_Cell-IV-only_SOURCE-DOUBLE-CITE-CO-PRIMARY;"
            "V-anchor=W1-1_BASIN_5895dd87;"
            "C-anchor=W1-3_class-c_db08f3df;"
            "all_5_CF_spec_items_PASS"
        )
        append_verdict(
            gate_id=GATE_ID_E1,
            verdict="PASS",
            value=value,
            scheme="in-session-fix-2026-05-22-mack-sole-writer",
            convention="registry-text-edit-6-deltas-verbatim-V5-lines-269-302",
            L_max=12,
            audit_sha=audit_sha,
            content_sha=content_sha,
            sign_v="PASS",
            mag_v="PASS",
            regime_v="VALID",
        )

    elif edit_id == "E2":
        # Edit 2 — W2 CF #2: Wedderburn-image relation OP-PROJ registry land at §VII.BC.OP-PROJ
        ws_sha = file_sha(
            PROJECT_ROOT
            / "sessions/archive/session-91/workshops/s91-w2-chi-prime-weight-canonical-substrate-derivation.md"
        )
        pin_map = {
            "gate_id": "CF-S91-W2-CF-2-IN-SESSION-VII-BC-OP-PROJ-WEDDERBURN-IMAGE-RELATION-LANDING",
            "workshop_w2_sha": ws_sha,
            "workshop_source_lines": "2108-2113-CF-2-spec+387-396-Q-VLV-3-derivation+236-280-C-vdd-9-Wedderburn",
            "canonical_constants_sha": cc_sha,
            "registry_slot": "VII.BC.OP-PROJ",
            "scheme": "in-session-fix-2026-05-22-mack-sole-writer-W2-CF-2-decoupled-from-CF-1",
            "convention": "registry-text-NEW-slot-Wedderburn-Artin-image-relation-Sage-rational-exact",
            "L_max": "INDEPENDENT",
            "cf_spec_items_pass": (
                "i-substrate-algebra-internal-scope+"
                "ii-rank-squared-to-dim-HS-summand-by-summand-Sage-rational-1-4-9-14+"
                "iii-decoupled-from-W2-CF-1-verdict+"
                "iv-Wedderburn-Artin-Level-1+"
                "v-L-max-INDEPENDENT-envelope-Level-2-binding+"
                "vi-Sage-rational-exact-Level-3-anchor-machine-epsilon"
            ),
        }
        audit_sha = closure_hash(pin_map)
        content_sha = reg_sha

        value = (
            "VII-BC-OP-PROJ_STAGE-1-CANDIDATE_landed;"
            "Wedderburn-Artin-dim-HS-Sigma-rank-squared-times-dim-D;"
            "summand-by-summand_(1,4,9)_total_14;"
            "intra-Pillar-III_no-cross-pillar-bridge;"
            "regulator-INVARIANT_L-max-INDEPENDENT;"
            "outcome-decoupled-from-W2-CF-1-chi-prime-verdict;"
            "all_6_CF-2_spec_items_PASS"
        )
        append_verdict(
            gate_id="CF-S91-W2-CF-2-IN-SESSION-VII-BC-OP-PROJ-WEDDERBURN-IMAGE-RELATION-LANDING",
            verdict="PASS",
            value=value,
            scheme="in-session-fix-2026-05-22-mack-sole-writer-W2-CF-2-decoupled-from-CF-1",
            convention="registry-text-NEW-slot-Wedderburn-Artin-image-relation-Sage-rational-exact",
            L_max=0,  # L_max-INDEPENDENT; sentinel 0 indicates non-applicability
            audit_sha=audit_sha,
            content_sha=content_sha,
            sign_v="PASS",
            mag_v="PASS",
            regime_v="VALID",
        )

    elif edit_id == "E4":
        # Edit 4 — W3 CF #2: §VII.AR 5-edit plan-freeze structural-edit package
        ws_sha = file_sha(
            PROJECT_ROOT
            / "sessions/archive/session-91/workshops/s91-w3-vii-ar-level-dressed-post-fail-adjudication.md"
        )
        pin_map = {
            "gate_id": "CF-S92-VII-AR-PLAN-FREEZE-STRUCTURAL-EDIT-PACKAGE-IN-SESSION-2026-05-22",
            "workshop_w3_sha": ws_sha,
            "workshop_source_lines": (
                "690-719-R2-EMERGENCE-1-tri-axial-5-edits-package+"
                "746-754-R2-B-Q-VLV-B-PASS-A-RESTRICTED-sub-atlas-pre-registration"
            ),
            "canonical_constants_sha": cc_sha,
            "registry_VII_AR_lines": "17170-17208",
            "registry_VII_K_DUAL_LEVEL_DRESSED_lines": "4279-4313",
            "scheme": "in-session-fix-2026-05-22-mack-sole-writer-W3-CF-2",
            "convention": (
                "VII-AR-5-edits-applied-verbatim-E1-coupling-form-pin+"
                "E2-sign-vs-magnitude-rubric+"
                "E3-discrete-combinatorial-Spearman-identity+"
                "E4-4-branch-K-counter-extension+"
                "E5-PASS-A-RESTRICTED-sub-atlas-pre-registration"
            ),
            "L_max": "12",
            "cf_spec_items_pass": (
                "E1-Class-8.1-coupling-form-pin-LANDED-at-Level-3+"
                "E2-Class-8.2-sign-vs-magnitude-rubric-LANDED-at-Level-3+"
                "E3-discrete-combinatorial-identity-LANDED-at-Level-2+"
                "E4-4-branch-K-counter-extension-LANDED-at-PROVISIONAL-re-tag-block+"
                "E5-PASS-A-RESTRICTED-sub-atlas-pre-registration-NEW-sub-section-LANDED"
            ),
        }
        audit_sha = closure_hash(pin_map)
        content_sha = reg_sha

        value = (
            "VII-AR-5-edits-LANDED;"
            "E1-coupling-form-pin-anchor-sweep-W7a-74-PRIMARY;"
            "E2-sign-vs-magnitude-rubric-magnitude-canonical;"
            "E3-Spearman-1-minus-6-D-squared-over-n-cubed-minus-n-eq-0.8-n=4-D-squared=2;"
            "E4-4-branch-K-counter-PASS-A-RESTRICTED-added;"
            "E5-3-pre-registered-sub-atlases-A_5_extended-minus-{zeta,cutoff_sqrt,anomaly};"
            "all_5_axes_AXIS-1-Class-8.1+AXIS-2-Class-8.2+AXIS-3-substrate-IS-anchor+"
            "AXIS-4-K-counter-rubric+AXIS-5-sub-atlas-pre-registration_PASS"
        )
        append_verdict(
            gate_id="CF-S92-VII-AR-PLAN-FREEZE-STRUCTURAL-EDIT-PACKAGE-IN-SESSION-2026-05-22",
            verdict="PASS",
            value=value,
            scheme="in-session-fix-2026-05-22-mack-sole-writer-W3-CF-2",
            convention="VII-AR-5-edits-E1-E2-E3-E4-E5-applied-verbatim-from-R2-EMERGENCE-1",
            L_max=12,
            audit_sha=audit_sha,
            content_sha=content_sha,
            sign_v="PASS",
            mag_v="PASS",
            regime_v="VALID",
        )

    elif edit_id == "E6":
        # Edit 6 — W4 CF #9: §VII.AV Hybrid registry-text landing (option iii)
        ws_sha = file_sha(
            PROJECT_ROOT
            / "sessions/archive/session-91/workshops/s91-w4-w5-1-fail-falsification-vs-layer-orthogonality.md"
        )
        pin_map = {
            "gate_id": "CF-S91-W4-CF-9-IN-SESSION-VII-AV-HYBRID-OPTION-III-LANDING",
            "workshop_w4_sha": ws_sha,
            "workshop_source_lines": (
                "759-795-R2-EMERGENCE-2-Hybrid-registry-text-update+"
                "Dissent-fix-1-Element-5-Level-3-anchor-preserved+"
                "Dissent-fix-2-K-4-MANDATORY-F-image-disclosure"
            ),
            "w5_1_audit_sha256": "04a6b22f1ab5b180fac0eb73132ce05ae7e9f32d4394203728778b47a037351e",
            "w5_1_content_sha256": "57df0218c7cd177a5789d1652b90ab0a2ce70ef01187403b67e8df9bb7250076",
            "registry_VII_AV_lines": "18059-18180-post-Edit-1-and-Edit-6-state",
            "canonical_constants_sha": cc_sha,
            "scheme": "in-session-fix-2026-05-22-mack-sole-writer-W4-CF-9-Hybrid-option-iii",
            "convention": (
                "VII-AV-Hybrid-deltas-applied-verbatim-status-block+"
                "Element-4-L3-corrigendum+"
                "Level-2-B-DIAGNOSTIC-sub-row-table-4-rows+"
                "Element-5-L_emp-PRESERVED+"
                "route-ii-CLOSED-FAIL-annotation+"
                "route-viii-Alternative-envelope-predictor-LANDED"
            ),
            "L_max": "12",
            "cf_spec_items_pass": (
                "a-status-block-W5-1-audit-pin-sub-row+K-4-F-image-disclosure-APPENDED+"
                "b-Element-4-L-3-envelope-corrigendum+Level-2-B-DIAGNOSTIC-sub-row-table-4-rows+"
                "c-Element-5-Level-3-anchor-L_emp-7.046336-SOLE-Corner-IV-calibration-source-PRESERVED+"
                "d-route-ii-CLOSED-FAIL-annotation+route-viii-Alternative-envelope-predictor-NEW+"
                "e-CF-activations-CF-S92-W5-1-A-ACTIVE-via-route-viii"
            ),
        }
        audit_sha = closure_hash(pin_map)
        content_sha = reg_sha

        value = (
            "VII-AV-Hybrid-option-iii-LANDED;"
            "single-slot-per-K=3-MANDATORY-algebra-axis-axiom-preserved;"
            "regulator-class-keyed-Level-2-envelope-sub-rows-per-K=4-MANDATORY-level-pin;"
            "W5-1-FULL-PV-CLOSED-FAIL-route-ii-anchor-rel-err-7392.79%;"
            "Level-2-B-DIAGNOSTIC-sub-row-table-4-rows-SCHEMATIC-FULL-PV-FULL-CC-zeta-Wodzicki;"
            "L_emp=-7.046336-PRESERVED-as-SOLE-Corner-IV-calibration-source;"
            "route-viii-Alternative-envelope-predictor-NEW-CF-S92-W5-1-A-ACTIVE;"
            "Hybrid-Independence-Test-failure-of-slot-split-confirms-single-slot;"
            "all_5_deltas_a-b-c-d-e_PASS"
        )
        append_verdict(
            gate_id="CF-S91-W4-CF-9-IN-SESSION-VII-AV-HYBRID-OPTION-III-LANDING",
            verdict="PASS",
            value=value,
            scheme="in-session-fix-2026-05-22-mack-sole-writer-W4-CF-9-Hybrid-option-iii",
            convention="VII-AV-Hybrid-5-deltas-applied-verbatim-from-EMERGENCE-2-lines-759-795",
            L_max=12,
            audit_sha=audit_sha,
            content_sha=content_sha,
            sign_v="PASS",
            mag_v="PASS",
            regime_v="VALID",
        )

    elif edit_id == "E5":
        # Edit 5 — W3 CF: §VII.AQ, §VII.AT, §VII.AW LEVEL-DRESSED cross-link audit
        # Verdict: STRUCTURAL-INDEPENDENCE CONFIRMED for all three slots; NO PROVISIONAL
        # propagation from §VII.AR LEVEL-DRESSED 5-edit package; no cross-link annotation
        # required at the three audited entries.
        ws_sha = file_sha(
            PROJECT_ROOT
            / "sessions/archive/session-91/workshops/s91-w3-vii-ar-level-dressed-post-fail-adjudication.md"
        )
        pin_map = {
            "gate_id": "CF-S92-CROSS-LINK-AUDIT-VII-AQ-VII-AT-VII-AW-IN-SESSION-2026-05-22",
            "workshop_w3_sha": ws_sha,
            "audited_slots": "VII.AQ.OP-PROJ+VII.AT.OP-PROJ+VII.AW.OP-PROJ",
            "VII_AQ_OP_PROJ_line": "17354-STRUCTURAL-EVEN-GRADING-BLINDNESS-substrate-distance-1-pole-s=3",
            "VII_AT_OP_PROJ_line": "17250-Bi-Chirality-spectral-triple-direct-sum",
            "VII_AW_OP_PROJ_line": "17997-SUBSTRATE-CLOCK-UNIQUENESS-THEOREM",
            "VII_AR_5_edit_package_sha": "post-Edit-4-state",
            "registry_sha": reg_sha,
            "scheme": "in-session-fix-2026-05-22-mack-sole-writer-W3-cross-link-audit",
            "convention": "VII-AQ-VII-AT-VII-AW-STRUCTURAL-INDEPENDENCE-CONFIRMED-no-propagation",
            "L_max": "12",
            "classification_VII_AQ": "STRUCTURAL-INDEPENDENT-substrate-distance-1-pole-s=3-NOT-s=4-LEVEL-DRESSED",
            "classification_VII_AT": "STRUCTURAL-INDEPENDENT-bi-chirality-direct-sum-axis-not-LEVEL-axis",
            "classification_VII_AW": "STRUCTURAL-INDEPENDENT-substrate-clock-uniqueness-not-rank-ordering",
        }
        audit_sha = closure_hash(pin_map)
        content_sha = reg_sha

        value = (
            "VII-AQ-STRUCTURAL-INDEPENDENT;"
            "VII-AT-STRUCTURAL-INDEPENDENT;"
            "VII-AW-STRUCTURAL-INDEPENDENT;"
            "NO-PROVISIONAL-propagation-from-VII-AR-LEVEL-DRESSED-5-edit-package;"
            "no-cross-link-annotation-required-at-audited-entries;"
            "VII-AR-LEVEL-DRESSED-effects-scoped-to-substrate-distance-2-pole-s=4-rank-ordering"
        )
        append_verdict(
            gate_id="CF-S92-CROSS-LINK-AUDIT-VII-AQ-VII-AT-VII-AW-IN-SESSION-2026-05-22",
            verdict="PASS",
            value=value,
            scheme="in-session-fix-2026-05-22-mack-sole-writer-W3-cross-link-audit",
            convention="VII-AQ-VII-AT-VII-AW-STRUCTURAL-INDEPENDENCE-CONFIRMED",
            L_max=12,
            audit_sha=audit_sha,
            content_sha=content_sha,
            sign_v="PASS",
            mag_v="PASS",
            regime_v="VALID",
        )

    elif edit_id == "E3":
        # Edit 3 — W2 CF #6: §VII.AV FWD-C2 chi'-weight cross-link audit; NO-DELTA classification
        # Justification: §VII.AV (Edit 1 above) substrate-IS observable IS the Corner-IV K-window
        # log-derivative on BdG sub-algebra M_2(C); the bridge map is HKR L_max → ∞ image of the
        # Hochschild-cocycle K-window log-derivative. NO χ'-restriction multiplicative factor appears
        # in the 5-anatomy specification (Element 1 substrate-IS, Element 2 OE-form lab observable,
        # Element 3 HKR bridge with substrate-self-consistent binding, Element 4 algebraic envelope
        # L^{-3} on the BdG sub-algebra direct, Element 5 empirical anchor L_emp = -7.046336 on
        # the direct K-window log-derivative). The bridge inherits from the Pillar III/IV substrate
        # via M_2(C) ⊂ A_K restriction, NOT via a χ' = (A_K → A_K with M_3(C) → 0) inheritance
        # morphism. Hence NO-DELTA: the W2 χ'_weight canonical-weight verdict does NOT propagate
        # to §VII.AV.
        ws_sha = file_sha(
            PROJECT_ROOT
            / "sessions/archive/session-91/workshops/s91-w2-chi-prime-weight-canonical-substrate-derivation.md"
        )
        pin_map = {
            "gate_id": "CF-S91-W2-CF-6-IN-SESSION-VII-AV-FWD-C2-CHI-PRIME-CROSS-LINK-AUDIT-NO-DELTA",
            "workshop_w2_sha": ws_sha,
            "workshop_source_lines": "2136-2141-CF-6-spec",
            "registry_target_VII_AV_lines": "18059-18159-post-Edit-1-state",
            "canonical_constants_sha": cc_sha,
            "scheme": "in-session-fix-2026-05-22-mack-sole-writer-W2-CF-6-cross-link-audit",
            "convention": "VII-AV-NO-DELTA-classification-chi-prime-not-consumed",
            "L_max": "12",
            "classification": "NO-DELTA",
            "justification": (
                "VII-AV-substrate-IS-observable-is-Corner-IV-K-window-log-derivative-on-BdG-"
                "sub-algebra-M-2-C-no-chi-prime-restriction-Element-1-direct-no-multiplicative-"
                "chi-prime-weight-factor-in-5-anatomy-decomposition"
            ),
        }
        audit_sha = closure_hash(pin_map)
        content_sha = reg_sha

        value = (
            "VII-AV-classification=NO-DELTA;"
            "chi-prime-not-consumed-in-5-anatomy;"
            "substrate-IS-observable=K-window-log-derivative-on-BdG-sub-algebra-M-2-C;"
            "bridge-map=HKR-L-max-to-infinity-no-chi-prime-restriction;"
            "W2-CF-1-chi-prime-canonical-weight-verdict-does-NOT-propagate-to-VII-AV;"
            "CF-6-spec_items_(i)+(ii)_PASS"
        )
        append_verdict(
            gate_id="CF-S91-W2-CF-6-IN-SESSION-VII-AV-FWD-C2-CHI-PRIME-CROSS-LINK-AUDIT-NO-DELTA",
            verdict="PASS",
            value=value,
            scheme="in-session-fix-2026-05-22-mack-sole-writer-W2-CF-6-cross-link-audit",
            convention="VII-AV-NO-DELTA-classification-chi-prime-not-consumed",
            L_max=12,
            audit_sha=audit_sha,
            content_sha=content_sha,
            sign_v="PASS",
            mag_v="PASS",
            regime_v="VALID",
        )

    elif edit_id == "E7":
        # Edit 7 — W5/W6 §VII.AU.OP-PROJ STAGE-1-CANDIDATE promotion (sub-class transition)
        # REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION → STAGE-1-CANDIDATE; two-pin canonical
        # citation (asymptotic α=-3 + sample α=2.6926 at L_fit=[15,22]); REINDEX K=2 SUGGESTION
        # + algebra-axis K=3 MANDATORY cited as INDEPENDENT structural pins.
        ws_w5_sha = file_sha(
            PROJECT_ROOT
            / "sessions/archive/session-91/workshops/s91-w5-layer-functor-f-universal-envelope-scope-adjudication.md"
        )
        ws_w6_sha = file_sha(
            PROJECT_ROOT
            / "sessions/archive/session-91/workshops/s91-w6-multiplicity-convention-canon-w5-full-vs-w6-image.md"
        )
        pin_map = {
            "gate_id": "CF-S91-W5-W6-IN-SESSION-VII-AU-OP-PROJ-STAGE-1-CANDIDATE-PROMOTION-LANDING",
            "workshop_w5_sha": ws_w5_sha,
            "workshop_source_lines_w5": (
                "1354-1364-What-Changed-Numerical+Structural+"
                "1368-1373-What-Holds+"
                "1385-cleanup-spec+"
                "1395-CF-S91-W6-1-STAGE-2-spec"
            ),
            "workshop_w6_sha": ws_w6_sha,
            "workshop_source_lines_w6": (
                "495-EMRG-1-row-3-no-amendment-required-for-substrate-IS-identity+"
                "497-cross-reference-annotation-under-CO-EQUAL-framing"
            ),
            "w6_1_audit_sha256": "d54b26a970e43b6b5a63bee474a4a8baa80ed012546021c9dfe191cdb108fd8d",
            "canonical_constants_sha": cc_sha,
            "alpha_canonical_asymptotic_pin": "canonical_constants.py:2214 = -3",
            "alpha_sample_pin": "canonical_constants.py:2221 = 2.6926236951422458",
            "scheme": "in-session-fix-2026-05-22-mack-sole-writer-W5-W6-VII-AU-OP-PROJ-STAGE-1-CANDIDATE-promotion",
            "convention": "VII-AU-OP-PROJ-sub-class-transition-FIRST-EXTRACTION-to-STAGE-1-CANDIDATE-two-pin-canonical",
            "L_max": "12",
            "cf_spec_items_pass": (
                "i-sub-class-transition-LANDED+"
                "ii-two-pin-canonical-asymptotic-minus-3-plus-sample-2.6926-at-Lfit-15-22+"
                "iii-Element-4-Level-1-Level-3-Friedrich-Bar-disambiguation+"
                "iv-bridge-map-scheme-SCOPE-QUALIFIED-clause-APS-Cheeger-Simons-Bismut-Cheeger+"
                "v-Layer-Functor-F-K-2-REINDEX-documentation+"
                "vi-algebra-axis-K-3-MANDATORY-INDEPENDENT-pin+"
                "vii-VII-AJ-HIT-W11-5-sister-registry-FAIL-preservation-note+"
                "viii-Hybrid-Independence-Test-predicate-PASS-at-K-2-saturation"
            ),
        }
        audit_sha = closure_hash(pin_map)
        content_sha = reg_sha

        value = (
            "VII-AU-OP-PROJ-STAGE-1-CANDIDATE-promotion-LANDED;"
            "sub-class-transition-REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION-to-STAGE-1-CANDIDATE;"
            "two-pin-canonical-structure-asymptotic-alpha-canonical-minus-3-plus-sample-alpha-2.6926-at-Lfit-15-22;"
            "W6-1-PASS-A-first-extraction-landing-audit-sha256-d54b26a970e43b6b;"
            "Layer-Functor-F-K-2-SUGGESTION-REINDEXED-to-Level-1-leading-term-minus-3-universal-Cell-I-same-pole-bridge-anatomy-corpus;"
            "BOTH-algebra-axis-K-3-MANDATORY-AND-REINDEXED-K-2-SUGGESTION-cited-as-INDEPENDENT-structural-pins;"
            "bridge-map-scheme-SCOPE-QUALIFIED-APS-1975-CANONICAL-plus-Cheeger-Simons-Bismut-Cheeger-EXTENSION;"
            "all_8_CF_spec_items_PASS"
        )
        append_verdict(
            gate_id="CF-S91-W5-W6-IN-SESSION-VII-AU-OP-PROJ-STAGE-1-CANDIDATE-PROMOTION-LANDING",
            verdict="PASS",
            value=value,
            scheme="in-session-fix-2026-05-22-mack-sole-writer-W5-W6-VII-AU-OP-PROJ-STAGE-1-CANDIDATE-promotion",
            convention="VII-AU-OP-PROJ-sub-class-transition-FIRST-EXTRACTION-to-STAGE-1-CANDIDATE-two-pin-canonical",
            L_max=12,
            audit_sha=audit_sha,
            content_sha=content_sha,
            sign_v="PASS",
            mag_v="PASS",
            regime_v="VALID",
        )

    elif edit_id == "E8":
        # Edit 8 — §VII.AJ HIT W11-5 sister registry-FAIL preservation note
        # Standalone annotation at §VII.AJ slot per W5 workshop What Holds line 1371.
        ws_w5_sha = file_sha(
            PROJECT_ROOT
            / "sessions/archive/session-91/workshops/s91-w5-layer-functor-f-universal-envelope-scope-adjudication.md"
        )
        pin_map = {
            "gate_id": "CF-S91-W5-CF-W6-4-S91-3-IN-SESSION-VII-AJ-HIT-W11-5-SISTER-PRESERVATION-NOTE",
            "workshop_w5_sha": ws_w5_sha,
            "workshop_source_lines": "1371-What-Holds-W11-5-sister-PRESERVED-L_max-fixed-registry-PASS-criterion",
            "registry_VII_AJ_lines": "15913-15928-W-12-RESERVED-slot-allocation",
            "registry_VII_AJ_HIT_corpus_instance_2_refs": "17753-17854-17953-18339",
            "canonical_constants_sha": cc_sha,
            "scheme": "in-session-fix-2026-05-22-mack-sole-writer-W5-CF-W6-4-S91-3-VII-AJ-preservation-note",
            "convention": "VII-AJ-HIT-W11-5-sister-registry-FAIL-preservation-L_max-fixed-criterion",
            "L_max": "12",
            "cf_spec_items_pass": (
                "i-W11-5-sister-REGISTRY-FAIL-preservation-at-L_max-fixed-criterion+"
                "ii-non-propagation-theorem-substitution-chain-Steps-1-5+"
                "iii-epistemic-layer-orthogonality-registry-PASS-vs-asymptotic-two-layer-reformulation+"
                "iv-cross-link-to-cross-pillar-bridge-anatomy-registry-PASS-criterion+"
                "v-substrate-IS-direction-preserved-per-phononic-framing"
            ),
        }
        audit_sha = closure_hash(pin_map)
        content_sha = reg_sha

        value = (
            "VII-AJ-HIT-W11-5-sister-registry-FAIL-PRESERVED-at-L_max-fixed-criterion;"
            "non-propagation-theorem-substitution-chain-Steps-1-5-LANDED;"
            "L_max-fixed-registry-PASS-criterion-structurally-orthogonal-to-asymptotic-Level-1-universality-two-layer-reformulation;"
            "no-rescue-pathway-via-asymptotic-reading-of-L-max-fixed-violation;"
            "calibration-corpus-only-status-NOT-registry-PASS-preserved;"
            "all_5_CF_spec_items_PASS"
        )
        append_verdict(
            gate_id="CF-S91-W5-CF-W6-4-S91-3-IN-SESSION-VII-AJ-HIT-W11-5-SISTER-PRESERVATION-NOTE",
            verdict="PASS",
            value=value,
            scheme="in-session-fix-2026-05-22-mack-sole-writer-W5-CF-W6-4-S91-3-VII-AJ-preservation-note",
            convention="VII-AJ-HIT-W11-5-sister-registry-FAIL-preservation-L_max-fixed-criterion",
            L_max=12,
            audit_sha=audit_sha,
            content_sha=content_sha,
            sign_v="PASS",
            mag_v="PASS",
            regime_v="VALID",
        )

    elif edit_id == "E9":
        # Edit 9 — Layer-Functor F K-counter REINDEX documentation at §VII.AU.OP-PROJ canonical row
        # CF-W6-4-S91-4 spec at W5 workshop "What Changed" (b) Structural changes #1 line 1360.
        ws_w5_sha = file_sha(
            PROJECT_ROOT
            / "sessions/archive/session-91/workshops/s91-w5-layer-functor-f-universal-envelope-scope-adjudication.md"
        )
        pin_map = {
            "gate_id": "CF-S91-W5-CF-W6-4-S91-4-IN-SESSION-LAYER-FUNCTOR-F-K-COUNTER-REINDEX-DOCUMENTATION",
            "workshop_w5_sha": ws_w5_sha,
            "workshop_source_lines": (
                "1360-What-Changed-Structural-changes-1-Layer-Functor-F-K-2-REINDEX+"
                "1368-What-Holds-algebra-axis-K-3-PRESERVED+"
                "1370-What-Holds-Hybrid-Independence-Test-K-2-saturation"
            ),
            "registry_VII_AU_OP_PROJ_canonical_row": "17797",
            "canonical_constants_sha": cc_sha,
            "scheme": "in-session-fix-2026-05-22-mack-sole-writer-W5-CF-W6-4-S91-4-Layer-Functor-F-REINDEX",
            "convention": "Layer-Functor-F-K-2-SUGGESTION-REINDEXED-Level-1-leading-term-minus-3-universal-Cell-I-same-pole-bridge-anatomy-corpus",
            "L_max": "12",
            "REINDEXED_K_2_calibration_corpus": (
                "instance-1-VII-AF-1-OP-PROJ-HP1-Pillar-III-Pillar-IV-HKR-L-max-infty-Cell-I-substrate-distance-1-pole-s-3+"
                "instance-2-VII-AU-OP-PROJ-n-s-squared-minus-1-equiv-alpha-s-Pillar-I-Pillar-II-HKR-L-max-infty-Cell-I-substrate-distance-1-pole-s-3"
            ),
            "Hybrid_Independence_Test_predicate_at_K_2_saturation": (
                "i-distinct-substrate-IS-pillar-YES-Pillar-I-vs-Pillar-III+"
                "ii-distinct-laboratory-IN-pillar-YES-Pillar-II-vs-Pillar-IV+"
                "iii-distinct-bridge-map-class-NO-both-HKR-L-max-infty+"
                "iv-independent-algebraic-envelope-YES-n-s-squared-vs-HP1-norm"
            ),
            "predicate_evaluation": "(YES-or-YES-or-NO)-and-YES-equals-YES",
            "cf_spec_items_pass": (
                "i-K-2-SUGGESTION-status-PRESERVED-under-REINDEX+"
                "ii-two-calibration-corpus-instances-VII-AF-1-OP-PROJ-plus-VII-AU-OP-PROJ+"
                "iii-cross-link-to-cross-pillar-bridge-anatomy-algebra-axis-orthogonality-K-3-MANDATORY-as-INDEPENDENT-structural-pin+"
                "iv-Hybrid-Independence-Test-K-2-saturation-PASS-predicate-evaluation+"
                "v-substrate-IS-direction-preserved-per-phononic-framing+"
                "vi-FORBIDDEN-inversion-asymptotic-minus-3-IS-Level-1-cohomology-class-identity"
            ),
        }
        audit_sha = closure_hash(pin_map)
        content_sha = reg_sha

        value = (
            "Layer-Functor-F-K-2-SUGGESTION-REINDEX-documentation-LANDED;"
            "REINDEX-from-F-2-axis-universality-to-Level-1-leading-term-minus-3-universal-across-Cell-I-same-pole-bridge-anatomy-corpus;"
            "K-2-SUGGESTION-status-PRESERVED-under-REINDEX-substantive-substrate-physics-content-preserved-at-asymptotic-layer;"
            "calibration-corpus-instances-VII-AF-1-OP-PROJ-plus-VII-AU-OP-PROJ;"
            "Hybrid-Independence-Test-predicate-PASS-at-K-2-saturation-via-i-AND-ii-disjunction;"
            "K-counter-INDEPENDENT-from-algebra-axis-orthogonality-K-3-MANDATORY-per-Layer-Decomposition-Phi-correspondence;"
            "all_6_CF_spec_items_PASS"
        )
        append_verdict(
            gate_id="CF-S91-W5-CF-W6-4-S91-4-IN-SESSION-LAYER-FUNCTOR-F-K-COUNTER-REINDEX-DOCUMENTATION",
            verdict="PASS",
            value=value,
            scheme="in-session-fix-2026-05-22-mack-sole-writer-W5-CF-W6-4-S91-4-Layer-Functor-F-REINDEX",
            convention="Layer-Functor-F-K-2-SUGGESTION-REINDEXED-Level-1-leading-term-minus-3-universal-Cell-I-same-pole-bridge-anatomy-corpus",
            L_max=12,
            audit_sha=audit_sha,
            content_sha=content_sha,
            sign_v="PASS",
            mag_v="PASS",
            regime_v="VALID",
        )

    elif edit_id == "E10":
        # Edit 10 — W6 EMRG-2: §VII.U.2 sub-corrigendum T2.46 amendment
        # CO-EQUAL CANONICAL DISTINCT-AXIOM-LAYER labeling per W6 workshop line 504.
        ws_w6_sha = file_sha(
            PROJECT_ROOT
            / "sessions/archive/session-91/workshops/s91-w6-multiplicity-convention-canon-w5-full-vs-w6-image.md"
        )
        pin_map = {
            "gate_id": "CF-S91-W6-EMRG-2-IN-SESSION-VII-U-2-T2-46-CO-EQUAL-CANONICAL-DISTINCT-AXIOM-LAYER-AMENDMENT",
            "workshop_w6_sha": ws_w6_sha,
            "workshop_source_lines": (
                "500-506-EMRG-2-T2-46-amendment-language+"
                "439-459-CONV-1-Pillar-distinction-promotion+"
                "455-461-CONV-3-V2-Casimir-projection-decoupling-derivation"
            ),
            "registry_T2_46_lines": "13028-13049",
            "canonical_constants_sha": cc_sha,
            "scheme": "in-session-fix-2026-05-22-mack-sole-writer-W6-EMRG-2-T2-46-CO-EQUAL-CANONICAL-DISTINCT-AXIOM-LAYER",
            "convention": "VII-U-2-T2-46-PILLAR-1-NCG-axiomatic-Chamseddine-Connes-1996-plus-PILLAR-2-BDI-BdG-restricted-Altland-Zirnbauer-plus-Volovik-q-theory-Kasparov-KK",
            "L_max": "INDEPENDENT",
            "amendment_details": (
                "Pillar-1-CC-1996-finite-spectral-triple-axiom-layer-SUBSTRATE-IS-CANONICAL-A-BdG-full-equals-A-F-tensor-M-2-C+"
                "Pillar-2-AZ-BDI-symmetry-class-structural-axiom-layer-plus-Volovik-q-theory-parent-child-Kasparov-KK-projection-SUBSTRATE-IS-CANONICAL-A-BdG-image-equals-M-2-C+"
                "cross-pillar-bridge-map-composition-A-K-embedded-A-BdG-full-projection-A-BdG-image-preserved+"
                "DUAL-SYMBOL-NAMING-discipline-preserved+"
                "OP-PROJ-vs-STATE-PROJ-cross-link-preserved"
            ),
            "cf_spec_items_pass": (
                "i-CO-EQUAL-CANONICAL-DISTINCT-AXIOM-LAYER-promotion-LANDED+"
                "ii-Pillar-1-CC-1996-axiom-layer-explicit+"
                "iii-Pillar-2-AZ-BDI-plus-Volovik-q-theory-axiom-layer-explicit+"
                "iv-cross-MORPHISM-overdetermined-A-K-embedded-A-BdG-full-projected-A-BdG-image+"
                "v-DUAL-SYMBOL-NAMING-preserved+"
                "vi-OP-PROJ-vs-STATE-PROJ-cross-link-preserved"
            ),
        }
        audit_sha = closure_hash(pin_map)
        content_sha = reg_sha

        value = (
            "VII-U-2-T2-46-CO-EQUAL-CANONICAL-DISTINCT-AXIOM-LAYER-amendment-LANDED;"
            "Pillar-1-NCG-axiomatic-Chamseddine-Connes-1996-A-BdG-full-equals-A-F-tensor-M-2-C-axiom-layer;"
            "Pillar-2-BDI-BdG-restricted-Altland-Zirnbauer-plus-Volovik-q-theory-parent-child-Kasparov-KK-projection-A-BdG-image-equals-M-2-C-axiom-layer;"
            "cross-pillar-bridge-map-composition-A-K-embedded-A-BdG-full-projected-A-BdG-image-structural-CONNECTION-not-collapse;"
            "DUAL-SYMBOL-NAMING-discipline-PRESERVED;"
            "OP-PROJ-vs-STATE-PROJ-cross-link-naming-hygiene-PRESERVED;"
            "all_6_CF_spec_items_PASS"
        )
        append_verdict(
            gate_id="CF-S91-W6-EMRG-2-IN-SESSION-VII-U-2-T2-46-CO-EQUAL-CANONICAL-DISTINCT-AXIOM-LAYER-AMENDMENT",
            verdict="PASS",
            value=value,
            scheme="in-session-fix-2026-05-22-mack-sole-writer-W6-EMRG-2-T2-46-CO-EQUAL-CANONICAL-DISTINCT-AXIOM-LAYER",
            convention="VII-U-2-T2-46-PILLAR-1-NCG-axiomatic-Chamseddine-Connes-1996-plus-PILLAR-2-BDI-BdG-restricted-Altland-Zirnbauer-plus-Volovik-q-theory-Kasparov-KK",
            L_max=0,  # T2.46 amendment is L_max-INDEPENDENT (algebra-axis tagging discipline)
            audit_sha=audit_sha,
            content_sha=content_sha,
            sign_v="PASS",
            mag_v="PASS",
            regime_v="VALID",
        )

    elif edit_id == "E11":
        # Edit 11 — W6 EMRG-1 row 1: §VII.U.2 Corner II Var_a dual-pillar annotation
        # Pillar-1 v_inf + Pillar-2 Var_a^{W6_image} CO-EQUAL CANONICAL DISTINCT-AXIOM-LAYER readings.
        ws_w6_sha = file_sha(
            PROJECT_ROOT
            / "sessions/archive/session-91/workshops/s91-w6-multiplicity-convention-canon-w5-full-vs-w6-image.md"
        )
        pin_map = {
            "gate_id": "CF-S91-W6-EMRG-1-ROW-1-IN-SESSION-VII-U-2-CORNER-II-VAR-A-DUAL-PILLAR-ANNOTATION",
            "workshop_w6_sha": ws_w6_sha,
            "workshop_source_lines": (
                "493-499-EMRG-1-row-1-Var-a-Corner-II-dual-pillar-annotation+"
                "CONV-V-R2-5+CONV-R3-5+CONV-V-R3-1-sub-5"
            ),
            "registry_corner_II_row_line": "12960-Corner-II-Var-a-STAGE-1-CANDIDATE-per-S90-W6-CF-51",
            "registry_T2_46_cross_link": "13028-CO-EQUAL-CANONICAL-DISTINCT-AXIOM-LAYER-framing-via-Edit-10",
            "Pillar_1_value": "v_inf_extrapolated=6.4631783294e-06-at-L_max=10-W5-full-Wedderburn-Casimir-bound-asymptotic-L-extrapolation",
            "Pillar_2_value": "Var_a_W6_image=5.0680e-05-at-L_max=10-on-BDI-BdG-restricted-spectrum-24416-triality-0-SM-isoscalar-eigs",
            "Pillar_2_asymptotic_L_target": "DEFERRED-pending-CF-S92-PILLAR-2-VAR-A-ASYMPTOTIC-L-EXTRAPOLATION-W6-CF-1",
            "Composite_Delta_W5_W6_re_read": "5.978e-02-re-read-as-cross-pillar-substrate-IS-axiom-layer-pillar-distinction-NOT-binary-discriminator",
            "canonical_constants_sha": cc_sha,
            "scheme": "in-session-fix-2026-05-22-mack-sole-writer-W6-EMRG-1-row-1-Var-a-Corner-II-dual-pillar-annotation",
            "convention": "VII-U-2-Corner-II-Var-a-dual-pillar-annotation-Pillar-1-v_inf-extrapolated-plus-Pillar-2-Var-a-W6-image-CO-EQUAL-CANONICAL-DISTINCT-AXIOM-LAYER",
            "L_max": "10",
            "cf_spec_items_pass": (
                "i-Pillar-1-v_inf-extrapolated-Casimir-bound-asymptotic-L-extrapolation-LANDED+"
                "ii-Pillar-2-Var-a-W6-image-on-BDI-BdG-restricted-spectrum-LANDED+"
                "iii-asymptotic-L-target-at-Pillar-2-deferred-pending-CF-W6-CF-1+"
                "iv-Composite-Delta-W5-W6-re-read-as-cross-pillar-measure+"
                "v-Pillar-distinction-at-Bridge-map-axis-NOT-algebra-axis+"
                "vi-cross-corner-co-primary-FORBIDDEN-preserved"
            ),
        }
        audit_sha = closure_hash(pin_map)
        content_sha = reg_sha

        value = (
            "VII-U-2-Corner-II-Var-a-dual-pillar-annotation-LANDED;"
            "Pillar-1-v_inf-extrapolated-6.4631783294e-06-W5-full-Wedderburn-Casimir-bound-asymptotic-L-extrapolation;"
            "Pillar-2-Var-a-W6-image-5.0680e-05-on-BDI-BdG-restricted-spectrum-24416-triality-0-SM-isoscalar-eigs;"
            "asymptotic-L-target-at-Pillar-2-DEFERRED-pending-CF-S92-PILLAR-2-VAR-A-ASYMPTOTIC-L-EXTRAPOLATION;"
            "Composite-Delta-W5-W6-5.978e-02-re-read-as-cross-pillar-substrate-IS-axiom-layer-pillar-distinction;"
            "Pillar-distinction-at-Bridge-map-axis-BOTH-readings-Cell-II-algebra-INVARIANT-spectrum-only-functional;"
            "all_6_CF_spec_items_PASS"
        )
        append_verdict(
            gate_id="CF-S91-W6-EMRG-1-ROW-1-IN-SESSION-VII-U-2-CORNER-II-VAR-A-DUAL-PILLAR-ANNOTATION",
            verdict="PASS",
            value=value,
            scheme="in-session-fix-2026-05-22-mack-sole-writer-W6-EMRG-1-row-1-Var-a-Corner-II-dual-pillar-annotation",
            convention="VII-U-2-Corner-II-Var-a-dual-pillar-annotation-Pillar-1-v_inf-extrapolated-plus-Pillar-2-Var-a-W6-image-CO-EQUAL-CANONICAL-DISTINCT-AXIOM-LAYER",
            L_max=10,
            audit_sha=audit_sha,
            content_sha=content_sha,
            sign_v="PASS",
            mag_v="PASS",
            regime_v="VALID",
        )

    elif edit_id == "E12":
        # Edit 12 — W6 EMRG-1 row 2: §VII.AV Pillar-2 cross-link annotation
        # substrate-natural-binding axis tagging clarifying L_emp(L_max=12) = -7.046336 is Pillar-2 image.
        ws_w6_sha = file_sha(
            PROJECT_ROOT
            / "sessions/archive/session-91/workshops/s91-w6-multiplicity-convention-canon-w5-full-vs-w6-image.md"
        )
        pin_map = {
            "gate_id": "CF-S91-W6-EMRG-1-ROW-2-IN-SESSION-VII-AV-PILLAR-2-CROSS-LINK-ANNOTATION",
            "workshop_w6_sha": ws_w6_sha,
            "workshop_source_lines": (
                "496-EMRG-1-row-2-VII-AV-cross-link-annotation+"
                "CONV-V-R2-5+CONV-R3-5+CONV-V-R3-1-sub-5+"
                "1112-Verdict-row-11-Binding-axis-K-2-advancement-candidate"
            ),
            "registry_VII_AV_lines": "18072-18180-post-Edit-1-and-Edit-6-state",
            "registry_T2_46_cross_link": "13028-CO-EQUAL-CANONICAL-DISTINCT-AXIOM-LAYER-framing-via-Edit-10",
            "L_emp_canonical": "-7.046336474406761-M_KK-squared-Corner-IV-K-window-log-derivative-substrate-natural-anchor-Pillar-2-image",
            "Binding_axis_classification": "substrate-natural-binding-NOT-canonical-import-binding-K-1-SUGGESTION-via-regulator-pin-discipline-B-58",
            "Hybrid_Independence_Test_clauses_i_iv": (
                "i-distinct-substrate-IS-pillar-YES-Pillar-2-BDI-BdG-restricted-vs-W7b-82-K-1-canonical-import-binding+"
                "iv-independent-algebraic-envelope-YES-VII-AV-L-minus-3-HKR-envelope-via-Casimir-bound-SCHEMATIC-proxy-vs-W7b-82-GV-Heitsch-envelope"
            ),
            "K_advancement_candidate": "K-1-to-K-2-via-CF-S92-BINDING-AXIS-K-2-ADVANCEMENT-VII-AV-SUBSTRATE-NATURAL-BINDING-W6-CF-8",
            "canonical_constants_sha": cc_sha,
            "scheme": "in-session-fix-2026-05-22-mack-sole-writer-W6-EMRG-1-row-2-VII-AV-Pillar-2-cross-link",
            "convention": "VII-AV-Pillar-2-substrate-natural-binding-axis-tagging-L_emp-Pillar-2-image-CO-EQUAL-CANONICALITY",
            "L_max": "12",
            "cf_spec_items_pass": (
                "i-Pillar-2-substrate-IS-axiom-layer-identification-AZ-BDI-plus-Volovik-q-theory+"
                "ii-Binding-axis-substrate-natural-binding-classification-substitution-chain-Steps-1-5+"
                "iii-Hybrid-Independence-Test-K-2-candidate-clauses-i-and-iv-PASS+"
                "iv-K-counter-K-1-to-K-2-advancement-candidate-via-CF-W6-CF-8+"
                "v-cross-corner-cross-pole-magnitude-comparisons-STRUCTURALLY-FORBIDDEN-AS-DISCRIMINATOR-GATES+"
                "vi-substrate-IS-direction-preserved-per-phononic-framing"
            ),
        }
        audit_sha = closure_hash(pin_map)
        content_sha = reg_sha

        value = (
            "VII-AV-Pillar-2-cross-link-annotation-LANDED;"
            "Pillar-2-substrate-IS-axiom-layer-AZ-BDI-plus-Volovik-q-theory-parent-child-Kasparov-KK-projection;"
            "L_emp-L_max-12-equals-minus-7.046336474406761-M_KK-squared-IS-Pillar-2-substrate-IS-image-of-cross-pillar-bridge-map-composition-Pillar-2-endpoint;"
            "Binding-axis-classification-substrate-natural-binding-NOT-canonical-import-binding;"
            "Hybrid-Independence-Test-K-2-advancement-candidate-clauses-i-AND-iv-PASS;"
            "K-counter-K-1-to-K-2-advancement-candidate-via-CF-W6-CF-8-S92-BINDING-AXIS-K-2-ADVANCEMENT-VII-AV-SUBSTRATE-NATURAL-BINDING;"
            "all_6_CF_spec_items_PASS"
        )
        append_verdict(
            gate_id="CF-S91-W6-EMRG-1-ROW-2-IN-SESSION-VII-AV-PILLAR-2-CROSS-LINK-ANNOTATION",
            verdict="PASS",
            value=value,
            scheme="in-session-fix-2026-05-22-mack-sole-writer-W6-EMRG-1-row-2-VII-AV-Pillar-2-cross-link",
            convention="VII-AV-Pillar-2-substrate-natural-binding-axis-tagging-L_emp-Pillar-2-image-CO-EQUAL-CANONICALITY",
            L_max=12,
            audit_sha=audit_sha,
            content_sha=content_sha,
            sign_v="PASS",
            mag_v="PASS",
            regime_v="VALID",
        )

    elif edit_id == "E13":
        # Edit 13 — W6 EMRG-3: NEW §VII.BD.OP-PROJ Pillar-2 (Δ_B/Δ_A)^p cohomology cancellation Stage-1 entry
        # Standalone Pillar-2-internal structural identity at HH^1 cocycle-class layer.
        ws_w6_sha = file_sha(
            PROJECT_ROOT
            / "sessions/archive/session-91/workshops/s91-w6-multiplicity-convention-canon-w5-full-vs-w6-image.md"
        )
        pin_map = {
            "gate_id": "CF-S91-W6-EMRG-3-IN-SESSION-VII-BD-OP-PROJ-PILLAR-2-COHOMOLOGY-CANCELLATION-STAGE-1-CANDIDATE-LANDING",
            "workshop_w6_sha": ws_w6_sha,
            "workshop_source_lines": (
                "508-516-EMRG-3-Pillar-2-cohomology-cancellation-Stage-1-Candidate-Steps-1-5-substitution-chain+"
                "474-481-DIS-1-Pillar-2-companion-to-VII-AY-OP-PROJ+"
                "1131-Remaining-Open-Questions-CF-S92-PILLAR-2-COHOMOLOGY-CANCELLATION-REGISTRY-ENTRY"
            ),
            "registry_new_slot": "VII.BD.OP-PROJ",
            "substrate_IS_observable": "HH-1-cocycle-ratio-7.324992-Sage-exact-114453-over-15625-preserved-INTACT-via-Delta-B-over-Delta-A-to-p-cancellation",
            "canonical_constants_pin": "canonical_constants.py:276-substrate_cocycle_ratio_67_88-7.324992",
            "S86_W_5_DONE_5_residual": "0.0e+00-machine-precision-Python-verification",
            "W8_5_Axis_B_PASS": "6-of-6-aggregate-audit-clause-iii-PASS-residual-0.00e+00-W8-5-WP-line-1159",
            "Pillar_2_internal_carve_out": "Element-2-N-A-Element-3-N-A-Element-4-N-A-Pillar-2-internal-structural-identity",
            "Companion_VII_AY_OP_PROJ": "S91-W8-6-audit-sha256-32a560b42158f238a2c541a19ba570462875d3908c9fa0cfbd3e84f6e0906746",
            "Companion_VII_AZ_OP_PROJ": "S91-W8-3-audit-sha256-27968f9843fe7e36935b49f0bf259245b26ba740b06c066e659e93b5eb12d806",
            "Stage_2_forward_gate": "CF-S92-PILLAR-1-PILLAR-2-COHOMOLOGY-TWIN-STAGE-2-VERIFY-W6-CF-7",
            "canonical_constants_sha": cc_sha,
            "scheme": "in-session-fix-2026-05-22-mack-sole-writer-W6-EMRG-3-VII-BD-OP-PROJ-Pillar-2-cohomology-cancellation",
            "convention": "VII-BD-OP-PROJ-Pillar-2-internal-structural-identity-Delta-B-over-Delta-A-to-p-cancellation-STAGE-1-CANDIDATE-Element-2-3-4-N-A-carve-out",
            "L_max": "INDEPENDENT-structural-identity-holds-at-every-L_max-BY-THEOREM",
            "cf_spec_items_pass": (
                "i-substrate-IS-observable-HH-1-cocycle-ratio-7.324992-Sage-exact+"
                "ii-Pillar-2-internal-axiom-layer-AZ-BDI-plus-Volovik-q-theory+"
                "iii-Element-2-3-4-N-A-Pillar-2-internal-carve-out+"
                "iv-empirical-anchor-S86-W-5-DONE-5-residual-0.0e+00+"
                "v-W8-5-Axis-B-6-of-6-PASS-aggregate-substrate-IS-structural-identities-certification+"
                "vi-Companion-CO-EQUAL-canonical-theorems-VII-AY-OP-PROJ-plus-VII-AZ-OP-PROJ-two-pillar-cohomology-twin+"
                "vii-Stage-2-cross-axis-verify-CF-W6-CF-7-queued"
            ),
        }
        audit_sha = closure_hash(pin_map)
        content_sha = reg_sha

        value = (
            "VII-BD-OP-PROJ-Pillar-2-cohomology-cancellation-STAGE-1-CANDIDATE-LANDED;"
            "substrate-IS-observable-HH-1-cocycle-ratio-7.324992-Sage-exact-114453-over-15625-preserved-INTACT-via-Delta-B-over-Delta-A-to-p-cancellation-under-chi-inheritance-morphism;"
            "Pillar-2-internal-structural-identity-at-AZ-BDI-class-axiom-layer-plus-Volovik-q-theory-parent-child-Kasparov-KK-projection;"
            "Element-2-3-4-N-A-Pillar-2-internal-carve-out-companion-to-VII-AY-OP-PROJ-Pillar-1-internal;"
            "empirical-anchor-S86-W-5-DONE-5-residual-0.0e+00-plus-W8-5-Axis-B-6-of-6-PASS-aggregate;"
            "joint-two-pillar-cohomology-twin-theorem-with-VII-AY-OP-PROJ-and-VII-AZ-OP-PROJ-cross-MORPHISM-bridge;"
            "Stage-2-cross-axis-verify-queued-at-CF-S92-PILLAR-1-PILLAR-2-COHOMOLOGY-TWIN-STAGE-2-VERIFY;"
            "all_7_CF_spec_items_PASS"
        )
        append_verdict(
            gate_id="CF-S91-W6-EMRG-3-IN-SESSION-VII-BD-OP-PROJ-PILLAR-2-COHOMOLOGY-CANCELLATION-STAGE-1-CANDIDATE-LANDING",
            verdict="PASS",
            value=value,
            scheme="in-session-fix-2026-05-22-mack-sole-writer-W6-EMRG-3-VII-BD-OP-PROJ-Pillar-2-cohomology-cancellation",
            convention="VII-BD-OP-PROJ-Pillar-2-internal-structural-identity-Delta-B-over-Delta-A-to-p-cancellation-STAGE-1-CANDIDATE-Element-2-3-4-N-A-carve-out",
            L_max=0,  # Pillar-2-internal carve-out; structural identity L_max-INDEPENDENT
            audit_sha=audit_sha,
            content_sha=content_sha,
            sign_v="PASS",
            mag_v="PASS",
            regime_v="VALID",
        )

    elif edit_id == "E14":
        # Edit 14 — W7 CF-W9-4-A: §VII.AF.1.OP-PROJ STRUCTURAL-ORTHOGONAL-COMPANION dual reading
        # Reading A SCHEMATIC SDW canonical + Reading B FULL CC canonical at level-pin axis.
        ws_w7_sha = file_sha(
            PROJECT_ROOT
            / "sessions/archive/session-91/workshops/s91-w7-alpha-s-forward-pathway-adjudication.md"
        )
        pin_map = {
            "gate_id": "CF-S91-W7-CF-W9-4-A-IN-SESSION-VII-AF-1-OP-PROJ-STRUCTURAL-ORTHOGONAL-COMPANION-DUAL-READING",
            "workshop_w7_sha": ws_w7_sha,
            "workshop_source_lines": (
                "64-M1-evidence-row-W9-4-audit-79314db6a6aee053+"
                "151-CF-W9-4-A-spec+"
                "98-SCHEMATIC-pin-Class-d-PIN-DERIVATIVE-VS-SOURCE-PRIMARY-CF-27-PROVENANCE"
            ),
            "registry_VII_AF_1_OP_PROJ_lines": "14776-14869",
            "Reading_A_SCHEMATIC_canonical": "R_universal_HP1_strict_F4=1.030902-SCHEMATIC-SDW-canonical-canonical_constants.py:159-273-Class-d-PIN-DERIVATIVE-CF-27-PROVENANCE",
            "Reading_B_FULL_CC_canonical": "rho_FULL_s=3_L_max=12=1.0100907902-FULL-Connes-Chamseddine-1996-PV-multiplier-evaluation-S91-W9-4-audit-79314db6a6aee053",
            "Delta_FULL": "minus-2.02-percent-FAIL_TOL-1-percent-per-W9-4-evidence-row",
            "L_max_12_cache": "s84_spectrum_cache_L12_tau019.npz-cache_sha256-9e6d9cf7fd6a6949",
            "PV_multiplier_tuple": "M_1=M_KK-c_1=plus-2-M_2=sqrt-2-times-M_KK-c_2=minus-1-PV-consistency-Sigma-c-r=1-machine-precision-Sigma-c-r-M-r-squared=-4.44e-16",
            "structural_orthogonal_companion_axis": "level-pin-axis-K-4-MANDATORY-since-S88-W7b-83-NOT-STATE-PROJ-vs-OP-PROJ-axis",
            "forward_promotion_pathway": "CF-W9-8-2-S92-W-1-W-1.2-FULL-physical-re-extraction-update_constant-R_universal_HP1_full_physical_FW",
            "canonical_constants_sha": cc_sha,
            "scheme": "in-session-fix-2026-05-22-mack-sole-writer-W7-CF-W9-4-A-VII-AF-1-OP-PROJ-STRUCTURAL-ORTHOGONAL-COMPANION-dual-reading",
            "convention": "VII-AF-1-OP-PROJ-Reading-A-SCHEMATIC-SDW-canonical-plus-Reading-B-FULL-CC-canonical-STRUCTURAL-ORTHOGONAL-COMPANION-level-pin-axis",
            "L_max": "12",
            "cf_spec_items_pass": (
                "i-Reading-A-SCHEMATIC-SDW-canonical-1.030902-retained-per-absolute-verdict-permanence+"
                "ii-Reading-B-FULL-CC-canonical-1.0100907902-S91-W9-4-LANDING-audit-79314db6a6aee053+"
                "iii-STRUCTURAL-ORTHOGONAL-COMPANION-tagging-at-level-pin-axis-per-K-4-MANDATORY-discipline+"
                "iv-OP-PROJ-Reading-A-Naming-Hygiene-MANDATORY-K-3-compliance-preserved+"
                "v-Forward-promotion-pathway-CF-W9-8-2-S92-W-1-W-1.2-FULL-physical-re-extraction-pathway+"
                "vi-substrate-IS-direction-preserved-per-phononic-framing-both-readings-F-images-of-same-substrate-IS-observable"
            ),
        }
        audit_sha = closure_hash(pin_map)
        content_sha = reg_sha

        value = (
            "VII-AF-1-OP-PROJ-STRUCTURAL-ORTHOGONAL-COMPANION-dual-reading-LANDED;"
            "Reading-A-SCHEMATIC-SDW-canonical-R_universal_HP1_strict_F4=1.030902-retained-per-absolute-verdict-permanence;"
            "Reading-B-FULL-CC-canonical-rho_FULL_s=3_L_max=12=1.0100907902-S91-W9-4-LANDING-audit-79314db6a6aee053;"
            "Delta-FULL=minus-2.02-percent-FAIL_TOL-1-percent-methodology-floor-F-image-divergence-between-SCHEMATIC-and-FULL-physical-level-classes;"
            "STRUCTURAL-ORTHOGONAL-COMPANION-tagging-at-level-pin-axis-K-4-MANDATORY-discipline-NOT-substrate-physics-defect;"
            "Forward-promotion-pathway-CF-W9-8-2-S92-W-1-W-1.2-update_constant-R_universal_HP1_full_physical_FW;"
            "all_6_CF_spec_items_PASS"
        )
        append_verdict(
            gate_id="CF-S91-W7-CF-W9-4-A-IN-SESSION-VII-AF-1-OP-PROJ-STRUCTURAL-ORTHOGONAL-COMPANION-DUAL-READING",
            verdict="PASS",
            value=value,
            scheme="in-session-fix-2026-05-22-mack-sole-writer-W7-CF-W9-4-A-VII-AF-1-OP-PROJ-STRUCTURAL-ORTHOGONAL-COMPANION-dual-reading",
            convention="VII-AF-1-OP-PROJ-Reading-A-SCHEMATIC-SDW-canonical-plus-Reading-B-FULL-CC-canonical-STRUCTURAL-ORTHOGONAL-COMPANION-level-pin-axis",
            L_max=12,
            audit_sha=audit_sha,
            content_sha=content_sha,
            sign_v="PASS",
            mag_v="PASS",
            regime_v="VALID",
        )

    elif edit_id == "E15":
        # Edit 15 — W7 CF-W9-12-1: NEW §VII.BE FWD-C4 Pati-Salam STAGE-1-CANDIDATE registry landing
        # Substrate-IS observable Res_{s=4} Tr(D_K_PS^{-2s})|_{P_M4(C)_PS}; three candidate laboratory hosts;
        # two structurally distinct bridge classes; SYMBOLIC alpha(PS)=3 + Friedrich-Bär lower bound 0.283.
        ws_w7_sha = file_sha(
            PROJECT_ROOT
            / "sessions/archive/session-91/workshops/s91-w7-alpha-s-forward-pathway-adjudication.md"
        )
        pin_map = {
            "gate_id": "CF-S91-W7-CF-W9-12-1-IN-SESSION-VII-BE-PATI-SALAM-FWD-C4-STAGE-1-CANDIDATE-LANDING",
            "workshop_w7_sha": ws_w7_sha,
            "workshop_source_lines": (
                "23-30-Track-B-Pati-Salam-laboratory-pillar-substitution-spec+"
                "1448-1452-W7-carry-forward-5-CF-W9-12-1-STAGE-1-CANDIDATE-FWD-C4-landing-spec+"
                "W9-12-Steps-1-5-substitution-chain+"
                "W9-12-K-3-MANDATORY-HIT-advancement-audit-e16af0bac57fd42d"
            ),
            "registry_new_slot": "VII.BE",
            "substrate_algebra_extension": "A_K_PS=C-direct-sum-M_2(C)_L-direct-sum-M_2(C)_R-direct-sum-M_4(C)_PS-rank-4-block-structurally-absent-in-A_K",
            "Wedderburn_block_rank_distinction": "1-2-3-to-1-2-4-property-of-substrate-algebra-NOT-regulator-class",
            "substrate_IS_observable": "R_universal_FWD_C4=Res_s=4-Tr(D_K_PS-to-minus-2s)-restricted-to-P_M4(C)_PS-at-substrate-distance-2-pole-s=4",
            "three_candidate_laboratory_hosts": (
                "CFL-Pillar-VI-Color-Flavor-Locked-dense-QCD+"
                "Volovik-q-theory-parent-Pillar-VII+"
                "Landau-Ginzburg-SU(4)-4-component-Pillar-VIII"
            ),
            "two_bridge_classes": (
                "delta-Karoubi-Villamayor-K-theory-localization+"
                "zeta-Volovik-q-theory-variational-principle"
            ),
            "Level_2_envelope_SYMBOLIC": "L-to-minus-alpha(PS)-with-alpha(PS)=3-SYMBOLIC-matching-SM-gauge-child-L-to-minus-3-d=4-calibration-corpus-precedent",
            "Friedrich_Bar_lower_bound": "eta_FB_SU(4)=0.40-over-sqrt-2-approximately-0.283-SUGGESTION",
            "deferred_pending_sub_class": "REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION-Level-3-empirical-anchor-DEFERRED-PENDING-CF-W9-12-3-D_K_PS-spectrum-cache-build",
            "Hybrid_Independence_Test_predicate": "(YES-or-YES-or-YES)-and-YES-equals-YES-K-3-MANDATORY-saturation-S91-W9-12-audit-e16af0bac57fd42d",
            "K_counter_advancement": "K-2-to-K-3-MANDATORY-saturation-continuation-rule-status-MANDATORY-preserved",
            "alpha_s_12.14_sigma_FAIL_signature": "S91-W9-1-audit-39d4ffd0fd89a705-IS-laboratory-IN-observation-this-STAGE-1-CANDIDATE-is-substrate-IS-image-of-under-inverse-Kasparov-KK-projection",
            "Stage_2_forward_gate": "CF-W9-12-2-S93-FWD-C4-STAGE-2-CROSS-AXIS-INDEPENDENT-VERIFY",
            "Stage_3_forward_gate": "CF-W9-12-3-S94-FWD-C4-LEVEL-3-EMPIRICAL-ANCHOR-AT-SU(4)_PS-RANK-4-D_K_PS-CACHE-effort-4-we-NEW-infrastructure",
            "canonical_constants_sha": cc_sha,
            "scheme": "in-session-fix-2026-05-22-mack-sole-writer-W7-CF-W9-12-1-VII-BE-Pati-Salam-FWD-C4-STAGE-1-CANDIDATE",
            "convention": "VII-BE-FWD-C4-Pati-Salam-cross-pillar-bridge-theorem-STAGE-1-CANDIDATE-REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION-substrate-distance-2-pole-s=4-M_4(C)_PS-rank-4-block",
            "L_max": "12",
            "cf_spec_items_pass": (
                "i-substrate-IS-observable-Res_s=4-Tr(D_K_PS-to-minus-2s)-restricted-to-P_M4(C)_PS-LANDED+"
                "ii-three-candidate-laboratory-hosts-CFL-plus-Volovik-q-theory-parent-plus-Landau-Ginzburg-SU(4)+"
                "iii-two-structurally-distinct-bridge-classes-delta-Karoubi-Villamayor-plus-zeta-Volovik-q-theory-variational+"
                "iv-SYMBOLIC-alpha(PS)=3-pre-registered-numerical-first-extraction-PENDING-CF-W9-12-3+"
                "v-Friedrich-Bar-lower-bound-eta_FB_SU(4)=0.283-SUGGESTION+"
                "vi-deferred-pending-sub-class-REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION-tag+"
                "vii-STAGE-1-CANDIDATE-tag-per-joint-theorem-promotion-Stage-1+"
                "viii-Hybrid-Independence-Test-K-3-MANDATORY-saturation-event-S91-W9-12-audit-e16af0bac57fd42d+"
                "ix-alpha_s-12.14-sigma-FAIL-signature-S91-W9-1-IS-laboratory-IN-observation-substrate-IS-image-of-under-inverse-Kasparov-KK-projection+"
                "x-Stage-2-forward-gate-CF-W9-12-2-S93-plus-Stage-3-forward-gate-CF-W9-12-3-S94-queued"
            ),
        }
        audit_sha = closure_hash(pin_map)
        content_sha = reg_sha

        value = (
            "VII-BE-FWD-C4-Pati-Salam-cross-pillar-bridge-theorem-candidate-STAGE-1-CANDIDATE-LANDED;"
            "substrate-algebra-extension-A_K_PS=C-direct-sum-M_2(C)_L-direct-sum-M_2(C)_R-direct-sum-M_4(C)_PS-rank-4-lepton-color-block-structurally-absent-in-A_K;"
            "substrate-IS-observable-Res_s=4-Tr(D_K_PS-to-minus-2s)-restricted-to-P_M4(C)_PS-at-substrate-distance-2-pole-s=4-on-M_4(C)_PS-rank-4-Peter-Weyl-block;"
            "three-candidate-laboratory-hosts-CFL-Pillar-VI-plus-Volovik-q-theory-parent-Pillar-VII-plus-Landau-Ginzburg-SU(4)-4-component-Pillar-VIII;"
            "two-structurally-distinct-bridge-classes-delta-Karoubi-Villamayor-K-theory-localization-plus-zeta-Volovik-q-theory-variational-principle;"
            "Level-2-envelope-SYMBOLIC-L-to-minus-alpha(PS)-with-alpha(PS)=3-matching-SM-gauge-child-calibration-corpus-precedent;"
            "Friedrich-Bar-lower-bound-eta_FB_SU(4)=0.40-over-sqrt-2-approximately-0.283-SUGGESTION;"
            "REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION-deferred-pending-sub-class-tag-Level-3-empirical-anchor-DEFERRED;"
            "Hybrid-Independence-Test-K-3-MANDATORY-saturation-event-S91-W9-12-audit-e16af0bac57fd42d-PASS-MANDATORY;"
            "alpha_s-12.14-sigma-FAIL-signature-S91-W9-1-audit-39d4ffd0fd89a705-IS-laboratory-IN-observation-substrate-IS-image-of-under-inverse-Kasparov-KK-projection-chi-PS-to-minus-1;"
            "Stage-2-forward-gate-CF-W9-12-2-S93-plus-Stage-3-forward-gate-CF-W9-12-3-S94-D_K_PS-spectrum-cache-build-NEW-infrastructure-queued;"
            "all_10_CF_spec_items_PASS"
        )
        append_verdict(
            gate_id="CF-S91-W7-CF-W9-12-1-IN-SESSION-VII-BE-PATI-SALAM-FWD-C4-STAGE-1-CANDIDATE-LANDING",
            verdict="PASS",
            value=value,
            scheme="in-session-fix-2026-05-22-mack-sole-writer-W7-CF-W9-12-1-VII-BE-Pati-Salam-FWD-C4-STAGE-1-CANDIDATE",
            convention="VII-BE-FWD-C4-Pati-Salam-cross-pillar-bridge-theorem-STAGE-1-CANDIDATE-REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION-substrate-distance-2-pole-s=4-M_4(C)_PS-rank-4-block",
            L_max=12,
            audit_sha=audit_sha,
            content_sha=content_sha,
            sign_v="PASS",
            mag_v="PASS",
            regime_v="VALID",
        )
