#!/usr/bin/env python3
"""Format-generation regex set + extractor functions (Phase 0 / Task #4).

Encodes the per-generation author-attribution extraction patterns identified
in tools/_format_generation_scan.py + targeted file reads of S16, S19, S22,
S78, S86, S88, S90, and the S86 alpha-s workshop.

Each generation contributes one or more extractor functions returning a list
of structured tuples (gate_id_or_section, agent_canonical_id, role, edge_type,
source_match_text).

Run `python tools/_format_generation_regex_set.py --self-test` to verify each
pattern against verbatim fixture strings from real session files.

This module is the foundation for the future
`tools/harvest_attribution_edges.py` harvester (Phase 1). It is dev-internal
(underscored) until self-test coverage is green and the dry-run counts
(Phase 0 / Task #5) match expectations.
"""
from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Optional, Tuple

# ---------------------------------------------------------------------------
# Canonical agent table
# ---------------------------------------------------------------------------

ROOT = Path(__file__).resolve().parent.parent
AGENTS_DIR = ROOT / ".claude" / "agents"


def load_canonical_agents() -> set[str]:
    """Read .claude/agents/*.md filenames as the canonical subagent ID set."""
    if not AGENTS_DIR.exists():
        return set()
    out = set()
    for p in AGENTS_DIR.glob("*.md"):
        out.add(p.stem)
    return out


CANONICAL_AGENTS = load_canonical_agents()

# Informal-name → canonical-ID alias table. Built from observed patterns
# across S01-S91. Keys are case-insensitive (we lowercase before lookup).
AGENT_ALIASES: dict[str, str] = {
    # gen-physicist family
    "gen-physicist":                "gen-physicist",
    "general":                      "gen-physicist",
    "physicist":                    "gen-physicist",
    "sim-specialist":               "gen-physicist",       # S16-era catch-all
    # kaluza-klein family
    "kk":                           "kaluza-klein-theorist",
    "kk-theorist":                  "kaluza-klein-theorist",
    "kaluza-klein":                 "kaluza-klein-theorist",
    "kaluza-klein-theorist":        "kaluza-klein-theorist",
    # baptista
    "baptista":                     "baptista-spacetime-analyst",
    "baptista-spacetime-analyst":   "baptista-spacetime-analyst",
    # berry
    "berry":                        "berry-geometric-phase-theorist",
    "berry-geometric-phase-theorist": "berry-geometric-phase-theorist",
    # connes
    "connes":                       "connes-ncg-theorist",
    "connes-ncg":                   "connes-ncg-theorist",
    "connes-ncg-theorist":          "connes-ncg-theorist",
    # cosmic web
    "cosmic-web":                   "cosmic-web-theorist",
    "cosmicweb":                    "cosmic-web-theorist",
    "cosmic-web-theorist":          "cosmic-web-theorist",
    # dirac
    "dirac":                        "dirac-antimatter-theorist",
    "dirac-antimatter-theorist":    "dirac-antimatter-theorist",
    # einstein
    "einstein":                     "einstein-theorist",
    "einstein-theorist":            "einstein-theorist",
    # feynman
    "feynman":                      "feynman-theorist",
    "feynman-theorist":             "feynman-theorist",
    # hawking
    "hawking":                      "hawking-theorist",
    "hawking-theorist":             "hawking-theorist",
    # kaku
    "kaku":                         "kaku-speculative-theorist",
    "kaku-speculative-theorist":    "kaku-speculative-theorist",
    # kitaev
    "kitaev":                       "kitaev-quantum-chaos-theorist",
    "kitaev-quantum-chaos-theorist": "kitaev-quantum-chaos-theorist",
    # landau
    "landau":                       "landau-condensed-matter-theorist",
    "landau-condensed-matter-theorist": "landau-condensed-matter-theorist",
    # little red dots
    "lrd":                          "little-red-dots-jwst-analyst",
    "little-red-dots":              "little-red-dots-jwst-analyst",
    "little-red-dots-jwst-analyst": "little-red-dots-jwst-analyst",
    # lizzi
    "lizzi":                        "lizzi-spectral-functional-theorist",
    "lizzi-spectral-functional-theorist": "lizzi-spectral-functional-theorist",
    # mack
    "mack":                         "mack-cosmic-bridge",
    "katie-mack":                   "mack-cosmic-bridge",
    "cosmic-bridge":                "mack-cosmic-bridge",
    "mack-cosmic-bridge":           "mack-cosmic-bridge",
    # nazarewicz
    "naz":                          "nazarewicz-nuclear-structure-theorist",
    "nazarewicz":                   "nazarewicz-nuclear-structure-theorist",
    "nazarewicz-nuclear-structure-theorist": "nazarewicz-nuclear-structure-theorist",
    # neutrino
    "neutrino":                     "neutrino-detection-specialist",
    "neutrino-detection":           "neutrino-detection-specialist",
    "neutrino-detection-specialist": "neutrino-detection-specialist",
    # paasch
    "paasch":                       "paasch-mass-quantization-analyst",
    "paasch-mass-quantization-analyst": "paasch-mass-quantization-analyst",
    # phonon-first
    "phonon-first":                 "phonon-first-cosmologist",
    "phonon-first-cosmologist":     "phonon-first-cosmologist",
    # quantum acoustics
    "qa":                           "quantum-acoustics-theorist",
    "quantum-acoustics":            "quantum-acoustics-theorist",
    "quantum-acoustics-theorist":   "quantum-acoustics-theorist",
    # quantum foam
    "quantum-foam":                 "quantum-foam-theorist",
    "quantum-foam-theorist":        "quantum-foam-theorist",
    # sagan
    "sagan":                        "sagan-empiricist",
    "sagan-empiricist":             "sagan-empiricist",
    # schwarzschild-penrose
    "schwarzschild-penrose":        "schwarzschild-penrose-geometer",
    "schwarzschild-penrose-geometer": "schwarzschild-penrose-geometer",
    "sp":                           "schwarzschild-penrose-geometer",
    "sp-geometer":                  "schwarzschild-penrose-geometer",
    # spectral geometer
    "spectral-geometer":            "spectral-geometer",
    "geometer":                     "spectral-geometer",
    # string theory
    "string-theory":                "string-theory-theorist",
    "string-theory-theorist":       "string-theory-theorist",
    # tesla
    "tesla":                        "tesla-resonance",
    "tesla-resonance":              "tesla-resonance",
    # transit dynamics
    "transit-dynamics":             "transit-dynamics-theorist",
    "transit-dynamics-theorist":    "transit-dynamics-theorist",
    # van den dungen
    "vdd":                          "van-den-dungen-bridge-theorist",
    "van-den-dungen":               "van-den-dungen-bridge-theorist",
    "dungen":                       "van-den-dungen-bridge-theorist",
    "van-den-dungen-bridge-theorist": "van-den-dungen-bridge-theorist",
    # volovik
    "volovik":                      "volovik-superfluid-universe-theorist",
    "volovik-superfluid-universe-theorist": "volovik-superfluid-universe-theorist",
    # meta-agents (not in .claude/agents/ but recognized in attribution)
    "orchestrator":                 "orchestrator",
    "team-lead":                    "orchestrator",
    "team_lead":                    "orchestrator",
}


