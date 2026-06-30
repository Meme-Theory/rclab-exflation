#!/usr/bin/env python3
# COMPUTATIONS-EXEMPTION: This is an infrastructure/audit tool, not a physics computation.
# It references no framework constants; the python-validate WARN about a
# missing `from canonical_constants import ...` is expected per
# .claude/rules/math-scripts.md ("tag as local"-equivalent whole-file exemption).
"""Agent-Memory Registry Inversion (AMRI) audit tool.

Detects project-level registry content misfiled inside agent-memory directories
and flags it for migration to sessions/framework/ + knowledge.db.

Per .claude/rules/agent-standards.md § AMRI, a memory-file section is AMRI if:
  1. Input-pin test: another gate references the memory file as an Input-SHA pin
  2. Output-target test: a gate writes the memory file as its primary output
  3. Cross-agent overlap: two or more agent memories share registry-style entries

This tool emits screening FLAGS, not verdicts — final classification is a
human (or /shortterm spawned agent) judgment call. The tool narrows the search.

Per .claude/rules/math-scripts.md, exit code reflects SCRIPT health, not
audit findings. Exit 0 on successful scan regardless of how many AMRI
candidates are found; exit != 0 only on I/O / parsing failure.

Usage:
    python computations/_shared/_agent_memory_inversion_audit.py
    python computations/_shared/_agent_memory_inversion_audit.py --agent little-red-dots-jwst-analyst
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

REGISTRY_HEADING_REGEX = re.compile(
    r'(?i)\b(watchlist|roster|registry|catalog(?!ue)|atlas|detector|'
    r'channel[s\-]|observable[s]?|forecast|prediction[-\s]table|'
    r'correlation[-\s]matrix|discount[-\s]table|sigma[-\s]prediction|'
    r'pin(ned)?[-\s]value|falsifier[s]?|null[-\s]elim)\b'
)
TABLE_ROW_REGEX = re.compile(r'^\s*\|.*\|.*\|.*$')
TABLE_SUBSTANTIVE_THRESHOLD = 4  # (local) rows in a markdown table to count as substantive
MULTI_FLAG_AMRI_THRESHOLD = 2    # (local) number of flags to escalate MAYBE -> LIKELY


def scan_memory_files(base_dir: Path):
    """Yield (agent, relative_path, content) for every .md under agent-memory/."""
    if not base_dir.is_dir():
        raise FileNotFoundError(f'agent-memory directory not found: {base_dir}')
    for agent_dir in sorted(base_dir.iterdir()):
        if not agent_dir.is_dir():
            continue
        for md in sorted(agent_dir.rglob('*.md')):
            try:
                content = md.read_text(encoding='utf-8', errors='ignore')
            except OSError as e:
                print(f'[WARN] could not read {md}: {e}', file=sys.stderr)
                continue
            rel = md.relative_to(base_dir.parent.parent) if base_dir.parent.parent in md.parents else md
            yield agent_dir.name, Path(*md.relative_to(base_dir.parent).parts), content


def detect_registry_headings(content: str):
    """Return list of (line_no, heading_text) for headings matching registry keywords."""
    hits = []
    for line_no, line in enumerate(content.splitlines(), 1):
        if line.lstrip().startswith('#') and REGISTRY_HEADING_REGEX.search(line):
            hits.append((line_no, line.strip()))
    return hits


def count_substantive_tables(content: str) -> int:
    """Count markdown table rows (rough proxy for tabular / registry-like content)."""
    return sum(1 for line in content.splitlines() if TABLE_ROW_REGEX.match(line))


def find_session_references(memory_rel_path: Path, session_dir: Path):
    """Search sessions/**/*.md for any reference to this memory file path.

    Returns list of (plan_file, line_no, context, kind) where kind is one of:
      INPUT_PIN   — line mentions 'input' or 'pin' or 'sha' alongside the path
      OUTPUT      — line mentions 'output' or 'write' alongside the path
      REFERENCE   — plain textual reference without input/output verb
    """
    results = []
    forward = str(memory_rel_path).replace('\\', '/')
    backward = str(memory_rel_path).replace('/', '\\')
    needles = {forward, backward}
    # also match the bare .claude/agent-memory/<agent>/ prefix form
    for md in session_dir.rglob('*.md'):
        try:
            lines = md.read_text(encoding='utf-8', errors='ignore').splitlines()
        except OSError:
            continue
        for line_no, line in enumerate(lines, 1):
            if not any(n in line for n in needles):
                continue
            low = line.lower()
            if any(kw in low for kw in ('input_pin_map', 'input-sha', 'input_sha', 'sha-pin')):
                kind = 'INPUT_PIN'
            elif any(kw in low for kw in ('input', 'pin', 'reads', 'read:')):
                kind = 'INPUT_PIN'
            elif any(kw in low for kw in ('output', 'writes', 'write:', 'sole writer')):
                kind = 'OUTPUT'
            else:
                kind = 'REFERENCE'
            try:
                rel = md.relative_to(session_dir.parent)
            except ValueError:
                rel = md
            results.append((str(rel).replace('\\', '/'), line_no, line.strip()[:200], kind))
    return results


def classify_file(agent: str, file_rel: Path, content: str, session_dir: Path):
    headings = detect_registry_headings(content)
    table_rows = count_substantive_tables(content)
    session_refs = find_session_references(file_rel, session_dir)

    flags = []
    if headings:
        flags.append('REGISTRY_HEADING')
    if table_rows >= TABLE_SUBSTANTIVE_THRESHOLD:
        flags.append('TABULAR_CONTENT')
    if any(kind == 'INPUT_PIN' for _, _, _, kind in session_refs):
        flags.append('INPUT_PIN_TEST')          # AMRI test 1
    if any(kind == 'OUTPUT' for _, _, _, kind in session_refs):
        flags.append('OUTPUT_TARGET_TEST')      # AMRI test 2

    if 'INPUT_PIN_TEST' in flags or 'OUTPUT_TARGET_TEST' in flags:
        verdict = 'AMRI-LIKELY'                 # a formal AMRI test fired
    elif len(flags) >= MULTI_FLAG_AMRI_THRESHOLD:
        verdict = 'AMRI-LIKELY'                 # multiple screening flags
    elif len(flags) == 1:
        verdict = 'AMRI-MAYBE'
    else:
        verdict = 'agent-private'

    return {
        'agent': agent,
        'file': str(file_rel).replace('\\', '/'),
        'verdict': verdict,
        'flags': flags,
        'registry_headings': headings,
        'table_row_count': table_rows,
        'session_references': session_refs,
    }


def detect_cross_agent_overlap(results):
    """AMRI test 3: two or more agents' memories sharing registry-style headings."""
    by_heading = defaultdict(list)
    for r in results:
        if r['verdict'] == 'agent-private':
            continue
        for _, h in r['registry_headings']:
            key = h.lower().lstrip('#').strip()
            by_heading[key].append((r['agent'], r['file']))
    overlaps = {}
    for h, occurrences in by_heading.items():
        agents = {a for a, _ in occurrences}
        if len(agents) >= 2:
            overlaps[h] = occurrences
    return overlaps


