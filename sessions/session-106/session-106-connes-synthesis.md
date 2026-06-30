# Session 106 Synthesis: §VII.AD Derivational-Anchor STRUCTURE-Tag Adjudication (SOURCE-DOUBLE-CITE-CO-PRIMARY vs PRIMARY + INDEPENDENT-CROSS-CHECK)

**Date**: 2026-06-13
**Agent**: connes-ncg-theorist (Workhorse-NCG)
**Source Documents**:
- `sessions/permanent-results-registry.md` §VII.AD (lines 16834–16891; §VII.AG.1 lines 14726–14736/14940–14950 read for bridge-map convention context only)
- `sessions/session-106/session-106-w4-workingpaper.md` §W4-2 (S106-VIIAD-STAGE2-VERIFY; Methodology block items (i)–(iv))
- `computations/session-106/s106_gate_verdicts.txt` line 74 (`S106-VIIAD-STAGE2-VERIFY` PASS; `audit_sha256=ac0bfe8034220fd49925937f1fc8cd1217ccf37cd9bc8efd5ba7eab0a160635c`)
- `computations/session-106/s106_w4_viiad_reviewer_vdd_axisA_verdict.json` (vdd Axis-A clause (c))
- `computations/session-106/s106_w4_viiad_reviewer_kitaev_axisB_verdict.json` (kitaev Axis-B clause (c))
- `.claude/rules/registry-landing.md` §"SOURCE-DOUBLE-CITE-CO-PRIMARY" + §"When PRIMARY+CONFIRMATION is wrong"

---

## I. Session Outcome

**STRUCTURAL VERDICT: (A) CO-PRIMARY CONFIRMED.** The registered §VII.AD STRUCTURE tag `SOURCE-DOUBLE-CITE-CO-PRIMARY` is correct as-written; **no registry tag edit is required.** The decidable predicate that separates the two readings — *does kitaev's generic-(c0,c1,c2,c3)-QQ symbolic proof independently reproduce the localization formula WITHOUT consuming the vdd V_input Schur factorization?* — resolves to **NO**. The C-route (exhaustive/generic-QQ enumeration) **enumerates over** the faithful-V_4-bijection domain whose very definition (a unique (−1,−1) stratum, so that `4·c_{σ⁻¹((−1,−1))}` is well-posed) is fixed by the V_input per-element Schur identity `[1−σ₁][1−σ₂] = 4·1_{σ₁=σ₂=−1}`. The C-route therefore consumes the V-route mechanism as a structural premise: the dependence is **sequential and non-fungible**, not parallel. The §VII.AD STAGE-3-PERMANENT promotion (S106 W4-2, gate `S106-VIIAD-STAGE2-VERIFY`, both reviewers PASS all clauses {a,b,c}) is **UNAFFECTED** either way — this is a `registry-landing.md` anchor-structure classification review of an already-proven identity, not a theorem down-tag. Classification of the adjudicated object: **GEOMETRIC** (a V_4 group-cocycle localization identity on the substrate's bot-20 D_K cardinality vector).

---

## II. Key Results

### II.1 — The decidable predicate resolves NO: the C-route consumes the V Schur mechanism

**Result**: The C_output enumeration's target formula `Δ_0 = 4·c_{σ⁻¹((−1,−1))}` is well-posed **only** on the faithful-V_4-bijection domain; that domain is fixed by the V_input per-element Schur localization, which the enumeration presupposes rather than derives. **Classification: GEOMETRIC.**

The detection criterion of `registry-landing.md` §"When PRIMARY+CONFIRMATION is wrong" is explicit: *"If two anchors independently reproduce the same conclusion via DIFFERENT routes (parallel, not sequential), use PRIMARY + INDEPENDENT-CROSS-CHECK instead."* The discriminator is therefore a single boolean — **parallel-route independence**. I tested it at the mechanism level (Sage QQ, exact):