def canonicalize_agent(raw: str) -> Optional[str]:
    """Map an informal agent name to its canonical subagent ID.

    Returns None when the raw string doesn't resolve. Strategy:
      1. Lowercase + strip
      2. Replace internal spaces with dashes
      3. Direct alias lookup
      4. Fuzzy match: trim known suffix words ("theorist", "analyst",
         "specialist", "geometer", "empiricist", "cosmologist", etc.)
         and retry
    """
    if not raw:
        return None
    cleaned = raw.lower().strip().rstrip(".").strip()
    cleaned = cleaned.replace(" ", "-").replace("_", "-")
    # Strip backticks + asterisks GLOBALLY (not just edges). Markdown
    # tends to embed these inside agent identifiers (`agent-id` notation,
    # **agent-id** bold). Edge-only strip leaves middle backticks intact
    # and breaks canonicalization at the suffix-loop step.
    cleaned = cleaned.replace("`", "").replace("*", "")
    cleaned = cleaned.strip().strip("-").strip()
    # Truncate at first parenthesis or comma
    for sep in ("(", ","):
        if sep in cleaned:
            cleaned = cleaned.split(sep, 1)[0].strip("-").strip()
    if cleaned in AGENT_ALIASES:
        return AGENT_ALIASES[cleaned]
    if cleaned in CANONICAL_AGENTS:
        return cleaned
    # Try without trailing role-suffix
    for suffix in ("-theorist", "-analyst", "-specialist", "-geometer",
                   "-empiricist", "-cosmologist", "-bridge", "-resonance"):
        if cleaned.endswith(suffix):
            stem = cleaned[: -len(suffix)]
            if stem in AGENT_ALIASES:
                return AGENT_ALIASES[stem]
    return None


# ---------------------------------------------------------------------------
# Role-tag vocabulary (G7+)
# ---------------------------------------------------------------------------

ROLE_VOCAB = {
    "PRIMARY":              "primary",
    "CO-AUTHOR":            "co_author",
    "CO-SIGN":              "co_sign",
    "CO-SIGN-WITH-NOTES":   "co_sign_with_notes",
    "ADVERSARIAL-REVIEW":   "adversarial_review",
    "ADVERSARIAL REVIEW":   "adversarial_review",
    "BLACKLISTED":          "blacklisted",
    "SOLE-WRITER":          "sole_writer",
}


# ---------------------------------------------------------------------------
# Per-generation extractor specifications
# ---------------------------------------------------------------------------

@dataclass
class AttributionEdge:
    """One emitted edge from an extractor pass."""
    edge_type: str                       # authored_by / co_authored_by / reviewed_by / participates_in / cites_prior_session / discussed_in / excluded_from / synthesized_by
    source_type: str                     # gates / theorems / sessions / files / workshops
    source_id: str                       # identifier of the source node
    target_type: str                     # researchers / sessions
    target_id: str                       # canonical agent / session id
    role: Optional[str] = None           # primary / co_author / ...
    confidence: str = "header-parsed"    # header-parsed / session-level-inference / filename-derived / provenance-block
    generation: str = ""                 # G1..G7
    match_text: str = ""                 # verbatim source fragment


# G1 — body-text mention frequency
G1_AGENT_RE = re.compile(
    r"\b(baptista|berry|connes|dirac|einstein|feynman|hawking|kaku|kitaev|"
    r"landau|lizzi|mack|nazarewicz|naz|paasch|sagan|spectral-geometer|"
    r"tesla|van-den-dungen|vdd|volovik|cosmic-web|gen-physicist|general|"
    r"phonon-first|quantum-acoustics|quantum-foam|kaluza-klein|kk|"
    r"schwarzschild-penrose|transit-dynamics|little-red-dots|lrd)\b",
    re.IGNORECASE,
)


