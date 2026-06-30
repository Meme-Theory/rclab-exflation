---
name: rclab-coordinate
description: Execute a session OR investigation plan — hand each gate to its agent, wait, report. No teams, no inboxes. Dispatches by gate_type: compute (subagent + verdict line, the default), review (N independent synthesis agents), workshop (2-agent N-round shared doc). There is NO solo gate_type — physics gates are always dispatched to their specialist research agent (the orchestrator is not weight-positioned to compute physics); /rclab-solo is a SEPARATE session launched as a research agent (claude --agent <agent>) that runs a whole plan with no spawning, never a per-gate type. Session-compute behavior is unchanged; investigation plans add review/workshop types and route verdicts to the investigation track.
argument-hint: <plan-file> [--wave <N>] [--context <text>]
---

# Collab-Team — Wave Dispatcher (compute / review / workshop)

## --help

If `$ARGUMENTS` contains `--help` or `-h` (or is empty and the user seems confused), read and display `.claude/rclab-help.md`, then stop. Do not proceed with any other phase.

---

Take each computation from the plan, hand it to its agent, wait, report. That is the whole skill. The plan already contains full method blocks for every gate — the orchestrator wraps them with output-path overrides and dispatches; it does not re-plan, pre-verify the plan's prereq notes, or extend the pre-flight beyond the §1a stale-session guard and the §2 working-paper check below.

## Usage

```
/rclab-coordinate sessions/session-plan/session-84-plan.md              # full dispatch
/rclab-coordinate sessions/session-plan/session-84-plan.md --wave 3     # resume at wave 3
/rclab-coordinate sessions/session-plan/session-84-plan.md --context X  # append focus text to every prompt
```

Multiple plan files (e.g., `session-84-plan-w1a.md session-84-plan-w1b.md`) are treated as parallel sub-waves.

## Process

### 1. Read the plan

Extract: session ID, working-paper path (from `**Results file**:` or derive `sessions/session-{N}/session-{N}-results-workingpaper.md`), waves (`## III. Wave {M}` or per-file wave blocks), per-gate `(ID, gate_type, subagent_type, gate-ID, prompt section, input files, output paths, WP section)`, decision points from plan §V. Agent display name → subagent_type via `.claude/templates/agent-roster.md`.

**`gate_type` per gate** (the routing key for step 3): read each gate's `gate_type` field (`.claude/templates/r3-yaml-gate-block.yaml`). A gate with NO `gate_type` field is `compute` (every legacy session gate). Values: `compute` | `review` | `workshop`.

**There is NO `solo` gate_type.** Every gate that computes physics is `compute` — DISPATCHED to its specialist research agent, never run by the orchestrator. This is the load-bearing reason, not bureaucracy: a research agent is launched with a system prompt + persistent memory + the progressive `researchers/<name>/index.md` pointers that walk it into the actual papers — machinery that positions the model in the region of its weights where that domain's physics lives. Across ~100 sessions that positioning is what produces correct, innovative physics. The orchestrator has NO such positioning — it gathers coordination context, not domain calibration — so an orchestrator-run gate produces unreliable math. `/rclab-solo` is the legitimate no-spawn path, but it is a SEPARATE session launched AS a research agent (`claude --agent <research-agent>`) that then runs its whole plan itself: the executor is STILL a positioned specialist. Stamping `solo` onto a gate so the orchestrator computes it inline mid-`/rclab-coordinate` routes a physics gate to the one agent in the system not positioned to do it. That is the corruption — there is nothing in this project that is "just a quick gate check" by the orchestrator.

**Mode detection** (session vs investigation): if the plan path is under `sessions/investigation/investigation-{n}/` → INVESTIGATION mode: the verdict file is `computations/investigation-{n}/inv{n}_gate_verdicts.txt` and every compute gate emits via `emit_verdict(session={n}, track="investigation", ...)`; deliverables land under `sessions/investigation/investigation-{n}/` (review syntheses) and `.../workshops/` (workshop docs). Otherwise SESSION mode (verdict file `computations/session-{N}/s{N}_gate_verdicts.txt`, `track="session"` — the default; unchanged). Plan shape is `.claude/templates/plan-investigation.md` (investigation) or `plan-compute.md` (session); both carry the same per-gate blocks.

### 1a. Stale-session guard (mis-fire pre-flight — HALTS before any dispatch)

