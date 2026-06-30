#!/usr/bin/env python3
"""
S87 W4-5 (CF-29) mechanical PRE-REG-INC closure
================================================

CF-29 (S87-TYPE-F-TYPE-S-CROSS-PILLAR-AUDIT) has CF-26
(S87-TYPE-F-PER-MODE-PHASE-AUDIT) as an upstream prerequisite per plan
§W4-5 lines 666-668:

    "CF-29 depends on CF-25 (cross-pillar bridge) AND CF-26 (Type-F
    partition validation) for the audit substrate. If either upstream
    FAILs, CF-29 routes to PRE-REG-INC per `mechanical-closure-discipline.md`
    blocked on the failing upstream(s)."

CF-26 closed FAIL (axiom-violation: J=1.625, gamma=2.264, first-order=0.115;
all > 1e-12 threshold; reason=axiom-violation per s87_gate_verdicts.txt
line 132). Per the literal plan-§W4-5 directive, CF-29 routes to
PRE-REG-INC.

Substantive-reading carve-out (logged for S88 carry-forward, NOT acted on
here): CF-26's FAIL is at the cell-phase-ansatz layer, not at the
operator-projection-criterion layer that CF-29's classification work
substantively depends on. The Type-F partition DEFINITION is intact; the
canonical 32-mode REALIZATION failed J/gamma. CF-29's substrate is the
DEFINITION (operator-projection criterion), not the REALIZATION. A
substantive S88 dispatch could resume CF-29 even before CF-26's
antisymmetric-cell-phase corridor (S88-TYPE-F-ANTISYMMETRIC-CELL-PHASE-RETRY)
closes. This is captured as S88-CF-29-RESUME-AFTER-CF-26-RESOLUTION.

Per `.claude/rules/mechanical-closure-discipline.md` §Scope: orchestrator-
authored mechanical-closure script; NO physics computation; NO specialist
agent dispatch.

Per `.claude/rules/gate-verdicts.md` and S86 W3 closure precedent
(`s86_w3_pre_reg_inc_closure.py`), upstream-blocked gates emit FAIL
verdicts with descriptive `value='PRE-REG-INC_blocked_by_<reason>'`
strings; no PASS verdict is permitted (PROHIBITED_ACTIONS Class 4).

Dual-SHA per `.claude/templates/script-template.py` §4:
    audit_sha256   = sha256(script_bytes || canonical_bytes || pinmap_json)
    content_sha256 = sha256(script_bytes)
"""

from __future__ import annotations

# canonical_constants import retained for audit compliance (no constants used;
# this script emits metadata closures only -- no framework computation)
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

# Carry-forward symbol -> canonical S87 gate ID for prereq lookup
PREREQ_GATE_IDS = {
    "CF-25": "S87-CROSS-PILLAR-3-CHANNEL-THEOREM-PROOF",
    "CF-26": "S87-TYPE-F-PER-MODE-PHASE-AUDIT",
}

# CF-29 gate metadata (per plan §W4-5 PRDR machinery pin block)
W4_5_GATE = {
    "gate_id":   "S87-TYPE-F-TYPE-S-CROSS-PILLAR-AUDIT",
    "wp_id":     "W4-5",
    "carry_id":  "CF-29",
    "scheme":    "NCG-axiomatic-operator-projection-criterion",
    "convention": "A_K-tripartite-bimodule",
    "L_max":     10,
    "required":  ["CF-25", "CF-26"],
    "agent":     "connes-ncg-theorist",
    "block_rule": "If either upstream FAILs, CF-29 routes to PRE-REG-INC (plan §W4-5 line 668).",
}

# Per plan §W4-5 line 668: only FAIL upstream blocks; INFO is acceptable.
BLOCKING_STATES = {"FAIL", "MISSING"}


