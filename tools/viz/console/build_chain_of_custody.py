#!/usr/bin/env python3
"""
Chain-of-custody sidecar builder (Phase 2 of the meme-engine-web Genealogy
re-spec).

Consumes:
  - tools/knowledge.db::edges  (31,700 typed edges; 4 lens classes)
  - tools/knowledge.db::nodes  (constants, theorems, gates, mechanisms, sessions, researchers)

Produces:
  - tools/viz/console/chain_of_custody.json

What it pre-computes:
  For each "anchor entity" (a node the Genealogy view lets the user click on),
  pre-compute bidirectional BFS chains via the typed edges:
    - upstream:   walk by reversing edges (what FEEDS the anchor?)
    - downstream: walk by following edges (what does the anchor FEED?)
  Bounded at depth=4 and top_K=20 per level — the standard "red string on the
  wall" radius beyond which the chain stops being informative.

Each edge in the chain is tagged with one of four LENS classes so the
frontend can re-color / hide subgraphs by lens at render time:

  authorship  - authored_by, co_authored_by, reviewed_by, participates_in,
                authored_round, synthesized_by, excluded_from
  citation    - cited_in, discussed_in, cites_prior_session
  custody     - carries_forward, anchored_in, succ_of
  logical     - depends_on, derived_from, reproduces, closed_by, refutes,
                confirms, bounds, supersedes, superseded_by, implies,
                feeds_into, grounds, refines, enables, validates,
                cross_validates, contradicts

Anchor selection (quality-filtered to keep the sidecar < 30 MB):

  - constants:     all in canonical_constants with PROVENANCE
  - theorems:      proven_N rows with statement length 20-400
  - gates:         non-empty session, verdict in {PASS, FAIL, INFO,
                   PASSED, FAILED, CLOSED, PROVEN}
  - mechanisms:    all closed_mechanisms
  - sessions:      all sessions (109)
  - researchers:   all researchers (39)

Output format:
  {
    "generated_from": "...",
    "summary": {...counts...},
    "lens_definitions": {...},
    "anchors": {
      "<type>:<id>": {
        "anchor":     {"type":..., "id":..., "title":..., "...":...},
        "upstream":   {"1":[...], "2":[...], "3":[...], "4":[...]},
        "downstream": {"1":[...], "2":[...], "3":[...], "4":[...]},
        "stats":      {"total_upstream":N, "total_downstream":M,
                       "truncated_at_depth":d (null if not truncated)}
      }
    }
  }

Each chain entry is:
  {"type":..., "id":..., "via":"<edge_type>", "lens":"<lens_name>",
   "title":"<short label>"}

The frontend reads the anchor's chain and renders by lens or by depth.

Run:
    "phonon-exflation-sim/.venv312/Scripts/python.exe" \\
        tools/viz/console/build_chain_of_custody.py
"""
from __future__ import annotations

import json
import re
import sqlite3
import sys
from collections import defaultdict, deque
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent             # tools/viz/console
ROOT = HERE.parent.parent.parent                     # project root
DB_PATH = ROOT / "tools" / "knowledge.db"
OUT_PATH = HERE / "chain_of_custody.json"


# ---------------------------------------------------------------------------
# Tunables (single-source-of-truth)
# ---------------------------------------------------------------------------

DEPTH = 4
# 200 covers ~99.9% of nodes uncapped (depth-1 fanout p99.9 = 290 at S87).
# The Genealogy view scrolls per-column, so the cap is just a safety budget
# against the handful of mega-hubs that would otherwise blow the payload.
TOP_K_PER_LEVEL = 200

# Theorem-quality filter (mirrors build_theorem_genealogy.py:262-265)
THEOREM_STATEMENT_MIN = 20
THEOREM_STATEMENT_MAX = 400

# Gate verdict whitelist (only anchor gates with a real outcome)
GATE_VERDICT_WHITELIST = {
    "PASS", "FAIL", "INFO", "PASSED", "FAILED", "CLOSED", "PROVEN",
    "CONFIRMED", "RESOLVED",
}


# ---------------------------------------------------------------------------
# Lens partition (matches EDGE_TYPE_CANONICAL semantic groupings)
# ---------------------------------------------------------------------------