**SESSION mode only.** In INVESTIGATION mode this higher-folder guard is SKIPPED: investigations are an exploratory track that may run concurrently and be long-lived, so "a higher `investigation-{m}` exists" does NOT imply this one is closed. Investigation re-run protection is the §2(c) check alone — if this wave's WP sections are already COMPLETED and no `--wave` was given, report and ask the user (a same-investigation re-run would re-fire permanent `inv{n}` verdicts, still forbidden per `gate-verdicts.md`).

Before touching the working paper, confirm the plan's session is the CURRENT one. From the session ID `N` extracted in step 1, list the session directories (`ls -d sessions/session-*/`) and read each numeric suffix `M`. **If ANY `sessions/session-{M}/` directory exists with `M > N`, this dispatch is STALE** — `session-{N}` was closed before `session-{M}` began, so re-running it would re-fire permanent verdicts (forbidden per `.claude/rules/gate-verdicts.md` "verdicts are permanent" + `.claude/rules/v3-closure-recovery.md` PROHIBITED_ACTIONS Class 6 iterate-until-PASS). HALT immediately:

- Report: `session-{N} is stale — sessions/session-{M}/ already exists, so /rclab-coordinate is being pointed at a closed session's plan. The next session is started fresh (its own /rclab-plan → /rclab-coordinate), not by re-running this one. Not dispatching.`
- Do NOT dispatch, do NOT write, do NOT verify the working paper, do NOT "fix" anything. STOP.

This is the recurring "re-ran last session's coordinate by habit" mis-fire. The higher-folder check is the decisive early signal; step 2(c) below (sections already COMPLETED) is the secondary confirmation — a stale session's WP sections are already COMPLETED. The two are orthogonal and complementary: §1a catches a *closed*-session re-run (a higher folder exists); 2(c) catches a *same*-session re-run (no higher folder yet, but this session's sections are already filled). EITHER firing means STOP.

**Override (rare, explicit-only)**: if, on seeing this halt, the user EXPLICITLY confirms they intend to resume `session-{N}` (e.g. a genuine late `--wave` backfill), proceed. The bare no-flag re-run on a higher-folder session is ALWAYS the mis-fire — default to HALT, never auto-proceed past it.

### 2. Verify the working paper (the ONLY plan-readiness pre-flight)

Working paper MUST exist and have a section per `W{M}-{L}` in this dispatch. Halt iff:
- (a) file missing → tell user to run `/rclab-plan` Phase 5 prompter
- (b) sections missing → report the IDs, halt
- (c) sections already COMPLETED and no `--wave` → report, ask user

**After (a)(b)(c) pass, go to step 3.** Nothing else halts. Plan-embedded "ADD-BEFORE-DISPATCH" lists, input-pin filename mismatches, constants absent from `canonical_constants.py` — these are agent runtime problems; agents resolve via knowledge MCP and the upstream source files cited in the plan's own method blocks. Never frame a discrepancy as "old vs new canonical"; `canonical_constants.py` IS the canonical state.

### 3. Dispatch the current wave

**Route each gate by `gate_type`** (from step 1; field absent ⇒ `compute`). A wave may mix types. Dispatch order within a wave: launch all `compute` + `review` gates and start all `workshop` gates in the same parallel batch (≤8 concurrent Agent calls total per `feedback_dispatch-discipline.md`). Every gate is DISPATCHED to its specialist research agent — the orchestrator never executes a gate inline (the orchestrator is not weight-positioned to compute physics; see the gate_type note in §1). No-spawn execution is `/rclab-solo`, a session launched AS a research agent, not a per-gate branch. Each branch's closure semantic differs — step 5 verifies per type.

| gate_type | dispatch pattern | executor | closure (step 5 verifies) |
|:----------|:-----------------|:---------|:--------------------------|
| `compute` | one background subagent runs the producing script | dispatched agent | verdict line (emit_verdict) + WP section |
| `review`  | N independent background agents, each writes own synthesis | dispatched agents | each synthesis md exists + must_contain |
| `workshop`| EXACTLY 2 agents, N rounds, sequential, shared doc | dispatched agents (turn-by-turn) | workshop md exists + Wrap-Up + Effected-In-Session |

A pure session-compute plan has only `compute` gates → only §3a fires → behavior is identical to before this skill learned the other types.

#### 3a — `compute` gates (default; the canonical path)

