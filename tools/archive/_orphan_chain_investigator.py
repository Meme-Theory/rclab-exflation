#!/usr/bin/env python3
"""Investigate the 156 FORMAT-MISS orphan files surfaced by Phase 0.9 +
emit per-file linked-chain analysis.

For each orphan:
  1. Read head + tail of the file (head 80 lines; tail 15 lines)
  2. Apply EXTENDED attribution regex set (forms the Phase 1 harvester
     misses by design — these are the patterns we're surfacing)
  3. Classify by archetype based on filename + content
  4. Extract upstream chain (Source / Reviewing / Predecessor / Input)
  5. Extract downstream chain (scan corpus for backreferences)
  6. Emit recommended edges per the Phase 1 edge-type vocabulary

The output augments orphan-content-watchlist.md with chain-of-custody
columns AND produces a separate analysis-detail file at
sessions/framework/registry/orphan-chain-analysis.md.

NOT a harvester replacement — this is investigation tooling that
inventories what edges SHOULD exist. Promoting the patterns into the
production harvester is Phase 1.1 work, queued separately.
"""
from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, NamedTuple

ROOT = Path(__file__).resolve().parent.parent
JSON_SRC = ROOT / "tools" / "_format_generation_zero_coverage.json"
OUT_ANALYSIS = ROOT / "sessions" / "framework" / "registry" / "orphan-chain-analysis.md"
OUT_JSON = ROOT / "tools" / "_orphan_chain_analysis.json"
OUT_WATCHLIST = ROOT / "sessions" / "framework" / "registry" / "orphan-content-watchlist.md"

# ----------------------------------------------------------------------
# AGENT alias map — synced manually with
# tools/_format_generation_regex_set.py::AGENT_ALIASES + extended with
# additional informal forms that show up in orphan files.
# ----------------------------------------------------------------------

AGENT_ALIASES: dict[str, str] = {
    # canonical
    "baptista": "baptista-spacetime-analyst",
    "baptista-spacetime-analyst": "baptista-spacetime-analyst",
    "tesla": "tesla-resonance",
    "tesla-resonance": "tesla-resonance",
    "qa": "quantum-acoustics-theorist",
    "quantum-acoustics-theorist": "quantum-acoustics-theorist",
    "qa-theorist": "quantum-acoustics-theorist",
    "kk": "kaluza-klein-theorist",
    "kaluza-klein-theorist": "kaluza-klein-theorist",
    "kk-theorist": "kaluza-klein-theorist",
    "gen-physicist": "gen-physicist",
    "sim": "phonon-first-cosmologist",
    "sim-specialist": "gen-physicist",  # canonical per harvester L55 (S16-era catch-all)
    "phonon-exflation-sim": "phonon-first-cosmologist",
    "phonon-first": "phonon-first-cosmologist",
    "phonon-first-cosmologist": "phonon-first-cosmologist",
    "paasch": "paasch-mass-quantization-analyst",
    "paasch-mass-quantization-analyst": "paasch-mass-quantization-analyst",
    "paasch-analyst": "paasch-mass-quantization-analyst",
    "feynman": "feynman-theorist",
    "feynman-theorist": "feynman-theorist",
    "hawking": "hawking-theorist",
    "hawking-theorist": "hawking-theorist",
    "einstein": "einstein-theorist",
    "einstein-theorist": "einstein-theorist",
    "sp": "schwarzschild-penrose-geometer",
    "schwarzschild-penrose": "schwarzschild-penrose-geometer",
    "schwarzschild-penrose-geometer": "schwarzschild-penrose-geometer",
    "sagan": "sagan-empiricist",
    "sagan-empiricist": "sagan-empiricist",
    "dirac": "dirac-antimatter-theorist",
    "dirac-antimatter-theorist": "dirac-antimatter-theorist",
    "antimatter": "dirac-antimatter-theorist",
    "neutrino": "neutrino-detection-specialist",
    "neutrino-detection-specialist": "neutrino-detection-specialist",
    "connes": "connes-ncg-theorist",
    "connes-ncg-theorist": "connes-ncg-theorist",
    "berry": "berry-geometric-phase-theorist",
    "berry-geometric-phase-theorist": "berry-geometric-phase-theorist",
    "landau": "landau-condensed-matter-theorist",
    "landau-condensed-matter-theorist": "landau-condensed-matter-theorist",
    "nazarewicz": "nazarewicz-nuclear-structure-theorist",
    "nazarewicz-nuclear-structure-theorist": "nazarewicz-nuclear-structure-theorist",
    "cosmic-web": "cosmic-web-theorist",
    "cosmic-web-theorist": "cosmic-web-theorist",
    "lrd": "little-red-dots-jwst-analyst",
    "little-red-dots": "little-red-dots-jwst-analyst",
    "little-red-dots-jwst-analyst": "little-red-dots-jwst-analyst",
    "mack": "mack-cosmic-bridge",
    "mack-cosmic-bridge": "mack-cosmic-bridge",
    "katie mack": "mack-cosmic-bridge",
    "katie-mack": "mack-cosmic-bridge",
    "volovik": "volovik-superfluid-universe-theorist",
    "volovik-superfluid-universe-theorist": "volovik-superfluid-universe-theorist",
    "lizzi": "lizzi-spectral-functional-theorist",
    "lizzi-spectral-functional-theorist": "lizzi-spectral-functional-theorist",
    "string": "string-theory-theorist",
    "string-theory-theorist": "string-theory-theorist",
    "kaku": "kaku-speculative-theorist",
    "kaku-speculative-theorist": "kaku-speculative-theorist",
    "kitaev": "kitaev-quantum-chaos-theorist",
    "kitaev-quantum-chaos-theorist": "kitaev-quantum-chaos-theorist",
    "transit-dynamics": "transit-dynamics-theorist",
    "transit-dynamics-theorist": "transit-dynamics-theorist",
    "spectral-geometer": "spectral-geometer",
    "spectral-functional": "lizzi-spectral-functional-theorist",
    "spectral-ops": "lizzi-spectral-functional-theorist",
    "qfoam": "quantum-foam-theorist",
    "quantum-foam": "quantum-foam-theorist",
    "quantum-foam-theorist": "quantum-foam-theorist",
    "van-den-dungen": "van-den-dungen-bridge-theorist",
    "van den dungen": "van-den-dungen-bridge-theorist",
    "vdd": "van-den-dungen-bridge-theorist",
    "van-den-dungen-bridge-theorist": "van-den-dungen-bridge-theorist",
    # additional canonical aliases mirroring harvester (parity at 2026-05-17)
    "naz": "nazarewicz-nuclear-structure-theorist",
    "neutrino-detection": "neutrino-detection-specialist",
    "cosmic-bridge": "mack-cosmic-bridge",
    "sp-geometer": "schwarzschild-penrose-geometer",
    "geometer": "spectral-geometer",
    "connes-ncg": "connes-ncg-theorist",
    "dungen": "van-den-dungen-bridge-theorist",
    "general": "gen-physicist",
    "physicist": "gen-physicist",
    "quantum-acoustics": "quantum-acoustics-theorist",
    "string-theory": "string-theory-theorist",
    "kaluza-klein": "kaluza-klein-theorist",
    "cosmicweb": "cosmic-web-theorist",
    # informal / orphan-only forms
    "claude": "claude",  # user-meta agent identity, project-internal
    "meme": "meme-pi",   # user identity ("Meme (PI)")
    "ainur-panel": "ainur-panel",
    "ainur": "ainur-panel",
    "panel": "ainur-panel",
    "team-lead": "orchestrator",  # canonical per harvester L159
    "orchestrator": "orchestrator",
    "coordinator": "orchestrator",
    "user": "user",
    "pi": "meme-pi",
    "giants": "giants-pair",
    "giants pair": "giants-pair",
    "team a": "team-a",
    "team b": "team-b",
    "team c": "team-c",
    "team d": "team-d",
    "team e": "team-e",
    "sole probability estimator": "sagan-empiricist",
    "sole writer": "orchestrator",
    "fusion team": "fusion-team",
    "lead researcher": "tesla-resonance",  # canonical mapping per S19d
}


