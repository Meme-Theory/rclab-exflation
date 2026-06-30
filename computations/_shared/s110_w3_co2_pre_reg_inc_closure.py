#!/usr/bin/env python
"""S110 W3 §W3-3 — S110-CF-CO2-FALSIFIER mechanical closure (orchestrator-authored).

Upstream-block: the CONDITIONAL anchor-free-falsifier gate fires ONLY on
WS-CO-1 (W1) = Reading-ESCAPE. WS-CO-1 returned **Reading-STERILE**
(sessions/session-110/workshops/ws-co-1.md): the one transport-safe ratio
RR=(dw/w)_{l=2}/(dw/w)_{l=3} is Kerr-degenerate (scalar alpha_HC cancels, l-flat),
and the parity-odd Pontryagin operator that would break it is forbidden at all
orders by [J,D_K]=0. The trigger condition did NOT hold => the gate is
structurally untestable this session.

Honest mechanical closure per .claude/rules/mechanical-closure-discipline.md:
verdict=FAIL, value='PRE-REG-INC_blocked_by_WS-CO-1_Reading-STERILE'
(NEVER PASS; the value carries the PRE-REG-INC / upstream-block semantics).
NO physics computation. The plan §W3-3 decision-point pre-registered this no-fire
branch. WP §W3-3 is updated IN THIS RUN (item 5: no verdict-without-WP).
"""
import hashlib
import json
import pathlib
import sys

# Mechanical-closure script: consumes NO framework constants (pure bookkeeping —
# hashlib/json/pathlib only). The import below is present solely to satisfy the
# computations/_shared/CLAUDE.md canonical-import audit (math-scripts.md); nothing
# from canonical_constants is used. Path-resolved so it imports from _shared/.
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from canonical_constants import *  # noqa: F401,F403  (audit-compliance only; no constant used)

ROOT = pathlib.Path(r"C:\sandbox\Ainulindale Exflation")
WP = ROOT / "sessions" / "session-110" / "session-110-w3-workingpaper.md"

# ---- per-gate-distinct input-pin map (identity keys => pairwise-distinct audit_sha256, sig_5) ----
pin_map = {
    "_gate_id": "S110-CF-CO2-FALSIFIER",
    "_wp_id": "W3-3",
    "_scheme": "CONDITIONAL-anchor-free-falsifier",
    "_convention": "WS-CO-1-Reading-STERILE-upstream-block-NOT-FIRED",
    "_L_max": "10",
    "blocking_prereq": "WS-CO-1=Reading-STERILE",
    "blocking_prereq_artifact": "sessions/session-110/workshops/ws-co-1.md",
    "cf_co1_note": "CF-CO1-EOS (W3-2) pins the dimensionful binding gap; the CO2 escape-ratio is the conditional leg that does not fire",
    "plan_anchor": "sessions/session-plan/session-110-plan-w3.md §W3-3 decision-point",
    "rule": ".claude/rules/mechanical-closure-discipline.md",
}
value = "PRE-REG-INC_blocked_by_WS-CO-1_Reading-STERILE"
audit_sha256 = hashlib.sha256(json.dumps(pin_map, sort_keys=True).encode("utf-8")).hexdigest()
content_sha256 = hashlib.sha256((value + "|" + pin_map["_gate_id"] + "|" + pin_map["_wp_id"]).encode("utf-8")).hexdigest()

# ---- WP §W3-3 block-scoped update (in-script; mechanical-closure-discipline item 5) ----
text = WP.read_text(encoding="utf-8")
marker = "### §W3-3. S110-CF-CO2-FALSIFIER"
nxt = "### §W3-4."
i = text.index(marker)
j = text.index(nxt, i)
block = text[i:j]
orig_block = block

block = block.replace(
    "**Status**: NOT STARTED",
    "**Status**: COMPLETED (mechanical closure — verdict FAIL / value PRE-REG-INC, upstream-block; no physics computed)",
    1,
)
block = block.replace(
    "**MCP Pre-Compute Audit**:\n*(pending — list the `mcp__knowledge__*` queries executed before writing the script, with one-line salient return each; mark PRE-CLOSED if a closure covers the gate. Per `.claude/rules/knowledge-index-usage.md`.)*",
    "**MCP Pre-Compute Audit**:\nPRE-CLOSED — no compute executed. Mandatory prerequisite check (per §W3-3 method): WS-CO-1 (`sessions/session-110/workshops/ws-co-1.md`) returned **Reading-STERILE** — the CONDITIONAL trigger (WS-CO-1=Reading-ESCAPE) did NOT hold, so the anchor-free-falsifier gate does not fire. Orchestrator-authored mechanical closure per `.claude/rules/mechanical-closure-discipline.md` (no specialist dispatch, no physics).",
    1,
)
block = block.replace(
    "**Verdict**:\n*(pending agent execution)*",
    "**Verdict**: FAIL — `value='PRE-REG-INC_blocked_by_WS-CO-1_Reading-STERILE'`. The compact-object sector is **sign-built but falsifier-sterile** (WS-CO-1 verdict; 5th M_KK-keystone confirmation): every dimensionless escape-ratio either re-entangles M_KK via the deg(T)=+2 NON-SCALAR transport or is Kerr-degenerate at leading EFT order. This is a constraint-map result, NOT an agent failure — the gate's PASS condition (anchor-free falsifier minted) was structurally unreachable because its upstream trigger did not hold. **Substrate framing**: the compact object is a relay-pattern configuration of the substrate; its QNM/tidal spectral features inherit the rank-1 M_KK weight, so no dimensionless ratio escapes it. No script/npz/png produced (closed-not-run); the only artifact is this closure record + the verdict line.",
    1,
)
assert block != orig_block, "no §W3-3 placeholder replaced — WP format drift; abort"
WP.write_text(text[:i] + block + text[j:], encoding="utf-8")

# ---- print verdict payload for emit_verdict (race-safe canonical writer) ----
payload = {
    "gate_id": "S110-CF-CO2-FALSIFIER",
    "verdict": "FAIL",
    "value": value,
    "scheme": pin_map["_scheme"],
    "convention": pin_map["_convention"],
    "L_max": pin_map["_L_max"],
    "audit_sha256": audit_sha256,
    "content_sha256": content_sha256,
    "session": 110,
    "track": "session",
    "extra_rows": [
        "# PRE-REG-INC per session-110-plan-w3.md §W3-3 decision-point; closed-not-run (WS-CO-1=Reading-STERILE); required prereq: [WS-CO-1=Reading-ESCAPE]; closure_script=computations/_shared/s110_w3_co2_pre_reg_inc_closure.py; orchestrator-authored mechanical closure per mechanical-closure-discipline.md (no specialist dispatch, no physics)",
    ],
}
print("<<<EMIT_VERDICT_PAYLOAD>>>")
print(json.dumps(payload))
print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
print(f"audit_sha256={audit_sha256}")
print(f"content_sha256={content_sha256}")
print("WP §W3-3 updated:", WP)
