# Atlas-08 Open Questions Refresh — Materials Packet (S52-S88)

**Producer**: workhorse-gen-physicist
**Target atlas**: `sessions/framework/Atlas/atlas-08-open-questions.md` (16,283 bytes; mtime 2026-05-03; entry-date 2026-04-04; "Updated Through S62" per atlas line 1)
**Scope**: Revise the 44-item list (6 decisive / 14 structural / 4 observational / 20 carry-forward) against S52-S88 closures and surface the new questions that emerged in that window.
**Frame discipline**: Open questions are **constraint-map holes** — regions of solution space neither closed nor confirmed. NEVER framed as "weaknesses" or "problems"; framed as "constraint-surface holes that the next round of computation maps." Per `epistemic-discipline.md` §"How to Assess a Mechanism", the three categories are well-motivated / untested / closed; an open question is the "untested" classification with an explicit pre-registered gate that decides it.
**Date compiled**: 2026-05-09

---

## Section 1 — What's currently in atlas-08

The existing atlas-08 contains **44 numbered open questions** organized into four sections:

- **Section I — Decisive Questions** (Q1-Q6, six items): one computation answers each. Format is per-question prose blocks with explicit `What decides it / If YES / If NO / Estimated effort / Threshold / Source / Priority` fields. Q1 (EFOLD-MAPPING-52) is flagged HIGHEST priority as "the single question to which 51 sessions reduce." Q2 (N-PAIR-FULL) and Q6 (V-TAU-SWEEP) carry explicit "DEPRIORITIZED by S62" annotations.
- **Section II — Structural Questions** (Q7-Q18b, fourteen items): new mathematics required. Per-question prose blocks with `Status / What is needed / Source / Priority` fields. Q18a (alpha_GUT tension) and Q18b (Yukawa hierarchy beyond rank-1) are explicit S62 "NEW" entries.
- **Section III — Observational Questions** (Q19-Q22, four items): external data required. Per-question prose blocks with `What it tests / Framework implication / Source` fields. Items: DESI DR3, CMB-S4 alpha_s, lensing sigma_8, ALPHA-ENV-43.
- **Section IV — Carry-Forward Items** (CF1-CF20, twenty items + 2 S46 corrections): "not yet promoted to questions." Format is **6 sub-tables** (Levels 2/3/4/5/6 + a final "S46 Corrections Still Not Propagated" 2-row table). Each row is `# | Item | Source | Description` (4-column markdown).

The atlas closes with a one-line provenance footer naming the source documents (collective-analysis, atlas-04, atlas-05, S47/S49 wayforward, MEMORY.md). The whole document is anchored at S62 (per the title line "Updated Through S62"); items added later as Q18a/Q18b are explicit "NEW, S62" amendments inside Section II. The post-S62 era (S63-S88) is **entirely absent** from the question registry — that is the gap this packet fills.

The 4-class taxonomy (decisive / structural / observational / carry-forward) is internally honest but incomplete relative to the post-S82 methodology-floor expansion: questions like FUNCTIONAL-SELECT-67 (which spectral functional generates n_s?) span the structural and methodology layers and do not fit cleanly into any one of the existing four classes. See §"Flag #4" below.

---

## Section 2 — What to revise

### 2a. Questions to CLOSE (answered post-S51)

Each row below identifies an existing atlas-08 question whose pre-registered decision criterion has been satisfied (PASS, FAIL, or structural reframe) by an S52-S88 result. The "closing event" column states the verdict; the "constraint-map status" column states which region of solution space is now closed/confirmed/reframed.

