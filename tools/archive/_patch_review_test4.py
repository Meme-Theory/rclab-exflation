"""Verify Patch A claim: VALID structurals in computations/*.txt duplicate data_provenance content.

The author claims dropping them is safe because data_provenance retains the same info.
Check: pick 30 VALID-A-only entries, search data_provenance for their raw content.
"""
import json
from pathlib import Path

ROOT = Path('C:/sandbox/Ainulindale Exflation')
idx = json.loads((ROOT / 'tools/knowledge-index.json').read_text(encoding='utf-8'))
audit = json.loads((ROOT / 'tools/_anchor_validation_results.json').read_text())
eq_index = {e['id']: e for e in idx['equations']}

# Find structural VALID entries in computations/*.txt|json
candidates = []
for aid, av in audit['equations'].items():
    if av['verdict'] != 'VALID':
        continue
    e = eq_index.get(aid)
    if not e or e['type'] != 'structural':
        continue
    sf = e['source_file'].replace('\\', '/').lower()
    if 'computations/' in sf and (sf.endswith('.txt') or sf.endswith('.json')):
        candidates.append(e)

print(f"Found {len(candidates)} VALID structurals in computations/*.txt or *.json")

# Build a content index of data_provenance and other equation tables
dp = idx.get('data_provenance', [])
print(f"data_provenance entries: {len(dp)}")
print(f"data_provenance sample entry keys: {list(dp[0].keys())}")
print(f"  sample: {dp[0]}")
print()

# Build a content-search corpus over data_provenance
dp_corpus = []
for d in dp:
    text_blob = ' '.join(str(v) for v in d.values() if v)
    dp_corpus.append((d, text_blob))


def search_dp(needle: str, n_max=3):
    needle = needle.strip()
    if len(needle) < 8:
        return []
    hits = []
    for d, blob in dp_corpus:
        if needle in blob:
            hits.append(d.get('artifact_path', d.get('name', '<?>')))
            if len(hits) >= n_max:
                return hits
    return hits


# Sample 30 entries; check if their content appears in data_provenance
import random
random.seed(42)
sample = random.sample(candidates, min(30, len(candidates)))
found_in_dp = 0
not_found = []
for e in sample:
    first = e['raw'].split('\n', 1)[0].strip()
    # Try the equation literal LHS as the key
    if '=' in first:
        lhs = first.split('=', 1)[0].strip()
        # Search either LHS or full first
        hits = search_dp(first[:50])
        if not hits:
            hits = search_dp(lhs)
        if hits:
            found_in_dp += 1
        else:
            not_found.append((e, first))
    else:
        not_found.append((e, first))


print(f"=== Patch A claim test: {found_in_dp}/{len(sample)} VALID entries' content found in data_provenance ===")
print()
print("Sample VALID entries NOT found in data_provenance:")
for e, first in not_found[:20]:
    print(f"  [{e['id']}] {e['source_file']}")
    print(f"    first line: {first[:130]}")

# Also: are these entries used elsewhere — e.g., theorem statements, registry, anything else?
# Check inline math and display math equations for the same content
inline_eqs = [e for e in idx['equations'] if e['type'] == 'inline']
display_eqs = [e for e in idx['equations'] if e['type'] == 'display']
print()
print(f"For reference: inline equations={len(inline_eqs)}, display equations={len(display_eqs)}")


# Are these actually unique (in the sense the value is uniquely visible HERE)?
# Build a corpus of all RAW equation content across the 22593 equations
raw_lookup = {}
for e in idx['equations']:
    first = e['raw'].split('\n', 1)[0].strip()
    raw_lookup.setdefault(first[:80], []).append(e)

unique_to_compute_txt = 0
for e in sample:
    first = e['raw'].split('\n', 1)[0].strip()[:80]
    others = [x for x in raw_lookup.get(first, []) if x['id'] != e['id']]
    if not others:
        unique_to_compute_txt += 1

print()
print(f"=== Of the 30 sample VALID-in-compute-txt entries, "
      f"{unique_to_compute_txt} have NO duplicate-content equation entry elsewhere ===")
