#!/usr/bin/env python3
"""
Harvest theorem -> constants and closed_mechanism -> constants edges from
the knowledge graph.

Theorem statements (`theorems.statement`) and closed-mechanism notes
(`closed_mechanisms.closed_by` -- the schema's free-text column; the
table has no `status_note` column) frequently mention named canonical
constants by their identifier. The existing edge-mining harvesters
(harvest_archive_edges.py, harvest_provenance_edges.py,
harvest_script_import_edges.py) never read knowledge.db, so this corpus
of citations is unmined.

This harvester walks both tables and emits one `[EDGE:bounds]` row per
unique (entity_id, constant_name) pair where the entity's text
contains a word-boundary token that matches a name in
`canonical_constants.py`.

Edge type: `bounds` (one of the 13 typed edges; semantically "the
theorem statement / closure note ranges over / constrains the
constant").

Source-of-truth for entity-type aliases: tools/extract_entities.py
ALIAS_MAP at line ~1927 ("theorems" -> "theorems",
"closed_mechanisms" -> "closed_mechanisms").

Output: computations/_shared/theorem_closure_edges.txt (single file;
re-runnable; matches existing edge-file conventions documented in
harvest_provenance_edges.py:23-24).

Conservative-discipline (mirrors _harvest_edges.py:12-14):
  * Word-boundary regex match (`\\b<name>\\b`) only.
  * Two-stage filter: token must appear in canonical_constants vocab.
  * Skip rows whose name is empty.
  * Statement / closed_by are read defensively via .get() so a NULL
    column does not raise.

Gate ID for this tool: THEOREM-CLOSURE-EDGE-HARVEST (NON-PHONONIC,
infrastructure).
"""
from __future__ import annotations

import re
import sqlite3
import sys
from collections import Counter
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
COMPUTATIONS_DIR = PROJECT_ROOT / "computations"
DB_PATH = PROJECT_ROOT / "tools" / "knowledge.db"
CC_PATH = COMPUTATIONS_DIR / "_shared" / "canonical_constants.py"
OUT_PATH = COMPUTATIONS_DIR / "theorem_closure_edges.txt"


# ----------------------------------------------------------------------------
# Vocabulary loader (mirrors harvest_archive_edges.py:46-59)
# ----------------------------------------------------------------------------

def load_canonical_names() -> set[str]:
    """Return the set of identifier-shaped public names exported by
    canonical_constants.py. This vocabulary is the membership filter
    used in conjunction with the word-boundary regex.
    """
    if not CC_PATH.exists():
        return set()
    sys.path.insert(0, str(COMPUTATIONS_DIR / "_shared"))
    try:
        import canonical_constants as CC  # noqa: WPS433
    except Exception:                         # noqa: BLE001
        return set()
    return {n for n in dir(CC) if not n.startswith("_") and n.isidentifier()}


# ----------------------------------------------------------------------------
# Row-text extraction
# ----------------------------------------------------------------------------

def row_get(row: sqlite3.Row, col: str) -> str:
    """Defensive .get() for sqlite3.Row -- returns "" when the column
    is NULL or absent. sqlite3.Row supports __getitem__ but raises
    IndexError on unknown keys, so we wrap.
    """
    try:
        v = row[col]
    except (IndexError, KeyError):
        return ""
    if v is None:
        return ""
    return str(v)


# ----------------------------------------------------------------------------
# Per-row scan: emit (entity_id, constant_name) pairs where
# `\b<name>\b` matches the concatenated text and `name` is in vocab.
# ----------------------------------------------------------------------------

def scan_text(text: str, vocab: set[str], compiled: dict[str, re.Pattern]) -> set[str]:
    """Return the set of canonical-constant names found in `text` via
    word-boundary match. The compiled-pattern cache is shared across
    rows so the regex compile cost is paid once per name.
    """
    if not text:
        return set()
    found: set[str] = set()
    # Coarse pre-filter: only test names whose first 2 chars appear in
    # the text (cheap O(len(text)) substring check). This skips ~95%
    # of vocab on short statements.
    text_lower = text.lower()
    for name in vocab:
        if name[:2].lower() not in text_lower and name[:2] not in text:
            # Substring miss on both case-folded and exact prefix --
            # the word-boundary regex cannot match.
            continue
        pat = compiled.get(name)
        if pat is None:
            pat = re.compile(r"\b" + re.escape(name) + r"\b")
            compiled[name] = pat
        if pat.search(text):
            found.add(name)
    return found


# ----------------------------------------------------------------------------
# Driver
# ----------------------------------------------------------------------------

HEADER = (
    "## Theorem & Closed-Mechanism -> Constants Edges\n"
    "## Generated by tools/harvest_theorem_closure_edges.py\n"
    "## Source: tools/knowledge.db (theorems.statement + closed_mechanisms.closed_by)\n"
    "## Vocabulary: computations/_shared/canonical_constants.py public names\n"
    "## Match rule: word-boundary regex (\\b<name>\\b) AND vocab membership\n"
    "## Edge type: bounds (theorem/closure cites a constant in its statement/note)\n"
    "\n"
)