# G2 — `## Authors` block + bulleted author list (S16 canonical form)
G2_AUTHORS_BLOCK_RE = re.compile(
    r"^##\s+Authors?\s*$"           # heading line
    r"(?P<body>(?:\n^-\s+.*$)+)",   # bulleted lines
    re.MULTILINE,
)
G2_AUTHOR_BULLET_RE = re.compile(
    r"^-\s+\*\*([^\*]+)\*\*(?:\s+\(([^)]+)\))?",
    re.MULTILINE,
)
# G2 sub-variant — `## Agents:` or `## Synthesis Team:` comma-list (S17/S18)
G2_AGENTS_LINE_RE = re.compile(
    r"^##\s+(?:Agents?|Synthesis\s+Team)\s*:\s*(?P<list>.+?)\s*$",
    re.MULTILINE | re.IGNORECASE,
)
# G2 sub-variant — deliverable table with `| Agent |` column (S17 line 21+)
# Detect a header row `| ... | Agent | ... |` then extract each data row's
# Agent-column value. The regex captures both header position discovery
# and individual rows.
G2_TABLE_HEADER_RE = re.compile(
    r"^\|([^\n]*\|\s*Agent\s*\|[^\n]*)\|\s*$",
    re.MULTILINE | re.IGNORECASE,
)
G2_TABLE_ROW_RE = re.compile(
    r"^\|([^\n]+)\|\s*$",
    re.MULTILINE,
)


# G5 sub-variant — gate-section heading with parenthetical agent:
#   ### HAWK-1: Zeta-Function Regularization Cross-Check (hawking-theorist)
# Captures (gate_id, agent_id) per heading.
G5_HEADING_AGENT_RE = re.compile(
    r"^#{2,4}\s+"
    r"(?P<gid>[A-Z][A-Z0-9-]{2,})"
    r"\s*:\s*[^()\n]+?\s*"
    r"\(\s*(?P<agent>[a-z][a-z0-9-]+)\s*\)\s*$",
    re.MULTILINE,
)


# G3-G5 — per-file `**Author**:` / `**Evaluator**:` / `**Subject**:`
G3_AUTHOR_RE = re.compile(
    r"^\*\*Author\*\*\s*:\s*(?P<name>[^\n(]+?)(?:\s*\((?P<paren>[^)]+)\))?\s*$",
    re.MULTILINE,
)
G3_EVALUATOR_RE = re.compile(
    r"^\*\*(?:Evaluator|Reviewer)\*\*\s*:\s*(?P<name>[^\n]+?)\s*$",
    re.MULTILINE,
)
G3_SUBJECT_RE = re.compile(
    r"^\*\*Subject\*\*\s*:\s*`?([^`\n]+?)`?\s*$",
    re.MULTILINE,
)
# Filename derivations
G3_FILENAME_AGENT_RE = re.compile(
    r"^session-\d+[a-z]?-([a-z][\w-]*?)-(?:collab|synthesis|verdict|wrapup|"
    r"constraint-audit|deepdive)(?:\.md$|-)",
    re.IGNORECASE,
)
G3_FILENAME_REVIEW_PAIR_RE = re.compile(
    r"^session-\d+[a-z]?-([a-z]+)-([a-z]+)-collab\.md$",
    re.IGNORECASE,
)


# G5 — wave-WP / cc-path / audit filenames
G5_WAVE_FILENAME_RE = re.compile(
    r"^session-(\d+)[a-z]?-wave(\d+)-workingpaper\.md$",
    re.IGNORECASE,
)
G5_AUDIT_FILENAME_RE = re.compile(
    r"^session-\d+[a-z]?-audit-([a-z][\w-]+)\.md$",
    re.IGNORECASE,
)
G5_CC_PATH_FILENAME_RE = re.compile(
    r"^cc-path-([a-z])\.md$",
)


# G6 — `**Owner**:` per-gate (S78+)
G6_OWNER_RE = re.compile(
    r"^\*\*Owner\*\*\s*:\s*(?P<value>[^\n]+?)\s*$",
    re.MULTILINE,
)
# Gate-section anchors used to bind an Owner: line to a gate-id
G6_GATE_HEADING_RE = re.compile(
    r"^#{2,4}\s+(?:§\s*)?"
    r"(?P<gid>(?:W\d+[a-z]?(?:-\d+)?[a-z]?|[A-Z][A-Z0-9-]{3,})"
    r"(?:[\s.:—-]+|$))",
    re.MULTILINE,
)


