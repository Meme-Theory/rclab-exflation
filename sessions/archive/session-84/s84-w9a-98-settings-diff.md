# S84-W9A-98 — settings.json wiring diff (for user to apply)

**Scope**: document the PostToolUse + Stop hook matchers that wire
`.claude/hooks/post-agent/completion-verify.sh` and
`.claude/hooks/post-session/v3-closure-audit.sh` into the harness.

**Rationale for not auto-applying**: per the S84-W9A-98 task CAUTION,
silent edits to `~/.claude/settings.json` are forbidden. The user must
apply this diff via the `/update-config` skill or by hand.

## Target file

`~/.claude/settings.json` (user-scope) OR `.claude/settings.local.json`
(project-scope, git-ignored) — the user chooses. Project-scope is
recommended so the rule co-travels with this repo.

## Hook-block addition

Append (or merge) into the top-level `hooks` key:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Agent",
        "hooks": [
          {
            "type": "command",
            "command": "bash \"${CLAUDE_PROJECT_DIR}/.claude/hooks/post-agent/completion-verify.sh\""
          }
        ]
      }
    ],
    "Stop": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "bash \"${CLAUDE_PROJECT_DIR}/.claude/hooks/post-session/v3-closure-audit.sh\""
          }
        ]
      }
    ]
  }
}
```

## Notes

- `PostToolUse` matcher `Agent` — fires only on Agent tool completions,
  not every bash call. ADVISORY posture: the hook exits 0 regardless.
  Advisory status is written into
  `.claude/hooks/logs/completion-queue.jsonl`.
- `Stop` matcher `*` — fires on every session close. BLOCKING posture:
  exits 1 on non-CLOSED / non-INFO verdicts. When exit 1, the `/handoff`
  skill (if present) will refuse to proceed.
- `${CLAUDE_PROJECT_DIR}` is the documented project-root env var the
  harness injects into hook commands.
- Hook scripts must have execute permission (`chmod +x` already applied
  during this session).

## Validation

After applying, trigger a no-op Agent dispatch and verify
`.claude/hooks/logs/completion-queue.jsonl` grows by one line. Trigger
a session end and verify `sessions/session-<NN>/v3_ladder_audit.json`
is written.

## Rollback

Remove the `PostToolUse` entry with `matcher: "Agent"` and the `Stop`
entry that references `v3-closure-audit.sh`. The hook scripts
themselves stay on disk — they are harmless when not wired.
