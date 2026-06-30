#!/usr/bin/env python3
"""
Canonical-Import Audit — Static Review Orchestrator
====================================================

Gate: S80-CANONICAL-AUDIT (infrastructure, NON-PHONONIC)

PURPOSE
-------
Per-script static analysis across `computations/_shared/`, combining eight
checks into a single JSON + markdown report. Output feeds the cluster-level
LLM review as the "live review set".

CHECKS (from script-review-plan.md §3)
--------------------------------------
  1. Canonical compliance  — hardcodes vs `canonical_constants.py`
  2. PRU audit extension   — per-script unregistered-constant breakdown
  3. Ruff lint             — E,F,W,I,UP,B selectors
  4. Vulture dead-code     — min confidence 80
  5. Import graph          — AST-based; who imports whom
  6. Registry cross-ref    — `permanent-results-registry.md` citations
  7. SHA-256 ledger        — recompute source hash, compare to verdict pin
  8. Knowledge-DB cross-ref — SELECT against `tools/knowledge.db`

Outputs:
  - `computations/_shared/_canonical_audit_report.json`
  - `computations/_shared/_canonical_audit_summary.md`

4-tuple output tag for this tool's declarations:
  (value=<counts>, scheme=STATIC-ANALYSIS, convention=CANONICAL-AUDIT, L_max=N/A)

DISCIPLINE
----------
- Imports canonical_constants (audit operates on *text*, not values).
- All intermediate tallies tagged `# (local)` per math-scripts.md.
"""

from __future__ import annotations

# Mandatory per math-scripts.md (audit tool; imports for discipline compliance)
from canonical_constants import *  # noqa: F401,F403

import ast
import hashlib
import json
import re
import sqlite3
import subprocess
import sys
import time
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
# X2-removed: alias 'COMPUTATIONS_ROOT' = ... 'computations' (replaced by tools.computation_root.resolve_*)
COMPUTATIONS_DIR = PROJECT_ROOT / "computations" / "_shared"
CANON_PY = resolve_script(None, 'canonical_constants.py')
REGISTRY_MD = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
KNOWLEDGE_DB = PROJECT_ROOT / "tools" / "knowledge.db"
VENV_PY = PROJECT_ROOT / "phonon-exflation-sim" / ".venv312" / "Scripts" / "python.exe"

REPORT_JSON = resolve_script(None, '_canonical_audit_report.json')
SUMMARY_MD = resolve_script(None, '_canonical_audit_summary.md')

# Ruff selectors: errors, flakes, warnings, isort, pyupgrade, bugbear.
RUFF_SELECT = "E,F,W,I,UP,B"  # (local)

# Vulture confidence floor (percent). 80 = default conservative.
VULTURE_CONF = 80  # (local)

# Script filter — session scripts only. Underscore-prefixed helpers skipped.
SCRIPT_GLOB = "s[0-9]*_*.py"
ALL_PY_GLOB = "*.py"

# Hardcode regex (reused from s80_pru_audit.py)
ASSIGN_RE = re.compile(
    r"^\s*([A-Za-z_][A-Za-z_0-9]*)\s*=\s*"
    r"(-?\d+(?:\.\d*)?(?:[eE][+-]?\d+)?)"
    r"\s*(?:#.*)?$"
)
CANON_IMPORT_RE = re.compile(
    r"from\s+canonical_constants\s+import\s+(.+)$"
)
SHA_RE = re.compile(r"\b[a-f0-9]{40,}\b")
LOCAL_TAG_RE = re.compile(r"#\s*\(?local\)?\b", re.IGNORECASE)
VERDICT_RE = re.compile(
    r":\s*(PASS|FAIL|INFO|PRE-REG|INCOMPUTABLE|CANCELLED|INTERMEDIATE"
    r"|INCOMPUTABLE-FALLBACK-TO-BOUND)\b"
)

# Don't flag built-in-looking single letters / common temporaries
BUILTIN_EXCLUDE = frozenset({
    "i", "j", "k", "l", "m", "n",
    "x", "y", "z", "t",
    "pi", "e",
    "tau",
    "eps", "epsilon",
    "delta",
    "N", "M",
})

# Session number from filename (sNN_foo.py -> NN)
SESSION_NUM_RE = re.compile(r"^s(\d+)[a-z_]")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def rel(p: Path) -> str:
    """Project-root-relative POSIX path."""
    try:
        return str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
    except ValueError:
        return str(p).replace("\\", "/")


def extract_session_num(name: str) -> int | None:
    m = SESSION_NUM_RE.match(name)
    return int(m.group(1)) if m else None


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def parse_canonical_constants(path: Path) -> dict[str, dict]:
    """Return {name: {line, rhs, provenance_comment, section}} for canonical_constants.py.

    Duplicates the parser from s80_pru_audit.py verbatim so this orchestrator
    doesn't create a circular dependency on the audit tool's internals.
    """
    result: dict[str, dict] = {}  # (local)
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()

    current_section = ""  # (local)
    for idx, line in enumerate(lines, start=1):
        stripped = line.strip()
        if stripped.startswith("#  SECTION") or stripped.startswith("# SECTION"):
            current_section = stripped.lstrip("# ").strip()
            continue

        code_part = line.split("#", 1)[0].rstrip()
        comment_part = line.split("#", 1)[1].strip() if "#" in line else ""

        if "=" not in code_part:
            continue
        lhs = code_part.split("=", 1)[0].strip()
        rhs = code_part.split("=", 1)[1].strip()
        if (
            re.match(r"^[A-Za-z_][A-Za-z_0-9]*$", lhs)
            and not line.startswith((" ", "\t"))
            and rhs
            and not lhs.startswith("_")
        ):
            try:
                ast.parse(rhs, mode="eval")
                result[lhs] = {
                    "line": idx,
                    "rhs": rhs[:80],
                    "provenance_comment": comment_part[:120],
                    "section": current_section,
                }
            except SyntaxError:
                pass

    return result


