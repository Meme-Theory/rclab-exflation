# Session 82 Plan: S80 Compute Queue Carry-Forward + S81 Follow-ups

**Date**: 2026-04-17 (planned)
**Session**: 82
**Author**: orchestrator (post-S81 close)
**Format**: Parallel single-agent computations (compute mode — match S80 plan §II Operational Discipline)
**Source**: `sessions/archive/session-80/session-80-results-workingpaper.md §VI` (S80 honest close) + `sessions/archive/session-81/session-81-results-workingpaper.md §X` (S81 carry-forward)
**Motivation**: S80 stalled mid-Wave-1 with 33 pre-registered computations unexecuted. The pre-registrations remain valid: no plan-property (PRU) failures were identified in the unexecuted items; each carries a full Gate / Trigger / Inputs / Script / Results-template specification in the S80 plan. Rather than re-author the specifications, S82 references them by line-number and re-dispatches. Per `.claude/rules/session-handoffs.md` recommendation-carry-forward rule: every S80 NOT-STARTED item appears here as a planned computation.
**Results file**: `sessions/archive/session-82/session-82-results-workingpaper.md` (to be created)

---

## I. Session Objective

S82 has two missions:

1. **Execute the unexecuted S80 compute queue** — 33 items inherited from S80's Wave 1 / Wave 2 / Wave 3. S80 plan specifications (`sessions/session-plan/session-80-plan.md`) remain the authoritative pre-registration; S82 is the execution pass.

2. **Resolve W0-15 INFO-6 taxonomy** via the 2D-BZ extension of s52 — predicted to yield 7 branches (Scenario A of W0-15's decision rule), which would unblock W0-14 phononic-length canonicalization.

### Pre-Registered Master Gate

- **GATE: S82-MASTER**: Three critical decisive verdicts from the original S80-MASTER
  set AT MINIMUM (H̃-EPOCH, UNIFIED-AS-79-FULL, CC-Ratios-Only) must land before
  Wave 2 + Wave 3 dispatch. Additionally, the W0-15 → W0-14 reconciliation must
  complete (either via 2D-BZ yielding 7 confirming Scenario A, or via explicit
  justification for the 6-count canonicalization).
- **PASS**: W1-1, W1-2, W1-4 all land with decisive verdicts AND (W0-A 2D-BZ
  yields ≤7 branches with reconciliation OR W0-14 proceeds with 6-entry
  canonicalization).
- **FAIL**: Any of the three Wave 1 critical gates returns INCOMPUTABLE.
- **Null hypothesis**: S80's null still applies (P_work_complete moves by
  ≤0.02 absent these gates landing; A_s observable alignment stays at 6/9
  without W1-1 + W1-2).

### Operational Discipline

Unchanged from S80 plan §I. Single-agent compute mode; independent Agent
tool invocations; 4-tuple output tags mandatory; SHA-64-char closures
mandatory per S81-hardened `.claude/rules/gate-verdicts.md`.

---

## II. Carry-Forward Inventory (33 items + 2 S81-added)

### II.A. Wave 0 carry-forward (1 item from S80, blocked)

| S82 ID | S80 ID | Title | S80 spec line | Status at S80 close |
|:-------|:-------|:------|--------------:|:--------------------|
| W0-1 | W0-14 | Phononic-Length Canonicalization (5-entry + K_star_goldstone) | §W0-14 | BLOCKED on W0-15 reconciliation |

### II.B. Wave 0 add-ons (S81-identified)

| S82 ID | Source | Title | Rationale |
|:-------|:-------|:------|:----------|
| W0-A | S81 §VI.2 prediction | 2D-BZ extension of `s52_gl_josephson.py` | Rank-universality predicts 7 branches on full 3D BCC; s52 currently produces 6 on 1D K-cut. 2D-BZ extension closes the off-by-1 (or confirms Scenario A INFO-6 is structural). Unblocks W0-1 (W0-14). |

### II.C. Wave 1 carry-forward (5 items — W1-3 was DONE)

| S82 ID | S80 ID | Title | S80 spec line | EVOI | Owner |
|:-------|:-------|:------|--------------:|:-----|:------|
| W1-1 | W1-1 | H̃-EPOCH-CONSISTENCY | §W1-1 (L1732) | 0.300 | transit-dynamics + lizzi-spectral-functional |
| W1-2 | W1-2 | UNIFIED-AS-79-FULL | §W1-2 (L1912) | 0.211 | transit-dynamics + landau-condensed-matter |
| W1-3 | W1-4 | CC-RATIOS-ONLY-THEOREM | §W1-4 (L2270) | 0.12 | connes-ncg + spectral-geometer |
| W1-4 | W1-5 | CHI-N-WARD-DUAL | §W1-5 (L2572) | 0.074 | gen-physicist |
| W1-5 | W1-6 | CSUB-SIGN identity | §W1-6 (L2656) | 0.073 | landau-condensed-matter |

