# Investigating Workshops

## Scope

This rule governs how `/rclab-investigate` (and any agent identifying workshop opportunities from a closed session's substance) distinguishes WORKSHOPS from CARRY-FORWARDS. It applies at investigator-prompt level, consolidator-prompt level, and at any session-end synthesis where the question is "what should be reviewed multi-agent next."

The `/rclab-investigate` skill's Phase 3a investigator prompt template uses the permissive phrasing "workshops, solo syntheses, or follow-up investigations" — this permissiveness is the structural cause of the carry-forward-listing failure mode. **This rule overrides that permissiveness.** Workshop-schedule deliverables are workshops, period; solos and follow-up computes are categorized differently and routed differently (see §"Cross-references" below).

## Definition: A WORKSHOP IS

A workshop is a structurally-specific kind of follow-up dispatch. ALL FOUR conditions must hold:

1. **TWO+ agents with COMPETING perspectives on a SPECIFIC TENSION**. Not one agent narrating a result, not two agents agreeing in parallel — two or more agents who *disagree* about how to read a claim, a verdict, or a structural pattern.
2. **Genuine LEDGER-DISSONANCE**: a competing-claim adjudication. The two perspectives MUST diverge on something concrete (a number, a sign, a structural reading, a methodology choice, a convention pin).
3. **Multi-round structure**: R1 steelman / R2 respond to opponent's best case / R3 converge on verdict. Three rounds for genuine adversarial review; two rounds for routine adjudication; one round only for informational exchanges (rare).
4. **Output: STRUCTURAL VERDICT** that resolves the competing claims. The workshop produces a NEW pinned position (a verdict, a registry entry, a rule diff, a pre-registered gate) — NOT a queued computation to run later.

## Definition: A WORKSHOP is NOT

The following are NOT workshops, even when narrative-inflated to look like ones:

1. **Solo compute follow-ups** — "Compute X next session" with pre-registered threshold and machinery pin. → carry-forward computation; belongs in S{N+1} session plan via `/rclab-plan`.
2. **Verification gates** — Stage-2 cross-check, plan-freeze audit, independent-verify dispatches. These have pre-specified protocol; nothing to adjudicate. → queued computation gate.
3. **Re-listings of WP-enumerated carry-forwards** — A wave-synthesis "Carry-forwards (4-field specs)" list re-formatted as "candidates". The carry-forwards already exist in the session's WP; the next-session planner picks them up directly. Re-naming them "workshops" adds zero structural content.
4. **Single-agent "synthesis" of one wave's gates** — That's a per-wave digest, useful as background but not a workshop.
5. **Single-agent "exploration" of a registry slot** — Even with "2-agent workshop" framing, if there's no genuine adversarial tension between the two named agents, it's a solo dispatch in disguise.
6. **Methodology-rule extension proposals where both agents would agree on the extension's content** — Workshop requires DISAGREEMENT, not parallel-agreement implementation.
7. **Registry-state classification choices / hygiene-promotion items / framework-housekeeping** — Choosing between registry status markers (PERMANENT vs PROVEN vs STAGE-1-CANDIDATE vs STRUCTURALLY-OPEN-BY-DESIGN) for already-landed slots, promoting LANDED-but-not-promoted records, fixing PROVENANCE-dict hygiene, addressing gate-finalization gaps, or other framework-housekeeping is bookkeeping, NOT adversarial substrate-physics. Even when the choice has structural import, the resolution is a registry-state design decision, not a substrate-physics tension between competing readings of an observable. → `session-{N}-housekeeping.md` §A (in-session fix) or §B/§D (deferred compute, mirrored to WP CF) per `.claude/templates/session-housekeeping.md`. NOT a workshop.
8. **Parallel-compute-wave structures dressed as N-agent panels** — When N prerequisite conditions can each be tested by an independent compute gate on its own pre-registered axis (substrate-physics / observational / methodology), and the N verdicts combine via logical AND for the final outcome, the structure is a **parallel-compute-wave** (N independent gates + 1 wave-AND closeout), NOT an N-agent workshop panel. The per-axis agent attribution is a derivation-author tag (which agent owns the math for axis X), not a workshop-participant tag (which agent debates which reading). No adversarial round protocol is needed because the axes are structurally orthogonal. → `session-{N}-housekeeping.md` §C (mirrored to WP CF, marked "wave-together") per `.claude/templates/session-housekeeping.md`.
9. **Not-yet-executed wave / pre-compute shell** — Wave with all gates `Status: NOT STARTED`, no `s{N}_w{stem}_*` artifacts on disk, and no matching gate-IDs in the verdict file. Investigator: emit `## Not investigated — wave w{stem} is pre-compute shell` (one sentence) and skip the wave in subsequent steps. Do NOT create a `CF-S{N+1}-W{stem}-WAVE-EXECUTION` or analogous "execute this wave next session" carry-forward. Consolidator: do NOT lift any wave-execution CF for the shell wave into its WP. → `session-{N}-housekeeping.md §E` (escalation only — `/rclab-coordinate` retry, NOT a CF) per `.claude/templates/session-housekeeping.md`.


## How to identify a real workshop in session substance

Look for these signals when reading a session's gates and verdicts:

- **FAILs that admit MULTIPLE structural readings** — Agent A reads the FAIL as evidence of X; agent B reads it as evidence of Y. The reading divergence is the workshop seed.
- **INFOs at borderline** — borderline-evidence values (e.g., ~0.5σ-1σ detections) where domain agents will disagree about marginal-detection vs regulator-class-dependent noise.
- **CROSS-WAVE tensions** — One wave's PASS conflicts with another wave's INFO/FAIL. The framework's own ledger has a contradiction that needs adjudication.
- **Methodology-vs-substrate-physics blurs** — A rule-extension proposal where the right shape is contested; two methodology agents give different rationales.
- **Convention questions where TWO PERSPECTIVES GENUINELY DIVERGE** — regulator-pin convention, scheme choice, observable definition, registry-anchor structure (PRIMARY+CONFIRMATION vs SOURCE-DOUBLE-CITE-CO-PRIMARY).
- **EXISTING claims that need ADVERSARIAL TESTING** — Not "compute next" but "audit what we already claimed." A registered theorem may need an adversarial review of its sufficiency conditions.

If the session's substance contains NONE of the above, the session produced NO workshops. That's a valid output.

## "No workshops" is a valid output

A session with clean PASSes, unambiguous verdicts, no cross-wave conflicts, and settled methodology produces ZERO workshops. The investigator MUST emit "## No workshops" with one paragraph explaining why. This is HONEST.

Padding with carry-forward listings dressed as workshops is a violation of:

- This rule (the workshop definition)
- `feedback_fix-in-session-never-defer.md` (carry-forwards belong in next session's plan)
- `feedback_max-effort-full-fidelity.md` (length is not quality)
- `feedback_session-process.md` (the feedback rule this rule promotes to permanent status)

## Honest count discipline

A typical session produces 0-4 genuine workshops. Even a content-heavy 17-wave session may produce only 2-5 genuine workshops; the rest of the substance feeds carry-forwards (next session's plan) or is settled in-place. Investigators who report 5-10 "workshops" per wave are almost certainly carrying-forward bloviation. Sanity-check the count against the four-condition definition above.

## Discriminating decision: workshop vs compute carry-forward

When evaluating any candidate from a closed session's substance, apply this 3-question decision procedure BEFORE adding it to the workshop schedule. The first YES wins.

### Q1 — Is the tension a math/physics adjudication?

Does the candidate's resolution require deciding between TWO+ competing readings of a substrate-physics observable, structural identity, or convention with first-principles arguments on both sides? If YES → workshop. If NO → not a workshop; continue to Q2.

A "math/physics adjudication" has these markers: (i) the disagreement is about WHAT the substrate-physics result MEANS, not what status to tag it with; (ii) the readings invoke different machinery (FI vs RD; algebra-INVARIANT vs algebra-DEPENDENT; HKR-bridge vs K-theory boundary; substrate-IS vs definitional-tautology); (iii) the two readings cannot both be right — the workshop's job is to derive which is correct from first principles, producing a STRUCTURAL VERDICT.

### Q2 — Is the candidate registry-state classification, hygiene, gate finalization, or framework-issue?

A candidate is Q2 iff its resolution is one of the following marker classes:

- **Status-tag edit** — choosing between status markers (PERMANENT / PROVEN / STAGE-1-CANDIDATE / STRUCTURALLY-OPEN-BY-DESIGN) for already-landed registry slots.
- **Mechanical promotion** — promoting LANDED-but-not-promoted records via the canonical 4-stage pathway (`joint-theorem-promotion.md`); pre-conditions already met, only the bookkeeping move remains.
- **Provenance / canonical-constants hygiene** — adding a missing PROVENANCE-dict entry, promoting a single-value pin to `canonical_constants.py`, registering a constant in the knowledge MCP.
- **Methodology-rule extension** — a rule-file diff that both candidate agents would agree on (no DISAGREEMENT in the workshop sense; cross-link "is NOT" item 6).
- **Audit-script extension** — adding regex patterns, detector subroutines, hook updates, or audit-trail extensions that any methodology-aware agent would derive the same way.
- **Registry-write hygiene** — parallel-writer race gaps, append-helper protocol violations, anchor-structure re-tags, slot-rerouting documentation.
- **Gate-finalization gap** — verdict-file backfill, dual-SHA companion-row repair, working-paper §-section finalization the gate-completion verification missed.
- **Pre-compute shell escalation** — waves with all gates `Status: NOT STARTED` (per "is NOT" item 9). Routes to `/rclab-coordinate` retry, NOT a CF.

**Marker test (one-line)**: would the resolution be a status-tag edit / mechanical promotion / rule-file diff / audit-script extension / mechanical re-run, rather than a derivation that produces a new structural claim? If YES → it's Q2. The "tension" is bookkeeping, not adversarial physics.

#### Routing — at wave-compute time, NOT at `/rclab-investigate` time

Q2 items MUST be identified during the wave-synthesis step of `/rclab-coordinate` (when the team-lead is writing the `## Wave {W} Synthesis` section of the WP), BEFORE `/rclab-investigate` runs. By the time `/rclab-investigate` dispatches, every Q2 item from S{N} should already be catalogued in the per-session housekeeping ledger.

The canonical Q2 ledger is `sessions/session-{N}/session-{N}-housekeeping.md` (template: `.claude/templates/session-housekeeping.md`). Its 5-section partition routes Q2 items by lifecycle:

| Section | Item lifecycle | Mirrored to |
|:--------|:---------------|:------------|
| **§A — In-session resolutions** | Fixed during S{N} (per `feedback_fix-in-session-never-defer.md`); ledger entry only | none — already effected |
| **§B — Hygiene compute carry-forwards** | Q2 mechanical re-run needs S{N+1} compute; 4-field spec | `session-{N}-w{w}-workingpaper.md §"Carry-Forward Computations"` as `CF-S{N+1}-HK-{n}` |
| **§C — Parallel-compute-wave carry-forwards** | Q3 wave-together: N axes + AND closeout (cross-link Q3 below) | Same as §B, marked "wave-together" |
| **§D — Methodology-rule extensions** | Q2 rule-file diff; cite `wave-classification.md §M1-M4` + allowlist | Same as §B |
| **§E — Pre-compute shell waves** | Upstream-coordinator escalation per "is NOT" item 9; NOT a CF | `/rclab-coordinate` retry — do NOT mirror to WP CF |

The housekeeping file is the CANONICAL Q2 ledger; WP CF blocks (where applicable) are MIRRORS. This split is load-bearing: `/rclab-investigate` filters against housekeeping.md (authoritative "non-workshop" list); `/rclab-plan` consumes WP CF blocks (its existing contract, unchanged).

#### Enforcement at `/rclab-investigate`

Investigators MUST read `sessions/session-{N}/session-{N}-housekeeping.md` BEFORE producing any candidates. Every item in that file is structurally a non-workshop by Q2 classification — drop, do not propagate to seed.

A Q2 candidate surfaced for the FIRST TIME by the investigator (i.e., not already in housekeeping.md) indicates an upstream wave-synthesis miss: the team-lead at wave-close should have caught it. The investigator routes the new Q2 candidate to housekeeping.md (NOT the workshop schedule), mirrors any forward-compute portion to the wave's WP CF, and logs a one-sentence process observation about the miss in the seed file. This keeps housekeeping.md authoritative even when wave-synthesis was incomplete.

### Q3 — Is the candidate a parallel-compute-wave structure (N conditions × N axes)?

Does the candidate involve N prerequisite conditions, each on a different substrate-physics / observational / methodology axis, where each condition has its own pre-registered PASS criterion AND the N verdicts combine via logical AND for the final outcome? If YES → compute carry-forward to the WP as a parallel-wave-together structure (N pre-registered sub-gates + 1 wave-AND closeout).

The trap: if the same N agents would be "dispatched" for the workshop AND for the parallel compute, it LOOKS like a workshop. But:

- A workshop **panel** has N agents converging on a SINGLE adversarial verdict via R1/R2/R3 rounds with cross-agent rebuttals. The reading-divergence is genuine.
- A parallel-compute-wave has N **independent** gates, each producing its OWN verdict on its OWN axis, with a single AND-closeout. No cross-agent rebuttal because the axes are structurally orthogonal — agent X cannot meaningfully rebut agent Y's verdict on a different axis.

If the candidate fits Q3, it is NOT a workshop, regardless of how many agents would be involved. The agent-attribution per axis is a derivation-author tag (which agent owns the math for axis X), not a workshop-participant tag (which agent debates which reading).

### Routing summary

| Decision | Route to | Canonical file | Mirror (where applicable) |
|:---------|:---------|:---------------|:--------------------------|
| Q1 YES (math/physics adjudication) | Workshop schedule via `/rclab-investigate` | `sessions/session-{N}/session-{N}-workshop-schedule[-w{W}].md` | — |
| Q2 YES — in-session fix | Housekeeping ledger §A (record of completed fix) | `sessions/session-{N}/session-{N}-housekeeping.md §A` (template: `.claude/templates/session-housekeeping.md`) | — (the fix itself lives in the relevant rule/template/registry file) |
| Q2 YES — hygiene compute carry-forward (Stage-2 verify, mechanical promotion w/ compute, etc.) | Housekeeping ledger §B | `session-{N}-housekeeping.md §B` | `session-{N}-w{w}-workingpaper.md §"Carry-Forward Computations"` as `CF-S{N+1}-HK-{n}` |
| Q3 YES (parallel-compute-wave, N conditions × N axes) | Housekeeping ledger §C, marked "wave-together" | `session-{N}-housekeeping.md §C` | Same as Q2-hygiene; mirror block carries the wave-together tag |
| Q2 YES — methodology rule extension (M1-M4 + allowlist) | Housekeeping ledger §D | `session-{N}-housekeeping.md §D` | Same as Q2-hygiene |
| Pre-compute shell wave (per "is NOT" item 9) | Housekeeping ledger §E (escalation only; NOT a CF) | `session-{N}-housekeeping.md §E` | — (escalation routes to `/rclab-coordinate` retry, not WP CF) |
| Multiple YES | Q1 wins. If Q1 NO, Q2 wins. If Q2 NO, Q3 wins. | — | — |

**Critical (canonical-vs-mirror split)**: `session-{N}-housekeeping.md` is the CANONICAL Q2 ledger — the authoritative filter source for `/rclab-investigate` (investigators read it BEFORE seeding candidates and skip everything in it). The WP `## Carry-Forward Computations` mirrors are the load-bearing consumption source for `/rclab-plan` (whose existing contract reads WPs, not housekeeping ledgers or workshop schedules). Both views see the same underlying §B/§C/§D items; the split keeps each consumer reading from its native file shape without rewiring upstream pipelines. A compute carry-forward that lives ONLY in the workshop schedule, OR ONLY in housekeeping.md without a WP CF mirror, is invisible to one or the other consumer — both surfaces must agree for §B/§C/§D items.

## Cross-references

- **Carry-forwards go in `/rclab-plan`** — per `feedback_fix-in-session-never-defer.md`, every wave-synthesis produces 4-field structured carry-forwards (what / inputs / gate / effort). Those are inputs to the NEXT compute session's plan, not to a workshop schedule. The workshop schedule and the carry-forward plan are SEPARATE OUTPUTS.
- **`/rclab-investigate` skill** — investigator and consolidator prompts MUST cite this rule as authoritative. Phase 3a's permissive "workshops, solo syntheses, or follow-up investigations" language is overridden: the deliverable is workshops only.
- **`/rclab-plan`** — workshop-schedule consumers feed S{N+1}'s plan via two SEPARATE input streams: (a) workshop OUTCOMES (verdicts produced by `/rclab-review` dispatches against the schedule), (b) carry-forward COMPUTATIONS (queued computation gates from wave-syntheses). The plan author distinguishes these.
- **`feedback_session-process.md`** — this rule's enforcement requires that the investigator can SEE enough cross-wave substance to identify cross-wave tensions. For very large WPs (10K+ lines), the partition is size-driven; each chunk should cover multiple waves so cross-wave tensions are visible to at least one investigator.

## Forward-looking enforcement

Future `/rclab-investigate` dispatches MUST cite this rule in the investigator prompt and require the investigator to read it BEFORE producing candidates. The investigator's seed file MUST use the heading `## Workshops` (not `## Candidates`) to enforce the categorical distinction. Solo computes that emerged from the wave's substance go into a SEPARATE seed-file section `## Carry-forwards (route to /rclab-plan, NOT this schedule)` so they're explicitly tagged as not-workshop content.