# ---------------------------------------------------------------------------
# Per-script scan (Checks 1 + 2 + 5)
# ---------------------------------------------------------------------------

def scan_script(
    path: Path,
    canon_names: set[str],
) -> dict:
    """Single-file pass: canonical compliance, hardcode violations,
    local-tag coverage, AST imports, sha256 source hash.

    Returns per-script record (dict).
    """
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return {
            "path": rel(path),
            "error": "read-failed",
            "imports_canonical": False,
            "imports_canonical_wildcard": False,
            "imported_names": [],
            "hardcoded_canonical": [],
            "unregistered_literals": [],
            "untagged_literals": [],
            "external_imports": [],
            "relative_imports": [],
            "sha256": "",
            "n_lines": 0,
        }

    lines = text.splitlines()
    sha = hashlib.sha256(text.encode("utf-8", errors="replace")).hexdigest()  # (local)

    imported_names: set[str] = set()
    has_wildcard = False  # (local)
    external_imports: set[str] = set()
    relative_imports: set[str] = set()

    hardcoded_canonical: list[dict] = []
    unregistered_literals: list[dict] = []
    untagged_literals: list[dict] = []

    for idx, line in enumerate(lines, start=1):
        stripped = line.strip()

        # Canonical import
        m = CANON_IMPORT_RE.match(stripped)
        if m:
            imp_list = m.group(1).split("#", 1)[0].strip()
            if imp_list == "*":
                has_wildcard = True
            else:
                for name in imp_list.split(","):
                    name = name.strip().split(" as ")[0].strip()
                    if name and name != "*":
                        imported_names.add(name)

    # AST-based imports (more robust than regex for non-canonical modules)
    try:
        tree = ast.parse(text, filename=str(path))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    external_imports.add(alias.name.split(".")[0])
            elif isinstance(node, ast.ImportFrom):
                mod = node.module or ""
                level = node.level or 0
                if mod == "canonical_constants":
                    continue  # tallied above
                if level > 0:
                    relative_imports.add(mod or f".(level={level})")
                else:
                    external_imports.add(mod.split(".")[0])
    except SyntaxError:
        pass  # keep going; flag in issues

    imports_canonical = bool(has_wildcard or imported_names)

    # Literal-assignment scan (reused pattern from s80_pru_audit.py)
    for idx, line in enumerate(lines, start=1):
        am = ASSIGN_RE.match(line)
        if not am:
            continue
        name = am.group(1)
        literal = am.group(2)
        if name in BUILTIN_EXCLUDE:
            continue

        is_tagged_local = bool(LOCAL_TAG_RE.search(line))

        if name in canon_names:
            # Reassignment of a canonical name with a literal — violation
            # unless explicitly tagged (# (local)) as a local shadow.
            if not is_tagged_local:
                hardcoded_canonical.append({
                    "name": name,
                    "line": idx,
                    "literal": literal,
                    "src": stripped[:120],
                })
        else:
            # Unregistered constant-shaped assignment. Emit if untagged.
            record = {
                "name": name,
                "line": idx,
                "literal": literal,
                "src": stripped[:120],
            }
            unregistered_literals.append(record)
            if not is_tagged_local:
                untagged_literals.append(record)

    return {
        "path": rel(path),
        "error": "",
        "imports_canonical": imports_canonical,
        "imports_canonical_wildcard": has_wildcard,
        "imported_names": sorted(imported_names),
        "hardcoded_canonical": hardcoded_canonical,
        "unregistered_literals": unregistered_literals,
        "untagged_literals": untagged_literals,
        "external_imports": sorted(external_imports),
        "relative_imports": sorted(relative_imports),
        "sha256": sha,
        "n_lines": len(lines),
    }


# ---------------------------------------------------------------------------
# Check 3 — Ruff
# ---------------------------------------------------------------------------

def run_ruff(targets: list[Path]) -> dict:
    """Run ruff across targets with JSON output. Returns per-file counts + sampled issues."""
    if not targets:
        return {"total_issues": 0, "per_file": {}, "ran": False}

    # Ruff accepts multiple directory arguments.
    cmd = [
        str(VENV_PY), "-m", "ruff", "check",
        "--output-format", "json",
        "--select", RUFF_SELECT,
        "--exit-zero",
    ] + [str(t) for t in targets]

    t0 = time.time()  # (local)
    try:
        proc = subprocess.run(
            cmd, capture_output=True, text=True, cwd=str(PROJECT_ROOT), timeout=900,
        )
    except subprocess.TimeoutExpired:
        return {"total_issues": 0, "per_file": {}, "ran": False, "error": "timeout"}
    wall = time.time() - t0  # (local)

    try:
        issues = json.loads(proc.stdout or "[]")
    except json.JSONDecodeError:
        issues = []

    per_file: dict[str, dict] = defaultdict(
        lambda: {"n_issues": 0, "by_code": Counter(), "sample": []}
    )
    for issue in issues:
        fname = issue.get("filename", "")
        try:
            rp = rel(Path(fname))
        except Exception:
            rp = fname
        per_file[rp]["n_issues"] += 1
        per_file[rp]["by_code"][issue.get("code", "?")] += 1
        if len(per_file[rp]["sample"]) < 3:
            per_file[rp]["sample"].append({
                "code": issue.get("code", "?"),
                "line": issue.get("location", {}).get("row", 0),
                "msg": (issue.get("message", "") or "")[:140],
            })

    # Convert Counter -> dict for JSON serialization
    out = {rp: {
        "n_issues": d["n_issues"],
        "by_code": dict(d["by_code"]),
        "sample": d["sample"],
    } for rp, d in per_file.items()}

    return {
        "total_issues": len(issues),
        "per_file": out,
        "ran": True,
        "wall_seconds": round(wall, 2),
        "ruff_cmd_select": RUFF_SELECT,
        "stderr_head": (proc.stderr or "")[:400],
    }


