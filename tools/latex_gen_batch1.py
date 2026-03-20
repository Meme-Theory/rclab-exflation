#!/usr/bin/env python3
"""
Generate LaTeX for physics equations in s22c_landau_classification.txt
and the next highest-priority files.
"""
import json
import re

ROOT = "C:/sandbox/Ainulindale Exflation"

def load_index():
    with open(f"{ROOT}/tools/knowledge-index.json", "r", encoding="utf-8") as f:
        return json.load(f)

def generate_latex_for_raw(raw, eq_type, context=""):
    """Generate LaTeX from a raw expression."""
    r = raw.strip()

    # Numerical result patterns: "X = number" or "X = number (note)"
    m = re.match(r"^([A-Za-z_][A-Za-z_0-9'^{}()]*(?:\([^)]*\))?)\s*=\s*(.+)$", r)
    if m:
        lhs = m.group(1)
        rhs = m.group(2).strip()
        lhs_latex = convert_var_to_latex(lhs)
        rhs_latex = convert_rhs_to_latex(rhs)
        return f"{lhs_latex} = {rhs_latex}"

    # Inequality patterns: "X < Y" or "X > Y" or "X <= Y"
    for op, latex_op in [("<=", r"\leq"), (">=", r"\geq"), ("<<", r"\ll"), (">>", r"\gg"), ("<", "<"), (">", ">")]:
        if op in r and "=" not in r.replace(op, ""):
            parts = r.split(op, 1)
            if len(parts) == 2:
                return f"{convert_var_to_latex(parts[0].strip())} {latex_op} {convert_rhs_to_latex(parts[1].strip())}"

    # Specific patterns
    if r.startswith("tau=") or r.startswith("N="):
        return convert_diagnostic_line(r)

    # Sentence with equation - extract the equation part
    # e.g., "In the BEC regime, w = -1 EXACTLY"
    eq_match = re.search(r'([A-Za-z_][A-Za-z_0-9]*)\s*=\s*([0-9.e+\-]+)', r)
    if eq_match:
        var = eq_match.group(1)
        val = eq_match.group(2)
        return f"{convert_var_to_latex(var)} = {val}"

    # Fall through: return None (skip)
    return None

def convert_var_to_latex(v):
    """Convert a variable name to LaTeX."""
    v = v.strip()

    # Special multi-char variables
    replacements = {
        "V_CW": r"V_{\mathrm{CW}}",
        "V_IR": r"V_{\mathrm{IR}}",
        "V_eff": r"V_{\mathrm{eff}}",
        "V_tree": r"V_{\mathrm{tree}}",
        "E_ferm": r"E_{\mathrm{ferm}}",
        "E_Cas": r"E_{\mathrm{Cas}}",
        "E_Casimir": r"E_{\mathrm{Casimir}}",
        "F_cond": r"F_{\mathrm{cond}}",
        "F_pert": r"F_{\mathrm{pert}}",
        "F_true": r"F_{\mathrm{true}}",
        "F_normal": r"F_{\mathrm{normal}}",
        "G_tau_tau": r"G_{\tau\tau}",
        "G_i": r"G_i",
        "Delta_F": r"\Delta F",
        "N(0)": r"N(0)",
        "N(0)_singlet": r"N(0)_{\mathrm{singlet}}",
        "N(0)_total": r"N(0)_{\mathrm{total}}",
        "g*N(0)": r"g^* N(0)",
        "g*N(0)_sing": r"g^* N(0)_{\mathrm{sing}}",
        "g*N(0)_tot": r"g^* N(0)_{\mathrm{tot}}",
        "lambda_min": r"\lambda_{\min}",
        "d_int": r"d_{\mathrm{int}}",
        "d_uc": r"d_{\mathrm{uc}}",
        "d_eff": r"d_{\mathrm{eff}}",
        "delta_T": r"\delta T",
        "omega_modulus": r"\omega_{\mathrm{mod}}",
        "T_eff": r"T_{\mathrm{eff}}",
        "xi_0": r"\xi_0",
        "R^2": r"R^2",
        "M_max": r"M_{\max}",
        "theta_12": r"\theta_{12}",
        "sin^2(theta_W)": r"\sin^2\theta_W",
    }

    for k, v_rep in replacements.items():
        if v == k:
            return v_rep

    # Generic: single letter with subscript
    m = re.match(r"^([A-Za-z])_([A-Za-z0-9]+)$", v)
    if m:
        return f"{m.group(1)}_{{{m.group(2)}}}"

    # Greek letters
    greeks = ["alpha", "beta", "gamma", "delta", "epsilon", "zeta", "eta",
              "theta", "iota", "kappa", "lambda", "mu", "nu", "xi",
              "pi", "rho", "sigma", "tau", "upsilon", "phi", "chi", "psi", "omega",
              "Gamma", "Delta", "Theta", "Lambda", "Xi", "Pi", "Sigma", "Phi", "Psi", "Omega"]
    for g in greeks:
        if v == g:
            return f"\\{g}"

    # With prime
    if v.endswith("'"):
        base = convert_var_to_latex(v[:-1])
        return f"{base}'"
    if v.endswith("''"):
        base = convert_var_to_latex(v[:-2])
        return f"{base}''"

    return v

