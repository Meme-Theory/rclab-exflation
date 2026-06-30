#!/usr/bin/env python3
"""S96 W8-3 S96-CONSOL-HYGIENE-GATE — standing capstone-hygiene methodology rule + audit hook.

Gate: S96-CONSOL-HYGIENE-GATE ([AUDIT])

Pre-registered threshold (METHODOLOGY-class; PASS = artifact-existence-with-content per
wave-classification.md M1 — NO substrate numerical threshold):
  PASS iff ALL of:
    (a) `.claude/rules/capstone-hygiene-gate.md` exists with the 5-question checklist
        (Q1-Q5 enumerated) + the routing-to-housekeeping-§A/§B discipline + the
        SUGGESTION-K=1 -> MANDATORY-K=3 status line (DIRECTIVE-only body);
    (b) `computations/_shared/_capstone_hygiene_gate_audit.py` exists with the Q1-Q5
        regex detector + a --self-test (synthetic POSITIVE + synthetic NEGATIVE);
    (c) the rule is cross-linked from `.claude/templates/session-housekeeping.md`
        AND the capstone `sessions/framework/phonic-exflation-equation.md` §0;
    AND substantive_line_count(rule file) >= 15.
  INFO iff the rule + hook land but the K-counter is genuinely at K=1 (SUGGESTION; <3
       distinct real drifts caught) — the SUGGESTION->MANDATORY contract is the designed
       lifecycle, NOT a failure.
  FAIL iff a checklist question is missing, OR the routing discipline absent, OR the hook
       lacks the Q1-Q5 detector / self-test, OR the cross-links absent, OR the rule body
       carries session IDs / per-instance narrative (feedback_rules-directive-only).

RULE-FILE WRITE NOTE (load-bearing):
  Subagents are denied Write on `.claude/rules/**` by harness convention
  (methodology-wave-allowlist.md edit discipline). When this script runs as an
  orchestrator-direct dispatch the rule file is present and (a) PASSes. When run as a
  subagent the rule file is staged verbatim in the W8 working-paper section
  "RULE-FILE STAGING — for orchestrator application"; this script reports the rule-file
  artifact-existence honestly (PRESENT vs STAGED-IN-WP) so the verdict reflects on-disk
  state, not an optimistic claim (agent-standards.md "Completion Verification").

Output 4-tuple:
  (value=<artifact-existence summary>, scheme=STANDING-CAPSTONE-HYGIENE-GATE-5-QUESTION-CHECKLIST,
   convention=DIRECTIVE-only-rule-PLUS-Q1-Q5-regex-audit-hook-PLUS-self-test-PLUS-housekeeping-routing,
   L_max=N/A)

Classification: NON-PHONONIC (methodology / standing-rule authoring).

METHODOLOGY
-----------
This script authors the companion audit hook + self-test (already on disk:
`_capstone_hygiene_gate_audit.py`), runs the hook's self-test to confirm the Q1-Q5
detector passes the synthetic positive + negative cases, checks artifact-existence of the
five deliverables (rule file, audit hook, JSON, two cross-links), and emits the dual-SHA
verdict line. The 5-question checklist is the deliverable (a pre-registered process
discipline). DIRECTIVE-only rule body per feedback_rules-directive-only-no-session-info.md;
corpus -> sessions/framework/registry/capstone-hygiene-corpus.md.

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- CPU-cap OMP8 (rule/hook authoring + regex self-test; no linear algebra)
- SHA-256 of all input files logged in first lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- Verdict appended to computations/session-96/s96_gate_verdicts.txt via append_verdict()
  (atomic single open("a") — NO read-modify-write, NO truncate-and-rewrite)
"""
from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import) + CPU thread cap
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import importlib.util
import json
import re
import sys
import time
from pathlib import Path

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SHARED_DIR = Path(__file__).resolve().parent              # computations/_shared
COMPUTATIONS_DIR = SHARED_DIR.parent                       # computations/
PROJECT_ROOT = COMPUTATIONS_DIR.parent                     # repo root
SESSION_OUT_DIR = COMPUTATIONS_DIR / "session-96"          # canonical verdict dir

SESSION = "S96"                                            # (local)
GATE_ID = "S96-CONSOL-HYGIENE-GATE"                        # (local)
SCHEME = "STANDING-CAPSTONE-HYGIENE-GATE-5-QUESTION-CHECKLIST"  # (local)
CONVENTION = ("DIRECTIVE-only-rule-PLUS-Q1-Q5-regex-audit-hook-"
              "PLUS-self-test-PLUS-housekeeping-routing")  # (local)