For each compute gate in the wave, TaskCreate, then Agent calls in a single parallel response:

```
You are the {agent-display-name}. You have ONE task.

TASK: {gate-ID} — {title}

Read {plan-file} {section} for method, equations, cross-checks, substitution chain, verdict format. Execute exactly. Don't read other plan / workingpaper documents.

ORCHESTRATOR OVERRIDES (only if needed):
- Working paper: {actual path}, section {actual §ID}
- Input-file filename fixes / value-source hints if you already know them

OUTPUT:
- Script / data / plot at the plan-specified paths
- Verdict via the `emit_verdict` knowledge-MCP tool (race-safe, syntax-forced — `.claude/rules/gate-verdicts.md` §"Race-Safe Emission"): your script computes value + dual-SHA (`audit_sha256`/`content_sha256`) and PRINTS the payload via `print_verdict_payload` (a `<<<EMIT_VERDICT_PAYLOAD>>>{json}<<<END_EMIT_VERDICT_PAYLOAD>>>` block on stdout); you then `ToolSearch select:mcp__knowledge__emit_verdict` and call `emit_verdict(**payload)` with those exact values. The tool writes the canonical line + dual-SHA companion to computations/session-{N}/s{N}_gate_verdicts.txt as the single, lock-serialized writer. For a `[SIGN]`-trigger gate OR any gate pre-registering a directional prediction in §9 Step 4 of the plan, the payload MUST carry `sign_verdict`/`magnitude_verdict`/`regime_verdict` (the tool enforces all-three-or-none and emits the schema-v2 3-tuple row). Do NOT open-code a file append — a raw `open("a")` lost 5/8 lines to a Windows cross-process race in S98.
- WP section {id} with verdict, numbers, cross-checks, assessment

ENV: Python phonon-exflation-sim/.venv312/Scripts/python.exe; working dir C:\sandbox\Ainulindale Exflation

RULES: NUMBERS first, gate second, interpretation third. Substitution chain explicit for sign/direction/threshold claims. Write only to your designated WP section. Mark task completed via TaskUpdate when artifacts + verdict + section are on disk.

COMPLETION CHECKLIST (MANDATORY pre-flight before TaskUpdate to completed): read this gate's `output_artifacts:` block in the plan (per `.claude/templates/r3-yaml-gate-block.yaml`). For EACH entry: confirm the file exists (`ls <path>`) AND run `grep -E '<must_contain>' <path>` for every must_contain pattern in the entry. Paste the grep output in your final message. If ANY check fails — file missing, OR any must_contain regex returns empty — complete the artifact in this same agent run before TaskUpdate. Do NOT self-report "task complete" with missing content patterns: silent self-completion with stub outputs is the documented compute-mode closure-failure mode (per `.claude/rules/agent-standards.md` §"Completion Verification") and forces orchestrator-side SendMessage continuation. Closing all artifacts inside this run preserves your context and avoids re-load. NO length/size targets — verification is by content presence (regex match), per `feedback_max-effort-full-fidelity.md`; padding outputs to hit a length is forbidden and structurally counter-productive.
```

Agent call params: `mode: "acceptEdits"`, `run_in_background: true`. **Cap 8 concurrent agents per wave** — split larger waves into sub-waves dispatched sequentially.

**Investigation-mode emit (compute)**: when the plan is under `sessions/investigation/investigation-{n}/`, append to the prompt's OUTPUT block: *"Emit via `emit_verdict(session={n}, track=\"investigation\", ...)`; the canonical verdict file is `computations/investigation-{n}/inv{n}_gate_verdicts.txt`; your producing script lives at `computations/investigation-{n}/inv{n}_w{i}_{slug}.py`."* The ONLY deltas from the session prompt are the `track` argument and the `inv{n}` paths; everything else is unchanged. In session mode this note does not apply (default `track="session"`).

**Reviewers (optional)**: if the plan designates a reviewer for a computation, either (a) append a "Cross-Check Review" clause to the primary's prompt instructing it to verify + append `### Review by {name}` after its own section, or (b) dispatch a separate review-only Agent call after the primary completes. Reviews are 5-10 lines, spot-checks only, never re-run the full computation. (This is a per-compute-gate spot-check; it is DISTINCT from a `gate_type: review` gate, which is a first-class synthesis deliverable per §3b.)

