#!/usr/bin/env python3
"""S90 W1-15 — FWD-C1 convention-tag retrofit via Option A SUPERSEDES protocol.

Per `sessions/session-plan/session-90-plan-w1.md` §W1-15 (CF-15, W-6 CF-4).

This script performs the artifact-existence verification + Option A SUPERSEDES
verdict-line emission for the S90 W1-15 METHODOLOGY-class landing:

  1. Verifies the post-edit registry state has the deferred-pending re-tag
     annotation on §VII.AU.OP-PROJ.
  2. Verifies the post-edit S89 W5 WP §W5-6 has the retrofit disclosure
     paragraph appended.
  3. Verifies CF-14 PASS prereq (deferred-pending sub-class taxonomy must be
     defined before CF-15 can route §VII.AU into it).
  4. Appends W1-15 row to `methodology-wave-allowlist.md`.
  5. Appends W1-15 rationale to `methodology-wave-instances.md`.
  6. Emits corrective canonical verdict line + dual-SHA companion row at
     `computations/session-90/s90_gate_verdicts.txt` per Option A SUPERSEDES
     protocol of `gate-verdicts.md §"Option A — sig_5 remediation pathway
     under absolute verdict permanence"`:
       - GATE_ID: `S89-W5-6-FWD-C1-RETRY-PARAMETERIZED-SLOPE-A-CANONICAL-RETROFIT`
       - composite verdict: INFO (same as §W5-6 original — DO NOT alter
         scientific verdict)
       - convention: `lizzi-fwd-c1-retry-parameterized-slope-A-canonical-
         TEMPLATE-INHERITED-FROM-W-5` (NEW suffix indicating substrate-IS
         Element-1 inheritance from §VII.AF.1.OP-PROJ W-5 calibration baseline)
       - supersedes: `273efb4b4e24e07bc372812cd53537a95afef9d268e41590109966ee5284cc67`
         (full 64-char original §W5-6 audit_sha256 at `s89_gate_verdicts.txt:122`)
       - audit_sha256: NEW (recomputed under new convention tag + new input-pin map)
       - content_sha256: post-edit `permanent-results-registry.md` (rule-file
         diff target where §VII.AU was re-tagged)

Per `wave-classification.md §"Dual-SHA closure for METHODOLOGY-class"`:
  - audit_sha256 = SHA-256 over JSON-serialized input-pin map (sorted keys).
  - content_sha256 = SHA-256 over post-edit registry (the primary diff target).

CF-15 PRECEDES CF-65 first-extraction gate; CF-15 REQUIRES CF-14 PASS.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "computations" / "_shared"))

from canonical_constants import *  # noqa: F401,F403 — canonical-constants discipline
from s90_w1_emit_verdict import emit_verdict, sha256_of_file


# --- Paths ---
REGISTRY = ROOT / "sessions" / "permanent-results-registry.md"
S89_W5_WP = ROOT / "sessions" / "session-89" / "session-89-w5-workingpaper.md"
ANATOMY = ROOT / ".claude" / "rules" / "cross-pillar-bridge-anatomy.md"
SUBSTRATE_FIRST_RULE = ROOT / ".claude" / "rules" / "substrate-first-canonical-sourcing.md"
V3_CLOSURE_RECOVERY = ROOT / ".claude" / "rules" / "v3-closure-recovery.md"
INSTANCES = ROOT / "sessions" / "framework" / "registry" / "methodology-wave-instances.md"
ALLOWLIST = ROOT / ".claude" / "rules" / "methodology-wave-allowlist.md"
S89_GATE_VERDICTS = ROOT / "computations" / "session-89" / "s89_gate_verdicts.txt"


# --- Constants (local — gate identity + pinned SHAs) ---
GATE_ROW = "W1-15"                                                       # (local)
SESSION = "S90"                                                          # (local)
GATE_ID = "S89-W5-6-FWD-C1-RETRY-PARAMETERIZED-SLOPE-A-CANONICAL-RETROFIT"  # (local)
PLAN_BLOCK_SHA = "49dd996b36dbbc97cf1de2a45a93131c9f99ee60cef3dc6a5150249a9e921afe"  # (local)

# Pre-edit + post-edit SHAs
ANATOMY_POST_W1_14_SHA = "a38ef420b50bae0abcc8dca4412c568a6aa13a3760f8443aa837a25e9c482347"  # (local)
SUBSTRATE_FIRST_RULE_SHA = "0e21abb4fa64184799c98784103221ba96d648b1d500337566e2030ed59763f3"  # (local)
V3_CLOSURE_RECOVERY_SHA = "ac847cf1db1e7e1fd7d93fd8384e228bc9c120c4baad420d1565701edd57ff1c"  # (local)
REGISTRY_PRE_W1_15_SHA = "0df0c18a59389eeaf4a1b4e171dd43ae224a131258c813e62bcc7f333c52d6c6"  # (local)
S89_W5_WP_PRE_W1_15_SHA = "3e3bcd51a35ca86b065eadd12859fcace9242f2e58ff3f40f129e287efee8177"  # (local)
ALLOWLIST_POST_W1_14_SHA = "4b2f084fc0d04d3e7bf74f655465d71245350cc8ee60fa7d3ef44f02565cf1bd"  # (local)
INSTANCES_POST_W1_14_SHA = "9cca19b84ba071458415807db136a37cc98de84d52c9fde84ebb321a90162c65"  # (local)

# Original §W5-6 verdict line content (verbatim from s89_gate_verdicts.txt:122)
ORIGINAL_GATE_ID = "S89-FWD-C1-RETRY-PARAMETERIZED-SLOPE-A-CANONICAL"     # (local)
ORIGINAL_AUDIT_SHA = "273efb4b4e24e07bc372812cd53537a95afef9d268e41590109966ee5284cc67"  # (local) — SUPERSEDES target
ORIGINAL_CONTENT_SHA = "3ce49a8114604236e7cdeb19df8cd81a4b0e91bb7db9b46b238f75521a9df96e"  # (local)
ORIGINAL_VERDICT = "INFO"                                                 # (local) — preserved
ORIGINAL_VALUE_FIELD = (                                                  # (local)
    "c_sub_corrected=2.238000;c_sub_ratio=1.000000;n_s_recomputed=0.956100;"
    "n_s_FW_match=1;planck_sigma=2.0952;slope_A_paramet=10.1224;hit_PASS=1;"
    "slot=§VII.AU;stage=STAGE-1-CANDIDATE;sign=N/A;mag=INFO;reg=VALID"
)
ORIGINAL_SCHEME = "zeta-zeta-spectral-action"                             # (local) — preserved
ORIGINAL_CONVENTION = "lizzi-fwd-c1-retry-parameterized-slope-A-canonical"  # (local) — base
ORIGINAL_L_MAX = "10"                                                     # (local) — preserved

# NEW convention tag suffix
CONVENTION_SUFFIX = "-TEMPLATE-INHERITED-FROM-W-5"                        # (local)
NEW_CONVENTION = ORIGINAL_CONVENTION + CONVENTION_SUFFIX                  # (local)

# Sub-class tag (post-CF-14 deferred-pending taxonomy routing target)
SUB_CLASS_TAG = "REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION"            # (local)

# CF-14 prereq pin (must have landed PASS for CF-15 to proceed)
CF_14_AUDIT_SHA = "b42d6b8cfe44da13e2c709fb7bedf4f1dc65600799b1dd57e42d604aec1de939"  # (local)

# Post-edit markers required by plan §W1-15 #9 PASS criterion (i)-(iv)
REQUIRED_REGISTRY_MARKERS = [                                             # (local)
    "S90 W1-15 deferred-pending re-tag (2026-05-13)",
    "REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION",
    "S89-W5-6-FWD-C1-RETRY-PARAMETERIZED-SLOPE-A-CANONICAL-RETROFIT",
    "supersedes=`273efb4b4e24e07bc372812cd53537a95afef9d268e41590109966ee5284cc67`",
    "-TEMPLATE-INHERITED-FROM-W-5",
]

REQUIRED_S89_W5_WP_MARKERS = [                                            # (local)
    "**S90 W1-15 retrofit disclosure (2026-05-13)**",
    "-TEMPLATE-INHERITED-FROM-W-5",
    "REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION",
    "supersedes=`273efb4b4e24e07bc372812cd53537a95afef9d268e41590109966ee5284cc67`",
    "substrate physics is UNCHANGED",
]


# --- Build-content blocks ---

ALLOWLIST_ROW = f"| {GATE_ROW} | {SESSION} | {PLAN_BLOCK_SHA} |\n"

INSTANCES_RATIONALE_TEMPLATE = """
### __GATE_ROW__ (__SESSION__) — __PLAN_BLOCK_SHA__

