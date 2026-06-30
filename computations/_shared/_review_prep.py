#!/usr/bin/env python3
"""
Re-Run Prep Tool — pulls top anchor scripts + MCP baselines into a pre-reg doc.

Produces _review_prep.md with one PRU pre-registration block per anchor script,
ready for GPU re-run once cluster review MAJOR/BLOCKER flags arrive.

For each of the top N anchors:
  1. SHA-256 of current source
  2. data_provenance rows from knowledge.db (what this script is known to produce)
  3. Proposed PRU block (scaffolded from .claude/templates/pru-pre-registration-template.md)
  4. Proposed re-run gate ID: <basename-upper>
  5. MCP queries the runner should make before touching the script

Read-only; does not modify the anchor scripts. Output is an advisory markdown doc.
"""

from __future__ import annotations

# Discipline: canonical_constants import required for all computation scripts
from canonical_constants import *  # noqa: F401,F403

import hashlib
import json
import re
import sqlite3
from pathlib import Path
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


PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'COMPUTATIONS_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
CANONICAL_AUDIT_JSON = resolve_script(None, '_canonical_audit_report.json')
KNOWLEDGE_DB = PROJECT_ROOT / "tools" / "knowledge.db"
OUT_MD = resolve_script(None, '_review_prep.md')

TOP_N = 40  # (local) number of anchors to prep


def sha256_head(path: Path) -> str:
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()[:16]
    except OSError:
        return "<unreadable>"


def provenance_rows_for(conn: sqlite3.Connection, script_basename: str) -> list[dict]:
    """Fetch every data_provenance row naming this script."""
    cur = conn.cursor()
    # script field may be a string, comma-joined list, or JSON array
    cur.execute(
        "SELECT session, name, inputs, outputs, gates_informed "
        "FROM data_provenance "
        "WHERE script LIKE ?",
        (f"%{script_basename}%",),
    )
    return [
        {"session": r[0], "name": r[1], "inputs": r[2], "outputs": r[3], "gates_informed": r[4]}
        for r in cur.fetchall()
    ]


def gates_for(conn: sqlite3.Connection, script_basename: str) -> list[dict]:
    """Fetch gate rows whose data_files list mentions this script."""
    cur = conn.cursor()
    cur.execute(
        "SELECT id, name, session, verdict, result, data_files "
        "FROM gates "
        "WHERE data_files LIKE ?",
        (f"%{script_basename}%",),
    )
    return [
        {"id": r[0], "name": r[1], "session": r[2], "verdict": r[3],
         "result": r[4], "data_files": r[5]}
        for r in cur.fetchall()
    ]


def propose_gate_id(script_basename: str) -> str:
    """Re-run gate ID = RERUN-<normalized-basename>."""
    stem = script_basename.rsplit(".", 1)[0]
    norm = re.sub(r"[^A-Za-z0-9]+", "-", stem).upper()
    return f"RERUN-{norm}"


