#!/usr/bin/env python3
"""
Knowledge Index Extractor for the Phonon-Exflation Project.

Walks sessions/ and computations/_shared/, extracts entities
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
FRAMEWORK_DIR = SESSIONS_DIR / "framework"
COMPUTATIONS_DIR = PROJECT_ROOT / "computations"
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
# computation-archive deleted at Phase 5 cutover (2026-05-03); set to non-existent
# sentinel so .exists() checks return False and iteration over the dir yields
# empty. Archive content was integrated into computations/session-N/ and
# computations/_shared/ during Phase 2a mirror.
COMPUTATIONS_ARCHIVE_DIR = PROJECT_ROOT / "_deleted_computations_archive_sentinel_"
# canonical_constants.py lives in computations/_shared/ post-Phase-3.
CANONICAL_CONSTANTS_PATH = SHARED_DIR / "canonical_constants.py"
INDEX_PATH = PROJECT_ROOT / "tools" / "knowledge-index.json"

# File priority (higher = more authoritative, processed later so they win dedup)
# NB: sessions/framework/*.md overrides these via _is_framework_file() → priority 7.
PRIORITY_PATTERNS = [
    (4, re.compile(r".*synthesis.*\.md$", re.IGNORECASE)),
    (5, re.compile(r".*sagan-verdict.*\.md$", re.IGNORECASE)),
    (3, re.compile(r".*gate_verdicts.*\.txt$", re.IGNORECASE)),
    (2, re.compile(r".*\.txt$")),   # other computation .txt output files
    (2, re.compile(r".*\.md$")),    # other session minutes
]

# Priority assigned to any file under sessions/framework/. Beats synthesis (4)
# and sagan-verdict (5) so that capstone-registry entries win dedup over
# session-minute extractions of the same-named entity. See extract_framework_registry().
FRAMEWORK_PRIORITY = 7


def _is_framework_file(filepath: Path) -> bool:
    """True if filepath lives under sessions/framework/ (the capstone registry)."""
    try:
        filepath.resolve().relative_to(FRAMEWORK_DIR.resolve())
        return True
    except (ValueError, FileNotFoundError):
        return False


def get_priority(filepath: Path) -> int:
    """Return processing priority for a file (higher = more authoritative)."""
    if _is_framework_file(filepath):
        return FRAMEWORK_PRIORITY
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
        # Match computation file references or sessions references
        for fm in re.finditer(r"(?:computations|computation-archive|sessions)/\S+", line):
            files.append(fm.group(0))
        # Match s{session}_*.{ext} patterns
        for fm in re.finditer(r"s\d+[a-z]?_\w+\.\w+", line):
            files.append(fm.group(0))

    # Deduplicate files list
    files = list(OrderedDict.fromkeys(files))

    # Normalize session ID to lowercase. Edges use bare numeric form
    # ('17a', '88') after the strip-S-prefix normalization; if the
    # extracted session ID is uppercase (e.g. '73B' or '29A'), set
    # intersection with edge IDs fails. Lowercasing makes the canonical
    # form match.
    if session_id:
        session_id = session_id.lower()
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

# Markdown structural language that the bullet/table extractors mistake for
# entity names. These are section labels, framing nouns, and metadata-prefixed
# lines that appear under PROVEN/CLOSED headers but do not name a theorem,
# mechanism, or gate. Without this filter, lines like "**Effort**: 2 hours,
# 1 agent session" and section subheadings like "Closed Mechanisms" are
# harvested as PROVEN+CLOSED entities, producing the spurious overlap warnings
# documented as the "endemic structural-language" parser bug.
_STRUCTURAL_LANGUAGE_WORDS = frozenset({
    # Single generic nouns appearing as section labels under PROVEN/CLOSED
    "correction", "retraction", "erratum", "downgrade", "factor", "sector",
    "summary", "overview", "context", "background", "discussion",
    "introduction", "conclusion", "appendix", "remark", "annotation",
    "footnote", "preamble", "rationale",
    # Multi-word section labels seen in the corpus
    "hard closes fired", "structural walls", "surviving channels",
    "closed mechanisms", "proven mathematical results",
    "uncomputed decisive tests", "open questions", "follow-ups",
    "next session", "carry forward", "carry-forward",
    "key results", "main findings", "headline results",
    "session metadata", "session summary",
    # Catalog/status framing labels (not entity names)
    "four-class integrity failure catalog",
    "multi-band bootstrap closed permanently",
})

_METADATA_PREFIXES = (
    "effort:", "session:", "agents:", "agent:", "date:",
    "summary:", "verdict:", "status:", "input:", "output:",
    "file:", "files:", "sha:", "hash:", "ref:", "reference:",
    "origin:", "target:", "co-author:", "author:",
)


def _is_structural_language(name: str) -> bool:
    """True if `name` is markdown structural language (section labels,
    metadata prefixes, generic English nouns) rather than a real entity name.

    The bullet/table extractors pick up any bulleted item under a PROVEN/
    CLOSED header. Markdown documents legitimately contain bullets that
    frame structure ("Closed Mechanisms", "Surviving Channels") or record
    metadata ("Effort: 2 hours, 1 agent session"). These are not entity
    names, but the bullet heuristic produces them.

    The filter checks two layers: an explicit blacklist of words and phrases
    that recur in this codebase as section labels, and a metadata-prefix
    sniff that catches lines beginning with `effort:`, `session:`, etc.
    """
    if not name:
        return True
    # Strip ALL Markdown emphasis markers (** _ etc.) anywhere in the string,
    # not just at the edges — they appear mid-string in entries like
    # `**Effort**: 2 hours...` and `four-class integrity failure catalog**`.
    n = re.sub(r"[\*_]+", "", name).lower().strip().rstrip(".:").strip()
    if n in _STRUCTURAL_LANGUAGE_WORDS:
        return True
    for prefix in _METADATA_PREFIXES:
        if n.startswith(prefix):
            return True
    # Also catch lines whose stripped form starts with a structural label
    # followed by parenthetical/bracket noise (e.g., "four-class ... (P1-3)")
    for label in _STRUCTURAL_LANGUAGE_WORDS:
        if " " in label and n.startswith(label):
            return True
    return False

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


def _is_plan_file(filepath: Path) -> bool:
    """True for session-plan/ files. Plans contain pre-registered criteria
    ('proposed theorem', 'hypothesized closure', 'open question list')
    which are NOT executed results — they should not land in theorems,
    closed_mechanisms, open_channels, or gates tables. Only results /
    synthesis / handoff documents carry real entity rows.

    S81 audit: before this filter, 88 theorems + 55 closed_mechanisms +
    106 open_channels + 226 gates = 475 ghost entities across 4 tables.
    """
    path_str = str(filepath).replace("\\", "/").lower()
    return "/session-plan/" in path_str or "sessions/session-plan/" in path_str


def extract_proven_theorems(filepath: Path, text: str) -> list[dict]:
    """Extract PROVEN theorems from a synthesis file."""
    if _is_plan_file(filepath):
        return []
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
            if name.startswith(":") or name.startswith("|") or len(name) < 4:
                continue
            # Skip generic table headers that are not entity names
            if name.lower() in _TABLE_HEADER_WORDS:
                continue
            # Skip markdown structural language (section labels, metadata)
            if _is_structural_language(name):
                continue
            # S90 cleanup: reject noise patterns same as closed_mechanisms
            # legacy parser cleanup. (a) digit-leading names — almost
            # always table-data values mis-parsed as theorem rows;
            # (b) x-digit prefix ("x0.44" from "× 0.44" parsing); (c)
            # name longer than 200 chars (prose, not entity name);
            # (d) sentence-shape ending in period; (e) name starts with
            # code/bold markdown.
            if re.match(r"^\s*[-+]?\d", name):
                continue
            if re.match(r"^\s*x\d", name):
                continue
            if len(name) > 200:
                continue
            if name.rstrip().endswith("."):
                continue
            if name.startswith("`") or name.startswith("**"):
                continue
            # Reject malformed session fields — same strict pattern as
            # closed_mechanisms uses. session must look like SXX/SXXa/
            # Session N pattern, OR be empty (some real theorems span
            # multi-session ranges in their text).
            if sessions:
                sm = re.match(r"^(S?\d+[a-z]?|Session\s+\d+)\b", sessions)
                if not sm:
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
                # Skip markdown structural language (section labels, metadata)
                if _is_structural_language(content[:120]):
                    continue
                # S90 cleanup: same noise filters as Strategy 1.
                _name120 = content[:120]
                if len(_name120) < 4:
                    continue
                if re.match(r"^\s*[-+]?\d", _name120):
                    continue
                if re.match(r"^\s*x\d", _name120):
                    continue
                if _name120.rstrip().endswith("."):
                    continue
                if _name120.startswith("`") or _name120.startswith("**"):
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
    r"|(?:Kill|Constraint)(?:ed)?\s+(?:Gate\s+)?"
    r"(?:Registry|Table|Chain|Condition|Map(?:\s+Updates)?)"  # S91: +Map
    r"|Complete\s+(?:Kill|Closure)"
    r"|(?:Dead|Closed)\s+Mechanism"
    r"|What\s+is\s+(?:NOT\s+)?(?:killed|closed)"
    r"|ALL\s+(?:DEAD|CLOSED)"
    r"|Definitive\s+(?:Kill|Closure)"
    r"|Perturbative\s+(?:Gates|Mechanisms)"
    r"|UPDATED\s+(?:KILL|CONSTRAINT)"
    r"|Summary\s+Table"                         # S91: post-S43 OOM / gap-report tables
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


# ---------------------------------------------------------------------------
# Non-closure source filter (S89 cleanup)
#
# Documents that are NOT closure registries but were caught by the legacy
# bullet/table heuristics. Each emits NO rows from extract_closed_mechanisms.
# Entity types these documents DO contain (walls, doors, windows, retractions,
# bulletins, falsifiers, methodology rules, etc.) need their own extractors;
# they belong here under their own bucket, not under closed_mechanisms.
# ---------------------------------------------------------------------------

_NON_CLOSURE_SOURCE_MARKERS = (
    # Atlas docs are closure SUMMARIES, not closure sources.
    # Closures live in per-session WPs / synthesis docs
    # (S91 cmap retrofit). atlas-02 was previously special-cased
    # as the 'canonical closure inventory'; that mapping was reverted
    # 2026-05-19 because Atlas docs are downstream summaries.
    "atlas/atlas-00-index",
    "atlas/atlas-01-session-timeline",
    "atlas/atlas-02-mechanism-lifecycle",
    "atlas/atlas-03-equation-flow",
    "atlas/atlas-04-assumptions",
    "atlas/atlas-05-walls-doors-windows",
    "atlas/atlas-06-probability-trajectory",
    "atlas/atlas-07-permanent-results",
    "atlas/atlas-08-open-questions",
    "atlas/atlas-09-retractions",
    "atlas/atlas-10-breakthrough-genealogy",
    "atlas/atlas-11-cross-pillar-bridge-corpus",
    "atlas/atlas-12-methodology-floor",
    # Atlas-uplift work materials
    "atlas-uplift-materials/",
    # Framework registries that aren't closure inventories
    "registry/elimination-bulletins",
    "registry/falsifier-",
    "registry/methodology-wave-instances",
    "registry/_registry-template",
    "registry/cross-pillar-bridge-corpus",
    "registry/pru-class-corpus",
    "registry/canonical-source-architecture",
    "registry/session-format-generations",
    "registry/permanence-map",
    "registry/orphan-",
    "registry/algebra-axis-",
    "registry/alpha-s-",
    "registry/branch-iv-canonical",
    "registry/cgwb-",
    "registry/class-a-",
    "registry/class-b-",
    "registry/cmb-hd-",
    "registry/constraint-mega-matrix",
    "registry/cutoff-sqrt-",
    "registry/detector-readiness-",
    "registry/dr3-3row-",
    "registry/external-clock-",
    "registry/fisher-pdf-",
    "registry/f-nl-folded-",
    "registry/impulsive-transit-",
    "registry/lancaster-",
    "registry/layer1-layer2-",
    "registry/lizzi-",
    "registry/lrd-",
    "registry/mack-observational-",
    "registry/musr-",
    "registry/path-b-",
    "registry/pillar-bridge-",
    "registry/pre-registered-",
    "registry/propagator-class-",
    "registry/regulator-monodromy-",
    "registry/sigma-2-stratum-",
    "registry/spectral-moment-",
    "registry/w0-primary-",
    "registry/W11-C5-C6-",
    "registry/3he-b-",
    "registry/21cm-",
    "registry/aalto-",
    # EVOI framework (OPEN/carry-forward items, not closures)
    "evoi-framework",
    # Framework root docs (substrate geometry / hypothesis / vis)
    "framework/Phononic-",
    "framework/Framework-First-Physics",
    "framework/Classification-of-phonon-",
    "framework/MathVariables",
    "framework/framework-bbn-hypothesis",
    "framework/framework-cc-oom",  # has CC closures but already in atlas-02
    "framework/framework-chaotic-instantons",
    "framework/framework-dm-properties",
    "framework/framework-parametric-amplification",
    "framework/path-b-",
    "framework/s90-slot-pre-allocation",
    # Framework ARCHIVE
    "framework/ARCHIVE/",
    # Framework correspondence docs (not closure registries)
    "framework/correspondence/",
    # Framework Collabs (atlas-collab work, not closures)
    "framework/Collabs/",
    # Rule / hook / template / skill / agent docs
    "/rules/",
    ".claude/rules/",
    "/hooks/",
    ".claude/hooks/",
    "/templates/",
    ".claude/templates/",
    "/skills/",
    ".claude/skills/",
    ".claude/agents/",
    ".claude/agent-memory/",
    # Session-plan docs (handled separately by _is_plan_file)
    "session-plan/",
)


def _is_non_closure_source(path_str: str) -> bool:
    """True if the path is a known non-closure document — these get []
    from extract_closed_mechanisms regardless of content. Path_str is
    expected to be lowercased and forward-slash-normalized.

    S90 audit (2026-05-17): an earlier handoff (§2.3) claimed
    spectral-post-mortem.md is a "framework ARCHIVE except" exception
    contributing 13 real closure rows. Direct inspection of the file
    (424 lines, 13 H2 narrative sections, 5 diagnostic tables) showed
    all 13 rows were extraction artifacts — numeric values from the
    (tau, <lambda^2>) data table mis-parsed as closure rows, plus H2
    section headings mirrored as closure rows. The closures discussed
    narratively in spectral-post-mortem are already enumerated in
    atlas-02 Era II as proper structured rows. So the blanket
    'framework/ARCHIVE/' blacklist is correct as-stated; no carve-out
    needed."""
    return any(m.lower() in path_str for m in _NON_CLOSURE_SOURCE_MARKERS)


# ---------------------------------------------------------------------------
# Canonical closure-source parsers (S89 cleanup)
#
# Background: the legacy extract_closed_mechanisms below is over-permissive.
# Per audit at tools/_audit_closed_mechanisms.py: 735 rows in the
# closed_mechanisms table where the framework's canonical inventory has
# ~287 real closures. The dominant noise sources are (a) the bullet-list
# pass picking up markdown bullets from any section with "closed" /
# "closure" in the header, and (b) the session-detection heuristic
# matching free-text floats / words as session IDs.
#
# Fix: route the canonical-inventory sources through dedicated parsers.
# Other sources fall through to the legacy parser until each is progressively
# replaced with stricter logic.
#
# Canonical sources covered here:
#   - sessions/permanent-results-registry.md §V
#   - sessions/framework/registry/closed-gw-channels.md
#
# atlas-02-mechanism-lifecycle.md was previously special-cased as a
# canonical source (S89 cleanup); reverted 2026-05-19 because Atlas
# docs are downstream summaries — the S91 cmap retrofit lifted
# closures back to per-session WPs / synthesis docs as the
# authoritative sources.
#
# Pending future commits:
#   - strict narrative-source parser (replaces legacy table+bullet+narrative
#     strategies)
# ---------------------------------------------------------------------------

# `#` column values: integer ("1"), sub-numbered ("56.1"), or range
# ("72-75" with ASCII hyphen, or "22–26" with U+2013 en-dash, or "22-26"
# / "22--26" / "22—26" with em-dash). §V Era II onward uses en-dash.
_ATLAS02_NUMBER_RE = re.compile(r"^\d+(?:\.\d+)?(?:[-–—]\d+)?$")

# ---------------------------------------------------------------------------
# permanent-results-registry.md §V parser
#
# §V uses subsections `### V-A. Era I:`, `### V-B. Era II:`, ..., currently
# through `### V-G. Era VII:` (covers S17-S62; 141+ closures). §V is a
# SUBSET of atlas-02's coverage — Eras VIII-XII (post-S62) are not in §V.
#
# Schema (5 cols, line 1482):
#   | # | Mechanism | Session | Closure Reason | Wall |
#
# The Wall column has a post-hoc `(value=..., scheme=CLOSURE-DECLARATION,
# convention=constraint-eliminated, L_max=NA)` suffix appended by some
# pipeline; strip it.
#
# Tables have BLANK LINES BETWEEN ROWS (artifact of /weave batch helper);
# the parser must tolerate this.
# ---------------------------------------------------------------------------

# §V has 13 subsections V-A through V-M. The Era-keyed subsections
# V-A..V-G enumerate closures for Eras I-VII (S17-S62). Subsections
# V-H, V-I, V-J use a different schema ("S63 Closures", "S64 Closures",
# "S65 Closures" — no Era keyword, no # column) and overlap with
# atlas-02 Era VIII §S63/S64/S65 (#67-91) which is enumerated more
# completely there. V-K, V-L, V-M are meta (Wall Attribution Summary,
# Sagan Correlation Correction, Closure Tally) — not closure tables.
#
# The parser scopes to Era-keyed subsections only. V-H/I/J are
# intentionally skipped (different schema — would require
# schema-specific handling; S63-S65 closures from those subsections
# fall through to the per-session WP / synthesis parsers).
# V-K/L/M are skipped because they're metadata.
_REGV_SUBSECTION_HEADER_RE = re.compile(
    r"^###\s+V-([A-Z]+)\.\s+Era\s+([IVXLC]+):\s+(.+?)$",
    re.MULTILINE,
)


def _strip_regv_wall_suffix(wall: str) -> str:
    """Strip the (value=..., scheme=CLOSURE-DECLARATION, ...) suffix off
    the Wall column in §V tables. Returns the bare wall token (W1/W4/—)."""
    # Match a leading wall token then optional (...) suffix
    m = re.match(r"^\s*(W\d+|[A-Z]\d+|—|-)\s*(?:\(.*\))?\s*$", wall.strip())
    if m:
        return m.group(1)
    # Fallback: take everything before first `(`
    return wall.split("(")[0].strip()[:30]


# ---------------------------------------------------------------------------
# closed-gw-channels.md parser
#
# Canonical registry of eliminated GW-detection channels (LRD-origin).
# Schema: `### channel_name` heading per closure, followed by Claim /
# Basis / Consequence as bullets/paragraphs. Single `## Summary table`
# section at the top.
#
# 7 channels per source (lines 23-29 of the file):
#   cosmic_strings_Gmu_exclusion (observational)
#   U(1)_7_global_Goldstone_not_GW (structural consequence)
#   domain_wall_GW_GUT_GHz (frequency mismatch)
#   KZ_defects_0D_quench (structural)
#   internal_domain_walls_not_4D (structural)
#   PBH_from_strings_light_seeds (parameter-bound consequence)
#   LRD_demographics_not_discriminating (observational degeneracy)
# ---------------------------------------------------------------------------

# Match `### channel_name` headings within the §"Entry detail" section.
# Channel names use snake_case + may include parentheses and digits
# (e.g., `U(1)_7_global_Goldstone_not_GW` at line 40 of the source).
_GWCH_CHANNEL_HEADER_RE = re.compile(
    r"^###\s+`?([A-Za-z_][A-Za-z0-9_()]*)`?\s*$",
    re.MULTILINE,
)


def _extract_closed_from_closed_gw_channels(filepath: Path, text: str) -> list[dict]:
    """Parse closed-gw-channels.md per-channel ### headings.

    Each `### channel_name` heading defines one closed GW channel.
    Subsection bullets `- **Claim**: ...`, `- **Basis**: ...`,
    `- **Consequence**: ...` give the fields. The Summary table at
    the top has the same 7 channels in tabular form; we parse the
    Entry detail section's headings as the canonical source.
    """
    results: list[dict] = []

    # Scope to the §"Entry detail" section (after `## Entry detail`)
    entry_detail = re.search(r"^##\s+Entry\s+detail",
                             text, re.MULTILINE)
    if entry_detail is None:
        return results
    start = entry_detail.end()
    # End at the next `## ` heading
    end_match = re.search(r"^##\s+\S", text[start:], re.MULTILINE)
    end = start + (end_match.start() if end_match else len(text) - start)
    section = text[start:end]

    # Find every channel heading + its content range
    channels = [(m.start(), m.group(1))
                for m in _GWCH_CHANNEL_HEADER_RE.finditer(section)]
    for idx, (cstart, name) in enumerate(channels):
        cend = (channels[idx + 1][0]
                if idx + 1 < len(channels) else len(section))
        body = section[cstart:cend]

        # Extract `- **Claim**: ...`, `- **Basis**: ...`,
        # `- **Consequence**: ...` bullets
        def grab(label: str) -> str:
            m = re.search(rf"-\s*\*\*{label}\*\*:\s*(.+?)(?=\n-\s*\*\*|\n##|\n---|\Z)",
                          body, re.DOTALL)
            if not m:
                return ""
            # Strip trailing whitespace + lingering markdown horizontal-rule artifacts
            val = m.group(1).strip()
            val = re.sub(r"\s*\n\s*-{3,}\s*$", "", val)
            return val[:300]

        claim = grab("Claim")
        basis = grab("Basis")
        consequence = grab("Consequence")

        # Closure reason = Basis (the structural / observational reason)
        # Consequence is the implication for detector reach
        results.append({
            "id": f"closed_gwch_{name}",
            "name": name,
            "session": "",  # GW channels are aggregated across many sessions
            "gate_id": None,
            "closed_by": (basis if basis else claim)[:300],
            "wall": "",
            "claim": claim[:300],
            "consequence": consequence[:300],
            "source_file": str(filepath.relative_to(PROJECT_ROOT)),
            "domain": "GW-channels",
        })

    return results


def _extract_closed_from_permanent_results_v(filepath: Path, text: str) -> list[dict]:
    """Parse permanent-results-registry.md §V subsections.

    Iterates `### V-A. Era I:` headers and parses each subsection's
    markdown table (5-col schema). Tolerates blank lines between rows.
    """
    results: list[dict] = []

    # Find the §V top-level header to scope the search
    v_section_match = re.search(
        r"^##\s+V\.\s+Closed\s+Mechanisms",
        text, re.MULTILINE,
    )
    if v_section_match is None:
        return results
    v_start = v_section_match.start()
    # End of §V is the next `## ` top-level section
    next_top = re.search(r"^##\s+[A-Z]", text[v_start + 10:], re.MULTILINE)
    v_end = v_start + 10 + next_top.start() if next_top else len(text)
    v_body = text[v_start:v_end]

    subsections = [
        (m.start(), m.group(1), m.group(2), m.group(3).strip())
        for m in _REGV_SUBSECTION_HEADER_RE.finditer(v_body)
    ]
    if not subsections:
        return results

    for idx, (start, vletter, era_num, era_name) in enumerate(subsections):
        next_start = (subsections[idx + 1][0]
                      if idx + 1 < len(subsections) else len(v_body))
        sub_body = v_body[start:next_start]

        # Collect all |-prefixed lines (ignoring blank lines between rows)
        table_lines = [line for line in sub_body.splitlines()
                       if line.startswith("|")]
        if not table_lines:
            continue

        # Parse: first non-separator line is header, rest are data
        header = None
        for line in table_lines:
            parts = line.split("|")
            if len(parts) < 3:
                continue
            cells = [c.strip() for c in parts[1:-1]]
            if not cells:
                continue
            if all(re.match(r"^:?-+:?$", c) for c in cells):
                continue
            if header is None:
                header = [c.lower().strip("*").strip() for c in cells]
                continue

            # §V has two schemas: 5-col (Era I-II include Wall) and 4-col
            # (Era III-VII omit Wall; Closure Reason absorbs the wall info)
            if len(cells) < 4:
                continue
            num_raw = cells[0].strip().strip("*").strip()
            if not _ATLAS02_NUMBER_RE.match(num_raw):
                continue
            name = cells[1].strip().strip("*").strip()
            if not name or len(name) < 3:
                continue
            if _is_structural_language(name):
                continue

            sess_cell = cells[2].strip()
            reason = cells[3].strip()
            wall_raw = cells[4].strip() if len(cells) > 4 else ""
            wall = _strip_regv_wall_suffix(wall_raw) if wall_raw else ""

            # 4-col schema embeds the wall suffix inside the Closure Reason
            # cell (last column). Strip the (value=..., scheme=..., ...)
            # suffix from reason so the displayed closed_by is the bare
            # closure reason.
            if not wall:
                reason = re.sub(r"\s*\(value=[^)]*\)\s*$", "", reason)

            # MALFORMED-ROW RECOVERY: row like #81 at line 1750
            # `| 81 | CC staircase | S60 |  | Λ_res (value=...) | oscillates, no convergence |`
            # has an extra empty pipe making the Closure Reason cell
            # empty and pushing real content into cells[4]+cells[5]+. Recover
            # by concatenating the trailing cells as the closure reason.
            source_malformed = False
            if not reason and len(cells) > 4:
                trailing = [c.strip() for c in cells[4:] if c.strip()]
                if trailing:
                    joined = " ".join(trailing)
                    # Strip embedded (value=..., scheme=..., ...) suffix
                    joined = re.sub(r"\s*\(value=[^)]*\)\s*", " ", joined).strip()
                    reason = joined
                    wall = ""  # no clean wall token in malformed row
                    source_malformed = True

            # Extract session + gate_id from `17a SP-4` style
            session = ""
            gate_id = None
            m = re.match(r"^(S?\d+[a-z]?)\s+([A-Z][A-Z0-9-]+[A-Za-z0-9])",
                         sess_cell)
            if m:
                session = m.group(1)
                gate_id = m.group(2)
            else:
                # Just session prefix
                sm = re.match(r"^(S?\d+[a-z]?)", sess_cell)
                if sm:
                    session = sm.group(1)

            # Normalize id key: convert all dash variants to `_`
            num_key = (num_raw.replace(".", "_")
                              .replace("-", "_")
                              .replace("–", "_")
                              .replace("—", "_"))
            entry = {
                "id": f"closed_regv_era{era_num}_{num_key}",
                "name": name[:200],
                "session": session,
                "gate_id": gate_id,
                "closed_by": reason[:300],
                "wall": wall[:50],
                "source_file": str(filepath.relative_to(PROJECT_ROOT)),
            }
            # Mark range rows (roll-up summaries) so downstream consumers
            # can distinguish single-closure rows from roll-ups
            if any(d in num_raw for d in "-–—"):
                entry["range_rollup"] = True
                entry["range_raw"] = num_raw
            # Mark rows where we had to recover from a source-malformed
            # cell layout (extra empty pipes); useful for gap-report
            # triage so the §V source can be corrected upstream
            if source_malformed:
                entry["source_malformed"] = True
            results.append(entry)

    return results


# ---------------------------------------------------------------------------
# S91 cleanup: dedicated parser for session-N(-w*)?(-results)?-workingpaper.md
#
# User adjudication (2026-05-19): "the workingpaper IS the planned output"
# (everything else is probably noise). The WP's `## Constraint[-\s]?Map`
# section is the authoritative structured closure registry per session.
# Schema variants observed across S35-S91 (~116 WP files):
#   - S43:  ID | Prior Status | S{N} Result | New Status | Consequence
#   - S76:  Gate ID | Verdict | Result | Consequence | Data file
#   - S86+: Date | Mechanism/gate | Prior state | New state | Reason
#   - S40:  `## V. Constraint Map Update` (Roman-numeral-prefixed variant)
# Schema-tolerant strategy: closure markers (CLOSED/LANDED/PINNED/REGISTERED/
# PROMOTED) appear in different columns across variants, so the parser keys
# on marker SUBSTRING in any cell rather than schema-specific column.
# ---------------------------------------------------------------------------

# Matches `## Constraint Map Updates`, `## Constraint-Map Updates`,
# `## V. Constraint Map Update`, `## Constraint Map Update`, etc.
_WP_CMAP_SECTION_RE = re.compile(
    r"^##\s+(?:[IVX]+\.\s+)?"
    r"Constraint[-\s]Map(?:[-\s](?:Update|Updates))?[^\n]*\n"
    r"((?:.*?\n)*?)"
    r"(?=^##\s|\Z)",
    re.MULTILINE,
)

# Filename → session ID (e.g., "session-86-w0a-workingpaper.md" → "S86",
# "session-76-results-workingpaper.md" → "S76",
# "session-73a-results-workingpaper.md" → "S73a")
_WP_FILENAME_RE = re.compile(
    r"^session-(\d+[a-z]?)(?:-(?:w[\w-]+|wave\d+|results))*"
    r"-workingpaper\.md$",
    re.IGNORECASE,
)

# Marker substrings that mark a row as a CLOSURE (case-insensitive).
# Includes both the explicit "CLOSED" outcome and the post-S82 vocabulary
# for promotions to permanent registry status ("LANDED" / "REGISTERED" /
# "PINNED" / "PROMOTED" / "WALL LANDED" / "CORRIDOR CLOSED").
_WP_CLOSURE_MARKERS = (
    "CLOSED", "LANDED", "REGISTERED", "PINNED", "PROMOTED",
    "CORRIDOR CLOSED", "WALL LANDED", "CONFIRMED-PROMOTED",
    "STAGE-3-PERMANENT",
)

# Table-header / boilerplate cell text to skip when picking the row's name.
_WP_HEADER_WORDS = {
    "id", "gate id", "gate", "mechanism", "mechanism / gate",
    "mechanism/gate", "date", "prior status", "prior state",
    "new status", "new state", "verdict", "result", "consequence",
    "reason", "data file", "value", "rerun", "rerun result",
    "s35 result", "s36 result", "s37 result", "s38 result",
    "s39 result", "s40 result", "s41 result", "s42 result",
    "s43 result", "s44 result", "s45 result", "s46 result",
    "s47 result", "s48 result",
}


def _extract_closed_from_session_workingpaper(
    filepath: Path, text: str,
) -> list[dict]:
    """Parse closures from session-N(-w*)?(-results)?-workingpaper.md.

    Targets the canonical `## Constraint[-\\s]?Map [Updates]?` section.
    A table row is a closure when any cell contains one of
    `_WP_CLOSURE_MARKERS` (CLOSED, LANDED, PINNED, REGISTERED, PROMOTED).

    Schema-tolerant: works across S43/S76/S86/S87 column orderings because
    the closure-marker substring is the discriminator, not the column
    position. Files without a Constraint-Map section emit nothing (per
    user directive that the WP IS the planned output — if the WP doesn't
    structure its closures, those closures are not in the "planned output"
    layer this parser targets).
    """
    results: list[dict] = []

    fname_m = _WP_FILENAME_RE.match(filepath.name)
    if not fname_m:
        return results
    session_id = "S" + fname_m.group(1)

    sec_m = _WP_CMAP_SECTION_RE.search(text)
    if not sec_m:
        return results
    section_text = sec_m.group(1)

    # Collect markdown table rows from the section (consecutive `|`-lines)
    in_tbl = False
    cur_table: list[str] = []
    tables: list[list[str]] = []
    for line in section_text.splitlines():
        if line.startswith("|"):
            in_tbl = True
            cur_table.append(line)
        elif in_tbl and cur_table:
            tables.append(cur_table)
            cur_table = []
            in_tbl = False
    if cur_table:
        tables.append(cur_table)

    seq = 0
    for tbl in tables:
        # Skip the first row if it's a header (no closure markers AND
        # contains header words); skip the separator row(s).
        for line in tbl:
            parts = line.split("|")
            if len(parts) < 3:
                continue
            cells = [c.strip() for c in parts[1:-1]]
            if not cells or all(not c for c in cells):
                continue
            # Separator row (e.g., `|:--|:--|...`)
            if all(re.match(r"^:?-+:?$", c) for c in cells):
                continue
            # Header row: first cell is a known header word
            first_cell_lower = cells[0].strip("*`").lower()
            if first_cell_lower in _WP_HEADER_WORDS:
                continue

            # Closure-marker test: any cell containing a marker substring
            joined_upper = " | ".join(cells).upper()
            if not any(m in joined_upper for m in _WP_CLOSURE_MARKERS):
                continue

            # Pick the row's name: first non-empty, non-date,
            # non-header-word cell.
            name = ""
            for c in cells:
                cs = c.strip().strip("*`").strip()
                if not cs:
                    continue
                # Skip date-like cells (e.g., "2026-04-30")
                if re.match(r"^\d{4}-\d{2}-\d{2}$", cs):
                    continue
                if cs.lower() in _WP_HEADER_WORDS:
                    continue
                name = cs
                break
            if not name or len(name) < 4 or len(name) > 200:
                continue

            # closed_by = longest non-name cell (typically the
            # "Reason"/"Consequence" column)
            non_name_cells = [c.strip() for c in cells
                              if c.strip() and c.strip() != name]
            closed_by = max(non_name_cells, key=len) if non_name_cells else ""

            # status = cell containing the closure marker (preserved for
            # diagnostics; reveals which marker fired)
            status = ""
            for c in cells:
                cu = c.upper()
                if any(m in cu for m in _WP_CLOSURE_MARKERS):
                    status = c.strip().strip("*`").strip()
                    break

            # gate_id: try to extract a structured gate-ID pattern
            gate_id = None
            gid_m = RE_GATE_ID.search(name + " " + closed_by)
            if gid_m:
                gate_id = gid_m.group(1)

            seq += 1
            results.append({
                "id": f"closed_wp_{session_id.lower()}_{seq}",
                "name": name[:200],
                "session": session_id,
                "gate_id": gate_id,
                "closed_by": closed_by[:300],
                "wp_status": status[:120],
                "source_file": str(filepath.relative_to(PROJECT_ROOT)),
            })

    return results


def extract_closed_mechanisms(filepath: Path, text: str) -> list[dict]:
    """Extract CLOSED mechanisms from a synthesis/framework file.

    S89 cleanup: canonical-inventory sources route to dedicated parsers
    (permanent-results-registry §V; closed-gw-channels). Other
    sources fall through to the legacy table+bullet+narrative parser,
    which is over-permissive and will be tightened in follow-up commits.

    S91 cleanup: session-N(-w*)?(-results)?-workingpaper.md files route
    to the dedicated WP parser (`_extract_closed_from_session_workingpaper`)
    before the legacy path runs. Per user directive (2026-05-19): the WP
    IS the planned output; closures live in the `## Constraint-Map` table.
    """
    if _is_plan_file(filepath):
        return []

    path_str = str(filepath).replace("\\", "/").lower()

    # Canonical-source routing
    if path_str.endswith("/permanent-results-registry.md"):
        rows = _extract_closed_from_permanent_results_v(filepath, text)
        # Drop range-rollup rows: §V uses compressed enumerations like
        # "22-26 Additional post-perturbative closures" or "30-33 Instanton
        # variants (gas, liquid, crystal, dilute)" that aggregate multiple
        # single closures into a synthetic aggregation row. atlas-02
        # enumerates each rolled-up closure individually, so emitting the
        # §V rollup as if it were a single closure produces noise rows
        # whose name (e.g., "Instanton variants (gas, liquid, crystal,
        # dilute)") isn't any one closure. The parser keeps these tagged
        # for gap-report consumers (test harness, future L3 audit); only
        # the closed_mechanisms-bound path filters them.
        return [r for r in rows if not r.get("range_rollup")]
    if path_str.endswith("/closed-gw-channels.md"):
        return _extract_closed_from_closed_gw_channels(filepath, text)

    # Source-blacklist: documents that are NOT closure registries
    if _is_non_closure_source(path_str):
        return []

    # Legacy path — tightened (S89 cleanup):
    #   Strategy 1 (table rows): KEPT with stricter filters
    #   Strategy 2 (bullet pass): REMOVED — was ~95% noise per audit
    #   Strategy 3 (narrative kill headers): KEPT unchanged (already strict)
    results = []

    # Real session-ID pattern: `S?\d+[a-z]?` optionally followed by a
    # gate-tag like "K-1e", or "Session N".
    _NARROW_SESSION_RE = re.compile(
        r"^(S?\d+[a-z]?|Session\s+\d+)\b", re.IGNORECASE)
    # Markdown-header words that masquerade as session IDs in noisy sources
    _SESSION_HEADER_WORDS = {
        "open", "closed", "closure", "pass", "fail", "info", "theorem",
        "path", "pending", "gate", "framework", "estimate", "insight",
        "untested", "true", "excluded", "hypa", "hypb", "hypc", "hypd",
        "done in-session",
    }

    for section_match in RE_CLOSED_SECTION.finditer(text):
        section_text = section_match.group(1)

        # Determine if section header implies all rows are dead
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

        # Table rows (most structured format)
        for cells in _parse_table_rows(section_text):
            if not is_constraint_registry:
                status_cell = None
                for cell in cells:
                    if cell.upper() in ("DEAD", "KILL", "CLOSED"):
                        status_cell = cell.upper()
                        break
                if status_cell is None:
                    continue

            # Name = first non-number cell
            idx = 0
            if cells[0].isdigit() and len(cells) > 1:
                idx = 1
            name = cells[idx]

            # --- STRICT FILTERS (S89 cleanup) ---
            # Skip names that look like markdown headers / table-header
            # words. S91 cleanup: added "question", "verdict", "quantity",
            # "item", "topic", "description" — these are common table-
            # header column labels that surface as false positives once
            # the S? prefix accepts header-row session-cells like
            # "S25 Verdict". Status-cell predicate already gates rows on
            # CLOSED/DEAD/KILL exact match; this is belt-and-suspenders.
            if any(name.lower().startswith(h) for h in
                   ["gate", "mechanism", "theorem", "--", ":", "id",
                    "question", "verdict", "quantity", "item", "topic",
                    "description"]):
                continue
            # Skip markdown structural language
            if _is_structural_language(name):
                continue
            # Name length discipline: 4-80 chars (shorter = fragment,
            # longer = prose sentence)
            if len(name) < 4 or len(name) > 80:
                continue
            # Reject names starting with code/bold markdown
            if name.startswith("`") or name.startswith("**"):
                continue
            # Reject names that are sentence-shaped (end with period)
            if name.rstrip().endswith("."):
                continue
            # S90 cleanup: reject digit-leading names — these are almost
            # always table-data values mis-parsed as closure rows (e.g.,
            # "0.0 (bit-exact)" from s88-w11 numeric table cell;
            # "1-18" from s33b summary row). Real digit-leading closure
            # names ("1-loop Coleman-Weinberg", "3-pole Leggett propagator")
            # are extracted via the per-session WP cmap parser and the
            # §V canonical-source parser, and do NOT touch this legacy path.
            if re.match(r"^\s*[-+]?\d", name):
                continue

            # Extract session + reason from remaining cells
            session = ""
            reason = ""
            remaining = cells[idx + 1:]
            for cell in remaining:
                cstrip = cell.strip()
                # S91 cleanup: accept optional `S` prefix (e.g., `S75`,
                # `S22b`) — pre-S43 sessions used bare `22b`; post-S43
                # adopted `S{N}` convention. The strict-session validator
                # (_NARROW_SESSION_RE at line ~1174) already allows `S?`;
                # this inner discovery loop was the silent block point.
                if not session and re.match(r'S?\d+[a-z]?\b', cstrip):
                    session = cstrip
                elif not session and re.search(r'Session\s+\d+', cell,
                                                re.IGNORECASE):
                    sm = re.search(r'(\d+[a-z]?)', cell)
                    if sm:
                        session = sm.group(1)
                elif cell.upper() not in ("CLOSED",) and not reason:
                    reason = cstrip
            if not session and idx + 1 < len(cells):
                session = cells[idx + 1]
            if not reason and idx + 2 < len(cells):
                reason = cells[idx + 2]

            # --- STRICT SESSION FILTER (S89 cleanup) ---
            # Session field must look like a real session ID
            session_clean = session.strip().lower()
            if session_clean in _SESSION_HEADER_WORDS:
                continue  # markdown-header word, not a session ID
            # Session field must match real-session-ID pattern OR be empty
            # (some legacy table formats omit session entirely)
            if session and not _NARROW_SESSION_RE.match(session):
                # Allow if first whitespace-separated token matches
                first_tok = session.split()[0] if session.split() else ""
                if not _NARROW_SESSION_RE.match(first_tok):
                    continue
            # Session field must not be a free-text float / measurement
            if re.match(r'^-?\d+\.\d{2,}', session):
                continue  # e.g., "R² = -72.3", "B = 1.5e+11", "2.9952"
            # Session field must not be > 30 chars (prose fragment)
            if len(session) > 30:
                continue

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

        # Strategy 2 (bullet-list pass) REMOVED — was the dominant noise
        # source per audit at tools/_audit_closed_mechanisms.py (S89).
        # Documents containing real closures use tables (Strategy 1) or
        # narrative-kill-header form (Strategy 3); the bullet pass was
        # picking up unrelated bullet items from any section that
        # mentioned "closure" in its header.

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

# S81+ canonical verdict line (per .claude/rules/gate-verdicts.md):
#   {GATE_ID}: PASS|FAIL|INFO -- value=<v> scheme=<s> convention=<c> L_max=<L> sha256=<closure>
# GATE_ID may be any dashed uppercase/digit identifier (e.g. T3-S69-BCS-SURFACE-GRAVITY,
# S80-W1-B, BCS-GAP-CANONICAL-70). The 'GATE ' prefix used in older verdict blocks is
# optional here — session s81+ files drop it.
#
# We match only the ID + verdict here; per-field extraction below uses individual
# regexes against the captured full line to avoid the non-greedy short-circuit
# that drops optional groups.
RE_S81_VERDICT = re.compile(
    r"^([A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+):\s+"
    r"(PASS|FAIL|INFO|PRE-REG|INCOMPUTABLE|CANCELLED|INTERMEDIATE)\b"
    r"([^\n]*)$",
    re.MULTILINE,
)
RE_S81_VALUE = re.compile(r"\bvalue=(\S+|\([^)]*\))")
RE_S81_SCHEME = re.compile(r"\bscheme=(\S+)")
RE_S81_CONVENTION = re.compile(r"\bconvention=(\S+)")
RE_S81_LMAX = re.compile(r"\bL_max=(\S+)")
RE_S81_SHA = re.compile(r"\bsha256=([a-f0-9]{16,})")


def extract_gates(filepath: Path, text: str) -> list[dict]:
    """Extract gate verdicts from synthesis or gate verdict files."""
    results = []

    # Plans contain pre-registered PASS/FAIL criteria, not verdicts.
    # See _is_plan_file() docstring. S81 audit: 226 ghost gates removed.
    if _is_plan_file(filepath):
        return results

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
            # data_files: scan every cell + the full surrounding section for
            # script references. Previously returned [] — that broke the
            # gates-to-scripts linkage the Level 3 runner depends on.
            data_files: list[str] = []
            for cell in cells:
                for fm in re.finditer(r"s\d+[a-z]?_\w+\.\w+", cell):
                    data_files.append(fm.group(0))
            # Also scan the section_text near this row (the full table's body)
            for fm in re.finditer(r"s\d+[a-z]?_\w+\.\w+", section_text):
                data_files.append(fm.group(0))
            data_files = list(OrderedDict.fromkeys(data_files))[:10]
            results.append({
                "id": gate_id,
                "name": gate_id,
                "session": session,
                "condition": condition[:200],
                "result": result[:200],
                "verdict": verdict[:100],
                "bayes_factor": bf,
                "data_files": data_files,
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

        # data_files: scan surrounding context (±1000 chars) for script refs.
        # Previously empty — broke the gate→script linkage.
        ctx_start = max(0, m.start() - 1000)
        ctx_end = min(len(text), m.end() + 1000)
        surrounding = text[ctx_start:ctx_end]
        data_files: list[str] = []
        for fm in re.finditer(r"s\d+[a-z]?_\w+\.\w+", surrounding):
            data_files.append(fm.group(0))
        data_files = list(OrderedDict.fromkeys(data_files))[:10]

        results.append({
            "id": gate_id,
            "name": gate_id,
            "session": session,
            "condition": description[:200],
            "result": "",
            "verdict": verdict[:100],
            "bayes_factor": bf,
            "data_files": data_files,
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

    # Strategy 5 (S81+): canonical verdict line — no GATE prefix, carries
    # `value=`, `scheme=`, `convention=`, `L_max=`, `sha256=` fields inline.
    # Required by .claude/rules/gate-verdicts.md (plan §4.5 retrofit).
    for m in RE_S81_VERDICT.finditer(text):
        gate_id = m.group(1).strip()
        verdict_kw = m.group(2).strip().upper()
        rest = m.group(3) or ""  # everything after the verdict keyword
        mv = RE_S81_VALUE.search(rest)
        ms = RE_S81_SCHEME.search(rest)
        mc = RE_S81_CONVENTION.search(rest)
        ml = RE_S81_LMAX.search(rest)
        mh = RE_S81_SHA.search(rest)
        v_value = mv.group(1) if mv else ""
        v_scheme = ms.group(1) if ms else ""
        v_convention = mc.group(1) if mc else ""
        v_lmax = ml.group(1) if ml else ""
        v_sha = mh.group(1) if mh else ""

        # Skip if already found by an earlier strategy with an actual verdict.
        if any(g["id"] == gate_id and
               _is_resolved_verdict(g) for g in results):
            continue

        # Skip patterns that are unrelated but accidentally match (e.g., a
        # chunk of code like 'BP-2: FAIL' in a comment). Require a sha256 pin
        # OR a value= field to confirm this is a real S81 verdict line.
        if not v_sha and not v_value:
            continue

        session = extract_session_from_context(filepath, text, m.start())

        # Compose a human-readable result string so downstream consumers see
        # the pinned fields without parsing the raw line.
        result_parts: list[str] = []
        if v_value:
            result_parts.append(f"value={v_value}")
        if v_scheme:
            result_parts.append(f"scheme={v_scheme}")
        if v_convention:
            result_parts.append(f"convention={v_convention}")
        if v_lmax:
            result_parts.append(f"L_max={v_lmax}")
        if v_sha:
            result_parts.append(f"sha256={v_sha[:16]}...")
        result_text = " | ".join(result_parts)

        # Rip file references from the rest of the same line (inline data_files).
        line_start = text.rfind("\n", 0, m.start()) + 1
        line_end = text.find("\n", m.end())
        if line_end == -1:
            line_end = len(text)
        line_text = text[line_start:line_end]
        data_files: list[str] = []
        for fm in re.finditer(r"s\d+[a-z]?_\w+\.\w+", line_text):
            data_files.append(fm.group(0))
        data_files = list(OrderedDict.fromkeys(data_files))[:10]

        # Remove any stale row for the same id that was PENDING — the S81
        # form is authoritative if it carries a sha256 pin.
        if v_sha:
            results = [g for g in results if g["id"] != gate_id
                       or _is_resolved_verdict(g)]

        results.append({
            "id": gate_id,
            "name": gate_id,
            "session": session,
            "condition": "",
            "result": result_text[:200],
            "verdict": verdict_kw,
            "bayes_factor": None,
            "data_files": data_files,
            "source_file": str(filepath.relative_to(PROJECT_ROOT)),
            # S81 extension fields (non-canonical but useful for downstream):
            "sha256_closure": v_sha,
            "output_4tuple": {
                "value": v_value,
                "scheme": v_scheme,
                "convention": v_convention,
                "L_max": v_lmax,
            },
        })

    return results


def extract_session_from_context(filepath: Path, text: str, pos: int) -> str:
    """Extract session ID from context near position."""
    # Strategy 0: Extract from computation filename prefix (s24a_... -> "24a")
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
# Data provenance extraction (computations/_shared/)
# ---------------------------------------------------------------------------

# Match s{session}_{name}.{ext}
RE_COMPUTATIONS_FILE = re.compile(
    r"^(s\d+[a-z]?)_(.+)\.(py|npz|png|txt|md)$",
    re.IGNORECASE,
)


def extract_data_provenance(computations_dir: Path) -> list[dict]:
    """Scan computations/ for script->data->gate provenance.

    Post-cutover (2026-05-03): files live under session-N/ and _shared/
    subdirs of computations/, so we rglob recursively rather than iterdir
    at top level. Each file_group entry stores the FULL PATH (relative to
    computations_dir) of every member so script_path resolves correctly under
    the new tree layout.
    """
    if not computations_dir.exists():
        return []

    # Group files by session+name prefix; values store relative paths.
    file_groups: dict[str, dict[str, dict | str]] = {}

    for f in sorted(computations_dir.rglob("*")):
        if not f.is_file():
            continue
        m = RE_COMPUTATIONS_FILE.match(f.name)
        if m:
            session = m.group(1)
            name = m.group(2)
            ext = m.group(3).lower()
            key = f"{session}_{name}"
            if key not in file_groups:
                file_groups[key] = {"session": session, "name": name, "files": {}}
            file_groups[key]["files"][ext] = f.relative_to(computations_dir).as_posix()

    results = []
    for key, group in file_groups.items():
        script_rel = group["files"].get("py")
        outputs = []
        for ext in ["npz", "png", "txt", "md"]:
            if ext in group["files"]:
                outputs.append(group["files"][ext])

        # Try to find what gates the script informs
        gates_informed = []
        if script_rel:
            script_path = computations_dir / script_rel
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
        if script_rel:
            script_path = computations_dir / script_rel
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

        # Skip rows with no script — these are harvester artifacts
        # (gate_verdicts.txt, attribution_edges files) whose group has
        # output files but no .py script. They aren't compute-script
        # provenance; treating them as such polluted the data_provenance
        # table with 672 orphans (rows that nothing references because
        # they don't represent a real script-to-output chain).
        if not script_rel:
            continue

        results.append({
            "script": script_rel,
            "session": group["session"],
            "name": group["name"],
            "inputs": inputs[:10],
            "outputs": outputs,
            "gates_informed": list(OrderedDict.fromkeys(gates_informed))[:10],
        })

    # Also include _shared/ and root computations/ helper .py files
    # that don't fit the `sNN_name.ext` pattern. These are import-only
    # libraries (_nc_two_torus_helpers.py, _pauli_villars_subtraction.py,
    # etc.) that equations get extracted from, but they have no session
    # prefix. Treat them as data_provenance rows so equations can
    # terminate against them.
    captured = {r["script"] for r in results}
    for f in sorted(computations_dir.rglob("*.py")):
        if not f.is_file():
            continue
        rel = f.relative_to(computations_dir).as_posix()
        if rel in captured:
            continue
        # Only include helpers (not the sNN_* scripts already captured)
        if RE_COMPUTATIONS_FILE.match(f.name):
            continue
        results.append({
            "script": rel,
            "session": "",
            "name": f.stem,
            "inputs": [],
            "outputs": [],
            "gates_informed": [],
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


AGENTS_DIR = PROJECT_ROOT / ".claude" / "agents"
SESSIONS_DIR = PROJECT_ROOT / "sessions"


def extract_session_files() -> list[dict]:
    """Walk sessions/ for markdown files and emit one row per file.

    The id is the encoded form harvesters use: '<session-id>:<filename>'.
    For files where the session can't be derived from the path, fall back
    to the bare filename. This table exists to anchor the 2,496 unique
    edge IDs in <session>:<filename.md> form that previously dangled
    against the data_provenance table (a type-meaning conflation —
    data_provenance models scripts, not session markdown files).
    """
    if not SESSIONS_DIR.exists():
        return []
    results = []
    seen_ids: set[str] = set()
    # Match session number from path: sessions/(archive/)?session-NN[a-z]?/
    session_re = re.compile(r"sessions[\\/](?:archive[\\/])?session-(\d+[a-z]?)[\\/]")
    # Match session from filename: session-NN-... or session-NNx-...
    # The letter is OPTIONAL (session-91-plan files use no letter,
    # session-17d-X files use lowercase, session-30B/31B files use
    # uppercase). Case-insensitive match; output lowercased so the
    # session ID is canonical.
    subsession_re = re.compile(r"^session-(\d+[a-zA-Z]?)-")
    for fp in SESSIONS_DIR.rglob("*.md"):
        if not fp.is_file():
            continue
        rel = str(fp.relative_to(PROJECT_ROOT)).replace("\\", "/")
        # Derive session-id: prefer sub-session from filename (more
        # specific), fall back to directory match (just the number).
        session = ""
        fm = subsession_re.match(fp.name)
        if fm:
            session = fm.group(1).lower()
        if not session:
            sm = session_re.search(rel.replace("/", "\\"))
            if not sm:
                sm = session_re.search(rel)
            session = sm.group(1).lower() if sm else ""
        filename = fp.name
        # Multiple encodings the edges might reference. Use the
        # '<session>:<filename>' form as canonical ID for files within
        # session-NN/ subdirs (matches harvester edge IDs); use the
        # full relative path for root-level files (permanent-results-
        # registry.md, plan files, framework/ docs, etc.).
        if session:
            encoded_id = f"{session}:{filename}"
        else:
            # Root-level or framework files use the relative path so
            # synthesized edges from theorems/closures pointing here
            # can find them via path match.
            encoded_id = rel
        if encoded_id in seen_ids:
            continue
        seen_ids.add(encoded_id)
        try:
            size = fp.stat().st_size
        except Exception:  # noqa: BLE001
            size = 0
        results.append({
            "id": encoded_id,
            "session": session,
            "filename": filename,
            "path": rel,
            "size_bytes": size,
        })
    return results


def extract_agents() -> list[dict]:
    """Scan .claude/agents/*.md for agent persona definitions.

    Each agent file has YAML frontmatter (name, description, model, color,
    persona, template, memory). The body text references researchers/<X>/
    for the agent's primary knowledge base. We extract the (slug,
    persona, researcher_domain) tuple so edges that reference agent
    slugs have a concrete anchor to terminate in.
    """
    if not AGENTS_DIR.exists():
        return []
    results = []
    for fp in sorted(AGENTS_DIR.iterdir()):
        if not fp.is_file() or fp.suffix != ".md":
            continue
        slug = fp.stem
        try:
            text = fp.read_text(encoding="utf-8", errors="replace")
        except Exception:  # noqa: BLE001
            continue
        fm = _extract_frontmatter(text)
        body = _strip_frontmatter(text)
        # researcher_domain from `researchers/<Domain>/` body references
        researcher_domain = ""
        # Prefer "Primary Knowledge Base" section references; fall back
        # to any researchers/<X>/ reference in the first 3000 chars
        rm = re.search(r"researchers/(\w[\w-]+)/", body[:5000])
        if rm:
            researcher_domain = rm.group(1)
        results.append({
            "slug": slug,
            "name": fm.get("name") or slug,
            "persona": (fm.get("persona") or "").strip().strip('"'),
            "description": (fm.get("description") or "").strip().strip('"')[:400],
            "researcher_domain": researcher_domain,
            "model": fm.get("model") or "",
            "color": fm.get("color") or "",
            "template": fm.get("template") or "",
            "source_file": str(fp.relative_to(PROJECT_ROOT)),
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
    if _is_plan_file(filepath):
        return []
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

# Structural equations in code blocks or plain text: LHS = RHS with math chars.
# Patch C (post-S91 prose-pollution fix): LHS is a math-token sequence. Balanced
# {...} and (...) groups are admitted as opaque tokens (whitespace OK inside),
# but bare whitespace between tokens is NOT allowed in the LHS. This rejects
# prose-with-embedded-equation captures like `with envelope α_k = 2k - 1` while
# preserving LaTeX subscripts like `T_{mu nu}` and parenthesized openers like
# `[V_KK] = ...` or `(iii) chirality chi = ...`.
RE_STRUCT_EQ = re.compile(
    r'^[ ]{0,8}('
    r'[A-Za-z_\(\[]'                              # first char: letter, _, (, [
    r'(?:'
    r'    \{[^{}\n]{0,80}\}'                      # balanced {...} (whitespace OK inside)
    r'    | \([^()\n]{0,80}\)'                    # balanced (...) (whitespace OK inside)
    r'    | [\w_{}\(\)\[\]\\,\^\']'               # safe single char (NO \s)
    r')*'
    r'\s*[=≡≈]\s*'
    r'[^\n|]{5,}'
    r')$',
    re.MULTILINE | re.VERBOSE,
)

# Patch B (post-S91 prose-pollution fix): in-loop filters for verdict-line
# metadata pins, section headers, and mid-clause-truncation indicators.
# Companion to RE_STRUCT_EQ above.
_PATCH_B_VERDICT_PIN_PREFIXES = (
    'audit_sha256', 'content_sha256', 'closure_sha256', 'sha256',
    'convention', 'scheme', 'tier_pin', 'supersedes', 'value',
)
_PATCH_B_PROSE_TAIL_STOPWORDS = frozenset([
    'is', 'was', 'are', 'were', 'has', 'have', 'had', 'be', 'been',
    'being', 'will', 'would', 'could', 'should', 'must', 'may',
    'might', 'the', 'a', 'an', 'of', 'in', 'at', 'to', 'from',
    'on', 'by', 'with', 'as', 'for', 'and', 'or', 'but',
])

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
    # In this project, Python code IS the math — computation scripts are physics computations
    for m in RE_STRUCT_EQ.finditer(text):
        line = m.group(1).strip()
        # Patch B: reject verdict-line metadata pins, section headers, mid-clause truncations
        if line.rstrip().endswith(':'):
            continue
        _first_tok = line.split('=', 1)[0].strip().split()[0] if '=' in line else ''
        if _first_tok in _PATCH_B_VERDICT_PIN_PREFIXES:
            continue
        _tail = re.sub(r'[.,;:]+$', '', line.rstrip())
        _tail_tokens = _tail.split()
        if _tail_tokens and _tail_tokens[-1].lower() in _PATCH_B_PROSE_TAIL_STOPWORDS:
            continue
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


# ---------------------------------------------------------------------------
# Relation-edge extraction (graph edges: implies / supersedes / closed_by / ...)
# ---------------------------------------------------------------------------
#
# Scope. Materializes cross-entity relations that the existing per-type
# extractors only capture as free text. Each edge has a typed source, a
# typed target, a canonical type, an optional comment, and provenance
# (source file + line number).
#
# Tagged-link syntax — block form. One edge per line:
#
#   [EDGE:<type>] <src-type>:<src-id> -> <tgt-type>:<tgt-id>  # optional comment
#
# Examples:
#   [EDGE:implies] theorems:BCS-GAP-CANONICAL-70 -> gates:T3-S69-BCS-SURFACE-GRAVITY
#   [EDGE:supersedes] closed:CC-PROP-62 -> closed:CC-PROP-58  # S63 replaced
#   [EDGE:closed_by] open:LAMBDA-RENORM-43 -> gates:DISSOLUTION-43
#   [EDGE:depends_on] data:s70_bcs_gap.py -> data:r20a_riemann_tensor.npz
#   [EDGE:derived_from] gates:T3-S69-BCS-SURFACE-GRAVITY -> theorems:BCS-GAP-CANONICAL-70
#
# Recognized edge types: implies, supersedes, superseded_by, closed_by,
#   depends_on, derived_from, enables, refutes, refuted_by.
#
# Recognized entity-type aliases:
#   theorems, closed (= closed_mechanisms), gates, open (= open_channels),
#   sessions, researchers, data (= data_provenance), equations, constants.
#
# Dedup key: (type, src_type, src_id_norm, tgt_type, tgt_id_norm). Later
# higher-priority files win; losing comments are preserved in alt_comments.

RE_EDGE_BLOCK = re.compile(
    r"\[EDGE:\s*(?P<etype>[A-Za-z_]+)\s*\]\s+"
    r"(?P<stype>[A-Za-z_]+):\s*(?P<sid>\S+)\s+"
    r"->\s+"
    r"(?P<ttype>[A-Za-z_]+):\s*(?P<tid>\S+?)"
    r"(?:\s*#\s*(?P<comment>.+))?$",
    re.MULTILINE,
)

# Canonical vocabulary tables live in tools/whitelist.py to keep cross-cutting
# data in one place. Producing scripts that emit edges or normalize entity
# types share the same definitions via that module.
from whitelist import EDGE_TYPE_CANONICAL, ENTITY_TYPE_ALIASES  # noqa: E402


def extract_edges(filepath: Path, text: str) -> list[dict]:
    """Extract tagged-link relation edges from a source file."""
    results: list[dict] = []
    for m in RE_EDGE_BLOCK.finditer(text):
        etype_raw = m.group("etype").strip().lower()
        etype = EDGE_TYPE_CANONICAL.get(etype_raw)
        if etype is None:
            continue
        stype_raw = m.group("stype").strip().lower()
        ttype_raw = m.group("ttype").strip().lower()
        stype = ENTITY_TYPE_ALIASES.get(stype_raw)
        ttype = ENTITY_TYPE_ALIASES.get(ttype_raw)
        if stype is None or ttype is None:
            continue
        sid = m.group("sid").strip().rstrip(",.;:")
        tid = m.group("tid").strip().rstrip(",.;:")
        if not sid or not tid:
            continue
        comment = (m.group("comment") or "").strip()
        line_no = text[:m.start()].count("\n") + 1
        results.append({
            "id": "",  # filled after dedup
            "type": etype,
            "source_type": stype,
            "source_id": sid,
            "target_type": ttype,
            "target_id": tid,
            "comment": comment[:300],
            "source_file": str(filepath.relative_to(PROJECT_ROOT)),
            "line": line_no,
        })
    return results


def dedup_edges(edges: list[dict]) -> list[dict]:
    """Deduplicate edges by (type, src_type, src_id_norm, tgt_type, tgt_id_norm).

    Later occurrences (higher file priority) win. Losing comments accumulate
    in `alt_comments`; no annotation is silently dropped.
    """
    def _norm(s: str) -> str:
        return (s or "").strip().lower()

    def _key(e: dict) -> tuple:
        return (
            e.get("type", ""),
            e.get("source_type", ""),
            _norm(e.get("source_id", "")),
            e.get("target_type", ""),
            _norm(e.get("target_id", "")),
        )

    seen: dict[tuple, int] = {}
    extra_comments: dict[tuple, list[str]] = {}

    for i, edge in enumerate(edges):
        k = _key(edge)
        if k in seen:
            winner_idx = seen[k]
            prior = edges[winner_idx]
            new_prio = get_priority(Path(edge.get("source_file", "")))
            old_prio = get_priority(Path(prior.get("source_file", "")))
            if new_prio >= old_prio:
                if prior.get("comment"):
                    extra_comments.setdefault(k, []).append(prior["comment"])
                seen[k] = i
            else:
                if edge.get("comment"):
                    extra_comments.setdefault(k, []).append(edge["comment"])
        else:
            seen[k] = i

    indices = sorted(seen.values())
    out: list[dict] = []
    for pos, i in enumerate(indices, 1):
        edge = edges[i]
        k = _key(edge)
        co = extra_comments.get(k) or []
        if co:
            edge = dict(edge)
            edge["alt_comments"] = co[:10]
        edge["id"] = f"edge_{pos}"
        out.append(edge)
    return out


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
    # Fields that should UNION across dedup collisions rather than winner-takes-all.
    # data_files: every source-file mention of this gate can contribute a script
    # reference; dropping duplicates discards valid linkages (e.g. a gate cited
    # in session-NN minutes AND in computation sNN_gate_verdicts.txt).
    _UNION_FIELDS = ("data_files",)

    # First pass: collect normalized names and their indices
    norms: list[tuple[str, int]] = []
    # Min-length guard varies by key: session/gate IDs can be 2 chars
    # (sessions 80..99 are legitimate "NN" IDs). Name fields (theorems,
    # closed_mechanisms, open_channels) need a higher floor to reject
    # table-fragment names.
    min_len = 2 if key == "id" else 3
    for i, ent in enumerate(entities):
        raw = ent.get(key, "")
        # Skip garbage entries (separator rows, pipe fragments)
        if raw.startswith(":") or raw.startswith("|") or len(raw.strip()) < min_len:
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
                # Union-merge data_files: every mention of this gate across
                # source files is a valid script linkage; taking only one
                # drops references that Level 3 anchor prep depends on.
                for field in _UNION_FIELDS:
                    lv = entities[loser_idx].get(field) or []
                    wv = entities[winner_idx].get(field) or []
                    if isinstance(lv, list) and isinstance(wv, list):
                        merged_list: list = []
                        for item in list(wv) + list(lv):
                            if item and item not in merged_list:
                                merged_list.append(item)
                        entities[winner_idx][field] = merged_list[:20]
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
    # where a proven theorem directly produces a closure).
    #
    # The entries below are GENUINE physics dual-states: each is a result that
    # is BOTH a proven structural theorem (no-go, monotonicity, exhaustion, etc.)
    # AND closes a corresponding mechanism in the constraint map. Storing them
    # in both buckets is correct; the overlap is the data, not noise.
    ALLOWED_OVERLAPS = {
        "rolling modulus quintessence",
        # Mechanisms whose proven no-go theorem closes them
        "v-1",
        "pi-junction phase frustration",
        "pomeranchuk instability of gge",
        "kosmann-bcs condensate (mu=0)",
        "gap-edge self-coupling",
        "fermion condensate (perturbative)",
        "single-field slow-roll",
        "higgs-sigma portal",
        "s_signed gauge-threshold",
        # Structural theorems that close all members of a class
        "perturbative exhaustion theorem",
        # Proven framework results with closed-mechanism status
        "1-loop coleman-weinberg",
        "multi-mode parametric resonance",
        "casimir scalar + vector",
        "casimir with tt 2-tensors",
        "connes 8-cutoff positive spectral sums",
        "connes 8-cutoff positive sums",
        # Proven structural property + closed mechanism
        "eigenvalue ratio phi in singlet",
        "v_tree minimum",
        "v_spec(tau; rho) monotone",
        "v''_total spinodal",
        # Proven no-go / structural results that close the named mechanism
        # (constraint-map closures; sources: constraint-mega-matrix.md,
        # permanent-results-registry.md, atlas-07, Classification-of-phonon-exflation.md)
        "schwinger-instanton duality",
        "lattice ed stabilization",
        "bcs cooling trajectories",
        "unimodular gravity for cc",
        "leptogenesis (real m_r)",
        "cc staircase",
        "gauge frustration",
        "ncg spectral action (seeley-dewitt)",
    }
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
            script_path = COMPUTATIONS_DIR / p["script"]
            archive_path = COMPUTATIONS_ARCHIVE_DIR / p["script"]
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

    # Check 6: Edge endpoint types must be known, and both endpoints non-empty.
    _ALLOWED_EDGE_TYPES = set(EDGE_TYPE_CANONICAL.values())
    _ALLOWED_ENDPOINT_TYPES = set(ENTITY_TYPE_ALIASES.values())
    for e in index.get("edges", []):
        eid = e.get("id", "<unidentified>")
        et = e.get("type", "")
        if et and et not in _ALLOWED_EDGE_TYPES:
            violations.append(f"Edge {eid}: unknown type '{et}'")
        for side in ("source", "target"):
            stype = e.get(f"{side}_type", "")
            sid = e.get(f"{side}_id", "")
            if stype and stype not in _ALLOWED_ENDPOINT_TYPES:
                violations.append(
                    f"Edge {eid}: unknown {side}_type '{stype}'")
            if not sid:
                violations.append(f"Edge {eid}: empty {side}_id")

    return violations


# ---------------------------------------------------------------------------
# Canonical constants audit (S34+ enforcement)
# Patterns, session floor, and exempt list all live in canonical_constants.py.
# This module imports them dynamically — add new patterns THERE, not here.
# ---------------------------------------------------------------------------

def _load_canon_audit_config():
    """Import audit config from canonical_constants.py (computations/_shared/).

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
        "canonical_constants", CANONICAL_CONSTANTS_PATH)
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
    """Extract integer session number from a computation filename like s42_foo.py."""
    m = re.match(r"^s(\d+)", filename, re.IGNORECASE)
    if m:
        return int(m.group(1))
    return None


def audit_canonical_constants(computations_dir: Path) -> list[dict]:
    """Scan S34+ scripts for hardcoded constants that should use canonical_constants.

    Two passes:
      1. VIOLATION: known stale patterns (from AUDIT_PATTERNS_COMPILED)
      2. POTENTIAL_HARDCODE: assignments that look like physics constants but
         aren't in the canon — catches agents inventing new constants without
         updating canonical_constants.py.

    Returns a list of dicts:
        {"script": str, "session": int, "line": int, "pattern": str, "detail": str}
    """
    if not computations_dir.exists():
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
    # Post-Phase-3 layout: scripts live in computations/session-N/, not flat.
    # rglob walks all sub-trees; non-session-named scripts (helpers in
    # _shared/, tests/) are filtered by _extract_session_number returning None.
    for pyf in sorted(computations_dir.rglob("*.py")):
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
                    # Skip if marked as local variable or already fixed
                    if "(local" in line or "# S72:" in line:
                        continue
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
# Canonical constants entity extraction — populates the top-level `constants`
# table in the knowledge index.
# ---------------------------------------------------------------------------
# Sister to audit_canonical_constants above. The AUDIT walks computation
# scripts for compliance violations; this function walks canonical_constants.py
# itself to produce one row per constant, with session/source/gate joined from
# the PROVENANCE dict where available. Constants without PROVENANCE entries
# get null session/source/gate — that's the intentional backfill worklist.

def extract_canonical_constants_entities() -> list[dict]:
    """Build the canonical-constants entity table from canonical_constants.py.

    Returns one dict per top-level scalar / non-config constant, with fields:
        id, name, value, value_type, session, source, gate, superseded,
        line, source_file

    Excludes audit-internal config (AUDIT_*, EXEMPT_*, PROVENANCE, CHANNEL_LABELS).
    Standalone reference implementation lives in tools/_build_constants_table.py.
    """
    import ast
    import importlib.util
    from blacklist import is_constants_excluded as is_excluded

    # AST scan for line numbers per top-level assignment
    try:
        src = CANONICAL_CONSTANTS_PATH.read_text(encoding="utf-8")
        tree = ast.parse(src, filename=str(CANONICAL_CONSTANTS_PATH))
    except Exception as e:
        print(f"  WARN: Could not parse canonical_constants for entity table: {e}")
        return []

    line_map: dict[str, int] = {}
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    line_map[target.id] = node.lineno
        elif isinstance(node, ast.AnnAssign):
            if isinstance(node.target, ast.Name):
                line_map[node.target.id] = node.lineno

    # Import the live module to capture current values + PROVENANCE
    spec = importlib.util.spec_from_file_location(
        "canonical_constants_for_entity_table", CANONICAL_CONSTANTS_PATH
    )
    if spec is None or spec.loader is None:
        print(f"  WARN: Could not load {CANONICAL_CONSTANTS_PATH} for entity extraction")
        return []
    try:
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
    except Exception as e:
        print(f"  WARN: Could not exec canonical_constants for entity extraction: {e}")
        return []

    provenance = getattr(mod, "PROVENANCE", {})
    if not isinstance(provenance, dict):
        provenance = {}

    constants: list[dict] = []
    for name in sorted(dir(mod)):
        if name.startswith("_") or is_excluded(name):
            continue
        if name not in line_map:
            continue  # imported from elsewhere, not a top-level assignment
        val = getattr(mod, name)
        if callable(val):
            continue
        if isinstance(val, (int, float, bool, str)) or val is None:
            value_repr = val
        else:
            value_repr = repr(val)
        prov = provenance.get(name, {})
        if not isinstance(prov, dict):
            prov = {}
        constants.append({
            "id": name,
            "name": name,
            "value": value_repr,
            "value_type": type(val).__name__,
            "session": prov.get("session"),
            "source": prov.get("source"),
            "gate": prov.get("gate"),
            "superseded": prov.get("superseded", False),
            "line": line_map[name],
            "source_file": "computations/_shared/canonical_constants.py",
        })
    return constants


# ---------------------------------------------------------------------------
# Canonical Classes (S86+) — sister to canonical_constants
# ---------------------------------------------------------------------------
# canonical_classes.py defines named groupings of constants ("classes") that
# share a topical or structural relationship — e.g. the CC family, the KK
# scale tower, the alpha_s hierarchy. Two structures are extracted:
#   CLASSES      : dict id -> class metadata (id, name, tier, parent_id,
#                  description, seed_session)
#   CLASS_EDGES  : list of edge-shaped membership records (mirrors REAL_EDGES
#                  schema) — type, srcType='classes', src, tgtType, tgt,
#                  role, comment
# These feed three downstream consumers: the knowledge MCP (via knowledge.db),
# the visualizer's Connections view (via build_data.py), and the topic-page
# builder (via build_topic_pages.py).

def extract_classes(computations_dir: Path) -> tuple[list[dict], list[dict]]:
    """Load canonical_classes.py and extract (classes, class_edges).

    Both returned lists are JSON-serializable. The CLASSES dict is converted
    to a list (each class dict already carries its id field, so the list
    form is lossless). CLASS_EDGES is already a list and is returned as-is.

    Returns ([], []) if canonical_classes.py is absent or fails to load.

    Implementation note: canonical_classes.py contains
    ``from canonical_constants import *`` to satisfy the computation import-rule
    audit, so the sibling module canonical_constants.py must be resolvable
    when the importlib loader executes the module. spec_from_file_location
    does NOT add computations_dir to sys.path automatically, so we inject it for
    the duration of the load and remove it afterwards.
    """
    classes_file = computations_dir / "canonical_classes.py"
    if not classes_file.exists():
        return [], []

    import importlib.util
    import sys as _sys

    computations_str = str(computations_dir)
    path_added = False
    if computations_str not in _sys.path:
        _sys.path.insert(0, computations_str)
        path_added = True

    try:
        spec = importlib.util.spec_from_file_location(
            "canonical_classes", classes_file)
        if spec is None or spec.loader is None:
            return [], []
        mod = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(mod)
        except Exception as e:
            print(f"  WARN: Could not load canonical_classes: {e}")
            return [], []

        classes_dict = getattr(mod, "CLASSES", {})
        class_edges = getattr(mod, "CLASS_EDGES", [])

        # CLASSES is a dict id -> class metadata. Emit as a list of class
        # dicts (each already carries id; the dict form is just a
        # convenience index). Defensive copy so downstream mutations don't
        # leak back into the imported module.
        classes_list = [dict(c) for c in classes_dict.values()]

        # CLASS_EDGES is already a list of dicts in REAL_EDGES schema.
        edges_list = [dict(e) for e in class_edges]

        return classes_list, edges_list
    finally:
        if path_added:
            _sys.path.remove(computations_str)


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
    registries = index.get("registries", [])

    # Gate-level first-word summary (excludes T3-BATCH INFO migrations)
    def _first_word(g):
        v = (g.get("verdict") or "").strip().upper()
        if not v:
            return ""
        return re.split(r"[\s\-|,:/]+", v, maxsplit=1)[0]

    fw_counts: dict[str, int] = {}
    for g in gates:
        w = _first_word(g)
        if w:
            fw_counts[w] = fw_counts.get(w, 0) + 1

    passes_strict = fw_counts.get("PASS", 0)
    fails_strict = fw_counts.get("FAIL", 0)
    closed_strict = fw_counts.get("CLOSED", 0) + fw_counts.get("KILL", 0) \
                    + fw_counts.get("DEAD", 0)
    info_strict = fw_counts.get("INFO", 0)
    diag_strict = fw_counts.get("DIAGNOSTIC", 0)
    # T3-BATCH-* are migration records, not adjudications — count separately.
    t3_batch = sum(1 for g in gates
                   if (g.get("id") or "").startswith("T3-BATCH-"))
    eliminations_gate = fails_strict + closed_strict
    n_closed_mech = len(dead)
    eliminations_total = eliminations_gate + n_closed_mech

    print("=" * 60)
    print("KNOWLEDGE INDEX STATISTICS")
    print("=" * 60)
    print(f"  Theorems (PROVEN):      {len(theorems)}")
    print(f"  Closed mechanisms:      {n_closed_mech}")
    print(f"  Gate verdicts:          {len(gates)}  "
          f"(T3-BATCH migrations: {t3_batch}; adjudicated: {len(gates) - t3_batch})")
    print(f"    PASS:                 {passes_strict}")
    print(f"    FAIL:                 {fails_strict}")
    print(f"    CLOSED/KILL/DEAD:     {closed_strict}")
    print(f"    INFO:                 {info_strict}  (incl. migrations)")
    print(f"    DIAGNOSTIC:           {diag_strict}")
    other = len(gates) - sum([passes_strict, fails_strict, closed_strict,
                              info_strict, diag_strict])
    print(f"    Other first-words:    {other}")
    print(f"  Elimination count (gate FAIL/CLOSED + closed_mechanisms):")
    print(f"    gate eliminations:    {eliminations_gate}")
    print(f"    closed_mechanisms:    {n_closed_mech}")
    print(f"    TOTAL eliminations:   {eliminations_total}")
    if passes_strict > 0:
        print(f"  Eliminations-to-passes ratio: "
              f"{eliminations_total}:{passes_strict} "
              f"({eliminations_total/passes_strict:.2f}:1)")
        print(f"  (Gate-only would read: {eliminations_gate}:{passes_strict} "
              f"= {eliminations_gate/max(1,passes_strict):.2f}:1 — "
              f"note this UNDER-COUNTS because narrative closures land in "
              f"closed_mechanisms, not gates.)")
    print(f"  Sessions indexed:       {len(sessions)}")
    print(f"  Probability points:     {len(traj)}")
    print(f"  Data provenance:        {len(provenance)}")
    print(f"    Scripts:              {sum(1 for p in provenance if p.get('script'))}")
    print(f"    Outputs:              {sum(len(p.get('outputs', [])) for p in provenance)}")
    print(f"  Open channels:          {len(open_ch)}")
    # Framework registries — capstone authority destination (sessions/framework/*.md)
    fw_entity_count = sum(
        1 for arr in (theorems, dead, gates, open_ch)
        for e in arr
        if (e.get("origin") or "") == "framework-registry"
    )
    print(f"  Framework registries:   {len(registries)}  "
          f"(row-level entries promoted: {fw_entity_count})")
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
    edges = index.get("edges", [])
    edge_types: dict[str, int] = {}
    for e in edges:
        t = e.get("type", "unknown")
        edge_types[t] = edge_types.get(t, 0) + 1
    print(f"  Relation edges:         {len(edges)}")
    for t, c in sorted(edge_types.items(), key=lambda x: -x[1]):
        print(f"    {t:22s}{c}")
    print(f"  Generated:              {index.get('generated', 'N/A')}")
    print("=" * 60)


# ---------------------------------------------------------------------------
# Framework registry extraction (capstone authority; fills 33 zero-entry files)
#
# Until this module was added, sessions/framework/ was crawled but produced no
# registry-level entries: every session-minute-format extractor above is keyed
# to patterns (## Session N header, verdict tables with GATE: format) that
# registry files don't use. The _registry-template.md file explicitly declares
# `ingested-by: /weave --update` in its frontmatter — a contract the pipeline
# did not honor. This module honors it.
#
# The framework folder is the canonical destination for knowledge. Entries
# emitted here carry origin="framework-registry" and beat session-level
# extractions on dedup via priority 7. They also flow into a new top-level
# `registries` bucket holding one meta-entry per framework file with its
# metadata, SHA pins, and consumer-gate list.
# ---------------------------------------------------------------------------

RE_FM_BLOCK = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
RE_FM_REG_ID = re.compile(r"^\*\*Registry\s+ID\*\*:\s*`?([^`\n]+?)`?\s*$", re.MULTILINE)
RE_FM_OWNER = re.compile(r"^\*\*Owner\s+agent\(s\)\*\*:\s*([^\n]+)$", re.MULTILINE)
RE_FM_LAST_UPDATED = re.compile(r"^\*\*Last\s+updated\*\*:\s*`?([^`\n]+?)`?\s*$", re.MULTILINE)
RE_FM_GATE_HDR = re.compile(r"^\*\*Gate\*\*:\s*([A-Za-z0-9][\w\-/]*)", re.MULTILINE)
RE_FM_CLOSURE_SHA = re.compile(
    r"^\*\*Closure\s+SHA-256\*\*:\s*`?([a-f0-9]{16,64})`?", re.MULTILINE
)
RE_FM_CONTENT_SHA = re.compile(
    r"\*\*[Cc]ontent[\s_-]SHA(?:-256)?\*\*:\s*`?([a-f0-9]{16,64})`?"
)
RE_FM_AUDIT_SHA = re.compile(
    r"\*\*[Aa]udit[\s_-]SHA(?:-256)?\*\*:\s*`?([a-f0-9]{16,64})`?"
)
RE_FM_SCOPE = re.compile(
    r"^##\s+Scope\s*\n(.+?)(?=\n##\s|\n---)",
    re.DOTALL | re.MULTILINE,
)
RE_FM_SUMMARY_SEC = re.compile(
    r"^##\s+Summary[^\n]*\n(.+?)(?=\n##\s|\Z)",
    re.DOTALL | re.MULTILINE,
)
RE_FM_CONSUMER_SEC = re.compile(
    r"^##\s+Consumer\s+gates\s*\n(.+?)(?=\n##\s|\n---|\Z)",
    re.DOTALL | re.MULTILINE | re.IGNORECASE,
)
RE_FM_CHANNEL_SEC = re.compile(
    r"^##\s+(?:Channel\s+Table|Falsifier\s+Channels?|Observable\s+Table|"
    r"Summary\s+table[^\n]*|Tally)[^\n]*\n(.+?)(?=\n##\s|\Z)",
    re.DOTALL | re.MULTILINE | re.IGNORECASE,
)
RE_FM_CHANGE_SEC = re.compile(
    r"^##\s+Change\s+log\s*\n(.+?)(?=\n##\s|\n---|\Z)",
    re.DOTALL | re.MULTILINE | re.IGNORECASE,
)
RE_FM_ANY_TABLE = re.compile(r"((?:^\|[^\n]+\n){3,})", re.MULTILINE)

# Per-experiment H2 sections in pre-registered-observations style
RE_FM_EXPERIMENT_H2 = re.compile(
    r"^##\s+([A-Z][A-Za-z0-9/ +&-]+?)\s*"
    r"(?:—|--|-)\s*"          # em-dash or hyphen separator
    r"(.+?)(?=\n##\s|\Z)",
    re.DOTALL | re.MULTILINE,
)


def _extract_frontmatter(text: str) -> dict:
    """Return {key: value} dict from YAML-ish frontmatter, or {} if absent."""
    m = RE_FM_BLOCK.match(text)
    if not m:
        return {}
    fm: dict[str, str] = {}
    for line in m.group(1).split("\n"):
        if ":" in line:
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm


def _strip_frontmatter(text: str) -> str:
    m = RE_FM_BLOCK.match(text)
    return text[m.end():] if m else text


def _parse_md_table(text: str) -> list[dict]:
    """Parse a markdown table into list of dicts {header_cell: cell}.

    Expects header row, separator row, then data rows. Returns empty list
    when the input has fewer than two pipe-lines. Each returned dict also
    carries `_raw_cells` holding the original split-by-pipe list, useful
    when headers collide or the first column is unnamed.
    """
    raw_lines = [ln for ln in text.split("\n") if ln.strip().startswith("|")]
    if len(raw_lines) < 2:
        return []

    def _cells(line: str) -> list[str]:
        parts = [c.strip() for c in line.split("|")]
        if parts and parts[0] == "":
            parts = parts[1:]
        if parts and parts[-1] == "":
            parts = parts[:-1]
        return parts

    header = _cells(raw_lines[0])
    rows: list[dict] = []
    body_start = 2 if len(raw_lines) >= 2 and _is_separator_row(raw_lines[1]) else 1
    for ln in raw_lines[body_start:]:
        cells = _cells(ln)
        if not cells:
            continue
        if _is_separator_row(ln):
            continue
        row = {}
        for i in range(min(len(header), len(cells))):
            row[header[i]] = cells[i]
        row["_raw_cells"] = cells
        rows.append(row)
    return rows


def _is_separator_row(line: str) -> bool:
    """True for markdown table separator rows like |:---|:---|."""
    stripped = line.strip().strip("|")
    cells = [c.strip() for c in stripped.split("|")]
    return all(set(c) <= {"-", ":", " "} and any(ch in c for ch in ":-") for c in cells if c)


_FW_BUCKET_HINTS = [
    # (filename-substring-matcher, target-buckets list)
    (("falsifier-rigor-registry",), ["open_channels"]),
    (("falsifier-watchlist",), ["open_channels"]),
    (("pre-registered-observations",), ["open_channels"]),
    (("framework-dm-properties",), ["open_channels"]),
    (("lrd-observational-constraints",), ["open_channels"]),
    (("21cm-science-case",), ["open_channels"]),
    (("cross-channel-correlation-matrix",), ["open_channels"]),
    (("closed-gw-channels",), ["closed_mechanisms"]),
    (("spectral-post-mortem",), ["closed_mechanisms"]),
    (("permanent-results", "atlas-07"), ["theorems"]),
    (("atlas-04", "assumptions"), ["theorems", "closed_mechanisms"]),
    (("atlas-05", "walls-doors-windows"), ["theorems", "closed_mechanisms"]),
    (("atlas-08", "open-questions"), ["open_channels"]),
    (("atlas-09", "retractions"), ["closed_mechanisms"]),
    (("atlas-10", "breakthrough-genealogy"), ["theorems"]),
    (("baseline-findings",), ["theorems", "gates", "open_channels"]),
    (("constraint-mega-matrix",), ["theorems", "gates", "closed_mechanisms"]),
    (("framework-bbn-hypothesis",), ["open_channels"]),
    (("framework-chaotic-instantons",), ["open_channels"]),
    (("framework-parametric-amplification",), ["open_channels"]),
    (("classification-of-phonon-exflation",), ["theorems"]),
    (("mathvariables",), []),
    (("phononic-investigation",), []),
]


def _classify_registry_buckets(filepath: Path, fm: dict) -> list[str]:
    """Return the entity buckets a framework registry's Summary rows feed into.

    Explicit frontmatter `ingests-as: bucket1, bucket2` wins; otherwise a
    filename heuristic drives it. Returning [] means the file is still given
    a meta-entry in `registries` but no row-level extraction (discussion/prose).
    """
    rel_l = str(filepath).lower().replace("\\", "/")
    explicit = (fm.get("ingests-as") or "").strip()
    if explicit:
        buckets = [b.strip() for b in explicit.split(",") if b.strip()]
    else:
        stem = filepath.stem.lower()
        buckets = []
        for keys, hint_buckets in _FW_BUCKET_HINTS:
            if any(k in stem or k in rel_l for k in keys):
                buckets = list(hint_buckets)
                break
        # Discussion / collab / phononic / general atlas — meta-entry only.

    # Respect _NON_CLOSURE_SOURCE_MARKERS — files marked non-closure must
    # not emit closed_mechanisms via the framework-registry path either,
    # even when _FW_BUCKET_HINTS maps them there. atlas-04-assumptions is
    # the canonical case: assumption rows tagged BROKEN/DISSOLVED look
    # like closures by status keyword but live in the assumptions
    # catalog rather than the mechanism-lifecycle inventory. The two
    # routing systems (extract_closed_mechanisms blacklist + bucket
    # hints) must agree on which files contribute closures.
    if _is_non_closure_source(rel_l):
        buckets = [b for b in buckets if b != "closed_mechanisms"]
    return buckets


def _first_header_title(text: str) -> str:
    m = re.search(r"^#\s+(.+?)\s*$", text, re.MULTILINE)
    return m.group(1).strip() if m else ""


def _extract_session_tag(text: str) -> str:
    """Find first 'S<NN>[-W<N>[-<item>]]' or 'S<NN><letter>' tag."""
    m = re.search(r"\bS(\d{1,3}[a-z]?)(?:-W\d+[a-z]?)?", text)
    return f"S{m.group(1)}" if m else ""


_INDEX_CELL_RE = re.compile(
    r"^(?:"
    r"\d+|"                          # pure integer: 1, 18
    r"[A-Z]{1,2}\d{1,3}[a-z]?|"      # tag: A1, G12, T17, B5a
    r"\(\d+\)|"                       # (1), (2)
    r"\d{4}(?:-\d{2,4})?|"            # year or year-range: 2026, 2026-27
    r"Q\d+"                           # Q1, Q2 (quarter or question tag)
    r")$"
)


# Status-keyword sets used by _route_row_to_bucket. PROVEN/ASSUMED/CONDITIONAL
# rows belong in theorems; BROKEN/DISSOLVED/CLOSED/KILL/DEAD rows belong in
# closed_mechanisms; LIVE flags / rigor tags belong in open_channels; canonical
# gate verdicts (PASS/FAIL/INFO) belong in gates. This matches the keyword
# legend used by the authors of atlas-04-assumptions and related registries.
_STATUS_THEOREMS = {"PROVEN", "ASSUMED", "CONDITIONAL", "PERMANENT"}
_STATUS_CLOSED = {"BROKEN", "DISSOLVED", "CLOSED", "KILL", "DEAD", "RETRACTED"}
_STATUS_OPEN = {"LIVE", "LIVE-PENDING", "ZERO-FREE-PARAMETER", "ACCOMMODATION",
                 "SCHEME-DEPENDENT", "DETECTOR-STERILE", "PINNED",
                 "WARRANT-DEFERRED", "DEPRECATED"}
_STATUS_GATES = {"PASS", "FAIL", "INFO"}


def _row_status_keyword(raw: list[str]) -> str:
    """Scan a row's cells for a recognized status keyword. Returns "" if absent."""
    blob = " | ".join(raw)
    m = re.search(
        r"\b(ZERO-FREE-PARAMETER|ACCOMMODATION|SCHEME-DEPENDENT|"
        r"DETECTOR-STERILE|PINNED|WARRANT-DEFERRED|DEPRECATED|"
        r"LIVE-PENDING|LIVE|PASS|FAIL|INFO|CLOSED|BROKEN|DISSOLVED|"
        r"CONDITIONAL|PROVEN|ASSUMED|RETRACTED|PERMANENT|KILL|DEAD)\b",
        blob,
    )
    return m.group(1) if m else ""


def _route_row_to_bucket(row: dict, target_buckets: list[str]) -> str | None:
    """Pick a single bucket for a registry row based on its status keyword.

    For single-bucket files every row goes to that one bucket (status-keyword
    routing is a no-op). For multi-bucket files (atlas-04-assumptions,
    baseline-findings-s66, constraint-mega-matrix) this prevents the same row
    from being emitted to both theorems and closed_mechanisms, which was
    causing 238 PROVEN+CLOSED overlap validation violations on first rebuild.

    Returns the chosen bucket, or None if the row has no matching bucket
    (shouldn't happen for well-classified files; defensive no-op on ambiguity).
    """
    if not target_buckets:
        return None
    if len(target_buckets) == 1:
        return target_buckets[0]
    raw = row.get("_raw_cells") or []
    keyword = _row_status_keyword(raw).upper()
    if keyword in _STATUS_THEOREMS and "theorems" in target_buckets:
        return "theorems"
    if keyword in _STATUS_CLOSED and "closed_mechanisms" in target_buckets:
        return "closed_mechanisms"
    if keyword in _STATUS_OPEN and "open_channels" in target_buckets:
        return "open_channels"
    if keyword in _STATUS_GATES and "gates" in target_buckets:
        return "gates"
    # No recognized status keyword — fall back to the first bucket hint, which
    # represents the file's primary classification (see _FW_BUCKET_HINTS order).
    return target_buckets[0]


def _looks_like_index_cell(cell: str) -> bool:
    """True when a cell is a pure index column (#, 1, A1, G12, 2026-27, etc.).

    Used by _registry_row_to_entity to detect tables whose first column is
    a row index rather than an entity name — in those cases the entity name
    lives in the second column. Seen in: atlas-07 Tier-A table (| # | Result),
    atlas-04 assumptions (| # | Assumption), falsifier-rigor Channel Table
    (| # | Channel), cross-channel-correlation-matrix (| i | Channel).
    """
    s = (cell or "").strip("`").strip("*").strip()
    if not s:
        return True
    if s.lower() in {"#", "i", "n", "no.", "num", "idx", "index",
                       "id", "test", "pair", "cell"}:
        return True
    return bool(_INDEX_CELL_RE.match(s))


def _registry_row_to_entity(
    row: dict,
    bucket: str,
    registry_id: str,
    source_rel: str,
    row_index: int,
) -> dict | None:
    """Map a Summary-table row to an entity of the target bucket.

    Returns None if the row is a placeholder (template angle-brackets) or
    otherwise unparseable. Bucket-specific fields follow the same schema
    as the session-level extractors so the entity flows through the same
    dedup + serialization paths.
    """
    raw = row.get("_raw_cells") or []
    if not raw:
        return None
    first = raw[0].strip()
    # Skip template placeholders, separator fragments, header-looking rows
    if not first or first.startswith("<") or first.startswith("`<"):
        return None
    if set(first) <= {"-", ":", " ", "|"}:
        return None

    # Pick the name cell. If the first column is an index (#, 1, A1, year,
    # etc.) the real name lives in the second column. The index token is
    # preserved in the `tag` field for traceability.
    name_idx = 0
    row_tag = None
    if len(raw) > 1 and _looks_like_index_cell(raw[0]):
        name_idx = 1
        row_tag = raw[0].strip("`").strip("*").strip()

    # Also skip if the candidate name is purely a header word.
    name = raw[name_idx].strip("`").strip("*").strip()
    while (name_idx < len(raw) - 1
           and (not name
                or name.lower() in ("#", "id", "test", "channel", "entry",
                                     "pair", "property", "result", "i",
                                     "idx", "n", "no.")
                or _looks_like_index_cell(name))):
        name_idx += 1
        if not row_tag:
            row_tag = raw[name_idx - 1].strip("`").strip("*").strip()
        name = raw[name_idx].strip("`").strip("*").strip()

    if not name or name.lower() in ("#", "id", "test", "channel", "entry",
                                      "pair", "property", "result"):
        return None
    # Skip markdown structural language (section labels, metadata prefixes)
    if _is_structural_language(name):
        return None

    # Flatten the row to a text blob for regex scans
    blob = " | ".join(raw)

    session = _extract_session_tag(blob)
    # Identify a gate-ID-looking token anywhere in the row
    gate_id_match = re.search(
        r"\b(S\d+[a-z]?-[A-Z][A-Z0-9-]*|[A-Z]{2,}-\d+[a-z]?|"
        r"[A-Z]+-[A-Z0-9-]+-\d+[a-z]?)\b", blob
    )
    gate_id = gate_id_match.group(1) if gate_id_match else None

    status_last = raw[-1].strip().strip("*").strip("`") if len(raw) > 1 else ""
    # Status can also be mid-row for Pattern-B flag tables
    status_match = re.search(
        r"\b(ZERO-FREE-PARAMETER|ACCOMMODATION|SCHEME-DEPENDENT|"
        r"DETECTOR-STERILE|PINNED|WARRANT-DEFERRED|DEPRECATED|"
        r"LIVE|LIVE-PENDING|PASS|FAIL|INFO|CLOSED|BROKEN|DISSOLVED|"
        r"CONDITIONAL|PROVEN|ASSUMED|RETRACTED|PERMANENT)\b", blob
    )
    status = status_match.group(1) if status_match else status_last
    # Strip obvious non-status tokens that might leak into the last-cell
    # fallback (session refs like "S64", script paths, year ranges). Atlas
    # theorem/closure tables often have a trailing Session column rather than
    # a Status column.
    if not status_match:
        _noise_pat = re.compile(
            r"^(?:S\d+[a-z]?(?:-[\w-]+)?|\d{4}(?:-\d{2,4})?|"
            r"[a-z_]+\.py(?::\d+)?|—|-|—|N/?A)$",
            re.IGNORECASE,
        )
        if _noise_pat.match(status or ""):
            status = ""

    base = {
        "id": f"fw_{bucket}_{row_index}",
        "name": name[:200],
        "tag": row_tag,
        "source_file": source_rel,
        "origin": "framework-registry",
        "registry_id": registry_id,
        "session": session,
        "sessions": session,
        "row_text": blob[:400],
    }

    if bucket == "theorems":
        # The monotonicity/classification atlases use Tier-A/B/etc. as status;
        # leave status as-is but default to PROVEN for rows without a status
        # keyword.
        precision_match = re.search(
            r"(machine\s+epsilon|exact(?:ly)?|PERMANENT|structural|"
            r"\b[0-9](?:\.\d+)?e[-+]?\d+\b)",
            blob, re.IGNORECASE,
        )
        return {
            **base,
            "status": status or "PROVEN",
            "precision": precision_match.group(1) if precision_match else None,
            "statement": (" | ".join(raw[1:]))[:300] or name[:300],
        }
    if bucket == "closed_mechanisms":
        return {
            **base,
            "closed_by": status or (raw[-1] if len(raw) > 1 else name)[:200],
            "gate_id": gate_id,
        }
    if bucket == "gates":
        return {
            **base,
            "id": gate_id or base["id"],
            "condition": (raw[1] if len(raw) > 1 else "")[:200],
            "result": (raw[2] if len(raw) > 2 else "")[:200],
            "verdict": status or "OPEN",
        }
    if bucket == "open_channels":
        return {
            **base,
            "detail": (" | ".join(raw[1:]))[:400] or name,
        }
    # Unknown bucket — pass through a minimal shape
    return base


def extract_framework_registry(filepath: Path, text: str) -> dict:
    """Extract framework-registry meta-entry and row-level entities.

    Returns:
      {"registry": <meta-dict or None>,
       "entities": {"theorems": [...], "closed_mechanisms": [...],
                    "gates": [...], "open_channels": [...]}}

    Pattern coverage:
      A. Registry template — YAML frontmatter `type: registry` OR bolded
         **Registry ID**: header; Summary table under ## Summary table; one
         Entry-detail block per slug.
      B. Falsifier-rigor — **Gate**: + **Closure SHA-256**: header; per-flag
         tally; Channel Table as the main registry.
      C. Pre-registered observations — per-detector H2 sections with their
         own ## tables; rigor registry appended at bottom.
      D. Atlas / classification — heterogeneous H2 tables (Tier-A/B/C/D/E,
         PROVEN/ASSUMED/BROKEN/DISSOLVED); no single Summary table but
         per-section tables each carry typed rows.
    """
    result: dict = {"registry": None, "entities": {}}
    if not _is_framework_file(filepath):
        return result
    if filepath.suffix != ".md":
        return result

    rel = str(filepath.relative_to(PROJECT_ROOT)).replace("\\", "/")
    fm = _extract_frontmatter(text)
    body = _strip_frontmatter(text)

    # Load metadata with multi-pattern tolerance
    mreg_id = RE_FM_REG_ID.search(body[:5000])
    mowner = RE_FM_OWNER.search(body[:5000])
    mupdate = RE_FM_LAST_UPDATED.search(body[:5000])
    mgate = RE_FM_GATE_HDR.search(body[:5000])
    mclosure = RE_FM_CLOSURE_SHA.search(body)
    mcontent = RE_FM_CONTENT_SHA.search(body)
    maudit = RE_FM_AUDIT_SHA.search(body)

    registry_id = (mreg_id.group(1).strip() if mreg_id else filepath.stem)

    # Scope paragraph (Pattern A) or Purpose (Pattern B)
    scope_match = RE_FM_SCOPE.search(body)
    if not scope_match:
        scope_match = re.search(
            r"^##\s+Purpose\s*\n(.+?)(?=\n##\s|\n---)",
            body, re.DOTALL | re.MULTILINE,
        )
    scope_text = scope_match.group(1).strip() if scope_match else ""

    owner_agents: list[str] = []
    if mowner:
        raw = mowner.group(1).strip()
        # Strip trailing comments, backticks
        raw = re.split(r"\s*[—–\-]{1,2}\s*", raw)[0]
        for token in re.split(r"[,;]", raw):
            t = token.strip().strip("`").strip("*").strip()
            if t and not t.startswith("("):
                owner_agents.append(t)

    # Summary table: try explicit ## Summary heading, then first big table
    sum_text = ""
    m = RE_FM_SUMMARY_SEC.search(body)
    if m:
        sum_text = m.group(1)
    if not sum_text:
        m = RE_FM_CHANNEL_SEC.search(body)
        if m:
            sum_text = m.group(1)
    summary_rows = _parse_md_table(sum_text) if sum_text else []

    if not summary_rows:
        # Fall back: first markdown table in the body
        tm = RE_FM_ANY_TABLE.search(body)
        if tm:
            summary_rows = _parse_md_table(tm.group(1))

    # Consumer gates
    consumer_gates: list[str] = []
    cg_match = RE_FM_CONSUMER_SEC.search(body)
    if cg_match:
        for row in _parse_md_table(cg_match.group(1)):
            gid_cell = row.get("Gate ID") or (
                row["_raw_cells"][0] if row.get("_raw_cells") else None
            )
            if not gid_cell:
                continue
            gid_cell = gid_cell.strip("`").strip("*").strip()
            if gid_cell and not gid_cell.startswith("<") and not gid_cell.startswith("("):
                # Extract just the gate ID token
                gm = re.match(r"([A-Z][\w-]+)", gid_cell)
                if gm:
                    consumer_gates.append(gm.group(1))

    target_buckets = _classify_registry_buckets(filepath, fm)

    title = _first_header_title(body) or filepath.stem
    frontmatter_type = fm.get("type") or ""
    declared_ingestion = fm.get("ingested-by") or ""

    # Build meta-entry for `registries` bucket
    meta = {
        "id": f"registry_{filepath.stem}",
        "registry_id": registry_id,
        "title": title,
        "owner_agents": owner_agents,
        "last_updated": (mupdate.group(1).strip() if mupdate else None),
        "origin_gate": mgate.group(1) if mgate else None,
        "closure_sha256": mclosure.group(1) if mclosure else None,
        "content_sha256": mcontent.group(1) if mcontent else None,
        "audit_sha256": maudit.group(1) if maudit else None,
        "frontmatter_type": frontmatter_type,
        "declared_ingestion": declared_ingestion,
        "scope": scope_text[:800],
        "summary_row_count": len(summary_rows),
        "target_buckets": target_buckets,
        "consumer_gates": consumer_gates,
        "source_file": rel,
        "origin": "framework-registry",
    }
    result["registry"] = meta

    # Row-level extraction (skip for discussion / unclassified files)
    if not target_buckets:
        return result

    per_bucket: dict[str, list] = {b: [] for b in target_buckets}
    for i, row in enumerate(summary_rows):
        # Route each row to the single best-matching bucket (prevents
        # PROVEN+CLOSED overlap violations when a multi-bucket file like
        # atlas-04-assumptions has both PROVEN and BROKEN rows).
        bucket = _route_row_to_bucket(row, target_buckets)
        if bucket is None:
            continue
        ent = _registry_row_to_entity(row, bucket, registry_id, rel, i + 1)
        if ent is not None:
            per_bucket[bucket].append(ent)

    # Pattern C: scan each per-experiment H2 section for additional tables
    # (pre-registered-observations emits per-detector tables each with its own
    # rigor/prediction rows; not just a top-level Summary).
    if "pre-registered-observations" in filepath.stem.lower():
        seen_rows = {tuple(r.get("_raw_cells") or []) for r in summary_rows}
        for detector_match in RE_FM_EXPERIMENT_H2.finditer(body):
            det_section = detector_match.group(0)
            for tbl_match in RE_FM_ANY_TABLE.finditer(det_section):
                for row in _parse_md_table(tbl_match.group(1)):
                    key = tuple(row.get("_raw_cells") or [])
                    if key in seen_rows:
                        continue
                    seen_rows.add(key)
                    bucket = _route_row_to_bucket(row, target_buckets)
                    if bucket is None:
                        continue
                    ent = _registry_row_to_entity(
                        row, bucket, registry_id, rel, len(per_bucket[bucket]) + 1
                    )
                    if ent is not None:
                        per_bucket[bucket].append(ent)

    # Pattern D1: Atlas numbered-narrative H2 sections (atlas-10 genealogy).
    # No tables — each breakthrough is a `## N. Title` section with prose.
    # Emit one theorem-entry per H2 whose heading matches `^## \d+\. `.
    if "breakthrough-genealogy" in filepath.stem.lower() or (
        re.search(r"^##\s+1\.\s", body, re.MULTILINE)
        and not re.search(r"^##\s+Summary\s+table", body, re.MULTILINE | re.IGNORECASE)
    ):
        for h2_match in re.finditer(
            r"^##\s+(\d+)\.\s+(.+?)\s*\n(.+?)(?=\n##\s|\Z)",
            body, re.DOTALL | re.MULTILINE,
        ):
            num = h2_match.group(1)
            title_text = h2_match.group(2).strip()
            body_text = h2_match.group(3)
            # Skip narrative section headings that are structural language
            if _is_structural_language(title_text):
                continue
            session = _extract_session_tag(title_text + " " + body_text[:500])
            # For atlas-10 narrative sections we always emit to the FIRST target
            # bucket — these are breakthroughs (theorems), not typed rows.
            narr_bucket = target_buckets[0] if target_buckets else None
            if narr_bucket is None:
                continue
            for bucket in [narr_bucket]:
                ent = {
                    "id": f"fw_{bucket}_narrative_{num}",
                    "name": title_text[:200],
                    "tag": f"#{num}",
                    "source_file": rel,
                    "origin": "framework-registry",
                    "registry_id": registry_id,
                    "session": session,
                    "sessions": session,
                    "row_text": title_text[:300],
                }
                if bucket == "theorems":
                    # Pull first-sentence significance as the statement
                    sig_match = re.search(
                        r"\*\*Significance\*\*:\s*(.+?)(?:\.\s|\n)",
                        body_text, re.DOTALL,
                    )
                    ent["status"] = "PROVEN"
                    ent["precision"] = None
                    ent["statement"] = (
                        sig_match.group(1).strip()[:300] if sig_match
                        else title_text[:300]
                    )
                elif bucket == "open_channels":
                    ent["detail"] = title_text[:400]
                elif bucket == "closed_mechanisms":
                    ent["closed_by"] = title_text[:200]
                    ent["gate_id"] = None
                per_bucket[bucket].append(ent)

    # Pattern D2: Atlas multi-section tables (atlas-04-assumptions,
    # atlas-07-permanent-results have ## I/II/III sections, each with
    # its own table — not one Summary block). Scan all H2 sections beyond
    # ## Scope / Consumer gates / Change log that contain tables.
    if "atlas" in filepath.stem.lower() or filepath.stem.lower() in (
        "constraint-mega-matrix", "baseline-findings-s66"
    ):
        seen_rows = {tuple(r.get("_raw_cells") or []) for r in summary_rows}
        for h2_match in re.finditer(
            r"^##\s+([^\n]+?)\n(.+?)(?=\n##\s|\Z)",
            body, re.DOTALL | re.MULTILINE,
        ):
            header = h2_match.group(1).strip().lower()
            if any(skip in header for skip in (
                "scope", "purpose", "consumer gates", "change log",
                "migration notes", "tally", "timeline overview",
                "audit methodology", "summary assessment",
            )):
                continue
            section = h2_match.group(2)
            for tbl_match in RE_FM_ANY_TABLE.finditer(section):
                for row in _parse_md_table(tbl_match.group(1)):
                    key = tuple(row.get("_raw_cells") or [])
                    if key in seen_rows:
                        continue
                    seen_rows.add(key)
                    bucket = _route_row_to_bucket(row, target_buckets)
                    if bucket is None:
                        continue
                    ent = _registry_row_to_entity(
                        row, bucket, registry_id, rel, len(per_bucket[bucket]) + 1
                    )
                    if ent is not None:
                        per_bucket[bucket].append(ent)

    result["entities"] = per_bucket
    return result


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

    for computation in [COMPUTATIONS_DIR, COMPUTATIONS_ARCHIVE_DIR]:
        if computation.exists():
            for f in computation.rglob("*.txt"):
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
    all_edges = []
    all_registries = []  # framework capstone registries (one meta-entry per file)
    all_classes = []      # canonical_classes.py CLASSES dict (constant groupings)
    all_class_edges = []  # canonical_classes.py CLASS_EDGES list (membership + parent-of)

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

        # Relation edges (tagged-link syntax, any file type)
        edges = extract_edges(filepath, text)
        all_edges.extend(edges)

        # Framework registry extraction (capstone authority).
        # Appended AFTER the session-level extractors so that when the same
        # name collides, dedup_by_name sees the framework entry last and wins
        # (its priority-7 source_file also causes collect_files to place it
        # last, but the intra-file append order doesn't matter to dedup).
        if filepath.suffix == ".md" and _is_framework_file(filepath):
            fw = extract_framework_registry(filepath, text)
            if fw.get("registry"):
                all_registries.append(fw["registry"])
            fw_entities = fw.get("entities") or {}
            all_theorems.extend(fw_entities.get("theorems", []))
            all_closed.extend(fw_entities.get("closed_mechanisms", []))
            all_gates.extend(fw_entities.get("gates", []))
            all_open.extend(fw_entities.get("open_channels", []))

    # Also extract equations from computation Python scripts (not in the minutes file list)
    for computation in [COMPUTATIONS_DIR, COMPUTATIONS_ARCHIVE_DIR]:
        if computation.exists():
            for pyf in sorted(computation.glob("*.py")):
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
    provenance = extract_data_provenance(COMPUTATIONS_DIR)
    if COMPUTATIONS_ARCHIVE_DIR.exists():
        provenance.extend(extract_data_provenance(COMPUTATIONS_ARCHIVE_DIR))

    # Researcher directory inventory
    researchers = extract_researcher_index(RESEARCHERS_DIR)

    # Agent persona inventory (.claude/agents/*.md)
    agents = extract_agents()
    agent_slugs = {a["slug"] for a in agents}

    # Session markdown file catalog (sessions/**/*.md). Anchors the
    # 2,496+ edge IDs in <session>:<filename.md> form that previously
    # dangled against data_provenance.
    session_files = extract_session_files()
    # Build lookup maps for the retype pass below
    _sf_by_id = {sf["id"]: sf for sf in session_files}
    _sf_by_path = {sf["path"]: sf for sf in session_files}
    _sf_by_filename = {sf["filename"]: sf for sf in session_files}

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

    # Filter unused researchers — those with no citations AND no
    # matching agent. Papers in the researcher dir without any session
    # citation aren't part of the knowledge graph (the visualizer can't
    # trace anywhere from them). Drop them to avoid phantom anchors.
    _agent_domain_set = {a.get("researcher_domain") for a in agents
                          if a.get("researcher_domain")}
    _filtered_researchers = []
    _dropped_researchers = 0
    for r in researchers:
        d = r.get("domain", "")
        has_citations = (r.get("citation_count") or 0) > 0
        has_agent = d in _agent_domain_set
        if has_citations or has_agent:
            _filtered_researchers.append(r)
        else:
            _dropped_researchers += 1
    if _dropped_researchers:
        print(f"  filtered unused researchers: {_dropped_researchers}")
    researchers = _filtered_researchers

    # Deduplicate (later/higher-priority files win)
    all_theorems = dedup_by_name(all_theorems, "name")
    all_closed = dedup_by_name(all_closed, "name")
    all_gates = dedup_by_name(all_gates, "id")
    all_sessions = dedup_by_name(all_sessions, "id")
    all_open = dedup_by_name(all_open, "name")
    all_equations = dedup_equations(all_equations)

    # Renumber legacy theorem/closed IDs after dedup but BEFORE edge
    # synthesis below. Canonical-namespace IDs (closed_regv_*,
    # closed_gwch_*, proven_atlas07_*, proven_regvii_*)
    # are preserved as-is for cross-rebuild stability; legacy rows get
    # sequential proven_N / closed_N IDs that the synthesis-pass edges
    # then reference. Moved here from below the synthesis (was
    # producing dangling edges because synthesized edges referenced
    # pre-renumber IDs that got rewritten downstream).
    _CANONICAL_CLOSED_PREFIXES = ("closed_regv_", "closed_gwch_")
    _CANONICAL_THEOREM_PREFIXES = ("proven_atlas07_", "proven_regvii_")
    _legacy_t = 1
    for t in all_theorems:
        if any((t.get("id") or "").startswith(p) for p in _CANONICAL_THEOREM_PREFIXES):
            continue
        t["id"] = f"proven_{_legacy_t}"
        _legacy_t += 1
    _legacy_c = 1
    for d in all_closed:
        if any((d.get("id") or "").startswith(p) for p in _CANONICAL_CLOSED_PREFIXES):
            continue
        d["id"] = f"closed_{_legacy_c}"
        _legacy_c += 1

    # S90 cleanup — synthesize upstream edges from entity relational fields.
    # Each closed_mechanism row already carries session + gate_id fields
    # from its source extraction. Materialize those as edges so the
    # chain-of-custody graph can traverse closure -> closing gate -> closing
    # session. Without this step the closures are graph-orphans (verified by
    # tools/_gap_survey.py: only 2.3% of closures had any edge reference).
    # Edges are constructed pre-dedup so dedup_edges can collapse them
    # against any pre-existing edges to the same target.
    _synth_session = 0
    _synth_gate = 0
    _path_session_re = re.compile(
        r"sessions[\\/](?:archive[\\/])?session-(\d+[a-z]?)[\\/]"
    )
    for cm in all_closed:
        cid = cm.get("id") or ""
        sess = (cm.get("session") or "").strip()
        gate_id = (cm.get("gate_id") or "").strip()
        src_file = cm.get("source_file") or ""
        if not cid:
            continue
        # Normalize session to "SXX" / "SXXa" form. Skip multi-session
        # ranges like "17a-24a" and noise like "0.0 (bit-exact)" — let
        # them stay orphans rather than create false edges.
        sess_clean = ""
        sm = re.match(r"^(S\d+[a-z]?|\d+[a-z]?)$", sess)
        if sm:
            sess_clean = sm.group(1)
            if not sess_clean.startswith("S"):
                sess_clean = f"S{sess_clean}"
        # Fallback to source_file path
        if not sess_clean and src_file:
            pm = _path_session_re.search(src_file)
            if pm:
                sess_clean = f"S{pm.group(1)}"
        if sess_clean:
            all_edges.append({
                "id": "",
                "type": "closed_by",
                "source_type": "sessions",
                "source_id": sess_clean,
                "target_type": "closed_mechanisms",
                "target_id": cid,
                "comment": "synthesized: session field on closure row",
                "source_file": src_file,
                "line": 0,
            })
            _synth_session += 1
        if gate_id and re.match(r"^[A-Z][A-Z0-9-]+[A-Za-z0-9]$", gate_id):
            all_edges.append({
                "id": "",
                "type": "closed_by",
                "source_type": "gates",
                "source_id": gate_id,
                "target_type": "closed_mechanisms",
                "target_id": cid,
                "comment": "synthesized: gate_id field on closure row",
                "source_file": src_file,
                "line": 0,
            })
            _synth_gate += 1
    print(f"  synthesized closure upstream edges: "
          f"{_synth_session} session->closed + {_synth_gate} gate->closed")

    # Same pattern for theorems. The `sessions` field on a theorem row
    # is the session(s) where the theorem was proven. When it's empty,
    # fall back to deriving the session from the theorem's source_file
    # path (sessions/(archive/)?session-NN[a-z]?/...).
    _synth_theorem_session = 0
    _path_session_re = re.compile(
        r"(?:sessions[\\/](?:archive[\\/])?|computations[\\/])session-(\d+[a-z]?)[\\/]"
    )
    for t in all_theorems:
        tid = t.get("id") or ""
        sess_raw = (t.get("sessions") or "").strip()
        src_file = t.get("source_file") or ""
        if not tid:
            continue
        sess_clean = ""
        # Primary: parse sessions field
        if sess_raw:
            sm = re.match(r"^(S\d+[a-z]?|\d+[a-z]?)\b", sess_raw)
            if sm:
                sess_clean = sm.group(1)
        # Fallback: derive session from source_file path (sessions/ or computations/)
        if not sess_clean and src_file:
            pm = _path_session_re.search(src_file)
            if pm:
                sess_clean = pm.group(1)
        if not sess_clean:
            continue
        if not sess_clean.startswith("S"):
            sess_clean = f"S{sess_clean}"
        all_edges.append({
            "id": "",
            "type": "anchored_in",
            "source_type": "theorems",
            "source_id": tid,
            "target_type": "sessions",
            "target_id": sess_clean,
            "comment": ("synthesized: theorem's sessions field"
                        if sess_raw else
                        "synthesized: theorem source_file path"),
            "source_file": src_file,
            "line": 0,
        })
        _synth_theorem_session += 1
    print(f"  synthesized theorem->session edges: {_synth_theorem_session}")

    # Open_channels: each has a `session` field. Synthesize
    # session -> open_channel edges so the visualizer can trace which
    # session opened each channel.
    _synth_open = 0
    for oc in all_open:
        # open_channels uses rowid (autoincrement) as DB pk; the JSON
        # representation has a "name" field but no stable id. Use the
        # session+name pair as a derived id for edge endpoints.
        oc_name = (oc.get("name") or "").strip()
        sess_raw = (oc.get("session") or "").strip()
        src_file = oc.get("source_file") or ""
        if not oc_name:
            continue
        sess_clean = ""
        if sess_raw:
            sm = re.match(r"^(S\d+[a-z]?|\d+[a-z]?)\b", sess_raw)
            if sm:
                sess_clean = sm.group(1)
        # Fallback to source_file path
        if not sess_clean and src_file:
            pm = _path_session_re.search(src_file)
            if pm:
                sess_clean = pm.group(1)
        if not sess_clean:
            continue
        if not sess_clean.startswith("S"):
            sess_clean = f"S{sess_clean}"
        # Open-channel IDs in the visualizer/edges use the name as the ID
        all_edges.append({
            "id": "",
            "type": "discussed_in",
            "source_type": "sessions",
            "source_id": sess_clean,
            "target_type": "open_channels",
            "target_id": oc_name,
            "comment": "synthesized: open_channel's session field",
            "source_file": src_file,
            "line": 0,
        })
        _synth_open += 1
    print(f"  synthesized session->open_channel edges: {_synth_open}")

    # Rewrite mis-typed researcher edges to agents. Many attribution
    # harvesters emit source_type='researchers' / target_type='researchers'
    # with the ID set to an agent slug (e.g., 'dirac-antimatter-theorist').
    # Slugs are agents, not researcher-domain entities (those live at
    # 'Antimatter', 'Baptista', etc.). The gap survey showed 2,952 edge
    # endpoints with this mis-typing — closes researchers/agents gap.
    _retyped_src = 0
    _retyped_tgt = 0
    for e in all_edges:
        if e.get("source_type") == "researchers" and e.get("source_id") in agent_slugs:
            e["source_type"] = "agents"
            _retyped_src += 1
        if e.get("target_type") == "researchers" and e.get("target_id") in agent_slugs:
            e["target_type"] = "agents"
            _retyped_tgt += 1
    print(f"  rewrote agent-slug edges from researchers -> agents: "
          f"{_retyped_src} sources + {_retyped_tgt} targets")

    # Semantic correction: closure-source 'bounds' edges are mislabeled.
    # harvest_theorem_closure_edges.py emits 'bounds' for both theorems
    # AND closures when their text mentions a canonical constant by name.
    # For theorems this is correct: a proven theorem CAN bound a constant
    # value. For closed_mechanisms this is wrong: a closure is a killed
    # hypothesis that FAILED to derive the constant; it discusses the
    # constant but doesn't bound it. Retype to 'discussed_in' AND reverse
    # direction so the constant is the source (the subject being
    # discussed) and the closure is the target (the discussion venue).
    # This both fixes the semantic AND honors the user's rule that
    # closures have no downstream.
    _semantic_corrected = 0
    for e in all_edges:
        if (e.get("source_type") == "closed_mechanisms"
                and e.get("type") == "bounds"):
            e["type"] = "discussed_in"
            e["source_type"], e["target_type"] = e["target_type"], "closed_mechanisms"
            e["source_id"], e["target_id"] = e["target_id"], e["source_id"]
            old_comment = e.get("comment") or ""
            e["comment"] = (
                "semantic correction (S90): harvester emitted closure->constant "
                "'bounds' but closure is a killed hypothesis that discusses the "
                "constant rather than bounding it. " + old_comment
            )[:300]
            _semantic_corrected += 1
    if _semantic_corrected:
        print(f"  semantic-corrected closure->constant bounds edges "
              f"(retyped + reversed): {_semantic_corrected}")

    # Retype data_provenance edges that reference session markdown files.
    # The harvested attribution corpus has ~2,500 unique edge IDs of the
    # form '<session>:<filename.md>' or 'sessions/.../file.md' that are
    # mis-typed as 'data_provenance' but actually reference session
    # markdown files. Look each ID up in session_files and retype.
    def _resolve_session_file_id(eid: str):
        """Return the canonical session_files.id matching this edge ID, or None."""
        if not eid:
            return None
        # Direct match (most common: '19:session-19d-baptista-collab.md')
        if eid in _sf_by_id:
            return eid
        # Strip 'data_provenance:' prefix (108 instances per gap audit)
        if eid.startswith("data_provenance:"):
            stripped = eid[len("data_provenance:"):]
            if stripped in _sf_by_path:
                return _sf_by_path[stripped]["id"]
            # Try as filename
            fn = stripped.rsplit("/", 1)[-1]
            if fn in _sf_by_filename:
                return _sf_by_filename[fn]["id"]
        # 'sessions/...' full path form (80 instances)
        if eid.startswith("sessions/"):
            if eid in _sf_by_path:
                return _sf_by_path[eid]["id"]
            fn = eid.rsplit("/", 1)[-1]
            if fn in _sf_by_filename:
                return _sf_by_filename[fn]["id"]
        return None

    _retyped_sf_src = 0
    _retyped_sf_tgt = 0
    for e in all_edges:
        if e.get("source_type") == "data_provenance":
            new_id = _resolve_session_file_id(e.get("source_id", ""))
            if new_id is not None:
                e["source_type"] = "session_files"
                e["source_id"] = new_id
                _retyped_sf_src += 1
        if e.get("target_type") == "data_provenance":
            new_id = _resolve_session_file_id(e.get("target_id", ""))
            if new_id is not None:
                e["target_type"] = "session_files"
                e["target_id"] = new_id
                _retyped_sf_tgt += 1
    print(f"  retyped data_provenance->session_files edges: "
          f"{_retyped_sf_src} sources + {_retyped_sf_tgt} targets")

    # Synthesize session -> data_provenance edges for actual compute
    # scripts in the data_provenance table. Each row's 'session' field
    # identifies the session that ran it. Pre-fix, data_provenance DB
    # rows had 0 incoming edges.
    _synth_dp = 0
    _synth_dp_gate = 0
    _GATE_ID_RE = re.compile(r"^[A-Z][A-Z0-9-]+[A-Za-z0-9]$")
    for p in provenance:
        script = (p.get("script") or "").strip()
        sess_raw = (p.get("session") or "").strip()
        if not script:
            continue
        # Sessions in data_provenance are lowercase like 's23a', 's35', 's88'
        sess_clean = ""
        sm = re.match(r"^s(\d+[a-z]?)$", sess_raw, re.IGNORECASE)
        if sm:
            sess_clean = f"S{sm.group(1).lower()}"
        else:
            sm = re.match(r"^(\d+[a-z]?)$", sess_raw)
            if sm:
                sess_clean = f"S{sm.group(1)}"
        # Fallback: derive from script path (e.g. 'session-23/...' → 'S23')
        if not sess_clean:
            pm = re.search(r"session-(\d+[a-z]?)[\\/]", script)
            if pm:
                sess_clean = f"S{pm.group(1)}"
        if sess_clean:
            all_edges.append({
                "id": "",
                "type": "feeds_into",
                "source_type": "sessions",
                "source_id": sess_clean,
                "target_type": "data_provenance",
                "target_id": script,
                "comment": "synthesized: data_provenance script's session field",
                "source_file": script,
                "line": 0,
            })
            _synth_dp += 1
        # Synthesize script -> gate edges from gates_informed list
        gates_informed = p.get("gates_informed") or []
        if isinstance(gates_informed, str):
            gates_informed = [
                g.strip() for g in gates_informed.split(",") if g.strip()
            ]
        for g in gates_informed:
            g_clean = (g or "").strip()
            if not g_clean or not _GATE_ID_RE.match(g_clean):
                continue
            all_edges.append({
                "id": "",
                "type": "feeds_into",
                "source_type": "data_provenance",
                "source_id": script,
                "target_type": "gates",
                "target_id": g_clean,
                "comment": "synthesized: data_provenance gates_informed list",
                "source_file": script,
                "line": 0,
            })
            _synth_dp_gate += 1
    print(f"  synthesized session->data_provenance edges: {_synth_dp}")
    print(f"  synthesized data_provenance->gate edges: {_synth_dp_gate}")

    # Generic entity -> session_files edge synthesis. Every theorem,
    # closure, gate, open_channel that was extracted from a file under
    # sessions/ gets an "extracted_from" edge to the matching
    # session_file. This connects entities whose source_file is in
    # sessions/ but the per-row session field is empty/malformed (most
    # often: §VII permanent-results-registry theorems with empty
    # sessions field).
    _path_to_sf_id = {sf["path"]: sf["id"] for sf in session_files}
    def _add_extracted_from(entity_type, entity_id, source_file):
        """Emit session_file -> entity edge (file CONTAINS the entity).

        Direction discipline: the session_file is UPSTREAM of the entity
        extracted from it. The file existed first; the entity was parsed
        out of it. For closed_mechanisms specifically the user's rule
        'closed mechanisms should NEVER have downstream' must be honored,
        so closures appear only on the TARGET side here, never source.
        """
        if not entity_id or not source_file:
            return False
        src_norm = source_file.replace("\\", "/")
        sf_id = _path_to_sf_id.get(src_norm)
        if not sf_id:
            return False
        all_edges.append({
            "id": "",
            "type": "discussed_in",
            "source_type": "session_files",
            "source_id": sf_id,
            "target_type": entity_type,
            "target_id": entity_id,
            "comment": "synthesized: session_file contains the entity",
            "source_file": source_file,
            "line": 0,
        })
        return True

    _synth_extract = 0
    for t in all_theorems:
        if _add_extracted_from("theorems", t.get("id"), t.get("source_file") or ""):
            _synth_extract += 1
    for cm in all_closed:
        if _add_extracted_from("closed_mechanisms", cm.get("id"), cm.get("source_file") or ""):
            _synth_extract += 1
    for g in all_gates:
        if _add_extracted_from("gates", g.get("id"), g.get("source_file") or ""):
            _synth_extract += 1
    for oc in all_open:
        if _add_extracted_from("open_channels", oc.get("name") or "", oc.get("source_file") or ""):
            _synth_extract += 1
    print(f"  synthesized entity->session_file (extracted_from) edges: {_synth_extract}")

    # Synthesize sessions -> session_files edges. Each session_file row
    # has a 'session' field; wire it up so every file in sessions/ has
    # at least one incoming edge from its containing session.
    _synth_sf = 0
    for sf in session_files:
        sf_id = sf.get("id") or ""
        sess = (sf.get("session") or "").strip()
        if not sf_id or not sess:
            continue
        sess_clean = f"S{sess}"
        all_edges.append({
            "id": "",
            "type": "discussed_in",
            "source_type": "sessions",
            "source_id": sess_clean,
            "target_type": "session_files",
            "target_id": sf_id,
            "comment": "synthesized: session_file's session field",
            "source_file": sf.get("path", ""),
            "line": 0,
        })
        _synth_sf += 1
    print(f"  synthesized session->session_file edges: {_synth_sf}")

    # Synthesize equations -> containing-file edges. Each equation has
    # a `source_file` field pointing at the markdown/python file it
    # was extracted from. For .py sources, connect to the matching
    # data_provenance script row; for .md sources in sessions/, connect
    # to the matching session_files row. Without this 22,632 equation
    # rows are graph-orphans.
    _dp_scripts: set = {
        (p.get("script") or "").replace("\\", "/").strip()
        for p in provenance if p.get("script")
    }
    # Build outputs-path lookup: every output path → its data_provenance
    # script identifier. Used to match equations extracted from .txt
    # output files (e.g., computations/session-52/s52_hfb_full_output.txt)
    # to the script that produced them.
    _dp_outputs_to_script: dict[str, str] = {}
    for p in provenance:
        script = (p.get("script") or "").strip()
        if not script:
            continue
        outputs = p.get("outputs") or []
        if isinstance(outputs, str):
            outputs = [o.strip() for o in outputs.split(",") if o.strip()]
        for out in outputs:
            o_norm = out.replace("\\", "/").strip()
            if o_norm:
                _dp_outputs_to_script[o_norm] = script
    _synth_eq_dp = 0
    _synth_eq_sf = 0
    _path_session_re2 = re.compile(
        r"sessions[\\/](?:archive[\\/])?session-(\d+[a-z]?)[\\/]"
    )
    for eq in all_equations:
        eq_id = (eq.get("id") or "").strip()
        eq_src = (eq.get("source_file") or "").strip()
        if not eq_id or not eq_src:
            continue
        eq_src_n = eq_src.replace("\\", "/")
        # Case A: .py file → data_provenance match by suffix
        if eq_src_n.endswith(".py"):
            matched_script = None
            for ds in _dp_scripts:
                if eq_src_n.endswith(ds) or ds.endswith(eq_src_n):
                    matched_script = ds
                    break
            if matched_script:
                all_edges.append({
                    "id": "",
                    "type": "depends_on",
                    "source_type": "equations",
                    "source_id": eq_id,
                    "target_type": "data_provenance",
                    "target_id": matched_script,
                    "comment": "synthesized: equation's .py source matches data_provenance",
                    "source_file": eq_src,
                    "line": 0,
                })
                _synth_eq_dp += 1
            continue
        # Case A2: .txt output file → match against data_provenance.
        # Equations extracted from computations/session-NN/*_output.txt
        # should link to the script that produced that .txt. Try in order:
        # (1) direct outputs match, (2) suffix outputs match, (3) name-stem
        # heuristic (strip _output suffix and look for matching .py script).
        if eq_src_n.endswith(".txt"):
            matched_script = _dp_outputs_to_script.get(eq_src_n)
            if not matched_script:
                # Try suffix matching against outputs lookup
                for out_path, script in _dp_outputs_to_script.items():
                    if eq_src_n.endswith(out_path) or out_path.endswith(eq_src_n):
                        matched_script = script
                        break
            if not matched_script:
                # Name-stem heuristic: 'computations/session-52/s52_X_output.txt'
                # → try 'session-52/s52_X.py' against _dp_scripts. Also handle
                # _log, _verdicts, _out, _results, _gate_verdicts suffixes
                # commonly used for various output kinds.
                base = eq_src_n.rsplit("/", 1)[-1]
                stem = ""
                for suffix in (
                    "_output.txt", "_log.txt", "_out.txt", "_results.txt",
                    "_gate_verdicts.txt", "_verdicts.txt", ".txt"
                ):
                    if base.endswith(suffix):
                        stem = base[:-len(suffix)]
                        break
                if stem:
                    candidate_py = f"{stem}.py"
                    for ds in _dp_scripts:
                        if ds.endswith(f"/{candidate_py}") or ds == candidate_py:
                            matched_script = ds
                            break
                    # Also try stem WITHOUT trailing letter (s29b_gate_verdicts
                    # → s29_gate_verdicts → script s29; or just s29* prefix).
                    if not matched_script and stem:
                        # Try matching stem prefix (any DP script in same session).
                        # Strip BOTH the trailing letter (sub-session) AND
                        # check both forms — session-29b/ and session-29/.
                        sm = re.match(r"^s(\d+)([a-z]?)", base, re.IGNORECASE)
                        if sm:
                            sess_num = sm.group(1)
                            sess_letter = sm.group(2)
                            candidate_dirs = []
                            if sess_letter:
                                candidate_dirs.append(f"session-{sess_num}{sess_letter}/")
                                candidate_dirs.append(f"session-{sess_num}{sess_letter}\\")
                            candidate_dirs.append(f"session-{sess_num}/")
                            candidate_dirs.append(f"session-{sess_num}\\")
                            for ds in _dp_scripts:
                                if any(cd in ds for cd in candidate_dirs):
                                    matched_script = ds
                                    break
            if matched_script:
                all_edges.append({
                    "id": "",
                    "type": "depends_on",
                    "source_type": "equations",
                    "source_id": eq_id,
                    "target_type": "data_provenance",
                    "target_id": matched_script,
                    "comment": "synthesized: equation's .txt source matches data_provenance script (stem heuristic)",
                    "source_file": eq_src,
                    "line": 0,
                })
                _synth_eq_dp += 1
            continue
        # Case B: any file in sessions/ that has a session_file row.
        # Try path-direct match first (handles framework/, session-plan/,
        # root-level files that don't fit the session-NN/ pattern).
        sf_id = None
        if eq_src_n in _sf_by_path:
            sf_id = _sf_by_path[eq_src_n]["id"]
        else:
            # Try session-NN/ extraction (the older pattern)
            pm = _path_session_re2.search(eq_src_n.replace("/", "\\"))
            if not pm:
                pm = _path_session_re2.search(eq_src_n)
            if pm:
                session = pm.group(1)
                filename = eq_src_n.rsplit("/", 1)[-1]
                candidate = f"{session}:{filename}"
                if candidate in _sf_by_id:
                    sf_id = candidate
        if not sf_id:
            continue
        all_edges.append({
            "id": "",
            "type": "depends_on",
            "source_type": "equations",
            "source_id": eq_id,
            "target_type": "session_files",
            "target_id": sf_id,
            "comment": "synthesized: equation's source matches session_file",
            "source_file": eq_src,
            "line": 0,
        })
        _synth_eq_sf += 1
    print(f"  synthesized equation->data_provenance edges: {_synth_eq_dp}")
    print(f"  synthesized equation->session_file edges: {_synth_eq_sf}")

    # Synthesize agent -> researcher edges from each agent's
    # researcher_domain field. This wires up the 39 researcher entities
    # (currently 0% edge coverage) by giving them upstream edges from the
    # agents informed by their corpus. The edge type 'grounds' (existing
    # canonical type) reads as "researcher's corpus grounds the agent's
    # methodology" — so the edge is researcher -> agent (researcher is
    # the foundational source; agent is the derived persona).
    _synth_agent_researcher = 0
    researcher_domains_set = {(r.get("domain") or "") for r in researchers}
    for a in agents:
        slug = a.get("slug") or ""
        domain = a.get("researcher_domain") or ""
        if not slug or not domain:
            continue
        if domain not in researcher_domains_set:
            continue  # agent references a domain we don't have (e.g., 'inflation-topic')
        all_edges.append({
            "id": "",
            "type": "grounds",
            "source_type": "researchers",
            "source_id": domain,
            "target_type": "agents",
            "target_id": slug,
            "comment": "synthesized: agent's researcher_domain field",
            "source_file": a.get("source_file", ""),
            "line": 0,
        })
        _synth_agent_researcher += 1
    print(f"  synthesized agent<-researcher edges: {_synth_agent_researcher}")

    # Synthesize researcher -> session edges from the cited_in_sessions
    # field on each researcher row. Researchers without an agent file
    # but with citation history (Inflation, Lost-Treasures, RF-Antimatter)
    # were graph-orphans; this wires them to the sessions that cited
    # their papers.
    _synth_rs = 0
    for r in researchers:
        domain = r.get("domain") or ""
        sess_list = r.get("cited_in_sessions") or []
        if not domain:
            continue
        # cited_in_sessions may be a list (from extraction) or a
        # comma-string (from the DB schema's TEXT serialization).
        if isinstance(sess_list, str):
            sess_list = [s.strip() for s in sess_list.split(",") if s.strip()]
        for sess in sess_list:
            sess = sess.strip()
            sm = re.match(r"^(\d+[a-zA-Z]?)$", sess)
            if not sm:
                continue
            all_edges.append({
                "id": "",
                "type": "cited_in",
                "source_type": "researchers",
                "source_id": domain,
                "target_type": "sessions",
                "target_id": sm.group(1),
                "comment": "synthesized: researcher's cited_in_sessions field",
                "source_file": r.get("index_file") or "",
                "line": 0,
            })
            _synth_rs += 1
    print(f"  synthesized researcher->session edges: {_synth_rs}")

    # Synthesize session -> gate edges for every gate with a non-empty
    # `session` field. Covers gates that the harvested attribution corpus
    # missed (e.g., S91-* forward-looking gates, S84-G-AUDIT).
    _synth_g = 0
    for g in all_gates:
        gid = g.get("id") or ""
        sess_raw = (g.get("session") or "").strip()
        if not gid or not sess_raw:
            continue
        sm = re.match(r"^(S?\d+[a-z]?|\d+[a-z]?)\b", sess_raw, re.IGNORECASE)
        if not sm:
            continue
        sess_clean = sm.group(1).lstrip("S").lstrip("s").lower()
        all_edges.append({
            "id": "",
            "type": "anchored_in",
            "source_type": "gates",
            "source_id": gid,
            "target_type": "sessions",
            "target_id": sess_clean,
            "comment": "synthesized: gate's session field",
            "source_file": g.get("source_file", ""),
            "line": 0,
        })
        _synth_g += 1
    print(f"  synthesized gate->session edges: {_synth_g}")

    # Synthesize session -> constant edges from constants WITH a session
    # field in their PROVENANCE entry. The canonical_constants_provenance_edges
    # harvester emits gate->constant edges but not session->constant.
    # This synthesis catches constants like ns_framework_err (S81) that
    # have provenance but no edges.
    _synth_const = 0
    # Import canonical_constants locally — this module is normally
    # imported in knowledge_db.py for the constants-table sync, but
    # extract_entities.py doesn't have a module-level import for it.
    import sys as _sys
    _sys.path.insert(0, str(COMPUTATIONS_DIR / "_shared"))
    try:
        import canonical_constants as CC  # noqa: WPS433
    except Exception:  # noqa: BLE001
        CC = None
    if CC is not None:
        prov_dict = getattr(CC, "PROVENANCE", {}) or {}
        for name, prov in (prov_dict.items() if isinstance(prov_dict, dict) else []):
            if not isinstance(prov, dict):
                continue
            sess = (prov.get("session") or "").strip()
            if not sess:
                continue
            sm = re.match(r"^S?(\d+[a-z]?)$", sess, re.IGNORECASE)
            if not sm:
                continue
            sess_clean = sm.group(1).lower()
            all_edges.append({
                "id": "",
                "type": "anchored_in",
                "source_type": "constants",
                "source_id": name,
                "target_type": "sessions",
                "target_id": sess_clean,
                "comment": "synthesized: constant's PROVENANCE session field",
                "source_file": "computations/_shared/canonical_constants.py",
                "line": 0,
            })
            _synth_const += 1
    print(f"  synthesized constant->session edges: {_synth_const}")

    # Synthesize registries -> session_file edges. The registries table
    # has one meta-entry per framework file (sessions/framework/*.md).
    # Each framework session_file orphan can be wired to its matching
    # registry by source_file path. This connects the 45 framework-docs
    # orphans without inventing synthetic anchors.
    _synth_reg_sf = 0
    # Use the registries.id (e.g. 'registry_21cm-science-case') as the
    # edge source_id since that's the table's primary key. Earlier
    # iteration used registry_id (without the 'registry_' prefix) which
    # didn't match the DB key.
    _reg_by_source = {
        (r.get("source_file") or "").replace("\\", "/"): r.get("id")
        for r in all_registries
        if r.get("source_file") and r.get("id")
    }
    for sf in session_files:
        sf_id = sf.get("id") or ""
        sf_path = (sf.get("path") or "").replace("\\", "/")
        if not sf_id or not sf_path:
            continue
        registry_id = _reg_by_source.get(sf_path)
        if not registry_id:
            continue
        all_edges.append({
            "id": "",
            "type": "anchored_in",
            "source_type": "registries",
            "source_id": registry_id,
            "target_type": "session_files",
            "target_id": sf_id,
            "comment": "synthesized: registry meta-entry's source_file matches",
            "source_file": sf_path,
            "line": 0,
        })
        _synth_reg_sf += 1
    print(f"  synthesized registry->session_file edges: {_synth_reg_sf}")

    # Normalize session IDs across ALL edges (synthesized + harvested).
    # Sessions table stores bare numeric form ('17a', '88'); some
    # harvesters + synthesis steps emit 'S'-prefixed form ('S17a', 'S88').
    # Strip the leading 'S' so set-intersection in the gap survey
    # actually matches. Must run AFTER all synthesis steps; if it runs
    # before, downstream syntheses that re-introduce 'S' prefix leak
    # past the normalization.
    _norm_session_re = re.compile(r"^S(\d+[a-z]?)$", re.IGNORECASE)
    _normalized = 0
    for e in all_edges:
        if e.get("source_type") == "sessions":
            sid = (e.get("source_id") or "").strip()
            m = _norm_session_re.match(sid)
            if m:
                e["source_id"] = m.group(1)
                _normalized += 1
        if e.get("target_type") == "sessions":
            tid = (e.get("target_id") or "").strip()
            m = _norm_session_re.match(tid)
            if m:
                e["target_id"] = m.group(1)
                _normalized += 1
    print(f"  normalized session-edge IDs (stripped S prefix): {_normalized}")

    all_edges = dedup_edges(all_edges)

    # Final-pass orphan filter: drop entities whose ID never appears as
    # an edge source or target. After all synthesis + retypes, anything
    # still orphan is genuinely unreferenced — for the visualizer goal
    # ("all anchors cross-referenced"), drop them rather than display
    # disconnected anchors. Applies to entity types where some rows may
    # exist as files / table rows but lack any incident edge.
    _referenced: dict[str, set] = {}
    for e in all_edges:
        st, sid = e.get("source_type"), e.get("source_id")
        tt, tid = e.get("target_type"), e.get("target_id")
        if st and sid:
            _referenced.setdefault(st, set()).add(sid)
        if tt and tid:
            _referenced.setdefault(tt, set()).add(tid)

    def _filter_orphans(items, key, type_name):
        ref = _referenced.get(type_name, set())
        kept = [i for i in items if i.get(key) in ref]
        dropped = len(items) - len(kept)
        if dropped:
            print(f"  final-pass: dropped {dropped} orphan {type_name}")
        return kept

    # Apply to entity tables where orphans are legitimate to drop (no
    # one references them; they're filesystem entries with no graph
    # connectivity). Skip core entity types (theorems, closures, gates,
    # sessions, agents, researchers, constants) — those already passed
    # 100% via synthesis or were filtered at extraction.
    all_equations = _filter_orphans(all_equations, "id", "equations")
    provenance = _filter_orphans(provenance, "script", "data_provenance")
    session_files = _filter_orphans(session_files, "id", "session_files")
    all_open = _filter_orphans(all_open, "name", "open_channels")

    # Strict dedup on open_channels: dedup_by_name's prefix-matching
    # allowed some exact-name duplicates through (n_s and α_s each
    # appearing 2x). The gap survey counts these as orphans because
    # the set intersection treats duplicates as single. Collapse here
    # so the DB row count matches the distinct-name count.
    _seen_oc: set = set()
    _open_unique = []
    for oc in all_open:
        n = (oc.get("name") or "").strip()
        if n in _seen_oc:
            continue
        _seen_oc.add(n)
        _open_unique.append(oc)
    if len(_open_unique) < len(all_open):
        print(f"  collapsed open_channel duplicates: "
              f"{len(all_open) - len(_open_unique)}")
    all_open = _open_unique

    # Enrich gates.data_files from the inverse of data_provenance.gates_informed.
    # Rationale: the per-file extractor only catches script references in the
    # immediate text vicinity of a gate row (<= 200 chars) or section, which
    # misses the common pattern where the gate is pre-registered in a session
    # plan and actually evaluated by a script that never sits next to the
    # gate block. data_provenance has 1324+ scripts carrying explicit
    # `# gates_informed: X, Y, Z` annotations — inverting that map is the
    # authoritative gate->script linkage the Level 3 runner needs.
    gate_to_scripts: dict[str, list[str]] = {}
    for p in provenance:
        script = p.get("script") or ""
        gi_list = p.get("gates_informed") or []
        if not script or not gi_list:
            continue
        # gates_informed is a list of gate IDs
        for g_raw in gi_list:
            g = (g_raw or "").strip()
            if not g:
                continue
            lst = gate_to_scripts.setdefault(g, [])
            if script not in lst:
                lst.append(script)

    enriched_gates_count = 0  # (local)
    for gate in all_gates:
        gid = (gate.get("id") or "").strip()
        if not gid:
            continue
        # Try exact match, and also case-insensitive / prefix match for
        # robustness (gate IDs are inconsistently cased across sources).
        candidates: list[str] = []
        if gid in gate_to_scripts:
            candidates = list(gate_to_scripts[gid])
        else:
            for other_gid, scripts in gate_to_scripts.items():
                if other_gid.upper() == gid.upper():
                    candidates = list(scripts)
                    break
        if not candidates:
            continue
        existing = gate.get("data_files") or []
        merged: list[str] = list(existing)
        for s in candidates:
            if s and s not in merged:
                merged.append(s)
        if merged != existing:
            gate["data_files"] = merged[:20]
            enriched_gates_count += 1

    if enriched_gates_count:
        print(f"  enriched gates.data_files via data_provenance inverse: "
              f"{enriched_gates_count} gates")

    # (ID renumbering was moved earlier — runs immediately after
    # dedup_by_name so synthesized edges reference stable IDs.)

    # Dedup framework registries by EXACT registry_id (not dedup_by_name's
    # prefix-matching rule, which collapses distinct files like
    # `framework-mechanism-discussion.md` and its `*-dirac-collab.md` /
    # `*-einstein-collab.md` siblings when their stems share a long prefix).
    # Registries are filename-derived identifiers; prefix-matching is wrong.
    _reg_seen: dict[str, dict] = {}
    for _r in all_registries:
        _rid = (_r.get("registry_id") or "").strip()
        if not _rid:
            continue
        # Later-in-iteration wins on exact match (same priority-7 framework
        # files have filesystem-walk order; rare exact-match collisions
        # indicate a duplicate file and the latter wins).
        _reg_seen[_rid] = _r
    all_registries = list(_reg_seen.values())

    # Canonical classes (S86+) — single-file source, extracted once per build.
    # These are NOT walked from the file iterator above (they live in
    # computations/_shared/canonical_classes.py exclusively); calling
    # extract_classes here mirrors the dedicated audit path used by
    # audit_canonical_constants.
    cls, cls_edges = extract_classes(SHARED_DIR)
    all_classes.extend(cls)
    all_class_edges.extend(cls_edges)

    # Canonical constants entity table — sister to extract_classes above.
    # Walks computations/_shared/canonical_constants.py directly and joins with
    # the PROVENANCE dict. Rows without PROVENANCE entries keep null
    # session/source/gate (backfill worklist).
    all_constants = extract_canonical_constants_entities()

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
        "agents": agents,
        "session_files": session_files,
        "equations": all_equations,
        "edges": all_edges,
        "registries": all_registries,
        "classes": all_classes,
        "class_edges": all_class_edges,
        "constants": all_constants,
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
        "registries": "registry_id",
        "classes": "id",
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
        audit_results = audit_canonical_constants(COMPUTATIONS_DIR) + audit_canonical_constants(COMPUTATIONS_ARCHIVE_DIR)
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
        audit_results = audit_canonical_constants(COMPUTATIONS_DIR) + audit_canonical_constants(COMPUTATIONS_ARCHIVE_DIR)
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
                     "probability_trajectory", "open_channels", "equations",
                     "edges", "registries", "classes", "class_edges"]:
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
            elif key in ("edges",):
                combined = dedup_edges(combined)
            elif key in ("registries",):
                # Strict equality dedup — see build_index() note on why
                # prefix-matching would collapse sibling Collab files.
                _reg_seen: dict[str, dict] = {}
                for _r in combined:
                    _rid = (_r.get("registry_id") or "").strip()
                    if _rid:
                        _reg_seen[_rid] = _r
                combined = list(_reg_seen.values())
            elif key in ("classes",):
                # Source is single-file (canonical_classes.py); dedup_by_name
                # on id keeps the latest extraction (last-wins semantics).
                combined = dedup_by_name(combined, "id")
            elif key in ("class_edges",):
                # No natural id; dedup by (type, src, tgt, role) tuple — the
                # uniqueness key of an edge in canonical_classes.py.
                _ce_seen: set = set()
                _out: list[dict] = []
                for _e in combined:
                    _k = (_e.get("type"), _e.get("src"),
                          _e.get("tgt"), _e.get("role"))
                    if _k in _ce_seen:
                        continue
                    _ce_seen.add(_k)
                    _out.append(_e)
                combined = _out
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

    # Canonical constants audit (S34+ enforcement).
    # The full audit_results list contains both compliance checkmarks (IMPORT_OK,
    # ~99.5% of rows) AND real violations (POTENTIAL_HARDCODE, TAU_FOLD=0.19).
    # We use the FULL list for the on-screen audit printout (so the user sees
    # compliance counts), but persist ONLY the violation rows into the index —
    # the IMPORT_OK rows are positive-acknowledgement noise that wastes index
    # space and makes the table unsearchable.
    print()
    audit_results = audit_canonical_constants(COMPUTATIONS_DIR) + audit_canonical_constants(COMPUTATIONS_ARCHIVE_DIR)
    index["constants_audit"] = [
        r for r in audit_results
        if isinstance(r, dict) and r.get("pattern") != "IMPORT_OK"
    ]
    # Re-write index with (filtered) audit results included
    write_index(index, output_path)
    print_constants_audit(audit_results)

    print()
    print_stats(index)


if __name__ == "__main__":
    main()
