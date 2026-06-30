#!/usr/bin/env python3
"""S90 W1-14 — Deferred-pending rule-file enforcement clause extension.

Per `sessions/session-plan/session-90-plan-w1.md` §W1-14.

This script performs the artifact-existence verification + 3 atomic appends
for the S90 W1-14 METHODOLOGY-class landing:

  1. Verifies that orchestrator-direct-edits of:
       - `.claude/rules/cross-pillar-bridge-anatomy.md §"Level-2 sub-class"`
       - `computations/_shared/_cross_pillar_bridge_audit.py`
       - `sessions/framework/registry/cross-pillar-bridge-corpus.md §1`
     have all landed with required markers.
  2. Runs the self-test driver `s90_w1_deferred_pending_audit_test.py`
     (T1+T2+T3 positive, T4 negative; all 4 must PASS).
  3. Appends W1-14 row to `methodology-wave-allowlist.md`.
  4. Appends W1-14 rationale to `methodology-wave-instances.md`.
  5. Emits canonical verdict line + dual-SHA companion row at
     `computations/session-90/s90_gate_verdicts.txt`.

Per `wave-classification.md §"Dual-SHA closure for METHODOLOGY-class"`:
  - audit_sha256 = SHA-256 over JSON-serialized input-pin map (sorted keys).
  - content_sha256 = SHA-256 over post-edit `cross-pillar-bridge-anatomy.md`
    (the primary rule-file diff target).
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "computations" / "_shared"))

from canonical_constants import *  # noqa: F401,F403 — canonical-constants discipline
from s90_w1_emit_verdict import emit_verdict, sha256_of_file


# --- Paths ---
ANATOMY = ROOT / ".claude" / "rules" / "cross-pillar-bridge-anatomy.md"
AUDIT_SCRIPT = ROOT / "computations" / "_shared" / "_cross_pillar_bridge_audit.py"
CORPUS = ROOT / "sessions" / "framework" / "registry" / "cross-pillar-bridge-corpus.md"
INSTANCES = ROOT / "sessions" / "framework" / "registry" / "methodology-wave-instances.md"
ALLOWLIST = ROOT / ".claude" / "rules" / "methodology-wave-allowlist.md"
SUBSTRATE_FIRST_RULE = ROOT / ".claude" / "rules" / "substrate-first-canonical-sourcing.md"
TEST_DRIVER = ROOT / "computations" / "_shared" / "s90_w1_deferred_pending_audit_test.py"
PYTHON_VENV = ROOT / "phonon-exflation-sim" / ".venv312" / "Scripts" / "python.exe"


# --- Constants (local — gate identity + pinned SHAs) ---
GATE_ROW = "W1-14"                                                       # (local)
SESSION = "S90"                                                          # (local)
GATE_ID = "S90-DEFERRED-PENDING-RULE-FILE-ENFORCEMENT-CLAUSE-EXTENSION"   # (local)
PLAN_BLOCK_SHA = "aff2bae7b7fe971f7430640651199fca67a60ddad5d9a91a3daab6442227a805"  # (local)

# Pre-edit input-pin SHAs (pinned by orchestrator at dispatch — see plan §W1-14 #7)
ANATOMY_PRE_EDIT_SHA = "0d6673941ced8df1b44f2e5b05fd012fbb72d32593b14ae6021ac6b95f7680cd"  # (local)
AUDIT_SCRIPT_PRE_EDIT_SHA = "490dd8818830a46d4cc78b31bd6e01b649699068db02dca9b4af9254719886ad"  # (local)
CORPUS_PRE_EDIT_SHA = "e1b3e891847b43fd253e584501f5e13745daca2ac31ae4941ed76842d375f4ee"  # (local) — post-W1-13
INSTANCES_PRE_EDIT_SHA = "5792bd28c0cbb281d6149d2ed4c9c697b2a4f7a7ed3d9a5d5c5c12e66b051565"  # (local) — pre-W1-14, post-connes-co-sign-append for W1-13
ALLOWLIST_PRE_EDIT_SHA = "3a61401c01330998c44db766cb622618237adcd7283fb3e9e39b8b82f19ab1e5"  # (local) — post-W1-13
SUBSTRATE_FIRST_RULE_SHA = "0e21abb4fa64184799c98784103221ba96d648b1d500337566e2030ed59763f3"  # (local)

# Regex pattern pins (Element-2 OE-form related; this gate's audit-extension reuses these for cross-link)
PATTERN_PROXY_REFINEMENT = "REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT"  # (local)
PATTERN_FIRST_EXTRACTION = "REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION"  # (local)

# K-counter pins
K_BEFORE = 0                                                              # (local) — pre-W1-14: no deferred-pending discipline
K_AFTER = 1                                                               # (local) — post-W1-14: K=1 (dual instances same landing event)
K_PROMOTION = 3                                                           # (local) per feedback_rules-compensate-missing-structure.md

# Calibration instance pins
CALIBRATION_INSTANCE_PROXY = "§VII.AV (FWD-C2 Pillar III/IV ↔ Pillar V; Casimir-bound proxy pending FULL BdG)"  # (local)
CALIBRATION_INSTANCE_FIRST = "§VII.AU (FWD-C1 Pillar I-II; parameterized slope_A canonical pending L_max scan)"  # (local)

# Post-edit markers required by plan §W1-14 #9 PASS criterion (i)-(vi)
REQUIRED_ANATOMY_MARKERS = [                                              # (local)
    "Deferred-pending intermediate verdict-class (S90 W-6 CF-W5-6 / W-6 CF-1 landing)",
    "REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT",
    "REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION",
    "Calibration corpus instance**: §VII.AV",
    "Calibration corpus instance**: §VII.AU",
    "Status**: SUGGESTION at K=1",
    "Audit-script extension**",
    "PATTERN_PROXY_REFINEMENT",
    "PATTERN_FIRST_EXTRACTION",
]

REQUIRED_AUDIT_SCRIPT_MARKERS = [                                         # (local)
    "Deferred-pending intermediate verdict-class detectors (S90 W1-14 landing)",
    "PATTERN_PROXY_REFINEMENT = re.compile(",
    "PATTERN_FIRST_EXTRACTION = re.compile(",
    "def detect_deferred_pending_sub_class(",
    "REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT",
    "REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION",
]

REQUIRED_CORPUS_MARKERS = [                                               # (local)
    "Instance #3 (deferred-pending; dual sub-class S90 W1-14 landing)",
    "(a) §VII.AV PROXY-REFINEMENT",
    "(b) §VII.AU FIRST-EXTRACTION",
    "detect_deferred_pending_sub_class(section_text, section_anchor)",
    "s90_w1_deferred_pending_audit_test.py",
]


# --- Build-content blocks (allowlist row + instances rationale) ---

ALLOWLIST_ROW = f"| {GATE_ROW} | {SESSION} | {PLAN_BLOCK_SHA} |\n"

INSTANCES_RATIONALE_TEMPLATE = """
### {gate_row} ({session}) — {plan_block_sha}

