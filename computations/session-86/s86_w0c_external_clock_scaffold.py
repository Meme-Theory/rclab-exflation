#!/usr/bin/env python3
"""
S86 W0c-8 — S86-EXTERNAL-CLOCK-SCAFFOLD
========================================

Gate: S86-EXTERNAL-CLOCK-SCAFFOLD ([VERIFY])
Classification: META

Pre-registered threshold (plan §W0c-8.9):
  PASS iff `sessions/framework/registry/external-clock-scaffold.md` is CREATED
  with 11-session table + pre-registered ingest-gates + freeze-no-re-pin
  discipline statement.
  FAIL iff file pre-existed (CREATE gate cannot over-write) OR write failed.
  INFO is N/A for this gate (binary CREATE).

Inputs (S84+ dual-SHA):
  - sessions/framework/ directory listing (verify scaffold absent pre-write)
  - script bytes (this file)

Output 4-tuple:
  (value=11_session_scaffold_landed, scheme=external_clock_freeze,
   convention=2026_2030_horizon, L_max=N/A)
"""
from __future__ import annotations

from canonical_constants import M_KK  # noqa: F401  # framework-import discipline

import hashlib
import json
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
GATE_ID = "S86-EXTERNAL-CLOCK-SCAFFOLD"
SCHEME = "external_clock_freeze"
CONVENTION = "2026_2030_horizon"
L_MAX = "N/A"

SCAFFOLD_TARGET = PROJECT_ROOT / "sessions" / "framework" / "external-clock-scaffold.md"
VERDICT_TXT = resolve_output(86, 's86_gate_verdicts.txt')


