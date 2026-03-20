#!/usr/bin/env python3
"""
Knowledge Visualization for the Phonon-Exflation Project.

Generates graphs, timelines, and diagrams from tools/knowledge-index.json.
All output goes to tools/viz/.

Usage:
    python visualize_knowledge.py --graph        # Knowledge topology
    python visualize_knowledge.py --timeline     # Probability trajectory
    python visualize_knowledge.py --provenance   # Data flow graph
    python visualize_knowledge.py --citations    # Researcher domain map
    python visualize_knowledge.py --gates        # Gate verdict table
    python visualize_knowledge.py --mermaid      # Mermaid code to stdout
    python visualize_knowledge.py --all          # All of the above
"""

import re
import json
import argparse
import textwrap
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.colors import to_rgba
import networkx as nx


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent
INDEX_PATH = PROJECT_ROOT / "tools" / "knowledge-index.json"
VIZ_DIR = PROJECT_ROOT / "tools" / "viz"

# Color palette for entity types
COLORS = {
    "theorem":        "#2ecc71",  # green
    "closed_mechanism": "#e74c3c",  # red
    "gate":           "#f39c12",  # orange
    "open_channel":   "#f1c40f",  # yellow
    "session":        "#3498db",  # blue
    "provenance":     "#9b59b6",  # purple
    "researcher":     "#1abc9c",  # teal
    "trajectory":     "#34495e",  # dark gray
}

# Gate verdict → color mapping for the table
VERDICT_COLORS = {
    "KILL":       "#e74c3c",
    "CLOSED":     "#e74c3c",
    "CLOSURE":    "#e74c3c",
    "FAIL":       "#e67e22",
    "DIAGNOSTIC": "#95a5a6",
    "DOES NOT":   "#bdc3c7",
}

# Key milestones for timeline annotations
MILESTONES = [
    ("7",   "KO-dim=6"),
    ("17b", "Baptista 67/67"),
    ("20b", "TT Casimir CLOSED"),
    ("23a", "K-1e CLOSED"),
    ("24a", "V-1 CLOSED"),
]


# ---------------------------------------------------------------------------
# Utility functions
# ---------------------------------------------------------------------------

def load_index() -> dict:
    """Load and return the knowledge index JSON."""
    if not INDEX_PATH.exists():
        raise FileNotFoundError(
            f"Index not found at {INDEX_PATH}. Run: /weave --update"
        )
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def setup_output_dir():
    """Ensure the viz output directory exists."""
    VIZ_DIR.mkdir(parents=True, exist_ok=True)


def parse_session_order(s: str) -> float:
    """
    Convert session ID to a sortable float.

    "prior" -> 0, "7" -> 7.0, "17a" -> 17.1, "22d" -> 22.4,
    "24a/24b" -> 24.1, "" -> -1 (skip)
    """
    if not s or s.strip() == "":
        return -1.0
    s = s.strip().lower()
    if s == "prior":
        return 0.0
    # Handle "24a/24b" -> take first
    if "/" in s:
        s = s.split("/")[0]
    # Match digits + optional letter suffix
    m = re.match(r"^(\d+)([a-d])?$", s)
    if m:
        num = int(m.group(1))
        suffix = m.group(2)
        offset = 0.0
        if suffix:
            offset = (ord(suffix) - ord("a") + 1) * 0.1
        return num + offset
    # Try bare number
    try:
        return float(s)
    except ValueError:
        return -1.0


def parse_range(s: str):
    """
    Parse a probability range string.

    "38-46" -> (midpoint=42, lo=38, hi=46)
    "40"    -> (40, 40, 40)
    ""      -> None
    """
    if not s or not s.strip():
        return None
    s = s.strip()
    # Range: "38-46"
    m = re.match(r"^(\d+(?:\.\d+)?)\s*[-–]\s*(\d+(?:\.\d+)?)$", s)
    if m:
        lo = float(m.group(1))
        hi = float(m.group(2))
        return ((lo + hi) / 2, lo, hi)
    # Single value
    try:
        v = float(s)
        return (v, v, v)
    except ValueError:
        return None


def extract_session_from_source(source_file: str) -> str:
    """Extract session ID from a source filename."""
    name = Path(source_file).stem
    # Match patterns like "session-24a-synthesis" or "session-22-master"
    m = re.search(r"session-(\d+[a-d]?)", name, re.IGNORECASE)
    if m:
        return m.group(1)
    # Match "s24a_gate_verdicts"
    m = re.search(r"^s(\d+[a-d]?)_", name)
    if m:
        return m.group(1)
    return ""