def canonicalize_agent(raw: str) -> str | None:
    """Normalize a raw agent token to its canonical form, or None if
    the token is not a recognized agent reference (e.g., it is actually
    a qualifier in a parenthetical).
    """
    if not raw:
        return None
    cleaned = raw.replace("`", "").replace("*", "").strip()
    cleaned = cleaned.strip(".,:;()[]")
    if not cleaned:
        return None
    lower = cleaned.lower()
    # Try direct lookup
    if lower in AGENT_ALIASES:
        return AGENT_ALIASES[lower]
    # Try suffix-stripped (remove -theorist / -analyst / -specialist / -geometer)
    for suffix in ("-theorist", "-analyst", "-specialist", "-geometer",
                   "theorist", "analyst", "specialist", "geometer"):
        if lower.endswith(suffix):
            base = lower[:-len(suffix)].rstrip(" -")
            if base in AGENT_ALIASES:
                return AGENT_ALIASES[base]
    # Reject obvious qualifiers (parentheticals like "geometry/math physics")
    qualifier_words = {"geometry", "physics", "framework", "review", "compute",
                       "pi", "phd", "audit", "synthesis", "computation", "mode",
                       "round", "verify", "ncg", "cpt", "rocm", "writer",
                       "math", "writer", "writer"}
    if any(w in lower for w in qualifier_words):
        return None
    if len(lower) > 60:  # too long to be an agent ID
        return None
    return None


# ----------------------------------------------------------------------
# EXTENDED attribution regex set
# These patterns capture forms the production harvester does NOT yet
# emit edges for. Each pattern includes a role qualifier so the
# investigator can emit role-specific edge recommendations.
# ----------------------------------------------------------------------

# Pattern: ## Author: <name> ...
#          ## Author: <name> + <name>...
RE_H2_AUTHOR = re.compile(
    r"^## Author:?\s*(.+?)$", re.IGNORECASE | re.MULTILINE,
)

# Pattern: ## Date: ... ## Author: ...
# captured by RE_H2_AUTHOR

# Pattern: ## Participants: <name> + <name>
RE_H2_PARTICIPANTS = re.compile(
    r"^## Participants:?\s*(.+?)$", re.IGNORECASE | re.MULTILINE,
)

# Pattern: ## QA-Theorist + Baptista-Analyst (H2 multi-author header)
RE_H2_MULTI_AUTHOR = re.compile(
    r"^## ([A-Z][\w-]+(?:-\w+)?(?:\s*[+]\s*[A-Z][\w-]+(?:-\w+)?)+)\s*$",
    re.MULTILINE,
)

# Pattern: **Team**: <descr>  /  **Agents**: <list>
RE_TEAM = re.compile(
    r"^[-*\s]*\*\*Team\*\*:?\s*(.+?)$", re.IGNORECASE | re.MULTILINE,
)
RE_AGENTS_LIST = re.compile(
    r"^[-*\s]*\*\*Agents?\*\*:?\s*(.+?)$", re.IGNORECASE | re.MULTILINE,
)
RE_PARTICIPANTS = re.compile(
    r"^[-*\s]*\*\*Participants?\*\*:?\s*(.+?)$", re.IGNORECASE | re.MULTILINE,
)

# Pattern: **Author**: / **Author:** / **Auteur:** / **Author/PI:**
RE_AUTHOR_BOLD = re.compile(
    r"^[-*\s]*\*\*Authors?\*\*:?\s*(.+?)$", re.IGNORECASE | re.MULTILINE,
)

# Designated writer (the file's sole-writer attribution)
RE_DESIGNATED_WRITER = re.compile(
    r"^[-*\s]*\*\*Designated Writer\*\*:?\s*(.+?)$", re.IGNORECASE | re.MULTILINE,
)
RE_SOLE_WRITER = re.compile(
    r"^[-*\s]*\*\*Sole [Ww]riter\*\*:?\s*(.+?)$", re.IGNORECASE | re.MULTILINE,
)
RE_WRITER = re.compile(
    r"^[-*\s]*\*\*Writer\*\*:?\s*(.+?)$", re.IGNORECASE | re.MULTILINE,
)

