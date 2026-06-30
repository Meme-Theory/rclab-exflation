#!/usr/bin/env python3
"""
S84 W9a-103 — S84-W1-CF-CRITPATH
================================

Gate: S84-W9A-103-CRITPATH  ([VERIFY])

Pre-registered threshold (plan lines 1137-1145):
  PASS: per-wave dependency graph constructed for every S84 wave;
        every gate has critical_path flag assigned; hook posture map
        emitted; self-test on W9a recovers the expected flag pattern.
  FAIL: graph construction fails (e.g. circular dependency),
        hook posture map absent, or self-test flag pattern deviates.
  INFO: graph built but some gates lack outgoing edges because their
        data-file declarations are ambiguous.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - sessions/session-plan/session-84-plan-w*.md (all 17 wave-plan files)
  - canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<self_test_status>, scheme=file-flow_dependency,
   convention=networkx_directed_graph, L_max=plan-scope)

Classification: NON-PHONONIC (methodology / dependency analysis)

METHODOLOGY
-----------
Parse markdown gate blocks from session-84 wave plans (delimited by
`## §W{wave}-{idx}` headings). For each gate extract:
  incoming  = input_files (backticked paths under ### Method, ### Inputs,
              "Files read", or "### input_files").
  outgoing  = producing_script + declared data outputs
              (.py / .npz / .png / .json / .md paths under ### Method,
               "Files created", or "### Effort").
Build one networkx DiGraph per wave; edges are gate-to-gate where one
gate's output is another gate's input (file-flow dependency). Assign
critical_path(g) by recursion (Definition 3 in plan §W9a-103):

  critical_path(g) = True iff outgoing(g) is non-empty
                     AND (some g' in outgoing(g) is terminal
                          OR critical_path(g') = True).

Emit hook_posture_map.json: BLOCKING for critical_path=True, ADVISORY
for critical_path=False. Self-test on W9a recovers the expected flag
pattern (W9a-97, 98, 99, 100, 102 = True; W9a-101, 103, 104 = depends).

DISCIPLINE
----------
- `from canonical_constants import *`
- All intermediates tagged `# (local)`
- CPU path (networkx); OMP_NUM_THREADS capped at 8 per computation-environment.md
- networkx 3.6.1 (installed in .venv312)
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- Atomic append to computations/session-84/s84_gate_verdicts.txt
"""

from __future__ import annotations

# -----------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# -----------------------------------------------------------------
import os
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

from canonical_constants import *  # noqa: F401,F403

# -----------------------------------------------------------------
# Section 2 — Standard imports
# -----------------------------------------------------------------
import hashlib
import json
import re
import sys
import time
from pathlib import Path

import networkx as nx

# -----------------------------------------------------------------
# Section 3 — Paths + PRDR pins
# -----------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: legacy alias replaced (replaced by tools.computation_root.resolve_*)
PLAN_DIR = PROJECT_ROOT / "sessions" / "session-plan"
SESSION_DIR = PROJECT_ROOT / "sessions" / "session-84"

SESSION = "S84"                                                      # (local)
GATE_ID = "S84-W9A-103-CRITPATH"                                     # (local)
SCHEME = "file-flow_dependency"                                      # (local)
CONVENTION = "networkx_directed_graph"                               # (local)
L_MAX = "plan-scope"                                                 # (local)

# --- PRDR PINS (plan §W9a-103, lines 1121-1128) ---
GRAPH_LIBRARY = "networkx"                                           # (local)
CRITICAL_PATH_DEFINITION = (                                         # (local)
    "has outgoing edges AND at least one outgoing target is "
    "critical_path or terminal"
)
HOOK_POSTURE_MAP_PATH = SESSION_DIR / "hook_posture_map.json"        # (local)
CROSS_SESSION_FLAG = "cross-session"                                 # (local)
WRITE_BACK_FLAG = "--write-back"                                     # (local)

# Output destinations
VERDICT_TXT = resolve_output(84, 's84_gate_verdicts.txt')
WAVE_PLAN_GLOB = "session-84-plan-w*.md"                             # (local)