### II.D. Wave 2 carry-forward (15 items, all NOT STARTED at S80 close)

| S82 ID | S80 ID | Title | S80 spec line | Owner |
|:-------|:-------|:------|--------------:|:------|
| W2-1 | W2-1 | UNIFIED-AS-79-FULL-REPLAY under H̃-branch | §W2-1 (L2707) | transit-dynamics |
| W2-2 | W2-2 | UNIFIED-BACKREACT-79 | §W2-2 (L2721) | transit-dynamics |
| W2-3 | W2-3 | KASPAROV-ABELIAN-PROOF | §W2-3 (L2735) | van-den-dungen-bridge + connes-ncg |
| W2-4 | W2-4 | PS-SUBSTRATE-MATCHED-IC | §W2-4 (L2753) | transit-dynamics + volovik |
| W2-5 | W2-5 | HEAT-KERNEL-MP-EXCLUSION | §W2-5 (L2767) | connes-ncg + spectral-geometer |
| W2-6 | W2-6 | GW-CHANNEL α vs γ Discrimination | §W2-6 (L2781) | einstein + feynman |
| W2-7 | W2-7 | W3G-β R1/R2/R3 DESI Falsifier Registration | §W2-7 (L2795) | mack-cosmic-bridge + einstein |
| W2-8 | W2-8 | A2-CLUSTER-TEST | §W2-8 (L2809) | lizzi + spectral-geometer |
| W2-9 | W2-9 | MULTIPAIR-ECOND | §W2-9 (L2823) | landau + volovik |
| W2-10 | W2-10 | B1-JENSEN-SCAN | §W2-10 (L2837) | landau |
| W2-11 | W2-11 | S++-FULL-ED | §W2-11 (L2851) | landau |
| W2-12 | W2-12 | CUSHION-DERIVATION-PIN | §W2-12 (L2865) | einstein |
| W2-13 | W2-13 | F0-CONVENTION-AUDIT | §W2-13 (L2879) | einstein + feynman |
| W2-14 | W2-14 | FIRAS-CHLUBA-FULL | §W2-14 (L2893) | mack-cosmic-bridge |
| W2-15 | W2-15 | PHASE-ALIGNMENT-K-SCAN | §W2-15 (L2907) | transit-dynamics |

### II.E. Wave 3 carry-forward (14 items, all NOT STARTED at S80 close)

| S82 ID | S80 ID | Title | S80 spec line | Owner |
|:-------|:-------|:------|--------------:|:------|
| W3-1 | W3-1 | RANK-UNIVERSALITY-PROOF | §W3-1 (L2923) | spectral-geometer + lizzi |
| W3-2 | W3-2 | R-FAMILY-ATLAS-EXTENSION | §W3-2 (L2937) | lizzi + connes-ncg |
| W3-3 | W3-3 | DIM-H-PI-UNIVERSAL-EXCLUSION | §W3-3 (L2951) | connes-ncg + van-den-dungen |
| W3-4 | W3-4 | GGE-FNL-CHANNEL | §W3-4 (L2965) | mack-cosmic-bridge + volovik |
| W3-5 | W3-5 | FAMP-SC-3PI | §W3-5 (L2979) | transit-dynamics |
| W3-6 | W3-6 | SIC-PHYSICAL-CAP | §W3-6 (L2993) | transit-dynamics |
| W3-7 | W3-7 | EJ-CONVENTION-AUDIT | §W3-7 (L3007) | einstein + feynman |
| W3-8 | W3-8 | MU-EFF-LK | §W3-8 (L3021) | landau |
| W3-9 | W3-9 | AS-ADJACENT-OBS | §W3-9 (L3035) | gen-physicist |
| W3-10 | W3-10 | CUBIC-SIN2-W-EW | §W3-10 (L3049) | feynman |
| W3-11 | W3-11 | XI-BCS-VS-L-PHONON-CLASSIFICATION | §W3-11 (L3063) | quantum-acoustics + lizzi |
| W3-12 | W3-12 | L-PHONON-DERIVATION | §W3-12 (L3077) | quantum-acoustics |
| W3-13 | W3-13 | FOUR-SPEED-PROVENANCE-PIN | §W3-13 (L3091) | quantum-acoustics + landau |
| W3-14 | W3-14 | C-GOLD-PROVENANCE-REPAIR | §W3-14 (L3105) | lizzi |

### II.F. Post-S81 optional quality passes (S82+ discretion)