# G7 — `**Agent**:`, multi-author with roles, Provenance blocks
# Agent header captures the entire value after the colon to end-of-line so
# multi-author tuples like
#   **Agent**: `a` PRIMARY + `b` CO-AUTHOR (notes)
# are captured wholesale, then G7_ROLE_TUPLE_RE scans the captured value.
G7_AGENT_RE = re.compile(
    r"^\*\*Agent\*\*\s*:\s*(?P<value>.+?)\s*$",
    re.MULTILINE,
)
G7_AUTHOR_MULTI_RE = re.compile(
    r"^\*\*Author\*\*\s*:\s*(?P<value>.+?)\s*$",
    re.MULTILINE,
)
# Inline role tags inside Agent/Author values
G7_ROLE_TUPLE_RE = re.compile(
    r"`?([a-z][\w-]*?)`?\s+(PRIMARY|CO-AUTHOR|CO-SIGN-WITH-NOTES|"
    r"CO-SIGN|ADVERSARIAL\s+REVIEW|BLACKLISTED|sole[- ]writer)",
    re.IGNORECASE,
)
G7_PROVENANCE_RE = re.compile(
    r"^>\s+\*\*Provenance\*\*\s*:\s*(?P<value>.+?)$",
    re.MULTILINE,
)
G7_PROVENANCE_AGENT_RE = re.compile(
    r"`?([a-z][\w-]*?)`?\s+(?:sole[- ]writer|writer|primary|author)",
    re.IGNORECASE,
)
G7_PROVENANCE_SESSION_RE = re.compile(
    r"\bS(\d+)[a-z]?\b",
)
# Workshop format
G7_WORKSHOP_AGENTS_LINE_RE = re.compile(
    r"^\*\*Agents\*\*\s*:\s*(?P<value>.+?)$",
    re.MULTILINE,
)
G7_WORKSHOP_AGENT_ENTRY_RE = re.compile(
    r"([A-Za-z][\w-]*?)\s*\(([\w-]+)\)",
)
# S87+ variant — `**Agents**:` followed by bulleted agent list on subsequent
# lines (rather than comma-separated on the same line):
#   **Agents**:
#   - `connes-ncg-theorist` (W9c-1 cross-reviewer; ...)
#   - `lizzi-spectral-functional-theorist` (...)
G7_WORKSHOP_AGENTS_BULLET_RE = re.compile(
    r"^\*\*Agents\*\*\s*:\s*$\n"
    r"(?P<body>(?:^-\s+.*?$\n?)+)",
    re.MULTILINE,
)
G7_WORKSHOP_AGENT_BULLET_ENTRY_RE = re.compile(
    r"^-\s+`?([a-z][\w-]+)`?",
    re.MULTILINE,
)
G7_WORKSHOP_ROUND_HEADING_RE = re.compile(
    r"^##\s+Round\s+(\d+)(?:\.\d+)?\s*[—:-]\s*([a-z][\w-]*)",
    re.MULTILINE | re.IGNORECASE,
)
# G5 wave-WP / workshop title with agent-pair in H1 parenthetical:
#   # Session 61 — Wave 9: Framework Implications Workshop (QA x Connes)
#   # Session 61 — Wave 7: Results Synthesis Workshop (Volovik × Hawking)
# Captures the two agent short-names in groups (a, b).
G5_TITLE_AGENT_PAIR_RE = re.compile(
    r"^#\s+Session\s+\d+[a-z]?\s+[—-]\s+Wave\s+\d+[a-z]?:\s+.+?\s*"
    r"\(\s*([A-Za-z][\w-]+)\s+(?:x|×|&|and|vs\.?)\s+([A-Za-z][\w-]+)\s*\)",
    re.MULTILINE | re.IGNORECASE,
)


# ---------------------------------------------------------------------------
# Self-test fixtures — verbatim strings from real files (Phase 0 evidence)
# ---------------------------------------------------------------------------

