#!/usr/bin/env python3
"""Emit two deliverables from the orphan-chain investigator output:

  1. Updated orphan-content-watchlist.md — preserves the original
     row structure but updates the Status column from UNREVIEWED →
     investigator's recommendation (ORPHAN-PROMOTED / MULTI-AUTHOR /
     REGEX-FIXED / HISTORICAL-ONLY), adds Archetype, and adds a Chain
     summary column.

  2. Companion orphan-chain-analysis.md — per-orphan detail block with
     full chain-of-custody: archetype + description, all extracted
     authors with role, all upstream chain refs, downstream consumers,
     recommended edges. This is the audit-trail document the user
     asked for ("metadocuments have an audit trail").

The two outputs cross-link each other.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
SRC_JSON = ROOT / "tools" / "_orphan_chain_analysis.json"
SRC_WATCHLIST_JSON = ROOT / "tools" / "_format_generation_zero_coverage.json"
OUT_WATCHLIST = ROOT / "sessions" / "framework" / "registry" / "orphan-content-watchlist.md"
OUT_ANALYSIS = ROOT / "sessions" / "framework" / "registry" / "orphan-chain-analysis.md"


def truncate(s: str, n: int) -> str:
    if not s:
        return ""
    s = s.replace("|", "\\|")
    return s if len(s) <= n else s[:n - 1] + "…"


def chain_summary(rec: dict) -> str:
    """Build a compact chain summary string for the watchlist row."""
    if "error" in rec:
        return f"ERROR: {rec['error']}"
    auth = len(rec.get("authors_extracted", []))
    up = len(rec.get("upstream_refs", []))
    dn = len(rec.get("downstream_consumers", []))
    edges = len(rec.get("recommended_edges", []))
    parts: list[str] = []
    if auth > 0:
        parts.append(f"auth={auth}")
    if up > 0:
        parts.append(f"up={up}")
    if dn > 0:
        parts.append(f"dn={dn}")
    parts.append(f"edges={edges}")
    return " ".join(parts)


# ----------------------------------------------------------------------
# Watchlist updater
# ----------------------------------------------------------------------


def emit_watchlist(records: list[dict], aggregators: list[dict]) -> None:
    """Re-emit orphan-content-watchlist.md with chain data."""
    md: list[str] = []
    md.append("---")
    md.append("type: orphan-watchlist")
    md.append("ingested-by: /weave --update")
    md.append("---")
    md.append("")
    md.append("# Orphan-content watchlist")
    md.append("")
    md.append("**Registry ID**: `orphan-content-watchlist`  ")
    md.append("**Owner agent(s)**: `orchestrator` (sole writer)  ")
    md.append("**Last updated**: 2026-05-17, Phase 1.1 / orphan-chain investigation  ")
    md.append("**Source**: `tools/_format_generation_zero_coverage.json` "
              "(generator: `tools/_format_generation_zero_coverage.py`)  ")
    md.append("**Chain data source**: `tools/_orphan_chain_analysis.json` "
              "(generator: `tools/_orphan_chain_investigator.py`)  ")
    md.append("**Per-orphan detail**: `sessions/framework/registry/orphan-chain-analysis.md`")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## Scope")
    md.append("")
    md.append("This registry lists session markdown files that emitted ZERO "
              "attribution edges in the Phase 1 harvester run "
              "(`tools/harvest_attribution_edges.py`). The Phase 1.1 "
              "investigation (`tools/_orphan_chain_investigator.py`) ran against "
              "all 156 orphans and produced:")
    md.append("")
    md.append("- **Archetype classification** for each file (synthesis, "
              "handoff, way-forward, workshop, etc. — 33 distinct archetypes)")
    md.append("- **Author extraction** via extended regex set covering "
              "patterns the production harvester misses (H2 `## Author:` lines, "
              "`**Team**:` / `**Synthesist**:` / `**Designated Writer**:` / "
              "`[E]S-1` bracket-tag forms, bullet-prefixed `- **Agents**:` "
              "em-dash lists)")
    md.append("- **Upstream chain refs** via `**Source**:` / `**Reviewing**:` / "
              "`**Predecessor**:` / `**Extracted from**:` / `**Source files**:` "
              "/ `**Reference corpus**:` patterns")
    md.append("- **Downstream consumers** via corpus-wide inbound-link index "
              "(6,467 unique basenames scanned across `sessions/`, "
              "`computations/`, `tools/`, `summary/`)")
    md.append("- **Recommended edges** per the canonical `EDGE_TYPE_CANONICAL` "
              "vocabulary (all 839 recommended edges resolve to "
              "whitelist-approved types)")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## How to use this list")
    md.append("")
    md.append("Each row carries the investigator's status recommendation. "
              "The five terminal states are:")
    md.append("")
    md.append("- `UNREVIEWED` (legacy default before chain investigation)")
    md.append("- `REGEX-FIXED` (attribution extracted — patterns to add to "
              "Phase 1 harvester for promotion)")
    md.append("- `MULTI-AUTHOR` (synthesis-archetype with implicit "
              "or extracted multi-author attribution — emit "
              "`synthesized_by` + per-author `participates_in` edges)")
    md.append("- `ORPHAN-PROMOTED` (no author extracted, but the file has "
              "upstream/downstream chain — emit `derived_from` / `cited_in` "
              "edges; surface to next-session planner if content is "
              "substantively novel)")
    md.append("- `HISTORICAL-ONLY` (no authors, no chain, low-value — "
              "leave in archive)")
    md.append("")
    md.append("Per-orphan detail blocks (extracted authors, upstream refs, "
              "downstream consumers, recommended edges) live in "
              "`sessions/framework/registry/orphan-chain-analysis.md`.")
    md.append("")
    md.append("---")
    md.append("")

    # Distribution summary
    from collections import Counter
    status_c = Counter(r.get("status_recommendation", "UNKNOWN") for r in records)
    arch_c = Counter(r.get("archetype", "uncategorized") for r in records)
    md.append("## Distribution")
    md.append("")
    md.append("**By recommended status**:")
    for status in ["REGEX-FIXED", "MULTI-AUTHOR", "ORPHAN-PROMOTED",
                   "HISTORICAL-ONLY"]:
        n = status_c.get(status, 0)
        md.append(f"- `{status}`: {n} files")
    md.append("")
    md.append("**By archetype** (top 15):")
    for arch, n in arch_c.most_common(15):
        md.append(f"- `{arch}`: {n}")
    md.append("")
    md.append("---")
    md.append("")

    # Orphan rows (preserved structure + new columns)
    records_sorted = sorted(records, key=lambda r: (-r.get("size", 0), r.get("sid", "")))
    md.append(f"## (B) Orphan-content candidates ({len(records_sorted)} files)")
    md.append("")
    md.append("Sorted by size (largest first).")
    md.append("")
    md.append("| # | Status | Gen | Sess | Archetype | File | Size | Chain summary |")
    md.append("|--:|:-------|:----|:-----|:----------|:-----|-----:|:--------------|")
    for i, r in enumerate(records_sorted, start=1):
        path_short = r["path"].split("/", 2)[-1] if r["path"].count("/") >= 2 else r["path"]
        status = r.get("status_recommendation", "UNREVIEWED")
        archetype = r.get("archetype", "uncategorized")
        md.append(
            f"| {i} | {status} | {r['generation']} | S{r['sid']} | "
            f"{archetype} | `{truncate(path_short, 60)}` | "
            f"{r['size']:,} | {chain_summary(r)} |"
        )
    md.append("")
    md.append("---")
    md.append("")

    # Aggregators (unchanged from prior emission)
    md.append(f"## (A) Master-aggregator pattern reference ({len(aggregators)} files)")
    md.append("")
    md.append("These files have NO attribution by design — authorship is "
              "offloaded to sister files (`session-N-{agent}-{topic}.md`). "
              "Listed here for reference, not for inspection.")
    md.append("")
    md.append("| Gen | Sess | File | Size | First header |")
    md.append("|:----|:-----|:-----|-----:|:-------------|")
    for r in sorted(aggregators, key=lambda x: (-x["size"], x["sid"])):
        path_short = r["path"].split("/", 2)[-1] if r["path"].count("/") >= 2 else r["path"]
        hd = (r.get("first_header") or "").replace("|", "\\|")[:100]
        md.append(f"| {r['generation']} | S{r['sid']} | "
                  f"`{truncate(path_short, 70)}` | {r['size']:,} | {hd} |")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## Cross-references")
    md.append("")
    md.append("- Per-orphan detail: `sessions/framework/registry/orphan-chain-analysis.md`")
    md.append("- Format-generation spec: `sessions/framework/registry/session-format-generations.md`")
    md.append("- Regex module + self-test: `tools/_format_generation_regex_set.py`")
    md.append("- Phase 0.9 zero-coverage scan: `tools/_format_generation_zero_coverage.py`")
    md.append("- Phase 1 harvester: `tools/harvest_attribution_edges.py`")
    md.append("- Phase 1.1 investigator: `tools/_orphan_chain_investigator.py`")
    md.append("- Per-run audit log: `tools/harvest_attribution_edges.log`")
    md.append("- Per-run summary: `tools/harvest_attribution_edges.summary.json`")
    md.append("- Chain analysis JSON: `tools/_orphan_chain_analysis.json`")
    md.append("")
    md.append("## Change log")
    md.append("")
    md.append("| Date | Session | Change | Author |")
    md.append("|:-----|:--------|:-------|:-------|")
    md.append("| 2026-05-17 | Phase 0.9 / Task #9 | Initial landing — 156 "
              "orphan candidates surfaced from full-corpus zero-coverage "
              "scan | orchestrator |")
    md.append("| 2026-05-17 | Phase 1.1 / orphan-chain investigation | "
              "Updated Status from UNREVIEWED → recommended class "
              "(REGEX-FIXED/MULTI-AUTHOR/ORPHAN-PROMOTED/HISTORICAL-ONLY); "
              "added Archetype + Chain summary columns; produced "
              "companion `orphan-chain-analysis.md` with per-file detail "
              "blocks | orchestrator |")
    md.append("")

    OUT_WATCHLIST.write_text("\n".join(md), encoding="utf-8")
    print(f"Wrote {OUT_WATCHLIST.relative_to(ROOT)} ({OUT_WATCHLIST.stat().st_size:,}B)")


# ----------------------------------------------------------------------
# Per-orphan analysis doc emitter
# ----------------------------------------------------------------------


def emit_analysis(records: list[dict]) -> None:
    """Emit the companion orphan-chain-analysis.md with per-orphan detail."""
    md: list[str] = []
    md.append("---")
    md.append("type: orphan-chain-analysis")
    md.append("ingested-by: /weave --update")
    md.append("---")
    md.append("")
    md.append("# Orphan chain-of-custody analysis")
    md.append("")
    md.append("**Registry ID**: `orphan-chain-analysis`  ")
    md.append("**Owner agent(s)**: `orchestrator` (sole writer)  ")
    md.append("**Last updated**: 2026-05-17, Phase 1.1  ")
    md.append("**Companion**: `sessions/framework/registry/orphan-content-watchlist.md`  ")
    md.append("**Source data**: `tools/_orphan_chain_analysis.json`  ")
    md.append("**Generator**: `tools/_orphan_chain_investigator.py` + "
              "`tools/_emit_orphan_chain_outputs.py`")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## Purpose")
    md.append("")
    md.append("The Phase 0.9 zero-coverage scan surfaced 156 session markdown "
              "files that emit ZERO attribution edges via the production "
              "Phase 1 harvester (`tools/harvest_attribution_edges.py`). "
              "This document is the per-file investigation output — it "
              "tells you, for each orphan, the linked chain (what feeds in, "
              "what consumes out, who wrote it) AND the recommended edge "
              "set to emit on a future harvester promotion pass.")
    md.append("")
    md.append("Each entry below contains:")
    md.append("")
    md.append("- **Archetype** — classified file type (synthesis, handoff, "
              "way-forward, workshop, etc.) with a one-line description")
    md.append("- **Status** — recommended terminal state per the "
              "watchlist's 5-state vocabulary")
    md.append("- **Authors** — every attribution candidate extracted by the "
              "investigator, with role (author / participant / synthesizer / "
              "reviewer / researcher_contributor / etc.) and the verbatim "
              "raw token it derived from")
    md.append("- **Upstream chain** — `**Source**:` / `**Reviewing**:` / "
              "`**Predecessor**:` / `**Input**:` references with target "
              "session numbers, file paths, or researcher IDs")
    md.append("- **Downstream consumers** — files in the corpus that "
              "reference this orphan via markdown link or bare path "
              "(corpus-inbound-link-index scan)")
    md.append("- **Recommended edges** — per-edge `(type, source, target, "
              "in_whitelist)` tuples. Edges with `in_whitelist=True` can be "
              "auto-emitted on the next harvester pass; edges with "
              "`in_whitelist=False` (none in this run, but reserved for "
              "future extensions) would require adding the type to "
              "`tools/extract_entities.py::EDGE_TYPE_CANONICAL`")
    md.append("")
    md.append("**Synthesis / summary qualification**: per the user's "
              "directive, every synthesis-archetype file is explicitly "
              "qualified as such by its primary edge type. Synthesis docs "
              "emit `synthesized_by` (file → orchestrator/synthesist) + "
              "`participates_in` (researcher → file) for every named "
              "contributor. Summary docs (handoffs, quicklooks, "
              "results-summary) emit `summarizes_session` (file → "
              "session) + `authored_by` (file → primary author).")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## Reading guide for the chain blocks")
    md.append("")
    md.append("```")
    md.append("### N. <file basename>")
    md.append("- Path: <full path>")
    md.append("- Generation, Session, Size")
    md.append("- Archetype, Status, Primary edge type")
    md.append("- Authors:  [role] canonical-id  <- raw extracted token")
    md.append("- Upstream: [kind] -> targets")
    md.append("- Downstream: file_path")
    md.append("- Edges (whitelisted): N total")
    md.append("```")
    md.append("")
    md.append("---")
    md.append("")

    # Group by status, then by archetype
    by_status: dict[str, list[dict]] = {
        "REGEX-FIXED": [], "MULTI-AUTHOR": [],
        "ORPHAN-PROMOTED": [], "HISTORICAL-ONLY": [],
    }
    for r in records:
        st = r.get("status_recommendation", "UNKNOWN")
        by_status.setdefault(st, []).append(r)

    status_descriptions = {
        "REGEX-FIXED": "Attribution successfully extracted — patterns "
                       "ready to promote into production harvester at "
                       "`tools/harvest_attribution_edges.py`. Re-running the "
                       "harvester with these patterns will move these files "
                       "from 0 edges to N edges per file.",
        "MULTI-AUTHOR": "Synthesis-archetype files where attribution is "
                        "either extracted (per-section `**Researcher**:` or "
                        "bracket-tag) or implicit (file is multi-author by "
                        "design). Recommended edges: `synthesized_by` + "
                        "per-contributor `participates_in`.",
        "ORPHAN-PROMOTED": "No author extracted but the file has a chain "
                           "(upstream sources OR downstream consumers). The "
                           "chain edges (`derived_from` / `cited_in` / "
                           "`feeds_into`) are recommended for emission. "
                           "Filename-pattern attribution may be derivable "
                           "for some (e.g., `*-connes.md` → "
                           "`connes-ncg-theorist`).",
        "HISTORICAL-ONLY": "No author, no chain detected. Likely "
                           "scratchpad / one-off artifact / early-format "
                           "fragment with no current consumer. Leave in "
                           "archive.",
    }

    counter = 0
    for status in ["REGEX-FIXED", "MULTI-AUTHOR", "ORPHAN-PROMOTED",
                   "HISTORICAL-ONLY"]:
        bucket = by_status.get(status, [])
        if not bucket:
            continue
        md.append(f"## Status: `{status}` ({len(bucket)} files)")
        md.append("")
        md.append(status_descriptions[status])
        md.append("")
        # Sort within status by size desc
        bucket.sort(key=lambda r: (-r.get("size", 0), r.get("sid", "")))
        for r in bucket:
            counter += 1
            name = r["path"].split("/")[-1]
            md.append(f"### {counter}. `{name}`")
            md.append("")
            md.append(f"- **Path**: `{r['path']}`")
            md.append(f"- **Session**: S{r['sid']} | **Generation**: "
                      f"{r['generation']} | **Size**: {r['size']:,} B")
            md.append(f"- **Archetype**: `{r['archetype']}` — "
                      f"{r.get('archetype_description', '')}")
            md.append(f"- **Status**: `{r['status_recommendation']}`")
            md.append(f"- **Primary edge type**: `{r['primary_edge_type']}`")

            authors = r.get("authors_extracted", [])
            md.append(f"- **Authors extracted** ({len(authors)}):")
            if authors:
                for a in authors:
                    md.append(f"    - `[{a['role']}]` "
                              f"**`{a['canonical']}`** ← raw token: "
                              f"`{truncate(a['raw'], 60)}`")
            else:
                md.append(f"    - _(none extracted; attribution may be "
                          f"implicit per archetype or absent by design)_")

            upstream = r.get("upstream_refs", [])
            md.append(f"- **Upstream chain refs** ({len(upstream)}):")
            if upstream:
                for u in upstream[:8]:  # cap at 8 per file (registry-readability)
                    tgts = ", ".join(f"`{t}`" for t in u["targets"][:5])
                    if len(u["targets"]) > 5:
                        tgts += f", …+{len(u['targets']) - 5} more"
                    md.append(f"    - `[{u['kind']}]` → {tgts}")
                if len(upstream) > 8:
                    md.append(f"    - _(+{len(upstream) - 8} more refs "
                              f"omitted for readability — see full JSON)_")
            else:
                md.append(f"    - _(no upstream refs detected)_")

            downstream = r.get("downstream_consumers", [])
            md.append(f"- **Downstream consumers** ({len(downstream)}):")
            if downstream:
                for d in downstream[:8]:  # cap at 8
                    md.append(f"    - `{d}`")
                if len(downstream) > 8:
                    md.append(f"    - _(+{len(downstream) - 8} more "
                              f"consumers omitted — see full JSON)_")
            else:
                md.append(f"    - _(no downstream consumers detected via "
                          f"corpus inbound-link index)_")

            edges = r.get("recommended_edges", [])
            in_wl = [e for e in edges if e.get("in_whitelist", True)]
            out_wl = [e for e in edges if not e.get("in_whitelist", True)]
            md.append(f"- **Recommended edges** ({len(edges)} total; "
                      f"{len(in_wl)} whitelist-ready, "
                      f"{len(out_wl)} need extension):")
            from collections import Counter
            edge_type_c = Counter(e["edge_type"] for e in edges)
            for et, n in edge_type_c.most_common():
                md.append(f"    - `{et}`: {n}")
            md.append("")

    md.append("---")
    md.append("")
    md.append("## Promotion guidance")
    md.append("")
    md.append("To promote the REGEX-FIXED + MULTI-AUTHOR attributions into "
              "the production graph:")
    md.append("")
    md.append("1. **Sync patterns**: copy the extended attribution regex set "
              "from `tools/_orphan_chain_investigator.py` "
              "(`RE_TEAM`, `RE_AGENTS_LIST`, `RE_PARTICIPANTS`, "
              "`RE_DESIGNATED_WRITER`, `RE_SYNTH`, `RE_ASSESSOR`, "
              "`RE_AUDITOR`, `RE_LEAD`, `RE_RESEARCHER`, `RE_TAG_BRACKET`, "
              "`RE_H2_AUTHOR`, `RE_H2_PARTICIPANTS`, `RE_H2_MULTI_AUTHOR`) "
              "into `tools/_format_generation_regex_set.py::FIXTURES` with "
              "verbatim positive-test snippets. Self-test must stay PASS.")
    md.append("2. **Sync aliases**: merge the orphan-only canonical aliases "
              "(`meme-pi`, `claude`, `ainur-panel`, `team-lead` → "
              "`orchestrator`, etc.) into "
              "`tools/_format_generation_regex_set.py::AGENT_ALIASES`. "
              "Watch for the `sim-specialist`/`team-lead` parity gotchas "
              "documented in the investigator.")
    md.append("3. **Allow bullet-prefix attribution lines**: update the "
              "harvester's per-pattern anchors from `^\\s*\\*\\*` to "
              "`^[-*\\s]*\\*\\*` to permit bullet-list forms like "
              "`- **Agents**: ...`.")
    md.append("4. **Scan window extension**: for synthesis-archetype "
              "files (synergy_index, framework_synergy, team_synthesis, "
              "fusion_synthesis, master_collab), scan the FULL FILE for "
              "attribution rather than head-N lines. Per-section "
              "`**Researcher**:` and bracket-tag attributions live in the "
              "body, not the header.")
    md.append("5. **Re-run the harvester** (`tools/harvest_attribution_edges.py`) "
              "and verify edge count growth.")
    md.append("6. **Run `/weave --update`** to ingest the new edges into "
              "`knowledge.db`.")
    md.append("")
    md.append("Per-orphan edge proposals are recorded in "
              "`tools/_orphan_chain_analysis.json::results[*].recommended_edges`. "
              "Each carries `in_whitelist: bool` indicating whether the type "
              "is currently auto-emittable.")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## Cross-references")
    md.append("")
    md.append("- Watchlist row table: `sessions/framework/registry/orphan-content-watchlist.md`")
    md.append("- Investigator JSON: `tools/_orphan_chain_analysis.json`")
    md.append("- Investigator source: `tools/_orphan_chain_investigator.py`")
    md.append("- Format-generation spec: `sessions/framework/registry/session-format-generations.md`")
    md.append("- Production harvester: `tools/harvest_attribution_edges.py`")
    md.append("- Edge-type whitelist: `tools/extract_entities.py::EDGE_TYPE_CANONICAL`")
    md.append("")

    OUT_ANALYSIS.write_text("\n".join(md), encoding="utf-8")
    print(f"Wrote {OUT_ANALYSIS.relative_to(ROOT)} ({OUT_ANALYSIS.stat().st_size:,}B)")


def main() -> None:
    if not SRC_JSON.exists():
        raise SystemExit(f"Source JSON not found: {SRC_JSON}")
    if not SRC_WATCHLIST_JSON.exists():
        raise SystemExit(f"Watchlist JSON not found: {SRC_WATCHLIST_JSON}")
    with SRC_JSON.open("r", encoding="utf-8") as f:
        data = json.load(f)
    with SRC_WATCHLIST_JSON.open("r", encoding="utf-8") as f:
        wl_data = json.load(f)

    records = data["results"]
    print(f"Loaded {len(records)} orphan records")

    # Aggregator records (preserved from prior watchlist)
    fm = [x for x in wl_data["zero_files"] if x["category"] == "FORMAT-MISS"]
    agg_arch = ("master-collab", "master-synthesis", "results-workingpaper", "wave")
    aggregators = [r for r in fm
                   if any(a in r["path"].split("/")[-1] for a in agg_arch)]
    print(f"Loaded {len(aggregators)} aggregator records")

    emit_watchlist(records, aggregators)
    emit_analysis(records)


if __name__ == "__main__":
    main()
