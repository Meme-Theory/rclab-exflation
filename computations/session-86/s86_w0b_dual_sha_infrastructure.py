"""S86-DUAL-SHA-INFRASTRUCTURE — W0b-5 producing script.

Verifies the 4 conjuncts (a)-(d) of the plan §W0b-5 §9 PASS criterion:
  S = boolean: computations/_shared/_dual_sha_uniqueness_audit.py exists + executable
  A = boolean: computations/_shared/_dual_sha_allowlist.json exists with exactly 3 patterns
  H = boolean: .claude/hooks/post-session/v3-closure-audit.sh contains the new invocation
  N_fp = false_positive_count from the synthetic test

  PASS_predicate = S AND A AND H AND (N_fp == 0)

Per .claude/rules/math-scripts.md exit-code discipline: PASS/FAIL/INFO all exit 0.
"""

from canonical_constants import c_fabric  # noqa: F401  (compliance audit per computations/_shared/CLAUDE.md)
import hashlib
import json
import pathlib
import subprocess
import sys
import tempfile


REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
PYTHON = REPO_ROOT / "phonon-exflation-sim" / ".venv312" / "Scripts" / "python.exe"
SCRIPT_PATH = REPO_ROOT / "computations" / "_shared" / "_dual_sha_uniqueness_audit.py"
ALLOWLIST_PATH = REPO_ROOT / "computations" / "_shared" / "_dual_sha_allowlist.json"
HOOK_PATH = REPO_ROOT / ".claude" / "hooks" / "post-session" / "v3-closure-audit.sh"
TEST_PATH = REPO_ROOT / "computations" / "_shared" / "test_dual_sha_uniqueness_audit.py"
S86_VERDICT = REPO_ROOT / "computations" / "session-86" / "s86_gate_verdicts.txt"

GATE_ID = "S86-DUAL-SHA-INFRASTRUCTURE"
EXPECTED_ALLOWLIST_PATTERN_COUNT = 3  # (local) plan §0.10 pin
EXPECTED_PATTERNS = {"REFRAME", "logspace_fix", "regex_fix"}  # (local) plan §0.10 pin
HOOK_INVOCATION_MARKER = "_dual_sha_uniqueness_audit.py"  # (local) presence-token in hook