LENS_AUTHORSHIP = {
    "authored_by",
    "co_authored_by",
    "reviewed_by",
    "participates_in",
    "authored_round",
    "synthesized_by",
    "excluded_from",
}
LENS_CITATION = {
    "cited_in",
    "discussed_in",
    "cites_prior_session",
}
LENS_CUSTODY = {
    "carries_forward",
    "anchored_in",
    "succ_of",
}
LENS_LOGICAL = {
    "depends_on",
    "derived_from",
    "reproduces",
    "closed_by",
    "refutes",
    "refuted_by",
    "confirms",
    "bounds",
    "supersedes",
    "superseded_by",
    "implies",
    "feeds_into",
    "consumes",
    "grounds",
    "refines",
    "enables",
    "validates",
    "cross_validates",
    "contradicts",
}

EDGE_TYPE_TO_LENS: dict[str, str] = {}
for et in LENS_AUTHORSHIP:
    EDGE_TYPE_TO_LENS[et] = "authorship"
for et in LENS_CITATION:
    EDGE_TYPE_TO_LENS[et] = "citation"
for et in LENS_CUSTODY:
    EDGE_TYPE_TO_LENS[et] = "custody"
for et in LENS_LOGICAL:
    EDGE_TYPE_TO_LENS[et] = "logical"


def lens_of(edge_type: str) -> str:
    return EDGE_TYPE_TO_LENS.get(edge_type, "logical")


# ---------------------------------------------------------------------------
# Predecessor-position semantics (fixes the directional-asymmetry bug)
# ---------------------------------------------------------------------------
#
# Edge harvesters emit edges in two mixed conventions:
#   (a) chronological / production: source is earlier, target is later.
#       Example: `carries_forward sessions -> gates` (session spawns future gate).
#   (b) dependency / provenance:    source is later, target is earlier.
#       Example: `anchored_in gates -> sessions` (gate anchored to earlier session).
#
# For a chain-of-custody view, "upstream of X" must consistently mean
# *predecessor of X* (what came before / what X depends on) regardless of which
# direction convention the edge uses. So per edge type, we record where the
# predecessor sits:
#
#   "source": the SOURCE end of the edge is the predecessor (chronological)
#   "target": the TARGET end of the edge is the predecessor (dependency)
#   "both":   symmetric edge (no predecessor / coeval)
#
# `get_incident_edges()` (below) reads this map and routes each edge incident
# to a node into the correct upstream-or-downstream bucket.
#
# Coverage: all 26 edge types currently in the DB, plus 6 future-proof types
# from LENS_LOGICAL that the harvesters do not yet emit.

PREDECESSOR_POSITION: dict[str, str] = {
    # -- Custody lens ------------------------------------------------------
    "carries_forward":     "source",  # session -> future gate
    "anchored_in":         "target",  # later gate -> earlier session
    "succ_of":             "target",  # gate G_later -> gate G_earlier

    # -- Citation lens -----------------------------------------------------
    "cited_in":            "source",  # researcher (earlier work) -> session citing them
    "discussed_in":        "source",  # researcher -> session
    "cites_prior_session": "target",  # gate -> earlier session

    # -- Authorship lens ---------------------------------------------------
    # Pattern: "X authored_by R" means R precedes X (R created X)
    "authored_by":         "target",  # gate/data/session -> researcher
    "co_authored_by":      "target",  # gate -> researcher
    "reviewed_by":         "target",  # gate/data -> researcher
    "synthesized_by":      "target",  # gate -> session (session is synthesis context)
    "participates_in":     "source",  # researcher -> data (researcher precedes data event)
    "authored_round":      "source",  # researcher -> data round
    "excluded_from":       "target",  # gate -> researcher

    # -- Logical lens ------------------------------------------------------
    "depends_on":          "target",  # X depends_on Y -> Y precedes
    "derived_from":        "target",  # X derived_from Y -> Y precedes
    "reproduces":          "target",  # gate reproduces earlier result
    "feeds_into":          "source",  # A feeds_into B -> A precedes
    "grounds":             "source",  # A grounds B -> A precedes
    "enables":             "source",  # A enables B -> A precedes
    "implies":             "source",  # A implies B -> A is premise (precedes)
    "bounds":              "source",  # theorem bounds constant -> theorem is the basis
    "confirms":            "target",  # gate confirms theorem -> theorem precedes
    "closed_by":           "source",  # open_channel closed_by gate -> channel is earlier open state
    "refutes":             "target",  # gate refutes session/theorem -> refuted thing precedes
    "supersedes":          "target",  # A supersedes B -> B is older

    # -- Future-proof (in LENS_LOGICAL but no edges in DB yet) ------------
    "consumes":            "target",
    "refines":             "target",
    "validates":           "target",
    "refuted_by":          "source",
    "superseded_by":       "source",
    "cross_validates":     "both",    # symmetric
    "contradicts":         "both",    # symmetric
}


