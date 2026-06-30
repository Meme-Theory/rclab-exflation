"""Build the `constants` entity table from computations/_shared/canonical_constants.py.

Stage A — standalone tool that:
  1. Walks canonical_constants.py via AST → captures line numbers per top-level
     assignment.
  2. Imports the live module → captures the actual value of each constant.
  3. Joins with the PROVENANCE dict to add session/source/gate fields where
     available; rows without PROVENANCE get null session/source/gate so the
     232 unannotated constants become a backfill worklist.
  4. (Optional, --apply) Patches tools/knowledge-index.json:
     - Adds top-level `constants` key with the new entity table
     - Filters `constants_audit` to drop the IMPORT_OK compliance noise
       (keeps only POTENTIAL_HARDCODE + TAU_FOLD=0.19 violation rows)

Defaults to --dry-run. Same safety model as _scrub_equations_prose.py and
_scrub_gates.py: backup before write, atomic rename via .tmp.

After running with --apply, run `tools/_dump_kb_to_markdown.py` to regenerate
the kb-dumps markdown (will produce a new `tools/kb-dumps/constants.md`).

Stage B (durability): the same extraction logic must be ported into
`tools/extract_entities.py` so that `/weave --update` rebuilds the table.
Without that, the next extractor run wipes Stage A's changes.
"""

from __future__ import annotations

import argparse
import ast
import importlib.util
import json
import shutil
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INDEX_PATH = ROOT / "knowledge-index.json"
CANONICAL_CONSTANTS_PATH = (
    ROOT.parent / "computations" / "_shared" / "canonical_constants.py"
)
REPORT_PATH = ROOT / "_build_constants_table_report.json"

# Module-level names that are NOT data constants but happen to appear in
# canonical_constants.py — exclude from the entity table.
EXCLUDED_NAMES = {
    "PROVENANCE",        # the provenance metadata dict — joined separately
    "CHANNEL_LABELS",    # config dict, not a physics constant
}

# Also exclude any name starting with one of these prefixes — these namespaces
# are extractor-internal configuration, not physics constants.
EXCLUDED_PREFIXES = (
    "AUDIT_",     # AUDIT_EXEMPT_SCRIPTS, AUDIT_PATTERNS_COMPILED, AUDIT_SESSION_FLOOR
    "EXEMPT_",    # EXEMPT_FILES
)


def _is_excluded(name: str) -> bool:
    if name in EXCLUDED_NAMES:
        return True
    return any(name.startswith(p) for p in EXCLUDED_PREFIXES)


