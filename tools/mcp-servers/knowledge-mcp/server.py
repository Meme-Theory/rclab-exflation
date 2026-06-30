#!/usr/bin/env python3
"""
Knowledge MCP Server — Project Knowledge Base Access for Agents

Wraps the knowledge-index.json / knowledge.db and canonical_constants.py
so that every spawned agent can query settled results, gate verdicts,
closed mechanisms, and framework constants without needing the /weave skill.

Tools:
  search_knowledge     — FTS5 ranked search across all entity types
  query_entity         — Direct lookup by table and ID
  list_entities        — Show all entities of a given type
  trace_entity         — Evidence chain for a named entity
  get_constant         — Get a canonical constant with provenance
  list_constants       — List/filter canonical constants
  update_constant      — Add or update a constant in canonical_constants.py
  emit_verdict         — Append a gate verdict line (syntax-forced canonical schema,
                         cross-process file lock, sig_5 uniqueness) — the race-safe,
                         single-source replacement for open-coded append_verdict()
"""

# Suppress warnings before any imports — stderr noise breaks MCP stdio
import warnings
import os
warnings.filterwarnings("ignore")
os.environ["PYTHONWARNINGS"] = "ignore"

import asyncio
import json
import sqlite3
import re
import logging
import sys
import time
from pathlib import Path
from typing import Any, Optional

import mcp.server.stdio
import mcp.types as types
from mcp.server import Server

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

SERVER_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SERVER_DIR.parent.parent.parent  # tools/mcp-servers/knowledge-mcp -> root
INDEX_PATH = PROJECT_ROOT / "tools" / "knowledge-index.json"
DB_PATH = PROJECT_ROOT / "tools" / "knowledge.db"
CONSTANTS_PATH = PROJECT_ROOT / "computations/_shared" / "canonical_constants.py"
USAGE_COUNTER_PATH = SERVER_DIR / "usage_counter.json"