| atlas-08 Q | original phrasing | closing event | session | constraint-map status | source registry |
|:-----------|:------------------|:--------------|:--------|:----------------------|:----------------|
| **Q1** EFOLD-MAPPING-52 | Does exflation produce ≥ 3.1 e-folds? | **FAIL (structural)** N_e = 0.1734 IC-independent; reframed as TRANSIT-PS-67 (transit power spectrum) per S67 / S73B / S77 reframe | S52 (FAIL landed) → S67 (reframe) → S73B (FAIL 125σ) → S77 (A_s gap inversion to overproduction) | **CLOSE-WITH-REFRAME**: the e-fold path-1 question is structurally closed (N_e = 0.1734 ceiling); the post-fold cosmological signature now routes through transit power spectrum + acoustic transfer (Window-9 in atlas-05). Replace Q1 with the corresponding TRANSIT-PS-67 entry as new decisive question. | `constraint-mega-matrix.md`; `session-52-way-forward.md` (theorem proven N_e = 0.1734); atlas-05-materials Window-9 entry; `summary/session-67-final.md`; `session-73b-transit-synthesis.md` |
| **Q2** N-PAIR-FULL | Physical pair number from full spectrum | DEPRIORITIZED by S62 q-theory closure (already noted in atlas); REMAINING-RELEVANCE for f_DM bracket SUPERSEDED by LEGGETT-MOMENT-70 (0.6% Planck match closing the DM bracket directly) | S62 W4-01 (CC-QTHEORY-GGE closure) → S70 LEGGETT-MOMENT (DM channel locked at 0.6%) | **CLOSE-DEPRIORITIZED-AND-SUPERSEDED**: Q2's CC-decisive role closed by S62; remaining DM-relevance role superseded by S70. The full-spectrum BCS ED is no longer decisive for any registered observational anchor. | `permanent-results-registry.md` C-Q row; knowledge-MCP `LEGGETT-MOMENT-70` PASS edge |
| **Q6** V-TAU-SWEEP | V_{kk'}(τ) sweep for Δ_B3 > 0.13 | DEPRIORITIZED by S62 q-theory closure (already noted in atlas); REMAINING-RELEVANCE for BCS condensate strength now anchored by S86 W-3 §VII.AC.2 B1/B2 block-decomposition uniqueness theorem and S87 W4-1 CF-25 9-cell tensor | S62 W4-01 → S86 W-3 → S87 W4-1 | **CLOSE-DEPRIORITIZED-AND-REANCHORED**: structural question's BCS-strength role replaced by registered §VII.AC.2 + §VII.X.W4-1 entries. | `permanent-results-registry.md` §VII.AC.2 + §VII.X.W4-1 |
| **Q14** WILSON-LOOP / Non-Abelian Berry phase for 492 degenerate multiplets | Wilson loop holonomy on degenerate eigenvectors; π-count predicted in [13, 50]; may connect to SM count 16 | **STRUCTURAL CLOSURE via §VII.W parity-grading orthogonality + W17 bare-eigenvalue parity-blindness wall**: even-grading regulator-weighted Mellin moments (η-invariant alone) cannot decode odd-grading HP^1 content; the 16-mode SM-channel projection is now anchored at §VII.X (16/136480 modes couple to 4D, A-tensor decomposition; theorem A7 atlas-07 line 27, S62) | S62 (Berry-NCG-KK Triple Identification A7) → S85 W2-7 (parity-blindness theorem Bulletin #2) → S86 W-11 ((η=0, GV≠0) signature) | **CLOSE-WITH-STRUCTURAL-REPLACEMENT**: the Wilson-loop holonomy question is replaced by the substrate-IS HP^1 ↔ HP^0 grading orthogonality + 16-mode A-tensor anchor. Q14's specific computation is no longer the decisive instrument; the substrate result it would have probed is settled. | `atlas-07-permanent-results.md §A7`; `permanent-results-registry.md §VII.W` (line 15003); `regulator-pin-discipline.md` Class-(c) extension |
| **Q15** Self-consistent HFB gap equation on SU(3) (sector-resolved) | Full HFB iteration with sector-resolved Δ_{(p,q)} at fold; mean-field 60% overestimate per S46 | PARTIALLY ANSWERED: S62 BCS sigma stabilization (D_s(GGE)/D_s(fold) = 0.9885; Door-S62-Meissner per atlas-05) closes the BCS-condensate-stability sub-question; sector-resolved Δ_{(p,q)} self-consistency remains computational | S62 W2-02 | **PARTIAL-CLOSE**: convert to a NARROWER STAGE-1-CANDIDATE — only the sector-resolved iteration remains open after the BCS-stability anchor is fixed. Recommend re-classify as STAGE-1-CANDIDATE pending sector-resolved Δ_{(p,q)} computation. | atlas-05-materials Door-S62-Meissner; `permanent-results-registry.md` §VII.AC.2 |
| **Q18** Z_3 domain wall energy and homotopy | Domain wall energy from GL parameters; U(1) × Z_3 order parameter | **STRUCTURAL ANCHOR via §VII.AG.4 + §VII.AG.5 Z_3 gauge-sector signature** (S86 W-6): 512 = (2/3) × 768 plaquette count; n_frust ∈ {0, 2}, NOT {0, 3}; gauge-counting correction landed | S86 W-6 (Z_3 substrate homotopy structurally pinned via cyclic-fold V_4 quotient + plaquette-counting correction) | **CLOSE-WITH-STRUCTURAL-REPLACEMENT**: the Z_3 substrate gauge structure is structurally fixed; the open computational sub-question (vortex support classification on T^2) survives but is no longer the decisive path — that role moves to LISA / CGWB Ω_GW window-12. | `permanent-results-registry.md §VII.AG.4 + §VII.AG.5`; atlas-05-materials Window-12 |

**CLOSE-COUNT**: **6 atlas-08 questions** are answered or structurally replaced post-S51. Of these:
- 2 (Q1, Q14) close with **structural reframe / replacement** (the question's substrate-IS content is settled; the original computational instrument is no longer the decisive path).
- 2 (Q2, Q6) close with **DEPRIORITIZED + SUPERSEDED**: the relevance role moved to a different registered anchor (LEGGETT-MOMENT-70 for Q2, §VII.AC.2 / §VII.X.W4-1 for Q6).
- 1 (Q15) closes **partially**: re-classify as a narrower STAGE-1-CANDIDATE.
- 1 (Q18) closes with **structural anchor** but a narrower computational sub-question survives.

**Items NOT closed** (verified explicit-OPEN status post-S51, retain in atlas-08):
- Q3 GOLDSTONE-MASS-FROM-DISORDER — the 170× Goldstone mass problem persists per `atlas-04-assumptions.md` P2 entry; no S52-S88 result resolves it.
- Q4 STRUTINSKY-DECOMPOSITION-AT-HIGH-PW — n_s(smooth) = -0.80 at current truncation (S51); higher PW truncation never executed.
- Q5 HIGH-PW-EIGENVALUES — gates Q4; never executed (weight-space algorithm bottleneck).
- Q7-Q13 — assumptions remain ASSUMED / BROKEN / UNTESTED per atlas-04 entries.
- Q16-Q17 — never executed.
- Q18a alpha_GUT tension — explicit OPEN (S62 NEW); two-loop test never performed.
- Q18b Yukawa hierarchy — explicit OPEN (S62 NEW); first-principles derivation never performed.
- Q19-Q22 (observational) — DESI DR3 binding pending 2027; CMB-S4 pending 2030; sigma_8 lensing convergence pending; ALPHA-ENV-43 queued since S43.
- All 20 carry-forwards (CF1-CF20) — none individually closed by S52-S88; the framework's growth has been on cross-pillar bridges and methodology floor, not on the S46/S47 wayforward backlog.

### 2b. New questions to ADD (S52-S88)

Each row below identifies a constraint-surface hole that opened post-S51 and remains unmapped at S88-close. Class follows the existing 4-class taxonomy (decisive / structural / observational / carry-forward); see §"Flag #4" for the case for adding a 5th class.

#### DECISIVE class (one computation answers it)

| question | session opened | current status | resolution path | falsifier protocol | source registry |
|:---------|:---------------|:---------------|:----------------|:-------------------|:----------------|
| **Q23 — TRANSIT-PS-67 / Stage-2 framework cosmology adjudication**: full Bogoliubov power spectrum through the τ-fold; resolves α_s, A_s normalization, n_s(k) simultaneously. Replaces Q1 EFOLD-MAPPING-52 as the highest-priority decisive question in the post-S51 era. | S67 (opened); S77 inverted A_s gap to OVERPRODUCTION; OPEN through S88 | OPEN (CRITICAL) | Coupled mode-equation through fold with substrate-physics F_amp; pre-registered PASS criterion `α_s(k_CMB) < 0.015`, FAIL > 0.019; A_s normalization within Planck band | `constraint-mega-matrix.md` UNCOMPUTED-CRITICAL #1; atlas-05-materials Window-9 | knowledge-MCP `TRANSIT-PS-67` OPEN; `falsifier-watchlist.md` α_s row |
| **Q24 — Stage-2 cross-pillar bridge verify (§VII.W-3.LAB STAGE-1-CANDIDATE)**: per `joint-theorem-promotion.md` 4-stage pathway, Stage-2 two-agent parallel cross-axis independent-verify is required before §VII.W-3.LAB promotes to STAGE-3-PERMANENT. Calibration-corpus instance #3 of cross-pillar-bridge-anatomy.md K=3 MANDATORY. | S88 W4a-17 (STAGE-1-CANDIDATE landing) | STAGE-1-CANDIDATE; Stage-2 NOT YET dispatched | Two-agent parallel dispatch: Axis-A spectral (connes/lizzi alternate per `joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol"` 3-condition discipline + downstream-inheritance reach test) + Axis-B substrate (volovik). Both reviewers operate WITHOUT prior workshop context. PASS iff BOTH PASS (logical AND, not OR) on all clauses including JOINT clauses. | `joint-theorem-promotion.md §"Stage 2"`; calibration corpus instance #3 | `permanent-results-registry.md` §VII.W-3.LAB (line 16693); atlas-07-materials line 75 |
| **Q25 — §VII.AM Universal Lock Condition Stage-2 verify**: per `joint-theorem-promotion.md` 4-stage pathway, the 3-clause joint theorem (pixelation lock + effacement lock + Page-time lock) at §VII.AM is STAGE-1-CANDIDATE; calibration corpus instance #2 after §VII.AH. Stage-2 cross-axis verify pending S89+. | S88 W1b2-65 (STAGE-1-CANDIDATE landing; orchestrator-direct write) | STAGE-1-CANDIDATE; Stage-2 NOT YET dispatched; FLAGGED at atlas-09 §2E as candidate for retraction-route if Stage-2 surfaces clause-level FAIL | Two-agent parallel dispatch on the 3 clauses; reviewers must NOT include hawking-theorist (original author) or downstream-inherited successor agents per axis-B selection protocol downstream-inheritance reach test. | `joint-theorem-promotion.md §"Stage 2"`; atlas-09-materials §2E entry | `permanent-results-registry.md §VII.AM` (line 16367); atlas-09-materials §2E |
| **Q26 — §VII.AH Joint F_2-Class Path-(c) Theorem Stage-2 verify**: 6-clause joint theorem with 4 corrigenda; clauses (c) + (d) JOINT. STAGE-1-CANDIDATE since S87 W9a-1; calibration corpus instance #1 of joint-theorem-promotion 4-stage pathway. | S86 W-9 (Stage-0); S87 W9a-1 (Stage-1-CANDIDATE landing) | STAGE-1-CANDIDATE; Stage-2 queued as `S88-OR-LATER-EXTENDED-THEOREM-INDEPENDENT-VERIFY` (CF-6, ~1.0 wave-equivalents) | Cross-reviewers: connes-ncg-theorist (spectral-side audits clauses (a) + (c) JOINT + (d) JOINT + (e)) + volovik-superfluid-universe-theorist (transit-side audits clauses (b) + (c) JOINT + (d) JOINT + (f)) per `joint-theorem-promotion.md §"Calibration corpus"` instance #1. Volovik selected per agent-memory feedback "framework's SHARPEST reviewer." | `joint-theorem-promotion.md §"Stage 2"` | `permanent-results-registry.md §VII.AH` (line 15522) |
| **Q27 — H_0 spinor-factor structural resolution** (LIVE-PENDING): framework prediction H_0 = 65.4 km/s/Mpc CONTINGENT on resolution of the spinor normalization factor (M_Pl,eff / M_Pl,unred = 3.92 ≈ √16); structural unresolved through S85. | S58 W3-16 (opened); LIVE-PENDING through S85 / S88 | LIVE-PENDING | First-principles KK-derivation of the spinor normalization factor from substrate's d_spec = 8 spectral triple. Promotes to FLAGSHIP on resolution. | `falsifier-watchlist.md` H_0 row; atlas-05-materials Window-19 | `falsifier-watchlist.md:160-169` |

#### STRUCTURAL class (new mathematics required)

| question | session opened | current status | resolution path | falsifier protocol | source registry |
|:---------|:---------------|:---------------|:----------------|:-------------------|:----------------|
| **Q28 — FUNCTIONAL-SELECT-67 finalization across post-W12-145/146/148 two-layer reading**: while S67 W1-C closed the anomaly family with a structural theorem (n_s > 1 for all φ > 0) and W3-A JOINT-FALSIFICATION-67 PASS isolated the Chamseddine-Connes sqrt(x) cutoff as the unique surviving spectral functional, S88 W12-145/146/148 surfaced the **two-layer reading discipline** (Layer 1 pole-universal F_2-class anti-correlation + Layer 2 pole-compressing cross-regulator atlas spread). Open question: does the Chamseddine-Connes selection survive the Layer-2 atlas-cardinality-aware sub-test under canonical_constants.py atlas A_5 → A_6 extensions? Status PARTIAL: archive-harvested edges show FAIL verdict in S67 table on the original FUNCTIONAL-SELECT-67 gate, while the BAYESIAN-FUNCTIONAL-67 follow-up edge shows PASS (posterior n_s within 2σ AND Ω_DM within 10%); evoi-framework still lists OPEN for the umbrella question. The post-W12 sharpening reopens the closed sub-question at the new Layer-2 atlas-cardinality axis. | S66 (opened); S67 (partial-PASS via Chamseddine-Connes selection); S88 W12-145/146/148 (Layer-2 reading reopens at atlas-cardinality axis) | OPEN (sub-question reopened by S88 atlas-cardinality K-counter Layer-2 reading) | Atlas-cardinality scan A_5 → A_6 with Spearman rank-invariance under monotone-increasing CAC anchoring; verify Layer-2 cross-regulator atlas spread compresses or expands under the extended atlas. | Pre-registered PASS criterion: cross-regulator atlas spread at Chamseddine-Connes survives ≤ 0.30 at all surveyed substrate-distance poles s ∈ {3, 4, 5, 6}; FAIL if any pole shows ≥ 1.0× pre-S85 spread. | `epistemic-discipline.md §"Resolution-Specificity Scoping sub-clause"` calibration corpus K=5; `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY-K=3 |
| **Q29 — BBN-VOLOVIK-67 structural sharpening across cross-channel xcorr**: while S72 audit landed BBN-VOLOVIK-67 PASS at \|w_vac − 1/3\| = 3.39e-41 with G_eff/G = 1.5 (marginal but inside BBN bounds), the cross-channel test against `falsifier-watchlist.md` 5-channel detector roster + post-W4-2 cross-channel-correlation-matrix has not been executed under the unified-schema (8-column) form. Status PARTIAL: gate is PASS but the unified-schema cross-channel xcorr is OPEN. | S66 (opened); S72 PASS at marginal G_eff/G = 1.5; S85 W4 (unified-schema introduced; xcorr not yet executed for BBN row) | OPEN (cross-channel xcorr extension) | Run `falsifier-watchlist.md` 8-column unified schema cross-product across BBN row × CMB-S4 / DESI-DR3 / LiteBIRD / CMB-HD / 21-cm; verify ρ_xcorr matrix elements consistent with BBN-PASS posterior. | PASS criterion: BBN posterior within 3σ of Planck-2026 at all 5 cross-channel pairings; FAIL if any pair shows ≥ 5σ excursion. | `falsifier-watchlist.md`; `sessions/framework/correspondence/cross-channel-correlation-matrix.md` |
| **Q30 — Cross-pillar bridge corpus extension (FWD-C1 / FWD-C2 / FWD-C3 forward calibration)**: per `cross-pillar-bridge-anatomy.md §"Three forward bridge candidates for S88+ dispatch"`, FWD-C1 (Pillar I ↔ Pillar II; n_s spectral-action ↔ Planck CMB), FWD-C2 (Pillar II ↔ Pillar V; Mellin-Barnes residue ↔ BdG spectral triple), FWD-C3 (Pillar IV ↔ Pillar V; substrate cocycle norms ↔ 3He-B / 3He-A laboratory observables) are pre-registered for S88+ dispatch. FWD-C3 instance #3 LANDED at §VII.W-3.LAB (advancing K=2 → K=3 MANDATORY); FWD-C1 + FWD-C2 not yet dispatched. | S88 W4a-17 (K=3 MANDATORY promoted); FWD-C1 + FWD-C2 NEVER DISPATCHED | OPEN | Per-candidate full-fidelity dispatch (5-anatomy + 3-level ladder declaration + Hybrid Independence Test verification). | PASS criterion per `cross-pillar-bridge-anatomy.md §"Registry-PASS criterion"`: Level-3 < Level-2 envelope at canonical L_max; Level-3 deferred is permitted (STAGE-1-CANDIDATE). | `cross-pillar-bridge-anatomy.md §"Three forward bridge candidates"`; `sessions/framework/registry/cross-pillar-bridge-corpus.md §4` |
| **Q31 — Per-Bulletin-per-pole Level-1 wall classification pole-distinct extension**: SUGGESTION at K=3 (mixed-status); status promotes to MANDATORY-at-cohomology-class-distinct-K=3 for S89+ Pillar-VII Bulletin-class entries SHARING substrate-distance pole with existing corpus instances; remains SUGGESTION-pending-pole-distinct-K=3 for S89+ entries at NEW substrate-distance poles s ∈ {5, 6, 7, ...}. The §W10-120 DORMANT shell is queued to surface the pole-distinct third instance when activated. | S88 W10-119 (sub-section landing) | DORMANT (queued for §W10-120 activation) | When §W10-120 activates, register a Pillar-VII Bulletin-class entry at substrate-distance pole s ∈ {5, 6, 7, ...} with full Level-1/2/3 ladder declaration. | PASS criterion per the per-pole sub-section + at-plan-freeze items 5-8: substrate-distance pole index declared; Level-1 classification (regulator-invariance + structural identity); Level-2 envelope cites pole-specific α(s) + Casimir/Friedrich-Bär saturation argument; Level-3 anchor at L_max=10 OR analytic limit. | `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` |
| **Q32 — D3 audit knowledge.db round-trip gap**: ~37 of 66 §VII slots in `permanent-results-registry.md` are missing from `tools/knowledge.db` per atlas-07-materials Section 2 round-trip audit (PARTIAL or NO hit on most non-headline slots). Methodology / structural defect: `/weave --update` + `tools/extract_entities.py` entity-extractor refinement needed to lift §VII slot family into FTS5-indexed knowledge graph. | S88 atlas-07 packet audit (2026-05-09); atlas-07-materials Section 2 status legend | OPEN | Refine `extract_entities.py` to detect §VII slot card patterns + ingest into theorem-table; rerun `/weave --update --db-sync`; re-audit round-trip. | PASS criterion: round-trip hit rate on §VII slot family ≥ 95% (currently ~50%); MANDATORY at K=3 calibration via methodology floor. | atlas-07-materials Section 2 (60 §VII slots tabulated; ~37 NO/PARTIAL); `tools/knowledge.db` |
| **Q33 — §VII.AJ.STATE-PROJ BCS-physics-grounded substrate derivation**: the STATE-PROJ companion slot at §VII.AJ.STATE-PROJ is OPEN (NEEDS-COMPUTATION); BCS-physics-grounded substrate-IS image of R_3HeB_lit = +0.03536 at polycritical-pressure point P_pc = 21.22 bar; algebraic shape (a−b)/(a+b) restored vs W11-5 (c−2d)/d mismatch. Queued S89 ~3 wave-equivalents (BCS gap-equation kernel + spectral-action moment construction on A_K^BdG_preimage = ℂ ⊕ ℍ). | S88 W7 + W10 (slot allocated); S89 derivation queued | OPEN (NEEDS-COMPUTATION) | landau (PRIMARY) + volovik (CO-AUTHOR) + connes (CO-AUTHOR) per Stage-2 dispatch protocol; substrate-side BCS gap-equation closed-form derivation on the BdG sub-algebra. | PASS criterion: per `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole"` Level-1/2/3 ladder; STATE-PROJ derivation matches OP-PROJ companion at Hybrid-Independence-Test (i ∨ ii ∨ iii) ∧ iv. | `permanent-results-registry.md §VII.AJ.STATE-PROJ` (line 16320) |
| **Q34 — W11 Volovik CC Tracking promotion gap (§VII.AT slot allocation)**: W11 Volovik CC Tracking Wall (DILUTION-CC-66) is currently anchored at `framework-cc-oom.md` (Door 12 in atlas-05) and `falsifier-watchlist.md` but lacks dedicated §VII slot in `permanent-results-registry.md`. Atlas-05-materials Section 2c flag: recommend §VII.AT allocation in S89+ housekeeping (next free letter post-§VII.AS Geometric-Resummation Closure at S88 W18 W6a-51). | S66 (DILUTION-CC-66 PASS, no §VII slot); flagged S88 atlas-05 packet | OPEN (registry-state housekeeping) | mack-cosmic-bridge sole-writer (per `feedback_mack-bridge-role.md`) lands new §VII.AT entry citing the Gibbs-Duhem theorem + functional-independence statement. METHODOLOGY-class wave per `wave-classification.md` M1∧M2∧M3∧M4 conjunction. | PASS criterion: §VII.AT slot landed with full 5-anatomy + 3-level structural-confidence ladder declaration (or substrate-only entry with explicit no-cross-pillar-bridge tag); audit-SHA registered. | atlas-05-materials Section "Promotion-gap walls"; `permanent-results-registry.md` §VII.AS (last allocated) |
| **Q35 — S52-S60 atlas-01 timeline backfill**: pre-existing structural gap in `atlas-01-session-timeline.md` between S47-S51 and S61-S62 (S52, S53, S54, S55, S56, S57, S58, S59, S60 absent from per-session rows). Atlas-01-materials Section 4 Recommendation #2: orchestrator dispatches separate atlas-01 backfill task for S52-S60. | (pre-existing, atlas-01 mtime 2026-05-08) | OPEN | Read S52-S60 synthesis files (knowledge-MCP `sessions` table shows entries for S52, S53, S55, S57, S58, S59, S60; S54, S56 also exist) and add per-session 2-4 line rows. | PASS criterion: 9 new rows in atlas-01 spanning S52-S60; chronological integrity preserved per `session-handoffs.md`. | atlas-01-materials Section 4 #2 |
| **Q36 — D_K Block-Diagonality + Recursive-Casimir-Projection sector-distinct extension**: while S87 W11-2 + W11-3 closed the bot-20 D_K(τ_fold) cardinality vector via Casimir-bound + Friedrich-Bär saturation theorems for sectors p+q ≤ 12, sector-distinct calibration at p+q ∈ {13, 14, 15} would extend the saturation theorem corpus; per `math-scripts.md §"D_K Block-Diagonality Pre-Check"` calibration corpus K=2 (Casimir-bound W11-2 + Friedrich-Bär W11-3); a third sector-distinct instance at p+q ≥ 13 would advance K=2 → K=3. | S87 W11-2 + W11-3 (K=2 calibration); K=3 not yet reached | OPEN (corpus extension) | Recursive Casimir-projection at p+q ≥ 13 (irrep construction empirically infeasible per W11-3 timeout > 10 min); analytic Friedrich-Bär lower bound extension; verify NEW-sector intrusion margins remain below stratum-4 ceiling. | PASS criterion: η_FB_lower bound preserved at p+q ≥ 13 within 8% safety margin; bottom-20 cardinality vector remains (2, 4, 8, 6) at canonical L_max. | `math-scripts.md §"D_K Block-Diagonality Pre-Check"` calibration corpus |

#### OBSERVATIONAL class (external data required)

| question | session opened | current status | resolution path | falsifier protocol | source registry |
|:---------|:---------------|:---------------|:----------------|:-------------------|:----------------|
| **Q37 — Window-14 DESI DR3 binding-event-pending**: DESI DR3 is the binding instrument for the R_842 falsifier rectangle (w_0, w_a) under S84-DR3-RESPONSE-PROTOCOL; the DES-Dovekie 2026 reanalysis on DR2 BAO is informational only (NOT binding). Post-Dovekie σ-distances: canonical w0_FW = -0.918 → 2.130σ (was 2.91σ vs DR2-DESY5; σ-reduction 0.78σ); branch-(iv) w0_FW_R842 = -0.842454 → 0.731σ (was 1.59σ; σ-reduction 0.86σ); w_a (four-fold lock = 0) → 3.429σ (was 2.92σ; σ-tightening 0.25→0.21 ADVANCES tension by +0.51σ). | S84 (R_842 pre-registered); S88 W5 (Dovekie audit-pin) | LIVE-PENDING (DESI DR3 expected ~2027) | DESI DR3 release; framework canonical `w0_FW = -0.918` placed inside R_842 = [-0.94, -0.88] × [-0.2, 0.2] | PASS criterion: DR3 90% confidence interval contains either canonical (-0.918) OR branch-(iv) (-0.842454); FAIL if neither contained at 5σ; informational outside Volovik-partition branch closure. | `falsifier-master-inventory.md` row 1 + 1.dovekie-2026-update; `falsifier-watchlist.md` w_0 row |
| **Q38 — Window-15 CMB-S4 α_s canon-shift annotation**: per `falsifier-watchlist.md:140` α_s row, "PLAN-DRIFT: pre-S85 falsifier-watchlist row cited -0.069 ± 0.008" — the CANONICAL α_s prediction was re-pinned in S85 from -0.069 (Josephson sector) to +0.00117 (S63 RUNNING-NS-63). atlas-05-materials Section "Compiler notes" Recommendation #3 flag: atlas-05 currently does not contain the canon shift; recommend explicit annotation. atlas-08 currently cites the OLD α_s value at Q20 (line 137). | S85 (RUNNING-NS-63 canon; PLAN-DRIFT annotation in falsifier-watchlist) | OPEN (annotation propagation incomplete across atlas-05 + atlas-08) | Update Q20 entry in atlas-08 to cite α_s_FW = +0.00117 ± uncertainty (S63 RUNNING-NS-63); cross-link to `falsifier-watchlist.md:140` PLAN-DRIFT note + atlas-05 annotation. | PASS criterion: CMB-S4 measures α_s ∈ [+0.00117 ± 0.002] at 4σ confidence; FAIL if α_s = -0.0045 ± 0.0067 (Planck central) confirmed at 5σ. Canonical post-W13-5 α_s framework gap_sigma = 9.622 vs Planck-legacy. | `falsifier-watchlist.md:140`; atlas-05-materials Window-15 |
| **Q39 — g_1/g_2 = 0.684 vs 0.709 LIVE 3.5% tension**: framework prediction g_1/g_2 = 0.684 at τ=0.19 from RGE running; observed 0.709; 3.5% below — not yet decisive (observational uncertainty on 0.709 dominates). LIVE-PENDING in falsifier-watchlist. | S59+ (opened); LIVE-PENDING through S85 / S88 | LIVE-PENDING | RGE running refinement to higher-loop precision; PDG observational uncertainty band tightening; refinement queued. | PASS criterion: RGE-refined prediction within 1σ of PDG g_1/g_2 measurement; FAIL if framework gap exceeds 3σ at improved precision. | `falsifier-watchlist.md:46-50`; atlas-05-materials Window-18 |
| **Q40 — eps_H sign reversal post-S66 functional crisis live observational discrimination**: per `atlas-10-breakthrough-genealogy.md` #20, eps_H sign reversal between cutoff families (sqrt(x): +0.022 vs zeta: negative) is the most-important-negative-since-Venus-Moment. While the structural theorem A13 is PERMANENT, the observational discrimination between functional families (CMB-S4 / CMB-HD / LiteBIRD pivot precision) is the live falsifier path. Per `regulator-pin-discipline.md` MANDATORY tagging: every n_s-citation must declare regulator class. | S66 W2-A (theorem A13 PERMANENT); observational discrimination LIVE | LIVE-PENDING (CMB-S4 ~2030 / CMB-HD ~2035) | CMB-S4 / CMB-HD measures n_s + α_s at sub-percent precision; framework tags every prediction by regulator class; observation discriminates which functional family is realized. | PASS criterion per regulator class: sqrt(x) family PASSes if observed n_s ∈ [0.9550, 0.9700] AND α_s ∈ [+0.00117 ± 2σ]; zeta family FAILs (n_s > 1 predicted); intermediate families adjudicated at posterior level. | `atlas-10-breakthrough-genealogy.md` #20; `atlas-07-permanent-results.md §A13`; `falsifier-watchlist.md` α_s row |
| **Q41 — Lab-falsifier suite SW1 (3He-A NMR sweet-spot λ_6) horizon-2031 reach**: framework predicts substrate's δ_ω_K/ω_K = 1.7267 (M_KK-norm) measured at 58.9589 MHz at λ_6 direction; detection_ratio 58958.86 over σ_detect 0.001 MHz; LAB-FALSIFIER-A class. | S86 W11-C5 (introduced); 5-yr horizon 2031 | LIVE (lab-falsifier; P_decisive 0.30-0.50 at 5-yr 2031 horizon) | 3He-A NMR experiment at sub-Hz precision targeting λ_6 direction sweet-spot. | PASS criterion: observed within ±1 σ_detect of 58.9589 MHz; FAIL outside ±3 σ_detect; UNINFORMATIVE-NULL background-systematic-limited. | `falsifier-master-inventory.md` row #13; atlas-05-materials Window-20 |
| **Q42 — Lab-falsifier suite SW3 (173Yb optical-lattice unique λ_8 channel) horizon-2031 reach**: framework predicts substrate's Γ_3B(unique)/Γ_3B(inherited) = 2.8500 at λ_8 direction; SI value 1.4250 s^-1; detection_ratio 28.50 over σ_detect 0.05 s^-1. SW3 is the unique λ_8 channel; FAIL-AT-LAB on SW3 is the framework's strongest single-row substrate-direction-falsification trigger. | S86 W11-C5; 5-yr horizon 2031 | LIVE (lab-falsifier; P_decisive 0.30-0.50) | 173Yb optical-lattice 3-body Γ_3B measurement targeting λ_8 direction. | PASS criterion: observed within ±1 σ_detect of 1.4250 s^-1; FAIL outside ±3 σ_detect; FAIL is a structural λ_8-direction substrate-parameter falsification (not adjustable). | `falsifier-master-inventory.md` row #15; atlas-05-materials Window-22 |

#### CARRY-FORWARD class (computational items not yet promoted to questions)

The carry-forward inventory (CF1-CF20) in atlas-08 is preserved verbatim; none has individually closed. The S52-S88 era added the following NEW carry-forwards that should be ingested into the same Level 2-6 partitioning when the orchestrator updates atlas-08:

| new CF | item | source registry / source session | priority | notes |
|:-------|:-----|:--------------------------------|:---------|:------|
| CF21 | TD/LI Mukhanov-Sasaki H̃-branch divergence chase | S82 W-1 H̃-DIVERGENCE-CHASE workshop; 2.38-OOM gap on the same observable | Level 2 (workshop-open) | Both PASS-F2 individually; divergence is on the same observable; resolution determines which substrate-distance reading (transit-side or static-spectral-moment side) is canonical at horizon-exit |
| CF22 | A_s ledger F_amp_3PI vs F_amp_slot adjudication | S82 W-2; 122× discrepancy (F_amp_3PI = 47.92 vs F_amp_slot = 0.39) | Level 2 (S82 workshop) | UNIFIED-AS-79 canonical hardened; CF22 is the structural follow-up — are slot-routing and parametric-amp INDEPENDENT physical channels or is slot-PASS double-counting the 3PI ceiling? |
| CF23 | Substrate F_supp dynamics-side rate-limiter | S84 W-1; F_supp_max = 1.043783 vs 1.10 threshold (FAIL by 56 ppt, structural not numerical) | Level 2 | A_s closure rate-limiter relocated from dynamics to baseline; this is the dynamics-side residual |
| CF24 | LISA Ω_GW (A) / (C) regulator-class discriminator | atlas-05-materials Window-12; LISA 2035 horizon | Level 4 (long-term observational) | (A)-class O(10^-10) vs (C)-class 8.299e-58 (Sage-exact null); 11+ OOM PASS-margin to LISA-PLS sensitivity |
| CF25 | LiteBIRD n_T 4.250σ Path-H vs Path-C decisive | atlas-05-materials Window-13; LiteBIRD 2030 horizon | Level 2 | Path-H r=0.00745 vs Path-C r=0.0117 internal-consistency split (36.3% Path-C-relative); decisive over BK-Array 2026 1.417σ marginal |
| CF26 | f_NL_folded LAB-IN observable (Window-23) + φ_3 substrate-IS counterpart (Window-24) | atlas-05-materials Windows 23-24; CF-28 split | Level 2 | 3-pathway GGE-coupling discriminator; substrate-IS φ_3 cocycle in HC^3(A_K) STAGE-1-CANDIDATE pending Stage-2 verify |
| CF27 | Lab-falsifier suite Window-20/21 (SW1 / SW2) horizon-2031 cross-platform measurements | atlas-05-materials Windows 20-21 | Level 4 | 3He-A NMR + FeSe NMR observational opportunities |
| CF28 | F_4-MB structural wall family pole-distinct corpus extension | `permanent-results-registry.md` §VII.Z + §VII.V + §VII.K-PROP.W10-4 | Level 3 | Add Pillar-VII Bulletin entries at substrate-distance poles s ∈ {5, 6, 7} per Q31 |
| CF29 | Methodology K-counter advisory promotions (Class 8.4 / 8.5 / 8.6 + Layer-separability carve-out + Hybrid Independence Test + closing-paragraph-coherence audit pattern) | `epistemic-discipline.md`; `cross-pillar-bridge-anatomy.md`; `mechanical-closure-discipline.md` | Level 5 | Six SUGGESTION-status sub-clauses pending K=3 promotion; calibration corpus building for 2026+ closures |

### 2c. AGGREGATE counts

**Verified arithmetic** (substitution chain):
```
Existing atlas-08 = 6 decisive + 14 structural + 4 observational + 20 carry-forward = 44 total.
Closures = 6 (Q1, Q2, Q6, Q14, Q15, Q18); after closure: 44 − 6 = 38 retained.
NEW entries: 5 decisive (Q23-Q27) + 9 structural (Q28-Q36) + 6 observational (Q37-Q42) + 9 carry-forward (CF21-CF29) = 29 new.
Post-uplift total: 38 + 29 = 67 questions.
```

| Category | atlas-08 baseline | S52-S88 close | S52-S88 add | Proposed total | atlas-08-as-stated |
|:---------|:------------------:|:--------------:|:------------:|:---------------:|:-------------------:|
| Decisive | 6 | -2 (Q1, Q2)¹ | +5 (Q23-Q27) | 9 | 6 |
| Structural | 14 | -3 (Q14, Q15, Q18)² | +9 (Q28-Q36) | 20 | 14 |
| Observational | 4 | 0 | +6 (Q37-Q42) | 10 | 4 |
| Carry-Forward | 20 | -1 (Q6 deprioritization)³ | +9 (CF21-CF29) | 28 | 20 |
| **Total** | **44** | **-6** | **+29** | **67** | **44** |

¹ Q1 reframed; Q2 fully deprioritized + superseded.
² Q14 structural-replacement; Q15 partial-close (re-classified narrower STAGE-1-CANDIDATE retained as structural); Q18 structural-anchor with narrower sub-question retained as structural.
³ Q6 deprioritized (was Level 1 priority in atlas; remains as a partial-close superseded by §VII.AC.2 + §VII.X.W4-1); the original Q6 carry-forward role replaces with new entries.

The proposed-total **67** is consistent with the framework's S52-S88 expansion: +11 walls / +14 doors / +18 windows in atlas-05; +30 §VII slots in atlas-07; +14 Tier-1/2/3 inflection points in atlas-06 — the constraint-surface contour is expanding faster than questions are closing, which is what the cross-pillar-bridge era + methodology-floor era should look like at the registry-discipline level.

---

## Section 3 — Cross-atlas dependencies

### 3A. atlas-02-mechanism-lifecycle.md (closed mechanisms close some open questions)

Each S52-S88 mechanism closure in atlas-02-materials Era IX-XII corresponds to one or more atlas-08 questions. Cross-link table:

| atlas-08 Q | atlas-02 closure | session |
|:-----------|:------------------|:--------|
| Q1 reframe | TRANSIT-PS-67 (open carry-forward; sub-case ACOUSTIC-TRANSFER-68 INFO at FAIL) | S67-S77 |
| Q2 close | LEGGETT-MOMENT-70 PASS (DM bracket closed at 0.6%); supersedes atlas-08 Q2 remaining-relevance | S70 |
| Q6 deprioritization | §VII.AC.2 B1/B2 block decomposition uniqueness theorem PROVEN; §VII.X.W4-1 9-cell tensor STAGE-1-CANDIDATE | S86 W-3 / S87 W4-1 |
| Q14 structural-replace | §VII.W parity-grading orthogonality of HP_*(A_F); W17 bare-eigenvalue parity-blindness wall | S86 1a-S7 / S85 W2-7 |
| Q15 partial-close | Door-S62-Meissner (atlas-05): D_s(GGE)/D_s(fold) = 0.9885; Type-I classification preserved | S62 W2-02 |
| Q18 structural-anchor | §VII.AG.4 Z_3 gauge-sector signature 512=(2/3)×768 + §VII.AG.5 D1 gauge-counting correction | S86 W-6 |
| Q23 (new TRANSIT-PS-67) | Open carry-forward; pre-registered against `α_s(k_CMB) < 0.015` PASS / >0.019 FAIL | S67-S88 OPEN |
| Q24 (new Stage-2 §VII.W-3.LAB) | §VII.W-3.LAB STAGE-1-CANDIDATE; calibration corpus instance #3 of cross-pillar-bridge-anatomy K=3 MANDATORY | S88 W4a-17 |
| Q25 (new Stage-2 §VII.AM) | §VII.AM Universal Lock Condition STAGE-1-CANDIDATE; calibration corpus instance #2 of joint-theorem-promotion 4-stage pathway | S88 W1b2-65 |
| Q34 (W11 promotion gap) | Mechanism A (Volovik CC tracking) anchored at framework-cc-oom + falsifier-watchlist; lacks §VII slot | S66 (PASS without slot) |

### 3B. atlas-04-assumptions.md (assumption status changes ⇒ atlas-08 movements)

Per atlas-04's PROVEN/BROKEN/CONDITIONAL/UNTESTED status taxonomy, S52-S88 closures move 5 atlas-04 entries:

- **N2 Order-one A_F extraction**: CONDITIONAL (C + M3(C) extracted, dim 20; H quaternions requires bimodule). Status remains CONDITIONAL through S88 (no S52-S88 result executes the o-map route). **Q11 retained in atlas-08**.
- **N3 Order-one survival for D_total**: BROKEN (norm 4.000 at axiom 5). Status remains BROKEN through S88. **Q10 retained in atlas-08**.
- **C1 tau-evolution to cosmic time map**: ASSUMED. Partially answered by S58 Volovik partition derivation (Mechanism A canonical); **Q12 + Q13 partially close** but the rigorous reduction from 12D Einstein equations is not achieved. Retain as STRUCTURAL with the partial-progress annotation.
- **P2 Leggett mode physical observable**: CONDITIONAL (mass problem 170× at S49). S70 LEGGETT-MOMENT closes the DM-channel sub-question at 0.6%; the 170× MASS problem persists. **Q3 GOLDSTONE-MASS retained**.

### 3C. atlas-05-walls-doors-windows.md (every open question has a window in atlas-05)

Cross-link table — every atlas-08 open question maps to an atlas-05 window:

| atlas-08 Q | atlas-05 window | atlas-05 status |
|:-----------|:----------------|:----------------|
| Q23 TRANSIT-PS-67 | Window-9 | OPEN (computational; 0 yr) |
| Q24 Stage-2 §VII.W-3.LAB | Window-10 | OPEN (computational; 0 yr) |
| Q25 Stage-2 §VII.AM | (analog of Window-10; recommend Window-10b allocation) | OPEN |
| Q26 Stage-2 §VII.AH | (analog of Window-10; recommend Window-10c allocation) | OPEN |
| Q27 H_0 spinor-factor | Window-19 | LIVE-PENDING |
| Q28 FUNCTIONAL-SELECT-67 finalization | Window-7 | OPEN (computational; deferred since S67 ~22 sessions) |
| Q29 BBN-VOLOVIK-67 sharpening | Window-8 | OPEN (computational; deferred since S67 ~22 sessions) |
| Q30 FWD-C1/C2 dispatch | (no atlas-05 window yet; recommend Windows 25-26 allocation) | OPEN |
| Q31 §W10-120 DORMANT activation | (sub-extension of §VII.K-PROP.W10-4 anchor; no atlas-05 window) | DORMANT |
| Q32 D3 audit knowledge.db round-trip | (methodology-layer; no atlas-05 window) | OPEN |
| Q33 §VII.AJ.STATE-PROJ derivation | (sub-window of Window-10; pending) | OPEN |
| Q34 W11 §VII.AT promotion | (registry-state; no atlas-05 window) | OPEN |
| Q37 DESI DR3 binding-pending | Window-14 | LIVE (1-yr horizon 2027) |
| Q38 CMB-S4 α_s canon-shift | Window-15 | LIVE (4-yr horizon 2030) |
| Q39 g_1/g_2 LIVE | Window-18 | LIVE-PENDING |
| Q40 eps_H sign reversal observational | Windows 15-16 | LIVE (4-9 yr) |
| Q41 Lab-falsifier SW1 | Window-20 | LIVE (5-yr horizon 2031) |
| Q42 Lab-falsifier SW3 | Window-22 | LIVE (5-yr horizon 2031; UNIQUE λ_8 channel) |

### 3D. atlas-06-probability-trajectory.md (open questions are negative-trajectory contributors)

Per atlas-06-materials Section 2, the existing atlas-06 trajectory is double-peaked through S66 and "TBD" since (no formal Sagan adjudication S63-S66+). The open question count is the live-test-surface measure for any future Sagan adjudication. The proposed atlas-08 totals (67 questions, of which 9 decisive + 20 structural + 10 observational + 28 carry-forward) define the constraint-surface holes the framework's probability is conditioned on — fewer holes = lower-probability-conditional uncertainty, more decisive holes = higher EVOI per `evoi-prioritization.md`.

The 6 closures should register as POSITIVE inflections (constraint-surface contracting); the 29 new entries should NOT be miscounted as negative inflections (they are constraint-mapping progress, NOT closures of solution space — see `feedback_reporting-framing.md`). atlas-06 future Sagan adjudication should weight per-tier:
- Tier-1 (Q23-Q27 decisive Stage-2 verifies + cosmology adjudication): high-EVOI; 5 decisive holes that each potentially shifts trajectory.
- Tier-2 (Q37-Q42 observational): bound by detector horizons (1-yr to 9-yr).
- Tier-3 (Q28-Q36 structural + Q34-Q35 housekeeping): cumulative; methodology floor is part of constraint-surface integrity.

### 3E. atlas-09-retractions.md (re-opened questions = retracted closures)

Per atlas-09-materials Items 40-46, three S52-S88 retractions correspond to question-status reopenings:

- **Item 40 (§VII.AJ FWD-C3 instance #2 W11-5 REGISTRY-FAIL slot identity reclassification)**: the OP-PROJ + STATE-PROJ structurally-orthogonal-companion split surfaces Q33 (§VII.AJ.STATE-PROJ derivation OPEN) as a NEW question.
- **Item 41 (§VII.AN cross-corner SOURCE-DOUBLE-CITE-CO-PRIMARY retraction)**: methodology-layer; does NOT reopen an atlas-08 question but adds CF29 calibration corpus row.
- **Item 42 (W4-2 + W9b-2 PRU Class-(f) → Class-(d) reclassification)**: methodology-layer; adds CF29 row.
- **Item 36 (eps_H sign reversal — recorded as PERMANENT correction)**: surfaces Q40 (eps_H observational discrimination LIVE) — eps_H sign-level scheme dependence is the structural floor that makes Q40 a live observational question, not a closed structural one.

atlas-09's Section 2E "Suspected-but-not-yet-retracted" flags §VII.AM Universal Lock Condition (S88 W1b2-65) as STAGE-1-CANDIDATE pending Stage-2 verify; this maps directly to atlas-08 Q25.

### 3F. atlas-11-cross-pillar-bridge-corpus.md (Stage-2 verify pending = open)

Per atlas-07-materials Section 2 "Special clusters", atlas-11 (NEW; not yet authored) catalogs the cross-pillar bridge corpus K-counter:
- K=1 (S86 W-5 §VII.AF.1.OP-PROJ): Stage-1-CANDIDATE landed; Stage-2 verify NOT YET = atlas-08 Q24 contributor.
- K=2 (S87 W11-5 REGISTRY-FAIL → routed to §VII.AJ.OP-PROJ + §VII.AJ.STATE-PROJ): atlas-08 Q33 contributor.
- K=3 (S88 W4a-17 §VII.W-3.LAB): atlas-08 Q24 anchor.

The K=3 MANDATORY status (per `cross-pillar-bridge-anatomy.md §"Status: MANDATORY at K=3"`) is the methodology-layer wall that atlas-08 Q30 (FWD-C1 / FWD-C2 forward calibration) tracks.

### 3G. atlas-12-methodology-floor.md (methodology open questions; NEW per atlas-07-materials Section 2)

The proposed atlas-12 (NEW) catalogs methodology-floor closures + open methodology questions. CF29 above (six SUGGESTION-status sub-clauses pending K=3 promotion) routes there. Q32 (D3 audit knowledge.db round-trip gap) is a methodology-floor question. Q34 (W11 §VII.AT slot allocation) is registry-state housekeeping that lives partially in atlas-12 + partially in atlas-07.

---

## Substrate-framing audit (per `phononic-framing.md` + `epistemic-discipline.md`)

Each question framed as a CONSTRAINT-SURFACE HOLE on the substrate, NEVER as a "weakness" / "problem" / "gap to be filled to save the framework":

- Q1 close: "the e-fold path-1 question is structurally closed" — N_e = 0.1734 IC-independent CEILING, which is a property of the substrate's spectral action moments, not a failure. The constraint-surface region "exflation produces ≥ 3.1 e-folds at IC-independent path-1" is now MAPPED (closed-by-FAIL); the surviving region routes through transit power spectrum + acoustic transfer.
- Q23 TRANSIT-PS-67: "full Bogoliubov power spectrum through the τ-fold" — the substrate's mode-equation observable; the question is which sector of the substrate's spectral action carries the resonant amplification. PASS / FAIL is a property of the substrate's spectral content, not a property of a container the substrate sits inside.
- Q24-Q26 Stage-2 verifies: "two-agent parallel cross-axis independent-verify" — this is the constructive pathway for joint-axis evidence (per `joint-theorem-promotion.md` + `epistemic-discipline.md §"Source Authority Hierarchy"`); the PASS/FAIL is whether the substrate's structural identity holds when independently audited from two different methodology-axis projections of the same substrate-IS observable.
- Q28 FUNCTIONAL-SELECT-67 finalization: the open sub-question is which spectral functional class IS the substrate's regulator; this is a property of the substrate's algebra-axis structure (algebra-INVARIANT vs algebra-DEPENDENT functionals per algebra-axis orthogonality MANDATORY-K=3), not a property of an external selection criterion.
- Q40 eps_H sign reversal: the live observational question is which regulator class the laboratory measures; the substrate's eps_H is a regulator-CLASS-conditional spectral moment, not a regulator-INDEPENDENT scalar.
- Q41-Q42 Lab-falsifier suite: each row is "the substrate's δE_a / K_anis / Γ_3B ratio measured at the [lab] compactification scale at λ_a direction" — substrate-IS predictions projected to laboratory-IN observables via W11 C5 SI translation; PASS-AT-LAB is substrate-PARAMETER-confirmation along the cited λ direction.

Direction of explanation throughout: substrate IS [observable] → bridge map → laboratory IN [observable]. NEVER inverted (laboratory → substrate).

---

## Citation discipline (per `epistemic-discipline.md` Reporting Format)

Every question above cites: (i) source registry / rule / WP for its origin; (ii) resolution path with specific gate / falsifier / cross-pillar-verify that closes it; (iii) pre-registered PASS/FAIL criterion (where applicable). Cross-references to atlas-uplift-materials packets are explicit (atlas-01-materials, atlas-02-materials, atlas-05-materials, atlas-06-materials, atlas-07-materials, atlas-09-materials).

No emojis, no filler-validation language ("promising", "encouraging", "likely correct"). Probability/Bayesian assessments are routed to the Sagan workshop per `feedback_framework-hygiene.md`; this packet does NOT assign numerical probabilities to question outcomes.

---

## Report-back metadata

**(1) Packet path**: `C:\sandbox\Ainulindale Exflation\sessions\archive\session-88\atlas-uplift-materials\atlas-08-open-questions-materials.md`

**(2) Counts**:
- **Close-count**: 6 atlas-08 questions answered or structurally replaced post-S51 (Q1, Q2, Q6, Q14, Q15, Q18; with Q15 partial and Q18 structural-anchor with sub-question retained).
- **New-add-count**: 29 (5 decisive Q23-Q27 + 9 structural Q28-Q36 + 6 observational Q37-Q42 + 9 carry-forward CF21-CF29).
- **Net Δ**: +23 (post-uplift total 67 vs baseline 44).

**(3) Status-ambiguous between two classes**:
- **Q28 FUNCTIONAL-SELECT-67 finalization** straddles structural (which spectral functional family algebraically PASSes) and methodology (atlas-cardinality-aware sub-test under canonical_constants.py atlas extensions) classes. Filed under structural per the algebraic-class-membership criterion, but methodology-floor reading is also defensible. Recommend orchestrator decides at atlas-08 ingest.
- **Q32 D3 audit knowledge.db round-trip gap** straddles structural (the round-trip is a structural property of the entity-extraction pipeline) and methodology (the fix is a `/weave --update` + entity-extractor refinement). Filed under structural per the registry-completeness criterion; methodology classification also defensible.
- **Q33 §VII.AJ.STATE-PROJ BCS-physics-grounded substrate derivation** straddles decisive (one computation produces the BCS gap-equation kernel; resolution is binary closed-form vs not) and structural (the new mathematics is sector-resolved BdG self-consistency). Filed under structural per the new-mathematics-required criterion.
- **Q34 W11 §VII.AT promotion gap** straddles structural (the registry slot anchor is structural) and carry-forward (the operationalization is a registry-write housekeeping task). Filed under structural per the wall/anchor-status criterion.
- **Q35 S52-S60 atlas-01 backfill** straddles structural (the atlas timeline integrity is structural) and carry-forward (the operationalization is a backfill task). Filed under structural per the atlas-integrity criterion.

**(4) 4-class taxonomy adequacy flag (5th class candidate?)**:
- **YES — recommend a 5th class "methodology"** for FUNCTIONAL-SELECT-style questions and methodology-floor extensions.
- **Rationale**: post-S82 the framework grew a methodology-floor era (S82-S85 PRU/PRDR/source-reconciliation; S86 cross-pillar-bridge-anatomy + joint-theorem-promotion; S87 algebra-axis orthogonality K=3; S88 K=3 MANDATORY across multiple disciplines + Class 8.4/8.5/8.6 sub-classes opening). Several open questions (Q32 D3 audit knowledge.db round-trip; Q34 W11 §VII.AT promotion; CF29 Six SUGGESTION-status sub-clauses pending K=3 promotion) are STRUCTURALLY methodology-layer; they are neither "decisive computational gates" (the existing decisive class) nor "new mathematics required" (the existing structural class) nor observational nor carry-forward — they are methodology-promotion-gates with their own K-counter calibration corpus.
- **Proposed 5-class taxonomy**:
  - I. Decisive (one computation answers it)
  - II. Structural (new mathematics required for substrate-physics theorems)
  - III. Observational (external data required)
  - IV. Methodology (rule-file / registry-state / K-counter / audit-pipeline questions)
  - V. Carry-Forward (computational items not yet promoted to questions)
- **Calibration corpus for new class IV** (immediate ingest from this packet): Q28 FUNCTIONAL-SELECT-67 finalization (methodology-floor sub-test), Q32 D3 audit, Q34 W11 §VII.AT, plus CF29 (six SUGGESTION-status sub-clauses).
- **Alternative**: keep 4-class taxonomy and tag methodology-floor questions with explicit "(methodology-layer)" annotation in their sub-section header. This is the lower-friction approach but loses the partition-honesty per `wave-classification.md` strict-conjunction conventions.
- **Recommendation**: **add 5th class "Methodology"** for partition honesty.

**(5) Open question whose horizon has past without resolution** (route to falsifier-watchlist update):
- **Q28 FUNCTIONAL-SELECT-67** — opened S66; deferred since S67 (~22 sessions through S88). 0 yr / no detection horizon (computational). Per `feedback_fix-in-session-never-defer.md`, recommend orchestrator flag for S89 plan W0 priority audit. Status PARTIAL: archive-harvested edges show FAIL verdict in S67 table while BAYESIAN-FUNCTIONAL-67 follow-up shows PASS; the umbrella question retains OPEN classification in evoi-framework.
- **Q29 BBN-VOLOVIK-67** — opened S66; PASS at S72 audit but unified-schema cross-channel xcorr OPEN since S85 W4 introduction. ~22 sessions of partial progress. Recommend S89 plan W0 priority audit alongside Q28.
- **CF20 279-mode tachyonic transit velocity** (existing atlas-08 Level 6 carry-forward; opened S46) — never executed across S47-S88 (~42 sessions). Recommend explicit DEPRIORITIZED tag if the substrate-IS observable it would test has been superseded by S82-S88 substrate-IS observables, OR re-classify under new class IV (methodology) if its operationalization gap is what blocks resolution.
- **Q35 S52-S60 atlas-01 backfill** — pre-existing structural gap in atlas-01 (predates S52); no S52-S88 effort to fill. Recommend orchestrator dispatches separate atlas-01 backfill task per atlas-01-materials Section 4 #2.
- **CF21 TD/LI Mukhanov-Sasaki H̃-branch divergence chase** — opened S82 W-1; through S88 the workshop is OPEN with no Stage-3 closure. Recommend explicit horizon flag (workshop-open >5 sessions = stale; route to S89 plan W0 priority audit).

**Horizons triggered**: Q28 + Q29 + CF21 collectively flag a methodology-floor stagnation pattern in the FUNCTIONAL-SELECT / BBN-VOLOVIK / TD-LI computational queue. The stagnation is consistent with the framework's S82-S88 prioritization of structural rule-file landings over computational-gate execution; the orchestrator should weigh whether S89 returns to computational execution OR continues structural rule-file build-out.

---

**End of packet.**