1. The per-stratum factor `[1−σ₁(i)][1−σ₂(i)]` evaluated at the four Klein values is `{(+,+):0, (+,−):0, (−,+):0, (−,−):4}` — it equals 4 **only** at the `(−,−)` element and 0 elsewhere. This is an identity on **each** stratum, *prior to any summation, partition assignment, or enumeration*. This per-element collapse IS the V_input/Schur content (ANCHOR-1, registry lines 16848–16857).

2. The rhs the C-route certifies, `4·c_{σ⁻¹((−1,−1))}`, is **undefined unless there is a unique (−1,−1) stratum**. My Sage check on a non-faithful labeling (strata 0 and 1 both carrying `(−,−)`) returns the alternating sum `4c₀+4c₁` (two surviving terms) while the rhs `4·c_{unique (−,−)}` has no referent — the formula's domain collapses to faithful bijections exactly. kitaev independently confirmed this in his own clause (b) rationale: he verified over all 256 (σ₁,σ₂) assignments that the "unique (−1,−1) stratum" precondition holds **iff** the assignment is a faithful V_4 bijection, and that the S88 anchor's apparent mismatch (`delta_0_formula_QQ=8`, `cc2_delta_0_match=False`) arises *only* for non-faithful labelings "OUTSIDE the theorem's stated domain."

3. Therefore: kitaev's generic-(c0,c1,c2,c3)-QQ symbolic proof (all 24 faithful bijections give `lhs−rhs=0` exact in QQ — reproduced here independently) is a **stronger certification** (it covers all rational partitions, subsuming the substrate-specific 576-instance sweep at (2,4,8,6)), but it is **not a parallel derivation of the localization mechanism**. It enumerates over the Schur-fixed faithful-bijection domain. Remove the V-leg and the C-route loses the structural reason why the formula is well-posed and why exactly one term survives — it degrades to (in vdd's words) "an unexplained finite enumeration." **Parallel-route independence boolean = FALSE.**

**Structural implication**: FALSE on the parallel-route boolean is precisely the SOURCE-DOUBLE-CITE-CO-PRIMARY condition. The two anchors are sequentially dependent (mechanism → exhaustive certification) and non-fungible (neither reproduces the conclusion alone). CO-PRIMARY is the correct tag.

### II.2 — The two reviewers' clause (c) verdicts both certify the V→A_F→C sequential dependence

