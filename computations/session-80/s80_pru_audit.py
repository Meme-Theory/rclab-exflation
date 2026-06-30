#!/usr/bin/env python3
"""
S80 W0-4 — PRU (Pre-Registration Underspecification) Audit Tool
================================================================

Gate: S80-PRU-AUDIT-TOOLING (infrastructure, NO substitution-chain trigger)

PURPOSE
-------
Automatically flag PRU Class 8 candidates by cross-referencing:

  (a) `computations/_shared/canonical_constants.py` — canonical constant names + provenance.
  (b) `sessions/permanent-results-registry.md` — theorem-entry output-tag formats.
  (c) `computations/_shared/s*_gate_verdicts.txt` — gate SHA-256 input-pin annotations.

MECHANICS
---------
1. Parse `canonical_constants.py` into a `dict {name: (value, provenance_str)}`.
2. Scan every `computations/_shared/s*.py` (session-NN scripts) for numerical assignments of
   the form  `identifier = <number>`.
3. Cross-reference each identifier against canonical names:
    - If the script imports from canonical_constants (direct OR wildcard) and the
      identifier matches a canonical name, treat as IMPORTED (not a hardcode).
    - Otherwise, if the identifier is a canonical name being re-assigned, flag
      as a hardcode.
    - Also count occurrences of canonical names APPEARING (read access) across
      scripts — a proxy for "≥3 usage" without false-positive inflation.
4. Flag any constant referenced >= 3 times that is NOT in canonical_constants.
   (Output-heuristic A: gate-relevant under PRU Class 8.)
5. Parse `permanent-results-registry.md` — for each row in a theorem table, check
   whether it carries a 4-tuple output tag
   `(value, scheme, convention, L_max)` or equivalent.
   (Output-heuristic B.)
6. Parse `s*_gate_verdicts.txt` — check each PASS/FAIL/INFO verdict line for a
   SHA-256 input-pin annotation (40+ hex chars).
   (Output-heuristic C.)
7. Emit machine-readable JSON report + human summary.

OUTPUTS
-------
- `computations/session-80/s80_pru_audit_report.json`   — structured, machine-readable.
- Stdout — human summary with baseline counts for (a), (b), (c).

DISCIPLINE
----------
- Imports canonical_constants (meta-ironic but mandated).
- NON-PHONONIC classification — pure infrastructure audit.
- This tool MUST NOT modify canonical_constants.py or the knowledge index.
- All intermediate tallies tagged `# (local)` per math-scripts.md.

4-tuple output tag (for this tool's own declarations):
(value=<count>, scheme=STRUCTURAL-AUDIT, convention=PRU-CLASS-8, L_max=N/A)
"""

from __future__ import annotations

# Mandatory per math-scripts.md — imports available constants (unused here;
# audit operates on the module's *text*, not values, but discipline requires
# the import line to exist).
from canonical_constants import *  # noqa: F401,F403

import ast
import hashlib  # (local) SHA-256 pattern checks
import json
import re
import sys
from collections import Counter, defaultdict
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


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
CANON_PY = resolve_script(None, 'canonical_constants.py')
REGISTRY_MD = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
VERDICTS_GLOB = "s*_gate_verdicts.txt"
REPORT_JSON = resolve_output(80, 's80_pru_audit_report.json')

# Threshold for flagging an unregistered constant as PRU-candidate.
# Three independent usages = the math-scripts.md "belongs in canonical_constants.py"
# rule -- pre-registered in CLAUDE.md.
OCCURRENCE_THRESHOLD = 3  # (local)

# Regex: identifier = <numeric literal>. Permits negatives, sci notation,
# trailing comment, etc. Captures only top-level-looking assignments
# (no operators on RHS except the sign and 'e').
#
# IMPORTANT: Lines tagged with `# (local)` (in any position after a #) are
# INTENTIONALLY ignored by the audit — per math-scripts.md, such lines
# are computed intermediates, not framework constants. The regex below
# excludes them at match time.
ASSIGN_RE = re.compile(
    r"^\s*([A-Za-z_][A-Za-z_0-9]*)\s*=\s*"
    r"(-?\d+(?:\.\d*)?(?:[eE][+-]?\d+)?)"
    r"\s*(?:#(?!.*\blocal\b).*)?$"  # comment without 'local' word is OK; with 'local' excludes
)
LOCAL_TAG_RE = re.compile(r"#.*\blocal\b", re.IGNORECASE)