def get_incident_edges(
    node: tuple[str, str],
    forward: dict[tuple[str, str], list[tuple[tuple[str, str], str]]],
    reverse: dict[tuple[str, str], list[tuple[tuple[str, str], str]]],
) -> list[tuple[tuple[str, str], str, str]]:
    """Return [(neighbor, edge_type, role)] for every edge incident to `node`.

    role in {"upstream", "downstream"} -- classifies the OTHER end of the edge
    relative to `node`, via PREDECESSOR_POSITION.

      - Outgoing edge (node is source):
          pos=="source" -> node is predecessor -> target is DOWNSTREAM
          pos=="target" -> target is predecessor -> target is UPSTREAM
      - Incoming edge (node is target):
          pos=="source" -> source is predecessor -> source is UPSTREAM
          pos=="target" -> node is predecessor -> source is DOWNSTREAM
      - "both" (symmetric edge): emit BOTH roles.

    Unknown edge types default to "target" (dependency convention).
    """
    out: list[tuple[tuple[str, str], str, str]] = []

    for (tgt, etype) in forward.get(node, []):
        pos = PREDECESSOR_POSITION.get(etype, "target")
        if pos == "source":
            out.append((tgt, etype, "downstream"))
        elif pos == "target":
            out.append((tgt, etype, "upstream"))
        else:  # "both"
            out.append((tgt, etype, "downstream"))
            out.append((tgt, etype, "upstream"))

    for (src, etype) in reverse.get(node, []):
        pos = PREDECESSOR_POSITION.get(etype, "target")
        if pos == "source":
            out.append((src, etype, "upstream"))
        elif pos == "target":
            out.append((src, etype, "downstream"))
        else:  # "both"
            out.append((src, etype, "downstream"))
            out.append((src, etype, "upstream"))

    return out


# ---------------------------------------------------------------------------
# Anchor selection
# ---------------------------------------------------------------------------

