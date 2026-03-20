"""
Comment equation triage: classify 2,945 comment-type equations as
substantive (real physics worth LaTeX-formatting) vs skip.

Heuristic classification:
  substantive: contains '=' with physics symbols, dimensional analysis, scaling relations
  skip: variable assignments, numpy/python, file paths, TODO/FIXME, debug prints, prose
"""
import json
import re
from collections import Counter

with open('tools/knowledge-index.json', 'r', encoding='utf-8') as f:
    ki = json.load(f)

comments = [e for e in ki.get('equations', []) if e.get('type') == 'comment']
print(f"Total comment equations: {len(comments)}")

# Physics symbols that suggest substantive content
PHYSICS_PATTERNS = [
    r'lambda', r'omega', r'C_2', r'Casimir', r'D_K', r'D_P',
    r'R_K', r'R_{', r'Ric', r'Riem', r'Weyl',
    r'sin\^2', r'theta_W', r'alpha_', r'g_1', r'g_2',
    r'V_eff', r'V_CW', r'V_tree', r'F_Casimir',
    r'Delta_L', r'nabla', r'Laplacian', r'Lichnerowicz',
    r'Tr\(', r'Tr ', r'det\(', r'Pf\(',
    r'hbar', r'kappa', r'sigma', r'beta\s*=', r'mu\s*=',
    r'pi\^', r'pi\s*\*', r'4\s*pi',
    r'BF\s*=', r'BF_', r'log-odds', r'posterior',
    r'dim\(', r'dim_', r'mult_', r'DOF',
    r'eigenvalue', r'eigenvector', r'spectrum',
    r'boson', r'fermion', r'spinor', r'scalar',
    r'instanton', r'condensate', r'gap\s*equation',
    r'Seeley', r'DeWitt', r'heat\s*kernel',
    r'Peter.Weyl', r'irrep', r'representation',
    r'Friedmann', r'Hubble', r'dark\s*energy',
    r'Weinberg', r'Higgs', r'Yukawa',
    r'Jensen', r'deformation', r'modulus',
    r'\^2\s*=', r'\^4\s*=', r'\^{',
    r'int_', r'integral', r'sum_', r'Sum_',
    r'exp\(', r'exp\{', r'e\^{',
    r'f\(D', r'Tr\s*f\(',
]

# Skip patterns (code, debug, procedural)
SKIP_PATTERNS = [
    r'np\.', r'numpy', r'scipy', r'matplotlib',
    r'import\s', r'from\s.*import',
    r'def\s+\w+\(', r'class\s+\w+',
    r'\.py', r'\.npz', r'\.png', r'\.txt', r'\.json',
    r'print\(', r'print\s*\(',
    r'TODO', r'FIXME', r'HACK', r'XXX',
    r'#\s*---', r'#\s*===',
    r'assert\s', r'raise\s',
    r'for\s+\w+\s+in\s', r'while\s',
    r'if\s+\w+\s*[><=!]', r'elif\s', r'else:',
    r'return\s', r'yield\s',
    r'try:', r'except\s',
    r'torch\.', r'cuda', r'\.to\(device',
    r'os\.path', r'pathlib', r'glob\(',
    r'json\.', r'h5py',
    r'\[\s*\d+\s*:\s*\d+\s*\]',  # array slicing
    r'\.shape', r'\.dtype', r'\.size',
    r'plt\.', r'fig,\s*ax', r'savefig',
    r'pq_sum', r'max_pq',
]

def classify(raw):
    """Classify a comment equation as substantive or skip."""
    if not raw:
        return 'skip', 'empty'

    raw_lower = raw.lower()

    # Strong skip signals
    for pat in SKIP_PATTERNS:
        if re.search(pat, raw, re.IGNORECASE):
            return 'skip', f'code/procedural ({pat})'

    # Check for '=' with something that looks like physics
    has_equals = '=' in raw

    # Strong substantive signals
    physics_hits = []
    for pat in PHYSICS_PATTERNS:
        if re.search(pat, raw, re.IGNORECASE):
            physics_hits.append(pat)

    if has_equals and len(physics_hits) >= 2:
        return 'substantive', f'physics ({", ".join(physics_hits[:3])})'

    if len(physics_hits) >= 3:
        return 'substantive', f'physics-dense ({", ".join(physics_hits[:3])})'

    # Moderate signals
    if has_equals and len(physics_hits) >= 1:
        # Check if the '=' is in a real equation context (not just "x = 5" or prose)
        # Look for math-like patterns around the '='
        if re.search(r'[a-zA-Z_]\w*\s*=\s*[-+]?\d*\.?\d+', raw):
            # Simple numeric assignment -- could be either
            if len(raw) < 40:
                return 'skip', 'short assignment'
        return 'substantive', f'equation ({", ".join(physics_hits[:2])})'

    if has_equals and len(raw) > 20:
        # Has equals but no physics keywords -- check for math operators
        if re.search(r'[\+\-\*/\^].*=|=.*[\+\-\*/\^]', raw):
            return 'borderline', 'arithmetic without physics keywords'

    # Default: if short and no physics content, skip
    if len(raw) < 30 and not physics_hits:
        return 'skip', 'short, no physics'

    if physics_hits:
        return 'borderline', f'some physics ({", ".join(physics_hits[:2])})'

    return 'skip', 'no physics content detected'

# Run classification
results = []
for e in comments:
    cat, reason = classify(e.get('raw', ''))
    results.append({
        'id': e['id'],
        'raw': e.get('raw', ''),
        'session': e.get('session', ''),
        'source_file': e.get('source_file', ''),
        'line': e.get('line', 0),
        'category': cat,
        'reason': reason
    })

# Count categories
cats = Counter(r['category'] for r in results)
print(f"\nClassification results:")
for cat, count in cats.most_common():
    print(f"  {cat}: {count}")

# Show substantive ones
substantive = [r for r in results if r['category'] == 'substantive']
borderline = [r for r in results if r['category'] == 'borderline']
skipped = [r for r in results if r['category'] == 'skip']

print(f"\n=== SUBSTANTIVE ({len(substantive)}) ===")
for r in substantive[:30]:
    raw = r['raw'][:100]
    print(f"  {r['id']} [{r['session']}] {r['reason'][:40]} | {raw}")

print(f"\n=== BORDERLINE ({len(borderline)}) ===")
for r in borderline[:20]:
    raw = r['raw'][:100]
    print(f"  {r['id']} [{r['session']}] {r['reason'][:40]} | {raw}")

print(f"\n=== SKIP (showing first 10 of {len(skipped)}) ===")
for r in skipped[:10]:
    raw = r['raw'][:100]
    print(f"  {r['id']} [{r['session']}] {r['reason'][:40]} | {raw}")

# Session distribution of substantive
sess_dist = Counter(r['session'] for r in substantive)
print(f"\nSubstantive by session:")
for s, c in sess_dist.most_common(15):
    print(f"  {s}: {c}")

# Save classification for batch processing
with open('tools/_comment_triage_results.json', 'w', encoding='utf-8') as f:
    json.dump({
        'total': len(comments),
        'substantive': len(substantive),
        'borderline': len(borderline),
        'skip': len(skipped),
        'substantive_ids': [r['id'] for r in substantive],
        'borderline_ids': [r['id'] for r in borderline],
        'results': results
    }, f, indent=2, ensure_ascii=False)

print(f"\nClassification saved to tools/_comment_triage_results.json")
