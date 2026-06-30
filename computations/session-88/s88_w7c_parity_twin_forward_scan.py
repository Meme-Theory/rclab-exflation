#!/usr/bin/env python3
"""
S88 W7c-86 mechanical PRE-REG-INC closure (PARITY-TWIN-FORWARD-SCAN)
=====================================================================

Gate: S88-W9c-1-PARITY-TWIN-FORWARD-SCAN ([VERIFY])
Plan: sessions/session-plan/session-88-plan-w7c.md §W7c-86 (lines 221-310)

This gate's pre-registered method (plan §W7c-86 Method step 3) requires
evaluation of the GV-Heitsch cocycle on each parity-twin pair (C_n, C_epsN)
for n ∈ {2, 4, 6} via the Connes-Karoubi pairing protocol of S86 W-11
Bulletin #2. Plan §W7c-86 machinery pin (line 247) names
`regulator_class = "GV-Heitsch odd-grading"` per
`.claude/rules/regulator-pin-discipline.md` §"Class-(c) PIN-DRIFT-FROM-STALE-
SOURCE — W-11 Calibration Corpus Extension" forward-looking remediation.

Orchestrator dispatch override (verbatim): "GV-Heitsch module:
phonon-exflation-sim/src/gv_heitsch.py — if absent at dispatch-time, emit
PRE-REG-INC per .claude/rules/mechanical-closure-discipline.md with
value='PRE-REG-INC_blocked_by_S88-GV-HEITSCH-MODULE_status_absent'."

Pre-flight check (2026-05-05):
  $ ls phonon-exflation-sim/src/gv_heitsch.py
    -> No such file or directory
  $ ls phonon-exflation-sim/src/
    -> __init__.py, backend.py, defect_census.py, diagnostics.py,
       expansion.py, gpe_solver.py, initial_conditions.py,
       vortex_detection.py    (NO gv_heitsch.py)

The shared `gv_heitsch.py` module pinned by plan §247 does not exist on
disk at dispatch time. Existing W-11 / W-8 GV-Heitsch implementations are
within-script ad-hoc (s86_w11_eta_gv_joint_probe.py, s87_w8_eta_gv_followup.py,
s88_w3c_eta_gv_regulator_independence.py) — none expose the shared module
the plan pinned, and forward-scan to NEW parity-twin pairs (C_n, C_epsN)
for n ∈ {2, 4, 6} is NOT covered by their (C_H, C_epsH)-only inputs.
The forward-scan is structurally untestable at this session.

Per `.claude/rules/mechanical-closure-discipline.md` §"When mechanical
closure IS acceptable":

  (1) Upstream-block topology: orchestrator dispatch override + plan §31
      Decision Point Prerequisites + plan §W7c-86 machinery pin §247
      explicitly anticipate the missing-module scenario; this is the
      pre-registered PRE-REG-INC pathway, not post-hoc plan editing.
  (2) Verdict honesty: emitted as composite FAIL with
      value='PRE-REG-INC_blocked_by_S88-GV-HEITSCH-MODULE_status_absent';
      never PASS.
  (3) Per-gate-distinct audit_sha256: pinmap embeds _gate_id, _wp_id,
      _scheme, _convention so this closure produces a unique audit_sha256
      vs other PRE-REG-INC closures in S88.
  (4) Audit-trail signature: descriptive value names the blocking module
      symbol (S88-GV-HEITSCH-MODULE) and its observed status (absent).
  (5) Working-paper update is in-script: §W7c-86 Status / MCP Pre-Compute
      Audit / Verdict / Results blocks are rewritten in the same run
      as the verdict-line append.

Per `.claude/rules/v3-closure-recovery.md` sig_5 audit uniqueness, the
dual-SHA pinmap embeds gate identity keys. The S87+ schema-v2 3-tuple
annotation companion row encodes:
  sign_verdict=N/A           (no directional pre-registration exercised;
                              substitution chain Step 4 not computed
                              because producing machinery never ran)
  magnitude_verdict=FAIL     (gate produced no measurable value)
  regime_verdict=VALID       (no regime breakdown — no regime tested;
                              L_max=10 substrate truncation valid IF
                              exercised)
which under the composite-collapse rule (gate-verdicts.md §"Composite-
collapse rule") yields composite=FAIL, consistent with the canonical
verdict line FAIL top-line.

This is a metadata-closure script: NO physics is computed. The .npz
and .png artifact paths pre-registered in plan §W7c-86 are NOT
produced (mechanical closure is metadata-only); the JSON sidecar
records the closure's audit-trail.

Per `.claude/rules/gate-verdicts.md` §"Canonical Verdict-File Path":
the verdict line writes to `computations/session-88/s88_gate_verdicts.txt`
(per-session directory, NOT _shared/).
"""

