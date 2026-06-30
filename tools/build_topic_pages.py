#!/usr/bin/env python3
"""
Topic Pages Builder — Class-Portrait Markdown for ``summary/topics/``
=====================================================================

Created: Session 86 (2026-04-26)
Purpose: Walk each class in ``computations/_shared/canonical_classes.py`` (via
``knowledge.db``), assemble member tables + cross-class memberships +
hierarchy, and emit a markdown topic page per class to
``summary/topics/<class_id_lower>.md``. Plus an index page listing all topics.

Design
------
- Reads knowledge.db (tables: classes, class_edges) — assumes /weave --db-sync
  has already run. If the tables don't exist, prints a graceful error and exits.
- Imports canonical_constants via importlib to resolve member values
  (alias chains + Pass 3 derived expressions evaluate natively in Python).
- Style: matches sessions/framework/registry/_registry-template.md conventions
  (YAML frontmatter, bold-key-colon-value metadata, summary table,
  per-entry detail, change log).

Output
------
- summary/topics/index.md          — class index
- summary/topics/<id_lower>.md     — one per class (9 in S86)

Run
---
    "phonon-exflation-sim/.venv312/Scripts/python.exe" tools/build_topic_pages.py
    "phonon-exflation-sim/.venv312/Scripts/python.exe" tools/build_topic_pages.py --class GR
    "phonon-exflation-sim/.venv312/Scripts/python.exe" tools/build_topic_pages.py --dry-run
"""

from __future__ import annotations

import argparse
import importlib.util
import math
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

# -----------------------------------------------------------------------------
# Paths
# -----------------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = PROJECT_ROOT / "tools" / "knowledge.db"
CC_PATH = PROJECT_ROOT / "computations" / "_shared" / "canonical_constants.py"
COMPUTATIONS_DIR = PROJECT_ROOT / "computations" / "_shared"
TOPICS_DIR = PROJECT_ROOT / "summary" / "topics"
VIZ_INDEX_REL = "tools/viz/console/index.html"  # for footer deep-link


# -----------------------------------------------------------------------------
# Constant value loading (importlib — gets alias chains + Pass 3 for free)
# -----------------------------------------------------------------------------

def load_canonical_constants() -> dict:
    """Import canonical_constants.py and return {name: value} for every
    numeric attribute. Uses importlib so alias chains (M_KK = M_KK_gravity)
    and derived expressions (alpha_s_inflation_framework = n_s_canon**2 - 1)
    resolve natively in Python — no regex parser needed.
    """
    if not CC_PATH.exists():
        return {}
    # Inject COMPUTATIONS_DIR into sys.path so canonical_constants's own imports
    # (and any sister modules like canonical_classes) can resolve.
    computations_str = str(COMPUTATIONS_DIR)
    path_added = False
    if computations_str not in sys.path:
        sys.path.insert(0, computations_str)
        path_added = True
    try:
        spec = importlib.util.spec_from_file_location("canonical_constants", CC_PATH)
        if spec is None or spec.loader is None:
            return {}
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        out = {}
        for name in dir(mod):
            if name.startswith("_"):
                continue
            val = getattr(mod, name)
            if isinstance(val, (int, float)):
                # Filter NaN/inf for clean rendering
                if isinstance(val, float) and not math.isfinite(val):
                    continue
                out[name] = float(val) if isinstance(val, float) else val
        return out
    except Exception as e:
        print(f"  WARN: canonical_constants import failed: {e}")
        return {}
    finally:
        if path_added:
            sys.path.remove(computations_str)


def fmt_value(val) -> str:
    """Format a numeric value for tooltip-friendly markdown display."""
    if val is None:
        return "—"
    if isinstance(val, bool):
        return str(val)
    try:
        f = float(val)
    except (TypeError, ValueError):
        return str(val)
    if not math.isfinite(f):
        return str(val)
    a = abs(f)
    if a == 0:
        return "0"
    if a >= 1e5 or a < 1e-3:
        return f"{f:.4g}"
    return f"{f:.4g}"


# -----------------------------------------------------------------------------
# DB queries
# -----------------------------------------------------------------------------

# Role display order — matches MCP server.py's CASE statement and views.js
# legend ordering. Drives both the summary-table grouping and per-role section
# emission below.
ROLE_ORDER = [
    "PRIMARY",
    "PRECONDITION",
    "EMERGENT_FROM",
    "CONSEQUENCE",
    "OBSERVABLE_OUTPUT",
    "DERIVED",
    "RELATED",
]

