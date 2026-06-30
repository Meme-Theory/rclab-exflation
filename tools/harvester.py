#!/usr/bin/env python3
"""harvester.py - consolidated edge harvester for the knowledge index.

Replaces the ten legacy harvest_*.py scripts with a single CLI entry point
exposing each as a subcommand. The original logic from each script is wrapped
in a private closure function (_archive_harvester, _provenance_harvester, ...)
so HEADER_TEMPLATE / main() / ROOT / OUT_PATH definitions stay local to each
implementation and don't collide.

Subcommands:
  archive                - Phase 1: edges from session-archive synthesis files.
  provenance             - Phase 1: script -> data -> gate lineage.
  theorem-closure        - Optional Phase 2 pass: theorem-closure edges from DB.
  equation               - Optional Phase 2 pass: equation-citation edges.
  attribution            - Phase 1 / G1-G7: authored_by / co_authored_by / reviewed_by.
  chain-of-custody       - Phase 1.1: carries_forward / anchored_in / succ_of.
  plan-pin               - Edges from session-plan PIN MAPs.
  workingpaper           - Edges from session-N workingpaper gate sections.
  script-import          - Edges from `from canonical_constants import X` patterns.
  archive-script-import  - Same, against the computations archive.

Each subcommand executes the original harvester's main() pipeline unchanged.
"""
from __future__ import annotations

import argparse
import ast
import json
import os
import re
import sqlite3
import sys
import types
from collections import Counter, defaultdict, OrderedDict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set, Tuple

# Shared path setup. Each harvester closure inherits these via Python's
# function-scope lookup (locals -> enclosing -> module -> builtins).
PROJECT_ROOT = Path(__file__).resolve().parent.parent
ROOT = PROJECT_ROOT                       # alias used by some harvesters
HERE = Path(__file__).resolve().parent    # alias used by some harvesters
COMPUTATIONS_DIR = PROJECT_ROOT / "computations"
COMPUTATIONS = COMPUTATIONS_DIR           # alias used by script-import
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
CC_PATH = SHARED_DIR / "canonical_constants.py"
DB_PATH = PROJECT_ROOT / "tools" / "knowledge.db"
ARCHIVE = PROJECT_ROOT / "computation-archive"   # used by archive-script-import
CANONICAL = CC_PATH                              # alias used by archive-script-import

# Make canonical_constants importable for harvesters that rely on
# `import canonical_constants as CC` (script-import edges build VOCAB via
# dir(CC)). Insert tools/../computations/_shared at front of sys.path.
if str(SHARED_DIR) not in sys.path:
    sys.path.insert(0, str(SHARED_DIR))

# Make format_generations symbols available to the attribution closure
# (was: from _format_generation_regex_set import ...). format_generations.py
# lives in the same tools/ directory.
from format_generations import (   # noqa: E402
    AttributionEdge,
    G1_AGENT_RE,
    canonicalize_agent,
    extract_g1,
    extract_g2,
    extract_g3,
    extract_g5_per_gate,
    extract_g6,
    extract_g7,
    extract_workshop_g7,
    session_to_generation,
)

import importlib.util   # noqa: E402  - used by plan-pin + archive-script-import closures

# Chain-of-custody extractor library, inlined here so the chain-of-custody
# closure has access without depending on the standalone module.
# ---- BEGIN INLINED _chain_of_custody_extractors.py ----
AGENTS_DIR = ROOT / ".claude" / "agents"


# ---------------------------------------------------------------------------
# ChainOfCustodyEdge (mirrors AttributionEdge from _format_generation_regex_set)
# ---------------------------------------------------------------------------

@dataclass
class ChainOfCustodyEdge:
    """A single chain-of-custody edge with audit trail metadata.

    Fields mirror AttributionEdge so downstream EdgeBuf can consume both.
    """
    edge_type: str           # carries_forward / anchored_in / cited_in / succ_of
    source_type: str         # gates / sessions / researchers / data_provenance
    source_id: str
    target_type: str
    target_id: str
    role: Optional[str]      # optional qualifier (e.g., "predecessor")
    confidence: str          # one of {verdict-line, table-row, path-citation,
                             #         heading-order, list-item}
    pattern: str             # which extractor produced this edge
    match_text: str          # verbatim snippet for audit


# ---------------------------------------------------------------------------
# Researcher-directory -> canonical-agent mapping
# ---------------------------------------------------------------------------
#
# Built from `researchers/` directory listing (2026-05-17) + `.claude/agents/`
# canonical agent IDs. Directories with no dedicated agent are mapped to a
# kebab-cased topic slug (still emitted as type=researchers so the Genealogy
# view treats them as researcher-class nodes).
#
# Verified via `Bash ls researchers/` (38 directories).

RESEARCHER_DIR_TO_AGENT: dict[str, str] = {
    # ---- Directories with canonical .claude/agents/ ----
    "Antimatter":            "dirac-antimatter-theorist",
    "Baptista":              "baptista-spacetime-analyst",
    "Berry":                 "berry-geometric-phase-theorist",
    "Connes":                "connes-ncg-theorist",
    "Cosmic-Web":            "cosmic-web-theorist",
    "Einstein":              "einstein-theorist",
    "Feynman":               "feynman-theorist",
    "Hawking":               "hawking-theorist",
    "Kaku":                  "kaku-speculative-theorist",
    "Kaluza-Klein":          "kaluza-klein-theorist",
    "Kitaev":                "kitaev-quantum-chaos-theorist",
    "Landau":                "landau-condensed-matter-theorist",
    "Little-Red-Dots":       "little-red-dots-jwst-analyst",
    "Lizzi":                 "lizzi-spectral-functional-theorist",
    "Mack":                  "mack-cosmic-bridge",
    "Nazarewicz":            "nazarewicz-nuclear-structure-theorist",
    "Neutrino-Detection":    "neutrino-detection-specialist",
    "Paasch":                "paasch-mass-quantization-analyst",
    "Phonon-First":          "phonon-first-cosmologist",
    "Quantum-Acoustics":     "quantum-acoustics-theorist",
    "Quantum-Foam":          "quantum-foam-theorist",
    "Sagan":                 "sagan-empiricist",
    "Schwarzschild-Penrose": "schwarzschild-penrose-geometer",
    "Spectral-Geometry":     "spectral-geometer",
    "String-Theory":         "string-theory-theorist",
    "Tesla-Resonance":       "tesla-resonance",
    "Transit-Dynamics":      "transit-dynamics-theorist",
    "Van-den-Dungen":        "van-den-dungen-bridge-theorist",
    "Volovik":               "volovik-superfluid-universe-theorist",
    # ---- Topic dirs without dedicated agents (kebab-cased slug) ----
    "Amari":                 "amari-information-geometry",
    "Inflation":             "inflation-topic",
    "Jacobson":              "jacobson-thermodynamic-gravity",
    "K-Theory":              "k-theory-topic",
    "Lost-Treasures":        "lost-treasures-topic",
    "Parker":                "parker-pair-production",
    "RF-Antimatter":         "rf-antimatter-topic",
    "Richardson-Gaudin":     "richardson-gaudin-topic",
    "Togelius":              "togelius-topic",
}


def researcher_dir_to_id(domain: str) -> Optional[str]:
    """Map a researchers/ subdir name to a canonical researcher id.

    Returns None if the domain is not in the table (silently skips e.g.
    'misc' or 'agents.md' / 'index.md' which are NOT subdirectories).
    """
    return RESEARCHER_DIR_TO_AGENT.get(domain)


# ---------------------------------------------------------------------------
# Regex sets
# ---------------------------------------------------------------------------

# ---- carries_forward ----
#
# Heading variants (verified at session-90-w2-workingpaper.md:1974, 1983):
#   ### CF-W2-5-CF-60-DEPENDENT — §W2-5 §VII.AR Sub-claim B advancement (...)
#   ### CF-W2-13-DR3-READINESS-REMEDIATION — DR3 binding-protocol 3-gap remediation
#   ### CF-1 — Header-line description
#   ### CF-{NUMBER} — title
# The CF-id portion is everything after `### ` and before the em-dash or end-of-line.

CF_HEADING_RE = re.compile(
    r"^###\s+(?P<cfid>CF[-A-Za-z0-9_]+)\s*(?:—|–|--)?\s*(?P<title>[^\n]*?)$",
    re.MULTILINE,
)

# 4-field table row (verified at session-90-w2-workingpaper.md:1978):
#   | **What** | Re-dispatch §W2-5 ... |
# Captures the value cell after a Field cell containing "What".
CF_TABLE_WHAT_RE = re.compile(
    r"^\|\s*\*\*What\*\*\s*\|\s*(?P<what>[^|][^|\n]+?)\s*\|\s*$",
    re.MULTILINE,
)

# Legacy 7-bullet Action Item (verified at researchers-of-our-time format
# and `.claude/rules/output-standards.md` §"Action Items Format"):
#   1. **What**: ...
# (Phase 1.1 emission: same edge, lower confidence tag)
CF_BULLET_WHAT_RE = re.compile(
    r"^\s*\d+\.\s+\*\*What\*\*\s*:\s*(?P<what>[^\n]+)$",
    re.MULTILINE,
)


# ---- anchored_in ----
#
# S81+ canonical (verified at session-90/s90_gate_verdicts.txt:1):
#   S90-VII-AN-AUDIT-SCRIPT-...: PASS -- value='...'
# Pre-S81 legacy (verified at session-24/s24a_gate_verdicts.txt:10):
#   GATE V-1: V_spec Monotone — Constraint Condition: ...
# Pre-S81 legacy alt (verified at session-26/s26_gate_verdicts.txt:10):
#   GATE T-1: Torsion Gap Gate -- PENDING

VERDICT_CANONICAL_RE = re.compile(
    r"^(?P<gate>[A-Z][A-Z0-9][A-Z0-9_-]+):\s+(?:PASS|FAIL|INFO|PASSED|FAILED|"
    r"PENDING|PRE-REG-INC|UNCOMPUTED)\b",
    re.MULTILINE,
)

VERDICT_LEGACY_RE = re.compile(
    r"^GATE\s+(?P<gate>[A-Z][A-Z0-9_-]*(?:-[A-Z0-9_]+)*)\s*:",
    re.MULTILINE,
)


# ---- cited_in ----
#
# Verified at sessions/observational_avenues.md:64, session-52/session-52-
# tesla-collab.md:175, session-62/session-62-vdd-tesla-workshop.md:35:
#   `researchers/Cosmic-Web/17_2025_DESI_BAO_Cosmological_Constraints.md`
#   Papers 01, 05, 06, 08, 09, 10, 11, 14, 16, 21, 24, 28, 29 from `researchers/Tesla-Resonance/`
#   `researchers/Van-den-Dungen/01_2018_van_den_Dungen_Kasparov_Submersions.md`
# We capture the domain (between `researchers/` and the next `/`). The optional
# trailing paper-md gives us file-level granularity; for now we emit a single
# (researcher, session) edge per session-file (dedup'd).

RESEARCHER_PATH_RE = re.compile(
    r"researchers/(?P<domain>[A-Z][A-Za-z0-9_-]+)/"
    r"(?P<paper>\d{2}_[^\s`\"'<>]+\.md)?",
)


# ---- succ_of ----
#
# Plan-file heading variants (verified):
#   sessions/session-plan/session-90-plan-w2.md:67-553 (S90 format):
#     `## §W2-1. CF-18 — S90-VII-AAU-VII-AV-WITHDRAWN-IN-FAVOR-OF-S90-LANDING-CLEANUP`
#   sessions/session-plan/session-91-plan-w1.md:63 (S91 format):
#     `## §W1-1. CF-S91-V4-K_CANONICAL-MULTI-BRANCH-FOSSIL-TEST (T1.3; DISPATCHED FIRST)`
#   sessions/session-plan/archive/session-88-plan-w7c.md (S88 format):
#     `## §W7c-84 — `S88-W9c-1-PRIMARY-LIVE-PHYSICAL-RE-RUN``
# Three variants: (.\s — \`X\`), (.\sX), (.\.\sCF-N — X).

# Captures wave-id, item-index, and the FOLLOWING text (which contains gate-ID)
PLAN_WAVE_HEADING_RE = re.compile(
    r"^##\s+§W(?P<wave>[0-9]+[a-z]?[0-9]*)-(?P<item>[0-9]+)"
    r"(?:[\.\s—–-]+)\s*(?P<rest>[^\n]+)$",
    re.MULTILINE,
)

# Within the `rest` text, locate the actual gate-ID:
# - if rest begins with `CF-XX — ` then gate is what's after the em-dash
# - if rest begins with a backticked ID, gate is between backticks
# - otherwise gate is the first ALL-CAPS-hyphenated token

PLAN_GATE_BACKTICKED_RE = re.compile(r"`(?P<gate>[A-Za-z][A-Za-z0-9_-]+)`")
PLAN_GATE_CFPREFIX_RE = re.compile(
    r"^CF-[A-Za-z0-9_-]+\s+(?:—|–|--)\s+(?P<gate>[A-Z][A-Z0-9_-]+(?:-[A-Z0-9_]+)+)"
)
PLAN_GATE_PREFIX_CF_RE = re.compile(r"^(?P<gate>CF-[A-Za-z0-9_-]+)\b")
PLAN_GATE_FALLBACK_RE = re.compile(r"^(?P<gate>[A-Z][A-Z0-9_-]+(?:-[A-Z0-9_]+)+)")


def extract_plan_gate_id(rest_text: str) -> Optional[str]:
    """Extract the gate ID from text following `## §W{w}-{n}.`."""
    rest = rest_text.strip()
    # Order matters: try most-specific first.
    m = PLAN_GATE_CFPREFIX_RE.match(rest)
    if m:
        return m.group("gate")
    m = PLAN_GATE_BACKTICKED_RE.search(rest)
    if m:
        return m.group("gate")
    m = PLAN_GATE_PREFIX_CF_RE.match(rest)
    if m:
        return m.group("gate")
    m = PLAN_GATE_FALLBACK_RE.match(rest)
    if m:
        return m.group("gate")
    return None


# ---------------------------------------------------------------------------
# Extractor functions
# ---------------------------------------------------------------------------

def extract_carry_forwards(text: str, session_id: str,
                           source_file: str) -> List[ChainOfCustodyEdge]:
    """Find ### CF-{ID} headings and emit sessions:N -> gates:CF-{ID} edges.

    The carry-forward heading is the structural anchor; the trailing 4-field
    table (or 7-bullet list) is the audit-trail content captured in the
    comment.
    """
    out: list[ChainOfCustodyEdge] = []
    seen: set[str] = set()
    for m in CF_HEADING_RE.finditer(text):
        cfid = m.group("cfid").strip()
        if not cfid.upper().startswith("CF"):
            continue
        # Dedup: only emit once per (session, CF-id) pair from the same file
        if cfid in seen:
            continue
        seen.add(cfid)
        title = m.group("title").strip().rstrip("—–-").strip()
        snippet = (m.group(0).strip())[:80]
        out.append(ChainOfCustodyEdge(
            edge_type="carries_forward",
            source_type="sessions",
            source_id=session_id,
            target_type="gates",
            target_id=cfid,
            role="predecessor",
            confidence="heading-parsed",
            pattern="CF_HEADING_RE",
            match_text=snippet,
        ))
    return out


def extract_anchored_in(text: str, session_id: str,
                        source_file: str) -> List[ChainOfCustodyEdge]:
    """Parse a `s{N}_gate_verdicts.txt` text and emit gates:G -> sessions:N
    edges for every gate verdict line (S81+ canonical AND pre-S81 legacy)."""
    out: list[ChainOfCustodyEdge] = []
    seen: set[str] = set()

    # S81+ canonical: GATE-ID at line start followed by `: PASS|FAIL|INFO --`
    for m in VERDICT_CANONICAL_RE.finditer(text):
        gate = m.group("gate").strip()
        if gate.upper() in ("GATE",):  # not a real gate id; legacy marker
            continue
        # Skip ASCII-art separator lines like "PRE-REG:" if any
        if "=" in gate or len(gate) < 3:
            continue
        if gate in seen:
            continue
        seen.add(gate)
        out.append(ChainOfCustodyEdge(
            edge_type="anchored_in",
            source_type="gates",
            source_id=gate,
            target_type="sessions",
            target_id=session_id,
            role="verdict-line-host",
            confidence="verdict-line",
            pattern="VERDICT_CANONICAL_RE",
            match_text=m.group(0)[:120],
        ))

    # Pre-S81 legacy: `GATE V-1: ...`
    for m in VERDICT_LEGACY_RE.finditer(text):
        gate = m.group("gate").strip()
        if gate in seen:
            continue
        seen.add(gate)
        out.append(ChainOfCustodyEdge(
            edge_type="anchored_in",
            source_type="gates",
            source_id=gate,
            target_type="sessions",
            target_id=session_id,
            role="verdict-line-host",
            confidence="verdict-line-legacy",
            pattern="VERDICT_LEGACY_RE",
            match_text=m.group(0)[:120],
        ))

    return out