# Synthesizer attribution
RE_SYNTH = re.compile(
    r"^[-*\s]*\*\*Synth(?:esist|esizer|esis Lead)\*\*:?\s*(.+?)$", re.IGNORECASE | re.MULTILINE,
)
RE_SYNTHESIZED_BY = re.compile(
    r"^[-*\s]*\*\*Synthesized [Bb]y\*\*:?\s*(.+?)$", re.IGNORECASE | re.MULTILINE,
)

# Assessor / Auditor / Reviewer
RE_ASSESSOR = re.compile(
    r"^[-*\s]*\*\*Assessor\*\*:?\s*(.+?)$", re.IGNORECASE | re.MULTILINE,
)
RE_AUDITOR = re.compile(
    r"^[-*\s]*\*\*Auditor\*\*:?\s*(.+?)$", re.IGNORECASE | re.MULTILINE,
)
RE_REVIEWER = re.compile(
    r"^[-*\s]*\*\*Reviewer\*\*:?\s*(.+?)$", re.IGNORECASE | re.MULTILINE,
)

# Team-lead / fusion team / lead researcher
RE_LEAD = re.compile(
    r"^[-*\s]*\*\*(?:Team[ -]?[Ll]ead|Lead [Rr]esearcher|Fusion [Tt]eam)\*\*:?\s*(.+?)$",
    re.IGNORECASE | re.MULTILINE,
)

# Agent (singular)
RE_AGENT_SING = re.compile(
    r"^[-*\s]*\*\*Agent\*\*:?\s*(.+?)$", re.IGNORECASE | re.MULTILINE,
)

# Researcher (used in S25 Investigation-* sub-section per-entry)
RE_RESEARCHER = re.compile(
    r"^[-*\s]*\*\*Researcher\*\*:?\s*(.+?)$", re.IGNORECASE | re.MULTILINE,
)

# Section header tag e.g. ## [E]S-1 (E = Einstein, L = Landau, etc.)
RE_TAG_BRACKET = re.compile(
    r"###?\s*\[([A-Za-z]+)\]\s*[A-Z]+-?\d+", re.MULTILINE,
)

# Upstream chain extractors
RE_SOURCE = re.compile(
    r"^[-*\s]*\*\*Sources?\*\*:?\s*(.+?)$", re.IGNORECASE | re.MULTILINE,
)
RE_REVIEWING = re.compile(
    r"^[-*\s]*\*\*Reviewing\*\*:?\s*(.+?)$", re.IGNORECASE | re.MULTILINE,
)
RE_REVIEWED = re.compile(
    r"^[-*\s]*\*\*(?:Session reviewed|Reviewed)\*\*:?\s*(.+?)$", re.IGNORECASE | re.MULTILINE,
)
RE_PREDECESSOR = re.compile(
    r"^[-*\s]*\*\*(?:Predecessor|Prior|Prior session)\*\*:?\s*(.+?)$",
    re.IGNORECASE | re.MULTILINE,
)
RE_EXTRACTED = re.compile(
    r"^[-*\s]*\*\*Extracted [Ff]rom\*\*:?\s*(.+?)$", re.IGNORECASE | re.MULTILINE,
)
RE_SOURCE_FILES = re.compile(
    r"^[-*\s]*\*\*Source files\*\*:?\s*(.+?)$", re.IGNORECASE | re.MULTILINE,
)
RE_REFCORPUS = re.compile(
    r"^[-*\s]*\*\*(?:Reference corpus|Reference|Basis)\*\*:?\s*(.+?)$", re.IGNORECASE | re.MULTILINE,
)
RE_INPUT = re.compile(
    r"^[-*\s]*\*\*Inputs?\*\*:?\s*(.+?)$", re.IGNORECASE | re.MULTILINE,
)

# Markdown link patterns to other session files
RE_MD_LINK = re.compile(r"\[[^\]]*\]\(([^)]+\.(?:md|npz|py|json|txt))\)")
RE_BARE_PATH = re.compile(r"`(sessions/[^\s`]+\.md|computations/[^\s`]+\.(?:py|md|txt|npz)|researchers/[^\s`]+\.md)`")

# Session number references (S{N}, Session N, session-N)
RE_SESSION_REF = re.compile(r"\b(?:S|Session\s+|session-?)(\d{1,2})\b")

# ----------------------------------------------------------------------
# Archetype classification
# ----------------------------------------------------------------------

