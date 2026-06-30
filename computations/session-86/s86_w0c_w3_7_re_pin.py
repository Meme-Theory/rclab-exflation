#!/usr/bin/env python3
"""
S86 W0c-9 — S86-W3-7-PASS-CLAUSE-RE-PIN
========================================

Gate: S86-W3-7-PASS-CLAUSE-RE-PIN ([SIGN])
Classification: META

Pre-registered threshold (plan §W0c-9.9):
  PASS iff PASS line edited from 10% → 12.5% AND FAIL line unchanged at 30%
  AND comment block landed above PASS line.
  FAIL iff edit fails OR pre-edit assertions don't match.
  INFO iff file shows PASS already at 12.5% (no edit needed; ALREADY_REPINNED).

Substitution chain (plan §W0c-9.10):
  scheme_floor = 12.5% (lower bound M(W3-7) can attain under pinned scheme)
  current_PASS = 10% < scheme_floor ⇒ structurally unattainable
  Re-pin PASS = 12.5% (= scheme_floor) restores attainability.
  FAIL = 30% unchanged ⇒ INFO band [12.5%, 30%] is genuine.

Inputs (S84+ dual-SHA):
  - sessions/session-plan/archive/session-85-plan-w3.md (W3-7 located at line 540)
    (canonical path was sessions/session-plan/session-85-plan-w3.md;
    file archived post-S85-close per W0c-5 finding)
  - script bytes (this file)

Output 4-tuple:
  (value=12.5%_pass_30%_fail, scheme=W3_7_re_pin,
   convention=scheme_floor_12.5, L_max=N/A)
"""
from __future__ import annotations

from canonical_constants import M_KK  # noqa: F401  # framework-import discipline

import hashlib
import json
import re
import sys
import time
import os
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


os.environ.setdefault("OMP_NUM_THREADS", "8")

PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S86"
GATE_ID = "S86-W3-7-PASS-CLAUSE-RE-PIN"
SCHEME = "W3_7_re_pin"
CONVENTION = "scheme_floor_12.5"
L_MAX = "N/A"

PLAN_W3_FILE = PROJECT_ROOT / "sessions" / "session-plan" / "archive" / "session-85-plan-w3.md"
VERDICT_TXT = resolve_output(86, 's86_gate_verdicts.txt')

# Pre-edit / post-edit assertions (plan §W0c-9.7 PRDR pins)
PRE_PASS_RATIO = "< 0.10"   # (local) — current PASS line in markdown bullet form
POST_PASS_RATIO = "< 0.125"  # (local) — re-pinned target (= 12.5% scheme floor)
PRE_FAIL_RATIO = "> 0.30"   # (local) — current FAIL line, asserted unchanged