def extract_researcher_citations(text: str, session_id: Optional[str],
                                 source_file: str) -> List[ChainOfCustodyEdge]:
    """Find `researchers/<Domain>/[paper.md]` path references in `text`.

    Emits one edge per (researcher, source_file) pair, deduped. If session_id
    is set the target is sessions:N; otherwise the target is the source-file
    treated as data_provenance.
    """
    out: list[ChainOfCustodyEdge] = []
    seen: set[str] = set()
    for m in RESEARCHER_PATH_RE.finditer(text):
        domain = m.group("domain")
        rid = researcher_dir_to_id(domain)
        if not rid:
            continue
        if rid in seen:
            continue
        seen.add(rid)
        if session_id:
            tgt_type, tgt_id = "sessions", session_id
        else:
            tgt_type, tgt_id = "data_provenance", source_file
        out.append(ChainOfCustodyEdge(
            edge_type="cited_in",
            source_type="researchers",
            source_id=rid,
            target_type=tgt_type,
            target_id=tgt_id,
            role="paper-cited",
            confidence="path-citation",
            pattern="RESEARCHER_PATH_RE",
            match_text=m.group(0)[:80],
        ))
    return out


def extract_succ_of(text: str,
                    source_file: str) -> List[ChainOfCustodyEdge]:
    """Parse a plan-file's `## §W{w}-{n}.` heading order and emit succ_of edges
    for adjacent (within-wave) gate pairs."""
    out: list[ChainOfCustodyEdge] = []
    # Build an ordered list of (wave_id, item_index, gate_id) for valid headings
    headings: list[tuple[str, int, str, str]] = []  # (wave, item, gate, match)
    for m in PLAN_WAVE_HEADING_RE.finditer(text):
        wave = m.group("wave")
        try:
            item = int(m.group("item"))
        except ValueError:
            continue
        rest = m.group("rest")
        gate = extract_plan_gate_id(rest)
        if not gate:
            continue
        headings.append((wave, item, gate, m.group(0)[:100]))

    # Sort by (wave, item) to ensure ordering is canonical even if headings
    # appear out-of-order in the plan body (rare but possible).
    headings.sort(key=lambda r: (r[0], r[1]))

    # Emit succ_of edge between (i, i+1) within the same wave.
    for i in range(len(headings) - 1):
        wave_a, item_a, gate_a, _ = headings[i]
        wave_b, item_b, gate_b, snippet_b = headings[i + 1]
        if wave_a != wave_b:
            continue  # cross-wave succession not emitted
        if item_b != item_a + 1:
            continue  # non-adjacent items skipped (gaps in numbering)
        if gate_a == gate_b:
            continue
        out.append(ChainOfCustodyEdge(
            edge_type="succ_of",
            source_type="gates",
            source_id=gate_b,
            target_type="gates",
            target_id=gate_a,
            role="dispatch-successor",
            confidence="heading-order",
            pattern="PLAN_WAVE_HEADING_RE",
            match_text=snippet_b,
        ))
    return out


# ---------------------------------------------------------------------------
# Self-test fixtures (verbatim snippets from real files)
# ---------------------------------------------------------------------------

FIXTURES: list[dict] = [
    # --- carries_forward ---
    {
        "name": "CF-S90-W2-table-form",
        "extractor": "carry_forwards",
        "session_id": "90",
        "text": """## Carry-Forward Computations

### CF-W2-5-CF-60-DEPENDENT — §W2-5 §VII.AR Sub-claim B advancement (re-dispatch after W8 CF-60 PASS)

| Field | Spec |
|:------|:-----|
| **What** | Re-dispatch §W2-5 `S90-VII-AR-STAGE-2-PENDING-A36-SUB-CLAIM-ADVANCEMENT` with branch decision per W8 CF-60 outcome. |
| **Inputs** | W8 CF-60 PASS verdict |
| **Gate** | Branch decision per CF-60 outcome |
| **Effort** | 0.5 we |

### CF-W2-13-DR3-READINESS-REMEDIATION — DR3 binding-protocol 3-gap remediation

| Field | Spec |
|:------|:-----|
| **What** | Address 3 identified readiness gaps from §W2-13 CF-30 audit |
| **Inputs** | §W2-13 audit verdict + JSON report sidecar |
| **Gate** | Re-run §W2-13 audit |
| **Effort** | 0.4 we total |
""",
        # Expected: 2 CF edges to gates:CF-W2-5-CF-60-DEPENDENT and gates:CF-W2-13-DR3-READINESS-REMEDIATION
        "expected_targets": ["CF-W2-13-DR3-READINESS-REMEDIATION",
                             "CF-W2-5-CF-60-DEPENDENT"],
    },
    {
        "name": "CF-bullet-form-legacy",
        "extractor": "carry_forwards",
        "session_id": "29",
        "text": """## Action Items

### CF-1
1. **What**: Compute foo via bar
2. **Who**: agent
""",
        "expected_targets": ["CF-1"],
    },
    # --- anchored_in ---
    {
        "name": "S81+-canonical-verdict",
        "extractor": "anchored_in",
        "session_id": "90",
        "text": """S90-VII-AN-AUDIT-SCRIPT-REGISTRY-ANCHOR-RECONCILIATION-EXTENSION: PASS -- value='audit-script-extension-landed' scheme=registry-anchor-class-g-extension convention=route-a-vs-route-b-detection-static-string-compare L_max=N/A audit_sha256=7733a880dc3fcb1c45d0e12c13cf42a7659590de938c78f4049490089ad53608 content_sha256=f82bf65410a5819514da5d14b8126dd5263543224913d14d0b8ea51a53a230b4 schema_version=S87+
# audit_sha256_short=7733a880dc3fcb1c content_sha256_short=f82bf65410a58195 # S90-VII-AN-AUDIT-SCRIPT-REGISTRY-ANCHOR-RECONCILIATION-EXTENSION dual-SHA companion row (W9a-99 split)
S90-W1-14: PASS -- value='all_checks_pass=True'
""",
        # Expected: 2 unique gate-IDs (S90-VII-AN-...-EXTENSION and S90-W1-14)
        "expected_sources": ["S90-VII-AN-AUDIT-SCRIPT-REGISTRY-ANCHOR-RECONCILIATION-EXTENSION",
                             "S90-W1-14"],
    },
    {
        "name": "pre-S81-legacy-verdict",
        "extractor": "anchored_in",
        "session_id": "24",
        "text": """GATE V-1: V_spec Monotone — Constraint Condition: V_spec(tau) monotonically decreasing or flat for ALL rho
  Closes if: No minimum found at any rho
GATE T-1: Torsion Gap Gate -- PENDING
""",
        "expected_sources": ["T-1", "V-1"],
    },
    # --- cited_in ---
    {
        "name": "cited_in-paper-path",
        "extractor": "researcher_citations",
        "session_id": "62",
        "text": """The factorization theorem (Paper 01, `researchers/Van-den-Dungen/01_2018_van_den_Dungen_Kasparov_Submersions.md`, Main Theorem) states:
The spectral action expansion (Paper 06, `researchers/Van-den-Dungen/06_2012_Chamseddine_Marcolli_Particle_Physics_ACM.md`, eq. at line 82) reads:
Volovik's superfluid vacuum program (37 papers in `researchers/Volovik/`) derives spacetime, gauge fields, and the standard model as collective excitations of a superfluid substrate.
""",
        # 2 distinct researcher dirs cited (Van-den-Dungen, Volovik) → 2 edges (deduped per researcher)
        "expected_sources": ["van-den-dungen-bridge-theorist",
                             "volovik-superfluid-universe-theorist"],
    },
    {
        "name": "cited_in-topic-dir",
        "extractor": "researcher_citations",
        "session_id": "65",
        "text": """- See `researchers/Inflation/` for slow-roll review papers.
- DESI BAO data in `researchers/Cosmic-Web/17_2025_DESI_BAO_Cosmological_Constraints.md`.
""",
        "expected_sources": ["cosmic-web-theorist", "inflation-topic"],
    },
    # --- succ_of ---
    {
        "name": "succ_of-S90-plan-format",
        "extractor": "succ_of",
        "source_file": "session-90-plan-w2.md",
        "text": """## §W2-1. CF-18 — S90-VII-AAU-VII-AV-WITHDRAWN-IN-FAVOR-OF-S90-LANDING-CLEANUP

Body text here.

## §W2-2. CF-19 — S90-VII-NEXT-SUBSTRATE-CLOCK-UNIQUENESS-THEOREM-STAGE-1-CANDIDATE-LANDING

Body text.

## §W2-3. CF-20 — S90-VII-AH-STAGE-3-PERMANENT-PROMOTION

Body.
""",
        # 2 succ_of edges. The extractor returns the FULL gate-ID (after the
        # em-dash), NOT the CF-id prefix — because the full gate-ID is the
        # canonical identifier used in verdict files and registry text. The
        # CF-id is the wave-item bookkeeping label.
        "expected_pairs": [
            ("S90-VII-AH-STAGE-3-PERMANENT-PROMOTION",
             "S90-VII-NEXT-SUBSTRATE-CLOCK-UNIQUENESS-THEOREM-STAGE-1-CANDIDATE-LANDING"),
            ("S90-VII-NEXT-SUBSTRATE-CLOCK-UNIQUENESS-THEOREM-STAGE-1-CANDIDATE-LANDING",
             "S90-VII-AAU-VII-AV-WITHDRAWN-IN-FAVOR-OF-S90-LANDING-CLEANUP"),
        ],
    },
    {
        "name": "succ_of-S88-backtick-format",
        "extractor": "succ_of",
        "source_file": "session-88-plan-w7c.md",
        "text": """## §W7c-84 — `S88-W9c-1-PRIMARY-LIVE-PHYSICAL-RE-RUN`

## §W7c-85 — `S88-W9c-1-THIRD-PROXY-CHEEGER-SIMONS`

## §W7c-86 — `S88-W9c-1-PARITY-TWIN-FORWARD-SCAN`
""",
        # 2 succ_of edges:
        #   85 → 84
        #   86 → 85
        "expected_pairs": [
            ("S88-W9c-1-THIRD-PROXY-CHEEGER-SIMONS", "S88-W9c-1-PRIMARY-LIVE-PHYSICAL-RE-RUN"),
            ("S88-W9c-1-PARITY-TWIN-FORWARD-SCAN", "S88-W9c-1-THIRD-PROXY-CHEEGER-SIMONS"),
        ],
    },
    {
        "name": "succ_of-S91-CF-prefix-format",
        "extractor": "succ_of",
        "source_file": "session-91-plan-w1.md",
        "text": """## §W1-1. CF-S91-V4-K_CANONICAL-MULTI-BRANCH-FOSSIL-TEST (T1.3; DISPATCHED FIRST)

Body.

## §W1-2. CF-S91-CF-70-FULL-CC-MULTIPLIERS (T1.1)

Body.
""",
        # 1 succ_of edge:
        #   CF-S91-CF-70-FULL-CC-MULTIPLIERS → CF-S91-V4-K_CANONICAL-MULTI-BRANCH-FOSSIL-TEST
        "expected_pairs": [
            ("CF-S91-CF-70-FULL-CC-MULTIPLIERS",
             "CF-S91-V4-K_CANONICAL-MULTI-BRANCH-FOSSIL-TEST"),
        ],
    },
    # --- negative cases ---
    {
        "name": "carry_forwards-no-CF-headings",
        "extractor": "carry_forwards",
        "session_id": "90",
        "text": """## Some Other Section

### Not a CF heading
Just narrative text.
""",
        "expected_targets": [],
    },
    {
        "name": "anchored_in-non-verdict-text",
        "extractor": "anchored_in",
        "session_id": "90",
        "text": """SESSION 90 GATE VERDICTS

Date: 2026-05-13

============================================================
""",
        "expected_sources": [],
    },
]


# ---------------------------------------------------------------------------
# Self-test driver
# ---------------------------------------------------------------------------

def run_self_test() -> int:
    passed = 0
    failed = 0
    for fx in FIXTURES:
        text = fx["text"]
        kind = fx["extractor"]
        if kind == "carry_forwards":
            edges = extract_carry_forwards(text, session_id=fx["session_id"],
                                            source_file="fixture.md")
            got = sorted(e.target_id for e in edges)
            want = sorted(fx["expected_targets"])
        elif kind == "anchored_in":
            edges = extract_anchored_in(text, session_id=fx["session_id"],
                                         source_file="fixture.txt")
            got = sorted(e.source_id for e in edges)
            want = sorted(fx["expected_sources"])
        elif kind == "researcher_citations":
            edges = extract_researcher_citations(text,
                                                  session_id=fx["session_id"],
                                                  source_file="fixture.md")
            got = sorted(e.source_id for e in edges)
            want = sorted(fx["expected_sources"])
        elif kind == "succ_of":
            edges = extract_succ_of(text, source_file=fx["source_file"])
            got = sorted((e.source_id, e.target_id) for e in edges)
            want = sorted(fx["expected_pairs"])
        else:
            print(f"  SKIP  {fx['name']:<40} (unknown extractor)")
            continue

        if got == want:
            print(f"  PASS  {fx['name']:<40}  ({len(got)} edges)")
            passed += 1
        else:
            print(f"  FAIL  {fx['name']:<40}")
            print(f"        expected: {want}")
            print(f"        got:      {got}")
            failed += 1

    print()
    print(f"Self-test: {passed} PASS, {failed} FAIL  ({len(FIXTURES)} total)")
    return 0 if failed == 0 else 1
# ---- END INLINED _chain_of_custody_extractors.py ----

# ==========================================================================
# ARCHIVE -- lifted from harvest_archive_edges.py
# ==========================================================================