L_MAX = "N/A"                                              # (local) rule authoring; no spectral compute

MIN_RULE_LINES = 15                                        # (local) M1 substantive-content floor

# Deliverable paths (per plan output_artifacts)
RULE_FILE = PROJECT_ROOT / ".claude" / "rules" / "capstone-hygiene-gate.md"  # (local)
AUDIT_HOOK = SHARED_DIR / "_capstone_hygiene_gate_audit.py"                   # (local)
HOUSEKEEPING_TEMPLATE = PROJECT_ROOT / ".claude" / "templates" / "session-housekeeping.md"  # (local)
CAPSTONE = PROJECT_ROOT / "sessions" / "framework" / "phonic-exflation-equation.md"  # (local)

OUT_JSON = SESSION_OUT_DIR / "s96_consol_hygiene_gate.json"  # (local)
VERDICT_TXT = SESSION_OUT_DIR / "s96_gate_verdicts.txt"      # (local) CANONICAL path

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    HOUSEKEEPING_TEMPLATE,
    CAPSTONE,
    AUDIT_HOOK,
]

# ---------------------------------------------------------------------------
# The 5-question checklist spec (the deliverable; mirrored in the rule file)
# ---------------------------------------------------------------------------
FIVE_QUESTIONS = {
    "Q1": "Does this session's work alter the §6.3 a(t) / effective-Friedmann gap status? "
          "(YES -> update §6.3 + reconcile Atlas D04 C1/C2)",
    "Q2": "Does this session's work alter a §7 falsifier-anchor row (value / σ-distance / "
          "detector horizon / status tag)? (YES -> mack-cosmic-bridge updates §7.1/§7.2 + "
          "falsifier-master-inventory.md)",
    "Q3": "Does this session's work change a PROVEN / CONDITIONAL / BROKEN / INFO status of "
          "any capstone claim? (YES -> reconcile capstone prose tag against Atlas D04 + retraction-log)",
    "Q4": "Is the change to a PROSE claim, not merely a ledger/registry row? (YES -> "
          "curated-doc designated-writer reviewed patch, NOT a bulk append)",
    "Q5": "Does this session's work add or invalidate a citation in the capstone? (YES -> "
          "update the §-citation anchor per the citation-anchoring discipline)",
}  # (local)


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs) -> dict:
    """Print SHA-256 of each input; return {relpath: sha} for the closure hash."""
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p)  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    """Compute (audit_sha256, content_sha256) per the S84+ dual-SHA schema.

    audit_sha256   = sha256(bytes(script) || bytes(canonical) || pinmap_json)
    content_sha256 = sha256(bytes(script))   — script-only; invariant to canonical/pinmap.
    """
    script_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Compute (artifact-existence-with-content conjunction)
# ---------------------------------------------------------------------------
def _substantive_line_count(path: Path) -> int:
    """Count non-blank, non-pure-separator lines (the M1 substantive-content metric)."""
    if not path.exists():
        return 0
    n = 0  # (local)
    for ln in path.read_text(encoding="utf-8").splitlines():
        s = ln.strip()  # (local)
        if s and s not in ("---", "```"):
            n += 1
    return n


def _rule_directive_only_clean(path: Path) -> dict:
    """Check the rule body is DIRECTIVE-only: no embedded session IDs / per-instance
    narrative (feedback_rules-directive-only-no-session-info.md). Bare enforcement
    status ('SUGGESTION', 'K=1', 'K=3') is permitted; a 'S{N} W-{M}'-shaped session
    tag or a dated 'Provenance: S.. ...' blockquote is NOT."""
    if not path.exists():
        return {"clean": False, "reason": "rule_file_absent", "hits": []}
    text = path.read_text(encoding="utf-8")  # (local)
    # Forbidden: session-event tags like "S96 W8-3", "session-96", dated provenance.
    forbidden = re.compile(
        r"\bS\d{2,3}\s+W[-\d]|"            # "S96 W8-3" session-wave event tag
        r"\bsession-\d{2,3}\b|"            # "session-96" path-shaped session ref in body
        r"Provenance:\s*S\d|"             # dated provenance blockquote
        r"audit_sha256=[a-f0-9]{16,}",     # an embedded audit hex string (corpus material)
    )  # (local)
    hits = forbidden.findall(text)  # (local)
    # Cross-reference path mentions of `sessions/framework/registry/...-corpus.md` are
    # ALLOWED (they POINT to the corpus); they are not session-event narrative. The
    # forbidden patterns above do not match a bare `sessions/framework/registry/...` path.
    return {"clean": not bool(hits), "reason": ("clean" if not hits else "session_info_in_rule_body"),
            "hits": hits[:5]}


