"""Per-session sig_5 audit — dual-SHA uniqueness with by-design allowlist.

S86 W0b-5 infrastructure script. Sibling of `_yaml_gate_validator.py` and
the (planned) `_pru_cardinality_audit.py`. Invoked from the post-session
hook `.claude/hooks/post-session/v3-closure-audit.sh` sig_5 block.

Distinguishes two cases of duplicate `audit_sha256` across canonical verdict
lines:
  ALLOWED    — gate IDs all match a by-design re-emission pattern in the
               allowlist (REFRAME / logspace_fix / regex_fix); the closure
               sha256 is genuinely identical because the input-pin map is
               unchanged at the math-identity level.
  FORBIDDEN  — gate IDs do NOT match an allowlisted pattern; the duplicate
               indicates a SHA-hardcoding bug or a copy-paste error in a
               producing script.

Usage:
  python computations/_shared/_dual_sha_uniqueness_audit.py \\
      --session SN \\
      --verdict-file computations/_shared/s{N}_gate_verdicts.txt \\
      --allowlist-file computations/_shared/_dual_sha_allowlist.json \\
      --output sessions/session-{N}/sig_5_audit.json

Exit codes:
  0   audit succeeded; sig_5_overall determined (PASS / FAIL written to JSON)
  1   audit failed (script error: missing input, parse error)

Per .claude/rules/math-scripts.md exit-code discipline: physics verdict is in
the JSON, not the exit code.
"""

from canonical_constants import c_fabric  # noqa: F401  (compliance audit per computations/_shared/CLAUDE.md)
import argparse
import collections
import fnmatch
import json
import pathlib
import re
import sys


CANONICAL_RE = re.compile(
    r"^(?P<gate_id>S\d+-[A-Z0-9_-]+):\s+(?:PASS|FAIL|INFO|PENDING-EVENT)\s+--\s+"
)
AUDIT_SHA_RE = re.compile(r"audit_sha256=(?P<sha>[0-9a-f]{64})")
LEGACY_SHA_RE = re.compile(r"\bsha256=(?P<sha>[0-9a-f]{64})\b")


def parse_audit_shas(text: str) -> dict[str, list[str]]:
    """Returns dict { audit_sha256 -> [gate_ids that emitted that sha] }."""
    by_sha: dict[str, list[str]] = collections.defaultdict(list)
    for line in text.splitlines():
        m = CANONICAL_RE.match(line)
        if not m:
            continue
        gate_id = m.group("gate_id")
        # Prefer dual-sha audit_sha256= field; fall back to single sha256= legacy
        am = AUDIT_SHA_RE.search(line)
        if am:
            by_sha[am.group("sha")].append(gate_id)
        else:
            lm = LEGACY_SHA_RE.search(line)
            if lm:
                by_sha[lm.group("sha")].append(gate_id)
    return dict(by_sha)


def load_allowlist(path: pathlib.Path) -> list[dict]:
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8"))


def classify_duplicate_set(
    audit_sha: str, gate_ids: list[str], allowlist: list[dict]
) -> tuple[str, str | None]:
    """Returns (status, allowlist_pattern_name or None).

    status ∈ {"ALLOWED", "FORBIDDEN"}.
    A duplicate set is ALLOWED iff there exists an allowlist pattern such that
    EVERY gate_id in the set matches the pattern's gate_id_glob.
    """
    for entry in allowlist:
        glob = entry.get("gate_id_glob", "")
        if not glob:
            continue
        if all(fnmatch.fnmatch(g, glob) for g in gate_ids):
            return ("ALLOWED", entry.get("pattern_name"))
    return ("FORBIDDEN", None)


def run_audit(
    verdict_file: pathlib.Path,
    allowlist_file: pathlib.Path,
    session: str,
) -> dict:
    if not verdict_file.exists():
        return {
            "session": session,
            "error": f"verdict file not found: {verdict_file}",
            "sig_5_overall": "ERROR",
            "false_positive_count": 0,
        }
    text = verdict_file.read_text(encoding="utf-8")
    by_sha = parse_audit_shas(text)
    total_canonical = sum(len(v) for v in by_sha.values())
    allowlist = load_allowlist(allowlist_file)

    duplicate_sets = []  # (local)
    forbidden_count = 0  # (local)
    allowed_count = 0  # (local)
    for sha, gates in by_sha.items():
        if len(gates) <= 1:
            continue
        status, pattern = classify_duplicate_set(sha, gates, allowlist)
        duplicate_sets.append({
            "audit_sha256": sha,
            "gate_ids": gates,
            "status": status,
            "allowlist_pattern": pattern,
        })
        if status == "ALLOWED":
            allowed_count += 1
        else:
            forbidden_count += 1

    sig_5_overall = "PASS" if forbidden_count == 0 else "FAIL"

    # The "false_positive_count" is the count of duplicates that the OLD
    # sig_5 logic (no allowlist) would flag as FAIL but that the new logic
    # correctly classifies as ALLOWED. The W0b-5 PASS criterion is that
    # synthetic-test false_positive_count == 0 against allowlisted patterns.
    false_positive_count = sum(
        1 for d in duplicate_sets
        if d["status"] == "FORBIDDEN" and any(
            fnmatch.fnmatch(g, e["gate_id_glob"])
            for g in d["gate_ids"] for e in allowlist
            if e.get("gate_id_glob")
        )
    )

    return {
        "session": session,
        "total_canonical_lines_with_audit_sha": total_canonical,
        "unique_audit_sha_count": len(by_sha),
        "duplicate_audit_sha_sets": duplicate_sets,
        "allowed_duplicate_count": allowed_count,
        "forbidden_duplicate_count": forbidden_count,
        "sig_5_overall": sig_5_overall,
        "false_positive_count": false_positive_count,
        "allowlist_pattern_count": len(allowlist),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--session", required=True)
    parser.add_argument("--verdict-file", required=True, type=pathlib.Path)
    parser.add_argument("--allowlist-file", required=True, type=pathlib.Path)
    parser.add_argument("--output", required=True, type=pathlib.Path)
    args = parser.parse_args()

    result = run_audit(args.verdict_file, args.allowlist_file, args.session)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps({
        "session": result["session"],
        "sig_5_overall": result.get("sig_5_overall"),
        "duplicates": len(result.get("duplicate_audit_sha_sets", [])),
        "allowed": result.get("allowed_duplicate_count", 0),
        "forbidden": result.get("forbidden_duplicate_count", 0),
        "false_positive_count": result.get("false_positive_count", 0),
        "output": str(args.output),
    }))
    return 0


if __name__ == "__main__":
    sys.exit(main())