def _archive_harvester() -> None:
    """Run the archive harvester. Lifted from harvest_archive_edges.py."""
    SUMMARY_DIR = PROJECT_ROOT / "summary"
    SUMMARY_ARCHIVE_DIR = SUMMARY_DIR / "Archives"
    CC_PATH = COMPUTATIONS_DIR / "_shared" / "canonical_constants.py"


    # ----------------------------------------------------------------------------
    # Vocabulary loaders
    # ----------------------------------------------------------------------------

    def load_canonical_names() -> set[str]:
        """Load canonical-constant names from canonical_constants.py.

        Imports the module and harvests dir(CC), then filters out
        re-exported modules / functions / classes / built-ins so that names
        like `np`, `sys`, `warnings`, `warn_stale` do not pollute the
        constant vocabulary. The leak was silent for table-cell harvesters
        (table cells don't reference Python module names) but leaked badly
        for any source-text harvester downstream.
        """
        import inspect
        import types
        if not CC_PATH.exists():
            return set()
        sys.path.insert(0, str(COMPUTATIONS_DIR / "_shared"))
        try:
            import canonical_constants as CC  # noqa: WPS433
        except Exception:                         # noqa: BLE001
            return set()
        out: set[str] = set()
        for name in dir(CC):
            if name.startswith("_") or not name.isidentifier():
                continue
            obj = getattr(CC, name)
            if isinstance(obj, types.ModuleType):
                continue
            if (inspect.isfunction(obj) or inspect.isclass(obj)
                    or inspect.isbuiltin(obj) or inspect.ismethod(obj)):
                continue
            out.add(name)
        return out


    # ----------------------------------------------------------------------------
    # Strict constant-name regex (copied verbatim from
    # `_harvest_edges.py:54-62`).  Two-stage filter: this regex shape AND
    # the loaded canonical-name vocabulary must both accept a token.
    # ----------------------------------------------------------------------------

    _CONSTANT_NAME_STRICT = re.compile(
        r"^(?:"
        r"[A-Z][A-Za-z0-9_]*_[A-Za-z0-9_]+"
        r"|phi_\w+|m_[A-Za-z0-9]+|M_[A-Za-z0-9]+|Delta_\w+|alpha_\w+"
        r"|beta_\w+|gamma_\w+|theta_\w+|omega_\w+|Omega_\w+|tau_\w+"
        r"|H_\d+|kappa_\w+|rho_\w+|Vol_\w+|T_\w+|J_\w+|S_\w+|E_\w+"
        r"|[A-Za-z]+_[A-Za-z0-9_]+\d|[A-Za-z]+\d[A-Za-z0-9_]*"
        r")$"
    )

    # A gate-ID shape covers legacy (`NEFF-THOULESS-35`, `V-1`, `B-30b`,
    # `OoO-3a`), T3 (`T3-S69-BCS-SURFACE-GRAVITY`), and lowercase-suffix
    # (`P-30conv`, `RGE-A`) forms.  Lowercase letters are allowed because S30+
    # adopted lowercase wave/sub-session suffixes (`B-30b`, `B-30Aa`).
    RE_GATE_ID = re.compile(r"^(?:T3-)?[A-Z][A-Za-z0-9]*(?:-[A-Za-z0-9]+)+$")
    RE_LOOSE_GATE_ID = re.compile(r"\b((?:T3-)?[A-Z][A-Za-z0-9]*(?:-[A-Za-z0-9]+){1,5})\b")

    # Verdict vocabulary observed across S20-S85 summaries.  Some sessions use
    # "FIRES / DOES NOT FIRE" terminology (Hard-Close gates, S30 style); others
    # use PASS/FAIL/INFO (S35+ style).  All of these mark a gate-row in a table.
    VERDICT_VOCAB = {
        "PASS", "FAIL", "INFO", "NEUTRAL", "DIAGNOSTIC", "CLOSED", "INFORMATIVE",
        "FIRES", "DOES NOT FIRE", "DOES-NOT-FIRE", "CANNOT FIRE", "CANNOT-FIRE",
        "MOOT", "REFRAMED", "FAIL/REFRAMED", "NOT COMPUTED", "NOT-COMPUTED",
        "UNCOMPUTED", "TRIVIAL", "QUEUED", "DEFERRED",
    }
    # Pre-compute uppercase forms for fast comparison
    VERDICT_VOCAB_UC = {v.upper() for v in VERDICT_VOCAB}
    RE_PCT_VERDICT = re.compile(r"^\d+%$")            # e.g. "32%" sagan-style

    # Filename in `summary/Archives/session-NN[a-z]?-final.md` (or quicklook).
    RE_SUMMARY_FILE = re.compile(
        r"^session-(?P<sess>\d+[a-z]?)-(?:final|quicklook|synthesis)\.md$",
        re.IGNORECASE,
    )


    # ----------------------------------------------------------------------------
    # Markdown helpers
    # ----------------------------------------------------------------------------

    def split_table_blocks(text: str) -> list[tuple[str, str]]:
        """Return [(heading, body), ...] for every '## ' section.

        The first chunk before any '## ' becomes ('', preamble).
        """
        blocks: list[tuple[str, str]] = []
        cur_header = ""
        cur_body: list[str] = []
        for line in text.splitlines(keepends=True):
            if line.startswith("## "):
                blocks.append((cur_header, "".join(cur_body)))
                cur_header = line[3:].strip()
                cur_body = []
            else:
                cur_body.append(line)
        blocks.append((cur_header, "".join(cur_body)))
        return blocks


    def parse_markdown_table_rows(body: str) -> list[list[str]]:
        """Return list of cell-lists for every data row in any markdown table
        appearing in `body`. Skips header and divider rows.
        """
        out: list[list[str]] = []
        in_table = False
        seen_divider = False
        for raw in body.splitlines():
            line = raw.strip()
            if not line.startswith("|"):
                in_table = False
                seen_divider = False
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if not in_table:
                in_table = True
                seen_divider = False
                continue                               # header row
            if not seen_divider:
                # Divider row: cells like ":--", "----", ":--:", etc.
                if all(re.match(r"^:?-+:?$", c) for c in cells if c):
                    seen_divider = True
                    continue
            out.append(cells)
        return out


    def strip_md_emphasis(s: str) -> str:
        """Remove markdown bold/italic/backtick wrappers from a cell."""
        return re.sub(r"[`*_]", "", s).strip()


    # ----------------------------------------------------------------------------
    # Edge-emission helper (mirrors _harvest_edges.py)
    # ----------------------------------------------------------------------------

    class EdgeBuf:
        def __init__(self) -> None:
            self.edges: list[dict] = []

        def add(self, etype: str, src_type: str, src_id: str,
                tgt_type: str, tgt_id: str, comment: str) -> None:
            if not src_id or not tgt_id:
                return
            if src_type == tgt_type and src_id == tgt_id:
                return
            self.edges.append({
                "type": etype,
                "src_type": src_type, "src_id": src_id,
                "tgt_type": tgt_type, "tgt_id": tgt_id,
                "comment": comment[:200],
            })

        def dedup(self) -> list[dict]:
            seen: set[tuple] = set()
            out: list[dict] = []
            for e in self.edges:
                key = (e["type"], e["src_type"], e["src_id"].lower(),
                       e["tgt_type"], e["tgt_id"].lower())
                if key in seen:
                    continue
                seen.add(key)
                out.append(e)
            return out


    # ----------------------------------------------------------------------------
    # Session-final extractor
    # ----------------------------------------------------------------------------

    def extract_session_id(name: str) -> str | None:
        m = RE_SUMMARY_FILE.match(name)
        if m:
            # Take just the digit-prefix; strip the optional sub-letter for the
            # session-number used as an edge target. Sub-letter sessions still
            # get their own output file.
            sess = m.group("sess")
            m2 = re.match(r"^(\d+)", sess)
            return m2.group(1) if m2 else sess
        return None


    def harvest_one(path: Path, canonical_names: set[str]) -> list[dict]:
        text = path.read_text(encoding="utf-8", errors="replace")
        sess = extract_session_id(path.name)
        if not sess:
            return []
        buf = EdgeBuf()

        blocks = split_table_blocks(text)

        # ----------- Pattern 1+3+α+γ+ζ: Gate verdict tables (multi-format) -----------
        # Five table layouts produce edges:
        #   Pattern 1 (S30/S35-style): col-0 = gate-ID, col-N = verdict
        #   Pattern α (S32/S42-style): col-0 = row#, col-1/2 = gate-ID, col-N = verdict
        #   Pattern γ (S46-quicklook): col-0 = verdict, col-2 = comma-list of gate-IDs
        #   Pattern ζ (S65-style):     col-0 = gate-ID in Constraint-Map header, NO verdict cell
        #   Pattern 3:                 cross-validation cells in any layout
        #
        # The unified scanner: find FIRST gate-ID-shaped cell (any column) and
        # FIRST verdict-shaped cell (any column).  Dispatch by their relative
        # positions and the section header.
        ZETA_HEADERS = ("constraint", "theorem", "closure", "structural")
        for header, body in blocks:
            header_lc = header.lower()
            for row in parse_markdown_table_rows(body):
                if len(row) < 2:
                    continue
                # Strip parenthetical annotations + emphasis from each cell
                cells_clean = [
                    re.sub(r"\s*\([^)]*\)\s*", "", strip_md_emphasis(c)).strip()
                    for c in row
                ]
                cells_uc = [
                    re.sub(r"\s+", " ", c.upper()) for c in cells_clean
                ]

                # Locate first gate-ID and first verdict cell (any column)
                gid_idx = -1
                gid = ""
                for i, c in enumerate(cells_clean):
                    if RE_GATE_ID.match(c):
                        gid_idx = i
                        gid = c
                        break

                verdict_idx = -1
                verdict_text = ""
                for i, cu in enumerate(cells_uc):
                    if cu in VERDICT_VOCAB_UC or RE_PCT_VERDICT.match(cu):
                        verdict_idx = i
                        verdict_text = cu
                        break
                    first_chunk = cu.split(",", 1)[0].split(";", 1)[0].strip()
                    if first_chunk in VERDICT_VOCAB_UC:
                        verdict_idx = i
                        verdict_text = first_chunk
                        break

                # Pattern γ: col-0 verdict, gate-IDs in any subsequent cell as
                # comma-separated tokens.  Only emit when col-0 is verdict-shaped
                # AND col-2 (or any later cell) contains ≥1 gate-ID-shaped token.
                if verdict_idx == 0:
                    for cell in row[1:]:
                        cell_str = strip_md_emphasis(cell)
                        for tok in re.findall(
                            r"(?:T3-)?[A-Z][A-Za-z0-9]*(?:-[A-Za-z0-9]+)+", cell_str
                        ):
                            if RE_GATE_ID.match(tok):
                                buf.add(
                                    "reproduces", "gates", tok,
                                    "sessions", sess,
                                    f"archive-harvested: γ-pattern {verdict_text} "
                                    f"verdict-list in S{sess}",
                                )
                    continue

                # Pattern 1 / α: gate-ID present somewhere AND verdict elsewhere.
                if gid_idx >= 0 and verdict_idx >= 0 and gid_idx != verdict_idx:
                    buf.add(
                        "reproduces", "gates", gid, "sessions", sess,
                        f"archive-harvested: {verdict_text} verdict in S{sess} table",
                    )
                    # Edge B: gate -> constant from ANY cell of the row mentioning
                    # a canonical-constant name token (key-number cell preferred,
                    # but constants also appear in mechanism-prose, source, and
                    # surviving-space cells).  buf.dedup() collapses duplicate
                    # (gate, constant) pairs across cells.
                    for cell in row:
                        for tok in re.findall(r"[A-Za-z_][A-Za-z0-9_]+", cell):
                            if (tok in canonical_names
                                    and _CONSTANT_NAME_STRICT.match(tok)):
                                buf.add(
                                    "reproduces", "gates", gid,
                                    "constants", tok,
                                    f"archive-harvested: row mentions {tok}",
                                )
                    # Edge C: cross-validation from prose in cells after verdict
                    for cell in row[verdict_idx + 1:]:
                        cell_clean_str = strip_md_emphasis(cell)
                        m_conf = re.search(
                            r"(?:Confirmed by|cf\.|cross-check|see also)\s+"
                            r"([A-Z][A-Za-z0-9]*(?:-[A-Za-z0-9]+){1,4})",
                            cell_clean_str,
                        )
                        if m_conf:
                            other = m_conf.group(1)
                            if RE_GATE_ID.match(other) and other != gid:
                                buf.add(
                                    "cross_validates", "gates", gid,
                                    "gates", other,
                                    f"archive-harvested: cross-check cell ({other})",
                                )
                    continue

                # Pattern ζ: gate-ID in col-0, NO verdict cell, but section header
                # implies a gate-row (Constraint Map / Theorems / Closures / Structural).
                if gid_idx == 0 and verdict_idx < 0 and any(
                    k in header_lc for k in ZETA_HEADERS
                ):
                    buf.add(
                        "reproduces", "gates", gid, "sessions", sess,
                        f"archive-harvested: ζ-pattern row in '{header[:50]}'",
                    )
                    # Constants in ALL subsequent cells (dedup at buf-level).
                    for cell in row[1:]:
                        for tok in re.findall(r"[A-Za-z_][A-Za-z0-9_]+", cell):
                            if (tok in canonical_names
                                    and _CONSTANT_NAME_STRICT.match(tok)):
                                buf.add(
                                    "reproduces", "gates", gid,
                                    "constants", tok,
                                    f"archive-harvested: ζ-pattern row mentions {tok}",
                                )
                    continue

        # ----------- Pattern 2: Mechanism Closures section -----------
        # Subsection headings look like:
        #   ### 1. Singlet Tridiagonal PMNS (PMNS-CORRECTED-35)
        # We emit closed_by from the mechanism slug to the gate.
        for m in re.finditer(
            r"^###\s+\d+\.\s+(?P<name>[^\n(]+?)\s*\((?P<gate>[A-Z][A-Z0-9_-]+)\)\s*$",
            text, re.MULTILINE,
        ):
            name = strip_md_emphasis(m.group("name")).strip()
            gate_id = m.group("gate")
            if not RE_GATE_ID.match(gate_id):
                continue
            # Mechanism slug: collapse whitespace+punctuation into underscores
            slug = re.sub(r"[^A-Za-z0-9]+", "_", name).strip("_")
            if not slug or len(slug) < 4:
                continue
            # Only emit when the section context is "Closures" — check the
            # nearest preceding ## heading.
            # We search backwards from this match for the last "## " line.
            before = text[:m.start()]
            last_h2 = before.rfind("\n## ")
            if last_h2 == -1:
                continue
            h2_line = before[last_h2 + 1:]
            if "closur" not in h2_line.lower() and "closed" not in h2_line.lower():
                # Not a closures section — skip rather than emit a mis-typed edge.
                continue
            buf.add(
                "closed_by", "open_channels", slug,
                "gates", gate_id,
                f"archive-harvested: closure section in S{sess} ({name[:60]})",
            )

        # ----------- Pattern 4: Files Produced — script -> gate -----------
        # Look for tables where col-0 is a script-prefix (sNN_...) and col-1
        # is a gate-id. Mirrors s81_harvested_edges.txt:8 convention.
        for header, body in blocks:
            if "files produced" not in header.lower() and "computation" not in header.lower():
                # Permissive: also check section text mentions "Computation Computations"
                if "computation" not in body.lower()[:200]:
                    continue
            for row in parse_markdown_table_rows(body):
                if len(row) < 2:
                    continue
                script_prefix = strip_md_emphasis(row[0])
                gate_id = strip_md_emphasis(row[1])
                if not re.match(r"^s\d+[a-z]?_[A-Za-z0-9_]+$", script_prefix):
                    continue
                if not RE_GATE_ID.match(gate_id):
                    continue
                buf.add(
                    "feeds_into", "data_provenance", f"{script_prefix}.py",
                    "gates", gate_id,
                    f"archive-harvested: Files Produced table in S{sess}",
                )

        return buf.dedup()


    # ----------------------------------------------------------------------------
    # Driver
    # ----------------------------------------------------------------------------

    def discover_summary_files() -> list[Path]:
        """Return all session-final/quicklook markdown files under summary/."""
        paths: list[Path] = []
        for d in (SUMMARY_ARCHIVE_DIR, SUMMARY_DIR):
            if not d.is_dir():
                continue
            for p in sorted(d.glob("session-*.md")):
                if RE_SUMMARY_FILE.match(p.name):
                    paths.append(p)
        return paths


    HEADER_TEMPLATE = (
        "## S{sess} Archive-Harvested Edges (generated by tools/harvest_archive_edges.py)\n"
        "## Source: summary/{rel}\n"
        "## Conservative-harvest discipline: prefer miss over false-positive\n"
        "## (per computations/_shared/_harvest_edges.py:12-14).\n"
        "\n"
    )


    def main() -> int:
        ap = argparse.ArgumentParser(description=__doc__)
        ap.add_argument("--dry", action="store_true",
                        help="Preview edges only; do not write output files.")
        ap.add_argument("--limit", type=int, default=0,
                        help="Limit to first N source files (0 = all).")
        args = ap.parse_args()

        canonical_names = load_canonical_names()
        paths = discover_summary_files()
        if args.limit:
            paths = paths[:args.limit]

        if not paths:
            print("No summary files found.")
            return 0

        total_raw = 0
        total_written = 0
        per_session: dict[str, list[dict]] = {}
        rel_for_sess: dict[str, str] = {}

        for p in paths:
            sess = extract_session_id(p.name)
            if not sess:
                continue
            edges = harvest_one(p, canonical_names)
            total_raw += len(edges)
            per_session.setdefault(sess, []).extend(edges)
            # Earliest-source-file wins for the relative-path comment.
            rel_for_sess.setdefault(sess, str(p.relative_to(SUMMARY_DIR.parent)))

        # Per-session dedup AND write.
        type_total: dict[str, int] = {}
        for sess, edges in sorted(per_session.items(), key=lambda x: int(x[0])):
            seen: set[tuple] = set()
            deduped: list[dict] = []
            for e in edges:
                key = (e["type"], e["src_type"], e["src_id"].lower(),
                       e["tgt_type"], e["tgt_id"].lower())
                if key in seen:
                    continue
                seen.add(key)
                deduped.append(e)
            if not deduped:
                continue
            for e in deduped:
                type_total[e["type"]] = type_total.get(e["type"], 0) + 1

            out_path = COMPUTATIONS_DIR / f"s{sess}_archive_harvested_edges.txt"
            if args.dry:
                print(f"[dry] would write {out_path.name}: {len(deduped)} edges")
                continue

            lines = [HEADER_TEMPLATE.format(sess=sess, rel=rel_for_sess[sess].replace("\\", "/"))]
            for e in deduped:
                lines.append(
                    f"[EDGE:{e['type']}] {e['src_type']}:{e['src_id']} -> "
                    f"{e['tgt_type']}:{e['tgt_id']}  # {e['comment']}\n"
                )
            out_path.write_text("".join(lines), encoding="utf-8")
            total_written += len(deduped)

        # Summary
        print(f"\nScanned {len(paths)} summary file(s); "
              f"harvested {total_raw} raw edge(s), wrote {total_written} unique.")
        print("By type:")
        for t, c in sorted(type_total.items(), key=lambda x: -x[1]):
            print(f"  {t:20s}  {c}")
        print("By session (top 25 by count):")
        rows = [(s, len(set(
            (e["type"], e["src_type"], e["src_id"].lower(),
             e["tgt_type"], e["tgt_id"].lower())
            for e in es)))
            for s, es in per_session.items()]
        for s, c in sorted(rows, key=lambda x: -x[1])[:25]:
            if c > 0:
                print(f"  S{s:>4s}  {c:4d} edges")
        return 0
    main()