def main() -> int:
    vocab = load_canonical_names()
    if not vocab:
        print("ERROR: canonical_constants.py vocabulary is empty; aborting.")
        return 1
    if not DB_PATH.exists():
        print(f"ERROR: knowledge.db not found at {DB_PATH}")
        return 1

    con = sqlite3.connect(str(DB_PATH))
    con.row_factory = sqlite3.Row

    compiled: dict[str, re.Pattern] = {}
    edges: list[tuple[str, str, str, str]] = []  # (alias, ent_id, const, snippet)
    inbound: Counter[str] = Counter()
    errors: list[tuple[str, str, str]] = []

    # ---------------- theorems ----------------
    n_theorems_scanned = 0
    n_theorems_edges = 0
    for row in con.execute("SELECT id, name, statement FROM theorems"):
        try:
            ent_id = row_get(row, "id")
            name = row_get(row, "name")
            statement = row_get(row, "statement")
            if not ent_id:
                continue
            n_theorems_scanned += 1
            text = (name + " " + statement).strip()
            if not text:
                continue
            hits = scan_text(text, vocab, compiled)
            for const in sorted(hits):
                snippet = (name + " | " + statement).strip(" |")[:150]
                edges.append(("theorems", ent_id, const, snippet))
                inbound[const] += 1
                n_theorems_edges += 1
        except Exception as exc:                  # noqa: BLE001
            errors.append(("theorems", row_get(row, "id"), repr(exc)))

    # ---------------- closed_mechanisms ----------------
    # Schema: closed_mechanisms(id, name, closed_by, session, gate_id,
    # source_file). The task spec named the note column "status_note"
    # but the actual column is `closed_by` -- per the task's
    # "use .get() defensively in case statement is null" instruction
    # we treat closed_by as the note text and skip rows where neither
    # name nor closed_by has content.
    n_closures_scanned = 0
    n_closures_edges = 0
    for row in con.execute(
        "SELECT id, name, closed_by FROM closed_mechanisms"
    ):
        try:
            ent_id = row_get(row, "id")
            name = row_get(row, "name")
            note = row_get(row, "closed_by")
            if not ent_id:
                continue
            n_closures_scanned += 1
            text = (name + " " + note).strip()
            if not text:
                continue
            hits = scan_text(text, vocab, compiled)
            for const in sorted(hits):
                snippet = (name + " | " + note).strip(" |")[:150]
                edges.append(("closed_mechanisms", ent_id, const, snippet))
                inbound[const] += 1
                n_closures_edges += 1
        except Exception as exc:                  # noqa: BLE001
            errors.append(("closed_mechanisms", row_get(row, "id"), repr(exc)))

    # ---------------- dedup (entity_id, constant_name) pairs ----------------
    seen: set[tuple[str, str]] = set()
    deduped: list[tuple[str, str, str, str]] = []
    for alias, ent_id, const, snippet in edges:
        key = (ent_id, const)
        if key in seen:
            continue
        seen.add(key)
        deduped.append((alias, ent_id, const, snippet))

    # Recompute inbound from deduped pairs (counter above
    # double-counts when the same theorem cites the same const twice
    # via name+statement vs statement-only matches).
    inbound = Counter()
    n_theorems_unique = 0
    n_closures_unique = 0
    for alias, ent_id, const, _snippet in deduped:
        inbound[const] += 1
        if alias == "theorems":
            n_theorems_unique += 1
        else:
            n_closures_unique += 1

    # ---------------- write output ----------------
    lines = [HEADER]
    for alias, ent_id, const, snippet in deduped:
        kind_tag = "theorem statement" if alias == "theorems" else "closure note"
        lines.append(
            f"[EDGE:bounds] {alias}:{ent_id} -> constants:{const}  "
            f"# {kind_tag} cites {const} ({snippet})\n"
        )
    OUT_PATH.write_text("".join(lines), encoding="utf-8")

    # ---------------- report ----------------
    print(f"Wrote {OUT_PATH.relative_to(PROJECT_ROOT)}")
    print(f"Theorems scanned: {n_theorems_scanned} | "
          f"unique edges emitted: {n_theorems_unique}")
    print(f"Closures scanned: {n_closures_scanned} | "
          f"unique edges emitted: {n_closures_unique}")
    print(f"Total unique edges: {len(deduped)}")
    print()
    print("Top 15 constants by inbound degree (theorems + closures combined):")
    for const, c in inbound.most_common(15):
        print(f"  {const:30s}  {c}")
    print()
    if errors:
        print(f"Errored rows ({len(errors)}):")
        for tbl, rid, exc in errors[:20]:
            print(f"  {tbl}:{rid}  {exc}")
    else:
        print("Errored rows: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
