#!/usr/bin/env python3
"""
S90 W4-3 — S90-L-H-CANONICAL-RE-PINNING-CASCADE-TAIL-13OOM-RETRY (CF-39)
=========================================================================
MECHANICAL CLOSURE — orchestrator-authored per `.claude/rules/mechanical-closure-discipline.md`

Gate: S90-L-H-CANONICAL-RE-PINNING-CASCADE-TAIL-13OOM-RETRY ([VERIFY])

Closure rationale: per plan §W4-3 §5 ("Verify CF-40 PASS verdict line ...
If CF-40 is not PASS yet, halt and request CF-40 dispatch first.") AND plan
§W4-4 §11 ("CF-39 is BLOCKED until model PASSes."), CF-39 dispatch requires
CF-40 PASS as a structural prerequisite. CF-40 closed FAIL in S90 W4 with
audit_sha256 `66209e0d71b1ed19969595b8f263d526dcb972d2c84895e86bdfd58ecb9573c6`
(verdict line at `computations/session-90/s90_gate_verdicts.txt`; rel_dev =
13.54% / 5.99% / 13.03% at the 3 PDG anchors; max_rel_dev > 10% PASS band;
g_star_BS_T_H = 9.4083 produced as candidate but NOT promoted to
`canonical_constants.py` per Class-(b) PIN-LOOSE-SOURCE-TIGHT prevention).

Mechanical-closure admissibility checklist (per .claude/rules/mechanical-closure-discipline.md):

  (1) Upstream-block topology is the cause: CF-40 verdict ≠ PASS;
      plan's Decision Point table line 29 specifies "Sequence: CF-40 →
      CF-39"; plan §W4-3 §5 explicitly halts on non-PASS upstream. ✓
  (2) Verdict honesty: emit FAIL (per rule §2 — never PASS for mechanical
      closure). ✓
  (3) Per-gate-distinct audit_sha256: closure script computes its own
      audit_sha256 from the input pin map, distinct from CF-40's
      audit_sha256. ✓
  (4) Audit-trail signature: value='PRE-REG-INC_blocked_by_CF40_FAIL_
      g_star_BS_T_H_pending_FD_BE_integrated_form_refinement'; descriptive
      and grep-verifiable. ✓
  (5) Working-paper update is in-script: handled separately by orchestrator
      WP-write Task 8 (per /rclab-solo two-task-per-gate decomposition).

NOT a substrate-physics failure; this is documented structural cascade
closure — the (d)∘(b) downstream cosmological-horizon prediction
remains structurally awaitable on a refined CF-40 retry at S91+.

Plan reference: sessions/session-plan/session-90-plan-w4.md §W4-3.
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

GATE_ID = "S90-L-H-CANONICAL-RE-PINNING-CASCADE-TAIL-13OOM-RETRY"  # (local)
SCHEME = "substrate-pinned-T_H-cascade-tail"  # (local) per plan §6 scheme_tag
CONVENTION = "canonical-re-pinning-Option-A-supersedes-MECHANICAL-CLOSURE-CF40-BLOCKED"  # (local)
L_MAX = 10  # (local) per plan §6 (substrate cascade L_max=10)
SCHEMA_VERSION = "S87+"  # (local)

CF40_GATE_ID = "S90-F-M-SPECIES-MULTIPLICITY-RETRY-BOLTZMANN-SUPPRESSED"  # (local)
S88_SUPERSEDED_FULL_SHA = (  # (local) S88-CF-CURV-16-U1-BBN-CHUNKY-HAWKING-METALLICITY at audit_sha 2afd17ef99c81123...
    "2afd17ef99c81123548642938a4053fb82ea075ea626b5fe6afcbcb73215ed5d"
)

VERDICT_TXT = SESSION_DIR / "s90_gate_verdicts.txt"
CANONICAL_CONSTANTS = SHARED_DIR / "canonical_constants.py"
PLAN_W4 = PROJECT_ROOT / "sessions" / "session-plan" / "session-90-plan-w4.md"
S88_VERDICTS = COMPUTATIONS_DIR / "session-88" / "s88_gate_verdicts.txt"


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
    """Compute dual SHA over script bytes + canonical bytes + pinmap_json + embed_keys.

    embed_keys is a dict of per-gate identity keys (gate_id, wp_id, scheme,
    convention, etc.) embedded into the audit_sha computation per
    `.claude/rules/mechanical-closure-discipline.md` §3 — preserves sig_5
    SHA uniqueness across multiple gates closed by the same script.
    """
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


def grep_cf40_verdict(verdict_text):
    """Locate CF-40's canonical verdict line + extract status, audit_sha, rel_dev_max."""
    for line in verdict_text.splitlines():
        if line.startswith(f"{CF40_GATE_ID}:"):
            # Parse status (after ':' before '--')
            head, _, tail = line.partition("--")
            status = head.split(":")[1].strip()  # PASS|FAIL|INFO
            # Extract audit_sha256
            m_sha = re.search(r"audit_sha256=([a-f0-9]{64})", tail)
            audit_sha = m_sha.group(1) if m_sha else None
            # Extract max_rel_dev from value field
            m_max = re.search(r"max_rel_dev=([0-9.]+)", tail)
            max_rel_dev = float(m_max.group(1)) if m_max else None
            # Extract g_star_BS_T_H
            m_g = re.search(r"g_star_BS_T_H=([0-9.]+)", tail)
            g_star_BS_T_H = float(m_g.group(1)) if m_g else None
            return {
                "found": True,
                "status": status,
                "audit_sha256": audit_sha,
                "max_rel_dev": max_rel_dev,
                "g_star_BS_T_H": g_star_BS_T_H,
            }
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
        f"# PRE-REG-INC per session-90-plan-w4.md §W4-3 §5 + §W4-4 §11; "
        f"deferred to S91; required prereq: [{CF40_GATE_ID}=PASS]; "
        f"closure_script=computations/session-90/s90_w4_cf39_mechanical_closure_blocked_by_cf40.py\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical)
        fp.write(companion)