# ---------------------------------------------------------------------------
# Check 4 — Vulture
# ---------------------------------------------------------------------------

def run_vulture(targets: list[Path]) -> dict:
    """Run vulture across targets; parse its text output into per-file findings.

    vulture's --json output is only in newer versions; we parse the default
    "path:line: kind 'name' (confidence% confidence)" format for portability.
    """
    if not targets:
        return {"total_dead": 0, "per_file": {}, "ran": False}

    cmd = [
        str(VENV_PY), "-m", "vulture",
        "--min-confidence", str(VULTURE_CONF),
    ] + [str(t) for t in targets]

    t0 = time.time()  # (local)
    try:
        proc = subprocess.run(
            cmd, capture_output=True, text=True, cwd=str(PROJECT_ROOT), timeout=900,
        )
    except subprocess.TimeoutExpired:
        return {"total_dead": 0, "per_file": {}, "ran": False, "error": "timeout"}
    wall = time.time() - t0  # (local)

    per_file: dict[str, list] = defaultdict(list)
    line_re = re.compile(
        r"^(.+?):(\d+):\s+(\w+[\w\s]*?)\s+'([^']+)'.*?\((\d+)%\s*confidence\)"
    )
    total = 0  # (local)
    for line in (proc.stdout or "").splitlines():
        m = line_re.match(line)
        if not m:
            continue
        fname, ln, kind, name, conf = m.groups()
        try:
            rp = rel(Path(fname))
        except Exception:
            rp = fname
        per_file[rp].append({
            "line": int(ln),
            "kind": kind.strip(),
            "name": name,
            "confidence": int(conf),
        })
        total += 1

    out = {rp: {
        "n_findings": len(lst),
        "findings_sample": lst[:5],
    } for rp, lst in per_file.items()}

    return {
        "total_dead": total,
        "per_file": out,
        "ran": True,
        "wall_seconds": round(wall, 2),
        "confidence_floor": VULTURE_CONF,
    }


# ---------------------------------------------------------------------------
# Check 5 — Import graph (built inside scan_script)
# ---------------------------------------------------------------------------

def build_local_import_graph(
    scans: list[dict],
    all_script_names: set[str],
) -> dict:
    """From per-script AST imports, build the subset graph over computation scripts.

    Python lets you `import s60_foo` when s60_foo.py sits next to the caller
    (sys.path[0] usage). We detect these intra-project imports by matching
    `external_imports` against the set of computation .py basenames (without suffix).
    """
    basename_set = {n.rsplit(".", 1)[0] for n in all_script_names}

    # forward: who X imports
    forward: dict[str, list[str]] = {}
    # reverse: who imports X
    reverse: dict[str, list[str]] = defaultdict(list)

    for s in scans:
        script_basename = Path(s["path"]).name.rsplit(".", 1)[0]
        imports_local = [
            m for m in s.get("external_imports", [])
            if m in basename_set and m != script_basename
        ]
        forward[s["path"]] = sorted(imports_local)
        for tgt in imports_local:
            reverse[tgt].append(script_basename)

    return {
        "forward": forward,
        "reverse": {k: sorted(set(v)) for k, v in reverse.items()},
    }


# ---------------------------------------------------------------------------
# Check 6 — Registry + canonical_constants PROVENANCE cross-reference
# ---------------------------------------------------------------------------

def parse_registry_citations(registry: Path) -> set[str]:
    """Return the set of script basenames cited anywhere in permanent-results-registry.md."""
    if not registry.exists():
        return set()
    text = registry.read_text(encoding="utf-8", errors="replace")
    # Match both `s54_foo.py` and `s60a_foo.py` and any .py reference
    cites = set(re.findall(r"\bs\d+[a-z]?_[A-Za-z0-9_]+\.py\b", text))
    # Also: some registry lines reference just the basename without .py
    cites |= {c for c in re.findall(r"\bs\d+[a-z]?_[A-Za-z0-9_]+\b", text)
              if not c.endswith(".py")}
    # Normalize by adding .py if missing so we can intersect with file names
    out = set()
    for c in cites:
        out.add(c if c.endswith(".py") else c + ".py")
    return out


def parse_canonical_provenance_citations(canon: Path) -> set[str]:
    """Extract script filenames referenced in canonical_constants.py comments.

    The file uses patterns like `# source: s62_m_top_3loop.py` or
    `# (s55_foo, S60 W1-A)` in provenance comments.
    """
    if not canon.exists():
        return set()
    text = canon.read_text(encoding="utf-8", errors="replace")
    cites = set(re.findall(r"\bs\d+[a-z]?_[A-Za-z0-9_]+(?:\.py)?\b", text))
    out = set()
    for c in cites:
        out.add(c if c.endswith(".py") else c + ".py")
    return out


# ---------------------------------------------------------------------------
# Check 7 — SHA-256 ledger (recompute source + closure hash, compare to verdict pin)
# ---------------------------------------------------------------------------

