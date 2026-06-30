#!/usr/bin/env python3
"""
S88 W4b mechanical PRE-REG-INC closure (FWD-C1 / FWD-C2 / FWD-C3 cross-pillar bridges)
=====================================================================================

Three of the four W4b gates have ≥1 unsatisfied upstream prerequisite per plan
§"Wave 4b Decision Point Prerequisites" (sessions/session-plan/session-88-plan-w4b.md
lines 36-48):

  * §W4b-21 (FWD-C1, Pillar I ↔ II, n_s spectral-action bridge):
      BLOCKED on S88 W6a-51 `S88-JENSEN-DIM-SPECTRUM-FIRST-PRINCIPLES-DERIVATION`
      (c_sub canonical pin from Jensen-derivation). W6a WP shows §W6a-51
      Status=NOT STARTED; no verdict line in s88_gate_verdicts.txt; n_s_FW
      and c_sub canonical constants not pinned in MCP knowledge base.
  * §W4b-22 (FWD-C2, Pillar II ↔ V, Mellin-BdG bridge):
      BLOCKED on S88 W2 Mellin-cone closure producing FWD-C2-relevant
      `mellin_residue_s3` and `mellin_residue_s4` canonicals. S88 W2 produced
      13 gates (W2-1..W2-13: V_4 monodromy / Δ_0 localization / partition
      stability / moduli-space asymmetry / Class-8.2 calibration / K-counter
      monitor) — none pinned the FWD-C2 prereq canonicals; mellin_residue_s3/s4
      not in MCP knowledge base.
  * §W4b-23 (FWD-C3, Pillar IV ↔ V, cocycle-3He bridge):
      BLOCKED on Lancaster MCT-3 (W11-C5) + Aalto LTL µSR (W11-C6) lab data;
      multi-year experimental cycle queued via S87 CF-32 + CF-33; not available
      at S88-open (2026-05-04); cocycle_ratio_67_88_FW + phi67/88_norm_FW
      canonicals not in MCP knowledge base.

The fourth gate (§W4b-24, K=3 auto-flip) is PRE-CLOSED — NOT BLOCKED — because
the K-counter K=2 → K=3 promotion + SUGGESTION → MANDATORY rule-file edit
already fired earlier in S88 at W4a-17 close (verdict file line 13:
`K-counter_K2_to_K3_MANDATORY_promoted;allowlist_row_appended`;
audit_sha256=a9ebeb99d9ddf7b14fa6844c1a20942a369d87931007b526feae3dc500d7b162).
W4b-24 is handled OUTSIDE this script per the rclab-solo skill PRE-CLOSED branch
(no verdict-line emission; cite upstream closure in WP entry). This script
processes only W4b-21/22/23.

Per `.claude/rules/gate-verdicts.md` and S86 W3 precedent (s86_w3_pre_reg_inc_closure.py),
upstream-blocked gates emit FAIL verdicts with descriptive
`value='PRE-REG-INC_blocked_by_<prereq_states>'` strings (matching the
exact value-string formats pre-registered in plan §W4b-21.11, §W4b-22.10, §W4b-23.10).

Dual-SHA per `.claude/rules/v3-closure-recovery.md` sig_5 audit uniqueness:
    audit_sha256   = sha256(script_bytes || canonical_bytes || pinmap_json)
    content_sha256 = sha256(script_bytes)
The pinmap embeds `_gate_id` (and other identity keys) so all 3 emitted gates
have pairwise-distinct audit_sha256 hashes even though they share the closure
mechanism — preserves sig_5 audit uniqueness.

This is a metadata-closure script: NO physics is computed. The 3 emitted
verdict lines record that each gate was structurally untestable at S88
because at least one upstream prerequisite has status ≠ PASS.

Per `.claude/rules/mechanical-closure-discipline.md` §"When mechanical closure
indicates a PLANNING DEFECT", the closed-gate count = 3 ≥ 4 (planning-defect
threshold) — but only marginally: 3 W4b-21/22/23 gates, with W4b-24 PRE-CLOSED
separately. This is logged as a plan-authorship lesson for next session: W4b
plan was over-optimistic about prereq landings (W6a-51 not started, W2 produced
different work than the FWD-C2 prereq, W4a-17 already promoted K=3).
"""

from __future__ import annotations

