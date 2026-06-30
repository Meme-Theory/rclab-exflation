#!/usr/bin/env python
"""Harvest gate->constant edges from session-plan machinery_pin_map blocks.

Walks every plan file under sessions/session-plan/ (current + archive), locates
gate blocks via heading anchors or YAML gate_id keys, then scans each block's
pinned-input subsections (machinery_pin_map, Inputs (pinned), Pre-registered
constants, Input SHA-256 pins, Pinned inputs) plus a soft prose zone for
canonical-constant tokens. Emits unique [EDGE:depends_on] gates:<G> ->
constants:<C> lines into computations/_shared/plan_pin_edges.txt for the
existing edge-mining pipeline to ingest.

Conservative discipline:
- Skips fenced code blocks (triple-backticks).
- Word-boundary matches only.
- Per (gate, constant) pair: emit one edge max, regardless of plan-revision
  duplication.
"""

from __future__ import annotations

import importlib.util
import re
import sys
from collections import defaultdict
from pathlib import Path

# ---------------------------------------------------------------------------
# Project paths (relative to repo root; this script is invoked from there).
# ---------------------------------------------------------------------------

ROOT = Path(__file__).resolve().parent.parent
CANONICAL = ROOT / "computations" / "_shared" / "canonical_constants.py"
PLAN_DIRS = [
    (ROOT / "sessions" / "session-plan", "session-*-plan*.md"),
    (ROOT / "sessions" / "session-plan" / "archive", "*.md"),
]
OUTPUT = ROOT / "computations" / "_shared" / "plan_pin_edges.txt"


# ---------------------------------------------------------------------------
# 1. Load canonical-constant vocab from canonical_constants.py
# ---------------------------------------------------------------------------

def load_canonical_vocab() -> set[str]:
    """Import canonical_constants.py as a module and harvest its public names.

    Returns the set of names that look like physics constants: drop dunders,
    drop names that are obviously imports (modules), and keep identifiers
    that are scalars / arrays / strings / floats.
    """
    spec = importlib.util.spec_from_file_location("canonical_constants", CANONICAL)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {CANONICAL}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    vocab: set[str] = set()
    for name in dir(mod):
        if name.startswith("_"):
            continue
        val = getattr(mod, name)
        # Skip modules and callables / classes -- only pin real CONSTANTS.
        if callable(val):
            continue
        if type(val).__name__ == "module":
            continue
        # A "constant" name should be at least 2 chars (filters "e", "i" stray)
        # and contain at least one of: underscore, digit, or uppercase.
        if len(name) < 2:
            continue
        if not (any(c.isdigit() for c in name) or "_" in name or any(c.isupper() for c in name)):
            continue
        vocab.add(name)
    return vocab


# ---------------------------------------------------------------------------
# 2. Code-block stripper.
# ---------------------------------------------------------------------------

CODE_FENCE = re.compile(r"^```")


def strip_code_blocks(text: str) -> str:
    """Replace lines inside triple-backtick fences with blank lines.

    Preserves line numbering so downstream offsets stay aligned.
    """
    out: list[str] = []
    in_block = False
    for line in text.splitlines():
        if CODE_FENCE.match(line.strip()):
            in_block = not in_block
            out.append("")  # drop fence line
            continue
        out.append("" if in_block else line)
    return "\n".join(out)


# ---------------------------------------------------------------------------
# 3. Gate-block detection.
# ---------------------------------------------------------------------------

# Gate-ID token: matches things like S85-W1a-SCHEME-DEP, T3-FOO-BAR-1, M-3, V-1.
# Requires at least one hyphen, starts uppercase or T3-, segments mix letters/digits.
GATE_ID = re.compile(r"\b((?:T3-)?[A-Z][A-Za-z0-9]*(?:-[A-Za-z0-9]+)+)\b")

# Heading lines that may anchor a gate block. Three observed forms:
#   ## §W1a-1. S85-W1a-SCHEME-DEP
#   ## §W9a-97 — S84-W1-CF-PRU-TOOL
#   ### W4-43 — Title (GATE-ID)
HEADING = re.compile(r"^#{1,6}\s+.+$")

# YAML-block-anchored: a line "gate_id: GATE-ID" inside a YAML mapping.
YAML_GATE_ID = re.compile(r"^\s*gate_id:\s*['\"]?([^'\"\s#]+)['\"]?\s*(?:#.*)?$")


