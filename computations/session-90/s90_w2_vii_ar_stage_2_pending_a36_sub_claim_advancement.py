#!/usr/bin/env python3
"""
S90 W2-5 — S90-VII-AR-STAGE-2-PENDING-A36-SUB-CLAIM-ADVANCEMENT (CF-22)
========================================================================

Gate: S90-VII-AR-STAGE-2-PENDING-A36-SUB-CLAIM-ADVANCEMENT ([VERIFY])

This gate is **mechanically closed** per plan §W2-5 §6 line 585: it depends
on W8 CF-60 PASS-A or PASS-B (FULL-tier W7a-74 PRIMARY evaluator), which has
NOT executed at S90 W2 dispatch time. Per the explicit plan fallback clause
and `.claude/rules/mechanical-closure-discipline.md §"When mechanical
closure IS acceptable"`, the gate emits FAIL with
`value='PRE-REG-INC_blocked_by_CF-60_pending...'` and the audit trail names
the blocking prereq + re-dispatch path. The §VII.AR registry text is NOT
modified by this gate; status advance lands when CF-60 PASS arrives + this
gate re-dispatches with a supersedes-tagged corrective emission per
`gate-verdicts.md §"Option A — sig_5 remediation pathway"`.

Pre-flight upstream check:
  - Search `computations/session-90/s90_gate_verdicts.txt` for a CF-60 /
    FWD-C2 PASS line. If absent → mechanical-closure FAIL.
  - On absence: emit FAIL with diagnostic; substrate-physics intact at
    §VII.AR (PENDING-CROSS-TIER-CONFIRMATION retained per existing
    registry entry); next-session re-dispatch path documented.

Output 4-tuple:
  (value='PRE-REG-INC_blocked_by_CF-60_pending', scheme=...,
   convention=vii-ar-stage-1-both-sub-claims-confirmed-branch-PASS-A-or-PASS-B,
   L_max=12)
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

GATE_ID = "S90-VII-AR-STAGE-2-PENDING-A36-SUB-CLAIM-ADVANCEMENT"  # (local)
SCHEME = "mack-sole-writer-single-shot-AFTER-pattern"             # (local)
CONVENTION = "vii-ar-stage-1-both-sub-claims-confirmed-branch-PASS-A-or-PASS-B"  # (local)
L_MAX = 12                                                        # (local)

REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
VERDICT_TXT = SESSION_DIR / "s90_gate_verdicts.txt"
S89_VERDICTS_PATH = (
    PROJECT_ROOT / "computations" / "session-89" / "s89_gate_verdicts.txt"
)

# CF-60 prerequisite gate-ID pattern (per plan §6 line 591:
# `s90_w8_cf60_full_tier_w7a74_primary_evaluator.npz`); the verdict-line
# gate-ID for CF-60 is expected to contain "CF-60" or "FWD-C2" or
# "W7A-74-PRIMARY" tokens per the W8 plan.
CF_60_GATE_PATTERNS = [
    r"^S90-(.*?-)?CF[-_]?60",
    r"^S90-.*FWD-C2.*FULL-TIER",
    r"^S90-.*W7A-74-PRIMARY.*EVALUATOR",
    r"^S90-W8-CF60",
]  # (local)

# §W5-7 SHA (S89 SCHEMATIC tier; Sub-claim A intra-class anchor robustness)
W5_7_AUDIT_SHA = (
    "884db5e02fff4d9791c94ad0140edc77158355d189faa26491dc83e5b9cbbc50"
)  # (local) per s89_gate_verdicts.txt:122 mentioned in §VII.AU PARTIAL-POSITIVE
# annotation at line 17265 (S90 W1-15 retrofit disclosure)

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    REGISTRY_PATH,
    VERDICT_TXT,
    S89_VERDICTS_PATH,
]


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


def check_cf_60_landed():
    """Scan s90_gate_verdicts.txt for a CF-60 PASS line. Return (bool, str)
    where the str is the matched gate-ID and audit_sha or 'not-found'."""
    try:
        text = VERDICT_TXT.read_text(encoding="utf-8")  # (local)
    except OSError:
        return False, "verdict_file_unreadable"
    for line in text.splitlines():
        if not line.startswith("S90-"):
            continue
        for pattern in CF_60_GATE_PATTERNS:
            if re.match(pattern, line, re.IGNORECASE):
                if ": PASS" in line[:200]:
                    # Extract gate-ID + audit_sha256
                    gate_id_match = re.match(r"^(S90-[A-Z0-9-]+):", line)
                    sha_match = re.search(r"audit_sha256=([a-f0-9]{64})", line)
                    gate_id = gate_id_match.group(1) if gate_id_match else "unknown"
                    sha = sha_match.group(1) if sha_match else "unknown"
                    return True, f"{gate_id}@{sha}"
    return False, "CF-60_PASS_not_found_in_s90_gate_verdicts"


def emit_verdict(verdict, value_str, audit_sha, content_sha):
    canonical = (
        f"{GATE_ID}: {verdict} -- value={value_str!r} "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    closure_doc_companion = (
        f"# {GATE_ID} mechanical-closure per `.claude/rules/mechanical-closure-discipline.md`; "
        f"PRE-REG-INC per session-90-plan-w2.md §W2-5 line 585; "
        f"deferred to S91 (re-dispatch after CF-60 PASS lands); "
        f"required prereqs: [CF-60 W8 FULL-TIER W7A-74 PRIMARY EVALUATOR PASS-A or PASS-B]; "
        f"closure_script=computations/session-90/s90_w2_vii_ar_stage_2_pending_a36_sub_claim_advancement.py\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical)
        fp.write(companion)
        fp.write(closure_doc_companion)


def main():
    t0 = time.time()
    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()
    canonical_path = SHARED_DIR / "canonical_constants.py"
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    print("Step 0: pre-flight CF-60 (W8) upstream-dependency check")
    cf_60_landed, cf_60_status = check_cf_60_landed()
    print(f"  CF-60 PASS landed: {cf_60_landed}; status: {cf_60_status}")
    print()

    if cf_60_landed:
        # CF-60 has PASSed — proceed with the conditional registry edit
        # (Branch PASS-A vs PASS-B). This code path is NOT EXERCISED in
        # solo W2 execution because W8 has not run; it's documented for
        # future re-dispatch when CF-60 lands.
        print("  NOTE: CF-60 PASS detected — registry edit would proceed here.")
        print("        (Code path not currently exercised; solo W2 execution.)")
        verdict = "INFO"  # would be PASS post-registry-edit; INFO here as guardrail
        verdict_value = (
            f"cf_60_landed=True;but_solo_W2_executor_does_not_implement_registry_branch;"
            f"cf_60_status={cf_60_status};"
            f"recommended_path=re-dispatch_with_branch_implementation_in_S91+;"
            f"allowlist_row=pending;instances_row=pending"
        )
    else:
        # Mechanical closure FAIL per plan §6 line 585 + `mechanical-closure-discipline.md`
        verdict = "FAIL"  # (local)
        verdict_value = (
            f"PRE-REG-INC_blocked_by_CF-60_pending;"
            f"blocking_prereq=W8_CF-60_FULL-TIER_W7A-74_PRIMARY_EVALUATOR_PASS-A_or_PASS-B;"
            f"cf_60_status={cf_60_status};"
            f"vii_ar_registry_text_unchanged_at_STAGE-1-CANDIDATE-PENDING-CROSS-TIER-CONFIRMATION;"
            f"substrate_physics_intact=True;"
            f"plan_section_authority=session-90-plan-w2.md_section_W2-5_line_585;"
            f"mechanical_closure_per_rule=.claude/rules/mechanical-closure-discipline.md;"
            f"re-dispatch_path=S91+_after_CF-60_PASS_lands_with_Option-A_supersedes_tag;"
            f"w5_7_audit_sha={W5_7_AUDIT_SHA[:16]};"
            f"solo_mode=W2_only_per_user_rclab_solo_dispatch;"
            f"after_pattern_compliance=True;"
            f"allowlist_row=pending;instances_row=pending"
        )

    print(f"Step 1: emit_verdict ({verdict})")
    emit_verdict(verdict, verdict_value, audit_sha, content_sha)
    print(f"(value={verdict_value[:80]}..., scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print(f"\n=== {GATE_ID}: {verdict} (wall {time.time() - t0:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