**Provenance**: gate-ID `{gate_id}`
(CF-W5-6 / W-6 CF-1; S90 W-6 atomic deliverables); agent
`gen-physicist orchestrator-direct-write` per
`wave-classification.md §"Dispatch consequences"`; plan reference
`sessions/session-plan/session-90-plan-w1.md` §W1-14 lines 927-1004; plan-block
sha256 `{plan_block_sha}` (7731 chars, 78 lines).

**Gate classification (M1∧M2∧M3∧M4 conjunction)**:
- **M1**: artifact-existence-with-substantive-content per `wave-classification.md §M1`.
  PASS predicate = (i) deferred-pending sub-section appended to
  `cross-pillar-bridge-anatomy.md §"Level-2 sub-class (binding vs non-binding)"`
  (≥30 substantive lines; actual ~85 lines); (ii) TWO sub-class tags defined
  (`REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT` + `REGISTRY-INCOMPLETE-
  PENDING-FIRST-EXTRACTION`); (iii) audit-script extension lands with 2 regex
  detectors (`PATTERN_PROXY_REFINEMENT` + `PATTERN_FIRST_EXTRACTION`) +
  `detect_deferred_pending_sub_class()` function; (iv) corpus §1 calibration
  Instance #3 (dual sub-class) appended; (v) allowlist + instances rows
  appended; (vi) dual-SHA closure emitted. No numerical comparison; all
  conditions are artifact-existence + content-substance + self-test PASS.
- **M2**: producing operations restricted to Edit/Write on rule-files +
  registry files + audit-script + self-test driver + canonical
  `s90_w1_emit_verdict.py` helper. No numerical comparisons against pre-
  registered thresholds; the only Python-execution step is the 4-test
  self-test driver (T1 PROXY-only + T2 FIRST-EXTRACTION-only + T3 BOTH +
  T4 negative-baseline) whose PASS predicate is binary-boolean assertion
  (deferred_pending field + sub_class string + severity field).
