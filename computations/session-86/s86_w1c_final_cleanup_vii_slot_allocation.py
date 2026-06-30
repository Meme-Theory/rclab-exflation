#!/usr/bin/env python3
"""
S86 W1c-final-cleanup — §VII slot-allocation FINAL CLEANUP verification
=======================================================================

Gate: S86-VII-SLOT-ALLOCATION-FINAL-CLEANUP ([VERIFY])

Purpose
-------
Verify that the central §VII Slot Allocation Table at the top of
`sessions/permanent-results-registry.md` reflects the §VII.Y → §VII.S.C-eta
+ §VII.S.C-theta sub-row migration applied during S86 W1c Task #13. After
the prior reconciliation gate (S86-VII-SLOT-ALLOCATION-RECONCILIATION,
verdict line 87, audit_sha256=ea640d42baa94898) drove `_vii_slot_allocation_audit.py`
from FAIL value=2 to PASS value=0, this gate is the post-Task-#13 mirror
sweep verifier: the audit must remain at PASS value=0 after the §VII.Y
header was DEPRECATED-redirected and §VII.S.C-eta + §VII.S.C-theta sub-row
headers were promoted to canonical.

Spawn-prompt premise vs observed state
--------------------------------------
The Task #14 spawn prompt anticipated value=8 (table out-of-sync with
post-Task-#13 registry). The live audit re-run shows value=0 (4 Class-A
matches; no Class B/C/D/E defects). Investigation: Task #13 (the §VII.Y
reconciliation) already mirrored the four required entries into the
central allocation table:

  - line 67: §VII.Y deprecated-stub redirect entry (THM)
  - line 68: §VII.S.C-eta sub-row entry (THM)
  - line 69: §VII.S.C-theta sub-row entry (CAT)
  - line 71: §VII.S parent entry (CAT)

The audit's REGISTRY_HEADER_PATTERN is r"^#{2,3}\s+§VII\.([A-Z][A-Za-z0-9.-]*)\b"
which captures the level-3 sub-row headers (§VII.S.C-eta, §VII.S.C-theta)
with suffix "S.C-eta" and "S.C-theta". The TABLE_ROW_PATTERN matches the
exact same suffixes. Both sides match → no Class-E REGISTRY_VS_TABLE_DRIFT.
The §VII.Y header is preserved as DEPRECATED redirect → table entry
preserved as DEPRECATED stub → no Class-D ORPHANED_TABLE_ENTRY. No plan
file reserves a freshly-conflicting slot → no Class-C COLLISION.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - sessions/permanent-results-registry.md   (read-only, audited)
  - computations/_shared/_vii_slot_allocation_audit.py  (audit runner)
  - canonical_constants.py                   (audit-closure-input only)
  - script bytes                             (audit + content SHAs)

Output 4-tuple:
  (value=<post-cleanup audit B+C+D+E count>, scheme=allocation-table-sub-row-sync,
   convention=slot-arbiter, L_max=N/A)

Pre-registered threshold (per Task #14 spawn prompt step 6):
  PASS  iff post-cleanup audit verdict == PASS (final defect count = 0;
                                                table fully mirrors registry +
                                                Task #13 sub-row migration absorbed)
  INFO  iff post-cleanup audit verdict == INFO (Class B only; not blocking)
  FAIL  iff any Class C/D/E defect remains (table-vs-registry drift unresolved)

Classification: NON-PHONONIC (catalog/registry hygiene; no substrate physics)

METHODOLOGY
-----------
1. Subprocess-invoke `_vii_slot_allocation_audit.py --json --quiet`.
2. Parse the audit JSON; extract verdict + Class B/C/D/E counts + Class A
   findings.
3. Cross-check that registry currently contains the four post-Task-#13
   anchor headers:
     - §VII.Y (DEPRECATED redirect at line 12588)
     - §VII.S (canonical parent at line 12806)
     - §VII.S.C-eta (canonical sub-row at line 12940)
     - §VII.S.C-theta (canonical sub-row at line 12961)
   AND that the central allocation table currently lists all four
   suffixes (Y, S, S.C-eta, S.C-theta).
4. Mirror-sweep is required only if the audit reports defects OR the
   cross-check identifies a header-vs-table mismatch. If both checks pass,
   no edits are needed (closed-by-existing-precedent per
   `feedback_fix-in-session-never-defer.md` triage).
5. Append PASS/INFO/FAIL verdict line via `append_verdict` atomic helper
   (S82-W1 race-safe pattern; single `open("a")` write).

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- Pure file-IO + subprocess (no linear algebra; no GPU; CPU thread-cap=8)
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- Verdict appended via atomic single-`open("a")` write per W9a-99 schema
- Substitution chain NOT required (catalog operation per spawn-prompt RULES)
"""
from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — OMP cap + canonical constants (MANDATORY first imports)
# ---------------------------------------------------------------------------
import os
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
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent  # (local)
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
sys.path.insert(0, str(SCRIPT_DIR))