ARCHETYPE_PATTERNS = [
    # (regex, archetype, recommended primary edge_type, description)
    (re.compile(r"-final\.md$|-handoff\.md$|-wrapup\.md$"), "handoff",
     "summarizes_session", "Session-level handoff or wrap-up document"),
    (re.compile(r"-quicklook\.md$"), "quicklook",
     "summarizes_session", "Quicklook session summary"),
    (re.compile(r"-quicklook-([a-z-]+)-collab\.md$"), "solo_collab_review",
     "reviews", "Solo collaborative review of session quicklook"),
    (re.compile(r"-Investigation-[A-Z][a-z]+(?:-Efforts)?\.md$"), "synergy_index",
     "synthesizes", "Multi-researcher synergy/investigation index"),
    (re.compile(r"-Investigation-Closing\.md$"), "investigation_closing",
     "summarizes_session", "Investigation closing verdict"),
    (re.compile(r"-Investigation-Framework\.md$"), "framework_synergy",
     "synthesizes", "Framework synergy synthesis"),
    (re.compile(r"-wayforward\.md$|-way-forward\.md$"), "wayforward",
     "plans_next_session", "Way-forward computation extraction"),
    (re.compile(r"-team-?[A-Za-z]?-?synthesis(?:-[a-z])?\.md$"), "team_synthesis",
     "synthesizes", "Multi-agent team synthesis"),
    (re.compile(r"-foundation\.md$|-verification\.md$"), "phase_layer",
     "authored_by", "Phase 1/2 layer artifact (S17 era)"),
    (re.compile(r"-spectral-diagnostics\.md$|-casimir-energy\.md$"), "sub_session_compute",
     "authored_by", "Sub-session computation"),
    (re.compile(r"-wrapup-reviewplan\.md$"), "wrapup_reviewplan",
     "plans_session", "Wrapup review plan"),
    (re.compile(r"-w\d+-(?:math-permanence|[A-Za-z-]+)\.md$"), "wave_subdocument",
     "discussed_in", "Wave-prefixed sub-document"),
    (re.compile(r"-Excursion\.md$|-excursion-?[\w-]*\.md$"), "excursion",
     "authored_by", "Session excursion / deep-investigation"),
    (re.compile(r"_audit\.md$|_assessment\.md$"), "single_agent_audit",
     "audits", "Single-agent audit / assessment"),
    (re.compile(r"_tinfoil_|_minus0\d+\.md$"), "tinfoil_investigation",
     "investigates", "Tinfoil-hat investigation"),
    (re.compile(r"-investigation-prompts\.md$|-oz-investigation-"), "investigation_prompts",
     "indexes", "Investigation prompts catalog"),
    (re.compile(r"session-\d+-s\d+-[\w-]+\.md$|session-\d+-s-?\d+-"), "slot_anchored_solo",
     "authored_by", "G7 slot-anchored solo synthesis"),
    (re.compile(r"session-\d+-(?:\d|[a-z])-[\w-]+\.md$"), "slot_anchored_solo",
     "authored_by", "G7 slot-anchored variant"),
    (re.compile(r"-LeadResearcher-Collab"), "lead_researcher_collab",
     "authored_by", "Lead researcher solo collab"),
    (re.compile(r"-fusion-synthesis\.md$"), "fusion_synthesis",
     "synthesizes", "Fusion synthesis across teams"),
    (re.compile(r"-(\w+-)*synthesis\.md$|-master-synthesis\.md$"), "synthesis",
     "synthesizes", "Synthesis document"),
    (re.compile(r"-workshop-synthesis\.md$"), "workshop_synthesis",
     "synthesizes", "Workshop output synthesis"),
    (re.compile(r"^workshops/.*\.md$|/workshops/.*\.md$"), "workshop",
     "discussed_in", "Workshop transcript or output"),
    (re.compile(r"-workshop\.md$"), "workshop",
     "discussed_in", "Workshop transcript"),
    (re.compile(r"-workingpaper\.md$"), "workingpaper",
     "authored_by", "Wave working paper (gate-anchored)"),
    (re.compile(r"-collab\.md$"), "solo_collab_review",
     "reviews", "Solo collaborative review"),
    (re.compile(r"-primer\.md$"), "session_primer",
     "primes_session", "Session primer / opening framing"),
    (re.compile(r"-round-?\d?[a-z]?-"), "round_discussion",
     "discussed_in", "Multi-round discussion transcript"),
    (re.compile(r"-priority-\d+\.md$"), "priority_computation",
     "authored_by", "Numbered priority computation"),
    (re.compile(r"-results\.md$"), "results_summary",
     "summarizes_session", "Session results summary"),
    (re.compile(r"-orchestration-state\.md$"), "orchestration_state",
     "tracks_session", "Orchestration tracking state"),
    (re.compile(r"-scratchpad\.md$"), "scratchpad",
     "scratchpad_for", "Investigation scratchpad"),
    (re.compile(r"-addendum-?.*\.md$"), "addendum",
     "addendum_to", "Session addendum"),
    (re.compile(r"-audit.*\.md$"), "audit",
     "audits", "Audit document"),
    (re.compile(r"-pre-?registration\.md$"), "pre_registration",
     "pre_registers", "Pre-registration document"),
    (re.compile(r"-graceful-handoff\.md$"), "graceful_handoff",
     "continues_session", "Session continuation handoff"),
    (re.compile(r"-pause-resume\.md$"), "pause_resume",
     "continues_session", "Pause/resume artifact"),
    (re.compile(r"-phase-plan\.md$|-plan\.md$|-investigation-schedule\.md$"), "plan",
     "plans_session", "Session phase plan"),
    (re.compile(r"-excursion\.md$"), "excursion",
     "authored_by", "Session excursion / single-agent investigation"),
    (re.compile(r"-midsession-review\.md$"), "midsession_review",
     "reviews_session", "Mid-session review"),
    (re.compile(r"-extraction\b"), "extraction",
     "extracted_from", "Extraction document"),
    (re.compile(r"-narrative\.md$|-directive\.md$"), "pi_directive",
     "directs_session", "PI directive or narrative"),
    (re.compile(r"-dismissal-?ack\.md$"), "dismissal_acknowledgment",
     "acknowledges", "Agent dismissal acknowledgment"),
    (re.compile(r"-settings-?diff\.md$"), "settings_diff",
     "configures", "Settings.json wiring diff"),
    (re.compile(r"-pre-registration\.md$"), "pre_registration",
     "pre_registers", "Pre-registration document"),
    (re.compile(r"_addendum.*\.md$"), "addendum",
     "addendum_to", "Session addendum"),
    (re.compile(r"-tinfoil-"), "tinfoil_investigation",
     "investigates", "Tinfoil-hat investigation"),
    (re.compile(r"-rf-analysis\.md$|-dossier\.md$"), "retrospective_analysis",
     "analyzes", "Retrospective analysis dossier"),
    (re.compile(r"-r2-r2\.md$"), "round_2_continuation",
     "discussed_in", "Round 2 continuation"),
    (re.compile(r"-combined-handout\.md$"), "combined_handout",
     "synthesizes", "Combined handout (multi-format synthesis)"),
    (re.compile(r"-(\w+)-eval-?(?:ii)?\.md$|-evaluation\.md$"), "evaluation",
     "evaluates", "Evaluation document"),
    (re.compile(r"-([\w-]+)-review\.md$"), "review",
     "reviews", "Review document"),
    (re.compile(r"-pi-([\w-]+)\.md$"), "pi_artifact",
     "directs_session", "PI artifact"),
    (re.compile(r"-workshop-teams\.md$"), "workshop_teams",
     "organizes_workshops", "Workshop team assignment"),
    (re.compile(r"-([\w-]+)-pre-registration\.md$"), "pre_registration",
     "pre_registers", "Pre-registration"),
]