ROLE_GLOSS = {
    "PRIMARY":           "defining constants — the class cannot be described without them",
    "PRECONDITION":      "substrate / context properties the class consumes but does not produce",
    "EMERGENT_FROM":     "constants that emerge from PRIMARY members via substrate-level computation (regulators, schemes, multi-route consistency) — NOT algebraic one-liners",
    "CONSEQUENCE":       "produced by the class's process; becomes a downstream-class PRIMARY",
    "OBSERVABLE_OUTPUT": "external-cosmology testable predictions — the class's headline observables",
    "DERIVED":           "algebraic / definitional consequences — unit conversions, ratios of PRIMARY members",
    "RELATED":           "kindred observables from sister classes, or boundary conditions; not native to this class",
}


def fetch_classes(con: sqlite3.Connection) -> list[dict]:
    cur = con.cursor()
    rows = cur.execute(
        "SELECT id, name, tier, parent_id, description, seed_session "
        "FROM classes ORDER BY tier, id"
    ).fetchall()
    return [
        {"id": r[0], "name": r[1], "tier": r[2], "parent_id": r[3],
         "description": r[4], "seed_session": r[5]}
        for r in rows
    ]


def fetch_members(con: sqlite3.Connection, class_id: str) -> list[dict]:
    """Return contains-edges for class_id as list of {tgt, role, comment}."""
    cur = con.cursor()
    case_sql = " ".join(
        f"WHEN '{r}' THEN {i}" for i, r in enumerate(ROLE_ORDER)
    )
    rows = cur.execute(
        f"SELECT tgt, role, comment FROM class_edges "
        f"WHERE src = ? AND type = 'contains' AND tgt_type = 'constants' "
        f"ORDER BY CASE role {case_sql} ELSE {len(ROLE_ORDER)} END, tgt",
        (class_id,),
    ).fetchall()
    return [{"tgt": r[0], "role": r[1], "comment": r[2]} for r in rows]


def fetch_subclasses(con: sqlite3.Connection, class_id: str) -> list[dict]:
    cur = con.cursor()
    rows = cur.execute(
        "SELECT id, name FROM classes WHERE parent_id = ? ORDER BY id",
        (class_id,),
    ).fetchall()
    return [{"id": r[0], "name": r[1]} for r in rows]


def fetch_constant_classes(con: sqlite3.Connection, constant_id: str) -> list[dict]:
    """For cross-class section: which OTHER classes also contain this constant?"""
    cur = con.cursor()
    rows = cur.execute(
        "SELECT src, role FROM class_edges "
        "WHERE type = 'contains' AND tgt_type = 'constants' AND tgt = ?",
        (constant_id,),
    ).fetchall()
    return [{"class": r[0], "role": r[1]} for r in rows]


# -----------------------------------------------------------------------------
# Markdown rendering
# -----------------------------------------------------------------------------

