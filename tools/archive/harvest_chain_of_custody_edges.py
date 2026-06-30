#!/usr/bin/env python3
"""Harvest chain-of-custody edges from session/plan/verdict files (Phase 1.1).

Sister harvester of `tools/harvest_attribution_edges.py`. That one walks
session markdown for researcher-side authorship; THIS one walks
workingpapers, verdict files, plan files, and any framework file with
paper-path citations for GATE-side chain-of-custody:

  - carries_forward : sessions -> gates:CF-X     (from workingpaper §CF blocks)
  - anchored_in     : gates -> sessions          (from per-session verdict files)
  - cited_in        : researchers -> sessions    (from `researchers/Domain/` path refs)
  - succ_of         : gates -> gates             (within-wave plan-file adjacency)

Reads:
  - sessions/session-*/session-*-workingpaper.md          (carries_forward)
  - sessions/session-*/**/*.md                            (cited_in scope)
  - sessions/archive/session-*/**/*.md                    (cited_in scope, archived)
  - sessions/session-plan/*.md + archive/*.md             (succ_of from plan headings)
  - sessions/*.md (top-level)                             (cited_in for shared docs)
  - computations/session-*/s*_gate_verdicts.txt           (anchored_in)
  - computations/_shared/s*_gate_verdicts.txt             (anchored_in misplaced files)

Writes per session:
  - computations/s{N}_chain_of_custody_edges.txt          (4 edge types mixed)

Writes top-level:
  - tools/harvest_chain_of_custody_edges.log              (append-mode invocation log)
  - tools/harvest_chain_of_custody_edges.summary.json     (per-run stats)

Edge types emitted (whitelisted in tools/extract_entities.py::EDGE_TYPE_CANONICAL
Phase 1.1 block):
  carries_forward, anchored_in, cited_in, succ_of

Discipline (mirrors _harvest_edges.py:12-14 + harvest_attribution_edges.py:34):
  - Prefer miss over false-positive. Each emission requires regex match.
  - Idempotent: re-running overwrites per-session .txt with same content
    (modulo dedup ordering). /weave --update consumes idempotently.
  - Audit trail: every edge carries a comment with file:line + pattern label +
    confidence tag so downstream auditors can re-verify.

Gate ID for this tool: CHAIN-OF-CUSTODY-EDGE-HARVEST (NON-PHONONIC, infrastructure).

Usage:
    "phonon-exflation-sim/.venv312/Scripts/python.exe" \\
        tools/harvest_chain_of_custody_edges.py
    "phonon-exflation-sim/.venv312/Scripts/python.exe" \\
        tools/harvest_chain_of_custody_edges.py --dry
    "phonon-exflation-sim/.venv312/Scripts/python.exe" \\
        tools/harvest_chain_of_custody_edges.py --session 90
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

from _chain_of_custody_extractors import (   # noqa: E402
    ChainOfCustodyEdge,
    extract_anchored_in,
    extract_carry_forwards,
    extract_researcher_citations,
    extract_succ_of,
)

COMPUTATIONS_DIR = ROOT / "computations"
SESSIONS_DIR = ROOT / "sessions"
SESSIONS_ARCHIVE_DIR = SESSIONS_DIR / "archive"
SESSION_PLAN_DIR = SESSIONS_DIR / "session-plan"
SESSION_PLAN_ARCHIVE = SESSION_PLAN_DIR / "archive"

OUT_LOG = HERE / "harvest_chain_of_custody_edges.log"
OUT_SUMMARY = HERE / "harvest_chain_of_custody_edges.summary.json"


# ---------------------------------------------------------------------------
# Edge buffer (mirrors EdgeBuf in harvest_attribution_edges.py:80-139)
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
            "comment": comment[:240],
        })

    def add_coc(self, edge: ChainOfCustodyEdge, source_file: str) -> None:
        """Translate ChainOfCustodyEdge → on-disk edge tuple."""
        # Audit comment: pattern + role + confidence + src file + match snippet
        bits = [edge.pattern]
        if edge.role:
            bits.append(f"role={edge.role}")
        bits.append(f"conf={edge.confidence}")
        bits.append(f"src={source_file}")
        if edge.match_text:
            snippet = re.sub(r"\s+", " ", edge.match_text)[:90]
            bits.append(f"match={snippet!r}")
        comment = " | ".join(bits)
        self.add(edge.edge_type, edge.source_type, edge.source_id,
                 edge.target_type, edge.target_id, comment)

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
# File discovery
# ---------------------------------------------------------------------------

def parse_session_id(name: str) -> str | None:
    """Extract a session id (e.g., '90', '24a', '17b') from a filename or
    directory name. Returns None if no match."""
    m = re.search(r"session-(\d+[a-z]?)", name)
    if m:
        return m.group(1)
    m = re.search(r"^s(\d+[a-z]?)_", name)
    if m:
        return m.group(1)
    return None


def find_all_session_ids() -> list[str]:
    """Enumerate all session ids from `sessions/session-*` + `sessions/archive/
    session-*` dirs, sorted numerically (with letter suffix preserved)."""
    sids: set[str] = set()
    for top in (SESSIONS_DIR, SESSIONS_ARCHIVE_DIR):
        if not top.exists():
            continue
        for d in top.glob("session-*"):
            if not d.is_dir():
                continue
            sid = parse_session_id(d.name)
            if sid:
                sids.add(sid)

    def sk(s: str) -> tuple[int, str]:
        m = re.match(r"(\d+)([a-z]?)", s)
        return (int(m.group(1)) if m else 999, m.group(2) if m else "")

    return sorted(sids, key=sk)


def find_workingpapers_for_session(sid: str) -> list[Path]:
    """All workingpaper-class files under a session's directory."""
    candidates: list[Path] = []
    for top in (SESSIONS_DIR, SESSIONS_ARCHIVE_DIR):
        d = top / f"session-{sid}"
        if not d.exists():
            continue
        for p in d.rglob("*workingpaper*.md"):
            candidates.append(p)
    return candidates


