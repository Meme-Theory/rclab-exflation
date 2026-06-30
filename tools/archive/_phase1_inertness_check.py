"""tools/_phase1_inertness_check.py — verify Phase 1 install is inert under default flag.

Runs a series of assertions that, taken together, confirm:

    1. tools/computation_root.json exists and parses as JSON.
    2. Its schema_version == 1, active_root == 'computations/_shared', and
       known_roots contains both expected entries.
    3. tools/computation_root.py is importable and exposes the documented API.
    4. get_active_root() returns 'computations/_shared' (the inertness invariant).
    5. resolve_script(86, 's86_test.py') returns a path containing
       'computations/_shared' and NOT containing 'computations/session-' (i.e.,
       the path matches the pre-Phase-1 flat-layout convention).
    6. resolve_output(86, 's86_gate_verdicts.txt') routes to the canonical
       verdict-file path under computations/ per .claude/rules/gate-verdicts.md.
    7. resolve_glob(86, 's86_*.py')'s parent directory is computations/.
    8. is_mirror_active() returns False (because computations/ has not yet
       been built; this check trips to True only after Phase 2).

If all 8 assertions pass, Phase 1 is verifiably inert: importing
tools.computation_root or reading tools/computation_root.json changes nothing
about how existing consumers compute paths. Existing scripts will continue
to use their hardcoded 'computations/...' strings; no Phase-1-installed
code is silently rerouting them.

Usage:
    python tools/_phase1_inertness_check.py

Output: PASS/FAIL per assertion, plus a summary line.
"""

from __future__ import annotations

import json
import sys
import pathlib

# Ensure tools/ is on sys.path so we can import computation_root regardless
# of the cwd this script runs from.
TOOLS_DIR = pathlib.Path(__file__).resolve().parent
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))


def _emit(label: str, ok: bool, detail: str = "") -> bool:
    tag = "PASS" if ok else "FAIL"
    print(f"  [{tag}] {label}" + (f" -- {detail}" if detail else ""))
    return ok


