#!/usr/bin/env python3
"""
Knowledge Index Extractor for the Phonon-Exflation Project.

Walks sessions/ and tier0-computation/, extracts entities
(theorems, closed mechanisms, gates, probability trajectory, session metadata,
data provenance, open channels, equations), and writes tools/knowledge-index.json.

Usage:
    python extract_entities.py                          # Full rebuild
    python extract_entities.py --incremental --file X   # Single-file update
    python extract_entities.py --validate               # Consistency checks
    python extract_entities.py --stats                  # Print counts
"""

import re
import json
import argparse
from pathlib import Path
from datetime import datetime
from collections import OrderedDict


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SESSIONS_DIR = PROJECT_ROOT / "sessions"
TIER0_DIR = PROJECT_ROOT / "tier0-computation"
TIER0_ARCHIVE_DIR = PROJECT_ROOT / "tier0-archive"
INDEX_PATH = PROJECT_ROOT / "tools" / "knowledge-index.json"

# File priority (higher = more authoritative, processed later so they win dedup)
PRIORITY_PATTERNS = [
    (4, re.compile(r".*synthesis.*\.md$", re.IGNORECASE)),
    (5, re.compile(r".*sagan-verdict.*\.md$", re.IGNORECASE)),
    (3, re.compile(r".*gate_verdicts.*\.txt$", re.IGNORECASE)),
    (2, re.compile(r".*\.txt$")),   # other tier0 .txt output files
    (2, re.compile(r".*\.md$")),    # other session minutes
]


def get_priority(filepath: Path) -> int:
    """Return processing priority for a file (higher = more authoritative)."""
    name = filepath.name
    for prio, pattern in PRIORITY_PATTERNS:
        if pattern.match(name):
            return prio
    return 1


# ---------------------------------------------------------------------------
# Session metadata extraction
# ---------------------------------------------------------------------------

# Patterns for session headers across format generations
RE_SESSION_ID = re.compile(
    r"#\s*Session\s+(\d+[a-z]?)\b.*",
    re.IGNORECASE,
)
RE_DATE_INLINE = re.compile(
    r"\*\*Date\*\*:\s*(\d{4}-\d{2}-\d{2})",
)
RE_DATE_HEADER = re.compile(
    r"##\s*Date:\s*(\d{4}-\d{2}-\d{2})",
)
RE_DATE_FROM_FILENAME = re.compile(
    r"(\d{4}-\d{2}-\d{2})",
)
RE_SESSION_TYPE = re.compile(
    r"\*\*Session\s+type\*\*:\s*(.+)",
    re.IGNORECASE,
)
RE_AGENTS = re.compile(
    r"\*\*Agents?\*\*:\s*(.+)",
    re.IGNORECASE,
)
RE_PRIOR = re.compile(
    r"\*\*Prior\*\*:\s*(.+)",
    re.IGNORECASE,
)
RE_VERDICT = re.compile(
    r"\*\*Verdict\*\*:\s*(.+)",
    re.IGNORECASE,
)
RE_SESSION_FROM_FILENAME = re.compile(
    r"session[- _]?(\d+[a-z]?)",
    re.IGNORECASE,
)


def extract_session_metadata(filepath: Path, text: str) -> dict | None:
    """Extract session metadata from a sessions file."""
    # Try to get session ID from the first heading or filename
    session_id = None
    m = RE_SESSION_ID.search(text[:500])
    if m:
        session_id = m.group(1)
    if not session_id:
        m = RE_SESSION_FROM_FILENAME.search(filepath.name)
        if m:
            session_id = m.group(1)
    if not session_id:
        return None

    # Date
    date = None
    for pat in [RE_DATE_INLINE, RE_DATE_HEADER]:
        m = pat.search(text[:600])
        if m:
            date = m.group(1)
            break
    if not date:
        m = RE_DATE_FROM_FILENAME.search(filepath.name)
        if m:
            date = m.group(1)

    # Session type
    session_type = None
    m = RE_SESSION_TYPE.search(text[:800])
    if m:
        session_type = m.group(1).strip().rstrip("*")

    # Agents
    agents = None
    m = RE_AGENTS.search(text[:800])
    if m:
        agents = m.group(1).strip().rstrip("*")

    # Prior
    prior = None
    m = RE_PRIOR.search(text[:800])
    if m:
        prior = m.group(1).strip().rstrip("*")

    # Verdict
    verdict = None
    m = RE_VERDICT.search(text[:1200])
    if m:
        verdict = m.group(1).strip().strip("*")

    # Posterior from post-session probability pattern
    posterior = extract_post_session_prob(text)

    # Collect output file references
    files = []
    for line in text.split("\n"):
        # Match tier0 file references or sessions references
        for fm in re.finditer(r"(?:tier0-computation|tier0-archive|sessions)/\S+", line):
            files.append(fm.group(0))
        # Match s{session}_*.{ext} patterns
        for fm in re.finditer(r"s\d+[a-z]?_\w+\.\w+", line):
            files.append(fm.group(0))

    # Deduplicate files list
    files = list(OrderedDict.fromkeys(files))

    return {
        "id": session_id,
        "date": date,
        "type": session_type,
        "agents": agents,
        "prior": prior,
        "posterior": posterior,
        "verdict": verdict,
        "files": files[:30],  # cap to avoid bloat
        "source_file": str(filepath.relative_to(PROJECT_ROOT)),
    }


# ---------------------------------------------------------------------------
# PROVEN theorems extraction
# ---------------------------------------------------------------------------

RE_PROVEN_SECTION = re.compile(
    r"^#{1,4}\s*(?:[IVXLC]+\.?\d*\s+)?"       # H1-H4 + optional Roman prefix
    r"(?:[^\n]*?"                               # anything before keyword
    r"(?:"
    r"PROVEN"
    r"|Structural\s+(?:Theorems?|Results?|Findings?)"
    r"|Permanent(?:\s+(?:Mathematical|Results?))?"
    r"|WHAT\s+(?:WE\s+)?PROVED"
    r"|WHAT\s+SURVIVES"
    r"|Clean\s+Results"
    r"|Machine\s+Epsilon"
    r"|Category\s+A"
    r")"
    r")[^\n]*\n"                                # rest of header line
    r"((?:.*?\n)*?)"                            # captured body
    r"(?=\n#{1,4}\s|\n---|\n={5,}|\Z)",         # section terminator
    re.IGNORECASE | re.MULTILINE,
)

# Generic table header words that should never be treated as entity names
_TABLE_HEADER_WORDS = frozenset({
    "quantity", "status", "source", "step", "property", "formula",
    "value", "result", "description", "type", "notes", "convention",
    "observable", "branch", "feature", "item", "parameter", "field",
    "label", "symbol", "meaning", "example", "category", "comment",
    "input", "output", "method", "epoch", "what", "why", "how",
    "where", "when", "who", "detail", "entry", "key", "data",
    "nuclear quantity", "physical meaning", "character", "analog",
    "location", "multiplicity", "effect", "nature",
})

RE_PROVEN_TABLE_ROW = re.compile(
    r"\|\s*(.+?)\s*\|\s*(\S+.*?)\s*\|\s*(.+?)\s*\|"
)

RE_PROVEN_BULLET = re.compile(
    r"[-*]\s+\*?\*?(.+?)(?:\*?\*?)?\s*(?:\(([^)]+)\))?\s*$"
)

# Match precision markers like "machine epsilon", "8.4e-15", etc.
RE_PRECISION = re.compile(
    r"(?:machine\s+epsilon|(?:\d+\.?\d*e-?\d+)|\d+/\d+\s+checks?|parameter-free)",
    re.IGNORECASE,
)

# Match session references like "Sessions 7-8", "Session 22b", "(22b)"
RE_SESSION_REF = re.compile(
    r"(?:Sessions?\s+)?(\d+[a-z]?(?:\s*[-–]\s*\d+[a-z]?)?)",
    re.IGNORECASE,
)


def extract_proven_theorems(filepath: Path, text: str) -> list[dict]:
    """Extract PROVEN theorems from a synthesis file."""
    results = []

    # Strategy 1: Look for table rows in PROVEN/Structural sections
    for section_match in RE_PROVEN_SECTION.finditer(text):
        section_text = section_match.group(1)
        for row_match in RE_PROVEN_TABLE_ROW.finditer(section_text):
            name = row_match.group(1).strip().strip("*")
            sessions = row_match.group(2).strip().strip("*")
            statement = row_match.group(3).strip().strip("*")
            if name.lower().startswith("theorem") or name.lower().startswith("--"):
                continue  # skip header rows
            # Skip garbage: separator rows, pipe fragments, tiny strings
            if name.startswith(":") or name.startswith("|") or len(name) < 3:
                continue
            # Skip generic table headers that are not entity names
            if name.lower() in _TABLE_HEADER_WORDS:
                continue
            precision = None
            pm = RE_PRECISION.search(statement)
            if pm:
                precision = pm.group(0)
            results.append({
                "id": f"proven_{len(results)+1}",
                "name": name,
                "status": "PROVEN",
                "sessions": sessions,
                "precision": precision,
                "statement": statement[:200],
                "source_file": str(filepath.relative_to(PROJECT_ROOT)),
            })

    # Strategy 2: Bullet lists under PROVEN headers
    proven_section = False
    for line in text.split("\n"):
        if re.match(
            r"^#{1,4}\s*(?:[IVXLC]+\.?\d*\s+)?.*?"
            r"(?:PROVEN|Permanent|Structural\s+(?:Theorem|Result|Finding)"
            r"|WHAT\s+(?:WE\s+)?PROVED|WHAT\s+SURVIV|Clean\s+Result"
            r"|Machine\s+Epsilon)",
            line, re.IGNORECASE,
        ):
            proven_section = True
            continue
        if re.match(r"^#{1,4}\s", line) and proven_section:
            proven_section = False
            continue
        if proven_section:
            m = RE_PROVEN_BULLET.match(line)
            if m:
                content = m.group(1).strip().strip("*")
                ref = m.group(2) or ""
                # Avoid duplicates with table extraction
                if any(t["name"] in content or content in t["name"]
                       for t in results):
                    continue
                sessions = ""
                sm = RE_SESSION_REF.search(ref)
                if sm:
                    sessions = sm.group(0)
                precision = None
                pm = RE_PRECISION.search(content + " " + ref)
                if pm:
                    precision = pm.group(0)
                # Skip generic words that aren't real theorem names
                if content[:120].lower().strip() in _TABLE_HEADER_WORDS:
                    continue
                results.append({
                    "id": f"proven_{len(results)+1}",
                    "name": content[:120],
                    "status": "PROVEN",
                    "sessions": sessions,
                    "precision": precision,
                    "statement": content[:200],
                    "source_file": str(filepath.relative_to(PROJECT_ROOT)),
                })

    return results


# ---------------------------------------------------------------------------
# CLOSED mechanisms extraction
# ---------------------------------------------------------------------------

RE_CLOSED_SECTION = re.compile(
    r"^#{2,4}\s*(?:[IVXLC]+\.?\d*\s+)?"       # H2-H4 + optional Roman prefix
    r"(?:[^\n]*?"                               # anything before keyword
    r"(?:"
    r"DEAD|CLOSED"                              # status keywords (old + new)
    r"|(?:Kill|Constraint)(?:ed)?\s+(?:Gate\s+)?(?:Registry|Table|Chain|Condition)"
    r"|Complete\s+(?:Kill|Closure)"
    r"|(?:Dead|Closed)\s+Mechanism"
    r"|What\s+is\s+(?:NOT\s+)?(?:killed|closed)"
    r"|ALL\s+(?:DEAD|CLOSED)"
    r"|Definitive\s+(?:Kill|Closure)"
    r"|Perturbative\s+(?:Gates|Mechanisms)"
    r"|UPDATED\s+(?:KILL|CONSTRAINT)"
    r")"
    r")[^\n]*\n"                                # rest of header line
    r"((?:.*?\n)*?)"                            # captured body
    r"(?=\n#{2,4}\s|\n---|\n={5,}|\Z)",         # section terminator
    re.IGNORECASE | re.MULTILINE,
)