# Expected self-test flag pattern (plan lines 1116-1118)
EXPECTED_CRITPATH = {                                                # (local)
    "W9a-97":  True,
    "W9a-98":  True,
    "W9a-99":  True,
    "W9a-100": True,
    "W9a-102": True,
    # plan explicitly says these "depend on outgoing-edge analysis
    # at plan freeze" — either True or False is acceptable
    "W9a-101": "depends",
    "W9a-103": "depends",
    "W9a-104": "depends",
}

# -----------------------------------------------------------------
# Section 4 — SHA helpers (S84+ dual-SHA schema)
# -----------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()                                             # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    """Print SHA-256 of each input; return {relpath: sha} for closure hash."""
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)                                           # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        except ValueError:
            rel = str(p)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
) -> tuple[str, str]:
    """Compute (audit_sha256, content_sha256) per S84+ dual-SHA schema."""
    script_bytes = b""                                               # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""                                            # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(                                        # (local)
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                      # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()                                  # (local)

    return audit, content


# -----------------------------------------------------------------
# Section 5 — Gate-YAML parser (markdown gate-block variant)
# -----------------------------------------------------------------

# Gate-header pattern: accepts three separator styles between the
# §{wave}-{idx} token and any title prose:
#   "## §W9a-103"                                   (bare)
#   "## §W9a-103 — Title"                           (em-dash)
#   "## §W1a-1. S84-BASELINE"                       (period + prose)
# Captures both the §-token and any trailing title text.
GATE_HEADER_RE = re.compile(
    r"^##\s+§(?P<id>[Ww]\d+[a-z]?-\d+)\s*[.\-—]?\s*(?P<title>.*)$",
    re.MULTILINE,
)

# File-path extraction (capture .py/.npz/.png/.json/.md/.yaml/.sh/.txt
# backticked paths that look like project-relative filesystem paths)
FILEPATH_RE = re.compile(
    r"`([A-Za-z0-9_./\-]+\.(?:py|npz|png|json|md|yaml|sh|txt|jsonl))`"
)

# Section-header pattern within a gate block
# Accepts `### Name`, `### N. Name`, `### N) Name`
SECTION_HEADER_RE = re.compile(r"^###\s+(.+?)\s*$", re.MULTILINE)


def _normalize_section_name(name: str) -> str:
    """Strip leading numbering ('1. ', '2) ', 'Step 3: ') and lowercase.

    Also strips trailing parenthetical annotations like '(one sentence)' and
    em-dash continuations like 'Method — complete dispatch prompt'.
    """
    n = re.sub(r"^\s*\d+\s*[.)]\s*", "", name)                       # (local)
    n = re.sub(r"\s+—\s+.*$", "", n)                                 # (local)
    n = re.sub(r"\s*\([^)]*\)\s*$", "", n)                           # (local)
    return n.strip().lower()


def parse_gate_blocks(plan_path: Path) -> list[dict]:
    """Split plan markdown into gate blocks keyed by §{wave}-{idx}.

    Returns list of dicts with keys:
      gate_id, wave, title, raw_body, sections (dict section_name -> text).
    """
    try:
        text = plan_path.read_text(encoding="utf-8")                 # (local)
    except OSError:
        return []

    # Find every gate header and its span
    matches = list(GATE_HEADER_RE.finditer(text))                    # (local)
    if not matches:
        return []

    blocks: list[dict] = []
    for i, m in enumerate(matches):
        start = m.end()                                              # (local)
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)  # (local)
        body = text[start:end]                                       # (local)

        # Extract ### sections (normalized to lowercase, leading numbers stripped)
        section_hits = list(SECTION_HEADER_RE.finditer(body))        # (local)
        sections: dict[str, str] = {}
        for j, sh in enumerate(section_hits):
            raw_name = sh.group(1).strip()                           # (local)
            key = _normalize_section_name(raw_name)                  # (local)
            s_start = sh.end()                                       # (local)
            s_end = section_hits[j + 1].start() if j + 1 < len(section_hits) else len(body)  # (local)
            sections[key] = body[s_start:s_end].strip()

        gate_id = m.group("id")                                      # (local)
        wave = re.match(r"(W\d+[a-z]?)", gate_id, re.IGNORECASE).group(1)  # (local)
        blocks.append({
            "gate_id": gate_id,
            "wave": wave,
            "title": (m.group("title") or "").strip(),
            "plan_file": str(plan_path.relative_to(PROJECT_ROOT)).replace("\\", "/"),
            "raw_body": body,
            "sections": sections,
        })
    return blocks