def convert_rhs_to_latex(rhs):
    """Convert RHS of equation to LaTeX."""
    rhs = rhs.strip()

    # Scientific notation: 1.234e+05 -> 1.234 \times 10^{5}
    rhs = re.sub(r'(\d+\.?\d*)e\+?(-?\d+)', lambda m: f"{m.group(1)} \\times 10^{{{int(m.group(2))}}}", rhs)

    # Replace common patterns
    rhs = rhs.replace("*", r" \cdot ")
    rhs = rhs.replace("sqrt(", r"\sqrt{").replace(")", "}")

    return rhs

def convert_diagnostic_line(r):
    """Convert diagnostic output lines like 'tau=0.10: g*N(0)_sing=2.96, ...'"""
    # These are multi-value diagnostic lines
    parts = []
    for segment in r.split(","):
        segment = segment.strip()
        m = re.match(r'([A-Za-z_*()0-9]+)\s*=\s*([0-9.e+\-]+)', segment)
        if m:
            var = convert_var_to_latex(m.group(1))
            val = m.group(2)
            # Scientific notation
            val = re.sub(r'(\d+\.?\d*)e\+?(-?\d+)', lambda mm: f"{mm.group(1)} \\times 10^{{{int(mm.group(2))}}}", val)
            parts.append(f"{var} = {val}")
    if parts:
        return ", \\quad ".join(parts)
    return None

def main():
    data = load_index()
    eqs = data['equations']

    # Target: structural/display/inline without LaTeX
    targets = [eq for eq in eqs
               if eq.get('type') in ('structural', 'display', 'inline')
               and not eq.get('latex')]

    generated = []
    skipped = []

    for eq in targets:
        raw = eq['raw']
        latex = generate_latex_for_raw(raw, eq.get('type', ''), eq.get('context', ''))
        if latex:
            generated.append({
                'id': eq['id'],
                'latex': latex,
                'raw': raw[:100],
            })
        else:
            skipped.append(eq['id'])

    print(f"Generated LaTeX for {len(generated)} equations")
    print(f"Skipped {len(skipped)} equations (no clear equation pattern)")

    # Save
    with open(f"{ROOT}/tools/latex_gen_results.json", "w", encoding="utf-8") as f:
        json.dump({
            'generated': generated,
            'skipped': skipped,
            'count_generated': len(generated),
            'count_skipped': len(skipped),
        }, f, indent=2)

    # Print first 30 for review
    print("\nFirst 30 generated:")
    for g in generated[:30]:
        print(f"  {g['id']}: {g['latex'][:100]}")
        print(f"    raw: {g['raw'][:80]}")

if __name__ == "__main__":
    main()