def main() -> int:
    print(f"Reading {CANONICAL_AUDIT_JSON.name} ...")
    data = json.loads(CANONICAL_AUDIT_JSON.read_text(encoding="utf-8"))
    anchors = data.get("anchor_set", [])[:TOP_N]
    print(f"  top {len(anchors)} anchors selected")

    if not KNOWLEDGE_DB.exists():
        raise SystemExit(f"Knowledge DB missing: {KNOWLEDGE_DB}")

    conn = sqlite3.connect(str(KNOWLEDGE_DB))
    try:
        # Build per-anchor records
        blocks: list[str] = []
        n_with_gates = 0  # (local)
        n_with_provenance = 0  # (local)

        for i, a in enumerate(anchors, start=1):
            name = a["name"]
            path = a["path"]
            session = a["session_num"]
            sigs = []
            if a.get("cited_in_canon"): sigs.append("canon")
            if a.get("cited_in_registry"): sigs.append("reg")
            if a.get("cited_in_mcp"): sigs.append("mcp")
            if a.get("n_importers", 0) > 0: sigs.append(f"imp{a['n_importers']}")

            src_path = PROJECT_ROOT / path
            sha = sha256_head(src_path) if src_path.exists() else "<missing>"

            prov = provenance_rows_for(conn, name)
            gates = gates_for(conn, name)
            if prov: n_with_provenance += 1
            if gates: n_with_gates += 1

            gate_id = propose_gate_id(name)

            b = []
            b.append(f"### {i}. `{name}` — {gate_id}")
            b.append("")
            b.append(f"- **Session**: S{session}")
            b.append(f"- **Path**: `{path}`")
            b.append(f"- **Citation sigils**: {', '.join(sigs) if sigs else '(none)'}")
            b.append(f"- **Priority_anchor**: {a.get('priority_anchor', 0)}")
            b.append(f"- **Current source SHA-256** (head 16): `{sha}`")
            b.append(f"- **Level 1 grade**: {a.get('grade', '?')}")
            b.append(f"- **Ruff issues / hardcode / untagged**: "
                     f"{a.get('n_ruff_issues', 0)} / "
                     f"{a.get('n_hardcoded_canonical', 0)} / "
                     f"{a.get('n_untagged_literals', 0)}")
            b.append("")

            # Provenance rows
            if prov:
                b.append(f"**Data-provenance rows ({len(prov)}):**")
                for p in prov[:5]:
                    gates_i = p.get("gates_informed") or "-"
                    outs = p.get("outputs") or "-"
                    b.append(f"- {p['session']}: `{p['name']}` → gates_informed: `{gates_i}`; "
                             f"outputs: `{outs[:80]}`")
                if len(prov) > 5:
                    b.append(f"- ...and {len(prov) - 5} more")
                b.append("")
            else:
                b.append("**Data-provenance rows**: _none found in `knowledge.db`_")
                b.append("")

            # Gate rows
            if gates:
                b.append(f"**Gates referencing this script ({len(gates)}):**")
                for g in gates[:5]:
                    b.append(f"- `{g['id']}` ({g['session']}): {g['verdict']} — {g['name']}")
                    if g.get("result"):
                        b.append(f"  result: {str(g['result'])[:120]}")
                if len(gates) > 5:
                    b.append(f"- ...and {len(gates) - 5} more")
                b.append("")
            else:
                b.append("**Gates referencing this script**: _none_")
                b.append("")

            # MCP baseline actions
            b.append("**Level 3 runner's MCP baseline queries (fetch BEFORE modifying the script):**")
            b.append("```")
            if prov:
                for p in prov[:3]:
                    b.append(f'query_entity("sessions", "{p["session"]}")')
                    if p.get("name"):
                        b.append(f'trace_entity("{p["name"]}")')
            if gates:
                for g in gates[:3]:
                    b.append(f'query_entity("gates", "{g["id"]}")')
            # Always: look up any canonical output value
            b.append(f'search_knowledge("{name.rsplit(".", 1)[0]}")')
            b.append("```")
            b.append("")

            b.append("**Proposed PRU block** — fill the scaffold from "
                     "`.claude/templates/pru-pre-registration-template.md` with:")
            b.append("")
            b.append(f"```")
            b.append(f"Gate {gate_id} — Level 3 re-run of {name}")
            b.append(f"Trigger:            [VERIFY-THEOREM] (reproducibility under PRU+GPU)")
            b.append(f"Classification:     (carry from original script docstring)")
            b.append(f"Producing script:   {path}")
            b.append(f"Session:            S81 (Level 3 re-run wave)")
            b.append(f"Original SHA (head): {sha}")
            b.append(f"Target value:       <MCP-registered value from get_constant / query_entity>")
            b.append(f"Tolerance:          RATIO→0.5% | ABSOLUTE→5% | THEOREM→machine-ε")
            b.append(f"PASS iff:           |reproduced − MCP| / MCP ≤ tolerance")
            b.append(f"FAIL iff:           |reproduced − MCP| / MCP > 10·tolerance")
            b.append(f"Input pins:         canonical_constants.py + (list .npz inputs here)")
            b.append(f"GPU path:           torch.linalg for N≥100 eigvals/SVD/matmul; "
                     f"OMP_NUM_THREADS=8 otherwise")
            b.append(f"Output 4-tuple:     (value=<v>, scheme=<s>, convention=<c>, L_max=<L>)")
            b.append(f"```")
            b.append("")
            blocks.append("\n".join(b))

        # Header + summary
        header = [
            "# Level 3 Anchor Re-Run Prep",
            "",
            f"**Generated**: {CANONICAL_AUDIT_JSON.name} → {OUT_MD.name}",
            f"**Source anchor_set**: {len(data.get('anchor_set', []))} total, "
            f"top {len(anchors)} selected by `priority_anchor`",
            f"**Anchors with data_provenance rows**: {n_with_provenance} / {len(anchors)}",
            f"**Anchors with gate references**: {n_with_gates} / {len(anchors)}",
            "",
            "**Status**: awaiting Level 2 MAJOR/BLOCKER flags before GPU re-run. The list "
            "below is the prep-only input — no script is modified by this document.",
            "",
            "## Runner Protocol (per anchor)",
            "",
            "1. Read this prep block + the script + the PRU template "
            "(`.claude/templates/pru-pre-registration-template.md`).",
            "2. Run the MCP baseline queries listed in the anchor's block. Capture the "
            "registered value + provenance as the null hypothesis the re-run tests.",
            "3. Retrofit the script per PRU block: SHA-pin block (first 20 lines of stdout), "
            "4-tuple output tag, gate-verdict append line with SHA pin.",
            "4. GPU refactor per `.claude/rules/computation-environment.md` (torch.linalg for "
            "N≥100; OMP_NUM_THREADS=8 fallback).",
            "5. Single-run re-execute. Save .npz + .png + log.",
            "6. Compare reproduced value to MCP-registered. Tolerance:",
            "   - RATIO quantities: 0.5%",
            "   - ABSOLUTE quantities: 5%",
            "   - Structural theorems: machine ε",
            "7. On match: `update_constant(name, value, session=\"S81\", "
            "source=\"<script>\", comment=\"Level 3 re-run; SHA=<closure>\")`.",
            "8. On mismatch: do NOT update; write a row in the Level 3 verdict table and "
            "flag for human adjudication.",
            "",
            "## Anchor List",
            "",
        ]
        out = "\n".join(header) + "\n" + "\n\n".join(blocks) + "\n"
        OUT_MD.write_text(out, encoding="utf-8")
        print(f"Wrote {OUT_MD.name} ({OUT_MD.stat().st_size // 1024} KB)")
        print(f"  anchors with provenance: {n_with_provenance} / {len(anchors)}")
        print(f"  anchors with gates:      {n_with_gates} / {len(anchors)}")
    finally:
        conn.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