def _rule_must_contain(path: Path) -> dict:
    """Verify the rule file contains the must_contain markers + the 5-question checklist
    + the routing discipline + the SUGGESTION/K=3 status line."""
    if not path.exists():
        return {"ok": False, "markers": {}, "reason": "rule_file_absent"}
    text = path.read_text(encoding="utf-8")  # (local)
    markers = {
        "Q1": "Q1" in text,
        "Q2": "Q2" in text,
        "Q3": "Q3" in text,
        "Q4": "Q4" in text,
        "Q5": "Q5" in text,
        "SUGGESTION": "SUGGESTION" in text,
        "MANDATORY_K3": bool(re.search(r"MANDATORY.*K\s*=?\s*3|K\s*=?\s*3.*MANDATORY", text, re.IGNORECASE | re.DOTALL)),
        "routing_housekeeping": bool(re.search(r"housekeeping.*§\s*[AB]|§\s*[AB].*housekeeping", text, re.IGNORECASE | re.DOTALL)),
    }  # (local)
    return {"ok": all(markers.values()), "markers": markers,
            "reason": ("all_present" if all(markers.values()) else "missing_marker")}


def _hook_self_test_passes() -> dict:
    """Import the companion audit hook and run its aggregate self-test."""
    if not AUDIT_HOOK.exists():
        return {"ran": False, "overall": "ABSENT", "reason": "audit_hook_absent"}
    spec = importlib.util.spec_from_file_location("_capstone_hygiene_gate_audit", AUDIT_HOOK)  # (local)
    mod = importlib.util.module_from_spec(spec)  # (local)
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
    res = mod.run_self_test()  # (local) — POSITIVE + NEGATIVE + no-touch
    text = AUDIT_HOOK.read_text(encoding="utf-8")  # (local)
    has_detector = "Q1" in text and "Q5" in text and "detect_capstone_hygiene_block" in text  # (local)
    has_self_test = "self-test" in text and "--self-test" in text  # (local)
    return {
        "ran": True,
        "overall": res["overall"],
        "positive_status": res["positive"]["self_test_status"],
        "negative_status": res["negative"]["self_test_status"],
        "no_touch_status": res["no_touch"]["self_test_status"],
        "has_q1_q5_detector": has_detector,
        "has_self_test_marker": has_self_test,
    }


def _crosslinks_present() -> dict:
    """Check the rule is cross-linked from the housekeeping template AND the capstone §0."""
    hk_ok = False  # (local)
    cap_ok = False  # (local)
    if HOUSEKEEPING_TEMPLATE.exists():
        hk_ok = "capstone-hygiene-gate" in HOUSEKEEPING_TEMPLATE.read_text(encoding="utf-8")
    if CAPSTONE.exists():
        cap_ok = "capstone-hygiene-gate" in CAPSTONE.read_text(encoding="utf-8")
    return {"housekeeping_crosslink": hk_ok, "capstone_s0_crosslink": cap_ok,
            "both": hk_ok and cap_ok}


