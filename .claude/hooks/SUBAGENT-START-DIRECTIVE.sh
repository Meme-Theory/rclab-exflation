#!/bin/bash
# SubagentStart hook: brief the spawned subagent at its execution boundary.
# Fires once per subagent spawn (child side). The contract is the spawn prompt;
# cited files are the contract's substrate.
# Unique transition need: spawn-prompt + cited-file contract enforcement.
#
# NOTE (2026-05-28, hook-relaxation): this hook is UNWIRED in settings.local.json
# (CONV-1, 7/7: the compute-completion contract is miscast on non-compute spawns;
# dispatch-mode is set by the dispatching skill and is NOT visible to a
# SubagentStart hook, so it cannot be conditioned). The brief below is also
# softened — no >=15-line clause, no compute-artifact checklist — so a future
# re-enable is clean. See HOOK-RELAXATION-2026-05-28.md.

cat << 'EOF'
{
  "suppressOutput": true,
  "hookSpecificOutput": {
    "hookEventName": "SubagentStart",
    "additionalContext": "SUBAGENT START — Read your spawn prompt and every file it cites before acting; match any pre-registered threshold and tolerance exactly. Verify your promised artifacts exist on disk (by content, not line count) before reporting done."
  }
}
EOF
