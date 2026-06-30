#!/bin/bash
# Pre-tool hook: when an agent attempts to Edit/Write/MultiEdit
# .claude/rules/epistemic-discipline.md, remind them that this file is
# DIRECTIVE ONLY. Calibration corpus, per-instance narratives, K-counter
# advancement records, audit-SHA hex strings, dated promotion histories,
# and session-event provenance belong in
# sessions/framework/registry/<topic>-corpus.md (canonical:
# pru-class-corpus.md), NOT in the rule file.
#
# Trigger: tool_input.file_path resolves to .claude/rules/epistemic-discipline.md
# (forward or back slashes, case-insensitive). Hook is advisory (does not
# block); emits additionalContext via the PreToolUse JSON protocol.

INPUT=$(cat)
TARGET=$(printf '%s' "$INPUT" | python -c "
import json, sys
try:
    d = json.load(sys.stdin)
    agent_id = (d.get('agent_id') or '').strip()
    fp = d.get('tool_input', {}).get('file_path', '') or ''
    fp_norm = fp.replace('\\\\', '/').lower()
    # Subagent attempts to edit .claude/rules/ are DENIED by rules-folder-subagent-block;
    # skip this advisory in that case to avoid wasted context on a blocked call.
    if agent_id:
        print('')
    elif fp_norm.endswith('.claude/rules/epistemic-discipline.md'):
        print('match')
    else:
        print('')
except Exception:
    print('')
" 2>/dev/null)

if [ "$TARGET" != "match" ]; then
  exit 0
fi

cat << 'EOF'
{
  "suppressOutput": true,
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "additionalContext": "STOP. You are about to edit `.claude/rules/epistemic-discipline.md`.\n\nThis file is a DIRECTIVE document — direction and statement, NOT a log, ledger, calibration corpus, or historical thesis. The user has corrected this rule file repeatedly for accreting session-event narrative; do not regress.\n\nFORBIDDEN edits to this file:\n- 'Provenance: S{N} W-{M} ...' blockquotes\n- 'Calibration corpus (K=N at <date>): instance #1 ...; instance #2 ...' tables or paragraphs\n- 'Status: SUGGESTION at K=1; promotes to MANDATORY at K=3' progress notes\n- audit_sha256 hex strings or any verdict-event content\n- 'Origin: S86 W-XX' / '(T1-21, S86 W-9)' subsection anchors\n- per-session promotion narratives, dated changelogs, 'NEW from S88 ...' tags\n- session-event narratives that explain HOW a rule got here rather than WHAT it directs\n\nREQUIRED shape for edits to this file:\n- Rule clauses are written as direction (\"When X, MUST Y\") with structurally-required elements enumerated.\n- Rule status is one tag per rule (MANDATORY / advisory until K=3); no further dated qualification.\n- Cross-references go to a SPECIFIC audit script, template, sister rule, or corpus file with one path each.\n\nWHERE LOGS GO INSTEAD (NOT in any file under .claude/rules/):\n- Calibration corpus, K-counter advancement records, per-instance narratives, audit-SHAs, dated promotion histories → `sessions/framework/registry/pru-class-corpus.md` (or another `*-corpus.md` in `sessions/framework/registry/`).\n- Session-event ledgers → the relevant session's `sessions/session-{N}/` artifacts.\n- Rule changelog → git log; do NOT embed inside the rule file.\n\nIf the edit you are about to make is corpus-shaped content, reroute to the corpus file. The rule file is already overlong; do NOT add narrative."
  }
}
EOF
exit 0
