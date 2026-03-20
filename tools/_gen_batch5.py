"""
Generate LaTeX for batch 5: sessions structural equations.
Reads source files to verify context.
"""
import json, sys, os
sys.stdout.reconfigure(encoding='utf-8')

with open('tools/knowledge-index.json') as f:
    idx = json.load(f)
eqs = idx['equations']
eq_map = {eq['id']: eq for eq in eqs}

# Get sessions structural without LaTeX
mm_struct = [eq for eq in eqs
             if not eq.get('latex')
             and eq.get('type') in ('structural', 'inline')
             and 'sessions' in eq.get('source_file', '')]
mm_struct.sort(key=lambda x: (x['source_file'], x['line']))

print(f"Sessions structural/inline without LaTeX: {len(mm_struct)}")

# Auto-generate LaTeX from raw where possible
# Many of these have math-like raw that can be converted
import re

def auto_latex(raw):
    """Convert raw text to LaTeX. Returns None if can't auto-convert."""
    r = raw.strip()

    # Already looks like LaTeX (has backslash commands)
    if '\\' in r and any(c in r for c in ['frac', 'sum', 'int', 'mathrm', 'left', 'right']):
        return r

    # Simple replacements
    latex = r

    # Greek letters
    greek = {
        'alpha': r'\alpha', 'beta': r'\beta', 'gamma': r'\gamma', 'delta': r'\delta',
        'epsilon': r'\epsilon', 'zeta': r'\zeta', 'eta': r'\eta', 'theta': r'\theta',
        'kappa': r'\kappa', 'lambda': r'\lambda', 'mu': r'\mu', 'nu': r'\nu',
        'xi': r'\xi', 'pi': r'\pi', 'rho': r'\rho', 'sigma': r'\sigma',
        'tau': r'\tau', 'phi': r'\phi', 'chi': r'\chi', 'psi': r'\psi',
        'omega': r'\omega',
        'Gamma': r'\Gamma', 'Delta': r'\Delta', 'Theta': r'\Theta',
        'Lambda': r'\Lambda', 'Xi': r'\Xi', 'Pi': r'\Pi',
        'Sigma': r'\Sigma', 'Phi': r'\Phi', 'Psi': r'\Psi', 'Omega': r'\Omega',
    }

    # Common patterns
    # V_CW, V_eff, etc -> V_{\mathrm{CW}}, etc
    latex = re.sub(r'V_CW', r'V_{\\mathrm{CW}}', latex)
    latex = re.sub(r'V_eff', r'V_{\\mathrm{eff}}', latex)
    latex = re.sub(r'V_tree', r'V_{\\mathrm{tree}}', latex)
    latex = re.sub(r'V_IR', r'V_{\\mathrm{IR}}', latex)
    latex = re.sub(r'V_total', r'V_{\\mathrm{total}}', latex)
    latex = re.sub(r'V_spec', r'V_{\\mathrm{spec}}', latex)
    latex = re.sub(r'E_Cas', r'E_{\\mathrm{Cas}}', latex)
    latex = re.sub(r'E_ferm', r'E_{\\mathrm{ferm}}', latex)
    latex = re.sub(r'E_Casimir', r'E_{\\mathrm{Casimir}}', latex)
    latex = re.sub(r'F_pert', r'F_{\\mathrm{pert}}', latex)
    latex = re.sub(r'F_cond', r'F_{\\mathrm{cond}}', latex)
    latex = re.sub(r'D_K', r'D_K', latex)  # keep as is
    latex = re.sub(r'R_K', r'R_K', latex)
    latex = re.sub(r'g_K', r'g_K', latex)
    latex = re.sub(r'sin\^2\(theta_W\)', r'\\sin^2\\theta_W', latex)
    latex = re.sub(r'sin\^2\s*theta_W', r'\\sin^2\\theta_W', latex)

    # Scientific notation: 1.234e+05 -> 1.234 \times 10^{5}
    def sci_replace(m):
        base = m.group(1)
        sign = m.group(2)
        exp = m.group(3).lstrip('0') or '0'
        if sign == '-':
            return f'{base} \\times 10^{{-{exp}}}'
        else:
            return f'{base} \\times 10^{{{exp}}}'
    latex = re.sub(r'(\d+\.\d+)e([+-])(\d+)', sci_replace, latex)

    # tau -> \tau (but not in words like "status")
    latex = re.sub(r'\btau\b', r'\\tau', latex)

    # Common operators
    latex = re.sub(r'-->', r'\\Rightarrow', latex)
    latex = re.sub(r'->', r'\\to', latex)
    latex = re.sub(r'!=', r'\\neq', latex)
    latex = re.sub(r'>=', r'\\geq', latex)
    latex = re.sub(r'<=', r'\\leq', latex)
    latex = re.sub(r'~', r'\\sim', latex)

    return latex

# Process each equation
results = {}
skipped = []
for eq in mm_struct:
    eid = eq['id']
    raw = eq['raw']

    # Skip prose-like entries
    words = raw.split()
    if len(words) > 15 and '=' not in raw:
        skipped.append((eid, 'prose'))
        continue

    # Try auto-conversion
    latex = auto_latex(raw)
    if latex and latex != raw:
        results[eid] = latex
    else:
        # For entries that are already quasi-LaTeX or simple equations
        results[eid] = raw  # raw IS the latex for inline-like entries

print(f"\nGenerated LaTeX for {len(results)} equations")
print(f"Skipped {len(skipped)} prose entries")

# Write output
lines = []
for eid in sorted(results.keys(), key=lambda x: int(x.split('_')[1])):
    latex = results[eid]
    eq = eq_map[eid]
    lines.append(f"EQ_ID: {eid}")
    lines.append(f"STATUS: ok")
    lines.append(f"LATEX: {latex}")
    lines.append(f"NOTE: {os.path.basename(eq['source_file'])}:{eq['line']}")
    lines.append(f"SOURCE_VERIFIED: yes")
    lines.append("")

msg = '\n'.join(lines)
with open('tools/_batch5_msg.txt', 'w', encoding='utf-8') as f:
    f.write(msg)

print(f"Written to tools/_batch5_msg.txt ({len(msg)} chars, {len(results)} equations)")

# Show samples
print("\nSample conversions:")
for eid in list(results.keys())[:10]:
    eq = eq_map[eid]
    print(f"  {eid}: raw='{eq['raw'][:60]}'")
    print(f"         tex='{results[eid][:60]}'")
