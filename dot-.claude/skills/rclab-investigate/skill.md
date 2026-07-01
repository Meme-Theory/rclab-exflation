---
name: rclab-investigate
description: Generate a workshop-schedule campaign from a just-closed session's working papers. Spawns N size-driven investigators (one per ~2000-line chunk) plus one consolidator. Investigators identify workshops + solo reviews per `.claude/rules/Investigating-Workshops.md` (workshop definition, 3-question discriminator, honest-count discipline). Consolidator writes the schedule per `.claude/templates/workshop-schedule.md` (slot structure, skill–slot mapping, invocation form). Carry-forwards (Q2 hygiene, Q3 parallel-wave, Q-other) route to the investigated wave's WP — `/rclab-plan` reads WPs, not the schedule. Also supports INVESTIGATION MODE (`--investigation n`): mines an `investigation-{n}` effort's outputs (the 31-agent survey for inv-1; per-wave WPs + review/workshop/solo deliverables + compute verdicts for inv-2+) into a `_synthesis.md` + a forward-candidate seed that drives the NEXT investigation via `/rclab-plan --investigation`, AND housekeeps `sessions/investigation/index.md` (status / outputs / drives) — see §"Investigation Mode".
argument-hint: <topic> [--session <N> | --investigation <n>] [--investigator <agent-type>] [--planner <agent-type>] [--context <file>...] [--dry-run]
---

# `/rclab-investigate` — Workshop-Schedule Campaign Generator

This skill is a **procedure**. It does not define what a workshop is and it does not define the schedule's output structure.

| File | Role | Authority over |
|:-----|:-----|:---------------|
| `.claude/skills/rclab-investigate/skill.md` (this file) | Procedure | Workflow: detect source, partition, spawn, consolidate, report. |
| `.claude/rules/Investigating-Workshops.md` | Policy | Workshop definition, 3-question discriminator, honest-count discipline, calibration corpus. |
| `.claude/templates/workshop-schedule.md` | Structure | Schedule file shape, slot definitions, skill–slot invocation mapping (SESSION mode). |
| `sessions/investigation/index.md` | Register (DATA) | Investigations index — HOUSEKEPT here in INVESTIGATION mode (§"Investigation Mode"); registered by `/rclab-plan`. |

When something feels missing from this skill, check the rule (for "what counts") or the template (for "what the output looks like") before adding to the skill. Skill = direction. Rule = constraint. Template = shape.

## `--help`

If `$ARGUMENTS` contains `--help` or `-h`, read and display `.claude/rclab-help.md`, then stop.

## Usage

```
/rclab-investigate                                       # mine the latest closed session; auto-detect
/rclab-investigate "substrate self-determination followup"
/rclab-investigate --session 86
/rclab-investigate --investigator gen-physicist
/rclab-investigate --planner phonon-first-cosmologist
/rclab-investigate --context sessions/observational_avenues.md
/rclab-investigate --dry-run                             # show manifest, stop

# Investigation mode (parallel exploratory track; see §"Investigation Mode")
/rclab-investigate --investigation 1                     # synthesize the 31-agent survey + seed investigation-2 + housekeep the index
/rclab-investigate --investigation 2                     # mine investigation-2's outputs + seed investigation-3 + housekeep the index
```

| Arg | Default | Notes |
|:----|:--------|:------|
| `<topic>` | `"S{N} workshop campaign"` | Label only. Never gates execution. |
| `--session <N>` | latest session with a WP | Source session to mine (SESSION mode). |
| `--investigation <n>` | — (presence = investigation mode) | Switches to INVESTIGATION mode (§"Investigation Mode"): mine `investigation-{n}`'s outputs → synthesis + next-investigation seed + index housekeeping. Mutually exclusive with `--session`. |
| `--investigator <type>` | `phonon-first-cosmologist` | Agent type for per-chunk investigators. |
| `--planner <type>` | `phonon-first-cosmologist` | Agent type for the consolidator. |
| `--context <file>` | none | Repeatable. Passed to consolidator. |
| `--dry-run` | false | Show manifest + chunk plan, stop before spawning. |

## Pipeline position