- **M3**: verbatim sub-diff from plan §W1-14 #6 dispatch prompt (the
  deferred-pending sub-section text, the 2 sub-class tag definitions,
  and the 2 audit-script regex patterns are all verbatim from the plan).
  Calibration instance bindings (§VII.AV PROXY-REFINEMENT + §VII.AU
  FIRST-EXTRACTION) are verbatim from plan §W1-14 #6 dispatch prompt and
  cross-reference S89 W-6 R2 workshop closeout per partition manifest
  `s89-w6-level2-binding-inheritance.md §Wrap-Up`. No first-principles
  new derivation.
- **M4**: row landing per `methodology-wave-allowlist.md §"Edit discipline"`
  orchestrator-only-edit protocol.

**Sub-clause structure landed**:
1. New sub-section `#### Deferred-pending intermediate verdict-class
   (S90 W-6 CF-W5-6 / W-6 CF-1 landing)` appended to
   `.claude/rules/cross-pillar-bridge-anatomy.md` between the existing
   `**Enforcement**:` paragraph bullets (lines 41-44 pre-edit) and the
   `### Level 3 — Empirical Anchor at Canonical L_max` heading (line 46
   pre-edit). Heading depth `####` matches sibling sub-sections
   (`#### Level-2 audit axes (Level-2-A vs Level-2-B)` and `#### Level-2
   sub-class (binding vs non-binding)`). Sub-section length ~85 lines
   substantive content + provenance header + 2 bullet definitions +
   3-point reservation enumeration + direction-of-explanation paragraph
   + status K=1 paragraph + audit-script-extension reference + corpus
   pointer.
2. `_cross_pillar_bridge_audit.py` extension: inserted between
   `audit_element_2_oe_form()` function (line 197 pre-edit) and `# Core
   audit` separator (line 200 pre-edit). Adds: header comment block
   citing parent rule + 2 regex pattern constants (`PATTERN_PROXY_REFINEMENT`,
   `PATTERN_FIRST_EXTRACTION`) + helper function
   `detect_deferred_pending_sub_class(section_text, section_anchor)`
   returning structured diagnostic dict with `deferred_pending` bool +
   `sub_class` string + `severity` string + count fields + diagnostic
   string. Detector emits S2 advisory severity only; does NOT route to
   plan-freeze HARD-HALT per plan §W1-14 #6 specification.
3. `s90_w1_deferred_pending_audit_test.py` (NEW; ~200 lines): self-test
   driver with 4 fixtures (FIXTURE_PROXY_ONLY emulating §VII.AV post-CF-63
   shape; FIXTURE_FIRST_EXTRACTION_ONLY emulating §VII.AU post-CF-63 shape;
   FIXTURE_BOTH testing edge-case dual-axis bridge; FIXTURE_NEGATIVE_BASELINE
   emulating W-5 §VII.AF.1 baseline with no deferred-pending tags). 4 tests
   (T1+T2+T3 positive variants + T4 negative); all 4 PASS at S90 W1-14
   close 2026-05-13 (run output: `T1 PROXY-REFINEMENT only: PASS`, `T2
   FIRST-EXTRACTION only: PASS`, `T3 BOTH: PASS`, `T4 negative baseline:
   PASS`).
4. Corpus §1 "Level-2 Layer Distinction calibration" extended with
   Instance #3 (deferred-pending; dual sub-class S90 W1-14 landing).
   Instance #3 documents BOTH calibration sub-instances: (a) §VII.AV
   PROXY-REFINEMENT + (b) §VII.AU FIRST-EXTRACTION. Pre-existing instances
   #1 (positive W-5 §VII.AF.1) + #2 (hypothetical negative counter-example)
   are preserved; Instance #3 is appended below Instance #2 and above the
   `### Audit-script extension queue` subsection.

**Closure conditions**: PASS verdict per pre-registered #9 (i)-(vi) — six
operational conditions satisfied (sub-section, 2 sub-class tags, audit-script
2 regex detectors + helper function, corpus Instance #3, allowlist +
instances rows). audit_sha256 over input-pin map (plan_block_sha + 5 file
pre-edit SHAs + 2 regex patterns + K-counter status + calibration instance
labels + self-test results). content_sha256 over post-edit
`cross-pillar-bridge-anatomy.md` (the primary rule-file diff target). Self-
test driver T1+T2+T3+T4 all PASS at landing.