def select_anchors(con: sqlite3.Connection) -> dict[tuple[str, str], dict]:
    """Return {(node_type, node_id): {title:..., extra:{}}} for all anchor
    entities. Title is a short human-readable label used in chain entries."""
    out: dict[tuple[str, str], dict] = {}

    # 1) Theorems (quality-filtered like build_theorem_genealogy.py)
    for tid, name, sessions, statement in con.execute("""
        SELECT id, name, sessions, statement FROM theorems
        WHERE statement IS NOT NULL
          AND length(statement) BETWEEN ? AND ?
    """, (THEOREM_STATEMENT_MIN, THEOREM_STATEMENT_MAX)):
        title = (name or tid or "").strip()[:120]
        out[("theorems", tid)] = {
            "title": title,
            "extra": {"sessions": sessions or ""},
        }

    # 2) Gates with real verdicts
    rows = con.execute("""
        SELECT id, condition, result, verdict, session
        FROM gates
        WHERE id IS NOT NULL AND id != ''
    """).fetchall()
    for gid, cond, result, verdict, session in rows:
        v = (verdict or "").strip().upper()
        # Accept any gate that has a verdict marker, even non-canonical ones
        # (so anchored_in edges from S81 batch still index)
        if not v and not result:
            continue
        if v and not any(w in v for w in GATE_VERDICT_WHITELIST):
            # Loose match: also accept verdicts that CONTAIN a whitelisted token
            if not any(w in (result or "").upper() for w in GATE_VERDICT_WHITELIST):
                continue
        title = (cond or gid or "").strip()[:120]
        out[("gates", gid)] = {
            "title": title,
            "extra": {"verdict": v, "session": session or ""},
        }

    # 3) Closed mechanisms (schema: id, name, closed_by, session, gate_id, source_file)
    for mid, name, session, closed_by in con.execute("""
        SELECT id, name, session, closed_by FROM closed_mechanisms
    """):
        title = (name or mid or "").strip()[:120]
        out[("closed_mechanisms", mid)] = {
            "title": title,
            "extra": {"session": session or "", "closed_by": closed_by or ""},
        }

    # 4) Sessions (schema: id, date, type, agents, prior, posterior, verdict, files, source_file)
    for sid, sverdict, sdate in con.execute("SELECT id, verdict, date FROM sessions"):
        if not sid:
            continue
        title = f"S{sid}"
        if sverdict:
            title += f" — {sverdict[:80]}"
        elif sdate:
            title += f" ({sdate})"
        out[("sessions", sid)] = {"title": title[:120], "extra": {}}

    # 5) Researchers — select from researchers TABLE (S90+: was previously
    # synthesized from edges, missing the 10 researcher domains without
    # any incoming edges. Now uses the real table.)
    try:
        for domain, desc in con.execute(
            "SELECT domain, description FROM researchers WHERE domain IS NOT NULL"
        ):
            if not domain:
                continue
            title = (desc or domain).strip()[:120]
            out[("researchers", domain)] = {"title": title, "extra": {}}
    except sqlite3.OperationalError:
        # Fallback to edge-derived (pre-S90 DB without proper researchers table)
        for r, in con.execute("""
            SELECT DISTINCT source_id FROM edges WHERE source_type='researchers'
            UNION
            SELECT DISTINCT target_id FROM edges WHERE target_type='researchers'
        """):
            if r:
                out[("researchers", r)] = {"title": r, "extra": {}}

    # 6) Canonical constants — select from real constants TABLE (S90+:
    # was previously synthesized from edges only). All 379 public
    # canonical-constants names are anchors, even those without edges.
    try:
        for name, value, session in con.execute(
            "SELECT name, value, session FROM constants"
        ):
            if not name:
                continue
            title = name[:120]
            if value:
                title = f"{name} = {value[:60]}"
            out[("constants", name)] = {
                "title": title[:120],
                "extra": {"value": value or "", "session": session or ""},
            }
    except sqlite3.OperationalError:
        for c, in con.execute("""
            SELECT DISTINCT target_id FROM edges
            WHERE target_type='constants' AND target_id IS NOT NULL
        """):
            if c:
                out[("constants", c)] = {"title": c, "extra": {}}

    # 7) Agents (S90+ table) — distinct entity from researchers; each
    # agent is a configured persona with its own slug.
    try:
        for slug, name, persona, rdomain in con.execute(
            "SELECT slug, name, persona, researcher_domain FROM agents"
        ):
            if not slug:
                continue
            title = (persona or name or slug).strip()[:120]
            out[("agents", slug)] = {
                "title": title,
                "extra": {"researcher_domain": rdomain or ""},
            }
    except sqlite3.OperationalError:
        pass

    # 8) Open channels (real entities — uncomputed predictions). The
    # rowid PK isn't stable; use name as the anchor ID.
    for oc_name, detail, session in con.execute(
        "SELECT name, detail_1, session FROM open_channels "
        "WHERE name IS NOT NULL AND name != ''"
    ):
        title = (oc_name or "").strip()[:120]
        out[("open_channels", oc_name)] = {
            "title": title,
            "extra": {"detail": detail or "", "session": session or ""},
        }

    # 9) Session files (S90+ table) — markdown files within sessions/.
    try:
        for sf_id, filename, session in con.execute(
            "SELECT id, filename, session FROM session_files"
        ):
            if not sf_id:
                continue
            title = (filename or sf_id)[:120]
            out[("session_files", sf_id)] = {
                "title": title,
                "extra": {"session": session or ""},
            }
    except sqlite3.OperationalError:
        pass

    # 10) Data provenance (compute scripts). Use script path as anchor ID.
    for script, name, session in con.execute(
        "SELECT script, name, session FROM data_provenance "
        "WHERE script IS NOT NULL AND script != ''"
    ):
        title = (script or name or "").strip()[:120]
        out[("data_provenance", script)] = {
            "title": title,
            "extra": {"name": name or "", "session": session or ""},
        }

    return out


# ---------------------------------------------------------------------------
# Edge index — build forward + reverse adjacency lists once
# ---------------------------------------------------------------------------

def build_adjacency(con: sqlite3.Connection) -> tuple[
        dict[tuple[str, str], list[tuple[tuple[str, str], str]]],
        dict[tuple[str, str], list[tuple[tuple[str, str], str]]]]:
    """Return (forward, reverse) adjacency maps.

    forward[(src_type, src_id)] = [((tgt_type, tgt_id), edge_type), ...]
    reverse[(tgt_type, tgt_id)] = [((src_type, src_id), edge_type), ...]
    """
    forward: dict[tuple[str, str], list[tuple[tuple[str, str], str]]] = defaultdict(list)
    reverse: dict[tuple[str, str], list[tuple[tuple[str, str], str]]] = defaultdict(list)

    for src_type, src_id, tgt_type, tgt_id, etype in con.execute("""
        SELECT source_type, source_id, target_type, target_id, type FROM edges
        WHERE source_id != '' AND target_id != ''
    """):
        s = (src_type, src_id)
        t = (tgt_type, tgt_id)
        forward[s].append((t, etype))
        reverse[t].append((s, etype))

    return dict(forward), dict(reverse)


