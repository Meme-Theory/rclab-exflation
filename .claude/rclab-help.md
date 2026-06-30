# rclab — Skill Suite Help

Six skills cover the full research-lab pipeline. Pick one:

## Decision guide

| I want to... | Use |
|:--|:--|
| Plan the next compute session (gather carry-forwards, partition into waves, design test cases) | `/rclab-plan` |
| Execute a planned session — dispatch independent parallel agents per wave, collect gate verdicts | `/rclab-coordinate` |
| Investigate the just-closed session's working paper to design a workshop-schedule campaign (structural patterns, convergences, dissonances) | `/rclab-investigate` |
| Have 1+ agents independently write their own synthesis from the same source docs (no coordination between agents) | `/rclab-review` |
| Have 2 agents iteratively co-author a single shared document over N rounds (sequential, Edit-based, no team infrastructure) | `/rclab-workshop` |
| Run a 2-3 agent team that coordinates via inbox — panel/debate or multi-round collaborate sessions where agents message each other | `/rclab-team` |
| Run an **investigation** (exploratory track): plan an `investigation-{n}` from a free-form seed (a survey output), then execute a MIXED-TYPE plan (compute/review/workshop) | `/rclab-plan --investigation`, `/rclab-coordinate`, `/rclab-investigate --investigation` |

## Pipeline sequence

```
/rclab-plan (S{N})
  → /rclab-coordinate (S{N})   ← execute the plan
    → /rclab-investigate (S{N}) ← mine results for follow-up campaign
      → /rclab-workshop | /rclab-review | /rclab-team (S{N} campaign)
        → /rclab-plan (S{N+1})  ← carry forward into next session
```

### Investigation track (parallel exploratory pipeline; `sessions/investigation/`)

Structurally the SAME three skills, in investigation mode. Seeded from a free-form input
(an investigation survey output, a synthesis) instead of prior-session carry-forwards; the plan
carries MIXED gate types and `/rclab-coordinate` juggles them directly (no separate schedule).

```
free-form seed (e.g. investigation-1 survey outputs)
  → /rclab-plan --investigation n --from <seed>   ← typed wave plan; registers investigation-{n} in the index
    → /rclab-coordinate sessions/investigation/investigation-{n}/…   ← juggles compute/review/workshop gates
      → /rclab-investigate --investigation n        ← synthesis + next-investigation seed; housekeeps the index
        → /rclab-plan --investigation n+1 --from <seed>   ← the survey drives the next effort
```

- **Index**: `sessions/investigation/index.md` cross-refs every `investigation-[n]` ↔ topic / driver / status / outputs / drives. `/rclab-plan` registers; `/rclab-investigate` housekeeps.
- **Gate types are the "slots"**: in the session track, `/rclab-investigate` emits a workshop-SCHEDULE of `/rclab-review` + `/rclab-workshop` invocations. In the investigation track those become `gate_type` values (review / workshop / compute) inside one plan — plan-then-coordinate, not schedule-then-dispatch.
- **Verdict track**: investigation compute gates emit to `computations/investigation-{n}/inv{n}_gate_verdicts.txt` (`emit_verdict(track="investigation")`); review/workshop close by artifact-existence. Track-local — promote to a session to make a result permanent.

## Coordination medium at a glance

| Skill | Medium | Max agents |
|:--|:--|:--|
| `/rclab-coordinate` | Independent Agent calls, no cross-talk | unlimited per wave |
| `/rclab-review` | Independent, each writes own file | any |
| `/rclab-workshop` | Shared document, sequential Edit-based turns | exactly 2 |
| `/rclab-team` (`collaborate` mode) | Team + inbox, multi-round | 2-3 |
| `/rclab-team` (`panel` mode) | Team + inbox, specialists + writer | 2-3 |

## Common disambiguations

- **"Workshop"** in legacy session files usually meant a team-based multi-round pattern — that's now `/rclab-team --mode collaborate`. The skill `/rclab-workshop` is the 2-agent shared-document pattern.
- **"Compute session"** = `/rclab-coordinate` executing an `/rclab-plan` output. Not `/rclab-team`.
- **"Workshop-schedule"** (as a document) = the output of `/rclab-investigate`, a list of `/rclab-synthesis`-style entries to dispatch.
- **"Synthesis"** is generated either by `/rclab-review` (solo, independent) or inside a `/rclab-workshop` / `/rclab-team --mode panel` run.
- **`/rclab-solo` vs `solo`**: `/rclab-solo` is a whole-plan run with NO subagent spawning, launched AS a research agent (`claude --agent <agent>`) so the executor is still a weight-positioned specialist. It is NOT a `gate_type` — there is no `solo` gate type. `/rclab-coordinate` always DISPATCHES physics gates to their specialists; the orchestrator never computes a gate inline (it is not weight-positioned to).

## Usage — each skill's own help

Every rclab skill accepts `--help` and prints this document's relevant section. For full argument lists and phase-by-phase behavior, read the skill file directly: `.claude/skills/rclab-{name}/skill.md`.
