#!/usr/bin/env python3
"""
harvest_equation_edges.py
=========================

Edge-mining harvester for the equation library in tools/knowledge.db.

Scans the `equations` table (filtered to type IN ('display','structural'))
and emits `[EDGE:depends_on] equations:EQ_ID -> constants:NAME` lines for
every canonical-constant token that appears (word-boundary) in the
equation `raw` text. The pipeline auto-ingests these from
computations/_shared/*.txt files.

Schema notes (verified at write-time):
  equations(id TEXT, type TEXT, raw TEXT, file TEXT, line INTEGER,
            context TEXT, source_file TEXT)

  type counts:
    code        188837   (skipped — too noisy)
    comment      60752   (skipped — too noisy)
    structural   12443   (kept)
    inline        3972   (skipped — too noisy)
    display       1273   (kept)

Vocab source:
  computations/_shared/canonical_constants.py — top-level assignments
  matching ^[A-Za-z_][A-Za-z0-9_]*\\s*= are extracted as the
  canonical-constant vocabulary. Single-letter and underscore-only
  names are excluded as too generic.

Output:
  computations/_shared/equation_edges.txt
"""

from __future__ import annotations

import ast
import re
import sqlite3
from collections import Counter, defaultdict
from pathlib import Path

# ----------------------------------------------------------------------------
# Paths
# ----------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "tools" / "knowledge.db"
CC_PATH = ROOT / "computations" / "_shared" / "canonical_constants.py"
OUT_PATH = ROOT / "computations" / "_shared" / "equation_edges.txt"


# ----------------------------------------------------------------------------
# 1. Canonical-constant vocab extraction
# ----------------------------------------------------------------------------
def load_canonical_vocab(cc_path: Path) -> set[str]:
    """Parse canonical_constants.py and return the set of top-level names
    bound by simple assignment (Name = ...). Uses ast for robustness vs
    regex (handles multi-line RHS, dict-of-provenance blocks, etc.)."""
    src = cc_path.read_text(encoding="utf-8")
    tree = ast.parse(src)
    names: set[str] = set()
    for node in tree.body:
        # top-level assignments only
        if isinstance(node, ast.Assign):
            for tgt in node.targets:
                if isinstance(tgt, ast.Name):
                    names.add(tgt.id)
        elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            names.add(node.target.id)
    # Filter generics: single-letter (ambiguous in latex), all-caps short
    # tokens like "PI" (covered by other variants), pure underscore fragments.
    # Keep "PI" since it is the canonical name even if generic.
    filtered = {n for n in names if len(n) >= 2}
    # Drop python builtins / module aliases that snuck in via top-level Assign
    drop = {"np", "PROVENANCE", "warnings", "sys"}
    filtered -= drop
    return filtered


# ----------------------------------------------------------------------------
# 2. DB scan
# ----------------------------------------------------------------------------
def fetch_equations(db_path: Path):
    """Yield (id, raw, type, source_file) rows for kept equation kinds."""
    con = sqlite3.connect(str(db_path))
    cur = con.cursor()
    cur.execute(
        "SELECT id, raw, type, source_file FROM equations "
        "WHERE type IN ('display','structural')"
    )
    for row in cur:
        yield row
    con.close()


# ----------------------------------------------------------------------------
# 3. Edge mining
# ----------------------------------------------------------------------------
def build_pattern(vocab: set[str]) -> re.Pattern:
    """One combined regex with word boundaries.

    Sort by length DESC so longer names match before shorter prefixes
    (Python's `re` alternation otherwise picks the first match in pattern
    order; with word boundaries this matters less, but length-sort is a
    cheap robustness win)."""
    parts = sorted(vocab, key=len, reverse=True)
    escaped = [re.escape(p) for p in parts]
    pat = r"(?<![A-Za-z0-9_])(" + "|".join(escaped) + r")(?![A-Za-z0-9_])"
    return re.compile(pat)


def harvest():
    vocab = load_canonical_vocab(CC_PATH)
    pattern = build_pattern(vocab)

    eq_count = 0
    edges: list[tuple[str, str]] = []
    seen: set[tuple[str, str]] = set()
    inbound: Counter[str] = Counter()

    for eq_id, raw, eq_type, source_file in fetch_equations(DB_PATH):
        eq_count += 1
        if not raw:
            continue
        # Find all distinct constant names in this equation
        hits = set(pattern.findall(raw))
        for name in hits:
            key = (eq_id, name)
            if key in seen:
                continue
            seen.add(key)
            edges.append((eq_id, name))
            inbound[name] += 1

    return eq_count, edges, inbound, vocab


# ----------------------------------------------------------------------------
# 4. Emit
# ----------------------------------------------------------------------------
HEADER = """# equation_edges.txt
# Auto-generated by tools/harvest_equation_edges.py
# Source: tools/knowledge.db (equations table, type IN ('display','structural'))
# Vocab : computations/_shared/canonical_constants.py top-level names (len>=2)
# Format: [EDGE:depends_on] equations:EQ_ID -> constants:NAME  # <type-tag>
#
"""


def write_edges(edges: list[tuple[str, str]]):
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUT_PATH.open("w", encoding="utf-8") as f:
        f.write(HEADER)
        for eq_id, name in edges:
            f.write(
                f"[EDGE:depends_on] equations:{eq_id} -> constants:{name}"
                f"  # display/structural eq references {name}\n"
            )


# ----------------------------------------------------------------------------
# 5. Main
# ----------------------------------------------------------------------------
def main():
    eq_count, edges, inbound, vocab = harvest()
    write_edges(edges)

    # Report
    print(f"Vocab size (canonical-constant names, len>=2): {len(vocab)}")
    print(f"Equations scanned (type IN display,structural): {eq_count}")
    print(f"Unique edges emitted: {len(edges)}")
    print(f"Distinct constants reached: {len(inbound)}")
    print(f"Output: {OUT_PATH}")
    print()
    print("Top 20 constants by inbound degree:")
    for name, deg in inbound.most_common(20):
        print(f"  {deg:6d}  {name}")


if __name__ == "__main__":
    main()