def extract_files(block: dict, *, which: str) -> set[str]:
    """Return set of file paths from gate block.

    which='outputs' — paths under ### Method (script produces),
                      ### Effort (Files created), and triple-backtick
                      code-block headers for .py scripts.
    which='inputs'  — paths under ### Method (reads), ### Hypothesis,
                      ### input_files, "Files read".
    """
    sections = block["sections"]                                     # (local)

    if which == "outputs":
        # Authoritative output signal: first backticked path on a
        # bulleted line within the ### Effort section. This excludes
        # references like "Integration with `path`" where the backticked
        # path is a dependency, not an artifact created by this gate.
        pool = ""                                                    # (local)
        for name in ("effort", "effort estimate", "files created",
                     "produces", "outputs"):
            if name in sections:
                pool += "\n" + sections[name]
        files: set[str] = set()
        # Match bulleted lines where the first non-whitespace char after
        # the bullet is a backticked path.
        # Two bullet styles: "- " and "* ".
        bullet_re = re.compile(
            r"^\s*[-*]\s+`([A-Za-z0-9_./\-]+\.(?:py|npz|png|json|md|yaml|sh|txt|jsonl))`",
            re.MULTILINE,
        )                                                            # (local)
        for m in bullet_re.finditer(pool):
            files.add(m.group(1))
        return files
    elif which == "inputs":
        pool = ""                                                    # (local)
        for name in ("method", "hypothesis", "prdr", "input_files",
                     "inputs", "files read", "input files",
                     "machinery pin", "machinery pin, prdr",
                     "hypothesis, one sentence",
                     "method, complete self-contained dispatch prompt"):
            if name in sections:
                pool += "\n" + sections[name]
        return set(FILEPATH_RE.findall(pool))
    else:
        raise ValueError(which)


def classify_file(path: str) -> str:
    """Return 'script' | 'data' | 'doc' | 'config' based on extension."""
    if path.endswith(".py"):
        return "script"
    if path.endswith((".npz", ".png", ".json", ".jsonl", ".txt")):
        return "data"
    if path.endswith((".md", ".yaml", ".sh")):
        return "config"
    return "doc"


# -----------------------------------------------------------------
# Section 6 — Graph construction
# -----------------------------------------------------------------

def _path_basename(p: str) -> str:
    """Normalize a file path to its basename for cross-gate matching.

    Plans reference artifacts with inconsistent prefixing:
      '_pru_cardinality_audit.py' vs 'computations/_shared/_pru_cardinality_audit.py'
    both refer to the same physical file. For graph-edge detection we
    match by basename; the full path is retained in node metadata.
    """
    return p.rsplit("/", 1)[-1]