**Cross-link**: `sessions/session-plan/session-90-plan-w1.md` §W1-14 (plan
reference, 7731-char block, sha256=`{plan_block_sha}`);
`.claude/rules/cross-pillar-bridge-anatomy.md §"Level-2 sub-class (binding
vs non-binding)" §"Deferred-pending intermediate verdict-class"` (rule-file
diff target; pre-edit sha256=`{anatomy_pre_edit_sha}`);
`computations/_shared/_cross_pillar_bridge_audit.py` (audit-script extension
with PATTERN_PROXY_REFINEMENT + PATTERN_FIRST_EXTRACTION +
`detect_deferred_pending_sub_class()` function; pre-edit sha256=
`{audit_script_pre_edit_sha}`); `computations/_shared/s90_w1_deferred_pending_audit_test.py`
(self-test driver, T1+T2+T3+T4 PASS at landing);
`sessions/framework/registry/cross-pillar-bridge-corpus.md §1`
"Level-2 Layer Distinction calibration" Instance #3 (corpus row #3;
pre-edit sha256=`{corpus_pre_edit_sha}`); `.claude/rules/substrate-first-
canonical-sourcing.md §(iv)` MANDATORY at K=4 (cross-link for Level-2 binding
axis; sha256=`{substrate_first_rule_sha}`); `feedback_rules-compensate-missing-structure.md`
(K-counter SUGGESTION → MANDATORY at K=3 threshold); `.claude/rules/wave-
classification.md §"Dual-SHA closure for METHODOLOGY-class"` (audit_sha256
over input-pin map + content_sha256 over post-edit rule-file diff target).

**Carry-forward (3 substantive items)**:
1. **K=3 promotion** (forward): when 2 additional distinct calibration
   instances land for the deferred-pending sub-class (provenance-distinct
   from the §VII.AV + §VII.AU dual-instance shared-landing event),
   `detect_deferred_pending_sub_class()` severity tag in
   cross-pillar-bridge-anatomy.md status migrates from "SUGGESTION at K=1"
   to "MANDATORY at K=3" and the audit fires at S1 HARD-HALT instead of
   S2 advisory.
2. **CF-63 W6 §VII.AV + §VII.AU registry-entry landing** (REQUIRED-FOR-
   downstream): mack writer per `feedback_mack-bridge-role.md` lands
   §VII.AV.OP-PROJ + §VII.AU.OP-PROJ registry entries with the deferred-
   pending sub-class tags in S90 W6. Until those entries land, the audit-
   script's `detect_deferred_pending_sub_class()` has no live §VII targets
   (only synthetic-fixture test cases). CF-14 is a prerequisite of CF-63
   (the sub-class tags must be defined as routing targets before W6 can
   cite them); CF-15 retrofits §VII.AU into the deferred-pending taxonomy
   via Option A SUPERSEDES protocol per plan §W1-15.
3. **Audit-script integration with plan-freeze auditor** (forward,
   NOT discharged here): future plan-freeze run of
   `_cross_pillar_bridge_audit.py` against `permanent-results-registry.md`
   should invoke `detect_deferred_pending_sub_class()` on each §VII section
   alongside the existing `audit_element_2_oe_form()` check. The audit
   pipeline composition order at `epistemic-discipline.md §"PRU pipeline
   composition order"` admits this extension at the PRDR / gate-execution
   layer. Integration is queued for next-session plan-freeze auditor
   refinement.

**Parallel-review dispatch**: not applicable per --tasking "as applicable"
clause (plan §W1-14 #4 names no CO-AUTHOR; gen-physicist orchestrator-
direct-write is the sole agent).

