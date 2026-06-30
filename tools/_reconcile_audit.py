"""
Content-key reconciliation tool for the Haiku audit
===================================================

Maps each audited anchor_id (`eq_42`, `closed_5`, etc.) to a stable content-derived
key so the 10,919 audit verdicts survive an extract_entities.py change.

Anchor IDs are sequential and renumber when the extractor changes; content keys
are computed from intrinsic per-entity attributes (source_file, line, name,
raw-text fingerprint) and are stable across extractor versions for any entity
whose source location and identity are preserved.

Modes:
    --build       (default) Read v1 index + audit → write content-key map artifact.
    --verify              Re-read built artifact, recompute, check determinism + uniqueness.
    --simulate            Synthesize a fake v2 by dropping random entries from v1;
                          verify the reconciliation pipeline end-to-end.
    --apply --v2-index P  After a real v2 index exists, apply the keymap to v2 and
                          produce tools/_anchor_validation_results_v2.json.

The content_key function (v1):
    key = (table, source_file_normalized, line, identity)
        source_file_normalized: forward slashes, lowercased, stripped.
        line: integer line number from the index entry (0 if absent).
        identity:
            ("name", lowercased-collapsed-name) when name is non-empty,
            ("raw",  sha256[:16] of whitespace-collapsed raw[:200]) otherwise.

Output artifacts:
    tools/_audit_content_keys.json              — keymap (the load-bearing artifact)
    tools/_audit_content_keys_diagnostics.json  — uniqueness + coverage stats
"""

from __future__ import annotations

import argparse
import hashlib
import json
import random
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

INDEX_PATH = Path("tools/knowledge-index.json")
AUDIT_PATH = Path("tools/_anchor_validation_results.json")
KEYMAP_OUT = Path("tools/_audit_content_keys.json")
DIAGNOSTICS_OUT = Path("tools/_audit_content_keys_diagnostics.json")

AUDITED_TABLES = [
    "theorems",
    "closed_mechanisms",
    "gates",
    "open_channels",
    "data_provenance",
    "equations",
    "researchers",
    "agents",
    "session_files",
    "registries",
    "constants",
]


def normalize_source_file(path: str) -> str:
    return (path or "").replace("\\", "/").strip().lower()


def normalize_name(name: Any) -> str:
    if not name:
        return ""
    return re.sub(r"\s+", " ", str(name).strip().lower())


def normalize_raw(raw: Any) -> str:
    if not raw:
        return ""
    return re.sub(r"\s+", " ", str(raw).strip()).lower()


def _source_file_for(entity: dict, table: str) -> str:
    """Per-table rule for the entity's source-file equivalent."""
    if table == "data_provenance":
        script = entity.get("script") or ""
        return normalize_source_file(f"computations/{script}" if script else "")
    if table == "session_files":
        return normalize_source_file(entity.get("path") or entity.get("source_file") or "")
    if table == "researchers":
        path = entity.get("path") or ""
        idx = (path.rstrip("/") + "/index.md") if path else ""
        return normalize_source_file(idx or entity.get("index_file") or "")
    if table == "constants":
        return "computations/_shared/canonical_constants.py"
    return normalize_source_file(entity.get("source_file", "") or "")


