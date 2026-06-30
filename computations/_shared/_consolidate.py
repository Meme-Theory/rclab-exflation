#!/usr/bin/env python3
"""
Consolidate 7 cluster review reports into:
  1. _review_summary.md — master grade table + BLOCKER/MAJOR roll-up
  2. _rerun_input.md — actual re-run queue (anchor ∩ BLOCKER/MAJOR)

Reads each cluster review report at the project root.
Grades are extracted by searching for script mentions (`sNNa_*.py`) near grade keywords.
"""

from __future__ import annotations

from canonical_constants import *  # noqa: F401,F403

import json
import re
from collections import defaultdict, Counter
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


PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'COMPUTATIONS_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
CANONICAL_AUDIT_JSON = resolve_script(None, '_canonical_audit_report.json')
OUT_SUMMARY = resolve_script(None, '_review_summary.md')
OUT_RERUN_INPUT = resolve_script(None, '_rerun_input.md')

CLUSTER_REPORTS = {
    "spectral":   resolve_script(None, '_review_cluster_spectral.md'),
    "bcs":        resolve_script(None, '_review_cluster_bcs.md'),
    "ncg":        resolve_script(None, '_review_cluster_ncg.md'),
    "kk":         resolve_script(None, '_review_cluster_kk.md'),
    "transit":    resolve_script(None, '_review_cluster_transit.md'),
    "cosmo":      resolve_script(None, '_review_cluster_cosmo.md'),
    "generalist": resolve_script(None, '_review_cluster_generalist.md'),
}

CLUSTER_AGENT = {
    "spectral":   "lizzi-spectral-functional-theorist",
    "bcs":        "landau-condensed-matter-theorist",
    "ncg":        "connes-ncg-theorist",
    "kk":         "baptista-spacetime-analyst",
    "transit":    "transit-dynamics-theorist",
    "cosmo":      "mack-cosmic-bridge",
    "generalist": "gen-physicist",
}

SCRIPT_RE = re.compile(r"\b(s\d+[a-z]?_[A-Za-z0-9_]+\.py|[A-Za-z0-9_]+\.py)\b")
GRADE_RE = re.compile(r"\b(BLOCKER|MAJOR|MINOR|CLEAN)\b")
# Section header patterns (agents wrote ## 2. BLOCKER findings, ## 3. MAJOR findings, etc.)
SECTION_RE = re.compile(r"^#{2,3}\s+(\d+\.?\s+)?(BLOCKER|MAJOR|MINOR|CLEAN)", re.IGNORECASE | re.MULTILINE)


def extract_grades_from_report(path: Path) -> dict[str, str]:
    """Walk the report. A script is graded X only if it appears in a
    `### N.M \`script.py\`` subheader inside a `## N. X findings` section
    (or in a compact MINOR+CLEAN table with explicit row grade).

    Scripts mentioned only in prose/discussion within a section are NOT graded
    by that section — they are comparison/context references.

    Severity order: BLOCKER > MAJOR > MINOR > CLEAN. Higher severity wins on
    collision.
    """
    if not path.exists():
        return {}

    text = path.read_text(encoding="utf-8", errors="replace")
    severity = {"BLOCKER": 3, "MAJOR": 2, "MINOR": 1, "CLEAN": 0}

    # Find top-level grade sections (## N. X findings)
    section_marks: list[tuple[int, str]] = []
    for m in SECTION_RE.finditer(text):
        grade = m.group(2).upper()
        section_marks.append((m.start(), grade))
    section_marks.sort()

    sections: list[tuple[int, int, str]] = []
    for i, (start, grade) in enumerate(section_marks):
        end = section_marks[i + 1][0] if i + 1 < len(section_marks) else len(text)
        sections.append((start, end, grade))

    # Subheader pattern: ### N.M `script.py` — OR ### `path/script.py` —
    # Allow optional directory prefix (computations/_shared/).
    subheader_re = re.compile(
        r"^#{3,4}\s+(?:\d+\.\d+[a-z]?\s+)?`?"
        r"(?:computations/_shared/)?"
        r"(s\d+[a-z]?_[A-Za-z0-9_]+\.py|[A-Za-z0-9_]+\.py)`?",
        re.MULTILINE,
    )
    # Compact-table row pattern: | `script.py` | GRADE | ...
    row_re = re.compile(
        r"\|\s*`?(?:computations/_shared/)?"
        r"(s\d+[a-z]?_[A-Za-z0-9_]+\.py|[A-Za-z0-9_]+\.py)`?\s*\|"
        r"\s*\*?\*?(BLOCKER|MAJOR|MINOR|CLEAN)\*?\*?\s*\|",
        re.IGNORECASE,
    )

    script_grade: dict[str, str] = {}

    # 1) Subheader grading inside grade-named sections
    for start, end, grade in sections:
        if grade not in severity:
            continue
        chunk = text[start:end]
        for sm in subheader_re.finditer(chunk):
            name = sm.group(1)
            if name not in script_grade or severity[grade] > severity[script_grade[name]]:
                script_grade[name] = grade

    # 2) Compact tables anywhere in the doc. The row format explicitly carries
    # the grade in a cell, so we don't need to be inside a particular section.
    for rm in row_re.finditer(text):
        name = rm.group(1)
        grade = rm.group(2).upper()
        if name not in script_grade or severity[grade] > severity[script_grade[name]]:
            script_grade[name] = grade

    return script_grade


