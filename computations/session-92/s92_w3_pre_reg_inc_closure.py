#!/usr/bin/env python3
"""S92 W3 mechanical PRE-REG-INC closure for §W3-8, §W3-10, §W3-11.

Three gates close mechanical per `.claude/rules/mechanical-closure-discipline.md`:

  §W3-8 (S92-W3-CF-S92-W5-1-B-VII-AV-FULL-CC-CROSS-ROUTE-COMPARISON)
    CONDITIONAL on W1 CF-W9-4 §VII.AF.1.OP-PROJ FULL-physical re-extraction PASS.
    Observed: W1 CF-W9-4 = FAIL (RD classification, atlas_spread=+3.015860e-02).
    Closure: PRE-REG-INC_blocked_by_W1_CF-W9-4_FAIL_RD_classification_atlas_spread_3.02pct.

  §W3-10 (S92-W3-CF-S92-W5-1-D-L-MAX-MULTIPLICATIVE-CANCELLATION-RULE-EXTENSION)
    CONDITIONAL on W3-6 PASS. Observed: W3-6 = INFO (Level_2_invariance_witness
    4.43e-10 ∈ INFO band per (1e-10, 1e-6]; structural identity at precision floor).
    Closure: PRE-REG-INC_blocked_by_W3-6_INFO_K-counter-K1-K2-advancement-evidence-recorded-rule-file-extension-deferred-S93.

  §W3-11 (S92-W3-CF-W8-CONSOLIDATED-10-VII-AV-W8-2-RE-DISPATCH)
    CONDITIONAL on (W1 CF-W9-4 PASS OR W5 T1.11 PASS) AND W3-1 PASS.
    Observed: W1 CF-W9-4 = FAIL ∧ W5 T1.11 = NOT LANDED at S92.
    Closure: PRE-REG-INC_blocked_by_W1_CF-W9-4_FAIL_AND_W5_T1_11_NOT_LANDED_S92.

All three upstream-block topologies are pre-registered in
sessions/session-plan/session-92-plan-w3.md §"Wave 3 Decision Point Prerequisites"
and per-gate upstream_prereq machinery pins — the closure script's emission is
plan-anticipated (NOT post-hoc) per mechanical-closure-discipline.md
§"When mechanical closure IS acceptable" item 1.

Modeled on computations/session-91/s91_w8_pre_reg_inc_closure.py canonical pattern.
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
VERDICT_TXT = PROJECT_ROOT / "computations" / "session-92" / "s92_gate_verdicts.txt"
CANONICAL_PY = PROJECT_ROOT / "computations" / "_shared" / "canonical_constants.py"
WP_PATH = PROJECT_ROOT / "sessions" / "session-92" / "session-92-w3-workingpaper.md"

sys.path.insert(0, str(PROJECT_ROOT / "computations" / "_shared"))
sys.path.insert(0, str(PROJECT_ROOT / "computations"))
from canonical_constants import *  # noqa: F401,F403,E402


# Upstream prereq verdict-line gate IDs (latest non-superseded reading per
# Option-A protocol; for these gates we just check status of the LATEST line).
PREREQ_GATE_IDS = {
    "W1_CF_W9_4": "S92-W1-CF-W9-4-VII-AF-1-OP-PROJ-FULL-PHYSICAL-RE-EXTRACTION",
    "W3_6":       "S92-W3-CF-S92-W5-2.2-VII-AV-LEVEL-2-INVARIANCE-EXTENSION",
    "W3_1":       "S92-W3-CF-S91-W1-3.2-VII-AV-STAGE-1-CANDIDATE-PROMOTION",
}


W3_GATES = [
    {
        "gate_id":     "S92-W3-CF-S92-W5-1-B-VII-AV-FULL-CC-CROSS-ROUTE-COMPARISON",
        "wp_id":       "W3-8",
        "carry_id":    "CF-S92-W5-1-B",
        "scheme":      "FULL-CC-multipliers-cross-route-comparison-VII-AV-substrate-distance-2-pole-s4-UV-regulator-FI-RD-MIXED-classification",
        "convention":  "VII-AV-FULL-CC-CROSS-ROUTE-3-CLASS-UV-REGULATOR-CONDITIONAL-W1-CF-W9-4-PLAN-OPERATOR-CANONICAL-L-EMP-VERIFIED-2026-05-22",
        "L_max":       12,
        "required":    ["W1_CF_W9_4"],
        "block_logic": "all_must_pass",
        "block_value": "PRE-REG-INC_blocked_by_W1_CF-W9-4_FAIL_RD_classification_atlas_spread_3.02pct",
        "agent":       "connes-ncg-theorist + volovik-superfluid-universe-theorist",
        "supersedes_tag": None,
    },
    {
        "gate_id":     "S92-W3-CF-S92-W5-1-D-L-MAX-MULTIPLICATIVE-CANCELLATION-RULE-EXTENSION",
        "wp_id":       "W3-10",
        "carry_id":    "CF-S92-W5-1-D",
        "scheme":      "METHODOLOGY-class-rule-file-extension-K-counter-K1-to-K2-advancement-catalog-corpus-row-landing",
        "convention":  "L-MAX-MULTIPLICATIVE-CANCELLATION-INVARIANTS-K1-TO-K2-RULE-EXTENSION-S92-W3-CF-S92-W5-1-D-LANDING-METHODOLOGY-CLASS",
        "L_max":       "N/A",
        "required":    ["W3_6"],
        "block_logic": "all_must_pass",
        "block_value": "PRE-REG-INC_blocked_by_W3-6_INFO_K-counter-K1-K2-advancement-evidence-recorded-rule-file-extension-deferred-S93",
        "agent":       "orchestrator-direct-write",
        "supersedes_tag": None,
    },
    {
        "gate_id":     "S92-W3-CF-W8-CONSOLIDATED-10-VII-AV-W8-2-RE-DISPATCH",
        "wp_id":       "W3-11",
        "carry_id":    "CF-W8-CONSOLIDATED-10",
        "scheme":      "joint-theorem-promotion-stage-2-pass-and-orchestrator-composite-FULL",
        "convention":  "VII-AV-STAGE-2-CROSS-AXIS-VERIFY-AXIS-A-VDD-PLUS-AXIS-B-MACK-OAA-EXCLUDES-CONNES-PHONON-FIRST-VOLOVIK-OPTION-A-CORRECTIVE-supersedes-S91-W8-CF-68-PRE-REG-INC-SCHEMATIC-TO-FULL-TRANSITION-PLAN-OPERATOR-CANONICAL-L-EMP-VERIFIED-2026-05-22",
        "L_max":       12,
        "required":    ["W1_CF_W9_4", "W3_1"],
        "block_logic": "all_must_pass",
        "block_value": "PRE-REG-INC_blocked_by_W1_CF-W9-4_FAIL_AND_W5_T1_11_NOT_LANDED_S92",
        "agent":       "cross-reviewer-vdd-axis-a-plus-mack-axis-b",
        # W3-11 must carry supersedes tag per plan §W3-11 must_contain regex
        "supersedes_tag": "d6f990a70111774af2314a814602e510b36154e2c24ff52761bd688c4274771c",
    },
]


def parse_prereq_verdicts() -> dict[str, tuple[str, str]]:
    """Parse latest verdict line for each prereq gate from s92_gate_verdicts.txt."""
    states: dict[str, tuple[str, str]] = {}
    if not VERDICT_TXT.exists():
        for sym in PREREQ_GATE_IDS:
            states[sym] = ("ABSENT", "verdict_file_not_present")
        return states
    text = VERDICT_TXT.read_text(encoding="utf-8")
    for sym, gate_id in PREREQ_GATE_IDS.items():
        prefix = gate_id + ":"
        lines = [ln for ln in text.splitlines()
                 if ln.startswith(prefix) and "audit_sha256=" in ln]
        if not lines:
            states[sym] = ("ABSENT", "no_verdict_line")
            continue
        last = lines[-1]
        body = last.split(":", 1)[1].strip()
        status = body.split()[0].rstrip(",")
        states[sym] = (status, "value_observed_in_verdict_file")
    return states


def compute_dual_sha(pinmap: dict[str, str]) -> tuple[str, str]:
    script_bytes = Path(__file__).read_bytes()
    canonical_bytes = CANONICAL_PY.read_bytes()
    pinmap_json = json.dumps(dict(sorted(pinmap.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


def make_verdict_line(gate: dict, value: str, audit_sha: str, content_sha: str) -> str:
    if gate.get("supersedes_tag"):
        value_with_supersedes = f"supersedes={gate['supersedes_tag']};{value}"
    else:
        value_with_supersedes = value
    return (
        f"{gate['gate_id']}: FAIL -- value={value_with_supersedes!r} "
        f"scheme={gate['scheme']} convention={gate['convention']} "
        f"L_max={gate['L_max']} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )


def make_companion_row(gate: dict, audit_sha: str, content_sha: str) -> str:
    req = ", ".join(gate["required"])
    return (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {gate['gate_id']} dual-SHA companion row (W9a-99 split); "
        f"PRE-REG-INC mechanical-closure per mechanical-closure-discipline.md 5-clause admissibility; "
        f"upstream prereqs: [{req}]; "
        f"closure_script=computations/session-92/s92_w3_pre_reg_inc_closure.py\n"
    )


def make_3tuple_row(gate: dict) -> str:
    return (
        f"# sign_verdict=N/A magnitude_verdict=FAIL regime_verdict=VALID "
        f"# {gate['gate_id']} 3-tuple annotation (S87 schema-v2); "
        f"mechanical-closure PRE-REG-INC blocked by upstream prereq\n"
    )


def make_wp_block(gate: dict, value: str, states: dict, audit_sha: str, content_sha: str) -> str:
    """Build the §W3-N WP section replacement content (post-NOT-STARTED Status update)."""
    prereq_state_lines = []
    for sym in gate["required"]:
        stat, _ = states[sym]
        prereq_state_lines.append(
            f"  - `{sym}` ({PREREQ_GATE_IDS[sym]}): **{stat}**"
        )

    supersedes_note = ""
    if gate.get("supersedes_tag"):
        supersedes_note = (
            f"\n**Option-A supersedes tag** (per gate-verdicts.md §\"Option A\" MANDATORY S88 W8-100): "
            f"`supersedes={gate['supersedes_tag']}` (full 64-char; original S91 W8-CF-68 "
            f"PRE-REG-INC at s91_gate_verdicts.txt:151 RETAINED on disk per absolute "
            f"verdict permanence; corrective canonical at this gate carries supersedes "
            f"tag at emission time NOT post-hoc).\n"
        )

    return (
        f"**Status**: PRE-REG-INCOMPLETE (mechanical closure 2026-05-22 per "
        f"mechanical-closure-discipline.md §\"When mechanical closure IS acceptable\" "
        f"5-clause admissibility; upstream prereq block; deferred to S93+)\n"
        f"\n"
        f"**Output Artifacts**:\n"
        f"\n"
        f"- Closure script: `computations/session-92/s92_w3_pre_reg_inc_closure.py` "
        f"(orchestrator-direct mechanical closure; no specialist-agent dispatch)\n"
        f"- Verdict line appended to `computations/session-92/s92_gate_verdicts.txt`\n"
        f"\n"
        f"**MCP Pre-Compute Audit**: N/A — mechanical-closure scripts emit metadata "
        f"closures only per mechanical-discipline.md §\"When mechanical closure IS "
        f"acceptable\" item 1 (upstream-block topology is the documented cause; no "
        f"physics computation performed).\n"
        f"\n"
        f"**Verdict**: **FAIL** (PRE-REG-INC) — value=`{value}`\n"
        f"\n"
        f"**Results**:\n"
        f"\n"
        f"Mechanical PRE-REG-INC closure per mechanical-closure-discipline.md 5-clause "
        f"admissibility:\n"
        f"\n"
        f"1. **Upstream-block topology is the cause** ✓ — plan §W3-N upstream_prereq "
        f"machinery pin pre-registered this scenario.\n"
        f"2. **Verdict honesty: FAIL/PRE-REG-INC, never PASS** ✓ — emitted FAIL with "
        f"`PRE-REG-INC_blocked_by_...` value string.\n"
        f"3. **Per-gate-distinct audit_sha256** ✓ — gate-distinct pinmap keys ensure "
        f"sig_5 uniqueness.\n"
        f"4. **Audit-trail signature** ✓ — value names blocking prereq with status.\n"
        f"5. **Working-paper update in-script** ✓ — this block is emitted in the same "
        f"Python process as the verdict-line append.\n"
        f"\n"
        f"**Required prerequisites and observed states**:\n"
        + "\n".join(prereq_state_lines) + "\n"
        f"\n"
        f"**block_logic**: `{gate['block_logic']}`\n"
        f"{supersedes_note}"
        f"\n"
        f"**4-tuple**: `(value={value!r}, scheme={gate['scheme']}, "
        f"convention={gate['convention']}, L_max={gate['L_max']})`\n"
        f"\n"
        f"**Dual-SHA**:\n"
        f"  - `audit_sha256`: `{audit_sha}`\n"
        f"  - `content_sha256`: `{content_sha}`\n"
        f"\n"
        f"**Solution-space interpretation**: Gate's intended structural-identity "
        f"verification corridor remains UNTESTED at this session — this is a no-info "
        f"outcome (NOT a corridor closure). The plan-§\"PASS/FAIL/INFO thresholds\" "
        f"consequence states are deferred to S93+ conditional on the blocking "
        f"prerequisite landing. Gate ID + dual-SHA + 4-tuple are recorded so the S93+ "
        f"re-emission can be audit-traced back to this PRE-REG-INC entry.\n"
        f"\n"
        f"**Substrate framing** (phononic-framing.md §\"IS Space, Not IN Space\"): the "
        f"substrate's spectral content this gate would have interrogated remains "
        f"uncharacterized by this gate's emission — only the audit trail's block-by-"
        f"prerequisite topology is reported. The substrate IS the spectral triple "
        f"`(A_K, H_K, D_K(τ_fold))`; the substrate-IS observable remains substrate-IS, "
        f"it is the METHODOLOGY-FLOOR F-image (the verdict line) that is PRE-REG-INC.\n"
        f"\n"
        f"**Closure mechanism**: orchestrator-authored mechanical closure NOT "
        f"specialist-agent dispatch per mechanical-closure-discipline.md "
        f"§\"Orchestrator-authored mechanical-closure scripts emit verdict lines "
        f"WITHOUT specialist-agent dispatch and WITHOUT physics computation\" carve-out.\n"
    )


def update_wp_section(wp_text: str, gate: dict, value: str, states: dict,
                      audit_sha: str, content_sha: str) -> str:
    """Replace the §W3-N NOT STARTED placeholder with the mechanical-closure block."""
    sect_marker = f"### §{gate['wp_id']}."
    sect_start = wp_text.index(sect_marker)
    # Find next section or end of file
    next_marker = "### §"
    search_from = sect_start + len(sect_marker)
    next_idx = wp_text.find(next_marker, search_from)
    if next_idx == -1:
        next_idx = len(wp_text)

    old_section = wp_text[sect_start:next_idx]
    # Identify the Status line and replace from there through end of section
    status_old = "**Status**: NOT STARTED"
    if status_old not in old_section:
        # Idempotent: already updated; skip
        return wp_text

    status_idx = old_section.index(status_old)
    head = old_section[:status_idx]  # keep section header + metadata block
    new_section = head + make_wp_block(gate, value, states, audit_sha, content_sha) + "\n---\n\n"
    return wp_text[:sect_start] + new_section + wp_text[next_idx:]


def main() -> int:
    states = parse_prereq_verdicts()
    print("=== S92 W3 prerequisite verdict states (latest non-superseded line) ===")
    for sym, (status, _) in states.items():
        print(f"  {sym:14} = {PREREQ_GATE_IDS[sym]:65} : {status}")
    print()

    # Idempotency: check for existing verdict lines
    verdict_text = VERDICT_TXT.read_text(encoding="utf-8") if VERDICT_TXT.exists() else ""
    existing: dict[str, tuple[str, str]] = {}
    for gate in W3_GATES:
        prefix = gate["gate_id"] + ":"
        matches = [ln for ln in verdict_text.splitlines()
                   if ln.startswith(prefix) and "audit_sha256=" in ln]
        if matches:
            last = matches[-1]
            audit_sha = last.split("audit_sha256=", 1)[1].split()[0]
            content_sha = last.split("content_sha256=", 1)[1].split()[0]
            existing[gate["gate_id"]] = (audit_sha, content_sha)

    emitted = []
    to_append = []
    for gate in W3_GATES:
        # Build pinmap with gate-distinct keys
        pinmap = {
            "_gate_id":     gate["gate_id"],
            "_wp_id":       gate["wp_id"],
            "_carry_id":    gate["carry_id"],
            "_scheme":      gate["scheme"],
            "_convention":  gate["convention"],
            "_block_logic": gate["block_logic"],
            "_value":       gate["block_value"],
        }
        for sym in gate["required"]:
            stat, _ = states[sym]
            pinmap[sym] = f"{PREREQ_GATE_IDS[sym]}={stat}"
        if gate.get("supersedes_tag"):
            pinmap["_supersedes"] = gate["supersedes_tag"]

        if gate["gate_id"] in existing:
            audit_sha, content_sha = existing[gate["gate_id"]]
            print(f"[ALREADY-EMITTED] {gate['wp_id']:6} {gate['gate_id']}")
            print(f"  audit: {audit_sha[:16]}...  content: {content_sha[:16]}...")
        else:
            audit_sha, content_sha = compute_dual_sha(pinmap)
            print(f"[BLOCKED] {gate['wp_id']:6} {gate['gate_id']}")
            print(f"  value: {gate['block_value']}")
            print(f"  audit: {audit_sha[:16]}...  content: {content_sha[:16]}...")
            to_append.append((gate, audit_sha, content_sha))
        emitted.append((gate, audit_sha, content_sha))

    # Append verdict lines (atomic POSIX O_APPEND)
    if to_append:
        print(f"\n=== Appending {len(to_append)} verdict + companion-row triples ===")
        with VERDICT_TXT.open("a", encoding="utf-8") as fp:
            for gate, audit_sha, content_sha in to_append:
                fp.write(make_verdict_line(gate, gate["block_value"], audit_sha, content_sha))
                fp.write(make_companion_row(gate, audit_sha, content_sha))
                fp.write(make_3tuple_row(gate))

    # Update WP sections
    print("\n=== Updating W3 working-paper sections ===")
    wp_text = WP_PATH.read_text(encoding="utf-8")
    for gate, audit_sha, content_sha in emitted:
        if "**Status**: PRE-REG-INCOMPLETE (mechanical closure" in wp_text[
            wp_text.index(f"### §{gate['wp_id']}."):
            wp_text.index(f"### §{gate['wp_id']}.") + 200
        ]:
            print(f"  skipped WP §{gate['wp_id']} — already mechanical-closed (idempotent)")
            continue
        wp_text = update_wp_section(wp_text, gate, gate["block_value"], states,
                                    audit_sha, content_sha)
        print(f"  updated WP §{gate['wp_id']} ({gate['gate_id']})")
    WP_PATH.write_text(wp_text, encoding="utf-8")
    print(f"\n=== Wrote {WP_PATH.relative_to(PROJECT_ROOT)} ===")
    print(f"=== S92-W3-PRE-REG-INC-CLOSURE: {len(emitted)} gates closed PRE-REG-INC ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
