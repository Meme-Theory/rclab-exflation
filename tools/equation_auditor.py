#!/usr/bin/env python3
"""
Equation Auditor for knowledge-index.json
Validates all equations against their source files.
"""
import json
import os
import re
import sys
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_index():
    path = os.path.join(ROOT, "tools", "knowledge-index.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def load_source_file(src_file):
    """Load source file, return list of lines."""
    path = os.path.join(ROOT, src_file.replace("\\", "/"))
    if not os.path.exists(path):
        return None
    for enc in ("utf-8", "utf-8-sig", "latin-1", "cp1252"):
        try:
            with open(path, "r", encoding=enc, errors="replace") as f:
                return f.readlines()
        except (UnicodeDecodeError, UnicodeError):
            continue
    # Last resort
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        return f.readlines()

# Cache loaded files
_file_cache = {}
def get_source_lines(src_file):
    if src_file not in _file_cache:
        _file_cache[src_file] = load_source_file(src_file)
    return _file_cache[src_file]

def normalize(s):
    """Normalize string for comparison: strip whitespace, collapse spaces."""
    return re.sub(r'\s+', ' ', s.strip())

def validate_raw_against_source(eq):
    """Check if raw expression matches the source file at the indicated line."""
    src_file = eq.get("source_file", "")
    line_num = eq.get("line", 0)
    raw = eq.get("raw", "")

    if not src_file or not line_num or not raw:
        return "SKIP", "Missing source_file, line, or raw"

    lines = get_source_lines(src_file)
    if lines is None:
        return "FILE_NOT_FOUND", f"File not found: {src_file}"

    if line_num > len(lines):
        return "LINE_BEYOND_EOF", f"Line {line_num} beyond file length {len(lines)}"

    source_line = lines[line_num - 1].strip()
    raw_norm = normalize(raw)
    source_norm = normalize(source_line)

    # Exact containment check
    if raw_norm in source_norm or source_norm in raw_norm:
        return "MATCH", "Exact match"

    # Partial match (first 40 chars)
    raw_prefix = raw_norm[:40]
    src_prefix = source_norm[:40]
    if raw_prefix in source_norm or src_prefix in raw_norm:
        return "PARTIAL_MATCH", "Partial match (prefix)"

    # Check surrounding lines (+-3)
    for offset in [-3, -2, -1, 1, 2, 3]:
        idx = line_num - 1 + offset
        if 0 <= idx < len(lines):
            neighbor = normalize(lines[idx])
            if raw_norm in neighbor or neighbor in raw_norm or raw_prefix in neighbor:
                return "LINE_OFFSET", f"Found at line {line_num + offset} (offset {offset:+d})"

    # Fuzzy: check if key tokens appear nearby
    raw_tokens = set(raw_norm.split())
    nearby_text = ""
    for offset in range(-3, 4):
        idx = line_num - 1 + offset
        if 0 <= idx < len(lines):
            nearby_text += " " + lines[idx]
    nearby_norm = normalize(nearby_text)
    nearby_tokens = set(nearby_norm.split())

    if len(raw_tokens) > 3:
        overlap = len(raw_tokens & nearby_tokens) / len(raw_tokens)
        if overlap > 0.7:
            return "FUZZY_MATCH", f"Token overlap {overlap:.0%} within +-3 lines"

    return "MISMATCH", f"No match at line {line_num}"

def validate_latex(eq):
    """Validate LaTeX against raw expression."""
    raw = eq.get("raw", "")
    latex = eq.get("latex", "")

    if not latex:
        return "NO_LATEX", "No LaTeX present"

    issues = []

    # Basic sanity checks
    # 1. Balanced braces
    brace_depth = 0
    for c in latex:
        if c == '{':
            brace_depth += 1
        elif c == '}':
            brace_depth -= 1
        if brace_depth < 0:
            issues.append("Unbalanced braces (extra })")
            break
    if brace_depth > 0:
        issues.append(f"Unbalanced braces ({brace_depth} unclosed)")

    # 2. Balanced \left \right
    lefts = len(re.findall(r'\\left[(\[{|\\]', latex))
    rights = len(re.findall(r'\\right[)\]}|\\]', latex))
    if lefts != rights:
        issues.append(f"Unbalanced \\left/\\right: {lefts} left vs {rights} right")

    # 3. Check key symbols from raw appear in LaTeX
    # Extract numbers from raw
    raw_numbers = set(re.findall(r'\d+\.?\d*', raw))
    latex_numbers = set(re.findall(r'\d+\.?\d*', latex))
    missing_numbers = raw_numbers - latex_numbers
    if missing_numbers and len(raw_numbers) > 0:
        # Only flag if significant numbers missing
        significant = [n for n in missing_numbers if float(n) > 1 or '.' in n]
        if significant:
            issues.append(f"Numbers in raw but not LaTeX: {significant[:5]}")

    if issues:
        return "LATEX_ISSUES", "; ".join(issues)
    return "LATEX_OK", "LaTeX passes basic checks"

def classify_severity(match_status, latex_status, eq):
    """Classify the severity of any issues found."""
    eq_type = eq.get("type", "code")

    if match_status in ("MATCH", "PARTIAL_MATCH") and latex_status in ("LATEX_OK", "NO_LATEX"):
        return "OK"

    if match_status == "FUZZY_MATCH":
        return "TYPO"  # Likely minor formatting difference

    if match_status == "LINE_OFFSET":
        return "TYPO"  # Line number drift, content is there

    if latex_status == "LATEX_ISSUES":
        return "MODERATE"  # LaTeX rendering issues

    if match_status == "MISMATCH":
        if eq_type in ("structural", "display"):
            return "SEVERE"  # Physics equation doesn't match source
        elif eq_type == "inline":
            return "MODERATE"
        else:
            return "TYPO"  # Code/comment mismatch is less critical

    if match_status in ("FILE_NOT_FOUND", "LINE_BEYOND_EOF"):
        return "MODERATE"  # Can't verify

    return "OK"

def audit_all(limit=None):
    """Run the full audit."""
    data = load_index()
    eqs = data.get("equations", [])

    if limit:
        eqs = eqs[:limit]

    results = {
        "total": len(eqs),
        "findings": [],
        "summary": Counter(),
        "severity": Counter(),
        "by_type": defaultdict(Counter),
    }

    for i, eq in enumerate(eqs):
        if i % 1000 == 0:
            print(f"  Auditing equation {i}/{len(eqs)}...", file=sys.stderr)

        match_status, match_detail = validate_raw_against_source(eq)
        latex_status, latex_detail = validate_latex(eq)
        severity = classify_severity(match_status, latex_status, eq)

        results["summary"][match_status] += 1
        results["severity"][severity] += 1
        results["by_type"][eq.get("type", "unknown")][severity] += 1

        if severity != "OK":
            results["findings"].append({
                "id": eq["id"],
                "type": eq.get("type", "unknown"),
                "severity": severity,
                "raw": eq.get("raw", "")[:200],
                "latex": eq.get("latex", "")[:200] if eq.get("latex") else None,
                "source_file": eq.get("source_file", ""),
                "line": eq.get("line", 0),
                "match_status": match_status,
                "match_detail": match_detail,
                "latex_status": latex_status,
                "latex_detail": latex_detail,
            })

    return results

def format_report(results):
    """Format audit results as markdown."""
    lines = []
    lines.append("# Equation Audit Report\n")
    lines.append(f"**Total equations audited**: {results['total']}\n")

    lines.append("## Summary by Match Status\n")
    lines.append("| Status | Count |")
    lines.append("|--------|-------|")
    for status, count in results["summary"].most_common():
        lines.append(f"| {status} | {count} |")

    lines.append("\n## Summary by Severity\n")
    lines.append("| Severity | Count |")
    lines.append("|----------|-------|")
    for sev, count in sorted(results["severity"].items(), key=lambda x: ["OK", "TYPO", "MODERATE", "SEVERE", "CRITICAL"].index(x[0]) if x[0] in ["OK", "TYPO", "MODERATE", "SEVERE", "CRITICAL"] else 99):
        lines.append(f"| {sev} | {count} |")

    lines.append("\n## Severity by Equation Type\n")
    lines.append("| Type | OK | TYPO | MODERATE | SEVERE |")
    lines.append("|------|-----|------|----------|--------|")
    for etype in ["structural", "display", "inline", "code", "comment"]:
        if etype in results["by_type"]:
            counts = results["by_type"][etype]
            lines.append(f"| {etype} | {counts.get('OK',0)} | {counts.get('TYPO',0)} | {counts.get('MODERATE',0)} | {counts.get('SEVERE',0)} |")

    # Group findings by severity
    for sev in ["CRITICAL", "SEVERE", "MODERATE", "TYPO"]:
        findings = [f for f in results["findings"] if f["severity"] == sev]
        if not findings:
            continue
        lines.append(f"\n## {sev} Findings ({len(findings)})\n")
        for f in findings:
            lines.append(f"### {f['id']} [{f['type']}] — {f['severity']}")
            lines.append(f"- **Source**: `{f['source_file']}` line {f['line']}")
            lines.append(f"- **Raw**: `{f['raw']}`")
            if f.get("latex"):
                lines.append(f"- **LaTeX**: `{f['latex']}`")
            lines.append(f"- **Match**: {f['match_status']} — {f['match_detail']}")
            if f["latex_status"] != "NO_LATEX":
                lines.append(f"- **LaTeX check**: {f['latex_status']} — {f['latex_detail']}")
            lines.append("")

    return "\n".join(lines)

if __name__ == "__main__":
    print("Starting equation audit...", file=sys.stderr)
    results = audit_all()
    report = format_report(results)

    output_path = os.path.join(ROOT, "tools", "equation-audit-full-findings.md")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"\nReport written to {output_path}", file=sys.stderr)

    # Also dump raw results as JSON for weaver
    json_path = os.path.join(ROOT, "tools", "equation-audit-full-results.json")
    # Convert defaultdict and Counter for JSON
    json_results = {
        "total": results["total"],
        "summary": dict(results["summary"]),
        "severity": dict(results["severity"]),
        "by_type": {k: dict(v) for k, v in results["by_type"].items()},
        "findings": results["findings"],
    }
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(json_results, f, indent=2)
    print(f"JSON results written to {json_path}", file=sys.stderr)

    # Print summary to stdout
    print(f"\n=== AUDIT COMPLETE ===")
    print(f"Total: {results['total']}")
    print(f"OK: {results['severity'].get('OK', 0)}")
    print(f"TYPO: {results['severity'].get('TYPO', 0)}")
    print(f"MODERATE: {results['severity'].get('MODERATE', 0)}")
    print(f"SEVERE: {results['severity'].get('SEVERE', 0)}")
    print(f"CRITICAL: {results['severity'].get('CRITICAL', 0)}")
    print(f"Findings written to: tools/equation-audit-full-findings.md")
