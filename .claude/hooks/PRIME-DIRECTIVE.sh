#!/bin/bash
# PreToolUse hook: brief for derivative-output actions.
# Fires on Write|Edit|MultiEdit|NotebookEdit|Agent|TaskCreate.
#
# Suppressions:
#   - Subagent edits of .claude/rules/ (rules-folder-subagent-block emits DENY).
#   - Batched parallel invocations with identical brief content (see _batch_suppress.py).
#
# Note on framing: PreToolUse hooks fire in the harness BEFORE the tool executes,
# but the additionalContext reaches the model AFTER the tool result. Briefs are
# therefore written as standing guidance, not as "stop and do X before this action".

INPUT=$(cat)

SKIP=$(printf '%s' "$INPUT" | python -c "
import json, sys
try:
    d = json.load(sys.stdin)
    agent_id = (d.get('agent_id') or '').strip()
    fp = (d.get('tool_input', {}).get('file_path') or '')
    fp_norm = fp.replace(chr(92), '/').lower()
    if agent_id and '.claude/rules/' in fp_norm:
        print('skip')
    else:
        print('')
except Exception:
    print('')
" 2>/dev/null)
if [ "$SKIP" = "skip" ]; then exit 0; fi

BRIEF=$(cat << 'EOF_BRIEF'
DERIVATIVE OUTPUT — Calls that mirror a source (template from exemplar, summary, spawn prompt, working-paper section) require source-citation: identify the specific lines/sections your output matches. If you cannot cite, the match is imagined. For Agent dispatches and TaskUpdates built on subagent summaries: the summary is INTENT; the artifact on disk is REALITY. Verify on disk.
EOF_BRIEF
)

python "$(dirname "$0")/_batch_suppress.py" "PRIME-DIRECTIVE" "$BRIEF" 15
if [ $? -eq 1 ]; then exit 0; fi

python -c "
import json, sys
print(json.dumps({
    'suppressOutput': True,
    'hookSpecificOutput': {
        'hookEventName': 'PreToolUse',
        'additionalContext': sys.argv[1]
    }
}))
" "$BRIEF"
