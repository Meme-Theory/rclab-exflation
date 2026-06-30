#!/usr/bin/env python
"""tools/export_routing_manifest.py — emit routing_manifest.json

Sister of `extract_entities.py` / `viz/console/build_data.py`: hydrates
entities + regex patterns + edge graph from `tools/knowledge.db` and
`computations/_shared/canonical_constants.py` into a single JSON manifest
that the meme-engine-web Astro rewriter consumes for build-time
cross-link resolution.

The contract is one-way: this script produces the manifest; the Astro
integration in `../meme-engine-web/` reads it. Regex patterns are
imported from the existing extractors (NOT re-derived) so the rewriter
and the entity extractor stay in lockstep — when the loose-gate-ID
pattern's `{1,5}` segment bound changes here, the manifest changes,
the rewriter recompiles, and link behavior updates everywhere at once.

Usage:
    "phonon-exflation-sim/.venv312/Scripts/python.exe" \\
        tools/export_routing_manifest.py
    "phonon-exflation-sim/.venv312/Scripts/python.exe" \\
        tools/export_routing_manifest.py --check
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

# Project paths (resolved from this file's location).
THIS_FILE = Path(__file__).resolve()
TOOLS_DIR = THIS_FILE.parent
PROJECT_ROOT = TOOLS_DIR.parent
COMPUTATIONS_DIR = PROJECT_ROOT / "computations"
SHARED_DIR = COMPUTATIONS_DIR / "_shared"  # canonical_constants + helpers post-Phase-3
KNOWLEDGE_DB = TOOLS_DIR / "knowledge.db"
CC_PATH = SHARED_DIR / "canonical_constants.py"
OUTPUT_PATH = TOOLS_DIR / "routing_manifest.json"

MANIFEST_VERSION = "1"

# Insert sibling dirs onto sys.path BEFORE the extractor imports so
# extract_entities can resolve `canonical_constants` and own helpers.
# `tools/archive/` carries the legacy per-edge-class harvesters whose
# regex symbols (RE_GATE_ID, RE_LOOSE_GATE_ID, _CONSTANT_NAME_STRICT,
# VERDICT_VOCAB, load_canonical_names) this script still imports — the
# consolidated `tools/harvester.py` wraps them inside subcommand handlers
# so they are NOT importable from module level.
sys.path.insert(0, str(SHARED_DIR))
sys.path.insert(0, str(COMPUTATIONS_DIR))
sys.path.insert(0, str(TOOLS_DIR))
sys.path.insert(0, str(TOOLS_DIR / "archive"))

from extract_entities import (  # noqa: E402  — import after path setup
    RE_GATE_ID as RE_GATE_ID_LEGACY,
    RE_VERDICT_LINE,
    RE_S81_VERDICT,
    RE_S81_VALUE,
    RE_S81_SCHEME,
    RE_S81_CONVENTION,
    RE_S81_LMAX,
    RE_S81_SHA,
    RE_SESSION_REF,
    RE_COMPUTATIONS_FILE,
    RE_RESEARCHER_DIR_REF,
    RE_EDGE_BLOCK,
    EDGE_TYPE_CANONICAL,
    ENTITY_TYPE_ALIASES,
)
from harvest_archive_edges import (  # noqa: E402
    RE_GATE_ID,
    RE_LOOSE_GATE_ID,
    _CONSTANT_NAME_STRICT,
    VERDICT_VOCAB,
    load_canonical_names,
)


# ─────────────────────────────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────────────────────────────

def _sha256_file(path: Path) -> str:
    if not path.exists():
        return ""
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


_SLUG_RE = re.compile(r"[^a-z0-9]+")


def _slug(s: str) -> str:
    return _SLUG_RE.sub("-", s.lower()).strip("-")


# Per-session primary-doc heuristic. Precedence ordered: canonical session-
# final first, then current-tree results-workingpaper / master synthesis,
# then archive-tree variants, then legacy snake_case, then bare-`session.md`
# (S01-style). First hit wins. Each entry is a (path_template, route_template)
# pair with a single `{n}` placeholder for the session id (digits + optional
# sub-letter, e.g. `73a`).
_SESSION_PRIMARY_DOC_CANDIDATES: list[tuple[str, str]] = [
    ("summary/session-{n}-final.md",                                     "/docs/summary/session-{n}-final"),
    ("sessions/session-{n}/session-{n}-results-workingpaper.md",         "/docs/sessions/{n}/session-{n}-results-workingpaper"),
    ("sessions/session-{n}/session-{n}-master-synthesis.md",             "/docs/sessions/{n}/session-{n}-master-synthesis"),
    ("sessions/session-{n}/session-{n}-master-collab.md",                "/docs/sessions/{n}/session-{n}-master-collab"),
    ("sessions/session-{n}/session-{n}-graceful-handoff.md",             "/docs/sessions/{n}/session-{n}-graceful-handoff"),
    ("sessions/archive/session-{n}/session-{n}-results-workingpaper.md", "/docs/sessions/{n}/session-{n}-results-workingpaper"),
    ("sessions/archive/session-{n}/session-{n}-master-synthesis.md",     "/docs/sessions/{n}/session-{n}-master-synthesis"),
    ("sessions/archive/session-{n}/session-{n}-master-collab.md",        "/docs/sessions/{n}/session-{n}-master-collab"),
    ("sessions/archive/session-{n}/session-{n}-graceful-handoff.md",     "/docs/sessions/{n}/session-{n}-graceful-handoff"),
    ("sessions/archive/session-{n}/s{n}_master.md",                      "/docs/sessions/{n}/s{n}_master"),
    ("sessions/archive/session-{n}/session.md",                          "/docs/sessions/{n}/session"),
]


def _session_primary_doc_index(session_ids: list[str]) -> dict[str, str]:
    """For each session id (e.g. "10", "17b", "73a", "87"), resolve the
    most authoritative document on disk and return a dict mapping
    session_id → repo-route. Sessions without any matching candidate
    (e.g. S87 mid-session before any finalized doc lands) are absent.
    """
    out: dict[str, str] = {}
    for sid in session_ids:
        if not sid:
            continue
        for path_tmpl, route_tmpl in _SESSION_PRIMARY_DOC_CANDIDATES:
            candidate = PROJECT_ROOT / path_tmpl.format(n=sid)
            if candidate.exists():
                out[sid] = route_tmpl.format(n=sid)
                break
    return out


def _source_file_to_route(source_file: str | None) -> str | None:
    """Map a repo-relative source path to the Astro doc route.

    Conventions match the directory layout proposed in the design discussion:
      sessions/{archive/}session-NN[a-z]?/<file>.md → /docs/sessions/<NN>[a-z]?/<file>
      sessions/framework/<...>/<file>.md            → /docs/framework/<...>/<file>
      summary/<file>.md                             → /docs/summary/<file>
      .claude/rules/<file>.md                       → /docs/rules/<file>
      researchers/<dom>/<file>.md                   → /docs/researchers/<dom>/<file>
      computations/_shared/<file>.md                   → /docs/computation/<file>
      permanent-results-registry.md                 → /docs/registry/permanent-results
    """
    if not source_file:
        return None
    p = source_file.replace("\\", "/").removeprefix("./")

    if p == "permanent-results-registry.md":
        return "/docs/registry/permanent-results"

    patterns = [
        (r"sessions/archive/session-(\d+[a-z]?)/(.+)\.md$", r"/docs/sessions/\1/\2"),
        (r"sessions/framework/(.+)\.md$",                   r"/docs/framework/\1"),
        (r"sessions/session-plan/(.+)\.md$",                r"/docs/sessions/plan/\1"),
        (r"sessions/session-(\d+[a-z]?)/(.+)\.md$",         r"/docs/sessions/\1/\2"),
        (r"summary/(.+)\.md$",                              r"/docs/summary/\1"),
        (r"\.claude/rules/(.+)\.md$",                       r"/docs/rules/\1"),
        (r"researchers/([^/]+)/(.+)\.md$",                  r"/docs/researchers/\1/\2"),
        (r"computations/_shared/(.+)\.md$",                    r"/docs/computation/\1"),
    ]
    for pat, repl in patterns:
        m = re.match(pat, p)
        if m:
            return re.sub(pat, repl, p)
    return None


# ID-shape filter mirrors viz/console/build_data.py:380 verbatim so
# the manifest's gate set matches the existing console's gate set.
GATE_ID_SHAPE_SQL = (
    "id GLOB '*-*' AND length(id) >= 3 AND id NOT GLOB '* *' "
    "AND id GLOB '*[A-Z]*' "
    "AND id NOT LIKE 'PASS%' AND id NOT LIKE 'FAIL%' AND id NOT LIKE 'INFO%'"
)


# ─────────────────────────────────────────────────────────────────────
# Entity exporters
# ─────────────────────────────────────────────────────────────────────

def export_constants() -> dict:
    """Read canonical_constants.py — names, values, PROVENANCE — and build
    the constant resolution table. Two-stage filter (regex shape AND
    `load_canonical_names` allowlist) matches the harvester's convention,
    keeping `np`, `sys`, etc. out of the constant vocabulary.
    """
    import canonical_constants as CC  # noqa: WPS433

    names = load_canonical_names()
    provenance = getattr(CC, "PROVENANCE", {})

    out: dict[str, dict] = {}
    for name in sorted(names):
        try:
            val = getattr(CC, name)
        except AttributeError:
            continue
        if isinstance(val, (int, float, str, bool)):
            value_repr: object = val
        else:
            try:
                value_repr = repr(val)
            except Exception:
                value_repr = None
        prov = provenance.get(name) or {}
        out[name] = {
            "value": value_repr,
            "session": prov.get("session"),
            "source": prov.get("source"),
            "gate": prov.get("gate"),
            "superseded": bool(prov.get("superseded", False)),
            "note": prov.get("note"),
            "r_protected": bool(prov.get("R_protected", False)),
            "route": f"/docs/constants/{name}",
        }
    return out


def export_gates(cur: sqlite3.Cursor, session_doc_index: dict[str, str]) -> dict:
    """Gates are NOT standalone documents — they are verdict-rows in
    session synthesis files. The bare `route = /docs/gates/<id>` would
    404 in Astro because no markdown backs it. So we ALSO emit:

      session_route → the session page that contains this gate (or None
                      if the session has no primary doc on disk yet)
      link_target   → the rewriter's recommended href: a deep-link into
                      the session page if available, else the bare route
                      (which the rewriter can choose to skip)
    """
    rows = cur.execute(
        f"""
        SELECT id, name, session, condition, result, verdict,
               bayes_factor, data_files
        FROM gates
        WHERE {GATE_ID_SHAPE_SQL}
        """
    ).fetchall()
    out: dict[str, dict] = {}
    for gid, name, session, condition, result, verdict, bf, data_files in rows:
        if not gid:
            continue
        sess = (session or "").strip()
        session_route = session_doc_index.get(sess) if sess else None
        bare_route = f"/docs/gates/{gid}"
        link_target = (
            f"{session_route}#{_slug(gid)}" if session_route else bare_route
        )
        out[gid] = {
            "id": gid,
            "name": name or "",
            "session": session or "",
            "verdict": verdict or "",
            "condition": (condition or "")[:300],
            "result": (result or "")[:300],
            "bayes_factor": bf,
            "data_files": data_files,
            "route": bare_route,
            "session_route": session_route,
            "link_target": link_target,
        }
    return out


def export_theorems(cur: sqlite3.Cursor) -> dict:
    # Length filter mirrors viz/console/build_data.py:268 — drops
    # column-shifted extraction errors (e.g., proven_1's "S44" statement
    # surfaced in the v1 spot-check).
    rows = cur.execute(
        """
        SELECT id, name, status, sessions, precision, statement, source_file
        FROM theorems
        WHERE sessions IS NOT NULL AND sessions != ''
          AND statement IS NOT NULL
          AND length(statement) BETWEEN 20 AND 260
        """
    ).fetchall()
    out: dict[str, dict] = {}
    for tid, name, status, sessions, precision, statement, source_file in rows:
        if not tid:
            continue
        out[tid] = {
            "id": tid,
            "name": name or "",
            "status": status or "",
            "sessions": sessions or "",
            "precision": precision or "",
            "statement": (statement or "")[:400],
            "source_file": source_file,
            "source_doc_route": _source_file_to_route(source_file),
            "route": f"/docs/theorems/{tid}",
        }
    return out


def export_mechanisms(cur: sqlite3.Cursor) -> dict:
    rows = cur.execute(
        "SELECT id, name, closed_by, session, gate_id, source_file "
        "FROM closed_mechanisms"
    ).fetchall()
    out: dict[str, dict] = {}
    for mid, name, closed_by, session, gate_id, source_file in rows:
        if not mid:
            continue
        out[mid] = {
            "id": mid,
            "name": name or "",
            "closed_by": closed_by or "",
            "session": session or "",
            "gate_id": gate_id or "",
            "source_file": source_file,
            "source_doc_route": _source_file_to_route(source_file),
            "route": f"/docs/mechanisms/{mid}",
        }
    return out


def export_open_channels(cur: sqlite3.Cursor) -> list:
    rows = cur.execute(
        "SELECT name, detail_1, detail_2, session, source_file FROM open_channels"
    ).fetchall()
    out: list[dict] = []
    seen: set[str] = set()
    for name, d1, d2, session, source_file in rows:
        if not name:
            continue
        slug = _slug(name)
        if not slug:
            continue
        # open_channels has no PK — disambiguate slug collisions.
        base = slug
        i = 2
        while slug in seen:
            slug = f"{base}-{i}"
            i += 1
        seen.add(slug)
        out.append({
            "slug": slug,
            "name": name,
            "detail_1": (d1 or "")[:200],
            "detail_2": (d2 or "")[:200],
            "session": session or "",
            "source_file": source_file,
            "source_doc_route": _source_file_to_route(source_file),
            "route": f"/docs/open/{slug}",
        })
    return out


def export_sessions(cur: sqlite3.Cursor) -> dict:
    rows = cur.execute(
        "SELECT id, date, type, agents, prior, posterior, verdict, files "
        "FROM sessions"
    ).fetchall()
    out: dict[str, dict] = {}
    for sid, date, type_, agents, prior, posterior, verdict, files in rows:
        if not sid:
            continue
        out[sid] = {
            "id": sid,
            "date": date or "",
            "type": type_ or "",
            "agents": agents or "",
            "prior": prior,
            "posterior": posterior,
            "verdict": verdict or "",
            "files": files or "",
            "route": f"/docs/sessions/{sid}",
        }
    return out


def export_researchers(cur: sqlite3.Cursor) -> dict:
    rows = cur.execute(
        "SELECT domain, paper_count, citation_count, description, path "
        "FROM researchers"
    ).fetchall()
    out: dict[str, dict] = {}
    for domain, papers, cites, desc, path in rows:
        if not domain:
            continue
        out[domain] = {
            "domain": domain,
            "paper_count": papers or 0,
            "citation_count": cites or 0,
            "description": (desc or "")[:300],
            "path": path,
            "route": f"/docs/researchers/{domain}",
        }
    return out


def export_edges(cur: sqlite3.Cursor) -> list:
    # Placeholder-ID filter: drop edge rows whose source_id or target_id
    # contain `<` or `>` (template artifacts like `<script>.py`, `<NAME>`
    # surfaced in v1 spot-check). SQL filter is faster than post-fetch.
    rows = cur.execute(
        "SELECT type, source_type, source_id, target_type, target_id, comment "
        "FROM edges "
        "WHERE source_id NOT GLOB '*<*' AND source_id NOT GLOB '*>*' "
        "  AND target_id NOT GLOB '*<*' AND target_id NOT GLOB '*>*'"
    ).fetchall()
    return [
        {
            "type": t,
            "source_type": st, "source_id": si,
            "target_type": tt, "target_id": ti,
            "comment": (c or "")[:140],
        }
        for (t, st, si, tt, ti, c) in rows
    ]


# ─────────────────────────────────────────────────────────────────────
# Pattern + vocab exporter — the rewriter binds to these strings
# ─────────────────────────────────────────────────────────────────────

def export_patterns() -> dict:
    """Embed regex patterns the Astro rewriter must use.

    These are .pattern strings from extract_entities.py +
    harvest_archive_edges.py. Importing them (rather than copy-pasting)
    is what guarantees the rewriter and the Python entity extractor
    operate on the same regex set across version bumps.
    """
    return {
        "_doc": (
            "Regex patterns from tools/extract_entities.py and "
            "tools/harvest_archive_edges.py. The Astro rewriter MUST use "
            "these (not re-derive) to keep the extractor and the rewriter "
            "in lockstep."
        ),
        "gate_id_strict_anchored":  RE_GATE_ID.pattern,
        "gate_id_loose_in_prose":   RE_LOOSE_GATE_ID.pattern,
        "gate_id_legacy":           RE_GATE_ID_LEGACY.pattern,
        "constant_name_strict":     _CONSTANT_NAME_STRICT.pattern,
        "session_ref":              RE_SESSION_REF.pattern,
        "computation_file_ref":           RE_COMPUTATIONS_FILE.pattern,
        "researcher_dir_ref":       RE_RESEARCHER_DIR_REF.pattern,
        "edge_block_explicit":      RE_EDGE_BLOCK.pattern,
        "verdict_line_canonical":   RE_VERDICT_LINE.pattern,
        "verdict_line_s81":         RE_S81_VERDICT.pattern,
        "verdict_field_value":      RE_S81_VALUE.pattern,
        "verdict_field_scheme":     RE_S81_SCHEME.pattern,
        "verdict_field_convention": RE_S81_CONVENTION.pattern,
        "verdict_field_l_max":      RE_S81_LMAX.pattern,
        "verdict_field_sha":        RE_S81_SHA.pattern,
    }


def export_vocab() -> dict:
    return {
        "_doc": (
            "Closed vocabularies. The rewriter uses these to disambiguate "
            "loose pattern matches (e.g., a token matching the loose "
            "gate-ID shape that is actually a verdict word should not "
            "be linked)."
        ),
        "verdict_terms":       sorted(VERDICT_VOCAB),
        "edge_type_canonical": EDGE_TYPE_CANONICAL,
        "entity_type_aliases": ENTITY_TYPE_ALIASES,
    }


# ─────────────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────────────

def build_manifest() -> dict:
    if not KNOWLEDGE_DB.exists():
        raise SystemExit(
            f"knowledge.db not found at {KNOWLEDGE_DB}. "
            f"Run `/weave --update && /weave --db-sync` first."
        )

    conn = sqlite3.connect(str(KNOWLEDGE_DB))
    cur = conn.cursor()
    try:
        # Build the session-doc index FIRST: gates depend on it for
        # link_target resolution. Index is filesystem-backed so it
        # reflects S87-style "results-workingpaper exists, no -final
        # yet" mid-session states accurately.
        sessions_raw = export_sessions(cur)
        session_doc_index = _session_primary_doc_index(list(sessions_raw.keys()))

        manifest = {
            "version": MANIFEST_VERSION,
            "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "source_db_sha256":        _sha256_file(KNOWLEDGE_DB),
            "source_constants_sha256": _sha256_file(CC_PATH),
            "constants":     export_constants(),
            "gates":         export_gates(cur, session_doc_index),
            "theorems":      export_theorems(cur),
            "mechanisms":    export_mechanisms(cur),
            "open_channels": export_open_channels(cur),
            "sessions":      sessions_raw,
            "researchers":   export_researchers(cur),
            "edges":         export_edges(cur),
            "patterns":      export_patterns(),
            "vocab":         export_vocab(),
        }
    finally:
        conn.close()

    return manifest


def _validate(manifest: dict) -> list[str]:
    """Minimum-count and structural integrity checks. The thresholds
    pin the contract: a regression in the upstream extractor that
    silently zeroes a table fails this check loudly.
    """
    errors: list[str] = []
    expected_min = {
        "constants":   100,   # canonical_constants.py has ~194 public scalars
        "gates":        50,
        "theorems":     30,
        "sessions":     50,
    }
    for key, min_count in expected_min.items():
        n = len(manifest[key])
        if n < min_count:
            errors.append(f"{key}: {n} rows (expected >= {min_count})")

    null_constants = [
        n for n, v in manifest["constants"].items()
        if v.get("value") is None and v.get("source") is None
    ]
    if null_constants:
        errors.append(
            f"{len(null_constants)} constants are fully unresolved "
            f"(no value, no provenance): {null_constants[:5]}"
        )

    for k, v in manifest["patterns"].items():
        if k == "_doc":
            continue
        if not isinstance(v, str) or not v:
            errors.append(f"patterns.{k}: empty or non-string")

    if len(manifest["edges"]) < 30:
        errors.append(f"edges: {len(manifest['edges'])} (expected >= 30)")

    # Quality assertions — should be zero by construction after the v2
    # filter fixes. Surfacing a non-zero count means the upstream
    # extractor regressed and the export filter no longer catches the
    # shape; investigate before shipping the manifest.
    placeholder_edges = [
        e for e in manifest["edges"]
        if any(c in (e.get(f) or "") for f in ("source_id", "target_id") for c in "<>")
    ]
    if placeholder_edges:
        errors.append(
            f"{len(placeholder_edges)} placeholder-id edges leaked through "
            f"(sample: {placeholder_edges[0]})"
        )

    short_theorems = [
        tid for tid, t in manifest["theorems"].items()
        if len(t.get("statement") or "") < 20
    ]
    if short_theorems:
        errors.append(
            f"{len(short_theorems)} theorems have statement < 20 chars "
            f"(sample: {short_theorems[:5]})"
        )

    # Soft threshold: many legacy gates have empty session in the DB.
    # Above 5% suggests a recent extractor regression; below is the
    # historical baseline.
    n_gates = len(manifest["gates"])
    gates_no_session = [
        gid for gid, g in manifest["gates"].items()
        if not (g.get("session") or "").strip()
    ]
    if n_gates and len(gates_no_session) > 0.05 * n_gates:
        pct = len(gates_no_session) * 100 // n_gates
        errors.append(
            f"{len(gates_no_session)} of {n_gates} gates ({pct}%) have empty "
            f"session — exceeds 5% threshold; sample: {gates_no_session[:5]}"
        )

    return errors


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Export tools/routing_manifest.json for the Astro rewriter."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Build the manifest and run validation; exit non-zero on errors.",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=OUTPUT_PATH,
        help=f"Output path (default: {OUTPUT_PATH.relative_to(PROJECT_ROOT)})",
    )
    args = parser.parse_args()

    manifest = build_manifest()
    payload = json.dumps(manifest, indent=2, sort_keys=False, ensure_ascii=False)
    args.out.write_text(payload, encoding="utf-8")

    size_kb = args.out.stat().st_size // 1024
    print(f"Wrote {args.out.relative_to(PROJECT_ROOT)} ({size_kb} KB)")
    print(f"  constants:    {len(manifest['constants'])}")
    print(f"  gates:        {len(manifest['gates'])}")
    print(f"  theorems:     {len(manifest['theorems'])}")
    print(f"  mechanisms:   {len(manifest['mechanisms'])}")
    print(f"  open chans:   {len(manifest['open_channels'])}")
    print(f"  sessions:     {len(manifest['sessions'])}")
    print(f"  researchers:  {len(manifest['researchers'])}")
    print(f"  edges:        {len(manifest['edges'])}")
    print(f"  patterns:     {len(manifest['patterns']) - 1}")  # minus _doc
    print(f"  db sha256:    {manifest['source_db_sha256'][:16]}...")
    print(f"  cc sha256:    {manifest['source_constants_sha256'][:16]}...")

    if args.check:
        errors = _validate(manifest)
        if errors:
            print("\n=== VALIDATION ERRORS ===", file=sys.stderr)
            for e in errors:
                print(f"  - {e}", file=sys.stderr)
            sys.exit(1)
        print("Validation: PASS")


if __name__ == "__main__":
    main()
