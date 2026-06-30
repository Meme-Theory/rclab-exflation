#!/usr/bin/env python3
"""S90 W1-13 — Cross-pillar bridge corpus §2 Element-2 OE-form K=3 calibration entry.

Per `sessions/session-plan/session-90-plan-w1.md` §W1-13.

This script performs the artifact-existence + regex-match verification for the
S90 W1-13 METHODOLOGY-class landing:

  1. Verifies that orchestrator-direct-edit of `cross-pillar-bridge-corpus.md §2`
     has landed row #3 (W7c emission #3 lexical + audit-pattern-documentation
     paragraph + K=2 → K=3 header advancement).
  2. Applies the [VERIFY] trigger — regex match of the W7c emission #3 lexical
     `∫_BZ d^d k Tr(P_n-s-substrate-distance-1) · ρ_BZ(k; τ_fold)` against the
     positive-match regex `(?:\\int|∫|\\sum|∑).*?(?:d.*?)?Tr.*?\\([ΠP][_^].*?\\)`
     (audit-script implementation; F-image of the rule's canonical pattern
     `\\int.*d.*Tr.*\\([ΠP]_[a-z0-9_-]+\\)`).
  3. Appends W1-13 row to `methodology-wave-allowlist.md`.
  4. Appends W1-13 rationale to `methodology-wave-instances.md`.
  5. Emits canonical verdict line + dual-SHA companion row at
     `computations/session-90/s90_gate_verdicts.txt`.

Per `wave-classification.md §"Dual-SHA closure for METHODOLOGY-class"`:
  - audit_sha256 = SHA-256 over JSON-serialized input-pin map (sorted keys).
  - content_sha256 = SHA-256 over post-edit `cross-pillar-bridge-corpus.md`
    (the rule-file diff target).
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "computations" / "_shared"))

from canonical_constants import *  # noqa: F401,F403 — canonical-constants discipline
from s90_w1_emit_verdict import emit_verdict, sha256_of_file  # canonical emitter


# --- Paths ---
CORPUS = ROOT / "sessions" / "framework" / "registry" / "cross-pillar-bridge-corpus.md"
ANATOMY = ROOT / ".claude" / "rules" / "cross-pillar-bridge-anatomy.md"
INSTANCES = ROOT / "sessions" / "framework" / "registry" / "methodology-wave-instances.md"
ALLOWLIST = ROOT / ".claude" / "rules" / "methodology-wave-allowlist.md"
AUDIT_SCRIPT = ROOT / "computations" / "_shared" / "_cross_pillar_bridge_audit.py"


# --- Constants (local — gate identity + pinned SHAs) ---
GATE_ROW = "W1-13"                                                       # (local)
SESSION = "S90"                                                          # (local)
GATE_ID = "S90-CROSS-PILLAR-BRIDGE-CORPUS-ELEMENT-2-OE-FORM-CALIBRATION-ENTRY"  # (local)
PLAN_BLOCK_SHA = "a8fadbc0a8160698b092bc63f0e7bd1244211fd50352ddd7743d0a20e145526d"  # (local)

# Pre-edit input-pin SHAs (pinned by orchestrator at dispatch — see plan §W1-13 #7)
CORPUS_PRE_EDIT_SHA = "b40f407abd979e10672504f13b00a60ffa2e97725a5da239ec02ef3225016539"  # (local)
ANATOMY_SHA = "0d6673941ced8df1b44f2e5b05fd012fbb72d32593b14ae6021ac6b95f7680cd"  # (local)
INSTANCES_PRE_EDIT_SHA = "47cd45f6e2c812b17efb222f960825869df8969bc0a30219ba648b795346ae13"  # (local)
ALLOWLIST_PRE_EDIT_SHA = "23a54af664503e879e5c393def188b9fbc1a6053965b54215cd6105f8ebe23a3"  # (local)
AUDIT_SCRIPT_SHA = "490dd8818830a46d4cc78b31bd6e01b649699068db02dca9b4af9254719886ad"  # (local)
W7C_EMISSION_3_AUDIT_SHA = "cc18126581ddd9a1ea0fa9f92e4d881219773fc363f749be082c8f2b429cc61d"  # (local)

# Lexical pin + regex pins
LEXICAL_PIN = "∫_BZ d^d k Tr(P_n-s-substrate-distance-1) · ρ_BZ(k; τ_fold)"  # (local)
PLAN_REGEX_CANONICAL = r"\int.*d.*Tr.*\([ΠP]_[a-z0-9_-]+\)"               # (local)
AUDIT_REGEX_IMPL = r"(?:\\int|∫|\\sum|∑).*?(?:d.*?)?Tr.*?\([ΠP][_^].*?\)"  # (local)

# K-counter pins
K_BEFORE = 2                                                              # (local)
K_AFTER = 3                                                               # (local)
K_PROMOTION = 3                                                           # (local) per feedback_rules-compensate-missing-structure.md

# Post-edit corpus markers required by plan §W1-13 #9 PASS criterion
REQUIRED_POST_EDIT_MARKERS = [                                            # (local)
    "K=3 calibration corpus (S88 W7a-73 baseline + S90 W1-13 advancement)",
    "S89 W7c emission #3 (§VII.AV rerouted; HIT K-counter K=2→K=3)",
    LEXICAL_PIN,
    "VALIDATED-W7c-EMISSION-3-LEXICAL",
    "Audit pattern documentation (S90 W1-13 landing)",
    W7C_EMISSION_3_AUDIT_SHA,  # the row cites the W7c verdict-line SHA explicitly
]


# --- Build-content blocks (allowlist row + instances rationale) ---

ALLOWLIST_ROW = f"| {GATE_ROW} | {SESSION} | {PLAN_BLOCK_SHA} |\n"

INSTANCES_RATIONALE_TEMPLATE = """
### {gate_row} ({session}) — {plan_block_sha}

