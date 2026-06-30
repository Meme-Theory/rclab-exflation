#!/usr/bin/env python3
"""
S87 W10-3 mechanical PRE-REG-INC closure
=========================================

§W10-3 (`S87-BULLETIN-#3-LIZZI-OBSERVABLE-PROMOTION`) is CONDITIONAL on §W10-1
(`S87-BULLETIN-#3-RESCUE-RESIDUAL`) ∈ {PASS, PASS-WITH-RESIDUAL}; otherwise
mechanical closure per plan `sessions/session-plan/session-87-plan-w10.md`
§"Wave 10 Decision Point Prerequisites" item 8 line 44 + plan §W10-3 lines 244,
272, 323.

§W10-1's verdict at `computations/session-87/s87_gate_verdicts.txt:280` is FAIL — the
L1↔L2 axis-decomposition under the canonical L1-Zubarev × L2-zeta regulator pair
at substrate-distance-1 does NOT surface s_eff = 11/2 as a Mellin-pole locus
(r_L1L2(L=12) = 6.6692 vs r_anchor = 11/7 = 1.571; |dev|=3.244 = 324% above the
PASS threshold of 0.1%). This fires the plan's pre-registered §W10-3 FAIL-path
branch and replaces the lizzi-spectral-functional-theorist promotion-authority
dispatch with this orchestrator-authored mechanical closure.

This is an orchestrator-authored mechanical closure per
`.claude/rules/mechanical-closure-discipline.md`:
- Plan-anticipated FAIL-path topology (rule §"When mechanical closure IS acceptable" #1)
- Verdict honesty: FAIL with descriptive value string naming blocking prereq (#2)
- Per-gate-distinct audit_sha256 via pinmap with gate identity keys (#3)
- Audit-trail signature naming the blocking prereq + its observed status (#4)
- Working-paper update is in-script (#5)

Dual-SHA per `.claude/templates/script-template.py` §4:
    audit_sha256   = sha256(script_bytes || canonical_bytes || pinmap_json)
    content_sha256 = sha256(script_bytes)

This is a metadata-closure script: NO physics is computed. The verdict line
records that the gate could not be evaluated because the upstream prerequisite
§W10-1 has status ≠ {PASS, PASS-WITH-RESIDUAL}.

Idempotency: re-runs parse the existing verdict line (if present) and reuse its
dual-SHA pair rather than recomputing — this keeps WP-update SHAs consistent
with the verdict file even across re-runs after partial-failure crashes (mirrors
the S86 W3 closure precedent at `computations/session-86/s86_w3_pre_reg_inc_closure.py`).
"""

from __future__ import annotations

# canonical_constants import retained for computations/_shared/CLAUDE.md compliance
# (no constants used; this script emits metadata closures only — no framework computation)
from canonical_constants import *  # noqa: F401,F403

import hashlib
import json
import sys
from pathlib import Path
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===


PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
VERDICT_TXT = resolve_output(87, 's87_gate_verdicts.txt')
CANONICAL_PY = resolve_script(None, 'canonical_constants.py')
WP_PATH = PROJECT_ROOT / "sessions" / "session-87" / "session-87-results-workingpaper.md"

# §W10-3 gate metadata + required-prereq map (per plan §W10-3 lines 234-323)
GATE = {
    "gate_id":     "S87-BULLETIN-#3-LIZZI-OBSERVABLE-PROMOTION",
    "wp_id":       "W10-3",
    "scheme":      "L2-zeta-Mellin-cone-residue",
    "convention":  "substrate-distance-1-Lizzi-observable",
    "L_max":       12,
    "required":    {"BULLETIN-#3-RESCUE-RESIDUAL": "S87-BULLETIN-#3-RESCUE-RESIDUAL"},
    "agent":       "lizzi-spectral-functional-theorist (PLAN; mechanical-closure replaces dispatch)",
}


def parse_prereq_verdicts() -> dict[str, tuple[str, str]]:
    """Read s87_gate_verdicts.txt; return {symbol: (status, value_chunk)} for prereqs.

    For each prereq, the LAST verdict line in the file (most-recent canonical
    state) is taken as the operative one.
    """
    states: dict[str, tuple[str, str]] = {}                     # (local)
    text = VERDICT_TXT.read_text(encoding="utf-8")              # (local)
    for sym, gate_id in GATE["required"].items():
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
    """Per .claude/templates/script-template.py §4 dual-SHA schema."""
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


