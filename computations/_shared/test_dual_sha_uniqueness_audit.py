"""Synthetic test for _dual_sha_uniqueness_audit.py.

Three cases per plan §W0b-5 PART 4:
  1. Two `*-REFRAME-*` gates with same audit_sha256 → ALLOWED
  2. Two `*-LOGSPACE-FIX-*` gates with same audit_sha256 → ALLOWED
  3. Two non-allowlisted gates with same audit_sha256 → FORBIDDEN

PASS criterion: false_positive_count == 0 across allowlisted patterns.
"""

from canonical_constants import c_fabric  # noqa: F401  (compliance audit per computations/_shared/CLAUDE.md)
import json
import pathlib
import subprocess
import sys
import tempfile


REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
PYTHON = REPO_ROOT / "phonon-exflation-sim" / ".venv312" / "Scripts" / "python.exe"
SCRIPT = REPO_ROOT / "computations" / "_shared" / "_dual_sha_uniqueness_audit.py"
ALLOWLIST = REPO_ROOT / "computations" / "_shared" / "_dual_sha_allowlist.json"


SHARED_SHA_REFRAME = "a" * 64
SHARED_SHA_LOGSPACE = "b" * 64
SHARED_SHA_FORBIDDEN = "c" * 64


def make_synthetic_verdict_file(tmp: pathlib.Path) -> pathlib.Path:
    p = tmp / "synthetic_gate_verdicts.txt"
    lines = [
        # Case 1: two REFRAME gates with same audit_sha → ALLOWED
        f"S99-W1-REFRAME-A: PASS -- value=1 scheme=test convention=test L_max=N/A "
        f"audit_sha256={SHARED_SHA_REFRAME} content_sha256={'1' * 64} schema_version=S84+",
        f"S99-W1-REFRAME-B: PASS -- value=2 scheme=test convention=test L_max=N/A "
        f"audit_sha256={SHARED_SHA_REFRAME} content_sha256={'2' * 64} schema_version=S84+",
        # Case 2: two LOGSPACE-FIX gates with same audit_sha → ALLOWED
        f"S99-W2-LOGSPACE-FIX-A: PASS -- value=3 scheme=test convention=test L_max=N/A "
        f"audit_sha256={SHARED_SHA_LOGSPACE} content_sha256={'3' * 64} schema_version=S84+",
        f"S99-W2-LOGSPACE-FIX-B: PASS -- value=4 scheme=test convention=test L_max=N/A "
        f"audit_sha256={SHARED_SHA_LOGSPACE} content_sha256={'4' * 64} schema_version=S84+",
        # Case 3: two NON-allowlisted gates with same audit_sha → FORBIDDEN
        f"S99-W3-PHYSICS-A: PASS -- value=5 scheme=test convention=test L_max=N/A "
        f"audit_sha256={SHARED_SHA_FORBIDDEN} content_sha256={'5' * 64} schema_version=S84+",
        f"S99-W3-PHYSICS-B: PASS -- value=6 scheme=test convention=test L_max=N/A "
        f"audit_sha256={SHARED_SHA_FORBIDDEN} content_sha256={'6' * 64} schema_version=S84+",
    ]
    p.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return p


def main() -> int:
    with tempfile.TemporaryDirectory() as td_str:
        td = pathlib.Path(td_str)
        verdict_file = make_synthetic_verdict_file(td)
        out_json = td / "sig_5_audit.json"
        cmd = [
            str(PYTHON),
            str(SCRIPT),
            "--session", "S99",
            "--verdict-file", str(verdict_file),
            "--allowlist-file", str(ALLOWLIST),
            "--output", str(out_json),
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, check=False)
        print("stdout:", result.stdout.strip())
        if result.returncode != 0:
            print("stderr:", result.stderr.strip())
            return 1
        report = json.loads(out_json.read_text(encoding="utf-8"))

        # Check each duplicate set's status
        sets_by_sha = {d["audit_sha256"]: d for d in report["duplicate_audit_sha_sets"]}
        ok = True

        if SHARED_SHA_REFRAME in sets_by_sha:
            s = sets_by_sha[SHARED_SHA_REFRAME]
            assert s["status"] == "ALLOWED", f"REFRAME case: expected ALLOWED, got {s['status']}"
            assert s["allowlist_pattern"] == "REFRAME"
            print(f"  Case 1 (REFRAME pair):    {s['status']} pattern={s['allowlist_pattern']}  ✓")
        else:
            print("  Case 1 (REFRAME pair):    NOT DETECTED  ✗")
            ok = False

        if SHARED_SHA_LOGSPACE in sets_by_sha:
            s = sets_by_sha[SHARED_SHA_LOGSPACE]
            assert s["status"] == "ALLOWED", f"LOGSPACE case: expected ALLOWED, got {s['status']}"
            assert s["allowlist_pattern"] == "logspace_fix"
            print(f"  Case 2 (LOGSPACE-FIX):    {s['status']} pattern={s['allowlist_pattern']}  ✓")
        else:
            print("  Case 2 (LOGSPACE-FIX):    NOT DETECTED  ✗")
            ok = False

        if SHARED_SHA_FORBIDDEN in sets_by_sha:
            s = sets_by_sha[SHARED_SHA_FORBIDDEN]
            assert s["status"] == "FORBIDDEN", f"FORBIDDEN case: expected FORBIDDEN, got {s['status']}"
            assert s["allowlist_pattern"] is None
            print(f"  Case 3 (non-allowlisted): {s['status']} pattern={s['allowlist_pattern']}  ✓")
        else:
            print("  Case 3 (non-allowlisted): NOT DETECTED  ✗")
            ok = False

        # Overall sig_5_overall: should be FAIL because case 3 is FORBIDDEN
        assert report["sig_5_overall"] == "FAIL", \
            f"Overall: expected FAIL (case 3), got {report['sig_5_overall']}"
        print(f"  sig_5_overall: {report['sig_5_overall']} (FAIL because Case 3 is FORBIDDEN — correct)")

        # false_positive_count: should be 0 across allowlisted patterns
        assert report["false_positive_count"] == 0, \
            f"false_positive_count: expected 0, got {report['false_positive_count']}"
        print(f"  false_positive_count: {report['false_positive_count']}  ✓")

        return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
