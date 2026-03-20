#!/usr/bin/env python3
"""
Deep LaTeX audit: determine which equations have genuinely wrong LaTeX
vs. which are correct renderings that our token heuristic misjudged.

Strategy: strip ALL LaTeX formatting from both raw and latex, then compare
the resulting "mathematical skeleton" (just letters, digits, operators).
"""
import json
import re

def math_skeleton(s, is_latex=False):
    """Extract the mathematical skeleton: variables, numbers, operators.
    For LaTeX: first undo all formatting commands to get the math content."""
    if is_latex:
        # Replace \mathrm{X}, \text{X}, \mathcal{X}, \mathbb{X} with just X
        s = re.sub(r'\\(?:mathrm|text|mathcal|mathbb|boldsymbol|hat)\{([^}]*)\}', r'\1', s)
        # Replace \operatorname{X} with X
        s = re.sub(r'\\operatorname\{([^}]*)\}', r'\1', s)
        # Replace \frac{A}{B} with A/B
        s = re.sub(r'\\frac\{([^}]*)\}\{([^}]*)\}', r'\1/\2', s)
        # Replace \sqrt{X} with sqrt(X)
        s = re.sub(r'\\sqrt\{([^}]*)\}', r'sqrt(\1)', s)
        # Replace \left, \right, \!, \;, \quad, \, with nothing
        s = re.sub(r'\\(?:left|right|!|;|quad|,|:)', '', s)
        # Replace \ln, \log, \exp, \sin, \cos, \det, \dim, \min, \max with the word
        s = re.sub(r'\\(ln|log|exp|sin|cos|det|dim|min|max|lim|Tr|tr|Re|Im|sup|inf)', r'\1', s)
        # Replace \sum, \int, \prod with the word
        s = re.sub(r'\\(sum|int|prod)', r'\1', s)
        # Replace \cdot, \times with *
        s = re.sub(r'\\(?:cdot|times)', '*', s)
        # Replace \oplus with +, \otimes with x
        s = re.sub(r'\\oplus', '+', s)
        s = re.sub(r'\\otimes', 'tensor', s)
        # Replace \langle, \rangle with < >
        s = re.sub(r'\\langle', '<', s)
        s = re.sub(r'\\rangle', '>', s)
        # Replace \leq, \geq, \neq, \approx, \equiv with symbols
        s = re.sub(r'\\leq', '<=', s)
        s = re.sub(r'\\geq', '>=', s)
        s = re.sub(r'\\neq', '!=', s)
        s = re.sub(r'\\approx', '~', s)
        s = re.sub(r'\\equiv', '==', s)
        # Replace \tag{X} with nothing
        s = re.sub(r'\\tag\{[^}]*\}', '', s)
        # Replace remaining \command with nothing (Greek letters etc.)
        # But KEEP the command name for Greek: \alpha -> alpha, \lambda -> lambda, etc.
        s = re.sub(r'\\([a-zA-Z]+)', r'\1', s)
    else:
        # For raw: replace common ASCII math notations
        s = s.replace('tensor', 'tensor')
        s = s.replace('**', '^')
        s = s.replace('integral', 'int')
        s = s.replace('SUM', 'sum')
        s = s.replace('Sum', 'sum')

    # Now normalize both: remove all punctuation except letters, digits, dots, +, -, *, /, ^, =, <, >, ~
    s = s.lower()
    s = re.sub(r'[{}()\[\]|\\,;:!@#$&_\'"` ]', ' ', s)
    # Collapse whitespace
    s = re.sub(r'\s+', ' ', s).strip()
    return s

def compare_skeletons(raw_skel, latex_skel):
    """Compare two math skeletons. Return overlap ratio."""
    raw_words = set(raw_skel.split())
    latex_words = set(latex_skel.split())

    # Remove very short trivial tokens
    trivial = {'', 'a', 'b', 'c', 'd', 'e', 'f', 'i', 'j', 'k', 'n', 's', 't', 'x', 'y', 'z',
               'the', 'is', 'at', 'of', 'in', 'for', 'and', 'to', 'with', 'from', 'by',
               'if', 'or', 'no', 'on', 'an', 'up', 'be', 'do', 'so', 'as', 'we'}
    raw_words -= trivial
    latex_words -= trivial

    if not raw_words:
        return 1.0  # nothing to compare

    overlap = len(raw_words & latex_words)
    return overlap / len(raw_words)

