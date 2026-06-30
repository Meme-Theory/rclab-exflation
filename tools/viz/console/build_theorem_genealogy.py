#!/usr/bin/env python3
"""
Theorem-genealogy graph builder.

Two node sources combine into one graph:

  1. Structural theorems from session-85 slot×track workshop files
     (`sessions/session-{N}/session-{N}-s{slot}-*-{track}.md`).  Each file
     proves the SAME structural theorem with DIFFERENT machinery — connes
     K-theory, lizzi spectral-functional, van-den-dungen Kasparov bridge,
     volovik analogue-gravity, etc.  Two tracks at the same slot generate
     a `cross_track` edge — these are the edges that turn the genealogy
     from a tree into a graph.

  2. Proven theorems from `tools/knowledge.db::theorems` (`proven_N` IDs)
     filtered by the same quality rules as `build_data.py::get_theorems`.

Edges:
  - cross_track : (slot, track_A) ↔ (slot, track_B)
  - cites       : theorem statement mentions another theorem id
  - depends_on  : structural-theorem references upstream gate (W5-N, S78 W2-F, ...)

Output:
  tools/viz/console/theorem_genealogy.json
"""

from __future__ import annotations

import json
import re
import sqlite3
from dataclasses import dataclass, field, asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent.parent
DB_PATH = ROOT / "tools" / "knowledge.db"
SESSIONS_DIR = ROOT / "sessions"
OUT_PATH = ROOT / "tools" / "viz" / "console" / "theorem_genealogy.json"


# ---------------------------------------------------------------------------
# Structural-theorem extraction (S85 slot×track workshop files)
# ---------------------------------------------------------------------------

# session-{N}-s{slot}-{slug}-{track}.md
SLOT_FILE_RE = re.compile(
    r"^session-(?P<sess>\d+)-(?P<slot>s\d+)-(?P<slug>[a-z][a-z0-9-]*?)-(?P<track>[a-z][a-z-]+)\.md$",
    re.I,
)
# **Theorem (Name, formulation)** or  ## §... Theorem ...
THEOREM_NAME_RE = re.compile(
    r"\*\*Theorem\s*(?:\(([^)]+)\))?\*\*",
    re.I,
)
# Slot tag in header: "Slot: S-1" or "Slot S-1" or first H1 line containing S-1
SLOT_TAG_RE = re.compile(r"\bS-\d+\b")
# Upstream gate reference patterns commonly used in workshop prose
GATE_REF_RE = re.compile(
    r"\b(?:S\d+\s+)?(W\d+[a-z]?-?\d*-?[A-Z][A-Z0-9-]+|S\d+-W\d+[a-z]?-[A-Z][A-Z0-9-]+|S\d+\s+W\d+[a-z]?-[A-Z]+)\b"
)
PROVEN_ID_RE = re.compile(r"\bproven_\d+\b")

# Track → broad area (used to color nodes; falls back to "general")
TRACK_AREA = {
    "connes":            "NCG",
    "lizzi":             "spectral",
    "van-den-dungen":    "NCG",
    "dungen":            "NCG",            # filename-truncated form
    "landau":            "BCS",
    "volovik":           "transit",
    "mack":              "cosmo",
    "kaku":              "geometry",
    "gen-physicist":     "general",
    "physicist":         "general",
    "spectral-geometer": "spectral",
    "geometer":          "spectral",
}


@dataclass
class Node:
    id: str
    kind: str                                       # structural | proven
    name: str = ""
    slot: str = ""
    track: str = ""
    session: str = ""
    area: str = ""
    statement: str = ""

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class Edge:
    src: str
    tgt: str
    kind: str                                       # cross_track | cites | depends_on
    note: str = ""

    def to_dict(self) -> dict:
        return asdict(self)


def normalize_track(t: str) -> str:
    """Map filename-truncated track tags back to canonical names."""
    if t == "dungen":
        return "van-den-dungen"
    if t == "physicist":
        return "gen-physicist"
    if t == "geometer":
        return "spectral-geometer"
    return t