def parse_sessions_field(text: str) -> list:
    """
    Parse a theorem's 'sessions' field to extract session IDs.

    "Sessions 7-8" -> ["7", "8"]
    "Session 17a"  -> ["17a"]
    "Session 22c"  -> ["22c"]
    "3"            -> []  (too ambiguous)
    """
    if not text:
        return []
    results = []
    # Match "Session(s) X-Y" or "Session X"
    for m in re.finditer(r"[Ss]essions?\s+(\d+[a-d]?)(?:\s*[-–]\s*(\d+[a-d]?))?", text):
        start = m.group(1)
        end = m.group(2)
        if end:
            # Range: expand "7-8" -> ["7", "8"]
            try:
                s_num = int(re.match(r"(\d+)", start).group(1))
                e_num = int(re.match(r"(\d+)", end).group(1))
                for n in range(s_num, e_num + 1):
                    results.append(str(n))
            except (ValueError, AttributeError):
                results.append(start)
        else:
            results.append(start)
    return results


def truncate(text: str, maxlen: int = 25) -> str:
    """Truncate text to maxlen with ellipsis."""
    if not text:
        return ""
    if len(text) <= maxlen:
        return text
    return text[:maxlen - 1] + "…"


def get_file_priority(source_file: str) -> int:
    """Rank source file authority: sagan-verdict > synthesis > master > other."""
    name = Path(source_file).name.lower()
    if "sagan-verdict" in name:
        return 5
    if "synthesis" in name:
        return 4
    if "master" in name:
        return 3
    if "gate_verdicts" in name:
        return 3
    return 1


# ---------------------------------------------------------------------------
# --graph: Knowledge Topology
# ---------------------------------------------------------------------------

