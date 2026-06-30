# Session Housekeeping Template

Per-session Q2-class ledger. Filled in DURING the session's wave-compute (at wave-synthesis time), BEFORE `/rclab-investigate` runs.

Authoritative scope source: `.claude/rules/Investigating-Workshops.md §"Q2 — Is the candidate registry-state classification, hygiene, gate finalization, or framework-issue?"`. This template is the CANONICAL Q2 ledger for a session; WP `## Carry-Forward Computations` blocks for §B/§C/§D items are MIRRORS.

## Purpose

Q2 items are bookkeeping, not adversarial physics. Catching them at wave-compute (not at `/rclab-investigate` time) closes two failure modes:

1. **Workshop bloat** — Q2 items dressed as workshops waste dispatch cycles (calibration: S87 batch-1 + S88 W13 W-2/W-4 in the rule's failure corpus).
2. **CF-block invisibility** — items that exist only in the workshop schedule are invisible to `/rclab-plan` (which reads WP CF blocks, not schedules).

Closing both: identify Q2 items at wave-close; record FIXES in §A (effected in-session); record genuine-future-compute items in §B/§C/§D with 4-field specs that mirror to WP CF blocks; escalate pre-compute shell waves in §E.

## When the file is written

- **At wave-close** — the team-lead synthesis writer (per `/rclab-coordinate` Step 6) scans the closed wave for Q2 items and appends entries. This is part of the auto-proceed wave-synthesis procedure (`feedback_no-asking-just-execute.md`) — no separate user authorization required.
- **At session-end** — during the closing-session synthesis pass, fold any straggler Q2 items into the appropriate section.
- **Before `/rclab-investigate` dispatches** — the file is the upstream filter so investigators skip these candidates by construction.

## §A vs §B-D distinction (load-bearing)

**§A is the record of what was already effected IN-SESSION.** Per `feedback_fix-in-session-never-defer.md`, hygiene observations on already-correct artifacts are NOT carry-forwards; status-tag edits, mechanical promotions, audit-script regex extensions, and other orchestrator-direct edits MUST happen in the same session that surfaced them. §A is the audit trail of those fixes, not a queue.

**§B/§C/§D are genuinely future-compute items.** An item belongs in §B-D iff its resolution requires substrate-physics compute that an orchestrator-direct edit cannot perform: a Stage-2 cross-axis independent-verify (per `joint-theorem-promotion.md §"Stage 2"`); a wave-together promotion compute whose verdict depends on a numerical re-run; a parallel-compute-wave with per-axis pre-registered thresholds; a methodology rule extension whose plan-freeze requires the M1-M4 conjunction validator. If an item can be effected by an Edit/Write on a rule/template/registry/canonical-constants file with no compute, it belongs in §A, NOT §B-D.

## Canonical instance path

`sessions/session-{N}/session-{N}-housekeeping.md`

## Schema

```markdown
# Session {N} Housekeeping Ledger

**Date**: {today}
**Session**: {N}
**Authoritative scope**: `.claude/rules/Investigating-Workshops.md §"Q2"`

## Q2 marker (citation)

A candidate is Q2 iff its resolution is a status-tag edit / mechanical promotion / rule-file diff / audit-script extension / mechanical re-run, rather than a derivation that produces a new structural claim. See the rule §"Q2" for the full marker list (status-tag edit, mechanical promotion, provenance hygiene, methodology-rule extension, audit-script extension, registry-write hygiene, gate-finalization gap, pre-compute shell escalation).

---

## §A. In-session resolutions (already effected; ledger only)

Per `feedback_fix-in-session-never-defer.md`: items in this section were FIXED during S{N} wave compute. Each row cites the surfacing wave/gate, the resolution edit (file:lines), and the gate's verdict-line audit_sha256 short.

| # | Source wave / gate | Item | Resolution (file:lines) | Verified at (audit_sha256 short) |
|:--|:-------------------|:-----|:------------------------|:---------------------------------|
| A1 | W{w}-§{g} | {one-line description} | `path/to/file.md:LL-LL` OR `path/to/script.py:LL-LL` | `{short16}` |
| A2 | ... | ... | ... | ... |

If no in-session resolutions: write `(none — no Q2 items fixed in-session this session)`.

---

## §B. Hygiene-promotion compute carry-forwards (4-field spec; mirrored to WP CF)

Q2 items requiring mechanical compute next session: promotion via the `joint-theorem-promotion.md` 4-stage pathway (Stage-2 cross-axis independent-verify cannot be effected by an orchestrator edit); canonical_constants.py promotions whose value comes from a re-run; registry-row landings whose anchor binding depends on a compute output.

Each entry MUST be MIRRORED to the originating wave's WP `## Carry-Forward Computations` section so `/rclab-plan` consumes it via its existing contract.

### CF-S{N+1}-HK-{n} — {one-line title} [Q2-hygiene]

> **Routing note**: Q2-class per `Investigating-Workshops.md §"Q2"`. Identified at S{N} W{w} wave-synthesis. NOT a workshop. Mirrored to `sessions/session-{N}/session-{N}-w{w}-workingpaper.md §"Carry-Forward Computations"`.

> **Why not §A (fix-in-session)**: {one sentence — names the substrate-physics compute step that prevents orchestrator-direct edit. Examples: "Stage-2 cross-axis verify requires connes+volovik independent dispatch per `joint-theorem-promotion.md §"Stage 2"`"; "registry-row anchor binds to a compute output that doesn't exist yet"; "the canonical value is a refinement of a SCHEMATIC predecessor and requires FULL physical re-run per `substrate-first-canonical-sourcing.md §(iv)`".}

1. **What**: {specific deliverable — status promotion target, dict entry, mechanical re-run with substrate-physics output}
2. **Inputs**: {file paths + canonical references + upstream gate audit_sha256 if applicable}
3. **Gate**: `S{N+1}-{GATE-ID}` with PASS criterion = {artifact-existence predicate per `wave-classification.md §M1` if METHODOLOGY-class, OR specific numerical predicate if COMPUTE-class}
4. **Effort**: {wave-equivalents}

(Repeat per item. Cluster multiple §B items into a wave-together group when they dispatch in a single S{N+1} wave — see CF-W13-5 pattern: 5 sub-gates + 1 wave-rerun closeout.)

If no §B items: write `(none)`.

---

## §C. Parallel-compute-wave carry-forwards (Q3 wave-together; mirrored to WP CF)

Q3 items per `Investigating-Workshops.md §"Q3"`: N prerequisite conditions on structurally orthogonal axes + 1 wave-AND closeout. Each entry uses the 4-field spec + per-axis sub-gate enumeration. Mirrored to the originating wave's WP CF blocks marked "wave-together."

Canonical worked example: `sessions/archive/session-88/session-88-w13-workingpaper.md:1325-1343` (CF-W13-6: Path-B Step-0 4-condition wave-together).

### CF-S{N+1}-HK-{n} — {one-line title} [Q3-wave-together]

> **Routing note**: Q3-class parallel-compute-wave per `Investigating-Workshops.md §"Q3"`. NOT a workshop panel — agent-attribution per axis is a derivation-author tag, not a workshop-participant tag. Mirrored to WP CF.

> **Why not a workshop**: {one sentence — names the structural orthogonality of the N axes that rules out adversarial adjudication. Example: "the 4 prereq conditions live on 4 structurally orthogonal substrate-physics axes (BdG-superfluid / condensed-matter analog / cosmological-anchor / empirical-rigor) per `cross-pillar-bridge-anatomy.md §"5-IS-not-IN anatomy"` elements 1, 3, 4, 5 — no cross-axis rebuttal is meaningful".}

1. **What**: N-axis prereq validation; logical AND closeout for the composite verdict
2. **Inputs**: per-axis prereqs; cite 5-anatomy elements from `cross-pillar-bridge-anatomy.md` when applicable
3. **Gate**: N parallel sub-gates dispatched together:
   - `S{N+1}-{GATE-A}` — axis A; PASS criterion = {...}; derivation agent = {...}
   - `S{N+1}-{GATE-B}` — axis B; PASS criterion = {...}; derivation agent = {...}
   - ...
   - **Wave-closeout gate**: `S{N+1}-{GATE-AND-CLOSURE}` — PASS criterion = ALL N sub-gates PASS (logical AND per `joint-theorem-promotion.md §"Stage 2"`)
4. **Effort**: {wave-equivalents}

If no §C items: write `(none)`.

---

## §D. Methodology-rule extensions (M1-M4 + allowlist; mirrored to WP CF)

Q2 items resolving as rule-file diffs that survive the M1-M4 conjunction per `wave-classification.md` (artifact-existence PASS predicate; Edit/Write on `.claude/{rules,templates,skills}/**` only; verbatim sub-diff from a closed workshop/synthesis; allowlist-cited per `methodology-wave-allowlist.md §"Edit discipline"`).

Allowlist append is orchestrator-only-edit (subagents denied by harness convention). The allowlist append happens at THIS session's housekeeping write OR at S{N+1} plan-freeze — never deferred past plan-freeze.

### CF-S{N+1}-HK-{n} — {one-line title} [Q2-methodology-rule]

> **Routing note**: Q2-class methodology rule extension per `Investigating-Workshops.md §"Q2"` + `wave-classification.md §M1-M4`. Mirrored to WP CF.

> **Why not §A (fix-in-session)**: {one sentence — the rule extension content is contested between two specific agents (then it's Q1, NOT Q2 — re-route to workshop schedule), OR the rule extension requires synthesis from a closed S{N} workshop whose verbatim sub-diff is not yet extractable at wave-close (then it's §D, deferred to S{N+1}).}

1. **What**: rule-file diff at `.claude/rules/{rule-file}.md §"{section}"` — state the structural extension
2. **Inputs**: cited source workshop/synthesis (verbatim sub-diff source); pre-existing rule version SHA
3. **Gate**: `S{N+1}-{GATE-ID}` with M1∧M2∧M3∧M4 conjunction PASS per `wave-classification.md`; allowlist append per `methodology-wave-allowlist.md`
4. **Effort**: {wave-equivalents}

If no §D items: write `(none)`.

---

## §E. Pre-compute shell waves (upstream escalation; NOT a CF)

Per `Investigating-Workshops.md §"is NOT" item 9` + S91 W7 calibration. A wave is a pre-compute shell iff ALL hold: every gate `Status: NOT STARTED` in the WP AND no matching `s{N}_w{stem}_*` artifacts on disk (verify via Glob) AND no matching gate-IDs in `computations/session-{N}/s{N}_gate_verdicts.txt` (verify via grep).

These are upstream-pipeline state for `/rclab-coordinate`, NOT carry-forwards. Do NOT create `CF-S{N+1}-W{stem}-WAVE-EXECUTION` entries.

| Wave | State evidence (Glob + grep verified) | Escalation |
|:-----|:--------------------------------------|:-----------|
| W{w} | all gates `Status: NOT STARTED`; no `s{N}_w{w}_*` artifacts; no `W{w}-*` gate-IDs in verdict file | Re-dispatch `/rclab-coordinate sessions/session-plan/session-{N}-plan-w{w}.md` |

If no §E items: write `(none — no pre-compute shell waves detected in S{N})`.

---

## §F. Structural counts (artifact shape; not length)

| Category | Count |
|:---------|------:|
| §A In-session resolutions | {n} |
| §B Hygiene compute CFs (mirrored to WP) | {n} |
| §C Q3 parallel-wave CFs (mirrored to WP) | {n} |
| §D Methodology rule extensions (mirrored to WP) | {n} |
| §E Pre-compute shell waves (escalation only) | {n} |
| **Total Q2-class items surfaced** | {sum} |

(Structural-fact reporting per `feedback_max-effort-full-fidelity.md` — these are item counts, not length metrics.)

---

## Consumption pointers

- **`/rclab-investigate` (S{N})**: read this file BEFORE producing any candidates. Every §A/§B/§C/§D/§E entry is structurally a non-workshop. A new Q2 candidate that the investigator surfaces and that is NOT in this file indicates an upstream wave-synthesis miss — route the new Q2 candidate to the appropriate section here (NOT to the schedule), mirror to WP CF if it belongs in §B/§C/§D, log the miss as a one-sentence process observation in the seed file.
- **`/rclab-plan` (S{N+1})**: consume §B, §C, §D via the WP CF blocks they mirror to. §A is ledger-only — do NOT re-dispatch the fixes. §E routes to `/rclab-coordinate` retry instead of plan input.
- **`/rclab-coordinate` (S{N+1})**: dispatch §E entries as re-runs of the pre-compute shell waves before opening new waves.

---

*End of S{N} housekeeping ledger.*
```

## Mirror discipline (WP CF blocks)

For every entry in §B / §C / §D, MIRROR a corresponding CF block into the originating wave's WP `## Carry-Forward Computations` section using the same `CF-S{N+1}-HK-{n}` identifier and 4-field structure. The WP block includes a `> **Routing note**` pointer back to `session-{N}-housekeeping.md §{B|C|D}` so the two views stay synchronized.

The housekeeping file is the CANONICAL Q2 ledger (filter source for `/rclab-investigate`); the WP CF blocks are MIRRORS (load-bearing consumption source for `/rclab-plan`). Per `feedback_fix-in-session-never-defer.md`, the 4-field CF spec is non-negotiable on the WP side — a bare housekeeping entry without WP CF mirror is invisible to the next-session planner.

## Anti-patterns

- **§A used as a queue** — items written to §A that were NOT actually effected during S{N}. §A is the AUDIT TRAIL of completed fixes; it is not a TODO list. Items not yet effected go in §B/§C/§D with a 4-field spec, or get effected immediately per `feedback_fix-in-session-never-defer.md`.
- **§B-D missing the "Why not §A" routing note** — without it, future audits cannot distinguish "this genuinely requires future substrate-physics compute" from "I was too lazy to fix in-session." The routing note is the load-bearing discipline that prevents §B-D bloat.
- **§B-D entries lacking the WP CF mirror** — `/rclab-plan` reads WPs, not this file. An unmirrored §B/§C/§D entry is invisible to the next session's planner regardless of how well-specified it is here.
- **§E entries with `CF-S{N+1}-W{stem}-WAVE-EXECUTION` carry-forwards** — pre-compute shell waves escalate to `/rclab-coordinate` retry per `Investigating-Workshops.md §"is NOT" item 9`. Manufacturing a "wave-execution CF" is the S91 W7 failure mode this section closes.
- **Length targets anywhere** — `feedback_max-effort-full-fidelity.md`: no "concise summary" / "≤N lines" / "thorough explanation" language in §A descriptions, §B-D 4-field entries, §E evidence rows, or §F counts. Content requirements only.
- **Option-asking phrasing in routing notes** — `feedback_no-asking-just-execute.md` + `feedback_no-asking-just-execute.md`: routing notes use directive language ("Mirrored to ...", "Re-dispatch ...", "MUST read"). Never "Should I ...", "Which option ...", "Awaiting direction".

## Cross-references

- **Authoritative scope**: `.claude/rules/Investigating-Workshops.md §"Q2"` (this template is the operational instantiation).
- **In-session vs carry-forward split**: `feedback_fix-in-session-never-defer.md` (the §A vs §B-D discipline).
- **4-field CF spec**: `feedback_fix-in-session-never-defer.md` (mandatory on §B/§C/§D entries).
- **METHODOLOGY-class M1-M4 + allowlist**: `.claude/rules/wave-classification.md` + `.claude/rules/methodology-wave-allowlist.md` (§D entries must satisfy both).
- **Joint-theorem 4-stage pathway**: `.claude/rules/joint-theorem-promotion.md` (Stage-2 cross-axis verify is the canonical "why not §A" reason for promotion §B entries).
- **Pre-compute shell escalation**: `.claude/rules/Investigating-Workshops.md §"is NOT" item 9` + S91 W7 calibration (§E routing).
- **Canonical §B mirror exemplar**: `sessions/archive/session-88/session-88-w13-workingpaper.md:1303-1323` (CF-W13-5).
- **Canonical §C mirror exemplar**: `sessions/archive/session-88/session-88-w13-workingpaper.md:1325-1343` (CF-W13-6).
- **WP CF section discipline**: `.claude/templates/workingpaper.md §"At wave close (team-lead)"` (CF block format).
- **Discriminator routing**: `.claude/rules/Investigating-Workshops.md §"Discriminating decision: workshop vs compute carry-forward"` (Q1/Q2/Q3 routing table).
- **Capstone-hygiene gate (§A/§B routing target)**: `.claude/rules/capstone-hygiene-gate.md` — a session whose wave-synthesis answers YES to any of the standing 5-question capstone-hygiene checklist (Q1 a(t)-gap / Q2 §7-falsifier-row / Q3 PROVEN-CONDITIONAL-BROKEN-INFO status / Q4 prose-vs-ledger / Q5 citation) routes the capstone-update action into THIS ledger's §A (in-session designated-writer fix) or §B (compute carry-forward). The capstone-hygiene gate is the canonical producer of capstone-touching §A/§B items.
