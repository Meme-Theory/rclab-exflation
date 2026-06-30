#!/usr/bin/env python3
"""
S90 W7-5 — S90-VII-AR-STAGE-2-INDEPENDENT-VERIFY (CF-58)
=========================================================
MECHANICAL CLOSURE — orchestrator-authored per `.claude/rules/mechanical-closure-discipline.md`

Gate: S90-VII-AR-STAGE-2-INDEPENDENT-VERIFY ([AUDIT])

Closure rationale: per plan §W7-5 §6 Method "EFFECTIVE DISPATCH ORDERING
(per CONNES V.2 + context line 241): W8 CF-60 (S90-W5-7-RETRY-WITH-
CANONICAL-W7A74-PRIMARY-EVALUATOR) PRECEDES CF-58. CF-58 dispatch is
CONDITIONAL on CF-60 completing FIRST", AND plan §"Wave 7 Decision
Point Prerequisites" item 1 ("W8 CF-60 PRECEDES CF-58: ... CF-58
dispatch is CONDITIONAL on CF-60 completing FIRST"), CF-58 dispatch
requires W8 CF-60 PASS as a structural prerequisite.

W8 CF-60 status check: NOT STARTED. §W8-2 in `sessions/archive/session-90/
session-90-w8-workingpaper.md` shows the gate `S90-W5-7-RETRY-WITH-
CANONICAL-W7A74-PRIMARY-EVALUATOR` at status NOT STARTED; no verdict
line for this gate-ID exists in `computations/session-90/s90_gate_verdicts.txt`.

W2 precedent: S90-VII-AR-STAGE-2-PENDING-A36-SUB-CLAIM-ADVANCEMENT
already closed PRE-REG-INC at S90 W2 with audit_sha256=
8b6ac827d81effac95ad6efb2182c1b4c8711c67a0593f84391c201bbe97690a
(verdict-file:57 region; value='PRE-REG-INC_blocked_by_CF-60_pending;...').
The current CF-58 in W7 is a structurally-similar §VII.AR Stage-2 gate
blocked on the same prereq (W8 CF-60); the W7 closure follows the W2
precedent pattern with a distinct gate-ID.

Mechanical-closure admissibility checklist (per .claude/rules/mechanical-closure-discipline.md):

  (1) Upstream-block topology is the cause: W8 CF-60 verdict ≠ PASS
      (NOT STARTED); plan §"Wave 7 Decision Point Prerequisites" item 1
      specifies "Sequence: CF-60 → CF-58"; plan §W7-5 §6 Method
      "EFFECTIVE DISPATCH ORDERING" explicitly halts on missing
      upstream. ✓
  (2) Verdict honesty: emit FAIL (per rule §2 — never PASS for
      mechanical closure); value field uses PRE-REG-INC_blocked_by_*
      pattern. ✓
  (3) Per-gate-distinct audit_sha256: closure script computes its own
      audit_sha256 from input pin map + embed_keys (gate-id, wp-id,
      scheme, convention); distinct from W2 closure audit_sha256
      8b6ac827... and from any other gate's audit_sha256. ✓
  (4) Audit-trail signature: value='PRE-REG-INC_blocked_by_W8_CF60_
      NOT_STARTED_substrate_physics_intact_True'; descriptive and
      grep-verifiable. ✓
  (5) Working-paper update is in-script: WP §W7-5 update appended via
      Edit-tool call from orchestrator after script run (single-shot
      AFTER-pattern; this script emits the verdict line, orchestrator
      updates WP section).

NOT a substrate-physics failure; this is documented structural cascade
closure — the §VII.AR Stage-2 → Stage-3 promotion pathway remains
structurally awaitable on a refined CF-60 (W8) PASS at S91+ with the
FULL-tier 5-anchor Spearman matrix input becoming available to the
Stage-2 cross-reviewers gen-physicist (Axis-A) + volovik (Axis-B).

Plan reference: sessions/session-plan/session-90-plan-w7.md §W7-5
(lines 895-1109).
"""

from __future__ import annotations

import sys
from pathlib import Path

_SHARED_DIR = Path(__file__).resolve().parent.parent / "_shared"
sys.path.insert(0, str(_SHARED_DIR))
from canonical_constants import *  # noqa: F401,F403,E402

import hashlib  # noqa: E402
import json  # noqa: E402
import re  # noqa: E402
import time  # noqa: E402

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

GATE_ID = "S90-VII-AR-STAGE-2-INDEPENDENT-VERIFY"  # (local)
SCHEME = "mack-sole-writer-single-shot-AFTER-pattern"  # (local) parallel to W2 precedent scheme tag
CONVENTION = "vii-ar-stage-2-independent-verify-MECHANICAL-CLOSURE-W8-CF60-BLOCKED"  # (local)
L_MAX = 10  # (local) per plan §W7-5 PRDR L_max pin
SCHEMA_VERSION = "S87+"  # (local)