```
/rclab-coordinate (S{N} compute)
  →  /rclab-investigate (S{N})       ← THIS SKILL
       ⟶  Slot 1 solos via /rclab-review (parallel, ≤8 concurrent)
       ⟶  Slot 2 workshops via /rclab-workshop (sequential)
       ⟶  Slot 3 closeout via /rclab-review
  →  /rclab-plan (S{N+1})  →  /rclab-coordinate (S{N+1})
```

The campaign LIVES IN the source session's folder. It does not consume a new session number. The next session's planner (`/rclab-plan`) consumes the WP carry-forwards, not the schedule directly.

---

## Investigation Mode (`--investigation n`)

`/rclab-investigate` has two modes. **Session mode** (default; Phases 1–5 below) mines a closed session's WPs into a workshop-SCHEDULE. **Investigation mode** (`--investigation n`) mines an `investigation-{n}` effort's outputs and does two jobs:

1. **Output analysis** — synthesize the investigation's outputs into `investigation-{n}/_synthesis.md` + a forward-candidate **seed** that drives the NEXT investigation (the seed is the free-form `--from` input to `/rclab-plan --investigation {n+1}`).
2. **Index housekeeping** — update `sessions/investigation/index.md` (status / outputs / drives). `/rclab-investigate` is the SOLE housekeeper of that index per its maintained-by contract; `/rclab-plan` only registers new rows.

**Key structural difference from session mode.** In the session track this skill emits a workshop-SCHEDULE (a list of `/rclab-review` + `/rclab-workshop` invocations the user dispatches by hand). In the investigation track there is NO separate schedule: follow-ups become **typed gates in the next investigation's PLAN** — `/rclab-plan --investigation` assigns each candidate a `gate_type` (workshop / review / compute) and `/rclab-coordinate` juggles them. So the seed this mode writes is shaped to feed `/rclab-plan --from`, carrying the SAME Q1/Q2/Q3 discriminator outcomes session-mode investigators produce — but as a **`suggested gate_type`** per candidate, not as schedule slots. The schedule-then-dispatch of the session track collapses into plan-then-coordinate in the investigation track.

### Sources by investigation shape

- **inv-1 (the root survey)**: the N agent files `investigation-1/<agent-type>.md` (each: gaps `G-x` / contradictions `C-x` / assumptions `A-x` / refinements `R-x` / bridges `B-x` / `## Highest-Leverage Next Steps`). Chunk for the investigator swarm.
- **inv-2+ (a planned effort)**: per-wave WPs `investigation-{n}-w*-workingpaper.md` + review syntheses (`*-synthesis.md`) + workshop docs (`workshops/*.md`) + compute verdicts (`computations/investigation-{n}/inv{n}_gate_verdicts.txt`). Read like session-mode WPs.

### Phase deltas (run Phases 1b + 3 + 4, retargeted)

- **1b partition**: chunk the investigation's output files (one investigator per ~2000 lines / per natural unit; for inv-1 batch the agent files into chunks of a few agents each; ≤8 concurrent, batch the rest). The `--dry-run` manifest reports the chunk plan, as in session mode.
- **Phase 3 investigators**: each reads its chunk and surfaces (a) cross-output **CONVERGENCES** (the same gap/bridge raised by ≥2 agents — the highest-signal items; the `_dispatch-tracker.md` already flags several for inv-1), (b) the strongest individual gaps / contradictions / bridges, (c) per candidate the `Investigating-Workshops.md` Q1/Q2/Q3 outcome → a `suggested gate_type` (Q1a → workshop, Q1b → review, concrete-numerical → compute). Seeds land at `investigation-{n}/workshops/_seed-*.md` (underscore-prefixed intermediates, same convention).
- **Phase 4 consolidator** writes TWO files (NOT a schedule):
  - `investigation-{n}/_synthesis.md` — the cross-output synthesis: convergences, settled-vs-open, the highest-leverage clusters.
  - `investigation-{n}/_next-investigation-seed.md` — the forward seed: candidate efforts clustered by theme, each a `Highest-Leverage Next Step`-shaped item (What / pre-registered Gate / Effort / **suggested gate_type** / source anchor `<agent-file> G-3` etc.). This IS the `--from` input to `/rclab-plan --investigation {n+1}`. A rich investigation may seed SEVERAL focused next-investigations — list them as separate clusters so the user can `/rclab-plan --investigation` each.