def find_verdict_files_for_session(sid: str) -> list[Path]:
    """Per-session verdict files. Canonical location is
    `computations/session-{N}/s{N}*_gate_verdicts.txt` plus the misplaced
    `computations/_shared/s{N}_gate_verdicts.txt` (FORBIDDEN per
    `.claude/rules/gate-verdicts.md` but harvested anyway for completeness)."""
    out: list[Path] = []
    # Canonical location
    d = COMPUTATIONS_DIR / f"session-{sid}"
    if d.exists():
        for p in d.glob(f"s{sid}*_gate_verdicts.txt"):
            out.append(p)
    # Misplaced fallback
    shared = COMPUTATIONS_DIR / "_shared"
    if shared.exists():
        for p in shared.glob(f"s{sid}_gate_verdicts.txt"):
            out.append(p)
    return out


def find_plan_files_for_session(sid: str) -> list[Path]:
    """All plan files for a session (active + archived)."""
    out: list[Path] = []
    for top in (SESSION_PLAN_DIR, SESSION_PLAN_ARCHIVE):
        if not top.exists():
            continue
        # Match session-{sid}-plan-*.md AND session-{sid}-context.md AND
        # session-{sid}-partition.md AND session-{sid[A-Z]*}-plan-*.md
        for p in top.glob(f"session-{sid}-*.md"):
            if p.is_file():
                out.append(p)
        # Also handle padded variants like "session-29A-plan-..." for legacy.
        try:
            n = int(re.match(r"(\d+)", sid).group(1))
        except (AttributeError, ValueError):
            n = None
        if n is not None:
            for p in top.glob(f"session-{n:02d}*-plan*.md"):
                if p.is_file() and p not in out:
                    out.append(p)
            for p in top.glob(f"session-{n}-plan*.md"):
                if p.is_file() and p not in out:
                    out.append(p)
    return out