**Result**: Despite their *opposite registry-text-tag instincts*, vdd (Axis-A) and kitaev (Axis-B) **agree on the load-bearing structural fact**: V_input→A_F is the necessary structural premise of the chain. **Classification: GEOMETRIC (methodology adjudication of a GEOMETRIC theorem's anchor structure).**

The apparent divergence is shallower than it looks once read against the decision criterion:

- **vdd Axis-A clause (c) = PASS, with an "INFO inside a PASS" reservation.** vdd's narrow clause-(c) certification ("is V_input→A_F the NECESSARY STRUCTURAL PREMISE?") is "answered YES unambiguously." His reservation — that from a *pure NCG-axiomatic standpoint* the factorization "is ITSELF already a complete exact-QQ proof... so an arguably-more-precise tag is PRIMARY (V) + INDEPENDENT-CROSS-CHECK (C)" — is a hypothesis that the two routes are *plausibly* parallel. vdd explicitly flagged it as non-load-bearing: *"both the CO-PRIMARY and the PRIMARY+CROSS-CHECK readings retain the V_input→A_F leg as a necessary structural premise, which is the only thing clause (c) asks me to certify; the CO-PRIMARY-vs-CROSS-CHECK tag is a registry-structure-classification refinement, recorded here as INFO inside a PASS, not a clause-(c) failure."* vdd's reservation is *about the C-route's standing*, not about the V-route — and it is exactly the reservation the §II.1 predicate test adjudicates against: the C-route is not parallel, because its target formula is Schur-domain-bound.

- **kitaev Axis-B clause (c) = PASS, taking the opposite reading explicitly.** kitaev: *"a mechanism statement alone does not discharge closure over the full discrete domain of 24 faithful characters × 24 orderings... C_output cannot stand alone (a finite numerical/Sage sweep carries no structural NCG derivation), and V_input cannot stand alone (a mechanism is not exhaustive certification); both must remain accessible... NOT PRIMARY+CONFIRMATION (the anchors do not independently reproduce the conclusion via parallel routes; the certification is downstream of the mechanism)."* This is the direct statement of the §II.1 conclusion.

The two readings are reconciled by the predicate, not split by it. vdd's reservation rests on the premise "the V factorization is *itself* already a complete proof, so the C enumeration is a *parallel* independent check." But the C enumeration's deliverable is not "the localization holds" in the abstract — it is "the localization holds *EXACT in QQ over the faithful-bijection domain, for all rational partitions*." That deliverable is **constructed on top of** the Schur-fixed domain; it is downstream, not lateral. Once the parallel-route premise is tested (and fails, §II.1), vdd's own clause (c) text retains V→A_F as necessary premise — which is the CO-PRIMARY structure. **Both reviewers' clause (c) PASS rationales are consistent with verdict (A).**

### II.3 — Why kitaev's strengthening does NOT promote the C-route to PRIMARY

**Result**: A *stronger certification scope* (generic rational partitions vs the substrate-specific 576 instances) is not the same as *route independence*. **Classification: GEOMETRIC.**

The LOAD-BEARING FACT cited in the task — kitaev strengthened C_output to a generic-(c0,c1,c2,c3)-QQ symbolic proof over all 24 faithful V_4 bijections (WP §W4-2 Methodology item (ii)) — could superficially read as "the C-route now stands alone, so promote it to a co-equal PRIMARY of a parallel pair." It does not, for one structural reason: **the strengthening is along the partition axis (substrate-(2,4,8,6) → arbitrary QQ), not along the mechanism axis.** The generic-QQ proof still:

1. restricts to **faithful** bijections (Schur-domain), and
2. states the rhs as `4·c_{σ⁻¹((−1,−1))}` (the unique-(−,−)-stratum form),

both of which are the V_input Schur deliverable. The generic-QQ proof is best classified, in registry-landing terms, as a **stronger C_output anchor** (it subsumes the 576-instance sweep) that nonetheless **occupies the C-output leg of the same sequential chain**. It increases the chain's robustness; it does not convert the chain from sequential to parallel. The registry's existing wording ("V_input alone supplies the algebraic-identity premise... but does NOT establish the result EXACT in QQ for ALL (c,σ) combinations; C_output certifies the formula at all 576 instances", line 16864) survives the strengthening verbatim — only "576 instances" is now a *lower bound* on what C_output covers.

### II.4 — Detection-criteria 1–4 (CO-PRIMARY) all satisfied

**Result**: All four `registry-landing.md` §"Detection" criteria for SOURCE-DOUBLE-CITE-CO-PRIMARY hold; no cross-corner violation. **Classification: GEOMETRIC.**

| # | Detection criterion (`registry-landing.md §"Detection"`) | §VII.AD status | Source |
|:--|:---------------------------------------------------------|:---------------|:-------|
| 1 | **Sequential** — Anchor-2 (C_output) cannot be invoked without first invoking Anchor-1 (V_input) | **HOLDS**. C_output's target formula `4·c_{σ⁻¹((−1,−1))}` is Schur-domain-bound (§II.1); the unique-(−,−) precondition IS the V_input deliverable. | §II.1 Sage; kitaev clause (b)+(c) |
| 2 | **Non-fungible** — anchors cannot be swapped/reordered without breaking the chain | **HOLDS**. V alone = "unexplained finite enumeration" status loss (vdd); C alone = "no structural NCG derivation" (kitaev). | vdd clause (c); kitaev clause (c) |
| 3 | **Both anchors must remain accessible** — neither can be deprecated | **HOLDS**. Both reviewers state both legs must remain accessible. | vdd clause (c); kitaev clause (c) |
| 4 | **Both anchors on the SAME algebra-axis cell** (per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3) | **HOLDS — Corner-I, algebra-INVARIANT**. vdd: *"Both anchors sit on the SAME algebra-axis cell (algebra-INVARIANT / spectrum-combinatorial: both are exact counting identities on the stratum cardinality vector, neither a state-pair functional)."* No cross-corner SOURCE-DOUBLE-CITE-CO-PRIMARY violation. | vdd clause (c) |

Criterion 4 is the one that would force a HARD-HALT re-tag if violated (cross-corner co-primary structures are STRUCTURALLY FORBIDDEN). Both anchors are exact counting identities on the cardinality vector — both algebra-INVARIANT spectrum-only functionals (`F({λ_k, m_k}) = Σ_k m_k g(λ_k)` family), neither a state-pair functional. Same Corner-I cell. No violation.

---

## III. Gate Verdicts

This is a registry-classification review; the underlying Stage-2 gate verdict is authoritative and is NOT re-adjudicated here.

| Gate | Verdict | Decisive Number / Outcome |
|:-----|:--------|:--------------------------|
| `S106-VIIAD-STAGE2-VERIFY` (line 74; authoritative, not re-adjudicated) | **PASS** | composite PASS; JOINT(c)=CO-PRIMARY-chain-PASS-AND; both blind reviewers PASS {a,b,c}; `audit_sha256=ac0bfe80…` |
| §VII.AD STRUCTURE-tag adjudication (THIS review) | **(A) CO-PRIMARY CONFIRMED** | parallel-route-independence boolean = **FALSE** (C-route consumes Schur-fixed faithful-bijection domain; Sage QQ exact) |
| §VII.AD STAGE-3-PERMANENT status | **UNAFFECTED** | anchor-structure re-tag is `registry-landing.md` hygiene, not a theorem down-tag (verdict is "no edit") |

---

## IV. Structural Implications

**Constraint-map update — registry tag.** §VII.AD's `STRUCTURE: SOURCE-DOUBLE-CITE-CO-PRIMARY` tag is **CONFIRMED CORRECT**; the state does not change. The blind Stage-2 verify surfaced a *candidate* refinement (vdd's PRIMARY+INDEPENDENT-CROSS-CHECK reservation, WP §W4-2 item (i)); the adjudication **closes that candidate as NOT-ADOPTED** on the basis of the parallel-route predicate failing. This eliminates a registry-text-classification corridor: the §VII.AD anchor structure is not re-classifiable as parallel, because the localization formula's domain is mechanism-fixed.

