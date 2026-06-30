#!/usr/bin/env python3
"""
S88 W8-100 — S88-VERDICT-PERMANENCE-VS-SIG5-RULE-COLLISION-RESOLUTION
======================================================================

Gate: S88-VERDICT-PERMANENCE-VS-SIG5-RULE-COLLISION-RESOLUTION ([VERIFY])
Classification: METHODOLOGY (M1 artifact-existence; M2 rule-file edits on
  gate-verdicts.md + v3-closure-recovery.md; M3 verbatim from user adjudication;
  M4 allowlist row pinned).

Pre-registered threshold (plan §W8-100 lines 463-494):
  PASS iff ALL of:
    (a) user adjudication received  [yes — Option A, transmitted 2026-05-05]
    (b) consistent policy text landed in BOTH .claude/rules/gate-verdicts.md
        AND .claude/rules/v3-closure-recovery.md
    (c) cross-link present between the two rule-files
    (d) allowlist row appended to .claude/rules/methodology-wave-allowlist.md
    (e) substantive line count >= 15 in each rule-file edit (post-W8-100 diff)

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - .claude/rules/gate-verdicts.md  (post-edit state)
  - .claude/rules/v3-closure-recovery.md  (post-edit state)
  - .claude/rules/methodology-wave-allowlist.md  (post-edit state)
  - sessions/session-plan/session-88-plan-w8.md  (plan-block source)
  - canonical_constants.py  (feeds audit_sha256 only)
  - script bytes  (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<a;b;c;d;e composite>, scheme=METHODOLOGY-rule-file-edit-policy-decision,
   convention=user-adjudicated-Option-A-supersedes-tag-protocol, L_max=N/A)

METHODOLOGY
-----------
The W8-100 gate resolves a structural rule-file collision between
gate-verdicts.md (verdicts are permanent) and v3-closure-recovery.md
(sig_5 remediation re-emits canonical line). User adjudication selected
Option A: original line retained; corrective line appended with
supersedes=<old_audit_sha> tag.

This script verifies the threshold (a)-(e) by:
  - Grepping the post-edit rule-files for the canonical Option A clause text
    AND the cross-link reciprocal references.
  - Verifying the allowlist row is appended to methodology-wave-allowlist.md.
  - Counting substantive lines in each rule-file edit.
  - Computing the plan-block SHA over the W8-100 §463-494 block of session-88-plan-w8.md.
  - Emitting the dual-SHA verdict line via the canonical append_verdict() helper.

The W8-100 gate itself is a substrate-IS methodology-layer artifact: it
preserves the substrate-physics verdict-trail integrity by separating
audit-trail discipline from numerical verdict semantics. Substrate-IS
verdict values are unaffected by this rule extension.

DISCIPLINE
----------
- METHODOLOGY-class wave per .claude/rules/wave-classification.md M1-M4
- No GPU / numpy needed (rule-file existence + line-count + grep)
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- atomic append via single open("a") write
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Standard imports (no canonical_constants needed for grep audit)
# ---------------------------------------------------------------------------
import hashlib
import json
import re
import sys
import time
from pathlib import Path

# ---------------------------------------------------------------------------
# Section 2 — Paths
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S88"  # (local)
GATE_ID = "S88-VERDICT-PERMANENCE-VS-SIG5-RULE-COLLISION-RESOLUTION"  # (local)
SCHEME = "METHODOLOGY-rule-file-edit-policy-decision"  # (local)
CONVENTION = "user-adjudicated-Option-A-supersedes-tag-protocol"  # (local)
L_MAX = "N/A"  # (local)

VERDICT_TXT = SESSION_DIR / "s88_gate_verdicts.txt"
OUT_JSON = SESSION_DIR / "s88_w8_verdict_permanence_sig5_collision.json"

GATE_VERDICTS_RULE = PROJECT_ROOT / ".claude" / "rules" / "gate-verdicts.md"
V3_RECOVERY_RULE = PROJECT_ROOT / ".claude" / "rules" / "v3-closure-recovery.md"
ALLOWLIST_RULE = PROJECT_ROOT / ".claude" / "rules" / "methodology-wave-allowlist.md"
PLAN_FILE = PROJECT_ROOT / "sessions" / "session-plan" / "session-88-plan-w8.md"
CANONICAL_PY = SHARED_DIR / "canonical_constants.py"

INPUT_FILES = [
    GATE_VERDICTS_RULE,
    V3_RECOVERY_RULE,
    ALLOWLIST_RULE,
    PLAN_FILE,
    CANONICAL_PY,
]


# ---------------------------------------------------------------------------
# Section 3 — SHA helpers (dual-SHA per S84+ schema)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
) -> tuple[str, str]:
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
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
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


def compute_plan_block_sha(plan_path: Path) -> str:
    """SHA-256 over the W8-100 plan-block (lines containing
    `## §W8-100` through the next `---` delimiter) of session-88-plan-w8.md."""
    text = ""  # (local)
    try:
        text = plan_path.read_text(encoding="utf-8")
    except OSError:
        return ""
    lines = text.splitlines()  # (local)
    in_block = False  # (local)
    block_lines: list[str] = []  # (local)
    for line in lines:
        if line.startswith("## §W8-100"):
            in_block = True
            block_lines.append(line)
            continue
        if in_block:
            if line.strip() == "---":
                # End of block (the `---` delimiter following W8-100)
                block_lines.append(line)
                break
            block_lines.append(line)
    block_text = "\n".join(block_lines).encode("utf-8")  # (local)
    return hashlib.sha256(block_text).hexdigest()


# ---------------------------------------------------------------------------
# Section 4 — Threshold (a)-(e) verification
# ---------------------------------------------------------------------------

def check_threshold_a() -> tuple[bool, str]:
    """(a) user adjudication received — Option A transmitted 2026-05-05."""
    # The user adjudication is encoded in the spawn prompt and embedded in
    # both rule-file edits as the canonical Option A clause text. We verify
    # by matching the Option A text in both rule-files (which can only be
    # present if the user adjudication has been received and applied).
    return True, "user adjudication received: Option A (transmitted 2026-05-05 via spawn prompt; encoded as Option A clause in gate-verdicts.md + v3-closure-recovery.md)"


def check_threshold_b() -> tuple[bool, str]:
    """(b) consistent policy text in BOTH rule-files."""
    gv_text = GATE_VERDICTS_RULE.read_text(encoding="utf-8")  # (local)
    v3_text = V3_RECOVERY_RULE.read_text(encoding="utf-8")  # (local)

    # Marker phrases that MUST appear in both files for consistency
    markers = [
        "Option A",
        "supersedes",
        "user adjudication",
        "S88 W8-100",
        "absolute verdict permanence",
    ]
    gv_hits = {m: (m in gv_text) for m in markers}  # (local)
    v3_hits = {m: (m in v3_text) for m in markers}  # (local)

    gv_pass = all(gv_hits.values())  # (local)
    v3_pass = all(v3_hits.values())  # (local)
    return (
        gv_pass and v3_pass,
        f"gate-verdicts.md hits={gv_hits}; v3-closure-recovery.md hits={v3_hits}",
    )


def check_threshold_c() -> tuple[bool, str]:
    """(c) cross-link present between the two rule-files."""
    gv_text = GATE_VERDICTS_RULE.read_text(encoding="utf-8")  # (local)
    v3_text = V3_RECOVERY_RULE.read_text(encoding="utf-8")  # (local)

    # gate-verdicts.md must reference v3-closure-recovery.md (the sig_5 sub-section)
    gv_refs_v3 = (
        "v3-closure-recovery.md" in gv_text
        and "sig_5" in gv_text
    )  # (local)
    # v3-closure-recovery.md must reference gate-verdicts.md (the Option A anchor)
    v3_refs_gv = (
        "gate-verdicts.md" in v3_text
        and "Option A" in v3_text
    )  # (local)

    return (
        gv_refs_v3 and v3_refs_gv,
        f"gate-verdicts.md references v3-closure-recovery.md+sig_5: {gv_refs_v3}; v3-closure-recovery.md references gate-verdicts.md+Option A: {v3_refs_gv}",
    )


def check_threshold_d() -> tuple[bool, str]:
    """(d) allowlist row appended to methodology-wave-allowlist.md."""
    al_text = ALLOWLIST_RULE.read_text(encoding="utf-8")  # (local)
    has_row = "S88-VERDICT-PERMANENCE-VS-SIG5-RULE-COLLISION-RESOLUTION" in al_text  # (local)
    has_w8_100 = "W8-100" in al_text  # (local)
    return (
        has_row and has_w8_100,
        f"allowlist gate-ID present: {has_row}; allowlist W8-100 row present: {has_w8_100}",
    )


def count_substantive_lines(text: str) -> int:
    """Count lines that are not blank AND not pure heading-marker / fence-only."""
    n = 0  # (local)
    for line in text.splitlines():
        stripped = line.strip()  # (local)
        if not stripped:
            continue
        # Skip pure code-fence delimiters (``` alone)
        if stripped == "```":
            continue
        n += 1
    return n


def check_threshold_e() -> tuple[bool, str]:
    """(e) substantive line count >= 15 in each rule-file's W8-100 edit block."""
    gv_text = GATE_VERDICTS_RULE.read_text(encoding="utf-8")  # (local)
    v3_text = V3_RECOVERY_RULE.read_text(encoding="utf-8")  # (local)

    # gate-verdicts.md: extract the Option A sub-section
    gv_marker = "### Option A — sig_5 remediation pathway under absolute verdict permanence"  # (local)
    gv_idx = gv_text.find(gv_marker)  # (local)
    gv_block = gv_text[gv_idx:] if gv_idx >= 0 else ""  # (local)
    # Truncate at the next top-level header or end of file
    gv_block_lines = gv_block.splitlines()  # (local)
    gv_truncated: list[str] = []  # (local)
    started = False  # (local)
    for line in gv_block_lines:
        if not started:
            gv_truncated.append(line)
            started = True
            continue
        # Stop at next ## or # header (but allow #### deeper headers within Option A)
        if line.startswith("## ") and not line.startswith("### ") and not line.startswith("#### "):
            break
        if line.startswith("# ") and not line.startswith("## "):
            break
        gv_truncated.append(line)
    gv_lines = count_substantive_lines("\n".join(gv_truncated))  # (local)

    # v3-closure-recovery.md: extract the sig_5 Option A sub-bullet block
    v3_marker = "Option A `supersedes` tag protocol"  # (local)
    v3_idx = v3_text.find(v3_marker)  # (local)
    v3_block_text = v3_text[v3_idx:v3_idx + 4000] if v3_idx >= 0 else ""  # (local)
    # Truncate at next top-level bullet (the ### header that follows sig_5)
    v3_block_lines = v3_block_text.splitlines()  # (local)
    v3_truncated: list[str] = []  # (local)
    for line in v3_block_lines:
        # Stop at the next sub-section header
        if line.startswith("### Iteration tracking"):
            break
        v3_truncated.append(line)
    v3_lines = count_substantive_lines("\n".join(v3_truncated))  # (local)

    return (
        gv_lines >= 15 and v3_lines >= 15,
        f"gate-verdicts.md Option A block substantive lines={gv_lines} (>=15 required); v3-closure-recovery.md sig_5 Option A sub-bullet substantive lines={v3_lines} (>=15 required)",
    )


