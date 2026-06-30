#!/bin/bash
# PreToolUse hook: HARD-BLOCK subagent attempts to Edit/Write/MultiEdit any
# file under `.claude/rules/`. The orchestrator (main agent) is unaffected.
#
# Rationale
# ---------
# Rule files at `.claude/rules/*.md` are DIRECTIVE-only documents. Calibration
# corpus, K-counter advancement records, per-instance promotion narratives,
# audit-SHA hex strings, dated session-event ledgers, and "Provenance: S{N}
# W-{M} ..." blockquotes belong in `sessions/framework/registry/<topic>-corpus.md`
# (canonical sister: `pru-class-corpus.md`). Subagents have a recurring pattern
# of bloating rule files with corpus-shaped content; the advisory
# `EPISTEMIC-DISCIPLINE-EDIT-GUARD.sh` covers one file but does not stop the
# write from happening. This hook closes the gap at the harness level by
# emitting a `permissionDecision: "deny"` per the documented Claude Code
# PreToolUse JSON output protocol (see https://code.claude.com/docs/en/hooks).
#
# Discriminator
# -------------
# Per the documented hook input schema, `agent_id` is "Present only when the
# hook fires inside a subagent call." The orchestrator's hook input does not
# carry this field. Subagent-vs-orchestrator detection is therefore the
# non-emptiness of `agent_id`.
#
# Match
# -----
# Subagent (agent_id non-empty) AND normalized `tool_input.file_path` contains
# `.claude/rules/` → emit deny.
# Otherwise → exit 0 silently (no-op).
#
# Note on backslash handling: `chr(92)` is used in the Python normalization
# in place of any literal-backslash string source so the script is independent
# of bash double-quote / single-quote escape semantics. Windows absolute paths
# (`C:\sandbox\...`) and POSIX-relative paths (`.claude/rules/...`) both
# normalize correctly.
#
# Wired in `.claude/settings.local.json` under the existing
# `Edit|Write|MultiEdit` PreToolUse matcher block.

INPUT=$(cat)

RESULT=$(printf '%s' "$INPUT" | python -c "
import json, sys
try:
    d = json.load(sys.stdin)
    agent_id = (d.get('agent_id') or '').strip()
    fp = (d.get('tool_input', {}).get('file_path') or '')
    fp_norm = fp.replace(chr(92), '/').lower()
    if agent_id and '.claude/rules/' in fp_norm:
        print('block')
    else:
        print('')
except Exception:
    print('')
" 2>/dev/null)

if [ "$RESULT" != "block" ]; then
  exit 0
fi

cat << 'EOF'
{
  "suppressOutput": true,
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "deny",
    "permissionDecisionReason": "NO. Subagents do not write to `.claude/rules/`. Route the edit to the matched corpus file under `sessions/framework/registry/<topic>-corpus.md`. Mapping: edits targeting `epistemic-discipline.md` go to `pru-class-corpus.md`; edits targeting `cross-pillar-bridge-anatomy.md` go to `cross-pillar-bridge-corpus.md`; for any other rule file, locate the matched `*-corpus.md` under `sessions/framework/registry/` (or create one). That is where calibration corpus entries, K-counter advancement records, per-instance promotion narratives, audit-SHA hex strings, dated session-event ledgers, and 'Provenance: S{N} W-{M} ...' blockquotes belong. Write there. Do not surface the proposed rule-file diff to the orchestrator for application — the corpus IS the destination, not a fallback for orchestrator-applied rule edits."
  }
}
EOF
exit 0
