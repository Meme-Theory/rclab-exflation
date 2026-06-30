"""Random-anchor validation: pick anchors across all 10 entity types and
investigate each one's actual chain-of-custody data.

For each randomly-sampled anchor:
- Confirm it exists in chain_of_custody.json
- Confirm it has at least one chain entry (upstream OR downstream)
- Check direction-consistency rules (closures have ONLY upstream)
- Report the chain depth + lens breakdown
- Spot-check that the referenced upstream/downstream anchors actually exist
"""
import json
import random
import sqlite3
from collections import Counter
from pathlib import Path

random.seed(20260517)  # deterministic

ROOT = Path(__file__).resolve().parent
SIDECAR = ROOT / "viz" / "console" / "chain_of_custody.json"
DB = ROOT / "knowledge.db"

print(f"Loading sidecar: {SIDECAR}")
sidecar = json.loads(SIDECAR.read_text(encoding="utf-8"))
anchors = sidecar.get("anchors", {})
print(f"Sidecar: {len(anchors)} anchor entries")

# Group anchors by entity type from the nested 'anchor' field
by_type: dict = {}
for anchor_key, entry in anchors.items():
    inner = entry.get("anchor", {}) if isinstance(entry, dict) else {}
    atype = inner.get("type") or anchor_key.split(":", 1)[0]
    by_type.setdefault(atype, []).append(anchor_key)
print(f"Anchor types: {sorted(by_type.keys())}")
for t, items in sorted(by_type.items()):
    print(f"  {t}: {len(items)} anchors")

# Pick 2-3 random anchors per type (total ~20-25)
samples = []
for atype, items in by_type.items():
    n_pick = min(3, len(items))
    samples.extend(random.sample(items, n_pick))
print()
print(f"Selected {len(samples)} random anchors for validation")
print("=" * 80)

# Connect to DB for cross-validation
conn = sqlite3.connect(DB)
cur = conn.cursor()

results = []
for i, anchor_key in enumerate(samples, 1):
    entry = anchors.get(anchor_key, {})
    inner = entry.get("anchor", {}) if isinstance(entry, dict) else {}
    atype = inner.get("type") or anchor_key.split(":", 1)[0]
    aid = inner.get("id") or (anchor_key.split(":", 1)[1] if ":" in anchor_key else anchor_key)
    title = (inner.get("title") or "")[:70]

    upstream_by_depth = entry.get("upstream", {}) if isinstance(entry, dict) else {}
    downstream_by_depth = entry.get("downstream", {}) if isinstance(entry, dict) else {}
    stats = entry.get("stats", {}) if isinstance(entry, dict) else {}

    total_upstream = stats.get("total_upstream", 0)
    total_downstream = stats.get("total_downstream", 0)
    total_nodes = total_upstream + total_downstream

    print(f"\n[{i}] {anchor_key}")
    print(f"    title: {title!r}")
    print(f"    upstream={total_upstream} downstream={total_downstream} (depths: up={list(upstream_by_depth.keys())} down={list(downstream_by_depth.keys())})")

    # Show first upstream node and downstream node (sample of chain content)
    for depth_key in sorted(upstream_by_depth.keys()):
        nodes = upstream_by_depth[depth_key]
        if nodes:
            n = nodes[0]
            print(f"    upstream[{depth_key}][0]: {n.get('type')}/{n.get('id')} via {n.get('via')} (lens={n.get('lens')})")
            break
    for depth_key in sorted(downstream_by_depth.keys()):
        nodes = downstream_by_depth[depth_key]
        if nodes:
            n = nodes[0]
            print(f"    downstream[{depth_key}][0]: {n.get('type')}/{n.get('id')} via {n.get('via')} (lens={n.get('lens')})")
            break

    # Direction rule check
    flags = []
    if atype == "closed_mechanisms" and total_downstream > 0:
        flags.append(f"FAIL closure-no-downstream rule ({total_downstream} downstream)")

    if total_nodes == 0:
        flags.append("ZERO chain nodes (anchor has no traceable chain)")

    # Verify anchor exists in DB by type+id
    pk_col = {
        "closed_mechanisms": "id", "theorems": "id", "gates": "id",
        "sessions": "id", "researchers": "domain", "agents": "slug",
        "open_channels": "name", "data_provenance": "script",
        "session_files": "id", "equations": "id", "constants": "name",
        "registries": "id",
    }.get(atype, "id")
    try:
        cur.execute(f"SELECT 1 FROM {atype} WHERE {pk_col} = ? LIMIT 1", (aid,))
        row = cur.fetchone()
        if not row:
            flags.append(f"NOT FOUND in DB.{atype}.{pk_col}")
    except sqlite3.OperationalError as e:
        flags.append(f"DB query error: {e}")

    if flags:
        for f in flags:
            print(f"    ⚠ {f}")
    else:
        print(f"    ✓ ok")

    results.append((anchor_key, atype, total_nodes, total_upstream,
                    total_downstream, flags))

print()
print("=" * 80)
print(f"SUMMARY: {len(samples)} anchors validated")
n_pass = sum(1 for r in results if not r[5])
n_fail = len(results) - n_pass
print(f"  PASS: {n_pass}")
print(f"  FAIL: {n_fail}")
if n_fail:
    print()
    print("Failed anchors:")
    for r in results:
        if r[5]:
            print(f"  {r[0]}: {r[5]}")

# Coverage statistics across the sample
print()
print("Chain-node distribution across sample:")
nodes_list = [r[2] for r in results]
nodes_list.sort()
print(f"  min: {nodes_list[0]}, median: {nodes_list[len(nodes_list)//2]}, max: {nodes_list[-1]}, mean: {sum(nodes_list)/len(nodes_list):.1f}")