def find_gate_blocks(text: str) -> list[tuple[str, int, int]]:
    """Return list of (gate_id, body_start_idx, body_end_idx) over the text.

    A gate block runs from the heading/YAML anchor line to (exclusive) the
    next anchor of either kind, or to EOF.
    """
    lines = text.splitlines()
    anchors: list[tuple[int, str]] = []  # (line_idx, gate_id)

    for i, line in enumerate(lines):
        # YAML-block-anchored.
        m = YAML_GATE_ID.match(line)
        if m:
            gate_id = m.group(1)
            # Confirm matches the gate-ID regex shape (rejects bare names).
            if GATE_ID.fullmatch(gate_id) or "-" in gate_id:
                anchors.append((i, gate_id))
                continue
        # Heading-anchored: scan headings for the first gate-ID token.
        if HEADING.match(line):
            mm = GATE_ID.search(line)
            if mm:
                anchors.append((i, mm.group(1)))

    # Convert anchor indices into char offsets in the joined text.
    # Easier: precompute line start offsets.
    offsets = [0]
    for ln in lines:
        offsets.append(offsets[-1] + len(ln) + 1)  # +1 for the "\n"

    blocks: list[tuple[str, int, int]] = []
    for k, (line_idx, gate_id) in enumerate(anchors):
        start = offsets[line_idx]
        end = offsets[anchors[k + 1][0]] if k + 1 < len(anchors) else len(text)
        blocks.append((gate_id, start, end))
    return blocks


# ---------------------------------------------------------------------------
# 4. Pinned-input subsection detection inside a gate body.
# ---------------------------------------------------------------------------

PIN_HEADERS = [
    re.compile(r"(?im)^\s*[-*#>\s]*\**\s*Inputs\s*\(pinned\)\s*[:\*]"),
    re.compile(r"(?im)^\s*[-*#>\s]*\**\s*machinery[_\- ]pin[_\- ]map\s*[:\*]"),
    re.compile(r"(?im)^\s*[-*#>\s]*\**\s*Pre[-_ ]registered\s+constants\s*[:\*]"),
    re.compile(r"(?im)^\s*[-*#>\s]*\**\s*Input\s+SHA[-_ ]?256\s+pins\s*[:\*]"),
    re.compile(r"(?im)^\s*[-*#>\s]*\**\s*Pinned\s+inputs\s*[:\*]"),
    # Common variant from S84/S85 plans: "**7. Machinery pin (PRDR §0.11)**"
    re.compile(r"(?im)^\s*[-*#>\s]*\**\s*\d*\.?\s*Machinery\s+pin\b"),
]

# Lines that end a pin section: the next bold-numbered list item, the next
# top-level YAML key (no leading whitespace, ends with ':'), or another
# heading.
SECTION_END_PATTERNS = [
    re.compile(r"^\s*\*\*\d+\.\s"),                # **8. Expected output...
    re.compile(r"^[A-Za-z][A-Za-z0-9_]*:\s*$"),    # top-level YAML key
    re.compile(r"^#{1,6}\s+"),                     # markdown heading
    re.compile(r"^---\s*$"),                       # rule
]


def extract_pin_zone(body: str) -> str:
    """Return the union of pinned-input subsections within a gate body.

    For each known pin header found, take from header line until next
    section-terminator. Concatenate with newlines. May be empty.
    """
    chunks: list[str] = []
    for pat in PIN_HEADERS:
        for m in pat.finditer(body):
            sec_start = m.start()
            # Find the line break that ends the header line.
            line_start = body.rfind("\n", 0, sec_start) + 1
            sec_lines_start = body.find("\n", sec_start)
            if sec_lines_start == -1:
                chunks.append(body[line_start:])
                continue
            # Walk forward line-by-line until a section-end pattern hits.
            tail = body[sec_lines_start + 1:]
            tail_lines = tail.splitlines(keepends=True)
            collected: list[str] = []
            for tl in tail_lines:
                if any(p.match(tl) for p in SECTION_END_PATTERNS):
                    break
                collected.append(tl)
            chunks.append(body[line_start:sec_lines_start + 1] + "".join(collected))
    return "\n".join(chunks)


# ---------------------------------------------------------------------------
# 5. Canonical-name token scanner.
# ---------------------------------------------------------------------------

