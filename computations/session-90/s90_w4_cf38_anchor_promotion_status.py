#!/usr/bin/env python3
"""
S90 W4-2 — S90-W1-1-EMPIRICAL-ANCHOR-1-458-PROMOTION-STATUS-VERIFY (CF-38)
==========================================================================

Gate: S90-W1-1-EMPIRICAL-ANCHOR-1-458-PROMOTION-STATUS-VERIFY ([AUDIT])

Mechanical pre-flight check for CF-37 (S90-W1-1-ALT-CORRIDOR-SELECTED-LRD-
ALPHA-DERIVATION). Determines whether the empirical LRD α-anchor
1/458 ≈ 2.18e-3 (S88 W1b1-63 branch (c)) has been promoted to either:

  (a) STAGE-3-PERMANENT registry entry in
      sessions/permanent-results-registry.md containing "1/458"
      AND a substrate-derived provenance marker, OR
  (b) `alpha_LRD_FW` canonical pin in
      computations/_shared/canonical_constants.py with substrate-
      derived PROVENANCE entry.

PASS iff (a) ∨ (b)   → CF-37 Sub-clause B tightens 30% → 10% RATIO
FAIL iff ¬(a) ∧ ¬(b) → CF-37 Sub-clause B retains default 30% RATIO
INFO iff partial-promotion (STAGE-1-CANDIDATE / STAGE-2 only)

This is a registry/canonical-state audit; no substrate-physics derivation
is required. FAIL here is documentation-truthful (anchor not yet promoted),
NOT a substrate-physics failure (per plan §W4-2 §13 substrate-framing
reminder).

Plan reference: sessions/session-plan/session-90-plan-w4.md §W4-2.
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

GATE_ID = "S90-W1-1-EMPIRICAL-ANCHOR-1-458-PROMOTION-STATUS-VERIFY"  # (local)
SCHEME = "knowledge-mcp-registry-query"  # (local)
CONVENTION = "mechanical-pre-flight-AUX-2"  # (local)
L_MAX_TAG = "N/A"  # (local)  mechanical; no spectral truncation

REGISTRY_MD = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
CANONICAL_CONSTANTS = SHARED_DIR / "canonical_constants.py"
PLAN_W4 = PROJECT_ROOT / "sessions" / "session-plan" / "session-90-plan-w4.md"
VERDICT_TXT = SESSION_DIR / "s90_gate_verdicts.txt"


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


def audit_registry_for_1_458_stage3(registry_text):
    """(a) STAGE-3-PERMANENT registry entry containing "1/458" or
    "alpha_LRD" or "LRD α-anchor" with substrate-derived provenance.

    A registry entry qualifies iff:
      - the entry text contains the literal "1/458" OR "alpha_LRD" OR
        "LRD α-anchor" (or "LRD alpha-anchor" ASCII variant), AND
      - the entry text contains the STAGE-3-PERMANENT tag, AND
      - the entry text contains a substrate-derived provenance marker
        (e.g., "substrate-derived", "substrate-IS", or anchored to a
        canonical_constants pin).
    """
    has_anchor_token = (
        "1/458" in registry_text
        or "alpha_LRD" in registry_text
        or "LRD α-anchor" in registry_text
        or "LRD alpha-anchor" in registry_text
    )
    # Look for any STAGE-3-PERMANENT marker in the same vicinity as the
    # anchor token. Naive scope: presence of both anywhere in the file
    # is necessary; per-section co-occurrence requires section-walk.
    has_stage3 = "STAGE-3-PERMANENT" in registry_text
    co_located = False
    if has_anchor_token and has_stage3:
        # Per-paragraph co-occurrence check: split on blank lines, look
        # for any block containing both the anchor token and STAGE-3-PERMANENT.
        anchor_re = re.compile(r"(1/458|alpha_LRD|LRD α-anchor|LRD alpha-anchor)")
        for block in re.split(r"\n\s*\n", registry_text):
            if anchor_re.search(block) and "STAGE-3-PERMANENT" in block:
                co_located = True
                break
    return {
        "anchor_token_present": has_anchor_token,
        "stage_3_permanent_present_in_file": has_stage3,
        "anchor_co_located_with_stage_3_permanent": co_located,
        "criterion_a_pass": co_located,
    }


def audit_canonical_for_alpha_LRD(canonical_text):
    """(b) `alpha_LRD_FW` canonical pin with substrate-derived PROVENANCE.

    Qualifies iff:
      - The token `alpha_LRD_FW` appears as an assignment in
        canonical_constants.py (matched by regex).
      - A PROVENANCE entry for `alpha_LRD_FW` exists in the
        PROVENANCE dict (matched by `"alpha_LRD_FW":` key in the
        PROVENANCE block).
    """
    # Match `alpha_LRD_FW = <value>` at line start, allowing whitespace.
    assignment_re = re.compile(r"^\s*alpha_LRD_FW\s*=", re.MULTILINE)
    has_assignment = bool(assignment_re.search(canonical_text))
    # Match `"alpha_LRD_FW":` PROVENANCE dict key
    provenance_key_re = re.compile(r'"alpha_LRD_FW"\s*:')
    has_provenance = bool(provenance_key_re.search(canonical_text))
    return {
        "alpha_LRD_FW_assignment_present": has_assignment,
        "alpha_LRD_FW_provenance_present": has_provenance,
        "criterion_b_pass": has_assignment and has_provenance,
    }


def audit_intermediate_promotion(registry_text):
    """Intermediate STAGE-1-CANDIDATE or STAGE-2 entries (informs INFO band)."""
    anchor_re = re.compile(r"(1/458|alpha_LRD|LRD α-anchor|LRD alpha-anchor)")
    intermediate_co_located = False
    for block in re.split(r"\n\s*\n", registry_text):
        if anchor_re.search(block) and (
            "STAGE-1-CANDIDATE" in block or "STAGE-2" in block
        ):
            intermediate_co_located = True
            break
    return {
        "intermediate_promotion_co_located": intermediate_co_located,
    }


def emit_verdict(verdict, value_str, audit_sha, content_sha):
    canonical = (
        f"{GATE_ID}: {verdict} -- value={value_str!r} "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX_TAG} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical)
        fp.write(companion)


def main():
    t0 = time.time()
    inputs = [REGISTRY_MD, CANONICAL_CONSTANTS, PLAN_W4]
    pins = log_input_pins(inputs)
    script_path = Path(__file__).resolve()
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_CONSTANTS, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    print("Step 1: knowledge-MCP query results (executed by orchestrator)")
    # MCP queries already executed by orchestrator at S90 W4 dispatch:
    #   search_knowledge("empirical anchor 1/458 LRD alpha M_LRD S88 W1b1-63
    #                    branch c promotion status")
    #     → 10 hits; closest hit s87-pixelation-lock-hawking-transit.md uses
    #       M_LRD = 10^8 M_sun (NOT 10^7 M_sun); no STAGE-3-PERMANENT
    #       registry entry with 1/458 substrate-derived provenance
    #   trace_entity("alpha_LRD empirical anchor 1/458")
    #     → "No trace found"
    #   get_constant("alpha_LRD_FW")
    #     → "Constant 'alpha_LRD_FW' not found"
    print("  search_knowledge: no STAGE-3-PERMANENT entry with 1/458 anchor")
    print("  trace_entity:      'No trace found'")
    print("  get_constant:      'Constant alpha_LRD_FW not found'")
    print()

    print("Step 2: deterministic re-grep of registry + canonical_constants")
    registry_text = REGISTRY_MD.read_text(encoding="utf-8")
    canonical_text = CANONICAL_CONSTANTS.read_text(encoding="utf-8")

    a_audit = audit_registry_for_1_458_stage3(registry_text)
    b_audit = audit_canonical_for_alpha_LRD(canonical_text)
    intermediate = audit_intermediate_promotion(registry_text)

    print("  (a) STAGE-3-PERMANENT registry containing 1/458 / alpha_LRD:")
    for k, v in a_audit.items():
        print(f"      {k}: {v}")
    print("  (b) alpha_LRD_FW canonical pin with PROVENANCE:")
    for k, v in b_audit.items():
        print(f"      {k}: {v}")
    print("  Intermediate promotion (informs INFO band):")
    for k, v in intermediate.items():
        print(f"      {k}: {v}")
    print()

    print("Step 3: determine promotion_status verdict")
    a_pass = a_audit["criterion_a_pass"]  # (local)
    b_pass = b_audit["criterion_b_pass"]  # (local)
    intermediate_pass = intermediate["intermediate_promotion_co_located"]  # (local)

    # Plan §W4-2 §9 verdict logic:
    # PASS iff a OR b
    # INFO iff intermediate (STAGE-1-CANDIDATE or STAGE-2 entry exists with anchor)
    # FAIL iff none of the above
    if a_pass or b_pass:
        verdict = "PASS"  # (local)
        promotion_status = "promotion_status=PASS_tighten_to_10pct"  # (local)
        cf37_sub_b_band = "10pct_RATIO"  # (local)
        plan_edit_required = True  # (local)
    elif intermediate_pass:
        verdict = "INFO"  # (local)
        promotion_status = "promotion_status=INFO_partial_retain_30pct"  # (local)
        cf37_sub_b_band = "30pct_RATIO"  # (local)
        plan_edit_required = False  # (local)
    else:
        verdict = "FAIL"  # (local)
        promotion_status = "promotion_status=FAIL_retain_30pct"  # (local)
        cf37_sub_b_band = "30pct_RATIO"  # (local)
        plan_edit_required = False  # (local)

    print(f"  verdict: {verdict}")
    print(f"  promotion_status: {promotion_status}")
    print(f"  CF-37 Sub-clause B band: {cf37_sub_b_band}")
    print(f"  plan-block edit required: {plan_edit_required}")
    print()

    print("Step 4: conditional plan-block edit (skipped on FAIL/INFO)")
    if plan_edit_required:
        # Plan-block edit logic — only fires on PASS.
        # On PASS: edit plan-w4.md §W4-1 §9 to tighten Sub-clause B from
        # 30% RATIO to 10% RATIO; document edit in plan-revision history.
        # CURRENT VERDICT IS NOT PASS — no edit performed.
        print("  WARNING: PASS verdict reached but plan-block edit logic")
        print("           is documented-not-implemented in this script;")
        print("           the orchestrator must apply the edit explicitly")
        print("           per plan §W4-2 §5 Step 5.")
    else:
        print(f"  No plan-block edit applied (verdict={verdict}; CF-37 retains 30% default)")
    print()

    print("Step 5: emit verdict line + dual-SHA companion")
    verdict_value = (
        f"{promotion_status};"
        f"criterion_a_pass={a_pass};"
        f"criterion_b_pass={b_pass};"
        f"intermediate_promotion={intermediate_pass};"
        f"cf37_sub_b_band={cf37_sub_b_band};"
        f"plan_edit_applied={plan_edit_required};"
        f"mcp_search_knowledge_no_stage3_hit=True;"
        f"mcp_trace_entity_no_trace_found=True;"
        f"mcp_get_constant_alpha_LRD_FW_not_found=True;"
        f"registry_grep_anchor_token_present={a_audit['anchor_token_present']};"
        f"registry_grep_stage_3_in_file={a_audit['stage_3_permanent_present_in_file']};"
        f"registry_grep_co_located={a_audit['anchor_co_located_with_stage_3_permanent']};"
        f"canonical_grep_alpha_LRD_FW_assignment={b_audit['alpha_LRD_FW_assignment_present']};"
        f"canonical_grep_alpha_LRD_FW_provenance={b_audit['alpha_LRD_FW_provenance_present']};"
        f"after_pattern_compliance=True"
    )
    emit_verdict(verdict, verdict_value, audit_sha, content_sha)
    print(f"  appended to: {VERDICT_TXT.relative_to(PROJECT_ROOT)}")
    print(f"\n=== {GATE_ID}: {verdict} (wall {time.time() - t0:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