**Provenance**: gate-ID `{gate_id}`
(PHONON-FIRST V.7); agents `gen-physicist orchestrator-direct-write` + `mack-cosmic-bridge` (writer per `feedback_mack-bridge-role.md`) + CO-AUTHOR `connes-ncg-theorist` (Element-2 OE-form corpus structural review per Cluster A header); plan reference
`sessions/session-plan/session-90-plan-w1.md` §W1-13 lines 861-925; plan-block
sha256 `{plan_block_sha}` (5416 chars, 65 lines).

**Gate classification (M1∧M2∧M3∧M4 conjunction)**:
- **M1**: artifact-existence-with-substantive-content per `wave-classification.md §M1`.
  PASS predicate = (i) row #3 appended to `cross-pillar-bridge-corpus.md §2` with
  full SHA pin (`{w7c_sha}`) + lexical form + regex match annotation; (ii) audit
  pattern documentation paragraph appended; (iii) allowlist + instances rows
  appended. No numerical comparison; all conditions are artifact-existence +
  content-substance + regex-match verification.
- **M2**: producing operations restricted to Edit/Write on rule-files +
  registry files + this verification script + canonical
  `s90_w1_emit_verdict.py` helper. No numerical comparisons against pre-
  registered thresholds; the only numerical step is a Boolean regex match
  applied to the pre-pinned lexical (audit-script regex
  `(?:\\\\int|∫|\\\\sum|∑).*?(?:d.*?)?Tr.*?\\([ΠP][_^].*?\\)` against
  `∫_BZ d^d k Tr(P_n-s-substrate-distance-1) · ρ_BZ(k; τ_fold)`).
- **M3**: verbatim sub-diff from plan §W1-13 #6 dispatch prompt (the corpus
  row text, audit-pattern paragraph, and substitution chain are all verbatim
  from the plan). The W7c emission #3 lexical is verbatim from the S89
  rerouted §VII.AV.OP-PROJ verdict-line value-field
  (`computations/session-89/s89_gate_verdicts.txt:143`, audit_sha256
  `{w7c_sha}`). No first-principles new derivation.
- **M4**: row landing per `methodology-wave-allowlist.md §"Edit discipline"`
  orchestrator-only-edit protocol.

**Sub-clause structure landed**:
1. `cross-pillar-bridge-corpus.md §2` header advanced from "K=2 calibration
   corpus (S88 W7a-73)" to "K=3 calibration corpus (S88 W7a-73 baseline +
   S90 W1-13 advancement)". The K=2 → K=3 advancement saturates the
   K_promotion=3 threshold per
   `feedback_rules-compensate-missing-structure.md`. The Element 2 OE-form
   discipline's underlying status is unchanged (MANDATORY at S88+ plan-freeze
   per `cross-pillar-bridge-anatomy.md §"Element 2 OE-form discipline"`); the
   K-counter advancement is structural-saturation of the calibration corpus,
   not status change.
