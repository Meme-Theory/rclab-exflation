#!/usr/bin/env python3
"""Dry-run edge-count driver (Phase 0 / Task #5).

Walks every session directory, routes each file through the appropriate
generation extractor from tools/_format_generation_regex_set.py, aggregates
edge counts per generation/edge-type/role/agent, and writes:

  tools/_format_generation_dry_run.json   (machine-readable per-session counts)
  tools/_format_generation_dry_run.md     (human-readable summary table)

This is the verification step before promoting to a real harvester. Output
counts inform the Phase 1 harvester implementation:
  - which generations contribute the largest edge volume
  - which edge types are well-represented vs sparse
  - which canonical agents are coverage-missing
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Iterable

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

# Import the extractor module
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

OUT_JSON = ROOT / "tools" / "_format_generation_dry_run.json"
OUT_MD = ROOT / "tools" / "_format_generation_dry_run.md"

# Generation routing — boundaries from Task #3 evidence
def session_to_generation(sid: str) -> str:
    m = re.match(r"(\d+)", sid)
    if not m:
        return "?"
    n = int(m.group(1))
    if n <= 15: return "G1"
    if n <= 18: return "G2"
    if n <= 35: return "G3"
    if n <= 60: return "G4"
    if n <= 77: return "G5"
    if n <= 81: return "G6"
    return "G7"


def extract_g1(session_id: str, all_text: str) -> list[AttributionEdge]:
    """G1 fallback: body-text mention frequency. Emits one
    `discussed_in: session → agent` edge per agent with ≥10 mentions
    OR top-3 by mention count, whichever is larger."""
    counter: Counter = Counter()
    for m in G1_AGENT_RE.finditer(all_text):
        raw = m.group(1)
        cid = canonicalize_agent(raw)
        if cid:
            counter[cid] += 1
    out: list[AttributionEdge] = []
    if not counter:
        return out
    # Top 3 or any with ≥10 mentions
    top3 = set(c for c, _ in counter.most_common(3))
    eligible = set(c for c, n in counter.items() if n >= 10)
    keep = top3 | eligible
    for agent, mentions in counter.most_common():
        if agent not in keep:
            continue
        out.append(AttributionEdge(
            edge_type="discussed_in",
            source_type="researchers",
            source_id=agent,
            target_type="sessions",
            target_id=session_id,
            role=None,
            confidence="session-level-inference",
            generation="G1",
            match_text=f"mentions={mentions}",
        ))
    return out


def find_session_dirs() -> list[tuple[str, Path, str]]:
    """Return (session_id, dir_path, location) for every session."""
    out: list[tuple[str, Path, str]] = []
    for top in [ROOT / "sessions", ROOT / "sessions" / "archive"]:
        if not top.exists():
            continue
        for d in sorted(top.glob("session-*")):
            if not d.is_dir():
                continue
            m = re.match(r"session-(\d+[a-z]?)", d.name)
            if not m:
                continue
            sid = m.group(1)
            loc = "archive" if "archive" in str(d) else "live"
            out.append((sid, d, loc))

    def sk(rec):
        m = re.match(r"(\d+)([a-z]?)", rec[0])
        return (int(m.group(1)) if m else 999, m.group(2) if m else "")
    out.sort(key=sk)
    return out


def process_session(sid: str, sess_dir: Path) -> dict:
    """Apply generation-appropriate extractors to a session directory."""
    gen = session_to_generation(sid)
    edges: list[AttributionEdge] = []
    md_files = sorted([p for p in sess_dir.glob("*.md") if p.is_file()])
    # Include workshops/ subdirectory for G7
    workshop_files = sorted([p for p in (sess_dir / "workshops").glob("*.md")
                             if p.is_file()]) if (sess_dir / "workshops").exists() else []

    if gen == "G1":
        # Concatenate all session text and run mention frequency
        all_text = "\n".join(p.read_text(encoding="utf-8", errors="ignore") for p in md_files)
        edges.extend(extract_g1(sid, all_text))

    elif gen == "G2":
        # Authors-block extraction on the master final file
        for p in md_files:
            text = p.read_text(encoding="utf-8", errors="ignore")
            edges.extend(extract_g2(text, session_id=sid))

    elif gen in ("G3", "G4", "G5"):
        # Per-file `**Author**:` / `**Evaluator**:` / `**Reviewer**:`
        # header + G5 per-gate parenthetical-in-heading + G7 `**Agent**:`
        # fallback + workshop extractor (S61+ wave-WPs have agent-pair in
        # H1 title parenthetical; older G3/G4 multi-agent workshop files
        # use `**Agents**:` body header).
        for p in md_files:
            text = p.read_text(encoding="utf-8", errors="ignore")
            file_id = f"{sid}:{p.name}"
            edges.extend(extract_g3(text, file_id=file_id, filename=p.name))
            edges.extend(extract_g5_per_gate(text, file_id=file_id))
            edges.extend(extract_g7(text, file_id=file_id))
            edges.extend(extract_workshop_g7(text, workshop_id=file_id))

    elif gen == "G6":
        # Owner-per-gate on the WP
        for p in md_files:
            text = p.read_text(encoding="utf-8", errors="ignore")
            edges.extend(extract_g6(text, file_id=f"{sid}:{p.name}"))
        # G6 also benefits from G3 author-header on the WP
        for p in md_files:
            text = p.read_text(encoding="utf-8", errors="ignore")
            edges.extend(extract_g3(text, file_id=f"{sid}:{p.name}", filename=p.name))

    elif gen == "G7":
        # Per-wave WP + per-author synthesis + workshops/
        for p in md_files:
            text = p.read_text(encoding="utf-8", errors="ignore")
            file_id = f"{sid}:{p.name}"
            edges.extend(extract_g7(text, file_id=file_id))
            # Per-author synthesis files: filename-derived author + G3 header
            edges.extend(extract_g3(text, file_id=file_id, filename=p.name))
            # Also try G6 Owner pattern (some S82+ WPs still use it)
            edges.extend(extract_g6(text, file_id=file_id))
            # And workshop extractor on top-level files too (per-wave WPs
            # with **Agents**: bullet-list pattern, or H1 title parenthetical)
            edges.extend(extract_workshop_g7(text, workshop_id=file_id))
        # Workshops subdirectory
        for p in workshop_files:
            text = p.read_text(encoding="utf-8", errors="ignore")
            workshop_id = f"{sid}:workshops/{p.stem}"
            edges.extend(extract_workshop_g7(text, workshop_id=workshop_id))

    # Per-session aggregation
    edge_type_counts: Counter = Counter()
    role_counts: Counter = Counter()
    agent_counts: Counter = Counter()
    for e in edges:
        edge_type_counts[e.edge_type] += 1
        if e.role:
            role_counts[e.role] += 1
        agent = e.source_id if e.source_type == "researchers" else (
            e.target_id if e.target_type == "researchers" else None
        )
        if agent:
            agent_counts[agent] += 1

    return {
        "sid": sid,
        "generation": gen,
        "file_count": len(md_files),
        "workshop_count": len(workshop_files),
        "total_edges": len(edges),
        "edge_type_counts": dict(edge_type_counts),
        "role_counts": dict(role_counts),
        "agent_counts": dict(agent_counts.most_common(10)),
    }


def main() -> None:
    sessions = find_session_dirs()
    rows: list[dict] = []
    for sid, sess_dir, loc in sessions:
        rec = process_session(sid, sess_dir)
        rec["location"] = loc
        rows.append(rec)

    # Per-generation aggregation
    per_gen_edge_types: dict[str, Counter] = defaultdict(Counter)
    per_gen_roles: dict[str, Counter] = defaultdict(Counter)
    per_gen_agents: dict[str, Counter] = defaultdict(Counter)
    per_gen_sessions: dict[str, list[str]] = defaultdict(list)
    per_gen_total: dict[str, int] = defaultdict(int)
    grand_total = 0
    for r in rows:
        g = r["generation"]
        per_gen_sessions[g].append(r["sid"])
        per_gen_total[g] += r["total_edges"]
        grand_total += r["total_edges"]
        for et, n in r["edge_type_counts"].items():
            per_gen_edge_types[g][et] += n
        for role, n in r["role_counts"].items():
            per_gen_roles[g][role] += n
        for ag, n in r["agent_counts"].items():
            per_gen_agents[g][ag] += n

    # Write JSON
    payload = {
        "summary": {
            "total_sessions": len(rows),
            "grand_total_edges": grand_total,
            "per_generation_total": dict(per_gen_total),
            "per_generation_edge_types": {g: dict(c) for g, c in per_gen_edge_types.items()},
            "per_generation_roles": {g: dict(c) for g, c in per_gen_roles.items()},
        },
        "per_generation_agents_top10": {
            g: dict(c.most_common(10)) for g, c in per_gen_agents.items()
        },
        "sessions": rows,
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2),
                        encoding="utf-8")

    # Console summary
    print(f"\n=== Dry-Run Summary ({len(rows)} sessions, {grand_total:,} edges total) ===\n")
    print(f"{'Gen':4} {'Sessions':>10} {'Edges':>8} {'Edges/sess':>11}  Top edge types")
    print("-" * 90)
    for g in ["G1", "G2", "G3", "G4", "G5", "G6", "G7"]:
        n_sess = len(per_gen_sessions[g])
        n_edges = per_gen_total[g]
        avg = (n_edges / n_sess) if n_sess else 0.0
        top = ", ".join(f"{t}={n}" for t, n in per_gen_edge_types[g].most_common(4))
        print(f"{g:4} {n_sess:>10} {n_edges:>8} {avg:>11.1f}  {top}")

    print("\n=== Per-generation role distribution ===\n")
    for g in ["G1", "G2", "G3", "G4", "G5", "G6", "G7"]:
        roles = per_gen_roles[g]
        if not roles:
            continue
        line = ", ".join(f"{r}={n}" for r, n in roles.most_common())
        print(f"  {g}: {line}")

    print("\n=== Per-generation top agents ===\n")
    for g in ["G1", "G2", "G3", "G4", "G5", "G6", "G7"]:
        ag = per_gen_agents[g]
        if not ag:
            continue
        line = ", ".join(f"{a}={n}" for a, n in ag.most_common(6))
        print(f"  {g}: {line}")

    print(f"\nWrote {OUT_JSON} ({OUT_JSON.stat().st_size:,}B)")

    # Write markdown summary
    md_lines: list[str] = ["# Format-generation dry-run summary", "",
                            f"Total sessions: {len(rows)}",
                            f"Grand-total edges: {grand_total:,}",
                            "",
                            "## Per-generation edge counts",
                            "",
                            "| Gen | Sessions | Edges | Edges/sess | Top edge types |",
                            "|:----|---------:|------:|-----------:|:----------------|"]
    for g in ["G1", "G2", "G3", "G4", "G5", "G6", "G7"]:
        n_sess = len(per_gen_sessions[g])
        n_edges = per_gen_total[g]
        avg = (n_edges / n_sess) if n_sess else 0.0
        top = ", ".join(f"`{t}={n}`" for t, n in per_gen_edge_types[g].most_common(4))
        md_lines.append(f"| {g} | {n_sess} | {n_edges:,} | {avg:.1f} | {top} |")
    md_lines.append("")
    md_lines.append("## Top agents per generation")
    md_lines.append("")
    for g in ["G1", "G2", "G3", "G4", "G5", "G6", "G7"]:
        ag = per_gen_agents[g]
        if not ag:
            continue
        line = ", ".join(f"`{a}` ({n})" for a, n in ag.most_common(6))
        md_lines.append(f"- **{g}**: {line}")
    md_lines.append("")
    OUT_MD.write_text("\n".join(md_lines), encoding="utf-8")
    print(f"Wrote {OUT_MD} ({OUT_MD.stat().st_size:,}B)")


if __name__ == "__main__":
    main()
