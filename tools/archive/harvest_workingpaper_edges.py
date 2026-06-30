#!/usr/bin/env python3
"""
Harvest gate -> constant edges from working-paper prose.

Working papers (`sessions/session-NN/session-NN-{results,wave,W,wN}-workingpaper.md`)
contain gate sections in their prose that cite specific canonical constants
(e.g. "M_KK = 1.5e16 GeV from G42-M3", "tau_fold drives the transit").
Existing harvesters (`tools/harvest_archive_edges.py`,
`computations/_shared/_harvest_edges.py`) work on session-final summaries +
T3 verdict files; neither walks the working-paper corpus, so these
gate -> constant edges are missed entirely.

This script adds that pass.

For each working-paper file:
  1. Strip fenced code blocks (no ``` ... ``` content scanned).
  2. Locate gate-section headings (## .. ####, possibly with §-marker).
  3. For each section: extract its body up to the next same-or-higher
     heading; scan for canonical-constant tokens (word-boundary match against
     the canonical_constants vocabulary).
  4. Emit one edge per (gate, constant) pair, dedup'd across the corpus.

Output: `computations/_shared/workingpaper_edges.txt` (single file), in
the standard `[EDGE:reproduces]` line format consumed by
`/weave --update` ingestion.

Conservative-discipline: prefer miss over false-positive.
- Constants must match \\b<name>\\b — no substring matches.
- Gate IDs must match the same regex used by `harvest_archive_edges.py`.
- Headings without a gate-ID token are skipped (no filename fallback).
- Pairs are deduped across the WHOLE corpus, not per-occurrence.

Gate ID for this tool: WP-EDGE-HARVEST (NON-PHONONIC, infrastructure).
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
COMPUTATIONS_DIR = PROJECT_ROOT / "computations"
SESSIONS_DIR = PROJECT_ROOT / "sessions"
CC_PATH = COMPUTATIONS_DIR / "_shared" / "canonical_constants.py"
OUTPUT_PATH = COMPUTATIONS_DIR / "workingpaper_edges.txt"


# ----------------------------------------------------------------------------
# Vocabulary loader — mirrors the pattern in harvest_archive_edges.py
# ----------------------------------------------------------------------------

def load_canonical_names() -> set[str]:
    if not CC_PATH.exists():
        return set()
    sys.path.insert(0, str(COMPUTATIONS_DIR / "_shared"))
    try:
        import canonical_constants as CC  # noqa: WPS433
    except Exception:                          # noqa: BLE001
        return set()
    return {n for n in dir(CC) if not n.startswith("_") and n.isidentifier()}


# ----------------------------------------------------------------------------
# Regex inventory
# ----------------------------------------------------------------------------

# Gate-ID shape: (T3- prefix optional) + leading-cap word + at least one
# hyphen-segment.  Identical to harvest_archive_edges.RE_GATE_ID.
RE_GATE_ID_TOKEN = re.compile(
    r"\b((?:T3-)?[A-Z][A-Za-z0-9]*(?:-[A-Za-z0-9]+){1,6})\b"
)

# Section headings (## through ####).  We scan the WHOLE heading text for the
# first gate-ID-shaped token (per spec, the first such token IS the gate ID).
RE_HEADING = re.compile(r"^(#{2,4})\s+(.+?)\s*$", re.MULTILINE)

# Fenced code block (triple-backtick), greedy match across newlines.
RE_FENCED_CODE = re.compile(r"```.*?```", re.DOTALL)

# Working-paper filename matcher.
RE_WP_FILE = re.compile(r".*workingpaper\.md$", re.IGNORECASE)

# Session ID extraction (from path parents).
RE_SESSION_DIR = re.compile(r"^session-(\d+[a-z]?)$", re.IGNORECASE)


# ----------------------------------------------------------------------------
# File discovery
# ----------------------------------------------------------------------------

def discover_workingpapers() -> list[Path]:
    """Walk the working-paper corpus.

    Per spec, three glob patterns are unioned:
      sessions/session-*/session-*-results-workingpaper.md
      sessions/session-*/*-workingpaper.md
      sessions/session-*/**/*workingpaper*.md   (recursive)

    Plus the archive subtree for completeness:
      sessions/archive/session-*/**/*workingpaper*.md
    """
    seen: set[Path] = set()
    patterns = [
        "session-*/session-*-results-workingpaper.md",
        "session-*/*-workingpaper.md",
        "session-*/**/*workingpaper*.md",
        "archive/session-*/**/*workingpaper*.md",
    ]
    for pat in patterns:
        for p in SESSIONS_DIR.glob(pat):
            if p.is_file() and RE_WP_FILE.match(p.name):
                seen.add(p.resolve())
    return sorted(seen)


