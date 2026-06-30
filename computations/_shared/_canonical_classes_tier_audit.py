"""One-shot audit: tabulate `tier` and `parent_id` population in CLASSES."""
import sys
from pathlib import Path
from collections import Counter

sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import *  # noqa: F401, F403 — rule compliance (S34+)
from canonical_classes import CLASSES

total = len(CLASSES)            # (local)
tier_dist = Counter()
no_tier_field = []
parent_set = 0                  # (local)
parent_null = 0                 # (local)
parent_ids_referenced = set()

for cid, c in CLASSES.items():
    if "tier" in c:
        tier_dist[c["tier"]] += 1
    else:
        no_tier_field.append(cid)
    pid = c.get("parent_id")
    if pid in (None, "", "null"):
        parent_null += 1
    else:
        parent_set += 1
        parent_ids_referenced.add(pid)

classes_that_are_parents = set(CLASSES) & parent_ids_referenced
orphan_parent_refs = parent_ids_referenced - set(CLASSES)

print(f"TOTAL CLASSES: {total}")
print()
print("TIER DISTRIBUTION:")
for k in sorted(tier_dist.keys()):
    pct = 100 * tier_dist[k] / total
    print(f"  tier = {k}:  {tier_dist[k]:4d}  ({pct:5.1f}%)")
if no_tier_field:
    print(f"  NO tier field: {len(no_tier_field):4d}  ({100*len(no_tier_field)/total:5.1f}%)")
print()
print("PARENT_ID STATUS:")
print(f"  parent_id set (non-null): {parent_set:4d}  ({100*parent_set/total:5.1f}%)")
print(f"  parent_id null/missing:   {parent_null:4d}  ({100*parent_null/total:5.1f}%)")
print()
print("PARENT/CHILD GRAPH STRUCTURE:")
print(f"  Distinct classes referenced AS parent: {len(parent_ids_referenced)}")
print(f"  Classes that have at least one child:  {len(classes_that_are_parents)}")
print(f"  Orphan parent_id refs (parent does not exist as a class): {len(orphan_parent_refs)}")
for o in sorted(orphan_parent_refs):
    print(f"    -> {o}")
print()
print("NON-ZERO TIER ENTRIES (the depth-tracking work that actually got done):")
nz = [(cid, c) for cid, c in CLASSES.items() if c.get("tier", 0) != 0]
for cid, c in nz:
    print(f"  {cid}: tier={c['tier']}, parent_id={c.get('parent_id')}")
if not nz:
    print("  (none)")
print()
print("CHILDREN GROUPED BY PARENT:")
children_of = {}
for cid, c in CLASSES.items():
    pid = c.get("parent_id")
    if pid:
        children_of.setdefault(pid, []).append(cid)
for pid in sorted(children_of):
    print(f"  {pid}  ->  {children_of[pid]}")