`.claude/templates/workshop-schedule.md` + its Slot machinery do NOT apply in investigation mode (there is no schedule). The synthesis + seed are free-form, shaped to feed `/rclab-plan`.

### Index housekeeping (Role 2 — MANDATORY; orchestrator-direct edit)

After the consolidator lands, update the `investigation-{n}` row in `sessions/investigation/index.md` per that file's schema (the index is a DATA register; this is a reviewed orchestrator-direct edit, never a bulk append):

- **Status** → `ANALYZING` while mining; `CLOSED` once `_synthesis.md` + the seed are on disk.
- **Outputs** → the deliverables produced (`_synthesis.md`, the seed, and — for inv-2+ — the wave WPs + review/workshop md + the `inv{n}` verdict file). Disk is truth — list what exists, do not invent.
- **Drives** → the next investigation(s) the seed proposes (e.g. "→ investigation-2 (A_s-normalization cluster), investigation-3 (moduli-space cluster)"). When `/rclab-plan --investigation` later registers a spawned row, its Driver/Seed cell points back here — reciprocal links.

Append-only on rows; update the existing row's cells.

### Output paths + report

```
SYNTH_FILE   = sessions/investigation/investigation-{n}/_synthesis.md
SEED_FILE    = sessions/investigation/investigation-{n}/_next-investigation-seed.md
INDEX        = sessions/investigation/index.md   (Role-2 housekeeping; orchestrator-direct)
seeds        = sessions/investigation/investigation-{n}/workshops/_seed-*.md   (intermediate investigator outputs)
```

Report: investigation mined, N investigators / 1 consolidator, the synthesis + seed paths, the clusters the seed proposes (with their suggested gate_type mix), and the index row updated. Next step: `/rclab-plan --investigation {n+1} --from {SEED_FILE}`.

---

## Phase 0 — Parse & validate

1. Parse the arguments table above.
2. Verify `--investigator` and `--planner` resolve to files under `.claude/agents/`. If not, list available types and stop.
3. Verify each `--context <file>` exists. If any are missing, report which and stop.
4. **Mode select**: if `--investigation n` is present → INVESTIGATION mode (jump to §"Investigation Mode"); `--investigation` and `--session` are mutually exclusive → stop with error if both passed; verify `sessions/investigation/investigation-{n}/` exists → if not, report and stop. Absent `--investigation` → SESSION mode (Phases 1–5 below, unchanged — workshop-schedule campaign).

## Phase 1 — Detect source session + partition by shape (wave → per wave; unified → by size)

### 1a. Source session

If `--session N` was provided, use it. Else pick the latest N for which at least one WP file exists:

```python
wave_wps    = glob "sessions/session-{N}/session-{N}-w*-workingpaper.md"
unified_wp  = "sessions/session-{N}/session-{N}-results-workingpaper.md"
```

If neither exists for any N, `AskUserQuestion` which session to mine.

### 1b. Partition (wave mode → one investigator per wave; unified mode → by size)

Line count is NOT a density proxy; do not bucket waves by an aggregate total. Partition by WP shape.

**Wave mode (per-wave WP files exist):**
- ONE investigator per wave. Chunk = that wave's WP + its plan file, read in full. Small aggregate line count does NOT override this.
- Never coalesce substantive waves to hit a line target. Coalesce two adjacent waves under one investigator ONLY if both are pre-compute SHELLS or pure-setup/sequencing waves (e.g. a Wave-0 lockfile / pre-reg wave with no gate carrying an adversarial reading). When in doubt, give the wave its own investigator.
- Split a SINGLE wave across 2+ investigators only if that wave's WP > ~3K lines; align splits to `### §`-anchors.
- Concurrency cap ≤ 8 (`feedback_dispatch-discipline.md`): > 8 substantive waves → dispatch in batches (8, then the rest), waiting for each batch to finish. Do NOT shrink investigator count to fit under 8 — BATCH.
- Cross-wave tension detection = CONSOLIDATOR's job (it reads every seed). Investigators go deep on one wave each.

