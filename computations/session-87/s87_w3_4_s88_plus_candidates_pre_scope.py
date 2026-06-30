#!/usr/bin/env python3
"""
S87 W3-4 — S87-S88-PLUS-CANDIDATES (CF-24, stub-only pre-scoping gate)
======================================================================

Gate: S87-S88-PLUS-CANDIDATES ([AUDIT])

Pre-registered threshold (per plan session-87-plan-w3.md §W3-4):
  PASS-precondition iff all 3 sub-stub W3-4{a,b,c} working-paper sections
  contain all 4 fields (What/Inputs/Gate/Effort).
  Composite verdict = INFO (per feedback_fix-in-session-never-defer.md:
  pre-scope for next-session is INFO, not PASS — there is no compute to PASS).
  FAIL iff any sub-stub missing a field.

Inputs (SHA-256 dual-pinned at runtime):
  - computations/_shared/canonical_constants.py     (audit_sha256 only)
  - sessions/session-plan/session-87-plan-w3.md  (plan source-of-truth)
  - sessions/archive/session-87/session-87-results-workingpaper.md
                                                 (W3-4 sections under audit)
  - script bytes                                 (BOTH audit + content)

Output 4-tuple:
  (value='3_substubs_pre_scoped', scheme=stub-only-pre-scope,
   convention=4-field-spec-per-feedback_fix-in-session-never-defer, L_max=N/A)

Classification: NON-PHONONIC (META — documentation-only sub-stub registry)

METHODOLOGY
-----------
Stub-only pre-scoping gate. NO compute, NO data, NO plot. The script:
  1. Reads §W3-4a / §W3-4b / §W3-4c sections of the working paper.
  2. Verifies each sub-stub contains the 4 required field markers in its
     4-field-spec table: 'What', 'Inputs', 'Gate', 'Effort'.
  3. Emits JSON diagnostic (per-substub completeness + composite outcome).
  4. Computes audit_sha256 (script + canonical + pinmap) and content_sha256
     (script bytes only) per S84+ dual-SHA schema.
  5. Appends canonical verdict line + dual-SHA companion row to
     computations/session-87/s87_gate_verdicts.txt.

DISCIPLINE
----------
- `from canonical_constants import *` for audit-trail completeness (no compute).
- Every local intermediate tagged `# (local)`.
- GPU NOT NEEDED (boolean grep + SHA-256 on small files).
- SHA-256 of all input files logged in first 20 lines of stdout.
- audit_sha256 + content_sha256 both 64-char hex, never truncated.
- 4-tuple printed as final non-verdict line.
- Atomic single-write append to verdict file (POSIX O_APPEND-safe).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import; audit-trail only)
# ---------------------------------------------------------------------------
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


PROJECT_ROOT = Path(__file__).resolve().parent.parent  # (local)
sys.path.insert(0, str(PROJECT_ROOT / "computations"))

from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import re
import time

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S87"                                                         # (local)
GATE_ID = "S87-S88-PLUS-CANDIDATES"                                     # (local)
SCHEME = "stub-only-pre-scope"                                          # (local)
CONVENTION = "4-field-spec-per-feedback_fix-in-session-never-defer"        # (local)
L_MAX_TAG = "N/A"                                                       # (local)

# Output destinations (NO .npz, NO .png — stub-only gate)
OUT_JSON = resolve_output(87, 's87_w3_4_s88_plus_candidates_pre_scope.json')    # (local)
VERDICT_TXT = resolve_output(87, 's87_gate_verdicts.txt')                       # (local)

# Sources
PLAN_FILE = PROJECT_ROOT / "sessions" / "session-plan" / "session-87-plan-w3.md"   # (local)
WP_FILE = PROJECT_ROOT / "sessions" / "session-87" / "session-87-results-workingpaper.md"  # (local)
CANONICAL_FILE = resolve_script(None, 'canonical_constants.py')                              # (local)

INPUT_FILES = [
    CANONICAL_FILE,
    PLAN_FILE,
    WP_FILE,
]

# 3 sub-stubs to audit
SUBSTUBS = [
    ("W3-4a", "S88-PATI-SALAM-EMBEDDING-PRESERVES-B1-B2-PARTITION"),
    ("W3-4b", "S88-EE-BB-T-CROSS-CORRELATION-DIRECT-CSUB-PROBE"),
    ("W3-4c", "S88-F-NL-EQUILATERAL-NON-GAUSSIANITY"),
]

# Required 4-field markers (must appear inside each substub's section)
REQUIRED_FIELDS = ["What", "Inputs", "Gate", "Effort"]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (dual-SHA per S84+ schema)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    """Print SHA-256 of each input; return {relpath: sha} for closure hash."""
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    """Stable hash over ordered input-pin map (used by audit_sha256)."""
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
    """Compute (audit_sha256, content_sha256) per the S84+ dual-SHA schema.

    audit_sha256 is taken as the closure_hash over the FULL pin-map
    (which already includes script SHA via the input list extension below
    AND canonical_constants SHA AND plan/wp SHAs). This matches the plan's
    §W3-4 PRDR pin-map specification:
      pin_map = {plan_block_sha256, W3-working-paper-section-shas, gate_id,
                 scheme, convention, L_max}.

    content_sha256 = sha256(bytes(script)) only.
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
# Section 5 — Sub-stub 4-field-completeness verifier
# ---------------------------------------------------------------------------