# ==========================================================================
# PROVENANCE -- lifted from harvest_provenance_edges.py
# ==========================================================================

def _provenance_harvester() -> None:
    """Run the provenance harvester. Lifted from harvest_provenance_edges.py."""
    OUT_PATH = COMPUTATIONS_DIR / "canonical_constants_provenance_edges.txt"

    # Match an assignment line with an inline comment.
    RE_ASSIGN_COMMENT = re.compile(
        r"^([A-Za-z_]\w*)\s*=.+?#(.+)$",
        re.MULTILINE,
    )
    # Session refs: S<num> or S<num><lower-letter> or "session NN"
    RE_SESS = re.compile(r"\bS(\d+)[a-z]?\b|\bsession[- ](\d+)", re.IGNORECASE)


    def load_canonical_names() -> set[str]:
        """Mirror harvest_archive_edges.py.load_canonical_names — including
        the module/function/class filter that prevents `np`, `sys`,
        `warnings`, `warn_stale` from leaking into the vocab."""
        import inspect
        import types
        sys.path.insert(0, str(COMPUTATIONS_DIR / "_shared"))
        try:
            import canonical_constants as CC  # noqa: WPS433
        except Exception:
            return set()
        out: set[str] = set()
        for name in dir(CC):
            if name.startswith("_") or not name.isidentifier():
                continue
            obj = getattr(CC, name)
            if isinstance(obj, types.ModuleType):
                continue
            if (inspect.isfunction(obj) or inspect.isclass(obj)
                    or inspect.isbuiltin(obj) or inspect.ismethod(obj)):
                continue
            out.add(name)
        return out


    def harvest() -> list[tuple[str, str, str]]:
        """Return list of (constant_name, session_id, comment_excerpt)."""
        if not CC_PATH.exists():
            return []
        text = CC_PATH.read_text(encoding="utf-8", errors="replace")
        canonical_names = load_canonical_names()
        seen: set[tuple[str, str]] = set()
        edges: list[tuple[str, str, str]] = []
        for m in RE_ASSIGN_COMMENT.finditer(text):
            name = m.group(1)
            comment = m.group(2).strip()
            if name not in canonical_names:
                continue
            for sm in RE_SESS.finditer(comment):
                sess = sm.group(1) or sm.group(2)
                key = (name, sess)
                if key in seen:
                    continue
                seen.add(key)
                edges.append((name, sess, comment[:120]))
        return edges


    HEADER = (
        "## Canonical Constants Provenance Edges\n"
        "## Generated by tools/harvest_provenance_edges.py\n"
        "## Source: computations/_shared/canonical_constants.py inline comments\n"
        "## Edge type: constants -> sessions (derived_from)\n"
        "\n"
    )


    def main() -> int:
        edges = harvest()
        if not edges:
            print("No provenance edges harvested.")
            return 0
        lines = [HEADER]
        for name, sess, comment in edges:
            lines.append(
                f"[EDGE:derived_from] constants:{name} -> sessions:{sess}  "
                f"# provenance: {comment}\n"
            )
        OUT_PATH.write_text("".join(lines), encoding="utf-8")
        distinct_constants = len({n for n, _, _ in edges})
        distinct_sessions = len({s for _, s, _ in edges})
        print(
            f"Wrote {OUT_PATH.relative_to(PROJECT_ROOT)}: {len(edges)} edges "
            f"({distinct_constants} constants -> {distinct_sessions} sessions)"
        )
        return 0
    main()


# ==========================================================================
# THEOREM-CLOSURE -- lifted from harvest_theorem_closure_edges.py
# ==========================================================================

def _theorem_closure_harvester() -> None:
    """Run the theorem-closure harvester. Lifted from harvest_theorem_closure_edges.py."""
    OUT_PATH = COMPUTATIONS_DIR / "theorem_closure_edges.txt"


    # ----------------------------------------------------------------------------
    # Vocabulary loader (mirrors harvest_archive_edges.py:46-59)
    # ----------------------------------------------------------------------------

    def load_canonical_names() -> set[str]:
        """Return the set of identifier-shaped public names exported by
        canonical_constants.py. This vocabulary is the membership filter
        used in conjunction with the word-boundary regex.
        """
        if not CC_PATH.exists():
            return set()
        sys.path.insert(0, str(COMPUTATIONS_DIR / "_shared"))
        try:
            import canonical_constants as CC  # noqa: WPS433
        except Exception:                         # noqa: BLE001
            return set()
        return {n for n in dir(CC) if not n.startswith("_") and n.isidentifier()}


    # ----------------------------------------------------------------------------
    # Row-text extraction
    # ----------------------------------------------------------------------------

    def row_get(row: sqlite3.Row, col: str) -> str:
        """Defensive .get() for sqlite3.Row -- returns "" when the column
        is NULL or absent. sqlite3.Row supports __getitem__ but raises
        IndexError on unknown keys, so we wrap.
        """
        try:
            v = row[col]
        except (IndexError, KeyError):
            return ""
        if v is None:
            return ""
        return str(v)


    # ----------------------------------------------------------------------------
    # Per-row scan: emit (entity_id, constant_name) pairs where
    # `\b<name>\b` matches the concatenated text and `name` is in vocab.
    # ----------------------------------------------------------------------------

    def scan_text(text: str, vocab: set[str], compiled: dict[str, re.Pattern]) -> set[str]:
        """Return the set of canonical-constant names found in `text` via
        word-boundary match. The compiled-pattern cache is shared across
        rows so the regex compile cost is paid once per name.
        """
        if not text:
            return set()
        found: set[str] = set()
        # Coarse pre-filter: only test names whose first 2 chars appear in
        # the text (cheap O(len(text)) substring check). This skips ~95%
        # of vocab on short statements.
        text_lower = text.lower()
        for name in vocab:
            if name[:2].lower() not in text_lower and name[:2] not in text:
                # Substring miss on both case-folded and exact prefix --
                # the word-boundary regex cannot match.
                continue
            pat = compiled.get(name)
            if pat is None:
                pat = re.compile(r"\b" + re.escape(name) + r"\b")
                compiled[name] = pat
            if pat.search(text):
                found.add(name)
        return found


    # ----------------------------------------------------------------------------
    # Driver
    # ----------------------------------------------------------------------------

    HEADER = (
        "## Theorem & Closed-Mechanism -> Constants Edges\n"
        "## Generated by tools/harvest_theorem_closure_edges.py\n"
        "## Source: tools/knowledge.db (theorems.statement + closed_mechanisms.closed_by)\n"
        "## Vocabulary: computations/_shared/canonical_constants.py public names\n"
        "## Match rule: word-boundary regex (\\b<name>\\b) AND vocab membership\n"
        "## Edge type: bounds (theorem/closure cites a constant in its statement/note)\n"
        "\n"
    )


    def main() -> int:
        vocab = load_canonical_names()
        if not vocab:
            print("ERROR: canonical_constants.py vocabulary is empty; aborting.")
            return 1
        if not DB_PATH.exists():
            print(f"ERROR: knowledge.db not found at {DB_PATH}")
            return 1

        con = sqlite3.connect(str(DB_PATH))
        con.row_factory = sqlite3.Row

        compiled: dict[str, re.Pattern] = {}
        edges: list[tuple[str, str, str, str]] = []  # (alias, ent_id, const, snippet)
        inbound: Counter[str] = Counter()
        errors: list[tuple[str, str, str]] = []

        # ---------------- theorems ----------------
        n_theorems_scanned = 0
        n_theorems_edges = 0
        for row in con.execute("SELECT id, name, statement FROM theorems"):
            try:
                ent_id = row_get(row, "id")
                name = row_get(row, "name")
                statement = row_get(row, "statement")
                if not ent_id:
                    continue
                n_theorems_scanned += 1
                text = (name + " " + statement).strip()
                if not text:
                    continue
                hits = scan_text(text, vocab, compiled)
                for const in sorted(hits):
                    snippet = (name + " | " + statement).strip(" |")[:150]
                    edges.append(("theorems", ent_id, const, snippet))
                    inbound[const] += 1
                    n_theorems_edges += 1
            except Exception as exc:                  # noqa: BLE001
                errors.append(("theorems", row_get(row, "id"), repr(exc)))

        # ---------------- closed_mechanisms ----------------
        # Schema: closed_mechanisms(id, name, closed_by, session, gate_id,
        # source_file). The task spec named the note column "status_note"
        # but the actual column is `closed_by` -- per the task's
        # "use .get() defensively in case statement is null" instruction
        # we treat closed_by as the note text and skip rows where neither
        # name nor closed_by has content.
        n_closures_scanned = 0
        n_closures_edges = 0
        for row in con.execute(
            "SELECT id, name, closed_by FROM closed_mechanisms"
        ):
            try:
                ent_id = row_get(row, "id")
                name = row_get(row, "name")
                note = row_get(row, "closed_by")
                if not ent_id:
                    continue
                n_closures_scanned += 1
                text = (name + " " + note).strip()
                if not text:
                    continue
                hits = scan_text(text, vocab, compiled)
                for const in sorted(hits):
                    snippet = (name + " | " + note).strip(" |")[:150]
                    edges.append(("closed_mechanisms", ent_id, const, snippet))
                    inbound[const] += 1
                    n_closures_edges += 1
            except Exception as exc:                  # noqa: BLE001
                errors.append(("closed_mechanisms", row_get(row, "id"), repr(exc)))

        # ---------------- dedup (entity_id, constant_name) pairs ----------------
        seen: set[tuple[str, str]] = set()
        deduped: list[tuple[str, str, str, str]] = []
        for alias, ent_id, const, snippet in edges:
            key = (ent_id, const)
            if key in seen:
                continue
            seen.add(key)
            deduped.append((alias, ent_id, const, snippet))

        # Recompute inbound from deduped pairs (counter above
        # double-counts when the same theorem cites the same const twice
        # via name+statement vs statement-only matches).
        inbound = Counter()
        n_theorems_unique = 0
        n_closures_unique = 0
        for alias, ent_id, const, _snippet in deduped:
            inbound[const] += 1
            if alias == "theorems":
                n_theorems_unique += 1
            else:
                n_closures_unique += 1

        # ---------------- write output ----------------
        lines = [HEADER]
        for alias, ent_id, const, snippet in deduped:
            kind_tag = "theorem statement" if alias == "theorems" else "closure note"
            lines.append(
                f"[EDGE:bounds] {alias}:{ent_id} -> constants:{const}  "
                f"# {kind_tag} cites {const} ({snippet})\n"
            )
        OUT_PATH.write_text("".join(lines), encoding="utf-8")

        # ---------------- report ----------------
        print(f"Wrote {OUT_PATH.relative_to(PROJECT_ROOT)}")
        print(f"Theorems scanned: {n_theorems_scanned} | "
              f"unique edges emitted: {n_theorems_unique}")
        print(f"Closures scanned: {n_closures_scanned} | "
              f"unique edges emitted: {n_closures_unique}")
        print(f"Total unique edges: {len(deduped)}")
        print()
        print("Top 15 constants by inbound degree (theorems + closures combined):")
        for const, c in inbound.most_common(15):
            print(f"  {const:30s}  {c}")
        print()
        if errors:
            print(f"Errored rows ({len(errors)}):")
            for tbl, rid, exc in errors[:20]:
                print(f"  {tbl}:{rid}  {exc}")
        else:
            print("Errored rows: 0")
        return 0
    main()


# ==========================================================================
# EQUATION -- lifted from harvest_equation_edges.py
# ==========================================================================

def _equation_harvester() -> None:
    """Run the equation harvester. Lifted from harvest_equation_edges.py."""
    OUT_PATH = ROOT / "computations" / "_shared" / "equation_edges.txt"


    # ----------------------------------------------------------------------------
    # 1. Canonical-constant vocab extraction
    # ----------------------------------------------------------------------------
    def load_canonical_vocab(cc_path: Path) -> set[str]:
        """Parse canonical_constants.py and return the set of top-level names
        bound by simple assignment (Name = ...). Uses ast for robustness vs
        regex (handles multi-line RHS, dict-of-provenance blocks, etc.)."""
        src = cc_path.read_text(encoding="utf-8")
        tree = ast.parse(src)
        names: set[str] = set()
        for node in tree.body:
            # top-level assignments only
            if isinstance(node, ast.Assign):
                for tgt in node.targets:
                    if isinstance(tgt, ast.Name):
                        names.add(tgt.id)
            elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
                names.add(node.target.id)
        # Filter generics: single-letter (ambiguous in latex), all-caps short
        # tokens like "PI" (covered by other variants), pure underscore fragments.
        # Keep "PI" since it is the canonical name even if generic.
        filtered = {n for n in names if len(n) >= 2}
        # Drop python builtins / module aliases that snuck in via top-level Assign
        drop = {"np", "PROVENANCE", "warnings", "sys"}
        filtered -= drop
        return filtered


    # ----------------------------------------------------------------------------
    # 2. DB scan
    # ----------------------------------------------------------------------------
    def fetch_equations(db_path: Path):
        """Yield (id, raw, type, source_file) rows for kept equation kinds."""
        con = sqlite3.connect(str(db_path))
        cur = con.cursor()
        cur.execute(
            "SELECT id, raw, type, source_file FROM equations "
            "WHERE type IN ('display','structural')"
        )
        for row in cur:
            yield row
        con.close()


    # ----------------------------------------------------------------------------
    # 3. Edge mining
    # ----------------------------------------------------------------------------
    def build_pattern(vocab: set[str]) -> re.Pattern:
        """One combined regex with word boundaries.

        Sort by length DESC so longer names match before shorter prefixes
        (Python's `re` alternation otherwise picks the first match in pattern
        order; with word boundaries this matters less, but length-sort is a
        cheap robustness win)."""
        parts = sorted(vocab, key=len, reverse=True)
        escaped = [re.escape(p) for p in parts]
        pat = r"(?<![A-Za-z0-9_])(" + "|".join(escaped) + r")(?![A-Za-z0-9_])"
        return re.compile(pat)


    def harvest():
        vocab = load_canonical_vocab(CC_PATH)
        pattern = build_pattern(vocab)

        eq_count = 0
        edges: list[tuple[str, str]] = []
        seen: set[tuple[str, str]] = set()
        inbound: Counter[str] = Counter()

        for eq_id, raw, eq_type, source_file in fetch_equations(DB_PATH):
            eq_count += 1
            if not raw:
                continue
            # Find all distinct constant names in this equation
            hits = set(pattern.findall(raw))
            for name in hits:
                key = (eq_id, name)
                if key in seen:
                    continue
                seen.add(key)
                edges.append((eq_id, name))
                inbound[name] += 1

        return eq_count, edges, inbound, vocab


    # ----------------------------------------------------------------------------
    # 4. Emit
    # ----------------------------------------------------------------------------
    HEADER = """# equation_edges.txt
    # Auto-generated by tools/harvest_equation_edges.py
    # Source: tools/knowledge.db (equations table, type IN ('display','structural'))
    # Vocab : computations/_shared/canonical_constants.py top-level names (len>=2)
    # Format: [EDGE:depends_on] equations:EQ_ID -> constants:NAME  # <type-tag>
    #
    """


    def write_edges(edges: list[tuple[str, str]]):
        OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
        with OUT_PATH.open("w", encoding="utf-8") as f:
            f.write(HEADER)
            for eq_id, name in edges:
                f.write(
                    f"[EDGE:depends_on] equations:{eq_id} -> constants:{name}"
                    f"  # display/structural eq references {name}\n"
                )


    # ----------------------------------------------------------------------------
    # 5. Main
    # ----------------------------------------------------------------------------
    def main():
        eq_count, edges, inbound, vocab = harvest()
        write_edges(edges)

        # Report
        print(f"Vocab size (canonical-constant names, len>=2): {len(vocab)}")
        print(f"Equations scanned (type IN display,structural): {eq_count}")
        print(f"Unique edges emitted: {len(edges)}")
        print(f"Distinct constants reached: {len(inbound)}")
        print(f"Output: {OUT_PATH}")
        print()
        print("Top 20 constants by inbound degree:")
        for name, deg in inbound.most_common(20):
            print(f"  {deg:6d}  {name}")
    main()


