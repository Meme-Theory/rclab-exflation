#!/usr/bin/env python3
"""
_s90_w1_13_connes_co_sign_emit.py — connes-ncg CO-AUTHOR verdict emitter for
S90 W1-13 Element-2 OE-form calibration-entry row #3 review.

Computes content_sha256 over the post-edit corpus file
(`sessions/framework/registry/cross-pillar-bridge-corpus.md`; matches the
primary W1-13 verdict's content_sha256), and audit_sha256 over an 8-pin
input-pin map: 6 spawn-prompt-pinned SHAs + verdict classification +
reasoning summary.

Per `.claude/rules/gate-verdicts.md` S87+ schema + `s90_w1_emit_verdict.py`
canonical helper.
"""
from __future__ import annotations
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from canonical_constants import *  # noqa: F401,F403  (mandatory per computations/_shared/CLAUDE.md)
from s90_w1_emit_verdict import emit_verdict  # noqa: E402


def main() -> int:
    gate_id = "S90-CROSS-PILLAR-BRIDGE-CORPUS-ELEMENT-2-OE-FORM-CALIBRATION-ENTRY-CONNES-CO-SIGN"  # (local)
    verdict = "PASS"  # (local)

    # 8-pin input-pin map for audit_sha256 closure
    # 6 spawn-prompt pins + verdict classification + reasoning summary
    input_pin_map = {  # (local)
        # Spawn-prompt pin 1: plan §W1-13 block SHA (5416 chars at lines 861-925)
        "plan_w1_13_block_sha256": "a8fadbc0a8160698b092bc63f0e7bd1244211fd50352ddd7743d0a20e145526d",
        # Spawn-prompt pin 2: post-edit corpus SHA (matches content_sha256)
        "corpus_post_edit_sha256": "e1b3e891847b43fd253e584501f5e13745daca2ac31ae4941ed76842d375f4ee",
        # Spawn-prompt pin 3: parent rule (cross-pillar-bridge-anatomy.md) SHA
        "rule_anatomy_sha256": "0d6673941ced8df1b44f2e5b05fd012fbb72d32593b14ae6021ac6b95f7680cd",
        # Spawn-prompt pin 4: W7c emission #3 verdict audit_sha256
        "w7c_emission_3_audit_sha256": "cc18126581ddd9a1ea0fa9f92e4d881219773fc363f749be082c8f2b429cc61d",
        # Spawn-prompt pin 5: audit-script line range for OE-form regex
        "audit_script_oe_regex_pin": "_cross_pillar_bridge_audit.py:154-200",
        # Spawn-prompt pin 6: W1-13 primary verdict audit_sha256
        "w1_13_primary_audit_sha256": "4debd49bdc5f3f5dac54546da54d881e5e25a50cdd02b0f88429a55c9975a8a6",
        # Verdict classification
        "co_sign_verdict": "PASS-CO-SIGN-WITH-NOTES",
        # Reasoning summary (one-line digest)
        "reasoning_summary": (
            "lexical correctly captures substrate-IS / lab-IN bridge anatomy at "
            "substrate-distance-1 pole s=3; named-projector P_n-s-substrate-distance-1 "
            "well-defined as band-0 at s=3 per Connes-Moscovici 1995 §III.4 + W7a "
            "Sage-QQ identity n_s_FW^2 - 1 = alpha_s_canonical in Q; BZ integration "
            "domain is HKR push-forward of Peter-Weyl spectral measure; pole-localization "
            "structurally correct via tau_fold-pinned band-0 projector. THREE NOTES: "
            "(1) ASCII Pi->P downgrade loses Connes-convention distinction Pi (substrate "
            "projector) vs P (ambient projector); (2) density factor rho_BZ(k; tau_fold) "
            "not captured by parent-rule positive-match regex - regex validates only "
            "projector-trace skeleton not weighted form; (3) two registry entries "
            "(VII.AU at line 17250 + VII.AV at line 17335) co-exist for the same FWD-C1 "
            "landing with notation-bifurcation Pi^{n_s}_{s.d.1} vs P_n-s-s.d.1 - "
            "structurally consistent but worth flagging."
        ),
    }

    value_str = (  # (local)
        "co_sign_with_notes;"
        "named_projector_well_defined=True;"
        "integration_domain_HKR_push_forward=True;"
        "substrate_distance_1_pole_localization_correct=True;"
        "oe_form_structural_intent_satisfied=True;"
        "note_1=ASCII-Pi-to-P-downgrade-loses-Connes-convention-substrate-vs-ambient;"
        "note_2=rho_BZ-density-factor-not-captured-by-positive-match-regex;"
        "note_3=VII-AU-VII-AV-notation-bifurcation-Pi-vs-P-for-same-landing;"
        "axis=NCG-axiomatic;"
        "review_type=parallel-co-author-not-Stage2-cross-axis-verify;"
        "primary_w1_13_verdict_intact=True"
    )

    scheme = "cross-pillar-bridge-corpus-element-2-extension-co-author-review"  # (local)
    convention = "oe-form-w7c-emission-3-lexical-NCG-axiomatic-axis"  # (local)
    L_max = "N/A"  # (local)

    # Content target is the post-edit corpus file (matches primary verdict)
    # __file__ = .../computations/_shared/_s90_w1_13_connes_co_sign_emit.py
    # parents[0]=_shared/, parents[1]=computations/, parents[2]=project-root/
    content_target = Path(__file__).resolve().parents[2] / "sessions" / "framework" / "registry" / "cross-pillar-bridge-corpus.md"  # (local)

    result = emit_verdict(  # (local)
        gate_id=gate_id,
        verdict=verdict,
        value_str=value_str,
        scheme=scheme,
        convention=convention,
        L_max=L_max,
        input_pin_map=input_pin_map,
        content_target=content_target,
        supersedes="",
    )

    import json
    print(json.dumps({
        "gate_id": result["gate_id"],
        "verdict": result["verdict"],
        "audit_sha256": result["audit_sha256"],
        "content_sha256": result["content_sha256"],
        "canonical_line_first_120": result["canonical_line"][:120],
    }, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