# ---------------------------------------------------------------------------
# Bounded BFS — bidirectional, top-K per level, lens-tagged
# ---------------------------------------------------------------------------

def bfs_directional(
    start: tuple[str, str],
    forward: dict[tuple[str, str], list[tuple[tuple[str, str], str]]],
    reverse: dict[tuple[str, str], list[tuple[tuple[str, str], str]]],
    title_lookup: dict[tuple[str, str], str],
    direction: str,
    depth: int = DEPTH,
    top_k: int = TOP_K_PER_LEVEL,
) -> tuple[dict[str, list[dict]], int, int | None]:
    """Bounded BFS from `start`, expanding along edges whose semantic role
    matches `direction` ("upstream" or "downstream").

    Per-edge role is determined by PREDECESSOR_POSITION via get_incident_edges,
    so the BFS walks BOTH forward and reverse adjacency lists and routes each
    edge into the correct directional bucket. This fixes the earlier bug
    where reverse adjacency was unconditionally mapped to "upstream", which
    flipped the meaning of chronologically-forward edges like `carries_forward`.

    Returns (levels, total_visited, truncated_at_depth) where:
      levels      = {"1": [...], "2": [...], "3": [...], "4": [...]}
      total       = number of unique nodes visited (excluding start)
      truncated   = depth at which we hit top_k limit (or None if never)
    """
    assert direction in ("upstream", "downstream"), direction
    visited: set[tuple[str, str]] = {start}
    levels: dict[str, list[dict]] = {str(d): [] for d in range(1, depth + 1)}
    frontier: list[tuple[str, str]] = [start]
    truncated_at: int | None = None

    for d in range(1, depth + 1):
        next_frontier: list[tuple[str, str]] = []
        # Collect candidate entries (deduped by neighbor)
        seen_neighbors_this_level: set[tuple[str, str]] = set()
        candidates: list[dict] = []
        for u in frontier:
            for (v, etype, role) in get_incident_edges(u, forward, reverse):
                if role != direction:
                    continue
                if v in visited:
                    continue
                if v in seen_neighbors_this_level:
                    continue
                seen_neighbors_this_level.add(v)
                title = title_lookup.get(v, "")
                candidates.append({
                    "type": v[0],
                    "id": v[1],
                    "via": etype,
                    "lens": lens_of(etype),
                    "title": title[:120],
                })
        # Sort by lens preference (logical first, then custody/citation/auth)
        # then alphabetical by id for stability.
        LENS_ORDER = {"logical": 0, "custody": 1, "citation": 2, "authorship": 3}
        candidates.sort(key=lambda c: (LENS_ORDER.get(c["lens"], 9), c["type"], c["id"]))

        if len(candidates) > top_k:
            if truncated_at is None:
                truncated_at = d
            candidates = candidates[:top_k]

        # Commit candidates to this level, mark visited, build next frontier
        for c in candidates:
            v = (c["type"], c["id"])
            visited.add(v)
            next_frontier.append(v)
        levels[str(d)] = candidates
        frontier = next_frontier
        if not frontier:
            break

    return levels, len(visited) - 1, truncated_at


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------

