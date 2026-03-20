#!/usr/bin/env python3
"""
Systematic file-by-file equation audit.
For each source file: read it once, check every equation's raw against the actual line.
For equations with LaTeX: verify semantic correspondence.
Output: per-file results, aggregated findings.
"""
import json
import os
import re
import sys
from collections import defaultdict, Counter

ROOT = "C:/sandbox/Ainulindale Exflation"

def read_file(src_file):
    path = os.path.join(ROOT, src_file.replace("\\", "/"))
    if not os.path.exists(path):
        return None
    for enc in ("utf-8", "utf-8-sig", "latin-1", "cp1252"):
        try:
            with open(path, "r", encoding=enc, errors="replace") as f:
                return f.readlines()
        except:
            continue
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        return f.readlines()

def normalize(s):
    return re.sub(r'\s+', ' ', s.strip())

def check_raw_match(raw, lines, line_num, window=5):
    """Check if raw appears at or near the indicated line."""
    if not lines:
        return "file_missing", 0
    if line_num < 1 or line_num > len(lines):
        return "line_oob", 0

    raw_n = normalize(raw)

    # Check exact line
    src = normalize(lines[line_num - 1])
    if raw_n in src or src in raw_n or (len(raw_n) > 15 and raw_n[:30] in src):
        return "ok", line_num

    # Check window
    for off in range(-window, window + 1):
        if off == 0:
            continue
        idx = line_num - 1 + off
        if 0 <= idx < len(lines):
            neighbor = normalize(lines[idx])
            if raw_n in neighbor or neighbor in raw_n or (len(raw_n) > 15 and raw_n[:30] in neighbor):
                return "offset", line_num + off

    # Fuzzy token match
    raw_tokens = set(raw_n.split())
    if len(raw_tokens) < 3:
        # Short raw - check character-level
        raw_chars = set(raw_n.replace(' ', ''))
        src_chars = set(src.replace(' ', ''))
        if len(raw_chars) > 0 and len(raw_chars & src_chars) / len(raw_chars) > 0.6:
            return "fuzzy", line_num
        return "mismatch", 0

    for off in range(-window, window + 1):
        idx = line_num - 1 + off
        if 0 <= idx < len(lines):
            line_tokens = set(normalize(lines[idx]).split())
            overlap = len(raw_tokens & line_tokens) / len(raw_tokens) if raw_tokens else 0
            if overlap > 0.6:
                return "fuzzy", line_num + off

    return "mismatch", 0

def check_latex_semantic(raw, latex):
    """Check if LaTeX semantically matches raw. Returns (status, note)."""
    if not latex:
        return "no_latex", ""

    # Strip ALL formatting from both sides
    def skeleton(s, is_latex=False):
        if is_latex:
            # Unwrap formatting commands
            s = re.sub(r'\\(?:mathrm|text|mathcal|mathbb|boldsymbol|hat|bar|tilde|vec|overline)\{([^}]*)\}', r'\1', s)
            s = re.sub(r'\\operatorname\{([^}]*)\}', r'\1', s)
            s = re.sub(r'\\frac\{([^}]*)\}\{([^}]*)\}', r'\1/\2', s)
            s = re.sub(r'\\sqrt(?:\[([^\]]*)\])?\{([^}]*)\}', r'sqrt\2', s)
            s = re.sub(r'\\(?:left|right|!|;|quad|,|:|qquad|\s)', ' ', s)
            s = re.sub(r'\\tag\{[^}]*\}', '', s)
            s = re.sub(r'\\(alpha|beta|gamma|delta|epsilon|zeta|eta|theta|iota|kappa|lambda|mu|nu|xi|pi|rho|sigma|tau|upsilon|phi|chi|psi|omega)', r'\1', s)
            s = re.sub(r'\\(Alpha|Beta|Gamma|Delta|Epsilon|Zeta|Eta|Theta|Iota|Kappa|Lambda|Mu|Nu|Xi|Pi|Rho|Sigma|Tau|Upsilon|Phi|Chi|Psi|Omega)', r'\1', s)
            s = re.sub(r'\\(ln|log|exp|sin|cos|tan|det|dim|min|max|lim|Tr|tr|Re|Im|sup|inf|ker|hom|deg|sgn|sign)', r'\1', s)
            s = re.sub(r'\\(sum|int|prod|oint|bigcup|bigcap)', r'\1', s)
            s = re.sub(r'\\(cdot|times|otimes|oplus)', ' ', s)
            s = re.sub(r'\\(langle|rangle|leq|geq|neq|approx|equiv|sim|subset|supset|in|notin|forall|exists|partial|nabla|infty|hbar|ell|pm|mp)', r'\1', s)
            s = re.sub(r'\\[a-zA-Z]+', ' ', s)  # remaining commands

        s = s.lower()
        s = re.sub(r'[^a-z0-9.+\-*/=<>~]', ' ', s)
        s = re.sub(r'\s+', ' ', s).strip()
        return s

    raw_s = skeleton(raw)
    latex_s = skeleton(latex, is_latex=True)

    raw_words = set(raw_s.split()) - {'', 'a', 'b', 'c', 'd', 'e', 'f', 'i', 'j', 'k', 'n', 's', 't', 'x', 'y', 'z', '0', '1', '2', '3', 'the', 'is', 'at', 'of', 'in', 'for', 'and', 'to', 'with', 'from'}
    latex_words = set(latex_s.split()) - {'', 'a', 'b', 'c', 'd', 'e', 'f', 'i', 'j', 'k', 'n', 's', 't', 'x', 'y', 'z', '0', '1', '2', '3', 'the', 'is', 'at', 'of', 'in', 'for', 'and', 'to', 'with', 'from'}

    if not raw_words:
        return "ok", "trivial raw"

    overlap = len(raw_words & latex_words) / len(raw_words)

    if overlap >= 0.3:
        return "ok", f"overlap={overlap:.0%}"

    # Additional check: LHS match
    raw_lhs = re.match(r'([A-Za-z_][A-Za-z_0-9]*)', raw)
    latex_lhs = re.match(r'([A-Za-z_][A-Za-z_0-9]*)', re.sub(r'\\[a-z]+\{([^}]*)\}', r'\1', latex))
    if raw_lhs and latex_lhs:
        if raw_lhs.group(1).lower()[:3] == latex_lhs.group(1).lower()[:3]:
            return "ok", f"LHS match, overlap={overlap:.0%}"

    if overlap >= 0.15:
        return "borderline", f"overlap={overlap:.0%}"

    return "wrong", f"overlap={overlap:.0%}"