# Logging — to file, not stderr
_log_path = SERVER_DIR / "knowledge_mcp.log"
logging.basicConfig(level=logging.INFO, filename=str(_log_path), filemode='w',
                    format='%(asctime)s %(name)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Server
# ---------------------------------------------------------------------------

server = Server("knowledge-base")

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _bump_counter(tool_name: str) -> None:
    """Increment per-tool and total usage counters. Silent on I/O error."""
    import datetime as _dt
    try:
        if USAGE_COUNTER_PATH.exists():
            with open(USAGE_COUNTER_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)
        else:
            data = {
                "started_at": _dt.datetime.utcnow().isoformat() + "Z",
                "total_calls": 0,
                "by_tool": {},
            }
        now = _dt.datetime.utcnow().isoformat() + "Z"
        data["total_calls"] = int(data.get("total_calls", 0)) + 1
        by_tool = data.setdefault("by_tool", {})
        entry = by_tool.setdefault(tool_name, {"count": 0, "last_called": None})
        entry["count"] = int(entry.get("count", 0)) + 1
        entry["last_called"] = now
        data["last_called"] = now
        tmp = USAGE_COUNTER_PATH.with_suffix(".json.tmp")
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        os.replace(tmp, USAGE_COUNTER_PATH)
    except Exception:
        logger.exception("usage_counter bump failed for %s", tool_name)


def _get_db() -> sqlite3.Connection:
    """Open the knowledge SQLite database."""
    if not DB_PATH.exists():
        raise FileNotFoundError(
            f"Knowledge DB not found at {DB_PATH}. Run /weave --db-sync first."
        )
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    return conn


def _load_index() -> dict:
    """Load the knowledge-index.json."""
    if not INDEX_PATH.exists():
        raise FileNotFoundError(f"Index not found at {INDEX_PATH}. Run /weave --update.")
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


TABLE_MAP = {
    "theorems": "theorems", "theorem": "theorems",
    "closed": "closed_mechanisms", "closed_mechanisms": "closed_mechanisms",
    "gates": "gates", "gate": "gates",
    "sessions": "sessions", "session": "sessions",
    "provenance": "data_provenance", "data_provenance": "data_provenance",
    "open": "open_channels", "open_channels": "open_channels",
    "researchers": "researchers", "researcher": "researchers",
    "trajectory": "probability_trajectory",
    "equations": "equations", "equation": "equations",
    "edges": "edges", "edge": "edges",  # S81: tagged-link relation edges
    "classes": "classes", "class": "classes",  # S86: canonical_classes
}

PK_COLS = {
    "theorems": "id", "closed_mechanisms": "id", "gates": "id",
    "sessions": "id", "researchers": "domain",
    "probability_trajectory": "session",
    "data_provenance": "name", "open_channels": "name",
    "equations": "id",
    "edges": "id",  # S81: edge_N
    "classes": "id",  # S86: canonical_classes
}


def _parse_constants_module() -> dict:
    """Parse canonical_constants.py via regex — no exec, no hanging."""
    if not CONSTANTS_PATH.exists():
        raise FileNotFoundError(f"canonical_constants.py not found at {CONSTANTS_PATH}")

    with open(CONSTANTS_PATH, "r", encoding="utf-8") as f:
        source = f.read()

    # --- Extract simple assignments: name = value  # comment ---
    # Matches: name = 1.23e-4, name = 0.190, name = 42, name = "string"
    assign_re = re.compile(
        r'^([A-Za-z_]\w*)\s*=\s*'           # name =
        r'(-?[\d]+(?:\.[\d]*)?(?:[eE][+-]?\d+)?)'  # numeric value
        r'\s*(?:#.*)?$',                      # optional comment
        re.MULTILINE
    )
    constants = {}
    for m in assign_re.finditer(source):
        name, val_str = m.group(1), m.group(2)
        if name.startswith("_") or name in ("PI",):
            continue
        try:
            constants[name] = float(val_str)
        except ValueError:
            pass

    # --- Pass 2: Alias assignments (name = other_name) ---
    # Matches: E_cond = E_cond_ED_8mode, M_KK = M_KK_gravity, Delta_BCS = Delta_0_OES
    alias_re = re.compile(
        r'^([A-Za-z_]\w*)\s*=\s*([A-Za-z_]\w*)\s*(?:#.*)?$',
        re.MULTILINE
    )
    aliases = {}  # alias_name -> target_name
    for m in alias_re.finditer(source):
        alias_name, target_name = m.group(1), m.group(2)
        if alias_name.startswith("_") or alias_name in ("PI", "PROVENANCE"):
            continue
        # Skip if it's a known non-constant (imports, builtins, modules)
        if target_name in ("np", "numpy", "sys", "warnings", "True", "False", "None"):
            continue
        aliases[alias_name] = target_name

    # Resolve alias chains: E_cond -> E_cond_ED_8mode -> (numeric value)
    for alias_name, target in aliases.items():
        if target in constants and alias_name not in constants:
            constants[alias_name] = constants[target]
        elif target in aliases and aliases[target] in constants:
            constants[alias_name] = constants[aliases[target]]

    # --- Pass 3: Derived expressions where all operands are already parsed ---
    # Catches: R_protected_fold = a0_fold * a4_fold / a2_fold**2
    #          Omega_DM = Omega_m - Omega_b
    #          T_CMB_GeV = T_CMB * k_B / 1e9
    import math
    expr_re = re.compile(
        r'^([A-Za-z_]\w*)\s*=\s*(.+?)\s*(?:#.*)?$',
        re.MULTILINE
    )
    safe_ns = {**constants, "np": type("np", (), {"pi": math.pi}), "PI": math.pi}
    for m in expr_re.finditer(source):
        name, expr = m.group(1), m.group(2).strip()
        if name in constants or name.startswith("_"):
            continue
        if name in ("PROVENANCE", "Path", "DATA_DIR", "warnings", "sys", "np"):
            continue
        # Only evaluate if the expression contains known constants or numbers
        # and basic operators (no function calls, imports, etc.)
        if any(c in expr for c in ("import", "open(", "exec", "__", "print")):
            continue
        try:
            val = eval(expr, {"__builtins__": {}}, safe_ns)
            if isinstance(val, (int, float)):
                constants[name] = float(val)
        except Exception:
            pass

    # --- Pass 4: Re-resolve aliases against the post-Pass-3 constants dict ---
    # Pass 2's resolution ran BEFORE Pass 3, so aliases pointing to derived
    # expressions (e.g., alpha_s_framework_central = alpha_s_inflation_framework
    # where alpha_s_inflation_framework is computed as n_s_canon**2 - 1) couldn't
    # resolve. Re-run with fixed-point iteration so that multi-level alias chains
    # eventually pointing into derived values all converge. The depth cap is a
    # safety net against pathological cycles (Python would NameError on cycles
    # at module load, but this regex parser doesn't validate the source).
    for _ in range(8):
        progress = False
        for alias_name, target in aliases.items():
            if alias_name in constants:
                continue
            # Direct: alias -> already-resolved (numeric or derived) value
            if target in constants:
                constants[alias_name] = constants[target]
                progress = True
            # One-hop: alias -> alias -> resolved value
            elif target in aliases and aliases[target] in constants:
                constants[alias_name] = constants[aliases[target]]
                progress = True
        if not progress:
            break

    # --- Extract PROVENANCE dict ---
    provenance = {}
    prov_start = source.find("PROVENANCE = {")
    if prov_start >= 0:
        # Find matching closing brace
        brace_depth = 0
        prov_text = ""
        for i in range(prov_start, len(source)):
            c = source[i]
            if c == '{':
                brace_depth += 1
            elif c == '}':
                brace_depth -= 1
                if brace_depth == 0:
                    prov_text = source[prov_start:i+1]
                    break

        if prov_text:
            # Clean up for JSON-ish parsing: replace Python dict syntax
            # Extract individual entries via regex
            entry_re = re.compile(
                r'"(\w+)":\s*\{([^}]+)\}',
                re.DOTALL
            )
            for em in entry_re.finditer(prov_text):
                name = em.group(1)
                body = em.group(2)
                entry = {}
                # Extract key-value pairs
                kv_re = re.compile(r'"(\w+)":\s*(?:"([^"]*)"|(None|True|False)|([\d.eE+-]+))')
                for kv in kv_re.finditer(body):
                    key = kv.group(1)
                    if kv.group(2) is not None:
                        entry[key] = kv.group(2)
                    elif kv.group(3) is not None:
                        val = kv.group(3)
                        entry[key] = None if val == "None" else val == "True"
                    elif kv.group(4) is not None:
                        try:
                            entry[key] = float(kv.group(4))
                        except ValueError:
                            entry[key] = kv.group(4)
                # Extract note field (may contain quotes)
                note_re = re.compile(r'"note":\s*"((?:[^"\\]|\\.)*)"')
                nm = note_re.search(body)
                if nm:
                    entry["note"] = nm.group(1)
                provenance[name] = entry

    return constants, provenance


# ---------------------------------------------------------------------------
# Tool definitions
# ---------------------------------------------------------------------------

@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="search_knowledge",
            description=(
                "FTS5 ranked search across ALL knowledge entities (theorems, "
                "closed mechanisms, gates, sessions, equations, etc.). "
                "Use this BEFORE computing anything to check if a result is already known."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search query (supports FTS5 syntax: AND, OR, NOT, quotes for phrases)"
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Max results (default 20)",
                        "default": 20
                    }
                },
                "required": ["query"]
            }
        ),
        types.Tool(
            name="query_entity",
            description=(
                "Look up a specific entity by table and ID. "
                "Tables: theorems, closed, gates, sessions, provenance, open, researchers, equations."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "table": {
                        "type": "string",
                        "description": "Entity table (theorems, closed, gates, sessions, provenance, open, researchers, equations)"
                    },
                    "entity_id": {
                        "type": "string",
                        "description": "Entity ID or name to look up (supports partial match)"
                    }
                },
                "required": ["table", "entity_id"]
            }
        ),
        types.Tool(
            name="list_entities",
            description=(
                "List all entities of a given type. "
                "Types: theorems, closed, gates, trajectory, open, researchers, sessions."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "entity_type": {
                        "type": "string",
                        "description": "Entity type to list"
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Max results (default 50)",
                        "default": 50
                    }
                },
                "required": ["entity_type"]
            }
        ),
        types.Tool(
            name="trace_entity",
            description=(
                "Trace an entity across all knowledge types — find every mention "
                "of a name/concept in theorems, gates, closed mechanisms, sessions, etc. "
                "Returns an evidence chain showing how findings connect."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Entity name or concept to trace (e.g. 'BCS', 'monotonic', 'tau stabilization')"
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Max results per entity type (default 10)",
                        "default": 10
                    }
                },
                "required": ["name"]
            }
        ),
        types.Tool(
            name="get_constant",
            description=(
                "Get a canonical constant's value and full provenance (session, source, gate, notes). "
                "Use this to check the current authoritative value before hardcoding anything."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Constant name (e.g. 'tau_fold', 'M_KK_gravity', 'Delta_BCS')"
                    }
                },
                "required": ["name"]
            }
        ),
        types.Tool(
            name="list_constants",
            description=(
                "List canonical constants, optionally filtered by a pattern. "
                "Returns name, value, and session provenance for each."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "pattern": {
                        "type": "string",
                        "description": "Filter pattern (regex, case-insensitive). Empty = list all.",
                        "default": ""
                    },
                    "section": {
                        "type": "string",
                        "description": "Filter by section: PDG, geometric, BCS, spectral, transit, cosmological, acoustic, observation",
                        "default": ""
                    }
                }
            }
        ),
        types.Tool(
            name="update_constant",
            description=(
                "Add or update a canonical constant in canonical_constants.py. "
                "Appends to the appropriate section with full provenance comment. "
                "NEVER use this to overwrite existing constants without explicit user approval."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Constant name (Python identifier)"
                    },
                    "value": {
                        "type": "string",
                        "description": "Value as a Python expression (e.g. '7.43e16', '0.190', '2.776e3')"
                    },
                    "session": {
                        "type": "string",
                        "description": "Session where this was established (e.g. 'S77')"
                    },
                    "source": {
                        "type": "string",
                        "description": "Source file or derivation (e.g. 's77_equil_tau_bcs.npz')"
                    },
                    "gate": {
                        "type": "string",
                        "description": "Gate ID if applicable (e.g. 'S77-A1-EQUIL-TAU'). Null if none.",
                        "default": ""
                    },
                    "comment": {
                        "type": "string",
                        "description": "Brief description comment for the assignment line"
                    },
                    "section_label": {
                        "type": "string",
                        "description": "Which section to append to (e.g. 'SECTION B', 'SECTION C', 'SECTION D')",
                        "default": "SECTION E"
                    }
                },
                "required": ["name", "value", "session", "source", "comment"]
            }
        ),
        types.Tool(
            name="list_classes",
            description=(
                "List canonical classes (constant groupings — e.g. CC, KK, "
                "alpha_s hierarchy, fold transit complex). Each class is a "
                "named grouping of related constants defined in "
                "computations/canonical_classes.py. Optional filters: "
                "pattern (regex on id/name), tier (max nest depth: 0=root only)."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "pattern": {
                        "type": "string",
                        "description": "Filter pattern (regex, case-insensitive on id and name). Empty = list all.",
                        "default": ""
                    },
                    "max_tier": {
                        "type": "integer",
                        "description": "Show only classes with tier <= max_tier (0 = root classes only). Default: show all tiers.",
                        "default": -1
                    }
                }
            }
        ),
        types.Tool(
            name="query_class",
            description=(
                "Get full details for a class: metadata (description, tier, "
                "parent), member constants with roles (PRIMARY/DERIVED/RELATED), "
                "current values from canonical_constants, and any sub-classes. "
                "This is the forward lookup — given a class, what's in it?"
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "class_id": {
                        "type": "string",
                        "description": "Class ID (e.g. 'CC', 'KK', 'alpha_s_inflation', 'fold')"
                    }
                },
                "required": ["class_id"]
            }
        ),
        types.Tool(
            name="get_constant_classes",
            description=(
                "Reverse lookup: given a constant name, return all classes "
                "that contain it (and the role — PRIMARY, DERIVED, or RELATED — "
                "the constant plays in each class). Use to discover topical "
                "groupings a constant belongs to."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "constant_id": {
                        "type": "string",
                        "description": "Constant name (e.g. 'CC_ratio', 'M_KK', 'tau_fold', 'alpha_s_inflation_framework')"
                    }
                },
                "required": ["constant_id"]
            }
        ),
        types.Tool(
            name="emit_verdict",
            description=(
                "Append a gate verdict line to computations/session-{N}/s{N}_gate_verdicts.txt "
                "(session track; default) OR computations/investigation-{n}/inv{n}_gate_verdicts.txt "
                "(investigation track — pass track='investigation') "
                "with a SYNTAX-FORCED canonical schema, a cross-process file lock, and "
                "sig_5 (audit_sha256) uniqueness — the race-safe, single-source verdict "
                "emission path that replaces open-coded append_verdict() in scripts. "
                "Your producing script computes the two SHAs (it holds the input-pin map "
                "and content target); this tool enforces the line grammar, serializes the "
                "append behind a lockfile, rejects duplicate/copy-pasted SHAs, and writes "
                "the canonical line + dual-SHA companion + (for [SIGN] gates) the 3-tuple "
                "row. Pass the RAW value payload (no surrounding value='' — the tool wraps it)."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "session": {
                        "type": ["integer", "string"],
                        "description": "Unit number — session N (session track) or investigation n (investigation track). Numeric or letter-suffixed (e.g. 99, '100a', 2); resolves the canonical verdict file for the chosen track."
                    },
                    "track": {
                        "type": "string",
                        "enum": ["session", "investigation"],
                        "default": "session",
                        "description": "Verdict-ledger track. 'session' (default) -> computations/session-{N}/s{N}_gate_verdicts.txt. 'investigation' -> computations/investigation-{n}/inv{n}_gate_verdicts.txt (the parallel investigation pipeline; gate-verdicts.md §'Investigation-Track Canonical Path')."
                    },
                    "gate_id": {
                        "type": "string",
                        "description": "Canonical gate ID, e.g. 'S98-W1-ROUTE-RECONCILIATION'",
                        "pattern": "^[A-Za-z0-9][A-Za-z0-9._-]*$"
                    },
                    "verdict": {
                        "type": "string",
                        "enum": ["PASS", "FAIL", "INFO", "PRE-REG-INC"],
                        "description": "Composite verdict (collapse rule applied by the script before emit)"
                    },
                    "value": {
                        "type": "string",
                        "description": "Raw value payload (no surrounding quotes; no single-quote chars). The tool wraps it as value='...'"
                    },
                    "scheme": {"type": "string", "description": "scheme= field"},
                    "convention": {"type": "string", "description": "convention= field"},
                    "l_max": {"type": "string", "description": "L_max= field (e.g. '12', 'N/A')"},
                    "audit_sha256": {
                        "type": "string",
                        "pattern": "^[a-f0-9]{64}$",
                        "description": "Full 64-char audit closure SHA (computed by the script from the input-pin map)"
                    },
                    "content_sha256": {
                        "type": "string",
                        "pattern": "^[a-f0-9]{64}$",
                        "description": "Full 64-char content SHA"
                    },
                    "schema_version": {"type": "string", "default": "S84+"},
                    "companion_note": {
                        "type": "string",
                        "description": "Optional extra text appended to the dual-SHA companion row",
                        "default": ""
                    },
                    "sign_verdict": {
                        "type": "string",
                        "enum": ["PASS", "FAIL", "N/A"],
                        "description": "[SIGN] gates ONLY — required together with magnitude_verdict + regime_verdict",
                        "default": ""
                    },
                    "magnitude_verdict": {
                        "type": "string",
                        "enum": ["PASS", "INFO", "FAIL"],
                        "default": ""
                    },
                    "regime_verdict": {
                        "type": "string",
                        "enum": ["VALID", "MARGINAL", "BREAKDOWN"],
                        "default": ""
                    },
                    "three_tuple_note": {
                        "type": "string",
                        "description": "Optional extra text appended to the 3-tuple row",
                        "default": ""
                    },
                    "extra_rows": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Optional additional companion comment rows (each MUST start with '#'): EMERGENCE-1 detail, regulator_pin row, etc.",
                        "default": []
                    },
                    "supersedes": {
                        "type": "string",
                        "description": "Option-A correction only: full 64-hex audit_sha256 this line supersedes (allows re-emitting a corrected verdict for a gate that already has a line)",
                        "default": ""
                    }
                },
                "required": ["session", "gate_id", "verdict", "value", "scheme",
                             "convention", "l_max", "audit_sha256", "content_sha256"]
            }
        ),
        types.Tool(
            name="usage_stats",
            description=(
                "Return the knowledge MCP usage counter: total calls, per-tool counts, "
                "and last-called timestamps. Counter persists across server restarts "
                "at tools/mcp-servers/knowledge-mcp/usage_counter.json. "
                "Delete that file to reset."
            ),
            inputSchema={
                "type": "object",
                "properties": {},
            }
        ),
    ]


