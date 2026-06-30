#!/usr/bin/env python3
"""
S84 W10a-112 — S84-S80-HEADER-REPAIR
====================================

Gate: S84-S80-HEADER-REPAIR ([AUDIT])

Pre-registered threshold:
  PASS: All 6 W1 headers updated to match their body-verdict strings;
        a follow-up audit pass confirms zero mismatches.
  FAIL: One or more header updates introduces a new inconsistency.
  INFO (PRE-REG-INCOMPLETE): A header has no extractable body verdict
        (body still stub) — mark PRE-REG-INCOMPLETE for that header.

ADAPTATION NOTE (2026-04-19):
  The plan (§W10a-112 lines 144-183) pre-registered the header pattern
    `## W1-N <slug> — <status>`  (2-hash level 2; status STRING in header)
  but the actual S80 file `sessions/archive/session-80/session-80-results-workingpaper.md`
  uses
    `### W1-N: <SLUG> — EVOI <value> (<owner>)`  (3-hash level 3; NO status string)
  with the status carried on the line immediately below as
    `**Status**: <STATUS>`
  Per `.claude/rules/gate-verdicts.md`, a gate whose pre-registered
  machinery does not match the actual file structure is PRE-REG-INCOMPLETE.
  This gate therefore returns INFO-PRE-REG-INCOMPLETE-PATTERN; we still
  produce a derivative reconciliation patch (Status-line vs body-verdict)
  as a reconstruction protocol so the next session can act on it.

  Plan's source_file `sessions/archive/session-80/session-80-plan.md` does not
  exist; the only S80 markdown is `session-80-results-workingpaper.md`.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - sessions/archive/session-80/session-80-results-workingpaper.md
  - computations/session-80/s80_gate_verdicts.txt
  - canonical_constants.py (audit_sha256 only)
  - script bytes (BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<count_repaired>, scheme=header_body_consistency,
   convention=s80_w1_only, L_max=N/A)

Classification: NON-PHONONIC (documentation repair)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import difflib
import hashlib
import json
import re
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


# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
SESSION_80_DIR = PROJECT_ROOT / "sessions" / "session-80"
SESSION_84_DIR = PROJECT_ROOT / "sessions" / "session-84"
ARTIFACTS_DIR = SESSION_84_DIR / "computation-artifacts"

SESSION = "S84"                                                    # (local)
GATE_ID = "S84-S80-HEADER-REPAIR"                                  # (local)
SCHEME = "header_body_consistency"                                 # (local)
CONVENTION = "s80_w1_only"                                         # (local)
L_MAX = "N/A"                                                      # (local)
N_EVAL = 6                                                         # (local)

S80_FILE = SESSION_80_DIR / "session-80-results-workingpaper.md"
S80_VERDICTS = resolve_output(80, 's80_gate_verdicts.txt')
CANONICAL_CONSTANTS = resolve_script(None, 'canonical_constants.py')
DIFF_OUT = ARTIFACTS_DIR / "s84_w10a_112_s80_header_diff.patch"
VERDICT_FILE = resolve_output(84, 's84_gate_verdicts.txt')

# Plan-pre-registered pattern (2-hash, status in header)
PLAN_HEADER_PATTERN = r"^## W1-(\d+) (.+?) — (.+)$"                # (local)

# Actual S80 file pattern (3-hash, no status; status on next line)
ACTUAL_HEADER_PATTERN = r"^### W1-(\d+):\s+(.+?)$"                 # (local)
ACTUAL_STATUS_PATTERN = r"^\*\*Status\*\*:\s*(.+?)$"               # (local)

VALID_STATUSES = {                                                  # (local)
    "NOT STARTED", "IN PROGRESS",
    "DONE", "DONE (primary + consult)",
    "COMPLETE",
    "COMPLETE (elevated [VERIFY] per W1-3 convergent-FAIL redirection)",
    "PASS", "FAIL", "INFO", "PRE-REG-INCOMPLETE",
}


# ---------------------------------------------------------------------------
# Section 4 — Dual-SHA helpers (S84+ schema)
# ---------------------------------------------------------------------------
def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(pin_map: dict) -> str:
    """Canonical SHA-256 over ordered input-pin map (audit_sha256)."""
    canonical = json.dumps(pin_map, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def content_hash(*pins: str) -> str:
    """Content-only SHA: data inputs + script bytes (excludes constants)."""
    h = hashlib.sha256()
    for pin in pins:
        h.update(pin.encode("utf-8"))
        h.update(b"\n")
    return h.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — Extraction logic
# ---------------------------------------------------------------------------
def extract_w1_blocks(text: str) -> list[dict]:
    """Locate every actual W1-N block; return the header line, its index,
    the Status field (if present), and the body-verdict token within the
    first 50 lines after the header."""
    lines = text.splitlines()
    blocks = []                                                     # (local)
    actual_re = re.compile(ACTUAL_HEADER_PATTERN)
    status_re = re.compile(ACTUAL_STATUS_PATTERN)

    for i, line in enumerate(lines):
        m = actual_re.match(line)
        if not m:
            continue
        n_id = int(m.group(1))                                      # (local)
        slug = m.group(2).strip()                                   # (local)

        # Look at next 1-3 lines for **Status**:
        status_str = None                                           # (local)
        status_line_idx = None                                      # (local)
        for j in range(i + 1, min(i + 4, len(lines))):
            sm = status_re.match(lines[j])
            if sm:
                status_str = sm.group(1).strip()
                status_line_idx = j
                break

        # Body verdict — scan first 50 lines after the header for the
        # first verdict-context line, then extract the canonical token.
        # Priority rules:
        #   (a) line must contain "verdict" / "VERDICT" / "Gate verdict"
        #   (b) prefer explicit constructions: "verdict: X", "Gate verdict: X",
        #       "VERDICT**: **X**", "= X (", "S80-...: X" — these pin the
        #       actual verdict
        #   (c) plain occurrences of FAIL/INFO/PASS in prose ("FAIL threshold",
        #       "INFO band") DO NOT count
        body_verdict = None                                         # (local)
        body_verdict_evidence = None                                # (local)
        # Patterns in priority order (most specific first)
        verdict_patterns = [                                        # (local)
            # "Gate verdict: INFO" / "verdict: PASS" / "Verdict: FAIL"
            (r"(?i)\b(?:Gate\s+)?verdict\s*[:=]?\s*\*{0,2}\s*"
             r"(PASS-F2|PASS|FAIL-GT15|FAIL|INFO|PRE-REG-INCOMPLETE)\b",
             "verdict_colon"),
            # "VERDICT**: **PASS**" - bolded verdict
            (r"(?i)\*\*VERDICT\*\*\s*[:=]?\s*\*{0,2}\s*"
             r"(PASS-F2|PASS|FAIL-GT15|FAIL|INFO|PRE-REG-INCOMPLETE)\b",
             "verdict_bold"),
            # "S80-XXX = PASS" or "S80-XXX: PASS" or
            # "S80-XXX [VERIFY] PASS-F2:" — allow optional bracketed
            # trigger token between gate ID and verdict
            (r"\bS80-[A-Z0-9_-]+(?:\s*\[[A-Z-]+\])?\s*[=:]?\s*\*{0,2}"
             r"(PASS-F2|PASS|FAIL-GT15|FAIL|INFO|PRE-REG-INCOMPLETE)\b",
             "s80_colon"),
            # Dual-branch: "BRANCH-XX=PASS-F2" or "BRANCH-XX=FAIL-GT15"
            # If both PASS and FAIL appear in a dual-branch line, prefer PASS
            # (any successful branch satisfies the gate).
            (r"\bBRANCH-[A-Z]+\s*=\s*"
             r"(PASS-F2|PASS)\b",
             "dual_branch_pass"),
            (r"\bBRANCH-[A-Z]+\s*=\s*"
             r"(FAIL-GT15|FAIL)\b",
             "dual_branch_fail"),
        ]
        for j in range(i + 1, min(i + 50, len(lines))):
            bl = lines[j]
            for pat, label in verdict_patterns:
                m2 = re.search(pat, bl)
                if m2:
                    tok = m2.group(1)
                    canon = "PASS" if tok.startswith("PASS") else (
                        "FAIL" if tok.startswith("FAIL") else (
                            "PRE-REG-INCOMPLETE"
                            if tok == "PRE-REG-INCOMPLETE" else "INFO"))
                    body_verdict = canon
                    body_verdict_evidence = (
                        j + 1, label, bl.strip()[:120])
                    break
            if body_verdict:
                break

        blocks.append({
            "id": n_id,
            "slug": slug,
            "header_line_idx_0based": i,
            "header_line": line,
            "status_str": status_str,
            "status_line_idx_0based": status_line_idx,
            "body_verdict": body_verdict,
            "body_verdict_evidence": body_verdict_evidence,
        })
    return blocks


def reconcile(block: dict) -> dict:
    """Decide what (if anything) to repair. Returns a record indicating
    the action — STATUS_ALIGN, STATUS_MISALIGN_FIX, STUB_INCOMPLETE,
    or HEADER_PATTERN_MISMATCH (always logged)."""
    rec = dict(block)                                               # (local)
    rec["pattern_mismatch"] = True  # always — actual != plan-pattern
    if block["body_verdict"] is None:
        rec["action"] = "STUB_INCOMPLETE"
        rec["new_status"] = None
        rec["repair_applied"] = False
        return rec

    bv = block["body_verdict"]                                      # (local)
    sstr = (block["status_str"] or "").upper()                      # (local)

    # An aligned status is one that ALREADY indicates the verdict OR
    # one of the "complete" sentinel strings (DONE / COMPLETE) — those
    # we treat as ambiguous and elevate to the body verdict.
    completion_sentinels = {"DONE", "COMPLETE",
                            "DONE (PRIMARY + CONSULT)"}             # (local)

    if sstr.startswith(bv):
        rec["action"] = "STATUS_ALIGN"
        rec["new_status"] = block["status_str"]
        rec["repair_applied"] = False
        return rec

    if (sstr in completion_sentinels
            or sstr.startswith("COMPLETE")
            or sstr.startswith("DONE")):
        # Reconcile: lift to body verdict
        rec["action"] = "STATUS_LIFT_FROM_DONE"
        rec["new_status"] = bv
        rec["repair_applied"] = True
        return rec

    if sstr == "NOT STARTED":
        rec["action"] = "STATUS_REPAIR_FROM_NOT_STARTED"
        rec["new_status"] = bv
        rec["repair_applied"] = True
        return rec

    # Catch-all: status string disagrees in some other way
    rec["action"] = "STATUS_MISALIGN_OTHER"
    rec["new_status"] = bv
    rec["repair_applied"] = True
    return rec


# ---------------------------------------------------------------------------
# Section 6 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    print(f"=== {GATE_ID} ===")

    # ------------------------------------------------------------------
    # Input SHA-256 pinning (first 20 lines of stdout per template §4)
    # ------------------------------------------------------------------
    s80_sha = sha256_file(S80_FILE)                                 # (local)
    s80v_sha = sha256_file(S80_VERDICTS)                            # (local)
    cc_sha = sha256_file(CANONICAL_CONSTANTS)                       # (local)
    script_sha = sha256_file(Path(__file__))                        # (local)

    print(f"INPUT SHA-256 PINS:")
    print(f"  s80_workingpaper       = {s80_sha}")
    print(f"  s80_gate_verdicts      = {s80v_sha}")
    print(f"  canonical_constants.py = {cc_sha}")
    print(f"  script_bytes           = {script_sha}")

    # ------------------------------------------------------------------
    # Pre-registered pattern probe (PRDR check — explicit)
    # ------------------------------------------------------------------
    text = S80_FILE.read_text(encoding="utf-8")
    plan_re = re.compile(PLAN_HEADER_PATTERN, re.MULTILINE)
    plan_matches = plan_re.findall(text)                            # (local)
    print(f"\nPLAN-PATTERN PROBE  (## W1-N <slug> — <status>):")
    print(f"  matches found = {len(plan_matches)}  "
          f"(EXPECTED 6; actual count establishes pre-reg validity)")

    # ------------------------------------------------------------------
    # Actual extraction
    # ------------------------------------------------------------------
    blocks = extract_w1_blocks(text)
    print(f"\nACTUAL HEADER PROBE (### W1-N: <SLUG> — ...):")
    print(f"  blocks found = {len(blocks)}")
    for b in blocks:
        ev = (f" body@L{b['body_verdict_evidence'][0]}"
              f"[{b['body_verdict_evidence'][1]}]: "
              f"{b['body_verdict_evidence'][2]!r}"
              if b["body_verdict_evidence"] else "")
        print(f"  W1-{b['id']:1d}  hdr@L{b['header_line_idx_0based']+1}  "
              f"status={b['status_str']!r}  body_verdict={b['body_verdict']}"
              f"{ev}")

    records = [reconcile(b) for b in blocks]                        # (local)

    # ------------------------------------------------------------------
    # Build reconciled file content + diff
    # ------------------------------------------------------------------
    lines = text.splitlines(keepends=True)
    repaired_lines = list(lines)                                    # (local)
    repaired_count = 0                                              # (local)
    incomplete_count = 0                                            # (local)
    repair_log = []                                                 # (local)

    for r in records:
        if r["action"] == "STUB_INCOMPLETE":
            incomplete_count += 1
            repair_log.append({
                "id": r["id"],
                "action": "STUB_INCOMPLETE",
                "old_status": r["status_str"],
                "new_status": None,
            })
            continue
        if not r["repair_applied"]:
            repair_log.append({
                "id": r["id"],
                "action": r["action"],
                "old_status": r["status_str"],
                "new_status": r["new_status"],
            })
            continue
        # Apply Status line repair
        idx = r["status_line_idx_0based"]
        if idx is None:
            # No Status line to repair; would require inserting one
            repair_log.append({
                "id": r["id"],
                "action": "STATUS_LINE_MISSING",
                "old_status": None,
                "new_status": r["new_status"],
            })
            incomplete_count += 1
            continue
        old_line = lines[idx]                                       # (local)
        new_line = f"**Status**: {r['new_status']}\n"               # (local)
        if not old_line.endswith("\n"):
            new_line = new_line.rstrip("\n")
        repaired_lines[idx] = new_line
        repaired_count += 1
        repair_log.append({
            "id": r["id"],
            "action": r["action"],
            "old_status": r["status_str"],
            "new_status": r["new_status"],
            "line_idx_1based": idx + 1,
        })

    # Compose unified diff
    repaired_text = "".join(repaired_lines)                         # (local)
    diff = difflib.unified_diff(
        text.splitlines(keepends=True),
        repaired_lines,
        fromfile="a/sessions/archive/session-80/session-80-results-workingpaper.md",
        tofile="b/sessions/archive/session-80/session-80-results-workingpaper.md",
        n=3,
    )
    diff_str = "".join(diff)                                        # (local)

    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)
    DIFF_OUT.write_text(diff_str, encoding="utf-8")
    print(f"\nDIFF written: {DIFF_OUT}  ({len(diff_str)} bytes)")

    # NOTE: Per PRE-REG-INCOMPLETE classification we DO NOT mutate the
    # source file. The diff is the reconstruction protocol; next session
    # picks it up via plan carry-forward.

    # ------------------------------------------------------------------
    # Verdict logic
    # ------------------------------------------------------------------
    # Plan pattern matched 0 of 6 expected → PRE-REG-INCOMPLETE on the
    # PATTERN itself. Per gate-verdicts.md this maps to INFO.
    pattern_pre_reg_incomplete = (len(plan_matches) == 0)           # (local)

    if pattern_pre_reg_incomplete:
        verdict = "INFO"
        verdict_value = repaired_count
        verdict_reason = (
            f"PRE-REG-INCOMPLETE-PATTERN: plan pattern "
            f"`## W1-N <slug> — <status>` matched {len(plan_matches)} of 6 "
            f"expected; actual S80 file uses `### W1-N: <SLUG> — EVOI ...` "
            f"with status carried on the line below. Derivative "
            f"reconciliation diff produced: {repaired_count} status-line "
            f"repairs queued, {incomplete_count} headers PRE-REG-INCOMPLETE "
            f"(no extractable body verdict)."
        )
    elif incomplete_count > 0 and repaired_count > 0:
        verdict = "INFO"
        verdict_value = repaired_count
        verdict_reason = (
            f"Mixed: {repaired_count} headers reconciled, {incomplete_count} "
            f"PRE-REG-INCOMPLETE per plan §INFO clause."
        )
    elif repaired_count == N_EVAL:
        verdict = "PASS"
        verdict_value = repaired_count
        verdict_reason = "All 6 W1 status fields reconciled with body verdicts."
    elif repaired_count == 0 and incomplete_count == 0:
        verdict = "PASS"
        verdict_value = 0                                           # (local)
        verdict_reason = "All 6 W1 status fields already aligned (no repair needed)."
    else:
        verdict = "INFO"
        verdict_value = repaired_count
        verdict_reason = (
            f"Partial: {repaired_count} repaired, {incomplete_count} stubs."
        )

    # ------------------------------------------------------------------
    # SHA closure (S84+ dual-SHA)
    # ------------------------------------------------------------------
    pin_map = {                                                     # (local)
        "s80_workingpaper_sha256": s80_sha,
        "s80_gate_verdicts_sha256": s80v_sha,
        "canonical_constants_sha256": cc_sha,
        "script_sha256": script_sha,
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "verdict_value": verdict_value,
        "verdict": verdict,
    }
    audit_sha = closure_hash(pin_map)                               # (local)
    content_sha = content_hash(s80_sha, s80v_sha, script_sha)       # (local)

    # ------------------------------------------------------------------
    # Print 4-tuple + reconciliation log
    # ------------------------------------------------------------------
    print(f"\nRECONCILIATION LOG ({len(repair_log)} entries):")
    for e in repair_log:
        print(f"  {e}")

    print(f"\nVERDICT REASON: {verdict_reason}")
    print(f"\n4-tuple: (value={verdict_value}, scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX})")
    print(f"audit_sha256 = {audit_sha}")
    print(f"content_sha256 = {content_sha}")

    # ------------------------------------------------------------------
    # Append verdict line
    # ------------------------------------------------------------------
    verdict_line = (
        f"{GATE_ID}: {verdict} -- value={verdict_value} "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha}\n"
    )
    with open(VERDICT_FILE, "a", encoding="utf-8") as f:
        f.write(verdict_line)
    print(f"\nVERDICT appended to {VERDICT_FILE}:")
    print(f"  {verdict_line.strip()}")

    # JSON sidecar
    json_out = ARTIFACTS_DIR / "s84_w10a_112_s80_header_repair.json"
    json_out.write_text(json.dumps({
        "gate_id": GATE_ID,
        "verdict": verdict,
        "verdict_value": verdict_value,
        "verdict_reason": verdict_reason,
        "plan_pattern_matches": len(plan_matches),
        "actual_blocks_found": len(blocks),
        "repaired_count": repaired_count,
        "incomplete_count": incomplete_count,
        "repair_log": repair_log,
        "input_pins": pin_map,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }, indent=2), encoding="utf-8")
    print(f"JSON sidecar: {json_out}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
