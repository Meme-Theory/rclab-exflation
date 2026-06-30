#!/usr/bin/env python3
"""
Harvest relation edges from session-final summaries (post-hoc archive pass).

Companion to `computations/_shared/_harvest_edges.py` — that one walks
T3 verdict files; THIS one walks `summary/Archives/*.md` and
`summary/session-*-final.md` to retro-fit edges for sessions whose
edge-file never landed.

Targeted markdown patterns (from a structural read of session-35-final.md):
  1. Gate verdict tables (`## II. Gate Verdicts Summary` and similar):
     `| GATE-ID | **PASS** | key-number | agent |`
     -> `[EDGE:reproduces] gates:GATE-ID -> sessions:N`
     -> `[EDGE:reproduces] gates:GATE-ID -> constants:NAME` (when key-number
        contains a canonical-constant name)
  2. Mechanism Closures (`### N. Name (GATE-ID)` subsection headings):
     -> `[EDGE:closed_by] open_channels:Mechanism_slug -> gates:GATE-ID`
  3. Mechanism chain cross-checks (cells like "Confirmed by GATE-X"):
     -> `[EDGE:cross_validates] gates:LINK_GATE -> gates:CROSS_GATE`
  4. Files Produced (`| s35_thouless_multiband | NEFF-THOULESS-35 | ... |`):
     -> `[EDGE:feeds_into] data_provenance:script.py -> gates:GATE-ID`

Discipline (per `_harvest_edges.py:12-14`): prefer miss over false-positive.
Each pattern requires both regex AND well-defined source/target pair.

Gate ID for this tool: ARCHIVE-EDGE-HARVEST (NON-PHONONIC, infrastructure).
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# This file lives at tools/archive/, two levels below the project root.
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
COMPUTATIONS_DIR = PROJECT_ROOT / "computations"
SUMMARY_DIR = PROJECT_ROOT / "summary"
SUMMARY_ARCHIVE_DIR = SUMMARY_DIR / "Archives"
CC_PATH = COMPUTATIONS_DIR / "_shared" / "canonical_constants.py"


# ----------------------------------------------------------------------------
# Vocabulary loaders
# ----------------------------------------------------------------------------

def load_canonical_names() -> set[str]:
    """Load canonical-constant names from canonical_constants.py.

    Imports the module and harvests dir(CC), then filters out
    re-exported modules / functions / classes / built-ins so that names
    like `np`, `sys`, `warnings`, `warn_stale` do not pollute the
    constant vocabulary. The leak was silent for table-cell harvesters
    (table cells don't reference Python module names) but leaked badly
    for any source-text harvester downstream.
    """
    import inspect
    import types
    if not CC_PATH.exists():
        return set()
    sys.path.insert(0, str(COMPUTATIONS_DIR / "_shared"))
    try:
        import canonical_constants as CC  # noqa: WPS433
    except Exception:                         # noqa: BLE001
        return set()
    out: set[str] = set()
    for name in dir(CC):
        if name.startswith("_") or not name.isidentifier():
            continue
        obj = getattr(CC, name)
        if isinstance(obj, types.ModuleType):
            continue
        if (inspect.isfunction(obj) or inspect.isclass(obj)
                or inspect.isbuiltin(obj) or inspect.ismethod(obj)):
            continue
        out.add(name)
    return out


# ----------------------------------------------------------------------------
# Strict constant-name regex (copied verbatim from
# `_harvest_edges.py:54-62`).  Two-stage filter: this regex shape AND
# the loaded canonical-name vocabulary must both accept a token.
# ----------------------------------------------------------------------------

_CONSTANT_NAME_STRICT = re.compile(
    r"^(?:"
    r"[A-Z][A-Za-z0-9_]*_[A-Za-z0-9_]+"
    r"|phi_\w+|m_[A-Za-z0-9]+|M_[A-Za-z0-9]+|Delta_\w+|alpha_\w+"
    r"|beta_\w+|gamma_\w+|theta_\w+|omega_\w+|Omega_\w+|tau_\w+"
    r"|H_\d+|kappa_\w+|rho_\w+|Vol_\w+|T_\w+|J_\w+|S_\w+|E_\w+"
    r"|[A-Za-z]+_[A-Za-z0-9_]+\d|[A-Za-z]+\d[A-Za-z0-9_]*"
    r")$"
)

# A gate-ID shape covers legacy (`NEFF-THOULESS-35`, `V-1`, `B-30b`,
# `OoO-3a`), T3 (`T3-S69-BCS-SURFACE-GRAVITY`), and lowercase-suffix
# (`P-30conv`, `RGE-A`) forms.  Lowercase letters are allowed because S30+
# adopted lowercase wave/sub-session suffixes (`B-30b`, `B-30Aa`).
RE_GATE_ID = re.compile(r"^(?:T3-)?[A-Z][A-Za-z0-9]*(?:-[A-Za-z0-9]+)+$")
RE_LOOSE_GATE_ID = re.compile(r"\b((?:T3-)?[A-Z][A-Za-z0-9]*(?:-[A-Za-z0-9]+){1,5})\b")

# Verdict vocabulary observed across S20-S85 summaries.  Some sessions use
# "FIRES / DOES NOT FIRE" terminology (Hard-Close gates, S30 style); others
# use PASS/FAIL/INFO (S35+ style).  All of these mark a gate-row in a table.
VERDICT_VOCAB = {
    "PASS", "FAIL", "INFO", "NEUTRAL", "DIAGNOSTIC", "CLOSED", "INFORMATIVE",
    "FIRES", "DOES NOT FIRE", "DOES-NOT-FIRE", "CANNOT FIRE", "CANNOT-FIRE",
    "MOOT", "REFRAMED", "FAIL/REFRAMED", "NOT COMPUTED", "NOT-COMPUTED",
    "UNCOMPUTED", "TRIVIAL", "QUEUED", "DEFERRED",
}
# Pre-compute uppercase forms for fast comparison
VERDICT_VOCAB_UC = {v.upper() for v in VERDICT_VOCAB}
RE_PCT_VERDICT = re.compile(r"^\d+%$")            # e.g. "32%" sagan-style

# Filename in `summary/Archives/session-NN[a-z]?-final.md` (or quicklook).
RE_SUMMARY_FILE = re.compile(
    r"^session-(?P<sess>\d+[a-z]?)-(?:final|quicklook|synthesis)\.md$",
    re.IGNORECASE,
)


# ----------------------------------------------------------------------------
# Markdown helpers
# ----------------------------------------------------------------------------

def split_table_blocks(text: str) -> list[tuple[str, str]]:
    """Return [(heading, body), ...] for every '## ' section.

    The first chunk before any '## ' becomes ('', preamble).
    """
    blocks: list[tuple[str, str]] = []
    cur_header = ""
    cur_body: list[str] = []
    for line in text.splitlines(keepends=True):
        if line.startswith("## "):
            blocks.append((cur_header, "".join(cur_body)))
            cur_header = line[3:].strip()
            cur_body = []
        else:
            cur_body.append(line)
    blocks.append((cur_header, "".join(cur_body)))
    return blocks


def parse_markdown_table_rows(body: str) -> list[list[str]]:
    """Return list of cell-lists for every data row in any markdown table
    appearing in `body`. Skips header and divider rows.
    """
    out: list[list[str]] = []
    in_table = False
    seen_divider = False
    for raw in body.splitlines():
        line = raw.strip()
        if not line.startswith("|"):
            in_table = False
            seen_divider = False
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not in_table:
            in_table = True
            seen_divider = False
            continue                               # header row
        if not seen_divider:
            # Divider row: cells like ":--", "----", ":--:", etc.
            if all(re.match(r"^:?-+:?$", c) for c in cells if c):
                seen_divider = True
                continue
        out.append(cells)
    return out


def strip_md_emphasis(s: str) -> str:
    """Remove markdown bold/italic/backtick wrappers from a cell."""
    return re.sub(r"[`*_]", "", s).strip()


# ----------------------------------------------------------------------------
# Edge-emission helper (mirrors _harvest_edges.py)
# ----------------------------------------------------------------------------

class EdgeBuf:
    def __init__(self) -> None:
        self.edges: list[dict] = []

    def add(self, etype: str, src_type: str, src_id: str,
            tgt_type: str, tgt_id: str, comment: str) -> None:
        if not src_id or not tgt_id:
            return
        if src_type == tgt_type and src_id == tgt_id:
            return
        self.edges.append({
            "type": etype,
            "src_type": src_type, "src_id": src_id,
            "tgt_type": tgt_type, "tgt_id": tgt_id,
            "comment": comment[:200],
        })

    def dedup(self) -> list[dict]:
        seen: set[tuple] = set()
        out: list[dict] = []
        for e in self.edges:
            key = (e["type"], e["src_type"], e["src_id"].lower(),
                   e["tgt_type"], e["tgt_id"].lower())
            if key in seen:
                continue
            seen.add(key)
            out.append(e)
        return out


# ----------------------------------------------------------------------------
# Session-final extractor
# ----------------------------------------------------------------------------

def extract_session_id(name: str) -> str | None:
    m = RE_SUMMARY_FILE.match(name)
    if m:
        # Take just the digit-prefix; strip the optional sub-letter for the
        # session-number used as an edge target. Sub-letter sessions still
        # get their own output file.
        sess = m.group("sess")
        m2 = re.match(r"^(\d+)", sess)
        return m2.group(1) if m2 else sess
    return None


def harvest_one(path: Path, canonical_names: set[str]) -> list[dict]:
    text = path.read_text(encoding="utf-8", errors="replace")
    sess = extract_session_id(path.name)
    if not sess:
        return []
    buf = EdgeBuf()

    blocks = split_table_blocks(text)

    # ----------- Pattern 1+3+α+γ+ζ: Gate verdict tables (multi-format) -----------
    # Five table layouts produce edges:
    #   Pattern 1 (S30/S35-style): col-0 = gate-ID, col-N = verdict
    #   Pattern α (S32/S42-style): col-0 = row#, col-1/2 = gate-ID, col-N = verdict
    #   Pattern γ (S46-quicklook): col-0 = verdict, col-2 = comma-list of gate-IDs
    #   Pattern ζ (S65-style):     col-0 = gate-ID in Constraint-Map header, NO verdict cell
    #   Pattern 3:                 cross-validation cells in any layout
    #
    # The unified scanner: find FIRST gate-ID-shaped cell (any column) and
    # FIRST verdict-shaped cell (any column).  Dispatch by their relative
    # positions and the section header.
    ZETA_HEADERS = ("constraint", "theorem", "closure", "structural")
    for header, body in blocks:
        header_lc = header.lower()
        for row in parse_markdown_table_rows(body):
            if len(row) < 2:
                continue
            # Strip parenthetical annotations + emphasis from each cell
            cells_clean = [
                re.sub(r"\s*\([^)]*\)\s*", "", strip_md_emphasis(c)).strip()
                for c in row
            ]
            cells_uc = [
                re.sub(r"\s+", " ", c.upper()) for c in cells_clean
            ]

            # Locate first gate-ID and first verdict cell (any column)
            gid_idx = -1
            gid = ""
            for i, c in enumerate(cells_clean):
                if RE_GATE_ID.match(c):
                    gid_idx = i
                    gid = c
                    break

            verdict_idx = -1
            verdict_text = ""
            for i, cu in enumerate(cells_uc):
                if cu in VERDICT_VOCAB_UC or RE_PCT_VERDICT.match(cu):
                    verdict_idx = i
                    verdict_text = cu
                    break
                first_chunk = cu.split(",", 1)[0].split(";", 1)[0].strip()
                if first_chunk in VERDICT_VOCAB_UC:
                    verdict_idx = i
                    verdict_text = first_chunk
                    break

            # Pattern γ: col-0 verdict, gate-IDs in any subsequent cell as
            # comma-separated tokens.  Only emit when col-0 is verdict-shaped
            # AND col-2 (or any later cell) contains ≥1 gate-ID-shaped token.
            if verdict_idx == 0:
                for cell in row[1:]:
                    cell_str = strip_md_emphasis(cell)
                    for tok in re.findall(
                        r"(?:T3-)?[A-Z][A-Za-z0-9]*(?:-[A-Za-z0-9]+)+", cell_str
                    ):
                        if RE_GATE_ID.match(tok):
                            buf.add(
                                "reproduces", "gates", tok,
                                "sessions", sess,
                                f"archive-harvested: γ-pattern {verdict_text} "
                                f"verdict-list in S{sess}",
                            )
                continue

            # Pattern 1 / α: gate-ID present somewhere AND verdict elsewhere.
            if gid_idx >= 0 and verdict_idx >= 0 and gid_idx != verdict_idx:
                buf.add(
                    "reproduces", "gates", gid, "sessions", sess,
                    f"archive-harvested: {verdict_text} verdict in S{sess} table",
                )
                # Edge B: gate -> constant from ANY cell of the row mentioning
                # a canonical-constant name token (key-number cell preferred,
                # but constants also appear in mechanism-prose, source, and
                # surviving-space cells).  buf.dedup() collapses duplicate
                # (gate, constant) pairs across cells.
                for cell in row:
                    for tok in re.findall(r"[A-Za-z_][A-Za-z0-9_]+", cell):
                        if (tok in canonical_names
                                and _CONSTANT_NAME_STRICT.match(tok)):
                            buf.add(
                                "reproduces", "gates", gid,
                                "constants", tok,
                                f"archive-harvested: row mentions {tok}",
                            )
                # Edge C: cross-validation from prose in cells after verdict
                for cell in row[verdict_idx + 1:]:
                    cell_clean_str = strip_md_emphasis(cell)
                    m_conf = re.search(
                        r"(?:Confirmed by|cf\.|cross-check|see also)\s+"
                        r"([A-Z][A-Za-z0-9]*(?:-[A-Za-z0-9]+){1,4})",
                        cell_clean_str,
                    )
                    if m_conf:
                        other = m_conf.group(1)
                        if RE_GATE_ID.match(other) and other != gid:
                            buf.add(
                                "cross_validates", "gates", gid,
                                "gates", other,
                                f"archive-harvested: cross-check cell ({other})",
                            )
                continue

            # Pattern ζ: gate-ID in col-0, NO verdict cell, but section header
            # implies a gate-row (Constraint Map / Theorems / Closures / Structural).
            if gid_idx == 0 and verdict_idx < 0 and any(
                k in header_lc for k in ZETA_HEADERS
            ):
                buf.add(
                    "reproduces", "gates", gid, "sessions", sess,
                    f"archive-harvested: ζ-pattern row in '{header[:50]}'",
                )
                # Constants in ALL subsequent cells (dedup at buf-level).
                for cell in row[1:]:
                    for tok in re.findall(r"[A-Za-z_][A-Za-z0-9_]+", cell):
                        if (tok in canonical_names
                                and _CONSTANT_NAME_STRICT.match(tok)):
                            buf.add(
                                "reproduces", "gates", gid,
                                "constants", tok,
                                f"archive-harvested: ζ-pattern row mentions {tok}",
                            )
                continue

    # ----------- Pattern 2: Mechanism Closures section -----------
    # Subsection headings look like:
    #   ### 1. Singlet Tridiagonal PMNS (PMNS-CORRECTED-35)
    # We emit closed_by from the mechanism slug to the gate.
    for m in re.finditer(
        r"^###\s+\d+\.\s+(?P<name>[^\n(]+?)\s*\((?P<gate>[A-Z][A-Z0-9_-]+)\)\s*$",
        text, re.MULTILINE,
    ):
        name = strip_md_emphasis(m.group("name")).strip()
        gate_id = m.group("gate")
        if not RE_GATE_ID.match(gate_id):
            continue
        # Mechanism slug: collapse whitespace+punctuation into underscores
        slug = re.sub(r"[^A-Za-z0-9]+", "_", name).strip("_")
        if not slug or len(slug) < 4:
            continue
        # Only emit when the section context is "Closures" — check the
        # nearest preceding ## heading.
        # We search backwards from this match for the last "## " line.
        before = text[:m.start()]
        last_h2 = before.rfind("\n## ")
        if last_h2 == -1:
            continue
        h2_line = before[last_h2 + 1:]
        if "closur" not in h2_line.lower() and "closed" not in h2_line.lower():
            # Not a closures section — skip rather than emit a mis-typed edge.
            continue
        buf.add(
            "closed_by", "open_channels", slug,
            "gates", gate_id,
            f"archive-harvested: closure section in S{sess} ({name[:60]})",
        )

    # ----------- Pattern 4: Files Produced — script -> gate -----------
    # Look for tables where col-0 is a script-prefix (sNN_...) and col-1
    # is a gate-id. Mirrors s81_harvested_edges.txt:8 convention.
    for header, body in blocks:
        if "files produced" not in header.lower() and "computation" not in header.lower():
            # Permissive: also check section text mentions "Computation Computations"
            if "computation" not in body.lower()[:200]:
                continue
        for row in parse_markdown_table_rows(body):
            if len(row) < 2:
                continue
            script_prefix = strip_md_emphasis(row[0])
            gate_id = strip_md_emphasis(row[1])
            if not re.match(r"^s\d+[a-z]?_[A-Za-z0-9_]+$", script_prefix):
                continue
            if not RE_GATE_ID.match(gate_id):
                continue
            buf.add(
                "feeds_into", "data_provenance", f"{script_prefix}.py",
                "gates", gate_id,
                f"archive-harvested: Files Produced table in S{sess}",
            )

    return buf.dedup()


# ----------------------------------------------------------------------------
# Driver
# ----------------------------------------------------------------------------

def discover_summary_files() -> list[Path]:
    """Return all session-final/quicklook markdown files under summary/."""
    paths: list[Path] = []
    for d in (SUMMARY_ARCHIVE_DIR, SUMMARY_DIR):
        if not d.is_dir():
            continue
        for p in sorted(d.glob("session-*.md")):
            if RE_SUMMARY_FILE.match(p.name):
                paths.append(p)
    return paths


HEADER_TEMPLATE = (
    "## S{sess} Archive-Harvested Edges (generated by tools/harvest_archive_edges.py)\n"
    "## Source: summary/{rel}\n"
    "## Conservative-harvest discipline: prefer miss over false-positive\n"
    "## (per computations/_shared/_harvest_edges.py:12-14).\n"
    "\n"
)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry", action="store_true",
                    help="Preview edges only; do not write output files.")
    ap.add_argument("--limit", type=int, default=0,
                    help="Limit to first N source files (0 = all).")
    args = ap.parse_args()

    canonical_names = load_canonical_names()
    paths = discover_summary_files()
    if args.limit:
        paths = paths[:args.limit]

    if not paths:
        print("No summary files found.")
        return 0

    total_raw = 0
    total_written = 0
    per_session: dict[str, list[dict]] = {}
    rel_for_sess: dict[str, str] = {}

    for p in paths:
        sess = extract_session_id(p.name)
        if not sess:
            continue
        edges = harvest_one(p, canonical_names)
        total_raw += len(edges)
        per_session.setdefault(sess, []).extend(edges)
        # Earliest-source-file wins for the relative-path comment.
        rel_for_sess.setdefault(sess, str(p.relative_to(SUMMARY_DIR.parent)))

    # Per-session dedup AND write.
    type_total: dict[str, int] = {}
    for sess, edges in sorted(per_session.items(), key=lambda x: int(x[0])):
        seen: set[tuple] = set()
        deduped: list[dict] = []
        for e in edges:
            key = (e["type"], e["src_type"], e["src_id"].lower(),
                   e["tgt_type"], e["tgt_id"].lower())
            if key in seen:
                continue
            seen.add(key)
            deduped.append(e)
        if not deduped:
            continue
        for e in deduped:
            type_total[e["type"]] = type_total.get(e["type"], 0) + 1

        out_path = COMPUTATIONS_DIR / f"s{sess}_archive_harvested_edges.txt"
        if args.dry:
            print(f"[dry] would write {out_path.name}: {len(deduped)} edges")
            continue

        lines = [HEADER_TEMPLATE.format(sess=sess, rel=rel_for_sess[sess].replace("\\", "/"))]
        for e in deduped:
            lines.append(
                f"[EDGE:{e['type']}] {e['src_type']}:{e['src_id']} -> "
                f"{e['tgt_type']}:{e['tgt_id']}  # {e['comment']}\n"
            )
        out_path.write_text("".join(lines), encoding="utf-8")
        total_written += len(deduped)

    # Summary
    print(f"\nScanned {len(paths)} summary file(s); "
          f"harvested {total_raw} raw edge(s), wrote {total_written} unique.")
    print("By type:")
    for t, c in sorted(type_total.items(), key=lambda x: -x[1]):
        print(f"  {t:20s}  {c}")
    print("By session (top 25 by count):")
    rows = [(s, len(set(
        (e["type"], e["src_type"], e["src_id"].lower(),
         e["tgt_type"], e["tgt_id"].lower())
        for e in es)))
        for s, es in per_session.items()]
    for s, c in sorted(rows, key=lambda x: -x[1])[:25]:
        if c > 0:
            print(f"  S{s:>4s}  {c:4d} edges")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