# ---------------------------------------------------------------------------
# Tool implementations
# ---------------------------------------------------------------------------

@server.call_tool()
async def handle_call_tool(name: str, arguments: dict | None) -> list[types.TextContent]:
    args = arguments or {}
    _bump_counter(name)
    try:
        if name == "search_knowledge":
            return await _search_knowledge(args)
        elif name == "query_entity":
            return await _query_entity(args)
        elif name == "list_entities":
            return await _list_entities(args)
        elif name == "trace_entity":
            return await _trace_entity(args)
        elif name == "get_constant":
            return await _get_constant(args)
        elif name == "list_constants":
            return await _list_constants(args)
        elif name == "update_constant":
            return await _update_constant(args)
        elif name == "list_classes":
            return await _list_classes(args)
        elif name == "query_class":
            return await _query_class(args)
        elif name == "get_constant_classes":
            return await _get_constant_classes(args)
        elif name == "emit_verdict":
            return await _emit_verdict(args)
        elif name == "usage_stats":
            return await _usage_stats(args)
        else:
            return [types.TextContent(type="text", text=f"Unknown tool: {name}")]
    except Exception as e:
        logger.exception(f"Error in tool {name}")
        return [types.TextContent(type="text", text=f"Error: {e}")]


async def _search_knowledge(args: dict) -> list[types.TextContent]:
    query = args["query"]
    limit = args.get("limit", 20)

    conn = _get_db()
    cur = conn.cursor()

    # FTS5: spaces = implicit AND (very strict). If no explicit operators,
    # convert to OR for broader matching. Users can still use AND/OR/NOT explicitly.
    fts_query = query
    has_operators = any(op in query.upper() for op in (" AND ", " OR ", " NOT ", '"'))
    if not has_operators and " " in query:
        fts_query = " OR ".join(query.split())

    try:
        cur.execute(
            """
            SELECT entity_type, entity_id, name, content, source_file,
                   bm25(knowledge_fts) AS rank
            FROM knowledge_fts
            WHERE knowledge_fts MATCH ?
            ORDER BY rank
            LIMIT ?
            """,
            (fts_query, limit),
        )
        rows = cur.fetchall()
    except Exception:
        # Fallback: quote each term
        terms = query.split()
        fts_query = " OR ".join(f'"{t}"' for t in terms)
        cur.execute(
            """
            SELECT entity_type, entity_id, name, content, source_file,
                   bm25(knowledge_fts) AS rank
            FROM knowledge_fts
            WHERE knowledge_fts MATCH ?
            ORDER BY rank
            LIMIT ?
            """,
            (fts_query, limit),
        )
        rows = cur.fetchall()

    conn.close()

    if not rows:
        return [types.TextContent(type="text", text=f"No results for '{query}'")]

    lines = [f"## Search: '{query}' — {len(rows)} results\n"]
    grouped = {}
    for row in rows:
        etype = row["entity_type"]
        if etype not in grouped:
            grouped[etype] = []
        grouped[etype].append(row)

    for etype, entries in grouped.items():
        lines.append(f"### [{etype}] ({len(entries)} hits)\n")
        for entry in entries:
            name_display = entry["name"] or entry["entity_id"] or "(unnamed)"
            content_short = (entry["content"] or "")[:300].replace("\n", " ")
            lines.append(f"**{name_display}**")
            lines.append(f"  {content_short}")
            if entry["source_file"]:
                lines.append(f"  _src: {Path(entry['source_file']).name}_")
            lines.append("")

    return [types.TextContent(type="text", text="\n".join(lines))]