def extract_canonical_constants_entities() -> list[dict]:
    """Walk canonical_constants.py + PROVENANCE → list of entity rows."""
    # 1. AST scan for line numbers
    src = CANONICAL_CONSTANTS_PATH.read_text(encoding="utf-8")
    tree = ast.parse(src, filename=str(CANONICAL_CONSTANTS_PATH))

    line_map: dict[str, int] = {}
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    line_map[target.id] = node.lineno
        elif isinstance(node, ast.AnnAssign):
            if isinstance(node.target, ast.Name):
                line_map[node.target.id] = node.lineno

    # 2. Import the live module
    spec = importlib.util.spec_from_file_location(
        "canonical_constants_for_index", CANONICAL_CONSTANTS_PATH
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {CANONICAL_CONSTANTS_PATH}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    provenance = getattr(mod, "PROVENANCE", {})
    if not isinstance(provenance, dict):
        provenance = {}

    # 3. Build entity rows
    constants: list[dict] = []
    for name in sorted(dir(mod)):
        if name.startswith("_"):
            continue
        if _is_excluded(name):
            continue
        if name not in line_map:
            continue  # imported or computed elsewhere, not a top-level assign
        val = getattr(mod, name)
        if callable(val):
            continue

        # JSON-safe value representation
        if isinstance(val, (int, float, bool, str)) and not isinstance(val, bool):
            # str(bool) is True/False — we want JSON booleans
            value_repr = val
        elif isinstance(val, bool):
            value_repr = val
        elif val is None:
            value_repr = None
        else:
            value_repr = repr(val)

        prov = provenance.get(name, {})
        if not isinstance(prov, dict):
            prov = {}

        constants.append({
            "id": name,
            "name": name,
            "value": value_repr,
            "value_type": type(val).__name__,
            "session": prov.get("session"),
            "source": prov.get("source"),
            "gate": prov.get("gate"),
            "superseded": prov.get("superseded", False),
            "line": line_map[name],
            "source_file": "computations/_shared/canonical_constants.py",
        })

    return constants


def filter_constants_audit(audit_rows: list[dict]) -> tuple[list[dict], int]:
    """Drop IMPORT_OK noise rows. Returns (kept_rows, dropped_count)."""
    kept: list[dict] = []
    dropped = 0
    for r in audit_rows:
        if isinstance(r, dict) and r.get("pattern") == "IMPORT_OK":
            dropped += 1
        else:
            kept.append(r)
    return kept, dropped


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--apply",
        action="store_true",
        help="Actually patch tools/knowledge-index.json (default: dry-run)",
    )
    args = ap.parse_args()

    print(f"Loading {CANONICAL_CONSTANTS_PATH} ...")
    constants = extract_canonical_constants_entities()
    print(f"  extracted {len(constants):,} constants")

    with_prov = sum(1 for c in constants if c["session"])
    without_prov = len(constants) - with_prov
    superseded = sum(1 for c in constants if c["superseded"])

    print(f"  with provenance (session set): {with_prov:,}")
    print(f"  without provenance (backfill worklist): {without_prov:,}")
    print(f"  superseded: {superseded:,}")

    # Type distribution
    from collections import Counter
    type_dist = Counter(c["value_type"] for c in constants)
    print(f"  value_type distribution: {dict(type_dist.most_common())}")

    print(f"\nLoading {INDEX_PATH} ...")
    with INDEX_PATH.open("r", encoding="utf-8") as f:
        idx = json.load(f)

    existing_constants = idx.get("constants")
    if existing_constants is not None:
        print(f"  WARNING: index already has 'constants' key with "
              f"{len(existing_constants)} rows — will be replaced")

    audit_rows = idx.get("constants_audit", [])
    kept_audit, dropped_audit = filter_constants_audit(audit_rows)
    print(f"  constants_audit: {len(audit_rows):,} → {len(kept_audit):,} "
          f"({dropped_audit:,} IMPORT_OK rows to drop)")

    # Report
    report = {
        "dry_run": not args.apply,
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "constants_table": {
            "total_rows": len(constants),
            "with_provenance": with_prov,
            "without_provenance": without_prov,
            "superseded": superseded,
            "value_type_distribution": dict(type_dist.most_common()),
            "sample_with_provenance": [c for c in constants if c["session"]][:10],
            "sample_without_provenance": [c for c in constants if not c["session"]][:10],
        },
        "constants_audit_cleanup": {
            "before": len(audit_rows),
            "after": len(kept_audit),
            "dropped_IMPORT_OK": dropped_audit,
            "kept_violations": kept_audit,
        },
    }
    with REPORT_PATH.open("w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2, default=str)

    print(f"\nFull report: {REPORT_PATH}")

    print("\n" + "=" * 60)
    print(f"{'DRY-RUN — NO CHANGES WRITTEN' if not args.apply else 'APPLY MODE'}")
    print("=" * 60)
    print(f"Constants extracted:        {len(constants):>6,}")
    print(f"  with provenance:          {with_prov:>6,}")
    print(f"  without (backfill todo):  {without_prov:>6,}")
    print(f"constants_audit kept:       {len(kept_audit):>6,}")
    print(f"constants_audit dropped:    {dropped_audit:>6,}")

    if not args.apply:
        print("\nThis was a DRY RUN — no files were modified.")
        print("Re-run with --apply to patch tools/knowledge-index.json.")
        return

    # ----- APPLY -----
    backup_path = INDEX_PATH.with_suffix(
        f".bak.constants.{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
    )
    print(f"\nBacking up index to {backup_path} ...")
    shutil.copy2(INDEX_PATH, backup_path)

    new_idx = dict(idx)
    new_idx["constants"] = constants
    new_idx["constants_audit"] = kept_audit

    tmp_path = INDEX_PATH.with_suffix(".tmp")
    print(f"Writing patched index to temp file {tmp_path} ...")
    with tmp_path.open("w", encoding="utf-8") as f:
        json.dump(new_idx, f, ensure_ascii=False, indent=2)
    tmp_path.replace(INDEX_PATH)
    print(f"Done. Backup retained at: {backup_path}")
    print("\nNext steps:")
    print("  1. Regenerate markdown dumps: python tools/_dump_kb_to_markdown.py")
    print("  2. Patch extract_entities.py (Stage B) so /weave --update preserves this.")


if __name__ == "__main__":
    main()
