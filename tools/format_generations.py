#!/usr/bin/env python3
"""format_generations.py - consolidated format-generation pipeline.

Replaces the four legacy scripts:
  - _format_generation_regex_set.py     (now: library backbone + self-test subcmd)
  - _format_generation_scan.py          (now: scan subcommand)
  - _format_generation_dry_run.py       (now: dry-run subcommand)
  - _format_generation_zero_coverage.py (now: zero-coverage subcommand)

Library functions (canonicalize_agent, ROLE_VOCAB, AttributionEdge, the G1-G7
regex set, extract_g2..g7, extract_workshop_g7) are exposed for import by
harvester.py's attribution subcommand.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple


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



# ===========================================================================
# SCAN - lifted from _format_generation_scan.py (renamed AGENT_NAMES->SCAN_AGENT_NAMES)
# ===========================================================================

# Agent identifiers seen in the project. Includes both short tracks
# (used in filenames like baptista-collab.md) and the canonical
# subagent IDs (.claude/agents/*.md filenames).
SCAN_AGENT_NAMES = [
    "baptista", "berry", "berry-geometric-phase-theorist",
    "connes", "connes-ncg-theorist",
    "cosmic-web", "cosmic-web-theorist",
    "dirac", "dirac-antimatter-theorist",
    "einstein", "einstein-theorist",
    "feynman", "feynman-theorist",
    "gen-physicist", "general", "physicist",
    "hawking", "hawking-theorist",
    "kaku", "kaku-speculative-theorist",
    "kaluza-klein", "kaluza-klein-theorist",
    "kitaev", "kitaev-quantum-chaos-theorist",
    "knowledge-weaver",
    "landau", "landau-condensed-matter-theorist",
    "little-red-dots", "little-red-dots-jwst-analyst",
    "lizzi", "lizzi-spectral-functional-theorist",
    "mack", "mack-cosmic-bridge",
    "nazarewicz", "naz", "nazarewicz-nuclear-structure-theorist",
    "neutrino-detection-specialist",
    "paasch", "paasch-mass-quantization-analyst",
    "phonon-first", "phonon-first-cosmologist",
    "quantum-acoustics", "quantum-acoustics-theorist",
    "quantum-foam", "quantum-foam-theorist",
    "sagan", "sagan-empiricist",
    "schwarzschild-penrose", "schwarzschild-penrose-geometer",
    "spectral-geometer", "geometer",
    "string-theory-theorist",
    "tesla", "tesla-resonance",
    "transit-dynamics", "transit-dynamics-theorist",
    "van-den-dungen", "van-den-dungen-bridge-theorist", "vdd", "dungen",
    "volovik", "volovik-superfluid-universe-theorist",
]
SCAN_AGENT_RE = re.compile(
    r"\b(" + "|".join(re.escape(a) for a in sorted(SCAN_AGENT_NAMES, key=len, reverse=True)) + r")\b",
    re.IGNORECASE,
)

# Filename archetypes
FILENAME_PATTERNS = [
    ("collab",            re.compile(r"-collab(?:-|\.md$|-addendum)")),
    ("synthesis",         re.compile(r"-synthesis(?:-|\.md$)")),
    ("workshop",          re.compile(r"-workshop(?:-|\.md$)")),
    ("workingpaper",      re.compile(r"-workingpaper\.md$")),
    ("master-synthesis",  re.compile(r"master-synthesis\.md$")),
    ("master-collab",     re.compile(r"master-collab\.md$")),
    ("results-workingpaper", re.compile(r"results-workingpaper\.md$")),
    ("final",             re.compile(r"-final\.md$")),
    ("wave-w-prefix",     re.compile(r"^session-[\dA-Za-z]+-w\d+[a-z]?")),
    ("session-final",     re.compile(r"session-[\d]+[a-z]?-final\.md$")),
    ("audit",             re.compile(r"-audit-|^audit-")),
    ("verdict",           re.compile(r"verdicts\.txt$|verdict\.md$")),
    ("sagan",             re.compile(r"sagan-(verdict|assessment|dismissal)")),
    ("quicklook",         re.compile(r"^quicklook-")),
    ("plan-block",        re.compile(r"-plan-w\d+[a-z]?\.md$")),
]

# Author-attribution patterns — read against actual file content
ATTRIBUTION_PATTERNS = [
    ("hdr-author-colon",
        re.compile(r"^(?:#+\s+)?(?:\*\*)?(?:Author|By|Authored\s*by|Synthesized\s*by|Written\s*by|Owner)(?:\*\*)?\s*:\s*(.+?)$",
                   re.IGNORECASE | re.MULTILINE)),
    ("bold-by",
        re.compile(r"\*\*(?:By|Author|Authors?)\*\*\s*:?\s*([^\n*]+)")),
    ("workshop-round",
        re.compile(r"^#+\s+(?:§\s*)?R(\d+)(?:-([A-Za-z][\w-]*))?(?:\s+([A-Za-z][\w-]+))?",
                   re.MULTILINE)),
    ("section-author-em-dash",
        re.compile(r"^#+\s+§?[\w.]+\s+[—-]\s+([a-z][\w-]+(?:-[a-z][\w-]+)*)\s*(?:$|[(\s])",
                   re.MULTILINE)),
    ("agent-block-prefix",
        re.compile(r"^#+\s+(\b(?:" + "|".join(SCAN_AGENT_NAMES) + r")\b)[\s:](.+)?$",
                   re.IGNORECASE | re.MULTILINE)),
    ("provenance-block",
        re.compile(r"^>\s*\*\*Provenance\*\*:?\s*(.+?)$",
                   re.IGNORECASE | re.MULTILINE)),
    ("agent-suffix-role",
        re.compile(r"\b([a-z][\w-]+)\s+\((?:author|primary|co-author|reviewer)\b",
                   re.IGNORECASE)),
    ("primary-coauthor",
        re.compile(r"\b(PRIMARY|CO-AUTHOR|CO-SIGN|ADVERSARIAL\s+REVIEW)\s+(?:by\s+)?([a-z][\w-]+(?:-[a-z][\w-]+)*)",
                   re.IGNORECASE)),
]


def fingerprint_session(sid: str, sess_dir: Path) -> dict:
    files = sorted([p for p in sess_dir.glob("*.md") if p.is_file()])
    archetype_counts: Counter = Counter()
    file_archetypes: List[str] = []
    for p in files:
        name = p.name
        matched_any = False
        for label, pat in FILENAME_PATTERNS:
            if pat.search(name):
                archetype_counts[label] += 1
                matched_any = True
        if not matched_any:
            archetype_counts["other"] += 1
        # Extract agent-token from filename if present
        # e.g. session-22-baptista-collab.md → baptista
        agent_hits = SCAN_AGENT_RE.findall(name)
        file_archetypes.append({
            "name": name,
            "size": p.stat().st_size,
            "filename_agents": list({a.lower() for a in agent_hits}),
        })

    # Content scan — read each file once, collect pattern hits + agent density
    attribution_counts: Counter = Counter()
    attribution_examples: Dict[str, List[str]] = {k: [] for k, _ in ATTRIBUTION_PATTERNS}
    agent_density: Counter = Counter()
    total_bytes = 0
    files_read = 0

    for p in files:
        try:
            text = p.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        total_bytes += len(text)
        files_read += 1
        for label, pat in ATTRIBUTION_PATTERNS:
            for m in pat.finditer(text):
                attribution_counts[label] += 1
                if len(attribution_examples[label]) < 3:
                    # Keep the full match line, capped at 200 chars
                    ex = m.group(0).strip()
                    if len(ex) > 200:
                        ex = ex[:197] + "…"
                    attribution_examples[label].append({
                        "file": p.name,
                        "match": ex,
                    })
        # Agent-name density
        for m in SCAN_AGENT_RE.finditer(text):
            agent_density[m.group(1).lower()] += 1

    return {
        "sid": sid,
        "dir": str(sess_dir.relative_to(ROOT)),
        "file_count": len(files),
        "total_bytes": total_bytes,
        "archetype_counts": dict(archetype_counts),
        "attribution_counts": dict(attribution_counts),
        "attribution_examples": attribution_examples,
        "top_agents_in_content": dict(agent_density.most_common(12)),
        "files_summary": file_archetypes[:30],  # cap for JSON size
    }


def run_scan() -> None:
    rows = []
    # Live sessions first (S52+), then archive (S01-S51).
    for top in [ROOT / "sessions", ROOT / "sessions" / "archive"]:
        if not top.exists():
            continue
        for d in sorted(top.glob("session-*")):
            if not d.is_dir():
                continue
            m = re.match(r"session-(\d+[a-z]?)", d.name)
            if not m:
                continue
            sid = m.group(1)
            rec = fingerprint_session(sid, d)
            rec["location"] = "archive" if "archive" in str(d) else "live"
            rows.append(rec)

    def sk(r):
        m = re.match(r"(\d+)([a-z]?)", r["sid"])
        return (int(m.group(1)) if m else 999, m.group(2) if m else "")

    rows.sort(key=sk)

    SCAN_OUT_PATH.write_text(
        json.dumps({"sessions": rows}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    # Console summary
    print(f"Scanned {len(rows)} sessions; wrote {SCAN_OUT_PATH}")
    print()
    print(f"{'sid':>4}  {'loc':4}  {'files':>5}  {'bytes':>8}  "
          f"{'collab':>6}  {'syn':>4}  {'work':>4}  {'wp':>4}  "
          f"{'hdrAth':>6}  {'wsRnd':>5}  {'prov':>4}  {'topAgent':>15}")
    print("-" * 100)
    for r in rows:
        ar = r["archetype_counts"]
        at = r["attribution_counts"]
        ta = r["top_agents_in_content"]
        top_agent = next(iter(ta), "-")[:14] if ta else "-"
        print(f"{r['sid']:>4}  {r['location']:4}  "
              f"{r['file_count']:>5}  {r['total_bytes']:>8,}  "
              f"{ar.get('collab',0):>6}  {ar.get('synthesis',0):>4}  "
              f"{ar.get('workshop',0):>4}  {ar.get('workingpaper',0):>4}  "
              f"{at.get('hdr-author-colon',0):>6}  "
              f"{at.get('workshop-round',0):>5}  "
              f"{at.get('provenance-block',0):>4}  "
              f"{top_agent:>15}")


# ===========================================================================
# DRY-RUN - lifted from _format_generation_dry_run.py (main -> run_dry_run)
# ===========================================================================

DRYRUN_OUT_JSON = ROOT / "tools" / "_format_generation_dry_run.json"
DRYRUN_OUT_MD = ROOT / "tools" / "_format_generation_dry_run.md"

# Generation routing — boundaries from Task #3 evidence
def session_to_generation(sid: str) -> str:
    m = re.match(r"(\d+)", sid)
    if not m:
        return "?"
    n = int(m.group(1))
    if n <= 15: return "G1"
    if n <= 18: return "G2"
    if n <= 35: return "G3"
    if n <= 60: return "G4"
    if n <= 77: return "G5"
    if n <= 81: return "G6"
    return "G7"


def extract_g1(session_id: str, all_text: str) -> list[AttributionEdge]:
    """G1 fallback: body-text mention frequency. Emits one
    `discussed_in: session → agent` edge per agent with ≥10 mentions
    OR top-3 by mention count, whichever is larger."""
    counter: Counter = Counter()
    for m in G1_AGENT_RE.finditer(all_text):
        raw = m.group(1)
        cid = canonicalize_agent(raw)
        if cid:
            counter[cid] += 1
    out: list[AttributionEdge] = []
    if not counter:
        return out
    # Top 3 or any with ≥10 mentions
    top3 = set(c for c, _ in counter.most_common(3))
    eligible = set(c for c, n in counter.items() if n >= 10)
    keep = top3 | eligible
    for agent, mentions in counter.most_common():
        if agent not in keep:
            continue
        out.append(AttributionEdge(
            edge_type="discussed_in",
            source_type="researchers",
            source_id=agent,
            target_type="sessions",
            target_id=session_id,
            role=None,
            confidence="session-level-inference",
            generation="G1",
            match_text=f"mentions={mentions}",
        ))
    return out


def find_session_dirs() -> list[tuple[str, Path, str]]:
    """Return (session_id, dir_path, location) for every session."""
    out: list[tuple[str, Path, str]] = []
    for top in [ROOT / "sessions", ROOT / "sessions" / "archive"]:
        if not top.exists():
            continue
        for d in sorted(top.glob("session-*")):
            if not d.is_dir():
                continue
            m = re.match(r"session-(\d+[a-z]?)", d.name)
            if not m:
                continue
            sid = m.group(1)
            loc = "archive" if "archive" in str(d) else "live"
            out.append((sid, d, loc))

    def sk(rec):
        m = re.match(r"(\d+)([a-z]?)", rec[0])
        return (int(m.group(1)) if m else 999, m.group(2) if m else "")
    out.sort(key=sk)
    return out


def process_session(sid: str, sess_dir: Path) -> dict:
    """Apply generation-appropriate extractors to a session directory."""
    gen = session_to_generation(sid)
    edges: list[AttributionEdge] = []
    md_files = sorted([p for p in sess_dir.glob("*.md") if p.is_file()])
    # Include workshops/ subdirectory for G7
    workshop_files = sorted([p for p in (sess_dir / "workshops").glob("*.md")
                             if p.is_file()]) if (sess_dir / "workshops").exists() else []

    if gen == "G1":
        # Concatenate all session text and run mention frequency
        all_text = "\n".join(p.read_text(encoding="utf-8", errors="ignore") for p in md_files)
        edges.extend(extract_g1(sid, all_text))

    elif gen == "G2":
        # Authors-block extraction on the master final file
        for p in md_files:
            text = p.read_text(encoding="utf-8", errors="ignore")
            edges.extend(extract_g2(text, session_id=sid))

    elif gen in ("G3", "G4", "G5"):
        # Per-file `**Author**:` / `**Evaluator**:` / `**Reviewer**:`
        # header + G5 per-gate parenthetical-in-heading + G7 `**Agent**:`
        # fallback + workshop extractor (S61+ wave-WPs have agent-pair in
        # H1 title parenthetical; older G3/G4 multi-agent workshop files
        # use `**Agents**:` body header).
        for p in md_files:
            text = p.read_text(encoding="utf-8", errors="ignore")
            file_id = f"{sid}:{p.name}"
            edges.extend(extract_g3(text, file_id=file_id, filename=p.name))
            edges.extend(extract_g5_per_gate(text, file_id=file_id))
            edges.extend(extract_g7(text, file_id=file_id))
            edges.extend(extract_workshop_g7(text, workshop_id=file_id))

    elif gen == "G6":
        # Owner-per-gate on the WP
        for p in md_files:
            text = p.read_text(encoding="utf-8", errors="ignore")
            edges.extend(extract_g6(text, file_id=f"{sid}:{p.name}"))
        # G6 also benefits from G3 author-header on the WP
        for p in md_files:
            text = p.read_text(encoding="utf-8", errors="ignore")
            edges.extend(extract_g3(text, file_id=f"{sid}:{p.name}", filename=p.name))

    elif gen == "G7":
        # Per-wave WP + per-author synthesis + workshops/
        for p in md_files:
            text = p.read_text(encoding="utf-8", errors="ignore")
            file_id = f"{sid}:{p.name}"
            edges.extend(extract_g7(text, file_id=file_id))
            # Per-author synthesis files: filename-derived author + G3 header
            edges.extend(extract_g3(text, file_id=file_id, filename=p.name))
            # Also try G6 Owner pattern (some S82+ WPs still use it)
            edges.extend(extract_g6(text, file_id=file_id))
            # And workshop extractor on top-level files too (per-wave WPs
            # with **Agents**: bullet-list pattern, or H1 title parenthetical)
            edges.extend(extract_workshop_g7(text, workshop_id=file_id))
        # Workshops subdirectory
        for p in workshop_files:
            text = p.read_text(encoding="utf-8", errors="ignore")
            workshop_id = f"{sid}:workshops/{p.stem}"
            edges.extend(extract_workshop_g7(text, workshop_id=workshop_id))

    # Per-session aggregation
    edge_type_counts: Counter = Counter()
    role_counts: Counter = Counter()
    agent_counts: Counter = Counter()
    for e in edges:
        edge_type_counts[e.edge_type] += 1
        if e.role:
            role_counts[e.role] += 1
        agent = e.source_id if e.source_type == "researchers" else (
            e.target_id if e.target_type == "researchers" else None
        )
        if agent:
            agent_counts[agent] += 1

    return {
        "sid": sid,
        "generation": gen,
        "file_count": len(md_files),
        "workshop_count": len(workshop_files),
        "total_edges": len(edges),
        "edge_type_counts": dict(edge_type_counts),
        "role_counts": dict(role_counts),
        "agent_counts": dict(agent_counts.most_common(10)),
    }


def run_dry_run() -> None:
    sessions = find_session_dirs()
    rows: list[dict] = []
    for sid, sess_dir, loc in sessions:
        rec = process_session(sid, sess_dir)
        rec["location"] = loc
        rows.append(rec)

    # Per-generation aggregation
    per_gen_edge_types: dict[str, Counter] = defaultdict(Counter)
    per_gen_roles: dict[str, Counter] = defaultdict(Counter)
    per_gen_agents: dict[str, Counter] = defaultdict(Counter)
    per_gen_sessions: dict[str, list[str]] = defaultdict(list)
    per_gen_total: dict[str, int] = defaultdict(int)
    grand_total = 0
    for r in rows:
        g = r["generation"]
        per_gen_sessions[g].append(r["sid"])
        per_gen_total[g] += r["total_edges"]
        grand_total += r["total_edges"]
        for et, n in r["edge_type_counts"].items():
            per_gen_edge_types[g][et] += n
        for role, n in r["role_counts"].items():
            per_gen_roles[g][role] += n
        for ag, n in r["agent_counts"].items():
            per_gen_agents[g][ag] += n

    # Write JSON
    payload = {
        "summary": {
            "total_sessions": len(rows),
            "grand_total_edges": grand_total,
            "per_generation_total": dict(per_gen_total),
            "per_generation_edge_types": {g: dict(c) for g, c in per_gen_edge_types.items()},
            "per_generation_roles": {g: dict(c) for g, c in per_gen_roles.items()},
        },
        "per_generation_agents_top10": {
            g: dict(c.most_common(10)) for g, c in per_gen_agents.items()
        },
        "sessions": rows,
    }
    DRYRUN_OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2),
                        encoding="utf-8")

    # Console summary
    print(f"\n=== Dry-Run Summary ({len(rows)} sessions, {grand_total:,} edges total) ===\n")
    print(f"{'Gen':4} {'Sessions':>10} {'Edges':>8} {'Edges/sess':>11}  Top edge types")
    print("-" * 90)
    for g in ["G1", "G2", "G3", "G4", "G5", "G6", "G7"]:
        n_sess = len(per_gen_sessions[g])
        n_edges = per_gen_total[g]
        avg = (n_edges / n_sess) if n_sess else 0.0
        top = ", ".join(f"{t}={n}" for t, n in per_gen_edge_types[g].most_common(4))
        print(f"{g:4} {n_sess:>10} {n_edges:>8} {avg:>11.1f}  {top}")

    print("\n=== Per-generation role distribution ===\n")
    for g in ["G1", "G2", "G3", "G4", "G5", "G6", "G7"]:
        roles = per_gen_roles[g]
        if not roles:
            continue
        line = ", ".join(f"{r}={n}" for r, n in roles.most_common())
        print(f"  {g}: {line}")

    print("\n=== Per-generation top agents ===\n")
    for g in ["G1", "G2", "G3", "G4", "G5", "G6", "G7"]:
        ag = per_gen_agents[g]
        if not ag:
            continue
        line = ", ".join(f"{a}={n}" for a, n in ag.most_common(6))
        print(f"  {g}: {line}")

    print(f"\nWrote {DRYRUN_OUT_JSON} ({DRYRUN_OUT_JSON.stat().st_size:,}B)")

    # Write markdown summary
    md_lines: list[str] = ["# Format-generation dry-run summary", "",
                            f"Total sessions: {len(rows)}",
                            f"Grand-total edges: {grand_total:,}",
                            "",
                            "## Per-generation edge counts",
                            "",
                            "| Gen | Sessions | Edges | Edges/sess | Top edge types |",
                            "|:----|---------:|------:|-----------:|:----------------|"]
    for g in ["G1", "G2", "G3", "G4", "G5", "G6", "G7"]:
        n_sess = len(per_gen_sessions[g])
        n_edges = per_gen_total[g]
        avg = (n_edges / n_sess) if n_sess else 0.0
        top = ", ".join(f"`{t}={n}`" for t, n in per_gen_edge_types[g].most_common(4))
        md_lines.append(f"| {g} | {n_sess} | {n_edges:,} | {avg:.1f} | {top} |")
    md_lines.append("")
    md_lines.append("## Top agents per generation")
    md_lines.append("")
    for g in ["G1", "G2", "G3", "G4", "G5", "G6", "G7"]:
        ag = per_gen_agents[g]
        if not ag:
            continue
        line = ", ".join(f"`{a}` ({n})" for a, n in ag.most_common(6))
        md_lines.append(f"- **{g}**: {line}")
    md_lines.append("")
    DRYRUN_OUT_MD.write_text("\n".join(md_lines), encoding="utf-8")
    print(f"Wrote {DRYRUN_OUT_MD} ({DRYRUN_OUT_MD.stat().st_size:,}B)")


# ===========================================================================
# ZERO-COVERAGE - lifted from _format_generation_zero_coverage.py (main -> run_zero_coverage)
# ===========================================================================

ZEROCOV_OUT_JSON = ROOT / "tools" / "_format_generation_zero_coverage.json"
ZEROCOV_OUT_MD = ROOT / "tools" / "_format_generation_zero_coverage.md"

# Heuristics for categorization
SYSTEM_FILE_PATTERNS = [
    re.compile(r"^evoi-framework\.md$"),
    re.compile(r"^compute-carryforward\.md$"),
    re.compile(r"^results-index\.md$"),
    re.compile(r"session-[\d]+[a-z]?-results-index\.md$"),
    re.compile(r"session-[\d]+[a-z]?-plan-w[\d]+[a-z]?\.md$"),
    re.compile(r"session-[\d]+[a-z]?-workshop-schedule(-w[\d]+)?\.md$"),
    re.compile(r"^_seed-"),
    re.compile(r"session-[\d]+[a-z]?-pending-edits-ledger\.md$"),
    re.compile(r"^s\d+-pending-edits-ledger\.md$"),
    re.compile(r"path-[abcdef]-carry-forward\.md$"),
    re.compile(r"session-[\d]+[a-z]?-OOM\.md$"),
    re.compile(r"^c1_(?:exflation|GR)_proposal\.md$"),
]


def is_system_file(name: str) -> bool:
    return any(p.search(name) for p in SYSTEM_FILE_PATTERNS)


def is_shell_file(text: str) -> bool:
    """Detect SHELL CREATED markers in plan-style WPs (S87+ pattern)."""
    head = text[:1500]
    if re.search(r"\bSHELL\s+CREATED\b", head, re.IGNORECASE):
        return True
    if re.search(r"\*\*Status\*\*:\s*SHELL", head, re.IGNORECASE):
        return True
    if re.search(r"awaiting\s+runtime\s+compute\s+dispatch", head, re.IGNORECASE):
        return True
    return False


# Workshop-filename pair extractor — runs against filename when body has
# no **Agents**: line. Pattern: session-N-{a}-{b}-workshop.md or
# session-N-{a}-{b}-{topic}-workshop.md. The {a}/{b} are agent-name tokens.
WORKSHOP_FILENAME_PAIR_RE = re.compile(
    r"^session-\d+[a-z]?-"
    r"(?P<a>[a-z][\w-]*?)"
    r"-(?P<b>[a-z][\w-]*?)"
    r"(?:-[a-z][\w-]*)?"          # optional topic mid-fix
    r"-workshop(?:s)?\.md$",
    re.IGNORECASE,
)


def is_data_only(text: str) -> bool:
    """Heuristic: file is data-only if (a) <2KB OR (b) ratio of pipe-table
    characters to total chars > 0.1, suggesting dominant-table content."""
    if len(text) < 2000:
        return True
    pipe = text.count("|")
    if pipe / max(len(text), 1) > 0.10:
        return True
    return False


def detect_first_header(text: str) -> str:
    """Return the first H1/H2 heading found (for context)."""
    m = re.search(r"^#{1,2}\s+(.+?)$", text, re.MULTILINE)
    return m.group(1).strip()[:120] if m else ""


def run_extractors_on_file(text: str, gen: str, file_id: str,
                            filename: str) -> int:
    """Run generation-appropriate extractors on ONE file's text and return
    the count of attribution edges emitted. Any file with -workshop in name
    additionally runs the workshop extractor (body **Agents**: line +
    `## Round N — agent:` headings) and the filename-pair fallback."""
    edges = []
    if gen == "G2":
        edges += extract_g2(text, session_id="(file-scoped)")
    if gen in ("G3", "G4", "G5"):
        edges += extract_g3(text, file_id=file_id, filename=filename)
        edges += extract_g5_per_gate(text, file_id=file_id)
        # G7 `**Agent**:` pattern fires universally — appears in S25+ files
        # even though it dominates in S82+. Run it as a fallback.
        edges += extract_g7(text, file_id=file_id)
    if gen == "G6":
        edges += extract_g6(text, file_id=file_id)
        edges += extract_g3(text, file_id=file_id, filename=filename)
    if gen == "G7":
        edges += extract_g7(text, file_id=file_id)
        edges += extract_g3(text, file_id=file_id, filename=filename)
        edges += extract_g6(text, file_id=file_id)
    # Workshop extractor — runs UNIVERSALLY on every file. The workshop
    # format (**Agents**: + ## Round N + G5 title-parenthetical) is
    # carrier-agnostic: workshop files live in workshops/ subdir for G7,
    # at the session-top-level for G5, and wave-WPs (no -workshop in
    # name) carry agent-pair-in-title for S61.
    edges += extract_workshop_g7(text, workshop_id=file_id)
    # Filename-pair fallback: even if body parse fires nothing, the
    # filename pattern session-N-{a}-{b}-workshop.md attributes BOTH
    # agents as participants.
    if not edges:
        fm = WORKSHOP_FILENAME_PAIR_RE.match(filename)
        if fm:
            for raw in (fm.group("a"), fm.group("b")):
                if canonicalize_agent(raw):
                    edges.append("filename-pair")  # sentinel
    return len(edges)


def run_zero_coverage() -> None:
    zero_files: list[dict] = []
    total_files = 0
    per_category: Counter = Counter()

    # Walk all sessions
    session_dirs: list[tuple[str, Path, str]] = []
    for top in [ROOT / "sessions", ROOT / "sessions" / "archive"]:
        if not top.exists():
            continue
        for d in sorted(top.glob("session-*")):
            if not d.is_dir():
                continue
            m = re.match(r"session-(\d+[a-z]?)", d.name)
            if not m:
                continue
            sid = m.group(1)
            loc = "archive" if "archive" in str(d) else "live"
            session_dirs.append((sid, d, loc))

    def sk(rec):
        m = re.match(r"(\d+)([a-z]?)", rec[0])
        return (int(m.group(1)) if m else 999, m.group(2) if m else "")
    session_dirs.sort(key=sk)

    for sid, sess_dir, loc in session_dirs:
        gen = session_to_generation(sid)
        # Top-level md files
        files = sorted([p for p in sess_dir.glob("*.md") if p.is_file()])
        # workshops/ subdir
        workshop_files = sorted([p for p in (sess_dir / "workshops").glob("*.md")
                                 if p.is_file()]) if (sess_dir / "workshops").exists() else []
        for p in files + workshop_files:
            total_files += 1
            text = p.read_text(encoding="utf-8", errors="ignore")
            file_id = f"S{sid}:{p.relative_to(sess_dir)}"

            # Try generation extractor + try workshop extractor if it's a
            # workshops/ file
            edge_count = run_extractors_on_file(text, gen, file_id, p.name)
            if "workshops" in str(p.relative_to(sess_dir)):
                edge_count += len(extract_workshop_g7(text, workshop_id=file_id))

            # Also try G1 frequency inference for any zero-result file
            # (catches G1 sessions whose extractor wasn't invoked above)
            if edge_count == 0 and gen == "G1":
                # G1 emits at session-level, not file-level — skip categorization
                # of individual G1 files unless they're suspiciously empty
                pass

            if edge_count > 0:
                continue

            # Zero-coverage — categorize
            if is_system_file(p.name):
                cat = "SYSTEM-FILE"
            elif is_shell_file(text):
                cat = "SHELL"
            elif gen == "G1":
                cat = "PRE-G3-NARRATIVE"
            elif is_data_only(text):
                cat = "DATA-ONLY"
            else:
                cat = "FORMAT-MISS"

            per_category[cat] += 1
            zero_files.append({
                "sid": sid,
                "location": loc,
                "generation": gen,
                "path": str(p.relative_to(ROOT)).replace("\\", "/"),
                "size": p.stat().st_size,
                "category": cat,
                "first_header": detect_first_header(text),
                "head_preview": re.sub(r"\s+", " ", text[:240]).strip(),
            })

    # Write JSON
    payload = {
        "summary": {
            "total_files_scanned": total_files,
            "zero_coverage_total": len(zero_files),
            "by_category": dict(per_category),
        },
        "zero_files": zero_files,
    }
    ZEROCOV_OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2),
                        encoding="utf-8")

    # Console summary
    print(f"Scanned {total_files} files across 90 sessions")
    print(f"Zero-coverage: {len(zero_files)} files ({100*len(zero_files)/total_files:.1f}%)\n")
    print("By category:")
    for cat in ("FORMAT-MISS", "DATA-ONLY", "SYSTEM-FILE", "PRE-G3-NARRATIVE"):
        print(f"  {cat:<22} {per_category[cat]:>5}")

    # Markdown report — surface FORMAT-MISS first (highest signal)
    md = ["# Zero-coverage report (Phase 0.9)",
          "",
          f"Scanned **{total_files}** session .md files. **{len(zero_files)}** "
          f"emit zero attribution edges ({100*len(zero_files)/total_files:.1f}%).",
          "",
          "## Distribution by category",
          "",
          "| Category | Count | Meaning |",
          "|:---------|------:|:--------|",
          f"| FORMAT-MISS | {per_category['FORMAT-MISS']} | File SHOULD have attribution but no regex fires. Regex-refinement OR orphan-content candidate. |",
          f"| SHELL | {per_category.get('SHELL', 0)} | File is a pre-allocated empty shell (e.g., S91 W4 `awaiting runtime compute dispatch`). Attribution will land when compute runs. |",
          f"| DATA-ONLY | {per_category['DATA-ONLY']} | File is mostly tables / short stub / data-listing. No attribution by design. |",
          f"| SYSTEM-FILE | {per_category['SYSTEM-FILE']} | Project-scaffolding (plans, schedules, indexes, ledgers, seeds). Attribution is project-level, not file-level. |",
          f"| PRE-G3-NARRATIVE | {per_category['PRE-G3-NARRATIVE']} | G1 session file. Pre-formal-attribution era; expected. |",
          "",
          "## FORMAT-MISS sub-classification",
          "",
          "The FORMAT-MISS pool splits into TWO distinct sub-classes:",
          "",
          "**(A) Master-aggregator pattern (design-correct)** — Files where authorship is offloaded to sister files. The aggregator (`session-N-results-workingpaper.md`, `session-N-master-collab.md`, `session-N-master-synthesis.md`) is orchestrator-aggregated; the per-author content lives in `session-N-{agent}-{topic}.md` siblings. The session as a whole IS attributed; only the roll-up file individually has no per-file author marker.",
          "",
          "**(B) Orphan-content candidates (the 'lost ideas' pool)** — Files matching no recognized archetype. These are peculiar one-offs: cross-session reviews, special audits, way-forward planning docs, named meta-documents. Worth manual inspection.",
          ""]
    # Compute sub-classification
    aggregator_archetypes = ("master-collab", "master-synthesis", "results-workingpaper", "wave")
    fm_aggregator = [f for f in zero_files
                     if f["category"] == "FORMAT-MISS" and
                     any(a in f["path"].split("/")[-1] for a in aggregator_archetypes)]
    fm_orphan = [f for f in zero_files
                 if f["category"] == "FORMAT-MISS" and f not in fm_aggregator]
    md.append(f"- **(A) Master-aggregator pattern**: {len(fm_aggregator)} files")
    md.append(f"- **(B) Orphan-content candidates**: {len(fm_orphan)} files")
    md.append("")

    # FORMAT-MISS orphan candidates (B) — the HIGH-SIGNAL section
    fm_orphan.sort(key=lambda r: (-r["size"], r["sid"]))
    md.append(f"## (B) Orphan-content candidates ({len(fm_orphan)} files) — the 'lost ideas' surface")
    md.append("")
    md.append("These are FORMAT-MISS files that DON'T match any standard aggregator archetype. Sorted by size (largest first). Each is a candidate for one of: (i) genuine orphan content worth re-surfacing, (ii) a one-off format the regex doesn't catch yet, (iii) an unusual review/audit pattern.")
    md.append("")
    md.append("| Gen | Session | File | Size | First header | Head preview |")
    md.append("|:---|:--------|:-----|-----:|:-------------|:-------------|")
    for f in fm_orphan[:150]:
        hd = f["first_header"].replace("|", "\\|")
        pv = f["head_preview"][:120].replace("|", "\\|")
        path_short = f["path"].split("/", 2)[-1]
        md.append(f"| {f['generation']} | S{f['sid']} | `{path_short}` | "
                  f"{f['size']:,} | {hd} | {pv} |")
    if len(fm_orphan) > 150:
        md.append(f"\n…and {len(fm_orphan)-150} more orphan entries in the JSON.")
    md.append("")

    # FORMAT-MISS master-aggregator (A) — design-correct, lower priority
    fm_aggregator.sort(key=lambda r: (-r["size"], r["sid"]))
    md.append(f"## (A) Master-aggregator pattern ({len(fm_aggregator)} files) — design-correct")
    md.append("")
    md.append("These are aggregator files whose authorship is offloaded to sister files. The session as a whole is attributed; only the roll-up file individually has no per-file author marker. Phase 1 harvester could optionally attribute the aggregator to `orchestrator` as the synthesizer.")
    md.append("")
    md.append("| Gen | Session | File | Size | First header |")
    md.append("|:---|:--------|:-----|-----:|:-------------|")
    for f in fm_aggregator[:60]:
        hd = f["first_header"].replace("|", "\\|")
        path_short = f["path"].split("/", 2)[-1]
        md.append(f"| {f['generation']} | S{f['sid']} | `{path_short}` | "
                  f"{f['size']:,} | {hd} |")
    if len(fm_aggregator) > 60:
        md.append(f"\n…and {len(fm_aggregator)-60} more aggregator entries in the JSON.")
    md.append("")

    # SYSTEM-FILE listing (collapsed; just enumerate)
    sf = [f for f in zero_files if f["category"] == "SYSTEM-FILE"]
    md.append(f"## SYSTEM-FILE ({len(sf)} files) — expected zero attribution")
    md.append("")
    by_kind: dict[str, list[dict]] = defaultdict(list)
    for f in sf:
        # Group by archetype keyword
        n = f["path"].split("/")[-1]
        if "plan" in n: kind = "plan-block"
        elif "schedule" in n: kind = "workshop-schedule"
        elif "_seed" in n: kind = "workshop-seed"
        elif "pending-edits" in n: kind = "pending-edits-ledger"
        elif "results-index" in n: kind = "results-index"
        elif "carry-forward" in n: kind = "carry-forward"
        elif "OOM" in n: kind = "OOM-summary"
        elif "evoi" in n: kind = "evoi-framework"
        elif "compute-carryforward" in n: kind = "compute-carryforward"
        else: kind = "other-system"
        by_kind[kind].append(f)
    md.append("| Kind | Count | Examples |")
    md.append("|:-----|------:|:---------|")
    for k, lst in sorted(by_kind.items(), key=lambda x: -len(x[1])):
        ex = ", ".join(f["path"].split("/")[-1] for f in lst[:2])
        md.append(f"| {k} | {len(lst)} | {ex} |")
    md.append("")

    # DATA-ONLY listing
    do = [f for f in zero_files if f["category"] == "DATA-ONLY"]
    md.append(f"## DATA-ONLY ({len(do)} files) — short / table-heavy / data stubs")
    md.append("")
    md.append("These are largely tables or short stubs. Listed for completeness.")
    md.append("")
    md.append("| Session | File | Size |")
    md.append("|:--------|:-----|-----:|")
    for f in do[:40]:
        path_short = f["path"].split("/", 2)[-1]
        md.append(f"| S{f['sid']} | `{path_short}` | {f['size']:,} |")
    if len(do) > 40:
        md.append(f"\n…and {len(do)-40} more in JSON.")
    md.append("")

    ZEROCOV_OUT_MD.write_text("\n".join(md), encoding="utf-8")
    print(f"\nWrote {ZEROCOV_OUT_JSON} ({ZEROCOV_OUT_JSON.stat().st_size:,}B)")
    print(f"Wrote {ZEROCOV_OUT_MD} ({ZEROCOV_OUT_MD.stat().st_size:,}B)")


# ---------------------------------------------------------------------------
# CLI dispatcher
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        prog="format_generations.py",
        description="Format-generation pipeline (scan / dry-run / zero-coverage / self-test).",
    )
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("scan", help="Phase 0: fingerprint sessions for archetypes.")
    sub.add_parser("dry-run", help="Phase 0.5: aggregate per-generation edge counts.")
    sub.add_parser("zero-coverage", help="Phase 0.9: surface files with zero attribution edges.")
    sub.add_parser("self-test", help="Verify the G1-G7 regex set against frozen fixtures.")
    args = parser.parse_args()
    if args.cmd == "scan":
        run_scan()
    elif args.cmd == "dry-run":
        run_dry_run()
    elif args.cmd == "zero-coverage":
        run_zero_coverage()
    elif args.cmd == "self-test":
        sys.exit(run_self_test())


if __name__ == "__main__":
    main()