# Narrative kill headers: ### II.2 K-1e: Description — DECISIVE CLOSURE
RE_NARRATIVE_CLOSURE_HEADER = re.compile(
    r"^#{2,4}\s+(?:[IVXLC]+\.\d+\s+)?"
    r"([A-Z][\w-]*(?:-\d+[a-z]?)?):\s+"        # gate ID
    r"(.+?)\s+(?:--+|[\u2013\u2014])+\s+"      # description + dash separator
    r"(DECISIVE\s+(?:KILL|CLOSURE)|STRUCTURAL\s+(?:KILL|CLOSURE)"
    r"|KILL|CLOSED|FATAL)",
    re.MULTILINE | re.IGNORECASE,
)

RE_CLOSED_BULLET = re.compile(
    r"[-*]\s+\*?\*?(.+?)(?:\*?\*?)?\s*(?:\(([^)]+)\))?\s*$"
)

RE_GATE_ID = re.compile(
    r"([A-Z]+-\d+[a-z]?|[A-Z]{1,3}-\d+)",
)


def _parse_table_rows(text: str) -> list[list[str]]:
    """Parse markdown table, returning list of cell lists (stripped, no headers)."""
    rows = []
    for line in text.split("\n"):
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip().strip("*") for c in line.split("|")]
        cells = [c for c in cells if c != ""]
        if len(cells) < 3:
            continue
        # Skip separator/header rows
        if cells[0].startswith(":") or cells[0].startswith("-"):
            continue
        if cells[0].lower() in ("gate", "mechanism", "#", "id", "theorem",
                                 "name", "route", "scenario") \
                or cells[0].lower() in _TABLE_HEADER_WORDS:
            continue
        rows.append(cells)
    return rows


def extract_closed_mechanisms(filepath: Path, text: str) -> list[dict]:
    """Extract CLOSED mechanisms from a synthesis file."""
    results = []

    for section_match in RE_CLOSED_SECTION.finditer(text):
        section_text = section_match.group(1)

        # Determine if section header implies all rows are dead
        # (Constraint Registry, Closed Mechanism, Complete Closure Table, ALL CLOSED, etc.)
        header_line = text[max(0, section_match.start()-5):section_match.start()
                          + text[section_match.start():].find("\n")]
        is_constraint_registry = bool(re.search(
            r"(?:(?:Kill|Constraint)\s+(?:Registry|Table)"
            r"|(?:Dead|Closed)\s+Mechanism"
            r"|Complete\s+(?:Kill|Closure)"
            r"|ALL\s+(?:DEAD|CLOSED)"
            r"|(?:DEAD|CLOSED)\s+\("
            r"|(?:Killed|Closed))",
            header_line, re.IGNORECASE,
        ))

        # Table rows (most structured format, used in 22d+)
        for cells in _parse_table_rows(section_text):
            # In kill registries, all rows are implicitly dead
            # Otherwise, require explicit CLOSED/KILL/CLOSED cell
            if not is_constraint_registry:
                status_cell = None
                for cell in cells:
                    if cell.upper() in ("DEAD", "KILL", "CLOSED"):
                        status_cell = cell.upper()
                        break
                if status_cell is None:
                    continue

            # Name is first cell (or second if first is a number)
            idx = 0
            if cells[0].isdigit() and len(cells) > 1:
                idx = 1

            name = cells[idx]

            # Skip if name looks like a header
            if any(name.lower().startswith(h) for h in
                   ["gate", "mechanism", "theorem", "--", ":", "id"]):
                continue

            # For kill registries, columns are: [#] Name Session Kill_reason [BF]
            # For status tables, columns are: Gate Session Result Status
            # Try to identify session by looking for session-like patterns
            session = ""
            reason = ""
            remaining = cells[idx + 1:]
            for cell in remaining:
                # Session cells typically contain digits or session refs like "22b"
                if not session and re.match(r'\d+[a-z]?\b', cell.strip()):
                    session = cell.strip()
                elif not session and re.search(r'Session\s+\d+', cell, re.IGNORECASE):
                    sm = re.search(r'(\d+[a-z]?)', cell)
                    if sm:
                        session = sm.group(1)
                elif cell.upper() not in ("CLOSED", "CLOSED", "CLOSED") and not reason:
                    reason = cell.strip()
            # Fallback: use positional extraction
            if not session and idx + 1 < len(cells):
                session = cells[idx + 1]
            if not reason and idx + 2 < len(cells):
                reason = cells[idx + 2]

            gate_id = None
            gm = RE_GATE_ID.search(reason + " " + name + " " + session)
            if gm:
                gate_id = gm.group(1)

            results.append({
                "id": f"closed_{len(results)+1}",
                "name": name[:120],
                "closed_by": reason[:200],
                "session": session,
                "gate_id": gate_id,
                "source_file": str(filepath.relative_to(PROJECT_ROOT)),
            })

        # Bullet lists (skip lines that are table rows)
        for line in section_text.split("\n"):
            stripped = line.strip()
            if stripped.startswith("|"):
                continue  # table row, not a bullet
            m = RE_CLOSED_BULLET.match(line)
            if m:
                content = m.group(1).strip().strip("*")
                ref = m.group(2) or ""
                # Skip if content is too short or looks like a header
                if len(content) < 5:
                    continue
                # Skip gate assessment lines (e.g., "V_IR monotonic: **CONFIRMED")
                if re.search(r":\s*\*?\*?(CONFIRMED|NOT CLOSED|NOT MET|"
                             r"UNRESOLVED|INCONCLUSIVE|PASSED|FAILED)\b",
                             content, re.IGNORECASE):
                    continue
                # Skip overly long prose descriptions (>120 chars = likely a sentence)
                if len(content) > 120:
                    continue
                # Avoid duplicates with table extraction
                if any(d["name"] in content or content in d["name"]
                       for d in results):
                    continue
                session = ""
                sm = RE_SESSION_REF.search(ref)
                if sm:
                    session = sm.group(0)
                gate_id = None
                gm = RE_GATE_ID.search(content + " " + ref)
                if gm:
                    gate_id = gm.group(1)

                results.append({
                    "id": f"closed_{len(results)+1}",
                    "name": content[:120],
                    "closed_by": ref[:200] if ref else content[:200],
                    "session": session,
                    "gate_id": gate_id,
                    "source_file": str(filepath.relative_to(PROJECT_ROOT)),
                })

    # Strategy 3: Narrative kill headers (### II.2 K-1e: ... — DECISIVE CLOSURE)
    for m in RE_NARRATIVE_CLOSURE_HEADER.finditer(text):
        gate_id = m.group(1).strip()
        description = m.group(2).strip()
        closure_type = m.group(3).strip().upper()
        # Avoid duplicates with prior strategies
        if any(gate_id in (d.get("gate_id") or "") or
               description[:30].lower() in d["name"].lower()
               for d in results):
            continue
        session = extract_session_from_context(filepath, text, m.start())
        results.append({
            "id": f"closed_{len(results)+1}",
            "name": description[:120],
            "closed_by": f"{gate_id}: {closure_type}",
            "session": session,
            "gate_id": gate_id,
            "source_file": str(filepath.relative_to(PROJECT_ROOT)),
        })

    return results


# ---------------------------------------------------------------------------
# Gate verdicts extraction
# ---------------------------------------------------------------------------

RE_GATE_TABLE_ROW = re.compile(
    r"\|\s*\*?\*?"                              # cell start + optional bold
    r"([A-Z][\w-]*(?:\*?\*?\s*\([^)]+\))?)"    # gate ID + optional bold-break + parenthetical
    r"\*?\*?\s*"                                # optional bold close
    r"\|\s*(.+?)\s*"                            # condition cell
    r"\|\s*(.+?)\s*"                            # result cell
    r"\|\s*\*?\*?(.+?)\*?\*?\s*\|"             # verdict cell
)

# Sections that actually contain gate verdicts
RE_GATE_SECTION = re.compile(
    r"^#{2,4}\s*(?:[IVXLC]+\.?\d*\s+)?"       # H2-H4 + optional Roman prefix
    r"(?:"
    r"Gate\s+(?:Table|Status|Verdicts?|Tally|Assessment)"
    r"|Gate-by-Gate"
    r"|(?:Definitive\s+)?(?:Kill|Constraint)\s+Gate(?:\s+(?:Registry|Verdicts?))?"
    r"|(?:Complete\s+)?(?:Kill|Constraint)\s+(?:Gate\s+)?(?:Registry|Table|Verdicts?)"
    r"|(?:Session\s+\d+\w?\s+)?(?:Kill|Constraint)\s+Gate\s+Verdicts?"
    r"|Nominal\s+(?:Kill|Constraint)\s+Gate"
    r"|Pre-Registered\s+(?:Kill|Constraint|Gate)"
    r"|Non-Perturbative\s+Gates"
    r"|Perturbative\s+Gates"
    r"|PB-\d+\s+and\s+PB-\d+\s+Gate"
    r"|[A-Z]+-\d+\s+Gate"
    r"|UPDATED\s+(?:KILL|CONSTRAINT)\s+REGISTRY"
    r"|PRE-REGISTERED\s+(?:KILL|CONSTRAINT|GATE)"
    r").*?\n"
    r"((?:.*?\n)*?)"                            # captured body
    r"(?=\n#{2,4}\s|\n---|\n={5,}|\Z)",         # section terminator
    re.IGNORECASE | re.MULTILINE,
)

RE_GATE_VERDICT_BLOCK = re.compile(
    r"^GATE\s+([A-Z]{1,3}-\d+[a-z]?):\s*(.+?)(?=^GATE\s|\Z)",
    re.DOTALL | re.MULTILINE,
)

RE_BF = re.compile(
    r"BF\s*[=:]\s*([\d.]+)",
    re.IGNORECASE,
)

RE_VERDICT_LINE = re.compile(
    r"VERDICT(?:\s+[A-Z]{1,3}-\d+[a-z]?)?:\s*\*?\*?(.+?)\*?\*?\s*$",
    re.MULTILINE,
)


