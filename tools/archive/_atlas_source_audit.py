"""Count entries sourced from sessions/framework/Atlas/ docs by table + verdict."""
import json
from pathlib import Path
from collections import Counter

agg = json.loads(Path("tools/_anchor_validation_results.json").read_text(encoding="utf-8"))

BATCH = Path("tools/anchor_validation_batches")
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


def is_atlas(sf):
    if not sf:
        return False
    sf_norm = sf.replace("\\", "/").lower()
    return "framework/atlas/" in sf_norm


stats = {}
for aid, e in entries.items():
    table = e.get("_table")
    sf = e.get("source_file") or ""
    if not table:
        continue
    verdict = agg.get(table, {}).get(aid, {}).get("verdict", "?")
    stats.setdefault(table, {}).setdefault(verdict, {"total": 0, "atlas": 0})
    stats[table][verdict]["total"] += 1
    if is_atlas(sf):
        stats[table][verdict]["atlas"] += 1

print(f"{'table':<22}{'verdict':<10}{'total':>8}{'atlas':>8}{'atlas%':>8}")
print("-" * 60)
for t in sorted(stats):
    for v in ("VALID", "NOISE", "UNSURE"):
        if v not in stats[t]:
            continue
        s = stats[t][v]
        pct = s["atlas"] / s["total"] * 100 if s["total"] else 0
        print(f"{t:<22}{v:<10}{s['total']:>8}{s['atlas']:>8}{pct:>7.1f}%")

print()
print("Atlas source files and per-file entry counts:")
atlas_files = Counter()
for e in entries.values():
    sf = e.get("source_file") or ""
    if is_atlas(sf):
        atlas_files[sf.replace("\\", "/")] += 1
for f, c in sorted(atlas_files.items(), key=lambda x: -x[1]):
    print(f"  {c:>5}  {f}")

# Now check: for each Atlas-derived NOISE entry, is there a SIMILAR name in a non-atlas VALID entry?
# Use loose substring match on first N significant chars.
import re


def norm(s):
    if not s:
        return ""
    s = re.sub(r"\\([_()\[\]{}\\#*])", r"\1", s)
    s = s.replace("`", "")
    s = re.sub(r"\*+", "", s)
    s = s.replace("|", " ")
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()


# Build non-atlas-derived VALID name index (key: anchor_id -> normalized name)
valid_nonatlas = {}
for aid, e in entries.items():
    table = e.get("_table")
    verdict = agg.get(table, {}).get(aid, {}).get("verdict", "?")
    if verdict != "VALID":
        continue
    if is_atlas(e.get("source_file") or ""):
        continue
    nm = norm(e.get("name") or "")
    if nm:
        valid_nonatlas[aid] = nm

# Now check Atlas-derived entries (NOISE or VALID): does their name appear in a non-atlas valid?
atlas_with_canonical_parent = 0
atlas_without_canonical_parent = 0
orphan_samples = []
for aid, e in entries.items():
    if not is_atlas(e.get("source_file") or ""):
        continue
    table = e.get("_table")
    nm = norm(e.get("name") or "")
    if len(nm) < 15:
        continue  # too short to compare reliably
    # search for first 20 char substring of atlas name in any non-atlas valid name
    needle = nm[:30] if len(nm) >= 30 else nm
    matched = False
    for other_aid, other_nm in valid_nonatlas.items():
        if needle in other_nm:
            matched = True
            break
    if matched:
        atlas_with_canonical_parent += 1
    else:
        atlas_without_canonical_parent += 1
        if len(orphan_samples) < 20:
            orphan_samples.append((aid, table, e.get("name", "")[:120]))

print()
print("Atlas-derived entries — canonical-parent audit (name-overlap with non-atlas VALID):")
print(f"  with canonical parent (likely duplicate): {atlas_with_canonical_parent}")
print(f"  without canonical parent (atlas-unique):  {atlas_without_canonical_parent}")
print()
print("First 20 Atlas-unique entries (no non-atlas VALID name match):")
for aid, table, nm in orphan_samples:
    print(f"  [{table}] {aid}: {nm}")
