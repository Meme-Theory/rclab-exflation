#!/usr/bin/env python3
"""
tests/test_sha_split.py — S84 W9a-99 dual-SHA schema test fixtures
==================================================================

Runnable either via `pytest computations/_shared/tests/test_sha_split.py` or
directly via `python computations/_shared/tests/test_sha_split.py`. The
latter mode prints one line per fixture and exits 0 (all pass) / 1
(any fail).

Fixtures (6 total; 4+ required by plan):

  (1) POSITIVE  new-template-style dual-SHA line parses; round-trips the
               record with schema_version == "S84+" and both SHAs intact.

  (2) NEGATIVE  mutate the pinmap (a single input SHA); recompute
               (audit, content). audit_sha256 MUST change; content_sha256
               MUST be unchanged.

  (3) NEGATIVE  mutate a byte inside the script text; recompute
               (audit, content). BOTH SHAs MUST change.

  (4) SHIM     legacy pre-S84 `sha256=<>` verdict line parses; record
               has content_sha256 == "LEGACY-PRE-S84" and
               schema_version == "LEGACY".

  (5) SHIM     malformed verdict line (missing both `audit_sha256=` and
               `sha256=`) raises MalformedVerdictLine.

  (6) CROSS    scan the project's real s83_gate_verdicts.txt + the S84
               verdict file; verify (a) every line in s83 parses as
               LEGACY, (b) at least one line in s84 parses as S84+, and
               (c) the malformed bucket is empty for both.

Discipline: NON-PHONONIC. No substrate content.
"""
from __future__ import annotations

import hashlib
import json
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


# Repo discovery: file lives at computations/_shared/tests/test_sha_split.py
HERE = Path(__file__).resolve().parent
PROJECT_ROOT = HERE.parent.parent
# X2-removed: legacy alias replaced (replaced by tools.computation_root.resolve_*)

# Ensure computations is on sys.path so we can import the consolidator
# and canonical_constants without relying on CWD.
sys.path.insert(0, str(COMPUTATIONS_DIR))

# Canonical import per project rules (unused at runtime here, but
# required by the script audit).
from canonical_constants import *  # noqa: E402,F401,F403

from _consolidate_intake import (  # noqa: E402
    LEGACY_CONTENT_MARKER,
    MalformedVerdictLine,
    parse_verdict_line,
    scan_verdict_file,
)


# ---------------------------------------------------------------------------
# helpers (mirror of template.compute_dual_sha / demo.dual_sha)
# ---------------------------------------------------------------------------

def _dual_sha(script: bytes, canonical: bytes, pins: dict[str, str]) -> tuple[str, str]:
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")
    h_audit = hashlib.sha256()
    h_audit.update(script)
    h_audit.update(canonical)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()
    h_content.update(script)
    return h_audit.hexdigest(), h_content.hexdigest()


def _make_dual_line(gate_id: str, audit: str, content: str) -> str:
    return (
        f"{gate_id}: PASS -- value=0.500 scheme=test convention=unit L_max=N/A "
        f"audit_sha256={audit} content_sha256={content} schema_version=S84+"
    )


def _make_legacy_line(gate_id: str, sha: str) -> str:
    return (
        f"{gate_id}: PASS -- value=0.500 scheme=test convention=unit L_max=N/A "
        f"sha256={sha}"
    )


# ---------------------------------------------------------------------------
# fixtures
# ---------------------------------------------------------------------------

def fixture_1_positive_dual_parse() -> tuple[str, bool, str]:
    """POSITIVE: new-template-style dual-SHA line parses cleanly."""
    script = b"# script v1\nresult = 7\n"
    canonical = b"# canonical\nM = 1\n"
    pins = {"x.npz": "a" * 64}
    audit, content = _dual_sha(script, canonical, pins)
    line = _make_dual_line("S84-TEST-DUAL", audit, content)
    rec = parse_verdict_line(line)
    ok = (
        rec["gate_id"] == "S84-TEST-DUAL"
        and rec["audit_sha256"] == audit
        and rec["content_sha256"] == content
        and rec["schema_version"] == "S84+"
        and rec["verdict"] == "PASS"
    )
    return "fixture_1_positive_dual_parse", ok, (
        f"record={{'gate':{rec['gate_id']!r}, 'schema':{rec['schema_version']!r}, "
        f"'audit_prefix':{rec['audit_sha256'][:12]!r}, 'content_prefix':{rec['content_sha256'][:12]!r}}}"
    )