async def _query_entity(args: dict) -> list[types.TextContent]:
    table = args["table"]
    entity_id = args["entity_id"]

    tbl = TABLE_MAP.get(table.lower())
    if not tbl:
        return [types.TextContent(type="text",
                text=f"Unknown table: {table}. Available: {', '.join(sorted(set(TABLE_MAP.values())))}")]

    pk = PK_COLS.get(tbl, "id")
    conn = _get_db()
    cur = conn.cursor()

    # Exact match first, then LIKE on PK, then LIKE on name column
    cur.execute(f"SELECT * FROM {tbl} WHERE {pk} = ?", (entity_id,))
    rows = cur.fetchall()
    if not rows:
        cur.execute(f"SELECT * FROM {tbl} WHERE {pk} LIKE ?", (f"%{entity_id}%",))
        rows = cur.fetchall()
    if not rows:
        # Try name column if it exists (most tables have one)
        name_col = "name" if tbl not in ("researchers", "probability_trajectory", "equations") else None
        if name_col:
            try:
                cur.execute(f"SELECT * FROM {tbl} WHERE {name_col} LIKE ?", (f"%{entity_id}%",))
                rows = cur.fetchall()
            except sqlite3.OperationalError:
                pass  # table doesn't have a name column
    conn.close()

    if not rows:
        return [types.TextContent(type="text",
                text=f"No entity found in {tbl} matching '{entity_id}'")]

    lines = [f"## {tbl} / {entity_id} — {len(rows)} result(s)\n"]
    for row in rows:
        for key in row.keys():
            val = row[key]
            if val is not None and str(val).strip():
                lines.append(f"**{key}**: {val}")
        lines.append("---")

    return [types.TextContent(type="text", text="\n".join(lines))]


async def _list_entities(args: dict) -> list[types.TextContent]:
    entity_type = args["entity_type"]
    limit = args.get("limit", 50)

    tbl = TABLE_MAP.get(entity_type.lower())
    if not tbl:
        return [types.TextContent(type="text",
                text=f"Unknown type: {entity_type}. Available: theorems, closed, gates, sessions, trajectory, open, researchers, equations, edges")]

    conn = _get_db()
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {tbl} LIMIT ?", (limit,))
    rows = cur.fetchall()
    conn.close()

    if not rows:
        return [types.TextContent(type="text", text=f"No entities in {tbl}")]

    # Build a compact table
    keys = rows[0].keys()
    lines = [f"## {tbl} — {len(rows)} entries\n"]
    lines.append("| " + " | ".join(keys) + " |")
    lines.append("| " + " | ".join(["---"] * len(keys)) + " |")
    for row in rows:
        vals = []
        for k in keys:
            v = str(row[k] or "")[:80]
            v = v.replace("|", "/").replace("\n", " ")
            vals.append(v)
        lines.append("| " + " | ".join(vals) + " |")

    return [types.TextContent(type="text", text="\n".join(lines))]