**Provenance**: gate-ID `__GATE_ID__` (CF-15 / W-6 CF-4; S90 W-6 atomic deliverables); agent `gen-physicist orchestrator-direct-write` per `wave-classification.md §"Dispatch consequences"`; plan reference `sessions/session-plan/session-90-plan-w1.md` §W1-15 lines 1006-1078; plan-block sha256 `__PLAN_BLOCK_SHA__` (6738 chars, 73 lines).

**Gate classification (M1∧M2∧M3∧M4 conjunction)**:
- **M1**: artifact-existence-with-substantive-content per `wave-classification.md §M1`. PASS predicate = (i) corrective canonical verdict line appended at `s90_gate_verdicts.txt` with `supersedes=<full-64-char-original-audit_sha256>` per Option A protocol; (ii) §W5-6 WP retrofit disclosure paragraph appended (bold-header subsection `**S90 W1-15 retrofit disclosure (2026-05-13)**` at end of §W5-6, before §W5-7 separator); (iii) §VII.AU.OP-PROJ registry text re-tagged with `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION` sub-class tag (annotation paragraph + header line update); (iv) allowlist + instances rows appended. No numerical comparison; all conditions are artifact-existence + verdict-line content-substance + audit-trail integrity verification.
- **M2**: producing operations restricted to Edit/Write on rule-files + registry + S89 W5 WP + canonical `s90_w1_emit_verdict.py` helper. No numerical comparisons against pre-registered thresholds; the only Python-execution is marker-presence assertions + canonical verdict-line emission. Substrate physics is PRESERVED (composite INFO unchanged; c_sub_corrected=2.238 EXACT, n_s_FW=0.9561, Planck σ=2.0952 by design).
- **M3**: verbatim sub-diff from plan §W1-15 #6 dispatch prompt (convention-tag suffix `-TEMPLATE-INHERITED-FROM-W-5`, sub-class tag `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION`, Option A supersedes-tag form, disclosure-paragraph content all verbatim from plan). The §W5-6 original verdict line is verbatim source from `s89_gate_verdicts.txt:122`. No first-principles new derivation.
- **M4**: row landing per `methodology-wave-allowlist.md §"Edit discipline"` orchestrator-only-edit protocol.