FIXTURES = [
    # G2: S16 — `## Authors` block (lines 6-10 of session-16-final.md)
    {
        "name": "G2-S16-authors-block",
        "generation": "G2",
        "text": (
            "# Session 16: Final Workshop Synthesis\n"
            "\n"
            "## Authors\n"
            "- **Gen-Physicist** (designated writer, master priority ranking, Bayesian analysis)\n"
            "- **KK-Theorist** (geometric assessment, corrections, Session 17 seeds)\n"
            "- **Sim-Specialist** (implementation roadmap, risk analysis, code specifications)\n"
            "- **Sagan-Empiricist** (Venus Rule audit, pre-registration integrity, empirical assessment)\n"
        ),
        # extract_g2 deduplicates per session, so the 4 bullets (Gen-Physicist,
        # KK-Theorist, Sim-Specialist, Sagan-Empiricist) collapse to 3 canonical
        # IDs — Sim-Specialist is mapped to gen-physicist as an S16-era catch-all
        # alias, which is the same canonical ID as the first bullet.
        "expected_agents": [
            "gen-physicist", "kaluza-klein-theorist", "sagan-empiricist",
        ],
    },
    # G3: S19d — `**Author**: Berry-Geometric-Phase-Theorist` (line 2)
    {
        "name": "G3-S19-author-direct",
        "generation": "G3",
        "text": (
            "# Berry-Geometric-Phase-Theorist: Collaborative Review of Session 19d\n"
            "\n"
            "**Author**: Berry-Geometric-Phase-Theorist\n"
            "**Date**: 2026-02-15\n"
        ),
        "expected_agents": ["berry-geometric-phase-theorist"],
    },
    # G3: S22 — `**Author**: Berry (berry-geometric-phase-theorist)` parenthetical
    {
        "name": "G3-S22-author-parenthetical",
        "generation": "G3",
        "text": (
            "**Author**: Berry (berry-geometric-phase-theorist)\n"
        ),
        "expected_agents": ["berry-geometric-phase-theorist"],
    },
    # G3: S19d feynman-quantum-acoustics-collab — `**Evaluator**: Feynman-Theorist`
    {
        "name": "G3-S19-evaluator",
        "generation": "G3",
        "text": (
            "# Feynman Evaluation of Quantum-Acoustics Collaborative Review (Session 19d)\n"
            "\n"
            "**Date**: 2026-02-15\n"
            "**Evaluator**: Feynman-Theorist\n"
            "**Subject**: `sessions/QuantumAcoustics-Collab-19d.md`\n"
            "**Posture**: Blind evaluation. Honest physics, no cheerleading.\n"
        ),
        "expected_agents": ["feynman-theorist"],
    },
    # G3: S40 parenthetical with role-words
    {
        "name": "G3-S40-author-paren-roles",
        "generation": "G3",
        "text": "**Author**: Baptista (Spacetime Analysis, KK Geometry, Metric Spaces)\n",
        "expected_agents": ["baptista-spacetime-analyst"],
    },
    # G4: S50 — orchestrator self-attribution
    {
        "name": "G4-S50-team-lead",
        "generation": "G4",
        "text": "**Author**: Team-lead (direct synthesis)\n",
        "expected_agents": ["orchestrator"],
    },
    # G4: S58 — agent with title format
    {
        "name": "G4-S58-mack-cosmic-bridge",
        "generation": "G4",
        "text": "**Author**: Katie Mack (Cosmic Bridge Agent)\n",
        "expected_agents": ["mack-cosmic-bridge"],
    },
    # G6: S78 — Owner per gate, real subagent id
    {
        "name": "G6-S78-owner-transit-dynamics",
        "generation": "G6",
        "text": "**Owner**: transit-dynamics-theorist\n",
        "expected_agents": ["transit-dynamics-theorist"],
    },
    # G6: S78 — Owner is wave-synthesized (NON-agent value)
    {
        "name": "G6-S78-owner-non-agent",
        "generation": "G6",
        "text": "**Owner**: synthesized across Wave 1 (not a single-agent gate)\n",
        "expected_agents": [],   # no agent extractable; should emit synthesized_by edge
    },
    # G7: S86 — Agent quoted
    {
        "name": "G7-S86-agent-backticked",
        "generation": "G7",
        "text": "**Agent**: `kaku-speculative-theorist` (primary, executed)\n",
        "expected_agents": ["kaku-speculative-theorist"],
    },
    # G7: S88 — multi-author with role tags
    {
        "name": "G7-S88-multi-author-roles",
        "generation": "G7",
        "text": "**Author**: volovik PRIMARY; connes CO-AUTHOR; hawking BLACKLISTED\n",
        "expected_agents": [
            "volovik-superfluid-universe-theorist",
            "connes-ncg-theorist",
            "hawking-theorist",
        ],
    },
    # G7: S88 — Agent with PRIMARY + CO-AUTHOR inline
    {
        "name": "G7-S88-agent-primary-coauthor",
        "generation": "G7",
        "text": (
            "**Agent**: `lizzi-spectral-functional-theorist` PRIMARY + "
            "`connes-ncg-theorist` CO-AUTHOR (NCG-axiomatic side per "
            "Chamseddine-Connes 1996)\n"
        ),
        "expected_agents": [
            "lizzi-spectral-functional-theorist",
            "connes-ncg-theorist",
        ],
    },
    # G7: S90 — Provenance block
    {
        "name": "G7-S90-provenance",
        "generation": "G7",
        "text": (
            "> **Provenance**: S89 W7c (`mack-cosmic-bridge` sole writer "
            "per joint-theorem-promotion §Stage 2; this rule promotion lifts "
            "the K=3 calibration)\n"
        ),
        "expected_agents": ["mack-cosmic-bridge"],
        "expected_session_cite": "89",
    },
    # G2 sub-variant — `## Agents:` comma-list (S17 line 5)
    {
        "name": "G2-S17-agents-line",
        "generation": "G2",
        "text": (
            "## Date: 2026-02-14\n"
            "## Session: 17 (Phases a-d)\n"
            "## Agents: Baptista-Spacetime-Analyst, Hawking-Theorist, "
            "Schwarzschild-Penrose-Geometer, Dirac-Antimatter-Theorist\n"
        ),
        "expected_agents": [
            "baptista-spacetime-analyst",
            "hawking-theorist",
            "schwarzschild-penrose-geometer",
            "dirac-antimatter-theorist",
        ],
    },
    # G2 sub-variant — `## Synthesis Team:` with role parens (S17 line 6)
    {
        "name": "G2-S17-synthesis-team",
        "generation": "G2",
        "text": (
            "## Synthesis Team: KK-Theorist (structural), "
            "Hawking-Theorist (thermodynamic/writer), "
            "Sagan-Empiricist (evidential)\n"
        ),
        "expected_agents": [
            "kaluza-klein-theorist",
            "hawking-theorist",
            "sagan-empiricist",
        ],
    },
    # G2 sub-variant — deliverable-table `| Agent |` column (S17 line 21+)
    {
        "name": "G2-S17-deliverable-table",
        "generation": "G2",
        "text": (
            "| # | ID | Phase | Deliverable | Agent | Key Result |\n"
            "|:--|:---|:------|:------------|:------|:-----------|\n"
            "| 1 | B-1 | 17a | Gauge coupling | Baptista | g_1/g_2 = e^{-2s}. |\n"
            "| 3 | H-1 | 17a | CW V_eff | Hawking | 0/40 raw minima. |\n"
            "| 5 | SP-1 | 17a | Explicit metric | SP-Geometer | diag(...) |\n"
            "| 7 | D-1 | 17a | J-compat audit | Dirac | [J,D_K]=0 |\n"
        ),
        "expected_agents": [
            "baptista-spacetime-analyst",
            "hawking-theorist",
            "schwarzschild-penrose-geometer",
            "dirac-antimatter-theorist",
        ],
    },
    # G5 per-gate — section heading with parenthetical agent (S61 wave2 line 23)
    {
        "name": "G5-S61-heading-paren-agent",
        "generation": "G5-per-gate",
        "text": (
            "## Lane 1: a_2 Cross-Check Gauntlet\n"
            "\n"
            "### HAWK-1: Zeta-Function Regularization Cross-Check of a_2 "
            "(hawking-theorist)\n"
            "\n"
            "### KK-2: Geometric a_2 evaluation on Jensen fiber "
            "(kaluza-klein-theorist)\n"
        ),
        "expected_agents": [
            "hawking-theorist",
            "kaluza-klein-theorist",
        ],
    },
    # G7: S86 workshop — Agents line + Round heading.
    # Expected edges: 2 participates_in (connes, volovik) + 1 authored_round
    # (connes). connes appears twice because the structural fact is "connes
    # is BOTH a workshop participant AND the author of Round 1" — both
    # are real edges with distinct edge_type values.
    {
        "name": "G7-S86-workshop-agents-and-round",
        "generation": "G7",
        "text": (
            "**Format**: Iterative 2-agent workshop (3 rounds, 6 turns)\n"
            "**Agents**: connes (connes-ncg-theorist), volovik "
            "(volovik-superfluid-universe-theorist)\n"
            "\n"
            "## Round 1 — connes: Opening Analysis\n"
            "\n"
            "### C1: Identity Exactness — Is α_s = n_s² − 1 Exact at Substrate Level?\n"
        ),
        "expected_agents": [
            "connes-ncg-theorist",                  # participates_in
            "volovik-superfluid-universe-theorist", # participates_in
            "connes-ncg-theorist",                  # authored_round 1
        ],
        "expected_rounds": [(1, "connes-ncg-theorist")],
    },
]