**Substrate framing**: Deferred-pending IS the methodology-layer F-image
of substrate-IS partial information about Level-2 envelope realization, per
`epistemic-discipline.md §"Layer-Decomposition"` `F: substrate → methodology
→ audit`. The substrate's Level-2-binding admissibility predicate IS a
structural identity at the cohomology-class / HKR-image layer (regulator-
invariant, L-independent — Level 1 inheritance); its empirical realization
can be SCHEMATIC (proxy) or symbolic-only (first-extraction-pending). The
two sub-classes preserve the F-image fidelity at the methodology layer
while admitting structurally-intermediate realization at the audit layer.
The substrate-IS predicate `Level-2-binding(envelope) := ∃ HKR-image
c_continuum on partner pillar : c_continuum = HKR(c_L)` is unchanged; the
deferred-pending sub-classes tag entries whose `c_continuum` realization is
pending refinement (PROXY) or pending first extraction (FIRST-EXTRACTION).
Container-thinking violation FORBIDDEN: "the deferred-pending status IS
the registry entry" — inverted: "the substrate's Level-2-binding identity
IS the structural anchor; the deferred-pending tag is the methodology
F-image documenting the empirical-realization completion state".
Direction of explanation: substrate-IS Level-2-binding predicate → emergent
Level-2 envelope realization (SCHEMATIC / symbolic-only / FULL) →
methodology-layer deferred-pending tag at the audit boundary.
"""


# --- Verification + emission ---

def verify_post_edit_anatomy() -> dict:
    """Verify the deferred-pending sub-section is present in post-edit anatomy rule."""
    text = ANATOMY.read_text(encoding="utf-8")
    missing = [m for m in REQUIRED_ANATOMY_MARKERS if m not in text]
    return {
        "all_markers_present": len(missing) == 0,
        "missing": missing,
        "markers_checked": len(REQUIRED_ANATOMY_MARKERS),
        "markers_found": len(REQUIRED_ANATOMY_MARKERS) - len(missing),
    }


def verify_post_edit_audit_script() -> dict:
    """Verify the deferred-pending detectors are present in post-edit audit script."""
    text = AUDIT_SCRIPT.read_text(encoding="utf-8")
    missing = [m for m in REQUIRED_AUDIT_SCRIPT_MARKERS if m not in text]
    return {
        "all_markers_present": len(missing) == 0,
        "missing": missing,
        "markers_checked": len(REQUIRED_AUDIT_SCRIPT_MARKERS),
        "markers_found": len(REQUIRED_AUDIT_SCRIPT_MARKERS) - len(missing),
    }


def verify_post_edit_corpus() -> dict:
    """Verify the §1 Instance #3 is present in post-edit corpus."""
    text = CORPUS.read_text(encoding="utf-8")
    missing = [m for m in REQUIRED_CORPUS_MARKERS if m not in text]
    return {
        "all_markers_present": len(missing) == 0,
        "missing": missing,
        "markers_checked": len(REQUIRED_CORPUS_MARKERS),
        "markers_found": len(REQUIRED_CORPUS_MARKERS) - len(missing),
    }


def run_self_test_driver() -> dict:
    """Run the self-test driver and confirm all 4 tests PASS."""
    result = subprocess.run(
        [str(PYTHON_VENV), str(TEST_DRIVER)],
        capture_output=True,
        text=True,
        encoding="utf-8",
        timeout=60,
    )
    return {
        "returncode": result.returncode,
        "all_tests_pass": result.returncode == 0,
        "stdout_tail": result.stdout[-500:] if result.stdout else "",
        "stderr_tail": result.stderr[-500:] if result.stderr else "",
    }


def build_input_pin_map(
    anatomy_check: dict,
    audit_script_check: dict,
    corpus_check: dict,
    self_test: dict,
) -> dict:
    """Construct ordered input-pin map for audit_sha256 computation."""
    return {
        "gate_id": GATE_ID,
        "plan_block_sha": PLAN_BLOCK_SHA,
        "anatomy_pre_edit_sha": ANATOMY_PRE_EDIT_SHA,
        "audit_script_pre_edit_sha": AUDIT_SCRIPT_PRE_EDIT_SHA,
        "corpus_pre_edit_sha": CORPUS_PRE_EDIT_SHA,
        "instances_pre_edit_sha": INSTANCES_PRE_EDIT_SHA,
        "allowlist_pre_edit_sha": ALLOWLIST_PRE_EDIT_SHA,
        "substrate_first_rule_sha": SUBSTRATE_FIRST_RULE_SHA,
        "pattern_proxy_refinement": PATTERN_PROXY_REFINEMENT,
        "pattern_first_extraction": PATTERN_FIRST_EXTRACTION,
        "K_before": K_BEFORE,
        "K_after": K_AFTER,
        "K_promotion": K_PROMOTION,
        "calibration_instance_proxy": CALIBRATION_INSTANCE_PROXY,
        "calibration_instance_first": CALIBRATION_INSTANCE_FIRST,
        "anatomy_markers_present": anatomy_check["all_markers_present"],
        "audit_script_markers_present": audit_script_check["all_markers_present"],
        "corpus_markers_present": corpus_check["all_markers_present"],
        "self_test_all_pass": self_test["all_tests_pass"],
    }