**Sub-clause structure landed**:
1. Corrective canonical verdict line at `computations/session-90/s90_gate_verdicts.txt`: `S89-W5-6-FWD-C1-RETRY-PARAMETERIZED-SLOPE-A-CANONICAL-RETROFIT: INFO -- value='__ORIGINAL_VALUE__...;supersedes=__ORIGINAL_AUDIT_SHA__' scheme=zeta-zeta-spectral-action convention=lizzi-fwd-c1-retry-parameterized-slope-A-canonical-TEMPLATE-INHERITED-FROM-W-5 L_max=10 audit_sha256=<NEW> content_sha256=<post-edit-registry-SHA> schema_version=S87+`. Per Option A absolute verdict permanence: original `S89-FWD-C1-RETRY-PARAMETERIZED-SLOPE-A-CANONICAL: INFO` line at `s89_gate_verdicts.txt:122` is RETAINED on disk; corrective line APPENDS to S90 verdict file; downstream consumers follow the supersedes chain to find the latest non-superseded line per `gate-verdicts.md §"Option A"` item 3.
2. §W5-6 retrofit disclosure paragraph appended at `sessions/archive/session-89/session-89-w5-workingpaper.md` line ~1811 (immediately before the `---` separator and §W5-7 header at line 1815): bold-header subsection `**S90 W1-15 retrofit disclosure (2026-05-13)**` documenting (a) the convention-tag suffix's substrate-IS Element-1 inheritance lineage from §VII.AF.1.OP-PROJ W-5 baseline; (b) the sub-class re-tag routing into REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION; (c) the Option A SUPERSEDES protocol citation with full 64-char original audit_sha256; (d) the substrate-physics-preserved assertion (composite INFO unchanged); (e) the substrate framing direction-of-explanation paragraph; (f) the container-thinking violation FORBIDDEN clause.
3. §VII.AU.OP-PROJ registry text re-tagged at `sessions/permanent-results-registry.md` line 17250 area: (i) section header line 17250 updated to include `; S90 W1-15 deferred-pending re-tag REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION`; (ii) new annotation paragraph `**S90 W1-15 deferred-pending re-tag (2026-05-13)**` inserted between the S89 W7c LANDING paragraph and the STRUCTURE tag paragraph, citing CF-14 audit_sha256, the audit-script detector function, the Option A supersedes protocol, and the substrate-physics-preserved assertion.

