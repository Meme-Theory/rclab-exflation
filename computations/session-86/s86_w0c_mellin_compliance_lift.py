#!/usr/bin/env python3
"""
S86 W0c-6 — S86-MELLIN-COMPLIANCE-LIFT
=======================================

Gate: S86-MELLIN-COMPLIANCE-LIFT ([AUDIT])
Classification: META

Pre-registered threshold (plan §W0c-6.9):
  PASS iff all identified non-compliant Mellin-labeled scripts post-lift
  carry the 5 W6-71 markers (n_compliant == n_total).
  FAIL iff any script post-lift missing 1+ markers.
  INFO iff glob count differs from expected 8.

The 5 W6-71 canonical markers (plan §W0c-6.6 step 1):
  1. # MELLIN-CONVERGENCE-STRIP: <s_lower>, <s_upper>
  2. # MELLIN-RESIDUE-EXTRACTION: <method>
  3. # MELLIN-COUNTERTERM-SUBTRACTION: <Seeley-DeWitt-coefficient>
  4. # MELLIN-ANALYTIC-CONTINUATION-PATH: <path-spec>
  5. # MELLIN-CLOSURE-VERIFICATION: <self-test-result>

Lift strategy: insert all 5 markers immediately after the
`from canonical_constants import *` line (or at top after shebang/docstring
if no such import). Marker values use W6-71 defaults with a
`(W6-71_default; per-script audit needed)` annotation per the plan's
"per-script values may differ" instruction (§W0c-6.6 step 3).

Excludes `_mellin_5_marker_audit.py` from the lift target set (the audit
script contains the marker regex patterns by virtue of being the audit;
its glob hit is a self-reference false positive).

Inputs:
  - computations/_shared/_mellin_5_marker_audit.py (post-lift validator)
  - computations/_shared/*[Mm]ellin*.py (lift targets, minus the audit)
  - script bytes (this file)

Output 4-tuple:
  (value=<n_compliant_post_lift>/<n_total>, scheme=W6_71_boilerplate,
   convention=5_marker, L_max=N/A)
"""
from __future__ import annotations

from canonical_constants import M_KK  # noqa: F401 — framework-import discipline

import hashlib
import json
import re
import subprocess
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
GATE_ID = "S86-MELLIN-COMPLIANCE-LIFT"
SCHEME = "W6_71_boilerplate"
CONVENTION = "5_marker"
L_MAX = "N/A"

AUDIT_SCRIPT = resolve_script(None, '_mellin_5_marker_audit.py')
VERDICT_TXT = resolve_output(86, 's86_gate_verdicts.txt')
EXCLUDE_FROM_LIFT = {"_mellin_5_marker_audit.py"}  # (local) — self-reference