def extract_structural_node(path: Path) -> tuple[Node, set[str]] | None:
    """Return (Node, set of upstream-gate references) for one workshop file."""
    m = SLOT_FILE_RE.match(path.name)
    if not m:
        return None
    sess = m.group("sess")
    slot_tag = m.group("slot").upper()              # e.g. "S1"
    slot_id = slot_tag.replace("S", "S-")           # canonicalize "S1" → "S-1"
    slug = m.group("slug")
    track_raw = m.group("track").lower()
    track = normalize_track(track_raw)
    area = TRACK_AREA.get(track_raw, TRACK_AREA.get(track, "general"))

    text = path.read_text(encoding="utf-8", errors="ignore")
    head = text[:8000]                              # title + theorem-statement region

    # Theorem name from the first **Theorem (...)** pattern in the head.
    name = ""
    nm = THEOREM_NAME_RE.search(head)
    if nm:
        name = (nm.group(1) or "").strip() or slug.replace("-", " ")
    if not name:
        name = slug.replace("-", " ").title()

    # First-paragraph statement after the **Theorem** marker.
    statement = ""
    if nm:
        after = head[nm.end():]
        # Take up to ~400 chars or to next blank line.
        statement = re.split(r"\n\s*\n", after, 1)[0]
        statement = re.sub(r"\s+", " ", statement).strip()[:400]

    # Confirm slot tag appears in head (defensive).
    if not SLOT_TAG_RE.search(head):
        slot_id = slot_tag                          # fall back to S1 form

    nid = f"slot:{slot_id}:{track}"
    node = Node(
        id=nid, kind="structural",
        name=name, slot=slot_id, track=track,
        session=f"S{sess}", area=area, statement=statement,
    )

    # Upstream references — look across the WHOLE file, not just head.
    refs: set[str] = set()
    for r in GATE_REF_RE.finditer(text):
        tok = r.group(1).strip()
        if not tok or tok.lower().startswith("session"):
            continue
        if len(tok) < 4:
            continue
        refs.add(tok)
    for r in PROVEN_ID_RE.finditer(text):
        refs.add(r.group(0))

    return (node, refs)


def collect_structural_nodes() -> tuple[list[Node], list[Edge]]:
    nodes: dict[str, Node] = {}
    refs_by_node: dict[str, set[str]] = {}

    # Walk all session-*/session-*-s{N}-*.md files.
    for sess_dir in sorted(SESSIONS_DIR.glob("session-*")):
        if not sess_dir.is_dir():
            continue
        for path in sorted(sess_dir.glob("*.md")):
            res = extract_structural_node(path)
            if not res:
                continue
            node, refs = res
            nodes[node.id] = node
            refs_by_node[node.id] = refs

    edges: list[Edge] = []
    # 1. cross_track edges — every pair of tracks at the same (session, slot).
    by_slot: dict[tuple[str, str], list[Node]] = {}
    for n in nodes.values():
        by_slot.setdefault((n.session, n.slot), []).append(n)
    for (sess, slot), members in by_slot.items():
        members.sort(key=lambda x: x.track)
        for i in range(len(members)):
            for j in range(i + 1, len(members)):
                edges.append(Edge(
                    src=members[i].id, tgt=members[j].id,
                    kind="cross_track",
                    note=f"{sess} {slot} multi-track proof",
                ))

    # 2. depends_on edges — structural theorem → upstream gate reference.
    for nid, refs in refs_by_node.items():
        for tok in sorted(refs):
            if tok.startswith("proven_"):
                edges.append(Edge(src=nid, tgt=tok, kind="cites"))
            else:
                edges.append(Edge(src=nid, tgt=tok, kind="depends_on"))

    return list(nodes.values()), edges


# ---------------------------------------------------------------------------
# Proven-theorem extraction (knowledge.db::theorems, quality-filtered)
# ---------------------------------------------------------------------------

ALPHA = re.compile(r"[A-Za-z]")
GARBAGE_NAME = re.compile(r"^[\sx\-+=.·×*\d,eE/]+$")
WRAP_PROSE = re.compile(
    r"(Answer\*\*:|Changed\*\*:|What it is\*\*:|Key insight|Strategy\*\*:)",
    re.I,
)
SESS_RE = re.compile(r"^(Session\s+\d+[a-z]?|\d+[a-z]?)(\s*\|\s*.*)?$", re.I)

AREA_KEYWORDS = [
    ("spectral", ["spectral", "seeley", "dewitt", "a_2", "a_4", "heat kernel", "dirac"]),
    ("BCS",      ["bcs", "gap", "pairing", "cooper", "condensate", "leggett", "richardson"]),
    ("NCG",      ["ncg", "noncommut", "spectral triple", "barrett", "ko-dim"]),
    ("symmetry", ["cpt", "cp", "charge conjug", "parity", "u(1)", "weyl group", "chirality"]),
    ("transit",  ["transit", "parker", "kibble", "zurek", "instanton", "bogoliubov", "quench"]),
    ("stability",["hessian", "stabil", "monoton", "saturat", "positive definite"]),
    ("acoustic", ["acoustic", "sound", "goldstone", "phonon", "impedance", "hawking"]),
    ("CC",       ["cosmolog", "constant", "vacuum", "lambda", "cc gap"]),
    ("cosmo",    ["cmb", "desi", "planck", "hubble", "redshift", "recomb", "bbn", "firas"]),
    ("gauge",    ["gauge", "weinberg", "sin", "coupling", "standard model"]),
    ("simulation", ["gpe", "simulation", "numerical", "ed", "exact diag"]),
    ("geometry", ["jensen", "metric", "curvature", "kk", "kaluza", "fiber", "su(3)", "volume"]),
]