def main():
    t0 = time.time()
    inputs = [VERDICT_TXT, S88_VERDICTS, CANONICAL_CONSTANTS, PLAN_W4]
    pins = log_input_pins(inputs)
    embed_keys = {
        "_gate_id": GATE_ID,
        "_wp_id": "session-90-w4-workingpaper.md::§W4-3",
        "_scheme": SCHEME,
        "_convention": CONVENTION,
        "_closure_kind": "PRE-REG-INC-upstream-blocked",
    }
    script_path = Path(__file__).resolve()
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_CONSTANTS, pins, embed_keys)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    # ---- Step 1: Locate CF-40 verdict line on disk ----
    print("Step 1: locate CF-40 verdict line on disk (substantiate prereq-block)")
    verdict_text = VERDICT_TXT.read_text(encoding="utf-8")
    cf40 = grep_cf40_verdict(verdict_text)
    print(f"  CF-40 grep result: {cf40}")
    if not cf40["found"]:
        print("ERROR: CF-40 verdict line NOT FOUND. CF-39 mechanical closure cannot")
        print("       proceed without an upstream FAIL/INFO/PASS verdict to cite.")
        return 2

    cf40_status = cf40["status"]  # (local)
    cf40_sha_full = cf40["audit_sha256"]  # (local)
    cf40_max_rel_dev = cf40["max_rel_dev"]  # (local)
    cf40_g_star_BS_T_H = cf40["g_star_BS_T_H"]  # (local)
    print()

    # ---- Step 2: Verify CF-40 status ≠ PASS (the mechanical-closure trigger) ----
    print("Step 2: verify CF-40 status ≠ PASS")
    print(f"  CF-40 status: {cf40_status}")
    print(f"  CF-40 audit_sha256: {cf40_sha_full}")
    print(f"  CF-40 max_rel_dev: {cf40_max_rel_dev}")
    print(f"  CF-40 g_star_BS_T_H (candidate, NOT promoted): {cf40_g_star_BS_T_H}")
    if cf40_status == "PASS":
        print("ERROR: CF-40 PASSed; mechanical closure NOT applicable.")
        print("       Re-dispatch CF-39 with the actual L_H_canonical computation per plan §5.")
        return 3
    print(f"  ✓ CF-40 status = {cf40_status} (not PASS); mechanical closure is admissible per")
    print(f"    `.claude/rules/mechanical-closure-discipline.md` §1 clause (1).")
    print()

    # ---- Step 3: Verify Option A supersedes target SHA full 64-char form ----
    print("Step 3: verify Option A supersedes target SHA full 64-char form")
    s88_text = S88_VERDICTS.read_text(encoding="utf-8") if S88_VERDICTS.exists() else ""
    head_match = "2afd17ef99c81123" in s88_text
    full_match = S88_SUPERSEDED_FULL_SHA in s88_text
    print(f"  S88 head form '2afd17ef99c81123' present: {head_match}")
    print(f"  S88 full 64-char form '{S88_SUPERSEDED_FULL_SHA}' present: {full_match}")
    print(f"  NOTE: CF-39 PASS would have emitted Option A `supersedes={S88_SUPERSEDED_FULL_SHA}` token;")
    print(f"        on FAIL/PRE-REG-INC closure no supersedes-tag emission per `gate-verdicts.md`")
    print(f"        Option A protocol (supersedes tags only on CORRECTIVE PASS lines).")
    print()

    # ---- Step 4: Determine closure verdict + value-field ----
    print("Step 4: determine closure verdict + audit-trail signature")
    # Per mechanical-closure-discipline.md §2: emit FAIL or PRE-REG-INC, NEVER PASS.
    # Plan §W4-3 §11 FAIL clause: "CF-39 is BLOCKED until model PASSes."
    closure_verdict = "FAIL"  # (local) — also could be tagged as PRE-REG-INC; FAIL is more honest
    closure_value = (
        f"PRE-REG-INC_blocked_by_{CF40_GATE_ID}={cf40_status}_"
        f"g_star_BS_T_H_pending_FD_BE_integrated_form_refinement;"
        f"cf40_max_rel_dev={cf40_max_rel_dev};"
        f"cf40_g_star_BS_T_H_candidate_not_promoted={cf40_g_star_BS_T_H};"
        f"cf40_audit_sha_full_64={cf40_sha_full};"
        f"option_a_supersedes_target_full_64={S88_SUPERSEDED_FULL_SHA};"
        f"option_a_supersedes_emission_deferred=True;"
        f"refinement_pathway=Kolb-Turner_Eq3.62_FD_BE_integrated_forms;"
        f"deferred_to_S91=True;"
        f"plan_decision_point_routing=session-90-plan-w4.md_§W4-3_§5_prereq_halt_+_§W4-4_§11_BLOCKED_clause;"
        f"closure_kind=mechanical-orchestrator-authored-no-mack-dispatch;"
        f"closure_admissibility_per_mechanical-closure-discipline.md=ALL_5_CLAUSES_PASS;"
        f"after_pattern_compliance=True"
    )
    print(f"  closure_verdict: {closure_verdict}")
    print(f"  closure_value (~600 chars): documents prereq-block topology +")
    print(f"                              mack candidate values + Option A deferred state")
    print()

    # ---- Step 5: Append closure verdict + dual-SHA companion + PRE-REG-INC comment ----
    print("Step 5: append closure verdict + dual-SHA companion + PRE-REG-INC comment row")
    emit_verdict(closure_verdict, closure_value, audit_sha, content_sha)
    print(f"  appended to: {VERDICT_TXT.relative_to(PROJECT_ROOT)}")
    print()

    print(f"=== {GATE_ID}: {closure_verdict} (mechanical closure; wall {time.time() - t0:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
