#!/bin/bash
# PreToolUse hook: reminder to Read applicable feedback_*.md under memory/.
# MEMORY.md one-liners are labels; the file content is the rule.
#
# Suppressions:
#   - Subagent edits of .claude/rules/ (rules-folder-subagent-block emits DENY).
#   - Batched parallel invocations with identical brief.

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
FEEDBACK RULES — The applicable feedback_*.md in `C:\Users\ryan\.claude\projects\C--sandbox-Ainulindale-Exflation\memory\` is the rule; MEMORY.md one-liners are labels. Concrete triggers: (a) user pinned a single-verb end-state (block/no/just X/never) → `feedback_no-asking-just-execute.md`; (b) drafting a response with `or`/`alternatively` after the user adjudicated → `feedback_no-asking-just-execute.md`; (c) audit/hook surfaced a problem → `feedback_no-asking-just-execute.md`; (d) hygiene observation on already-correct artifact → `feedback_fix-in-session-never-defer.md`.
EOF_BRIEF
)

python "$(dirname "$0")/_batch_suppress.py" "READ-FEEDBACK-RULES" "$BRIEF" 15
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
exit 0