def build_sha_ledger(
    computations_dir: Path,
    script_sha_map: dict[str, str],
) -> dict:
    """Scan every s*_gate_verdicts.txt for pinned hashes, compare to recomputed.

    A verdict line matches a pin when it contains a 40+ hex-char token.
    Match the pin against the source SHA of any computation script; report hit/miss.
    """
    sha_to_script = defaultdict(list)  # (local) hash -> script path(s)
    for path, sha in script_sha_map.items():
        if sha:
            sha_to_script[sha].append(path)

    entries: list[dict] = []
    ledger_files = sorted(computations_dir.glob("s*_gate_verdicts.txt"))
    n_pinned = 0  # (local)
    n_matched = 0  # (local)
    n_unmatched = 0  # (local)

    for fp in ledger_files:
        try:
            text = fp.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for idx, line in enumerate(text.splitlines(), start=1):
            stripped = line.strip()
            if not VERDICT_RE.search(stripped):
                continue
            shas_on_line = SHA_RE.findall(stripped)
            if not shas_on_line:
                continue
            for pin in shas_on_line:
                n_pinned += 1
                matched_scripts = sha_to_script.get(pin, [])
                if matched_scripts:
                    n_matched += 1
                else:
                    n_unmatched += 1
                entries.append({
                    "verdict_file": fp.name,
                    "line": idx,
                    "pin_sha": pin,
                    "matched_scripts": matched_scripts,
                    "verdict_head": stripped[:100],
                })

    return {
        "n_pinned_verdicts": n_pinned,
        "n_matched": n_matched,
        "n_unmatched": n_unmatched,
        "ledger_entries": entries[:200],  # cap for report size
        "ledger_entries_total": len(entries),
    }


# ---------------------------------------------------------------------------
# Check 8 — Knowledge DB cross-reference
# ---------------------------------------------------------------------------

def knowledge_db_crossref(db_path: Path) -> dict:
    """SELECT against the knowledge DB to enumerate scripts referenced by
    theorems, gates, closed_mechanisms, and data_provenance.

    Returns a set of script basenames the MCP knows about, plus per-script
    provenance hits from data_provenance.
    """
    if not db_path.exists():
        return {"available": False, "note": "knowledge.db missing; run /weave --db-sync"}

    conn = sqlite3.connect(str(db_path))
    try:
        cur = conn.cursor()

        # data_provenance.script is canonical (JSON array or comma-sep string)
        cur.execute("SELECT script, session, name, gates_informed FROM data_provenance")
        prov_rows = cur.fetchall()

        prov_scripts: set[str] = set()
        prov_by_script: dict[str, list[dict]] = defaultdict(list)

        for script_field, session, name, gates in prov_rows:
            if not script_field:
                continue
            # scripts may be a single name, a comma-joined string, or JSON array
            candidates: list[str] = []
            if isinstance(script_field, str):
                s = script_field.strip()
                if s.startswith("["):
                    try:
                        candidates = [str(x) for x in json.loads(s)]
                    except Exception:
                        candidates = [s]
                else:
                    candidates = [x.strip() for x in s.split(",") if x.strip()]
            for c in candidates:
                base = c if c.endswith(".py") else c + ".py"
                prov_scripts.add(base)
                prov_by_script[base].append({
                    "session": session,
                    "name": name,
                    "gates_informed": gates,
                })

        # Fetch aggregate counts for reporting
        cur.execute("SELECT COUNT(*) FROM theorems")
        n_theorems = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM gates")
        n_gates = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM closed_mechanisms")
        n_closed = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM sessions")
        n_sessions = cur.fetchone()[0]

        return {
            "available": True,
            "n_theorems": n_theorems,
            "n_gates": n_gates,
            "n_closed_mechanisms": n_closed,
            "n_sessions": n_sessions,
            "n_data_provenance_rows": len(prov_rows),
            "cited_scripts_from_provenance": sorted(prov_scripts),
            "per_script_provenance": {
                k: v[:5] for k, v in prov_by_script.items()  # cap
            },
        }
    finally:
        conn.close()


# ---------------------------------------------------------------------------
# Synthesis: live-review set + priority ranking
# ---------------------------------------------------------------------------