def classify_archetype(path: str) -> tuple[str, str, str]:
    """Classify a file by archetype based on filename pattern.

    Returns (archetype, primary_edge_type, description).
    """
    name = path.split("/")[-1]
    # Order matters: more specific patterns first (in the list above).
    for regex, arch, edge, desc in ARCHETYPE_PATTERNS:
        if regex.search(name) or regex.search(path):
            return arch, edge, desc
    # Default
    return "uncategorized", "authored_by", "Uncategorized file type"


# ----------------------------------------------------------------------
# Attribution extraction
# ----------------------------------------------------------------------


class Author(NamedTuple):
    """A single attribution edge candidate."""
    raw_token: str         # the literal text as it appeared
    canonical: str         # canonical agent ID
    role: str              # primary | participant | designated_writer | reviewer | synthesizer | assessor | auditor | author | researcher | team_member


def _split_author_list(s: str) -> list[str]:
    """Split an attribution string into individual author tokens.

    Handles: ',', '+', 'and', '&', em-dashes, parenthetical qualifiers.
    """
    # Strip parenthetical qualifiers
    s_clean = re.sub(r"\([^)]*\)", "", s)
    # Strip backticks
    s_clean = s_clean.replace("`", "")
    # Split on common separators
    parts: list[str] = []
    tokens = re.split(r"[,+&]|\sand\s|\sx\s|\sX\s|\sor\s|/|—|–", s_clean)
    for tok in tokens:
        t = tok.strip()
        if t:
            parts.append(t)
    return parts


def extract_attribution(text: str) -> list[Author]:
    """Extract all attribution candidates from a file's content."""
    authors: list[Author] = []
    seen: set[tuple[str, str]] = set()  # (canonical, role) dedup

    def add(token: str, role: str) -> None:
        canon = canonicalize_agent(token)
        if canon and (canon, role) not in seen:
            authors.append(Author(raw_token=token.strip()[:80], canonical=canon, role=role))
            seen.add((canon, role))

    pattern_pairs = [
        (RE_H2_AUTHOR, "author"),
        (RE_H2_PARTICIPANTS, "participant"),
        (RE_TEAM, "team_member"),
        (RE_AGENTS_LIST, "participant"),
        (RE_PARTICIPANTS, "participant"),
        (RE_AUTHOR_BOLD, "author"),
        (RE_DESIGNATED_WRITER, "designated_writer"),
        (RE_SOLE_WRITER, "sole_writer"),
        (RE_WRITER, "writer"),
        (RE_SYNTH, "synthesizer"),
        (RE_SYNTHESIZED_BY, "synthesizer"),
        (RE_ASSESSOR, "assessor"),
        (RE_AUDITOR, "auditor"),
        (RE_REVIEWER, "reviewer"),
        (RE_LEAD, "lead"),
        (RE_AGENT_SING, "primary"),
        (RE_RESEARCHER, "primary"),
    ]
    for regex, role in pattern_pairs:
        for m in regex.finditer(text):
            line = m.group(1).strip()
            # Multi-author lines: split and try each
            for token in _split_author_list(line):
                add(token, role)
            # Also try the full line as a single token (handles cases
            # where the agent ID is the WHOLE line content)
            add(line, role)

    # H2 multi-author header (## QA-Theorist + Baptista-Analyst + ...)
    for m in RE_H2_MULTI_AUTHOR.finditer(text):
        line = m.group(1).strip()
        for token in _split_author_list(line):
            add(token, "primary")

    # Filename-derived attribution (fallback for S85-era slot-anchored
    # solo synthesis + S43/S44/S46/S52/S56/S60 *-{agent}-collab.md patterns).
    # Only applies if no in-content author was extracted.
    # NOTE: caller passes filename via `_filename_hint` (set globally before
    # extract_attribution is called).
    # We delay filename extraction until we know caller-context; see
    # extract_attribution_with_filename below.

    # Bracket-tag (S25 Investigation pattern: [E]S-1 = Einstein, [L]S-1 = Landau)
    bracket_tags = set()
    for m in RE_TAG_BRACKET.finditer(text):
        bracket_tags.add(m.group(1).lower())
    BRACKET_MAP = {
        "e": "einstein-theorist", "l": "landau-condensed-matter-theorist",
        "k": "kaluza-klein-theorist", "b": "baptista-spacetime-analyst",
        "h": "hawking-theorist", "f": "feynman-theorist",
        "p": "paasch-mass-quantization-analyst",
        "q": "quantum-acoustics-theorist", "qa": "quantum-acoustics-theorist",
        "t": "tesla-resonance", "s": "sagan-empiricist",
        "kk": "kaluza-klein-theorist", "n": "neutrino-detection-specialist",
        "c": "cosmic-web-theorist", "d": "dirac-antimatter-theorist",
        "v": "volovik-superfluid-universe-theorist",
        "g": "gen-physicist", "m": "mack-cosmic-bridge",
    }
    for tag in bracket_tags:
        if tag in BRACKET_MAP:
            canon = BRACKET_MAP[tag]
            if (canon, "researcher_contributor") not in seen:
                authors.append(Author(raw_token=f"[{tag.upper()}]",
                                      canonical=canon,
                                      role="researcher_contributor"))
                seen.add((canon, "researcher_contributor"))

    return authors