# Scaffold content per plan §W0c-8.6 step 2 (template verbatim from plan)
SCAFFOLD_CONTENT = """# External-Clock Scaffold (S86-S96)

**Created**: S86 W0c-8 (gate ID: `S86-EXTERNAL-CLOCK-SCAFFOLD`)
**Owner**: mack-cosmic-bridge (delegated to rclab-solo for S86 W0c-8 land)
**Pattern**: freeze-no-re-pin (S86 freezes the scaffold; subsequent
sessions extend or ingest, never re-pin)
**Status**: DOCUMENTATION ONLY for S86 (no compute; ingest-gates fire
at S88 + S96 on data publication)

## §1. 11-Session Scaffold Table

| Session | Date Anchor       | Action                                    | Trigger Type   | Gate ID (pre-reg)   |
|:--------|:------------------|:------------------------------------------|:---------------|:--------------------|
| S86     | 2026-04 (frozen)  | Scaffold creation; freeze 2026-2030 plan  | METHODOLOGY    | S86-W0c-8           |
| S87     | 2026-Q3           | Scaffold extend (add S97-S100 horizon)    | METHODOLOGY    | S87-EXT-EXTERNAL    |
| S88     | 2026-Q4 (target)  | BK-Array data ingest                      | OBSERVATIONAL  | S88-BK-ARRAY-INGEST |
| S89     | 2027-Q1           | Post-BK-Array consolidation               | METHODOLOGY    | S89-CONSOL          |
| S90     | 2027-Q2           | Maintain                                  | MAINTAIN       | S90-MAINT           |
| S91     | 2027-Q3           | Maintain                                  | MAINTAIN       | S91-MAINT           |
| S92     | 2027-Q4           | Maintain                                  | MAINTAIN       | S92-MAINT           |
| S93     | 2028-Q1           | Maintain                                  | MAINTAIN       | S93-MAINT           |
| S94     | 2028-Q3           | Maintain                                  | MAINTAIN       | S94-MAINT           |
| S95     | 2029-Q4           | Pre-LiteBIRD prep                         | METHODOLOGY    | S95-PREP            |
| S96     | 2030-Q1 (target)  | LiteBIRD data ingest                      | OBSERVATIONAL  | S96-LITEBIRD-INGEST |

## §2. Pre-Registered Ingest-Gates (DOCUMENTATION ONLY in S86)

### S88-BK-ARRAY-INGEST

**Trigger**: BK-Array 2026 r-tensor-to-scalar publication (Ade+ or successor).
**Action**: Re-fire S86 W11 C5/C6 lab-falsifier suite + W14 W6 inventory edits
using BK-Array measured r-band as new SI anchor.
**Owner**: mack-cosmic-bridge.
**Branches** (4-branch decision tree per W12 C31):
  - Branch 1: r ∈ [0, 0.005)     → Path-H r=0.00745 (BK-Array null, framework-Path-H consistent)
  - Branch 2: r ∈ [0.005, 0.015) → Path-H r=0.00745 (BK-Array consistent with Path-H)
  - Branch 3: r ∈ [0.015, 0.030) → Path-C r=0.0117 (BK-Array prefers Path-C)
  - Branch 4: r ≥ 0.030          → BOTH-PATHS excluded (re-derivation required)

### S96-LITEBIRD-INGEST

**Trigger**: LiteBIRD 2030 publication (Hazumi+ or successor).
**Action**: Re-fire S86 W11 C5/C6 + W14 W6 with LiteBIRD measured r-band.
**Owner**: mack-cosmic-bridge.
**Branches**: same 4-branch decision tree as S88, applied to LiteBIRD r-band.

## §3. Freeze-No-Re-Pin Discipline

The scaffold is FROZEN at S86. Subsequent sessions MAY:
  - Extend (add S97-S100 horizon at S87)
  - Ingest (S88 / S96 fire ingest gates on data publication)
  - Maintain (S89-S95 sessions touch the scaffold only for housekeeping)

Subsequent sessions MUST NOT:
  - Re-pin S86's frozen 2026-2030 plan (would violate freeze-no-re-pin)
  - Re-define ingest-gate branches without explicit user approval
  - Add new ingest-gates between S86 and the target session (would silently
    re-pin the scaffold)

## §4. Provenance

**Source plan**: `sessions/session-plan/session-86-plan-w0c.md` §W0c-8
**Created in S86 W0c-8** by `s86_w0c_external_clock_scaffold.py`
**Verdict**: PASS → `computations/session-86/s86_gate_verdicts.txt`
"""


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def compute_dual_sha(script_path: Path, scaffold_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    sb = b""  # (local)
    try:
        sb = script_path.read_bytes()
    except OSError:
        pass
    cb = b""  # (local)
    try:
        cb = scaffold_path.read_bytes()
    except OSError:
        pass
    pj = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")  # (local)
    h_a = hashlib.sha256(); h_a.update(sb); h_a.update(cb); h_a.update(pj)
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

    print(f"=== {GATE_ID} — pre-existence check (CREATE gate) ===")
    pre_existed = SCAFFOLD_TARGET.exists()  # (local)
    pre_existed_sha = sha256_of(SCAFFOLD_TARGET) if pre_existed else ""  # (local)
    print(f"  Target: {SCAFFOLD_TARGET.relative_to(PROJECT_ROOT)}")
    print(f"  Pre-existence: {'EXISTS (CREATE FAIL)' if pre_existed else 'ABSENT (CREATE OK)'}")
    if pre_existed:
        print(f"  Pre-existing SHA: {pre_existed_sha[:16]}...")
        verdict = "FAIL"
        value = "scaffold_pre_existed"
        # Compute dual-SHA without modifying anything
        pins = {  # (local)
            "sessions/framework/registry/external-clock-scaffold.md": pre_existed_sha,
        }
        audit_sha, content_sha = compute_dual_sha(
            Path(__file__).resolve(), SCAFFOLD_TARGET, pins
        )
        append_verdict(verdict, value, audit_sha, content_sha)
        print(f"\n=== {GATE_ID}: {verdict} ===")
        return 0

    # Ensure parent directory exists
    SCAFFOLD_TARGET.parent.mkdir(parents=True, exist_ok=True)

    # Write the scaffold
    print(f"\n=== {GATE_ID} — writing scaffold ===")
    SCAFFOLD_TARGET.write_text(SCAFFOLD_CONTENT, encoding="utf-8")
    post_write_sha = sha256_of(SCAFFOLD_TARGET)  # (local)
    print(f"  Scaffold written: {len(SCAFFOLD_CONTENT)} bytes")
    print(f"  Post-write SHA-256: {post_write_sha[:16]}...")

    # Verify content properties (11-session table + 2 ingest-gates + freeze discipline)
    text = SCAFFOLD_TARGET.read_text(encoding="utf-8")  # (local)
    has_11_sessions = all(f"| S{n}" in text for n in (86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96))  # (local)
    has_bk_array = "S88-BK-ARRAY-INGEST" in text  # (local)
    has_litebird = "S96-LITEBIRD-INGEST" in text  # (local)
    has_freeze = "Freeze-No-Re-Pin" in text  # (local)
    has_4_branches = "Branch 4" in text  # (local)
    print(f"\n=== Scaffold content verification ===")
    print(f"  11-session table:        {'OK' if has_11_sessions else 'MISSING'}")
    print(f"  BK-Array ingest:         {'OK' if has_bk_array else 'MISSING'}")
    print(f"  LiteBIRD ingest:         {'OK' if has_litebird else 'MISSING'}")
    print(f"  Freeze-No-Re-Pin:        {'OK' if has_freeze else 'MISSING'}")
    print(f"  4-branch decision tree:  {'OK' if has_4_branches else 'MISSING'}")

    pass_cond = has_11_sessions and has_bk_array and has_litebird and has_freeze and has_4_branches  # (local)

    pins = {  # (local)
        "sessions/framework/registry/external-clock-scaffold.md": post_write_sha,
    }
    audit_sha, content_sha = compute_dual_sha(
        Path(__file__).resolve(), SCAFFOLD_TARGET, pins
    )
    print(f"\n  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")

    verdict = "PASS" if pass_cond else "FAIL"  # (local)
    value = "11_session_scaffold_landed" if pass_cond else "scaffold_content_incomplete"  # (local)

    print(f"\n(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    append_verdict(verdict, value, audit_sha, content_sha)

    # Diagnostic JSON
    diag = {
        "gate_id": GATE_ID,
        "verdict": verdict,
        "session": SESSION,
        "wave": "W0c",
        "pre_existed": pre_existed,
        "scaffold_path": str(SCAFFOLD_TARGET.relative_to(PROJECT_ROOT)).replace("\\", "/"),
        "scaffold_size_bytes": len(SCAFFOLD_CONTENT),
        "post_write_sha256": post_write_sha,
        "content_checks": {
            "has_11_sessions": has_11_sessions,
            "has_bk_array_ingest": has_bk_array,
            "has_litebird_ingest": has_litebird,
            "has_freeze_no_repin": has_freeze,
            "has_4_branch_tree": has_4_branches,
        },
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
    }  # (local)
    diag_path = resolve_output(86, 's86_w0c_8_external_clock_scaffold.json')  # (local)
    diag_path.write_text(json.dumps(diag, indent=2), encoding="utf-8")
    print(f"\nDiagnostic JSON: {diag_path.name}")

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
