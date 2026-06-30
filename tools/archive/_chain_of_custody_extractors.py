#!/usr/bin/env python3
"""Chain-of-custody edge extractors (Phase 1.1).

Sister module to `tools/_format_generation_regex_set.py` (which extracts
researcher-side authorship). THIS module extracts GATE-side chain-of-custody:
carry-forwards from workingpapers, gate→session anchoring from verdict files,
researcher-paper citations in framework files, and within-wave gate adjacency
from plan files.

Edge types emitted:
  - carries_forward: sessions:N -> gates:CF-X
      Source: workingpaper `## Carry-Forward Computations` sections, with
              `### CF-{ID}` headings followed by 4-field `| Field | Spec |`
              tables (modern format) OR 7-bullet Action Items (legacy format).
      Verified: sessions/session-90/session-90-w2-workingpaper.md:1972-1990

  - anchored_in: gates:G -> sessions:N
      Source: `computations/session-{N}/s{N}*_gate_verdicts.txt` files.
              S81+ canonical format `{GATE-ID}: PASS|FAIL|INFO -- value=...`
              pre-S81 legacy format `GATE {GATE-ID}: {status}`.
      Verified: computations/session-90/s90_gate_verdicts.txt:1 +
                computations/session-24/s24a_gate_verdicts.txt:10

  - cited_in: researchers:R -> sessions:N  (REVISED from Phase 1 spec)
      Source: ANY framework file (sessions, registries, agent memory) that
              references a paper path `researchers/<Domain>/<paper>.md`.
              Researcher canonical ID derived from <Domain> via mapping.
      Verified: sessions/observational_avenues.md:64 (3 distinct researcher
                paths cited); sessions/session-62/session-62-vdd-tesla-
                workshop.md:35 + 86 + 577 (Van-den-Dungen citations).

  - succ_of: gates:G_next -> gates:G_prev
      Source: plan-file `## §W{w}-{n}.` headings in order of appearance.
              Within a single plan file, adjacent §W{w}-{n} headings produce
              succ_of(next → prev) edges, capturing pre-registered dispatch
              ordering.
      Verified: sessions/session-plan/session-90-plan-w2.md:67/195/336/440/553
                (§W2-1 through §W2-5 sequential gate IDs);
                sessions/session-plan/archive/session-88-plan-w7c.md (different
                heading format ## §W7c-{N} backtick GATE-ID backtick).

Discipline (per `_harvest_edges.py:12-14`): prefer miss over false-positive.
Each emission requires regex match + non-ambiguous src/tgt mapping.

Run `python tools/_chain_of_custody_extractors.py --self-test` to verify each
pattern against verbatim fixtures from real session/plan/verdict files.
"""
from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Optional, Tuple

ROOT = Path(__file__).resolve().parent.parent
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


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        sys.exit(run_self_test())
    print(f"RESEARCHER_DIR_TO_AGENT entries: {len(RESEARCHER_DIR_TO_AGENT)}")
    print(f"FIXTURES: {len(FIXTURES)}")
    print(f"Run with --self-test to verify pattern coverage.")
