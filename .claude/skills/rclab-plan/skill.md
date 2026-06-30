---
name: rclab-plan
description: Plan the next compute session — mechanically gather carry-forwards from the prior session's working papers, partition into waves by reviewer-origin theme, spawn a per-wave planner swarm that writes full-fidelity gate blocks, validate upstream pins, optionally consolidate, then spawn working-paper prompters. Also MAINTAINS the forward registers (EVOI, atlas-08 open questions, open-channel-ledger, atlas-04 status) from the just-mined session and CONSUMES them as a co-equal planning source alongside WP carry-forwards (Phase 1c-REGISTERS — plan-time doubles as the session wrap-up). Defaults to fanout (per-wave plan files + per-wave working papers) per S87 W1b lesson. For workshop-schedule campaigns derived from a just-closed session, use `/rclab-investigate` instead. Also supports INVESTIGATION MODE (`--investigation [n] --from <seed>`): plans an `investigation-{n}` effort in the parallel `sessions/investigation/` exploratory track from a free-form seed (e.g. an investigation survey output) into a MIXED-TYPE wave plan (compute / review / workshop gates), and registers the effort in the investigations index — see §"Investigation Mode".
argument-hint: <topic> [--session <N>] [--investigation [n]] [--from <seed>...] [--waves <N>] [--consolidate|--fanout] [--planner <agent-type>] [--prompter <agent-type>] [--context <file>...] [--dry-run]
---

# `/rclab-plan` — Next-Session Plan & Working-Paper Bootstrap

This skill is a **procedure**. It does not define what a gate block looks like, what a plan file looks like, what counts as a carry-forward, or what disciplines a plan must satisfy. Those live in templates and rules.

| File | Role | Authority over |
|:-----|:-----|:---------------|
| `.claude/skills/rclab-plan/skill.md` (this file) | Procedure | Workflow: gather → partition → swarm → validate → consolidate? → prompt → report |
| `.claude/templates/plan-compute.md` | Shape | Plan-file structure (consolidated + per-wave + plan-index) — SESSION mode |
| `.claude/templates/plan-investigation.md` | Shape | Plan-file structure for INVESTIGATION mode (same shapes; mixed gate types; investigation namespace) |
| `sessions/investigation/index.md` | Register (DATA) | Investigations index — REGISTERED here in investigation mode (§"Investigation Mode"); housekept by `/rclab-investigate` |
| `.claude/templates/pru-pre-registration-template.md` | Shape | Per-gate PRU block + R3 YAML scaffold |
| `.claude/templates/r3-yaml-gate-block.yaml` | Shape | 8-item PRDR YAML schema (consumed by `_yaml_gate_validator.py`) |
| `.claude/templates/workingpaper.md` (+ `examples/workingpaper-shell-example.md`) | Shape | Working-paper dispatch shell |
| `.claude/templates/agent-roster.md` | Shape | Agent-type catalog for `--planner`, `--prompter`, and gate-block `agent_type` fields |
| `.claude/rules/epistemic-discipline.md` | Policy | PRU Class 8, PRDR, Source-Reconciliation, Layer Decomposition |
| `.claude/rules/gate-verdicts.md` | Policy | Verdict-line schema, canonical verdict-file path, `verdict_source` discipline |
| `.claude/rules/wave-classification.md` + `methodology-wave-allowlist.md` | Policy | METHODOLOGY vs COMPUTE classification (M1–M4 conjunction); allowlist append at plan-freeze |
| `.claude/rules/cross-pillar-bridge-anatomy.md` | Policy | 5-anatomy + 3-level discipline for cross-pillar bridge gates |
| `.claude/rules/substrate-first-canonical-sourcing.md` | Policy | Pin provenance; SCHEMATIC vs FULL physical level pin |
| `.claude/rules/regulator-pin-discipline.md` | Policy | `a_n^{regulator}` tagging; SCHEMATIC convention suffix |
| `.claude/rules/math-scripts.md` | Policy | Substitution chain MANDATORY for sign/direction; canonical_constants imports; compute environment |
| `.claude/rules/phononic-framing.md` | Policy | Substrate-IS framing in every gate block's `substrate_framing` field + agent dispatch prompt |
| `.claude/rules/mechanical-closure-discipline.md` | Policy | Upstream-blocked prereq closure honesty discipline |
| `.claude/rules/Investigating-Workshops.md` | Policy | Cross-reference: carry-forwards live in WP §"Carry-Forward Computations", NOT the workshop schedule |
| `.claude/rules/output-standards.md` | Policy | Action-item 7-field format; carry-forward numerical-vs-structural separation |
| `feedback_fix-in-session-never-defer.md` + `feedback_fix-in-session-never-defer.md` | Policy | 4-field CF spec + no hygiene padding |
| `feedback_dispatch-discipline.md` + `feedback_session-process.md` | Policy | ≤8 concurrent dispatch cap; size-driven partition |
| `feedback_max-effort-full-fidelity.md` | Policy | Per-wave planner prompts are not abbreviated, even late in a session |
| `sessions/evoi-framework.md` + `Atlas/atlas-08-open-questions.md` + `Atlas/atlas-04-assumptions.md` + `registry/open-channel-ledger.md` | Forward registers (DATA) | Maintained + consumed by Phase **1c-REGISTERS** — the framework's forward direction |
| `.claude/rules/capstone-hygiene-gate.md` + `feedback_framework-hygiene.md` + `feedback_mack-bridge-role.md` | Policy | Register-maintenance discipline: status-tag reconciliation, curated-doc reviewed patches, mack sole-writer of the observational surface |

When something feels missing from this skill, check the rule (for "what's required") or the template (for "what the output looks like") before adding to the skill. Skill = direction. Rule = constraint. Template = shape.

## `--help`

If `$ARGUMENTS` contains `--help` or `-h`, read and display `.claude/rclab-help.md`, then stop.

## Usage

