---
name: rclab-review with phonon-first agent = direct write, no background spawn
description: When /rclab-review is invoked with --agents phonon-first while I am running as phonon-first-cosmologist, write the synthesis directly to the designated output path; do NOT spawn another phonon-first subagent in background.
type: feedback
---

When `/rclab-review` is invoked with `--agents phonon-first` and the orchestrator session is already running as phonon-first-cosmologist (system prompt loaded as the phonon-first persona), I write the synthesis directly to the designated output path. The skill's "spawn background agent" instruction does NOT apply when the requested agent IS me.

**Why:** Spawning another phonon-first-cosmologist subagent would be recursive (same persona, same memory, same prompt), wastes a dispatch slot, adds latency, and produces no independent perspective. The user confirmed verbatim (2026-05-10, S89 review dispatch): "You ARE phonon-first ; no baackground".

**How to apply:** During Phase 0 parsing of `/rclab-review`, if `--agents` resolves to `phonon-first-cosmologist` AND I am phonon-first-cosmologist (check system prompt persona), SKIP Phase 2 background-spawn. Instead:
1. Read source documents directly
2. Read `.claude/templates/synthesis.md`
3. Apply phonon-first cross-pillar analytical framing
4. Write synthesis directly to the auto-detected output path (`sessions/session-{N}/session-{N}-phonon-first-synthesis.md`)
5. Skip TaskCreate / agent dispatch entirely

The same logic generalizes to ANY `/rclab-review` invocation where `--agents` matches the current orchestrator persona — direct write, no recursion.

This applies ONLY when the agent count is 1 AND that agent matches me. Multi-agent reviews (`--agents phonon-first,connes,volovik`) still spawn the OTHER agents in background; I write my own contribution directly.