async def _trace_entity(args: dict) -> list[types.TextContent]:
    name = args["name"]
    limit = args.get("limit", 10)

    conn = _get_db()
    cur = conn.cursor()

    # Search across all FTS content
    try:
        cur.execute(
            """
            SELECT entity_type, entity_id, name, content, source_file,
                   bm25(knowledge_fts) AS rank
            FROM knowledge_fts
            WHERE knowledge_fts MATCH ?
            ORDER BY rank
            LIMIT ?
            """,
            (name, limit * 5),
        )
        rows = cur.fetchall()
    except sqlite3.OperationalError:
        # FTS query syntax error — try quoting
        cur.execute(
            """
            SELECT entity_type, entity_id, name, content, source_file,
                   bm25(knowledge_fts) AS rank
            FROM knowledge_fts
            WHERE knowledge_fts MATCH ?
            ORDER BY rank
            LIMIT ?
            """,
            (f'"{name}"', limit * 5),
        )
        rows = cur.fetchall()

    # S86: direct class-membership enrichment. The FTS search picks up class
    # entries by description/name, but for an exact constant-id like "CC_ratio"
    # or class-id like "alpha_s_inflation" we want the direct class_edges
    # relationships (which are NOT in FTS — class_edges is index-only).
    class_member_of = []   # name appears as tgt in a contains-edge
    class_contains = []    # name appears as src in a contains-edge
    parent_class = None    # name's parent class (if name is itself a class)
    sub_classes = []       # name's sub-classes (if name is itself a class)
    try:
        # As a constant: which classes contain it?
        cur.execute(
            "SELECT ce.src AS class_id, c.name AS class_name, ce.role, ce.comment "
            "FROM class_edges ce LEFT JOIN classes c ON ce.src = c.id "
            "WHERE ce.type = 'contains' AND ce.tgt_type = 'constants' AND ce.tgt = ? "
            "ORDER BY CASE ce.role "
            "  WHEN 'PRIMARY' THEN 0 WHEN 'DERIVED' THEN 1 WHEN 'RELATED' THEN 2 "
            "  ELSE 3 END",
            (name,),
        )
        class_member_of = cur.fetchall()

        # As a class: what does it contain (members) and what is its parent?
        cur.execute(
            "SELECT tgt, role, comment FROM class_edges "
            "WHERE src = ? AND type = 'contains' AND tgt_type = 'constants' "
            "ORDER BY CASE role "
            "  WHEN 'PRIMARY' THEN 0 WHEN 'DERIVED' THEN 1 WHEN 'RELATED' THEN 2 "
            "  ELSE 3 END",
            (name,),
        )
        class_contains = cur.fetchall()
        cur.execute("SELECT parent_id FROM classes WHERE id = ?", (name,))
        pr = cur.fetchone()
        if pr and pr["parent_id"]:
            parent_class = pr["parent_id"]
        cur.execute(
            "SELECT id, name FROM classes WHERE parent_id = ? ORDER BY id",
            (name,),
        )
        sub_classes = cur.fetchall()
    except sqlite3.OperationalError:
        # class_edges / classes tables don't exist — older DB. Silent skip.
        pass

    conn.close()

    if (not rows and not class_member_of and not class_contains
            and not parent_class and not sub_classes):
        return [types.TextContent(type="text", text=f"No trace found for '{name}'")]

    lines = [f"## Evidence Chain: '{name}'\n"]

    # --- Direct class connections (exact-match, S86+) ---
    # Surfaced first because they are exact relationships, not FTS-ranked
    # similarity. FTS picks up resemblance; this picks up membership.
    if class_member_of:
        lines.append(f"### class memberships ({len(class_member_of)} hits — '{name}' is a constant in these classes)")
        for r in class_member_of:
            comment = (r["comment"] or "").replace("\n", " ")[:150]
            lines.append(f"- **{r['class_name'] or r['class_id']}** "
                         f"[{r['class_id']}] role={r['role']}: {comment}")
        lines.append("")

    if class_contains:
        lines.append(f"### class membership: '{name}' contains ({len(class_contains)} constants)")
        for r in class_contains:
            comment = (r["comment"] or "").replace("\n", " ")[:120]
            lines.append(f"- **{r['tgt']}** role={r['role']}: {comment}")
        lines.append("")

    if parent_class or sub_classes:
        lines.append(f"### class hierarchy")
        if parent_class:
            lines.append(f"- parent: **{parent_class}**")
        if sub_classes:
            lines.append(f"- sub-classes ({len(sub_classes)}):")
            for sc in sub_classes:
                lines.append(f"  - **{sc['id']}**: {sc['name']}")
        lines.append("")

    # --- FTS-based evidence chain (existing behavior) ---
    grouped = {}
    for row in rows:
        etype = row["entity_type"]
        if etype not in grouped:
            grouped[etype] = []
        if len(grouped[etype]) < limit:
            grouped[etype].append(row)

    # 'class' added to the display order so FTS class hits surface even when
    # the direct class_edges lookup returns nothing (e.g. fuzzy / multi-word
    # name queries that match a class description but no exact id).
    for etype in ["class", "theorem", "gate", "closed_mechanism", "session",
                  "provenance", "open_channel", "trajectory", "researcher",
                  "equation"]:
        entries = grouped.get(etype, [])
        if not entries:
            continue
        lines.append(f"### {etype} ({len(entries)} hits)")
        for entry in entries:
            eid = entry["entity_id"] or ""
            ename = entry["name"] or ""
            content = (entry["content"] or "")[:200].replace("\n", " ")
            lines.append(f"- **{ename}** [{eid}]: {content}")
        lines.append("")

    return [types.TextContent(type="text", text="\n".join(lines))]


async def _get_constant(args: dict) -> list[types.TextContent]:
    name = args["name"]
    constants, provenance = _parse_constants_module()

    def _format_constant(cname, val, prov):
        lines = [f"## Constant: {cname}\n"]
        lines.append(f"**Value**: {val}")
        if prov:
            lines.append(f"**Session**: {prov.get('session', 'unknown')}")
            lines.append(f"**Source**: {prov.get('source', 'unknown')}")
            lines.append(f"**Gate**: {prov.get('gate', 'None')}")
            lines.append(f"**Superseded**: {prov.get('superseded', False)}")
            if prov.get("R_protected"):
                lines.append("**R-Protected**: YES")
            if prov.get("note"):
                lines.append(f"**Note**: {prov['note']}")
        else:
            lines.append("_No PROVENANCE entry (PDG/CODATA or needs to be added)_")
        return lines

    # Exact match in constants dict
    if name in constants:
        prov = provenance.get(name, {})
        return [types.TextContent(type="text",
                text="\n".join(_format_constant(name, constants[name], prov)))]

    # Has provenance but value not parsed (complex alias or expression)
    if name in provenance:
        prov = provenance[name]
        # Try to resolve via source hint (e.g., "alias for E_cond_ED_8mode")
        alias_target = None
        src = prov.get("source", "")
        if "alias for " in src:
            target_name = src.split("alias for ")[1].strip()
            if target_name in constants:
                alias_target = target_name
        lines = [f"## Constant: {name}\n"]
        if alias_target:
            lines.append(f"**Value**: {constants[alias_target]} (alias for {alias_target})")
        else:
            lines.append("**Value**: _(not directly parsed — check canonical_constants.py)_")
        lines.append(f"**Session**: {prov.get('session', 'unknown')}")
        lines.append(f"**Source**: {prov.get('source', 'unknown')}")
        lines.append(f"**Gate**: {prov.get('gate', 'None')}")
        lines.append(f"**Superseded**: {prov.get('superseded', False)}")
        if prov.get("R_protected"):
            lines.append("**R-Protected**: YES")
        if prov.get("note"):
            lines.append(f"**Note**: {prov['note']}")
        return [types.TextContent(type="text", text="\n".join(lines))]

    # Fuzzy search across both constants and provenance
    matches_c = [k for k in constants if name.lower() in k.lower()]
    matches_p = [k for k in provenance if name.lower() in k.lower() and k not in matches_c]
    if matches_c or matches_p:
        lines = [f"No exact match for '{name}'. Did you mean:\n"]
        for m in matches_c[:10]:
            lines.append(f"- **{m}** = {constants[m]}")
        for m in matches_p[:5]:
            prov = provenance[m]
            lines.append(f"- **{m}** (provenance only: {prov.get('source', '?')})")
        return [types.TextContent(type="text", text="\n".join(lines))]

    return [types.TextContent(type="text", text=f"Constant '{name}' not found")]


async def _list_constants(args: dict) -> list[types.TextContent]:
    pattern = args.get("pattern", "")
    section = args.get("section", "")
    constants, provenance = _parse_constants_module()

    filtered = {}
    for k, v in constants.items():
        if pattern:
            try:
                if not re.search(pattern, k, re.IGNORECASE):
                    continue
            except re.error:
                if pattern.lower() not in k.lower():
                    continue
        if section:
            prov = provenance.get(k, {})
            src = prov.get("source", "")
            sess = prov.get("session", "")
            # Rough section matching by keyword
            if not any(s.lower() in f"{k} {src} {sess}".lower() for s in section.split()):
                continue
        filtered[k] = v

    if not filtered:
        return [types.TextContent(type="text",
                text=f"No constants matching pattern='{pattern}' section='{section}'")]

    lines = [f"## Canonical Constants ({len(filtered)} matches)\n"]
    lines.append("| Name | Value | Session | Gate |")
    lines.append("|:-----|:------|:--------|:-----|")
    for k in sorted(filtered.keys()):
        v = filtered[k]
        prov = provenance.get(k, {})
        sess = prov.get("session", "")
        gate = prov.get("gate", "") or ""
        val_str = f"{v:.6g}" if isinstance(v, float) else str(v)
        lines.append(f"| {k} | {val_str} | {sess} | {gate} |")

    return [types.TextContent(type="text", text="\n".join(lines))]