**Closure conditions**: PASS verdict per pre-registered #9 (i)-(iv) — four operational conditions satisfied (verdict line + supersedes; WP disclosure paragraph; registry re-tag annotation + header update; allowlist + instances rows). audit_sha256 over input-pin map (plan_block_sha + 7 file SHAs + original audit_sha + sub-class tag + CF-14 prereq pin). content_sha256 over post-edit `permanent-results-registry.md` (primary rule-file diff target; the §VII.AU re-tag is the structurally-load-bearing change). CF-14 PASS prereq verified at audit_sha256 `__CF_14_AUDIT_SHA__`. Verdict permanence absolute: original §W5-6 INFO verdict at `s89_gate_verdicts.txt:122` is RETAINED on disk; the corrective line is an APPEND-only addition to S90 verdict file.

**Cross-link**: `sessions/session-plan/session-90-plan-w1.md` §W1-15 (plan reference, 6738-char block, sha256=`__PLAN_BLOCK_SHA__`); `.claude/rules/cross-pillar-bridge-anatomy.md §"Level-2 sub-class (binding vs non-binding)" §"Deferred-pending intermediate verdict-class (S90 W-6 CF-W5-6 / W-6 CF-1 landing)"` POST-CF-14 (sub-class taxonomy routing target; CF-14 landed at audit_sha256=`__CF_14_AUDIT_SHA__`); `.claude/rules/substrate-first-canonical-sourcing.md §(iv)` MANDATORY at K=4 (SCHEMATIC vs FULL level-pin discipline; sha256=`__SUBSTRATE_FIRST_RULE_SHA__`); `.claude/rules/v3-closure-recovery.md §"Stage 1: Automatic re-dispatch"` sig_5 sub-section (Option A SUPERSEDES protocol companion; sha256=`__V3_CLOSURE_RECOVERY_SHA__`); `.claude/rules/gate-verdicts.md §"Option A — sig_5 remediation pathway under absolute verdict permanence"` (Option A unified policy text; S88 W8-100 user adjudication); `sessions/permanent-results-registry.md §VII.AU.OP-PROJ` post-W1-15 (deferred-pending re-tag; pre-edit sha256=`__REGISTRY_PRE_W1_15_SHA__`); `sessions/archive/session-89/session-89-w5-workingpaper.md §W5-6` (disclosure paragraph appended; pre-edit sha256=`__S89_W5_WP_PRE_W1_15_SHA__`); `computations/session-89/s89_gate_verdicts.txt:122` (original §W5-6 verdict line; gate-ID `S89-FWD-C1-RETRY-PARAMETERIZED-SLOPE-A-CANONICAL` INFO; original audit_sha256=`__ORIGINAL_AUDIT_SHA__`); `feedback_mack-bridge-role.md` (mack-cosmic-bridge sole-writer for §VII.AU registry text — but this is a methodology re-tag annotation, NOT a substrate-physics edit, so orchestrator-direct-write per `wave-classification.md §"Dispatch consequences"` applies); `.claude/rules/wave-classification.md §"Dual-SHA closure for METHODOLOGY-class"` (audit_sha256 over input-pin map + content_sha256 over post-edit registry).

