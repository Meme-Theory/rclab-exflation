# Capstone Equation Review — Campaign Tracker

**Skill**: `/rclab-review` (solo synthesis — independent, no cross-agent coordination)
**Source**: `sessions/framework/phonic-exflation-equation.md` (S95-era capstone)
**Agents**: `ALL` → 31 research theorists (canonical roster, excl. `phonon-exflation-sim`)
**Output**: this directory — one `{short-name}-synthesis.md` per agent
**Context (verbatim)**: "This is our capstone from the last 95 sessions; all research agents should evaluate it, and provide the skill mandated review. There are still open questions, that we have in the open, and each question is a ripe harvest of math waiting for our greedy hands to calculate."
**Dispatch policy**: background agents, Opus tier, `acceptEdits`, ≤8 concurrent, 4 batches, wait-ALL between batches. Identical neutral prompt to every agent (review-dispatch neutrality).

## Concurrency note (recovery)
First attempt launched 8 concurrent → ALL hit a transient server-side rate-limit (`not your usage limit`), 0 files landed. Recovered: 35s backoff, then probe at 3 (clean: 220k/246k/224k tokens), now ramped to **5 concurrent** per batch. If a future batch re-throttles: longer backoff + drop to 2.

## Batch plan (revised, 5-concurrent)

| Batch | Agents | State |
|:------|:-------|:------|
| probe | connes, volovik, baptista | DONE (208/293/244 lines) |
| R1 | lizzi, spectral-geometer, transit, mack, gen-physicist | DONE (8 files total on disk) |
| R2 | hawking, einstein, feynman, sagan, landau | DONE (13 files total on disk) |
| R3 | kk, berry, dirac, van-den-dungen, phonon-first | DONE (18 files total on disk) |
| R4 | kaku, kitaev, string-theory, quantum-foam, lqg | DONE (23 files total on disk) |
| R5 | paasch, tesla, quantum-acoustics, sp, neutrino | DONE (28 files total on disk) |
| R6 | cosmic-web, little-red-dots, nazarewicz | DONE (31 files total on disk) |

## Resume protocol (if context summarized mid-run)
1. `ls sessions/framework/equation-collab/*-synthesis.md` and count.
2. Map present files against the batch plan above to find the last completed batch.
3. If a batch is fully present (its files all on disk with substantive content), launch the next batch with the identical neutral prompt (template below).
4. When all 31 present → write Phase-3 report + index, done.

## Per-agent prompt template (substitute {TYPE}=subagent_type, {SHORT}=short-name)
Read order: (1) `.claude/agent-memory/{TYPE}/MEMORY.md` if present; (2) `.claude/rules/phononic-framing.md`; (3) `sessions/framework/phonic-exflation-equation.md` in full. Focus = the verbatim context above. Task: write `sessions/framework/equation-collab/{SHORT}-synthesis.md` per `.claude/templates/synthesis.md` (I–VI), title `# Capstone Equation Review — {SHORT}`, §V mandatory (open-question harvest, 4-field). Rules: source verdicts authoritative (cross-check via knowledge MCP / canonical_constants, do not overturn); flag conflicts; sole writer of own file; substrate language; dimensional consistency; PRELIMINARY tags.

## Status: COMPLETE — 31/31 reviews on disk. Consolidated convergence/dissonance/harvest map: `_consolidated-findings.md`.
