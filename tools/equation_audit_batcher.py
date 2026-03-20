#!/usr/bin/env python3
"""
Equation Audit Batcher
======================
Extracts equations from knowledge-index.json in reviewable batches.
Groups by source file, outputs batch JSON + human-readable markdown.

Usage:
    python equation_audit_batcher.py --mode stats
    python equation_audit_batcher.py --mode extract --source-type sessions --batch-size 50
    python equation_audit_batcher.py --mode extract --source-type tier0 --batch-size 50
    python equation_audit_batcher.py --mode extract --source-file "sessions/session-06/session-6-cg-algebra.md"
    python equation_audit_batcher.py --mode apply --results-file tools/audit-results/batch_001_results.json
"""
import json
import os
import sys
import argparse
from pathlib import Path
from collections import Counter, defaultdict

sys.stdout.reconfigure(encoding='utf-8')

PROJECT_ROOT = Path(__file__).parent.parent
INDEX_PATH = PROJECT_ROOT / "tools" / "knowledge-index.json"
BATCH_DIR = PROJECT_ROOT / "tools" / "audit-batches"
RESULTS_DIR = PROJECT_ROOT / "tools" / "audit-results"


def load_index():
    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_index(idx):
    tmp = str(INDEX_PATH) + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump(idx, f, indent=2, ensure_ascii=False)
    os.replace(tmp, str(INDEX_PATH))


def stats_mode(idx):
    """Print comprehensive statistics about equations in the index."""
    eqs = idx.get('equations', [])
    print(f"Total equations: {len(eqs)}")
    print()

    # Audit status
    statuses = Counter(eq.get('audit_status', 'none') for eq in eqs)
    print("Audit status:")
    for k, v in statuses.most_common():
        print(f"  {k}: {v}")
    print()

    # LaTeX coverage
    has_latex = sum(1 for eq in eqs if eq.get('latex'))
    print(f"With LaTeX: {has_latex}")
    print(f"Without LaTeX: {len(eqs) - has_latex}")
    print()

    # Source type breakdown
    mm_count = 0
    t0_count = 0
    other_count = 0
    for eq in eqs:
        sf = eq.get('source_file', '')
        if sf.startswith('sessions'):
            mm_count += 1
        elif sf.startswith('tier0-computation') or sf.startswith('tier0-archive'):
            t0_count += 1
        else:
            other_count += 1
    print(f"Sessions equations: {mm_count}")
    print(f"Tier0-computation equations: {t0_count}")
    print(f"Other/unknown: {other_count}")
    print()

    # Source files by count (top 30)
    sources = Counter(eq.get('source_file', 'unknown') for eq in eqs)
    print(f"Unique source files: {len(sources)}")
    print("Top 30 source files:")
    for k, v in sources.most_common(30):
        has_l = sum(1 for eq in eqs if eq.get('source_file') == k and eq.get('latex'))
        audited = sum(1 for eq in eqs if eq.get('source_file') == k and eq.get('audit_status', 'none') != 'none')
        print(f"  {v:5d} ({has_l:3d} LaTeX, {audited:3d} audited)  {k}")

    # Unaudited files needing work
    print()
    unaudited_files = defaultdict(int)
    for eq in eqs:
        if eq.get('audit_status', 'none') == 'none':
            unaudited_files[eq.get('source_file', 'unknown')] += 1
    print(f"Files with unaudited equations: {len(unaudited_files)}")
    print("Top 20 unaudited:")
    for k, v in sorted(unaudited_files.items(), key=lambda x: -x[1])[:20]:
        print(f"  {v:5d}  {k}")