def extract_substub_section(wp_text: str, substub_id: str) -> str:
    """Extract the substub section between its `#### §{id}` heading and the
    next sibling heading (`#### §` or higher).
    Returns empty string if the heading is not found.
    """
    # Heading pattern: "#### §W3-4a." or "#### §W3-4b." etc.
    heading_pat = re.compile(rf"^####\s+§{re.escape(substub_id)}\.", re.MULTILINE)
    m = heading_pat.search(wp_text)
    if not m:
        return ""
    start = m.end()
    # Find the next sibling heading at level #### or shallower (#, ##, ###).
    next_heading = re.compile(r"^(#{1,4})\s+§", re.MULTILINE)
    after = wp_text[start:]
    n = next_heading.search(after)
    end = start + (n.start() if n else len(after))
    return wp_text[start:end]


def check_field_present(section_text: str, field_name: str) -> bool:
    """Check that a 4-field-spec table row containing the field name is present.

    Field rows are formatted as:
        | **What** | <specification text> |
        | **Inputs** | ... |
    The check requires the bolded field marker `**{field_name}**` inside a
    pipe-delimited table cell to appear at least once in the section.
    """
    pat = re.compile(rf"\|\s*\*\*{re.escape(field_name)}\*\*\s*\|", re.MULTILINE)
    return bool(pat.search(section_text))


def verify_substubs(wp_text: str) -> dict:
    """Run the 4-field-completeness verifier on each substub.
    Returns a diagnostic dict mapping each substub ID to a per-field map +
    overall completeness boolean.
    """
    out: dict = {}  # (local)
    for substub_id, gate_id in SUBSTUBS:
        section = extract_substub_section(wp_text, substub_id)
        section_present = bool(section.strip())
        per_field = {fld: check_field_present(section, fld) for fld in REQUIRED_FIELDS}
        all_present = section_present and all(per_field.values())
        out[substub_id] = {
            "gate_id": gate_id,
            "section_extracted": section_present,
            "section_length_chars": len(section),
            "fields_present": per_field,
            "all_4_fields_present": all_present,
        }
    return out


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict + 4-tuple output
# ---------------------------------------------------------------------------

def emit_4tuple(value: str, scheme: str, convention: str, L_max: str) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(
    verdict: str,
    value: str,
    audit_sha: str,
    content_sha: str,
) -> None:
    """Atomic single-write append: canonical verdict line + dual-SHA companion
    row. Per .claude/rules/gate-verdicts.md S81+ + S84+ schema.
    """
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX_TAG} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion_row = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split; S87-W3-4 stub gate)\n"
    )
    # Single atomic open("a") write of both lines.
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(companion_row)


def evaluate_gate(diag: dict) -> tuple[str, str]:
    """Per plan §W3-4 substitution chain:
        Step 1: substub_complete_i = (4 fields present) for i in {a,b,c}
        Step 2: PASS-precondition <=> all three TRUE
        Step 3: composite verdict = INFO (per feedback_fix-in-session-never-defer.md)
                or FAIL if any substub_complete_i is FALSE.
    Returns (verdict, value_string).
    """
    all_complete = all(d["all_4_fields_present"] for d in diag.values())  # (local)
    if all_complete:
        return ("INFO", "3_substubs_pre_scoped")
    # FAIL: list which substub(s) are incomplete
    incomplete = [k for k, v in diag.items() if not v["all_4_fields_present"]]  # (local)
    return ("FAIL", f"incomplete_substubs={','.join(incomplete)}")


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 1. Log input pins (first 20 lines of stdout)
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)  # (local)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # 1b. Compute S84+ dual SHAs
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_FILE, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. Read working paper, verify the 3 substubs
    if not WP_FILE.exists():
        print(f"FATAL: working paper not found at {WP_FILE}")
        return 2
    wp_text = WP_FILE.read_text(encoding="utf-8")  # (local)
    diag = verify_substubs(wp_text)

    print("=== Sub-stub 4-field-completeness diagnostic ===")
    for substub_id, info in diag.items():
        flag = "PASS" if info["all_4_fields_present"] else "FAIL"
        fields_str = ", ".join(
            f"{k}={'Y' if v else 'N'}" for k, v in info["fields_present"].items()
        )  # (local)
        print(f"  §{substub_id}  ({info['gate_id']}): {flag}  [{fields_str}]")
    print()

    # 3. Evaluate gate
    verdict, value = evaluate_gate(diag)
    print(f"Gate evaluation: verdict={verdict}, value={value!r}")

    # 4. Write JSON diagnostic
    json_payload = {
        "gate_id": GATE_ID,
        "session": SESSION,
        "wave": "W3",
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX_TAG,
        "verdict": verdict,
        "value": value,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
        "input_pins": pins,
        "substub_diagnostic": diag,
        "all_substubs_complete": all(
            d["all_4_fields_present"] for d in diag.values()
        ),
    }
    OUT_JSON.write_text(
        json.dumps(json_payload, indent=2, sort_keys=False),
        encoding="utf-8",
    )
    print(f"JSON diagnostic written: {OUT_JSON.relative_to(PROJECT_ROOT)}")

    # 5. Emit 4-tuple + append verdict (dual-SHA, S84+ schema)
    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX_TAG)  # (local)
    print(tag)
    append_verdict(verdict, value, audit_sha, content_sha)
    print(f"Verdict appended to {VERDICT_TXT.relative_to(PROJECT_ROOT)}")

    # 6. Final summary
    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
