#!/usr/bin/env python3
r"""
_registry_landing_audit.py — Registry-landing audit script (S90 W1-1 landing).

Purpose: detect structural conflations between registry-anchor declarations and
producing-script implementations on permanent-results-registry.md §VII entries.

Class-(g) detector: REGISTRY-ANCHOR-ROUTE-A-VS-ROUTE-B-CONFLATION
- Reads a §VII slot's ANCHOR-{N} lines from sessions/permanent-results-registry.md
- Extracts session+gate citation + route-claim string (Route-A / Route-B / Route-C)
- Globs computations/session-{N}/s{N}_w{wave}_{item}_*.py for the producing script
- Reads the script's docstring header for `^#\s*(Route|Derivation):\s*(.+)$` regex match
- Compares declared_route vs actual_route per static-string compare

Diagnostic outcomes (severity per SOURCE-RECONCILIATION 4-band calibration in
`.claude/rules/epistemic-discipline.md §"Source Reconciliation"`):
  (i)   script_not_found_AND_route_claimed   → S1 MANDATORY (HARD-HALT band)
  (ii)  route_mismatch                       → S2 advisory   (drift band)
  (iii) route_declaration_absent_in_producing_script → S2 advisory (W5a-44 pattern)
  (iv)  PASS                                 → NONE (commutativity verified)
  (v)   no_route_claim                       → NONE (registry makes no route claim)

Calibration corpus K=1 (S90 W1-1 landing, 2026-05-12):
  §VII.AN (S88 W5a-37) — V-anchor "S82 W3-9 single-pole Mellin closure" (Route-A
  claim); cited script computations/session-82/s82_w3_9_as_adjacent_obs.py exists
  but lacks explicit `# Route:` / `# Derivation:` header → fires
  route_declaration_absent_in_producing_script at S2 advisory. Cross-link to
  W5a-44 NEGATIVE-CALIBRATION FAIL audit_sha256 =
  c092fe1bff9ab66928aa9c545a3a22776f847053af40b5d2814db0143d21f64b which
  empirically determined the script implements Route-B (n_s² − 1 identity at
  line 203) per §VII.AN-CORRIGENDUM (Option-A successor at registry line 16791).

Provenance: S90 W1-1 (gen-physicist orchestrator-direct-write, 2026-05-12).
Plan: sessions/session-plan/session-90-plan-w1.md §W1-1.

Cross-references:
- `.claude/rules/substrate-first-canonical-sourcing.md §(i)` — K=4 NEGATIVE-CALIBRATION corpus
- `.claude/rules/gate-verdicts.md §"Option A — sig_5 remediation pathway"` — supersedes-tag protocol
- `.claude/rules/registry-landing.md §"SOURCE-DOUBLE-CITE-CO-PRIMARY"` — anchor-structure rule
- `.claude/rules/epistemic-discipline.md §"Source Reconciliation"` — 4-band severity calibration
- `.claude/rules/cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` — MANDATORY-K=3

Substrate framing per `phononic-framing.md §"IS Space, Not IN Space"`:
  the §VII registry entry IS the methodology-layer F-image of the substrate-IS
  derivation chain (substrate-distance pole → producing script's actual route
  → registry-anchor declared route); Class-(g) audit verifies F-image
  commutativity. Direction: substrate-IS derivation chain → producing-script
  body (F-image at methodology layer) → registry-anchor text (F-image at audit
  layer). Inverting (treating registry-anchor as authoritative against
  producing-script body) is forbidden per substrate-prior discipline.
"""

import json
import re
import sys
from pathlib import Path
from typing import Optional

# Canonical-constants import per `computations/_shared/CLAUDE.md` MANDATORY
# discipline. This audit script does not actively use any framework constants,
# but the import satisfies the discipline declared at the project rule level.
SHARED_DIR = Path(__file__).resolve().parent  # (local) — script-dir resolver
sys.path.insert(0, str(SHARED_DIR))
try:
    from canonical_constants import *  # noqa: F401,F403,E402
except Exception as e:
    print(f"ERROR: canonical_constants.py import failed: {e}", file=sys.stderr)
    raise

# =====================================================================
# Route-claim keyword set (registry V-anchor / C-anchor declaration patterns)
# =====================================================================

ROUTE_CLAIM_KEYWORDS = {
    'Route-A': r'\b(Route[\s\-]A|single[\s\-]pole|Mellin\s+closure|primary[\s\-]pole)\b',
    'Route-B': r'\b(Route[\s\-]B|double[\s\-]pole|n_s\s*[\^²]\s*[−\-]\s*1|n_s\^2\s*[−\-]\s*1|secondary[\s\-]pole)\b',
    'Route-C': r'\b(Route[\s\-]C|tertiary[\s\-]pole)\b',
}