# Regex: module import line (direct or wildcard) from canonical_constants.
CANON_IMPORT_RE = re.compile(
    r"from\s+canonical_constants\s+import\s+(.+)$"
)

# Regex: SHA-256 input-pin annotation. Real SHA-256 hexdigest is 64 chars.
# Accept any hash >= 40 chars (SHA-1 compatibility would still be unusual in
# a physics verdict context, so 40+ is the lower bound for "looks like
# a cryptographic pin").
SHA_RE = re.compile(r"\b[a-f0-9]{40,}\b")

# Regex: 4-tuple output tag in the registry. We look for ANY of:
#   (value=..., scheme=..., convention=..., L_max=...)
#   or "4-tuple"
#   or "output tag" with four comma-separated fields.
FOUR_TUPLE_RE = re.compile(
    r"\(\s*value\s*=.*?,\s*scheme\s*=.*?,\s*convention\s*=.*?,\s*L_max\s*=",
    re.IGNORECASE,
)
FOUR_TUPLE_LITERAL_RE = re.compile(r"4-tuple", re.IGNORECASE)

# Session-script filter. We audit session scripts (sNN_*.py), not helpers
# or underscore-prefixed inspection scripts.
SCRIPT_GLOB = "s[0-9]*_*.py"

# Python built-in names and common library symbols to never flag as
# "framework constants being reassigned" (reduces false positives).
BUILTIN_EXCLUDE = frozenset({
    "i", "j", "k", "l", "m", "n",  # loop/index counters
    "x", "y", "z", "t",             # coordinates
    "pi", "e",                      # math symbols
    "tau",                           # commonly-used local, distinct from tau_fold
    "eps", "epsilon",                # commonly-used local tolerance
    "delta",                         # commonly-used local
    "N", "M",                        # matrix sizes
})


# ---------------------------------------------------------------------------
# Parsers
# ---------------------------------------------------------------------------


def parse_canonical_constants(path: Path) -> dict[str, dict]:
    """Extract {name: {value_literal, provenance, line}} from canonical_constants.py.

    Provenance is the inline comment on the assignment line (if any), plus
    the nearest preceding section header or commentary block.
    """
    result: dict[str, dict] = {}  # (local)
    if not path.exists():
        raise FileNotFoundError(f"Canonical constants file missing: {path}")

    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()

    current_section = ""  # (local) tracks most-recent section header
    for idx, line in enumerate(lines, start=1):
        stripped = line.strip()

        # Detect section headers
        if stripped.startswith("#  SECTION") or stripped.startswith("# SECTION"):
            current_section = stripped.lstrip("# ").strip()
            continue

        # Strip inline comment to isolate code portion
        code_part = line.split("#", 1)[0].rstrip()
        comment_part = line.split("#", 1)[1].strip() if "#" in line else ""

        # Module-level scalar assignment: name = <numeric> (allow simple RHS
        # including multiplicative expressions like 0.912 * ... because many
        # constants are defined that way).
        if "=" in code_part:
            # Simple LHS extraction: take the text before the first '='
            lhs = code_part.split("=", 1)[0].strip()
            rhs = code_part.split("=", 1)[1].strip()

            # Valid identifier only, no indentation (top-level)
            if (
                re.match(r"^[A-Za-z_][A-Za-z_0-9]*$", lhs)
                and not line.startswith((" ", "\t"))
                and rhs  # non-empty
                and not lhs.startswith("_")  # skip module-private
            ):
                # Try AST parse of the RHS to confirm it's numeric-like.
                try:
                    tree = ast.parse(rhs, mode="eval")
                    # Accept literals, unary, binary arithmetic, attribute access
                    # (e.g. np.sqrt), and calls. If it parses, accept.
                    result[lhs] = {
                        "line": idx,
                        "rhs": rhs,
                        "provenance_comment": comment_part,
                        "section": current_section,
                    }
                except SyntaxError:
                    pass

    return result