def infer_area(name: str, statement: str) -> str:
    text = f"{name} {statement}".lower()
    for area, kws in AREA_KEYWORDS:
        if any(k in text for k in kws):
            return area
    return "general"


def collect_proven_nodes(limit: int = 250) -> tuple[list[Node], list[Edge]]:
    nodes: list[Node] = []
    if not DB_PATH.exists():
        return ([], [])
    con = sqlite3.connect(str(DB_PATH))
    rows = con.execute(
        """
        SELECT id, name, sessions, statement
        FROM theorems
        WHERE sessions IS NOT NULL AND sessions != ''
          AND statement IS NOT NULL AND length(statement) BETWEEN 20 AND 260
        """
    ).fetchall()
    con.close()

    accepted: dict[str, Node] = {}
    for tid, name, sessions, statement in rows:
        nm = (name or "").strip()
        st = (statement or "").strip()
        ss = (sessions or "").strip()
        if ss.startswith("["):
            try:
                ss = ", ".join(str(x) for x in json.loads(ss))
            except Exception:                        # noqa: BLE001
                pass
        if not SESS_RE.match(ss):
            continue
        if not ALPHA.search(nm) or GARBAGE_NAME.match(nm):
            continue
        if not ALPHA.search(st) or WRAP_PROSE.search(st):
            continue
        node = Node(
            id=tid, kind="proven",
            name=nm[:120], slot="", track="",
            session=ss, area=infer_area(nm, st),
            statement=st,
        )
        accepted[tid] = node
        if len(accepted) >= limit:
            break

    # Citation edges — theorem statement mentions another theorem id.
    edges: list[Edge] = []
    ids = set(accepted)
    for n in accepted.values():
        for m in PROVEN_ID_RE.finditer(n.statement):
            tgt = m.group(0)
            if tgt == n.id or tgt not in ids:
                continue
            edges.append(Edge(src=n.id, tgt=tgt, kind="cites"))

    return list(accepted.values()), edges


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------

def main() -> None:
    s_nodes, s_edges = collect_structural_nodes()
    p_nodes, p_edges = collect_proven_nodes()
    nodes = s_nodes + p_nodes
    edges = s_edges + p_edges

    # Node-existence filter: drop edges whose target is neither a proven_N id
    # in the corpus nor a structural-track node nor a recognized gate reference.
    node_ids = {n.id for n in nodes}
    structural_targets = {n.id for n in s_nodes}
    cleaned_edges: list[Edge] = []
    for e in edges:
        if e.tgt in node_ids or e.kind == "depends_on":
            cleaned_edges.append(e)

    # Track-count summary for header text in the view.
    by_slot: dict[str, list[str]] = {}
    for n in s_nodes:
        by_slot.setdefault(n.slot, []).append(n.track)

    payload = {
        "generated_from": "tools/viz/console/build_theorem_genealogy.py",
        "summary": {
            "structural_nodes": len(s_nodes),
            "proven_nodes": len(p_nodes),
            "edges_total": len(cleaned_edges),
            "cross_track_edges": sum(1 for e in cleaned_edges if e.kind == "cross_track"),
            "slots": {slot: sorted(set(tracks)) for slot, tracks in by_slot.items()},
        },
        "nodes": [n.to_dict() for n in nodes],
        "edges": [e.to_dict() for e in cleaned_edges],
    }
    OUT_PATH.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(
        f"[build_theorem_genealogy]\n"
        f"  structural nodes : {len(s_nodes)}\n"
        f"  proven nodes     : {len(p_nodes)}\n"
        f"  edges total      : {len(cleaned_edges)}\n"
        f"    cross_track    : {sum(1 for e in cleaned_edges if e.kind == 'cross_track')}\n"
        f"    cites          : {sum(1 for e in cleaned_edges if e.kind == 'cites')}\n"
        f"    depends_on     : {sum(1 for e in cleaned_edges if e.kind == 'depends_on')}\n"
        f"  slots with multi-track: "
        f"{sorted(s for s, t in by_slot.items() if len(set(t)) > 1)}\n"
        f"  -> {OUT_PATH} ({OUT_PATH.stat().st_size:,} bytes)"
    )


if __name__ == "__main__":
    main()