# Docstring route-header regex (case-insensitive, multi-line)
ROUTE_HEADER_RE = re.compile(
    r'^\s*#\s*(?:Route|Derivation)\s*:\s*(.+?)\s*$',
    re.IGNORECASE | re.MULTILINE,
)

# ANCHOR-{N} line regex — captures session+gate citation + claim text
ANCHOR_LINE_RE = re.compile(
    r'^ANCHOR-(\d+)\s*\(([^)]+)\)\s*:\s*(S\d+\s+W[0-9a-z]+-\d+)\s+(.+?)(?:;|$)',
    re.MULTILINE,
)


# =====================================================================
# Class-(h) state-history label pattern set + parse-tree expansion detector
# (S90 W1-8 extension; per `.claude/rules/registry-landing.md §"Parse-Tree
# Expansion Pre-Registration for new §VII entries (S90 W-3 CF-R1-3)"`)
#
# Provenance:
#   - §W1-7 sub-clause baseline pattern set (7 patterns; landed at
#     `.claude/rules/cross-pillar-bridge-anatomy.md §"Observable-Naming-History
#     vs Parse-Tree-Structure (S90 W-3 CF-LZ-5 sub-clause)"`,
#     audit_sha256=cee6a4da1c4ea564aa35768fe3e9aa663e137631a60ad77dd97abdde82d70943).
#   - lizzi-spectral-functional-theorist CO-SIGN-WITH-NOTES forward expansions
#     (3 additions: Bogoliubov-(state|amplitude|coefficient), Delta_M / Δ_M,
#     α_s_route_[0-9]+ regex generalization). In-session incorporation per
#     `feedback_fix-in-session-never-defer.md` instead of S91+ deferral.
# =====================================================================

STATE_HISTORY_LABEL_PATTERNS = [
    # §W1-7 sub-clause baseline (7 patterns)
    r'n_a\^GGE',
    r'n_a_GGE',
    r'state\.GGE\b',
    r'Bogoliubov\(',
    r'\bGGE-state\b',
    r'α_s_canonical',
    r'α_s_route_3',
    # lizzi CO-SIGN-WITH-NOTES forward expansions (3 additions; S90 W1-8 in-session
    # incorporation per `feedback_fix-in-session-never-defer.md`):
    r'\bBogoliubov-(state|amplitude|coefficient)\b',  # closes §(1)/§(3) gap
    r'Δ_M\b',  # actively used in sessions/session-plan/session-90-plan-w7.md line 103
    r'\bDelta_M\b',  # ASCII variant of Δ_M
    r'α_s_route_[0-9]+',  # regex generalization (covers route_3, route_4, ...)
]
STATE_HISTORY_RE = re.compile('|'.join(STATE_HISTORY_LABEL_PATTERNS))

# Parse-tree expansion presence detection pattern set.
# §W1-7 sub-clause baseline (formal block markers) + S90 W1-8 forward-looking
# enrichment (clause-(e)-style references that match the actual canonical
# §VII.U.2 parse-tree decision wording).
PARSE_TREE_EXPANSION_MARKERS = [
    # §W1-7 baseline (formal block markers — exact-string match)
    r'Parse-tree expansion:',
    r'parse_tree_expansion:',
    r'## Parse-tree',
    r'### Parse-tree',
    # S90 W1-8 enrichment (canonical §VII.U.2-style inline references):
    r'\bparse-tree (decision|level|reduction|expansion)\b',
    r'\bParse-tree (decision|level|reduction|expansion)\b',
    r'\bparse-tree\b',  # broadest fallback (catches any literal mention)
]
PARSE_TREE_EXPANSION_RE = re.compile(
    '|'.join(PARSE_TREE_EXPANSION_MARKERS),
    re.IGNORECASE,
)


def classify_registry_route(claim_text: str) -> Optional[str]:
    """Map registry V/C-anchor claim text to a canonical Route label."""
    for route_label, pattern in ROUTE_CLAIM_KEYWORDS.items():
        if re.search(pattern, claim_text, re.IGNORECASE):
            return route_label
    return None


