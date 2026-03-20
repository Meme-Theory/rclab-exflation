"""
Triage structural+inline equations without LaTeX into:
  - MATH: genuine equations that need LaTeX rendering
  - LOG: computational output / data tables / prose with numbers
  - PROSE: descriptive text that was misclassified as structural
"""
import json, sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('tools/knowledge-index.json') as f:
    idx = json.load(f)
eqs = idx['equations']

needs_work = [eq for eq in eqs if not eq.get('latex') and eq.get('type') in ('structural', 'inline')]
needs_work.sort(key=lambda x: (x['source_file'], x['line']))

# Classification heuristics
def classify(raw):
    r = raw.strip()

    # Clearly prose (long sentences without math operators)
    words = r.split()
    if len(words) > 12 and '=' not in r:
        return 'PROSE'

    # Python artifacts
    if 'np.float64' in r or 'np.int64' in r:
        return 'LOG'

    # Log output patterns: "N=20: ..." format
    if re.match(r'^N\s*=\s*\d+:', r):
        return 'LOG'

    # Data ranges: "range [-1.2250, -1.0387]"
    if 'range [' in r:
        return 'LOG'

    # Regime labels without real math
    if r.startswith('regime=') or 'regime=BEC' in r:
        return 'LOG'

    # Computational status messages
    if any(x in r.lower() for x in ['confirmed', 'monotonically increasing', 'monotonically decreasing',
                                      'spinodal', 'no spinodal', 'no ir spinodal']):
        if '=' in r and any(c.isdigit() for c in r):
            # Has an actual equation embedded
            return 'MATH'
        return 'LOG'

    # Gate verdicts and status
    if any(x in r for x in ['--> IR SPINODAL', '--> CLOSED', '--> PASS', '--> FAIL',
                             '--> NEUTRAL', '--> COMPELLING']):
        # These contain embedded equations worth rendering
        if '=' in r:
            return 'MATH'
        return 'LOG'

    # Prose descriptions with "the" "is" "was" etc
    prose_words = ['the ', 'is ', 'was ', 'are ', 'has ', 'used ', 'tesla ', 'below ',
                   'above ', 'within ', 'only ', 'this ', 'both ']
    prose_count = sum(1 for pw in prose_words if pw.lower() in r.lower())
    if prose_count >= 2 and len(words) > 8:
        return 'PROSE'

    # Has equation-like content
    if '=' in r and any(c.isdigit() or c in 'eE+-' for c in r):
        return 'MATH'

    # Has explicit math symbols
    if any(s in r for s in ['\\frac', '\\sum', '\\int', '\\prod', '^{', '_{',
                            'lambda', 'sigma', 'tau', 'Delta', 'Gamma', 'pi']):
        return 'MATH'

    # Short expressions with = sign
    if '=' in r and len(words) <= 8:
        return 'MATH'

    # Default: if it has numbers and operators, treat as math
    if re.search(r'\d+\.?\d*\s*[<>=]', r):
        return 'MATH'

    return 'PROSE'


math_eqs = []
log_eqs = []
prose_eqs = []

for eq in needs_work:
    cat = classify(eq['raw'])
    if cat == 'MATH':
        math_eqs.append(eq)
    elif cat == 'LOG':
        log_eqs.append(eq)
    else:
        prose_eqs.append(eq)

print(f"TRIAGE RESULTS ({len(needs_work)} total):")
print(f"  MATH (needs LaTeX):  {len(math_eqs)}")
print(f"  LOG (data output):   {len(log_eqs)}")
print(f"  PROSE (misclassified): {len(prose_eqs)}")
print()

print("=== MATH EQUATIONS (sample) ===")
for eq in math_eqs[:30]:
    sf = eq['source_file'].split('\\')[-1]
    print(f"  {eq['id']} | {sf}:{eq['line']}")
    print(f"    {eq['raw'][:120]}")
print(f"  ... ({len(math_eqs)} total)")
print()

print("=== LOG OUTPUT (sample) ===")
for eq in log_eqs[:15]:
    sf = eq['source_file'].split('\\')[-1]
    print(f"  {eq['id']} | {sf}:{eq['line']}")
    print(f"    {eq['raw'][:120]}")
print(f"  ... ({len(log_eqs)} total)")
print()

print("=== PROSE (sample) ===")
for eq in prose_eqs[:15]:
    sf = eq['source_file'].split('\\')[-1]
    print(f"  {eq['id']} | {sf}:{eq['line']}")
    print(f"    {eq['raw'][:120]}")
print(f"  ... ({len(prose_eqs)} total)")