**Carry-forward (3 substantive items)**:
1. **CF-65 W6 first-extraction gate** (REQUIRED-FOR-FIRST-EXTRACTION-COMPLETION): `S90-FWD-C1-LMAX-SCAN-PARAMETERIZED-SLOPE-A-CANONICAL-WITH-PROMOTION-SEMANTICS` (W-6 CF-3) is the first-extraction gate for §VII.AU.OP-PROJ. Upon CF-65 PASS, the §VII.AU entry can be re-tagged from `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION` to plain Level-2-binding ELIGIBLE (registry-PASS eligible per `cross-pillar-bridge-anatomy.md §"Registry-PASS criterion"`).
2. **Stage-2 cross-axis independent-verify** (`joint-theorem-promotion.md` 4-stage pathway Stage 2 of 4): `S90-FWD-C1-STAGE-2-INDEPENDENT-VERIFY` carry-forward already pre-registered at §VII.AU.OP-PROJ entry's Provenance paragraph (Stage 2 = two cross-reviewers on opposite axes per `joint-theorem-promotion.md §"Stage 2"`; spectral-functional side DIFFERENT from lizzi; transit / cosmological-bridge side mack-cosmic-bridge admissible per Axis-B Selection Protocol). Stage-2 PASS-AND on joint clauses promotes §VII.AU.OP-PROJ from STAGE-1-CANDIDATE to STAGE-3-PERMANENT.
3. **Audit-trail supersession chain consumer adoption** (forward, NOT discharged here): downstream consumers (orchestrators, audit scripts, `/weave --update`, `_consolidate_intake.py`) MUST adopt the Option A supersession-chain reading discipline per `gate-verdicts.md §"Option A"` item 3 for FWD-C1 §W5-6 verdict consumption: scan all canonical lines for gate-ID matching `S89-FWD-C1-RETRY-PARAMETERIZED-SLOPE-A-CANONICAL*` (both original + retrofit), identify the `supersedes=` chain, treat the latest non-superseded line as canonical. The latest canonical for FWD-C1 §W5-6 is now the W1-15 retrofit INFO line; the original §W5-6 INFO at `s89_gate_verdicts.txt:122` is superseded but RETAINED on disk for audit-trail integrity.