def extract_gates(filepath: Path, text: str) -> list[dict]:
    """Extract gate verdicts from synthesis or gate verdict files."""
    results = []

    # Strategy 1: Markdown tables WITHIN gate-specific sections only
    gate_sections = []
    for section_match in RE_GATE_SECTION.finditer(text):
        gate_sections.append((section_match.start(), section_match.group(1)))

    # For .txt files (gate_verdicts.txt), use the full text — they are gate-only
    if filepath.suffix == ".txt" and "gate_verdict" in filepath.name.lower():
        gate_sections.append((0, text))

    for section_start, section_text in gate_sections:
        for row_match in RE_GATE_TABLE_ROW.finditer(section_text):
            gate_name = row_match.group(1).replace("**", "").strip().strip("*")
            condition = row_match.group(2).strip().strip("*")
            result = row_match.group(3).strip().strip("*")
            verdict = row_match.group(4).strip().strip("*")

            # Skip header rows, separator rows, and non-gate content
            name_lower = gate_name.lower()
            verdict_lower = verdict.lower()
            if any(name_lower.startswith(h) for h in
                   ["gate", "id", "--", ":", "result", "level",
                    "computation", "bf", "mechanism", "#", "session",
                    "pre-registered", "criterion", "outcome", "assessor"]):
                continue
            if verdict_lower in ["status", "notes", "", "---", ":---",
                                 "|:---", "verdict", ":-------", "bf",
                                 "prob shift", "prob_shift", "bayes",
                                 "closure reason", "session"]:
                continue
            # Gate IDs should be short identifiers like V-1, R-1, SP-5
            if len(gate_name) > 40:
                continue
            # Gate IDs typically have format: LETTER(s)-DIGIT or short name
            # Filter out verdict categories used as row starts
            if name_lower.rstrip(")").rstrip(" ").rstrip("(") in (
                "compelling", "interesting", "neutral",
                "structural", "closure", "pass", "fail",
                "inconclusive", "closed", "open", "diagnostic",
                "conditional", "marginal"):
                continue
            # Also filter names that look like verdict categories with parentheticals
            if any(name_lower.startswith(cat) for cat in
                   ("compelling", "interesting", "neutral", "structural",
                    "inconclusive", "conditional", "marginal")):
                continue
            # Verdicts that are clearly table metadata
            if verdict_lower.startswith("|") or verdict_lower.startswith(":"):
                continue
            # Must contain a recognizable verdict keyword somewhere in the row
            full_row = (verdict + " " + result + " " + condition).upper()
            has_verdict_kw = any(kw in full_row for kw in
                                 ["KILL", "CLOSED", "CLOSURE", "PASS", "FAIL",
                                  "FIRE", "CLOSE",
                                  "COMPELLING", "INTERESTING", "DIAGNOSTIC",
                                  "NEUTRAL", "INCONCLUSIVE", "STRUCTURAL",
                                  "DEAD", "CONDITIONAL", "MARGINAL",
                                  "DOES NOT", "CONFIRMED", "CLEARED",
                                  "UNRESOLVED", "NOT CLOSED", "NOT CLOSED",
                                  "PARTIALLY"])
            if not has_verdict_kw:
                continue

            # Extract BF
            bf = None
            bm = RE_BF.search(result + " " + verdict)
            if bm:
                bf = float(bm.group(1))
            # Check for BF in the verdict or a trailing column
            bm2 = RE_BF.search(section_text[row_match.end():row_match.end()+50])
            if bm2 and bf is None:
                try:
                    bf = float(bm2.group(1))
                except ValueError:
                    pass

            session = extract_session_from_context(filepath, text,
                                                   section_start + row_match.start())

            # Data files referenced nearby
            data_files = []
            window = section_text[max(0, row_match.start()-200):row_match.end()+200]
            for fm in re.finditer(r"s\d+[a-z]?_\w+\.\w+", window):
                data_files.append(fm.group(0))
            data_files = list(OrderedDict.fromkeys(data_files))

            # Clean up markdown artifacts from verdict/condition
            verdict = verdict.strip("*").strip()
            condition = condition.strip("*").strip()
            result = result.strip("*").strip()

            results.append({
                "id": gate_name,
                "name": gate_name,
                "session": session,
                "condition": condition[:200],
                "result": result[:200],
                "verdict": verdict[:100],
                "bayes_factor": bf,
                "data_files": data_files[:10],
                "source_file": str(filepath.relative_to(PROJECT_ROOT)),
            })

    # Strategy 1b: Multi-column tables via generic table parser
    # Handles 5/6/7-column tables that RE_GATE_TABLE_ROW misses
    _verdict_keywords = {
        "KILL FIRES", "DECISIVE KILL", "STRUCTURAL KILL", "MARGINAL KILL",
        "CLOSED", "DECISIVE CLOSURE", "STRUCTURAL CLOSURE", "MARGINAL CLOSURE",
        "KILL", "PASS", "TRIVIAL PASS", "FAIL", "DOES NOT FIRE",
        "DOES NOT CLOSE",
        "COMPELLING", "INTERESTING", "DIAGNOSTIC", "DIAGNOSTIC UNFAVORABLE",
        "NEUTRAL", "INCONCLUSIVE", "CONFIRMED", "CLEARED", "CONDITIONAL",
        "DEAD", "OPEN", "NOT FAVORABLE", "N/A", "ROBUST", "UNRESOLVED",
    }
    for section_start, section_text in gate_sections:
        for cells in _parse_table_rows(section_text):
            if len(cells) < 3:
                continue
            # Find gate ID: look for LETTER-DIGIT pattern in cells
            gate_id = None
            gate_cell_idx = -1
            for ci, cell in enumerate(cells):
                cleaned = cell.strip().strip("*").replace("**", "")
                gm = RE_GATE_ID.match(cleaned)
                if gm:
                    gate_id = gm.group(1)
                    gate_cell_idx = ci
                    break
            if not gate_id:
                continue
            # Skip if already found by Strategy 1 or is a number/header
            if any(g["id"] == gate_id for g in results):
                continue
            # Find verdict: look for verdict keyword in cells
            verdict = ""
            for cell in cells:
                cell_upper = cell.strip().strip("*").upper()
                for kw in sorted(_verdict_keywords, key=len, reverse=True):
                    if kw in cell_upper:
                        verdict = cell.strip().strip("*")
                        break
                if verdict:
                    break
            if not verdict:
                continue
            # Remaining cells = condition/result
            other_cells = [c.strip().strip("*") for i, c in enumerate(cells)
                           if i != gate_cell_idx and c.strip().strip("*") != verdict]
            condition = other_cells[0] if other_cells else ""
            result = other_cells[1] if len(other_cells) > 1 else ""
            # Extract BF from any cell
            bf = None
            for cell in cells:
                bm = RE_BF.search(cell)
                if bm:
                    try:
                        bf = float(bm.group(1))
                    except ValueError:
                        pass
                    break
            session = extract_session_from_context(filepath, text, section_start)
            results.append({
                "id": gate_id,
                "name": gate_id,
                "session": session,
                "condition": condition[:200],
                "result": result[:200],
                "verdict": verdict[:100],
                "bayes_factor": bf,
                "data_files": [],
                "source_file": str(filepath.relative_to(PROJECT_ROOT)),
            })

    # Strategy 2: GATE blocks in text files (s24a_gate_verdicts.txt format)
    # Preprocess: strip ==== separator lines so GATE blocks flow into their content
    # (handles s28b format where ==== brackets the GATE header line)
    text_for_blocks = re.sub(r"\n?={5,}\n?", "\n", text)
    for block_match in RE_GATE_VERDICT_BLOCK.finditer(text_for_blocks):
        gate_name = block_match.group(1).strip()
        block_text = block_match.group(2)

        # Don't duplicate if already found in table
        if any(g["id"] == gate_name for g in results):
            continue

        # Extract condition/result/verdict from block
        condition = ""
        result = ""
        verdict = ""

        for line in block_text.split("\n"):
            line_s = line.strip()
            if line_s.startswith("Condition:"):
                condition = line_s[len("Condition:"):].strip()
            elif line_s.startswith("Result:"):
                result = line_s[len("Result:"):].strip()
            elif line_s.startswith("Closes if:") or line_s.startswith("Fires if:"):
                prefix_len = len("Closes if:") if line_s.startswith("Closes if:") else len("Fires if:")
                condition += " | " + line_s[prefix_len:].strip()
            vm = RE_VERDICT_LINE.match(line_s)
            if vm:
                verdict = vm.group(1).strip()

        bf = None
        bm = RE_BF.search(block_text)
        if bm:
            bf = float(bm.group(1))

        session = extract_session_from_context(filepath, text, block_match.start())

        data_files = []
        for fm in re.finditer(r"s\d+[a-z]?_\w+\.\w+", block_text):
            data_files.append(fm.group(0))
        data_files = list(OrderedDict.fromkeys(data_files))

        results.append({
            "id": gate_name,
            "name": gate_name,
            "session": session,
            "condition": condition[:200],
            "result": result[:200],
            "verdict": verdict[:100],
            "bayes_factor": bf,
            "data_files": data_files[:10],
            "source_file": str(filepath.relative_to(PROJECT_ROOT)),
        })

    # Strategy 3: Narrative gate headers (### II.1 K-0: Description — VERDICT)
    re_narrative_gate = re.compile(
        r"^#{2,4}\s+(?:[IVXLC]+\.\d+\s+)?"
        r"([A-Z][\w-]*(?:-\d+[a-z]?)?):\s+"       # gate ID
        r"(.+?)\s+(?:--+|[\u2013\u2014])+\s+"     # description + dash separator
        r"\*?\*?(DECISIVE\s+(?:KILL|CLOSURE)|STRUCTURAL\s+(?:KILL|CLOSURE)"
        r"|MARGINAL\s+(?:KILL|CLOSURE)"
        r"|KILL(?:\s+FIRES)?|CLOSED|PASS|TRIVIAL\s+PASS|FAIL"
        r"|DOES\s+NOT\s+(?:FIRE|CLOSE)"
        r"|COMPELLING|INTERESTING|NEUTRAL|INCONCLUSIVE|NOT\s+FAVORABLE"
        r"|CLEARED|N/A|ROBUST)\*?\*?",
        re.MULTILINE | re.IGNORECASE,
    )
    for m in re_narrative_gate.finditer(text):
        gate_id = m.group(1).strip()
        description = m.group(2).strip()
        verdict = m.group(3).strip().upper()

        # Skip if already found
        if any(g["id"] == gate_id for g in results):
            continue

        bf = None
        bm = RE_BF.search(description)
        if bm:
            bf = float(bm.group(1))

        session = extract_session_from_context(filepath, text, m.start())

        results.append({
            "id": gate_id,
            "name": gate_id,
            "session": session,
            "condition": description[:200],
            "result": "",
            "verdict": verdict[:100],
            "bayes_factor": bf,
            "data_files": [],
            "source_file": str(filepath.relative_to(PROJECT_ROOT)),
        })

    # Strategy 4: Verdict-colon headers (### B-1 VERDICT: **PASS**)
    # Handles the common pattern where computation documents declare gate results
    # with "VERDICT:" as the separator instead of em-dash.
    _verdict_kws = (
        "DECISIVE KILL", "STRUCTURAL KILL", "MARGINAL KILL",
        "DECISIVE CLOSURE", "STRUCTURAL CLOSURE", "MARGINAL CLOSURE",
        "KILL FIRES", "KILL", "CLOSED", "PASS", "TRIVIAL PASS", "FAIL",
        "DOES NOT FIRE", "DOES NOT CLOSE",
        "COMPELLING", "INTERESTING", "NEUTRAL",
        "INCONCLUSIVE", "NOT FAVORABLE", "CLEARED", "N/A", "ROBUST",
    )
    re_verdict_colon = re.compile(
        r"^#{2,4}\s+"
        r"([A-Z][\w-]*(?:-\d+[a-z]?)?)\s+"        # gate ID (e.g., B-1)
        r"(?:VERDICT|RESULT|GATE\s+VERDICT)\s*:\s*" # VERDICT: separator
        r"\*?\*?"
        r"(" + "|".join(re.escape(kw) for kw in _verdict_kws) + r")"
        r"\*?\*?",
        re.MULTILINE | re.IGNORECASE,
    )
    for m in re_verdict_colon.finditer(text):
        gate_id = m.group(1).strip()
        verdict = m.group(2).strip().upper()

        # Skip if already found
        if any(g["id"] == gate_id for g in results):
            continue

        # Look for condition/result in nearby text (next 500 chars)
        context_after = text[m.end():m.end() + 500]
        condition = ""
        result_text = ""
        bf = None
        data_files = []

        for line in context_after.split("\n"):
            line_s = line.strip()
            if line_s.startswith("Condition:"):
                condition = line_s[len("Condition:"):].strip()
            elif line_s.startswith("Result:"):
                result_text = line_s[len("Result:"):].strip()
            bm = RE_BF.search(line_s)
            if bm and bf is None:
                try:
                    bf = float(bm.group(1))
                except ValueError:
                    pass
            for fm in re.finditer(r"s\d+[a-z]?_\w+\.\w+", line_s):
                data_files.append(fm.group(0))

        data_files = list(OrderedDict.fromkeys(data_files))[:10]
        session = extract_session_from_context(filepath, text, m.start())

        results.append({
            "id": gate_id,
            "name": gate_id,
            "session": session,
            "condition": condition[:200],
            "result": result_text[:200],
            "verdict": verdict[:100],
            "bayes_factor": bf,
            "data_files": data_files,
            "source_file": str(filepath.relative_to(PROJECT_ROOT)),
        })

    return results