# ==========================================================================
# ATTRIBUTION -- lifted from harvest_attribution_edges.py
# ==========================================================================

def _attribution_harvester() -> None:
    """Run the attribution harvester. Lifted from harvest_attribution_edges.py."""
    OUT_LOG = HERE / "harvest_attribution_edges.log"
    OUT_SUMMARY = HERE / "harvest_attribution_edges.summary.json"


    # ---------------------------------------------------------------------------
    # Edge buffer (mirrors EdgeBuf in harvest_archive_edges.py)
    # ---------------------------------------------------------------------------

    class EdgeBuf:
        """Accumulator with idempotent dedup keyed on
        (type, src_type, src_id.lower(), tgt_type, tgt_id.lower())."""

        def __init__(self) -> None:
            self.edges: list[dict] = []

        def add(self, etype: str, src_type: str, src_id: str,
                tgt_type: str, tgt_id: str, comment: str) -> None:
            if not src_id or not tgt_id:
                return
            if src_type == tgt_type and src_id == tgt_id:
                return
            self.edges.append({
                "type": etype,
                "src_type": src_type, "src_id": src_id,
                "tgt_type": tgt_type, "tgt_id": tgt_id,
                "comment": comment[:200],
            })

        def add_attribution(self, edge: AttributionEdge, source_file: str) -> None:
            """Translate AttributionEdge → on-disk edge tuple.

            Source-type mapping (matches ENTITY_TYPE_ALIASES in extract_entities.py):
              - `files`            → `data_provenance` (file = data artifact)
              - `gates`            → `gates`
              - `sessions`         → `sessions`
              - `workshops`        → `data_provenance` (workshop file as data artifact)
              - `researchers`      → `researchers`
            """
            TYPE_MAP = {
                "files": "data_provenance",
                "workshops": "data_provenance",
            }
            src_type = TYPE_MAP.get(edge.source_type, edge.source_type)
            tgt_type = TYPE_MAP.get(edge.target_type, edge.target_type)
            # Audit comment: pattern label + file + generation + role
            bits = [edge.generation]
            if edge.role:
                bits.append(f"role={edge.role}")
            bits.append(f"conf={edge.confidence}")
            bits.append(f"src={source_file}")
            if edge.match_text:
                snippet = re.sub(r"\s+", " ", edge.match_text)[:80]
                bits.append(f"match={snippet!r}")
            comment = " | ".join(bits)
            self.add(edge.edge_type, src_type, edge.source_id,
                     tgt_type, edge.target_id, comment)

        def dedup(self) -> list[dict]:
            seen: set[tuple] = set()
            out: list[dict] = []
            for e in self.edges:
                key = (e["type"], e["src_type"], e["src_id"].lower(),
                       e["tgt_type"], e["tgt_id"].lower())
                if key in seen:
                    continue
                seen.add(key)
                out.append(e)
            return out


    # ---------------------------------------------------------------------------
    # Per-session harvester
    # ---------------------------------------------------------------------------

    def harvest_session(sid: str, sess_dir: Path) -> tuple[EdgeBuf, dict]:
        """Run generation-appropriate extractors on every .md file in the session.
        Returns (EdgeBuf, per-file-edge-count dict)."""
        gen = session_to_generation(sid)
        buf = EdgeBuf()
        per_file_counts: dict[str, int] = {}

        md_files = sorted([p for p in sess_dir.glob("*.md") if p.is_file()])
        workshop_files = sorted([p for p in (sess_dir / "workshops").glob("*.md")
                                 if p.is_file()]) if (sess_dir / "workshops").exists() else []

        def run_one(p: Path, edges_pre: list[AttributionEdge]) -> None:
            rel = str(p.relative_to(ROOT)).replace("\\", "/")
            before = len(buf.edges)
            for e in edges_pre:
                buf.add_attribution(e, source_file=rel)
            per_file_counts[rel] = len(buf.edges) - before

        if gen == "G1":
            # G1: body-text mention frequency across all session text
            all_text = "\n".join(
                p.read_text(encoding="utf-8", errors="ignore") for p in md_files
            )
            run_one(sess_dir, extract_g1(sid, all_text))

        elif gen == "G2":
            for p in md_files:
                text = p.read_text(encoding="utf-8", errors="ignore")
                run_one(p, extract_g2(text, session_id=sid))

        elif gen in ("G3", "G4", "G5"):
            for p in md_files:
                text = p.read_text(encoding="utf-8", errors="ignore")
                file_id = f"{sid}:{p.name}"
                edges = []
                edges.extend(extract_g3(text, file_id=file_id, filename=p.name))
                edges.extend(extract_g5_per_gate(text, file_id=file_id))
                edges.extend(extract_g7(text, file_id=file_id))
                workshop_id = f"data_provenance:{p.relative_to(ROOT).as_posix()}"
                edges.extend(extract_workshop_g7(text, workshop_id=workshop_id))
                run_one(p, edges)

        elif gen == "G6":
            for p in md_files:
                text = p.read_text(encoding="utf-8", errors="ignore")
                file_id = f"{sid}:{p.name}"
                edges = []
                edges.extend(extract_g6(text, file_id=file_id))
                edges.extend(extract_g3(text, file_id=file_id, filename=p.name))
                run_one(p, edges)

        elif gen == "G7":
            for p in md_files:
                text = p.read_text(encoding="utf-8", errors="ignore")
                file_id = f"{sid}:{p.name}"
                edges = []
                edges.extend(extract_g7(text, file_id=file_id))
                edges.extend(extract_g3(text, file_id=file_id, filename=p.name))
                edges.extend(extract_g6(text, file_id=file_id))
                workshop_id = f"data_provenance:{p.relative_to(ROOT).as_posix()}"
                edges.extend(extract_workshop_g7(text, workshop_id=workshop_id))
                run_one(p, edges)
            # workshops/ subdir gets dedicated workshop extraction
            for p in workshop_files:
                text = p.read_text(encoding="utf-8", errors="ignore")
                workshop_id = p.relative_to(ROOT).as_posix()  # data_provenance:<path>
                edges = extract_workshop_g7(text, workshop_id=workshop_id)
                # ALSO run extract_g7 for **Agent**: lines inside workshop bodies
                edges.extend(extract_g7(text, file_id=workshop_id))
                run_one(p, edges)

        stats = {
            "generation": gen,
            "md_file_count": len(md_files),
            "workshop_file_count": len(workshop_files),
            "raw_edges": len(buf.edges),
            "deduped_edges": len(buf.dedup()),
            "per_file_counts": per_file_counts,
        }
        return buf, stats


    # ---------------------------------------------------------------------------
    # Driver
    # ---------------------------------------------------------------------------

    HEADER_TEMPLATE = (
        "## S{sess} Attribution Edges (generated by tools/harvest_attribution_edges.py)\n"
        "## Generated: {timestamp}\n"
        "## Generation: {generation}\n"
        "## Files scanned: {file_count} (+ {workshop_count} in workshops/)\n"
        "## Total edges (deduped): {edge_count}\n"
        "## Spec: sessions/framework/registry/session-format-generations.md\n"
        "## Regex module: tools/_format_generation_regex_set.py (self-test 18/18 PASS)\n"
        "\n"
    )


    def find_session_dirs() -> list[tuple[str, Path]]:
        out: list[tuple[str, Path]] = []
        for top in [ROOT / "sessions", ROOT / "sessions" / "archive"]:
            if not top.exists():
                continue
            for d in sorted(top.glob("session-*")):
                if not d.is_dir():
                    continue
                m = re.match(r"session-(\d+[a-z]?)", d.name)
                if not m:
                    continue
                out.append((m.group(1), d))

        def sk(rec):
            m = re.match(r"(\d+)([a-z]?)", rec[0])
            return (int(m.group(1)) if m else 999, m.group(2) if m else "")
        out.sort(key=sk)
        return out


    def main() -> int:
        ap = argparse.ArgumentParser(description=__doc__)
        ap.add_argument("--dry", action="store_true",
                        help="Preview edges; do not write .txt or .log files.")
        ap.add_argument("--limit", type=int, default=0,
                        help="Limit to first N sessions (0 = all).")
        ap.add_argument("--session", type=str, default="",
                        help="Process a single session (e.g., 86 or 73a).")
        args = ap.parse_args()

        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        sessions = find_session_dirs()
        if args.session:
            sessions = [(s, d) for (s, d) in sessions if s == args.session]
        if args.limit:
            sessions = sessions[:args.limit]

        if not sessions:
            print("No sessions matched.")
            return 0

        # Aggregate counters
        total_raw = 0
        total_deduped = 0
        per_session_count: dict[str, int] = {}
        per_gen_count: Counter = Counter()
        per_edge_type: Counter = Counter()
        per_role: Counter = Counter()
        per_agent: Counter = Counter()
        written_paths: list[Path] = []
        session_stats: dict[str, dict] = {}

        for sid, sess_dir in sessions:
            buf, stats = harvest_session(sid, sess_dir)
            deduped = buf.dedup()
            total_raw += stats["raw_edges"]
            total_deduped += stats["deduped_edges"]
            per_session_count[sid] = stats["deduped_edges"]
            per_gen_count[stats["generation"]] += stats["deduped_edges"]
            for e in deduped:
                per_edge_type[e["type"]] += 1
                # role from comment (extract `role=` tag)
                mr = re.search(r"role=(\w+)", e["comment"])
                if mr:
                    per_role[mr.group(1)] += 1
                # researcher mention
                for side in ("src", "tgt"):
                    if e[f"{side}_type"] == "researchers":
                        per_agent[e[f"{side}_id"]] += 1
            session_stats[sid] = {
                "generation": stats["generation"],
                "md_file_count": stats["md_file_count"],
                "workshop_file_count": stats["workshop_file_count"],
                "deduped_edges": stats["deduped_edges"],
            }

            if args.dry:
                print(f"[dry] S{sid} ({stats['generation']}): "
                      f"{stats['deduped_edges']} edges")
                continue

            if not deduped:
                continue

            out_path = COMPUTATIONS_DIR / f"s{sid}_attribution_edges.txt"
            lines = [HEADER_TEMPLATE.format(
                sess=sid, timestamp=timestamp,
                generation=stats["generation"],
                file_count=stats["md_file_count"],
                workshop_count=stats["workshop_file_count"],
                edge_count=len(deduped),
            )]
            for e in deduped:
                lines.append(
                    f"[EDGE:{e['type']}] "
                    f"{e['src_type']}:{e['src_id']} -> "
                    f"{e['tgt_type']}:{e['tgt_id']}  # {e['comment']}\n"
                )
            out_path.write_text("".join(lines), encoding="utf-8")
            written_paths.append(out_path)

        # Console summary
        print(f"\nAttribution-edge harvest ({timestamp})")
        print(f"  Sessions scanned: {len(sessions)}")
        print(f"  Raw edges:        {total_raw:,}")
        print(f"  Deduped edges:    {total_deduped:,}")
        if not args.dry:
            print(f"  Wrote {len(written_paths)} per-session .txt files at {COMPUTATIONS_DIR}/")
        print(f"\nPer generation:")
        for g in ["G1", "G2", "G3", "G4", "G5", "G6", "G7"]:
            if per_gen_count.get(g):
                print(f"  {g}: {per_gen_count[g]:,} edges")
        print(f"\nPer edge type:")
        for t, c in per_edge_type.most_common():
            print(f"  {t:25} {c:>6,}")
        print(f"\nTop 10 researchers (by edge incidence):")
        for a, c in per_agent.most_common(10):
            print(f"  {a:45} {c:>5}")

        if args.dry:
            return 0

        # Write summary JSON + append run log
        summary = {
            "timestamp": timestamp,
            "regex_module": "tools/_format_generation_regex_set.py",
            "spec": "sessions/framework/registry/session-format-generations.md",
            "sessions_scanned": len(sessions),
            "raw_edges": total_raw,
            "deduped_edges": total_deduped,
            "per_generation": dict(per_gen_count),
            "per_edge_type": dict(per_edge_type),
            "per_role": dict(per_role),
            "per_agent_top20": dict(per_agent.most_common(20)),
            "written_files": [str(p.relative_to(ROOT)).replace("\\", "/")
                              for p in written_paths],
            "session_stats": session_stats,
        }
        OUT_SUMMARY.write_text(json.dumps(summary, ensure_ascii=False, indent=2),
                                encoding="utf-8")

        log_line = (f"{timestamp}  sessions={len(sessions)}  "
                    f"raw={total_raw}  deduped={total_deduped}  "
                    f"files_written={len(written_paths)}\n")
        with OUT_LOG.open("a", encoding="utf-8") as f:
            f.write(log_line)

        print(f"\nWrote {OUT_SUMMARY} ({OUT_SUMMARY.stat().st_size:,}B)")
        print(f"Appended {OUT_LOG}")
        return 0
    main()


# ==========================================================================
# CHAIN-OF-CUSTODY -- lifted from harvest_chain_of_custody_edges.py
# ==========================================================================