def build_graph_for_wave(blocks: list[dict]) -> nx.DiGraph:
    """Build one DiGraph per wave.

    Nodes: gate_ids.
    Edges: g1 -> g2 if some output-path of g1 appears as an input of g2
           (matched by basename to tolerate path-prefix variation).
    """
    G = nx.DiGraph()                                                 # (local)

    # Collect per-gate input/output sets (full paths)
    gate_in_full: dict[str, set[str]] = {}                           # (local)
    gate_out_full: dict[str, set[str]] = {}                          # (local)
    # Basename sets (used for matching)
    gate_in_bn: dict[str, set[str]] = {}                             # (local)
    gate_out_bn: dict[str, set[str]] = {}                            # (local)

    for b in blocks:
        g = b["gate_id"]
        ins = extract_files(b, which="inputs")                       # (local)
        outs = extract_files(b, which="outputs")                     # (local)
        # A gate's own outputs that also appear in its Method section
        # (input harvest source) are NOT real inputs; remove them by
        # basename.
        out_bn = {_path_basename(x) for x in outs}                   # (local)
        ins_clean = {x for x in ins if _path_basename(x) not in out_bn}  # (local)
        gate_in_full[g] = ins_clean
        gate_out_full[g] = outs
        gate_in_bn[g] = {_path_basename(x) for x in ins_clean}
        gate_out_bn[g] = out_bn
        G.add_node(
            g,
            wave=b["wave"],
            title=b["title"],
            plan_file=b["plan_file"],
            incoming_files=sorted(ins_clean),
            outgoing_files=sorted(outs),
        )

    # Edges: for each output basename of g1 that is an input basename
    # of g2, add g1 -> g2 (exclude self-loops)
    for g1, out_bn in gate_out_bn.items():
        for g2, in_bn in gate_in_bn.items():
            if g1 == g2:
                continue
            shared = out_bn & in_bn                                  # (local)
            if shared:
                G.add_edge(g1, g2, files=sorted(shared))

    return G


# -----------------------------------------------------------------
# Section 7 — critical_path recursion (plan Definition 3)
# -----------------------------------------------------------------

def compute_critical_path(G: nx.DiGraph) -> dict[str, bool]:
    """Assign critical_path(g) per plan Definition 3.

    critical_path(g) = True iff outgoing(g) non-empty
                       AND (some g' in outgoing(g) is terminal
                            OR critical_path(g') = True).

    Requires G to be a DAG; otherwise raises.
    """
    if not nx.is_directed_acyclic_graph(G):
        cycles = list(nx.simple_cycles(G))                           # (local)
        raise RuntimeError(f"graph is not a DAG; cycles: {cycles[:3]}")

    critpath: dict[str, bool] = {}                                   # (local)
    # Process nodes in reverse topological order (terminals first)
    topo = list(nx.topological_sort(G))                              # (local)
    for g in reversed(topo):
        succ = list(G.successors(g))                                 # (local)
        if not succ:
            critpath[g] = False                                      # terminal (base case)
            continue
        # Non-empty outgoing: critical iff ANY successor is terminal
        # OR already marked critical_path
        is_critical = False                                          # (local)
        for g2 in succ:
            if not list(G.successors(g2)):                           # g2 terminal
                is_critical = True
                break
            if critpath.get(g2, False):
                is_critical = True
                break
        critpath[g] = is_critical
    return critpath


# -----------------------------------------------------------------
# Section 8 — JSON emission (per-wave + hook posture map)
# -----------------------------------------------------------------

def graph_summary(G: nx.DiGraph) -> dict:
    """Return summary of graph: nodes, edges, max_depth (longest path)."""
    nodes = G.number_of_nodes()                                      # (local)
    edges = G.number_of_edges()                                      # (local)
    try:
        max_depth = nx.dag_longest_path_length(G) if nodes else 0    # (local)
    except Exception:
        max_depth = -1                                               # (local)
    return {"nodes": nodes, "edges": edges, "max_depth": max_depth}


def gate_record(
    g: str, G: nx.DiGraph, critpath: dict[str, bool]
) -> dict:
    """JSON record per gate."""
    data = G.nodes[g]                                                # (local)
    incoming_edges = [                                               # (local)
        {"from": u, "files": G.edges[u, g]["files"]}
        for u in G.predecessors(g)
    ]
    outgoing_edges = [                                               # (local)
        {"to": v, "files": G.edges[g, v]["files"]}
        for v in G.successors(g)
    ]
    return {
        "gate_id": g,
        "wave": data.get("wave"),
        "title": data.get("title"),
        "plan_file": data.get("plan_file"),
        "incoming_files": data.get("incoming_files", []),
        "outgoing_files": data.get("outgoing_files", []),
        "incoming_edges": incoming_edges,
        "outgoing_edges": outgoing_edges,
        "critical_path": critpath[g],
        "hook_posture": "BLOCKING" if critpath[g] else "ADVISORY",
    }