def find_producing_script(session_label: str, gate_label: str, repo_root: Path) -> Optional[Path]:
    """
    Glob computations/session-{N}/s{N}_w{wave}_{item}_*.py given 'S82' and 'W3-9'.
    Returns first match or None.
    """
    n_match = re.match(r'S(\d+)', session_label)
    g_match = re.match(r'W([0-9a-z]+)-(\d+)', gate_label)
    if not n_match or not g_match:
        return None
    sess = n_match.group(1)
    wave = g_match.group(1)
    item = g_match.group(2)
    pattern = f'computations/session-{sess}/s{sess}_w{wave}_{item}_*.py'
    candidates = list(repo_root.glob(pattern))
    if candidates:
        return candidates[0]
    # Fallback: search alternate root patterns (e.g., no item-number suffix)
    alt_pattern = f'computations/session-{sess}/s{sess}_w{wave}*.py'
    alt_candidates = list(repo_root.glob(alt_pattern))
    return alt_candidates[0] if alt_candidates else None


def read_script_route_header(script_path: Path) -> Optional[str]:
    """Return route declaration from `# Route:` / `# Derivation:` header line."""
    if not script_path.exists():
        return None
    text = script_path.read_text(encoding='utf-8', errors='ignore')
    # Only scan the first 60 lines (docstring header)
    head = '\n'.join(text.splitlines()[:60])
    m = ROUTE_HEADER_RE.search(head)
    return m.group(1).strip() if m else None


def detect_class_g(
    registry_block: str,
    registry_slot: str,
    repo_root: Path,
) -> dict:
    """
    Class-(g) REGISTRY-ANCHOR-ROUTE-A-VS-ROUTE-B-CONFLATION detector.

    Args:
      registry_block:  the text of the §VII slot's block (between ## headers)
      registry_slot:   the slot label (e.g. '§VII.AN')
      repo_root:       project repo root for glob resolution

    Returns:
      dict with keys: gate, registry_slot, anchors[], diagnostic, severity,
                      remediation, has_class_g_flag (bool)
    """
    result = {
        'gate': 'S90-VII-AN-AUDIT-SCRIPT-REGISTRY-ANCHOR-RECONCILIATION-EXTENSION',
        'audit_class': 'Class-(g) REGISTRY-ANCHOR-ROUTE-A-VS-ROUTE-B-CONFLATION',
        'registry_slot': registry_slot,
        'anchors': [],
        'diagnostic': 'PASS',
        'severity': 'NONE',
        'remediation': 'No remediation required.',
        'has_class_g_flag': False,
    }

    for m in ANCHOR_LINE_RE.finditer(registry_block):
        anchor_n, anchor_role, session_gate, claim_text = m.groups()
        parts = session_gate.split()
        session_label = parts[0]
        gate_label = parts[1] if len(parts) > 1 else ''

        route_claimed = classify_registry_route(claim_text)
        script_path = find_producing_script(session_label, gate_label, repo_root)
        script_found = script_path is not None and script_path.exists()
        actual_route = read_script_route_header(script_path) if script_found else None

        anchor_record = {
            'anchor': f'ANCHOR-{anchor_n}',
            'role': anchor_role.strip(),
            'session_gate_citation': session_gate,
            'claim_text_excerpt': claim_text[:80],
            'route_claimed': route_claimed,
            'script_path': str(script_path) if script_path else None,
            'script_found': script_found,
            'actual_route_header': actual_route,
            'anchor_diagnostic': 'PASS',
            'anchor_severity': 'NONE',
        }

        # Severity routing per SOURCE-RECONCILIATION 4-band calibration
        if route_claimed is None:
            anchor_record['anchor_diagnostic'] = 'no_route_claim'
            result['anchors'].append(anchor_record)
            continue

        if not script_found:
            anchor_record['anchor_diagnostic'] = 'script_not_found_AND_route_claimed'
            anchor_record['anchor_severity'] = 'S1'
            if _severity_rank(result['severity']) < _severity_rank('S1'):
                result['diagnostic'] = 'script_not_found_AND_route_claimed'
                result['severity'] = 'S1'
                result['has_class_g_flag'] = True
                result['remediation'] = (
                    f'Route to mack-cosmic-bridge sole-writer (per feedback_mack-bridge-role.md) '
                    f'for {registry_slot} registry-text reconciliation. Cited producing script for '
                    f'{session_gate} not found at expected computations/session-{session_label[1:]}/ '
                    f'path; either correct registry citation or supply producing script.'
                )
            result['anchors'].append(anchor_record)
            continue

        if actual_route is None:
            # Script exists but no explicit route header → W5a-44 pattern
            anchor_record['anchor_diagnostic'] = 'route_declaration_absent_in_producing_script'
            anchor_record['anchor_severity'] = 'S2'
            if _severity_rank(result['severity']) < _severity_rank('S2'):
                result['diagnostic'] = 'route_declaration_absent_in_producing_script'
                result['severity'] = 'S2'
                result['has_class_g_flag'] = True
                result['remediation'] = (
                    f'Producing script {script_path} exists but lacks explicit `# Route:` or '
                    f'`# Derivation:` header. Registry {anchor_record["anchor"]} claims '
                    f'{route_claimed} for {registry_slot}; cannot verify commutativity at the '
                    f'docstring layer. Recommend adding header to script OR cross-link to '
                    f'W5a-44 NEGATIVE-CALIBRATION '
                    f'(audit_sha256=c092fe1bff9ab66928aa9c545a3a22776f847053af40b5d2814db0143d21f64b) '
                    f'which empirically determined the actual route via AST-parse audit.'
                )
            result['anchors'].append(anchor_record)
            continue

        # Header present — compare declared_route vs actual_route
        actual_normalized = classify_registry_route(actual_route) or actual_route
        if route_claimed != actual_normalized:
            anchor_record['anchor_diagnostic'] = 'route_mismatch'
            anchor_record['anchor_severity'] = 'S2'
            if _severity_rank(result['severity']) < _severity_rank('S2'):
                result['diagnostic'] = 'route_mismatch'
                result['severity'] = 'S2'
                result['has_class_g_flag'] = True
                result['remediation'] = (
                    f'Registry {anchor_record["anchor"]} declares {route_claimed}; '
                    f'producing script {script_path} declares {actual_normalized}. '
                    f'Class-(g) ROUTE-A-VS-ROUTE-B-CONFLATION fires. Route to '
                    f'mack-cosmic-bridge sole-writer for registry-text reconciliation OR '
                    f'append Option-A `supersedes=<old-audit-sha>` successor per '
                    f'gate-verdicts.md §"Option A — sig_5 remediation pathway".'
                )
        else:
            anchor_record['anchor_diagnostic'] = 'PASS'

        result['anchors'].append(anchor_record)

    return result