def session_id_for(path: Path) -> str | None:
    """Extract session-NN[a-z]? token from any parent dir; return digit-prefix
    portion (without sub-letter suffix to align with edge-target convention)."""
    for parent in path.parents:
        m = RE_SESSION_DIR.match(parent.name)
        if m:
            sess = m.group(1)
            m2 = re.match(r"^(\d+)", sess)
            return (m2.group(1) if m2 else sess)
    return None


# ----------------------------------------------------------------------------
# Section splitter
# ----------------------------------------------------------------------------

def strip_code_blocks(text: str) -> str:
    """Replace fenced code blocks with blank lines preserving line-count
    so heading offsets stay valid downstream."""
    def _blank(m: re.Match[str]) -> str:
        return "\n" * m.group(0).count("\n")
    return RE_FENCED_CODE.sub(_blank, text)


def find_gate_sections(text: str) -> list[tuple[str, str]]:
    """Return [(gate_id, body_text), ...] for each gate-section in the file.

    A gate-section is any markdown heading (level 2-4) whose heading text
    contains at least one gate-ID-shaped token.  The first such token IS
    the gate ID for that section.  Body extends from the heading line to
    the next heading at SAME or HIGHER level (smaller-or-equal '#' count).
    Headings without a gate-ID token are skipped (no filename fallback).
    """
    matches = list(RE_HEADING.finditer(text))
    out: list[tuple[str, str]] = []
    for i, m in enumerate(matches):
        level = len(m.group(1))            # 2..4
        head_text = m.group(2)
        # Find the first gate-ID-shaped token in the heading.
        gid_match = RE_GATE_ID_TOKEN.search(head_text)
        if not gid_match:
            continue
        gate_id = gid_match.group(1)
        # Body ends at next heading whose level <= this one.
        body_start = m.end()
        body_end = len(text)
        for m2 in matches[i + 1:]:
            if len(m2.group(1)) <= level:
                body_end = m2.start()
                break
        body = text[body_start:body_end]
        out.append((gate_id, body))
    return out


# ----------------------------------------------------------------------------
# Edge harvesting
# ----------------------------------------------------------------------------

def harvest_pairs(
    paths: list[Path], canonical_names: set[str],
) -> tuple[list[dict], dict[str, int], set[str]]:
    """Walk every working-paper file and emit (gate, constant) pairs.

    Returns:
      edges          — list of edge dicts, deduped across the whole corpus.
      sections_per_session — map session-id -> count of gate-sections detected.
      sessions_zero_edges  — set of session ids whose WP files yielded ZERO
                             edges (reported as "unexpected" anomalies).
    """
    seen_pairs: set[tuple[str, str]] = set()
    edges: list[dict] = []
    sections_per_session: dict[str, int] = {}
    edges_per_session: dict[str, int] = {}
    sessions_seen: set[str] = set()

    n_sections_total = 0

    for p in paths:
        sess = session_id_for(p) or "?"
        sessions_seen.add(sess)
        try:
            raw = p.read_text(encoding="utf-8", errors="replace")
        except Exception:                  # noqa: BLE001
            continue
        text = strip_code_blocks(raw)

        sections = find_gate_sections(text)
        sections_per_session[sess] = (
            sections_per_session.get(sess, 0) + len(sections)
        )
        n_sections_total += len(sections)

        # Pre-locate which file/section each pair came from for the comment.
        for gate_id, body in sections:
            # Scan the section body for canonical-constant-name tokens.
            # Strict word-boundary match using the constant's own name as
            # the regex literal (re.escape).  This avoids the false-positive
            # of "M" matching inside "M_KK"; we want exact-token matches.
            #
            # Optimization: tokenize once, then membership-check.
            tokens = set(re.findall(r"\b[A-Za-z_][A-Za-z0-9_]*\b", body))
            hits = tokens & canonical_names
            if not hits:
                continue
            for const in sorted(hits):
                key = (gate_id, const)
                if key in seen_pairs:
                    continue
                seen_pairs.add(key)
                edges.append({
                    "type": "reproduces",
                    "src_type": "gates",
                    "src_id": gate_id,
                    "tgt_type": "constants",
                    "tgt_id": const,
                    "comment": (
                        f"WP-harvested: section §{gate_id} body cites "
                        f"{const} (s{sess})"
                    ),
                })
                edges_per_session[sess] = edges_per_session.get(sess, 0) + 1

    sessions_zero = {
        s for s in sessions_seen
        if edges_per_session.get(s, 0) == 0
    }

    # Report total sections via sentinel so the driver can include in summary.
    sections_per_session["__TOTAL__"] = n_sections_total
    return edges, sections_per_session, sessions_zero