def main() -> int:
    if not DB_PATH.exists():
        print(f"[build_chain_of_custody] ERROR: {DB_PATH} not found. "
              f"Run `/weave --update` first.")
        return 1

    con = sqlite3.connect(str(DB_PATH))
    try:
        print("[build_chain_of_custody] selecting anchors...")
        anchors = select_anchors(con)
        print(f"  {len(anchors):,} anchors selected.")

        print("[build_chain_of_custody] building adjacency...")
        forward, reverse = build_adjacency(con)
        n_edges = sum(len(v) for v in forward.values())
        print(f"  {n_edges:,} edges indexed "
              f"({len(forward):,} src nodes / {len(reverse):,} tgt nodes).")

        # Title lookup: anchor titles + edge endpoints that aren't anchors
        title_lookup: dict[tuple[str, str], str] = {}
        for key, info in anchors.items():
            title_lookup[key] = info["title"]
        # Also pre-populate any constants / sessions seen in edges
        for nodes_map in (forward, reverse):
            for src, edges in nodes_map.items():
                if src not in title_lookup:
                    title_lookup[src] = src[1]
                for (tgt, _) in edges:
                    if tgt not in title_lookup:
                        title_lookup[tgt] = tgt[1]
    finally:
        con.close()

    print(f"[build_chain_of_custody] BFS at depth={DEPTH}, top_k={TOP_K_PER_LEVEL} per level...")

    anchor_output: dict[str, dict] = {}
    truncated_count = 0
    total_chain_nodes = 0
    by_anchor_type: dict[str, int] = defaultdict(int)

    for key, info in anchors.items():
        node_type, node_id = key
        # upstream = predecessors of the anchor (semantic, per PREDECESSOR_POSITION)
        up_levels, up_total, up_trunc = bfs_directional(
            key, forward, reverse, title_lookup, "upstream", DEPTH, TOP_K_PER_LEVEL
        )
        # downstream = successors of the anchor (semantic, per PREDECESSOR_POSITION)
        dn_levels, dn_total, dn_trunc = bfs_directional(
            key, forward, reverse, title_lookup, "downstream", DEPTH, TOP_K_PER_LEVEL
        )

        # Skip anchors with zero edges either way (no chain to tell)
        if up_total == 0 and dn_total == 0:
            continue

        trunc_depth = None
        if up_trunc is not None and dn_trunc is not None:
            trunc_depth = min(up_trunc, dn_trunc)
        elif up_trunc is not None:
            trunc_depth = up_trunc
        elif dn_trunc is not None:
            trunc_depth = dn_trunc
        if trunc_depth is not None:
            truncated_count += 1

        anchor_key = f"{node_type}:{node_id}"
        anchor_output[anchor_key] = {
            "anchor": {
                "type": node_type,
                "id": node_id,
                "title": info["title"],
                **info.get("extra", {}),
            },
            "upstream": up_levels,
            "downstream": dn_levels,
            "stats": {
                "total_upstream": up_total,
                "total_downstream": dn_total,
                "truncated_at_depth": trunc_depth,
            },
        }
        total_chain_nodes += up_total + dn_total
        by_anchor_type[node_type] += 1

    # Lens counts across all chain edges (for the summary panel)
    by_lens: dict[str, int] = defaultdict(int)
    for entry in anchor_output.values():
        for direction in ("upstream", "downstream"):
            for level_entries in entry[direction].values():
                for c in level_entries:
                    by_lens[c["lens"]] += 1

    payload = {
        "generated_from": "tools/viz/console/build_chain_of_custody.py",
        "schema_version": "1.0",
        "config": {
            "depth": DEPTH,
            "top_k_per_level": TOP_K_PER_LEVEL,
        },
        "lens_definitions": {
            "authorship": sorted(LENS_AUTHORSHIP),
            "citation":   sorted(LENS_CITATION),
            "custody":    sorted(LENS_CUSTODY),
            "logical":    sorted(LENS_LOGICAL),
        },
        "summary": {
            "anchors_in_payload":      len(anchor_output),
            "anchors_skipped_no_edges": len(anchors) - len(anchor_output),
            "total_chain_nodes":       total_chain_nodes,
            "by_anchor_type":          dict(by_anchor_type),
            "by_lens":                 dict(by_lens),
            "truncated_anchors":       truncated_count,
            "depth":                   DEPTH,
            "top_k_per_level":         TOP_K_PER_LEVEL,
        },
        "anchors": anchor_output,
    }

    OUT_PATH.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    size_bytes = OUT_PATH.stat().st_size
    print()
    print(f"[build_chain_of_custody] anchors      : {len(anchor_output):,} "
          f"(of {len(anchors):,} selected; {len(anchors) - len(anchor_output):,} "
          f"had no edges)")
    print(f"  by type:")
    for t in sorted(by_anchor_type, key=lambda x: -by_anchor_type[x]):
        print(f"    {t:<22} {by_anchor_type[t]:>6,}")
    print(f"  chain nodes  : {total_chain_nodes:,} (mean "
          f"{total_chain_nodes/max(1,len(anchor_output)):.1f} per anchor)")
    print(f"  truncated    : {truncated_count:,} anchors hit top_k cap")
    print(f"  by lens:")
    for L in sorted(by_lens, key=lambda x: -by_lens[x]):
        print(f"    {L:<14} {by_lens[L]:>7,}")
    print(f"  -> {OUT_PATH}")
    print(f"     ({size_bytes:,} bytes / {size_bytes/1024/1024:.2f} MB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
