#!/usr/bin/env python3
"""Format-generation fingerprint scan (Phase 0 / Task #2).

Reads every session-N markdown file and records:
  * Per-session counts of filename archetypes (-collab, -synthesis, -workshop,
    workingpaper, -final, -master-collab, w{N}-, etc.)
  * Match counts for known author-attribution regex patterns
  * Agent-name hit density (mentions per 1KB of text)
  * Up-to-3 verbatim example match strings per pattern, per session

Output: JSON to tools/_format_generation_scan.json with per-session records,
plus a console summary table. This is the raw evidence base for the
generation-clustering step (Task #3).
"""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path
from typing import Dict, List, Tuple

ROOT = Path(__file__).resolve().parent.parent
OUT_PATH = ROOT / "tools" / "_format_generation_scan.json"

# Agent identifiers seen in the project. Includes both short tracks
# (used in filenames like baptista-collab.md) and the canonical
# subagent IDs (.claude/agents/*.md filenames).
AGENT_NAMES = [
    "baptista", "berry", "berry-geometric-phase-theorist",
    "connes", "connes-ncg-theorist",
    "cosmic-web", "cosmic-web-theorist",
    "dirac", "dirac-antimatter-theorist",
    "einstein", "einstein-theorist",
    "feynman", "feynman-theorist",
    "gen-physicist", "general", "physicist",
    "hawking", "hawking-theorist",
    "kaku", "kaku-speculative-theorist",
    "kaluza-klein", "kaluza-klein-theorist",
    "kitaev", "kitaev-quantum-chaos-theorist",
    "knowledge-weaver",
    "landau", "landau-condensed-matter-theorist",
    "little-red-dots", "little-red-dots-jwst-analyst",
    "lizzi", "lizzi-spectral-functional-theorist",
    "mack", "mack-cosmic-bridge",
    "nazarewicz", "naz", "nazarewicz-nuclear-structure-theorist",
    "neutrino-detection-specialist",
    "paasch", "paasch-mass-quantization-analyst",
    "phonon-first", "phonon-first-cosmologist",
    "quantum-acoustics", "quantum-acoustics-theorist",
    "quantum-foam", "quantum-foam-theorist",
    "sagan", "sagan-empiricist",
    "schwarzschild-penrose", "schwarzschild-penrose-geometer",
    "spectral-geometer", "geometer",
    "string-theory-theorist",
    "tesla", "tesla-resonance",
    "transit-dynamics", "transit-dynamics-theorist",
    "van-den-dungen", "van-den-dungen-bridge-theorist", "vdd", "dungen",
    "volovik", "volovik-superfluid-universe-theorist",
]
AGENT_RE = re.compile(
    r"\b(" + "|".join(re.escape(a) for a in sorted(AGENT_NAMES, key=len, reverse=True)) + r")\b",
    re.IGNORECASE,
)

# Filename archetypes
FILENAME_PATTERNS = [
    ("collab",            re.compile(r"-collab(?:-|\.md$|-addendum)")),
    ("synthesis",         re.compile(r"-synthesis(?:-|\.md$)")),
    ("workshop",          re.compile(r"-workshop(?:-|\.md$)")),
    ("workingpaper",      re.compile(r"-workingpaper\.md$")),
    ("master-synthesis",  re.compile(r"master-synthesis\.md$")),
    ("master-collab",     re.compile(r"master-collab\.md$")),
    ("results-workingpaper", re.compile(r"results-workingpaper\.md$")),
    ("final",             re.compile(r"-final\.md$")),
    ("wave-w-prefix",     re.compile(r"^session-[\dA-Za-z]+-w\d+[a-z]?")),
    ("session-final",     re.compile(r"session-[\d]+[a-z]?-final\.md$")),
    ("audit",             re.compile(r"-audit-|^audit-")),
    ("verdict",           re.compile(r"verdicts\.txt$|verdict\.md$")),
    ("sagan",             re.compile(r"sagan-(verdict|assessment|dismissal)")),
    ("quicklook",         re.compile(r"^quicklook-")),
    ("plan-block",        re.compile(r"-plan-w\d+[a-z]?\.md$")),
]