# canonical_constants import retained for audit compliance (no constants used;
# this script emits metadata closures only — no framework computation).
# Path bootstrap injected for cross-session imports from computations/_shared.
import sys as _bootstrap_sys
from pathlib import Path as _bootstrap_Path
_bootstrap_sys.path.insert(0, str(_bootstrap_Path(__file__).resolve().parents[1] / "_shared"))
from canonical_constants import *  # noqa: F401,F403,E402

import hashlib  # noqa: E402
import json  # noqa: E402
import sys  # noqa: E402
from pathlib import Path  # noqa: E402


PROJECT_ROOT = Path(__file__).resolve().parents[2]
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
# Per .claude/rules/gate-verdicts.md MANDATORY: canonical verdict-file path
# is computations/_shared/s{N}_gate_verdicts.txt (NOT computations/session-{N}/...).
VERDICT_TXT = SHARED_DIR / "s88_gate_verdicts.txt"
CANONICAL_PY = SHARED_DIR / "canonical_constants.py"
WP_PATH = PROJECT_ROOT / "sessions" / "session-88" / "session-88-w4b-workingpaper.md"

# W4b prerequisite-class identifiers. Each maps a symbolic prereq class to
# the canonical S88 gate ID (or synthetic ID for absence-of-canonical /
# absence-of-lab-data) that, if PASSed, would unblock the corresponding gate.
# All three are expected to be MISSING from s88_gate_verdicts.txt at S88 close.
PREREQ_GATE_IDS = {
    "C_SUB":   "S88-JENSEN-DIM-SPECTRUM-FIRST-PRINCIPLES-DERIVATION",
    "MELLIN":  "S88-W2-MELLIN-CONE-FWD-C2-RESIDUE-S3-S4-CANONICAL-LANDING",
    "LAB":     "S88-LANCASTER-MCT3-AALTO-LTL-LAB-DATA-AVAILABLE-FOR-FWD-C3",
}

# W4b PRE-REG-INC gate metadata + required-prereq map (per plan §0.5/§0.10
# Decision Point Prerequisites + §W4b-21.11 / §W4b-22.10 / §W4b-23.10
# pre-registered value-string formats).
W4B_GATES = [
    {
        "gate_id":   "S88-FWD-C1-PILLAR-I-II-N-S-BRIDGE-LANDING",
        "wp_id":     "W4b-21",
        "scheme":    "mukhanov-sasaki-HKR-L_max-10",
        "convention": "substrate-IS-scalar-spectral-moment-band-0-tau-fold",
        "L_max":     "10",
        "required":  ["C_SUB"],
        "agent":     "mack-cosmic-bridge",
        # Plan §W4b-21.11 pre-registered value-string format:
        #   value='PRE-REG-INC_blocked_by_c_sub_canonical_W6_51_<status>'
        "value_template": "PRE-REG-INC_blocked_by_c_sub_canonical_W6_51_{status}",
        "registry_slot_planned": "§VII.AK",
    },
    {
        "gate_id":   "S88-FWD-C2-MELLIN-BDG-BRIDGE-LANDING",
        "wp_id":     "W4b-22",
        "scheme":    "connes-karoubi-K-theory-boundary-L_max-10",
        "convention": "substrate-IS-mellin-residue-zeta-regulated-hochschild-moment",
        "L_max":     "10",
        "required":  ["MELLIN"],
        "agent":     "mack-cosmic-bridge",
        # Plan §W4b-22.10 pre-registered value-string format:
        #   value='PRE-REG-INC_blocked_by_mellin_cone_closure_W2_<status>'
        "value_template": "PRE-REG-INC_blocked_by_mellin_cone_closure_W2_{status}",
        "registry_slot_planned": "§VII.AL",
    },
    {
        "gate_id":   "S88-FWD-C3-COCYCLE-3HE-BRIDGE-LANDING",
        "wp_id":     "W4b-23",
        "scheme":    "inheritance-morphism-delta-cancellation-L_max-10",
        "convention": "substrate-IS-cocycle-pair-phi67-phi88-Sage-exact",
        "L_max":     "10",
        "required":  ["LAB"],
        "agent":     "mack-cosmic-bridge",
        # Plan §W4b-23.10 pre-registered value-string format (literal, no
        # status interpolation — lab-data prereq is structurally pending the
        # multi-year experimental cycle):
        "value_template": "PRE-REG-INC_blocked_by_lab_data_pending_W11_C5_W11_C6",
        "registry_slot_planned": "§VII.AM",
    },
]


