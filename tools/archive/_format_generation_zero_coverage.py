#!/usr/bin/env python3
"""Zero-coverage report (Phase 0.9).

For every .md file in every session directory (including workshops/ subdir),
runs the generation-appropriate extractor against that file individually and
records files that emit ZERO attribution edges. Categorizes by apparent
reason:

  - SYSTEM-FILE      : scaffolding / index / framework-anchored files where
                       attribution is not expected by design
  - PRE-G3-NARRATIVE : G1 sessions where no formal attribution exists
  - DATA-ONLY        : file is mostly tables, scripts, or short stubs
  - FORMAT-MISS      : file SHOULD have attribution but no regex fired —
                       these are the highest-signal candidates for either
                       (a) regex refinement OR (b) orphan content surfaced

Output:
  tools/_format_generation_zero_coverage.json  (machine-readable)
  tools/_format_generation_zero_coverage.md    (human-readable; FORMAT-MISS
                                                files surfaced first)
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from _format_generation_regex_set import (   # noqa: E402
    extract_g2,
    extract_g3,
    extract_g5_per_gate,
    extract_g6,
    extract_g7,
    extract_workshop_g7,
)
from _format_generation_dry_run import session_to_generation   # noqa: E402

OUT_JSON = ROOT / "tools" / "_format_generation_zero_coverage.json"
OUT_MD = ROOT / "tools" / "_format_generation_zero_coverage.md"

# Heuristics for categorization
SYSTEM_FILE_PATTERNS = [
    re.compile(r"^evoi-framework\.md$"),
    re.compile(r"^compute-carryforward\.md$"),
    re.compile(r"^results-index\.md$"),
    re.compile(r"session-[\d]+[a-z]?-results-index\.md$"),
    re.compile(r"session-[\d]+[a-z]?-plan-w[\d]+[a-z]?\.md$"),
    re.compile(r"session-[\d]+[a-z]?-workshop-schedule(-w[\d]+)?\.md$"),
    re.compile(r"^_seed-"),
    re.compile(r"session-[\d]+[a-z]?-pending-edits-ledger\.md$"),
    re.compile(r"^s\d+-pending-edits-ledger\.md$"),
    re.compile(r"path-[abcdef]-carry-forward\.md$"),
    re.compile(r"session-[\d]+[a-z]?-OOM\.md$"),
    re.compile(r"^c1_(?:exflation|GR)_proposal\.md$"),
]


def is_system_file(name: str) -> bool:
    return any(p.search(name) for p in SYSTEM_FILE_PATTERNS)


def is_shell_file(text: str) -> bool:
    """Detect SHELL CREATED markers in plan-style WPs (S87+ pattern)."""
    head = text[:1500]
    if re.search(r"\bSHELL\s+CREATED\b", head, re.IGNORECASE):
        return True
    if re.search(r"\*\*Status\*\*:\s*SHELL", head, re.IGNORECASE):
        return True
    if re.search(r"awaiting\s+runtime\s+compute\s+dispatch", head, re.IGNORECASE):
        return True
    return False


# Workshop-filename pair extractor — runs against filename when body has
# no **Agents**: line. Pattern: session-N-{a}-{b}-workshop.md or
# session-N-{a}-{b}-{topic}-workshop.md. The {a}/{b} are agent-name tokens.
WORKSHOP_FILENAME_PAIR_RE = re.compile(
    r"^session-\d+[a-z]?-"
    r"(?P<a>[a-z][\w-]*?)"
    r"-(?P<b>[a-z][\w-]*?)"
    r"(?:-[a-z][\w-]*)?"          # optional topic mid-fix
    r"-workshop(?:s)?\.md$",
    re.IGNORECASE,
)


def is_data_only(text: str) -> bool:
    """Heuristic: file is data-only if (a) <2KB OR (b) ratio of pipe-table
    characters to total chars > 0.1, suggesting dominant-table content."""
    if len(text) < 2000:
        return True
    pipe = text.count("|")
    if pipe / max(len(text), 1) > 0.10:
        return True
    return False


def detect_first_header(text: str) -> str:
    """Return the first H1/H2 heading found (for context)."""
    m = re.search(r"^#{1,2}\s+(.+?)$", text, re.MULTILINE)
    return m.group(1).strip()[:120] if m else ""


def run_extractors_on_file(text: str, gen: str, file_id: str,
                            filename: str) -> int:
    """Run generation-appropriate extractors on ONE file's text and return
    the count of attribution edges emitted. Any file with -workshop in name
    additionally runs the workshop extractor (body **Agents**: line +
    `## Round N — agent:` headings) and the filename-pair fallback."""
    edges = []
    if gen == "G2":
        edges += extract_g2(text, session_id="(file-scoped)")
    if gen in ("G3", "G4", "G5"):
        edges += extract_g3(text, file_id=file_id, filename=filename)
        edges += extract_g5_per_gate(text, file_id=file_id)
        # G7 `**Agent**:` pattern fires universally — appears in S25+ files
        # even though it dominates in S82+. Run it as a fallback.
        edges += extract_g7(text, file_id=file_id)
    if gen == "G6":
        edges += extract_g6(text, file_id=file_id)
        edges += extract_g3(text, file_id=file_id, filename=filename)
    if gen == "G7":
        edges += extract_g7(text, file_id=file_id)
        edges += extract_g3(text, file_id=file_id, filename=filename)
        edges += extract_g6(text, file_id=file_id)
    # Workshop extractor — runs UNIVERSALLY on every file. The workshop
    # format (**Agents**: + ## Round N + G5 title-parenthetical) is
    # carrier-agnostic: workshop files live in workshops/ subdir for G7,
    # at the session-top-level for G5, and wave-WPs (no -workshop in
    # name) carry agent-pair-in-title for S61.
    edges += extract_workshop_g7(text, workshop_id=file_id)
    # Filename-pair fallback: even if body parse fires nothing, the
    # filename pattern session-N-{a}-{b}-workshop.md attributes BOTH
    # agents as participants.
    if not edges:
        fm = WORKSHOP_FILENAME_PAIR_RE.match(filename)
        if fm:
            from _format_generation_regex_set import canonicalize_agent
            for raw in (fm.group("a"), fm.group("b")):
                if canonicalize_agent(raw):
                    edges.append("filename-pair")  # sentinel
    return len(edges)


def main() -> None:
    zero_files: list[dict] = []
    total_files = 0
    per_category: Counter = Counter()

    # Walk all sessions
    session_dirs: list[tuple[str, Path, str]] = []
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
            session_dirs.append((sid, d, loc))

    def sk(rec):
        m = re.match(r"(\d+)([a-z]?)", rec[0])
        return (int(m.group(1)) if m else 999, m.group(2) if m else "")
    session_dirs.sort(key=sk)

    for sid, sess_dir, loc in session_dirs:
        gen = session_to_generation(sid)
        # Top-level md files
        files = sorted([p for p in sess_dir.glob("*.md") if p.is_file()])
        # workshops/ subdir
        workshop_files = sorted([p for p in (sess_dir / "workshops").glob("*.md")
                                 if p.is_file()]) if (sess_dir / "workshops").exists() else []
        for p in files + workshop_files:
            total_files += 1
            text = p.read_text(encoding="utf-8", errors="ignore")
            file_id = f"S{sid}:{p.relative_to(sess_dir)}"

            # Try generation extractor + try workshop extractor if it's a
            # workshops/ file
            edge_count = run_extractors_on_file(text, gen, file_id, p.name)
            if "workshops" in str(p.relative_to(sess_dir)):
                edge_count += len(extract_workshop_g7(text, workshop_id=file_id))

            # Also try G1 frequency inference for any zero-result file
            # (catches G1 sessions whose extractor wasn't invoked above)
            if edge_count == 0 and gen == "G1":
                # G1 emits at session-level, not file-level — skip categorization
                # of individual G1 files unless they're suspiciously empty
                pass

            if edge_count > 0:
                continue

            # Zero-coverage — categorize
            if is_system_file(p.name):
                cat = "SYSTEM-FILE"
            elif is_shell_file(text):
                cat = "SHELL"
            elif gen == "G1":
                cat = "PRE-G3-NARRATIVE"
            elif is_data_only(text):
                cat = "DATA-ONLY"
            else:
                cat = "FORMAT-MISS"

            per_category[cat] += 1
            zero_files.append({
                "sid": sid,
                "location": loc,
                "generation": gen,
                "path": str(p.relative_to(ROOT)).replace("\\", "/"),
                "size": p.stat().st_size,
                "category": cat,
                "first_header": detect_first_header(text),
                "head_preview": re.sub(r"\s+", " ", text[:240]).strip(),
            })

    # Write JSON
    payload = {
        "summary": {
            "total_files_scanned": total_files,
            "zero_coverage_total": len(zero_files),
            "by_category": dict(per_category),
        },
        "zero_files": zero_files,
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2),
                        encoding="utf-8")

    # Console summary
    print(f"Scanned {total_files} files across 90 sessions")
    print(f"Zero-coverage: {len(zero_files)} files ({100*len(zero_files)/total_files:.1f}%)\n")
    print("By category:")
    for cat in ("FORMAT-MISS", "DATA-ONLY", "SYSTEM-FILE", "PRE-G3-NARRATIVE"):
        print(f"  {cat:<22} {per_category[cat]:>5}")

    # Markdown report — surface FORMAT-MISS first (highest signal)
    md = ["# Zero-coverage report (Phase 0.9)",
          "",
          f"Scanned **{total_files}** session .md files. **{len(zero_files)}** "
          f"emit zero attribution edges ({100*len(zero_files)/total_files:.1f}%).",
          "",
          "## Distribution by category",
          "",
          "| Category | Count | Meaning |",
          "|:---------|------:|:--------|",
          f"| FORMAT-MISS | {per_category['FORMAT-MISS']} | File SHOULD have attribution but no regex fires. Regex-refinement OR orphan-content candidate. |",
          f"| SHELL | {per_category.get('SHELL', 0)} | File is a pre-allocated empty shell (e.g., S91 W4 `awaiting runtime compute dispatch`). Attribution will land when compute runs. |",
          f"| DATA-ONLY | {per_category['DATA-ONLY']} | File is mostly tables / short stub / data-listing. No attribution by design. |",
          f"| SYSTEM-FILE | {per_category['SYSTEM-FILE']} | Project-scaffolding (plans, schedules, indexes, ledgers, seeds). Attribution is project-level, not file-level. |",
          f"| PRE-G3-NARRATIVE | {per_category['PRE-G3-NARRATIVE']} | G1 session file. Pre-formal-attribution era; expected. |",
          "",
          "## FORMAT-MISS sub-classification",
          "",
          "The FORMAT-MISS pool splits into TWO distinct sub-classes:",
          "",
          "**(A) Master-aggregator pattern (design-correct)** — Files where authorship is offloaded to sister files. The aggregator (`session-N-results-workingpaper.md`, `session-N-master-collab.md`, `session-N-master-synthesis.md`) is orchestrator-aggregated; the per-author content lives in `session-N-{agent}-{topic}.md` siblings. The session as a whole IS attributed; only the roll-up file individually has no per-file author marker.",
          "",
          "**(B) Orphan-content candidates (the 'lost ideas' pool)** — Files matching no recognized archetype. These are peculiar one-offs: cross-session reviews, special audits, way-forward planning docs, named meta-documents. Worth manual inspection.",
          ""]
    # Compute sub-classification
    aggregator_archetypes = ("master-collab", "master-synthesis", "results-workingpaper", "wave")
    fm_aggregator = [f for f in zero_files
                     if f["category"] == "FORMAT-MISS" and
                     any(a in f["path"].split("/")[-1] for a in aggregator_archetypes)]
    fm_orphan = [f for f in zero_files
                 if f["category"] == "FORMAT-MISS" and f not in fm_aggregator]
    md.append(f"- **(A) Master-aggregator pattern**: {len(fm_aggregator)} files")
    md.append(f"- **(B) Orphan-content candidates**: {len(fm_orphan)} files")
    md.append("")

    # FORMAT-MISS orphan candidates (B) — the HIGH-SIGNAL section
    fm_orphan.sort(key=lambda r: (-r["size"], r["sid"]))
    md.append(f"## (B) Orphan-content candidates ({len(fm_orphan)} files) — the 'lost ideas' surface")
    md.append("")
    md.append("These are FORMAT-MISS files that DON'T match any standard aggregator archetype. Sorted by size (largest first). Each is a candidate for one of: (i) genuine orphan content worth re-surfacing, (ii) a one-off format the regex doesn't catch yet, (iii) an unusual review/audit pattern.")
    md.append("")
    md.append("| Gen | Session | File | Size | First header | Head preview |")
    md.append("|:---|:--------|:-----|-----:|:-------------|:-------------|")
    for f in fm_orphan[:150]:
        hd = f["first_header"].replace("|", "\\|")
        pv = f["head_preview"][:120].replace("|", "\\|")
        path_short = f["path"].split("/", 2)[-1]
        md.append(f"| {f['generation']} | S{f['sid']} | `{path_short}` | "
                  f"{f['size']:,} | {hd} | {pv} |")
    if len(fm_orphan) > 150:
        md.append(f"\n…and {len(fm_orphan)-150} more orphan entries in the JSON.")
    md.append("")

    # FORMAT-MISS master-aggregator (A) — design-correct, lower priority
    fm_aggregator.sort(key=lambda r: (-r["size"], r["sid"]))
    md.append(f"## (A) Master-aggregator pattern ({len(fm_aggregator)} files) — design-correct")
    md.append("")
    md.append("These are aggregator files whose authorship is offloaded to sister files. The session as a whole is attributed; only the roll-up file individually has no per-file author marker. Phase 1 harvester could optionally attribute the aggregator to `orchestrator` as the synthesizer.")
    md.append("")
    md.append("| Gen | Session | File | Size | First header |")
    md.append("|:---|:--------|:-----|-----:|:-------------|")
    for f in fm_aggregator[:60]:
        hd = f["first_header"].replace("|", "\\|")
        path_short = f["path"].split("/", 2)[-1]
        md.append(f"| {f['generation']} | S{f['sid']} | `{path_short}` | "
                  f"{f['size']:,} | {hd} |")
    if len(fm_aggregator) > 60:
        md.append(f"\n…and {len(fm_aggregator)-60} more aggregator entries in the JSON.")
    md.append("")

    # SYSTEM-FILE listing (collapsed; just enumerate)
    sf = [f for f in zero_files if f["category"] == "SYSTEM-FILE"]
    md.append(f"## SYSTEM-FILE ({len(sf)} files) — expected zero attribution")
    md.append("")
    by_kind: dict[str, list[dict]] = defaultdict(list)
    for f in sf:
        # Group by archetype keyword
        n = f["path"].split("/")[-1]
        if "plan" in n: kind = "plan-block"
        elif "schedule" in n: kind = "workshop-schedule"
        elif "_seed" in n: kind = "workshop-seed"
        elif "pending-edits" in n: kind = "pending-edits-ledger"
        elif "results-index" in n: kind = "results-index"
        elif "carry-forward" in n: kind = "carry-forward"
        elif "OOM" in n: kind = "OOM-summary"
        elif "evoi" in n: kind = "evoi-framework"
        elif "compute-carryforward" in n: kind = "compute-carryforward"
        else: kind = "other-system"
        by_kind[kind].append(f)
    md.append("| Kind | Count | Examples |")
    md.append("|:-----|------:|:---------|")
    for k, lst in sorted(by_kind.items(), key=lambda x: -len(x[1])):
        ex = ", ".join(f["path"].split("/")[-1] for f in lst[:2])
        md.append(f"| {k} | {len(lst)} | {ex} |")
    md.append("")

    # DATA-ONLY listing
    do = [f for f in zero_files if f["category"] == "DATA-ONLY"]
    md.append(f"## DATA-ONLY ({len(do)} files) — short / table-heavy / data stubs")
    md.append("")
    md.append("These are largely tables or short stubs. Listed for completeness.")
    md.append("")
    md.append("| Session | File | Size |")
    md.append("|:--------|:-----|-----:|")
    for f in do[:40]:
        path_short = f["path"].split("/", 2)[-1]
        md.append(f"| S{f['sid']} | `{path_short}` | {f['size']:,} |")
    if len(do) > 40:
        md.append(f"\n…and {len(do)-40} more in JSON.")
    md.append("")

    OUT_MD.write_text("\n".join(md), encoding="utf-8")
    print(f"\nWrote {OUT_JSON} ({OUT_JSON.stat().st_size:,}B)")
    print(f"Wrote {OUT_MD} ({OUT_MD.stat().st_size:,}B)")


if __name__ == "__main__":
    main()
