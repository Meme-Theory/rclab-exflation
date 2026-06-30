#!/usr/bin/env python3
"""
open_channel_reconcile.py  —  Provenance reconciliation of the knowledge.db
`open_channels` view (877 rows as of 2026-05-31 / S97).

WHAT THIS IS / IS NOT
---------------------
The `open_channels` table is NOT a curated open-question ledger. It is a raw
FTS extractor scrape: any markdown-table row or `OPEN`-tagged line across the
session corpus (S6 -> S97) is captured. This script tags every row by the ONE
thing that is mechanically verifiable from the data itself -- its source
document (provenance) -- so we can see how much of the "open" view is
extraction artifact / stale snapshot / superseded staging vs how much is a
genuine forward channel.

DISCIPLINE (no fabrication): the provenance tag is derived ONLY from
`source_file`. The script makes NO claim that any physics channel is open or
closed. A small curated OVERRIDE map upgrades specific rows to CLOSED/ARTIFACT
ONLY where the closure is cited to a canonical register (EVOI Items-CLOSED
table; row self-statement) or the row is a visible table-header / SHA row.
Everything else keeps its provenance tag. Genuine LIVE-channel synthesis is
done separately, by hand, in open-channel-ledger.md, sourced to
atlas-04-assumptions.md (the S97-current status register).

Run:  phonon-exflation-sim/.venv312/Scripts/python.exe tools/open_channel_reconcile.py
Out:  sessions/framework/registry/open-channel-reconciliation.md
"""
import sqlite3
import re
import os

DB = os.path.join("tools", "knowledge.db")
OUT = os.path.join("sessions", "framework", "registry", "open-channel-reconciliation.md")

# --- curated overrides (rowid -> (tag, reason)), each grounded ----------------
# CLOSED: closure cited to a canonical register or self-stated in the row.
GROUNDED_CLOSED = {
    14: "FUNCTIONAL-SELECT-67 = FAIL-PERMANENT (S73B W1-C) per evoi-framework.md Items-CLOSED",
    15: "BBN-VOLOVIK-67 = FAIL (S73A W1-C) per evoi-framework.md Items-CLOSED",
    16: "TRANSIT-PS-67 = FAIL (S73B W1-A, alpha_s=+0.833 125sigma) per evoi-framework.md Items-CLOSED",
    35: "Q23 TRANSIT-PS-67 -> FAIL S73B W1-A (evoi Items-CLOSED)",
    40: "Q28 FUNCTIONAL-SELECT-67 -> FAIL-PERMANENT S73B W1-C (evoi Items-CLOSED)",
    41: "Q29 BBN-VOLOVIK-67 -> FAIL S73A W1-C (evoi Items-CLOSED)",
    67: "Pomeranchuk g*N(0)=3.24 algebraic-permanent (S75 W4-K); row self-states RESOLVED",
}
# ARTIFACT: visible table-header rows or SHA/path provenance rows (not channels).
ARTIFACT = {
    34: "markdown table-header row", 69: "markdown table-header row",
    70: "markdown table-header row", 74: "markdown table-header row",
    75: "plan-SHA provenance row", 76: "audit_sha256 hex string",
    77: "content_sha256 hex string", 78: "workshop-precedent SHA",
    79: "script path", 80: "data path", 81: "plot path",
    82: "split-writer script path", 83: "markdown table-header row",
    94: "markdown table-header row", 112: "markdown table-header row",
    182: "markdown table-header row", 189: "markdown table-header row",
    202: "markdown table-header row", 240: "markdown table-header row",
}


def provenance_tag(src: str) -> str:
    s = (src or "").replace("\\", "/").lower()
    if "open-channel-audit" in s:
        return "EXCLUDED-MORNING-AUDIT"
    if "atlas-uplift-materials" in s:
        return "SUPERSEDED-STAGING-S88"
    if "/archive/" in s:
        return "STALE-SNAPSHOT-ARCHIVE"
    if "/seeds/" in s:
        return "WORKSHOP-SEED"
    if "/workshops/" in s:
        return "WORKSHOP-SCRATCH"
    if "permanent-results-registry" in s:
        return "REGISTRY-SCRAPE"
    if "framework/atlas" in s or "framework/registry" in s or "framework/correspondence" in s:
        return "FRAMEWORK-CURATED-SCRAPE"
    if "pin-drift" in s or "pending-edits" in s or "taxonomy" in s:
        return "METHODOLOGY-TABLE"
    if re.search(r"session-\d+", s):
        return "SNAPSHOT-SESSION"
    return "OTHER"


def era_of(src: str):
    s = (src or "").replace("\\", "/")
    m = re.search(r"session-(\d+)", s)
    return int(m.group(1)) if m else None


def short(txt, n=58):
    t = (txt or "").replace("\n", " ").replace("|", "/").strip()
    return t if len(t) <= n else t[: n - 1] + "…"