def build_value_string(states: dict[str, tuple[str, str]]) -> tuple[str, dict[str, str]]:
    """Build (value_str, pinmap) for §W10-3.

    Plan-pinned conditional-trigger predicate: §W10-3 dispatches with full lizzi
    promotion-authority IFF §W10-1 verdict ∈ {PASS, PASS-WITH-RESIDUAL}; else
    mechanical closure per plan line 244 with value pattern
    `PRE-REG-INC_blocked_by_S87-BULLETIN-#3-RESCUE-RESIDUAL_<status>`.

    The pinmap embeds gate identity keys for per-gate-distinct audit_sha256
    per `.claude/rules/mechanical-closure-discipline.md` §"When mechanical
    closure IS acceptable" item (3).
    """
    pinmap: dict[str, str] = {                                  # (local)
        "_gate_id":    GATE["gate_id"],
        "_wp_id":      GATE["wp_id"],
        "_scheme":     GATE["scheme"],
        "_convention": GATE["convention"],
    }
    block_parts: list[str] = []                                 # (local)
    blocked = False                                             # (local)
    PASS_ACCEPT = {"PASS", "PASS-WITH-RESIDUAL"}                # (local) plan line 244 conditional predicate
    for sym, gid in GATE["required"].items():
        stat, _ = states[sym]
        pinmap[sym] = f"{gid}={stat}"
        if stat not in PASS_ACCEPT:
            blocked = True
            block_parts.append(f"{gid}_{stat}")
    if not blocked:
        return ("", pinmap)
    return (f"PRE-REG-INC_blocked_by_{'_'.join(block_parts)}", pinmap)


def make_verdict_line(value_str: str, audit_sha: str, content_sha: str) -> str:
    """Canonical verdict line per `.claude/rules/gate-verdicts.md` §"S81+ canonical form"."""
    return (
        f"{GATE['gate_id']}: FAIL -- value={value_str!r} "
        f"scheme={GATE['scheme']} convention={GATE['convention']} "
        f"L_max={GATE['L_max']} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=R3\n"
    )


def make_companion_row(value_str: str, audit_sha: str, content_sha: str) -> str:
    """Dual-SHA companion row per `.claude/rules/gate-verdicts.md` W9a-99 split + closure provenance."""
    req = ", ".join(GATE["required"].values())                  # (local)
    return (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE['gate_id']} dual-SHA companion row (W9a-99 split); "
        f"PRE-REG-INC per session-87-plan-w10.md "
        f"\"Wave 10 Decision Point Prerequisites\" item 8 line 44; "
        f"deferred to S88+; required prereqs: [{req}]; "
        f"closure_script=computations/session-87/s87_w10_3_pre_reg_inc_closure.py\n"
    )