def find_constants(text: str, vocab: set[str]) -> set[str]:
    """Word-boundary scan: return constants from `vocab` that appear in `text`."""
    found: set[str] = set()
    if not text:
        return found
    # Single regex with all vocab terms; sort longest-first so e.g. M_KK
    # is preferred over a shorter prefix when both could match (not strictly
    # necessary with \b but defensive).
    if not vocab:
        return found
    sorted_vocab = sorted(vocab, key=len, reverse=True)
    pattern = re.compile(r"\b(" + "|".join(re.escape(v) for v in sorted_vocab) + r")\b")
    for m in pattern.finditer(text):
        found.add(m.group(1))
    return found


# ---------------------------------------------------------------------------
# 6. Per-plan harvest.
# ---------------------------------------------------------------------------

def harvest_plan(path: Path, vocab: set[str]) -> tuple[int, dict[str, set[str]]]:
    """Return (gate_block_count, edges_dict[gate_id -> set of constants])."""
    raw = path.read_text(encoding="utf-8", errors="replace")
    text = strip_code_blocks(raw)
    blocks = find_gate_blocks(text)

    edges: dict[str, set[str]] = defaultdict(set)
    for gate_id, start, end in blocks:
        body = text[start:end]
        # Hard zone: declared pin subsections.
        pin_zone = extract_pin_zone(body)
        # Soft zone: first 800 chars of gate-block body (catches prose
        # like "uses M_KK=1.5e16" without a structured pin list).
        soft_zone = body[:800]
        scan_text = pin_zone + "\n" + soft_zone
        consts = find_constants(scan_text, vocab)
        if consts:
            edges[gate_id].update(consts)
    return len(blocks), edges


# ---------------------------------------------------------------------------
# 7. Driver.
# ---------------------------------------------------------------------------

def main() -> None:
    vocab = load_canonical_vocab()

    plan_files: list[Path] = []
    for d, pat in PLAN_DIRS:
        if d.is_dir():
            plan_files.extend(sorted(d.glob(pat)))
    # Dedup (archive may overlap if symlinks).
    seen: set[Path] = set()
    plan_files = [p for p in plan_files if not (p.resolve() in seen or seen.add(p.resolve()))]

    all_edges: dict[str, set[str]] = defaultdict(set)
    gate_block_total = 0
    plans_zero: list[str] = []

    for path in plan_files:
        gb, edges = harvest_plan(path, vocab)
        gate_block_total += gb
        if not edges:
            plans_zero.append(path.name)
            continue
        for g, cs in edges.items():
            all_edges[g].update(cs)

    # Build the unique edge set. Per (gate, const) pair, exactly one edge.
    edge_lines: list[str] = []
    for gate_id in sorted(all_edges):
        for const in sorted(all_edges[gate_id]):
            edge_lines.append(
                f"[EDGE:depends_on] gates:{gate_id} -> constants:{const}"
                f"  # plan-pin or plan-prose mention"
            )

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        "# Auto-generated by tools/harvest_plan_pin_edges.py\n"
        "# Edges: gate -> canonical-constant pinned in session-plan machinery_pin_map\n"
        "# Source: sessions/session-plan/**/*.md\n\n"
        + "\n".join(edge_lines)
        + ("\n" if edge_lines else ""),
        encoding="utf-8",
    )

    # Inbound-degree ranking on constants.
    inbound: dict[str, int] = defaultdict(int)
    for gate_id, cs in all_edges.items():
        for c in cs:
            inbound[c] += 1
    top15 = sorted(inbound.items(), key=lambda kv: (-kv[1], kv[0]))[:15]

    # Report.
    print(f"Plan files scanned:    {len(plan_files)}")
    print(f"Gate blocks detected:  {gate_block_total}")
    print(f"Unique gates with >=1 edge: {len(all_edges)}")
    print(f"Unique edges emitted:  {len(edge_lines)}")
    print(f"Output written to:     {OUTPUT.relative_to(ROOT)}")
    print()
    print("Top 15 constants by inbound degree:")
    for name, deg in top15:
        print(f"  {deg:5d}  {name}")
    print()
    if plans_zero:
        print(f"Plans yielding zero edges ({len(plans_zero)}):")
        for n in plans_zero:
            print(f"  {n}")
    else:
        print("Plans yielding zero edges: (none)")


if __name__ == "__main__":
    sys.exit(main())