def extract_session_from_context(filepath: Path, text: str, pos: int) -> str:
    """Extract session ID from context near position."""
    # Strategy 0: Extract from tier0 filename prefix (s24a_... -> "24a")
    m = re.match(r'^s(\d+[a-z]?)_', filepath.name)
    if m:
        return m.group(1)

    # Strategy 1: Check sessions filename (session-24b-... -> "24b")
    m = RE_SESSION_FROM_FILENAME.search(filepath.name)
    if m:
        return m.group(1)

    # Strategy 2: Look backward from position for session header
    preceding = text[max(0, pos - 2000):pos]
    matches = list(RE_SESSION_REF.finditer(preceding))
    if matches:
        return matches[-1].group(1)
    return ""


# ---------------------------------------------------------------------------
# Probability trajectory extraction
# ---------------------------------------------------------------------------

RE_POST_PROB = re.compile(
    r"\*\*Post[- ](?:session\s+)?(?:\d+[a-z]?\s+)?probability:\s*"
    r"(?:Panel\s+)?(\d+[-–]?\d*)\s*%\s*"
    r"(?:\([^)]*\))?\s*,?\s*"
    r"(?:Sagan\s+)?(\d+[-–]?\d*)\s*%",
    re.IGNORECASE,
)

RE_PROB_TRAJECTORY_LINE = re.compile(
    r"(?:After|Post)\s+(?:Session\s+)?(\S+?):\s+"
    r"(?:~?\s*)?(\d+[-–]?\d*)\s*%\s*"
    r"(?:\(([^)]*)\))?",
    re.IGNORECASE,
)

RE_ADOPTED_POSTERIOR = re.compile(
    r"\*\*(?:Post[- ]\d+[a-z]?\s+)?adopted\*?\*?:\s*"
    r"\*?\*?Panel\s+(\d+[-–]?\d*)\s*%.*?"
    r"Sagan\s+(\d+[-–]?\d*)\s*%",
    re.IGNORECASE,
)


def extract_post_session_prob(text: str) -> dict | None:
    """Extract post-session probability from text."""
    # Try the adopted posterior first (most authoritative)
    m = RE_ADOPTED_POSTERIOR.search(text[:2000])
    if m:
        return {"panel": m.group(1), "sagan": m.group(2)}

    # Try the post-session probability pattern
    m = RE_POST_PROB.search(text)
    if m:
        return {"panel": m.group(1), "sagan": m.group(2)}

    return None


RE_TRAJ_CODE_LINE = re.compile(
    r"(?:Prior|After|Post|===).*?:\s+(?:~?\s*)?(\d+[-–]?\d*)\s*%\s*(?:\(([^)]*)\))?",
    re.IGNORECASE,
)

RE_TRAJ_LABEL_VALUE = re.compile(
    r"^(.+?):\s+(?:~?\s*)?(\d+[-–]?\d*)\s*%\s*(?:\(([^)]*)\))?",
)


def extract_probability_trajectory(filepath: Path, text: str) -> list[dict]:
    """Extract probability data points from a file."""
    results = []

    # Date from filename
    date = None
    dm = RE_DATE_FROM_FILENAME.search(filepath.name)
    if dm:
        date = dm.group(1)

    # Session from filename
    session = ""
    sm = RE_SESSION_FROM_FILENAME.search(filepath.name)
    if sm:
        session = sm.group(1)

    # Strategy 1: Look for code-block trajectory sections (24b format)
    # These are the most complete and authoritative
    in_code_block = False
    code_block_is_trajectory = False
    for line in text.split("\n"):
        stripped = line.strip()

        # Track code block boundaries
        if stripped == "```":
            if in_code_block:
                in_code_block = False
                code_block_is_trajectory = False
            else:
                in_code_block = True
            continue

        if in_code_block and not code_block_is_trajectory:
            # Check if this code block contains trajectory data
            if any(kw in stripped.lower() for kw in
                   ["probability", "prior", "after session", "post-session"]):
                code_block_is_trajectory = True

        if in_code_block and code_block_is_trajectory:
            m = RE_TRAJ_LABEL_VALUE.match(stripped)
            if m:
                label = m.group(1).strip()
                pct = m.group(2)
                note = m.group(3) or ""

                # Extract session reference from label
                ref_session = ""
                sm2 = RE_SESSION_FROM_FILENAME.search(label.replace(" ", "-"))
                if sm2:
                    ref_session = sm2.group(1)
                elif "prior" in label.lower():
                    ref_session = "prior"
                elif "peak" in label.lower():
                    ref_session = "peak"

                # Determine assessor
                assessor = "panel"
                if "sagan" in label.lower():
                    assessor = "sagan"

                results.append({
                    "session": ref_session,
                    "date": date,
                    "panel": pct if assessor == "panel" else "",
                    "sagan": pct if assessor == "sagan" else "",
                    "key_event": note.strip()[:100] or label.strip()[:100],
                    "source_file": str(filepath.relative_to(PROJECT_ROOT)),
                })

    # Strategy 2: Section-header trajectory data
    in_trajectory = False
    for line in text.split("\n"):
        if re.match(
            r"^#{1,4}\s*(?:[IVXLC]+\.?\d*\s+)?.*?"
            r"(?:trajectory|probability\s+(?:timeline|estimate|assessment|update|table)"
            r"|framework\s+prob|per-agent|adopted\s+posterior|convergence\s+assessment"
            r"|bayes\s+factor\s+(?:update|computation)"
            r"|posterior\s+computation"
            r"|combined\s+probability)",
            line, re.IGNORECASE,
        ):
            in_trajectory = True
            continue
        if re.match(r"^#{1,4}\s", line) and in_trajectory:
            in_trajectory = False
            continue
        if in_trajectory:
            m = RE_PROB_TRAJECTORY_LINE.search(line)
            if m:
                ref = m.group(1).strip().rstrip(":")
                pct = m.group(2)
                note = m.group(3) or ""
                assessor = "sagan" if "sagan" in line.lower() else "panel"
                results.append({
                    "session": ref,
                    "date": date,
                    "panel": pct if assessor == "panel" else "",
                    "sagan": pct if assessor == "sagan" else "",
                    "key_event": note.strip()[:100],
                    "source_file": str(filepath.relative_to(PROJECT_ROOT)),
                })

    # Strategy 3: Post-session probability from file headers
    prob = extract_post_session_prob(text)
    if prob and session:
        # Don't add if we already have this session from strategies 1/2
        if not any(r.get("session") == session for r in results):
            results.append({
                "session": session,
                "date": date,
                "panel": prob.get("panel", ""),
                "sagan": prob.get("sagan", ""),
                "key_event": "",
                "source_file": str(filepath.relative_to(PROJECT_ROOT)),
            })

    # Strategy 4: Adopted posterior tables (Panel X%, Sagan Y% in table rows)
    re_adopted_row = re.compile(
        r"\|\s*(?:Sagan|Panel|Combined|Adopted|Einstein)\s*\|"
        r".*?(\d+[-\u2013]?\d*)\s*%",
        re.IGNORECASE,
    )
    in_posterior_section = False
    for line in text.split("\n"):
        if re.match(
            r"^#{1,4}\s*(?:[IVXLC]+\.?\d*\s+)?.*?"
            r"(?:adopted\s+posterior|convergence\s+assessment|pre-registered\s+outcome"
            r"|probability\s+update)",
            line, re.IGNORECASE,
        ):
            in_posterior_section = True
            continue
        if re.match(r"^#{1,4}\s", line) and in_posterior_section:
            in_posterior_section = False
            continue
        if in_posterior_section:
            m = re_adopted_row.search(line)
            if m:
                pct = m.group(1)
                assessor = ""
                line_lower = line.lower()
                if "sagan" in line_lower:
                    assessor = "sagan"
                elif "panel" in line_lower:
                    assessor = "panel"
                elif "combined" in line_lower or "adopted" in line_lower:
                    assessor = "panel"
                elif "einstein" in line_lower:
                    assessor = "panel"
                else:
                    continue
                # Avoid duplicates
                if any(r.get("session") == session and
                       ((assessor == "sagan" and r.get("sagan") == pct) or
                        (assessor == "panel" and r.get("panel") == pct))
                       for r in results):
                    continue
                results.append({
                    "session": session,
                    "date": date,
                    "panel": pct if assessor == "panel" else "",
                    "sagan": pct if assessor == "sagan" else "",
                    "key_event": "adopted posterior",
                    "source_file": str(filepath.relative_to(PROJECT_ROOT)),
                })

    return results


# ---------------------------------------------------------------------------
# Data provenance extraction (tier0-computation/)
# ---------------------------------------------------------------------------

# Match s{session}_{name}.{ext}
RE_TIER0_FILE = re.compile(
    r"^(s\d+[a-z]?)_(.+)\.(py|npz|png|txt|md)$",
    re.IGNORECASE,
)


def extract_data_provenance(tier0_dir: Path) -> list[dict]:
    """Scan tier0-computation/ for script->data->gate provenance."""
    if not tier0_dir.exists():
        return []

    # Group files by session+name prefix
    file_groups: dict[str, dict[str, list[str]]] = {}

    for f in sorted(tier0_dir.iterdir()):
        m = RE_TIER0_FILE.match(f.name)
        if m:
            session = m.group(1)
            name = m.group(2)
            ext = m.group(3).lower()
            key = f"{session}_{name}"
            if key not in file_groups:
                file_groups[key] = {"session": session, "name": name, "files": {}}
            file_groups[key]["files"][ext] = f.name

    results = []
    for key, group in file_groups.items():
        script = group["files"].get("py")
        outputs = []
        for ext in ["npz", "png", "txt", "md"]:
            if ext in group["files"]:
                outputs.append(group["files"][ext])

        # Try to find what gates the script informs
        gates_informed = []
        if script:
            script_path = tier0_dir / script
            if script_path.exists():
                try:
                    script_text = script_path.read_text(encoding="utf-8", errors="replace")
                    # Look for gate references in comments
                    for gm in RE_GATE_ID.finditer(script_text[:2000]):
                        gates_informed.append(gm.group(1))
                except Exception:
                    pass

        # Also check for inputs (.npz files loaded)
        inputs = []
        if script:
            script_path = tier0_dir / script
            if script_path.exists():
                try:
                    script_text = script_path.read_text(encoding="utf-8", errors="replace")
                    for im in re.finditer(r"(?:load|open)\s*\(\s*['\"]([^'\"]+\.npz)['\"]", script_text):
                        inputs.append(im.group(1))
                    for im in re.finditer(r"np\.load\s*\(\s*['\"]([^'\"]+)['\"]", script_text):
                        inputs.append(im.group(1))
                except Exception:
                    pass
        inputs = list(OrderedDict.fromkeys(inputs))

        results.append({
            "script": script,
            "session": group["session"],
            "name": group["name"],
            "inputs": inputs[:10],
            "outputs": outputs,
            "gates_informed": list(OrderedDict.fromkeys(gates_informed))[:10],
        })

    return results


