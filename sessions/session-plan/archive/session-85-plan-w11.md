# Session 85 Plan — Wave W11: van-den-dungen-origin reviewer wave

**Owner**: van-den-dungen-bridge-theorist
**Wave ID**: W11
**Theme**: van-den-dungen-origin single-reviewer wave (Kasparov submersions, NCG factorization, shriek maps, cyclic-cohomology parity, categorical exclusion)
**Item count**: 5
**Output**: `sessions/session-plan/session-85-plan-w11.md`
**Verdict file** (canonical, per `.claude/rules/gate-verdicts.md`): `computations/s85_gate_verdicts.txt`
**Script prefix**: `s85_w11_`
**Generated**: 2026-04-21

---

## Wave W11 Summary

Five single-reviewer carry-forwards from the S84 vdd S-5 cohomology synthesis (`session-84-s5-vdd-cohomology-synthesis.md` §V) and upstream vdd-origin items in the collapsed carry-forward table (rows 33, 43, 52, 118, 120). Every gate lives inside the Kasparov-product factorization formalism (Paper 01, 1811.07824, Main Theorem) and its cohomological consequences (HP^*-parity, π_! shriek, non-flat base extension, categorical unification).

**Substrate framing** (mandatory, per `.claude/rules/phononic-framing.md`): Kasparov-product factorization and spectral-triple decomposition are not "mathematical machinery" sitting on top of the substrate — they are the substrate's native self-description. `D_K on Jensen-SU(3)` is the structure at each point; `[D] = [D_F] ⊗_{C(M)} [D_M]` is how that structure assembles into the emergent M^4 base. Every W11 gate probes what this decomposition actually preserves (parity, Pontryagin, shriek-action) or what it forbids (categorical exclusion walls).

| # | Gate ID | Theme | Effort (h) | Agent |
|:-:|:--------|:------|-----------:|:------|
| W11-1 | S85-EPSH-JENSEN-SURVIVAL | Heitsch 1-cocycle survival under Jensen τ-sweep (transverse sector) | 3–4 | van-den-dungen-bridge-theorist |
| W11-2 | S85-S5-CONVERGENCE-AUDIT | 3-way convergence audit (connes / lizzi / vdd S-5 solos) | 2–3 | van-den-dungen-bridge-theorist |
| W11-3 | S85-NCG-META-EXCLUSION-CERTIFY | Categorical unification of parity-exclusion (W10-114) and rank-exclusion (W2-3) | 6–8 | van-den-dungen-bridge-theorist |
| W11-4 | S85-FIBER-GROUP-PARITY-CLASSIFY | Shriek-map parity action for alternative fiber groups (SU(2), G_2, SO(3), Spin(5), SU(3)×U(1)) | 2–3 | van-den-dungen-bridge-theorist |
| W11-5 | S85-BASE-PONTRYAGIN-PARITY-PRESERVE | Submersion preservation under non-flat base — `p_1(TM^4)` on FRW-like base | 4–5 | van-den-dungen-bridge-theorist |

**Estimated total**: 17–23 agent-hours.

---

## Wave W11 Decision Point Prerequisites

- S84 vdd S-5 synthesis landed at `sessions/archive/session-84/session-84-s5-vdd-cohomology-synthesis.md` (326 lines).
- S84 connes / lizzi S-5 syntheses landed at `sessions/archive/session-84/session-84-s5-connes-cohomology-synthesis.md` and `session-84-s5-lizzi-cohomology-synthesis.md`.
- S83 NONFLAT-T-CORRECTION-L2 VERDICT: **PASS** (ratio = 0 EXACT, Cartan-commuting-1-form convention), SHA `676cfc2148eaf7a08160f0bff696a9490b15ce4ed875b9899f49e18e2c28b28f`. The W11-5 gate extends the PASS from fiber (SU(3)) to base (M^4).
- S82 ABELIAN-SUBFACTOR-LACKS-L2-R-PROTECTION theorem registered; provides the "rank-exclusion" half for the W11-3 meta-theorem.
- S84 W10-113/114/115 PASS triplet (HP-parity disjoint corridors, heitsch_ratio = 16.197719); provides the "parity-exclusion" half.
- `canonical_constants.py` has `tau_fold = 0.19`, `Vol_SU3_Haar = 8*sqrt(3)*π^4 ≈ 1349.74`, `J_C2 = 0.933` — all W11 scripts MUST import via `from canonical_constants import *`.

W11 does not block downstream waves; it is self-contained. W11-3 (meta-theorem) outputs feed `permanent-results-registry.md` if PASS.

---

## §W11-1. S85-EPSH-JENSEN-SURVIVAL

1. **Gate ID**: `S85-EPSH-JENSEN-SURVIVAL`
2. **Trigger**: `[VERIFY-THEOREM]`
3. **Classification**: **GEOMETRIC** (Hopf-cyclic 1-cocycle stability under Jensen deformation of the transverse sector of the codim-1 foliation of SU(3))
4. **Agent type**: van-den-dungen-bridge-theorist
5. **Hypothesis**: The Heitsch 1-cocycle representative `[ε_H] ∈ HP^1(A_F)` is not merely non-zero at τ = τ_fold = 0.19 (S83 anchor, heitsch_ratio = 16.197719); it survives the full admissible Jensen range `τ ∈ [0, 0.4]` with strictly bounded-away-from-zero HP¹ norm. If it vanished at any τ in range, `[ε_H]` would be exact somewhere, collapsing the HP^0/HP^1 disjoint corridor locally.
6. **Method** (`computations/s85_w11_epsh_jensen_survival.py`, output `.npz` + `.png`):
    - `from canonical_constants import tau_fold, Vol_SU3_Haar, J_C2`
    - GPU path: `torch.linalg` on 1-cocycle eigenmode computation (matrix sizes ~155,984 at L_max=10; scales to ~20k per-τ eigenreduction). For per-τ Heitsch integral use GPU (`torch 2.9.1+rocm`).
    - CPU fallback: `os.environ['OMP_NUM_THREADS'] = '8'` before numpy import.
    - Scan: 41 τ-values, `τ ∈ {0.00, 0.01, 0.02, ..., 0.40}`.
    - At each τ, construct Jensen-deformed connection 1-form `ω_J(τ)` on the codim-1 foliation of SU(3); compute Heitsch integral `H(τ) = ∫_F ω_J ∧ dω_J` on the fiber; compute `‖[ε_H](τ)‖_{HP^1}` via the heitsch_ratio normalization used in S83-W1-G2.
    - SHA pins:
        - input: `computations/s83_w1_g2_epsilon_h_promotion.npz` — sha256=`<computed-at-runtime>` (pinned in ledger)
        - input: `canonical_constants.py` — sha256=`<computed-at-runtime>`
        - output: `s85_w11_epsh_jensen_survival.npz`, `.png` (monotonicity plot)