def _chain_of_custody_harvester() -> None:
    """Run the chain-of-custody harvester. Lifted from harvest_chain_of_custody_edges.py."""
    SESSIONS_DIR = ROOT / "sessions"
    SESSIONS_ARCHIVE_DIR = SESSIONS_DIR / "archive"
    SESSION_PLAN_DIR = SESSIONS_DIR / "session-plan"
    SESSION_PLAN_ARCHIVE = SESSION_PLAN_DIR / "archive"

    OUT_LOG = HERE / "harvest_chain_of_custody_edges.log"
    OUT_SUMMARY = HERE / "harvest_chain_of_custody_edges.summary.json"


    # ---------------------------------------------------------------------------
    # Edge buffer (mirrors EdgeBuf in harvest_attribution_edges.py:80-139)
    # ---------------------------------------------------------------------------

    class EdgeBuf:
        """Accumulator with idempotent dedup keyed on
        (type, src_type, src_id.lower(), tgt_type, tgt_id.lower())."""

        def __init__(self) -> None:
            self.edges: list[dict] = []

        def add(self, etype: str, src_type: str, src_id: str,
                tgt_type: str, tgt_id: str, comment: str) -> None:
            if not src_id or not tgt_id:
                return
            if src_type == tgt_type and src_id == tgt_id:
                return
            self.edges.append({
                "type": etype,
                "src_type": src_type, "src_id": src_id,
                "tgt_type": tgt_type, "tgt_id": tgt_id,
                "comment": comment[:240],
            })

        def add_coc(self, edge: ChainOfCustodyEdge, source_file: str) -> None:
            """Translate ChainOfCustodyEdge → on-disk edge tuple."""
            # Audit comment: pattern + role + confidence + src file + match snippet
            bits = [edge.pattern]
            if edge.role:
                bits.append(f"role={edge.role}")
            bits.append(f"conf={edge.confidence}")
            bits.append(f"src={source_file}")
            if edge.match_text:
                snippet = re.sub(r"\s+", " ", edge.match_text)[:90]
                bits.append(f"match={snippet!r}")
            comment = " | ".join(bits)
            self.add(edge.edge_type, edge.source_type, edge.source_id,
                     edge.target_type, edge.target_id, comment)

        def dedup(self) -> list[dict]:
            seen: set[tuple] = set()
            out: list[dict] = []
            for e in self.edges:
                key = (e["type"], e["src_type"], e["src_id"].lower(),
                       e["tgt_type"], e["tgt_id"].lower())
                if key in seen:
                    continue
                seen.add(key)
                out.append(e)
            return out


    # ---------------------------------------------------------------------------
    # File discovery
    # ---------------------------------------------------------------------------

    def parse_session_id(name: str) -> str | None:
        """Extract a session id (e.g., '90', '24a', '17b') from a filename or
        directory name. Returns None if no match."""
        m = re.search(r"session-(\d+[a-z]?)", name)
        if m:
            return m.group(1)
        m = re.search(r"^s(\d+[a-z]?)_", name)
        if m:
            return m.group(1)
        return None


    def find_all_session_ids() -> list[str]:
        """Enumerate all session ids from `sessions/session-*` + `sessions/archive/
        session-*` dirs, sorted numerically (with letter suffix preserved)."""
        sids: set[str] = set()
        for top in (SESSIONS_DIR, SESSIONS_ARCHIVE_DIR):
            if not top.exists():
                continue
            for d in top.glob("session-*"):
                if not d.is_dir():
                    continue
                sid = parse_session_id(d.name)
                if sid:
                    sids.add(sid)

        def sk(s: str) -> tuple[int, str]:
            m = re.match(r"(\d+)([a-z]?)", s)
            return (int(m.group(1)) if m else 999, m.group(2) if m else "")

        return sorted(sids, key=sk)


    def find_workingpapers_for_session(sid: str) -> list[Path]:
        """All workingpaper-class files under a session's directory."""
        candidates: list[Path] = []
        for top in (SESSIONS_DIR, SESSIONS_ARCHIVE_DIR):
            d = top / f"session-{sid}"
            if not d.exists():
                continue
            for p in d.rglob("*workingpaper*.md"):
                candidates.append(p)
        return candidates


    def find_verdict_files_for_session(sid: str) -> list[Path]:
        """Per-session verdict files. Canonical location is
        `computations/session-{N}/s{N}*_gate_verdicts.txt` plus the misplaced
        `computations/_shared/s{N}_gate_verdicts.txt` (FORBIDDEN per
        `.claude/rules/gate-verdicts.md` but harvested anyway for completeness)."""
        out: list[Path] = []
        # Canonical location
        d = COMPUTATIONS_DIR / f"session-{sid}"
        if d.exists():
            for p in d.glob(f"s{sid}*_gate_verdicts.txt"):
                out.append(p)
        # Misplaced fallback
        shared = COMPUTATIONS_DIR / "_shared"
        if shared.exists():
            for p in shared.glob(f"s{sid}_gate_verdicts.txt"):
                out.append(p)
        return out


    def find_plan_files_for_session(sid: str) -> list[Path]:
        """All plan files for a session (active + archived)."""
        out: list[Path] = []
        for top in (SESSION_PLAN_DIR, SESSION_PLAN_ARCHIVE):
            if not top.exists():
                continue
            # Match session-{sid}-plan-*.md AND session-{sid}-context.md AND
            # session-{sid}-partition.md AND session-{sid[A-Z]*}-plan-*.md
            for p in top.glob(f"session-{sid}-*.md"):
                if p.is_file():
                    out.append(p)
            # Also handle padded variants like "session-29A-plan-..." for legacy.
            try:
                n = int(re.match(r"(\d+)", sid).group(1))
            except (AttributeError, ValueError):
                n = None
            if n is not None:
                for p in top.glob(f"session-{n:02d}*-plan*.md"):
                    if p.is_file() and p not in out:
                        out.append(p)
                for p in top.glob(f"session-{n}-plan*.md"):
                    if p.is_file() and p not in out:
                        out.append(p)
        return out


    def find_session_md_files(sid: str) -> list[Path]:
        """All .md files under a session's directory (sessions/session-N/** +
        sessions/archive/session-N/**), used for paper-path citation scanning."""
        out: list[Path] = []
        for top in (SESSIONS_DIR, SESSIONS_ARCHIVE_DIR):
            d = top / f"session-{sid}"
            if not d.exists():
                continue
            for p in d.rglob("*.md"):
                if p.is_file():
                    out.append(p)
        return out


    def find_shared_session_files() -> list[Path]:
        """Top-level shared files under `sessions/` not tied to a specific session
        (e.g., observational_avenues.md, evoi-framework.md, permanent-results-
        registry.md). These get scanned for cited_in citations with
        session_id=None (emitted as data_provenance target)."""
        out: list[Path] = []
        if not SESSIONS_DIR.exists():
            return out
        for p in SESSIONS_DIR.glob("*.md"):
            if p.is_file():
                out.append(p)
        framework_dir = SESSIONS_DIR / "framework"
        if framework_dir.exists():
            for p in framework_dir.rglob("*.md"):
                if p.is_file():
                    out.append(p)
        return out


    # ---------------------------------------------------------------------------
    # Per-session harvest
    # ---------------------------------------------------------------------------

    def relpath(p: Path) -> str:
        try:
            return str(p.relative_to(ROOT)).replace("\\", "/")
        except ValueError:
            return str(p).replace("\\", "/")


    def harvest_session(sid: str) -> tuple[EdgeBuf, dict]:
        """Run all 4 chain-of-custody extractors for a single session."""
        buf = EdgeBuf()
        stats: dict = {
            "session_id": sid,
            "workingpapers_scanned": 0,
            "verdict_files_scanned": 0,
            "plan_files_scanned": 0,
            "session_md_files_scanned": 0,
            "edges_by_type": Counter(),
        }

        # 1) carries_forward — workingpapers
        for wp in find_workingpapers_for_session(sid):
            stats["workingpapers_scanned"] += 1
            text = wp.read_text(encoding="utf-8", errors="ignore")
            rel = relpath(wp)
            for e in extract_carry_forwards(text, session_id=sid, source_file=rel):
                buf.add_coc(e, source_file=rel)
                stats["edges_by_type"]["carries_forward"] += 1

        # 2) anchored_in — verdict files
        for vp in find_verdict_files_for_session(sid):
            stats["verdict_files_scanned"] += 1
            text = vp.read_text(encoding="utf-8", errors="ignore")
            rel = relpath(vp)
            for e in extract_anchored_in(text, session_id=sid, source_file=rel):
                buf.add_coc(e, source_file=rel)
                stats["edges_by_type"]["anchored_in"] += 1

        # 3) cited_in — all session-keyed .md files (researchers/Domain/ refs)
        for p in find_session_md_files(sid):
            stats["session_md_files_scanned"] += 1
            text = p.read_text(encoding="utf-8", errors="ignore")
            rel = relpath(p)
            for e in extract_researcher_citations(text, session_id=sid,
                                                  source_file=rel):
                buf.add_coc(e, source_file=rel)
                stats["edges_by_type"]["cited_in"] += 1

        # 4) succ_of — plan files
        for pp in find_plan_files_for_session(sid):
            stats["plan_files_scanned"] += 1
            text = pp.read_text(encoding="utf-8", errors="ignore")
            rel = relpath(pp)
            for e in extract_succ_of(text, source_file=rel):
                buf.add_coc(e, source_file=rel)
                stats["edges_by_type"]["succ_of"] += 1

        return buf, stats


    def harvest_shared_files(buf: EdgeBuf) -> dict:
        """Scan top-level shared session files for paper-path citations.
        These are NOT keyed to a single session, so emitted as
        researchers -> data_provenance:<filepath> edges (session_id=None)."""
        stats: dict = {"shared_files_scanned": 0,
                       "shared_cited_in_edges": 0}
        for p in find_shared_session_files():
            stats["shared_files_scanned"] += 1
            text = p.read_text(encoding="utf-8", errors="ignore")
            rel = relpath(p)
            for e in extract_researcher_citations(text, session_id=None,
                                                  source_file=rel):
                buf.add_coc(e, source_file=rel)
                stats["shared_cited_in_edges"] += 1
        return stats


    # ---------------------------------------------------------------------------
    # Driver
    # ---------------------------------------------------------------------------

    HEADER_TEMPLATE = (
        "## S{sess} Chain-of-Custody Edges "
        "(generated by tools/harvest_chain_of_custody_edges.py)\n"
        "## Generated: {timestamp}\n"
        "## Workingpapers scanned: {wp_count}\n"
        "## Verdict files scanned: {vp_count}\n"
        "## Plan files scanned: {pp_count}\n"
        "## Session .md files scanned (cited_in scope): {md_count}\n"
        "## Total edges (deduped): {edge_count}\n"
        "## Edge types: {edge_types}\n"
        "## Extractors: tools/_chain_of_custody_extractors.py (self-test 11/11 PASS)\n"
        "\n"
    )

    SHARED_HEADER_TEMPLATE = (
        "## Shared-file Chain-of-Custody Edges "
        "(non-session-keyed; emitted to data_provenance targets)\n"
        "## Generated: {timestamp}\n"
        "## Shared files scanned: {n}\n"
        "## Total edges (deduped): {edge_count}\n"
        "## Extractors: tools/_chain_of_custody_extractors.py (self-test 11/11 PASS)\n"
        "\n"
    )


    def main() -> int:
        ap = argparse.ArgumentParser(description=__doc__)
        ap.add_argument("--dry", action="store_true",
                        help="Preview edges; do not write .txt or .log files.")
        ap.add_argument("--limit", type=int, default=0,
                        help="Limit to first N sessions (0 = all).")
        ap.add_argument("--session", type=str, default="",
                        help="Process a single session (e.g., 86 or 73a).")
        ap.add_argument("--no-shared", action="store_true",
                        help="Skip shared-files scan (cited_in via top-level docs).")
        args = ap.parse_args()

        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        all_sids = find_all_session_ids()
        if args.session:
            sids = [s for s in all_sids if s == args.session]
        else:
            sids = all_sids
        if args.limit:
            sids = sids[:args.limit]

        if not sids:
            print("No sessions matched.")
            return 0

        # Aggregate counters
        total_raw = 0
        total_deduped = 0
        per_session_count: dict[str, int] = {}
        per_edge_type: Counter = Counter()
        per_researcher: Counter = Counter()
        written_paths: list[Path] = []
        session_stats: dict[str, dict] = {}

        for sid in sids:
            buf, stats = harvest_session(sid)
            deduped = buf.dedup()
            total_raw += len(buf.edges)
            total_deduped += len(deduped)
            per_session_count[sid] = len(deduped)
            for e in deduped:
                per_edge_type[e["type"]] += 1
                if e["src_type"] == "researchers":
                    per_researcher[e["src_id"]] += 1
                if e["tgt_type"] == "researchers":
                    per_researcher[e["tgt_id"]] += 1
            session_stats[sid] = {
                "workingpapers": stats["workingpapers_scanned"],
                "verdict_files": stats["verdict_files_scanned"],
                "plan_files": stats["plan_files_scanned"],
                "session_md_files": stats["session_md_files_scanned"],
                "edges": len(deduped),
                "by_type": dict(stats["edges_by_type"]),
            }

            if args.dry:
                print(f"[dry] S{sid}: {len(deduped)} edges "
                      f"(wp={stats['workingpapers_scanned']}, "
                      f"vp={stats['verdict_files_scanned']}, "
                      f"pp={stats['plan_files_scanned']}, "
                      f"md={stats['session_md_files_scanned']})")
                continue

            if not deduped:
                continue

            out_path = COMPUTATIONS_DIR / f"s{sid}_chain_of_custody_edges.txt"
            edge_types_str = ",".join(sorted(stats["edges_by_type"].keys()))
            lines = [HEADER_TEMPLATE.format(
                sess=sid, timestamp=timestamp,
                wp_count=stats["workingpapers_scanned"],
                vp_count=stats["verdict_files_scanned"],
                pp_count=stats["plan_files_scanned"],
                md_count=stats["session_md_files_scanned"],
                edge_count=len(deduped),
                edge_types=edge_types_str or "(none)",
            )]
            for e in deduped:
                lines.append(
                    f"[EDGE:{e['type']}] "
                    f"{e['src_type']}:{e['src_id']} -> "
                    f"{e['tgt_type']}:{e['tgt_id']}  # {e['comment']}\n"
                )
            out_path.write_text("".join(lines), encoding="utf-8")
            written_paths.append(out_path)

        # Shared-file pass (non-session-keyed cited_in)
        shared_edges_written = 0
        if not args.no_shared and not args.session:
            sbuf = EdgeBuf()
            sstats = harvest_shared_files(sbuf)
            sdedup = sbuf.dedup()
            total_raw += len(sbuf.edges)
            total_deduped += len(sdedup)
            for e in sdedup:
                per_edge_type[e["type"]] += 1
                if e["src_type"] == "researchers":
                    per_researcher[e["src_id"]] += 1
            if not args.dry and sdedup:
                shared_out = COMPUTATIONS_DIR / "_shared_chain_of_custody_edges.txt"
                sheader = SHARED_HEADER_TEMPLATE.format(
                    timestamp=timestamp,
                    n=sstats["shared_files_scanned"],
                    edge_count=len(sdedup),
                )
                lines = [sheader]
                for e in sdedup:
                    lines.append(
                        f"[EDGE:{e['type']}] "
                        f"{e['src_type']}:{e['src_id']} -> "
                        f"{e['tgt_type']}:{e['tgt_id']}  # {e['comment']}\n"
                    )
                shared_out.write_text("".join(lines), encoding="utf-8")
                written_paths.append(shared_out)
                shared_edges_written = len(sdedup)
            elif args.dry:
                print(f"[dry] shared-files: {len(sdedup)} edges "
                      f"({sstats['shared_files_scanned']} files scanned)")

        # Console summary
        print(f"\nChain-of-custody edge harvest ({timestamp})")
        print(f"  Sessions scanned: {len(sids)}")
        print(f"  Raw edges:        {total_raw:,}")
        print(f"  Deduped edges:    {total_deduped:,}")
        if not args.dry:
            print(f"  Wrote {len(written_paths)} per-session .txt files at {COMPUTATIONS_DIR}/")
            if shared_edges_written:
                print(f"  Wrote 1 shared-files .txt with {shared_edges_written:,} edges")
        print(f"\nPer edge type:")
        for t, c in per_edge_type.most_common():
            print(f"  {t:25} {c:>6,}")
        print(f"\nTop 10 researchers (by cited_in incidence):")
        for r, c in per_researcher.most_common(10):
            print(f"  {r:45} {c:>5}")
        print(f"\nTop 10 sessions (by edge count):")
        top_sess = sorted(per_session_count.items(),
                          key=lambda kv: -kv[1])[:10]
        for s, c in top_sess:
            print(f"  S{s:<5}                                          {c:>5}")

        if args.dry:
            return 0

        # Write summary JSON + append run log
        summary = {
            "timestamp": timestamp,
            "extractor_module": "tools/_chain_of_custody_extractors.py",
            "sessions_scanned": len(sids),
            "raw_edges": total_raw,
            "deduped_edges": total_deduped,
            "per_edge_type": dict(per_edge_type),
            "per_researcher_top20": dict(per_researcher.most_common(20)),
            "written_files": [relpath(p) for p in written_paths],
            "session_stats": session_stats,
            "shared_edges": shared_edges_written,
        }
        OUT_SUMMARY.write_text(json.dumps(summary, ensure_ascii=False, indent=2),
                                encoding="utf-8")

        log_line = (f"{timestamp}  sessions={len(sids)}  "
                    f"raw={total_raw}  deduped={total_deduped}  "
                    f"files_written={len(written_paths)}\n")
        with OUT_LOG.open("a", encoding="utf-8") as f:
            f.write(log_line)

        print(f"\nWrote {OUT_SUMMARY} ({OUT_SUMMARY.stat().st_size:,}B)")
        print(f"Appended {OUT_LOG}")
        return 0
    main()


# ==========================================================================
# PLAN-PIN -- lifted from harvest_plan_pin_edges.py
# ==========================================================================