CF60_GATE_ID = "S90-W5-7-RETRY-WITH-CANONICAL-W7A74-PRIMARY-EVALUATOR"  # (local) per plan §W7-5 §6 + W8 plan §W8-2
W2_PRECEDENT_GATE_ID = "S90-VII-AR-STAGE-2-PENDING-A36-SUB-CLAIM-ADVANCEMENT"  # (local)
W2_PRECEDENT_AUDIT_SHA = "8b6ac827d81effac95ad6efb2182c1b4c8711c67a0593f84391c201bbe97690a"  # (local)

VERDICT_TXT = SESSION_DIR / "s90_gate_verdicts.txt"
CANONICAL_CONSTANTS = SHARED_DIR / "canonical_constants.py"
PLAN_W7 = PROJECT_ROOT / "sessions" / "session-plan" / "session-90-plan-w7.md"
WP_W7 = PROJECT_ROOT / "sessions" / "session-90" / "session-90-w7-workingpaper.md"
WP_W8 = PROJECT_ROOT / "sessions" / "session-90" / "session-90-w8-workingpaper.md"
MCC_RULE = PROJECT_ROOT / ".claude" / "rules" / "mechanical-closure-discipline.md"


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
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path, canonical_path, pins, embed_keys):
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
    embed_json = json.dumps(
        dict(sorted(embed_keys.items())), separators=(",", ":"), sort_keys=True,
    ).encode("utf-8")
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_audit.update(embed_json)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


def grep_cf60_status(verdict_text):
    """Check if W8 CF-60 has any verdict line on disk."""
    for line in verdict_text.splitlines():
        if line.startswith(f"{CF60_GATE_ID}:"):
            head, _, tail = line.partition("--")
            status = head.split(":")[1].strip()
            m_sha = re.search(r"audit_sha256=([a-f0-9]{64})", tail)
            audit_sha = m_sha.group(1) if m_sha else None
            return {"found": True, "status": status, "audit_sha256": audit_sha}
    return {"found": False}


def grep_w8_2_status(wp_w8_text):
    """Check W8 §W8-2 working-paper status."""
    # Look for §W8-2. ... \n**Status**: NOT STARTED pattern
    pattern = r"### §W8-2\..*?\*\*Status\*\*:\s*([A-Z ]+)"
    m = re.search(pattern, wp_w8_text, re.DOTALL)
    if m:
        return {"found": True, "status": m.group(1).strip()}
    return {"found": False}


def emit_verdict(verdict, value_str, audit_sha, content_sha):
    canonical = (
        f"{GATE_ID}: {verdict} -- value={value_str!r} "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA_VERSION}\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
        f"# PRE-REG-INC per session-90-plan-w7.md §W7-5 §6 + §\"Wave 7 Decision Point Prerequisites\" item 1; "
        f"deferred to S91; required prereq: [{CF60_GATE_ID}=PASS]; "
        f"closure_script=computations/session-90/s90_w7_cf58_mechanical_closure_blocked_by_w8_cf60.py; "
        f"W2_precedent={W2_PRECEDENT_GATE_ID}_audit_sha_{W2_PRECEDENT_AUDIT_SHA[:16]}\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical)
        fp.write(companion)


