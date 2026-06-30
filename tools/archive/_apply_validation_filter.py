"""tools/_apply_validation_filter.py - Consumer-layer filter for knowledge-index.json.

Reads `tools/knowledge-index.json` (the canonical extractor output) and applies
two filters at the consumer layer (without touching extract_entities.py):

  Filter 1 (AUDITED_NOISE): drop entries the Haiku audit marked NOISE in
    `tools/_anchor_validation_results.json`. Match by (table, source_file, name)
    fingerprint because the audit's anchor_id format uses SQLite rowids for
    some tables (open_channels, data_provenance) that aren't in the JSON.

  Filter 2 (ATLAS_SOURCE): drop entries whose source_file matches
    `framework/Atlas/` (case-insensitive). Atlas docs are synthesis/catalog
    products, not derivation sources.

Outputs:
  tools/knowledge-index.filtered.json   - filtered version (only if --apply)
  tools/_filter_drop_log.json           - per-entry drop record with reasons

Dry-run mode (default): prints per-table before/after counts AND the residual
count of unaudited equations (since only 500 of 22,593 equations have audit
verdicts; pre-filter sizing tells us what's left to audit).

Usage:
  python tools/_apply_validation_filter.py            # dry-run (default)
  python tools/_apply_validation_filter.py --apply    # write filtered JSON
"""
import argparse
import json
import re
from pathlib import Path
from collections import defaultdict, Counter

ROOT = Path(".")
INDEX = ROOT / "tools" / "knowledge-index.json"
AGG = ROOT / "tools" / "_anchor_validation_results.json"
BATCH = ROOT / "tools" / "anchor_validation_batches"
OUT_FILTERED = ROOT / "tools" / "knowledge-index.filtered.json"
OUT_LOG = ROOT / "tools" / "_filter_drop_log.json"


def is_atlas(sf):
    if not sf:
        return False
    return "framework/atlas/" in sf.replace("\\", "/").lower()


def _norm_path(s):
    return (s or "").replace("\\", "/").lower()


def audit_fingerprint(table, entity):
    """Reconstruct the audit-time fingerprint (table, source_file, name) for a batch entry.

    Batch entries carry source_file + name in audit-time form (per the per-table
    yield logic in _haiku_anchor_audit.py:114-256). Use the entity dict directly.
    """
    sf = _norm_path(entity.get("source_file"))
    nm = (entity.get("name") or "").strip()
    return (table, sf, nm)