**What this sharpens about the framework's cocycle-localization machinery.** The result is a clean instance of a recurring NCG pattern: a *factorization/Schur identity that fixes the support of a cocycle* is logically prior to *any exhaustive verification over that support*. The substrate IS the localization formula (per `phononic-framing.md` §"IS Space"); the formula's well-posedness flows `D_K eigenvalue degeneracy clusters → cardinality vector (c₁,…,c₄) → V_4 character algebra (Schur localization) → Δ_0 = 4·c_{σ⁻¹((−1,−1))}`. The C_output enumeration sits at the **end** of that arrow, certifying the QQ-exactness of the localized value; it does not sit *beside* the Schur step as an independent route. This is why the chain is CO-PRIMARY and not PRIMARY+CROSS-CHECK — and it is the substrate-first reading: the group-cocycle identity is fundamental, the exhaustive sweep is its emergent numerical readout.

**No structural wall opened or closed.** The identity itself (`Δ_0 = 4·c_{σ⁻¹((−1,−1))}` EXACT in QQ) was already proven and already STAGE-3-PERMANENT; this review touches only its anchor-citation classification. The substrate-IS V_4-on-strata incarnation remains characterized by its GROUP STRUCTURE (Klein-V_4 action on the 4-stratum partition), NOT by the vanishing of its parallelogram cocycle (registry "Solution-space implication", line 16891).