def update_wp_section(
    wp_text: str,
    states: dict[str, tuple[str, str]],
    value_str: str,
    audit_sha: str,
    content_sha: str,
) -> str:
    """Replace placeholder content in WP §W10-3; preserve section bounds."""
    sect_marker = f"### §{GATE['wp_id']}."                      # (local)
    sect_start = wp_text.index(sect_marker)                     # (local)
    sect_end = wp_text.index("\n---\n", sect_start)             # (local)
    old_section = wp_text[sect_start:sect_end]                  # (local)
    new_section = old_section                                   # (local)

    # Heading update — plan §17 specifies lizzi as PRIMARY; WP shell says connes;
    # mechanical closure replaces the dispatch entirely → reflect the orchestrator authorship.
    new_section = new_section.replace(
        "### §W10-3. S87-BULLETIN-#3-LIZZI-OBSERVABLE-PROMOTION (connes-ncg-theorist)",
        "### §W10-3. S87-BULLETIN-#3-LIZZI-OBSERVABLE-PROMOTION (orchestrator mechanical-closure; replaces planned lizzi-spectral-functional-theorist dispatch per plan §44 conditional-trigger predicate FAIL-path firing)",
    )

    # Status
    new_section = new_section.replace(
        "**Status**: NOT STARTED",
        "**Status**: PRE-REG-INCOMPLETE (mechanical closure per `.claude/rules/mechanical-closure-discipline.md`; deferred to S88+ as carry-forward `S88-BULLETIN-#3-RESCUE-RESIDUAL-REMEDIATION` followed by `S88-BULLETIN-#3-LIZZI-OBSERVABLE-PROMOTION-RE-EMIT` if predecessor PASSes)",
    )

    # Trigger drift fix per plan canonical [VERIFY-THEOREM] (plan line 240)
    new_section = new_section.replace(
        "**Trigger**: `[VERIFY]` (CONDITIONAL on §W10-1 verdict; mechanical-closure protocol on FAIL path)",
        "**Trigger**: `[VERIFY-THEOREM]` plan-canonical (WP-shell drift `[VERIFY]` superseded; CONDITIONAL on §W10-1; FAIL-path activated, mechanical closure replaces specialist dispatch)",
    )

    # MCP block
    new_section = new_section.replace(
        "**MCP Pre-Compute Audit**:\n*(pending — list the `mcp__knowledge__*` queries executed before writing the script, with one-line salient return each; mark PRE-CLOSED if a closure covers the gate. Per `.claude/rules/knowledge-index-usage.md`.)*",
        "**MCP Pre-Compute Audit**: N/A — mechanical closure performs no physics computation; the gate is structurally untestable until §W10-1 (`S87-BULLETIN-#3-RESCUE-RESIDUAL`) lands a successor verdict ∈ {PASS, PASS-WITH-RESIDUAL}. The blocking prereq is recorded as the closure value-string; the substrate-physics question (does the s_eff = 11/2 candidate surface as a Mellin-pole locus under L1↔L2 axis decomposition?) was answered NEGATIVELY by §W10-1 — that is where the substrate-spectral information lives.",
    )

    # Verdict block
    sym = next(iter(GATE["required"]))                          # (local)
    gid = GATE["required"][sym]                                 # (local)
    stat, val = states[sym]                                     # (local)
    verdict_old = "**Verdict**:\n*(pending agent execution)*"
    verdict_new = (
        f"**Verdict**: FAIL (PRE-REG-INC mechanical closure) — value={value_str!r}\n\n"
        "Mechanical PRE-REG-INC closure per plan §\"Wave 10 Decision Point Prerequisites\" item 8 "
        "line 44 (FAIL-path conditional-trigger predicate) and `.claude/rules/mechanical-closure-discipline.md` "
        "§\"When mechanical closure IS acceptable\". The §W10-1 (`S87-BULLETIN-#3-RESCUE-RESIDUAL`) "
        f"verdict at `computations/session-87/s87_gate_verdicts.txt:280` is **{stat}** with value={val!r}; "
        "this fires the §W10-3 conditional-trigger FAIL-path branch the plan author pre-registered "
        "(per plan line 244: `value='PRE-REG-INC_blocked_by_S87-BULLETIN-#3-RESCUE-RESIDUAL_FAIL'`). "
        "FAIL verdict + descriptive value-string follows the `mechanical-closure-discipline.md` "
        "verdict-honesty discipline (#2) and audit-trail signature requirement (#4).\n\n"
        "**Required prerequisite and observed state**:\n"
        f"  - {sym} (`{gid}`): **{stat}** (value={val!r}) — BLOCKING\n\n"
        f"**4-tuple**: `(value={value_str!r}, scheme={GATE['scheme']}, "
        f"convention={GATE['convention']}, L_max={GATE['L_max']})`\n\n"
        f"**Dual-SHA**:\n"
        f"  - `audit_sha256`: `{audit_sha}`\n"
        f"  - `content_sha256`: `{content_sha}`\n\n"
        "**Closure mechanism**: `computations/session-87/s87_w10_3_pre_reg_inc_closure.py` "
        "(orchestrator-authored mechanical closure, NOT lizzi-spectral-functional-theorist dispatch). "
        "The planned lizzi promotion-authority dispatch is REPLACED by this mechanical closure per "
        "the plan's pre-registered FAIL-path branch — this is not a dispatch failure, it is the "
        "plan's conditional-trigger predicate firing as designed. No physics computation performed; "
        "the verdict line records that theorem-grade Lizzi-observable promotion of s_eff = 11/2 was "
        "structurally untestable at S87 because the upstream substrate-spectral L1↔L2 axis-"
        "decomposition that would have surfaced the s_eff = 11/2 Mellin-pole locus did not realize "
        "that locus (§W10-1 returned r_L1L2 = 6.67 vs anchor 11/7 = 1.57, deviation 324%).\n\n"
        "**Schema-v2 3-tuple companion**: not emitted — mechanical-closure verdict has no "
        "directional pre-registration (the closure is binary: blocked vs not-blocked by upstream "
        "verdict state); no signed delta against a target."
    )
    new_section = new_section.replace(verdict_old, verdict_new)

    # Results block
    res_start_marker = "**Results**:\n*(pending"                # (local)
    if res_start_marker in new_section:
        rs = new_section.index(res_start_marker)                # (local)
        re_close = new_section.index(")*", rs) + 2              # (local)
        results_old = new_section[rs:re_close]                  # (local)
        results_new = (
            "**Results**: NONE — gate not executed; PRE-REG-INC mechanical closure only.\n\n"
            "**Solution-space interpretation**: The Lizzi-observable promotion of `s_eff = 11/2` "
            "remains UNTESTED at theorem grade in S87. This is NOT itself a corridor closure (no "
            "structural information is added by the mechanical closure per se); the corridor "
            "closure was supplied by §W10-1's FAIL — the L1↔L2 axis decomposition under the "
            "canonical L1-Zubarev × L2-zeta regulator pair at substrate-distance-1 does NOT "
            "surface `s_eff = 11/2` as a Mellin-pole locus (r_L1L2(L=12) = 6.67 vs anchor 11/7). "
            "§W10-3 records that the Stage-0 → Stage-1 candidate landing per "
            "`.claude/rules/joint-theorem-promotion.md` cannot be performed without the upstream "
            "§W10-1 axis-decomposition realization PASSing.\n\n"
            "**Audit hygiene** (per `.claude/rules/mechanical-closure-discipline.md` §"
            "\"Carry-forward script-bytes immutability\"): the closure script is written as a one-shot "
            "metadata closure; idempotent re-run logic parses the existing verdict line and reuses "
            "its dual-SHA pair (preventing audit-pin drift across re-runs). After first execution "
            "the script SHOULD be made read-only or a frozen snapshot committed alongside the "
            "verdict-file emission per the rule's forward-looking hazard mitigation.\n\n"
            "**S88+ carry-forward** (4-field spec per `.claude/rules/output-standards.md` §\"Action Items Format\"):\n\n"
            "1. **What**: After §W10-1 successor (`S88-BULLETIN-#3-RESCUE-RESIDUAL-REMEDIATION` "
            "carry-forward identifying which S52-S77 chain element drifted, per §W10-1 Wrap-Up "
            "S88 4-field spec) lands a successor verdict ∈ {PASS, PASS-WITH-RESIDUAL}, re-emit "
            "§W10-3 (`S88-BULLETIN-#3-LIZZI-OBSERVABLE-PROMOTION-RE-EMIT`) with full "
            "lizzi-spectral-functional-theorist promotion-authority dispatch to evaluate the three "
            "Lizzi-observable promotion criteria.\n"
            "2. **Inputs**: (a) §W10-1 successor data + verdict line (when available); "
            "(b) §VII.M Three-Layer Regulator Theorem registry entry (machine-exact composition "
            "law preserved here in §W10-1 even under FAIL — the composition-law structure is sound; "
            "only the identification of r_L1L2 with 11/7 was broken); "
            "(c) §VII.K-PROP.W10-4 substrate constant `rho_inf_FW = -0.8103647022669215` (§W10-2 "
            "PASS) for any Mellin-cone-residue cross-reference; "
            "(d) `computations/_shared/canonical_constants.py` standard imports + "
            "`sessions/framework/registry/elimination-bulletins.md` Bulletin #3 source SHA pin.\n"
            "3. **Gate**: Three Lizzi-observable promotion criteria per plan §W10-3 lines 250-254 — "
            "(a) regulator-pin compliance (L_max-stability of s_eff at Level-2 envelope "
            "`|s_eff(L_max=12) − 11/2| ≤ 6.94e-3`); "
            "(b) Three-Layer-Regulator-Theorem invariance under L1↔L2 axis composition (verified "
            "by §W10-1 successor PASS); "
            "(c) Mellin-cone-residue locus closed-form algebraic identity at substrate-distance-1 "
            "pole. Composite PASS iff all 3 hold; INFO at PASS-WITH-RESIDUAL upstream → Stage-1 "
            "candidate per `joint-theorem-promotion.md`; FAIL otherwise.\n"
            "4. **Effort**: ~half-wave (lizzi-spectral-functional-theorist dispatch; depends on "
            "§W10-1 successor's preceding wave-equivalent via `S88-BULLETIN-#3-RESCUE-RESIDUAL-"
            "REMEDIATION` ~1 wave).\n\n"
            "**Substrate framing** (per `.claude/rules/phononic-framing.md` §\"IS Space, Not IN Space\"): "
            "the substrate-distance-1 Mellin-cone-residue locus that Lizzi-observable promotion "
            "would have characterized remains uncharacterized at the S87 cutoff; the gate does not "
            "report on the substrate's structural state at the s_eff = 11/2 candidate Mellin-pole "
            "locus — only on the audit-trail's conditional-trigger topology firing the FAIL-path "
            "branch. The substrate-physics question itself (does s_eff = 11/2 surface as a canonical "
            "L2-zeta exponent post-decomposition?) was answered NEGATIVELY by §W10-1; what §W10-3 "
            "records is that promotion-AUTHORITY-grade theorem landing requires the upstream "
            "axis-decomposition realization PASS, which is currently absent."
        )
        new_section = new_section.replace(results_old, results_new)

    return wp_text[:sect_start] + new_section + wp_text[sect_end:]