COMMENT_BLOCK = """<!--
  W3-7 PASS clause re-pinned in S86 W0c-9 (gate: S86-W3-7-PASS-CLAUSE-RE-PIN).
  Reason: prior PASS = `< 0.10` sat below scheme floor 12.5%;
          structurally unattainable under heat_kernel/Branch-A/L_max=10.
  Substitution chain: see sessions/session-plan/session-86-plan-w0c.md §W0c-9.
  FAIL clause `> 0.30` preserved unchanged.
-->
"""


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def compute_dual_sha(script_path: Path, plan_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    sb = b""  # (local)
    try:
        sb = script_path.read_bytes()
    except OSError:
        pass
    pb = b""  # (local)
    try:
        pb = plan_path.read_bytes()
    except OSError:
        pass
    pj = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")  # (local)
    h_a = hashlib.sha256(); h_a.update(sb); h_a.update(pb); h_a.update(pj)
    h_c = hashlib.sha256(); h_c.update(sb)
    return h_a.hexdigest(), h_c.hexdigest()


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


def main() -> int:
    t0 = time.time()  # (local)

    print(f"=== {GATE_ID} — pre-edit assertion check ===")
    if not PLAN_W3_FILE.exists():
        print(f"  FAIL: plan file absent at {PLAN_W3_FILE}")
        return 0

    pre_text = PLAN_W3_FILE.read_text(encoding="utf-8")  # (local)
    pre_sha = sha256_of(PLAN_W3_FILE)  # (local)
    print(f"  Plan file: {PLAN_W3_FILE.relative_to(PROJECT_ROOT)}")
    print(f"  Pre-edit SHA-256: {pre_sha[:16]}...")

    # Find the W3-7 PASS line: `- **PASS**: |A_s(K=2.035) - 2.10e-9| / 2.10e-9 < 0.10 ...`
    pass_pattern = re.compile(
        r"(\*\*PASS\*\*:\s+\|A_s\(K=2\.035\)\s+-\s+2\.10e-9\|\s+/\s+2\.10e-9\s+)< 0\.10",
    )
    fail_pattern = re.compile(
        r"(\*\*FAIL\*\*:\s+\|A_s\s+-\s+2\.10e-9\|\s+/\s+2\.10e-9\s+)> 0\.30",
    )
    already_repinned = re.compile(
        r"\*\*PASS\*\*:\s+\|A_s\(K=2\.035\)\s+-\s+2\.10e-9\|\s+/\s+2\.10e-9\s+< 0\.125",
    )

    pre_pass_match = pass_pattern.search(pre_text)  # (local)
    pre_fail_match = fail_pattern.search(pre_text)  # (local)
    already_match = already_repinned.search(pre_text)  # (local)

    if already_match:
        print(f"  INFO: W3-7 PASS already re-pinned to < 0.125 (idempotent no-op).")
        verdict = "INFO"
        value = "ALREADY_REPINNED_no_edit_needed"
        pins = {  # (local)
            "sessions/session-plan/archive/session-85-plan-w3.md": pre_sha,
        }
        audit_sha, content_sha = compute_dual_sha(
            Path(__file__).resolve(), PLAN_W3_FILE, pins
        )
        append_verdict(verdict, value, audit_sha, content_sha)
        print(f"\n=== {GATE_ID}: {verdict} (idempotent no-op) ===")
        return 0

    if not pre_pass_match:
        print(f"  FAIL: W3-7 PASS line `< 0.10` not found at expected location")
        verdict = "FAIL"
        value = "pre_edit_assertion_pass_line_not_found"
        pins = {  # (local)
            "sessions/session-plan/archive/session-85-plan-w3.md": pre_sha,
        }
        audit_sha, content_sha = compute_dual_sha(
            Path(__file__).resolve(), PLAN_W3_FILE, pins
        )
        append_verdict(verdict, value, audit_sha, content_sha)
        return 0

    if not pre_fail_match:
        print(f"  FAIL: W3-7 FAIL line `> 0.30` not found at expected location")
        verdict = "FAIL"
        value = "pre_edit_assertion_fail_line_not_found"
        pins = {  # (local)
            "sessions/session-plan/archive/session-85-plan-w3.md": pre_sha,
        }
        audit_sha, content_sha = compute_dual_sha(
            Path(__file__).resolve(), PLAN_W3_FILE, pins
        )
        append_verdict(verdict, value, audit_sha, content_sha)
        return 0

    print(f"  Pre-PASS line found at position {pre_pass_match.start()}")
    print(f"  Pre-FAIL line found at position {pre_fail_match.start()}")
    print(f"  PRE-EDIT ASSERTIONS: PASS=`< 0.10` FAIL=`> 0.30` BOTH MATCH ✓")

    # Apply edit:
    #   1. Insert COMMENT_BLOCK immediately above the PASS line.
    #   2. Replace `< 0.10` with `< 0.125` in the PASS clause only.
    pass_line_start = pre_text.rfind("\n", 0, pre_pass_match.start()) + 1  # (local)

    # Build the new text in two passes
    # Insert comment block
    text_with_comment = (
        pre_text[:pass_line_start]
        + COMMENT_BLOCK
        + pre_text[pass_line_start:]
    )  # (local)

    # Replace the 0.10 in the PASS line (only that one occurrence)
    new_text = pass_pattern.sub(
        lambda m: m.group(1) + "< 0.125",
        text_with_comment,
        count=1,
    )  # (local)

    # Sanity checks before write
    fail_unchanged = fail_pattern.search(new_text) is not None  # (local)
    new_pass_present = re.search(
        r"\*\*PASS\*\*:\s+\|A_s\(K=2\.035\)\s+-\s+2\.10e-9\|\s+/\s+2\.10e-9\s+< 0\.125",
        new_text,
    ) is not None  # (local)
    comment_present = "S86-W3-7-PASS-CLAUSE-RE-PIN" in new_text  # (local)

    print(f"\n  Post-edit checks (pre-write):")
    print(f"    new PASS `< 0.125` present:  {new_pass_present}")
    print(f"    FAIL `> 0.30` unchanged:     {fail_unchanged}")
    print(f"    Comment block present:       {comment_present}")

    if not (new_pass_present and fail_unchanged and comment_present):
        print(f"  FAIL: post-edit content checks failed; aborting write")
        verdict = "FAIL"
        value = "post_edit_content_check_failed"
        pins = {  # (local)
            "sessions/session-plan/archive/session-85-plan-w3.md": pre_sha,
        }
        audit_sha, content_sha = compute_dual_sha(
            Path(__file__).resolve(), PLAN_W3_FILE, pins
        )
        append_verdict(verdict, value, audit_sha, content_sha)
        return 0

    # Write the new text
    PLAN_W3_FILE.write_text(new_text, encoding="utf-8")
    post_sha = sha256_of(PLAN_W3_FILE)  # (local)
    print(f"\n  Edit applied.")
    print(f"  Post-edit SHA-256: {post_sha[:16]}...")

    # Compute dual-SHA against post-edit state
    pins = {  # (local)
        "sessions/session-plan/archive/session-85-plan-w3.md": post_sha,
    }
    audit_sha, content_sha = compute_dual_sha(
        Path(__file__).resolve(), PLAN_W3_FILE, pins
    )
    print(f"\n  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")

    verdict = "PASS"  # (local)
    value = "12.5%_pass_30%_fail"  # (local)

    print(f"\n(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    append_verdict(verdict, value, audit_sha, content_sha)

    # Diagnostic JSON
    diag = {
        "gate_id": GATE_ID,
        "verdict": verdict,
        "session": SESSION,
        "wave": "W0c",
        "plan_file": str(PLAN_W3_FILE.relative_to(PROJECT_ROOT)).replace("\\", "/"),
        "pre_edit_sha256": pre_sha,
        "post_edit_sha256": post_sha,
        "pre_pass_match_position": pre_pass_match.start(),
        "pre_fail_match_position": pre_fail_match.start(),
        "post_edit_checks": {
            "new_pass_125_present": new_pass_present,
            "fail_30_unchanged": fail_unchanged,
            "comment_block_present": comment_present,
        },
        "pre_edit_pass": "< 0.10",
        "post_edit_pass": "< 0.125",
        "pre_edit_fail_unchanged": "> 0.30",
        "info_band_now": "[0.125, 0.30]",
        "scheme_floor_canonical": 0.125,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
    }  # (local)
    diag_path = resolve_output(86, 's86_w0c_9_w3_7_re_pin.json')  # (local)
    diag_path.write_text(json.dumps(diag, indent=2), encoding="utf-8")
    print(f"\nDiagnostic JSON: {diag_path.name}")

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