---

## ROUTED-TO-MACK (registry sole-writer per `feedback_mack-bridge-role.md`)

### (1) STRUCTURE-tag edit — **NONE REQUIRED**

The verdict is **(A) CO-PRIMARY confirmed**. The registry text at line 16864 already reads `**STRUCTURE**: SOURCE-DOUBLE-CITE-CO-PRIMARY (per .claude/rules/registry-landing.md §"Schema")`. **No before/after patch is needed for the structure tag** — the existing tag is correct as-written. The vdd PRIMARY+INDEPENDENT-CROSS-CHECK refinement candidate (WP §W4-2 item (i)) is recorded here as **closed NOT-ADOPTED**; no registry change follows from it.

*(If the orchestrator nonetheless wishes the registry to record that the Stage-2 verify examined and rejected the parallel-route reading, the minimal in-place annotation would append one sentence to the existing STRUCTURE paragraph at line 16864 — see optional annotation below. This is OPTIONAL hygiene, not a required edit; the tag itself stands.)*

**OPTIONAL annotation (append to the end of the STRUCTURE paragraph, line 16864, AFTER the existing sentence ending "...non-fungible and sequentially dependent (NCG-derivation premise → exhaustive verification)."):**

> Before (line 16864, terminal sentence):
> `NOT PRIMARY+CONFIRMATION because the two anchors are non-fungible and sequentially dependent (NCG-derivation premise → exhaustive verification).`
>
> After (append one sentence; CO-PRIMARY tag UNCHANGED):
> `NOT PRIMARY+CONFIRMATION because the two anchors are non-fungible and sequentially dependent (NCG-derivation premise → exhaustive verification). [S106 W4-2 Stage-2 verify examined and rejected a PRIMARY + INDEPENDENT-CROSS-CHECK re-tag (vdd Axis-A reservation, recorded INFO-inside-PASS): the C_output generic-(c0,c1,c2,c3)-QQ proof — though it subsumes the 576-instance sweep over ALL rational partitions — enumerates over the FAITHFUL-V_4-bijection domain whose unique-(−1,−1)-stratum precondition IS the V_input Schur deliverable, so the parallel-route-independence boolean is FALSE; sequential CO-PRIMARY confirmed; connes-ncg-theorist synthesis sessions/session-106/session-106-connes-synthesis.md §II.1.]`

This annotation is purely documentary (it records that the parallel-route alternative was tested and rejected). It does **not** change the tag, the theorem, or its STAGE-3-PERMANENT status. Apply only if the orchestrator wants the rejection auditable in the registry surface; otherwise the WP §W4-2 item (i) + this synthesis already carry it.

### (2) Legacy npz path-citation hygiene (WP §W4-2 item (iv)) — **ALREADY RESOLVED ON DISK; NO ACTION**

WP §W4-2 item (iv) flagged the §VII.AD block as citing the Sage cache at a bare legacy path `computations/s87_w11_hypercube_vertex_identity.npz`. **On verification at synthesis time this is already corrected on disk**: a `grep -n 'computations/s87_w11_hypercube' sessions/permanent-results-registry.md` over the live file returns **zero bare-path matches**, and the two §VII.AD citations (line 16861 "cached at..." and line 16877 "Sage callable cached SHA") both already read the canonical `computations/session-87/s87_w11_hypercube_vertex_identity.npz` form (per `gate-verdicts.md §"Canonical Verdict-File Path"`). The normalization appears to have landed at the same S106 plan-freeze hygiene pass that reconciled the §VII.AG.1 ratio annotation (registry line 14736). **No mack edit is required** — routing a fix for an already-correct path would inflate the queue with a non-actionable item (`CLAUDE.md` No Technical Debt; `feedback_fix-in-session-never-defer.md` no-padding clause). Recorded here only so the WP §W4-2 item (iv) observation is closed, not left dangling.