# ---------------------------------------------------------------------------
# Researcher cross-mapping extraction
# ---------------------------------------------------------------------------

RESEARCHERS_DIR = PROJECT_ROOT / "researchers"

RE_PAPER_ENTRY = re.compile(
    r"\[(\d+)\]\s+(.+?)$",
    re.MULTILINE,
)

RE_PAPER_TABLE_ROW = re.compile(
    r"\|\s*(\d+)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|",
)

RE_PAPER_REF_IN_MINUTES = re.compile(
    r"(?:Paper|paper|Ref|ref\.?|Eq\.?|eq\.?)\s*(?:#?\s*)?(\d+).*?"
    r"(?:`researchers/([^`]+?)/|researchers/([^\s)]+?)/)",
    re.IGNORECASE,
)

RE_RESEARCHER_DIR_REF = re.compile(
    r"researchers/(\w[\w-]+)/",
)


def extract_researcher_index(researchers_dir: Path) -> list[dict]:
    """Scan researchers/ directories for paper inventory."""
    if not researchers_dir.exists():
        return []

    results = []
    for subdir in sorted(researchers_dir.iterdir()):
        if not subdir.is_dir():
            continue
        domain = subdir.name

        # Find index file
        index_file = None
        for name in ["index.md", "INDEX.md"]:
            candidate = subdir / name
            if candidate.exists():
                index_file = candidate
                break

        # Count paper files
        paper_files = list(subdir.glob("*.md"))
        paper_files = [f for f in paper_files if f.name.lower() not in
                       ("index.md", "readme.md")]

        paper_count = len(paper_files)
        description = ""

        if index_file:
            try:
                idx_text = index_file.read_text(encoding="utf-8", errors="replace")
                # Extract description from first few lines
                for line in idx_text.split("\n")[:10]:
                    if line.startswith("**Primary domain**:"):
                        description = line.split(":", 1)[1].strip()
                        break
                    elif line.startswith("**Focus**:"):
                        description = line.split(":", 1)[1].strip()
                        break
            except Exception:
                pass

        results.append({
            "domain": domain,
            "paper_count": paper_count,
            "description": description[:200],
            "index_file": str(index_file.relative_to(PROJECT_ROOT)) if index_file else None,
            "path": f"researchers/{domain}/",
        })

    return results


def extract_researcher_citations(filepath: Path, text: str) -> list[dict]:
    """Extract researcher paper citations from meeting minutes."""
    results = []

    # Find all references to researcher directories
    for m in RE_RESEARCHER_DIR_REF.finditer(text):
        domain = m.group(1)
        # Get surrounding context for the citation
        start = max(0, m.start() - 100)
        end = min(len(text), m.end() + 100)
        context = text[start:end].replace("\n", " ").strip()

        session = ""
        sm = RE_SESSION_FROM_FILENAME.search(filepath.name)
        if sm:
            session = sm.group(1)

        results.append({
            "domain": domain,
            "session": session,
            "context": context[:200],
            "source_file": str(filepath.relative_to(PROJECT_ROOT)),
        })

    return results


# ---------------------------------------------------------------------------
# OPEN channels extraction
# ---------------------------------------------------------------------------

RE_OPEN_SECTION = re.compile(
    r"^#{2,4}\s*(?:[IVXLC]+\.?\d*\s+)?"       # H2-H4 + optional Roman prefix
    r"(?:[^\n]*?"                               # anything before keyword
    r"(?:"
    r"OPEN"
    r"|Open\s+Channels?"
    r"|Remaining"
    r"|Rescue"
    r"|Surviving(?:\s+Claim)?"
    r"|P2[ab](?:/P2[ab])?"
    r"|Escape\s+Routes?"
    r"|What(?:'?s)?\s+(?:Survives?|Open)"
    r"|Post-Mortem"
    r"|OFF-DIAGONAL\s+COUPLING"
    r")"
    r")[^\n]*\n"                                # rest of header line
    r"((?:.*?\n)*?)"                            # captured body
    r"(?=\n#{2,4}\s|\n---|\n={5,}|\Z)",         # section terminator
    re.IGNORECASE | re.MULTILINE,
)

RE_OPEN_TABLE_ROW = re.compile(
    r"\|\s*\*?\*?(.+?)\*?\*?\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|"
)

RE_OPEN_BULLET = re.compile(
    r"[-*]\s+\*?\*?([^*\n]+?)\*?\*?:\s*(.+?)$"
)


def extract_open_channels(filepath: Path, text: str) -> list[dict]:
    """Extract OPEN channels from a synthesis file."""
    results = []

    for section_match in RE_OPEN_SECTION.finditer(text):
        section_text = section_match.group(1)

        # Table rows — use robust parser
        for cells in _parse_table_rows(section_text):
            if len(cells) < 2:
                continue
            name = cells[0]

            # Skip if name is too short or looks like metadata
            if len(name) < 5:
                continue
            if name.startswith("|") or name.startswith(":") or name.startswith("-"):
                continue

            col2 = cells[1] if len(cells) > 1 else ""
            col3 = cells[2] if len(cells) > 2 else ""

            session = ""
            sm = RE_SESSION_FROM_FILENAME.search(filepath.name)
            if sm:
                session = sm.group(1)

            results.append({
                "name": name[:120],
                "detail_1": col2[:200],
                "detail_2": col3[:200],
                "session": session,
                "source_file": str(filepath.relative_to(PROJECT_ROOT)),
            })

        # Bullet lists (skip table rows)
        for line in section_text.split("\n"):
            stripped = line.strip()
            if stripped.startswith("|"):
                continue
            m = RE_OPEN_BULLET.match(line)
            if m:
                name = m.group(1).strip()
                detail = m.group(2).strip()
                if len(name) < 5:
                    continue
                # Avoid duplicates
                if any(o["name"] in name or name in o["name"] for o in results):
                    continue
                session = ""
                sm = RE_SESSION_FROM_FILENAME.search(filepath.name)
                if sm:
                    session = sm.group(1)
                results.append({
                    "name": name[:120],
                    "detail_1": detail[:200],
                    "detail_2": "",
                    "session": session,
                    "source_file": str(filepath.relative_to(PROJECT_ROOT)),
                })

    return results


# ---------------------------------------------------------------------------
# Equation extraction
# ---------------------------------------------------------------------------

# Display math: $$...$$
RE_DISPLAY_MATH = re.compile(r'\$\$(.+?)\$\$', re.DOTALL)

# Inline math: $...$  (must contain = and be non-trivial)
RE_INLINE_MATH = re.compile(r'(?<!\$)\$([^\$\n]{5,150})\$(?!\$)')

# Structural equations in code blocks or plain text: LHS = RHS with math chars
RE_STRUCT_EQ = re.compile(
    r'^[ ]{0,8}('
    r'[A-Za-z_\(\[][\w_{}\(\)\[\]\\,\s\^\']*'
    r'\s*[=≡≈]\s*'
    r'[^\n|]{5,}'
    r')$',
    re.MULTILINE,
)

# Equation tag pattern: \tag{E-3} or (E-3) or [eq. 7.5]
RE_EQ_TAG = re.compile(r'\\tag\{([^}]+)\}|\(([A-Z]-\d+[a-z]?)\)|\[eq\.?\s*([\d.]+)\]')

# Characters that indicate real math content
MATH_CHARS = set(r'^{}()\\_∫∑∏≤≥±²³λτφψΛΔγσρκμν∇')

ARTIFACTS_DIR = PROJECT_ROOT / "artifacts"


def _has_math_content(s: str) -> bool:
    """Check if a string contains mathematical notation."""
    return any(c in MATH_CHARS for c in s)


def _get_context(text: str, pos: int, before_lines: int = 2) -> str:
    """Get text context (preceding lines) around a position."""
    preceding = text[:pos]
    lines = preceding.split('\n')
    ctx_lines = lines[-(before_lines + 1):-1] if len(lines) > before_lines else lines[:-1]
    ctx = ' '.join(line.strip() for line in ctx_lines if line.strip())
    # Strip markdown formatting
    ctx = re.sub(r'\*\*(.+?)\*\*', r'\1', ctx)
    ctx = re.sub(r'#+\s*', '', ctx)
    return ctx[:200]


def _normalize_equation(raw: str) -> str:
    """Normalize equation for dedup comparison."""
    # Strip whitespace, common LaTeX noise
    s = raw.strip()
    s = re.sub(r'\s+', ' ', s)
    s = re.sub(r'\\(?:left|right|,|;|quad|qquad|text\{[^}]*\})', '', s)
    s = s.replace(' ', '').lower()
    return s[:100]