from __future__ import annotations

# canonical_constants import retained for audit compliance (no constants
# used; this script emits metadata closure only — no framework computation).
import sys as _bootstrap_sys
from pathlib import Path as _bootstrap_Path
_bootstrap_sys.path.insert(0, str(_bootstrap_Path(__file__).resolve().parents[1] / "_shared"))
from canonical_constants import *  # noqa: F401,F403,E402

import hashlib  # noqa: E402
import json  # noqa: E402
import sys  # noqa: E402
from pathlib import Path  # noqa: E402

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SESSION_DIR = PROJECT_ROOT / "computations" / "session-88"
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
# Per .claude/rules/gate-verdicts.md MANDATORY (orchestrator override
# explicit): canonical verdict-file path is
# computations/session-{N}/s{N}_gate_verdicts.txt — NOT _shared/.
VERDICT_TXT = SESSION_DIR / "s88_gate_verdicts.txt"
CANONICAL_PY = SHARED_DIR / "canonical_constants.py"
WP_PATH = PROJECT_ROOT / "sessions" / "session-88" / "session-88-w7c-workingpaper.md"
JSON_SIDECAR = SESSION_DIR / "s88_w7c_parity_twin_forward_scan.json"

# The shared GV-Heitsch module path pinned by plan §247 (regulator_class)
# and orchestrator dispatch override.
GV_HEITSCH_MODULE_PATH = PROJECT_ROOT / "phonon-exflation-sim" / "src" / "gv_heitsch.py"

# Single-gate metadata for this closure
GATE = {
    "gate_id":   "S88-W9c-1-PARITY-TWIN-FORWARD-SCAN",
    "wp_id":     "W7c-86",
    "scheme":    "(η=0, GV≠0) parity-twin signature forward-scan rank-2-cocycle",
    "convention": "axiom-side-c_sub-region-parity-twin-extension-PRIMARY",
    "L_max":     "10",
    # Pre-registered value-string per orchestrator override (verbatim)
    "value":     "PRE-REG-INC_blocked_by_S88-GV-HEITSCH-MODULE_status_absent",
    "registry_slot_planned": "§VII.AH.3 (B#2 generic-parity promotion candidate, BLOCKED)",
}


def detect_gv_heitsch_module() -> dict[str, object]:
    """Detect whether the shared GV-Heitsch module is present at dispatch.

    Returns a dict with detection metadata for audit-trail purposes.
    """
    present = GV_HEITSCH_MODULE_PATH.is_file()                      # (local)
    src_dir = GV_HEITSCH_MODULE_PATH.parent                         # (local)
    src_listing: list[str] = []                                     # (local)
    if src_dir.is_dir():
        src_listing = sorted(p.name for p in src_dir.iterdir() if p.is_file())
    return {
        "module_path":     str(GV_HEITSCH_MODULE_PATH.relative_to(PROJECT_ROOT)),
        "present":         present,
        "src_dir":         str(src_dir.relative_to(PROJECT_ROOT)),
        "src_listing":     src_listing,
        "status":          ("PRESENT" if present else "ABSENT"),
    }