def extract_filename_authors(filename: str,
                             existing_canonicals: set[str]) -> list[Author]:
    """Filename-derived attribution fallback.

    For filenames like:
      - session-85-s3-alphas-registry-mack.md → mack-cosmic-bridge
      - session-90-connes-s5-pin-derivative-synthesis.md → connes-ncg-theorist
      - session-44-quicklook-nazarewicz-collab.md → nazarewicz-...

    Tokenize the filename (split on `-` and `_`), check each token
    against AGENT_ALIASES. Emit Author entries for any match not already
    in `existing_canonicals` to avoid double-counting.
    """
    out: list[Author] = []
    base = filename.lower().replace(".md", "").replace(" (raw)", "")
    # Try multi-token forms FIRST: `van-den-dungen`, `cosmic-web`, etc.
    multi_token_hits: set[str] = set()
    for raw_alias in AGENT_ALIASES:
        if "-" in raw_alias and len(raw_alias) > 3 and raw_alias in base:
            canon = AGENT_ALIASES[raw_alias]
            if canon not in existing_canonicals and canon not in multi_token_hits:
                out.append(Author(
                    raw_token=f"filename:{raw_alias}",
                    canonical=canon,
                    role="filename_derived",
                ))
                multi_token_hits.add(canon)
    # Then single-token forms
    tokens = re.split(r"[-_./]", base)
    for tok in tokens:
        tok = tok.strip()
        if not tok or len(tok) < 2:
            continue
        # Skip session-number / wave-number / slot tokens that happen to be
        # 2 chars (e.g., 's5', 'w1') — these would collide with 2-letter
        # canonical aliases like 'qa', 'kk', 'sp' if not filtered.
        if re.match(r"^[sw]\d+$", tok) or re.match(r"^\d+[a-z]?$", tok):
            continue
        if tok in AGENT_ALIASES:
            canon = AGENT_ALIASES[tok]
            if canon not in existing_canonicals and canon not in multi_token_hits:
                out.append(Author(
                    raw_token=f"filename:{tok}",
                    canonical=canon,
                    role="filename_derived",
                ))
                multi_token_hits.add(canon)
    return out


# ----------------------------------------------------------------------
# Upstream chain extraction
# ----------------------------------------------------------------------


class UpstreamRef(NamedTuple):
    raw: str
    kind: str        # source | reviewing | predecessor | input | extracted_from | reference
    targets: list[str]  # list of session numbers OR file paths OR researcher names


def _extract_targets(s: str) -> tuple[list[str], list[str], list[str]]:
    """From an upstream-ref string, extract: session numbers, file paths,
    raw researcher names.
    """
    session_refs: list[str] = []
    file_paths: list[str] = []
    raw_names: list[str] = []
    # Session refs
    for m in RE_SESSION_REF.finditer(s):
        n = m.group(1)
        if 1 <= int(n) <= 99 and n not in session_refs:
            session_refs.append(n)
    # File paths
    for m in RE_BARE_PATH.finditer(s):
        file_paths.append(m.group(1))
    for m in RE_MD_LINK.finditer(s):
        file_paths.append(m.group(1))
    # Researcher names (try canonicalize each comma-separated chunk)
    s_clean = re.sub(r"\([^)]*\)", "", s)
    for tok in re.split(r"[,;]|\sand\s|\s+", s_clean):
        canon = canonicalize_agent(tok.strip(".,:;()[]"))
        if canon and canon not in raw_names and not canon.startswith("S"):
            raw_names.append(canon)
    return session_refs, file_paths, raw_names


def extract_upstream(text: str) -> list[UpstreamRef]:
    """Extract upstream chain references."""
    refs: list[UpstreamRef] = []
    pattern_pairs = [
        (RE_SOURCE, "source"),
        (RE_REVIEWING, "reviewing"),
        (RE_REVIEWED, "reviewed"),
        (RE_PREDECESSOR, "predecessor"),
        (RE_EXTRACTED, "extracted_from"),
        (RE_SOURCE_FILES, "source_files"),
        (RE_REFCORPUS, "reference_corpus"),
        (RE_INPUT, "input"),
    ]
    for regex, kind in pattern_pairs:
        for m in regex.finditer(text):
            raw_line = m.group(1).strip()
            sessions, files, names = _extract_targets(raw_line)
            targets = list(sessions) + list(files) + list(names)
            if targets:
                refs.append(UpstreamRef(raw=raw_line[:150], kind=kind, targets=targets))
    return refs


# ----------------------------------------------------------------------
# Downstream chain extraction (corpus-wide backreference scan)
# ----------------------------------------------------------------------


def build_corpus_index() -> dict[str, list[str]]:
    """Build a {basename: [referencing_file_paths]} index by scanning
    all sessions/*.md and researchers/*/*.md for markdown links + bare
    file refs.
    """
    index: dict[str, list[str]] = defaultdict(list)
    scan_dirs = [
        ROOT / "sessions",
        ROOT / "computations",
        ROOT / "tools",
        ROOT / "summary",
    ]
    for d in scan_dirs:
        if not d.exists():
            continue
        for p in d.rglob("*.md"):
            try:
                content = p.read_text(encoding="utf-8", errors="replace")
            except Exception:
                continue
            rel = str(p.relative_to(ROOT)).replace("\\", "/")
            for link_m in RE_MD_LINK.finditer(content):
                target = link_m.group(1).replace("\\", "/")
                basename = target.split("/")[-1]
                if rel not in index[basename]:
                    index[basename].append(rel)
            for bare_m in RE_BARE_PATH.finditer(content):
                target = bare_m.group(1).replace("\\", "/")
                basename = target.split("/")[-1]
                if rel not in index[basename]:
                    index[basename].append(rel)
    return dict(index)


# ----------------------------------------------------------------------
# Edge recommendation
# ----------------------------------------------------------------------


# Canonical edge-type set from tools/extract_entities.py::EDGE_TYPE_CANONICAL
# (snapshot at 2026-05-17; sync if extract_entities.py is updated)
EDGE_TYPE_WHITELIST: frozenset[str] = frozenset({
    # Logical
    "implies", "supersedes", "superseded_by",
    # Closure
    "closed_by", "refutes", "refuted_by", "contradicts",
    # Dependency
    "depends_on", "derived_from", "enables",
    # Validation
    "reproduces", "cross_validates", "confirms", "grounds",
    "feeds_into", "bounds", "refines",
    # Attribution (Phase 1)
    "authored_by", "co_authored_by", "reviewed_by", "participates_in",
    "authored_round", "cites_prior_session", "discussed_in",
    "synthesized_by", "excluded_from", "cited_in",
})