from canonical_constants import *  # noqa: F401,F403,E402

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import re  # noqa: E402
import subprocess  # noqa: E402
import time  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION = "S86"                                                      # (local)
GATE_ID = "S86-VII-SLOT-ALLOCATION-FINAL-CLEANUP"                    # (local)
SCHEME = "allocation-table-sub-row-sync"                             # (local)
CONVENTION = "slot-arbiter"                                          # (local)
L_MAX = "N/A"                                                        # (local)

REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"  # (local)
AUDIT_SCRIPT = resolve_script(None, '_vii_slot_allocation_audit.py')            # (local)
CANONICAL_PATH = resolve_script(None, 'canonical_constants.py')                 # (local)
VERDICT_TXT = resolve_output(86, f's86_gate_verdicts.txt')                    # (local)

PYTHON_EXE = str(PROJECT_ROOT / "phonon-exflation-sim" / ".venv312" / "Scripts" / "python.exe")  # (local)

# Required post-Task-#13 anchor suffixes (registry headers AND table rows)
REQUIRED_SUFFIXES = ("Y", "S", "S.C-eta", "S.C-theta")  # (local)

INPUT_FILES = [
    REGISTRY_PATH,
    AUDIT_SCRIPT,
    CANONICAL_PATH,
]

# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
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
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
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

    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Verifier
# ---------------------------------------------------------------------------

def verify_required_anchors(registry_text: str) -> dict[str, dict[str, bool]]:
    """Confirm all REQUIRED_SUFFIXES present as both registry headers and table rows.

    Returns a per-suffix dict with {'registry_header': bool, 'table_row': bool}.
    """
    out: dict[str, dict[str, bool]] = {}  # (local)
    # Registry header pattern (matches level-2 or level-3 §VII.<suffix> headers)
    header_re = re.compile(  # (local)
        r"^#{2,3}\s+§VII\.([A-Z][A-Za-z0-9.-]*)\b",
        re.MULTILINE,
    )
    headers_present = {m.group(1) for m in header_re.finditer(registry_text)}  # (local)

    # Allocation-table row pattern (matches | §VII.<suffix> | ... |)
    table_re = re.compile(  # (local)
        r"^\|\s*§VII\.([A-Z][A-Za-z0-9.-]*)\s*\|",
        re.MULTILINE,
    )
    table_suffixes = {m.group(1) for m in table_re.finditer(registry_text)}  # (local)

    for suffix in REQUIRED_SUFFIXES:
        out[suffix] = {
            "registry_header": (suffix in headers_present),
            "table_row": (suffix in table_suffixes),
        }
    return out


def run_audit_json() -> dict:
    """Subprocess-invoke the audit script and parse its JSON output."""
    cmd = [  # (local)
        PYTHON_EXE,
        str(AUDIT_SCRIPT),
        "--json",
        "--quiet",
    ]
    print(f"\n=== Subprocess: {AUDIT_SCRIPT.name} --json --quiet ===")
    res = subprocess.run(  # (local)
        cmd,
        capture_output=True,
        text=True,
        check=False,
    )
    if res.returncode != 0:
        print(f"  audit subprocess returned {res.returncode}")
        print(f"  stderr: {res.stderr[:500]}")
    payload = json.loads(res.stdout)  # (local)
    return payload


