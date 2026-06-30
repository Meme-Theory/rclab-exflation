r"""tools/_noise_coverage_check.py - Loose search for NOISE entries in data.

For each NOISE entry sampled, this script answers:
  "Is the math/content of this NOISE entry ALREADY preserved somewhere?"

Three-tier coverage check:
  Tier 1: PRESERVED-IN-VALID-INDEX
    The key appears in another VALID-classified entry's indexed text.
    Strongest signal: the math lives in the cleaned knowledge graph.
  Tier 2: PRESERVED-IN-SAME-FILE-MULTI
    The key appears at multiple positions in the noise's own source_file.
    Indicates the math is referenced more than once in its own file
    (likely a parent theorem block plus the noise-extraction location).
  Tier 3: PRESERVED-IN-OTHER-SOURCE
    The key appears in a different source_file in the corpus.
    Math is replicated across sessions / files; even if the parent isn't
    indexed, the content is in the corpus.
  Tier 4: ORPHANED
    None of the above. The math appears only once, in the noise's own file.

The search is loose (substring match on a normalized form):
  - markdown escape backslashes stripped (`\_` -> `_`, `\(` -> `(`)
  - backticks, bold/italic asterisks stripped
  - pipe characters (markdown table separators) replaced with spaces
  - whitespace collapsed to single spaces
  - lowercased

Cross-table by design: a theorems-NOISE entry whose content lives inside a
closed_mechanisms VALID entry's text counts as PRESERVED-IN-VALID-INDEX.

Usage:
    python tools/_noise_coverage_check.py
        # default: read spot-check sample from tools/_noise_spot_check.md
    python tools/_noise_coverage_check.py --sample tools/_noise_spot_check_seed43.md
        # use a different sample file
    python tools/_noise_coverage_check.py --full
        # check all 2162 NOISE entries
    python tools/_noise_coverage_check.py --min-key 20
        # require longer keys
    python tools/_noise_coverage_check.py --no-source-pass
        # skip the source-file tiers (faster; tier-1 only)

Output: tools/_noise_coverage_report.md (or seed-suffixed path)
"""

import argparse
import json
import re
from pathlib import Path

ROOT = Path(".")
AGG_PATH = ROOT / "tools" / "_anchor_validation_results.json"
BATCH = ROOT / "tools" / "anchor_validation_batches"
DEFAULT_SPOT_MD = ROOT / "tools" / "_noise_spot_check.md"
DEFAULT_REPORT_OUT = ROOT / "tools" / "_noise_coverage_report.md"


def normalize(s):
    """Normalize for loose matching: strip markdown, escapes, collapse whitespace."""
    if not s:
        return ""
    # Strip markdown escape backslashes before common chars
    s = re.sub(r"\\([_()\[\]{}\\#*])", r"\1", s)
    # Strip backticks
    s = s.replace("`", "")
    # Strip bold/italic asterisks (any run of *)
    s = re.sub(r"\*+", "", s)
    # Strip pipe characters (markdown table cell separators)
    s = s.replace("|", " ")
    # Collapse whitespace
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()


def search_key(name, min_len):
    """Extract the most distinctive part of name for searching."""
    nm = normalize(name)
    nm = nm.rstrip(".,:;-=+")
    if len(nm) < min_len:
        return None
    if len(nm) > 250:
        nm = nm[:250]
    return nm


def load_all_entries():
    """anchor_id -> entry-dict (from batch files)."""
    out = {}
    for b in sorted(BATCH.glob("*.json")):
        try:
            payload = json.loads(b.read_text(encoding="utf-8"))
        except Exception:
            continue
        for a in payload.get("anchors", []):
            aid = a.get("anchor_id")
            if aid:
                a["_table"] = payload.get("table")
                out[aid] = a
    return out


def build_valid_index(agg, all_entries):
    """anchor_id -> (table, normalized(name+statement+...)) for all VALID entries."""
    idx = {}
    for table, verdicts in agg.items():
        for aid, v in verdicts.items():
            if v.get("verdict") != "VALID":
                continue
            e = all_entries.get(aid)
            if not e:
                continue
            text_parts = [
                str(e.get("name") or ""),
                str(e.get("statement") or ""),
                str(e.get("condition") or ""),
                str(e.get("detail_1") or ""),
                str(e.get("detail_2") or ""),
                str(e.get("context_snippet") or ""),
            ]
            idx[aid] = (table, normalize(" ".join(text_parts)))
    return idx


def collect_source_files(all_entries):
    """Return set of unique source_file paths referenced by any anchor."""
    files = set()
    for e in all_entries.values():
        sf = e.get("source_file")
        if sf:
            files.add(sf.replace("\\", "/"))
    return files