def wave_record(wave: str, G: nx.DiGraph, critpath: dict[str, bool]) -> dict:
    gates_map = {                                                    # (local)
        g: gate_record(g, G, critpath) for g in sorted(G.nodes())
    }
    return {
        "wave": wave,
        "graph_summary": graph_summary(G),
        "gates": gates_map,
    }


# -----------------------------------------------------------------
# Section 9 — Self-test on W9a
# -----------------------------------------------------------------

def self_test_w9a(
    wave_recs: dict[str, dict]
) -> tuple[str, list[str]]:
    """Compare computed critical_path flags to EXPECTED_CRITPATH.

    Returns (status, diagnostics). Status is one of:
      'PASS' — all must-True gates matched; depends gates accepted.
      'INFO' — must-True gates that computed False have 0 outgoing
               edges (ambiguous file-declaration, per plan line 1143-1145).
      'FAIL' — any must-True gate computed False AND has outgoing edges
               (structural critical_path logic broken), or graph missing.
    """
    diagnostics: list[str] = []
    if "W9a" not in wave_recs:
        return "FAIL", ["W9a wave not present in wave_recs"]

    w9a = wave_recs["W9a"]["gates"]                                  # (local)
    hard_fail = False                                                # (local)
    ambiguous_count = 0                                              # (local)
    for expected_key, expected_val in EXPECTED_CRITPATH.items():
        match = None                                                 # (local)
        for gid in w9a:
            if gid.lower() == expected_key.lower():
                match = gid
                break
        if match is None:
            diagnostics.append(f"  MISSING: {expected_key} not in W9a graph")
            hard_fail = True
            continue
        computed = w9a[match]["critical_path"]                       # (local)
        out_edges = w9a[match].get("outgoing_edges", [])             # (local)
        n_out = len(out_edges)                                       # (local)
        if expected_val == "depends":
            diagnostics.append(
                f"  OK (depends): {expected_key} critical_path={computed} "
                f"out_edges={n_out}"
            )
            continue
        if computed == expected_val:
            diagnostics.append(
                f"  OK: {expected_key} critical_path={computed} "
                f"out_edges={n_out}"
            )
            continue
        # Mismatch: must-True gate came back False
        if n_out == 0:
            # Ambiguous file-declaration per plan INFO clause
            ambiguous_count += 1
            diagnostics.append(
                f"  INFO (ambiguous): {expected_key} critical_path=False, "
                f"out_edges=0 — plan asserts downstream consumers exist but "
                f"file-flow parser did not detect them"
            )
        else:
            # Hard failure: gate has outgoing edges but recursion says False
            hard_fail = True
            diagnostics.append(
                f"  FAIL: {expected_key} critical_path=False, "
                f"out_edges={n_out} — structural logic broken"
            )
    if hard_fail:
        return "FAIL", diagnostics
    if ambiguous_count > 0:
        return "INFO", diagnostics
    return "PASS", diagnostics