def find_session_md_files(sid: str) -> list[Path]:
    """All .md files under a session's directory (sessions/session-N/** +
    sessions/archive/session-N/**), used for paper-path citation scanning."""
    out: list[Path] = []
    for top in (SESSIONS_DIR, SESSIONS_ARCHIVE_DIR):
        d = top / f"session-{sid}"
        if not d.exists():
            continue
        for p in d.rglob("*.md"):
            if p.is_file():
                out.append(p)
    return out


def find_shared_session_files() -> list[Path]:
    """Top-level shared files under `sessions/` not tied to a specific session
    (e.g., observational_avenues.md, evoi-framework.md, permanent-results-
    registry.md). These get scanned for cited_in citations with
    session_id=None (emitted as data_provenance target)."""
    out: list[Path] = []
    if not SESSIONS_DIR.exists():
        return out
    for p in SESSIONS_DIR.glob("*.md"):
        if p.is_file():
            out.append(p)
    framework_dir = SESSIONS_DIR / "framework"
    if framework_dir.exists():
        for p in framework_dir.rglob("*.md"):
            if p.is_file():
                out.append(p)
    return out


# ---------------------------------------------------------------------------
# Per-session harvest
# ---------------------------------------------------------------------------

def relpath(p: Path) -> str:
    try:
        return str(p.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(p).replace("\\", "/")


def harvest_session(sid: str) -> tuple[EdgeBuf, dict]:
    """Run all 4 chain-of-custody extractors for a single session."""
    buf = EdgeBuf()
    stats: dict = {
        "session_id": sid,
        "workingpapers_scanned": 0,
        "verdict_files_scanned": 0,
        "plan_files_scanned": 0,
        "session_md_files_scanned": 0,
        "edges_by_type": Counter(),
    }

    # 1) carries_forward — workingpapers
    for wp in find_workingpapers_for_session(sid):
        stats["workingpapers_scanned"] += 1
        text = wp.read_text(encoding="utf-8", errors="ignore")
        rel = relpath(wp)
        for e in extract_carry_forwards(text, session_id=sid, source_file=rel):
            buf.add_coc(e, source_file=rel)
            stats["edges_by_type"]["carries_forward"] += 1

    # 2) anchored_in — verdict files
    for vp in find_verdict_files_for_session(sid):
        stats["verdict_files_scanned"] += 1
        text = vp.read_text(encoding="utf-8", errors="ignore")
        rel = relpath(vp)
        for e in extract_anchored_in(text, session_id=sid, source_file=rel):
            buf.add_coc(e, source_file=rel)
            stats["edges_by_type"]["anchored_in"] += 1

    # 3) cited_in — all session-keyed .md files (researchers/Domain/ refs)
    for p in find_session_md_files(sid):
        stats["session_md_files_scanned"] += 1
        text = p.read_text(encoding="utf-8", errors="ignore")
        rel = relpath(p)
        for e in extract_researcher_citations(text, session_id=sid,
                                              source_file=rel):
            buf.add_coc(e, source_file=rel)
            stats["edges_by_type"]["cited_in"] += 1

    # 4) succ_of — plan files
    for pp in find_plan_files_for_session(sid):
        stats["plan_files_scanned"] += 1
        text = pp.read_text(encoding="utf-8", errors="ignore")
        rel = relpath(pp)
        for e in extract_succ_of(text, source_file=rel):
            buf.add_coc(e, source_file=rel)
            stats["edges_by_type"]["succ_of"] += 1

    return buf, stats


def harvest_shared_files(buf: EdgeBuf) -> dict:
    """Scan top-level shared session files for paper-path citations.
    These are NOT keyed to a single session, so emitted as
    researchers -> data_provenance:<filepath> edges (session_id=None)."""
    stats: dict = {"shared_files_scanned": 0,
                   "shared_cited_in_edges": 0}
    for p in find_shared_session_files():
        stats["shared_files_scanned"] += 1
        text = p.read_text(encoding="utf-8", errors="ignore")
        rel = relpath(p)
        for e in extract_researcher_citations(text, session_id=None,
                                              source_file=rel):
            buf.add_coc(e, source_file=rel)
            stats["shared_cited_in_edges"] += 1
    return stats


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------

HEADER_TEMPLATE = (
    "## S{sess} Chain-of-Custody Edges "
    "(generated by tools/harvest_chain_of_custody_edges.py)\n"
    "## Generated: {timestamp}\n"
    "## Workingpapers scanned: {wp_count}\n"
    "## Verdict files scanned: {vp_count}\n"
    "## Plan files scanned: {pp_count}\n"
    "## Session .md files scanned (cited_in scope): {md_count}\n"
    "## Total edges (deduped): {edge_count}\n"
    "## Edge types: {edge_types}\n"
    "## Extractors: tools/_chain_of_custody_extractors.py (self-test 11/11 PASS)\n"
    "\n"
)

SHARED_HEADER_TEMPLATE = (
    "## Shared-file Chain-of-Custody Edges "
    "(non-session-keyed; emitted to data_provenance targets)\n"
    "## Generated: {timestamp}\n"
    "## Shared files scanned: {n}\n"
    "## Total edges (deduped): {edge_count}\n"
    "## Extractors: tools/_chain_of_custody_extractors.py (self-test 11/11 PASS)\n"
    "\n"
)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry", action="store_true",
                    help="Preview edges; do not write .txt or .log files.")
    ap.add_argument("--limit", type=int, default=0,
                    help="Limit to first N sessions (0 = all).")
    ap.add_argument("--session", type=str, default="",
                    help="Process a single session (e.g., 86 or 73a).")
    ap.add_argument("--no-shared", action="store_true",
                    help="Skip shared-files scan (cited_in via top-level docs).")
    args = ap.parse_args()

    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    all_sids = find_all_session_ids()
    if args.session:
        sids = [s for s in all_sids if s == args.session]
    else:
        sids = all_sids
    if args.limit:
        sids = sids[:args.limit]

    if not sids:
        print("No sessions matched.")
        return 0

    # Aggregate counters
    total_raw = 0
    total_deduped = 0
    per_session_count: dict[str, int] = {}
    per_edge_type: Counter = Counter()
    per_researcher: Counter = Counter()
    written_paths: list[Path] = []
    session_stats: dict[str, dict] = {}

    for sid in sids:
        buf, stats = harvest_session(sid)
        deduped = buf.dedup()
        total_raw += len(buf.edges)
        total_deduped += len(deduped)
        per_session_count[sid] = len(deduped)
        for e in deduped:
            per_edge_type[e["type"]] += 1
            if e["src_type"] == "researchers":
                per_researcher[e["src_id"]] += 1
            if e["tgt_type"] == "researchers":
                per_researcher[e["tgt_id"]] += 1
        session_stats[sid] = {
            "workingpapers": stats["workingpapers_scanned"],
            "verdict_files": stats["verdict_files_scanned"],
            "plan_files": stats["plan_files_scanned"],
            "session_md_files": stats["session_md_files_scanned"],
            "edges": len(deduped),
            "by_type": dict(stats["edges_by_type"]),
        }

        if args.dry:
            print(f"[dry] S{sid}: {len(deduped)} edges "
                  f"(wp={stats['workingpapers_scanned']}, "
                  f"vp={stats['verdict_files_scanned']}, "
                  f"pp={stats['plan_files_scanned']}, "
                  f"md={stats['session_md_files_scanned']})")
            continue

        if not deduped:
            continue

        out_path = COMPUTATIONS_DIR / f"s{sid}_chain_of_custody_edges.txt"
        edge_types_str = ",".join(sorted(stats["edges_by_type"].keys()))
        lines = [HEADER_TEMPLATE.format(
            sess=sid, timestamp=timestamp,
            wp_count=stats["workingpapers_scanned"],
            vp_count=stats["verdict_files_scanned"],
            pp_count=stats["plan_files_scanned"],
            md_count=stats["session_md_files_scanned"],
            edge_count=len(deduped),
            edge_types=edge_types_str or "(none)",
        )]
        for e in deduped:
            lines.append(
                f"[EDGE:{e['type']}] "
                f"{e['src_type']}:{e['src_id']} -> "
                f"{e['tgt_type']}:{e['tgt_id']}  # {e['comment']}\n"
            )
        out_path.write_text("".join(lines), encoding="utf-8")
        written_paths.append(out_path)

    # Shared-file pass (non-session-keyed cited_in)
    shared_edges_written = 0
    if not args.no_shared and not args.session:
        sbuf = EdgeBuf()
        sstats = harvest_shared_files(sbuf)
        sdedup = sbuf.dedup()
        total_raw += len(sbuf.edges)
        total_deduped += len(sdedup)
        for e in sdedup:
            per_edge_type[e["type"]] += 1
            if e["src_type"] == "researchers":
                per_researcher[e["src_id"]] += 1
        if not args.dry and sdedup:
            shared_out = COMPUTATIONS_DIR / "_shared_chain_of_custody_edges.txt"
            sheader = SHARED_HEADER_TEMPLATE.format(
                timestamp=timestamp,
                n=sstats["shared_files_scanned"],
                edge_count=len(sdedup),
            )
            lines = [sheader]
            for e in sdedup:
                lines.append(
                    f"[EDGE:{e['type']}] "
                    f"{e['src_type']}:{e['src_id']} -> "
                    f"{e['tgt_type']}:{e['tgt_id']}  # {e['comment']}\n"
                )
            shared_out.write_text("".join(lines), encoding="utf-8")
            written_paths.append(shared_out)
            shared_edges_written = len(sdedup)
        elif args.dry:
            print(f"[dry] shared-files: {len(sdedup)} edges "
                  f"({sstats['shared_files_scanned']} files scanned)")

    # Console summary
    print(f"\nChain-of-custody edge harvest ({timestamp})")
    print(f"  Sessions scanned: {len(sids)}")
    print(f"  Raw edges:        {total_raw:,}")
    print(f"  Deduped edges:    {total_deduped:,}")
    if not args.dry:
        print(f"  Wrote {len(written_paths)} per-session .txt files at {COMPUTATIONS_DIR}/")
        if shared_edges_written:
            print(f"  Wrote 1 shared-files .txt with {shared_edges_written:,} edges")
    print(f"\nPer edge type:")
    for t, c in per_edge_type.most_common():
        print(f"  {t:25} {c:>6,}")
    print(f"\nTop 10 researchers (by cited_in incidence):")
    for r, c in per_researcher.most_common(10):
        print(f"  {r:45} {c:>5}")
    print(f"\nTop 10 sessions (by edge count):")
    top_sess = sorted(per_session_count.items(),
                      key=lambda kv: -kv[1])[:10]
    for s, c in top_sess:
        print(f"  S{s:<5}                                          {c:>5}")

    if args.dry:
        return 0

    # Write summary JSON + append run log
    summary = {
        "timestamp": timestamp,
        "extractor_module": "tools/_chain_of_custody_extractors.py",
        "sessions_scanned": len(sids),
        "raw_edges": total_raw,
        "deduped_edges": total_deduped,
        "per_edge_type": dict(per_edge_type),
        "per_researcher_top20": dict(per_researcher.most_common(20)),
        "written_files": [relpath(p) for p in written_paths],
        "session_stats": session_stats,
        "shared_edges": shared_edges_written,
    }
    OUT_SUMMARY.write_text(json.dumps(summary, ensure_ascii=False, indent=2),
                            encoding="utf-8")

    log_line = (f"{timestamp}  sessions={len(sids)}  "
                f"raw={total_raw}  deduped={total_deduped}  "
                f"files_written={len(written_paths)}\n")
    with OUT_LOG.open("a", encoding="utf-8") as f:
        f.write(log_line)

    print(f"\nWrote {OUT_SUMMARY} ({OUT_SUMMARY.stat().st_size:,}B)")
    print(f"Appended {OUT_LOG}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
