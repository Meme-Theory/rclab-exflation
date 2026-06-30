#!/usr/bin/env bash
# ----------------------------------------------------------------------------
# MCP Pre-Check Hook (Phi(a_4) load-bearing axis per wave-classification.md)
# ----------------------------------------------------------------------------
# Triggered by: PreToolUse with matcher "mcp__.*"
# Purpose:      Inject a per-MCP-server brief into the model's next turn before
#               the MCP tool call is dispatched.
# Mechanism:    Reads tool_name from PreToolUse JSON stdin, dispatches via
#               case on the mcp__<server>__ prefix, emits a brief tailored to
#               the server. Silent passthrough for unknown / future MCP servers.
#
# Architecture rationale:
#   - Single dispatcher (case statement) keeps the brief catalog in ONE
#     searchable, diff-able place. Adding a new server = adding one case arm.
#   - Per-server briefs are project-specific reminders (project rules in
#     `.claude/rules/` are general background; these fire just-in-time).
#   - Argument-aware briefs are a v2 enhancement; v1 dispatches on tool_name
#     prefix only.
#
# Convention: project venv Python for stdin parsing + JSON output, matching
# framework-edit-reindex.sh and source-recon-plan-audit.sh. PRIME-DIRECTIVE
# uses bare `python` for stdin-JSON parsing — both work for json-stdlib only.
#
# Forward extension: when claude_ai_Gmail / claude_ai_Google_Calendar /
# claude_ai_Google_Drive MCPs become physics-relevant, add case arms.
# Default `*) exit 0` keeps unknown servers silent rather than blocking.
# ----------------------------------------------------------------------------

set -u

VENV_PY="C:/sandbox/Ainulindale Exflation/phonon-exflation-sim/.venv312/Scripts/python.exe"
[ -x "$VENV_PY" ] || exit 0

INPUT=$(cat)
TOOL_NAME=$(printf '%s' "$INPUT" | "$VENV_PY" -c \
  "import sys,json; print(json.loads(sys.stdin.read() or '{}').get('tool_name',''))" \
  2>/dev/null || echo "")

case "$TOOL_NAME" in
  mcp__knowledge__*)
    BRIEF="KNOWLEDGE-MCP — query-first discipline. This is the canonical project graph (~77 sessions, 25+ closed mechanisms, 180+ canonical constants per CLAUDE.md). Before computing, verify the result isn't already known/closed/canonical. Order: search_knowledge → trace_entity → get_constant → list_constants. Do not recompute what is closed."
    ;;
  mcp__sage__*)
    BRIEF="SAGE-MCP — exact-rational discipline. When floats lose precision near a threshold (cluster-span <1e-14, regulator-class ratio splits, OOM comparisons), use Sage QQ-coerced compute. Cite the Sage-exact rational alongside any float mnemonic. See regulator-pin-discipline.md §'Sage-Exact Rationals for Ω_GW' and math-scripts.md §'Mnemonic-vs-exact ratio discipline'."
    ;;
  mcp__oeis__*)
    BRIEF="OEIS-MCP — integer-sequence verification. lookup_by_values needs ≥5 terms; search_oeis for keyword/name. A hit is STRUCTURAL identification, not statistical evidence. Useful for spectral cardinality vectors, partition functions, dimension formulas."
    ;;
  mcp__paper-search__*)
    BRIEF="PAPER-SEARCH-MCP — download-before-read. search → download → read. Do NOT cite a paper from training knowledge per feedback_research-corpus.md. New papers land under researchers/<area>/. Mark gaps explicitly when a citation cannot be fetched."
    ;;
  mcp__mathscinet__*)
    BRIEF="MATHSCINET-MCP — citation-verification. Use lookup_mr_reference for canonical MR ID + bibtex; search_mathscinet for keyword. Pair with paper-search to fetch full text. Citation form must match the MR record exactly when entering a registry row."
    ;;
  mcp__zbmath__*)
    BRIEF="ZBMATH-MCP — MSC subject classification + European math literature. search_msc by code (e.g., 58J42 spectral triples, 81T05 QFT axioms); search_zbmath for keyword. Complements mathscinet."
    ;;
  mcp__astro__*)
    BRIEF="ASTRO-MCP — observational anchor lookup. search_objects for known coordinates; astroquery_query for service-specific (Vizier, SIMBAD). Cite service+query as PROVENANCE in any constraint plot. Watch Class-(c) PIN-DRIFT-FROM-STALE-SOURCE — verify catalog version against canonical-constants_provenance edges."
    ;;
  mcp__madrigal__*)
    BRIEF="MADRIGAL-MCP — geophysical/ionospheric instrument database. Niche: radar/GPS/satellite atmospheric data. Order: list_madrigal_servers → list_instruments → list_experiments → describe_framework_target → download_file."
    ;;
  *)
    # Unknown / future MCP server (e.g., claude_ai_Gmail, claude_ai_Google_Calendar,
    # claude_ai_Google_Drive). Silent passthrough; add a case arm when project use
    # makes one warranted.
    exit 0
    ;;
esac

# Emit additionalContext for the model's next turn. Use venv Python for
# JSON building so brief text containing punctuation (apostrophes, backticks,
# non-ASCII) round-trips cleanly without shell-quoting hazards.
"$VENV_PY" -c "
import json, sys
print(json.dumps({
  'hookSpecificOutput': {
    'hookEventName': 'PreToolUse',
    'additionalContext': sys.argv[1]
  }
}))
" "$BRIEF"

exit 0