```
/rclab-plan                                       # bootstrap S{N+1} from S{N} carry-forwards, fanout default
/rclab-plan --session 90                          # pin the session number
/rclab-plan --consolidate                         # single plan + single working paper
/rclab-plan --planner phonon-first-cosmologist    # override default planner
/rclab-plan --waves 10                            # override auto-partition wave count
/rclab-plan --context sessions/observational_avenues.md
/rclab-plan "BCS gap closure"                     # cosmetic topic label only
/rclab-plan --dry-run                             # gather + partition, stop before planner dispatch

# Investigation mode (parallel exploratory track; see §"Investigation Mode")
/rclab-plan --investigation --from sessions/investigation/investigation-1/_synthesis.md   # auto-next n, seed from a synthesis
/rclab-plan --investigation 2 --from "sessions/investigation/investigation-1/connes-ncg-theorist.md"  # pin n=2, seed from one agent's survey
/rclab-plan --investigation 2 --from "sessions/investigation/investigation-1/*.md"        # seed from the whole survey (glob)
```

| Arg | Default | Notes |
|:----|:--------|:------|
| `<topic>` | `"S{N} carry-forward plan"` | Cosmetic label. NEVER scopes execution — every run tests the full carry-forward (S83 close: "the topic is just a name — we test the entire carry-forward"). |
| `--session <N>` | latest plan number + 1 | Session ID for the new plan (SESSION mode). |
| `--investigation [n]` | — (presence = investigation mode; `n` auto-next) | Switches to INVESTIGATION mode (§"Investigation Mode"). Bare → auto-next `investigation-{n}`; `n` pins. Mutually exclusive with `--session`. |
| `--from <seed>` | — (REQUIRED in investigation mode) | Free-form seed input: an investigation agent's survey output, a `_synthesis.md`, or a file/glob/dir of agent files. Repeatable. The seed IS the scope (analog of WP carry-forwards in session mode). |
| `--waves <N>` | auto-partition by theme | Wave count; orchestrator may still split a wave that stalls. |
| `--consolidate` / `--fanout` | `--fanout` (S87 W1b lesson) | Mutually exclusive. Fanout = per-wave plan + per-wave WP. Consolidate = single files. |
| `--planner <type>` | `gen-physicist` | Cross-reviewer fallback planner. Per-wave planners default to the reviewer-origin owner (Phase 1c). |
| `--prompter <type>` | `gen-physicist` | Working-paper prompter agent. |
| `--context <file>` | none | Repeatable. Folded verbatim into the context file for planners. |
| `--dry-run` | false | Phase 1 only; do not spawn planners. |

`--fanout` is default per S87 W1b: runtime agents working on a unified WP appended new sections at the bottom of the monolith instead of filling prebuilt sections; per-wave WPs eliminate the failure mode by construction. Use `--consolidate` only for small sessions (≤4 waves, ≤4K aggregate WP lines).

## Pipeline position

```
/rclab-coordinate (S{N} compute)  →  /rclab-investigate (S{N})  →  workshops & reviews
                                              ↓
                                        WP carry-forwards  (per-wave §"Carry-Forward Computations")
                                              ↓
                                  /rclab-plan (S{N+1})  ← THIS SKILL
                                              ↓
                                  /rclab-coordinate (S{N+1})
```

Per `Investigating-Workshops.md §"Cross-references"`: carry-forwards live in the source session's WP §"Carry-Forward Computations". `/rclab-plan` reads the WP — NOT the workshop schedule. Anything routed only to the schedule is invisible to this skill.

**Plus (1c-REGISTERS):** `/rclab-plan` also MAINTAINS the forward registers (EVOI, atlas-08 open questions, open-channel-ledger, atlas-04 status) from the mined session, then CONSUMES them as a co-equal planning source — so a live channel with no WP carry-forward is still planned, and the registers don't silently rot. Plan-time doubles as the session wrap-up (there is no separate wrap-up command).

---

## Investigation Mode (`--investigation`)

`/rclab-plan` has two modes. **Session mode** (default; everything outside this section) plans `S{N+1}` from `S{N}` WP carry-forwards + forward registers. **Investigation mode** (`--investigation [n] --from <seed>`) plans `investigation-{n}` for the parallel exploratory track at `sessions/investigation/`, seeded from a **free-form input** instead of prior-session carry-forwards. The pipeline shape is identical (gather → partition → swarm → validate → prompt → report); the deltas are concentrated here. Output shape per `.claude/templates/plan-investigation.md`. The investigations track and its index are documented at `sessions/investigation/index.md`.

### Trigger + number resolution

- `--investigation` (bare) → auto-next: glob `sessions/investigation/investigation-*/`, pick highest existing `n`, new `n = max+1`. Minimum 2 — `investigation-1` is the manual root survey, never planned.
- `--investigation n` → pin `n`. If `investigation-{n}/` already has a plan, AskUserQuestion overwrite / next / cancel (same collision protocol as session mode, Phase 1a).

### Paths (override Phase 1a)

```
INV_DIR            = sessions/investigation/investigation-{n}/
SEED_FILE          = sessions/investigation/investigation-{n}/investigation-{n}-seed.md      (Phase-1b digest; the CONTEXT_FILE analog)
PARTITION_FILE     = sessions/investigation/investigation-{n}/investigation-{n}-partition.md
PLAN_FILE          = sessions/investigation/investigation-{n}/investigation-{n}-plan.md       (consolidate)
PLAN_INDEX         = sessions/investigation/investigation-{n}/investigation-{n}-plan-index.md (fanout)
WAVE_PLAN_FILE(i)  = sessions/investigation/investigation-{n}/investigation-{n}-plan-w{i}.md
WAVE_WP_FILE(i)    = sessions/investigation/investigation-{n}/investigation-{n}-w{i}-workingpaper.md
VERDICT_FILE       = computations/investigation-{n}/inv{n}_gate_verdicts.txt                  (compute gates only)
```

### 1b-delta — gather from the seed, not WP carry-forwards

Instead of mining a prior session's WP §"Carry-Forward Computations", READ the `--from` seed(s) in full and translate the (regular) survey structure into candidate gate items. The investigation-1 agent files (and any like them) carry a fixed shape:

| Seed section | Becomes |
|:-------------|:--------|
| `## Highest-Leverage Next Steps` (3-5 items) | The PRIMARY source — each item already states a pre-registered gate + effort + bridge linkage; lift it near-verbatim into a gate item. |
| `## 5. UNTRAVELED BRIDGES` (B-x) | Candidate gates: a bridge whose resolution needs adjudication between two competing readings → workshop; a bridge needing a synthesis/characterization → review; a bridge with a concrete numerical test → compute. |
| `## 1.-4.` GAPS (G-x) / CONTRADICTIONS (C-x) / ASSUMPTIONS (A-x) / REFINEMENTS (R-x) | Context + candidate items wherever a concrete gate is stated; a C-x with two genuinely-competing readings is a strong workshop seed. |

Each candidate records: the 4-field-equivalent (What / Inputs / Gate / Effort), its **gate_type** (see 1c-delta), and its **seed anchor** (`<agent-file> G-3` / `B-1` / `next-step 4`). No invented items — the seed is the scope, exactly as WP carry-forwards are the scope in session mode (Safety rule 7 carries over). Deduplicate convergent items across seed files (the dispatch-tracker already flags cross-agent convergences — e.g. the A_s amplitude-normalization cluster surfaced by 5 agents). Write `SEED_FILE` (the `CONTEXT_FILE` analog): deduped candidate table + per-item seed-anchor + source manifest + any `--context` files folded verbatim. No MEMORY/verdict/index dumps — planners query MCP directly.

### 1c-delta — partition + assign gate_type