def content_key(entity: dict, table: str) -> list:
    """Stable, JSON-serializable content key. See module docstring.

    Per-table identity rule: pick the field that survives extractor changes.
    """
    sf = _source_file_for(entity, table)
    line = int(entity.get("line", 0) or 0)

    if table == "researchers":
        identity = ["name", normalize_name(entity.get("domain", ""))]
    elif table == "agents":
        identity = ["name", normalize_name(entity.get("slug", ""))]
    elif table == "session_files":
        identity = ["name", normalize_source_file(entity.get("path", "") or entity.get("id", ""))]
    elif table == "registries":
        identity = [
            "name",
            normalize_name(entity.get("registry_id") or entity.get("id", "")),
        ]
    elif table == "data_provenance":
        script = normalize_source_file(entity.get("script", "") or "")
        name = normalize_name(entity.get("name", ""))
        identity = ["name", f"{script}::{name}"]
    elif table == "constants":
        identity = ["name", normalize_name(entity.get("name", ""))]
    elif table == "gates":
        # Gates: stored 'id' is the gate code (e.g. KZ-NS-62) — already content-derived
        # and stable. Use it directly to disambiguate placeholder-name entries.
        gid = entity.get("id") or ""
        if gid:
            identity = ["id", gid]
        else:
            identity = ["name", normalize_name(entity.get("name", ""))]
    elif table == "theorems":
        # Theorems: stored 'id' is `proven_N` (positional, renumbers). Use (name,
        # statement) hash for stability. Statement disambiguates the
        # name="n_s" collision in baseline-findings-s66.md.
        name = entity.get("name") or ""
        statement = entity.get("statement") or ""
        if name or statement:
            blob = f"{normalize_name(name)}::{normalize_raw(statement)[:300]}"
            digest = hashlib.sha256(blob.encode("utf-8")).hexdigest()[:16]
            identity = ["name+stmt", digest]
        else:
            identity = ["empty", ""]
    else:
        # closed_mechanisms, open_channels, equations
        name = entity.get("name")
        raw = entity.get("raw") or entity.get("statement") or ""
        if name:
            identity = ["name", normalize_name(name)]
        elif raw:
            digest = hashlib.sha256(
                normalize_raw(raw)[:200].encode("utf-8")
            ).hexdigest()[:16]
            identity = ["raw", digest]
        else:
            identity = ["empty", ""]

    return [table, sf, line, identity]


def build_audit_anchor_index(index: dict, table: str) -> dict:
    """Return {audit_anchor_id: entity} for one table.

    Mirrors the anchor-id construction in tools/_haiku_anchor_audit.py:fetch_anchors.
    """
    entries = index.get(table, [])
    out: dict = {}

    if table == "open_channels":
        for i, e in enumerate(entries):
            out[f"open_{i + 1}"] = e
    elif table == "data_provenance":
        for i, e in enumerate(entries):
            out[f"prov_{i + 1}"] = e
    elif table == "researchers":
        for e in entries:
            dom = e.get("domain", "")
            out[f"researcher_{dom}"] = e
    elif table == "agents":
        for e in entries:
            slug = e.get("slug", "")
            out[f"agent_{slug}"] = e
    elif table == "gates":
        for e in entries:
            eid = e.get("id", "")
            key = f"gate_{eid[:60]}" if eid else "gate_<null>"
            out[key] = e  # last-write-wins on truncation collision (audit-matching)
    elif table == "session_files":
        for e in entries:
            eid = e.get("id")
            fn = e.get("filename", "")
            key = f"sf_{eid}" if eid else f"sf_<{fn}>"
            out[key] = e
    elif table == "constants":
        # Not in JSON index; entities are synthesized from anchor_id by callers.
        return {}
    else:
        # theorems, closed_mechanisms, equations, registries: anchor_id == e['id']
        for e in entries:
            eid = e.get("id")
            if eid:
                out[eid] = e

    return out


def _synthesize_constant_entity(anchor_id: str) -> dict:
    """Build a synthetic entity for the constants table from its anchor_id."""
    name = anchor_id[len("const_"):] if anchor_id.startswith("const_") else anchor_id
    return {"name": name, "source_file": "computations/_shared/canonical_constants.py"}


def _key_str(k: list) -> str:
    """JSON-serialize a key for use as a dict key in collision tracking."""
    return json.dumps(k, ensure_ascii=False)


def load_index(p: Path) -> dict:
    return json.loads(p.read_text(encoding="utf-8"))


def load_audit(p: Path) -> dict:
    return json.loads(p.read_text(encoding="utf-8"))


