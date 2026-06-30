# Seed file — sessions/archive/session-86/session-86-w4-workingpaper.md

**Date**: 2026-04-26
**Investigator**: phonon-first-cosmologist
**Source WP**: `sessions/archive/session-86/session-86-w4-workingpaper.md` (572 lines read in full)

## Reading summary (orientation for the consolidator)

W4 closed three gates that all sit at the regulator-class adjudication seam between substrate spectral content and Mellin/heat-kernel summation prescriptions:

- **§W4-1 P4 `S86-BRANCH-IV-FORMULATION-COMMIT`** — PASS (line 112; FAIL line 110 retained as W1c-8 publication-precision audit-trail). Retired R_JE; canonicalized two distance-tagged spectral diagnostics: `R_JK = 0.00803460529503449` (distance-2, M_KK^{−2}, Newton-constant slot) and `xi_E_GGE_inv = 13.642473425595973` (distance-1, M_KK^{+1}, GGE residue). Both at full float64 in `canonical_constants.py` SECTION E.B; framework file `branch-iv-canonical.md` created. Dimensional rescaling CC PASS at machine-epsilon (M_KK→2M_KK gives 0.25 exact for R_JK and 2.0 exact for xi_E_GGE_inv). Unlocks W5a P3 `S86-SECTOR-1-SR-FLOW-Z-FACTOR` ξ²(0) IC.

- **§W4-2 P5 `S86-SECTOR-2-MELLIN-KERNEL-K-INVARIANT`** — FAIL. The substrate Mellin-kernel residue at s=3 (d_spec=8 NCG) is NOT regulator-class invariant on the live atlas A_5 = {ζ, Zubarev, SDW, cutoff_sqrt, anomaly}. `max_pair_ratio = 9.240e-01` at (ζ, Zubarev), three OOM above PASS 1e-3. Per-regulator residues: M_ζ = M_SDW = 1.581e-01; M_Zubarev = 1.201e-02; M_cutoff_sqrt = 1.110e-01; M_anomaly = 3.185e-02. CC-3 counterexample probe FAILed on Zubarev (rel_deriv = 6.98 vs tolerance 1e-4) — the heat-kernel regulator carries explicit τ-dependence at the s=3 residue level. CC-2 PASSed at machine-epsilon (rel_err = 1.7556e-16) but only because zeta = Mellin on positive-definite Casimir spectra (definition-level identity, not invariance). Mellin-cone live-vs-fallback flag: `mellin_cone_live = False` (W2 C9/C10 not yet landed); fallback = direct heat-kernel truncation per S85 W2-5. Helpers acknowledged SCHEMATIC, not full Connes-Chamseddine 1996 §2.2-2.3 multipliers. Forces SECTOR-2 to split into per-regulator distance tags at the registry level.

- **§W4-3 C28 `S86-W-4-CUTOFF-SQRT-ADJUDICATION`** — INFO (REQUIRES-S86-GATE). Captures S85 W4 connes×lizzi 3-round workshop convergence into registry. Created `sessions/framework/registry/cutoff-sqrt-adjudication.md` (369 lines, 6 sections, 3 PRDR-grade pre-registered S86+ gates). Atlas state: A_5 PENDING with cutoff_sqrt PENDING-EVENT. Three new gates registered for S86+ dispatch: GATE A `S86-CUTOFF-SQRT-GATE-A-LMAX-FINITENESS` (master; expected FAIL per R3-C-E3-C structural pre-determination — Peter-Weyl L^8/960 mode-count growth at d=8 spectral dimension implies α = −k_eff/4 < 0 for every k_eff ∈ [5.09, 8]); GATE B `S86-CUTOFF-SQRT-GATE-B-KERNEL-ADMISSIBILITY` (subset-removal sweep on a_0 slot under W2-1 protocol); GATE C `S86-CUTOFF-SQRT-GATE-C-S82-APPLICABILITY` (HBW / MP-abs-conv at s=6 on framework-truncated f_6 = 0.1 residue). Permanent methodology gain: **LAYER 1 vs LAYER 2 taxonomy** (combinatorial-position-on-atlas vs admissibility-on-axioms; R3-C-E3-L deliverable) repairing S78-onward 5-atlas conflation. C45 S87 sixth-regulator-synthesis stays DEFERRED.