Bucket by theme/domain (owner = the seed author's domain — connes items → connes-ncg-theorist owns that wave, etc.). Then assign **gate_type** to each item by applying the `.claude/rules/Investigating-Workshops.md` Q1/Q2/Q3 discriminator (the SAME decision the session pipeline makes at `/rclab-investigate` time — here it is made at plan time, because the investigation plan IS the schedule):

- concrete compute with a pre-registered numerical gate + effort → **compute** (whether large or small; "one reasoning thread vs many" is NOT a gate_type axis).
- a tension with two genuinely-competing readings where cross-rebuttal is essential to converge (Q1a) → **workshop** (EXACTLY 2 agents).
- independent reading + write-up — "synthesize / characterize / survey X" (Q1b) → **review** (1+ agents, default 1 = question owner).

**There is NO `solo` gate_type.** Every physics gate is `compute` — dispatched to its specialist research agent. The reason is load-bearing, not procedural: a research agent's system prompt + memory + the progressive `researchers/<name>/index.md` pointers position the model in the weight-region where that domain's physics actually lives (the project's ~100-session-proven innovation mechanism); the orchestrator has no such positioning and is not trusted to compute. `/rclab-solo` is the legitimate no-spawn path, but it is a SEPARATE session launched AS a research agent (`claude --agent <research-agent>`) running its whole plan itself — the executor is still a positioned specialist. Stamping `solo` onto individual gates mid-plan, so the orchestrator runs them inline during a `/rclab-coordinate` effort, routes physics to the one agent not positioned to do it — the corruption this skill must not reintroduce.

Write `PARTITION_FILE` with a **gate_type column** (`compute` | `review` | `workshop`) per item (the manifest `/rclab-coordinate` reads to branch dispatch). Mixed-type waves are normal and expected.

### 1c-REGISTERS-delta — REGISTER in the index (forward-register maintenance is SKIPPED)

Investigation mode does NOT close a session, so the session-mode forward-register maintenance (EVOI / atlas-08 / atlas-04 / open-channel-ledger) is **SKIPPED entirely**. In its place, the index-registration step fires: append (or update) the `investigation-{n}` row in `sessions/investigation/index.md` per that file's schema — **topic** (from the seed; never invented), **driver/seed** (the `--from` source + what investigation/synthesis produced it), **plan** path, status `PLANNED`. Append-only; do not reorder or delete rows. This is the "plan touches the index" half of the maintained-by contract; `/rclab-investigate --investigation n` housekeeps the other half (status → outputs → drives). The index is a DATA register, not a rule file (Safety rule 4 carries over).

### Phase-2-delta — mixed-type gate blocks

Per-wave planners read `.claude/templates/plan-investigation.md` (instead of `plan-compute.md`) AND the `gate_type` field of `.claude/templates/r3-yaml-gate-block.yaml`. Each gate sets `gate_type` and fills the type-appropriate fields:
- **compute** → all 8 PRDR items + verdict rubric + output_artifacts WITH `verdict_line` (pinned to `computations/investigation-{n}/inv{n}_gate_verdicts.txt`, NEVER a `session-{N}` path).
- **review** → the `review:` block (agents / sources / output_paths / context); PRDR numerics N/A; output_artifacts = one synthesis md per agent, NO verdict_line.
- **workshop** → the `workshop:` block (EXACTLY 2 agents / rounds / sources / output_path / adjudication_question / context); PRDR numerics N/A; output_artifacts = the workshop md, NO verdict_line.

Per-wave planner prompt: same as session mode (Phase 2) but swap the "Read first" item 1 to `plan-investigation.md`, add `r3-yaml-gate-block.yaml §gate_type`, and instruct the planner to set `gate_type` per its assigned `PARTITION_FILE` rows. Owner-agent / stall-handling / close-grep all unchanged.

### Phase-3-delta — validate compute gates only

`_plan_upstream_pin_validator.py` + `_yaml_gate_validator.py` run on the **compute gates only** (they alone have npz pins + numeric PRDR). For **review/workshop** gates, validation is artifact-existence-readiness: confirm the `review:`/`workshop:` block is complete (agents present; workshop has EXACTLY 2; sources + output paths set) and output_artifacts lists the deliverable md with `must_contain`. A review/workshop gate is NOT pin-validated and is NOT PRU-vulnerable for lacking a numeric threshold (per `r3-yaml-gate-block.yaml` footer + `wave-classification.md §M1`). The 3b user checkpoint + 3c consolidate are unchanged.

### Phase-4-delta — mixed-type WP sections

WP prompters write per-wave WP shells under `INV_DIR`. compute gate sections use the normal `*(pending …)*` blocks + verdict-line closure checklist. review/workshop gate sections instead carry a pending block pointing at the deliverable md + an **artifact-existence** checklist (file exists + `must_contain` matches), NOT a verdict-line block (there is no verdict line for these types).

### Phase-5-delta — report + next step

Report per Phase 5 with the investigation paths. Next step: `/rclab-coordinate sessions/investigation/investigation-{n}/investigation-{n}-plan-index.md` (it juggles the three gate types directly).

---

## Phase 0 — Parse & validate

1. Parse arguments per the table above.
2. Resolve `--planner` and `--prompter` against `.claude/agents/` files (see `.claude/templates/agent-roster.md`). Invalid → list available types and stop.
3. Verify each `--context <file>` exists (Read 1 line). Missing → report and stop.
4. `--consolidate` and `--fanout` cannot both be set; if both passed, stop with error.
5. **Mode select**: if `--investigation` is present → INVESTIGATION mode (jump to §"Investigation Mode" for the Phase-1 deltas; Phases 2–5 run as written with the investigation paths). `--investigation` and `--session` are mutually exclusive → stop with error if both passed. In investigation mode, `--from` is REQUIRED — verify each `--from` glob/dir/file resolves to ≥1 existing file (Read 1 line of one); missing → report and stop. Absent `--investigation` → SESSION mode (everything below, unchanged).

## Phase 1 — Detect session, gather carry-forwards, partition by wave

### 1a. Session ID + output paths

If `--session` not provided: glob `sessions/session-plan/session-*-plan*.md`, pick highest N, new session = N+1.

```
PRIOR              = N - 1
CONTEXT_FILE       = sessions/session-plan/session-{N}-context.md
PARTITION_FILE     = sessions/session-plan/session-{N}-partition.md
PLAN_FILE          = sessions/session-plan/session-{N}-plan.md          (consolidate)
PLAN_INDEX         = sessions/session-plan/session-{N}-plan-index.md    (fanout)
WAVE_PLAN_FILE(i)  = sessions/session-plan/session-{N}-plan-w{i}.md
WORKING_PAPER      = sessions/session-{N}/session-{N}-results-workingpaper.md   (consolidate)
WAVE_WP_FILE(i)    = sessions/session-{N}/session-{N}-w{i}-workingpaper.md      (fanout)
```

If `PLAN_FILE` or `PLAN_INDEX` exists, `AskUserQuestion` overwrite / next number / cancel.

### 1b. Gather carry-forwards (mechanical)

The canonical source for carry-forwards is the prior session's per-wave WP §"Carry-Forward Computations" sections per `.claude/templates/workingpaper.md` Rule 4 + `feedback_fix-in-session-never-defer.md`.

Sources, in preference order:

```
sessions/session-{PRIOR}/session-{PRIOR}-w*-workingpaper.md      # per-wave WPs (preferred per S87 W1b)
sessions/session-{PRIOR}/session-{PRIOR}-results-workingpaper.md # unified WP fallback
sessions/session-{PRIOR}/workshops/*.md                          # workshop wrap-ups (carry-forwards in §Wrap-Up)
```

From each source, extract the **carry-forward block only** — not the gate verdicts or synthesis prose:

- WP file: `## Carry-Forward Computations` top-level section per `workingpaper.md` Rule 4.
- Workshop wrap-up: `## Wrap-Up` → `### Carry-Forward Computations` numbered list.

Each carry-forward is a **4-field spec** (What / Inputs / Gate / Effort) per `feedback_fix-in-session-never-defer.md`. Items missing any field are bookkeeping, not future work — flag them and skip per `feedback_fix-in-session-never-defer.md`. **No grep-fallback** on unstructured prose.

Deduplicate by computation title (case-insensitive) or explicit gate-ID match. Record per item: 4 fields, source-file list (convergence count), reviewer origin (which agent's synthesis surfaced it).

Write `CONTEXT_FILE` with the deduplicated table + source manifest + extra `--context` files folded verbatim. The context file contains ONLY this — **no** MEMORY.md dump, **no** prior verdict snapshot, **no** knowledge-index extract. Planners query MCP directly per `.claude/rules/knowledge-index-usage.md`.

### 1c. Partition into waves (mechanical bucketing)

Group items by natural theme. Default wave-owner subagent_type is the reviewer-origin of the items:

- A wave dominated by items from one reviewer's synthesis → that reviewer owns it (transit-dynamics-theorist owns transit waves, lizzi-spectral-functional-theorist owns spectral-functional waves, mack-cosmic-bridge owns observational waves, etc.).
- A cross-reviewer wave (primary live gates, audit integrity, methodology closure) → `gen-physicist` (breadth owner).
- Target 6–15 items per wave per `feedback_session-process.md`. Waves >15 items are pre-split into sub-waves (`W2a`, `W2b`, ...) along reviewer-origin or theme boundaries BEFORE dispatch, not after a stall.
- Respect `feedback_dispatch-discipline.md`: ≤8 concurrent dispatches per batch; sub-wave splits count separately.

Semantic-duplicate merge: items with slashed gate IDs (e.g., `S84-VII-M-LANDING / S84-THREE-LAYER-REG-LANDING`) are dual-ID single gates; merge them.

Write `PARTITION_FILE` per `.claude/templates/plan-compute.md`. One section per wave: theme, owner agent, item list with one-line scope each, natural split candidates (in case the wave stalls).

> **Item set**: the 1b carry-forwards are the SEED. `1c-REGISTERS.CONSUME` (below) adds register-sourced candidates (live atlas-08 / ledger channels with no WP carry-forward) and finalizes the EVOI-tiered order — re-bucket any added items into the right wave before writing the final `PARTITION_FILE`.

### 1c-REGISTERS. Maintain & consume the forward registers (MANDATORY — two step-processes)

The framework's forward direction lives in a small set of **curated registers**, not in the WP carry-forwards alone. These registers rot silently whenever no skill consumes them — the EVOI guiding star content-froze for ~13 sessions because nothing read it (S96 rebuild §0; "an unenforced rule rots silently"). This step closes that gap for the whole set by making `/rclab-plan` the single place that BOTH **maintains** the registers from the just-mined session AND **consumes** them as a planning source. Plan-time IS the de-facto session wrap-up (the framework has no separate wrap-up command); register maintenance rides on the Phase-1 session mining already done in 1b.

**The forward-register set:**

| Register | Holds | Maintained here | Consumed here | Owner / routing |
|:--|:--|:--|:--|:--|
| `sessions/evoi-framework.md` | compute-priority tiers + §6 actionable queue | yes (currency audit + rebuild) | yes (§6 = Wave-1 list; §1–§4 tiers order waves) | orchestrator |
| `sessions/framework/Atlas/atlas-08-open-questions.md` | open-question ledger (Decisive/Structural/Observational/Methodology) | yes (S{PRIOR} freshness updates) | yes (still-OPEN questions = candidates) | orchestrator; observational-VALUE rows → mack |
| `sessions/framework/registry/open-channel-ledger.md` | curated live channels (§A–§D) | yes (refresh + mark closed) | yes (§A–§D = candidates) | orchestrator |
| `sessions/framework/Atlas/atlas-04-assumptions.md` | assumption status (PROVEN/CONDITIONAL/BROKEN) | yes (status down-tags only) | yes (BROKEN/CONDITIONAL w/ tractable gate = candidate) | orchestrator; §IX snapshot → mack |
| `sessions/framework/registry/falsifier-master-inventory.md` + `falsifier-watchlist.md` | observational falsifier rows | route to **mack** (sole writer) | yes (detector-bound watch) | **mack-cosmic-bridge only** |

#### Step-process 1 — MAINTAIN: update the registers from the mined session

Reconcile the just-closed S{PRIOR} into each register. Every update MUST be **traceable** to S{PRIOR}'s `computations/session-{PRIOR}/s{PRIOR}_gate_verdicts.txt` + `sessions/session-{PRIOR}/session-{PRIOR}-housekeeping.md` + WP closures — **no invented closures** (an orchestrator once wasted a session fabricating an open-channel audit; traceability closes that failure mode).

1. **EVOI** — run the currency audit; if it lags, REBUILD before ordering (do NOT re-note-and-defer — that loop is what froze it for ~13 sessions):
   ```bash
   phonon-exflation-sim/.venv312/Scripts/python.exe computations/_shared/_evoi_staleness_audit.py --current-session {N}
   ```
   S2/S1 → fold S{PRIOR} closures into §5; refresh §1–§4 + §6 from the gathered carry-forwards + `atlas-08-open-questions.md` §0 EVOI tiers; bump `<!-- evoi-content-currency: S{N} -->`; re-run to PASS.
2. **atlas-08-open-questions** — for each S{PRIOR} verdict/closure that resolves or advances a listed question, **append** an `S{PRIOR} freshness update` bullet (bullet-format Q's) or inline `**S{PRIOR}: …**` tag (table-format Q's), citing the verdict + atlas-04 entry. PRESERVE the verbatim original (atlas-08 §V convention: "originals preserved; closures recorded as updates"). Re-stamp the header banner. Write the backing audit to `sessions/framework/registry/atlas-08-freshness-S{PRIOR}.md` (pattern: the S97 freshness pass).
3. **atlas-04-assumptions** — down-tag any assumption whose status S{PRIOR} changed (status cell only). Per `.claude/rules/capstone-hygiene-gate.md`: run the 5-question gate; a status down-tag NEVER inverts the explanation direction (substrate-first framing preserved per `phononic-framing.md`); the prose tag MUST equal the register status.
4. **open-channel-ledger** — refresh §A–§D live channels; mark any S{PRIOR}-closed channel.
5. **Routing (do NOT direct-edit):** observational prediction VALUES (atlas-04 §IX, capstone §7, `falsifier-master-inventory.md`, `falsifier-watchlist.md`) are `mack-cosmic-bridge`'s sole-writer surface (`feedback_mack-bridge-role.md`) — emit a mack dispatch for those rows; propagate already-canonical values into non-mack copies WITH citation only. A genuinely-unreconciled math/physics tension routes to a workshop/CF per `Investigating-Workshops.md`, NOT a fabricated status edit.

#### Step-process 2 — CONSUME: use the registers as a planning source

With the registers now current, the planning corpus is **WP carry-forwards (1b) ∪ register-sourced candidates** — not WP carry-forwards alone. The WP-only blind spot: a live channel can sit in atlas-08 / the ledger with NO WP carry-forward surfacing it (no session happened to route it), so a WP-only planner never plans it.

1. **Gather register candidates:** EVOI §6 (authoritative Wave-1 list) + §1–§4 tiers; atlas-08 still-OPEN Decisive/Structural/Observational questions; open-channel-ledger §A–§D; atlas-04 BROKEN/CONDITIONAL entries that have a tractable pre-registrable gate.
2. **Dedupe vs WP carry-forwards (1b):** a register item already covered by a 1b carry-forward → merge (record convergence). A register item with NO 1b carry-forward → genuine candidate the WPs missed → add it to the corpus, tagged `register-sourced`.
3. **Order by EVOI tier** (§6 authoritative for Wave-1). EVOI values are **ordinal leverage proxies, not probabilities** — ordering only.
4. **Fold** the register-sourced candidates into the 1c partition (re-bucket by theme/owner). A high-leverage register candidate with NO tractable gate (e.g. K_pivot / atlas-04 C2) is recorded as a **standing gap**, not a wave gate — leverage ≠ tractability.

### 1d. Dry-run exit

If `--dry-run`, report source manifest, deduplicated entry count, wave count, partition table — and stop.

---

## Phase 2 — Spawn per-wave planner swarm

Each per-wave planner writes ONE wave file. Dispatch in parallel batches of ≤8 per `feedback_dispatch-discipline.md`. Track via TaskCreate/TaskUpdate. Background, `mode="acceptEdits"`, `name="planner-w{i}"`. (The Agent tool has no `effort` param — depth is inherited from the orchestrator's model/effort; do not pass `model` either, so each planner inherits the running model rather than resolving a different Opus point-release.)

### Why a swarm

A single planner trying to hold ~100 carry-forward items in working memory while writing 3000+ lines of structured gate blocks hits the stream watchdog (S84 calibration: two gen-physicist planners stalled at 600s with zero writes). Per-wave planners holding 6–15 items each consistently succeed. Stalled per-wave agents get split further into sub-waves with the SAME full-fidelity spec, NOT abbreviated.

### Per-wave planner prompt

```
You are writing **Wave {i} only** of the Session {N} compute plan.

## Read first (mandatory before writing any gate block)

1. `.claude/templates/plan-compute.md` — the per-wave plan file shape you must produce.
2. `.claude/templates/r3-yaml-gate-block.yaml` — the gate-block schema. Every gate block conforms to this YAML or the markdown equivalent at `.claude/templates/pru-pre-registration-template.md`. `computations/_shared/_yaml_gate_validator.py` runs against this schema.
3. `.claude/rules/epistemic-discipline.md` §"Pre-Registration Completeness" — PRU Class 8 + PRDR + Source-Reconciliation. The audit pipeline composition order is `PRU → SOURCE-RECON → SUBSTRATE-FIRST-PROVENANCE → PRDR → gate execution`.
4. `.claude/rules/gate-verdicts.md` — verdict-line schema; canonical verdict-file path (`computations/session-{N}/s{N}_gate_verdicts.txt` — all other variants forbidden); use `verdict_source: computations/session-{N}/s{N}_gate_verdicts.txt` in gate blocks, NEVER `expected_verdicts: [...]` arrays.
5. `.claude/rules/math-scripts.md` — substitution chain MANDATORY for sign/direction/threshold claims (no "obviously from structure"); `from canonical_constants import *`; GPU/CPU dispatch rules; D_K block-diagonality pre-check for L_max ≥ 10.
6. `.claude/rules/substrate-first-canonical-sourcing.md` — every NUMERICAL pin sources from substrate-first computation, not external-paper placeholder. SCHEMATIC vs FULL physical level pin (§(iv) K=4 MANDATORY): if a gate consumes `_spectral_action_regulators.py` or similar SCHEMATIC helper, declare CLASS=SCHEMATIC + add `-SCHEMATIC` suffix to convention + emit `tier_pin=TIER-2` companion row.
7. `.claude/rules/regulator-pin-discipline.md` — every NEW Seeley-DeWitt citation uses `a_n^{regulator}` tagging.
8. `.claude/rules/wave-classification.md` + `.claude/rules/methodology-wave-allowlist.md` — if any gate is METHODOLOGY-class, it must satisfy M1–M4 strict conjunction AND its gate-ID must appear in the allowlist. If not yet listed, flag it for orchestrator allowlist append at plan-freeze.
9. `.claude/rules/cross-pillar-bridge-anatomy.md` — if any gate registers or refines a cross-pillar bridge §VII entry, declare ALL 5 anatomy elements (substrate-IS / laboratory-IN / bridge map / algebraic envelope / empirical anchor) + 3 levels (cohomology / envelope / anchor).
10. `.claude/rules/output-standards.md` — action-item 7-field format; numerical-vs-structural separation in any "what changed" block.

## Your task

Write Wave {i} to `sessions/session-plan/session-{N}-plan-w{i}.md`, matching the per-wave shape in `.claude/templates/plan-compute.md`.

**Wave {i} theme**: {theme from partition manifest}
**Owner**: {owner subagent_type from partition manifest}

**Your assigned items** ({count}):

| # | Gate ID | Scope |
|:--|:--------|:------|
{rows copy-pasted from CONTEXT_FILE for this wave's items}

## Inputs you may read

- `sessions/session-plan/session-{N}-context.md` — your authoritative scope.
- The rules and templates enumerated above.
- Knowledge MCP (`mcp__knowledge__*`) for prior verdicts / closures / constants. Query first, compute second per CLAUDE.md.

Do NOT read `session-{N-1}-plan.md` or individual S{N-1} synthesis files — too large; watchdog-stall risk. The context file is self-sufficient.

## Per-gate block: fill every R3 YAML field

For each assigned item, write one gate block per `.claude/templates/r3-yaml-gate-block.yaml`. All 8 PRDR checklist items required and non-empty: `operator`, `strict_PASS_boundary`, `boundary_reachable_analytically`, `reachable_rationals`, `machinery_pin_map`, `audit_discriminators`, `substitution_chain`, `input_files`. Plus identity (gate_id, schema_version="R3", trigger, classification, agent_type, hypothesis), verdict rubric (PASS/FAIL/INFO meanings), effort, substrate framing.

In `agent_type`: pick a domain specialist from `.claude/templates/agent-roster.md` matched to the gate's substrate physics. Gen-physicist is the planner default, not necessarily the gate executor — pick whoever owns the substrate.

For sign / direction / threshold claims in any gate's hypothesis or PASS condition: substitution chain MANDATORY per `math-scripts.md §"Double-Check Logic"`. No shortcuts.

## Constraints

- Write ONLY `session-{N}-plan-w{i}.md`. No other file.
- Do NOT execute computations.
- Do NOT re-list items from other waves.
- Do NOT collide with existing gate IDs (consult `computations/session-{N-1}/s{N-1}_gate_verdicts.txt` for the S{N-1} gate-ID space).
- Full-fidelity gate blocks per `feedback_max-effort-full-fidelity.md`. No abbreviation, even in late waves.
- Do not terminate until the file exists with non-stub content for every assigned gate.
```

### Stall handling

If a per-wave planner reports `killed` or `stalled` without writing:

1. **Do NOT re-dispatch with a leaner spec.** A stall is an infrastructure event, not a signal to degrade pre-registration. (S84 calibration: "stalled agents don't mean do it again, but shittier.")
2. **Split** the wave into sub-waves along the partition manifest's "natural split candidates" (typically reviewer-origin boundaries).
3. **Re-dispatch** each sub-wave with the SAME full-fidelity prompt — narrower item list, per-sub-wave owner agent, identical rigor.

### Phase 2 close

For each wave file:
1. Verify `session-{N}-plan-w{i}.md` exists.
2. Grep for each expected gate ID. Missing → re-dispatch that sub-wave only with a targeted gate list.

---

## Phase 3 — Validate upstream pins, user checkpoint, optional consolidate

### 3a. Per-wave upstream-pin validation (MANDATORY)

For each wave plan file, run:

```bash
"phonon-exflation-sim/.venv312/Scripts/python.exe" \
  computations/_shared/_plan_upstream_pin_validator.py --json \
  "sessions/session-plan/session-{N}-plan-w{i}.md" \
  > "sessions/session-plan/session-{N}-plan-w{i}-validation.json"
```

Exit code:

- **0 (PASS)** — every cited upstream `.npz` exists on disk AND machinery pins agree with npz payload keys under alias normalization. Proceed.
- **1 (HARD FAIL)** — cited upstream `.npz` missing OR machinery pin disagrees with npz payload (pin drift). Per `.claude/rules/epistemic-discipline.md §"Source Reconciliation"` Class-(c): either (a) edit the wave plan to correct slugs/pins and re-run, or (b) explicitly document why runtime canonical-path rescue per `.claude/rules/gate-verdicts.md` is acceptable — annotate the rationale inline next to the affected pin and record the wave as ACCEPTED-RESCUE in the 3b checkpoint. (Interface note, corrected 2026-06-07: the script has NO `--strict=false` form — `--strict` is an opt-in extra-severity flag, and missing-npz drives exit 1 even in default mode. The common benign case is a FORWARD-PINNED INTRA-SESSION input — gate B consumes gate A's npz produced earlier in the same session; signature = `n_mismatches: 0` with `n_missing_npz ≥ 1` on `s{N}_*`-slugged paths; disposition (b) applies.)
- **2 (PARSE-ERROR)** — file structurally malformed; treat as a planner-stall equivalent — split the wave and re-dispatch per Phase 2 stall handling.

The validator runs mechanically; no agent compliance required. Prompt-based "please cross-check your pins" reverts to planner-agent compliance and is therefore insufficient (S85 W9 calibration: 7 plan-authoring documentation bugs across two gates — slug mismatches, `L_max` and `n_tau` pin drift, wrong registry path).

Orthogonal to this: `_yaml_gate_validator.py` checks PRDR machinery-enumeration checklist completeness. Both should run per wave before Phase 3b.

### 3b. User checkpoint

Report per `.claude/rules/output-standards.md`:

```
=== WAVE PLANS GENERATED ===
Session: {N}
Partition: {PARTITION_FILE}
Wave files:
  {WAVE_PLAN_FILE i}    {lines} lines, {gate_count} gates    [3a: PASS | FAIL | PARSE]
Total gates: {count}
Validation: {N_pass} PASS, {N_fail} FAIL, {N_parse} PARSE
{verbatim FAIL list, referencing each *-validation.json}
Mode: {consolidate | fanout}
```

`AskUserQuestion`. "Continue" is offered only if all 3a verdicts PASS; if any FAIL, replace "Continue" with "Accept runtime canonical-path rescue with documented rationale" per `gate-verdicts.md`:

- **Continue** → Phase 3c (consolidate) or Phase 4 (fanout WPs).
- **Re-spawn a specific wave** → user names a wave; re-dispatch with feedback (typical for 3a FAIL caused by planner pin drift).
- **Accept runtime canonical-path rescue** (3a FAIL path) → orchestrator appends an inline comment to each affected plan pin documenting the rescue rationale.
- **Edit wave files manually** → user edits; re-run `/rclab-plan` afterward (Phase 3a re-runs automatically).
- **Stop here** → wave plans stand on their own.

### 3c. Optional consolidate (`--consolidate` only)

Mechanically stitch wave files into `PLAN_FILE` per the consolidated shape in `.claude/templates/plan-compute.md`:

- §I Session Objective (one paragraph synthesizing the partition manifest's themes)
- §0.10 PRU Pre-Registration (aggregate of per-wave `machinery_pin_map` entries)
- §II Wave Structure (dependency graph)
- §III Wave M (verbatim body of each `session-{N}-plan-w{i}.md` under its wave heading)
- §IV Constraint Gates Summary (aggregated)
- §V Decision Points (aggregated from per-wave `→ Wave {i+1}` blocks)
- §VI Execution Notes

Per-wave plan files may be kept as appendices or deleted (user choice; default keep for fanout, delete for consolidate cleanliness).

`--fanout` skips this; write thin `PLAN_INDEX` per the index shape in `plan-compute.md` (one row per wave: theme, owner, gate count, plan file).

---

## Phase 4 — Spawn working-paper prompters

Spawn prompters per `feedback_dispatch-discipline.md`:

- **Consolidate mode**: 1 prompter writes `WORKING_PAPER` covering all waves.
- **Fanout mode**: N prompters in parallel (batched to the cap), one per wave, each writes `WAVE_WP_FILE(i)`. Orchestrator also writes thin `sessions/session-{N}/session-{N}-results-index.md` listing per-wave WPs.

### Prompter prompt

```
You are generating a results working-paper shell from an approved session plan.

## Read first

1. `.claude/templates/workingpaper.md` — authoritative shell shape (per-gate pending blocks, footer sections, MCP Pre-Compute Audit block, anti-pattern warnings).
2. `.claude/templates/examples/workingpaper-shell-example.md` — CANONICAL frozen example. Match it exactly. ~15 lines per gate; 10-gate wave → ~150-line file.

## Your task

{Consolidate}: Read plan at `{PLAN_FILE}`. Write `{WORKING_PAPER}`.
{Fanout}: Read `session-{N}-plan-w{i}.md`. Write `session-{N}/session-{N}-w{i}-workingpaper.md`.

## Constraints

- One pending block per gate, of the form `*(pending — include: ...)*`. The include-list names plan deliverables (4-tuple, CCs from gate block, substitution chain, dual-SHA, artifacts) — it's a contract for the runtime agent, not a stub.
- **Zero** `<!-- Runtime agent fills: ... -->` stub comments — banned per `workingpaper.md §"Anti-pattern"`.
- Hypothesis = one-line paraphrase from the plan, not a verbatim copy.
- Every gate's pending blocks include the `**MCP Pre-Compute Audit**` placeholder per `workingpaper.md` Rule 3 + `.claude/rules/knowledge-index-usage.md`.
- Footer: `## Wave {W} Synthesis (team-lead)`, `## Carry-Forward Computations`, `## Constraint-Map Updates`, `## Files Produced` per `workingpaper.md`.
- Write ONLY the working-paper file. Do NOT modify the plan.
- No length targets. Shells substantially longer than ~15 lines/gate are plan-echo bloat per `feedback_max-effort-full-fidelity.md`.
```

### Phase 4 close

For each working paper: verify it exists, has the expected number of gate sections (one per `W{i}-{L}` in its plan), and is not stub-shaped. Missing sections → re-spawn prompter for that subset.

---

## Phase 5 — Report

```
=== /rclab-plan COMPLETE ({consolidate | fanout}) ===
Session: {N}
Generated files:
  {CONTEXT_FILE}              {lines}
  {PARTITION_FILE}            {lines}
  {PLAN_FILE | PLAN_INDEX}    {lines}
  per-wave plans:  session-{N}-plan-w{i}.md         {lines each}
  working papers:  {WORKING_PAPER | session-{N}-w{i}-workingpaper.md}    {lines each}
Total waves: {W}    Total gates: {count}
Validation: all PASS  (or: {N_fail} FAIL with documented rescue)
Next step: /rclab-coordinate {plan-or-index path}
```

---

## Safety rules

1. Never overwrite existing files without user confirmation (Phase 1a collision check).
2. Never spawn teams — solo agents only. No TeamCreate, no SendMessage.
3. Never execute computations — plan-time skill only.
4. Never modify MEMORY.md, agent memory, the knowledge index, or rule files. (Phase **1c-REGISTERS.MAINTAIN** DOES edit the forward registers — EVOI / atlas-08 / atlas-04 / open-channel-ledger — as reviewed status/freshness patches per capstone-hygiene + framework-hygiene; these are *registers*, NOT rule files. mack's observational surface — atlas-04 §IX, `falsifier-master-inventory.md`, `falsifier-watchlist.md`, capstone §7 — is ROUTED to mack, never direct-edited.) **In investigation mode**, the **1c-REGISTERS-delta** registers the new `investigation-{n}` row in `sessions/investigation/index.md` (a DATA register, append-only) and SKIPS the forward-register maintenance entirely (an investigation does not close a session).
5. Gate IDs in generated plans must NOT collide with existing session IDs.
6. Phase 1 gathering/partition (1b/1c) is mechanical only — no interpretive content in the context file or partition manifest. **1c-REGISTERS** is the one disciplined-reconciliation step: every update is traceable to S{PRIOR}'s verdict file + housekeeping (no invented closures), append-only over verbatim originals, and routes adjudication-requiring items to workshops/CFs.
7. No grep fallback in carry-forward gathering. Items lacking a 4-field spec are not carry-forwards per `feedback_fix-in-session-never-defer.md` + `feedback_fix-in-session-never-defer.md`.
8. Stalls do not justify degrading the per-wave spec. Split the wave; keep the rigor (`feedback_max-effort-full-fidelity.md`).
9. Planners must not read `session-{N-1}-plan.md`. The context file is self-sufficient.
10. Concurrency: ≤8 concurrent agents per `feedback_dispatch-discipline.md`.

## Error handling

| Condition | Action |
|:----------|:-------|
| Empty topic | Auto-default per Phase 0 — never stop. |
| Agent type not found | List available, stop. |
| `--context` file missing | Report which, stop. |
| Both `--consolidate` and `--fanout` set | Stop with error. |
| Both `--session` and `--investigation` set | Stop with error (mutually exclusive modes). |
| `--investigation` without `--from` | Stop with error — the seed IS the scope; investigation mode cannot proceed without it. |
| `--from` glob/dir resolves to zero files | Report the glob, stop. |
| Investigation number collision (`investigation-{n}` plan exists) | AskUserQuestion overwrite / next / cancel. |
| Session ID collision | AskUserQuestion overwrite / next / cancel. |
| Prior session folder missing | Fall back to latest existing; AskUserQuestion if ambiguous. |
| Source WP lacks `## Carry-Forward Computations` | Report which file, skip; no grep fallback. |
| Partition ambiguous (item fits 2+ themes) | Assign to wave with stronger reviewer-origin signal; flag in manifest. |
| Planner stall (>600s no write) | Split wave per Phase 2 stall handling. |
| Wave file missing gates | Re-dispatch that sub-wave only with a targeted gate list. |
| Validator HARD FAIL | User checkpoint per 3b. |
| Validator PARSE-ERROR | Treat as stall; split + re-dispatch. |
| Consolidation collides (duplicate gate IDs across wave files) | Stop; report collision; user renames gates. |
| Prompter stall | One retry; if still stalled, split prompter by gate count (one prompter per 3–5 gates). |
| Working-paper sections missing | Re-spawn prompter for the missing subset. |

---

## Notes

- **`--fanout` is default** (S87 W1b). Per-wave files prevent the runtime-append-at-bottom failure mode of unified WPs.
- **Planner ≠ gate executor.** `--planner gen-physicist` writes the plan; each gate block's `agent_type` field names the agent that EXECUTES that gate at `/rclab-coordinate` time. Pick gate executors per-gate from `.claude/templates/agent-roster.md` by substrate match.
- **Per-wave planner = reviewer-origin owner.** When the partition manifest assigns a domain specialist (transit-dynamics-theorist, lizzi-spectral-functional-theorist, etc.) as wave owner, that specialist is the planner for the wave; `--planner` only sets the cross-reviewer fallback. Specialists consistently produce denser plans than gen-physicist on their own substrate.
- **`/rclab-plan` does NOT read the workshop schedule.** Per `Investigating-Workshops.md §"Cross-references"`, the schedule and the carry-forward queue are separate input streams. Schedule outcomes feed back into the source session's WP carry-forwards; THAT is what this skill reads. A compute item routed only to the schedule is invisible here.