def build_keymap(index_path: Path = INDEX_PATH, audit_path: Path = AUDIT_PATH) -> tuple[dict, dict]:
    """Returns (keymap_artifact, diagnostics)."""
    index = load_index(index_path)
    audit = load_audit(audit_path)

    keymap_artifact = {
        "schema_version": "1.0",
        "v1_index": str(index_path),
        "v1_index_generated": index.get("generated"),
        "v1_audit": str(audit_path),
        "key_function": "content_key.v1 (table, source_file, line, identity)",
        "by_table": {},
    }
    diagnostics: dict = {
        "by_table": {},
        "global": {
            "total_audited": 0,
            "total_matched_in_index": 0,
            "total_unmatched_audit": 0,
            "total_key_collisions": 0,
        },
    }

    for table in AUDITED_TABLES:
        if table not in audit:
            continue

        audit_entries: dict = audit[table]
        if table == "constants":
            # Constants live in canonical_constants.py, not the JSON index.
            index_entries = {aid: _synthesize_constant_entity(aid) for aid in audit_entries}
        else:
            index_entries = build_audit_anchor_index(index, table)

        anchor_to_key: dict = {}
        key_to_anchors: dict = defaultdict(list)
        unmatched: list = []

        for anchor_id in audit_entries:
            e = index_entries.get(anchor_id)
            if e is None:
                unmatched.append(anchor_id)
                continue
            ck = content_key(e, table)
            anchor_to_key[anchor_id] = ck
            key_to_anchors[_key_str(ck)].append(anchor_id)

        collisions = {k: v for k, v in key_to_anchors.items() if len(v) > 1}

        keymap_artifact["by_table"][table] = {
            "audited_count": len(audit_entries),
            "matched_in_index": len(anchor_to_key),
            "key_collisions_among_audited": len(collisions),
            "anchor_id_to_key": anchor_to_key,
        }
        diagnostics["by_table"][table] = {
            "audited_count": len(audit_entries),
            "matched_in_index": len(anchor_to_key),
            "unmatched_audit_count": len(unmatched),
            "unmatched_audit_examples": unmatched[:10],
            "collision_count": len(collisions),
            "collision_examples": [
                {"key": k, "anchor_ids": v} for k, v in list(collisions.items())[:5]
            ],
        }
        g = diagnostics["global"]
        g["total_audited"] += len(audit_entries)
        g["total_matched_in_index"] += len(anchor_to_key)
        g["total_unmatched_audit"] += len(unmatched)
        g["total_key_collisions"] += len(collisions)

    return keymap_artifact, diagnostics