def emit_markdown(results, overlaps, out_path: Path):
    n_likely = sum(1 for r in results if r['verdict'] == 'AMRI-LIKELY')
    n_maybe = sum(1 for r in results if r['verdict'] == 'AMRI-MAYBE')
    n_private = sum(1 for r in results if r['verdict'] == 'agent-private')

    lines = [
        '# AMRI audit report',
        '',
        '**Source rule**: `.claude/rules/agent-standards.md` § AMRI',
        '**Migration tool**: `/shortterm <agent>` with AMRI-PROMOTE classification',
        '**Framework template**: `sessions/framework/registry/_registry-template.md`',
        '',
        f'**Total files scanned**: {len(results)}',
        f'- AMRI-LIKELY: {n_likely}',
        f'- AMRI-MAYBE:  {n_maybe}',
        f'- agent-private: {n_private}',
        '',
        f'**Cross-agent overlapping headings**: {len(overlaps)}',
        '',
        '---',
        '',
        '## Flagged files',
        '',
    ]
    for r in sorted(results, key=lambda x: (x['verdict'], x['file'])):
        if r['verdict'] == 'agent-private':
            continue
        lines.append(f'### `{r["file"]}` — {r["verdict"]}')
        lines.append(f'- **Agent**: `{r["agent"]}`')
        lines.append(f'- **Flags**: {", ".join(r["flags"]) or "(none)"}')
        lines.append(f'- **Table rows**: {r["table_row_count"]}')
        if r['registry_headings']:
            lines.append(f'- **Registry-like headings ({len(r["registry_headings"])})**:')
            for ln, h in r['registry_headings'][:10]:
                lines.append(f'  - L{ln}: `{h}`')
            if len(r['registry_headings']) > 10:
                lines.append(f'  - ...({len(r["registry_headings"]) - 10} more)')
        if r['session_references']:
            lines.append(f'- **Session references ({len(r["session_references"])})**:')
            for plan, ln, ctx, kind in r['session_references'][:8]:
                lines.append(f'  - [{kind}] `{plan}:{ln}` — {ctx}')
            if len(r['session_references']) > 8:
                lines.append(f'  - ...({len(r["session_references"]) - 8} more)')
        lines.append('')

    if overlaps:
        lines.extend(['---', '', '## Cross-agent heading overlaps (AMRI test 3)', ''])
        for h, occurrences in sorted(overlaps.items()):
            lines.append(f'- `{h}`:')
            for agent, f in occurrences:
                lines.append(f'  - `{agent}` — `{f}`')
            lines.append('')

    out_path.write_text('\n'.join(lines) + '\n', encoding='utf-8')