def _severity_rank(severity: str) -> int:
    return {'NONE': 0, 'S2': 1, 'S1': 2}.get(severity, 0)


def extract_registry_block(registry_md_text: str, slot_label: str) -> str:
    """Extract a `## §VII.{slot}` block from registry text up to the next `##` header."""
    # Slot pattern handles ## §VII.{slot} variations (with or without -CORRIGENDUM, OP-PROJ, etc.)
    escaped = re.escape(slot_label)
    block_re = re.compile(
        rf'(## {escaped}\b[^\n]*\n[\s\S]*?)(?=\n##\s)',
        re.MULTILINE,
    )
    m = block_re.search(registry_md_text)
    return m.group(1) if m else ''


def extract_registry_block_anylevel(registry_md_text: str, slot_label: str) -> str:
    """Extract a registry §VII.{slot} block at heading level ## OR ###.

    Walks both heading levels and returns the first matching block. Termination:
    block extends to the next heading at the same OR shallower level.

    Used by Class-(h) MISSING-PARSE-TREE-EXPANSION audit which targets §VII
    entries that may live at either heading level (e.g., §VII.AN at ##,
    §VII.U.2 at ###).
    """
    escaped = re.escape(slot_label)
    # Try level-3 first (e.g., §VII.U.2)
    block_re_l3 = re.compile(
        rf'(### {escaped}\b[^\n]*\n[\s\S]*?)(?=\n###?\s)',
        re.MULTILINE,
    )
    m = block_re_l3.search(registry_md_text)
    if m:
        return m.group(1)
    # Fall back to level-2 (e.g., §VII.AN per existing convention)
    block_re_l2 = re.compile(
        rf'(## {escaped}\b[^\n]*\n[\s\S]*?)(?=\n##\s)',
        re.MULTILINE,
    )
    m = block_re_l2.search(registry_md_text)
    return m.group(1) if m else ''