async def _update_constant(args: dict) -> list[types.TextContent]:
    name = args["name"]
    value = args["value"]
    session = args["session"]
    source = args["source"]
    gate = args.get("gate", "")
    comment = args["comment"]
    section_label = args.get("section_label", "SECTION E")

    # Validate name is a valid Python identifier
    if not name.isidentifier():
        return [types.TextContent(type="text",
                text=f"Error: '{name}' is not a valid Python identifier")]

    # Check if constant already exists
    constants, provenance = _parse_constants_module()
    if name in constants:
        return [types.TextContent(type="text",
                text=f"Error: Constant '{name}' already exists with value {constants[name]}. "
                     f"To update an existing constant, manually edit canonical_constants.py "
                     f"(safety measure to prevent accidental overwrites).")]

    # Build the assignment line
    assignment = f"{name} = {value}  # {comment} ({session})"

    # Build the PROVENANCE entry
    gate_str = f'"{gate}"' if gate else "None"
    prov_entry = (
        f'    "{name}": {{"session": "{session}", "source": "{source}", '
        f'"gate": {gate_str}, "superseded": False}},'
    )

    # Read the file to find insertion points
    with open(CONSTANTS_PATH, "r", encoding="utf-8") as f:
        content = f.read()
        lines = content.split("\n")

    # Find the section to insert the constant
    section_line = None
    for i, line in enumerate(lines):
        if section_label in line and line.strip().startswith("#"):
            section_line = i
            break

    if section_line is None:
        # Append before PROVENANCE dict
        for i, line in enumerate(lines):
            if line.startswith("PROVENANCE"):
                section_line = i - 2
                break

    if section_line is None:
        return [types.TextContent(type="text",
                text=f"Error: Could not find '{section_label}' or PROVENANCE in canonical_constants.py")]

    # Find end of section (next blank line or next section header)
    insert_at = section_line + 1
    for i in range(section_line + 1, len(lines)):
        if lines[i].strip().startswith("# ==") or lines[i].strip().startswith("PROVENANCE"):
            insert_at = i - 1
            break
        if lines[i].strip() == "" and i > section_line + 2:
            insert_at = i
            break
    else:
        insert_at = len(lines) - 1

    # Insert the constant
    lines.insert(insert_at, assignment)

    # Find PROVENANCE dict end and insert entry
    prov_insert = None
    for i, line in enumerate(lines):
        if line.strip().startswith(f'"session": "{session}"') or \
           (line.strip().startswith("}") and i > 0 and "PROVENANCE" in "\n".join(lines[max(0,i-200):i])):
            # Find the closing brace of PROVENANCE
            pass

    # Simpler approach: find the last entry before the closing }
    in_prov = False
    last_entry_line = None
    for i, line in enumerate(lines):
        if line.startswith("PROVENANCE"):
            in_prov = True
        if in_prov and line.strip() == "}":
            last_entry_line = i
            break

    if last_entry_line:
        lines.insert(last_entry_line, prov_entry)
        lines.insert(last_entry_line, f"\n    # {section_label} — {session}")

    # Write back
    with open(CONSTANTS_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    return [types.TextContent(type="text",
            text=f"Added constant **{name}** = {value}\n"
                 f"Session: {session}\n"
                 f"Source: {source}\n"
                 f"Gate: {gate or 'None'}\n"
                 f"Inserted into {section_label} of canonical_constants.py\n"
                 f"PROVENANCE entry added.\n\n"
                 f"**Run `/weave --update` to rebuild the knowledge index.**")]


async def _list_classes(args: dict) -> list[types.TextContent]:
    pattern = args.get("pattern", "")
    max_tier = args.get("max_tier", -1)

    conn = _get_db()
    cur = conn.cursor()

    # Defensive: classes table may not exist in older DBs; return graceful
    # error instead of a 500 from the dispatcher.
    try:
        cur.execute(
            "SELECT id, name, tier, parent_id, description, seed_session "
            "FROM classes ORDER BY tier, id"
        )
        rows = cur.fetchall()
    except sqlite3.OperationalError:
        conn.close()
        return [types.TextContent(type="text",
                text="No `classes` table — knowledge.db predates S86. "
                     "Run /weave --db-sync to rebuild.")]

    # Count members per class for the summary table
    cur.execute(
        "SELECT src, COUNT(*) AS n FROM class_edges "
        "WHERE type='contains' AND tgt_type='constants' GROUP BY src"
    )
    member_counts = {row["src"]: row["n"] for row in cur.fetchall()}
    conn.close()

    # Apply filters
    filtered = []
    for r in rows:
        if max_tier >= 0 and (r["tier"] or 0) > max_tier:
            continue
        if pattern:
            try:
                if not (re.search(pattern, r["id"] or "", re.IGNORECASE)
                        or re.search(pattern, r["name"] or "", re.IGNORECASE)):
                    continue
            except re.error:
                if (pattern.lower() not in (r["id"] or "").lower()
                        and pattern.lower() not in (r["name"] or "").lower()):
                    continue
        filtered.append(r)

    if not filtered:
        return [types.TextContent(type="text",
                text=f"No classes matching pattern='{pattern}' max_tier={max_tier}")]

    lines = [f"## Canonical Classes ({len(filtered)} of {len(rows)} shown)\n"]
    lines.append("| ID | Name | Tier | Parent | Members | Seed |")
    lines.append("|:---|:-----|-----:|:-------|--------:|:-----|")
    for r in filtered:
        cid = r["id"]
        # Indent sub-classes for visual hierarchy
        depth_prefix = "└─ " * (r["tier"] or 0) if (r["tier"] or 0) > 0 else ""
        members = member_counts.get(cid, 0)
        lines.append(
            f"| {depth_prefix}{cid} | {r['name'] or ''} | {r['tier']} | "
            f"{r['parent_id'] or '-'} | {members} | {r['seed_session'] or ''} |"
        )

    return [types.TextContent(type="text", text="\n".join(lines))]


async def _query_class(args: dict) -> list[types.TextContent]:
    class_id = args["class_id"]

    conn = _get_db()
    cur = conn.cursor()

    try:
        # Class metadata
        cur.execute(
            "SELECT id, name, tier, parent_id, description, seed_session "
            "FROM classes WHERE id = ?", (class_id,)
        )
        cls = cur.fetchone()
    except sqlite3.OperationalError:
        conn.close()
        return [types.TextContent(type="text",
                text="No `classes` table — run /weave --db-sync.")]

    if not cls:
        # Fuzzy match
        cur.execute("SELECT id, name FROM classes WHERE id LIKE ? OR name LIKE ?",
                    (f"%{class_id}%", f"%{class_id}%"))
        candidates = cur.fetchall()
        conn.close()
        if candidates:
            lines = [f"No exact match for '{class_id}'. Did you mean:\n"]
            for c in candidates:
                lines.append(f"- **{c['id']}**: {c['name']}")
            return [types.TextContent(type="text", text="\n".join(lines))]
        return [types.TextContent(type="text", text=f"Class '{class_id}' not found")]

    # Member constants (contains-edges)
    cur.execute(
        "SELECT tgt, role, comment FROM class_edges "
        "WHERE src = ? AND type = 'contains' AND tgt_type = 'constants' "
        "ORDER BY CASE role "
        "  WHEN 'PRIMARY' THEN 0 "
        "  WHEN 'PRECONDITION' THEN 1 "
        "  WHEN 'EMERGENT_FROM' THEN 2 "
        "  WHEN 'CONSEQUENCE' THEN 3 "
        "  WHEN 'OBSERVABLE_OUTPUT' THEN 4 "
        "  WHEN 'DERIVED' THEN 5 "
        "  WHEN 'RELATED' THEN 6 "
        "  ELSE 7 END, tgt",
        (class_id,)
    )
    members = cur.fetchall()

    # Sub-classes (parent_of edges)
    cur.execute(
        "SELECT tgt FROM class_edges "
        "WHERE src = ? AND type = 'parent_of' AND tgt_type = 'classes'",
        (class_id,)
    )
    sub_class_ids = [r["tgt"] for r in cur.fetchall()]
    sub_classes = []
    for sid in sub_class_ids:
        cur.execute("SELECT id, name FROM classes WHERE id = ?", (sid,))
        sc = cur.fetchone()
        if sc:
            sub_classes.append(sc)

    conn.close()

    # Resolve constant values via the canonical_constants parser
    try:
        constants, _prov = _parse_constants_module()
    except Exception:
        constants = {}

    lines = [f"## Class: {cls['id']} — {cls['name']}\n"]
    lines.append(f"**Tier**: {cls['tier']}  •  "
                 f"**Parent**: {cls['parent_id'] or '(root)'}  •  "
                 f"**Seed session**: {cls['seed_session'] or '?'}")
    lines.append("")
    lines.append(f"**Description**: {cls['description'] or '(none)'}")
    lines.append("")

    if members:
        lines.append(f"### Member constants ({len(members)})")
        lines.append("")
        lines.append("| Constant | Role | Value | Note |")
        lines.append("|:---------|:-----|:------|:-----|")
        for m in members:
            tgt = m["tgt"]
            role = m["role"] or ""
            comment = (m["comment"] or "").replace("|", "/")
            val = constants.get(tgt)
            if val is None:
                val_str = "(value not parsed)"
            elif isinstance(val, float):
                val_str = f"{val:.6g}"
            else:
                val_str = str(val)
            lines.append(f"| {tgt} | {role} | {val_str} | {comment[:60]} |")
        lines.append("")
    else:
        lines.append("### Member constants: (none — see sub-classes)")
        lines.append("")

    if sub_classes:
        lines.append(f"### Sub-classes ({len(sub_classes)})")
        for sc in sub_classes:
            lines.append(f"- **{sc['id']}**: {sc['name']}")
        lines.append("")

    return [types.TextContent(type="text", text="\n".join(lines))]


async def _get_constant_classes(args: dict) -> list[types.TextContent]:
    constant_id = args["constant_id"]

    conn = _get_db()
    cur = conn.cursor()

    try:
        cur.execute(
            "SELECT ce.src AS class_id, c.name AS class_name, ce.role, ce.comment "
            "FROM class_edges ce "
            "LEFT JOIN classes c ON ce.src = c.id "
            "WHERE ce.type = 'contains' "
            "  AND ce.tgt_type = 'constants' "
            "  AND ce.tgt = ? "
            "ORDER BY CASE ce.role "
            "  WHEN 'PRIMARY' THEN 0 WHEN 'DERIVED' THEN 1 WHEN 'RELATED' THEN 2 "
            "  ELSE 3 END, ce.src",
            (constant_id,)
        )
        rows = cur.fetchall()
    except sqlite3.OperationalError:
        conn.close()
        return [types.TextContent(type="text",
                text="No `class_edges` table — run /weave --db-sync.")]

    conn.close()

    if not rows:
        return [types.TextContent(type="text",
                text=f"Constant '{constant_id}' is not a member of any class")]

    lines = [f"## Classes containing `{constant_id}` ({len(rows)} memberships)\n"]
    lines.append("| Class | Class Name | Role | Note |")
    lines.append("|:------|:-----------|:-----|:-----|")
    for r in rows:
        cid = r["class_id"]
        cname = r["class_name"] or "(class metadata missing)"
        role = r["role"] or ""
        note = (r["comment"] or "").replace("|", "/")
        lines.append(f"| {cid} | {cname} | {role} | {note[:60]} |")

    return [types.TextContent(type="text", text="\n".join(lines))]


async def _usage_stats(args: dict) -> list[types.TextContent]:
    """Return the usage counter state. Note: this call itself is counted (pre-bumped in dispatch)."""
    if not USAGE_COUNTER_PATH.exists():
        return [types.TextContent(
            type="text",
            text="Usage counter file not found yet. It will be created on the next tool call."
        )]
    try:
        with open(USAGE_COUNTER_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        return [types.TextContent(type="text", text=f"Error reading usage counter: {e}")]

    lines = []
    lines.append("# Knowledge MCP Usage Counter\n")
    lines.append(f"- Started: {data.get('started_at', 'unknown')}")
    lines.append(f"- Last call: {data.get('last_called', 'never')}")
    lines.append(f"- Total calls: {data.get('total_calls', 0)}")
    lines.append(f"- Counter file: `{USAGE_COUNTER_PATH}`")
    lines.append("")
    lines.append("## By tool")
    lines.append("| Tool | Count | Last called |")
    lines.append("|:-----|------:|:------------|")
    by_tool = data.get("by_tool", {}) or {}
    # Sort by count desc
    for tool_name, entry in sorted(by_tool.items(), key=lambda kv: -int(kv[1].get("count", 0))):
        lines.append(f"| {tool_name} | {entry.get('count', 0)} | {entry.get('last_called', 'never')} |")
    lines.append("")
    lines.append("To reset: delete the counter file and restart the server.")
    return [types.TextContent(type="text", text="\n".join(lines))]


# ---------------------------------------------------------------------------
# emit_verdict — syntax-forced, race-safe gate-verdict emission (added S98)
# ---------------------------------------------------------------------------
# Replaces open-coded append_verdict() in computation scripts. The verdict write
# moves out of N concurrent agent processes into this single MCP handler, guarded
# by a cross-process O_EXCL lockfile — closing the Windows O_APPEND lost-update
# race that clobbered s98_gate_verdicts.txt (5 of 8 lines lost under 8 concurrent
# writers, S98 Batch-1). The JSON schema + server-side re-validation force the
# canonical line grammar; sig_5 (audit_sha256 uniqueness) is checked at write-time.

_SHA_RE = re.compile(r"^[a-f0-9]{64}$")
_GATE_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")
_SESSION_RE = re.compile(r"^\d{1,6}[a-z]?$")  # numeric or letter-suffixed sub-session (e.g. 99, 100a); 6 digits admits test sentinels (990001)
_VERDICTS = {"PASS", "FAIL", "INFO", "PRE-REG-INC"}


async def _acquire_lock(lock_path: Path, timeout: float = 30.0, stale: float = 120.0) -> None:
    """Cross-process advisory lock via an O_CREAT|O_EXCL lockfile (portable Win+POSIX).

    O_EXCL create is atomic on both NTFS and POSIX, so exactly one process holds the
    lock at a time. A lock older than `stale` seconds is presumed orphaned (holder died
    mid-write) and stolen. Spin with asyncio.sleep so the event loop is not blocked.
    """
    deadline = time.time() + timeout
    while True:
        try:
            fd = os.open(str(lock_path), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            try:
                os.write(fd, str(os.getpid()).encode())
            finally:
                os.close(fd)
            return
        except FileExistsError:
            try:
                if time.time() - lock_path.stat().st_mtime > stale:
                    lock_path.unlink()
                    continue
            except OSError:
                pass
            if time.time() > deadline:
                raise TimeoutError(f"verdict lock timeout ({timeout:.0f}s) on {lock_path.name}")
            await asyncio.sleep(0.02)


def _release_lock(lock_path: Path) -> None:
    try:
        lock_path.unlink()
    except OSError:
        pass


def _verr(msg: str) -> list[types.TextContent]:
    return [types.TextContent(type="text", text=f"emit_verdict ERROR: {msg}")]


async def _emit_verdict(args: dict) -> list[types.TextContent]:
    # ---- required fields ----
    try:
        session = str(args["session"]).strip().lower()  # numeric or letter-suffixed (e.g. "99", "100a")
        gate_id = str(args["gate_id"]).strip()
        verdict = str(args["verdict"]).strip().upper()
        value = str(args["value"])
        scheme = str(args["scheme"]).strip()
        convention = str(args["convention"]).strip()
        l_max = str(args["l_max"]).strip()
        audit_sha = str(args["audit_sha256"]).strip().lower()
        content_sha = str(args["content_sha256"]).strip().lower()
    except (KeyError, ValueError, TypeError) as e:
        return _verr(f"missing/invalid required field ({e}); required: session, gate_id, "
                     "verdict, value, scheme, convention, l_max, audit_sha256, content_sha256")

    schema_version = str(args.get("schema_version") or "S84+").strip()
    companion_note = str(args.get("companion_note") or "").strip()
    supersedes = str(args.get("supersedes") or "").strip().lower()
    track = str(args.get("track") or "session").strip().lower()

    # ---- syntax-force (server-side re-validation; clients may not enforce the schema) ----
    if not _SESSION_RE.match(session):
        return _verr(f"session must be numeric or letter-suffixed (e.g. 99, 100a), got '{session}'")
    if track not in {"session", "investigation"}:
        return _verr(f"track must be 'session' or 'investigation', got '{track}'")
    if verdict not in _VERDICTS:
        return _verr(f"verdict must be one of {sorted(_VERDICTS)}, got '{verdict}'")
    if not _GATE_ID_RE.match(gate_id):
        return _verr(f"gate_id '{gate_id}' is not a valid gate identifier")
    if not _SHA_RE.match(audit_sha):
        return _verr(f"audit_sha256 must be 64 lowercase hex chars (got length {len(audit_sha)})")
    if not _SHA_RE.match(content_sha):
        return _verr(f"content_sha256 must be 64 lowercase hex chars (got length {len(content_sha)})")
    if supersedes and not _SHA_RE.match(supersedes):
        return _verr("supersedes must be a 64-hex audit_sha256")
    if "'" in value:
        return _verr("value payload must not contain a single quote (it delimits value='...')")
    if any("\n" in s for s in (value, scheme, convention, l_max)):
        return _verr("value/scheme/convention/l_max must be single-line")

    # ---- [SIGN] 3-tuple group enforcement (all-three-or-none) ----
    sign_v = str(args.get("sign_verdict") or "").strip().upper()
    mag_v = str(args.get("magnitude_verdict") or "").strip().upper()
    reg_v = str(args.get("regime_verdict") or "").strip().upper()
    three_tuple_note = str(args.get("three_tuple_note") or "").strip()
    three_tuple_line = None
    if any([sign_v, mag_v, reg_v]):
        if not all([sign_v, mag_v, reg_v]):
            return _verr("[SIGN] 3-tuple requires ALL of sign_verdict + magnitude_verdict + "
                         "regime_verdict together (or none, for AUDIT/VERIFY gates)")
        if sign_v not in {"PASS", "FAIL", "N/A"}:
            return _verr(f"sign_verdict must be PASS|FAIL|N/A, got '{sign_v}'")
        if mag_v not in {"PASS", "INFO", "FAIL"}:
            return _verr(f"magnitude_verdict must be PASS|INFO|FAIL, got '{mag_v}'")
        if reg_v not in {"VALID", "MARGINAL", "BREAKDOWN"}:
            return _verr(f"regime_verdict must be VALID|MARGINAL|BREAKDOWN, got '{reg_v}'")
        three_tuple_line = (
            f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={reg_v} "
            f"# {gate_id} 3-tuple annotation (schema-v2)"
            + (f"; {three_tuple_note}" if three_tuple_note else "")
        )

    # ---- optional extra comment rows ----
    clean_extra = []
    for r in (args.get("extra_rows") or []):
        r = str(r).rstrip("\n")
        if not r.startswith("#"):
            return _verr(f"extra_rows must each start with '#' (comment rows); got '{r[:40]}'")
        clean_extra.append(r)

    # ---- resolve canonical path (gate-verdicts.md) ----
    # session track:        computations/session-{N}/s{N}_gate_verdicts.txt
    # investigation track:  computations/investigation-{n}/inv{n}_gate_verdicts.txt
    if track == "investigation":
        vfile = PROJECT_ROOT / "computations" / f"investigation-{session}" / f"inv{session}_gate_verdicts.txt"
    else:
        vfile = PROJECT_ROOT / "computations" / f"session-{session}" / f"s{session}_gate_verdicts.txt"
    vrel = vfile.relative_to(PROJECT_ROOT).as_posix()
    try:
        vfile.parent.mkdir(parents=True, exist_ok=True)
    except OSError as e:
        return _verr(f"cannot create {track} dir {vfile.parent}: {e}")
    lock_path = vfile.parent / (vfile.name + ".lock")

    # ---- build the rows ----
    canonical = (
        f"{gate_id}: {verdict} -- value='{value}' "
        f"scheme={scheme} convention={convention} L_max={l_max} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} schema_version={schema_version}"
    )
    if supersedes:
        canonical += f" supersedes={supersedes}"
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {gate_id} dual-SHA companion row"
        + (f"; {companion_note}" if companion_note else "")
    )
    rows = [canonical, companion]
    if three_tuple_line:
        rows.append(three_tuple_line)
    rows.extend(clean_extra)
    block = "\n".join(rows) + "\n"

    # ---- locked, sig_5-checked, single-writer append ----
    try:
        await _acquire_lock(lock_path)
    except TimeoutError as e:
        return _verr(str(e))
    try:
        existing = vfile.read_text(encoding="utf-8") if vfile.exists() else ""
        # sig_5: audit_sha256 must be unique across the file
        if f"audit_sha256={audit_sha}" in existing:
            same_gate = re.search(
                rf"^{re.escape(gate_id)}:\s.*audit_sha256={audit_sha}\b", existing, re.M)
            if same_gate:
                return [types.TextContent(type="text", text=(
                    f"emit_verdict NO-OP: {gate_id} with audit_sha256={audit_sha[:16]}... "
                    "is already present (idempotent re-call; nothing written)."))]
            return _verr(
                f"sig_5 COLLISION — audit_sha256={audit_sha[:16]}... is already used by a "
                "DIFFERENT gate. This is the hardcoded/copy-pasted-SHA bug; recompute the "
                "closure from the input-pin map. (supersedes= is only for correcting THIS gate.)")
        # one canonical line per gate unless this is an Option-A correction
        if re.search(rf"^{re.escape(gate_id)}:\s(PASS|FAIL|INFO|PRE-REG-INC)\s", existing, re.M) \
                and not supersedes:
            return _verr(
                f"{gate_id} already has a canonical verdict line and no supersedes= was given. "
                "Verdicts are permanent; to correct, pass supersedes=<old 64-hex audit_sha256> "
                "(Option-A protocol). Otherwise this is a forbidden double-emission.")
        if existing and not existing.endswith("\n"):
            block = "\n" + block
        with vfile.open("a", encoding="utf-8") as f:
            f.write(block)
    except OSError as e:
        return _verr(f"append failed: {e}")
    finally:
        _release_lock(lock_path)

    return [types.TextContent(type="text", text=(
        f"emit_verdict OK — {len(rows)} rows appended to "
        f"{vrel} "
        f"(cross-process locked; sig_5 unique; track={track}). Lines written:\n\n{block}"))]


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

async def main():
    logger.info("Knowledge MCP server starting...")
    logger.info(f"Project root: {PROJECT_ROOT}")
    logger.info(f"DB path: {DB_PATH} (exists: {DB_PATH.exists()})")
    logger.info(f"Index path: {INDEX_PATH} (exists: {INDEX_PATH.exists()})")
    logger.info(f"Constants path: {CONSTANTS_PATH} (exists: {CONSTANTS_PATH.exists()})")

    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options(),
        )


if __name__ == "__main__":
    asyncio.run(main())