7. **Machinery pin (PRDR)**:
    - `N_eval = 41` (τ-grid)
    - `L_max = 10` (fixed; S61 canonical)
    - `scan_range = [0.00, 0.40]`, `step_size = 0.01`
    - `tolerance = 1e-4` (PASS floor on `‖[ε_H](τ)‖`)
    - `scheme = Heitsch-1-cocycle-HP1-norm`
    - `convention = Jensen-deformed-ω_J-transverse`
    - `random_seed = 85011` (for any Monte-Carlo integration inside HP¹ norm)
    - `GPU path = torch.linalg on ROCm (fallback: OMP_NUM_THREADS=8)`
    - cross-check: monotonicity of `d‖[ε_H]‖/dτ` via finite difference (order-4 stencil) at interior τ; at boundaries (τ=0, τ=0.40), use one-sided 3-point stencil.
8. **Expected output 4-tuple**: `(value=min_{τ}‖[ε_H](τ)‖_{HP^1}, scheme=Heitsch-1-cocycle-HP1-norm, convention=Jensen-deformed-ω_J-transverse, L_max=10)`. Anchor sanity: at τ = 0.19 the value must reproduce `16.197719 ± 1e-3` (S83 W1-G2 PASS).
9. **PASS / FAIL / INFO**:
    - **PASS**: `min_{τ ∈ [0,0.4]} ‖[ε_H](τ)‖_{HP^1} > 1e-4` AND sign of `d‖[ε_H]‖/dτ` resolved (strictly monotonic OR resolved extremum)
    - **FAIL**: `∃ τ ∈ [0,0.4]` with `‖[ε_H](τ)‖_{HP^1} < 1e-4` (the class becomes exact somewhere — HP^0/HP^1 disjoint corridor LOCALLY breaks)
    - **INFO**: numerical instability at τ=0 or τ=0.40 endpoints (one-sided derivative ambiguity); report range where monotonicity IS resolved, defer endpoints
10. **Substitution chain** (survival-direction claim, required by `.claude/rules/math-scripts.md`):
    ```
    Definition 1:  H(τ) = ∫_{F=SU(3) cover} ω_J(τ) ∧ dω_J(τ)     [Heitsch 1-cocycle integral]
    Definition 2:  heitsch_ratio(τ) = H(τ) / ||boundary||_{HP^0}   [normalization, S83 anchor]
    Definition 3:  ‖[ε_H](τ)‖_{HP^1} ≡ |heitsch_ratio(τ)|         [HP^1 norm for this representative]
    Step 1:  ‖[ε_H](τ_fold=0.19)‖_{HP^1} = 16.197719             [S83 W1-G2 PASS]
    Step 2:  ω_J(τ) depends smoothly on τ (Jensen deformation is C^∞ in τ by construction)
    Step 3:  H(τ) is a smooth function of τ (integral of smooth forms on compact fiber)
    Step 4:  If H(τ*) = 0 at some τ* ∈ [0, 0.4], then heitsch_ratio(τ*) = 0
             ⇒ [ε_H](τ*) becomes HP^1-exact, HP^0 ∩ HP^1 ≠ {0} LOCALLY
             ⇒ disjoint corridor wall breaks at τ = τ*
    Direction: The gate tests whether H(τ) avoids zero across the range.
               PASS direction = |H(τ)| strictly bounded below by 1e-4.
               FAIL direction = H(τ*) = 0 for some τ* ⇒ parity wall breaks at τ*.
    Conclusion: The gate measures distance from zero-crossing, not sign per se.
                No sign claim is made here — only a magnitude-floor claim.
    ```
11. **Implications**:
    - **PASS**: extends S83 W1-G2's pointwise result to a full τ-corridor survival; elevates HP^0/HP^1 disjoint-corridor wall from "τ_fold-local" to "Jensen-corridor-global". Feeds permanent registry entry (W11-3 meta-theorem).
    - **FAIL**: disjoint corridor is a τ_fold-local accident; meta-theorem (W11-3) must weaken scope to "at τ_fold only". This would not falsify the framework but would constrain claims that the wall is structural-forever.
    - **INFO**: endpoint instability (τ = 0 is the undeformed limit where Jensen is trivial; the Heitsch integral may be ambiguously normalized there). Report analytic limit separately.
12. **Effort**: 3–4 agent-hours.
13. **Substrate framing**: `[ε_H]` is not "a cohomology class living on a manifold"; it is a specific invariant of the substrate's own spectral-triple-generated HP^*(A_F), computed from D_K eigendata. Jensen deformation is not "changing the metric of a Lie group"; it is a 1-parameter family of substrate self-descriptions. Survival of `[ε_H]` under τ-sweep is a statement that the substrate's cyclic-cohomological fingerprint does not cross a vanishing locus as the fabric reorganizes through the fold. If it fails, the substrate develops a local parity-wall defect at a specific fabric-configuration τ*; that defect would be a new topological object of interest in its own right.

---

## §W11-2. S85-S5-CONVERGENCE-AUDIT

1. **Gate ID**: `S85-S5-CONVERGENCE-AUDIT`
2. **Trigger**: `[AUDIT]`
3. **Classification**: **GEOMETRIC** (meta-level consistency check on three independent solo syntheses of the same NCG structural result)
4. **Agent type**: van-den-dungen-bridge-theorist (primary — owns the source synthesis and is canonical NCG translator per `CLAUDE.md` / agent-memory "convention translation" directive)
5. **Hypothesis**: The three S-5 S84 solo syntheses (connes, lizzi, vdd) converge on the same canonical meta-theorem statement for NCG-STRUCTURAL-EXCLUSION. There are at most **convention** / **notation** differences (not substantive disagreements) in scope statements, hypotheses, or conclusion.
6. **Method** (`computations/s85_w11_s5_convergence_audit.py`, output `.md` reconciliation table + `.npz` for any numerical checks):
    - Read all three S-5 files:
        - `sessions/archive/session-84/session-84-s5-connes-cohomology-synthesis.md`
        - `sessions/archive/session-84/session-84-s5-lizzi-cohomology-synthesis.md`
        - `sessions/archive/session-84/session-84-s5-vdd-cohomology-synthesis.md`
    - Extract: (i) meta-theorem statements, (ii) scope hypotheses, (iii) proof sketches, (iv) permanent-registry proposals, (v) cited SHAs for W10-113/114/115 and W2-3.
    - Build a 3-column reconciliation table: one row per substantive claim, three columns for the three agents' formulations, plus a "delta" column marking (a) identical, (b) convention-difference only, (c) scope-difference, (d) substantive disagreement.
    - Classify each row: if ≥1 (c) or (d) → audit FAIL. If only (a) and (b) → audit PASS.
    - Cross-check: verify that all three cite the same W10-114 verdict SHA for parity-exclusion and the same S82 W2-3 SHA for rank-exclusion; mismatched SHAs are automatic (d)-class.
    - This is an analysis script; no heavy linalg. CPU is fine, `OMP_NUM_THREADS=8`.
    - SHA pins:
        - input: three S-5 markdown files (sha256=`<computed-at-runtime>` each)
        - input: `computations/s84_gate_verdicts.txt` (for cross-check of cited SHAs)
        - input: `computations/s82_gate_verdicts.txt`
        - output: `s85_w11_s5_convergence_audit_table.md` and `.npz` (match-vector)