def detect_class_h_missing_parse_tree_expansion(
    entry_block: str,
    entry_label: str,
) -> dict:
    """
    Class-(h) MISSING-PARSE-TREE-EXPANSION detector (S90 W1-8 extension).

    Per `.claude/rules/registry-landing.md §"Parse-Tree Expansion
    Pre-Registration for new §VII entries (S90 W-3 CF-R1-3)"`: a §VII entry
    that cites an observable with a state-historic name (per
    STATE_HISTORY_LABEL_PATTERNS) MUST declare the parse-tree expansion
    alongside the symbolic form (per PARSE_TREE_EXPANSION_MARKERS).

    Detection logic:
      1. Scan entry_block for any STATE_HISTORY_LABEL_PATTERNS match.
      2. If no match → diagnostic = 'no_state_history_label_present' (rule N/A).
      3. If match found → scan for PARSE_TREE_EXPANSION_MARKERS.
      4. If marker found → diagnostic = 'PASS' (rule satisfied).
      5. If marker absent → diagnostic = 'MISSING-PARSE-TREE-EXPANSION' at S2.

    Returns:
      dict with keys: audit_class, entry_label, state_history_label_matches,
                      parse_tree_expansion_present, diagnostic, severity,
                      remediation, has_class_h_flag (bool).
    """
    result = {
        'audit_class': 'Class-(h) MISSING-PARSE-TREE-EXPANSION',
        'entry_label': entry_label,
        'state_history_label_matches': [],
        'parse_tree_expansion_present': False,
        'diagnostic': 'PASS',
        'severity': 'NONE',
        'remediation': 'No remediation required.',
        'has_class_h_flag': False,
    }

    for pat in STATE_HISTORY_LABEL_PATTERNS:
        m = re.search(pat, entry_block)
        if m:
            result['state_history_label_matches'].append({
                'pattern': pat,
                'match_text': m.group(0),
                'span_start': m.start(),
            })

    if not result['state_history_label_matches']:
        result['diagnostic'] = 'no_state_history_label_present'
        return result

    pt_match = PARSE_TREE_EXPANSION_RE.search(entry_block)
    if pt_match:
        result['parse_tree_expansion_present'] = True
        result['parse_tree_marker_match'] = pt_match.group(0)
        result['diagnostic'] = 'PASS'
        return result

    result['diagnostic'] = 'MISSING-PARSE-TREE-EXPANSION'
    result['severity'] = 'S2'
    result['has_class_h_flag'] = True
    label_summary = ', '.join(
        m['match_text'] for m in result['state_history_label_matches'][:3]
    )
    result['remediation'] = (
        f'Registry entry {entry_label} contains state-history label(s) '
        f'[{label_summary}] but no parse-tree expansion block detected. '
        f'Per `.claude/rules/registry-landing.md §"Parse-Tree Expansion '
        f'Pre-Registration for new §VII entries (S90 W-3 CF-R1-3)"`, NEW §VII '
        f'entries with state-historic observables MUST declare the parse-tree '
        f'expansion (matching '
        f'`Parse-tree expansion:|parse_tree_expansion:|## Parse-tree` OR an '
        f'inline `parse-tree (decision|level|reduction|expansion)` reference). '
        f'Recommend adding a "Parse-tree expansion:" block citing the '
        f'reduction chain from history-label to closed-form on substrate '
        f'algebra (canonical worked example: §VII.U.2 Corner II row line '
        f'12961, `Var_a(n_a^GGE) → (1/N) Σ_a m_a |v_a|^4 − '
        f'((1/N) Σ_a m_a |v_a|^2)^2` where '
        f'`n_a = Δ_BCS² / (2(λ_a² + Δ_BCS²))`).'
    )
    return result