def main():
    ap = argparse.ArgumentParser(description='AMRI audit tool (screening)')
    ap.add_argument('--agent-memory-dir', default='.claude/agent-memory')
    ap.add_argument('--session-dir', default='sessions')
    ap.add_argument('--output-json', default='computations/_shared/amri_audit_report.json')
    ap.add_argument('--output-md', default='computations/_shared/amri_audit_report.md')
    ap.add_argument('--agent', default=None, help='Restrict scan to this agent subdirectory')
    args = ap.parse_args()

    base = Path(args.agent_memory_dir)
    session_dir = Path(args.session_dir)

    try:
        results = []
        for agent, file_rel, content in scan_memory_files(base):
            if args.agent and agent != args.agent:
                continue
            results.append(classify_file(agent, file_rel, content, session_dir))
    except FileNotFoundError as e:
        print(f'[ERR] {e}', file=sys.stderr)
        sys.exit(1)

    overlaps = detect_cross_agent_overlap(results)

    out_json = Path(args.output_json)
    out_md = Path(args.output_md)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_md.parent.mkdir(parents=True, exist_ok=True)

    out_json.write_text(
        json.dumps({'results': results, 'overlaps': overlaps}, indent=2, ensure_ascii=False),
        encoding='utf-8',
    )
    emit_markdown(results, overlaps, out_md)

    n_likely = sum(1 for r in results if r['verdict'] == 'AMRI-LIKELY')
    n_maybe = sum(1 for r in results if r['verdict'] == 'AMRI-MAYBE')
    n_private = sum(1 for r in results if r['verdict'] == 'agent-private')
    print(f'AMRI audit: {len(results)} files scanned')
    print(f'  AMRI-LIKELY  : {n_likely}')
    print(f'  AMRI-MAYBE   : {n_maybe}')
    print(f'  agent-private: {n_private}')
    print(f'  overlaps     : {len(overlaps)}')
    print(f'  JSON -> {out_json}')
    print(f'  MD   -> {out_md}')

    sys.exit(0)


if __name__ == '__main__':
    main()