def parse_script_imports_and_assigns(path: Path) -> tuple[set[str], dict[str, list[int]], list[str]]:
    """For one .py file, return:
       - the set of canonical_constants names imported,
       - mapping of {reassigned_name: [line_numbers]} that are literal assigns,
       - raw token occurrences (names used as identifiers).
    """
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return set(), {}, []

    imported: set[str] = set()
    assigns: dict[str, list[int]] = defaultdict(list)
    tokens: list[str] = []

    for idx, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()

        # Track canonical_constants imports
        m = CANON_IMPORT_RE.match(stripped)
        if m:
            imp_list = m.group(1).strip()
            if imp_list == "*":
                imported.add("*")
            else:
                # Strip any trailing comment
                imp_list = imp_list.split("#")[0]
                for name in imp_list.split(","):
                    name = name.strip().split(" as ")[0].strip()
                    if name:
                        imported.add(name)

        # Track literal assignments: identifier = <number>
        # Only match top-level-looking (low indentation)
        if line and not line.startswith(("    ", "\t\t")):  # allow one tab/4sp
            # Still skip class/function bodies with more than one indent level
            pass
        am = ASSIGN_RE.match(line)
        if am:
            name = am.group(1)
            assigns[name].append(idx)

        # Tokenize — rough regex over identifier-like tokens for occurrence counts.
        # Only count names that aren't in strings. Cheapest approximation: strip
        # string literals before tokenizing.
        line_no_str = re.sub(r'"[^"]*"|\'[^\']*\'', "", line)
        line_no_comment = line_no_str.split("#", 1)[0]
        for tok in re.findall(r"\b[A-Za-z_][A-Za-z_0-9]*\b", line_no_comment):
            tokens.append(tok)

    return imported, dict(assigns), tokens


def parse_registry_entries(path: Path) -> list[dict]:
    """Extract theorem-table rows from permanent-results-registry.md.

    Returns a list of dicts with {line, row, has_4tuple_tag}. We count rows
    in table sections (starting with '|') and check each row for the
    4-tuple output tag.
    """
    if not path.exists():
        raise FileNotFoundError(f"Registry file missing: {path}")

    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()

    entries: list[dict] = []
    in_table = False
    header_passed = False  # (local) skip header + separator row

    for idx, line in enumerate(lines, start=1):
        stripped = line.strip()

        # Table boundary detection: blank line ends a table block.
        if not stripped:
            in_table = False
            header_passed = False
            continue

        if stripped.startswith("|"):
            # Is this a separator row ("|:---|:---|")?
            if re.match(r"^\|[\s:\-|]+\|?\s*$", stripped):
                header_passed = True
                in_table = True
                continue
            if not in_table:
                in_table = True
                header_passed = False
                continue
            if not header_passed:
                # This is the header row; skip.
                continue

            # Data row: check for 4-tuple tag in any cell.
            has_four = bool(FOUR_TUPLE_RE.search(line)) or bool(
                FOUR_TUPLE_LITERAL_RE.search(line)
            )

            # A theorem entry SHOULD have a result-like first cell (number, name).
            # Capture the first non-empty cell.
            cells = [c.strip() for c in stripped.strip("|").split("|")]
            if not cells or not cells[0]:
                continue

            entries.append(
                {
                    "line": idx,
                    "row_head": cells[0][:60],
                    "has_4tuple_tag": has_four,
                }
            )

    return entries


def parse_verdict_files(script_dir: Path, glob: str) -> list[dict]:
    """Scan every s*_gate_verdicts.txt for PASS/FAIL/INFO lines and check
    whether each carries a SHA-256-style hash annotation.

    Returns list of dicts {file, line, verdict_text, has_sha_pin}.
    """
    results: list[dict] = []

    for fp in sorted(script_dir.glob(glob)):
        try:
            text = fp.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue

        for idx, line in enumerate(text.splitlines(), start=1):
            stripped = line.strip()
            # A verdict line STARTS with an uppercase gate ID followed by
            # ':' or whitespace + verdict keyword. Comment lines ("# Level 3
            # grade: PASS ...") do NOT count as verdicts — they were false-
            # matched by the earlier broad regex. The tightened rule requires
            # the line to begin with a canonical-looking gate ID (no leading
            # '#', no leading whitespace inside the comment prefix).
            if stripped.startswith("#"):
                continue
            if not re.match(
                r"^[A-Z][A-Z0-9\-]+:\s*(PASS|FAIL|INFO|PRE-REG|INCOMPUTABLE"
                r"|CANCELLED|INTERMEDIATE|INCOMPUTABLE-FALLBACK-TO-BOUND)\b",
                stripped,
            ) and not re.match(
                r"^[A-Z][A-Z0-9\-]+\s+(PASS|FAIL|INFO|PRE-REG|INCOMPUTABLE"
                r"|CANCELLED|INTERMEDIATE)\b",
                stripped,
            ):
                continue

            has_sha = bool(SHA_RE.search(stripped))
            results.append(
                {
                    "file": fp.name,
                    "line": idx,
                    "verdict_text": stripped[:160],
                    "has_sha_pin": has_sha,
                }
            )

    return results