# ----------------------------------------------------------------------------
# Output writer
# ----------------------------------------------------------------------------

HEADER_TEMPLATE = (
    "## Working-Paper Edges (generated by tools/harvest_workingpaper_edges.py)\n"
    "## Source: sessions/session-*/*workingpaper*.md (recursive,\n"
    "##         including sessions/archive/).\n"
    "## Conservative-harvest discipline: prefer miss over false-positive\n"
    "## (per computations/_shared/_harvest_edges.py:12-14).\n"
    "## Pairs deduped across the whole corpus (one (gate, constant) per pair).\n"
    "\n"
)


def write_edges(edges: list[dict], path: Path) -> None:
    lines: list[str] = [HEADER_TEMPLATE]
    for e in sorted(edges, key=lambda x: (x["src_id"], x["tgt_id"])):
        lines.append(
            f"[EDGE:{e['type']}] "
            f"{e['src_type']}:{e['src_id']} -> "
            f"{e['tgt_type']}:{e['tgt_id']}  # {e['comment']}\n"
        )
    path.write_text("".join(lines), encoding="utf-8")


# ----------------------------------------------------------------------------
# Driver
# ----------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--dry", action="store_true",
        help="Preview edges only; do not write output file.",
    )
    args = ap.parse_args()

    canonical_names = load_canonical_names()
    if not canonical_names:
        print("ERROR: failed to load canonical_constants vocab.")
        return 2

    paths = discover_workingpapers()
    if not paths:
        print("No working-paper files discovered.")
        return 0

    edges, sections_per_session, sessions_zero = harvest_pairs(
        paths, canonical_names,
    )

    n_total_sections = sections_per_session.pop("__TOTAL__", 0)

    if not args.dry:
        write_edges(edges, OUTPUT_PATH)

    # ----------------- Reporting -----------------
    print(f"WP files scanned       : {len(paths)}")
    print(f"Gate-sections detected : {n_total_sections}")
    print(f"Unique edges emitted   : {len(edges)}")

    if not args.dry:
        print(f"Output                 : {OUTPUT_PATH}")
    else:
        print("[dry] no output written.")

    # Top 15 constants by inbound degree.
    inbound: dict[str, int] = {}
    for e in edges:
        inbound[e["tgt_id"]] = inbound.get(e["tgt_id"], 0) + 1
    top = sorted(inbound.items(), key=lambda x: (-x[1], x[0]))[:15]
    print("\nTop 15 constants by inbound degree:")
    for name, deg in top:
        print(f"  {deg:5d}  {name}")

    if sessions_zero:
        zsorted = sorted(
            sessions_zero,
            key=lambda s: (int(s) if s.isdigit() else 99999, s),
        )
        print(f"\nSessions yielding ZERO edges (unexpected): "
              f"{', '.join(zsorted)}")
    else:
        print("\nSessions yielding ZERO edges: (none)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