# =====================================================================
# Class-(i) Level-3 band-containment pattern set + internal-consistency detector
# (S92 §VII.AX.OP-PROJ JE5 workshop extension; per the Level-3 annotation
# discipline DIRECTIVE at `sessions/framework/registry/cross-pillar-bridge-corpus.md
# §20` and its orchestrator-reserved mirrors at
# `.claude/rules/cross-pillar-bridge-anatomy.md §"Registry-PASS criterion"`
# (criterion-side home) + `.claude/rules/registry-landing.md` (audit-side home,
# parallel to Class-(h) MISSING-PARSE-TREE-EXPANSION)).
#
# Provenance:
#   - S92 §VII.AX.OP-PROJ JOINT Element-5 central-value-vs-conjunctive workshop
#     (connes-ncg-theorist + volovik-superfluid-universe-theorist; CONVERGED 2
#     rounds, 2026-05-23). The detector is the structural generalization of the
#     §VII.AX.OP-PROJ Stage-2 Axis-B FAIL (audit_sha256=f20bc3ad108dbfad...):
#     a Level-3 row that STATES the falsifying band-edge numbers in the same
#     breath as a false "both edges inside conjunct" containment summary is
#     internally inconsistent and should be caught at PLAN-FREEZE, not only at
#     Stage-2 cross-review.
#   - Effected in-session by volovik-superfluid-universe-theorist (final turn);
#     single-function-scope (regex + float parsing only; NO eigenvalue / GPE /
#     canonical-constants compute), so a file edit, not a math carry-forward —
#     matching how §18/§19 detect_* detectors were landed.
#
# Detection logic (structurally identical to detect_class_h):
#   1. Scan the Level-3 block for a band-containment claim — a
#      "1σ band [L_b, U_b] ... both edges inside ... conjunct [L_c, U_c]"
#      lexical pattern (TWO bracketed numeric pairs + a "both ... inside"
#      containment assertion).
#   2. No match → diagnostic 'no_band_containment_claim_present' (rule N/A).
#   3. Match found → numeric sub-check: parse L_b, U_b, L_c, U_c as floats
#      (handle e-notation, ASCII/Unicode minus); test L_b >= L_c AND U_b <= U_c.
#   4. Containment TRUE → diagnostic 'PASS' (claim is self-consistent).
#   5. Containment FALSE → diagnostic 'INTERNALLY-INCONSISTENT-LEVEL-3-BAND-
#      STATEMENT' at S2 advisory (escalating to HARD-HALT on K=3 promotion of
#      the Level-3 annotation discipline); halts plan-freeze.
#
# Status: SUGGESTION at K=1 (S2 advisory; NOT HARD-HALT). Promotes to MANDATORY
# at K=3 distinct calibration instances per
# `feedback_rules-compensate-missing-structure.md`.
# =====================================================================

# Containment-claim trigger patterns (the "both edges inside" assertion).
# A Level-3 row firing ANY of these is making a band-edge containment claim
# that the numeric sub-check then validates against the stated bracketed pairs.
LEVEL_3_BAND_CONTAINMENT_PATTERNS = [
    r'both\s+edges\s+inside',
    r'both\s+1\s*[σo]\s*edges\s+inside',
    r'both\s+(?:1σ\s+)?edges\s+(?:lie\s+)?(?:with)?in',
]
LEVEL_3_BAND_CONTAINMENT_RE = re.compile(
    '|'.join(LEVEL_3_BAND_CONTAINMENT_PATTERNS),
    re.IGNORECASE,
)

# A bracketed numeric pair [a, b] with e-notation + ASCII/Unicode minus.
# Captures the two floats of one [lower, upper] pair.
_FLOAT_TOKEN = r'[−\-]?\d+(?:\.\d+)?(?:[eE][−\-]?\d+)?'
BRACKETED_PAIR_RE = re.compile(
    rf'\[\s*({_FLOAT_TOKEN})\s*,\s*({_FLOAT_TOKEN})\s*\]'
)


def _parse_float_token(tok: str) -> float:
    """Parse a float token handling the Unicode minus sign U+2212 ('−')."""
    return float(tok.replace('−', '-'))  # (local) Unicode-minus normalization