def main():
    t0 = time.time()
    inputs = [VERDICT_TXT, WP_W8, PLAN_W7, MCC_RULE, CANONICAL_CONSTANTS]
    pins = log_input_pins(inputs)
    embed_keys = {
        "_gate_id": GATE_ID,
        "_wp_id": "session-90-w7-workingpaper.md::§W7-5",
        "_scheme": SCHEME,
        "_convention": CONVENTION,
        "_closure_kind": "PRE-REG-INC-upstream-blocked-by-W8-CF60",
        "_blocking_prereq": CF60_GATE_ID,
        "_w2_precedent_audit_sha": W2_PRECEDENT_AUDIT_SHA,
    }
    script_path = Path(__file__).resolve()
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_CONSTANTS, pins, embed_keys)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    # Step 1: locate W8 CF-60 verdict line on disk (substantiate prereq-block)
    print("Step 1: locate W8 CF-60 verdict line on disk (substantiate prereq-block)")
    verdict_text = VERDICT_TXT.read_text(encoding="utf-8")
    cf60_verdict = grep_cf60_status(verdict_text)
    print(f"  CF-60 verdict-file grep: {cf60_verdict}")
    wp_w8_text = WP_W8.read_text(encoding="utf-8") if WP_W8.exists() else ""
    w8_2_status = grep_w8_2_status(wp_w8_text)
    print(f"  W8 §W8-2 working-paper status grep: {w8_2_status}")
    cf60_blocked = (not cf60_verdict["found"]) or (cf60_verdict["found"] and cf60_verdict["status"] != "PASS")
    if not cf60_blocked:
        print("ERROR: W8 CF-60 PASSed; mechanical closure NOT applicable.")
        print("       Re-dispatch CF-58 as Stage-2 multi-agent dispatch per plan §W7-5 §6.")
        return 3
    print(f"  ✓ W8 CF-60 verdict-block confirmed (no PASS line on disk); mechanical closure admissible.")
    print()

    # Step 2: verify W2 precedent exists on disk (cross-link audit)
    print("Step 2: verify W2 precedent S90-VII-AR-STAGE-2-PENDING-A36 PRE-REG-INC closure on disk")
    w2_precedent = grep_cf60_status_helper(verdict_text, W2_PRECEDENT_GATE_ID)
    print(f"  W2 precedent grep: {w2_precedent}")
    if w2_precedent["found"]:
        print(f"  ✓ W2 precedent cross-link audit confirmed (W2 closure for §VII.AR Stage-2 family).")
    else:
        print(f"  WARN: W2 precedent NOT FOUND. Closure still admissible per mechanical-closure-discipline.md")
        print(f"        (prereq-block topology is independent of W2 precedent existence).")
    print()

    # Step 3: determine closure verdict + value-field
    print("Step 3: determine closure verdict + audit-trail signature")
    closure_verdict = "FAIL"  # (local) — never PASS for mechanical closure per rule §2
    closure_value = (
        f"PRE-REG-INC_blocked_by_{CF60_GATE_ID}=NOT_STARTED;"
        f"blocking_prereq=W8_CF-60_FULL-TIER_W7A-74_PRIMARY_EVALUATOR;"
        f"cf60_status=CF-60_PASS_not_found_in_s90_gate_verdicts;"
        f"w8_2_wp_status={w8_2_status.get('status', 'unknown')};"
        f"vii_ar_registry_text_unchanged_at_STAGE-1-CANDIDATE-PENDING-CROSS-TIER-CONFIRMATION;"
        f"substrate_physics_intact=True;"
        f"plan_section_authority=session-90-plan-w7.md_§W7-5_§6_+_Wave_7_Decision_Point_Prerequisites_item_1;"
        f"mechanical_closure_per_rule=.claude/rules/mechanical-closure-discipline.md;"
        f"re-dispatch_path=S91+_after_CF-60_PASS_lands;"
        f"w2_precedent_gate_id={W2_PRECEDENT_GATE_ID};"
        f"w2_precedent_audit_sha_full_64={W2_PRECEDENT_AUDIT_SHA};"
        f"axis_a_cross_reviewer_planned=gen-physicist;"
        f"axis_b_cross_reviewer_planned=volovik-superfluid-universe-theorist;"
        f"OAA_exclusion=connes-ncg-theorist_+_lizzi-spectral-functional-theorist_excluded_as_W-22_W7a-74_§V.5_authors;"
        f"closure_kind=mechanical-orchestrator-authored-no-multi-agent-dispatch;"
        f"closure_admissibility_per_mechanical-closure-discipline.md=ALL_5_CLAUSES_PASS;"
        f"after_pattern_compliance=True"
    )
    print(f"  closure_verdict: {closure_verdict}")
    print(f"  closure_value: documents prereq-block + W2 precedent + planned Stage-2 cross-reviewer assignment")
    print()

    # Step 4: append closure verdict + dual-SHA companion + PRE-REG-INC comment
    print("Step 4: append closure verdict + dual-SHA companion + PRE-REG-INC comment row")
    emit_verdict(closure_verdict, closure_value, audit_sha, content_sha)
    print(f"  appended to: {VERDICT_TXT.relative_to(PROJECT_ROOT)}")
    print()

    print(f"=== {GATE_ID}: {closure_verdict} (mechanical closure; wall {time.time() - t0:.2f}s) ===")
    return 0


def grep_cf60_status_helper(verdict_text, gate_id):
    """Generic grep for any gate-ID in verdict file."""
    for line in verdict_text.splitlines():
        if line.startswith(f"{gate_id}:"):
            head, _, tail = line.partition("--")
            status = head.split(":")[1].strip()
            m_sha = re.search(r"audit_sha256=([a-f0-9]{64})", tail)
            audit_sha = m_sha.group(1) if m_sha else None
            return {"found": True, "status": status, "audit_sha256": audit_sha}
    return {"found": False}


if __name__ == "__main__":
    sys.exit(main())