**Unified mode (one `*-results-workingpaper.md`, no per-wave files):** no wave boundaries → line count drives N.

| Unified-WP lines | N investigators | Notes |
|:-----------------|:----------------|:------|
| ≤ 2K | 1 | Small unified WP (S82-era). |
| 2K – 10K | round(lines / 2000) | ~2000 lines each, aligned to `### §`-anchors. |
| 10K – 30K | 5–12 | ~2000 lines each. |
| > 30K | cap at 12 | `/rclab-plan --fanout` should have prevented this upstream. |

```python
if wave_wps:
    chunks = [[wp] for wp in natural_sort(wave_wps)]   # one wave per chunk
    chunks = coalesce_only_shell_or_pure_setup(chunks) # NEVER substantive waves
    # split a single >3K-line wave by ### §-anchor; dispatch in batches of <= 8
else:
    N = pick_N_by_size(wc -l unified_wp)               # round(lines/2000); cap 12
    chunks = partition_lines_by_size(unified_wp, N, target_lines=2000, align_to="### §W")
```

Refs: `feedback_session-process.md` (unified-WP size split); `feedback_session-process.md` (wave = natural unit).

### 1c. Output paths

```
SESSION_FOLDER     = sessions/session-{N}/
WORKSHOPS_SUBDIR   = sessions/session-{N}/workshops/
SCHEDULE_FILE      = sessions/session-{N}/session-{N}-workshop-schedule.md
SEED_FILE({stem})  = sessions/session-{N}/workshops/_seed-{stem}.md
```

`{stem}` = wave id (`w0a`, `w12`) for per-wave shape; `unified-{i}` for unified shape. Underscore prefix marks seeds as intermediate.

Create `WORKSHOPS_SUBDIR` if missing. If `SCHEDULE_FILE` already exists, `AskUserQuestion` overwrite / cancel.

## Phase 2 — Build manifest + dry-run

| Source | Path | Required |
|:-------|:-----|:--------:|
| Working papers | `session-{N}-w*-workingpaper.md` or `session-{N}-results-workingpaper.md` | YES |
| Gate verdicts | `computations/session-{N}/s{N}_gate_verdicts.txt` | YES |
| Results index | `sessions/session-{N}/session-{N}-results-index.md` | optional |
| Per-wave / unified plans | `sessions/session-plan/session-{N}-plan*.md` | optional |
| Permanent results registry | `sessions/permanent-results-registry.md` | optional |
| Investigator rule | `.claude/rules/Investigating-Workshops.md` | required (read by every investigator + consolidator) |
| Output template | `.claude/templates/workshop-schedule.md` | required (read by consolidator) |
| Extra `--context` files | from flag | optional |

If `--dry-run` is set, print: topic, source session, mode (wave/unified), aggregate line count, N investigators, chunk plan (one row per chunk: id, files or line-range, lines), output paths, agent types. Then stop.

## Phase 3 — Spawn per-chunk investigators

Spawn N investigators using `--investigator` agent type, in **batches of ≤ 8** (project rule `feedback_dispatch-discipline.md`). Background, `mode="acceptEdits"`, `name=f"inv-{stem}"` (no `effort` param on the Agent tool; depth inherits from the orchestrator). Wait for the whole batch before launching the next.

### Investigator prompt

The prompt is short. It points the agent at the rule (which is the only authoritative source for what to look for) and at the chunk it owns. It does not re-encode the rule.

