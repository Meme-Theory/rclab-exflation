"""S86-CANONICAL-PHRASING-AUDIT — W0b-1 producing script.

Audits two paths for the forbidden phrasing pattern that conflates the
substrate sound speed `c_fabric` with a momentum cutoff `Λ_eff`:

  forbidden ::= (?i)(Λ|Lambda)_eff\\s*=\\s*c_fabric

Targets:
  1. computations/_shared/ (recursive)
  2. sessions/session-plan/session-86-plan-w3.md

PASS iff: post-edit grep count == 0  AND  canonical_constants.py c_fabric
docstring contains the substrate-sound-speed qualification verbatim.

Verdict line appended to computations/session-86/s86_gate_verdicts.txt per
.claude/rules/gate-verdicts.md (S81+ canonical form + W9a-99 dual-SHA
companion row).

Per .claude/rules/math-scripts.md exit-code discipline: exit 0 on PASS or
FAIL; non-zero only on script error.
"""

from canonical_constants import c_fabric  # noqa: F401  (import enforces compliance audit)
import hashlib
import os
import pathlib
import re
import sys
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



REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
W3_PLAN = REPO_ROOT / "sessions" / "session-plan" / "session-86-plan-w3.md"
CANON = REPO_ROOT / "computations" / "_shared" / "canonical_constants.py"
VERDICT_FILE = REPO_ROOT / "computations" / "session-86" / "s86_gate_verdicts.txt"

GATE_ID = "S86-CANONICAL-PHRASING-AUDIT"

# Forbidden pattern: (Λ|Lambda)_eff = c_fabric  (any case, any spacing)
FORBIDDEN_RE = re.compile(r"(?i)(Λ|Lambda)_eff\s*=\s*c_fabric")

REQUIRED_DOCSTRING_FRAGMENT = (
    "substrate sound speed (velocity scale, NOT a momentum cutoff)"
)


def sha256_path(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def grep_forbidden(roots: list[pathlib.Path]) -> list[tuple[str, int, str]]:
    hits: list[tuple[str, int, str]] = []  # (local)
    for root in roots:
        if root.is_file():
            files = [root]  # (local)
        else:
            files = [p for p in root.rglob("*") if p.is_file() and p.suffix in {".py", ".md", ".txt", ".sh", ".json"}]  # (local)
        for f in files:
            try:
                content = f.read_text(encoding="utf-8", errors="ignore")  # (local)
            except (OSError, UnicodeDecodeError):
                continue
            for ln, line in enumerate(content.splitlines(), 1):
                if FORBIDDEN_RE.search(line):
                    hits.append((str(f.relative_to(REPO_ROOT)), ln, line.strip()))
    return hits


def docstring_check() -> bool:
    text = CANON.read_text(encoding="utf-8")  # (local)
    # Find c_fabric assignment line
    lines = text.splitlines()  # (local)
    for i, line in enumerate(lines):
        if line.lstrip().startswith("c_fabric"):
            # Check this line + 2 surrounding lines for the required fragment
            window = "\n".join(lines[max(0, i - 1):i + 3])  # (local)
            return REQUIRED_DOCSTRING_FRAGMENT in window
    return False


def closure_sha(input_pin_map: dict[str, str]) -> str:
    payload = "|".join(f"{k}:{v}" for k, v in sorted(input_pin_map.items()))  # (local)
    return hashlib.sha256(payload.encode()).hexdigest()


def main() -> int:
    # Input-pin SHAs (computed at runtime per .claude/rules/gate-verdicts.md)
    pins: dict[str, str] = {  # (local)
        "canonical_constants.py": sha256_path(CANON),
        "session-86-plan-w3.md": sha256_path(W3_PLAN) if W3_PLAN.exists() else "MISSING",
        "script_dir_marker": "recursive",
    }
    print("=" * 76)
    print(f"{GATE_ID} — input-pin SHAs:")
    for k, v in pins.items():
        print(f"  {k}: {v}")
    print("=" * 76)

    # Audit
    hits = grep_forbidden([SCRIPT_DIR, W3_PLAN] if W3_PLAN.exists() else [SCRIPT_DIR])  # (local)
    n_forbidden = len(hits)  # (local)
    docstring_ok = docstring_check()  # (local)

    print(f"Forbidden-pattern grep hits: {n_forbidden}")
    for h in hits:
        print(f"  {h[0]}:{h[1]}  {h[2]}")
    print(f"Canonical docstring contains required fragment: {docstring_ok}")

    pass_predicate = (n_forbidden == 0) and docstring_ok  # (local)
    verdict = "PASS" if pass_predicate else "FAIL"  # (local)

    # Closure SHA over the input-pin map
    audit_sha = closure_sha(pins)  # (local)

    # Content SHA = SHA-256 of the gate-state payload
    content_payload = (  # (local)
        f"{GATE_ID}|value={n_forbidden}|scheme=canonical_constants_py"
        f"|convention=phrasing_audit|docstring_ok={docstring_ok}|hits={n_forbidden}"
    )
    content_sha = hashlib.sha256(content_payload.encode()).hexdigest()  # (local)

    canonical_line = (  # (local)
        f"{GATE_ID}: {verdict} -- value={n_forbidden} scheme=canonical_constants_py "
        f"convention=phrasing_audit L_max=N/A sha256={audit_sha}"
    )
    companion_line = (  # (local)
        f"# audit_sha256_short={audit_sha[:16]} content_sha256={content_sha} "
        f"audit_sha256={audit_sha}"
    )

    with VERDICT_FILE.open("a", encoding="utf-8") as f:
        f.write(canonical_line + "\n")
        f.write(companion_line + "\n")

    print()
    print(canonical_line)
    print(companion_line)
    print(f"\n4-tuple: (value={n_forbidden}, scheme=canonical_constants_py, "
          f"convention=phrasing_audit, L_max=N/A)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