# W6-71 default marker block (per plan §W0c-6.6 step 1 + step 3)
MARKER_BLOCK = """
# ─── W6-71 Mellin discipline markers (S86 W0c-6 retrofit) ───
# MELLIN-CONVERGENCE-STRIP: -1, +3   # (W6-71_default; per-script audit needed)
# MELLIN-RESIDUE-EXTRACTION: residue-at-pole_via_lhopital   # (W6-71_default; per-script audit needed)
# MELLIN-COUNTERTERM-SUBTRACTION: a_2_zeta-regulated   # (W6-71_default; per-script audit needed)
# MELLIN-ANALYTIC-CONTINUATION-PATH: vertical-line_Re(s)=1   # (W6-71_default; per-script audit needed)
# MELLIN-CLOSURE-VERIFICATION: self-consistent_at_residue   # (W6-71_default; per-script audit needed)
# ─────────────────────────────────────────────────────────────
"""


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def compute_dual_sha(script_path: Path, audit_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    sb = b""  # (local)
    try:
        sb = script_path.read_bytes()
    except OSError:
        pass
    ab = b""  # (local)
    try:
        ab = audit_path.read_bytes()
    except OSError:
        pass
    pj = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")  # (local)
    h_a = hashlib.sha256(); h_a.update(sb); h_a.update(ab); h_a.update(pj)
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


def insert_markers(text: str) -> tuple[str, bool]:
    """Insert MARKER_BLOCK after `from canonical_constants import *` (or at top).

    Idempotent: if markers already present, no-op.
    Returns (new_text, modified).
    """
    if "MELLIN-CONVERGENCE-STRIP" in text and "MELLIN-CLOSURE-VERIFICATION" in text:
        return text, False  # already has at least 2 markers; idempotent skip

    # Try to find the canonical_constants import line
    m = re.search(
        r"^(from\s+canonical_constants\s+import\s+[^\n]+)$",
        text,
        re.MULTILINE,
    )
    if m:
        insert_pos = m.end()  # (local)
        new_text = text[:insert_pos] + "\n" + MARKER_BLOCK.lstrip("\n") + text[insert_pos:]
        return new_text, True

    # Fallback: insert after the docstring (find closing triple quote)
    m_doc = re.search(r'^"""[\s\S]+?"""', text)  # (local)
    if m_doc:
        insert_pos = m_doc.end()
        new_text = text[:insert_pos] + "\n\n" + MARKER_BLOCK.strip() + "\n" + text[insert_pos:]
        return new_text, True

    # Final fallback: insert at the top
    new_text = MARKER_BLOCK.strip() + "\n\n" + text
    return new_text, True


def run_audit(targets: list[Path]) -> dict:
    """Invoke _mellin_5_marker_audit.py --json on the targets."""
    cmd = [
        sys.executable,
        str(AUDIT_SCRIPT),
        "--json",
    ] + [str(p) for p in targets]  # (local)
    proc = subprocess.run(cmd, capture_output=True, text=True, cwd=str(PROJECT_ROOT))  # (local)
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError:
        return {
            "error": "JSON decode failed",
            "stdout": proc.stdout[:500],
            "stderr": proc.stderr[:500],
            "returncode": proc.returncode,
        }


def main() -> int:
    t0 = time.time()  # (local)

    print(f"=== {GATE_ID} — pre-lift discovery ===")
    # Glob Mellin scripts; exclude the audit (self-reference)
    all_mellin = sorted(SCRIPT_DIR.glob("*[Mm]ellin*.py"))  # (local)
    targets = [p for p in all_mellin if p.name not in EXCLUDE_FROM_LIFT]  # (local)
    excluded = [p for p in all_mellin if p.name in EXCLUDE_FROM_LIFT]  # (local)

    print(f"  Total *[Mm]ellin*.py glob hits: {len(all_mellin)}")
    print(f"  Excluded (audit self-reference): {[p.name for p in excluded]}")
    print(f"  Lift targets: {len(targets)}")
    expected_count = 8  # (local) — plan §W0c-6.7 expected_target_count
    actual_count = len(targets)  # (local)
    count_variance = (actual_count != expected_count)  # (local)
    if count_variance:
        print(f"  COUNT VARIANCE: expected {expected_count}, found {actual_count}")
        print(f"  (Plan §W0c-6.9 INFO clause: 'glob count differs from expected 8'.)")
    print()

    # Pin SHAs pre-edit
    pins: dict[str, str] = {}  # (local)
    print(f"=== {GATE_ID} — input SHA-256 pins (pre-lift) ===")
    pins["computations/_shared/_mellin_5_marker_audit.py"] = sha256_of(AUDIT_SCRIPT)
    print(f"  _mellin_5_marker_audit.py: {pins['computations/_shared/_mellin_5_marker_audit.py'][:16]}...")
    for p in targets:
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        sha = sha256_of(p)  # (local)
        pins[rel] = sha
        print(f"  {rel}: {sha[:16]}...")
    print()

    # Pre-lift audit
    pre_audit = run_audit(targets)  # (local)
    if "error" in pre_audit:
        print(f"  Audit ERROR (pre-lift): {pre_audit['error']}")
        verdict = "FAIL"
        value = "audit_error_pre_lift"
        audit_sha, content_sha = compute_dual_sha(
            Path(__file__).resolve(), AUDIT_SCRIPT, pins
        )
        append_verdict(verdict, value, audit_sha, content_sha)
        return 0
    pre_compliant = pre_audit["n_compliant"]  # (local)
    pre_total = pre_audit["n_total"]  # (local)
    print(f"=== Pre-lift compliance: {pre_compliant}/{pre_total} = "
          f"{pre_compliant / pre_total:.4f} ===\n")

    # Apply lift
    print(f"=== {GATE_ID} — applying W6-71 5-marker lift ===")
    n_modified = 0  # (local)
    per_file: dict[str, str] = {}  # (local)
    for p in targets:
        text = p.read_text(encoding="utf-8")  # (local)
        new_text, modified = insert_markers(text)  # (local)
        if modified:
            p.write_text(new_text, encoding="utf-8")
            n_modified += 1
            per_file[p.name] = "modified"
            print(f"  {p.name}: markers inserted")
        else:
            per_file[p.name] = "skip (already had markers)"
            print(f"  {p.name}: skip (already had markers)")
    print(f"  Total scripts modified: {n_modified}/{len(targets)}")
    print()

    # Post-lift audit
    post_audit = run_audit(targets)  # (local)
    if "error" in post_audit:
        print(f"  Audit ERROR (post-lift): {post_audit['error']}")
        verdict = "FAIL"
        value = "audit_error_post_lift"
        audit_sha, content_sha = compute_dual_sha(
            Path(__file__).resolve(), AUDIT_SCRIPT, pins
        )
        append_verdict(verdict, value, audit_sha, content_sha)
        return 0
    post_compliant = post_audit["n_compliant"]  # (local)
    post_total = post_audit["n_total"]  # (local)
    print(f"=== Post-lift compliance: {post_compliant}/{post_total} = "
          f"{post_compliant / post_total:.4f} ===")

    # Update pins for post-edit SHAs
    for p in targets:
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        pins[rel] = sha256_of(p)

    audit_sha, content_sha = compute_dual_sha(
        Path(__file__).resolve(), AUDIT_SCRIPT, pins
    )
    print(f"\n  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")

    # Verdict
    pass_cond = (post_compliant == post_total)  # (local)
    if count_variance:
        # Plan INFO clause when expected vs actual count differs
        verdict = "INFO" if pass_cond else "FAIL"
        info_tag = "_count_variance" if count_variance else ""
    else:
        verdict = "PASS" if pass_cond else "FAIL"
        info_tag = ""

    value = f"{post_compliant}/{post_total}{info_tag}"  # (local)

    print(f"\n(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    append_verdict(verdict, value, audit_sha, content_sha)

    # Diagnostic JSON
    diag = {
        "gate_id": GATE_ID,
        "verdict": verdict,
        "session": SESSION,
        "wave": "W0c",
        "pre_lift_compliant": pre_compliant,
        "pre_lift_total": pre_total,
        "post_lift_compliant": post_compliant,
        "post_lift_total": post_total,
        "expected_target_count": expected_count,
        "actual_target_count": actual_count,
        "count_variance": count_variance,
        "lift_per_file": per_file,
        "n_modified": n_modified,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "marker_value_provenance": (
            "W6-71 default values (per plan §W0c-6.6 step 3 'Use the W6-71 "
            "reference values where applicable'); each marker carries "
            "'(W6-71_default; per-script audit needed)' annotation. "
            "Per-script value confirmation is a S87+ task — this gate "
            "lifts marker presence, not per-script value verification."
        ),
    }  # (local)
    diag_path = resolve_output(86, 's86_w0c_6_mellin_compliance_lift.json')  # (local)
    diag_path.write_text(json.dumps(diag, indent=2), encoding="utf-8")
    print(f"\nDiagnostic JSON: {diag_path.name}")

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
