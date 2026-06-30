#!/usr/bin/env python3
"""
Harvest attribution edges from session markdown files (Phase 1).

Sister harvester of `tools/harvest_archive_edges.py`. That one walks
summary/Archives/ for verdict-table edges; THIS one walks every session
directory under `sessions/` and `sessions/archive/` for author-attribution
edges across 7 format generations (G1-G7).

Reads:
  - tools/_format_generation_regex_set.py  — verified extractor module
                                              (18/18 self-test PASS)
  - sessions/session-*/*.md  + sessions/archive/session-*/*.md

Writes per session:
  - computations/s{N}_attribution_edges.txt  — `[EDGE:type] src -> tgt # comment`
                                                 (one file per session)

Writes top-level:
  - tools/harvest_attribution_edges.log       — append-mode invocation log
  - tools/harvest_attribution_edges.summary.json  — structured per-run stats

Edge types emitted (whitelisted in tools/extract_entities.py::EDGE_TYPE_CANONICAL):
  authored_by, co_authored_by, reviewed_by, participates_in, authored_round,
  cites_prior_session, discussed_in, synthesized_by, excluded_from, cited_in

Discipline (per `_harvest_edges.py:12-14` + this harvester):
  - Prefer miss over false-positive. Each emission requires regex match.
  - Idempotent: re-running overwrites per-session .txt with same content
    (modulo dedup ordering). /weave --update consumes idempotently.
  - Audit trail: every edge carries a comment with file:line + generation
    tag + pattern label so downstream auditors can re-verify.

Gate ID for this tool: ATTRIBUTION-EDGE-HARVEST (NON-PHONONIC, infrastructure).

Usage:
    "phonon-exflation-sim/.venv312/Scripts/python.exe" \\
        tools/harvest_attribution_edges.py
    "phonon-exflation-sim/.venv312/Scripts/python.exe" \\
        tools/harvest_attribution_edges.py --dry
    "phonon-exflation-sim/.venv312/Scripts/python.exe" \\
        tools/harvest_attribution_edges.py --session 86
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from _format_generation_regex_set import (   # noqa: E402
    AttributionEdge,
    G1_AGENT_RE,
    canonicalize_agent,
    extract_g2,
    extract_g3,
    extract_g5_per_gate,
    extract_g6,
    extract_g7,
    extract_workshop_g7,
)
from _format_generation_dry_run import extract_g1, session_to_generation  # noqa: E402

COMPUTATIONS_DIR = ROOT / "computations"
OUT_LOG = HERE / "harvest_attribution_edges.log"
OUT_SUMMARY = HERE / "harvest_attribution_edges.summary.json"


# ---------------------------------------------------------------------------
# Edge buffer (mirrors EdgeBuf in harvest_archive_edges.py)
# ---------------------------------------------------------------------------

class EdgeBuf:
    """Accumulator with idempotent dedup keyed on
    (type, src_type, src_id.lower(), tgt_type, tgt_id.lower())."""

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

    def add_attribution(self, edge: AttributionEdge, source_file: str) -> None:
        """Translate AttributionEdge → on-disk edge tuple.

        Source-type mapping (matches ENTITY_TYPE_ALIASES in extract_entities.py):
          - `files`            → `data_provenance` (file = data artifact)
          - `gates`            → `gates`
          - `sessions`         → `sessions`
          - `workshops`        → `data_provenance` (workshop file as data artifact)
          - `researchers`      → `researchers`
        """
        TYPE_MAP = {
            "files": "data_provenance",
            "workshops": "data_provenance",
        }
        src_type = TYPE_MAP.get(edge.source_type, edge.source_type)
        tgt_type = TYPE_MAP.get(edge.target_type, edge.target_type)
        # Audit comment: pattern label + file + generation + role
        bits = [edge.generation]
        if edge.role:
            bits.append(f"role={edge.role}")
        bits.append(f"conf={edge.confidence}")
        bits.append(f"src={source_file}")
        if edge.match_text:
            snippet = re.sub(r"\s+", " ", edge.match_text)[:80]
            bits.append(f"match={snippet!r}")
        comment = " | ".join(bits)
        self.add(edge.edge_type, src_type, edge.source_id,
                 tgt_type, edge.target_id, comment)

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


# ---------------------------------------------------------------------------
# Per-session harvester
# ---------------------------------------------------------------------------

def harvest_session(sid: str, sess_dir: Path) -> tuple[EdgeBuf, dict]:
    """Run generation-appropriate extractors on every .md file in the session.
    Returns (EdgeBuf, per-file-edge-count dict)."""
    gen = session_to_generation(sid)
    buf = EdgeBuf()
    per_file_counts: dict[str, int] = {}

    md_files = sorted([p for p in sess_dir.glob("*.md") if p.is_file()])
    workshop_files = sorted([p for p in (sess_dir / "workshops").glob("*.md")
                             if p.is_file()]) if (sess_dir / "workshops").exists() else []

    def run_one(p: Path, edges_pre: list[AttributionEdge]) -> None:
        rel = str(p.relative_to(ROOT)).replace("\\", "/")
        before = len(buf.edges)
        for e in edges_pre:
            buf.add_attribution(e, source_file=rel)
        per_file_counts[rel] = len(buf.edges) - before

    if gen == "G1":
        # G1: body-text mention frequency across all session text
        all_text = "\n".join(
            p.read_text(encoding="utf-8", errors="ignore") for p in md_files
        )
        run_one(sess_dir, extract_g1(sid, all_text))

    elif gen == "G2":
        for p in md_files:
            text = p.read_text(encoding="utf-8", errors="ignore")
            run_one(p, extract_g2(text, session_id=sid))

    elif gen in ("G3", "G4", "G5"):
        for p in md_files:
            text = p.read_text(encoding="utf-8", errors="ignore")
            file_id = f"{sid}:{p.name}"
            edges = []
            edges.extend(extract_g3(text, file_id=file_id, filename=p.name))
            edges.extend(extract_g5_per_gate(text, file_id=file_id))
            edges.extend(extract_g7(text, file_id=file_id))
            workshop_id = f"data_provenance:{p.relative_to(ROOT).as_posix()}"
            edges.extend(extract_workshop_g7(text, workshop_id=workshop_id))
            run_one(p, edges)

    elif gen == "G6":
        for p in md_files:
            text = p.read_text(encoding="utf-8", errors="ignore")
            file_id = f"{sid}:{p.name}"
            edges = []
            edges.extend(extract_g6(text, file_id=file_id))
            edges.extend(extract_g3(text, file_id=file_id, filename=p.name))
            run_one(p, edges)

    elif gen == "G7":
        for p in md_files:
            text = p.read_text(encoding="utf-8", errors="ignore")
            file_id = f"{sid}:{p.name}"
            edges = []
            edges.extend(extract_g7(text, file_id=file_id))
            edges.extend(extract_g3(text, file_id=file_id, filename=p.name))
            edges.extend(extract_g6(text, file_id=file_id))
            workshop_id = f"data_provenance:{p.relative_to(ROOT).as_posix()}"
            edges.extend(extract_workshop_g7(text, workshop_id=workshop_id))
            run_one(p, edges)
        # workshops/ subdir gets dedicated workshop extraction
        for p in workshop_files:
            text = p.read_text(encoding="utf-8", errors="ignore")
            workshop_id = p.relative_to(ROOT).as_posix()  # data_provenance:<path>
            edges = extract_workshop_g7(text, workshop_id=workshop_id)
            # ALSO run extract_g7 for **Agent**: lines inside workshop bodies
            edges.extend(extract_g7(text, file_id=workshop_id))
            run_one(p, edges)

    stats = {
        "generation": gen,
        "md_file_count": len(md_files),
        "workshop_file_count": len(workshop_files),
        "raw_edges": len(buf.edges),
        "deduped_edges": len(buf.dedup()),
        "per_file_counts": per_file_counts,
    }
    return buf, stats


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------

HEADER_TEMPLATE = (
    "## S{sess} Attribution Edges (generated by tools/harvest_attribution_edges.py)\n"
    "## Generated: {timestamp}\n"
    "## Generation: {generation}\n"
    "## Files scanned: {file_count} (+ {workshop_count} in workshops/)\n"
    "## Total edges (deduped): {edge_count}\n"
    "## Spec: sessions/framework/registry/session-format-generations.md\n"
    "## Regex module: tools/_format_generation_regex_set.py (self-test 18/18 PASS)\n"
    "\n"
)


def find_session_dirs() -> list[tuple[str, Path]]:
    out: list[tuple[str, Path]] = []
    for top in [ROOT / "sessions", ROOT / "sessions" / "archive"]:
        if not top.exists():
            continue
        for d in sorted(top.glob("session-*")):
            if not d.is_dir():
                continue
            m = re.match(r"session-(\d+[a-z]?)", d.name)
            if not m:
                continue
            out.append((m.group(1), d))

    def sk(rec):
        m = re.match(r"(\d+)([a-z]?)", rec[0])
        return (int(m.group(1)) if m else 999, m.group(2) if m else "")
    out.sort(key=sk)
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry", action="store_true",
                    help="Preview edges; do not write .txt or .log files.")
    ap.add_argument("--limit", type=int, default=0,
                    help="Limit to first N sessions (0 = all).")
    ap.add_argument("--session", type=str, default="",
                    help="Process a single session (e.g., 86 or 73a).")
    args = ap.parse_args()

    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    sessions = find_session_dirs()
    if args.session:
        sessions = [(s, d) for (s, d) in sessions if s == args.session]
    if args.limit:
        sessions = sessions[:args.limit]

    if not sessions:
        print("No sessions matched.")
        return 0

    # Aggregate counters
    total_raw = 0
    total_deduped = 0
    per_session_count: dict[str, int] = {}
    per_gen_count: Counter = Counter()
    per_edge_type: Counter = Counter()
    per_role: Counter = Counter()
    per_agent: Counter = Counter()
    written_paths: list[Path] = []
    session_stats: dict[str, dict] = {}

    for sid, sess_dir in sessions:
        buf, stats = harvest_session(sid, sess_dir)
        deduped = buf.dedup()
        total_raw += stats["raw_edges"]
        total_deduped += stats["deduped_edges"]
        per_session_count[sid] = stats["deduped_edges"]
        per_gen_count[stats["generation"]] += stats["deduped_edges"]
        for e in deduped:
            per_edge_type[e["type"]] += 1
            # role from comment (extract `role=` tag)
            mr = re.search(r"role=(\w+)", e["comment"])
            if mr:
                per_role[mr.group(1)] += 1
            # researcher mention
            for side in ("src", "tgt"):
                if e[f"{side}_type"] == "researchers":
                    per_agent[e[f"{side}_id"]] += 1
        session_stats[sid] = {
            "generation": stats["generation"],
            "md_file_count": stats["md_file_count"],
            "workshop_file_count": stats["workshop_file_count"],
            "deduped_edges": stats["deduped_edges"],
        }

        if args.dry:
            print(f"[dry] S{sid} ({stats['generation']}): "
                  f"{stats['deduped_edges']} edges")
            continue

        if not deduped:
            continue

        out_path = COMPUTATIONS_DIR / f"s{sid}_attribution_edges.txt"
        lines = [HEADER_TEMPLATE.format(
            sess=sid, timestamp=timestamp,
            generation=stats["generation"],
            file_count=stats["md_file_count"],
            workshop_count=stats["workshop_file_count"],
            edge_count=len(deduped),
        )]
        for e in deduped:
            lines.append(
                f"[EDGE:{e['type']}] "
                f"{e['src_type']}:{e['src_id']} -> "
                f"{e['tgt_type']}:{e['tgt_id']}  # {e['comment']}\n"
            )
        out_path.write_text("".join(lines), encoding="utf-8")
        written_paths.append(out_path)

    # Console summary
    print(f"\nAttribution-edge harvest ({timestamp})")
    print(f"  Sessions scanned: {len(sessions)}")
    print(f"  Raw edges:        {total_raw:,}")
    print(f"  Deduped edges:    {total_deduped:,}")
    if not args.dry:
        print(f"  Wrote {len(written_paths)} per-session .txt files at {COMPUTATIONS_DIR}/")
    print(f"\nPer generation:")
    for g in ["G1", "G2", "G3", "G4", "G5", "G6", "G7"]:
        if per_gen_count.get(g):
            print(f"  {g}: {per_gen_count[g]:,} edges")
    print(f"\nPer edge type:")
    for t, c in per_edge_type.most_common():
        print(f"  {t:25} {c:>6,}")
    print(f"\nTop 10 researchers (by edge incidence):")
    for a, c in per_agent.most_common(10):
        print(f"  {a:45} {c:>5}")

    if args.dry:
        return 0

    # Write summary JSON + append run log
    summary = {
        "timestamp": timestamp,
        "regex_module": "tools/_format_generation_regex_set.py",
        "spec": "sessions/framework/registry/session-format-generations.md",
        "sessions_scanned": len(sessions),
        "raw_edges": total_raw,
        "deduped_edges": total_deduped,
        "per_generation": dict(per_gen_count),
        "per_edge_type": dict(per_edge_type),
        "per_role": dict(per_role),
        "per_agent_top20": dict(per_agent.most_common(20)),
        "written_files": [str(p.relative_to(ROOT)).replace("\\", "/")
                          for p in written_paths],
        "session_stats": session_stats,
    }
    OUT_SUMMARY.write_text(json.dumps(summary, ensure_ascii=False, indent=2),
                            encoding="utf-8")

    log_line = (f"{timestamp}  sessions={len(sessions)}  "
                f"raw={total_raw}  deduped={total_deduped}  "
                f"files_written={len(written_paths)}\n")
    with OUT_LOG.open("a", encoding="utf-8") as f:
        f.write(log_line)

    print(f"\nWrote {OUT_SUMMARY} ({OUT_SUMMARY.stat().st_size:,}B)")
    print(f"Appended {OUT_LOG}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