The wave is structurally mixed: one canonicalization, one structural FAIL forcing a downstream registry split, one INFO converting workshop deferral into pre-registered numerical contest. The synthesis itself flags two PRU Class 8 carry-forwards (publication-precision pre-registration; plan-template wording for collision-check MCP) but no other items are explicitly carry-forwarded for next-session dispatch.

## Candidates

### Candidate 1 — SECTOR-2 per-regulator split — taxonomy ratification + downstream re-evaluation

**What it would do**: Take the structural FAIL of K-invariance on A_5 and produce the formal registry split: SECTOR-2 → {SECTOR-2-ζ, SECTOR-2-Zubarev, SECTOR-2-SDW, SECTOR-2-cutoff_sqrt, SECTOR-2-anomaly}, each with its own substrate-distance tag derived from where its M_R(s=3) sits relative to the F_2 ζ=SDW machine-epsilon class. The workshop adjudicates: (a) which sub-classes fall into the same equivalence class (the 4-class partition implied by §W4-2 results: F_2 = {ζ, SDW}, then {cutoff_sqrt}, then {anomaly}, then {Zubarev}); (b) whether substrate-distance is itself regulator-class-relative (a methodological claim that breaks the S78-onward "single-atlas-distance" framing); (c) which downstream observables are legitimately substrate-property vs regulator-property under the split. Output: a registry document `sessions/framework/sector-2-per-regulator-split.md` with the 4-class partition, its derivation from §W4-2 Step 3 (pole_R = a_2 · M_R(s=3)), and the propagation map into W5a P3 IC, W6 perturbative-immunization C-α/β/γ, and the LAYER 1 vs LAYER 2 taxonomy from C28.

**Why it's worthwhile**: The W4 synthesis §4 row "SECTOR-2 taxonomy" explicitly carries this forward without dispatching it. The FAIL is structural (3 OOM above threshold; not a numerical near-miss), so the split is forced — but there is no current registry document defining the per-regulator distance tags. Without it, downstream gates (W5a P3 ξ²(0) IC, W6 perturbative-immunization corollaries) inherit an undefined splitting. This is exactly the S78-onward conflation that C28's LAYER 1/LAYER 2 taxonomy was supposed to repair; W4-2's FAIL provides the first numerical instance where the repair must be applied. Without a workshop adjudicating the partition, the next-session planner has to guess which equivalence relation governs SECTOR-2.

**Type**: 2-agent workshop

**Suggested agents**: lizzi-spectral-functional-theorist (primary; Mellin-kernel pole structure home domain; ran §W4-2), connes-ncg-theorist (cross-cite — Connes-Chamseddine 1996 §2.2-2.3 Mellin-multiplier formalism is the source for the regulator-class structure)