def _plan_pin_harvester() -> None:
    """Run the plan-pin harvester. Lifted from harvest_plan_pin_edges.py."""
    PLAN_DIRS = [
        (ROOT / "sessions" / "session-plan", "session-*-plan*.md"),
        (ROOT / "sessions" / "session-plan" / "archive", "*.md"),
    ]
    OUTPUT = ROOT / "computations" / "_shared" / "plan_pin_edges.txt"


    # ---------------------------------------------------------------------------
    # 1. Load canonical-constant vocab from canonical_constants.py
    # ---------------------------------------------------------------------------

    def load_canonical_vocab() -> set[str]:
        """Import canonical_constants.py as a module and harvest its public names.

        Returns the set of names that look like physics constants: drop dunders,
        drop names that are obviously imports (modules), and keep identifiers
        that are scalars / arrays / strings / floats.
        """
        spec = importlib.util.spec_from_file_location("canonical_constants", CANONICAL)
        if spec is None or spec.loader is None:
            raise RuntimeError(f"Cannot load {CANONICAL}")
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)

        vocab: set[str] = set()
        for name in dir(mod):
            if name.startswith("_"):
                continue
            val = getattr(mod, name)
            # Skip modules and callables / classes -- only pin real CONSTANTS.
            if callable(val):
                continue
            if type(val).__name__ == "module":
                continue
            # A "constant" name should be at least 2 chars (filters "e", "i" stray)
            # and contain at least one of: underscore, digit, or uppercase.
            if len(name) < 2:
                continue
            if not (any(c.isdigit() for c in name) or "_" in name or any(c.isupper() for c in name)):
                continue
            vocab.add(name)
        return vocab


    # ---------------------------------------------------------------------------
    # 2. Code-block stripper.
    # ---------------------------------------------------------------------------

    CODE_FENCE = re.compile(r"^```")


    def strip_code_blocks(text: str) -> str:
        """Replace lines inside triple-backtick fences with blank lines.

        Preserves line numbering so downstream offsets stay aligned.
        """
        out: list[str] = []
        in_block = False
        for line in text.splitlines():
            if CODE_FENCE.match(line.strip()):
                in_block = not in_block
                out.append("")  # drop fence line
                continue
            out.append("" if in_block else line)
        return "\n".join(out)


    # ---------------------------------------------------------------------------
    # 3. Gate-block detection.
    # ---------------------------------------------------------------------------

    # Gate-ID token: matches things like S85-W1a-SCHEME-DEP, T3-FOO-BAR-1, M-3, V-1.
    # Requires at least one hyphen, starts uppercase or T3-, segments mix letters/digits.
    GATE_ID = re.compile(r"\b((?:T3-)?[A-Z][A-Za-z0-9]*(?:-[A-Za-z0-9]+)+)\b")

    # Heading lines that may anchor a gate block. Three observed forms:
    #   ## §W1a-1. S85-W1a-SCHEME-DEP
    #   ## §W9a-97 — S84-W1-CF-PRU-TOOL
    #   ### W4-43 — Title (GATE-ID)
    HEADING = re.compile(r"^#{1,6}\s+.+$")

    # YAML-block-anchored: a line "gate_id: GATE-ID" inside a YAML mapping.
    YAML_GATE_ID = re.compile(r"^\s*gate_id:\s*['\"]?([^'\"\s#]+)['\"]?\s*(?:#.*)?$")


    def find_gate_blocks(text: str) -> list[tuple[str, int, int]]:
        """Return list of (gate_id, body_start_idx, body_end_idx) over the text.

        A gate block runs from the heading/YAML anchor line to (exclusive) the
        next anchor of either kind, or to EOF.
        """
        lines = text.splitlines()
        anchors: list[tuple[int, str]] = []  # (line_idx, gate_id)

        for i, line in enumerate(lines):
            # YAML-block-anchored.
            m = YAML_GATE_ID.match(line)
            if m:
                gate_id = m.group(1)
                # Confirm matches the gate-ID regex shape (rejects bare names).
                if GATE_ID.fullmatch(gate_id) or "-" in gate_id:
                    anchors.append((i, gate_id))
                    continue
            # Heading-anchored: scan headings for the first gate-ID token.
            if HEADING.match(line):
                mm = GATE_ID.search(line)
                if mm:
                    anchors.append((i, mm.group(1)))

        # Convert anchor indices into char offsets in the joined text.
        # Easier: precompute line start offsets.
        offsets = [0]
        for ln in lines:
            offsets.append(offsets[-1] + len(ln) + 1)  # +1 for the "\n"

        blocks: list[tuple[str, int, int]] = []
        for k, (line_idx, gate_id) in enumerate(anchors):
            start = offsets[line_idx]
            end = offsets[anchors[k + 1][0]] if k + 1 < len(anchors) else len(text)
            blocks.append((gate_id, start, end))
        return blocks


    # ---------------------------------------------------------------------------
    # 4. Pinned-input subsection detection inside a gate body.
    # ---------------------------------------------------------------------------

    # Backtracking fix (2026-05-22): the previous form `[-*#>\s]*\**\s*` had
    # overlapping quantifiers — the character class already includes `*` and
    # whitespace, so the additional `\**\s*` lets the engine redistribute the
    # same consumed characters in many ways, triggering catastrophic
    # backtracking on bullet-heavy lines (S90+ plans go from <0.1s to 18s).
    # Collapsed to a single `[-*#>\s]*`; same match set, ~200x faster.
    PIN_HEADERS = [
        re.compile(r"(?im)^[-*#>\s]*Inputs\s*\(pinned\)\s*[:\*]"),
        re.compile(r"(?im)^[-*#>\s]*machinery[_\- ]pin[_\- ]map\s*[:\*]"),
        re.compile(r"(?im)^[-*#>\s]*Pre[-_ ]registered\s+constants\s*[:\*]"),
        re.compile(r"(?im)^[-*#>\s]*Input\s+SHA[-_ ]?256\s+pins\s*[:\*]"),
        re.compile(r"(?im)^[-*#>\s]*Pinned\s+inputs\s*[:\*]"),
        # Common variant from S84/S85 plans: "**7. Machinery pin (PRDR §0.11)**"
        re.compile(r"(?im)^[-*#>\s]*\d*\.?\s*Machinery\s+pin\b"),
    ]

    # Lines that end a pin section: the next bold-numbered list item, the next
    # top-level YAML key (no leading whitespace, ends with ':'), or another
    # heading.
    SECTION_END_PATTERNS = [
        re.compile(r"^\s*\*\*\d+\.\s"),                # **8. Expected output...
        re.compile(r"^[A-Za-z][A-Za-z0-9_]*:\s*$"),    # top-level YAML key
        re.compile(r"^#{1,6}\s+"),                     # markdown heading
        re.compile(r"^---\s*$"),                       # rule
    ]


    def extract_pin_zone(body: str) -> str:
        """Return the union of pinned-input subsections within a gate body.

        For each known pin header found, take from header line until next
        section-terminator. Concatenate with newlines. May be empty.
        """
        chunks: list[str] = []
        for pat in PIN_HEADERS:
            for m in pat.finditer(body):
                sec_start = m.start()
                # Find the line break that ends the header line.
                line_start = body.rfind("\n", 0, sec_start) + 1
                sec_lines_start = body.find("\n", sec_start)
                if sec_lines_start == -1:
                    chunks.append(body[line_start:])
                    continue
                # Walk forward line-by-line until a section-end pattern hits.
                tail = body[sec_lines_start + 1:]
                tail_lines = tail.splitlines(keepends=True)
                collected: list[str] = []
                for tl in tail_lines:
                    if any(p.match(tl) for p in SECTION_END_PATTERNS):
                        break
                    collected.append(tl)
                chunks.append(body[line_start:sec_lines_start + 1] + "".join(collected))
        return "\n".join(chunks)


    # ---------------------------------------------------------------------------
    # 5. Canonical-name token scanner.
    # ---------------------------------------------------------------------------

    def find_constants(text: str, vocab: set[str]) -> set[str]:
        """Word-boundary scan: return constants from `vocab` that appear in `text`."""
        found: set[str] = set()
        if not text:
            return found
        # Single regex with all vocab terms; sort longest-first so e.g. M_KK
        # is preferred over a shorter prefix when both could match (not strictly
        # necessary with \b but defensive).
        if not vocab:
            return found
        sorted_vocab = sorted(vocab, key=len, reverse=True)
        pattern = re.compile(r"\b(" + "|".join(re.escape(v) for v in sorted_vocab) + r")\b")
        for m in pattern.finditer(text):
            found.add(m.group(1))
        return found


    # ---------------------------------------------------------------------------
    # 6. Per-plan harvest.
    # ---------------------------------------------------------------------------

    def harvest_plan(path: Path, vocab: set[str]) -> tuple[int, dict[str, set[str]]]:
        """Return (gate_block_count, edges_dict[gate_id -> set of constants])."""
        raw = path.read_text(encoding="utf-8", errors="replace")
        text = strip_code_blocks(raw)
        blocks = find_gate_blocks(text)

        edges: dict[str, set[str]] = defaultdict(set)
        for gate_id, start, end in blocks:
            body = text[start:end]
            # Hard zone: declared pin subsections.
            pin_zone = extract_pin_zone(body)
            # Soft zone: first 800 chars of gate-block body (catches prose
            # like "uses M_KK=1.5e16" without a structured pin list).
            soft_zone = body[:800]
            scan_text = pin_zone + "\n" + soft_zone
            consts = find_constants(scan_text, vocab)
            if consts:
                edges[gate_id].update(consts)
        return len(blocks), edges


    # ---------------------------------------------------------------------------
    # 7. Driver.
    # ---------------------------------------------------------------------------

    def main() -> None:
        vocab = load_canonical_vocab()

        plan_files: list[Path] = []
        for d, pat in PLAN_DIRS:
            if d.is_dir():
                plan_files.extend(sorted(d.glob(pat)))
        # Dedup (archive may overlap if symlinks).
        seen: set[Path] = set()
        plan_files = [p for p in plan_files if not (p.resolve() in seen or seen.add(p.resolve()))]

        all_edges: dict[str, set[str]] = defaultdict(set)
        gate_block_total = 0
        plans_zero: list[str] = []

        for path in plan_files:
            gb, edges = harvest_plan(path, vocab)
            gate_block_total += gb
            if not edges:
                plans_zero.append(path.name)
                continue
            for g, cs in edges.items():
                all_edges[g].update(cs)

        # Build the unique edge set. Per (gate, const) pair, exactly one edge.
        edge_lines: list[str] = []
        for gate_id in sorted(all_edges):
            for const in sorted(all_edges[gate_id]):
                edge_lines.append(
                    f"[EDGE:depends_on] gates:{gate_id} -> constants:{const}"
                    f"  # plan-pin or plan-prose mention"
                )

        OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        OUTPUT.write_text(
            "# Auto-generated by tools/harvest_plan_pin_edges.py\n"
            "# Edges: gate -> canonical-constant pinned in session-plan machinery_pin_map\n"
            "# Source: sessions/session-plan/**/*.md\n\n"
            + "\n".join(edge_lines)
            + ("\n" if edge_lines else ""),
            encoding="utf-8",
        )

        # Inbound-degree ranking on constants.
        inbound: dict[str, int] = defaultdict(int)
        for gate_id, cs in all_edges.items():
            for c in cs:
                inbound[c] += 1
        top15 = sorted(inbound.items(), key=lambda kv: (-kv[1], kv[0]))[:15]

        # Report.
        print(f"Plan files scanned:    {len(plan_files)}")
        print(f"Gate blocks detected:  {gate_block_total}")
        print(f"Unique gates with >=1 edge: {len(all_edges)}")
        print(f"Unique edges emitted:  {len(edge_lines)}")
        print(f"Output written to:     {OUTPUT.relative_to(ROOT)}")
        print()
        print("Top 15 constants by inbound degree:")
        for name, deg in top15:
            print(f"  {deg:5d}  {name}")
        print()
        if plans_zero:
            print(f"Plans yielding zero edges ({len(plans_zero)}):")
            for n in plans_zero:
                print(f"  {n}")
        else:
            print("Plans yielding zero edges: (none)")
    main()


# ==========================================================================
# WORKINGPAPER -- lifted from harvest_workingpaper_edges.py
# ==========================================================================

def _workingpaper_harvester() -> None:
    """Run the workingpaper harvester. Lifted from harvest_workingpaper_edges.py."""
    SESSIONS_DIR = PROJECT_ROOT / "sessions"
    CC_PATH = COMPUTATIONS_DIR / "_shared" / "canonical_constants.py"
    OUTPUT_PATH = COMPUTATIONS_DIR / "workingpaper_edges.txt"


    # ----------------------------------------------------------------------------
    # Vocabulary loader — mirrors the pattern in harvest_archive_edges.py
    # ----------------------------------------------------------------------------

    def load_canonical_names() -> set[str]:
        if not CC_PATH.exists():
            return set()
        sys.path.insert(0, str(COMPUTATIONS_DIR / "_shared"))
        try:
            import canonical_constants as CC  # noqa: WPS433
        except Exception:                          # noqa: BLE001
            return set()
        return {n for n in dir(CC) if not n.startswith("_") and n.isidentifier()}


    # ----------------------------------------------------------------------------
    # Regex inventory
    # ----------------------------------------------------------------------------

    # Gate-ID shape: (T3- prefix optional) + leading-cap word + at least one
    # hyphen-segment.  Identical to harvest_archive_edges.RE_GATE_ID.
    RE_GATE_ID_TOKEN = re.compile(
        r"\b((?:T3-)?[A-Z][A-Za-z0-9]*(?:-[A-Za-z0-9]+){1,6})\b"
    )

    # Section headings (## through ####).  We scan the WHOLE heading text for the
    # first gate-ID-shaped token (per spec, the first such token IS the gate ID).
    RE_HEADING = re.compile(r"^(#{2,4})\s+(.+?)\s*$", re.MULTILINE)

    # Fenced code block (triple-backtick), greedy match across newlines.
    RE_FENCED_CODE = re.compile(r"```.*?```", re.DOTALL)

    # Working-paper filename matcher.
    RE_WP_FILE = re.compile(r".*workingpaper\.md$", re.IGNORECASE)

    # Session ID extraction (from path parents).
    RE_SESSION_DIR = re.compile(r"^session-(\d+[a-z]?)$", re.IGNORECASE)


    # ----------------------------------------------------------------------------
    # File discovery
    # ----------------------------------------------------------------------------

    def discover_workingpapers() -> list[Path]:
        """Walk the working-paper corpus.

        Per spec, three glob patterns are unioned:
          sessions/session-*/session-*-results-workingpaper.md
          sessions/session-*/*-workingpaper.md
          sessions/session-*/**/*workingpaper*.md   (recursive)

        Plus the archive subtree for completeness:
          sessions/archive/session-*/**/*workingpaper*.md
        """
        seen: set[Path] = set()
        patterns = [
            "session-*/session-*-results-workingpaper.md",
            "session-*/*-workingpaper.md",
            "session-*/**/*workingpaper*.md",
            "archive/session-*/**/*workingpaper*.md",
        ]
        for pat in patterns:
            for p in SESSIONS_DIR.glob(pat):
                if p.is_file() and RE_WP_FILE.match(p.name):
                    seen.add(p.resolve())
        return sorted(seen)


    def session_id_for(path: Path) -> str | None:
        """Extract session-NN[a-z]? token from any parent dir; return digit-prefix
        portion (without sub-letter suffix to align with edge-target convention)."""
        for parent in path.parents:
            m = RE_SESSION_DIR.match(parent.name)
            if m:
                sess = m.group(1)
                m2 = re.match(r"^(\d+)", sess)
                return (m2.group(1) if m2 else sess)
        return None


    # ----------------------------------------------------------------------------
    # Section splitter
    # ----------------------------------------------------------------------------

    def strip_code_blocks(text: str) -> str:
        """Replace fenced code blocks with blank lines preserving line-count
        so heading offsets stay valid downstream."""
        def _blank(m: re.Match[str]) -> str:
            return "\n" * m.group(0).count("\n")
        return RE_FENCED_CODE.sub(_blank, text)


    def find_gate_sections(text: str) -> list[tuple[str, str]]:
        """Return [(gate_id, body_text), ...] for each gate-section in the file.

        A gate-section is any markdown heading (level 2-4) whose heading text
        contains at least one gate-ID-shaped token.  The first such token IS
        the gate ID for that section.  Body extends from the heading line to
        the next heading at SAME or HIGHER level (smaller-or-equal '#' count).
        Headings without a gate-ID token are skipped (no filename fallback).
        """
        matches = list(RE_HEADING.finditer(text))
        out: list[tuple[str, str]] = []
        for i, m in enumerate(matches):
            level = len(m.group(1))            # 2..4
            head_text = m.group(2)
            # Find the first gate-ID-shaped token in the heading.
            gid_match = RE_GATE_ID_TOKEN.search(head_text)
            if not gid_match:
                continue
            gate_id = gid_match.group(1)
            # Body ends at next heading whose level <= this one.
            body_start = m.end()
            body_end = len(text)
            for m2 in matches[i + 1:]:
                if len(m2.group(1)) <= level:
                    body_end = m2.start()
                    break
            body = text[body_start:body_end]
            out.append((gate_id, body))
        return out


    # ----------------------------------------------------------------------------
    # Edge harvesting
    # ----------------------------------------------------------------------------

    def harvest_pairs(
        paths: list[Path], canonical_names: set[str],
    ) -> tuple[list[dict], dict[str, int], set[str]]:
        """Walk every working-paper file and emit (gate, constant) pairs.

        Returns:
          edges          — list of edge dicts, deduped across the whole corpus.
          sections_per_session — map session-id -> count of gate-sections detected.
          sessions_zero_edges  — set of session ids whose WP files yielded ZERO
                                 edges (reported as "unexpected" anomalies).
        """
        seen_pairs: set[tuple[str, str]] = set()
        edges: list[dict] = []
        sections_per_session: dict[str, int] = {}
        edges_per_session: dict[str, int] = {}
        sessions_seen: set[str] = set()

        n_sections_total = 0

        for p in paths:
            sess = session_id_for(p) or "?"
            sessions_seen.add(sess)
            try:
                raw = p.read_text(encoding="utf-8", errors="replace")
            except Exception:                  # noqa: BLE001
                continue
            text = strip_code_blocks(raw)

            sections = find_gate_sections(text)
            sections_per_session[sess] = (
                sections_per_session.get(sess, 0) + len(sections)
            )
            n_sections_total += len(sections)

            # Pre-locate which file/section each pair came from for the comment.
            for gate_id, body in sections:
                # Scan the section body for canonical-constant-name tokens.
                # Strict word-boundary match using the constant's own name as
                # the regex literal (re.escape).  This avoids the false-positive
                # of "M" matching inside "M_KK"; we want exact-token matches.
                #
                # Optimization: tokenize once, then membership-check.
                tokens = set(re.findall(r"\b[A-Za-z_][A-Za-z0-9_]*\b", body))
                hits = tokens & canonical_names
                if not hits:
                    continue
                for const in sorted(hits):
                    key = (gate_id, const)
                    if key in seen_pairs:
                        continue
                    seen_pairs.add(key)
                    edges.append({
                        "type": "reproduces",
                        "src_type": "gates",
                        "src_id": gate_id,
                        "tgt_type": "constants",
                        "tgt_id": const,
                        "comment": (
                            f"WP-harvested: section §{gate_id} body cites "
                            f"{const} (s{sess})"
                        ),
                    })
                    edges_per_session[sess] = edges_per_session.get(sess, 0) + 1

        sessions_zero = {
            s for s in sessions_seen
            if edges_per_session.get(s, 0) == 0
        }

        # Report total sections via sentinel so the driver can include in summary.
        sections_per_session["__TOTAL__"] = n_sections_total
        return edges, sections_per_session, sessions_zero


    # ----------------------------------------------------------------------------
    # Output writer
    # ----------------------------------------------------------------------------

    HEADER_TEMPLATE = (
        "## Working-Paper Edges (generated by tools/harvest_workingpaper_edges.py)\n"
        "## Source: sessions/session-*/*workingpaper*.md (recursive,\n"
        "##         including sessions/archive/).\n"
        "## Conservative-harvest discipline: prefer miss over false-positive\n"
        "## (per computations/_shared/_harvest_edges.py:12-14).\n"
        "## Pairs deduped across the whole corpus (one (gate, constant) per pair).\n"
        "\n"
    )


    def write_edges(edges: list[dict], path: Path) -> None:
        lines: list[str] = [HEADER_TEMPLATE]
        for e in sorted(edges, key=lambda x: (x["src_id"], x["tgt_id"])):
            lines.append(
                f"[EDGE:{e['type']}] "
                f"{e['src_type']}:{e['src_id']} -> "
                f"{e['tgt_type']}:{e['tgt_id']}  # {e['comment']}\n"
            )
        path.write_text("".join(lines), encoding="utf-8")


    # ----------------------------------------------------------------------------
    # Driver
    # ----------------------------------------------------------------------------

    def main() -> int:
        ap = argparse.ArgumentParser(description=__doc__)
        ap.add_argument(
            "--dry", action="store_true",
            help="Preview edges only; do not write output file.",
        )
        args = ap.parse_args()

        canonical_names = load_canonical_names()
        if not canonical_names:
            print("ERROR: failed to load canonical_constants vocab.")
            return 2

        paths = discover_workingpapers()
        if not paths:
            print("No working-paper files discovered.")
            return 0

        edges, sections_per_session, sessions_zero = harvest_pairs(
            paths, canonical_names,
        )

        n_total_sections = sections_per_session.pop("__TOTAL__", 0)

        if not args.dry:
            write_edges(edges, OUTPUT_PATH)

        # ----------------- Reporting -----------------
        print(f"WP files scanned       : {len(paths)}")
        print(f"Gate-sections detected : {n_total_sections}")
        print(f"Unique edges emitted   : {len(edges)}")

        if not args.dry:
            print(f"Output                 : {OUTPUT_PATH}")
        else:
            print("[dry] no output written.")

        # Top 15 constants by inbound degree.
        inbound: dict[str, int] = {}
        for e in edges:
            inbound[e["tgt_id"]] = inbound.get(e["tgt_id"], 0) + 1
        top = sorted(inbound.items(), key=lambda x: (-x[1], x[0]))[:15]
        print("\nTop 15 constants by inbound degree:")
        for name, deg in top:
            print(f"  {deg:5d}  {name}")

        if sessions_zero:
            zsorted = sorted(
                sessions_zero,
                key=lambda s: (int(s) if s.isdigit() else 99999, s),
            )
            print(f"\nSessions yielding ZERO edges (unexpected): "
                  f"{', '.join(zsorted)}")
        else:
            print("\nSessions yielding ZERO edges: (none)")

        return 0
    main()