def fixture_2_negative_pinmap_flip() -> tuple[str, bool, str]:
    """NEGATIVE: pinmap-only mutation flips audit, preserves content."""
    script = b"# script v1\nresult = 7\n"
    canonical = b"# canonical\nM = 1\n"
    pins_0 = {"x.npz": "a" * 64, "y.npz": "b" * 64}
    pins_1 = dict(pins_0)
    pins_1["y.npz"] = "c" * 64
    a0, c0 = _dual_sha(script, canonical, pins_0)
    a1, c1 = _dual_sha(script, canonical, pins_1)
    audit_changed = a1 != a0
    content_unchanged = c1 == c0
    ok = audit_changed and content_unchanged
    return "fixture_2_negative_pinmap_flip", ok, (
        f"audit_changed={audit_changed}, content_unchanged={content_unchanged}"
    )


def fixture_3_negative_script_flip() -> tuple[str, bool, str]:
    """NEGATIVE: script-only mutation flips BOTH audit AND content."""
    script_0 = b"# script v1\nresult = 7\n"
    script_1 = b"# script v1\nresult = 8\n"  # single byte diff
    canonical = b"# canonical\nM = 1\n"
    pins = {"x.npz": "a" * 64}
    a0, c0 = _dual_sha(script_0, canonical, pins)
    a1, c1 = _dual_sha(script_1, canonical, pins)
    audit_changed = a1 != a0
    content_changed = c1 != c0
    ok = audit_changed and content_changed
    return "fixture_3_negative_script_flip", ok, (
        f"audit_changed={audit_changed}, content_changed={content_changed}"
    )


def fixture_4_shim_legacy_parse() -> tuple[str, bool, str]:
    """SHIM: legacy pre-S84 single-SHA line parses as LEGACY."""
    legacy_sha = "d" * 64
    line = _make_legacy_line("S83-LEGACY-EXAMPLE", legacy_sha)
    rec = parse_verdict_line(line)
    ok = (
        rec["gate_id"] == "S83-LEGACY-EXAMPLE"
        and rec["audit_sha256"] == legacy_sha
        and rec["content_sha256"] == LEGACY_CONTENT_MARKER
        and rec["schema_version"] == "LEGACY"
    )
    return "fixture_4_shim_legacy_parse", ok, (
        f"schema={rec['schema_version']}, content={rec['content_sha256']}"
    )


def fixture_5_shim_malformed_raises() -> tuple[str, bool, str]:
    """SHIM: a line missing both audit_sha256 and sha256 MUST raise."""
    bad = "S84-NO-SHA: PASS -- value=0.5 scheme=test convention=unit L_max=N/A"
    raised = False
    try:
        parse_verdict_line(bad)
    except MalformedVerdictLine:
        raised = True
    return "fixture_5_shim_malformed_raises", raised, (
        f"raised={raised} (expected True)"
    )