```
You are investigating Session {N} for the workshop-schedule campaign.

## Read first (mandatory before producing any candidate)

- `sessions/evoi-framework.md` §1–§4 (EVOI tiers) + §6 (actionable queue) — hold open while reading the WPs. For every open item / tension a WP surfaces: note its EVOI tier if already listed; if it is a NEW high-leverage open item ABSENT from §1–§4, flag it under cross-wave flags so the consolidator routes it INTO the EVOI table (via the wave's WP CF → `/rclab-plan` Step 1c-REGISTERS maintain). New frontiers must land in the guiding star, not only in scattered WPs.

1. `.claude/rules/Investigating-Workshops.md` — this is the authoritative source for:
   - the four-condition workshop definition
   - the "is NOT a workshop" list (solo computes, verification gates, registry-state hygiene, parallel-compute-wave structures, etc.)
   - the 3-question discriminator (Q1 math/physics → workshop-eligible; Q2 hygiene / framework-issue → WP CF; Q3 parallel-compute-wave → WP CF wave-together) — first YES wins
   - honest-count discipline (do not pad; "no candidates" is valid)
2. `.claude/templates/workshop-schedule.md` — so you understand what the consolidator will write your candidates into. You do not write the schedule; you write a seed.

## Your chunk

Chunk id: {chunk_id} of {N_total}
{Per-wave shape: list of WP files to read in full.}
{Unified shape: (file, start_line, end_line) — Read with offset/limit ≤ 200 lines per call per the project's ~30KB Read-tool silent-truncation rule.}
Plan files referenced by your waves: {list}

## Procedure

1. Read the rule in full FIRST.
2. Read your assigned chunk. Read each referenced plan file.
3. Grep `computations/session-{N}/s{N}_gate_verdicts.txt` for gate IDs in your range.
4. For each wave in your chunk, check SHELL-only status: all gates `Status: NOT STARTED` in the WP AND no matching `s{N}_w{stem}_*` artifacts (Glob) AND no matching gate-IDs in the verdict file (grep). If yes, emit `## Not investigated — wave w{stem} is pre-compute shell` and skip the wave in steps 5-6. Do NOT create a `CF-S{N+1}-W{stem}-WAVE-EXECUTION` carry-forward. Per rule §"is NOT" item 9.
5. Identify candidate tensions per the rule's §"How to identify a real workshop in session substance".
6. Surface (don't resolve) any candidate that depends on or conflicts with another wave's result under `## Cross-wave flags`, citing both. One investigator per wave means no investigator sees cross-wave tensions — the consolidator adjudicates them from these flags.
7. Apply the 3-question discriminator from the rule to EVERY candidate. First YES wins.
   - Q1 YES → workshop-eligible. Sub-classify per the rule's §"Discriminating decision":
     - Q1a (cross-rebuttal essential to converge) → Slot 2 workshop entry
     - Q1b (independent reading suffices) → Slot 1 solo-review entry
     - Default to Slot 1 when uncertain — workshops are expensive.
   - Q2 YES → carry-forward (route to WP, NOT schedule).
   - Q3 YES → carry-forward wave-together (route to WP, NOT schedule).

## Write your seed

Output: `sessions/session-{N}/workshops/_seed-{chunk_id}.md`

Use these headings (the rule + template-aligned shape; consolidator depends on them):

```
# Seed — Chunk {chunk_id} ({chunk_description})

**Date**: {today}   **Investigator**: {agent-type}   **Source**: {chunk spec}
**Wave summary**: <PASS/FAIL/INFO counts per wave, brief structural reading>

## Slot 1 candidates — solo reviews (`/rclab-review`)
(Q1-YES, Q1b: independent reading suffices)

### S1-1 — <one-line title>
**What this answers**: <question + source anchors: gate IDs, verdict lines, §-anchors>
**Why solo, not workshop**: <1-2 sentences — no cross-rebuttal needed>
**Agents**: <agent-type> (default 1 = primary author of the question)
**Source anchors**: <gate IDs, §-anchors, registry slots>
**Output**: <what structural questions the synthesis answers>

## Slot 2 candidates — workshops (`/rclab-workshop`)
(Q1-YES, Q1a: cross-rebuttal essential)

### S2-1 — <one-line title naming the tension>
**Tension**: <2-4 sentences — competing claims, cited gate IDs / numeric anchors>
**Why workshop, not solo**: <1-2 sentences — cross-rebuttal genuinely converges>
**Agents (EXACTLY 2)**: <Agent-A>, <Agent-B>
**Adjudication question**: <(a)(b)(c)(d) specific sub-questions>
**Rounds**: 2 default; 3 only with explicit R1=steelman / R2=rebuttal / R3=converge rationale
**Output**: <pre-registered gate / theorem / methodology rule / structural verdict>

## Cross-wave flags (surface for consolidator; NOT resolved here)
- <this wave's result X depends on / conflicts with wave wY's result Z — cite both>

## Carry-forwards (route to investigated wave's WP CF section, NOT this schedule)

- **[Q2-hygiene]** — <registry-state / hygiene / gate-finalization item; name the slot or rule>
- **[Q3-wave-together]** — <parallel-compute-wave item; list N axes + AND-closeout>
- **[Q-other]** — <solo compute follow-ups, verification gates that aren't workshops>

## Not investigated (only if any waves in your chunk are pre-compute shells; per rule §"is NOT" item 9)

- **wave w{stem}** — <one sentence stating SHELL state: all gates `Status: NOT STARTED`, no `s{N}_w{stem}_*` artifacts, no matching verdict entries>

## Wave-by-wave digest (consolidator background)

<concise per-wave summary: gates / verdicts / standout findings>
```

If your chunk produces no Slot 1 and no Slot 2 candidates, write `## No candidates` with one paragraph explaining why (settled methodology, clean verdicts, no cross-wave conflicts). You may still list `## Carry-forwards` items — those are not schedule entries by definition.

## Constraints (delegated to the rule)

- Apply the rule's honest-count discipline. Typical: 0–4 Slot 1, 0–2 Slot 2 per chunk.
- Do not propose duplicates of any existing file under `sessions/session-{N}/workshops/` — Glob the directory first.
- Modify only your seed file.
- Do not read other chunks' files / line ranges.
```

### Phase 3 close

After all batches complete, for each chunk verify the seed exists, has either a candidates section with ≥ 1 entry or a `## No candidates` paragraph, and is not stub-shaped (< 2 content lines under each section). Re-dispatch any stub-shaped seed once with the same prompt. If a seed remains missing or stub after one retry, report which chunk failed and pause for user direction — do not silently proceed.

## Phase 4 — Spawn consolidator

Spawn ONE consolidator using `--planner` agent type. Background, `mode="acceptEdits"` (no `effort` param on the Agent tool; depth inherits from the orchestrator).

### Consolidator prompt

Short. Points at the template (output shape) and the rule (re-applied discriminator). Does not re-encode either.

```
You are consolidating per-chunk investigation seeds into the unified workshop-schedule for Phonon-Exflation Cosmology Session {N}.

## Read first (mandatory)

1. `.claude/templates/workshop-schedule.md` — this defines the schedule's structure, the 3-slot organization, the skill–slot invocation mapping (Slot 1 → /rclab-review; Slot 2 → /rclab-workshop; Slot 3 → /rclab-review), the context-string fidelity expectations, the deliverable table, and the Planning Input Checklist. Follow it exactly.
2. `.claude/rules/Investigating-Workshops.md` — re-apply the 3-question discriminator to every candidate the investigators surfaced. Trust your discriminator over the seed's tag when they conflict; investigators sometimes mis-classify (S88 W13 calibration in the rule's §"Calibration corpus (failures)" is the reference).
3. All seeds at `sessions/session-{N}/workshops/_seed-*.md`. Read every one in full.

## Read for cross-reference (as needed)

- `computations/session-{N}/s{N}_gate_verdicts.txt`
- `sessions/session-{N}/session-{N}-results-index.md` (if wave mode)
- `sessions/permanent-results-registry.md` (by §-anchor when a candidate references one)
- `--context` files: {list}

## Procedure

1. Aggregate every candidate from every seed, retaining source-seed attribution. Also collect every `## Cross-wave flags` entry: a flag naming a genuine cross-wave CONTRADICTION (two waves' results that cannot both hold) is itself a workshop candidate — run it through the discriminator in step 2. A flag that is a dependency/disambiguation (not a contradiction) feeds dedupe/coalesce in step 4 and is otherwise noted, not scheduled.
2. Re-apply the rule's 3-question discriminator to each candidate. Re-tag where the investigator was wrong.
3. Partition by discriminator outcome:
   - Q1 YES (with Q1a vs Q1b sub-classification) → schedule entries (Slot 1 / Slot 2 / Slot 3).
   - Q2 / Q3 / Q-other → carry-forwards (do NOT go in the schedule; see step 6).
   - `## Not investigated — wave w{stem} is pre-compute shell` declarations → drop any `CF-S{N+1}-W{stem}-WAVE-EXECUTION` or analogous "wave-execution" CF the seed lists; do NOT append to any WP. Verify SHELL state by Glob/grep before dropping; if substantive content exists, surface to the user. Per rule §"is NOT" item 9.
4. Deduplicate + coalesce Slot 1 and Slot 2 entries when multiple seeds surface overlapping candidates. The merged entry's Why cites all source seeds.
5. Order Slot 2 by independence — non-overlapping entries can dispatch parallel through external orchestration; overlapping entries go sequential. (Skill-side dispatch is always sequential through the Skill tool; the ordering hint informs the user's downstream choices.)
6. Lift every Q2 / Q3 / Q-other item to the investigated wave's WP CF section at `sessions/session-{N}/session-{N}-w{stem}-workingpaper.md` §"Carry-Forward Computations" using a fresh `CF-W{stem}-{N}` identifier and a 4-field block (What / Inputs / Gate / Effort) per `feedback_fix-in-session-never-defer.md`. Tag Q2 items "registry-hygiene compute carry-forward"; tag Q3 items "parallel-wave-together compute structure". These items do not appear in the schedule. `/rclab-plan` consumes the WP, not the schedule — anything routed only to the schedule is invisible to the next-session planner. Skip any wave with a `## Not investigated` declaration.
7. Write the schedule to `sessions/session-{N}/session-{N}-workshop-schedule.md` strictly per the template. Every entry is a fully-specified slash-command invocation matching its slot's skill (Slot 1 / Slot 3 → `/rclab-review`; Slot 2 → `/rclab-workshop`).

## Constraints (delegated to the template + rule)

- The template's skill–slot mapping is load-bearing. Never emit `/rclab-review --type workshop --rounds N --agents A,B` — that flag combination does not exist on `/rclab-review`. Workshop semantics are encoded by `/rclab-workshop`. (Calibration: S88 2026-05-07 schedule emitted 34 entries under that invalid form; user halted dispatch.)
- Context strings: full-fidelity. Every specific gate ID, numeric anchor, claim, adjudication rule the entry needs. No "see source docs" or "appropriate context".
- Every invocation context demands the 4-field carry-forward (what / inputs / gate / effort) per `feedback_fix-in-session-never-defer.md`.
- Concurrency: if Slot 1 has > 8 entries, split into Slot 1a / Slot 1b per `feedback_dispatch-discipline.md`.
- Slot 3 invocations must reference Slot 2 outputs "if landed" so they degrade gracefully.
- No length targets in any context — content requirements only.
- Do not invent candidates. Aggregate, deduplicate, partition. If you think something critical is missing, surface it to the user in your terminal output (NOT in the schedule file).
- End the schedule with the template's Deliverable Table and Planning Input Checklist sections.

## Output

1. `sessions/session-{N}/session-{N}-workshop-schedule.md` — the schedule.
2. Appended CF blocks in `sessions/session-{N}/session-{N}-w{stem}-workingpaper.md` §"Carry-Forward Computations" for each Q2 / Q3 / Q-other item. Append-only; preserve any pre-existing CF blocks.

Do not modify seed files. Do not modify any other file.
```

### Phase 4 close

After the consolidator returns, verify:

1. `SCHEDULE_FILE` exists.
2. It has Slot 1, Slot 2, Slot 3 sections (the template's structure).
3. It has the Deliverable Table and Planning Input Checklist sections.
4. Every Slot 1 invocation uses `/rclab-review` (no `--type`, no `--rounds`).
5. Every Slot 2 invocation uses `/rclab-workshop` with exactly two agents in `--agents` and an explicit `--rounds`.
6. Every Slot 3 invocation uses `/rclab-review`.
7. For each `## Not investigated — wave w{stem} is pre-compute shell` declaration in any seed, verify no `CF-S{N+1}-W{stem}-WAVE-EXECUTION` or analogous "wave-execution" CF was appended to that wave's WP. If one was, report and offer to revert. Per rule §"is NOT" item 9.

If any check fails: report and suggest re-spawning the consolidator with feedback, or manual repair.

## Phase 5 — Final report

```
=== /rclab-investigate COMPLETE ===

Topic: "{topic}"
Source: S{N} ({mode}, {N_chunks} chunks, ~{aggregate_lines} lines aggregated)
Next compute: S{N+1}

Generated:
  {SCHEDULE_FILE}                                          {lines}
  sessions/session-{N}/workshops/_seed-*.md (×{N_chunks})  {total seed lines}
  CF blocks appended to: {list of wave WP files touched}

Investigator type: {investigator}  (×{N_chunks} dispatches)
Consolidator type: {planner}       (×1 dispatch)

Slot breakdown: {N_solo} Slot 1 solos + {N_workshop} Slot 2 workshops + {N_closeout} Slot 3 closeout = {total} entries
Planning Input Checklist: {count} forward items for S{N+1}

Next step: dispatch Slot 1 in parallel (≤8 concurrent), then Slot 2 sequentially through the Skill tool, then Slot 3. Each invocation is copy-paste-ready per its slot's skill.
```

---

## Safety rules

1. Never overwrite existing files without user confirmation (Phase 1c collision check).
2. Never spawn teams — solo agents only. No TeamCreate, no SendMessage.
3. Never execute the syntheses the schedule describes. Schedule-only deliverable.
4. Never modify MEMORY.md, agent memory, knowledge index, or any rule / template file. In SESSION mode the investigator-consolidator pipeline produces seeds, the schedule, and the WP CF appends — nothing else. In INVESTIGATION mode it ALSO writes `investigation-{n}/_synthesis.md` + `_next-investigation-seed.md` AND housekeeps `sessions/investigation/index.md` (a DATA register — Role 2; orchestrator-direct reviewed edit, append-only on rows, never a bulk dump). The index is the ONLY register this skill edits.
5. Concurrency cap: ≤ 8 concurrent investigators per `feedback_dispatch-discipline.md`. Batch dispatch above that.

## Error handling

| Condition | Action |
|:----------|:-------|
| Empty topic | Auto-generate per Phase 0 default — never stop. |
| Agent type not found | List available types, stop. |
| `--context` file missing | Report which, stop. |
| Source session has no WP material | AskUserQuestion: name a session with WPs, or stop. |
| Both `--session` and `--investigation` set | Stop with error (mutually exclusive modes). |
| `--investigation n` but `investigation-{n}/` missing | Report, stop. |
| Investigation has no outputs yet (no agent files / WPs / deliverables) | Report what's on disk; if a survey is mid-flight (some agent files present), proceed on what exists and note the partial count; if empty, stop. |
| `_synthesis.md` / seed collision | AskUserQuestion: overwrite / cancel. |
| Schedule file collision | AskUserQuestion: overwrite / cancel. |
| Investigator returns empty or stalls | One retry on that chunk; if still empty, pause for user direction. |
| Seed file stub-shaped | Same as stall — one retry, then pause. |
| Consolidator stalls | Report; suggest different `--planner` type or manual consolidation from seeds. |
| Consolidator schedule has 0 entries while seeds collectively had > 0 candidates | Report; ask whether to re-spawn with feedback or accept. |
| Consolidator schedule has 0 entries and all seeds were "no candidates" | Accept — campaign is genuinely empty. Rare but valid per the rule. |

---

## Notes

- **Default investigator + consolidator type** `phonon-first-cosmologist` fits both per-chunk multi-domain reading and the consolidator's cross-domain composition. Override `--investigator` for single-domain source material; override `--planner` for a different consolidator style.
- **Auto-detected source session** is the highest N for which any WP file exists. Override with `--session N` to retroactively run on an earlier session.
- **Seeds are intermediate**, not deliverables — `_seed-*.md` underscore prefix marks that. They live in `sessions/session-{N}/workshops/` alongside the actual workshop output files (no underscore) that downstream `/rclab-workshop` dispatches will create.
- **Wave-mode and unified-mode carry identical content.** Partition is size-driven, identical for both shapes. Per-wave is preferred at compute time (S87 W1b lesson — agents in a unified WP append at the bottom and ignore prebuilt sections), but `/rclab-investigate` treats both identically.