7. **Machinery pin (PRDR)**:
    - `N_eval = number of substantive claims extracted` (determined at script runtime; must be reported in output)
    - `L_max = N/A` (text-extraction audit)
    - `scan_range = N/A`, `step_size = N/A`
    - `tolerance = ZERO substantive disagreements` (boolean)
    - `scheme = three-agent-syntheses-reconciliation`
    - `convention = vdd-canonical-NCG-translation` (vdd is the explicit convention-translator per agent definition)
    - `random_seed = N/A`
    - `GPU path = CPU` (text extraction)
    - classification-rubric pin: delta-classes (a)/(b)/(c)/(d) enumerated above; a row with `status = (d)` triggers FAIL; a row with `status = (c)` (scope difference) triggers FAIL unless the scope difference is explicitly acknowledged and reconciled in one of the three syntheses as equivalent under a named translation.
8. **Expected output 4-tuple**: `(value=n_substantive_disagreements, scheme=three-agent-syntheses-reconciliation, convention=vdd-canonical-NCG-translation, L_max=N/A)`. Expected: `value = 0` (all three agents built from the same W10-113/114/115 + W2-3 substrate).
9. **PASS / FAIL / INFO**:
    - **PASS**: zero (c)- or (d)-class rows; the three-way convergence is certified; meta-theorem W11-3 may proceed with "three-agent-converged" provenance.
    - **FAIL**: ≥1 substantive disagreement (d) or unreconciled scope difference (c); meta-theorem W11-3 must be dispatched in isolation and cannot claim multi-agent convergence.
    - **INFO**: only convention-difference rows (b) but the convention-translation is non-trivial (e.g., one agent uses "HP-parity", another "Z/2-parity", a third "Chern-class parity"); output translation table but no substantive finding.
10. **Substitution chain** (disagreement-count threshold claim):
    ```
    Definition 1:  claim_i^agent = i-th substantive claim in agent's synthesis (i = 1..N_claims, agent ∈ {connes, lizzi, vdd})
    Definition 2:  delta_i ∈ {(a), (b), (c), (d)}  classifies the 3-way comparison of claim_i
    Definition 3:  n_substantive_disagreements = #{i : delta_i ∈ {(c), (d)}}
    Step 1:  PASS threshold: n_substantive_disagreements = 0
    Step 2:  delta_i = (c) or (d) ⇒ contributes +1 to count
             delta_i = (a) or (b) ⇒ contributes +0
    Step 3:  PASS iff sum over i = 0
    Direction: This is a boolean-reducible audit; no signed-quantity direction claim.
               Direction = "zero disagreements" is the PASS boundary.
    Conclusion: The gate asks whether the 3-agent convergence flag in vdd synthesis IV.4
                can be certified. Certification requires hard match on the core meta-theorem,
                not merely a narrative claim that agents agree.
    ```
11. **Implications**:
    - **PASS**: unlocks W11-3 (meta-theorem certification) with 3-agent-converged provenance; strengthens the registry claim from "proposed by vdd" to "triangulated across Connes-formalism / Lizzi-formalism / vdd-bridge-formalism".
    - **FAIL**: meta-theorem proceeds but marked "single-agent-formulated"; substantive disagreement becomes its own open question (what structural hypothesis do the agents actually disagree on?).
    - **INFO**: convention translation table is a useful artifact but does not elevate the meta-theorem's status.
12. **Effort**: 2–3 agent-hours.
13. **Substrate framing**: The three agents are three viewpoints on the same substrate object. Connes sees a spectral-triple axiomatic object; Lizzi sees a regulator-conditional spectral-functional object; vdd sees a Kasparov-product factorized object. If all three viewpoints produce the same conclusion, that is evidence the substrate's cyclic-cohomological structure is robust to observer choice — a framework-internal version of "viewpoint invariance". If they diverge, the substrate has a genuinely viewpoint-dependent feature that needs to be accounted for, not papered over by superficial notational agreement.

---

## §W11-3. S85-NCG-META-EXCLUSION-CERTIFY