def render_topic_page(cls: dict, members: list[dict], subclasses: list[dict],
                      parent: dict | None, constants: dict,
                      all_classes: list[dict],
                      cross_class_index: dict[str, list[dict]]) -> str:
    """Build the markdown body for a single class topic page."""
    cid = cls["id"]
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    # Group members by role
    by_role: dict[str, list[dict]] = {r: [] for r in ROLE_ORDER}
    for m in members:
        role = m.get("role") or "UNKNOWN"
        by_role.setdefault(role, []).append(m)

    lines: list[str] = []

    # 1. YAML frontmatter (matches _registry-template.md)
    lines.append("---")
    lines.append("type: topic-page")
    lines.append("ingested-by: /weave --update")
    lines.append(f"class-id: {cid}")
    lines.append(f"class-tier: {cls.get('tier', 0)}")
    lines.append(f"generated: {today}")
    lines.append("---")
    lines.append("")

    # 2. Title + blockquote intro
    lines.append(f"# Topic — {cls.get('name') or cid}")
    lines.append("")
    lines.append(
        "> Auto-generated from `computations/_shared/canonical_classes.py` via "
        "`tools/build_topic_pages.py`. Edits to this file will be overwritten "
        "by the next `/weave --update`. To change the content, edit the class "
        "definition or its CLASS_EDGES entries in canonical_classes.py."
    )
    lines.append("")

    # 3. Metadata block (bold-key-colon-value style — matches template)
    lines.append(f"**Class ID**: `{cid}`  ")
    lines.append(f"**Tier**: {cls.get('tier', 0)} "
                 f"({'root' if cls.get('tier', 0) == 0 else 'sub-class'})  ")
    parent_link = (
        f"[{parent['id']}](./{parent['id'].lower()}.md) ({parent['name']})"
        if parent else "(root)"
    )
    lines.append(f"**Parent class**: {parent_link}  ")
    lines.append(f"**Seed session**: `{cls.get('seed_session') or '?'}`  ")
    lines.append(f"**Member count**: {len(members)} "
                 f"({len(subclasses)} sub-classes)")
    lines.append("")

    # 4. Description (full text)
    lines.append("## Scope")
    lines.append("")
    desc = (cls.get("description") or "").strip()
    if desc:
        lines.append(desc)
    else:
        lines.append("_(no description provided)_")
    lines.append("")

    # 5. Summary table — members ordered by role per ROLE_ORDER
    lines.append(f"## Members ({len(members)})")
    lines.append("")
    if members:
        lines.append("| Constant | Role | Value | Comment |")
        lines.append("|:---------|:-----|:------|:--------|")
        for r in ROLE_ORDER:
            for m in by_role.get(r, []):
                tgt = m["tgt"]
                role = m.get("role") or ""
                val = constants.get(tgt)
                val_str = fmt_value(val) if val is not None else "_(not parsed)_"
                comment = (m.get("comment") or "").replace("|", "/").replace("\n", " ")
                lines.append(f"| `{tgt}` | {role} | {val_str} | {comment[:80]} |")
    else:
        lines.append(
            "_(no constant members — see sub-classes below for nested membership)_"
        )
    lines.append("")

    # 6. Per-role detail sections — only emit roles that actually have members
    lines.append("## By role")
    lines.append("")
    any_role_emitted = False
    for r in ROLE_ORDER:
        entries = by_role.get(r, [])
        if not entries:
            continue
        any_role_emitted = True
        lines.append(f"### {r} ({len(entries)})")
        lines.append("")
        lines.append(f"_{ROLE_GLOSS.get(r, '')}_")
        lines.append("")
        for m in entries:
            tgt = m["tgt"]
            comment = (m.get("comment") or "").replace("\n", " ")
            val = constants.get(tgt)
            val_str = fmt_value(val) if val is not None else "(not parsed)"
            other_classes = [
                cc for cc in cross_class_index.get(tgt, [])
                if cc["class"] != cid
            ]
            line = f"- **`{tgt}`** = {val_str}"
            if comment:
                line += f" — {comment}"
            lines.append(line)
            if other_classes:
                others_str = ", ".join(
                    f"[{cc['class']}](./{cc['class'].lower()}.md) ({cc['role']})"
                    for cc in other_classes
                )
                lines.append(f"  - _Also in: {others_str}_")
        lines.append("")
    if not any_role_emitted:
        lines.append("_(no role-organized members — class may be a parent only)_")
        lines.append("")

    # 7. Sub-classes (replaces template's Migration notes section)
    if subclasses:
        lines.append(f"## Sub-classes ({len(subclasses)})")
        lines.append("")
        for sc in subclasses:
            sc_id = sc["id"]
            lines.append(
                f"- [`{sc_id}`](./{sc_id.lower()}.md) — {sc['name']}"
            )
        lines.append("")

    # 8. Consumer gates placeholder (matches _registry-template.md structure)
    lines.append("## Consumer gates")
    lines.append("")
    lines.append(
        "_(no consumer gates yet — topic pages do not currently carry "
        "Input-SHA pins. When gates start citing topic pages as authoritative "
        "data, list them here.)_"
    )
    lines.append("")

    # 9. Change log (matches template)
    lines.append("## Change log")
    lines.append("")
    lines.append("| Date | Session | Change | Author |")
    lines.append("|:-----|:--------|:-------|:-------|")
    lines.append(
        f"| {today} | S86-W*-build_topic_pages | "
        f"auto-generated from canonical_classes.py | "
        f"build_topic_pages.py |"
    )
    lines.append("")

    # 10. Footer — visualizer deep-link
    lines.append("---")
    lines.append("")
    lines.append(
        f"**Visualizer**: open `{VIZ_INDEX_REL}` and select `{cid}` from the "
        f"`▣ classes` dropdown in the Connections tab to see the radial "
        f"member graph (color-coded by role)."
    )
    lines.append("")

    return "\n".join(lines)