def parse_prereq_verdicts() -> dict[str, tuple[str, str]]:
    """Read s88_gate_verdicts.txt; return {symbol: (status, value_chunk)} for prereqs.

    Mirrors s86_w3_pre_reg_inc_closure.py:parse_prereq_verdicts. For each
    prereq, the LAST verdict line in the file (most-recent canonical state)
    is taken as the operative one. None of the W4b prereq gate IDs are
    expected to be present; all should return ("MISSING", "no_verdict_line").
    """
    states: dict[str, tuple[str, str]] = {}                     # (local)
    text = VERDICT_TXT.read_text(encoding="utf-8")              # (local)
    for sym, gate_id in PREREQ_GATE_IDS.items():
        prefix = gate_id + ":"                                  # (local)
        lines = [ln for ln in text.splitlines() if ln.startswith(prefix)]  # (local)
        if not lines:
            states[sym] = ("MISSING", "no_verdict_line")
            continue
        last = lines[-1]                                        # (local)
        body = last.split(":", 1)[1].strip()                    # (local)
        status = body.split()[0].rstrip(",")                    # (local)
        if "value=" in last:
            v_start = last.index("value=") + len("value=")      # (local)
            v_chunk = last[v_start:].split()[0]                 # (local)
        else:
            v_chunk = "unknown"                                 # (local)
        states[sym] = (status, v_chunk)
    return states