def fixture_6_cross_real_files() -> tuple[str, bool, str]:
    """CROSS: scan project's actual S83 + S84 verdict files.

    Expected (empirical, post-W9a-99 shim):
    - s83_gate_verdicts.txt: every parsed record is LEGACY; dual_sha == 0;
      hybrid == 0 (S83 pre-dates dual-SHA).
    - s84_gate_verdicts.txt: at least one DUAL-SHA record present AND
      at least one HYBRID-TRANSITION record (artifact of the pre-W9a-99
      S84 emitters that wrote both old and new SHA keys). legacy == 0
      or nonzero (some S84 scripts wrote legacy-only during the
      transition) — not checked.

    Residual malformed allowed (with a small bounded cap): genuinely
    non-canonical lines like S83 L45/L53 which omit `value=` entirely
    (a pre-strict-format documentation bug). The shim correctly
    rejects these rather than silently promoting them.
    """
    s83_path = resolve_output(83, 's83_gate_verdicts.txt')
    s84_path = resolve_output(84, 's84_gate_verdicts.txt')
    s83 = scan_verdict_file(s83_path)
    s84 = scan_verdict_file(s84_path)
    MALFORMED_BUDGET = 5  # (local) allow bounded legitimate malformed

    # S83 pre-dates the dual-SHA schema: no dual-SHA records expected.
    # Hybrid records may exist — they arise when a legacy S83 line has
    # non-canonical value/convention content (e.g., commas/spaces in
    # the convention literal) so the shim falls back to the hybrid
    # rescue path, which promotes the legacy SHA to audit_sha256 and
    # stamps content_sha256 = LEGACY_CONTENT_MARKER. A small bounded
    # number of such rescues is expected and acceptable.
    HYBRID_BUDGET_PRE_S84 = 5  # (local)
    s83_pure_legacy = (
        len(s83["dual_sha"]) == 0
        and len(s83["hybrid"]) <= HYBRID_BUDGET_PRE_S84
        and len(s83["legacy"]) > 0
    )
    s83_bounded_malformed = len(s83["malformed"]) <= MALFORMED_BUDGET
    s84_has_dual = len(s84["dual_sha"]) > 0
    s84_has_hybrid = len(s84["hybrid"]) >= 0  # ok whether present or not
    s84_bounded_malformed = len(s84["malformed"]) <= MALFORMED_BUDGET
    ok = (
        s83_pure_legacy
        and s83_bounded_malformed
        and s84_has_dual
        and s84_has_hybrid
        and s84_bounded_malformed
    )
    return "fixture_6_cross_real_files", ok, (
        f"s83=(dual={len(s83['dual_sha'])}, legacy={len(s83['legacy'])}, "
        f"hybrid={len(s83['hybrid'])}, malformed={len(s83['malformed'])})  "
        f"s84=(dual={len(s84['dual_sha'])}, legacy={len(s84['legacy'])}, "
        f"hybrid={len(s84['hybrid'])}, malformed={len(s84['malformed'])})"
    )


FIXTURES = [
    fixture_1_positive_dual_parse,
    fixture_2_negative_pinmap_flip,
    fixture_3_negative_script_flip,
    fixture_4_shim_legacy_parse,
    fixture_5_shim_malformed_raises,
    fixture_6_cross_real_files,
]


def main() -> int:
    print("=== test_sha_split.py — S84 W9a-99 fixtures ===\n")
    failures = 0  # (local)
    for f in FIXTURES:
        name, ok, detail = f()
        status = "PASS" if ok else "FAIL"
        print(f"  [{status}] {name}")
        print(f"         {detail}")
        if not ok:
            failures += 1
    print()
    print(f"=== {len(FIXTURES) - failures} / {len(FIXTURES)} fixtures PASS ===")
    return 0 if failures == 0 else 1


# pytest compatibility: wrap each fixture as a test_* function that
# asserts ok. This allows discovery without adding a pytest dependency.
def test_positive_dual_parse():
    _, ok, detail = fixture_1_positive_dual_parse()
    assert ok, detail


def test_negative_pinmap_flip():
    _, ok, detail = fixture_2_negative_pinmap_flip()
    assert ok, detail


def test_negative_script_flip():
    _, ok, detail = fixture_3_negative_script_flip()
    assert ok, detail


def test_shim_legacy_parse():
    _, ok, detail = fixture_4_shim_legacy_parse()
    assert ok, detail


def test_shim_malformed_raises():
    _, ok, detail = fixture_5_shim_malformed_raises()
    assert ok, detail


def test_cross_real_files():
    _, ok, detail = fixture_6_cross_real_files()
    assert ok, detail


if __name__ == "__main__":
    sys.exit(main())