def main() -> int:
    # Step 1 — Verify post-edit anatomy state
    anatomy_check = verify_post_edit_anatomy()
    if not anatomy_check["all_markers_present"]:
        print(json.dumps({
            "error": "Post-edit anatomy verification FAILED",
            "check": anatomy_check,
        }, indent=2, ensure_ascii=False))
        return 1

    # Step 2 — Verify post-edit audit-script state
    audit_check = verify_post_edit_audit_script()
    if not audit_check["all_markers_present"]:
        print(json.dumps({
            "error": "Post-edit audit-script verification FAILED",
            "check": audit_check,
        }, indent=2, ensure_ascii=False))
        return 1

    # Step 3 — Verify post-edit corpus state
    corpus_check = verify_post_edit_corpus()
    if not corpus_check["all_markers_present"]:
        print(json.dumps({
            "error": "Post-edit corpus verification FAILED",
            "check": corpus_check,
        }, indent=2, ensure_ascii=False))
        return 1

    # Step 4 — Run self-test driver
    self_test = run_self_test_driver()
    if not self_test["all_tests_pass"]:
        print(json.dumps({
            "error": "Self-test driver FAILED",
            "check": self_test,
        }, indent=2, ensure_ascii=False))
        return 1

    # Step 5 — Append allowlist row
    with ALLOWLIST.open("a", encoding="utf-8") as f:
        f.write(ALLOWLIST_ROW)
    print(f"Allowlist row appended: {ALLOWLIST_ROW.strip()}")

    # Step 6 — Append instances rationale
    rationale = INSTANCES_RATIONALE_TEMPLATE.format(
        gate_row=GATE_ROW,
        session=SESSION,
        plan_block_sha=PLAN_BLOCK_SHA,
        gate_id=GATE_ID,
        anatomy_pre_edit_sha=ANATOMY_PRE_EDIT_SHA,
        audit_script_pre_edit_sha=AUDIT_SCRIPT_PRE_EDIT_SHA,
        corpus_pre_edit_sha=CORPUS_PRE_EDIT_SHA,
        substrate_first_rule_sha=SUBSTRATE_FIRST_RULE_SHA,
    )
    with INSTANCES.open("a", encoding="utf-8") as f:
        f.write(rationale)
    print(f"Instances rationale appended: {rationale.count(chr(10))} lines, {len(rationale)} chars")

    # Step 7 — Emit verdict line + dual-SHA companion row
    input_pin_map = build_input_pin_map(anatomy_check, audit_check, corpus_check, self_test)
    value_str = (
        f"deferred-pending-sub-class-landed-with-2-sub-classes_AND_audit-extension_AND_K-1-corpus-dual"
        f";deferred_pending_sub_section_appended_to_enforcement_clause=True"
        f";n_sub_class_tags_defined=2"
        f";audit_script_2_regex_detectors_landed=True"
        f";helper_function_detect_deferred_pending_sub_class_landed=True"
        f";corpus_section_1_instance_3_appended=True"
        f";self_test_T1_T2_T3_T4_all_pass=True"
        f";anatomy_markers_found={anatomy_check['markers_found']}_of_{anatomy_check['markers_checked']}"
        f";audit_script_markers_found={audit_check['markers_found']}_of_{audit_check['markers_checked']}"
        f";corpus_markers_found={corpus_check['markers_found']}_of_{corpus_check['markers_checked']}"
        f";K_advance={K_BEFORE}to{K_AFTER}"
        f";K_promotion_threshold={K_PROMOTION}"
        f";K_status=SUGGESTION-K=1"
        f";calibration_instance_proxy_pin=§VII.AV"
        f";calibration_instance_first_extraction_pin=§VII.AU"
        f";severity_band_S2_advisory_NOT_S1_hard_halt=True"
        f";allowlist_row_appended=True"
        f";instances_row_appended=True"
        f";cf_14_precedes_cf_15_intra_wave=True"
    )

    result = emit_verdict(
        gate_id=GATE_ID,
        verdict="PASS",
        value_str=value_str,
        scheme="cross-pillar-bridge-anatomy-enforcement-clause-extension",
        convention="deferred-pending-proxy-refinement-first-extraction",
        L_max="N/A",
        input_pin_map=input_pin_map,
        content_target=ANATOMY,
    )
    print(json.dumps({
        "gate_id": result["gate_id"],
        "verdict": result["verdict"],
        "audit_sha256": result["audit_sha256"],
        "content_sha256": result["content_sha256"],
        "anatomy_check": anatomy_check,
        "audit_script_check": audit_check,
        "corpus_check": corpus_check,
        "self_test": {k: v for k, v in self_test.items() if k != "stdout_tail" and k != "stderr_tail"},
    }, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