def compute_dual_sha(pinmap: dict[str, str]) -> tuple[str, str]:
    """Per .claude/rules/v3-closure-recovery.md sig_5 schema.

    audit_sha256   = sha256(script_bytes || canonical_bytes || pinmap_json)
    content_sha256 = sha256(script_bytes)
    """
    script_bytes = Path(__file__).read_bytes()                      # (local)
    canonical_bytes = CANONICAL_PY.read_bytes()                     # (local)
    pinmap_json = json.dumps(
        dict(sorted(pinmap.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")                                               # (local)
    h_audit = hashlib.sha256()                                      # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                     # (local)
    h_content = hashlib.sha256()                                    # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()                                 # (local)
    return audit, content


def build_pinmap(detection: dict[str, object]) -> dict[str, str]:
    """Build pinmap embedding gate-identity keys for audit_sha256.

    Identity keys (`_gate_id`, `_wp_id`, `_scheme`, `_convention`) ensure
    sig_5 audit uniqueness across distinct PRE-REG-INC closures.
    """
    pinmap: dict[str, str] = {                                      # (local)
        "_gate_id":         GATE["gate_id"],
        "_wp_id":           GATE["wp_id"],
        "_scheme":          GATE["scheme"],
        "_convention":      GATE["convention"],
        "GV_HEITSCH_MODULE": f"{detection['module_path']}={detection['status']}",
        "L_max_pin":        GATE["L_max"],
        "regulator_class":  "GV-Heitsch odd-grading",
        "level_pin":        "LEVEL=1 (live-physical; SCHEMATIC FORBIDDEN)",
        "parity_twin_n":    "n in {2, 4, 6}",
    }
    return pinmap


def make_verdict_line(audit_sha: str, content_sha: str) -> str:
    """Canonical S87+ verdict line per .claude/rules/gate-verdicts.md."""
    return (
        f"{GATE['gate_id']}: FAIL -- value={GATE['value']!r} "
        f"scheme={GATE['scheme']} "
        f"convention={GATE['convention']} "
        f"L_max={GATE['L_max']} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )


def make_companion_row(audit_sha: str, content_sha: str) -> str:
    """W9a-99 split dual-SHA companion comment row."""
    return (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE['gate_id']} dual-SHA companion row (W9a-99 split); "
        f"PRE-REG-INC per session-88-plan-w7c.md §{GATE['wp_id']} machinery pin §247 "
        f"+ orchestrator dispatch override; deferred to S89; "
        f"required prereqs: [S88-GV-HEITSCH-MODULE]; "
        f"closure_script=computations/session-88/s88_w7c_parity_twin_forward_scan.py\n"
    )


def make_3tuple_annotation_row() -> str:
    """S87+ schema-v2 3-tuple annotation row (sign × magnitude × regime).

    PRE-REG-INC mechanical closure semantics:
      sign_verdict=N/A      — directional pre-registration (substitution
                              chain Step 4: even-grading -> η=0; odd-grading
                              -> GV≠0; ratio preserved) was not exercised
                              because the producing machinery never ran.
      magnitude_verdict=FAIL — gate produced no measurable value (no η_n,
                              no GV_n, no ratio); pass_count_eta_zero_AND_
                              GV_nonzero is undefined / 0 of 3.
      regime_verdict=VALID  — no regime breakdown occurred since no regime
                              was tested; L_max=10 substrate truncation
                              would be VALID under Casimir-bound + Friedrich-
                              Bär saturation if actually exercised.

    Composite-collapse: magnitude=FAIL + regime=VALID -> composite=FAIL,
    consistent with the canonical verdict-line FAIL top-line.
    """
    return (
        f"# sign_verdict=N/A magnitude_verdict=FAIL regime_verdict=VALID "
        f"# {GATE['gate_id']} 3-tuple annotation (S87 schema-v2); "
        f"PRE-REG-INC mechanical-closure: substitution chain Step 4 not "
        f"exercised (no producing machinery ran); composite=FAIL via "
        f"magnitude=FAIL+regime=VALID\n"
    )


def write_json_sidecar(detection: dict[str, object], pinmap: dict[str, str],
                        audit_sha: str, content_sha: str) -> None:
    """JSON sidecar recording closure metadata + MCP pre-compute audit."""
    sidecar = {                                                     # (local)
        "gate_id":          GATE["gate_id"],
        "wp_id":            GATE["wp_id"],
        "verdict":          "FAIL",
        "value":            GATE["value"],
        "scheme":           GATE["scheme"],
        "convention":       GATE["convention"],
        "L_max":            GATE["L_max"],
        "audit_sha256":     audit_sha,
        "content_sha256":   content_sha,
        "schema_version":   "S87+",
        "closure_kind":     "mechanical-PRE-REG-INC",
        "closure_script":   "computations/session-88/s88_w7c_parity_twin_forward_scan.py",
        "verdict_file":     "computations/session-88/s88_gate_verdicts.txt",
        "module_detection": detection,
        "pinmap":           dict(sorted(pinmap.items())),
        "mcp_pre_compute_audit": {
            "tau_fold":             {"value": 0.19, "session": "S12/S42",
                                     "source": "s42_constants_snapshot.npz",
                                     "gate": "CONST-FREEZE-42"},
            "M_KK":                 {"value": 7.428660036284456e+16},
            "phi_67_phi_88_ratio":  {"value": "NOT FOUND in canonical_constants.py "
                                              "(plan §250 cites 7.324992 from S86 W-5 "
                                              "Sage-exact; promotion to canonical pending)"},
            "gv_canonical_difference_FW": {"value": -40579.1500479506,
                                           "provenance": "GV-Heitsch invariant difference on "
                                                         "(C_H, C_epsH) parity-twin pair at "
                                                         "canonical regulator; full float64 from "
                                                         "s84_w10a_115"},
            "HP1_dim":              {"value": 3.0},
            "trace_S86_W11_Bulletin_2": "no trace_entity hit (W-11 Bulletin #2 = even Seeley-DeWitt "
                                        "parity-blindness theorem at S85 W2-7 promotion; cited via "
                                        "permanent-results-registry.md §VII.AC.4 STAGE-3-PERMANENT)",
            "trace_eta_GV_parity_twin_signature": "no trace_entity hit; archive-script provenance "
                                                  "edges show s86_w11_eta_gv_joint_probe.py + "
                                                  "s87_w8_eta_gv_followup.py + s88_w3c_eta_gv_"
                                                  "regulator_independence.py exist with within-"
                                                  "script ad-hoc GV evaluation, NOT a shared module",
        },
        "blocking_prerequisite": {
            "symbol":          "S88-GV-HEITSCH-MODULE",
            "module_path":     str(GV_HEITSCH_MODULE_PATH.relative_to(PROJECT_ROOT)),
            "status":          detection["status"],
            "src_dir_listing": detection["src_listing"],
            "rationale":       ("Plan §W7c-86 machinery pin §247 names regulator_class = "
                                "'GV-Heitsch odd-grading'; the shared phonon-exflation-sim/"
                                "src/gv_heitsch.py module is absent at dispatch time. "
                                "Existing within-script implementations target only "
                                "(C_H, C_epsH); plan-required forward-scan to (C_n, C_epsN) "
                                "n ∈ {2, 4, 6} is structurally untestable without the "
                                "shared module's parity-twin pair construction API."),
        },
        "registry_slot_planned": GATE["registry_slot_planned"],
        "carry_forward":     ("S89-W9c-1-PARITY-TWIN-FORWARD-SCAN-RE-EMIT (after "
                              "S89-GV-HEITSCH-MODULE-LANDING). 4-field spec: (1) what: "
                              "implement gv_heitsch.py shared module exposing "
                              "parity_twin_pair_construct(n) + GV_evaluate(C_n) APIs "
                              "consistent with S86 W-11 / S87 W-8 within-script protocols; "
                              "(2) inputs: D_K_block_diagonal_cache, regulator atlas A_5_extended, "
                              "GV anchor (C_H, C_epsH); (3) gate: PASS iff parity_twin_pair_"
                              "construct(n=2,4,6) produces well-defined cocycles AND GV_n "
                              "evaluates non-zero AND ratios match substrate anchor 7.324992 "
                              "within 1%; (4) effort: 1.0 wave-equivalent."),
    }
    JSON_SIDECAR.write_text(
        json.dumps(sidecar, indent=2, sort_keys=False),
        encoding="utf-8",
    )


def update_wp_section(wp_text: str, detection: dict[str, object],
                      audit_sha: str, content_sha: str) -> str:
    """Replace placeholder Status / MCP Audit / Verdict / Results blocks
    in §W7c-86. Mirrors s88_w4b_pre_reg_inc_closure.py:update_wp_section.
    """
    sect_marker = f"### §{GATE['wp_id']}."                          # (local)
    sect_start = wp_text.index(sect_marker)                         # (local)
    sect_end = wp_text.index("\n---\n", sect_start)                 # (local)
    old_section = wp_text[sect_start:sect_end]                      # (local)
    new_section = old_section                                       # (local)

    # Status line
    new_section = new_section.replace(
        "**Status**: NOT STARTED",
        "**Status**: PRE-REG-INCOMPLETE (mechanical closure 2026-05-05 per orchestrator "
        "dispatch override + plan §W7c-86 machinery pin §247; deferred to S89)",
    )

    # MCP Pre-Compute Audit block
    mcp_old = (
        "**MCP Pre-Compute Audit**:\n"
        "*(pending — list the `mcp__knowledge__*` queries executed before writing the script, "
        "with one-line salient return each; mark PRE-CLOSED if a closure covers the gate. "
        "Per `.claude/rules/knowledge-index-usage.md`.)*"
    )                                                               # (local)
    mcp_new = (
        "**MCP Pre-Compute Audit**:\n\n"
        "  - `mcp__knowledge__get_constant('phi_67_phi_88_ratio')` → NOT FOUND "
        "(plan §250 cites 7.324992 from S86 W-5 Sage-exact; not yet pinned to "
        "canonical_constants.py; cited in registry §VII.AF.1 + W-5 Sage-exact ‖φ_67‖/‖φ_88‖)\n"
        "  - `mcp__knowledge__get_constant('tau_fold')` → 0.19 (S12/S42, "
        "s42_constants_snapshot.npz, gate=CONST-FREEZE-42, NOT superseded)\n"
        "  - `mcp__knowledge__get_constant('M_KK')` → 7.428660036284456e+16 "
        "(no PROVENANCE entry)\n"
        "  - `mcp__knowledge__get_constant('gv_canonical_difference_FW')` → "
        "-40579.1500479506 (S87, S84 W10-115 GV-Heitsch invariant difference on "
        "(C_H, C_epsH) parity-twin pair; canonical regulator)\n"
        "  - `mcp__knowledge__get_constant('HP1_dim')` → 3.0 (CM-2008 confirmed dimension)\n"
        "  - `mcp__knowledge__trace_entity('S86 W-11 Bulletin 2')` → no trace hit "
        "(the W-11 Bulletin #2 = even Seeley-DeWitt parity-blindness theorem promoted "
        "at S85 W2-7; cited via permanent-results-registry.md §VII.AC.4 STAGE-3-PERMANENT)\n"
        "  - `mcp__knowledge__trace_entity('eta GV parity-twin signature')` → no trace hit\n"
        "  - `mcp__knowledge__search_knowledge('GV-Heitsch HP1 odd-grading parity-blindness')` → "
        "20 results: archive-script edges show s86_w11_eta_gv_joint_probe.py + "
        "s87_w8_eta_gv_followup.py + s88_w3c_eta_gv_regulator_independence.py "
        "exist with within-script ad-hoc GV evaluation; **NO shared gv_heitsch.py module**; "
        "their inputs are (C_H, C_epsH)-only — forward-scan to (C_n, C_epsN) "
        "for n ∈ {2, 4, 6} not covered\n"
        "  - Filesystem grep `find . -name 'gv_heitsch*'` → no results\n"
        "  - Filesystem `ls phonon-exflation-sim/src/` → __init__.py, backend.py, "
        "defect_census.py, diagnostics.py, expansion.py, gpe_solver.py, "
        "initial_conditions.py, vortex_detection.py (NO gv_heitsch.py)\n\n"
        "**Conclusion**: Plan §W7c-86 machinery pin §247 names "
        "`regulator_class = \"GV-Heitsch odd-grading\"`; orchestrator dispatch override "
        "explicitly mandates: 'GV-Heitsch module: phonon-exflation-sim/src/gv_heitsch.py — "
        "if absent at dispatch-time, emit PRE-REG-INC per .claude/rules/mechanical-closure-"
        "discipline.md with value='PRE-REG-INC_blocked_by_S88-GV-HEITSCH-MODULE_status_absent'.' "
        "Module is genuinely absent. Proceed with mechanical PRE-REG-INC closure."
    )
    new_section = new_section.replace(mcp_old, mcp_new)

    # Verdict block
    verdict_old = "**Verdict**:\n*(pending agent execution)*"
    verdict_new = (
        f"**Verdict**: FAIL (PRE-REG-INC) — value={GATE['value']!r}\n\n"
        "Mechanical PRE-REG-INC closure per `.claude/rules/mechanical-closure-discipline.md` "
        "§\"When mechanical closure IS acceptable\". This gate's required upstream prerequisite "
        "— the shared `phonon-exflation-sim/src/gv_heitsch.py` module pinned by plan §W7c-86 "
        "machinery pin §247 (`regulator_class = \"GV-Heitsch odd-grading\"`) — has not landed "
        "in the codebase at dispatch time (2026-05-05). Per the orchestrator dispatch override "
        "(verbatim): \"GV-Heitsch module: phonon-exflation-sim/src/gv_heitsch.py — if absent "
        "at dispatch-time, emit PRE-REG-INC per .claude/rules/mechanical-closure-discipline.md "
        "with value='PRE-REG-INC_blocked_by_S88-GV-HEITSCH-MODULE_status_absent'.\" "
        "Plan §W7c overall §31 Decision Point Prerequisites also pre-registers PRE-REG-INC "
        "as the documented outcome for this prerequisite-block class.\n\n"
        "**Substitution chain — Step 4 NOT EXERCISED**: the directional prediction (η_n = 0 "
        "EXACTLY for even n; GV_n ≠ 0; ratio GV_n/GV_H consistent with substrate anchor "
        "‖φ_67‖/‖φ_88‖ = 7.324992 within 1%) was NOT computed because the producing "
        "machinery never ran. The substitution chain Step 1-Step 6 derivation (plan §266-294) "
        "remains valid as a structural prediction; it is reserved for the S89 re-emission gate.\n\n"
        f"**Required prerequisites and observed states**:\n"
        f"  - `S88-GV-HEITSCH-MODULE` "
        f"(`phonon-exflation-sim/src/gv_heitsch.py`): **ABSENT** "
        f"(value=module_not_on_filesystem) — BLOCKING\n\n"
        f"**4-tuple**: `(value={GATE['value']!r}, scheme={GATE['scheme']}, "
        f"convention={GATE['convention']}, L_max={GATE['L_max']})`\n\n"
        "**Per-pair table** (n ∈ {2, 4, 6}) — NOT EVALUATED:\n\n"
        "| n | η_n | GV_n | ratio GV_n/GV_H | substrate anchor 7.324992 dev |\n"
        "|---|-----|------|------------------|--------------------------------|\n"
        "| 2 | (not computed) | (not computed) | (not computed) | (not computed) |\n"
        "| 4 | (not computed) | (not computed) | (not computed) | (not computed) |\n"
        "| 6 | (not computed) | (not computed) | (not computed) | (not computed) |\n\n"
        "`pass_count_eta_zero_AND_GV_nonzero` = **N/A** (mechanical closure; gate not exercised). "
        "Per plan §258 thresholds: PASS at 3/3, INFO at 2/3, FAIL at ≤1/3 — none of these "
        "thresholds are exercisable without the GV-Heitsch evaluator.\n\n"
        "**Dual-SHA**:\n"
        f"  - `audit_sha256`: `{audit_sha}`\n"
        f"  - `content_sha256`: `{content_sha}`\n\n"
        "**S87+ schema-v2 3-tuple annotation**:\n"
        "  - `sign_verdict = N/A` — directional pre-registration (Step 4: even-grading → η=0; "
        "odd-grading → GV≠0; ratio preserved) was not exercised because the producing "
        "machinery never ran.\n"
        "  - `magnitude_verdict = FAIL` — gate produced no measurable value "
        "(`pass_count_eta_zero_AND_GV_nonzero` undefined).\n"
        "  - `regime_verdict = VALID` — no regime breakdown occurred since no regime was "
        "tested; L_max=10 substrate truncation would be VALID under Casimir-bound + "
        "Friedrich-Bär saturation IF actually exercised.\n"
        "  - Composite-collapse: `magnitude=FAIL + regime=VALID → composite=FAIL`.\n\n"
        "**Closure mechanism**: `computations/session-88/s88_w7c_parity_twin_forward_scan.py` "
        "(orchestrator-authored mechanical closure per `.claude/rules/mechanical-closure-"
        "discipline.md`, NOT specialist-agent dispatch). No physics computation was "
        "performed; the verdict line records that the gate could not be evaluated due "
        "to upstream prerequisite block. The pre-registered `.npz` and `.png` artifacts "
        "are NOT produced (mechanical closure is metadata-only); a JSON sidecar at "
        "`s88_w7c_parity_twin_forward_scan.json` records the closure's audit trail.\n\n"
        f"**Registry append**: NONE — registry-landing at planned slot "
        f"{GATE['registry_slot_planned']} (`sessions/permanent-results-registry.md`) "
        "is BLOCKED on upstream landing; entry deferred to S89+ re-emission gate."
    )
    new_section = new_section.replace(verdict_old, verdict_new)

    # Results block — find by start-marker, terminate at the next `)*` close
    res_start_marker = "**Results**:\n*(pending"                    # (local)
    if res_start_marker in new_section:
        rs = new_section.index(res_start_marker)                    # (local)
        re_close = new_section.index(")*", rs) + 2                  # (local)
        results_old = new_section[rs:re_close]                      # (local)
        results_new = (
            "**Results**: NONE — gate not executed; PRE-REG-INC closure only.\n\n"
            "**Solution-space interpretation**: The W7c-86 parity-twin forward-scan "
            "extension corridor remains UNTESTED at this session; this is a "
            "no-information outcome, NOT a corridor closure. The S86 W-11 Bulletin #2 "
            "(even Seeley-DeWitt parity-blindness theorem) at `permanent-results-registry.md` "
            "§VII.AC.4 STAGE-3-PERMANENT remains pinned at the n=H reference pair only; "
            "its generic-parity extension to (C_n, C_epsN) for n ∈ {2, 4, 6} is "
            "deferred to S89+ conditional on `S88-GV-HEITSCH-MODULE` (a shared "
            "`phonon-exflation-sim/src/gv_heitsch.py` module exposing parity-twin "
            "pair construction + GV evaluation APIs) landing.\n\n"
            "Plan §297-300 PASS/FAIL/INFO consequence states are deferred to S89+:\n"
            "  - PASS would have promoted Bulletin #2 from n=H-specific to "
            "generic-even-grading (registry §VII.AH.3 candidate);\n"
            "  - INFO at 2/3 would have routed to "
            "`S89-PARITY-TWIN-BOUNDARY-EFFECT-AUDIT` carry-forward;\n"
            "  - FAIL at ≤1/3 would have routed to a Class-(c) PIN-DRIFT-FROM-STALE-SOURCE "
            "narrowing entry per `regulator-pin-discipline.md` extension.\n\n"
            "All three outcome paths remain reachable; this PRE-REG-INC entry preserves "
            "the gate ID + dual-SHA + 4-tuple so that S89+ re-emission can be audit-traced "
            "back here.\n\n"
            "**Substrate framing** (5-element IS-not-IN block per "
            "`cross-pillar-bridge-anatomy.md` §\"IS-not-IN Anatomy\"; bridge-internal "
            "substrate-IS observable, no laboratory-IN counterpart at this gate):\n\n"
            "  1. **Substrate-IS observable** — `(η(C_n), GV(C_n))` pairs evaluated on "
            "`(A_K^{<=10}, H_K^{<=10}, D_K^{<=10})` for n ∈ {2, 4, 6}; cocycles `C_n` are "
            "n-th anomaly-coefficient cocycles in the Jensen-deformed band-0 spectrum at "
            "τ_fold = 0.190 — substrate-IS at the Level-1 single-τ-slice per "
            "`phononic-framing.md` §\"Single-τ-slice vs moduli-deformation substrate-IS levels\". "
            "These pairs ARE the framework's parity-asymmetric substrate content; no continuum "
            "geometric container exists for them.\n"
            "  2. **Laboratory-IN observable** — N/A. This gate is substrate-internal "
            "HP^1 cohomology probe; no laboratory-IN observable corresponds at this gate. "
            "Cross-pillar bridge to laboratory-IN observables (FWD-C3 Pillar IV ↔ Pillar V "
            "BdG inheritance morphism per `cross-pillar-bridge-anatomy.md` §\"Three forward "
            "bridge candidates for S88+ dispatch\") is registered separately at "
            "§VII.W-3.LAB STAGE-1-CANDIDATE (S88 W4a-17).\n"
            "  3. **Bridge map** — N/A at this gate; the rank-2 cocycle preservation "
            "structure (the substrate ratio ‖φ_67‖/‖φ_88‖ = 7.324992 anchor) is the "
            "INTERNAL substrate cohomology relation, not a bridge to laboratory measurement.\n"
            "  4. **Algebraic envelope** — rank-2 cocycle preservation per "
            "`inheritance-falsifier-protocol.md` §\"Two Test Classes\" Class B; the "
            "(Δ_B/Δ_A)^p cancellation theorem applies in principle but is not exercised "
            "(no laboratory mapping at this gate).\n"
            "  5. **Empirical anchor** — substrate anchor `‖φ_67‖/‖φ_88‖ = 7.324992` "
            "(S86 W-5 Sage-exact); plan §309 cites this as the ratio-preservation target. "
            "Anchor evaluation deferred to S89+.\n\n"
            "Per `phononic-framing.md` direction-of-explanation discipline, no "
            "substrate-IS-to-laboratory-IN mapping is asserted from a non-execution outcome; "
            "the substrate IS the parity-twin cocycle pairs at fixed τ_fold, and the "
            "(η=0, GV≠0) signature would CONFIRM the rank-2 substrate content, not "
            "explain the substrate via an external structure.\n\n"
            "**Class-(c) PIN-DRIFT-FROM-STALE-SOURCE proximity**: per "
            "`regulator-pin-discipline.md` §\"Class-(c) PIN-DRIFT-FROM-STALE-SOURCE — W-11 "
            "Calibration Corpus Extension\", joint-probe gates targeting HP^1 detection MUST "
            "use **odd-grading observables** (GV-Heitsch, K-theoretic torsion, η-Cheeger-"
            "Simons secondary classes) — never η alone. This gate's protocol uses BOTH η "
            "(even-grading expected = 0) AND GV (odd-grading expected ≠ 0); it is the "
            "canonical odd-grading + even-grading joint probe. Without the GV evaluator, "
            "the η-arm alone would re-test a structural law (Bulletin #2 promoted) and "
            "produce a Class-(c)-style stale-source FAIL. The mechanical closure is the "
            "structurally correct response: do NOT run the η-arm in isolation.\n\n"
            "**Carry-forward to S89+** (4-field spec per "
            "`feedback_fix-in-session-never-defer.md`):\n\n"
            "  1. **What**: implement `phonon-exflation-sim/src/gv_heitsch.py` shared module "
            "exposing `parity_twin_pair_construct(n)` + `GV_evaluate(C_n)` APIs consistent "
            "with S86 W-11 / S87 W-8 within-script protocols; lift the (C_H, C_epsH)-only "
            "ad-hoc evaluations to a generic n-parametrized parity-twin construction.\n"
            "  2. **Inputs**: D_K_block_diagonal_cache "
            "(`computations/session-84/s84_spectrum_cache_L12_tau019.npz`); regulator "
            "atlas A_5_extended; GV anchor (C_H, C_epsH) at "
            "`gv_canonical_difference_FW = -40579.1500479506`; substrate ratio "
            "anchor `‖φ_67‖/‖φ_88‖ = 7.324992` (S86 W-5 Sage-exact).\n"
            "  3. **Gate**: PASS iff `parity_twin_pair_construct(n=2,4,6)` produces "
            "well-defined cocycles AND `GV_n` evaluates non-zero AND ratios match "
            "substrate anchor 7.324992 within 1% AND `η_n` ≤ 1e-15 machine epsilon for "
            "all three n.\n"
            "  4. **Effort**: 1.0 wave-equivalent (module implementation 0.6 + parity-"
            "twin forward-scan re-emission 0.4 wave-equivalents).\n\n"
            "**K-counter advancement**: NONE — PRE-REG-INC verdicts do NOT count toward "
            "the cross-pillar-bridge-anatomy K-counter (this gate is bridge-internal, not "
            "a cross-pillar bridge candidate). The §VII.AH.3 generic-parity-promotion "
            "candidate slot remains UNALLOCATED until S89+ re-emission lands a verdict."
        )
        new_section = new_section.replace(results_old, results_new)

    return wp_text[:sect_start] + new_section + wp_text[sect_end:]


def main() -> int:
    print("=== S88 W7c-86 PRE-REG-INC mechanical closure ===")
    print(f"  Gate ID:    {GATE['gate_id']}")
    print(f"  WP ID:      §{GATE['wp_id']}")
    print(f"  Verdict:    FAIL (PRE-REG-INC)")
    print(f"  Value:      {GATE['value']!r}")
    print()

    # GV-Heitsch module detection
    detection = detect_gv_heitsch_module()                          # (local)
    print(f"=== GV-Heitsch module detection ===")
    print(f"  Module path:    {detection['module_path']}")
    print(f"  Status:         {detection['status']}")
    print(f"  src/ listing:   {detection['src_listing']}")
    print()

    if detection["status"] == "PRESENT":
        print("!! WARNING: gv_heitsch.py is PRESENT — orchestrator dispatch override "
              "PRE-REG-INC closure should NOT fire. Aborting.")
        return 2

    # Check for prior verdict-line emission (idempotency)
    verdict_text = VERDICT_TXT.read_text(encoding="utf-8")          # (local)
    prefix = GATE["gate_id"] + ":"                                  # (local)
    prior_lines = [ln for ln in verdict_text.splitlines()
                   if ln.startswith(prefix) and "audit_sha256=" in ln]  # (local)

    pinmap = build_pinmap(detection)                                # (local)

    if prior_lines:
        last = prior_lines[-1]                                      # (local)
        audit_sha = last.split("audit_sha256=", 1)[1].split()[0]    # (local)
        content_sha = last.split("content_sha256=", 1)[1].split()[0]    # (local)
        print(f"=== Recovered prior emission (idempotent re-run) ===")
        print(f"  audit_sha256:   {audit_sha}")
        print(f"  content_sha256: {content_sha}")
        appended = False                                            # (local)
    else:
        audit_sha, content_sha = compute_dual_sha(pinmap)           # (local)
        print(f"=== Computed dual-SHA ===")
        print(f"  audit_sha256:   {audit_sha}")
        print(f"  content_sha256: {content_sha}")
        # Append 3-row block: canonical line + dual-SHA companion + 3-tuple companion
        with VERDICT_TXT.open("a", encoding="utf-8") as fp:
            fp.write(make_verdict_line(audit_sha, content_sha))
            fp.write(make_companion_row(audit_sha, content_sha))
            fp.write(make_3tuple_annotation_row())
        print(f"  appended 3-row block to {VERDICT_TXT.relative_to(PROJECT_ROOT)}")
        appended = True                                             # (local)

    # JSON sidecar (always written; idempotent)
    write_json_sidecar(detection, pinmap, audit_sha, content_sha)
    print(f"=== Wrote {JSON_SIDECAR.relative_to(PROJECT_ROOT)} ===")

    # Update WP §W7c-86
    print(f"=== Updating WP §{GATE['wp_id']} in {WP_PATH.relative_to(PROJECT_ROOT)} ===")
    wp_text = WP_PATH.read_text(encoding="utf-8")
    if "**Status**: PRE-REG-INCOMPLETE" in wp_text:
        print(f"  WP §{GATE['wp_id']} already updated; skipping (idempotent)")
    else:
        wp_text = update_wp_section(wp_text, detection, audit_sha, content_sha)
        WP_PATH.write_text(wp_text, encoding="utf-8")
        print(f"  updated WP §{GATE['wp_id']}")

    print()
    print(f"=== S88-W7c-86 PRE-REG-INC closure: COMPLETE ===")
    print(f"  Verdict appended: {appended}")
    print(f"  Verdict file:     {VERDICT_TXT.relative_to(PROJECT_ROOT)}")
    print(f"  JSON sidecar:     {JSON_SIDECAR.relative_to(PROJECT_ROOT)}")
    print(f"  WP section:       §{GATE['wp_id']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