def main() -> int:
    # 1) Parse each cluster report
    cluster_data: dict[str, dict[str, str]] = {}
    for cluster, path in CLUSTER_REPORTS.items():
        cluster_data[cluster] = extract_grades_from_report(path)
        print(f"  {cluster:12s}: {len(cluster_data[cluster]):4d} graded scripts")

    # Cross-reference vs partition expectations
    partition = json.loads(
        (resolve_script(None, '_review_partition.json')).read_text(encoding="utf-8")
    )
    expected_counts = {k: len(v) for k, v in partition["clusters"].items()}

    # 2) Load anchor_set for re-run intersection
    audit = json.loads(CANONICAL_AUDIT_JSON.read_text(encoding="utf-8"))
    anchor_set = audit.get("anchor_set", [])
    anchor_by_name = {a["name"]: a for a in anchor_set}

    # 3) Build master grade table
    lines: list[str] = []
    lines.append("# Cluster Review — Master Consolidation")
    lines.append("")
    lines.append(f"**Generated**: from 7 cluster reports under `_review_cluster_*.md`")
    lines.append(f"**Input**: narrow_live_set (181 scripts) from canonical-import audit")
    lines.append(f"**Status**: **ALL 7 CLUSTERS COMPLETE** (per script-review plan §3)")
    lines.append("")
    lines.append("## 1. Aggregate grade counts")
    lines.append("")
    lines.append("| Cluster | Agent | Expected | Graded | BLOCKER | MAJOR | MINOR | CLEAN |")
    lines.append("|:--------|:------|:---------|:-------|:-------:|:-----:|:-----:|:-----:|")
    totals = Counter()
    grand_graded = 0  # (local)
    grand_expected = 0  # (local)
    for cluster, scripts in cluster_data.items():
        grades = Counter(scripts.values())
        expected = expected_counts.get(cluster, 0)
        n_graded = len(scripts)
        grand_graded += n_graded
        grand_expected += expected
        for g, n in grades.items():
            totals[g] += n
        lines.append(
            f"| {cluster} | {CLUSTER_AGENT[cluster]} | {expected} | {n_graded} "
            f"| {grades.get('BLOCKER', 0)} | {grades.get('MAJOR', 0)} "
            f"| {grades.get('MINOR', 0)} | {grades.get('CLEAN', 0)} |"
        )
    lines.append(
        f"| **TOTAL** |  | **{grand_expected}** | **{grand_graded}** "
        f"| **{totals.get('BLOCKER', 0)}** | **{totals.get('MAJOR', 0)}** "
        f"| **{totals.get('MINOR', 0)}** | **{totals.get('CLEAN', 0)}** |"
    )
    lines.append("")
    lines.append(f"_Note: `Expected` is the partition size; `Graded` is the count of scripts "
                 f"the consolidator extracted a grade for. A shortfall means the cluster's "
                 f"report discussed scripts en-bloc rather than per-script under a graded "
                 f"section — check the original report for those._")
    lines.append("")

    # 4) BLOCKER roll-up
    blockers: list[tuple[str, str]] = []
    majors: list[tuple[str, str]] = []
    for cluster, scripts in cluster_data.items():
        for name, grade in sorted(scripts.items()):
            if grade == "BLOCKER":
                blockers.append((name, cluster))
            elif grade == "MAJOR":
                majors.append((name, cluster))

    lines.append("## 2. BLOCKER scripts")
    lines.append("")
    if not blockers:
        lines.append("_none_")
    else:
        lines.append("| Script | Cluster | Anchor? | Session |")
        lines.append("|:-------|:--------|:-------:|:-------:|")
        for name, cluster in blockers:
            a = anchor_by_name.get(name)
            anchor_mark = "✓" if a else ""
            session = a["session_num"] if a else "?"
            lines.append(f"| `{name}` | {cluster} | {anchor_mark} | {session} |")
    lines.append("")

    lines.append("## 3. MAJOR scripts")
    lines.append("")
    if not majors:
        lines.append("_none_")
    else:
        lines.append("| Script | Cluster | Anchor? | Session |")
        lines.append("|:-------|:--------|:-------:|:-------:|")
        for name, cluster in majors:
            a = anchor_by_name.get(name)
            anchor_mark = "✓" if a else ""
            session = a["session_num"] if a else "?"
            lines.append(f"| `{name}` | {cluster} | {anchor_mark} | {session} |")
    lines.append("")

    # 5) Cluster-report pointers
    lines.append("## 4. Full cluster reports")
    lines.append("")
    for cluster, path in CLUSTER_REPORTS.items():
        rel = path.relative_to(PROJECT_ROOT)
        lines.append(f"- **{cluster}** — `{rel}` (agent: `{CLUSTER_AGENT[cluster]}`)")
    lines.append("")

    OUT_SUMMARY.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"\nWrote {OUT_SUMMARY.name} ({OUT_SUMMARY.stat().st_size // 1024} KB)")

    # 6) Re-run input: anchor_set ∩ (BLOCKER ∪ MAJOR)
    t3_lines: list[str] = []
    t3_lines.append("# Re-Run Input Set — Anchor ∩ (BLOCKER ∪ MAJOR)")
    t3_lines.append("")
    t3_lines.append(f"**Source**: {OUT_SUMMARY.name} + {CANONICAL_AUDIT_JSON.name}")
    t3_lines.append("")
    t3_lines.append("Re-run selection criteria (per script-review plan):")
    t3_lines.append("- Cited in canon PROVENANCE / MCP data_provenance / registry (= anchor_set)")
    t3_lines.append("- AND flagged BLOCKER or MAJOR in cluster review")
    t3_lines.append("")
    t3_input = []
    for name, grade, cluster in (
        [(n, "BLOCKER", c) for n, c in blockers] + [(n, "MAJOR", c) for n, c in majors]
    ):
        a = anchor_by_name.get(name)
        if not a:
            continue
        t3_input.append({
            "name": name,
            "grade": grade,
            "cluster": cluster,
            "session": a.get("session_num", 0),
            "priority_anchor": a.get("priority_anchor", 0),
            "cited_in_canon": a.get("cited_in_canon", False),
            "cited_in_mcp": a.get("cited_in_mcp", False),
            "cited_in_registry": a.get("cited_in_registry", False),
            "path": a.get("path", ""),
        })

    t3_input.sort(key=lambda r: (
        0 if r["grade"] == "BLOCKER" else 1,
        -r["priority_anchor"],
        r["name"],
    ))

    t3_lines.append(f"## Queue ({len(t3_input)} scripts)")
    t3_lines.append("")
    t3_lines.append("| # | Script | Grade | Cluster | S | pa | canon | mcp | reg |")
    t3_lines.append("|:-:|:-------|:------|:--------|:-:|:--:|:-----:|:---:|:---:|")
    for i, r in enumerate(t3_input, 1):
        t3_lines.append(
            f"| {i} | `{r['name']}` | {r['grade']} | {r['cluster']} | {r['session']} "
            f"| {r['priority_anchor']} "
            f"| {'✓' if r['cited_in_canon'] else ''} "
            f"| {'✓' if r['cited_in_mcp'] else ''} "
            f"| {'✓' if r['cited_in_registry'] else ''} |"
        )
    t3_lines.append("")
    t3_lines.append("## Non-anchor BLOCKER/MAJOR (audit-only, not re-run)")
    t3_lines.append("")
    non_anchor = []
    for name, cluster in blockers + majors:
        if name not in anchor_by_name:
            grade = "BLOCKER" if (name, cluster) in blockers else "MAJOR"
            non_anchor.append((name, grade, cluster))
    if not non_anchor:
        t3_lines.append("_none_")
    else:
        t3_lines.append("| Script | Grade | Cluster |")
        t3_lines.append("|:-------|:------|:--------|")
        for name, grade, cluster in non_anchor:
            t3_lines.append(f"| `{name}` | {grade} | {cluster} |")
    t3_lines.append("")
    t3_lines.append("## Next step for the re-run runner")
    t3_lines.append("")
    t3_lines.append("1. Read `_review_prep.md` for the per-anchor MCP "
                    "baseline queries + proposed PRU blocks (prep already done for top 40 anchors).")
    t3_lines.append("2. Fill the PRU block per anchor using the template at "
                    "`.claude/templates/pru-pre-registration-template.md`.")
    t3_lines.append("3. For each BLOCKER: fix the source-code issue FIRST, then re-run under PRU pins.")
    t3_lines.append("4. For each MAJOR: canonical-migrate FIRST (swap hardcode for `from canonical_constants import X`), "
                    "then re-run under PRU pins + GPU path.")
    t3_lines.append("5. Compare reproduced value to MCP-registered. On match: `update_constant(...)`. "
                    "On mismatch: human adjudication per the script-review plan.")
    t3_lines.append("")
    OUT_RERUN_INPUT.write_text("\n".join(t3_lines) + "\n", encoding="utf-8")
    print(f"Wrote {OUT_RERUN_INPUT.name} ({OUT_RERUN_INPUT.stat().st_size // 1024} KB)")
    print(f"\n  Re-run queue (anchor ∩ B/M): {len(t3_input)} scripts")
    print(f"  Non-anchor B/M (audit-only):  {len(non_anchor)} scripts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