2. Row #3 appended to the §2 calibration-corpus table with: bridge source
   (S89 W7c emission #3 / §VII.AV rerouted), Element-2 lexical form
   (`∫_BZ d^d k Tr(P_n-s-substrate-distance-1) · ρ_BZ(k; τ_fold)`), positive-
   match regex (`\\int.*d.*Tr.*\\([ΠP]_[a-z0-9_-]+\\)`), verdict (PASS
   VALIDATED-W7c-EMISSION-3-LEXICAL), and explicit citation of the W7c
   emission #3 verdict-line audit_sha256 `{w7c_sha}`
   at `s89_gate_verdicts.txt:143`.
3. "Audit pattern documentation (S90 W1-13 landing)" sub-section appended
   below the calibration-corpus table, carrying the 4-step substitution
   chain pre-registered at plan §W1-13 #10 (definition → substitution →
   simplify → direction) and explicit mapping of the rule's canonical
   pattern `\\int.*d.*Tr.*\\([ΠP]_[a-z0-9_-]+\\)` to the audit-script
   implementation `(?:\\\\int|∫|\\\\sum|∑).*?(?:d.*?)?Tr.*?\\([ΠP][_^].*?\\)`
   at `_cross_pillar_bridge_audit.py:158`.

**Closure conditions**: PASS verdict per pre-registered #9 (i)-(iii) — three
operational conditions satisfied (corpus row #3 + audit pattern documentation
+ allowlist/instances rows). audit_sha256 over 11-pin input-pin map
(plan_block_sha + 5 file pre-edit SHAs + W7c emission #3 verdict SHA + plan
regex + audit-script regex + lexical pin + K-counter status). content_sha256
over post-edit `cross-pillar-bridge-corpus.md` (the rule-file diff target).
Regex match validation: `re.search(audit_regex, lexical_pin)` returns a
non-None match object (group(0) = `∫_BZ d^d k Tr(P_n-s-substrate-distance-1)`).

**Cross-link**: `sessions/session-plan/session-90-plan-w1.md` §W1-13 (plan
reference, 5416-char block, sha256=`{plan_block_sha}`);
`sessions/framework/registry/cross-pillar-bridge-corpus.md §2` (K=3
calibration corpus + audit pattern documentation; this is the rule-file diff
target); `.claude/rules/cross-pillar-bridge-anatomy.md §"Element 2 OE-form
discipline"` (parent rule statement; MANDATORY at S88+ plan-freeze);
`computations/_shared/_cross_pillar_bridge_audit.py` line 154-158
(`ELEMENT_2_OE_POSITIVE_REGEX` implementation); W7c emission #3 verdict at
`computations/session-89/s89_gate_verdicts.txt:143` audit_sha256
`{w7c_sha}` (`element_2_oe_form=True` per
`s89_w7c_*.py` emission; slot=§VII.AV.OP-PROJ after rerouting from §VII.AU);
`feedback_rules-compensate-missing-structure.md` (K-counter promotion
threshold; K=3 saturated at this landing);
`feedback_mack-bridge-role.md` (registry-writer designation for mack-cosmic-
bridge on cross-pillar bridge registry entries).

**Carry-forward (2 substantive items)**:
1. Future cross-pillar bridge entries citing Element-2 lexical forms SHOULD
   register additional rows in §2 to grow the corpus beyond K=3. The K-counter
   advancement to K≥4 is no longer threshold-binding (already MANDATORY at
   S88+ per the parent rule) but enriches the binary-classifier calibration
   beyond the current 1-PASS-baseline + 1-FAIL-counterexample + 1-PASS-new-
   instance shape. Substrate-distance-2 and substrate-distance-3 bridge
   instances would be natural K≥4 candidates.