def cmd_graph(idx: dict):
    """Generate the knowledge topology graph."""
    G = nx.DiGraph()

    # Track which sessions are referenced
    session_refs = set()

    # --- Add theorem nodes ---
    seen_theorem_names = set()
    for t in idx["theorems"]:
        # Skip parse artifacts
        if t["name"].startswith(":--") or t["name"].startswith("|"):
            continue
        # Deduplicate by name similarity (keep first)
        name_key = re.sub(r"[^a-z0-9]", "", t["name"].lower())[:30]
        if name_key in seen_theorem_names:
            continue
        seen_theorem_names.add(name_key)

        node_id = f"T_{t['id']}"
        G.add_node(node_id, label=truncate(t["name"], 28),
                    ntype="theorem", entity=t)
        # Link to sessions
        for sid in parse_sessions_field(t.get("sessions", "")):
            sess_node = f"S_{sid}"
            session_refs.add(sid)
            G.add_edge(node_id, sess_node)

    # --- Add closed mechanism nodes ---
    for dm in idx["closed_mechanisms"]:
        node_id = f"D_{dm['id']}"
        G.add_node(node_id, label=truncate(dm["name"], 28),
                    ntype="closed_mechanism", entity=dm)
        # Link to gate if present
        if dm.get("gate_id") and dm["gate_id"] != "None":
            gate_node = f"G_{dm['gate_id']}"
            G.add_edge(gate_node, node_id)
        # Link to session from session field
        sess = dm.get("session", "")
        if sess:
            # Extract session number from field like "17a SP-4" or "Session 18"
            m = re.match(r"(?:Session\s+)?(\d+[a-d]?)", sess)
            if m:
                sid = m.group(1)
                sess_node = f"S_{sid}"
                session_refs.add(sid)
                G.add_edge(node_id, sess_node)

    # --- Add gate nodes ---
    for g in idx["gates"]:
        node_id = f"G_{g['id']}"
        G.add_node(node_id, label=g["id"],
                    ntype="gate", entity=g)
        # Extract session from source_file (more reliable than session field)
        sid = extract_session_from_source(g.get("source_file", ""))
        if sid:
            sess_node = f"S_{sid}"
            session_refs.add(sid)
            G.add_edge(node_id, sess_node)

    # --- Add open channel nodes ---
    for i, oc in enumerate(idx["open_channels"]):
        if oc["name"].startswith("Check") or oc["name"].startswith(":"):
            continue  # Skip parse artifacts
        node_id = f"O_{i}"
        G.add_node(node_id, label=truncate(oc["name"], 28),
                    ntype="open_channel", entity=oc)

    # --- Add referenced session nodes ---
    for sid in session_refs:
        sess_node = f"S_{sid}"
        if sess_node not in G:
            G.add_node(sess_node, label=f"Session {sid}",
                        ntype="session", entity={"id": sid})

    # --- Provenance -> gate links ---
    for prov in idx["data_provenance"]:
        if prov.get("gates_informed"):
            script_name = prov.get("script", prov.get("name", ""))
            if script_name:
                prov_node = f"P_{script_name}"
                if prov_node not in G:
                    G.add_node(prov_node, label=truncate(script_name, 20),
                                ntype="provenance", entity=prov)
                for gate_id in prov["gates_informed"]:
                    gate_node = f"G_{gate_id}"
                    if gate_node in G:
                        G.add_edge(prov_node, gate_node)

    # --- Layout ---
    pos = nx.spring_layout(G, k=2.5, iterations=100, seed=42)

    fig, ax = plt.subplots(figsize=(20, 16))
    ax.set_title("Phonon-Exflation Knowledge Topology", fontsize=18, fontweight="bold", pad=20)

    # Draw edges
    nx.draw_networkx_edges(G, pos, ax=ax, alpha=0.2, edge_color="#7f8c8d",
                            arrows=True, arrowsize=8, width=0.5)

    # Draw nodes by type
    for ntype, color in COLORS.items():
        nodes = [n for n, d in G.nodes(data=True) if d.get("ntype") == ntype]
        if not nodes:
            continue
        sizes = []
        for n in nodes:
            if ntype == "gate":
                sizes.append(400)
            elif ntype == "session":
                sizes.append(200)
            elif ntype == "provenance":
                sizes.append(150)
            else:
                sizes.append(250)
        nx.draw_networkx_nodes(G, pos, nodelist=nodes, node_color=color,
                                node_size=sizes, alpha=0.85, ax=ax)

    # Draw labels (only for larger nodes)
    label_nodes = {n: d.get("label", n) for n, d in G.nodes(data=True)
                    if d.get("ntype") in ("theorem", "closed_mechanism", "gate", "session")}
    nx.draw_networkx_labels(G, pos, labels=label_nodes, font_size=5,
                             font_weight="bold", ax=ax)

    # Legend
    legend_handles = []
    type_labels = {
        "theorem": "Theorems (PROVEN)",
        "closed_mechanism": "Closed Mechanisms",
        "gate": "Gate Verdicts",
        "open_channel": "Open Channels",
        "session": "Sessions",
        "provenance": "Provenance Scripts",
    }
    for ntype, label in type_labels.items():
        count = sum(1 for _, d in G.nodes(data=True) if d.get("ntype") == ntype)
        if count:
            legend_handles.append(
                mpatches.Patch(color=COLORS[ntype], label=f"{label} ({count})")
            )
    ax.legend(handles=legend_handles, loc="upper left", fontsize=10,
               framealpha=0.9, fancybox=True)

    # Stats annotation
    stats_text = f"Nodes: {G.number_of_nodes()}  |  Edges: {G.number_of_edges()}"
    ax.annotate(stats_text, xy=(0.99, 0.01), xycoords="axes fraction",
                 ha="right", va="bottom", fontsize=9, color="#7f8c8d")

    ax.axis("off")
    out = VIZ_DIR / "knowledge_graph.png"
    fig.savefig(out, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  [graph] {out}  ({out.stat().st_size / 1024:.0f} KB)")
    return out


# ---------------------------------------------------------------------------
# --timeline: Probability Trajectory
# ---------------------------------------------------------------------------

def cmd_timeline(idx: dict):
    """Generate the probability trajectory chart."""
    raw = idx["probability_trajectory"]

    # --- Step 1: Filter entries with session AND (panel or sagan) ---
    candidates = []
    for pt in raw:
        sess = pt.get("session", "").strip()
        if not sess:
            # Try to extract session from source_file
            sess = extract_session_from_source(pt.get("source_file", ""))
        if not sess:
            continue
        panel = parse_range(pt.get("panel", ""))
        sagan = parse_range(pt.get("sagan", ""))
        if panel is None and sagan is None:
            continue
        candidates.append({
            "session": sess,
            "panel": panel,
            "sagan": sagan,
            "priority": get_file_priority(pt.get("source_file", "")),
            "source": pt.get("source_file", ""),
        })

    # --- Step 2: Deduplicate per session ---
    # For each session, collect all panel values and all sagan values
    # Keep highest-priority source for each
    session_panel = {}   # session -> (priority, midpoint, lo, hi)
    session_sagan = {}

    for c in candidates:
        sess = c["session"]
        if c["panel"]:
            mid, lo, hi = c["panel"]
            existing = session_panel.get(sess)
            if existing is None or c["priority"] > existing[0]:
                session_panel[sess] = (c["priority"], mid, lo, hi)
        if c["sagan"]:
            mid, lo, hi = c["sagan"]
            existing = session_sagan.get(sess)
            if existing is None or c["priority"] > existing[0]:
                session_sagan[sess] = (c["priority"], mid, lo, hi)

    # --- Step 3: Build sorted data series ---
    all_sessions = sorted(
        set(list(session_panel.keys()) + list(session_sagan.keys())),
        key=parse_session_order,
    )
    # Remove sessions with negative order (unparseable)
    all_sessions = [s for s in all_sessions if parse_session_order(s) >= 0]

    panel_x, panel_y, panel_lo, panel_hi = [], [], [], []
    sagan_x, sagan_y, sagan_lo, sagan_hi = [], [], [], []

    for sess in all_sessions:
        x_val = parse_session_order(sess)
        if sess in session_panel:
            _, mid, lo, hi = session_panel[sess]
            panel_x.append(x_val)
            panel_y.append(mid)
            panel_lo.append(lo)
            panel_hi.append(hi)
        if sess in session_sagan:
            _, mid, lo, hi = session_sagan[sess]
            sagan_x.append(x_val)
            sagan_y.append(mid)
            sagan_lo.append(lo)
            sagan_hi.append(hi)

    # --- Step 4: Plot ---
    fig, ax = plt.subplots(figsize=(18, 8))
    ax.set_title("Framework Probability Evolution", fontsize=16, fontweight="bold", pad=15)

    # Panel series (blue)
    if panel_x:
        ax.plot(panel_x, panel_y, "o-", color="#2980b9", linewidth=2,
                markersize=6, label="Panel Median", zorder=5)
        ax.fill_between(panel_x, panel_lo, panel_hi,
                         color="#2980b9", alpha=0.15, zorder=2)

    # Sagan series (red)
    if sagan_x:
        ax.plot(sagan_x, sagan_y, "s-", color="#c0392b", linewidth=2,
                markersize=6, label="Sagan Assessment", zorder=5)
        ax.fill_between(sagan_x, sagan_lo, sagan_hi,
                         color="#c0392b", alpha=0.15, zorder=2)

    # --- Step 5: Milestone annotations ---
    for sess_id, label in MILESTONES:
        x_pos = parse_session_order(sess_id)
        ax.axvline(x=x_pos, color="#7f8c8d", linestyle="--", alpha=0.4, zorder=1)
        ax.annotate(label, xy=(x_pos, ax.get_ylim()[1] * 0.95),
                     fontsize=8, rotation=45, ha="left", va="top",
                     color="#2c3e50", fontweight="bold",
                     bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="#bdc3c7", alpha=0.8))

    # --- Step 6: Axes ---
    # Build tick labels from all_sessions
    tick_positions = [parse_session_order(s) for s in all_sessions]
    tick_labels = [s if s != "prior" else "prior" for s in all_sessions]
    ax.set_xticks(tick_positions)
    ax.set_xticklabels(tick_labels, rotation=45, ha="right", fontsize=8)
    ax.set_xlabel("Session", fontsize=12)
    ax.set_ylabel("Probability (%)", fontsize=12)
    ax.set_ylim(-2, 60)
    ax.legend(loc="upper right", fontsize=11)
    ax.grid(True, alpha=0.3)
    ax.axhline(y=5, color="#e74c3c", linestyle=":", alpha=0.5, label="_nolegend_")
    ax.annotate("Current: 5% (panel), 3% (Sagan)", xy=(0.98, 0.05),
                 xycoords="axes fraction", ha="right", va="bottom",
                 fontsize=10, color="#7f8c8d", style="italic")

    fig.tight_layout()
    out = VIZ_DIR / "probability_timeline.png"
    fig.savefig(out, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  [timeline] {out}  ({out.stat().st_size / 1024:.0f} KB)")
    return out


# ---------------------------------------------------------------------------
# --provenance: Data Flow Graph
# ---------------------------------------------------------------------------

def cmd_provenance(idx: dict):
    """Generate the data provenance flow graph."""
    G = nx.DiGraph()

    for prov in idx["data_provenance"]:
        session = prov.get("session", "unknown")
        script = prov.get("script")
        name = prov.get("name", "")
        inputs = prov.get("inputs", [])
        outputs = prov.get("outputs", [])
        gates = prov.get("gates_informed", [])

        # Script node
        if script:
            script_id = f"script:{script}"
            G.add_node(script_id, label=truncate(script, 22),
                        ntype="script", session=session,
                        informs_gates=bool(gates))

            # Input -> Script edges
            for inp in inputs:
                inp_id = f"data:{inp}"
                if inp_id not in G:
                    G.add_node(inp_id, label=truncate(inp, 22),
                                ntype="data", session=session)
                G.add_edge(inp_id, script_id)

            # Script -> Output edges
            for out in outputs:
                out_id = f"data:{out}"
                if out_id not in G:
                    G.add_node(out_id, label=truncate(out, 22),
                                ntype="data", session=session)
                G.add_edge(script_id, out_id)

            # Script -> Gate edges
            for gate_id in gates:
                gate_node = f"gate:{gate_id}"
                if gate_node not in G:
                    G.add_node(gate_node, label=gate_id,
                                ntype="gate_ref", session=session)
                G.add_edge(script_id, gate_node)

    # --- Layout ---
    # Use kamada_kawai for better spread with directed graphs
    if G.number_of_nodes() > 0:
        pos = nx.kamada_kawai_layout(G)
    else:
        pos = {}

    fig, ax = plt.subplots(figsize=(24, 16))
    ax.set_title("Data Provenance Flow", fontsize=18, fontweight="bold", pad=20)

    # Draw edges
    nx.draw_networkx_edges(G, pos, ax=ax, alpha=0.25, edge_color="#7f8c8d",
                            arrows=True, arrowsize=6, width=0.5,
                            connectionstyle="arc3,rad=0.05")

    # Node groups
    script_nodes = [n for n, d in G.nodes(data=True) if d.get("ntype") == "script"]
    gate_scripts = [n for n, d in G.nodes(data=True)
                     if d.get("ntype") == "script" and d.get("informs_gates")]
    regular_scripts = [n for n in script_nodes if n not in gate_scripts]
    data_nodes = [n for n, d in G.nodes(data=True) if d.get("ntype") == "data"]
    gate_nodes = [n for n, d in G.nodes(data=True) if d.get("ntype") == "gate_ref"]

    # Color by session prefix
    session_cmap = plt.cm.tab20
    all_sessions_prov = sorted(set(d.get("session", "?") for _, d in G.nodes(data=True)))
    session_to_idx = {s: i for i, s in enumerate(all_sessions_prov)}

    def session_color(node):
        sess = G.nodes[node].get("session", "?")
        idx_val = session_to_idx.get(sess, 0)
        return session_cmap(idx_val / max(len(all_sessions_prov), 1))

    # Draw gate-informing scripts (larger, bold)
    if gate_scripts:
        colors = [session_color(n) for n in gate_scripts]
        nx.draw_networkx_nodes(G, pos, nodelist=gate_scripts, node_color=colors,
                                node_size=350, node_shape="h", alpha=0.9, ax=ax,
                                edgecolors="black", linewidths=2)
    # Draw regular scripts
    if regular_scripts:
        colors = [session_color(n) for n in regular_scripts]
        nx.draw_networkx_nodes(G, pos, nodelist=regular_scripts, node_color=colors,
                                node_size=200, node_shape="h", alpha=0.7, ax=ax)
    # Draw data nodes
    if data_nodes:
        colors = [session_color(n) for n in data_nodes]
        nx.draw_networkx_nodes(G, pos, nodelist=data_nodes, node_color=colors,
                                node_size=120, node_shape="D", alpha=0.6, ax=ax)
    # Draw gate reference nodes
    if gate_nodes:
        nx.draw_networkx_nodes(G, pos, nodelist=gate_nodes,
                                node_color=COLORS["gate"], node_size=300,
                                node_shape="s", alpha=0.9, ax=ax,
                                edgecolors="black", linewidths=1.5)

    # Labels for gates and gate-informing scripts
    important_labels = {}
    for n in gate_nodes:
        important_labels[n] = G.nodes[n].get("label", n)
    for n in gate_scripts:
        important_labels[n] = G.nodes[n].get("label", n)
    nx.draw_networkx_labels(G, pos, labels=important_labels,
                             font_size=6, font_weight="bold", ax=ax)

    # Legend
    legend_handles = [
        mpatches.Patch(color="#9b59b6", label=f"Scripts ({len(script_nodes)})"),
        mpatches.Patch(color="#3498db", label=f"Data files ({len(data_nodes)})"),
        mpatches.Patch(color=COLORS["gate"], label=f"Gates ({len(gate_nodes)})"),
    ]
    ax.legend(handles=legend_handles, loc="upper left", fontsize=10)

    stats_text = (f"Nodes: {G.number_of_nodes()}  |  "
                  f"Edges: {G.number_of_edges()}  |  "
                  f"Gate-linked scripts: {len(gate_scripts)}")
    ax.annotate(stats_text, xy=(0.99, 0.01), xycoords="axes fraction",
                 ha="right", va="bottom", fontsize=9, color="#7f8c8d")

    ax.axis("off")
    out = VIZ_DIR / "data_provenance.png"
    fig.savefig(out, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  [provenance] {out}  ({out.stat().st_size / 1024:.0f} KB)")
    return out


# ---------------------------------------------------------------------------
# --citations: Researcher Domain Map
# ---------------------------------------------------------------------------

def cmd_citations(idx: dict):
    """Generate the researcher citation network."""
    researchers = idx["researchers"]
    G = nx.Graph()

    # Add researcher nodes
    for r in researchers:
        G.add_node(
            r["domain"],
            paper_count=r.get("paper_count", 0),
            citation_count=r.get("citation_count", 0),
            description=r.get("description", ""),
            sessions=set(r.get("cited_in_sessions", [])),
        )

    # Connect domains that share session references
    domains = list(G.nodes())
    for i in range(len(domains)):
        for j in range(i + 1, len(domains)):
            d1, d2 = domains[i], domains[j]
            shared = G.nodes[d1]["sessions"] & G.nodes[d2]["sessions"]
            if shared:
                G.add_edge(d1, d2, weight=len(shared), shared=shared)

    # --- Layout ---
    pos = nx.spring_layout(G, k=3.0, iterations=150, seed=42)

    fig, ax = plt.subplots(figsize=(12, 10))
    ax.set_title("Researcher Domain Network", fontsize=16, fontweight="bold", pad=15)

    # Node sizes proportional to paper_count
    sizes = [G.nodes[n]["paper_count"] * 80 + 100 for n in G.nodes()]

    # Node colors by citation intensity
    cites = np.array([G.nodes[n]["citation_count"] for n in G.nodes()], dtype=float)
    max_cite = max(cites.max(), 1)
    colors_norm = cites / max_cite

    # Edge weights
    edge_weights = [G.edges[e].get("weight", 1) for e in G.edges()]
    max_w = max(edge_weights) if edge_weights else 1

    # Draw edges
    if edge_weights:
        widths = [0.5 + 3.0 * (w / max_w) for w in edge_weights]
        nx.draw_networkx_edges(G, pos, ax=ax, width=widths,
                                alpha=0.3, edge_color="#7f8c8d")

    # Draw nodes
    cmap = plt.cm.YlGnBu
    node_colors = [cmap(0.3 + 0.7 * c) for c in colors_norm]
    nx.draw_networkx_nodes(G, pos, node_size=sizes, node_color=node_colors,
                            alpha=0.85, ax=ax, edgecolors="#2c3e50", linewidths=1.5)

    # Labels
    labels = {n: f"{n}\n({G.nodes[n]['paper_count']}p, {G.nodes[n]['citation_count']}c)"
              for n in G.nodes()}
    nx.draw_networkx_labels(G, pos, labels=labels, font_size=8,
                             font_weight="bold", ax=ax)

    # Edge labels (shared session count)
    if edge_weights:
        edge_labels = {e: str(G.edges[e]["weight"]) for e in G.edges()
                       if G.edges[e]["weight"] > 1}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels,
                                      font_size=7, ax=ax)

    ax.annotate(f"{len(researchers)} domains  |  "
                f"{sum(r.get('paper_count', 0) for r in researchers)} papers  |  "
                f"{sum(r.get('citation_count', 0) for r in researchers)} cross-citations",
                xy=(0.99, 0.01), xycoords="axes fraction",
                ha="right", va="bottom", fontsize=9, color="#7f8c8d")

    ax.axis("off")
    out = VIZ_DIR / "researcher_citations.png"
    fig.savefig(out, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  [citations] {out}  ({out.stat().st_size / 1024:.0f} KB)")
    return out


# ---------------------------------------------------------------------------
# --gates: Gate Verdict Summary Table
# ---------------------------------------------------------------------------

def cmd_gates(idx: dict):
    """Generate the gate verdict visual table."""
    gates = idx["gates"]

    fig, ax = plt.subplots(figsize=(16, max(2, 0.7 * len(gates) + 1.5)))
    ax.set_title("Gate Verdicts Summary", fontsize=14, fontweight="bold", pad=10)
    ax.axis("off")

    headers = ["Gate ID", "Session", "Condition", "Result", "Verdict", "BF"]
    col_widths = [0.08, 0.07, 0.30, 0.30, 0.15, 0.10]
    col_x = [0.0]
    for w in col_widths[:-1]:
        col_x.append(col_x[-1] + w)

    n_rows = len(gates) + 1  # +1 for header
    row_height = 1.0 / (n_rows + 0.5)
    y_top = 0.95

    def get_verdict_color(verdict_str):
        v = verdict_str.upper()
        for key, color in VERDICT_COLORS.items():
            if key in v:
                return to_rgba(color, alpha=0.3)
        return to_rgba("#ecf0f1", alpha=0.3)

    # Header row
    for j, h in enumerate(headers):
        ax.text(col_x[j] + col_widths[j] / 2, y_top, h,
                ha="center", va="center", fontsize=10, fontweight="bold",
                transform=ax.transAxes,
                bbox=dict(boxstyle="round,pad=0.3", fc="#2c3e50", ec="none", alpha=0.9),
                color="white")

    # Data rows
    for i, g in enumerate(gates):
        y = y_top - (i + 1) * row_height - row_height * 0.3
        bg_color = get_verdict_color(g.get("verdict", ""))

        # Extract session from source_file (more reliable)
        session = extract_session_from_source(g.get("source_file", "")) or g.get("session", "?")
        bf_str = f"{g['bayes_factor']:.2f}" if g.get("bayes_factor") else "—"

        row_data = [
            g.get("id", "?"),
            session,
            truncate(g.get("condition", ""), 55),
            truncate(g.get("result", ""), 55),
            g.get("verdict", "?"),
            bf_str,
        ]

        for j, val in enumerate(row_data):
            fontweight = "bold" if j in (0, 4) else "normal"
            fontsize = 8 if j in (2, 3) else 9
            ax.text(col_x[j] + col_widths[j] / 2, y, val,
                    ha="center", va="center", fontsize=fontsize,
                    fontweight=fontweight, transform=ax.transAxes,
                    bbox=dict(boxstyle="round,pad=0.3", fc=bg_color, ec="#bdc3c7",
                              alpha=0.8))

    fig.tight_layout()
    out = VIZ_DIR / "gate_verdicts.png"
    fig.savefig(out, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  [gates] {out}  ({out.stat().st_size / 1024:.0f} KB)")
    return out


# ---------------------------------------------------------------------------
# --mermaid: Mermaid Diagram Generator
# ---------------------------------------------------------------------------

def cmd_mermaid(idx: dict):
    """Generate Mermaid flowchart code."""
    lines = ["graph TD"]
    lines.append("    %% Key Sessions")

    # Collect session IDs referenced by theorems and gates
    key_sessions = set()
    for t in idx["theorems"]:
        for sid in parse_sessions_field(t.get("sessions", "")):
            key_sessions.add(sid)
    for g in idx["gates"]:
        sid = extract_session_from_source(g.get("source_file", ""))
        if sid:
            key_sessions.add(sid)

    # Session nodes (subset)
    for sid in sorted(key_sessions, key=parse_session_order):
        if parse_session_order(sid) >= 0:
            safe_id = f"S{sid.replace('/', '_')}"
            lines.append(f"    {safe_id}[Session {sid}]")

    # Theorem nodes (deduplicated, skip artifacts)
    lines.append("    %% Proven Theorems")
    seen_theorems = set()
    theorem_nodes = []
    for t in idx["theorems"]:
        name = t["name"]
        if name.startswith(":--") or name.startswith("|"):
            continue
        name_key = re.sub(r"[^a-z0-9]", "", name.lower())[:30]
        if name_key in seen_theorems:
            continue
        seen_theorems.add(name_key)
        tid = t["id"].replace("proven_", "T")
        safe_name = truncate(name, 40).replace('"', "'")
        lines.append(f'    {tid}["{safe_name} ✓"]')
        theorem_nodes.append((tid, t))
        # Cap at ~20 theorems
        if len(theorem_nodes) >= 20:
            break

    # Gate nodes
    lines.append("    %% Gates")
    for g in idx["gates"]:
        gid = g["id"].replace(" ", "_").replace("(", "").replace(")", "")
        safe_name = g["id"]
        verdict = g.get("verdict", "")
        if any(kw in verdict.upper() for kw in ("KILL", "CLOSED", "CLOSURE")):
            lines.append("    " + gid + "{{" + safe_name + " CLOSED}}")
        elif "FAIL" in verdict.upper():
            lines.append("    " + gid + "{{" + safe_name + " FAIL}}")
        else:
            lines.append(f'    {gid}[{safe_name}]')

    # Closed Mechanism nodes (cap at ~15)
    lines.append("    %% Closed Mechanism")
    dead_nodes = []
    for dm in idx["closed_mechanisms"][:15]:
        did = dm["id"].replace("closed_", "DM")
        safe_name = truncate(dm["name"], 35).replace('"', "'")
        lines.append(f'    {did}("{safe_name} ✗")')
        dead_nodes.append((did, dm))

    # Edges: Session -> Theorem
    lines.append("    %% Session -> Theorem links")
    for tid, t in theorem_nodes:
        for sid in parse_sessions_field(t.get("sessions", "")):
            safe_sid = f"S{sid.replace('/', '_')}"
            if parse_session_order(sid) >= 0:
                lines.append(f"    {safe_sid} --> {tid}")

    # Edges: Gate -> Closed Mechanism
    lines.append("    %% Gate closes")
    for did, dm in dead_nodes:
        gate_id = dm.get("gate_id")
        if gate_id and gate_id != "None":
            gid = gate_id.replace(" ", "_").replace("(", "").replace(")", "")
            lines.append(f"    {gid} -->|closes| {did}")

    # Styling
    lines.append("    %% Styling")
    lines.append("    classDef proven fill:#2ecc71,stroke:#27ae60,color:#fff")
    lines.append("    classDef closed fill:#e74c3c,stroke:#c0392b,color:#fff")
    lines.append("    classDef gate fill:#f39c12,stroke:#e67e22,color:#fff")
    lines.append("    classDef session fill:#3498db,stroke:#2980b9,color:#fff")

    # Apply classes
    theorem_ids = [tid for tid, _ in theorem_nodes]
    if theorem_ids:
        lines.append(f"    class {','.join(theorem_ids)} proven")
    dead_ids = [did for did, _ in dead_nodes]
    if dead_ids:
        lines.append(f"    class {','.join(dead_ids)} closed")
    gate_ids = [g["id"].replace(" ", "_").replace("(", "").replace(")", "")
                for g in idx["gates"]]
    if gate_ids:
        lines.append(f"    class {','.join(gate_ids)} gate")
    session_ids = [f"S{sid.replace('/', '_')}" for sid in key_sessions
                   if parse_session_order(sid) >= 0]
    if session_ids:
        lines.append(f"    class {','.join(session_ids)} session")

    mermaid_code = "\n".join(lines)

    # Print to stdout
    print(mermaid_code)

    # Write to file
    out = VIZ_DIR / "knowledge_graph.mmd"
    out.write_text(mermaid_code, encoding="utf-8")
    print(f"\n  [mermaid] {out}  ({out.stat().st_size / 1024:.1f} KB)")
    return out


# ---------------------------------------------------------------------------
# --all: Run everything
# ---------------------------------------------------------------------------

def cmd_all(idx: dict):
    """Run all visualization subcommands."""
    print("Generating all visualizations...\n")
    outputs = []
    for name, func in [
        ("timeline",   cmd_timeline),
        ("gates",      cmd_gates),
        ("graph",      cmd_graph),
        ("provenance", cmd_provenance),
        ("citations",  cmd_citations),
        ("mermaid",    cmd_mermaid),
    ]:
        try:
            out = func(idx)
            outputs.append((name, out))
        except Exception as e:
            print(f"  [ERROR] {name}: {e}")
            outputs.append((name, None))

    print("\n" + "=" * 60)
    print("Summary:")
    print("=" * 60)
    for name, out in outputs:
        if out and out.exists():
            size = out.stat().st_size / 1024
            print(f"  {name:15s} → {out.name:35s} ({size:.0f} KB)")
        else:
            print(f"  {name:15s} → FAILED")
    print("=" * 60)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Knowledge visualization for the Phonon-Exflation project.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""\
            Examples:
              python visualize_knowledge.py --graph
              python visualize_knowledge.py --timeline
              python visualize_knowledge.py --all
        """),
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--graph", action="store_true",
                        help="Knowledge topology graph")
    group.add_argument("--timeline", action="store_true",
                        help="Probability trajectory chart")
    group.add_argument("--provenance", action="store_true",
                        help="Data flow/provenance graph")
    group.add_argument("--citations", action="store_true",
                        help="Researcher domain citation network")
    group.add_argument("--gates", action="store_true",
                        help="Gate verdict summary table")
    group.add_argument("--mermaid", action="store_true",
                        help="Mermaid diagram code")
    group.add_argument("--all", action="store_true",
                        help="Generate all visualizations")

    args = parser.parse_args()

    setup_output_dir()
    idx = load_index()

    if args.graph:
        cmd_graph(idx)
    elif args.timeline:
        cmd_timeline(idx)
    elif args.provenance:
        cmd_provenance(idx)
    elif args.citations:
        cmd_citations(idx)
    elif args.gates:
        cmd_gates(idx)
    elif args.mermaid:
        cmd_mermaid(idx)
    elif args.all:
        cmd_all(idx)


if __name__ == "__main__":
    main()