def build_source_corpus(source_files, max_bytes=2_000_000):
    """source_file (normalized path) -> normalized-text content. Skip files >max_bytes."""
    corpus = {}
    skipped = 0
    missing = 0
    for sf in source_files:
        p = ROOT / sf
        if not p.exists():
            missing += 1
            continue
        try:
            size = p.stat().st_size
            if size > max_bytes:
                skipped += 1
                continue
            text = p.read_text(encoding="utf-8", errors="replace")
            corpus[sf] = normalize(text)
        except Exception:
            skipped += 1
    return corpus, skipped, missing


def get_sample_aids(sample_path, full):
    """Return list of anchor_ids to check."""
    if full:
        agg = json.loads(AGG_PATH.read_text(encoding="utf-8"))
        out = []
        for _t, verdicts in agg.items():
            out.extend(aid for aid, v in verdicts.items() if v.get("verdict") == "NOISE")
        return out
    text = sample_path.read_text(encoding="utf-8")
    return re.findall(r"^### (\S+)$", text, re.MULTILINE)


def check_coverage(aid, all_entries, valid_index, agg, source_corpus, min_key,
                   max_preview=200, do_source=True):
    """Per-entry coverage check across the 3 tiers."""
    entry = all_entries.get(aid)
    if not entry:
        return {"aid": aid, "verdict": "MISSING_FROM_BATCHES", "tiers": {}}
    table = entry.get("_table") or entry.get("anchor_type")
    if not table:
        for t, vs in agg.items():
            if aid in vs:
                table = t
                break
    name = entry.get("name") or ""
    key = search_key(name, min_key)
    if not key:
        return {
            "aid": aid, "table": table, "name": name,
            "verdict": "TOO_SHORT_TO_SEARCH",
            "key": None, "tiers": {},
        }

    result = {
        "aid": aid, "table": table, "name": name, "key": key,
        "tiers": {
            "in_valid_index": {"matched": False, "matches": []},
            "in_same_file_multi": {"matched": False, "count": 0, "file": None},
            "in_other_source": {"matched": False, "files": []},
        },
    }

    # Tier 1: search VALID index (cross-table)
    for other_aid, (other_table, other_text) in valid_index.items():
        if other_aid == aid:
            continue
        if key in other_text:
            idx_pos = other_text.find(key)
            preview = other_text[max(0, idx_pos - 40):idx_pos + len(key) + 40]
            result["tiers"]["in_valid_index"]["matches"].append({
                "aid": other_aid, "table": other_table,
                "preview": preview[:max_preview],
            })
            result["tiers"]["in_valid_index"]["matched"] = True
            if len(result["tiers"]["in_valid_index"]["matches"]) >= 3:
                break

    if do_source:
        # Tier 2: search noise's own source_file for multiple occurrences
        own_file = entry.get("source_file")
        if own_file:
            own_file_norm = own_file.replace("\\", "/")
            own_text = source_corpus.get(own_file_norm)
            if own_text is not None:
                count = own_text.count(key)
                result["tiers"]["in_same_file_multi"]["count"] = count
                result["tiers"]["in_same_file_multi"]["file"] = own_file_norm
                if count > 1:
                    result["tiers"]["in_same_file_multi"]["matched"] = True

        # Tier 3: search any OTHER source_file
        for sf, text in source_corpus.items():
            if sf == (own_file or "").replace("\\", "/"):
                continue
            if key in text:
                result["tiers"]["in_other_source"]["files"].append(sf)
                result["tiers"]["in_other_source"]["matched"] = True
                if len(result["tiers"]["in_other_source"]["files"]) >= 3:
                    break

    # Final verdict (tiered priority)
    if result["tiers"]["in_valid_index"]["matched"]:
        result["verdict"] = "PRESERVED_IN_VALID_INDEX"
    elif result["tiers"]["in_same_file_multi"]["matched"]:
        result["verdict"] = "PRESERVED_IN_SAME_FILE_MULTI"
    elif result["tiers"]["in_other_source"]["matched"]:
        result["verdict"] = "PRESERVED_IN_OTHER_SOURCE"
    else:
        result["verdict"] = "ORPHANED"

    return result


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--full", action="store_true",
                    help="Check all NOISE entries, not just the sample.")
    ap.add_argument("--sample", default=str(DEFAULT_SPOT_MD),
                    help="Spot-check markdown file to read sampled anchor_ids from.")
    ap.add_argument("--min-key", type=int, default=15)
    ap.add_argument("--no-source-pass", action="store_true",
                    help="Skip Tier 2+3 source-file passes (faster; tier-1 only).")
    ap.add_argument("--out", default=None,
                    help="Output report path. Default: tools/_noise_coverage_report.md or "
                         "seed-suffixed if --sample is seed-suffixed.")
    args = ap.parse_args()

    sample_path = Path(args.sample)
    if args.out:
        out_path = Path(args.out)
    elif sample_path.stem == "_noise_spot_check":
        out_path = DEFAULT_REPORT_OUT
    else:
        # mirror the seed suffix from sample filename onto report
        suffix = sample_path.stem.replace("_noise_spot_check", "")
        out_path = ROOT / "tools" / f"_noise_coverage_report{suffix}.md"

    agg = json.loads(AGG_PATH.read_text(encoding="utf-8"))
    all_entries = load_all_entries()
    valid_index = build_valid_index(agg, all_entries)
    sample_aids = get_sample_aids(sample_path, args.full)

    # Filter to NOISE-only
    noise_only = []
    for aid in sample_aids:
        for _t, vs in agg.items():
            if aid in vs and vs[aid].get("verdict") == "NOISE":
                noise_only.append(aid)
                break

    source_corpus = {}
    if not args.no_source_pass:
        source_files = collect_source_files(all_entries)
        print(f"Building source corpus from {len(source_files)} unique source_file paths...")
        source_corpus, skipped, missing = build_source_corpus(source_files)
        print(f"  loaded {len(source_corpus)} files; skipped {skipped} (too large); missing {missing}")

    print(f"Checking {len(noise_only)} NOISE entries...")
    results = [check_coverage(aid, all_entries, valid_index, agg, source_corpus,
                              args.min_key, do_source=not args.no_source_pass)
               for aid in noise_only]

    # Tally
    counts = {
        "PRESERVED_IN_VALID_INDEX": 0,
        "PRESERVED_IN_SAME_FILE_MULTI": 0,
        "PRESERVED_IN_OTHER_SOURCE": 0,
        "ORPHANED": 0,
        "TOO_SHORT_TO_SEARCH": 0,
        "MISSING_FROM_BATCHES": 0,
    }
    for r in results:
        counts[r["verdict"]] = counts.get(r["verdict"], 0) + 1

    preserved = (counts["PRESERVED_IN_VALID_INDEX"]
                 + counts["PRESERVED_IN_SAME_FILE_MULTI"]
                 + counts["PRESERVED_IN_OTHER_SOURCE"])

    # By table
    by_table = {}
    for r in results:
        t = r.get("table") or "?"
        b = by_table.setdefault(t, {k: 0 for k in counts})
        b["total"] = b.get("total", 0) + 1
        b[r["verdict"]] = b.get(r["verdict"], 0) + 1

    # Write report
    lines = [
        "# NOISE Coverage Check - loose search results",
        "",
        f"Sample source: `{sample_path}`",
        f"Sample size: {len(noise_only)} NOISE entries",
        f"Min key length: {args.min_key} chars (normalized)",
        f"VALID index size: {len(valid_index)} entries (cross-table)",
        f"Source corpus: {len(source_corpus)} files loaded" if source_corpus else "Source corpus: SKIPPED",
        "",
        "## Aggregate (tiered priority — first match wins)",
        f"- **Tier 1 PRESERVED_IN_VALID_INDEX**: **{counts['PRESERVED_IN_VALID_INDEX']}** "
        f"({counts['PRESERVED_IN_VALID_INDEX']/len(results)*100:.1f}%)  -  content in another VALID entry",
        f"- **Tier 2 PRESERVED_IN_SAME_FILE_MULTI**: **{counts['PRESERVED_IN_SAME_FILE_MULTI']}** "
        f"({counts['PRESERVED_IN_SAME_FILE_MULTI']/len(results)*100:.1f}%)  -  multiple occurrences in own source",
        f"- **Tier 3 PRESERVED_IN_OTHER_SOURCE**: **{counts['PRESERVED_IN_OTHER_SOURCE']}** "
        f"({counts['PRESERVED_IN_OTHER_SOURCE']/len(results)*100:.1f}%)  -  content appears in another file",
        f"- **PRESERVED total** (any tier): **{preserved}** ({preserved/len(results)*100:.1f}%)",
        f"- **ORPHANED** (no match anywhere): **{counts['ORPHANED']}** "
        f"({counts['ORPHANED']/len(results)*100:.1f}%)",
        f"- TOO_SHORT_TO_SEARCH: {counts['TOO_SHORT_TO_SEARCH']}",
        f"- MISSING_FROM_BATCHES: {counts['MISSING_FROM_BATCHES']}",
        "",
        "## Per-table breakdown",
        "",
        "| Table | Total | T1-index | T2-same-file | T3-other-src | Orphaned | Too short |",
        "|:------|----:|----:|----:|----:|----:|----:|",
    ]
    for t in sorted(by_table):
        b = by_table[t]
        lines.append(
            f"| {t} | {b.get('total',0)} | {b.get('PRESERVED_IN_VALID_INDEX',0)} | "
            f"{b.get('PRESERVED_IN_SAME_FILE_MULTI',0)} | {b.get('PRESERVED_IN_OTHER_SOURCE',0)} | "
            f"{b.get('ORPHANED',0)} | {b.get('TOO_SHORT_TO_SEARCH',0)} |"
        )
    lines.append("")
    lines.append("**Reading**: PRESERVED at any tier means dropping the NOISE entry doesn't lose content. ORPHANED means the math appears once, only in the noise's own source location — those are the real review priority (potential content loss).")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## ORPHANED entries (real review priority)")
    lines.append("")
    orphans = [r for r in results if r["verdict"] == "ORPHANED"]
    if not orphans:
        lines.append("*(none — every sampled NOISE entry has content preserved somewhere in the corpus)*")
    else:
        for r in orphans:
            lines.append(f"### {r['aid']}  ({r.get('table','?')})")
            lines.append(f"- name: `{(r.get('name') or '')[:180]}`")
            lines.append(f"- key: `{(r.get('key') or '')[:160]}`")
            own = r["tiers"]["in_same_file_multi"]
            lines.append(f"- own-file occurrences: {own['count']} in `{own['file']}`")
            lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## PRESERVED entries — sample previews (top 10 per tier)")
    lines.append("")
    for tier_label, verdict in [
        ("Tier 1 (in VALID index)", "PRESERVED_IN_VALID_INDEX"),
        ("Tier 2 (multi-occurrence in own file)", "PRESERVED_IN_SAME_FILE_MULTI"),
        ("Tier 3 (in another source file)", "PRESERVED_IN_OTHER_SOURCE"),
    ]:
        items = [r for r in results if r["verdict"] == verdict][:10]
        if not items:
            continue
        lines.append(f"### {tier_label}")
        lines.append("")
        for r in items:
            lines.append(f"#### {r['aid']}  ({r.get('table','?')})")
            lines.append(f"- name: `{(r.get('name') or '')[:160]}`")
            lines.append(f"- key:  `{(r.get('key') or '')[:160]}`")
            if verdict == "PRESERVED_IN_VALID_INDEX":
                for m in r["tiers"]["in_valid_index"]["matches"][:2]:
                    lines.append(f"- found in **{m['aid']}** ({m['table']}):")
                    lines.append(f"    `...{m['preview']}...`")
            elif verdict == "PRESERVED_IN_SAME_FILE_MULTI":
                own = r["tiers"]["in_same_file_multi"]
                lines.append(f"- {own['count']} occurrences in `{own['file']}`")
            else:
                files = r["tiers"]["in_other_source"]["files"][:3]
                for f in files:
                    lines.append(f"- found in `{f}`")
            lines.append("")

    if counts["TOO_SHORT_TO_SEARCH"] or counts["MISSING_FROM_BATCHES"]:
        lines.append("---")
        lines.append("")
        lines.append("## TOO_SHORT / MISSING (no search performed)")
        lines.append("")
        for r in results:
            if r["verdict"] in ("TOO_SHORT_TO_SEARCH", "MISSING_FROM_BATCHES"):
                lines.append(f"- [{r['verdict']}] {r['aid']} ({r.get('table','?')}): "
                             f"`{(r.get('name') or '')[:160]}`")

    out_path.write_text("\n".join(lines), encoding="utf-8")

    print()
    print("=" * 80)
    print("COVERAGE SUMMARY")
    print("=" * 80)
    print(f"  T1 PRESERVED_IN_VALID_INDEX:    {counts['PRESERVED_IN_VALID_INDEX']:>4}")
    print(f"  T2 PRESERVED_IN_SAME_FILE_MULTI:{counts['PRESERVED_IN_SAME_FILE_MULTI']:>4}")
    print(f"  T3 PRESERVED_IN_OTHER_SOURCE:   {counts['PRESERVED_IN_OTHER_SOURCE']:>4}")
    print(f"  PRESERVED total:                {preserved:>4}  ({preserved/len(results)*100:.1f}%)")
    print(f"  ORPHANED:                       {counts['ORPHANED']:>4}  ({counts['ORPHANED']/len(results)*100:.1f}%)")
    print(f"  TOO_SHORT_TO_SEARCH:            {counts['TOO_SHORT_TO_SEARCH']:>4}")
    print(f"  MISSING_FROM_BATCHES:           {counts['MISSING_FROM_BATCHES']:>4}")
    print()
    print(f"Report: {out_path}")


if __name__ == "__main__":
    main()
