"""Fix: use author's actual Patch A normalization (replace \\ -> /; then check /computations/ AND endswith txt|json)."""
import json
import re
from pathlib import Path
from collections import Counter

ROOT = Path('C:/sandbox/Ainulindale Exflation')
idx = json.loads((ROOT / 'tools/knowledge-index.json').read_text(encoding='utf-8'))
audit = json.loads((ROOT / 'tools/_anchor_validation_results.json').read_text())
eq_index = {e['id']: e for e in idx['equations']}


def patch_a_kills(source_file: str) -> bool:
    """Author's claimed Patch A check, applied to the entry's source_file string."""
    posix_path = source_file.replace('\\', '/').lower()
    # Note: author's snippet uses '/computations/' which requires a leading slash.
    # The actual entries have source_file starting with 'computations/' (no leading /).
    # This is a bug in the author's snippet — it wouldn't fire on the live index entries.
    # We test BOTH interpretations.
    A_strict = (
        (posix_path.endswith('.txt') or posix_path.endswith('.json'))
        and '/computations/' in posix_path
    )
    A_relaxed = (
        (posix_path.endswith('.txt') or posix_path.endswith('.json'))
        and ('computations/' in posix_path)
    )
    return A_strict, A_relaxed


# Re-derive Test 7 numbers using A_relaxed (matches the index)
noise_structurals = []
valid_structurals = []
for aid, av in audit['equations'].items():
    e = eq_index.get(aid)
    if not e or e['type'] != 'structural':
        continue
    if av['verdict'] == 'NOISE':
        noise_structurals.append(e)
    elif av['verdict'] == 'VALID':
        valid_structurals.append(e)

# Strict-leading-slash interpretation
n_strict = sum(1 for e in noise_structurals if patch_a_kills(e['source_file'])[0])
v_strict = sum(1 for e in valid_structurals if patch_a_kills(e['source_file'])[0])

# Relaxed: file just contains 'computations/' anywhere (this matches reality)
n_relaxed = sum(1 for e in noise_structurals if patch_a_kills(e['source_file'])[1])
v_relaxed = sum(1 for e in valid_structurals if patch_a_kills(e['source_file'])[1])

print('=== Patch A interpretation A: strict /computations/ (leading slash) ===')
print(f'  NOISE killed: {n_strict}/133')
print(f'  VALID killed: {v_strict}/266')
print()
print('=== Patch A interpretation B: relaxed computations/ (matches index strings) ===')
print(f'  NOISE killed: {n_relaxed}/133')
print(f'  VALID killed: {v_relaxed}/266')
print()
print('Sample source_file values to show what the entries actually look like:')
seen = set()
for e in noise_structurals + valid_structurals[:30]:
    sf = e['source_file']
    if sf not in seen and 'omputation' in sf.lower():
        print(f'  {sf}')
        seen.add(sf)
        if len(seen) > 10:
            break

# The author's snippet has a leading-slash bug: '/computations/' won't match
# 'computations\\session-22\\foo.txt' after replace('\\','/') → 'computations/session-22/foo.txt'
# because there's no leading '/'. This is a literal bug in the proposed Patch A code.

# ----- New regex behavior re-derived with proper test -----

# proposed Patch C regex
NEW_RE = re.compile(
    r'^[ ]{0,8}('
    r'(?:'
    r'  [A-Za-z_\\][\w]*'              # identifier or \latex command
    r'  (?:'
    r'    \([^()\n]{0,80}\)'           # (...) group, no nested
    r'    | \{[^{}\n]{0,80}\}'         # {...} group, no nested
    r'    | \^[\w{}()]+'               # ^... superscript
    r'    | _[\w{}()]+'                # _... subscript
    r"    | '+"                        # primes
    r'  )*'
    r')'
    r'\s*[=≡≈]\s*'
    r'[^\n|]{5,}'
    r')$',
    re.MULTILINE | re.VERBOSE,
)


def matches_new(s):
    return bool(NEW_RE.match(s + "\n"))


VERDICT_PIN_PREFIXES = (
    'audit_sha256', 'content_sha256', 'closure_sha256', 'sha256',
    'convention', 'scheme', 'value=', 'value =',
    'tier_pin', 'schema_version', 'supersedes',
    'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'PYTHONPATH'
)


def patch_b_kills(line: str) -> bool:
    first_tok = line.split('=', 1)[0].strip()
    for p in VERDICT_PIN_PREFIXES:
        if first_tok.startswith(p):
            return True
    if line.rstrip().endswith(':'):
        return True
    return False


def first_line(raw):
    return raw.split('\n', 1)[0].strip()


# Re-do union analysis with A_relaxed (the realistic interpretation)
a_kills = set()
b_kills = set()
c_kills = set()
for e in noise_structurals:
    line = first_line(e['raw'])
    if patch_a_kills(e['source_file'])[1]:
        a_kills.add(e['id'])
    if patch_b_kills(line):
        b_kills.add(e['id'])
    if not matches_new(line):
        c_kills.add(e['id'])

union = a_kills | b_kills | c_kills

print()
print('=== UPDATED Test 7 with relaxed Patch A (the realistic interpretation) ===')
print(f'  Patch A kills: {len(a_kills)}/133 NOISE')
print(f'  Patch B kills: {len(b_kills)}/133 NOISE')
print(f'  Patch C kills: {len(c_kills)}/133 NOISE')
print(f'  UNION:         {len(union)}/133 NOISE ({100.0*len(union)/133:.1f}%)')
print(f"  Author's stated combined: ~100/133 (~75%)")
print(f'  Intersections:')
print(f'    A∩B={len(a_kills & b_kills)}  A∩C={len(a_kills & c_kills)}  B∩C={len(b_kills & c_kills)}  A∩B∩C={len(a_kills & b_kills & c_kills)}')

print()
print('=== UPDATED VALID false-positive rates per patch ===')
v_a_kills = set(e['id'] for e in valid_structurals if patch_a_kills(e['source_file'])[1])
v_b_kills = set(e['id'] for e in valid_structurals if patch_b_kills(first_line(e['raw'])))
v_c_kills = set(e['id'] for e in valid_structurals if not matches_new(first_line(e['raw'])))
v_union = v_a_kills | v_b_kills | v_c_kills
print(f'  VALID killed by A: {len(v_a_kills)}/266 ({100.0*len(v_a_kills)/266:.1f}%)')
print(f'  VALID killed by B: {len(v_b_kills)}/266 ({100.0*len(v_b_kills)/266:.1f}%)')
print(f'  VALID killed by C: {len(v_c_kills)}/266 ({100.0*len(v_c_kills)/266:.1f}%)')
print(f'  VALID UNION DROPPED: {len(v_union)}/266 ({100.0*len(v_union)/266:.1f}%)')

# Look at what Patch A *uniquely* drops in VALID (i.e., entries that B and C would NOT have caught)
v_a_only = v_a_kills - v_b_kills - v_c_kills
print()
print(f'VALID entries that ONLY Patch A drops (lose if A applied, save if A removed): {len(v_a_only)}/266')
sample = sorted(v_a_only)[:20]
for vid in sample:
    e = next(x for x in valid_structurals if x['id'] == vid)
    print(f'  [{vid}] {e["source_file"]}')
    print(f'         {first_line(e["raw"])[:120]}')
