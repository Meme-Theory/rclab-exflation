# Session 88 Plan — Wave 8: K-counter discipline + cf29 carve-out + W4 corpus + Stage-2 verifies

> **Provenance**: planner-w8 (gen-physicist orchestrator + connes-ncg-theorist Stage-2 reviewer + lizzi-spectral-functional CO + volovik-superfluid-universe Stage-2 reviewer). Cluster H items 87-100 of the S88 carry-forward queue. 14-item wave covering K-counter discipline (cross-pillar-bridge-anatomy.md), cf29 carve-out (mechanical-closure-discipline.md), W4 corpus extensions, and the Stage-2 independent-verify of the §VII.AJ.W4-1 9-cell tensor STAGE-1-CANDIDATE (joint-theorem-promotion.md 4-stage pathway).
>
> **Verdict source**: `computations/s88_gate_verdicts.txt`
>
> **Substrate framing (per `.claude/rules/phononic-framing.md` §IS-not-IN)**: Every gate in this wave operates on the substrate spectral triple `(A_K, H_K, D_K)` with `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)`. The 9-cell cross-pillar tensor and its 18 off-diagonal Stage-2 verifies are bridge-anatomy declarations BETWEEN substrate-IS observables on different finite-L pillars and laboratory-IN observables on continuum platforms — the substrate IS the finite-L cocycle pair / Hochschild moment / spectral-action invariant; the laboratory IS NOT the substrate. The K-counter discipline tracks structural calibration of the bridge anatomy across distinct workshops, not narrative agreement.

## Wave 8 Summary

Cluster H (items 87-100; 14 gates) has FOUR theme-blocks:

| Block | Items | Theme |
|:------|:------|:------|
| **B-K-counter** | 87, 88 | Cross-pillar-bridge-anatomy.md K-counter discipline (Independence Test + Level-2 layer-distinction) |
| **B-carve-out** | 89, 90, 91 | mechanical-closure-discipline.md §"Layer-separability carve-out" + cf29/cf30 substantive runs |
| **B-W4-corpus** | 92, 93, 94, 97, 98, 99 | Reading-A registry-naming-hygiene rule, Type-F antisymmetric retry, channel-label normalization, orphan f_NL pathway, CF-29/30 resume-after-resolution chains |
| **B-Stage-2** | 95, 96, 100 | §VII.AJ.W4-1 Stage-2 cross-axis verify, CF-27 W14-4 re-pin, verdict-permanence-vs-sig5 user adjudication |

**Wave-class classification (per `.claude/rules/wave-classification.md` §M1-M4)**:
- **METHODOLOGY-class**: 87, 88, 89, 92, 94, 97, 100 (rule-file / template / pin-registry edits; allowlist append-only rows pinned in §0.11)
- **COMPUTE-class**: 90, 91, 93, 95, 96, 98, 99 (substrate-physics computation numerical output with pre-registered thresholds)

**Strict-conjunction note**: Items 89 and 90 are SEQUENTIALLY DEPENDENT — #90 is CONDITIONAL on #89 PASS + Stage-2 cross-reviewer PASS-AND. Items 91 and 93 are SEQUENTIALLY DEPENDENT — #91 CONDITIONAL on #90 PASS; #93 unblocks #98 unblocks #99.

## Wave 8 Decision Point Prerequisites