def index_fingerprint(table, entity):
    """Reconstruct what the audit WOULD have computed for an index entry.

    Per-table field mapping mirrors _haiku_anchor_audit.py:114-256 verbatim:
      closed_mechanisms  -> source_file (DB), name
      open_channels      -> source_file (DB), name
      theorems           -> source_file (DB), name
      gates              -> source_file (DB), name
      data_provenance    -> "computations/" + script, name
      session_files      -> path, filename
      equations          -> source_file or file, name (raw, trimmed at audit)
      researchers        -> path.rstrip("/") + "/index.md", domain
      agents             -> source_file, name
      registries         -> source_file, title
    """
    sf = ""
    nm = ""
    if table == "data_provenance":
        script = entity.get("script") or ""
        sf = _norm_path("computations/" + script) if script else ""
        nm = (entity.get("name") or "").strip()
    elif table == "session_files":
        sf = _norm_path(entity.get("path"))
        nm = (entity.get("filename") or "").strip()
    elif table == "researchers":
        p = (entity.get("path") or "").rstrip("/")
        sf = _norm_path((p + "/index.md") if p else "")
        nm = (entity.get("domain") or "").strip()
    elif table == "agents":
        sf = _norm_path(entity.get("source_file"))
        nm = (entity.get("name") or "").strip()
    elif table == "registries":
        sf = _norm_path(entity.get("source_file"))
        # registries audit-batch yields name=title; index field is also title
        nm = (entity.get("title") or entity.get("name") or "").strip()
    elif table == "equations":
        # equations: source_file fallback to `file`; name is the trimmed raw (200 chars)
        sf = _norm_path(entity.get("source_file") or entity.get("file"))
        # audit truncates raw via _trim(raw, 200); for matching we use the same truncation
        raw = entity.get("raw") or entity.get("name") or ""
        if len(raw) > 200:
            raw = raw[:200] + "..."
        nm = raw.strip()
    else:
        # theorems, closed_mechanisms, open_channels, gates -> straight (source_file, name)
        sf = _norm_path(entity.get("source_file"))
        nm = (entity.get("name") or "").strip()
    return (table, sf, nm)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true",
                    help="Write filtered JSON + drop log. Default: dry-run only.")
    args = ap.parse_args()

    print(f"Loading {INDEX}...")
    index = json.loads(INDEX.read_text(encoding="utf-8"))
    print(f"Loading {AGG}...")
    agg = json.loads(AGG.read_text(encoding="utf-8"))

    # Build NOISE-fingerprint set from the audit + batch files
    # batches carry (anchor_id, entity-data); audit carries (anchor_id, verdict)
    # Map: anchor_id -> (table, source_file, name) for NOISE-classified entries
    print(f"Loading {BATCH}/ for fingerprint reconstruction...")
    noise_fingerprints = set()
    audited_fingerprints_by_table = defaultdict(set)  # all audited entries (for stats)
    for b in sorted(BATCH.glob("*.json")):
        try:
            payload = json.loads(b.read_text(encoding="utf-8"))
        except Exception:
            continue
        table = payload.get("table")
        for a in payload.get("anchors", []):
            aid = a.get("anchor_id")
            if not aid or not table:
                continue
            verdict = agg.get(table, {}).get(aid, {}).get("verdict")
            if not verdict:
                continue
            fp = audit_fingerprint(table, a)
            audited_fingerprints_by_table[table].add(fp)
            if verdict == "NOISE":
                noise_fingerprints.add(fp)
    print(f"  NOISE fingerprints: {len(noise_fingerprints)}")

    # Tables in the index that carry entity lists (entity tables, not edges/meta)
    ENTITY_TABLES = [
        "theorems", "closed_mechanisms", "open_channels", "gates",
        "data_provenance", "session_files", "equations",
        "researchers", "agents", "registries",
    ]

    # Apply filters per table
    drop_log = []
    counts_before = {}
    counts_after = {}
    counts_drop_atlas = Counter()
    counts_drop_noise = Counter()
    filtered_index = {k: v for k, v in index.items() if k not in ENTITY_TABLES}

    # Equations-audit-residual tracking
    eq_total_pre = 0
    eq_atlas_drop = 0
    eq_noise_drop = 0
    eq_already_audited_kept = 0
    eq_unaudited_kept = 0

    for table in ENTITY_TABLES:
        items = index.get(table, [])
        counts_before[table] = len(items)
        kept = []
        for e in items:
            fp = index_fingerprint(table, e)
            sf = e.get("source_file") or ""
            drop_reason = None
            if fp in noise_fingerprints:
                drop_reason = "AUDITED_NOISE"
            elif is_atlas(sf):
                drop_reason = "ATLAS_SOURCE"

            if drop_reason:
                counts_drop_noise[table] += (drop_reason == "AUDITED_NOISE")
                counts_drop_atlas[table] += (drop_reason == "ATLAS_SOURCE")
                drop_log.append({
                    "table": table,
                    "reason": drop_reason,
                    "fingerprint": list(fp),
                    "id": e.get("id"),
                    "name": (e.get("name") or "")[:120],
                    "source_file": sf,
                })
                if table == "equations":
                    if drop_reason == "ATLAS_SOURCE":
                        eq_atlas_drop += 1
                    else:
                        eq_noise_drop += 1
            else:
                kept.append(e)
                if table == "equations":
                    if fp in audited_fingerprints_by_table.get("equations", set()):
                        eq_already_audited_kept += 1
                    else:
                        eq_unaudited_kept += 1
        counts_after[table] = len(kept)
        filtered_index[table] = kept
        eq_total_pre = counts_before.get("equations", 0)

    # Pretty-print summary
    print()
    print("=" * 90)
    print(f"FILTER DRY-RUN  ({'WILL WRITE' if args.apply else 'DRY-RUN, NO WRITE'})")
    print("=" * 90)
    print(f"{'table':<22}{'before':>9}{'dropped':>9}{'  (noise':>10}{'  atlas)':>10}{'after':>9}{'drop%':>8}")
    total_before = total_after = total_drop_noise = total_drop_atlas = 0
    for t in ENTITY_TABLES:
        b = counts_before.get(t, 0)
        dn = counts_drop_noise[t]
        da = counts_drop_atlas[t]
        d = dn + da
        a = counts_after.get(t, 0)
        pct = (d / b * 100) if b else 0
        print(f"{t:<22}{b:>9}{d:>9}{dn:>10}{da:>10}{a:>9}{pct:>7.1f}%")
        total_before += b; total_after += a; total_drop_noise += dn; total_drop_atlas += da
    print("-" * 90)
    print(f"{'TOTAL':<22}{total_before:>9}{total_drop_noise+total_drop_atlas:>9}"
          f"{total_drop_noise:>10}{total_drop_atlas:>10}{total_after:>9}"
          f"{(total_drop_noise+total_drop_atlas)/total_before*100:>7.1f}%")
    print()
    print("Equations-audit residual breakdown:")
    print(f"  Total equations pre-filter:           {eq_total_pre}")
    print(f"  - dropped (Atlas source):             {eq_atlas_drop}")
    print(f"  - dropped (audited NOISE):            {eq_noise_drop}")
    print(f"  = kept                                {eq_already_audited_kept + eq_unaudited_kept}")
    print(f"    of which already audited VALID:     {eq_already_audited_kept}")
    print(f"    of which UNAUDITED (need Haiku):    {eq_unaudited_kept}  <-- residual audit scope")
    print()
    if args.apply:
        OUT_FILTERED.write_text(json.dumps(filtered_index, indent=2, ensure_ascii=False), encoding="utf-8")
        OUT_LOG.write_text(json.dumps({
            "summary": {
                "total_before": total_before,
                "total_after": total_after,
                "total_dropped_noise": total_drop_noise,
                "total_dropped_atlas": total_drop_atlas,
            },
            "per_table_before": counts_before,
            "per_table_after": counts_after,
            "per_table_drop_noise": dict(counts_drop_noise),
            "per_table_drop_atlas": dict(counts_drop_atlas),
            "equations_audit_residual": {
                "total_pre": eq_total_pre,
                "atlas_drop": eq_atlas_drop,
                "noise_drop": eq_noise_drop,
                "kept_already_audited_valid": eq_already_audited_kept,
                "kept_unaudited": eq_unaudited_kept,
            },
            "drops": drop_log,
        }, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"WROTE: {OUT_FILTERED}")
        print(f"WROTE: {OUT_LOG}")
    else:
        print("(dry-run; no files written. Re-run with --apply to write filtered JSON + drop log.)")


if __name__ == "__main__":
    main()