# Aliases per EDGE_TYPE_CANONICAL dict in extract_entities.py
EDGE_TYPE_ALIAS_TO_CANONICAL: dict[str, str] = {
    "closes": "closed_by",
    "depends": "depends_on",
    "derives_from": "derived_from",
    "validates": "confirms",
    "consumes": "feeds_into",
}


def _resolve_edge_type(raw: str) -> tuple[str, bool]:
    """Resolve a raw edge type to canonical + whitelist flag.

    Returns (canonical_or_raw, in_whitelist).
    """
    canonical = EDGE_TYPE_ALIAS_TO_CANONICAL.get(raw, raw)
    return canonical, canonical in EDGE_TYPE_WHITELIST


def recommend_edges(orphan_rec: dict, authors: list[Author],
                    upstream: list[UpstreamRef],
                    downstream: list[str]) -> list[dict]:
    """Emit edge-type recommendations for this orphan.

    Each recommended edge carries `in_whitelist: bool` indicating whether
    its type is currently emittable (in `EDGE_TYPE_CANONICAL`) or requires
    whitelist extension at `tools/extract_entities.py`.
    """
    edges: list[dict] = []
    src_basename = orphan_rec["path"].split("/")[-1]
    sid_raw = orphan_rec.get("sid")
    try:
        sid_int = int(sid_raw) if sid_raw is not None else None
    except (ValueError, TypeError):
        sid_int = None
    src_sess = f"s{sid_int:02d}" if sid_int is not None else "unknown"
    src_sid_str = str(sid_raw) if sid_raw is not None else "unknown"
    arch = orphan_rec["archetype"]

    # Author edges (all attribution edge types are in the Phase 1 whitelist)
    for a in authors:
        role_map = {
            "author": "authored_by",
            "primary": "authored_by",
            "participant": "participates_in",
            "team_member": "participates_in",
            "designated_writer": "synthesized_by",
            "sole_writer": "synthesized_by",
            "writer": "authored_by",
            "synthesizer": "synthesized_by",
            "assessor": "reviewed_by",
            "auditor": "reviewed_by",
            "reviewer": "reviewed_by",
            "lead": "synthesized_by",
            "researcher_contributor": "participates_in",
            "filename_derived": "authored_by",
        }
        edge_type_raw = role_map.get(a.role, "authored_by")
        edge_type, in_wl = _resolve_edge_type(edge_type_raw)
        edges.append({
            "edge_type": edge_type,
            "in_whitelist": in_wl,
            "source": f"gates:{orphan_rec['sid']}:{src_basename}",
            "target": f"researchers:{a.canonical}",
            "comment": f"INVESTIGATOR-EXTRACTED | gen={orphan_rec['generation']} | role={a.role} | raw='{a.raw_token}'",
        })

    # Upstream edges (mix of in-whitelist and needs-extension)
    for u in upstream:
        kind_map = {
            "source": "derived_from",            # ✓ whitelist
            "source_files": "derived_from",      # ✓ whitelist
            "reviewing": "reviewed_by",          # ✓ whitelist (semantic: this file reviews target)
            "reviewed": "reviewed_by",           # ✓ whitelist
            "predecessor": "cites_prior_session",  # ✓ whitelist (closest semantic)
            "extracted_from": "derived_from",    # ✓ whitelist (closest semantic)
            "reference_corpus": "cites_prior_session",  # ✓ whitelist (closest semantic)
            "input": "feeds_into",               # ✓ whitelist (via alias 'consumes')
        }
        edge_type_raw = kind_map.get(u.kind, "derived_from")
        edge_type, in_wl = _resolve_edge_type(edge_type_raw)
        for tgt in u.targets:
            # Heuristic: if tgt is just a number, treat as session
            if tgt.isdigit():
                target = f"sessions:s{int(tgt):02d}"
            elif "/" in tgt or tgt.endswith(".md") or tgt.endswith(".py") or tgt.endswith(".npz"):
                target = f"files:{tgt}"
            else:
                target = f"researchers:{tgt}"
            edges.append({
                "edge_type": edge_type,
                "in_whitelist": in_wl,
                "source": f"gates:{orphan_rec['sid']}:{src_basename}",
                "target": target,
                "comment": f"INVESTIGATOR-EXTRACTED | kind={u.kind} | raw='{u.raw[:80]}'",
            })

    # Downstream consumer edges (this file is REFERENCED BY others)
    cited_in_canonical, cited_in_wl = _resolve_edge_type("cited_in")
    for d in downstream[:20]:  # cap to top 20 referencing files
        edges.append({
            "edge_type": cited_in_canonical,
            "in_whitelist": cited_in_wl,
            "source": f"gates:{orphan_rec['sid']}:{src_basename}",
            "target": f"files:{d}",
            "comment": "INVESTIGATOR-EXTRACTED | downstream_consumer | scan=corpus_inbound_link_index",
        })

    return edges


# ----------------------------------------------------------------------
# Main investigator loop
# ----------------------------------------------------------------------