def extract_equations(filepath: Path, text: str) -> list[dict]:
    """Extract mathematical equations from a source file."""
    results = []
    fname = filepath.name
    is_python = filepath.suffix == '.py'

    # --- Display math (highest value) ---
    for m in RE_DISPLAY_MATH.finditer(text):
        raw = m.group(1).strip().replace('\n', ' ')
        if len(raw) < 5:
            continue
        line_no = text[:m.start()].count('\n') + 1
        context = _get_context(text, m.start())

        # Check for explicit tag
        tag = None
        tm = RE_EQ_TAG.search(raw)
        if tm:
            tag = tm.group(1) or tm.group(2) or tm.group(3)

        # Extract session from filename
        session = ""
        sm = RE_SESSION_FROM_FILENAME.search(fname)
        if sm:
            session = sm.group(1)

        results.append({
            "id": "",  # assigned later
            "name": None,
            "raw": raw[:500],
            "type": "display",
            "tag": tag,
            "context": context,
            "session": session,
            "source_file": str(filepath.relative_to(PROJECT_ROOT)),
            "line": line_no,
        })

    # --- Inline math with equations (= sign required, must be non-trivial) ---
    for m in RE_INLINE_MATH.finditer(text):
        raw = m.group(1).strip()
        # Must contain = and math-like content, and be long enough
        if '=' not in raw:
            continue
        if len(raw) < 10:
            continue
        if not (_has_math_content(raw) or '\\' in raw):
            continue
        # Skip things that are clearly not equations
        if raw.startswith('http') or '|' in raw[:5]:
            continue

        line_no = text[:m.start()].count('\n') + 1
        context = _get_context(text, m.start())

        tag = None
        tm = RE_EQ_TAG.search(raw)
        if tm:
            tag = tm.group(1) or tm.group(2) or tm.group(3)

        session = ""
        sm = RE_SESSION_FROM_FILENAME.search(fname)
        if sm:
            session = sm.group(1)

        results.append({
            "id": "",
            "name": None,
            "raw": raw[:500],
            "type": "inline",
            "tag": tag,
            "context": context,
            "session": session,
            "source_file": str(filepath.relative_to(PROJECT_ROOT)),
            "line": line_no,
        })

    # --- Pre-pass: build set of line numbers inside fenced code blocks ---
    # Prevents Python/bash in ```python ... ``` blocks from being tagged "structural"
    # Pattern already used in extract_probability_trajectory() (lines 676-688)
    fenced_lines: set[int] = set()  # line numbers inside fences
    in_fence = False
    fence_lang = ""
    for i, fline in enumerate(text.split("\n"), start=1):
        stripped = fline.strip()
        if not in_fence and stripped.startswith("```"):
            in_fence = True
            fence_lang = stripped[3:].strip().lower()  # e.g. "python", "bash", ""
            continue
        if in_fence and stripped == "```":
            in_fence = False
            fence_lang = ""
            continue
        if in_fence and fence_lang in ("python", "py", "bash", "shell", "sh", "javascript", "js", "json"):
            fenced_lines.add(i)

    # --- Structural equations (code-block, plain-text, or Python code) ---
    # In this project, Python code IS the math — tier0 scripts are physics computations
    for m in RE_STRUCT_EQ.finditer(text):
        line = m.group(1).strip()
        # Filter: skip table rows, headers, URLs
        if line.startswith('|') or line.startswith('#') or 'http' in line:
            continue
        if len(line) < 12:
            continue
        # For markdown: require math chars OR known physics identifiers
        # For Python: the code itself is the equation — be more inclusive
        if not is_python:
            if not _has_math_content(line):
                continue
            # Skip lines that are clearly prose (too many words with no math)
            words = line.split()
            if len(words) > 15:
                continue
        else:
            # Python: skip pure imports, prints, file I/O, control flow
            stripped_line = line.lstrip()
            if any(stripped_line.startswith(kw) for kw in (
                'import ', 'from ', 'print(', 'print (', 'plt.', 'ax.',
                'fig,', 'fig =', 'parser', 'args', 'if __', 'def ',
                'class ', 'return ', '#', 'with ', 'open(', 'json.',
                'Path(', 'os.', 'sys.', 'for ', 'while ', 'try:',
                'except', 'finally', 'raise ', 'assert ',
                'logging', 'logger', 'warnings',
            )):
                continue
            # Skip string assignments and pure formatting
            if re.match(r'^\w+\s*=\s*["\']', stripped_line):
                continue
            if re.match(r'^\w+\s*=\s*(?:True|False|None|\[\]|\{\}|\(\))\s*$', stripped_line):
                continue
            # Must have numeric, mathematical, or array content
            if not any(c in line for c in '0123456789.*+-/()[]@'):
                continue

        line_no = text[:m.start()].count('\n') + 1
        context = _get_context(text, m.start())

        session = ""
        sm = RE_SESSION_FROM_FILENAME.search(fname)
        if sm:
            session = sm.group(1)
        if not session and is_python:
            sm2 = re.match(r'^s(\d+[a-z]?)_', fname)
            if sm2:
                session = sm2.group(1)

        # If line is inside a fenced code block in a .md file, tag as "code"
        if not is_python and line_no in fenced_lines:
            eq_type = "code"
        else:
            eq_type = "code" if is_python else "structural"
        results.append({
            "id": "",
            "name": None,
            "raw": line[:500],
            "type": eq_type,
            "tag": None,
            "context": context,
            "session": session,
            "source_file": str(filepath.relative_to(PROJECT_ROOT)),
            "line": line_no,
        })

    # --- Python comment equations (# physics formula) ---
    if is_python:
        for m in re.finditer(r'#\s*(.+?[=≡≈].{5,})', text):
            line = m.group(1).strip()
            if len(line) < 15:
                continue
            # Must look like math, not a prose comment
            if not (_has_math_content(line) or any(c in line for c in '*/^()+-')):
                continue
            words = line.split()
            if len(words) > 20:
                continue

            line_no = text[:m.start()].count('\n') + 1
            context = _get_context(text, m.start())

            session = ""
            sm2 = re.match(r'^s(\d+[a-z]?)_', fname)
            if sm2:
                session = sm2.group(1)

            results.append({
                "id": "",
                "name": None,
                "raw": line[:500],
                "type": "comment",
                "tag": None,
                "context": context,
                "session": session,
                "source_file": str(filepath.relative_to(PROJECT_ROOT)),
                "line": line_no,
            })

    return results


def dedup_equations(equations: list[dict]) -> list[dict]:
    """Deduplicate equations by normalized content, keeping highest-authority source.

    Curated fields (name, latex, audit_status) are preserved from the existing
    entry when the new entry doesn't have them, regardless of which wins on
    priority.  This prevents full rebuilds from discarding manual curation.
    """
    _CURATED_FIELDS = ("name", "latex", "audit_status", "errata")
    seen: dict[str, int] = {}
    priorities = []

    for i, eq in enumerate(equations):
        norm = _normalize_equation(eq["raw"])
        prio = get_priority(Path(eq.get("source_file", "")))
        priorities.append(prio)

        if norm in seen:
            existing_idx = seen[norm]
            loser_idx = existing_idx if prio >= priorities[existing_idx] else i
            winner_idx = i if loser_idx == existing_idx else existing_idx
            # Preserve curated fields from whichever copy has them
            for field in _CURATED_FIELDS:
                loser_val = equations[loser_idx].get(field)
                winner_val = equations[winner_idx].get(field)
                if loser_val and not winner_val:
                    equations[winner_idx][field] = loser_val
            seen[norm] = winner_idx
        else:
            seen[norm] = i

    # Collect unique equations, sorted by original order
    indices = sorted(set(seen.values()))
    result = []
    for i in indices:
        eq = equations[i]
        eq["id"] = f"eq_{len(result) + 1}"
        result.append(eq)

    return result


# ---------------------------------------------------------------------------
# Deduplication
# ---------------------------------------------------------------------------

def _normalize_for_dedup(name) -> str:
    """Normalize a name for deduplication comparison."""
    if name is None:
        return ""
    n = str(name).strip().lower()
    # Unicode -> ASCII for common physics symbols
    for old, new in [
        ("\u03c4", "tau"), ("\u03c3", "sigma"), ("\u03c6", "phi"),
        ("\u03c8", "psi"), ("\u03bb", "lambda"), ("\u03b1", "alpha"),
        ("\u03b2", "beta"), ("\u03b3", "gamma"), ("\u0394", "delta"),
        ("\u03c0", "pi"), ("\u2261", "="), ("\u2248", "~"),
        ("\u2014", "-"), ("\u2013", "-"),
        # Unicode subscript digits
        ("\u2080", "0"), ("\u2081", "1"), ("\u2082", "2"), ("\u2083", "3"),
        ("\u2084", "4"), ("\u2085", "5"), ("\u2086", "6"), ("\u2087", "7"),
        ("\u2088", "8"), ("\u2089", "9"),
        # Unicode superscript digits
        ("\u00b2", "2"), ("\u00b3", "3"),
    ]:
        n = n.replace(old, new)
    # Strip markdown artifacts
    n = re.sub(r'[*`|]', '', n)
    # Strip parenthetical suffixes
    n = re.sub(r'\s*\([^)]*\)\s*$', '', n)
    # Normalize whitespace around operators
    n = re.sub(r'\s*([+\-=])\s*', r'\1', n)
    # Normalize _N notation to bare N (so _2 and ₂ both become 2)
    n = re.sub(r'_(\d)', r'\1', n)
    # Collapse whitespace
    n = re.sub(r'\s+', ' ', n).strip()
    return n[:80]


def _is_resolved_verdict(entity: dict) -> bool:
    """Check if a gate entity has a resolved (non-PENDING) verdict."""
    verdict = (entity.get("verdict") or "").upper()
    return any(kw in verdict for kw in ("KILL", "CLOSED", "CLOSURE", "PASS", "FAIL",
                                         "FIRE", "CLOSE", "DEAD",
                                         "CONFIRMED", "CLEARED"))


def dedup_by_name(entities: list[dict], key: str = "name") -> list[dict]:
    """Deduplicate entities by name, keeping the last occurrence (highest authority).

    Uses normalized names with Unicode folding and prefix matching:
    if name_A is a prefix of name_B (or vice versa), they're duplicates.
    Curated fields (errata) are preserved from the loser when the winner
    lacks them, preventing full rebuilds from discarding manual annotations.

    Special rule for gates: a resolved verdict (PASS/KILL/FAIL) always beats
    a PENDING verdict, regardless of file priority. This prevents pre-registered
    gate stubs from overwriting actual computation results.
    """
    _CURATED_GENERAL = ("errata",)

    # First pass: collect normalized names and their indices
    norms: list[tuple[str, int]] = []
    for i, ent in enumerate(entities):
        raw = ent.get(key, "")
        # Skip garbage entries (separator rows, pipe fragments)
        if raw.startswith(":") or raw.startswith("|") or len(raw.strip()) < 3:
            continue
        norms.append((_normalize_for_dedup(raw), i))

    # Second pass: deduplicate with prefix matching
    # Process in order so later entries (higher authority) win
    seen: dict[str, int] = {}
    for norm, idx in norms:
        if not norm:
            continue
        # Check if this norm is a prefix of (or matches) an existing key
        merged = False
        for existing_norm in list(seen.keys()):
            if norm.startswith(existing_norm) or existing_norm.startswith(norm):
                existing_idx = seen[existing_norm]
                # Default: later entry (higher priority) wins
                winner_idx = idx
                loser_idx = existing_idx
                # Gate-specific override: resolved verdict beats PENDING
                # regardless of file priority ordering
                new_resolved = _is_resolved_verdict(entities[idx])
                old_resolved = _is_resolved_verdict(entities[existing_idx])
                if old_resolved and not new_resolved:
                    # Existing has a real verdict, newcomer is PENDING — keep existing
                    winner_idx = existing_idx
                    loser_idx = idx
                # Preserve curated fields from loser
                for field in _CURATED_GENERAL:
                    loser_val = entities[loser_idx].get(field)
                    winner_val = entities[winner_idx].get(field)
                    if loser_val and not winner_val:
                        entities[winner_idx][field] = loser_val
                # Keep the longer name as the key, use the winner index
                longer = norm if len(norm) >= len(existing_norm) else existing_norm
                del seen[existing_norm]
                seen[longer] = winner_idx
                merged = True
                break
        if not merged:
            seen[norm] = idx

    # Return in original order
    indices = sorted(seen.values())
    return [entities[i] for i in indices]


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def validate_index(index: dict) -> list[str]:
    """Run consistency checks on the index. Returns list of violation strings."""
    violations = []

    # Check 1: No entity both PROVEN and CLOSED (allow known valid overlaps
    # where a proven theorem directly produces a closure)
    ALLOWED_OVERLAPS = {"rolling modulus quintessence"}
    proven_names = {t["name"].lower().strip() for t in index.get("theorems", [])}
    closed_names = {d["name"].lower().strip() for d in index.get("closed_mechanisms", [])}
    overlap = (proven_names & closed_names) - ALLOWED_OVERLAPS
    if overlap:
        for name in overlap:
            violations.append(f"PROVEN+CLOSED overlap: '{name}'")

    # Check 2: Gate verdicts should have a verdict
    for g in index.get("gates", []):
        if not g.get("verdict"):
            violations.append(f"Gate '{g['id']}' has no verdict")

    # Check 3: Session date check removed — filenames are date-stripped

    # Check 4: Data provenance scripts should exist
    for p in index.get("data_provenance", []):
        if p.get("script"):
            script_path = TIER0_DIR / p["script"]
            archive_path = TIER0_ARCHIVE_DIR / p["script"]
            if not script_path.exists() and not archive_path.exists():
                violations.append(f"Missing script: {p['script']}")

    # Check 5: Source files should exist
    all_entities = (
        index.get("theorems", []) +
        index.get("closed_mechanisms", []) +
        index.get("gates", []) +
        index.get("sessions", [])
    )
    for ent in all_entities:
        sf = ent.get("source_file", "")
        if sf and not (PROJECT_ROOT / sf).exists():
            violations.append(f"Missing source: {sf}")

    return violations


