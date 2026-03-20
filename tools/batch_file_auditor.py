#!/usr/bin/env python3
"""
Batch file-by-file equation auditor.
Reads each source file once, validates all equations from that file.
Outputs chunk-by-chunk results for the weaver.
"""
import json
import os
import re
import sys
from collections import defaultdict

ROOT = "C:/sandbox/Ainulindale Exflation"

def load_index():
    with open(os.path.join(ROOT, "tools", "knowledge-index.json"), "r", encoding="utf-8") as f:
        return json.load(f)

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

def check_raw_vs_source(raw, lines, line_num):
    """Check if raw matches source at given line. Return (status, detail, best_line)."""
    if not lines:
        return "file_missing", "Source file not found", line_num
    if line_num < 1 or line_num > len(lines):
        return "line_oob", f"Line {line_num} out of range (file has {len(lines)} lines)", line_num

    raw_norm = normalize(raw)
    source_line = normalize(lines[line_num - 1])

    # Exact match
    if raw_norm in source_line or source_line in raw_norm:
        return "match", "exact", line_num

    # Prefix match (first 30 chars)
    if len(raw_norm) > 10 and raw_norm[:30] in source_line:
        return "match", "prefix", line_num
    if len(source_line) > 10 and source_line[:30] in raw_norm:
        return "match", "prefix_rev", line_num

    # Check nearby lines
    for offset in range(-5, 6):
        if offset == 0:
            continue
        idx = line_num - 1 + offset
        if 0 <= idx < len(lines):
            neighbor = normalize(lines[idx])
            if raw_norm in neighbor or neighbor in raw_norm:
                return "offset", f"Found at line {line_num + offset} (offset {offset:+d})", line_num + offset
            if len(raw_norm) > 10 and raw_norm[:30] in neighbor:
                return "offset", f"Prefix at line {line_num + offset} (offset {offset:+d})", line_num + offset

    # Fuzzy: token overlap
    raw_tokens = set(raw_norm.split())
    best_overlap = 0
    best_line = line_num
    for offset in range(-5, 6):
        idx = line_num - 1 + offset
        if 0 <= idx < len(lines):
            line_tokens = set(normalize(lines[idx]).split())
            if raw_tokens:
                overlap = len(raw_tokens & line_tokens) / len(raw_tokens)
                if overlap > best_overlap:
                    best_overlap = overlap
                    best_line = idx + 1

    if best_overlap > 0.6:
        return "fuzzy", f"Best overlap {best_overlap:.0%} at line {best_line}", best_line

    return "mismatch", f"No match found near line {line_num}", line_num

def check_latex_vs_raw(raw, latex):
    """Check if LaTeX correctly renders the raw expression."""
    if not latex:
        return "missing", "No LaTeX"

    issues = []

    # 1. Structural checks
    brace_depth = 0
    for c in latex:
        if c == '{': brace_depth += 1
        elif c == '}': brace_depth -= 1
        if brace_depth < 0:
            issues.append("unbalanced_braces")
            break
    if brace_depth > 0:
        issues.append(f"unclosed_braces({brace_depth})")

    # 2. Semantic correspondence: strip LaTeX formatting and compare
    def math_skeleton(s, is_latex=False):
        if is_latex:
            s = re.sub(r'\\(?:mathrm|text|mathcal|mathbb|boldsymbol|hat|bar|tilde|vec)\{([^}]*)\}', r'\1', s)
            s = re.sub(r'\\operatorname\{([^}]*)\}', r'\1', s)
            s = re.sub(r'\\frac\{([^}]*)\}\{([^}]*)\}', r'\1/\2', s)
            s = re.sub(r'\\sqrt\{([^}]*)\}', r'sqrt(\1)', s)
            s = re.sub(r'\\(?:left|right|!|;|quad|,|:|\s)', '', s)
            s = re.sub(r'\\(ln|log|exp|sin|cos|det|dim|min|max|lim|Tr|tr|Re|Im|sup|inf)', r'\1', s)
            s = re.sub(r'\\(sum|int|prod)', r'\1', s)
            s = re.sub(r'\\(?:cdot|times)', '*', s)
            s = re.sub(r'\\oplus', '+', s)
            s = re.sub(r'\\otimes', 'x', s)
            s = re.sub(r'\\langle', '<', s)
            s = re.sub(r'\\rangle', '>', s)
            s = re.sub(r'\\tag\{[^}]*\}', '', s)
            s = re.sub(r'\\([a-zA-Z]+)', r'\1', s)
        s = s.lower()
        s = re.sub(r'[{}()\[\]|\\,;:!@#$&_\'"` ]', ' ', s)
        s = re.sub(r'\s+', ' ', s).strip()
        return s

    raw_skel = math_skeleton(raw)
    latex_skel = math_skeleton(latex, is_latex=True)

    raw_words = set(raw_skel.split())
    latex_words = set(latex_skel.split())
    trivial = {'', 'a', 'b', 'c', 'd', 'e', 'f', 'i', 'j', 'k', 'n', 's', 't', 'x', 'y', 'z',
               'the', 'is', 'at', 'of', 'in', 'for', 'and', 'to', 'with', 'from', 'by',
               'if', 'or', 'no', 'on', 'an', 'up', 'be', 'do', 'so', 'as', 'we', '0', '1', '2'}
    raw_words -= trivial
    latex_words -= trivial

    if not raw_words:
        return "ok" if not issues else "structural_issue", "; ".join(issues) if issues else "ok"

    overlap = len(raw_words & latex_words) / len(raw_words)

    if overlap < 0.15 and len(raw_words) >= 3:
        return "wrong_equation", f"LaTeX is a different equation (overlap={overlap:.0%})"

    if issues:
        return "structural_issue", "; ".join(issues)

    return "ok", f"overlap={overlap:.0%}"