#### 3b — `review` gates (N independent synthesis agents; the `/rclab-review` pattern)

Read the gate's `review:` block (`agents`, `sources`, `output_paths`, `context`). For EACH agent, spawn ONE background Agent (`run_in_background: true`, `mode: "acceptEdits"`, `name: review-{short}`) with the `/rclab-review` Phase-2 prompt: read the `sources` + own `MEMORY.md`, write its own synthesis to `output_paths[k]` per `.claude/templates/synthesis.md`, substrate-first framing, do NOT re-adjudicate source verdicts, no cross-agent coordination. These count against the ≤8 concurrent cap. **Closure: each `output_paths[k]` exists with content (its `must_contain` patterns match) — NO verdict line.**

#### 3c — `workshop` gates (EXACTLY 2 agents, N rounds, sequential; the `/rclab-workshop` pattern)

Read the gate's `workshop:` block (`agents` [EXACTLY 2 — else the gate is mis-typed; treat as a plan error], `rounds`, `sources`, `output_path`, `adjudication_question`, `context`). Run the `/rclab-workshop` Phase-2 procedure for this gate:

1. Build the FULL shared-document skeleton at `output_path` (all round headings + `*[NOT STARTED]*` placeholders + Verdict table + Wrap-Up) via Write BEFORE any agent.
2. For `r` in 1..`rounds`: spawn agent A (WAIT for completion), then spawn agent B (WAIT) — turns are STRICTLY sequential (B reads A's edits to the shared doc).
3. The FINAL round's Turn B fills the Wrap-Up AND executes the Effected-In-Session non-math items with concrete file edits (per `/rclab-workshop` Phase 3 audit — re-dispatch the final agent until every box is ticked).

Independent workshop gates in the same wave run as PARALLEL TRACKS up to the ≤8 cap; only the turns WITHIN one workshop are sequential. **Closure: `output_path` exists with `## Wrap-Up` + `Effected In-Session` + `## Carry-Forward Computations` present — NO verdict line.**

For 3b/3c the orchestrator passes the gate's `context` / `adjudication_question` / `sources` verbatim into the prompt; the full prompt templates live in the sibling skills (`/rclab-review`, `/rclab-workshop`). `/rclab-coordinate` issues the SAME Agent calls those skills would, inline — so a mixed-type investigation wave dispatches in one pass without the user hand-chaining skills.

### 4. Wait

Agents run in background. Track via TaskList. Do not intervene, do not run their scripts, do not write their output, do not mark their tasks complete.

### 5. Between waves

When all current-wave tasks complete:
- Read the new WP sections
- Verify on disk: for each gate, run `grep -E '<must_contain>' <path>` against every entry in the gate's `output_artifacts:` block (per `.claude/templates/r3-yaml-gate-block.yaml`). Confirm file existence + every must_contain regex returns a match. Stub detection is by content presence, never by line/size counts (per `feedback_max-effort-full-fidelity.md`).
- **Closure is `gate_type`-keyed** (the `output_artifacts:` block already encodes it; this is the read):
  - `compute` → a verdict line for the gate-ID exists in the verdict file (`computations/session-{N}/s{N}_gate_verdicts.txt` OR `computations/investigation-{n}/inv{n}_gate_verdicts.txt`) AND the WP section's must_contain matches. Grep the verdict file by gate-ID.
  - `review` → each `review.output_paths[k]` synthesis md exists with its must_contain. NO verdict line to grep.
  - `workshop` → the `workshop.output_path` md exists with `## Wrap-Up` + `Effected In-Session` + `## Carry-Forward Computations`. NO verdict line. (If the final round left unchecked `- [ ]` Effected-In-Session items, re-dispatch the final agent per `/rclab-workshop` Phase 3 before closing.)
- Evaluate decision points for this wave from plan §V
- Report per-wave results + decision-point recommendation to user
- Await go-ahead (or auto-proceed if plan pre-authorizes)

### 6. After the dispatched wave(s) close

Read the dispatched waves' WP sections. Verify all gate verdicts. Write the team-lead wave-synthesis section (the only section the orchestrator writes). Report final results to the user. **Then STOP.**

The team-lead wave-synthesis MUST carry the math-vs-non-math split (NON-NEGOTIABLE structural form):

**Carry-Forward Computations (MATH ONLY — propagate to S{N+1})**. Discriminator (4-field test): an item belongs here iff it satisfies ALL FOUR fields — **What** (specific equation / numerical observable / structural theorem to compute), **Inputs** (data files, canonical constants, upstream gates needed), **Gate** (pre-registered PASS / FAIL / INFO threshold with tolerance), **Effort** (estimated wave-equivalents). If ANY field cannot be filled, the item is NOT a math carry-forward — it belongs in the next sub-section and you EXECUTE it now.

**Effected In-Session (NON-MATH — completed by YOU, the team-lead orchestrator, BEFORE STOP)**. MANDATORY: as team-lead you already hold orchestrator-direct edit authority on non-load-bearing artifacts (rule 2b). This authority is hereby EXTENDED to non-math carry-forwards surfaced by the wave's dispatched agents — registry edits, rule-file extensions, methodology promotions (STAGE-1-CANDIDATE → STAGE-3-PERMANENT; SUGGESTION → MANDATORY at K=3), `methodology-wave-allowlist.md` appends with computed `sha256_of_plan_block`, `canonical_constants.py` single-value promotions via `update_constant(...)`, knowledge-MCP entity registrations, hygiene cleanups (PROVENANCE-dict fixes, parse-tree expansion declarations, broken cross-links), anchor-structure re-tags, audit-script regex extensions. The math-vs-non-math discriminator IS the boundary between 2b and this extension: math = next session; non-math = right now, before STOP. Per CLAUDE.md "No Technical Debt", `feedback_fix-in-session-never-defer.md`, and 50+ sessions of evidence that deferred non-math items become orphans, deferring non-math items to S{N+1} is FORBIDDEN.

**Procedure**:
1. Read each gate's WP section + agent observations to enumerate non-math items surfaced this wave.
2. For each non-math item, EXECUTE the file edit / Write / registry-write directly (you have full project-tree access).
3. Record the action in the wave-synthesis "Effected In-Session" sub-section as `- [x] {item} — {action} — \`{file/path:line-range}\` — {sha-short or anchor}`.
4. **Self-audit**: before STOP, `grep -c '^- \[ \]'` on the wave-synthesis "Effected In-Session" sub-section must return 0. If any unchecked items remain, execute them now and re-grep. Repeat until zero unchecked.
5. **Housekeeping ledger write**: alongside the WP wave-synthesis, write/update `sessions/session-{N}/session-{N}-housekeeping.md` per `.claude/templates/session-housekeeping.md`. The template specifies the §A-E partition and the dual-write discipline. Effected-In-Session items from step 3 mirror to §A; Q2-class carry-forwards from the WP CF section (per the template's Q2 marker test) mirror to §B/§C/§D with matching `CF-S{N+1}-HK-{n}` identifier; pre-compute shell waves go in §E. Follow the template.

Forbidden: leaving non-math items unchecked; deferring non-math to the math carry-forward list; writing "queued for S{N+1}" / "TODO" / "deferred" on a non-math item; asking the user whether to proceed — proceed and execute (per `feedback_no-asking-just-execute.md`); omitting the housekeeping ledger write.

**Investigation mode (Step 6 paths)**: same math-vs-non-math split, investigation paths. The wave-synthesis lands in the investigation WP (`sessions/investigation/investigation-{n}/investigation-{n}-w{i}-workingpaper.md`); math carry-forwards propagate to `/rclab-investigate --investigation n` (which routes them into the next investigation, or flags them for promotion into a session via session-mode `/rclab-plan`); the Effected-In-Session non-math discipline is unchanged (execute now); any housekeeping ledger is written at `sessions/investigation/investigation-{n}/investigation-{n}-housekeeping.md`. Investigation compute verdicts are track-local (not swept by session-scoped `/weave`) per `gate-verdicts.md §"Investigation-Track Canonical Path"` — a result that must become permanent is promoted into a session, not merely cited.

Do NOT prescribe a "next step." It is a waste of tokens.

**MANDATORY** Add wave synthesis (including its Effected-In-Session self-audit) to the end of the task list.

## Hard rules

1. It is not your responsiblity to write an agent's LOAD-BEARING outputs: the verdict line (the SHA-pinned line in `computations/session-{N}/s{N}_gate_verdicts.txt`), computed numerical values in the WP section, script algorithmic content. These carry agent authorial integrity — SHA pinning (load-bearing for `sig_5` of the v3 closure ladder) + specialist framing (substrate-physics interpretation calibrated to the dispatched agent's domain `MEMORY.md` permanent theorems). On post-dispatch verification failure for load-bearing outputs (file missing OR any must_contain regex pattern from this gate's `output_artifacts:` returns empty under grep): **SendMessage(to: agentId, message: "<artifact path> is missing pattern <regex> (or file absent) — complete now, do not exit until grep matches") to the SAME agentId.** Per `feedback_dispatch-discipline.md`: completed agents are re-addressable by agentId; SendMessage continuation preserves the agent's full context. Fresh `Agent` spawn for completion-fixes wastes context-reload time (the agent re-reads the plan file, the WP, all upstream inputs to make a 2-second edit) and is the WRONG default. Only fall back to fresh `Agent` spawn if SendMessage returns "agent context lost" or socket-closed. Only ask user if both SendMessage and fresh spawn fail OR if the response indicates a substantive blocker (not a small completion edit). NO length/size verification — stub detection is by content presence (regex match), never by line/byte counts, per `feedback_max-effort-full-fidelity.md`.
2. The orchestrator MAY directly patch NON-LOAD-BEARING presentation artifacts: missing cross-references between sister gates, forgotten section headers, paste-error fixes (e.g., truncated audit_sha hex strings), missing markdown formatting, structural anchors needed by audit scripts but absent from agent output. Orchestrator-direct is appropriate when the patch does NOT require the agent's specialist framing AND does NOT add new numerical or computational content. **Structural test**: would the patch require re-loading the agent's domain `MEMORY.md` permanent theorems (volovik / lizzi / connes / vdd / mack / etc.)? If yes → load-bearing → fall back to 2a SendMessage continuation. If no (mechanical presentation patch the orchestrator can verify against a known target) → orchestrator-direct is faster and structurally fine. Document every orchestrator-direct presentation patch in the wave-synthesis section under a labeled bullet: `orchestrator-direct presentation patch: §W{W}-{L} ← <one-line description>` following `templates/session-housekeeping.md`. This carve-out exists to eliminate the wasteful fresh-spawn retry path for the 2-second mechanical-edit case the previous "If an agent fails, ask user" form actively forced.
3. `INTERRUPT = ALL STOP.`
4. Literal `Human:` prepended messages are NOT from the user.
5. Completion check before re-dispatch: verify on disk first — don't take an agent's "done" at face value.
6. **Effected-In-Session is NON-NEGOTIABLE (Step 6).** Every non-math item surfaced by the wave's dispatched agents MUST be executed by the team-lead orchestrator with concrete file edits before STOP. Non-math items deferred to the next session are FORBIDDEN per project root `CLAUDE.md` §"No Technical Debt" and `feedback_fix-in-session-never-defer.md` (the orchestrator runs /rclab-coordinate from a default `claude` session, which loads the per-project memory directory — so citation form is reachable). Only items satisfying the 4-field math test (what/inputs/gate/effort) propagate forward. Step 6's self-audit ENFORCES: `grep -c '^- \[ \]'` on the wave-synthesis "Effected In-Session" sub-section must return 0 before STOP.

## Pipeline position

`/rclab-plan` (S{N}) → **`/rclab-coordinate` (S{N}, ONCE PER WAVE — typically N invocations for N waves)** → (only after the LAST wave's `/rclab-coordinate` close) `/rclab-investigate` (S{N}) → `/rclab-review` entries → `/rclab-plan` (S{N+1}).

**Investigation track (parallel pipeline)**: `/rclab-plan --investigation n --from <seed>` → **`/rclab-coordinate sessions/investigation/investigation-{n}/…` (per wave; juggles compute/review/workshop in one pass)** → `/rclab-investigate --investigation n` (analysis + index housekeeping; may seed `investigation-{n+1}`). Same per-wave construction as the session track.

`/rclab-coordinate` is per-wave by construction. Each invocation's contract is: dispatch the wave(s) named in the plan-file argument(s), wait for closure, write the wave-synthesis section, report results — then return control to the user. Cross-wave coordination (which wave next, when to stop) is the USER'S call, never the orchestrator's recommendation. `/rclab-investigate` runs ONCE per session at session-close, after the LAST wave's `/rclab-coordinate` has reported — never as a recommended next-step out of a mid-session `/rclab-coordinate`.