def detect_class_i_internally_inconsistent_level_3_band(
    entry_block: str,
    entry_label: str,
) -> dict:
    """
    Class-(i) INTERNALLY-INCONSISTENT-LEVEL-3-BAND-STATEMENT detector.

    Per the Level-3 annotation discipline DIRECTIVE
    (`sessions/framework/registry/cross-pillar-bridge-corpus.md §20`;
    orchestrator-reserved mirrors at
    `.claude/rules/cross-pillar-bridge-anatomy.md §"Registry-PASS criterion"`
    + `.claude/rules/registry-landing.md`): a Level-3 registry row that states
    band-edge numbers AND a containment claim those same numbers falsify is
    internally inconsistent and fires at S2 advisory (HARD-HALT on K=3
    promotion), halting plan-freeze.

    The detector reads BOTH bracketed numeric pairs the row lists (the band
    [L_b, U_b] FIRST, the conjunct [L_c, U_c] SECOND in canonical phrasing)
    and checks the stated containment (L_b >= L_c AND U_b <= U_c) against the
    numbers the same row states. The §VII.AX.OP-PROJ row is the K=1 calibration
    instance (lists 5.316e-23, 5.5e-23, and "both edges inside" with
    5.316e-23 < 5.500e-23 ⇒ FALSE ⇒ fires).

    Args:
      entry_block:  the text of the §VII slot's Level-3 block.
      entry_label:  the slot label (e.g. '§VII.AX.OP-PROJ').

    Returns:
      dict with keys: audit_class, entry_label, containment_claim_present,
                      band_pair, conjunct_pair, containment_holds, diagnostic,
                      severity, remediation, has_class_i_flag (bool).
    """
    result = {
        'audit_class': 'Class-(i) INTERNALLY-INCONSISTENT-LEVEL-3-BAND-STATEMENT',
        'entry_label': entry_label,
        'containment_claim_present': False,
        'band_pair': None,
        'conjunct_pair': None,
        'containment_holds': None,
        'diagnostic': 'PASS',
        'severity': 'NONE',
        'remediation': 'No remediation required.',
        'has_class_i_flag': False,
    }

    claim_match = LEVEL_3_BAND_CONTAINMENT_RE.search(entry_block)
    if not claim_match:
        result['diagnostic'] = 'no_band_containment_claim_present'
        return result

    result['containment_claim_present'] = True
    result['containment_claim_text'] = claim_match.group(0)

    pairs = BRACKETED_PAIR_RE.findall(entry_block)
    if len(pairs) < 2:
        # Containment claim present but the two bracketed pairs (band + conjunct)
        # are not both parseable from the block — flag as INFO (cannot decide).
        result['diagnostic'] = 'containment_claim_present_but_pairs_unparseable'
        result['severity'] = 'S2'
        result['remediation'] = (
            f'Registry entry {entry_label} makes a band-containment claim '
            f'("{claim_match.group(0)}") but fewer than two bracketed numeric '
            f'pairs [lower, upper] were parseable from the block; cannot run '
            f'the numeric sub-check. Ensure the row states BOTH the 1σ band '
            f'[L_b, U_b] AND the conjunct [L_c, U_c] in bracketed form.'
        )
        return result

    # Canonical phrasing lists the band FIRST, the conjunct SECOND.
    (l_b, u_b) = (_parse_float_token(pairs[0][0]), _parse_float_token(pairs[0][1]))
    (l_c, u_c) = (_parse_float_token(pairs[1][0]), _parse_float_token(pairs[1][1]))
    result['band_pair'] = [l_b, u_b]
    result['conjunct_pair'] = [l_c, u_c]

    containment_holds = (l_b >= l_c) and (u_b <= u_c)  # (local) both-edges-inside test
    result['containment_holds'] = containment_holds

    if containment_holds:
        result['diagnostic'] = 'PASS'
        return result

    # Containment claim is FALSE on at least one edge — internally inconsistent.
    result['diagnostic'] = 'INTERNALLY-INCONSISTENT-LEVEL-3-BAND-STATEMENT'
    result['severity'] = 'S2'
    result['has_class_i_flag'] = True
    lower_viol = l_b < l_c  # (local)
    upper_viol = u_b > u_c  # (local)
    viol_edges = []  # (local)
    if lower_viol:
        viol_edges.append(
            f'lower band edge {l_b:.6g} < conjunct lower {l_c:.6g}'
        )
    if upper_viol:
        viol_edges.append(
            f'upper band edge {u_b:.6g} > conjunct upper {u_c:.6g}'
        )
    result['remediation'] = (
        f'Registry entry {entry_label} asserts band-containment '
        f'("{claim_match.group(0)}") but the numbers the same row lists '
        f'falsify it: {"; ".join(viol_edges)}. Per the Level-3 annotation '
        f'discipline (`sessions/framework/registry/cross-pillar-bridge-corpus.md '
        f'§20`; criterion-side `cross-pillar-bridge-anatomy.md '
        f'§"Registry-PASS criterion"`), descriptive 1σ-band / edge-containment '
        f'statements are NON-LOAD-BEARING annotations governed by the canonical '
        f'central-value criterion, NOT band-containment. Correct the false '
        f'summary in-place to a TRUE statement of the same numbers (the '
        f'§VII.AX.OP-PROJ Eq. (2′) pattern: state which edge lies outside and '
        f'by how much, attribute the offset to the Friedrich-Bär '
        f'TRUNCATION-resolution envelope at the canonical L_max, and cite the '
        f'central-value criterion as governing). Registry-text correction is '
        f'mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`, '
        f'routed to housekeeping §A.'
    )
    return result