def main():
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    rows = con.execute(
        "SELECT rowid, name, detail_1, detail_2, session, source_file "
        "FROM open_channels ORDER BY rowid"
    ).fetchall()

    tagged = []
    for r in rows:
        rid = r["rowid"]
        tag = provenance_tag(r["source_file"])
        reason = "provenance: " + os.path.basename((r["source_file"] or "").replace("\\", "/"))
        if rid in ARTIFACT:
            tag, reason = "ARTIFACT", ARTIFACT[rid]
        elif rid in GROUNDED_CLOSED:
            tag, reason = "CLOSED-VERIFIED", GROUNDED_CLOSED[rid]
        tagged.append((rid, r["name"], era_of(r["source_file"]),
                       tag, r["source_file"], reason))

    # --- summaries ---
    from collections import Counter
    tagc = Counter(t[3] for t in tagged)
    srcc = Counter(os.path.basename((t[4] or "").replace("\\", "/")) for t in tagged)
    erac = Counter(t[2] for t in tagged if t[2] is not None)

    lines = []
    A = lines.append
    A("# Open-Channel View — Provenance Reconciliation")
    A("")
    A("**Registry ID**: `open-channel-reconciliation`  ")
    A("**Owner agent(s)**: `coordinator` (orchestrator-curated audit)  ")
    A("**Last updated**: `2026-05-31, S97 open-channel-view triage`  ")
    A("**Ingestion**: `/weave --update` picks up this file; it is a reference audit "
      "(provenance tags only, no row-level entity claims).  ")
    A("")
    A("**Generated by** `tools/open_channel_reconcile.py` (reads `tools/knowledge.db`).  ")
    A(f"**Total `open_channels` rows**: {len(tagged)}  ")
    A("**Date**: 2026-05-31 (S97 era).  ")
    A("**Method**: each row tagged by *provenance* (`source_file`) — mechanically "
      "verifiable, NO physics claim. Curated overrides upgrade specific rows to "
      "`CLOSED-VERIFIED` (closure cited to a canonical register) or `ARTIFACT` "
      "(visible table-header / SHA / path row). Genuine live-channel synthesis "
      "is in `open-channel-ledger.md`, sourced to `atlas-04-assumptions.md`.")
    A("")
    A("## What each tag means")
    A("")
    A("| Tag | Meaning | Actionable? |")
    A("|:----|:--------|:------------|")
    A("| `EXCLUDED-MORNING-AUDIT` | Scraped from `sessions/open-channel-audit/` (the 31MAY flagged session). | No — excluded per user instruction |")
    A("| `SUPERSEDED-STAGING-S88` | Draft copy in S88 `atlas-uplift-materials/`; canonical is `framework/Atlas/`. | No — read the canonical Atlas instead |")
    A("| `STALE-SNAPSHOT-ARCHIVE` | Frozen `OPEN`-status row from an archived session WP (S6–S49). | No — point-in-time, superseded by later closures |")
    A("| `WORKSHOP-SCRATCH` | Internal reasoning row from a workshop doc. | No — never was a tracked channel |")
    A("| `WORKSHOP-SEED` | Planning-seed row from a session `seeds/` doc. | No — planning scaffold |")
    A("| `REGISTRY-SCRAPE` | Row scraped from `permanent-results-registry.md` (headers/SHAs/landed results). | Mostly no — landed results, not open |")
    A("| `FRAMEWORK-CURATED-SCRAPE` | Row scraped from a curated `framework/` doc. | Check canonical doc for current status |")
    A("| `METHODOLOGY-TABLE` | Pin-drift / pending-edit / taxonomy table row. | No — methodology bookkeeping |")
    A("| `SNAPSHOT-SESSION` | Frozen `OPEN`-status row from a non-archived session WP (S53–S97). | Maybe — closer to current; cross-check canonical |")
    A("| `ARTIFACT` | Visible table-header / SHA / path row — never a channel. | No |")
    A("| `CLOSED-VERIFIED` | Closure cited to a canonical register. | No — already resolved |")
    A("| `OTHER` | Unclassified provenance. | Review |")
    A("")
    A("## Tag distribution (all rows)")
    A("")
    A("| Tag | Count | % |")
    A("|:----|------:|--:|")
    for tag, c in tagc.most_common():
        A(f"| `{tag}` | {c} | {100*c/len(tagged):.1f}% |")
    A("")
    A("## Era distribution (session of the source document)")
    A("")
    A("Most rows were scraped from documents written many sessions ago — the "
      "scrape is dominated by old source material, not current open work.")
    A("")
    A("| Source session | Rows scraped | ")
    A("|:---------------|-------------:|")
    for era in sorted(erac):
        A(f"| S{era} | {erac[era]} |")
    A("")
    A("## Top source documents")
    A("")
    A("| Source file | Rows |")
    A("|:------------|-----:|")
    for src, c in srcc.most_common(25):
        A(f"| `{src}` | {c} |")
    A("")
    A("## Full row-by-row audit (all rows)")
    A("")
    A("| rowid | name | era | tag | reason / provenance |")
    A("|------:|:-----|:---:|:----|:--------------------|")
    for rid, name, era, tag, src, reason in tagged:
        eralbl = f"S{era}" if era else "—"
        A(f"| {rid} | {short(name)} | {eralbl} | `{tag}` | {short(reason, 70)} |")
    A("")

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    # console summary
    print(f"rows={len(tagged)}  ->  {OUT}")
    print("TAG DISTRIBUTION:")
    for tag, c in tagc.most_common():
        print(f"  {tag:28s} {c:4d}  {100*c/len(tagged):5.1f}%")
    print("ERA SPREAD (top 12):")
    for era, c in erac.most_common(12):
        print(f"  S{era:<4} {c}")


if __name__ == "__main__":
    main()