---

## V. Carry-Forward Computations

**No MATH carry-forward is required.** The decidable predicate (does kitaev's generic-(c0,c1,c2,c3)-QQ proof depend on the V_input Schur factorization or is it self-contained) was **resolved in-session** by the Sage QQ check in §II.1: the C-route's target formula `4·c_{σ⁻¹((−1,−1))}` is well-posed only on the faithful-bijection domain fixed by the Schur per-element localization, so the parallel-route-independence boolean = **FALSE** (self-containment is FALSE; the C-route DEPENDS on the V Schur mechanism as a structural premise). The optional fresh-Sage-QQ-independence-check carry-forward described in the task spec is therefore **discharged in-session, not carried forward** — its gate (parallel-route independence boolean) returned FALSE here at effort ≈ 0.10, below the 0.25 budget.

For completeness, the discharged item recorded in 4-field form:

```
V.1. [DISCHARGED IN-SESSION] Parallel-route independence of the C_output generic-QQ proof
   - What: test whether kitaev's generic-(c0,c1,c2,c3)-QQ symbolic proof reproduces the
           Δ_0 = 4·c_{σ⁻¹((−1,−1))} localization WITHOUT consuming the V_input Schur
           factorization [1−σ₁][1−σ₂] = 4·1_{σ₁=σ₂=−1} as a structural premise.
   - Inputs: s106_w4_viiad_reviewer_vdd_axisA_verdict.json + s106_w4_viiad_reviewer_kitaev_axisB_verdict.json
             + computations/session-87/s87_w11_hypercube_vertex_identity.npz (canonical session-87 path).
   - Gate: parallel-route independence boolean. PASS(parallel) ⇒ re-tag to PRIMARY + INDEPENDENT-CROSS-CHECK;
           FAIL(sequential) ⇒ CO-PRIMARY confirmed.
   - Effort: 0.25 (BUDGET); 0.10 (ACTUAL — Sage QQ, §II.1). RESULT: boolean = FALSE (sequential) ⇒
             CO-PRIMARY CONFIRMED. No further compute; no registry tag edit.
```

**Process item routed (NOT a CF; orchestrator/mack at session close):** the legacy-npz-path normalization in the §VII.AD block (ROUTED-TO-MACK item (2) above) — a registry-text-hygiene fix, in-session per `feedback_fix-in-session-never-defer.md`, independent of the structure-tag verdict.

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | Parallel-route-independence boolean = FALSE (Sage QQ exact) | GEOMETRIC | RESOLVED | C-route consumes Schur-fixed faithful-bijection domain ⇒ sequential, non-fungible |
| 2 | STRUCTURE-tag verdict: **(A) CO-PRIMARY confirmed** | GEOMETRIC | VERDICT | Existing registry tag correct; **no edit required** |
| 3 | vdd + kitaev clause (c) both certify V→A_F as necessary premise | GEOMETRIC | RECONCILED | Apparent tag-instinct divergence dissolves under the predicate; both consistent with CO-PRIMARY |
| 4 | kitaev generic-QQ strengthening is along partition axis, not mechanism axis | GEOMETRIC | NOTED | Stronger C_output anchor (subsumes 576 sweep), still the C-output leg of the SAME sequential chain |
| 5 | Detection criteria 1–4 all HOLD (incl. same-cell Corner-I) | GEOMETRIC | CONFIRMED | No cross-corner co-primary violation; criterion 4 (HARD-HALT trigger) satisfied |
| 6 | §VII.AD STAGE-3-PERMANENT | GEOMETRIC | UNAFFECTED | Anchor-structure review ≠ theorem down-tag; identity remains permanent |
| 7 | Legacy npz path citation (WP §W4-2 item (iv)) | GEOMETRIC | ALREADY-RESOLVED | Verified on disk: zero bare-path matches; lines 16861/16877 already `session-87/`. No edit; item closed, not padded into queue |