**Rounds (workshops only)**: 3 (R1 each agent steelmans their preferred partition: Lizzi argues from F_2/F_4-class taxonomy, Connes from full 5-class partition; R2 each responds to the other's structural objections; R3 converge on a binding 4- or 5-class registry partition with explicit propagation map)

**Context the workshop will need**: §W4-2 Step 3 substitution chain (pole_R = a_2·M_R(s=3)); the 5 numerical pole values with regulator-tagged decomposition; CC-2 machine-epsilon ζ=SDW identity (lines 192-198 of WP); CC-3 Zubarev counterexample probe (line 196); the W4 synthesis §4 "SECTOR-2 taxonomy" cascade row; C28 LAYER 1 vs LAYER 2 taxonomy (lines 511, 547); the existing `_spectral_action_regulators.py` schematic helpers + the explicit honesty disclosure that they are SCHEMATIC not Connes-Chamseddine 1996 full physical regularizations (line 503); the regulator-specific scales identified in §W4-2 (Zubarev t_ref, cutoff_sqrt cutoff_frac at 0.7·C_max, Pauli-Villars M_PV² at 0.1·C_max; line 248-249 + line 292 of WP).

---

### Candidate 2 — Mellin-cone live-path re-run of K-invariant on A_5 (sub-wave audit)

**What it would do**: Build (or import once W2 C9/C10 land) the live Mellin-cone infrastructure (`from analytic_zeta import analytic_zeta`) and re-run the K-invariant test with full physical Mellin-Barnes regulators rather than the schematic helpers in `_spectral_action_regulators.py`. The sub-wave audit specifically tests whether the FAIL is regulator-class structural (predicted: yes, Zubarev's τ-dependence is not infrastructure-dependent) or schematic-helper-artifact (predicted: no). Includes: (i) port helpers to the live Mellin-cone path; (ii) re-evaluate the 5 pole_R values; (iii) re-compute max_pair_ratio + counterexample probe; (iv) produce a verdict on whether the §W4-2 FAIL replicates with the live infrastructure.

**Why it's worthwhile**: The W4 synthesis §2 explicitly calls this out: "A live-Mellin-cone re-run is the obvious sub-wave audit; it would not change the structural finding (Zubarev's τ-dependence is the dominant violator and is regulator-class, not infrastructure-dependent)." The honesty disclosure in line 503 ("`_spectral_action_regulators.py` helpers are SCHEMATIC analogs of Connes-Chamseddine 1996 §2.2-2.3 multipliers") is a known caveat on the FAIL verdict. The §W4-2 FAIL drives the SECTOR-2 split (Candidate 1), the W5a P3 IC inheritance, and the W6 corollary re-evaluation; if the FAIL is sustained under live-physical regularization, the structural finding is permanent; if it is helper-artifact-dependent, the cascade unwinds. This is a single-shot binary decisive audit.

**Type**: solo (1 agent)

**Suggested agents**: lizzi-spectral-functional-theorist (Mellin Strip / Convergence Cone Theorem domain; ran §W4-2 with the schematic helpers; can audit the helper-artifact vs structural distinction)

**Rounds (workshops only)**: N/A (solo)

**Context the workshop will need**: The W2 C9/C10 status (whether `analytic_zeta` is now importable); the §W4-2 FAIL numerical pole values + decomposition pole_R = a_2·M_R(s=3); the schematic helper code in `computations/_spectral_action_regulators.py` (zeta_a_n, mellin_a_n, heat_kernel_a_n, hard_cutoff_a_n, pauli_villars_a_n); Connes-Chamseddine 1996 §2.2-2.3 Mellin-multiplier formalism; the §W4-2 substitution chain Step 3 (the structural prediction that a_2 is regulator-independent and only M_R(s=3) carries the regulator class). Pre-register: `S86-SECTOR-2-MELLIN-KERNEL-K-INVARIANT-LIVE-RERUN` with the same threshold (max_pair_ratio ≤ 1e-3 OR max_pair_abs ≤ 1e-6) and same 4 verdict directions (PASS reverses §W4-2; FAIL replicates §W4-2; INFO band; FAIL with regulator-class restructured).

---

### Candidate 3 — GATE A canonical-record dispatch (S86 master cutoff_sqrt gate)

**What it would do**: Dispatch `S86-CUTOFF-SQRT-GATE-A-LMAX-FINITENESS` (the master gate from C28's 3-gate apparatus) per the PRDR-grade machinery pin in `sessions/framework/registry/cutoff-sqrt-adjudication.md` §3.1. Test whether `f_0 · Λ(L_max)^4 · a_0(L_max)` admits a positive-α scaling Λ(L_max) = Λ_0·L_max^α (α ∈ [−2, +2]) such that the coupling is bounded as L_max → ∞ on Jensen-deformed SU(3). Inputs pinned: a_0(L_max) Peter-Weyl L^2(SU(3)) sum-of-dim^2 multiplicity (leading L_max^8/960; discrete anchors a_0(3)=12880, a_0(4)=50176, ..., a_0(10)=9785776); cutoff_AL2010 Mellin vector `(1/2, 1, 1, 0)` published or `(2, 1, 0.5, 0.1)` framework-truncated. Per W4-3 line 437: "the S86 GATE A dispatch is therefore canonical-record (logging the FAIL with input-pin closure-hash for the permanent registry), not adjudication."

**Why it's worthwhile**: GATE A is the structural MASTER of the joint outcome rule (line 432-435). The C28 INFO verdict explicitly registers GATE A as expected to FAIL "per R3-C-E3-C structural pre-determination — α = −k_eff/4 < 0 for every k_eff ∈ [5.09, 8]" (lines 437, 509). If GATE A FAILs, atlas A_5 collapses to A_4 = {ζ, Zubarev, SDW, anomaly}; cutoff_sqrt is removed; C45 S87 sixth-regulator-synthesis is promoted (line 520). If GATE A PASSes, the contest moves to GATE B+C and cutoff_sqrt's canonical status is decided by inner-fluctuation lift / HBW conditional. This is the single most consequential atlas-cardinality determinant in the framework's regulator-class taxonomy. The plan §3.1 is PRDR-grade and the gate is "runnable" today (machinery pinned). Treating it as canonical-record is the right framing — but it still needs to land into the verdict registry to discharge the C28 INFO state.

**Type**: solo (1 agent)

**Suggested agents**: connes-ncg-theorist (primary; CC-2010 axioms domain; was R3 closer of S85 workshop where the structural pre-determination R3-C-E3-C was established)

**Rounds (workshops only)**: N/A (solo)

**Context the workshop will need**: `sessions/framework/registry/cutoff-sqrt-adjudication.md` §3.1 (full PRDR machinery pin for GATE A); the R3-C-E3-C structural pre-determination (Peter-Weyl L^8/960 mode-count growth at d=8 spectral dimension implies α = −k_eff/4 < 0 for every k_eff ∈ [5.09, 8]); the discrete a_0(L_max) anchors (lines 422 of WP); cutoff_AL2010 Mellin vector candidates (1/2, 1, 1, 0) [published] vs (2, 1, 0.5, 0.1) [framework-truncated]; the joint-outcome rule from C28 (line 432-435); pre-register as `S86-CUTOFF-SQRT-GATE-A-LMAX-FINITENESS` with the explicit PASS/FAIL/INFO directions from §3.1. Note: PROHIBITED_ACTIONS includes iterate-until-PASS, so the structural pre-determination of FAIL must be honored if the computation lands FAIL; this is canonical-record, not adjudication.

---

### Candidate 4 — GATE B (kernel admissibility) + GATE C (S82 applicability) joint dispatch

**What it would do**: Dispatch `S86-CUTOFF-SQRT-GATE-B-KERNEL-ADMISSIBILITY` (subset-removal sweep on a_0 slot under W2-1 protocol; tests {dim, fin} vs {reg, 1st-order} sourcing) and `S86-CUTOFF-SQRT-GATE-C-S82-APPLICABILITY` (HBW / MP-abs-conv at s=6 on framework-truncated f_6 = 0.1 residue specifically — NOT the unregulated kernel which was retracted under R2-A-CONV-(a)) together. Per the joint outcome rule, these are conditional on GATE A PASS — but the C28 framing calls for canonical-record landing of the full apparatus regardless of GATE A outcome.

**Why it's worthwhile**: GATE B and GATE C complete the C28 3-gate apparatus. If GATE A is dispatched as canonical-record (Candidate 3) and FAILs (the structural prediction), B and C become moot for cutoff_sqrt's atlas membership but remain meaningful as taxonomic tests of how cutoff_AL2010 sits relative to the LAYER 2 admissibility axioms — they decide whether cutoff_sqrt's exclusion is clean (FAIL on dim/fin alone), structurally inner-fluctuation-related (FAIL on reg / 1st-order), or HBW-positive-cone-related (FAIL on f_6 residue MP-abs-conv). The C28 framing line 502 + 520 indicate the cascade depends on which GATE actually closed the case. Without B+C, the LAYER 2 admissibility audit is incomplete even after GATE A lands.

**Type**: solo (2 agents) — independent dispatches in parallel

**Suggested agents**: connes-ncg-theorist (GATE B; CC-2007 axiom set + subset-removal protocol domain); lizzi-spectral-functional-theorist (GATE C; HBW / MP-abs-conv at s=6 + Mellin Strip / Convergence Cone Theorem domain)

**Rounds (workshops only)**: N/A (solo dispatches)

**Context the workshop will need**: `sessions/framework/registry/cutoff-sqrt-adjudication.md` §3.2 (GATE B PRDR machinery pin: scheme `subset-removal-sweep`, convention `W2-1-protocol-on-a0-slot`, L_max=7); §3.3 (GATE C PRDR machinery pin: scheme `MP-abs-conv-s6`, convention `f_6=0.1-residue`, L_max=3); CCM-2007 axiom set {dim, reg, fin, real, 1st-order, orient, PD}; W2-1 subset-removal protocol; framework Mellin vector `(2, 1, 0.5, 0.1)` with f_6 = 0.1 residue; HBW positive cone definition; the explicit caveat from C28 line 426 that GATE C tests the framework-truncated residue NOT the unregulated kernel (R2-A-CONV-(a) citation correction). Both gates carry pre-registered PASS/FAIL/INFO directions in the framework file.

---

### Candidate 5 — Publication-precision pre-registration rule promotion to plan-template MANDATORY

**What it would do**: Take the second independent witness of the publication-precision rule (W4-1 P4 dual-verdict line 110 FAIL → line 112 PASS; the canonical entry was initially registered at presentation precision, Stage-4 anchor consistency at rel_tol=1e-12 surfaced rel_diff > 0; fix was re-pin at full float64) and elevate the rule from "follow-up surface" status to MANDATORY plan-template machinery-pin checklist item. Update `.claude/templates/pru-pre-registration-template.md` to require `_published_sig_figs` declaration alongside any value pinned downstream. Update `.claude/rules/epistemic-discipline.md` §"Publication-Precision Pre-Registration" to register the second witness and convert the rule from forward-looking advisory to plan-freeze MANDATORY (severity S1).

**Why it's worthwhile**: The W4 synthesis §5 explicitly calls this out: "Two plan-time machinery-pin gaps surfaced as PRU Class 8 carry-forwards: publication-precision pre-registration (P4 dual-verdict witness; same pattern as S86 W1c-8) and plan-template wording for canonical-collision-check MCP semantics (P4 self-corrected). Both have explicit fix-now remediations available; the wave synthesis flags them for the next plan-template revision rather than deferring." The S86 W1c-8 surface registered the rule as forward-looking (rule text in `epistemic-discipline.md` §"Publication-Precision Pre-Registration"). W4-1 P4 produces the second independent witness in a structurally distinct sub-domain (canonical-constant registration vs n_s downstream comparison). Two witnesses across distinct sub-domains is the threshold for promoting a rule from advisory to MANDATORY (analogous to how S86 W2-4 cluster-span FAIL canonicalized the |ratio−2| metric). The W4 synthesis recommends fix-now via plan-template revision; this is the dispatch that does that.

**Type**: solo (1 agent)

**Suggested agents**: gen-physicist (rule-author / plan-template-revision domain; not a physics-content gate but a machinery-discipline gate)

**Rounds (workshops only)**: N/A (solo)

**Context the workshop will need**: The current rule text in `.claude/rules/epistemic-discipline.md` §"Publication-Precision Pre-Registration"; the W1c-8 first-witness provenance (S86 W1C-C29-FOLLOWUP-NS-OF-CSUB-PROMOTION, 2026-04-26); the W4-1 P4 second-witness provenance (line 495 of WP: "W1c-8 thus has a second independent witness in S86; the underlying plan-time gap (publication precision unpinned in plan §W4-1 STEP 3) is now structural carry-forward"); the dual-verdict line trace (line 110 FAIL + line 112 PASS in `computations/s86_gate_verdicts.txt`); the PROHIBITED_ACTIONS Class 2 audit verifying value/scheme/convention/L_max identity across both lines (line 495 of WP: "value/scheme/convention/L_max identical across both lines; only canonical-pin precision changed"); plan-template at `.claude/templates/pru-pre-registration-template.md`. Output: rule-text update + plan-template machinery-pin checklist update + audit-script update.

---

### Candidate 6 — LAYER 1 vs LAYER 2 taxonomy retroactive sweep

**What it would do**: Apply the LAYER 1 (combinatorial-position-on-atlas) vs LAYER 2 (admissibility-on-axioms) taxonomy from C28 (line 511, 547) retroactively to all S78-onward regulator-class statements in the project's framework files, working papers, and canonical constants. Per C28 line 511: "This permanently repairs the S78-onward conflation that treated the canonical 5-atlas as uniform-admissible." The sweep identifies every place where a regulator's combinatorial position (Mellin support, observable-cross-classification) was conflated with its axiomatic admissibility (CCM-2007 GATE A/B/C tests), produces the corrected per-regulator tagging, and lands an audit document `sessions/framework/registry/layer1-layer2-retroactive-audit.md` with the full inventory.

**Why it's worthwhile**: C28 registered LAYER 1 vs LAYER 2 as a permanent methodology gain (constraint-map line 547 of WP). The C28 framework file `cutoff-sqrt-adjudication.md` §3.4 + §6 hold the prospective registration. But the retroactive application across S78-S85 work is not yet done. The constraint-map row line 547 says "All S86+ regulator-class statements MUST tag combinatorial-position vs axiomatic-admissibility separately" — this is forward-looking discipline. The retrospective audit would inventory which prior closures, theorems, and gates conflated the two layers and need re-tagging. Without it, the framework carries S78-onward regulator-class statements that are unevaluated under the new taxonomy.

**Type**: solo (1 agent)

**Suggested agents**: lizzi-spectral-functional-theorist (the R3-C-E3-L taxonomy author; lizzi-track home domain spans Mellin-Strip / Convergence-Cone / ZETA-NOT-PHYSICAL-75 which all fall under LAYER 1 vs LAYER 2 distinctions)

**Rounds (workshops only)**: N/A (solo audit)

**Context the workshop will need**: `sessions/framework/registry/cutoff-sqrt-adjudication.md` §3.4 + §6 (LAYER 1 vs LAYER 2 taxonomy primary registration); the workshop quote E3-L lines 1255-1269 of `s85-w4-cutoff-sqrt-status.md` (verbatim taxonomy definition); ZETA-NOT-PHYSICAL-75 origin (S82 W2-3) as a LAYER 2 closure; the 5-regulator atlas convention origin S78+; existing entries in `sessions/permanent-results-registry.md` for regulator-class statements; the `mcp__knowledge__list_classes` + `mcp__knowledge__query_class` queries to enumerate prior regulator-class theorems; the Regulator-Family Boundary Theorem `Phi_r(nu_i) = M(r) · Phi_zeta(nu_i)` (line 315 of WP) as a LAYER 1 structural identity that needs re-tagging.

---

### Candidate 7 — W5a P3 SR-flow Z-factor IC propagation under per-regulator splitting

**What it would do**: Re-evaluate the W5a P3 `S86-SECTOR-1-SR-FLOW-Z-FACTOR` initial condition ξ²(0) = `xi_E_GGE_inv` (Candidate 1's per-regulator splitting forces SECTOR-2 propagation upstream into Sector-1's IC). Per W4-1 line 113: "W5a P3 dispatch should `from canonical_constants import xi_E_GGE_inv` and consume directly." Per W4 synthesis §4 line 518: "W6 perturbative-immunization corollaries C2 / C-α/β/γ inherit per-regulator splitting; W5a P3 IC inherits per-regulator structure if SECTOR-2 split propagates upstream." This workshop adjudicates: (a) does W5a P3 IC inherit per-regulator splitting (5 ICs, one per regulator class)? (b) is xi_E_GGE_inv itself a substrate-distance-1 quantity that should split per the SECTOR-2 partition? (c) what is the canonical SR-flow trajectory under each per-regulator IC?

**Why it's worthwhile**: W4-1 P4 passed and explicitly unlocked W5a P3. But §W4-2's K-invariant FAIL means substrate-distance-1 quantities are NOT regulator-class invariant on A_5. This creates a tension: xi_E_GGE_inv is registered as canonical (single-valued, full float64) but the K-invariant FAIL implies the s=−1 spectral residue is regulator-dependent at the same structural level as the s=3 residue. Either (i) xi_E_GGE_inv at s=−1 IS regulator-invariant (different from s=3) and the FAIL doesn't propagate; or (ii) xi_E_GGE_inv inherits per-regulator splitting and the canonical entry needs revision; or (iii) the s=−1 vs s=3 distinction is structurally important and should be registered. Without resolving this, W5a P3 dispatch has an undefined IC state.

**Type**: 2-agent workshop

**Suggested agents**: transit-dynamics-theorist (primary; W4-1 owner; xi_E_GGE_inv canonical formulation home domain), lizzi-spectral-functional-theorist (cross-cite; Mellin-residue-structure home domain; ran §W4-2 K-invariant FAIL)

**Rounds (workshops only)**: 2 (R1 each agent steelmans whether xi_E_GGE_inv inherits per-regulator splitting; R2 converge on registry treatment)

**Context the workshop will need**: §W4-1 R_JK + xi_E_GGE_inv canonical entries and dimensional rescaling CC PASS at s=−1 (line 74-89 of WP); §W4-2 K-invariant FAIL at s=3 (line 108-198 of WP); §W4 synthesis §4 cascade row (line 518); `canonical_constants.py` SECTION E.B current entries; the s=−1 vs s=3 structural distinction in d_spec=8 NCG (s=d_spec/2−n: s=−1 is n=5, s=3 is n=1; structurally different Mellin residues); xi_E_GGE_inv = 59.8 × Delta_BCS / K_base anchor (line 29 of WP); the 3He-B parent→child inheritance template (line 117 of WP); the W6 perturbative-immunization corollaries C-α/β/γ that also inherit per-regulator splitting (line 502 of WP).

---

### Candidate 8 — ζ = SDW machine-epsilon identity — structural theorem registration

**What it would do**: Take the §W4-2 CC-2 PASS at machine-epsilon (rel_err = 1.7556e-16, lines 192-198) — "the structural identity (zeta = Mellin on positive-definite spectrum)" — and register it as a permanent structural theorem in the framework. The theorem statement: ζ-regularization and SDW (spectral density weighting / Mellin-on-positive-spectrum) regularization produce identical Mellin-residue values at s=3 in d_spec=8 NCG when applied to a positive-definite spectrum (such as the Casimir spectrum on Jensen-deformed SU(3)). The result holds at all Mellin-residue locations s = d_spec/2 − n for positive-definite spectra; it is a definition-level identity not a coincidence.

**Why it's worthwhile**: §W4-2 explicitly notes that the F_2 ζ=SDW pair was the only PASS-strict tight pair (line 163 of WP) and that this is "a structural identity (zeta = Mellin on positive-definite spectrum) and does not lift the K-invariance claim to even the F_4 = {ζ, Zubarev, SDW} sub-atlas" (line 290). The synthesis §2 line 532 reinforces: "The F_2 zeta=SDW machine-epsilon agreement is a definition-level identity (zeta = Mellin on positive-definite spectrum), not evidence; the framework cannot lean on it for a substantive K-invariance claim." Registering this as a permanent theorem (with proof + scope-of-validity statement) prevents the framework from accidentally citing the F_2 identity as evidence in future regulator-class arguments. It also strengthens Candidate 6 (LAYER 1 vs LAYER 2 retroactive sweep) by registering one structural identity that explicitly is NOT a LAYER 2 admissibility result.

**Type**: solo (1 agent)

**Suggested agents**: lizzi-spectral-functional-theorist (Mellin-on-positive-spectrum + ZETA-NOT-PHYSICAL-75 home domain)

**Rounds (workshops only)**: N/A (solo theorem-registration)

**Context the workshop will need**: §W4-2 CC-2 PASS detail (rel_err = 1.7556e-16, line 193 of WP); the substitution chain Step 3 decomposition pole_R = a_2 · M_R(s=3) where M_ζ = M_SDW (line 246 of WP); the explicit "F_4-class identity" annotation (line 246); ZETA-NOT-PHYSICAL-75 closed mechanism (S82 W2-3 origin) as the prior anchor on ζ admissibility; the positive-definiteness condition on the Casimir spectrum on Jensen-deformed SU(3); the Connes-Chamseddine 1996 §2.2-2.3 Mellin-multiplier formalism. Output: a 1-2 page theorem registration document with statement, scope-of-validity (positive-definite spectrum required), and explicit non-evidence-status declaration (the identity does NOT support any K-invariance or atlas-uniformity claim).

