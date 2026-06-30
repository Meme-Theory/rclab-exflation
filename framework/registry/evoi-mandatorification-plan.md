# EVOI Update + Mandatorification Plan

**Authored**: 2026-05-10
**Scope**: Continuous-story-fill of `sessions/evoi-framework.md` for sessions **S67-S88** (22-session gap) + structural enforcement (mandatorification) to prevent re-occurrence.
**Reading prerequisite**: cold-start readable. Read `feedback_framework-hygiene.md`, `.claude/rules/evoi-prioritization.md`, and `sessions/evoi-framework.md` (especially the S86 Refresh at line 563+) BEFORE executing.

---

## 1. Why this plan exists

Per `feedback_framework-hygiene.md` (user-authored 34 days before this plan):
> "The EVOI priority table at `sessions/evoi-framework.md` has been frozen since S66. It was not updated in S67, S68, or S69 despite dozens of computations being completed and new ones identified... The table must be COMPUTED, not hand-waved — estimate P(pass), delta_P(pass), delta_P(fail) for each gate. After each session, UPDATE the EVOI table with actual results (gates that fired change the priors)."

EVOI is a **continuous story**: each session's predictions vs outcomes calibrate the next session's priors. Discontinuous stamps (S66 → S73B → S78 → S83 → S86) lose the inter-session evolution that EVOI's predictive value depends on. **You cannot compute a useful S88 EVOI without S87's outcomes incorporated; cannot compute S87 without S86's outcomes; etc.** The chain IS the deliverable.

The user's verbatim correction (this session, 2026-05-10):
> "I never relaxed EVOI at all - just the pre-EVOI baysian percentages which were more trouble than worth. I am very concerend that EVOI hasn't been updated since S66 - there is a fucking EVOI entry in every fucking session"

> "You can't just take the last two sessions EVOI and update with that - EVOI is a story, it requires EVERY session to be included to have any usefulness."

---

## 2. Two distinct things, previously conflated

| Concept | Status | Where |
|:--------|:-------|:------|
| **Sagan/panel numerical probability percentages** (P_panel%, P_sagan% column data) | DISCONTINUED post-S66 per user direction (more trouble than worth) | atlas-06 data table; was Sagan workshop output |
| **EVOI per-session priority table** | **REQUIRED EVERY session** per `feedback_framework-hygiene.md` | `sessions/evoi-framework.md` |

Previous atlas text (atlas-00, -01, -04, -06, -08) conflated these by claiming "EVOI frozen since S66" — that's the Sagan-percentage state, NOT the EVOI state. The atlas text correction (Phase 1 of this plan) fixes that propagation.

---

## 3. Current EVOI maintenance state — explicit ledger

From `sessions/evoi-framework.md` provenance line + section headings:

| Session | EVOI state | Section in evoi-framework.md | Gap with previous |
|:--------|:-----------|:-----------------------------|:------------------|
| S66 | INITIAL BASELINE | top-of-file | — |
| **S67** | **FROZEN — NO ENTRY** | (missing) | 1-session gap from S66 |
| **S68** | **FROZEN — NO ENTRY** | (missing) | 2-session gap |
| **S69** | **FROZEN — NO ENTRY** | (missing) | 3-session gap |
| **S70** | **FROZEN — NO ENTRY** | (missing) | 4-session gap |
| **S71** | **FROZEN — NO ENTRY** | (missing) | 5-session gap |
| **S72** | **FROZEN — NO ENTRY** | (missing) | 6-session gap |
| S73B | UPDATE 2026-04-11 | line 500 (`## The Joint Probability Argument (S73B Update)`) | 6-session gap closed by stamp |
| **S74** | **NO ENTRY** | (missing) | 1-session gap from S73B |
| **S75** | **NO ENTRY** | (missing) | 2-session gap |
| **S76** | **NO ENTRY** | (missing) | 3-session gap |
| **S77** | **NO ENTRY** | (missing) | 4-session gap |
| S78 | STAMP (post-scrub; execution tossed) | line 187 (`## The Priority Table (S78 Stamp — historical, pre-S83)`) | 4-session gap closed by stamp |
| **S79** | **NO ENTRY** | (missing) | 1-session gap from S78 |
| **S80** | **NO ENTRY** | (missing) | 2-session gap |
| **S81** | **NO ENTRY** | (missing) | 3-session gap |
| **S82** | **NO ENTRY** | (missing) | 4-session gap |
| S83 | STAMP 2026-04-18 | line 108 (`## The Priority Table (S83 Stamp — 2026-04-18)`) | 4-session gap closed by stamp |
| **S84** | **NO ENTRY** | (missing) | 1-session gap from S83 |
| **S85** | **NO ENTRY** | (missing) | 2-session gap |
| S86 | REFRESH 2026-04-26 | line 563 (`## S86 Refresh -- 2026-04-26`) | 2-session gap closed by stamp |
| **S87** | **NO ENTRY** | (missing) | 1-session gap from S86 |
| **S88** | **NO ENTRY** | (missing) | 2-session gap |