| Prerequisite | Status at Plan-Freeze | Reference |
|:-------------|:---------------------|:----------|
| §VII.AJ.W4-1 9-cell tensor STAGE-1-CANDIDATE landed | LANDED at S87 W4-? close | `sessions/permanent-results-registry.md` §VII.AJ.W4-1 |
| §VII.AG.1 (T7 ↔ S67 quotient-functor isomorphism) STAGE-1-CANDIDATE | LANDED at S87 W6-1 | `sessions/permanent-results-registry.md` §VII.AG.1 |
| §VII.AF.1 (W-5 Pillar III ↔ Pillar IV bridge theorem; 5-IS-not-IN + 3-level ladder) | LANDED at S87 W5-1 (calibration corpus instance #1; K=2 at S87-close per W11-meta-1 advancement) | `sessions/permanent-results-registry.md` §VII.AF.1; `.claude/rules/cross-pillar-bridge-anatomy.md` §"Calibration-corpus tracking" |
| W11-meta-2 K-counter advancement K=1→2 | LANDED at S87 W11-meta close | `.claude/rules/methodology-wave-allowlist.md` row W11-meta-1 |
| mechanical-closure-discipline.md §"When mechanical closure IS acceptable" | EXISTING at S87-close | `.claude/rules/mechanical-closure-discipline.md` §"When mechanical closure IS acceptable" |
| Type-F partition definition (single-summand-projection trace on `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)`) | LANDED at S87 W4-2 §3717 | `sessions/archive/session-87/session-87-results-workingpaper.md` §W4-2 line 3717 |
| joint-theorem-promotion.md Stage-2 protocol | EXISTING (S86 W-9 RULE-1) | `.claude/rules/joint-theorem-promotion.md` §"Stage 2" |
| canonical_constants.py `M_KK`, `tau_fold`, `Delta_BCS` | LANDED across S58-S86 | `computations/canonical_constants.py` |

All prerequisites cleared; Wave 8 dispatch authorized.

---

## §W8-87 — S88-CONSENSUS-INDEPENDENCE-TEST-LANDING

- **Gate ID**: `S88-CONSENSUS-INDEPENDENCE-TEST-LANDING`
- **Trigger**: Wave-0 plan-freeze; methodology rule-file edit
- **Classification**: METHODOLOGY-class (M1: artifact-existence; M2: Edit-only; M3: verbatim sub-diff from S87 cross-pillar-bridge-anatomy review; M4: allowlist row pinned §0.11)
- **Agent**: gen-physicist orchestrator (sole writer); CO-AUTHOR lizzi-spectral-functional-theorist for Independence Test rationale review (orchestrator-direct-write per `wave-classification.md §"Dispatch consequences"`)
- **Hypothesis**: A hybrid Independence Test `(i ∨ ii ∨ iii) ∧ iv` correctly partitions the cross-pillar-bridge calibration corpus such that retroactive §VII.AG.1 entry SUPERSEDES K-counter K=2 to K=1 (shared-anchor with §VII.AF.1 W-5 Level-3 + partial-axes-instance) while §VII.AF.1 + W11-5 §VII.AJ remain as the K=1 + K=2 (pending) instances.
- **Method**:
  1. Edit `.claude/rules/cross-pillar-bridge-anatomy.md` §"Forward template-adoption" to insert §"Hybrid Independence Test" sub-section.
  2. The Independence Test states: a calibration corpus instance counts toward K iff `(i ∨ ii ∨ iii) ∧ iv` where:
     - **(i)** distinct substrate-IS pillar from prior K-instances
     - **(ii)** distinct laboratory-IN pillar from prior K-instances
     - **(iii)** distinct bridge map class (HKR / Connes-Karoubi / K-theory boundary) from prior K-instances
     - **(iv)** independent algebraic envelope (NOT a numerical refinement of an existing K-instance's envelope)
  3. Apply retroactively to §VII.AG.1 (S87 W6-1 STAGE-1-CANDIDATE; T7 ↔ S67 quotient-functor isomorphism modulo cyclic-fold V_4): §VII.AG.1's Level-3 anchor is SHARED with §VII.AF.1 W-5 Level-3 (workshop-flagged shared-anchor) and only PARTIAL-AXES (the cyclic-fold V_4 partition is a quotient refinement of the full V_4-on-strata structure of §VII.AF.1, not an independent bridge map class). Therefore §VII.AG.1 fails clause (iv) — the algebraic envelope is a quotient-refinement of the W-5 envelope, not independent.
  4. Tag §VII.AG.1 retroactively as `SHARED-ANCHOR-COMPANION + PARTIAL-AXES-INSTANCE`; K-counter holds at K=1 (pre-W11-5 W11-meta-1 advancement re-evaluated at K=1 NOT K=2).
  5. Update §"Calibration-corpus tracking" sub-section to reflect K=1 (instance #1: §VII.AF.1 W-5) + K-counter pending at K=2 contingent on W11-5 §VII.AJ landing satisfying the Independence Test.
  6. Append allowlist row `W8-87 | S88 | S88-CONSENSUS-INDEPENDENCE-TEST-LANDING (cross-pillar-bridge-anatomy.md K-counter Independence Test landing) | <pending plan-freeze SHA>` to `.claude/rules/methodology-wave-allowlist.md`.
- **Machinery pin (PRDR)**:
  - Input pins: `.claude/rules/cross-pillar-bridge-anatomy.md` (current state at plan-freeze; SHA pinned in §0.11 ledger); `.claude/rules/methodology-wave-allowlist.md` (current state); `sessions/permanent-results-registry.md` §VII.AG.1, §VII.AF.1, §VII.AJ entries.
  - Free parameters: NONE (verbatim text-edit; no numerical thresholds).
- **4-tuple**: `(gate_id=S88-CONSENSUS-INDEPENDENCE-TEST-LANDING, wp_id=W8-87, scheme=METHODOLOGY-rule-file-edit, convention=hybrid-independence-test-i-ii-iii-AND-iv)`
- **Threshold**: PASS iff (a) `cross-pillar-bridge-anatomy.md` contains §"Hybrid Independence Test" sub-section with all four clauses (i/ii/iii/iv) verbatim AND (b) §VII.AG.1 retroactive tagging present `SHARED-ANCHOR-COMPANION + PARTIAL-AXES-INSTANCE` AND (c) calibration-corpus K-counter table updated to K=1 (W-5 only) AND (d) allowlist row appended AND (e) substantive line count ≥ 15 in the new sub-section.
- **Substitution chain (verifier rationale)**:
  - Step 1: Definition of K-counter advancement — N=3 promotion threshold per `feedback_rules-compensate-missing-structure.md` (existing at K=3 promotion to MANDATORY).
  - Step 2: Definition of "distinct calibration instance" PRE-Independence-Test — original cross-pillar-bridge-anatomy.md §"Forward template-adoption" treats EACH §VII registry entry citing the 5-IS-not-IN + 3-level discipline as one K-instance.
  - Step 3: Substitution under hybrid Independence Test `(i ∨ ii ∨ iii) ∧ iv`: §VII.AG.1's substrate-IS pillar (Pillar III) MATCHES §VII.AF.1 W-5 substrate-IS pillar (Pillar III) → clause (i) FAILS; §VII.AG.1's laboratory-IN pillar (Pillar IV) MATCHES §VII.AF.1 laboratory-IN pillar (Pillar IV) → clause (ii) FAILS; §VII.AG.1's bridge map (cyclic-fold V_4 quotient-functor) is a refinement of §VII.AF.1's HKR map, not an independent class → clause (iii) FAILS. Disjunction `(i ∨ ii ∨ iii)` therefore = FALSE.
  - Step 4: Conjunction `(false) ∧ iv = false` regardless of clause (iv). §VII.AG.1 fails the Independence Test.
  - Step 5 (direction): K-counter does NOT advance for §VII.AG.1; therefore K-counter post-W6-1 is K=1 (W-5 alone), NOT K=2.
  - Conclusion: The retroactive tag `SHARED-ANCHOR-COMPANION + PARTIAL-AXES-INSTANCE` correctly classifies §VII.AG.1 outside the K-counter, preserving K=1.
- **What PASS means**: cross-pillar-bridge-anatomy.md K-counter promotion threshold to MANDATORY (K=3) tracks ONLY structurally-independent calibration instances; §VII.AG.1 narrative inflation cannot drive premature MANDATORY-status. Bridge-anatomy discipline remains SUGGESTION at K=1.
- **What FAIL means**: methodology rule-file edit absent / malformed → re-dispatch with explicit verbatim text spec. K-counter promotion path uncertain pending re-edit.
- **Effort**: ~0.3 wave-equivalents (rule-file edit + retroactive registry tag + allowlist append).
- **Substrate framing**: The Independence Test enforces structural orthogonality of substrate-IS pillars / laboratory-IN pillars / bridge map classes — substrate is logically prior; rule-file content describes the substrate's calibration-corpus structure, not narrative agreement among reviewers.

---

## §W8-88 — S88-CROSS-PILLAR-BRIDGE-ANATOMY-SCHEMATIC-LAYER-DISTINCTION-LANDING

- **Gate ID**: `S88-CROSS-PILLAR-BRIDGE-ANATOMY-SCHEMATIC-LAYER-DISTINCTION-LANDING`
- **Trigger**: Wave-0 plan-freeze; methodology rule-file edit (companion to #87)
- **Classification**: METHODOLOGY-class (M1-M4 same justification as #87)
- **Agent**: gen-physicist orchestrator (sole writer); CO-AUTHOR connes-ncg-theorist for cohomology-class-binding rationale review.
- **Hypothesis**: The 3-level structural-confidence ladder admits a formal **layer distinction** at Level-2: cohomology-class-binding envelopes (regulator-invariant; bind to Level-1 identity at L → ∞) vs bare-decomposition envelopes (regulator-class-dependent; do not bind to Level-1 cohomology class). Failure to distinguish these at Level-2 propagates to Level-3 anchor mis-classification.
- **Method**:
  1. Edit `.claude/rules/cross-pillar-bridge-anatomy.md` §"Three-Level Structural-Confidence Ladder" to insert §"Level-2 Layer Distinction" sub-section (between Level-2 spec and Level-3 spec).
  2. Define two Level-2 layer classes:
     - **Level-2-binding**: algebraic envelope `L^{-α}` is the convergence rate of an HKR-image that binds the Level-1 cohomology class (e.g., W-5 `L^{-3}` at d=4 binds the HP^1 cohomology class via HKR `L → ∞` image to the Peotta-Törmä quantum-metric trace).
     - **Level-2-non-binding**: algebraic envelope is a bare-decomposition convergence rate that does NOT bind to Level-1 (e.g., a generic `L^{-2}` Mellin truncation envelope on `Tr(D_K^{-2s})` that lacks an HKR image to a continuum laboratory observable).
  3. Specify enforcement: Level-3 empirical anchor satisfies Level-2 only when the envelope is Level-2-binding; bare-decomposition envelopes are Level-2-non-binding and DO NOT count toward registry-PASS criterion (`Level-3 < Level-2 envelope`).
  4. Cross-link to §"Audit at plan-freeze" — auditor must verify Level-2 envelope is Level-2-binding via explicit bridge-map citation (HKR / Connes-Karoubi pairing / K-theory boundary).
  5. Append allowlist row `W8-88 | S88 | S88-CROSS-PILLAR-BRIDGE-ANATOMY-SCHEMATIC-LAYER-DISTINCTION-LANDING (Level-2 layer-distinction extension) | <pending>` to `methodology-wave-allowlist.md`.
- **Machinery pin (PRDR)**: Input pins: `.claude/rules/cross-pillar-bridge-anatomy.md` (current state); `.claude/rules/methodology-wave-allowlist.md` (current state). Free parameters: NONE.
- **4-tuple**: `(gate_id=S88-CROSS-PILLAR-BRIDGE-ANATOMY-SCHEMATIC-LAYER-DISTINCTION-LANDING, wp_id=W8-88, scheme=METHODOLOGY-rule-file-edit, convention=level2-binding-vs-non-binding-layer-distinction)`
- **Threshold**: PASS iff (a) §"Level-2 Layer Distinction" sub-section present with Level-2-binding + Level-2-non-binding definitions verbatim AND (b) enforcement clause specifying Level-3 < Level-2 envelope only counts under Level-2-binding AND (c) cross-link to §"Audit at plan-freeze" present AND (d) allowlist row appended AND (e) substantive line count ≥ 15.
- **Substitution chain (cohomology-class binding)**:
  - Step 1: Definition of HKR image — `HKR : HH^*(A^{≤L}) → H^*_{dR}(continuum-image)` (Hochschild-Kostant-Rosenberg, classical NCG).
  - Step 2: Definition of Level-1 cohomology-class identity — Level-1 states `[ε_substrate-IS] ↔ HKR-image[ε_laboratory-IN]` at the cohomology-class level (regulator-invariant, L-independent).
  - Step 3: Substitution: a `L^{-α}` envelope on `‖HKR(c_L) - c_continuum‖` IS a binding envelope iff `c_continuum` is the HKR-image of the Level-1 cohomology class; the envelope describes convergence of the Level-1 binding under HKR `L → ∞`.
  - Step 4: Simplify: a `L^{-α}` envelope on `Tr(D_K^{-2s})` (Mellin moment, no HKR image to continuum observable) does NOT bind Level-1; it is a bare-decomposition envelope.
  - Step 5 (direction): registry-PASS criterion `Level-3 < Level-2 envelope` is meaningful ONLY for Level-2-binding envelopes; applying it to Level-2-non-binding envelopes admits false-PASS. Therefore the layer distinction MUST be enforced at the audit level.
- **What PASS means**: Bridge-anatomy registry-landing audit can distinguish genuine Level-1-binding envelopes from bare-decomposition envelopes; false-PASS pathway closed.
- **What FAIL means**: Layer distinction unrecorded; bare-decomposition envelopes admissible at audit → false-PASS pathway open; remediation re-dispatch with explicit text spec.
- **Effort**: ~0.3 wave-equivalents.
- **Substrate framing**: Level-2-binding vs non-binding is a structural property of the bridge map (HKR / Connes-Karoubi) at the substrate ↔ laboratory layer pair — substrate-IS observables on the substrate side bind to laboratory-IN observables on the continuum side ONLY via HKR-image bridge maps; bare-decomposition envelopes describe substrate-internal convergence without binding to laboratory.

---

## §W8-89 — S88-MECHANICAL-CLOSURE-DISCIPLINE-LAYER-SEPARABILITY-CARVE-OUT-CLAUSE

- **Gate ID**: `S88-MECHANICAL-CLOSURE-DISCIPLINE-LAYER-SEPARABILITY-CARVE-OUT-CLAUSE`
- **Trigger**: Wave-0 plan-freeze; methodology rule-file edit (extends mechanical-closure-discipline.md)
- **Classification**: METHODOLOGY-class (M1-M4 same justification; M3 source = S87 W4-2 carry-forward analysis + cross-reviewer adjudication)
- **Agent**: gen-physicist orchestrator (sole writer); Stage-2 PASS-AND from connes-ncg + volovik cross-reviewers (cf. joint-theorem-promotion.md Stage-2 protocol).
- **Hypothesis**: Mechanical-closure scripts are admissible WITH CONDITIONS for layer-separable analyses where the layer-functor F (per `epistemic-discipline.md §"Layer-Decomposition"`) cleanly separates a substrate-physics observable into a Type-F (single-summand-projection trace) carve-out that admits closed-form mechanical evaluation distinct from a Type-S (state-pair functional) numerical evaluation.
- **Method**:
  1. Edit `.claude/rules/mechanical-closure-discipline.md` to add new top-level §"Layer-separability carve-out (admissible-with-conditions)" section between §"When mechanical closure IS acceptable" and §"When mechanical closure indicates a PLANNING DEFECT".
  2. Specify FOUR conditions L1-L4 for admissibility:
     - **L1 (Layer-functor cleanness)**: the substrate-physics observable admits a layer-functor F decomposition `F: substrate → methodology → audit` per `epistemic-discipline.md §"Layer-Decomposition"`, and the Type-F vs Type-S partition aligns with the substrate ↔ methodology layer pair under F.
     - **L2 (Type-F closed-form)**: the Type-F sub-observable admits a closed-form algebraic identity (e.g., single-summand-projection trace `Tr_{M_n(ℂ)}(P · A)` with `P` a minimal central projection) whose evaluation is mechanical (no numerical iteration; no random seed; no scan).
     - **L3 (Type-S separation)**: the Type-S sub-observable is structurally separated from Type-F (state-pair functional vs spectrum-only functional per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality"` 4-corner classification); mechanical closure on Type-F does NOT pre-determine Type-S verdict.
     - **L4 (Honesty disclosure)**: the closure script's verdict-line `convention` field MUST encode the carve-out tag `convention=<scheme>-LAYER-SEPARABLE-CARVE-OUT-TYPE-F`; the working-paper section MUST include explicit Type-F/Type-S separation paragraph; failure to disclose = PROHIBITED_ACTIONS Class 1 (convention-shopping).
  3. Specify Stage-2 cross-reviewer PASS-AND requirement: the carve-out is structurally novel; Stage-2 cross-reviewer PASS-AND (joint-theorem-promotion.md Stage-2 two-agent independent-verify, axes A=connes-spectral + B=volovik-substrate) is REQUIRED before #90 can dispatch.
  4. Establish calibration-corpus tracking K=1 → K=3 promotion to MANDATORY via the standard rule promotion threshold (`feedback_rules-compensate-missing-structure.md`); status SUGGESTION at K=1.
  5. Cross-link to v3-closure-recovery.md PROHIBITED_ACTIONS Class 1 (convention-shopping) — the carve-out is a STRUCTURAL extension of mechanical closure, not a per-gate convention swap; convention-tag honesty discipline (L4) is the boundary.
  6. Append allowlist row `W8-89 | S88 | S88-MECHANICAL-CLOSURE-DISCIPLINE-LAYER-SEPARABILITY-CARVE-OUT-CLAUSE | <pending>` to `methodology-wave-allowlist.md`.
- **Machinery pin (PRDR)**:
  - Input pins: `.claude/rules/mechanical-closure-discipline.md` (current state); `.claude/rules/epistemic-discipline.md §"Layer-Decomposition"` (current state); `.claude/rules/joint-theorem-promotion.md §"Stage 2"` (current state); `.claude/rules/cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality"` (current state).
  - Free parameters: NONE.
- **4-tuple**: `(gate_id=S88-MECHANICAL-CLOSURE-DISCIPLINE-LAYER-SEPARABILITY-CARVE-OUT-CLAUSE, wp_id=W8-89, scheme=METHODOLOGY-rule-file-edit, convention=layer-separability-carve-out-L1-L2-L3-L4-Stage-2-PASS-AND)`
- **Threshold**: PASS iff (a) §"Layer-separability carve-out (admissible-with-conditions)" section present with all four conditions L1-L4 verbatim AND (b) Stage-2 cross-reviewer PASS-AND requirement specified AND (c) calibration-corpus tracking K=1 → K=3 specified AND (d) cross-link to v3-closure-recovery.md PROHIBITED_ACTIONS Class 1 present AND (e) allowlist row appended AND (f) substantive line count ≥ 15.
- **Substitution chain (carve-out admissibility)**:
  - Step 1: Definition of mechanical closure (existing §"When mechanical closure IS acceptable") — orchestrator-authored verdict-line emission for upstream-blocked gates; FAIL/PRE-REG-INC only; no PASS.
  - Step 2: Definition of layer-functor F — `F: substrate → methodology → audit` mapping eigenvalue → rule-file content → audit-line content (epistemic-discipline.md §"Layer-Decomposition"). Type-F = single-summand-projection trace on `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` (substrate-physics layer). Type-S = state-pair functional (algebra-DEPENDENT layer per algebra-axis orthogonality).
  - Step 3: Substitution: under L1 ∧ L2 ∧ L3 ∧ L4, a Type-F closed-form evaluation is mechanical (no scan, no seed) AND structurally separable from Type-S (orthogonal under algebra-axis classification) AND honestly disclosed (convention tag + working-paper paragraph).
  - Step 4: Simplify: such a closure is NOT convention-shopping (the convention tag is fixed at plan-freeze and honestly disclosed) and NOT iterate-until-PASS (mechanical evaluation is closed-form, no iteration). It is a genuine STRUCTURAL extension of mechanical closure to layer-separable analyses.
  - Step 5 (direction): the carve-out admissibility opens a new pathway for S70-class / Pillar-III BCS / Pillar-VI A_s/n_s analyses that have Type-F sub-observables admitting mechanical evaluation; #90 dispatch CONDITIONAL on this carve-out + Stage-2 PASS-AND.
- **What PASS means**: mechanical-closure-discipline.md gains a structurally-validated carve-out clause; #90 dispatch authorized.
- **What FAIL means**: carve-out clause unauthored / Stage-2 PASS-AND fails → #90 BLOCKED; cf-29 substantive run cannot proceed via partition criterion.
- **Effort**: ~0.5 wave-equivalents (rule-file edit + Stage-2 dispatch coordination + cross-reviewer PASS-AND verification).
- **Substrate framing**: Layer-separability carve-out enforces structural orthogonality at the layer-functor F level — substrate Type-F observables (single-summand-projection traces) are mechanically evaluable BY CONSTRUCTION; substrate Type-S observables are state-pair functionals requiring numerical evaluation. The carve-out does not permit substrate-IS / laboratory-IN conflation; the layer distinction enforces IS-not-IN.

---

## §W8-90 — S88-CF-29-SUBSTANTIVE-RUN-VIA-PARTITION-CRITERION-ONLY

- **Gate ID**: `S88-CF-29-SUBSTANTIVE-RUN-VIA-PARTITION-CRITERION-ONLY`
- **Trigger**: CONDITIONAL on §W8-89 PASS + Stage-2 cross-reviewer PASS-AND. NOT dispatched at plan-freeze; queued for runtime conditional dispatch.
- **Classification**: COMPUTE-class (M1 fails: numerical comparison via Type-F partition test against Level-2 envelope tolerances; producing-script `computations/s88_w8_cf29_partition_classify.py`)
- **Agent**: connes-ncg-theorist (PRIMARY, Type-F partition algebraic verification on `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)`); volovik-superfluid-universe-theorist (CO, Type-S separation cross-check via state-pair functional structural tests).
- **Hypothesis**: The three substrate-physics observables {S70 LEGGETT-MOMENT, Pillar III BCS, Pillar VI A_s/n_s} partition under the partition criterion into Type-F (single-summand-projection trace; mechanically evaluable) or Type-S (state-pair functional; numerically evaluable) classes; the partition is unique and structurally testable at L_max=10 on the substrate spectral triple `(A_K, H_K, D_K)`.
- **Method**:
  1. Producing script: `computations/s88_w8_cf29_partition_classify.py`. Imports `from canonical_constants import *` for `M_KK`, `tau_fold`, `Delta_BCS`, `Vol_SU3`, `c_sub_baseline`, `r_PathH`. Loads `s84_spectrum_cache_L12_tau019.npz` master spectrum (S87 W11 cache).
  2. For each of the three observables {S70 LEGGETT-MOMENT, Pillar III BCS, Pillar VI A_s/n_s}, compute:
     - **Type-F partition test**: enumerate central minimal projections `P_α` on `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` (α ∈ {ℂ, ℍ, M_3}); evaluate the observable's expression on each projection: `O_α := Tr(P_α · O · P_α) / Tr(P_α · I)`. Test whether the observable equals `O_α` exactly for some single α (Type-F) OR is a non-trivial combination across α's (Type-S).
     - **Type-S separation cross-check**: evaluate the observable as a state-pair functional `O[ω_1, ω_2]` for state pair `(ω_1, ω_2) ∈ S(A_K) × S(A_K)`; verify whether the observable is non-constant on the state-pair manifold (Type-S) or projects to a spectrum-only functional (Type-F).
     - **Partition tag emission**: each observable receives a tag ∈ {Type-F-α (with α ∈ ℂ/ℍ/M_3), Type-S, MIXED}.
  3. Verdict-line composite: `composite = Type-F-tag(LEGGETT) + Type-F-tag(BCS) + Type-F-tag(A_s_n_s)`.
- **Machinery pin (PRDR)**:
  - Input pins: `s84_spectrum_cache_L12_tau019.npz` (S87 W11 cache; SHA pinned in §0.11 ledger); `canonical_constants.py` (current state); rule-file `mechanical-closure-discipline.md` post-#89 PASS (SHA pinned at runtime conditional dispatch).
  - Free parameters: L_max=10 (S87 W11 Casimir-bound canonical truncation; pinned per `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"`); tolerance `partition_tol=1e-12` for Type-F equality detection.
- **4-tuple**: `(gate_id=S88-CF-29-SUBSTANTIVE-RUN-VIA-PARTITION-CRITERION-ONLY, wp_id=W8-90, scheme=Type-F-partition-classify-via-A_K-central-projections, convention=L_max-10-Casimir-bound-truncation-tol-1e-12)`
- **Threshold**: PASS iff (a) all three observables receive a partition tag ∈ {Type-F-α, Type-S, MIXED} AND (b) Type-F partitions verified bit-identical against the central-projection trace at `partition_tol=1e-12` AND (c) Type-S separations verified non-trivial on state-pair manifold AND (d) verdict-line `convention=` field encodes `LAYER-SEPARABLE-CARVE-OUT-TYPE-F` per §W8-89 L4 honesty discipline. FAIL iff partition tag is ambiguous (no clean Type-F-α match within tolerance AND no clean Type-S separation). INFO iff one or more observables route to MIXED (combination of Type-F and Type-S sub-components).
- **Substitution chain (Type-F partition)**:
  - Step 1: Definition of `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` central minimal projections — `P_ℂ = (1, 0, 0)`, `P_ℍ = (0, I_2, 0)`, `P_{M_3} = (0, 0, I_3)`. Central minimal in the sense `Z(A_K) = ℂ ⊕ ℂ ⊕ ℂ` (one central projection per direct summand).
  - Step 2: Definition of single-summand-projection trace — `Tr_α(O) := Tr_{A_K}(P_α · O · P_α) / Tr_{A_K}(P_α · I)`, the normalized trace of `O` restricted to the α-th summand.
  - Step 3: Substitution: an observable `O` is Type-F-α iff `O = Tr_α(O) · I_{A_K}` (within `partition_tol`) for some unique α — i.e., `O` is a scalar multiple of the identity supported on a single summand.
  - Step 4: Simplify: equivalently, `O - Tr_α(O) · I_{A_K}` has Frobenius norm < `partition_tol` on the α-th summand AND vanishes on the other two summands.
  - Step 5 (direction): Type-F partition is mechanically testable bit-precision; Type-S separation requires evaluating `O[ω_1, ω_2]` non-trivial dependence — both tests are pre-registered with explicit tolerance, no convention-shopping pathway.
- **What PASS means**: cf-29 partition classification complete; CF-30 (#91) re-evaluation of K-count K=2 unblocked.
- **What FAIL means**: ambiguous partition; CF-29 substantive run cannot proceed via partition criterion alone; route to alternate classification path or PRE-REG-INC carry-forward.
- **What INFO means**: at least one observable routes to MIXED; CF-30 K-count re-evaluation must account for MIXED-class instances separately.
- **Effort**: ~1.0 wave-equivalents (compute on cached spectrum + Type-F/Type-S tests on three observables + verdict emission).
- **Substrate framing**: The substrate IS the algebra `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)`; central minimal projections `P_α` partition `A_K` into single summands by construction. Type-F observables ARE supported on a single summand of the substrate; Type-S observables ARE state-pair functionals on the substrate. The partition is intrinsic to the substrate's algebraic structure, not imposed externally.

---

## §W8-91 — S88-CF-30-RETROACTIVE-K-COUNT-REVISION-VIA-CF-29-SUBSTANTIVE

- **Gate ID**: `S88-CF-30-RETROACTIVE-K-COUNT-REVISION-VIA-CF-29-SUBSTANTIVE`
- **Trigger**: CONDITIONAL on §W8-90 PASS. Re-evaluates CF-30 K-count via the substantive partition classifications.
- **Classification**: COMPUTE-class (M1 fails: K-count integer comparison; M2 producing-script `computations/s88_w8_cf30_k_count_revise.py`)
- **Agent**: gen-physicist orchestrator (PRIMARY); CO-AUTHOR connes-ncg-theorist for instance-2 verification cross-check.
- **Hypothesis**: Under the substantive partition classifications from #90, CF-30 K-count revises to K=2: Instance 1 (S86 W-4 R3-A; verified at S86 close) + Instance 2 (verified at #90 via Type-F-α tag on at least one of {LEGGETT, BCS, A_s/n_s}) + Instance 3 (REFUTED — no clean Type-F partition for the third observable, or MIXED-class).
- **Method**:
  1. Producing script: `computations/s88_w8_cf30_k_count_revise.py`. Loads `s88_w8_cf29_partition_classify.npz` output from #90.
  2. For each of the three observables, read partition tag from #90 output:
     - Tag = Type-F-α → counts toward K
     - Tag = Type-S → does NOT count toward K
     - Tag = MIXED → does NOT count toward K (per cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality" 4-corner classification — MIXED-class observables fail layer-separability)
  3. Compute revised K-count: `K_revised = 1 (S86 W-4 R3-A baseline) + count(Type-F-α tags from #90)`.
  4. Verdict-line: PASS if K_revised = 2 AND third observable is REFUTED (Type-S or MIXED); FAIL if K_revised = 1 (no Type-F tags) or K_revised = 3 (all three Type-F, contradicting the prior REFUTED stance for instance 3); INFO if K_revised = 2 but third observable tag is MIXED rather than REFUTED.
- **Machinery pin (PRDR)**:
  - Input pins: `s88_w8_cf29_partition_classify.npz` (output of #90; SHA pinned at runtime); `mechanical-closure-discipline.md` post-#89 (SHA pinned).
  - Free parameters: NONE (deterministic count from #90 tags).
- **4-tuple**: `(gate_id=S88-CF-30-RETROACTIVE-K-COUNT-REVISION-VIA-CF-29-SUBSTANTIVE, wp_id=W8-91, scheme=K-count-revise-from-cf29-tags, convention=K-count-Type-F-only-Type-S-and-MIXED-excluded)`
- **Threshold**: PASS iff K_revised = 2 (one Type-F tag + Instance 1 baseline) AND third observable REFUTED. FAIL iff K_revised ∉ {2}. INFO iff K_revised = 2 but third observable MIXED rather than REFUTED.
- **Substitution chain (K-count derivation)**:
  - Step 1: Definition of K-count under Reading-B operator-projection separation rule — K = number of distinct calibration corpus instances satisfying the Type-F partition criterion (one Type-F-α tag per instance).
  - Step 2: Definition of Instance 1 (S86 W-4 R3-A) — verified at S86 close; baseline K=1 contribution.
  - Step 3: Substitution: K_revised = 1 + |{observables in {LEGGETT, BCS, A_s/n_s} : partition_tag = Type-F-α}|.
  - Step 4: Simplify: enumerate possibilities. If exactly one Type-F → K_revised = 2 (PASS). If zero Type-F → K_revised = 1 (FAIL; insufficient corpus). If two or three Type-F → K_revised ≥ 3 (FAIL; contradicts REFUTED-for-instance-3 prior).
  - Step 5 (direction): the threshold is asymmetric — only K_revised = 2 PASSes; both K=1 and K≥3 FAIL because the Reading-B operator-projection separation rule promotion is K=3 MANDATORY threshold; pre-promotion K=2 is the SUGGESTION-status target.
- **What PASS means**: CF-30 K-count K=2 substantively confirmed; Reading-B operator-projection separation rule promotion path remains at K=2 (SUGGESTION-status; promotion to MANDATORY at K=3 still requires one more instance).
- **What FAIL means**: K-count contradicts prior; Reading-B promotion path requires re-evaluation.
- **What INFO means**: K_revised = 2 via MIXED tag on instance 3 (rather than REFUTED); K-count technically PASSes but instance 3 status changes from REFUTED to MIXED, requiring registry-text update.
- **Effort**: ~0.3 wave-equivalents.
- **Substrate framing**: K-count tracks STRUCTURAL calibration corpus instances at the substrate-IS observable layer; Type-F partition is intrinsic to the substrate algebra `A_K`. K-count advancement is a structural property of the substrate's classification, not narrative agreement.

---

## §W8-92 — S88-OPERATOR-PROJECTION-READING-A-RULE-PROMOTE

- **Gate ID**: `S88-OPERATOR-PROJECTION-READING-A-RULE-PROMOTE`
- **Trigger**: Wave-0 plan-freeze; standalone Reading-A registry-naming-hygiene rule promotion (3-instance corpus already verified)
- **Classification**: METHODOLOGY-class (M1-M4 satisfied; M3 source = S87 W4-2 + W6-1 + W11-meta corpus verbatim extracts)
- **Agent**: gen-physicist orchestrator (sole writer); CO-AUTHOR connes-ncg-theorist for registry-naming consistency cross-check.
- **Hypothesis**: The Reading-A operator-projection registry-naming-hygiene rule (corpus already at K=3 across S87 W4-2 + W6-1 + W11-meta) qualifies for MANDATORY promotion per `feedback_rules-compensate-missing-structure.md` K=3 threshold; rule formalization in dedicated rule-file or as extension to `registry-landing.md` is the structural deliverable.
- **Method**:
  1. Author / extend rule-file (chosen path: extend `.claude/rules/registry-landing.md` with new top-level §"Operator-Projection Reading-A Naming Hygiene" section).
  2. Specify Reading-A naming convention: registry entry slot identifiers MUST distinguish operator-side projection (e.g., `§VII.X.OP-PROJ`) from state-side projection (e.g., `§VII.X.STATE-PROJ`) when the §VII.X theorem admits both projection readings.
  3. Cite calibration corpus K=3 instances:
     - **Instance 1**: S87 W4-2 §VII.AJ.W4-1 9-cell tensor (operator-projection on `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` central-projection traces)
     - **Instance 2**: S87 W6-1 §VII.AG.1 (operator-projection on T7 ↔ S67 quotient-functor cyclic-fold V_4 modulo)
     - **Instance 3**: S87 W11-meta-2 K-counter advancement (operator-projection on cross-pillar bridge-anatomy K-count discipline)
  4. Specify enforcement: registry-landing audit script `_registry_landing_audit.py` (existing) MUST flag entries that conflate operator-projection vs state-projection readings without explicit suffix tagging.
  5. Append allowlist row `W8-92 | S88 | S88-OPERATOR-PROJECTION-READING-A-RULE-PROMOTE | <pending>` to `methodology-wave-allowlist.md`.
- **Machinery pin (PRDR)**:
  - Input pins: `.claude/rules/registry-landing.md` (current state); `sessions/permanent-results-registry.md` §VII.AJ.W4-1, §VII.AG.1 entries; `feedback_rules-compensate-missing-structure.md` (K=3 promotion threshold).
  - Free parameters: NONE (3-instance corpus pre-verified at S87-close).
- **4-tuple**: `(gate_id=S88-OPERATOR-PROJECTION-READING-A-RULE-PROMOTE, wp_id=W8-92, scheme=METHODOLOGY-rule-file-edit, convention=reading-A-operator-projection-K-3-promote-MANDATORY)`
- **Threshold**: PASS iff (a) §"Operator-Projection Reading-A Naming Hygiene" section present in `registry-landing.md` with naming convention + 3-instance corpus + enforcement clause AND (b) status promoted to MANDATORY (per K=3) AND (c) allowlist row appended AND (d) substantive line count ≥ 15.
- **Substitution chain (rule promotion)**:
  - Step 1: Definition of K=3 promotion threshold — `feedback_rules-compensate-missing-structure.md` states rules promote from SUGGESTION → MANDATORY at K=3 distinct calibration corpus instances.
  - Step 2: Definition of Reading-A naming convention — operator-projection (algebra-side) vs state-projection (state-side) registry entry suffix.
  - Step 3: Substitution: corpus = {S87 W4-2 §VII.AJ.W4-1, S87 W6-1 §VII.AG.1, S87 W11-meta-2}; |corpus| = 3.
  - Step 4: Simplify: K = 3 ≥ K_promotion = 3 → status = MANDATORY.
  - Step 5 (direction): rule formalization at MANDATORY-status forces all future S88+ registry entries with both projection readings to use the explicit suffix tagging; registry-landing audit fires diagnostic FAIL on missing suffixes.
- **What PASS means**: registry-naming-hygiene rule landed at MANDATORY-status; future registry entries cannot conflate operator-projection vs state-projection readings.
- **What FAIL means**: rule formalization absent; registry-naming hygiene drift continues; re-dispatch.
- **Effort**: ~0.3 wave-equivalents.
- **Substrate framing**: Operator-projection vs state-projection is a structural distinction at the algebra-axis orthogonality layer (`cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality"`); registry-naming hygiene enforces the distinction at the registry-entry level.

---

## §W8-93 — S88-TYPE-F-ANTISYMMETRIC-CELL-PHASE-RETRY

- **Gate ID**: `S88-TYPE-F-ANTISYMMETRIC-CELL-PHASE-RETRY`
- **Trigger**: Wave-0 plan-freeze; re-run of CF-26 with antisymmetric ansatz
- **Classification**: COMPUTE-class
- **Agent**: connes-ncg-theorist (PRIMARY, Voronoi-cell phase realization on `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` central projections); CO-AUTHOR volovik-superfluid-universe-theorist (axiom-eps cross-check).
- **Hypothesis**: The Type-F Voronoi-cell phase realization with **antisymmetric ansatz** `θ_c = π · sin(2π · c/N) · (eig_c / λ_min)` satisfies axiom-eps `< 1e-12` AND drift `< 1%` PASS thresholds, where prior CF-26 symmetric ansatz FAILed.
- **Method**:
  1. Producing script: `computations/s88_w8_type_f_antisymmetric_cell_phase_retry.py`. Imports canonical constants. Loads `s84_spectrum_cache_L12_tau019.npz` for eigenvalue spectrum.
  2. Voronoi-cell partition: enumerate substrate cells `c ∈ {0, 1, ..., N-1}` indexed by central-projection-traced eigenvalue ordering. Use `N = 18` (matching the 18 off-diagonal cells of §VII.AJ.W4-1 9-cell tensor).
  3. Antisymmetric ansatz: `θ_c = π · sin(2π · c / N) · (eig_c / λ_min)` where `eig_c` is the c-th eigenvalue and `λ_min = min_c |eig_c|`. The `sin(2π · c / N)` factor introduces antisymmetry under `c → N - c` (zero at c=0, c=N/2; max at c=N/4; antisymmetric pairing).
  4. Axiom-eps test: compute axiom residual `axiom_eps = max_c |D_K(P_α · e^{i θ_c} · P_α) - e^{i θ_c} · D_K(P_α · P_α)|` (the equivariance residual under Type-F single-summand-projection phase rotation).
  5. Drift test: compute drift `drift = |Tr_α(e^{i θ_total} · O) - Tr_α(O)| / |Tr_α(O)|` where `θ_total = sum_c θ_c` — the integrated phase drift of a Type-F observable under the antisymmetric ansatz.
  6. PASS thresholds: `axiom_eps < 1e-12` AND `drift < 1e-2` (1%).
- **Machinery pin (PRDR)**:
  - Input pins: `s84_spectrum_cache_L12_tau019.npz` (S87 W11 cache; SHA pinned in §0.11); `canonical_constants.py` (M_KK, tau_fold).
  - Free parameters: `N = 18` (matched to §VII.AJ.W4-1 18-off-diagonal-cell structure; pinned per anchor); ansatz form `π · sin(2π · c/N) · (eig_c / λ_min)` (pinned; scan over alternative antisymmetric forms NOT permitted — convention-shopping prevention); `axiom_eps_threshold = 1e-12` (pre-registered); `drift_threshold = 1e-2` (pre-registered).
- **4-tuple**: `(gate_id=S88-TYPE-F-ANTISYMMETRIC-CELL-PHASE-RETRY, wp_id=W8-93, scheme=Voronoi-cell-antisymmetric-ansatz-pi-sin-2pi-c-N-eig-c-over-lambda-min, convention=N-18-axiom-eps-1e-12-drift-1e-2)`
- **Threshold**: PASS iff `axiom_eps < 1e-12` AND `drift < 1e-2`. FAIL otherwise.
- **Substitution chain (antisymmetric ansatz justification)**:
  - Step 1: Definition of CF-26 symmetric ansatz (FAILed at S87) — `θ_c = π · (eig_c / λ_min)` (no sinusoidal factor); residual integrated drift was 14.6% at N=18.
  - Step 2: Definition of antisymmetric ansatz — `θ_c = π · sin(2π · c/N) · (eig_c / λ_min)`.
  - Step 3: Substitution: integrated phase `θ_total = sum_{c=0}^{N-1} π · sin(2π · c/N) · (eig_c / λ_min)`. Use the identity `sum_{c=0}^{N-1} sin(2π · c/N) = 0` (geometric-series identity for N-th roots of unity).
  - Step 4: Simplify: if `eig_c / λ_min` were constant in c, then `θ_total = π · const · 0 = 0`, drift = 0 EXACTLY. Realistic `eig_c / λ_min` varies with c, but the antisymmetric weighting suppresses the integrated drift by a factor `~ <(eig_c - mean(eig)) / λ_min>` which is typically `O(1)` not `O(N)`.
  - Step 5 (direction): antisymmetric ansatz REDUCES integrated drift relative to symmetric ansatz BY CONSTRUCTION via the `sum sin(2π · c/N) = 0` identity; quantitative reduction depends on eigenvalue distribution and is the empirical content of the gate. Threshold `drift < 1%` tests whether the residual eigenvalue-variation contribution is suppressed below 1%.
- **What PASS means**: Type-F antisymmetric cell-phase realization is structurally consistent (axiom-eps < 1e-12) AND empirically consistent (drift < 1%); CF-26 unblocked; #98 dispatch authorized.
- **What FAIL means**: antisymmetric ansatz also fails; CF-26 remains BLOCKED; alternative classification path (substantive-reading carve-out adoption per §W8-89) required for #98.
- **Effort**: ~1.0 wave-equivalents (compute on cached spectrum + axiom-eps + drift evaluation).
- **Substrate framing**: The substrate IS the spectral triple `(A_K, H_K, D_K)`; Voronoi-cell partition is intrinsic to the eigenvalue ordering on `H_K`. Phase ansatz on cells is a substrate-internal structural choice; antisymmetric ansatz is a structural property of the substrate's cell-symmetry, not a free parameter.

---

## §W8-94 — S88-CHANNEL-LABEL-NORMALIZATION

- **Gate ID**: `S88-CHANNEL-LABEL-NORMALIZATION`
- **Trigger**: Wave-0 plan-freeze; canonical_constants.py pin landing
- **Classification**: METHODOLOGY-class (M1: artifact-existence; M2: Edit on canonical_constants.py + provenance entry; M3: verbatim from S87 W4-2 channel-label drift analysis; M4: allowlist row pinned)
- **Agent**: gen-physicist orchestrator (sole writer; canonical_constants.py edit per `math-scripts.md §"Canonical write-order"`).
- **Hypothesis**: The Hochschild cocycle channel labels {`channel_M2C`, `channel_M3C`, `channel_H`, `channel_C`, `channel_off_diag_<i,j>`} require canonical pinning in `canonical_constants.py` to prevent label-drift across S88+ scripts citing §VII.AJ.W4-1 9-cell tensor cells.
- **Method**:
  1. Edit `computations/canonical_constants.py` to add `CHANNEL_LABELS` dictionary pin:
     ```
     CHANNEL_LABELS = {
       "M_2(C)": "channel_M2C",  # M_2(ℂ) BdG sector (from inheritance ι_*(M_3(ℂ)) → M_2(ℂ))
       "M_3(C)": "channel_M3C",  # M_3(ℂ) Cartan-zone full sector
       "H":      "channel_H",     # ℍ quaternionic-isospin sector
       "C":      "channel_C",     # ℂ scalar-trace sector
       # 18 off-diagonal cells indexed by (k, i↔j) for i ≠ j in {C, H, M_3, M_2}
       "off_diag_C_H":   "channel_off_diag_C_H",
       "off_diag_C_M3":  "channel_off_diag_C_M3",
       # ... (full 18-cell enumeration)
     }
     ```
  2. Add provenance entry in canonical_constants.py: `# CHANNEL_LABELS pinned S88 W8-94 per s87 §VII.AJ.W4-1 9-cell tensor channel-label drift analysis; cites operator-projection Reading-A naming hygiene (S88 W8-92).`
  3. Append allowlist row `W8-94 | S88 | S88-CHANNEL-LABEL-NORMALIZATION | <pending>` to `methodology-wave-allowlist.md`.
- **Machinery pin (PRDR)**:
  - Input pins: `computations/canonical_constants.py` (current state); §VII.AJ.W4-1 registry entry (current state); §W8-92 Reading-A naming hygiene rule (post-#92 PASS state pinned at runtime).
  - Free parameters: NONE.
- **4-tuple**: `(gate_id=S88-CHANNEL-LABEL-NORMALIZATION, wp_id=W8-94, scheme=METHODOLOGY-canonical-constants-pin-landing, convention=CHANNEL-LABELS-dict-9-cell-tensor-22-entries)`
- **Threshold**: PASS iff (a) `CHANNEL_LABELS` dict present in canonical_constants.py with all 22 entries (4 diagonal + 18 off-diagonal) AND (b) provenance entry present AND (c) allowlist row appended AND (d) all S88+ scripts citing §VII.AJ.W4-1 channels CAN import `from canonical_constants import CHANNEL_LABELS`.
- **What PASS means**: channel-label drift across S88+ scripts prevented; canonical pin authoritative.
- **What FAIL means**: channel-label drift continues; re-dispatch with explicit dictionary spec.
- **Effort**: ~0.2 wave-equivalents.
- **Substrate framing**: Channel labels are structural identifiers of the substrate algebra `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` and its Hochschild-cocycle off-diagonal cells; canonical pin enforces structural consistency at the canonical-constants layer.

---

## §W8-95 — S88-CF-25-STAGE-2-INDEPENDENT-VERIFY

- **Gate ID**: `S88-CF-25-STAGE-2-INDEPENDENT-VERIFY`
- **Trigger**: Wave-0 plan-freeze; Stage-2 two-agent parallel cross-axis verify of §VII.AJ.W4-1 STAGE-1-CANDIDATE per joint-theorem-promotion.md 4-stage pathway.
- **Classification**: COMPUTE-class (M1 fails: PASS-AND verdict on per-clause cross-axis review; M2 producing-coordination via two parallel agent dispatches)
- **Agent**:
  - **Axis-A cross-reviewer**: connes-ncg-theorist (NCG-axiomatic / spectral-action perspective). Audits axis-A clauses + JOINT clauses.
  - **Axis-B cross-reviewer**: volovik-superfluid-universe-theorist (substrate-physics / superfluid analogy perspective). Audits axis-B clauses + JOINT clauses.
  - Both dispatched in PARALLEL with prompts CONTAINING ONLY the registered §VII.AJ.W4-1 entry text + relevant input files; NO workshop R1/R2/R3 transcripts.
- **Hypothesis**: The §VII.AJ.W4-1 9-cell tensor STAGE-1-CANDIDATE (joint Cross-Pillar 3-Channel Bridge Theorem; HKR + Connes-Karoubi pairing + K-theory boundary) advances from STAGE-1-CANDIDATE to STAGE-3-PERMANENT under Stage-2 cross-axis PASS-AND.
- **Method**:
  1. Coordinator (orchestrator) reads §VII.AJ.W4-1 registered entry text (Stage-1 form; contains all clauses (a)..(n) with axis-attribution).
  2. Identify per-clause axis-attribution: clauses authored on axis A (NCG-axiomatic) → connes audits; clauses authored on axis B (substrate-physics) → volovik audits; JOINT clauses → BOTH audit.
  3. Dispatch connes-ncg-theorist with prompt containing:
     - §VII.AJ.W4-1 registered entry text (Stage-1 form)
     - `computations/canonical_constants.py` (current state)
     - `s84_spectrum_cache_L12_tau019.npz` master spectrum cache (S87 W11)
     - Per-clause audit instruction: verify axis-A clauses + JOINT clauses from first principles WITHOUT reference to W4-1 workshop transcripts
     - Output: per-clause PASS/FAIL/INFO with substitution chain
  4. Dispatch volovik-superfluid-universe-theorist in PARALLEL with same structure; per-clause audit on axis-B clauses + JOINT clauses.
  5. Coordinator collects both verdicts; PASS-AND'd on JOINT clauses (both must independently PASS); single-axis clauses PASS only the axis-attributed reviewer.
  6. Producing script (coordinator-side aggregation): `computations/s88_w8_cf25_stage_2_aggregate.py`. Reads both reviewers' per-clause verdict outputs (npz files); computes Stage-2 composite.
- **Machinery pin (PRDR)**:
  - Input pins: §VII.AJ.W4-1 registered entry text SHA (pinned at plan-freeze); `canonical_constants.py` SHA (pinned); `s84_spectrum_cache_L12_tau019.npz` SHA (pinned); per-axis audit prompts (pinned at plan-freeze, frozen text).
  - Free parameters: NONE (Stage-2 protocol pre-specified per joint-theorem-promotion.md §"Stage 2"; cross-reviewer dispatches executed in parallel without prior workshop context).
- **4-tuple**: `(gate_id=S88-CF-25-STAGE-2-INDEPENDENT-VERIFY, wp_id=W8-95, scheme=Stage-2-two-agent-parallel-cross-axis-verify-no-workshop-context, convention=PASS-AND-on-JOINT-clauses-axis-A-connes-axis-B-volovik)`
- **Threshold**: PASS iff (a) BOTH cross-reviewers return PASS on their respective single-axis clauses AND (b) JOINT clauses PASS independently in BOTH verdicts (logical AND, NOT OR) AND (c) `_joint_theorem_independent_verify_audit.py` returns no Stage-2 protocol violations. FAIL iff any clause returns FAIL in either verdict. INFO iff any JOINT clause returns INFO in either verdict (Stage-2 → 3 promotion blocked; clause routes to remediation carry-forward).
- **Substitution chain (Stage-2 PASS-AND structure)**:
  - Step 1: Definition of Stage-2 protocol (joint-theorem-promotion.md §"Stage 2") — TWO independent cross-reviewers, ONE per axis, dispatched in parallel WITHOUT prior workshop context; JOINT clauses PASS-AND'd across the two verdicts.
  - Step 2: Definition of "without prior workshop context" — cross-reviewers receive ONLY the registered Stage-1 entry text + relevant input files; NO R1/R2/R3 transcripts.
  - Step 3: Substitution: connes verdict V_A = (clauses_A_PASS-states, JOINT_PASS-states_from_A); volovik verdict V_B = (clauses_B_PASS-states, JOINT_PASS-states_from_B).
  - Step 4: Simplify: JOINT_combined = JOINT_A AND JOINT_B (logical AND, per-clause). Stage-2-PASS = (all clauses_A PASS in V_A) AND (all clauses_B PASS in V_B) AND (all JOINT clauses PASS in both V_A and V_B).
  - Step 5 (direction): the AND-conjunction is structurally INDEPENDENT (the two reviewers operate without shared context); agreement under AND-conjunction is INDEPENDENT verification per `epistemic-discipline.md §"What Counts as Evidence"`. Stage-2 PASS is the only pathway that promotes §VII.AJ.W4-1 from STAGE-1-CANDIDATE to STAGE-3-PERMANENT.
- **What PASS means**: §VII.AJ.W4-1 promotes STAGE-1-CANDIDATE → STAGE-3-PERMANENT; orchestrator session-end synthesis updates registry tag.
- **What FAIL means**: Stage-2 → 3 promotion blocked; theorem stays at Stage-1; FAILing clauses route to next-session remediation.
- **What INFO means**: theorem stays at Stage-1; INFO clause documented as Stage-2-INFO-deferred item.
- **Effort**: ~1.5 wave-equivalents (two parallel cross-reviewer dispatches + coordinator aggregation + Stage-2 audit script execution).
- **Substrate framing**: Stage-2 cross-axis verify enforces structural independence of the cross-reviewers' agreement on JOINT clauses; substrate-IS observables (axis-A NCG-axiomatic) and substrate-IS observables (axis-B substrate-physics analog) are independently verified at the cohomology-class level. The agreement IS structurally independent (no shared workshop context); IS-not-IN discipline preserved.

---

## §W8-96 — S88-CF-27-PIN-RE-PIN-AT-PLAN-FREEZE

- **Gate ID**: `S88-CF-27-PIN-RE-PIN-AT-PLAN-FREEZE`
- **Trigger**: Wave-0 plan-freeze; CF-27 W14-4 locked-text source re-pin
- **Classification**: COMPUTE-class (M1 fails: SHA comparison against canonical pin; M2 producing-script `computations/s88_w8_cf27_pin_repin.py`)
- **Agent**: gen-physicist orchestrator (PRIMARY).
- **Hypothesis**: The W14-4 locked-text source SHA at S88 plan-freeze matches the canonical constants `f_NL_FW_S82_equilateral`, `f_NL_FW_S67_folded`, `f_NL_FW_S85_W9_3_analytic_template` provenance entries; if drift detected, re-pin to S88-current state.
- **Method**:
  1. Producing script: `computations/s88_w8_cf27_pin_repin.py`. Reads `computations/canonical_constants.py` provenance entries for `f_NL_FW_S82_equilateral`, `f_NL_FW_S67_folded`, `f_NL_FW_S85_W9_3_analytic_template`.
  2. For each, extract cited source path + line range; compute SHA-256 of source file at S88 plan-freeze.
  3. Compare against canonical SHA in provenance entry.
  4. If match: PASS (pin still valid). If drift: emit FAIL with diagnostic; re-pin via `update_constant(name, value, session="S88", source="S88-W8-96", comment="re-pinned at S88 plan-freeze; prior SHA <old>; new SHA <new>")`.
- **Machinery pin (PRDR)**:
  - Input pins: `canonical_constants.py` provenance entries (current state SHA pinned); cited source files (SHAs computed at runtime).
  - Free parameters: NONE.
- **4-tuple**: `(gate_id=S88-CF-27-PIN-RE-PIN-AT-PLAN-FREEZE, wp_id=W8-96, scheme=SHA-comparison-canonical-vs-source, convention=re-pin-on-drift-via-update_constant)`
- **Threshold**: PASS iff all 3 f_NL pathway-keyed provenance SHAs match source SHAs at S88 plan-freeze. FAIL with diagnostic + re-pin if drift detected. INFO if pathway-keyed entry missing entirely (route to canonical_constants.py promotion via `math-scripts.md §"Canonical write-order"`).
- **What PASS means**: W14-4 source pins remain valid at S88; no re-pinning required.
- **What FAIL means**: drift detected; re-pin executed in-script; canonical_constants.py updated with new SHA.
- **Effort**: ~0.3 wave-equivalents.
- **Substrate framing**: Pin-source tracking enforces canonical-sourcing discipline per `substrate-first-canonical-sourcing.md` — substrate-first canonical pin is authoritative; drift detection prevents stale-source citation drift.

---

## §W8-97 — S88-CF-28-ORPHAN-FNL-PATHWAY-REGISTRY-UPDATE

- **Gate ID**: `S88-CF-28-ORPHAN-FNL-PATHWAY-REGISTRY-UPDATE`
- **Trigger**: Wave-0 plan-freeze; orphan f_NL pathway registry update
- **Classification**: METHODOLOGY-class (M1: artifact-existence; M2: Edit-only on registry markdown; M3: verbatim from S87 W14-4 follow-up; M4: allowlist row pinned)
- **Agent**: gen-physicist orchestrator (sole writer; mack-cosmic-bridge cross-check per `feedback_mack-bridge-role.md` if mack is registry sole-writer for falsifier inventory).
- **Hypothesis**: The f_NL folded-pathway registry row label updates from "Row #9" to "Row #9a" to reflect orphan-pathway sub-rowing per S87 W14-4 follow-up.
- **Method**:
  1. Edit `sessions/framework/registry/f-nl-folded-pathway-registry.md` (or equivalent registry file location) to rename "Row #9" → "Row #9a" verbatim across all citations within the file.
  2. Add cross-reference note: "Row #9a indicates orphan-pathway sub-row landing per S88 W8-97 (S87 W14-4 follow-up)".
  3. Cross-link to `falsifier-master-inventory.md` if applicable (mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`).
  4. Append allowlist row `W8-97 | S88 | S88-CF-28-ORPHAN-FNL-PATHWAY-REGISTRY-UPDATE | <pending>` to `methodology-wave-allowlist.md`.
- **Machinery pin (PRDR)**:
  - Input pins: `sessions/framework/registry/f-nl-folded-pathway-registry.md` (current state); S87 W14-4 follow-up registry-row analysis (SHA pinned).
  - Free parameters: NONE.
- **4-tuple**: `(gate_id=S88-CF-28-ORPHAN-FNL-PATHWAY-REGISTRY-UPDATE, wp_id=W8-97, scheme=METHODOLOGY-registry-row-rename, convention=Row-9-to-Row-9a-orphan-pathway)`
- **Threshold**: PASS iff (a) all "Row #9" instances renamed to "Row #9a" in registry file AND (b) cross-reference note present AND (c) allowlist row appended.
- **What PASS means**: orphan f_NL pathway registry hygiene fixed; downstream consumers cite Row #9a unambiguously.
- **What FAIL means**: registry-row rename incomplete; re-dispatch.
- **Effort**: ~0.2 wave-equivalents.
- **Substrate framing**: Registry-row labels track substrate-physics observables (f_NL pathway-keyed predictions); orphan-pathway sub-rowing preserves structural attribution.

---

## §W8-98 — S88-CF-29-RESUME-AFTER-CF-26-RESOLUTION

- **Gate ID**: `S88-CF-29-RESUME-AFTER-CF-26-RESOLUTION`
- **Trigger**: CONDITIONAL on §W8-93 PASS (CF-26 antisymmetric ansatz resolution) OR on §W8-89 PASS + §W8-90 PASS (substantive-reading carve-out adoption).
- **Classification**: COMPUTE-class (M1 fails: numerical comparison via partition criterion or substantive-reading carve-out)
- **Agent**: connes-ncg-theorist (PRIMARY); CO-AUTHOR volovik-superfluid-universe-theorist.
- **Hypothesis**: CF-29 Type-F/Type-S classification of the three substrate observables resumes via either (path-A) CF-26 antisymmetric ansatz PASS unblocking Voronoi-cell phase realization, or (path-B) substantive-reading carve-out clause adoption per §W8-89.
- **Method**:
  1. At runtime, check trigger conditions:
     - If §W8-93 PASS → path-A: re-run CF-29 Type-F partition test using cell-phase realization output from #93.
     - Else if §W8-89 PASS + §W8-90 PASS → path-B: CF-29 already classified via partition criterion at #90; emit verdict cross-link to #90.
     - Else: PRE-REG-INC (both pathways blocked).
  2. Producing script: `computations/s88_w8_cf29_resume.py`. Branches on trigger condition.
  3. Path-A: Re-run partition tests on three observables {LEGGETT, BCS, A_s/n_s} using Voronoi-cell phase data from #93 NPZ output; emit composite Type-F/Type-S tags.
  4. Path-B: Emit cross-link verdict citing #90 partition tags directly.
- **Machinery pin (PRDR)**:
  - Input pins: §W8-93 NPZ output (path-A; SHA pinned at runtime); §W8-90 NPZ output (path-B; SHA pinned at runtime); rule-files post-#89 (path-B; SHA pinned).
  - Free parameters: NONE (deterministic branch on trigger condition).
- **4-tuple**: `(gate_id=S88-CF-29-RESUME-AFTER-CF-26-RESOLUTION, wp_id=W8-98, scheme=trigger-conditional-path-A-cell-phase-or-path-B-substantive-carve-out, convention=Type-F-tag-emission-on-three-observables)`
- **Threshold**: PASS iff (path-A: all three observables receive Type-F-α / Type-S / MIXED tag at `partition_tol=1e-12`) OR (path-B: cross-link verdict consistent with #90 tags). FAIL iff trigger conditions both fail. PRE-REG-INC iff both upstream pathways unresolved.
- **What PASS means**: CF-29 substantive classification complete via one of two structural paths; #99 dispatch unblocked.
- **What FAIL means**: classification ambiguous; #99 BLOCKED.
- **What PRE-REG-INC means**: upstream §W8-89, §W8-90, §W8-93 all FAIL or upstream-blocked; mechanical-closure verdict per `mechanical-closure-discipline.md §"When mechanical closure IS acceptable"` (FAIL with `value='upstream_<reason>'`).
- **Effort**: ~0.5 wave-equivalents (conditional branch + classification re-emission).
- **Substrate framing**: Type-F/Type-S classification is structural; substrate algebra `A_K` partition is intrinsic; resume pathways are structural recovery from upstream BLOCKED states.

---

## §W8-99 — S88-CF-30-RESUME-AFTER-CF-29-RESOLUTION

- **Gate ID**: `S88-CF-30-RESUME-AFTER-CF-29-RESOLUTION`
- **Trigger**: CONDITIONAL on §W8-98 PASS.
- **Classification**: COMPUTE-class (M1 fails: K-count comparison; M2 producing-script)
- **Agent**: gen-physicist orchestrator (PRIMARY); CO-AUTHOR connes-ncg-theorist.
- **Hypothesis**: Reading-B operator-projection separation rule promotion path re-attempts under K=3 corpus (CF-29 substantive contributions from #98 added to existing K=2 baseline).
- **Method**:
  1. Producing script: `computations/s88_w8_cf30_resume.py`. Loads `s88_w8_cf29_resume.npz` (output of #98).
  2. Compute K_revised = 1 (S86 W-4 R3-A baseline) + count(Type-F-α tags from #98).
  3. If K_revised ≥ 3 → Reading-B operator-projection separation rule promotion to MANDATORY pathway authorized; emit PASS-PROMOTION-AUTHORIZED.
  4. If K_revised = 2 → status remains SUGGESTION at K=2; emit INFO-K-2-PROMOTION-PENDING.
  5. If K_revised < 2 → FAIL.
- **Machinery pin (PRDR)**:
  - Input pins: `s88_w8_cf29_resume.npz` (output of #98; SHA pinned at runtime).
  - Free parameters: NONE.
- **4-tuple**: `(gate_id=S88-CF-30-RESUME-AFTER-CF-29-RESOLUTION, wp_id=W8-99, scheme=K-count-K-revised-from-cf29-resume, convention=K-3-promotion-MANDATORY-K-2-SUGGESTION-K-1-FAIL)`
- **Threshold**: PASS-PROMOTION-AUTHORIZED iff K_revised ≥ 3. INFO-K-2-PROMOTION-PENDING iff K_revised = 2. FAIL iff K_revised < 2.
- **Substitution chain (K-count under #98 substantive contributions)**:
  - Step 1: Definition of K_revised — 1 (baseline) + count(Type-F-α tags from #98).
  - Step 2: Substitution from #98 NPZ output: enumerate the three observable tags. K_revised = 1 + |{Type-F-α tags}|.
  - Step 3: Simplify: if all three Type-F → K_revised = 4 (PASS-PROMOTION). If two Type-F → K_revised = 3 (PASS-PROMOTION). If one Type-F → K_revised = 2 (INFO). If zero → K_revised = 1 (FAIL).
  - Step 4: Direction: PASS-PROMOTION threshold K ≥ 3 per `feedback_rules-compensate-missing-structure.md` MANDATORY promotion criterion.
- **What PASS means**: Reading-B operator-projection separation rule advances to MANDATORY status; rule-file landing dispatched in S89+.
- **What INFO means**: K=2 SUGGESTION-status retained; one more substantive instance needed for MANDATORY promotion.
- **What FAIL means**: K-count regresses below 2; rule-promotion path uncertain.
- **Effort**: ~0.3 wave-equivalents.
- **Substrate framing**: K-count promotion tracks substrate-IS structural calibration corpus; operator-projection vs state-projection distinction is intrinsic to substrate algebra-axis orthogonality.

---

## §W8-100 — S88-VERDICT-PERMANENCE-VS-SIG5-RULE-COLLISION-RESOLUTION

- **Gate ID**: `S88-VERDICT-PERMANENCE-VS-SIG5-RULE-COLLISION-RESOLUTION`
- **Trigger**: Wave-0 plan-freeze; user-adjudicated policy decision
- **Classification**: METHODOLOGY-class (M1: artifact-existence; M2: rule-file edit; M3: verbatim from user adjudication; M4: allowlist row pinned)
- **Agent**: gen-physicist orchestrator (sole writer; user adjudicates the policy collision; orchestrator drafts policy text and routes to user for final approval before edit).
- **Hypothesis**: A genuine rule-file collision exists between (i) `gate-verdicts.md` "verdict permanence" clause (verdicts are permanent, never retroactively changed) and (ii) `v3-closure-recovery.md` sig_5 SHA-uniqueness remediation (re-emit verdict line via script rerun on SHA-hardcoding bug detection). Resolution requires user adjudication; once adjudicated, a unified policy text lands in both rule-files.
- **Method**:
  1. Author policy-decision proposal (orchestrator draft, awaiting user adjudication):
     - **Option A**: Verdict permanence absolute; sig_5 remediation operates by APPENDING a corrected canonical line (with `supersedes=<old_audit_sha>` tag) — original verdict line retained in audit trail; downstream consumers cite the latest non-superseded line.
     - **Option B**: sig_5 remediation overrides verdict permanence on duplicate-SHA detection; old verdict line REPLACED in-place; audit trail logged in recovery_iteration_log.json instead of verdict file.
     - **Option C**: Per-class boundary: SHA-hardcoding bug (`audit_sha256` duplicate) → Option B (replace; audit log preserves trail). Genuine duplicate verdict (same gate ID, same value) → Option A (append with supersedes tag).
  2. Route policy-decision proposal to user; user selects Option A / B / C OR provides custom resolution.
  3. Edit BOTH `gate-verdicts.md` and `v3-closure-recovery.md` with consistent policy text reflecting user's decision.
  4. Cross-link the two rule-files at the relevant clauses.
  5. Append allowlist row `W8-100 | S88 | S88-VERDICT-PERMANENCE-VS-SIG5-RULE-COLLISION-RESOLUTION | <pending>` to `methodology-wave-allowlist.md`.
- **Machinery pin (PRDR)**:
  - Input pins: `.claude/rules/gate-verdicts.md` (current state); `.claude/rules/v3-closure-recovery.md` (current state); user adjudication output (pinned at decision time).
  - Free parameters: user's adjudication choice (Option A / B / C / custom) — NOT a free parameter post-adjudication; pinned at decision time.
- **4-tuple**: `(gate_id=S88-VERDICT-PERMANENCE-VS-SIG5-RULE-COLLISION-RESOLUTION, wp_id=W8-100, scheme=METHODOLOGY-rule-file-edit-policy-decision, convention=user-adjudicated-Option-A-or-B-or-C)`
- **Threshold**: PASS iff (a) user adjudication received AND (b) consistent policy text landed in both `gate-verdicts.md` and `v3-closure-recovery.md` AND (c) cross-link present between the two rule-files AND (d) allowlist row appended AND (e) substantive line count ≥ 15 in each rule-file edit.
- **Substitution chain (rule-collision identification)**:
  - Step 1: Definition of `gate-verdicts.md` permanence clause — verdicts are permanent; once recorded, a verdict cannot be retroactively changed.
  - Step 2: Definition of `v3-closure-recovery.md` sig_5 remediation — duplicate `audit_sha256` across two or more verdict lines → fix offending gate's producing script + RERUN (rerun appends new canonical line per dual-SHA template).
  - Step 3: Substitution: a sig_5 remediation rerun emits a NEW canonical line; the OLD canonical line (with duplicate SHA) is structurally invalidated.
  - Step 4: Simplify: the question is whether the OLD line is RETAINED (verdict permanence; superseded by new line) or REPLACED in-place (sig_5 fix; old line removed).
  - Step 5 (direction): under Option A, both lines are retained, and the new line carries `supersedes=<old_audit_sha>`. Under Option B, old line is removed; recovery_iteration_log.json preserves audit trail. Under Option C, the choice depends on whether the duplicate is a SHA-hardcoding bug (replace) or a genuine duplicate verdict (append). Resolution is structurally meaningful; user adjudication selects the policy.
- **What PASS means**: rule-file collision resolved via user adjudication; consistent policy across `gate-verdicts.md` + `v3-closure-recovery.md`; downstream consumers (orchestrator + audit scripts) cite the unified policy.
- **What FAIL means**: user adjudication absent or inconsistent edits; collision unresolved; potential for downstream verdict-line / recovery-log conflict.
- **Effort**: ~0.5 wave-equivalents (policy proposal authoring + user adjudication routing + rule-file edits).
- **Substrate framing**: The collision is a methodology-layer (rule-file) artifact; resolution preserves substrate-physics verdict-trail integrity. Substrate-IS observables (verdict values) are not affected; only the methodology-layer audit-trail discipline is at issue.

---

## Wave 8 → Wave 9 Decision Point

| Trigger | Action |
|:--------|:-------|
| All 14 gates PASS | Cluster H closes; Wave 9 dispatched per S88 W9 plan |
| §W8-89 FAIL (carve-out clause) | §W8-90, §W8-91 BLOCKED; mechanical-closure CF-29 routed to PRE-REG-INC; carry-forward to S89 |
| §W8-93 FAIL AND §W8-89 FAIL | §W8-98, §W8-99 PRE-REG-INC; CF-26/CF-29/CF-30 chain BLOCKED; carry-forward to S89 |
| §W8-95 FAIL (Stage-2 cross-axis verify) | §VII.AJ.W4-1 stays at Stage-1; FAILing clauses route to S89 remediation (per joint-theorem-promotion.md Stage-2 → 3 promotion blocked) |
| §W8-100 user-deferral | rule-file collision unresolved; orchestrator emits PRE-REG-INC for #100; carry-forward to S89 with policy-decision queued at session-start |

## Wave 8 Machinery-Enumeration Pin (§0.11 PRDR)

| Gate | Free Parameters | Source / Pin |
|:-----|:---------------|:-------------|
| §W8-87 | NONE | rule-file edit; verbatim text |
| §W8-88 | NONE | rule-file edit; verbatim text |
| §W8-89 | NONE | rule-file edit + Stage-2 PASS-AND coordination |
| §W8-90 | L_max=10 (Casimir-bound canonical), partition_tol=1e-12 | `math-scripts.md §"D_K Block-Diagonality"`; pre-registered tolerance |
| §W8-91 | NONE (deterministic count from #90 tags) | derived from #90 NPZ output |
| §W8-92 | NONE (3-instance corpus pre-verified) | rule-file edit; verbatim text |
| §W8-93 | N=18 (matched §VII.AJ.W4-1 18-cell), ansatz `π·sin(2π·c/N)·(eig_c/λ_min)`, axiom_eps_threshold=1e-12, drift_threshold=1e-2 | pinned per anchor; ansatz form pinned per convention-shopping prevention |
| §W8-94 | NONE | canonical_constants.py edit; verbatim dict |
| §W8-95 | NONE (Stage-2 protocol pre-specified) | joint-theorem-promotion.md §"Stage 2" |
| §W8-96 | NONE (SHA comparison deterministic) | `canonical_constants.py` provenance entries |
| §W8-97 | NONE | registry-row rename; verbatim |
| §W8-98 | NONE (deterministic branch on trigger) | conditional on §W8-93 OR §W8-89+§W8-90 |
| §W8-99 | NONE | deterministic K-count from #98 |
| §W8-100 | user adjudication pinned at decision time | rule-file edit policy decision |

**Methodology-wave-allowlist append-only rows pinned at plan-freeze** (per `wave-classification.md §M4`):

| gate_id | session | rationale | sha256_of_plan_block |
|:--------|:--------|:----------|:---------------------|
| W8-87 | S88 | S88-CONSENSUS-INDEPENDENCE-TEST-LANDING | pending |
| W8-88 | S88 | S88-CROSS-PILLAR-BRIDGE-ANATOMY-SCHEMATIC-LAYER-DISTINCTION-LANDING | pending |
| W8-89 | S88 | S88-MECHANICAL-CLOSURE-DISCIPLINE-LAYER-SEPARABILITY-CARVE-OUT-CLAUSE | pending |
| W8-92 | S88 | S88-OPERATOR-PROJECTION-READING-A-RULE-PROMOTE | pending |
| W8-94 | S88 | S88-CHANNEL-LABEL-NORMALIZATION | pending |
| W8-97 | S88 | S88-CF-28-ORPHAN-FNL-PATHWAY-REGISTRY-UPDATE | pending |
| W8-100 | S88 | S88-VERDICT-PERMANENCE-VS-SIG5-RULE-COLLISION-RESOLUTION | pending |

Pending SHAs computed at S88 plan-freeze final pass per `methodology-wave-allowlist.md §"Pending SHA resolution"`.

## Wave 8 Input-SHA Ledger

Pinned at S88 plan-freeze (final pass; SHA values populated by orchestrator at plan-freeze completion):

| File | Purpose | SHA pin |
|:-----|:--------|:--------|
| `.claude/rules/cross-pillar-bridge-anatomy.md` | §W8-87, §W8-88 substrate edit target | pending |
| `.claude/rules/mechanical-closure-discipline.md` | §W8-89 substrate edit target | pending |
| `.claude/rules/methodology-wave-allowlist.md` | §W8-87 through §W8-100 allowlist append target | pending |
| `.claude/rules/registry-landing.md` | §W8-92 substrate edit target | pending |
| `.claude/rules/gate-verdicts.md` | §W8-100 substrate edit target | pending |
| `.claude/rules/v3-closure-recovery.md` | §W8-100 substrate edit target | pending |
| `.claude/rules/joint-theorem-promotion.md` | §W8-89, §W8-95 protocol reference | pending |
| `.claude/rules/epistemic-discipline.md` (§"Layer-Decomposition") | §W8-89 layer-functor F reference | pending |
| `computations/canonical_constants.py` | §W8-94, §W8-96 substrate edit + reference | pending |
| `sessions/permanent-results-registry.md` (§VII.AJ.W4-1, §VII.AG.1, §VII.AF.1) | §W8-87, §W8-88, §W8-95 reference | pending |
| `sessions/framework/registry/f-nl-folded-pathway-registry.md` | §W8-97 substrate edit target | pending |
| `computations/s84_spectrum_cache_L12_tau019.npz` | §W8-90, §W8-93, §W8-95 master spectrum | pending |
| `sessions/archive/session-87/session-87-results-workingpaper.md` (§W4-2 line 3717) | Type-F partition definition reference | pending |
| `feedback_rules-compensate-missing-structure.md` | §W8-89, §W8-92, §W8-99 K=3 promotion threshold | pending |

All file SHAs computed via `sha256sum` at plan-freeze final pass; verdict-line `audit_sha256` per gate is `closure_hash(input_pin_map)` per `computations/script-template.py append_verdict()` protocol.
