"""
Batch 5 v2: Hand-triage sessions equations.
Classify each as MATH or SKIP, generate LaTeX only for MATH.
"""
import json, sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

with open('tools/knowledge-index.json') as f:
    idx = json.load(f)
eqs = idx['equations']
eq_map = {eq['id']: eq for eq in eqs}

mm_struct = [eq for eq in eqs
             if not eq.get('latex')
             and eq.get('type') in ('structural', 'inline')
             and 'sessions' in eq.get('source_file', '')]
mm_struct.sort(key=lambda x: (x['source_file'], x['line']))

def is_real_math(raw):
    """Heuristic: does this raw string contain a real equation worth rendering?"""
    r = raw.strip()
    # Must have an = sign or known math operator to be an equation
    has_eq = '=' in r
    has_ineq = any(op in r for op in ['<', '>', '<=', '>=', '~', 'neq'])
    has_math_sym = any(s in r for s in ['^{', '_{', '\\frac', '\\sum', '\\int',
                                         'pi', 'lambda', 'sigma', 'Delta',
                                         'sqrt', 'exp', 'log', 'ln',
                                         'Gamma', 'Tr(', 'det(', 'dim(',
                                         'Pf(', 'Ric', 'Vol('])

    # Reject long prose
    words = r.split()
    if len(words) > 20 and not has_eq:
        return False

    # Reject things that are clearly prose descriptions
    prose_starts = ['the ', 'this ', 'scan ', 'average ', 'within ', 'check ',
                    'note:', 'confirms', 'verified', 'result:', 'compare ',
                    'phase ', 'session ', 'convergence', 'we ', 'our ']
    for ps in prose_starts:
        if r.lower().startswith(ps):
            return False

    # Must have SOME mathematical content
    if has_eq or has_ineq or has_math_sym:
        # But reject simple status lines like "status = ok"
        if re.match(r'^[A-Z][a-z]+\s*=\s*\d', r) and len(words) < 5:
            return True
        return True

    # Reject data table rows
    if re.match(r'^\s*(N|tau)\s*=?\s*\d', r):
        if ':' in r and len(words) > 8:
            return False  # log line
        return True  # simple assignment

    return False

# Separate MATH from SKIP
math_eqs = []
skip_eqs = []
for eq in mm_struct:
    if is_real_math(eq['raw']):
        math_eqs.append(eq)
    else:
        skip_eqs.append(eq)

print(f"MATH (needs LaTeX): {len(math_eqs)}")
print(f"SKIP (prose/log):   {len(skip_eqs)}")
print()

# Show what we're skipping
print("=== SKIPPED (sample) ===")
for eq in skip_eqs[:20]:
    sf = os.path.basename(eq['source_file'])
    print(f"  {eq['id']} | {sf}:{eq['line']}")
    print(f"    {eq['raw'][:100]}")
print(f"  ... ({len(skip_eqs)} total)")
print()

# Show what we're converting
print("=== MATH (sample) ===")
for eq in math_eqs[:20]:
    sf = os.path.basename(eq['source_file'])
    print(f"  {eq['id']} | {sf}:{eq['line']}")
    print(f"    {eq['raw'][:100]}")
print(f"  ... ({len(math_eqs)} total)")