**Total missing per-session entries**: **18** (S67, S68, S69, S70, S71, S72, S74, S75, S76, S77, S79, S80, S81, S82, S84, S85, S87, S88)

The 4 stamps (S73B, S78, S83, S86) are **periodic snapshots**, NOT the continuous chain the rule requires. Each stamp jumped over multiple sessions of inter-session evolution.

---

## 4. The work — continuous-story-fill protocol per session

For EACH of the 18 missing sessions, produce a `## S{N} Refresh -- DATE` entry following the S86 Refresh template (line 563+ of `evoi-framework.md`). Each entry MUST contain:

### 4.1 Per-session inputs (read in order)
1. `computations/session-{N}/s{N}_gate_verdicts.txt` — canonical verdict ledger; ground truth for what fired
2. `sessions/session-plan/session-{N}-plan-w*.md` — planned gates with pre-registered P(pass) priors
3. `sessions/session-{N}/session-{N}-results-workingpaper.md` (or wave-specific files) — synthesis context: what closed, what opened, what paradigm shift if any
4. `sessions/session-{N}/session-{N}-final.md` (if exists; not all sessions have one) — Sagan summary (pre-S67 only) or session-final synthesis

### 4.2 Per-gate computation (for each gate that fired in the session)
For each gate G with verdict V ∈ {PASS, FAIL, INFO}:
- **P_pass_prior(G)**: from plan-block pre-registration (extract from plan file's gate block)
- **outcome(G)**: V from verdict file
- **ΔP_pass(G)**: realized | predicted-vs-actual residual; if PASS at predicted P_pass, ΔP_pass ≈ 0; if FAIL when P_pass=0.7, ΔP_pass = -0.7 (corridor closes)
- **ΔP_fail(G)**: complement
- **EVOI_realized(G) = P_pass_prior × |ΔP_pass| + P_fail_prior × |ΔP_fail|** (information value extracted)

### 4.3 Per-session aggregate
- **completion_fraction increment**: number of newly-closed gates / total open inventory
- **open-channel evolution**: which channels closed (move from open list to closed_mechanisms); which opened (new entries)
- **re-ranked priority queue**: re-sort remaining open gates by EVOI value
- **trendline**: monotone-upward direction confirmation (per `evoi-prioritization.md` §"Effort-Based Probability")

### 4.4 Per-session output entry format
Modeled on S86 Refresh (evoi-framework.md line 563+). Contains:
```markdown
## S{N} Refresh -- YYYY-MM-DD

**Inputs consumed**: {list of verdict file + plan + WP files}
**Gates that fired this session**: {N} (P={pass count} / F={fail count} / I={info count})
**Realized EVOI per fired gate**: {table}
**Open channels evolved**: {table: closed | opened}
**Re-ranked priority queue (top-K post-session)**: {table}
**Trendline**: monotone-upward / NEUTRAL / DOWN-tick (per direction class)
**S66 baseline preservation**: PRESERVED (no historical row rewritten)
**Verdict line emitted**: {GATE_ID for the EVOI refresh gate itself if applicable}

**Closing remark**: {what the post-S{N} bracket feeds the next session's plan-write priority allocation per /rclab-plan}
```

---

## 5. Mandatorification — structural enforcement

The 22-session gap survived because there was no automated check forcing per-session EVOI. The fix:

### 5.1 NEW audit script: `tools/_evoi_continuity_audit.py`
- Walk `sessions/evoi-framework.md` for `## S{N} (Refresh|Update|Stamp)` headings; build `set_present`
- Walk `computations/session-*/s{N}_gate_verdicts.txt` for sessions with actual verdicts; build `set_required`
- `gap = set_required - set_present`
- Output: stdout report + JSON
- WARN mode (default) emits gap list; `--strict` exits 1 on any gap

### 5.2 Wire into `/weave --update` as Phase 8 (post-Phase 7 path-existence audit)
Edit `.claude/skills/weave/skill.md` to add:
```
# Phase 8 — audit EVOI continuity (per-session entry presence)
"phonon-exflation-sim/.venv312/Scripts/python.exe" tools/_evoi_continuity_audit.py --json
```
WARN-only inside /weave --update; standalone --strict for CI.

### 5.3 NEW rule file: `.claude/rules/evoi-continuous-story.md`
Codifies what `feedback_framework-hygiene.md` directs (the feedback file is user-private memory; the rule file is project-scoped + versioned + agent-loaded). Contents:
- "EVOI is a continuous story; per-session entry MANDATORY"
- Audit script reference + threshold
- S86 Refresh as canonical template
- Cross-link to `evoi-prioritization.md` (methodology) and `evoi-framework.md` (the table)
- Pre-registration: every plan-block must include P_pass prior estimate; every closeout must compute realized ΔP_pass

### 5.4 Update `/rclab-coordinate` (or session-close workflow) checklist
Add EVOI refresh as a session-close gate: a session cannot be marked formally complete until its EVOI Refresh entry is written. (Session-close hook OR last-wave-of-session synthesis MUST include the EVOI refresh.)

### 5.5 Update `feedback_framework-hygiene.md` (user memory) cross-link
Update the feedback file to point at the new rule file + audit script for enforcement. Note in the feedback: "Mandatorification landed via `_evoi_continuity_audit.py` Phase 8 of /weave --update + `.claude/rules/evoi-continuous-story.md` + `/rclab-coordinate` close-out checklist."

---

## 6. Atlas text correction — mechanical fix (Phase 1 of execution)

5 atlas files; ~10 lines total. Replace the conflated "EVOI frozen since S66" claims with the correct distinction.

### Files + lines + corrected wording

**atlas-00-index.md**:
- Line 5: replace "EVOI table frozen since S66" → "Sagan/panel numerical probability percentages discontinued post-S66 (user direction); EVOI per-session priority table required EVERY session per `feedback_framework-hygiene.md` — current state has 18-session gap pending fill (see `sessions/framework/registry/evoi-mandatorification-plan.md`)"
- Line 36: replace "EVOI frozen since S66" → "Sagan numerical assessment discontinued post-S66"
- Line 80: same correction in vital signs row

**atlas-01-session-timeline.md**:
- Line 487: replace "TBD (frozen since S66)" → "TBD (Sagan re-anchoring pending)"
- Line 501: rewrite the **Note** to distinguish the two concepts properly
- Line 512: drop "Sagan workshop S89 to re-anchor probability trajectory (frozen since S66)" → "Sagan workshop S89 to re-anchor probability trajectory + EVOI 18-session continuous-story-fill (S67-S88 missing per-session entries) per `evoi-mandatorification-plan.md`"

**atlas-04-assumptions.md**:
- Line 192: rewrite to: "Per `feedback_framework-hygiene.md`, **EVOI per-session priority table required EVERY session**; current state has 18-session gap (S67-S88 missing) pending fill per `evoi-mandatorification-plan.md`. Separately: no formal Sagan probability assessment has been conducted post-S66 (Sagan numerical % discontinued per user direction; not the same as EVOI)."

**atlas-06-probability-trajectory.md**:
- Line 4 + Line 6: rewrite the header **Authority** + **Updated** to:
  - Sagan/panel numerical % discontinued post-S66 (user direction)
  - EVOI per-session table required EVERY session (NOT frozen; gap is being filled per `evoi-mandatorification-plan.md`)
- Line 85: same correction in the data-table footer note
- Line 101: keep the layer-tag forward-looking discipline; just remove the "Sagan re-anchoring" mis-phrasing
- Lines 227 + 245: rewrite the closing-paragraph + final-assessment paragraphs to distinguish the two concepts

**atlas-08-open-questions.md**:
- Line 285 (Q44): split into Q44 (Sagan re-anchoring) + Q44.5 (EVOI continuous-story-fill — references this plan file)

---

## 7. Execution sequence (multi-batch; cold-start friendly)

Each phase below is independently runnable from cold-start. Read this plan + the prerequisite files at top, then execute the phase.

### Phase 1 — Atlas text correction (~15 min focused; mechanical)
- Fix the ~10 lines across 5 atlas files per Section 6
- Verify with `grep "EVOI.*frozen since S66\|EVOI.*FROZEN.*S66" sessions/framework/Atlas/` — expect 0 hits
- Commit-checkpoint candidate

### Phase 2 — Build `_evoi_continuity_audit.py` (~30 min)
- Model on `tools/_path_existence_audit.py` structure (this session's deliverable; canonical example of audit-script + JSON-report + --strict mode)
- Walk `evoi-framework.md` for `## S{N}` section headings
- Walk `computations/session-*/s{N}_gate_verdicts.txt` for sessions with verdicts
- Diff: gap = sessions-with-verdicts - sessions-in-evoi-framework
- Emit JSON + stdout report
- Verify: at this point, expect gap = 18 (S67, S68, S69, S70, S71, S72, S74, S75, S76, S77, S79, S80, S81, S82, S84, S85, S87, S88)

### Phase 3 — Wire to `/weave --update` Phase 8 (~10 min)
- Edit `.claude/skills/weave/skill.md` to add Phase 8
- Add `--audit-evoi` standalone subcommand mirroring the `--audit-paths` pattern (this session's precedent at line 271+ of skill.md)
- Verify: `/weave --update` runs Phase 8 and emits the WARN listing 18 gap sessions

### Phase 4 — NEW rule + feedback cross-link (~15 min)
- Write `.claude/rules/evoi-continuous-story.md` per Section 5.3 spec
- Update `feedback_framework-hygiene.md` to cross-link the new rule + audit
- Verify: rule loads in agent system prompts; audit references rule file

### Phase 5 — Continuous-story-fill (the substantive 18-session work)
**Recommend executing in 4 batches over multiple focused sessions** (NOT in one cold-start; each batch needs fresh attention to gate-by-gate accuracy):

**Batch A — S67-S72 (6 sessions; original freeze period)**:
- Earliest gap; covers Volovik DILUTION-CC PASS aftermath, FUNCTIONAL-SELECT-67, Leggett DM lock-down, n_s scheme-dependence, BBN constraint
- Per-session: 1-2 hours focused work

**Batch B — S74-S77 (4 sessions; post-S73B inter-stamp)**:
- DILUTION-CC scheme-lock at S74; f_conv A_s closure at S75; transit + α_s sharpening at S76; A_s inversion paradigm shift at S77
- Per-session: 1-2 hours

**Batch C — S79-S82 (4 sessions; post-S78-scrub)**:
- Frozen Spectrum Theorem at S79; PRDR enforcement at S80; PRU-zero at S81; substrate-IC corridor + workshop methodology launch at S82
- Per-session: 1-2 hours

**Batch D — S84-S85 + S87-S88 (4 sessions; post-S83/S86 stamps)**:
- Branch-(iv) RETRACTED at S84; Dual-SHA mandatory + α_s sharpening at S85; cross-pillar K=3 promotions at S87; full S88 cycle
- Per-session: 1-2 hours

**Total estimated effort**: 18 sessions × ~1.5 hours = **~27 hours of focused work**, distributable across 4-5 dedicated work sessions.

### Phase 6 — Validation gates (after each batch + final)
- After each batch: re-run `_evoi_continuity_audit.py` to confirm gap shrinking
- Final: `_evoi_continuity_audit.py --strict` exits 0 (all S67-S88 covered)
- `/weave --update` Phase 8 shows clean

### Phase 7 — Mandatorification commit
- Add `_evoi_continuity_audit.py --strict` to CI / pre-commit gates (if applicable)
- Verify: a session that closes WITHOUT writing an EVOI Refresh entry triggers WARN at next /weave --update
- Update `team-lead-behavior.md` and `/rclab-coordinate` skill close-out checklist

---

## 8. Token-budget guidance

- **This plan is fully self-contained**: cold-start readable. Read it + the 3 prerequisite files (top of section 1) and execute any phase independently.
- **Phase 1** (atlas correction) is one-context-window task (~15 min)
- **Phase 2-4** (audit script + skill wire-up + rule file) is one-context-window task (~1 hour)
- **Phase 5** is the 4-batch substantive work; each batch is its own context window (recommend separate /clear between batches)
- **Phase 6-7** is post-fill validation; one-context-window task (~30 min)

After each phase, /weave --update + git commit-checkpoint to lock progress. Avoid trying to compress the substantive 18-session fill into context-rolls — the gate-by-gate accuracy needed is the whole point.

---

## 9. Cross-references (canonical sources)

- `feedback_framework-hygiene.md` (user memory) — the original directive
- `.claude/rules/evoi-prioritization.md` — EVOI methodology (P(pass) × |ΔP_pass| + P(fail) × |ΔP_fail|)
- `sessions/evoi-framework.md` — the canonical EVOI table being filled
- `sessions/permanent-results-registry.md` — closed mechanisms ledger (input to per-session open-channel evolution)
- `tools/_path_existence_audit.py` + `tools/_path_existence_fix.py` — canonical audit-script template (model for `_evoi_continuity_audit.py`)
- `.claude/skills/weave/skill.md` — `--audit-paths` precedent for adding `--audit-evoi` subcommand + Phase 8 invocation
- atlas-06 (probability-trajectory) — directional history (separate from EVOI; needs Section-6 corrections per Phase 1)
- atlas-08 (open-questions) — open-channels inventory (input to per-session EVOI re-ranking)

---

## 10. Done criteria

This plan is COMPLETE when:

1. **Atlas text corrections applied** (5 files, ~10 lines): Phase 1 ✓
2. **`_evoi_continuity_audit.py` script ships**: Phase 2 ✓
3. **`/weave --update` Phase 8 wired**: Phase 3 ✓
4. **`.claude/rules/evoi-continuous-story.md` rule file ships**: Phase 4 ✓
5. **All 18 missing session entries (S67-S72, S74-S77, S79-S82, S84-S85, S87-S88) added to `evoi-framework.md`**: Phase 5 ✓
6. **`_evoi_continuity_audit.py --strict` exits 0**: Phase 6 ✓
7. **Session-close gate enforces EVOI refresh going forward**: Phase 7 ✓

When all 7 conditions hold, the 22-session EVOI gap is closed AND mandatorified — never to recur silently again.

---

## 11. Anti-patterns to avoid (from this conversation's lessons)

1. **DO NOT compress 18 sessions of priority-evolution into one context window**. The user explicitly rejected this approach: "You can't just take the last two sessions EVOI and update with that - EVOI is a story, it requires EVERY session to be included to have any usefulness."
2. **DO NOT conflate "Sagan numerical %" with "EVOI table"**. They are distinct. Sagan % was discontinued; EVOI was NOT. The conflation across atlas-00/-01/-04/-06/-08 (~10 lines) is what surfaced this whole investigation.
3. **DO NOT defer per-session EVOI to "next session's plan"**. The feedback rule says EVERY session must include it; the mandatorification (Phase 5.4 close-out gate) enforces this going forward.
4. **DO NOT generate plausible-looking P(pass) priors without grounding them in actual plan-block pre-registrations**. Each per-gate prior MUST be extracted from the gate's plan-block, not synthesized.
5. **DO NOT skip the FROZEN S67-S72 fill assuming "the stamps cover it"**. The stamps are periodic snapshots that lose inter-session evolution; the fill needs continuous per-session entries.