def main() -> int:
    states = parse_prereq_verdicts()
    print("=== §W10-3 prerequisite verdict states (most-recent line per gate) ===")
    for sym, (status, value) in states.items():
        gid = GATE["required"][sym]
        print(f"  {sym:30} = {gid:35} : {status:5} (value={value})")
    print()

    # Idempotency: parse pre-existing §W10-3 verdict lines (re-run safety)
    verdict_text = VERDICT_TXT.read_text(encoding="utf-8")       # (local)
    prefix = GATE["gate_id"] + ":"                               # (local)
    existing = [ln for ln in verdict_text.splitlines()
                if ln.startswith(prefix)
                and "audit_sha256=" in ln
                and "content_sha256=" in ln]                     # (local)

    value_str, pinmap = build_value_string(states)
    if not value_str:
        print(f"[NOT-BLOCKED] {GATE['gate_id']} — prereq PASSes ∈ {{PASS, PASS-WITH-RESIDUAL}};")
        print(f"            mechanical closure should NOT fire here. ABORTING — re-run lizzi dispatch instead.")
        return 1  # script-error: precondition for mechanical closure not met

    if existing:
        last = existing[-1]                                      # (local)
        audit_sha = last.split("audit_sha256=", 1)[1].split()[0] # (local)
        content_sha = last.split("content_sha256=", 1)[1].split()[0]  # (local)
        print(f"[ALREADY-EMITTED] {GATE['gate_id']}")
        print(f"          recovered audit:   {audit_sha[:16]}...")
        print(f"          recovered content: {content_sha[:16]}...")
        appended = False                                         # (local)
    else:
        audit_sha, content_sha = compute_dual_sha(pinmap)
        print(f"[BLOCKED] {GATE['gate_id']}")
        print(f"          value:   {value_str}")
        print(f"          audit:   {audit_sha[:16]}...")
        print(f"          content: {content_sha[:16]}...")
        with VERDICT_TXT.open("a", encoding="utf-8") as fp:
            fp.write(make_verdict_line(value_str, audit_sha, content_sha))
            fp.write(make_companion_row(value_str, audit_sha, content_sha))
        appended = True                                          # (local)

    print()
    print("=== Updating §W10-3 working-paper section ===")
    wp_text = WP_PATH.read_text(encoding="utf-8")
    new_text = update_wp_section(wp_text, states, value_str, audit_sha, content_sha)
    WP_PATH.write_text(new_text, encoding="utf-8")
    print(f"  updated WP §{GATE['wp_id']} ({GATE['gate_id']})")

    if appended:
        print(f"\n=== §W10-3 mechanical closure complete: 1 verdict appended, WP updated ===")
    else:
        print(f"\n=== §W10-3 mechanical closure idempotent re-run: WP refreshed, verdict-file unchanged ===")
    return 0  # script ran successfully — verdict is data, not exit-code-encoded (per math-scripts.md §"Exit Codes")


if __name__ == "__main__":
    sys.exit(main())