# ---------------------------------------------------------------------------
# Extractor functions (one per generation)
# ---------------------------------------------------------------------------

def extract_g2(text: str, session_id: str) -> List[AttributionEdge]:
    """G2 extractor — covers three sub-variants:
      (a) `## Authors` bulleted block (S16 canonical)
      (b) `## Agents:` / `## Synthesis Team:` comma-list (S17/S18)
      (c) deliverable table with `| Agent |` column (S17 line 21+)
    Each agent encountered emits one `authored_by: session → researcher`.
    """
    out: list[AttributionEdge] = []
    seen: set[str] = set()

    def emit(cid: str, match: str) -> None:
        if cid is None or cid in seen:
            return
        seen.add(cid)
        out.append(AttributionEdge(
            edge_type="authored_by",
            source_type="sessions",
            source_id=session_id,
            target_type="researchers",
            target_id=cid,
            role="primary",
            confidence="header-parsed",
            generation="G2",
            match_text=match,
        ))

    # (a) `## Authors` bulleted block
    block_m = G2_AUTHORS_BLOCK_RE.search(text)
    if block_m:
        body = block_m.group("body")
        for bm in G2_AUTHOR_BULLET_RE.finditer(body):
            cid = canonicalize_agent(bm.group(1).strip())
            if cid:
                emit(cid, bm.group(0).strip())

    # (b) `## Agents:` / `## Synthesis Team:` comma-list
    for am in G2_AGENTS_LINE_RE.finditer(text):
        lst = am.group("list")
        for token in lst.split(","):
            tok = token.strip()
            if not tok:
                continue
            # strip trailing parenthetical role-description
            cid = canonicalize_agent(tok.split("(")[0])
            if cid:
                emit(cid, am.group(0).strip())

    # (c) Deliverable table `| Agent |` column
    header_m = G2_TABLE_HEADER_RE.search(text)
    if header_m:
        # Determine column-index of `Agent` in the header
        cols = [c.strip() for c in header_m.group(1).split("|")]
        try:
            agent_col = next(i for i, c in enumerate(cols)
                              if c.lower().strip() == "agent")
        except StopIteration:
            agent_col = None
        if agent_col is not None:
            # Walk rows below the header. Skip the separator line `|----|----|`.
            for rm in G2_TABLE_ROW_RE.finditer(text, header_m.end()):
                row_cells = [c.strip() for c in rm.group(1).split("|")]
                if len(row_cells) <= agent_col:
                    continue
                cell = row_cells[agent_col]
                if not cell or set(cell) <= set(":- "):
                    continue
                # Multi-agent cells like "Hawking + Baptista" → split on +
                for sub in re.split(r"\s*[+/&]\s*", cell):
                    cid = canonicalize_agent(sub)
                    if cid:
                        emit(cid, f"table-row: {cell}")
    return out


def extract_g5_per_gate(text: str, file_id: str) -> List[AttributionEdge]:
    """G5 per-gate attribution from section heading with parenthetical agent:
       ### HAWK-1: Zeta-Function Regularization (hawking-theorist)
    Emits `authored_by: gate_id → researcher` for each matched heading.
    """
    out: list[AttributionEdge] = []
    for m in G5_HEADING_AGENT_RE.finditer(text):
        gid = m.group("gid").strip()
        cid = canonicalize_agent(m.group("agent"))
        if cid is None:
            continue
        out.append(AttributionEdge(
            edge_type="authored_by",
            source_type="gates",
            source_id=gid,
            target_type="researchers",
            target_id=cid,
            role="primary",
            confidence="header-parsed",
            generation="G5",
            match_text=m.group(0).strip(),
        ))
    return out


def extract_g3(text: str, file_id: str, filename: str) -> List[AttributionEdge]:
    out: list[AttributionEdge] = []
    # Author header
    for m in G3_AUTHOR_RE.finditer(text):
        raw = m.group("name").strip()
        cid = canonicalize_agent(raw)
        if cid is None:
            cid = canonicalize_agent(m.group("paren") or "")
        if cid is None:
            continue
        out.append(AttributionEdge(
            edge_type="authored_by",
            source_type="files",
            source_id=file_id,
            target_type="researchers",
            target_id=cid,
            role="primary",
            confidence="header-parsed",
            generation="G3",
            match_text=m.group(0).strip(),
        ))
    # Evaluator header — emit reviewed_by
    for m in G3_EVALUATOR_RE.finditer(text):
        cid = canonicalize_agent(m.group("name"))
        if cid is None:
            continue
        out.append(AttributionEdge(
            edge_type="reviewed_by",
            source_type="files",
            source_id=file_id,
            target_type="researchers",
            target_id=cid,
            role="adversarial_review",
            confidence="header-parsed",
            generation="G3",
            match_text=m.group(0).strip(),
        ))
    # Filename fallback when no header present
    if not out:
        fm = G3_FILENAME_AGENT_RE.match(filename)
        if fm:
            cid = canonicalize_agent(fm.group(1))
            if cid:
                out.append(AttributionEdge(
                    edge_type="authored_by",
                    source_type="files",
                    source_id=file_id,
                    target_type="researchers",
                    target_id=cid,
                    role="primary",
                    confidence="filename-derived",
                    generation="G3",
                    match_text=filename,
                ))
    return out