2. W7c emission #3 composite verdict at `s89_gate_verdicts.txt:143` is FAIL
   (magnitude_verdict=FAIL on the overall registry-landing gate); only the
   element_2_oe_form sub-condition was PASS. The FAIL is a separate substrate-
   physics carry-forward (FWD-C1 Pillar-I-II bridge magnitude convergence) not
   discharged by W1-13; W1-13 documents only the Element-2 OE-form structural
   subset that PASSed at the W7c emission #3 slot. The §VII.AU vs §VII.AV
   rerouting is documented per the W7c emission chain
   (line 140 emission #1/#2 at §VII.AU with element_2_oe_form=False, line 143
   emission #3 at §VII.AV with element_2_oe_form=True, supersedes chain
   anchored at `c857179040b40224...`).

**Parallel-review dispatch**: APPLICABLE per --tasking "as applicable"
clause. Plan §W1-13 #4 names CO-AUTHOR `connes-ncg-theorist` (Element-2 OE-
form corpus structural review per Cluster A header). Dispatched in background
post-WP-update per the --tasking modifier: "task the identified review agent
as a parallel review after you move on". Connes-ncg-theorist's review-axis
is the NCG-axiomatic perspective on whether the W7c emission #3 lexical
`Tr(P_n-s-substrate-distance-1) · ρ_BZ(k; τ_fold)` correctly captures the
substrate-IS / laboratory-IN bridge anatomy at substrate-distance-1.