def parse_prereq_verdicts() -> dict[str, tuple[str, str]]:
    """Read s87_gate_verdicts.txt; return {symbol: (status, value_chunk)} for prereqs.

    For each prereq, the LAST canonical verdict line (no leading '#') in the
    file is taken as the operative one.
    """
    states: dict[str, tuple[str, str]] = {}                     # (local)
    text = VERDICT_TXT.read_text(encoding="utf-8")              # (local)
    for sym, gate_id in PREREQ_GATE_IDS.items():
        prefix = gate_id + ":"                                  # (local)
        # Only canonical lines (no leading '#'); skip companion / retraction comments.
        lines = [ln for ln in text.splitlines()
                 if ln.startswith(prefix)
                 and not ln.lstrip().startswith("#")]            # (local)
        if not lines:
            states[sym] = ("MISSING", "no_verdict_line")
            continue
        last = lines[-1]                                        # (local)
        body = last.split(":", 1)[1].strip()                    # (local)
        status = body.split()[0].rstrip(",")                    # (local)
        if "value=" in last:
            v_start = last.index("value=") + len("value=")      # (local)
            v_chunk = last[v_start:].split()[0].strip("'\"")    # (local)
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


def build_value_string(gate: dict, states: dict[str, tuple[str, str]]) -> tuple[str, dict[str, str], list[str]]:
    """Build (value_str, pinmap, blocking_list) for the W4-5 gate."""
    pinmap: dict[str, str] = {"_gate_id": gate["gate_id"],
                              "_wp_id":   gate["wp_id"],
                              "_scheme":  gate["scheme"],
                              "_convention": gate["convention"]}     # (local)
    blocking: list[str] = []                                     # (local)
    block_parts: list[str] = []                                  # (local)
    for sym in gate["required"]:
        stat, val = states[sym]
        pinmap[sym] = f"{PREREQ_GATE_IDS[sym]}={stat}"
        if stat in BLOCKING_STATES:
            blocking.append(sym)
            # Encode the FAIL reason in the value string when available.
            reason_tag = ""                                      # (local)
            if "axiom-violation" in val:
                reason_tag = "_axiom-violation"
            elif "PIN-DRIFT" in val.upper():
                reason_tag = "_PIN-DRIFT"
            elif "upstream" in val.lower():
                reason_tag = "_upstream-block"
            block_parts.append(f"{PREREQ_GATE_IDS[sym]}_{stat}{reason_tag}")
    if not blocking:
        return ("", pinmap, blocking)
    return (f"PRE-REG-INC_blocked_by_{'_AND_'.join(block_parts)}", pinmap, blocking)