# ---------------------------------------------------------------------------
# Canonical constants audit (S34+ enforcement)
# Patterns, session floor, and exempt list all live in canonical_constants.py.
# This module imports them dynamically — add new patterns THERE, not here.
# ---------------------------------------------------------------------------

def _load_canon_audit_config():
    """Import audit config from canonical_constants.py (tier0-computation/).

    Returns a dict with keys: patterns, session_floor, exempt_scripts, import_re,
    potential_hardcode_re, canon_names, ignore_names, ignore_prefixes.
    Falls back to empty config if the module can't be loaded.
    """
    import importlib.util
    empty = {
        "patterns": [], "session_floor": 34,
        "exempt_scripts": frozenset(),
        "import_re": re.compile(r"from\s+canonical_constants\s+import\s+"),
        "potential_hardcode_re": None,
        "canon_names": frozenset(),
        "ignore_names": frozenset(),
        "ignore_prefixes": (),
    }
    spec = importlib.util.spec_from_file_location(
        "canonical_constants", TIER0_DIR / "canonical_constants.py")
    if spec is None or spec.loader is None:
        return empty
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
    except Exception as e:
        print(f"  WARN: Could not load canonical_constants: {e}")
        return empty

    return {
        "patterns": getattr(mod, "AUDIT_PATTERNS_COMPILED", []),
        "session_floor": getattr(mod, "AUDIT_SESSION_FLOOR", 34),
        "exempt_scripts": getattr(mod, "AUDIT_EXEMPT_SCRIPTS", frozenset()),
        "import_re": re.compile(r"from\s+canonical_constants\s+import\s+"),
        "potential_hardcode_re": getattr(mod, "_RE_POTENTIAL_HARDCODE", None),
        "canon_names": getattr(mod, "_CANON_NAMES", frozenset()),
        "ignore_names": getattr(mod, "_HARDCODE_IGNORE_NAMES", frozenset()),
        "ignore_prefixes": getattr(mod, "_HARDCODE_IGNORE_PREFIXES", ()),
    }


def _extract_session_number(filename: str) -> int | None:
    """Extract integer session number from a tier0 filename like s42_foo.py."""
    m = re.match(r"^s(\d+)", filename, re.IGNORECASE)
    if m:
        return int(m.group(1))
    return None


def audit_canonical_constants(tier0_dir: Path) -> list[dict]:
    """Scan S34+ scripts for hardcoded constants that should use canonical_constants.

    Two passes:
      1. VIOLATION: known stale patterns (from AUDIT_PATTERNS_COMPILED)
      2. POTENTIAL_HARDCODE: assignments that look like physics constants but
         aren't in the canon — catches agents inventing new constants without
         updating canonical_constants.py.

    Returns a list of dicts:
        {"script": str, "session": int, "line": int, "pattern": str, "detail": str}
    """
    if not tier0_dir.exists():
        return []

    cfg = _load_canon_audit_config()
    stale_patterns = cfg["patterns"]
    session_floor = cfg["session_floor"]
    exempt_scripts = cfg["exempt_scripts"]
    import_re = cfg["import_re"]
    hardcode_re = cfg["potential_hardcode_re"]
    canon_names = cfg["canon_names"]
    ignore_names = cfg["ignore_names"]
    ignore_prefixes = cfg["ignore_prefixes"]

    if not stale_patterns:
        print("  WARN: No audit patterns loaded — check canonical_constants.py")
        return []

    results = []
    for pyf in sorted(tier0_dir.glob("*.py")):
        if pyf.name in exempt_scripts:
            continue
        session_num = _extract_session_number(pyf.name)
        if session_num is None or session_num < session_floor:
            continue

        try:
            lines = pyf.read_text(encoding="utf-8", errors="replace").splitlines()
        except Exception:
            continue

        has_import = False
        imported_names = set()
        violations = []
        potential = []
        in_docstring = False

        for line_no, line in enumerate(lines, 1):
            stripped = line.lstrip()

            # Track docstring boundaries (triple-quote toggle)
            tq_count = stripped.count('"""') + stripped.count("'''")
            if tq_count % 2 == 1:
                in_docstring = not in_docstring
            if in_docstring:
                continue

            # Track canonical imports
            if import_re.search(line):
                has_import = True
                # Extract imported names
                m = re.search(r"from\s+canonical_constants\s+import\s+(.+)", line)
                if m:
                    for part in m.group(1).split(","):
                        name = part.strip().split(" as ")[0].strip()
                        imported_names.add(name)
                        # Also track the alias
                        if " as " in part:
                            alias = part.strip().split(" as ")[1].strip()
                            imported_names.add(alias)

            if stripped.startswith("#"):
                continue

            # Pass 1: known stale patterns
            for pat_name, pat_re, detail in stale_patterns:
                if pat_re.search(line):
                    violations.append({
                        "script": pyf.name,
                        "session": session_num,
                        "line": line_no,
                        "pattern": pat_name,
                        "detail": detail,
                    })

            # Pass 2: heuristic — potential new hardcodes
            if hardcode_re:
                hm = hardcode_re.match(stripped)
                if hm:
                    name = hm.group(1)
                    name_lower = name.lower()
                    # Skip if: already imported, known canon name, ignorable,
                    # or starts with ignore prefix
                    if (name in imported_names
                            or name in canon_names
                            or name_lower in ignore_names
                            or any(name_lower.startswith(p) for p in ignore_prefixes)):
                        continue
                    # Only flag names that look like physics constants:
                    # at least 2 chars, contains uppercase or underscore
                    if len(name) >= 2 and ("_" in name or any(c.isupper() for c in name)):
                        potential.append({
                            "script": pyf.name,
                            "session": session_num,
                            "line": line_no,
                            "pattern": "POTENTIAL_HARDCODE",
                            "detail": f"{name} = ... — not in canonical_constants.py",
                        })

        if has_import and not violations:
            results.append({
                "script": pyf.name,
                "session": session_num,
                "line": 0,
                "pattern": "IMPORT_OK",
                "detail": "Uses canonical_constants import",
            })
        results.extend(violations)
        results.extend(potential)

    return results


def print_constants_audit(audit_results: list[dict]):
    """Print the canonical constants audit report."""
    violations = [r for r in audit_results
                  if r["pattern"] not in ("IMPORT_OK", "POTENTIAL_HARDCODE")]
    potential = [r for r in audit_results if r["pattern"] == "POTENTIAL_HARDCODE"]
    imports_ok = [r for r in audit_results if r["pattern"] == "IMPORT_OK"]

    print("=" * 60)
    print("CANONICAL CONSTANTS AUDIT (S34+)")
    print("=" * 60)

    if imports_ok:
        print(f"\n  Compliant scripts ({len(imports_ok)}):")
        for r in imports_ok:
            print(f"    {r['script']}")

    if violations:
        print(f"\n  VIOLATIONS ({len(violations)}):")
        for r in violations:
            print(f"    {r['script']}:{r['line']}  [{r['pattern']}]")
            print(f"      -> {r['detail']}")
    else:
        print(f"\n  No violations found.")

    if potential:
        print(f"\n  POTENTIAL HARDCODES ({len(potential)}):")
        print(f"  (assignments not in canonical_constants.py — add or ignore)")
        for r in potential:
            print(f"    {r['script']}:{r['line']}  {r['detail']}")

    n_scanned = len(set(r['script'] for r in audit_results))
    print(f"\n  Scripts scanned: {n_scanned}")
    print(f"  Compliant: {len(imports_ok)}, Violations: {len(violations)}, "
          f"Potential: {len(potential)}")
    print("=" * 60)


# ---------------------------------------------------------------------------
# Stats
# ---------------------------------------------------------------------------

def print_stats(index: dict):
    """Print summary statistics."""
    theorems = index.get("theorems", [])
    dead = index.get("closed_mechanisms", [])
    gates = index.get("gates", [])
    sessions = index.get("sessions", [])
    provenance = index.get("data_provenance", [])
    open_ch = index.get("open_channels", [])
    traj = index.get("probability_trajectory", [])

    closures = sum(1 for g in gates
                    if any(kw in g.get("verdict", "").upper()
                           for kw in ("KILL", "CLOSED", "CLOSURE")))
    passes = sum(1 for g in gates if "PASS" in g.get("verdict", "").upper())
    fails = sum(1 for g in gates if "FAIL" in g.get("verdict", "").upper())

    print("=" * 60)
    print("KNOWLEDGE INDEX STATISTICS")
    print("=" * 60)
    print(f"  Theorems (PROVEN):      {len(theorems)}")
    print(f"  Closed mechanisms:      {len(dead)}")
    print(f"  Gate verdicts:          {len(gates)}")
    print(f"    CLOSED:               {closures}")
    print(f"    PASS:                 {passes}")
    print(f"    FAIL:                 {fails}")
    print(f"    Other:                {len(gates) - closures - passes - fails}")
    print(f"  Closure-to-pass ratio:  {closures}:{passes}" +
          (f" ({closures/passes:.1f}:1)" if passes > 0 else ""))
    print(f"  Sessions indexed:       {len(sessions)}")
    print(f"  Probability points:     {len(traj)}")
    print(f"  Data provenance:        {len(provenance)}")
    print(f"    Scripts:              {sum(1 for p in provenance if p.get('script'))}")
    print(f"    Outputs:              {sum(len(p.get('outputs', [])) for p in provenance)}")
    print(f"  Open channels:          {len(open_ch)}")
    researchers = index.get("researchers", [])
    total_papers = sum(r.get("paper_count", 0) for r in researchers)
    total_citations = sum(r.get("citation_count", 0) for r in researchers)
    print(f"  Researchers:            {len(researchers)}")
    print(f"    Total papers:         {total_papers}")
    print(f"    Cross-citations:      {total_citations}")
    equations = index.get("equations", [])
    eq_types = {}
    for eq in equations:
        t = eq.get("type", "unknown")
        eq_types[t] = eq_types.get(t, 0) + 1
    named = sum(1 for eq in equations if eq.get("name"))
    print(f"  Equations:              {len(equations)}")
    print(f"    Named:                {named}")
    for t, c in sorted(eq_types.items(), key=lambda x: -x[1]):
        print(f"    {t:22s}{c}")
    print(f"  Generated:              {index.get('generated', 'N/A')}")
    print("=" * 60)


# ---------------------------------------------------------------------------
# Main extraction pipeline
# ---------------------------------------------------------------------------

def _is_sessions_file(filepath: Path) -> bool:
    """Check if filepath is under SESSIONS_DIR."""
    try:
        filepath.resolve().relative_to(SESSIONS_DIR.resolve())
        return True
    except ValueError:
        return False


def collect_files() -> list[Path]:
    """Collect all files to process, sorted by priority (low first, high last)."""
    files = []

    if SESSIONS_DIR.exists():
        for f in SESSIONS_DIR.rglob("*.md"):
            files.append(f)
        for f in SESSIONS_DIR.rglob("*.txt"):
            files.append(f)

    for tier0 in [TIER0_DIR, TIER0_ARCHIVE_DIR]:
        if tier0.exists():
            for f in tier0.iterdir():
                if f.suffix == ".txt":
                    files.append(f)

    # Sort by priority ascending (low priority processed first; high priority
    # processed last so they win deduplication)
    files.sort(key=lambda f: (get_priority(f), f.name))
    return files