def _self_test_class_i() -> int:
    """Self-test fixture for detect_class_i (4 cases: positive / 2 negatives /
    parse-degenerate). Mirrors the s90_w1_deferred_pending_audit_test.py
    self-test pattern. Returns count of PASSing assertions (expects 4)."""
    n_pass = 0  # (local)

    # T1 (positive: the §VII.AX.OP-PROJ K=1 calibration instance — fires).
    t1 = (
        '1σ band [5.316e-23, 9.775e-23] m⁻³ with both edges inside the '
        'upper-22.6%-conjunct [5.500e-23, 2.200e-22] m⁻³.'
    )
    r1 = detect_class_i_internally_inconsistent_level_3_band(t1, '§VII.AX.OP-PROJ')
    assert r1['diagnostic'] == 'INTERNALLY-INCONSISTENT-LEVEL-3-BAND-STATEMENT', r1
    assert r1['has_class_i_flag'] is True, r1
    assert r1['containment_holds'] is False, r1
    n_pass += 1

    # T2 (negative: a genuinely self-consistent containment claim — PASS).
    t2 = (
        '1σ band [6.000e-23, 9.000e-23] m⁻³ with both edges inside the '
        'conjunct [5.500e-23, 2.200e-22] m⁻³.'
    )
    r2 = detect_class_i_internally_inconsistent_level_3_band(t2, '§VII.TEST-OK')
    assert r2['diagnostic'] == 'PASS', r2
    assert r2['has_class_i_flag'] is False, r2
    assert r2['containment_holds'] is True, r2
    n_pass += 1

    # T3 (negative: no containment claim at all — rule N/A).
    t3 = 'Level-3 anchor n_PBH = 7.2761e-23 m⁻³; central value inside the conjunct.'
    r3 = detect_class_i_internally_inconsistent_level_3_band(t3, '§VII.TEST-NA')
    assert r3['diagnostic'] == 'no_band_containment_claim_present', r3
    assert r3['has_class_i_flag'] is False, r3
    n_pass += 1

    # T4 (parse-degenerate: claim present, fewer than two bracketed pairs).
    t4 = 'both edges inside the conjunct (band [5.316e-23, 9.775e-23], conjunct not bracketed).'
    r4 = detect_class_i_internally_inconsistent_level_3_band(t4, '§VII.TEST-DEGEN')
    assert r4['diagnostic'] == 'containment_claim_present_but_pairs_unparseable', r4
    n_pass += 1

    return n_pass


def main():
    """CLI entry. Default: audit §VII.AN as the Class-(g) K=1 calibration
    instance. Flags:
      --self-test-i   run the Class-(i) self-test fixture (4 cases) and exit.
      --class-i SLOT  run the Class-(i) detector on a named §VII slot's block.
    """
    # --self-test-i: exercise the Class-(i) self-test fixture (no registry read).
    if '--self-test-i' in sys.argv:
        n_pass = _self_test_class_i()  # (local)
        print(json.dumps(
            {'self_test': 'detect_class_i_internally_inconsistent_level_3_band',
             'cases_passed': n_pass, 'cases_total': 4,
             'verdict': 'PASS' if n_pass == 4 else 'FAIL'},
            indent=2, ensure_ascii=False,
        ))
        # Exit 0 regardless — verdict is data, not exit code, per math-scripts.md
        sys.exit(0)

    # Resolve repo root from this file's location (computations/_shared/_registry_landing_audit.py)
    repo_root = Path(__file__).resolve().parents[2]
    registry_md = repo_root / 'sessions' / 'permanent-results-registry.md'
    if not registry_md.exists():
        print(json.dumps({'error': f'registry not found at {registry_md}'}, indent=2))
        sys.exit(1)

    text = registry_md.read_text(encoding='utf-8', errors='ignore')

    # --class-i SLOT: run the Class-(i) detector on a named slot's block.
    if '--class-i' in sys.argv:
        ci_idx = sys.argv.index('--class-i')  # (local)
        slot = sys.argv[ci_idx + 1] if len(sys.argv) > ci_idx + 1 else '§VII.AX.OP-PROJ'  # (local)
        block = extract_registry_block_anylevel(text, slot)
        if not block:
            print(json.dumps({'error': f'block for {slot} not found'}, indent=2))
            sys.exit(1)
        result = detect_class_i_internally_inconsistent_level_3_band(block, slot)
        print(json.dumps(result, indent=2, ensure_ascii=False))
        sys.exit(0)

    slot = sys.argv[1] if len(sys.argv) > 1 else '§VII.AN'
    block = extract_registry_block(text, slot)
    if not block:
        print(json.dumps({'error': f'block for {slot} not found'}, indent=2))
        sys.exit(1)

    result = detect_class_g(block, registry_slot=slot, repo_root=repo_root)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    # Exit 0 regardless of diagnostic — verdict is data, not exit code, per math-scripts.md
    sys.exit(0)


if __name__ == '__main__':
    main()