def investigate_one(orphan_rec: dict, corpus_index: dict[str, list[str]]) -> dict:
    """Investigate a single orphan file.

    Returns a dict with: path, archetype, archetype_desc, authors, upstream,
    downstream_consumers, recommended_edges, status_recommendation.
    """
    abs_path = ROOT / orphan_rec["path"]
    if not abs_path.exists():
        return {
            "path": orphan_rec["path"],
            "error": "FILE_NOT_FOUND",
        }
    # Read head + tail
    try:
        full_content = abs_path.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        return {"path": orphan_rec["path"], "error": str(e)}
    # Classify archetype FIRST (informs scan window)
    archetype, primary_edge, archetype_desc = classify_archetype(orphan_rec["path"])

    # Scan window: large for multi-author synthesis docs; small otherwise.
    # The S25 Investigation-* docs (161KB) have per-section **Researcher**:
    # fields well beyond any reasonable head cap, so we scan the whole file
    # for those archetypes.
    FULL_SCAN_ARCHETYPES = {
        "synergy_index", "framework_synergy", "investigation_closing",
        "fusion_synthesis", "team_synthesis", "synthesis",
        "workshop_synthesis", "combined_handout", "wayforward",
        "extraction", "handoff", "midsession_review", "results_summary",
        "review", "evaluation", "workshop",
    }
    lines = full_content.split("\n")
    if archetype in FULL_SCAN_ARCHETYPES:
        scan_text = full_content
    else:
        scan_text = "\n".join(lines[:80])

    # Extract attribution + upstream
    authors = extract_attribution(scan_text)
    upstream = extract_upstream(scan_text)

    # Filename-derived attribution fallback (S85 slot-anchored solo +
    # *-{agent}-collab.md patterns)
    existing = {a.canonical for a in authors}
    filename = orphan_rec["path"].split("/")[-1]
    filename_authors = extract_filename_authors(filename, existing)
    authors.extend(filename_authors)

    # Downstream scan: look up basename in corpus index
    basename = orphan_rec["path"].split("/")[-1]
    downstream = corpus_index.get(basename, [])
    # Filter out the orphan itself
    self_rel = orphan_rec["path"].replace("\\", "/")
    downstream = [d for d in downstream if d != self_rel]

    # Augment record
    rec = dict(orphan_rec)
    rec["archetype"] = archetype
    rec["archetype_description"] = archetype_desc
    rec["primary_edge_type"] = primary_edge
    rec["authors_extracted"] = [
        {"raw": a.raw_token, "canonical": a.canonical, "role": a.role}
        for a in authors
    ]
    rec["upstream_refs"] = [
        {"kind": u.kind, "raw": u.raw, "targets": u.targets}
        for u in upstream
    ]
    rec["downstream_consumers"] = downstream
    rec["recommended_edges"] = recommend_edges(rec, authors, upstream, downstream)

    # Status recommendation
    has_authors = len(authors) > 0
    has_chain = len(upstream) > 0 or len(downstream) > 0
    is_synthesis = archetype in {
        "synthesis", "workshop_synthesis", "fusion_synthesis",
        "team_synthesis", "synergy_index", "framework_synergy",
        "combined_handout", "wayforward", "handoff", "midsession_review",
    }
    if is_synthesis and has_authors:
        rec["status_recommendation"] = "MULTI-AUTHOR"
    elif has_authors:
        rec["status_recommendation"] = "REGEX-FIXED"
    elif is_synthesis and not has_authors:
        rec["status_recommendation"] = "MULTI-AUTHOR"  # implicit-author synthesis
    elif has_chain and not has_authors:
        rec["status_recommendation"] = "ORPHAN-PROMOTED"  # has connections, just not author
    else:
        rec["status_recommendation"] = "HISTORICAL-ONLY"

    return rec


def main() -> None:
    if not JSON_SRC.exists():
        sys.exit(f"Source JSON not found: {JSON_SRC}")
    with JSON_SRC.open("r", encoding="utf-8") as f:
        data = json.load(f)
    fm = [x for x in data["zero_files"] if x["category"] == "FORMAT-MISS"]
    agg_arch = ("master-collab", "master-synthesis", "results-workingpaper", "wave")
    orphans = [r for r in fm if not any(a in r["path"].split("/")[-1] for a in agg_arch)]
    print(f"Investigating {len(orphans)} orphan files...")

    print(f"Building corpus inbound-link index...")
    corpus_index = build_corpus_index()
    print(f"  Indexed {len(corpus_index):,} unique basenames")

    print(f"Running per-orphan investigation...")
    results: list[dict] = []
    for i, r in enumerate(orphans, 1):
        if i % 25 == 0:
            print(f"  ...{i}/{len(orphans)}")
        rec = investigate_one(r, corpus_index)
        results.append(rec)

    # Save JSON
    out_data = {
        "schema_version": "1.0",
        "generated_at": "2026-05-17",
        "source_corpus": str(JSON_SRC.relative_to(ROOT)).replace("\\", "/"),
        "orphan_count": len(results),
        "results": results,
    }
    OUT_JSON.write_text(json.dumps(out_data, indent=2), encoding="utf-8")
    print(f"Wrote {OUT_JSON.relative_to(ROOT)} ({OUT_JSON.stat().st_size:,}B)")

    # Summary statistics
    archetype_counts: dict[str, int] = defaultdict(int)
    status_counts: dict[str, int] = defaultdict(int)
    edge_counts: dict[str, int] = defaultdict(int)
    author_count = 0
    upstream_count = 0
    downstream_count = 0
    total_recommended = 0
    for r in results:
        if "error" in r:
            continue
        archetype_counts[r["archetype"]] += 1
        status_counts[r["status_recommendation"]] += 1
        author_count += len(r["authors_extracted"])
        upstream_count += len(r["upstream_refs"])
        downstream_count += len(r["downstream_consumers"])
        for e in r["recommended_edges"]:
            edge_counts[e["edge_type"]] += 1
            total_recommended += 1
    print()
    print(f"Archetype distribution:")
    for arch, n in sorted(archetype_counts.items(), key=lambda x: -x[1]):
        print(f"  {arch:40s}: {n}")
    print()
    print(f"Recommended status:")
    for st, n in sorted(status_counts.items(), key=lambda x: -x[1]):
        print(f"  {st:20s}: {n}")
    print()
    print(f"Total extracted attributions: {author_count}")
    print(f"Total upstream chain refs:    {upstream_count}")
    print(f"Total downstream consumers:   {downstream_count}")
    print(f"Total recommended edges:      {total_recommended}")
    print(f"  Per edge type:")
    for et, n in sorted(edge_counts.items(), key=lambda x: -x[1]):
        print(f"    {et:25s}: {n}")


if __name__ == "__main__":
    main()