def classify_severity(raw_status, latex_status, eq_type):
    """Classify overall severity."""
    if raw_status == "mismatch":
        if eq_type in ("structural", "display", "inline"):
            return "severe"
        return "moderate"
    if raw_status == "file_missing":
        return "moderate"
    if latex_status == "wrong_equation":
        return "severe"
    if latex_status == "structural_issue":
        return "moderate"
    if raw_status == "offset":
        return "typo"
    return "ok"

def audit_file_group(eqs, src_file, lines):
    """Audit all equations from a single source file."""
    results = []
    for eq in eqs:
        raw_status, raw_detail, best_line = check_raw_vs_source(eq['raw'], lines, eq.get('line', 0))
        latex_status, latex_detail = check_latex_vs_raw(eq['raw'], eq.get('latex', ''))
        severity = classify_severity(raw_status, latex_status, eq.get('type', 'code'))

        results.append({
            'id': eq['id'],
            'type': eq.get('type', 'unknown'),
            'raw_status': raw_status,
            'raw_detail': raw_detail,
            'latex_status': latex_status,
            'latex_detail': latex_detail,
            'severity': severity,
            'line': eq.get('line', 0),
            'best_line': best_line,
            'has_latex': bool(eq.get('latex')),
            'raw_preview': eq['raw'][:120],
            'latex_preview': (eq.get('latex') or '')[:120],
        })
    return results

def main():
    data = load_index()
    eqs = data['equations']

    # Group by source file
    by_file = defaultdict(list)
    for eq in eqs:
        by_file[eq['source_file']].append(eq)

    # Sort files by count descending
    sorted_files = sorted(by_file.items(), key=lambda x: -len(x[1]))

    all_results = []
    total_checked = 0

    # Severity counters
    severity_counts = defaultdict(int)

    for src_file, file_eqs in sorted_files:
        lines = read_file(src_file)
        results = audit_file_group(file_eqs, src_file, lines)
        all_results.extend(results)
        total_checked += len(results)

        for r in results:
            severity_counts[r['severity']] += 1

        if total_checked % 1000 < len(file_eqs):
            print(f"  Checked {total_checked}/{len(eqs)} equations...", file=sys.stderr)

    print(f"\n=== AUDIT COMPLETE ===", file=sys.stderr)
    print(f"Total: {total_checked}", file=sys.stderr)
    for sev in ['ok', 'typo', 'moderate', 'severe', 'critical']:
        print(f"  {sev}: {severity_counts.get(sev, 0)}", file=sys.stderr)

    # Save full results
    output = {
        'total': total_checked,
        'severity_counts': dict(severity_counts),
        'findings': [r for r in all_results if r['severity'] != 'ok'],
        'all_results': all_results,
    }

    out_path = os.path.join(ROOT, "tools", "equation-audit-full-results.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults written to {out_path}", file=sys.stderr)

    # Print findings summary
    print(f"\nTotal: {total_checked}")
    print(f"OK: {severity_counts.get('ok', 0)}")
    print(f"TYPO: {severity_counts.get('typo', 0)}")
    print(f"MODERATE: {severity_counts.get('moderate', 0)}")
    print(f"SEVERE: {severity_counts.get('severe', 0)}")
    print(f"CRITICAL: {severity_counts.get('critical', 0)}")

    # Print all non-ok findings
    findings = [r for r in all_results if r['severity'] != 'ok']
    print(f"\n=== NON-OK FINDINGS ({len(findings)}) ===")
    for r in sorted(findings, key=lambda x: ['critical', 'severe', 'moderate', 'typo'].index(x['severity']) if x['severity'] in ['critical', 'severe', 'moderate', 'typo'] else 99):
        print(f"\n{r['id']} [{r['type']}] — {r['severity'].upper()}")
        print(f"  raw_status: {r['raw_status']} — {r['raw_detail']}")
        print(f"  latex_status: {r['latex_status']} — {r['latex_detail']}")
        if r['has_latex']:
            print(f"  raw:   {r['raw_preview']}")
            print(f"  latex: {r['latex_preview']}")

if __name__ == "__main__":
    main()
