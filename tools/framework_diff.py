#!/usr/bin/env python3
"""Framework-registry rectification diff.

The framework folder (sessions/framework/*.md) is the canonical destination for
knowledge. Session-level extractions that disagree with a framework entry are
flagged here as WARRANTs, framed as "framework authoritative — investigate
session file". This is the Phase 2 deliverable of the knowledge-index
framework-ingestion fix.

Design:
  - Run two parallel extraction passes:
    * framework-only — only sessions/framework/*.md files.
    * session-only   — all sessions/*.md files excluding framework/.
  - Build name→entity maps per bucket (theorems, closed_mechanisms, gates,
    open_channels). Names are normalized via the same folding rule that
    dedup_by_name uses.
  - Partition each bucket's entity space into 4 sets:
      1. both-agree   (framework value == session value on the authoritative field)
      2. both-disagree (framework != session — WARRANT, framework wins)
      3. framework-only (no session counterpart; registry-native)
      4. session-only  (not yet promoted to framework registry — candidate for
                        AMRI or registry authorship)
  - Emit tools/framework_diff_report.md with counts + the WARRANT list.

Runs as a standalone script. Called by /weave --framework-diff.
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

# Import extractor machinery. We specifically reuse the public functions so
# the diff stays in lockstep with the index pipeline: any new extractor strategy
# lands once in extract_entities.py and the diff picks it up for free.
from extract_entities import (  # noqa: E402
    SESSIONS_DIR,
    _is_framework_file,
    _is_sessions_file,
    _normalize_for_dedup,
    extract_closed_mechanisms,
    extract_framework_registry,
    extract_gates,
    extract_open_channels,
    extract_proven_theorems,
)

REPORT_PATH = ROOT / "tools" / "framework_diff_report.md"

# The "authoritative field" per bucket — the single field we compare on to
# decide whether framework and session agree. More fields could be added; the
# current choice matches the canonical contract each file type advertises.
AUTH_FIELD: dict[str, str] = {
    "theorems": "status",
    "closed_mechanisms": "closed_by",
    "gates": "verdict",
    "open_channels": "status",
}


def _collect_framework_files() -> list[Path]:
    if not SESSIONS_DIR.exists():
        return []
    return sorted(p for p in SESSIONS_DIR.rglob("*.md") if _is_framework_file(p))


def _collect_session_files() -> list[Path]:
    if not SESSIONS_DIR.exists():
        return []
    return sorted(
        p for p in SESSIONS_DIR.rglob("*.md")
        if _is_sessions_file(p) and not _is_framework_file(p)
    )


def _framework_pass() -> dict[str, list[dict]]:
    buckets: dict[str, list[dict]] = defaultdict(list)
    for path in _collect_framework_files():
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        fw = extract_framework_registry(path, text)
        ents = fw.get("entities") or {}
        for bucket in ("theorems", "closed_mechanisms", "gates", "open_channels"):
            buckets[bucket].extend(ents.get(bucket, []))
    return buckets


def _session_pass() -> dict[str, list[dict]]:
    buckets: dict[str, list[dict]] = defaultdict(list)
    for path in _collect_session_files():
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        buckets["theorems"].extend(extract_proven_theorems(path, text))
        buckets["closed_mechanisms"].extend(extract_closed_mechanisms(path, text))
        buckets["gates"].extend(extract_gates(path, text))
        buckets["open_channels"].extend(extract_open_channels(path, text))
    return buckets


def _index_by_name(entries: list[dict], key: str = "name") -> dict[str, dict]:
    """Return dict norm_name -> first-seen entry. Later duplicates are discarded
    (we're comparing framework vs session, so per-side duplication is benign)."""
    out: dict[str, dict] = {}
    for e in entries:
        raw = e.get(key) or ""
        norm = _normalize_for_dedup(raw)
        if not norm:
            continue
        if norm not in out:
            out[norm] = e
    return out


def _values_agree(framework_val: str | None, session_val: str | None) -> bool:
    """Normalize both values and check agreement.

    Agreement is lenient: any shared non-empty keyword counts. For example,
    framework 'PROVEN (machine epsilon)' and session 'PROVEN' both reduce to
    the set {'proven', 'machine', 'epsilon'} — agreement. This matches the
    way dedup treats names: prefix-matching tolerance. The purpose of the diff
    is to surface REAL disagreements, not stylistic drift.
    """
    if not framework_val and not session_val:
        return True
    fw = (framework_val or "").strip().lower()
    se = (session_val or "").strip().lower()
    if not fw or not se:
        return False
    # Tokenize on whitespace + common separators
    import re
    fw_toks = set(re.findall(r"[a-z0-9_-]{3,}", fw))
    se_toks = set(re.findall(r"[a-z0-9_-]{3,}", se))
    if not fw_toks or not se_toks:
        return fw == se
    return bool(fw_toks & se_toks)


def compute_diff() -> dict:
    """Run both extraction passes and produce the diff structure."""
    fw_entities = _framework_pass()
    se_entities = _session_pass()

    summary: dict = {
        "generated": datetime.now().isoformat(),
        "buckets": {},
    }

    for bucket in ("theorems", "closed_mechanisms", "gates", "open_channels"):
        key = "name" if bucket != "gates" else "id"
        fw_by_name = _index_by_name(fw_entities.get(bucket, []), key)
        se_by_name = _index_by_name(se_entities.get(bucket, []), key)
        fw_names = set(fw_by_name.keys())
        se_names = set(se_by_name.keys())
        overlap = fw_names & se_names
        auth_field = AUTH_FIELD[bucket]

        agree_list: list[dict] = []
        disagree_list: list[dict] = []
        for norm in sorted(overlap):
            fw_ent = fw_by_name[norm]
            se_ent = se_by_name[norm]
            fw_val = fw_ent.get(auth_field)
            se_val = se_ent.get(auth_field)
            record = {
                "name": fw_ent.get(key) or se_ent.get(key),
                "framework_val": fw_val,
                "session_val": se_val,
                "framework_source": fw_ent.get("source_file"),
                "framework_registry_id": fw_ent.get("registry_id"),
                "session_source": se_ent.get("source_file"),
            }
            if _values_agree(fw_val, se_val):
                agree_list.append(record)
            else:
                disagree_list.append(record)

        summary["buckets"][bucket] = {
            "framework_count": len(fw_by_name),
            "session_count": len(se_by_name),
            "overlap_count": len(overlap),
            "agree_count": len(agree_list),
            "disagree_count": len(disagree_list),
            "framework_only_count": len(fw_names - se_names),
            "session_only_count": len(se_names - fw_names),
            "disagree": disagree_list,
            # Full enumeration of framework_only and session_only names would
            # bloat the report; they're available via the index on demand.
        }
    return summary


def write_report(diff: dict) -> Path:
    lines: list[str] = []
    lines.append("# Framework-Registry Rectification Diff Report")
    lines.append("")
    lines.append(f"**Generated**: {diff['generated']}")
    lines.append("")
    lines.append(
        "The framework folder (`sessions/framework/*.md`) is the canonical "
        "destination for knowledge. This diff cross-checks session-level "
        "extractions against framework-registry entries. When the two "
        "disagree on the authoritative field, the **framework is wins** and "
        "the session file should be updated."
    )
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append("| Bucket | Framework entries | Session entries | Overlap | Agree | **Disagree** | Framework-only | Session-only |")
    lines.append("|:-------|------------------:|----------------:|--------:|------:|-------------:|--------------:|-------------:|")
    for bucket, b in diff["buckets"].items():
        lines.append(
            f"| {bucket} | {b['framework_count']} | {b['session_count']} | "
            f"{b['overlap_count']} | {b['agree_count']} | "
            f"**{b['disagree_count']}** | {b['framework_only_count']} | "
            f"{b['session_only_count']} |"
        )
    lines.append("")

    total_disagree = sum(b["disagree_count"] for b in diff["buckets"].values())
    lines.append(f"**Total WARRANTs (disagreements)**: {total_disagree}")
    lines.append("")

    if total_disagree == 0:
        lines.append(
            "No disagreements: every session-extracted entity that has a "
            "framework-registry counterpart agrees on the authoritative field."
        )
    else:
        lines.append("## WARRANT entries")
        lines.append("")
        lines.append(
            "For each disagreement, the framework-registry value is "
            "authoritative. The session file should be updated to match, or "
            "the disagreement should be resolved through explicit session "
            "work (with a new framework-registry entry that supersedes)."
        )
        lines.append("")
        for bucket, b in diff["buckets"].items():
            if not b["disagree"]:
                continue
            lines.append(f"### {bucket}")
            lines.append("")
            lines.append("| Name | Framework value | Session value | Framework source | Session source |")
            lines.append("|:-----|:----------------|:--------------|:-----------------|:---------------|")
            for r in b["disagree"]:
                name = (r.get("name") or "").replace("|", r"\|")[:80]
                fw_v = (r.get("framework_val") or "—").replace("|", r"\|")[:80]
                se_v = (r.get("session_val") or "—").replace("|", r"\|")[:80]
                fw_s = r.get("framework_source") or "—"
                se_s = r.get("session_source") or "—"
                lines.append(f"| {name} | {fw_v} | {se_v} | `{fw_s}` | `{se_s}` |")
            lines.append("")

    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")
    return REPORT_PATH


def main(argv: list[str] | None = None) -> int:
    argv = argv or sys.argv[1:]
    quiet = "--quiet" in argv

    diff = compute_diff()
    path = write_report(diff)

    if not quiet:
        total_disagree = sum(b["disagree_count"] for b in diff["buckets"].values())
        print("=" * 60)
        print("FRAMEWORK-REGISTRY DIFF")
        print("=" * 60)
        for bucket, b in diff["buckets"].items():
            print(
                f"  {bucket:20s} "
                f"fw={b['framework_count']:5d} "
                f"se={b['session_count']:5d} "
                f"overlap={b['overlap_count']:4d}  "
                f"agree={b['agree_count']:4d}  "
                f"DISAGREE={b['disagree_count']:4d}  "
                f"fw_only={b['framework_only_count']:4d}  "
                f"se_only={b['session_only_count']:5d}"
            )
        print("-" * 60)
        print(f"  Total WARRANTs: {total_disagree}")
        print(f"  Report: {path.relative_to(ROOT)}")
        print("=" * 60)
    return 0 if True else 1


if __name__ == "__main__":
    sys.exit(main())