def main():
    with open("tools/knowledge-index.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    eqs = data.get("equations", [])

    has_latex = [eq for eq in eqs if eq.get("latex")]
    print(f"Equations with LaTeX: {len(has_latex)}")

    correct = []  # LaTeX correctly renders raw
    wrong = []    # LaTeX is a different equation entirely
    partial = []  # Partial match / unclear

    for eq in has_latex:
        raw = eq.get("raw", "")
        latex = eq.get("latex", "")
        eid = eq["id"]

        raw_skel = math_skeleton(raw, is_latex=False)
        latex_skel = math_skeleton(latex, is_latex=True)

        ratio = compare_skeletons(raw_skel, latex_skel)

        if ratio >= 0.35:
            correct.append((eid, ratio))
        elif ratio >= 0.15:
            partial.append((eid, eq.get("type"), raw[:100], latex[:100], raw_skel[:80], latex_skel[:80], ratio))
        else:
            wrong.append((eid, eq.get("type"), raw[:120], latex[:120], raw_skel[:80], latex_skel[:80], ratio))

    print(f"\nCorrect LaTeX renderings: {len(correct)}")
    print(f"Partial/borderline: {len(partial)}")
    print(f"WRONG LaTeX (different equation): {len(wrong)}")

    # Manual re-check: many in "wrong" might be correct renderings where ASCII->LaTeX
    # loses ALL token matches because of notation shift
    # Let's look at wrong list and identify true vs false positives
    truly_wrong = []
    false_positives = []

    for eid, etype, raw, latex, raw_skel, latex_skel, ratio in wrong:
        # Key test: does the LaTeX have the SAME LHS as the raw?
        raw_lhs = re.match(r'([A-Za-z_][A-Za-z_0-9\'^{}()\[\]*]*)\s*[=<>~]', raw)
        latex_lhs = re.match(r'([A-Za-z_\\{}0-9\'^]*)\s*[=<>~]', latex)

        if raw_lhs and latex_lhs:
            raw_lhs_clean = math_skeleton(raw_lhs.group(1))
            latex_lhs_clean = math_skeleton(latex_lhs.group(1), is_latex=True)
            if raw_lhs_clean and latex_lhs_clean and (raw_lhs_clean in latex_lhs_clean or latex_lhs_clean in raw_lhs_clean):
                false_positives.append((eid, etype, raw, latex, "LHS match"))
                continue

        # Check if it's a code-to-math translation (e.g. V_eff vs V_{eff})
        raw_clean = raw.lower().replace('_', '').replace('^', '').replace(' ', '').replace('*', '')
        latex_clean = re.sub(r'\\[a-z]+', '', latex.lower()).replace('{', '').replace('}', '').replace('_', '').replace('^', '').replace(' ', '')
        # Compare first 20 chars of cleaned versions
        if len(raw_clean) > 5 and len(latex_clean) > 5:
            if raw_clean[:10] == latex_clean[:10]:
                false_positives.append((eid, etype, raw, latex, "prefix match after cleanup"))
                continue

        truly_wrong.append((eid, etype, raw, latex, ratio))

    print(f"\nAfter manual re-check:")
    print(f"  Truly WRONG LaTeX: {len(truly_wrong)}")
    print(f"  False positives (actually correct): {len(false_positives)}")

    print("\n=== TRULY WRONG LaTeX (needs replacement) ===")
    for eid, etype, raw, latex, ratio in truly_wrong:
        print(f"\n  {eid} [{etype}] (overlap={ratio:.0%}):")
        print(f"    RAW:   {raw}")
        print(f"    LATEX: {latex}")

    print("\n=== FALSE POSITIVES (correct renderings) ===")
    for eid, etype, raw, latex, reason in false_positives:
        print(f"  {eid} [{etype}]: {reason}")

    # Summary stats
    print(f"\n=== FINAL SUMMARY ===")
    print(f"Total with LaTeX: {len(has_latex)}")
    print(f"Correct: {len(correct) + len(false_positives)}")
    print(f"Borderline: {len(partial)}")
    print(f"WRONG: {len(truly_wrong)}")

    # Return the truly wrong IDs for the report
    wrong_ids = [eid for eid, _, _, _, _ in truly_wrong]
    print(f"\nWrong equation IDs: {wrong_ids}")

if __name__ == "__main__":
    main()
