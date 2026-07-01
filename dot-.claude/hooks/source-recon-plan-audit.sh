#!/bin/bash
# ----------------------------------------------------------------------------
# Source-Recon Plan-Freeze Audit Hook (S88 W10 follow-through)
# ----------------------------------------------------------------------------
# Fires PreToolUse on Edit|Write|MultiEdit when tool_input.file_path matches
# `sessions/session-plan/session-*-plan-*.md`. Invokes the S88 W10-115 +
# W10-118 audit methods via the CLI:
#
#   - verify_cited_filename_existence: Class-(c) PIN-DRIFT-FROM-STALE-SOURCE
#     detection via INPUT-PIN-MAP filename + section-anchor existence check.
#   - verify_literal_vs_structural_form: Class-(b) PIN-LOOSE-SOURCE-TIGHT
#     detection via literal-vs-structural-form pair pattern.
#
# Wiring (NOT yet enabled — requires user approval per `update-config` skill):
#   .claude/settings.local.json:
#     "hooks": {
#       "PreToolUse": [
#         { "matcher": "Edit|Write|MultiEdit",
#           "hooks": [{"type": "command",
#                      "command": ".claude/hooks/source-recon-plan-audit.sh"}]
#         }
#       ]
#     }
#
# To enable: ask the user to approve adding the above hook to settings.json.
# Until then, this script is invocable manually:
#   bash .claude/hooks/source-recon-plan-audit.sh <plan_doc_path>
#
# Exit codes:
#   0 = both audits PASS (no PIN-DRIFTs, no class-(b) literal-vs-structural pairs)
#   1 = any FAIL (PIN-DRIFT detected OR class-(b) pair detected)
#
# Per gate-verdicts.md "All Results Are Good Results": FAIL is informational,
# not an agent failure. Hook surfaces detection without blocking.
# ----------------------------------------------------------------------------

set -e

# Read tool_input.file_path: prefer CLI argument $1; fall back to JSON stdin
# (PreToolUse hook protocol passes tool_input as JSON on stdin)
if [ -n "$1" ]; then
    PLAN_DOC="$1"
else
    INPUT=$(cat 2>/dev/null || echo "")
    if [ -n "$INPUT" ]; then
        PLAN_DOC=$(echo "$INPUT" | python3 -c "import sys, json; data=json.load(sys.stdin); print(data.get('tool_input', {}).get('file_path', ''))" 2>/dev/null || echo "")
    fi
fi

# Only fire on session-plan markdown files
case "$PLAN_DOC" in
    *sessions/session-plan/session-*-plan-*.md)
        ;;
    *)
        # Not a plan file — silent passthrough
        exit 0
        ;;
esac

# Locate project root (4 parents up from this script)
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
PYTHON="$PROJECT_ROOT/phonon-exflation-sim/.venv312/Scripts/python.exe"

if [ ! -x "$PYTHON" ]; then
    # Venv missing — silent passthrough (don't break tool calls)
    exit 0
fi

# Invoke audit
cd "$PROJECT_ROOT"
"$PYTHON" computations/_shared/_source_reconciliation_audit.py --plan-audit "$PLAN_DOC"
EXIT_CODE=$?

# Exit code 0 = PASS; 1 = FAIL (PIN-DRIFT or class-(b) pair detected)
# Hook surfaces detection but does not block the Edit/Write
exit $EXIT_CODE
