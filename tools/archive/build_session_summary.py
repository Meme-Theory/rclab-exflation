"""Canonical session-summary builder.

Concatenates every post-workshop .md file in `sessions/session-{ID}/` into a
single comprehensive summary at `summary/session-{ID}-final.md`. Verbatim:
no edits, no truncation, no paraphrasing.

Usage
-----
    python tools/build_session_summary.py 76
    python tools/build_session_summary.py 73a 73b
    python tools/build_session_summary.py 76 77 78 79 80 81 82 83 84

Auto-classifies each .md file into one of four sections by filename pattern:

    MASTER   — master-collab, master-workshop-synthesis, way-forward,
               synthesis-collation, cross-workshop, post-workshop,
               framework-update, rf-analysis, pre-registration,
               phonon-vs-data-plan, bare `session-N-synthesis.md`
    WORKSHOP — *-workshop.md, *-workshop-synthesis.md, *-singularity-review,
               *-review.md (singular reviewer-led documents)
    PER_AGENT — *-{agent}-collab.md (incl. workshop-{agent}-collab),
                *-{agent}-synthesis.md (per-agent, not master),
                *audit*, *dismissal-ack*
    OUTPUTS  — results-workingpaper, outputs, extraction, verdicts,
               OOM, phonon-vs-data-plan-when-not-master

Aborts loudly on any file that fails to classify (forces explicit handling
of new naming patterns rather than silent omission).

Design choices that compensate for divergences across the 9 agent-built
helpers this script replaces:

- Read in BINARY then decode utf-8 with errors="replace" — preserves source
  bytes; never loses a line silently. (S72 pattern, recommended over S70's
  text-mode-CRLF-normalization which produced disk-byte vs content-byte
  discrepancies.)
- Write with newline="\\n" — output is consistently LF, matching markdown-
  renderer expectations and matching what 10 of 11 batch-2 outputs produced.
- Per-file marker is `### {filename}` immediately followed by content, then
  a blank line. No per-file `---` separator — keeps overhead small (~500B
  per file) and matches S72's tight-overhead pattern.
- Files within each section are sorted alphabetically — deterministic,
  reproducible output across runs.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Dict, List

ROOT = Path(__file__).resolve().parent.parent
SESSIONS_DIR = ROOT / "sessions"
SUMMARY_DIR = ROOT / "summary"

SECTIONS = ("master", "workshop", "per_agent", "outputs")
SECTION_HEADER = {
    "master": "## Master Post-Workshop Synthesis",
    "workshop": "## Workshop Documents",
    "per_agent": "## Per-Agent Reviewer Collabs",
    "outputs": "## Outputs / Gate Verdicts / Computational Results",
}

MASTER_EXPLICIT_PATTERNS = (
    "master-collab",
    "master-workshop-synthesis",
    "master-synthesis",
    "way-forward",
    "synthesis-collation",
    "cross-workshop",
    "post-workshop",
    "framework-update",
    "rf-analysis",
    "phonon-vs-data-plan",
    "workshop-schedule",
)
MASTER_BARE_TOPIC_PATTERNS = (
    "pre-registration",
    "pre_registration",
    "pause-resume",
    "phase-plan",
    "cc-revisit",
    "phononic-engine-precursor",
)
OUTPUTS_PATTERNS = (
    "results-workingpaper",
    "-workingpaper",
    "extraction",
    "verdicts",
    "oom",
    "settings-diff",
)
BARE_MASTER_FILE_RE = re.compile(r"^session-\d+[a-z]?-(synthesis|final)$")


def classify(filename: str) -> str:
    """Return one of: master | workshop | per_agent | outputs | unknown.

    Priority order is critical:
    P1. Bare `session-N-(synthesis|final).md` → master  (session-71-synthesis,
        session-79-final).
    P2. Explicit master keywords → master  (master-collab, synthesis-collation,
        workshop-schedule, etc. — these win over generic substring matches).
    P3. Bare topic-master files (no per-agent suffix) → master  (CC-revisit,
        phononic-engine-precursor, pause-resume, phase-plan, pre-registration).
        Guarded by absence of -synthesis/-collab/-audit suffix so that
        transit-CCrevisit-synthesis correctly falls through to per-agent.
    P4. Per-agent suffix → per_agent  (-collab, -synthesis except
        -workshop-synthesis, audit substring, ack suffix).
    P5. Outputs (BEFORE workshop, so extraction-workshops goes to outputs not
        workshop).
    P6. Workshop suffix/substring/-review → workshop.
    """
    if not filename.endswith(".md"):
        return "unknown"
    stem = filename[:-3].lower()

    if BARE_MASTER_FILE_RE.match(stem):
        return "master"

    for pat in MASTER_EXPLICIT_PATTERNS:
        if pat in stem:
            return "master"

    has_per_agent_suffix = (
        stem.endswith("-synthesis")
        or stem.endswith("-collab")
        or "audit" in stem
    )
    if not has_per_agent_suffix:
        for pat in MASTER_BARE_TOPIC_PATTERNS:
            if pat in stem:
                return "master"

    if stem.endswith("-collab"):
        return "per_agent"
    if stem.endswith("-synthesis") and not stem.endswith("-workshop-synthesis"):
        return "per_agent"
    if "audit" in stem:
        return "per_agent"
    if "dismissal-ack" in stem or stem.endswith("-ack"):
        return "per_agent"

    for pat in OUTPUTS_PATTERNS:
        if pat in stem:
            return "outputs"
    if "outputs" in stem:
        return "outputs"

    if stem.endswith("-workshop") or stem.endswith("-workshop-synthesis"):
        return "workshop"
    if "-workshop" in stem:
        return "workshop"
    if stem.endswith("-review") or "-singularity-review" in stem:
        return "workshop"

    return "unknown"


def read_verbatim(path: Path) -> str:
    """Read a source file as bytes then decode utf-8 with replacement.

    Binary-then-decode preserves all source bytes; errors='replace' guarantees
    no silent byte loss on files that contain non-utf8 sequences.
    """
    return path.read_bytes().decode("utf-8", errors="replace")


def build_summary(session_id: str) -> Dict[str, object]:
    """Build summary/session-{session_id}-final.md from sessions/session-{session_id}/.

    Returns a dict reporting: out_path, out_bytes, source_count, sources_by_section,
    total_source_bytes, overhead_bytes.
    """
    src_dir = SESSIONS_DIR / f"session-{session_id}"
    if not src_dir.is_dir():
        raise FileNotFoundError(f"Session folder not found: {src_dir}")

    out_path = SUMMARY_DIR / f"session-{session_id}-final.md"
    SUMMARY_DIR.mkdir(parents=True, exist_ok=True)

    md_files = sorted(p.name for p in src_dir.glob("*.md"))
    if not md_files:
        raise RuntimeError(f"No .md files found in {src_dir}")

    buckets: Dict[str, List[str]] = {s: [] for s in SECTIONS}
    unknown: List[str] = []
    for fn in md_files:
        section = classify(fn)
        if section == "unknown":
            unknown.append(fn)
        else:
            buckets[section].append(fn)

    if unknown:
        raise RuntimeError(
            f"Cannot classify these files in {src_dir}:\n  "
            + "\n  ".join(unknown)
            + "\nAdd a pattern to classify() or rename the file."
        )

    all_sources = sum((buckets[s] for s in SECTIONS), [])

    parts: List[str] = []
    parts.append(f"# Session {session_id} — Comprehensive Summary\n\n")
    parts.append(f"_Built from: {', '.join(all_sources)}_\n\n")
    parts.append("---\n\n")

    for section in SECTIONS:
        parts.append(f"{SECTION_HEADER[section]}\n\n")
        files = buckets[section]
        if not files:
            parts.append("_(none)_\n\n")
        else:
            for fn in files:
                body = read_verbatim(src_dir / fn)
                parts.append(f"### {fn}\n\n")
                parts.append(body)
                if not body.endswith("\n"):
                    parts.append("\n")
                parts.append("\n")
        parts.append("---\n\n")

    content = "".join(parts)

    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)

    out_bytes = out_path.stat().st_size
    total_source_bytes = sum((src_dir / fn).stat().st_size for fn in all_sources)

    return {
        "session_id": session_id,
        "out_path": str(out_path),
        "out_bytes": out_bytes,
        "source_count": len(all_sources),
        "sources_by_section": {s: list(buckets[s]) for s in SECTIONS},
        "total_source_bytes": total_source_bytes,
        "overhead_bytes": out_bytes - total_source_bytes,
    }


def main(argv: List[str]) -> int:
    if len(argv) < 2:
        print(__doc__)
        return 1

    session_ids = argv[1:]
    for sid in session_ids:
        try:
            report = build_summary(sid)
        except (FileNotFoundError, RuntimeError) as e:
            print(f"[FAIL] session-{sid}: {e}")
            return 2

        print(f"[OK] session-{sid}-final.md")
        print(f"     out_bytes:          {report['out_bytes']:>10}")
        print(f"     total_source_bytes: {report['total_source_bytes']:>10}")
        print(f"     overhead_bytes:     {report['overhead_bytes']:>10}")
        print(f"     source_count:       {report['source_count']:>10}")
        for section in SECTIONS:
            files = report["sources_by_section"][section]
            print(f"     {section:>9}: {len(files):>2} file(s)")
            for fn in files:
                print(f"         {fn}")
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
