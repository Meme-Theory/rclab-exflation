# Session 117 — Workshop / Synthesis Schedule

**Date drafted**: 2026-06-29
**Scope**: Near-empty honest-count campaign. S117 was a hygiene + refinement-heavy session (30 gates / 10 waves: 14 compute PASS + 1 review PASS-AND, 3 FAIL, 12 INFO). Nine of ten waves reported `## No candidates`; one wave (W8) surfaced a single low-leverage Slot-1 solo-review candidate. ZERO Slot-2 workshops survive the discriminator.
**Rationale**: Per `Investigating-Workshops.md §"No workshops is a valid output"`, a session with clean PASSes, pre-registered branch-fires, and settled methodology produces few-to-zero workshops. Every S117 FAIL/INFO landed at a determinate, pre-registered branch (no FAIL admitting competing structural readings; the two-grade INFOs are designed outcomes). All cross-wave flags aggregated from the ten seeds are dependencies / coherences / disambiguations — **zero genuine cross-wave contradictions** — so none seeds a workshop. The one genuine candidate (W8 S1-1) is a first-principles counting-class determination the W8 plan deferred by inheriting the S116-W7 convention rather than deriving it.

**Source documents (authoritative; do not re-adjudicate)**:
- `sessions/session-117/workshops/_seed-w0.md` … `_seed-w9.md` (10 per-chunk investigation seeds; 1 Slot-1 candidate in `_seed-w8.md`, 0 Slot-2, `## Cross-wave flags` in every seed)
- `sessions/session-117/session-117-w8-workingpaper.md` (174 lines — the single scheduled entry's source)
- `computations/session-117/s117_gate_verdicts.txt` (165 lines — gate verdicts)
- `sessions/session-117/session-117-housekeeping.md` (105 lines — canonical Q2 ledger; every §A/§D entry is a structurally-non-workshop)
- `sessions/session-117/session-117-results-index.md` (31 lines — wave→theme map)

**All workshop + synthesis outputs land inside `sessions/session-117/`**. The next session plan (S118) is open; this campaign feeds it via the S1-1 structural verdict and the seven investigator-surfaced carry-forwards routed to the per-wave WP CF blocks (consumed by `/rclab-plan`).

---

## Dispatch Strategy

A one-entry campaign. The single Slot-1 solo review (`/rclab-review`) launches alone. There are no Slot-2 workshops (no cross-rebuttal-requiring ledger-dissonance survived the discriminator) and no Slot-3 closeout (no combined-landscape view to synthesize across a single low-leverage solo).

| Slot | ID | Title | Skill | Agents | Rounds | Depends on |
|:----:|:---|:------|:------|:-------|:------:|:-----------|
| 1 | S-1 | R_summand counting-class determination (§VII.AJ.STATE-PROJ sign) | `/rclab-review` | 1 (`landau-condensed-matter-theorist`) | — | — |
| 2 | — | (no workshops — zero cross-wave contradictions; see note) | — | — | — | — |
| 3 | — | (no closeout — single low-leverage solo; nothing to combine) | — | — | — | — |

---

## Slot 1 — Independent Solo Syntheses (`/rclab-review`)

### S-1 — Is the §VII.AJ.STATE-PROJ `R_summand` sign substrate-forced (intensive vs extensive counting-class), or a permanent convention-dependent d.o.f.?

**Why**: W8 gate `CF-S117-STATEPROJ-INTER-SUMMAND` (PASS) discharged the §VII.AJ.STATE-PROJ slot to substrate-first with a datum `R_summand=+0.955038` whose registered SIGN is **counting-axis-determined** — intensive `RATIO-NORMALIZED-TRACE-MEAN` gives **+0.9550** (per-mode: the color-singlet electroweak edge wins) but flips to **−0.9917** under extensive `RATIO-BLOCKSUM` (the color tower wins by mode count). The G1 vanishing test that *discharges* the slot passes on BOTH axes; only the sign flips. The W8 plan pinned intensive by **inheritance** ("to match the S116-W7 `bcs_condensation_energy` functional"), NOT by a first-principles application of the counting-axis discriminator (`regulator-pin-discipline.md §"Counting (intensive/extensive)"`: mass/position-class → intensive `ρ_g`; width/degeneracy/occupation/action-moment-class → extensive `n_g·ρ_g`). A BCS *condensation-energy*-derived functional is arguably action-moment-class (→ extensive → −0.992), yet was registered intensive (+0.955). This is a genuine **Q1b** first-principles classification (a derivation against a pre-registered taxonomy, not a status-tag edit), but **solo not workshop**: the two candidate readings (DOS-density-intensive vs condensation-energy-action-moment-extensive) are INPUTS to the class-determination, not two positions that must rebut each other to converge — a single counting-axis-fluent agent applies the discriminator and reports the class. **Stated up front: LOW leverage** — the §VII.AJ.STATE-PROJ discharge is sign-INDEPENDENT and STANDS in all three outcomes; only the registered datum's sign annotation (and, under outcome B, a one-line mack sign-fix) is at stake.

**Agents**: `landau-condensed-matter-theorist` (1 agent — primary author of W8-1, owner of the BdG condensation-energy functional whose counting-class is in question).
*Default 1 agent per S88 calibration. Natural alternative if the spectral-functional-class angle is preferred: `lizzi-spectral-functional-theorist` (counting-class / K₀-rank / scheme-dependence-as-physical-d.o.f. domain). Not bumped to 2 — LOW leverage; the class-determination is single-agent-decidable.*

**Invocation** (NO `--type`, NO `--rounds` — `/rclab-review` is solo-only):
```
/rclab-review sessions/session-117/session-117-w8-workingpaper.md computations/session-117/s117_gate_verdicts.txt --agents landau-condensed-matter-theorist --session 117 --context "Adjudicate the counting-class of the §VII.AJ.STATE-PROJ substrate-first datum R_summand (Q33, Wave 8). CONTEXT: gate CF-S117-STATEPROJ-INTER-SUMMAND (verdict s117_gate_verdicts.txt L152, PASS) registered R_summand=(a_H-b_M3)/(a_H+b_M3)=+0.955038 at L_max=12 (+0.968531 at L14, drift 1.41%), convention=RATIO-NORMALIZED-TRACE-MEAN (intensive, per-mode). The companion row L158 records the load-bearing fact: the SIGN is counting-axis-determined. Intensive RATIO-NORMALIZED-TRACE-MEAN gives R=+0.9550>0 (per-mode: the color-singlet C+H edge, N=16, per-mode density a_H=6.60e-3, beats the M3 color tower, N=166,880, per-mode b_M3=1.52e-4, by ~43x => R≈(43-1)/(43+1)); extensive RATIO-BLOCKSUM gives R=-0.9917<0 (total block-sum: the color tower wins by sheer mode count 166,880>>16). The G1 vanishing test |R|>=1e-3 that DISCHARGES the slot's REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION credential passes on BOTH axes; only the SIGN flips. THE GAP: the plan pinned intensive by INHERITANCE ('to match the S116-W7 bcs_condensation_energy functional', which used rho_g=P_g/Tr(P_g)), NOT by a first-principles application of the counting-axis discriminator at regulator-pin-discipline.md section 'Counting (intensive/extensive)' (the 4-axis-orthogonality row). That discriminator classifies observables as mass/position-class -> intensive rho_g vs width/degeneracy/occupation/action-moment-class -> extensive n_g*rho_g (n_g = K0-rank factor, topological). A BCS condensation-ENERGY-derived state-pair functional is arguably action-moment-class (-> extensive -> -0.992), yet was registered intensive (+0.955). TASK: apply the counting-axis discriminator FROM FIRST PRINCIPLES to the BdG condensation-energy R_summand functional and return ONE of three structural verdicts: (A) intensive substrate-FORCED (DOS-density/normalized-ratio class => +0.955 canonical, plan-pin vindicated, no registry change); (B) extensive substrate-FORCED (action-moment class => the registered sign corrects to -0.992 -- specify the exact mack VII.AJ.STATE-PROJ sign-annotation recommendation, mack sole-writer per feedback_mack-bridge-role.md, since this solo cannot edit the VII surface); or (C) genuinely dual-class => the sign is a PERMANENT convention-dependent physical d.o.f. (a lizzi-signature scheme-dependence parallel to the a_0/a_2 CC-ratio; both signs registered). STAKES (state up front, LOW leverage): the VII.AJ.STATE-PROJ DISCHARGE to substrate-first is sign-INDEPENDENT (the vanishing test passes on both axes) and STANDS in all three outcomes -- only the registered datum's SIGN annotation (and, under B, a one-line mack sign-fix) is at stake. SOURCE ANCHORS: verdict L152/L154 (PASS, sign_verdict=PASS DIAGNOSTIC)/L155-158 (composite-precedence + counting-axis rows); WP section W8-1 'Counting-axis is LOAD-BEARING for the sign' + the per-summand intensive-evaluations table; housekeeping section D counting-axis calibration instance (SUGGESTION K=1); regulator-pin-discipline.md section 'Counting (intensive/extensive)' row (mass/position rho_g vs action-moment n_g*rho_g discriminator); registered slot sessions/permanent-results-registry.md VII.AJ.STATE-PROJ (mack section A7, discharged substrate-first +0.955). DELIVERABLES: (1) the A/B/C structural verdict with the first-principles substitution chain (state the definition of the condensation-energy functional, write whether it is a per-mode intensive density or a block-extensive moment, read off the class); (2) record the determination as a section-D counting-axis calibration-corpus strengthening recommendation -- the durable output regardless of A/B/C, since the section-D housekeeping entry recorded only THAT the sign is convention-determined, not WHICH class is substrate-forced; (3) under outcome B, the precise mack VII.AJ.STATE-PROJ sign-annotation patch text. CARRY-FORWARD MANDATE: any residual MATH compute the determination surfaces must be a 4-field structured carry-forward (what/inputs/gate/effort) per feedback_fix-in-session-never-defer.md; a NON-MATH registry recommendation (the mack sign-fix under B, or the section-D corpus strengthening) must be specified precisely for S118 plan-freeze. Do NOT iterate toward a preferred sign -- A, B, and C are all valid structural results; the verdict is the class-determination, whatever it is. Frame everything substrate-first (phononic-framing.md): R_summand IS the inter-summand BdG edge-condensation-density asymmetry of the substrate, not a measurement IN a container."
```

---

## Slot 2 — Workshops (`/rclab-workshop`)

**No workshops.** Zero Slot-2 candidates survived the discriminator. Honest reasons:

- **No FAIL admitted multiple structural readings.** All three S117 FAILs (1-1 composite, 1-4 greybody, 2-3 seesaw-resonance) are determinate pre-registered branch-fires that the gate and the wave synthesis read identically.
- **The two genuine-looking cross-wave "structural-reading questions" are coherences, not contradictions.** (i) The W6↔W1 flag (is L_emp's a₀-grade UV-regulator SD-OPEN the SAME no-go as A_s functional-pluralism?) resolves via the existing 4-axis orthogonality machinery (`regulator-pin-discipline.md`): UV-regulator-selection ⊥ functional-selection are DISTINCT axes; W6-2 already established the SD-OPEN is structurally real/permanent. Both claims hold simultaneously → not a contradiction; the residual is a low-leverage Q2 cohort-note (routed to the W6 WP CF). (ii) The W6/W7-1 {APS,CS,BC} flag (secondary-class FORCED in W6 vs scheme-blind Δ_scheme=0 in W7-1) is expected behavior on two structurally different observables (nonzero-secondary-class state-pair functional vs degree-0 scheme-blind morphism by Wodzicki uniqueness) → coherent framework-wide, no adjudication.
- **The honest-count discipline + the housekeeping consumption pointer agree.** `session-117-housekeeping.md` line 99 names W1/W2/W6 as the candidate-*bearing* waves but routes the highest-leverage open frontier (Q23 A_s plurality) to the W1 physics CF, "not a workshop." No workshop seed survives.

---

## Slot 3 — Closeout (`/rclab-review`)

**No closeout.** Slot 3 is a combined-landscape synthesis that depends on Slot-1/Slot-2 outputs. With one low-leverage Slot-1 solo and zero workshops, there is no multi-thread landscape to synthesize — a Slot-3 entry would be padding (`feedback_max-effort-full-fidelity.md`: length is not quality). The S1-1 solo's own synthesis report IS the deliverable; it feeds S118 directly.

---

## Post-Campaign Deliverable Summary

| File | Produced by | Feeds into next session as |
|:-----|:------------|:----------------------------|
| `sessions/session-117/session-117-landau-synthesis.md` (skill-default solo path) | S-1 solo (`landau-condensed-matter-theorist`) | The R_summand counting-class structural verdict (A/B/C). Feeds the §VII.AJ.STATE-PROJ sign-annotation decision (mack, under outcome B) + the §D counting-axis calibration-corpus strengthening (which counting-class is substrate-forced — the §D ledger recorded only THAT it is convention-determined). |

**Total expected outputs**: 0 workshop MDs + 1 per-agent solo MD = **1 file**.

The campaign's other forward content is the seven investigator-surfaced carry-forwards routed to the per-wave WP `## Carry-Forward Computations` blocks (NOT this schedule), consumed by `/rclab-plan` at S118:

| WP CF | Wave | Class | One-line |
|:------|:-----|:------|:---------|
| `CF-W0-1` | W0 | Q2 registry-hygiene | α_s-family scale-channel label-consistency check (Row #3 "pivot-local" vs W9 "CMB-pivot"; mack) |
| `CF-W1-1` | W1 | Q-other compute | ALT-GREYBODY structural-wall upgrade (4th knob-free class OR knob-free-impossibility no-go) |
| `CF-W1-2` | W1 | Q2 registry-hygiene | §EVOI.BF A_s-liability freshness-fold (prose stale through S114 despite S117 marker) |
| `CF-W2-1` | W2 | Q-other compute | Joint (R, PMNS-angle) admissibility scan over the FREE U_eL/ε_LX texture family |
| `CF-W2-2` | W2 | Q2 registry-hygiene | §VII.CK D4 scope-token hygiene ("t(O)=±1" coset-shift scope inside the token) |
| `CF-W4-1` | W4 | Q2 gate-finalization | Row #79 "discharge owed" reconciliation + EVOI "170× DM-mass" §5-fold |
| `CF-W6-1` | W6 | Q2 EVOI cohort-note | L_emp a₀-grade UV-regulator SD as a §EVOI.BF lizzi-d.o.f.-cohort sibling (axis-distinct) |

---

## Planning Input Checklist (populated by this campaign)

Items this campaign produces that the S118 planner needs:

- **R_summand counting-class structural verdict (A/B/C)** from S-1 — the only schedule deliverable. Under A: plan-pin vindicated, no action. Under B: a mack §VII.AJ.STATE-PROJ sign-annotation fix (+0.955 → −0.992). Under C: register the sign as a permanent convention-dependent d.o.f. (a third §EVOI.BF lizzi-signature cohort member alongside A_s and the a_0/a_2-CC ratio).
- **A §D counting-axis calibration-corpus strengthening** (the first-principles class-determination, regardless of A/B/C) → `regulator-pin-discipline.md §"Counting axis"` corpus.
- **Seven WP-CF carry-forwards** (above) — two genuine forward computes (`CF-W1-1` greybody-wall upgrade; `CF-W2-1` joint-admissibility scan) and five registry-hygiene/EVOI folds — consumed by `/rclab-plan` from the per-wave WP `## Carry-Forward Computations` blocks.
- **No EVOI Tier-1–4 insertion** — every flag/CF refines an already-tracked position (§EVOI.BF A_s/w0/DM cohort, the algebra-axis K-counter corpus, atlas-08 Q-status freshness); none is a new high-leverage frontier absent from §1–§4 by oversight.

---

## Operational Notes

- **Session ID pinning**: the S-1 invocation uses `--session 117` explicitly.
- **Output path**: the S-1 solo uses the skill-default `sessions/session-117/session-117-{short-name}-synthesis.md`.
- **Dispatch count**: Slot 1 = 1 agent (single dispatch). Slot 2 = 0. Slot 3 = 0.
- **Concurrency cap**: trivially satisfied (1 dispatch ≪ 8).
- **Length targets**: none in the S-1 context — content requirements only.
- **Carry-forward mandate (math-only)**: the S-1 context carries the 4-field carry-forward mandate (what/inputs/gate/effort) per `feedback_fix-in-session-never-defer.md`; a non-math registry recommendation (the mack sign-fix under B; the §D corpus strengthening) is specified precisely for S118 plan-freeze rather than effected by the solo (the solo cannot dispatch mack; `/rclab-review` has no team / no designated final writer).
- **Honest count**: 1 Slot-1 solo, 0 workshops, 0 closeout. A near-empty schedule is the correct, non-padded outcome for a hygiene + refinement-heavy session whose cross-wave flags are all coherences/dependencies — `Investigating-Workshops.md §"Honest count discipline"`.

---

*End of S117 workshop schedule. Draft 2026-06-29.*
