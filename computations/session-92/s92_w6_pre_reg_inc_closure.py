#!/usr/bin/env python3
"""S92 W6 mechanical PRE-REG-INC closure for §W6-4, §W6-5, §W6-6.

Three downstream gates close mechanical per `.claude/rules/mechanical-closure-
discipline.md` 5-clause admissibility when §W6-3 Stage-2 PASS-AND is structurally
impossible because BOTH cross-reviewers (Axis-A connes-NCG + Axis-B volovik)
independently FAIL on STRUCTURALLY DISTINCT clauses.

Observed prereq state on `computations/session-92/s92_gate_verdicts.txt`:
  Axis-A (connes): FAIL — Element 2 OE-form (laboratory-IN on substrate sub-
                   algebra image); verdict-line 172;
                   audit_sha256=`19662dc1544604e55f49280bd36d5a1e3862df381d0eb14f17b68ebc5b933cff`
  Axis-B (volovik): FAIL — JOINT Element 5 (1σ lower edge 5.316e-23 m⁻³ below
                    conjunct lower 5.500e-23 m⁻³ by 3.3%); verdict-line 167;
                    audit_sha256=`f20bc3ad108dbfad15a698682c6dbc5adfd30eddf8efe5d31ff2b0e1662f29f8`

Per `joint-theorem-promotion.md §"Stage 2 FAIL criterion"`: ANY cross-reviewer
FAIL on ANY clause → Stage-2 → 3 promotion BLOCKED. §VII.AX.OP-PROJ remains
STAGE-1-CANDIDATE.

Three blocked gates (downstream-conditional on §W6-3 PASS-AND):

  §W6-4 (S92-W6-CF-S92-W5-4-VII-AX-STATE-PROJ-COMPANION-LANDING)
    §VII.AX.STATE-PROJ companion landing is BLOCKED — Stage-3-eligibility of
    OP-PROJ does not exist, so the structural-orthogonal-companion landing
    is not yet eligible.

  §W6-5 (S92-W6-CF-S92-W5-4-FWD-C5-FORWARD-CALIBRATION-INSTANCES)
    FWD-C5 K=1→K=2 advancement is BLOCKED — substrate-physics analysis of
    the cardinality-cascade-shoulder variant is gated on the OP-PROJ
    Stage-3-eligibility verdict per the plan §W6-5 block_logic=must_pass_and.

  §W6-6 (S92-W6-CF-S92-W5-4-CANONICAL-CONSTANTS-PROMOTION-N-PBH-FW-PENDING-STAGE-3)
    canonical_constants.py promotion of `n_PBH_FW_central` is BLOCKED — Step 2
    of canonical write-order halted at the prereq-block boundary. Step 1
    (verdict-file emission) was already discharged at S91 W5-4 line 106 and
    Step 3 (mack inventory row) was already discharged at S91 W5-4; only
    Step 2 (canonical_constants.py write) is deferred.

All three upstream-block topologies pre-registered in
`sessions/session-plan/session-92-plan-w6.md §"Wave 6 Decision Point
Prerequisites"` row 28-30 + closing paragraph line 32 — the closure script's
emission is plan-anticipated (NOT post-hoc per mechanical-closure-discipline.md
§"When mechanical closure IS acceptable" item 1).

Modeled on `computations/session-92/s92_w3_pre_reg_inc_closure.py`
canonical pattern.

MCP pre-compute audit (mechanical-closure-discipline.md §"item 1"):
  search_knowledge("mechanical-closure-discipline upstream-block-topology")
    -> S88-MECHANICAL-CLOSURE-DISCIPLINE-LAYER-SEPARABILITY-CARVE-OUT-CLAUSE
       (FAIL/landed; corpus K=1)
  search_knowledge("PRE-REG-INC blocked by Stage-2 PASS-AND")
    -> S89-FOUR-CORNER-STAGE-2-CROSS-AXIS-VERIFY-DUAL-BASIS (PRE-REG-INC
       canonical), S91-W8-CF-68 (PRE-REG-INC canonical), S92 §W2-5 (PRE-REG-INC
       mechanical-closure precedent). Closure pattern is canonical.
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
VERDICT_TXT = PROJECT_ROOT / "computations" / "session-92" / "s92_gate_verdicts.txt"
CANONICAL_PY = PROJECT_ROOT / "computations" / "_shared" / "canonical_constants.py"
WP_PATH = PROJECT_ROOT / "sessions" / "session-92" / "session-92-w6-workingpaper.md"
JSON_OUT = PROJECT_ROOT / "computations" / "session-92" / "s92_w6_pre_reg_inc_closure.json"

sys.path.insert(0, str(PROJECT_ROOT / "computations" / "_shared"))
sys.path.insert(0, str(PROJECT_ROOT / "computations"))
from canonical_constants import *  # noqa: F401,F403,E402


# Upstream prereq Stage-2 cross-reviewer verdict-line gate IDs.
# §W6-3 is a TWO-AXIS Stage-2 cross-axis verify; the composite PASS-AND
# evaluates as `axis_a_PASS AND axis_b_PASS`. Both axes FAIL on disk; composite
# IS FAIL.
PREREQ_GATE_IDS = {
    "W6_3_AXIS_A": "S92-W6-CF-S92-W5-4-STAGE-2-VII-AX-CROSS-AXIS-VERIFY-AXIS-A",
    "W6_3_AXIS_B": "S92-W6-CF-S92-W5-4-STAGE-2-VII-AX-CROSS-AXIS-VERIFY-AXIS-B",
}

# Per-axis audit_sha256 (pinned for audit-traceability into closure value strings)
PREREQ_AXIS_A_AUDIT_SHA = "19662dc1544604e55f49280bd36d5a1e3862df381d0eb14f17b68ebc5b933cff"
PREREQ_AXIS_B_AUDIT_SHA = "f20bc3ad108dbfad15a698682c6dbc5adfd30eddf8efe5d31ff2b0e1662f29f8"


# Block-value strings (per closure-discipline item 2: descriptive, name blocking
# prereq + status). Same value string across all three closures because the
# blocking prereq is the same: §W6-3 PASS-AND impossible because BOTH Axis-A
# E2 FAIL AND Axis-B JE5 FAIL.
BLOCK_VALUE = (
    "PRE-REG-INC_blocked_by_S92-W6-CF-S92-W5-4-STAGE-2-VII-AX-CROSS-AXIS-VERIFY"
    "_PASS-AND-IMPOSSIBLE_axis_a_E2_FAIL_axis_b_JE5_FAIL"
)


W6_GATES = [
    {
        "gate_id":     "S92-W6-CF-S92-W5-4-VII-AX-STATE-PROJ-COMPANION-LANDING",
        "wp_id":       "W6-4",
        "carry_id":    "CF-S92-W5-4-STATE-PROJ-COMPANION",
        "scheme":      "mechanical-closure-discipline-upstream-block-topology-pre-registered",
        "convention":  "stage-1-candidate-state-proj-companion-landing-DEFERRED-pending-stage-2-pass-and",
        "L_max":       "N/A",
        "required":    ["W6_3_AXIS_A", "W6_3_AXIS_B"],
        "block_logic": "all_must_pass_and",
        "block_value": BLOCK_VALUE,
        "agent":       "mack-cosmic-bridge + connes-ncg-theorist (sole-writer + CO-SIGNER)",
        "supersedes_tag": None,
        "needs_sign_3tuple": False,
        "substrate_proj":  "STATE-PROJ companion (Cell IV; algebra-DEPENDENT × cardinality-cascade-pole)",
        "substrate_obs":   "⟨ψ_GGE-PBH|n_a^PBH|ψ_GGE-PBH⟩ state-pair functional",
        "block_reason":    (
            "§VII.AX.STATE-PROJ companion landing requires §VII.AX.OP-PROJ "
            "Stage-3-PERMANENT eligibility via §W6-3 PASS-AND. Stage-2 verdict "
            "is FAIL on both Axis-A and Axis-B; §VII.AX.OP-PROJ remains "
            "STAGE-1-CANDIDATE per `joint-theorem-promotion.md §\"Stage 2 FAIL "
            "criterion\"`. STATE-PROJ landing routes to next-session remediation."
        ),
    },
    {
        "gate_id":     "S92-W6-CF-S92-W5-4-FWD-C5-FORWARD-CALIBRATION-INSTANCES",
        "wp_id":       "W6-5",
        "carry_id":    "CF-S92-W5-4-FWD-C5",
        "scheme":      "mechanical-closure-discipline-upstream-block-topology-pre-registered",
        "convention":  "fwd-c5-k2-advancement-DEFERRED-pending-stage-2-pass-and",
        "L_max":       "N/A",
        "required":    ["W6_3_AXIS_A", "W6_3_AXIS_B"],
        "block_logic": "all_must_pass_and",
        "block_value": BLOCK_VALUE,
        "agent":       "mack-cosmic-bridge + volovik-superfluid-universe-theorist",
        "supersedes_tag": None,
        # §W6-5 is [SIGN] trigger → REQUIRES 3-tuple companion row
        "needs_sign_3tuple": True,
        "sign_3tuple": {
            "sign_verdict":      "N/A",
            "magnitude_verdict": "N/A",
            "regime_verdict":    "BREAKDOWN",
        },
        "substrate_proj":  "FWD-C5 K=2 advancement at cardinality-cascade-shoulder",
        "substrate_obs":   "n_PBH_shoulder(g) at substrate-distance-3 pole s=5",
        "block_reason":    (
            "FWD-C5 K=1 → K=2 advancement requires §VII.AX.OP-PROJ "
            "Stage-3-PERMANENT eligibility verdict at §W6-3. Stage-2 PASS-AND "
            "impossible (both axes FAIL); K=2 corpus row deferred to next "
            "session. K=3 forward target "
            "`S93-OR-LATER-FWD-C5-K3-MANDATORY-PROMOTION-DISTINCT-PILLAR-IX-"
            "LAB-OBSERVABLE-LANDING` remains pre-registered for S93+ multi-"
            "session completion."
        ),
    },
    {
        "gate_id":     "S92-W6-CF-S92-W5-4-CANONICAL-CONSTANTS-PROMOTION-N-PBH-FW-PENDING-STAGE-3",
        "wp_id":       "W6-6",
        "carry_id":    "CF-S92-W5-4-N-PBH-FW-PROMOTION",
        "scheme":      "mechanical-closure-discipline-upstream-block-topology-pre-registered",
        "convention":  "canonical-constants-promotion-n-pbh-fw-DEFERRED-pending-stage-2-pass-and",
        "L_max":       "N/A",
        "required":    ["W6_3_AXIS_A", "W6_3_AXIS_B"],
        "block_logic": "all_must_pass_and",
        "block_value": BLOCK_VALUE,
        "agent":       "orchestrator (direct-write to canonical_constants.py)",
        "supersedes_tag": None,
        "needs_sign_3tuple": False,
        "substrate_proj":  "canonical_constants.py promotion (Step 2 of canonical write-order)",
        "substrate_obs":   "n_PBH_FW_central = 7.2761e-23 m⁻³ (NOT written this session)",
        "block_reason":    (
            "`canonical_constants.py` promotion of n_PBH_FW_central requires "
            "§VII.AX.OP-PROJ Stage-3-PERMANENT eligibility verdict at §W6-3 "
            "PASS-AND. Stage-2 PASS-AND impossible (both axes FAIL); Step 2 "
            "of `math-scripts.md §\"Canonical Write-Order for New Framework "
            "Predictions\"` HALTED at prereq-block boundary. Step 1 "
            "(verdict-file emission) ALREADY discharged at S91 W5-4 line 106; "
            "Step 3 (mack inventory row) ALREADY discharged at S91 W5-4 per "
            "falsifier-master-inventory.md Row #65. Only Step 2 deferred to "
            "next session. CRITICAL: no `n_PBH_FW_central` entry is written "
            "to `computations/_shared/canonical_constants.py` by this closure "
            "script."
        ),
    },
]


def parse_prereq_verdicts() -> dict[str, tuple[str, str]]:
    """Parse latest verdict line for each prereq gate from s92_gate_verdicts.txt.

    Returns dict mapping prereq symbol -> (status, raw_value_snippet).
    """
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
        # snippet up to 60 chars from value=
        if "value=" in last:
            snip = last.split("value=", 1)[1][:60]
        else:
            snip = "no_value_field"
        states[sym] = (status, snip)
    return states


def compute_dual_sha(pinmap: dict[str, str]) -> tuple[str, str]:
    """Compute (audit_sha256, content_sha256) per W9a-99 split.

    audit_sha256 = sha256(script_bytes || canonical_constants_bytes || pinmap_json)
    content_sha256 = sha256(script_bytes)

    Per-gate pinmap distinct keys (_gate_id, _wp_id, _scheme, _convention)
    guarantee pairwise-distinct audit_sha256 across gates.
    """
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
    """S81+ canonical verdict line."""
    return (
        f"{gate['gate_id']}: FAIL -- value={value!r} "
        f"scheme={gate['scheme']} convention={gate['convention']} "
        f"L_max={gate['L_max']} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )


def make_companion_row(gate: dict, audit_sha: str, content_sha: str) -> str:
    """Dual-SHA companion comment row (W9a-99 split)."""
    req = ", ".join(gate["required"])
    return (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {gate['gate_id']} dual-SHA companion row (W9a-99 split); "
        f"PRE-REG-INC mechanical-closure per mechanical-closure-discipline.md 5-clause admissibility; "
        f"upstream prereqs: [{req}]; "
        f"closure_script=computations/session-92/s92_w6_pre_reg_inc_closure.py\n"
    )


def make_3tuple_row(gate: dict) -> str:
    """S87+ schema-v2 3-tuple companion row for [SIGN] trigger gates.

    Per `gate-verdicts.md §"Composite-collapse rule"`:
      regime_verdict == BREAKDOWN ⇒ composite = FAIL (regardless of other fields).
    sign_verdict=N/A and magnitude_verdict=N/A reflect the mechanical-closure
    nature: no substrate-physics computation performed; only the audit-trail
    block-by-prerequisite topology is reported.
    """
    t3 = gate["sign_3tuple"]
    return (
        f"# sign_verdict={t3['sign_verdict']} magnitude_verdict={t3['magnitude_verdict']} "
        f"regime_verdict={t3['regime_verdict']} "
        f"# {gate['gate_id']} 3-tuple annotation (S87 schema-v2); "
        f"mechanical-closure PRE-REG-INC blocked by upstream prereq §W6-3 "
        f"PASS-AND impossible (Axis-A E2 FAIL ∧ Axis-B JE5 FAIL)\n"
    )


def make_wp_block(gate: dict, value: str, states: dict, audit_sha: str, content_sha: str) -> str:
    """Build the §W6-N WP section replacement content (post-NOT-STARTED Status update)."""
    prereq_state_lines = []
    for sym in gate["required"]:
        stat, snip = states[sym]
        prereq_state_lines.append(
            f"  - `{sym}` ({PREREQ_GATE_IDS[sym]}): **{stat}**  \n"
            f"    audit_sha256=`"
            + (PREREQ_AXIS_A_AUDIT_SHA if sym == "W6_3_AXIS_A" else PREREQ_AXIS_B_AUDIT_SHA)
            + "`"
        )

    sign_3tuple_block = ""
    if gate.get("needs_sign_3tuple"):
        t3 = gate["sign_3tuple"]
        sign_3tuple_block = (
            f"\n**[SIGN] 3-tuple (S87 schema-v2)**:\n"
            f"  - `sign_verdict`: **{t3['sign_verdict']}** "
            f"(mechanical-closure: no directional pre-registration evaluated)\n"
            f"  - `magnitude_verdict`: **{t3['magnitude_verdict']}** "
            f"(mechanical-closure: no value-vs-threshold comparison performed)\n"
            f"  - `regime_verdict`: **{t3['regime_verdict']}** "
            f"(prereq-block renders substrate-physics computation undefined at "
            f"this dispatch; intended K=2 advancement window is fully outside "
            f"regime-of-validity at the §W6-3 PASS-AND blocking event)\n"
            f"  - **Composite collapse**: `regime_verdict == BREAKDOWN ⇒ "
            f"composite = FAIL` per `gate-verdicts.md §\"Composite-collapse "
            f"rule\"` — yields FAIL composite top-line.\n"
        )

    return (
        f"**Status**: PRE-REG-INCOMPLETE (mechanical closure 2026-05-23 per "
        f"mechanical-closure-discipline.md §\"When mechanical closure IS acceptable\" "
        f"5-clause admissibility; upstream §W6-3 PASS-AND impossible because BOTH "
        f"cross-reviewers FAIL on structurally distinct clauses)\n"
        f"\n"
        f"**Output Artifacts**:\n"
        f"\n"
        f"- Closure script: `computations/session-92/s92_w6_pre_reg_inc_closure.py` "
        f"(orchestrator-direct mechanical closure; no specialist-agent dispatch)\n"
        f"- JSON sidecar: `computations/session-92/s92_w6_pre_reg_inc_closure.json` "
        f"(per-gate verdict 4-tuple + dual-SHA + per-gate pinmap)\n"
        f"- Verdict line appended to `computations/session-92/s92_gate_verdicts.txt`\n"
        f"\n"
        f"**MCP Pre-Compute Audit**:\n"
        f"- `mcp__knowledge__search_knowledge(\"mechanical-closure-discipline upstream-block-topology\")` "
        f"→ S88-MECHANICAL-CLOSURE-DISCIPLINE-LAYER-SEPARABILITY-CARVE-OUT-CLAUSE (landed; K=1 corpus); "
        f"closure pattern is canonical for upstream-block topology.\n"
        f"- `mcp__knowledge__search_knowledge(\"PRE-REG-INC blocked by Stage-2 PASS-AND\")` "
        f"→ S89-FOUR-CORNER-STAGE-2-CROSS-AXIS-VERIFY-DUAL-BASIS (PRE-REG-INC canonical) + "
        f"S91-W8-CF-68 (PRE-REG-INC canonical, both-axes-FAIL precedent) + "
        f"S92 §W2-5 (PRE-REG-INC mechanical-closure precedent); pattern confirmed.\n"
        f"\n"
        f"**Verdict**: **FAIL** (PRE-REG-INC) — value=`{value}`\n"
        f"\n"
        f"**Results**:\n"
        f"\n"
        f"Mechanical PRE-REG-INC closure per mechanical-closure-discipline.md 5-clause "
        f"admissibility:\n"
        f"\n"
        f"1. **Upstream-block topology is the cause** ✓ — plan §\"Wave 6 Decision "
        f"Point Prerequisites\" row {gate['wp_id'][-1]} (block_logic=must_pass_and on "
        f"§W6-3 PASS-AND) + closing paragraph line 32 pre-registered the prereq-block "
        f"scenario for every chained gate. The closure is plan-anticipated, NOT post-"
        f"hoc plan editing (PROHIBITED_ACTIONS Class 3 does NOT apply).\n"
        f"2. **Verdict honesty: FAIL/PRE-REG-INC, never PASS** ✓ — emitted FAIL with "
        f"`PRE-REG-INC_blocked_by_S92-W6-CF-S92-W5-4-STAGE-2-VII-AX-CROSS-AXIS-VERIFY_"
        f"PASS-AND-IMPOSSIBLE_*` value string naming both axes' FAIL clauses.\n"
        f"3. **Per-gate-distinct audit_sha256** ✓ — pinmap embeds gate-distinct keys "
        f"(_gate_id, _wp_id, _scheme, _convention, _carry_id) so the three closure "
        f"verdict lines emitted by this script have pairwise-distinct audit_sha256 "
        f"(sig_5 ladder uniqueness preserved by construction).\n"
        f"4. **Audit-trail signature** ✓ — value names BOTH blocking axes "
        f"(`axis_a_E2_FAIL` + `axis_b_JE5_FAIL`) and both audit_sha256 are cross-"
        f"referenced in this WP block. A future audit script can grep this canonical "
        f"line + the prereq lines (167, 172) and verify the named upstream gates exist "
        f"with the named statuses.\n"
        f"5. **Working-paper update in-script** ✓ — this block is emitted in the same "
        f"Python process (`s92_w6_pre_reg_inc_closure.py main()`) as the verdict-line "
        f"append; no S82/S84 task-complete-lie pattern.\n"
        f"\n"
        f"**Required prerequisites and observed states**:\n"
        + "\n".join(prereq_state_lines) + "\n"
        f"\n"
        f"**block_logic**: `{gate['block_logic']}` — §W6-3 PASS-AND is computed as "
        f"`axis_a_PASS ∧ axis_b_PASS`. Observed: `FAIL ∧ FAIL = FAIL`. PASS-AND impossible.\n"
        f"\n"
        f"**Specific reason for block**: {gate['block_reason']}\n"
        f"{sign_3tuple_block}\n"
        f"**4-tuple**: `(value={value!r}, scheme={gate['scheme']}, "
        f"convention={gate['convention']}, L_max={gate['L_max']})`\n"
        f"\n"
        f"**Dual-SHA**:\n"
        f"  - `audit_sha256`: `{audit_sha}`\n"
        f"  - `content_sha256`: `{content_sha}`\n"
        f"\n"
        f"**Solution-space interpretation**: The intended structural target "
        f"({gate['substrate_proj']}) for substrate-IS observable "
        f"{gate['substrate_obs']} remains UNTESTED at this session — this is a "
        f"no-info outcome (NOT a corridor closure). Stage-3-PERMANENT eligibility "
        f"of §VII.AX.OP-PROJ at §W6-3 is the gating prerequisite; the FAILing "
        f"clauses on Axis-A (Element 2 OE-form structural rejection) and Axis-B "
        f"(JOINT Element 5 conjunct-lower-edge magnitude FAIL) route to next-session "
        f"remediation per `joint-theorem-promotion.md §\"Stage 2 FAIL criterion\"`. "
        f"Gate ID + dual-SHA + 4-tuple are recorded so the S93+ re-emission can be "
        f"audit-traced back to this PRE-REG-INC entry.\n"
        f"\n"
        f"**Substrate framing** (`phononic-framing.md §\"IS Space, Not IN Space\"`): "
        f"The substrate IS the finite spectral triple `(A_K, H_K, D_K(τ_fold = 0.190))` "
        f"at Pillar I; the cardinality-cascade-tail saturation regime at g ≥ "
        f"g_saturate = 143 IS the substrate's intrinsic Peter-Weyl multiplicity-"
        f"saturation regime; PBH detection at Pillar IX IS the laboratory-IN "
        f"measurement context. The substrate-IS observable this gate would have "
        f"interrogated ({gate['substrate_obs']}) remains substrate-IS — it is the "
        f"METHODOLOGY-FLOOR F-image (the verdict line, the registry slot, the "
        f"canonical_constants.py entry) that is PRE-REG-INC. The direction of "
        f"explanation is preserved: substrate-IS observable → bridge map (HKR-style "
        f"image; substrate-clock cancellation ∘ Friedrich-Bär saturation) → laboratory-IN "
        f"observable; only the methodology-floor verification ladder is deferred.\n"
        f"\n"
        f"**Closure mechanism**: orchestrator-authored mechanical closure NOT "
        f"specialist-agent dispatch per mechanical-closure-discipline.md scope clause "
        f"(\"Orchestrator-authored mechanical-closure scripts emit verdict lines "
        f"WITHOUT specialist-agent dispatch and WITHOUT physics computation\"). "
        f"Re-dispatch of {gate['agent']} for this gate is structurally pre-empted at "
        f"the §W6-3 PASS-AND boundary; the closure preserves the audit trail "
        f"honestly by recording the block-by-prerequisite topology rather than "
        f"running a substrate-physics computation downstream of an impossible "
        f"prerequisite.\n"
    )


def update_wp_section(wp_text: str, gate: dict, value: str, states: dict,
                      audit_sha: str, content_sha: str) -> str:
    """Replace the §W6-N NOT STARTED placeholder with the mechanical-closure block."""
    sect_marker = f"### §{gate['wp_id']}."
    sect_start = wp_text.index(sect_marker)
    # Find next section or end of file
    next_marker_section = "### §"
    next_marker_h2 = "\n## "
    search_from = sect_start + len(sect_marker)
    next_idx_section = wp_text.find(next_marker_section, search_from)
    next_idx_h2 = wp_text.find(next_marker_h2, search_from)
    candidates = [i for i in (next_idx_section, next_idx_h2) if i != -1]
    next_idx = min(candidates) if candidates else len(wp_text)

    old_section = wp_text[sect_start:next_idx]
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
    print("=== S92 W6 prerequisite verdict states (latest non-superseded line) ===")
    for sym, (status, _) in states.items():
        gate_id_ref = PREREQ_GATE_IDS[sym]
        expected_sha = PREREQ_AXIS_A_AUDIT_SHA if sym == "W6_3_AXIS_A" else PREREQ_AXIS_B_AUDIT_SHA
        print(f"  {sym:14} = {gate_id_ref:65} : {status}  (audit_sha256={expected_sha[:16]}...)")
    print()

    # Sanity: both axes MUST be FAIL for this closure to be admissible
    axis_a_status = states["W6_3_AXIS_A"][0]
    axis_b_status = states["W6_3_AXIS_B"][0]
    if axis_a_status == "PASS" and axis_b_status == "PASS":
        print("=== ABORT: §W6-3 PASS-AND verified PASS; mechanical closure NOT admissible. ===")
        print("    Re-dispatch the downstream §W6-4/5/6 gates as substrate-physics gates.")
        return 1
    if axis_a_status not in ("FAIL", "INFO", "ABSENT") or axis_b_status not in ("FAIL", "INFO", "ABSENT"):
        print(f"=== UNEXPECTED prereq states: axis_a={axis_a_status}, axis_b={axis_b_status} ===")
        return 2

    # Idempotency: check for existing verdict lines
    verdict_text = VERDICT_TXT.read_text(encoding="utf-8") if VERDICT_TXT.exists() else ""
    existing: dict[str, tuple[str, str]] = {}
    for gate in W6_GATES:
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
    json_records = []
    for gate in W6_GATES:
        # Build pinmap with gate-distinct keys
        pinmap = {
            "_gate_id":     gate["gate_id"],
            "_wp_id":       gate["wp_id"],
            "_carry_id":    gate["carry_id"],
            "_scheme":      gate["scheme"],
            "_convention":  gate["convention"],
            "_block_logic": gate["block_logic"],
            "_value":       gate["block_value"],
            "_substrate_proj": gate["substrate_proj"],
            "_substrate_obs":  gate["substrate_obs"],
        }
        for sym in gate["required"]:
            stat, _ = states[sym]
            expected_sha = PREREQ_AXIS_A_AUDIT_SHA if sym == "W6_3_AXIS_A" else PREREQ_AXIS_B_AUDIT_SHA
            pinmap[sym] = f"{PREREQ_GATE_IDS[sym]}={stat};audit_sha256={expected_sha}"
        if gate.get("supersedes_tag"):
            pinmap["_supersedes"] = gate["supersedes_tag"]
        if gate.get("needs_sign_3tuple"):
            t3 = gate["sign_3tuple"]
            pinmap["_sign_3tuple"] = f"sign={t3['sign_verdict']};mag={t3['magnitude_verdict']};reg={t3['regime_verdict']}"

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
        json_records.append({
            "gate_id":     gate["gate_id"],
            "wp_id":       gate["wp_id"],
            "verdict":     "FAIL",
            "value":       gate["block_value"],
            "scheme":      gate["scheme"],
            "convention":  gate["convention"],
            "L_max":       gate["L_max"],
            "audit_sha256":   audit_sha,
            "content_sha256": content_sha,
            "pinmap":      pinmap,
            "prereq_states": {sym: states[sym][0] for sym in gate["required"]},
            "prereq_audit_shas": {
                "W6_3_AXIS_A": PREREQ_AXIS_A_AUDIT_SHA,
                "W6_3_AXIS_B": PREREQ_AXIS_B_AUDIT_SHA,
            },
            "needs_sign_3tuple": gate.get("needs_sign_3tuple", False),
        })

    # Pairwise SHA distinctness verification (sig_5 ladder uniqueness)
    audit_shas = [a for _, a, _ in emitted]
    if len(set(audit_shas)) != len(audit_shas):
        print("=== ERROR: audit_sha256 are NOT pairwise distinct ===")
        for g, a, _ in emitted:
            print(f"  {g['gate_id']}: {a}")
        return 3
    print(f"\n=== Pairwise audit_sha256 distinctness verified across {len(audit_shas)} gates ===")

    # Append verdict lines (atomic POSIX O_APPEND)
    if to_append:
        print(f"\n=== Appending {len(to_append)} verdict + companion-row groups ===")
        with VERDICT_TXT.open("a", encoding="utf-8") as fp:
            for gate, audit_sha, content_sha in to_append:
                fp.write(make_verdict_line(gate, gate["block_value"], audit_sha, content_sha))
                fp.write(make_companion_row(gate, audit_sha, content_sha))
                if gate.get("needs_sign_3tuple"):
                    fp.write(make_3tuple_row(gate))

    # Update WP sections
    print("\n=== Updating W6 working-paper sections ===")
    wp_text = WP_PATH.read_text(encoding="utf-8")
    for gate, audit_sha, content_sha in emitted:
        sect_start = wp_text.index(f"### §{gate['wp_id']}.")
        sect_peek_end = min(sect_start + 200, len(wp_text))
        if "**Status**: PRE-REG-INCOMPLETE (mechanical closure" in wp_text[sect_start:sect_peek_end]:
            print(f"  skipped WP §{gate['wp_id']} — already mechanical-closed (idempotent)")
            continue
        wp_text = update_wp_section(wp_text, gate, gate["block_value"], states,
                                    audit_sha, content_sha)
        print(f"  updated WP §{gate['wp_id']} ({gate['gate_id']})")
    WP_PATH.write_text(wp_text, encoding="utf-8")
    print(f"\n=== Wrote {WP_PATH.relative_to(PROJECT_ROOT)} ===")

    # Emit JSON sidecar
    json_payload = {
        "session": "S92",
        "wave": "W6",
        "closure_script": "computations/session-92/s92_w6_pre_reg_inc_closure.py",
        "prereq_gates": PREREQ_GATE_IDS,
        "prereq_audit_shas": {
            "W6_3_AXIS_A": PREREQ_AXIS_A_AUDIT_SHA,
            "W6_3_AXIS_B": PREREQ_AXIS_B_AUDIT_SHA,
        },
        "prereq_states": {sym: status for sym, (status, _) in states.items()},
        "pass_and_status": "FAIL_BOTH_AXES_FAIL",
        "block_value_canonical": BLOCK_VALUE,
        "gates_closed": json_records,
        "pairwise_sha_distinct": True,
    }
    JSON_OUT.write_text(json.dumps(json_payload, indent=2), encoding="utf-8")
    print(f"=== Wrote {JSON_OUT.relative_to(PROJECT_ROOT)} ===")

    print(f"\n=== S92-W6-PRE-REG-INC-CLOSURE: {len(emitted)} gates closed PRE-REG-INC ===")
    print(f"   §W6-4 (STATE-PROJ companion landing): DEFERRED to S93+")
    print(f"   §W6-5 (FWD-C5 K=2 advancement):       DEFERRED to S93+ ([SIGN]-trigger)")
    print(f"   §W6-6 (canonical_constants promotion): DEFERRED to S93+ (canonical_constants.py NOT written)")
    print(f"\n   §VII.AX.OP-PROJ STAGE-1-CANDIDATE status PRESERVED; STAGE-3-PERMANENT promotion BLOCKED.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