# Author-attribution patterns — read against actual file content
ATTRIBUTION_PATTERNS = [
    ("hdr-author-colon",
        re.compile(r"^(?:#+\s+)?(?:\*\*)?(?:Author|By|Authored\s*by|Synthesized\s*by|Written\s*by|Owner)(?:\*\*)?\s*:\s*(.+?)$",
                   re.IGNORECASE | re.MULTILINE)),
    ("bold-by",
        re.compile(r"\*\*(?:By|Author|Authors?)\*\*\s*:?\s*([^\n*]+)")),
    ("workshop-round",
        re.compile(r"^#+\s+(?:§\s*)?R(\d+)(?:-([A-Za-z][\w-]*))?(?:\s+([A-Za-z][\w-]+))?",
                   re.MULTILINE)),
    ("section-author-em-dash",
        re.compile(r"^#+\s+§?[\w.]+\s+[—-]\s+([a-z][\w-]+(?:-[a-z][\w-]+)*)\s*(?:$|[(\s])",
                   re.MULTILINE)),
    ("agent-block-prefix",
        re.compile(r"^#+\s+(\b(?:" + "|".join(AGENT_NAMES) + r")\b)[\s:](.+)?$",
                   re.IGNORECASE | re.MULTILINE)),
    ("provenance-block",
        re.compile(r"^>\s*\*\*Provenance\*\*:?\s*(.+?)$",
                   re.IGNORECASE | re.MULTILINE)),
    ("agent-suffix-role",
        re.compile(r"\b([a-z][\w-]+)\s+\((?:author|primary|co-author|reviewer)\b",
                   re.IGNORECASE)),
    ("primary-coauthor",
        re.compile(r"\b(PRIMARY|CO-AUTHOR|CO-SIGN|ADVERSARIAL\s+REVIEW)\s+(?:by\s+)?([a-z][\w-]+(?:-[a-z][\w-]+)*)",
                   re.IGNORECASE)),
]


def fingerprint_session(sid: str, sess_dir: Path) -> dict:
    files = sorted([p for p in sess_dir.glob("*.md") if p.is_file()])
    archetype_counts: Counter = Counter()
    file_archetypes: List[str] = []
    for p in files:
        name = p.name
        matched_any = False
        for label, pat in FILENAME_PATTERNS:
            if pat.search(name):
                archetype_counts[label] += 1
                matched_any = True
        if not matched_any:
            archetype_counts["other"] += 1
        # Extract agent-token from filename if present
        # e.g. session-22-baptista-collab.md → baptista
        agent_hits = AGENT_RE.findall(name)
        file_archetypes.append({
            "name": name,
            "size": p.stat().st_size,
            "filename_agents": list({a.lower() for a in agent_hits}),
        })

    # Content scan — read each file once, collect pattern hits + agent density
    attribution_counts: Counter = Counter()
    attribution_examples: Dict[str, List[str]] = {k: [] for k, _ in ATTRIBUTION_PATTERNS}
    agent_density: Counter = Counter()
    total_bytes = 0
    files_read = 0

    for p in files:
        try:
            text = p.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        total_bytes += len(text)
        files_read += 1
        for label, pat in ATTRIBUTION_PATTERNS:
            for m in pat.finditer(text):
                attribution_counts[label] += 1
                if len(attribution_examples[label]) < 3:
                    # Keep the full match line, capped at 200 chars
                    ex = m.group(0).strip()
                    if len(ex) > 200:
                        ex = ex[:197] + "…"
                    attribution_examples[label].append({
                        "file": p.name,
                        "match": ex,
                    })
        # Agent-name density
        for m in AGENT_RE.finditer(text):
            agent_density[m.group(1).lower()] += 1

    return {
        "sid": sid,
        "dir": str(sess_dir.relative_to(ROOT)),
        "file_count": len(files),
        "total_bytes": total_bytes,
        "archetype_counts": dict(archetype_counts),
        "attribution_counts": dict(attribution_counts),
        "attribution_examples": attribution_examples,
        "top_agents_in_content": dict(agent_density.most_common(12)),
        "files_summary": file_archetypes[:30],  # cap for JSON size
    }


def main() -> None:
    rows = []
    # Live sessions first (S52+), then archive (S01-S51).
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
            rec = fingerprint_session(sid, d)
            rec["location"] = "archive" if "archive" in str(d) else "live"
            rows.append(rec)

    def sk(r):
        m = re.match(r"(\d+)([a-z]?)", r["sid"])
        return (int(m.group(1)) if m else 999, m.group(2) if m else "")

    rows.sort(key=sk)

    OUT_PATH.write_text(
        json.dumps({"sessions": rows}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    # Console summary
    print(f"Scanned {len(rows)} sessions; wrote {OUT_PATH}")
    print()
    print(f"{'sid':>4}  {'loc':4}  {'files':>5}  {'bytes':>8}  "
          f"{'collab':>6}  {'syn':>4}  {'work':>4}  {'wp':>4}  "
          f"{'hdrAth':>6}  {'wsRnd':>5}  {'prov':>4}  {'topAgent':>15}")
    print("-" * 100)
    for r in rows:
        ar = r["archetype_counts"]
        at = r["attribution_counts"]
        ta = r["top_agents_in_content"]
        top_agent = next(iter(ta), "-")[:14] if ta else "-"
        print(f"{r['sid']:>4}  {r['location']:4}  "
              f"{r['file_count']:>5}  {r['total_bytes']:>8,}  "
              f"{ar.get('collab',0):>6}  {ar.get('synthesis',0):>4}  "
              f"{ar.get('workshop',0):>4}  {ar.get('workingpaper',0):>4}  "
              f"{at.get('hdr-author-colon',0):>6}  "
              f"{at.get('workshop-round',0):>5}  "
              f"{at.get('provenance-block',0):>4}  "
              f"{top_agent:>15}")


if __name__ == "__main__":
    main()