def build_index(files: list[Path] | None = None) -> dict:
    """Build the full knowledge index from source files."""
    if files is None:
        files = collect_files()

    all_theorems = []
    all_closed = []
    all_gates = []
    all_sessions = []
    all_trajectory = []
    all_open = []
    all_citations = []
    all_equations = []

    for filepath in files:
        try:
            text = filepath.read_text(encoding="utf-8", errors="replace")
        except Exception as e:
            print(f"  WARN: Could not read {filepath.name}: {e}")
            continue

        # Session metadata (from sessions .md files only)
        if filepath.suffix == ".md" and _is_sessions_file(filepath):
            session = extract_session_metadata(filepath, text)
            if session:
                all_sessions.append(session)

        # PROVEN theorems
        theorems = extract_proven_theorems(filepath, text)
        all_theorems.extend(theorems)

        # CLOSED mechanisms
        dead = extract_closed_mechanisms(filepath, text)
        all_closed.extend(dead)

        # Gate verdicts
        gates = extract_gates(filepath, text)
        all_gates.extend(gates)

        # Probability trajectory
        traj = extract_probability_trajectory(filepath, text)
        all_trajectory.extend(traj)

        # OPEN channels
        open_ch = extract_open_channels(filepath, text)
        all_open.extend(open_ch)

        # Researcher citations in meeting minutes
        if filepath.suffix == ".md" and _is_sessions_file(filepath):
            citations = extract_researcher_citations(filepath, text)
            all_citations.extend(citations)

        # Equations (from all file types)
        equations = extract_equations(filepath, text)
        all_equations.extend(equations)

    # Also extract equations from tier0 Python scripts (not in the minutes file list)
    for tier0 in [TIER0_DIR, TIER0_ARCHIVE_DIR]:
        if tier0.exists():
            for pyf in sorted(tier0.glob("*.py")):
                if pyf in [f for f in files]:  # skip if already processed
                    continue
                try:
                    py_text = pyf.read_text(encoding="utf-8", errors="replace")
                    equations = extract_equations(pyf, py_text)
                    all_equations.extend(equations)
                except Exception:
                    pass

    # Also extract from artifacts
    if ARTIFACTS_DIR.exists():
        for artf in sorted(ARTIFACTS_DIR.glob("*.md")):
            if artf in [f for f in files]:
                continue
            try:
                art_text = artf.read_text(encoding="utf-8", errors="replace")
                equations = extract_equations(artf, art_text)
                all_equations.extend(equations)
            except Exception:
                pass

    # Data provenance from filesystem scan (both active and archive)
    provenance = extract_data_provenance(TIER0_DIR)
    if TIER0_ARCHIVE_DIR.exists():
        provenance.extend(extract_data_provenance(TIER0_ARCHIVE_DIR))

    # Researcher directory inventory
    researchers = extract_researcher_index(RESEARCHERS_DIR)

    # Cross-map: count citations per researcher domain
    citation_counts: dict[str, int] = {}
    citation_sessions: dict[str, set] = {}
    for c in all_citations:
        d = c["domain"]
        citation_counts[d] = citation_counts.get(d, 0) + 1
        if c.get("session"):
            citation_sessions.setdefault(d, set()).add(c["session"])

    for r in researchers:
        d = r["domain"]
        r["citation_count"] = citation_counts.get(d, 0)
        r["cited_in_sessions"] = sorted(citation_sessions.get(d, set()))

    # Deduplicate (later/higher-priority files win)
    all_theorems = dedup_by_name(all_theorems, "name")
    all_closed = dedup_by_name(all_closed, "name")
    all_gates = dedup_by_name(all_gates, "id")
    all_sessions = dedup_by_name(all_sessions, "id")
    all_open = dedup_by_name(all_open, "name")
    all_equations = dedup_equations(all_equations)

    # Re-number IDs after dedup
    for i, t in enumerate(all_theorems, 1):
        t["id"] = f"proven_{i}"
    for i, d in enumerate(all_closed, 1):
        d["id"] = f"closed_{i}"

    index = {
        "$schema": "knowledge-index-v1",
        "generated": datetime.now().isoformat(),
        "theorems": all_theorems,
        "closed_mechanisms": all_closed,
        "gates": all_gates,
        "probability_trajectory": all_trajectory,
        "sessions": all_sessions,
        "data_provenance": provenance,
        "open_channels": all_open,
        "researchers": researchers,
        "equations": all_equations,
    }

    return index


def merge_curated_from_existing(new_index: dict, existing_index: dict):
    """Transplant curated fields from existing index into new index.

    This prevents full rebuilds from discarding manually-added annotations
    like 'errata' on any entity type, and 'name'/'latex'/'audit_status'
    on equations.

    Matching is by normalized name (for named entities) or normalized raw
    content (for equations).
    """
    # --- Equations: match by normalized raw ---
    _EQ_CURATED = ("name", "latex", "audit_status", "errata")
    old_eqs = {}
    for eq in existing_index.get("equations", []):
        norm = _normalize_equation(eq.get("raw", ""))
        if norm:
            old_eqs[norm] = eq

    transplanted_eq = 0
    for eq in new_index.get("equations", []):
        norm = _normalize_equation(eq.get("raw", ""))
        old = old_eqs.get(norm)
        if old:
            for field in _EQ_CURATED:
                old_val = old.get(field)
                new_val = eq.get(field)
                if old_val and not new_val:
                    eq[field] = old_val
                    transplanted_eq += 1

    # --- Named entities: match by normalized name, transplant errata ---
    _GENERAL_CURATED = ("errata",)
    _NAMED_KEYS = {
        "theorems": "name",
        "closed_mechanisms": "name",
        "gates": "id",
        "open_channels": "name",
        "sessions": "id",
        "data_provenance": "script",
        "researchers": "domain",
    }

    transplanted_gen = 0
    for entity_type, match_key in _NAMED_KEYS.items():
        old_map = {}
        for ent in existing_index.get(entity_type, []):
            k = _normalize_for_dedup(ent.get(match_key, ""))
            if k:
                old_map[k] = ent

        for ent in new_index.get(entity_type, []):
            k = _normalize_for_dedup(ent.get(match_key, ""))
            old = old_map.get(k)
            if old:
                for field in _GENERAL_CURATED:
                    old_val = old.get(field)
                    new_val = ent.get(field)
                    if old_val and not new_val:
                        ent[field] = old_val
                        transplanted_gen += 1

    if transplanted_eq or transplanted_gen:
        print(f"  Curated fields preserved: {transplanted_eq} equation, "
              f"{transplanted_gen} general")


def write_index(index: dict, path: Path | None = None):
    """Write the index to JSON."""
    path = path or INDEX_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2, ensure_ascii=False)
    print(f"Index written to {path}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Knowledge Index Extractor for Phonon-Exflation Project"
    )
    parser.add_argument(
        "--incremental", action="store_true",
        help="Incremental update (requires --file)"
    )
    parser.add_argument(
        "--file", type=str,
        help="Single file to process in incremental mode"
    )
    parser.add_argument(
        "--validate", action="store_true",
        help="Run consistency checks on the index"
    )
    parser.add_argument(
        "--stats", action="store_true",
        help="Print index statistics"
    )
    parser.add_argument(
        "--audit-constants", action="store_true",
        help="Audit S34+ scripts for stale hardcoded constants"
    )
    parser.add_argument(
        "--output", type=str,
        help="Override output path (default: tools/knowledge-index.json)"
    )

    args = parser.parse_args()
    output_path = Path(args.output) if args.output else INDEX_PATH

    if args.audit_constants:
        audit_results = audit_canonical_constants(TIER0_DIR) + audit_canonical_constants(TIER0_ARCHIVE_DIR)
        print_constants_audit(audit_results)
        violations = [r for r in audit_results
                      if r["pattern"] not in ("IMPORT_OK", "POTENTIAL_HARDCODE")]
        if violations:
            print(f"\n{len(violations)} violation(s) — fix with "
                  f"'from canonical_constants import ...'")
        return

    if args.validate:
        if not output_path.exists():
            print(f"ERROR: Index not found at {output_path}. Run without --validate first.")
            return
        index = json.loads(output_path.read_text(encoding="utf-8"))
        violations = validate_index(index)
        if violations:
            print(f"VALIDATION: {len(violations)} violation(s) found:")
            for v in violations:
                print(f"  - {v}")
        else:
            print("VALIDATION: 0 violations. Index is consistent.")
        # Also run canonical constants audit
        print()
        audit_results = audit_canonical_constants(TIER0_DIR) + audit_canonical_constants(TIER0_ARCHIVE_DIR)
        print_constants_audit(audit_results)
        return

    if args.stats:
        if not output_path.exists():
            print(f"ERROR: Index not found at {output_path}. Run without --stats first.")
            return
        index = json.loads(output_path.read_text(encoding="utf-8"))
        print_stats(index)
        return

    if args.incremental and args.file:
        # Incremental: load existing index, re-extract from one file, merge
        if output_path.exists():
            index = json.loads(output_path.read_text(encoding="utf-8"))
        else:
            index = build_index(files=[])

        filepath = Path(args.file)
        if not filepath.is_absolute():
            filepath = PROJECT_ROOT / filepath
        if not filepath.exists():
            print(f"ERROR: File not found: {filepath}")
            return

        print(f"Incremental update from: {filepath.name}")
        new_index = build_index(files=[filepath])

        # Merge: for each entity type, combine and re-dedup
        for key in ["theorems", "closed_mechanisms", "gates", "sessions",
                     "probability_trajectory", "open_channels", "equations"]:
            existing = index.get(key, [])
            new_items = new_index.get(key, [])
            combined = existing + new_items
            if key in ("theorems",):
                combined = dedup_by_name(combined, "name")
            elif key in ("closed_mechanisms",):
                combined = dedup_by_name(combined, "name")
            elif key in ("gates",):
                combined = dedup_by_name(combined, "id")
            elif key in ("sessions",):
                combined = dedup_by_name(combined, "id")
            elif key in ("open_channels",):
                combined = dedup_by_name(combined, "name")
            elif key in ("equations",):
                combined = dedup_equations(combined)
            index[key] = combined

        index["generated"] = datetime.now().isoformat()
        write_index(index, output_path)
        print_stats(index)
        return

    # Full rebuild
    print("Full index rebuild...")
    files = collect_files()
    print(f"  Processing {len(files)} files...")

    # Load existing index to preserve curated fields (errata, equation names)
    existing_index = None
    if output_path.exists():
        try:
            existing_index = json.loads(output_path.read_text(encoding="utf-8"))
            print("  Loaded existing index for curated field preservation")
        except Exception:
            pass

    index = build_index(files)

    if existing_index:
        merge_curated_from_existing(index, existing_index)

    write_index(index, output_path)
    print()

    # Auto-validate
    violations = validate_index(index)
    if violations:
        print(f"\nVALIDATION: {len(violations)} violation(s):")
        for v in violations:
            print(f"  - {v}")
    else:
        print("\nVALIDATION: 0 violations.")

    # Canonical constants audit (S34+ enforcement)
    print()
    audit_results = audit_canonical_constants(TIER0_DIR) + audit_canonical_constants(TIER0_ARCHIVE_DIR)
    index["constants_audit"] = audit_results
    # Re-write index with audit results included
    write_index(index, output_path)
    print_constants_audit(audit_results)

    print()
    print_stats(index)


if __name__ == "__main__":
    main()