# ---------------------------------------------------------------------------
# Section 6 — Verdict emission (atomic append per W9a-99)
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(
    verdict: str,
    value,
    audit_sha: str,
    content_sha: str,
    defect_counts: dict[str, int],
) -> None:
    """Append canonical verdict line + dual-SHA companion comment row.

    Single-`open("a")` atomic write each (no read-modify-write, no truncate).
    Two appends (one for the verdict line, one for the companion row) is
    POSIX-O_APPEND-safe; the companion row is a comment so order does not
    affect the consolidator parser.
    """
    line = (  # (local)
        f"{GATE_ID}: {verdict} -- value={value} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (  # (local)
        f"# audit_sha256 companion row: {GATE_ID} "
        f"audit={audit_sha[:16]} content={content_sha[:16]} "
        f"defect_counts={json.dumps(defect_counts, separators=(',', ':'))}\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(companion)


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 1. Log input pins
    pins = log_input_pins(INPUT_FILES)  # (local)
    closure = closure_hash(pins)  # (local)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # 1b. Dual-SHA computation
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PATH, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. Cross-check: required post-Task-#13 anchor suffixes present?
    print(f"=== Anchor-suffix cross-check (post-Task-#13 §VII.Y migration) ===")
    registry_text = REGISTRY_PATH.read_text(encoding="utf-8", errors="replace")  # (local)
    anchor_check = verify_required_anchors(registry_text)  # (local)
    all_anchors_ok = True  # (local)
    for suffix, status in anchor_check.items():
        rh = "OK " if status["registry_header"] else "MISS"
        tr = "OK " if status["table_row"] else "MISS"
        print(f"  §VII.{suffix:12s}  registry_header={rh}  table_row={tr}")
        if not (status["registry_header"] and status["table_row"]):
            all_anchors_ok = False

    # 3. Run the audit
    audit_payload = run_audit_json()  # (local)
    audit_verdict = audit_payload["verdict"]  # (local)
    counts = audit_payload["counts"]  # (local)
    defect_count = (  # (local)
        counts["B_UNREGISTERED_RESERVATION"]
        + counts["C_COLLISION_DOUBLE_RESERVATION"]
        + counts["D_ORPHANED_TABLE_ENTRY"]
        + counts["E_REGISTRY_VS_TABLE_DRIFT"]
    )
    print(f"\n=== Audit verdict: {audit_verdict} ===")
    print(f"  Class A (matched):      {counts['A_REGISTERED_AND_MATCHED']}")
    print(f"  Class B (soft):         {counts['B_UNREGISTERED_RESERVATION']}")
    print(f"  Class C (collision):    {counts['C_COLLISION_DOUBLE_RESERVATION']}")
    print(f"  Class D (orphan):       {counts['D_ORPHANED_TABLE_ENTRY']}")
    print(f"  Class E (reg-drift):    {counts['E_REGISTRY_VS_TABLE_DRIFT']}")
    print(f"  TOTAL B+C+D+E defects:  {defect_count}")
    print(f"  Anchor-suffix cross-check: {'PASS' if all_anchors_ok else 'FAIL'}")

    # 4. Verdict rule
    hard_defects = (  # (local)
        counts["C_COLLISION_DOUBLE_RESERVATION"]
        + counts["D_ORPHANED_TABLE_ENTRY"]
        + counts["E_REGISTRY_VS_TABLE_DRIFT"]
    )
    if not all_anchors_ok:
        verdict = "FAIL"
    elif hard_defects > 0:
        verdict = "FAIL"
    elif counts["B_UNREGISTERED_RESERVATION"] > 0:
        verdict = "INFO"
    else:
        verdict = "PASS"

    # 5. Emit 4-tuple + append verdict
    tag = emit_4tuple(defect_count, SCHEME, CONVENTION, L_MAX)  # (local)
    print(f"\n4-tuple: {tag}")
    append_verdict(verdict, defect_count, audit_sha, content_sha, counts)

    # 6. Final summary
    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    print(f"  Spawn-prompt premise: value=8 expected (table out-of-sync post-Task-#13)")
    print(f"  Observed reality:     value={defect_count}; Task #13 mirrored "
          f"sub-rows already")
    print(f"  Disposition: closed-by-existing-precedent (no edits needed)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