**Substrate framing**: Element-2 OE-form IS the laboratory-IN observable's
structural form pinned to the substrate sub-algebra image under the bridge
map ι_*. The named projector `P_n-s-substrate-distance-1` IS substrate-IS
(an operator-projection on the substrate's Peter-Weyl block decomposition at
the substrate-distance-1 sector); the BZ-trace `∫_BZ d^d k · ρ_BZ(k; τ_fold)`
IS the laboratory-IN integral over emergent Brillouin zone (the ρ_BZ density
is the substrate's own measure pushed forward under HKR-image). The corpus
row makes this lexical form auditable for future bridge entries: any S88+
bridge entry whose Element-2 specification matches the positive regex
inherits the substrate-IS / laboratory-IN structural anchor by construction.
Container-thinking violation FORBIDDEN: "the BZ is a container in which the
laboratory operates" — inverted: "the BZ IS the emergent topological-momentum
manifold pushed forward from the substrate sub-algebra by ι_*; the lab
observable IS the trace of P_n-s-substrate-distance-1 against the BZ-density".
Direction of explanation: substrate sub-algebra → bridge map ι_* → laboratory
observable on emergent BZ — never inverted.
"""


# --- Verification + emission ---

def verify_post_edit_corpus() -> dict:
    """Verify all required markers are present in post-edit corpus."""
    text = CORPUS.read_text(encoding="utf-8")
    missing = [m for m in REQUIRED_POST_EDIT_MARKERS if m not in text]
    return {
        "all_markers_present": len(missing) == 0,
        "missing": missing,
        "markers_checked": len(REQUIRED_POST_EDIT_MARKERS),
        "markers_found": len(REQUIRED_POST_EDIT_MARKERS) - len(missing),
    }


def verify_regex_match() -> dict:
    """[VERIFY] trigger — regex match per substitution chain (plan §W1-13 #10)."""
    audit_match = re.search(AUDIT_REGEX_IMPL, LEXICAL_PIN)
    # The plan-canonical regex `\int.*d.*Tr.*\([ΠP]_[a-z0-9_-]+\)` interprets
    # `\int` as an integration token per the corpus authoring convention. In
    # Python regex, `\i` is literal `i`, so the literal plan regex would NOT
    # match Unicode `∫`. The audit-script implementation expands `\int` to the
    # alternation `(?:\\int|∫|\\sum|∑)` which is the operational F-image.
    return {
        "audit_regex_used": AUDIT_REGEX_IMPL,
        "plan_canonical_regex_documented": PLAN_REGEX_CANONICAL,
        "lexical_pin": LEXICAL_PIN,
        "match_object_str": audit_match.group(0) if audit_match else None,
        "match_PASS": audit_match is not None,
    }


def build_input_pin_map(
    regex_match_pass: bool,
    markers_present: bool,
) -> dict:
    """Construct ordered input-pin map for audit_sha256 computation."""
    return {
        "gate_id": GATE_ID,
        "plan_block_sha": PLAN_BLOCK_SHA,
        "corpus_pre_edit_sha": CORPUS_PRE_EDIT_SHA,
        "anatomy_rule_sha": ANATOMY_SHA,
        "instances_pre_edit_sha": INSTANCES_PRE_EDIT_SHA,
        "allowlist_pre_edit_sha": ALLOWLIST_PRE_EDIT_SHA,
        "audit_script_sha": AUDIT_SCRIPT_SHA,
        "w7c_emission_3_audit_sha": W7C_EMISSION_3_AUDIT_SHA,
        "plan_canonical_regex": PLAN_REGEX_CANONICAL,
        "audit_regex_implementation": AUDIT_REGEX_IMPL,
        "lexical_pin": LEXICAL_PIN,
        "K_before": K_BEFORE,
        "K_after": K_AFTER,
        "K_promotion": K_PROMOTION,
        "regex_match_pass": regex_match_pass,
        "post_edit_markers_present": markers_present,
    }


def main() -> int:
    # Step 1 — Verify post-edit corpus state (the orchestrator-direct-edit must have landed)
    post_edit_check = verify_post_edit_corpus()
    if not post_edit_check["all_markers_present"]:
        print(json.dumps({
            "error": "Post-edit corpus state verification FAILED",
            "check": post_edit_check,
        }, indent=2))
        return 1

    # Step 2 — [VERIFY] regex match validation
    regex_check = verify_regex_match()
    if not regex_check["match_PASS"]:
        print(json.dumps({
            "error": "Regex match validation FAILED",
            "check": regex_check,
        }, indent=2))
        return 1

    # Step 3 — Append allowlist row
    with ALLOWLIST.open("a", encoding="utf-8") as f:
        f.write(ALLOWLIST_ROW)
    print(f"Allowlist row appended: {ALLOWLIST_ROW.strip()}")

    # Step 4 — Append instances rationale
    rationale = INSTANCES_RATIONALE_TEMPLATE.format(
        gate_row=GATE_ROW,
        session=SESSION,
        plan_block_sha=PLAN_BLOCK_SHA,
        gate_id=GATE_ID,
        w7c_sha=W7C_EMISSION_3_AUDIT_SHA,
    )
    with INSTANCES.open("a", encoding="utf-8") as f:
        f.write(rationale)
    print(f"Instances rationale appended: {rationale.count(chr(10))} lines, {len(rationale)} chars")

    # Step 5 — Emit verdict line + dual-SHA companion row
    # content_target = post-edit corpus (the rule-file diff target per
    # wave-classification.md §"Dual-SHA closure for METHODOLOGY-class")
    input_pin_map = build_input_pin_map(
        regex_match_pass=regex_check["match_PASS"],
        markers_present=post_edit_check["all_markers_present"],
    )
    value_str = (
        f"corpus_row_3_appended_with_lexical_AND_regex_match_PASS"
        f";k_advance={K_BEFORE}to{K_AFTER}"
        f";k_promotion_threshold={K_PROMOTION}"
        f";k_promotion_saturated=True"
        f";regex_match_PASS=True"
        f";post_edit_markers_found={post_edit_check['markers_found']}_of_{post_edit_check['markers_checked']}"
        f";w7c_emission_3_audit_sha={W7C_EMISSION_3_AUDIT_SHA}"
        f";element_2_oe_form_status_unchanged=MANDATORY_at_S88plus_plan_freeze"
        f";allowlist_row_appended=True"
        f";instances_row_appended=True"
        f";co_author_connes_dispatched_post_emit_per_tasking_modifier=pending"
    )

    result = emit_verdict(
        gate_id=GATE_ID,
        verdict="PASS",
        value_str=value_str,
        scheme="cross-pillar-bridge-corpus-element-2-extension",
        convention="oe-form-w7c-emission-3-lexical",
        L_max="N/A",
        input_pin_map=input_pin_map,
        content_target=CORPUS,
    )
    print(json.dumps({
        "gate_id": result["gate_id"],
        "verdict": result["verdict"],
        "audit_sha256": result["audit_sha256"],
        "content_sha256": result["content_sha256"],
        "post_edit_check": post_edit_check,
        "regex_check": {
            "match_PASS": regex_check["match_PASS"],
            "match_object_str": regex_check["match_object_str"],
        },
    }, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