def extract_g6(text: str, file_id: str) -> List[AttributionEdge]:
    """Per-gate `**Owner**:` extractor. Binds each Owner: line to the nearest
    preceding gate-section heading (§W{N}-{M} or canonical-ID-shape heading).
    """
    out: list[AttributionEdge] = []
    # Pre-compute (offset, gate_id) for every heading.
    headings: list[tuple[int, str]] = [
        (m.start(), m.group("gid").rstrip(": —.").strip())
        for m in G6_GATE_HEADING_RE.finditer(text)
    ]
    for m in G6_OWNER_RE.finditer(text):
        val = m.group("value").strip()
        cid = canonicalize_agent(val)
        # Find nearest preceding heading
        gate_id = None
        for off, gid in reversed(headings):
            if off < m.start():
                gate_id = gid
                break
        if cid is None:
            # Owner is non-agent (synthesized across Wave N etc.) — emit
            # synthesized_by edge to wave node (deferred — wave id derived
            # from gate_id prefix). For self-test purposes we still emit
            # nothing in expected_agents; the synthesized_by edge tracks
            # separately.
            if gate_id:
                out.append(AttributionEdge(
                    edge_type="synthesized_by",
                    source_type="gates",
                    source_id=gate_id,
                    target_type="sessions",
                    target_id="(wave-synthesis)",
                    role="orchestrator",
                    confidence="header-parsed",
                    generation="G6",
                    match_text=m.group(0).strip(),
                ))
            continue
        out.append(AttributionEdge(
            edge_type="authored_by",
            source_type="gates" if gate_id else "files",
            source_id=gate_id or file_id,
            target_type="researchers",
            target_id=cid,
            role="primary",
            confidence="header-parsed",
            generation="G6",
            match_text=m.group(0).strip(),
        ))
    return out


def extract_g7(text: str, file_id: str) -> List[AttributionEdge]:
    """G7 multi-pattern extractor: Agent: / Author: (multi-author tuple) /
    Provenance: blocks. Each pattern emits its own edge type; the inline
    role-tag tuple matching handles PRIMARY/CO-AUTHOR/CO-SIGN/etc."""
    out: list[AttributionEdge] = []
    # **Agent**: line — primary attribution; check for inline role tuples
    for m in G7_AGENT_RE.finditer(text):
        val = m.group("value").strip()
        role_tuples = list(G7_ROLE_TUPLE_RE.finditer(val))
        if role_tuples:
            for rm in role_tuples:
                cid = canonicalize_agent(rm.group(1))
                if cid is None:
                    continue
                role = ROLE_VOCAB.get(rm.group(2).upper().replace(" ", "-"), rm.group(2).lower())
                edge_type = "authored_by" if role == "primary" else (
                    "co_authored_by" if role.startswith("co_") else
                    "reviewed_by" if role == "adversarial_review" else
                    "excluded_from" if role == "blacklisted" else
                    "authored_by"
                )
                out.append(AttributionEdge(
                    edge_type=edge_type,
                    source_type="gates",
                    source_id=file_id,
                    target_type="researchers",
                    target_id=cid,
                    role=role,
                    confidence="header-parsed",
                    generation="G7",
                    match_text=m.group(0).strip(),
                ))
        else:
            # Plain `**Agent**: <id>`
            cid = canonicalize_agent(val)
            if cid:
                out.append(AttributionEdge(
                    edge_type="authored_by",
                    source_type="gates",
                    source_id=file_id,
                    target_type="researchers",
                    target_id=cid,
                    role="primary",
                    confidence="header-parsed",
                    generation="G7",
                    match_text=m.group(0).strip(),
                ))
    # **Author**: line with multi-author semicolon list
    for m in G7_AUTHOR_MULTI_RE.finditer(text):
        val = m.group("value").strip()
        clauses = [c.strip() for c in val.split(";")]
        for clause in clauses:
            tm = G7_ROLE_TUPLE_RE.search(clause)
            if tm:
                cid = canonicalize_agent(tm.group(1))
                if cid is None:
                    continue
                role = ROLE_VOCAB.get(tm.group(2).upper().replace(" ", "-"), tm.group(2).lower())
                edge_type = "authored_by" if role == "primary" else (
                    "co_authored_by" if role.startswith("co_") else
                    "reviewed_by" if role == "adversarial_review" else
                    "excluded_from" if role == "blacklisted" else
                    "authored_by"
                )
                out.append(AttributionEdge(
                    edge_type=edge_type,
                    source_type="gates",
                    source_id=file_id,
                    target_type="researchers",
                    target_id=cid,
                    role=role,
                    confidence="header-parsed",
                    generation="G7",
                    match_text=m.group(0).strip(),
                ))
            else:
                # Plain agent name (no role tag); treat as authored_by
                cid = canonicalize_agent(clause)
                if cid:
                    out.append(AttributionEdge(
                        edge_type="authored_by",
                        source_type="gates",
                        source_id=file_id,
                        target_type="researchers",
                        target_id=cid,
                        role="primary",
                        confidence="header-parsed",
                        generation="G7",
                        match_text=m.group(0).strip(),
                    ))
    # > **Provenance**: block — emit cites_prior_session + authored_by
    for m in G7_PROVENANCE_RE.finditer(text):
        val = m.group("value").strip()
        # Session cite
        sm = G7_PROVENANCE_SESSION_RE.search(val)
        if sm:
            out.append(AttributionEdge(
                edge_type="cites_prior_session",
                source_type="gates",
                source_id=file_id,
                target_type="sessions",
                target_id=sm.group(1),
                role=None,
                confidence="provenance-block",
                generation="G7",
                match_text=m.group(0).strip(),
            ))
        # Author within provenance
        am = G7_PROVENANCE_AGENT_RE.search(val)
        if am:
            cid = canonicalize_agent(am.group(1))
            if cid:
                out.append(AttributionEdge(
                    edge_type="authored_by",
                    source_type="gates",
                    source_id=file_id,
                    target_type="researchers",
                    target_id=cid,
                    role="sole_writer",
                    confidence="provenance-block",
                    generation="G7",
                    match_text=m.group(0).strip(),
                ))
    return out