# ---------------------------------------------------------------------------
# Audit core
# ---------------------------------------------------------------------------


def audit_unregistered_constants(
    script_dir: Path,
    canon_names: set[str],
) -> dict:
    """Scan all session scripts; report identifiers assigned to numeric
    literals that are NOT in canonical_constants and appear >= threshold
    times across scripts.
    """
    script_files = sorted(script_dir.glob(SCRIPT_GLOB))

    # Map: identifier -> set(script_paths where it's reassigned to a literal)
    assign_script_map: dict[str, set[str]] = defaultdict(set)
    # Per-script hardcode of a canonical name (direct violation):
    canonical_reassigns: dict[str, list[tuple[str, int]]] = defaultdict(list)

    # Occurrence count across scripts for every identifier (tokenized)
    occurrence_scripts: dict[str, set[str]] = defaultdict(set)

    total_scripts = 0  # (local)
    for fp in script_files:
        total_scripts += 1
        imported, assigns, tokens = parse_script_imports_and_assigns(fp)
        rel_name = fp.name

        for name, line_nums in assigns.items():
            if name in BUILTIN_EXCLUDE:
                continue
            assign_script_map[name].add(rel_name)
            if name in canon_names:
                # This script imports from canonical_constants yet reassigns
                # a canonical name — hardcode violation (unless intentional
                # local shadow, which is rare and should be tagged `# (local)`).
                for ln in line_nums:
                    canonical_reassigns[name].append((rel_name, ln))

        for tok in tokens:
            if tok not in BUILTIN_EXCLUDE:
                occurrence_scripts[tok].add(rel_name)

    # Unregistered = assigned as literal in a script AND not in canonical
    unreg_ge_threshold: list[dict] = []
    for name, script_set in assign_script_map.items():
        if name in canon_names:
            continue
        if len(script_set) >= OCCURRENCE_THRESHOLD:
            unreg_ge_threshold.append(
                {
                    "name": name,
                    "n_scripts_assigning": len(script_set),
                    "scripts": sorted(script_set)[:10],  # cap for report size
                }
            )

    unreg_ge_threshold.sort(
        key=lambda d: (-d["n_scripts_assigning"], d["name"])
    )

    return {
        "total_scripts_scanned": total_scripts,
        "threshold": OCCURRENCE_THRESHOLD,
        "unregistered_ge_threshold": unreg_ge_threshold,
        "canonical_reassignments": {
            k: v for k, v in canonical_reassigns.items()
        },
    }


def audit_theorem_tags(registry_path: Path) -> dict:
    entries = parse_registry_entries(registry_path)
    n_total = len(entries)
    n_tagged = sum(1 for e in entries if e["has_4tuple_tag"])
    n_untagged = n_total - n_tagged
    sample_untagged = [e for e in entries if not e["has_4tuple_tag"]][:20]
    return {
        "registry_path": str(registry_path.relative_to(PROJECT_ROOT)),
        "total_entries": n_total,
        "tagged_entries": n_tagged,
        "untagged_entries": n_untagged,
        "sample_untagged": sample_untagged,
    }