def sha256_path(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    pins: dict[str, str] = {  # (local)
        "_dual_sha_uniqueness_audit.py": sha256_path(SCRIPT_PATH) if SCRIPT_PATH.exists() else "MISSING",
        "_dual_sha_allowlist.json": sha256_path(ALLOWLIST_PATH) if ALLOWLIST_PATH.exists() else "MISSING",
        "v3-closure-audit.sh": sha256_path(HOOK_PATH) if HOOK_PATH.exists() else "MISSING",
        "test_dual_sha_uniqueness_audit.py": sha256_path(TEST_PATH) if TEST_PATH.exists() else "MISSING",
    }
    print("=" * 76)
    print(f"{GATE_ID} — input-pin SHAs:")
    for k, v in pins.items():
        print(f"  {k}: {v}")
    print("=" * 76)

    # (a) Script exists
    S = SCRIPT_PATH.exists() and SCRIPT_PATH.is_file()  # (local)

    # (b) Allowlist exists with exactly 3 patterns matching the expected names
    A = False  # (local)
    n_patterns = 0  # (local)
    pattern_names: set[str] = set()  # (local)
    if ALLOWLIST_PATH.exists():
        try:
            allowlist = json.loads(ALLOWLIST_PATH.read_text(encoding="utf-8"))  # (local)
            n_patterns = len(allowlist)
            pattern_names = {entry.get("pattern_name") for entry in allowlist if "pattern_name" in entry}
            A = (n_patterns == EXPECTED_ALLOWLIST_PATTERN_COUNT) and (pattern_names == EXPECTED_PATTERNS)
        except (json.JSONDecodeError, OSError):
            A = False

    # (c) Hook contains the invocation
    H = False  # (local)
    if HOOK_PATH.exists():
        H = HOOK_INVOCATION_MARKER in HOOK_PATH.read_text(encoding="utf-8")

    # (d) Synthetic test false_positive_count == 0
    N_fp = -1  # (local) sentinel
    test_passed = False  # (local)
    if TEST_PATH.exists() and SCRIPT_PATH.exists() and ALLOWLIST_PATH.exists():
        # Replicate the test's harness inline so we capture false_positive_count
        # directly from the JSON output rather than via stdout parsing.
        with tempfile.TemporaryDirectory() as td_str:
            td = pathlib.Path(td_str)  # (local)
            verdict_file = td / "synthetic.txt"  # (local)
            sha_a = "a" * 64  # (local) REFRAME pair
            sha_b = "b" * 64  # (local) LOGSPACE-FIX pair
            sha_c = "c" * 64  # (local) FORBIDDEN pair
            verdict_file.write_text(
                "\n".join([
                    f"S99-W1-REFRAME-A: PASS -- value=1 scheme=test convention=test L_max=N/A audit_sha256={sha_a} content_sha256={'1' * 64} schema_version=S84+",
                    f"S99-W1-REFRAME-B: PASS -- value=2 scheme=test convention=test L_max=N/A audit_sha256={sha_a} content_sha256={'2' * 64} schema_version=S84+",
                    f"S99-W2-LOGSPACE-FIX-A: PASS -- value=3 scheme=test convention=test L_max=N/A audit_sha256={sha_b} content_sha256={'3' * 64} schema_version=S84+",
                    f"S99-W2-LOGSPACE-FIX-B: PASS -- value=4 scheme=test convention=test L_max=N/A audit_sha256={sha_b} content_sha256={'4' * 64} schema_version=S84+",
                    f"S99-W3-PHYSICS-A: PASS -- value=5 scheme=test convention=test L_max=N/A audit_sha256={sha_c} content_sha256={'5' * 64} schema_version=S84+",
                    f"S99-W3-PHYSICS-B: PASS -- value=6 scheme=test convention=test L_max=N/A audit_sha256={sha_c} content_sha256={'6' * 64} schema_version=S84+",
                ]) + "\n",
                encoding="utf-8",
            )
            out_json = td / "out.json"  # (local)
            cmd = [  # (local)
                str(PYTHON), str(SCRIPT_PATH),
                "--session", "S99",
                "--verdict-file", str(verdict_file),
                "--allowlist-file", str(ALLOWLIST_PATH),
                "--output", str(out_json),
            ]
            r = subprocess.run(cmd, capture_output=True, text=True, check=False)  # (local)
            if r.returncode == 0 and out_json.exists():
                report = json.loads(out_json.read_text(encoding="utf-8"))  # (local)
                N_fp = report.get("false_positive_count", -1)
                # Confirm the 3 cases land in the right buckets
                sets_by_sha = {d["audit_sha256"]: d for d in report.get("duplicate_audit_sha_sets", [])}  # (local)
                ok_reframe = sets_by_sha.get(sha_a, {}).get("status") == "ALLOWED"  # (local)
                ok_logspace = sets_by_sha.get(sha_b, {}).get("status") == "ALLOWED"  # (local)
                ok_forbidden = sets_by_sha.get(sha_c, {}).get("status") == "FORBIDDEN"  # (local)
                test_passed = ok_reframe and ok_logspace and ok_forbidden and (N_fp == 0)

    print(f"S (script exists)              = {S}")
    print(f"A (allowlist with 3 patterns)  = {A}  (n_patterns={n_patterns}; names={sorted(pattern_names)})")
    print(f"H (hook invocation present)    = {H}")
    print(f"N_fp (synthetic false-pos)     = {N_fp}  (test_passed={test_passed})")

    pass_predicate = S and A and H and (N_fp == 0) and test_passed  # (local)
    verdict = "PASS" if pass_predicate else "FAIL"  # (local)

    audit_payload = "|".join(f"{k}:{v}" for k, v in sorted(pins.items()))  # (local)
    audit_sha = hashlib.sha256(
        (audit_payload + f"|S={S}|A={A}|H={H}|N_fp={N_fp}").encode()
    ).hexdigest()  # (local)
    content_payload = (  # (local)
        f"{GATE_ID}|S={S}|A={A}|n_patterns={n_patterns}|H={H}"
        f"|N_fp={N_fp}|test_passed={test_passed}|verdict={verdict}"
    )
    content_sha = hashlib.sha256(content_payload.encode()).hexdigest()  # (local)

    canonical_line = (  # (local)
        f"{GATE_ID}: {verdict} -- value={N_fp} "
        f"scheme=dual_sha_uniqueness_audit convention=sig_5_allowlist_v1 "
        f"L_max=N/A sha256={audit_sha}"
    )
    companion_line = (  # (local)
        f"# audit_sha256_short={audit_sha[:16]} content_sha256={content_sha} "
        f"audit_sha256={audit_sha}"
    )

    with S86_VERDICT.open("a", encoding="utf-8") as f:
        f.write(canonical_line + "\n")
        f.write(companion_line + "\n")

    print()
    print(canonical_line)
    print(companion_line)
    print(f"\n4-tuple: (value={N_fp}, scheme=dual_sha_uniqueness_audit, "
          f"convention=sig_5_allowlist_v1, L_max=N/A)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