def main():
    with open(os.path.join(ROOT, "tools", "knowledge-index.json"), "r", encoding="utf-8") as f:
        data = json.load(f)
    eqs = data['equations']

    # Group by source file
    by_file = defaultdict(list)
    for eq in eqs:
        by_file[eq['source_file']].append(eq)

    sorted_files = sorted(by_file.items(), key=lambda x: -len(x[1]))

    total = 0
    issues = []
    raw_status_counts = Counter()
    latex_status_counts = Counter()

    for src_file, file_eqs in sorted_files:
        lines = read_file(src_file)

        for eq in file_eqs:
            total += 1
            raw_status, best_line = check_raw_match(eq['raw'], lines, eq.get('line', 0))
            raw_status_counts[raw_status] += 1

            latex_status, latex_note = check_latex_semantic(eq['raw'], eq.get('latex'))
            latex_status_counts[latex_status] += 1

            # Record issues
            if raw_status not in ('ok', 'fuzzy') or latex_status in ('wrong', 'borderline'):
                severity = 'ok'
                if raw_status == 'mismatch':
                    severity = 'severe' if eq.get('type') in ('structural', 'display', 'inline') else 'moderate'
                elif raw_status == 'offset':
                    severity = 'typo'
                elif raw_status in ('file_missing', 'line_oob'):
                    severity = 'moderate'

                if latex_status == 'wrong':
                    severity = 'severe'
                elif latex_status == 'borderline' and severity == 'ok':
                    severity = 'typo'

                if severity != 'ok':
                    issues.append({
                        'id': eq['id'],
                        'type': eq.get('type', 'unknown'),
                        'severity': severity,
                        'source_file': src_file,
                        'line': eq.get('line', 0),
                        'best_line': best_line,
                        'raw_status': raw_status,
                        'latex_status': latex_status,
                        'latex_note': latex_note,
                        'raw': eq['raw'][:150],
                        'latex': (eq.get('latex') or '')[:150],
                        'audit_status': eq.get('audit_status', 'NONE'),
                    })

        if total % 2000 < len(file_eqs):
            print(f"  {total}/{len(eqs)} checked...", file=sys.stderr)

    print(f"\n{'='*60}", file=sys.stderr)
    print(f"SYSTEMATIC AUDIT COMPLETE: {total} equations", file=sys.stderr)
    print(f"\nRaw match status:", file=sys.stderr)
    for s, c in raw_status_counts.most_common():
        print(f"  {s}: {c}", file=sys.stderr)
    print(f"\nLaTeX status:", file=sys.stderr)
    for s, c in latex_status_counts.most_common():
        print(f"  {s}: {c}", file=sys.stderr)
    print(f"\nTotal issues: {len(issues)}", file=sys.stderr)

    sev_counts = Counter(i['severity'] for i in issues)
    print(f"By severity:", file=sys.stderr)
    for s in ['critical', 'severe', 'moderate', 'typo']:
        if s in sev_counts:
            print(f"  {s}: {sev_counts[s]}", file=sys.stderr)

    # Output results
    print(f"\n{'='*60}")
    print(f"TOTAL EQUATIONS: {total}")
    print(f"ISSUES FOUND: {len(issues)}")

    for sev in ['critical', 'severe', 'moderate', 'typo']:
        sev_issues = [i for i in issues if i['severity'] == sev]
        if not sev_issues:
            continue
        print(f"\n=== {sev.upper()} ({len(sev_issues)}) ===")
        for i in sev_issues:
            print(f"\n{i['id']} [{i['type']}] current_audit={i['audit_status']}")
            print(f"  File: {i['source_file']} line {i['line']}" + (f" -> {i['best_line']}" if i['best_line'] != i['line'] and i['best_line'] != 0 else ""))
            print(f"  Raw status: {i['raw_status']}")
            print(f"  LaTeX status: {i['latex_status']} {i['latex_note']}")
            print(f"  Raw: {i['raw']}")
            if i['latex']:
                print(f"  LaTeX: {i['latex']}")

    # Save JSON
    result = {
        'total': total,
        'raw_status_counts': dict(raw_status_counts),
        'latex_status_counts': dict(latex_status_counts),
        'issue_count': len(issues),
        'severity_counts': dict(sev_counts),
        'issues': issues,
    }

    out_path = os.path.join(ROOT, "tools", "equation-audit-full-results.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
    print(f"\nResults saved to {out_path}", file=sys.stderr)

if __name__ == "__main__":
    main()