def render_index(classes: list[dict], member_counts: dict[str, int]) -> str:
    """Build summary/topics/index.md — table of all topic pages."""
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    lines: list[str] = []
    lines.append("---")
    lines.append("type: topic-page-index")
    lines.append("ingested-by: /weave --update")
    lines.append(f"generated: {today}")
    lines.append("---")
    lines.append("")
    lines.append("# Topic Pages — Index")
    lines.append("")
    lines.append(
        "> Auto-generated index of class topic pages. One row per class in "
        "`computations/_shared/canonical_classes.py`. Each topic page is itself "
        "auto-generated; edits land in the source module, not here."
    )
    lines.append("")
    lines.append(
        f"**Generator**: `tools/build_topic_pages.py`  "
    )
    lines.append(
        f"**Source**: `computations/_shared/canonical_classes.py`  "
    )
    lines.append(f"**Class count**: {len(classes)}")
    lines.append("")
    lines.append("## Classes")
    lines.append("")
    lines.append("| Class | Topic page | Tier | Parent | Members | Seed session |")
    lines.append("|:------|:-----------|-----:|:-------|--------:|:-------------|")
    for c in classes:
        cid = c["id"]
        tier = c.get("tier", 0)
        parent = c.get("parent_id")
        parent_str = (
            f"[{parent}](./{parent.lower()}.md)" if parent else "_(root)_"
        )
        link = f"[{c.get('name') or cid}](./{cid.lower()}.md)"
        n = member_counts.get(cid, 0)
        seed = c.get("seed_session") or "?"
        # Indent sub-classes for visual hierarchy
        prefix = "└─ " * tier if tier > 0 else ""
        lines.append(
            f"| {prefix}`{cid}` | {link} | {tier} | {parent_str} | {n} | `{seed}` |"
        )
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(
        f"**Visualizer**: open `{VIZ_INDEX_REL}` and pick a class from the "
        f"`▣ classes` dropdown in the Connections tab."
    )
    lines.append("")
    return "\n".join(lines)


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Build summary/topics/<class>.md pages from knowledge.db classes."
    )
    parser.add_argument(
        "--class", dest="cls_filter", type=str, default=None,
        help="Only build the topic page for this class id (default: all)."
    )
    parser.add_argument(
        "--output", type=Path, default=TOPICS_DIR,
        help=f"Output directory (default: {TOPICS_DIR})."
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Render to stdout instead of writing files."
    )
    args = parser.parse_args()

    if not DB_PATH.exists():
        print(
            f"[build_topic_pages] ERROR: {DB_PATH} missing. Run /weave --db-sync first.",
            file=sys.stderr,
        )
        sys.exit(1)

    # Load constant values via importlib
    constants = load_canonical_constants()
    if not constants:
        print(
            "[build_topic_pages] WARN: canonical_constants did not yield any "
            "values; member rows will show '(not parsed)'.",
            file=sys.stderr,
        )

    con = sqlite3.connect(str(DB_PATH))
    try:
        # Defensive: classes / class_edges may be absent on pre-S86 DBs.
        try:
            classes = fetch_classes(con)
        except sqlite3.OperationalError:
            print(
                "[build_topic_pages] ERROR: knowledge.db has no `classes` "
                "table. This DB predates S86. Rebuild with /weave --db-sync "
                "after extracting classes.",
                file=sys.stderr,
            )
            sys.exit(1)

        if not classes:
            print("[build_topic_pages] No classes found — nothing to build.")
            return

        # Apply --class filter if any
        target_classes = (
            [c for c in classes if c["id"] == args.cls_filter]
            if args.cls_filter else classes
        )
        if args.cls_filter and not target_classes:
            print(
                f"[build_topic_pages] ERROR: class '{args.cls_filter}' not found. "
                f"Available: {', '.join(c['id'] for c in classes)}",
                file=sys.stderr,
            )
            sys.exit(1)

        # Build cross-class index once (constant_id -> [{class, role}, ...])
        cross_class_index: dict[str, list[dict]] = {}
        for c in classes:
            for m in fetch_members(con, c["id"]):
                cross_class_index.setdefault(m["tgt"], []).append(
                    {"class": c["id"], "role": m["role"]}
                )

        # Class-id -> metadata map (for parent lookup)
        class_by_id = {c["id"]: c for c in classes}

        # Compute total member counts per class (for the index)
        member_counts: dict[str, int] = {
            c["id"]: len(fetch_members(con, c["id"])) for c in classes
        }

        # Ensure output dir exists (unless dry-run)
        if not args.dry_run:
            args.output.mkdir(parents=True, exist_ok=True)

        # Render each class's topic page
        written: list[Path] = []
        for cls in target_classes:
            members = fetch_members(con, cls["id"])
            subclasses = fetch_subclasses(con, cls["id"])
            parent = (
                class_by_id.get(cls["parent_id"]) if cls.get("parent_id") else None
            )
            body = render_topic_page(
                cls, members, subclasses, parent,
                constants, classes, cross_class_index,
            )
            out_path = args.output / f"{cls['id'].lower()}.md"
            if args.dry_run:
                print(f"--- {out_path} ---")
                print(body)
                print()
            else:
                out_path.write_text(body, encoding="utf-8")
                written.append(out_path)

        # Build and write index (only when full rebuild + not dry-run)
        if not args.cls_filter and not args.dry_run:
            index_body = render_index(classes, member_counts)
            index_path = args.output / "index.md"
            index_path.write_text(index_body, encoding="utf-8")
            written.append(index_path)

        # Report
        if args.dry_run:
            print(
                f"[build_topic_pages] dry-run: would write "
                f"{len(target_classes)} topic page(s)."
            )
        else:
            total_size = sum(p.stat().st_size for p in written)
            print(
                f"[build_topic_pages] wrote {len(written)} file(s) to "
                f"{args.output} ({total_size:,} bytes)"
            )
            for p in written:
                print(f"  {p.relative_to(PROJECT_ROOT)}")
    finally:
        con.close()


if __name__ == "__main__":
    main()
