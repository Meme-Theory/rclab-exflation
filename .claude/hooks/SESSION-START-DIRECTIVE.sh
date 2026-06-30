#!/bin/bash
# SessionStart hook: brief at session boundary (resume/compact/startup/clear).
# Counter to the "skim handoff, propose plausible next steps" failure mode.
# Unique transition need: prior-session inheritance.

cat << 'EOF'
{
  "suppressOutput": true,
  "hookSpecificOutput": {
    "hookEventName": "SessionStart",
    "additionalContext": "SESSION BOUNDARY — compact/resume starts a fresh context; in-memory state from the prior turn is gone. If continuing prior work, read the actual handoff/plan file rather than relying on the resume banner or recall."
  }
}
EOF
