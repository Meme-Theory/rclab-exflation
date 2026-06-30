#!/usr/bin/env python3
"""
S91 W8 mechanical PRE-REG-INC closure for §W8-1 + §W8-2
========================================================

§W8-1 (S91-W8-CF-67-VII-AU-OP-PROJ-FWD-C1-STAGE-2-CROSS-AXIS-INDEPENDENT-VERIFY)
  Conditional on W2 T1.5 (S91-VII-AU-OP-PROJ-FIRST-EXTRACTION-PARAMETERIZATION-
  REFINEMENT) PASS.  If W2 T1.5 returns FAIL/INFO/ABSENT across all sub-options,
  this gate mechanical-closes per `.claude/rules/mechanical-closure-discipline.md`
  with value='PRE-REG-INC_blocked_by_W2_T1_5_first_extraction_NOT_PASS'.

§W8-2 (S91-W8-CF-68-VII-AV-CORNER-IV-STAGE-2-CROSS-AXIS-INDEPENDENT-VERIFY)
  Blocked unless EITHER W1 T1.1 (S91-VII-AV-FULL-CC-PHYSICAL-MULTIPLIERS) PASS
  OR W5 T1.11 (S91-VII-AV-FULL-BDG-RE-DERIVATION) PASS.  If BOTH FAIL/ABSENT,
  this gate mechanical-closes per `.claude/rules/mechanical-closure-discipline.md`
  with value='PRE-REG-INC_blocked_by_W1_T1_1_FAIL_AND_W5_T1_11_FAIL'.

Both upstream-block topologies are pre-registered in
sessions/session-plan/session-91-plan-w8.md §"Wave 8 Decision Point
Prerequisites" routing table (lines 34-42), so the closure script's emission
is plan-anticipated (NOT post-hoc) per mechanical-closure-discipline.md
§"When mechanical closure IS acceptable" item 1.

Dual-SHA per `.claude/templates/script-template.py` §4:
    audit_sha256   = sha256(script_bytes || canonical_bytes || pinmap_json)
    content_sha256 = sha256(script_bytes)

Per-gate-distinct audit_sha256 is preserved by construction: the pinmap
embeds per-gate _gate_id + _wp_id + _scheme + _convention so the two W8
gates compute distinct audit_sha256 values even when their prereq sets
might overlap (here they don't — §W8-1 ↔ W2 T1.5; §W8-2 ↔ W1 T1.1 + W5 T1.11
disjunct).

This is a metadata-closure script: NO physics is computed.  The 2 emitted
verdict lines record that each gate was structurally untestable at S91 W8
because its upstream prerequisite verdict(s) have status ≠ PASS in
`computations/session-91/s91_gate_verdicts.txt`.
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
VERDICT_TXT = PROJECT_ROOT / "computations" / "session-91" / "s91_gate_verdicts.txt"
CANONICAL_PY = PROJECT_ROOT / "computations" / "_shared" / "canonical_constants.py"
WP_PATH = PROJECT_ROOT / "sessions" / "session-91" / "session-91-w8-workingpaper.md"

# sys.path setup BEFORE canonical_constants import (matches S91 W1 producing-
# script pattern: e.g. s91_w1_cf70_full_cc_multipliers.py lines 130-134).
sys.path.insert(0, str(PROJECT_ROOT / "computations" / "_shared"))
sys.path.insert(0, str(PROJECT_ROOT / "computations"))

# canonical_constants import retained for audit compliance (no constants used;
# this script emits metadata closures only — no framework computation).
from canonical_constants import *  # noqa: F401,F403,E402


# Carry-forward symbol → canonical S91 gate ID for prereq lookup.
PREREQ_GATE_IDS = {
    "W2_T1_5":   "S91-VII-AU-OP-PROJ-FIRST-EXTRACTION-PARAMETERIZATION-REFINEMENT",
    "W1_T1_1":   "S91-VII-AV-FULL-CC-PHYSICAL-MULTIPLIERS",
    "W5_T1_11":  "S91-VII-AV-FULL-BDG-RE-DERIVATION",
}

# W8 mechanical-close gate metadata + required-prereq map per plan §"Wave 8
# Decision Point Prerequisites" (session-91-plan-w8.md lines 34-42).
# Each gate carries an explicit `block_logic` field:
#   "all_must_pass"  → blocked iff at least one prereq is non-PASS
#                       (single-prereq case; equivalent here)
#   "any_must_pass"  → blocked iff ALL prereqs are non-PASS (disjunctive prereq)
W8_GATES = [
    {
        "gate_id":     "S91-W8-CF-67-VII-AU-OP-PROJ-FWD-C1-STAGE-2-CROSS-AXIS-INDEPENDENT-VERIFY",
        "wp_id":       "W8-1",
        "carry_id":    "T2.28",
        "scheme":      "joint-theorem-promotion-stage-2-pass-and-orchestrator-composite",
        "convention":  "cross-axis-axis-a-vdd-plus-axis-b-mack-orchestrator-direct",
        "L_max":       12,
        "required":    ["W2_T1_5"],
        "block_logic": "all_must_pass",
        "block_value_template": "PRE-REG-INC_blocked_by_W2_T1_5_first_extraction_NOT_PASS",
        "agent":       "van-den-dungen-bridge-theorist + mack-cosmic-bridge",
    },
    {
        "gate_id":     "S91-W8-CF-68-VII-AV-CORNER-IV-STAGE-2-CROSS-AXIS-INDEPENDENT-VERIFY",
        "wp_id":       "W8-2",
        "carry_id":    "T2.29",
        "scheme":      "joint-theorem-promotion-stage-2-pass-and-orchestrator-composite-FULL",
        "convention":  "cross-axis-axis-a-vdd-plus-axis-b-mack-orchestrator-direct-FULL",
        "L_max":       12,
        "required":    ["W1_T1_1", "W5_T1_11"],
        "block_logic": "any_must_pass",
        "block_value_template": "PRE-REG-INC_blocked_by_W1_T1_1_FAIL_AND_W5_T1_11_FAIL",
        "agent":       "van-den-dungen-bridge-theorist + mack-cosmic-bridge",
    },
]


def parse_prereq_verdicts() -> dict[str, tuple[str, str]]:
    """Read s91_gate_verdicts.txt; return {symbol: (status, value_chunk)} for prereqs.

    Most-recent canonical line per prereq gate_id wins (the file is append-only;
    per .claude/rules/gate-verdicts.md §"Option A — sig_5 remediation pathway",
    later lines supersede earlier ones via the supersedes= tag chain, but for
    the "is this gate's verdict PASS?" predicate the LATEST line is the
    operative one).
    """
    states: dict[str, tuple[str, str]] = {}            # (local)
    if not VERDICT_TXT.exists():
        # Defensive: if verdict file does not exist, treat all prereqs as ABSENT.
        for sym in PREREQ_GATE_IDS:
            states[sym] = ("ABSENT", "verdict_file_not_present")
        return states
    text = VERDICT_TXT.read_text(encoding="utf-8")     # (local)
    for sym, gate_id in PREREQ_GATE_IDS.items():
        prefix = gate_id + ":"                          # (local)
        lines = [ln for ln in text.splitlines()
                 if ln.startswith(prefix)
                 and "audit_sha256=" in ln]            # (local)
        if not lines:
            states[sym] = ("ABSENT", "no_verdict_line_in_s91_gate_verdicts_txt")
            continue
        last = lines[-1]                                # (local)
        body = last.split(":", 1)[1].strip()            # (local)
        status = body.split()[0].rstrip(",")            # (local)
        if "value=" in last:
            v_start = last.index("value=") + len("value=")   # (local)
            v_chunk = last[v_start:].split()[0]               # (local)
        else:
            v_chunk = "unknown"                          # (local)
        states[sym] = (status, v_chunk)
    return states


def compute_dual_sha(pinmap: dict[str, str]) -> tuple[str, str]:
    """Per .claude/templates/script-template.py §4 dual-SHA schema."""
    script_bytes = Path(__file__).read_bytes()         # (local)
    canonical_bytes = CANONICAL_PY.read_bytes()        # (local)
    pinmap_json = json.dumps(
        dict(sorted(pinmap.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")                                   # (local)
    h_audit = hashlib.sha256()                          # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                         # (local)
    h_content = hashlib.sha256()                        # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()                     # (local)
    return audit, content


def is_gate_blocked(gate: dict, states: dict[str, tuple[str, str]]) -> tuple[bool, list[str]]:
    """Return (blocked, list_of_block_reasons_per_prereq).

    block_logic = "all_must_pass": blocked iff ANY prereq != PASS
    block_logic = "any_must_pass": blocked iff ALL prereqs != PASS
    """
    block_parts: list[str] = []                         # (local)
    pass_count = 0                                      # (local)
    for sym in gate["required"]:
        stat, _ = states[sym]
        if stat == "PASS":
            pass_count += 1
        else:
            block_parts.append(f"{sym}_{stat}")
    if gate["block_logic"] == "all_must_pass":
        blocked = (pass_count < len(gate["required"]))
    elif gate["block_logic"] == "any_must_pass":
        blocked = (pass_count == 0)
    else:
        raise ValueError(f"unknown block_logic: {gate['block_logic']}")
    return blocked, block_parts


def build_value_string_and_pinmap(
    gate: dict,
    states: dict[str, tuple[str, str]],
    block_parts: list[str],
) -> tuple[str, dict[str, str]]:
    """Build (value_str, pinmap) for the given W8 gate."""
    pinmap: dict[str, str] = {
        "_gate_id":     gate["gate_id"],
        "_wp_id":       gate["wp_id"],
        "_carry_id":    gate["carry_id"],
        "_scheme":      gate["scheme"],
        "_convention":  gate["convention"],
        "_block_logic": gate["block_logic"],
    }                                                   # (local)
    for sym in gate["required"]:
        stat, _ = states[sym]
        pinmap[sym] = f"{PREREQ_GATE_IDS[sym]}={stat}"
    # Use the plan-documented value string verbatim so downstream consumers
    # can grep for the canonical phrase per the routing table.
    return gate["block_value_template"], pinmap


def make_verdict_line(gate: dict, value_str: str, audit_sha: str, content_sha: str) -> str:
    return (
        f"{gate['gate_id']}: FAIL -- value={value_str!r} "
        f"scheme={gate['scheme']} convention={gate['convention']} "
        f"L_max={gate['L_max']} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )


def make_companion_row(gate: dict, value_str: str, audit_sha: str, content_sha: str) -> str:
    req = ", ".join(gate["required"])                   # (local)
    return (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {gate['gate_id']} dual-SHA companion row (W9a-99 split); "
        f"PRE-REG-INC per session-91-plan-w8.md §\"Wave 8 Decision Point Prerequisites\" "
        f"routing table (lines 34-42); deferred to S92+; "
        f"required prereqs: [{req}] (block_logic={gate['block_logic']}); "
        f"closure_script=computations/session-91/s91_w8_pre_reg_inc_closure.py\n"
    )


def make_3tuple_companion_row(gate: dict, audit_sha: str) -> str:
    """S87+ schema-v2 3-tuple companion: sign/magnitude/regime annotation.

    For mechanical PRE-REG-INC closure (no physics computed, no directional
    claim asserted):
      sign_verdict     = N/A   (no signed delta; gate is [VERIFY-THEOREM] not [SIGN])
      magnitude_verdict = FAIL  (composite FAIL per plan routing table)
      regime_verdict    = VALID (mechanical-closure-discipline.md path; no
                                  regime-breakdown — the gate was structurally
                                  untestable, not numerically out-of-band)
    """
    return (
        f"# sign_verdict=N/A magnitude_verdict=FAIL regime_verdict=VALID "
        f"# {gate['gate_id']} 3-tuple annotation (S87 schema-v2); "
        f"mechanical-closure-discipline-md PRE-REG-INC blocked by upstream prereq absence\n"
    )


def update_wp_section(
    wp_text: str,
    gate: dict,
    states: dict[str, tuple[str, str]],
    value_str: str,
    pinmap: dict[str, str],
    audit_sha: str,
    content_sha: str,
) -> str:
    """Patch the WP §W8-1 or §W8-2 section with mechanical-closure status + verdict.

    Targets: the gate's top-level `**Status**: NOT STARTED` line is replaced
    with the PRE-REG-INC status; the three sub-section statuses (.AXIS-A,
    .AXIS-B, .COMPOSITE) are each replaced with a not-dispatched-due-to-
    mechanical-closure marker.  A new `### §{wp_id}.MECHANICAL-CLOSURE` block
    is appended at the end of the gate's section (before the closing `---`)
    carrying the verdict + dual-SHA + per-prereq state table.
    """
    sect_marker = f"## §{gate['wp_id']}."               # (local)
    sect_start = wp_text.index(sect_marker)             # (local)
    sect_end = wp_text.index("\n---\n", sect_start)     # (local)
    old_section = wp_text[sect_start:sect_end]          # (local)
    new_section = old_section                           # (local)

    # 1. Patch the TOP-LEVEL Status line (the first **Status**: NOT STARTED
    #    in the section).  We do a single-replace so sub-section statuses
    #    (which have the same literal "**Status**: NOT STARTED" text) are
    #    handled separately below.
    top_status_old = "**Status**: NOT STARTED"          # (local)
    top_status_new = (
        "**Status**: PRE-REG-INCOMPLETE (mechanical closure 2026-05-17 per plan "
        "§\"Wave 8 Decision Point Prerequisites\" routing table; deferred to S92+)"
    )                                                   # (local)
    # Replace only the FIRST occurrence (which is the top-level status).
    idx_first = new_section.find(top_status_old)
    if idx_first != -1:
        new_section = (new_section[:idx_first] + top_status_new
                       + new_section[idx_first + len(top_status_old):])

    # 2. Patch each remaining sub-section `**Status**: NOT STARTED` (within
    #    .AXIS-A, .AXIS-B, .COMPOSITE) with a mechanical-closure marker.
    sub_status_new = (
        "**Status**: NOT DISPATCHED (mechanical PRE-REG-INC closure on parent gate; "
        "no axis-side reviewer was spawned because the upstream prerequisite verdict "
        "was absent in s91_gate_verdicts.txt at W8 dispatch time)"
    )                                                   # (local)
    new_section = new_section.replace(top_status_old, sub_status_new)

    # 3. Append a `### §{wp_id}.MECHANICAL-CLOSURE` block at the end of the
    #    section (just before the closing `---`).  The block carries the
    #    verdict + dual-SHA + per-prereq observed states + 4-tuple +
    #    solution-space interpretation + substrate framing.
    prereq_lines = []                                   # (local)
    for sym in gate["required"]:
        stat, val = states[sym]
        gid = PREREQ_GATE_IDS[sym]
        if stat == "PASS":
            prereq_lines.append(f"  - {sym} (`{gid}`): **PASS** — does not block this gate")
        elif stat == "ABSENT":
            prereq_lines.append(
                f"  - {sym} (`{gid}`): **ABSENT** (no verdict line in "
                f"`computations/session-91/s91_gate_verdicts.txt`) — BLOCKING; "
                f"value_observed={val}"
            )
        else:
            prereq_lines.append(
                f"  - {sym} (`{gid}`): **{stat}** (value_observed={val}) — BLOCKING"
            )

    closure_block = (
        "\n"
        f"### §{gate['wp_id']}.MECHANICAL-CLOSURE — Orchestrator-direct PRE-REG-INC closure\n"
        "\n"
        f"**Status**: PRE-REG-INCOMPLETE (mechanical closure per "
        f"`.claude/rules/mechanical-closure-discipline.md`)\n"
        f"**Verdict**: FAIL (PRE-REG-INC) — value={value_str!r}\n"
        "\n"
        "Mechanical PRE-REG-INC closure: this gate's upstream prerequisite(s) per the "
        f"plan §\"Wave 8 Decision Point Prerequisites\" routing table (block_logic="
        f"`{gate['block_logic']}`) have not all met the PASS predicate in "
        "`computations/session-91/s91_gate_verdicts.txt` at W8 dispatch time. The plan "
        "explicitly anticipates this scenario and pre-registers the mechanical-closure "
        "value-string verbatim — the closure is plan-anticipated, NOT post-hoc, per "
        "`mechanical-closure-discipline.md §\"When mechanical closure IS acceptable\"` "
        "item 1 (upstream-block topology is the cause; closure value follows the plan-"
        "documented pattern).\n"
        "\n"
        "**Required prerequisites and observed states**:\n"
        + "\n".join(prereq_lines) + "\n"
        "\n"
        f"**4-tuple**: `(value={value_str!r}, scheme={gate['scheme']}, "
        f"convention={gate['convention']}, L_max={gate['L_max']})`\n"
        "\n"
        f"**Dual-SHA** (per `.claude/templates/script-template.py §4`):\n"
        f"  - `audit_sha256`: `{audit_sha}`\n"
        f"  - `content_sha256`: `{content_sha}`\n"
        "\n"
        f"**Pinmap** (input to `closure_hash` for `audit_sha256`):\n"
        "```json\n"
        + json.dumps(dict(sorted(pinmap.items())), indent=2)
        + "\n```\n"
        "\n"
        "**Closure mechanism**: `computations/session-91/s91_w8_pre_reg_inc_closure.py` "
        "(orchestrator-authored mechanical closure, NOT specialist-agent dispatch). "
        "No physics computation was performed; the verdict line records that the gate "
        "could not be evaluated due to upstream prerequisite block. The dispatched-agent "
        "fallback was not invoked because the absent prereq verdict is a structural "
        "fact about the verdict-file state — agents cannot synthesize a verdict from a "
        "non-existent upstream gate.\n"
        "\n"
        "**Solution-space interpretation**: The gate's intended Stage-2 cohomology-class "
        "structural-identity verification corridor remains UNTESTED at this session; "
        "this is a no-information outcome (NOT a corridor closure). The plan-§\"PASS / "
        "FAIL / INFO thresholds\" consequence states are deferred to S92+ conditional "
        "on the blocking prerequisite landing. The gate ID + dual-SHA + 4-tuple are "
        "recorded so the S92+ re-emission can be audit-traced back to this PRE-REG-INC "
        "entry. STAGE-1-CANDIDATE registry status of the underlying §VII registry slot "
        "is RETAINED-PROVISIONAL pending the next Stage-2 attempt; HIT K-counter does "
        "NOT advance.\n"
        "\n"
        "**Substrate framing** (per `.claude/rules/phononic-framing.md §\"IS Space, "
        "Not IN Space\"`): the substrate's spectral content this gate would have "
        "interrogated remains uncharacterized by this gate's emission; the gate does "
        "not report on the substrate's structural state, only on the audit trail's "
        "block-by-prerequisite topology. The substrate IS the spectral triple "
        "`(A_K, H_K, D_K)` at τ_fold = 0.190; the substrate-IS observable the gate "
        "would have verified remains substrate-IS — it is the METHODOLOGY-FLOOR "
        "F-image (a verdict line) that is PRE-REG-INC, not the substrate-IS identity "
        "itself.\n"
        "\n"
        "**Verdict line appended to** `computations/session-91/s91_gate_verdicts.txt`:\n"
        "```\n"
        + make_verdict_line(gate, value_str, audit_sha, content_sha)
        + make_companion_row(gate, value_str, audit_sha, content_sha)
        + make_3tuple_companion_row(gate, audit_sha)
        + "```\n"
    )                                                   # (local)
    new_section = new_section + closure_block

    return wp_text[:sect_start] + new_section + wp_text[sect_end:]


def main() -> int:
    states = parse_prereq_verdicts()
    print("=== S91 W8 prerequisite verdict states (most-recent line per gate) ===")
    for sym, (status, value) in states.items():
        gid = PREREQ_GATE_IDS[sym]
        print(f"  {sym:10} = {gid:65} : {status:7} (value={value})")
    print()

    # Recover any pre-existing W8 verdict lines (idempotency on re-runs).
    verdict_text = VERDICT_TXT.read_text(encoding="utf-8") if VERDICT_TXT.exists() else ""
    existing: dict[str, tuple[str, str, str]] = {}     # (local)
    for gate in W8_GATES:
        prefix = gate["gate_id"] + ":"                  # (local)
        ms = [ln for ln in verdict_text.splitlines()
              if ln.startswith(prefix)
              and "audit_sha256=" in ln
              and "content_sha256=" in ln]              # (local)
        if not ms:
            continue
        last = ms[-1]                                   # (local)
        audit_sha = last.split("audit_sha256=", 1)[1].split()[0]
        content_sha = last.split("content_sha256=", 1)[1].split()[0]
        v_chunk = last.split("value=", 1)[1].split()[0].strip("'\"")
        existing[gate["gate_id"]] = (audit_sha, content_sha, v_chunk)

    emitted: list[tuple] = []                           # (local)
    to_append: list[tuple] = []                         # (local)
    for gate in W8_GATES:
        blocked, block_parts = is_gate_blocked(gate, states)
        if not blocked:
            print(f"[NOT-BLOCKED] {gate['gate_id']} — "
                  f"prereqs satisfied (block_logic={gate['block_logic']}); skipping closure")
            continue
        value_str, pinmap = build_value_string_and_pinmap(gate, states, block_parts)
        if gate["gate_id"] in existing:
            audit_sha, content_sha, _ = existing[gate["gate_id"]]
            print(f"[ALREADY-EMITTED] {gate['wp_id']:5} {gate['gate_id']}")
            print(f"          recovered audit: {audit_sha[:16]}...  content: {content_sha[:16]}...")
        else:
            audit_sha, content_sha = compute_dual_sha(pinmap)
            print(f"[BLOCKED] {gate['wp_id']:5} {gate['gate_id']}")
            print(f"          value: {value_str}")
            print(f"          block_logic: {gate['block_logic']}; block_parts: {block_parts}")
            print(f"          audit: {audit_sha[:16]}...  content: {content_sha[:16]}...")
            to_append.append((gate, value_str, audit_sha, content_sha))
        emitted.append((gate, value_str, pinmap, audit_sha, content_sha))

    if not emitted:
        print("\nNo W8 gates were blocked; nothing to close.")
        return 0

    # Append NEW verdict lines (canonical + W9a-99 dual-SHA companion +
    # S87+ schema-v2 3-tuple companion).  Atomic single-shot POSIX O_APPEND
    # write per `.claude/rules/epistemic-discipline.md §"Registry-Write
    # Hygiene under Parallel-Writer Race"` item 2.
    if to_append:
        print(f"\n=== Appending {len(to_append)} verdict + companion-row triples ===")
        with VERDICT_TXT.open("a", encoding="utf-8") as fp:
            for gate, value_str, audit_sha, content_sha in to_append:
                fp.write(make_verdict_line(gate, value_str, audit_sha, content_sha))
                fp.write(make_companion_row(gate, value_str, audit_sha, content_sha))
                fp.write(make_3tuple_companion_row(gate, audit_sha))
    else:
        print("\n=== All blocked W8 verdicts already in verdict file; no appends needed ===")

    # Update WP sections (§W8-1 and §W8-2 separately).
    print("\n=== Updating W8 working-paper sections ===")
    wp_text = WP_PATH.read_text(encoding="utf-8")
    for gate, value_str, pinmap, audit_sha, content_sha in emitted:
        # Skip WP update if the MECHANICAL-CLOSURE block already exists
        # (idempotency).
        if f"### §{gate['wp_id']}.MECHANICAL-CLOSURE" in wp_text:
            print(f"  skipped WP §{gate['wp_id']} ({gate['gate_id']}) — "
                  "MECHANICAL-CLOSURE block already present (idempotent re-run)")
            continue
        wp_text = update_wp_section(wp_text, gate, states, value_str, pinmap,
                                    audit_sha, content_sha)
        print(f"  updated WP §{gate['wp_id']} ({gate['gate_id']})")
    WP_PATH.write_text(wp_text, encoding="utf-8")
    print(f"\n=== Wrote {WP_PATH.relative_to(PROJECT_ROOT)} ===")

    print(f"\n=== S91-W8-PRE-REG-INC-CLOSURE: {len(emitted)} gates closed PRE-REG-INC ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