**Parallel-review dispatch**: not applicable per --tasking "as applicable" clause (plan §W1-15 #4 names no CO-AUTHOR; gen-physicist orchestrator-direct-write is the sole agent).

**Substrate framing**: TEMPLATE-INHERITED convention-tag suffix IS the methodology F-image of substrate-IS Element-1 inheritance from W-5 calibration baseline, per `epistemic-discipline.md §"Layer-Decomposition"` `F: substrate → methodology → audit`. The substrate's Element-1 specification template (W-5 §VII.AF.1.OP-PROJ `R_geom(τ_fold) = ∫_BZ Tr g_ab^{(P_0)}(k; τ_fold) d^d k` HKR-image; calibration baseline for substrate-distance-1 d=4 Pillar III↔IV bridge) is PRESERVED across the FWD-C1 candidate (§VII.AU.OP-PROJ Pillar I↔II bridge at substrate-distance-1 pole s=3); the convention-tag suffix discloses this lineage at the methodology layer. Container-thinking violation FORBIDDEN: "the TEMPLATE-INHERITED tag IS a different substrate-physics computation" — inverted: "the substrate physics IS UNCHANGED (composite INFO; c_sub_corrected=2.238 EXACT; n_s_FW=0.9561 bit-match; Planck σ=2.0952 by design); only the methodology disclosure (convention-tag suffix + deferred-pending sub-class taxonomy routing) is updated". The retrofit lands the audit-trail discipline that the original §W5-6 INFO verdict pre-dated; the retrofit DOES NOT alter the scientific verdict per Option A absolute verdict permanence.
""".strip()


# --- Verification + emission ---

def verify_post_edit_registry() -> dict:
    """Verify the §VII.AU re-tag markers are present in post-edit registry."""
    text = REGISTRY.read_text(encoding="utf-8")
    missing = [m for m in REQUIRED_REGISTRY_MARKERS if m not in text]
    return {
        "all_markers_present": len(missing) == 0,
        "missing": missing,
        "markers_checked": len(REQUIRED_REGISTRY_MARKERS),
        "markers_found": len(REQUIRED_REGISTRY_MARKERS) - len(missing),
    }


def verify_post_edit_s89_w5_wp() -> dict:
    """Verify the §W5-6 retrofit disclosure paragraph is present in S89 W5 WP."""
    text = S89_W5_WP.read_text(encoding="utf-8")
    missing = [m for m in REQUIRED_S89_W5_WP_MARKERS if m not in text]
    return {
        "all_markers_present": len(missing) == 0,
        "missing": missing,
        "markers_checked": len(REQUIRED_S89_W5_WP_MARKERS),
        "markers_found": len(REQUIRED_S89_W5_WP_MARKERS) - len(missing),
    }


def verify_cf_14_landed() -> dict:
    """Verify CF-14 PASS prereq."""
    s90_verdicts = (ROOT / "computations" / "session-90" / "s90_gate_verdicts.txt").read_text(encoding="utf-8")
    has_cf_14_pass = (
        "S90-DEFERRED-PENDING-RULE-FILE-ENFORCEMENT-CLAUSE-EXTENSION: PASS" in s90_verdicts
        and CF_14_AUDIT_SHA in s90_verdicts
    )
    return {
        "cf_14_pass_landed": has_cf_14_pass,
        "cf_14_audit_sha": CF_14_AUDIT_SHA,
    }


def verify_original_w5_6_verdict_retained() -> dict:
    """Verify the original §W5-6 INFO verdict is RETAINED on disk (verdict permanence)."""
    s89_verdicts = S89_GATE_VERDICTS.read_text(encoding="utf-8")
    return {
        "original_audit_sha_present": ORIGINAL_AUDIT_SHA in s89_verdicts,
        "original_gate_id_info_line_present": (
            f"{ORIGINAL_GATE_ID}: INFO" in s89_verdicts
        ),
        "original_verdict_retained_on_disk": (
            ORIGINAL_AUDIT_SHA in s89_verdicts
            and f"{ORIGINAL_GATE_ID}: INFO" in s89_verdicts
        ),
    }


def build_input_pin_map(
    registry_check: dict,
    s89_w5_wp_check: dict,
    cf_14_check: dict,
    original_retained: dict,
) -> dict:
    """Construct ordered input-pin map for audit_sha256 computation."""
    return {
        "gate_id": GATE_ID,
        "plan_block_sha": PLAN_BLOCK_SHA,
        "anatomy_post_w1_14_sha": ANATOMY_POST_W1_14_SHA,
        "substrate_first_rule_sha": SUBSTRATE_FIRST_RULE_SHA,
        "v3_closure_recovery_sha": V3_CLOSURE_RECOVERY_SHA,
        "registry_pre_w1_15_sha": REGISTRY_PRE_W1_15_SHA,
        "s89_w5_wp_pre_w1_15_sha": S89_W5_WP_PRE_W1_15_SHA,
        "allowlist_post_w1_14_sha": ALLOWLIST_POST_W1_14_SHA,
        "instances_post_w1_14_sha": INSTANCES_POST_W1_14_SHA,
        "original_audit_sha_supersedes_target": ORIGINAL_AUDIT_SHA,
        "original_content_sha": ORIGINAL_CONTENT_SHA,
        "new_convention": NEW_CONVENTION,
        "convention_suffix": CONVENTION_SUFFIX,
        "sub_class_tag": SUB_CLASS_TAG,
        "cf_14_audit_sha_prereq": CF_14_AUDIT_SHA,
        "registry_markers_present": registry_check["all_markers_present"],
        "s89_w5_wp_markers_present": s89_w5_wp_check["all_markers_present"],
        "cf_14_pass_landed": cf_14_check["cf_14_pass_landed"],
        "original_verdict_retained": original_retained["original_verdict_retained_on_disk"],
    }


def main() -> int:
    # Step 1 — Verify CF-14 prereq
    cf_14_check = verify_cf_14_landed()
    if not cf_14_check["cf_14_pass_landed"]:
        print(json.dumps({
            "error": "CF-14 PASS prereq NOT landed; W1-15 cannot proceed",
            "check": cf_14_check,
            "verdict": "INFO (PRE-REG-INC blocked on CF-14)",
        }, indent=2))
        return 1

    # Step 2 — Verify original §W5-6 verdict permanence on S89 disk
    original_retained = verify_original_w5_6_verdict_retained()
    if not original_retained["original_verdict_retained_on_disk"]:
        print(json.dumps({
            "error": "Original §W5-6 verdict NOT retained on S89 disk; verdict permanence violated",
            "check": original_retained,
        }, indent=2))
        return 1

    # Step 3 — Verify post-edit registry state
    registry_check = verify_post_edit_registry()
    if not registry_check["all_markers_present"]:
        print(json.dumps({
            "error": "Post-edit registry verification FAILED",
            "check": registry_check,
        }, indent=2))
        return 1

    # Step 4 — Verify post-edit S89 W5 WP state
    s89_w5_wp_check = verify_post_edit_s89_w5_wp()
    if not s89_w5_wp_check["all_markers_present"]:
        print(json.dumps({
            "error": "Post-edit S89 W5 WP verification FAILED",
            "check": s89_w5_wp_check,
        }, indent=2))
        return 1

    # Step 5 — Append allowlist row
    with ALLOWLIST.open("a", encoding="utf-8") as f:
        f.write(ALLOWLIST_ROW)
    print(f"Allowlist row appended: {ALLOWLIST_ROW.strip()}")

    # Step 6 — Append instances rationale (use .replace() not .format() to avoid
    # curly-brace conflicts with math notation like g_ab^{(P_0)})
    rationale = (
        "\n" + INSTANCES_RATIONALE_TEMPLATE
        .replace("__GATE_ROW__", GATE_ROW)
        .replace("__SESSION__", SESSION)
        .replace("__PLAN_BLOCK_SHA__", PLAN_BLOCK_SHA)
        .replace("__GATE_ID__", GATE_ID)
        .replace("__ORIGINAL_AUDIT_SHA__", ORIGINAL_AUDIT_SHA)
        .replace("__ORIGINAL_VALUE__", ORIGINAL_VALUE_FIELD)
        .replace("__CF_14_AUDIT_SHA__", CF_14_AUDIT_SHA)
        .replace("__SUBSTRATE_FIRST_RULE_SHA__", SUBSTRATE_FIRST_RULE_SHA)
        .replace("__V3_CLOSURE_RECOVERY_SHA__", V3_CLOSURE_RECOVERY_SHA)
        .replace("__REGISTRY_PRE_W1_15_SHA__", REGISTRY_PRE_W1_15_SHA)
        .replace("__S89_W5_WP_PRE_W1_15_SHA__", S89_W5_WP_PRE_W1_15_SHA)
        + "\n"
    )
    with INSTANCES.open("a", encoding="utf-8") as f:
        f.write(rationale)
    print(f"Instances rationale appended: {rationale.count(chr(10))} lines, {len(rationale)} chars")

    # Step 7 — Emit corrective canonical verdict line with SUPERSEDES tag
    # Per Option A: supersedes goes in value= field per `gate-verdicts.md §"Option A"`.
    # The emit_verdict() helper appends ';supersedes=<sha>' to value= when supersedes is non-empty.
    input_pin_map = build_input_pin_map(registry_check, s89_w5_wp_check, cf_14_check, original_retained)

    # value preserves original substrate-physics content + adds retrofit metadata
    value_str = (
        f"{ORIGINAL_VALUE_FIELD}"
        f";retrofit_landing=S90_W1_15"
        f";convention_suffix_added=-TEMPLATE-INHERITED-FROM-W-5"
        f";substrate_physics_unchanged=True"
        f";sub_class_re_tag=REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION"
        f";cf_14_prereq_pass_audit_sha={CF_14_AUDIT_SHA}"
        f";registry_markers_present={registry_check['all_markers_present']}"
        f";s89_w5_wp_disclosure_paragraph_appended={s89_w5_wp_check['all_markers_present']}"
        f";original_verdict_retained_on_disk_per_verdict_permanence=True"
        f";allowlist_row_appended=True"
        f";instances_row_appended=True"
    )

    result = emit_verdict(
        gate_id=GATE_ID,
        verdict=ORIGINAL_VERDICT,  # INFO — DO NOT alter scientific verdict
        value_str=value_str,
        scheme=ORIGINAL_SCHEME,
        convention=NEW_CONVENTION,
        L_max=ORIGINAL_L_MAX,
        input_pin_map=input_pin_map,
        content_target=REGISTRY,  # post-edit registry is the primary diff target
        supersedes=ORIGINAL_AUDIT_SHA,  # Option A SUPERSEDES tag (full 64-char)
    )
    print(json.dumps({
        "gate_id": result["gate_id"],
        "verdict": result["verdict"],
        "audit_sha256": result["audit_sha256"],
        "content_sha256": result["content_sha256"],
        "supersedes": ORIGINAL_AUDIT_SHA,
        "cf_14_check": cf_14_check,
        "original_retained": original_retained,
        "registry_check": registry_check,
        "s89_w5_wp_check": s89_w5_wp_check,
    }, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