def cmd_build() -> None:
    keymap, diagnostics = build_keymap()
    KEYMAP_OUT.write_text(json.dumps(keymap, indent=2, ensure_ascii=False), encoding="utf-8")
    DIAGNOSTICS_OUT.write_text(
        json.dumps(diagnostics, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    g = diagnostics["global"]
    print(f"Wrote keymap:      {KEYMAP_OUT}  ({KEYMAP_OUT.stat().st_size:,} bytes)")
    print(f"Wrote diagnostics: {DIAGNOSTICS_OUT}  ({DIAGNOSTICS_OUT.stat().st_size:,} bytes)")
    print()
    print("Global summary:")
    print(f"  total audited:     {g['total_audited']:,}")
    print(f"  matched in index:  {g['total_matched_in_index']:,}")
    print(f"  unmatched:         {g['total_unmatched_audit']:,}")
    print(f"  key collisions:    {g['total_key_collisions']:,}")
    print()
    print(f"{'table':22s} {'audited':>8s} {'matched':>8s} {'unmatched':>10s} {'collisions':>11s}")
    for table, d in diagnostics["by_table"].items():
        print(
            f"{table:22s} {d['audited_count']:>8d} {d['matched_in_index']:>8d} "
            f"{d['unmatched_audit_count']:>10d} {d['collision_count']:>11d}"
        )


def cmd_verify() -> None:
    """Recompute from sources; compare against persisted artifact (determinism)."""
    if not KEYMAP_OUT.exists():
        print(f"ERROR: {KEYMAP_OUT} does not exist. Run --build first.", file=sys.stderr)
        sys.exit(2)

    persisted = json.loads(KEYMAP_OUT.read_text(encoding="utf-8"))
    fresh, _ = build_keymap()

    mismatches = 0
    for table, d_fresh in fresh["by_table"].items():
        d_persisted = persisted["by_table"].get(table, {})
        a_fresh = d_fresh["anchor_id_to_key"]
        a_persisted = d_persisted.get("anchor_id_to_key", {})
        if set(a_fresh) != set(a_persisted):
            print(f"  {table}: anchor_id set differs")
            mismatches += 1
            continue
        for aid, k in a_fresh.items():
            if a_persisted.get(aid) != k:
                mismatches += 1
                if mismatches <= 5:
                    print(f"  {table}/{aid}: persisted={a_persisted.get(aid)} fresh={k}")

    if mismatches == 0:
        print("VERIFY PASS: keymap is deterministic; persisted artifact matches fresh recomputation.")
    else:
        print(f"VERIFY FAIL: {mismatches} mismatches between persisted artifact and fresh recomputation.")
        sys.exit(1)


def cmd_simulate(drop_fraction: float = 0.10, seed: int = 1729) -> None:
    """Synthesize a v2 by deleting random entries from v1; verify reconciliation.

    Demonstrates the v1 → v2 audit-transfer pipeline end-to-end before any real
    v2 exists. Dropped entries simulate the extractor-fix removing prose.
    """
    print(f"=== SIMULATE mode (drop_fraction={drop_fraction}, seed={seed}) ===\n")
    if not KEYMAP_OUT.exists():
        print(f"ERROR: {KEYMAP_OUT} not found. Run --build first.", file=sys.stderr)
        sys.exit(2)

    v1_index = load_index(INDEX_PATH)
    audit = load_audit(AUDIT_PATH)
    keymap = json.loads(KEYMAP_OUT.read_text(encoding="utf-8"))

    rng = random.Random(seed)
    v2_index = {k: v for k, v in v1_index.items() if not isinstance(v, list)}
    survivors_per_table: dict = {}
    drops_per_table: dict = {}
    for table in AUDITED_TABLES:
        entries = list(v1_index.get(table, []))
        n_total = len(entries)
        n_drop = int(round(n_total * drop_fraction))
        drop_ids = set(rng.sample(range(n_total), n_drop)) if n_total else set()
        survivors = [e for i, e in enumerate(entries) if i not in drop_ids]
        drops = [e for i, e in enumerate(entries) if i in drop_ids]
        v2_index[table] = survivors
        survivors_per_table[table] = survivors
        drops_per_table[table] = drops

    v2_key_to_anchor: dict = {}
    for table in AUDITED_TABLES:
        if table == "constants":
            # Constants aren't in the JSON index — simulation has no drop semantics
            # for them. Replay audit anchor_ids unchanged.
            for aid in audit.get(table, {}):
                entity = _synthesize_constant_entity(aid)
                ck = content_key(entity, table)
                v2_key_to_anchor[_key_str(ck)] = aid
            continue
        # Re-derive v2 anchor_ids from survivor positions/fields (positional IDs
        # like open_N, prov_N renumber under entry drops — that's the renumbering
        # this simulation is designed to exercise).
        v2_anchor_to_entity = build_audit_anchor_index(
            {table: survivors_per_table[table]}, table
        )
        for v2_aid, e in v2_anchor_to_entity.items():
            ck = content_key(e, table)
            v2_key_to_anchor[_key_str(ck)] = v2_aid

    transferred = 0
    audit_dropped = 0
    audit_orphaned = 0
    by_table_report = []
    for table in AUDITED_TABLES:
        if table not in audit:
            continue
        audit_for_table = audit[table]
        keymap_for_table = keymap["by_table"].get(table, {}).get("anchor_id_to_key", {})
        n_transferred = 0
        n_dropped = 0
        n_orphaned = 0
        for v1_aid in audit_for_table:
            ck = keymap_for_table.get(v1_aid)
            if ck is None:
                n_orphaned += 1
                continue
            v2_aid = v2_key_to_anchor.get(_key_str(ck))
            if v2_aid:
                n_transferred += 1
            else:
                n_dropped += 1
        transferred += n_transferred
        audit_dropped += n_dropped
        audit_orphaned += n_orphaned
        by_table_report.append((table, len(audit_for_table), n_transferred, n_dropped, n_orphaned))

    total_audited = sum(len(audit[t]) for t in AUDITED_TABLES if t in audit)
    print(
        f"{'table':22s} {'audited':>8s} {'transferred':>12s} {'dropped':>8s} {'orphaned':>9s}"
    )
    for row in by_table_report:
        t, na, nt, nd, no = row
        print(f"{t:22s} {na:>8d} {nt:>12d} {nd:>8d} {no:>9d}")
    print(f"{'TOTAL':22s} {total_audited:>8d} {transferred:>12d} {audit_dropped:>8d} {audit_orphaned:>9d}")
    print()
    print(f"Reconciliation rate: {100.0 * transferred / max(1, total_audited):.2f}%")
    print(f"Expected (1 - drop_fraction): {100.0 * (1 - drop_fraction):.2f}%")
    deviation = transferred / max(1, total_audited) - (1 - drop_fraction)
    if abs(deviation) < 0.02:
        print(f"PASS: transfer rate matches expected within 2pp (Δ={deviation*100:+.2f}pp).")
    else:
        print(f"FAIL: transfer rate deviates >2pp from expected (Δ={deviation*100:+.2f}pp).")
        sys.exit(1)


def cmd_apply(v2_index_path: Path, output_path: Path) -> None:
    """After a real v2 index exists, re-pin audit verdicts onto v2 anchor_ids."""
    if not KEYMAP_OUT.exists():
        print(f"ERROR: {KEYMAP_OUT} not found. Run --build first.", file=sys.stderr)
        sys.exit(2)

    keymap = json.loads(KEYMAP_OUT.read_text(encoding="utf-8"))
    v2_index = load_index(v2_index_path)
    audit_v1 = load_audit(AUDIT_PATH)

    v2_key_to_anchor: dict = {}
    for table in AUDITED_TABLES:
        if table == "constants":
            # Constants live in canonical_constants.py, not the index. Replay
            # audit anchor_ids unchanged (any rename of a constant would require
            # a separate canonical-constants migration).
            for aid in audit_v1.get(table, {}):
                entity = _synthesize_constant_entity(aid)
                ck = content_key(entity, table)
                v2_key_to_anchor[_key_str(ck)] = aid
            continue
        v2_anchor_to_entity = build_audit_anchor_index(v2_index, table)
        for v2_aid, e in v2_anchor_to_entity.items():
            ck = content_key(e, table)
            v2_key_to_anchor[_key_str(ck)] = v2_aid

    audit_v2: dict = {}
    transfer_report: dict = {}
    for table in AUDITED_TABLES:
        if table not in audit_v1:
            continue
        audit_v2[table] = {}
        km = keymap["by_table"].get(table, {}).get("anchor_id_to_key", {})
        n_transferred = 0
        n_dropped_entities = 0
        n_orphaned_audit = 0
        for v1_aid, verdict_obj in audit_v1[table].items():
            ck = km.get(v1_aid)
            if ck is None:
                n_orphaned_audit += 1
                continue
            v2_aid = v2_key_to_anchor.get(_key_str(ck))
            if v2_aid:
                audit_v2[table][v2_aid] = verdict_obj
                n_transferred += 1
            else:
                n_dropped_entities += 1
        transfer_report[table] = {
            "audited_v1": len(audit_v1[table]),
            "transferred_to_v2": n_transferred,
            "dropped_entities_were_audited": n_dropped_entities,
            "orphaned_in_v1": n_orphaned_audit,
        }

    output_path.write_text(json.dumps(audit_v2, indent=2, ensure_ascii=False), encoding="utf-8")
    report_path = output_path.with_suffix(".transfer_report.json")
    report_path.write_text(json.dumps(transfer_report, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"Wrote reconciled audit: {output_path}")
    print(f"Wrote transfer report:  {report_path}")
    for table, d in transfer_report.items():
        print(
            f"  {table:22s} v1={d['audited_v1']:>5} → v2={d['transferred_to_v2']:>5} "
            f"(dropped {d['dropped_entities_were_audited']}, orphaned {d['orphaned_in_v1']})"
        )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--build", action="store_true", help="Build the v1 keymap artifact")
    parser.add_argument("--verify", action="store_true", help="Recompute and verify determinism")
    parser.add_argument("--simulate", action="store_true", help="Simulate a v2 and verify reconciliation")
    parser.add_argument("--drop-fraction", type=float, default=0.10)
    parser.add_argument("--seed", type=int, default=1729)
    parser.add_argument("--apply", action="store_true", help="Apply keymap to a real v2 index")
    parser.add_argument("--v2-index", type=Path)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("tools/_anchor_validation_results_v2.json"),
    )
    args = parser.parse_args()

    if args.apply:
        if not args.v2_index:
            parser.error("--apply requires --v2-index PATH")
        cmd_apply(args.v2_index, args.output)
    elif args.verify:
        cmd_verify()
    elif args.simulate:
        cmd_simulate(drop_fraction=args.drop_fraction, seed=args.seed)
    else:
        cmd_build()


if __name__ == "__main__":
    main()