def extract_mode(idx, source_type=None, source_file=None, batch_size=50):
    """Extract equations into batch files for review."""
    eqs = idx.get('equations', [])
    BATCH_DIR.mkdir(exist_ok=True)

    # Filter by source type
    if source_file:
        filtered = [eq for eq in eqs if eq.get('source_file', '') == source_file]
        label = source_file.replace('/', '_').replace('\\', '_').replace('.', '_')
    elif source_type == 'sessions':
        filtered = [eq for eq in eqs if eq.get('source_file', '').startswith('sessions')]
        label = 'sessions'
    elif source_type == 'tier0':
        filtered = [eq for eq in eqs if eq.get('source_file', '').startswith(('tier0-computation', 'tier0-archive'))]
        label = 'tier0'
    else:
        filtered = eqs
        label = 'all'

    # Only unaudited
    unaudited = [eq for eq in filtered if eq.get('audit_status', 'none') == 'none']
    print(f"Filtered: {len(filtered)} total, {len(unaudited)} unaudited")

    if not unaudited:
        print("Nothing to extract.")
        return

    # Group by source file for coherent batches
    by_file = defaultdict(list)
    for eq in unaudited:
        by_file[eq.get('source_file', 'unknown')].append(eq)

    # Create batches respecting file boundaries
    batches = []
    current_batch = []
    for sf in sorted(by_file.keys()):
        file_eqs = by_file[sf]
        if len(current_batch) + len(file_eqs) > batch_size and current_batch:
            batches.append(current_batch)
            current_batch = []
        if len(file_eqs) > batch_size:
            # Large file: split into sub-batches
            for i in range(0, len(file_eqs), batch_size):
                batches.append(file_eqs[i:i+batch_size])
        else:
            current_batch.extend(file_eqs)
    if current_batch:
        batches.append(current_batch)

    print(f"Created {len(batches)} batches (target size: {batch_size})")

    # Write batch files
    for i, batch in enumerate(batches):
        batch_id = f"{label}_batch_{i+1:04d}"
        batch_data = {
            "batch_id": batch_id,
            "source_type": source_type or "all",
            "equation_count": len(batch),
            "source_files": sorted(set(eq.get('source_file', '') for eq in batch)),
            "equations": []
        }
        for eq in batch:
            batch_data["equations"].append({
                "id": eq.get("id"),
                "raw": eq.get("raw", ""),
                "type": eq.get("type", ""),
                "context": eq.get("context", ""),
                "session": eq.get("session", ""),
                "source_file": eq.get("source_file", ""),
                "line": eq.get("line", 0),
                "existing_latex": eq.get("latex", ""),
                "audit_status": eq.get("audit_status", "none"),
                # Fields for the auditor to fill in:
                "new_latex": "",
                "new_status": "",  # ok, typo, error, critical
                "error_note": "",
                "severity": "",  # TYPO, MINOR, MAJOR, CRITICAL
            })

        out_path = BATCH_DIR / f"{batch_id}.json"
        with open(out_path, 'w', encoding='utf-8') as f:
            json.dump(batch_data, f, indent=2, ensure_ascii=False)

    # Write manifest
    manifest = {
        "label": label,
        "total_batches": len(batches),
        "total_equations": sum(len(b) for b in batches),
        "batch_files": [f"{label}_batch_{i+1:04d}.json" for i in range(len(batches))]
    }
    manifest_path = BATCH_DIR / f"{label}_manifest.json"
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    print(f"Manifest: {manifest_path}")
    print(f"Batches written to: {BATCH_DIR}")


def apply_results(results_file):
    """Apply audit results back to the knowledge index."""
    idx = load_index()
    eqs = idx.get('equations', [])
    eq_map = {eq['id']: eq for eq in eqs}

    with open(results_file, 'r', encoding='utf-8') as f:
        results = json.load(f)

    applied = 0
    errors_found = 0
    latex_added = 0

    for r in results.get('equations', []):
        eq_id = r.get('id')
        if eq_id not in eq_map:
            print(f"WARNING: {eq_id} not found in index")
            continue

        eq = eq_map[eq_id]

        # Apply new LaTeX
        if r.get('new_latex'):
            eq['latex'] = r['new_latex']
            latex_added += 1

        # Apply audit status
        if r.get('new_status'):
            eq['audit_status'] = r['new_status']

        # Apply error info
        if r.get('error_note'):
            eq['error_note'] = r['error_note']
            eq['severity'] = r.get('severity', 'UNKNOWN')
            errors_found += 1

        applied += 1

    save_index(idx)
    print(f"Applied {applied} results: {latex_added} LaTeX added, {errors_found} errors flagged")


def main():
    parser = argparse.ArgumentParser(description="Equation audit batcher")
    parser.add_argument('--mode', choices=['stats', 'extract', 'apply'], required=True)
    parser.add_argument('--source-type', choices=['sessions', 'tier0'], default=None)
    parser.add_argument('--source-file', default=None)
    parser.add_argument('--batch-size', type=int, default=50)
    parser.add_argument('--results-file', default=None)
    args = parser.parse_args()

    idx = load_index()

    if args.mode == 'stats':
        stats_mode(idx)
    elif args.mode == 'extract':
        extract_mode(idx, args.source_type, args.source_file, args.batch_size)
    elif args.mode == 'apply':
        if not args.results_file:
            print("ERROR: --results-file required for apply mode")
            sys.exit(1)
        apply_results(args.results_file)


if __name__ == '__main__':
    main()