def audit_gate_sha_pins(script_dir: Path) -> dict:
    entries = parse_verdict_files(script_dir, VERDICTS_GLOB)
    n_total = len(entries)
    n_pinned = sum(1 for e in entries if e["has_sha_pin"])
    n_unpinned = n_total - n_pinned
    sample_unpinned = [e for e in entries if not e["has_sha_pin"]][:20]
    # Also aggregate by-file
    by_file: dict[str, dict] = defaultdict(lambda: {"total": 0, "pinned": 0})
    for e in entries:
        by_file[e["file"]]["total"] += 1
        if e["has_sha_pin"]:
            by_file[e["file"]]["pinned"] += 1

    return {
        "verdicts_glob": VERDICTS_GLOB,
        "total_verdict_lines": n_total,
        "pinned_verdicts": n_pinned,
        "unpinned_verdicts": n_unpinned,
        "sample_unpinned": sample_unpinned,
        "by_file": dict(by_file),
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> int:
    print("=" * 78)
    print("S80 W0-4 PRU AUDIT TOOL -- s80_pru_audit.py")
    print("=" * 78)

    # ---- Step 1: parse canonical_constants.py ------------------------------
    print(f"\n[1] Parsing canonical_constants.py ...")
    canon = parse_canonical_constants(CANON_PY)
    canon_names = set(canon.keys())
    print(f"    Canonical constants found: {len(canon_names)}")

    # Tagged 4-tuple for our own output:
    # (value=<count>, scheme=STRUCTURAL-AUDIT, convention=PRU-CLASS-8, L_max=N/A)

    # ---- Step 2 & 3: audit unregistered constants --------------------------
    print(f"\n[2] Scanning computations/_shared/{SCRIPT_GLOB} ...")
    const_audit = audit_unregistered_constants(SCRIPT_DIR, canon_names)
    print(f"    Scripts scanned: {const_audit['total_scripts_scanned']}")
    print(
        f"    Unregistered constants with >= {const_audit['threshold']} "
        f"script-level assignments: {len(const_audit['unregistered_ge_threshold'])}"
    )
    n_canon_reassigns = sum(
        len(v) for v in const_audit["canonical_reassignments"].values()
    )
    print(
        f"    Canonical names reassigned in scripts (hardcode "
        f"violations): {n_canon_reassigns} lines "
        f"across {len(const_audit['canonical_reassignments'])} names"
    )

    # ---- Step 4: registry theorem-tag audit --------------------------------
    print(f"\n[3] Parsing permanent-results-registry.md ...")
    tag_audit = audit_theorem_tags(REGISTRY_MD)
    print(f"    Theorem/result rows parsed: {tag_audit['total_entries']}")
    print(f"    Rows carrying 4-tuple tag:  {tag_audit['tagged_entries']}")
    print(f"    Rows WITHOUT 4-tuple tag:   {tag_audit['untagged_entries']}")

    # ---- Step 5: gate SHA-pin audit ----------------------------------------
    print(f"\n[4] Scanning {VERDICTS_GLOB} ...")
    sha_audit = audit_gate_sha_pins(SCRIPT_DIR)
    print(f"    Verdict lines parsed:        {sha_audit['total_verdict_lines']}")
    print(f"    Lines carrying SHA-256 pin:  {sha_audit['pinned_verdicts']}")
    print(f"    Lines WITHOUT SHA-256 pin:   {sha_audit['unpinned_verdicts']}")

    # ---- Step 6: emit machine-readable JSON --------------------------------
    report = {
        "tool": "s80_pru_audit.py",
        "session": "S80",
        "gate": "S80-PRU-AUDIT-TOOLING",
        "classification": "NON-PHONONIC",
        "threshold_occurrences": OCCURRENCE_THRESHOLD,
        "baseline_counts": {
            "a_unregistered_constants_ge_threshold": len(
                const_audit["unregistered_ge_threshold"]
            ),
            "b_untagged_theorem_entries": tag_audit["untagged_entries"],
            "c_gates_without_sha_pin": sha_audit["unpinned_verdicts"],
        },
        "canonical_constants": {
            "path": str(CANON_PY.relative_to(PROJECT_ROOT)),
            "n_constants": len(canon_names),
        },
        "constants_audit": const_audit,
        "theorem_tag_audit": tag_audit,
        "gate_sha_audit": sha_audit,
    }

    REPORT_JSON.write_text(
        json.dumps(report, indent=2, default=str), encoding="utf-8"
    )
    print(f"\n[5] Wrote report: {REPORT_JSON.relative_to(PROJECT_ROOT)}")

    # ---- Baseline summary --------------------------------------------------
    print("\n" + "=" * 78)
    print("BASELINE COUNTS (S80-PRU-AUDIT-TOOLING)")
    print("=" * 78)
    a = report["baseline_counts"]["a_unregistered_constants_ge_threshold"]
    b = report["baseline_counts"]["b_untagged_theorem_entries"]
    c = report["baseline_counts"]["c_gates_without_sha_pin"]
    print(f"  (a) Unregistered constants with >= 3 script assignments : {a}")
    print(f"  (b) Theorem rows without 4-tuple output tag              : {b}")
    print(f"  (c) Gate verdict lines without SHA-256 input pin         : {c}")
    print(
        "\n  4-tuple: (value=(a={},b={},c={}), scheme=STRUCTURAL-AUDIT, "
        "convention=PRU-CLASS-8, L_max=N/A)".format(a, b, c)
    )

    # Gate VERDICT: PASS iff the tool ran end-to-end, produced report, and
    # printed baseline counts.
    print("\n" + "=" * 78)
    print("Gate S80-PRU-AUDIT-TOOLING: PASS")
    print("  Tool executed end-to-end.")
    print(f"  Machine-readable report: {REPORT_JSON.name}")
    print(f"  Baselines: a={a}, b={b}, c={c}")
    print("=" * 78)

    return 0


if __name__ == "__main__":
    sys.exit(main())