# -----------------------------------------------------------------
# Section 10 — Verdict emission
# -----------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(
    verdict: str, value, audit_sha: str, content_sha: str
) -> None:
    """Atomic single-line append to the canonical verdict file."""
    line = (
        f"{GATE_ID}: {verdict} -- value={value} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    comment = (
        f"# {GATE_ID} dual-SHA: content_sha256={content_sha} "
        f"audit_sha256={audit_sha}\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(comment)


# -----------------------------------------------------------------
# Section 11 — Main
# -----------------------------------------------------------------

def main() -> int:
    t0 = time.time()                                                 # (local)

    # 1. Enumerate plan files
    plan_files = sorted(PLAN_DIR.glob(WAVE_PLAN_GLOB))               # (local)
    print(f"=== {GATE_ID} — {len(plan_files)} wave plans discovered ===")

    # 2. Log SHA pins for all plan files + canonical_constants
    inputs = plan_files + [resolve_script(None, 'canonical_constants.py')]     # (local)
    pins = log_input_pins(inputs)

    # 3. Dual SHAs
    script_path = Path(__file__).resolve()                           # (local)
    canonical_path = resolve_script(None, 'canonical_constants.py')            # (local)
    audit_sha, content_sha = compute_dual_sha(
        script_path, canonical_path, pins
    )
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    # 4. Parse every plan file into gate blocks
    all_blocks: list[dict] = []                                      # (local)
    for pf in plan_files:
        blocks = parse_gate_blocks(pf)                               # (local)
        all_blocks.extend(blocks)
        print(f"  parsed {len(blocks):3d} gate(s) from {pf.name}")
    print(f"  total gates: {len(all_blocks)}")
    print()

    # 5. Partition by wave and build one DiGraph per wave
    by_wave: dict[str, list[dict]] = {}                              # (local)
    for b in all_blocks:
        by_wave.setdefault(b["wave"], []).append(b)

    wave_records: dict[str, dict] = {}                               # (local)
    critpath_by_wave: dict[str, dict[str, bool]] = {}                # (local)
    for wave, blocks in sorted(by_wave.items()):
        G = build_graph_for_wave(blocks)                             # (local)
        try:
            critpath = compute_critical_path(G)                      # (local)
        except RuntimeError as exc:
            print(f"  FAIL on wave {wave}: {exc}")
            # emit a FAIL verdict and exit
            append_verdict("FAIL", f"cycle_in_{wave}",
                           audit_sha, content_sha)
            return 1
        critpath_by_wave[wave] = critpath
        rec = wave_record(wave, G, critpath)                         # (local)
        wave_records[wave] = rec
        summ = rec["graph_summary"]
        n_crit = sum(1 for v in critpath.values() if v)              # (local)
        print(f"  {wave}: nodes={summ['nodes']:3d} "
              f"edges={summ['edges']:3d} "
              f"max_depth={summ['max_depth']:2d} "
              f"critical={n_crit}")

    # 6. Self-test on W9a
    print()
    print("=== Self-test on W9a ===")
    self_test_status, diags = self_test_w9a(wave_records)            # (local)
    for line in diags:
        print(line)
    print(f"  self-test: {self_test_status}")

    # 7. Emit hook_posture_map.json (flat map: gate_id -> BLOCKING|ADVISORY)
    SESSION_DIR.mkdir(parents=True, exist_ok=True)
    posture_map: dict[str, str] = {}                                 # (local)
    for wave, rec in wave_records.items():
        for gid, g_rec in rec["gates"].items():
            posture_map[gid] = g_rec["hook_posture"]

    hook_json = {                                                    # (local)
        "schema_version": "S84+W9a-103",
        "critical_path_definition": CRITICAL_PATH_DEFINITION,
        "graph_library": GRAPH_LIBRARY,
        "cross_session_flag": CROSS_SESSION_FLAG,
        "waves": wave_records,
        "posture_map": posture_map,
        "self_test": {
            "expected": {k: (v if v != "depends" else "DEPENDS")
                         for k, v in EXPECTED_CRITPATH.items()},
            "status": self_test_status,
            "diagnostics": diags,
        },
    }
    HOOK_POSTURE_MAP_PATH.write_text(
        json.dumps(hook_json, indent=2, sort_keys=False),
        encoding="utf-8",
    )
    print(f"  wrote {HOOK_POSTURE_MAP_PATH.relative_to(PROJECT_ROOT)}")

    # 8. Verdict + 4-tuple
    verdict = self_test_status                                       # (local)
    value_tag = f"self_test_{self_test_status}"                      # (local)
    tag = emit_4tuple(value_tag, SCHEME, CONVENTION, L_MAX)
    print(tag)

    if os.environ.get("CRITPATH_DRYRUN") == "1":
        print("  [DRYRUN] verdict NOT appended to s84_gate_verdicts.txt")
    else:
        append_verdict(verdict, value_tag, audit_sha, content_sha)

    wall = time.time() - t0                                          # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    # Exit 0 on PASS or INFO (both indicate successful graph construction);
    # exit 1 only on FAIL (graph construction error or structural break).
    return 0 if verdict in ("PASS", "INFO") else 1


if __name__ == "__main__":
    sys.exit(main())
