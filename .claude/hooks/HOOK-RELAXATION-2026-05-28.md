# Hook Relaxation — 2026-05-28

**Trigger**: user directive following `sessions/session-plan/session-95-model-swap-meta-report.md` §D
("backup settings.json, then relax the hook scripts; every one of them was a bandaid on Opus 4.7's
inability to stay on task or review its own work"). Running model: `claude-opus-4-8[1m]`.

**Principle**: the wired hooks split into (1) **functional infrastructure** (real side-effects) and
(2) **reminder-injection bandaids** (pure `additionalContext` text compensating for 4.7-era
stay-on-task / review-own-work lapses). Class (1) is KEPT intact. Class (2) is unwired or softened.
Bias is toward deleting the reminder echo, NOT the rules content or the real audits
(`feedback_structure-appetite-is-a-symptom.md`: the per-tool reminder echo is the deletion-test
candidate; the load-bearing audits are not). Convergent findings CONV-1 (7/7 planners: the compute
completion-contract fires on non-compute spawns) and CONV-8 (the ≥15-line clause contradicts
`feedback_max-effort-full-fidelity.md`) drove the specifics.

## Backups (restore points)
- `C:/Users/ryan/.claude/settings.json.bak-2026-05-28-pre-hook-relax` (global; backup only — its content is unchanged, it only wires `git_command_blocker.py`)
- `.claude/settings.local.json.bak-2026-05-28-pre-hook-relax`
- `.claude/hooks/{SESSION-START-DIRECTIVE,SUBAGENT-START-DIRECTIVE,PRIME-DIRECTIVE,READ-FEEDBACK-RULES-DIRECTIVE,TASK-UPDATE-RETROSPECTIVE}.sh.bak-2026-05-28-pre-hook-relax`
- All hook scripts + `settings.local.json` are also git-tracked → `git checkout` restores them.

## Changes

### Unwired in `.claude/settings.local.json` (scripts left on disk for clean re-enable)
| Hook | Event / matcher (was) | Why unwired |
|:-----|:----------------------|:------------|
| `PRIME-DIRECTIVE.sh` ("DERIVATIVE OUTPUT") | PreToolUse `Write\|Edit\|MultiEdit\|NotebookEdit\|Agent\|TaskCreate` | High-frequency pure reminder (~14 injections per 7-agent batch); zero behavior change for a rule-aware model (§D). |
| `READ-FEEDBACK-RULES-DIRECTIVE.sh` ("FEEDBACK RULES") | same matcher (was paired) | Same; "read your feedback rules" is intrinsic, not a hook's job. |
| `SUBAGENT-START-DIRECTIVE.sh` ("verify on disk: script+npz+plot+verdict+WP ≥15 lines") | SubagentStart (every spawn) | CONV-1, 7/7 UNANIMOUS: the compute completion-contract is categorically inapplicable to planner / reviewer / prompter spawns (markdown-only). The contract for genuine compute gates already lives in the spawn prompt. |

`PRIME-DIRECTIVE.sh`, `READ-FEEDBACK-RULES-DIRECTIVE.sh` (and `_batch_suppress.py`, which only they
called) remain on disk untouched, so re-enabling is a one-line `settings.local.json` restore.
`SUBAGENT-START-DIRECTIVE.sh` is unwired AND its brief was softened (≥15-line clause + compute-artifact
checklist removed) so a future re-enable does not reintroduce the CONV-1/CONV-8 miscalibration.

### Softened (kept wired)
- `TASK-UPDATE-RETROSPECTIVE.sh` — removed the "COMPLETION CLAIM" reminder brief + the ≥15-line stub
  heuristic (CONV-8). **Kept** the real VII-slot-allocation audit (delta-suppressed); the hook now emits
  ONLY when that audit has findings, and emits nothing otherwise.
- `SESSION-START-DIRECTIVE.sh` — softened from the "read §5/§7 IN FULL before any plan" nag down to the
  load-bearing harness fact (compact/resume = fresh context, banner ≠ handoff, read the file).

### Kept unchanged (functional infra / structural guards — NOT 4.7 bandaids)
- `framework-edit-reindex.sh` (PostToolUse) — runs `extract_entities.py --incremental` (knowledge-index sync).
- `python-validate.sh` → `python-validate.py` (PostToolUse) — canonical-import / hardcode lint on `computations/**/*.py`.
- `source-recon-plan-audit.sh` (PreToolUse Edit|Write|MultiEdit) — runs the source-reconciliation audit on plan files.
- `rules-folder-subagent-block.sh` (PreToolUse Edit|Write|MultiEdit) — HARD `permissionDecision:deny` on subagent edits to `.claude/rules/` (recursion-attack closure; report flagged KEEP).
- `EPISTEMIC-DISCIPLINE-EDIT-GUARD.sh` (PreToolUse Edit|Write|MultiEdit) — narrow advisory when editing `epistemic-discipline.md` (orchestrator-only, low-frequency). Candidate for later removal if desired.
- `mcp-pre-check.sh` (PreToolUse `mcp__.*`) — just-in-time per-MCP-server briefs (low-frequency, useful).

### Dormant (not wired; left as-is)
- `post-agent/completion-verify.sh` — contains the same ≥15-line GREEN/YELLOW heuristic; it is NOT wired
  in `settings.local.json`, so it does not fire. If ever re-wired, relax the `ln -ge 15` clause first.

## To restore everything
```
cp .claude/settings.local.json.bak-2026-05-28-pre-hook-relax .claude/settings.local.json
cp .claude/hooks/TASK-UPDATE-RETROSPECTIVE.sh.bak-2026-05-28-pre-hook-relax .claude/hooks/TASK-UPDATE-RETROSPECTIVE.sh
cp .claude/hooks/SESSION-START-DIRECTIVE.sh.bak-2026-05-28-pre-hook-relax .claude/hooks/SESSION-START-DIRECTIVE.sh
```
(or `git checkout -- .claude/settings.local.json .claude/hooks/`)

## Related same-session changes (not hooks)
- `C:/Users/ryan/.claude/CLAUDE.md` §"AGENT OUTPUT MONITORING" reconciled to the live harness (report §A).
- Project `CLAUDE.md` §"READ TOOL BYTE LIMIT" updated: the ~30KB ceiling was retested and does not exist
  (256KB single-call read succeeded 2026-05-28).
- `effort="thorough"` Agent-tool param removed from `rclab-plan/skill.md` + `rclab-investigate/skill.md`
  (the param no longer exists on the Agent tool; depth inherits from the orchestrator) (report §B).