def extract_workshop_g7(text: str, workshop_id: str) -> List[AttributionEdge]:
    """Parse the structured workshop format (G7+); handles three sub-variants:
       (a) `**Agents**:` comma-list on same line (S82-S86)
       (b) `**Agents**:` followed by bulleted list (S87+)
       (c) `## Round N — agent:` round-author binding (all G7)
    Also handles G5 wave-WP title with agent-pair in H1 parenthetical.
    """
    out: list[AttributionEdge] = []
    seen_participants: set[str] = set()

    def emit_participant(cid: str, match_text: str) -> None:
        if cid in seen_participants:
            return
        seen_participants.add(cid)
        out.append(AttributionEdge(
            edge_type="participates_in",
            source_type="researchers",
            source_id=cid,
            target_type="workshops",
            target_id=workshop_id,
            role="participant",
            confidence="header-parsed",
            generation="G7",
            match_text=match_text,
        ))

    # (a) Same-line `**Agents**:` comma-list
    am = G7_WORKSHOP_AGENTS_LINE_RE.search(text)
    if am:
        for em in G7_WORKSHOP_AGENT_ENTRY_RE.finditer(am.group("value")):
            short, canonical = em.group(1), em.group(2)
            cid = canonicalize_agent(canonical) or canonicalize_agent(short)
            if cid:
                emit_participant(cid, em.group(0).strip())
        # If the line has no `<short> (<canonical>)` matches, fall through to
        # the bullet variant (which may follow on subsequent lines)

    # (b) Bullet-list variant: `**Agents**:\n- `agent-id` (notes)\n...`
    bm = G7_WORKSHOP_AGENTS_BULLET_RE.search(text)
    if bm:
        for em in G7_WORKSHOP_AGENT_BULLET_ENTRY_RE.finditer(bm.group("body")):
            cid = canonicalize_agent(em.group(1))
            if cid:
                emit_participant(cid, em.group(0).strip())

    # G5 wave-WP title parenthetical: `# Session 61 — Wave 9: ... (QA x Connes)`
    tm = G5_TITLE_AGENT_PAIR_RE.search(text)
    if tm:
        for raw in (tm.group(1), tm.group(2)):
            cid = canonicalize_agent(raw)
            if cid:
                emit_participant(cid, tm.group(0).strip())

    # (c) Round-author bindings
    for rm in G7_WORKSHOP_ROUND_HEADING_RE.finditer(text):
        round_no = int(rm.group(1))
        cid = canonicalize_agent(rm.group(2))
        if cid is None:
            continue
        out.append(AttributionEdge(
            edge_type="authored_round",
            source_type="researchers",
            source_id=cid,
            target_type="workshops",
            target_id=f"{workshop_id}#round-{round_no}",
            role="round_author",
            confidence="header-parsed",
            generation="G7",
            match_text=rm.group(0).strip(),
        ))
    return out


# ---------------------------------------------------------------------------
# Self-test driver
# ---------------------------------------------------------------------------

def run_self_test() -> int:
    """Apply each fixture against the relevant extractor; report PASS/FAIL."""
    passed = 0
    failed = 0
    for fx in FIXTURES:
        text = fx["text"]
        gen = fx["generation"]
        expected = fx.get("expected_agents", [])
        if gen == "G2":
            edges = extract_g2(text, session_id="16")
        elif gen == "G3":
            edges = extract_g3(text, file_id="fixture", filename="session-19d-berry-collab.md")
        elif gen in ("G4", "G5"):
            edges = extract_g3(text, file_id="fixture", filename="session-fixture.md")
        elif gen == "G5-per-gate":
            edges = extract_g5_per_gate(text, file_id="fixture")
        elif gen == "G6":
            # Need a heading for gate-binding to fire; the per-gate binding
            # path requires a preceding heading. For Owner-only fixtures we
            # accept file-scoped edge as long as the agent is canonical.
            wrapped = "## §W1-2 Gate Heading\n" + text
            edges = extract_g6(wrapped, file_id="fixture")
        elif gen == "G7":
            if "Round" in text and "**Agents**:" in text:
                edges = extract_workshop_g7(text, workshop_id="s86-alpha-s-fixture")
            else:
                edges = extract_g7(text, file_id="fixture")
        else:
            edges = []

        # Researcher edges may have the researcher as either source
        # (participates_in workshops, authored_round) or target
        # (authored_by gates/files/sessions). Extract from whichever side.
        got: list[str] = []
        for e in edges:
            if e.source_type == "researchers":
                got.append(e.source_id)
            elif e.target_type == "researchers":
                got.append(e.target_id)
        if sorted(got) == sorted(expected):
            print(f"  PASS  {fx['name']:<40}  got {got}")
            passed += 1
        else:
            print(f"  FAIL  {fx['name']:<40}")
            print(f"        expected: {sorted(expected)}")
            print(f"        got:      {sorted(got)}")
            failed += 1

    print()
    print(f"Self-test: {passed} PASS, {failed} FAIL  ({len(FIXTURES)} total)")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        sys.exit(run_self_test())
    print(f"Canonical agents: {len(CANONICAL_AGENTS)}")
    print(f"Alias entries:    {len(AGENT_ALIASES)}")
    print(f"Fixtures:         {len(FIXTURES)}")
    print(f"Run with --self-test to verify pattern coverage.")