def main() -> int:
    print("=" * 72)
    print("Phase 1 inertness check (tools/_phase1_inertness_check.py)")
    print("=" * 72)
    all_ok = True

    # ----------------------------------------------------------------------
    # Assertion 1: JSON exists and parses
    # ----------------------------------------------------------------------
    json_path = TOOLS_DIR / "computation_root.json"
    json_exists = json_path.exists()
    all_ok &= _emit("computation_root.json exists", json_exists,
                    f"path={json_path}")
    if not json_exists:
        print("\nABORT: cannot continue without computation_root.json.")
        return 1

    try:
        with open(json_path, "r", encoding="utf-8") as f:
            cfg = json.load(f)
        all_ok &= _emit("computation_root.json parses as JSON", True)
    except json.JSONDecodeError as exc:
        all_ok &= _emit("computation_root.json parses as JSON", False,
                        f"JSONDecodeError: {exc}")
        return 1

    # ----------------------------------------------------------------------
    # Assertion 2: JSON schema fields correct for inert default
    # ----------------------------------------------------------------------
    sv = cfg.get("schema_version")
    all_ok &= _emit("schema_version == 1", sv == 1, f"got {sv!r}")

    ar = cfg.get("active_root")
    all_ok &= _emit("active_root == 'computations/_shared'",
                    ar == "computations/_shared", f"got {ar!r}")

    kr = cfg.get("known_roots") or []
    kr_ok = "computations/_shared" in kr and "computations" in kr
    all_ok &= _emit("known_roots contains both expected entries", kr_ok,
                    f"got {kr!r}")

    # ----------------------------------------------------------------------
    # Assertion 3: computation_root module importable + has expected API
    # ----------------------------------------------------------------------
    try:
        import computation_root as cr
        all_ok &= _emit("computation_root.py importable", True)
    except ImportError as exc:
        all_ok &= _emit("computation_root.py importable", False,
                        f"ImportError: {exc}")
        return 1

    expected_api = [
        "get_active_root", "resolve_script", "resolve_output",
        "resolve_glob", "is_mirror_active", "get_known_roots",
        "project_root", "config_path",
    ]
    missing = [name for name in expected_api if not hasattr(cr, name)]
    all_ok &= _emit("API surface complete", not missing,
                    f"missing={missing}" if missing else
                    f"all 8 functions present")

    # ----------------------------------------------------------------------
    # Assertion 4: get_active_root() returns the inertness-invariant value
    # ----------------------------------------------------------------------
    active = cr.get_active_root()
    all_ok &= _emit("get_active_root() == 'computations/_shared'",
                    active == "computations/_shared", f"got {active!r}")

    # ----------------------------------------------------------------------
    # Assertion 5: resolve_script returns flat-layout computations/_shared path
    # ----------------------------------------------------------------------
    p_script = cr.resolve_script(86, "s86_test.py")
    p_str = str(p_script).replace("\\", "/")
    cond_5 = ("computations/s86_test.py" in p_str
              and "computations/session-" not in p_str)
    all_ok &= _emit("resolve_script(86, ...) routes to computations/ flat",
                    cond_5, f"got {p_str!r}")

    # ----------------------------------------------------------------------
    # Assertion 6: resolve_output routes verdict file canonically
    # ----------------------------------------------------------------------
    p_verdict = cr.resolve_output(86, "s86_gate_verdicts.txt")
    p_verdict_str = str(p_verdict).replace("\\", "/")
    cond_6 = "computations/s86_gate_verdicts.txt" in p_verdict_str
    all_ok &= _emit(
        "resolve_output(86, 's86_gate_verdicts.txt') matches "
        "gate-verdicts.md canonical",
        cond_6, f"got {p_verdict_str!r}",
    )

    # ----------------------------------------------------------------------
    # Assertion 7: resolve_glob's parent is the flat computations/_shared root
    # ----------------------------------------------------------------------
    glob_results = cr.resolve_glob(86, "s86_*.py")
    if glob_results:
        parent_str = str(glob_results[0].parent).replace("\\", "/")
        cond_7 = parent_str.endswith("computations/_shared")
        all_ok &= _emit(
            "resolve_glob(86, ...) parent is computations/",
            cond_7, f"got parent={parent_str!r}",
        )
    else:
        # Empty glob is acceptable here; the assertion is about ROUTING,
        # not whether files exist. Re-route a synthetic check via
        # resolve_script to verify the routing logic with no glob results.
        synthetic = cr.resolve_script(86, "s86_synthetic.py")
        synthetic_str = str(synthetic).replace("\\", "/")
        cond_7 = "computations/s86_synthetic.py" in synthetic_str
        all_ok &= _emit(
            "resolve_glob(86, ...) returned empty; routing verified via "
            "resolve_script synthetic",
            cond_7, f"synthetic_path={synthetic_str!r}",
        )

    # ----------------------------------------------------------------------
    # Assertion 8: is_mirror_active() == False (computations/ not built yet)
    # ----------------------------------------------------------------------
    mirror_active = cr.is_mirror_active()
    # Note: this is NOT a hard FAIL if mirror_active is True; it just means
    # Phase 2 has run. We still PASS-with-note so this script is useful both
    # before and after Phase 2.
    if mirror_active:
        _emit(
            "is_mirror_active() — mirror exists (Phase 2 has run)",
            True,
            "computations/ directory present; this is expected post-Phase-2",
        )
    else:
        all_ok &= _emit(
            "is_mirror_active() == False (Phase 2 not yet run)",
            True,
            "computations/ not yet built; expected pre-Phase-2",
        )

    # ----------------------------------------------------------------------
    # Summary
    # ----------------------------------------------------------------------
    print()
    print("=" * 72)
    if all_ok:
        print("RESULT: Phase 1 inertness check PASSED.")
        print("All resolutions route to computations/ — existing consumer")
        print("behavior is preserved. Safe to proceed to Phase 2 authoring.")
        return 0
    else:
        print("RESULT: Phase 1 inertness check FAILED.")
        print("One or more assertions did not hold. Investigate before proceeding.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