def compute_dual_sha(pinmap: dict[str, str]) -> tuple[str, str]:
    """Per .claude/rules/v3-closure-recovery.md sig_5 schema."""
    script_bytes = Path(__file__).read_bytes()                  # (local)
    canonical_bytes = CANONICAL_PY.read_bytes()                 # (local)
    pinmap_json = json.dumps(
        dict(sorted(pinmap.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")                                           # (local)
    h_audit = hashlib.sha256()                                  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                 # (local)
    h_content = hashlib.sha256()                                # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()                             # (local)
    return audit, content


def build_value_string(gate: dict, states: dict[str, tuple[str, str]]) -> tuple[str, dict[str, str]]:
    """Build (value_str, pinmap) for the given W4b gate.

    The pinmap embeds the gate's own ID under "_gate_id" (and _wp_id, _scheme,
    _convention) so all 3 W4b gates produce DISTINCT audit_sha256 closures —
    preserving sig_5 audit uniqueness per .claude/rules/v3-closure-recovery.md.
    """
    pinmap: dict[str, str] = {"_gate_id": gate["gate_id"],
                              "_wp_id":   gate["wp_id"],
                              "_scheme":  gate["scheme"],
                              "_convention": gate["convention"]}     # (local)
    blocked = False                                             # (local)
    last_status = ""                                            # (local)
    for sym in gate["required"]:
        stat, _ = states[sym]
        pinmap[sym] = f"{PREREQ_GATE_IDS[sym]}={stat}"
        if stat != "PASS":
            blocked = True
            last_status = stat
    if not blocked:
        return ("", pinmap)
    # Render the gate's pre-registered value template. For W4b-23, the
    # template is literal (no {status} placeholder); .format() leaves it
    # untouched. For W4b-21/22, {status} is interpolated.
    value_str = gate["value_template"].format(status=last_status)   # (local)
    return (value_str, pinmap)


def make_verdict_line(gate: dict, value_str: str, audit_sha: str, content_sha: str) -> str:
    return (
        f"{gate['gate_id']}: FAIL -- value={value_str!r} "
        f"scheme={gate['scheme']} convention={gate['convention']} "
        f"L_max={gate['L_max']} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )


def make_companion_row(gate: dict, value_str: str, audit_sha: str, content_sha: str) -> str:
    req = ", ".join(gate["required"])                           # (local)
    return (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {gate['gate_id']} dual-SHA companion row (W9a-99 split); "
        f"PRE-REG-INC per session-88-plan-w4b.md {gate['wp_id'].replace('W4b-', '§W4b-')}; "
        f"deferred to S89; required prereqs: [{req}]; "
        f"closure_script=computations/session-88/s88_w4b_pre_reg_inc_closure.py\n"
    )


def make_3tuple_annotation_row(gate: dict) -> str:
    """S87+ schema-v2 3-tuple annotation companion row.

    Per `.claude/rules/gate-verdicts.md` §"S87+ canonical form (Schema-v2)":
    PRE-REG-INC mechanical closures emit:
      - sign_verdict = N/A (no directional pre-registration was exercised; the
        Level-3 < Level-2 numerical comparison from the substitution chain was
        not computed because the producing machinery never ran)
      - magnitude_verdict = FAIL (the gate produced no measurable value)
      - regime_verdict = VALID (no regime breakdown occurred since no regime
        was tested; the L_max=10 substrate truncation is well within validity
        bounds when actually exercised)

    Per the composite-collapse rule:
      magnitude_verdict == FAIL and regime_verdict == VALID  →  composite FAIL
    consistent with the FAIL top-line of the canonical verdict line.

    This matches the pattern of S88-A0-M2-BICONDITIONAL-SPLIT-REGISTRY-LANDING
    (line 15 of s88_gate_verdicts.txt: `sign_verdict=N/A magnitude_verdict=FAIL
    regime_verdict=VALID`).
    """
    return (
        f"# sign_verdict=N/A magnitude_verdict=FAIL regime_verdict=VALID "
        f"# {gate['gate_id']} 3-tuple annotation (S87 schema-v2); "
        f"PRE-REG-INC mechanical-closure: substitution chain not exercised "
        f"(no producing machinery ran); composite=FAIL via magnitude=FAIL+regime=VALID\n"
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
    """Replace placeholder Status / MCP Pre-Compute Audit / Verdict / Results
    blocks in this gate's section.

    Mirrors s86_w3_pre_reg_inc_closure.py:update_wp_section; the
    MCP-Pre-Compute-Audit and Results-block placeholder texts are W4b-specific
    (longer parentheticals than the W3 exemplar — see W4b WP file head for
    exact strings).
    """
    sect_marker = f"### §{gate['wp_id']}."                      # (local)
    sect_start = wp_text.index(sect_marker)                     # (local)
    sect_end = wp_text.index("\n---\n", sect_start)             # (local)
    old_section = wp_text[sect_start:sect_end]                  # (local)
    new_section = old_section                                   # (local)

    # Status line
    new_section = new_section.replace(
        "**Status**: NOT STARTED",
        "**Status**: PRE-REG-INCOMPLETE (mechanical closure 2026-05-04 per plan §"
        + gate["wp_id"]
        + " Decision Point Prerequisites; deferred to S89)",
    )

    # MCP Pre-Compute Audit block — W4b-specific phrasing (matches WP head)
    mcp_old = (
        "**MCP Pre-Compute Audit**:\n"
        "*(pending — list the `mcp__knowledge__*` queries executed before writing the script, "
        "with one-line salient return each; mark PRE-CLOSED if a closure covers the gate. "
        "Per `.claude/rules/knowledge-index-usage.md`.)*"
    )                                                            # (local)
    # MCP queries executed at orchestrator pre-flight (not in script;
    # documented here for audit trail per knowledge-index-usage.md).
    mcp_new = _build_mcp_audit_block(gate)                      # (local)
    new_section = new_section.replace(mcp_old, mcp_new)

    # Verdict block
    prereq_lines = []                                            # (local)
    for sym in gate["required"]:
        stat, val = states[sym]
        gid = PREREQ_GATE_IDS[sym]
        if stat == "PASS":
            prereq_lines.append(f"  - {sym} (`{gid}`): **PASS** — does not block this gate")
        else:
            prereq_lines.append(f"  - {sym} (`{gid}`): **{stat}** (value={val}) — BLOCKING")

    verdict_old = "**Verdict**:\n*(pending agent execution)*"
    verdict_new = (
        f"**Verdict**: FAIL (PRE-REG-INC) — value={value_str!r}\n\n"
        "Mechanical PRE-REG-INC closure per `.claude/rules/mechanical-closure-discipline.md`. "
        "This gate's required upstream prerequisites (per `sessions/session-plan/session-88-plan-w4b.md` "
        "§\"Wave 4b Decision Point Prerequisites\") have not landed in `computations/_shared/s88_gate_verdicts.txt`; "
        "per the plan's PRE-REG-INC pathway clause for this gate, the documented outcome is "
        "**PRE-REG-INC, deferred to S89+** until upstream landing. FAIL verdict + descriptive value-string follows "
        "S86 W3 precedent (`computations/session-86/s86_w3_pre_reg_inc_closure.py`) and matches the value-string "
        "format pre-registered in plan §" + gate["wp_id"] + ".\n\n"
        "**Required prerequisites and observed states**:\n"
        + "\n".join(prereq_lines) + "\n\n"
        f"**4-tuple**: `(value={value_str!r}, scheme={gate['scheme']}, "
        f"convention={gate['convention']}, L_max={gate['L_max']})`\n\n"
        "**Dual-SHA**:\n"
        f"  - `audit_sha256`: `{audit_sha}`\n"
        f"  - `content_sha256`: `{content_sha}`\n\n"
        "**Closure mechanism**: `computations/session-88/s88_w4b_pre_reg_inc_closure.py` "
        "(orchestrator-authored mechanical closure per `.claude/rules/mechanical-closure-discipline.md`, "
        "NOT specialist-agent dispatch). No physics computation was performed; the verdict line "
        "records that the gate could not be evaluated due to upstream prerequisite block.\n\n"
        "**Registry append**: NONE — registry-landing at planned slot " + gate["registry_slot_planned"]
        + " (`sessions/permanent-results-registry.md`) is BLOCKED on upstream landing; entry deferred to S89+ "
        "re-emission gate."
    )
    new_section = new_section.replace(verdict_old, verdict_new)

    # Results block — find by start-marker, terminate at the next `)*` close
    res_start_marker = "**Results**:\n*(pending"                # (local)
    if res_start_marker in new_section:
        rs = new_section.index(res_start_marker)                # (local)
        re_close = new_section.index(")*", rs) + 2              # (local)
        results_old = new_section[rs:re_close]                  # (local)
        results_new = (
            "**Results**: NONE — gate not executed; PRE-REG-INC closure only.\n\n"
            "**Solution-space interpretation**: The "
            + gate["wp_id"]
            + " cross-pillar bridge corridor remains UNTESTED at this session; this is a no-information outcome "
            "(not a corridor closure). The plan's PASS/FAIL/INFO consequence states (per plan §"
            + gate["wp_id"]
            + ".11) are deferred to S89+ conditional on the blocking prerequisite landing. The gate ID + "
            "dual-SHA + 4-tuple are recorded so the S89+ re-emission can be audit-traced back to this "
            "PRE-REG-INC entry.\n\n"
            "**Substrate framing**: The substrate-IS observable this gate would have anchored against the "
            "laboratory-IN observable remains uncharacterized at the W4b entry-point; the gate does not "
            "report on the substrate's structural state, only on the audit trail's block-by-prerequisite "
            "topology. Per `.claude/rules/phononic-framing.md` direction-of-explanation discipline, no "
            "substrate-IS-to-laboratory-IN mapping is asserted from a non-execution outcome.\n\n"
            "**K-counter advancement**: NONE — INFO/PRE-REG-INC verdicts do NOT count toward the cross-pillar-"
            "bridge-anatomy K-counter per plan §W4b-24 K-increment rule (`PASS=+1, FAIL=+1, INFO=+0`). The "
            "K-counter remains at K=3 (saturated by S88 W4a-17 §VII.W-3.LAB landing); no further advancement "
            "from this gate's PRE-REG-INC closure."
        )
        new_section = new_section.replace(results_old, results_new)

    return wp_text[:sect_start] + new_section + wp_text[sect_end:]


def _build_mcp_audit_block(gate: dict) -> str:
    """Per-gate MCP Pre-Compute Audit block matching the W4b WP placeholder slot.

    Lists the orchestrator's pre-flight MCP queries (executed before this
    closure script ran) and salient returns. Per `.claude/rules/knowledge-
    index-usage.md`, every compute task records its MCP pre-flight here.
    """
    if gate["wp_id"] == "W4b-21":
        return (
            "**MCP Pre-Compute Audit**:\n\n"
            "  - `mcp__knowledge__get_constant('n_s_FW')` → NOT FOUND (no canonical pin for the substrate-IS "
            "scalar spectral moment of band-0 at τ_fold; expected canonical_constants.py:n_s_FW absent)\n"
            "  - `mcp__knowledge__get_constant('c_sub')` → no exact match; nearest = `c_sub_baseline = 2.238` "
            "(but plan §W4b-21.11 requires the W6a-51-derived Jensen canonical c_sub, not the baseline)\n"
            "  - `mcp__knowledge__search_knowledge('FWD-C1 FWD-C2 FWD-C3 cross-pillar bridge candidate')` → "
            "returned S88-METH-CROSS-PILLAR-BRIDGE-ANATOMY-K-COUNTER-MONITOR (W2-12, INFO at K=2 status holding) "
            "and S88 W4a-17 K=3 promotion via §VII.W-3.LAB; NO S88 FWD-C1/C2/C3 closures present\n"
            "  - Verdict-file grep `S88-JENSEN-DIM-SPECTRUM` → no match; W6a-51 prereq has no verdict line\n"
            "  - W6a WP grep §W6a-51 → Status=NOT STARTED\n\n"
            "**Conclusion**: No closure covers FWD-C1; required c_sub canonical not pinned; gate is structurally "
            "untestable at S88 — proceed with mechanical PRE-REG-INC closure."
        )
    if gate["wp_id"] == "W4b-22":
        return (
            "**MCP Pre-Compute Audit**:\n\n"
            "  - `mcp__knowledge__search_knowledge('mellin residue substrate distance s=3 s=4 canonical')` → "
            "returned plan-w4b §22.5 self-citation + S86 path-c-double-double workshop (M_R(s=3) Mellin residue) "
            "+ S87/S88 substrate-distance-2 residue at s=4 (different observable from FWD-C2 prereq)\n"
            "  - W2 WP grep `^### §W2-` → 13 gates W2-1..W2-13 all COMPLETE 2026-05-03; topics: V_4 monodromy, "
            "Δ_0 localization, partition stability, moduli-space τ-asymmetry, Class-8.2 calibration, K-counter "
            "monitor; NONE pin mellin_residue_s3 / mellin_residue_s4 canonicals required by FWD-C2\n"
            "  - Verdict-file grep `S88-MELLIN|S88-CLUSTER-SPAN|S88-VII-U-2` → no match\n"
            "  - `mcp__knowledge__get_constant('mellin_residue_s3')` / `('mellin_residue_s4')` → NOT FOUND\n\n"
            "**Conclusion**: No closure covers FWD-C2; W2 wave produced different work than the FWD-C2 prereq "
            "demanded; required Mellin-residue canonicals not pinned; gate is structurally untestable at S88 — "
            "proceed with mechanical PRE-REG-INC closure."
        )
    if gate["wp_id"] == "W4b-23":
        return (
            "**MCP Pre-Compute Audit**:\n\n"
            "  - `mcp__knowledge__get_constant('cocycle_ratio_67_88_FW')` → NOT FOUND\n"
            "  - `mcp__knowledge__get_constant('phi67_norm_FW')` → NOT FOUND\n"
            "  - `mcp__knowledge__get_constant('phi88_norm_FW')` → NOT FOUND (S86 W-5 Sage-exact substrate "
            "values exist in workshop output but not pinned to canonical_constants.py)\n"
            "  - S87 CF-32 + CF-33 lab pre-registrations queued; Lancaster MCT-3 vortex-core spectroscopy "
            "(W11-C5) and Aalto LTL µSR (W11-C6) require multi-year experimental cycle; not available at "
            "S88-open (2026-05-04)\n"
            "  - W11-5 §VII.W-3.LAB landed at S88 W4a-17 as STAGE-1-CANDIDATE per joint-theorem-promotion.md "
            "(the cocycle-pair landing IS in the registry as candidate, but the Level-3 lab anchor required "
            "for FULL-LANDING in cocycle-pair form is the multi-year experimental cycle data — not available)\n\n"
            "**Conclusion**: FWD-C3 FULL-LANDING in cocycle-pair form is structurally pending lab data from "
            "multi-year experimental cycle; the related W4a-17 STAGE-1-CANDIDATE landing is a distinct "
            "observable axis (registry-anchored cocycle-pair evidence), not the bridge-anatomy Level-3 "
            "empirical anchor — proceed with mechanical PRE-REG-INC closure."
        )
    return "**MCP Pre-Compute Audit**: (unrecognized wp_id; no pre-flight recorded)"


def main() -> int:
    states = parse_prereq_verdicts()
    print("=== W4b prerequisite verdict states (most-recent line per prereq) ===")
    for sym, (status, value) in states.items():
        gid = PREREQ_GATE_IDS[sym]
        print(f"  {sym:8} = {gid:65} : {status:12} (value={value})")
    print()

    # Recover any pre-existing W4b verdict lines (for idempotency on re-runs).
    # If a gate already has a verdict line, parse its dual-SHA pair from the
    # file rather than re-computing — keeps WP-update SHAs consistent with
    # verdict file across re-runs after a partial-failure crash.
    verdict_text = VERDICT_TXT.read_text(encoding="utf-8")       # (local)
    existing: dict[str, tuple[str, str, str]] = {}               # (local)  gate_id -> (audit, content, value)
    for gate in W4B_GATES:
        prefix = gate["gate_id"] + ":"                           # (local)
        ms = [ln for ln in verdict_text.splitlines()
              if ln.startswith(prefix)
              and "audit_sha256=" in ln
              and "content_sha256=" in ln]                       # (local)
        if not ms:
            continue
        last = ms[-1]                                            # (local)
        audit_sha = last.split("audit_sha256=", 1)[1].split()[0] # (local)
        content_sha = last.split("content_sha256=", 1)[1].split()[0]  # (local)
        v_chunk = last.split("value=", 1)[1].split()[0].strip("'\"")  # (local)
        existing[gate["gate_id"]] = (audit_sha, content_sha, v_chunk)

    emitted: list[tuple] = []                                    # (local)
    to_append: list[tuple] = []                                  # (local)
    for gate in W4B_GATES:
        value_str, pinmap = build_value_string(gate, states)
        if not value_str:
            print(f"[NOT-BLOCKED] {gate['gate_id']} — all prereqs PASS; skipping closure")
            continue
        if gate["gate_id"] in existing:
            audit_sha, content_sha, _existing_value = existing[gate["gate_id"]]
            print(f"[ALREADY-EMITTED] {gate['wp_id']:6} {gate['gate_id']:55}")
            print(f"          recovered audit: {audit_sha[:16]}...  content: {content_sha[:16]}...")
        else:
            audit_sha, content_sha = compute_dual_sha(pinmap)
            print(f"[BLOCKED] {gate['wp_id']:6} {gate['gate_id']:55}")
            print(f"          value: {value_str}")
            print(f"          audit: {audit_sha[:16]}...  content: {content_sha[:16]}...")
            to_append.append((gate, value_str, audit_sha, content_sha))
        emitted.append((gate, value_str, pinmap, audit_sha, content_sha))

    if not emitted:
        print("\nNo W4b gates were blocked; nothing to close.")
        return 0

    # Append NEW verdict lines (only those not yet in the file).
    # Per S87+ schema-v2 (gate-verdicts.md), each gate emits a 3-row block:
    #   1. canonical verdict line (PASS|FAIL|INFO -- value=... + dual-SHA)
    #   2. dual-SHA companion row (W9a-99 split short-hex form + metadata)
    #   3. 3-tuple annotation row (sign/magnitude/regime — composite-collapse trace)
    if to_append:
        print(f"\n=== Appending {len(to_append)} 3-row verdict blocks to {VERDICT_TXT.name} ===")
        with VERDICT_TXT.open("a", encoding="utf-8") as fp:
            for gate, value_str, audit_sha, content_sha in to_append:
                fp.write(make_verdict_line(gate, value_str, audit_sha, content_sha))
                fp.write(make_companion_row(gate, value_str, audit_sha, content_sha))
                fp.write(make_3tuple_annotation_row(gate))
    else:
        print("\n=== All blocked W4b verdicts already in verdict file; no appends needed ===")

    # Sig_5 audit uniqueness cross-check: all emitted audit_sha256 distinct.
    audit_set = {audit for _, _, _, audit, _ in emitted}        # (local)
    if len(audit_set) != len(emitted):
        print(f"\n!! WARNING: {len(emitted)} emitted gates produced only {len(audit_set)} distinct "
              f"audit_sha256 — sig_5 audit uniqueness violated; investigate pinmap _gate_id embedding")
        return 2

    # Update WP sections
    print(f"\n=== Updating WP sections in {WP_PATH.relative_to(PROJECT_ROOT)} ===")
    wp_text = WP_PATH.read_text(encoding="utf-8")
    for gate, value_str, pinmap, audit_sha, content_sha in emitted:
        wp_text = update_wp_section(wp_text, gate, states, value_str, pinmap, audit_sha, content_sha)
        print(f"  updated WP §{gate['wp_id']} ({gate['gate_id']})")
    WP_PATH.write_text(wp_text, encoding="utf-8")
    print(f"\n=== Wrote {WP_PATH.relative_to(PROJECT_ROOT)} ===")

    print(f"\n=== S88-W4B-PRE-REG-INC-CLOSURE: {len(emitted)} gates closed PRE-REG-INC ===")
    print("    (W4b-24 K=3 auto-flip is PRE-CLOSED separately; handled outside this script)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