def make_verdict_line(gate: dict, value_str: str, audit_sha: str, content_sha: str) -> str:
    return (
        f"{gate['gate_id']}: FAIL -- value={value_str!r} "
        f"scheme={gate['scheme']} convention={gate['convention']} "
        f"L_max={gate['L_max']} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )


def make_companion_dual_sha_row(gate: dict, audit_sha: str, content_sha: str) -> str:
    return (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {gate['gate_id']} dual-SHA companion row (W9a-99 split)\n"
    )


def make_3tuple_row(gate: dict) -> str:
    # Mechanical closure: sign_verdict=N/A (no signed delta predicted; gate
    # untestable), magnitude_verdict=FAIL (binary upstream-block per plan
    # §W4-5 line 668), regime_verdict=VALID (closure regime is well-defined).
    return (
        f"# sign_verdict=N/A magnitude_verdict=FAIL regime_verdict=VALID "
        f"# {gate['gate_id']} 3-tuple annotation (S87 schema-v2)\n"
    )


def make_diagnostic_row(gate: dict, blocking: list[str], states: dict[str, tuple[str, str]]) -> str:
    blocked_summary = "; ".join(
        f"{sym}={PREREQ_GATE_IDS[sym]}_status_{states[sym][0]}_value_{states[sym][1][:80]}"
        for sym in blocking
    )                                                            # (local)
    return (
        f"# diagnostic: PRE-REG-INC per session-87-plan-w4.md §W4-5 lines 666-668; "
        f"deferred to S88 (S88-CF-29-RESUME-AFTER-CF-26-RESOLUTION carry-forward); "
        f"blocking prereqs: [{blocked_summary}]; "
        f"closure_script=computations/session-87/s87_w4_5_pre_reg_inc_closure.py; "
        f"substantive-reading carve-out: CF-26 FAIL is at cell-phase-ansatz layer (operator-projection-criterion intact). "
        f"# {gate['gate_id']} mechanical-closure diagnostic\n"
    )


def update_wp_section(
    wp_text: str,
    gate: dict,
    states: dict[str, tuple[str, str]],
    value_str: str,
    blocking: list[str],
    audit_sha: str,
    content_sha: str,
) -> str:
    """Replace the placeholder Status/Verdict/Results in WP §W4-5."""
    sect_marker = f"### §{gate['wp_id']}."                      # (local)
    sect_start = wp_text.index(sect_marker)                     # (local)
    sect_end = wp_text.index("\n---\n", sect_start)             # (local)
    old_section = wp_text[sect_start:sect_end]                  # (local)
    new_section = old_section                                   # (local)

    # Status line
    new_section = new_section.replace(
        "**Status**: NOT STARTED",
        "**Status**: PRE-REG-INCOMPLETE (mechanical closure 2026-04-28 per plan §W4-5 lines 666-668; deferred to S88)",
    )

    # MCP Pre-Compute Audit block
    new_section = new_section.replace(
        "**MCP Pre-Compute Audit**:\n*(pending — list the `mcp__knowledge__*` queries executed before writing the script, with one-line salient return each; mark PRE-CLOSED if a closure covers the gate. Per `.claude/rules/knowledge-index-usage.md`.)*",
        "**MCP Pre-Compute Audit**: N/A — no physics compute performed; gate is structurally untestable until upstream prereq lands per plan §W4-5 line 668.",
    )

    # Verdict block
    prereq_lines = []                                            # (local)
    for sym in gate["required"]:
        stat, val = states[sym]
        gid = PREREQ_GATE_IDS[sym]
        if stat in BLOCKING_STATES:
            prereq_lines.append(f"  - {sym} (`{gid}`): **{stat}** (value=`{val}`) — BLOCKING")
        else:
            prereq_lines.append(f"  - {sym} (`{gid}`): **{stat}** (value=`{val}`) — does not block this gate (INFO/PASS acceptable per plan §W4-5 line 668)")

    verdict_old = "**Verdict**:\n*(pending agent execution)*"
    verdict_new = (
        f"**Verdict**: FAIL (PRE-REG-INC) — value={value_str!r}\n\n"
        "Mechanical PRE-REG-INC closure: this gate's required upstream prerequisites "
        "(per `sessions/session-plan/session-87-plan-w4.md` §W4-5 lines 666-668) have not all "
        "satisfied the non-blocking threshold (PASS or INFO) in `computations/session-87/s87_gate_verdicts.txt`; "
        "per plan §W4-5 line 668 the documented outcome for upstream-FAIL is **PRE-REG-INC, deferred to S88**. "
        "FAIL verdict + descriptive value-string follows S86 precedent (`s86_w3_pre_reg_inc_closure.py`) and "
        "the canonical pattern at `.claude/rules/mechanical-closure-discipline.md` §Audit-trail signature.\n\n"
        "**Required prerequisites and observed states**:\n"
        + "\n".join(prereq_lines) + "\n\n"
        f"**4-tuple**: `(value={value_str!r}, scheme={gate['scheme']}, "
        f"convention={gate['convention']}, L_max={gate['L_max']})`\n\n"
        f"**Dual-SHA**:\n"
        f"  - `audit_sha256`: `{audit_sha}`\n"
        f"  - `content_sha256`: `{content_sha}`\n\n"
        "**Substantive-reading carve-out (LOGGED, NOT ACTED ON)**: CF-26's FAIL is at the "
        "cell-phase-ansatz layer (the canonical monotone θ_c = 2π·c/N · (eig_c/λ_min) realization "
        "broke J/γ axiom invariance), NOT at the operator-projection-criterion layer that CF-29's "
        "Type-F/Type-S classification work substantively depends on. The Type-F PARTITION DEFINITION "
        "(an observable is Type-F iff its expectation factorizes as a single-projection trace on "
        "A_K = C ⊕ H ⊕ M_3(C)) is intact per WP §W4-2 line 3717. CF-29 could substantively proceed "
        "even before CF-26's antisymmetric-cell-phase corridor "
        "(`S88-TYPE-F-ANTISYMMETRIC-CELL-PHASE-RETRY`) closes. This carve-out is captured as the "
        "S88 carry-forward `S88-CF-29-RESUME-AFTER-CF-26-RESOLUTION` below; it is NOT acted on here "
        "because plan §W4-5 line 668 is literal and rule-strict mechanical closure honors the "
        "literal plan directive (per `feedback_max-effort-full-fidelity.md`).\n\n"
        "**Closure mechanism**: `computations/session-87/s87_w4_5_pre_reg_inc_closure.py` "
        "(orchestrator-authored mechanical closure, NOT specialist-agent dispatch, per "
        "`.claude/rules/mechanical-closure-discipline.md` §Scope). No physics computation was "
        "performed; the verdict line records that the gate could not be evaluated due to upstream "
        "FAIL block."
    )
    new_section = new_section.replace(verdict_old, verdict_new)

    # Results block
    res_start_marker = "**Results**:\n*(pending"                # (local)
    if res_start_marker in new_section:
        rs = new_section.index(res_start_marker)                # (local)
        re_close = new_section.index(")*", rs) + 2              # (local)
        results_old = new_section[rs:re_close]                  # (local)
        results_new = (
            "**Results**: NONE — gate not executed; PRE-REG-INC closure only.\n\n"
            "**Solution-space interpretation** (per `.claude/rules/epistemic-discipline.md` §Evidence Hierarchy): "
            "The CF-29 gate corridor — Type-F vs Type-S classification of {S70 LEGGETT-MOMENT, "
            "Pillar III BCS, Pillar VI A_s/n_s} via the NCG-axiomatic operator-projection criterion — "
            "remains UNTESTED at this session. This is a no-information outcome (NOT a corridor "
            "closure); the plan-§W4-5 PASS / FAIL / INFO consequence states are deferred to S88 "
            "conditional on the blocking CF-26 prerequisite landing (or, alternatively, on the "
            "substantive-reading carve-out being adopted at S88 plan-freeze).\n\n"
            "**Substrate framing** (per `.claude/rules/phononic-framing.md` §\"IS Space, Not IN Space\"): "
            "The substrate IS the operator-projection structure on (A_K, H_K, D_K). Type-F observables "
            "ARE single-projection trace cocycles; Type-S observables ARE mixed-projection trace "
            "cocycles. The pillar labels (II, III, IV, V, VI) are NOT containers — they ARE substrate-IS "
            "observables under distinct regulator-class restrictions. This gate would have classified "
            "3 priority observables under the operator-projection criterion; it does not report on the "
            "substrate's structural state, only on the audit trail's block-by-prerequisite topology.\n\n"
            "**S88 carry-forward** (4-field spec per `feedback_fix-in-session-never-defer.md`):\n"
            "  - **What**: Resume CF-29's Type-F/Type-S classification of {S70 LEGGETT-MOMENT, "
            "Pillar III BCS, Pillar VI A_s/n_s} via the NCG operator-projection criterion. EITHER "
            "(a) wait for `S88-TYPE-F-ANTISYMMETRIC-CELL-PHASE-RETRY` (CF-26 corridor) to PASS and "
            "then run CF-29 substantively, OR (b) adopt the substantive-reading carve-out at S88 "
            "plan-freeze and run CF-29 directly using the operator-projection criterion (which is "
            "well-defined regardless of CF-26's cell-phase ansatz outcome).\n"
            "  - **Inputs**: `computations/session-84/s84_spectrum_cache_L12_tau019.npz` (L_max=10 strict "
            "subset); `sessions/archive/session-86/session-86-w4-workingpaper.md` (Type-F partition R3 "
            "closure); CF-25 verdict at `s87_gate_verdicts.txt:135` "
            "(`audit_sha256=cbab3d5e5abd605c...`); `permanent-results-registry.md` BCS + LEGGETT-MOMENT "
            "blocks; `canonical_constants.py` A_s_FW_eps_02163, A_s_FW_eps_020, n_s_framework.\n"
            "  - **Gate**: `S88-CF-29-RESUME-AFTER-CF-26-RESOLUTION` — PASS = all 3 observables "
            "classified Type-F or Type-S with explicit operator-projection-criterion justification AND "
            "NCG-axiomatic verification AND cross-pillar consistency; FAIL = ill-defined classification "
            "OR axiom violation OR cross-pillar inconsistency; INFO = classifications PASS but "
            "≥1 re-classification triggers cross-cutting framework re-evaluation.\n"
            "  - **Effort**: ~1 wave-equivalent (matches plan §W4-5 estimate)."
        )
        new_section = new_section.replace(results_old, results_new)

    return wp_text[:sect_start] + new_section + wp_text[sect_end:]


def main() -> int:
    states = parse_prereq_verdicts()
    print("=== W4-5 prerequisite verdict states (most-recent canonical line per gate) ===")
    for sym, (status, value) in states.items():
        gid = PREREQ_GATE_IDS[sym]
        print(f"  {sym:6} = {gid:55} : {status:5} (value={value[:60]})")
    print()

    value_str, pinmap, blocking = build_value_string(W4_5_GATE, states)
    if not value_str:
        print(f"[NOT-BLOCKED] {W4_5_GATE['gate_id']} — all prereqs PASS or INFO; mechanical closure not warranted.")
        print(f"  Substantive specialist-agent dispatch is the correct path. Aborting closure.")
        return 1

    # Idempotency: check if a CF-29 verdict line already exists.
    verdict_text = VERDICT_TXT.read_text(encoding="utf-8")       # (local)
    prefix = W4_5_GATE["gate_id"] + ":"                          # (local)
    existing_lines = [ln for ln in verdict_text.splitlines()
                      if ln.startswith(prefix)
                      and not ln.lstrip().startswith("#")
                      and "audit_sha256=" in ln]                 # (local)
    if existing_lines:
        last = existing_lines[-1]                                # (local)
        audit_sha = last.split("audit_sha256=", 1)[1].split()[0] # (local)
        content_sha = last.split("content_sha256=", 1)[1].split()[0]  # (local)
        print(f"[ALREADY-EMITTED] {W4_5_GATE['wp_id']} {W4_5_GATE['gate_id']}")
        print(f"          recovered audit: {audit_sha[:16]}...  content: {content_sha[:16]}...")
        new_appends = False                                      # (local)
    else:
        audit_sha, content_sha = compute_dual_sha(pinmap)
        print(f"[BLOCKED] {W4_5_GATE['wp_id']} {W4_5_GATE['gate_id']}")
        print(f"          value: {value_str}")
        print(f"          blocking prereqs: {blocking}")
        print(f"          audit:   {audit_sha}")
        print(f"          content: {content_sha}")
        new_appends = True                                       # (local)

    if new_appends:
        print(f"\n=== Appending verdict + 3 companion rows to {VERDICT_TXT.relative_to(PROJECT_ROOT)} ===")
        with VERDICT_TXT.open("a", encoding="utf-8") as fp:
            fp.write(make_verdict_line(W4_5_GATE, value_str, audit_sha, content_sha))
            fp.write(make_companion_dual_sha_row(W4_5_GATE, audit_sha, content_sha))
            fp.write(make_3tuple_row(W4_5_GATE))
            fp.write(make_diagnostic_row(W4_5_GATE, blocking, states))
    else:
        print(f"\n=== Canonical verdict line already in {VERDICT_TXT.relative_to(PROJECT_ROOT)}; no append ===")

    # Update WP §W4-5
    print(f"\n=== Updating WP §W4-5 in {WP_PATH.relative_to(PROJECT_ROOT)} ===")
    wp_text = WP_PATH.read_text(encoding="utf-8")
    wp_text_new = update_wp_section(wp_text, W4_5_GATE, states, value_str, blocking, audit_sha, content_sha)
    if wp_text_new == wp_text:
        print(f"  WP §W4-5 already updated (no change); idempotent re-run.")
    else:
        WP_PATH.write_text(wp_text_new, encoding="utf-8")
        print(f"  WP §W4-5 updated.")

    print(f"\n=== S87-W4-5-CF-29 PRE-REG-INC closure complete ===")
    print(f"    Verdict: FAIL")
    print(f"    Value:   {value_str}")
    print(f"    Blocking prereqs: {blocking}")
    print(f"    audit_sha256:   {audit_sha}")
    print(f"    content_sha256: {content_sha}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