def synthesize(
    scans: list[dict],
    registry_cites: set[str],
    canon_cites: set[str],
    mcp_cites: set[str],
    import_graph: dict,
    ruff: dict,
    vulture: dict,
) -> dict:
    """Combine all checks into per-script verdict + priority rank."""
    scripts_by_name = {Path(s["path"]).name: s for s in scans}
    reverse_imports = import_graph.get("reverse", {})

    broad_set: list[dict] = []
    narrow_set: list[dict] = []
    anchor_set: list[dict] = []
    archive_dead: list[str] = []
    orphan: list[str] = []

    for s in scans:
        name = Path(s["path"]).name
        is_archive = False  # archive directory removed
        session_num = extract_session_num(name) or 0

        cited_in_registry = name in registry_cites
        cited_in_canon = name in canon_cites
        cited_in_mcp = name in mcp_cites
        basename = name.rsplit(".", 1)[0]
        imported_by = reverse_imports.get(basename, [])
        n_importers = len(imported_by)

        cited_anywhere = (
            cited_in_registry or cited_in_canon or cited_in_mcp or n_importers > 0
        )
        # "Anchor" = strong citation (canon PROVENANCE or MCP data_provenance).
        # These are the GPU-rerun candidates.
        is_anchor = cited_in_canon or cited_in_mcp or cited_in_registry

        rf = ruff.get("per_file", {}).get(s["path"], {})
        vu = vulture.get("per_file", {}).get(s["path"], {})
        n_ruff = rf.get("n_issues", 0)  # (local)
        n_vult = vu.get("n_findings", 0)  # (local)
        n_hardcode = len(s.get("hardcoded_canonical", []))
        n_untagged = len(s.get("untagged_literals", []))

        # Issue severity grade (pre-classification; cluster-review agents refine)
        if n_hardcode or not s.get("imports_canonical"):
            grade = "NEEDS-CANONICAL-MIGRATION"
        elif n_ruff > 10 or n_vult > 5:
            grade = "STATIC-LINT-HEAVY"
        elif n_untagged > 5:
            grade = "LOCAL-TAG-DEBT"
        elif n_ruff == 0 and n_vult == 0 and n_hardcode == 0 and n_untagged <= 2:
            grade = "AUDIT-CLEAN"
        else:
            grade = "AUDIT-MINOR"

        # Two priority rankings:
        #   priority_review — recency dominates (cluster-review newest-first)
        #   priority_anchor — citations dominate (re-run anchor-first)
        impact = (
            3 * int(cited_in_canon)
            + 2 * int(cited_in_registry)
            + 2 * int(cited_in_mcp)
            + int(n_importers > 0)
        )
        priority_review = session_num * 10 + impact  # (local)
        priority_anchor = impact * 100 + session_num  # (local)

        record = {
            "path": s["path"],
            "name": name,
            "archived": is_archive,
            "session_num": session_num,
            "cited_in_registry": cited_in_registry,
            "cited_in_canon": cited_in_canon,
            "cited_in_mcp": cited_in_mcp,
            "is_anchor": is_anchor,
            "n_importers": n_importers,
            "importers": imported_by[:10],
            "imports_canonical": s.get("imports_canonical", False),
            "n_hardcoded_canonical": n_hardcode,
            "n_untagged_literals": n_untagged,
            "n_ruff_issues": n_ruff,
            "n_vulture_findings": n_vult,
            "grade": grade,
            "priority_review": priority_review,
            "priority_anchor": priority_anchor,
            "sha256": s.get("sha256", ""),
        }

        if is_archive:
            if not cited_anywhere:
                archive_dead.append(s["path"])
            else:
                broad_set.append(record)
                narrow_set.append(record)
                if is_anchor:
                    anchor_set.append(record)
        else:
            # computations
            if cited_anywhere or session_num >= 52:
                broad_set.append(record)
            else:
                orphan.append(s["path"])
            if cited_anywhere:
                narrow_set.append(record)
            if is_anchor:
                anchor_set.append(record)

    # Sort:
    #   broad_set  by priority_review (recency first)
    #   narrow_set by priority_review (recency first) among cited-anywhere
    #   anchor_set by priority_anchor (impact first) — re-run input
    broad_set.sort(key=lambda r: (-r["priority_review"], r["path"]))
    narrow_set.sort(key=lambda r: (-r["priority_review"], r["path"]))
    anchor_set.sort(key=lambda r: (-r["priority_anchor"], r["path"]))

    return {
        "broad_live_set": broad_set,
        "narrow_live_set": narrow_set,
        "anchor_set": anchor_set,
        "archive_dead_scripts": sorted(archive_dead),
        "orphan_scripts": sorted(orphan),
        "n_broad": len(broad_set),
        "n_narrow": len(narrow_set),
        "n_anchor": len(anchor_set),
        "n_archive_dead": len(archive_dead),
        "n_orphan": len(orphan),
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    print("=" * 78)
    print("CANONICAL-IMPORT AUDIT — STATIC REVIEW ORCHESTRATOR  (_canonical_audit.py)")
    print("=" * 78)
    t_start = time.time()  # (local)

    # --- Step 0: parse canonical constants ---------------------------------
    print(f"\n[0] Parsing {rel(CANON_PY)} ...")
    canon = parse_canonical_constants(CANON_PY)
    canon_names = set(canon.keys())
    print(f"    Canonical constants registered: {len(canon_names)}")

    # --- Step 1: discover scripts ------------------------------------------
    print(f"\n[1] Discovering computation scripts ...")
    comp_scripts = sorted(COMPUTATIONS_DIR.glob(ALL_PY_GLOB))
    arch_scripts: list[Path] = []  # archive directory removed
    # Filter out __init__ and helpers
    comp_scripts = [p for p in comp_scripts if not p.name.startswith("__")]
    print(f"    computations/_shared/: {len(comp_scripts)} .py")
    all_scripts = comp_scripts + arch_scripts

    all_names = {p.name for p in all_scripts}

    # --- Step 2: per-script canonical/hardcode/import scan (1+2+5) ---------
    print(f"\n[2] Per-script static scan (canonical + hardcodes + AST imports) ...")
    t0 = time.time()  # (local)
    scans: list[dict] = []
    for i, p in enumerate(all_scripts, start=1):
        scans.append(scan_script(p, canon_names))
        if i % 200 == 0:
            print(f"    scanned {i}/{len(all_scripts)}")
    print(f"    scanned {len(scans)} scripts in {time.time() - t0:.1f}s")

    script_sha_map = {s["path"]: s["sha256"] for s in scans}

    # --- Step 3: ruff -------------------------------------------------------
    print(f"\n[3] Ruff check (select={RUFF_SELECT}) ...")
    ruff = run_ruff([COMPUTATIONS_DIR])
    if ruff.get("ran"):
        print(f"    total issues: {ruff['total_issues']}   wall: {ruff['wall_seconds']}s")
    else:
        print(f"    ruff did not run: {ruff.get('error', 'unknown')}")

    # --- Step 4: vulture ----------------------------------------------------
    print(f"\n[4] Vulture dead-code (min_confidence={VULTURE_CONF}) ...")
    vulture = run_vulture([COMPUTATIONS_DIR])
    if vulture.get("ran"):
        print(f"    total findings: {vulture['total_dead']}   wall: {vulture['wall_seconds']}s")
    else:
        print(f"    vulture did not run: {vulture.get('error', 'unknown')}")

    # --- Step 5: import graph ----------------------------------------------
    print(f"\n[5] Building local import graph ...")
    import_graph = build_local_import_graph(scans, all_names)
    n_edges = sum(len(v) for v in import_graph["forward"].values())
    print(f"    edges: {n_edges}   scripts with importers: {len(import_graph['reverse'])}")

    # --- Step 6: registry + canonical_constants provenance -----------------
    print(f"\n[6] Cross-referencing registry + canonical_constants provenance ...")
    registry_cites = parse_registry_citations(REGISTRY_MD)
    canon_cites = parse_canonical_provenance_citations(CANON_PY)
    print(f"    scripts cited in registry: {len(registry_cites)}")
    print(f"    scripts cited in canonical_constants.py: {len(canon_cites)}")

    # --- Step 7: SHA-256 ledger --------------------------------------------
    print(f"\n[7] SHA-256 verdict-pin ledger ...")
    ledger = build_sha_ledger(COMPUTATIONS_DIR, script_sha_map)
    print(f"    pinned verdict entries: {ledger['n_pinned_verdicts']}")
    print(f"    matched to current source: {ledger['n_matched']}")
    print(f"    unmatched (stale or foreign hash): {ledger['n_unmatched']}")

    # --- Step 8: knowledge DB cross-ref ------------------------------------
    print(f"\n[8] Knowledge DB cross-reference ({rel(KNOWLEDGE_DB)}) ...")
    mcp = knowledge_db_crossref(KNOWLEDGE_DB)
    if mcp.get("available"):
        mcp_scripts = set(mcp.get("cited_scripts_from_provenance", []))
        print(f"    theorems={mcp['n_theorems']}  gates={mcp['n_gates']}  "
              f"closed={mcp['n_closed_mechanisms']}  prov_rows={mcp['n_data_provenance_rows']}")
        print(f"    scripts cited via data_provenance: {len(mcp_scripts)}")
    else:
        mcp_scripts = set()
        print(f"    knowledge DB unavailable: {mcp.get('note', '')}")

    # --- Step 9: synthesize ------------------------------------------------
    print(f"\n[9] Synthesizing live review sets + priority ranking ...")
    synth = synthesize(
        scans, registry_cites, canon_cites, mcp_scripts,
        import_graph, ruff, vulture,
    )
    print(f"    narrow (cited):   {synth['n_narrow']}")
    print(f"    broad  (S52+):    {synth['n_broad']}")
    print(f"    anchor (re-run):  {synth['n_anchor']}")
    print(f"    orphan:           {synth['n_orphan']}")

    # --- Step 10: write JSON -----------------------------------------------
    report = {
        "tool": "_canonical_audit.py",
        "session": "S80",
        "gate": "S80-CANONICAL-AUDIT",
        "classification": "NON-PHONONIC",
        "generated_timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "wall_seconds_total": round(time.time() - t_start, 1),
        "baseline_counts": {
            "scripts_scanned_total": len(scans),
            "scripts_scanned_computations": len(comp_scripts),
            "canonical_constants": len(canon_names),
            "ruff_total_issues": ruff.get("total_issues", 0),
            "vulture_total_findings": vulture.get("total_dead", 0),
            "registry_citations": len(registry_cites),
            "canonical_provenance_citations": len(canon_cites),
            "mcp_provenance_citations": len(mcp_scripts) if mcp.get("available") else 0,
            "sha_pinned_verdicts": ledger["n_pinned_verdicts"],
            "sha_pin_matches": ledger["n_matched"],
            "sha_pin_unmatches": ledger["n_unmatched"],
            "narrow_live_set": synth["n_narrow"],
            "broad_live_set": synth["n_broad"],
            "anchor_set": synth["n_anchor"],
            "orphan_scripts": synth["n_orphan"],
        },
        "canonical_constants": {
            "path": rel(CANON_PY),
            "n_constants": len(canon_names),
        },
        "registry_citations": sorted(registry_cites),
        "canonical_provenance_citations": sorted(canon_cites),
        "mcp_cross_reference": mcp,
        "ruff_summary": {
            "total_issues": ruff.get("total_issues", 0),
            "ran": ruff.get("ran", False),
            "wall_seconds": ruff.get("wall_seconds", 0),
            "per_file_n_files": len(ruff.get("per_file", {})),
        },
        "vulture_summary": {
            "total_dead": vulture.get("total_dead", 0),
            "ran": vulture.get("ran", False),
            "wall_seconds": vulture.get("wall_seconds", 0),
            "per_file_n_files": len(vulture.get("per_file", {})),
        },
        "sha_ledger_summary": {
            "n_pinned_verdicts": ledger["n_pinned_verdicts"],
            "n_matched": ledger["n_matched"],
            "n_unmatched": ledger["n_unmatched"],
        },
        "narrow_live_set_sample": synth["narrow_live_set"][:50],
        "narrow_live_set": synth["narrow_live_set"],
        "broad_live_set": synth["broad_live_set"],
        "anchor_set": synth["anchor_set"],
        "orphan_scripts": synth["orphan_scripts"],
        "sha_ledger_entries_sample": ledger["ledger_entries"][:25],
        "ruff_per_file": ruff.get("per_file", {}),
        "vulture_per_file": vulture.get("per_file", {}),
        "per_script_scans": scans,
        "import_graph": import_graph,
    }

    REPORT_JSON.write_text(json.dumps(report, indent=2, default=str), encoding="utf-8")
    print(f"\n[10] Wrote report: {rel(REPORT_JSON)}  "
          f"({REPORT_JSON.stat().st_size // 1024} KB)")

    # --- Step 11: write markdown summary -----------------------------------
    md = build_markdown_summary(report, synth, ruff, vulture, ledger, mcp)
    SUMMARY_MD.write_text(md, encoding="utf-8")
    print(f"[11] Wrote summary: {rel(SUMMARY_MD)}")

    # --- Gate verdict ------------------------------------------------------
    print("\n" + "=" * 78)
    print("Gate S80-CANONICAL-AUDIT: PASS")
    print(f"  Scripts scanned total: {len(scans)}")
    print(f"  Narrow live set:       {synth['n_narrow']}  (cluster-review input)")
    print(f"  Broad  live set:       {synth['n_broad']}  (S52+ backdrop)")
    print(f"  Anchor set:            {synth['n_anchor']}  (re-run input)")
    print(f"  Orphan:                {synth['n_orphan']}")
    print(f"  Wall seconds:          {round(time.time() - t_start, 1)}")
    print(
        "  (value=(narrow={},broad={},anchor={},orphan={}), "
        "scheme=STATIC-ANALYSIS, convention=CANONICAL-AUDIT, L_max=N/A)".format(
            synth["n_narrow"], synth["n_broad"], synth["n_anchor"],
            synth["n_orphan"],
        )
    )
    print("=" * 78)

    return 0


# ---------------------------------------------------------------------------
# Markdown summary builder
# ---------------------------------------------------------------------------

def build_markdown_summary(
    report: dict,
    synth: dict,
    ruff: dict,
    vulture: dict,
    ledger: dict,
    mcp: dict,
) -> str:
    b = report["baseline_counts"]
    lines: list[str] = []
    lines.append("# Canonical-Import Audit — Static Review Summary")
    lines.append("")
    lines.append(f"**Generated**: {report['generated_timestamp']}")
    lines.append(f"**Tool**: `computations/_shared/_canonical_audit.py`")
    lines.append(f"**Gate**: {report['gate']} (PASS)")
    lines.append(f"**Wall time**: {report['wall_seconds_total']}s")
    lines.append("")
    lines.append("## 1. Corpus")
    lines.append("")
    lines.append("| Metric | Count |")
    lines.append("|:-------|:------|")
    lines.append(f"| Scripts scanned (total) | {b['scripts_scanned_total']} |")
    lines.append(f"| computations/_shared/ .py | {b['scripts_scanned_computations']} |")
    lines.append(f"| Canonical constants registered | {b['canonical_constants']} |")
    lines.append("")
    lines.append("## 2. Reductions")
    lines.append("")
    lines.append("| Bucket | Count | Notes |")
    lines.append("|:-------|:------|:------|")
    lines.append(f"| **Narrow live set** (cluster-review input) | **{b['narrow_live_set']}** | Cited in canon / registry / MCP / imported by another script |")
    lines.append(f"| Broad live set (S52+ backdrop) | {b['broad_live_set']} | Narrow ∪ session_num ≥ 52 in computations/_shared/ |")
    lines.append(f"| **Anchor set** (re-run input) | **{b['anchor_set']}** | canon / MCP / registry cited only (citation-first priority) |")
    lines.append(f"| Orphan (uncited pre-S52 comp) | {b['orphan_scripts']} | Candidate for archival |")
    lines.append("")
    lines.append("## 3. Lint & Dead-Code")
    lines.append("")
    lines.append("| Check | Total | Files Flagged | Wall |")
    lines.append("|:------|:------|:--------------|:-----|")
    lines.append(f"| Ruff (`{RUFF_SELECT}`) | {ruff.get('total_issues', 0)} | {len(ruff.get('per_file', {}))} | {ruff.get('wall_seconds', 0)}s |")
    lines.append(f"| Vulture (conf ≥ {VULTURE_CONF}%) | {vulture.get('total_dead', 0)} | {len(vulture.get('per_file', {}))} | {vulture.get('wall_seconds', 0)}s |")
    lines.append("")
    lines.append("## 4. SHA-256 Ledger")
    lines.append("")
    lines.append("| Metric | Count |")
    lines.append("|:-------|:------|")
    lines.append(f"| Pinned verdict lines | {ledger['n_pinned_verdicts']} |")
    lines.append(f"| Matched to current source | {ledger['n_matched']} |")
    lines.append(f"| Unmatched (stale or external) | {ledger['n_unmatched']} |")
    lines.append("")
    lines.append("## 5. Knowledge DB Cross-Reference")
    lines.append("")
    if mcp.get("available"):
        lines.append(f"- theorems: {mcp['n_theorems']}")
        lines.append(f"- gates: {mcp['n_gates']}")
        lines.append(f"- closed_mechanisms: {mcp['n_closed_mechanisms']}")
        lines.append(f"- data_provenance rows: {mcp['n_data_provenance_rows']}")
        lines.append(f"- scripts cited via data_provenance: {len(mcp.get('cited_scripts_from_provenance', []))}")
    else:
        lines.append(f"_Knowledge DB unavailable: {mcp.get('note', '')}_")
    lines.append("")
    lines.append("## 6. Anchor Set (Re-Run Input — Top 40 by Citation Impact)")
    lines.append("")
    lines.append("Anchor priority = 100·citation_impact + session_num. Citation impact = 3·canon + 2·registry + 2·mcp + 1·importers.")
    lines.append("")
    lines.append("| # | Script | S | Grade | Canon? | Reg? | MCP? | Imp | Ruff | Vult | HC | UT |")
    lines.append("|:--|:-------|:--|:------|:------:|:----:|:----:|:---:|:----:|:----:|:--:|:--:|")
    for i, r in enumerate(synth["anchor_set"][:40], start=1):
        lines.append(
            f"| {i} | `{r['name']}` | {r['session_num']} | {r['grade']} "
            f"| {'✓' if r['cited_in_canon'] else ''} "
            f"| {'✓' if r['cited_in_registry'] else ''} "
            f"| {'✓' if r['cited_in_mcp'] else ''} "
            f"| {r['n_importers']} "
            f"| {r['n_ruff_issues']} | {r['n_vulture_findings']} "
            f"| {r['n_hardcoded_canonical']} | {r['n_untagged_literals']} |"
        )
    lines.append("")
    lines.append("## 7. Narrow Live Set (Cluster-Review Input — Top 50 by Review Priority)")
    lines.append("")
    lines.append("Review priority = 10·session_num + 3·canon + 2·registry + 2·mcp + 1·importers (recency-first).")
    lines.append("")
    lines.append("| # | Script | S | Grade | Canon? | Reg? | MCP? | Imp | Ruff | Vult | HC | UT |")
    lines.append("|:--|:-------|:--|:------|:------:|:----:|:----:|:---:|:----:|:----:|:--:|:--:|")
    for i, r in enumerate(synth["narrow_live_set"][:50], start=1):
        lines.append(
            f"| {i} | `{r['name']}` | {r['session_num']} | {r['grade']} "
            f"| {'✓' if r['cited_in_canon'] else ''} "
            f"| {'✓' if r['cited_in_registry'] else ''} "
            f"| {'✓' if r['cited_in_mcp'] else ''} "
            f"| {r['n_importers']} "
            f"| {r['n_ruff_issues']} | {r['n_vulture_findings']} "
            f"| {r['n_hardcoded_canonical']} | {r['n_untagged_literals']} |"
        )
    lines.append("")
    lines.append("## 8. Grade Distributions")
    lines.append("")
    lines.append("### Narrow Live Set")
    narrow_grade: Counter = Counter(r["grade"] for r in synth["narrow_live_set"])
    lines.append("| Grade | Count |")
    lines.append("|:------|:------|")
    for grade, n in narrow_grade.most_common():
        lines.append(f"| {grade} | {n} |")
    lines.append("")
    lines.append("### Broad Live Set (S52+ backdrop)")
    broad_grade: Counter = Counter(r["grade"] for r in synth["broad_live_set"])
    lines.append("| Grade | Count |")
    lines.append("|:------|:------|")
    for grade, n in broad_grade.most_common():
        lines.append(f"| {grade} | {n} |")
    lines.append("")
    lines.append("### Anchor Set")
    anchor_grade: Counter = Counter(r["grade"] for r in synth["anchor_set"])
    lines.append("| Grade | Count |")
    lines.append("|:------|:------|")
    for grade, n in anchor_grade.most_common():
        lines.append(f"| {grade} | {n} |")
    lines.append("")
    lines.append("## 9. Cluster-Review Handoff")
    lines.append("")
    lines.append("**Cluster-review input = narrow_live_set** (cited scripts only). The broad set is context-only. Suggested cluster split per the script-review plan §3 cluster table:")
    lines.append("")
    lines.append("| Cluster (agent) | Approx count |")
    lines.append("|:----------------|:------------|")
    lines.append("| Spectral action / heat kernel (`lizzi-spectral-functional-theorist`) | ~60 |")
    lines.append("| BCS / Leggett (`landau-condensed-matter-theorist`) | ~80 |")
    lines.append("| NCG / Chamseddine-Connes (`connes-ncg-theorist`) | ~40 |")
    lines.append("| KK / Jensen deformation (`baptista-spacetime-analyst`) | ~40 |")
    lines.append("| Transit / mode eqn (`transit-dynamics-theorist`) | ~40 |")
    lines.append("| Cosmology / observational (`mack-cosmic-bridge`) | ~30 |")
    lines.append("| Generalist (`gen-physicist`) | ~30 |")
    lines.append("")
    lines.append("## 10. Full Data")
    lines.append("")
    lines.append("- JSON: `computations/_shared/_canonical_audit_report.json`")
    lines.append("- This summary: `computations/_shared/_canonical_audit_summary.md`")
    lines.append("")
    lines.append("Top-level JSON keys:")
    lines.append("- `narrow_live_set` — cluster-review input (cited scripts, recency-sorted)")
    lines.append("- `broad_live_set` — S52+ full backdrop (recency-sorted)")
    lines.append("- `anchor_set` — re-run input (cited, citation-impact-sorted)")
    lines.append("- `orphan_scripts` — computations pre-S52, no citation hit")
    lines.append("- `per_script_scans` — raw per-script record with SHA, hardcodes, imports")
    lines.append("- `ruff_per_file`, `vulture_per_file` — raw lint findings")
    lines.append("- `sha_ledger_entries_sample` — up to 25 pinned-verdict records")
    lines.append("- `import_graph.{forward,reverse}` — intra-project dependency graph")
    lines.append("")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    sys.exit(main())