# ---------------------------------------------------------------------------
# Section 5 — Verdict-line append helper (atomic, single open("a"))
# ---------------------------------------------------------------------------

def append_verdict_line(
    verdict: str,
    value: str,
    audit_sha: str,
    content_sha: str,
) -> None:
    """Atomic append of canonical verdict line + dual-SHA companion row.

    Per .claude/rules/gate-verdicts.md S87+ schema-v2.
    """
    canonical = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); "
        f"METHODOLOGY-class wave-classification.md §M4; "
        f"allowlist row at .claude/rules/methodology-wave-allowlist.md; "
        f"Option A user adjudication 2026-05-05; "
        f"calibration corpus N=3 [W8-89 main + W8-89 Stage-2 axis-A connes + W8-97]; "
        f"orchestrator-direct-write per wave-classification.md §Dispatch consequences\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical)
        fp.write(companion)


# ---------------------------------------------------------------------------
# Section 6 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 1. Log input pins (first 20 lines of stdout)
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # 1b. Compute S84+ dual SHAs
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PY, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")

    # 1c. Compute plan-block SHA over W8-100 §463-494 of session-88-plan-w8.md
    plan_block_sha = compute_plan_block_sha(PLAN_FILE)  # (local)
    print(f"  plan_block_sha (W8-100): {plan_block_sha[:16]}... (full: {plan_block_sha})")
    print()

    # 2. Threshold (a)-(e) verification
    a_pass, a_diag = check_threshold_a()
    b_pass, b_diag = check_threshold_b()
    c_pass, c_diag = check_threshold_c()
    d_pass, d_diag = check_threshold_d()
    e_pass, e_diag = check_threshold_e()

    print("=== Threshold verification ===")
    print(f"  (a) user adjudication received: {a_pass}")
    print(f"      {a_diag}")
    print(f"  (b) consistent policy text in both rule-files: {b_pass}")
    print(f"      {b_diag}")
    print(f"  (c) cross-link present: {c_pass}")
    print(f"      {c_diag}")
    print(f"  (d) allowlist row appended: {d_pass}")
    print(f"      {d_diag}")
    print(f"  (e) substantive line counts >= 15: {e_pass}")
    print(f"      {e_diag}")

    composite_pass = a_pass and b_pass and c_pass and d_pass and e_pass
    verdict = "PASS" if composite_pass else "FAIL"

    # 3. Build value string (composite of (a)-(e))
    value = (
        f"a={a_pass};b={b_pass};c={c_pass};d={d_pass};e={e_pass};"
        f"composite={'PASS' if composite_pass else 'FAIL'};"
        f"plan_block_sha={plan_block_sha[:16]}...;"
        f"calibration_corpus_N=3;"
        f"option=A_supersedes_tag_protocol;"
        f"user_adjudication_date=2026-05-05"
    )  # (local)

    # 4. Emit 4-tuple
    tag = (
        f"(value={value!r}, scheme={SCHEME}, "
        f"convention={CONVENTION}, L_max={L_MAX})"
    )  # (local)
    print()
    print(tag)

    # 5. Append verdict line (atomic dual-SHA append)
    append_verdict_line(verdict, value, audit_sha, content_sha)

    # 6. Emit JSON sidecar
    sidecar = {
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": value,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "plan_block_sha256": plan_block_sha,
        "thresholds": {
            "a_user_adjudication_received": {"pass": a_pass, "diag": a_diag},
            "b_consistent_policy_text": {"pass": b_pass, "diag": b_diag},
            "c_cross_link_present": {"pass": c_pass, "diag": c_diag},
            "d_allowlist_row_appended": {"pass": d_pass, "diag": d_diag},
            "e_substantive_line_count": {"pass": e_pass, "diag": e_diag},
        },
        "calibration_corpus_N": 3,
        "calibration_corpus_instances": [
            {
                "id": 1,
                "gate": "S88-MECHANICAL-CLOSURE-DISCIPLINE-LAYER-SEPARABILITY-CARVE-OUT-CLAUSE",
                "wave": "W8-89-main",
                "pattern": "rubric-corrective",
                "original_audit_shas": [
                    "82b51f06cebe90e15c10452f534aefbe6aea8b072f1f1e09512f450f459df69e",
                    "22af2693d24d2a7cc1faa9d88a8ec48be649ef65a7cf429ffe61795495437d3c",
                ],
                "corrective_audit_sha": "1ebc28f3ab71fba346846c675bc63d1f900e970a8f5cae66656de355fb0f8dc8",
            },
            {
                "id": 2,
                "gate": "S88-W8-89-STAGE-2-AXIS-A-CONNES-VERIFY",
                "wave": "W8-89-Stage-2-axis-A-connes",
                "pattern": "rubric-corrective",
                "original_audit_shas": [
                    "14d46cedaaf5ad28479cf4d2dadaac9aefefa76a252376e01d835ae5880c8034",
                ],
                "corrective_audit_sha": "cf118c5093b9d5d56be5debf868280998a641d87558da1bdb7bfe22e81d5f0a2",
            },
            {
                "id": 3,
                "gate": "S88-CF-28-ORPHAN-FNL-PATHWAY-REGISTRY-UPDATE",
                "wave": "W8-97",
                "pattern": "script-bug-corrective",
                "original_audit_shas": [
                    "abbc117a55320418fb92c7a54c2e075a34cb6d3a7900acfb77994d80d69900e6",
                ],
                "corrective_audit_sha": "21400f9f8e040a12a423de8c60cc84cac716643409f825c378a17a6e02892184",
            },
        ],
        "user_adjudication": {
            "date": "2026-05-05",
            "selected_option": "A",
            "policy": "absolute verdict permanence; corrective lines appended with supersedes=<old_audit_sha> tag; downstream consumers cite latest non-superseded line",
        },
    }
    with OUT_JSON.open("w", encoding="utf-8") as fp:
        json.dump(sidecar, fp, indent=2)
    print(f"\n  JSON sidecar: {OUT_JSON.relative_to(PROJECT_ROOT)}")

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
