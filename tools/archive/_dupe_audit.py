"""Full in-database duplication audit.

Computes:
 - within-table duplicates: same normalized name in same table (multiple entries)
 - cross-table duplicates:  same normalized name spans 2+ tables
 - distribution of duplication multiplicity
 - worst-offenders for eyeball

Uses the same loose-normalization as the coverage check.
"""
import json
import re
from pathlib import Path
from collections import defaultdict, Counter

ROOT = Path(".")
BATCH = ROOT / "tools" / "anchor_validation_batches"
AGG_PATH = ROOT / "tools" / "_anchor_validation_results.json"


def normalize(s):
    if not s:
        return ""
    s = re.sub(r"\\([_()\[\]{}\\#*])", r"\1", s)
    s = s.replace("`", "")
    s = re.sub(r"\*+", "", s)
    s = s.replace("|", " ")
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()


agg = json.loads(AGG_PATH.read_text(encoding="utf-8"))

entries = {}
for b in sorted(BATCH.glob("*.json")):
    try:
        payload = json.loads(b.read_text(encoding="utf-8"))
    except Exception:
        continue
    for a in payload.get("anchors", []):
        aid = a.get("anchor_id")
        if aid:
            a["_table"] = payload.get("table")
            entries[aid] = a

# Build normalized-name -> [(aid, table, source_file, verdict)]
name_to_entries = defaultdict(list)
for aid, e in entries.items():
    nm = normalize(e.get("name") or "")
    if len(nm) < 15:  # skip too-short
        continue
    table = e.get("_table")
    verdict = agg.get(table, {}).get(aid, {}).get("verdict", "?")
    name_to_entries[nm].append({
        "aid": aid,
        "table": table,
        "source_file": e.get("source_file") or "",
        "verdict": verdict,
        "name": e.get("name") or "",
    })

# ------------------------------------------------------------------
# Within-table duplication: same name appearing N times in same table
# ------------------------------------------------------------------
within_table_dups = defaultdict(list)  # (table, name) -> [entry...]
for nm, ents in name_to_entries.items():
    by_table = defaultdict(list)
    for e in ents:
        by_table[e["table"]].append(e)
    for table, items in by_table.items():
        if len(items) >= 2:
            within_table_dups[(table, nm)] = items

# Per-table within-table dup count
within_by_table = Counter()
within_dup_entry_count_by_table = Counter()
for (table, nm), items in within_table_dups.items():
    within_by_table[table] += 1
    within_dup_entry_count_by_table[table] += len(items) - 1  # excess copies

# ------------------------------------------------------------------
# Cross-table duplication: same name appearing in 2+ DIFFERENT tables
# ------------------------------------------------------------------
cross_table = []
for nm, ents in name_to_entries.items():
    tables = set(e["table"] for e in ents)
    if len(tables) >= 2:
        cross_table.append((nm, ents))

# ------------------------------------------------------------------
# Overall multiplicity distribution
# ------------------------------------------------------------------
mult_dist = Counter()
for nm, ents in name_to_entries.items():
    mult_dist[len(ents)] += 1

# ------------------------------------------------------------------
# Atlas-overlap: how many name groups span Atlas AND non-Atlas sources?
# ------------------------------------------------------------------
def is_atlas(sf):
    return "framework/atlas/" in (sf or "").replace("\\", "/").lower()


atlas_overlap = 0
non_atlas_only = 0
atlas_only = 0
total_named = 0
for nm, ents in name_to_entries.items():
    total_named += 1
    has_atlas = any(is_atlas(e["source_file"]) for e in ents)
    has_non_atlas = any(not is_atlas(e["source_file"]) for e in ents)
    if has_atlas and has_non_atlas:
        atlas_overlap += 1
    elif has_atlas:
        atlas_only += 1
    else:
        non_atlas_only += 1

# ------------------------------------------------------------------
# REPORT
# ------------------------------------------------------------------
total_entries_named = sum(len(v) for v in name_to_entries.values())
total_uniq_names = len(name_to_entries)
total_excess = sum(within_dup_entry_count_by_table.values())

print("=" * 80)
print("DUPLICATION AUDIT")
print("=" * 80)
print(f"Total entries with name length >= 15: {total_entries_named}")
print(f"Total unique normalized names:        {total_uniq_names}")
print(f"Excess entries (dupes beyond first):  {total_excess}")
print(f"In-database dup rate:                 {total_excess/total_entries_named*100:.1f}%")
print()
print("Multiplicity distribution (# entries per unique name):")
for m in sorted(mult_dist):
    bar = "#" * min(60, mult_dist[m] // 10) if mult_dist[m] > 10 else ""
    print(f"  multiplicity={m:>3}: {mult_dist[m]:>5} unique names  {bar}")
print()
print("Per-table within-table duplication:")
print(f"  {'table':<22}{'dup-name-groups':>18}{'excess-entries':>16}")
for t in sorted(within_by_table):
    print(f"  {t:<22}{within_by_table[t]:>18}{within_dup_entry_count_by_table[t]:>16}")
print()
print(f"Cross-table name groups (same name in 2+ different tables): {len(cross_table)}")
print()
print(f"Atlas vs non-Atlas overlap:")
print(f"  name groups spanning BOTH Atlas + non-Atlas: {atlas_overlap}")
print(f"  name groups in Atlas-only sources:           {atlas_only}")
print(f"  name groups in non-Atlas-only sources:       {non_atlas_only}")
print()

# Top within-table duplicate offenders
print("Top 15 within-table dup-name-groups by excess count:")
sorted_dups = sorted(within_table_dups.items(), key=lambda x: -len(x[1]))
for (table, nm), items in sorted_dups[:15]:
    src_files = Counter(e["source_file"] for e in items)
    verdict_counts = Counter(e["verdict"] for e in items)
    print(f"\n  [{table}] '{nm[:80]}' x{len(items)}")
    print(f"     verdicts: {dict(verdict_counts)}")
    for sf, c in src_files.most_common(3):
        print(f"     {c}x  {sf}")

print()
print("Sample 10 cross-table dup-name-groups:")
for nm, ents in sorted(cross_table, key=lambda x: -len(x[1]))[:10]:
    tables = sorted(set(e["table"] for e in ents))
    print(f"\n  '{nm[:80]}'  tables={tables}  N={len(ents)}")
    for e in ents[:4]:
        print(f"     [{e['table']}|{e['verdict']}] {e['aid']}: {e['source_file'][:80]}")

# Write a JSON dump for downstream programmatic use
out = ROOT / "tools" / "_dupe_audit_results.json"
out.write_text(json.dumps({
    "summary": {
        "total_entries_named": total_entries_named,
        "total_uniq_names": total_uniq_names,
        "total_excess": total_excess,
        "in_db_dup_rate_pct": round(total_excess / total_entries_named * 100, 2),
        "within_table_dup_groups": dict(within_by_table),
        "within_table_excess_entries": dict(within_dup_entry_count_by_table),
        "cross_table_dup_groups": len(cross_table),
        "atlas_overlap_groups": atlas_overlap,
        "atlas_only_groups": atlas_only,
        "non_atlas_only_groups": non_atlas_only,
        "multiplicity_distribution": dict(mult_dist),
    }
}, indent=2), encoding="utf-8")
print(f"\nWrote {out}")