| ID | Title | Scope |
|:---|:------|:------|
| Q-1 | Physicist-aware 4-tuple refinement | 443 theorem rows got section-aware placeholder classes in S81. A per-theorem pass replacing `scheme=STRUCTURAL-THEOREM` with the specific theorem's class (e.g., Block-Diagonality → `scheme=STRUCTURAL-ALGEBRAIC`) improves downstream trace quality but is NOT blocking. |
| Q-2 | Level 3 minor-graded script sweep | Level 2 identified MINOR-graded scripts not yet individually re-run. Lower priority than Wave 2/3; consider after Master Gate lands. |

Q-1 and Q-2 are optional — they don't appear on the Master Gate. Execute opportunistically between waves or in an S83+ quality session.

---

## III. Execution Plan

### III.A. Wave dispatch rules

1. **W0-A** (2D-BZ s52 extension) runs FIRST as a single-agent compute.
   Blocks W0-1 phononic-length canonicalization. ~1 agent, ~30min compute.

2. **Wave 1** dispatches in parallel (5 agents: W1-1 through W1-5; W1-3 and later
   have no mutual dependency). S80 plan §W1-1..W1-6 prompts remain verbatim.
   Top EVOI first: W1-1 (0.300) → W1-2 (0.211) → W1-3 (0.12) → W1-4 (0.074)
   → W1-5 (0.073).

3. **Decision point after Wave 1**: check W1-1 branch, W1-2 verdict, W1-3 theorem
   status. If all three land decisive, dispatch Wave 2. If any returns
   INCOMPUTABLE, pause and escalate — do not dispatch Wave 2 speculatively.

4. **Wave 2** (15 items) dispatches in two sub-batches of 8 + 7 (avoid >8
   concurrent agents per `feedback_dispatch-discipline.md`). W2-1 first
   (branch-conditional replay).

5. **Wave 3** (14 items) dispatches after Wave 2 completes. Two sub-batches.

6. **W0-1** (phononic-length canonicalization) runs opportunistically after
   W0-A unblocks it; typical window is alongside Wave 2.

### III.B. Estimated wall time

S80 plan budgeted ~12h single-threaded compute for all four waves. S82
inherits that budget minus W1-3 (done) and W0-15 (done). Revised estimate:
**~10-11h compute** plus ~2h orchestrator-local consolidation + extraction.

### III.C. Master gate checkpoint

After Wave 1 closes, re-run `s80_pru_audit.py` + `s80_pru_trendline.py`.
Expected delta from pre-S82 baseline (a=0, b=0, c=0):
- New S82 verdicts land in `s82_gate_verdicts.txt` with 64-char SHA pins,
  preserving c=0.
- New gate IDs extend the entity graph; extractor ingests automatically.
- Any new canonicals promoted during W2/W3 may temporarily spike (a) until
  the batch-tag + rename passes re-run.

---

## IV. Artifacts (Expected)

| Path | Produced By | Notes |
|:-----|:------------|:------|
| `sessions/archive/session-82/session-82-results-workingpaper.md` | team-lead | honest-close from S80 pattern |
| `computations/s82_gate_verdicts.txt` | per-agent | 34+ verdict lines, all SHA-pinned |
| `computations/s82_*.py` | Wave 2 / Wave 3 agents | per-item scripts |
| `computations/s82_*.npz` | same | per-item outputs |
| `sessions/archive/session-82/prep_S82-*.md` | per-agent (if script needs new prep block) | consolidated via `_consolidate_prep.py` |

---

## V. What S82 Does NOT Do

- Does not re-do S81 audit/retrofit work (PRU already at 0).
- Does not retroactively re-classify the 443 theorem 4-tuples (Q-1 deferred).
- Does not promote new canonicals unless a Wave 2/Wave 3 gate explicitly produces a reproducible framework constant. S81 promoted the S80-identified 6; further promotions must emerge from new physics, not from audit.
- Does not weaken the Master Gate threshold. If Wave 1 decisive fails, S82 closes without Wave 2/Wave 3 and carries forward the failure honestly.

---

## VI. Cross-Reference Index

- S80 full plan specifications: `sessions/session-plan/session-80-plan.md` (2264 lines; authoritative for all item-level gate definitions).
- S80 honest close: `sessions/archive/session-80/session-80-results-workingpaper.md §VI`.
- S81 handoff: `sessions/archive/session-81/session-81-results-workingpaper.md`.
- PRU trendline: `computations/s80_pru_trendline.jsonl` (session-persisting).
- PRU audit rule: `.claude/rules/epistemic-discipline.md §Pre-Registration Completeness`.
- Gate-verdict form: `.claude/rules/gate-verdicts.md` (S81-hardened 64-char mandate).
- Canonical constants: `computations/canonical_constants.py` (S81 promotions block at line 795-800).

---

S82_PLAN_COMPLETE 2026-04-17
