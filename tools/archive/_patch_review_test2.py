"""Verify the author's Patch A claim: drops 101 VALID structurals from computations/."""
import json
from pathlib import Path
from collections import Counter

ROOT = Path('C:/sandbox/Ainulindale Exflation')
idx = json.loads((ROOT / 'tools/knowledge-index.json').read_text(encoding='utf-8'))
audit = json.loads((ROOT / 'tools/_anchor_validation_results.json').read_text())
eq_index = {e['id']: e for e in idx['equations']}


def bucket_of(source_file: str) -> str:
    sf = source_file.replace('\\', '/').lower()
    if '/computations/' in sf or sf.startswith('computations/'):
        if sf.endswith('.txt'):
            return 'computations_*.txt'
        elif sf.endswith('.json'):
            return 'computations_*.json'
        elif sf.endswith('.py'):
            return 'computations_*.py'
        else:
            return 'computations_other'
    elif 'session-plan' in sf:
        return 'session_plan'
    elif '/workshops/' in sf or '\\workshops\\' in sf:
        return 'workshop_md'
    elif 'sessions/framework' in sf:
        return 'framework_md'
    elif 'sessions/' in sf:
        return 'session_md'
    else:
        return 'other'


src_dist_valid = Counter()
src_dist_noise = Counter()
for aid, av in audit['equations'].items():
    e = eq_index.get(aid)
    if not e or e['type'] != 'structural':
        continue
    bk = bucket_of(e['source_file'])
    if av['verdict'] == 'VALID':
        src_dist_valid[bk] += 1
    else:
        src_dist_noise[bk] += 1

print('=== Audited STRUCTURAL distribution by source_file bucket ===')
all_buckets = sorted(set(src_dist_valid) | set(src_dist_noise))
print(f'{"bucket":30s} {"VALID":>6s} {"NOISE":>6s} {"NOISE%":>8s}')
for k in all_buckets:
    v = src_dist_valid[k]
    n = src_dist_noise[k]
    tot = v + n
    pct = (100.0 * n / tot) if tot else 0
    print(f'{k:30s} {v:>6d} {n:>6d} {pct:>7.1f}%')

print()
print('=== Sample VALID computations/*.txt and *.json entries ===')
n_shown = 0
for aid, av in audit['equations'].items():
    e = eq_index.get(aid)
    if not e or e['type'] != 'structural' or av['verdict'] != 'VALID':
        continue
    bk = bucket_of(e['source_file'])
    if bk in ('computations_*.txt', 'computations_*.json'):
        first = e['raw'].split('\n', 1)[0]
        print(f'  [{aid}] src={e["source_file"]}')
        print(f'         raw: {first[:140]}')
        n_shown += 1
        if n_shown >= 15:
            break

if n_shown == 0:
    print('  (none)')

print()
print('=== Total VALID-structural entries in computations/*.txt|*.json ===')
v_in_compute_txt = src_dist_valid['computations_*.txt'] + src_dist_valid['computations_*.json']
n_in_compute_txt = src_dist_noise['computations_*.txt'] + src_dist_noise['computations_*.json']
print(f'VALID: {v_in_compute_txt}    NOISE: {n_in_compute_txt}    Sum: {v_in_compute_txt + n_in_compute_txt}')
print()
print('Author claimed: Patch A "closes ~39 of 133 NOISE; drops 101 VALID structurals that duplicate data_provenance content"')
print(f'Empirical:      Patch A closes {n_in_compute_txt} of 133 NOISE; drops {v_in_compute_txt} VALID structurals')