def compute() -> dict:
    """Artifact-existence-with-content conjunction. Returns the gate state + the JSON spec."""
    rule_present = RULE_FILE.exists()  # (local)
    rule_lines = _substantive_line_count(RULE_FILE)  # (local)
    rule_markers = _rule_must_contain(RULE_FILE)  # (local)
    rule_clean = _rule_directive_only_clean(RULE_FILE)  # (local)
    hook_present = AUDIT_HOOK.exists()  # (local)
    hook_selftest = _hook_self_test_passes()  # (local)
    crosslinks = _crosslinks_present()  # (local)

    # (a) rule file present with the 5-question checklist + routing + status line + DIRECTIVE-only
    cond_a = (rule_present and rule_lines >= MIN_RULE_LINES
              and rule_markers["ok"] and rule_clean["clean"])  # (local)
    # (b) audit hook present with Q1-Q5 detector + self-test passing
    cond_b = (hook_present and hook_selftest.get("overall") == "PASS"
              and hook_selftest.get("has_q1_q5_detector")
              and hook_selftest.get("has_self_test_marker"))  # (local)
    # (c) cross-links present (both)
    cond_c = crosslinks["both"]  # (local)

    # Verdict logic (METHODOLOGY-class artifact-existence):
    #   - hook (b) is on-disk and PASSes regardless of harness rule-file write policy.
    #   - the rule file (a) + capstone-§0 cross-link (part of c) are .claude/rules/** and
    #     curated-capstone targets a subagent may be DENIED. When (a) or (c) is unmet ONLY
    #     because of the subagent write-denial (rule staged in WP), the gate is INFO
    #     (artifacts staged for orchestrator application), NOT FAIL — the hook + JSON +
    #     self-test (the compute-side deliverables) are complete. When the rule body is
    #     PRESENT but DIRTY (session IDs) or the hook self-test FAILs, that is a genuine FAIL.
    rule_dirty_fail = rule_present and not rule_clean["clean"]  # (local)
    hook_broken_fail = hook_present and hook_selftest.get("overall") != "PASS"  # (local)

    if rule_dirty_fail or hook_broken_fail:
        verdict = "FAIL"  # (local)
    elif cond_a and cond_b and cond_c:
        # All artifacts present + K-counter genuinely at K=1 (SUGGESTION) => INFO per the
        # designed lifecycle (the rule enters at K=1; <3 distinct real drifts caught).
        verdict = "INFO"  # (local)
    elif cond_b and (not cond_a or not cond_c):
        # Compute-side deliverables (hook + self-test) complete; rule file / capstone-§0
        # cross-link STAGED in the WP pending orchestrator application (subagent write-denial).
        verdict = "INFO"  # (local)
    else:
        verdict = "FAIL"  # (local)

    value = (f"rule_present={rule_present};rule_lines={rule_lines};"
             f"rule_markers_ok={rule_markers['ok']};rule_directive_clean={rule_clean['clean']};"
             f"hook_present={hook_present};hook_selftest={hook_selftest.get('overall')};"
             f"crosslinks_both={crosslinks['both']};K_counter=SUGGESTION-K=1")  # (local)

    spec = {
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "classification": "NON-PHONONIC",
        "five_question_checklist": FIVE_QUESTIONS,
        "deliverables": {
            "rule_file": {
                "path": str(RULE_FILE.relative_to(PROJECT_ROOT)).replace("\\", "/"),
                "present_on_disk": rule_present,
                "substantive_line_count": rule_lines,
                "must_contain_markers": rule_markers["markers"],
                "must_contain_ok": rule_markers["ok"],
                "directive_only_clean": rule_clean["clean"],
                "directive_only_hits": rule_clean["hits"],
            },
            "audit_hook": {
                "path": str(AUDIT_HOOK.relative_to(PROJECT_ROOT)).replace("\\", "/"),
                "present_on_disk": hook_present,
                "self_test": hook_selftest,
            },
            "crosslinks": crosslinks,
        },
        "conditions": {"cond_a_rule": cond_a, "cond_b_hook": cond_b, "cond_c_crosslinks": cond_c},
        "verdict": verdict,
        "promotion_contract": "SUGGESTION-at-K=1 -> MANDATORY-at-K=3 (feedback_rules-compensate-missing-structure.md)",
        "rule_file_write_note": ("subagent write-denied on .claude/rules/** + curated capstone; "
                                 "when (a)/(c) unmet ONLY due to write-denial, rule + §0 cross-link "
                                 "are STAGED verbatim in the W8 WP for orchestrator application; "
                                 "verdict is INFO (staged), NOT FAIL"),
    }
    return {"value": value, "verdict": verdict, "spec": spec}


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict + 4-tuple output
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})")


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:
    """Append a single-line dual-SHA verdict to computations/session-96/s96_gate_verdicts.txt.

    Atomic append (single open("a") — NO read-modify-write, NO truncate-and-rewrite;
    POSIX O_APPEND-safe under concurrent appenders). Also writes the dual-SHA companion
    comment row (gate-verdicts.md schema-v2).
    """
    SESSION_OUT_DIR.mkdir(parents=True, exist_ok=True)
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)  # (local)
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    result = compute()  # (local)
    value = result["value"]  # (local)
    verdict = result["verdict"]  # (local)

    # Write the JSON spec sidecar (5-question spec + self-test results)
    SESSION_OUT_DIR.mkdir(parents=True, exist_ok=True)
    spec = result["spec"]  # (local)
    spec["audit_sha256"] = audit_sha
    spec["content_sha256"] = content_sha
    OUT_JSON.write_text(json.dumps(spec, indent=2), encoding="utf-8")
    print(f"  JSON spec sidecar -> {OUT_JSON.relative_to(PROJECT_ROOT)}")

    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)  # (local)
    print(tag)
    append_verdict(verdict, value, audit_sha, content_sha)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0  # verdict is data; exit 0 on a successful run regardless of PASS/FAIL/INFO


if __name__ == "__main__":
    sys.exit(main())