# ==========================================================================
# SCRIPT-IMPORT -- lifted from harvest_script_import_edges.py
# ==========================================================================

def _script_import_harvester() -> None:
    """Run the script-import harvester. Lifted from harvest_script_import_edges.py."""
    OUTFILE = COMPUTATIONS / "script_import_edges.txt"

    # Load canonical-constants vocab. Filter out re-exported modules / functions
    # / classes (e.g. numpy aliased as np, sys, warnings, helper functions like
    # warn_stale) — those are not framework constants.
    sys.path.insert(0, str(COMPUTATIONS))
    import canonical_constants as CC  # noqa: E402

    _CALLABLE_OR_MODULE = (
        types.ModuleType,
        types.FunctionType,
        types.BuiltinFunctionType,
        type,
    )
    VOCAB = {
        n
        for n in dir(CC)
        if not n.startswith("_")
        and n.isidentifier()
        and not isinstance(getattr(CC, n), _CALLABLE_OR_MODULE)
    }

    SCRIPT_NAME_RE = re.compile(r"^s\d+[a-z]?_")
    TOKEN_RE = re.compile(r"\b[A-Za-z_]\w*\b")


    def strip_strings_and_comments(src: str) -> str:
        """Remove triple-quoted strings, single-line strings, and # comments.

        Conservative: replaces them with spaces so line/column structure roughly
        survives but their textual contents are gone.
        """
        # Triple-quoted strings (greedy-safe, non-greedy body).
        src = re.sub(r'"""[\s\S]*?"""', " ", src)
        src = re.sub(r"'''[\s\S]*?'''", " ", src)
        # Single-line strings ('..' and "..") — handle escapes minimally.
        src = re.sub(r'"(?:\\.|[^"\\\n])*"', " ", src)
        src = re.sub(r"'(?:\\.|[^'\\\n])*'", " ", src)
        # `#` comments to end-of-line.
        src = re.sub(r"#[^\n]*", " ", src)
        return src


    # Match `from canonical_constants import ...` allowing parens + multi-line.
    IMPORT_RE = re.compile(
        r"from\s+canonical_constants\s+import\s+(\*|\([\s\S]*?\)|[^\n;()]+)",
        re.MULTILINE,
    )


    def parse_imports(clean_src: str) -> tuple[set[str], bool]:
        """Return (explicit_names, has_star_import)."""
        names: set[str] = set()
        has_star = False
        for m in IMPORT_RE.finditer(clean_src):
            body = m.group(1).strip()
            if body == "*":
                has_star = True
                continue
            # Strip surrounding parens.
            if body.startswith("(") and body.endswith(")"):
                body = body[1:-1]
            # Split on commas, then strip "as" aliases — we want the source name.
            for piece in body.split(","):
                piece = piece.strip()
                if not piece:
                    continue
                # Handle `Name as Alias` — keep the source name (canonical side).
                piece = re.split(r"\s+as\s+", piece, maxsplit=1)[0].strip()
                if piece.isidentifier():
                    names.add(piece)
        return names, has_star


    def harvest_script(path: Path) -> set[str]:
        """Return the set of canonical-constant names this script depends on."""
        raw = path.read_text(encoding="utf-8", errors="replace")
        clean = strip_strings_and_comments(raw)

        explicit, has_star = parse_imports(clean)
        found = {n for n in explicit if n in VOCAB}

        if has_star:
            # Scan body tokens; anything in vocab is a referenced constant.
            for tok in TOKEN_RE.findall(clean):
                if tok in VOCAB:
                    found.add(tok)
        return found


    def main() -> int:
        scripts = sorted(COMPUTATIONS.glob("s*.py"))
        edges: dict[str, set[str]] = defaultdict(set)
        errors: list[tuple[str, str]] = []
        inbound: Counter[str] = Counter()
        scanned = 0
        skipped_name = 0

        for path in scripts:
            name = path.name
            if not SCRIPT_NAME_RE.match(name):
                skipped_name += 1
                continue
            if name == "canonical_constants.py" or name == "__init__.py":
                continue
            try:
                consts = harvest_script(path)
            except Exception as exc:  # pragma: no cover - reported below
                errors.append((name, f"{type(exc).__name__}: {exc}"))
                continue
            scanned += 1
            for c in consts:
                edges[name].add(c)
                inbound[c] += 1

        # Emit.
        lines = [
            "## Script Constant-Import Edges",
            "## Generated by tools/harvest_script_import_edges.py",
            "## Source: computations/_shared/s*.py imports of canonical_constants",
            "## Edge type: data_provenance -> constants (depends_on)",
            "",
        ]
        total_edges = 0
        for script in sorted(edges):
            for const in sorted(edges[script]):
                lines.append(
                    f"[EDGE:depends_on] data_provenance:{script} "
                    f"-> constants:{const}  # script imports {const}"
                )
                total_edges += 1

        OUTFILE.write_text("\n".join(lines) + "\n", encoding="utf-8")

        # Report.
        print(f"scripts scanned : {scanned}")
        print(f"scripts skipped (name pattern) : {skipped_name}")
        print(f"unique edges emitted : {total_edges}")
        print(f"output : {OUTFILE.relative_to(ROOT)}")
        print()
        print("Top 15 constants by inbound degree:")
        for const, count in inbound.most_common(15):
            print(f"  {count:4d}  {const}")
        print()
        if errors:
            print(f"Parse errors ({len(errors)}):")
            for name, err in errors:
                print(f"  {name} : {err}")
        else:
            print("Parse errors: none")
        return 0
    main()


# ==========================================================================
# ARCHIVE-SCRIPT-IMPORT -- lifted from harvest_archive_script_import_edges.py
# ==========================================================================

def _archive_script_import_harvester() -> None:
    """Run the archive-script-import harvester. Lifted from harvest_archive_script_import_edges.py."""
    OUTPUT = ROOT / "computations" / "_shared" / "archive_script_import_edges.txt"


    def load_vocab() -> set[str]:
        """Import canonical_constants.py and extract public identifier names.

        Filters out re-exported modules / functions / classes / built-ins so that
        names like `np`, `sys`, `warnings`, `warn_stale` do not pollute the
        constant vocabulary. Mirrors the filter pattern in harvest_archive_edges.py
        `load_canonical_names`. The unfiltered form leaks badly here because this
        is a source-text harvester (every `import numpy as np` line hits `np`).
        """
        import inspect
        import types
        spec = importlib.util.spec_from_file_location("canonical_constants", CANONICAL)
        if spec is None or spec.loader is None:
            raise RuntimeError(f"could not load spec for {CANONICAL}")
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        out: set[str] = set()
        for name in dir(mod):
            if name.startswith("_") or not name.isidentifier():
                continue
            obj = getattr(mod, name)
            if isinstance(obj, types.ModuleType):
                continue
            if (inspect.isfunction(obj) or inspect.isclass(obj)
                    or inspect.isbuiltin(obj) or inspect.ismethod(obj)):
                continue
            out.add(name)
        return out


    # Strip triple-quoted strings (docstrings + multi-line strings) and # comments.
    _TRIPLE_RE = re.compile(r'("""|\'\'\')(?:.|\n)*?\1', re.MULTILINE)
    _LINE_COMMENT_RE = re.compile(r"#.*?$", re.MULTILINE)
    _SINGLE_QUOTED_RE = re.compile(r"'([^'\\\n]|\\.)*'")
    _DOUBLE_QUOTED_RE = re.compile(r'"([^"\\\n]|\\.)*"')
    _TOKEN_RE = re.compile(r"\b[A-Za-z_][A-Za-z0-9_]*\b")


    def strip_source(src: str) -> str:
        """Remove docstrings, comments, and string literals so token search hits real identifiers."""
        src = _TRIPLE_RE.sub(" ", src)
        src = _LINE_COMMENT_RE.sub(" ", src)
        src = _SINGLE_QUOTED_RE.sub(" ", src)
        src = _DOUBLE_QUOTED_RE.sub(" ", src)
        return src


    def is_skipped(path: Path) -> bool:
        name = path.name
        if name == "canonical_constants.py":
            return True
        if name == "__init__.py":
            return True
        if name.startswith("_"):
            return True
        return False


    def main() -> int:
        vocab = load_vocab()
        print(f"[harvest] vocab size: {len(vocab)}", file=sys.stderr)

        if not ARCHIVE.is_dir():
            print(f"[harvest] ERROR: archive not found at {ARCHIVE}", file=sys.stderr)
            return 1

        edges: set[tuple[str, str]] = set()
        inbound_degree: dict[str, int] = {}
        scanned = 0
        errored: list[tuple[str, str]] = []

        for py in ARCHIVE.rglob("*.py"):
            if is_skipped(py):
                continue
            scanned += 1
            try:
                src = py.read_text(encoding="utf-8", errors="replace")
            except Exception as exc:  # noqa: BLE001
                errored.append((str(py), repr(exc)))
                continue
            try:
                stripped = strip_source(src)
                tokens = set(_TOKEN_RE.findall(stripped))
            except Exception as exc:  # noqa: BLE001
                errored.append((str(py), repr(exc)))
                continue

            hits = tokens & vocab
            if not hits:
                continue
            bare = py.name
            for c in hits:
                edge = (bare, c)
                if edge in edges:
                    continue
                edges.add(edge)
                inbound_degree[c] = inbound_degree.get(c, 0) + 1

        # Write output.
        OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        with OUTPUT.open("w", encoding="utf-8") as f:
            f.write("# archive_script_import_edges.txt\n")
            f.write(f"# Generated by tools/harvest_archive_script_import_edges.py\n")
            f.write(f"# Scanned {scanned} archive scripts; emitted {len(edges)} unique edges.\n")
            f.write("# Edge format: [EDGE:depends_on] data_provenance:<script>.py -> constants:<NAME>  # archive-script uses <NAME>\n")
            f.write("#\n")
            for bare, c in sorted(edges):
                f.write(
                    f"[EDGE:depends_on] data_provenance:{bare} -> constants:{c}"
                    f"  # archive-script uses {c}\n"
                )

        # Report.
        print(f"[harvest] scanned: {scanned}", file=sys.stderr)
        print(f"[harvest] unique edges: {len(edges)}", file=sys.stderr)
        top = sorted(inbound_degree.items(), key=lambda kv: (-kv[1], kv[0]))[:15]
        print("[harvest] top 15 constants by inbound degree:", file=sys.stderr)
        for name, deg in top:
            print(f"  {deg:>5d}  {name}", file=sys.stderr)
        print(f"[harvest] errored files: {len(errored)}", file=sys.stderr)
        for path, exc in errored[:25]:
            print(f"  ERROR  {path}  {exc}", file=sys.stderr)

        print(f"[harvest] wrote {OUTPUT}", file=sys.stderr)
        return 0
    main()

# ---------------------------------------------------------------------------
# CLI dispatcher
# ---------------------------------------------------------------------------

SUBCMDS = {
    "archive":               _archive_harvester,
    "provenance":            _provenance_harvester,
    "theorem-closure":       _theorem_closure_harvester,
    "equation":              _equation_harvester,
    "attribution":           _attribution_harvester,
    "chain-of-custody":      _chain_of_custody_harvester,
    "plan-pin":              _plan_pin_harvester,
    "workingpaper":          _workingpaper_harvester,
    "script-import":         _script_import_harvester,
    "archive-script-import": _archive_script_import_harvester,
}


def main_dispatch() -> None:
    parser = argparse.ArgumentParser(
        prog="harvester.py",
        description="Edge harvesters for the knowledge index.",
    )
    sub = parser.add_subparsers(dest="cmd", required=True)
    for name in SUBCMDS:
        sub.add_parser(name)
    args, _extra = parser.parse_known_args()
    # Each closure invokes its own argparse on sys.argv, so reset sys.argv to
    # only what the inner main() expects (drop the harvester.py + subcommand
    # tokens, keep any pass-through flags).
    inner_argv = [f"harvester.py {args.cmd}"] + _extra
    saved_argv = sys.argv
    sys.argv = inner_argv
    try:
        SUBCMDS[args.cmd]()
    finally:
        sys.argv = saved_argv


if __name__ == "__main__":
    main_dispatch()