1. **Gate ID**: `S85-NCG-META-EXCLUSION-CERTIFY` (referenced elsewhere as `NCG-STRUCTURAL-EXCLUSION`, row 52 of collapsed carry-forward)
2. **Trigger**: `[VERIFY-THEOREM]`
3. **Classification**: **GEOMETRIC** (bivariant K-theory / KK-theory meta-statement unifying two structural exclusions)
4. **Agent type**: van-den-dungen-bridge-theorist (primary; Kasparov bivariant machinery is vdd's native corpus, Paper 01 §2–§4)
5. **Hypothesis**: There exists a single categorical statement in KK / bivariant cyclic-cohomology from which both:
    - **S84-W10-114** parity-exclusion (`[ε_H] ∈ HP^1(A_F) \ image(ch: K_0(A_F) → HP^*(A_F))`; heitsch_ratio = 16.197719, 5 OOM above threshold), AND
    - **S82-W2-3** rank-exclusion (`ABELIAN-SUBFACTOR-LACKS-L2-R-PROTECTION`; `c_2` requires rank-≥2 projections which abelian `C(X)` ⊂ `C^*(G)` lacks)

    emerge as corollaries with independent lemmas. Specifically: both are zero-maps in a **six-term exact sequence** (Cuntz-Quillen bivariant cyclic) or a **Puppe sequence** connecting the finite fiber algebra's K-theory to its cyclic-cohomology target groups.
6. **Method** (`computations/s85_w11_ncg_meta_exclusion_certify.py` + companion `.md` proof sketch):
    - Input: Paper 01 (1811.07824) §2–§4 Kasparov factorization; Connes NCG Thm III.2.5 (Connes-Chern); Cuntz-Quillen bivariant cyclic Six-Term exact sequence; S82 ABELIAN-SUBFACTOR theorem (sha `<S82-pinned>`); S84-W10-114 PASS (sha `<S84-W10-114-pinned>`).
    - Produce categorical skeleton:
        - identify the common functor: `image_ch_ev: K_*(A_F) → HP^*(A_F)` (parity-graded Chern)
        - identify the common zero-map witness: (i) for parity-exclusion, `π_{HP^1} ∘ ch^0 = 0`; (ii) for rank-exclusion, `c_2: K_0(A_B) → H^4(X, Z)` has `c_2 ≡ 0` on abelian `A_B`
        - unify: both are zero-maps obtained by projecting a Chern-class image onto a target group that does not host the required parity / rank → categorical object = "graded image-restriction functor with target-zero lemma"
    - Verify: check that each corollary drops out of the unified statement using only the lemmas marked "independent" (no shared ad-hoc hypothesis beyond "finite-dim A_F" and "Paper 01 factorization on M^4 × SU(3)").
    - Cross-check: search for a third exclusion type (candidate: S71 w_0 asymmetry exclusion) — does it fit the same meta-family? If yes, add as corollary; if no, classify why (different categorical skeleton).
    - sage-compute MCP for symbolic six-term exact sequence verification (Z/2-graded HP^*, entries: K_0, K_1, HP^0, HP^1).
    - SHA pins:
        - input: S82 verdict SHA (sha256=`<computed-at-runtime>`) — pins the rank-exclusion statement
        - input: S84 W10-114 verdict SHA (sha256=`<computed-at-runtime>`) — pins the parity-exclusion statement
        - input: S83 W1-G2 heitsch_ratio = 16.197719 verdict SHA — pins the HP^1 witness norm
        - input: `canonical_constants.py`, three S-5 syntheses (convergence provenance per W11-2)
        - output: `s85_w11_ncg_meta_exclusion_certify_sketch.md` (proof sketch), `.npz` (corollary-status vector), `.png` (categorical diagram)
7. **Machinery pin (PRDR)**:
    - `N_eval = 3` (parity-exclusion, rank-exclusion, candidate-w_0-asymmetry-exclusion) — pre-register which exclusions are tested
    - `L_max = N/A` (meta-theorem is structure-level; uses S83/S84 pinned finite-L results as inputs)
    - `scan_range = {parity, rank, w_0_asymmetry}`, `step_size = N/A` (discrete corollary set)
    - `tolerance = 0` (both named exclusions must drop out as corollaries; w_0 candidate is classified in-or-out without tolerance)
    - `scheme = KK-bivariant-six-term-exact`
    - `convention = Z/2-graded-HP*, Cuntz-Quillen-bivariant`
    - `random_seed = N/A`
    - `GPU path = CPU + sage-compute MCP` (symbolic)
    - proof-sketch pin: meta-theorem statement frozen to the three-clause form in vdd synthesis §II.5 (see `session-84-s5-vdd-cohomology-synthesis.md` line 182) BEFORE the script runs. Any refinement to the statement after the script emits the corollary-status vector is a post-hoc edit per PROHIBITED_ACTIONS §3.
8. **Expected output 4-tuple**: `(value=n_corollaries_derived / n_tested, scheme=KK-bivariant-six-term-exact, convention=Z/2-graded-HP*, L_max=N/A)`. Expected: `value = 2/2` (parity + rank both drop out); w_0_asymmetry candidate classified separately as in-family or new-family.
9. **PASS / FAIL / INFO**:
    - **PASS**: both named exclusions (parity, rank) emerge as corollaries with independent lemmas from a single structural statement; proof sketch consistent with six-term exact sequence framework; three-agent convergence (W11-2 PASS) provides reinforcing provenance.
    - **FAIL**: one exclusion requires an ad-hoc hypothesis not shared with the other; the meta-theorem does not unify them in the proposed form; the statement must be weakened to two independent theorems (each registered separately).
    - **INFO**: proof sketch is incomplete (e.g., six-term exact sequence closure requires an additional lemma not in current corpus); the categorical **skeleton** is resolved but the full sketch is deferred — meta-theorem provisionally accepted pending later fill-in; registered with status PROPOSED-WITH-SKELETON.
10. **Substitution chain** (unification claim):
    ```
    Definition 1:  Excl_parity  ≡  [ε_H] ∉ image(ch^0: K_0(A_F) → HP^0(A_F))     [W10-114]
    Definition 2:  Excl_rank    ≡  c_2(A_B → X) = 0 for A_B abelian ⊂ C^*(G)     [S82 W2-3]
    Definition 3:  Unified_Meta ≡  ∀ (ch_target, source), image_Chern(source) ⊂ parity-compatible-subgroup-of-target
                                   and the restriction to "forbidden" sub-target = 0
    Step 1:  Apply Unified_Meta with (source = K_0(A_F), target = HP^*(A_F)):
             image(ch^0) ⊂ HP^0(A_F), so restriction to HP^1 = 0 ⇒ Excl_parity holds.   ✓
    Step 2:  Apply Unified_Meta with (source = K_0(A_B), target = H^*(X)):
             image(ch) on rank-1 projections sits in H^{even}(X), and the second Chern
             class c_2 ∈ H^4(X) requires rank-≥2 Bott generators. Abelian A_B has no
             rank-≥2 minimal projections (by definition of commutative C*-algebra
             spectrum = topological space, K_0(C(X)) = K^0(X) generated by line bundles).
             ⇒ c_2-restriction = 0 ⇒ Excl_rank holds.   ✓
    Step 3:  Both (Step 1) and (Step 2) follow from the single statement Unified_Meta
             with independent specializations of (source, target). No ad-hoc hypothesis.
             ⇒ unification PASS direction.
    Direction: PASS direction = both corollaries derive cleanly.
               FAIL direction = one requires an ad-hoc hypothesis (e.g., "and also assume A_F is finite-dim" that Step 2 does not use), making unification forced.
    Conclusion: The meta-theorem is a categorical statement, not a numerical claim.
                No sign/magnitude direction applies. The verdict depends on categorical
                derivation cleanness, pre-registered as PASS iff BOTH exclusions drop
                out without shared ad-hoc hypotheses.
    ```
11. **Implications**:
    - **PASS**: promote NCG-STRUCTURAL-EXCLUSION META-THEOREM to permanent-results-registry with dual-SHA provenance (W10-114 parity + S82 W2-3 rank); the framework now exhibits a **family** of K-theoretic structural walls, not two isolated accidents. Downstream gates can invoke the family — e.g., a new exclusion proposed for any (source, target) pair gets first-line classified as in-family or new-family.
    - **FAIL**: both exclusions remain individually registered; the observation in vdd synthesis §IV.2 ("the framework produces K-structural exclusions under Paper 01 factorization" is a pattern with two instances, not one) is weakened — the two instances share only surface traits, not categorical common structure.
    - **INFO**: skeleton-only registration; feeds a future session's full-sketch gate. Candidate w_0_asymmetry exclusion's in-family status is recorded separately.
12. **Effort**: 6–8 agent-hours (may span two sessions if categorical unification proves resistant — per vdd synthesis V.3 effort estimate).
13. **Substrate framing**: Structural exclusions are not artifacts of representation-theoretic bookkeeping; they are walls in the substrate's state space. The substrate cannot produce `[ε_H]` as a K-theoretic index of any elliptic operator built from its spectral triple (parity wall), and it cannot produce `c_2 ≠ 0` from an abelian subfactor of its gauge module (rank wall). A meta-theorem unifying them is a statement that the substrate's K-theoretic self-description has a common categorical symmetry constraining what cohomological fingerprints it can exhibit. The substrate is the thing; the exact sequence is how it organizes its own invariants.

---

## §W11-4. S85-FIBER-GROUP-PARITY-CLASSIFY

1. **Gate ID**: `S85-FIBER-GROUP-PARITY-CLASSIFY` (row 118 of collapsed carry-forward)
2. **Trigger**: `[VERIFY-THEOREM]`
3. **Classification**: **GEOMETRIC** (shriek-map π_! parity action on HP^* as a function of fiber-group dimension mod 2)
4. **Agent type**: van-den-dungen-bridge-theorist (Paper 01 shriek formula is vdd's native result)
5. **Hypothesis**: For a Riemannian submersion `π: E → M` with compact fiber-group `G`, the shriek-map `π_!: K^*(E) → K^{*-dim_R G}(M)` preserves Z/2-parity of HP^* representatives **iff** `dim_R G ≡ 0 (mod 2)`. Specifically: SU(3) (dim 8) and SU(3)×U(1) (dim 9? — test case) and G_2 (dim 14) preserve corridor labels; SU(2) (dim 3), SO(3) (dim 3) reshuffle them. The SU(3) choice is thus not arbitrary — it is one of a classifiable subset.
6. **Method** (`computations/s85_w11_fiber_group_parity_classify.py`, output `.npz` + `.md` classification table):
    - `from canonical_constants import *` — even though no framework constants appear in the parity table itself, the audit MUST import for compliance.
    - Enumerate candidate fiber groups:
        - SU(2) — dim_R = 3
        - SU(3) — dim_R = 8 (canonical framework choice)
        - SU(2)×SU(2) — dim_R = 6
        - SU(3)×U(1) — dim_R = 9 (standard-model candidate)
        - SO(3) — dim_R = 3
        - SO(4) — dim_R = 6
        - SO(5) — dim_R = 10
        - Spin(5) — dim_R = 10
        - G_2 — dim_R = 14
        - F_4 — dim_R = 52
        - Sp(1) — dim_R = 3
        - Sp(2) — dim_R = 10
    - For each, apply Paper 01 shriek formula: `π_!: K^*(E) → K^{*-dim_R G}(M)`. The induced map on HP^* shifts degree by `dim_R G mod 2`:
        - If `dim_R G ≡ 0 (mod 2)`: π_!: HP^0 → HP^0, HP^1 → HP^1 (parity preserved)
        - If `dim_R G ≡ 1 (mod 2)`: π_!: HP^0 → HP^1, HP^1 → HP^0 (parity flipped)
    - Classify each row: **PRESERVE** / **FLIP**.
    - Cross-check via direct Gysin sequence on a representative example (e.g., explicit SU(2)-bundle over S^4 and SU(3)-bundle over S^8) using sage-compute.
    - SHA pins: `canonical_constants.py`, Paper 01 shriek formula (cited, not file-hashed), Lie-group dimension table (from standard reference; cite and hash a local copy).
7. **Machinery pin (PRDR)**:
    - `N_eval = 12` (candidate fiber groups enumerated above, frozen at plan time)
    - `L_max = N/A`
    - `scan_range = {12 named groups}`, `step_size = N/A`
    - `tolerance = 0` (classification is integer-mod-2, no tolerance)
    - `scheme = Paper-01-shriek-HP*-parity`
    - `convention = dim_R-mod-2`
    - `random_seed = N/A`
    - `GPU path = CPU + sage-compute` (symbolic Gysin)
    - cross-check pin: compute π_! on `SU(2)-Hopf-bundle S^7 → S^4` (dim_R = 3) as explicit flip-witness; compute π_! on `SU(3)-principal-bundle over S^8` (dim_R = 8) as explicit preserve-witness. Both witnesses use standard Gysin, not Paper 01 abstract formula, providing independent cross-check.
8. **Expected output 4-tuple**: `(value=n_flip + n_preserve == 12 AND SU(3) ∈ preserve, scheme=Paper-01-shriek-HP*-parity, convention=dim_R-mod-2, L_max=N/A)`. Expected: 7 PRESERVE (SU(3), SU(2)×SU(2), SO(4), SO(5), Spin(5), G_2, F_4, Sp(2)) + 5 FLIP (SU(2), SU(3)×U(1), SO(3), Sp(1), candidate not-yet-listed). The count split depends on `dim_R mod 2` for each; any count error indicates a classification error.
9. **PASS / FAIL / INFO**:
    - **PASS**: SU(3) AND SU(3)×U(1) both classified correctly (SU(3) = PRESERVE since dim=8, SU(3)×U(1) = FLIP since dim=9) AND at least one alternative candidate FLIPS (provides the discriminator that rules out odd-dim fiber groups as drop-in replacements). This matches vdd synthesis V.5 PASS criterion.
    - **FAIL**: all candidates PRESERVE (no discriminator — meaning parity is not a fiber-group constraint). Note: this is mathematically impossible (odd-dim groups exist), so a true FAIL here indicates a script bug, not a physical result.
    - **INFO**: parity analysis extends to non-simply-connected covers with a subtlety not captured by dim_R alone — e.g., SO(3) vs Spin(3) = SU(2) both have dim_R = 3 but differ in π_1; the HP-parity shift is the same but other K-theoretic properties (Stiefel-Whitney classes) differ. Report as a caveat subsection but classify per dim_R for the main table.
10. **Substitution chain** (parity-shift direction claim):
    ```
    Definition 1:  π_!: K^j(E) → K^{j - dim_R G}(M)   [Gysin / shriek push-forward, Paper 01]
    Definition 2:  HP^k(A) = periodic cyclic cohomology, Z/2-graded (k = 0, 1)
    Definition 3:  image under Chern:  K^j → HP^{j mod 2}
    Step 1:  π_! shifts K-degree by dim_R G:
             π_!: K^0(E) → K^{-dim_R G}(M) = K^{(-dim_R G) mod 2}(M)
    Step 2:  Z/2-reduction of shifted degree:
             j = 0 → j - dim_R G (mod 2) = -dim_R G (mod 2) = dim_R G (mod 2)
    Step 3:  Two cases:
             Case A: dim_R G ≡ 0 (mod 2) ⇒ π_! sends HP^0 → HP^0, HP^1 → HP^1. PARITY PRESERVED.
             Case B: dim_R G ≡ 1 (mod 2) ⇒ π_! sends HP^0 → HP^1, HP^1 → HP^0. PARITY FLIPPED.
    Step 4:  SU(3): dim_R = 8, 8 mod 2 = 0 ⇒ PRESERVE.                       [Case A]
             SU(2): dim_R = 3, 3 mod 2 = 1 ⇒ FLIP.                             [Case B]
             SU(3) × U(1): dim_R = 8 + 1 = 9, 9 mod 2 = 1 ⇒ FLIP.              [Case B]
             G_2: dim_R = 14, 14 mod 2 = 0 ⇒ PRESERVE.                         [Case A]
             F_4: dim_R = 52, 52 mod 2 = 0 ⇒ PRESERVE.                         [Case A]
             Sp(2): dim_R = 10, 10 mod 2 = 0 ⇒ PRESERVE.                       [Case A]
             Sp(1): dim_R = 3, 3 mod 2 = 1 ⇒ FLIP.                             [Case B]
             SO(3): dim_R = 3, 3 mod 2 = 1 ⇒ FLIP.                             [Case B]
             SO(4): dim_R = 6, 6 mod 2 = 0 ⇒ PRESERVE.                         [Case A]
             SO(5): dim_R = 10, 10 mod 2 = 0 ⇒ PRESERVE.                       [Case A]
             Spin(5): dim_R = 10, 10 mod 2 = 0 ⇒ PRESERVE.                     [Case A]
             SU(2) × SU(2): dim_R = 6, 6 mod 2 = 0 ⇒ PRESERVE.                 [Case A]
    Direction: PRESERVE class = dim_R ≡ 0 (mod 2); FLIP class = dim_R ≡ 1 (mod 2).
               Pre-registered: SU(3) ∈ PRESERVE, SU(2) ∈ FLIP.
    Conclusion: The parity classification is deterministic given dim_R. The test is whether
                the framework's canonical SU(3) choice is the PRESERVE class (it is), and
                whether an alternative (e.g., SU(3)×U(1)) breaks that preservation (it does).
                This pins SU(3) as non-arbitrary WITHIN the submersion-preservation constraint.
    ```
11. **Implications**:
    - **PASS**: SU(3)'s disjoint-corridor label stability under π_! is not an accident; it is a dim_R-parity consequence. SU(3)×U(1) FLIPS labels — so the standard-model extension (Connes-Chamseddine A_F with the full gauge group reconstructed from its bundle) introduces a parity flip under shriek unless the base compensates. This is a non-trivial geometric constraint on fiber-group substitution, potentially restricting any proposed extension of the framework to larger fiber groups.
    - **FAIL**: script bug (see rationale in §9).
    - **INFO**: non-simply-connected-cover subtlety feeds a future audit of whether Spin-structure on the base interacts with the shriek-parity (vdd Paper 02 pseudo-Riemannian spectral triples relevant here).
12. **Effort**: 2–3 agent-hours.
13. **Substrate framing**: Fiber-integration is how the substrate hands off its internal structure to the emergent base. The shriek map π_! is the substrate's own integration measure on its internal coordinates. If the fiber group were odd-dimensional, the substrate's cohomological fingerprint would invert under fiber integration — what is primary (HP^0) on the total space becomes secondary (HP^1) on the base, and vice versa. SU(3)'s 8-dimensional real structure is the smallest simple non-abelian group that preserves corridor labels (SU(2) at dim 3 does not). The framework's SU(3) is not arbitrary; it is the smallest simple fiber group compatible with corridor-preserving shriek integration. This is a non-trivial internal consistency constraint, not a postulate.

---

## §W11-5. S85-BASE-PONTRYAGIN-PARITY-PRESERVE

1. **Gate ID**: `S85-BASE-PONTRYAGIN-PARITY-PRESERVE` (extends S83-NONFLAT-T-CORRECTION-L2; row 120 of collapsed carry-forward)
2. **Trigger**: `[VERIFY-THEOREM]`
3. **Classification**: **GEOMETRIC** (Kasparov-product parity preservation under non-zero base curvature — extends S83 from fiber (SU(3)) to base (M^4))
4. **Agent type**: van-den-dungen-bridge-theorist
5. **Hypothesis**: The Kasparov-product factorization `[D] = [D_F] ⊗_{C(M)} [D_M]` preserves Z/2-parity of HP^* representatives **even when M^4 has non-zero Ricci / Pontryagin density**. Concretely: on a FRW-like non-flat base with metric `g_M` producing `p_1(TM^4) = (1/8π²) tr(R ∧ R) ≠ 0`, the parity shift `deg(ch([D])) - deg(ch([D_F]))` remains zero (mod 2), matching the flat-base result S83 extended by non-flat O'Neill / connection-compatibility corrections.
6. **Method** (`computations/s85_w11_base_pontryagin_parity_preserve.py`, output `.npz` + `.png`):
    - `from canonical_constants import tau_fold, Vol_SU3_Haar, J_C2, planck_ns` (and any M^4-curvature scalars already pinned).
    - Construct a 1-parameter family of FRW-like base metrics: `g_M(a) = -dt² + a(t)² δ_ij dx^i dx^j`; scan scale-factor curvature through two regimes:
        - Regime 1: small curvature, `R_M^4 → 0` (recovers S83 flat-base PASS)
        - Regime 2: substrate-relevant curvature, `R_M^4` at physical values at τ_fold
    - At each scale-factor, compute:
        - base Pontryagin density `p_1(TM^4) = (1/8π²) tr(R_M^4 ∧ R_M^4)` (2-form on M^4 integrated)
        - fiber Pontryagin `p_1(T^V)` on Jensen-SU(3) (this is the S83 PASS anchor = 0 on Cartan)
        - total-space `p_1(TE) = π*p_1(TM^4) + p_1(T^V)` (Chern-Weil additivity on the Riemannian submersion, with O'Neill correction terms A and T)
        - parity-shift `δ_parity = [deg(ch([D_E])) - deg(ch([D_F])) - deg(ch([D_M]))] mod 2`
    - Cross-check: A-tensor and T-tensor O'Neill invariants evaluated at each base-curvature value — verify that non-zero O'Neill components do not introduce parity-flip terms. Per S61 O'Neill audit, A = T = 0 at τ_fold on Jensen-SU(3), so the only curvature source in the total-space is the base; this gate tests whether that base-curvature contribution is parity-preserving.
    - GPU path: `torch.linalg` for Riemann-tensor contractions on M^4 (4×4 indices, tiny; CPU is also fine).
    - SHA pins:
        - input: `s83_w2_g24_nonflat_t_correction_l2.py` and its `.npz` output (baseline flat-base PASS; sha256=`<computed-at-runtime>`)
        - input: `canonical_constants.py`
        - input: S61 O'Neill A-tensor / T-tensor artifacts (sha256=`<computed-at-runtime>`)
        - output: `s85_w11_base_pontryagin_parity_preserve.npz`, `.png` (δ_parity vs base-curvature plot)
7. **Machinery pin (PRDR)**:
    - `N_eval = 11` (scale-factor grid: 11 points sampling low → physical curvature)
    - `L_max = N/A` (eigenvalue reduction not needed; this is a 2-form cohomology computation)
    - `scan_range = {scale-factor a ∈ [a_low, a_physical]}`, `step_size = log-spaced`
    - `tolerance = 0` (parity shift is integer-mod-2)
    - `scheme = first-Pontryagin-plus-Chern-Weil-submersion`
    - `convention = Riemannian-submersion-with-non-flat-base`
    - `random_seed = 85054`
    - `GPU path = torch.linalg or CPU` (tiny-tensor; either works)
    - O'Neill pin: `A_tensor = T_tensor = 0` on Jensen-SU(3) at τ_fold (per S61 verdict); this is an INPUT hypothesis, not re-computed here.
    - base-metric pin: FRW-like, spatially flat, a(t) the single degree of freedom; the test does NOT require a specific a(t) evolution, only non-zero `R_M^4`. Pick a(t) = exp(H t) with H scanning to produce curvature sweep.
8. **Expected output 4-tuple**: `(value=max_over_scan |δ_parity|, scheme=first-Pontryagin-plus-Chern-Weil-submersion, convention=Riemannian-submersion-with-non-flat-base, L_max=N/A)`. Expected: `value = 0` (parity preserved throughout scan — extends S83 PASS).
9. **PASS / FAIL / INFO**:
    - **PASS**: `max_{scan} |δ_parity| = 0`, which is equivalent to `δ_parity = 0` EXACT at every sampled base-curvature. The Kasparov-product factorization preserves Z/2-parity on curved base.
    - **FAIL**: `∃ scan-point` with `|δ_parity| = 1`. Non-zero base curvature introduces a parity-flip term, breaking the disjoint-corridor wall under submersion with non-flat base. This would be a structural discovery: the Paper 01 factorization's parity-preservation relies on a hypothesis that fails on curved base.
    - **INFO**: A-tensor or T-tensor non-zero at some scan-point (O'Neill pin violated off τ_fold); the computation can still be performed but the parity-preservation now includes an O'Neill-dependent compensation term. Report the compensation structure but defer PASS/FAIL adjudication.
10. **Substitution chain** (parity-preservation direction claim):
    ```
    Definition 1:  p_1(TE) = (1/8π²) tr(R_E ∧ R_E) ∈ H^4(E, R)          [first Pontryagin on total space]
    Definition 2:  [D] = [D_F] ⊗_{C(M)} [D_M] ∈ KK(C_0(E), C)           [Paper 01 Main Theorem]
    Definition 3:  ch([D]) = ch([D_F]) ∪ ch([D_M])                      [Chern is multiplicative under Kasparov ⊗_C(M)]
    Definition 4:  deg_{HP^*}(ch(·)) ∈ {0, 1} is the Z/2-grading of the HP^* representative
    Definition 5:  δ_parity = deg(ch([D])) - (deg(ch([D_F])) + deg(ch([D_M]))) mod 2
    Step 1:  By Chern multiplicativity (Def 3) on even-dim K-theory under cup:
             deg(ch([D])) = (deg(ch([D_F])) + deg(ch([D_M]))) mod 2
             ⇒ δ_parity = 0 IDENTICALLY if cup is Z/2-additive.
    Step 2:  Cup product on HP^* is Z/2-graded: HP^i ⊗ HP^j → HP^{i+j mod 2}.
             ⇒ Z/2-additivity holds. δ_parity = 0 at the algebraic level.
    Step 3:  Non-flat base introduces:
             R_E = R_F + π*R_M + A-tensor-correction + T-tensor-correction
             (Gauss-Codazzi on Riemannian submersion; O'Neill 1966 formula)
    Step 4:  Under O'Neill pin A = T = 0 (S61 PASS at τ_fold):
             R_E = R_F ⊕ π*R_M   (direct-sum of fiber and pulled-back-base curvatures)
             ⇒ tr(R_E ∧ R_E) = tr(R_F ∧ R_F) + tr(π*R_M ∧ π*R_M) + 2 tr(R_F ∧ π*R_M)
             The cross-term tr(R_F ∧ π*R_M) integrates to zero on the fiber (fiber has
             even dimension and R_F is a 2-form on the fiber, π*R_M is a 2-form on the base;
             their product integrates-fiber-wise to p_1(TM) × ∫_F tr(R_F), which is
             even-integer-class and parity-even).
             ⇒ p_1(TE) = p_1(T^V) + π*p_1(TM) EXACT up to parity.
    Step 5:  HP-parity of each summand:
             - p_1(T^V) at τ_fold = 0 on Cartan (S83 PASS), so it contributes HP^0 (trivial).
             - π*p_1(TM^4): Pontryagin is a 4-form, integrates to integer, parity-even.
             ⇒ deg(ch([D])) = deg(ch([D_F])) + deg(ch([D_M])) mod 2 PRESERVED.
    Step 6:  δ_parity = 0 on all scan points where A-tensor = T-tensor = 0.
    Direction: PASS direction = δ_parity = 0. Preserved by Chern multiplicativity + O'Neill vanishing.
               FAIL direction = δ_parity = 1. Requires a specific mechanism to generate an odd-parity
               contribution from base curvature, which the Chern-Weil additivity does NOT provide.
    Conclusion: The test is NOT whether non-flat base breaks parity (the substitution chain shows
                it cannot, under the O'Neill pin). The test IS whether the numerical implementation
                respects this structure across a range of base-curvatures OR whether an
                implementation artifact (e.g., regulator asymmetry, discrete-integration roundoff)
                introduces a spurious parity shift. This is a numerical-robustness gate on a
                structurally-forced result.
    ```
11. **Implications**:
    - **PASS**: S83's flat-base result extends to curved base, certifying that the Kasparov-product factorization's parity-preservation is not a flat-base accident. Meta-theorem (W11-3) gains a curvature-robustness clause. Canonical entry in permanent-registry can be upgraded from "flat-base only" to "Riemannian-submersion with A=T=0 O'Neill".
    - **FAIL**: new structural discovery — the framework's HP^0/HP^1 disjoint corridor wall is a flat-base phenomenon, breaking when M^4 curves. This would change the scope of the NCG-STRUCTURAL-EXCLUSION meta-theorem (W11-3) and potentially require the Connes-Chamseddine ACM formalism to be amended with a base-curvature parity-correction term.
    - **INFO**: O'Neill A or T non-zero off τ_fold; the gate becomes a compensation-mapping exercise rather than a PASS/FAIL threshold. Documents what compensation terms appear.
12. **Effort**: 4–5 agent-hours.
13. **Substrate framing**: The base M^4 is not a container; it is the substrate's emergent large-scale description. When M^4 curves, that curvature is itself a substrate reorganization — not a change to "space" as an independent object. The test asks: does the substrate's internal cyclic-cohomological fingerprint survive a global reorganization of its own large-scale description? If yes (PASS), the substrate's internal self-description is invariant under base-curvature emergence — a strong internal-consistency statement. If no (FAIL), the substrate's fingerprint is linked to base-flatness, which is physically implausible given observed FRW-like curvature, and would force a framework amendment. S83 showed the fiber (SU(3)) Pontryagin is parity-preserving; W11-5 closes the loop on the base side.

---

## Wave W11 → Wave W12 Decision Point

W11 does not block W12 (gen-physicist-origin wave). Batch-2 concurrency places W12 and W11 in the same dispatch window per the partition manifest. W11 outputs, however, **feed two permanent-registry landings** if PASS:

- W11-3 PASS → `NCG-STRUCTURAL-EXCLUSION META-THEOREM` registered in `sessions/permanent-results-registry.md` §VII.P (new section: "K-theoretic structural exclusions in NCG").
- W11-5 PASS → extend the S83-NONFLAT-T-CORRECTION-L2 row in registry from "Cartan only" / "fiber only" to "full submersion with non-flat base".

These registry landings are not themselves W11 gates; they are post-wave bookkeeping triggered only by PASS outcomes.

---

## Wave W11 Machinery-Enumeration Pin

Per `.claude/rules/epistemic-discipline.md` §Pre-Registration Completeness, every gate-relevant machinery parameter is pinned at plan-time. PRDR dry-run outcome for each gate:

| Gate | Free param enumerated | Pin / disposition |
|:-----|:----------------------|:------------------|
| W11-1 | τ-grid | `N_eval=41`, `τ ∈ [0, 0.4] step 0.01` |
| W11-1 | HP^1 norm normalization | `heitsch_ratio convention` (S83 W1-G2 anchor) |
| W11-1 | Derivative stencil | order-4 interior, 3-point one-sided at endpoints |
| W11-1 | MC seed (if needed) | `random_seed = 85011` |
| W11-2 | Claim-extraction grain | substantive-claim-level, delta-classes (a)/(b)/(c)/(d) |
| W11-2 | Cross-check SHAs | S82 W2-3 + S84 W10-114 must match across all 3 syntheses |
| W11-3 | Corollary set | `N_eval = 3` (parity, rank, w_0-candidate) |
| W11-3 | Categorical framework | Cuntz-Quillen bivariant six-term exact |
| W11-3 | Meta-theorem text | frozen to vdd synthesis §II.5, line 182 (post-hoc edits forbidden) |
| W11-4 | Fiber-group list | 12 candidates frozen above |
| W11-4 | Cross-check witnesses | SU(2)-Hopf S^7→S^4 (FLIP), SU(3)-bundle over S^8 (PRESERVE) |
| W11-5 | Scale-factor grid | `N_eval = 11`, log-spaced |
| W11-5 | O'Neill pin | `A = T = 0` (S61-inherited; re-verified at τ_fold by reading S61 output, NOT re-computed) |
| W11-5 | Base metric family | FRW-like spatially-flat, `a(t) = exp(H t)`, H = scan variable |

**PRU audit disposition**: Each gate has all machinery parameters pinned or explicitly marked N/A (for classification / audit gates). Zero D_PRU_raw at plan-time.

---

## Wave W11 Input-SHA Ledger

Per `.claude/rules/gate-verdicts.md` §Pre-Registration Protocol, every script MUST log input SHA-256 of every file it reads in the first 20 lines of stdout. Pre-computed SHAs (to be inserted by the runtime from `canonical_sha_ledger.json`):

| Gate | Input file | Pre-computed SHA | Runtime |
|:-----|:-----------|:-----------------|:-------:|
| W11-1 | `computations/s83_w1_g2_epsilon_h_promotion.npz` | (from ledger) | static |
| W11-1 | `computations/canonical_constants.py` | (from ledger) | static |
| W11-2 | `sessions/archive/session-84/session-84-s5-connes-cohomology-synthesis.md` | `<runtime>` | dynamic |
| W11-2 | `sessions/archive/session-84/session-84-s5-lizzi-cohomology-synthesis.md` | `<runtime>` | dynamic |
| W11-2 | `sessions/archive/session-84/session-84-s5-vdd-cohomology-synthesis.md` | `<runtime>` | dynamic |
| W11-2 | `computations/s84_gate_verdicts.txt` | `<runtime>` | dynamic |
| W11-2 | `computations/s82_gate_verdicts.txt` | `<runtime>` | dynamic |
| W11-3 | `computations/s82_gate_verdicts.txt` (W2-3 SHA extraction) | `<runtime>` | dynamic |
| W11-3 | `computations/s84_gate_verdicts.txt` (W10-114 SHA extraction) | `<runtime>` | dynamic |
| W11-3 | `computations/s83_gate_verdicts.txt` (W1-G2 heitsch_ratio SHA) | `<runtime>` | dynamic |
| W11-3 | `sessions/archive/session-84/session-84-s5-vdd-cohomology-synthesis.md` (§II.5 meta-theorem text) | `<runtime>` | dynamic |
| W11-4 | `computations/canonical_constants.py` | (from ledger) | static |
| W11-4 | Lie-group dimension table (local copy) | `<runtime>` | static-once-written |
| W11-5 | `computations/s83_w2_g24_nonflat_t_correction_l2.py` | (from ledger) | static |
| W11-5 | `computations/s83_w2_g24_nonflat_t_correction_l2.npz` | (from ledger) | static |
| W11-5 | `computations/canonical_constants.py` | (from ledger) | static |
| W11-5 | S61 O'Neill artifact (`.npz`) | (from ledger) | static |

**Output SHA schema**: Each `.npz` + `.md` + `.png` output produces a `closure_sha256` computed from the ordered input-pin map (per S81+ verdict-line discipline). That closure SHA appears in `computations/s85_gate_verdicts.txt` as the `sha256=<closure>` field.

---

## Verdict-Line Templates (to be appended by each script to `computations/s85_gate_verdicts.txt` upon completion)

```
S85-EPSH-JENSEN-SURVIVAL: PASS|FAIL|INFO -- value=<min_norm> scheme=Heitsch-1-cocycle-HP1-norm convention=Jensen-deformed-ω_J-transverse L_max=10 sha256=<closure_64_hex>
S85-S5-CONVERGENCE-AUDIT: PASS|FAIL|INFO -- value=<n_substantive_disagreements> scheme=three-agent-syntheses-reconciliation convention=vdd-canonical-NCG-translation L_max=N/A sha256=<closure_64_hex>
S85-NCG-META-EXCLUSION-CERTIFY: PASS|FAIL|INFO -- value=<n_corollaries_derived>/<n_tested> scheme=KK-bivariant-six-term-exact convention=Z/2-graded-HP* L_max=N/A sha256=<closure_64_hex>
S85-FIBER-GROUP-PARITY-CLASSIFY: PASS|FAIL|INFO -- value=<n_preserve>+<n_flip>=<total>,SU3_in_preserve=<bool> scheme=Paper-01-shriek-HP*-parity convention=dim_R-mod-2 L_max=N/A sha256=<closure_64_hex>
S85-BASE-PONTRYAGIN-PARITY-PRESERVE: PASS|FAIL|INFO -- value=<max_delta_parity> scheme=first-Pontryagin-plus-Chern-Weil-submersion convention=Riemannian-submersion-with-non-flat-base L_max=N/A sha256=<closure_64_hex>
```

Each verdict line MUST carry full 64-char hexdigest `closure_sha256` computed from `closure_hash(ordered_input_pin_map)` per S81+ discipline (`computations/_consolidate_intake.py` rejects shorter SHAs).

---

## Cross-references to upstream session artifacts

- S61 O'Neill A-tensor / T-tensor PASS (A = T = 0 EXACT on Jensen-SU(3) at τ_fold)
- S82 ABELIAN-SUBFACTOR-LACKS-L2-R-PROTECTION PASS (`s82_w2_3_*` verdict)
- S83-W1-G2 `ε_H` 1-cocycle promotion PASS (heitsch_ratio = 16.197719 at τ_fold, norm in HP^1)
- S83-W2-G24 NONFLAT-T-CORRECTION-L2 PASS (ratio = 0 EXACT, fiber Pontryagin on Cartan)
- S84-W10-113/114/115 HP-parity disjoint corridor PASS triplet (W10-113 atlas purity, W10-114 parity-exclusion of `[ε_H]` at 5 OOM, W10-115 GV 3-form stencil match at RATIO = 1.000)
- `researchers/Van-den-Dungen/` Paper 01 (1811.07824) — Kasparov product factorization on submersions; Paper 05 (1405.5368) — globally non-trivial almost-commutative manifolds; Paper 06 (1204.0328) — ACM review

---

**End of Wave W11 plan.**
